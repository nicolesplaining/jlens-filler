# What happens at dot positions (50 held-out items, k=50)

## 1. Problem-independence of dot residuals

Fraction of dot-residual variance explained by *which problem* (vs which dot position), and mean cosine of the same dot position across different problems.

| Model | quantity | L0 | L15 | L31 | L46 | L59 | L61 |
|---|---|---:|---:|---:|---:|---:|---:|
| gemma-27b-it | var frac: problem | 0.02 | 0.00 | 0.01 | 0.02 | 0.01 | 0.01 |
| gemma-27b-it | var frac: position | 0.93 | 1.00 | 0.86 | 0.56 | 0.78 | 0.81 |
| gemma-27b-it | cos same pos, other problems | 1.00 | 1.00 | 0.99 | 0.97 | 0.97 | 0.94 |

## 2. Linear probes (ridge, 5-fold CV R², item-level folds)

Predicting stage values from residuals. `dots_mean` = mean over the 50 dot residuals. `answer_SHUFFLED` = shuffled-label control.

| Model | position | target | L0 | L15 | L31 | L46 | L59 | L61 | best layer (R²) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| gemma-27b-it | dots_mean | base_value | -0.78 | -0.26 | 0.71 | 0.81 | 0.79 | 0.78 | L38 (0.85) |
| gemma-27b-it | dots_mean | bound_value | -0.60 | -0.12 | 0.67 | 0.76 | 0.79 | 0.79 | L55 (0.83) |
| gemma-27b-it | dots_mean | answer | -0.62 | -0.07 | 0.69 | 0.77 | 0.79 | 0.78 | L55 (0.81) |
| gemma-27b-it | dots_mean | answer_SHUFFLED | -0.64 | -0.29 | -0.08 | -0.31 | -0.17 | -0.22 | L31 (-0.08) |
| gemma-27b-it | q_last | base_value | -0.41 | -0.52 | 0.55 | 0.86 | 0.81 | 0.81 | L51 (0.89) |
| gemma-27b-it | q_last | bound_value | -0.37 | -0.38 | 0.60 | 0.86 | 0.82 | 0.81 | L38 (0.89) |
| gemma-27b-it | q_last | answer | -0.36 | -0.29 | 0.63 | 0.86 | 0.83 | 0.82 | L38 (0.90) |
| gemma-27b-it | q_last | answer_SHUFFLED | -0.52 | -0.40 | -0.68 | -0.22 | -0.17 | -0.22 | L2 (-0.06) |
| gemma-27b-it | cue | base_value | -0.44 | -0.37 | 0.76 | 0.92 | 0.88 | 0.88 | L47 (0.93) |
| gemma-27b-it | cue | bound_value | -0.29 | -0.11 | 0.76 | 0.90 | 0.87 | 0.86 | L44 (0.91) |
| gemma-27b-it | cue | answer | -0.29 | -0.06 | 0.79 | 0.89 | 0.87 | 0.87 | L44 (0.90) |
| gemma-27b-it | cue | answer_SHUFFLED | -0.36 | -0.87 | -0.28 | -0.72 | -0.72 | -0.69 | L23 (-0.01) |
| gemma-27b-it | gen | base_value | -0.45 | -0.15 | 0.74 | 0.92 | 0.87 | 0.86 | L47 (0.95) |
| gemma-27b-it | gen | bound_value | -0.42 | 0.08 | 0.76 | 0.91 | 0.86 | 0.86 | L47 (0.93) |
| gemma-27b-it | gen | answer | -0.53 | 0.12 | 0.79 | 0.92 | 0.88 | 0.87 | L47 (0.94) |
| gemma-27b-it | gen | answer_SHUFFLED | 0.15 | -0.14 | -0.28 | -0.52 | 0.02 | -0.02 | L6 (0.21) |

## 3. Attention (full-attention blocks only)

Mean attention mass by key region. Regions: bos, prefix (system + demonstrations), problem (target definitions + question), dots, template (answer cue and assistant header).

### gemma-27b-it

