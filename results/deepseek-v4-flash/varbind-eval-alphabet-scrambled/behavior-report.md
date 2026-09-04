# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 5 | 50 | 38 | 0.760 | 0.834 | 0.960 | 9 / 5 | 0.424 |
| 10 | 50 | 32 | 0.640 | 0.759 | 0.980 | 4 / 6 | 0.754 |
| 25 | 50 | 38 | 0.760 | 0.846 | 1.000 | 7 / 3 | 0.344 |
| 50 | 50 | 41 | 0.820 | 0.875 | 0.940 | 10 / 3 | 0.0923 |
| 100 | 50 | 46 | 0.920 | 0.953 | 1.000 | 13 / 1 | 0.00183 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
