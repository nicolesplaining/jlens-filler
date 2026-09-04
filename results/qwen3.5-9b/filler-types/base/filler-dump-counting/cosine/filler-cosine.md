# Adjacent-position cosine across the filler span

## qwen-base-counting (50 items, 140 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.986 [0.981 @ 77] | 0.319 [0.035 @ 2] |
| 8 | 0.851 [0.730 @ 49] | 0.050 [-0.042 @ 69] |
| 16 | 0.719 [0.606 @ 28] | 0.037 [-0.035 @ 2] |
| 24 | 0.500 [0.284 @ 28] | 0.055 [-0.048 @ 5] |
| 31 | 0.407 [0.173 @ 91] | 0.083 [-0.027 @ 60] |

Flattened over layers (per-layer-normalized): mean 0.690, min 0.585 at boundary 28, first boundary 0.679, last 0.853.
Centered: mean 0.090, min 0.032 at boundary 5, first 0.071, last 0.334.
Change points (z < -2.0) per item: raw 0.00, centered 0.16.
Most frequent change-point boundaries (raw): F94|F95 (0 items), F92|F93 (0 items), F93|F94 (0 items), F91|F92 (0 items), F95|F96 (0 items)
Most frequent change-point boundaries (centered): F102|F103 (2 items), F5|F6 (2 items), F33|F34 (1 items), F30|F31 (1 items), F60|F61 (1 items)

Centered cosine filler -> q_last: peaks at layer 0 (mean over filler 0.099; F1 0.063, F140 0.069).
Centered cosine filler -> cue: peaks at layer 14 (mean over filler 0.094; F1 0.112, F140 0.178).
Centered cosine filler -> gen: peaks at layer 10 (mean over filler 0.087; F1 0.097, F140 0.171).
