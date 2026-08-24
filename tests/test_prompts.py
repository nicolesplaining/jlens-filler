from jlens_filler.prompts import build_messages, make_filler


def test_dot_filler_surface_count():
    assert make_filler("dots", 10) == ". . . . . . . . . ."


def test_filler_between_question_and_answer():
    item = {"fact_phrase_1": "A", "fact_phrase_2": "B", "answer": 3}
    messages = build_messages([], item, "dots", 3)
    content = messages[-1]["content"]
    assert content.index("Question:") < content.index("Filler:") < content.index("Answer:")

