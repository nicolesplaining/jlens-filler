# What happens at dot positions (50 held-out items, k=50)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet-scrambled | var frac: problem | 0.00 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 |
| qwen-base-alphabet-scrambled | var frac: position | 1.00 | 0.87 | 0.53 | 0.42 | 0.42 | 0.44 |
| qwen-base-alphabet-scrambled | cos same pos, other problems | 1.00 | 0.97 | 0.82 | 0.66 | 0.72 | 0.62 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet-scrambled | dots_mean | base_value | -1.60 | 0.02 | -0.11 | 0.07 | 0.11 | -0.00 | L27 (0.20) |
| qwen-base-alphabet-scrambled | dots_mean | bound_value | -1.50 | -0.04 | 0.01 | 0.14 | 0.18 | 0.07 | L27 (0.27) |
| qwen-base-alphabet-scrambled | dots_mean | answer | -1.36 | -0.03 | 0.02 | 0.16 | 0.17 | 0.06 | L27 (0.25) |
| qwen-base-alphabet-scrambled | dots_mean | answer_SHUFFLED | -0.89 | -0.82 | -0.48 | -0.26 | -0.21 | -0.25 | L25 (-0.15) |
| qwen-base-alphabet-scrambled | q_last | base_value | -1.19 | -0.69 | -0.59 | -0.06 | -0.13 | -0.37 | L18 (0.02) |
| qwen-base-alphabet-scrambled | q_last | bound_value | -1.19 | -0.82 | -0.39 | 0.11 | 0.05 | -0.12 | L18 (0.22) |
| qwen-base-alphabet-scrambled | q_last | answer | -1.04 | -0.68 | -0.27 | 0.19 | 0.12 | -0.03 | L18 (0.30) |
| qwen-base-alphabet-scrambled | q_last | answer_SHUFFLED | -0.74 | -1.36 | -1.16 | -1.15 | -0.95 | -0.86 | L1 (-0.51) |
| qwen-base-alphabet-scrambled | cue | base_value | -0.93 | -0.54 | -0.17 | 0.69 | 0.50 | 0.50 | L24 (0.69) |
| qwen-base-alphabet-scrambled | cue | bound_value | -0.86 | -0.51 | 0.09 | 0.71 | 0.54 | 0.55 | L24 (0.71) |
| qwen-base-alphabet-scrambled | cue | answer | -0.77 | -0.39 | 0.17 | 0.79 | 0.61 | 0.60 | L24 (0.79) |
| qwen-base-alphabet-scrambled | cue | answer_SHUFFLED | -1.04 | -0.90 | -0.69 | -1.44 | -1.00 | -1.05 | L2 (-0.10) |
| qwen-base-alphabet-scrambled | gen | base_value | -0.72 | -0.36 | 0.07 | 0.59 | 0.57 | 0.65 | L31 (0.65) |
| qwen-base-alphabet-scrambled | gen | bound_value | -0.97 | -0.27 | 0.11 | 0.69 | 0.71 | 0.72 | L31 (0.72) |
| qwen-base-alphabet-scrambled | gen | answer | -0.94 | -0.23 | 0.22 | 0.74 | 0.73 | 0.76 | L31 (0.76) |
| qwen-base-alphabet-scrambled | gen | answer_SHUFFLED | -1.02 | -0.44 | -0.46 | -0.49 | -0.46 | -0.30 | L19 (-0.21) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-base-alphabet-scrambled

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.031 | 0.690 | 0.053 | 0.001 | 0.225 | 0.01 |
| 3 | cue | 0.008 | 0.749 | 0.191 | 0.019 | 0.033 |  |
| 3 | dots | 0.004 | 0.765 | 0.143 | 0.088 | 0.000 |  |
| 7 | gen | 0.050 | 0.722 | 0.011 | 0.001 | 0.217 | 0.01 |
| 7 | cue | 0.004 | 0.542 | 0.404 | 0.020 | 0.030 |  |
| 7 | dots | 0.009 | 0.722 | 0.154 | 0.114 | 0.000 |  |
| 11 | gen | 0.026 | 0.830 | 0.008 | 0.003 | 0.133 | 0.01 |
| 11 | cue | 0.013 | 0.298 | 0.637 | 0.021 | 0.031 |  |
| 11 | dots | 0.016 | 0.774 | 0.148 | 0.062 | 0.000 |  |
| 15 | gen | 0.055 | 0.795 | 0.010 | 0.008 | 0.132 | 0.03 |
| 15 | cue | 0.025 | 0.421 | 0.450 | 0.076 | 0.029 |  |
| 15 | dots | 0.020 | 0.807 | 0.126 | 0.047 | 0.000 |  |
| 19 | gen | 0.030 | 0.598 | 0.189 | 0.039 | 0.144 | 0.11 |
| 19 | cue | 0.012 | 0.297 | 0.604 | 0.073 | 0.014 |  |
| 19 | dots | 0.025 | 0.746 | 0.148 | 0.080 | 0.000 |  |
| 23 | gen | 0.053 | 0.564 | 0.177 | 0.017 | 0.189 | 0.05 |
| 23 | cue | 0.016 | 0.264 | 0.482 | 0.127 | 0.112 |  |
| 23 | dots | 0.024 | 0.762 | 0.133 | 0.081 | 0.000 |  |
| 27 | gen | 0.097 | 0.497 | 0.051 | 0.006 | 0.349 | 0.02 |
| 27 | cue | 0.127 | 0.677 | 0.090 | 0.025 | 0.081 |  |
| 27 | dots | 0.075 | 0.789 | 0.090 | 0.046 | 0.000 |  |
| 31 | gen | 0.028 | 0.429 | 0.019 | 0.004 | 0.521 | 0.02 |
| 31 | cue | 0.022 | 0.707 | 0.040 | 0.008 | 0.223 |  |
| 31 | dots | 0.027 | 0.704 | 0.056 | 0.212 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet-scrambled | entropy_dots | 11.20 | 11.57 | 11.17 | 8.67 | 3.38 | 0.44 |
| qwen-base-alphabet-scrambled | entropy_qlast | 11.21 | 11.60 | 11.44 | 8.89 | 3.73 | 0.41 |
| qwen-base-alphabet-scrambled | entropy_gen | 11.50 | 11.16 | 10.63 | 10.88 | 7.01 | 1.34 |
| qwen-base-alphabet-scrambled | norm_dots | 6.37 | 19.14 | 35.20 | 82.77 | 153.00 | 184.99 |
| qwen-base-alphabet-scrambled | norm_qlast | 5.09 | 17.88 | 34.38 | 92.51 | 158.22 | 214.57 |
| qwen-base-alphabet-scrambled | norm_gen | 5.00 | 15.08 | 27.39 | 73.40 | 145.27 | 248.21 |
