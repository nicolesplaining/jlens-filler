# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 5 | 50 | 31 | 0.620 | 0.749 | 0.960 | 6 / 9 | 0.607 |
| 10 | 50 | 41 | 0.820 | 0.875 | 0.980 | 11 / 4 | 0.118 |
| 25 | 50 | 41 | 0.820 | 0.879 | 0.980 | 9 / 2 | 0.0654 |
| 50 | 50 | 49 | 0.980 | 0.990 | 1.000 | 15 / 0 | 6.1e-05 |
| 100 | 50 | 50 | 1.000 | 1.000 | 1.000 | 16 / 0 | 3.05e-05 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
