# Letter Position filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 50 | 46 | 0.920 | 0.947 | 1.000 | — |
| 5 | 50 | 46 | 0.920 | 0.942 | 1.000 | 1 / 1 |
| 10 | 50 | 47 | 0.940 | 0.959 | 1.000 | 1 / 0 |
| 25 | 50 | 47 | 0.940 | 0.955 | 1.000 | 1 / 0 |
| 50 | 50 | 47 | 0.940 | 0.961 | 1.000 | 1 / 0 |
| 100 | 50 | 47 | 0.940 | 0.960 | 1.000 | 1 / 0 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
