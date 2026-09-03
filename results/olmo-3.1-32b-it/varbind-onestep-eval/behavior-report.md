# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 41 | 0.820 | 0.897 | 1.000 | — | — |
| 5 | 50 | 38 | 0.760 | 0.860 | 1.000 | 0 / 3 | 0.25 |
| 10 | 50 | 39 | 0.780 | 0.882 | 1.000 | 0 / 2 | 0.5 |
| 25 | 50 | 39 | 0.780 | 0.886 | 1.000 | 0 / 2 | 0.5 |
| 50 | 50 | 40 | 0.800 | 0.880 | 1.000 | 1 / 2 | 1 |
| 100 | 50 | 42 | 0.840 | 0.904 | 1.000 | 2 / 1 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
