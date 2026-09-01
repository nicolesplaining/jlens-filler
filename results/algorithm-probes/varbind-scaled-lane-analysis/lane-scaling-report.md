# Variable-binding filler-lane scaling

These are J-Lens token readouts, not formal sparse J-space coordinates.
Top-lane recurrence compares three coordinate hypotheses: fixed absolute dot ordinal, proportional location in the filler span, and fixed distance from the answer cue.

## Readout recurrence

| Readout | Stage | Coordinate | N comparisons | Mean top-lane hit rate | Median |
|---|---|---|---:|---:|---:|
| j_lens | answer | absolute | 30 | 0.317 | 0.300 |
| j_lens | answer | end_relative | 30 | 0.190 | 0.000 |
| j_lens | answer | relative | 30 | 0.260 | 0.200 |
| j_lens | base_value | absolute | 30 | 0.207 | 0.000 |
| j_lens | base_value | end_relative | 30 | 0.123 | 0.000 |
| j_lens | base_value | relative | 30 | 0.250 | 0.150 |
| j_lens | bound_value | absolute | 30 | 0.223 | 0.000 |
| j_lens | bound_value | end_relative | 30 | 0.263 | 0.150 |
| j_lens | bound_value | relative | 30 | 0.307 | 0.200 |
| j_lens | second_product | absolute | 30 | 0.220 | 0.000 |
| j_lens | second_product | end_relative | 30 | 0.390 | 0.400 |
| j_lens | second_product | relative | 30 | 0.367 | 0.200 |
| logit_lens | answer | absolute | 30 | 0.350 | 0.400 |
| logit_lens | answer | end_relative | 30 | 0.163 | 0.000 |
| logit_lens | answer | relative | 30 | 0.400 | 0.450 |
| logit_lens | base_value | absolute | 30 | 0.333 | 0.200 |
| logit_lens | base_value | end_relative | 30 | 0.147 | 0.000 |
| logit_lens | base_value | relative | 30 | 0.373 | 0.400 |
| logit_lens | bound_value | absolute | 30 | 0.257 | 0.000 |
| logit_lens | bound_value | end_relative | 30 | 0.247 | 0.100 |
| logit_lens | bound_value | relative | 30 | 0.253 | 0.050 |
| logit_lens | second_product | absolute | 30 | 0.180 | 0.000 |
| logit_lens | second_product | end_relative | 30 | 0.367 | 0.200 |
| logit_lens | second_product | relative | 30 | 0.363 | 0.300 |

## Readout recurrence when the donor is correct at both lengths

| Readout | Stage | Coordinate | N comparisons | Mean top-lane hit rate | Median |
|---|---|---|---:|---:|---:|
| j_lens | answer | absolute | 22 | 0.273 | 0.200 |
| j_lens | answer | end_relative | 22 | 0.168 | 0.050 |
| j_lens | answer | relative | 22 | 0.241 | 0.200 |
| j_lens | base_value | absolute | 22 | 0.191 | 0.050 |
| j_lens | base_value | end_relative | 22 | 0.123 | 0.000 |
| j_lens | base_value | relative | 22 | 0.250 | 0.200 |
| j_lens | bound_value | absolute | 22 | 0.236 | 0.100 |
| j_lens | bound_value | end_relative | 22 | 0.177 | 0.050 |
| j_lens | bound_value | relative | 22 | 0.191 | 0.150 |
| j_lens | second_product | absolute | 22 | 0.277 | 0.250 |
| j_lens | second_product | end_relative | 22 | 0.350 | 0.300 |
| j_lens | second_product | relative | 22 | 0.273 | 0.150 |
| logit_lens | answer | absolute | 22 | 0.273 | 0.200 |
| logit_lens | answer | end_relative | 22 | 0.177 | 0.100 |
| logit_lens | answer | relative | 22 | 0.341 | 0.300 |
| logit_lens | base_value | absolute | 22 | 0.227 | 0.050 |
| logit_lens | base_value | end_relative | 22 | 0.177 | 0.050 |
| logit_lens | base_value | relative | 22 | 0.282 | 0.300 |
| logit_lens | bound_value | absolute | 22 | 0.305 | 0.200 |
| logit_lens | bound_value | end_relative | 22 | 0.200 | 0.100 |
| logit_lens | bound_value | relative | 22 | 0.209 | 0.050 |
| logit_lens | second_product | absolute | 22 | 0.177 | 0.000 |
| logit_lens | second_product | end_relative | 22 | 0.318 | 0.200 |
| logit_lens | second_product | relative | 22 | 0.268 | 0.000 |

