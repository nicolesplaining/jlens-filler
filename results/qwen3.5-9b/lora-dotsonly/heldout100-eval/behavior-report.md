# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 100 | 67 | 0.670 | 0.973 | 1.000 | — | — |
| 5 | 100 | 70 | 0.700 | 0.978 | 1.000 | 8 / 5 | 0.581 |
| 10 | 100 | 73 | 0.730 | 0.978 | 1.000 | 10 / 4 | 0.18 |
| 25 | 100 | 68 | 0.680 | 0.978 | 1.000 | 7 / 6 | 1 |
| 50 | 100 | 63 | 0.630 | 0.978 | 1.000 | 5 / 9 | 0.424 |
| 100 | 100 | 67 | 0.670 | 0.978 | 1.000 | 8 / 8 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
