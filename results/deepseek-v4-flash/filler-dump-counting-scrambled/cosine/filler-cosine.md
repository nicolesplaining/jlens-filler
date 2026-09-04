# Adjacent-position cosine across the filler span

## chat-counting-scrambled (50 items, 99 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.253 [0.187 @ 66] | 0.043 [0.025 @ 4] |
| 10 | 0.256 [0.186 @ 4] | -0.012 [-0.089 @ 36] |
| 21 | 0.164 [0.114 @ 80] | -0.000 [-0.035 @ 84] |
| 32 | 0.226 [0.155 @ 98] | 0.008 [-0.010 @ 44] |
| 42 | 0.672 [0.562 @ 96] | 0.059 [-0.036 @ 46] |

Flattened over layers (per-layer-normalized): mean 0.257, min 0.214 at boundary 44, first boundary 0.250, last 0.232.
Centered: mean 0.013, min -0.010 at boundary 84, first 0.029, last 0.007.
Change points (z < -2.0) per item: raw 1.28, centered 2.34.
Most frequent change-point boundaries (raw): F42|F43 (8 items), F44|F45 (8 items), F36|F37 (8 items), F52|F53 (6 items), F9|F10 (5 items)
Most frequent change-point boundaries (centered): F95|F96 (11 items), F91|F92 (9 items), F46|F47 (8 items), F47|F48 (7 items), F87|F88 (6 items)

Centered cosine filler -> q_last: peaks at layer 42 (mean over filler 0.033; F1 0.060, F99 0.115).
Centered cosine filler -> cue: peaks at layer 40 (mean over filler 0.102; F1 0.028, F99 0.093).
Centered cosine filler -> gen: peaks at layer 39 (mean over filler 0.092; F1 0.026, F99 0.070).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.199 / 0.018
- stream 1: 0.252 / 0.008
- stream 2: 0.216 / 0.003
- stream 3: 0.182 / 0.008
