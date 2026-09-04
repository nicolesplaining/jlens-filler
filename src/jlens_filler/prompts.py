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
    if filler_type == "alphabet-scrambled":
        return " ".join(_scrambled([chr(ord("a") + (i % 26)) for i in range(length)]))
    if filler_type == "counting-scrambled":
        return " ".join(_scrambled([str(i) for i in range(1, length + 1)]))
    raise ValueError(f"unsupported filler type: {filler_type}")


def _scrambled(items: list[str]) -> list[str]:
    """Fixed permutation (seed 0) of the in-order filler, so every item sees the same sequence.

    Using one sequence for all items keeps the position-identity analyses meaningful; the
    sequence is a deterministic function of the length and is recorded in the sweep output.
    """
    import random

    items = list(items)
    random.Random(0).shuffle(items)
    return items


def filler_description(filler_type: str) -> str:
    return {
        "dots": "dots",
        "counting": "counting numbers",
        "alphabet": "letters",
        "alphabet-scrambled": "letters in scrambled order",
        "counting-scrambled": "numbers in scrambled order",
    }[filler_type]


def paper_filler_suffix(filler_type: str, length: int) -> str:
    """Return the filler sentence used in arXiv:2607.03502v1 Appendix A."""
    if length <= 0:
        return ""
    return (
        f" After the question, there will be {length} filler tokens "
        f"(a sequence of {filler_description(filler_type)}) before you answer."
    )


def pre_question_filler_suffix(filler_type: str, length: int) -> str:
    if length <= 0:
        return ""
    return (
        f" Before the variable definitions and question, there will be {length} "
        f"filler tokens (a sequence of {filler_description(filler_type)})."
    )


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
    return text + paper_filler_suffix(filler_type, length)


def build_repeated_squaring_system_message(filler_type: str, length: int) -> str:
    text = (
        "You will be given integers x, N, and T. Set x_0 = x mod N, then "
        "repeatedly apply x_t = x_(t-1)^2 mod N exactly T times. "
        "Answer immediately with just x_T as a base-10 integer, nothing else. "
        "No explanation, no words, no reasoning, just the number."
    )
    return text + paper_filler_suffix(filler_type, length)


def build_fact_plus_number_system_message(filler_type: str, length: int) -> str:
    text = (
        "You will be given a question that requires recalling one value and adding "
        "a supplied number to it. Answer immediately with just the number, nothing "
        "else. No explanation, no words, no reasoning, just the number."
    )
    return text + paper_filler_suffix(filler_type, length)


def build_letter_position_system_message(filler_type: str, length: int) -> str:
    """System message from the released letter-position prompt scaffold."""
    text = (
        "You will be given a question asking for a specific letter. "
        "Answer immediately with just the single lowercase letter, nothing else. "
        "No explanation, no words, no reasoning, just the letter."
    )
    return text + paper_filler_suffix(filler_type, length)


def build_variable_binding_system_message(filler_type: str, length: int) -> str:
    """System message from the released chained-variable prompt scaffold."""
    text = (
        "You will be given a list of variable definitions followed by a question. "
        "Each variable equals either a number or an expression that refers to an "
        "earlier variable (for example 'twice the number for X plus 3'). Resolve "
        "the references to work out the value the question asks for, then answer "
        "immediately with just the number, nothing else. No explanation, no words, "
        "no reasoning, just the number."
    )
    return text + paper_filler_suffix(filler_type, length)


def build_variable_binding_pre_filler_system_message(
    filler_type: str, length: int
) -> str:
    text = build_variable_binding_system_message(filler_type, 0)
    return text + pre_question_filler_suffix(filler_type, length)


def build_pointer_chase_system_message(filler_type: str, length: int) -> str:
    text = (
        "You will be given a lookup table defining a function f, a starting value "
        "x_0, and a number of steps T. Repeatedly apply x_t = f(x_(t-1)) exactly "
        "T times. Answer immediately with just x_T as a base-10 integer, nothing "
        "else. No explanation, no words, no reasoning, just the number."
    )
    return text + paper_filler_suffix(filler_type, length)


def build_arithmetic_program_system_message(filler_type: str, length: int) -> str:
    text = (
        "You will be given integer inputs followed by a straight-line arithmetic "
        "program. Execute the assignments exactly in the order shown. Answer "
        "immediately with just the queried integer, nothing else. No explanation, "
        "no words, no reasoning, just the number."
    )
    return text + paper_filler_suffix(filler_type, length)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def build_user_turn(item: dict[str, Any], filler_type: str, length: int) -> str:
    question = f"Question: What is {' plus '.join(_fact_phrases(item))}?"
    if length:
        return f"{question}\n\nFiller: {make_filler(filler_type, length)}\n\nAnswer:"
    return f"{question}\n\nAnswer:"


def build_fact_plus_number_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    if "fact_phrase" not in item or "x" not in item:
        raise ValueError("fact-plus-number items require fact_phrase and x")
    question = f"Question: What is {item['fact_phrase']} plus {item['x']}?"
    if length:
        return f"{question}\n\nFiller: {make_filler(filler_type, length)}\n\nAnswer:"
    return f"{question}\n\nAnswer:"


