# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 0 | 0.000 | 0.021 | 0.040 | — | — |
| 5 | 50 | 0 | 0.000 | 0.023 | 0.020 | 0 / 0 | 1 |
| 10 | 50 | 0 | 0.000 | 0.019 | 0.020 | 0 / 0 | 1 |
| 25 | 50 | 0 | 0.000 | 0.017 | 0.020 | 0 / 0 | 1 |
| 50 | 50 | 0 | 0.000 | 0.026 | 0.040 | 0 / 0 | 1 |
| 100 | 50 | 0 | 0.000 | 0.022 | 0.040 | 0 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
