# Adjacent-position cosine across the filler span

## qwen-dotsonly-counting-scrambled (50 items, 140 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.985 [0.981 @ 97] | 0.305 [0.007 @ 10] |
| 8 | 0.903 [0.837 @ 68] | 0.112 [-0.021 @ 28] |
| 16 | 0.819 [0.508 @ 68] | 0.134 [-0.023 @ 11] |
| 24 | 0.667 [0.144 @ 103] | 0.230 [-0.001 @ 82] |
| 31 | 0.576 [0.097 @ 68] | 0.202 [0.001 @ 132] |

Flattened over layers (per-layer-normalized): mean 0.784, min 0.578 at boundary 104, first boundary 0.880, last 0.844.
Centered: mean 0.191, min 0.054 at boundary 34, first 0.324, last 0.216.
Change points (z < -2.0) per item: raw 0.88, centered 0.32.
Most frequent change-point boundaries (raw): F104|F105 (14 items), F9|F10 (8 items), F69|F70 (5 items), F103|F104 (4 items), F8|F9 (3 items)
Most frequent change-point boundaries (centered): F44|F45 (5 items), F135|F136 (4 items), F5|F6 (3 items), F92|F93 (2 items), F11|F12 (1 items)

Centered cosine filler -> q_last: peaks at layer 18 (mean over filler 0.165; F1 0.160, F140 0.321).
Centered cosine filler -> cue: peaks at layer 18 (mean over filler 0.222; F1 0.178, F140 0.374).
Centered cosine filler -> gen: peaks at layer 18 (mean over filler 0.214; F1 0.191, F140 0.405).
