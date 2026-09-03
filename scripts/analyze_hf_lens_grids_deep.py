#!/usr/bin/env python3
"""Sharper statistics over ``extract_hf.py --phase filler`` grids.

1. Actual minus control first-digit log-probability at filler cells, by layer band
   (positive = the true stage digit is more decodable than a deranged one).
2. Stage ladder at the answer cue and generation positions: first layer at which
   each stage's best form is rank 1 / rank <= 10 (median over examples).
3. What the dot cells decode to: fraction of filler-cell top-1 tokens that are
   digits by layer band, and the most common top-1 tokens in the late band.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("readout_dir", type=Path)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    files = [f for f in sorted(args.readout_dir.glob("*.json")) if f.name != "runtime.json"]
    results = [json.loads(f.read_text()) for f in files]
    layers = sorted(map(int, results[0]["readouts"]["logit_lens"]))
    n = len(layers); bands = {"early": layers[: n // 3], "mid": layers[n // 3 : 2 * n // 3], "late": layers[2 * n // 3 :]}
    stages = list(results[0]["example"]["expected_intermediates"])

    def lp(cell, label):
        v = [x for x in cell["targets"][label]["variants"] if "probability" in x]
        return max((math.log(max(x["probability"], 1e-30)) for x in v), default=None)

    lines = [f"# Deep grid statistics ({len(results)} examples, {n} layers)", ""]
    # 1. actual - control at filler cells
    lines += ["## Filler cells: log p(true stage first digit) − log p(control digit), mean over cells", "",
              "| Stage | " + " | ".join(bands) + " |", "|---|" + "---:|" * len(bands)]
    for label in stages:
        row = []
        for band, ls in bands.items():
            diffs = []
            for r in results:
                if f"control_{label}" not in r["tracked_token_variants"]:
                    continue
                for l in ls:
                    for cell in r["readouts"]["logit_lens"][str(l)]:
                        if cell["position_kind"] != "filler":
                            continue
                        a, c = lp(cell, label), lp(cell, f"control_{label}")
                        if a is not None and c is not None:
                            diffs.append(a - c)
            row.append(f"{st.fmean(diffs):+.3f}" if diffs else "—")
        lines.append(f"| {label} | " + " | ".join(row) + " |")
    # 2. ladders at cue and gen positions
    for kind in ("answer_cue", "answer_prediction"):
        lines += ["", f"## Ladder at {kind}: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)", "",
                  "| Stage | rank 1 | rank ≤ 10 | control rank 1 |", "|---|---:|---:|---:|"]
        for label in stages:
            r1, r10, c1 = [], [], []
            for r in results:
                col = next(i for i, c in enumerate(r["selected_columns"]) if c["position_kind"] == kind)
                f1 = next((l for l in layers if r["readouts"]["logit_lens"][str(l)][col]["targets"][label]["best_rank"] == 1), None)
                f10 = next((l for l in layers if (r["readouts"]["logit_lens"][str(l)][col]["targets"][label]["best_rank"] or 10**9) <= 10), None)
                cl = f"control_{label}"
                fc = next((l for l in layers if cl in r["tracked_token_variants"] and r["readouts"]["logit_lens"][str(l)][col]["targets"][cl]["best_rank"] == 1), None)
                if f1 is not None: r1.append(f1)
                if f10 is not None: r10.append(f10)
                if fc is not None: c1.append(fc)
            fmt = lambda xs: f"{st.median(xs):g} (n={len(xs)})" if xs else "— (n=0)"
            lines.append(f"| {label} | {fmt(r1)} | {fmt(r10)} | {fmt(c1)} |")
    # 3. what dots decode to
    lines += ["", "## Filler-cell top-1 tokens", "", "| band | fraction digit tokens | most common top-1 tokens |", "|---|---:|---|"]
    for band, ls in bands.items():
        toks = Counter()
        for r in results:
            for l in ls:
                for cell in r["readouts"]["logit_lens"][str(l)]:
                    if cell["position_kind"] == "filler":
                        toks[cell["top_tokens"][0]["token"]] += 1
        total = sum(toks.values()); digit = sum(v for t, v in toks.items() if t.strip().isdigit())
        lines.append(f"| {band} | {digit/total:.3f} | " + ", ".join(f"`{t!r}`×{v}" for t, v in toks.most_common(6)) + " |")
    args.output.write_text("\n".join(lines) + "\n"); print("\n".join(lines))


if __name__ == "__main__":
    main()
