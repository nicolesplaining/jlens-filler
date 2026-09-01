#!/usr/bin/env python3
"""Build J-Lens/logit-lens/control patch selections for one readout pair."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_varbind_deep_dive import patch_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--pair", required=True)
    parser.add_argument("--cells", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ids = [value.strip() for value in args.pair.split(",", 1)]
    if len(ids) != 2 or not all(ids):
        raise ValueError("--pair must contain two comma-separated IDs")
    results = [
        json.loads((args.input_dir / f"{example_id}.json").read_text(encoding="utf-8"))
        for example_id in ids
    ]
    output = patch_manifest(results, args.pair, args.cells)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
