#!/usr/bin/env python3
"""Distributed DeepSeek-V4-Flash J-Lens/logit-lens extraction.

This script deliberately imports DeepSeek's released reference implementation
(``inference/model.py`` and ``encoding/encoding_dsv4.py``) instead of assuming
Hugging Face's generic chat or residual conventions. Launch with ``torchrun``
using the same model-parallel width as the converted checkpoint.

The released workspace lens is square (4096 x 4096) even though a raw V4 block
output is an mHC tensor of shape [B,S,4,4096]. The only model-native 4096-wide
readout is ``ParallelHead.hc_head``. We apply that exact final hyper-head at
each captured layer, record the convention prominently, and gate filler work
on final-head closure and the lens's identity anchor. This does not erase the
metadata omission: the lens file itself does not state its source projection.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import sys
import time
from contextlib import contextmanager
from datetime import timedelta
from pathlib import Path
from typing import Any

import torch
import torch.distributed as dist
import torch.nn.functional as F
from safetensors.torch import load_model
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from jlens_filler.prompts import (  # noqa: E402
    build_messages,
    make_filler,
    render_and_align,
    token_variants,
)


def parse_layers(spec: str, valid: set[int]) -> list[int]:
    if spec == "all":
        return sorted(valid)
    layers = sorted({int(x.strip()) for x in spec.split(",") if x.strip()})
    unknown = set(layers) - valid
    if unknown:
        raise ValueError(f"layers not covered by lens: {sorted(unknown)}")
    return layers


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def installed_version(distribution: str) -> str | None:
    try:
        return importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return None


def parse_numeric_answer(text: str) -> int | None:
    match = re.search(r"-?\d+", text)
    return int(match.group()) if match else None


def parse_model_answer(text: str, expected: Any) -> int | str | None:
    """Parse only the answer type declared by the dataset.

    Numeric tasks retain the released repository's first-integer convention.
    Letter-position tasks accept a bare lowercase/uppercase letter or the last
    standalone letter in a more verbose completion, then normalize case.
    """
    if isinstance(expected, int) and not isinstance(expected, bool):
        return parse_numeric_answer(text)
    expected_text = str(expected).strip()
    if len(expected_text) == 1 and expected_text.isalpha():
        stripped = text.strip()
        if len(stripped) == 1 and stripped.isalpha():
            return stripped.lower()
        matches = re.findall(r"(?<![A-Za-z])([A-Za-z])(?![A-Za-z])", text)
        return matches[-1].lower() if matches else None
    stripped = text.strip()
    return stripped if stripped else None


def answer_is_correct(parsed: int | str | None, expected: Any) -> bool:
    if isinstance(expected, int) and not isinstance(expected, bool):
        return parsed == expected
    return parsed == str(expected).strip().lower()


ONE_TOKEN_FILLERS = {"dots", "alphabet", "alphabet-scrambled"}


def check_filler_token_count(filler_type: str, filler_length: int, indices: list[int], example_id: str) -> None:
    """Dots and single letters are one token each; numbers carry a separate space token, so they map
    to about two tokens per item. Require exact equality for the one-token types and at least one
    token per item otherwise; the sweep output records the actual `filler_token_indices`."""
    n = len(indices)
    if filler_type in ONE_TOKEN_FILLERS and n != filler_length:
        raise AssertionError(f"{example_id} at k={filler_length}: {filler_length} visible fillers mapped to {n} tokens")
    if n < filler_length:
        raise AssertionError(f"{example_id} at k={filler_length}: {filler_length} visible fillers mapped to only {n} tokens")


def filler_placement_for_task(task_type: str) -> str:
    return (
        "before_question"
        if task_type == "variable_binding_pre_filler"
        else "between_question_answer"
    )


def distributed_setup(timeout_minutes: int) -> tuple[int, int, int]:
    world_size = int(os.environ.get("WORLD_SIZE", "1"))
    rank = int(os.environ.get("RANK", "0"))
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    torch.cuda.set_device(local_rank)
    if world_size > 1:
        dist.init_process_group(
            "nccl",
            timeout=timedelta(minutes=timeout_minutes),
            device_id=torch.device("cuda", local_rank),
        )
    return rank, local_rank, world_size


def all_reduce(tensor: torch.Tensor, op: dist.ReduceOp) -> torch.Tensor:
    if dist.is_initialized():
        dist.all_reduce(tensor, op=op)
    return tensor


def barrier() -> None:
    if dist.is_initialized():
        dist.barrier()


def distributed_readout(
    local_logits: torch.Tensor,
    *,
    tokenizer: Any,
    top_k: int,
    tracked: dict[str, list[dict[str, Any]]],
    rank: int,
    world_size: int,
) -> list[dict[str, Any]] | None:
    """Top-k, probabilities, and exact ranks with an ephemeral gathered logit tensor.

    V4 shards the vocabulary across four ranks. Gathering the compact
    [positions, vocab_shard] projections (about 5.7 MB for eleven positions)
    is both simpler and more robust than issuing small mixed-dtype collectives
    for every tracked target. The gathered full-vocabulary tensor is never
    saved and is released before the next readout.
    """
    if local_logits.ndim != 2:
        raise AssertionError(f"expected [positions,vocab_shard], got {local_logits.shape}")
    n_positions, shard_vocab = local_logits.shape

    if world_size > 1:
        torch.cuda.synchronize()
        shards = [torch.empty_like(local_logits) for _ in range(world_size)]
        dist.all_gather(shards, local_logits.contiguous())
        global_logits = torch.cat(shards, dim=-1)
    else:
        global_logits = local_logits
    if global_logits.shape[-1] != shard_vocab * world_size:
        raise AssertionError(f"gathered logits have shape {tuple(global_logits.shape)}")
    if rank != 0:
        return None
    best_values, best_ids = global_logits.topk(top_k, dim=-1)
    log_z = torch.logsumexp(global_logits, dim=-1)

    target_records: dict[str, list[dict[str, Any]]] = {
        label: [] for label in tracked
    }
    for label, variants in tracked.items():
        for variant in variants:
            token_ids = variant["token_ids"]
            record = dict(variant)
            if len(token_ids) != 1:
                record["rank_by_position"] = None
                record["logit_by_position"] = None
                record["probability_by_position"] = None
                target_records[label].append(record)
                continue
            token_id = token_ids[0]
            if token_id >= global_logits.shape[-1]:
                raise AssertionError(f"token id {token_id} exceeds distributed vocabulary")
            score = global_logits[:, token_id]
            counts = (global_logits > score[:, None]).sum(
                dim=-1, dtype=torch.int64
            )
            record["rank_by_position"] = (counts + 1).cpu().tolist()
            record["logit_by_position"] = score.cpu().tolist()
            record["probability_by_position"] = torch.exp(score - log_z).cpu().tolist()
            target_records[label].append(record)

    outputs: list[dict[str, Any]] = []
    best_values_cpu = best_values.cpu()
    best_ids_cpu = best_ids.cpu()
    log_z_cpu = log_z.cpu()
    for pos in range(n_positions):
        top_tokens = []
        for order in range(top_k):
            token_id = int(best_ids_cpu[pos, order])
            logit = float(best_values_cpu[pos, order])
            top_tokens.append(
                {
                    "rank": order + 1,
                    "token_id": token_id,
                    "token": tokenizer.decode([token_id]),
                    "logit": logit,
                    "probability": float(torch.exp(best_values_cpu[pos, order] - log_z_cpu[pos])),
                }
            )
        per_target: dict[str, Any] = {}
        for label, variants in target_records.items():
            positioned = []
            for variant in variants:
                item = {
                    key: value
                    for key, value in variant.items()
                    if not key.endswith("_by_position")
                }
                if variant["rank_by_position"] is not None:
                    item.update(
                        {
                            "rank": int(variant["rank_by_position"][pos]),
                            "logit": float(variant["logit_by_position"][pos]),
                            "probability": float(
                                variant["probability_by_position"][pos]
                            ),
                        }
                    )
                positioned.append(item)
            ranked = [x for x in positioned if "rank" in x]
            per_target[label] = {
                "best_rank": min((x["rank"] for x in ranked), default=None),
                "variants": positioned,
            }
        outputs.append({"top_tokens": top_tokens, "targets": per_target})
    return outputs


def full_logits_summary(
    logits: torch.Tensor, tokenizer: Any, top_k: int
) -> dict[str, Any]:
    logits = logits.float().cpu()
    probabilities = logits.softmax(dim=-1)
    values, ids = logits.topk(top_k)
    return {
        "top_tokens": [
            {
                "rank": idx + 1,
                "token_id": int(token_id),
                "token": tokenizer.decode([int(token_id)]),
                "logit": float(values[idx]),
                "probability": float(probabilities[int(token_id)]),
            }
            for idx, token_id in enumerate(ids)
        ]
    }


def target_logit_summary(
    logits: torch.Tensor, tokenizer: Any, answer: Any
) -> dict[str, Any]:
    """Exact first-token rank for every single-token rendering of an answer."""
    scores = logits.float().cpu()
    log_z = torch.logsumexp(scores, dim=-1)
    answer_text = str(answer)
    variants = token_variants(tokenizer, answer_text)
    ranked: list[dict[str, Any]] = []
    for variant in variants:
        record = dict(variant)
        if variant["single_token"]:
            token_id = int(variant["token_ids"][0])
            score = scores[token_id]
            record.update(
                {
                    "rank": int((scores > score).sum().item()) + 1,
                    "logit": float(score),
                    "log_probability": float(score - log_z),
                    "probability": float(torch.exp(score - log_z)),
                }
            )
            ranked.append(record)
    if not ranked:
        raise AssertionError(f"answer {answer_text} has no single-token tokenizer form")
    best = min(ranked, key=lambda item: item["rank"])
    return {
        "answer": answer,
        "best_rank": best["rank"],
        "best_logit": best["logit"],
        "best_log_probability": best["log_probability"],
        "best_probability": best["probability"],
        "variants": variants,
    }


@contextmanager
def capture_layers(model: Any, layer_indices: list[int], positions: list[int]):
    captured: dict[int, torch.Tensor] = {}
    handles = []

    def make_hook(layer: int):
        def hook(_module, _inputs, output):
            tensor = output[0] if isinstance(output, tuple) else output
            if tensor.ndim != 4:
                raise AssertionError(
                    f"layer {layer}: expected raw mHC [B,S,4,D], got {tuple(tensor.shape)}"
                )
            captured[layer] = tensor[:, positions].detach().clone()

        return hook

    try:
        for layer in layer_indices:
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield captured
    finally:
        for handle in handles:
            handle.remove()


def collapse_streams(model: Any, streams: torch.Tensor) -> torch.Tensor:
    """Apply the model's exact final mHC hyper-head without norm/unembedding."""
    if streams.ndim != 4 or streams.shape[-2] != 4 or streams.shape[-1] != 4096:
        raise AssertionError(f"unexpected mHC activation shape: {tuple(streams.shape)}")
    return model.head.hc_head(
        streams,
        model.hc_head_fn,
        model.hc_head_scale,
        model.hc_head_base,
    )


