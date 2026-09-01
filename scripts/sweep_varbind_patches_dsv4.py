#!/usr/bin/env python3
"""Map single-cell causal influence across filler positions and layers.

For one matched variable-binding donor/target pair, patch exactly one raw
post-block mHC residual at a time. The resulting layer x filler-position map
can be compared directly with J-Lens and logit-lens scores from extraction.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
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
)
from patch_varbind_dsv4 import (  # noqa: E402
    capture_raw_layers,
    forward,
    local_max_all_ranks,
    patch_raw_layers,
    rank_summary,
    render_example,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--donor-id", required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--layers", default="29-38")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-seq-len", type=int, default=1024)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=60)
    parser.add_argument("--require-identical-token-layout", action="store_true")
    return parser.parse_args()


def parse_layers(spec: str) -> list[int]:
    values: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, stop = (int(value) for value in part.split("-", 1))
            if stop < start:
                raise ValueError(f"descending layer range: {part}")
            values.update(range(start, stop + 1))
        else:
            values.add(int(part))
    layers = sorted(values)
    if not layers or min(layers) < 0 or max(layers) > 41:
        raise ValueError(f"invalid J-Lens layer set: {layers}")
    return layers


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def main() -> None:
    args = parse_args()
    layers = parse_layers(args.layers)
    rank, _local_rank, world_size = distributed_setup(
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
        print(f"loading single-cell sweep model on {world_size} GPUs", flush=True)
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
    examples = {example["id"]: example for example in experiment["examples"]}
    donor_example = examples[args.donor_id]
    target_example = examples[args.target_id]
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
    if len(donor_alignment.filler_token_indices) != len(
        target_alignment.filler_token_indices
    ):
        raise AssertionError("donor and target must have the same filler count")
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
    filler_count = len(target_alignment.filler_token_indices)

    if rank == 0:
        print(
            f"capturing {args.donor_id} -> {args.target_id}; "
            f"{len(layers)} layers x {filler_count} positions",
            flush=True,
        )
    with capture_raw_layers(
        model, layers, donor_alignment.filler_token_indices
    ) as donor_captured:
        donor_logits = forward(model, donor_alignment.input_ids)
    with capture_raw_layers(
        model, layers, target_alignment.filler_token_indices
    ) as target_captured:
        target_logits = forward(model, target_alignment.input_ids)
    if set(donor_captured) != set(layers) or set(target_captured) != set(layers):
        raise AssertionError("one or more requested residual hooks did not fire")

    # Exercise the same hook path used by the sweep before accepting any result.
    identity_cell = [{"layer": layers[0], "position": 1}]
    with patch_raw_layers(
        model,
        identity_cell,
        target_captured,
        target_alignment.filler_token_indices,
    ):
        identity_logits = forward(model, target_alignment.input_ids)
    identity_error = local_max_all_ranks((identity_logits - target_logits).abs().max())
    if identity_error > 1e-4:
        raise AssertionError(f"identity patch closure failed: {identity_error}")

    donor_answer = donor_example["answer"]
    target_answer = target_example["answer"]
    output_path = args.output_dir / "single-cell-grid.json"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output: dict[str, Any] | None = None
    completed: set[tuple[int, int]] = set()
    if rank == 0:
        baseline_donor = rank_summary(target_logits, tokenizer, donor_answer)
        baseline_target = rank_summary(target_logits, tokenizer, target_answer)
        output = {
            "schema_version": 1,
            "intervention": (
                "one donor raw post-block mHC residual [B,S,4,4096] patched "
                "into the same filler ordinal of the target"
            ),
            "donor_id": args.donor_id,
            "target_id": args.target_id,
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
            "layers": layers,
            "filler_count": filler_count,
            "identity_patch_max_abs_logit_error": identity_error,
            "unpatched": {
                "donor_self_answer": rank_summary(
                    donor_logits, tokenizer, donor_answer
                ),
                "target_prompt_donor_answer": baseline_donor,
                "target_prompt_target_answer": baseline_target,
                "target_top_tokens": full_logits_summary(
                    target_logits[0], tokenizer, 10
                )["top_tokens"],
            },
            "cells": [],
            "runtime": {
                "timestamp_unix": time.time(),
                "platform": platform.platform(),
                "torch": torch.__version__,
                "world_size": world_size,
                "model_revision": args.model_revision,
                "model_config_sha256": file_sha256(args.model_config),
                "examples_config_sha256": file_sha256(args.examples_config),
                "seed": 42,
            },
        }
        write_json_atomic(output_path, output)

    for layer_number, layer in enumerate(layers, start=1):
        for position in range(1, filler_count + 1):
            cell = [{"layer": layer, "position": position}]
            with patch_raw_layers(
                model,
                cell,
                donor_captured,
                target_alignment.filler_token_indices,
            ):
                patched_logits = forward(model, target_alignment.input_ids)
            if rank == 0:
                assert output is not None
                donor_rank = rank_summary(patched_logits, tokenizer, donor_answer)
                target_rank = rank_summary(patched_logits, tokenizer, target_answer)
                baseline_donor = output["unpatched"]["target_prompt_donor_answer"]
                baseline_target = output["unpatched"]["target_prompt_target_answer"]
                output["cells"].append(
                    {
                        "layer": layer,
                        "position": position,
                        "absolute_index": target_alignment.filler_token_indices[
                            position - 1
                        ],
                        "donor_answer": donor_rank,
                        "target_answer": target_rank,
                        "donor_rank_improvement": (
                            baseline_donor["best_rank"] - donor_rank["best_rank"]
                        ),
                        "donor_log_probability_change": (
                            donor_rank["best_log_probability"]
                            - baseline_donor["best_log_probability"]
                        ),
                        "target_rank_worsening": (
                            target_rank["best_rank"] - baseline_target["best_rank"]
                        ),
                        "target_log_probability_change": (
                            target_rank["best_log_probability"]
                            - baseline_target["best_log_probability"]
                        ),
                        "top_token": full_logits_summary(
                            patched_logits[0], tokenizer, 1
                        )["top_tokens"][0],
                    }
                )
                completed.add((layer, position))
        if rank == 0:
            assert output is not None
            output["runtime"]["last_completed_layer"] = layer
            output["runtime"]["timestamp_unix"] = time.time()
            write_json_atomic(output_path, output)
            print(
                f"completed layer {layer} "
                f"({layer_number}/{len(layers)}; {len(completed)} cells)",
                flush=True,
            )

    if rank == 0:
        assert output is not None
        output["runtime"]["complete"] = True
        output["runtime"]["timestamp_unix"] = time.time()
        write_json_atomic(output_path, output)
        print(f"wrote {output_path}", flush=True)

    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
