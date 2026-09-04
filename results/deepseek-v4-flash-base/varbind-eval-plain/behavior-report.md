# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 47 | 0.940 | 0.180 | 0.720 | — | — |
| 5 | 50 | 44 | 0.880 | 0.091 | 0.420 | 2 / 5 | 0.453 |
| 10 | 50 | 50 | 1.000 | 0.126 | 0.620 | 3 / 0 | 0.25 |
| 25 | 50 | 47 | 0.940 | 0.066 | 0.220 | 1 / 1 | 1 |
| 50 | 50 | 50 | 1.000 | 0.081 | 0.300 | 3 / 0 | 0.25 |
| 100 | 50 | 50 | 1.000 | 0.124 | 0.440 | 3 / 0 | 0.25 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
