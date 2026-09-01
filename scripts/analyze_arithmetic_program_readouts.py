#!/usr/bin/env python3
"""Summarize stage timing in balanced-tree and serial arithmetic readouts."""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path, nargs="+")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--rank-threshold", type=int, default=10)
    parser.add_argument("--min-filler-cells", type=int, default=2)
    return parser.parse_args()


def median(values: list[int | float | None]) -> float | None:
    present = [float(value) for value in values if value is not None]
    return statistics.median(present) if present else None


def rankdata(values: list[float]) -> list[float]:
    ordered = sorted(range(len(values)), key=values.__getitem__)
    result = [0.0] * len(values)
    cursor = 0
    while cursor < len(values):
        end = cursor + 1
        while end < len(values) and values[ordered[end]] == values[ordered[cursor]]:
            end += 1
        average = (cursor + 1 + end) / 2
        for index in ordered[cursor:end]:
            result[index] = average
        cursor = end
    return result


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


def target_stats(
    method_layers: dict[str, list[dict[str, Any]]],
    label: str,
    rank_threshold: int,
    min_filler_cells: int,
) -> dict[str, Any]:
    rows: list[dict[str, int]] = []
    per_layer: list[dict[str, int]] = []
    for layer_text, cells in sorted(method_layers.items(), key=lambda item: int(item[0])):
        layer = int(layer_text)
        layer_rows = []
        for cell in cells:
            if cell["position_kind"] != "filler":
                continue
            rank = cell["targets"][label]["best_rank"]
            if rank is None:
                continue
            row = {
                "layer": layer,
                "filler_ordinal": int(cell["filler_ordinal"]),
                "rank": int(rank),
            }
            rows.append(row)
            layer_rows.append(row)
        per_layer.append(
            {
                "layer": layer,
                "at_threshold": sum(row["rank"] <= rank_threshold for row in layer_rows),
                "at_rank1": sum(row["rank"] == 1 for row in layer_rows),
            }
        )
    if not rows:
        return {
            "best_rank": None,
            "best_cell": None,
            "first_any_at_threshold": None,
            "broadcast_onset": None,
            "first_rank1": None,
            "threshold_cells": 0,
            "rank1_cells": 0,
            "peak_rank1_cells_in_layer": 0,
            "total_cells": 0,
        }
    best = min(rows, key=lambda row: (row["rank"], row["layer"], row["filler_ordinal"]))
    first_any = min(
        (row for row in rows if row["rank"] <= rank_threshold),
        key=lambda row: (row["layer"], row["filler_ordinal"]),
        default=None,
    )
    first_rank1 = min(
        (row for row in rows if row["rank"] == 1),
        key=lambda row: (row["layer"], row["filler_ordinal"]),
        default=None,
    )
    broadcast = next(
        (
            row["layer"]
            for row in per_layer
            if row["at_threshold"] >= min_filler_cells
        ),
        None,
    )
    return {
        "best_rank": best["rank"],
        "best_cell": {"layer": best["layer"], "filler_ordinal": best["filler_ordinal"]},
        "first_any_at_threshold": first_any,
        "broadcast_onset": broadcast,
        "first_rank1": first_rank1,
        "threshold_cells": sum(row["rank"] <= rank_threshold for row in rows),
        "rank1_cells": sum(row["rank"] == 1 for row in rows),
        "peak_rank1_cells_in_layer": max(row["at_rank1"] for row in per_layer),
        "total_cells": len(rows),
    }