def local_unembed(model: Any, residual: torch.Tensor) -> torch.Tensor:
    return F.linear(model.norm(residual).float(), model.head.weight)


def run_forward_capture(
    model: Any,
    input_ids: list[int],
    layers: list[int],
    positions: list[int],
) -> tuple[dict[int, torch.Tensor], torch.Tensor]:
    tokens = torch.tensor([input_ids], dtype=torch.long, device="cuda")
    with capture_layers(model, layers, positions) as captured:
        actual_logits = model.forward(tokens, 0)
    missing = set(layers) - set(captured)
    if missing:
        raise AssertionError(f"hooks did not fire for layers {sorted(missing)}")
    return captured, actual_logits


@torch.inference_mode()
def read_layers(
    *,
    model: Any,
    captured: dict[int, torch.Tensor],
    lens_j: dict[int, torch.Tensor],
    layers: list[int],
    columns: list[dict[str, Any]],
    tokenizer: Any,
    top_k: int,
    tracked: dict[str, list[dict[str, Any]]],
    rank: int,
    world_size: int,
) -> dict[str, Any] | None:
    output = {"j_lens": {}, "logit_lens": {}} if rank == 0 else None
    for layer in layers:
        started = time.monotonic()
        if rank == 0:
            print(f"readout layer {layer}: start", flush=True)
        collapsed = collapse_streams(model, captured[layer])[0]
        if tuple(collapsed.shape) != (len(columns), 4096):
            raise AssertionError(
                f"layer {layer}: collapsed activation has shape {tuple(collapsed.shape)}"
            )
        j_matrix = lens_j[layer].to(device="cuda", dtype=torch.float32)
        if tuple(j_matrix.shape) != (4096, 4096):
            raise AssertionError(
                f"layer {layer}: lens matrix has shape {tuple(j_matrix.shape)}"
            )
        transported = collapsed.float() @ j_matrix.T
        local_j = local_unembed(model, transported)
        # The official JacobianLens.apply() casts selected residuals to FP32
        # before both the transported and vanilla logit-lens paths.
        local_ll = local_unembed(model, collapsed.float())
        j_records = distributed_readout(
            local_j,
            tokenizer=tokenizer,
            top_k=top_k,
            tracked=tracked,
            rank=rank,
            world_size=world_size,
        )
        ll_records = distributed_readout(
            local_ll,
            tokenizer=tokenizer,
            top_k=top_k,
            tracked=tracked,
            rank=rank,
            world_size=world_size,
        )
        if rank == 0:
            assert output is not None and j_records is not None and ll_records is not None
            output["j_lens"][str(layer)] = [
                {**column, **record} for column, record in zip(columns, j_records)
            ]
            output["logit_lens"][str(layer)] = [
                {**column, **record} for column, record in zip(columns, ll_records)
            ]
            print(
                f"readout layer {layer}: done in {time.monotonic() - started:.2f}s",
                flush=True,
            )
        del j_matrix, transported, local_j, local_ll
    return output


