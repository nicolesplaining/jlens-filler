#!/usr/bin/env python3
"""Validate and summarize a paired repeated-squaring filler-length sweep."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from pathlib import Path
from typing import Any, Callable


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
    samples = []
    for _ in range(BOOTSTRAP_SAMPLES):
        resample = [rows[rng.randrange(len(rows))] for _ in rows]
        samples.append(metric(resample))
    return percentile_interval(samples)


def condition(row: dict[str, Any], length: int) -> dict[str, Any]:
    return row["conditions"][str(length)]


def summarize_condition(rows: list[dict[str, Any]], length: int) -> dict[str, Any]:
    records = [condition(row, length) for row in rows]
    return {
        "n": len(records),
        "correct": sum(record["correct"] for record in records),
        "accuracy": sum(record["correct"] for record in records) / len(records),
        "median_target_rank": statistics.median(
            record["target"]["best_rank"] for record in records
        ),
        "mean_reciprocal_rank": statistics.mean(
            1 / record["target"]["best_rank"] for record in records
        ),
        "mean_target_log_probability": statistics.mean(
            record["target"]["best_log_probability"] for record in records
        ),
        "median_prompt_tokens": statistics.median(
            len(record["input_ids"]) for record in records
        ),
        "maximum_prompt_tokens": max(len(record["input_ids"]) for record in records),
    }


def paired_summary(rows: list[dict[str, Any]], length: int) -> dict[str, Any]:
    def accuracy_difference(items: list[dict[str, Any]]) -> float:
        return statistics.mean(
            condition(row, length)["correct"] - condition(row, 0)["correct"]
            for row in items
        )

    def reciprocal_rank_difference(items: list[dict[str, Any]]) -> float:
        return statistics.mean(
            1 / condition(row, length)["target"]["best_rank"]
            - 1 / condition(row, 0)["target"]["best_rank"]
            for row in items
        )

    def log_probability_difference(items: list[dict[str, Any]]) -> float:
        return statistics.mean(
            condition(row, length)["target"]["best_log_probability"]
            - condition(row, 0)["target"]["best_log_probability"]
            for row in items
        )

    filler_only = sum(
        condition(row, length)["correct"] and not condition(row, 0)["correct"]
        for row in rows
    )
    baseline_only = sum(
        condition(row, 0)["correct"] and not condition(row, length)["correct"]
        for row in rows
    )
    filler_better_rank = sum(
        condition(row, length)["target"]["best_rank"]
        < condition(row, 0)["target"]["best_rank"]
        for row in rows
    )
    baseline_better_rank = sum(
        condition(row, length)["target"]["best_rank"]
        > condition(row, 0)["target"]["best_rank"]
        for row in rows
    )
    return {
        "accuracy_difference": accuracy_difference(rows),
        "mean_reciprocal_rank_difference": reciprocal_rank_difference(rows),
        "mean_target_log_probability_difference": log_probability_difference(rows),
        "filler_only_correct": filler_only,
        "baseline_only_correct": baseline_only,
        "exact_mcnemar_p": exact_two_sided_binomial(
            filler_only, filler_only + baseline_only
        ),
        "filler_better_rank": filler_better_rank,
        "baseline_better_rank": baseline_better_rank,
        "rank_ties": len(rows) - filler_better_rank - baseline_better_rank,
        "exact_rank_sign_test_p": exact_two_sided_binomial(
            filler_better_rank, filler_better_rank + baseline_better_rank
        ),
        "paired_bootstrap_95_percent_intervals": {
            "accuracy_difference": bootstrap_interval(rows, accuracy_difference),
            "mean_reciprocal_rank_difference": bootstrap_interval(
                rows, reciprocal_rank_difference
            ),
            "mean_target_log_probability_difference": bootstrap_interval(
                rows, log_probability_difference
            ),
            "samples": BOOTSTRAP_SAMPLES,
            "seed": BOOTSTRAP_SEED,
        },
    }


def validate(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[int]]:
    if data["task_type"] != "repeated_squaring_mod":
        raise AssertionError(f"unexpected task type: {data['task_type']}")
    rows = data["examples"]
    lengths = [int(value) for value in data["filler_lengths"]]
    if len(rows) != 100:
        raise AssertionError(f"expected 100 examples, found {len(rows)}")
    if lengths != sorted(set(lengths)) or not lengths or lengths[0] != 0:
        raise AssertionError(f"invalid filler lengths: {lengths}")
    for step in range(1, 11):
        count = sum(int(row["example"]["time_steps"]) == step for row in rows)
        if count != 10:
            raise AssertionError(f"T={step} has {count} examples, expected 10")
    for row in rows:
        if sorted(map(int, row["conditions"])) != lengths:
            raise AssertionError(f"{row['id']}: condition grid mismatch")
        for length in lengths:
            record = condition(row, length)
            if record["filler_length"] != length:
                raise AssertionError(f"{row['id']} at k={length}: mislabeled record")
            if len(record["filler_token_indices"]) != length:
                raise AssertionError(
                    f"{row['id']} at k={length}: filler-token alignment mismatch"
                )
            prompt = record["rendered_prompt"]
            if length == 0:
                if "After the question, there will be" in prompt or "Filler:" in prompt:
                    raise AssertionError(f"{row['id']}: baseline contains filler scaffold")
            else:
                sentence = (
                    f"After the question, there will be {length} filler tokens "
                    "(a sequence of dots) before you answer."
                )
                if sentence not in prompt or prompt.count("Filler:") != 6:
                    raise AssertionError(
                        f"{row['id']} at k={length}: paper prompt mismatch"
                    )
    return rows, lengths


def write_summary_csv(
    path: Path,
    lengths: list[int],
    summaries: dict[str, dict[str, Any]],
    comparisons: dict[str, dict[str, Any]],
) -> None:
    fields = [
        "filler_length",
        "n",
        "correct",
        "accuracy",
        "accuracy_difference_vs_k0",
        "accuracy_difference_ci_low",
        "accuracy_difference_ci_high",
        "exact_mcnemar_p",
        "median_target_rank",
        "mean_reciprocal_rank",
        "mean_reciprocal_rank_difference_vs_k0",
        "mean_target_log_probability",
        "mean_target_log_probability_difference_vs_k0",
        "filler_better_rank_count",
        "baseline_better_rank_count",
        "exact_rank_sign_test_p",
        "median_prompt_tokens",
        "maximum_prompt_tokens",
    ]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for length in lengths:
            summary = summaries[str(length)]
            comparison = comparisons.get(str(length))
            interval = (
                comparison["paired_bootstrap_95_percent_intervals"][
                    "accuracy_difference"
                ]
                if comparison
                else [0.0, 0.0]
            )
            writer.writerow(
                {
                    "filler_length": length,
                    **summary,
                    "accuracy_difference_vs_k0": (
                        comparison["accuracy_difference"] if comparison else 0.0
                    ),
                    "accuracy_difference_ci_low": interval[0],
                    "accuracy_difference_ci_high": interval[1],
                    "exact_mcnemar_p": comparison["exact_mcnemar_p"] if comparison else 1.0,
                    "mean_reciprocal_rank_difference_vs_k0": (
                        comparison["mean_reciprocal_rank_difference"]
                        if comparison
                        else 0.0
                    ),
                    "mean_target_log_probability_difference_vs_k0": (
                        comparison["mean_target_log_probability_difference"]
                        if comparison
                        else 0.0
                    ),
                    "filler_better_rank_count": (
                        comparison["filler_better_rank"] if comparison else 0
                    ),
                    "baseline_better_rank_count": (
                        comparison["baseline_better_rank"] if comparison else 0
                    ),
                    "exact_rank_sign_test_p": (
                        comparison["exact_rank_sign_test_p"] if comparison else 1.0
                    ),
                }
            )


def write_by_t_csv(
    path: Path,
    rows: list[dict[str, Any]],
    lengths: list[int],
) -> dict[str, dict[str, dict[str, Any]]]:
    output: dict[str, dict[str, dict[str, Any]]] = {}
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["time_steps", "filler_length", "n", "correct", "accuracy"],
        )
        writer.writeheader()
        for step in range(1, 11):
            step_rows = [
                row for row in rows if int(row["example"]["time_steps"]) == step
            ]
            output[str(step)] = {}
            for length in lengths:
                correct = sum(condition(row, length)["correct"] for row in step_rows)
                summary = {
                    "n": len(step_rows),
                    "correct": correct,
                    "accuracy": correct / len(step_rows),
                }
                output[str(step)][str(length)] = summary
                writer.writerow(
                    {"time_steps": step, "filler_length": length, **summary}
                )
    return output


def percent(value: float) -> str:
    return f"{100 * value:.1f}%"


def write_markdown(
    path: Path,
    rows: list[dict[str, Any]],
    lengths: list[int],
    summaries: dict[str, dict[str, Any]],
    comparisons: dict[str, dict[str, Any]],
    by_t: dict[str, dict[str, dict[str, Any]]],
) -> None:
    best_length = min(
        lengths,
        key=lambda length: (-summaries[str(length)]["accuracy"], length),
    )
    baseline = summaries["0"]
    best = summaries[str(best_length)]
    lines = [
        "# Repeated-squaring dot-length sweep",
        "",
        "## Result",
        "",
        f"The best observed condition was k={best_length}: "
        f"{best['correct']}/{best['n']} correct ({percent(best['accuracy'])}), versus "
        f"{baseline['correct']}/{baseline['n']} ({percent(baseline['accuracy'])}) "
        "without filler. This is an exploratory eight-condition sweep; individual "
        "p-values are uncorrected and should not be treated as confirmatory.",
        "",
        "| Dots k | Correct | Accuracy | Difference vs k=0 | 95% paired CI | McNemar p | Median target rank | MRR | Max prompt tokens |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for length in lengths:
        summary = summaries[str(length)]
        if length:
            comparison = comparisons[str(length)]
            interval = comparison["paired_bootstrap_95_percent_intervals"][
                "accuracy_difference"
            ]
            difference = f"{100 * comparison['accuracy_difference']:+.1f} pp"
            interval_text = f"[{100 * interval[0]:+.1f}, {100 * interval[1]:+.1f}] pp"
            p_value = f"{comparison['exact_mcnemar_p']:.4f}"
        else:
            difference = "-"
            interval_text = "-"
            p_value = "-"
        lines.append(
            f"| {length} | {summary['correct']}/{summary['n']} | "
            f"{percent(summary['accuracy'])} | {difference} | {interval_text} | "
            f"{p_value} | {summary['median_target_rank']:.1f} | "
            f"{summary['mean_reciprocal_rank']:.4f} | "
            f"{summary['maximum_prompt_tokens']} |"
        )
    lines.extend(
        [
            "",
            "## Correct answers by dependency length",
            "",
            "Each cell is correct/10. Treat isolated changes cautiously because each T row "
            "contains only ten examples.",
            "",
            "| T | " + " | ".join(f"k={length}" for length in lengths) + " |",
            "|---:|" + "---:|" * len(lengths),
        ]
    )
    for step in range(1, 11):
        lines.append(
            f"| {step} | "
            + " | ".join(
                f"{by_t[str(step)][str(length)]['correct']}/10"
                for length in lengths
            )
            + " |"
        )
    filler_successes = [
        (row, length)
        for row in rows
        for length in lengths
        if length > 0 and condition(row, length)["correct"]
    ]
    maximum_successful_t = max(
        (int(row["example"]["time_steps"]) for row, _ in filler_successes),
        default=0,
    )
    highest_rows = {
        row["id"]: row
        for row, _ in filler_successes
        if int(row["example"]["time_steps"]) == maximum_successful_t
    }
    lines.extend(["", "## Highest-depth filler successes", ""])
    for row in highest_rows.values():
        successful_lengths = [
            length
            for length in lengths
            if length > 0 and condition(row, length)["correct"]
        ]
        example = row["example"]
        trace = " -> ".join(row["expected_intermediates"].values())
        lines.append(
            f"- `{row['id']}` reaches T={example['time_steps']} and is correct at "
            f"k={successful_lengths}; N={example['modulus']}, x={example['x']}, "
            f"trace {trace}."
        )
    if not highest_rows:
        lines.append("- No positive filler length produced a correct answer.")
    if maximum_successful_t < 10:
        lines.append(
            f"- No filler length solves T>{maximum_successful_t}; in particular, all "
            "T=10 conditions are incorrect."
        )
    lines.extend(
        [
            "",
            "A high-T hit is a candidate for mechanistic inspection, not evidence by "
            "itself that the model executed every modular squaring. The moduli are small, "
            "and a salient or frequently generated final residue can be correct by an "
            "alternative route or coincidence.",
        ]
    )
    lines.extend(
        [
            "",
            "## Validation and interpretation boundary",
            "",
            "Every condition uses the same 100 shortcut-controlled examples and greedy "
            "non-thinking decoding. The no-filler prompt is evaluated once per example. "
            "For each k>0, the Appendix A exact-count system sentence and k spaced dots "
            "appear in all five demonstrations and the target. Character-to-token alignment "
            "is asserted separately at every k.",
            "",
            "These are small semiprimes chosen for a tokenizer-compatible mechanistic pilot, "
            "not cryptographic-size instances. A length effect here therefore tests whether "
            "extra positions help this prompt/model combination; it does not establish the "
            "claimed no-shortcut complexity property at realistic modulus sizes.",
            "",
        ]
    )
    path.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    rows, lengths = validate(data)
    summaries = {
        str(length): summarize_condition(rows, length) for length in lengths
    }
    comparisons = {
        str(length): paired_summary(rows, length) for length in lengths if length
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_summary_csv(
        args.output_dir / "summary.csv", lengths, summaries, comparisons
    )
    by_t = write_by_t_csv(args.output_dir / "by-t.csv", rows, lengths)
    aggregate = {
        "schema_version": 1,
        "filler_lengths": lengths,
        "by_filler_length": summaries,
        "paired_vs_no_filler": comparisons,
        "by_time_steps": by_t,
    }
    (args.output_dir / "length_sweep_summary.json").write_text(
        json.dumps(aggregate, indent=2)
    )
    write_markdown(
        args.output_dir / "length-sweep-report.md",
        rows,
        lengths,
        summaries,
        comparisons,
        by_t,
    )
    print(json.dumps(aggregate["by_filler_length"], indent=2))


if __name__ == "__main__":
    main()
