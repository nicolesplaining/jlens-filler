#!/usr/bin/env python3
"""Ridge probes (dual form, 5-fold CV R^2, item-level folds) for the answer and stage values at q_last / cue / gen
from a residual dump, for any filler length including K=0. Prints per-layer R^2 and the best layer per position."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import torch

def cv_r2(X: torch.Tensor, y: torch.Tensor, alpha: float, folds: int = 5) -> float:
    N = X.shape[0]; idx = torch.arange(N); preds = torch.zeros(N)
    for f in range(folds):
        te = idx[f::folds]; tr = torch.tensor([i for i in range(N) if i % folds != f])
        Xtr, ytr = X[tr], y[tr]; mu = Xtr.mean(0, keepdim=True); ym = ytr.mean()
        A = Xtr - mu; K = A @ A.T; coef = torch.linalg.solve(K + alpha * torch.eye(len(tr)), ytr - ym)
        preds[te] = ((X[te] - mu) @ A.T) @ coef + ym
    return float(1 - ((preds - y) ** 2).sum() / ((y - y.mean()) ** 2).sum())

def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--dump", action="append", required=True, help="label=path"); p.add_argument("--output", type=Path, required=True)
    p.add_argument("--targets", default="answer,bound_value,base_value"); a = p.parse_args()
    lines = ["| model | position | target | " + " | ".join(f"L{l}" for l in (0, 10, 21, 28, 32, 35, 40, 42)) + " | best |", "|---|---|---|" + "---:|" * 9]
    out = {}
    for spec in a.dump:
        label, path = spec.split("=", 1); d = torch.load(path, map_location="cpu", weights_only=False)
        resid = d["resid"].float(); pos = d["positions"]; L = resid.shape[1]
        meta = d["meta"]; ys = {t: torch.tensor([float(m["expected_intermediates"][t]) for m in meta]) for t in a.targets.split(",")}
        out[label] = {}
        for name in ("q_last", "cue", "gen"):
            j = pos.index(name)
            for t, y in ys.items():
                r2 = [cv_r2(resid[:, l, j], y, alpha=resid.shape[0] * 10.0) for l in range(L)]
                out[label][f"{name}/{t}"] = r2; best = max(range(L), key=lambda l: r2[l])
                cells = [f"{r2[l]:.2f}" for l in (0, 10, 21, 28, 32, 35, 40, 42) if l < L]
                lines.append(f"| {label} | {name} | {t} | " + " | ".join(cells) + f" | L{best} ({r2[best]:.2f}) |")
    a.output.parent.mkdir(parents=True, exist_ok=True); a.output.write_text("\n".join(lines) + "\n"); a.output.with_suffix(".json").write_text(json.dumps(out))
    print("\n".join(lines))

if __name__ == "__main__":
    main()
