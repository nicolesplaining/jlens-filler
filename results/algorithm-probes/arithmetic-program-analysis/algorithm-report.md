# Arithmetic-program J-Lens algorithm probe

These are **J-Lens token readouts**, not formal sparse J-space coordinates.

A broadcast onset is the first layer where a target reaches rank ≤10 at at least 2 filler positions. This is stricter than a single-cell hit.

## `arithmetic_serial_013` (serial_chain)

Filler answer correct: `True`; no-filler correct: `True`; expected answer: `78`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `x1` | 8 | 3 | L27/F18 | L27 | 0 |
| `x2` | 24 | 1 | L35/F18 | L31 | 2 |
| `x3` | 20 | 2 | L38/F18 | — | 0 |
| `x4` | 27 | 1 | L36/F7 | L31 | 3 |
| `x5` | 81 | 182 | L31/F6 | — | 0 |
| `x6` | 76 | 20 | L31/F7 | — | 0 |
| `y` | 78 | 9 | L31/F7 | — | 0 |

Actual/control cell counts: rank-1 `5` / `1`; rank ≤10 `53` / `8`.
Mean per-target cell fractions (actual/control): rank-1 `0.0007` / `0.0001`; rank ≤10 `0.0072` / `0.0011`.

Algorithm signature: `{"detected_steps": 3, "spearman_step_vs_onset": 0.8660254037844387, "step_broadcast_onsets": {"x1": 27, "x2": 31, "x3": null, "x4": 31, "x5": null, "x6": null, "y": null}}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `x1` | 8 | 1 | L28/F18 | — | 1 |
| `x2` | 24 | 2 | L32/F8 | L31 | 0 |
| `x3` | 20 | 7 | L38/F18 | — | 0 |
| `x4` | 27 | 1 | L31/F9 | L28 | 3 |
| `x5` | 81 | 96 | L33/F7 | — | 0 |
| `x6` | 76 | 28 | L31/F7 | — | 0 |
| `y` | 78 | 16 | L33/F7 | — | 0 |

Actual/control cell counts: rank-1 `4` / `0`; rank ≤10 `44` / `17`.
Mean per-target cell fractions (actual/control): rank-1 `0.0005` / `0.0000`; rank ≤10 `0.0060` / `0.0023`.

Algorithm signature: `{"detected_steps": 2, "spearman_step_vs_onset": null, "step_broadcast_onsets": {"x1": null, "x2": 31, "x3": null, "x4": 28, "x5": null, "x6": null, "y": null}}`

## `arithmetic_serial_014` (serial_chain)

Filler answer correct: `True`; no-filler correct: `False`; expected answer: `145`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `x1` | 16 | 1 | L35/F14 | L35 | 2 |
| `x2` | 48 | 1 | L30/F7 | L30 | 6 |
| `x3` | 40 | 18 | L31/F7 | — | 0 |
| `x4` | 47 | 5 | L34/F8 | L34 | 0 |
| `x5` | 141 | 10 | L30/F4 | — | 0 |
| `x6` | 136 | 1 | L32/F4 | L39 | 7 |
| `y` | 145 | 1 | L39/F8 | L38 | 3 |

Actual/control cell counts: rank-1 `18` / `8`; rank ≤10 `57` / `29`.
Mean per-target cell fractions (actual/control): rank-1 `0.0024` / `0.0011`; rank ≤10 `0.0078` / `0.0039`.

Algorithm signature: `{"detected_steps": 5, "spearman_step_vs_onset": 0.6, "step_broadcast_onsets": {"x1": 35, "x2": 30, "x3": null, "x4": 34, "x5": null, "x6": 39, "y": 38}}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `x1` | 16 | 1 | L35/F14 | L29 | 1 |
| `x2` | 48 | 1 | L29/F7 | L28 | 6 |
| `x3` | 40 | 19 | L29/F7 | — | 0 |
| `x4` | 47 | 2 | L30/F18 | — | 0 |
| `x5` | 141 | 4 | L30/F4 | — | 0 |
| `x6` | 136 | 1 | L33/F4 | L39 | 5 |
| `y` | 145 | 1 | L39/F8 | L39 | 1 |

Actual/control cell counts: rank-1 `13` / `6`; rank ≤10 `69` / `28`.
Mean per-target cell fractions (actual/control): rank-1 `0.0018` / `0.0008`; rank ≤10 `0.0094` / `0.0038`.

Algorithm signature: `{"detected_steps": 4, "spearman_step_vs_onset": 0.7378647873726218, "step_broadcast_onsets": {"x1": 29, "x2": 28, "x3": null, "x4": null, "x5": null, "x6": 39, "y": 39}}`

## `arithmetic_tree_000` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `False`; expected answer: `148`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 17 | 71 | L35/F15 | — | 0 |
| `p2` | 4 | 26 | L21/F4 | — | 0 |
| `p3` | 16 | 75 | L35/F15 | — | 0 |
| `p4` | 5 | 33 | L35/F18 | — | 0 |
| `m1` | 68 | 1 | L35/F1 | — | 1 |
| `m2` | 80 | 2 | L35/F4 | — | 0 |
| `y` | 148 | 14 | L39/F4 | — | 0 |

