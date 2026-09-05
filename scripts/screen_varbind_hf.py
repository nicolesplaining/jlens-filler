#!/usr/bin/env python3
"""Behavior-first filler-dot screen for smaller Hugging Face causal LMs.

This intentionally runs no lens analysis.  A model must first show a replicated
accuracy/rank benefit from post-question dots on the same variable-binding prompts.
Only models passing that gate should receive a model-specific logit-lens follow-up.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import sys
import time
from pathlib import Path
from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from jlens_filler.prompts import build_messages, make_filler, token_variants  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--revision", default="main")
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--filler-lengths", default="0,5,10,25,50,100")
    parser.add_argument("--max-examples", type=int, default=100)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--max-new-tokens", type=int, default=4)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dtype", choices=("bfloat16", "float16"), default="bfloat16")
    parser.add_argument("--attn-implementation", default="sdpa")
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_answer(text: str) -> int | None:
    match = re.search(r"-?\d+", text)
    return int(match.group()) if match else None


def filler_token_alignment(
    tokenizer: Any, rendered: str, filler_type: str, filler_length: int
) -> dict[str, Any]:
    if filler_length == 0:
        return {"char_span": None, "token_indices": [], "tokens": []}
    surface = make_filler(filler_type, filler_length)
    marker = f"Filler: {surface}\n\nAnswer:"
    marker_start = rendered.rfind(marker)
    if marker_start < 0:
        raise AssertionError("target filler marker absent from rendered chat template")
    char_start = marker_start + len("Filler: ")
    char_end = char_start + len(surface)
    encoded = tokenizer(
        rendered,
        add_special_tokens=False,
        return_offsets_mapping=True,
    )
    indices = [
        index
        for index, (start, end) in enumerate(encoded["offset_mapping"])
        if end > char_start and start < char_end
    ]
    return {
        "char_span": [char_start, char_end],
        "token_indices": indices,
        "token_ids": [int(encoded["input_ids"][index]) for index in indices],
        "tokens": [
            tokenizer.decode([int(encoded["input_ids"][index])]) for index in indices
        ],
        "visible_filler_count": filler_length,
        "model_token_count": len(indices),
    }


def target_rank(logits: torch.Tensor, tokenizer: Any, answer: Any) -> dict[str, Any]:
    scores = logits.float().cpu()
    log_z = torch.logsumexp(scores, dim=-1)
    variants = token_variants(tokenizer, str(answer))
    ranked = []
    for variant in variants:
        item = dict(variant)
        if variant["single_token"]:
            token_id = int(variant["token_ids"][0])
            score = scores[token_id]
            item.update(
                {
                    "rank": int((scores > score).sum()) + 1,
                    "logit": float(score),
                    "log_probability": float(score - log_z),
                }
            )
            ranked.append(item)
    if not ranked:
        return {"best_rank": None, "variants": variants}
    best = min(ranked, key=lambda item: item["rank"])
    return {
        "best_rank": best["rank"],
        "best_log_probability": best["log_probability"],
        "variants": variants,
    }


def render_messages(tokenizer: Any, messages: list[dict[str, str]]) -> str:
    return tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )


def write_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


@torch.inference_mode()
def main() -> None:
    args = parse_args()
    filler_lengths = [int(value) for value in args.filler_lengths.split(",")]
    if filler_lengths != sorted(set(filler_lengths)) or min(filler_lengths) < 0:
        raise ValueError("filler lengths must be unique, increasing, and nonnegative")
    if 0 not in filler_lengths:
        raise ValueError("behavior screen requires a no-filler baseline")
    dtype = getattr(torch, args.dtype)
    tokenizer = AutoTokenizer.from_pretrained(args.model, revision=args.revision)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        revision=args.revision,
        dtype=dtype,
        attn_implementation=args.attn_implementation,
    ).to(args.device)
    model.eval()

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    examples = experiment["examples"][: args.max_examples]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "behavior-screen.json"
    output: dict[str, Any] = {
        "schema_version": 1,
        "model": args.model,
        "revision": args.revision,
        "task_type": experiment["task_type"],
        "filler_type": experiment["filler_type"],
        "filler_lengths": filler_lengths,
        "examples": [],
        "summary": {},
        "runtime": {
            "timestamp_unix": time.time(),
            "platform": platform.platform(),
            "torch": torch.__version__,
            "transformers": __import__("transformers").__version__,
            "device": args.device,
            "dtype": args.dtype,
            "examples_config_sha256": sha256(args.examples_config),
            "seed": 42,
        },
    }
    torch.manual_seed(42)

    # Length is outermost so each batch has similar prompt sizes.
    by_id: dict[str, dict[str, Any]] = {
        example["id"]: {
            "id": example["id"],
            "answer": example["answer"],
            "expected_intermediates": example.get("expected_intermediates", {}),
            "conditions": {},
        }
        for example in examples
    }
    for filler_length in filler_lengths:
        print(f"filler length {filler_length}", flush=True)
        prepared = []
        for example in examples:
            messages = build_messages(
                experiment["few_shot"],
                example,
                experiment["filler_type"],
                filler_length,
                task_type=experiment["task_type"],
            )
            rendered = render_messages(tokenizer, messages)
            alignment = filler_token_alignment(
                tokenizer, rendered, experiment["filler_type"], filler_length
            )
            prepared.append((example, rendered, alignment))

        for batch_start in range(0, len(prepared), args.batch_size):
            batch = prepared[batch_start : batch_start + args.batch_size]
            rendered_batch = [item[1] for item in batch]
            encoded = tokenizer(
                rendered_batch,
                padding=True,
                add_special_tokens=False,
                return_tensors="pt",
            ).to(args.device)
            generated = model.generate(
                **encoded,
                do_sample=False,
                max_new_tokens=args.max_new_tokens,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
                return_dict_in_generate=True,
                output_scores=True,
            )
            if not generated.scores:
                raise AssertionError("generation returned no next-token scores")
            first_logits = generated.scores[0].float()
            new_ids = generated.sequences[:, encoded["input_ids"].shape[1] :]
            completions = tokenizer.batch_decode(new_ids, skip_special_tokens=True)
            for offset, ((example, rendered, alignment), completion) in enumerate(
                zip(batch, completions)
            ):
                logits = first_logits[offset]
                top_values, top_ids = logits.topk(10)
                parsed = parse_answer(completion)
                by_id[example["id"]]["conditions"][str(filler_length)] = {
                    "rendered_prompt": rendered,
                    "input_token_count": int(encoded["attention_mask"][offset].sum()),
                    "filler_alignment": alignment,
                    "completion": completion,
                    "completion_token_ids": [int(value) for value in new_ids[offset].cpu()],
                    "parsed_answer": parsed,
                    "correct": parsed == int(example["answer"]),
                    "answer_readout": target_rank(logits, tokenizer, example["answer"]),
                    "top_tokens": [
                        {
                            "rank": rank + 1,
                            "token_id": int(token_id),
                            "token": tokenizer.decode([int(token_id)]),
                            "logit": float(value),
                        }
                        for rank, (value, token_id) in enumerate(zip(top_values, top_ids))
                    ],
                }
            print(
                f"  {min(batch_start + args.batch_size, len(prepared))}/{len(prepared)}",
                flush=True,
            )
        output["examples"] = [by_id[example["id"]] for example in examples]
        write_atomic(output_path, output)

    for filler_length in filler_lengths:
        key = str(filler_length)
        conditions = [row["conditions"][key] for row in output["examples"]]
        ranks = [
            int(item["answer_readout"]["best_rank"])
            for item in conditions
            if item["answer_readout"]["best_rank"] is not None
        ]
        output["summary"][key] = {
            "correct": sum(bool(item["correct"]) for item in conditions),
            "total": len(conditions),
            "accuracy": sum(bool(item["correct"]) for item in conditions)
            / len(conditions),
            "mean_answer_rank": sum(ranks) / len(ranks) if ranks else None,
            "single_token_rank_count": len(ranks),
        }
    baseline = {row["id"]: row["conditions"]["0"] for row in output["examples"]}
    output["paired_changes"] = {
        str(length): {
            "rescued": sum(
                not baseline[row["id"]]["correct"]
                and row["conditions"][str(length)]["correct"]
                for row in output["examples"]
            ),
            "hurt": sum(
                baseline[row["id"]]["correct"]
                and not row["conditions"][str(length)]["correct"]
                for row in output["examples"]
            ),
        }
        for length in filler_lengths
        if length > 0
    }
    write_atomic(output_path, output)
    print(json.dumps(output["summary"], indent=2), flush=True)
    print(json.dumps(output["paired_changes"], indent=2), flush=True)


if __name__ == "__main__":
    main()
