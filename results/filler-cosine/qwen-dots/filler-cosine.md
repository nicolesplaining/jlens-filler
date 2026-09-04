# Adjacent-position cosine across the filler span

## qwen-base (100 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 1.000 [0.982 @ 1] | 0.940 [0.640 @ 1] |
| 8 | 0.945 [0.822 @ 13] | 0.455 [-0.011 @ 1] |
| 16 | 0.808 [0.583 @ 13] | 0.235 [-0.027 @ 4] |
| 24 | 0.674 [0.374 @ 12] | 0.249 [-0.024 @ 24] |
| 31 | 0.666 [0.314 @ 25] | 0.304 [-0.002 @ 24] |

Flattened over layers (per-layer-normalized): mean 0.811, min 0.648 at boundary 13, first boundary 0.747, last 0.915.
Centered: mean 0.407, min 0.118 at boundary 1, first 0.118, last 0.718.
Change points (z < -2.0) per item: raw 0.06, centered 0.15.
Most frequent change-point boundaries (raw): F15|F16 (6 items), F36|F37 (0 items), F33|F34 (0 items), F34|F35 (0 items), F35|F36 (0 items)
Most frequent change-point boundaries (centered): F1|F2 (5 items), F16|F17 (3 items), F31|F32 (3 items), F29|F30 (2 items), F18|F19 (1 items)

Centered cosine filler -> q_last: peaks at layer 31 (mean over filler 0.112; F1 0.127, F50 0.322).
Centered cosine filler -> cue: peaks at layer 2 (mean over filler 0.126; F1 0.231, F50 0.091).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.081; F1 0.125, F50 0.158).

## qwen-dotsonly (100 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 1.000 [0.976 @ 1] | 0.938 [0.608 @ 1] |
| 8 | 0.982 [0.895 @ 3] | 0.659 [-0.079 @ 2] |
| 16 | 0.961 [0.705 @ 3] | 0.681 [-0.030 @ 5] |
| 24 | 0.916 [0.137 @ 3] | 0.761 [-0.023 @ 4] |
| 31 | 0.929 [0.366 @ 2] | 0.822 [0.036 @ 2] |

Flattened over layers (per-layer-normalized): mean 0.954, min 0.582 at boundary 3, first boundary 0.935, last 0.999.
Centered: mean 0.746, min 0.137 at boundary 3, first 0.511, last 0.893.
Change points (z < -2.0) per item: raw 3.95, centered 4.17.
Most frequent change-point boundaries (raw): F2|F3 (100 items), F3|F4 (100 items), F7|F8 (98 items), F9|F10 (95 items), F1|F2 (1 items)
Most frequent change-point boundaries (centered): F2|F3 (100 items), F3|F4 (100 items), F4|F5 (87 items), F7|F8 (78 items), F5|F6 (43 items)

Centered cosine filler -> q_last: peaks at layer 18 (mean over filler 0.227; F1 0.216, F50 0.276).
Centered cosine filler -> cue: peaks at layer 18 (mean over filler 0.260; F1 0.332, F50 0.283).
Centered cosine filler -> gen: peaks at layer 29 (mean over filler 0.342; F1 -0.044, F50 0.500).

## qwen-k0only (100 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 1.000 [0.981 @ 1] | 0.941 [0.640 @ 1] |
| 8 | 0.966 [0.869 @ 13] | 0.483 [-0.062 @ 1] |
| 16 | 0.890 [0.670 @ 2] | 0.353 [-0.179 @ 1] |
| 24 | 0.769 [0.198 @ 2] | 0.440 [-0.071 @ 1] |
| 31 | 0.785 [0.350 @ 2] | 0.510 [0.014 @ 2] |

Flattened over layers (per-layer-normalized): mean 0.872, min 0.585 at boundary 2, first boundary 0.932, last 0.928.
Centered: mean 0.515, min 0.070 at boundary 1, first 0.070, last 0.643.
Change points (z < -2.0) per item: raw 2.01, centered 0.69.
Most frequent change-point boundaries (raw): F2|F3 (88 items), F5|F6 (52 items), F13|F14 (36 items), F14|F15 (10 items), F8|F9 (7 items)
Most frequent change-point boundaries (centered): F1|F2 (42 items), F27|F28 (18 items), F19|F20 (6 items), F4|F5 (3 items), F38|F39 (0 items)

Centered cosine filler -> q_last: peaks at layer 19 (mean over filler 0.206; F1 -0.001, F50 0.302).
Centered cosine filler -> cue: peaks at layer 19 (mean over filler 0.244; F1 0.005, F50 0.255).
Centered cosine filler -> gen: peaks at layer 14 (mean over filler 0.267; F1 -0.050, F50 0.318).
