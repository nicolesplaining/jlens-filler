# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 48 | 0.960 | 0.980 | 1.000 | — | — |
| 50 | 50 | 49 | 0.980 | 0.990 | 1.000 | 2 / 1 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
