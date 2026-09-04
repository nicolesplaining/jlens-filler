# What happens at dot positions (50 held-out items, k=140)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting-scrambled | var frac: problem | 0.00 | 0.00 | 0.01 | 0.03 | 0.03 | 0.02 |
| qwen-dotsonly-counting-scrambled | var frac: position | 1.00 | 0.98 | 0.87 | 0.71 | 0.67 | 0.71 |
| qwen-dotsonly-counting-scrambled | cos same pos, other problems | 1.00 | 1.00 | 0.98 | 0.92 | 0.91 | 0.89 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L8 | L16 | L24 | L29 | L31 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting-scrambled | dots_mean | base_value | -0.43 | 0.19 | 0.81 | 0.97 | 0.92 | 0.91 | L22 (0.97) |
| qwen-dotsonly-counting-scrambled | dots_mean | bound_value | -0.50 | 0.04 | 0.85 | 0.96 | 0.93 | 0.91 | L20 (0.97) |
| qwen-dotsonly-counting-scrambled | dots_mean | answer | -0.43 | 0.12 | 0.86 | 0.97 | 0.94 | 0.93 | L21 (0.98) |
| qwen-dotsonly-counting-scrambled | dots_mean | answer_SHUFFLED | -0.86 | -0.55 | -0.26 | -0.47 | -0.26 | -0.25 | L10 (-0.13) |
| qwen-dotsonly-counting-scrambled | q_last | base_value | -0.89 | -1.36 | 0.55 | 0.88 | 0.77 | 0.76 | L21 (0.88) |
| qwen-dotsonly-counting-scrambled | q_last | bound_value | -0.89 | -1.40 | 0.63 | 0.89 | 0.83 | 0.83 | L21 (0.90) |
| qwen-dotsonly-counting-scrambled | q_last | answer | -0.75 | -1.17 | 0.66 | 0.90 | 0.84 | 0.84 | L21 (0.91) |
| qwen-dotsonly-counting-scrambled | q_last | answer_SHUFFLED | -0.82 | -0.92 | -0.40 | -0.85 | -0.27 | -0.29 | L15 (-0.25) |
| qwen-dotsonly-counting-scrambled | cue | base_value | -0.75 | -0.68 | 0.70 | 0.97 | 0.94 | 0.94 | L20 (0.98) |
| qwen-dotsonly-counting-scrambled | cue | bound_value | -0.92 | -0.67 | 0.77 | 0.96 | 0.93 | 0.94 | L19 (0.98) |
| qwen-dotsonly-counting-scrambled | cue | answer | -0.74 | -0.51 | 0.78 | 0.97 | 0.95 | 0.95 | L19 (0.98) |
| qwen-dotsonly-counting-scrambled | cue | answer_SHUFFLED | -1.33 | -0.12 | -0.61 | -1.34 | -1.10 | -1.09 | L8 (-0.12) |
| qwen-dotsonly-counting-scrambled | gen | base_value | -0.80 | 0.11 | 0.84 | 0.94 | 0.93 | 0.92 | L22 (0.96) |
| qwen-dotsonly-counting-scrambled | gen | bound_value | -1.17 | 0.02 | 0.86 | 0.95 | 0.89 | 0.89 | L22 (0.96) |
| qwen-dotsonly-counting-scrambled | gen | answer | -1.03 | 0.07 | 0.87 | 0.96 | 0.92 | 0.93 | L22 (0.97) |
| qwen-dotsonly-counting-scrambled | gen | answer_SHUFFLED | -0.79 | -0.44 | -0.40 | -0.06 | -0.86 | -0.71 | L19 (0.17) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### qwen-dotsonly-counting-scrambled

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | gen | 0.037 | 0.719 | 0.041 | 0.003 | 0.201 | 0.01 |
| 3 | cue | 0.011 | 0.819 | 0.113 | 0.022 | 0.035 |  |
| 3 | dots | 0.003 | 0.811 | 0.060 | 0.126 | 0.000 |  |
| 7 | gen | 0.049 | 0.690 | 0.022 | 0.001 | 0.237 | 0.01 |
| 7 | cue | 0.006 | 0.484 | 0.460 | 0.012 | 0.038 |  |
| 7 | dots | 0.008 | 0.652 | 0.144 | 0.196 | 0.000 |  |
| 11 | gen | 0.020 | 0.811 | 0.021 | 0.004 | 0.145 | 0.01 |
| 11 | cue | 0.015 | 0.235 | 0.662 | 0.028 | 0.059 |  |
| 11 | dots | 0.012 | 0.577 | 0.249 | 0.161 | 0.000 |  |
| 15 | gen | 0.036 | 0.772 | 0.029 | 0.014 | 0.150 | 0.07 |
| 15 | cue | 0.013 | 0.376 | 0.512 | 0.078 | 0.021 |  |
| 15 | dots | 0.011 | 0.771 | 0.153 | 0.064 | 0.000 |  |
| 19 | gen | 0.006 | 0.205 | 0.655 | 0.094 | 0.040 | 0.36 |
| 19 | cue | 0.003 | 0.218 | 0.705 | 0.073 | 0.002 |  |
| 19 | dots | 0.011 | 0.634 | 0.211 | 0.145 | 0.000 |  |
| 23 | gen | 0.019 | 0.262 | 0.316 | 0.281 | 0.123 | 0.50 |
| 23 | cue | 0.015 | 0.232 | 0.527 | 0.218 | 0.008 |  |
| 23 | dots | 0.022 | 0.657 | 0.150 | 0.171 | 0.000 |  |
| 27 | gen | 0.105 | 0.619 | 0.056 | 0.078 | 0.142 | 0.21 |
| 27 | cue | 0.089 | 0.672 | 0.115 | 0.115 | 0.009 |  |
| 27 | dots | 0.062 | 0.762 | 0.060 | 0.116 | 0.000 |  |
| 31 | gen | 0.010 | 0.497 | 0.022 | 0.030 | 0.440 | 0.09 |
| 31 | cue | 0.004 | 0.737 | 0.041 | 0.032 | 0.186 |  |
| 31 | dots | 0.017 | 0.660 | 0.037 | 0.285 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L8 | L16 | L24 | L29 | L31 |
|---|---|---:|---:|---:|---:|---:|---:|
| qwen-dotsonly-counting-scrambled | entropy_dots | 11.24 | 11.59 | 11.33 | 10.87 | 5.05 | 0.01 |
| qwen-dotsonly-counting-scrambled | entropy_qlast | 11.23 | 11.55 | 11.36 | 10.38 | 6.79 | 0.03 |
| qwen-dotsonly-counting-scrambled | entropy_gen | 11.51 | 11.41 | 11.04 | 10.66 | 7.49 | 0.19 |
| qwen-dotsonly-counting-scrambled | norm_dots | 6.04 | 19.98 | 37.89 | 85.37 | 159.56 | 190.91 |
| qwen-dotsonly-counting-scrambled | norm_qlast | 5.11 | 22.11 | 36.11 | 82.04 | 160.71 | 211.40 |
| qwen-dotsonly-counting-scrambled | norm_gen | 5.03 | 17.73 | 31.94 | 83.61 | 234.78 | 357.13 |
