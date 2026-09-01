#!/usr/bin/env python3
"""Build a full-readout config for every k=50-rescued varbind example."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("sweep", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--filler-length", type=int, default=50)
    parser.add_argument("--include-failures", action="store_true")
    return parser.parse_args()


def assign_controls(examples: list[dict[str, Any]]) -> None:
    """Attach a complete stage-matched derangement with no value collisions."""
    for index, recipient in enumerate(examples):
        actual = set(recipient["expected_intermediates"].values())
        donor = None
        for offset in range(1, len(examples)):
            candidate = examples[(index + offset) % len(examples)]
            candidate_values = set(candidate["expected_intermediates"].values())
            if not actual & candidate_values:
                donor = candidate
                break
        if donor is None:
            raise ValueError(f"no collision-free control donor for {recipient['id']}")
        recipient["tracked_controls"] = {
            f"control_{label}": surface
            for label, surface in donor["expected_intermediates"].items()
        }
        recipient["control_donor_id"] = donor["id"]


def main() -> None:
    args = parse_args()
    sweep = json.loads(args.sweep.read_text(encoding="utf-8"))
    source = json.loads(args.config.read_text(encoding="utf-8"))
    length_text = str(args.filler_length)
    if args.filler_length not in map(int, sweep["filler_lengths"]):
        raise ValueError(f"k={args.filler_length} is absent from the behavior sweep")

    cohorts: dict[str, str] = {}
    for row in sweep["examples"]:
        baseline = bool(row["conditions"]["0"]["correct"])
        filler = bool(row["conditions"][length_text]["correct"])
        if filler and not baseline:
            cohorts[row["id"]] = "rescued"
        elif args.include_failures and not filler:
            cohorts[row["id"]] = "filler_failure"
    if not any(cohort == "rescued" for cohort in cohorts.values()):
        raise ValueError("selection contains no dot-rescued examples")

    selected: list[dict[str, Any]] = []
    for raw in source["examples"]:
        if raw["id"] not in cohorts:
            continue
        item = copy.deepcopy(raw)
        item["behavior_cohort"] = cohorts[item["id"]]
        selected.append(item)
    if set(cohorts) != {item["id"] for item in selected}:
        raise ValueError("behavior IDs and source config IDs do not match")
    assign_controls(selected)

    output = copy.deepcopy(source)
    output.pop("filler_lengths", None)
    output["filler_length"] = args.filler_length
    output["examples"] = selected
    output["source"]["selection"] += (
        f"; deep-dive extraction of all k={args.filler_length} rescued examples"
        + (" plus all k=50 failures" if args.include_failures else "")
        + "; each target has a collision-free, stage-matched deranged control"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "filler_length": args.filler_length,
                "n": len(selected),
                "cohorts": {
                    cohort: sum(item["behavior_cohort"] == cohort for item in selected)
                    for cohort in sorted(set(cohorts.values()))
                },
                "ids": [item["id"] for item in selected],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
