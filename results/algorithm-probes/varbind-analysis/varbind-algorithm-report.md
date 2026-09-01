# Variable-binding filler workspace: initial algorithmic evidence

All decoded values below are **J-Lens token readouts**, not formal sparse J-space coordinates and not a transcript of hidden reasoning.

## Behavioral effect

| Dots | Correct / 50 | Accuracy | Helped / hurt vs no filler |
|---:|---:|---:|---:|
| 0 | 35 / 50 | 0.70 | — |
| 5 | 45 / 50 | 0.90 | 11 / 1 |
| 10 | 42 / 50 | 0.84 | 9 / 2 |
| 25 | 43 / 50 | 0.86 | 11 / 3 |
| 50 | 49 / 50 | 0.98 | 14 / 0 |
| 100 | 49 / 50 | 0.98 | 14 / 0 |

## Depth ladder at k=50

Median first layer with an exact rank-1 token in any filler cell across the four selected examples:

| Stage | J-Lens layer | Logit-lens layer | J examples with rank-1 |
|---|---:|---:|---:|
| visible base | 25.5 | 25.5 | 4 / 4 |
| first product | — | — | 0 / 4 |
| hidden bound value | 30.5 | 30.0 | 4 / 4 |
| second product | 32.0 | 33.0 | 4 / 4 |
| final answer | 36.0 | 36.0 | 4 / 4 |

## Across-example shuffled-token control

Exact top-1 filler-cell matches after a fixed two-example derangement of the tracked values:

| Stage | J actual / shuffled | Logit lens actual / shuffled |
|---|---:|---:|
| visible base | 86 / 0 | 69 / 0 |
| first product | 0 / 0 | 0 / 0 |
| hidden bound value | 98 / 0 | 75 / 0 |
| second product | 143 / 0 | 121 / 0 |
| final answer | 101 / 0 | 96 / 0 |

## Selected k=50 cases

| Example | No filler | 50 dots | J-Lens first rank-1 layers (base → bound → second product → answer) |
|---|---|---|---|
| `varbind_easy_0000` | `219` (✓) | `219` (✓) | 27 → 30 → 33 → 36 |
| `varbind_easy_0002` | `225` (✗) | `224` (✓) | 23 → 31 → 33 → 33 |
| `varbind_easy_0035` | `322` (✗) | `374` (✓) | 24 → 31 → 31 → 36 |
| `varbind_easy_0037` | `383` (✗) | `387` (✗) | 27 → 30 → 31 → 36 |

## Dot-threshold comparisons

| Example | Dots | Output | J rank-1 cell counts (base / bound / second product / answer) |
|---|---:|---|---:|
| `varbind_easy_0035` | 5 | `324` (✗) | 0 / 0 / 1 / 0 |
| `varbind_easy_0035` | 25 | `320` (✗) | 1 / 3 / 26 / 10 |
| `varbind_easy_0035` | 50 | `374` (✓) | 21 / 24 / 60 / 25 |
| `varbind_easy_0037` | 50 | `387` (✗) | 20 / 24 / 33 / 8 |
| `varbind_easy_0037` | 100 | `385` (✓) | 29 / 55 / 65 / 43 |

## Evidence-weighted interpretation

1. The hidden chain is ordered primarily by **layer depth**, not by filler ordinal: base retrieval appears in the mid-20s, the hidden bound value near layer 30, the second product in the low-30s, and the answer in the mid-30s.
2. The raw first product is absent as rank-1 in every selected case, while the post-add/subtract bound value is clear. The most conservative reading is that the multiply and offset are fused or represented outside a clean token direction—not that the product was never computed.
3. Filler positions do not behave like a left-to-right scratchpad. Later stages often first decode at earlier filler ordinals than earlier stages, and late values are broadcast across several noncontiguous cells.
4. More dots increase the number of parallel decodable copies and can move stage onsets earlier in layer depth. Since prompt-prefill positions are evaluated in parallel within each transformer layer, this is consistent with extra sequence width acting as a distributed workspace rather than extra serial transformer steps.
5. Existence is not sufficiency: at 25 dots the hard example contains rank-1 readouts for every major stage but still answers incorrectly. The 50-dot boundary failure also contains the correct answer in several cells. A causal intervention is needed before claiming those cells determine the output.
6. J-Lens and logit lens recover nearly the same ladder here. J-Lens sometimes advances the second-product readout by a few layers or increases its multiplicity, but the current sample does not support a broad J-Lens-superiority claim.