def greedy_generate(
    model: Any,
    prompt_tokens: list[int],
    *,
    max_new_tokens: int,
    eos_id: int,
) -> tuple[list[int], torch.Tensor]:
    """Reference-equivalent greedy generation for one prompt."""
    total_len = min(model.max_seq_len, len(prompt_tokens) + max_new_tokens)
    tokens = torch.full((1, total_len), -1, dtype=torch.long, device="cuda")
    tokens[0, : len(prompt_tokens)] = torch.tensor(prompt_tokens, device="cuda")
    previous = 0
    first_logits = None
    end = len(prompt_tokens)
    for current in range(len(prompt_tokens), total_len):
        logits = model.forward(tokens[:, previous:current], previous)
        if first_logits is None:
            first_logits = logits.detach().clone()
        next_token = logits.argmax(dim=-1)
        tokens[:, current] = next_token
        end = current + 1
        previous = current
        if int(next_token.item()) == eos_id:
            break
    if first_logits is None:
        raise AssertionError("generation produced no logits")
    completion = tokens[0, len(prompt_tokens) : end].tolist()
    return completion, first_logits


def tracked_variants(
    tokenizer: Any, expected: dict[str, str]
) -> dict[str, list[dict[str, Any]]]:
    return {label: token_variants(tokenizer, text) for label, text in expected.items()}


@torch.inference_mode()
def ordinary_sanity(
    *,
    model: Any,
    tokenizer: Any,
    encode_messages: Any,
    prompts: list[dict[str, Any]],
    lens_j: dict[int, torch.Tensor],
    layers: list[int],
    top_k: int,
    rank: int,
    world_size: int,
) -> list[dict[str, Any]] | None:
    results = [] if rank == 0 else None
    for prompt in prompts:
        rendered = encode_messages(prompt["messages"], thinking_mode="chat")
        ids = tokenizer.encode(rendered)
        position = len(ids) - 1
        capture_indices = sorted(set(layers) | {42})
        captured, actual_logits = run_forward_capture(
            model, ids, capture_indices, [position]
        )
        columns = [
            {
                "position_kind": "answer_prediction",
                "absolute_index": position,
                "surface": tokenizer.decode([ids[position]]),
            }
        ]
        readouts = read_layers(
            model=model,
            captured=captured,
            lens_j=lens_j,
            layers=layers,
            columns=columns,
            tokenizer=tokenizer,
            top_k=top_k,
            tracked={},
            rank=rank,
            world_size=world_size,
        )
        collapsed_final = collapse_streams(model, captured[42])[0]
        rebuilt_local = local_unembed(model, collapsed_final)
        shard = rebuilt_local.shape[-1]
        actual_local = actual_logits[:, rank * shard : (rank + 1) * shard]
        local_error = (rebuilt_local - actual_local).abs().max()
        closure_error = all_reduce(local_error, dist.ReduceOp.MAX)
        closure_records = distributed_readout(
            rebuilt_local,
            tokenizer=tokenizer,
            top_k=top_k,
            tracked={},
            rank=rank,
            world_size=world_size,
        )
        if rank == 0:
            assert results is not None and readouts is not None and closure_records is not None
            actual = full_logits_summary(actual_logits[0], tokenizer, top_k)
            layer_41_j = readouts["j_lens"].get("41", [None])[0]
            layer_41_ll = readouts["logit_lens"].get("41", [None])[0]
            j_ids = [x["token_id"] for x in layer_41_j["top_tokens"]] if layer_41_j else []
            ll_ids = [x["token_id"] for x in layer_41_ll["top_tokens"]] if layer_41_ll else []
            actual_ids = [x["token_id"] for x in actual["top_tokens"]]
            results.append(
                {
                    "id": prompt["id"],
                    "rendered_prompt": rendered,
                    "input_ids": ids,
                    "token_strings": [tokenizer.decode([x]) for x in ids],
                    "generation_position": position,
                    "readouts": readouts,
                    "actual_next_token": actual,
                    "layer_42_closure": {
                        "max_absolute_logit_error": float(closure_error.cpu()),
                        "top_tokens": closure_records[0]["top_tokens"],
                        "top1_matches_actual": closure_records[0]["top_tokens"][0]["token_id"]
                        == actual["top_tokens"][0]["token_id"],
                    },
                    "late_layer_checks": {
                        "layer_41_j_vs_ll_topk_overlap": len(set(j_ids) & set(ll_ids)),
                        "layer_41_j_vs_ll_ordered_topk_exact": j_ids == ll_ids,
                        "layer_41_j_vs_actual_topk_overlap": len(
                            set(j_ids) & set(actual_ids)
                        ),
                    },
                }
            )
    return results


