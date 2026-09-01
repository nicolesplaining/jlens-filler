# Variable Binding filler-length sweep

| Visible dots | N | Correct | Accuracy | Answer MRR | R@10 | Helped / hurt vs k=0 | Exact McNemar p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 100 | 59 | 0.590 | 0.670 | 0.850 | — | — |
| 5 | 100 | 74 | 0.740 | 0.821 | 0.960 | 22 / 7 | 0.00813 |
| 10 | 100 | 70 | 0.700 | 0.782 | 0.910 | 16 / 5 | 0.0266 |
| 25 | 100 | 79 | 0.790 | 0.852 | 0.970 | 21 / 1 | 1.1e-05 |
| 50 | 100 | 94 | 0.940 | 0.958 | 0.980 | 35 / 0 | 5.82e-11 |
| 100 | 100 | 96 | 0.960 | 0.975 | 1.000 | 37 / 0 | 1.46e-11 |

The rank metrics use the model's actual next-token logits, not either lens. They are used only to choose behaviorally meaningful examples for readout extraction.
