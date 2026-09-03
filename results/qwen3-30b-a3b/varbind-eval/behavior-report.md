# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 5 | 0.100 | 0.742 | 1.000 | — | — |
| 5 | 50 | 4 | 0.080 | 0.674 | 1.000 | 0 / 1 | 1 |
| 10 | 50 | 5 | 0.100 | 0.656 | 1.000 | 0 / 0 | 1 |
| 25 | 50 | 4 | 0.080 | 0.668 | 1.000 | 0 / 1 | 1 |
| 50 | 50 | 4 | 0.080 | 0.711 | 1.000 | 0 / 1 | 1 |
| 100 | 50 | 3 | 0.060 | 0.610 | 0.980 | 0 / 2 | 0.5 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
