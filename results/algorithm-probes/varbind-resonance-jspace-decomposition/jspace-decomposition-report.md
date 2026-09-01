# Formal J-space decomposition: filler candidate competition

These results use a sparse nonnegative gradient-pursuit decomposition with `k=25`. They are formal J-space coordinates under the released dictionary and the stated DeepSeek mHC-collapse convention, not ranked J-Lens readouts.

## Validation

- Synthetic support recovery: exact; maximum coefficient error `0.0e+00`.
- Folding DeepSeek RMSNorm into the token dictionary reproduces the complete top-25 J-Lens ranking at every site; maximum relative logit error `1.45e-06`.
- The decomposition implementation is pinned to TransformerLens revision `1f8224d5e147c98e8f43f0d310e32bbd1578a4b6` and source SHA-256 `3193aeee3174ad9781327aca42d1cac7466d2cbf88530d39da831f02a9eb1161`.

## Main result

Every tracked task token that was J-Lens rank 1 was retained as an active J-space atom (`7/7`). Among tracked task tokens ranked 2–25, none was retained (`0/9`).

In both joint-candidate cells, the readout ranked the requested answer `235` first and sibling answer `185` second. The formal `k=25` support retained `235` and omitted `185`. Likewise, at k=25/L36/F10 it retained bound value `125` (rank 1) but omitted product `250` (rank 2). Thus a ranked list can show several related candidates even when the pursuit inventory chooses only one of them.

This refines the earlier candidate-competition claim: `235` and `185` are both broadcast across the layer × filler grid, but the selected individual cells are more winner-like under the paper-standard sparse inventory. Because the dictionary is overcomplete and the pursuit is greedy, omission does not prove that an alternative sparse support containing the runner-up is impossible.

## Site summary

| Site | Output | L/F | Active task atoms in J-space | Active task atoms in sparse logit space | J raw FVE | Rotated control | Excess |
|---|---:|---:|---|---|---:|---:|---:|
| `k05_l36_f02_correct_narrow` | 235 | L36/F2 | answer=235 | — | 6.88% | 7.33% | -0.45 pp |
| `k10_l36_f02_wrong_sibling` | 185 | L36/F2 | — | — | 6.54% | 7.87% | -1.33 pp |
| `k25_l36_f10_requested_intermediates` | 185 | L36/F10 | bound_value=125 | bound_value=125 | 6.17% | 7.52% | -1.35 pp |
| `k25_l38_f21_wrong_answer` | 185 | L38/F21 | distractor_answer=185 | distractor_answer=185 | 7.42% | 7.69% | -0.27 pp |
| `k50_l31_f14_joint_candidates` | 235 | L31/F14 | answer=235 | answer=235 | 5.87% | 7.43% | -1.57 pp |
| `k50_l31_f25_same_layer_control` | 235 | L31/F25 | — | — | 5.69% | 7.52% | -1.83 pp |
| `k50_l33_f43_requested_product` | 235 | L33/F43 | second_product=250 | — | 6.99% | 7.45% | -0.46 pp |
| `k50_l15_f14_early_control` | 235 | L15/F14 | — | — | 5.52% | 4.08% | +1.45 pp |
| `k100_l33_f19_requested_product` | 235 | L33/F19 | second_product=250 | second_product=250 | 6.21% | 7.60% | -1.40 pp |
| `k100_l36_f19_joint_candidates` | 235 | L36/F19 | answer=235 | answer=235 | 8.69% | 7.33% | +1.36 pp |

## Reconstruction and controls

Raw J-space reconstruction explains `5.52–8.69%` of squared activation norm across the ten sites (mean `6.60%`). The mean Haar-orthogonal relative-orientation control explains `7.18%`; observed minus control is negative on `8/10` sites. Therefore the raw percentage must not be presented as above-chance J-space variance for these activations.

The sparse logit-space baseline explains `7.05%` on average versus `6.60%` for J-space. Only `6.3/25` atoms overlap on average, so Jacobian transport materially changes the selected dictionary support, but does not improve reconstruction in this selected sample.

Two selected task atoms are J-space-only in this sample: answer `235` at k=5/L36/F2 and product `250` at k=50/L33/F43. This is suggestive of a J-specific interpretive benefit, but the cells were preselected with J-Lens, so it is not an unbiased performance comparison.

