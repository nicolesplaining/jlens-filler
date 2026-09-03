# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 4 | 0.080 | 0.882 | 1.000 | — | — |
| 5 | 50 | 5 | 0.100 | 0.877 | 1.000 | 2 / 1 | 1 |
| 10 | 50 | 7 | 0.140 | 0.905 | 1.000 | 4 / 1 | 0.375 |
| 25 | 50 | 4 | 0.080 | 0.877 | 1.000 | 2 / 2 | 1 |
| 50 | 50 | 7 | 0.140 | 0.898 | 1.000 | 4 / 1 | 0.375 |
| 100 | 50 | 4 | 0.080 | 0.887 | 1.000 | 3 / 3 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
