# Arithmetic Program filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 48 | 9 | 0.188 | 0.295 | 0.562 | — |
| 5 | 48 | 5 | 0.104 | 0.254 | 0.604 | 1 / 5 |
| 10 | 48 | 5 | 0.104 | 0.234 | 0.521 | 1 / 5 |
| 25 | 48 | 8 | 0.167 | 0.296 | 0.646 | 3 / 4 |
| 50 | 48 | 6 | 0.125 | 0.295 | 0.625 | 1 / 4 |

## Group `balanced_tree`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 24 | 0.250 | 0.336 |
| 5 | 24 | 0.125 | 0.263 |
| 10 | 24 | 0.083 | 0.195 |
| 25 | 24 | 0.250 | 0.352 |
| 50 | 24 | 0.167 | 0.306 |

## Group `serial_chain`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 24 | 0.125 | 0.253 |
| 5 | 24 | 0.083 | 0.244 |
| 10 | 24 | 0.125 | 0.272 |
| 25 | 24 | 0.083 | 0.240 |
| 50 | 24 | 0.083 | 0.284 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
