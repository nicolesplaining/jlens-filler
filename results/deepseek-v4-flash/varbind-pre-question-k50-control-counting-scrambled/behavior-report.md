# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 50 | 50 | 28 | 0.560 | 0.669 | 0.940 | 5 / 11 | 0.21 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
