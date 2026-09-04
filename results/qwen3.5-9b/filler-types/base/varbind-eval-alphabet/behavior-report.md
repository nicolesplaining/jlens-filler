# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 0 | 0.000 | 0.621 | 1.000 | — | — |
| 5 | 50 | 2 | 0.040 | 0.617 | 1.000 | 2 / 0 | 0.5 |
| 10 | 50 | 2 | 0.040 | 0.599 | 1.000 | 2 / 0 | 0.5 |
| 25 | 50 | 1 | 0.020 | 0.597 | 1.000 | 1 / 0 | 1 |
| 50 | 50 | 1 | 0.020 | 0.572 | 1.000 | 1 / 0 | 1 |
| 100 | 50 | 1 | 0.020 | 0.603 | 1.000 | 1 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
