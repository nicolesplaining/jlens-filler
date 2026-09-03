#!/usr/bin/env python3
"""Synthetic chain_len=1 variable-binding items matching the released distribution.

Measured on the 155 released items (50 + 100 held-out + 5 few-shot): five
definitions per item with 1–4 literals and 1–4 derived expressions, every
coefficient "twice", constants 1–30, literals 10–99, derived expressions
referencing a literal 63% of the time and another derived variable otherwise,
the queried term at definition position 1–4 and always one hop from a literal.
Items whose definitions exactly match any released item are excluded.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from build_algorithm_probe_configs import derive_varbind_targets, random_variable_names  # noqa: E402

RELEASED = [
    "configs/varbind_easy_dot_length_sweep.json",
    "configs/varbind_heldout_050_149_dot_length_sweep.json",
]


def released_signatures() -> set[str]:
    sigs: set[str] = set()
    for path in RELEASED:
        cfg = json.loads((REPO / path).read_text())
        for item in cfg["examples"] + cfg["few_shot"]:
            sigs.add(json.dumps(item["definitions"]))
    return sigs


def make_item(rng: random.Random, item_id: str, chain_len: int = 1) -> dict[str, Any]:
    for _ in range(10_000):
        n_lit = rng.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4])  # released: 1:32, 2:63, 3:48, 4:12
        n_der = 5 - n_lit
        names = random_variable_names(rng, 5)
        values: dict[str, int] = {}
        definitions: list[list[Any]] = []
        literal_names: list[str] = []
        derived_src: dict[str, str] = {}
        # Layout: literals and derived interleaved, every derived after its source.
        rest = ["L"] * (n_lit - 1) + ["D"] * n_der
        rng.shuffle(rest)
        slots = ["L"] + rest  # first definition is always a literal
        ok = True
        for slot, name in zip(slots, names):
            if slot == "L":
                v = rng.randint(10, 99)
                values[name] = v; literal_names.append(name); definitions.append([name, v])
            else:
                derived_names = [n for n in values if n not in literal_names]
                if derived_names and rng.random() < (0.6 if chain_len == 1 else 0.85):  # 0.6 lands near the released 37% derived->derived share
                    candidates = derived_names  # released: 37% of derived refs point at another derived variable
                else:
                    candidates = [n for n in values if n in literal_names]
                if not candidates:
                    ok = False; break
                src = rng.choice(candidates)
                const = rng.randint(1, 30); op = rng.choice(("plus", "minus"))
                v = 2 * values[src] + const if op == "plus" else 2 * values[src] - const
                if v <= 0 or v >= 1000:
                    ok = False; break
                values[name] = v; derived_src[name] = src
                definitions.append([name, f"twice the number for {src} {op} {const}"])
        if not ok:
            continue
        # Queried term: derived, exactly ``chain_len`` hops from a literal, not at position 0.
        def hops(n: str) -> int:
            return 0 if n in literal_names else 1 + hops(derived_src[n])
        q_candidates = [n for n in derived_src if hops(n) == chain_len and names.index(n) >= 1]
        if not q_candidates:
            continue
        q = rng.choice(q_candidates)
        q_const = rng.randint(1, 30); q_op = rng.choice(("plus", "minus"))
        answer = 2 * values[q] + q_const if q_op == "plus" else 2 * values[q] - q_const
        if answer <= 0 or answer >= 1000:
            continue
        if len(set(values.values())) != len(values):
            continue
        item = {
            "id": item_id,
            "type": "chained_var_binding",
            "definitions": definitions,
            "queried_term": q,
            "queried_value": values[q],
            "coefficient": 2,
            "operation": q_op,
            "constant": q_const,
            "num_terms": 5,
            "chain_len": chain_len,
            "question": f"What is twice the number for {q} {q_op} {q_const}?",
            "answer": answer,
        }
        if chain_len == 1:
            item["expected_intermediates"] = derive_varbind_targets(item)  # independent recheck against Nicole's derivation
        else:
            # Walk the chain from the literal to the queried term, then the final question op.
            chain = [q]
            while chain[-1] not in literal_names:
                chain.append(derived_src[chain[-1]])
            chain.reverse()  # literal ... q
            trace: dict[str, str] = {"base_value": str(values[chain[0]])}
            for hop, name in enumerate(chain[1:], start=1):
                trace[f"hop{hop}_product"] = str(2 * values[derived_src[name]])
                trace[f"hop{hop}_value"] = str(values[name])
            trace["final_product"] = str(2 * values[q])
            trace["answer"] = str(answer)
            assert int(trace[f"hop{chain_len}_value"]) == values[q]
            item["expected_intermediates"] = trace
        item["highlight_forms"] = {k: [v] for k, v in item["expected_intermediates"].items()}
        return item
    raise RuntimeError("generation failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=4000)
    parser.add_argument("--seed", type=int, default=20260903)
    parser.add_argument("--output", type=Path, default=Path("data/varbind_sft_train.jsonl"))
    parser.add_argument("--chain-len", type=int, default=1)
    parser.add_argument("--eval-config", type=Path, default=None,
                        help="also write a held-out sweep config (5 few-shot + --eval-count items, disjoint from training)")
    parser.add_argument("--eval-count", type=int, default=100)
    parser.add_argument("--eval-seed", type=int, default=777)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    banned = released_signatures()
    seen: set[str] = set()
    items = []
    while len(items) < args.count:
        item = make_item(rng, f"varbind_sft_{len(items):05d}", args.chain_len)
        sig = json.dumps(item["definitions"])
        if sig in banned or sig in seen:
            continue
        seen.add(sig); items.append(item)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        for item in items:
            f.write(json.dumps(item) + "\n")
    print(f"wrote {len(items)} items to {args.output} (excluded {len(banned)} released signatures)")
    if args.eval_config:
        erng = random.Random(args.eval_seed)
        evals = []
        while len(evals) < args.eval_count + 5:
            item = make_item(erng, f"varbind_c{args.chain_len}_heldout_{max(0, len(evals) - 5):04d}", args.chain_len)
            sig = json.dumps(item["definitions"])
            if sig in banned or sig in seen:
                continue
            seen.add(sig); evals.append(item)
        few_shot = evals[:5]
        for f in few_shot:
            f.pop("id")
        base_cfg = json.loads((REPO / RELEASED[0]).read_text())
        cfg = {k: v for k, v in base_cfg.items() if k in ("seed", "task_type", "filler_type", "filler_lengths", "sanity_prompts")}
        cfg["source"] = {"kind": f"synthetic chain_len={args.chain_len} variable binding", "seed": args.eval_seed,
                         "selection": f"{args.eval_count} held-out items and 5 disjoint few-shots, disjoint from the seed-{args.seed} training set"}
        cfg["few_shot"] = few_shot
        cfg["examples"] = evals[5:]
        args.eval_config.write_text(json.dumps(cfg, indent=2) + "\n")
        print(f"wrote eval config {args.eval_config} ({len(cfg['examples'])} items)")


if __name__ == "__main__":
    main()
