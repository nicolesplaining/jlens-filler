# Addition filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 60 | 4 | 0.067 | 0.108 | 0.150 | — |
| 5 | 60 | 3 | 0.050 | 0.106 | 0.200 | 1 / 2 |
| 10 | 60 | 3 | 0.050 | 0.102 | 0.167 | 1 / 2 |
| 25 | 60 | 3 | 0.050 | 0.102 | 0.167 | 1 / 2 |
| 50 | 60 | 3 | 0.050 | 0.102 | 0.183 | 1 / 2 |
| 100 | 60 | 1 | 0.017 | 0.089 | 0.217 | 1 / 4 |

## Group `0`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 20 | 0.000 | 0.072 |
| 5 | 20 | 0.050 | 0.094 |
| 10 | 20 | 0.050 | 0.098 |
| 25 | 20 | 0.000 | 0.064 |
| 50 | 20 | 0.050 | 0.087 |
| 100 | 20 | 0.050 | 0.096 |

## Group `1`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 20 | 0.100 | 0.131 |
| 5 | 20 | 0.000 | 0.077 |
| 10 | 20 | 0.050 | 0.098 |
| 25 | 20 | 0.000 | 0.075 |
| 50 | 20 | 0.050 | 0.100 |
| 100 | 20 | 0.000 | 0.084 |

## Group `2`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 20 | 0.100 | 0.121 |
| 5 | 20 | 0.100 | 0.148 |
| 10 | 20 | 0.050 | 0.109 |
| 25 | 20 | 0.150 | 0.169 |
| 50 | 20 | 0.050 | 0.119 |
| 100 | 20 | 0.000 | 0.088 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
