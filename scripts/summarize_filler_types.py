#!/usr/bin/env python3
"""One table across filler types and models from analyze_dot_residuals.py and analyze_filler_cosine.py outputs.

Usage: summarize_filler_types.py --root results --models deepseek-v4-flash:chat deepseek-v4-flash-base:base
Reads <root>/<model>/dot-dump/analysis (dots) and <root>/<model>/filler-dump-<type>/{analysis,cosine}.
Columns: behavior at k=50 (from varbind-eval-<type>/behavior-summary.json when present), late-block attention
gen->filler and cue->filler, max head, same-position cross-problem cosine at 3/4 depth, variance fraction by
problem, answer probe R^2 from filler mean / q_last / cue, centered adjacent cosine at 3/4 depth, change points
per item, filler->gen centered cosine at its peak layer (first 5 vs last 5 filler positions).
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

DOT_REGION = 3


def load(p: Path, label: str = ""):
    d = json.loads(p.read_text())
    if isinstance(d, list):
        for r in d:
            rl = str(r.get("label", ""))
            if label and (label in rl or rl == label.split("-", 1)[-1] or rl == label): return r
        return d[0]
    return d


def anatomy_row(a: dict) -> dict:
    att = a["attention"]; L = a["n_layers"]; layers = sorted(int(k) for k in att); last = layers[len(layers) - len(layers) // 3:]
    g = sum(att[str(l)]["gen_by_region"][DOT_REGION] for l in last) / len(last)
    c = sum(att[str(l)]["cue_by_region"][DOT_REGION] for l in last) / len(last)
    mh = max(att[str(l)]["max_head_gen_dot_mass"] for l in layers if l >= 20) if any(l >= 20 for l in layers) else max(att[str(l)]["max_head_gen_dot_mass"] for l in layers)
    pi = a["problem_independence"]; q = 3 * L // 4
    row_q = next((r for r in pi if r.get("layer") == q), pi[min(q, len(pi) - 1)])
    cos_same = row_q.get("cos_same_pos_across_problems", float("nan")); vf = row_q.get("frac_var_problem", float("nan"))
    pr = a["probes"]
    def best(pos, tgt):
        v = pr.get(pos, {}).get(tgt); return max(v) if isinstance(v, list) else float("nan")
    return {"gen->filler": g, "cue->filler": c, "max head (L>=20)": mh, "cos same pos": cos_same, "var by problem": vf,
            "R2 ans|filler": best("dots_mean", "answer"), "R2 ans|q_last": best("q_last", "answer"), "R2 ans|cue": best("cue", "answer")}


def cosine_row(c: dict) -> dict:
    L = c["n_layers"]; K = c["n_filler"]; q = 3 * L // 4
    adj = c["centered_adjacent_per_layer_mean"][q]; adj_mid = sum(adj[2:-2]) / max(1, len(adj) - 4)
    raw = c["adjacent_per_layer_mean"][q]; raw_mid = sum(raw[2:-2]) / max(1, len(raw) - 4)
    M = c.get("centered_cos_filler_to_gen_per_layer")
    if M:
        means = [sum(r) / K for r in M]; lpk = max(range(L), key=lambda l: means[l]); row = M[lpk]
        first, lastp = sum(row[:5]) / 5, sum(row[-5:]) / 5
    else:
        lpk, first, lastp = -1, float("nan"), float("nan")
    return {"n filler tok": K, "raw adj (3/4)": raw_mid, "centered adj (3/4)": adj_mid, "changepts/item": c["centered_changepoint_mean_count"],
            "filler->gen peak L": lpk, "f->gen first5": first, "f->gen last5": lastp}


def behavior(p: Path) -> str:
    if not p.exists(): return ""
    s = json.loads(p.read_text())
    rows = s.get("rows") or s.get("conditions") or s
    try:
        for r in rows:
            if int(r.get("filler_length", r.get("k", -1))) == 50: return str(r.get("correct", r.get("n_correct", "")))
    except Exception:
        return ""
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", type=Path, default=Path("results"))
    ap.add_argument("--models", nargs="+", default=["deepseek-v4-flash:chat", "deepseek-v4-flash-base:base"])
    ap.add_argument("--types", nargs="+", default=["dots", "alphabet", "alphabet-scrambled", "counting", "counting-scrambled"])
    ap.add_argument("--output", type=Path, default=None)
    a = ap.parse_args()
    rows = []
    for spec in a.models:
        mdir, label = spec.split(":")
        for ft in a.types:
            d = a.root / mdir / ("dot-dump" if ft == "dots" else f"filler-dump-{ft}")
            if ft == "dots" and not (d / "analysis").exists() and (a.root / mdir).parent.name == "filler-types":
                d = (a.root / mdir).parent.parent / "dot-dump"
            an = d / "analysis" / "dot-analysis.json"; co = d / "cosine" / "filler-cosine.json"
            if ft == "dots" and not co.exists():
                for alt in (a.root / "filler-cosine" / "dots" / "filler-cosine.json", a.root / "filler-cosine" / "qwen-dots" / "filler-cosine.json"):
                    if alt.exists():
                        for r in json.loads(alt.read_text()):
                            if r["label"] == f"{label}-dots" or r["label"].startswith(label): co = None; cdata = r; break
                    if co is None: break
            if not an.exists(): continue
            row = {"model": label, "filler": ft}
            row.update(anatomy_row(load(an, label)))
            if co is None: row.update(cosine_row(cdata))
            elif co.exists(): row.update(cosine_row(load(co, label)))
            rows.append(row)
    if not rows: print("no analysis outputs found"); return
    cols = [k for k in rows[0] if k not in ("model", "filler")]
    hdr = "| model | filler | " + " | ".join(cols) + " |"; sep = "|---|---|" + "|".join(["---:"] * len(cols)) + "|"
    lines = [hdr, sep]
    for r in rows:
        lines.append(f"| {r['model']} | {r['filler']} | " + " | ".join(f"{r.get(c, float('nan')):.3f}" if isinstance(r.get(c), float) else str(r.get(c, "")) for c in cols) + " |")
    out = "\n".join(lines); print(out)
    if a.output: a.output.write_text(out + "\n")


if __name__ == "__main__":
    main()
