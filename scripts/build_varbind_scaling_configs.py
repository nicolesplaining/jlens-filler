#!/usr/bin/env python3
"""Build held-out and exact-layout configs for scaling the varbind study.

The first stage takes a held-out slice of the released dataset.  The second
stage chooses templates rescued by a requested filler length and creates a
family of counterfactuals that differ only in the numeric literal feeding the
queried variable.  The final stages select within-family donor/target pairs or
emit one behavior-resonance example at a requested filler length.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

from build_algorithm_probe_configs import (
    COEFFICIENTS,
    RELEASED_REVISION,
    SANITY_PROMPTS,
    derive_varbind_targets,
)
from select_varbind_deep_dive import assign_controls


EXPRESSION = re.compile(
    r"^(twice|three times|four times|five times) the number for "
    r"([a-z]+) (plus|minus) (\d+)$"
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def keyed_text(value: str) -> tuple[str, str]:
    key, separator, text = value.partition("=")
    if not separator or not key or not text:
        raise argparse.ArgumentTypeError("expected NAME=TOKEN_SURFACE")
    return key, text


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(path)


def decorate(raw: dict[str, Any], example_id: str) -> dict[str, Any]:
    item = copy.deepcopy(raw)
    item["id"] = example_id
    item["expected_intermediates"] = derive_varbind_targets(item)
    item["highlight_forms"] = {
        label: [surface]
        for label, surface in item["expected_intermediates"].items()
    }
    return item


def common_config(
    *, examples: list[dict[str, Any]], few_shot: list[dict[str, Any]], source: dict[str, Any]
) -> dict[str, Any]:
    return {
        "seed": 42,
        "task_type": "variable_binding",
        "filler_type": "dots",
        "filler_lengths": [0, 5, 10, 25, 50, 100],
        "source": source,
        "sanity_prompts": SANITY_PROMPTS,
        "few_shot": few_shot,
        "examples": examples,
    }


def build_screen(args: argparse.Namespace) -> None:
    dataset = read_json(args.dataset)
    stop = args.start + args.count
    raw_examples = dataset["examples"][args.start:stop]
    if len(raw_examples) != args.count:
        raise ValueError(
            f"requested {args.count} examples from {args.start}, found {len(raw_examples)}"
        )
    examples = [
        decorate(raw, f"varbind_heldout_{int(raw['idx']):04d}")
        for raw in raw_examples
    ]
    output = common_config(
        examples=examples,
        few_shot=dataset["few_shot_examples"][:5],
        source={
            "repository": "https://github.com/kaleybrauer/filler-token-reasoning",
            "revision": RELEASED_REVISION,
            "path": "data/chained_var_binding_easy_dataset.json",
            "selection": (
                f"held-out released examples [{args.start}, {stop}); disjoint from "
                "the original first-50 exploration"
            ),
            "probe_rationale": (
                "Behavior-gate independent variable-binding templates before any "
                "representational or causal analysis."
            ),
        },
    )
    write_json(args.output, output)


def rescued_ids(sweep: dict[str, Any], filler_length: int) -> list[str]:
    length = str(filler_length)
    if filler_length not in map(int, sweep["filler_lengths"]):
        raise ValueError(f"filler length {filler_length} is absent from sweep")
    return [
        row["id"]
        for row in sweep["examples"]
        if not row["conditions"]["0"]["correct"]
        and row["conditions"][length]["correct"]
    ]


def varied_term(template: dict[str, Any]) -> str:
    definitions = dict(template["definitions"])
    query_definition = str(definitions[str(template["queried_term"])])
    match = EXPRESSION.fullmatch(query_definition)
    if match is None:
        raise ValueError(f"cannot parse queried definition: {query_definition!r}")
    term = match.group(2)
    if not isinstance(definitions.get(term), int):
        raise ValueError(f"queried definition does not point to a numeric term: {term}")
    return term


def counterfactual(
    template: dict[str, Any], *, family_index: int, base_term: str, base_value: int
) -> dict[str, Any]:
    item = copy.deepcopy(template)
    changed = False
    for definition in item["definitions"]:
        if definition[0] == base_term:
            definition[1] = base_value
            changed = True
            break
    if not changed:
        raise ValueError(f"missing numeric base term {base_term}")

    # Recompute both derived values before calling the validating helper.
    definitions = dict(item["definitions"])
    match = EXPRESSION.fullmatch(str(definitions[str(item["queried_term"])]))
    if match is None:
        raise ValueError("cannot parse varied queried definition")
    coefficient_text, parsed_base_term, operation, constant_text = match.groups()
    if parsed_base_term != base_term:
        raise AssertionError("varied term and parsed queried base disagree")
    first_product = COEFFICIENTS[coefficient_text] * base_value
    constant = int(constant_text)
    bound_value = (
        first_product + constant if operation == "plus" else first_product - constant
    )
    second_product = int(item["coefficient"]) * bound_value
    answer = (
        second_product + int(item["constant"])
        if item["operation"] == "plus"
        else second_product - int(item["constant"])
    )
    item["queried_value"] = bound_value
    item["answer"] = answer
    targets = derive_varbind_targets(item)
    item["expected_intermediates"] = targets
    item["highlight_forms"] = {
        label: [surface] for label, surface in targets.items()
    }
    item["source_template_id"] = template["id"]
    item["counterfactual_family"] = family_index
    item["varied_term"] = base_term
    item["varied_value"] = base_value
    item["id"] = f"varbind_scale_f{family_index:02d}_{base_term}_{base_value:03d}"
    item["idx"] = item["id"]
    for key in ("tracked_controls", "control_donor_id", "behavior_cohort"):
        item.pop(key, None)
    return item


def build_families(args: argparse.Namespace) -> None:
    screen = read_json(args.screen_config)
    sweep = read_json(args.sweep)
    by_id = {item["id"]: item for item in screen["examples"]}
    candidates = rescued_ids(sweep, args.selection_length)
    if len(candidates) < args.family_count:
        raise ValueError(
            f"need {args.family_count} rescued templates, found {len(candidates)}"
        )
    selected = candidates[: args.family_count]
    values = [int(value) for value in args.base_values.split(",") if value.strip()]
    if not values or len(values) != len(set(values)):
        raise ValueError("base values must be non-empty and unique")

    examples: list[dict[str, Any]] = []
    family_metadata = []
    for family_index, example_id in enumerate(selected):
        template = by_id[example_id]
        term = varied_term(template)
        family_metadata.append(
            {
                "family": family_index,
                "source_template_id": example_id,
                "varied_term": term,
                "original_value": dict(template["definitions"])[term],
            }
        )
        examples.extend(
            counterfactual(
                template,
                family_index=family_index,
                base_term=term,
                base_value=value,
            )
            for value in values
        )

    output = common_config(
        examples=examples,
        few_shot=screen["few_shot"],
        source={
            **screen["source"],
            "selection": (
                f"{args.family_count} independent templates rescued by "
                f"k={args.selection_length}; {len(values)} exact-structure numeric "
                "counterfactuals per template"
            ),
            "families": family_metadata,
            "prompt_note": (
                "Within a family, only the numeric literal feeding the queried "
                "variable changes. Exact one-token layout is checked after official "
                "DeepSeek encoding."
            ),
        },
    )
    write_json(args.output, output)


def build_selected(args: argparse.Namespace) -> None:
    families = read_json(args.families_config)
    sweep = read_json(args.sweep)
    by_id = {item["id"]: copy.deepcopy(item) for item in families["examples"]}
    sweep_by_id = {row["id"]: row for row in sweep["examples"]}
    rescued = set(rescued_ids(sweep, args.selection_length))
    grouped: dict[int, list[dict[str, Any]]] = {}
    for example_id in rescued:
        item = by_id[example_id]
        grouped.setdefault(int(item["counterfactual_family"]), []).append(item)

    selected: list[dict[str, Any]] = []
    pairs = []
    for family in sorted(grouped):
        candidates = sorted(grouped[family], key=lambda item: int(item["varied_value"]))
        if len(candidates) < 2:
            continue
        pairs_scored = []
        for left_index, left in enumerate(candidates):
            for right in candidates[left_index + 1 :]:
                left_conditions = sweep_by_id[left["id"]]["conditions"]
                right_conditions = sweep_by_id[right["id"]]["conditions"]
                both_correct_lengths = [
                    int(length)
                    for length in sweep["filler_lengths"]
                    if int(length) > 0
                    and left_conditions[str(length)]["correct"]
                    and right_conditions[str(length)]["correct"]
                ]
                pairs_scored.append(
                    (
                        len(both_correct_lengths),
                        abs(int(right["varied_value"]) - int(left["varied_value"])),
                        left,
                        right,
                        both_correct_lengths,
                    )
                )
        _, _, target, donor, both_correct_lengths = max(
            pairs_scored, key=lambda row: (row[0], row[1])
        )
        donor["behavior_cohort"] = "rescued"
        target["behavior_cohort"] = "rescued"
        selected.extend([donor, target])
        pairs.append(
            {
                "family": family,
                "donor_id": donor["id"],
                "target_id": target["id"],
                "source_template_id": donor["source_template_id"],
                "both_correct_lengths": both_correct_lengths,
            }
        )
        if args.max_pairs is not None and len(pairs) >= args.max_pairs:
            break
    if len(pairs) < args.min_pairs:
        raise ValueError(
            f"need at least {args.min_pairs} within-family rescued pairs, found {len(pairs)}"
        )
    if args.members == "donors":
        donor_ids = {pair["donor_id"] for pair in pairs}
        selected = [item for item in selected if item["id"] in donor_ids]
    assign_controls(selected)
    output = copy.deepcopy(families)
    output.pop("filler_lengths", None)
    output["filler_length"] = args.output_filler_length
    output["examples"] = selected
    output["source"]["selection"] += (
        f"; selected {len(pairs)} exact-layout donor/target pairs with both members "
        f"wrong at k=0 and correct at k={args.selection_length}; emitted for "
        f"k={args.output_filler_length} readout/causal analysis ({args.members})"
    )
    output["source"]["selected_pairs"] = pairs
    write_json(args.output, output)


def build_example(args: argparse.Namespace) -> None:
    families = read_json(args.families_config)
    by_id = {item["id"]: copy.deepcopy(item) for item in families["examples"]}
    if args.example_id not in by_id:
        raise ValueError(f"example {args.example_id!r} is absent from family config")
    target = by_id[args.example_id]
    target_values = set(target["expected_intermediates"].values())
    control = next(
        (
            item
            for example_id, item in sorted(by_id.items())
            if example_id != args.example_id
            and not target_values & set(item["expected_intermediates"].values())
        ),
        None,
    )
    if control is None:
        raise ValueError(f"no collision-free control for {args.example_id}")
    selected = [target, control]
    assign_controls(selected)
    tracked = dict(args.tracked)
    if len(tracked) != len(args.tracked):
        raise ValueError("tracked target names must be unique")
    overlap = set(tracked) & set(target["tracked_controls"])
    if overlap:
        raise ValueError(f"tracked target names collide with controls: {sorted(overlap)}")
    target["tracked_controls"].update(tracked)
    output = copy.deepcopy(families)
    if args.all_filler_lengths:
        length_description = "all configured positive filler lengths"
    else:
        output.pop("filler_lengths", None)
        output["filler_length"] = args.filler_length
        length_description = f"k={args.filler_length}"
    output["examples"] = selected
    output["source"]["selection"] += (
        f"; singled out {args.example_id} at {length_description} for a "
        "dot-count resonance readout, plus one collision-free shuffled-value control"
    )
    output["source"]["primary_example_id"] = args.example_id
    write_json(args.output, output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    screen = subparsers.add_parser("screen")
    screen.add_argument("--dataset", type=Path, required=True)
    screen.add_argument("--start", type=int, default=50)
    screen.add_argument("--count", type=int, default=100)
    screen.add_argument("--output", type=Path, required=True)
    screen.set_defaults(func=build_screen)

    families = subparsers.add_parser("families")
    families.add_argument("--screen-config", type=Path, required=True)
    families.add_argument("--sweep", type=Path, required=True)
    families.add_argument("--selection-length", type=int, default=50)
    families.add_argument("--family-count", type=int, default=6)
    families.add_argument("--base-values", default="52,56,60,64,68,72,76,80")
    families.add_argument("--output", type=Path, required=True)
    families.set_defaults(func=build_families)

    selected = subparsers.add_parser("select")
    selected.add_argument("--families-config", type=Path, required=True)
    selected.add_argument("--sweep", type=Path, required=True)
    selected.add_argument("--selection-length", type=int, default=50)
    selected.add_argument("--output-filler-length", type=int, default=50)
    selected.add_argument("--members", choices=("both", "donors"), default="both")
    selected.add_argument("--min-pairs", type=int, default=3)
    selected.add_argument("--max-pairs", type=int, default=4)
    selected.add_argument("--output", type=Path, required=True)
    selected.set_defaults(func=build_selected)

    example = subparsers.add_parser("example")
    example.add_argument("--families-config", type=Path, required=True)
    example.add_argument("--example-id", required=True)
    lengths = example.add_mutually_exclusive_group(required=True)
    lengths.add_argument("--filler-length", type=int)
    lengths.add_argument("--all-filler-lengths", action="store_true")
    example.add_argument("--tracked", action="append", type=keyed_text, default=[])
    example.add_argument("--output", type=Path, required=True)
    example.set_defaults(func=build_example)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
