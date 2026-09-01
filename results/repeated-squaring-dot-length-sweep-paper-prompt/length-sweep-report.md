# Repeated-squaring dot-length sweep

## Result

The best observed condition was k=3: 7/100 correct (7.0%), versus 2/100 (2.0%) without filler. This is an exploratory eight-condition sweep; individual p-values are uncorrected and should not be treated as confirmatory.

| Dots k | Correct | Accuracy | Difference vs k=0 | 95% paired CI | McNemar p | Median target rank | MRR | Max prompt tokens |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2/100 | 2.0% | - | - | - | 99.5 | 0.0731 | 356 |
| 1 | 3/100 | 3.0% | +1.0 pp | [-3.0, +5.0] pp | 1.0000 | 99.5 | 0.0895 | 401 |
| 3 | 7/100 | 7.0% | +5.0 pp | [+1.0, +10.0] pp | 0.0625 | 88.5 | 0.1110 | 413 |
| 5 | 3/100 | 3.0% | +1.0 pp | [-3.0, +6.0] pp | 1.0000 | 82.5 | 0.0858 | 425 |
| 10 | 7/100 | 7.0% | +5.0 pp | [+1.0, +10.0] pp | 0.0625 | 89.0 | 0.1111 | 455 |
| 25 | 5/100 | 5.0% | +3.0 pp | [-2.0, +8.0] pp | 0.4531 | 88.0 | 0.0969 | 545 |
| 50 | 5/100 | 5.0% | +3.0 pp | [-1.0, +8.0] pp | 0.3750 | 93.5 | 0.0967 | 695 |
| 100 | 3/100 | 3.0% | +1.0 pp | [-2.0, +5.0] pp | 1.0000 | 77.0 | 0.0846 | 995 |

## Correct answers by dependency length

Each cell is correct/10. Treat isolated changes cautiously because each T row contains only ten examples.

| T | k=0 | k=1 | k=3 | k=5 | k=10 | k=25 | k=50 | k=100 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2/10 | 2/10 | 5/10 | 1/10 | 5/10 | 3/10 | 2/10 | 1/10 |
| 2 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| 3 | 0/10 | 0/10 | 1/10 | 1/10 | 1/10 | 1/10 | 1/10 | 0/10 |
| 4 | 0/10 | 1/10 | 1/10 | 1/10 | 1/10 | 1/10 | 1/10 | 1/10 |
| 5 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| 6 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| 7 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| 8 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| 9 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 1/10 | 1/10 |
| 10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |

## Highest-depth filler successes

- `repeated_squaring_n319_x27_t9` reaches T=9 and is correct at k=[50, 100]; N=319, x=27, trace 91 -> 306 -> 169 -> 170 -> 190 -> 53 -> 257 -> 16 -> 256.
- No filler length solves T>9; in particular, all T=10 conditions are incorrect.

A high-T hit is a candidate for mechanistic inspection, not evidence by itself that the model executed every modular squaring. The moduli are small, and a salient or frequently generated final residue can be correct by an alternative route or coincidence.

## Validation and interpretation boundary

Every condition uses the same 100 shortcut-controlled examples and greedy non-thinking decoding. The no-filler prompt is evaluated once per example. For each k>0, the Appendix A exact-count system sentence and k spaced dots appear in all five demonstrations and the target. Character-to-token alignment is asserted separately at every k.

These are small semiprimes chosen for a tokenizer-compatible mechanistic pilot, not cryptographic-size instances. A length effect here therefore tests whether extra positions help this prompt/model combination; it does not establish the claimed no-shortcut complexity property at realistic modulus sizes.
