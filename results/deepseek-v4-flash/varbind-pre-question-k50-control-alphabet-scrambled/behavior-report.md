# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 34 | 0.680 | 0.784 | 0.940 | — | — |
| 50 | 50 | 36 | 0.720 | 0.788 | 0.940 | 5 / 3 | 0.727 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
