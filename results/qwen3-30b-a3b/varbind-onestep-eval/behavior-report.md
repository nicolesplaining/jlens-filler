# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 48 | 0.960 | 0.990 | 1.000 | — | — |
| 5 | 50 | 48 | 0.960 | 0.990 | 1.000 | 0 / 0 | 1 |
| 10 | 50 | 47 | 0.940 | 0.980 | 1.000 | 0 / 1 | 1 |
| 25 | 50 | 47 | 0.940 | 0.980 | 1.000 | 0 / 1 | 1 |
| 50 | 50 | 47 | 0.940 | 0.980 | 1.000 | 0 / 1 | 1 |
| 100 | 50 | 47 | 0.940 | 0.980 | 1.000 | 0 / 1 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
