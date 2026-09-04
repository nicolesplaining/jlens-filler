# Adjacent-position cosine across the filler span

## chat-dots (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.974 [0.410 @ 49] | 0.602 [0.147 @ 49] |
| 10 | 0.933 [0.445 @ 49] | 0.132 [-0.063 @ 49] |
| 21 | 0.783 [0.304 @ 49] | 0.074 [-0.032 @ 1] |
| 32 | 0.699 [0.237 @ 49] | 0.117 [-0.059 @ 30] |
| 42 | 0.902 [0.591 @ 49] | 0.284 [0.065 @ 1] |

Flattened over layers (per-layer-normalized): mean 0.819, min 0.360 at boundary 49, first boundary 0.549, last 0.360.
Centered: mean 0.192, min 0.048 at boundary 49, first 0.077, last 0.048.
Change points (z < -2.0) per item: raw 2.88, centered 0.88.
Most frequent change-point boundaries (raw): F49|F50 (50 items), F2|F3 (49 items), F1|F2 (43 items), F5|F6 (2 items), F33|F34 (0 items)
Most frequent change-point boundaries (centered): F30|F31 (5 items), F34|F35 (5 items), F35|F36 (3 items), F37|F38 (3 items), F28|F29 (3 items)

Centered cosine filler -> q_last: peaks at layer 4 (mean over filler 0.063; F1 0.114, F50 0.102).
Centered cosine filler -> cue: peaks at layer 40 (mean over filler 0.178; F1 0.283, F50 0.458).
Centered cosine filler -> gen: peaks at layer 39 (mean over filler 0.180; F1 0.353, F50 0.487).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.443 / 0.140
- stream 1: 0.583 / 0.091
- stream 2: 0.429 / 0.115
- stream 3: 0.787 / 0.117

## base-dots (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.975 [0.412 @ 49] | 0.595 [0.170 @ 49] |
| 10 | 0.940 [0.433 @ 49] | 0.169 [-0.045 @ 49] |
| 21 | 0.754 [0.290 @ 49] | 0.061 [-0.045 @ 25] |
| 32 | 0.605 [0.278 @ 49] | 0.102 [-0.055 @ 25] |
| 42 | 0.934 [0.765 @ 49] | 0.182 [-0.043 @ 7] |

Flattened over layers (per-layer-normalized): mean 0.776, min 0.373 at boundary 49, first boundary 0.535, last 0.373.
Centered: mean 0.187, min 0.043 at boundary 49, first 0.118, last 0.043.
Change points (z < -2.0) per item: raw 2.70, centered 0.48.
Most frequent change-point boundaries (raw): F49|F50 (50 items), F2|F3 (49 items), F1|F2 (36 items), F34|F35 (0 items), F33|F34 (0 items)
Most frequent change-point boundaries (centered): F27|F28 (4 items), F26|F27 (3 items), F7|F8 (3 items), F49|F50 (2 items), F12|F13 (2 items)

Centered cosine filler -> q_last: peaks at layer 35 (mean over filler 0.157; F1 0.353, F50 0.135).
Centered cosine filler -> cue: peaks at layer 35 (mean over filler 0.206; F1 0.427, F50 0.127).
Centered cosine filler -> gen: peaks at layer 35 (mean over filler 0.166; F1 0.324, F50 0.135).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.380 / 0.102
- stream 1: 0.478 / 0.089
- stream 2: 0.366 / 0.122
- stream 3: 0.697 / 0.100
