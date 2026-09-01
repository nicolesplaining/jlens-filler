#!/usr/bin/env python3
"""Combine varbind readouts, causal patches, and geometry into compact artifacts."""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


STAGES = [
    "base_value",
    "first_product",
    "bound_value",
    "second_product",
    "answer",
]
ORDERED_STAGES = ["base_value", "bound_value", "second_product", "answer"]
METHODS = ["j_lens", "logit_lens"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readout-dir", type=Path, required=True)
    parser.add_argument(
        "--causal-readout-dir",
        type=Path,
        help="optional readout directory for the causal donor",
    )
    parser.add_argument("--deep-dive-summary", type=Path, required=True)
    parser.add_argument("--patch-results", type=Path, required=True)
    parser.add_argument("--causal-grid", type=Path, required=True)
    parser.add_argument("--behavior-summary", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def mean(values: Iterable[float]) -> float | None:
    materialized = list(values)
    return sum(materialized) / len(materialized) if materialized else None


def median(values: Iterable[float]) -> float | None:
    materialized = list(values)
    return statistics.median(materialized) if materialized else None


def tied_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [0.0] * len(values)
    start = 0
    while start < len(order):
        stop = start + 1
        while stop < len(order) and values[order[stop]] == values[order[start]]:
            stop += 1
        value = (start + stop - 1) / 2 + 1
        for index in order[start:stop]:
            result[index] = value
        start = stop
    return result


def spearman(left: list[float], right: list[float]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    x = tied_ranks(left)
    y = tied_ranks(right)
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    numerator = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in zip(x, y)
    )
    denominator = math.sqrt(
        sum((value - x_mean) ** 2 for value in x)
        * sum((value - y_mean) ** 2 for value in y)
    )
    return numerator / denominator if denominator else None


def best_variant(target: dict[str, Any]) -> dict[str, Any]:
    variants = [
        variant
        for variant in target["variants"]
        if variant.get("single_token") and variant.get("rank") is not None
    ]
    if not variants:
        raise ValueError(f"no single-token target variant in {target}")
    return min(variants, key=lambda variant: int(variant["rank"]))


def cell_target(cell: dict[str, Any], stage: str) -> dict[str, Any]:
    variant = best_variant(cell["targets"][stage])
    return {
        "rank": int(variant["rank"]),
        "logit": float(variant["logit"]),
        "probability": float(variant["probability"]),
        "surface": variant["surface"],
    }


def load_readout_grid(path: Path) -> tuple[dict[str, Any], dict[str, dict[tuple[int, int], dict[str, Any]]]]:
    document = json.loads(path.read_text(encoding="utf-8"))
    methods: dict[str, dict[tuple[int, int], dict[str, Any]]] = {}
    for method in METHODS:
        grid: dict[tuple[int, int], dict[str, Any]] = {}
        for layer_text, cells in document["readouts"][method].items():
            layer = int(layer_text)
            for cell in cells:
                if cell["position_kind"] != "filler":
                    continue
                grid[(layer, int(cell["filler_ordinal"]))] = cell
        methods[method] = grid
    return document, methods


def analyze_geometry(
    readout_dir: Path, rescued_ids: list[str]
) -> tuple[dict[str, Any], dict[str, dict[str, dict[tuple[int, int], dict[str, Any]]]]]:
    loaded: dict[str, dict[str, dict[tuple[int, int], dict[str, Any]]]] = {}
    method_rows: dict[str, list[tuple[int, int, int]]] = {
        method: [] for method in METHODS
    }
    method_example_rhos: dict[str, dict[str, list[float]]] = {
        method: {"layer": [], "position": []} for method in METHODS
    }
    occupancy: dict[str, dict[str, dict[str, Counter[int]]]] = {
        method: {
            stage: {"layer": Counter(), "position": Counter()} for stage in STAGES
        }
        for method in METHODS
    }
    simultaneous: dict[str, list[int]] = {method: [] for method in METHODS}
    ordered_chains: dict[str, Counter[str]] = {
        method: Counter() for method in METHODS
    }
    rank1_sets: dict[str, dict[str, set[tuple[str, int, int]]]] = {
        method: {stage: set() for stage in STAGES} for method in METHODS
    }

    for example_id in rescued_ids:
        _document, grids = load_readout_grid(readout_dir / f"{example_id}.json")
        loaded[example_id] = grids
        for method, grid in grids.items():
            rows: list[tuple[int, int, int]] = []
            by_layer: dict[int, set[str]] = defaultdict(set)
            by_position: dict[int, dict[str, list[int]]] = defaultdict(
                lambda: defaultdict(list)
            )
            for (layer, position), cell in grid.items():
                for stage_index, stage in enumerate(ORDERED_STAGES):
                    if cell_target(cell, stage)["rank"] != 1:
                        continue
                    rows.append((stage_index, layer, position))
                    method_rows[method].append((stage_index, layer, position))
                    occupancy[method][stage]["layer"][layer] += 1
                    occupancy[method][stage]["position"][position] += 1
                    by_layer[layer].add(stage)
                    by_position[position][stage].append(layer)
                    rank1_sets[method][stage].add((example_id, layer, position))
            simultaneous[method].append(
                max((len(stages) for stages in by_layer.values()), default=0)
            )
            if rows:
                stage_indices = [row[0] for row in rows]
                layer_rho = spearman(stage_indices, [row[1] for row in rows])
                position_rho = spearman(stage_indices, [row[2] for row in rows])
                if layer_rho is not None:
                    method_example_rhos[method]["layer"].append(layer_rho)
                if position_rho is not None:
                    method_example_rhos[method]["position"].append(position_rho)
            for stages_by_name in by_position.values():
                present = [
                    stage for stage in ORDERED_STAGES if stage in stages_by_name
                ]
                if len(present) < 3:
                    continue
                ordered_chains[method]["eligible"] += 1
                first_layers = [min(stages_by_name[stage]) for stage in present]
                if all(
                    left <= right
                    for left, right in zip(first_layers, first_layers[1:])
                ):
                    ordered_chains[method]["ordered"] += 1

    result: dict[str, Any] = {"rescued_examples": rescued_ids, "methods": {}}
    rng = random.Random(42)
    for method in METHODS:
        rows = method_rows[method]
        stage_indices = [row[0] for row in rows]
        layers = [row[1] for row in rows]
        positions = [row[2] for row in rows]
        observed_layer_rho = spearman(stage_indices, layers)
        null_rhos: list[float] = []
        for _ in range(500):
            permuted = layers.copy()
            rng.shuffle(permuted)
            value = spearman(stage_indices, permuted)
            if value is not None:
                null_rhos.append(value)
        method_result: dict[str, Any] = {
            "all_rank1_cells": len(rows),
            "all_cell_stage_vs_layer_spearman": observed_layer_rho,
            "all_cell_stage_vs_position_spearman": spearman(
                stage_indices, positions
            ),
            "median_within_example_stage_vs_layer_spearman": median(
                method_example_rhos[method]["layer"]
            ),
            "median_within_example_stage_vs_position_spearman": median(
                method_example_rhos[method]["position"]
            ),
            "layer_permutation_null": {
                "permutations": len(null_rhos),
                "mean_rho": mean(null_rhos),
                "max_abs_rho": max((abs(value) for value in null_rhos), default=None),
                "two_sided_p": (
                    (1 + sum(abs(value) >= abs(observed_layer_rho) for value in null_rhos))
                    / (1 + len(null_rhos))
                    if observed_layer_rho is not None
                    else None
                ),
            },
            "examples_with_at_least_three_stages_at_one_layer": sum(
                value >= 3 for value in simultaneous[method]
            ),
            "max_simultaneous_stage_distribution": dict(
                sorted(Counter(simultaneous[method]).items())
            ),
            "same_position_three_plus_stage_chains": dict(
                ordered_chains[method]
            ),
            "occupancy": {},
        }
        for stage in ORDERED_STAGES:
            layer_counts = occupancy[method][stage]["layer"]
            position_counts = occupancy[method][stage]["position"]
            method_result["occupancy"][stage] = {
                "rank1_cells": sum(layer_counts.values()),
                "by_layer": [layer_counts.get(layer, 0) for layer in range(42)],
                "by_position": [
                    position_counts.get(position, 0) for position in range(1, 51)
                ],
                "peak_layer": (
                    max(layer_counts, key=layer_counts.get) if layer_counts else None
                ),
                "peak_layer_count": max(layer_counts.values(), default=0),
                "peak_position": (
                    max(position_counts, key=position_counts.get)
                    if position_counts
                    else None
                ),
                "peak_position_count": max(position_counts.values(), default=0),
            }
        result["methods"][method] = method_result

    overlap: dict[str, Any] = {}
    for stage in ORDERED_STAGES:
        left = rank1_sets["j_lens"][stage]
        right = rank1_sets["logit_lens"][stage]
        overlap[stage] = {
            "j_lens_cells": len(left),
            "logit_lens_cells": len(right),
            "intersection": len(left & right),
            "union": len(left | right),
            "jaccard": len(left & right) / len(left | right) if left | right else None,
        }
    result["j_lens_logit_lens_rank1_overlap"] = overlap
    return result, loaded


def analyze_pilot(patch_results: dict[str, Any]) -> dict[str, Any]:
    output: dict[str, Any] = {
        "identity_patch_max_abs_logit_error": max(
            direction["identity_patch_max_abs_logit_error"]
            for direction in patch_results["directions"]
        ),
        "directions": [],
    }
    for direction in patch_results["directions"]:
        baseline = direction["unpatched"]["target_prompt_donor_answer"]
        direction_result = {
            "donor_id": direction["donor_id"],
            "target_id": direction["target_id"],
            "baseline_donor_answer_rank": baseline["best_rank"],
            "baseline_donor_answer_log_probability": baseline[
                "best_log_probability"
            ],
            "results": [],
        }
        for patch in direction["patches"]:
            direction_result["results"].append(
                {
                    "stage": patch["stage"],
                    "strategy": patch["strategy"],
                    "dose": patch["dose"],
                    "donor_answer_rank": patch["donor_answer"]["best_rank"],
                    "donor_log_probability_change": patch[
                        "donor_log_probability_change"
                    ],
                    "target_answer_probability": patch["target_answer"][
                        "best_probability"
                    ],
                    "full_donor_answer_swap": patch["full_donor_answer_swap"],
                }
            )
        output["directions"].append(direction_result)
    return output


def analyze_causal_grid(
    causal: dict[str, Any],
    donor_grids: dict[str, dict[tuple[int, int], dict[str, Any]]],
) -> dict[str, Any]:
    if not causal["runtime"].get("complete"):
        raise ValueError("single-cell causal grid is incomplete")
    cells: list[dict[str, Any]] = []
    for causal_cell in causal["cells"]:
        key = (int(causal_cell["layer"]), int(causal_cell["position"]))
        record: dict[str, Any] = {
            "layer": key[0],
            "position": key[1],
            "donor_log_probability_change": float(
                causal_cell["donor_log_probability_change"]
            ),
            "donor_rank": int(causal_cell["donor_answer"]["best_rank"]),
            "target_log_probability_change": float(
                causal_cell["target_log_probability_change"]
            ),
            "target_probability": float(
                causal_cell["target_answer"]["best_probability"]
            ),
            "top_token": causal_cell["top_token"]["token"],
            "readouts": {},
        }
        for method in METHODS:
            source = donor_grids[method][key]
            record["readouts"][method] = {
                "_top1": {
                    key: source["top_tokens"][0][key]
                    for key in ("token", "token_id", "logit", "probability")
                },
                **{stage: cell_target(source, stage) for stage in STAGES},
            }
        cells.append(record)

    effects = [cell["donor_log_probability_change"] for cell in cells]
    summary: dict[str, Any] = {
        "donor_id": causal["donor_id"],
        "target_id": causal["target_id"],
        "donor_answer": causal["donor_answer"],
        "target_answer": causal["target_answer"],
        "input_token_differences": causal.get("input_token_differences", []),
        "identity_patch_max_abs_logit_error": causal[
            "identity_patch_max_abs_logit_error"
        ],
        "baseline_donor_answer_rank": causal["unpatched"][
            "target_prompt_donor_answer"
        ]["best_rank"],
        "baseline_target_answer_probability": causal["unpatched"][
            "target_prompt_target_answer"
        ]["best_probability"],
        "cell_count": len(cells),
        "effect_range": [min(effects), max(effects)],
        "effect_vs_layer_spearman": spearman(
            effects, [cell["layer"] for cell in cells]
        ),
        "effect_vs_position_spearman": spearman(
            effects, [cell["position"] for cell in cells]
        ),
        "cells_improving_donor_logp_by_1": sum(effect >= 1 for effect in effects),
        "cells_improving_donor_logp_by_3": sum(effect >= 3 for effect in effects),
        "top_causal_cells": [],
        "position_summary": [],
        "layer_summary": [],
        "methods": {},
        "cells": cells,
    }
    for position in sorted({cell["position"] for cell in cells}):
        selected = [cell for cell in cells if cell["position"] == position]
        best = max(selected, key=lambda cell: cell["donor_log_probability_change"])
        summary["position_summary"].append(
            {
                "position": position,
                "mean_effect": mean(
                    cell["donor_log_probability_change"] for cell in selected
                ),
                "max_effect": best["donor_log_probability_change"],
                "best_layer": best["layer"],
            }
        )
    for layer in sorted({cell["layer"] for cell in cells}):
        selected = [cell for cell in cells if cell["layer"] == layer]
        best = max(selected, key=lambda cell: cell["donor_log_probability_change"])
        summary["layer_summary"].append(
            {
                "layer": layer,
                "mean_effect": mean(
                    cell["donor_log_probability_change"] for cell in selected
                ),
                "max_effect": best["donor_log_probability_change"],
                "best_position": best["position"],
            }
        )
    for cell in sorted(
        cells, key=lambda value: value["donor_log_probability_change"], reverse=True
    )[:25]:
        compact = {
            key: cell[key]
            for key in (
                "layer",
                "position",
                "donor_log_probability_change",
                "donor_rank",
                "target_probability",
                "top_token",
            )
        }
        compact["best_readout_stage"] = {}
        for method in METHODS:
            compact["best_readout_stage"][method] = min(
                STAGES,
                key=lambda stage: cell["readouts"][method][stage]["rank"],
            )
            compact[f"{method}_ranks"] = {
                stage: cell["readouts"][method][stage]["rank"]
                for stage in STAGES
            }
        summary["top_causal_cells"].append(compact)

    top_k = min(25, len(cells))
    causal_top = set(
        (cell["layer"], cell["position"])
        for cell in sorted(
            cells,
            key=lambda value: value["donor_log_probability_change"],
            reverse=True,
        )[:top_k]
    )
    for method in METHODS:
        method_result: dict[str, Any] = {}
        for stage in STAGES:
            readout_ranks = [
                cell["readouts"][method][stage]["rank"] for cell in cells
            ]
            readout_probabilities = [
                cell["readouts"][method][stage]["probability"] for cell in cells
            ]
            lens_sorted = sorted(
                cells,
                key=lambda cell: (
                    cell["readouts"][method][stage]["rank"],
                    -cell["readouts"][method][stage]["probability"],
                ),
            )
            lens_top = set(
                (cell["layer"], cell["position"])
                for cell in lens_sorted[:top_k]
            )
            rank1 = [
                cell
                for cell in cells
                if cell["readouts"][method][stage]["rank"] == 1
            ]
            method_result[stage] = {
                "effect_vs_negative_rank_spearman": spearman(
                    effects, [-float(rank) for rank in readout_ranks]
                ),
                "effect_vs_log_probability_spearman": spearman(
                    effects,
                    [math.log10(max(probability, 1e-30)) for probability in readout_probabilities],
                ),
                "top25_lens_top25_causal_overlap": len(lens_top & causal_top),
                "mean_effect_top25_lens_cells": mean(
                    cell["donor_log_probability_change"]
                    for cell in lens_sorted[:top_k]
                ),
                "rank1_cell_count": len(rank1),
                "mean_effect_rank1_cells": mean(
                    cell["donor_log_probability_change"] for cell in rank1
                ),
                "max_effect_rank1_cells": max(
                    (
                        cell["donor_log_probability_change"]
                        for cell in rank1
                    ),
                    default=None,
                ),
            }
        summary["methods"][method] = method_result
    return summary


def format_number(value: Any, digits: int = 3) -> str:
    if value is None:
        return "—"
    if isinstance(value, int):
        return str(value)
    return f"{float(value):.{digits}f}"


def write_report(output: dict[str, Any], path: Path) -> None:
    geometry = output["geometry"]
    causal = output["causal_grid"]
    pilot = output["patching_pilot"]
    lines = [
        "# Variable-binding filler workspace: readout and causal deep dive",
        "",
        "All decoded values are **J-Lens token readouts**, not formal sparse J-space coordinates or a transcript of hidden reasoning.",
        "",
    ]
    if "behavior" in output:
        behavior = output["behavior"]["overall"]
        baseline = behavior["by_length"]["0"]
        filler = behavior["by_length"]["50"]
        paired = behavior["paired_vs_k0"]["50"]
        lines.extend(
            [
                "## Exact-layout counterfactual behavior",
                "",
                f"Changing only one numeric literal yields {baseline['correct']} / {baseline['n']} correct without filler and {filler['correct']} / {filler['n']} with 50 dots ({paired['helped_count']} helped, {paired['hurt_count']} hurt).",
                "",
            ]
        )
    lines.extend(
        [
            "## Geometry across all 14 examples rescued by 50 dots",
            "",
            "| Readout | Stage↔layer ρ | Stage↔dot ρ | ≥3 stages at one layer | Ordered same-dot chains |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for method in METHODS:
        item = geometry["methods"][method]
        chains = item["same_position_three_plus_stage_chains"]
        lines.append(
            f"| {method.replace('_', ' ').title()} | "
            f"{format_number(item['all_cell_stage_vs_layer_spearman'])} | "
            f"{format_number(item['all_cell_stage_vs_position_spearman'])} | "
            f"{item['examples_with_at_least_three_stages_at_one_layer']} / 14 | "
            f"{chains.get('ordered', 0)} / {chains.get('eligible', 0)} |"
        )
    lines.extend(
        [
            "",
            "The stage ordering is carried mainly by transformer depth, while dot ordinal has almost no monotonic relation to stage. Multiple stages nevertheless coexist at the same layer across different dots, which is the signature expected from a width-distributed workspace rather than a left-to-right textual scratchpad.",
            "",
            "## Causal patching pilot",
            "",
            f"Identity-patch closure error: `{pilot['identity_patch_max_abs_logit_error']}`.",
            "",
            "The table reports the donor answer after patching the largest 16-cell dose.",
            "",
            "| Direction | Stage | J-Lens rank / Δlog p | Logit-lens rank / Δlog p | Random rank / Δlog p | Complement rank / Δlog p |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for direction in pilot["directions"]:
        for stage in ("bound_value", "second_product", "answer"):
            selected = {
                item["strategy"]: item
                for item in direction["results"]
                if item["stage"] == stage and item["dose"] == 16
            }
            cells = []
            for strategy in (
                "j_lens",
                "logit_lens",
                "random_layer_matched",
                "complement_layer_matched",
            ):
                item = selected[strategy]
                cells.append(
                    f"{item['donor_answer_rank']} / {item['donor_log_probability_change']:+.2f}"
                )
            lines.append(
                f"| `{direction['donor_id']}` → `{direction['target_id']}` | "
                f"{stage.replace('_', ' ')} | " + " | ".join(cells) + " |"
            )

    lines.extend(
        [
            "",
            "## Single-cell causal map",
            "",
            f"Direction: `{causal['donor_id']}` → `{causal['target_id']}`. "
            f"The unpatched donor answer starts at rank {causal['baseline_donor_answer_rank']}. "
            f"Across {causal['cell_count']} one-cell interventions, "
            f"{causal['cells_improving_donor_logp_by_1']} improve its log probability by at least 1 nat and "
            f"{causal['cells_improving_donor_logp_by_3']} by at least 3 nats.",
            "",
            "| Readout | Stage | Effect↔readout-rank ρ | Top-25 overlap | Mean effect in top-25 readout cells |",
            "|---|---|---:|---:|---:|",
        ]
    )
    if causal["input_token_differences"]:
        differences = ", ".join(
            f"index {item['absolute_index']}: `{item['target_token']}` → `{item['donor_token']}`"
            for item in causal["input_token_differences"]
        )
        lines.insert(
            lines.index("| Readout | Stage | Effect↔readout-rank ρ | Top-25 overlap | Mean effect in top-25 readout cells |"),
            f"The aligned prompts differ only at {differences}.\n",
        )
    for method in METHODS:
        for stage in STAGES:
            item = causal["methods"][method][stage]
            lines.append(
                f"| {method.replace('_', ' ').title()} | {stage.replace('_', ' ')} | "
                f"{format_number(item['effect_vs_negative_rank_spearman'])} | "
                f"{item['top25_lens_top25_causal_overlap']} | "
                f"{format_number(item['mean_effect_top25_lens_cells'])} |"
            )
    strongest_positions = sorted(
        causal["position_summary"], key=lambda item: item["max_effect"], reverse=True
    )[:6]
    lines.extend(
        [
            "",
            "Strongest causal lanes by their best single-cell intervention: "
            + ", ".join(
                f"dot {item['position']} (L{item['best_layer']}, Δlog p {item['max_effect']:+.2f})"
                for item in strongest_positions
            )
            + ".",
        ]
    )
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "The causal map transfers a full residual vector from a matched donor; it does not isolate a single feature. A positive donor-answer effect shows that the location carries counterfactual answer-relevant information, but does not by itself prove that the displayed token direction is the sole mediator.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    deep_dive = json.loads(args.deep_dive_summary.read_text(encoding="utf-8"))
    rescued_ids = [
        example["id"]
        for example in deep_dive["examples"]
        if example["cohort"] == "rescued"
    ]
    geometry, loaded = analyze_geometry(args.readout_dir, rescued_ids)
    patch_results = json.loads(args.patch_results.read_text(encoding="utf-8"))
    causal = json.loads(args.causal_grid.read_text(encoding="utf-8"))
    donor_id = causal["donor_id"]
    causal_readout_dir = args.causal_readout_dir or args.readout_dir
    if donor_id not in loaded or causal_readout_dir != args.readout_dir:
        _document, loaded[donor_id] = load_readout_grid(
            causal_readout_dir / f"{donor_id}.json"
        )
    output = {
        "schema_version": 1,
        "geometry": geometry,
        "patching_pilot": analyze_pilot(patch_results),
        "causal_grid": analyze_causal_grid(causal, loaded[donor_id]),
    }
    if args.behavior_summary:
        output["behavior"] = json.loads(
            args.behavior_summary.read_text(encoding="utf-8")
        )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = args.output_dir / "varbind-causal-analysis.json"
    report_path = args.output_dir / "varbind-causal-report.md"
    summary_path.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_report(output, report_path)
    print(f"wrote {summary_path}")
    print(f"wrote {report_path}")


if __name__ == "__main__":
    main()
