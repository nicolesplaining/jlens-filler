# Adjacent-position cosine across the filler span

## base-counting-scrambled (50 items, 99 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.249 [0.183 @ 44] | 0.038 [0.019 @ 94] |
| 10 | 0.252 [0.190 @ 44] | -0.014 [-0.098 @ 96] |
| 21 | 0.160 [0.117 @ 8] | -0.003 [-0.032 @ 72] |
| 32 | 0.201 [0.124 @ 1] | 0.001 [-0.012 @ 46] |
| 42 | 0.795 [0.708 @ 98] | 0.057 [-0.043 @ 43] |

Flattened over layers (per-layer-normalized): mean 0.242, min 0.193 at boundary 4, first boundary 0.209, last 0.232.
Centered: mean 0.008, min -0.011 at boundary 96, first 0.031, last 0.004.
Change points (z < -2.0) per item: raw 0.68, centered 2.72.
Most frequent change-point boundaries (raw): F8|F9 (6 items), F52|F53 (5 items), F36|F37 (5 items), F9|F10 (4 items), F4|F5 (4 items)
Most frequent change-point boundaries (centered): F95|F96 (10 items), F96|F97 (9 items), F91|F92 (9 items), F97|F98 (8 items), F11|F12 (7 items)

Centered cosine filler -> q_last: peaks at layer 35 (mean over filler 0.093; F1 -0.000, F99 0.022).
Centered cosine filler -> cue: peaks at layer 35 (mean over filler 0.112; F1 -0.004, F99 0.007).
Centered cosine filler -> gen: peaks at layer 40 (mean over filler 0.127; F1 0.043, F99 0.176).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.154 / 0.007
- stream 1: 0.217 / 0.005
- stream 2: 0.190 / -0.008
- stream 3: 0.163 / 0.002
