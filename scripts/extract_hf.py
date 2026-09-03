#!/usr/bin/env python3
"""Single-GPU Hugging Face port of the filler-token behavioral sweep.

``extract_dsv4.py`` is welded to DeepSeek's reference model, four-way vocab
sharding, and the [B,S,4,4096] hyper-connection hook shape. Ordinary dense
checkpoints (Qwen3.5-4B is the first target) have a single residual stream
and load through ``transformers`` directly, so this script keeps the prompt
scaffold, config format, and output schema and replaces only the model plumbing.

Only the ``eval`` phase (paired filler-length sweep, no lens) is implemented
here. Lens readouts come after the behavior gate passes.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from pathlib import Path
from typing import Any

import torch
from transformers import AutoTokenizer

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from extract_dsv4 import (  # noqa: E402
    answer_is_correct,
    configured_filler_lengths,
    expand_experiment_examples,
    file_sha256,
    filler_placement_for_task,
    full_logits_summary,
    installed_version,
    parse_model_answer,
)
from jlens_filler.prompts import build_messages, render_and_align, token_variants  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", default="main")
    parser.add_argument("--examples-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--phase", choices=["eval", "filler"], default="eval")
    parser.add_argument("--adapter", type=Path, default=None, help="PEFT LoRA adapter to merge into the base model")
    parser.add_argument("--layers", default="all", help="'all' or comma-separated block indices for --phase filler")
    parser.add_argument("--filler-length", type=int, default=None, help="dot count for --phase filler (default: config filler_length or largest configured length)")
    parser.add_argument("--dtype", choices=["bfloat16", "float16", "float32"], default="bfloat16")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--max-new-tokens", type=int, default=3)
    parser.add_argument("--example-ids", default="")
    parser.add_argument("--attn-implementation", default=None)
    parser.add_argument("--load-in-8bit", action="store_true", help="bitsandbytes LLM.int8 weights")
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def load_model(model_id: str, revision: str, dtype: torch.dtype, attn: str | None, load_in_8bit: bool = False, device: str = "cuda"):
    """Qwen3.5 registers as ForConditionalGeneration; fall back when CausalLM refuses."""
    from transformers import AutoModelForCausalLM

    kwargs: dict[str, Any] = {"revision": revision, "dtype": dtype, "device_map": device}
    if load_in_8bit:
        from transformers import BitsAndBytesConfig

        # LLM.int8 weight-only quantization; activations and the lm_head stay in bf16.
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
    if attn:
        kwargs["attn_implementation"] = attn
    try:
        return AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
    except ValueError as error:
        from transformers import AutoModelForImageTextToText

        print(f"AutoModelForCausalLM refused ({error}); trying ImageTextToText", flush=True)
        return AutoModelForImageTextToText.from_pretrained(model_id, **kwargs)


class _NoDoubleBos:
    """Tokenizer proxy: skip add_special_tokens when the text already starts with BOS.

    Llama-3 chat templates emit ``<|begin_of_text|>`` themselves, so a plain
    ``tokenizer.encode`` would prepend a second BOS and break the alignment
    assertion in ``prompts.align_rendered_prompt``. Qwen has no BOS and is
    unaffected.
    """

    def __init__(self, tokenizer: Any):
        self._t = tokenizer

    def _already_has_bos(self, text: str) -> bool:
        bos = self._t.bos_token
        return bool(bos) and text.startswith(bos)

    def encode(self, text: str, **kwargs: Any) -> list[int]:
        if self._already_has_bos(text):
            kwargs["add_special_tokens"] = False
        return self._t.encode(text, **kwargs)

    def __call__(self, text: str, **kwargs: Any) -> Any:
        if self._already_has_bos(text):
            kwargs["add_special_tokens"] = False
        return self._t(text, **kwargs)

    def __len__(self) -> int:
        return len(self._t)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._t, name)


def make_encode_messages(tokenizer: Any):
    """Shim so ``render_and_align`` can call the HF chat template like DeepSeek's encoder."""

    def encode_messages(messages: list[dict[str, str]], thinking_mode: str = "chat") -> str:
        if thinking_mode != "chat":
            raise ValueError("only non-thinking chat rendering is supported")
        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )

    return encode_messages


