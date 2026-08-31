from jlens_filler.prompts import build_messages, make_filler


def test_dot_filler_surface_count():
    assert make_filler("dots", 10) == ". . . . . . . . . ."


def test_filler_between_question_and_answer():
    item = {"fact_phrase_1": "A", "fact_phrase_2": "B", "answer": 3}
    messages = build_messages([], item, "dots", 3)
    content = messages[-1]["content"]
    assert content.index("Question:") < content.index("Filler:") < content.index("Answer:")


def test_three_fact_prompt_and_system_message():
    item = {
        "fact_phrase_1": "A",
        "fact_phrase_2": "B",
        "fact_phrase_3": "C",
        "answer": 6,
    }
    messages = build_messages([], item, "dots", 3)
    assert "adding three values together" in messages[0]["content"]
    assert "Question: What is A plus B plus C?" in messages[-1]["content"]


def test_mixed_fact_counts_are_rejected():
    two_fact = {"fact_phrase_1": "A", "fact_phrase_2": "B", "answer": 3}
    three_fact = {
        "fact_phrase_1": "A",
        "fact_phrase_2": "B",
        "fact_phrase_3": "C",
        "answer": 6,
    }
    try:
        build_messages([two_fact], three_fact, "dots", 3)
    except ValueError as error:
        assert "same number of facts" in str(error)
    else:
        raise AssertionError("mixed fact counts should be rejected")


def test_repeated_squaring_prompt():
    item = {
        "modulus": 437,
        "factorization_for_validation_only": [19, 23],
        "x": 12,
        "time_steps": 10,
        "answer": 311,
    }
    messages = build_messages(
        [], item, "dots", 10, task_type="repeated_squaring_mod"
    )
    assert "apply x_t = x_(t-1)^2 mod N exactly T times" in messages[0]["content"]
    assert "x_0 = 12 mod 437" in messages[-1]["content"]
    assert "for exactly 10 steps" in messages[-1]["content"]
    assert "19" not in messages[-1]["content"]
    assert "23" not in messages[-1]["content"]
    assert messages[-1]["content"].endswith(
        "Filler: . . . . . . . . . .\n\nAnswer:"
    )
