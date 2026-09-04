#!/usr/bin/env python3
"""Dump what a model does at dot positions: residuals, lens entropy, norms, attention.

For every item in a fixed-k config, one eager-attention forward pass records
post-block residuals at all filler positions, the last question token, the
answer cue, and the generation position (every block), plus logit-lens entropy
and residual norm at those positions, plus, for full-attention blocks, the
attention mass from the answer positions and from the dots onto prompt regions.
Residuals are saved as one bf16 tensor per model for downstream probing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import torch
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src")); sys.path.insert(0, str(REPO / "scripts"))
from extract_hf import _NoDoubleBos, capture_block_outputs, decoder_parts, load_model, make_encode_messages  # noqa: E402
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402

REGIONS = ["bos", "prefix", "problem", "dots", "template"]


@torch.inference_mode()
def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", required=True); p.add_argument("--adapter", type=Path, default=None)
    p.add_argument("--examples-config", type=Path, required=True); p.add_argument("--filler-length", type=int, default=50)
    p.add_argument("--output-dir", type=Path, required=True); p.add_argument("--max-items", type=int, default=0)
    args = p.parse_args()

    tokenizer = _NoDoubleBos(AutoTokenizer.from_pretrained(args.model_id))
    model = load_model(args.model_id, "main", torch.bfloat16, "eager")
    if args.adapter:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, str(args.adapter)).merge_and_unload()
    model.eval(); encode = make_encode_messages(tokenizer)
    layers_module, norm, head = decoder_parts(model); L = len(layers_module)
    layer_types = list(getattr(model.config, "layer_types", None) or getattr(model.config.get_text_config(), "layer_types", []))
    attn_layers = [i for i, t in enumerate(layer_types) if t == "full_attention"] if layer_types else list(range(L))
    im_start = tokenizer.get_vocab().get("<|im_start|>")

    cfg = json.loads(args.examples_config.read_text()); items = cfg["examples"][: args.max_items or None]
    K = args.filler_length
    _m0 = build_messages(cfg["few_shot"], items[0], cfg["filler_type"], K, task_type=cfg.get("task_type", "variable_binding"))
    _, _al0 = render_and_align(tokenizer, encode, _m0, cfg["filler_type"], K)
    NF = len(_al0.filler_token_indices)   # numbers span more than one token per item
    resid = torch.zeros(len(items), L, NF + 3, model.config.get_text_config().hidden_size if hasattr(model.config, "get_text_config") else model.config.hidden_size, dtype=torch.bfloat16)
    entropy = torch.zeros(len(items), L, NF + 3); norms = torch.zeros(len(items), L, NF + 3)
    attn_from_answer: list[Any] = []  # per item: {layer: [query(3), head, region]}
    attn_from_dots: list[Any] = []    # per item: {layer: [head, region]} averaged over dot queries
    meta = []
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for n, ex in enumerate(items):
        msgs = build_messages(cfg["few_shot"], ex, cfg["filler_type"], K, task_type=cfg.get("task_type", "variable_binding"))
        _, al = render_and_align(tokenizer, encode, msgs, cfg["filler_type"], K)
        fabs = al.filler_token_indices; cue = al.answer_cue_token_indices[-1]; gen = al.generation_position
        if len(fabs) != NF: raise AssertionError(f"{ex['id']}: {len(fabs)} filler tokens, expected {NF}")
        # last question token: the token just before "\n\nFiller:" i.e. before the first token whose offset >= filler marker start
        q_last = next(i for i in range(fabs[0] - 1, 0, -1) if al.token_strings[i].strip().endswith("?"))
        target_start = max(i for i, t in enumerate(al.input_ids[: fabs[0]]) if t == im_start) if im_start is not None else 0
        positions = fabs + [q_last, cue, gen]
        ids = torch.tensor([al.input_ids], device=model.device)
        with capture_block_outputs(layers_module, list(range(L)), positions) as cap:
            out = model(input_ids=ids, attention_mask=torch.ones_like(ids), use_cache=False, output_attentions=True)
        for l in range(L):
            h = cap[l]                                  # [P, d]
            resid[n, l] = h.cpu()
            norms[n, l] = h.float().norm(dim=-1).cpu()
            logits = head(norm(h)).float(); lp = torch.log_softmax(logits, -1)
            entropy[n, l] = (-(lp.exp() * lp).sum(-1)).cpu()
        # region index per key position
        T = ids.shape[1]; region = torch.full((T,), 1, dtype=torch.long)  # prefix
        region[0] = 0; region[target_start: fabs[0]] = 2; region[fabs] = 3; region[fabs[-1] + 1: gen + 1] = 4
        onehot = torch.nn.functional.one_hot(region, len(REGIONS)).float().to(model.device)  # [T, R]
        a_ans, a_dots = {}, {}
        atts = out.attentions or ()
        for li, l in enumerate(attn_layers):
            A = atts[l] if len(atts) == L else (atts[li] if li < len(atts) else None)
            if A is None: continue
            A = A[0].float()                              # [H, T, T]
            q_idx = torch.tensor([q_last, cue, gen], device=model.device)
            a_ans[l] = (A[:, q_idx, :] @ onehot).permute(1, 0, 2).cpu()             # [3, H, R]
            a_dots[l] = (A[:, torch.tensor(fabs, device=model.device), :] @ onehot).mean(1).cpu()  # [H, R]
        attn_from_answer.append({str(l): v.tolist() for l, v in a_ans.items()}); attn_from_dots.append({str(l): v.tolist() for l, v in a_dots.items()})
        meta.append({"id": ex["id"], "answer": ex["answer"], "expected_intermediates": ex["expected_intermediates"], "n_tokens": T,
                     "filler_token_indices": fabs, "q_last": q_last, "cue": cue, "gen": gen, "target_start": target_start})
        del out
        if n % 10 == 0: print(f"[{n+1}/{len(items)}] {ex['id']} T={T}", flush=True)
    torch.save({"resid": resid, "entropy": entropy, "norms": norms, "positions": [f"F{i+1}" for i in range(NF)] + ["q_last", "cue", "gen"], "filler_type": cfg["filler_type"], "filler_items": K, "filler_token_strings": [_al0.token_strings[i] for i in _al0.filler_token_indices],
                "attn_layers": attn_layers, "regions": REGIONS, "attn_from_answer": attn_from_answer, "attn_from_dots": attn_from_dots,
                "meta": meta, "model_id": args.model_id, "adapter": str(args.adapter) if args.adapter else None, "n_layers": L},
               args.output_dir / "dot_dump.pt")
    print("DUMP_DONE", args.output_dir / "dot_dump.pt", flush=True)


if __name__ == "__main__":
    main()
