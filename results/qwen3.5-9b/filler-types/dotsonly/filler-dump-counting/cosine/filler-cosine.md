# Adjacent-position cosine across the filler span

## qwen-dotsonly-counting (50 items, 140 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.985 [0.981 @ 77] | 0.323 [0.020 @ 2] |
| 8 | 0.893 [0.836 @ 64] | 0.090 [-0.002 @ 58] |
| 16 | 0.809 [0.693 @ 11] | 0.080 [-0.059 @ 32] |
| 24 | 0.592 [0.185 @ 11] | 0.145 [-0.018 @ 39] |
| 31 | 0.465 [0.082 @ 25] | 0.137 [-0.029 @ 117] |

Flattened over layers (per-layer-normalized): mean 0.752, min 0.591 at boundary 12, first boundary 0.749, last 0.881.
Centered: mean 0.143, min 0.050 at boundary 64, first 0.079, last 0.382.
Change points (z < -2.0) per item: raw 0.04, centered 0.30.
Most frequent change-point boundaries (raw): F12|F13 (1 items), F17|F18 (1 items), F93|F94 (0 items), F92|F93 (0 items), F94|F95 (0 items)
Most frequent change-point boundaries (centered): F84|F85 (3 items), F102|F103 (2 items), F132|F133 (2 items), F30|F31 (2 items), F54|F55 (2 items)

Centered cosine filler -> q_last: peaks at layer 19 (mean over filler 0.172; F1 0.090, F140 0.230).
Centered cosine filler -> cue: peaks at layer 19 (mean over filler 0.240; F1 0.072, F140 0.160).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.218; F1 0.129, F140 0.287).