## Complete atoms by site

### k05_l36_f02_correct_narrow

Correct narrow-workspace regime: J-Lens answer 235 is rank 1 and sibling answer 185 is rank 16.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"235"` | 0.8844 | 4.6709 | 1 |
| 2 | `"�"` | 0.5341 | 3.0564 | 4 |
| 3 | `"ogene"` | 0.4826 | 2.4344 | 28 |
| 4 | `" ترك"` | 0.5772 | 2.8091 | 94 |
| 5 | `"冰雪"` | 0.4592 | 2.7792 | 20 |
| 6 | `" torn"` | 0.5614 | 2.8253 | 19 |
| 7 | `"お"` | 0.7829 | 2.5790 | 1549 |
| 8 | `"得很"` | 0.5518 | 2.2467 | 427 |
| 9 | `"कार"` | 0.6680 | 2.8488 | 208 |
| 10 | `"otechnical"` | 0.5313 | 2.6843 | 54 |
| 11 | `"大海"` | 0.4214 | 2.3462 | 46 |
| 12 | `"思路"` | 0.5038 | 2.4089 | 130 |
| 13 | `" ."` | 1.0379 | 2.8332 | 9652 |
| 14 | `"园长"` | 0.4419 | 2.3927 | 74 |
| 15 | `"ilig"` | 0.4924 | 3.0431 | 129 |
| 16 | `" postup"` | 0.4771 | 2.2361 | 147 |
| 17 | `"崇拜"` | 0.4794 | 2.4448 | 110 |
| 18 | `"诊所"` | 0.4324 | 2.2819 | 416 |
| 19 | `".).\n\n"` | 0.6961 | 1.7626 | 10520 |
| 20 | `"不尽"` | 0.3999 | 2.4576 | 51 |
| 21 | `"ahoo"` | 0.4463 | 2.3897 | 156 |
| 22 | `"用了"` | 0.4725 | 2.0345 | 646 |
| 23 | `" defaults"` | 0.4029 | 2.2859 | 1421 |
| 24 | `" perturb"` | 0.3416 | 1.8702 | 143 |
| 25 | `"认"` | 0.2757 | 1.6386 | 169 |

### k10_l36_f02_wrong_sibling

Incorrect regime: sibling-consistent answer 185 is rank 7 while requested answer 235 is rank 2608.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"165"` | 0.6760 | 3.5763 | 3 |
| 2 | `"ographs"` | 0.6440 | 3.7173 | 4 |
| 3 | `"态势"` | 0.6931 | 3.3029 | 35 |
| 4 | `"温暖"` | 0.6702 | 3.4414 | 13 |
| 5 | `" strukt"` | 0.5808 | 2.9270 | 10 |
| 6 | `"成了"` | 0.6475 | 2.7754 | 257 |
| 7 | `"佩服"` | 0.6388 | 2.9721 | 136 |
| 8 | `" generator"` | 0.4186 | 2.5144 | 34 |
| 9 | `"场比赛"` | 0.5783 | 2.9247 | 30 |
| 10 | `" Labour"` | 0.4672 | 2.7796 | 95 |
| 11 | `" enclosing"` | 0.5306 | 2.6560 | 25 |
| 12 | `"�"` | 0.4214 | 2.6236 | 182 |
| 13 | `"ота"` | 0.5420 | 2.5800 | 61 |
| 14 | `" non"` | 0.6028 | 2.6497 | 761 |
| 15 | `"疑惑"` | 0.5971 | 2.9556 | 64 |
| 16 | `"历史"` | 0.4659 | 2.4810 | 80 |
| 17 | `"#####"` | 0.8123 | 2.4093 | 2606 |
| 18 | `"acin"` | 0.3993 | 2.5011 | 22 |
| 19 | `"oze"` | 0.5119 | 3.1601 | 14 |
| 20 | `" ها"` | 0.6386 | 1.8300 | 3803 |
| 21 | `"医生"` | 0.5347 | 2.5248 | 249 |
| 22 | `"翻"` | 0.4093 | 2.3237 | 143 |
| 23 | `"技术在"` | 0.4611 | 2.1976 | 72 |
| 24 | `"認"` | 0.3327 | 1.8836 | 227 |
| 25 | `"寓言"` | 0.3333 | 1.8150 | 141 |

