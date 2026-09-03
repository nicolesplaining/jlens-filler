# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 41 | 0.820 | 0.950 | 1.000 | — | — |
| 5 | 50 | 41 | 0.820 | 0.960 | 1.000 | 1 / 1 | 1 |
| 10 | 50 | 44 | 0.880 | 0.980 | 1.000 | 4 / 1 | 0.375 |
| 25 | 50 | 41 | 0.820 | 0.950 | 1.000 | 2 / 2 | 1 |
| 50 | 50 | 42 | 0.840 | 0.960 | 1.000 | 3 / 2 | 1 |
| 100 | 50 | 41 | 0.820 | 0.960 | 1.000 | 1 / 1 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
