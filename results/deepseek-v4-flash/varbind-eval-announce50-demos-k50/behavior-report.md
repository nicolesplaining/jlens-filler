# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.762 | 0.960 | — | — |
| 50 | 50 | 47 | 0.940 | 0.961 | 1.000 | 13 / 0 | 0.000244 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
