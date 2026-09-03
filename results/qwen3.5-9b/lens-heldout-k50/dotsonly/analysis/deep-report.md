# Deep grid statistics (8 examples, 32 layers)

## Filler cells: log p(true stage first digit) − log p(control digit), mean over cells

| Stage | early | mid | late |
|---|---:|---:|---:|
| base_value | -0.001 | +0.004 | +0.069 |
| first_product | -0.006 | -0.023 | -0.055 |
| bound_value | +0.002 | +0.005 | -0.103 |
| second_product | -0.004 | -0.003 | +0.337 |
| answer | -0.001 | -0.010 | +0.123 |

## Ladder at answer_cue: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | — (n=0) | 1 (n=1) | — (n=0) |
| first_product | — (n=0) | 1 (n=3) | 29 (n=1) |
| bound_value | — (n=0) | 1 (n=3) | 29 (n=1) |
| second_product | 29 (n=3) | 27 (n=7) | — (n=0) |
| answer | 29.5 (n=4) | 27 (n=5) | 29 (n=1) |

## Ladder at answer_prediction: first layer with rank 1 / rank ≤ 10 (median over examples; n with any)

| Stage | rank 1 | rank ≤ 10 | control rank 1 |
|---|---:|---:|---:|
| base_value | 30 (n=1) | 31 (n=3) | — (n=0) |
| first_product | 30 (n=1) | 2 (n=5) | 30 (n=2) |
| bound_value | — (n=0) | 16.5 (n=6) | 30 (n=1) |
| second_product | 30 (n=5) | 28 (n=7) | 30 (n=1) |
| answer | 30 (n=8) | 28 (n=8) | 29 (n=2) |

## Filler-cell top-1 tokens

| band | fraction digit tokens | most common top-1 tokens |
|---|---:|---|
| early | 0.000 | `'s'`×2039, `' '`×620, `'...'`×388, `'u'`×207, `'\n'`×203, `'�'`×95 |
| mid | 0.000 | `'提'`×1459, `' '`×965, `'�'`×388, `'内'`×289, `'<think>'`×103, `'和'`×92 |
| late | 0.002 | `' .'`×1823, `'յ'`×1818, `'ек'`×91, `'�'`×37, `'变量'`×30, `'ာ'`×27 |