## Full-profile recurrence when the donor is correct at both lengths

Spearman correlations compare the complete per-position top-10 strength profile after applying each coordinate mapping.

| Readout | Stage | Coordinate | N comparisons | Mean profile ρ | Median profile ρ |
|---|---|---|---:|---:|---:|
| j_lens | answer | absolute | 20 | 0.166 | 0.155 |
| j_lens | answer | end_relative | 18 | 0.007 | 0.016 |
| j_lens | answer | relative | 21 | -0.024 | -0.017 |
| j_lens | base_value | absolute | 12 | -0.038 | -0.100 |
| j_lens | base_value | end_relative | 10 | -0.083 | -0.082 |
| j_lens | base_value | relative | 10 | 0.087 | -0.075 |
| j_lens | bound_value | absolute | 12 | 0.009 | -0.093 |
| j_lens | bound_value | end_relative | 13 | -0.038 | -0.087 |
| j_lens | bound_value | relative | 11 | -0.055 | -0.075 |
| j_lens | second_product | absolute | 12 | 0.110 | 0.103 |
| j_lens | second_product | end_relative | 14 | 0.202 | 0.131 |
| j_lens | second_product | relative | 15 | 0.017 | 0.036 |
| logit_lens | answer | absolute | 16 | 0.091 | 0.015 |
| logit_lens | answer | end_relative | 14 | 0.024 | -0.081 |
| logit_lens | answer | relative | 18 | 0.036 | 0.055 |
| logit_lens | base_value | absolute | 8 | 0.001 | -0.047 |
| logit_lens | base_value | end_relative | 8 | -0.097 | -0.075 |
| logit_lens | base_value | relative | 9 | 0.129 | 0.167 |
| logit_lens | bound_value | absolute | 10 | 0.064 | -0.058 |
| logit_lens | bound_value | end_relative | 12 | -0.007 | -0.087 |
| logit_lens | bound_value | relative | 10 | -0.016 | -0.064 |
| logit_lens | second_product | absolute | 10 | -0.004 | 0.002 |
| logit_lens | second_product | end_relative | 14 | 0.235 | 0.207 |
| logit_lens | second_product | relative | 15 | -0.024 | -0.166 |

## Stage-addressed readout peaks at k=50

Profiles average top-10 target strength over correct exact-layout family members and layers 24–38. Strength is the rank-weighted number of top-10 layers at that dot (range 0–15).

| Readout | Stage | Strongest dot | Mean strength | Next strongest dots |
|---|---|---:|---:|---|
| j_lens | base_value | F44 | 6.383 | F15, F28, F11, F16 |
| j_lens | bound_value | F43 | 5.550 | F15, F5, F16, F41 |
| j_lens | second_product | F50 | 5.217 | F41, F15, F40, F16 |
| j_lens | answer | F1 | 3.317 | F20, F36, F40, F35 |
| logit_lens | base_value | F44 | 4.100 | F45, F11, F28, F14 |
| logit_lens | bound_value | F43 | 3.883 | F15, F5, F41, F16 |
| logit_lens | second_product | F41 | 4.867 | F40, F15, F16, F50 |
| logit_lens | answer | F40 | 3.400 | F21, F1, F35, F36 |