### k25_l36_f10_requested_intermediates

Incorrect output despite a clean requested route: bound 125 is rank 1 and product 250 is rank 2.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"125"` | 0.8359 | 4.3892 | 1 |
| 2 | `"去掉"` | 0.4972 | 2.5445 | 4 |
| 3 | `"ота"` | 0.5150 | 2.4514 | 141 |
| 4 | `"运用"` | 0.5465 | 2.4137 | 128 |
| 5 | `"俯"` | 0.4404 | 2.5423 | 8 |
| 6 | `"alski"` | 0.3447 | 1.9508 | 5 |
| 7 | `" thrilling"` | 0.5434 | 2.3838 | 209 |
| 8 | `"新娘"` | 0.3943 | 2.0997 | 32 |
| 9 | `" Wil"` | 0.4461 | 2.6982 | 10 |
| 10 | `"师徒"` | 0.3853 | 2.2690 | 28 |
| 11 | `"atzen"` | 0.4174 | 2.1420 | 124 |
| 12 | `"言辞"` | 0.4199 | 2.0277 | 161 |
| 13 | `" \\"` | 0.7473 | 2.2197 | 2106 |
| 14 | `"市场化"` | 0.3797 | 2.1281 | 40 |
| 15 | `"不急"` | 0.3571 | 1.9245 | 189 |
| 16 | `"我有"` | 0.5809 | 2.2229 | 1285 |
| 17 | `" examined"` | 0.4314 | 2.0005 | 459 |
| 18 | `" intelligence"` | 0.3814 | 2.0424 | 131 |
| 19 | `"支持"` | 0.3811 | 2.1130 | 35 |
| 20 | `" nac"` | 0.3604 | 2.0091 | 98 |
| 21 | `" loose"` | 0.3707 | 2.0022 | 12 |
| 22 | `"radesh"` | 0.2976 | 2.0265 | 67 |
| 23 | `"计算方法"` | 0.3552 | 1.9777 | 30 |
| 24 | `" Heidelberg"` | 0.3352 | 1.8215 | 229 |
| 25 | `" prescription"` | 0.3391 | 1.8422 | 85 |

### k25_l38_f21_wrong_answer

Incorrect regime answer state: sibling answer 185 is rank 1 and requested answer 235 is rank 26.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"185"` | 1.0012 | 5.0892 | 1 |
| 2 | `"оже"` | 0.6485 | 3.0055 | 25 |
| 3 | `"教育教学"` | 0.6319 | 2.7789 | 16 |
| 4 | `"富士"` | 0.5626 | 2.8716 | 21 |
| 5 | `"记述"` | 0.5984 | 2.5631 | 32 |
| 6 | `"团的"` | 0.5234 | 2.5559 | 58 |
| 7 | `"疑问"` | 0.6188 | 2.5697 | 123 |
| 8 | `"ark"` | 0.4989 | 2.3366 | 120 |
| 9 | `"迎面"` | 0.6643 | 2.8566 | 529 |
| 10 | `" postup"` | 0.6766 | 2.7067 | 95 |
| 11 | `" sweat"` | 0.5825 | 2.8781 | 495 |
| 12 | `"离开"` | 0.6048 | 2.4862 | 375 |
| 13 | `"银杏"` | 0.5151 | 2.6701 | 66 |
| 14 | `" War"` | 0.5533 | 2.5593 | 141 |
| 15 | `"clud"` | 0.6165 | 2.6270 | 297 |
| 16 | `"常务"` | 0.5714 | 2.5320 | 195 |
| 17 | `" "` | 1.3905 | 3.0204 | 28773 |
| 18 | `"nahmen"` | 0.5973 | 2.4013 | 188 |
| 19 | `"电影的"` | 0.5322 | 2.4444 | 101 |
| 20 | `"轻松"` | 0.5661 | 2.3327 | 363 |
| 21 | `" Elk"` | 0.4706 | 2.4110 | 219 |
| 22 | `" Mär"` | 0.4636 | 2.3177 | 152 |
| 23 | `" ST"` | 0.5210 | 2.5822 | 3284 |
| 24 | `"овые"` | 0.6331 | 2.0961 | 1643 |
| 25 | `"\\).\n\n"` | 0.3176 | 0.7688 | 11589 |

