#!/usr/bin/env python3
"""Generate token-position-matched counterfactuals from one varbind template."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--example-id", default="varbind_easy_0002")
    parser.add_argument("--base-values", default="52,56,60,64,68,72,76,80")
    parser.add_argument("--single-filler-length", type=int)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def derive_example(template: dict[str, Any], base: int) -> dict[str, Any]:
    item = copy.deepcopy(template)
    definitions = item["definitions"]
    queried_term = item["queried_term"]
    query_definition = next(value for name, value in definitions if name == queried_term)
    if not isinstance(query_definition, str):
        raise ValueError("queried term must be derived")
    if query_definition != "twice the number for suv minus 9":
        raise ValueError(f"unexpected template definition: {query_definition}")
    for definition in definitions:
        if definition[0] == "suv":
            definition[1] = base
            break
    else:
        raise ValueError("template does not contain suv")
    bound = 2 * base - 9
    second_product = 2 * bound
    answer = second_product - 14
    item["id"] = f"varbind_cf_suv_{base:03d}"
    item["idx"] = item["id"]
    item["queried_value"] = bound
    item["answer"] = answer
    item["expected_intermediates"] = {
        "base_value": str(base),
        "first_product": str(2 * base),
        "bound_value": str(bound),
        "second_product": str(second_product),
        "answer": str(answer),
    }
    item["highlight_forms"] = {
        label: [surface]
        for label, surface in item["expected_intermediates"].items()
    }
    item.pop("tracked_controls", None)
    item.pop("control_donor_id", None)
    item.pop("behavior_cohort", None)
    return item


def main() -> None:
    args = parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    template = next(
        example for example in source["examples"] if example["id"] == args.example_id
    )
    bases = [int(value) for value in args.base_values.split(",") if value.strip()]
    if len(bases) != len(set(bases)) or not bases:
        raise ValueError("base values must be unique")
    output = copy.deepcopy(source)
    if args.single_filler_length is None:
        output["filler_lengths"] = [0, 50]
        output.pop("filler_length", None)
    else:
        output["filler_length"] = args.single_filler_length
        output.pop("filler_lengths", None)
    output["examples"] = [derive_example(template, base) for base in bases]
    output["source"] = {
        **source["source"],
        "selection": (
            f"controlled counterfactuals derived from {args.example_id}; only the "
            "single-token numeric literal bound to suv changes"
        ),
        "prompt_note": (
            "Behavior screen for exact-structure donor/target residual patching. "
            "Token lengths and filler indices are validated after inference."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "examples": [
                    {
                        "id": example["id"],
                        "expected": example["expected_intermediates"],
                    }
                    for example in output["examples"]
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
