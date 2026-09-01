#!/usr/bin/env python3
"""Summarize a generic paired filler-length sweep and select lens candidates."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def safe_mean(values: list[float]) -> float | None:
    return statistics.fmean(values) if values else None


def exact_mcnemar_p(helped: int, hurt: int) -> float:
    """Two-sided exact binomial test on discordant paired outcomes."""
    discordant = helped + hurt
    if discordant == 0:
        return 1.0
    tail = sum(math.comb(discordant, index) for index in range(min(helped, hurt) + 1))
    return min(1.0, 2.0 * tail / (2**discordant))


def summarize_rows(rows: list[dict[str, Any]], lengths: list[int]) -> dict[str, Any]:
    by_length: dict[str, Any] = {}
    for length in lengths:
        conditions = [row["conditions"][str(length)] for row in rows]
        reciprocal_ranks = [1.0 / condition["target"]["best_rank"] for condition in conditions]
        by_length[str(length)] = {
            "n": len(conditions),
            "correct": sum(bool(condition["correct"]) for condition in conditions),
            "accuracy": safe_mean([float(condition["correct"]) for condition in conditions]),
            "mrr": safe_mean(reciprocal_ranks),
            "recall_at_1": safe_mean(
                [float(condition["target"]["best_rank"] <= 1) for condition in conditions]
            ),
            "recall_at_5": safe_mean(
                [float(condition["target"]["best_rank"] <= 5) for condition in conditions]
            ),
            "recall_at_10": safe_mean(
                [float(condition["target"]["best_rank"] <= 10) for condition in conditions]
            ),
            "recall_at_50": safe_mean(
                [float(condition["target"]["best_rank"] <= 50) for condition in conditions]
            ),
        }

    paired: dict[str, Any] = {}
    for length in lengths:
        if length == 0:
            continue
        helped: list[str] = []
        hurt: list[str] = []
        rank_gains: list[tuple[float, str]] = []
        for row in rows:
            baseline = row["conditions"]["0"]
            filler = row["conditions"][str(length)]
            if filler["correct"] and not baseline["correct"]:
                helped.append(row["id"])
            if baseline["correct"] and not filler["correct"]:
                hurt.append(row["id"])
            baseline_rank = int(baseline["target"]["best_rank"])
            filler_rank = int(filler["target"]["best_rank"])
            log_rank_gain = math.log10(baseline_rank) - math.log10(filler_rank)
            rank_gains.append((log_rank_gain, row["id"]))
        rank_gains.sort(reverse=True)
        paired[str(length)] = {
            "helped_count": len(helped),
            "hurt_count": len(hurt),
            "net_correct": len(helped) - len(hurt),
            "exact_mcnemar_p": exact_mcnemar_p(len(helped), len(hurt)),
            "helped_ids": helped,
            "hurt_ids": hurt,
            "mean_log10_rank_gain": safe_mean([gain for gain, _ in rank_gains]),
            "largest_rank_gain_ids": [example_id for _, example_id in rank_gains[:10]],
        }
    return {"by_length": by_length, "paired_vs_k0": paired}


def group_rows(
    rows: list[dict[str, Any]], field: str | None
) -> dict[str, list[dict[str, Any]]]:
    if field is None:
        return {}
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        value = row["example"].get(field)
        groups[str(value)].append(row)
    return dict(groups)


def markdown(summary: dict[str, Any], task_type: str, lengths: list[int]) -> str:
    lines = [
        f"# {task_type.replace('_', ' ').title()} filler-length sweep",
        "",
        "| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for length in lengths:
        row = summary["overall"]["by_length"][str(length)]
        if length == 0:
            transition = "—"
            p_value = "—"
        else:
            pair = summary["overall"]["paired_vs_k0"][str(length)]
            transition = f"{pair['helped_count']} / {pair['hurt_count']}"
            p_value = f"{pair['exact_mcnemar_p']:.3g}"
        lines.append(
            f"| {length} | {row['n']} | {row['correct']} | {row['accuracy']:.3f} | "
            f"{row['mrr']:.3f} | {row['recall_at_10']:.3f} | {transition} | {p_value} |"
        )
    for group_name, group_summary in summary.get("groups", {}).items():
        lines.extend(
            [
                "",
                f"## Group `{group_name}`",
                "",
                "| Visible dots | N | Accuracy | Answer MRR |",
                "|---:|---:|---:|---:|",
            ]
        )
        for length in lengths:
            row = group_summary["by_length"][str(length)]
            lines.append(
                f"| {length} | {row['n']} | {row['accuracy']:.3f} | {row['mrr']:.3f} |"
            )
    lines.extend(
        [
            "",
            "The rank metrics use the model's actual next-token logits, not either lens. "
            "They are used only to choose behaviorally meaningful examples for readout extraction.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--group-field")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    lengths = [int(value) for value in data["filler_lengths"]]
    rows = data["examples"]
    summary: dict[str, Any] = {"overall": summarize_rows(rows, lengths)}
    groups = group_rows(rows, args.group_field)
    if groups:
        summary["group_field"] = args.group_field
        summary["groups"] = {
            name: summarize_rows(group, lengths) for name, group in groups.items()
        }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "behavior-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (args.output_dir / "behavior-report.md").write_text(
        markdown(summary, data["task_type"], lengths), encoding="utf-8"
    )
    print(args.output_dir / "behavior-report.md")


if __name__ == "__main__":
    main()
