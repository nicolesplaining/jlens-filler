# Adjacent-position cosine across the filler span

## base-counting (50 items, 99 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.259 [0.197 @ 80] | 0.037 [0.015 @ 94] |
| 10 | 0.290 [0.216 @ 96] | -0.003 [-0.094 @ 98] |
| 21 | 0.231 [0.181 @ 45] | 0.013 [-0.034 @ 56] |
| 32 | 0.277 [0.171 @ 1] | 0.031 [-0.004 @ 45] |
| 42 | 0.758 [0.646 @ 48] | 0.087 [-0.054 @ 73] |

Flattened over layers (per-layer-normalized): mean 0.294, min 0.241 at boundary 93, first boundary 0.329, last 0.246.
Centered: mean 0.027, min -0.006 at boundary 86, first 0.022, last -0.003.
Change points (z < -2.0) per item: raw 0.20, centered 1.24.
Most frequent change-point boundaries (raw): F92|F93 (4 items), F56|F57 (2 items), F96|F97 (2 items), F60|F61 (1 items), F93|F94 (1 items)
Most frequent change-point boundaries (centered): F38|F39 (8 items), F18|F19 (6 items), F34|F35 (6 items), F19|F20 (4 items), F11|F12 (3 items)

Centered cosine filler -> q_last: peaks at layer 35 (mean over filler 0.083; F1 0.000, F99 0.019).
Centered cosine filler -> cue: peaks at layer 34 (mean over filler 0.109; F1 -0.000, F99 0.006).
Centered cosine filler -> gen: peaks at layer 35 (mean over filler 0.102; F1 0.001, F99 0.008).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.231 / 0.031
- stream 1: 0.294 / 0.022
- stream 2: 0.245 / 0.038
- stream 3: 0.253 / 0.028
