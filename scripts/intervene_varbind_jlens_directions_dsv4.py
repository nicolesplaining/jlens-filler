#!/usr/bin/env python3
"""Causally suppress J-Lens-decoded token directions in DeepSeek-V4 fillers.

The existing patching experiments use J-Lens to choose a layer/position and then
replace the complete residual state.  This experiment is more specific.  At a
J-Lens-selected raw post-block mHC state ``X`` it differentiates one decoded token
logit through the exact model-native collapse

    X [4,4096] -> final hc_head -> J_l -> final RMSNorm -> token logit

and follows the minimum-norm first-order raw-stream direction that lowers that
score.  The requested local score drop is reached by line search, subject to a
relative-L2 cap.  Logit-lens, J-only (orthogonal to the logit-lens gradient),
counterfactual-token, and random directions receive the same raw L2 dose at the
same cells.

This is a decoder-gradient intervention, not a proof that the gradient is a unique
semantic feature.  The matched controls and downstream answer effects are the test.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import statistics
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import torch
import torch.distributed as dist
import torch.nn.functional as F
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
from jlens_filler.direction_intervention import (  # noqa: E402
    cosine,
    find_amplification_step,
    find_suppression_step,
    matched_delta,
    orthogonal_component,
    stable_seed,
    unit_direction,
)
from jlens_filler.prompts import (  # noqa: E402
    build_messages,
    render_and_align,
    token_variants,
)
from patch_varbind_dsv4 import (  # noqa: E402
    capture_raw_layers,
    forward,
    output_tensor,
    replace_output_tensor,
)


CONDITIONS = (
    "j_lens_target",
    "logit_lens_target",
    "j_lens_unique",
    "j_lens_counterfactual",
    "random_matched",
)


def parse_csv_ints(value: str) -> list[int]:
    values = [int(item) for item in value.split(",") if item.strip()]
    if not values or values != sorted(set(values)) or min(values) < 1:
        raise argparse.ArgumentTypeError("expected unique increasing positive integers")
    return values


def parse_csv_floats(value: str) -> list[float]:
    values = [float(item) for item in value.split(",") if item.strip()]
    if not values or values != sorted(set(values)) or min(values) <= 0:
        raise argparse.ArgumentTypeError("expected unique increasing positive numbers")
    return values


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--lens-path", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--patch-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stages", default="second_product,answer")
    parser.add_argument("--cell-doses", type=parse_csv_ints, default=parse_csv_ints("1,4,16"))
    parser.add_argument("--score-drops", type=parse_csv_floats, default=parse_csv_floats("2,4"))
    parser.add_argument("--conditions", default=",".join(CONDITIONS))
    parser.add_argument(
        "--intervention-mode",
        choices=("suppress", "counterfactual_amplify"),
        default="suppress",
        help=(
            "Suppress the correct decoded value in its own prompt, or run the "
            "paired target prompt and amplify the donor/counterfactual value."
        ),
    )
    parser.add_argument("--max-relative-norm", type=float, default=0.05)
    parser.add_argument("--max-directions", type=int)
    parser.add_argument("--max-seq-len", type=int, default=1280)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=60)
    parser.add_argument("--require-identical-token-layout", action="store_true")
    return parser.parse_args()


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def render_example(
    *,
    tokenizer: Any,
    encode_messages: Any,
    experiment: dict[str, Any],
    example: dict[str, Any],
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


def single_token_ids(tokenizer: Any, value: Any) -> list[int]:
    ids = sorted(
        {
            int(variant["token_ids"][0])
            for variant in token_variants(tokenizer, str(value))
            if variant["single_token"]
        }
    )
    if not ids:
        raise ValueError(f"{value!r} has no single-token tokenizer variant")
    return ids


def broadcast_unembedding_row(
    model: Any,
    token_id: int,
    *,
    rank: int,
    world_size: int,
) -> torch.Tensor:
    part_vocab = int(model.head.weight.shape[0])
    owner = token_id // part_vocab
    if not 0 <= owner < world_size:
        raise AssertionError(f"token {token_id} maps to invalid vocabulary shard {owner}")
    row = torch.zeros(4096, dtype=torch.float32, device="cuda")
    if rank == owner:
        row.copy_(model.head.weight[token_id - owner * part_vocab].float())
    if dist.is_initialized():
        dist.broadcast(row, src=owner)
    return row


def decoded_score(
    *,
    model: Any,
    raw_streams: torch.Tensor,
    unembedding_row: torch.Tensor,
    lens_matrix: torch.Tensor | None,
) -> torch.Tensor:
    if raw_streams.shape != (4, 4096):
        raise AssertionError(f"expected raw [4,4096], got {tuple(raw_streams.shape)}")
    collapsed = model.head.hc_head(
        raw_streams[None, None],
        model.hc_head_fn,
        model.hc_head_scale,
        model.hc_head_base,
    )[0, 0].float()
    decoded = F.linear(collapsed, lens_matrix) if lens_matrix is not None else collapsed
    normalized = model.norm(decoded).float()
    return torch.dot(normalized, unembedding_row.float())


def score_and_gradient(
    *,
    model: Any,
    raw_streams: torch.Tensor,
    unembedding_row: torch.Tensor,
    lens_matrix: torch.Tensor | None,
) -> tuple[float, torch.Tensor]:
    with torch.inference_mode(False), torch.enable_grad():
        activation = raw_streams.detach().clone().float().requires_grad_(True)
        score = decoded_score(
            model=model,
            raw_streams=activation,
            unembedding_row=unembedding_row,
            lens_matrix=lens_matrix,
        )
        gradient = torch.autograd.grad(score, activation, only_inputs=True)[0]
    return float(score.detach()), gradient.detach().float()


def choose_j_lens_variant(
    *,
    model: Any,
    raw_streams: torch.Tensor,
    token_ids: list[int],
    row_cache: dict[int, torch.Tensor],
    lens_matrix: torch.Tensor,
) -> tuple[int, float]:
    scored = []
    with torch.no_grad():
        for token_id in token_ids:
            scored.append(
                (
                    float(
                        decoded_score(
                            model=model,
                            raw_streams=raw_streams.float(),
                            unembedding_row=row_cache[token_id],
                            lens_matrix=lens_matrix,
                        )
                    ),
                    token_id,
                )
            )
    score, token_id = max(scored)
    return token_id, score


def random_direction_like(reference: torch.Tensor, *, seed: int) -> torch.Tensor:
    generator = torch.Generator(device=reference.device)
    generator.manual_seed(seed)
    return unit_direction(
        torch.randn(
            reference.shape,
            dtype=torch.float32,
            device=reference.device,
            generator=generator,
        )
    )


def serializable_step(step: Any) -> dict[str, Any]:
    return {
        "baseline_score": step.baseline_score,
        "resulting_score": step.resulting_score,
        "requested_drop": step.requested_drop,
        "achieved_drop": step.achieved_drop,
        "step_norm": step.step_norm,
        "relative_step_norm": step.relative_step_norm,
        "capped": step.capped,
    }


def build_cell_plan(
    *,
    model: Any,
    tokenizer: Any,
    raw_streams: torch.Tensor,
    layer: int,
    position: int,
    lens_matrix: torch.Tensor,
    target_value: Any,
    counterfactual_value: Any,
    row_cache: dict[int, torch.Tensor],
    score_drops: list[float],
    max_relative_norm: float,
    intervention_mode: str,
    direction_name: str,
    stage: str,
) -> dict[str, Any]:
    target_ids = single_token_ids(tokenizer, target_value)
    counterfactual_ids = single_token_ids(tokenizer, counterfactual_value)
    target_id, _ = choose_j_lens_variant(
        model=model,
        raw_streams=raw_streams,
        token_ids=target_ids,
        row_cache=row_cache,
        lens_matrix=lens_matrix,
    )
    counterfactual_id, _ = choose_j_lens_variant(
        model=model,
        raw_streams=raw_streams,
        token_ids=counterfactual_ids,
        row_cache=row_cache,
        lens_matrix=lens_matrix,
    )
    target_row = row_cache[target_id]
    counterfactual_row = row_cache[counterfactual_id]
    j_score, j_gradient = score_and_gradient(
        model=model,
        raw_streams=raw_streams,
        unembedding_row=target_row,
        lens_matrix=lens_matrix,
    )
    ll_score, ll_gradient = score_and_gradient(
        model=model,
        raw_streams=raw_streams,
        unembedding_row=target_row,
        lens_matrix=None,
    )
    counterfactual_score, counterfactual_gradient = score_and_gradient(
        model=model,
        raw_streams=raw_streams,
        unembedding_row=counterfactual_row,
        lens_matrix=lens_matrix,
    )
    unique_gradient = orthogonal_component(j_gradient, ll_gradient)
    random_direction = random_direction_like(
        j_gradient,
        seed=stable_seed(direction_name, stage, layer, position, "random"),
    )

    def j_score_fn(value: torch.Tensor) -> torch.Tensor:
        return decoded_score(
            model=model,
            raw_streams=value,
            unembedding_row=target_row,
            lens_matrix=lens_matrix,
        )

    interventions: dict[str, Any] = {}
    for requested_drop in score_drops:
        if intervention_mode == "suppress":
            step = find_suppression_step(
                j_score_fn,
                raw_streams,
                j_gradient,
                requested_drop=requested_drop,
                max_relative_norm=max_relative_norm,
            )
            suppress = True
        elif intervention_mode == "counterfactual_amplify":
            step = find_amplification_step(
                j_score_fn,
                raw_streams,
                j_gradient,
                requested_increase=requested_drop,
                max_relative_norm=max_relative_norm,
            )
            suppress = False
        else:
            raise ValueError(f"unknown intervention mode {intervention_mode!r}")
        norm = step.step_norm
        deltas = {
            "j_lens_target": step.delta,
            "logit_lens_target": matched_delta(
                ll_gradient, norm, suppress=suppress
            ),
            "j_lens_unique": matched_delta(
                unique_gradient, norm, suppress=suppress
            ),
            "j_lens_counterfactual": matched_delta(
                counterfactual_gradient, norm, suppress=suppress
            ),
            "random_matched": random_direction * norm,
        }
        offline_scores = {}
        with torch.no_grad():
            for condition, delta in deltas.items():
                altered = raw_streams.float() + delta
                offline_scores[condition] = {
                    "target_j_lens_score": float(j_score_fn(altered)),
                    "target_logit_lens_score": float(
                        decoded_score(
                            model=model,
                            raw_streams=altered,
                            unembedding_row=target_row,
                            lens_matrix=None,
                        )
                    ),
                    "counterfactual_j_lens_score": float(
                        decoded_score(
                            model=model,
                            raw_streams=altered,
                            unembedding_row=counterfactual_row,
                            lens_matrix=lens_matrix,
                        )
                    ),
                }
        interventions[str(requested_drop)] = {
            "step": serializable_step(step),
            "deltas": deltas,
            "offline_scores": offline_scores,
        }

    unique_fraction = float(unique_gradient.norm() / j_gradient.norm())
    return {
        "layer": layer,
        "position": position,
        "raw_streams": raw_streams,
        "target_value": str(target_value),
        "counterfactual_value": str(counterfactual_value),
        "target_token_id": target_id,
        "target_token": tokenizer.decode([target_id]),
        "counterfactual_token_id": counterfactual_id,
        "counterfactual_token": tokenizer.decode([counterfactual_id]),
        "baseline_scores": {
            "target_j_lens": j_score,
            "target_logit_lens": ll_score,
            "counterfactual_j_lens": counterfactual_score,
        },
        "gradient_geometry": {
            "j_lens_norm": float(j_gradient.norm()),
            "logit_lens_norm": float(ll_gradient.norm()),
            "j_vs_logit_cosine": cosine(j_gradient, ll_gradient),
            "j_unique_norm_fraction": unique_fraction,
            "j_unique_vs_logit_cosine": cosine(unique_gradient, ll_gradient),
        },
        "score_drops": interventions,
    }


@contextmanager
def patch_direction_deltas(
    model: Any,
    *,
    plans: list[dict[str, Any]],
    condition: str,
    score_drop: float,
    filler_indices: list[int],
) -> Iterator[dict[tuple[int, int], torch.Tensor]]:
    by_layer: dict[int, list[dict[str, Any]]] = {}
    for plan in plans:
        by_layer.setdefault(int(plan["layer"]), []).append(plan)
    observed: dict[tuple[int, int], torch.Tensor] = {}
    handles = []

    def make_hook(layer: int):
        def hook(_module: Any, _inputs: Any, output: Any) -> Any:
            tensor = output_tensor(output)
            patched = tensor.clone()
            for plan in by_layer[layer]:
                ordinal = int(plan["position"])
                absolute = filler_indices[ordinal - 1]
                delta = plan["score_drops"][str(score_drop)]["deltas"][condition]
                value = patched[:, absolute].float() + delta[None]
                patched[:, absolute] = value.to(patched.dtype)
                observed[(layer, ordinal)] = patched[:, absolute].detach().clone()
            return replace_output_tensor(output, patched)

        return hook

    try:
        for layer in sorted(by_layer):
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield observed
    finally:
        for handle in handles:
            handle.remove()


def observed_scores(
    *,
    model: Any,
    plans: list[dict[str, Any]],
    observed: dict[tuple[int, int], torch.Tensor],
    row_cache: dict[int, torch.Tensor],
    lens_by_layer: dict[int, torch.Tensor],
) -> list[dict[str, Any]]:
    results = []
    with torch.no_grad():
        for plan in plans:
            key = (int(plan["layer"]), int(plan["position"]))
            raw = observed[key][0].float()
            target_row = row_cache[int(plan["target_token_id"])]
            counterfactual_row = row_cache[int(plan["counterfactual_token_id"])]
            results.append(
                {
                    "layer": key[0],
                    "position": key[1],
                    "target_token_id": int(plan["target_token_id"]),
                    "target_j_lens_score": float(
                        decoded_score(
                            model=model,
                            raw_streams=raw,
                            unembedding_row=target_row,
                            lens_matrix=lens_by_layer[key[0]],
                        )
                    ),
                    "target_logit_lens_score": float(
                        decoded_score(
                            model=model,
                            raw_streams=raw,
                            unembedding_row=target_row,
                            lens_matrix=None,
                        )
                    ),
                    "counterfactual_j_lens_score": float(
                        decoded_score(
                            model=model,
                            raw_streams=raw,
                            unembedding_row=counterfactual_row,
                            lens_matrix=lens_by_layer[key[0]],
                        )
                    ),
                }
            )
    return results


def strip_tensors(plan: dict[str, Any], score_drop: float) -> dict[str, Any]:
    record = {
        key: value
        for key, value in plan.items()
        if key not in {"raw_streams", "score_drops"}
    }
    dose = plan["score_drops"][str(score_drop)]
    record["step"] = dose["step"]
    record["offline_scores"] = dose["offline_scores"]
    return record


def summarize_change(
    *, logits: torch.Tensor, baseline: dict[str, Any], tokenizer: Any, answer: Any
) -> dict[str, Any]:
    summary = target_logit_summary(logits[0], tokenizer, answer)
    return {
        **summary,
        "rank_change": summary["best_rank"] - baseline["best_rank"],
        "log_probability_change": (
            summary["best_log_probability"] - baseline["best_log_probability"]
        ),
    }


def distributed_max(value: torch.Tensor) -> float:
    result = value.detach().float().reshape(1)
    if dist.is_initialized():
        dist.all_reduce(result, op=dist.ReduceOp.MAX)
    return float(result.cpu())


def main() -> None:
    args = parse_args()
    stages = [item.strip() for item in args.stages.split(",") if item.strip()]
    conditions = [item.strip() for item in args.conditions.split(",") if item.strip()]
    unknown = set(conditions) - set(CONDITIONS)
    if not stages or unknown or len(conditions) != len(set(conditions)):
        raise ValueError(f"invalid stages/conditions; unknown conditions={sorted(unknown)}")
    if not 0 < args.max_relative_norm <= 1:
        raise ValueError("--max-relative-norm must lie in (0,1]")

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
    if model_args.hc_mult != 4 or model_args.n_layers != 43:
        raise AssertionError("expected DeepSeek V4 Flash with four streams and 43 blocks")
    if rank == 0:
        print(f"loading decoder-direction model on {world_size} GPUs", flush=True)
    with torch.device("cuda"):
        model = Transformer(model_args)
    load_model(
        model,
        str(args.ckpt_path / f"model{rank}-mp{world_size}.safetensors"),
        strict=False,
    )
    model.requires_grad_(False)
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.ckpt_path)
    if len(tokenizer) != model_args.vocab_size:
        raise AssertionError("tokenizer/model vocabulary mismatch")
    torch.set_default_device("cuda")
    barrier()

    checkpoint = torch.load(args.lens_path, map_location="cpu", weights_only=True)
    required = {"J", "source_layers", "d_model", "provenance"}
    if not required.issubset(checkpoint):
        raise AssertionError(f"lens keys missing: {required - set(checkpoint)}")
    if list(map(int, checkpoint["source_layers"])) != list(range(42)):
        raise AssertionError("expected released J-Lens layers 0..41")
    if int(checkpoint["d_model"]) != 4096:
        raise AssertionError("unexpected J-Lens width")
    lens_cpu = {int(key): value.float() for key, value in checkpoint["J"].items()}
    if float((lens_cpu[41] - torch.eye(4096, device="cpu")).abs().max()) != 0:
        raise AssertionError("released layer-41 J-Lens anchor is not identity")

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    manifest = json.loads(args.patch_manifest.read_text(encoding="utf-8"))
    directions = list(manifest["directions"])
    if args.max_directions is not None:
        directions = directions[: args.max_directions]
    max_dose = max(args.cell_doses)
    if max_dose > int(manifest["cells_per_stage"]):
        raise ValueError("cell dose exceeds manifest selection size")
    examples = {example["id"]: example for example in experiment["examples"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "direction-interventions.json"
    output: dict[str, Any] | None = (
        {
            "schema_version": 2,
            "intervention_mode": args.intervention_mode,
            "method": (
                "minimum-norm first-order raw-mHC J-Lens decoder direction, "
                "with nonlinear line search and matched-L2 controls"
            ),
            "activation_convention": (
                "raw post-block [4,4096] -> model final hc_head -> optional J_l -> "
                "final RMSNorm -> selected unembedding row"
            ),
            "stages": stages,
            "cell_doses": args.cell_doses,
            "score_drops": args.score_drops,
            "max_relative_norm": args.max_relative_norm,
            "conditions": {
                "j_lens_target": "edit target token along its J-Lens gradient",
                "logit_lens_target": "edit the same token along its logit-lens gradient",
                "j_lens_unique": "J-Lens target gradient component orthogonal to logit lens",
                "j_lens_counterfactual": "edit the paired prompt's stage token via J-Lens",
                "random_matched": "random raw direction with identical per-cell L2 norm",
            },
            "directions": [],
        }
        if rank == 0
        else None
    )

    row_cache: dict[int, torch.Tensor] = {}
    for direction_number, direction in enumerate(directions, start=1):
        donor_id, target_id = direction["donor_id"], direction["target_id"]
        donor, target = examples[donor_id], examples[target_id]
        active = donor if args.intervention_mode == "suppress" else target
        paired = target if args.intervention_mode == "suppress" else donor
        rendered, alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=active,
        )
        target_rendered, target_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=paired,
        )
        differences = [
            index
            for index, (left, right) in enumerate(
                zip(alignment.input_ids, target_alignment.input_ids)
            )
            if left != right
        ]
        if args.require_identical_token_layout:
            if len(alignment.input_ids) != len(target_alignment.input_ids):
                raise AssertionError("counterfactual token lengths differ")
            if alignment.filler_token_indices != target_alignment.filler_token_indices:
                raise AssertionError("counterfactual filler indices differ")
            if len(differences) != 1:
                raise AssertionError(f"expected one token difference, got {differences}")

        selected_cells = {
            stage: direction["selections"]["j_lens"][stage][:max_dose]
            for stage in stages
        }
        layers = sorted(
            {
                int(cell["layer"])
                for stage in stages
                for cell in selected_cells[stage]
            }
        )
        lens_by_layer = {
            layer: lens_cpu[layer].to(device="cuda", dtype=torch.float32)
            for layer in layers
        }
        needed_token_ids = sorted(
            {
                token_id
                for stage in stages
                for value in (
                    direction["donor_expected"][stage],
                    target["expected_intermediates"][stage],
                )
                for token_id in single_token_ids(tokenizer, value)
            }
        )
        for token_id in needed_token_ids:
            if token_id not in row_cache:
                row_cache[token_id] = broadcast_unembedding_row(
                    model, token_id, rank=rank, world_size=world_size
                )

        if rank == 0:
            print(
                f"direction {direction_number}/{len(directions)}: {donor_id} -> {target_id}",
                flush=True,
            )
        with capture_raw_layers(
            model, layers, alignment.filler_token_indices
        ) as captured:
            baseline_logits = forward(model, alignment.input_ids)
        missing = set(layers) - set(captured)
        if missing:
            raise AssertionError(f"capture missed layers {sorted(missing)}")
        baseline_intervention_answer = (
            target_logit_summary(baseline_logits[0], tokenizer, donor["answer"])
            if rank == 0
            else None
        )
        baseline_active_answer = (
            target_logit_summary(baseline_logits[0], tokenizer, active["answer"])
            if rank == 0
            else None
        )
        if (
            rank == 0
            and args.intervention_mode == "suppress"
            and baseline_intervention_answer["best_rank"] != 1
        ):
            raise AssertionError(f"donor prompt is not baseline rank 1: {donor_id}")
        if rank == 0 and baseline_active_answer["best_rank"] != 1:
            raise AssertionError(f"active prompt is not baseline rank 1: {active['id']}")

        plans_by_stage: dict[str, list[dict[str, Any]]] = {}
        for stage in stages:
            plans = []
            for cell in selected_cells[stage]:
                position = int(cell["position"])
                layer = int(cell["layer"])
                raw = captured[layer][0, position - 1]
                plans.append(
                    build_cell_plan(
                        model=model,
                        tokenizer=tokenizer,
                        raw_streams=raw,
                        layer=layer,
                        position=position,
                        lens_matrix=lens_by_layer[layer],
                        target_value=direction["donor_expected"][stage],
                        counterfactual_value=target["expected_intermediates"][stage],
                        row_cache=row_cache,
                        score_drops=args.score_drops,
                        max_relative_norm=args.max_relative_norm,
                        intervention_mode=args.intervention_mode,
                        direction_name=f"{donor_id}->{target_id}",
                        stage=stage,
                    )
                )
            plans_by_stage[stage] = plans

        direction_output: dict[str, Any] | None = None
        if rank == 0:
            assert baseline_intervention_answer is not None
            assert baseline_active_answer is not None
            direction_output = {
                "donor_id": donor_id,
                "target_id": target_id,
                "donor_answer": donor["answer"],
                "target_answer": target["answer"],
                "active_id": active["id"],
                "donor_expected": direction["donor_expected"],
                "counterfactual_expected": target["expected_intermediates"],
                "rendered_prompt": rendered,
                "input_length": len(alignment.input_ids),
                "filler_indices": alignment.filler_token_indices,
                "input_token_differences": differences,
                "baseline": {
                    "answer": baseline_intervention_answer,
                    "intervention_answer": baseline_intervention_answer,
                    "active_answer": baseline_active_answer,
                    "top_tokens": full_logits_summary(
                        baseline_logits[0], tokenizer, 5
                    )["top_tokens"],
                },
                "runs": [],
            }

        # A zero-delta hook must be an exact identity under the raw mHC convention.
        identity_plan = plans_by_stage[stages[0]][0]
        identity_delta = identity_plan["score_drops"][str(args.score_drops[0])]["deltas"][
            "j_lens_target"
        ]
        identity_plan["score_drops"]["identity"] = {
            "deltas": {"identity": torch.zeros_like(identity_delta)}
        }
        with patch_direction_deltas(
            model,
            plans=[identity_plan],
            condition="identity",
            score_drop="identity",  # type: ignore[arg-type]
            filler_indices=alignment.filler_token_indices,
        ):
            identity_logits = forward(model, alignment.input_ids)
        identity_error = distributed_max((identity_logits - baseline_logits).abs().max())
        del identity_plan["score_drops"]["identity"]
        if identity_error != 0.0:
            raise AssertionError(f"zero-delta closure failed: {identity_error}")
        if rank == 0:
            assert direction_output is not None
            direction_output["identity_max_abs_logit_error"] = identity_error

        for stage in stages:
            for score_drop in args.score_drops:
                for dose in args.cell_doses:
                    plans = plans_by_stage[stage][:dose]
                    for condition in conditions:
                        started = time.monotonic()
                        with patch_direction_deltas(
                            model,
                            plans=plans,
                            condition=condition,
                            score_drop=score_drop,
                            filler_indices=alignment.filler_token_indices,
                        ) as observed:
                            logits = forward(model, alignment.input_ids)
                        cell_scores = observed_scores(
                            model=model,
                            plans=plans,
                            observed=observed,
                            row_cache=row_cache,
                            lens_by_layer=lens_by_layer,
                        )
                        if rank == 0:
                            assert direction_output is not None
                            assert baseline_intervention_answer is not None
                            assert baseline_active_answer is not None
                            intervention_answer = summarize_change(
                                logits=logits,
                                baseline=baseline_intervention_answer,
                                tokenizer=tokenizer,
                                answer=donor["answer"],
                            )
                            active_answer = summarize_change(
                                logits=logits,
                                baseline=baseline_active_answer,
                                tokenizer=tokenizer,
                                answer=active["answer"],
                            )
                            run = {
                                "stage": stage,
                                "score_drop": score_drop,
                                "cell_dose": dose,
                                "condition": condition,
                                "answer": intervention_answer,
                                "intervention_answer": intervention_answer,
                                "active_answer": active_answer,
                                "top_tokens": full_logits_summary(logits[0], tokenizer, 5)[
                                    "top_tokens"
                                ],
                                "cells": [strip_tensors(plan, score_drop) for plan in plans],
                                "observed_scores": cell_scores,
                                "elapsed_seconds": time.monotonic() - started,
                            }
                            direction_output["runs"].append(run)
                            median_local_drop = statistics.median(
                                plan["baseline_scores"]["target_j_lens"]
                                - score["target_j_lens_score"]
                                for plan, score in zip(plans, cell_scores)
                            )
                            print(
                                f"  {stage} drop={score_drop:g} cells={dose:2d} "
                                f"{condition}: donor-answer Δlogp="
                                f"{intervention_answer['log_probability_change']:+.3f} "
                                f"rank={intervention_answer['best_rank']} "
                                f"observed J change={-median_local_drop:+.2f}",
                                flush=True,
                            )

        if rank == 0:
            assert output is not None and direction_output is not None
            output["directions"].append(direction_output)
            write_json_atomic(output_path, output)
        del lens_by_layer, captured, plans_by_stage
        torch.cuda.empty_cache()

    if rank == 0:
        assert output is not None
        output["runtime"] = {
            "timestamp_unix": time.time(),
            "platform": platform.platform(),
            "torch": torch.__version__,
            "world_size": world_size,
            "model_revision": args.model_revision,
            "model_config_sha256": file_sha256(args.model_config),
            "model_code_sha256": file_sha256(args.reference_code_dir / "model.py"),
            "examples_config_sha256": file_sha256(args.examples_config),
            "patch_manifest_sha256": file_sha256(args.patch_manifest),
            "lens_sha256": file_sha256(args.lens_path),
            "lens_provenance": checkpoint["provenance"],
            "seed": 42,
        }
        write_json_atomic(output_path, output)
        print(f"wrote {output_path}", flush=True)
    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
