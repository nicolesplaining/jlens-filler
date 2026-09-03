#!/usr/bin/env python3
"""Summarize logit-lens grids from ``extract_hf.py --phase filler`` across examples.

For each tracked stage: the first layer at which its best form is rank 1 in any
filler cell, the number of rank-1 filler cells, and the same numbers for the
deranged control labels (``control_*``) if present. Also the per-position
rank-1 profile (which dots carry each stage) and the answer-position ladder.
"""

from __future__ import annotations

import argparse
import json
import statistics as st
from collections import defaultdict
from pathlib import Path
from typing import Any


def grid_stats(result: dict[str, Any]) -> dict[str, Any]:
    cells = result["readouts"]["logit_lens"]
    layers = sorted(map(int, cells))
    stages = list(result["example"]["expected_intermediates"])
    controls = [k for k in result["tracked_token_variants"] if k.startswith("control_")]
    out: dict[str, Any] = {"id": result["example"]["id"], "layers": layers, "stages": {}, "profile": {}}
    n_filler = sum(c["position_kind"] == "filler" for c in result["selected_columns"])
    for label in stages + controls:
        first_l1, n_l1, best = None, 0, (10**9, None, None)
        pos_counts = [0] * n_filler
        cue_first, gen_first = None, None
        for l in layers:
            for cell in cells[str(l)]:
                r = cell["targets"][label]["best_rank"]
                if r is None:
                    continue
                if cell["position_kind"] == "filler":
                    if r == 1:
                        n_l1 += 1; pos_counts[cell["filler_ordinal"] - 1] += 1
                        if first_l1 is None: first_l1 = l
                    if r < best[0]: best = (r, l, cell["filler_ordinal"])
                elif cell["position_kind"] == "answer_cue" and r == 1 and cue_first is None: cue_first = l
                elif cell["position_kind"] == "answer_prediction" and r == 1 and gen_first is None: gen_first = l
        out["stages"][label] = {"first_rank1_layer": first_l1, "rank1_filler_cells": n_l1, "best": best,
                                "cue_first_rank1_layer": cue_first, "gen_first_rank1_layer": gen_first}
        out["profile"][label] = pos_counts
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("readout_dir", type=Path)
    p.add_argument("--output-dir", type=Path, required=True)
    args = p.parse_args()
    files = sorted(args.readout_dir.glob("*.json"))
    files = [f for f in files if f.name != "runtime.json"]
    per = [grid_stats(json.loads(f.read_text())) for f in files]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "lens-grid-summary.json").write_text(json.dumps(per, indent=1))

    labels = list(per[0]["stages"])
    lines = [f"# Logit-lens grid summary ({len(per)} examples, {len(per[0]['layers'])} layers)", "",
             "Readouts are first-digit forms for multi-digit values (coarse). `control_*` are stage-matched deranged values from another example.", "",
             "| Stage | Median first rank-1 layer (filler) | Examples with any rank-1 filler cell | Mean rank-1 filler cells | Median first rank-1 layer (gen pos) |", "|---|---:|---:|---:|---:|"]
    for label in labels:
        fl = [x["stages"][label]["first_rank1_layer"] for x in per if x["stages"][label]["first_rank1_layer"] is not None]
        gl = [x["stages"][label]["gen_first_rank1_layer"] for x in per if x["stages"][label]["gen_first_rank1_layer"] is not None]
        cells = [x["stages"][label]["rank1_filler_cells"] for x in per]
        lines.append(f"| {label} | {st.median(fl) if fl else '—'} | {len(fl)}/{len(per)} | {st.fmean(cells):.1f} | {st.median(gl) if gl else '—'} |")
    lines += ["", "## Rank-1 cells by filler position (summed over examples and layers)", ""]
    n = len(per[0]["profile"][labels[0]])
    lines.append("| Stage | " + " | ".join(f"F{i+1}" for i in range(n)) + " |"); lines.append("|---|" + "---:|" * n)
    for label in labels:
        tot = [sum(x["profile"][label][i] for x in per) for i in range(n)]
        lines.append(f"| {label} | " + " | ".join(map(str, tot)) + " |")
    (args.output_dir / "lens-grid-report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:6 + len(labels)]))


if __name__ == "__main__":
    main()
