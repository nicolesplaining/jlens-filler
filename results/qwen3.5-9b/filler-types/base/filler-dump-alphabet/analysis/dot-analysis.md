# What happens at dot positions (50 held-out items, k=50)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet | var frac: problem | 0.00 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 |
| qwen-base-alphabet | var frac: position | 1.00 | 0.85 | 0.50 | 0.43 | 0.44 | 0.47 |
| qwen-base-alphabet | cos same pos, other problems | 1.00 | 0.98 | 0.85 | 0.75 | 0.80 | 0.68 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet | dots_mean | base_value | -1.51 | 0.10 | 0.12 | 0.24 | 0.19 | 0.11 | L27 (0.30) |
| qwen-base-alphabet | dots_mean | bound_value | -1.42 | -0.03 | 0.17 | 0.29 | 0.27 | 0.24 | L27 (0.38) |
| qwen-base-alphabet | dots_mean | answer | -1.30 | 0.01 | 0.18 | 0.31 | 0.26 | 0.22 | L27 (0.38) |
| qwen-base-alphabet | dots_mean | answer_SHUFFLED | -0.96 | -0.55 | -0.08 | -0.24 | -0.11 | -0.15 | L18 (0.03) |
| qwen-base-alphabet | q_last | base_value | -1.11 | -0.64 | -0.37 | -0.04 | -0.05 | -0.28 | L18 (0.09) |
| qwen-base-alphabet | q_last | bound_value | -1.07 | -0.83 | -0.23 | 0.09 | 0.11 | -0.04 | L18 (0.26) |
| qwen-base-alphabet | q_last | answer | -0.95 | -0.70 | -0.11 | 0.19 | 0.19 | 0.05 | L18 (0.34) |
| qwen-base-alphabet | q_last | answer_SHUFFLED | -0.82 | -1.13 | -1.29 | -1.21 | -0.78 | -0.75 | L1 (-0.51) |
| qwen-base-alphabet | cue | base_value | -0.99 | -0.58 | 0.04 | 0.72 | 0.53 | 0.55 | L23 (0.73) |
| qwen-base-alphabet | cue | bound_value | -0.99 | -0.61 | 0.15 | 0.78 | 0.58 | 0.58 | L23 (0.79) |
| qwen-base-alphabet | cue | answer | -0.89 | -0.48 | 0.24 | 0.80 | 0.63 | 0.64 | L23 (0.81) |
| qwen-base-alphabet | cue | answer_SHUFFLED | -0.91 | -0.72 | -0.43 | -1.38 | -1.50 | -1.34 | L2 (0.12) |
| qwen-base-alphabet | gen | base_value | -0.78 | 0.10 | 0.29 | 0.58 | 0.67 | 0.64 | L28 (0.68) |
| qwen-base-alphabet | gen | bound_value | -0.96 | -0.05 | 0.34 | 0.71 | 0.71 | 0.71 | L28 (0.73) |
| qwen-base-alphabet | gen | answer | -0.93 | -0.03 | 0.42 | 0.76 | 0.76 | 0.75 | L28 (0.77) |
| qwen-base-alphabet | gen | answer_SHUFFLED | -0.99 | -0.43 | -0.60 | -0.25 | -0.53 | -0.35 | L22 (-0.20) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-base-alphabet

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.030 | 0.690 | 0.051 | 0.001 | 0.228 | 0.01 |
| 3 | cue | 0.008 | 0.749 | 0.189 | 0.020 | 0.034 |  |
| 3 | dots | 0.005 | 0.679 | 0.146 | 0.170 | 0.000 |  |
| 7 | gen | 0.050 | 0.722 | 0.011 | 0.001 | 0.215 | 0.01 |
| 7 | cue | 0.005 | 0.546 | 0.398 | 0.032 | 0.020 |  |
| 7 | dots | 0.006 | 0.706 | 0.188 | 0.099 | 0.000 |  |
| 11 | gen | 0.027 | 0.829 | 0.010 | 0.002 | 0.133 | 0.00 |
| 11 | cue | 0.024 | 0.329 | 0.563 | 0.031 | 0.053 |  |
| 11 | dots | 0.015 | 0.788 | 0.146 | 0.052 | 0.000 |  |
| 15 | gen | 0.057 | 0.793 | 0.009 | 0.007 | 0.133 | 0.03 |
| 15 | cue | 0.027 | 0.452 | 0.409 | 0.066 | 0.045 |  |
| 15 | dots | 0.021 | 0.794 | 0.138 | 0.047 | 0.000 |  |
| 19 | gen | 0.029 | 0.570 | 0.188 | 0.044 | 0.168 | 0.12 |
| 19 | cue | 0.009 | 0.293 | 0.633 | 0.053 | 0.012 |  |
| 19 | dots | 0.027 | 0.705 | 0.177 | 0.092 | 0.000 |  |
| 23 | gen | 0.062 | 0.555 | 0.148 | 0.022 | 0.213 | 0.05 |
| 23 | cue | 0.015 | 0.248 | 0.503 | 0.150 | 0.085 |  |
| 23 | dots | 0.028 | 0.707 | 0.167 | 0.098 | 0.000 |  |
| 27 | gen | 0.100 | 0.476 | 0.045 | 0.015 | 0.365 | 0.03 |
| 27 | cue | 0.137 | 0.662 | 0.091 | 0.045 | 0.064 |  |
| 27 | dots | 0.090 | 0.749 | 0.108 | 0.053 | 0.000 |  |
| 31 | gen | 0.030 | 0.415 | 0.017 | 0.007 | 0.532 | 0.02 |
| 31 | cue | 0.021 | 0.719 | 0.038 | 0.010 | 0.211 |  |
| 31 | dots | 0.029 | 0.688 | 0.069 | 0.215 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-base-alphabet | entropy_dots | 11.19 | 11.54 | 11.18 | 8.60 | 3.79 | 0.41 |
| qwen-base-alphabet | entropy_qlast | 11.21 | 11.60 | 11.44 | 9.49 | 3.68 | 0.30 |
| qwen-base-alphabet | entropy_gen | 11.50 | 11.17 | 10.63 | 10.89 | 7.42 | 1.31 |
| qwen-base-alphabet | norm_dots | 6.42 | 18.40 | 34.10 | 81.20 | 152.17 | 182.65 |
| qwen-base-alphabet | norm_qlast | 5.09 | 17.79 | 34.23 | 92.92 | 157.67 | 211.76 |
| qwen-base-alphabet | norm_gen | 4.98 | 15.11 | 27.08 | 74.55 | 147.05 | 252.87 |
