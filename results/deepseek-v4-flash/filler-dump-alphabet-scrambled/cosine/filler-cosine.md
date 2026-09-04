# Adjacent-position cosine across the filler span

## chat-alphabet-scrambled (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.455 [0.328 @ 48] | 0.157 [0.088 @ 13] |
| 10 | 0.484 [0.412 @ 48] | 0.093 [-0.008 @ 7] |
| 21 | 0.510 [0.294 @ 19] | 0.007 [-0.438 @ 38] |
| 32 | 0.486 [0.306 @ 19] | 0.031 [-0.399 @ 38] |
| 42 | 0.811 [0.625 @ 49] | 0.087 [-0.405 @ 38] |

Flattened over layers (per-layer-normalized): mean 0.507, min 0.401 at boundary 19, first boundary 0.474, last 0.428.
Centered: mean 0.078, min -0.195 at boundary 38, first 0.109, last 0.066.
Change points (z < -2.0) per item: raw 0.34, centered 1.92.
Most frequent change-point boundaries (raw): F19|F20 (6 items), F28|F29 (4 items), F6|F7 (2 items), F37|F38 (2 items), F18|F19 (2 items)
Most frequent change-point boundaries (centered): F38|F39 (35 items), F37|F38 (19 items), F8|F9 (6 items), F35|F36 (5 items), F22|F23 (4 items)

Centered cosine filler -> q_last: peaks at layer 4 (mean over filler 0.061; F1 0.089, F50 0.048).
Centered cosine filler -> cue: peaks at layer 28 (mean over filler 0.109; F1 0.027, F50 0.030).
Centered cosine filler -> gen: peaks at layer 2 (mean over filler 0.131; F1 0.140, F50 0.095).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.318 / 0.013
- stream 1: 0.431 / -0.001
- stream 2: 0.301 / 0.022
- stream 3: 0.510 / 0.048