def build_letter_position_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    question = str(item.get("question", "")).strip()
    if not question:
        raise ValueError("letter-position items require a question")
    question_line = f"Question: {question}"
    if length:
        return (
            f"{question_line}\n\nFiller: {make_filler(filler_type, length)}"
            "\n\nAnswer:"
        )
    return f"{question_line}\n\nAnswer:"


def build_variable_binding_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    definitions = item.get("definitions")
    if not isinstance(definitions, list) or not definitions:
        raise ValueError("variable-binding items require definitions")
    rendered_definitions: list[str] = []
    seen: set[str] = set()
    for definition in definitions:
        if not isinstance(definition, (list, tuple)) or len(definition) != 2:
            raise ValueError("each variable definition must be a name/value pair")
        name, value = definition
        name = str(name)
        if name in seen:
            raise ValueError(f"duplicate variable definition: {name}")
        seen.add(name)
        rendered_definitions.append(f"{name} = {value}")
    question = str(item.get("question", "")).strip()
    if not question:
        raise ValueError("variable-binding items require a question")
    question_line = "\n".join(rendered_definitions) + f"\nQuestion: {question}"
    if length:
        return (
            f"{question_line}\n\nFiller: {make_filler(filler_type, length)}"
            "\n\nAnswer:"
        )
    return f"{question_line}\n\nAnswer:"


def build_variable_binding_pre_filler_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    ordinary = build_variable_binding_user_turn(item, filler_type, 0)
    if length:
        return f"Filler: {make_filler(filler_type, length)}\n\n{ordinary}"
    return ordinary


def build_pointer_chase_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    raw_mapping = item.get("mapping")
    if not isinstance(raw_mapping, list) or not raw_mapping:
        raise ValueError("pointer-chase items require a nonempty mapping")
    mapping: dict[int, int] = {}
    rendered_mapping: list[str] = []
    for entry in raw_mapping:
        if not isinstance(entry, (list, tuple)) or len(entry) != 2:
            raise ValueError("each pointer mapping entry must be a source/destination pair")
        source, destination = map(int, entry)
        if source in mapping:
            raise ValueError(f"duplicate pointer source: {source}")
        mapping[source] = destination
        rendered_mapping.append(f"f({source}) = {destination}")
    if any(destination not in mapping for destination in mapping.values()):
        raise ValueError("pointer destinations must all appear in the mapping domain")
    start = int(item["start"])
    time_steps = int(item["time_steps"])
    if start not in mapping or time_steps < 0:
        raise ValueError("pointer chase requires a mapped start and T >= 0")
    value = start
    trace: list[int] = []
    for _ in range(time_steps):
        value = mapping[value]
        trace.append(value)
    if int(item["answer"]) != value:
        raise ValueError(f"pointer-chase answer {item['answer']} does not match {value}")
    expected = item.get("expected_intermediates")
    if expected is not None and list(map(int, expected.values())) != trace:
        raise ValueError("expected intermediates do not match the pointer trace")
    question = (
        "\n".join(rendered_mapping)
        + f"\nQuestion: Starting with x_0 = {start}, repeatedly apply "
        + f"x_t = f(x_(t-1)) for exactly {time_steps} steps. What is x_{time_steps}?"
    )
    if length:
        return f"{question}\n\nFiller: {make_filler(filler_type, length)}\n\nAnswer:"
    return f"{question}\n\nAnswer:"


