# Adjacent-position cosine across the filler span

## base-alphabet-scrambled (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.468 [0.351 @ 48] | 0.168 [0.095 @ 18] |
| 10 | 0.498 [0.436 @ 48] | 0.084 [-0.015 @ 15] |
| 21 | 0.454 [0.330 @ 7] | -0.014 [-0.400 @ 33] |
| 32 | 0.426 [0.288 @ 20] | 0.026 [-0.323 @ 33] |
| 42 | 0.896 [0.818 @ 49] | 0.049 [-0.317 @ 33] |

Flattened over layers (per-layer-normalized): mean 0.480, min 0.403 at boundary 6, first boundary 0.466, last 0.417.
Centered: mean 0.067, min -0.151 at boundary 33, first 0.115, last 0.069.
Change points (z < -2.0) per item: raw 0.00, centered 1.82.
Most frequent change-point boundaries (raw): F35|F36 (0 items), F32|F33 (0 items), F33|F34 (0 items), F34|F35 (0 items), F31|F32 (0 items)
Most frequent change-point boundaries (centered): F33|F34 (32 items), F32|F33 (14 items), F38|F39 (9 items), F37|F38 (8 items), F31|F32 (6 items)

Centered cosine filler -> q_last: peaks at layer 35 (mean over filler 0.101; F1 0.009, F50 0.014).
Centered cosine filler -> cue: peaks at layer 35 (mean over filler 0.108; F1 0.002, F50 0.007).
Centered cosine filler -> gen: peaks at layer 2 (mean over filler 0.138; F1 0.132, F50 0.109).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.274 / 0.016
- stream 1: 0.377 / 0.011
- stream 2: 0.293 / 0.023
- stream 3: 0.443 / 0.026
