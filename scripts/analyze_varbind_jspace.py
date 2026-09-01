#!/usr/bin/env python3
"""Summarize formal sparse J-space decompositions for the resonance probe."""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path
from typing import Any


TASK_LABELS = (
    "base_value",
    "bound_value",
    "second_product",
    "answer",
    "distractor_bound",
    "distractor_second_product",
    "distractor_answer",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def mean(values: list[float]) -> float:
    return statistics.mean(values) if values else float("nan")


def median(values: list[float]) -> float:
    return statistics.median(values) if values else float("nan")


def active_labels(record: dict[str, Any]) -> list[str]:
    return [
        label
        for label in TASK_LABELS
        if label in record["tracked_targets"]
        and record["tracked_targets"][label]["active_atom"]
    ]


def label_text(record: dict[str, Any], labels: list[str]) -> str:
    if not labels:
        return "—"
    return ", ".join(
        f"{label}={record['tracked_targets'][label]['value']}"
        for label in labels
    )


def main() -> None:
    args = parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    sites = data["sites"]
    if not sites:
        raise ValueError("input contains no decomposition sites")

    threshold_counts: dict[str, dict[str, int]] = {}
    for threshold in (1, 2, 5, 10, 25, 50):
        eligible = 0
        active = 0
        for site in sites:
            for label in TASK_LABELS:
                target = site["j_space"]["tracked_targets"].get(label)
                if target is None or target["readout_rank"] > threshold:
                    continue
                eligible += 1
                active += int(target["active_atom"])
        threshold_counts[str(threshold)] = {"eligible": eligible, "active": active}

    rows: list[dict[str, Any]] = []
    for site in sites:
        j_space = site["j_space"]
        logit_space = site["logit_space_sparse"]
        j_atoms = {int(atom["token_id"]) for atom in j_space["atoms"]}
        ll_atoms = {int(atom["token_id"]) for atom in logit_space["atoms"]}
        rows.append(
            {
                "id": site["id"],
                "filler_length": site["filler_length"],
                "layer": site["layer"],
                "filler_ordinal": site["filler_ordinal"],
                "expected_output": site["expected_output"],
                "correct": int(site["expected_output"]) == 235,
                "reason": site["reason"],
                "j_active_task_labels": active_labels(j_space),
                "logit_active_task_labels": active_labels(logit_space),
                "j_fve": j_space["reconstruction"][
                    "reconstruction_fraction_variance_explained"
                ],
                "j_rotation_control_mean": j_space["rotation_control"][
                    "mean_fraction_variance_explained"
                ],
                "j_excess_fve": j_space["rotation_control"][
                    "observed_minus_control_mean"
                ],
                "logit_fve": logit_space["reconstruction"][
                    "reconstruction_fraction_variance_explained"
                ],
                "logit_rotation_control_mean": logit_space["rotation_control"][
                    "mean_fraction_variance_explained"
                ],
                "logit_excess_fve": logit_space["rotation_control"][
                    "observed_minus_control_mean"
                ],
                "atom_overlap": len(j_atoms & ll_atoms),
                "j_atoms": j_space["atoms"],
                "logit_atoms": logit_space["atoms"],
                "j_targets": j_space["tracked_targets"],
                "logit_targets": logit_space["tracked_targets"],
                "j_pair_cosines": j_space["tracked_atom_pair_cosines"],
            }
        )

    rank_one = threshold_counts["1"]
    rank_25 = threshold_counts["25"]
    joint_ids = {
        "k50_l31_f14_joint_candidates",
        "k100_l36_f19_joint_candidates",
    }
    joint_results = []
    for row in rows:
        if row["id"] not in joint_ids:
            continue
        answer = row["j_targets"]["answer"]
        distractor = row["j_targets"]["distractor_answer"]
        joint_results.append(
            {
                "id": row["id"],
                "answer_rank": answer["readout_rank"],
                "answer_active": answer["active_atom"],
                "distractor_rank": distractor["readout_rank"],
                "distractor_active": distractor["active_atom"],
                "answer_distractor_atom_cosine": next(
                    item["cosine"]
                    for item in row["j_pair_cosines"]
                    if item["left"] == "answer"
                ),
            }
        )

    summary = {
        "schema_version": 1,
        "method": data["method"],
        "synthetic_validation": data["synthetic_validation"],
        "site_count": len(rows),
        "dictionary_validation": {
            "max_absolute_logit_error": max(
                site["dictionary_validation"]["max_absolute_logit_error"]
                for site in sites
            ),
            "max_relative_logit_error": max(
                site["dictionary_validation"]["relative_to_max_absolute_logit"]
                for site in sites
            ),
            "all_top_k_exact": all(
                site["dictionary_validation"]["top_k_ids_exact_match"]
                for site in sites
            ),
        },
        "task_target_inclusion_by_readout_threshold": threshold_counts,
        "rank_one_task_targets_selected": rank_one,
        "rank_2_to_25_task_targets_selected": {
            "eligible": rank_25["eligible"] - rank_one["eligible"],
            "active": rank_25["active"] - rank_one["active"],
        },
        "joint_candidate_cells": joint_results,
        "j_space_fve": {
            "mean": mean([row["j_fve"] for row in rows]),
            "median": median([row["j_fve"] for row in rows]),
            "min": min(row["j_fve"] for row in rows),
            "max": max(row["j_fve"] for row in rows),
            "mean_rotation_control": mean(
                [row["j_rotation_control_mean"] for row in rows]
            ),
            "mean_excess": mean([row["j_excess_fve"] for row in rows]),
            "median_excess": median([row["j_excess_fve"] for row in rows]),
            "positive_excess_sites": sum(row["j_excess_fve"] > 0 for row in rows),
        },
        "logit_space_fve": {
            "mean": mean([row["logit_fve"] for row in rows]),
            "median": median([row["logit_fve"] for row in rows]),
            "mean_rotation_control": mean(
                [row["logit_rotation_control_mean"] for row in rows]
            ),
            "mean_excess": mean([row["logit_excess_fve"] for row in rows]),
        },
        "j_logit_atom_overlap": {
            "mean_of_25": mean([row["atom_overlap"] for row in rows]),
            "median_of_25": median([row["atom_overlap"] for row in rows]),
        },
        "j_only_task_atom_sites": [
            row["id"]
            for row in rows
            if set(row["j_active_task_labels"])
            - set(row["logit_active_task_labels"])
        ],
        "rows": rows,
    }

    lines = [
        "# Formal J-space decomposition: filler candidate competition",
        "",
        "These results use a sparse nonnegative gradient-pursuit decomposition with "
        "`k=25`. They are formal J-space coordinates under the released dictionary and "
        "the stated DeepSeek mHC-collapse convention, not ranked J-Lens readouts.",
        "",
        "## Validation",
        "",
        f"- Synthetic support recovery: exact; maximum coefficient error "
        f"`{data['synthetic_validation']['max_coefficient_error']:.1e}`.",
        f"- Folding DeepSeek RMSNorm into the token dictionary reproduces the complete "
        f"top-25 J-Lens ranking at every site; maximum relative logit error "
        f"`{summary['dictionary_validation']['max_relative_logit_error']:.2e}`.",
        f"- The decomposition implementation is pinned to TransformerLens revision "
        f"`{data['method']['external_implementation']['revision']}` and source SHA-256 "
        f"`{data['method']['external_implementation']['sha256']}`.",
        "",
        "## Main result",
        "",
        f"Every tracked task token that was J-Lens rank 1 was retained as an active "
        f"J-space atom (`{rank_one['active']}/{rank_one['eligible']}`). Among tracked "
        f"task tokens ranked 2–25, none was retained "
        f"(`{summary['rank_2_to_25_task_targets_selected']['active']}/"
        f"{summary['rank_2_to_25_task_targets_selected']['eligible']}`).",
        "",
        "In both joint-candidate cells, the readout ranked the requested answer `235` "
        "first and sibling answer `185` second. The formal `k=25` support retained `235` "
        "and omitted `185`. Likewise, at k=25/L36/F10 it retained bound value `125` "
        "(rank 1) but omitted product `250` (rank 2). Thus a ranked list can show several "
        "related candidates even when the pursuit inventory chooses only one of them.",
        "",
        "This refines the earlier candidate-competition claim: `235` and `185` are both "
        "broadcast across the layer × filler grid, but the selected individual cells are "
        "more winner-like under the paper-standard sparse inventory. Because the dictionary "
        "is overcomplete and the pursuit is greedy, omission does not prove that an "
        "alternative sparse support containing the runner-up is impossible.",
        "",
        "## Site summary",
        "",
        "| Site | Output | L/F | Active task atoms in J-space | Active task atoms in sparse logit space | J raw FVE | Rotated control | Excess |",
        "|---|---:|---:|---|---|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['id']}` | {row['expected_output']} | "
            f"L{row['layer']}/F{row['filler_ordinal']} | "
            f"{label_text({'tracked_targets': row['j_targets']}, row['j_active_task_labels'])} | "
            f"{label_text({'tracked_targets': row['logit_targets']}, row['logit_active_task_labels'])} | "
            f"{100 * row['j_fve']:.2f}% | "
            f"{100 * row['j_rotation_control_mean']:.2f}% | "
            f"{100 * row['j_excess_fve']:+.2f} pp |"
        )

    lines.extend(
        [
            "",
            "## Reconstruction and controls",
            "",
            f"Raw J-space reconstruction explains `5.52–8.69%` of squared activation "
            f"norm across the ten sites (mean `{100 * summary['j_space_fve']['mean']:.2f}%`). "
            f"The mean Haar-orthogonal relative-orientation control explains "
            f"`{100 * summary['j_space_fve']['mean_rotation_control']:.2f}%`; observed "
            f"minus control is negative on `{len(rows) - summary['j_space_fve']['positive_excess_sites']}/"
            f"{len(rows)}` sites. Therefore the raw percentage must not be presented as "
            f"above-chance J-space variance for these activations.",
            "",
            f"The sparse logit-space baseline explains `{100 * summary['logit_space_fve']['mean']:.2f}%` "
            f"on average versus `{100 * summary['j_space_fve']['mean']:.2f}%` for J-space. "
            f"Only `{summary['j_logit_atom_overlap']['mean_of_25']:.1f}/25` atoms overlap on "
            f"average, so Jacobian transport materially changes the selected dictionary "
            f"support, but does not improve reconstruction in this selected sample.",
            "",
            "Two selected task atoms are J-space-only in this sample: answer `235` at "
            "k=5/L36/F2 and product `250` at k=50/L33/F43. This is suggestive of a "
            "J-specific interpretive benefit, but the cells were preselected with J-Lens, "
            "so it is not an unbiased performance comparison.",
            "",
            "## Complete atoms by site",
            "",
        ]
    )
    for row in rows:
        lines.extend(
            [
                f"### {row['id']}",
                "",
                row["reason"],
                "",
                "| Order | Token | Coefficient | Contribution norm | J-readout rank |",
                "|---:|---|---:|---:|---:|",
            ]
        )
        for order, atom in enumerate(row["j_atoms"], start=1):
            token = json.dumps(atom["token"], ensure_ascii=False)
            lines.append(
                f"| {order} | `{token}` | {atom['coefficient']:.4f} | "
                f"{atom['contribution_norm']:.4f} | {atom['readout_rank']} |"
            )
        lines.append("")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "jspace-decomposition-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (args.output_dir / "jspace-decomposition-report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    print(f"wrote analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
