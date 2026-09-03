# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 4 | 0.080 | 0.683 | 1.000 | — | — |
| 5 | 50 | 0 | 0.000 | 0.752 | 1.000 | 0 / 4 | 0.125 |
| 10 | 50 | 1 | 0.020 | 0.709 | 1.000 | 0 / 3 | 0.25 |
| 25 | 50 | 1 | 0.020 | 0.712 | 1.000 | 0 / 3 | 0.25 |
| 50 | 50 | 0 | 0.000 | 0.734 | 1.000 | 0 / 4 | 0.125 |
| 100 | 50 | 1 | 0.020 | 0.723 | 1.000 | 1 / 4 | 0.375 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
