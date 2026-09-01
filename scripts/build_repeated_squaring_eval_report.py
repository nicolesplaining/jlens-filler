#!/usr/bin/env python3
"""Combine the paired dot evaluation, compute statistics, and write reports."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from pathlib import Path
from typing import Any, Callable


EXCLUDED_BASE = (299, 35)
BOOTSTRAP_SAMPLES = 20_000
BOOTSTRAP_SEED = 42


def exact_two_sided_binomial(successes: int, trials: int) -> float:
    if trials == 0:
        return 1.0
    tail = min(successes, trials - successes)
    probability = 2 * sum(math.comb(trials, value) for value in range(tail + 1))
    return min(1.0, probability / (2**trials))


def percentile_interval(values: list[float]) -> list[float]:
    ordered = sorted(values)
    return [
        ordered[int(0.025 * len(ordered))],
        ordered[int(0.975 * len(ordered))],
    ]


def bootstrap_interval(
    rows: list[dict[str, Any]], metric: Callable[[list[dict[str, Any]]], float]
) -> list[float]:
    rng = random.Random(BOOTSTRAP_SEED)
    count = len(rows)
    samples = []
    for _ in range(BOOTSTRAP_SAMPLES):
        resample = [rows[rng.randrange(count)] for _ in range(count)]
        samples.append(metric(resample))
    return percentile_interval(samples)


def accuracy_difference(rows: list[dict[str, Any]]) -> float:
    return sum(
        row["dots"]["correct"] - row["no_dots"]["correct"] for row in rows
    ) / len(rows)


def log_probability_difference(rows: list[dict[str, Any]]) -> float:
    return sum(
        row["dots"]["target"]["best_log_probability"]
        - row["no_dots"]["target"]["best_log_probability"]
        for row in rows
    ) / len(rows)


def reciprocal_rank_difference(rows: list[dict[str, Any]]) -> float:
    return sum(
        1 / row["dots"]["target"]["best_rank"]
        - 1 / row["no_dots"]["target"]["best_rank"]
        for row in rows
    ) / len(rows)


def summarize(rows: list[dict[str, Any]], *, intervals: bool = False) -> dict[str, Any]:
    count = len(rows)
    dots_correct = sum(row["dots"]["correct"] for row in rows)
    no_dots_correct = sum(row["no_dots"]["correct"] for row in rows)
    dots_only = sum(
        row["dots"]["correct"] and not row["no_dots"]["correct"] for row in rows
    )
    no_dots_only = sum(
        row["no_dots"]["correct"] and not row["dots"]["correct"] for row in rows
    )
    both = sum(
        row["dots"]["correct"] and row["no_dots"]["correct"] for row in rows
    )
    neither = count - dots_only - no_dots_only - both
    dots_better = sum(
        row["dots"]["target"]["best_rank"]
        < row["no_dots"]["target"]["best_rank"]
        for row in rows
    )
    no_dots_better = sum(
        row["dots"]["target"]["best_rank"]
        > row["no_dots"]["target"]["best_rank"]
        for row in rows
    )
    tied = count - dots_better - no_dots_better
    output: dict[str, Any] = {
        "n": count,
        "dots_correct": dots_correct,
        "no_dots_correct": no_dots_correct,
        "dots_accuracy": dots_correct / count,
        "no_dots_accuracy": no_dots_correct / count,
        "accuracy_difference": (dots_correct - no_dots_correct) / count,
        "paired_outcomes": {
            "dots_only_correct": dots_only,
            "no_dots_only_correct": no_dots_only,
            "both_correct": both,
            "neither_correct": neither,
            "exact_mcnemar_p": exact_two_sided_binomial(
                dots_only, dots_only + no_dots_only
            ),
        },
        "target_rank": {
            "dots_mean": statistics.mean(
                row["dots"]["target"]["best_rank"] for row in rows
            ),
            "no_dots_mean": statistics.mean(
                row["no_dots"]["target"]["best_rank"] for row in rows
            ),
            "dots_median": statistics.median(
                row["dots"]["target"]["best_rank"] for row in rows
            ),
            "no_dots_median": statistics.median(
                row["no_dots"]["target"]["best_rank"] for row in rows
            ),
            "dots_better": dots_better,
            "no_dots_better": no_dots_better,
            "tied": tied,
            "exact_sign_test_p": exact_two_sided_binomial(
                dots_better, dots_better + no_dots_better
            ),
        },
        "mean_reciprocal_rank": {
            "dots": statistics.mean(
                1 / row["dots"]["target"]["best_rank"] for row in rows
            ),
            "no_dots": statistics.mean(
                1 / row["no_dots"]["target"]["best_rank"] for row in rows
            ),
            "difference": reciprocal_rank_difference(rows),
        },
        "mean_target_log_probability": {
            "dots": statistics.mean(
                row["dots"]["target"]["best_log_probability"] for row in rows
            ),
            "no_dots": statistics.mean(
                row["no_dots"]["target"]["best_log_probability"] for row in rows
            ),
            "difference": log_probability_difference(rows),
        },
    }
    if intervals:
        output["paired_bootstrap_95_percent_intervals"] = {
            "accuracy_difference": bootstrap_interval(rows, accuracy_difference),
            "mean_reciprocal_rank_difference": bootstrap_interval(
                rows, reciprocal_rank_difference
            ),
            "mean_target_log_probability_difference": bootstrap_interval(
                rows, log_probability_difference
            ),
            "samples": BOOTSTRAP_SAMPLES,
            "seed": BOOTSTRAP_SEED,
        }
    return output


def validate_rows(rows: list[dict[str, Any]]) -> None:
    if len(rows) != 100:
        raise AssertionError(f"evaluation has {len(rows)} rows, expected 100")
    for step in range(1, 11):
        if sum(int(row["time_steps"]) == step for row in rows) != 10:
            raise AssertionError(f"T={step} does not have ten rows")
    shortcut_rows = [row["id"] for row in rows if row["expected_answer"] == row["x"]]
    if shortcut_rows:
        raise AssertionError(f"final answer equals x_0 in: {shortcut_rows}")
    t10_rows = [row for row in rows if int(row["time_steps"]) == 10]
    for row in t10_rows:
        trace = [int(value) for value in row["expected_intermediates"].values()]
        if len(trace) != 10 or len(set(trace)) != 10 or int(row["x"]) in trace:
            raise AssertionError(f"trace is cyclic within the horizon: {row['id']}")


def combine(
    initial: dict[str, Any], replacement: dict[str, Any]
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    kept = [
        row
        for row in initial["examples"]
        if (int(row["modulus"]), int(row["x"])) != EXCLUDED_BASE
    ]
    removed = len(initial["examples"]) - len(kept)
    replacement_rows = replacement["examples"]
    if removed != 10 or len(replacement_rows) != 10:
        raise AssertionError(
            f"expected to replace ten rows, removed={removed}, added={len(replacement_rows)}"
        )
    rows = kept + replacement_rows
    rows.sort(key=lambda row: (int(row["time_steps"]), int(row["modulus"])))
    validate_rows(rows)
    provenance = {
        "initial_file": "paired_task_eval_initial.json",
        "replacement_file": "replacement/paired_task_eval.json",
        "excluded_base": {"modulus": EXCLUDED_BASE[0], "x": EXCLUDED_BASE[1]},
        "exclusion_reason": (
            "Its T=10 answer equaled x_0, so copying the input could mimic a "
            "ten-step success. All ten T values for that base were replaced."
        ),
        "replacement_base": {"modulus": 667, "x": 41},
        "combined_assertions": {
            "n": 100,
            "ten_examples_per_T": True,
            "no_final_answer_equals_x_0": True,
        },
    }
    return rows, provenance


def write_pairs_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "id",
        "modulus",
        "x",
        "time_steps",
        "expected_answer",
        "dots_answer",
        "dots_correct",
        "dots_target_rank",
        "dots_target_log_probability",
        "no_dots_answer",
        "no_dots_correct",
        "no_dots_target_rank",
        "no_dots_target_log_probability",
        "rank_delta_no_dots_minus_dots",
        "log_probability_delta_dots_minus_no_dots",
    ]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row["id"],
                    "modulus": row["modulus"],
                    "x": row["x"],
                    "time_steps": row["time_steps"],
                    "expected_answer": row["expected_answer"],
                    "dots_answer": row["dots"]["parsed_answer"],
                    "dots_correct": row["dots"]["correct"],
                    "dots_target_rank": row["dots"]["target"]["best_rank"],
                    "dots_target_log_probability": row["dots"]["target"][
                        "best_log_probability"
                    ],
                    "no_dots_answer": row["no_dots"]["parsed_answer"],
                    "no_dots_correct": row["no_dots"]["correct"],
                    "no_dots_target_rank": row["no_dots"]["target"]["best_rank"],
                    "no_dots_target_log_probability": row["no_dots"]["target"][
                        "best_log_probability"
                    ],
                    "rank_delta_no_dots_minus_dots": (
                        row["no_dots"]["target"]["best_rank"]
                        - row["dots"]["target"]["best_rank"]
                    ),
                    "log_probability_delta_dots_minus_no_dots": (
                        row["dots"]["target"]["best_log_probability"]
                        - row["no_dots"]["target"]["best_log_probability"]
                    ),
                }
            )


def write_summary_csv(path: Path, summaries: dict[str, dict[str, Any]]) -> None:
    fields = [
        "time_steps",
        "n",
        "dots_correct",
        "no_dots_correct",
        "dots_accuracy",
        "no_dots_accuracy",
        "accuracy_difference",
        "dots_median_target_rank",
        "no_dots_median_target_rank",
        "dots_better_rank_count",
        "no_dots_better_rank_count",
        "mean_log_probability_difference",
    ]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for label, summary in summaries.items():
            writer.writerow(
                {
                    "time_steps": label,
                    "n": summary["n"],
                    "dots_correct": summary["dots_correct"],
                    "no_dots_correct": summary["no_dots_correct"],
                    "dots_accuracy": summary["dots_accuracy"],
                    "no_dots_accuracy": summary["no_dots_accuracy"],
                    "accuracy_difference": summary["accuracy_difference"],
                    "dots_median_target_rank": summary["target_rank"]["dots_median"],
                    "no_dots_median_target_rank": summary["target_rank"][
                        "no_dots_median"
                    ],
                    "dots_better_rank_count": summary["target_rank"]["dots_better"],
                    "no_dots_better_rank_count": summary["target_rank"][
                        "no_dots_better"
                    ],
                    "mean_log_probability_difference": summary[
                        "mean_target_log_probability"
                    ]["difference"],
                }
            )


def percent(value: float) -> str:
    return f"{100 * value:.1f}%"


def write_markdown(
    path: Path,
    rows: list[dict[str, Any]],
    overall: dict[str, Any],
    by_t: dict[str, dict[str, Any]],
) -> None:
    interval = overall["paired_bootstrap_95_percent_intervals"]
    paper_sentence = (
        "After the question, there will be 10 filler tokens "
        "(a sequence of dots) before you answer."
    )
    paper_matched = paper_sentence in rows[0]["dots"]["rendered_prompt"]
    prompt_boundary = (
        "The dots system instruction uses the Appendix A wording for k=10 "
        f'exactly: “{paper_sentence}” Ten spaced periods appear after `Filler:` '
        "in every demonstration and target."
        if paper_matched
        else
        "This is a legacy prompt run: its system message says only “some filler "
        "tokens” and adds an extra-space rationale. It predates the exact Appendix A "
        "prompt match and should not be pooled with the paper-matched results."
    )
    lines = [
        "# Do dot fillers improve repeated squaring?",
        "",
        "## Result",
        "",
        f"Across 100 matched problems, dots were correct on {overall['dots_correct']} "
        f"and no-dots on {overall['no_dots_correct']} ({percent(overall['dots_accuracy'])} "
        f"versus {percent(overall['no_dots_accuracy'])}). The paired difference was "
        f"{100 * overall['accuracy_difference']:+.1f} percentage points, with a "
        f"95% paired-bootstrap interval of "
        f"[{100 * interval['accuracy_difference'][0]:+.1f}, "
        f"{100 * interval['accuracy_difference'][1]:+.1f}] points. The exact "
        f"McNemar p-value was {overall['paired_outcomes']['exact_mcnemar_p']:.3f}.",
        "",
        "This is directionally positive but not conclusive. Absolute accuracy is very "
        "low, and every nontrivial success occurs at T <= 4. There is no verified "
        "T=10 serial-computation success in the shortcut-controlled set.",
        "",
        "## By dependency length",
        "",
        "| T | Dots correct | No dots correct | Difference | Median target rank, dots | Median target rank, no dots |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for step in range(1, 11):
        summary = by_t[str(step)]
        lines.append(
            f"| {step} | {summary['dots_correct']}/10 | "
            f"{summary['no_dots_correct']}/10 | "
            f"{100 * summary['accuracy_difference']:+.0f} pp | "
            f"{summary['target_rank']['dots_median']:.1f} | "
            f"{summary['target_rank']['no_dots_median']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## Paired diagnostics",
            "",
            f"- Dots-only correct: {overall['paired_outcomes']['dots_only_correct']}.",
            f"- No-dots-only correct: {overall['paired_outcomes']['no_dots_only_correct']}.",
            f"- Correct in both: {overall['paired_outcomes']['both_correct']}.",
            f"- Incorrect in both: {overall['paired_outcomes']['neither_correct']}.",
            f"- Correct-token rank favored dots in {overall['target_rank']['dots_better']} "
            f"pairs, no-dots in {overall['target_rank']['no_dots_better']}, and tied in "
            f"{overall['target_rank']['tied']} (exact sign-test p="
            f"{overall['target_rank']['exact_sign_test_p']:.3f}).",
            f"- Median correct-token rank: {overall['target_rank']['dots_median']:.1f} "
            f"with dots versus {overall['target_rank']['no_dots_median']:.1f} without.",
            f"- Mean correct-token log-probability difference: "
            f"{overall['mean_target_log_probability']['difference']:+.3f} nats; "
            f"95% interval [{interval['mean_target_log_probability_difference'][0]:+.3f}, "
            f"{interval['mean_target_log_probability_difference'][1]:+.3f}].",
            f"- Mean reciprocal-rank difference: "
            f"{overall['mean_reciprocal_rank']['difference']:+.3f}; 95% interval "
            f"[{interval['mean_reciprocal_rank_difference'][0]:+.3f}, "
            f"{interval['mean_reciprocal_rank_difference'][1]:+.3f}].",
            "",
            "## Discordant generations",
            "",
            "| Example | T | Expected | Dots | No dots |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        if row["dots"]["correct"] == row["no_dots"]["correct"]:
            continue
        lines.append(
            f"| `{row['id']}` | {row['time_steps']} | {row['expected_answer']} | "
            f"{row['dots']['parsed_answer']} "
            f"{'✓' if row['dots']['correct'] else '✗'} | "
            f"{row['no_dots']['parsed_answer']} "
            f"{'✓' if row['no_dots']['correct'] else '✗'} |"
        )
    lines.extend(
        [
            "",
            "## Design and interpretation boundary",
            "",
            "The final set contains ten independent small-semiprime base instances at "
            "each T from 1 through 10. Within every base, the first ten residues are "
            "distinct and none equals x_0. The initial N=299, x=35 base was excluded in "
            "full because x_10=x_0 made its apparent T=10 success copy-solvable; it was "
            "replaced by N=667, x=41.",
            "",
            prompt_boundary,
            "",
            "The comparison follows the filler-paper-style convention already used in "
            "this repository: the filler condition mentions dots in the system message "
            "and places ten dots in every demonstration and target; the no-filler "
            "condition removes that clause and those dots throughout. It therefore "
            "measures the complete prompting condition, not a target-only insertion.",
            "",
            "These small moduli make all target residues single tokenizer tokens and are "
            "appropriate for this readout pilot. They are not cryptographic-size "
            "instances, so the result should not be generalized to the benchmark's "
            "strong no-shortcut setting. All generations are greedy and non-thinking.",
            "",
        ]
    )
    path.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("initial", type=Path)
    parser.add_argument("replacement", type=Path, nargs="?")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    initial = json.loads(args.initial.read_text())
    if args.replacement is None:
        rows = list(initial["examples"])
        rows.sort(key=lambda row: (int(row["time_steps"]), int(row["modulus"])))
        validate_rows(rows)
        provenance = {
            "source_file": args.initial.name,
            "combined_assertions": {
                "n": 100,
                "ten_examples_per_T": True,
                "no_final_answer_equals_x_0": True,
            },
        }
    else:
        replacement = json.loads(args.replacement.read_text())
        rows, provenance = combine(initial, replacement)
    overall = summarize(rows, intervals=True)
    by_t = {
        str(step): summarize(
            [row for row in rows if int(row["time_steps"]) == step]
        )
        for step in range(1, 11)
    }
    summary = {"overall": overall, "by_time_steps": by_t}

    args.output_dir.mkdir(parents=True, exist_ok=True)
    combined = {
        "schema_version": 2,
        "task_type": initial["task_type"],
        "filler_type": initial["filler_type"],
        "filler_length": initial["filler_length"],
        "provenance": provenance,
        "examples": rows,
        "summary": summary,
    }
    (args.output_dir / "paired_task_eval.json").write_text(
        json.dumps(combined, indent=2, ensure_ascii=False)
    )
    write_pairs_csv(args.output_dir / "pairs.csv", rows)
    summary_rows = {"overall": overall, **by_t}
    write_summary_csv(args.output_dir / "summary.csv", summary_rows)
    write_markdown(args.output_dir / "evaluation-report.md", rows, overall, by_t)
    print(json.dumps(overall, indent=2))


if __name__ == "__main__":
    main()
