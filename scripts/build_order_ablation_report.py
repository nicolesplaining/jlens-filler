#!/usr/bin/env python3
"""Summarize the matched tungsten/carbon order and three-fact runs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


DEFAULT_INPUTS = [
    Path("results/filler/tungsten_plus_carbon.json"),
    Path("results/two-fact-swapped/carbon_plus_tungsten.json"),
    Path("results/three-fact-order/tungsten_carbon_oxygen.json"),
    Path("results/three-fact-order/carbon_tungsten_oxygen.json"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="*", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument(
        "--output-prefix",
        type=Path,
        default=Path("results/order-ablation-summary"),
    )
    return parser.parse_args()


def filler_rows(result: dict[str, Any], method: str, target: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for layer, cells in result["readouts"][method].items():
        for cell in cells:
            if cell["position_kind"] != "filler":
                continue
            rank = cell["targets"][target]["best_rank"]
            if rank is not None:
                rows.append(
                    {
                        "rank": rank,
                        "layer": int(layer),
                        "filler": cell["filler_ordinal"],
                        "top1": cell["top_tokens"][0]["token"],
                    }
                )
    return rows


def summarize_target(
    result: dict[str, Any], method: str, target: str
) -> dict[str, Any]:
    rows = filler_rows(result, method, target)
    best = min(rows, key=lambda row: (row["rank"], row["layer"], row["filler"]))
    first = min(
        (row for row in rows if row["rank"] <= 10),
        key=lambda row: (row["layer"], row["filler"]),
        default=None,
    )
    return {"best": best, "first": first}


def question_order(example: dict[str, Any]) -> str:
    facts = []
    index = 1
    while f"fact_phrase_{index}" in example:
        phrase = example[f"fact_phrase_{index}"]
        facts.append(phrase.rsplit(" ", 1)[-1].lower())
        index += 1
    return " → ".join(facts)


def build_rows(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for result in results:
        example = result["example"]
        for method in ("j_lens", "logit_lens"):
            for target, surface in example["expected_intermediates"].items():
                summary = summarize_target(result, method, target)
                best, first = summary["best"], summary["first"]
                output.append(
                    {
                        "example_id": example["id"],
                        "order": question_order(example),
                        "fact_count": sum(
                            key.startswith("fact_phrase_") for key in example
                        ),
                        "filler_answer": result["model_output"]["generated_text"],
                        "filler_correct": result["model_output"]["correct"],
                        "no_filler_answer": result["no_filler_control"]["generated_text"],
                        "no_filler_correct": result["no_filler_control"]["correct"],
                        "method": method,
                        "target_label": target,
                        "target_surface": surface,
                        "best_rank": best["rank"],
                        "best_layer": best["layer"],
                        "best_filler": best["filler"],
                        "best_cell_top1": best["top1"],
                        "first_rank_le_10_layer": first["layer"] if first else None,
                        "first_rank_le_10_filler": first["filler"] if first else None,
                        "first_rank_le_10": first["rank"] if first else None,
                    }
                )
    return output


def lookup(
    rows: list[dict[str, Any]], example_id: str, method: str, surface: str
) -> dict[str, Any]:
    return next(
        row
        for row in rows
        if row["example_id"] == example_id
        and row["method"] == method
        and row["target_surface"] == surface
    )


def loc(row: dict[str, Any]) -> str:
    return f"rank {row['best_rank']} at L{row['best_layer']}/F{row['best_filler']}"


def write_markdown(
    results: list[dict[str, Any]], rows: list[dict[str, Any]], path: Path
) -> None:
    lines = [
        "# Three-fact and order-ablation results",
        "",
        "These are **J-Lens token readouts**, not formal sparse J-space coordinates. "
        "All conditions use ten dot tokens and non-thinking chat-mode encoding.",
        "",
        "## Model outcomes",
        "",
        "| Condition | Order | Filler answer | No-filler answer | Expected |",
        "|---|---|---:|---:|---:|",
    ]
    for result in results:
        example = result["example"]
        filler = result["model_output"]
        no_filler = result["no_filler_control"]
        lines.append(
            f"| `{example['id']}` | {question_order(example)} | "
            f"`{filler['generated_text']}` ({'correct' if filler['correct'] else 'wrong'}) | "
            f"`{no_filler['generated_text']}` ({'correct' if no_filler['correct'] else 'wrong'}) | "
            f"`{example['answer']}` |"
        )

    lines.extend(
        [
            "",
            "## Best direct numeric-token rank over all filler cells",
            "",
            "| Condition | Target | J-Lens | Logit lens |",
            "|---|---:|---|---|",
        ]
    )
    for result in results:
        example_id = result["example"]["id"]
        for surface in result["example"]["expected_intermediates"].values():
            j_row = lookup(rows, example_id, "j_lens", surface)
            ll_row = lookup(rows, example_id, "logit_lens", surface)
            lines.append(
                f"| `{example_id}` | `{surface}` | {loc(j_row)} | {loc(ll_row)} |"
            )

    wco_j88 = lookup(rows, "tungsten_carbon_oxygen", "j_lens", "88")
    wco_ll88 = lookup(rows, "tungsten_carbon_oxygen", "logit_lens", "88")
    wco_j80 = lookup(rows, "tungsten_carbon_oxygen", "j_lens", "80")
    wco_ll80 = lookup(rows, "tungsten_carbon_oxygen", "logit_lens", "80")
    wc_j74 = lookup(rows, "tungsten_plus_carbon", "j_lens", "74")
    cw_j74 = lookup(rows, "carbon_plus_tungsten", "j_lens", "74")
    wco_j74 = lookup(rows, "tungsten_carbon_oxygen", "j_lens", "74")
    cwo_j74 = lookup(rows, "carbon_tungsten_oxygen", "j_lens", "74")
    lines.extend(
        [
            "",
            "## Factual readout contrasts",
            "",
            f"- In `tungsten_carbon_oxygen`, the correct sum token `88` reaches "
            f"{loc(wco_j88)} with J-Lens versus {loc(wco_ll88)} with logit lens. "
            "The model nevertheless generates `106`, so decodability is not sufficient for "
            "correct final selection.",
            f"- The partial sum `80` in that same condition reaches {loc(wco_j80)} with "
            f"J-Lens versus {loc(wco_ll80)} with logit lens.",
            f"- In the two-fact swap, the strongest J-Lens `74` cell moves from "
            f"L{wc_j74['best_layer']}/F{wc_j74['best_filler']} to "
            f"L{cw_j74['best_layer']}/F{cw_j74['best_filler']}.",
            f"- In the three-fact swap, the strongest J-Lens `74` cell moves from "
            f"L{wco_j74['best_layer']}/F{wco_j74['best_filler']} to "
            f"L{cwo_j74['best_layer']}/F{cwo_j74['best_filler']}. This is an order effect in "
            "the readout location, not evidence of a fixed filler-position algorithm.",
            "",
            "Each source JSON records the exact prompt, token IDs, offsets, filler indices, "
            "top-10 readouts, target ranks, generated output, and final-block closure check.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    results = [json.loads(path.read_text(encoding="utf-8")) for path in args.inputs]
    rows = build_rows(results)
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_prefix.with_suffix(".csv")
    md_path = args.output_prefix.with_suffix(".md")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write_markdown(results, rows, md_path)
    print(md_path)
    print(csv_path)


if __name__ == "__main__":
    main()
