#!/usr/bin/env python3
"""Aggregate selected variable-binding J/LL readouts into an algorithm report."""

from __future__ import annotations

import argparse
import html
import json
import statistics
from pathlib import Path
from typing import Any


TARGET_ORDER = [
    "base_value",
    "first_product",
    "bound_value",
    "second_product",
    "answer",
]
TARGET_LABELS = {
    "base_value": "visible base",
    "first_product": "first product",
    "bound_value": "hidden bound value",
    "second_product": "second product",
    "answer": "final answer",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def readout_metrics(result: dict[str, Any], method: str, target: str) -> dict[str, Any]:
    cells: list[dict[str, Any]] = []
    for layer_text, row in result["readouts"][method].items():
        layer = int(layer_text)
        for cell in row:
            if cell["position_kind"] != "filler":
                continue
            rank = cell["targets"][target]["best_rank"]
            if rank is None:
                continue
            cells.append(
                {
                    "rank": int(rank),
                    "layer": layer,
                    "position": int(cell["filler_ordinal"]),
                    "absolute_index": int(cell["absolute_index"]),
                }
            )
    best = min(cells, key=lambda item: (item["rank"], item["layer"], item["position"]))
    first_top10 = min(
        (cell for cell in cells if cell["rank"] <= 10),
        key=lambda item: (item["layer"], item["position"]),
        default=None,
    )
    first_rank1 = min(
        (cell for cell in cells if cell["rank"] == 1),
        key=lambda item: (item["layer"], item["position"]),
        default=None,
    )
    rank1_cells = [cell for cell in cells if cell["rank"] == 1]
    return {
        "best": best,
        "first_top10": first_top10,
        "first_rank1": first_rank1,
        "rank1_cell_count": len(rank1_cells),
        "rank1_position_median": (
            statistics.median(cell["position"] for cell in rank1_cells)
            if rank1_cells
            else None
        ),
        "rank1_unique_positions": sorted({cell["position"] for cell in rank1_cells}),
    }


def layer_rank1_fraction(
    result: dict[str, Any], method: str, target: str
) -> list[float]:
    fractions = []
    for layer in range(42):
        cells = [
            cell
            for cell in result["readouts"][method][str(layer)]
            if cell["position_kind"] == "filler"
        ]
        fractions.append(
            sum(cell["targets"][target]["best_rank"] == 1 for cell in cells)
            / len(cells)
        )
    return fractions


def summarize_result(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": result["example"]["id"],
        "filler_length": result["condition"]["filler_length"],
        "filler_answer": result["model_output"]["parsed_answer"],
        "filler_correct": result["model_output"]["correct"],
        "baseline_answer": result["no_filler_control"]["parsed_answer"],
        "baseline_correct": result["no_filler_control"]["correct"],
        "expected": result["example"]["expected_intermediates"],
        "methods": {
            method: {
                target: {
                    **readout_metrics(result, method, target),
                    "rank1_fraction_by_layer": layer_rank1_fraction(
                        result, method, target
                    ),
                }
                for target in TARGET_ORDER
            }
            for method in ("j_lens", "logit_lens")
        },
    }


def median_or_none(values: list[int | float | None]) -> float | None:
    present = [float(value) for value in values if value is not None]
    return statistics.median(present) if present else None


def aggregate_k50(examples: list[dict[str, Any]]) -> dict[str, Any]:
    aggregate: dict[str, Any] = {}
    for method in ("j_lens", "logit_lens"):
        aggregate[method] = {}
        for target in TARGET_ORDER:
            rows = [example["methods"][method][target] for example in examples]
            aggregate[method][target] = {
                "median_first_rank1_layer": median_or_none(
                    [
                        row["first_rank1"]["layer"] if row["first_rank1"] else None
                        for row in rows
                    ]
                ),
                "median_first_rank1_position": median_or_none(
                    [
                        row["first_rank1"]["position"]
                        if row["first_rank1"]
                        else None
                        for row in rows
                    ]
                ),
                "median_rank1_cell_count": median_or_none(
                    [row["rank1_cell_count"] for row in rows]
                ),
                "examples_with_rank1": sum(row["first_rank1"] is not None for row in rows),
            }
    return aggregate


def shuffled_rank1_control(
    results: list[dict[str, Any]], method: str
) -> dict[str, dict[str, int]]:
    """Compare true stage tokens with a fixed across-example derangement."""
    shifted = results[len(results) // 2 :] + results[: len(results) // 2]
    output: dict[str, dict[str, int]] = {}
    for target in TARGET_ORDER:
        actual_count = 0
        shuffled_count = 0
        for result, donor in zip(results, shifted):
            actual = str(result["example"]["expected_intermediates"][target])
            shuffled = str(donor["example"]["expected_intermediates"][target])
            for cells in result["readouts"][method].values():
                for cell in cells:
                    if cell["position_kind"] != "filler":
                        continue
                    top1 = cell["top_tokens"][0]["token"].strip()
                    actual_count += top1 == actual
                    shuffled_count += top1 == shuffled
        output[target] = {
            "actual_top1_cells": actual_count,
            "shuffled_top1_cells": shuffled_count,
        }
    return output


def build_summary(
    behavior: dict[str, Any],
    k50_results: list[dict[str, Any]],
    threshold_results: list[dict[str, Any]],
) -> dict[str, Any]:
    k50 = [summarize_result(result) for result in k50_results]
    thresholds = [summarize_result(result) for result in threshold_results]
    return {
        "behavior": behavior,
        "k50_examples": k50,
        "k50_aggregate": aggregate_k50(k50),
        "shuffled_rank1_control": {
            method: shuffled_rank1_control(k50_results, method)
            for method in ("j_lens", "logit_lens")
        },
        "threshold_examples": thresholds,
    }


def fmt(value: Any) -> str:
    return "—" if value is None else str(value)


def write_markdown(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# Variable-binding filler workspace: initial algorithmic evidence",
        "",
        "All decoded values below are **J-Lens token readouts**, not formal sparse "
        "J-space coordinates and not a transcript of hidden reasoning.",
        "",
        "## Behavioral effect",
        "",
        "| Dots | Correct / 50 | Accuracy | Helped / hurt vs no filler |",
        "|---:|---:|---:|---:|",
    ]
    behavior = summary["behavior"]["overall"]
    for length_text, row in behavior["by_length"].items():
        if length_text == "0":
            paired = "—"
        else:
            transition = behavior["paired_vs_k0"][length_text]
            paired = f"{transition['helped_count']} / {transition['hurt_count']}"
        lines.append(
            f"| {length_text} | {row['correct']} / {row['n']} | "
            f"{row['accuracy']:.2f} | {paired} |"
        )

    lines.extend(
        [
            "",
            "## Depth ladder at k=50",
            "",
            "Median first layer with an exact rank-1 token in any filler cell across "
            "the four selected examples:",
            "",
            "| Stage | J-Lens layer | Logit-lens layer | J examples with rank-1 |",
            "|---|---:|---:|---:|",
        ]
    )
    for target in TARGET_ORDER:
        j = summary["k50_aggregate"]["j_lens"][target]
        ll = summary["k50_aggregate"]["logit_lens"][target]
        lines.append(
            f"| {TARGET_LABELS[target]} | {fmt(j['median_first_rank1_layer'])} | "
            f"{fmt(ll['median_first_rank1_layer'])} | {j['examples_with_rank1']} / 4 |"
        )

    lines.extend(
        [
            "",
            "## Across-example shuffled-token control",
            "",
            "Exact top-1 filler-cell matches after a fixed two-example derangement of "
            "the tracked values:",
            "",
            "| Stage | J actual / shuffled | Logit lens actual / shuffled |",
            "|---|---:|---:|",
        ]
    )
    for target in TARGET_ORDER:
        j = summary["shuffled_rank1_control"]["j_lens"][target]
        ll = summary["shuffled_rank1_control"]["logit_lens"][target]
        lines.append(
            f"| {TARGET_LABELS[target]} | {j['actual_top1_cells']} / "
            f"{j['shuffled_top1_cells']} | {ll['actual_top1_cells']} / "
            f"{ll['shuffled_top1_cells']} |"
        )

    lines.extend(
        [
            "",
            "## Selected k=50 cases",
            "",
            "| Example | No filler | 50 dots | J-Lens first rank-1 layers "
            "(base → bound → second product → answer) |",
            "|---|---|---|---|",
        ]
    )
    for example in summary["k50_examples"]:
        metrics = example["methods"]["j_lens"]
        ladder = " → ".join(
            fmt(metrics[target]["first_rank1"]["layer"] if metrics[target]["first_rank1"] else None)
            for target in ("base_value", "bound_value", "second_product", "answer")
        )
        lines.append(
            f"| `{example['id']}` | `{example['baseline_answer']}` "
            f"({'✓' if example['baseline_correct'] else '✗'}) | "
            f"`{example['filler_answer']}` ({'✓' if example['filler_correct'] else '✗'}) | {ladder} |"
        )

    lines.extend(
        [
            "",
            "## Dot-threshold comparisons",
            "",
            "| Example | Dots | Output | J rank-1 cell counts "
            "(base / bound / second product / answer) |",
            "|---|---:|---|---:|",
        ]
    )
    threshold_rows = sorted(
        summary["threshold_examples"], key=lambda item: (item["id"], item["filler_length"])
    )
    for example in threshold_rows:
        metrics = example["methods"]["j_lens"]
        counts = " / ".join(
            str(metrics[target]["rank1_cell_count"])
            for target in ("base_value", "bound_value", "second_product", "answer")
        )
        lines.append(
            f"| `{example['id']}` | {example['filler_length']} | "
            f"`{example['filler_answer']}` ({'✓' if example['filler_correct'] else '✗'}) | {counts} |"
        )

    lines.extend(
        [
            "",
            "## Evidence-weighted interpretation",
            "",
            "1. The hidden chain is ordered primarily by **layer depth**, not by filler "
            "ordinal: base retrieval appears in the mid-20s, the hidden bound value near "
            "layer 30, the second product in the low-30s, and the answer in the mid-30s.",
            "2. The raw first product is absent as rank-1 in every selected case, while "
            "the post-add/subtract bound value is clear. The most conservative reading is "
            "that the multiply and offset are fused or represented outside a clean token "
            "direction—not that the product was never computed.",
            "3. Filler positions do not behave like a left-to-right scratchpad. Later stages "
            "often first decode at earlier filler ordinals than earlier stages, and late values "
            "are broadcast across several noncontiguous cells.",
            "4. More dots increase the number of parallel decodable copies and can move stage "
            "onsets earlier in layer depth. Since prompt-prefill positions are evaluated in "
            "parallel within each transformer layer, this is consistent with extra sequence "
            "width acting as a distributed workspace rather than extra serial transformer steps.",
            "5. Existence is not sufficiency: at 25 dots the hard example contains rank-1 "
            "readouts for every major stage but still answers incorrectly. The 50-dot boundary "
            "failure also contains the correct answer in several cells. A causal intervention is "
            "needed before claiming those cells determine the output.",
            "6. J-Lens and logit lens recover nearly the same ladder here. J-Lens sometimes "
            "advances the second-product readout by a few layers or increases its multiplicity, "
            "but the current sample does not support a broad J-Lens-superiority claim.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def viewer_html(summary: dict[str, Any]) -> str:
    payload = json.dumps(summary, ensure_ascii=False, separators=(",", ":"))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Variable-binding filler workspace</title>
<style>
:root{{color-scheme:light dark;--bg:#f7f8fb;--panel:#fff;--text:#172033;--muted:#657086;--line:#d8deea;--hot:#2563eb}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0d1220;--panel:#151c2d;--text:#edf2ff;--muted:#a8b2c7;--line:#344057;--hot:#60a5fa}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--text);font:14px/1.4 system-ui,sans-serif}}main{{max-width:1300px;margin:auto;padding:20px}}h1{{font-size:22px;margin:0 0 4px}}.sub{{color:var(--muted);margin-bottom:14px}}.controls{{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}}label{{display:grid;gap:4px;color:var(--muted)}}select{{font:inherit;padding:6px;background:var(--panel);color:var(--text);border:1px solid var(--line)}}.scroll{{overflow:auto;border:1px solid var(--line);background:var(--panel)}}.grid{{display:grid;min-width:970px;grid-template-columns:150px repeat(42,20px)}}.label,.layer{{padding:4px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}}.layer{{font-size:10px;text-align:center;color:var(--muted)}}.label{{position:sticky;left:0;background:var(--panel);z-index:1}}.cell{{height:26px;border-right:1px solid color-mix(in srgb,var(--line) 55%,transparent);border-bottom:1px solid color-mix(in srgb,var(--line) 55%,transparent)}}.legend{{margin:8px 0;color:var(--muted)}}table{{width:100%;border-collapse:collapse;margin-top:20px}}th,td{{padding:6px;border-bottom:1px solid var(--line);text-align:left}}th{{color:var(--muted)}}
</style></head><body><main><h1>Variable-binding filler workspace</h1><div class="sub">Color = fraction of filler cells where the tracked value is the exact rank-1 token. These are token readouts, not formal J-space coordinates.</div><div class="controls"><label>Readout<select id="method"><option value="j_lens">J-Lens</option><option value="logit_lens">Logit lens</option></select></label><label>Cases<select id="case"><option value="k50">Four selected k=50 examples (mean)</option></select></label></div><div class="legend">No color = 0%; strongest color = at least 35% of filler cells at that layer. Hover for the exact fraction.</div><div class="scroll"><div id="grid" class="grid"></div></div><table><thead><tr><th>Stage</th><th>Median first rank-1 layer</th><th>Examples with rank-1</th><th>Median rank-1 cells</th></tr></thead><tbody id="table"></tbody></table></main><script>
const D={payload},method=document.getElementById('method'),grid=document.getElementById('grid'),table=document.getElementById('table');
const order={json.dumps(TARGET_ORDER)},labels={json.dumps(TARGET_LABELS)};
function render(){{const m=method.value;let out='<div class="label">stage / layer</div>'+Array.from({{length:42}},(_,i)=>`<div class="layer">${{i}}</div>`).join('');for(const target of order){{const values=Array.from({{length:42}},(_,layer)=>D.k50_examples.reduce((s,e)=>s+e.methods[m][target].rank1_fraction_by_layer[layer],0)/D.k50_examples.length);out+=`<div class="label">${{labels[target]}}</div>`+values.map((v,l)=>`<div class="cell" title="${{labels[target]}}, layer ${{l}}: ${{(100*v).toFixed(1)}}% of filler cells" style="background:color-mix(in srgb,var(--hot) ${{Math.min(85,Math.round(v/.35*85))}}%,transparent)"></div>`).join('')}}grid.innerHTML=out;table.innerHTML=order.map(t=>{{const x=D.k50_aggregate[m][t];return `<tr><td>${{labels[t]}}</td><td>${{x.median_first_rank1_layer??'—'}}</td><td>${{x.examples_with_rank1}} / 4</td><td>${{x.median_rank1_cell_count??'—'}}</td></tr>`}}).join('')}}method.addEventListener('change',render);render();
</script></body></html>"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--behavior-summary", type=Path, required=True)
    parser.add_argument("--k50-dir", type=Path, required=True)
    parser.add_argument("--threshold-json", type=Path, action="append", default=[])
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    k50_results = [
        load(path)
        for path in sorted(args.k50_dir.glob("varbind_easy_*.json"))
        if path.is_file()
    ]
    if len(k50_results) != 4:
        raise ValueError(f"expected four k=50 results, found {len(k50_results)}")
    threshold_results = [load(path) for path in args.threshold_json]
    # Include the relevant k=50 members so threshold tables show all endpoints.
    threshold_results.extend(
        result
        for result in k50_results
        if result["example"]["id"] in {"varbind_easy_0035", "varbind_easy_0037"}
    )
    summary = build_summary(
        load(args.behavior_summary), k50_results, threshold_results
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "varbind-algorithm-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_markdown(summary, args.output_dir / "varbind-algorithm-report.md")
    (args.output_dir / "varbind-algorithm-viewer.html").write_text(
        viewer_html(summary), encoding="utf-8"
    )
    print(args.output_dir / "varbind-algorithm-report.md")


if __name__ == "__main__":
    main()
