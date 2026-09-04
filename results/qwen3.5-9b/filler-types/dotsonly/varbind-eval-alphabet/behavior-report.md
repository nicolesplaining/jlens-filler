# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 42 | 0.840 | 0.990 | 1.000 | — | — |
| 5 | 50 | 40 | 0.800 | 0.970 | 1.000 | 1 / 3 | 0.625 |
| 10 | 50 | 40 | 0.800 | 0.990 | 1.000 | 2 / 4 | 0.688 |
| 25 | 50 | 39 | 0.780 | 0.990 | 1.000 | 2 / 5 | 0.453 |
| 50 | 50 | 40 | 0.800 | 0.990 | 1.000 | 1 / 3 | 0.625 |
| 100 | 50 | 39 | 0.780 | 0.970 | 1.000 | 2 / 5 | 0.453 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