@torch.inference_mode()
def run_filler_example(
    *,
    model: Any,
    tokenizer: Any,
    encode_messages: Any,
    few_shot: list[dict[str, Any]],
    example: dict[str, Any],
    filler_type: str,
    filler_length: int,
    task_type: str,
    lens_j: dict[int, torch.Tensor],
    layers: list[int],
    top_k: int,
    max_new_tokens: int,
    rank: int,
    world_size: int,
) -> dict[str, Any] | None:
    messages = build_messages(
        few_shot, example, filler_type, filler_length, task_type=task_type
    )
    rendered, alignment = render_and_align(
        tokenizer,
        encode_messages,
        messages,
        filler_type,
        filler_length,
        filler_placement=filler_placement_for_task(task_type),
    )
    answer_cue_position = alignment.answer_cue_token_indices[-1]
    selected_positions = alignment.filler_token_indices + [
        answer_cue_position,
        alignment.generation_position,
    ]
    columns = []
    for ordinal, absolute in enumerate(alignment.filler_token_indices, start=1):
        columns.append(
            {
                "position_kind": "filler",
                "filler_ordinal": ordinal,
                "absolute_index": absolute,
                "surface": alignment.token_strings[absolute],
            }
        )
    columns.append(
        {
            "position_kind": "answer_cue",
            "absolute_index": answer_cue_position,
            "surface": alignment.token_strings[answer_cue_position],
        }
    )
    columns.append(
        {
            "position_kind": "answer_prediction",
            "absolute_index": alignment.generation_position,
            "surface": alignment.token_strings[alignment.generation_position],
        }
    )
    capture_indices = sorted(set(layers) | {42})
    captured, actual_logits = run_forward_capture(
        model, alignment.input_ids, capture_indices, selected_positions
    )
    tracked_surfaces = dict(example["expected_intermediates"])
    controls = example.get("tracked_controls", {})
    overlap = set(tracked_surfaces) & set(controls)
    if overlap:
        raise ValueError(f"tracked control labels collide with targets: {sorted(overlap)}")
    tracked_surfaces.update({str(label): str(value) for label, value in controls.items()})
    variants = tracked_variants(tokenizer, tracked_surfaces)
    if task_type == "repeated_squaring_mod":
        multi_token_only = [
            label
            for label, forms in variants.items()
            if not any(form["single_token"] for form in forms)
        ]
        if multi_token_only:
            raise AssertionError(
                "T-hop target residues lack single-token forms: "
                + ", ".join(multi_token_only)
            )
    readouts = read_layers(
        model=model,
        captured=captured,
        lens_j=lens_j,
        layers=layers,
        columns=columns,
        tokenizer=tokenizer,
        top_k=top_k,
        tracked=variants,
        rank=rank,
        world_size=world_size,
    )

    completion_ids, first_logits = greedy_generate(
        model,
        alignment.input_ids,
        max_new_tokens=max_new_tokens,
        eos_id=tokenizer.eos_token_id,
    )
    filler_text = tokenizer.decode(completion_ids, skip_special_tokens=True)
    filler_prediction = parse_model_answer(filler_text, example["answer"])

    baseline_messages = build_messages(
        few_shot, example, filler_type, 0, task_type=task_type
    )
    baseline_rendered = encode_messages(baseline_messages, thinking_mode="chat")
    baseline_ids = tokenizer.encode(baseline_rendered)
    baseline_completion_ids, baseline_logits = greedy_generate(
        model,
        baseline_ids,
        max_new_tokens=max_new_tokens,
        eos_id=tokenizer.eos_token_id,
    )
    baseline_text = tokenizer.decode(baseline_completion_ids, skip_special_tokens=True)
    baseline_prediction = parse_model_answer(baseline_text, example["answer"])

    collapsed_final = collapse_streams(model, captured[42])[0]
    final_local = local_unembed(model, collapsed_final[-1:])
    shard = final_local.shape[-1]
    actual_local = actual_logits[:, rank * shard : (rank + 1) * shard]
    closure_error = all_reduce(
        (final_local - actual_local).abs().max(), dist.ReduceOp.MAX
    )

    if rank != 0:
        return None
    assert readouts is not None
    return {
        "schema_version": 1,
        "example": example,
        "condition": {
            "task_type": task_type,
            "filler_type": filler_type,
            "filler_length": filler_length,
        },
        "messages": messages,
        "rendered_prompt": rendered,
        "alignment": alignment.to_dict(),
        "selected_columns": columns,
        "tracked_token_variants": variants,
        "readouts": readouts,
        "model_output": {
            "actual_prompt_logits": full_logits_summary(actual_logits[0], tokenizer, top_k),
            "generation_first_logits": full_logits_summary(first_logits[0], tokenizer, top_k),
            "generated_token_ids": completion_ids,
            "generated_text": filler_text,
            "parsed_answer": filler_prediction,
            "correct": answer_is_correct(filler_prediction, example["answer"]),
        },
        "no_filler_control": {
            "rendered_prompt": baseline_rendered,
            "input_ids": baseline_ids,
            "actual_prompt_logits": full_logits_summary(baseline_logits[0], tokenizer, top_k),
            "generated_token_ids": baseline_completion_ids,
            "generated_text": baseline_text,
            "parsed_answer": baseline_prediction,
            "correct": answer_is_correct(baseline_prediction, example["answer"]),
        },
        "compatibility_checks": {
            "raw_layer_shape": list(captured[layers[0]].shape),
            "collapsed_shape": list(
                collapse_streams(model, captured[layers[0]]).shape
            ),
            "layer_42_final_head_closure_max_abs_error": float(closure_error.cpu()),
        },
    }


