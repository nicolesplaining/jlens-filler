#!/usr/bin/env python3
"""Mechanism-discriminating ablations for DeepSeek-V4 filler dots.

This script tests two architecture-level hypotheses on the variable-binding task:

* Are the dots a serial chain?  Attention ablations prevent filler queries from
  reading earlier filler keys while preserving their access to the prompt and
  preserving the answer query's access to every filler state.
* Does the four-stream mHC residual provide essential within-token workspace?
  mHC ablations project the four raw post-block streams at filler positions onto
  their common (stream-mean) component, optionally preserving flattened L2 norm.

The attention intervention covers both the exact 128-token window and compressed
KV groups.  A compressed group is conservatively removed whenever its receptive
field contains a key forbidden by the condition.  Model and lens weights are never
modified.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from contextlib import contextmanager, nullcontext
from pathlib import Path
from types import MethodType, SimpleNamespace
from typing import Any, Iterator

import torch
import torch.distributed as dist
from safetensors.torch import load_model
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

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
from jlens_filler.prompts import build_messages, render_and_align  # noqa: E402
from patch_varbind_dsv4 import output_tensor, replace_output_tensor  # noqa: E402


ATTENTION_CONDITIONS = {
    "no_interdot",
    "no_interdot_local",
    "no_interdot_compressed",
    "previous_dot_only",
    "previous_dot_only_local",
    "last_2_dots_only_local",
    "last_4_dots_only_local",
    "last_8_dots_only_local",
    "last_16_dots_only_local",
    "last_32_dots_only_local",
    "first_dot_only",
    "no_filler_to_prefix",
    "no_answer_to_dots",
    "no_answer_to_dots_local",
    "no_answer_to_dots_compressed",
}
DOT_HISTORY_WIDTHS = {
    "previous_dot_only": 1,
    "last_2_dots_only": 2,
    "last_4_dots_only": 4,
    "last_8_dots_only": 8,
    "last_16_dots_only": 16,
    "last_32_dots_only": 32,
}
MHC_CONDITIONS = {
    "mhc_common_all": (range(43), False),
    "mhc_common_all_norm": (range(43), True),
    "mhc_common_early_norm": (range(0, 15), True),
    "mhc_common_middle_norm": (range(15, 29), True),
    "mhc_common_late_norm": (range(29, 43), True),
}
MHC_PERMUTATION_CONDITIONS = {
    "mhc_rotate_all": range(43),
    "mhc_rotate_layer14": [14],
    "mhc_rotate_layer28": [28],
    "mhc_rotate_layer41": [41],
}
DEFAULT_CONDITIONS = [
    "no_filler",
    "baseline",
    "no_interdot",
    "previous_dot_only",
    "first_dot_only",
    "no_filler_to_prefix",
    "no_answer_to_dots",
    "mhc_common_all_norm",
    "mhc_common_early_norm",
    "mhc_common_middle_norm",
    "mhc_common_late_norm",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt-path", type=Path, required=True)
    parser.add_argument("--model-config", type=Path, required=True)
    parser.add_argument("--reference-code-dir", type=Path, required=True)
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--filler-length", type=int, default=50)
    parser.add_argument("--conditions", default=",".join(DEFAULT_CONDITIONS))
    parser.add_argument("--selection-sweep", type=Path)
    parser.add_argument(
        "--cohort",
        choices=("all", "rescued", "baseline_correct", "filler_correct", "filler_wrong"),
        default="all",
    )
    parser.add_argument("--max-examples", type=int)
    parser.add_argument("--max-new-tokens", type=int, default=3)
    parser.add_argument("--max-seq-len", type=int, default=1280)
    parser.add_argument("--model-revision", default="unknown")
    parser.add_argument("--process-group-timeout-minutes", type=int, default=60)
    return parser.parse_args()


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def choose_examples(
    experiment: dict[str, Any],
    *,
    selection_sweep: Path | None,
    cohort: str,
    filler_length: int,
    max_examples: int | None,
) -> list[dict[str, Any]]:
    examples = list(experiment["examples"])
    if cohort != "all":
        if selection_sweep is None:
            raise ValueError("non-all cohorts require --selection-sweep")
        sweep = json.loads(selection_sweep.read_text(encoding="utf-8"))
        selected: set[str] = set()
        length_key = str(filler_length)
        for row in sweep["examples"]:
            baseline = bool(row["conditions"]["0"]["correct"])
            filler = bool(row["conditions"][length_key]["correct"])
            keep = {
                "rescued": filler and not baseline,
                "baseline_correct": baseline,
                "filler_correct": filler,
                "filler_wrong": not filler,
            }[cohort]
            if keep:
                selected.add(row["id"])
        examples = [example for example in examples if example["id"] in selected]
    if max_examples is not None:
        examples = examples[: max_examples]
    if not examples:
        raise ValueError("example selection is empty")
    return examples


def render_example(
    *,
    tokenizer: Any,
    encode_messages: Any,
    experiment: dict[str, Any],
    example: dict[str, Any],
    filler_length: int,
) -> tuple[str, Any]:
    messages = build_messages(
        experiment["few_shot"],
        example,
        experiment["filler_type"],
        filler_length,
        task_type=experiment["task_type"],
    )
    # The prompt builders intentionally omit the entire ``Filler:`` field at
    # k=0.  ``render_and_align`` therefore cannot (and should not) manufacture
    # a filler span for the no-filler control.  Use the same official encoding
    # path as the behavioral filler-length sweep and expose an empty span.
    if filler_length == 0:
        rendered = encode_messages(messages, thinking_mode="chat")
        return rendered, SimpleNamespace(
            input_ids=tokenizer.encode(rendered),
            filler_token_indices=[],
        )
    rendered, alignment = render_and_align(
        tokenizer,
        encode_messages,
        messages,
        experiment["filler_type"],
        filler_length,
    )
    if len(alignment.filler_token_indices) != filler_length:
        raise AssertionError(
            f"expected {filler_length} one-token fillers, got "
            f"{len(alignment.filler_token_indices)}"
        )
    return rendered, alignment


def forbidden_key(condition: str, key: int, query: int, fillers: list[int]) -> bool:
    condition = condition.removesuffix("_local").removesuffix("_compressed")
    filler_set = set(fillers)
    first, last = fillers[0], fillers[-1]
    if condition == "no_interdot":
        return query in filler_set and key in filler_set and key < query
    if condition in DOT_HISTORY_WIDTHS:
        if query not in filler_set or key not in filler_set or key >= query:
            return False
        earlier = [position for position in fillers if position < query]
        retained = set(earlier[-DOT_HISTORY_WIDTHS[condition] :])
        return bool(earlier) and key not in retained
    if condition == "first_dot_only":
        return (
            query in filler_set
            and key in filler_set
            and key < query
            and key != first
        )
    if condition == "no_filler_to_prefix":
        return query in filler_set and key < first
    if condition == "no_answer_to_dots":
        return query > last and key in filler_set
    raise ValueError(f"unknown attention condition: {condition}")


def compressed_support(group: int, ratio: int, overlap: bool) -> range:
    start = group * ratio
    if overlap and group > 0:
        start -= ratio
    return range(start, (group + 1) * ratio)


def window_storage_index(key: int, *, start_pos: int, window_size: int) -> int:
    return key if start_pos == 0 else key % window_size


@contextmanager
def attention_ablation(
    model: Any,
    model_module: Any,
    *,
    condition: str,
    fillers: list[int],
    stats: dict[str, int],
) -> Iterator[None]:
    """Remove condition-specific keys from local and compressed attention indexes."""
    if condition not in ATTENTION_CONDITIONS:
        raise ValueError(condition)
    if not fillers:
        raise ValueError("attention ablations require filler positions")
    original_window = model_module.get_window_topk_idxs
    original_compress = model_module.get_compress_topk_idxs
    window_size = int(model.layers[0].attn.window_size)
    local_enabled = not condition.endswith("_compressed")
    compressed_enabled = not condition.endswith("_local")
    local_tables: dict[tuple[int, int, torch.dtype, torch.device], torch.Tensor] = {}
    compressed_tables: dict[
        tuple[int, int, int, int, bool, torch.dtype, torch.device], torch.Tensor
    ] = {}

    def padded_table(
        rows: list[list[int]], base: torch.Tensor
    ) -> torch.Tensor | None:
        width = max((len(row) for row in rows), default=0)
        if width == 0:
            return None
        table = torch.full(
            (len(rows), width),
            -2,
            dtype=base.dtype,
            device=base.device,
        )
        for row_number, values in enumerate(rows):
            if values:
                table[row_number, : len(values)] = torch.tensor(
                    values, dtype=base.dtype, device=base.device
                )
        return table

    def mask_local(base: torch.Tensor, start_pos: int) -> torch.Tensor:
        cache_key = (start_pos, base.shape[1], base.dtype, base.device)
        table = local_tables.get(cache_key)
        if cache_key not in local_tables:
            rows: list[list[int]] = []
            for row in range(base.shape[1]):
                query = start_pos + row
                rows.append(
                    [
                        window_storage_index(
                            key, start_pos=start_pos, window_size=window_size
                        )
                        for key in range(
                            max(0, query - window_size + 1), query + 1
                        )
                        if forbidden_key(condition, key, query, fillers)
                    ]
                )
            table = padded_table(rows, base)
            if table is not None:
                local_tables[cache_key] = table
        if table is None:
            return base
        masked = base.clone()
        row_mask = (masked.unsqueeze(-1) == table[None, :, None, :]).any(dim=-1)
        stats["local_indexes_removed"] += int(row_mask.sum().item())
        masked[row_mask] = -1
        return masked

    def mask_compressed(
        base: torch.Tensor,
        *,
        ratio: int,
        start_pos: int,
        offset: int,
        overlap: bool,
    ) -> torch.Tensor:
        cache_key = (
            ratio,
            start_pos,
            base.shape[1],
            offset,
            overlap,
            base.dtype,
            base.device,
        )
        table = compressed_tables.get(cache_key)
        if cache_key not in compressed_tables:
            latest_key = start_pos + base.shape[1] - 1
            group_limit = latest_key // ratio + 2
            rows = []
            for row in range(base.shape[1]):
                query = start_pos + row
                rows.append(
                    [
                        group + offset
                        for group in range(group_limit)
                        if any(
                            forbidden_key(condition, key, query, fillers)
                            for key in compressed_support(group, ratio, overlap)
                        )
                    ]
                )
            table = padded_table(rows, base)
            if table is not None:
                compressed_tables[cache_key] = table
        if table is None:
            return base
        masked = base.clone()
        row_mask = (masked.unsqueeze(-1) == table[None, :, None, :]).any(dim=-1)
        stats["compressed_indexes_removed"] += int(row_mask.sum().item())
        masked[row_mask] = -1
        return masked

    def wrapped_window(win: int, bsz: int, seqlen: int, start_pos: int):
        base = original_window(win, bsz, seqlen, start_pos)
        return mask_local(base, start_pos) if local_enabled else base

    def wrapped_compress(
        ratio: int, bsz: int, seqlen: int, start_pos: int, offset: int
    ):
        base = original_compress(ratio, bsz, seqlen, start_pos, offset)
        return mask_compressed(
            base,
            ratio=ratio,
            start_pos=start_pos,
            offset=offset,
            overlap=False,
        ) if compressed_enabled else base

    indexers: list[tuple[Any, Any]] = []
    try:
        model_module.get_window_topk_idxs = wrapped_window
        model_module.get_compress_topk_idxs = wrapped_compress
        for layer in model.layers:
            indexer = getattr(layer.attn, "indexer", None)
            if indexer is None:
                continue
            original_forward = indexer.forward

            def wrapped_indexer(
                this: Any,
                x: torch.Tensor,
                qr: torch.Tensor,
                start_pos: int,
                offset: int,
                *,
                _original: Any = original_forward,
            ) -> torch.Tensor:
                base = _original(x, qr, start_pos, offset)
                return mask_compressed(
                    base,
                    ratio=int(this.compress_ratio),
                    start_pos=start_pos,
                    offset=offset,
                    overlap=True,
                ) if compressed_enabled else base

            indexers.append((indexer, original_forward))
            indexer.forward = MethodType(wrapped_indexer, indexer)
        yield
    finally:
        model_module.get_window_topk_idxs = original_window
        model_module.get_compress_topk_idxs = original_compress
        for indexer, original_forward in indexers:
            indexer.forward = original_forward


@contextmanager
def mhc_common_ablation(
    model: Any,
    *,
    layers: list[int],
    fillers: list[int],
    norm_matched: bool,
    stats: dict[str, int],
) -> Iterator[None]:
    """Project selected raw mHC filler states onto the common-stream subspace."""
    handles = []

    def make_hook(layer_number: int):
        def hook(_module: Any, inputs: Any, output: Any) -> Any:
            tensor = output_tensor(output)
            if tensor.ndim != 4 or tensor.shape[2] != 4:
                raise AssertionError(
                    f"layer {layer_number}: expected [B,S,4,D], got {tuple(tensor.shape)}"
                )
            start_pos = int(inputs[1])
            local_positions = [
                position - start_pos
                for position in fillers
                if start_pos <= position < start_pos + tensor.shape[1]
            ]
            if not local_positions:
                return output
            patched = tensor.clone()
            selected = patched[:, local_positions]
            common = selected.mean(dim=2, keepdim=True).expand_as(selected).clone()
            if norm_matched:
                original_norm = selected.float().flatten(2).norm(dim=-1, keepdim=True)
                common_norm = common.float().flatten(2).norm(dim=-1, keepdim=True)
                scale = (original_norm / common_norm.clamp_min(1e-12)).unsqueeze(-1)
                common = (common.float() * scale).to(common.dtype)
            patched[:, local_positions] = common
            stats["mhc_cells_projected"] += len(local_positions)
            return replace_output_tensor(output, patched)

        return hook

    try:
        for layer in layers:
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield
    finally:
        for handle in handles:
            handle.remove()


def rotate_mhc_streams(tensor: torch.Tensor) -> torch.Tensor:
    """Cyclically permute all four mHC streams without discarding information."""
    if tensor.ndim < 3 or tensor.shape[-2] != 4:
        raise AssertionError(f"expected a four-stream tensor, got {tuple(tensor.shape)}")
    return tensor.roll(shifts=1, dims=-2)


@contextmanager
def mhc_permutation_ablation(
    model: Any,
    *,
    layers: list[int],
    fillers: list[int],
    stats: dict[str, int],
) -> Iterator[None]:
    """Rotate mHC stream identities at target fillers while preserving all values."""
    handles = []

    def make_hook(layer_number: int):
        def hook(_module: Any, inputs: Any, output: Any) -> Any:
            tensor = output_tensor(output)
            if tensor.ndim != 4 or tensor.shape[2] != 4:
                raise AssertionError(
                    f"layer {layer_number}: expected [B,S,4,D], got {tuple(tensor.shape)}"
                )
            start_pos = int(inputs[1])
            local_positions = [
                position - start_pos
                for position in fillers
                if start_pos <= position < start_pos + tensor.shape[1]
            ]
            if not local_positions:
                return output
            patched = tensor.clone()
            patched[:, local_positions] = rotate_mhc_streams(
                patched[:, local_positions]
            )
            stats["mhc_cells_permuted"] += len(local_positions)
            return replace_output_tensor(output, patched)

        return hook

    try:
        for layer in layers:
            handles.append(model.layers[layer].register_forward_hook(make_hook(layer)))
        yield
    finally:
        for handle in handles:
            handle.remove()


def intervention_context(
    *,
    model: Any,
    model_module: Any,
    condition: str,
    fillers: list[int],
    stats: dict[str, int],
):
    if condition in {"baseline", "no_filler"}:
        return nullcontext()
    if condition in ATTENTION_CONDITIONS:
        return attention_ablation(
            model, model_module, condition=condition, fillers=fillers, stats=stats
        )
    if condition in MHC_CONDITIONS:
        raw_layers, norm_matched = MHC_CONDITIONS[condition]
        return mhc_common_ablation(
            model,
            layers=list(raw_layers),
            fillers=fillers,
            norm_matched=norm_matched,
            stats=stats,
        )
    if condition in MHC_PERMUTATION_CONDITIONS:
        return mhc_permutation_ablation(
            model,
            layers=list(MHC_PERMUTATION_CONDITIONS[condition]),
            fillers=fillers,
            stats=stats,
        )
    raise ValueError(f"unknown condition: {condition}")


def main() -> None:
    args = parse_args()
    conditions = [value.strip() for value in args.conditions.split(",") if value.strip()]
    if len(conditions) != len(set(conditions)):
        raise ValueError("conditions must be unique")
    unknown = set(conditions) - (
        {"baseline", "no_filler"}
        | ATTENTION_CONDITIONS
        | set(MHC_CONDITIONS)
        | set(MHC_PERMUTATION_CONDITIONS)
    )
    if unknown:
        raise ValueError(f"unknown conditions: {sorted(unknown)}")
    if args.filler_length <= 0:
        raise ValueError("--filler-length must be positive")

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
    import model as model_module  # type: ignore  # noqa: E402
    from model import ModelArgs, Transformer  # type: ignore  # noqa: E402

    model_args = ModelArgs(**json.loads(args.model_config.read_text(encoding="utf-8")))
    model_args.max_batch_size = 1
    model_args.max_seq_len = args.max_seq_len
    if model_args.hc_mult != 4 or model_args.n_layers != 43:
        raise AssertionError(
            f"expected DeepSeek V4 Flash hc_mult=4/n_layers=43, got "
            f"{model_args.hc_mult}/{model_args.n_layers}"
        )
    if rank == 0:
        print(f"loading mechanism-ablation model on {world_size} GPUs", flush=True)
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
    examples = choose_examples(
        experiment,
        selection_sweep=args.selection_sweep,
        cohort=args.cohort,
        filler_length=args.filler_length,
        max_examples=args.max_examples,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "mechanism-ablations.json"
    output: dict[str, Any] | None = (
        {
            "schema_version": 1,
            "task_type": experiment["task_type"],
            "filler_type": experiment["filler_type"],
            "filler_length": args.filler_length,
            "cohort": args.cohort,
            "conditions": conditions,
            "attention_semantics": {
                "no_interdot": "filler queries cannot read any earlier filler key",
                "no_interdot_local": "same prohibition only in exact local attention",
                "no_interdot_compressed": "same prohibition only in compressed attention",
                "previous_dot_only": "filler queries retain only their immediately preceding filler key",
                "last_N_dots_only_local": (
                    "filler queries retain only their N most recent earlier filler "
                    "keys in exact local attention; N is swept over 1,2,4,8,16,32"
                ),
                "first_dot_only": "filler queries retain only the first earlier filler key",
                "no_filler_to_prefix": "filler queries cannot read keys before the filler span",
                "no_answer_to_dots": "queries after the filler span cannot read filler keys",
                "no_answer_to_dots_local": "same prohibition only in exact local attention",
                "no_answer_to_dots_compressed": "same prohibition only in compressed attention",
                "compressed_kv": (
                    "a compressed group is removed if its receptive field contains "
                    "any condition-forbidden key"
                ),
            },
            "mhc_semantics": (
                "project raw post-block filler activations [B,S,4,4096] onto "
                "the common-stream subspace; *_norm preserves flattened L2 norm; "
                "mhc_rotate_* cyclically permutes stream identities while retaining "
                "every scalar value"
            ),
            "examples": [],
            "summary": {},
            "runtime": {
                "timestamp_unix": time.time(),
                "platform": platform.platform(),
                "torch": torch.__version__,
                "world_size": world_size,
                "model_revision": args.model_revision,
                "model_config_sha256": file_sha256(args.model_config),
                "examples_config_sha256": file_sha256(args.examples_config),
                "selection_sweep_sha256": (
                    file_sha256(args.selection_sweep) if args.selection_sweep else None
                ),
                "seed": 42,
            },
        }
        if rank == 0
        else None
    )

    for example_number, example in enumerate(examples, start=1):
        if rank == 0:
            print(
                f"example {example_number}/{len(examples)}: {example['id']}",
                flush=True,
            )
        example_output: dict[str, Any] | None = (
            {
                "id": example["id"],
                "answer": example["answer"],
                "expected_intermediates": example.get("expected_intermediates", {}),
                "conditions": {},
            }
            if rank == 0
            else None
        )
        for condition in conditions:
            filler_length = 0 if condition == "no_filler" else args.filler_length
            rendered, alignment = render_example(
                tokenizer=tokenizer,
                encode_messages=encode_messages,
                experiment=experiment,
                example=example,
                filler_length=filler_length,
            )
            stats = {
                "local_indexes_removed": 0,
                "compressed_indexes_removed": 0,
                "mhc_cells_projected": 0,
                "mhc_cells_permuted": 0,
            }
            started = time.monotonic()
            with intervention_context(
                model=model,
                model_module=model_module,
                condition=condition,
                fillers=alignment.filler_token_indices,
                stats=stats,
            ):
                completion_ids, first_logits = greedy_generate(
                    model,
                    alignment.input_ids,
                    max_new_tokens=args.max_new_tokens,
                    eos_id=tokenizer.eos_token_id,
                )
            completion = tokenizer.decode(completion_ids, skip_special_tokens=True)
            parsed = parse_model_answer(completion, example["answer"])
            correct = answer_is_correct(parsed, example["answer"])
            if rank == 0:
                assert example_output is not None
                summary = target_logit_summary(first_logits[0], tokenizer, example["answer"])
                example_output["conditions"][condition] = {
                    "rendered_prompt": rendered,
                    "input_length": len(alignment.input_ids),
                    "filler_token_indices": alignment.filler_token_indices,
                    "filler_token_ids": [
                        alignment.input_ids[index]
                        for index in alignment.filler_token_indices
                    ],
                    "completion_token_ids": completion_ids,
                    "completion": completion,
                    "parsed_answer": parsed,
                    "correct": correct,
                    "answer_readout": summary,
                    "top_tokens": full_logits_summary(
                        first_logits[0], tokenizer, 10
                    )["top_tokens"],
                    "intervention_counts": stats,
                    "elapsed_seconds": time.monotonic() - started,
                }
                print(
                    f"  {condition}: {completion!r} correct={correct} "
                    f"rank={summary['best_rank']}",
                    flush=True,
                )
        if rank == 0:
            assert output is not None and example_output is not None
            output["examples"].append(example_output)
            write_json_atomic(output_path, output)

    if rank == 0:
        assert output is not None
        for condition in conditions:
            records = [row["conditions"][condition] for row in output["examples"]]
            output["summary"][condition] = {
                "correct": sum(bool(record["correct"]) for record in records),
                "total": len(records),
                "accuracy": sum(bool(record["correct"]) for record in records)
                / len(records),
                "mean_answer_rank": sum(
                    int(record["answer_readout"]["best_rank"]) for record in records
                )
                / len(records),
                "median_answer_rank": sorted(
                    int(record["answer_readout"]["best_rank"]) for record in records
                )[len(records) // 2],
                "mean_elapsed_seconds": sum(
                    float(record["elapsed_seconds"]) for record in records
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