@torch.inference_mode()
def greedy_generate(
    model: Any, input_ids: list[int], *, max_new_tokens: int, eos_ids: list[int]
) -> tuple[list[int], torch.Tensor]:
    """Greedy completion plus the raw first-step logits over the full vocabulary."""
    tokens = torch.tensor([input_ids], dtype=torch.long, device=model.device)
    out = model.generate(
        input_ids=tokens,
        attention_mask=torch.ones_like(tokens),
        max_new_tokens=max_new_tokens,
        do_sample=False,
        temperature=None,
        top_p=None,
        top_k=None,
        eos_token_id=eos_ids,
        pad_token_id=eos_ids[0],
        output_logits=True,
        return_dict_in_generate=True,
    )
    completion = out.sequences[0, len(input_ids):].tolist()
    first_logits = out.logits[0].float()  # [1, vocab]
    return completion, first_logits


@torch.inference_mode()
def answer_target_summary(
    model: Any,
    tokenizer: Any,
    input_ids: list[int],
    first_logits: torch.Tensor,
    answer: Any,
) -> dict[str, Any]:
    """Rank/log-prob for an answer that may span several tokens.

    Qwen tokenizers split numbers into single digits, so the DeepSeek helper's
    single-token assumption fails. ``best_rank`` here is the rank of the answer's
    *first* token at the generation position (kept under that name so the
    existing analyzers run), and ``best_log_probability`` is the teacher-forced
    log-probability of the complete answer. Both tokenizer surfaces (bare and
    space-prefixed) are scored and the higher-probability one is reported.
    """
    scores = first_logits[0].float()
    log_z = torch.logsumexp(scores, dim=-1)
    variants: list[dict[str, Any]] = []
    seen: set[tuple[int, ...]] = set()
    for surface in (str(answer), f" {answer}"):
        ids = tuple(tokenizer.encode(surface, add_special_tokens=False))
        if not ids or ids in seen:
            continue
        seen.add(ids)
        first = ids[0]
        first_score = scores[first]
        record: dict[str, Any] = {
            "surface": surface,
            "token_ids": list(ids),
            "decoded_tokens": [tokenizer.decode([i]) for i in ids],
            "single_token": len(ids) == 1,
            "first_token_rank": int((scores > first_score).sum().item()) + 1,
            "first_token_log_probability": float(first_score - log_z),
        }
        if len(ids) == 1:
            record["sequence_log_probability"] = record["first_token_log_probability"]
        else:
            full = torch.tensor([list(input_ids) + list(ids)], device=model.device)
            logits = model(input_ids=full, attention_mask=torch.ones_like(full)).logits[0].float()
            start = len(input_ids) - 1
            step_logp = torch.log_softmax(logits[start : start + len(ids)], dim=-1)
            per_token = [float(step_logp[i, ids[i]]) for i in range(len(ids))]
            record["per_token_log_probability"] = per_token
            record["sequence_log_probability"] = float(sum(per_token))
        variants.append(record)
    best = max(variants, key=lambda v: v["sequence_log_probability"])
    return {
        "answer": answer,
        "rank_semantics": "first_token",
        "best_rank": best["first_token_rank"],
        "best_logit": float(scores[best["token_ids"][0]]),
        "best_log_probability": best["sequence_log_probability"],
        "best_probability": float(torch.exp(torch.tensor(best["sequence_log_probability"]))),
        "best_first_token_log_probability": best["first_token_log_probability"],
        "variants": variants,
    }


def decoder_parts(model: Any) -> tuple[Any, Any, Any]:
    """Locate (layers, final norm, lm_head) across HF wrappers (mirrors jlens.hf layouts)."""
    for path in ("model", "model.language_model", "language_model"):
        obj = model
        try:
            for attr in path.split("."):
                obj = getattr(obj, attr)
        except AttributeError:
            continue
        if hasattr(obj, "layers") and hasattr(obj, "norm"):
            return obj.layers, obj.norm, model.lm_head
    raise AttributeError("could not locate decoder layers/norm on this model")


from contextlib import contextmanager


