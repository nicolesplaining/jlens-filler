# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 4 | 0.080 | 0.883 | 1.000 | — | — |
| 5 | 50 | 3 | 0.060 | 0.900 | 1.000 | 2 / 3 | 1 |
| 10 | 50 | 3 | 0.060 | 0.880 | 1.000 | 2 / 3 | 1 |
| 25 | 50 | 5 | 0.100 | 0.898 | 1.000 | 3 / 2 | 1 |
| 50 | 50 | 3 | 0.060 | 0.891 | 1.000 | 2 / 3 | 1 |
| 100 | 50 | 2 | 0.040 | 0.883 | 1.000 | 1 / 3 | 0.625 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
