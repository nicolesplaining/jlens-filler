#!/usr/bin/env python3
"""Test interchangeability and necessity of filler-position workspace lanes.

Two interventions go beyond same-position counterfactual patching:

1. Cross-position transplant: move one donor state decoded as an intermediate
   into many different target filler positions at the same layer.
2. Mean lesion: replace readout-selected or layer-matched-random cells in a
   correct donor run with that layer's mean filler residual.

The first distinguishes interchangeable workspace slots from position-addressed
channels.  The second tests necessity/redundancy with a matched control.
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
from patch_varbind_dsv4 import (  # noqa: E402
    capture_raw_layers,
    forward,
    output_tensor,
    replace_output_tensor,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--patch-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stages", default="second_product,answer")
    parser.add_argument("--source-cells", type=int, default=1)
    parser.add_argument("--destination-stride", type=int, default=1)
    parser.add_argument("--lesion-doses", default="1,4,8,16")
    parser.add_argument("--max-seq-len", type=int, default=1024)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=30)
    parser.add_argument("--require-identical-token-layout", action="store_true")
    return parser.parse_args()


def render_example(
    *, tokenizer: Any, encode_messages: Any, experiment: dict[str, Any], example: dict[str, Any]
) -> tuple[str, Any]:
    filler_length = int(experiment["filler_length"])
    messages = build_messages(
        experiment["few_shot"],
        example,
        experiment["filler_type"],
        filler_length,
        task_type=experiment["task_type"],
    )
    rendered, alignment = render_and_align(
        tokenizer,
        encode_messages,
        messages,
        experiment["filler_type"],
        filler_length,
    )
    if len(alignment.filler_token_indices) != filler_length:
        raise AssertionError("visible fillers do not map one-to-one to model tokens")
    return rendered, alignment


def rank_summary(logits: torch.Tensor, tokenizer: Any, answer: Any) -> dict[str, Any]:
    return target_logit_summary(logits[0], tokenizer, answer)


def distributed_max(value: torch.Tensor) -> float:
    scalar = value.detach().float().reshape(1)
    if dist.is_initialized():
        dist.all_reduce(scalar, op=dist.ReduceOp.MAX)
    return float(scalar.cpu().item())


@contextmanager
def patch_from_captured(
    model: Any,
    specs: list[dict[str, Any]],
    captured: dict[int, torch.Tensor],
    target_filler_indices: list[int],
):
    """Patch target cells with a captured source position or layer mean."""
    by_layer: dict[int, list[dict[str, Any]]] = {}
    for spec in specs:
        by_layer.setdefault(int(spec["layer"]), []).append(spec)
    handles = []

    def make_hook(layer: int):
        def hook(_module: Any, _inputs: Any, output: Any) -> Any:
            tensor = output_tensor(output)
            patched = tensor.clone()
            source = captured[layer]
            occupied: set[int] = set()
            for spec in by_layer[layer]:
                target_position = int(spec["target_position"])
                if not 1 <= target_position <= len(target_filler_indices):
                    raise AssertionError(f"invalid target filler ordinal {target_position}")
                target_absolute = target_filler_indices[target_position - 1]
                if target_absolute in occupied:
                    raise AssertionError("duplicate target cell in one intervention")
                occupied.add(target_absolute)
                if spec["source"] == "mean":
                    value = source.mean(dim=1)
                else:
                    source_position = int(spec["source_position"])
                    if not 1 <= source_position <= source.shape[1]:
                        raise AssertionError(
                            f"invalid source filler ordinal {source_position}"
                        )
                    value = source[:, source_position - 1]
                patched[:, target_absolute] = value
            return replace_output_tensor(output, patched)

        return hook

    try:
        for layer in sorted(by_layer):
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield
    finally:
        for handle in handles:
            handle.remove()


def summarize_change(
    *, logits: torch.Tensor, baseline: dict[str, Any], tokenizer: Any, answer: Any
) -> dict[str, Any]:
    result = rank_summary(logits, tokenizer, answer)
    return {
        **result,
        "rank_improvement": baseline["best_rank"] - result["best_rank"],
        "log_probability_change": (
            result["best_log_probability"] - baseline["best_log_probability"]
        ),
    }


def main() -> None:
    args = parse_args()
    stages = [value.strip() for value in args.stages.split(",") if value.strip()]
    doses = [int(value) for value in args.lesion_doses.split(",") if value]
    if not stages:
        raise ValueError("at least one stage is required")
    if args.source_cells < 1 or args.destination_stride < 1:
        raise ValueError("source-cells and destination-stride must be positive")
    if not doses or doses != sorted(set(doses)):
        raise ValueError("lesion doses must be unique and increasing")

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
    sys.path.insert(0, str(args.reference_code_dir.resolve().parent / "encoding"))
    from encoding_dsv4 import encode_messages  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    model_args = ModelArgs(**json.loads(args.model_config.read_text(encoding="utf-8")))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if rank == 0:
        print(f"loading workspace-probe model on {world_size} GPUs", flush=True)
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
    filler_count = int(experiment["filler_length"])
    destinations = sorted(
        set(range(1, filler_count + 1, args.destination_stride)) | {filler_count}
    )
    output: dict[str, Any] | None = (
        {
            "schema_version": 1,
            "interventions": {
                "cross_position": (
                    "one donor post-block mHC residual moved from a readout-selected "
                    "source dot into target destination dots at the same layer"
                ),
                "mean_lesion": (
                    "selected donor cells replaced by that layer's mean residual "
                    "across all filler positions"
                ),
            },
            "filler_count": filler_count,
            "stages": stages,
            "destinations": destinations,
            "directions": [],
        }
        if rank == 0
        else None
    )

    for direction_index, direction in enumerate(manifest["directions"], start=1):
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
        differences = [
            index
            for index, (left, right) in enumerate(
                zip(donor_alignment.input_ids, target_alignment.input_ids)
            )
            if left != right
        ]
        if args.require_identical_token_layout:
            if len(donor_alignment.input_ids) != len(target_alignment.input_ids):
                raise AssertionError("counterfactual token lengths differ")
            if donor_alignment.filler_token_indices != target_alignment.filler_token_indices:
                raise AssertionError("counterfactual filler indices differ")
            if len(differences) != 1:
                raise AssertionError(
                    f"exact-layout pair must differ once, got {differences}"
                )

        requested = [
            cell
            for strategy in ("j_lens", "random_layer_matched")
            for stage in stages
            for cell in direction["selections"][strategy][stage]
        ]
        layers = sorted({int(cell["layer"]) for cell in requested})
        if rank == 0:
            print(
                f"workspace direction {direction_index}/{len(manifest['directions'])}: "
                f"{donor_id} -> {target_id}",
                flush=True,
            )
        with capture_raw_layers(
            model, layers, donor_alignment.filler_token_indices
        ) as donor_captured:
            donor_logits = forward(model, donor_alignment.input_ids)
        target_logits = forward(model, target_alignment.input_ids)

        donor_answer = donor_example["answer"]
        target_answer = target_example["answer"]
        donor_baseline = rank_summary(donor_logits, tokenizer, donor_answer) if rank == 0 else None
        target_donor_baseline = rank_summary(target_logits, tokenizer, donor_answer) if rank == 0 else None
        target_self_baseline = rank_summary(target_logits, tokenizer, target_answer) if rank == 0 else None

        # Exact closure for the hook and captured tensor convention.
        identity_cell = direction["selections"]["j_lens"][stages[0]][0]
        identity_spec = {
            "layer": identity_cell["layer"],
            "target_position": identity_cell["position"],
            "source": "position",
            "source_position": identity_cell["position"],
        }
        with patch_from_captured(
            model,
            [identity_spec],
            donor_captured,
            donor_alignment.filler_token_indices,
        ):
            identity_logits = forward(model, donor_alignment.input_ids)
        identity_error = distributed_max((identity_logits - donor_logits).abs().max())
        if identity_error > 1e-4:
            raise AssertionError(f"identity patch closure failed: {identity_error}")

        direction_output: dict[str, Any] | None = None
        if rank == 0:
            assert donor_baseline and target_donor_baseline and target_self_baseline
            direction_output = {
                "family": direction.get("family"),
                "source_template_id": direction.get("source_template_id"),
                "donor_id": donor_id,
                "target_id": target_id,
                "donor_answer": donor_answer,
                "target_answer": target_answer,
                "input_token_differences": differences,
                "identity_patch_max_abs_logit_error": identity_error,
                "unpatched": {
                    "donor_self_answer": donor_baseline,
                    "target_prompt_donor_answer": target_donor_baseline,
                    "target_prompt_target_answer": target_self_baseline,
                    "donor_top_tokens": full_logits_summary(
                        donor_logits[0], tokenizer, 5
                    )["top_tokens"],
                },
                "cross_position": [],
                "mean_lesions": [],
            }

        for stage in stages:
            source_cells = direction["selections"]["j_lens"][stage][
                : args.source_cells
            ]
            for source_index, cell in enumerate(source_cells, start=1):
                for destination in destinations:
                    spec = {
                        "layer": int(cell["layer"]),
                        "target_position": destination,
                        "source": "position",
                        "source_position": int(cell["position"]),
                    }
                    with patch_from_captured(
                        model,
                        [spec],
                        donor_captured,
                        target_alignment.filler_token_indices,
                    ):
                        logits = forward(model, target_alignment.input_ids)
                    if rank == 0:
                        assert direction_output is not None and target_donor_baseline
                        direction_output["cross_position"].append(
                            {
                                "stage": stage,
                                "source_index": source_index,
                                "source_layer": int(cell["layer"]),
                                "source_position": int(cell["position"]),
                                "source_rank": int(cell["rank"]),
                                "destination_position": destination,
                                "donor_answer": summarize_change(
                                    logits=logits,
                                    baseline=target_donor_baseline,
                                    tokenizer=tokenizer,
                                    answer=donor_answer,
                                ),
                                "target_answer": summarize_change(
                                    logits=logits,
                                    baseline=target_self_baseline,
                                    tokenizer=tokenizer,
                                    answer=target_answer,
                                ),
                            }
                        )

            for strategy in ("j_lens", "random_layer_matched"):
                configured = direction["selections"][strategy][stage]
                for dose in doses:
                    if dose > len(configured):
                        raise ValueError(
                            f"dose {dose} exceeds {strategy}/{stage} selection"
                        )
                    specs = [
                        {
                            "layer": int(cell["layer"]),
                            "target_position": int(cell["position"]),
                            "source": "mean",
                        }
                        for cell in configured[:dose]
                    ]
                    with patch_from_captured(
                        model,
                        specs,
                        donor_captured,
                        donor_alignment.filler_token_indices,
                    ):
                        logits = forward(model, donor_alignment.input_ids)
                    if rank == 0:
                        assert direction_output is not None and donor_baseline
                        direction_output["mean_lesions"].append(
                            {
                                "stage": stage,
                                "strategy": strategy,
                                "dose": dose,
                                "cells": configured[:dose],
                                "donor_answer": summarize_change(
                                    logits=logits,
                                    baseline=donor_baseline,
                                    tokenizer=tokenizer,
                                    answer=donor_answer,
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
        args.output_dir.mkdir(parents=True, exist_ok=True)
        path = args.output_dir / "workspace-probe-results.json"
        path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {path}", flush=True)

    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
