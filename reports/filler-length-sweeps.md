# Filler-length sweeps and task selection

## Outcome

Two paired behavioral sweeps were run with DeepSeek V4 Flash using the paper PDF's
exact-count filler instruction. The repeated-squaring sweep used the same 100
shortcut-controlled examples at every condition. The two-fact calibration used the
first 100 released targets and all five released demonstrations from
`data/2fact_addition_dataset.json` at commit
`4ba4c75d5d9f04248749ec46b8bed8661b746715`.

| Visible dots k | Repeated squaring | Two-fact addition |
|---:|---:|---:|
| 0 | 2/100 | 41/100 |
| 1 | 3/100 | 38/100 |
| 3 | 7/100 | - |
| 5 | 3/100 | 40/100 |
| 10 | 7/100 | 42/100 |
| 25 | 5/100 | 40/100 |
| 50 | 5/100 | 44/100 |
| 100 | 3/100 | 45/100 |

The repeated-squaring response is non-monotonic. Both k=3 and k=10 improve observed
accuracy from 2% to 7% (paired-bootstrap 95% interval for the difference: +1 to +10
percentage points; exact McNemar p=0.0625 before correction for testing seven positive
lengths). Correct-token rank also favors filler at k=3 in 62 pairs versus 34 for the
baseline (exact sign-test p=0.0056). Longer filler does not increase aggregate
accuracy: k=25 and 50 score 5%, and k=100 scores 3%.

One notable stress-test case, `repeated_squaring_n319_x27_t9`, is correct only at
k=50 and k=100. Its trace is
`91 -> 306 -> 169 -> 170 -> 190 -> 53 -> 257 -> 16 -> 256`; shorter conditions output
`81`, while the two longest output `256`. This is worth inspecting with the J-Lens,
but it is not by itself evidence of nine sequential squarings: 256 is salient, the
modulus 319 is small, and the benchmark is not cryptographic-scale. No k solves any
T=10 example.

The addition calibration has a much healthier behavioral range. Its best observed
condition is k=100 at 45%, versus 41% without filler. The accuracy difference is not
statistically resolved in this pilot (95% interval -5 to +13 points; exact McNemar
p=0.523). However, k=100 improves the target's rank in 37 pairs and worsens it in 21
(exact sign-test p=0.0479), raises MRR by 0.0597, and raises mean target log-probability
by 0.741 nats. Those rank-level effects make it a better lens calibration even though
the accuracy uplift is uncertain.

## Recommended mechanistic sequence

Use two-fact addition as the primary J-Lens calibration and retain repeated squaring
as a stress test. Two-fact addition has known, tokenizer-friendly retrieved values and
a known sum, plus enough correct and incorrect answers for matched error analysis. It
is compositional but not a forced serial chain because the two facts may be retrieved
in parallel.

Start with these paired qualitative cases at k=100, with matched k=10 extractions where
useful:

- `two_fact_0007`: Iridium 77 + Antimony 51 = 128. It is wrong through k=10, then
  correct at k=25, 50, and 100; target rank moves from 6 at baseline to 1.
- `two_fact_0016`: Potassium 19 + Dysprosium 66 = 85. It is correct only at k=100,
  making it a clean long-filler transition case.
- `two_fact_0006`: Silver 47 + Hydrogen 1 = 48. It is correct at every length and is
  an easy positive control.
- `two_fact_0000`: Thorium 90 + Tellurium 52 = 142. It is correct without filler but
  wrong from k=5 onward, providing a filler-hurts control.

For a middle rung that preserves a genuine dependency chain while avoiding the
repeated-squaring floor, use the filler paper's in-context chained-equation task after
the addition calibration. Three-fact addition is also useful for order ablations, but
associativity means it still does not enforce a serial computation.

## Reproducibility caveat

An independent earlier k=0/k=10 repeated-squaring run used byte-identical rendered
prompts and produced identical correctness on all 100 examples. It did not reproduce
all logits bit-for-bit: small FP8/custom-kernel numerical differences changed many
close target ranks and changed the already-wrong top-1 answer in two k=10 examples.
Aggregate k=10 accuracy remained 7/100. Seeds, revisions, prompt hashes, and commands
are recorded, but borderline logits should be repeated rather than treated as exactly
deterministic.

The three-token generation cap used for these sweeps preserves all numeric responses
(which terminate in two tokens in the prior run) and keeps instruction-violating prose
from dominating runtime. All target ranks and log-probabilities are computed from the
unchanged first-token distribution.
