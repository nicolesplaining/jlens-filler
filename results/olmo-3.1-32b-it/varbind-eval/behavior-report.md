# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 1 | 0.020 | 0.056 | 0.120 | — | — |
| 5 | 50 | 1 | 0.020 | 0.075 | 0.180 | 0 / 0 | 1 |
| 10 | 50 | 1 | 0.020 | 0.070 | 0.140 | 0 / 0 | 1 |
| 25 | 50 | 1 | 0.020 | 0.067 | 0.180 | 0 / 0 | 1 |
| 50 | 50 | 1 | 0.020 | 0.064 | 0.140 | 0 / 0 | 1 |
| 100 | 50 | 1 | 0.020 | 0.068 | 0.160 | 0 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
