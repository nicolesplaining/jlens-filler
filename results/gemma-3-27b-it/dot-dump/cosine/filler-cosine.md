# Adjacent-position cosine across the filler span

## gemma-27b-it (50 items, 50 filler positions, 62 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 1.000 [1.000 @ 1] | 0.659 [0.512 @ 38] |
| 15 | 0.995 [0.972 @ 6] | 0.636 [0.449 @ 2] |
| 31 | 0.988 [0.972 @ 16] | 0.238 [-0.037 @ 23] |
| 46 | 0.964 [0.913 @ 6] | 0.231 [-0.106 @ 21] |
| 61 | 0.951 [0.736 @ 6] | 0.361 [0.001 @ 30] |

Flattened over layers (per-layer-normalized): mean 0.983, min 0.955 at boundary 6, first boundary 0.971, last 0.988.
Centered: mean 0.371, min 0.175 at boundary 7, first 0.180, last 0.515.
Change points (z < -2.0) per item: raw 0.78, centered 0.26.
Most frequent change-point boundaries (raw): F6|F7 (28 items), F5|F6 (4 items), F11|F12 (3 items), F12|F13 (2 items), F4|F5 (2 items)
Most frequent change-point boundaries (centered): F6|F7 (3 items), F1|F2 (2 items), F10|F11 (1 items), F9|F10 (1 items), F23|F24 (1 items)

Centered cosine filler -> q_last: peaks at layer 0 (mean over filler 0.142; F1 0.088, F50 0.074).
Centered cosine filler -> cue: peaks at layer 12 (mean over filler 0.258; F1 0.238, F50 0.277).
Centered cosine filler -> gen: peaks at layer 8 (mean over filler 0.201; F1 0.052, F50 0.156).
