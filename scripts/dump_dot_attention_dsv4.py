#!/usr/bin/env python3
"""DeepSeek V4 Flash: attention mass from answer positions and dots onto prompt regions.

V4 attention (reference ``inference/model.py``) is MLA with a 128-token sliding
window plus compressed KV: even blocks 2..40 attend to 4-token compressed blocks
chosen by a learned indexer (top 512 of them, which at our ~1.3k-token prompts is
all of them), odd blocks 3..41 attend to 128-token compressed blocks, and blocks
0, 1, 42 are window-only. The fused kernel returns no weights, so this script
wraps ``sparse_attn`` and recomputes softmax(q k^T * scale, with the per-head
sink) for selected query positions, then attributes each selected key to a
prompt region: a window key is one token; a compressed key is spread evenly over
the tokens it pools. Output matches ``dump_dot_residuals_hf.py``'s attention
fields so ``analyze_dot_residuals.py`` and the heatmap script run unchanged.
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
from extract_dsv4 import barrier, distributed_setup, filler_placement_for_task  # noqa: E402
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402

REGIONS = ["bos", "prefix", "problem", "dots", "template", "announce"]   # announce = the filler sentence in the system message
STATE: dict[str, Any] = {"layer": None, "queries": None, "key_region": None, "record": {}}


def install_attention_probe(model_module: Any, model: Any) -> None:
    """Wrap model.sparse_attn to record region-attributed weights for STATE['queries']."""
    real = model_module.sparse_attn

    def probed(q, kv, attn_sink, topk_idxs, softmax_scale):
        o = real(q, kv, attn_sink, topk_idxs, softmax_scale)
        if STATE["queries"] is None or STATE["layer"] is None:
            return o
        Q = STATE["queries"]                                      # list of query positions
        qs = q[0, Q].float()                                      # [nq, H, d]
        idx = topk_idxs[0, Q].long()                              # [nq, topk]
        valid = idx >= 0
        keys = kv[0][idx.clamp(min=0)].float()                    # [nq, topk, d]
        logits = torch.einsum("qhd,qkd->qhk", qs, keys) * softmax_scale
        logits = logits.masked_fill(~valid[:, None, :], float("-inf"))
        sink = attn_sink.float()[None, :, None]                   # [1, H, 1]
        m = torch.maximum(logits.max(-1, keepdim=True).values, sink)
        w = torch.exp(logits - m); denom = w.sum(-1, keepdim=True) + torch.exp(sink - m)
        w = w / denom                                             # [nq, H, topk]; sink mass = 1 - w.sum
        reg = STATE["key_region"][idx.clamp(min=0)]               # [nq, topk, R] fractional region membership
        mass = torch.einsum("qhk,qkr->qhr", w, reg.float())       # [nq, H, R]
        STATE["record"][STATE["layer"]] = mass.cpu()
        return o

    model_module.sparse_attn = probed
    for i, block in enumerate(model.layers):
        block.attn.register_forward_pre_hook(lambda mod, args, i=i: STATE.__setitem__("layer", i))


def key_region_matrix(seqlen: int, n_keys: int, offset: int, ratio: int, token_region: torch.Tensor) -> torch.Tensor:
    """[n_keys, R] with window keys -> one-hot token region, compressed keys -> mean region over pooled tokens."""
    R = len(REGIONS); out = torch.zeros(n_keys, R, dtype=torch.float32)
    onehot = torch.nn.functional.one_hot(token_region, R).float()
    out[:seqlen] = onehot[:seqlen]
    if ratio:
        for b in range(n_keys - offset):
            lo, hi = b * ratio, min((b + 1) * ratio, seqlen)
            if hi > lo:
                out[offset + b] = onehot[lo:hi].mean(0)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt-path", type=Path, required=True); p.add_argument("--model-config", type=Path, required=True)
    p.add_argument("--reference-code-dir", type=Path, required=True); p.add_argument("--examples-config", type=Path, required=True)
    p.add_argument("--filler-length", type=int, default=50); p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--max-items", type=int, default=0); p.add_argument("--max-seq-len", type=int, default=1280)
    p.add_argument("--process-group-timeout-minutes", type=int, default=60); p.add_argument("--announce-filler", type=int, default=0)
    args = p.parse_args()

    rank, local_rank, world_size = distributed_setup(args.process_group_timeout_minutes)
    if world_size != 4:
        raise SystemExit("converted checkpoint requires world_size=4")
    torch.set_default_dtype(torch.bfloat16); torch.manual_seed(42)
    sys.path.insert(0, str(args.reference_code_dir.resolve())); sys.path.insert(0, str(args.reference_code_dir.resolve().parent / "encoding"))
    from encoding_dsv4 import encode_messages  # type: ignore
    import model as model_module  # type: ignore
    model_args = model_module.ModelArgs(**json.loads(args.model_config.read_text())); model_args.max_batch_size = 1; model_args.max_seq_len = args.max_seq_len
    with torch.device("cuda"):
        model = model_module.Transformer(model_args)
    load_model(model, str(args.ckpt_path / f"model{rank}-mp{world_size}.safetensors"), strict=False); model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.ckpt_path); torch.set_default_device("cuda"); barrier()
    install_attention_probe(model_module, model)
    ratios = list(model_args.compress_ratios); win = model_args.window_size; L = len(model.layers)

    cfg = json.loads(args.examples_config.read_text()); items = cfg["examples"][: args.max_items or None]
    task = cfg.get("task_type", "variable_binding"); K = args.filler_length
    attn_from_answer, attn_from_dots, meta = [], [], []
    with torch.inference_mode():
        for n, ex in enumerate(items):
            msgs = build_messages(cfg["few_shot"], ex, cfg["filler_type"], args.announce_filler or K, task_type=task, target_length=K)
            if K > 0:
                rendered, al = render_and_align(tokenizer, encode_messages, msgs, cfg["filler_type"], K, filler_placement=filler_placement_for_task(task))
            else:
                rendered = encode_messages(msgs, thinking_mode="chat")
                enc = tokenizer(rendered, add_special_tokens=False, return_offsets_mapping=True)
                ids = list(enc["input_ids"]); offs = [tuple(x) for x in enc["offset_mapping"]]
                a0 = rendered.rfind("Answer:"); a1 = a0 + len("Answer:")
                class _A: pass
                al = _A(); al.input_ids = ids; al.offsets = offs; al.token_strings = [tokenizer.decode([t]) for t in ids]
                al.filler_token_indices = []; al.answer_cue_token_indices = [i for i, (x, y) in enumerate(offs) if y > a0 and x < a1]
                al.generation_position = len(ids) - 1; al.filler_char_span = (a0, a0)
            fabs = al.filler_token_indices; cue = al.answer_cue_token_indices[-1]; gen = al.generation_position; T = len(al.input_ids)
            q_last = next(i for i in range(((fabs[0] if fabs else cue) - 1), 0, -1) if al.token_strings[i].strip().endswith("?"))
            first_def = f"{ex['definitions'][0][0]} = {ex['definitions'][0][1]}"
            char_start = rendered.rfind(first_def, 0, al.filler_char_span[0])
            target_start = next(i for i, (a, b) in enumerate(al.offsets) if b > char_start)
            token_region = torch.ones(T, dtype=torch.long); token_region[0] = 0
            token_region[target_start: (fabs[0] if fabs else cue)] = 2
            if fabs: token_region[fabs] = 3
            token_region[(fabs[-1] + 1 if fabs else cue): gen + 1] = 4
            ann = rendered.find(" After the question, there will be")
            if ann >= 0:
                ann_end = rendered.find("before you answer.", ann) + len("before you answer.")
                for i, (x, y) in enumerate(al.offsets):
                    if y > ann and x < ann_end: token_region[i] = 5
            queries = fabs + [q_last, cue, gen]
            STATE["queries"] = queries; STATE["record"] = {}
            per_layer_key_region = {}
            tokens = torch.tensor([al.input_ids], dtype=torch.long, device="cuda")
            # key-region matrices depend on the layer's compress ratio; build lazily inside the probe via STATE
            class _KR:
                def __getitem__(self_, idx):
                    l = STATE["layer"]; ratio = ratios[l]
                    if l not in per_layer_key_region:
                        n_keys = T + (T // ratio if ratio else 0)
                        per_layer_key_region[l] = key_region_matrix(T, n_keys, T, ratio, token_region).to("cuda")
                    return per_layer_key_region[l][idx]
            STATE["key_region"] = _KR()
            model.forward(tokens, 0)
            # gather heads across ranks: each rank holds 16 local heads
            rec_ans, rec_dots = {}, {}
            for l in range(L):
                mass = STATE["record"].get(l)
                if mass is None: continue
                mass = mass.to("cuda")                             # [nq, H_local, R]
                gathered = [torch.empty_like(mass) for _ in range(world_size)]; dist.all_gather(gathered, mass.contiguous())
                full = torch.cat(gathered, dim=1).cpu()           # [nq, H, R]
                nf = len(fabs)
                rec_ans[str(l)] = full[nf:].tolist()               # [3, H, R] for q_last, cue, gen
                rec_dots[str(l)] = full[:nf].mean(0).tolist() if nf else []   # [H, R]
            attn_from_answer.append(rec_ans); attn_from_dots.append(rec_dots)
            meta.append({"id": ex["id"], "answer": ex["answer"], "expected_intermediates": ex["expected_intermediates"], "n_tokens": T,
                         "filler_token_indices": fabs, "q_last": q_last, "cue": cue, "gen": gen, "target_start": target_start, "n_announce_tokens": int((token_region == 5).sum())})
            if rank == 0 and n % 5 == 0:
                g = torch.tensor(rec_ans[str(L - 2)])[2].mean(0); print(f"[{n+1}/{len(items)}] {ex['id']} T={T} gen-attn@L{L-2} by region {dict(zip(REGIONS, [round(float(x), 3) for x in g]))}", flush=True)
    STATE["queries"] = None
    if rank == 0:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        torch.save({"attn_layers": list(range(L)), "regions": REGIONS, "attn_from_answer": attn_from_answer, "attn_from_dots": attn_from_dots, "meta": meta,
                    "window_size": win, "compress_ratios": ratios, "index_topk": model_args.index_topk,
                    "note": "weights recomputed from q/kv/topk_idxs with the per-head sink; compressed keys spread evenly over pooled tokens; sink mass = 1 - sum of regions"},
                   args.output_dir / "dot_attention.pt")
        print("ATTN_DONE", flush=True)
    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
