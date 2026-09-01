#!/usr/bin/env python3
"""Causal residual-patching pilot for matched DeepSeek-V4 varbind examples.

Locations are selected offline from J-Lens/logit-lens readouts. This script
patches the model's raw post-block mHC residual [B,S,4,4096], preserving all
four streams, and measures exact next-token ranks for donor and target answers.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import torch
import torch.distributed as dist
from safetensors.torch import load_model
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from extract_dsv4 import (  # noqa: E402
    barrier,
    distributed_setup,
    file_sha256,
    full_logits_summary,
    target_logit_summary,
)
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--patch-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--doses", default="1,4,8,16")
    parser.add_argument("--stages", default="bound_value,second_product,answer")
    parser.add_argument("--max-seq-len", type=int, default=1024)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=30)
    parser.add_argument("--require-identical-token-layout", action="store_true")
    return parser.parse_args()


def output_tensor(output: Any) -> torch.Tensor:
    return output[0] if isinstance(output, tuple) else output


def replace_output_tensor(output: Any, tensor: torch.Tensor) -> Any:
    if not isinstance(output, tuple):
        return tensor
    values = list(output)
    values[0] = tensor
    return tuple(values)


@contextmanager
def capture_raw_layers(model: Any, layers: list[int], absolute_positions: list[int]):
    captured: dict[int, torch.Tensor] = {}
    handles = []

    def make_hook(layer: int):
        def hook(_module: Any, _inputs: Any, output: Any) -> None:
            tensor = output_tensor(output)
            if tensor.ndim != 4 or tensor.shape[-2:] != (4, 4096):
                raise AssertionError(
                    f"layer {layer}: expected [B,S,4,4096], got {tuple(tensor.shape)}"
                )
            captured[layer] = tensor[:, absolute_positions].detach().clone()

        return hook

    try:
        for layer in layers:
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield captured
    finally:
        for handle in handles:
            handle.remove()


@contextmanager
def patch_raw_layers(
    model: Any,
    cells: list[dict[str, Any]],
    donor_by_layer: dict[int, torch.Tensor],
    target_filler_indices: list[int],
):
    by_layer: dict[int, list[dict[str, Any]]] = {}
    for cell in cells:
        by_layer.setdefault(int(cell["layer"]), []).append(cell)
    handles = []

    def make_hook(layer: int):
        def hook(_module: Any, _inputs: Any, output: Any) -> Any:
            tensor = output_tensor(output)
            patched = tensor.clone()
            donor = donor_by_layer[layer]
            for cell in by_layer[layer]:
                ordinal = int(cell["position"])
                if not 1 <= ordinal <= len(target_filler_indices):
                    raise AssertionError(f"invalid filler ordinal: {ordinal}")
                target_absolute = target_filler_indices[ordinal - 1]
                patched[:, target_absolute] = donor[:, ordinal - 1]
            return replace_output_tensor(output, patched)

        return hook

    try:
        for layer in sorted(by_layer):
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield
    finally:
        for handle in handles:
            handle.remove()


def forward(model: Any, input_ids: list[int]) -> torch.Tensor:
    tokens = torch.tensor([input_ids], dtype=torch.long, device="cuda")
    return model.forward(tokens, 0).detach().clone()


def render_example(
    *, tokenizer: Any, encode_messages: Any, experiment: dict[str, Any], example: dict[str, Any]
) -> tuple[str, Any]:
    messages = build_messages(
        experiment["few_shot"],
        example,
        experiment["filler_type"],
        int(experiment["filler_length"]),
        task_type=experiment["task_type"],
    )
    rendered, alignment = render_and_align(
        tokenizer,
        encode_messages,
        messages,
        experiment["filler_type"],
        int(experiment["filler_length"]),
    )
    if len(alignment.filler_token_indices) != int(experiment["filler_length"]):
        raise AssertionError("visible fillers do not map one-to-one to model tokens")
    return rendered, alignment


def rank_summary(logits: torch.Tensor, tokenizer: Any, answer: Any) -> dict[str, Any]:
    return target_logit_summary(logits[0], tokenizer, answer)


def local_max_all_ranks(value: torch.Tensor) -> float:
    scalar = value.detach().float().reshape(1)
    if dist.is_initialized():
        dist.all_reduce(scalar, op=dist.ReduceOp.MAX)
    return float(scalar.cpu().item())


def main() -> None:
    args = parse_args()
    doses = [int(value) for value in args.doses.split(",") if value]
    stages = [value.strip() for value in args.stages.split(",") if value.strip()]
    if not doses or doses != sorted(set(doses)) or min(doses) < 1:
        raise ValueError("doses must be unique increasing positive integers")

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
    from encoding_dsv4 import encode_messages  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    model_args = ModelArgs(**json.loads(args.model_config.read_text(encoding="utf-8")))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if rank == 0:
        print(f"loading patching model on {world_size} GPUs", flush=True)
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
        raise AssertionError("tokenizer/model vocabulary mismatch")
    torch.set_default_device("cuda")
    barrier()

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    manifest = json.loads(args.patch_manifest.read_text(encoding="utf-8"))
    examples = {example["id"]: example for example in experiment["examples"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output: dict[str, Any] | None = (
        {
            "schema_version": 1,
            "intervention": (
                "donor raw post-block mHC residual [B,S,4,4096] patched into "
                "the same filler ordinal of the target"
            ),
            "doses": doses,
            "stages": stages,
            "directions": [],
        }
        if rank == 0
        else None
    )

    for direction_number, direction in enumerate(manifest["directions"], start=1):
        donor_id, target_id = direction["donor_id"], direction["target_id"]
        donor_example, target_example = examples[donor_id], examples[target_id]
        donor_rendered, donor_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=donor_example,
        )
        target_rendered, target_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=target_example,
        )
        layout_differences = [
            index
            for index, (donor_token, target_token) in enumerate(
                zip(donor_alignment.input_ids, target_alignment.input_ids)
            )
            if donor_token != target_token
        ]
        if args.require_identical_token_layout:
            if len(donor_alignment.input_ids) != len(target_alignment.input_ids):
                raise AssertionError(
                    "donor and target token lengths differ under exact-layout mode"
                )
            if donor_alignment.filler_token_indices != target_alignment.filler_token_indices:
                raise AssertionError(
                    "donor and target filler indices differ under exact-layout mode"
                )
            if len(layout_differences) != 1:
                raise AssertionError(
                    "exact-layout counterfactuals must differ at one token, got "
                    f"{layout_differences}"
                )
        requested_cells = [
            cell
            for strategy in direction["selections"].values()
            for stage in stages
            for cell in strategy[stage]
        ]
        layers = sorted({int(cell["layer"]) for cell in requested_cells})
        if rank == 0:
            print(
                f"direction {direction_number}: {donor_id} -> {target_id}, layers {layers}",
                flush=True,
            )
        with capture_raw_layers(
            model, layers, donor_alignment.filler_token_indices
        ) as donor_captured:
            donor_logits = forward(model, donor_alignment.input_ids)
        missing = set(layers) - set(donor_captured)
        if missing:
            raise AssertionError(f"donor hooks missed layers {sorted(missing)}")
        target_logits = forward(model, target_alignment.input_ids)

        donor_answer = donor_example["answer"]
        target_answer = target_example["answer"]
        baseline_donor_rank = rank_summary(target_logits, tokenizer, donor_answer) if rank == 0 else None
        baseline_target_rank = rank_summary(target_logits, tokenizer, target_answer) if rank == 0 else None
        donor_self_rank = rank_summary(donor_logits, tokenizer, donor_answer) if rank == 0 else None

        # Identity closure: recapture the target and write its own selected streams back.
        identity_cells = direction["selections"]["j_lens"]["bound_value"]
        identity_layers = sorted({int(cell["layer"]) for cell in identity_cells})
        with capture_raw_layers(
            model, identity_layers, target_alignment.filler_token_indices
        ) as target_captured:
            identity_reference = forward(model, target_alignment.input_ids)
        with patch_raw_layers(
            model,
            identity_cells,
            target_captured,
            target_alignment.filler_token_indices,
        ):
            identity_logits = forward(model, target_alignment.input_ids)
        identity_error = local_max_all_ranks(
            (identity_logits - identity_reference).abs().max()
        )
        if identity_error > 1e-4:
            raise AssertionError(f"identity patch closure failed: {identity_error}")

        direction_output: dict[str, Any] | None = None
        if rank == 0:
            assert (
                output is not None
                and baseline_donor_rank is not None
                and baseline_target_rank is not None
                and donor_self_rank is not None
            )
            direction_output = {
                "donor_id": donor_id,
                "target_id": target_id,
                "donor_answer": donor_answer,
                "target_answer": target_answer,
                "donor_intermediates": donor_example["expected_intermediates"],
                "target_intermediates": target_example["expected_intermediates"],
                "donor_rendered_prompt": donor_rendered,
                "target_rendered_prompt": target_rendered,
                "input_token_differences": [
                    {
                        "absolute_index": index,
                        "donor_token_id": donor_alignment.input_ids[index],
                        "donor_token": tokenizer.decode(
                            [donor_alignment.input_ids[index]],
                            skip_special_tokens=False,
                        ),
                        "target_token_id": target_alignment.input_ids[index],
                        "target_token": tokenizer.decode(
                            [target_alignment.input_ids[index]],
                            skip_special_tokens=False,
                        ),
                    }
                    for index in layout_differences
                ],
                "identity_patch_max_abs_logit_error": identity_error,
                "unpatched": {
                    "donor_self_answer": donor_self_rank,
                    "target_prompt_donor_answer": baseline_donor_rank,
                    "target_prompt_target_answer": baseline_target_rank,
                    "target_top_tokens": full_logits_summary(
                        target_logits[0], tokenizer, 10
                    )["top_tokens"],
                },
                "patches": [],
            }

        for stage in stages:
            for strategy in (
                "j_lens",
                "logit_lens",
                "random_layer_matched",
                "complement_layer_matched",
            ):
                configured = direction["selections"][strategy][stage]
                if max(doses) > len(configured):
                    raise ValueError(
                        f"dose {max(doses)} exceeds {strategy}/{stage} selection"
                    )
                for dose in doses:
                    cells = configured[:dose]
                    with patch_raw_layers(
                        model,
                        cells,
                        donor_captured,
                        target_alignment.filler_token_indices,
                    ):
                        patched_logits = forward(model, target_alignment.input_ids)
                    if rank == 0:
                        assert (
                            direction_output is not None
                            and baseline_donor_rank is not None
                            and baseline_target_rank is not None
                        )
                        donor_rank = rank_summary(
                            patched_logits, tokenizer, donor_answer
                        )
                        target_rank = rank_summary(
                            patched_logits, tokenizer, target_answer
                        )
                        top = full_logits_summary(patched_logits[0], tokenizer, 5)[
                            "top_tokens"
                        ]
                        direction_output["patches"].append(
                            {
                                "stage": stage,
                                "strategy": strategy,
                                "dose": dose,
                                "cells": cells,
                                "donor_answer": donor_rank,
                                "target_answer": target_rank,
                                "donor_rank_improvement": (
                                    baseline_donor_rank["best_rank"]
                                    - donor_rank["best_rank"]
                                ),
                                "donor_log_probability_change": (
                                    donor_rank["best_log_probability"]
                                    - baseline_donor_rank["best_log_probability"]
                                ),
                                "target_rank_worsening": (
                                    target_rank["best_rank"]
                                    - baseline_target_rank["best_rank"]
                                ),
                                "target_log_probability_change": (
                                    target_rank["best_log_probability"]
                                    - baseline_target_rank["best_log_probability"]
                                ),
                                "top_tokens": top,
                                "full_donor_answer_swap": (
                                    top[0]["token"].strip() == str(donor_answer)
                                ),
                            }
                        )
        if rank == 0:
            assert output is not None and direction_output is not None
            output["directions"].append(direction_output)

    if rank == 0:
        assert output is not None
        output["runtime"] = {
            "timestamp_unix": time.time(),
            "platform": platform.platform(),
            "torch": torch.__version__,
            "world_size": world_size,
            "model_revision": args.model_revision,
            "model_config_sha256": file_sha256(args.model_config),
            "examples_config_sha256": file_sha256(args.examples_config),
            "patch_manifest_sha256": file_sha256(args.patch_manifest),
            "seed": 42,
        }
        path = args.output_dir / "patch-results.json"
        path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {path}", flush=True)

    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
