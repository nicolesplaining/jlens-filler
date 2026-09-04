# Adjacent-position cosine across the filler span

## llama-8b-it (50 items, 50 filler positions, 32 layers)

Mean adjacent cosine cos(F_p, F_p+1) by layer (mean over items and boundaries; min over boundaries in brackets):

| layer | raw | centered (problem component) |
|---:|---:|---:|
| 0 | 0.981 [0.510 @ 49] | 0.845 [0.319 @ 49] |
| 8 | 0.830 [0.228 @ 2] | 0.593 [-0.027 @ 4] |
| 16 | 0.721 [0.147 @ 2] | 0.444 [-0.099 @ 4] |
| 24 | 0.776 [0.209 @ 2] | 0.447 [-0.149 @ 4] |
| 31 | 0.863 [0.345 @ 49] | 0.578 [-0.017 @ 4] |

Flattened over layers (per-layer-normalized): mean 0.813, min 0.331 at boundary 2, first boundary 0.369, last 0.492.
Centered: mean 0.543, min 0.081 at boundary 4, first 0.128, last 0.318.
Change points (z < -2.0) per item: raw 2.08, centered 0.44.
Most frequent change-point boundaries (raw): F2|F3 (50 items), F1|F2 (43 items), F3|F4 (11 items), F37|F38 (0 items), F34|F35 (0 items)
Most frequent change-point boundaries (centered): F4|F5 (22 items), F33|F34 (0 items), F31|F32 (0 items), F34|F35 (0 items), F35|F36 (0 items)

Centered cosine filler -> q_last: peaks at layer 31 (mean over filler 0.155; F1 0.064, F50 0.382).
Centered cosine filler -> cue: peaks at layer 5 (mean over filler 0.203; F1 0.206, F50 0.430).
Centered cosine filler -> gen: peaks at layer 0 (mean over filler 0.165; F1 0.163, F50 0.333).
