#!/usr/bin/env python3
"""Separate instruction, demonstration, and target-dot effects on variable binding.

The paper-style prompt normally changes all three together: the system message
announces k fillers, every few-shot example contains k fillers, and the target
contains k fillers.  This 2x2x2 factorial holds those components apart so a
behavioral rescue is not automatically attributed to computation at target dots.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path
from typing import Any

import torch
import torch.distributed as dist
from safetensors.torch import load_model
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from ablate_varbind_mechanism_dsv4 import choose_examples, write_json_atomic  # noqa: E402
from extract_dsv4 import (  # noqa: E402
    answer_is_correct,
    barrier,
    distributed_setup,
    file_sha256,
    full_logits_summary,
    greedy_generate,
    parse_model_answer,
    target_logit_summary,
)
from jlens_filler.prompts import (  # noqa: E402
    align_rendered_prompt,
    build_variable_binding_system_message,
    build_variable_binding_user_turn,
    make_filler,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--selection-sweep", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--filler-length", type=int, default=50)
    parser.add_argument(
        "--cohort",
        choices=("all", "rescued", "baseline_correct", "filler_correct", "filler_wrong"),
        default="all",
    )
    parser.add_argument("--max-examples", type=int)
    parser.add_argument("--max-new-tokens", type=int, default=1)
    parser.add_argument("--max-seq-len", type=int, default=1280)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=60)
    return parser.parse_args()


def factorial_conditions(k: int) -> list[tuple[str, int, int, int]]:
    """Return canonical endpoints first, followed by the other six cells."""
    return [
        ("s0_d0_t0", 0, 0, 0),
        (f"s{k}_d{k}_t{k}", k, k, k),
        (f"s{k}_d{k}_t0", k, k, 0),
        (f"s{k}_d0_t{k}", k, 0, k),
        (f"s{k}_d0_t0", k, 0, 0),
        (f"s0_d{k}_t{k}", 0, k, k),
        (f"s0_d{k}_t0", 0, k, 0),
        (f"s0_d0_t{k}", 0, 0, k),
    ]


def render_factorial_prompt(
    *,
    tokenizer: Any,
    encode_messages: Any,
    few_shot: list[dict[str, Any]],
    example: dict[str, Any],
    filler_type: str,
    system_length: int,
    demo_length: int,
    target_length: int,
) -> tuple[str, list[int], list[int]]:
    messages: list[dict[str, str]] = [
        {
            "role": "system",
            "content": build_variable_binding_system_message(
                filler_type, system_length
            ),
        }
    ]
    for item in few_shot:
        messages.extend(
            [
                {
                    "role": "user",
                    "content": build_variable_binding_user_turn(
                        item, filler_type, demo_length
                    ),
                },
                {"role": "assistant", "content": str(item["answer"])},
            ]
        )
    messages.append(
        {
            "role": "user",
            "content": build_variable_binding_user_turn(
                example, filler_type, target_length
            ),
        }
    )
    rendered = encode_messages(messages, thinking_mode="chat")
    if target_length == 0:
        return rendered, tokenizer.encode(rendered), []
    alignment = align_rendered_prompt(
        tokenizer, rendered, make_filler(filler_type, target_length)
    )
    if len(alignment.filler_token_indices) != target_length:
        raise AssertionError(
            f"expected {target_length} target filler tokens, got "
            f"{len(alignment.filler_token_indices)}"
        )
    return rendered, alignment.input_ids, alignment.filler_token_indices


@torch.inference_mode()
def main() -> None:
    args = parse_args()
    if args.filler_length <= 0:
        raise ValueError("factorial filler length must be positive")
    rank, _local_rank, world_size = distributed_setup(
        args.process_group_timeout_minutes
    )
    if world_size != 4:
        raise SystemExit(f"converted checkpoint requires world_size=4, got {world_size}")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_default_dtype(torch.bfloat16)
    torch.set_num_threads(8)
    torch.manual_seed(42)

    sys.path.insert(0, str(args.reference_code_dir.resolve()))
    sys.path.insert(0, str(args.reference_code_dir.resolve().parent / "encoding"))
    from encoding_dsv4 import encode_messages  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    model_args = ModelArgs(**json.loads(args.model_config.read_text(encoding="utf-8")))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if model_args.hc_mult != 4 or model_args.n_layers != 43:
        raise AssertionError("expected DeepSeek V4 Flash hc_mult=4/n_layers=43")
    if rank == 0:
        print(f"loading prompt-factorial model on {world_size} GPUs", flush=True)
    with torch.device("cuda"):
        model = Transformer(model_args)
    load_model(
        model,
        str(args.ckpt_path / f"model{rank}-mp{world_size}.safetensors"),
        strict=False,
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.ckpt_path)
    if len(tokenizer) != model_args.vocab_size:
        raise AssertionError("tokenizer/model vocabulary mismatch")
    torch.set_default_device("cuda")
    barrier()

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    if experiment.get("task_type") != "variable_binding":
        raise ValueError("this factorial is specific to variable_binding")
    examples = choose_examples(
        experiment,
        selection_sweep=args.selection_sweep,
        cohort=args.cohort,
        filler_length=args.filler_length,
        max_examples=args.max_examples,
    )
    conditions = factorial_conditions(args.filler_length)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "prompt-factorial.json"
    output: dict[str, Any] | None = (
        {
            "schema_version": 1,
            "design": {
                "s": "system message announces filler length",
                "d": "each few-shot demonstration contains fillers",
                "t": "target example contains fillers",
                "filler_length": args.filler_length,
            },
            "cohort": args.cohort,
            "conditions": [name for name, *_ in conditions],
            "examples": [],
            "summary": {},
            "runtime": {
                "timestamp_unix": time.time(),
                "platform": platform.platform(),
                "torch": torch.__version__,
                "world_size": world_size,
                "seed": 42,
                "model_revision": args.model_revision,
                "model_config_sha256": file_sha256(args.model_config),
                "examples_config_sha256": file_sha256(args.examples_config),
                "selection_sweep_sha256": (
                    file_sha256(args.selection_sweep) if args.selection_sweep else None
                ),
            },
        }
        if rank == 0
        else None
    )

    for number, example in enumerate(examples, start=1):
        if rank == 0:
            print(f"example {number}/{len(examples)}: {example['id']}", flush=True)
        row: dict[str, Any] | None = (
            {
                "id": example["id"],
                "answer": example["answer"],
                "expected_intermediates": example.get("expected_intermediates", {}),
                "conditions": {},
            }
            if rank == 0
            else None
        )
        for name, system_length, demo_length, target_length in conditions:
            rendered, input_ids, target_fillers = render_factorial_prompt(
                tokenizer=tokenizer,
                encode_messages=encode_messages,
                few_shot=experiment["few_shot"],
                example=example,
                filler_type=experiment["filler_type"],
                system_length=system_length,
                demo_length=demo_length,
                target_length=target_length,
            )
            if len(input_ids) >= model.max_seq_len:
                raise AssertionError(f"prompt length {len(input_ids)} exceeds model limit")
            started = time.monotonic()
            completion_ids, first_logits = greedy_generate(
                model,
                input_ids,
                max_new_tokens=args.max_new_tokens,
                eos_id=tokenizer.eos_token_id,
            )
            if rank == 0:
                assert row is not None
                completion = tokenizer.decode(completion_ids, skip_special_tokens=True)
                parsed = parse_model_answer(completion, example["answer"])
                readout = target_logit_summary(first_logits[0], tokenizer, example["answer"])
                row["conditions"][name] = {
                    "system_length": system_length,
                    "demo_length": demo_length,
                    "target_length": target_length,
                    "rendered_prompt": rendered,
                    "input_length": len(input_ids),
                    "target_filler_token_indices": target_fillers,
                    "completion_token_ids": completion_ids,
                    "completion": completion,
                    "parsed_answer": parsed,
                    "correct": answer_is_correct(parsed, example["answer"]),
                    "answer_readout": readout,
                    "top_tokens": full_logits_summary(first_logits[0], tokenizer, 10)[
                        "top_tokens"
                    ],
                    "elapsed_seconds": time.monotonic() - started,
                }
                print(
                    f"  {name}: {completion!r} correct="
                    f"{row['conditions'][name]['correct']} rank={readout['best_rank']}",
                    flush=True,
                )
        if rank == 0:
            assert output is not None and row is not None
            output["examples"].append(row)
            write_json_atomic(output_path, output)

    if rank == 0:
        assert output is not None
        for name, *_ in conditions:
            records = [row["conditions"][name] for row in output["examples"]]
            output["summary"][name] = {
                "correct": sum(bool(record["correct"]) for record in records),
                "total": len(records),
                "accuracy": sum(bool(record["correct"]) for record in records)
                / len(records),
                "mean_answer_rank": sum(
                    int(record["answer_readout"]["best_rank"]) for record in records
                )
                / len(records),
                "mean_answer_log_probability": sum(
                    float(record["answer_readout"]["best_log_probability"])
                    for record in records
                )
                / len(records),
            }
        write_json_atomic(output_path, output)
        print(json.dumps(output["summary"], indent=2), flush=True)
        print(f"wrote {output_path}", flush=True)
    barrier()
    if dist.is_initialized():
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
