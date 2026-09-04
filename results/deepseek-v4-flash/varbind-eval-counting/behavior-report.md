# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 5 | 50 | 45 | 0.900 | 0.945 | 1.000 | 12 / 1 | 0.00342 |
| 10 | 50 | 45 | 0.900 | 0.936 | 0.980 | 11 / 0 | 0.000977 |
| 25 | 50 | 46 | 0.920 | 0.946 | 1.000 | 13 / 1 | 0.00183 |
| 50 | 50 | 49 | 0.980 | 0.990 | 1.000 | 15 / 0 | 6.1e-05 |
| 100 | 50 | 48 | 0.960 | 0.975 | 1.000 | 15 / 1 | 0.000519 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
