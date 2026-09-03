# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 3 | 0.060 | 0.657 | 1.000 | — | — |
| 5 | 50 | 3 | 0.060 | 0.627 | 1.000 | 1 / 1 | 1 |
| 10 | 50 | 2 | 0.040 | 0.607 | 1.000 | 0 / 1 | 1 |
| 25 | 50 | 3 | 0.060 | 0.652 | 1.000 | 0 / 0 | 1 |
| 50 | 50 | 4 | 0.080 | 0.676 | 1.000 | 1 / 0 | 1 |
| 100 | 50 | 4 | 0.080 | 0.655 | 1.000 | 1 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
