# Variable Binding Pre Filler filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 35 | 0.700 | 0.795 | 0.960 | — |
| 50 | 50 | 35 | 0.700 | 0.789 | 0.980 | 5 / 5 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
