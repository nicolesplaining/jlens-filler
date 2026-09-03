# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 100 | 67 | 0.670 | 0.973 | 1.000 | — | — |
| 50 | 100 | 69 | 0.690 | 0.973 | 1.000 | 7 / 5 | 0.774 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
