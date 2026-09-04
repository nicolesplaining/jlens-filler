#!/usr/bin/env python3
"""Figures from analyze_dot_residuals.py output: attention heatmaps, probe R², problem-independence, trajectories."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

p = argparse.ArgumentParser(); p.add_argument("analysis_json", type=Path); p.add_argument("--output-dir", type=Path, required=True); a = p.parse_args()
res = json.loads(a.analysis_json.read_text()); a.output_dir.mkdir(parents=True, exist_ok=True)
regions = ["bos", "prefix", "problem", "dots", "template"]

# 1. attention heatmaps: rows = full-attention layers, cols = regions; one panel per model × query
n_att = max(len(r["attention"]) for r in res)
fig, axes = plt.subplots(len(res), 3, figsize=(12, max(2.6, 0.28 * n_att + 1.2) * len(res)), squeeze=False)
for i, r in enumerate(res):
    layers = list(r["attention"]); 
    for j, q in enumerate(("gen", "cue", "dots")):
        M = np.array([r["attention"][l][f"{q}_by_region"] for l in layers])
        ax = axes[i, j]; im = ax.imshow(M, vmin=0, vmax=1, cmap="viridis", aspect="auto")
        ax.set_xticks(range(5)); ax.set_xticklabels(regions, rotation=30, fontsize=8); ax.set_yticks(range(len(layers))); ax.set_yticklabels([f"L{l}" for l in layers], fontsize=8)
        ax.set_title(f"{r['label']}: attention from {q}", fontsize=9)
        if len(layers) <= 12:
            for (y, x), v in np.ndenumerate(M): ax.text(x, y, f"{v:.2f}", ha="center", va="center", fontsize=7, color="w" if v < 0.5 else "k")
n_items = " / ".join(str(r.get("n_items", "?")) for r in res)
fig.suptitle(f"Attention mass by key region (full-attention blocks, mean over heads and {n_items} held-out items)", fontsize=10); fig.tight_layout(); fig.savefig(a.output_dir / "attention_heatmaps.png", dpi=130); plt.close(fig)

# 2. probes
stages = [s for s in res[0]["probes"]["gen"] if s not in ("first_product", "second_product")]
fig, axes = plt.subplots(1, 4, figsize=(15, 3.4), sharey=True)
for j, where in enumerate(("dots_mean", "q_last", "cue", "gen")):
    ax = axes[j]
    for r in res:
        for s in stages:
            y = np.clip(r["probes"][where][s], -0.2, 1)
            ax.plot(y, lw=1.6 if s == "answer" else 1, ls="--" if s == "answer_SHUFFLED" else "-", label=f"{r['label']}/{s}")
    ax.set_title(f"probe at {where}", fontsize=9); ax.set_xlabel("block"); ax.axhline(0, color="k", lw=0.5)
axes[0].set_ylabel("CV R²"); axes[-1].legend(fontsize=6, ncol=1, loc="upper left", bbox_to_anchor=(1.01, 1))
fig.suptitle("Ridge probes for stage values from residuals (5-fold CV, item folds)", fontsize=10); fig.tight_layout(); fig.savefig(a.output_dir / "probes.png", dpi=130, bbox_inches="tight"); plt.close(fig)

# 3. problem-independence + 4. trajectories
fig, axes = plt.subplots(1, 3, figsize=(14, 3.4))
for r in res:
    pi = r["problem_independence"]
    axes[0].plot([x["frac_var_problem"] for x in pi], label=f"{r['label']} problem"); axes[0].plot([x["frac_var_position"] for x in pi], ls="--", label=f"{r['label']} position")
    axes[1].plot(r["trajectories"]["entropy_dots"], label=f"{r['label']} dots"); axes[1].plot(r["trajectories"]["entropy_gen"], ls="--", label=f"{r['label']} gen")
    axes[2].plot(r["trajectories"]["norm_dots"], label=f"{r['label']} dots"); axes[2].plot(r["trajectories"]["norm_gen"], ls="--", label=f"{r['label']} gen")
axes[0].set_title("dot-residual variance: fraction by problem vs by position", fontsize=9); axes[0].legend(fontsize=6)
axes[1].set_title("logit-lens entropy (nats)", fontsize=9); axes[1].legend(fontsize=6); axes[2].set_title("residual norm", fontsize=9); axes[2].legend(fontsize=6)
for ax in axes: ax.set_xlabel("block")
fig.tight_layout(); fig.savefig(a.output_dir / "independence_trajectories.png", dpi=130); plt.close(fig)
print("wrote", sorted(str(x.name) for x in a.output_dir.glob("*.png")))