@contextmanager
def capture_block_outputs(layers_module: Any, layer_indices: list[int], positions: list[int] | None):
    """Capture true post-block residuals via forward hooks.

    ``output_hidden_states`` is not usable for this: HF decoders append the
    *final-normed* state as the last entry, so the last block's raw residual is
    never exposed and re-normalizing it corrupts the readout. Hooks see the raw
    block output. ``positions=None`` keeps every position.
    """
    captured: dict[int, torch.Tensor] = {}
    handles = []

    def make_hook(layer: int):
        def hook(_m: Any, _i: Any, output: Any) -> None:
            t = output[0] if isinstance(output, tuple) else output
            captured[layer] = (t[0] if positions is None else t[0, positions]).detach().clone()
        return hook

    try:
        for layer in layer_indices:
            handles.append(layers_module[layer].register_forward_hook(make_hook(layer)))
        yield captured
    finally:
        for h in handles:
            h.remove()


def tracked_forms(tokenizer: Any, expected: dict[str, str]) -> dict[str, list[dict[str, Any]]]:
    """Tokenizer forms for each tracked value, plus a first-digit form for digit-split tokenizers.

    The DeepSeek pipeline ranks only single-token forms. Qwen splits numbers into
    single digits, so every multi-digit value would be rank-less; the added
    ``first_digit`` form ranks the value's leading digit token instead. It is a
    coarse readout (many values share a first digit) and is labeled as such.
    """
    forms: dict[str, list[dict[str, Any]]] = {}
    for label, text in expected.items():
        variants = token_variants(tokenizer, str(text))
        if not any(v["single_token"] for v in variants):
            head = str(text).lstrip("-")[:1]
            ids = tokenizer.encode(head, add_special_tokens=False)
            if len(ids) == 1:
                variants.append({
                    "surface": head, "token_ids": ids, "decoded_tokens": [tokenizer.decode(ids)],
                    "single_token": True, "form": "first_digit", "of": str(text),
                })
        forms[label] = variants
    return forms


