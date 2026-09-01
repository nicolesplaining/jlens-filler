# Variable-binding filler workspace: readout and causal deep dive

All decoded values are **J-Lens token readouts**, not formal sparse J-space coordinates or a transcript of hidden reasoning.

## Exact-layout counterfactual behavior

Changing only one numeric literal yields 0 / 8 correct without filler and 8 / 8 with 50 dots (8 helped, 0 hurt).

## Geometry across all 14 examples rescued by 50 dots

| Readout | Stage↔layer ρ | Stage↔dot ρ | ≥3 stages at one layer | Ordered same-dot chains |
|---|---:|---:|---:|---:|
| J Lens | 0.590 | 0.058 | 13 / 14 | 7 / 9 |
| Logit Lens | 0.587 | 0.060 | 10 / 14 | 10 / 10 |

The stage ordering is carried mainly by transformer depth, while dot ordinal has almost no monotonic relation to stage. Multiple stages nevertheless coexist at the same layer across different dots, which is the signature expected from a width-distributed workspace rather than a left-to-right textual scratchpad.

## Causal patching pilot

Identity-patch closure error: `0.0`.

The table reports the donor answer after patching the largest 16-cell dose.

| Direction | Stage | J-Lens rank / Δlog p | Logit-lens rank / Δlog p | Random rank / Δlog p | Complement rank / Δlog p |
|---|---|---:|---:|---:|---:|
| `varbind_cf_suv_072` → `varbind_cf_suv_064` | bound value | 36 / +3.30 | 15 / +6.69 | 31 / +2.95 | 87 / -0.21 |
| `varbind_cf_suv_072` → `varbind_cf_suv_064` | second product | 2 / +10.20 | 2 / +10.43 | 16 / +5.63 | 83 / +0.18 |
| `varbind_cf_suv_072` → `varbind_cf_suv_064` | answer | 4 / +9.53 | 4 / +9.56 | 61 / +0.80 | 88 / +0.20 |
| `varbind_cf_suv_064` → `varbind_cf_suv_072` | bound value | 8 / +7.72 | 7 / +8.62 | 27 / +4.18 | 79 / -0.12 |
| `varbind_cf_suv_064` → `varbind_cf_suv_072` | second product | 7 / +8.39 | 3 / +9.22 | 86 / +0.18 | 78 / -0.22 |
| `varbind_cf_suv_064` → `varbind_cf_suv_072` | answer | 5 / +8.68 | 7 / +7.69 | 33 / +3.89 | 84 / -0.14 |

## Single-cell causal map

Direction: `varbind_cf_suv_072` → `varbind_cf_suv_064`. The unpatched donor answer starts at rank 82. Across 500 one-cell interventions, 77 improve its log probability by at least 1 nat and 14 by at least 3 nats.

The aligned prompts differ only at index 751: `64` → `72`.

| Readout | Stage | Effect↔readout-rank ρ | Top-25 overlap | Mean effect in top-25 readout cells |
|---|---|---:|---:|---:|
| J Lens | base value | 0.175 | 0 | 0.101 |
| J Lens | first product | 0.088 | 0 | 0.238 |
| J Lens | bound value | 0.342 | 0 | 0.478 |
| J Lens | second product | 0.592 | 1 | 0.963 |
| J Lens | answer | 0.571 | 7 | 2.002 |
| Logit Lens | base value | 0.079 | 0 | 0.270 |
| Logit Lens | first product | 0.024 | 0 | 0.637 |
| Logit Lens | bound value | 0.254 | 0 | 0.449 |
| Logit Lens | second product | 0.569 | 5 | 1.277 |
| Logit Lens | answer | 0.552 | 7 | 2.016 |

Strongest causal lanes by their best single-cell intervention: dot 41 (L33, Δlog p +4.86), dot 40 (L33, Δlog p +4.25), dot 14 (L33, Δlog p +2.97), dot 28 (L33, Δlog p +2.69), dot 43 (L29, Δlog p +2.15), dot 10 (L31, Δlog p +2.11).

## Interpretation boundary

The causal map transfers a full residual vector from a matched donor; it does not isolate a single feature. A positive donor-answer effect shows that the location carries counterfactual answer-relevant information, but does not by itself prove that the displayed token direction is the sole mediator.
