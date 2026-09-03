#!/usr/bin/env python3
"""DeepSeek V4 Flash: dump what dot positions hold, per hyper-connection stream.

Distributed twin of ``dump_dot_residuals_hf.py`` built on ``extract_dsv4.py``'s
loader and hooks. For every item in a fixed-k config it records, at every block,
the raw post-block mHC residual [4, 4096] at all filler positions, the last
question token, the answer cue, and the generation position; the model-native
collapsed residual (``hc_head``); and the logit-lens entropy of the collapsed
residual. Rank 0 writes one tensor file. Attention is handled separately.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import torch
import torch.distributed as dist
from safetensors.torch import load_model
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src")); sys.path.insert(0, str(REPO / "scripts"))
from extract_dsv4 import barrier, capture_layers, collapse_streams, distributed_setup, filler_placement_for_task, local_unembed  # noqa: E402
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt-path", type=Path, required=True); p.add_argument("--model-config", type=Path, required=True)
    p.add_argument("--reference-code-dir", type=Path, required=True); p.add_argument("--examples-config", type=Path, required=True)
    p.add_argument("--filler-length", type=int, default=50); p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--max-items", type=int, default=0); p.add_argument("--max-seq-len", type=int, default=1280)
    p.add_argument("--process-group-timeout-minutes", type=int, default=60)
    args = p.parse_args()

    rank, local_rank, world_size = distributed_setup(args.process_group_timeout_minutes)
    if world_size != 4:
        raise SystemExit("converted checkpoint requires world_size=4")
    torch.set_default_dtype(torch.bfloat16); torch.manual_seed(42)
    sys.path.insert(0, str(args.reference_code_dir.resolve())); sys.path.insert(0, str(args.reference_code_dir.resolve().parent / "encoding"))
    from encoding_dsv4 import encode_messages  # type: ignore
    from model import ModelArgs, Transformer  # type: ignore
    model_args = ModelArgs(**json.loads(args.model_config.read_text())); model_args.max_batch_size = 1; model_args.max_seq_len = args.max_seq_len
    with torch.device("cuda"):
        model = Transformer(model_args)
    load_model(model, str(args.ckpt_path / f"model{rank}-mp{world_size}.safetensors"), strict=False); model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.ckpt_path); torch.set_default_device("cuda"); barrier()

    cfg = json.loads(args.examples_config.read_text()); items = cfg["examples"][: args.max_items or None]
    task = cfg.get("task_type", "variable_binding"); K = args.filler_length
    L = len(model.layers); positions_n = K + 3
    resid = torch.zeros(len(items), L, positions_n, 4, 4096, dtype=torch.bfloat16) if rank == 0 else None
    collapsed = torch.zeros(len(items), L, positions_n, 4096, dtype=torch.bfloat16) if rank == 0 else None
    entropy = torch.zeros(len(items), L, positions_n) if rank == 0 else None
    meta = []
    with torch.inference_mode():
        for n, ex in enumerate(items):
            msgs = build_messages(cfg["few_shot"], ex, cfg["filler_type"], K, task_type=task)
            _, al = render_and_align(tokenizer, encode_messages, msgs, cfg["filler_type"], K, filler_placement=filler_placement_for_task(task))
            fabs = al.filler_token_indices; cue = al.answer_cue_token_indices[-1]; gen = al.generation_position
            q_last = next(i for i in range(fabs[0] - 1, 0, -1) if al.token_strings[i].strip().endswith("?"))
            positions = fabs + [q_last, cue, gen]
            tokens = torch.tensor([al.input_ids], dtype=torch.long, device="cuda")
            with capture_layers(model, list(range(L)), positions) as cap:
                model.forward(tokens, 0)
            for l in range(L):
                raw = cap[l][0]                                   # [P, 4, 4096]
                col = collapse_streams(model, cap[l])[0]          # [P, 4096]
                local = local_unembed(model, col.float())         # [P, vocab_shard]
                shards = [torch.empty_like(local) for _ in range(world_size)]; dist.all_gather(shards, local.contiguous())
                logits = torch.cat(shards, -1); lp = torch.log_softmax(logits, -1); ent = -(lp.exp() * lp).sum(-1)
                if rank == 0:
                    resid[n, l] = raw.cpu(); collapsed[n, l] = col.cpu(); entropy[n, l] = ent.cpu()
            meta.append({"id": ex["id"], "answer": ex["answer"], "expected_intermediates": ex["expected_intermediates"], "n_tokens": len(al.input_ids),
                         "filler_token_indices": fabs, "q_last": q_last, "cue": cue, "gen": gen})
            if rank == 0 and n % 5 == 0:
                print(f"[{n+1}/{len(items)}] {ex['id']} T={len(al.input_ids)}", flush=True)
    if rank == 0:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        torch.save({"resid_streams": resid, "resid": collapsed, "entropy": entropy, "norms": collapsed.float().norm(dim=-1),
                    "positions": [f"F{i+1}" for i in range(K)] + ["q_last", "cue", "gen"], "meta": meta, "n_layers": L,
                    "model_id": "deepseek-ai/DeepSeek-V4-Flash", "adapter": None, "collapse": "model.head.hc_head (model-native), per extract_dsv4"},
                   args.output_dir / "dot_dump.pt")
        print("DUMP_DONE", flush=True)
    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
