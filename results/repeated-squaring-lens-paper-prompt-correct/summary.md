# Paper-matched correct T=4 J-Lens readout

This run uses the Appendix A dots scaffold, including the exact system sentence
that there will be 10 filler tokens. These are J-Lens token readouts, not the
paper's formal sparse J-space decomposition.

## Outcome

For `N=407`, `x_0=30`, the expected trace is
`86 → 70 → 16 → 256`. With dots the model generated `256` (correct); without
dots it generated `16`, the penultimate residue. The ten target filler tokens are
absolute model-token indices 441–450.

## Filler-position readouts

No expected residue reaches either lens's top 10 at a filler position. Best ranks:

| Target | J-Lens best filler cell | Logit-lens best filler cell |
|---|---:|---:|
| `x_1=86` | rank 80, L35/F1 | rank 151, L41/F10 |
| `x_2=70` | rank 302, L27/F7 | rank 118, L5/F1 |
| `x_3=16` | rank 341, L35/F1 | rank 170, L35/F1 |
| `x_4=256` | rank 362, L40/F10 | rank 183, L40/F10 |

The strongest qualitative signal is procedural rather than residue-valued.
Around layers 30–38, J-Lens readouts emphasize `modulus`/`modulo`/`modular` at
filler 3, `repeated`/`repetition` at filler 5, `step` at filler 7, and
`answer`-related tokens near filler 10. This resembles a task scaffold, but it is
not evidence of the four numeric squarings being represented in order.

At the answer-prediction position, J-Lens makes `256` top-1 by layer 40 and keeps
it top-1 at layer 41. The logit lens has `256` at rank 2 behind `81` at layer 40,
then makes it top-1 at layer 41. The actual model logits rank `256` first. Thus the
correct answer becomes cleanly decodable after the filler region even though the
known residues are weak within the filler cells.

## Validation boundary

The ordinary-prompt sanity gate passed, and final-head closure error is exactly
zero for this example. The released lens still omits the fit-time projection from
the model's four hyper-connection streams; this repository's documented
`hc_head` convention remains the main interpretation caveat.

- [Interactive viewer](repeated_squaring_n407_x30_t4/viewer.html)
- [Machine-readable readouts](repeated_squaring_n407_x30_t4/readouts.jsonl)
- [Exact filler-rank table](lens-summary.csv)
