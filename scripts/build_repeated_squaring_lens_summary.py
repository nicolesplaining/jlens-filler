#!/usr/bin/env python3
"""Summarize best filler-cell J-Lens and logit-lens ranks."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def best_cell(
    data: dict[str, Any], method: str, target: str, filler_indices: set[int]
) -> dict[str, int]:
    candidates = []
    for layer, cells in data["readouts"][method].items():
        for cell in cells:
            if cell["absolute_index"] not in filler_indices:
                continue
            candidates.append(
                {
                    "rank": int(cell["targets"][target]["best_rank"]),
                    "layer": int(layer),
                    "filler_position": int(cell["filler_ordinal"]),
                }
            )
    return min(
        candidates,
        key=lambda item: (item["rank"], item["layer"], item["filler_position"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results_dir", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--example-ids",
        help="Optional comma-separated subset of config example IDs.",
    )
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    selected_ids = (
        {value.strip() for value in args.example_ids.split(",") if value.strip()}
        if args.example_ids
        else None
    )
    selected_examples = [
        example
        for example in config["examples"]
        if selected_ids is None or example["id"] in selected_ids
    ]
    if selected_ids is not None:
        missing = selected_ids - {example["id"] for example in selected_examples}
        if missing:
            raise ValueError(f"unknown example IDs: {sorted(missing)}")
    if not selected_examples:
        raise ValueError("no examples selected")
    records = []
    examples = []
    for example in selected_examples:
        path = args.results_dir / f"{example['id']}.json"
        data = json.loads(path.read_text())
        filler_indices = {
            int(column["absolute_index"])
            for column in data["selected_columns"]
            if column["position_kind"] == "filler"
        }
        example_record = {
            "id": example["id"],
            "selection_reason": example["selection_reason"],
            "time_steps": int(example["time_steps"]),
            "expected_answer": int(example["answer"]),
            "dots_answer": data["model_output"]["parsed_answer"],
            "dots_correct": bool(data["model_output"]["correct"]),
            "no_dots_answer": data["no_filler_control"]["parsed_answer"],
            "no_dots_correct": bool(data["no_filler_control"]["correct"]),
            "closure_max_absolute_error": float(
                data["compatibility_checks"][
                    "layer_42_final_head_closure_max_abs_error"
                ]
            ),
        }
        examples.append(example_record)
        for target, surface in example["expected_intermediates"].items():
            for method in ("j_lens", "logit_lens"):
                best = best_cell(data, method, target, filler_indices)
                records.append(
                    {
                        "example_id": example["id"],
                        "time_steps": int(example["time_steps"]),
                        "target": target,
                        "surface": surface,
                        "method": method,
                        "best_rank": best["rank"],
                        "best_layer": best["layer"],
                        "best_filler_position": best["filler_position"],
                    }
                )

    j = {
        (record["example_id"], record["target"]): record
        for record in records
        if record["method"] == "j_lens"
    }
    ll = {
        (record["example_id"], record["target"]): record
        for record in records
        if record["method"] == "logit_lens"
    }
    keys = sorted(j)
    comparison = {
        "target_instances": len(keys),
        "j_lens_better": sum(j[key]["best_rank"] < ll[key]["best_rank"] for key in keys),
        "logit_lens_better": sum(j[key]["best_rank"] > ll[key]["best_rank"] for key in keys),
        "tied": sum(j[key]["best_rank"] == ll[key]["best_rank"] for key in keys),
        "j_lens_top_10": sum(j[key]["best_rank"] <= 10 for key in keys),
        "logit_lens_top_10": sum(ll[key]["best_rank"] <= 10 for key in keys),
    }
    output = {"examples": examples, "comparison": comparison, "records": records}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "lens-summary.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False)
    )
    with (args.output_dir / "lens-summary.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(json.dumps(comparison, indent=2))


if __name__ == "__main__":
    main()
