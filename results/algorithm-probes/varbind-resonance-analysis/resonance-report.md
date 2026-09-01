# Dot-count resonance readouts

These are J-Lens token readouts, not formal sparse J-space coordinates.

| Dots | Output | Correct | Answer rank |
|---:|---:|:---:|---:|
| 5 | 235 | yes | 1 |
| 10 | 185 | no | 76 |
| 25 | 185 | no | 12 |
| 50 | 235 | yes | 1 |
| 100 | 235 | yes | 1 |

## J-Lens

Each cell is `rank-1 count / rank-weighted top-10 strength (first rank-1 layer, dot)`.

| Dots | Base | Bound | Second product | Answer |
|---:|---:|---:|---:|---:|
| 5 | 0 / 0.0 (—) | 0 / 0.0 (—) | 0 / 0.0 (—) | 3 / 4.6 (L36,F2) |
| 10 | 7 / 10.5 (L22,F1) | 0 / 0.0 (—) | 0 / 0.0 (—) | 0 / 0.0 (—) |
| 25 | 12 / 13.7 (L24,F8) | 4 / 7.1 (L35,F10) | 0 / 2.0 (—) | 0 / 0.0 (—) |
| 50 | 36 / 46.1 (L23,F44) | 20 / 32.0 (L31,F13) | 13 / 26.1 (L32,F43) | 24 / 37.6 (L31,F14) |
| 100 | 37 / 76.4 (L24,F8) | 71 / 109.5 (L30,F5) | 36 / 75.5 (L32,F19) | 60 / 87.4 (L31,F20) |

## Logit lens

Each cell is `rank-1 count / rank-weighted top-10 strength (first rank-1 layer, dot)`.

| Dots | Base | Bound | Second product | Answer |
|---:|---:|---:|---:|---:|
| 5 | 0 / 0.0 (—) | 0 / 0.0 (—) | 0 / 0.0 (—) | 0 / 0.3 (—) |
| 10 | 11 / 12.7 (L24,F1) | 0 / 0.0 (—) | 0 / 0.0 (—) | 0 / 0.0 (—) |
| 25 | 9 / 17.4 (L27,F8) | 5 / 6.9 (L35,F10) | 0 / 0.8 (—) | 0 / 0.0 (—) |
| 50 | 38 / 53.9 (L25,F1) | 17 / 31.5 (L31,F13) | 13 / 27.8 (L32,F43) | 22 / 37.1 (L31,F14) |
| 100 | 77 / 140.9 (L24,F23) | 63 / 115.9 (L29,F5) | 33 / 82.3 (L32,F23) | 41 / 86.7 (L35,F59) |

## Correct route versus sibling-variable route (J-Lens)

The wrong output 185 is the exact result of applying the question's final operation to sibling variable `rek=100` instead of requested variable `xav=125`.

Each cell is `rank-1 count / rank-weighted top-10 strength`.

| Dots | Correct bound 125 | Distractor bound 100 | Correct product 250 | Distractor product 200 | Correct answer 235 | Distractor answer 185 |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 3 / 4.6 | 0 / 0.0 |
| 10 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 1.0 |
| 25 | 4 / 7.1 | 0 / 0.7 | 0 / 2.0 | 0 / 0.0 | 0 / 0.0 | 7 / 11.7 |
| 50 | 20 / 32.0 | 3 / 4.2 | 13 / 26.1 | 0 / 0.0 | 24 / 37.6 | 21 / 48.1 |
| 100 | 71 / 109.5 | 5 / 7.7 | 36 / 75.5 | 0 / 3.4 | 60 / 87.4 | 24 / 69.6 |
