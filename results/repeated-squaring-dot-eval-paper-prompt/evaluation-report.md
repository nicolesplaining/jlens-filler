# Do dot fillers improve repeated squaring?

## Result

Across 100 matched problems, dots were correct on 7 and no-dots on 2 (7.0% versus 2.0%). The paired difference was +5.0 percentage points, with a 95% paired-bootstrap interval of [+1.0, +10.0] points. The exact McNemar p-value was 0.062.

This is directionally positive but not conclusive. Absolute accuracy is very low, and every nontrivial success occurs at T <= 4. There is no verified T=10 serial-computation success in the shortcut-controlled set.

## By dependency length

| T | Dots correct | No dots correct | Difference | Median target rank, dots | Median target rank, no dots |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/10 | 2/10 | +30 pp | 1.5 | 4.5 |
| 2 | 0/10 | 0/10 | +0 pp | 76.5 | 100.0 |
| 3 | 1/10 | 0/10 | +10 pp | 130.5 | 138.0 |
| 4 | 1/10 | 0/10 | +10 pp | 87.0 | 92.5 |
| 5 | 0/10 | 0/10 | +0 pp | 129.0 | 93.5 |
| 6 | 0/10 | 0/10 | +0 pp | 60.5 | 96.0 |
| 7 | 0/10 | 0/10 | +0 pp | 148.5 | 161.0 |
| 8 | 0/10 | 0/10 | +0 pp | 131.0 | 237.5 |
| 9 | 0/10 | 0/10 | +0 pp | 73.0 | 105.0 |
| 10 | 0/10 | 0/10 | +0 pp | 187.5 | 225.0 |

## Paired diagnostics

- Dots-only correct: 5.
- No-dots-only correct: 0.
- Correct in both: 2.
- Incorrect in both: 93.
- Correct-token rank favored dots in 62 pairs, no-dots in 35, and tied in 3 (exact sign-test p=0.008).
- Median correct-token rank: 88.0 with dots versus 98.5 without.
- Mean correct-token log-probability difference: +0.077 nats; 95% interval [-0.084, +0.229].
- Mean reciprocal-rank difference: +0.038; 95% interval [+0.011, +0.069].

## Discordant generations

| Example | T | Expected | Dots | No dots |
|---|---:|---:|---:|---:|
| `repeated_squaring_n209_x24_t1` | 1 | 158 | 158 ✓ | 170 ✗ |
| `repeated_squaring_n391_x37_t1` | 1 | 196 | 196 ✓ | 202 ✗ |
| `repeated_squaring_n611_x36_t1` | 1 | 74 | 74 ✓ | 158 ✗ |
| `repeated_squaring_n209_x24_t3` | 3 | 80 | 80 ✓ | 144 ✗ |
| `repeated_squaring_n407_x30_t4` | 4 | 256 | 256 ✓ | 16 ✗ |

## Design and interpretation boundary

The final set contains ten independent small-semiprime base instances at each T from 1 through 10. Within every base, the first ten residues are distinct and none equals x_0. The initial N=299, x=35 base was excluded in full because x_10=x_0 made its apparent T=10 success copy-solvable; it was replaced by N=667, x=41.

The dots system instruction uses the Appendix A wording for k=10 exactly: “After the question, there will be 10 filler tokens (a sequence of dots) before you answer.” Ten spaced periods appear after `Filler:` in every demonstration and target.

The comparison follows the filler-paper-style convention already used in this repository: the filler condition mentions dots in the system message and places ten dots in every demonstration and target; the no-filler condition removes that clause and those dots throughout. It therefore measures the complete prompting condition, not a target-only insertion.

These small moduli make all target residues single tokenizer tokens and are appropriate for this readout pilot. They are not cryptographic-size instances, so the result should not be generalized to the benchmark's strong no-shortcut setting. All generations are greedy and non-thinking.
