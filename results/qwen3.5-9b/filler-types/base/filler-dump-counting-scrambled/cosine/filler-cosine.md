# Adjacent-position cosine across the filler span

## qwen-base-counting-scrambled (50 items, 140 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.986 [0.981 @ 97] | 0.298 [-0.062 @ 7] |
| 8 | 0.868 [0.789 @ 128] | 0.087 [-0.029 @ 20] |
| 16 | 0.718 [0.631 @ 75] | 0.035 [-0.030 @ 30] |
| 24 | 0.522 [0.284 @ 18] | 0.047 [-0.037 @ 135] |
| 31 | 0.428 [0.188 @ 82] | 0.071 [-0.054 @ 47] |

Flattened over layers (per-layer-normalized): mean 0.697, min 0.608 at boundary 18, first boundary 0.717, last 0.723.
Centered: mean 0.093, min 0.038 at boundary 34, first 0.104, last 0.123.
Change points (z < -2.0) per item: raw 0.02, centered 0.42.
Most frequent change-point boundaries (raw): F10|F11 (1 items), F94|F95 (0 items), F93|F94 (0 items), F95|F96 (0 items), F96|F97 (0 items)
Most frequent change-point boundaries (centered): F109|F110 (4 items), F19|F20 (4 items), F27|F28 (4 items), F50|F51 (2 items), F59|F60 (1 items)

Centered cosine filler -> q_last: peaks at layer 0 (mean over filler 0.097; F1 0.106, F140 0.106).
Centered cosine filler -> cue: peaks at layer 0 (mean over filler 0.106; F1 0.035, F140 0.131).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.075; F1 0.016, F140 0.266).
