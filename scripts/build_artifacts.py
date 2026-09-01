#!/usr/bin/env python3
"""Build compact reports and a standalone interactive viewer from extraction JSON."""

from __future__ import annotations

import argparse
import html
import json
import math
from pathlib import Path
from typing import Any


REPORT_LAYERS = [0, 10, 20, 30, 35, 36, 37, 38, 39, 40, 41]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def best_variant(target: dict[str, Any]) -> dict[str, Any] | None:
    ranked = [variant for variant in target["variants"] if "rank" in variant]
    return min(ranked, key=lambda item: item["rank"], default=None)


def compact_viewer_data(result: dict[str, Any]) -> dict[str, Any]:
    methods: dict[str, Any] = {}
    for method in ("j_lens", "logit_lens"):
        method_layers: dict[str, Any] = {}
        for layer, cells in result["readouts"][method].items():
            compact_cells = []
            for cell in cells:
                targets = {}
                for label, target in cell["targets"].items():
                    variant = best_variant(target)
                    targets[label] = {
                        "rank": target["best_rank"],
                        "probability": variant.get("probability") if variant else None,
                        "logit": variant.get("logit") if variant else None,
                        "surface": variant.get("surface") if variant else None,
                    }
                compact_cells.append(
                    {
                        "top": [
                            [
                                token["token"],
                                round(token["probability"], 8),
                                round(token["logit"], 5),
                                token["token_id"],
                            ]
                            for token in cell["top_tokens"]
                        ],
                        "targets": targets,
                    }
                )
            method_layers[layer] = compact_cells
        methods[method] = method_layers
    return {
        "title": result["example"]["id"],
        "columns": result["selected_columns"],
        "expected": result["example"]["expected_intermediates"],
        "highlightForms": result["example"].get("highlight_forms", {}),
        "actualFinal": {
            "block": 42,
            "generatedText": result["model_output"]["generated_text"],
            "top": [
                [
                    token["token"],
                    round(token["probability"], 8),
                    round(token["logit"], 5),
                    token["token_id"],
                ]
                for token in result["model_output"]["actual_prompt_logits"][
                    "top_tokens"
                ]
            ],
        },
        "methods": methods,
    }


def write_jsonl(result: dict[str, Any], path: Path) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for method in ("j_lens", "logit_lens"):
            for layer, cells in result["readouts"][method].items():
                for cell in cells:
                    record = {
                        "example_id": result["example"]["id"],
                        "method": method,
                        "layer": int(layer),
                        "position_kind": cell["position_kind"],
                        "filler_ordinal": cell.get("filler_ordinal"),
                        "absolute_index": cell["absolute_index"],
                        "surface": cell["surface"],
                        "top_tokens": cell["top_tokens"],
                        "targets": cell["targets"],
                    }
                    handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def rank_summary(result: dict[str, Any], method: str, target: str) -> dict[str, Any]:
    rows = []
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
                        "position": cell["filler_ordinal"],
                        "top1": cell["top_tokens"][0]["token"],
                    }
                )
    best = min(rows, key=lambda row: (row["rank"], row["layer"], row["position"]))
    threshold = min(
        (row for row in rows if row["rank"] <= 10),
        key=lambda row: (row["layer"], row["position"]),
        default=None,
    )
    return {"best": best, "first_at_10": threshold}


def token_list(cell: dict[str, Any], count: int = 5) -> str:
    return ", ".join(f"`{item['token'].replace(chr(10), '↵')}`" for item in cell["top_tokens"][:count])


