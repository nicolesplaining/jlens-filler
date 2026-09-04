# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 42 | 0.840 | 0.990 | 1.000 | — | — |
| 5 | 50 | 39 | 0.780 | 0.990 | 1.000 | 1 / 4 | 0.375 |
| 10 | 50 | 38 | 0.760 | 0.980 | 1.000 | 2 / 6 | 0.289 |
| 25 | 50 | 39 | 0.780 | 0.970 | 1.000 | 1 / 4 | 0.375 |
| 50 | 50 | 37 | 0.740 | 0.970 | 1.000 | 0 / 5 | 0.0625 |
| 100 | 50 | 39 | 0.780 | 0.980 | 1.000 | 3 / 6 | 0.508 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
