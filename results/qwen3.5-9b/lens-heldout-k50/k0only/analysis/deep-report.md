# Deep grid statistics (8 examples, 32 layers)

## Filler cells: log p(true stage first digit) − log p(control digit), mean over cells

| Stage | early | mid | late |
|---|---:|---:|---:|
| base_value | +0.002 | +0.080 | -0.042 |
| first_product | -0.003 | -0.012 | +0.169 |
| bound_value | +0.000 | -0.003 | +0.008 |
| second_product | -0.005 | -0.034 | +0.597 |
| answer | -0.003 | -0.029 | +0.358 |

## Ladder at answer_cue: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | — (n=0) | 4 (n=1) | — (n=0) |
| first_product | — (n=0) | 4 (n=3) | 30 (n=1) |
| bound_value | — (n=0) | 4 (n=3) | 30 (n=1) |
| second_product | 30 (n=3) | 27 (n=7) | — (n=0) |
| answer | 30 (n=4) | 27 (n=5) | 29 (n=1) |

## Ladder at answer_prediction: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | 30 (n=1) | 31 (n=4) | — (n=0) |
| first_product | 29 (n=1) | 12.5 (n=6) | 29 (n=2) |
| bound_value | — (n=0) | 2 (n=5) | 29 (n=1) |
| second_product | 28.5 (n=4) | 27 (n=7) | 30 (n=1) |
| answer | 29 (n=7) | 28 (n=8) | 29 (n=2) |

## Filler-cell top-1 tokens

| band | fraction digit tokens | most common top-1 tokens |
|---|---:|---|
| early | 0.000 | `'s'`×1451, `'o'`×702, `' '`×465, `'\n'`×409, `'...'`×218, `'�'`×208 |
| mid | 0.000 | `'\n'`×472, `'յ'`×397, `'内'`×324, `'�'`×302, `'ံ'`×237, `'提'`×199 |
| late | 0.010 | `' .'`×1525, `'յ'`×1146, `'�'`×187, `'ာ'`×91, `'longleftrightarrow'`×88, `'\n\n'`×69 |
