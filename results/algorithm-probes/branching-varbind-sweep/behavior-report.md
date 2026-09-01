# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36 | 34 | 0.944 | 0.961 | 1.000 | — |
| 5 | 36 | 33 | 0.917 | 0.954 | 1.000 | 0 / 1 |
| 10 | 36 | 34 | 0.944 | 0.968 | 1.000 | 1 / 1 |
| 25 | 36 | 33 | 0.917 | 0.954 | 1.000 | 1 / 2 |
| 50 | 36 | 34 | 0.944 | 0.972 | 1.000 | 1 / 1 |

## Group `parallel_branches`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 36 | 0.944 | 0.961 |
| 5 | 36 | 0.917 | 0.954 |
| 10 | 36 | 0.944 | 0.968 |
| 25 | 36 | 0.917 | 0.954 |
| 50 | 36 | 0.944 | 0.972 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
