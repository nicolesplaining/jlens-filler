# What happens at dot positions (50 held-out items, k=50)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet | var frac: problem | 0.00 | 0.00 | 0.02 | 0.04 | 0.05 | 0.04 |
| qwen-dotsonly-alphabet | var frac: position | 1.00 | 0.93 | 0.70 | 0.62 | 0.56 | 0.65 |
| qwen-dotsonly-alphabet | cos same pos, other problems | 1.00 | 1.00 | 0.96 | 0.90 | 0.91 | 0.89 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet | dots_mean | base_value | -1.49 | -0.05 | 0.73 | 0.96 | 0.93 | 0.93 | L26 (0.96) |
| qwen-dotsonly-alphabet | dots_mean | bound_value | -1.40 | -0.05 | 0.78 | 0.94 | 0.91 | 0.91 | L20 (0.94) |
| qwen-dotsonly-alphabet | dots_mean | answer | -1.27 | 0.07 | 0.80 | 0.95 | 0.93 | 0.93 | L22 (0.95) |
| qwen-dotsonly-alphabet | dots_mean | answer_SHUFFLED | -0.99 | -0.78 | -0.12 | -0.28 | -0.21 | -0.19 | L26 (-0.05) |
| qwen-dotsonly-alphabet | q_last | base_value | -1.09 | -1.20 | 0.43 | 0.86 | 0.74 | 0.74 | L21 (0.89) |
| qwen-dotsonly-alphabet | q_last | bound_value | -1.07 | -1.25 | 0.54 | 0.90 | 0.83 | 0.83 | L21 (0.92) |
| qwen-dotsonly-alphabet | q_last | answer | -0.95 | -1.04 | 0.58 | 0.90 | 0.84 | 0.84 | L21 (0.92) |
| qwen-dotsonly-alphabet | q_last | answer_SHUFFLED | -0.74 | -1.05 | -0.44 | -0.96 | -0.32 | -0.25 | L30 (-0.25) |
| qwen-dotsonly-alphabet | cue | base_value | -0.96 | -0.47 | 0.62 | 0.98 | 0.94 | 0.94 | L19 (0.98) |
| qwen-dotsonly-alphabet | cue | bound_value | -0.95 | -0.34 | 0.70 | 0.97 | 0.93 | 0.93 | L19 (0.98) |
| qwen-dotsonly-alphabet | cue | answer | -0.87 | -0.22 | 0.72 | 0.97 | 0.95 | 0.95 | L19 (0.98) |
| qwen-dotsonly-alphabet | cue | answer_SHUFFLED | -0.85 | 0.08 | -0.34 | -1.38 | -1.32 | -1.12 | L2 (0.11) |
| qwen-dotsonly-alphabet | gen | base_value | -0.68 | 0.09 | 0.82 | 0.96 | 0.93 | 0.92 | L22 (0.97) |
| qwen-dotsonly-alphabet | gen | bound_value | -0.93 | 0.02 | 0.85 | 0.95 | 0.89 | 0.89 | L22 (0.97) |
| qwen-dotsonly-alphabet | gen | answer | -0.88 | 0.06 | 0.86 | 0.96 | 0.93 | 0.93 | L22 (0.97) |
| qwen-dotsonly-alphabet | gen | answer_SHUFFLED | -1.28 | -0.58 | -0.69 | 0.02 | -0.65 | -0.61 | L19 (0.16) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-dotsonly-alphabet

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.037 | 0.710 | 0.046 | 0.001 | 0.205 | 0.01 |
| 3 | cue | 0.014 | 0.783 | 0.152 | 0.022 | 0.030 |  |
| 3 | dots | 0.007 | 0.791 | 0.089 | 0.112 | 0.000 |  |
| 7 | gen | 0.057 | 0.677 | 0.027 | 0.001 | 0.238 | 0.00 |
| 7 | cue | 0.006 | 0.454 | 0.515 | 0.004 | 0.021 |  |
| 7 | dots | 0.006 | 0.683 | 0.206 | 0.105 | 0.000 |  |
| 11 | gen | 0.021 | 0.807 | 0.027 | 0.001 | 0.144 | 0.00 |
| 11 | cue | 0.017 | 0.253 | 0.639 | 0.021 | 0.070 |  |
| 11 | dots | 0.021 | 0.495 | 0.408 | 0.076 | 0.000 |  |
| 15 | gen | 0.037 | 0.757 | 0.045 | 0.009 | 0.153 | 0.06 |
| 15 | cue | 0.017 | 0.394 | 0.508 | 0.049 | 0.033 |  |
| 15 | dots | 0.014 | 0.582 | 0.330 | 0.073 | 0.000 |  |
| 19 | gen | 0.006 | 0.194 | 0.721 | 0.035 | 0.044 | 0.16 |
| 19 | cue | 0.004 | 0.209 | 0.760 | 0.025 | 0.002 |  |
| 19 | dots | 0.013 | 0.604 | 0.310 | 0.073 | 0.000 |  |
| 23 | gen | 0.024 | 0.249 | 0.450 | 0.089 | 0.189 | 0.16 |
| 23 | cue | 0.023 | 0.245 | 0.646 | 0.069 | 0.017 |  |
| 23 | dots | 0.026 | 0.640 | 0.212 | 0.122 | 0.000 |  |
| 27 | gen | 0.123 | 0.579 | 0.075 | 0.015 | 0.208 | 0.06 |
| 27 | cue | 0.129 | 0.690 | 0.130 | 0.036 | 0.017 |  |
| 27 | dots | 0.092 | 0.760 | 0.080 | 0.068 | 0.000 |  |
| 31 | gen | 0.011 | 0.469 | 0.023 | 0.007 | 0.489 | 0.04 |
| 31 | cue | 0.005 | 0.737 | 0.042 | 0.020 | 0.196 |  |
| 31 | dots | 0.013 | 0.697 | 0.023 | 0.266 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet | entropy_dots | 11.22 | 11.67 | 11.38 | 10.70 | 5.58 | 0.04 |
| qwen-dotsonly-alphabet | entropy_qlast | 11.24 | 11.56 | 11.36 | 10.36 | 6.82 | 0.02 |
| qwen-dotsonly-alphabet | entropy_gen | 11.51 | 11.41 | 11.08 | 10.66 | 7.66 | 0.16 |
| qwen-dotsonly-alphabet | norm_dots | 6.41 | 20.11 | 36.76 | 87.08 | 168.78 | 194.30 |
| qwen-dotsonly-alphabet | norm_qlast | 5.08 | 22.18 | 36.14 | 82.39 | 162.85 | 216.65 |
| qwen-dotsonly-alphabet | norm_gen | 5.03 | 17.82 | 31.74 | 83.75 | 231.91 | 352.65 |