Actual/control cell counts: rank-1 `1` / `1`; rank ≤10 `3` / `7`.
Mean per-target cell fractions (actual/control): rank-1 `0.0001` / `0.0002`; rank ≤10 `0.0004` / `0.0013`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": null, "merges": null}, "stages_depth_ordered": false}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 17 | 52 | L35/F15 | — | 0 |
| `p2` | 4 | 40 | L29/F16 | — | 0 |
| `p3` | 16 | 50 | L35/F15 | — | 0 |
| `p4` | 5 | 1 | L29/F16 | L29 | 2 |
| `m1` | 68 | 11 | L35/F1 | — | 0 |
| `m2` | 80 | 8 | L34/F4 | — | 0 |
| `y` | 148 | 67 | L39/F22 | — | 0 |

Actual/control cell counts: rank-1 `2` / `2`; rank ≤10 `14` / `21`.
Mean per-target cell fractions (actual/control): rank-1 `0.0003` / `0.0004`; rank ≤10 `0.0019` / `0.0040`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 29.0, "merges": null}, "stages_depth_ordered": false}`

## `arithmetic_tree_014` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `True`; expected answer: `116`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 20 | 2 | L40/F15 | — | 0 |
| `p2` | 4 | 23 | L21/F4 | — | 0 |
| `p3` | 18 | 1 | L38/F16 | L31 | 1 |
| `p4` | 2 | 81 | L35/F18 | — | 0 |
| `m1` | 80 | 47 | L35/F3 | — | 0 |
| `m2` | 36 | 1 | L31/F4 | L36 | 1 |
| `y` | 116 | 2 | L37/F4 | — | 0 |

Actual/control cell counts: rank-1 `2` / `0`; rank ≤10 `30` / `4`.
Mean per-target cell fractions (actual/control): rank-1 `0.0003` / `0.0000`; rank ≤10 `0.0041` / `0.0006`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 31.0, "merges": 36.0}, "stages_depth_ordered": false}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 20 | 2 | L41/F15 | — | 0 |
| `p2` | 4 | 9 | L31/F11 | — | 0 |
| `p3` | 18 | 1 | L29/F9 | L29 | 9 |
| `p4` | 2 | 4 | L30/F9 | — | 0 |
| `m1` | 80 | 99 | L35/F25 | — | 0 |
| `m2` | 36 | 1 | L26/F7 | L31 | 4 |
| `y` | 116 | 9 | L39/F4 | — | 0 |

Actual/control cell counts: rank-1 `13` / `0`; rank ≤10 `46` / `7`.
Mean per-target cell fractions (actual/control): rank-1 `0.0018` / `0.0000`; rank ≤10 `0.0063` / `0.0011`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": null, "branches": 29.0, "merges": 31.0}, "stages_depth_ordered": false}`

## `arithmetic_tree_017` (balanced_tree)

Filler answer correct: `True`; no-filler correct: `False`; expected answer: `131`.

### J-Lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 14 | 506 | L35/F6 | — | 0 |
| `p2` | 4 | 23 | L21/F4 | — | 0 |
| `p3` | 15 | 1 | L31/F11 | L31 | 3 |
| `p4` | 5 | 1 | L35/F15 | — | 1 |
| `m1` | 56 | 16 | L30/F7 | — | 0 |
| `m2` | 75 | 1 | L31/F4 | L31 | 8 |
| `y` | 131 | 1 | L38/F11 | L38 | 5 |

Actual/control cell counts: rank-1 `17` / `1`; rank ≤10 `48` / `5`.
Mean per-target cell fractions (actual/control): rank-1 `0.0023` / `0.0002`; rank ≤10 `0.0065` / `0.0010`.

Algorithm signature: `{"branch_onset_spread": null, "stage_broadcast_onsets": {"answer": 38.0, "branches": 31.0, "merges": 31.0}, "stages_depth_ordered": true}`

### Logit lens

| Stage | Value | Best rank | Best cell | Broadcast onset | Rank-1 cells |
|---|---:|---:|---:|---:|---:|
| `p1` | 14 | 9 | L29/F11 | — | 0 |
| `p2` | 4 | 16 | L29/F15 | — | 0 |
| `p3` | 15 | 1 | L29/F11 | L29 | 8 |
| `p4` | 5 | 1 | L28/F15 | L31 | 5 |
| `m1` | 56 | 3 | L30/F7 | — | 0 |
| `m2` | 75 | 1 | L31/F4 | L30 | 16 |
| `y` | 131 | 1 | L39/F4 | L38 | 1 |

Actual/control cell counts: rank-1 `30` / `0`; rank ≤10 `100` / `6`.
Mean per-target cell fractions (actual/control): rank-1 `0.0041` / `0.0000`; rank ≤10 `0.0136` / `0.0011`.

Algorithm signature: `{"branch_onset_spread": 2, "stage_broadcast_onsets": {"answer": 38.0, "branches": 30.0, "merges": 30.0}, "stages_depth_ordered": true}`

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