def build_arithmetic_program_user_turn(
    item: dict[str, Any], filler_type: str, length: int
) -> str:
    """Render and independently validate a small straight-line integer program."""
    raw_inputs = item.get("inputs")
    raw_operations = item.get("operations")
    query = str(item.get("query", "")).strip()
    if not isinstance(raw_inputs, list) or not raw_inputs:
        raise ValueError("arithmetic-program items require nonempty inputs")
    if not isinstance(raw_operations, list) or not raw_operations:
        raise ValueError("arithmetic-program items require nonempty operations")
    if not query:
        raise ValueError("arithmetic-program items require a query variable")

    values: dict[str, int] = {}
    rendered: list[str] = []
    for entry in raw_inputs:
        if not isinstance(entry, (list, tuple)) or len(entry) != 2:
            raise ValueError("each arithmetic input must be a name/value pair")
        name, raw_value = str(entry[0]), entry[1]
        if name in values:
            raise ValueError(f"duplicate arithmetic variable: {name}")
        value = int(raw_value)
        values[name] = value
        rendered.append(f"{name} = {value}")

    trace: dict[str, str] = {}
    symbols = {"add": "+", "subtract": "-", "multiply": "*"}
    for entry in raw_operations:
        if not isinstance(entry, (list, tuple)) or len(entry) != 4:
            raise ValueError(
                "each arithmetic operation must be [output, left, operator, right]"
            )
        output, left, operator, right = map(str, entry)
        if output in values:
            raise ValueError(f"duplicate arithmetic variable: {output}")
        if left not in values or right not in values:
            raise ValueError(
                f"operation {output} refers to an undefined or future variable"
            )
        if operator == "add":
            value = values[left] + values[right]
        elif operator == "subtract":
            value = values[left] - values[right]
        elif operator == "multiply":
            value = values[left] * values[right]
        else:
            raise ValueError(f"unsupported arithmetic operator: {operator}")
        values[output] = value
        trace[output] = str(value)
        rendered.append(f"{output} = {left} {symbols[operator]} {right}")

    if query not in values:
        raise ValueError(f"arithmetic query variable is undefined: {query}")
    if int(item["answer"]) != values[query]:
        raise ValueError(
            f"arithmetic-program answer {item['answer']} does not match {values[query]}"
        )
    expected = item.get("expected_intermediates")
    if expected is not None and {
        str(name): str(value) for name, value in expected.items()
    } != trace:
        raise ValueError("expected intermediates do not match the arithmetic trace")

    question = "\n".join(rendered) + f"\nQuestion: What is the value of {query}?"
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
    target_length: int | None = None,
    announce_mode: str = "both",
) -> list[dict[str, str]]:
    """`length` sets the filler count announced in the system message and rendered in every demonstration;
    `target_length` (default: same) sets the count rendered in the target turn. `target_length=0` with
    `length=50` is the "announced but absent" control."""
    if target_length is None:
        target_length = length
    if announce_mode not in ("both", "sentence", "demos", "none"):
        raise ValueError(f"unsupported announce_mode: {announce_mode}")   # "none": filler only in the target
    system_length = length if announce_mode in ("both", "sentence") else 0   # "demos": no filler sentence
    demo_length = length if announce_mode in ("both", "demos") else 0        # "sentence": demos without filler
    if task_type == "addition":
        fact_count = len(_fact_phrases(target))
        for item in few_shot:
            if len(_fact_phrases(item)) != fact_count:
                raise ValueError("few-shot and target items must use the same number of facts")
        system_message = build_system_message(filler_type, system_length, fact_count)
        user_builder = build_user_turn
    else:
        task_builders = {
            "repeated_squaring_mod": (
                build_repeated_squaring_system_message,
                build_repeated_squaring_user_turn,
            ),
            "fact_plus_number": (
                build_fact_plus_number_system_message,
                build_fact_plus_number_user_turn,
            ),
            "letter_position": (
                build_letter_position_system_message,
                build_letter_position_user_turn,
            ),
            "variable_binding": (
                build_variable_binding_system_message,
                build_variable_binding_user_turn,
            ),
            "variable_binding_pre_filler": (
                build_variable_binding_pre_filler_system_message,
                build_variable_binding_pre_filler_user_turn,
            ),
            "pointer_chase": (
                build_pointer_chase_system_message,
                build_pointer_chase_user_turn,
            ),
            "arithmetic_program": (
                build_arithmetic_program_system_message,
                build_arithmetic_program_user_turn,
            ),
        }
        if task_type not in task_builders:
            raise ValueError(f"unsupported task type: {task_type}")
        system_builder, user_builder = task_builders[task_type]
        system_message = system_builder(filler_type, system_length)

    messages: list[dict[str, str]] = [
        {"role": "system", "content": system_message}
    ]
    for item in few_shot:
        messages.append(
            {"role": "user", "content": user_builder(item, filler_type, demo_length)}
        )
        messages.append({"role": "assistant", "content": str(item["answer"])})
    messages.append(
        {"role": "user", "content": user_builder(target, filler_type, target_length)}
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
    filler_placement: str = "between_question_answer",
) -> TokenAlignment:
    """Find the target turn's filler and answer cue without token assumptions."""
    if filler_placement == "between_question_answer":
        filler_marker = f"Filler: {filler_surface}\n\nAnswer:"
        answer_offset = len(f"Filler: {filler_surface}\n\n")
    elif filler_placement == "before_question":
        filler_marker = f"Filler: {filler_surface}\n\n"
        answer_offset = None
    else:
        raise ValueError(f"unsupported filler placement: {filler_placement}")
    marker_start = rendered_prompt.rfind(filler_marker)
    if marker_start < 0:
        raise ValueError("target filler marker was not found in rendered prompt")
    filler_start = marker_start + len("Filler: ")
    filler_span = (filler_start, filler_start + len(filler_surface))

    if answer_offset is None:
        answer_start = rendered_prompt.rfind("Answer:", marker_start)
        if answer_start < 0:
            raise ValueError("target answer cue was not found after pre-question filler")
    else:
        answer_start = marker_start + answer_offset
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
    filler_placement: str = "between_question_answer",
) -> tuple[str, TokenAlignment]:
    rendered = encode_messages(messages, thinking_mode="chat")
    alignment = align_rendered_prompt(
        tokenizer,
        rendered,
        make_filler(filler_type, filler_length),
        filler_placement=filler_placement,
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
