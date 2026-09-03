# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 45 | 0.900 | 0.960 | 1.000 | — | — |
| 5 | 50 | 45 | 0.900 | 0.950 | 1.000 | 1 / 1 | 1 |
| 10 | 50 | 43 | 0.860 | 0.930 | 1.000 | 1 / 3 | 0.625 |
| 25 | 50 | 46 | 0.920 | 0.960 | 1.000 | 1 / 0 | 1 |
| 50 | 50 | 47 | 0.940 | 0.970 | 1.000 | 2 / 0 | 0.5 |
| 100 | 50 | 46 | 0.920 | 0.960 | 1.000 | 2 / 1 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
