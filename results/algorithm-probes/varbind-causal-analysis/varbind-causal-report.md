# Variable-binding filler workspace: readout and causal deep dive

All decoded values are **J-Lens token readouts**, not formal sparse J-space coordinates or a transcript of hidden reasoning.

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
| `varbind_easy_0033` → `varbind_easy_0002` | bound value | 14 / +0.95 | 17 / +0.89 | 11 / +2.24 | 19 / -0.06 |
| `varbind_easy_0033` → `varbind_easy_0002` | second product | 8 / +3.29 | 10 / +2.43 | 19 / +0.09 | 20 / -0.04 |
| `varbind_easy_0033` → `varbind_easy_0002` | answer | 8 / +3.59 | 8 / +3.40 | 19 / +0.20 | 19 / +0.07 |
| `varbind_easy_0002` → `varbind_easy_0033` | bound value | 3 / +6.97 | 2 / +8.72 | 26 / +0.72 | 45 / -0.16 |
| `varbind_easy_0002` → `varbind_easy_0033` | second product | 2 / +9.44 | 2 / +9.72 | 36 / +0.29 | 36 / +0.16 |
| `varbind_easy_0002` → `varbind_easy_0033` | answer | 2 / +9.70 | 2 / +8.47 | 36 / +0.18 | 34 / +0.31 |

## Single-cell causal map

Direction: `varbind_easy_0002` → `varbind_easy_0033`. The unpatched donor answer starts at rank 39. Across 500 one-cell interventions, 48 improve its log probability by at least 1 nat and 27 by at least 3 nats.

| Readout | Stage | Effect↔readout-rank ρ | Top-25 overlap | Mean effect in top-25 readout cells |
|---|---|---:|---:|---:|
| J Lens | base value | 0.018 | 0 | -0.003 |
| J Lens | first product | 0.189 | 6 | 1.117 |
| J Lens | bound value | 0.240 | 0 | 0.021 |
| J Lens | second product | 0.394 | 14 | 2.683 |
| J Lens | answer | 0.340 | 9 | 2.144 |
| Logit Lens | base value | -0.046 | 0 | 0.005 |
| Logit Lens | first product | 0.074 | 7 | 1.357 |
| Logit Lens | bound value | 0.138 | 0 | 0.159 |
| Logit Lens | second product | 0.398 | 15 | 2.776 |
| Logit Lens | answer | 0.323 | 9 | 2.249 |

## Interpretation boundary

The causal map transfers a full residual vector from a matched donor; it does not isolate a single feature. A positive donor-answer effect shows that the location carries counterfactual answer-relevant information, but does not by itself prove that the displayed token direction is the sole mediator.
