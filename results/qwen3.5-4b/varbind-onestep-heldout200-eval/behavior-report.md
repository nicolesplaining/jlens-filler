# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 200 | 147 | 0.735 | 0.938 | 1.000 | — | — |
| 5 | 200 | 145 | 0.725 | 0.928 | 1.000 | 5 / 7 | 0.774 |
| 10 | 200 | 142 | 0.710 | 0.933 | 1.000 | 5 / 10 | 0.302 |
| 25 | 200 | 150 | 0.750 | 0.949 | 1.000 | 9 / 6 | 0.607 |
| 50 | 200 | 144 | 0.720 | 0.935 | 1.000 | 6 / 9 | 0.607 |
| 100 | 200 | 149 | 0.745 | 0.947 | 1.000 | 9 / 7 | 0.804 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
