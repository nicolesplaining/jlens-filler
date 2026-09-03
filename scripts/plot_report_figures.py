#!/usr/bin/env python3
"""Figures for the PDF report: model screen, training curves, lesion/patch summary."""
import json, statistics as st
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = Path("results/report-figures"); out.mkdir(parents=True, exist_ok=True)
acc = lambda d, k: sum(r["conditions"][str(k)]["correct"] for r in d["examples"])

# 1. screen: two-step accuracy, k=0 vs best dots vs pre-question control
models = [("Qwen3.5-4B", "qwen3.5-4b"), ("Qwen3.5-9B", "qwen3.5-9b"), ("Llama-3.1-8B-it", "llama3.1-8b-it"), ("Qwen3.5-27B", "qwen3.5-27b"),
          ("Qwen3.6-27B", "qwen3.6-27b"), ("Gemma-3-27B-it", "gemma-3-27b-it"), ("Qwen3-32B", "qwen3-32b"), ("OLMo-3.1-32B-it", "olmo-3.1-32b-it"),
          ("Qwen3-30B-A3B (MoE)", "qwen3-30b-a3b"), ("Qwen3.5-35B-A3B (MoE)", "qwen3.5-35b-a3b")]
rows = []
for name, tag in models:
    d = json.load(open(f"results/{tag}/varbind-eval/filler_length_sweep.json")); c = json.load(open(f"results/{tag}/varbind-pre-question-k50-control/filler_length_sweep.json"))
    rows.append((name, acc(d, 0), max(acc(d, k) for k in (5, 10, 25, 50, 100)), acc(c, 50)))
rows.append(("DeepSeek V4 Flash (Nicole)", 35, 49, 35))
fig, ax = plt.subplots(figsize=(10, 4.2)); x = np.arange(len(rows)); w = 0.27
ax.bar(x - w, [r[1] for r in rows], w, label="no dots (k=0)", color="#888"); ax.bar(x, [r[2] for r in rows], w, label="best dot count after the question", color="#2a6fdb"); ax.bar(x + w, [r[3] for r in rows], w, label="50 dots before the question (control)", color="#c96")
ax.set_xticks(x); ax.set_xticklabels([r[0] for r in rows], rotation=30, ha="right", fontsize=8); ax.set_ylabel("correct out of 50"); ax.set_ylim(0, 50); ax.legend(fontsize=8, loc="upper left")
ax.set_title("Released two-step variable-binding items: filler effect by model", fontsize=10); fig.tight_layout(); fig.savefig(out / "screen.png", dpi=150); plt.close(fig)

# 2. training curves
runs = [("9B, mixed k, chain 1", "qwen3.5-9b/lora-mixedk"), ("9B, mixed k, chain 2", "qwen3.5-9b/lora-c2-mixedk"), ("4B, mixed k, chain 1", "qwen3.5-4b/lora-mixedk"),
        ("9B, dots only (k=25,50,100)", "qwen3.5-9b/lora-dotsonly"), ("9B, k=0 only", "qwen3.5-9b/lora-k0only")]
fig, axes = plt.subplots(1, 5, figsize=(16, 3.3), sharey=True)
for ax, (name, path) in zip(axes, runs):
    log = [json.loads(l) for l in open(f"results/{path}/train-log.jsonl") if "eval" in l]
    steps = [r["step"] for r in log]
    for k, col in (("0", "k"), ("5", "#9ecae1"), ("25", "#4292c6"), ("50", "#2a6fdb"), ("100", "#08306b")):
        ax.plot(steps, [r["eval"][k] for r in log], marker="o", ms=3, color=col, label=f"k={k}" if ax is axes[0] else None)
    ax.plot(steps, [r["control"]["50"] for r in log], ls="--", color="#c96", marker="s", ms=3, label="50 dots before question" if ax is axes[0] else None)
    ax.set_title(name, fontsize=9); ax.set_xlabel("optimizer step"); ax.set_ylim(0, 50)
axes[0].set_ylabel("correct out of 50"); axes[0].legend(fontsize=7)
fig.suptitle("LoRA training: accuracy on 50 held-out items by dot count (chain-2 run evaluated on 50 chain-2 items)", fontsize=10); fig.tight_layout(); fig.savefig(out / "training.png", dpi=150); plt.close(fig)

# 3. lesions + patch grid
fig, axes = plt.subplots(1, 3, figsize=(14, 3.6))
for tag, col, label in (("lora-dotsonly", "#2a6fdb", "dots-only model"), ("lora-k0only", "#c96", "k=0-only model at k=50")):
    d = json.load(open(f"results/qwen3.5-9b/{tag}/lesion-all-layers/all-dots-lesion.json"))
    for mode, mk in (("mean", "o"), ("zero", "x")):
        vals = [t["all_layers"][mode]["delta_logp"] for t in d["targets"]]
        axes[0].scatter(np.full(len(vals), {"mean": 0, "zero": 1}[mode]) + (0.15 if tag == "lora-k0only" else -0.15) + np.random.default_rng(0).uniform(-0.05, 0.05, len(vals)), vals, color=col, marker=mk, label=f"{label}, {mode}", alpha=0.8)
axes[0].axhline(0, color="k", lw=0.5); axes[0].set_xticks([0, 1]); axes[0].set_xticklabels(["mean-replace all dots,\nall 32 blocks", "zero all dots,\nall 32 blocks"], fontsize=8)
axes[0].set_ylabel("change in log p(correct answer), nats"); axes[0].set_title("All-dot lesions", fontsize=9); axes[0].legend(fontsize=6)
d = json.load(open("results/qwen3.5-9b/lora-dotsonly/lesion-varbind_easy_0010/all-dots-lesion.json"))
axes[1].plot([r["layer"] for r in d["layers"]], [r["target_log_probability_change"] for r in d["layers"]], marker="o", ms=3, color="#2a6fdb")
axes[1].axhline(0, color="k", lw=0.5); axes[1].set_xlabel("block lesioned"); axes[1].set_title("Dots-only model: mean-replace all 50 dots at one block (item 0010)", fontsize=9); axes[1].set_ylabel("Δ log p(answer)")
for tag, col in (("dotsonly", "#2a6fdb"), ("k0only", "#c96")):
    g = json.load(open(f"results/qwen3.5-9b/patch-heldout-0067/{tag}/single-cell-grid.json"))
    M = np.zeros((len(g["layers"]), len(g["positions"])))
    for c in g["cells"]: M[g["layers"].index(c["layer"]), g["positions"].index(c["position"])] = c["donor_log_probability_change"]
    axes[2].plot(g["layers"], M.max(1), color=col, label=f"{tag}: best cell per block")
axes[2].axhline(0, color="k", lw=0.5); axes[2].set_xlabel("block"); axes[2].set_ylabel("max donor-answer Δ log p over 50 dots"); axes[2].set_title("Single-cell patching, held-out pair (base 43 vs 13)", fontsize=9); axes[2].legend(fontsize=7)
fig.tight_layout(); fig.savefig(out / "causal.png", dpi=150); plt.close(fig)
print(sorted(p.name for p in out.glob("*.png")))