def write_markdown_report(result: dict[str, Any], path: Path) -> None:
    expected = result["example"]["expected_intermediates"]
    lines = [
        "# First qualitative filler readout",
        "",
        "These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.",
        "",
        "## Outcome",
        "",
        f"- Filler answer: `{result['model_output']['generated_text']}` "
        f"({'correct' if result['model_output']['correct'] else 'incorrect'}).",
        f"- No-filler answer: `{result['no_filler_control']['generated_text']}` "
        f"({'correct' if result['no_filler_control']['correct'] else 'incorrect'}).",
        f"- Filler tokens: {len(result['alignment']['filler_token_indices'])} tokens at absolute indices "
        f"{result['alignment']['filler_token_indices'][0]}–{result['alignment']['filler_token_indices'][-1]}.",
        f"- Final-head closure max absolute logit error: "
        f"`{result['compatibility_checks']['layer_42_final_head_closure_max_abs_error']}`.",
        "",
        "## Direct target-rank summary over filler cells",
        "",
        "| Readout | Target | Best filler-cell rank | First rank ≤ 10 |",
        "|---|---|---:|---|",
    ]
    for method, method_label in (("j_lens", "J-Lens"), ("logit_lens", "Logit lens")):
        for target, surface in expected.items():
            summary = rank_summary(result, method, target)
            best = summary["best"]
            first = summary["first_at_10"]
            first_text = (
                f"L{first['layer']}, filler {first['position']} (rank {first['rank']})"
                if first
                else "Never"
            )
            lines.append(
                f"| {method_label} | `{target}={surface}` | {best['rank']} "
                f"(L{best['layer']}, filler {best['position']}) | {first_text} |"
            )

    lines.extend(["", "## J-Lens top-5 by filler position", ""])
    available = set(map(int, result["readouts"]["j_lens"]))
    layers = [layer for layer in REPORT_LAYERS if layer in available]
    for column_index, column in enumerate(result["selected_columns"]):
        if column["position_kind"] != "filler":
            continue
        lines.extend(
            [
                f"### Filler position {column['filler_ordinal']} "
                f"(absolute token {column['absolute_index']}, surface "
                f"`{column['surface'].replace(chr(10), '↵')}`)",
                "",
            ]
        )
        for layer in layers:
            cell = result["readouts"]["j_lens"][str(layer)][column_index]
            target_ranks = ", ".join(
                f"{label}={expected[label]}:{cell['targets'][label]['best_rank']}"
                for label in expected
            )
            lines.append(
                f"- Layer {layer}: {token_list(cell)} (target ranks: {target_ranks})"
            )
        lines.append("")

    lines.extend(
        [
            "## Exact rendered prompt",
            "",
            "```text",
            result["rendered_prompt"],
            "```",
            "",
            "## Interpretation boundary",
            "",
            "A high-ranked token is evidence about a token direction produced by average-Jacobian "
            "transport and the model's norm/unembedding. It is not a literal transcript of a "
            "private chain of thought. The square released lens also omits an explicit convention "
            "for reducing V4's four hyper-connection streams; see `compatibility.md`.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_viewer_html(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    title = html.escape(data["title"].replace("_", " ").title())
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — J-Lens filler readouts</title>
<style>
:root {{ color-scheme: light dark; --bg:#f7f8fb; --panel:#fff; --text:#172033; --muted:#657086; --line:#d8deea; --hot:#f59e0b; --j:#2563eb; --ll:#7c3aed; --target1:#0f9d74; --target2:#d97706; --target3:#dc2626; --target4:#2563eb; --target5:#7c3aed; --target6:#0891b2; --actual:#dc2626; }}
@media (prefers-color-scheme:dark) {{ :root {{ --bg:#0d1220; --panel:#151c2d; --text:#edf2ff; --muted:#a8b2c7; --line:#344057; --hot:#fbbf24; --j:#60a5fa; --ll:#c4b5fd; --target1:#34d399; --target2:#fbbf24; --target3:#fb7185; --target4:#60a5fa; --target5:#c4b5fd; --target6:#22d3ee; --actual:#fb7185; }} }}
* {{ box-sizing:border-box }} body {{ margin:0; background:var(--bg); color:var(--text); font:14px/1.4 system-ui,sans-serif }}
main {{ max-width:1600px; margin:auto; padding:20px }} h1 {{ margin:0 0 4px; font-size:22px }} h2 {{ margin:28px 0 8px; font-size:17px }}
.sub {{ color:var(--muted); margin-bottom:16px }} .controls {{ display:flex; flex-wrap:wrap; gap:12px; align-items:end; margin:12px 0 }} label {{ display:grid; gap:4px; color:var(--muted) }} select {{ font:inherit; padding:7px 9px; color:var(--text); background:var(--panel); border:1px solid var(--line); border-radius:6px }}
.legend {{ display:flex; flex-wrap:wrap; gap:12px; color:var(--muted); margin:8px 0 }} .dot {{ display:inline-block; width:10px; height:10px; border-radius:2px; margin-right:4px }}
.scroll {{ overflow:auto; border:1px solid var(--line); background:var(--panel) }} .matrix {{ display:grid }}
.head,.layer {{ position:sticky; z-index:2; background:var(--panel); border-bottom:1px solid var(--line); padding:6px; font-weight:600 }} .head {{ top:0; text-align:center }} .layer {{ left:0; z-index:1; border-right:1px solid var(--line) }}
.cell {{ min-height:44px; padding:5px; border:0; border-right:1px solid var(--line); border-bottom:1px solid var(--line); background:transparent; color:var(--text); font:inherit; cursor:pointer; overflow-wrap:anywhere }} .cell:hover,.cell:focus {{ outline:2px solid var(--j); outline-offset:-2px }} .cell.hit0 {{ background:color-mix(in srgb,var(--target1) 20%,transparent) }} .cell.hit1 {{ background:color-mix(in srgb,var(--target2) 20%,transparent) }} .cell.hit2 {{ background:color-mix(in srgb,var(--target3) 20%,transparent) }} .cell.hit3 {{ background:color-mix(in srgb,var(--target4) 20%,transparent) }} .cell.hit4 {{ background:color-mix(in srgb,var(--target5) 20%,transparent) }} .cell.hit5 {{ background:color-mix(in srgb,var(--target6) 20%,transparent) }} .cell.unavailable {{ cursor:default; color:var(--muted); border-top:3px solid var(--line) }} .cell.actual {{ border-top:3px solid var(--actual); background:color-mix(in srgb,var(--actual) 24%,transparent); font-weight:600 }} .layer.actual-layer {{ border-top:3px solid var(--actual); color:var(--actual) }}
.detail {{ margin-top:10px; padding:12px; background:var(--panel); border:1px solid var(--line) }} .detail h3 {{ margin:0 0 8px; font-size:15px }} table {{ width:100%; border-collapse:collapse }} th,td {{ text-align:left; border-bottom:1px solid var(--line); padding:5px }} th {{ color:var(--muted); font-weight:600 }} .num {{ text-align:right; font-variant-numeric:tabular-nums }}
.target {{ margin-top:24px }} .target-head {{ display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px; align-items:baseline }} .summary {{ color:var(--muted) }}
.heat {{ overflow:auto; border:1px solid var(--line); background:var(--panel) }} .heat-grid {{ display:grid }} .heat-label,.heat-head {{ padding:3px 5px; color:var(--muted); border-bottom:1px solid var(--line) }} .heat-cell {{ min-height:22px; border:0; border-right:1px solid var(--line); border-bottom:1px solid var(--line); color:var(--text); font:12px system-ui; cursor:pointer }}
.chart {{ margin-top:8px; border:1px solid var(--line); background:var(--panel); padding:6px }} svg {{ display:block; width:100%; height:170px }} .axis {{ stroke:var(--line); stroke-width:1 }} .axistext {{ fill:var(--muted); font-size:11px }} .path {{ fill:none; stroke-width:2 }}
@media(max-width:700px) {{ main {{ padding:12px }} .detail {{ overflow:auto }} }}
</style>
</head>
<body>
<main>
<h1>{title}: filler-token readouts</h1>
<div class="sub">Layers 0–41 are intermediate lens readouts. The separately marked final row is the model's actual output after block 42. Select a populated cell for its top-10.</div>
<div class="controls">
<label>Readout<select id="method"><option value="j_lens">J-Lens</option><option value="logit_lens">Logit lens</option></select></label>
<label>Layers<select id="layers"><option value="sampled">22 sampled layers</option><option value="all">All 42 layers</option></select></label>
</div>
<div id="legend" class="legend"></div>
<div class="scroll"><div id="matrix" class="matrix" aria-label="Layer by filler-position token readout grid"></div></div>
<section id="detail" class="detail" aria-live="polite"></section>
<h2>Tracked intermediate ranks</h2>
<div id="targets"></div>
</main>
<script>
const DATA={payload};
const methodEl=document.getElementById('method'), layersEl=document.getElementById('layers'), matrixEl=document.getElementById('matrix'), detailEl=document.getElementById('detail'), targetsEl=document.getElementById('targets'), legendEl=document.getElementById('legend');
const labels=Object.keys(DATA.expected), colors=['var(--target1)','var(--target2)','var(--target3)','var(--target4)','var(--target5)','var(--target6)','var(--target1)','var(--target2)','var(--target3)','var(--target4)','var(--target5)','var(--target6)'];
function esc(x){{return String(x).replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function shownLayers(){{const all=Object.keys(DATA.methods[methodEl.value]).map(Number).sort((a,b)=>a-b);return layersEl.value==='all'?all:all.filter(x=>x%2===0||x===41)}}
function colLabel(c){{const surface=esc(c.surface).replace(/\\n/g,'↵');if(c.position_kind==='filler')return `F${{c.filler_ordinal}}<br><code>${{surface}}</code><br><small>#${{c.absolute_index}}</small>`;if(c.position_kind==='answer_cue')return `Answer cue<br><code>${{surface}}</code><br><small>#${{c.absolute_index}}</small>`;return `Predict<br><code>${{surface}}</code><br><small>#${{c.absolute_index}}</small>`}}
function targetColor(i){{return colors[i%6]}}
function renderLegend(){{legendEl.innerHTML=labels.map((k,i)=>`<span><i class="dot" style="background:${{targetColor(i)}}"></i><code>${{esc(k)}}=${{esc(DATA.expected[k])}}</code> rank ≤10 or highlighted surface form</span>`).join('')+`<span><i class="dot" style="background:var(--actual)"></i>actual model row</span>`}}
function hitClass(cell){{const top=cell.top[0][0].trim().toLowerCase();for(let i=0;i<labels.length;i++){{const r=cell.targets[labels[i]].rank,forms=(DATA.highlightForms[labels[i]]||[]).map(x=>x.trim().toLowerCase());if((r!==null&&r<=10)||forms.includes(top))return `hit${{i%6}}`}}return ''}}
function selectCell(layer,index){{const c=DATA.columns[index],cell=DATA.methods[methodEl.value][layer][index];let rows=cell.top.map((t,i)=>`<tr><td>${{i+1}}</td><td><code>${{esc(t[0]).replace(/\\n/g,'↵')}}</code></td><td class="num">${{t[3]}}</td><td class="num">${{t[1].toExponential(3)}}</td><td class="num">${{t[2].toFixed(3)}}</td></tr>`).join('');let ranks=labels.map((k,i)=>`<span style="color:${{colors[i]}}"><code>${{esc(DATA.expected[k])}}</code> rank ${{cell.targets[k].rank??'n/a'}}</span>`).join(' · ');detailEl.innerHTML=`<h3>${{methodEl.options[methodEl.selectedIndex].text}}, layer ${{layer}}, ${{c.position_kind.replace('_',' ')}} ${{c.filler_ordinal??''}} (token #${{c.absolute_index}}, <code>${{esc(c.surface).replace(/\\n/g,'↵')}}</code>)</h3><div class="summary">${{ranks}}</div><table><thead><tr><th>Rank</th><th>Token</th><th class="num">ID</th><th class="num">Probability</th><th class="num">Logit</th></tr></thead><tbody>${{rows}}</tbody></table>`}}
function selectActual(){{const top=DATA.actualFinal.top,position=DATA.columns.find(c=>c.position_kind==='answer_prediction');const rows=top.map((t,i)=>`<tr><td>${{i+1}}</td><td><code>${{esc(t[0]).replace(/\\n/g,'↵')}}</code></td><td class="num">${{t[3]}}</td><td class="num">${{t[1].toExponential(3)}}</td><td class="num">${{t[2].toFixed(3)}}</td></tr>`).join('');detailEl.innerHTML=`<h3>Actual model logits after block ${{DATA.actualFinal.block}} at the generation position (token #${{position.absolute_index}})</h3><div class="summary">Generated answer: <strong><code>${{esc(DATA.actualFinal.generatedText)}}</code></strong>. This is the final model output, not a lens readout.</div><table><thead><tr><th>Rank</th><th>Token</th><th class="num">ID</th><th class="num">Probability</th><th class="num">Logit</th></tr></thead><tbody>${{rows}}</tbody></table>`}}
function renderMatrix(){{const layers=shownLayers(),predictionIndex=DATA.columns.findIndex(c=>c.position_kind==='answer_prediction');matrixEl.style.minWidth=`${{68+DATA.columns.length*78}}px`;matrixEl.style.gridTemplateColumns=`68px repeat(${{DATA.columns.length}},minmax(78px,1fr))`;let out='<div class="head">Layer</div>'+DATA.columns.map(c=>`<div class="head">${{colLabel(c)}}</div>`).join('');for(const l of layers){{out+=`<div class="layer">L${{l}}</div>`;DATA.methods[methodEl.value][l].forEach((cell,i)=>{{const tok=esc(cell.top[0][0]).replace(/\\n/g,'↵');const ranks=labels.map(k=>`${{DATA.expected[k]}} rank ${{cell.targets[k].rank??'n/a'}}`).join(', ');out+=`<button class="cell ${{hitClass(cell)}}" data-layer="${{l}}" data-col="${{i}}" aria-label="Layer ${{l}}, ${{DATA.columns[i].position_kind}}, top token ${{tok}}; ${{ranks}}"><code>${{tok}}</code></button>`}})}}out+='<div class="layer actual-layer">Actual L42</div>';DATA.columns.forEach((c,i)=>{{if(i===predictionIndex){{const tok=esc(DATA.actualFinal.top[0][0]).replace(/\\n/g,'↵');out+=`<button id="actual-final-cell" class="cell actual" aria-label="Actual model logits after block 42, top token ${{tok}}"><code>${{tok}}</code></button>`}}else{{out+='<div class="cell unavailable" aria-label="Actual final logits were only recorded at the generation position">—</div>'}}}});matrixEl.innerHTML=out;matrixEl.querySelectorAll('button.cell[data-layer]').forEach(b=>b.addEventListener('click',()=>selectCell(b.dataset.layer,Number(b.dataset.col))));document.getElementById('actual-final-cell').addEventListener('click',selectActual);selectActual();renderTargets()}}
function rankStrength(r){{if(r===null)return 0;return Math.max(.04,1-Math.log10(Math.max(1,r))/4)}}
function renderTargets(){{const layers=shownLayers(),method=DATA.methods[methodEl.value],fillers=DATA.columns.map((c,i)=>({{c,i}})).filter(x=>x.c.position_kind==='filler');let out='';labels.forEach((key,ki)=>{{let pts=[],best=null,first=null;layers.forEach(l=>{{const row=fillers.map(x=>({{r:method[l][x.i].targets[key].rank,p:x.c.filler_ordinal,i:x.i}}));let min=Math.min(...row.map(x=>x.r).filter(r=>r!==null));if(!Number.isFinite(min))min=129280;pts.push([l,min]);row.forEach(x=>{{if(x.r!==null&&(!best||x.r<best.r))best={{r:x.r,l,p:x.p,i:x.i}};if(x.r!==null&&x.r<=10&&(!first||l<first.l||(l===first.l&&x.p<first.p)))first={{r:x.r,l,p:x.p,i:x.i}}}})}});let heat='<div class="heat-label">L/P</div>'+fillers.map(x=>`<div class="heat-head">F${{x.c.filler_ordinal}}</div>`).join('');layers.forEach(l=>{{heat+=`<div class="heat-label">${{l}}</div>`;fillers.forEach(x=>{{const r=method[l][x.i].targets[key].rank,s=rankStrength(r);heat+=`<button class="heat-cell" style="background:color-mix(in srgb,${{colors[ki]}} ${{Math.round(s*72)}}%,transparent)" data-l="${{l}}" data-p="${{x.i}}" aria-label="Layer ${{l}}, filler ${{x.c.filler_ordinal}}, target rank ${{r??'n/a'}}">${{r===null?'':r}}</button>`}})}});const W=900,H=150,pad={{l:48,r:15,t:12,b:28}},x=l=>pad.l+(l-layers[0])/(layers[layers.length-1]-layers[0])*(W-pad.l-pad.r),y=r=>pad.t+Math.log10(Math.max(1,Math.min(1000,r)))/3*(H-pad.t-pad.b);const path=pts.map((p,i)=>`${{i?'L':'M'}}${{x(p[0]).toFixed(1)}},${{y(p[1]).toFixed(1)}}`).join(' ');const summary=`Best rank ${{best?.r??'n/a'}} at L${{best?.l??'–'}} / F${{best?.p??'–'}}; first rank ≤10: ${{first?`L${{first.l}} / F${{first.p}} (rank ${{first.r}})`:'never'}}`;const gridStyle=`min-width:${{54+fillers.length*54}}px;grid-template-columns:54px repeat(${{fillers.length}},minmax(54px,1fr))`;out+=`<section class="target"><div class="target-head"><h3><code>${{esc(key)}}=${{esc(DATA.expected[key])}}</code></h3><span class="summary">${{summary}}</span></div><div class="heat"><div class="heat-grid" style="${{gridStyle}}">${{heat}}</div></div><div class="chart"><svg viewBox="0 0 ${{W}} ${{H}}" role="img" aria-label="Minimum filler-position rank trajectory for ${{esc(DATA.expected[key])}}"><line class="axis" x1="${{pad.l}}" y1="${{H-pad.b}}" x2="${{W-pad.r}}" y2="${{H-pad.b}}"/><line class="axis" x1="${{pad.l}}" y1="${{pad.t}}" x2="${{pad.l}}" y2="${{H-pad.b}}"/><text class="axistext" x="8" y="18">rank 1</text><text class="axistext" x="3" y="${{y(10)+4}}">rank 10</text><text class="axistext" x="0" y="${{y(1000)+4}}">rank 1000</text><text class="axistext" x="${{pad.l}}" y="${{H-7}}">layer ${{layers[0]}}</text><text class="axistext" text-anchor="end" x="${{W-pad.r}}" y="${{H-7}}">layer ${{layers[layers.length-1]}}</text><path class="path" stroke="${{colors[ki]}}" d="${{path}}"/></svg></div></section>`}});targetsEl.innerHTML=out;targetsEl.querySelectorAll('.heat-cell').forEach(b=>b.addEventListener('click',()=>selectCell(b.dataset.l,Number(b.dataset.p))))}}
methodEl.addEventListener('change',renderMatrix);layersEl.addEventListener('change',renderMatrix);renderLegend();renderMatrix();
</script>
</body>
</html>
"""


def main() -> None:
    args = parse_args()
    result = json.loads(args.input.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    compact = compact_viewer_data(result)
    (args.output_dir / "viewer.html").write_text(
        build_viewer_html(compact), encoding="utf-8"
    )
    write_jsonl(result, args.output_dir / "readouts.jsonl")
    write_markdown_report(result, args.output_dir / "qualitative-report.md")
    print(args.output_dir / "viewer.html")


if __name__ == "__main__":
    main()