def expand_experiment_examples(experiment: dict[str, Any]) -> list[dict[str, Any]]:
    """Expand a compact repeated-squaring T sweep into ordinary example records."""
    examples = experiment.get("examples")
    sweep = experiment.get("sweep")
    if examples is not None and sweep is not None:
        raise ValueError("examples and sweep are mutually exclusive")
    if examples is not None:
        return list(examples)
    if sweep is None:
        raise ValueError("experiment must define examples or sweep")
    if experiment.get("task_type") != "repeated_squaring_mod":
        raise ValueError("compact sweep expansion is only supported for repeated squaring")

    time_steps = [int(value) for value in sweep["time_steps"]]
    if not time_steps or min(time_steps) < 1 or len(set(time_steps)) != len(time_steps):
        raise ValueError("sweep time_steps must be unique positive integers")
    maximum = max(time_steps)
    expanded: list[dict[str, Any]] = []
    for base in sweep["base_instances"]:
        modulus = int(base["modulus"])
        value = int(base["x"]) % modulus
        trace: list[int] = []
        for _ in range(maximum):
            value = value * value % modulus
            trace.append(value)
        for step in time_steps:
            intermediates = {
                f"x_{index}": str(residue)
                for index, residue in enumerate(trace[:step], start=1)
            }
            expanded.append(
                {
                    **base,
                    "id": f"repeated_squaring_n{modulus}_x{base['x']}_t{step}",
                    "time_steps": step,
                    "answer": trace[step - 1],
                    "expected_intermediates": intermediates,
                    "highlight_forms": {
                        label: [surface] for label, surface in intermediates.items()
                    },
                }
            )
    return expanded


def paired_eval_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    def summarize(items: list[dict[str, Any]]) -> dict[str, Any]:
        count = len(items)
        dots_correct = sum(item["dots"]["correct"] for item in items)
        no_dots_correct = sum(item["no_dots"]["correct"] for item in items)
        dots_only = sum(
            item["dots"]["correct"] and not item["no_dots"]["correct"]
            for item in items
        )
        no_dots_only = sum(
            item["no_dots"]["correct"] and not item["dots"]["correct"]
            for item in items
        )
        both = sum(
            item["dots"]["correct"] and item["no_dots"]["correct"]
            for item in items
        )
        neither = count - dots_only - no_dots_only - both
        improved_rank = sum(
            item["dots"]["target"]["best_rank"]
            < item["no_dots"]["target"]["best_rank"]
            for item in items
        )
        worsened_rank = sum(
            item["dots"]["target"]["best_rank"]
            > item["no_dots"]["target"]["best_rank"]
            for item in items
        )
        tied_rank = count - improved_rank - worsened_rank
        return {
            "n": count,
            "dots_accuracy": dots_correct / count,
            "no_dots_accuracy": no_dots_correct / count,
            "accuracy_difference": (dots_correct - no_dots_correct) / count,
            "paired_outcomes": {
                "dots_only_correct": dots_only,
                "no_dots_only_correct": no_dots_only,
                "both_correct": both,
                "neither_correct": neither,
            },
            "mean_reciprocal_rank": {
                "dots": sum(1 / item["dots"]["target"]["best_rank"] for item in items)
                / count,
                "no_dots": sum(
                    1 / item["no_dots"]["target"]["best_rank"] for item in items
                )
                / count,
            },
            "mean_target_log_probability": {
                "dots": sum(
                    item["dots"]["target"]["best_log_probability"]
                    for item in items
                )
                / count,
                "no_dots": sum(
                    item["no_dots"]["target"]["best_log_probability"]
                    for item in items
                )
                / count,
            },
            "target_rank_pairing": {
                "dots_better": improved_rank,
                "no_dots_better": worsened_rank,
                "tied": tied_rank,
            },
        }

    per_t = {}
    for step in sorted({row["time_steps"] for row in rows}):
        per_t[str(step)] = summarize(
            [row for row in rows if row["time_steps"] == step]
        )
    return {"overall": summarize(rows), "by_time_steps": per_t}


def configured_filler_lengths(experiment: dict[str, Any]) -> list[int] | None:
    """Validate an optional behavioral filler-length sweep."""
    raw = experiment.get("filler_lengths")
    if raw is None:
        return None
    if "filler_length" in experiment:
        raise ValueError("filler_length and filler_lengths are mutually exclusive")
    lengths = [int(value) for value in raw]
    if not lengths or lengths != sorted(set(lengths)):
        raise ValueError("filler_lengths must be unique and increasing")
    if lengths[0] != 0:
        raise ValueError("filler_lengths must begin with the no-filler baseline 0")
    return lengths


