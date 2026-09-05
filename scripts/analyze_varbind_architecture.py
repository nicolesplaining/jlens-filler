#!/usr/bin/env python3
"""Relate existing variable-binding readouts/causal maps to V4 layer types.

The analysis is deliberately descriptive: layer/position cells within one prompt
are not independent samples.  It asks whether the observed workspace behavior is
concentrated in DeepSeek-V4's CSA (4x compression) or HCA (128x compression)
layers and whether receiver gain follows the CSA four-token grouping.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--readout-dir",
        action="append",
        type=Path,
        default=[],
        help="Directory containing k=50 extraction JSON files; repeatable.",
    )
    parser.add_argument(
        "--causal-grid",
        action="append",
        type=Path,
        default=[],
        help="single-cell-grid.json path; repeatable.",
    )
    parser.add_argument("--workspace-probe", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def layer_type(layer: int) -> str:
    if layer < 2:
        return "SWA"
    return "CSA" if layer % 2 == 0 else "HCA"


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def load_readouts(directories: list[Path]) -> dict[str, dict[str, Any]]:
    outputs: dict[str, dict[str, Any]] = {}
    for directory in directories:
        for path_text in glob.glob(str(directory / "*.json")):
            path = Path(path_text)
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if "readouts" not in record:
                continue
            if int(record.get("condition", {}).get("filler_length", -1)) != 50:
                continue
            outputs[record["example"]["id"]] = record
    if not outputs:
        raise ValueError("no k=50 readout records found")
    return outputs


def filler_ranks(cells: list[dict[str, Any]], stage: str) -> list[int]:
    return [
        int(cell["targets"][stage]["best_rank"])
        for cell in cells
        if cell["position_kind"] == "filler"
        and cell["targets"][stage]["best_rank"] is not None
    ]


def summarize_readouts(records: dict[str, dict[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {"example_count": len(records), "lenses": {}}
    for lens in ("j_lens", "logit_lens"):
        threshold_counts: dict[str, Any] = {}
        for threshold in (1, 5, 10, 50):
            counts: dict[str, int] = defaultdict(int)
            events = 0
            for record in records.values():
                for stage in record["example"]["expected_intermediates"]:
                    for layer_text, cells in record["readouts"][lens].items():
                        layer = int(layer_text)
                        if min(filler_ranks(cells, stage)) <= threshold:
                            counts[layer_type(layer)] += 1
                            events += 1
                            break
            threshold_counts[str(threshold)] = {
                "events": events,
                "first_crossing_layer_types": dict(counts),
            }

        transition_values: dict[str, list[float]] = defaultdict(list)
        exact_top1: dict[str, int] = defaultdict(int)
        cell_totals: dict[str, int] = defaultdict(int)
        for record in records.values():
            stages = record["example"]["expected_intermediates"]
            for stage in stages:
                previous: int | None = None
                for layer_text, cells in record["readouts"][lens].items():
                    layer = int(layer_text)
                    ranks = filler_ranks(cells, stage)
                    best = min(ranks)
                    kind = layer_type(layer)
                    if previous is not None:
                        transition_values[kind].append(
                            math.log(previous) - math.log(best)
                        )
                    previous = best
                    exact_top1[kind] += sum(rank == 1 for rank in ranks)
                    cell_totals[kind] += len(ranks)
        output["lenses"][lens] = {
            "first_crossings": threshold_counts,
            "mean_log_rank_improvement_entering_layer_type": {
                kind: mean(values) for kind, values in transition_values.items()
            },
            "positive_transition_fraction": {
                kind: sum(value > 0 for value in values) / len(values)
                for kind, values in transition_values.items()
            },
            "exact_rank1_cells": {
                kind: {
                    "count": exact_top1[kind],
                    "total": cell_totals[kind],
                    "rate": exact_top1[kind] / cell_totals[kind],
                }
                for kind in cell_totals
            },
        }
    return output


def summarize_causal_grids(paths: list[Path]) -> list[dict[str, Any]]:
    outputs = []
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        by_type: dict[str, list[float]] = defaultdict(list)
        layer_means: dict[str, float] = {}
        for cell in record["cells"]:
            by_type[layer_type(int(cell["layer"]))].append(
                float(cell["donor_log_probability_change"])
            )
        for layer in record["layers"]:
            values = [
                float(cell["donor_log_probability_change"])
                for cell in record["cells"]
                if int(cell["layer"]) == int(layer)
            ]
            layer_means[str(layer)] = mean(values)
        outputs.append(
            {
                "path": str(path),
                "donor_id": record["donor_id"],
                "target_id": record["target_id"],
                "cell_count": len(record["cells"]),
                "mean_donor_log_probability_change": {
                    kind: mean(values) for kind, values in by_type.items()
                },
                "median_donor_log_probability_change": {
                    kind: statistics.median(values)
                    for kind, values in by_type.items()
                },
                "positive_cells": {
                    kind: sum(value > 0 for value in values)
                    for kind, values in by_type.items()
                },
                "cells_by_type": {
                    kind: len(values) for kind, values in by_type.items()
                },
                "layer_means": layer_means,
            }
        )
    return outputs


def summarize_workspace(path: Path) -> dict[str, Any]:
    record = json.loads(path.read_text(encoding="utf-8"))
    output: dict[str, Any] = {"direction_count": len(record["directions"]), "stages": {}}
    for stage in record["stages"]:
        by_position: dict[int, list[float]] = defaultdict(list)
        by_mod4: dict[int, list[float]] = defaultdict(list)
        for direction in record["directions"]:
            for item in direction["cross_position"]:
                if item["stage"] != stage:
                    continue
                position = int(item["destination_position"])
                change = float(item["donor_answer"]["log_probability_change"])
                by_position[position].append(change)
                by_mod4[position % 4].append(change)
        early = [value for pos, values in by_position.items() if pos <= 10 for value in values]
        late = [value for pos, values in by_position.items() if pos >= 41 for value in values]
        position_means = {str(pos): mean(values) for pos, values in by_position.items()}
        output["stages"][stage] = {
            "early_positions_1_10_mean": mean(early),
            "late_positions_41_50_mean": mean(late),
            "late_minus_early": mean(late) - mean(early),
            "destination_ordinal_mod4_means": {
                str(modulo): mean(values) for modulo, values in by_mod4.items()
            },
            "top_destination_positions": [
                {"position": pos, "mean_log_probability_change": value}
                for value, pos in sorted(
                    ((value, int(pos)) for pos, value in position_means.items()),
                    reverse=True,
                )[:10]
            ],
        }
    return output


def markdown_report(output: dict[str, Any]) -> str:
    lines = [
        "# DeepSeek V4 variable-binding architecture analysis",
        "",
        "This descriptive analysis relates existing k=50 J-Lens/logit-lens and "
        "causal results to V4 Flash's attention schedule: layers 0–1 are local "
        "sliding-window attention, then even layers are 4× Compressed Sparse "
        "Attention (CSA) and odd layers are 128× Heavily Compressed Attention (HCA).",
        "",
        "## Layer-type result",
        "",
    ]
    readouts = output["readouts"]
    for lens in ("j_lens", "logit_lens"):
        result = readouts["lenses"][lens]
        top1 = result["exact_rank1_cells"]
        lines.extend(
            [
                f"### {lens.replace('_', ' ').title()}",
                "",
                "| Metric | CSA | HCA |",
                "|---|---:|---:|",
                f"| Exact rank-1 cells | {top1['CSA']['count']} / {top1['CSA']['total']} "
                f"({top1['CSA']['rate']:.2%}) | {top1['HCA']['count']} / "
                f"{top1['HCA']['total']} ({top1['HCA']['rate']:.2%}) |",
                f"| Mean log-rank improvement entering layer | "
                f"{result['mean_log_rank_improvement_entering_layer_type']['CSA']:.3f} | "
                f"{result['mean_log_rank_improvement_entering_layer_type']['HCA']:.3f} |",
                "",
            ]
        )
        for threshold in (1, 5, 10, 50):
            crossing = result["first_crossings"][str(threshold)]
            counts = crossing["first_crossing_layer_types"]
            lines.append(
                f"At rank ≤{threshold}, {counts.get('CSA', 0)} first crossings were "
                f"in CSA and {counts.get('HCA', 0)} were in HCA "
                f"({crossing['events']} observed stage/example crossings)."
            )
        lines.append("")

    lines.extend(["## Causal layer-type result", ""])
    for grid in output["causal_grids"]:
        means = grid["mean_donor_log_probability_change"]
        lines.append(
            f"- `{grid['donor_id']} → {grid['target_id']}`: mean donor-answer "
            f"log-probability change was {means['CSA']:.3f} in CSA versus "
            f"{means['HCA']:.3f} in HCA across {grid['cell_count']} one-cell patches."
        )
    lines.extend(
        [
            "",
            "The two attention types are nearly tied causally. The current evidence "
            "therefore does not support a mechanism confined to either CSA or HCA.",
            "",
            "## Position result",
            "",
        ]
    )
    for stage, result in output["workspace"]["stages"].items():
        mod_values = result["destination_ordinal_mod4_means"]
        lines.append(
            f"- **{stage}:** moving one fixed donor state into positions 41–50 changed "
            f"donor-answer log probability by {result['late_positions_41_50_mean']:.3f} "
            f"on average, versus {result['early_positions_1_10_mean']:.3f} for positions "
            f"1–10 (late − early = {result['late_minus_early']:.3f}). Destination "
            f"modulo-4 means were "
            + ", ".join(
                f"r={key}: {value:.3f}" for key, value in sorted(mod_values.items())
            )
            + "."
        )
    lines.extend(
        [
            "",
            "Receiver gain rises strongly toward the end of the filler span but is "
            "essentially flat modulo four. That is evidence against the four-token "
            "CSA compression boundary itself explaining the useful late-dot lanes.",
            "",
            "## Interpretation limits",
            "",
            "Cells from the same prompt are correlated, and the attention types "
            "alternate, so these are descriptive comparisons rather than independent "
            "statistical tests. A direct attention-mask ablation and an mHC stream "
            "ablation are required to distinguish serial dot communication from "
            "parallel slots and to test whether four-stream mHC is necessary.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    records = load_readouts(args.readout_dir)
    output = {
        "schema_version": 1,
        "attention_schedule": {
            "layers_0_1": "SWA (compress ratio 0)",
            "even_layers_2_40": "CSA (compress ratio 4)",
            "odd_layers_3_41": "HCA (compress ratio 128)",
        },
        "readouts": summarize_readouts(records),
        "causal_grids": summarize_causal_grids(args.causal_grid),
        "workspace": summarize_workspace(args.workspace_probe),
        "input_example_ids": sorted(records),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "architecture-analysis.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "architecture-analysis.md").write_text(
        markdown_report(output), encoding="utf-8"
    )
    print(f"wrote {args.output_dir}")


if __name__ == "__main__":
    main()
