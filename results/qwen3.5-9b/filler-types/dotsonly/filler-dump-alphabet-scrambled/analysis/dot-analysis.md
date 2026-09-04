# What happens at dot positions (50 held-out items, k=50)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet-scrambled | var frac: problem | 0.00 | 0.00 | 0.01 | 0.03 | 0.04 | 0.03 |
| qwen-dotsonly-alphabet-scrambled | var frac: position | 1.00 | 0.92 | 0.74 | 0.65 | 0.59 | 0.66 |
| qwen-dotsonly-alphabet-scrambled | cos same pos, other problems | 1.00 | 0.99 | 0.95 | 0.88 | 0.89 | 0.89 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet-scrambled | dots_mean | base_value | -1.62 | 0.00 | 0.79 | 0.94 | 0.91 | 0.92 | L19 (0.96) |
| qwen-dotsonly-alphabet-scrambled | dots_mean | bound_value | -1.51 | 0.04 | 0.83 | 0.94 | 0.92 | 0.92 | L19 (0.96) |
| qwen-dotsonly-alphabet-scrambled | dots_mean | answer | -1.37 | 0.13 | 0.85 | 0.96 | 0.93 | 0.94 | L19 (0.97) |
| qwen-dotsonly-alphabet-scrambled | dots_mean | answer_SHUFFLED | -0.91 | -0.83 | -0.25 | -0.30 | -0.45 | -0.37 | L14 (-0.06) |
| qwen-dotsonly-alphabet-scrambled | q_last | base_value | -0.93 | -1.27 | 0.45 | 0.87 | 0.74 | 0.74 | L21 (0.89) |
| qwen-dotsonly-alphabet-scrambled | q_last | bound_value | -0.92 | -1.28 | 0.55 | 0.90 | 0.83 | 0.83 | L21 (0.91) |
| qwen-dotsonly-alphabet-scrambled | q_last | answer | -0.80 | -1.07 | 0.59 | 0.90 | 0.84 | 0.84 | L21 (0.92) |
| qwen-dotsonly-alphabet-scrambled | q_last | answer_SHUFFLED | -0.79 | -1.10 | -0.55 | -0.91 | -0.42 | -0.31 | L31 (-0.31) |
| qwen-dotsonly-alphabet-scrambled | cue | base_value | -0.71 | -0.72 | 0.66 | 0.98 | 0.94 | 0.94 | L19 (0.99) |
| qwen-dotsonly-alphabet-scrambled | cue | bound_value | -0.76 | -0.57 | 0.74 | 0.97 | 0.93 | 0.94 | L19 (0.98) |
| qwen-dotsonly-alphabet-scrambled | cue | answer | -0.66 | -0.42 | 0.76 | 0.97 | 0.95 | 0.95 | L19 (0.98) |
| qwen-dotsonly-alphabet-scrambled | cue | answer_SHUFFLED | -1.11 | 0.08 | -0.28 | -1.31 | -1.36 | -1.11 | L7 (0.11) |
| qwen-dotsonly-alphabet-scrambled | gen | base_value | -0.96 | 0.11 | 0.80 | 0.96 | 0.93 | 0.93 | L22 (0.97) |
| qwen-dotsonly-alphabet-scrambled | gen | bound_value | -1.13 | 0.03 | 0.83 | 0.95 | 0.89 | 0.89 | L22 (0.96) |
| qwen-dotsonly-alphabet-scrambled | gen | answer | -1.08 | 0.09 | 0.84 | 0.96 | 0.93 | 0.93 | L22 (0.97) |
| qwen-dotsonly-alphabet-scrambled | gen | answer_SHUFFLED | -1.04 | 0.01 | -0.33 | -0.03 | -0.75 | -0.63 | L9 (0.27) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-dotsonly-alphabet-scrambled

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.039 | 0.712 | 0.046 | 0.001 | 0.203 | 0.00 |
| 3 | cue | 0.013 | 0.788 | 0.153 | 0.018 | 0.027 |  |
| 3 | dots | 0.007 | 0.840 | 0.091 | 0.062 | 0.000 |  |
| 7 | gen | 0.057 | 0.676 | 0.027 | 0.001 | 0.240 | 0.01 |
| 7 | cue | 0.006 | 0.438 | 0.528 | 0.002 | 0.025 |  |
| 7 | dots | 0.008 | 0.742 | 0.165 | 0.085 | 0.000 |  |
| 11 | gen | 0.021 | 0.812 | 0.025 | 0.001 | 0.142 | 0.00 |
| 11 | cue | 0.017 | 0.255 | 0.640 | 0.016 | 0.072 |  |
| 11 | dots | 0.016 | 0.542 | 0.375 | 0.067 | 0.000 |  |
| 15 | gen | 0.039 | 0.752 | 0.045 | 0.008 | 0.156 | 0.05 |
| 15 | cue | 0.017 | 0.394 | 0.516 | 0.041 | 0.033 |  |
| 15 | dots | 0.017 | 0.687 | 0.244 | 0.052 | 0.000 |  |
| 19 | gen | 0.006 | 0.189 | 0.727 | 0.035 | 0.043 | 0.16 |
| 19 | cue | 0.004 | 0.204 | 0.768 | 0.022 | 0.002 |  |
| 19 | dots | 0.013 | 0.677 | 0.254 | 0.056 | 0.000 |  |
| 23 | gen | 0.026 | 0.248 | 0.455 | 0.077 | 0.193 | 0.14 |
| 23 | cue | 0.024 | 0.234 | 0.664 | 0.058 | 0.019 |  |
| 23 | dots | 0.026 | 0.702 | 0.167 | 0.104 | 0.000 |  |
| 27 | gen | 0.133 | 0.572 | 0.078 | 0.012 | 0.204 | 0.05 |
| 27 | cue | 0.140 | 0.671 | 0.140 | 0.028 | 0.021 |  |
| 27 | dots | 0.103 | 0.760 | 0.067 | 0.070 | 0.000 |  |
| 31 | gen | 0.012 | 0.474 | 0.024 | 0.006 | 0.483 | 0.03 |
| 31 | cue | 0.005 | 0.740 | 0.043 | 0.014 | 0.198 |  |
| 31 | dots | 0.013 | 0.698 | 0.021 | 0.268 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-alphabet-scrambled | entropy_dots | 11.23 | 11.70 | 11.42 | 10.66 | 4.65 | 0.02 |
| qwen-dotsonly-alphabet-scrambled | entropy_qlast | 11.24 | 11.56 | 11.36 | 10.38 | 7.01 | 0.03 |
| qwen-dotsonly-alphabet-scrambled | entropy_gen | 11.51 | 11.41 | 11.07 | 10.65 | 7.71 | 0.16 |
| qwen-dotsonly-alphabet-scrambled | norm_dots | 6.38 | 20.14 | 36.66 | 89.00 | 167.39 | 198.22 |
| qwen-dotsonly-alphabet-scrambled | norm_qlast | 5.09 | 22.16 | 36.10 | 82.45 | 163.02 | 216.73 |
| qwen-dotsonly-alphabet-scrambled | norm_gen | 5.03 | 17.73 | 31.75 | 83.59 | 232.19 | 353.68 |
