# Three-fact and order-ablation results

These are **J-Lens token readouts**, not formal sparse J-space coordinates. All conditions use ten dot tokens and non-thinking chat-mode encoding.

## Model outcomes

| Condition | Order | Filler answer | No-filler answer | Expected |
|---|---|---:|---:|---:|
| `tungsten_plus_carbon` | tungsten → carbon | `80` (correct) | `80` (correct) | `80` |
| `carbon_plus_tungsten` | carbon → tungsten | `80` (correct) | `80` (correct) | `80` |
| `tungsten_carbon_oxygen` | tungsten → carbon → oxygen | `106` (wrong) | `96` (wrong) | `88` |
| `carbon_tungsten_oxygen` | carbon → tungsten → oxygen | `90` (wrong) | `42` (wrong) | `88` |

## Best direct numeric-token rank over all filler cells

| Condition | Target | J-Lens | Logit lens |
|---|---:|---|---|
| `tungsten_plus_carbon` | `74` | rank 1 at L36/F4 | rank 2 at L37/F5 |
| `tungsten_plus_carbon` | `6` | rank 5 at L36/F8 | rank 12 at L36/F8 |
| `tungsten_plus_carbon` | `80` | rank 89 at L41/F10 | rank 77 at L40/F10 |
| `carbon_plus_tungsten` | `74` | rank 1 at L35/F3 | rank 1 at L35/F3 |
| `carbon_plus_tungsten` | `6` | rank 92 at L20/F1 | rank 58 at L38/F5 |
| `carbon_plus_tungsten` | `80` | rank 53 at L39/F10 | rank 76 at L32/F3 |
| `tungsten_carbon_oxygen` | `74` | rank 1 at L35/F4 | rank 1 at L35/F4 |
| `tungsten_carbon_oxygen` | `6` | rank 6 at L35/F7 | rank 10 at L34/F4 |
| `tungsten_carbon_oxygen` | `8` | rank 30 at L22/F3 | rank 691 at L26/F3 |
| `tungsten_carbon_oxygen` | `80` | rank 40 at L24/F3 | rank 187 at L24/F3 |
| `tungsten_carbon_oxygen` | `88` | rank 2 at L27/F3 | rank 59 at L27/F3 |
| `carbon_tungsten_oxygen` | `74` | rank 1 at L35/F1 | rank 1 at L34/F1 |
| `carbon_tungsten_oxygen` | `6` | rank 20 at L40/F5 | rank 18 at L37/F3 |
| `carbon_tungsten_oxygen` | `8` | rank 17 at L22/F3 | rank 169 at L26/F3 |
| `carbon_tungsten_oxygen` | `80` | rank 13 at L35/F4 | rank 132 at L26/F3 |
| `carbon_tungsten_oxygen` | `88` | rank 13 at L27/F3 | rank 11 at L33/F1 |

## Factual readout contrasts

- In `tungsten_carbon_oxygen`, the correct sum token `88` reaches rank 2 at L27/F3 with J-Lens versus rank 59 at L27/F3 with logit lens. The model nevertheless generates `106`, so decodability is not sufficient for correct final selection.
- The partial sum `80` in that same condition reaches rank 40 at L24/F3 with J-Lens versus rank 187 at L24/F3 with logit lens.
- In the two-fact swap, the strongest J-Lens `74` cell moves from L36/F4 to L35/F3.
- In the three-fact swap, the strongest J-Lens `74` cell moves from L35/F4 to L35/F1. This is an order effect in the readout location, not evidence of a fixed filler-position algorithm.

Each source JSON records the exact prompt, token IDs, offsets, filler indices, top-10 readouts, target ranks, generated output, and final-block closure check.