@torch.inference_mode()
def run_filler_length_sweep(
    *,
    model: Any,
    tokenizer: Any,
    encode_messages: Any,
    few_shot: list[dict[str, Any]],
    examples: list[dict[str, Any]],
    filler_type: str,
    filler_lengths: list[int],
    task_type: str,
    top_k: int,
    max_new_tokens: int,
    rank: int,
) -> dict[str, Any] | None:
    """Evaluate each example once at every configured filler length.

    Unlike ``run_paired_task_eval``, this computes the k=0 condition only once
    and reuses it as the paired baseline for every positive length.
    """
    rows = [] if rank == 0 else None
    for number, example in enumerate(examples, start=1):
        if rank == 0:
            print(
                f"length sweep {number}/{len(examples)}: {example['id']}",
                flush=True,
            )
        conditions: dict[str, Any] | None = {} if rank == 0 else None
        for filler_length in filler_lengths:
            messages = build_messages(
                few_shot,
                example,
                filler_type,
                filler_length,
                task_type=task_type,
            )
            if filler_length:
                rendered, alignment = render_and_align(
                    tokenizer,
                    encode_messages,
                    messages,
                    filler_type,
                    filler_length,
                    filler_placement=filler_placement_for_task(task_type),
                )
                check_filler_token_count(filler_type, filler_length, alignment.filler_token_indices, example["id"])
                input_ids = alignment.input_ids
                token_strings = alignment.token_strings
                filler_token_indices = alignment.filler_token_indices
            else:
                rendered = encode_messages(messages, thinking_mode="chat")
                input_ids = tokenizer.encode(rendered)
                token_strings = [tokenizer.decode([token_id]) for token_id in input_ids]
                filler_token_indices = []
            if len(input_ids) >= model.max_seq_len:
                raise AssertionError(
                    f"{example['id']} at k={filler_length}: prompt has "
                    f"{len(input_ids)} tokens, model limit is {model.max_seq_len}"
                )

            completion_ids, first_logits = greedy_generate(
                model,
                input_ids,
                max_new_tokens=max_new_tokens,
                eos_id=tokenizer.eos_token_id,
            )
            if rank == 0:
                assert conditions is not None
                generated_text = tokenizer.decode(
                    completion_ids, skip_special_tokens=True
                )
                parsed_answer = parse_model_answer(generated_text, example["answer"])
                conditions[str(filler_length)] = {
                    "filler_length": filler_length,
                    "rendered_prompt": rendered,
                    "input_ids": input_ids,
                    "token_strings": token_strings,
                    "filler_token_indices": filler_token_indices,
                    "generated_token_ids": completion_ids,
                    "generated_text": generated_text,
                    "parsed_answer": parsed_answer,
                    "correct": answer_is_correct(parsed_answer, example["answer"]),
                    "target": target_logit_summary(
                        first_logits[0], tokenizer, example["answer"]
                    ),
                    "top_tokens": full_logits_summary(
                        first_logits[0], tokenizer, top_k
                    )["top_tokens"],
                }

        if rank == 0:
            assert rows is not None and conditions is not None
            rows.append(
                {
                    "id": example["id"],
                    "example": example,
                    "expected_answer": example["answer"],
                    "expected_intermediates": example.get(
                        "expected_intermediates", {}
                    ),
                    "conditions": conditions,
                }
            )

    if rank != 0:
        return None
    assert rows is not None
    return {
        "schema_version": 1,
        "task_type": task_type,
        "filler_type": filler_type,
        "filler_lengths": filler_lengths,
        "examples": rows,
    }


