# Variable-binding deep dive: all dot-rescued examples

These are **J-Lens token readouts**, not formal sparse J-space coordinates.
The primary cohort is all 14 examples that are wrong without filler and correct with 50 post-question dots. Every stage is compared with the same stage value borrowed from a collision-free donor example.

## Stage timing and shuffled controls

| Readout | Stage | Rank-1 examples | Median first rank-1 layer | Median first rank-1 dot | Actual/control rank-1 cells |
|---|---|---:|---:|---:|---:|
| J-Lens | visible base | 13 / 14 | 24.0 | 15.0 | 201 / 0 |
| J-Lens | first product | 4 / 14 | 32.0 | 28.5 | 17 / 0 |
| J-Lens | hidden bound value | 14 / 14 | 31.0 | 15.0 | 392 / 1 |
| J-Lens | second product | 13 / 14 | 31.0 | 21.0 | 447 / 0 |
| J-Lens | answer | 14 / 14 | 36.0 | 12.5 | 508 / 0 |
| Logit lens | visible base | 11 / 14 | 25.0 | 15.0 | 172 / 2 |
| Logit lens | first product | 5 / 14 | 30.0 | 21.0 | 18 / 0 |
| Logit lens | hidden bound value | 14 / 14 | 30.0 | 16.0 | 291 / 2 |
| Logit lens | second product | 13 / 14 | 31.0 | 29.0 | 445 / 0 |
| Logit lens | answer | 14 / 14 | 36.0 | 17.0 | 481 / 0 |

## Depth versus dot ordinal

Spearman correlations use the first exact rank-1 readout for the visible base, hidden bound value, second product, and final answer within each example.

| Readout | Examples measurable | Median stage↔layer ρ | Examples measurable | Median stage↔dot-position ρ |
|---|---:|---:|---:|---:|
| J-Lens | 13 | 0.9486832980505138 | 13 | -0.21081851067789195 |
| Logit lens | 14 | 1.0 | 14 | 0.1 |

## Causal follow-up

The patch manifest uses the matched pair `varbind_easy_0033 ↔ varbind_easy_0002`. Both are rescued by 50 dots and share the same final operation `2 × bound − 14`, so transferring the bound value has a clear counterfactual prediction for the answer.
