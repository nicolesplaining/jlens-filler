#!/usr/bin/env python3
"""Select correct/dot-helped arithmetic programs for full lens extraction."""

from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("sweep", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--filler-length", type=int)
    parser.add_argument("--per-topology", type=int, default=3)
    parser.add_argument(
        "--example-ids",
        default="",
        help="optional comma-separated explicit selection, in the requested order",
    )
    return parser.parse_args()


def choose_length(data: dict[str, Any]) -> int:
    candidates = [int(value) for value in data["filler_lengths"] if int(value) > 0]
    rows = data["examples"]
    # Favor actual performance, then enough positions to expose spatial structure.
    return max(
        candidates,
        key=lambda length: (
            sum(row["conditions"][str(length)]["correct"] for row in rows),
            length,
        ),
    )


def priority(row: dict[str, Any], length: int) -> tuple[Any, ...]:
    baseline = row["conditions"]["0"]
    filler = row["conditions"][str(length)]
    helped = bool(filler["correct"] and not baseline["correct"])
    both = bool(filler["correct"] and baseline["correct"])
    return (
        int(helped),
        int(both),
        int(filler["correct"]),
        -int(filler["target"]["best_rank"]),
        row["id"],
    )


def add_deranged_controls(examples: list[dict[str, Any]]) -> None:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for example in examples:
        groups[str(example["topology"])].append(example)
    for group in groups.values():
        if len(group) < 2:
            continue
        for index, recipient in enumerate(group):
            actual_values = set(recipient["expected_intermediates"].values())
            donor = None
            for offset in range(1, len(group)):
                candidate = group[(index + offset) % len(group)]
                if not actual_values & set(candidate["expected_intermediates"].values()):
                    donor = candidate
                    break
            if donor is None:
                donor = group[(index + 1) % len(group)]
            recipient["tracked_controls"] = {
                f"control_{label}": surface
                for label, surface in donor["expected_intermediates"].items()
                if surface not in actual_values
            }
            recipient["control_donor_id"] = donor["id"]


def main() -> None:
    args = parse_args()
    sweep = json.loads(args.sweep.read_text(encoding="utf-8"))
    config = json.loads(args.config.read_text(encoding="utf-8"))
    length = args.filler_length or choose_length(sweep)
    if length not in map(int, sweep["filler_lengths"]):
        raise ValueError(f"filler length {length} was not evaluated")

    if args.example_ids:
        selected_ids = [
            value.strip() for value in args.example_ids.split(",") if value.strip()
        ]
    else:
        rows_by_topology: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in sweep["examples"]:
            rows_by_topology[str(row["example"]["topology"])].append(row)
        selected_ids = []
        for topology in sorted(rows_by_topology):
            ordered = sorted(
                rows_by_topology[topology],
                key=lambda row: priority(row, length),
                reverse=True,
            )
            correct = [
                row for row in ordered if row["conditions"][str(length)]["correct"]
            ]
            # Readout extraction is expensive and algorithm claims should begin with
            # behaviorally successful executions. Keep fewer cases rather than pad a
            # topology with known-wrong outputs.
            selected_ids.extend(
                row["id"] for row in correct[: args.per_topology]
            )

    source_by_id = {item["id"]: item for item in config["examples"]}
    missing = set(selected_ids) - set(source_by_id)
    if missing:
        raise ValueError(f"explicit example IDs are absent: {sorted(missing)}")
    selected = [copy.deepcopy(source_by_id[example_id]) for example_id in selected_ids]
    add_deranged_controls(selected)
    output = copy.deepcopy(config)
    output.pop("filler_lengths", None)
    output["filler_length"] = length
    output["examples"] = selected
    output["source"]["selection"] += (
        f"; full readout at k={length}, up to {args.per_topology} cases per topology, "
        "prioritizing dot-helped then correct-in-both examples; cross-example "
        "stage-matched target values included as tracked controls"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"filler_length": length, "selected_ids": selected_ids}, indent=2))


if __name__ == "__main__":
    main()
