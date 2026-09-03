#!/usr/bin/env python3
"""Four analyses over ``dump_dot_residuals_hf.py`` output, for one or more models.

1. Problem-independence of dot residuals: variance of dot residuals split into
   position identity vs problem identity, and same-position cross-problem cosine.
2. Linear probes: ridge regression from residuals to stage values (item-level
   5-fold CV R^2), at dots (mean-pooled and per-dot pooled), q_last, cue, gen;
   shuffled-label control.
3. Attention: mass from the answer positions and from dots onto prompt regions,
   per full-attention layer, mean over items and heads; heads with most dot mass.
4. Processing trajectories: residual norm and lens entropy by layer for dots vs
   content positions.
Writes a markdown report and a JSON of the numbers.
"""

from __future__ import annotations

import argparse
import json
import statistics as st
from pathlib import Path

import numpy as np
import torch


def ridge_cv_r2(X: np.ndarray, y: np.ndarray, groups: np.ndarray, alpha: float, folds: int = 5, seed: int = 0) -> float:
    rng = np.random.default_rng(seed); uniq = np.unique(groups); rng.shuffle(uniq)
    fold_of = {g: i % folds for i, g in enumerate(uniq)}; f = np.array([fold_of[g] for g in groups])
    preds = np.zeros_like(y, dtype=np.float64)
    for k in range(folds):
        tr, te = f != k, f == k
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-6
        Xtr, Xte = (X[tr] - mu) / sd, (X[te] - mu) / sd
        ym = y[tr].mean()
        # dual ridge (n < d): w = X^T (XX^T + aI)^-1 y
        G = Xtr @ Xtr.T
        a = np.linalg.solve(G + alpha * np.eye(G.shape[0]), y[tr] - ym)
        preds[te] = Xte @ (Xtr.T @ a) + ym
    ss_res = ((y - preds) ** 2).sum(); ss_tot = ((y - y.mean()) ** 2).sum()
    return 1 - ss_res / ss_tot


