#!/usr/bin/env python3
"""Validate and summarize a paired two-fact-addition filler-length sweep."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from build_repeated_squaring_length_sweep_report import (
    condition,
    paired_summary,
    percent,
    summarize_condition,
    write_summary_csv,
)


def validate(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[int]]:
    if data["task_type"] != "addition":
        raise AssertionError(f"unexpected task type: {data['task_type']}")
    rows = data["examples"]
    lengths = [int(value) for value in data["filler_lengths"]]
    if len(rows) != 100:
        raise AssertionError(f"expected 100 examples, found {len(rows)}")
    if lengths != sorted(set(lengths)) or not lengths or lengths[0] != 0:
        raise AssertionError(f"invalid filler lengths: {lengths}")
    for row in rows:
        example = row["example"]
        if int(example["fact_value_1"]) + int(example["fact_value_2"]) != int(
            row["expected_answer"]
        ):
            raise AssertionError(f"{row['id']}: incorrect target sum")
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


def select_examples(
    rows: list[dict[str, Any]], lengths: list[int], best_length: int
) -> dict[str, list[str]]:
    baseline = 0
    dots_only = [
        row["id"]
        for row in rows
        if condition(row, best_length)["correct"]
        and not condition(row, baseline)["correct"]
    ]
    both = [
        row["id"]
        for row in rows
        if condition(row, best_length)["correct"]
        and condition(row, baseline)["correct"]
    ]
    filler_hurts = [
        row["id"]
        for row in rows
        if not condition(row, best_length)["correct"]
        and condition(row, baseline)["correct"]
    ]
    rank_improved = sorted(
        rows,
        key=lambda row: (
            condition(row, best_length)["target"]["best_rank"]
            - condition(row, baseline)["target"]["best_rank"]
        ),
    )
    return {
        "dots_only_correct": dots_only,
        "correct_in_both": both,
        "baseline_only_correct": filler_hurts,
        "largest_target_rank_improvements": [row["id"] for row in rank_improved[:10]],
    }


def write_examples_csv(
    path: Path, rows: list[dict[str, Any]], lengths: list[int]
) -> None:
    fields = [
        "id",
        "fact_phrase_1",
        "fact_value_1",
        "fact_phrase_2",
        "fact_value_2",
        "expected_answer",
    ]
    for length in lengths:
        fields.extend(
            [
                f"k{length}_answer",
                f"k{length}_correct",
                f"k{length}_target_rank",
                f"k{length}_target_log_probability",
            ]
        )
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            example = row["example"]
            output = {
                "id": row["id"],
                "fact_phrase_1": example["fact_phrase_1"],
                "fact_value_1": example["fact_value_1"],
                "fact_phrase_2": example["fact_phrase_2"],
                "fact_value_2": example["fact_value_2"],
                "expected_answer": row["expected_answer"],
            }
            for length in lengths:
                record = condition(row, length)
                output.update(
                    {
                        f"k{length}_answer": record["parsed_answer"],
                        f"k{length}_correct": record["correct"],
                        f"k{length}_target_rank": record["target"]["best_rank"],
                        f"k{length}_target_log_probability": record["target"][
                            "best_log_probability"
                        ],
                    }
                )
            writer.writerow(output)


def write_markdown(
    path: Path,
    lengths: list[int],
    summaries: dict[str, dict[str, Any]],
    comparisons: dict[str, dict[str, Any]],
    selected: dict[str, list[str]],
) -> None:
    best_length = min(
        lengths,
        key=lambda length: (-summaries[str(length)]["accuracy"], length),
    )
    baseline = summaries["0"]
    best = summaries[str(best_length)]
    lines = [
        "# Two-fact addition dot-length sweep",
        "",
        "## Result",
        "",
        f"The best observed condition was k={best_length}: "
        f"{best['correct']}/{best['n']} correct ({percent(best['accuracy'])}), versus "
        f"{baseline['correct']}/{baseline['n']} ({percent(baseline['accuracy'])}) "
        "without filler. This is an exploratory seven-condition calibration sweep; "
        "individual p-values are uncorrected.",
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
            "## Qualitative J-Lens candidates at the best k",
            "",
            f"- Dots-only correct: {len(selected['dots_only_correct'])} examples; "
            + ", ".join(f"`{value}`" for value in selected["dots_only_correct"][:10])
            + ("." if selected["dots_only_correct"] else "none."),
            f"- Correct in both: {len(selected['correct_in_both'])} examples; "
            + ", ".join(f"`{value}`" for value in selected["correct_in_both"][:10])
            + ("." if selected["correct_in_both"] else "none."),
            f"- Baseline-only correct: {len(selected['baseline_only_correct'])} examples; "
            + ", ".join(f"`{value}`" for value in selected["baseline_only_correct"][:10])
            + ("." if selected["baseline_only_correct"] else "none."),
            "",
            "## Validation and interpretation boundary",
            "",
            "The five demonstrations and first 100 target pairs are copied from the "
            "released `data/2fact_addition_dataset.json` at commit "
            "`4ba4c75d5d9f04248749ec46b8bed8661b746715`. Prompt construction uses the "
            "paper PDF's exact-count filler sentence, as requested, rather than the "
            "different wording currently present on repository main.",
            "",
            "Every k uses identical examples and greedy non-thinking decoding. The "
            "no-filler prompt is evaluated once per example, and target filler alignment "
            "is asserted at every positive length. This task is a calibration benchmark: "
            "it has known retrieved intermediates and a simple sum, but it does not test "
            "a growing serial dependency chain like repeated squaring.",
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
    best_length = min(
        lengths,
        key=lambda length: (-summaries[str(length)]["accuracy"], length),
    )
    selected = select_examples(rows, lengths, best_length)
    aggregate = {
        "schema_version": 1,
        "filler_lengths": lengths,
        "by_filler_length": summaries,
        "paired_vs_no_filler": comparisons,
        "best_observed_filler_length": best_length,
        "selected_examples": selected,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_summary_csv(
        args.output_dir / "summary.csv", lengths, summaries, comparisons
    )
    write_examples_csv(args.output_dir / "examples.csv", rows, lengths)
    (args.output_dir / "length_sweep_summary.json").write_text(
        json.dumps(aggregate, indent=2)
    )
    (args.output_dir / "selected-examples.json").write_text(
        json.dumps(selected, indent=2)
    )
    write_markdown(
        args.output_dir / "length-sweep-report.md",
        lengths,
        summaries,
        comparisons,
        selected,
    )
    print(json.dumps(aggregate["by_filler_length"], indent=2))


if __name__ == "__main__":
    main()