def analyze_result(
    result: dict[str, Any], rank_threshold: int, min_filler_cells: int
) -> dict[str, Any]:
    example = result["example"]
    topology = example["topology"]
    expected = example["expected_intermediates"]
    controls = example.get("tracked_controls", {})
    output: dict[str, Any] = {
        "id": example["id"],
        "topology": topology,
        "answer": example["answer"],
        "filler_correct": result["model_output"]["correct"],
        "no_filler_correct": result["no_filler_control"]["correct"],
        "filler_length": result["condition"]["filler_length"],
        "targets": expected,
        "control_targets": controls,
        "methods": {},
    }
    for method in ("j_lens", "logit_lens"):
        stats = {
            label: target_stats(
                result["readouts"][method], label, rank_threshold, min_filler_cells
            )
            for label in list(expected) + list(controls)
        }
        actual_stats = {label: stats[label] for label in expected}
        control_stats = {label: stats[label] for label in controls}
        method_output: dict[str, Any] = {
            "targets": actual_stats,
            "controls": control_stats,
            "actual_vs_control_cells": {
                "actual_rank1": sum(item["rank1_cells"] for item in actual_stats.values()),
                "control_rank1": sum(item["rank1_cells"] for item in control_stats.values()),
                "actual_at_threshold": sum(
                    item["threshold_cells"] for item in actual_stats.values()
                ),
                "control_at_threshold": sum(
                    item["threshold_cells"] for item in control_stats.values()
                ),
                "actual_mean_rank1_fraction": statistics.fmean(
                    item["rank1_cells"] / item["total_cells"]
                    for item in actual_stats.values()
                    if item["total_cells"]
                ),
                "control_mean_rank1_fraction": (
                    statistics.fmean(
                        item["rank1_cells"] / item["total_cells"]
                        for item in control_stats.values()
                        if item["total_cells"]
                    )
                    if control_stats
                    else None
                ),
                "actual_mean_threshold_fraction": statistics.fmean(
                    item["threshold_cells"] / item["total_cells"]
                    for item in actual_stats.values()
                    if item["total_cells"]
                ),
                "control_mean_threshold_fraction": (
                    statistics.fmean(
                        item["threshold_cells"] / item["total_cells"]
                        for item in control_stats.values()
                        if item["total_cells"]
                    )
                    if control_stats
                    else None
                ),
            },
        }
        if topology == "balanced_tree":
            stage_labels = {
                "branches": ["p1", "p2", "p3", "p4"],
                "merges": ["m1", "m2"],
                "answer": ["y"],
            }
            stage_onsets = {
                stage: median([actual_stats[label]["broadcast_onset"] for label in labels])
                for stage, labels in stage_labels.items()
            }
            branch_onsets = [
                actual_stats[label]["broadcast_onset"] for label in stage_labels["branches"]
            ]
            present_branches = [value for value in branch_onsets if value is not None]
            method_output["algorithm_signature"] = {
                "stage_broadcast_onsets": stage_onsets,
                "branch_onset_spread": (
                    max(present_branches) - min(present_branches)
                    if len(present_branches) >= 2
                    else None
                ),
                "stages_depth_ordered": (
                    all(value is not None for value in stage_onsets.values())
                    and stage_onsets["branches"] <= stage_onsets["merges"] <= stage_onsets["answer"]
                ),
            }
        elif topology == "serial_chain":
            labels = ["x1", "x2", "x3", "x4", "x5", "x6", "y"]
            pairs = [
                (step, actual_stats[label]["broadcast_onset"])
                for step, label in enumerate(labels, start=1)
                if actual_stats[label]["broadcast_onset"] is not None
            ]
            method_output["algorithm_signature"] = {
                "step_broadcast_onsets": {
                    label: actual_stats[label]["broadcast_onset"] for label in labels
                },
                "detected_steps": len(pairs),
                "spearman_step_vs_onset": correlation(
                    rankdata([float(step) for step, _ in pairs]),
                    rankdata([float(onset) for _, onset in pairs]),
                ),
            }
        elif topology == "parallel_branches":
            branch_labels = ["branch_a_value", "branch_b_value"]
            branch_onsets = [
                actual_stats[label]["broadcast_onset"] for label in branch_labels
            ]
            present = [value for value in branch_onsets if value is not None]
            answer_onset = actual_stats["answer"]["broadcast_onset"]
            first_rank1_layers = {
                label: (
                    actual_stats[label]["first_rank1"]["layer"]
                    if actual_stats[label]["first_rank1"]
                    else None
                )
                for label in branch_labels + ["answer"]
            }
            method_output["algorithm_signature"] = {
                "branch_value_broadcast_onsets": dict(
                    zip(branch_labels, branch_onsets)
                ),
                "branch_value_first_rank1_layers": first_rank1_layers,
                "branch_value_onset_spread": (
                    max(present) - min(present) if len(present) == 2 else None
                ),
                "answer_broadcast_onset": answer_onset,
                "answer_lag_after_later_branch": (
                    answer_onset - max(present)
                    if answer_onset is not None and len(present) == 2
                    else None
                ),
                "branches_before_answer": (
                    answer_onset is not None
                    and len(present) == 2
                    and max(present) <= answer_onset
                ),
            }
        elif topology == "parallel_depth2":
            levels = {
                "level_1": ["branch_a_value_1", "branch_b_value_1"],
                "level_2": ["branch_a_value_2", "branch_b_value_2"],
                "answer": ["answer"],
            }
            onsets = {
                level: {
                    label: actual_stats[label]["broadcast_onset"] for label in labels
                }
                for level, labels in levels.items()
            }
            level_medians = {
                level: median(
                    [actual_stats[label]["broadcast_onset"] for label in labels]
                )
                for level, labels in levels.items()
            }
            level_spreads = {}
            for level in ("level_1", "level_2"):
                present = [value for value in onsets[level].values() if value is not None]
                level_spreads[level] = (
                    max(present) - min(present) if len(present) == 2 else None
                )
            method_output["algorithm_signature"] = {
                "broadcast_onsets": onsets,
                "stage_median_onsets": level_medians,
                "within_level_branch_spreads": level_spreads,
                "parallel_depth_ordered": (
                    all(value is not None for value in level_medians.values())
                    and level_medians["level_1"]
                    <= level_medians["level_2"]
                    <= level_medians["answer"]
                ),
            }
        else:
            raise ValueError(f"unsupported topology: {topology}")
        output["methods"][method] = method_output
    return output


