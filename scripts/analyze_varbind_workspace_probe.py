#!/usr/bin/env python3
"""Summarize cross-position transplants and matched workspace lesions."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def rankdata(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(order):
        end = cursor + 1
        while end < len(order) and values[order[end]] == values[order[cursor]]:
            end += 1
        average = (cursor + 1 + end) / 2
        for index in order[cursor:end]:
            ranks[index] = average
        cursor = end
    return ranks


def spearman(left: list[float], right: list[float]) -> float | None:
    if len(left) != len(right) or len(left) < 3:
        return None
    left_ranks, right_ranks = rankdata(left), rankdata(right)
    left_mean = statistics.fmean(left_ranks)
    right_mean = statistics.fmean(right_ranks)
    numerator = sum(
        (x - left_mean) * (y - right_mean)
        for x, y in zip(left_ranks, right_ranks)
    )
    denominator = math.sqrt(
        sum((x - left_mean) ** 2 for x in left_ranks)
        * sum((y - right_mean) ** 2 for y in right_ranks)
    )
    return numerator / denominator if denominator else None


def direction_summary(direction: dict[str, Any]) -> dict[str, Any]:
    cross = []
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in direction["cross_position"]:
        grouped[(row["stage"], int(row["source_index"]))].append(row)
    for (stage, source_index), rows in sorted(grouped.items()):
        ordered = sorted(
            rows,
            key=lambda item: float(item["donor_answer"]["log_probability_change"]),
            reverse=True,
        )
        effects = [
            float(item["donor_answer"]["log_probability_change"]) for item in rows
        ]
        target_effects = [
            float(item["target_answer"]["log_probability_change"]) for item in rows
        ]
        source_position = int(rows[0]["source_position"])
        same = next(
            item for item in rows if int(item["destination_position"]) == source_position
        )
        best = ordered[0]
        positive = [effect for effect in effects if effect > 0]
        threshold = max(effects) * 0.5 if max(effects) > 0 else 0.0
        cross.append(
            {
                "stage": stage,
                "source_index": source_index,
                "source_layer": int(rows[0]["source_layer"]),
                "source_position": source_position,
                "same_position_effect": float(
                    same["donor_answer"]["log_probability_change"]
                ),
                "best_destination": int(best["destination_position"]),
                "best_effect": float(
                    best["donor_answer"]["log_probability_change"]
                ),
                "same_position_target_effect": float(
                    same["target_answer"]["log_probability_change"]
                ),
                "best_destination_target_effect": float(
                    best["target_answer"]["log_probability_change"]
                ),
                "median_effect": statistics.median(effects),
                "mean_positive_effect": (
                    statistics.fmean(positive) if positive else None
                ),
                "destinations_positive": len(positive),
                "destinations_at_least_half_max": sum(
                    effect >= threshold for effect in effects
                ),
                "destination_count": len(effects),
                "destinations_selective": sum(
                    donor_effect > 0 and target_effect < 0
                    for donor_effect, target_effect in zip(effects, target_effects)
                ),
                "donor_target_effect_spearman": spearman(effects, target_effects),
                "best_is_same_position": int(best["destination_position"])
                == source_position,
                "rows": rows,
            }
        )

    lesion_grouped: dict[tuple[str, int], dict[str, float]] = defaultdict(dict)
    for row in direction["mean_lesions"]:
        key = (row["stage"], int(row["dose"]))
        lesion_grouped[key][row["strategy"]] = float(
            row["donor_answer"]["log_probability_change"]
        )
    lesions = []
    for (stage, dose), strategies in sorted(lesion_grouped.items()):
        targeted = strategies.get("j_lens")
        random = strategies.get("random_layer_matched")
        lesions.append(
            {
                "stage": stage,
                "dose": dose,
                "targeted_logp_change": targeted,
                "random_logp_change": random,
                "targeted_minus_random": (
                    targeted - random
                    if targeted is not None and random is not None
                    else None
                ),
            }
        )
    return {
        "family": direction.get("family"),
        "donor_id": direction["donor_id"],
        "target_id": direction["target_id"],
        "identity_patch_max_abs_logit_error": direction[
            "identity_patch_max_abs_logit_error"
        ],
        "cross_position": cross,
        "mean_lesions": lesions,
    }


def aggregate(directions: list[dict[str, Any]]) -> dict[str, Any]:
    cross_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    destination_groups: dict[tuple[str, int], list[float]] = defaultdict(list)
    lesions: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for direction in directions:
        for row in direction["cross_position"]:
            cross_groups[row["stage"]].append(row)
            for raw in row["rows"]:
                destination_groups[
                    (row["stage"], int(raw["destination_position"]))
                ].append(float(raw["donor_answer"]["log_probability_change"]))
        for row in direction["mean_lesions"]:
            lesions[(row["stage"], int(row["dose"]))].append(row)

    cross_output = {}
    for stage, rows in sorted(cross_groups.items()):
        pairwise_profile_correlations = []
        for left_index, left in enumerate(rows):
            left_effects = {
                int(raw["destination_position"]): float(
                    raw["donor_answer"]["log_probability_change"]
                )
                for raw in left["rows"]
            }
            for right in rows[left_index + 1 :]:
                right_effects = {
                    int(raw["destination_position"]): float(
                        raw["donor_answer"]["log_probability_change"]
                    )
                    for raw in right["rows"]
                }
                common = sorted(set(left_effects) & set(right_effects))
                value = spearman(
                    [left_effects[position] for position in common],
                    [right_effects[position] for position in common],
                )
                if value is not None:
                    pairwise_profile_correlations.append(value)
        best_destination_counts: dict[int, int] = defaultdict(int)
        for row in rows:
            best_destination_counts[int(row["best_destination"])] += 1
        cross_output[stage] = {
            "n_sources": len(rows),
            "same_position_is_best_fraction": statistics.fmean(
                float(row["best_is_same_position"]) for row in rows
            ),
            "median_same_position_effect": statistics.median(
                row["same_position_effect"] for row in rows
            ),
            "median_best_effect": statistics.median(row["best_effect"] for row in rows),
            "median_best_destination_target_effect": statistics.median(
                row["best_destination_target_effect"] for row in rows
            ),
            "median_destination_effect": statistics.median(
                row["median_effect"] for row in rows
            ),
            "median_fraction_positive_destinations": statistics.median(
                row["destinations_positive"] / row["destination_count"] for row in rows
            ),
            "median_fraction_half_max_destinations": statistics.median(
                row["destinations_at_least_half_max"] / row["destination_count"]
                for row in rows
            ),
            "median_fraction_selective_destinations": statistics.median(
                row["destinations_selective"] / row["destination_count"]
                for row in rows
            ),
            "median_donor_target_effect_spearman": median(
                [
                    row["donor_target_effect_spearman"]
                    for row in rows
                    if row["donor_target_effect_spearman"] is not None
                ]
            ),
            "pairwise_destination_profile_spearman_n": len(
                pairwise_profile_correlations
            ),
            "mean_pairwise_destination_profile_spearman": (
                statistics.fmean(pairwise_profile_correlations)
                if pairwise_profile_correlations
                else None
            ),
            "median_pairwise_destination_profile_spearman": median(
                pairwise_profile_correlations
            ),
            "best_destination_counts": [
                {"destination_position": position, "count": count}
                for position, count in sorted(
                    best_destination_counts.items(),
                    key=lambda item: (-item[1], item[0]),
                )
            ],
        }

    destination_output = [
        {
            "stage": stage,
            "destination_position": position,
            "n": len(values),
            "mean_logp_change": statistics.fmean(values),
            "median_logp_change": statistics.median(values),
        }
        for (stage, position), values in sorted(destination_groups.items())
    ]
    top_destinations = {
        stage: sorted(
            [row for row in destination_output if row["stage"] == stage],
            key=lambda row: (-row["mean_logp_change"], row["destination_position"]),
        )[:10]
        for stage in sorted(cross_groups)
    }
    lesion_output = []
    for (stage, dose), rows in sorted(lesions.items()):
        targeted = [
            row["targeted_logp_change"]
            for row in rows
            if row["targeted_logp_change"] is not None
        ]
        random = [
            row["random_logp_change"]
            for row in rows
            if row["random_logp_change"] is not None
        ]
        differences = [
            row["targeted_minus_random"]
            for row in rows
            if row["targeted_minus_random"] is not None
        ]
        lesion_output.append(
            {
                "stage": stage,
                "dose": dose,
                "n": len(differences),
                "median_targeted_logp_change": median(targeted),
                "median_random_logp_change": median(random),
                "median_targeted_minus_random": median(differences),
                "targeted_more_damaging_fraction": (
                    statistics.fmean(float(value < 0) for value in differences)
                    if differences
                    else None
                ),
            }
        )
    return {
        "cross_position_by_stage": cross_output,
        "destination_effects": destination_output,
        "top_destinations_by_stage": top_destinations,
        "mean_lesions": lesion_output,
    }


def write_report(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# Filler workspace: slot interchangeability and necessity",
        "",
        "Residual interventions use the model's raw post-block mHC state. J-Lens is "
        "used to select cells; the patch does not isolate a token direction and is not "
        "a formal J-space-coordinate intervention.",
        "",
        "## Cross-position transplants",
        "",
        "| Stage | Sources | Same position is best | Median same-position Δlog p | Median best Δlog p | Median positive destinations | Median ≥ half-max destinations |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for stage, row in summary["aggregate"]["cross_position_by_stage"].items():
        lines.append(
            f"| {stage} | {row['n_sources']} | "
            f"{row['same_position_is_best_fraction']:.3f} | "
            f"{row['median_same_position_effect']:+.3f} | "
            f"{row['median_best_effect']:+.3f} | "
            f"{row['median_fraction_positive_destinations']:.3f} | "
            f"{row['median_fraction_half_max_destinations']:.3f} |"
        )
    lines.extend(
        [
            "",
            "Pairwise Spearman correlation tests whether the full destination-effect "
            "profile recurs across independent donor→target directions.",
            "",
            "| Stage | Profile pairs | Mean ρ | Median ρ | Most frequent best destinations |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for stage, row in summary["aggregate"]["cross_position_by_stage"].items():
        destinations = ", ".join(
            f"F{item['destination_position']} ({item['count']})"
            for item in row["best_destination_counts"][:5]
        )
        lines.append(
            f"| {stage} | {row['pairwise_destination_profile_spearman_n']} | "
            f"{row['mean_pairwise_destination_profile_spearman']:+.3f} | "
            f"{row['median_pairwise_destination_profile_spearman']:+.3f} | "
            f"{destinations} |"
        )
    lines.extend(
        [
            "",
            "### Donor-versus-target selectivity",
            "",
            "A destination is selective when it raises the donor answer while lowering "
            "the target's original answer.",
            "",
            "| Stage | Median target Δlog p at donor-best destination | Median selective destinations | Median donor↔target effect ρ |",
            "|---|---:|---:|---:|",
        ]
    )
    for stage, row in summary["aggregate"]["cross_position_by_stage"].items():
        lines.append(
            f"| {stage} | {row['median_best_destination_target_effect']:+.3f} | "
            f"{row['median_fraction_selective_destinations']:.3f} | "
            f"{row['median_donor_target_effect_spearman']:+.3f} |"
        )
    lines.extend(
        [
            "",
            "### Highest mean-effect destination addresses",
            "",
            "| Stage | Destination | Mean Δlog p | Median Δlog p | N directions |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for stage, rows in summary["aggregate"]["top_destinations_by_stage"].items():
        for row in rows[:5]:
            lines.append(
                f"| {stage} | F{row['destination_position']} | "
                f"{row['mean_logp_change']:+.3f} | "
                f"{row['median_logp_change']:+.3f} | {row['n']} |"
            )
    lines.extend(
        [
            "",
            "## Mean-residual lesions",
            "",
            "Negative Δlog p means the correct donor answer became less likely.",
            "",
            "| Stage | Dose | N directions | J-selected median Δlog p | Random median Δlog p | Median targeted−random | Targeted more damaging |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in summary["aggregate"]["mean_lesions"]:
        lines.append(
            f"| {row['stage']} | {row['dose']} | {row['n']} | "
            f"{row['median_targeted_logp_change']:+.3f} | "
            f"{row['median_random_logp_change']:+.3f} | "
            f"{row['median_targeted_minus_random']:+.3f} | "
            f"{row['targeted_more_damaging_fraction']:.3f} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    raw = json.loads(args.results.read_text(encoding="utf-8"))
    directions = [direction_summary(direction) for direction in raw["directions"]]
    summary = {
        "schema_version": 1,
        "filler_count": raw["filler_count"],
        "stages": raw["stages"],
        "directions": directions,
        "aggregate": aggregate(directions),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "workspace-probe-summary.json"
    output.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_report(summary, args.output_dir / "workspace-probe-report.md")
    print(output)


if __name__ == "__main__":
    main()
