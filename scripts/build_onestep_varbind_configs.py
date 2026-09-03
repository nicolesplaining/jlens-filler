#!/usr/bin/env python3
"""Deterministic one-step (chain_len=0) variable-binding configs.

Every released ``chained_var_binding_easy`` item has ``chain_len=1``: the queried
variable is itself defined by an affine expression, so the answer needs two
hidden steps. Qwen3.5-4B/9B and Llama-3.1-8B-Instruct score ~0% on those in
direct-answer mode, leaving nothing for filler to amplify. These items keep the
released scaffold, vocabulary, five-definition layout, and derived-expression
distractors, but query a *literal* variable, so the answer is one hidden step:
``base -> coefficient*base -> answer``.
"""

from __future__ import annotations

import argparse
import copy
import random
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_algorithm_probe_configs import (  # noqa: E402
    common,
    random_variable_names,
    write_config,
)

COEFFICIENT_WORDS = {2: "twice", 3: "three times"}


def onestep_item(rng: random.Random, item_id: str) -> dict[str, Any]:
    for _attempt in range(10_000):
        names = random_variable_names(rng, 5)
        # Two literals, three derived distractors that reference the *other* literal,
        # so binding the queried name matters. Layout order is shuffled per item.
        target_base = rng.randint(20, 99)
        other_base = rng.randint(20, 99)
        if other_base == target_base:
            continue
        coefficient = rng.choice((2, 2, 2, 3))  # released "easy" set is mostly "twice"
        constant = rng.randint(1, 30)
        operation = rng.choice(("plus", "minus"))
        product = coefficient * target_base
        answer = product + constant if operation == "plus" else product - constant

        distractor_values: list[int] = []
        distractor_defs: list[str] = []
        for _ in range(3):
            c = rng.choice((2, 3))
            k = rng.randint(1, 30)
            op = rng.choice(("plus", "minus"))
            value = c * other_base + k if op == "plus" else c * other_base - k
            distractor_values.append(value)
            distractor_defs.append(
                f"{COEFFICIENT_WORDS[c]} the number for {names[1]} {op} {k}"
            )

        literals = {target_base, other_base, constant, coefficient}
        hidden = [product, answer]
        if (
            answer <= 0
            or answer >= 1000
            or product in literals
            or answer in literals
            or answer == product
            or answer in distractor_values
            or product in distractor_values
            or len(set(distractor_values)) != 3
        ):
            continue

        definitions: list[list[Any]] = [
            [names[0], target_base],
            [names[1], other_base],
            [names[2], distractor_defs[0]],
            [names[3], distractor_defs[1]],
            [names[4], distractor_defs[2]],
        ]
        rng.shuffle(definitions)
        # A derived definition must not precede the literal it references.
        order = {name: index for index, (name, _) in enumerate(definitions)}
        if any(order[names[1]] > order[names[i]] for i in (2, 3, 4)):
            continue

        trace = {
            "base_value": str(target_base),
            "first_product": str(product),
            "answer": str(answer),
        }
        return {
            "id": item_id,
            "type": "onestep_var_binding",
            "chain_len": 0,
            "num_terms": 5,
            "definitions": definitions,
            "queried_term": names[0],
            "queried_value": target_base,
            "coefficient": coefficient,
            "operation": operation,
            "constant": constant,
            "question": (
                f"What is {COEFFICIENT_WORDS[coefficient]} the number for {names[0]} "
                f"{operation} {constant}?"
            ),
            "answer": answer,
            "expected_intermediates": trace,
            "highlight_forms": {label: [surface] for label, surface in trace.items()},
        }
    raise RuntimeError("failed to generate one-step variable-binding item")


def build(seed: int, count: int) -> dict[str, Any]:
    rng = random.Random(seed)
    few_shot = [onestep_item(rng, f"onestep_fewshot_{i}") for i in range(5)]
    for item in few_shot:
        item.pop("id")
    examples = [onestep_item(rng, f"varbind_onestep_{i:04d}") for i in range(count)]
    config = common(
        "variable_binding",
        {
            "kind": "deterministic synthetic one-step variable binding (chain_len=0)",
            "seed": seed,
            "selection": f"{count} held-out examples and 5 disjoint few-shots",
            "probe_rationale": (
                "Released chain_len=1 items are at floor for open models up to 9B in "
                "direct-answer mode. This keeps the released language, five-definition "
                "layout, and derived-expression distractors, but queries a literal "
                "variable so the answer needs one hidden affine step. Intended to place "
                "small models in the 30-80% band where a filler effect is measurable."
            ),
        },
    )
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("configs"))
    parser.add_argument("--seed", type=int, default=90211)
    parser.add_argument("--count", type=int, default=50)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    config = build(args.seed, args.count)
    write_config(args.output_dir, "varbind_onestep_dot_length_sweep.json", config)
    pre = copy.deepcopy(config)
    pre["task_type"] = "variable_binding_pre_filler"
    pre["filler_lengths"] = [0, 50]
    pre["source"]["selection"] += "; placement control with identical dots before the definitions/question"
    write_config(args.output_dir, "varbind_onestep_pre_question_k50_control.json", pre)


if __name__ == "__main__":
    main()
