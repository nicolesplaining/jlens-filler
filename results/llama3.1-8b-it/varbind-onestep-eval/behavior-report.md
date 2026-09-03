# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 26 | 0.520 | 0.629 | 0.860 | — | — |
| 5 | 50 | 25 | 0.500 | 0.621 | 0.860 | 1 / 2 | 1 |
| 10 | 50 | 26 | 0.520 | 0.622 | 0.840 | 2 / 2 | 1 |
| 25 | 50 | 26 | 0.520 | 0.638 | 0.880 | 3 / 3 | 1 |
| 50 | 50 | 24 | 0.480 | 0.615 | 0.900 | 2 / 4 | 0.688 |
| 100 | 50 | 26 | 0.520 | 0.618 | 0.840 | 4 / 4 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
