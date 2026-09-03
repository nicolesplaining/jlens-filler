#!/usr/bin/env python3
"""Exact-layout counterfactual families for digit-split tokenizers.

Takes one chained-variable-binding item and produces variants that change the
queried chain's base literal by exactly one digit (e.g. 64 -> 74 or 64 -> 68),
so the rendered prompts differ at exactly one token. Recomputes and validates
every intermediate. Emits (a) a filler-length sweep config to screen behavior
of each variant and (b) a fixed-k config for single-cell patching.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from build_algorithm_probe_configs import CHAIN_PATTERN, derive_varbind_targets  # noqa: E402


def variants_of(item: dict[str, Any], values: list[int]) -> list[dict[str, Any]]:
    defs = {n: v for n, v in item["definitions"]}
    q = item["queried_term"]
    m = CHAIN_PATTERN.fullmatch(str(defs[q]))
    base_name = m.group(2)
    base = int(defs[base_name])
    out = []
    for value in values:
        if len(str(value)) != len(str(base)) or sum(a != b for a, b in zip(str(value), str(base))) != 1:
            continue  # must differ in exactly one digit -> exactly one token
        v = copy.deepcopy(item)
        v["definitions"] = [[n, value if n == base_name else val] for n, val in item["definitions"]]
        # recompute every derived value that depends (directly or transitively) on the base
        vals: dict[str, int] = {}
        for n, val in v["definitions"]:
            if isinstance(val, int):
                vals[n] = val
            else:
                mm = CHAIN_PATTERN.fullmatch(val); src = mm.group(2); c = int(mm.group(4))
                vals[n] = 2 * vals[src] + c if mm.group(3) == "plus" else 2 * vals[src] - c
        if any(x <= 0 or x >= 1000 for x in vals.values()):
            continue
        v["queried_value"] = vals[q]
        v["answer"] = 2 * vals[q] + item["constant"] if item["operation"] == "plus" else 2 * vals[q] - item["constant"]
        if v["answer"] <= 0 or v["answer"] >= 1000:
            continue
        v["expected_intermediates"] = derive_varbind_targets(v)
        v["highlight_forms"] = {k: [s] for k, s in v["expected_intermediates"].items()}
        v["id"] = f"{item['id']}_cf_{base_name}_{value:03d}"
        v["counterfactual_of"] = item["id"]; v["changed_literal"] = {"name": base_name, "from": base, "to": value}
        out.append(v)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("config", type=Path)
    p.add_argument("--example-id", required=True)
    p.add_argument("--filler-length", type=int, default=50)
    p.add_argument("--filler-lengths", default="0,5,10,25,50,100")
    p.add_argument("--output-prefix", type=Path, required=True)
    args = p.parse_args()
    cfg = json.loads(args.config.read_text())
    item = next(e for e in cfg["examples"] if e["id"] == args.example_id)
    defs = {n: v for n, v in item["definitions"]}
    base = int(defs[CHAIN_PATTERN.fullmatch(str(defs[item["queried_term"]])).group(2)])
    candidates = sorted({int(f"{d}{str(base)[1]}") for d in "123456789"} | {int(f"{str(base)[0]}{d}") for d in "0123456789"})
    variants = variants_of(item, [c for c in candidates if c != base])
    original = copy.deepcopy(item); original["id"] = f"{item['id']}_cf_{item['id'].split('_')[-1]}_{base:03d}_orig"
    family = [original] + variants
    common = {k: v for k, v in cfg.items() if k not in ("examples", "filler_length", "filler_lengths")}
    sweep = dict(common, filler_lengths=[int(x) for x in args.filler_lengths.split(",")], examples=family)
    fixed = dict(common, filler_length=args.filler_length, examples=family)
    Path(f"{args.output_prefix}_sweep.json").write_text(json.dumps(sweep, indent=2) + "\n")
    Path(f"{args.output_prefix}_k{args.filler_length}.json").write_text(json.dumps(fixed, indent=2) + "\n")
    print(f"{len(family)} family members (base {base} -> {[v['changed_literal']['to'] for v in variants]})")
    for v in family:
        print("  ", v["id"], v["expected_intermediates"])


if __name__ == "__main__":
    main()
