#!/usr/bin/env python3
"""Build deterministic configs for algorithm/parallelism filler probes.

The released datasets are read from a pinned checkout of
kaleybrauer/filler-token-reasoning. Novel three-fact and pointer-chase probes
are generated deterministically and record their construction in each config.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import re
from pathlib import Path
from typing import Any


RELEASED_REVISION = "4ba4c75d5d9f04248749ec46b8bed8661b746715"
FILLER_LENGTHS = [0, 5, 10, 25, 50, 100]
SANITY_PROMPTS = [
    {
        "id": "capital",
        "messages": [{"role": "user", "content": "The capital of France is"}],
    },
    {
        "id": "arithmetic",
        "messages": [
            {"role": "user", "content": "Complete with only the answer: 17 + 25 ="}
        ],
    },
    {
        "id": "chinese",
        "messages": [{"role": "user", "content": "用一个词回答：中国的首都是"}],
    },
]

COEFFICIENTS = {
    "twice": 2,
    "three times": 3,
    "four times": 4,
    "five times": 5,
}
CHAIN_PATTERN = re.compile(
    r"^(twice|three times|four times|five times) the number for "
    r"([a-z]+) (plus|minus) (\d+)$"
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_config(output_dir: Path, name: str, config: dict[str, Any]) -> None:
    path = output_dir / name
    path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n")
    print(path)


def common(task_type: str, source: dict[str, Any]) -> dict[str, Any]:
    return {
        "seed": 42,
        "task_type": task_type,
        "filler_type": "dots",
        "filler_lengths": FILLER_LENGTHS,
        "source": source,
        "sanity_prompts": SANITY_PROMPTS,
    }


def derive_varbind_targets(item: dict[str, Any]) -> dict[str, str]:
    definitions = {str(name): value for name, value in item["definitions"]}
    queried_term = str(item["queried_term"])
    match = CHAIN_PATTERN.fullmatch(str(definitions[queried_term]))
    if match is None:
        raise ValueError(f"cannot parse definition for {queried_term}")
    coefficient_text, base_term, operation, constant_text = match.groups()
    base_value = int(definitions[base_term])
    first_product = COEFFICIENTS[coefficient_text] * base_value
    constant = int(constant_text)
    bound_value = first_product + constant if operation == "plus" else first_product - constant
    if bound_value != int(item["queried_value"]):
        raise ValueError(f"queried value mismatch for item {item.get('idx')}")
    second_product = int(item["coefficient"]) * bound_value
    answer = (
        second_product + int(item["constant"])
        if item["operation"] == "plus"
        else second_product - int(item["constant"])
    )
    if answer != int(item["answer"]):
        raise ValueError(f"answer mismatch for item {item.get('idx')}")
    return {
        "base_value": str(base_value),
        "first_product": str(first_product),
        "bound_value": str(bound_value),
        "second_product": str(second_product),
        "answer": str(answer),
    }


def build_varbind(source_dir: Path) -> dict[str, Any]:
    path = source_dir / "data/chained_var_binding_easy_dataset.json"
    dataset = read_json(path)
    examples = []
    for item in dataset["examples"][:50]:
        item = dict(item)
        item["id"] = f"varbind_easy_{int(item['idx']):04d}"
        item["expected_intermediates"] = derive_varbind_targets(item)
        item["highlight_forms"] = {
            label: [surface]
            for label, surface in item["expected_intermediates"].items()
        }
        examples.append(item)
    config = common(
        "variable_binding",
        {
            "repository": "https://github.com/kaleybrauer/filler-token-reasoning",
            "revision": RELEASED_REVISION,
            "path": "data/chained_var_binding_easy_dataset.json",
            "selection": "first 50 examples in released order",
            "prompt_note": (
                "Released variable-binding scaffold with the paper PDF exact-count "
                "filler suffix. Five tracked values are derived and validated from "
                "the released definitions."
            ),
        },
    )
    config["few_shot"] = dataset["few_shot_examples"][:5]
    config["examples"] = examples
    return config


def build_letter_position(source_dir: Path, dataset_name: str) -> dict[str, Any]:
    path = source_dir / f"data/{dataset_name}.json"
    dataset = read_json(path)
    is_capital = dataset_name.startswith("capital")
    examples = []
    for index, raw in enumerate(dataset["examples"][:50]):
        item = dict(raw)
        entity = str(item["intermediate"] if is_capital else item["element"])
        prefix = "capital_letter" if is_capital else "element_letter"
        item["id"] = f"{prefix}_{index:04d}"
        item["expected_intermediates"] = {
            "retrieved_name": entity,
            "answer_letter": str(item["answer"]),
        }
        item["highlight_forms"] = {
            "retrieved_name": [entity],
            "answer_letter": [str(item["answer"])],
        }
        examples.append(item)
    config = common(
        "letter_position",
        {
            "repository": "https://github.com/kaleybrauer/filler-token-reasoning",
            "revision": RELEASED_REVISION,
            "path": f"data/{dataset_name}.json",
            "selection": "first 50 examples in released order",
            "prompt_note": (
                "Released letter-position scaffold with the paper PDF exact-count "
                "filler suffix."
            ),
        },
    )
    config["few_shot"] = dataset["few_shot_examples"][:5]
    config["examples"] = examples
    return config


def atomic_fact_pool(source_dir: Path) -> list[tuple[str, int]]:
    dataset = read_json(source_dir / "data/2fact_addition_dataset.json")
    pool: list[tuple[str, int]] = []
    seen: set[str] = set()
    for section in (dataset["few_shot_facts"], dataset["examples"]):
        for item in section:
            for index in (1, 2):
                phrase = str(item[f"fact_phrase_{index}"])
                if phrase not in seen:
                    seen.add(phrase)
                    pool.append((phrase, int(item[f"fact_value_{index}"])))
    return pool


def three_fact_item(group: int, permutation: int, facts: list[tuple[str, int]]) -> dict[str, Any]:
    ordered = facts[permutation:] + facts[:permutation]
    values = [value for _, value in ordered]
    item: dict[str, Any] = {
        "id": f"three_fact_g{group:02d}_p{permutation}",
        "permutation_group": group,
        "cyclic_permutation": permutation,
        "answer": sum(values),
        "expected_intermediates": {
            "fact_1": str(values[0]),
            "fact_2": str(values[1]),
            "fact_3": str(values[2]),
            "prefix_sum_12": str(values[0] + values[1]),
            "sum": str(sum(values)),
        },
    }
    for index, (phrase, value) in enumerate(ordered, start=1):
        item[f"fact_phrase_{index}"] = phrase
        item[f"fact_value_{index}"] = value
    item["highlight_forms"] = {
        label: [surface] for label, surface in item["expected_intermediates"].items()
    }
    return item


def build_three_fact(source_dir: Path) -> dict[str, Any]:
    pool = atomic_fact_pool(source_dir)
    if len(pool) < 75:
        raise ValueError(f"need at least 75 unique atomic facts, found {len(pool)}")
    few_shot = []
    for group in range(5):
        facts = pool[group * 3 : group * 3 + 3]
        item = three_fact_item(-1, 0, facts)
        item.pop("id")
        item.pop("permutation_group")
        item.pop("cyclic_permutation")
        few_shot.append(item)
    examples = []
    offset = 15
    for group in range(20):
        facts = pool[offset + group * 3 : offset + group * 3 + 3]
        for permutation in range(3):
            examples.append(three_fact_item(group, permutation, facts))
    config = common(
        "addition",
        {
            "repository": "https://github.com/kaleybrauer/filler-token-reasoning",
            "revision": RELEASED_REVISION,
            "path": "data/2fact_addition_dataset.json",
            "selection": (
                "deterministic unique atomic-fact pool; 5 disjoint few-shots and "
                "20 held-out triples, each in three cyclic orders"
            ),
            "probe_rationale": (
                "Three independent retrievals distinguish concurrent fact recovery "
                "from an order-dependent prefix-sum algorithm."
            ),
        },
    )
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def make_cycle_mapping(rng: random.Random, size: int) -> tuple[list[list[int]], list[int]]:
    cycle = list(range(size))
    rng.shuffle(cycle)
    mapping = {cycle[index]: cycle[(index + 1) % size] for index in range(size)}
    table_order = list(range(size))
    rng.shuffle(table_order)
    return [[source, mapping[source]] for source in table_order], cycle


def pointer_item(rng: random.Random, item_id: str, time_steps: int) -> dict[str, Any]:
    mapping_entries, cycle = make_cycle_mapping(rng, 12)
    mapping = dict(mapping_entries)
    start = rng.choice(cycle)
    value = start
    trace = []
    for _ in range(time_steps):
        value = mapping[value]
        trace.append(value)
    return {
        "id": item_id,
        "mapping": mapping_entries,
        "start": start,
        "time_steps": time_steps,
        "answer": value,
        "expected_intermediates": {
            f"x{index}": str(result) for index, result in enumerate(trace, start=1)
        },
        "highlight_forms": {
            f"x{index}": [str(result)] for index, result in enumerate(trace, start=1)
        },
        "cycle_for_validation_only": cycle,
    }


def build_pointer_chase() -> dict[str, Any]:
    rng = random.Random(91377)
    few_shot = [
        pointer_item(rng, f"pointer_fewshot_{index}", steps)
        for index, steps in enumerate((2, 4, 8))
    ]
    examples = [
        pointer_item(rng, f"pointer_t{steps}_{index:02d}", steps)
        for steps in (1, 2, 4, 8)
        for index in range(10)
    ]
    config = common(
        "pointer_chase",
        {
            "kind": "deterministic synthetic single-cycle permutation tables",
            "seed": 91377,
            "domain_size": 12,
            "selection": "10 examples at each T in {1,2,4,8}; 3 few-shots",
            "probe_rationale": (
                "A learned serial lookup predicts roughly one-hop-at-a-time onset; "
                "pointer jumping predicts doubling (x1, x2, x4, x8) across layer bands. "
                "All table values are visible, so claims require cross-example and "
                "shuffled-label controls."
            ),
        },
    )
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def arithmetic_trace(item: dict[str, Any]) -> dict[str, str]:
    values = {str(name): int(value) for name, value in item["inputs"]}
    trace: dict[str, str] = {}
    for output, left, operator, right in item["operations"]:
        if operator == "add":
            value = values[left] + values[right]
        elif operator == "subtract":
            value = values[left] - values[right]
        elif operator == "multiply":
            value = values[left] * values[right]
        else:
            raise ValueError(f"unknown arithmetic operator: {operator}")
        values[output] = value
        trace[output] = str(value)
    return trace


def arithmetic_item(
    rng: random.Random, item_id: str, topology: str
) -> dict[str, Any]:
    """Generate a seven-operation program with nonliteral, unique intermediates."""
    for _attempt in range(10_000):
        if topology == "balanced_tree":
            raw = [rng.randint(2, 12) for _ in range(8)]
            # Keep both subtractive branches positive.
            raw[2], raw[3] = max(raw[2], raw[3]), min(raw[2], raw[3])
            raw[6], raw[7] = max(raw[6], raw[7]), min(raw[6], raw[7])
            if raw[2] == raw[3] or raw[6] == raw[7]:
                continue
            names = list("abcdefgh")
            operations = [
                ["p1", "a", "add", "b"],
                ["p2", "c", "subtract", "d"],
                ["p3", "e", "add", "f"],
                ["p4", "g", "subtract", "h"],
                ["m1", "p1", "multiply", "p2"],
                ["m2", "p3", "multiply", "p4"],
                ["y", "m1", "add", "m2"],
            ]
        elif topology == "serial_chain":
            raw = [rng.randint(2, 9) for _ in range(8)]
            names = ["x0", "a", "b", "c", "d", "e", "f", "g"]
            # Two modest multipliers keep all targets compact and tokenizable.
            raw[2] = rng.choice([2, 3])
            raw[5] = rng.choice([2, 3])
            operations = [
                ["x1", "x0", "add", "a"],
                ["x2", "x1", "multiply", "b"],
                ["x3", "x2", "subtract", "c"],
                ["x4", "x3", "add", "d"],
                ["x5", "x4", "multiply", "e"],
                ["x6", "x5", "subtract", "f"],
                ["y", "x6", "add", "g"],
            ]
        else:
            raise ValueError(f"unknown topology: {topology}")

        inputs = [[name, value] for name, value in zip(names, raw)]
        item = {"inputs": inputs, "operations": operations}
        trace = arithmetic_trace(item)
        intermediate_values = list(map(int, trace.values()))
        if (
            min(intermediate_values) <= 0
            or max(intermediate_values) >= 1000
            or len(set(intermediate_values)) != len(intermediate_values)
            or set(intermediate_values) & set(raw)
        ):
            continue
        item.update(
            {
                "id": item_id,
                "topology": topology,
                "query": "y",
                "answer": intermediate_values[-1],
                "expected_intermediates": trace,
                "highlight_forms": {
                    label: [surface] for label, surface in trace.items()
                },
            }
        )
        return item
    raise RuntimeError(f"failed to generate a valid {topology} item")


def build_arithmetic_programs() -> dict[str, Any]:
    rng = random.Random(62217)
    few_shot = []
    for index, topology in enumerate(
        ("balanced_tree", "serial_chain", "balanced_tree", "serial_chain")
    ):
        item = arithmetic_item(rng, f"arithmetic_fewshot_{index}", topology)
        item.pop("id")
        few_shot.append(item)
    examples = [
        arithmetic_item(rng, f"arithmetic_tree_{index:03d}", "balanced_tree")
        for index in range(24)
    ] + [
        arithmetic_item(rng, f"arithmetic_serial_{index:03d}", "serial_chain")
        for index in range(24)
    ]
    config = common(
        "arithmetic_program",
        {
            "kind": "deterministic synthetic seven-operation integer programs",
            "seed": 62217,
            "selection": (
                "24 balanced-tree and 24 matched left-deep serial programs; "
                "4 mixed-topology few-shots"
            ),
            "probe_rationale": (
                "The balanced program has four independent first-level branches, "
                "then two merges, then a root. The serial control has seven strict "
                "dependencies. Both expose eight literal inputs and seven operation "
                "lines. Every hidden intermediate is unique and absent from the "
                "target's literal inputs. Concurrent branch onsets followed by merge "
                "onsets would support tree-parallel execution; a depth-ordered state "
                "ladder would support serial execution."
            ),
        },
    )
    config["filler_lengths"] = [0, 5, 10, 25, 50]
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def random_variable_names(rng: random.Random, count: int) -> list[str]:
    names: list[str] = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(names) < count:
        name = "".join(rng.choice(alphabet) for _ in range(3))
        if name not in names:
            names.append(name)
    return names


def branching_varbind_item(rng: random.Random, item_id: str) -> dict[str, Any]:
    coefficient_words = {2: "twice", 3: "three times", 4: "four times"}
    for _attempt in range(10_000):
        names = random_variable_names(rng, 4)
        base_a, base_b = rng.randint(8, 39), rng.randint(8, 39)
        coefficient_a, coefficient_b = rng.randint(2, 4), rng.randint(2, 4)
        constant_a, constant_b = rng.randint(1, 9), rng.randint(1, 9)
        operation_a, operation_b = rng.choice(("plus", "minus")), rng.choice(
            ("plus", "minus")
        )
        product_a, product_b = coefficient_a * base_a, coefficient_b * base_b
        value_a = (
            product_a + constant_a
            if operation_a == "plus"
            else product_a - constant_a
        )
        value_b = (
            product_b + constant_b
            if operation_b == "plus"
            else product_b - constant_b
        )
        answer = value_a + value_b
        literals = {base_a, base_b, constant_a, constant_b, coefficient_a, coefficient_b}
        hidden = [product_a, value_a, product_b, value_b, answer]
        if (
            min(hidden) <= 0
            or max(hidden) >= 1000
            or len(set(hidden)) != len(hidden)
            or set(hidden) & literals
        ):
            continue
        definitions: list[list[Any]] = [
            [names[0], base_a],
            [
                names[1],
                f"{coefficient_words[coefficient_a]} the number for {names[0]} "
                f"{operation_a} {constant_a}",
            ],
            [names[2], base_b],
            [
                names[3],
                f"{coefficient_words[coefficient_b]} the number for {names[2]} "
                f"{operation_b} {constant_b}",
            ],
        ]
        trace = {
            "branch_a_product": str(product_a),
            "branch_a_value": str(value_a),
            "branch_b_product": str(product_b),
            "branch_b_value": str(value_b),
            "answer": str(answer),
        }
        return {
            "id": item_id,
            "topology": "parallel_branches",
            "definitions": definitions,
            "question": (
                f"What is the number for {names[1]} plus the number for {names[3]}?"
            ),
            "answer": answer,
            "expected_intermediates": trace,
            "highlight_forms": {
                label: [surface] for label, surface in trace.items()
            },
            "construction_for_validation": {
                "branch_a": {
                    "base": base_a,
                    "coefficient": coefficient_a,
                    "operation": operation_a,
                    "constant": constant_a,
                },
                "branch_b": {
                    "base": base_b,
                    "coefficient": coefficient_b,
                    "operation": operation_b,
                    "constant": constant_b,
                },
                "merge": "addition",
            },
        }
    raise RuntimeError("failed to generate branching variable-binding item")


def build_branching_varbind() -> dict[str, Any]:
    rng = random.Random(74193)
    few_shot = [
        branching_varbind_item(rng, f"branch_varbind_fewshot_{index}")
        for index in range(5)
    ]
    for item in few_shot:
        item.pop("id")
    examples = [
        branching_varbind_item(rng, f"branch_varbind_{index:03d}")
        for index in range(36)
    ]
    config = common(
        "variable_binding",
        {
            "kind": "deterministic synthetic two-branch variable-binding DAG",
            "seed": 74193,
            "selection": "36 held-out examples and 5 disjoint few-shots",
            "probe_rationale": (
                "This retains the released variable-binding language, where dots "
                "already have a strong behavioral effect, but introduces two "
                "independent affine branches followed by an addition merge. If the "
                "model exploits token-position width, the two branch values should "
                "become decodable concurrently and the merged answer later."
            ),
        },
    )
    config["filler_lengths"] = [0, 5, 10, 25, 50]
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def branching_varbind_depth2_item(
    rng: random.Random, item_id: str
) -> dict[str, Any]:
    coefficient_words = {2: "twice", 3: "three times"}
    for _attempt in range(20_000):
        names = random_variable_names(rng, 6)
        bases = [rng.randint(5, 18), rng.randint(5, 18)]
        coefficients = [rng.randint(2, 3) for _ in range(4)]
        constants = [rng.randint(1, 7) for _ in range(4)]
        operations = [rng.choice(("plus", "minus")) for _ in range(4)]

        hidden: list[int] = []
        branch_values: list[list[int]] = []
        cursor = 0
        for base in bases:
            value = base
            stages: list[int] = []
            for _ in range(2):
                coefficient = coefficients[cursor]
                constant = constants[cursor]
                operation = operations[cursor]
                product = coefficient * value
                value = product + constant if operation == "plus" else product - constant
                stages.extend([product, value])
                hidden.extend([product, value])
                cursor += 1
            branch_values.append(stages)
        answer = branch_values[0][-1] + branch_values[1][-1]
        hidden.append(answer)
        literals = set(bases + coefficients + constants)
        if (
            min(hidden) <= 0
            or max(hidden) >= 1000
            or len(set(hidden)) != len(hidden)
            or set(hidden) & literals
        ):
            continue

        definitions: list[list[Any]] = [[names[0], bases[0]]]
        for index, (source, output) in enumerate(
            ((names[0], names[1]), (names[1], names[2]))
        ):
            definitions.append(
                [
                    output,
                    f"{coefficient_words[coefficients[index]]} the number for {source} "
                    f"{operations[index]} {constants[index]}",
                ]
            )
        definitions.append([names[3], bases[1]])
        for index, (source, output) in enumerate(
            ((names[3], names[4]), (names[4], names[5])), start=2
        ):
            definitions.append(
                [
                    output,
                    f"{coefficient_words[coefficients[index]]} the number for {source} "
                    f"{operations[index]} {constants[index]}",
                ]
            )
        trace = {
            "branch_a_product_1": str(branch_values[0][0]),
            "branch_a_value_1": str(branch_values[0][1]),
            "branch_a_product_2": str(branch_values[0][2]),
            "branch_a_value_2": str(branch_values[0][3]),
            "branch_b_product_1": str(branch_values[1][0]),
            "branch_b_value_1": str(branch_values[1][1]),
            "branch_b_product_2": str(branch_values[1][2]),
            "branch_b_value_2": str(branch_values[1][3]),
            "answer": str(answer),
        }
        return {
            "id": item_id,
            "topology": "parallel_depth2",
            "definitions": definitions,
            "question": (
                f"What is the number for {names[2]} plus the number for {names[5]}?"
            ),
            "answer": answer,
            "expected_intermediates": trace,
            "highlight_forms": {
                label: [surface] for label, surface in trace.items()
            },
            "construction_for_validation": {
                "bases": bases,
                "coefficients": coefficients,
                "constants": constants,
                "operations": operations,
                "merge": "addition",
            },
        }
    raise RuntimeError("failed to generate depth-2 branching variable-binding item")


def build_branching_varbind_depth2() -> dict[str, Any]:
    rng = random.Random(274193)
    few_shot = [
        branching_varbind_depth2_item(rng, f"branch_depth2_fewshot_{index}")
        for index in range(5)
    ]
    for item in few_shot:
        item.pop("id")
    examples = [
        branching_varbind_depth2_item(rng, f"branch_depth2_{index:03d}")
        for index in range(40)
    ]
    config = common(
        "variable_binding",
        {
            "kind": "deterministic two-branch depth-2 variable-binding DAG",
            "seed": 274193,
            "selection": "40 held-out examples and 5 disjoint few-shots",
            "behavioral_gate": (
                "Do not extract lens readouts unless at least one positive dot length "
                "has helped_count > hurt_count and >= 0.10 absolute accuracy gain."
            ),
            "probe_rationale": (
                "The depth-1 branch task saturated and showed no filler benefit. "
                "This calibrated extension gives each independent branch two affine "
                "steps before the addition merge, while retaining the released "
                "dot-responsive variable-binding language."
            ),
        },
    )
    config["filler_lengths"] = [0, 10, 25, 50]
    config["few_shot"] = few_shot
    config["examples"] = examples
    return config


def selected_extraction_config(
    sweep_config: dict[str, Any], filler_length: int, example_ids: list[str]
) -> dict[str, Any]:
    config = copy.deepcopy(sweep_config)
    config.pop("filler_lengths")
    config["filler_length"] = filler_length
    selected = [
        example for example in config["examples"] if example["id"] in example_ids
    ]
    found = {example["id"] for example in selected}
    missing = set(example_ids) - found
    if missing:
        raise ValueError(f"selected IDs absent from sweep: {sorted(missing)}")
    config["examples"] = selected
    config["source"]["selection"] += (
        f"; readout selection at k={filler_length}: " + ", ".join(example_ids)
    )
    return config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("tmp/filler-token-reasoning"),
    )
    parser.add_argument("--output-dir", type=Path, default=Path("configs"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    varbind = build_varbind(args.source_dir)
    write_config(
        args.output_dir,
        "varbind_easy_dot_length_sweep.json",
        varbind,
    )
    varbind_pre = copy.deepcopy(varbind)
    varbind_pre["task_type"] = "variable_binding_pre_filler"
    varbind_pre["filler_lengths"] = [0, 50]
    varbind_pre["source"]["selection"] += (
        "; causal placement control with identical dots before all target definitions/question"
    )
    write_config(
        args.output_dir,
        "varbind_pre_question_k50_control.json",
        varbind_pre,
    )
    write_config(
        args.output_dir,
        "varbind_jlens_k50_selected.json",
        selected_extraction_config(
            varbind,
            50,
            [
                "varbind_easy_0035",
                "varbind_easy_0002",
                "varbind_easy_0000",
                "varbind_easy_0037",
            ],
        ),
    )
    for filler_length in (5, 25):
        write_config(
            args.output_dir,
            f"varbind_jlens_k{filler_length}_threshold.json",
            selected_extraction_config(
                varbind, filler_length, ["varbind_easy_0035"]
            ),
        )
    write_config(
        args.output_dir,
        "varbind_jlens_k100_boundary.json",
        selected_extraction_config(varbind, 100, ["varbind_easy_0037"]),
    )
    element_letter = build_letter_position(
        args.source_dir, "element_letter_positions"
    )
    write_config(
        args.output_dir,
        "element_letter_dot_length_sweep.json",
        element_letter,
    )
    element_selected = selected_extraction_config(
        element_letter,
        10,
        ["element_letter_0000", "element_letter_0044"],
    )
    rubidium = next(
        example
        for example in element_selected["examples"]
        if example["id"] == "element_letter_0044"
    )
    rubidium["expected_intermediates"] = {
        "retrieved_prefix": "Rub",
        "retrieved_suffix": "idium",
        "answer_letter": "u",
    }
    rubidium["highlight_forms"] = {
        label: [surface]
        for label, surface in rubidium["expected_intermediates"].items()
    }
    write_config(
        args.output_dir,
        "element_letter_jlens_k10_selected.json",
        element_selected,
    )
    write_config(
        args.output_dir,
        "capital_letter_dot_length_sweep.json",
        build_letter_position(args.source_dir, "capital_letter_position"),
    )
    three_fact = build_three_fact(args.source_dir)
    write_config(
        args.output_dir,
        "three_fact_order_dot_length_sweep.json",
        three_fact,
    )
    write_config(
        args.output_dir,
        "three_fact_order_jlens_g14_k50.json",
        selected_extraction_config(
            three_fact,
            50,
            [
                "three_fact_g14_p0",
                "three_fact_g14_p1",
                "three_fact_g14_p2",
            ],
        ),
    )
    write_config(
        args.output_dir,
        "pointer_chase_dot_length_sweep.json",
        build_pointer_chase(),
    )
    write_config(
        args.output_dir,
        "arithmetic_program_dot_length_sweep.json",
        build_arithmetic_programs(),
    )
    write_config(
        args.output_dir,
        "branching_varbind_dot_length_sweep.json",
        build_branching_varbind(),
    )
    write_config(
        args.output_dir,
        "branching_varbind_depth2_dot_length_sweep.json",
        build_branching_varbind_depth2(),
    )


if __name__ == "__main__":
    main()
