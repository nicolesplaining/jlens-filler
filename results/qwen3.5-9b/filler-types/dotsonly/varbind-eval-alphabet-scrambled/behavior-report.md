# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 41 | 0.820 | 0.990 | 1.000 | — | — |
| 5 | 50 | 40 | 0.800 | 0.990 | 1.000 | 2 / 3 | 1 |
| 10 | 50 | 39 | 0.780 | 0.990 | 1.000 | 3 / 5 | 0.727 |
| 25 | 50 | 41 | 0.820 | 0.990 | 1.000 | 3 / 3 | 1 |
| 50 | 50 | 40 | 0.800 | 0.990 | 1.000 | 3 / 4 | 1 |
| 100 | 50 | 38 | 0.760 | 0.977 | 1.000 | 3 / 6 | 0.508 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
