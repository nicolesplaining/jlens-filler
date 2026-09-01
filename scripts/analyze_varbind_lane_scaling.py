#!/usr/bin/env python3
"""Compare filler-lane coordinates across lengths and independent templates."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


STAGES = ["base_value", "bound_value", "second_product", "answer"]
ALIGNMENTS = ("absolute", "relative", "end_relative")


def keyed_path(value: str) -> tuple[int, Path]:
    key, separator, path = value.partition("=")
    if not separator:
        raise argparse.ArgumentTypeError("expected FILLER_LENGTH=PATH")
    return int(key), Path(path)


def best_variant(target: dict[str, Any]) -> dict[str, Any] | None:
    variants = [item for item in target["variants"] if "rank" in item]
    return min(variants, key=lambda item: int(item["rank"]), default=None)


def load_readouts(directory: Path) -> dict[str, dict[str, Any]]:
    output = {}
    for path in sorted(directory.glob("varbind_scale_*.json")):
        result = json.loads(path.read_text(encoding="utf-8"))
        output[result["example"]["id"]] = result
    if not output:
        raise ValueError(f"no scaled readout JSON files under {directory}")
    return output


def profile(
    result: dict[str, Any], method: str, stage: str, filler_count: int
) -> list[dict[str, Any]]:
    positions = {
        position: {
            "position": position,
            "rank1_layers": 0,
            "top10_layers": 0,
            "top10_strength": 0.0,
            "best_rank": 129280,
        }
        for position in range(1, filler_count + 1)
    }
    for layer_text, row in result["readouts"][method].items():
        layer = int(layer_text)
        if not 24 <= layer <= 38:
            continue
        for cell in row:
            if cell["position_kind"] != "filler":
                continue
            position = int(cell["filler_ordinal"])
            variant = best_variant(cell["targets"][stage])
            if variant is None:
                continue
            rank = int(variant["rank"])
            item = positions[position]
            item["best_rank"] = min(item["best_rank"], rank)
            item["rank1_layers"] += rank == 1
            item["top10_layers"] += rank <= 10
            if rank <= 10:
                item["top10_strength"] += (11 - rank) / 10
    return [positions[position] for position in sorted(positions)]


def top_positions(values: list[dict[str, Any]], fraction: float) -> set[int]:
    count = max(1, math.ceil(len(values) * fraction))
    ordered = sorted(
        values,
        key=lambda item: (
            -int(item["rank1_layers"]),
            -int(item["top10_layers"]),
            int(item["best_rank"]),
            int(item["position"]),
        ),
    )
    return {int(item["position"]) for item in ordered[:count]}


def map_position(position: int, short: int, long: int, alignment: str) -> int:
    if alignment == "absolute":
        return position
    if alignment == "end_relative":
        return long - (short - position)
    if alignment == "relative":
        if short == 1:
            return 1
        return 1 + round((position - 1) * (long - 1) / (short - 1))
    raise ValueError(alignment)


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


def correlation(left: list[float], right: list[float]) -> float | None:
    if len(left) < 3:
        return None
    left_ranks, right_ranks = rankdata(left), rankdata(right)
    left_mean, right_mean = statistics.fmean(left_ranks), statistics.fmean(right_ranks)
    numerator = sum(
        (x - left_mean) * (y - right_mean)
        for x, y in zip(left_ranks, right_ranks)
    )
    denominator = (
        sum((x - left_mean) ** 2 for x in left_ranks)
        * sum((y - right_mean) ** 2 for y in right_ranks)
    ) ** 0.5
    return numerator / denominator if denominator else None


def readout_comparisons(
    readouts: dict[int, dict[str, dict[str, Any]]], fraction: float
) -> list[dict[str, Any]]:
    records = []
    lengths = sorted(readouts)
    for short_index, short in enumerate(lengths):
        for long in lengths[short_index + 1 :]:
            common = sorted(set(readouts[short]) & set(readouts[long]))
            for example_id in common:
                for method in ("j_lens", "logit_lens"):
                    for stage in STAGES:
                        short_profile = profile(
                            readouts[short][example_id], method, stage, short
                        )
                        long_profile = profile(
                            readouts[long][example_id], method, stage, long
                        )
                        short_top = top_positions(short_profile, fraction)
                        long_top = top_positions(long_profile, fraction)
                        for alignment in ALIGNMENTS:
                            mapped = {
                                map_position(position, short, long, alignment)
                                for position in short_top
                            }
                            long_by_position = {
                                int(item["position"]): item for item in long_profile
                            }
                            profile_spearman = correlation(
                                [float(item["top10_strength"]) for item in short_profile],
                                [
                                    float(
                                        long_by_position[
                                            map_position(
                                                int(item["position"]),
                                                short,
                                                long,
                                                alignment,
                                            )
                                        ]["top10_strength"]
                                    )
                                    for item in short_profile
                                ],
                            )
                            records.append(
                                {
                                    "short_length": short,
                                    "long_length": long,
                                    "example_id": example_id,
                                    "method": method,
                                    "stage": stage,
                                    "alignment": alignment,
                                    "short_correct": bool(
                                        readouts[short][example_id]["model_output"]["correct"]
                                    ),
                                    "long_correct": bool(
                                        readouts[long][example_id]["model_output"]["correct"]
                                    ),
                                    "short_top_positions": sorted(short_top),
                                    "mapped_positions": sorted(mapped),
                                    "long_top_positions": sorted(long_top),
                                    "hit_rate": len(mapped & long_top) / len(mapped),
                                    "profile_spearman": profile_spearman,
                                }
                            )
    return records


def causal_profiles(grids: dict[int, Path], fraction: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    profiles = {}
    serialized = []
    for length, path in sorted(grids.items()):
        data = json.loads(path.read_text(encoding="utf-8"))
        by_position: dict[int, list[float]] = defaultdict(list)
        for cell in data["cells"]:
            by_position[int(cell["position"])].append(
                float(cell["donor_log_probability_change"])
            )
        values = [
            {
                "position": position,
                "max_delta_logp": max(by_position[position]),
                "mean_delta_logp": statistics.fmean(by_position[position]),
            }
            for position in range(1, length + 1)
        ]
        profiles[length] = values
        serialized.append(
            {
                "filler_length": length,
                "donor_id": data["donor_id"],
                "target_id": data["target_id"],
                "positions": values,
            }
        )

    comparisons = []
    lengths = sorted(profiles)
    for short_index, short in enumerate(lengths):
        for long in lengths[short_index + 1 :]:
            short_count = max(1, math.ceil(short * fraction))
            long_count = max(1, math.ceil(long * fraction))
            short_top = {
                item["position"]
                for item in sorted(
                    profiles[short], key=lambda item: -item["max_delta_logp"]
                )[:short_count]
            }
            long_top = {
                item["position"]
                for item in sorted(
                    profiles[long], key=lambda item: -item["max_delta_logp"]
                )[:long_count]
            }
            for alignment in ALIGNMENTS:
                mapped = {
                    map_position(position, short, long, alignment)
                    for position in short_top
                }
                comparisons.append(
                    {
                        "short_length": short,
                        "long_length": long,
                        "alignment": alignment,
                        "mapped_positions": sorted(mapped),
                        "long_top_positions": sorted(long_top),
                        "hit_rate": len(mapped & long_top) / len(mapped),
                    }
                )
    return serialized, comparisons


def aggregate(records: list[dict[str, Any]], keys: list[str]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[float]] = defaultdict(list)
    for record in records:
        groups[tuple(record[key] for key in keys)].append(float(record["hit_rate"]))
    return [
        {
            **dict(zip(keys, group)),
            "n": len(values),
            "mean_hit_rate": statistics.fmean(values),
            "median_hit_rate": statistics.median(values),
        }
        for group, values in sorted(groups.items())
    ]


def aggregate_spearman(
    records: list[dict[str, Any]], keys: list[str]
) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[float]] = defaultdict(list)
    for record in records:
        value = record.get("profile_spearman")
        if value is not None:
            groups[tuple(record[key] for key in keys)].append(float(value))
    return [
        {
            **dict(zip(keys, group)),
            "n": len(values),
            "mean_profile_spearman": statistics.fmean(values),
            "median_profile_spearman": statistics.median(values),
        }
        for group, values in sorted(groups.items())
    ]


def aggregate_position_profiles(
    readouts: dict[int, dict[str, dict[str, Any]]]
) -> list[dict[str, Any]]:
    output = []
    for filler_count, examples in sorted(readouts.items()):
        for method in ("j_lens", "logit_lens"):
            for stage in STAGES:
                by_position: dict[int, list[float]] = defaultdict(list)
                for result in examples.values():
                    if not result["model_output"]["correct"]:
                        continue
                    for row in profile(result, method, stage, filler_count):
                        by_position[int(row["position"])].append(
                            float(row["top10_strength"])
                        )
                positions = [
                    {
                        "position": position,
                        "n_examples": len(values),
                        "mean_top10_strength": statistics.fmean(values),
                        "median_top10_strength": statistics.median(values),
                    }
                    for position, values in sorted(by_position.items())
                ]
                if not positions:
                    continue
                ordered = sorted(
                    positions,
                    key=lambda item: (
                        -item["mean_top10_strength"],
                        item["position"],
                    ),
                )
                output.append(
                    {
                        "filler_length": filler_count,
                        "method": method,
                        "stage": stage,
                        "n_correct_examples": ordered[0]["n_examples"],
                        "best_position": ordered[0]["position"],
                        "best_mean_top10_strength": ordered[0][
                            "mean_top10_strength"
                        ],
                        "top_positions": ordered[:10],
                        "positions": positions,
                    }
                )
    return output


def write_report(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# Variable-binding filler-lane scaling",
        "",
        "These are J-Lens token readouts, not formal sparse J-space coordinates.",
        "Top-lane recurrence compares three coordinate hypotheses: fixed absolute dot "
        "ordinal, proportional location in the filler span, and fixed distance from the "
        "answer cue.",
        "",
        "## Readout recurrence",
        "",
        "| Readout | Stage | Coordinate | N comparisons | Mean top-lane hit rate | Median |",
        "|---|---|---|---:|---:|---:|",
    ]
    for row in summary["readout_aggregate"]:
        lines.append(
            f"| {row['method']} | {row['stage']} | {row['alignment']} | {row['n']} | "
            f"{row['mean_hit_rate']:.3f} | {row['median_hit_rate']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## Readout recurrence when the donor is correct at both lengths",
            "",
            "| Readout | Stage | Coordinate | N comparisons | Mean top-lane hit rate | Median |",
            "|---|---|---|---:|---:|---:|",
        ]
    )
    for row in summary["readout_aggregate_both_correct"]:
        lines.append(
            f"| {row['method']} | {row['stage']} | {row['alignment']} | {row['n']} | "
            f"{row['mean_hit_rate']:.3f} | {row['median_hit_rate']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## Full-profile recurrence when the donor is correct at both lengths",
            "",
            "Spearman correlations compare the complete per-position top-10 strength profile after applying each coordinate mapping.",
            "",
            "| Readout | Stage | Coordinate | N comparisons | Mean profile ρ | Median profile ρ |",
            "|---|---|---|---:|---:|---:|",
        ]
    )
    for row in summary["readout_profile_aggregate_both_correct"]:
        lines.append(
            f"| {row['method']} | {row['stage']} | {row['alignment']} | {row['n']} | "
            f"{row['mean_profile_spearman']:.3f} | "
            f"{row['median_profile_spearman']:.3f} |"
        )
    if summary["causal_aggregate"]:
        lines.extend(
            [
                "",
                "## Causal-lane recurrence",
                "",
                "| Coordinate | N length pairs | Mean top-lane hit rate | Median |",
                "|---|---:|---:|---:|",
            ]
        )
        for row in summary["causal_aggregate"]:
            lines.append(
                f"| {row['alignment']} | {row['n']} | "
                f"{row['mean_hit_rate']:.3f} | {row['median_hit_rate']:.3f} |"
            )
    k50_profiles = [
        row
        for row in summary["readout_position_aggregate"]
        if row["filler_length"] == 50
    ]
    if k50_profiles:
        lines.extend(
            [
                "",
                "## Stage-addressed readout peaks at k=50",
                "",
                "Profiles average top-10 target strength over correct exact-layout "
                "family members and layers 24–38. Strength is the rank-weighted "
                "number of top-10 layers at that dot (range 0–15).",
                "",
                "| Readout | Stage | Strongest dot | Mean strength | Next strongest dots |",
                "|---|---|---:|---:|---|",
            ]
        )
        for row in k50_profiles:
            next_positions = ", ".join(
                f"F{item['position']}"
                for item in row["top_positions"][1:5]
            )
            lines.append(
                f"| {row['method']} | {row['stage']} | "
                f"F{row['best_position']} | "
                f"{row['best_mean_top10_strength']:.3f} | {next_positions} |"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readout", action="append", type=keyed_path, required=True)
    parser.add_argument("--causal-grid", action="append", type=keyed_path, default=[])
    parser.add_argument("--top-fraction", type=float, default=0.20)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if not 0 < args.top_fraction <= 1:
        raise ValueError("top fraction must be in (0, 1]")
    readout_paths = dict(args.readout)
    if len(readout_paths) != len(args.readout):
        raise ValueError("readout filler lengths must be unique")
    readouts = {length: load_readouts(path) for length, path in readout_paths.items()}
    comparisons = readout_comparisons(readouts, args.top_fraction)
    causal_profiles_data, causal_comparisons = causal_profiles(
        dict(args.causal_grid), args.top_fraction
    ) if args.causal_grid else ([], [])
    summary = {
        "schema_version": 1,
        "top_fraction": args.top_fraction,
        "readout_lengths": sorted(readouts),
        "examples_by_length": {
            str(length): sorted(values) for length, values in readouts.items()
        },
        "readout_comparisons": comparisons,
        "readout_aggregate": aggregate(
            comparisons, ["method", "stage", "alignment"]
        ),
        "readout_aggregate_both_correct": aggregate(
            [
                record
                for record in comparisons
                if record["short_correct"] and record["long_correct"]
            ],
            ["method", "stage", "alignment"],
        ),
        "readout_profile_aggregate_both_correct": aggregate_spearman(
            [
                record
                for record in comparisons
                if record["short_correct"] and record["long_correct"]
            ],
            ["method", "stage", "alignment"],
        ),
        "readout_position_aggregate": aggregate_position_profiles(readouts),
        "causal_profiles": causal_profiles_data,
        "causal_comparisons": causal_comparisons,
        "causal_aggregate": aggregate(causal_comparisons, ["alignment"]),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "lane-scaling-summary.json"
    output.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_report(summary, args.output_dir / "lane-scaling-report.md")
    print(output)


if __name__ == "__main__":
    main()
