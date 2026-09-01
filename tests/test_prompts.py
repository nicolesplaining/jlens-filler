from jlens_filler.prompts import build_messages, make_filler


def test_dot_filler_surface_count():
    assert make_filler("dots", 10) == ". . . . . . . . . ."


def test_dot_system_message_matches_paper_filler_sentence():
    item = {"fact_phrase_1": "A", "fact_phrase_2": "B", "answer": 3}
    messages = build_messages([], item, "dots", 10)
    assert messages[0]["content"].endswith(
        "After the question, there will be 10 filler tokens "
        "(a sequence of dots) before you answer."
    )
    assert "some filler tokens" not in messages[0]["content"]
    assert "extra space" not in messages[0]["content"]


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
    assert messages[0]["content"].endswith(
        "After the question, there will be 10 filler tokens "
        "(a sequence of dots) before you answer."
    )
    assert "x_0 = 12 mod 437" in messages[-1]["content"]
    assert "for exactly 10 steps" in messages[-1]["content"]
    assert "19" not in messages[-1]["content"]
    assert "23" not in messages[-1]["content"]
    assert messages[-1]["content"].endswith(
        "Filler: . . . . . . . . . .\n\nAnswer:"
    )


def test_variable_binding_prompt_matches_released_scaffold():
    item = {
        "definitions": [["yuf", 59], ["xel", "twice the number for yuf minus 1"]],
        "question": "What is twice the number for xel minus 15?",
        "answer": 219,
    }
    messages = build_messages([], item, "dots", 3, task_type="variable_binding")
    assert "list of variable definitions" in messages[0]["content"]
    assert messages[0]["content"].endswith(
        "After the question, there will be 3 filler tokens "
        "(a sequence of dots) before you answer."
    )
    assert messages[-1]["content"] == (
        "yuf = 59\n"
        "xel = twice the number for yuf minus 1\n"
        "Question: What is twice the number for xel minus 15?\n\n"
        "Filler: . . .\n\nAnswer:"
    )


def test_variable_binding_pre_question_filler_control():
    item = {
        "definitions": [["yuf", 59], ["xel", "twice the number for yuf minus 1"]],
        "question": "What is twice the number for xel minus 15?",
        "answer": 219,
    }
    messages = build_messages(
        [], item, "dots", 3, task_type="variable_binding_pre_filler"
    )
    assert "Before the variable definitions and question" in messages[0]["content"]
    assert messages[-1]["content"] == (
        "Filler: . . .\n\n"
        "yuf = 59\n"
        "xel = twice the number for yuf minus 1\n"
        "Question: What is twice the number for xel minus 15?\n\n"
        "Answer:"
    )


def test_letter_position_prompt_and_string_answer():
    item = {
        "question": "What is the last letter of the name of the capital of France?",
        "answer": "s",
    }
    messages = build_messages([], item, "dots", 2, task_type="letter_position")
    assert "single lowercase letter" in messages[0]["content"]
    assert messages[-1]["content"].endswith("Filler: . .\n\nAnswer:")


def test_fact_plus_number_prompt():
    item = {
        "fact_phrase": "the atomic number of tungsten",
        "x": 6,
        "answer": 80,
    }
    messages = build_messages([], item, "dots", 2, task_type="fact_plus_number")
    assert "recalling one value" in messages[0]["content"]
    assert "What is the atomic number of tungsten plus 6?" in messages[-1]["content"]


def test_pointer_chase_prompt_validates_trace():
    item = {
        "mapping": [[0, 2], [1, 0], [2, 3], [3, 1]],
        "start": 0,
        "time_steps": 3,
        "answer": 1,
        "expected_intermediates": {"x1": "2", "x2": "3", "x3": "1"},
    }
    messages = build_messages([], item, "dots", 4, task_type="pointer_chase")
    content = messages[-1]["content"]
    assert "f(0) = 2" in content
    assert "What is x_3?" in content
    assert content.endswith("Filler: . . . .\n\nAnswer:")


def test_arithmetic_program_prompt_validates_hidden_trace():
    item = {
        "inputs": [["a", 3], ["b", 4], ["c", 2]],
        "operations": [
            ["left", "a", "add", "b"],
            ["answer", "left", "multiply", "c"],
        ],
        "query": "answer",
        "answer": 14,
        "expected_intermediates": {"left": "7", "answer": "14"},
    }
    messages = build_messages([], item, "dots", 3, task_type="arithmetic_program")
    assert "straight-line arithmetic program" in messages[0]["content"]
    assert messages[-1]["content"] == (
        "a = 3\n"
        "b = 4\n"
        "c = 2\n"
        "left = a + b\n"
        "answer = left * c\n"
        "Question: What is the value of answer?\n\n"
        "Filler: . . .\n\nAnswer:"
    )
