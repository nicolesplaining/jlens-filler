#!/usr/bin/env python3
"""Pick held-out items for logit-lens extraction on a trained model.

Keeps items that are wrong without dots and correct at ``--filler-length``
(the behavior-gated "rescued" set), then prefers items whose five stage values
have pairwise-distinct first digits, because on digit-split tokenizers the
per-cell readout can only rank the leading digit. Attaches Nicole's
stage-matched derangement controls so every grid has a null comparison.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from select_varbind_deep_dive import assign_controls  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("sweep", type=Path, help="filler_length_sweep.json from the trained model on the held-out config")
    p.add_argument("config", type=Path, help="the held-out config the sweep was run on")
    p.add_argument("--filler-length", type=int, default=50)
    p.add_argument("--max-cases", type=int, default=8)
    p.add_argument("--require-distinct-first-digits", action="store_true")
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    sweep = json.loads(args.sweep.read_text()); cfg = json.loads(args.config.read_text())
    by_id = {e["id"]: e for e in cfg["examples"]}
    k = str(args.filler_length)
    rescued, distinct = [], []
    for row in sweep["examples"]:
        c = row["conditions"]
        if c[k]["correct"] and not c["0"]["correct"]:
            item = by_id[row["id"]]
            digits = [str(v).lstrip("-")[0] for v in item["expected_intermediates"].values()]
            (distinct if len(set(digits)) == len(digits) else rescued).append(item)
    pool = distinct if args.require_distinct_first_digits else distinct + rescued
    chosen = [copy.deepcopy(e) for e in pool[: args.max_cases]]
    if len(chosen) < 2:
        raise SystemExit(f"only {len(chosen)} eligible items (rescued {len(rescued)+len(distinct)}, distinct-digit {len(distinct)})")
    assign_controls(chosen)
    out = {k2: v for k2, v in cfg.items() if k2 not in ("examples", "filler_lengths")}
    out["filler_length"] = args.filler_length
    out["examples"] = chosen
    out["source"] = dict(cfg.get("source", {}), selection=(
        f"held-out items wrong at k=0 and correct at k={args.filler_length} on the trained model; "
        f"{len(distinct)} with distinct stage first digits, {len(rescued)} others; first {len(chosen)} taken"))
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(f"rescued {len(rescued)+len(distinct)} (distinct-digit {len(distinct)}); wrote {len(chosen)} cases to {args.output}")
    for e in chosen:
        print("  ", e["id"], e["expected_intermediates"], "control:", e["control_donor_id"])


if __name__ == "__main__":
    main()
