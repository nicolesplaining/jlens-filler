# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 40 | 2 | 0.050 | 0.086 | 0.075 | — |
| 10 | 40 | 1 | 0.025 | 0.069 | 0.125 | 0 / 1 |
| 25 | 40 | 3 | 0.075 | 0.128 | 0.225 | 2 / 1 |
| 50 | 40 | 1 | 0.025 | 0.086 | 0.200 | 0 / 1 |

## Group `parallel_depth2`

| Visible dots | N | Accuracy | Answer MRR |
|---:|---:|---:|---:|
| 0 | 40 | 0.050 | 0.086 |
| 10 | 40 | 0.025 | 0.069 |
| 25 | 40 | 0.075 | 0.128 |
| 50 | 40 | 0.025 | 0.086 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
