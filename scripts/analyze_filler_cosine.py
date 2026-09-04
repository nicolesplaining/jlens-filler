#!/usr/bin/env python3
"""Adjacent-position cosine similarity across a filler span: where does the model "change thought"?

Input: one or more residual dumps from dump_dot_residuals_dsv4.py / dump_dot_residuals_hf.py
(`resid` [N, L, P, D] collapsed residuals; optional `resid_streams` [N, L, P, S, D]; `positions`
labels F1..FK, q_last, cue, gen).

For each model:
  1. per-layer adjacent cosine  cos(h[l, p], h[l, p+1])  averaged over items -> [L, K-1]
  2. flattened-over-layers adjacent cosine (raw concatenation and per-layer-normalized concatenation)
  3. the same on item-centered residuals (subtract the per-position mean over items), which removes
     the position-identity component and leaves the problem-specific content
  4. cosine of every filler position to F1 and to the last filler position (drift), per layer
  5. cosine of filler positions to q_last / cue / gen per layer
  6. change points: per item, positions where the normalized-flat adjacent cosine drops more than
     `--zthresh` standard deviations below that item's own mean; histogram over positions
  7. per-stream adjacent cosine when streams are present
Writes JSON, a markdown summary, and PNG figures to --output-dir.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def cos(a: torch.Tensor, b: torch.Tensor, dim: int = -1) -> torch.Tensor:
    return torch.nn.functional.cosine_similarity(a.float(), b.float(), dim=dim, eps=1e-8)


def analyze(label: str, path: Path, zthresh: float) -> dict:
    d = torch.load(path, map_location="cpu", weights_only=False)
    resid = d["resid"].float()                        # [N, L, P, D]
    positions = d["positions"]
    K = sum(1 for p in positions if p.startswith("F"))
    N, L, P, D = resid.shape
    F = resid[:, :, :K]                               # filler positions
    idx = {name: positions.index(name) for name in ("q_last", "cue", "gen") if name in positions}
    out: dict = {"label": label, "n_items": N, "n_layers": L, "n_filler": K, "positions": positions}

    # 1. per-layer adjacent cosine
    adj = cos(F[:, :, :-1], F[:, :, 1:])              # [N, L, K-1]
    out["adjacent_per_layer_mean"] = adj.mean(0).tolist()
    out["adjacent_per_layer_std_over_items"] = adj.std(0).tolist()

    # 2. flattened over layers
    flat = F.permute(0, 2, 1, 3).reshape(N, K, L * D)          # [N, K, L*D]
    adj_flat = cos(flat[:, :-1], flat[:, 1:])                    # [N, K-1]
    Fn = torch.nn.functional.normalize(F, dim=-1)
    flat_n = Fn.permute(0, 2, 1, 3).reshape(N, K, L * D)
    adj_flat_n = cos(flat_n[:, :-1], flat_n[:, 1:])              # equals the mean over layers of per-layer cos
    out["adjacent_flat_raw_mean"] = adj_flat.mean(0).tolist()
    out["adjacent_flat_raw_std"] = adj_flat.std(0).tolist()
    out["adjacent_flat_normalized_mean"] = adj_flat_n.mean(0).tolist()
    out["adjacent_flat_normalized_std"] = adj_flat_n.std(0).tolist()

    # 3. item-centered (problem-specific component only)
    C = F - F.mean(0, keepdim=True)
    adj_c = cos(C[:, :, :-1], C[:, :, 1:])                       # [N, L, K-1]
    out["centered_adjacent_per_layer_mean"] = adj_c.mean(0).tolist()
    Cn = torch.nn.functional.normalize(C, dim=-1)
    flat_c = Cn.permute(0, 2, 1, 3).reshape(N, K, L * D)
    adj_flat_c = cos(flat_c[:, :-1], flat_c[:, 1:])
    out["centered_adjacent_flat_normalized_mean"] = adj_flat_c.mean(0).tolist()
    out["centered_adjacent_flat_normalized_std"] = adj_flat_c.std(0).tolist()

    # 4. drift: cosine to F1 and to F_K, per layer
    out["cos_to_first_per_layer"] = cos(F, F[:, :, :1].expand_as(F)).mean(0).tolist()   # [L, K]
    out["cos_to_last_per_layer"] = cos(F, F[:, :, -1:].expand_as(F)).mean(0).tolist()
    out["centered_cos_to_first_per_layer"] = cos(C, C[:, :, :1].expand_as(C)).mean(0).tolist()

    # 5. filler vs answer-side positions
    for name, j in idx.items():
        tgt = resid[:, :, j:j + 1].expand_as(F)
        out[f"cos_filler_to_{name}_per_layer"] = cos(F, tgt).mean(0).tolist()              # [L, K]
        tgt_c = (resid[:, :, j] - resid[:, :, j].mean(0, keepdim=True)).unsqueeze(2).expand_as(C)
        out[f"centered_cos_filler_to_{name}_per_layer"] = cos(C, tgt_c).mean(0).tolist()

    # 6. change points on the normalized-flat series, per item
    series = adj_flat_n                                            # [N, K-1]
    mu = series.mean(1, keepdim=True); sd = series.std(1, keepdim=True)
    z = (series - mu) / (sd + 1e-8)
    cp = (z < -zthresh)                                            # boundary p means between F_{p+1} and F_{p+2}
    out["changepoint_zthresh"] = zthresh
    out["changepoints_per_item"] = cp.sum(1).tolist()
    out["changepoint_histogram"] = cp.sum(0).tolist()              # [K-1]
    out["changepoint_mean_count"] = float(cp.sum(1).float().mean())
    series_c = adj_flat_c
    zc = (series_c - series_c.mean(1, keepdim=True)) / (series_c.std(1, keepdim=True) + 1e-8)
    cpc = (zc < -zthresh)
    out["centered_changepoints_per_item"] = cpc.sum(1).tolist()
    out["centered_changepoint_histogram"] = cpc.sum(0).tolist()
    out["centered_changepoint_mean_count"] = float(cpc.sum(1).float().mean())

    # 7. streams
    if "resid_streams" in d:
        S = d["resid_streams"].float()[:, :, :K]                     # [N, L, K, S, D]
        adj_s = cos(S[:, :, :-1], S[:, :, 1:])                       # [N, L, K-1, S]
        out["stream_adjacent_per_layer_mean"] = adj_s.mean(0).permute(2, 0, 1).tolist()   # [S, L, K-1]
        Sc = S - S.mean(0, keepdim=True)
        out["stream_centered_adjacent_per_layer_mean"] = cos(Sc[:, :, :-1], Sc[:, :, 1:]).mean(0).permute(2, 0, 1).tolist()
    return out


def summarize(res: list[dict]) -> str:
    lines = ["# Adjacent-position cosine across the filler span", ""]
    for r in res:
        L, K = r["n_layers"], r["n_filler"]
        lines += [f"## {r['label']} ({r['n_items']} items, {K} filler positions, {L} layers)", ""]
        sel = sorted(set([0, L // 4, L // 2, 3 * L // 4, L - 1]))
        lines += ["Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):", "",
                  "| layer | raw | centered (problem component) |", "|---:|---:|---:|"]
        for l in sel:
            a = torch.tensor(r["adjacent_per_layer_mean"][l]); c = torch.tensor(r["centered_adjacent_per_layer_mean"][l])
            lines.append(f"| {l} | {a.mean():.3f} [{a.min():.3f} @ {int(a.argmin()) + 1}] | {c.mean():.3f} [{c.min():.3f} @ {int(c.argmin()) + 1}] |")
        fn = torch.tensor(r["adjacent_flat_normalized_mean"]); fc = torch.tensor(r["centered_adjacent_flat_normalized_mean"])
        lines += ["", f"Flattened over layers (per-layer-normalized): mean {fn.mean():.3f}, min {fn.min():.3f} at boundary {int(fn.argmin()) + 1}, "
                  f"first boundary {fn[0]:.3f}, last {fn[-1]:.3f}.",
                  f"Centered: mean {fc.mean():.3f}, min {fc.min():.3f} at boundary {int(fc.argmin()) + 1}, first {fc[0]:.3f}, last {fc[-1]:.3f}.",
                  f"Change points (z < -{r['changepoint_zthresh']}) per item: raw {r['changepoint_mean_count']:.2f}, centered {r['centered_changepoint_mean_count']:.2f}."]
        h = torch.tensor(r["changepoint_histogram"]); hc = torch.tensor(r["centered_changepoint_histogram"])
        top = torch.topk(h, min(5, len(h))); topc = torch.topk(hc, min(5, len(hc)))
        lines += [f"Most frequent change-point boundaries (raw): " + ", ".join(f"F{int(i) + 1}|F{int(i) + 2} ({int(v)} items)" for v, i in zip(top.values, top.indices)),
                  f"Most frequent change-point boundaries (centered): " + ", ".join(f"F{int(i) + 1}|F{int(i) + 2} ({int(v)} items)" for v, i in zip(topc.values, topc.indices)), ""]
        for name in ("q_last", "cue", "gen"):
            key = f"centered_cos_filler_to_{name}_per_layer"
            if key in r:
                m = torch.tensor(r[key])                                   # [L, K]
                lmax = int(m.mean(1).argmax())
                lines.append(f"Centered cosine filler -> {name}: peaks at layer {lmax} (mean over filler {m[lmax].mean():.3f}; F1 {m[lmax, 0]:.3f}, F{K} {m[lmax, -1]:.3f}).")
        if "stream_adjacent_per_layer_mean" in r:
            lines += ["", "Per stream, mean adjacent cosine at three-quarter depth (raw / centered):"]
            l = 3 * L // 4
            for s_i, (a, c) in enumerate(zip(r["stream_adjacent_per_layer_mean"], r["stream_centered_adjacent_per_layer_mean"])):
                lines.append(f"- stream {s_i}: {torch.tensor(a[l]).mean():.3f} / {torch.tensor(c[l]).mean():.3f}")
        lines.append("")
    return "\n".join(lines)


def plot(res: list[dict], out: Path) -> None:
    n = len(res)
    fig, axes = plt.subplots(2, n, figsize=(5.2 * n, 7.5), squeeze=False)
    for i, r in enumerate(res):
        for row, key, title in ((0, "adjacent_per_layer_mean", "adjacent cos (raw)"), (1, "centered_adjacent_per_layer_mean", "adjacent cos (item-centered)")):
            M = torch.tensor(r[key])
            ax = axes[row, i]; im = ax.imshow(M, aspect="auto", cmap="viridis", vmin=-0.2 if row else 0, vmax=1)
            ax.set_title(f"{r['label']}: {title}", fontsize=9); ax.set_xlabel("boundary p|p+1"); ax.set_ylabel("layer")
            plt.colorbar(im, ax=ax, fraction=0.03)
    fig.tight_layout(); fig.savefig(out / "adjacent_cosine_heatmaps.png", dpi=130); plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for r in res:
        K = r["n_filler"]; x = list(range(1, K))
        m = torch.tensor(r["adjacent_flat_normalized_mean"]); s = torch.tensor(r["adjacent_flat_normalized_std"])
        axes[0].plot(x, m, label=r["label"]); axes[0].fill_between(x, m - s, m + s, alpha=0.15)
        mc = torch.tensor(r["centered_adjacent_flat_normalized_mean"]); sc = torch.tensor(r["centered_adjacent_flat_normalized_std"])
        axes[1].plot(x, mc, label=r["label"]); axes[1].fill_between(x, mc - sc, mc + sc, alpha=0.15)
        axes[2].plot(x, torch.tensor(r["centered_changepoint_histogram"]) / r["n_items"], label=r["label"])
    axes[0].set_title("adjacent cosine, flattened over layers (raw)"); axes[1].set_title("adjacent cosine, flattened (item-centered)"); axes[2].set_title("fraction of items with a change point at boundary (centered)")
    for ax in axes: ax.set_xlabel("boundary p|p+1"); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(out / "adjacent_cosine_flat.png", dpi=130); plt.close(fig)

    fig, axes = plt.subplots(1, n, figsize=(5.2 * n, 3.8), squeeze=False)
    for i, r in enumerate(res):
        ax = axes[0, i]
        for name in ("q_last", "cue", "gen"):
            key = f"centered_cos_filler_to_{name}_per_layer"
            if key in r: ax.plot(torch.tensor(r[key]).mean(1), label=f"filler -> {name}")
        ax.plot(torch.tensor(r["centered_cos_to_first_per_layer"])[:, 1:].mean(1), "--", label="filler -> F1")
        ax.set_title(f"{r['label']}: item-centered cosine by layer", fontsize=9); ax.set_xlabel("layer"); ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(out / "filler_to_answer_cosine.png", dpi=130); plt.close(fig)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dump", action="append", required=True, help="label=path/to/dot_dump.pt (repeatable)")
    p.add_argument("--output-dir", type=Path, required=True); p.add_argument("--zthresh", type=float, default=2.0)
    a = p.parse_args(); a.output_dir.mkdir(parents=True, exist_ok=True)
    res = []
    for spec in a.dump:
        label, path = spec.split("=", 1); res.append(analyze(label, Path(path), a.zthresh)); print("analyzed", label, flush=True)
    (a.output_dir / "filler-cosine.json").write_text(json.dumps(res))
    md = summarize(res); (a.output_dir / "filler-cosine.md").write_text(md); print(md)
    plot(res, a.output_dir); print("wrote figures to", a.output_dir)


if __name__ == "__main__":
    main()
