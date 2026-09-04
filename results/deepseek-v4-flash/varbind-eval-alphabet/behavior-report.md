# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 5 | 50 | 41 | 0.820 | 0.867 | 0.980 | 11 / 4 | 0.118 |
| 10 | 50 | 43 | 0.860 | 0.896 | 0.980 | 11 / 2 | 0.0225 |
| 25 | 50 | 41 | 0.820 | 0.883 | 0.980 | 10 / 3 | 0.0923 |
| 50 | 50 | 42 | 0.840 | 0.876 | 0.940 | 12 / 4 | 0.0768 |
| 100 | 50 | 43 | 0.860 | 0.918 | 1.000 | 12 / 3 | 0.0352 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
