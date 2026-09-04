# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 19 | 0.380 | 0.012 | 0.020 | — | — |
| 5 | 50 | 23 | 0.460 | 0.017 | 0.000 | 7 / 3 | 0.344 |
| 10 | 50 | 29 | 0.580 | 0.015 | 0.000 | 14 / 4 | 0.0309 |
| 25 | 50 | 36 | 0.720 | 0.017 | 0.000 | 17 / 0 | 1.53e-05 |
| 50 | 50 | 39 | 0.780 | 0.020 | 0.020 | 22 / 2 | 3.59e-05 |
| 100 | 50 | 44 | 0.880 | 0.041 | 0.080 | 27 / 2 | 1.62e-06 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
