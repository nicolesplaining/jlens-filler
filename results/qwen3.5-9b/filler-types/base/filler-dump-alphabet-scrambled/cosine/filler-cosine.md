# Adjacent-position cosine across the filler span

## qwen-base-alphabet-scrambled (50 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.979 [0.971 @ 41] | 0.299 [0.115 @ 18] |
| 8 | 0.879 [0.821 @ 36] | 0.059 [-0.102 @ 41] |
| 16 | 0.711 [0.598 @ 10] | 0.004 [-0.043 @ 22] |
| 24 | 0.515 [0.339 @ 10] | 0.023 [-0.059 @ 37] |
| 31 | 0.477 [0.277 @ 11] | 0.070 [-0.018 @ 18] |

Flattened over layers (per-layer-normalized): mean 0.702, min 0.618 at boundary 10, first boundary 0.669, last 0.849.
Centered: mean 0.089, min 0.040 at boundary 18, first 0.081, last 0.283.
Change points (z < -2.0) per item: raw 0.14, centered 1.04.
Most frequent change-point boundaries (raw): F25|F26 (2 items), F10|F11 (1 items), F23|F24 (1 items), F31|F32 (1 items), F11|F12 (1 items)
Most frequent change-point boundaries (centered): F18|F19 (6 items), F40|F41 (4 items), F32|F33 (4 items), F15|F16 (4 items), F22|F23 (4 items)

Centered cosine filler -> q_last: peaks at layer 18 (mean over filler 0.061; F1 0.130, F50 0.267).
Centered cosine filler -> cue: peaks at layer 4 (mean over filler 0.069; F1 0.056, F50 0.109).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.050; F1 0.109, F50 0.241).
