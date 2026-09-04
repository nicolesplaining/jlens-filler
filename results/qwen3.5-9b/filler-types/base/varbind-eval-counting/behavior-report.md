# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 0 | 0.000 | 0.621 | 1.000 | — | — |
| 5 | 50 | 0 | 0.000 | 0.574 | 1.000 | 0 / 0 | 1 |
| 10 | 50 | 1 | 0.020 | 0.544 | 1.000 | 1 / 0 | 1 |
| 25 | 50 | 0 | 0.000 | 0.550 | 1.000 | 0 / 0 | 1 |
| 50 | 50 | 0 | 0.000 | 0.576 | 1.000 | 0 / 0 | 1 |
| 100 | 50 | 0 | 0.000 | 0.618 | 1.000 | 0 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
