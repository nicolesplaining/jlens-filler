#!/usr/bin/env python3
"""Attention mass on the filler-announcement sentence (region 'announce') from q_last / cue / gen, per block,
from dot_attention.pt files written by dump_dot_attention_dsv4.py with the announce region."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import torch

def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--dump", action="append", required=True, help="label=path"); p.add_argument("--output", type=Path, required=True); a = p.parse_args()
    lines = []; out = {}
    for spec in a.dump:
        label, path = spec.split("=", 1); d = torch.load(path, map_location="cpu", weights_only=False)
        R = d["regions"]; ai = R.index("announce"); pi = R.index("prefix"); layers = d["attn_layers"]
        recs = d["attn_from_answer"]; n_ann = [m.get("n_announce_tokens", 0) for m in d["meta"]]
        per = {}   # query -> [L] mean mass on announce; also max head
        for qi, qname in enumerate(("q_last", "cue", "gen")):
            means, maxh, pref = [], [], []
            for l in layers:
                vals = [torch.tensor(r[str(l)])[qi] for r in recs if str(l) in r]     # [H, R] each
                if not vals: means.append(float("nan")); maxh.append(float("nan")); pref.append(float("nan")); continue
                M = torch.stack(vals)                                              # [N, H, R]
                means.append(float(M[:, :, ai].mean())); maxh.append(float(M[:, :, ai].mean(0).max())); pref.append(float(M[:, :, pi].mean()))
            per[qname] = {"announce_mean": means, "announce_max_head": maxh, "prefix_mean": pref}
        out[label] = {"per_query": per, "n_announce_tokens_mean": sum(n_ann) / max(1, len(n_ann)), "layers": layers}
        L = len(layers); last = layers[L - L // 3:]
        lines.append(f"## {label} ({len(recs)} items; announcement sentence = {out[label]['n_announce_tokens_mean']:.0f} tokens)")
        lines.append("| query | mean mass on announcement, all blocks | last third | peak block (mass) | max single head (block) | mass on rest of prefix, last third |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for qname, v in per.items():
            m = torch.tensor(v["announce_mean"]); mh = torch.tensor(v["announce_max_head"]); pr = torch.tensor(v["prefix_mean"])
            li = [layers.index(l) for l in last]
            pk = int(m.argmax()); hk = int(mh.argmax())
            lines.append(f"| {qname} | {float(m.mean()):.4f} | {float(m[li].mean()):.4f} | L{layers[pk]} ({float(m[pk]):.3f}) | {float(mh[hk]):.3f} (L{layers[hk]}) | {float(pr[li].mean()):.3f} |")
        # all-region breakdown from q_last, last third of blocks and peak block per region
        lines.append("q_last mass by region (last third mean | peak block):")
        for r_i, rname in enumerate(R):
            vals = []
            for l in layers:
                v = [torch.tensor(r[str(l)])[0, :, r_i].mean() for r in recs if str(l) in r]
                vals.append(float(torch.stack(v).mean()) if v else float("nan"))
            vt = torch.tensor(vals); li = [layers.index(l) for l in last]; pk = int(vt.argmax())
            lines.append(f"- {rname}: {float(vt[li].mean()):.3f} | L{layers[pk]} ({float(vt[pk]):.3f})")
        lines.append("")
    a.output.parent.mkdir(parents=True, exist_ok=True); a.output.write_text("\n".join(lines) + "\n"); a.output.with_suffix(".json").write_text(json.dumps(out)); print("\n".join(lines))

if __name__ == "__main__":
    main()
