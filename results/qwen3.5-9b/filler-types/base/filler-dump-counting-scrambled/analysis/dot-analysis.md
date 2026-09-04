# What happens at dot positions (50 held-out items, k=140)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-counting-scrambled | var frac: problem | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 |
| qwen-base-counting-scrambled | var frac: position | 1.00 | 0.96 | 0.75 | 0.57 | 0.59 | 0.60 |
| qwen-base-counting-scrambled | cos same pos, other problems | 1.00 | 0.99 | 0.92 | 0.79 | 0.83 | 0.78 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-base-counting-scrambled | dots_mean | base_value | -0.42 | 0.10 | 0.31 | 0.43 | 0.32 | 0.14 | L24 (0.43) |
| qwen-base-counting-scrambled | dots_mean | bound_value | -0.48 | -0.10 | 0.34 | 0.44 | 0.35 | 0.19 | L19 (0.46) |
| qwen-base-counting-scrambled | dots_mean | answer | -0.41 | -0.04 | 0.35 | 0.45 | 0.34 | 0.18 | L19 (0.47) |
| qwen-base-counting-scrambled | dots_mean | answer_SHUFFLED | -0.85 | -1.05 | -0.25 | -0.16 | -0.23 | -0.29 | L22 (-0.07) |
| qwen-base-counting-scrambled | q_last | base_value | -0.97 | -0.92 | -0.29 | -0.03 | -0.09 | -0.27 | L18 (0.15) |
| qwen-base-counting-scrambled | q_last | bound_value | -0.97 | -0.95 | -0.16 | 0.09 | 0.08 | -0.03 | L18 (0.29) |
| qwen-base-counting-scrambled | q_last | answer | -0.81 | -0.81 | -0.05 | 0.18 | 0.16 | 0.06 | L18 (0.36) |
| qwen-base-counting-scrambled | q_last | answer_SHUFFLED | -0.87 | -1.39 | -1.28 | -1.03 | -0.67 | -0.80 | L1 (-0.55) |
| qwen-base-counting-scrambled | cue | base_value | -0.73 | -0.39 | 0.26 | 0.74 | 0.69 | 0.69 | L23 (0.77) |
| qwen-base-counting-scrambled | cue | bound_value | -0.98 | -0.48 | 0.34 | 0.79 | 0.72 | 0.73 | L23 (0.81) |
| qwen-base-counting-scrambled | cue | answer | -0.80 | -0.40 | 0.43 | 0.82 | 0.75 | 0.76 | L23 (0.84) |
| qwen-base-counting-scrambled | cue | answer_SHUFFLED | -1.22 | -0.57 | -0.40 | -1.72 | -1.70 | -1.49 | L4 (-0.14) |
| qwen-base-counting-scrambled | gen | base_value | -0.71 | -0.11 | 0.36 | 0.60 | 0.66 | 0.67 | L31 (0.67) |
| qwen-base-counting-scrambled | gen | bound_value | -1.30 | -0.17 | 0.41 | 0.70 | 0.77 | 0.76 | L28 (0.77) |
| qwen-base-counting-scrambled | gen | answer | -1.16 | -0.12 | 0.47 | 0.76 | 0.78 | 0.78 | L28 (0.80) |
| qwen-base-counting-scrambled | gen | answer_SHUFFLED | -0.56 | -0.46 | -0.38 | -0.12 | -0.19 | -0.04 | L26 (-0.04) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-base-counting-scrambled

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.028 | 0.701 | 0.043 | 0.002 | 0.226 | 0.01 |
| 3 | cue | 0.007 | 0.809 | 0.129 | 0.016 | 0.039 |  |
| 3 | dots | 0.002 | 0.710 | 0.113 | 0.175 | 0.000 |  |
| 7 | gen | 0.041 | 0.746 | 0.009 | 0.001 | 0.203 | 0.01 |
| 7 | cue | 0.009 | 0.625 | 0.297 | 0.025 | 0.045 |  |
| 7 | dots | 0.007 | 0.651 | 0.120 | 0.223 | 0.000 |  |
| 11 | gen | 0.025 | 0.806 | 0.008 | 0.003 | 0.158 | 0.01 |
| 11 | cue | 0.020 | 0.538 | 0.364 | 0.036 | 0.042 |  |
| 11 | dots | 0.009 | 0.774 | 0.100 | 0.118 | 0.000 |  |
| 15 | gen | 0.053 | 0.800 | 0.008 | 0.008 | 0.131 | 0.03 |
| 15 | cue | 0.025 | 0.468 | 0.411 | 0.054 | 0.042 |  |
| 15 | dots | 0.015 | 0.811 | 0.095 | 0.078 | 0.000 |  |
| 19 | gen | 0.023 | 0.556 | 0.212 | 0.042 | 0.166 | 0.10 |
| 19 | cue | 0.008 | 0.313 | 0.571 | 0.093 | 0.015 |  |
| 19 | dots | 0.020 | 0.761 | 0.106 | 0.113 | 0.000 |  |
| 23 | gen | 0.051 | 0.533 | 0.184 | 0.033 | 0.198 | 0.11 |
| 23 | cue | 0.012 | 0.262 | 0.478 | 0.187 | 0.061 |  |
| 23 | dots | 0.025 | 0.758 | 0.120 | 0.097 | 0.000 |  |
| 27 | gen | 0.104 | 0.495 | 0.040 | 0.017 | 0.344 | 0.07 |
| 27 | cue | 0.127 | 0.666 | 0.103 | 0.055 | 0.049 |  |
| 27 | dots | 0.073 | 0.776 | 0.086 | 0.066 | 0.000 |  |
| 31 | gen | 0.029 | 0.429 | 0.014 | 0.007 | 0.521 | 0.02 |
| 31 | cue | 0.026 | 0.708 | 0.036 | 0.010 | 0.219 |  |
| 31 | dots | 0.047 | 0.710 | 0.064 | 0.179 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-counting-scrambled | entropy_dots | 11.22 | 11.53 | 11.18 | 9.15 | 3.85 | 0.46 |
| qwen-base-counting-scrambled | entropy_qlast | 11.20 | 11.61 | 11.44 | 9.33 | 4.04 | 0.39 |
| qwen-base-counting-scrambled | entropy_gen | 11.49 | 11.14 | 10.58 | 10.75 | 6.63 | 1.34 |
| qwen-base-counting-scrambled | norm_dots | 6.02 | 18.81 | 34.89 | 81.15 | 148.59 | 177.75 |
| qwen-base-counting-scrambled | norm_qlast | 5.12 | 17.98 | 34.42 | 94.02 | 158.34 | 212.58 |
| qwen-base-counting-scrambled | norm_gen | 4.99 | 14.99 | 27.37 | 71.95 | 144.59 | 253.17 |
