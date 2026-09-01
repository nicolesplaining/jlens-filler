# Two-fact addition dot-length sweep

## Result

The best observed condition was k=100: 45/100 correct (45.0%), versus 41/100 (41.0%) without filler. This is an exploratory seven-condition calibration sweep; individual p-values are uncorrected.

| Dots k | Correct | Accuracy | Difference vs k=0 | 95% paired CI | McNemar p | Median target rank | MRR | Max prompt tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 41/100 | 41.0% | - | - | - | 2.0 | 0.5344 | 191 |
| 1 | 38/100 | 38.0% | -3.0 pp | [-10.0, +4.0] pp | 0.6072 | 2.0 | 0.5132 | 236 |
| 5 | 40/100 | 40.0% | -1.0 pp | [-9.0, +7.0] pp | 1.0000 | 3.0 | 0.5092 | 260 |
| 10 | 42/100 | 42.0% | +1.0 pp | [-5.0, +8.0] pp | 1.0000 | 2.0 | 0.5467 | 290 |
| 25 | 40/100 | 40.0% | -1.0 pp | [-9.0, +7.0] pp | 1.0000 | 2.0 | 0.5343 | 380 |
| 50 | 44/100 | 44.0% | +3.0 pp | [-5.0, +12.0] pp | 0.6476 | 2.0 | 0.5433 | 530 |
| 100 | 45/100 | 45.0% | +4.0 pp | [-5.0, +13.0] pp | 0.5235 | 2.0 | 0.5940 | 830 |

## Qualitative J-Lens candidates at the best k

- Dots-only correct: 13 examples; `two_fact_0007`, `two_fact_0016`, `two_fact_0027`, `two_fact_0029`, `two_fact_0046`, `two_fact_0053`, `two_fact_0056`, `two_fact_0082`, `two_fact_0088`, `two_fact_0091`.
- Correct in both: 32 examples; `two_fact_0006`, `two_fact_0010`, `two_fact_0015`, `two_fact_0018`, `two_fact_0020`, `two_fact_0021`, `two_fact_0024`, `two_fact_0031`, `two_fact_0038`, `two_fact_0042`.
- Baseline-only correct: 9 examples; `two_fact_0000`, `two_fact_0002`, `two_fact_0032`, `two_fact_0036`, `two_fact_0037`, `two_fact_0039`, `two_fact_0051`, `two_fact_0055`, `two_fact_0072`.

## Validation and interpretation boundary

The five demonstrations and first 100 target pairs are copied from the released `data/2fact_addition_dataset.json` at commit `4ba4c75d5d9f04248749ec46b8bed8661b746715`. Prompt construction uses the paper PDF's exact-count filler sentence, as requested, rather than the different wording currently present on repository main.

Every k uses identical examples and greedy non-thinking decoding. The no-filler prompt is evaluated once per example, and target filler alignment is asserted at every positive length. This task is a calibration benchmark: it has known retrieved intermediates and a simple sum, but it does not test a growing serial dependency chain like repeated squaring.