def lens_readout(logits: torch.Tensor, tokenizer: Any, top_k: int, tracked: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    """Top-k plus exact ranks/probabilities of tracked forms for a [positions, vocab] logit block."""
    logits = logits.float()
    log_z = torch.logsumexp(logits, dim=-1)
    best_values, best_ids = logits.topk(top_k, dim=-1)
    out = []
    for pos in range(logits.shape[0]):
        row = logits[pos]
        top = [
            {"rank": i + 1, "token_id": int(best_ids[pos, i]), "token": tokenizer.decode([int(best_ids[pos, i])]),
             "logit": float(best_values[pos, i]), "probability": float(torch.exp(best_values[pos, i] - log_z[pos]))}
            for i in range(top_k)
        ]
        targets: dict[str, Any] = {}
        for label, variants in tracked.items():
            positioned = []
            for v in variants:
                item = {k: val for k, val in v.items()}
                if v["single_token"]:
                    tid = v["token_ids"][0]; score = row[tid]
                    item.update({"rank": int((row > score).sum().item()) + 1, "logit": float(score),
                                 "probability": float(torch.exp(score - log_z[pos]))})
                positioned.append(item)
            ranked = [x["rank"] for x in positioned if "rank" in x]
            targets[label] = {"best_rank": min(ranked) if ranked else None, "variants": positioned}
        out.append({"top_tokens": top, "targets": targets})
    return out


@torch.inference_mode()
def run_filler_example(
    *, model: Any, tokenizer: Any, encode_messages: Any, few_shot: list[dict[str, Any]], example: dict[str, Any],
    filler_type: str, filler_length: int, task_type: str, layers: list[int], top_k: int, max_new_tokens: int, eos_ids: list[int],
) -> dict[str, Any]:
    """Logit-lens grid over every filler position, the answer cue, and the generation position."""
    messages = build_messages(few_shot, example, filler_type, filler_length, task_type=task_type)
    rendered, alignment = render_and_align(tokenizer, encode_messages, messages, filler_type, filler_length,
                                           filler_placement=filler_placement_for_task(task_type))
    if len(alignment.filler_token_indices) != filler_length:
        raise AssertionError(f"{example['id']}: {filler_length} fillers mapped to {len(alignment.filler_token_indices)} tokens")
    cue = alignment.answer_cue_token_indices[-1]
    positions = alignment.filler_token_indices + [cue, alignment.generation_position]
    columns = [{"position_kind": "filler", "filler_ordinal": i, "absolute_index": a, "surface": alignment.token_strings[a]}
               for i, a in enumerate(alignment.filler_token_indices, start=1)]
    columns.append({"position_kind": "answer_cue", "absolute_index": cue, "surface": alignment.token_strings[cue]})
    columns.append({"position_kind": "answer_prediction", "absolute_index": alignment.generation_position,
                    "surface": alignment.token_strings[alignment.generation_position]})

    ids = torch.tensor([alignment.input_ids], device=model.device)
    layers_module, norm, head = decoder_parts(model)
    n_blocks = len(layers_module)
    if any(l < 0 or l >= n_blocks for l in layers):
        raise ValueError(f"layers must be within 0..{n_blocks - 1}")
    with capture_block_outputs(layers_module, sorted(set(layers) | {n_blocks - 1}), positions) as captured:
        out = model(input_ids=ids, attention_mask=torch.ones_like(ids), use_cache=False)

    tracked_surfaces = dict(example["expected_intermediates"])
    controls = example.get("tracked_controls", {})
    if set(tracked_surfaces) & set(controls):
        raise ValueError("tracked control labels collide with targets")
    tracked_surfaces.update({str(k): str(v) for k, v in controls.items()})
    tracked = tracked_forms(tokenizer, tracked_surfaces)

    readouts: dict[str, Any] = {"logit_lens": {}}
    for layer in layers:
        logits = head(norm(captured[layer])).float()
        readouts["logit_lens"][str(layer)] = [{**c, **r} for c, r in zip(columns, lens_readout(logits, tokenizer, top_k, tracked))]

    # Closure: final block through norm+head must reproduce the model's own logits at the generation position.
    final_rebuilt = head(norm(captured[n_blocks - 1][-1])).float()
    actual = out.logits[0, alignment.generation_position].float()
    closure = float((final_rebuilt - actual).abs().max())

    completion_ids, first_logits = greedy_generate(model, alignment.input_ids, max_new_tokens=max_new_tokens, eos_ids=eos_ids)
    text = tokenizer.decode(completion_ids, skip_special_tokens=True)
    parsed = parse_model_answer(text, example["answer"])
    base_messages = build_messages(few_shot, example, filler_type, 0, task_type=task_type)
    base_rendered = encode_messages(base_messages, thinking_mode="chat")
    base_ids = tokenizer.encode(base_rendered)
    base_completion, base_logits = greedy_generate(model, base_ids, max_new_tokens=max_new_tokens, eos_ids=eos_ids)
    base_text = tokenizer.decode(base_completion, skip_special_tokens=True)
    base_parsed = parse_model_answer(base_text, example["answer"])

    return {
        "schema_version": 1,
        "example": example,
        "condition": {"task_type": task_type, "filler_type": filler_type, "filler_length": filler_length},
        "messages": messages,
        "rendered_prompt": rendered,
        "alignment": alignment.to_dict(),
        "selected_columns": columns,
        "tracked_token_variants": tracked,
        "rank_semantics": "single-token forms ranked exactly; multi-digit values also carry a first_digit form (coarse)",
        "readouts": readouts,
        "model_output": {
            "actual_prompt_logits": full_logits_summary(actual, tokenizer, top_k),
            "generation_first_logits": full_logits_summary(first_logits[0], tokenizer, top_k),
            "generated_token_ids": completion_ids, "generated_text": text, "parsed_answer": parsed,
            "correct": answer_is_correct(parsed, example["answer"]),
        },
        "no_filler_control": {
            "rendered_prompt": base_rendered, "input_ids": base_ids,
            "actual_prompt_logits": full_logits_summary(base_logits[0], tokenizer, top_k),
            "generated_token_ids": base_completion, "generated_text": base_text, "parsed_answer": base_parsed,
            "correct": answer_is_correct(base_parsed, example["answer"]),
        },
        "compatibility_checks": {
            "n_blocks": n_blocks, "hidden_size": int(captured[layers[0]].shape[-1]),
            "final_block_closure_max_abs_error": closure,
        },
    }


@torch.inference_mode()
def run_filler_length_sweep(
    *,
    model: Any,
    tokenizer: Any,
    encode_messages: Any,
    few_shot: list[dict[str, Any]],
    examples: list[dict[str, Any]],
    filler_type: str,
    filler_lengths: list[int],
    task_type: str,
    top_k: int,
    max_new_tokens: int,
    eos_ids: list[int],
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for number, example in enumerate(examples, start=1):
        started = time.monotonic()
        conditions: dict[str, Any] = {}
        for filler_length in filler_lengths:
            messages = build_messages(
                few_shot, example, filler_type, filler_length, task_type=task_type
            )
            if filler_length:
                rendered, alignment = render_and_align(
                    tokenizer,
                    encode_messages,
                    messages,
                    filler_type,
                    filler_length,
                    filler_placement=filler_placement_for_task(task_type),
                )
                if len(alignment.filler_token_indices) != filler_length:
                    raise AssertionError(
                        f"{example['id']} at k={filler_length}: {filler_length} visible "
                        f"fillers mapped to {len(alignment.filler_token_indices)} tokens"
                    )
                input_ids = alignment.input_ids
                token_strings = alignment.token_strings
                filler_token_indices = alignment.filler_token_indices
            else:
                rendered = encode_messages(messages, thinking_mode="chat")
                input_ids = tokenizer.encode(rendered)
                token_strings = [tokenizer.decode([t]) for t in input_ids]
                filler_token_indices = []

            completion_ids, first_logits = greedy_generate(
                model, input_ids, max_new_tokens=max_new_tokens, eos_ids=eos_ids
            )
            generated_text = tokenizer.decode(completion_ids, skip_special_tokens=True)
            parsed_answer = parse_model_answer(generated_text, example["answer"])
            conditions[str(filler_length)] = {
                "filler_length": filler_length,
                "rendered_prompt": rendered,
                "input_ids": input_ids,
                "token_strings": token_strings,
                "filler_token_indices": filler_token_indices,
                "generated_token_ids": completion_ids,
                "generated_text": generated_text,
                "parsed_answer": parsed_answer,
                "correct": answer_is_correct(parsed_answer, example["answer"]),
                "target": answer_target_summary(model, tokenizer, input_ids, first_logits, example["answer"]),
                "top_tokens": full_logits_summary(first_logits[0], tokenizer, top_k)["top_tokens"],
            }
        rows.append(
            {
                "id": example["id"],
                "example": example,
                "expected_answer": example["answer"],
                "expected_intermediates": example.get("expected_intermediates", {}),
                "conditions": conditions,
            }
        )
        verdicts = " ".join(
            f"k{length}={'Y' if conditions[str(length)]['correct'] else 'n'}"
            for length in filler_lengths
        )
        print(
            f"[{number}/{len(examples)}] {example['id']} {verdicts} "
            f"({time.monotonic() - started:.1f}s)",
            flush=True,
        )
    return {
        "schema_version": 1,
        "task_type": task_type,
        "filler_type": filler_type,
        "filler_lengths": filler_lengths,
        "examples": rows,
    }


def main() -> None:
    args = parse_args()
    torch.manual_seed(42)
    dtype = getattr(torch, args.dtype)

    tokenizer = AutoTokenizer.from_pretrained(args.model_id, revision=args.model_revision)
    tokenizer = _NoDoubleBos(tokenizer)
    model = load_model(args.model_id, args.model_revision, dtype, args.attn_implementation, args.load_in_8bit, args.device)
    if args.adapter is not None:
        from peft import PeftModel

        model = PeftModel.from_pretrained(model, str(args.adapter)).merge_and_unload()
        print(f"merged adapter {args.adapter}", flush=True)
    model.eval()
    encode_messages = make_encode_messages(tokenizer)

    # End-of-turn ids: the tokenizer's eos plus any chat end-of-turn marker that exists.
    vocab = tokenizer.get_vocab()
    eos_ids = sorted(
        {tokenizer.eos_token_id}
        | {vocab[t] for t in ("<|im_end|>", "<|eot_id|>", "<end_of_turn>") if t in vocab}
    )
    print("end-of-turn ids:", {tokenizer.decode([i]): i for i in eos_ids}, flush=True)

    experiment = json.loads(args.examples_config.read_text(encoding="utf-8"))
    filler_lengths = configured_filler_lengths(experiment)
    if filler_lengths is None and args.phase == "eval":
        raise ValueError("eval phase needs a filler_lengths sweep config (k=0 baseline included)")
    examples = expand_experiment_examples(experiment)
    if args.example_ids:
        requested = {v.strip() for v in args.example_ids.split(",") if v.strip()}
        missing = requested - {e["id"] for e in examples}
        if missing:
            raise ValueError(f"requested example IDs are absent: {sorted(missing)}")
        examples = [e for e in examples if e["id"] in requested]
    task_type = experiment.get("task_type", "addition")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    import transformers

    runtime = {
        "timestamp_unix": time.time(),
        "platform": platform.platform(),
        "python": sys.version,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "packages": {d: installed_version(d) for d in ("accelerate", "flash_attn", "fla", "causal_conv1d")},
        "cuda": torch.version.cuda,
        "device": args.device,
        "gpus": [
            {
                "index": i,
                "name": torch.cuda.get_device_name(i),
                "total_memory_bytes": torch.cuda.get_device_properties(i).total_memory,
            }
            for i in range(torch.cuda.device_count() if args.device != "cpu" else 0)
        ],
        "model_id": args.model_id,
        "adapter": str(args.adapter) if args.adapter else None,
        "phase": args.phase,
        "model_revision": args.model_revision,
        "model_class": type(model).__name__,
        "model_config": model.config.to_dict(),
        "dtype": args.dtype,
        "weight_quantization": "bitsandbytes_int8" if args.load_in_8bit else None,
        "attn_implementation": getattr(model.config, "_attn_implementation", None),
        "experiment_config": {
            "path": str(args.examples_config),
            "sha256": file_sha256(args.examples_config),
        },
        "inference": {
            "seed": 42,
            "top_k": args.top_k,
            "max_new_tokens": args.max_new_tokens,
            "thinking_mode": "chat (apply_chat_template enable_thinking=False)",
            "decoding": "greedy",
            "target_rank_semantics": "first answer token rank; log-probability is teacher-forced over all answer tokens",
            "eos_token_ids": eos_ids,
        },
        "tokenizer": {
            "class": type(tokenizer).__name__,
            "length_with_added_tokens": len(tokenizer),
            "bos_token_id": tokenizer.bos_token_id,
            "eos_token_id": tokenizer.eos_token_id,
        },
    }
    (args.output_dir / "runtime.json").write_text(json.dumps(runtime, indent=2, ensure_ascii=False))

    if args.phase == "filler":
        n_blocks = len(decoder_parts(model)[0])
        layers = list(range(n_blocks)) if args.layers == "all" else sorted({int(x) for x in args.layers.split(",") if x.strip()})
        k = args.filler_length if args.filler_length is not None else int(experiment.get("filler_length") or max(filler_lengths))
        for example in examples:
            started = time.time()
            result = run_filler_example(
                model=model, tokenizer=tokenizer, encode_messages=encode_messages, few_shot=experiment["few_shot"],
                example=example, filler_type=experiment["filler_type"], filler_length=k, task_type=task_type,
                layers=layers, top_k=args.top_k, max_new_tokens=args.max_new_tokens, eos_ids=eos_ids,
            )
            result["runtime_file"] = "runtime.json"
            path = args.output_dir / f"{example['id']}.json"
            path.write_text(json.dumps(result, ensure_ascii=False))
            print(f"wrote {path} (dots={'Y' if result['model_output']['correct'] else 'n'} "
                  f"nodots={'Y' if result['no_filler_control']['correct'] else 'n'} "
                  f"closure={result['compatibility_checks']['final_block_closure_max_abs_error']:.2e}, {time.time()-started:.1f}s)", flush=True)
        return

    evaluation = run_filler_length_sweep(
        model=model,
        tokenizer=tokenizer,
        encode_messages=encode_messages,
        few_shot=experiment["few_shot"],
        examples=examples,
        filler_type=experiment["filler_type"],
        filler_lengths=filler_lengths,
        task_type=task_type,
        top_k=args.top_k,
        max_new_tokens=args.max_new_tokens,
        eos_ids=eos_ids,
    )
    path = args.output_dir / "filler_length_sweep.json"
    path.write_text(json.dumps(evaluation, indent=2, ensure_ascii=False))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