### k50_l31_f14_joint_candidates

Correct regime with both candidates in one readout: requested 235 is rank 1 and sibling 185 is rank 2.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"235"` | 0.4578 | 2.7878 | 1 |
| 2 | `"الع"` | 0.3464 | 1.4866 | 311 |
| 3 | `"と"` | 0.6900 | 1.7725 | 2942 |
| 4 | `"参赛"` | 0.2441 | 1.4559 | 41 |
| 5 | `" maximal"` | 0.2104 | 1.3280 | 14 |
| 6 | `" dripping"` | 0.3376 | 2.2208 | 16 |
| 7 | `"五十"` | 0.2968 | 1.5954 | 77 |
| 8 | `" Dir"` | 0.2101 | 1.3754 | 39 |
| 9 | `"表的"` | 0.2384 | 1.5167 | 33 |
| 10 | `" concerned"` | 0.2682 | 1.4820 | 207 |
| 11 | `" advantage"` | 0.2718 | 1.6185 | 95 |
| 12 | `" basal"` | 0.2564 | 1.6764 | 21 |
| 13 | `"ре"` | 0.3410 | 1.3092 | 1664 |
| 14 | `"市场"` | 0.2715 | 1.4416 | 94 |
| 15 | `" pod"` | 0.2412 | 1.3890 | 115 |
| 16 | `"鸦片"` | 0.2737 | 1.5964 | 466 |
| 17 | `" Is"` | 0.3172 | 1.3322 | 955 |
| 18 | `"�"` | 0.2771 | 1.2529 | 637 |
| 19 | `"院"` | 0.2273 | 1.3398 | 170 |
| 20 | `"acos"` | 0.1837 | 1.3372 | 17 |
| 21 | `" backward"` | 0.2231 | 1.5130 | 35 |
| 22 | `"疑难"` | 0.2139 | 1.2555 | 529 |
| 23 | `"有待"` | 0.2271 | 1.1663 | 599 |
| 24 | `" ==="` | 0.1827 | 0.9649 | 836 |
| 25 | `"舍弃"` | 0.1617 | 1.0205 | 486 |

### k50_l31_f25_same_layer_control

Same prompt and layer as the joint-candidate cell, but a nonselected filler destination.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"kur"` | 0.5070 | 3.3654 | 1 |
| 2 | `" first"` | 0.6902 | 2.9518 | 185 |
| 3 | `"算出"` | 0.3845 | 2.3818 | 11 |
| 4 | `" passo"` | 0.3297 | 1.8893 | 141 |
| 5 | `" KV"` | 0.2736 | 1.8970 | 332 |
| 6 | `" Re"` | 0.4359 | 2.0021 | 852 |
| 7 | `"遵循"` | 0.3727 | 2.1461 | 2529 |
| 8 | `" aus"` | 0.4196 | 2.1222 | 191 |
| 9 | `" sik"` | 0.3180 | 2.1194 | 3714 |
| 10 | `" verk"` | 0.3170 | 1.9910 | 25 |
| 11 | `"เริ่ม"` | 0.4065 | 1.8563 | 1525 |
| 12 | `" baseline"` | 0.2987 | 1.7982 | 1081 |
| 13 | `"私下"` | 0.3173 | 1.9295 | 950 |
| 14 | `" consuming"` | 0.2787 | 1.7383 | 295 |
| 15 | `" fat"` | 0.2994 | 2.1730 | 14124 |
| 16 | `"一试"` | 0.2846 | 1.7918 | 147 |
| 17 | `" ك"` | 0.4195 | 1.3589 | 3116 |
| 18 | `"没有被"` | 0.2799 | 1.6649 | 1503 |
| 19 | `"进宫"` | 0.2972 | 1.9979 | 8463 |
| 20 | `"R"` | 0.3433 | 1.4019 | 1868 |
| 21 | `" quote"` | 0.2691 | 1.6933 | 2350 |
| 22 | `"kä"` | 0.2382 | 1.5553 | 7 |
| 23 | `" Sure"` | 0.2697 | 1.4802 | 14112 |
| 24 | `"困扰"` | 0.2026 | 1.1231 | 1189 |
| 25 | `" ▲"` | 0.1311 | 0.6281 | 8363 |

### k50_l33_f43_requested_product

