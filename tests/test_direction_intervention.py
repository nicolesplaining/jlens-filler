import math

import torch

from jlens_filler.direction_intervention import (
    cosine,
    find_suppression_step,
    matched_delta,
    orthogonal_component,
    orthogonalize,
    stable_seed,
)


def test_stable_seed_is_repeatable_and_named():
    assert stable_seed("a", 1, "b") == stable_seed("a", 1, "b")
    assert stable_seed("a", 1, "b") != stable_seed("a", 2, "b")


def test_orthogonal_component_removes_reference_projection():
    vector = torch.tensor([2.0, 3.0, 4.0])
    reference = torch.tensor([1.0, 0.0, 0.0])
    result = orthogonal_component(vector, reference)
    assert torch.allclose(result, torch.tensor([0.0, 3.0, 4.0]))
    assert abs(float(torch.dot(result, reference))) < 1e-7


def test_orthogonalize_removes_multiple_orthogonal_references():
    vector = torch.tensor([2.0, 3.0, 4.0])
    result = orthogonalize(
        vector,
        [torch.tensor([1.0, 0.0, 0.0]), torch.tensor([0.0, 1.0, 0.0])],
    )
    assert torch.allclose(result, torch.tensor([0.0, 0.0, 4.0]))


def test_matched_delta_has_requested_norm_and_sign():
    gradient = torch.tensor([3.0, 4.0])
    delta = matched_delta(gradient, 2.5)
    assert math.isclose(float(delta.norm()), 2.5, rel_tol=1e-6)
    assert float(torch.dot(delta, gradient)) < 0
    assert math.isclose(cosine(delta, gradient), -1.0, abs_tol=1e-6)


def test_line_search_hits_linear_score_drop():
    weight = torch.tensor([2.0, -1.0, 0.5])
    activation = torch.tensor([4.0, 3.0, -2.0])

    def score_fn(value):
        return torch.dot(weight, value)

    step = find_suppression_step(
        score_fn,
        activation,
        weight,
        requested_drop=2.0,
        max_relative_norm=0.5,
    )
    assert not step.capped
    assert math.isclose(step.achieved_drop, 2.0, rel_tol=2e-5)
    assert math.isclose(step.step_norm, 2.0 / float(weight.norm()), rel_tol=2e-5)
    assert torch.allclose(
        step.delta,
        -weight / weight.norm() * step.step_norm,
        rtol=2e-5,
        atol=2e-5,
    )


def test_line_search_reports_cap():
    weight = torch.tensor([1.0, 0.0])
    activation = torch.tensor([1.0, 0.0])
    step = find_suppression_step(
        lambda value: torch.dot(weight, value),
        activation,
        weight,
        requested_drop=1.0,
        max_relative_norm=0.1,
    )
    assert step.capped
    assert math.isclose(step.step_norm, 0.1, rel_tol=1e-6)
    assert math.isclose(step.achieved_drop, 0.1, rel_tol=1e-6)
