#!/usr/bin/env python3
"""Quantify stage geometry across all k=50-rescued variable-binding cases."""

from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path
from typing import Any


TARGET_ORDER = [
    "base_value",
    "first_product",
    "bound_value",
    "second_product",
    "answer",
]
CHAIN_ORDER = ["base_value", "bound_value", "second_product", "answer"]
TARGET_LABELS = {
    "base_value": "visible base",
    "first_product": "first product",
    "bound_value": "hidden bound value",
    "second_product": "second product",
    "answer": "answer",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--patch-pair", default="varbind_easy_0033,varbind_easy_0002")
    parser.add_argument("--patch-cells", type=int, default=16)
    return parser.parse_args()


def best_variant(target: dict[str, Any]) -> dict[str, Any] | None:
    ranked = [variant for variant in target["variants"] if "rank" in variant]
    return min(ranked, key=lambda item: item["rank"], default=None)


def target_metrics(
    result: dict[str, Any], method: str, label: str
) -> dict[str, Any]:
    cells: list[dict[str, Any]] = []
    layer_counts: dict[int, dict[str, int]] = {}
    position_rank1 = {position: 0 for position in range(1, 51)}
    for layer_text, row in result["readouts"][method].items():
        layer = int(layer_text)
        layer_counts[layer] = {"top10": 0, "rank1": 0}
        for cell in row:
            if cell["position_kind"] != "filler":
                continue
            target = cell["targets"][label]
            variant = best_variant(target)
            if variant is None:
                continue
            record = {
                "layer": layer,
                "position": int(cell["filler_ordinal"]),
                "absolute_index": int(cell["absolute_index"]),
                "rank": int(target["best_rank"]),
                "logit": float(variant["logit"]),
                "probability": float(variant["probability"]),
            }
            cells.append(record)
            if record["rank"] <= 10:
                layer_counts[layer]["top10"] += 1
            if record["rank"] == 1:
                layer_counts[layer]["rank1"] += 1
                position_rank1[record["position"]] += 1
    if not cells:
        raise ValueError(f"no ranked filler cells for {label}")
    first_top10 = min(
        (cell for cell in cells if cell["rank"] <= 10),
        key=lambda cell: (cell["layer"], cell["position"]),
        default=None,
    )
    first_rank1 = min(
        (cell for cell in cells if cell["rank"] == 1),
        key=lambda cell: (cell["layer"], cell["position"]),
        default=None,
    )
    broadcast_onset = next(
        (
            layer
            for layer in sorted(layer_counts)
            if layer_counts[layer]["top10"] >= 2
        ),
        None,
    )
    best = min(cells, key=lambda cell: (cell["rank"], cell["layer"], cell["position"]))
    rank1 = [cell for cell in cells if cell["rank"] == 1]
    return {
        "best": best,
        "first_top10": first_top10,
        "first_rank1": first_rank1,
        "broadcast_onset": broadcast_onset,
        "rank1_cells": len(rank1),
        "top10_cells": sum(cell["rank"] <= 10 for cell in cells),
        "total_cells": len(cells),
        "rank1_positions": sorted({cell["position"] for cell in rank1}),
        "rank1_fraction_by_layer": [
            layer_counts[layer]["rank1"] / 50 for layer in sorted(layer_counts)
        ],
        "rank1_count_by_position": [position_rank1[position] for position in range(1, 51)],
        "cells": cells,
    }


def rankdata(values: list[float]) -> list[float]:
    ordered = sorted(range(len(values)), key=values.__getitem__)
    output = [0.0] * len(values)
    cursor = 0
    while cursor < len(values):
        end = cursor + 1
        while end < len(values) and values[ordered[end]] == values[ordered[cursor]]:
            end += 1
        average = (cursor + 1 + end) / 2
        for index in ordered[cursor:end]:
            output[index] = average
        cursor = end
    return output


def correlation(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 3:
        return None
    mean_x, mean_y = statistics.fmean(xs), statistics.fmean(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = (
        sum((x - mean_x) ** 2 for x in xs)
        * sum((y - mean_y) ** 2 for y in ys)
    ) ** 0.5
    return numerator / denominator if denominator else None


def spearman(stage_metrics: dict[str, Any], coordinate: str) -> float | None:
    pairs = []
    for index, label in enumerate(CHAIN_ORDER):
        first = stage_metrics[label]["first_rank1"]
        if first is not None:
            pairs.append((float(index), float(first[coordinate])))
    if len(pairs) < 3:
        return None
    return correlation(
        rankdata([pair[0] for pair in pairs]),
        rankdata([pair[1] for pair in pairs]),
    )


def compact_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in metrics.items() if key != "cells"}


def summarize_result(result: dict[str, Any]) -> dict[str, Any]:
    example = result["example"]
    output: dict[str, Any] = {
        "id": example["id"],
        "cohort": example.get("behavior_cohort", "unknown"),
        "expected": example["expected_intermediates"],
        "controls": example.get("tracked_controls", {}),
        "control_donor_id": example.get("control_donor_id"),
        "filler_answer": result["model_output"]["parsed_answer"],
        "filler_correct": result["model_output"]["correct"],
        "baseline_answer": result["no_filler_control"]["parsed_answer"],
        "baseline_correct": result["no_filler_control"]["correct"],
        "methods": {},
    }
    for method in ("j_lens", "logit_lens"):
        actual_full = {
            label: target_metrics(result, method, label) for label in TARGET_ORDER
        }
        control_full = {
            label: target_metrics(result, method, f"control_{label}")
            for label in TARGET_ORDER
        }
        output["methods"][method] = {
            "actual": {
                label: compact_metrics(metrics)
                for label, metrics in actual_full.items()
            },
            "control": {
                label: compact_metrics(metrics)
                for label, metrics in control_full.items()
            },
            "geometry": {
                "spearman_stage_vs_first_rank1_layer": spearman(actual_full, "layer"),
                "spearman_stage_vs_first_rank1_position": spearman(actual_full, "position"),
            },
        }
    return output


def median_or_none(values: list[int | float | None]) -> float | None:
    present = [float(value) for value in values if value is not None]
    return statistics.median(present) if present else None


def aggregate(examples: list[dict[str, Any]]) -> dict[str, Any]:
    rescued = [example for example in examples if example["cohort"] == "rescued"]
    output: dict[str, Any] = {"n_rescued": len(rescued), "methods": {}}
    for method in ("j_lens", "logit_lens"):
        method_output: dict[str, Any] = {"targets": {}}
        for label in TARGET_ORDER:
            actual = [example["methods"][method]["actual"][label] for example in rescued]
            control = [example["methods"][method]["control"][label] for example in rescued]
            actual_rank1 = sum(item["rank1_cells"] for item in actual)
            control_rank1 = sum(item["rank1_cells"] for item in control)
            actual_top10 = sum(item["top10_cells"] for item in actual)
            control_top10 = sum(item["top10_cells"] for item in control)
            total_actual = sum(item["total_cells"] for item in actual)
            total_control = sum(item["total_cells"] for item in control)
            method_output["targets"][label] = {
                "examples_with_rank1": sum(item["first_rank1"] is not None for item in actual),
                "control_examples_with_rank1": sum(
                    item["first_rank1"] is not None for item in control
                ),
                "median_first_rank1_layer": median_or_none(
                    [item["first_rank1"]["layer"] if item["first_rank1"] else None for item in actual]
                ),
                "median_first_rank1_position": median_or_none(
                    [item["first_rank1"]["position"] if item["first_rank1"] else None for item in actual]
                ),
                "median_broadcast_onset": median_or_none(
                    [item["broadcast_onset"] for item in actual]
                ),
                "actual_rank1_cells": actual_rank1,
                "control_rank1_cells": control_rank1,
                "actual_rank1_rate": actual_rank1 / total_actual,
                "control_rank1_rate": control_rank1 / total_control,
                "actual_top10_cells": actual_top10,
                "control_top10_cells": control_top10,
                "actual_top10_rate": actual_top10 / total_actual,
                "control_top10_rate": control_top10 / total_control,
                "mean_rank1_fraction_by_layer": [
                    statistics.fmean(
                        item["rank1_fraction_by_layer"][layer] for item in actual
                    )
                    for layer in range(42)
                ],
                "rank1_count_by_position": [
                    sum(item["rank1_count_by_position"][position] for item in actual)
                    for position in range(50)
                ],
            }
        layer_rhos = [
            example["methods"][method]["geometry"]["spearman_stage_vs_first_rank1_layer"]
            for example in rescued
        ]
        position_rhos = [
            example["methods"][method]["geometry"]["spearman_stage_vs_first_rank1_position"]
            for example in rescued
        ]
        method_output["geometry"] = {
            "examples_with_layer_spearman": sum(value is not None for value in layer_rhos),
            "median_stage_vs_layer_spearman": median_or_none(layer_rhos),
            "examples_with_position_spearman": sum(value is not None for value in position_rhos),
            "median_stage_vs_position_spearman": median_or_none(position_rhos),
        }
        output["methods"][method] = method_output
    return output


def select_patch_cells(
    result: dict[str, Any], method: str, label: str, count: int
) -> list[dict[str, Any]]:
    metrics = target_metrics(result, method, label)
    onset = metrics["broadcast_onset"]
    cells = metrics["cells"]
    window = (
        [cell for cell in cells if onset is not None and onset <= cell["layer"] <= onset + 2]
        if onset is not None
        else []
    )
    pool = window if len(window) >= count else cells
    ordered = sorted(
        pool,
        key=lambda cell: (
            cell["rank"],
            -cell["logit"],
            cell["layer"],
            cell["position"],
        ),
    )
    return ordered[:count]


def patch_manifest(
    results: list[dict[str, Any]], pair_spec: str, count: int
) -> dict[str, Any]:
    donor_id, target_id = [value.strip() for value in pair_spec.split(",", 1)]
    by_id = {result["example"]["id"]: result for result in results}
    missing = {donor_id, target_id} - set(by_id)
    if missing:
        raise ValueError(f"patch pair is absent from extraction: {sorted(missing)}")
    directions = []
    for donor, target in ((donor_id, target_id), (target_id, donor_id)):
        result = by_id[donor]
        selections: dict[str, dict[str, list[dict[str, Any]]]] = {
            "j_lens": {},
            "logit_lens": {},
            "random_layer_matched": {},
            "complement_layer_matched": {},
        }
        for label in ("bound_value", "second_product", "answer"):
            j_cells = select_patch_cells(result, "j_lens", label, count)
            ll_cells = select_patch_cells(result, "logit_lens", label, count)
            selections["j_lens"][label] = j_cells
            selections["logit_lens"][label] = ll_cells

            all_cells = target_metrics(result, "j_lens", label)["cells"]
            by_layer: dict[int, list[dict[str, Any]]] = {}
            for cell in all_cells:
                by_layer.setdefault(cell["layer"], []).append(cell)
            excluded = {
                (cell["layer"], cell["position"]) for cell in j_cells + ll_cells
            }
            rng = random.Random(f"{donor}:{target}:{label}:42")
            random_cells: list[dict[str, Any]] = []
            complement_cells: list[dict[str, Any]] = []
            used_random: set[tuple[int, int]] = set()
            used_complement: set[tuple[int, int]] = set()
            for selected in j_cells:
                layer = selected["layer"]
                candidates = [
                    cell
                    for cell in by_layer[layer]
                    if (layer, cell["position"]) not in excluded
                    and (layer, cell["position"]) not in used_random
                ]
                if not candidates:
                    raise ValueError(f"no random control cell at layer {layer}")
                random_cell = rng.choice(candidates)
                used_random.add((layer, random_cell["position"]))
                random_cells.append(random_cell)

                candidates = [
                    cell
                    for cell in by_layer[layer]
                    if (layer, cell["position"]) not in excluded
                    and (layer, cell["position"]) not in used_complement
                ]
                if not candidates:
                    raise ValueError(f"no complementary control cell at layer {layer}")
                complement_cell = max(
                    candidates,
                    key=lambda cell: (cell["rank"], -cell["logit"], cell["position"]),
                )
                used_complement.add((layer, complement_cell["position"]))
                complement_cells.append(complement_cell)
            selections["random_layer_matched"][label] = random_cells
            selections["complement_layer_matched"][label] = complement_cells
        directions.append(
            {
                "donor_id": donor,
                "target_id": target,
                "donor_expected": result["example"]["expected_intermediates"],
                "selections": selections,
            }
        )
    return {"cells_per_stage": count, "directions": directions}


def fmt(value: Any) -> str:
    return "—" if value is None else str(value)


def write_markdown(summary: dict[str, Any], path: Path) -> None:
    aggregate_data = summary["aggregate"]
    lines = [
        "# Variable-binding deep dive: all dot-rescued examples",
        "",
        "These are **J-Lens token readouts**, not formal sparse J-space coordinates.",
        "The primary cohort is all 14 examples that are wrong without filler and correct "
        "with 50 post-question dots. Every stage is compared with the same stage value "
        "borrowed from a collision-free donor example.",
        "",
        "## Stage timing and shuffled controls",
        "",
        "| Readout | Stage | Rank-1 examples | Median first rank-1 layer | Median first rank-1 dot | Actual/control rank-1 cells |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for method, method_label in (("j_lens", "J-Lens"), ("logit_lens", "Logit lens")):
        for target in TARGET_ORDER:
            row = aggregate_data["methods"][method]["targets"][target]
            lines.append(
                f"| {method_label} | {TARGET_LABELS[target]} | "
                f"{row['examples_with_rank1']} / {aggregate_data['n_rescued']} | "
                f"{fmt(row['median_first_rank1_layer'])} | "
                f"{fmt(row['median_first_rank1_position'])} | "
                f"{row['actual_rank1_cells']} / {row['control_rank1_cells']} |"
            )
    lines.extend(
        [
            "",
            "## Depth versus dot ordinal",
            "",
            "Spearman correlations use the first exact rank-1 readout for the visible base, "
            "hidden bound value, second product, and final answer within each example.",
            "",
            "| Readout | Examples measurable | Median stage↔layer ρ | Examples measurable | Median stage↔dot-position ρ |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for method, method_label in (("j_lens", "J-Lens"), ("logit_lens", "Logit lens")):
        row = aggregate_data["methods"][method]["geometry"]
        lines.append(
            f"| {method_label} | {row['examples_with_layer_spearman']} | "
            f"{fmt(row['median_stage_vs_layer_spearman'])} | "
            f"{row['examples_with_position_spearman']} | "
            f"{fmt(row['median_stage_vs_position_spearman'])} |"
        )
    lines.extend(
        [
            "",
            "## Causal follow-up",
            "",
            "The patch manifest uses the matched pair `varbind_easy_0033 ↔ "
            "varbind_easy_0002`. Both are rescued by 50 dots and share the same final "
            "operation `2 × bound − 14`, so transferring the bound value has a clear "
            "counterfactual prediction for the answer.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    paths = sorted(args.input_dir.glob("varbind_easy_*.json"))
    if not paths:
        raise SystemExit(f"no extraction files in {args.input_dir}")
    results = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    examples = [summarize_result(result) for result in results]
    summary = {
        "schema_version": 1,
        "examples": examples,
        "aggregate": aggregate(examples),
        "patch_manifest": patch_manifest(results, args.patch_pair, args.patch_cells),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "varbind-deep-dive-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (args.output_dir / "patch-manifest.json").write_text(
        json.dumps(summary["patch_manifest"], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(summary, args.output_dir / "varbind-deep-dive-report.md")
    print(args.output_dir / "varbind-deep-dive-report.md")


if __name__ == "__main__":
    main()
