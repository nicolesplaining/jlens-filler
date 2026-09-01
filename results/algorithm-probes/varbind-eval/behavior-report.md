# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 35 | 0.700 | 0.795 | 0.960 | — |
| 5 | 50 | 45 | 0.900 | 0.923 | 0.980 | 11 / 1 |
| 10 | 50 | 42 | 0.840 | 0.890 | 1.000 | 9 / 2 |
| 25 | 50 | 43 | 0.860 | 0.911 | 1.000 | 11 / 3 |
| 50 | 50 | 49 | 0.980 | 0.990 | 1.000 | 14 / 0 |
| 100 | 50 | 49 | 0.980 | 0.990 | 1.000 | 14 / 0 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
