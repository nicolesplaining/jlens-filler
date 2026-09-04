# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 28 | 0.560 | 0.720 | 0.960 | — | — |
| 50 | 50 | 36 | 0.720 | 0.803 | 0.960 | 11 / 3 | 0.0574 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
