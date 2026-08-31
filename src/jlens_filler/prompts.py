"""Prompt construction and exact token/character alignment.

The filler scaffold and five-shot structure mirror
``kaleybrauer/filler-token-reasoning``. Rendering into model text is delegated
to DeepSeek's released ``encoding_dsv4.encode_messages`` implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt
from typing import Any, Callable


def make_filler(filler_type: str, length: int) -> str:
    if length < 0:
        raise ValueError("filler length must be nonnegative")
    if filler_type == "dots":
        return " ".join(["."] * length)
    if filler_type == "counting":
        return " ".join(str(i) for i in range(1, length + 1))
    if filler_type == "alphabet":
        return " ".join(chr(ord("a") + (i % 26)) for i in range(length))
    raise ValueError(f"unsupported filler type: {filler_type}")


def filler_description(filler_type: str) -> str:
    return {
        "dots": "dots",
        "counting": "counting numbers",
        "alphabet": "letters",
    }[filler_type]


def _fact_phrases(item: dict[str, Any]) -> list[str]:
    phrases: list[str] = []
    index = 1
    while f"fact_phrase_{index}" in item:
        phrases.append(str(item[f"fact_phrase_{index}"]))
        index += 1
    if len(phrases) < 2:
        raise ValueError("each addition item must contain at least two fact phrases")
    return phrases


def build_system_message(filler_type: str, length: int, fact_count: int = 2) -> str:
    if fact_count < 2:
        raise ValueError("fact_count must be at least two")
    count_word = {2: "two", 3: "three"}.get(fact_count, str(fact_count))
    text = (
        f"You will be given a question that requires adding {count_word} values together. "
        "Answer immediately with just the number, nothing else. "
        "No explanation, no words, no reasoning, just the number."
    )
    if length:
        text += (
            " After the question, there will be some filler tokens "
            f"(a sequence of {filler_description(filler_type)}) to give you extra "
            "space to process the problem before answering."
        )
    return text


def build_repeated_squaring_system_message(filler_type: str, length: int) -> str:
    text = (
        "You will be given integers x, N, and T. Set x_0 = x mod N, then "
        "repeatedly apply x_t = x_(t-1)^2 mod N exactly T times. "
        "Answer immediately with just x_T as a base-10 integer, nothing else. "
        "No explanation, no words, no reasoning, just the number."
    )
    if length:
        text += (
            " After the question, there will be some filler tokens "
            f"(a sequence of {filler_description(filler_type)}) to give you extra "
            "space to process the problem before answering."
        )
    return text


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def build_user_turn(item: dict[str, Any], filler_type: str, length: int) -> str:
    question = f"Question: What is {' plus '.join(_fact_phrases(item))}?"
    if length:
        return f"{question}\n\nFiller: {make_filler(filler_type, length)}\n\nAnswer:"
    return f"{question}\n\nAnswer:"


def build_repeated_squaring_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    modulus = int(item["modulus"])
    start = int(item["x"])
    time_steps = int(item["time_steps"])
    if modulus <= 1 or time_steps < 0:
        raise ValueError("repeated-squaring items require N > 1 and T >= 0")
    if gcd(start, modulus) != 1:
        raise ValueError("repeated-squaring x must be coprime to N")
    residue = start % modulus
    trace: list[int] = []
    for _ in range(time_steps):
        residue = residue * residue % modulus
        trace.append(residue)
    if int(item["answer"]) != residue:
        raise ValueError(
            f"repeated-squaring answer {item['answer']} does not match {residue}"
        )
    if "factorization_for_validation_only" in item:
        factors = [int(value) for value in item["factorization_for_validation_only"]]
        if (
            len(factors) != 2
            or factors[0] == factors[1]
            or not all(_is_prime(value) for value in factors)
            or factors[0] * factors[1] != modulus
        ):
            raise ValueError("validation-only factors must be distinct primes multiplying to N")
    expected = item.get("expected_intermediates")
    if expected is not None and list(map(int, expected.values())) != trace:
        raise ValueError("expected intermediates do not match the squaring trace")
    question = (
        f"Question: Starting with x_0 = {start} mod {modulus}, repeatedly apply "
        f"x_t = x_(t-1)^2 mod {modulus} for exactly {time_steps} steps. "
        f"What is x_{time_steps}?"
    )
    if length:
        return f"{question}\n\nFiller: {make_filler(filler_type, length)}\n\nAnswer:"
    return f"{question}\n\nAnswer:"


def build_messages(
    few_shot: list[dict[str, Any]],
    target: dict[str, Any],
    filler_type: str,
    length: int,
    task_type: str = "addition",
) -> list[dict[str, str]]:
    if task_type == "repeated_squaring_mod":
        messages = [
            {
                "role": "system",
                "content": build_repeated_squaring_system_message(
                    filler_type, length
                ),
            }
        ]
        for item in few_shot:
            messages.append(
                {
                    "role": "user",
                    "content": build_repeated_squaring_user_turn(
                        item, filler_type, length
                    ),
                }
            )
            messages.append({"role": "assistant", "content": str(item["answer"])})
        messages.append(
            {
                "role": "user",
                "content": build_repeated_squaring_user_turn(
                    target, filler_type, length
                ),
            }
        )
        return messages
    if task_type != "addition":
        raise ValueError(f"unsupported task type: {task_type}")
    fact_count = len(_fact_phrases(target))
    for item in few_shot:
        if len(_fact_phrases(item)) != fact_count:
            raise ValueError("few-shot and target items must use the same number of facts")
    messages: list[dict[str, str]] = [
        {
            "role": "system",
            "content": build_system_message(filler_type, length, fact_count),
        }
    ]
    for item in few_shot:
        messages.append(
            {"role": "user", "content": build_user_turn(item, filler_type, length)}
        )
        messages.append({"role": "assistant", "content": str(item["answer"])})
    messages.append(
        {"role": "user", "content": build_user_turn(target, filler_type, length)}
    )
    return messages


@dataclass(frozen=True)
class TokenAlignment:
    input_ids: list[int]
    token_strings: list[str]
    offsets: list[tuple[int, int]]
    filler_char_span: tuple[int, int]
    filler_token_indices: list[int]
    answer_cue_char_span: tuple[int, int]
    answer_cue_token_indices: list[int]
    generation_position: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "input_ids": self.input_ids,
            "token_strings": self.token_strings,
            "offsets": [list(x) for x in self.offsets],
            "filler_char_span": list(self.filler_char_span),
            "filler_token_indices": self.filler_token_indices,
            "answer_cue_char_span": list(self.answer_cue_char_span),
            "answer_cue_token_indices": self.answer_cue_token_indices,
            "generation_position": self.generation_position,
        }


def _overlapping_token_indices(
    offsets: list[tuple[int, int]], char_span: tuple[int, int]
) -> list[int]:
    start, end = char_span
    return [
        idx
        for idx, (tok_start, tok_end) in enumerate(offsets)
        if tok_end > start and tok_start < end
    ]


def align_rendered_prompt(
    tokenizer: Any,
    rendered_prompt: str,
    filler_surface: str,
) -> TokenAlignment:
    """Find the target turn's filler and answer cue without token assumptions."""
    filler_marker = f"Filler: {filler_surface}\n\nAnswer:"
    marker_start = rendered_prompt.rfind(filler_marker)
    if marker_start < 0:
        raise ValueError("target filler marker was not found in rendered prompt")
    filler_start = marker_start + len("Filler: ")
    filler_span = (filler_start, filler_start + len(filler_surface))

    answer_start = marker_start + len(f"Filler: {filler_surface}\n\n")
    answer_span = (answer_start, answer_start + len("Answer:"))

    encoded = tokenizer(
        rendered_prompt,
        add_special_tokens=False,
        return_offsets_mapping=True,
    )
    input_ids = list(encoded["input_ids"])
    offsets = [tuple(x) for x in encoded["offset_mapping"]]
    official_ids = tokenizer.encode(rendered_prompt)
    if input_ids != official_ids:
        raise AssertionError(
            "tokenizer.encode(rendered_prompt) differs from the offset-mapped "
            "add_special_tokens=False encoding; official generation convention is ambiguous"
        )

    filler_indices = _overlapping_token_indices(offsets, filler_span)
    answer_indices = _overlapping_token_indices(offsets, answer_span)
    if not filler_indices:
        raise AssertionError("filler character span maps to no tokens")
    if not answer_indices:
        raise AssertionError("answer cue character span maps to no tokens")
    if filler_indices[-1] >= answer_indices[0]:
        raise AssertionError("filler tokens are not strictly before the answer cue")

    token_strings = [tokenizer.decode([token_id]) for token_id in input_ids]
    return TokenAlignment(
        input_ids=input_ids,
        token_strings=token_strings,
        offsets=offsets,
        filler_char_span=filler_span,
        filler_token_indices=filler_indices,
        answer_cue_char_span=answer_span,
        answer_cue_token_indices=answer_indices,
        generation_position=len(input_ids) - 1,
    )


def render_and_align(
    tokenizer: Any,
    encode_messages: Callable[..., str],
    messages: list[dict[str, str]],
    filler_type: str,
    filler_length: int,
) -> tuple[str, TokenAlignment]:
    rendered = encode_messages(messages, thinking_mode="chat")
    alignment = align_rendered_prompt(
        tokenizer, rendered, make_filler(filler_type, filler_length)
    )
    return rendered, alignment


def token_variants(tokenizer: Any, text: str) -> list[dict[str, Any]]:
    """Return unique tokenizer forms for a tracked concept."""
    variants: list[dict[str, Any]] = []
    seen: set[tuple[int, ...]] = set()
    for surface in (text, f" {text}"):
        ids = tuple(tokenizer.encode(surface, add_special_tokens=False))
        if not ids or ids in seen:
            continue
        seen.add(ids)
        variants.append(
            {
                "surface": surface,
                "token_ids": list(ids),
                "decoded_tokens": [tokenizer.decode([x]) for x in ids],
                "single_token": len(ids) == 1,
            }
        )
    return variants