@torch.inference_mode()
def run_paired_task_eval(
    *,
    model: Any,
    tokenizer: Any,
    encode_messages: Any,
    few_shot: list[dict[str, Any]],
    examples: list[dict[str, Any]],
    filler_type: str,
    filler_length: int,
    task_type: str,
    top_k: int,
    max_new_tokens: int,
    rank: int,
) -> dict[str, Any] | None:
    """Evaluate paired dot/no-dot generations without computing lens readouts."""
    rows = [] if rank == 0 else None
    for number, example in enumerate(examples, start=1):
        if rank == 0:
            print(
                f"paired eval {number}/{len(examples)}: {example['id']}",
                flush=True,
            )
        dots_messages = build_messages(
            few_shot,
            example,
            filler_type,
            filler_length,
            task_type=task_type,
        )
        dots_rendered, alignment = render_and_align(
            tokenizer,
            encode_messages,
            dots_messages,
            filler_type,
            filler_length,
        )
        check_filler_token_count(filler_type, filler_length, alignment.filler_token_indices, example["id"])
        dots_ids, dots_logits = greedy_generate(
            model,
            alignment.input_ids,
            max_new_tokens=max_new_tokens,
            eos_id=tokenizer.eos_token_id,
        )

        no_dots_messages = build_messages(
            few_shot, example, filler_type, 0, task_type=task_type
        )
        no_dots_rendered = encode_messages(no_dots_messages, thinking_mode="chat")
        no_dots_input_ids = tokenizer.encode(no_dots_rendered)
        no_dots_ids, no_dots_logits = greedy_generate(
            model,
            no_dots_input_ids,
            max_new_tokens=max_new_tokens,
            eos_id=tokenizer.eos_token_id,
        )

        if rank == 0:
            assert rows is not None
            dots_text = tokenizer.decode(dots_ids, skip_special_tokens=True)
            no_dots_text = tokenizer.decode(no_dots_ids, skip_special_tokens=True)
            dots_answer = parse_numeric_answer(dots_text)
            no_dots_answer = parse_numeric_answer(no_dots_text)
            rows.append(
                {
                    "id": example["id"],
                    "modulus": example["modulus"],
                    "x": example["x"],
                    "time_steps": example["time_steps"],
                    "expected_answer": example["answer"],
                    "expected_intermediates": example["expected_intermediates"],
                    "dots": {
                        "rendered_prompt": dots_rendered,
                        "input_ids": alignment.input_ids,
                        "token_strings": alignment.token_strings,
                        "filler_token_indices": alignment.filler_token_indices,
                        "generated_token_ids": dots_ids,
                        "generated_text": dots_text,
                        "parsed_answer": dots_answer,
                        "correct": dots_answer == example["answer"],
                        "target": target_logit_summary(
                            dots_logits[0], tokenizer, example["answer"]
                        ),
                        "top_tokens": full_logits_summary(
                            dots_logits[0], tokenizer, top_k
                        )["top_tokens"],
                    },
                    "no_dots": {
                        "rendered_prompt": no_dots_rendered,
                        "input_ids": no_dots_input_ids,
                        "token_strings": [
                            tokenizer.decode([token_id])
                            for token_id in no_dots_input_ids
                        ],
                        "generated_token_ids": no_dots_ids,
                        "generated_text": no_dots_text,
                        "parsed_answer": no_dots_answer,
                        "correct": no_dots_answer == example["answer"],
                        "target": target_logit_summary(
                            no_dots_logits[0], tokenizer, example["answer"]
                        ),
                        "top_tokens": full_logits_summary(
                            no_dots_logits[0], tokenizer, top_k
                        )["top_tokens"],
                    },
                }
            )
    if rank != 0:
        return None
    assert rows is not None
    return {
        "schema_version": 1,
        "task_type": task_type,
        "filler_type": filler_type,
        "filler_length": filler_length,
        "examples": rows,
        "summary": paired_eval_summary(rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--lens-path", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--phase", choices=["sanity", "eval", "filler", "all"], default="all"
    )
    parser.add_argument("--layers", default="all")
    parser.add_argument("--sanity-layers", default="0,5,10,15,20,25,30,35,40,41")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--max-new-tokens", type=int, default=12)
    parser.add_argument("--max-seq-len", type=int, default=1024)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument(
        "--example-ids",
        default="",
        help="optional comma-separated subset of configured example IDs",
    )
    parser.add_argument("--process-group-timeout-minutes", type=int, default=30)
    parser.add_argument(
        "--render",
        choices=["chat", "plain"],
        default="chat",
        help="chat: official encode_messages (non-thinking); plain: raw few-shot text for base models",
    )
    args = parser.parse_args()

    rank, local_rank, world_size = distributed_setup(
        args.process_group_timeout_minutes
    )
    if world_size != 4:
        raise SystemExit(f"converted checkpoint requires world_size=4, got {world_size}")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_default_dtype(torch.bfloat16)
    torch.set_num_threads(8)
    torch.manual_seed(42)

    sys.path.insert(0, str(args.reference_code_dir.resolve()))
    encoding_dir = args.reference_code_dir.resolve().parent / "encoding"
    sys.path.insert(0, str(encoding_dir))
    from encoding_dsv4 import encode_messages as chat_encode_messages  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    def plain_encode_messages(messages: list[dict[str, str]], thinking_mode: str = "chat") -> str:
        """Raw few-shot text for a base checkpoint: no turn markers, demo answers inline."""
        parts: list[str] = []
        pending_user: str | None = None
        for message in messages:
            if message["role"] == "system":
                parts.append(message["content"])
            elif message["role"] == "user":
                pending_user = message["content"]
            else:
                parts.append(f"{pending_user} {message['content']}")
                pending_user = None
        if pending_user is not None:
            parts.append(pending_user)
        return "\n\n".join(parts)

    encode_messages = chat_encode_messages if args.render == "chat" else plain_encode_messages

    with args.model_config.open() as handle:
        model_args = ModelArgs(**json.load(handle))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if rank == 0:
        print(f"loading model on {world_size} GPUs: {model_args}", flush=True)
    with torch.device("cuda"):
        model = Transformer(model_args)
    load_model(
        model,
        str(args.ckpt_path / f"model{rank}-mp{world_size}.safetensors"),
        strict=False,
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.ckpt_path)
    if len(tokenizer) != model_args.vocab_size:
        raise AssertionError(
            f"tokenizer has {len(tokenizer)} tokens, model expects {model_args.vocab_size}"
        )
    torch.set_default_device("cuda")
    barrier()

    checkpoint = torch.load(args.lens_path, map_location="cpu", weights_only=True)
    required_keys = {"J", "n_prompts", "source_layers", "d_model", "provenance"}
    if not required_keys.issubset(checkpoint):
        raise AssertionError(f"lens keys missing: {required_keys - set(checkpoint)}")
    lens_j = {int(k): v for k, v in checkpoint["J"].items()}
    source_layers = list(map(int, checkpoint["source_layers"]))
    if source_layers != list(range(42)):
        raise AssertionError(f"expected lens layers 0..41, got {source_layers}")
    if checkpoint["d_model"] != 4096:
        raise AssertionError(f"lens d_model is {checkpoint['d_model']}, expected 4096")
    for layer, matrix in lens_j.items():
        if tuple(matrix.shape) != (4096, 4096):
            raise AssertionError(f"J[{layer}] shape {tuple(matrix.shape)}")
    anchor_error = float(
        (lens_j[41].float() - torch.eye(4096, device="cpu")).abs().max()
    )
    if anchor_error != 0.0:
        raise AssertionError(f"lens target-layer anchor is not identity: {anchor_error}")

    experiment = json.loads(args.examples_config.read_text())
    filler_lengths = configured_filler_lengths(experiment)
    examples = expand_experiment_examples(experiment)
    if args.example_ids:
        requested = {value.strip() for value in args.example_ids.split(",") if value.strip()}
        available = {example["id"] for example in examples}
        missing = requested - available
        if missing:
            raise ValueError(f"requested example IDs are absent: {sorted(missing)}")
        examples = [example for example in examples if example["id"] in requested]
    layers = parse_layers(args.layers, set(source_layers))
    sanity_layers = parse_layers(args.sanity_layers, set(source_layers))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    runtime = None
    if rank == 0:
        import transformers

        runtime = {
            "timestamp_unix": time.time(),
            "platform": platform.platform(),
            "python": sys.version,
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "packages": {
                distribution: installed_version(distribution)
                for distribution in (
                    "tilelang",
                    "apache-tvm-ffi",
                    "safetensors",
                    "fast_hadamard_transform",
                    "numpy",
                )
            },
            "cuda": torch.version.cuda,
            "world_size": world_size,
            "gpus": [
                {
                    "index": idx,
                    "name": torch.cuda.get_device_name(idx),
                    "total_memory_bytes": torch.cuda.get_device_properties(idx).total_memory,
                }
                for idx in range(torch.cuda.device_count())
            ],
            "model_revision": args.model_revision,
            "experiment_config": {
                "path": str(args.examples_config),
                "sha256": file_sha256(args.examples_config),
            },
            "inference": {
                "seed": 42,
                "top_k": args.top_k,
                "max_new_tokens": args.max_new_tokens,
                "max_seq_len": args.max_seq_len,
                "thinking_mode": "chat (official non-thinking renderer)" if args.render == "chat" else "plain few-shot text (base model)",
                "render": args.render,
                "decoding": "greedy",
            },
            "model_config": vars(model_args),
            "tokenizer": {
                "class": type(tokenizer).__name__,
                "base_vocab_size": tokenizer.vocab_size,
                "length_with_added_tokens": len(tokenizer),
                "bos_token_id": tokenizer.bos_token_id,
                "eos_token_id": tokenizer.eos_token_id,
                "tokenizer_json_sha256": file_sha256(
                    args.ckpt_path / "tokenizer.json"
                ),
                "tokenizer_config_json_sha256": file_sha256(
                    args.ckpt_path / "tokenizer_config.json"
                ),
            },
            "reference_code": {
                name: {
                    "path": str(path),
                    "sha256": file_sha256(path),
                }
                for name, path in {
                    "model.py": args.reference_code_dir / "model.py",
                    "kernel.py": args.reference_code_dir / "kernel.py",
                    "encoding_dsv4.py": encoding_dir / "encoding_dsv4.py",
                }.items()
            },
            "lens": {
                "path": str(args.lens_path),
                "sha256": file_sha256(args.lens_path),
                "n_prompts": checkpoint["n_prompts"],
                "d_model": checkpoint["d_model"],
                "source_layers": source_layers,
                "provenance": checkpoint["provenance"],
                "target_anchor_max_abs_error_from_identity": anchor_error,
            },
            "activation_convention": {
                "captured": "post-block raw mHC output [B,S,4,4096]",
                "lens_input": "model.head.hc_head(post_block_mHC) [B,S,4096]",
                "normalization": "model.norm after optional J transport",
                "unembedding": "rank-sharded model.head.weight, globally merged",
                "warning": (
                    "The square lens checkpoint omits an explicit source projection. "
                    "Applying the model's final hc_head per layer is the unique model-native "
                    "4096-wide readout compatible with its matrices, but this convention is inferred."
                ),
            },
        }
        (args.output_dir / "runtime.json").write_text(
            json.dumps(runtime, indent=2, ensure_ascii=False)
        )

    if args.phase in {"sanity", "all"}:
        sanity = ordinary_sanity(
            model=model,
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            prompts=experiment["sanity_prompts"],
            lens_j=lens_j,
            layers=sanity_layers,
            top_k=args.top_k,
            rank=rank,
            world_size=world_size,
        )
        if rank == 0:
            assert sanity is not None
            (args.output_dir / "sanity.json").write_text(
                json.dumps(sanity, indent=2, ensure_ascii=False)
            )
            failures = [
                item["id"]
                for item in sanity
                if not item["layer_42_closure"]["top1_matches_actual"]
                or item["layer_42_closure"]["max_absolute_logit_error"] > 1e-4
                or not item["late_layer_checks"][
                    "layer_41_j_vs_ll_ordered_topk_exact"
                ]
            ]
            gate = {"passed": not failures, "failed_prompts": failures}
            (args.output_dir / "sanity_gate.json").write_text(
                json.dumps(gate, indent=2)
            )
            print(f"sanity gate: {gate}", flush=True)
        barrier()
        gate_tensor = torch.tensor(
            [0 if rank == 0 and failures else 1], dtype=torch.int32, device="cuda"
        )
        if world_size > 1:
            dist.broadcast(gate_tensor, src=0)
        if int(gate_tensor.item()) != 1:
            raise SystemExit("sanity gate failed; refusing filler extraction")

    if args.phase == "eval":
        if filler_lengths is not None:
            evaluation = run_filler_length_sweep(
                model=model,
                tokenizer=tokenizer,
                encode_messages=encode_messages,
                few_shot=experiment["few_shot"],
                examples=examples,
                filler_type=experiment["filler_type"],
                filler_lengths=filler_lengths,
                task_type=experiment.get("task_type", "addition"),
                top_k=args.top_k,
                max_new_tokens=args.max_new_tokens,
                rank=rank,
            )
            output_name = "filler_length_sweep.json"
        else:
            evaluation = run_paired_task_eval(
                model=model,
                tokenizer=tokenizer,
                encode_messages=encode_messages,
                few_shot=experiment["few_shot"],
                examples=examples,
                filler_type=experiment["filler_type"],
                filler_length=experiment["filler_length"],
                task_type=experiment.get("task_type", "addition"),
                top_k=args.top_k,
                max_new_tokens=args.max_new_tokens,
                rank=rank,
            )
            output_name = "paired_task_eval.json"
        if rank == 0:
            assert evaluation is not None
            path = args.output_dir / output_name
            path.write_text(json.dumps(evaluation, indent=2, ensure_ascii=False))
            print(f"wrote {path}", flush=True)

    if args.phase in {"filler", "all"}:
        extraction_lengths = (
            [length for length in filler_lengths if length > 0]
            if filler_lengths is not None
            else [int(experiment["filler_length"])]
        )
        if not extraction_lengths:
            raise ValueError("filler extraction requires at least one positive length")
        multi_length = filler_lengths is not None
        for filler_length in extraction_lengths:
            length_output_dir = (
                args.output_dir / f"k{filler_length}"
                if multi_length
                else args.output_dir
            )
            if rank == 0:
                length_output_dir.mkdir(parents=True, exist_ok=True)
            barrier()
            for example in examples:
                result = run_filler_example(
                    model=model,
                    tokenizer=tokenizer,
                    encode_messages=encode_messages,
                    few_shot=experiment["few_shot"],
                    example=example,
                    filler_type=experiment["filler_type"],
                    filler_length=filler_length,
                    task_type=experiment.get("task_type", "addition"),
                    lens_j=lens_j,
                    layers=layers,
                    top_k=args.top_k,
                    max_new_tokens=args.max_new_tokens,
                    rank=rank,
                    world_size=world_size,
                )
                if rank == 0:
                    assert result is not None
                    result["runtime_file"] = (
                        "../runtime.json" if multi_length else "runtime.json"
                    )
                    path = length_output_dir / f"{example['id']}.json"
                    path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
                    print(f"wrote {path}", flush=True)

    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
