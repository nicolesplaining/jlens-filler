# Do dot fillers improve repeated squaring?

## Result

Across 100 matched problems, dots were correct on 5 and no-dots on 2 (5.0% versus 2.0%). The paired difference was +3.0 percentage points, with a 95% paired-bootstrap interval of [-2.0, +8.0] points. The exact McNemar p-value was 0.453.

This is directionally positive but not conclusive. Absolute accuracy is very low, and every nontrivial success occurs at T <= 4. There is no verified T=10 serial-computation success in the shortcut-controlled set.

## By dependency length

| T | Dots correct | No dots correct | Difference | Median target rank, dots | Median target rank, no dots |
|---:|---:|---:|---:|---:|---:|
| 1 | 3/10 | 2/10 | +10 pp | 2.0 | 4.5 |
| 2 | 0/10 | 0/10 | +0 pp | 111.5 | 100.0 |
| 3 | 1/10 | 0/10 | +10 pp | 89.5 | 138.0 |
| 4 | 1/10 | 0/10 | +10 pp | 98.0 | 92.5 |
| 5 | 0/10 | 0/10 | +0 pp | 103.0 | 93.5 |
| 6 | 0/10 | 0/10 | +0 pp | 54.5 | 96.0 |
| 7 | 0/10 | 0/10 | +0 pp | 151.0 | 161.0 |
| 8 | 0/10 | 0/10 | +0 pp | 179.0 | 237.5 |
| 9 | 0/10 | 0/10 | +0 pp | 71.5 | 105.0 |
| 10 | 0/10 | 0/10 | +0 pp | 152.0 | 225.0 |

## Paired diagnostics

- Dots-only correct: 5.
- No-dots-only correct: 2.
- Correct in both: 0.
- Incorrect in both: 93.
- Correct-token rank favored dots in 59 pairs, no-dots in 40, and tied in 1 (exact sign-test p=0.070).
- Median correct-token rank: 88.0 with dots versus 98.5 without.
- Mean correct-token log-probability difference: +0.076 nats; 95% interval [-0.052, +0.204].
- Mean reciprocal-rank difference: +0.029; 95% interval [-0.002, +0.063].

## Discordant generations

| Example | T | Expected | Dots | No dots |
|---|---:|---:|---:|---:|
| `repeated_squaring_n209_x24_t1` | 1 | 158 | 158 ✓ | 170 ✗ |
| `repeated_squaring_n391_x37_t1` | 1 | 196 | 196 ✓ | 202 ✗ |
| `repeated_squaring_n407_x30_t1` | 1 | 86 | 86 ✓ | 206 ✗ |
| `repeated_squaring_n473_x31_t1` | 1 | 15 | 31 ✗ | 15 ✓ |
| `repeated_squaring_n517_x34_t1` | 1 | 122 | 146 ✗ | 122 ✓ |
| `repeated_squaring_n209_x24_t3` | 3 | 80 | 80 ✓ | 144 ✗ |
| `repeated_squaring_n407_x30_t4` | 4 | 256 | 256 ✓ | 16 ✗ |

## Design and interpretation boundary

The final set contains ten independent small-semiprime base instances at each T from 1 through 10. Within every base, the first ten residues are distinct and none equals x_0. The initial N=299, x=35 base was excluded in full because x_10=x_0 made its apparent T=10 success copy-solvable; it was replaced by N=667, x=41.

This is a legacy prompt run: its system message says only “some filler tokens” and adds an extra-space rationale. It predates the exact Appendix A prompt match and should not be pooled with the paper-matched results.

The comparison follows the filler-paper-style convention already used in this repository: the filler condition mentions dots in the system message and places ten dots in every demonstration and target; the no-filler condition removes that clause and those dots throughout. It therefore measures the complete prompting condition, not a target-only insertion.

These small moduli make all target residues single tokenizer tokens and are appropriate for this readout pilot. They are not cryptographic-size instances, so the result should not be generalized to the benchmark's strong no-shortcut setting. All generations are greedy and non-thinking.
