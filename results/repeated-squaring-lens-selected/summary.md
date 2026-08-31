# Selected repeated-squaring J-Lens readouts

These are J-Lens token readouts, not the paper's formal sparse J-space
decomposition.

## Result

The selected examples do not show a residue-by-residue computation moving across
successive filler positions. Across 26 known intermediate targets, J-Lens achieved
a better best filler-cell rank than the logit lens for 8, the logit lens was better
for 17, and one tied. Each method put exactly one target in its top 10.

The strongest result is conceptual rather than numerical. In the shortcut-controlled
T=10 failure (`N=667`, `x=41`), J-Lens readouts at filler 3 move through `gcd`,
`φ`, `Carmichael`, `factoring`, and `totient` around layers 30–38. This indicates
that number-theoretic task structure is transported into token space. It does not
yield the expected sequential trace, and the model's answer is wrong (`1` rather
than `639`).

## Examples

| Example | Condition outcome | Main filler-cell observation |
|---|---|---|
| `N=209, x=24, T=3` | Dots `80` ✓; no dots `144` ✗ | J-Lens improves `x_1=158` from rank 61 to 51 and `x_2=93` from 67 to 28, both at filler 3, but worsens final `x_3=80` from 148 to 411. The correct answer is not strongly decoded in a filler cell. |
| `N=407, x=30, T=4` | Dots `256` ✓; no dots `16` ✗ | No intermediate reaches either lens's top 10. The correct final token is rank 1 at the answer-prediction position by layer 41, but only rank 201 in the best filler cell. |
| `N=667, x=41, T=10` | Dots `1` ✗; no dots `41` ✗ | J-Lens puts `x_8=59` at rank 10 at L35/F1 versus logit-lens rank 54, but the other residues remain weak and their best positions cluster at filler 1 rather than following step order. |
| `N=473, x=31, T=1` | Dots `31` ✗; no dots `15` ✓ | The target `15` is weak in both readouts: J-Lens rank 261 versus logit-lens rank 158. |
| `N=473, x=31, T=8` | Dots `256` ✗; no dots `31` ✗ | Logit lens decodes `x_2=225` at rank 3 at L36/F4; J-Lens ranks it 23. J-Lens modestly improves `x_7=58` and `x_8=53`, but neither reaches rank 10. Several residues share filler 4 as their best position, not successive positions. |

The T=3 case is especially revealing about timing. At layer 41 and the
answer-prediction position, the eventual answer `80` is still only rank 6 and the
top token is `144`; the actual block-42 logits then make `80` top 1. In the T=4
case, `256` is already top 1 at that layer-41 answer position. Thus a successful
generation need not imply that the final answer was strongly present at a filler
position.

## Excluded shortcut control

The initial `N=299`, `x=35`, `T=10` example was correct in both conditions, and
J-Lens ranked `35` second at L30/F5. It was removed from the task evaluation when
we noticed that `x_10=x_0=35`; copying the input can therefore mimic success.
Its viewer remains saved as an explicit shortcut control, not evidence of ten-step
serial computation.

## Viewers

- [Dots-only T=3 success](repeated_squaring_n209_x24_t3/viewer.html)
- [Dots-only T=4 success](repeated_squaring_n407_x30_t4/viewer.html)
- [Shortcut-controlled T=10 failure](repeated_squaring_n667_x41_t10/viewer.html)
- [No-dots-only T=1 control](repeated_squaring_n473_x31_t1/viewer.html)
- [T=8 rank-improvement failure](repeated_squaring_n473_x31_t8/viewer.html)
- [Excluded copy-solvable T=10 control](repeated_squaring_n299_x35_t10/viewer.html)

## Validation boundary

The ordinary-prompt sanity gate passed. Final-head closure errors were zero for
the T=3, T=4, and shortcut-controlled T=10 examples; `7.6e-6` for the T=1
control; and `9.7e-4` for T=8. The last value is tiny relative to the roughly
tens-scale logits and did not change the decoded top token, but is recorded rather
than rounded to zero.

The released checkpoint still omits the fit-time projection from DeepSeek V4's
four hyper-connection streams. The implementation uses the model's final
`hc_head` at every layer, as documented in the compatibility report. This remains
the main interpretation caveat.
