# Adjacent-position cosine across the filler span

## base-alphabet (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.479 [0.410 @ 26] | 0.177 [0.090 @ 23] |
| 10 | 0.521 [0.384 @ 26] | 0.069 [-0.004 @ 26] |
| 21 | 0.491 [0.272 @ 26] | 0.013 [-0.123 @ 6] |
| 32 | 0.458 [0.248 @ 26] | 0.038 [-0.084 @ 9] |
| 42 | 0.869 [0.812 @ 40] | 0.100 [-0.100 @ 26] |

Flattened over layers (per-layer-normalized): mean 0.499, min 0.339 at boundary 26, first boundary 0.493, last 0.442.
Centered: mean 0.071, min -0.014 at boundary 6, first 0.103, last 0.046.
Change points (z < -2.0) per item: raw 1.00, centered 1.12.
Most frequent change-point boundaries (raw): F26|F27 (45 items), F19|F20 (2 items), F13|F14 (2 items), F24|F25 (1 items), F34|F35 (0 items)
Most frequent change-point boundaries (centered): F6|F7 (19 items), F9|F10 (5 items), F36|F37 (3 items), F22|F23 (2 items), F42|F43 (2 items)

Centered cosine filler -> q_last: peaks at layer 34 (mean over filler 0.100; F1 0.317, F50 0.026).
Centered cosine filler -> cue: peaks at layer 34 (mean over filler 0.116; F1 0.341, F50 0.009).
Centered cosine filler -> gen: peaks at layer 2 (mean over filler 0.113; F1 0.135, F50 0.077).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.276 / 0.026
- stream 1: 0.368 / 0.018
- stream 2: 0.253 / 0.030
- stream 3: 0.489 / 0.042
