# What happens at dot positions (50 held-out items, k=140)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting | var frac: problem | 0.00 | 0.00 | 0.01 | 0.05 | 0.06 | 0.05 |
| qwen-dotsonly-counting | var frac: position | 1.00 | 0.98 | 0.82 | 0.63 | 0.53 | 0.57 |
| qwen-dotsonly-counting | cos same pos, other problems | 1.00 | 1.00 | 0.96 | 0.82 | 0.80 | 0.77 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting | dots_mean | base_value | -0.45 | 0.29 | 0.78 | 0.96 | 0.92 | 0.92 | L22 (0.96) |
| qwen-dotsonly-counting | dots_mean | bound_value | -0.52 | 0.22 | 0.83 | 0.94 | 0.92 | 0.93 | L20 (0.96) |
| qwen-dotsonly-counting | dots_mean | answer | -0.44 | 0.28 | 0.84 | 0.96 | 0.94 | 0.94 | L22 (0.97) |
| qwen-dotsonly-counting | dots_mean | answer_SHUFFLED | -0.99 | -0.68 | -0.61 | -0.36 | -0.27 | -0.30 | L10 (-0.10) |
| qwen-dotsonly-counting | q_last | base_value | -0.89 | -1.21 | 0.47 | 0.85 | 0.71 | 0.72 | L21 (0.86) |
| qwen-dotsonly-counting | q_last | bound_value | -0.84 | -1.28 | 0.56 | 0.88 | 0.80 | 0.82 | L21 (0.89) |
| qwen-dotsonly-counting | q_last | answer | -0.72 | -1.07 | 0.60 | 0.88 | 0.81 | 0.82 | L21 (0.90) |
| qwen-dotsonly-counting | q_last | answer_SHUFFLED | -0.79 | -0.74 | -0.41 | -0.91 | -0.36 | -0.40 | L15 (-0.33) |
| qwen-dotsonly-counting | cue | base_value | -0.76 | -0.54 | 0.68 | 0.98 | 0.94 | 0.94 | L19 (0.98) |
| qwen-dotsonly-counting | cue | bound_value | -0.99 | -0.48 | 0.75 | 0.97 | 0.93 | 0.93 | L19 (0.98) |
| qwen-dotsonly-counting | cue | answer | -0.78 | -0.34 | 0.77 | 0.97 | 0.95 | 0.95 | L19 (0.98) |
| qwen-dotsonly-counting | cue | answer_SHUFFLED | -1.02 | -0.04 | -0.47 | -1.40 | -1.35 | -1.16 | L7 (-0.02) |
| qwen-dotsonly-counting | gen | base_value | -0.76 | 0.22 | 0.83 | 0.94 | 0.93 | 0.92 | L22 (0.96) |
| qwen-dotsonly-counting | gen | bound_value | -1.06 | 0.18 | 0.86 | 0.95 | 0.89 | 0.89 | L26 (0.96) |
| qwen-dotsonly-counting | gen | answer | -0.99 | 0.22 | 0.87 | 0.96 | 0.92 | 0.93 | L26 (0.97) |
| qwen-dotsonly-counting | gen | answer_SHUFFLED | -0.69 | -0.27 | -0.42 | -0.07 | -0.74 | -0.63 | L22 (0.07) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-dotsonly-counting

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.037 | 0.716 | 0.039 | 0.003 | 0.205 | 0.01 |
| 3 | cue | 0.011 | 0.811 | 0.118 | 0.021 | 0.039 |  |
| 3 | dots | 0.005 | 0.773 | 0.082 | 0.140 | 0.000 |  |
| 7 | gen | 0.050 | 0.692 | 0.022 | 0.001 | 0.235 | 0.01 |
| 7 | cue | 0.007 | 0.459 | 0.494 | 0.011 | 0.029 |  |
| 7 | dots | 0.011 | 0.557 | 0.229 | 0.203 | 0.000 |  |
| 11 | gen | 0.019 | 0.810 | 0.023 | 0.002 | 0.147 | 0.01 |
| 11 | cue | 0.019 | 0.230 | 0.638 | 0.049 | 0.064 |  |
| 11 | dots | 0.019 | 0.445 | 0.385 | 0.151 | 0.000 |  |
| 15 | gen | 0.034 | 0.770 | 0.030 | 0.015 | 0.150 | 0.06 |
| 15 | cue | 0.014 | 0.385 | 0.497 | 0.077 | 0.028 |  |
| 15 | dots | 0.015 | 0.643 | 0.247 | 0.096 | 0.000 |  |
| 19 | gen | 0.006 | 0.196 | 0.675 | 0.078 | 0.044 | 0.28 |
| 19 | cue | 0.003 | 0.210 | 0.718 | 0.067 | 0.002 |  |
| 19 | dots | 0.016 | 0.513 | 0.328 | 0.143 | 0.000 |  |
| 23 | gen | 0.019 | 0.229 | 0.348 | 0.260 | 0.145 | 0.49 |
| 23 | cue | 0.018 | 0.226 | 0.547 | 0.198 | 0.012 |  |
| 23 | dots | 0.020 | 0.476 | 0.266 | 0.239 | 0.000 |  |
| 27 | gen | 0.112 | 0.583 | 0.065 | 0.079 | 0.161 | 0.33 |
| 27 | cue | 0.102 | 0.654 | 0.127 | 0.107 | 0.011 |  |
| 27 | dots | 0.083 | 0.670 | 0.105 | 0.142 | 0.000 |  |
| 31 | gen | 0.011 | 0.480 | 0.024 | 0.028 | 0.456 | 0.10 |
| 31 | cue | 0.005 | 0.724 | 0.042 | 0.038 | 0.192 |  |
| 31 | dots | 0.023 | 0.542 | 0.070 | 0.364 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting | entropy_dots | 11.25 | 11.56 | 11.31 | 10.10 | 7.88 | 0.04 |
| qwen-dotsonly-counting | entropy_qlast | 11.23 | 11.55 | 11.36 | 10.42 | 6.30 | 0.03 |
| qwen-dotsonly-counting | entropy_gen | 11.51 | 11.42 | 11.05 | 10.70 | 7.57 | 0.17 |
| qwen-dotsonly-counting | norm_dots | 6.07 | 19.85 | 37.32 | 85.00 | 160.17 | 180.57 |
| qwen-dotsonly-counting | norm_qlast | 5.11 | 21.95 | 35.95 | 81.74 | 159.67 | 210.31 |
| qwen-dotsonly-counting | norm_gen | 5.03 | 17.76 | 31.96 | 83.43 | 231.87 | 351.79 |
