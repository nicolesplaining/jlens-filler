#!/usr/bin/env python3
"""Build one multi-family patch manifest from scaled varbind readouts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_varbind_deep_dive import patch_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--cells", type=int, default=16)
    parser.add_argument("--max-pairs", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    pairs = config["source"]["selected_pairs"][: args.max_pairs]
    results = {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in args.input_dir.glob("varbind_scale_*.json")
    }
    directions = []
    for pair in pairs:
        donor_id, target_id = pair["donor_id"], pair["target_id"]
        missing = {donor_id, target_id} - set(results)
        if missing:
            raise ValueError(f"missing readouts for {sorted(missing)}")
        one = patch_manifest(
            [results[donor_id], results[target_id]],
            f"{donor_id},{target_id}",
            args.cells,
        )
        for direction in one["directions"]:
            direction["family"] = pair["family"]
            direction["source_template_id"] = pair["source_template_id"]
            directions.append(direction)

    output = {
        "schema_version": 1,
        "cells_per_stage": args.cells,
        "pair_count": len(pairs),
        "directions": directions,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.output}: {len(pairs)} pairs, {len(directions)} directions")


if __name__ == "__main__":
    main()
