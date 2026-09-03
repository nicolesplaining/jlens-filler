# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36 | 0 | 0.000 | 0.814 | 1.000 | — | — |
| 5 | 36 | 0 | 0.000 | 0.817 | 1.000 | 0 / 0 | 1 |
| 10 | 36 | 0 | 0.000 | 0.840 | 1.000 | 0 / 0 | 1 |
| 25 | 36 | 0 | 0.000 | 0.846 | 1.000 | 0 / 0 | 1 |
| 50 | 36 | 0 | 0.000 | 0.874 | 1.000 | 0 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
