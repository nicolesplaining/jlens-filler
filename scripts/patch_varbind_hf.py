#!/usr/bin/env python3
"""Single-cell activation patching on a Hugging Face (optionally LoRA-merged) model.

Port of ``sweep_varbind_patches_dsv4.py`` for single-residual-stream models.
For one exact-layout donor/target pair rendered at the same dot count, the
donor's post-block residual at (layer, filler ordinal) replaces the target's at
the same cell, one cell at a time, and the effect on the next-token
distribution is measured. Multi-digit answers are scored by teacher-forced
sequence log-probability under the patch, so digit-split tokenizers are fine.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import torch
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))
from extract_hf import _NoDoubleBos, capture_block_outputs, decoder_parts, load_model, make_encode_messages  # noqa: E402
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", required=True)
    p.add_argument("--adapter", type=Path, default=None)
    p.add_argument("--examples-config", type=Path, required=True)
    p.add_argument("--donor-id", required=True)
    p.add_argument("--target-id", required=True)
    p.add_argument("--filler-length", type=int, required=True)
    p.add_argument("--layers", default="all", help="'all', 'a-b', or comma list")
    p.add_argument("--positions", default="all", help="'all' or comma list of filler ordinals (1-based)")
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--require-identical-token-layout", action="store_true")
    p.add_argument("--lesion-all-dots", action="store_true",
                   help="instead of donor patching, replace ALL filler residuals at one layer with their position-mean (per layer), on the target only")
    p.add_argument("--lesion-all-layers", action="store_true",
                   help="with --lesion-all-dots: also lesion every layer simultaneously (modes mean and zero); --target-id may be a comma list")
    return p.parse_args()


def parse_layers(spec: str, n: int) -> list[int]:
    if spec == "all":
        return list(range(n))
    if "-" in spec and "," not in spec:
        a, b = spec.split("-"); return list(range(int(a), int(b) + 1))
    return sorted({int(x) for x in spec.split(",") if x.strip()})


def output_tensor(output: Any) -> torch.Tensor:
    return output[0] if isinstance(output, tuple) else output


def replace_output(output: Any, tensor: torch.Tensor) -> Any:
    if not isinstance(output, tuple):
        return tensor
    values = list(output); values[0] = tensor; return tuple(values)


@contextmanager
def patch_cells(layers_module: Any, cells: list[tuple[int, int]], donor_hidden: dict[int, torch.Tensor], filler_abs: list[int]):
    """cells: (layer, ordinal). donor_hidden[layer]: [n_filler, d] donor post-block residuals at filler positions."""
    by_layer: dict[int, list[int]] = {}
    for layer, ordinal in cells:
        by_layer.setdefault(layer, []).append(ordinal)
    handles = []

    def make_hook(layer: int):
        def hook(_m: Any, _i: Any, output: Any) -> Any:
            t = output_tensor(output)
            if t.shape[1] <= max(filler_abs):
                return output  # decode step (KV/recurrent state already carry the intervention)
            t = t.clone()
            for ordinal in by_layer[layer]:
                t[:, filler_abs[ordinal - 1]] = donor_hidden[layer][ordinal - 1].to(t.dtype)
            return replace_output(output, t)
        return hook

    try:
        for layer in by_layer:
            handles.append(layers_module[layer].register_forward_hook(make_hook(layer)))
        yield
    finally:
        for h in handles:
            h.remove()


@contextmanager
def lesion_all_dots(layers_module: Any, layer: int, filler_abs: list[int], mode: str = "mean"):
    """Replace every filler residual at ``layer`` with the mean over filler positions (or zeros)."""
    def hook(_m: Any, _i: Any, output: Any) -> Any:
        t = output_tensor(output)
        if t.shape[1] <= max(filler_abs):
            return output
        t = t.clone()
        block = t[:, filler_abs]
        t[:, filler_abs] = block.mean(dim=1, keepdim=True) if mode == "mean" else torch.zeros_like(block)
        return replace_output(output, t)
    h = layers_module[layer].register_forward_hook(hook)
    try:
        yield
    finally:
        h.remove()


@contextmanager
def lesion_all_dots_all_layers(layers_module: Any, layer_indices: list[int], filler_abs: list[int], mode: str):
    def make_hook():
        def hook(_m: Any, _i: Any, output: Any) -> Any:
            t = output_tensor(output)
            if t.shape[1] <= max(filler_abs):
                return output  # decode step (KV/recurrent state already carry the intervention)
            t = t.clone()
            block = t[:, filler_abs]
            t[:, filler_abs] = block.mean(dim=1, keepdim=True) if mode == "mean" else torch.zeros_like(block)
            return replace_output(output, t)
        return hook
    handles = [layers_module[l].register_forward_hook(make_hook()) for l in layer_indices]
    try:
        yield
    finally:
        for h in handles:
            h.remove()


@torch.inference_mode()
def score_answers(model: Any, tokenizer: Any, prompt_ids: list[int], answers: dict[str, Any]) -> dict[str, dict[str, float]]:
    """Teacher-forced sequence log-prob and first-token rank for each answer under the current hooks."""
    out: dict[str, dict[str, float]] = {}
    for label, answer in answers.items():
        ids = tokenizer.encode(str(answer), add_special_tokens=False)
        full = torch.tensor([prompt_ids + ids], device=model.device)
        logits = model(input_ids=full, attention_mask=torch.ones_like(full), use_cache=False).logits[0].float()
        start = len(prompt_ids) - 1
        logp = torch.log_softmax(logits[start : start + len(ids)], dim=-1)
        seq = sum(float(logp[i, ids[i]]) for i in range(len(ids)))
        first = logits[start]
        rank = int((first > first[ids[0]]).sum().item()) + 1
        out[label] = {"sequence_log_probability": seq, "first_token_rank": rank, "n_tokens": len(ids)}
    return out


def main() -> None:
    args = parse_args()
    tokenizer = _NoDoubleBos(AutoTokenizer.from_pretrained(args.model_id))
    model = load_model(args.model_id, "main", torch.bfloat16, None)
    if args.adapter is not None:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, str(args.adapter)).merge_and_unload()
    model.eval()
    encode = make_encode_messages(tokenizer)
    layers_module, _, _ = decoder_parts(model)

    cfg = json.loads(args.examples_config.read_text())
    by_id = {e["id"]: e for e in cfg["examples"]}
    first_target = args.target_id.split(",")[0]
    donor, target = by_id[args.donor_id.split(",")[0]], by_id[first_target]
    task = cfg.get("task_type", "variable_binding")

    def render(ex):
        m = build_messages(cfg["few_shot"], ex, cfg["filler_type"], args.filler_length, task_type=task)
        return render_and_align(tokenizer, encode, m, cfg["filler_type"], args.filler_length)

    _, d_al = render(donor); _, t_al = render(target)
    diffs = [i for i, (a, b) in enumerate(zip(d_al.input_ids, t_al.input_ids)) if a != b]
    if args.require_identical_token_layout:
        assert len(d_al.input_ids) == len(t_al.input_ids), "token lengths differ"
        assert d_al.filler_token_indices == t_al.filler_token_indices, "filler indices differ"
        assert len(diffs) == 1, f"expected exactly one differing token, got {diffs}"
    filler_abs = t_al.filler_token_indices
    n_blocks = len(layers_module)
    layers = parse_layers(args.layers, n_blocks)
    ordinals = list(range(1, len(filler_abs) + 1)) if args.positions == "all" else [int(x) for x in args.positions.split(",")]

    # Donor residuals at filler positions, every layer.
    ids = torch.tensor([d_al.input_ids], device=model.device)
    with capture_block_outputs(layers_module, layers, d_al.filler_token_indices) as donor_hidden:
        model(input_ids=ids, attention_mask=torch.ones_like(ids), use_cache=False)
    tids = torch.tensor([t_al.input_ids], device=model.device)
    with capture_block_outputs(layers_module, layers, filler_abs) as target_hidden:
        model(input_ids=tids, attention_mask=torch.ones_like(tids), use_cache=False)

    answers = {"donor_answer": donor["answer"], "target_answer": target["answer"]}
    baseline = score_answers(model, tokenizer, t_al.input_ids, answers)
    # Identity closure: patching the target's own residual must not change anything.
    with patch_cells(layers_module, [(layers[0], 1)], target_hidden, filler_abs):
        ident = score_answers(model, tokenizer, t_al.input_ids, answers)
    ident_err = max(abs(ident[k]["sequence_log_probability"] - baseline[k]["sequence_log_probability"]) for k in answers)
    print(f"baseline: donor {baseline['donor_answer']} target {baseline['target_answer']} | identity closure max |Δlogp| = {ident_err:.2e}", flush=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.lesion_all_dots:
        # Necessity test: if the dot positions carry usable computation, wiping all of them must hurt.
        def greedy_answer(input_ids):
            ids = torch.tensor([input_ids], device=model.device)
            outg = model.generate(input_ids=ids, attention_mask=torch.ones_like(ids), max_new_tokens=3, do_sample=False,
                                  temperature=None, top_p=None, top_k=None, pad_token_id=tokenizer.eos_token_id)
            return tokenizer.decode(outg[0, ids.shape[1]:], skip_special_tokens=True)
        all_out = []
        for tid in args.target_id.split(","):
            tgt = by_id[tid]; _, al = render(tgt); fabs = al.filler_token_indices
            base_s = score_answers(model, tokenizer, al.input_ids, {"a": tgt["answer"]})["a"]
            base_gen = greedy_answer(al.input_ids)
            rec = {"target_id": tid, "answer": tgt["answer"], "unpatched": {**base_s, "greedy": base_gen}, "per_layer_mean": [], "all_layers": {}}
            if not args.lesion_all_layers:
                for layer in layers:
                    with lesion_all_dots(layers_module, layer, fabs, "mean"):
                        s = score_answers(model, tokenizer, al.input_ids, {"a": tgt["answer"]})["a"]
                    rec["per_layer_mean"].append({"layer": layer, "delta_logp": s["sequence_log_probability"] - base_s["sequence_log_probability"], "first_token_rank": s["first_token_rank"]})
            for mode in ("mean", "zero"):
                with lesion_all_dots_all_layers(layers_module, layers, fabs, mode):
                    s = score_answers(model, tokenizer, al.input_ids, {"a": tgt["answer"]})["a"]
                    gen = greedy_answer(al.input_ids)
                rec["all_layers"][mode] = {"delta_logp": s["sequence_log_probability"] - base_s["sequence_log_probability"],
                                          "first_token_rank": s["first_token_rank"], "greedy": gen, "still_correct": gen.strip() == str(tgt["answer"])}
            m, z = rec["all_layers"]["mean"], rec["all_layers"]["zero"]
            print(f"{tid}: base logp {base_s['sequence_log_probability']:+.3f} greedy {base_gen!r} | all-layer MEAN lesion Δlogp {m['delta_logp']:+.3f} greedy {m['greedy']!r} | all-layer ZERO lesion Δlogp {z['delta_logp']:+.3f} greedy {z['greedy']!r}", flush=True)
            all_out.append(rec)
        out = {"schema_version": 1, "intervention": "all filler residuals replaced by their mean over filler positions (or zeros), at one layer at a time and at all layers simultaneously",
               "model_id": args.model_id, "adapter": str(args.adapter) if args.adapter else None, "filler_length": args.filler_length, "layers": layers, "targets": all_out}
        (args.output_dir / "all-dots-lesion.json").write_text(json.dumps(out, indent=1))
        print("LESION_DONE", flush=True)
        return

    result: dict[str, Any] = {
        "schema_version": 1,
        "intervention": "one donor post-block residual (single stream) patched into the same filler ordinal of the target",
        "model_id": args.model_id, "adapter": str(args.adapter) if args.adapter else None,
        "donor_id": args.donor_id, "target_id": args.target_id, "filler_length": args.filler_length,
        "donor_answer": donor["answer"], "target_answer": target["answer"],
        "donor_intermediates": donor.get("expected_intermediates"), "target_intermediates": target.get("expected_intermediates"),
        "input_token_differences": [{"absolute_index": i, "donor_token": tokenizer.decode([d_al.input_ids[i]]), "target_token": tokenizer.decode([t_al.input_ids[i]])} for i in diffs],
        "filler_token_indices": filler_abs, "layers": layers, "positions": ordinals,
        "identity_patch_max_abs_logp_error": ident_err,
        "unpatched": baseline,
        "cells": [],
    }
    t0 = time.time(); n = 0
    for layer in layers:
        for ordinal in ordinals:
            with patch_cells(layers_module, [(layer, ordinal)], donor_hidden, filler_abs):
                s = score_answers(model, tokenizer, t_al.input_ids, answers)
            result["cells"].append({
                "layer": layer, "position": ordinal,
                "donor_log_probability_change": s["donor_answer"]["sequence_log_probability"] - baseline["donor_answer"]["sequence_log_probability"],
                "donor_first_token_rank": s["donor_answer"]["first_token_rank"],
                "target_log_probability_change": s["target_answer"]["sequence_log_probability"] - baseline["target_answer"]["sequence_log_probability"],
                "target_first_token_rank": s["target_answer"]["first_token_rank"],
            })
            n += 1
        best = max((c for c in result["cells"] if c["layer"] == layer), key=lambda c: c["donor_log_probability_change"])
        print(f"layer {layer:>2}: best cell F{best['position']} donor Δlogp {best['donor_log_probability_change']:+.2f} target Δlogp {best['target_log_probability_change']:+.2f} ({(time.time()-t0)/n:.2f}s/cell)", flush=True)
        (args.output_dir / "single-cell-grid.json").write_text(json.dumps(result, indent=1))
    print("PATCH_DONE", flush=True)


if __name__ == "__main__":
    main()
