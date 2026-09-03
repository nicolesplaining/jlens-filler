# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 2 | 0.040 | 0.502 | 0.980 | — | — |
| 5 | 50 | 1 | 0.020 | 0.498 | 1.000 | 0 / 1 | 1 |
| 10 | 50 | 2 | 0.040 | 0.518 | 0.960 | 1 / 1 | 1 |
| 25 | 50 | 3 | 0.060 | 0.536 | 0.980 | 1 / 0 | 1 |
| 50 | 50 | 2 | 0.040 | 0.532 | 0.960 | 1 / 1 | 1 |
| 100 | 50 | 2 | 0.040 | 0.528 | 0.960 | 0 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
