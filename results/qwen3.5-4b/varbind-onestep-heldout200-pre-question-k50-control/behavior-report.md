# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 200 | 147 | 0.735 | 0.938 | 1.000 | — | — |
| 50 | 200 | 139 | 0.695 | 0.917 | 1.000 | 4 / 12 | 0.0768 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
