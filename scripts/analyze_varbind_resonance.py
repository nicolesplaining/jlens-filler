#!/usr/bin/env python3
"""Summarize one variable-binding example across non-monotonic filler lengths."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


STAGES = ("base_value", "bound_value", "second_product", "answer")
DISTRACTOR_STAGES = (
    "distractor_bound",
    "distractor_second_product",
    "distractor_answer",
)


def keyed_path(value: str) -> tuple[int, Path]:
    key, separator, path = value.partition("=")
    if not separator:
        raise argparse.ArgumentTypeError("expected FILLER_LENGTH=RESULT.json")
    return int(key), Path(path)


def best_rank(target: dict[str, Any]) -> int | None:
    ranks = [int(item["rank"]) for item in target["variants"] if "rank" in item]
    return min(ranks, default=None)


def summarize(
    result: dict[str, Any], filler_length: int, behavior: dict[str, Any]
) -> dict[str, Any]:
    if bool(result["model_output"]["correct"]) != bool(behavior["correct"]):
        raise ValueError(f"readout and behavior correctness disagree at k={filler_length}")
    output: dict[str, Any] = {
        "filler_length": filler_length,
        "example_id": result["example"]["id"],
        "correct": bool(result["model_output"]["correct"]),
        "generated_text": result["model_output"]["generated_text"],
        "answer_rank": int(behavior["target"]["best_rank"]),
        "methods": {},
    }
    for method in ("j_lens", "logit_lens"):
        method_output = {}
        for stage in STAGES + DISTRACTOR_STAGES:
            cells = []
            for layer_text, row in result["readouts"][method].items():
                layer = int(layer_text)
                for cell in row:
                    if cell["position_kind"] != "filler":
                        continue
                    rank = best_rank(cell["targets"][stage])
                    if rank is None:
                        continue
                    cells.append(
                        {
                            "layer": layer,
                            "position": int(cell["filler_ordinal"]),
                            "rank": rank,
                        }
                    )
            rank1 = [cell for cell in cells if cell["rank"] == 1]
            top10 = [cell for cell in cells if cell["rank"] <= 10]
            method_output[stage] = {
                "rank1_cells": len(rank1),
                "top10_cells": len(top10),
                "first_rank1_layer": min(
                    (cell["layer"] for cell in rank1), default=None
                ),
                "first_rank1_position": min(
                    (
                        cell["position"]
                        for cell in rank1
                        if cell["layer"]
                        == min(item["layer"] for item in rank1)
                    ),
                    default=None,
                ),
                "rank1_positions": sorted({cell["position"] for cell in rank1}),
                "top10_strength": sum((11 - cell["rank"]) / 10 for cell in top10),
            }
        output["methods"][method] = method_output
    return output


def write_report(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# Dot-count resonance readouts",
        "",
        "These are J-Lens token readouts, not formal sparse J-space coordinates.",
        "",
        "| Dots | Output | Correct | Answer rank |",
        "|---:|---:|:---:|---:|",
    ]
    for row in summary["lengths"]:
        lines.append(
            f"| {row['filler_length']} | {row['generated_text'].strip()} | "
            f"{'yes' if row['correct'] else 'no'} | {row['answer_rank']} |"
        )
    for method, label in (("j_lens", "J-Lens"), ("logit_lens", "Logit lens")):
        lines.extend(
            [
                "",
                f"## {label}",
                "",
                "Each cell is `rank-1 count / rank-weighted top-10 strength "
                "(first rank-1 layer, dot)`.",
                "",
                "| Dots | Base | Bound | Second product | Answer |",
                "|---:|---:|---:|---:|---:|",
            ]
        )
        for row in summary["lengths"]:
            values = []
            for stage in STAGES:
                item = row["methods"][method][stage]
                onset = (
                    "—"
                    if item["first_rank1_layer"] is None
                    else f"L{item['first_rank1_layer']},F{item['first_rank1_position']}"
                )
                values.append(
                    f"{item['rank1_cells']} / {item['top10_strength']:.1f} ({onset})"
                )
            lines.append(f"| {row['filler_length']} | " + " | ".join(values) + " |")
    lines.extend(
        [
            "",
            "## Correct route versus sibling-variable route (J-Lens)",
            "",
            "The wrong output 185 is the exact result of applying the question's "
            "final operation to sibling variable `rek=100` instead of requested "
            "variable `xav=125`.",
            "",
            "Each cell is `rank-1 count / rank-weighted top-10 strength`.",
            "",
            "| Dots | Correct bound 125 | Distractor bound 100 | Correct product 250 | Distractor product 200 | Correct answer 235 | Distractor answer 185 |",
            "|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in summary["lengths"]:
        method = row["methods"]["j_lens"]
        def route(stage: str) -> str:
            item = method[stage]
            return f"{item['rank1_cells']} / {item['top10_strength']:.1f}"
        lines.append(
            f"| {row['filler_length']} | {route('bound_value')} | "
            f"{route('distractor_bound')} | {route('second_product')} | "
            f"{route('distractor_second_product')} | {route('answer')} | "
            f"{route('distractor_answer')} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readout", action="append", type=keyed_path, required=True)
    parser.add_argument("--example-id", required=True)
    parser.add_argument("--behavior-sweep", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    paths = dict(args.readout)
    if len(paths) != len(args.readout):
        raise ValueError("filler lengths must be unique")
    behavior_sweep = json.loads(args.behavior_sweep.read_text(encoding="utf-8"))
    behavior_row = next(
        (row for row in behavior_sweep["examples"] if row["id"] == args.example_id),
        None,
    )
    if behavior_row is None:
        raise ValueError(f"behavior sweep is missing {args.example_id}")
    lengths = []
    for filler_length, path in sorted(paths.items()):
        result = json.loads(path.read_text(encoding="utf-8"))
        if result["example"]["id"] != args.example_id:
            raise ValueError(f"{path} is not {args.example_id}")
        if int(result["condition"]["filler_length"]) != filler_length:
            raise ValueError(f"{path} filler count does not match k={filler_length}")
        lengths.append(
            summarize(result, filler_length, behavior_row["conditions"][str(filler_length)])
        )
    summary = {
        "schema_version": 1,
        "example_id": args.example_id,
        "expected_intermediates": json.loads(
            paths[min(paths)].read_text(encoding="utf-8")
        )["example"]["expected_intermediates"],
        "lengths": lengths,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "resonance-summary.json"
    output.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_report(summary, args.output_dir / "resonance-report.md")
    print(output)


if __name__ == "__main__":
    main()