def format_cell(item: dict[str, Any] | None) -> str:
    return "—" if item is None else f"L{item['layer']}/F{item['filler_ordinal']}"


def write_markdown(analysis: dict[str, Any], path: Path) -> None:
    threshold = analysis["settings"]["rank_threshold"]
    minimum = analysis["settings"]["min_filler_cells"]
    lines = [
        "# Arithmetic-program J-Lens algorithm probe",
        "",
        "These are **J-Lens token readouts**, not formal sparse J-space coordinates.",
        "",
        f"A broadcast onset is the first layer where a target reaches rank ≤{threshold} "
        f"at at least {minimum} filler positions. This is stricter than a single-cell hit.",
    ]
    for example in analysis["examples"]:
        lines.extend(
            [
                "",
                f"## `{example['id']}` ({example['topology']})",
                "",
                f"Filler answer correct: `{example['filler_correct']}`; no-filler correct: "
                f"`{example['no_filler_correct']}`; expected answer: `{example['answer']}`.",
            ]
        )
        for method, label in (("j_lens", "J-Lens"), ("logit_lens", "Logit lens")):
            details = example["methods"][method]
            lines.extend(
                [
                    "",
                    f"### {label}",
                    "",
                    "| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |",
                    "|---|---:|---:|---:|---:|---:|",
                ]
            )
            for target, value in example["targets"].items():
                stats = details["targets"][target]
                lines.append(
                    f"| `{target}` | {value} | {stats['best_rank']} | "
                    f"{format_cell(stats['best_cell'])} | "
                    f"{('L' + str(stats['broadcast_onset'])) if stats['broadcast_onset'] is not None else '—'} | "
                    f"{stats['rank1_cells']} |"
                )
            control = details["actual_vs_control_cells"]
            lines.append(
                f"\nActual/control cell counts: rank-1 `{control['actual_rank1']}` / "
                f"`{control['control_rank1']}`; rank ≤{threshold} "
                f"`{control['actual_at_threshold']}` / `{control['control_at_threshold']}`."
            )
            lines.append(
                f"Mean per-target cell fractions (actual/control): rank-1 "
                f"`{control['actual_mean_rank1_fraction']:.4f}` / "
                f"`{control['control_mean_rank1_fraction']:.4f}`; rank ≤{threshold} "
                f"`{control['actual_mean_threshold_fraction']:.4f}` / "
                f"`{control['control_mean_threshold_fraction']:.4f}`."
            )
            signature = details["algorithm_signature"]
            lines.append(f"\nAlgorithm signature: `{json.dumps(signature, sort_keys=True)}`")
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "Stage ordering is evidence about linearly transported token directions, not a "
            "literal trace of internal thoughts. Values copied from another example are tracked "
            "as controls; final claims should require actual targets to exceed those controls.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    paths = sorted(
        path
        for input_dir in args.input_dir
        for path in input_dir.glob("arithmetic_*.json")
    )
    if not paths:
        raise SystemExit(f"no arithmetic extraction JSON found in {args.input_dir}")
    examples = [
        analyze_result(
            json.loads(path.read_text(encoding="utf-8")),
            args.rank_threshold,
            args.min_filler_cells,
        )
        for path in paths
    ]
    analysis = {
        "settings": {
            "rank_threshold": args.rank_threshold,
            "min_filler_cells": args.min_filler_cells,
        },
        "examples": examples,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "algorithm-analysis.json").write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_markdown(analysis, args.output_dir / "algorithm-report.md")
    print(args.output_dir / "algorithm-report.md")


if __name__ == "__main__":
    main()
