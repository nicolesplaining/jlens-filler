# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 37 | 0.740 | 0.930 | 1.000 | — | — |
| 5 | 50 | 42 | 0.840 | 0.970 | 1.000 | 6 / 1 | 0.125 |
| 10 | 50 | 38 | 0.760 | 0.950 | 1.000 | 3 / 2 | 1 |
| 25 | 50 | 36 | 0.720 | 0.940 | 1.000 | 3 / 4 | 1 |
| 50 | 50 | 40 | 0.800 | 0.970 | 1.000 | 6 / 3 | 0.508 |
| 100 | 50 | 41 | 0.820 | 0.980 | 1.000 | 5 / 1 | 0.219 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
