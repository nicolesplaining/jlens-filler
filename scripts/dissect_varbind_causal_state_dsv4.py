#!/usr/bin/env python3
"""Dissect the useful substructure of a causal DeepSeek-V4 filler state.

For each exact-layout donor/target direction and task stage, the strongest
J-Lens-selected donor cell is transplanted into target filler position 50. The
full donor-minus-target raw mHC difference is a positive control. We compare it
with interpolation doses, individual mHC streams, complementary coordinate
halves, expected-token decoder spans, their orthogonal remainders, and a
leave-one-family-out shared difference span.
"""

from __future__ import annotations

import argparse
import json
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
from intervene_varbind_jlens_directions_dsv4 import (  # noqa: E402
    broadcast_unembedding_row,
    decoded_score,
    render_example,
    score_and_gradient,
    single_token_ids,
)
from jlens_filler.direction_intervention import (  # noqa: E402
    orthonormal_basis,
    project_onto_basis,
    stable_seed,
    unit_direction,
)
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
    parser.add_argument("--lens-path", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--patch-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stages", default="second_product,answer")
    parser.add_argument("--destination-position", type=int, default=50)
    parser.add_argument(
        "--conditions",
        help="optional comma-separated subset of intervention conditions",
    )
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


def distributed_max(value: torch.Tensor) -> float:
    result = value.detach().float().reshape(1)
    if dist.is_initialized():
        dist.all_reduce(result, op=dist.ReduceOp.MAX)
    return float(result.cpu())


def choose_variant(
    *,
    model: Any,
    raw_streams: torch.Tensor,
    token_ids: list[int],
    row_cache: dict[int, torch.Tensor],
    lens_matrix: torch.Tensor | None,
) -> tuple[int, float]:
    scores = []
    with torch.no_grad():
        for token_id in token_ids:
            scores.append(
                (
                    float(
                        decoded_score(
                            model=model,
                            raw_streams=raw_streams,
                            unembedding_row=row_cache[token_id],
                            lens_matrix=lens_matrix,
                        )
                    ),
                    token_id,
                )
            )
    score, token_id = max(scores)
    return token_id, score


def matched_random_delta(
    reference: torch.Tensor, *, norm: float, seed_parts: tuple[object, ...]
) -> torch.Tensor:
    generator = torch.Generator(device=reference.device)
    generator.manual_seed(stable_seed(*seed_parts))
    random = torch.randn(
        reference.shape,
        generator=generator,
        dtype=torch.float32,
        device=reference.device,
    )
    return unit_direction(random) * float(norm)


def random_basis(
    reference: torch.Tensor, *, rank: int, seed_parts: tuple[object, ...]
) -> torch.Tensor:
    generator = torch.Generator(device=reference.device)
    generator.manual_seed(stable_seed(*seed_parts))
    vectors = [
        torch.randn(
            reference.shape,
            generator=generator,
            dtype=torch.float32,
            device=reference.device,
        )
        for _ in range(rank)
    ]
    return orthonormal_basis(vectors)


@contextmanager
def patch_one_delta(
    model: Any,
    *,
    layer: int,
    absolute_position: int,
    delta: torch.Tensor,
) -> Iterator[dict[str, torch.Tensor]]:
    observed: dict[str, torch.Tensor] = {}

    def hook(_module: Any, _inputs: Any, output: Any) -> Any:
        tensor = output_tensor(output)
        patched = tensor.clone()
        value = patched[:, absolute_position].float() + delta[None]
        patched[:, absolute_position] = value.to(patched.dtype)
        observed["raw"] = patched[:, absolute_position].detach().clone()
        return replace_output_tensor(output, patched)

    handle = model.layers[layer].register_forward_hook(hook)
    try:
        yield observed
    finally:
        handle.remove()


def summarize_change(
    *, logits: torch.Tensor, baseline: dict[str, Any], tokenizer: Any, answer: Any
) -> dict[str, Any]:
    result = target_logit_summary(logits[0], tokenizer, answer)
    return {
        **result,
        "rank_improvement": int(baseline["best_rank"]) - int(result["best_rank"]),
        "logit_change": float(result["best_logit"]) - float(baseline["best_logit"]),
        "log_probability_change": float(result["best_log_probability"])
        - float(baseline["best_log_probability"]),
    }


def span_plan(
    *,
    model: Any,
    tokenizer: Any,
    target_raw: torch.Tensor,
    lens_matrix: torch.Tensor,
    values: list[Any],
    row_cache: dict[int, torch.Tensor],
) -> dict[str, Any]:
    j_gradients = []
    ll_gradients = []
    records = []
    for value in values:
        ids = single_token_ids(tokenizer, value)
        j_id, j_score = choose_variant(
            model=model,
            raw_streams=target_raw,
            token_ids=ids,
            row_cache=row_cache,
            lens_matrix=lens_matrix,
        )
        ll_id, ll_score = choose_variant(
            model=model,
            raw_streams=target_raw,
            token_ids=ids,
            row_cache=row_cache,
            lens_matrix=None,
        )
        _, j_gradient = score_and_gradient(
            model=model,
            raw_streams=target_raw,
            unembedding_row=row_cache[j_id],
            lens_matrix=lens_matrix,
        )
        _, ll_gradient = score_and_gradient(
            model=model,
            raw_streams=target_raw,
            unembedding_row=row_cache[ll_id],
            lens_matrix=None,
        )
        j_gradients.append(j_gradient)
        ll_gradients.append(ll_gradient)
        records.append(
            {
                "value": str(value),
                "j_token_id": j_id,
                "j_token": tokenizer.decode([j_id]),
                "j_score": j_score,
                "logit_token_id": ll_id,
                "logit_token": tokenizer.decode([ll_id]),
                "logit_score": ll_score,
            }
        )
    j_basis = orthonormal_basis(j_gradients)
    ll_basis = orthonormal_basis(ll_gradients)
    combined_basis = orthonormal_basis([*j_gradients, *ll_gradients])
    return {
        "j_basis": j_basis,
        "ll_basis": ll_basis,
        "combined_basis": combined_basis,
        "records": records,
    }


def condition_deltas(case: dict[str, Any], all_cases: list[dict[str, Any]]) -> dict[str, torch.Tensor]:
    delta = case["full_delta"]
    j_projection = project_onto_basis(delta, case["j_basis"])
    ll_projection = project_onto_basis(delta, case["ll_basis"])
    combined_projection = project_onto_basis(delta, case["combined_basis"])

    other_family_deltas = [
        other["full_delta"] / other["full_delta"].norm()
        for other in all_cases
        if other["stage"] == case["stage"] and other["family"] != case["family"]
    ]
    shared_basis = orthonormal_basis(other_family_deltas)
    shared_projection = project_onto_basis(delta, shared_basis)

    generator = torch.Generator(device=delta.device)
    generator.manual_seed(
        stable_seed(case["donor_id"], case["target_id"], case["stage"], "coordinate-half")
    )
    half_mask = torch.rand(
        delta.shape, generator=generator, dtype=torch.float32, device=delta.device
    ) < 0.5
    half_a = delta * half_mask
    half_b = delta * (~half_mask)

    results = {
        "full_delta": delta,
        "scale_025": delta * 0.25,
        "scale_050": delta * 0.50,
        "scale_075": delta * 0.75,
        "j_expected_span": j_projection,
        "j_expected_orthogonal": delta - j_projection,
        "logit_expected_span": ll_projection,
        "logit_expected_orthogonal": delta - ll_projection,
        "combined_expected_span": combined_projection,
        "combined_expected_orthogonal": delta - combined_projection,
        "shared_loo_span": shared_projection,
        "shared_loo_orthogonal": delta - shared_projection,
        "coordinate_half_a": half_a,
        "coordinate_half_b": half_b,
    }
    for stream in range(4):
        stream_delta = torch.zeros_like(delta)
        stream_delta[stream] = delta[stream]
        results[f"stream_{stream}"] = stream_delta
    for name, streams in {
        "stream_2_3": (2, 3),
        "stream_except_0": (1, 2, 3),
        "stream_except_1": (0, 2, 3),
        "stream_except_2": (0, 1, 3),
        "stream_except_3": (0, 1, 2),
    }.items():
        stream_delta = torch.zeros_like(delta)
        for stream in streams:
            stream_delta[stream] = delta[stream]
        results[name] = stream_delta

    random_j = random_basis(
        delta,
        rank=case["j_basis"].shape[1],
        seed_parts=(case["donor_id"], case["target_id"], case["stage"], "random-j-span"),
    )
    results["random_j_rank_span"] = project_onto_basis(delta, random_j)
    results["random_j_norm_matched"] = matched_random_delta(
        delta,
        norm=float(j_projection.norm()),
        seed_parts=(case["donor_id"], case["target_id"], case["stage"], "random-j-norm"),
    )
    case["subspace_ranks"] = {
        "j_expected": int(case["j_basis"].shape[1]),
        "logit_expected": int(case["ll_basis"].shape[1]),
        "combined_expected": int(case["combined_basis"].shape[1]),
        "shared_loo": int(shared_basis.shape[1]),
    }
    return results


def main() -> None:
    args = parse_args()
    stages = [item.strip() for item in args.stages.split(",") if item.strip()]
    if not stages or not 1 <= args.destination_position <= 50:
        raise ValueError("invalid stages or destination position")

    rank, _local_rank, world_size = distributed_setup(args.process_group_timeout_minutes)
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
        print(f"loading state-dissection model on {world_size} GPUs", flush=True)
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
    if list(map(int, checkpoint["source_layers"])) != list(range(42)):
        raise AssertionError("expected released J-Lens layers 0..41")
    if int(checkpoint["d_model"]) != 4096:
        raise AssertionError("unexpected J-Lens width")
    lens_cpu = {int(key): value.float() for key, value in checkpoint["J"].items()}

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    manifest = json.loads(args.patch_manifest.read_text(encoding="utf-8"))
    directions = list(manifest["directions"])
    if args.max_directions is not None:
        directions = directions[: args.max_directions]
    examples = {example["id"]: example for example in experiment["examples"]}
    filler_count = int(experiment["filler_length"])
    if args.destination_position > filler_count:
        raise ValueError("destination exceeds filler count")

    needed_ids = sorted(
        {
            token_id
            for direction in directions
            for example_id in (direction["donor_id"], direction["target_id"])
            for value in examples[example_id]["expected_intermediates"].values()
            for token_id in single_token_ids(tokenizer, value)
        }
    )
    row_cache = {
        token_id: broadcast_unembedding_row(
            model, token_id, rank=rank, world_size=world_size
        )
        for token_id in needed_ids
    }

    cases: list[dict[str, Any]] = []
    baselines: dict[tuple[str, str], dict[str, Any]] = {}
    rendered_prompts: dict[str, str] = {}
    identity_errors = []
    for direction_number, direction in enumerate(directions, start=1):
        donor_id, target_id = direction["donor_id"], direction["target_id"]
        donor, target = examples[donor_id], examples[target_id]
        donor_rendered, donor_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=donor,
        )
        target_rendered, target_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=target,
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
                raise AssertionError(f"expected one token difference, got {differences}")
        selected = {stage: direction["selections"]["j_lens"][stage][0] for stage in stages}
        layers = sorted({int(cell["layer"]) for cell in selected.values()})
        if rank == 0:
            print(
                f"capture {direction_number}/{len(directions)}: {donor_id} -> {target_id}",
                flush=True,
            )
        with capture_raw_layers(model, layers, donor_alignment.filler_token_indices) as donor_raw:
            donor_logits = forward(model, donor_alignment.input_ids)
        with capture_raw_layers(model, layers, target_alignment.filler_token_indices) as target_raw:
            target_logits = forward(model, target_alignment.input_ids)

        donor_answer_baseline = (
            target_logit_summary(target_logits[0], tokenizer, donor["answer"])
            if rank == 0
            else None
        )
        target_answer_baseline = (
            target_logit_summary(target_logits[0], tokenizer, target["answer"])
            if rank == 0
            else None
        )
        donor_self = (
            target_logit_summary(donor_logits[0], tokenizer, donor["answer"])
            if rank == 0
            else None
        )
        if rank == 0:
            assert donor_answer_baseline and target_answer_baseline and donor_self
            if target_answer_baseline["best_rank"] != 1 or donor_self["best_rank"] != 1:
                raise AssertionError("both matched prompts must be rank-1 correct")
            baselines[(donor_id, target_id)] = {
                "target_prompt_donor_answer": donor_answer_baseline,
                "target_prompt_target_answer": target_answer_baseline,
                "donor_prompt_donor_answer": donor_self,
                "target_top_tokens": full_logits_summary(target_logits[0], tokenizer, 5)[
                    "top_tokens"
                ],
            }
            rendered_prompts[target_id] = target_rendered

        destination_absolute = target_alignment.filler_token_indices[
            args.destination_position - 1
        ]
        for stage in stages:
            cell = selected[stage]
            layer = int(cell["layer"])
            source_position = int(cell["position"])
            donor_state = donor_raw[layer][0, source_position - 1].float()
            target_state = target_raw[layer][0, args.destination_position - 1].float()
            full_delta = donor_state - target_state
            lens_matrix = lens_cpu[layer].to(device="cuda", dtype=torch.float32)
            values = []
            for example in (donor, target):
                for value in example["expected_intermediates"].values():
                    if str(value) not in {str(existing) for existing in values}:
                        values.append(value)
            span = span_plan(
                model=model,
                tokenizer=tokenizer,
                target_raw=target_state,
                lens_matrix=lens_matrix,
                values=values,
                row_cache=row_cache,
            )
            stage_ids = single_token_ids(tokenizer, direction["donor_expected"][stage])
            stage_token_id, stage_baseline_score = choose_variant(
                model=model,
                raw_streams=target_state,
                token_ids=stage_ids,
                row_cache=row_cache,
                lens_matrix=lens_matrix,
            )
            cases.append(
                {
                    "family": int(direction.get("family", direction_number // 2)),
                    "donor_id": donor_id,
                    "target_id": target_id,
                    "donor_answer": donor["answer"],
                    "target_answer": target["answer"],
                    "stage": stage,
                    "layer": layer,
                    "source_position": source_position,
                    "destination_position": args.destination_position,
                    "destination_absolute": destination_absolute,
                    "source_readout": cell,
                    "donor_state": donor_state,
                    "target_state": target_state,
                    "full_delta": full_delta,
                    "lens_matrix": lens_matrix,
                    "j_basis": span["j_basis"],
                    "ll_basis": span["ll_basis"],
                    "combined_basis": span["combined_basis"],
                    "span_tokens": span["records"],
                    "stage_token_id": stage_token_id,
                    "stage_token": tokenizer.decode([stage_token_id]),
                    "stage_baseline_j_score": stage_baseline_score,
                    "input_token_differences": differences,
                }
            )

        # A zero edit must preserve the target forward exactly.
        identity_case = cases[-1]
        with patch_one_delta(
            model,
            layer=identity_case["layer"],
            absolute_position=identity_case["destination_absolute"],
            delta=torch.zeros_like(identity_case["full_delta"]),
        ):
            identity_logits = forward(model, target_alignment.input_ids)
        identity_error = distributed_max((identity_logits - target_logits).abs().max())
        if identity_error != 0:
            raise AssertionError(f"zero-delta closure failed: {identity_error}")
        identity_errors.append(identity_error)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "state-dissection.json"
    output: dict[str, Any] | None = (
        {
            "schema_version": 1,
            "method": (
                "decomposition of a causal donor-source minus target-destination raw "
                "post-block mHC state difference"
            ),
            "activation_convention": "raw block output [4,4096] before downstream layers",
            "destination_position": args.destination_position,
            "stages": stages,
            "directions": [],
            "identity_max_abs_logit_error": max(identity_errors),
        }
        if rank == 0
        else None
    )

    for case_number, case in enumerate(cases, start=1):
        donor_id, target_id = case["donor_id"], case["target_id"]
        target = examples[target_id]
        _, target_alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=target,
        )
        deltas = condition_deltas(case, cases)
        if args.conditions:
            requested_conditions = [
                item.strip() for item in args.conditions.split(",") if item.strip()
            ]
            unknown = set(requested_conditions) - set(deltas)
            if unknown or len(requested_conditions) != len(set(requested_conditions)):
                raise ValueError(f"invalid intervention conditions: {sorted(unknown)}")
            deltas = {name: deltas[name] for name in requested_conditions}
        full_norm = float(case["full_delta"].norm())
        if rank == 0:
            print(
                f"dissect {case_number}/{len(cases)}: {donor_id}->{target_id} "
                f"{case['stage']} L{case['layer']} F{case['source_position']}->F{case['destination_position']}",
                flush=True,
            )
        runs = []
        for condition, delta in deltas.items():
            started = time.monotonic()
            with patch_one_delta(
                model,
                layer=case["layer"],
                absolute_position=case["destination_absolute"],
                delta=delta,
            ) as observed:
                logits = forward(model, target_alignment.input_ids)
            if "raw" not in observed:
                raise AssertionError("patch hook did not run")
            observed_raw = observed["raw"][0].float()
            observed_delta = observed_raw - case["target_state"]
            observed_norm = float(observed_delta.norm())
            stage_score = float(
                decoded_score(
                    model=model,
                    raw_streams=observed_raw,
                    unembedding_row=row_cache[case["stage_token_id"]],
                    lens_matrix=case["lens_matrix"],
                )
            )
            if rank == 0:
                baseline = baselines[(donor_id, target_id)]
                donor_answer = summarize_change(
                    logits=logits,
                    baseline=baseline["target_prompt_donor_answer"],
                    tokenizer=tokenizer,
                    answer=case["donor_answer"],
                )
                target_answer = summarize_change(
                    logits=logits,
                    baseline=baseline["target_prompt_target_answer"],
                    tokenizer=tokenizer,
                    answer=case["target_answer"],
                )
                runs.append(
                    {
                        "condition": condition,
                        "requested_delta_norm": float(delta.norm()),
                        "requested_norm_fraction": float(delta.norm()) / full_norm,
                        "observed_delta_norm": observed_norm,
                        "observed_norm_fraction": observed_norm / full_norm,
                        "stage_j_lens_score_change": stage_score
                        - float(case["stage_baseline_j_score"]),
                        "donor_answer": donor_answer,
                        "target_answer": target_answer,
                        "top_tokens": full_logits_summary(logits[0], tokenizer, 5)[
                            "top_tokens"
                        ],
                        "elapsed_seconds": time.monotonic() - started,
                    }
                )
                print(
                    f"  {condition}: donor Δlogp="
                    f"{donor_answer['log_probability_change']:+.3f} "
                    f"rank={donor_answer['best_rank']} norm={100*float(delta.norm())/full_norm:.1f}%",
                    flush=True,
                )

        if rank == 0:
            assert output is not None
            output["directions"].append(
                {
                    "family": case["family"],
                    "donor_id": donor_id,
                    "target_id": target_id,
                    "stage": case["stage"],
                    "layer": case["layer"],
                    "source_position": case["source_position"],
                    "destination_position": case["destination_position"],
                    "donor_answer": case["donor_answer"],
                    "target_answer": case["target_answer"],
                    "input_token_differences": case["input_token_differences"],
                    "source_readout": case["source_readout"],
                    "stage_token_id": case["stage_token_id"],
                    "stage_token": case["stage_token"],
                    "stage_baseline_j_score": case["stage_baseline_j_score"],
                    "full_delta_norm": full_norm,
                    "subspace_ranks": case["subspace_ranks"],
                    "span_tokens": case["span_tokens"],
                    "baseline": baselines[(donor_id, target_id)],
                    "target_rendered_prompt": rendered_prompts[target_id],
                    "runs": runs,
                }
            )
            write_json_atomic(output_path, output)

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
