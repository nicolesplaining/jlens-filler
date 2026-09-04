# Adjacent-position cosine across the filler span

## qwen-dotsonly-alphabet-scrambled (50 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.979 [0.971 @ 41] | 0.304 [0.104 @ 18] |
| 8 | 0.932 [0.893 @ 36] | 0.111 [-0.075 @ 36] |
| 16 | 0.835 [0.691 @ 1] | 0.038 [-0.057 @ 25] |
| 24 | 0.680 [0.216 @ 39] | 0.111 [-0.065 @ 25] |
| 31 | 0.608 [0.284 @ 40] | 0.213 [-0.018 @ 25] |

Flattened over layers (per-layer-normalized): mean 0.801, min 0.593 at boundary 39, first boundary 0.606, last 0.869.
Centered: mean 0.148, min 0.047 at boundary 25, first 0.136, last 0.261.
Change points (z < -2.0) per item: raw 1.02, centered 0.70.
Most frequent change-point boundaries (raw): F39|F40 (22 items), F1|F2 (17 items), F5|F6 (3 items), F8|F9 (3 items), F40|F41 (3 items)
Most frequent change-point boundaries (centered): F25|F26 (8 items), F34|F35 (4 items), F41|F42 (4 items), F24|F25 (4 items), F14|F15 (3 items)

Centered cosine filler -> q_last: peaks at layer 19 (mean over filler 0.103; F1 0.067, F50 0.308).
Centered cosine filler -> cue: peaks at layer 19 (mean over filler 0.154; F1 0.052, F50 0.219).
Centered cosine filler -> gen: peaks at layer 19 (mean over filler 0.121; F1 0.030, F50 0.206).
