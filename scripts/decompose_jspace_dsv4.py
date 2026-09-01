#!/usr/bin/env python3
"""Formal sparse nonnegative J-space decomposition for selected DSV4 filler cells.

This script uses an external, pinned implementation of gradient pursuit rather
than treating ranked J-Lens logits as J-space coordinates.  For layer ``l`` it
constructs the token-vector dictionary

    V_l = (W_U * gamma) @ J_l,

where ``gamma`` is DeepSeek's final RMSNorm weight.  The scalar RMS factor is
activation-dependent but common to every token logit, so folding ``gamma`` into
``W_U`` preserves the exact J-Lens ranking.  The target of the decomposition is
the 4096-wide activation obtained by applying DeepSeek's model-native final mHC
hyper-head to the raw post-block ``[4,4096]`` state, matching the existing
readout pipeline.

The output also includes the same sparse decomposition against ``W_U * gamma``
without Jacobian transport.  This is explicitly labelled a logit-space sparse
baseline, not formal J-space.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
import time
from collections import defaultdict
from pathlib import Path
from types import ModuleType
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
    capture_layers,
    collapse_streams,
    distributed_setup,
    file_sha256,
)
from jlens_filler.prompts import build_messages, render_and_align, token_variants  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--lens-path", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--sites-config", type=Path, required=True)
    parser.add_argument("--decomposition-module", type=Path, required=True)
    parser.add_argument("--decomposition-revision", required=True)
    parser.add_argument("--expected-decomposition-sha256")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--k", type=int, default=25)
    parser.add_argument(
        "--algorithm",
        choices=("gradient_pursuit", "nonnegative_orthogonal_matching_pursuit"),
        default="gradient_pursuit",
    )
    parser.add_argument("--top-k", type=int, default=25)
    parser.add_argument(
        "--rotation-control-seeds",
        default="101,202,303",
        help=(
            "Comma-separated seeds for Haar-orthogonal relative-orientation controls. "
            "Use an empty string to disable."
        ),
    )
    parser.add_argument("--max-seq-len", type=int, default=1280)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=30)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_decomposition_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("pinned_jlens_decomposition", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load decomposition module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not hasattr(module, "get_sparse_decomposition"):
        raise ImportError(f"{path} has no get_sparse_decomposition")
    return module


def validate_decomposer(module: ModuleType, algorithm: str) -> dict[str, Any]:
    """Synthetic support-recovery gate independent of the language model."""
    dictionary = torch.eye(8, dtype=torch.float32)
    target = torch.zeros(8, dtype=torch.float32)
    expected = {1: 0.75, 4: 1.25, 6: 0.50}
    for index, coefficient in expected.items():
        target[index] = coefficient
    result = module.get_sparse_decomposition(
        target, dictionary, k=5, algorithm=algorithm
    )
    support = result.support.tolist()
    recovered = {
        int(index): float(value)
        for index, value in zip(support, result.coordinates.cpu().tolist())
    }
    max_error = max(abs(recovered.get(index, 0.0) - value) for index, value in expected.items())
    unexpected = sorted(set(recovered) - set(expected))
    reconstruction_error = float((result.reconstruction.cpu() - target).abs().max())
    if max_error > 1e-5 or reconstruction_error > 1e-5 or unexpected:
        raise AssertionError(
            "sparse decomposition synthetic recovery failed: "
            f"recovered={recovered}, unexpected={unexpected}"
        )
    return {
        "expected_support": sorted(expected),
        "recovered_support": sorted(recovered),
        "max_coefficient_error": max_error,
        "max_reconstruction_error": reconstruction_error,
    }


def tracked_values(example: dict[str, Any]) -> dict[str, str]:
    values = dict(example.get("expected_intermediates", {}))
    values.update(example.get("tracked_controls", {}))
    return {str(label): str(value) for label, value in values.items()}


def single_token_targets(tokenizer: Any, values: dict[str, str]) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for label, value in values.items():
        variants = token_variants(tokenizer, value)
        singles = [variant for variant in variants if variant["single_token"]]
        if not singles:
            continue
        chosen = singles[0]
        output[label] = {
            "value": value,
            "token_id": int(chosen["token_ids"][0]),
            "token": tokenizer.decode([int(chosen["token_ids"][0])]),
            "variants": variants,
        }
    return output


def render_example(
    *,
    tokenizer: Any,
    encode_messages: Any,
    experiment: dict[str, Any],
    example: dict[str, Any],
    filler_length: int,
) -> tuple[str, Any]:
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
        raise AssertionError(
            f"k={filler_length}: expected {filler_length} filler tokens, "
            f"got {len(alignment.filler_token_indices)}"
        )
    return rendered, alignment


def top_token_records(logits: torch.Tensor, tokenizer: Any, top_k: int) -> list[dict[str, Any]]:
    values, ids = logits.topk(top_k)
    return [
        {
            "rank": rank,
            "token_id": int(token_id),
            "token": tokenizer.decode([int(token_id)]),
            "score": float(score),
        }
        for rank, (token_id, score) in enumerate(zip(ids.cpu(), values.cpu()), start=1)
    ]


def exact_rank(scores: torch.Tensor, token_id: int) -> int:
    score = scores[token_id]
    return int((scores > score).sum().item()) + 1


def decomposition_record(
    *,
    result: Any,
    target: torch.Tensor,
    dictionary: torch.Tensor,
    dictionary_norms: torch.Tensor,
    dictionary_scores: torch.Tensor,
    readout_scores: torch.Tensor,
    tokenizer: Any,
    targets: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    target = target.float()
    reconstruction = result.reconstruction.float()
    component = result.j_space_component.float()
    residual = target - reconstruction
    target_sq = float(target.square().sum())
    reconstruction_residual_sq = float(residual.square().sum())
    component_residual_sq = float((target - component).square().sum())
    target_norm = math.sqrt(target_sq)
    reconstruction_norm = float(reconstruction.norm())
    component_norm = float(component.norm())
    cosine = float(
        torch.dot(target, reconstruction)
        / (target.norm() * reconstruction.norm()).clamp_min(1e-30)
    )

    support = result.support.tolist()
    coordinates = result.coordinates.detach().float().cpu().tolist()
    atoms: list[dict[str, Any]] = []
    coordinate_by_token: dict[int, float] = {}
    for token_id, coefficient in zip(support, coordinates):
        atom = dictionary[int(token_id)]
        atom_norm = float(atom.norm())
        coordinate_by_token[int(token_id)] = float(coefficient)
        atoms.append(
            {
                "token_id": int(token_id),
                "token": tokenizer.decode([int(token_id)]),
                "coefficient": float(coefficient),
                "atom_norm": atom_norm,
                "contribution_norm": float(coefficient) * atom_norm,
                "readout_rank": exact_rank(readout_scores, int(token_id)),
                "readout_score": float(readout_scores[int(token_id)]),
            }
        )

    selected = set(result.selected_support.tolist())
    normalized_scores = dictionary_scores / dictionary_norms
    tracked: dict[str, Any] = {}
    for label, target_info in targets.items():
        token_id = int(target_info["token_id"])
        atom = dictionary[token_id]
        initial_normalized_score = normalized_scores[token_id]
        residual_correlation = torch.dot(atom, residual) / atom.norm().clamp_min(1e-30)
        tracked[label] = {
            **{key: value for key, value in target_info.items() if key != "variants"},
            "readout_rank": exact_rank(readout_scores, token_id),
            "readout_score": float(readout_scores[token_id]),
            "initial_atom_cosine": float(
                initial_normalized_score / target.norm().clamp_min(1e-30)
            ),
            "initial_normalized_correlation_rank": int(
                (normalized_scores > initial_normalized_score).sum().item()
            )
            + 1,
            "post_reconstruction_residual_normalized_correlation": float(
                residual_correlation
            ),
            "selected_atom": token_id in selected,
            "active_atom": token_id in coordinate_by_token,
            "coefficient": coordinate_by_token.get(token_id),
        }

    tracked_pairs: list[dict[str, Any]] = []
    for left, right in (
        ("bound_value", "distractor_bound"),
        ("second_product", "distractor_second_product"),
        ("answer", "distractor_answer"),
    ):
        if left not in targets or right not in targets:
            continue
        left_id = int(targets[left]["token_id"])
        right_id = int(targets[right]["token_id"])
        left_atom = dictionary[left_id]
        right_atom = dictionary[right_id]
        tracked_pairs.append(
            {
                "left": left,
                "left_token_id": left_id,
                "right": right,
                "right_token_id": right_id,
                "cosine": float(
                    torch.dot(left_atom, right_atom)
                    / (left_atom.norm() * right_atom.norm()).clamp_min(1e-30)
                ),
            }
        )

    return {
        "selected_count": int(result.selected_support.numel()),
        "active_count": int(result.support.numel()),
        "selected_support": [int(value) for value in result.selected_support.tolist()],
        "atoms": atoms,
        "tracked_targets": tracked,
        "tracked_atom_pair_cosines": tracked_pairs,
        "reconstruction": {
            "target_norm": target_norm,
            "reconstruction_norm": reconstruction_norm,
            "j_space_component_norm": component_norm,
            "residual_norm": math.sqrt(reconstruction_residual_sq),
            "reconstruction_fraction_squared_norm": (
                reconstruction_norm * reconstruction_norm / target_sq
            ),
            "reconstruction_fraction_variance_explained": (
                1.0 - reconstruction_residual_sq / target_sq
            ),
            "projection_fraction_variance_explained": (
                1.0 - component_residual_sq / target_sq
            ),
            "target_reconstruction_cosine": cosine,
        },
    }


def reconstruction_fve(result: Any, target: torch.Tensor) -> float:
    target = target.float()
    residual = target - result.reconstruction.float()
    return 1.0 - float(residual.square().sum() / target.square().sum())


def summarize_rotation_controls(
    observed_fve: float, values: list[float], seeds: list[int]
) -> dict[str, Any]:
    if not values:
        return {"seeds": [], "fraction_variance_explained": []}
    control = torch.tensor(values, dtype=torch.float64, device="cpu")
    mean = float(control.mean())
    return {
        "type": (
            "Haar-orthogonal relative-orientation control: rotate the target activation "
            "against the fixed token dictionary while preserving its norm and the "
            "dictionary's complete geometry"
        ),
        "seeds": seeds,
        "fraction_variance_explained": values,
        "mean_fraction_variance_explained": mean,
        "median_fraction_variance_explained": float(control.median()),
        "standard_deviation": float(control.std(unbiased=False)),
        "observed_minus_control_mean": observed_fve - mean,
    }


def main() -> None:
    args = parse_args()
    if args.k < 1 or args.top_k < 1:
        raise ValueError("k and top-k must be positive")
    module_hash = sha256(args.decomposition_module)
    if (
        args.expected_decomposition_sha256
        and module_hash != args.expected_decomposition_sha256
    ):
        raise AssertionError(
            f"decomposition source hash {module_hash} does not match expected "
            f"{args.expected_decomposition_sha256}"
        )
    decomposition_module = load_decomposition_module(args.decomposition_module)
    synthetic_gate = validate_decomposer(decomposition_module, args.algorithm)
    rotation_control_seeds = [
        int(value)
        for value in args.rotation_control_seeds.split(",")
        if value.strip()
    ]
    if len(rotation_control_seeds) != len(set(rotation_control_seeds)):
        raise ValueError("rotation-control-seeds must be unique")

    rank, _local_rank, world_size = distributed_setup(
        args.process_group_timeout_minutes
    )
    if world_size != 4:
        raise SystemExit(f"converted checkpoint requires world_size=4, got {world_size}")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_default_dtype(torch.bfloat16)
    torch.set_num_threads(8)
    torch.manual_seed(42)
    torch.set_float32_matmul_precision("highest")

    sys.path.insert(0, str(args.reference_code_dir.resolve()))
    sys.path.insert(0, str(args.reference_code_dir.resolve().parent / "encoding"))
    from encoding_dsv4 import encode_messages  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    model_args = ModelArgs(**json.loads(args.model_config.read_text(encoding="utf-8")))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if rank == 0:
        print(f"loading J-space model on {world_size} GPUs", flush=True)
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
    sites_config = json.loads(args.sites_config.read_text(encoding="utf-8"))
    examples = {example["id"]: example for example in experiment["examples"]}
    example_id = sites_config["example_id"]
    if example_id not in examples:
        raise KeyError(f"example {example_id} not found")
    example = examples[example_id]
    targets = single_token_targets(tokenizer, tracked_values(example))

    sites = sites_config["sites"]
    site_ids = [site["id"] for site in sites]
    if len(site_ids) != len(set(site_ids)):
        raise AssertionError("site ids must be unique")
    valid_layers = {int(site["layer"]) for site in sites}
    lens_checkpoint = None
    lens_j: dict[int, torch.Tensor] = {}
    if rank == 0:
        lens_checkpoint = torch.load(args.lens_path, map_location="cpu", weights_only=True)
        if set(valid_layers) - set(lens_checkpoint["J"]):
            raise AssertionError("one or more requested layers are absent from the lens")
        if int(lens_checkpoint["d_model"]) != model_args.dim:
            raise AssertionError("lens/model hidden dimensions differ")
        lens_j = {layer: lens_checkpoint["J"][layer] for layer in valid_layers}

    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for site in sites:
        grouped[int(site["filler_length"])].append(site)

    captured_sites: dict[str, torch.Tensor] = {}
    site_metadata: dict[str, dict[str, Any]] = {}
    prompt_records: dict[str, dict[str, Any]] = {}
    for filler_length, group in sorted(grouped.items()):
        rendered, alignment = render_example(
            tokenizer=tokenizer,
            encode_messages=encode_messages,
            experiment=experiment,
            example=example,
            filler_length=filler_length,
        )
        layers = sorted({int(site["layer"]) for site in group})
        absolute_positions = sorted(
            {
                alignment.filler_token_indices[int(site["filler_ordinal"]) - 1]
                for site in group
            }
        )
        position_to_offset = {
            absolute: offset for offset, absolute in enumerate(absolute_positions)
        }
        tokens = torch.tensor(
            [alignment.input_ids], dtype=torch.long, device="cuda"
        )
        if rank == 0:
            print(
                f"capturing k={filler_length}: layers={layers}, "
                f"positions={absolute_positions}",
                flush=True,
            )
        with capture_layers(model, layers, absolute_positions) as captured:
            actual_logits = model.forward(tokens, 0)
        top_id = int(actual_logits[0].argmax())
        expected_token_ids = {
            int(variant["token_ids"][0])
            for variant in token_variants(tokenizer, str(group[0]["expected_output"]))
            if variant["single_token"]
        }
        if top_id not in expected_token_ids:
            raise AssertionError(
                f"k={filler_length}: expected first output {group[0]['expected_output']}, "
                f"got token {top_id}={tokenizer.decode([top_id])!r}"
            )
        if rank == 0:
            prompt_records[str(filler_length)] = {
                "rendered_prompt": rendered,
                "input_token_count": len(alignment.input_ids),
                "filler_token_indices": alignment.filler_token_indices,
                "first_output_token_id": top_id,
                "first_output_token": tokenizer.decode([top_id]),
            }
        for site in group:
            layer = int(site["layer"])
            ordinal = int(site["filler_ordinal"])
            absolute = alignment.filler_token_indices[ordinal - 1]
            collapsed = collapse_streams(model, captured[layer])[0]
            activation = collapsed[position_to_offset[absolute]].detach().float()
            if rank == 0:
                captured_sites[site["id"]] = activation
                site_metadata[site["id"]] = {
                    **site,
                    "absolute_token_index": absolute,
                    "surface_token": tokenizer.decode([alignment.input_ids[absolute]]),
                    "input_token_count": len(alignment.input_ids),
                }
        del captured, actual_logits, tokens
        torch.cuda.empty_cache()

    # Gather the vocabulary-sharded unembedding. It is replicated only briefly
    # on nonzero ranks; rank zero retains the complete matrix for decomposition.
    local_unembedding = model.head.weight.detach().float().contiguous()
    gathered = [torch.empty_like(local_unembedding) for _ in range(world_size)]
    dist.all_gather(gathered, local_unembedding)
    if rank == 0:
        full_unembedding = torch.cat(gathered, dim=0)
        if tuple(full_unembedding.shape) != (model_args.vocab_size, model_args.dim):
            raise AssertionError(
                f"full unembedding shape {tuple(full_unembedding.shape)}"
            )
        norm_weight = model.norm.weight.detach().float()
        effective_unembedding = full_unembedding * norm_weight.unsqueeze(0)
    else:
        full_unembedding = None
        effective_unembedding = None
    del gathered, local_unembedding
    torch.cuda.empty_cache()
    barrier()

    output: dict[str, Any] | None = None
    if rank == 0:
        assert full_unembedding is not None and effective_unembedding is not None
        effective_unembedding_norms = effective_unembedding.norm(dim=1)
        orthogonal_controls: list[torch.Tensor] = []
        for seed in rotation_control_seeds:
            print(f"building Haar-orthogonal control seed {seed}", flush=True)
            generator = torch.Generator(device="cuda")
            generator.manual_seed(seed)
            random_matrix = torch.randn(
                model_args.dim,
                model_args.dim,
                dtype=torch.float32,
                device="cuda",
                generator=generator,
            )
            orthogonal, _triangular = torch.linalg.qr(random_matrix)
            orthogonal_controls.append(orthogonal)
            del random_matrix, _triangular
        output = {
            "schema_version": 1,
            "method": {
                "name": "formal sparse nonnegative J-space decomposition",
                "dictionary": "V_l = (W_U * final_rmsnorm_weight) @ J_l",
                "target_activation": (
                    "model.head.hc_head(raw post-block mHC [4,4096]) -> [4096]"
                ),
                "algorithm": args.algorithm,
                "k": args.k,
                "rotation_control_seeds": rotation_control_seeds,
                "external_implementation": {
                    "repository": "https://github.com/TransformerLensOrg/TransformerLens",
                    "revision": args.decomposition_revision,
                    "path": str(args.decomposition_module),
                    "sha256": module_hash,
                },
                "baseline": (
                    "same sparse nonnegative algorithm over W_U * final_rmsnorm_weight "
                    "without J transport; labelled logit_space_sparse"
                ),
            },
            "synthetic_validation": synthetic_gate,
            "model": {
                "id": "deepseek-ai/DeepSeek-V4-Flash",
                "revision": args.model_revision,
                "world_size": world_size,
                "vocab_size": model_args.vocab_size,
                "d_model": model_args.dim,
                "lens_provenance": lens_checkpoint.get("provenance", {}),
            },
            "inputs": {
                "examples_config": str(args.examples_config),
                "examples_config_sha256": file_sha256(args.examples_config),
                "sites_config": str(args.sites_config),
                "sites_config_sha256": file_sha256(args.sites_config),
                "lens_sha256": file_sha256(args.lens_path),
                "model_config_sha256": file_sha256(args.model_config),
            },
            "prompts": prompt_records,
            "sites": [],
            "runtime": {
                "timestamp_unix": int(time.time()),
                "platform": platform.platform(),
                "torch": torch.__version__,
                "cuda_device": torch.cuda.get_device_name(0),
            },
        }

        sites_by_layer: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for site in sites:
            sites_by_layer[int(site["layer"])].append(site)
        for layer, layer_sites in sorted(sites_by_layer.items()):
            started = time.monotonic()
            print(
                f"building layer {layer} J-space dictionary for "
                f"{len(layer_sites)} site(s)",
                flush=True,
            )
            j_matrix = lens_j[layer].to(device="cuda", dtype=torch.float32)
            dictionary = effective_unembedding @ j_matrix
            if tuple(dictionary.shape) != (model_args.vocab_size, model_args.dim):
                raise AssertionError(f"dictionary shape {tuple(dictionary.shape)}")
            atom_norms = dictionary.norm(dim=1)
            if not bool(torch.isfinite(atom_norms).all()) or bool((atom_norms == 0).any()):
                raise AssertionError("J-space dictionary contains invalid atoms")

            for site in layer_sites:
                site_id = site["id"]
                activation = captured_sites[site_id]
                transported = j_matrix @ activation
                rms_scale = torch.rsqrt(
                    transported.square().mean() + float(model_args.norm_eps)
                )
                dictionary_scores = dictionary @ activation
                exact_logits = full_unembedding @ (
                    transported * rms_scale * norm_weight
                )
                reconstructed_logits = dictionary_scores * rms_scale
                max_abs_logit_error = float(
                    (exact_logits - reconstructed_logits).abs().max()
                )
                logit_scale = max(float(exact_logits.abs().max()), 1e-12)
                relative_logit_error = max_abs_logit_error / logit_scale
                exact_top = exact_logits.topk(args.top_k).indices
                reconstructed_top = reconstructed_logits.topk(args.top_k).indices
                if not torch.equal(exact_top, reconstructed_top):
                    raise AssertionError(
                        f"{site_id}: folded dictionary does not preserve top-{args.top_k}"
                    )
                if relative_logit_error > 5e-5:
                    raise AssertionError(
                        f"{site_id}: dictionary/readout relative error "
                        f"{relative_logit_error:.3e}"
                    )

                j_result = decomposition_module.get_sparse_decomposition(
                    activation,
                    dictionary,
                    k=args.k,
                    algorithm=args.algorithm,
                )
                logit_scores = effective_unembedding @ activation
                ll_result = decomposition_module.get_sparse_decomposition(
                    activation,
                    effective_unembedding,
                    k=args.k,
                    algorithm=args.algorithm,
                )
                j_control_values: list[float] = []
                ll_control_values: list[float] = []
                for orthogonal in orthogonal_controls:
                    control_target = orthogonal.T @ activation
                    j_control = decomposition_module.get_sparse_decomposition(
                        control_target,
                        dictionary,
                        k=args.k,
                        algorithm=args.algorithm,
                    )
                    ll_control = decomposition_module.get_sparse_decomposition(
                        control_target,
                        effective_unembedding,
                        k=args.k,
                        algorithm=args.algorithm,
                    )
                    j_control_values.append(
                        reconstruction_fve(j_control, control_target)
                    )
                    ll_control_values.append(
                        reconstruction_fve(ll_control, control_target)
                    )
                j_record = decomposition_record(
                    result=j_result,
                    target=activation,
                    dictionary=dictionary,
                    dictionary_norms=atom_norms,
                    dictionary_scores=dictionary_scores,
                    readout_scores=exact_logits,
                    tokenizer=tokenizer,
                    targets=targets,
                )
                ll_record = decomposition_record(
                    result=ll_result,
                    target=activation,
                    dictionary=effective_unembedding,
                    dictionary_norms=effective_unembedding_norms,
                    dictionary_scores=logit_scores,
                    readout_scores=logit_scores,
                    tokenizer=tokenizer,
                    targets=targets,
                )
                j_record["rotation_control"] = summarize_rotation_controls(
                    j_record["reconstruction"][
                        "reconstruction_fraction_variance_explained"
                    ],
                    j_control_values,
                    rotation_control_seeds,
                )
                ll_record["rotation_control"] = summarize_rotation_controls(
                    ll_record["reconstruction"][
                        "reconstruction_fraction_variance_explained"
                    ],
                    ll_control_values,
                    rotation_control_seeds,
                )
                output["sites"].append(
                    {
                        **site_metadata[site_id],
                        "j_lens_readout": {
                            "top_tokens": top_token_records(
                                exact_logits, tokenizer, args.top_k
                            ),
                            "tracked_targets": {
                                label: {
                                    **{
                                        key: value
                                        for key, value in target.items()
                                        if key != "variants"
                                    },
                                    "rank": exact_rank(
                                        exact_logits, int(target["token_id"])
                                    ),
                                    "logit": float(
                                        exact_logits[int(target["token_id"])]
                                    ),
                                }
                                for label, target in targets.items()
                            },
                        },
                        "dictionary_validation": {
                            "rms_scale": float(rms_scale),
                            "max_absolute_logit_error": max_abs_logit_error,
                            "relative_to_max_absolute_logit": relative_logit_error,
                            "top_k_ids_exact_match": True,
                        },
                        "j_space": j_record,
                        "logit_space_sparse": ll_record,
                    }
                )
                print(
                    f"  {site_id}: J active={j_result.support.numel()} "
                    f"FVE={output['sites'][-1]['j_space']['reconstruction']['reconstruction_fraction_variance_explained']:.4f}",
                    flush=True,
                )
            del dictionary, atom_norms, j_matrix
            torch.cuda.empty_cache()
            print(
                f"layer {layer} complete in {time.monotonic() - started:.1f}s",
                flush=True,
            )

        output["sites"].sort(key=lambda item: sites_config["sites"].index(
            next(site for site in sites_config["sites"] if site["id"] == item["id"])
        ))
        args.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = args.output_dir / "jspace-decomposition.json"
        output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
        print(f"wrote {output_path}", flush=True)

    barrier()


if __name__ == "__main__":
    main()
