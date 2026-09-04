# Adjacent-position cosine across the filler span

## chat-alphabet (50 items, 50 filler positions, 43 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.463 [0.392 @ 26] | 0.164 [0.066 @ 23] |
| 10 | 0.514 [0.392 @ 26] | 0.074 [-0.023 @ 26] |
| 21 | 0.553 [0.307 @ 26] | 0.025 [-0.073 @ 27] |
| 32 | 0.546 [0.302 @ 26] | 0.051 [-0.085 @ 27] |
| 42 | 0.793 [0.721 @ 47] | 0.155 [-0.017 @ 9] |

Flattened over layers (per-layer-normalized): mean 0.542, min 0.366 at boundary 26, first boundary 0.498, last 0.444.
Centered: mean 0.083, min 0.015 at boundary 27, first 0.054, last 0.049.
Change points (z < -2.0) per item: raw 1.32, centered 0.90.
Most frequent change-point boundaries (raw): F26|F27 (45 items), F39|F40 (10 items), F13|F14 (3 items), F49|F50 (2 items), F30|F31 (2 items)
Most frequent change-point boundaries (centered): F45|F46 (7 items), F8|F9 (4 items), F9|F10 (4 items), F44|F45 (3 items), F37|F38 (3 items)

Centered cosine filler -> q_last: peaks at layer 3 (mean over filler 0.052; F1 0.112, F50 0.040).
Centered cosine filler -> cue: peaks at layer 28 (mean over filler 0.109; F1 0.137, F50 0.028).
Centered cosine filler -> gen: peaks at layer 28 (mean over filler 0.106; F1 0.141, F50 0.015).

Per stream, mean adjacent cosine at three-quarter depth (raw / centered):
- stream 0: 0.358 / 0.044
- stream 1: 0.455 / 0.012
- stream 2: 0.312 / 0.028
- stream 3: 0.572 / 0.069
