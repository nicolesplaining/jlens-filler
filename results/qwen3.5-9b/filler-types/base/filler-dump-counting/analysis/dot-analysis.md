# What happens at dot positions (50 held-out items, k=140)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-counting | var frac: problem | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 |
| qwen-base-counting | var frac: position | 1.00 | 0.95 | 0.73 | 0.58 | 0.60 | 0.61 |
| qwen-base-counting | cos same pos, other problems | 1.00 | 0.99 | 0.92 | 0.77 | 0.81 | 0.73 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-base-counting | dots_mean | base_value | -0.42 | 0.12 | 0.13 | 0.42 | 0.30 | 0.13 | L26 (0.44) |
| qwen-base-counting | dots_mean | bound_value | -0.46 | -0.05 | 0.21 | 0.41 | 0.36 | 0.22 | L19 (0.49) |
| qwen-base-counting | dots_mean | answer | -0.39 | 0.01 | 0.24 | 0.45 | 0.37 | 0.23 | L19 (0.51) |
| qwen-base-counting | dots_mean | answer_SHUFFLED | -0.96 | -0.41 | -0.23 | -0.10 | -0.28 | -0.36 | L25 (-0.09) |
| qwen-base-counting | q_last | base_value | -0.94 | -0.67 | -0.32 | 0.02 | -0.04 | -0.20 | L18 (0.16) |
| qwen-base-counting | q_last | bound_value | -0.93 | -0.79 | -0.16 | 0.13 | 0.10 | -0.01 | L18 (0.30) |
| qwen-base-counting | q_last | answer | -0.79 | -0.65 | -0.04 | 0.23 | 0.19 | 0.09 | L18 (0.38) |
| qwen-base-counting | q_last | answer_SHUFFLED | -0.87 | -1.28 | -1.27 | -1.00 | -0.70 | -0.70 | L4 (-0.53) |
| qwen-base-counting | cue | base_value | -0.67 | -0.60 | 0.28 | 0.73 | 0.67 | 0.67 | L23 (0.74) |
| qwen-base-counting | cue | bound_value | -0.92 | -0.58 | 0.37 | 0.76 | 0.69 | 0.67 | L25 (0.77) |
| qwen-base-counting | cue | answer | -0.73 | -0.48 | 0.44 | 0.80 | 0.74 | 0.72 | L23 (0.80) |
| qwen-base-counting | cue | answer_SHUFFLED | -1.22 | -0.35 | -0.42 | -0.81 | -0.75 | -0.67 | L2 (-0.15) |
| qwen-base-counting | gen | base_value | -0.66 | 0.06 | 0.26 | 0.56 | 0.67 | 0.68 | L31 (0.68) |
| qwen-base-counting | gen | bound_value | -1.13 | -0.03 | 0.25 | 0.66 | 0.73 | 0.73 | L28 (0.74) |
| qwen-base-counting | gen | answer | -1.03 | 0.01 | 0.31 | 0.71 | 0.77 | 0.77 | L28 (0.77) |
| qwen-base-counting | gen | answer_SHUFFLED | -0.49 | -0.45 | -0.45 | -0.59 | -0.50 | -0.43 | L1 (-0.13) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-base-counting

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.028 | 0.693 | 0.041 | 0.002 | 0.235 | 0.01 |
| 3 | cue | 0.007 | 0.796 | 0.139 | 0.013 | 0.044 |  |
| 3 | dots | 0.004 | 0.652 | 0.165 | 0.180 | 0.000 |  |
| 7 | gen | 0.043 | 0.747 | 0.009 | 0.002 | 0.199 | 0.01 |
| 7 | cue | 0.009 | 0.579 | 0.334 | 0.032 | 0.045 |  |
| 7 | dots | 0.009 | 0.621 | 0.165 | 0.205 | 0.000 |  |
| 11 | gen | 0.024 | 0.814 | 0.009 | 0.002 | 0.151 | 0.01 |
| 11 | cue | 0.019 | 0.585 | 0.313 | 0.040 | 0.042 |  |
| 11 | dots | 0.011 | 0.724 | 0.129 | 0.136 | 0.000 |  |
| 15 | gen | 0.060 | 0.791 | 0.008 | 0.008 | 0.133 | 0.03 |
| 15 | cue | 0.020 | 0.447 | 0.402 | 0.092 | 0.038 |  |
| 15 | dots | 0.015 | 0.774 | 0.109 | 0.103 | 0.000 |  |
| 19 | gen | 0.024 | 0.543 | 0.196 | 0.071 | 0.166 | 0.18 |
| 19 | cue | 0.009 | 0.314 | 0.580 | 0.085 | 0.012 |  |
| 19 | dots | 0.022 | 0.703 | 0.129 | 0.146 | 0.000 |  |
| 23 | gen | 0.052 | 0.553 | 0.156 | 0.029 | 0.209 | 0.07 |
| 23 | cue | 0.014 | 0.268 | 0.468 | 0.188 | 0.062 |  |
| 23 | dots | 0.022 | 0.695 | 0.137 | 0.147 | 0.000 |  |
| 27 | gen | 0.098 | 0.506 | 0.035 | 0.016 | 0.345 | 0.10 |
| 27 | cue | 0.119 | 0.671 | 0.094 | 0.068 | 0.047 |  |
| 27 | dots | 0.077 | 0.758 | 0.099 | 0.066 | 0.000 |  |
| 31 | gen | 0.030 | 0.428 | 0.013 | 0.006 | 0.523 | 0.02 |
| 31 | cue | 0.026 | 0.707 | 0.034 | 0.012 | 0.221 |  |
| 31 | dots | 0.046 | 0.687 | 0.071 | 0.195 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-counting | entropy_dots | 11.22 | 11.45 | 11.18 | 8.38 | 4.36 | 0.38 |
| qwen-base-counting | entropy_qlast | 11.20 | 11.60 | 11.42 | 9.26 | 3.74 | 0.34 |
| qwen-base-counting | entropy_gen | 11.49 | 11.17 | 10.59 | 10.79 | 7.07 | 1.36 |
| qwen-base-counting | norm_dots | 6.06 | 18.84 | 34.62 | 80.94 | 150.08 | 174.01 |
| qwen-base-counting | norm_qlast | 5.11 | 17.87 | 34.15 | 93.48 | 158.18 | 213.05 |
| qwen-base-counting | norm_gen | 4.99 | 15.02 | 27.11 | 74.31 | 146.49 | 255.13 |
