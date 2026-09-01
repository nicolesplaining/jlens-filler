#!/usr/bin/env python3
"""Build a compact interactive viewer for the beyond-paper workspace probes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def behavior_series(summary: dict[str, Any], label: str) -> dict[str, Any]:
    return {
        "label": label,
        "values": [
            {
                "x": int(length),
                "accuracy": float(row["accuracy"]),
                "correct": int(row["correct"]),
                "n": int(row["n"]),
            }
            for length, row in sorted(
                summary["overall"]["by_length"].items(), key=lambda item: int(item[0])
            )
        ],
    }


def build_data(args: argparse.Namespace) -> dict[str, Any]:
    lane = read(args.lane_summary)
    workspace = read(args.workspace_summary)
    return {
        "behavior": [
            behavior_series(read(args.heldout_behavior), "100 held-out templates"),
            behavior_series(read(args.family_behavior), "48 exact-family variants"),
        ],
        "positionProfiles": [
            row
            for row in lane["readout_position_aggregate"]
            if int(row["filler_length"]) == 50
        ],
        "coordinateRecurrence": lane["readout_profile_aggregate_both_correct"],
        "workspace": workspace["aggregate"],
        "directions": workspace["directions"],
        "resonance": (
            read(args.resonance_summary) if args.resonance_summary else None
        ),
    }


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Filler workspace mechanism</title>
<style>
:root{color-scheme:light dark;--bg:#f7f7f4;--fg:#1d211f;--muted:#66706b;--line:#c9cfcb;--surface:#fff;--a:#176b87;--b:#b65d24;--good:#217a4b;--bad:#b13b3b;--soft:#e8ece9}
@media(prefers-color-scheme:dark){:root{--bg:#151816;--fg:#edf1ee;--muted:#a4ada7;--line:#454c48;--surface:#202421;--a:#68bfdc;--b:#efa36c;--good:#69ca91;--bad:#ed8383;--soft:#2c322e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:1180px;margin:auto;padding:24px}h1{font-size:24px;font-weight:600;margin:0 0 4px}h2{font-size:17px;font-weight:600;margin:0 0 12px}.sub{color:var(--muted);margin:0 0 20px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}.panel{min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px}.wide{grid-column:1/-1}.controls{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-bottom:8px}select{font:inherit;color:inherit;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:5px 8px}svg{display:block;width:100%;height:auto}.axis{stroke:var(--line);stroke-width:1}.zero{stroke:var(--muted);stroke-width:1;stroke-dasharray:4 4}.tick{fill:var(--muted);font-size:11px}.label{fill:var(--fg);font-size:12px}.legend{display:flex;gap:14px;flex-wrap:wrap;color:var(--muted);margin:8px 0 0}.swatch{display:inline-block;width:10px;height:10px;margin-right:5px;border-radius:50%}.a{background:var(--a)}.b{background:var(--b)}.metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:0 0 20px}.metric{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px}.metric strong{display:block;font-size:20px;font-weight:600}.metric span{color:var(--muted);font-size:12px}.note{color:var(--muted);font-size:12px;margin:8px 0 0}.tooltip{position:fixed;display:none;pointer-events:none;background:var(--fg);color:var(--bg);padding:6px 8px;border-radius:5px;font-size:12px;z-index:2}.heat-cell{cursor:crosshair}.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:12px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);white-space:nowrap}th{color:var(--muted);font-weight:600}@media(max-width:760px){main{padding:16px}.grid{grid-template-columns:1fr}.wide{grid-column:auto}.metrics{grid-template-columns:1fr 1fr}.panel{padding:12px}}
</style>
</head>
<body>
<main>
<h1>Filler dots behave like portable, position-biased workspace</h1>
<p class="sub">DeepSeek V4 Flash · pretrained J-Lens token readouts · raw post-block mHC residual interventions</p>
<div class="metrics" id="metrics"></div>
<div class="grid">
  <section class="panel"><h2>Dots improve the behavior gate</h2><svg id="behavior" viewBox="0 0 520 280" role="img" aria-label="Accuracy by filler length"></svg><div class="legend"><span><i class="swatch a"></i>held-out</span><span><i class="swatch b"></i>exact families</span></div></section>
  <section class="panel"><h2>Cross-length coordinate recurrence</h2><svg id="coordinates" viewBox="0 0 520 280" role="img" aria-label="Readout profile recurrence by coordinate system"></svg><p class="note">Mean Spearman ρ for examples correct at both lengths; higher means the same dot-address profile recurs.</p></section>
  <section class="panel wide"><div class="controls"><h2 style="margin:0">Where stages are readable at k=50</h2><label>Readout <select id="method"><option value="j_lens">J-Lens</option><option value="logit_lens">Logit lens</option></select></label></div><svg id="heatmap" viewBox="0 0 1040 185" role="img" aria-label="Stage by filler-position readout heatmap"></svg><p class="note">Rank-weighted target appearances across layers 24–38. This is a readout map, not a causal map.</p></section>
  <section class="panel wide"><div class="controls"><h2 style="margin:0">Move one decoded state through every destination dot</h2><label>Direction <select id="direction"></select></label></div><svg id="causal" viewBox="0 0 1040 300" role="img" aria-label="Donor and target answer effects by destination filler position"></svg><div class="legend"><span><i class="swatch a"></i>donor answer Δlog p</span><span><i class="swatch b"></i>target answer Δlog p</span></div></section>
  <section class="panel"><h2>Destination profiles recur</h2><svg id="destinations" viewBox="0 0 520 280" role="img" aria-label="Mean causal effect by destination position"></svg><p class="note">Mean donor-answer effect over six exact-layout directions.</p></section>
  <section class="panel"><h2>Neutralize selected versus random cells</h2><svg id="lesions" viewBox="0 0 520 280" role="img" aria-label="Lesion dose response"></svg><p class="note">Negative Δlog p damages the correct answer. Random controls match the selected layers.</p></section>
  <section class="panel wide" id="resonance-panel" hidden><h2>Dot-count resonance: requested versus sibling route</h2><div class="table-wrap"><table id="resonance"><thead><tr><th>Dots</th><th>Output</th><th>Correct</th><th>Answer rank</th><th>J cells: requested 235</th><th>J cells: sibling 185</th><th>J cells: product 250 / 200</th></tr></thead><tbody></tbody></table></div></section>
</div>
</main><div class="tooltip" id="tip"></div>
<script>
const DATA=__DATA__;
const NS='http://www.w3.org/2000/svg';
const css=name=>getComputedStyle(document.documentElement).getPropertyValue(name).trim();
const el=(name,attrs={},parent)=>{const n=document.createElementNS(NS,name);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);if(parent)parent.appendChild(n);return n};
const txt=(parent,x,y,value,cls='tick',anchor='middle')=>{const n=el('text',{x,y,class:cls,'text-anchor':anchor},parent);n.textContent=value;return n};
const pathFrom=pts=>pts.map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+','+p[1].toFixed(1)).join(' ');
const tip=document.getElementById('tip');
function hover(node,text){node.addEventListener('mousemove',e=>{tip.textContent=text;tip.style.display='block';tip.style.left=(e.clientX+12)+'px';tip.style.top=(e.clientY+12)+'px'});node.addEventListener('mouseleave',()=>tip.style.display='none')}
function axes(svg,w,h,m,xTicks,yTicks,xLabel,yLabel,yDomain=[0,1]){el('line',{x1:m.l,y1:h-m.b,x2:w-m.r,y2:h-m.b,class:'axis'},svg);el('line',{x1:m.l,y1:m.t,x2:m.l,y2:h-m.b,class:'axis'},svg);for(const[v,label]of xTicks){txt(svg,v,h-m.b+18,label)}for(const[v,label]of yTicks){el('line',{x1:m.l-4,y1:v,x2:w-m.r,y2:v,class:'axis',opacity:.45},svg);txt(svg,m.l-8,v+4,label,'tick','end')}txt(svg,(m.l+w-m.r)/2,h-5,xLabel,'label');const y=txt(svg,14,(m.t+h-m.b)/2,yLabel,'label');y.setAttribute('transform',`rotate(-90 14 ${(m.t+h-m.b)/2})`)}
function behavior(){const s=document.getElementById('behavior'),w=520,h=280,m={l:54,r:18,t:18,b:48},lengths=DATA.behavior[0].values.map(d=>d.x),x=i=>m.l+i*(w-m.l-m.r)/(lengths.length-1),y=v=>h-m.b-v*(h-m.t-m.b);axes(s,w,h,m,lengths.map((v,i)=>[x(i),v]),[0,.25,.5,.75,1].map(v=>[y(v),Math.round(v*100)+'%']),'filler dots','accuracy');DATA.behavior.forEach((series,si)=>{const color=css(si?'--b':'--a'),pts=series.values.map((d,i)=>[x(i),y(d.accuracy)]);el('path',{d:pathFrom(pts),fill:'none',stroke:color,'stroke-width':2.5},s);series.values.forEach((d,i)=>{const c=el('circle',{cx:x(i),cy:y(d.accuracy),r:4,fill:color},s);hover(c,`${series.label}: k=${d.x}, ${d.correct}/${d.n} (${Math.round(d.accuracy*100)}%)`)})})}
function coordinates(){const s=document.getElementById('coordinates'),w=520,h=280,m={l:62,r:18,t:18,b:66},rows=DATA.coordinateRecurrence.filter(d=>d.method==='j_lens'&&(d.stage==='answer'||d.stage==='second_product')),groups=['absolute','relative','end_relative'],labels=['absolute','proportional','from answer'],stages=['second_product','answer'],lo=Math.min(-.05,...rows.map(d=>d.mean_profile_spearman)),hi=Math.max(.25,...rows.map(d=>d.mean_profile_spearman)),x=(gi,si)=>m.l+(gi+.2+si*.34)*(w-m.l-m.r)/groups.length,y=v=>m.t+(hi-v)*(h-m.t-m.b)/(hi-lo);axes(s,w,h,m,groups.map((g,i)=>[m.l+(i+.5)*(w-m.l-m.r)/groups.length,labels[i]]),[lo,0,hi].map(v=>[y(v),v.toFixed(2)]),'dot-coordinate hypothesis','mean profile ρ',[lo,hi]);el('line',{x1:m.l,y1:y(0),x2:w-m.r,y2:y(0),class:'zero'},s);stages.forEach((stage,si)=>groups.forEach((g,gi)=>{const d=rows.find(r=>r.stage===stage&&r.alignment===g);if(!d)return;const bw=(w-m.l-m.r)/groups.length*.28;const r=el('rect',{x:x(gi,si),y:y(Math.max(0,d.mean_profile_spearman)),width:bw,height:Math.abs(y(d.mean_profile_spearman)-y(0)),fill:css(si?'--b':'--a')},s);hover(r,`${stage}, ${labels[gi]}: mean ρ ${d.mean_profile_spearman.toFixed(3)}, n=${d.n}`)}));txt(s,m.l,h-18,'blue: second product · orange: answer','tick','start')}
function heatmap(){const s=document.getElementById('heatmap'),method=document.getElementById('method').value,w=1040,h=185,m={l:118,r:15,t:18,b:34},stages=['base_value','bound_value','second_product','answer'],profiles=DATA.positionProfiles.filter(d=>d.method===method),all=profiles.flatMap(d=>d.positions.map(p=>p.mean_top10_strength)),max=Math.max(...all,1),cw=(w-m.l-m.r)/50,rh=(h-m.t-m.b)/4;s.replaceChildren();stages.forEach((stage,ri)=>{txt(s,m.l-8,m.t+(ri+.65)*rh,stage.replaceAll('_',' '),'label','end');const p=profiles.find(d=>d.stage===stage);for(let pos=1;pos<=50;pos++){const v=p.positions.find(x=>x.position===pos)?.mean_top10_strength||0;const rect=el('rect',{x:m.l+(pos-1)*cw,y:m.t+ri*rh,width:Math.max(1,cw-1),height:rh-2,fill:css('--a'),'fill-opacity':.06+.94*v/max,class:'heat-cell'},s);hover(rect,`${stage}, F${pos}: ${v.toFixed(2)} weighted top-10 layers`)}});[1,5,10,15,20,25,30,35,40,45,50].forEach(pos=>txt(s,m.l+(pos-.5)*cw,h-12,pos));txt(s,(m.l+w-m.r)/2,h-1,'filler ordinal','label')}
function causal(){const s=document.getElementById('causal'),choice=document.getElementById('direction').value,stage=choice.split('|')[0],di=+choice.split('|')[1],dir=DATA.directions[di],row=dir.cross_position.find(x=>x.stage===stage),values=row.rows,w=1040,h=300,m={l:64,r:18,t:18,b:48},all=values.flatMap(d=>[d.donor_answer.log_probability_change,d.target_answer.log_probability_change]),lo=Math.min(0,...all),hi=Math.max(0,...all),pad=(hi-lo)*.08||1,x=p=>m.l+(p-1)*(w-m.l-m.r)/49,y=v=>m.t+(hi+pad-v)*(h-m.t-m.b)/(hi-lo+2*pad);s.replaceChildren();axes(s,w,h,m,[1,5,10,15,20,25,30,35,40,45,50].map(v=>[x(v),v]),[lo,0,hi].map(v=>[y(v),v.toFixed(1)]),'destination filler ordinal','Δ log probability',[lo,hi]);el('line',{x1:m.l,y1:y(0),x2:w-m.r,y2:y(0),class:'zero'},s);[['donor_answer','--a'],['target_answer','--b']].forEach(([key,color])=>{const pts=values.map(d=>[x(d.destination_position),y(d[key].log_probability_change)]);el('path',{d:pathFrom(pts),fill:'none',stroke:css(color),'stroke-width':2},s);values.forEach(d=>{const c=el('circle',{cx:x(d.destination_position),cy:y(d[key].log_probability_change),r:2.8,fill:css(color)},s);hover(c,`${stage} · ${dir.donor_id} → ${dir.target_id} · F${d.destination_position}: ${key==='donor_answer'?'donor':'target'} Δlog p ${d[key].log_probability_change.toFixed(3)}`)})});el('line',{x1:x(row.source_position),y1:m.t,x2:x(row.source_position),y2:h-m.b,stroke:css('--good'),'stroke-width':1.5,'stroke-dasharray':'3 3'},s);txt(s,x(row.source_position),m.t+11,'source F'+row.source_position,'tick')}
function destinations(){const s=document.getElementById('destinations'),w=520,h=280,m={l:58,r:18,t:18,b:48},stages=['second_product','answer'],rows=DATA.workspace.destination_effects,all=rows.map(d=>d.mean_logp_change),lo=Math.min(0,...all),hi=Math.max(0,...all),x=p=>m.l+(p-1)*(w-m.l-m.r)/49,y=v=>m.t+(hi-v)*(h-m.t-m.b)/(hi-lo||1);axes(s,w,h,m,[1,10,20,30,40,50].map(v=>[x(v),v]),[lo,0,hi].map(v=>[y(v),v.toFixed(1)]),'destination dot','mean donor Δlog p',[lo,hi]);el('line',{x1:m.l,y1:y(0),x2:w-m.r,y2:y(0),class:'zero'},s);stages.forEach((stage,si)=>{const vals=rows.filter(d=>d.stage===stage);el('path',{d:pathFrom(vals.map(d=>[x(d.destination_position),y(d.mean_logp_change)])),fill:'none',stroke:css(si?'--b':'--a'),'stroke-width':2},s)});txt(s,m.l,h-18,'blue: second product · orange: answer','tick','start')}
function lesions(){const s=document.getElementById('lesions'),w=520,h=280,m={l:60,r:18,t:18,b:54},rows=DATA.workspace.mean_lesions.filter(d=>d.stage==='answer'),doses=[...new Set(rows.map(d=>d.dose))],all=rows.flatMap(d=>[d.median_targeted_logp_change,d.median_random_logp_change]),lo=Math.min(0,...all),hi=Math.max(0,...all),x=(d)=>m.l+doses.indexOf(d)*(w-m.l-m.r)/(doses.length-1),y=v=>m.t+(hi-v)*(h-m.t-m.b)/(hi-lo||1);axes(s,w,h,m,doses.map(d=>[x(d),d]),[lo,0,hi].map(v=>[y(v),v.toFixed(3)]),'lesioned cells (answer stage)','median Δlog p',[lo,hi]);el('line',{x1:m.l,y1:y(0),x2:w-m.r,y2:y(0),class:'zero'},s);[['median_targeted_logp_change','--a'],['median_random_logp_change','--b']].forEach(([key,color])=>{el('path',{d:pathFrom(rows.map(d=>[x(d.dose),y(d[key])])),fill:'none',stroke:css(color),'stroke-width':2.5},s);rows.forEach(d=>el('circle',{cx:x(d.dose),cy:y(d[key]),r:4,fill:css(color)},s))});txt(s,m.l,h-18,'blue: J-selected · orange: layer-matched random','tick','start')}
function metrics(){const cross=DATA.workspace.cross_position_by_stage.answer,les=DATA.workspace.mean_lesions.find(d=>d.stage==='answer'&&d.dose===16),items=[[Math.round(DATA.behavior[0].values.at(-2).accuracy*100)+'%','held-out accuracy at 50 dots'],[cross.median_fraction_positive_destinations.toFixed(2),'median positive destination fraction'],[(cross.median_pairwise_destination_profile_spearman??0).toFixed(2),'destination-profile recurrence ρ'],[(les?.median_targeted_minus_random??0).toFixed(2),'J minus random lesion Δlog p']];document.getElementById('metrics').innerHTML=items.map(([v,l])=>`<div class="metric"><strong>${v}</strong><span>${l}</span></div>`).join('')}
function resonance(){if(!DATA.resonance)return;const panel=document.getElementById('resonance-panel');panel.hidden=false;const body=document.querySelector('#resonance tbody');DATA.resonance.lengths.forEach(d=>{const tr=document.createElement('tr'),m=d.methods.j_lens;tr.innerHTML=`<td>${d.filler_length}</td><td>${d.generated_text.trim()}</td><td>${d.correct?'yes':'no'}</td><td>${d.answer_rank}</td><td>${m.answer.rank1_cells}</td><td>${m.distractor_answer.rank1_cells}</td><td>${m.second_product.rank1_cells} / ${m.distractor_second_product.rank1_cells}</td>`;body.appendChild(tr)})}
const select=document.getElementById('direction');DATA.directions.forEach((d,di)=>d.cross_position.forEach(r=>{const o=document.createElement('option');o.value=r.stage+'|'+di;o.textContent=`${r.stage.replaceAll('_',' ')} · ${d.donor_id} → ${d.target_id}`;select.appendChild(o)}));document.getElementById('method').addEventListener('change',heatmap);select.addEventListener('change',causal);metrics();behavior();coordinates();heatmap();causal();destinations();lesions();resonance();
</script>
</body></html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--heldout-behavior", type=Path, required=True)
    parser.add_argument("--family-behavior", type=Path, required=True)
    parser.add_argument("--lane-summary", type=Path, required=True)
    parser.add_argument("--workspace-summary", type=Path, required=True)
    parser.add_argument("--resonance-summary", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.dumps(build_data(args), ensure_ascii=False, separators=(",", ":"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(HTML.replace("__DATA__", data), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
