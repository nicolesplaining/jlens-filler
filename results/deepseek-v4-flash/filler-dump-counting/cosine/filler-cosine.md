# Adjacent-position cosine across the filler span

## chat-counting (50 items, 99 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.264 [0.206 @ 80] | 0.041 [0.019 @ 93] |
| 10 | 0.287 [0.228 @ 80] | -0.003 [-0.102 @ 10] |
| 21 | 0.240 [0.170 @ 94] | 0.019 [-0.025 @ 6] |
| 32 | 0.306 [0.181 @ 98] | 0.038 [-0.022 @ 6] |
| 42 | 0.557 [0.357 @ 32] | 0.091 [0.004 @ 56] |

Flattened over layers (per-layer-normalized): mean 0.306, min 0.234 at boundary 93, first boundary 0.360, last 0.241.
Centered: mean 0.032, min -0.000 at boundary 6, first 0.020, last 0.005.
Change points (z < -2.0) per item: raw 0.90, centered 1.18.
Most frequent change-point boundaries (raw): F93|F94 (11 items), F94|F95 (8 items), F92|F93 (6 items), F56|F57 (3 items), F36|F37 (2 items)
Most frequent change-point boundaries (centered): F22|F23 (3 items), F50|F51 (3 items), F11|F12 (3 items), F15|F16 (3 items), F31|F32 (3 items)

Centered cosine filler -> q_last: peaks at layer 3 (mean over filler 0.034; F1 0.074, F99 0.018).
Centered cosine filler -> cue: peaks at layer 35 (mean over filler 0.118; F1 0.008, F99 0.012).
Centered cosine filler -> gen: peaks at layer 35 (mean over filler 0.111; F1 0.006, F99 0.018).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.279 / 0.050
- stream 1: 0.372 / 0.031
- stream 2: 0.275 / 0.042
- stream 3: 0.275 / 0.029
