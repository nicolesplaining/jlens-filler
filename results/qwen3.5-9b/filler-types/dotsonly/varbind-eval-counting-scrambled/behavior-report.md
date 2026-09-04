# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 42 | 0.840 | 0.990 | 1.000 | — | — |
| 5 | 50 | 38 | 0.760 | 0.980 | 1.000 | 1 / 5 | 0.219 |
| 10 | 50 | 36 | 0.720 | 0.970 | 1.000 | 0 / 6 | 0.0312 |
| 25 | 50 | 30 | 0.600 | 0.960 | 1.000 | 0 / 12 | 0.000488 |
| 50 | 50 | 30 | 0.600 | 0.957 | 1.000 | 0 / 12 | 0.000488 |
| 100 | 50 | 36 | 0.720 | 0.960 | 1.000 | 1 / 7 | 0.0703 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
