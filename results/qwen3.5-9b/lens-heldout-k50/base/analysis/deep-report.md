# Deep grid statistics (8 examples, 32 layers)

## Filler cells: log p(true stage first digit) − log p(control digit), mean over cells

| Stage | early | mid | late |
|---|---:|---:|---:|
| base_value | -0.001 | -0.011 | +0.201 |
| first_product | -0.003 | +0.003 | +0.070 |
| bound_value | -0.001 | +0.006 | +0.056 |
| second_product | -0.004 | -0.006 | +0.007 |
| answer | +0.001 | -0.028 | +0.006 |

## Ladder at answer_cue: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | — (n=0) | 29 (n=2) | — (n=0) |
| first_product | — (n=0) | 29 (n=4) | — (n=0) |
| bound_value | — (n=0) | 29 (n=5) | — (n=0) |
| second_product | — (n=0) | 29 (n=6) | — (n=0) |
| answer | — (n=0) | 29 (n=5) | — (n=0) |

## Ladder at answer_prediction: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | 31 (n=1) | 30 (n=8) | — (n=0) |
| first_product | 29 (n=1) | 29.5 (n=8) | 30 (n=2) |
| bound_value | 29 (n=3) | 28 (n=8) | 29 (n=3) |
| second_product | 29 (n=5) | 28.5 (n=8) | 31 (n=1) |
| answer | 31 (n=3) | 29 (n=8) | 30 (n=2) |

## Filler-cell top-1 tokens

| band | fraction digit tokens | most common top-1 tokens |
|---|---:|---|
| early | 0.000 | `'s'`×1191, `' '`×584, `'�'`×567, `'o'`×425, `'\n'`×421, `'...'`×208 |
| mid | 0.000 | `'\n'`×379, `'յ'`×351, `'�'`×334, `'内'`×145, `'人'`×144, `'提'`×136 |
| late | 0.010 | `' .'`×1258, `'յ'`×803, `' twice'`×106, `'\n\n'`×86, `'�'`×56, `'<|im_end|>'`×55 |