Correct requested-route intermediate: product 250 is J-Lens rank 1.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"250"` | 0.5387 | 3.0697 | 1 |
| 2 | `"二十五"` | 0.4441 | 2.4908 | 3 |
| 3 | `" maxima"` | 0.3707 | 2.2344 | 17 |
| 4 | `" сп"` | 0.6020 | 2.4944 | 2428 |
| 5 | `" dilation"` | 0.2853 | 1.8409 | 7 |
| 6 | `"平滑"` | 0.3848 | 2.7318 | 419 |
| 7 | `" tournament"` | 0.3707 | 2.1448 | 63 |
| 8 | `" excited"` | 0.3875 | 2.0778 | 232 |
| 9 | `" Katz"` | 0.3231 | 2.0057 | 299 |
| 10 | `"dit"` | 0.4067 | 2.1834 | 134 |
| 11 | `"言语"` | 0.4101 | 2.4169 | 645 |
| 12 | `"有期徒刑"` | 0.4525 | 2.1195 | 647 |
| 13 | `"�"` | 0.3432 | 2.2584 | 1804 |
| 14 | `"德国"` | 0.3801 | 2.2081 | 30 |
| 15 | `" tested"` | 0.3516 | 1.9259 | 1361 |
| 16 | `" came"` | 0.4391 | 2.0578 | 415 |
| 17 | `" indulge"` | 0.3970 | 2.3733 | 3938 |
| 18 | `"ing"` | 0.4231 | 2.0512 | 264 |
| 19 | `"算法的"` | 0.3500 | 2.0295 | 706 |
| 20 | `" popcorn"` | 0.3063 | 2.1029 | 25 |
| 21 | `"anation"` | 0.3391 | 2.0625 | 4145 |
| 22 | `"班子"` | 0.3166 | 1.7663 | 367 |
| 23 | `" underwater"` | 0.2879 | 1.7849 | 2692 |
| 24 | `" employed"` | 0.2518 | 1.3373 | 359 |
| 25 | `" actionable"` | 0.1725 | 1.0619 | 1072 |

### k50_l15_f14_early_control

Same prompt and position as the joint-candidate cell before the observed workspace band.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"max"` | 0.0364 | 0.3930 | 37664 |
| 2 | `" Nelson"` | 0.0516 | 0.5145 | 40362 |
| 3 | `"wait"` | 0.0355 | 0.4100 | 42849 |
| 4 | `"水中"` | 0.0355 | 0.3397 | 44717 |
| 5 | `"满天"` | 0.0309 | 0.3426 | 42560 |
| 6 | `" �"` | 0.0369 | 0.3647 | 50685 |
| 7 | `"生生的"` | 0.0319 | 0.4433 | 43318 |
| 8 | `"rib"` | 0.0299 | 0.3014 | 47828 |
| 9 | `"抗拒"` | 0.0325 | 0.4936 | 36865 |
| 10 | `"ಾ"` | 0.0384 | 0.3659 | 50791 |
| 11 | `" Liberty"` | 0.0356 | 0.4116 | 48320 |
| 12 | `"enog"` | 0.0323 | 0.5244 | 42584 |
| 13 | `" Calculation"` | 0.0283 | 0.3575 | 40458 |
| 14 | `"土"` | 0.0251 | 0.2726 | 52408 |
| 15 | `"反映"` | 0.0230 | 0.2845 | 46293 |
| 16 | `"一阵"` | 0.0259 | 0.3324 | 56464 |
| 17 | `"Fa"` | 0.0212 | 0.3054 | 38525 |
| 18 | `" Tal"` | 0.0239 | 0.3250 | 56679 |
| 19 | `"or"` | 0.0188 | 0.2213 | 38881 |
| 20 | `" World"` | 0.0161 | 0.1548 | 45864 |
| 21 | `" other"` | 0.0160 | 0.2583 | 37581 |
| 22 | `"精"` | 0.0129 | 0.1746 | 56099 |
| 23 | `"设为"` | 0.0101 | 0.1583 | 40669 |
| 24 | `"我刚"` | 0.0069 | 0.1425 | 57466 |
| 25 | `"姓名"` | 0.0040 | 0.0563 | 38043 |

### k100_l33_f19_requested_product

