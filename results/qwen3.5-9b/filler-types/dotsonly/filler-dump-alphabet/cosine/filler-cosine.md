# Adjacent-position cosine across the filler span

## qwen-dotsonly-alphabet (50 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.980 [0.974 @ 1] | 0.322 [0.099 @ 17] |
| 8 | 0.932 [0.843 @ 26] | 0.115 [-0.034 @ 35] |
| 16 | 0.841 [0.716 @ 26] | 0.063 [-0.082 @ 40] |
| 24 | 0.648 [0.155 @ 1] | 0.110 [-0.009 @ 44] |
| 31 | 0.532 [0.270 @ 9] | 0.191 [0.022 @ 13] |

Flattened over layers (per-layer-normalized): mean 0.793, min 0.595 at boundary 1, first boundary 0.595, last 0.873.
Centered: mean 0.159, min 0.069 at boundary 26, first 0.133, last 0.229.
Change points (z < -2.0) per item: raw 0.48, centered 0.42.
Most frequent change-point boundaries (raw): F1|F2 (16 items), F26|F27 (6 items), F6|F7 (1 items), F9|F10 (1 items), F33|F34 (0 items)
Most frequent change-point boundaries (centered): F40|F41 (8 items), F44|F45 (3 items), F42|F43 (3 items), F29|F30 (2 items), F4|F5 (2 items)

Centered cosine filler -> q_last: peaks at layer 19 (mean over filler 0.127; F1 0.044, F50 0.187).
Centered cosine filler -> cue: peaks at layer 19 (mean over filler 0.189; F1 0.052, F50 0.118).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.150; F1 0.075, F50 0.226).
