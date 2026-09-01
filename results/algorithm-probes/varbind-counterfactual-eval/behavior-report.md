# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0 | 0.000 | 0.178 | 0.625 | — |
| 50 | 8 | 8 | 1.000 | 1.000 | 1.000 | 8 / 0 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
