# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 0 | 0.000 | 0.631 | 1.000 | — | — |
| 5 | 50 | 2 | 0.040 | 0.643 | 1.000 | 2 / 0 | 0.5 |
| 10 | 50 | 1 | 0.020 | 0.627 | 1.000 | 1 / 0 | 1 |
| 25 | 50 | 1 | 0.020 | 0.628 | 1.000 | 1 / 0 | 1 |
| 50 | 50 | 2 | 0.040 | 0.588 | 1.000 | 2 / 0 | 0.5 |
| 100 | 50 | 1 | 0.020 | 0.712 | 1.000 | 1 / 0 | 1 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
