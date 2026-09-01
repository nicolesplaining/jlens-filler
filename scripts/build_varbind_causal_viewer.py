#!/usr/bin/env python3
"""Build a standalone interactive viewer for the varbind causal analysis."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Variable-binding filler workspace</title>
<style>
:root{color-scheme:light dark;--bg:#f7f5ef;--ink:#1d2822;--muted:#637069;--panel:#fffdf8;--line:#d7ddd7;--blue:#2774ae;--green:#21865b;--orange:#d07a22;--purple:#8455a3;--red:#c94848;--shadow:0 10px 28px rgba(32,48,39,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#111814;--ink:#eaf1ec;--muted:#a7b4ac;--panel:#17211b;--line:#34443a;--blue:#69a9dc;--green:#57c38c;--orange:#e8a354;--purple:#b48ad1;--red:#ed7777;--shadow:none}}
*{box-sizing:border-box}html,body{max-width:100%;overflow-x:hidden}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{width:min(1180px,calc(100% - 28px));max-width:100%;margin:32px auto 56px}h1{font-size:clamp(25px,4vw,42px);line-height:1.06;letter-spacing:-.035em;margin:0 0 8px;overflow-wrap:anywhere}h2{font-size:19px;margin:0 0 5px}p{margin:0;color:var(--muted)}code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:22px 0}.stat,.panel,.detail{min-width:0;background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}.stat{padding:13px 15px}.stat b{display:block;font-size:22px;font-weight:650}.stat span{color:var(--muted);font-size:12px}.panel{padding:18px;margin-top:14px}.head{display:flex;min-width:0;gap:12px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}.controls{display:flex;max-width:100%;gap:6px;align-items:center;flex-wrap:wrap}button,select{max-width:100%;font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:6px 9px}button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}button:focus-visible,select:focus-visible,.heat-cell:focus-visible{outline:3px solid color-mix(in srgb,var(--blue) 55%,transparent);outline-offset:2px}.profiles{width:100%;height:auto;display:block;margin-top:10px}.axis{stroke:var(--line);stroke-width:1}.tick{fill:var(--muted);font-size:11px}.legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:6px;color:var(--muted);font-size:12px}.swatch{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:5px}.heat-wrap{max-width:100%;overflow-x:auto;margin-top:13px;padding-bottom:5px}.heat{display:grid;grid-template-columns:40px repeat(50,15px);grid-auto-rows:20px;gap:2px;width:max-content;align-items:center}.xlab,.ylab{font-size:10px;color:var(--muted);text-align:center}.ylab{text-align:right;padding-right:5px}.heat-cell{width:15px;height:20px;border:0;border-radius:2px;padding:0;cursor:pointer;position:relative}.heat-cell[data-rank1="true"]::after{content:"";position:absolute;width:4px;height:4px;border-radius:50%;background:currentColor;left:5.5px;top:8px}.heat-cell.selected{outline:2px solid var(--ink);outline-offset:1px}.scale{display:flex;align-items:center;gap:7px;color:var(--muted);font-size:11px;margin-top:8px;flex-wrap:wrap}.gradient{height:8px;width:150px;border-radius:8px;background:linear-gradient(90deg,var(--red),color-mix(in srgb,var(--panel) 85%,var(--line)),var(--green))}.detail{margin-top:12px;padding:13px 15px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.detail b{display:block;font-size:12px;color:var(--muted);font-weight:500;margin-bottom:3px}.detail span{font-variant-numeric:tabular-nums;overflow-wrap:anywhere}.rank-table{width:100%;table-layout:fixed;border-collapse:collapse;margin-top:13px;font-size:13px}.rank-table th,.rank-table td{border-bottom:1px solid var(--line);padding:7px 8px;text-align:right;overflow-wrap:anywhere}.rank-table th:first-child,.rank-table td:first-child{text-align:left}.note{font-size:12px;margin-top:11px}.footer{margin-top:18px;color:var(--muted);font-size:12px;overflow-wrap:anywhere}.footer a{color:var(--blue)}
@media(max-width:760px){main{width:calc(100% - 16px);margin-top:18px}.stats{grid-template-columns:repeat(2,minmax(0,1fr))}.detail{grid-template-columns:repeat(2,minmax(0,1fr))}.panel{padding:13px}}
@media(max-width:480px){.stats,.detail{grid-template-columns:1fr}.controls{align-items:flex-start}.rank-table{font-size:12px}}
</style>
</head>
<body>
<main>
  <h1>Filler dots form a depth-clocked workspace</h1>
  <p>Fourteen variable-binding examples that fail without filler and succeed with 50 dots.</p>
  <section class="stats" aria-label="Key findings">
    <div class="stat"><b id="behavior-value">35 → 49</b><span id="behavior-label">correct out of 50, no filler → 50 dots</span></div>
    <div class="stat"><b id="layer-rho">—</b><span>stage ↔ layer Spearman ρ</span></div>
    <div class="stat"><b id="dot-rho">—</b><span>stage ↔ dot Spearman ρ</span></div>
    <div class="stat"><b id="hot-count">—</b><span>single cells with donor Δlog p ≥ 3</span></div>
  </section>

  <section class="panel">
    <div class="head">
      <div><h2>Stage occupancy is ordered by layer depth</h2><p>Count of exact rank-1 stage readouts across all rescued examples.</p></div>
      <div class="controls" aria-label="Readout method">
        <button type="button" class="method" data-method="j_lens" aria-pressed="true">J-Lens</button>
        <button type="button" class="method" data-method="logit_lens" aria-pressed="false">Logit lens</button>
      </div>
    </div>
    <svg class="profiles" id="profiles" viewBox="0 0 1060 280" role="img" aria-labelledby="profile-title profile-desc"><title id="profile-title">Stage readout occupancy by layer</title><desc id="profile-desc">Lines show the number of rank-one readouts for each intermediate stage across layer depth.</desc></svg>
    <div class="legend" id="legend"></div>
  </section>

  <section class="panel">
    <div class="head">
      <div><h2>Every dot × layer, patched one at a time</h2><p><code id="donor-id">donor</code> residuals transferred into matched target <code id="target-id">target</code>.</p></div>
      <div class="controls">
        <label for="mode">Color</label>
        <select id="mode">
          <option value="causal">Donor-answer Δlog p</option>
          <option value="j_lens">J-Lens target rank</option>
          <option value="logit_lens">Logit-lens target rank</option>
        </select>
        <label for="stage">Stage</label>
        <select id="stage">
          <option value="base_value">visible base</option>
          <option value="first_product">first product</option>
          <option value="bound_value">hidden bound value</option>
          <option value="second_product" selected>second product</option>
          <option value="answer">answer</option>
        </select>
      </div>
    </div>
    <div class="heat-wrap"><div class="heat" id="heat" role="grid" aria-label="Layer by filler-position causal map"></div></div>
    <div class="scale"><span id="scale-left">lower donor probability</span><div class="gradient" id="gradient"></div><span id="scale-right">higher donor probability</span><span>• exact rank 1 for selected lens/stage</span></div>
    <div class="detail" id="detail" aria-live="polite"></div>
    <table class="rank-table" aria-label="Selected cell target ranks">
      <thead><tr><th>Tracked stage</th><th>J-Lens rank</th><th>Logit-lens rank</th></tr></thead>
      <tbody id="rank-body"></tbody>
    </table>
    <p class="note">A positive patch effect means that one donor filler residual makes the donor’s counterfactual answer more likely in the target prompt. It does not isolate the displayed token direction from the rest of the residual.</p>
  </section>
  <p class="footer">These are J-Lens token readouts, not formal sparse J-space coordinates. <a id="full-readout-link" href="#">Open the complete all-layer, top-10 donor readout viewer.</a></p>
</main>
<script>
const DATA=__DATA__;
const STAGES=["base_value","bound_value","second_product","answer"];
const ALL_STAGES=["base_value","first_product","bound_value","second_product","answer"];
const LABEL={base_value:"visible base",first_product:"first product",bound_value:"hidden bound",second_product:"second product",answer:"answer"};
const COLOR={base_value:"var(--blue)",bound_value:"var(--orange)",second_product:"var(--purple)",answer:"var(--green)"};
let method="j_lens";
const geometry=DATA.geometry.methods.j_lens;
if(DATA.behavior){const by=DATA.behavior.overall.by_length;document.getElementById("behavior-value").textContent=`${by["0"].correct} → ${by["50"].correct}`;document.getElementById("behavior-label").textContent=`correct out of ${by["0"].n}, no filler → 50 dots`;}
document.getElementById("layer-rho").textContent=geometry.all_cell_stage_vs_layer_spearman.toFixed(2);
document.getElementById("dot-rho").textContent=geometry.all_cell_stage_vs_position_spearman.toFixed(2);
document.getElementById("hot-count").textContent=DATA.causal_grid.cells_improving_donor_logp_by_3;
document.getElementById("donor-id").textContent=DATA.causal_grid.donor_id;
document.getElementById("target-id").textContent=DATA.causal_grid.target_id;
const donorId=DATA.causal_grid.donor_id;
document.getElementById("full-readout-link").href=donorId.startsWith("varbind_cf_")?`../varbind-counterfactual-jlens-k50/${donorId}/viewer.html`:`../varbind-jlens-k50/${donorId}/viewer.html`;

function drawProfiles(){
  const svg=document.getElementById("profiles");
  const W=1060,H=280,m={l:48,r:18,t:18,b:36};
  const series=STAGES.map(stage=>({stage,values:DATA.geometry.methods[method].occupancy[stage].by_layer.slice(20,42)}));
  const ymax=Math.max(...series.flatMap(s=>s.values),1);
  const x=i=>m.l+i*(W-m.l-m.r)/21;
  const y=v=>H-m.b-v*(H-m.t-m.b)/ymax;
  const ticks=[0,Math.round(ymax/2),ymax];
  let html="";
  ticks.forEach(v=>{html+=`<line class="axis" x1="${m.l}" y1="${y(v)}" x2="${W-m.r}" y2="${y(v)}"/><text class="tick" x="${m.l-8}" y="${y(v)+4}" text-anchor="end">${v}</text>`});
  [20,25,30,35,41].forEach(v=>{const px=x(v-20);html+=`<text class="tick" x="${px}" y="${H-10}" text-anchor="middle">L${v}</text>`});
  series.forEach(s=>{const points=s.values.map((v,i)=>`${x(i)},${y(v)}`).join(" ");html+=`<polyline points="${points}" fill="none" stroke="${COLOR[s.stage]}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>`});
  svg.innerHTML=`<title>Stage readout occupancy by layer</title><desc>Rank-one ${method.replaceAll("_"," ")} stage readout counts across layer depth.</desc>${html}`;
  document.getElementById("legend").innerHTML=STAGES.map(s=>`<span><i class="swatch" style="background:${COLOR[s]}"></i>${LABEL[s]}</span>`).join("");
}
document.querySelectorAll("button.method").forEach(button=>button.addEventListener("click",()=>{method=button.dataset.method;document.querySelectorAll("button.method").forEach(other=>other.setAttribute("aria-pressed",String(other===button)));drawProfiles()}));

const cells=DATA.causal_grid.cells;
const byKey=new Map(cells.map(c=>[`${c.layer}:${c.position}`,c]));
const layers=[...new Set(cells.map(c=>c.layer))].sort((a,b)=>a-b);
const heat=document.getElementById("heat");
let selected=null;
function esc(value){return String(value).replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[ch]))}
function causalColor(value){const max=Math.max(...cells.map(c=>Math.abs(c.donor_log_probability_change)),.001);const strength=Math.min(Math.abs(value)/max,1);const hue=value>=0?145:3;return `hsl(${hue} 58% ${82-strength*52}%)`}
function rankColor(rank){const intensity=Math.max(0,1-Math.log10(Math.max(rank,1))/5.2);return `color-mix(in srgb, var(--blue) ${Math.round(12+intensity*80)}%, var(--panel))`}
function renderHeat(){
  const mode=document.getElementById("mode").value,stage=document.getElementById("stage").value;
  heat.innerHTML='<div></div>'+Array.from({length:50},(_,i)=>`<div class="xlab">${(i+1)%5===0?i+1:""}</div>`).join("");
  layers.forEach(layer=>{
    heat.insertAdjacentHTML("beforeend",`<div class="ylab">L${layer}</div>`);
    for(let position=1;position<=50;position++){
      const c=byKey.get(`${layer}:${position}`);const rankMethod=mode==="causal"?"j_lens":mode;const rank=c.readouts[rankMethod][stage].rank;
      const color=mode==="causal"?causalColor(c.donor_log_probability_change):rankColor(rank);
      const button=document.createElement("button");button.type="button";button.className="heat-cell";button.style.background=color;button.style.color=rank===1?"var(--ink)":"transparent";button.dataset.rank1=String(rank===1);button.setAttribute("role","gridcell");button.setAttribute("aria-label",`Layer ${layer}, dot ${position}, donor log probability change ${c.donor_log_probability_change.toFixed(2)}, ${rankMethod.replaceAll("_"," ")} ${LABEL[stage]} rank ${rank}`);button.title=button.getAttribute("aria-label");button.addEventListener("click",()=>selectCell(c,button));heat.appendChild(button);
    }
  });
  document.getElementById("gradient").style.background=mode==="causal"?"linear-gradient(90deg,var(--red),color-mix(in srgb,var(--panel) 85%,var(--line)),var(--green))":"linear-gradient(90deg,color-mix(in srgb,var(--blue) 8%,var(--panel)),var(--blue))";
  document.getElementById("scale-left").textContent=mode==="causal"?"lower donor probability":"low-ranked";
  document.getElementById("scale-right").textContent=mode==="causal"?"higher donor probability":"rank 1";
  if(selected){const match=[...heat.querySelectorAll(".heat-cell")][layers.indexOf(selected.layer)*50+selected.position-1];if(match)match.classList.add("selected")}
}
function selectCell(c,button){document.querySelectorAll(".heat-cell.selected").forEach(x=>x.classList.remove("selected"));button.classList.add("selected");selected=c;
  const j=c.readouts.j_lens._top1,l=c.readouts.logit_lens._top1;
  document.getElementById("detail").innerHTML=`<div><b>Location</b><span>layer ${c.layer}, dot ${c.position}</span></div><div><b>Causal transfer</b><span>Δlog p ${c.donor_log_probability_change>=0?"+":""}${c.donor_log_probability_change.toFixed(2)} · donor rank ${c.donor_rank}</span></div><div><b>J-Lens top-1</b><span><code>${esc(j.token)}</code> · ${(j.probability*100).toFixed(1)}%</span></div><div><b>Logit-lens top-1</b><span><code>${esc(l.token)}</code> · ${(l.probability*100).toFixed(1)}%</span></div>`;
  document.getElementById("rank-body").innerHTML=ALL_STAGES.map(s=>`<tr><td>${LABEL[s]}</td><td>${c.readouts.j_lens[s].rank}</td><td>${c.readouts.logit_lens[s].rank}</td></tr>`).join("");
}
document.getElementById("mode").addEventListener("change",renderHeat);document.getElementById("stage").addEventListener("change",renderHeat);
drawProfiles();renderHeat();
const best=[...cells].sort((a,b)=>b.donor_log_probability_change-a.donor_log_probability_change)[0];selectCell(best,[...heat.querySelectorAll(".heat-cell")][layers.indexOf(best.layer)*50+best.position-1]);
</script>
</body>
</html>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("analysis", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.analysis.read_text(encoding="utf-8"))
    encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    encoded = encoded.replace("<", "\\u003c").replace(">", "\\u003e")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(TEMPLATE.replace("__DATA__", encoded), encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