Wide correct-workspace regime: requested product 250 is J-Lens rank 1.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"250"` | 0.5621 | 3.2033 | 1 |
| 2 | `" leave"` | 0.3812 | 2.2247 | 50 |
| 3 | `"涌现"` | 0.3346 | 1.7759 | 174 |
| 4 | `"腹膜"` | 0.3647 | 2.1872 | 93 |
| 5 | `" Intelligence"` | 0.3207 | 1.9025 | 57 |
| 6 | `"大水"` | 0.2703 | 1.9164 | 4 |
| 7 | `" polynomials"` | 0.3592 | 2.2663 | 1332 |
| 8 | `" ها"` | 0.5060 | 1.6108 | 3207 |
| 9 | `"الع"` | 0.4167 | 1.6960 | 2025 |
| 10 | `" \\"` | 0.5676 | 2.0697 | 2640 |
| 11 | `"解脱"` | 0.2961 | 1.9037 | 801 |
| 12 | `"有话"` | 0.3039 | 1.8744 | 100 |
| 13 | `" gel"` | 0.3237 | 1.9358 | 146 |
| 14 | `" employed"` | 0.3496 | 1.8567 | 201 |
| 15 | `" Zel"` | 0.3238 | 2.3092 | 1149 |
| 16 | `"行为"` | 0.2876 | 1.7068 | 126 |
| 17 | `"孜"` | 0.2957 | 1.6611 | 387 |
| 18 | `"ise"` | 0.3111 | 1.5897 | 549 |
| 19 | `"ре"` | 0.3799 | 1.4053 | 5970 |
| 20 | `" भ"` | 0.3133 | 1.0169 | 2645 |
| 21 | `"arket"` | 0.2833 | 1.8603 | 783 |
| 22 | `" Dit"` | 0.2582 | 1.4189 | 223 |
| 23 | `" fifty"` | 0.2642 | 1.3995 | 75 |
| 24 | `"长青"` | 0.2139 | 1.3826 | 273 |
| 25 | `" computational"` | 0.1567 | 0.9122 | 366 |

### k100_l36_f19_joint_candidates

Wide correct-workspace regime with requested answer 235 rank 1 and sibling answer 185 rank 2.

| Order | Token | Coefficient | Contribution norm | J-readout rank |
|---:|---|---:|---:|---:|
| 1 | `"235"` | 1.5295 | 8.0774 | 1 |
| 2 | `"离开"` | 0.7761 | 3.8964 | 11 |
| 3 | `"浊"` | 0.7685 | 4.4869 | 14 |
| 4 | `"ahoo"` | 0.7464 | 3.9965 | 28 |
| 5 | `" Markov"` | 0.7691 | 4.4252 | 18 |
| 6 | `"得太"` | 0.7872 | 3.6590 | 203 |
| 7 | `"\u0005"` | 0.9048 | 3.4603 | 380 |
| 8 | `"cost"` | 0.7501 | 4.2526 | 58 |
| 9 | `"тина"` | 0.8146 | 3.7091 | 148 |
| 10 | `"有期徒刑"` | 0.9574 | 3.9695 | 686 |
| 11 | `" trends"` | 0.8818 | 4.6035 | 24 |
| 12 | `"松开"` | 0.7781 | 4.3346 | 143 |
| 13 | `" Clean"` | 0.6979 | 4.1878 | 16 |
| 14 | `"欠缺"` | 0.7398 | 3.6250 | 298 |
| 15 | `"�"` | 0.6081 | 3.5088 | 225 |
| 16 | `"搞"` | 0.7982 | 3.7375 | 304 |
| 17 | `" educated"` | 0.7387 | 3.6218 | 160 |
| 18 | `"<｜place▁holder▁no▁571｜>"` | 0.6470 | 3.1993 | 241 |
| 19 | `" ubang"` | 0.7422 | 3.8571 | 280 |
| 20 | `"石窟"` | 0.5462 | 3.0373 | 2044 |
| 21 | `"赛车"` | 0.7131 | 3.8120 | 107 |
| 22 | `" an"` | 0.6771 | 1.7450 | 20836 |
| 23 | `" controversy"` | 0.6731 | 3.2313 | 178 |
| 24 | `"操作"` | 0.4748 | 2.8030 | 567 |
| 25 | `"国民党"` | 0.4838 | 2.4188 | 138 |