| layer | query | bos | prefix | problem | dots | template | max head→dots |
|---:|---|---:|---:|---:|---:|---:|---:|
| 5 | gen | 0.000 | 0.000 | 0.927 | 0.038 | 0.035 | 0.74 |
| 5 | cue | 0.000 | 0.000 | 0.912 | 0.059 | 0.029 |  |
| 5 | dots | 0.000 | 0.000 | 0.922 | 0.078 | 0.000 |  |
| 11 | gen | 0.000 | 0.000 | 0.964 | 0.000 | 0.036 | 0.01 |
| 11 | cue | 0.000 | 0.000 | 0.965 | 0.003 | 0.032 |  |
| 11 | dots | 0.000 | 0.000 | 0.964 | 0.036 | 0.000 |  |
| 17 | gen | 0.000 | 0.000 | 0.936 | 0.004 | 0.060 | 0.06 |
| 17 | cue | 0.000 | 0.000 | 0.923 | 0.004 | 0.073 |  |
| 17 | dots | 0.000 | 0.000 | 0.926 | 0.074 | 0.000 |  |
| 23 | gen | 0.000 | 0.000 | 0.935 | 0.005 | 0.060 | 0.02 |
| 23 | cue | 0.000 | 0.000 | 0.963 | 0.008 | 0.029 |  |
| 23 | dots | 0.000 | 0.000 | 0.933 | 0.067 | 0.000 |  |
| 29 | gen | 0.000 | 0.000 | 0.946 | 0.026 | 0.028 | 0.11 |
| 29 | cue | 0.000 | 0.000 | 0.957 | 0.031 | 0.012 |  |
| 29 | dots | 0.000 | 0.000 | 0.978 | 0.022 | 0.000 |  |
| 35 | gen | 0.000 | 0.000 | 0.928 | 0.030 | 0.043 | 0.13 |
| 35 | cue | 0.000 | 0.000 | 0.950 | 0.029 | 0.020 |  |
| 35 | dots | 0.000 | 0.000 | 0.958 | 0.042 | 0.000 |  |
| 41 | gen | 0.000 | 0.000 | 0.948 | 0.023 | 0.028 | 0.17 |
| 41 | cue | 0.000 | 0.000 | 0.964 | 0.026 | 0.010 |  |
| 41 | dots | 0.000 | 0.000 | 0.972 | 0.028 | 0.000 |  |
| 47 | gen | 0.000 | 0.000 | 0.943 | 0.030 | 0.027 | 0.18 |
| 47 | cue | 0.000 | 0.000 | 0.969 | 0.025 | 0.005 |  |
| 47 | dots | 0.000 | 0.000 | 0.990 | 0.010 | 0.000 |  |
| 53 | gen | 0.000 | 0.000 | 0.981 | 0.009 | 0.011 | 0.05 |
| 53 | cue | 0.000 | 0.000 | 0.989 | 0.008 | 0.003 |  |
| 53 | dots | 0.000 | 0.000 | 0.988 | 0.012 | 0.000 |  |
| 59 | gen | 0.000 | 0.000 | 0.936 | 0.002 | 0.062 | 0.01 |
| 59 | cue | 0.000 | 0.000 | 0.942 | 0.010 | 0.048 |  |
| 59 | dots | 0.000 | 0.000 | 0.903 | 0.097 | 0.000 |  |

## 4. Processing trajectories

Mean logit-lens entropy (nats) and residual norm by layer.

| Model | quantity | L0 | L15 | L31 | L46 | L59 | L61 |
|---|---|---:|---:|---:|---:|---:|---:|
| gemma-27b-it | entropy_dots | 0.01 | 2.35 | 10.43 | 4.17 | 0.02 | 0.00 |
| gemma-27b-it | entropy_qlast | 0.00 | 0.44 | 9.53 | 3.26 | 0.02 | 0.00 |
| gemma-27b-it | entropy_gen | 0.00 | 2.09 | 4.88 | 1.55 | 1.00 | 0.09 |
| gemma-27b-it | norm_dots | 727.38 | 3023.99 | 32013.84 | 45111.08 | 108764.87 | 99319.06 |
| gemma-27b-it | norm_qlast | 616.18 | 2514.16 | 38697.56 | 49521.14 | 110383.63 | 111593.15 |
| gemma-27b-it | norm_gen | 1035.84 | 3760.34 | 38763.38 | 54824.02 | 144060.45 | 93906.51 |
