# Adjacent-position cosine across the filler span

## qwen-base-alphabet (50 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.980 [0.974 @ 1] | 0.319 [0.078 @ 17] |
| 8 | 0.881 [0.791 @ 31] | 0.045 [-0.043 @ 25] |
| 16 | 0.715 [0.577 @ 1] | -0.001 [-0.143 @ 25] |
| 24 | 0.509 [0.280 @ 1] | 0.026 [-0.064 @ 7] |
| 31 | 0.479 [0.306 @ 15] | 0.082 [0.004 @ 7] |

Flattened over layers (per-layer-normalized): mean 0.708, min 0.593 at boundary 1, first boundary 0.593, last 0.773.
Centered: mean 0.094, min 0.034 at boundary 25, first 0.115, last 0.106.
Change points (z < -2.0) per item: raw 0.44, centered 1.00.
Most frequent change-point boundaries (raw): F1|F2 (9 items), F36|F37 (5 items), F40|F41 (2 items), F35|F36 (1 items), F37|F38 (1 items)
Most frequent change-point boundaries (centered): F25|F26 (7 items), F47|F48 (6 items), F7|F8 (6 items), F42|F43 (4 items), F48|F49 (3 items)

Centered cosine filler -> q_last: peaks at layer 31 (mean over filler 0.071; F1 0.208, F50 0.153).
Centered cosine filler -> cue: peaks at layer 5 (mean over filler 0.081; F1 0.067, F50 0.032).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.052; F1 0.158, F50 0.131).