def analyze(dump_path: Path, label: str) -> dict:
    d = torch.load(dump_path, map_location="cpu")
    attn_path = dump_path.parent / "dot_attention.pt"
    if "attn_layers" not in d and attn_path.exists():
        a = torch.load(attn_path, map_location="cpu")
        for k in ("attn_layers", "regions", "attn_from_answer", "attn_from_dots"):
            d[k] = a[k]
    R = d["resid"].float().numpy()            # [N, L, P, D]
    N, L, P, D = R.shape; K = P - 3
    meta = d["meta"]; regions = d.get("regions", ["bos", "prefix", "problem", "dots", "template"])
    out = {"label": label, "n_items": N, "n_layers": L, "k": K}

    # 1. problem independence
    dots = R[:, :, :K, :]                      # [N, L, K, D]
    pi = []
    for l in range(L):
        X = dots[:, l]                          # [N, K, D]
        total = X.reshape(-1, D).var(0).sum()
        pos_means = X.mean(0); item_means = X.mean(1)
        var_pos = pos_means.var(0).sum(); var_item = item_means.var(0).sum()
        resid = X - pos_means[None] - item_means[:, None] + X.mean((0, 1))[None, None]
        var_res = resid.reshape(-1, D).var(0).sum()
        Xn = X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-6)
        same_pos = np.mean([ (Xn[:, k] @ Xn[:, k].T)[np.triu_indices(N, 1)].mean() for k in range(0, K, max(1, K // 10)) ])
        diff_pos = np.mean([ (Xn[i] @ Xn[i].T)[np.triu_indices(K, 1)].mean() for i in range(0, N, max(1, N // 10)) ])
        pi.append({"layer": l, "frac_var_position": float(var_pos / total), "frac_var_problem": float(var_item / total), "frac_var_interaction": float(var_res / total),
                   "cos_same_pos_across_problems": float(same_pos), "cos_same_problem_across_pos": float(diff_pos)})
    out["problem_independence"] = pi

    # 2. probes
    stages = list(meta[0]["expected_intermediates"])
    y_all = {s: np.array([float(m["expected_intermediates"][s]) for m in meta]) for s in stages}
    probe = {}
    rng = np.random.default_rng(1)
    for where, sel in (("dots_mean", None), ("q_last", K), ("cue", K + 1), ("gen", K + 2)):
        probe[where] = {}
        for s in stages:
            y = y_all[s]; row = []
            for l in range(L):
                X = dots[:, l].mean(1) if sel is None else R[:, l, sel]
                r2 = ridge_cv_r2(X, y, np.arange(N), alpha=10.0)
                row.append(r2)
            probe[where][s] = row
        # shuffled-label control for 'answer'
        y = y_all["answer"].copy(); rng.shuffle(y)
        probe[where]["answer_SHUFFLED"] = [ridge_cv_r2(dots[:, l].mean(1) if sel is None else R[:, l, sel], y, np.arange(N), 10.0) for l in range(L)]
    out["probes"] = probe

    # 3. attention (absent for the DeepSeek dump)
    att = {}
    for l in d.get("attn_layers", []):
        A = np.array([a[str(l)] for a in d["attn_from_answer"] if str(l) in a])   # [N, 3, H, R]
        Dd = np.array([a[str(l)] for a in d["attn_from_dots"] if str(l) in a])    # [N, H, R]
        if len(A) == 0: continue
        att[l] = {"gen_by_region": A[:, 2].mean((0, 1)).tolist(), "cue_by_region": A[:, 1].mean((0, 1)).tolist(), "qlast_by_region": A[:, 0].mean((0, 1)).tolist(),
                  "dots_by_region": Dd.mean((0, 1)).tolist(),
                  "gen_dot_mass_per_head": A[:, 2, :, regions.index("dots")].mean(0).tolist(),
                  "max_head_gen_dot_mass": float(A[:, 2, :, regions.index("dots")].mean(0).max())}
    out["attention"] = att

    # 5. per-stream analysis (DeepSeek hyper-connection dumps: resid_streams [N, L, P, 4, D])
    if "resid_streams" in d and d["resid_streams"] is not None:
        S = d["resid_streams"].float().numpy(); n_s = S.shape[3]
        per_stream = {"frac_var_problem": [], "cos_same_pos_other_problems": [], "probe_answer_dots": [], "probe_queried_base_dots": []}
        y_ans = y_all["answer"]; y_base = y_all[stages[0]]
        for si in range(n_s):
            fv, cs, pa, pb = [], [], [], []
            for l in range(L):
                X = S[:, l, :K, si, :]
                total = X.reshape(-1, D).var(0).sum(); item_means = X.mean(1); fv.append(float(item_means.var(0).sum() / total))
                Xn = X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-6)
                cs.append(float(np.mean([(Xn[:, k] @ Xn[:, k].T)[np.triu_indices(N, 1)].mean() for k in range(0, K, max(1, K // 10))])))
                pa.append(ridge_cv_r2(X.mean(1), y_ans, np.arange(N), 10.0)); pb.append(ridge_cv_r2(X.mean(1), y_base, np.arange(N), 10.0))
            per_stream["frac_var_problem"].append(fv); per_stream["cos_same_pos_other_problems"].append(cs)
            per_stream["probe_answer_dots"].append(pa); per_stream["probe_queried_base_dots"].append(pb)
        # stream norms at dots by layer
        per_stream["norm_dots"] = [np.linalg.norm(S[:, :, :K, si, :], axis=-1).mean((0, 2)).tolist() for si in range(n_s)]
        out["per_stream"] = per_stream

    # 4. trajectories
    E, Nn = d["entropy"].float().numpy(), d["norms"].float().numpy()
    out["trajectories"] = {"entropy_dots": E[:, :, :K].mean((0, 2)).tolist(), "entropy_qlast": E[:, :, K].mean(0).tolist(), "entropy_cue": E[:, :, K + 1].mean(0).tolist(), "entropy_gen": E[:, :, K + 2].mean(0).tolist(),
                           "norm_dots": Nn[:, :, :K].mean((0, 2)).tolist(), "norm_qlast": Nn[:, :, K].mean(0).tolist(), "norm_cue": Nn[:, :, K + 1].mean(0).tolist(), "norm_gen": Nn[:, :, K + 2].mean(0).tolist()}
    return out


def fmt_layers(vals, picks):
    return " | ".join(f"{vals[i]:.2f}" for i in picks)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dump", action="append", required=True, help="label=path/to/dot_dump.pt")
    p.add_argument("--output-dir", type=Path, required=True)
    args = p.parse_args()
    results = []
    for spec in args.dump:
        label, path = spec.split("=", 1); results.append(analyze(Path(path), label)); print("analyzed", label, flush=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "dot-analysis.json").write_text(json.dumps(results))
    L = results[0]["n_layers"]; picks = [0, L // 4, L // 2, 3 * L // 4, L - 3, L - 1]; hdr = " | ".join(f"L{i}" for i in picks)
    lines = [f"# What happens at dot positions ({results[0]['n_items']} held-out items, k={results[0]['k']})", ""]
    lines += ["## 1. Problem-independence of dot residuals", "", "Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.", ""]
    lines += [f"| Model | quantity | {hdr} |", "|---|---|" + "---:|" * len(picks)]
    for r in results:
        pi = r["problem_independence"]
        lines.append(f"| {r['label']} | var frac: problem | " + fmt_layers([x['frac_var_problem'] for x in pi], picks) + " |")
        lines.append(f"| {r['label']} | var frac: position | " + fmt_layers([x['frac_var_position'] for x in pi], picks) + " |")
        lines.append(f"| {r['label']} | cos same pos, other problems | " + fmt_layers([x['cos_same_pos_across_problems'] for x in pi], picks) + " |")
    lines += ["", "## 2. Linear probes (ridge, 5-fold CV R², item-level folds)", "", "Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.", ""]
    lines += [f"| Model | position | target | {hdr} | best layer (R²) |", "|---|---|---|" + "---:|" * len(picks) + "---:|"]
    for r in results:
        for where in ("dots_mean", "q_last", "cue", "gen"):
            for s, row in r["probes"][where].items():
                if s in ("first_product", "second_product"): continue
                b = int(np.argmax(row)); lines.append(f"| {r['label']} | {where} | {s} | " + fmt_layers(row, picks) + f" | L{b} ({row[b]:.2f}) |")
    lines += ["", "## 3. Attention (full-attention blocks only)", "", "Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).", ""]
    for r in results:
        if not r["attention"]:
            lines += [f"### {r['label']}", "", "(no attention recorded for this dump)", ""]; continue
        lines += [f"### {r['label']}", "", "| layer | query | " + " | ".join(REG := ["bos", "prefix", "problem", "dots", "template"]) + " | max head→dots |", "|---:|---|" + "---:|" * 6]
        for l, a in r["attention"].items():
            for q in ("gen", "cue", "dots"):
                v = a[f"{q}_by_region"]; extra = f"{a['max_head_gen_dot_mass']:.2f}" if q == "gen" else ""
                lines.append(f"| {l} | {q} | " + " | ".join(f"{x:.3f}" for x in v) + f" | {extra} |")
        lines.append("")
    lines += ["## 4. Processing trajectories", "", "Mean logit-lens entropy (nats) and residual norm by layer.", "", f"| Model | quantity | {hdr} |", "|---|---|" + "---:|" * len(picks)]
    for r in results:
        t = r["trajectories"]
        for q in ("entropy_dots", "entropy_qlast", "entropy_gen", "norm_dots", "norm_qlast", "norm_gen"):
            lines.append(f"| {r['label']} | {q} | " + fmt_layers(t[q], picks) + " |")
    for r in results:
        if "per_stream" not in r: continue
        ps = r["per_stream"]; n_s = len(ps["frac_var_problem"])
        lines += ["", f"## 5. Per hyper-connection stream ({r['label']})", "", f"| stream | quantity | {hdr} |", "|---|---|" + "---:|" * len(picks)]
        for si in range(n_s):
            lines.append(f"| {si} | var frac: problem (dots) | " + fmt_layers(ps["frac_var_problem"][si], picks) + " |")
            lines.append(f"| {si} | cos same pos, other problems | " + fmt_layers(ps["cos_same_pos_other_problems"][si], picks) + " |")
            lines.append(f"| {si} | probe R² answer from dots | " + fmt_layers(ps["probe_answer_dots"][si], picks) + " |")
            lines.append(f"| {si} | probe R² queried base from dots | " + fmt_layers(ps["probe_queried_base_dots"][si], picks) + " |")
            lines.append(f"| {si} | mean norm at dots | " + fmt_layers(ps["norm_dots"][si], picks) + " |")
    (args.output_dir / "dot-analysis.md").write_text("\n".join(lines) + "\n"); print("\n".join(lines))


if __name__ == "__main__":
    main()
