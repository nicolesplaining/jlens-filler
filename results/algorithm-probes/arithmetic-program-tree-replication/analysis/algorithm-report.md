# Arithmetic-program J-Lens algorithm probe

These are **J-Lens token readouts**, not formal sparse J-space coordinates.

A broadcast onset is the first layer where a target reaches rank ≤10 at at least 2 filler positions. This is stricter than a single-cell hit.

## `arithmetic_tree_002` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `True`; expected answer: `140`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 22 | 1 | L30/F15 | — | 6 |
| `p2` | 5 | 11 | L35/F16 | — | 0 |
| `p3` | 15 | 5 | L31/F9 | — | 0 |
| `p4` | 2 | 194 | L21/F11 | — | 0 |
| `m1` | 110 | 3 | L37/F7 | — | 0 |
| `m2` | 30 | 1 | L32/F9 | — | 6 |
| `y` | 140 | 214 | L37/F4 | — | 0 |

Actual/control cell counts: rank-1 `12` / `0`; rank ≤10 `25` / `0`.
Mean per-target cell fractions (actual/control): rank-1 `0.0016` / `0.0000`; rank ≤10 `0.0034` / `0.0000`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": null, "merges": null}, "stages_depth_ordered": false}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 22 | 1 | L27/F15 | L28 | 11 |
| `p2` | 5 | 8 | L30/F16 | — | 0 |
| `p3` | 15 | 1 | L31/F9 | — | 1 |
| `p4` | 2 | 11 | L31/F11 | — | 0 |
| `m1` | 110 | 1 | L37/F7 | — | 1 |
| `m2` | 30 | 1 | L32/F9 | L31 | 6 |
| `y` | 140 | 119 | L30/F4 | — | 0 |

Actual/control cell counts: rank-1 `19` / `3`; rank ≤10 `49` / `24`.
Mean per-target cell fractions (actual/control): rank-1 `0.0026` / `0.0004`; rank ≤10 `0.0067` / `0.0033`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 28.0, "merges": 31.0}, "stages_depth_ordered": false}`

## `arithmetic_tree_004` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `True`; expected answer: `165`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 21 | 1 | L37/F15 | — | 1 |
| `p2` | 5 | 114 | L20/F22 | — | 0 |
| `p3` | 20 | 107 | L20/F22 | — | 0 |
| `p4` | 3 | 9 | L30/F16 | — | 0 |
| `m1` | 105 | 6 | L36/F25 | — | 0 |
| `m2` | 60 | 1 | L35/F9 | — | 2 |
| `y` | 165 | 35 | L37/F4 | — | 0 |

Actual/control cell counts: rank-1 `3` / `1`; rank ≤10 `12` / `7`.
Mean per-target cell fractions (actual/control): rank-1 `0.0004` / `0.0002`; rank ≤10 `0.0016` / `0.0011`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": null, "merges": null}, "stages_depth_ordered": false}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 21 | 2 | L39/F15 | — | 0 |
| `p2` | 5 | 48 | L31/F9 | — | 0 |
| `p3` | 20 | 2 | L32/F9 | — | 0 |
| `p4` | 3 | 1 | L29/F16 | L29 | 5 |
| `m1` | 105 | 7 | L32/F25 | — | 0 |
| `m2` | 60 | 1 | L34/F9 | — | 5 |
| `y` | 165 | 32 | L39/F7 | — | 0 |

Actual/control cell counts: rank-1 `10` / `17`; rank ≤10 `28` / `55`.
Mean per-target cell fractions (actual/control): rank-1 `0.0014` / `0.0027`; rank ≤10 `0.0038` / `0.0087`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 29.0, "merges": null}, "stages_depth_ordered": false}`

## `arithmetic_tree_011` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `True`; expected answer: `100`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 12 | 3 | L40/F15 | — | 0 |
| `p2` | 3 | 105 | L20/F22 | — | 0 |
| `p3` | 16 | 7 | L35/F22 | — | 0 |
| `p4` | 4 | 32 | L20/F24 | — | 0 |
| `m1` | 36 | 2 | L36/F22 | L35 | 0 |
| `m2` | 64 | 11 | L35/F9 | — | 0 |
| `y` | 100 | 43 | L31/F7 | — | 0 |

Actual/control cell counts: rank-1 `0` / `0`; rank ≤10 `8` / `3`.
Mean per-target cell fractions (actual/control): rank-1 `0.0000` / `0.0000`; rank ≤10 `0.0011` / `0.0004`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": null, "merges": 35.0}, "stages_depth_ordered": false}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 12 | 5 | L31/F22 | — | 0 |
| `p2` | 3 | 64 | L36/F8 | — | 0 |
| `p3` | 16 | 3 | L33/F22 | L32 | 0 |
| `p4` | 4 | 4 | L29/F16 | — | 0 |
| `m1` | 36 | 1 | L27/F7 | L30 | 3 |
| `m2` | 64 | 2 | L25/F7 | L30 | 0 |
| `y` | 100 | 1 | L24/F7 | — | 1 |

Actual/control cell counts: rank-1 `4` / `0`; rank ≤10 `60` / `7`.
Mean per-target cell fractions (actual/control): rank-1 `0.0005` / `0.0000`; rank ≤10 `0.0082` / `0.0010`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 32.0, "merges": 30.0}, "stages_depth_ordered": false}`

## Interpretation boundary

Stage ordering is evidence about linearly transported token directions, not a literal trace of internal thoughts. Values copied from another example are tracked as controls; final claims should require actual targets to exceed those controls.
