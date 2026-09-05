"""Small, testable helpers for decoder-gradient activation interventions."""

from __future__ import annotations

import hashlib
from collections.abc import Callable, Iterable
from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class SuppressionStep:
    delta: torch.Tensor
    baseline_score: float
    resulting_score: float
    requested_drop: float
    achieved_drop: float
    step_norm: float
    relative_step_norm: float
    capped: bool


def stable_seed(*parts: object) -> int:
    """Return a process-independent 63-bit seed for named controls."""
    digest = hashlib.sha256("\x1f".join(map(str, parts)).encode()).digest()
    return int.from_bytes(digest[:8], "big") & ((1 << 63) - 1)


def unit_direction(vector: torch.Tensor, *, eps: float = 1e-20) -> torch.Tensor:
    norm = vector.float().norm()
    if float(norm) <= eps:
        raise ValueError("cannot normalize a zero direction")
    return vector.float() / norm


def orthogonal_component(
    vector: torch.Tensor, reference: torch.Tensor, *, eps: float = 1e-20
) -> torch.Tensor:
    """Remove the Euclidean projection of ``vector`` onto ``reference``."""
    vector_f = vector.float()
    reference_f = reference.float()
    denominator = reference_f.square().sum()
    if float(denominator) <= eps:
        raise ValueError("reference direction is zero")
    return vector_f - reference_f * (
        torch.sum(vector_f * reference_f) / denominator
    )


def orthogonalize(
    vector: torch.Tensor, references: Iterable[torch.Tensor]
) -> torch.Tensor:
    output = vector.float()
    for reference in references:
        output = orthogonal_component(output, reference)
    return output


def orthonormal_basis(
    vectors: Iterable[torch.Tensor], *, relative_tolerance: float = 1e-6
) -> torch.Tensor:
    """Build a flattened Euclidean basis with modified Gram-Schmidt."""

    if relative_tolerance <= 0:
        raise ValueError("relative_tolerance must be positive")
    flattened = [vector.detach().float().reshape(-1) for vector in vectors]
    if not flattened:
        raise ValueError("at least one vector is required")
    width = flattened[0].numel()
    if any(vector.numel() != width for vector in flattened):
        raise ValueError("all vectors must have the same number of elements")
    scale = max(float(vector.norm()) for vector in flattened)
    if scale == 0:
        raise ValueError("all candidate vectors are zero")
    basis: list[torch.Tensor] = []
    for vector in flattened:
        residual = vector.clone()
        # Re-orthogonalize once because decoder gradients can be correlated.
        for _ in range(2):
            for direction in basis:
                residual -= direction * torch.dot(direction, residual)
        norm = float(residual.norm())
        if norm > relative_tolerance * scale:
            basis.append(residual / norm)
    if not basis:
        raise ValueError("candidate vectors have no nonzero span")
    return torch.stack(basis, dim=1)


def project_onto_basis(vector: torch.Tensor, basis: torch.Tensor) -> torch.Tensor:
    """Project an arbitrary-shaped vector onto a flattened orthonormal basis."""

    flattened = vector.float().reshape(-1)
    if basis.ndim != 2 or basis.shape[0] != flattened.numel():
        raise ValueError("basis shape is incompatible with vector")
    projected = basis @ (basis.T @ flattened)
    return projected.reshape_as(vector)


def cosine(left: torch.Tensor, right: torch.Tensor, *, eps: float = 1e-20) -> float:
    left_f, right_f = left.float(), right.float()
    denominator = left_f.norm() * right_f.norm()
    if float(denominator) <= eps:
        return float("nan")
    return float(torch.sum(left_f * right_f) / denominator)


def matched_delta(
    gradient: torch.Tensor, step_norm: float, *, suppress: bool = True
) -> torch.Tensor:
    sign = -1.0 if suppress else 1.0
    return sign * float(step_norm) * unit_direction(gradient)


@torch.no_grad()
def find_suppression_step(
    score_fn: Callable[[torch.Tensor], torch.Tensor],
    activation: torch.Tensor,
    gradient: torch.Tensor,
    *,
    requested_drop: float,
    max_relative_norm: float,
    bisection_steps: int = 18,
) -> SuppressionStep:
    """Line-search the steepest local direction for a requested score decrease.

    The returned perturbation is parallel to ``-gradient``.  The search is capped
    by ``max_relative_norm * ||activation||`` so a weak decoder gradient cannot
    silently produce an enormous off-manifold edit.
    """
    if requested_drop <= 0:
        raise ValueError("requested_drop must be positive")
    if not 0 < max_relative_norm <= 1:
        raise ValueError("max_relative_norm must lie in (0, 1]")
    if bisection_steps < 1:
        raise ValueError("bisection_steps must be positive")

    activation_f = activation.detach().float()
    gradient_f = gradient.detach().float()
    direction = -unit_direction(gradient_f)
    baseline = float(score_fn(activation_f))
    target = baseline - float(requested_drop)
    activation_norm = float(activation_f.norm())
    cap = float(max_relative_norm) * activation_norm
    if cap <= 0:
        raise ValueError("activation norm is zero")

    gradient_norm = float(gradient_f.norm())
    high = min(cap, max(float(requested_drop) / gradient_norm * 1.25, cap / 1024))

    def score_at(distance: float) -> float:
        return float(score_fn(activation_f + direction * distance))

    high_score = score_at(high)
    while high < cap and high_score > target:
        high = min(cap, high * 2)
        high_score = score_at(high)

    capped = high_score > target
    if not capped:
        low = 0.0
        for _ in range(bisection_steps):
            middle = (low + high) / 2
            if score_at(middle) <= target:
                high = middle
            else:
                low = middle
        high_score = score_at(high)

    delta = direction * high
    return SuppressionStep(
        delta=delta,
        baseline_score=baseline,
        resulting_score=high_score,
        requested_drop=float(requested_drop),
        achieved_drop=baseline - high_score,
        step_norm=float(delta.norm()),
        relative_step_norm=float(delta.norm()) / activation_norm,
        capped=capped,
    )


def find_amplification_step(
    score_fn: Callable[[torch.Tensor], torch.Tensor],
    activation: torch.Tensor,
    gradient: torch.Tensor,
    *,
    requested_increase: float,
    max_relative_norm: float,
    bisection_steps: int = 18,
) -> SuppressionStep:
    """Line-search the steepest local direction for a requested score increase."""

    suppression = find_suppression_step(
        lambda value: -score_fn(value),
        activation,
        -gradient,
        requested_drop=requested_increase,
        max_relative_norm=max_relative_norm,
        bisection_steps=bisection_steps,
    )
    return SuppressionStep(
        delta=suppression.delta,
        baseline_score=-suppression.baseline_score,
        resulting_score=-suppression.resulting_score,
        requested_drop=suppression.requested_drop,
        achieved_drop=suppression.achieved_drop,
        step_norm=suppression.step_norm,
        relative_step_norm=suppression.relative_step_norm,
        capped=suppression.capped,
    )
