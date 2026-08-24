#!/usr/bin/env python3
"""Render one ordinary-prompt sanity result as a complete Markdown table."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def clean(text: str) -> str:
    return text.replace("\n", "↵").replace("|", "\\|").replace("`", "\\`")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--prompt-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    records = json.loads(args.input.read_text(encoding="utf-8"))
    record = next(item for item in records if item["id"] == args.prompt_id)
    lines = [
        f"# Complete J-Lens results: {args.prompt_id}",
        "",
        "These are J-Lens token readouts, not formal sparse J-space coordinates.",
        "",
        "## Exact rendered prompt",
        "",
        f"`{clean(record['rendered_prompt'])}`",
        "",
        f"Readout position: token {record['generation_position']} "
        f"(`{clean(record['token_strings'][record['generation_position']])}`).",
        "",
        "| Layer | Top-10 J-Lens tokens (rank order) | Top-1 probability |",
        "|---:|---|---:|",
    ]
    for layer, cells in sorted(
        record["readouts"]["j_lens"].items(), key=lambda item: int(item[0])
    ):
        tokens = cells[0]["top_tokens"]
        token_text = ", ".join(f"`{clean(token['token'])}`" for token in tokens)
        lines.append(f"| {layer} | {token_text} | {tokens[0]['probability']:.6f} |")
    lines.extend(
        [
            "",
            "## Token IDs and scores",
            "",
        ]
    )
    for layer, cells in sorted(
        record["readouts"]["j_lens"].items(), key=lambda item: int(item[0])
    ):
        lines.append(f"### Layer {layer}")
        lines.append("")
        lines.append("| Rank | Token | ID | Probability | Logit |")
        lines.append("|---:|---|---:|---:|---:|")
        for token in cells[0]["top_tokens"]:
            lines.append(
                f"| {token['rank']} | `{clean(token['token'])}` | {token['token_id']} | "
                f"{token['probability']:.9g} | {token['logit']:.6f} |"
            )
        lines.append("")
    args.output.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
