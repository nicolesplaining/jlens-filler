# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `119` (correct).
- No-filler answer: `115` (incorrect).
- Filler tokens: 50 tokens at absolute indices 516–565.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `fact_1=21` | 1 (L35, filler 41) | L35, filler 37 (rank 5) |
| J-Lens | `fact_2=6` | 1 (L35, filler 13) | L34, filler 13 (rank 6) |
| J-Lens | `fact_3=92` | 1 (L35, filler 29) | L35, filler 1 (rank 6) |
| J-Lens | `prefix_sum_12=27` | 5 (L31, filler 16) | L31, filler 1 (rank 9) |
| J-Lens | `sum=119` | 12 (L38, filler 4) | Never |
| Logit lens | `fact_1=21` | 1 (L35, filler 41) | L35, filler 41 (rank 1) |
| Logit lens | `fact_2=6` | 2 (L34, filler 13) | L31, filler 13 (rank 4) |
| Logit lens | `fact_3=92` | 1 (L36, filler 29) | L35, filler 9 (rank 7) |
| Logit lens | `prefix_sum_12=27` | 2 (L31, filler 37) | L31, filler 1 (rank 7) |
| Logit lens | `sum=119` | 16 (L39, filler 40) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 516, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: fact_1=21:120838, fact_2=6:125110, fact_3=92:117683, prefix_sum_12=27:120411, sum=119:114154)
- Layer 10: `anta`, `locked`, `fine`, `s`, `Walker` (target ranks: fact_1=21:35360, fact_2=6:27489, fact_3=92:48017, prefix_sum_12=27:47326, sum=119:51960)
- Layer 20: `足`, `表面`, `甸`, `重`, `梯` (target ranks: fact_1=21:935, fact_2=6:64, fact_3=92:2424, prefix_sum_12=27:3559, sum=119:23649)
- Layer 30: ` pakig`, ` talags`, `akang`, ` gilay`, `得分` (target ranks: fact_1=21:7358, fact_2=6:37385, fact_3=92:2156, prefix_sum_12=27:200, sum=119:32896)
- Layer 35: `93`, `88`, `78`, `33`, `87` (target ranks: fact_1=21:544, fact_2=6:8027, fact_3=92:6, prefix_sum_12=27:28, sum=119:14858)
- Layer 36: `93`, `88`, `87`, `92`, `78` (target ranks: fact_1=21:16314, fact_2=6:48978, fact_3=92:4, prefix_sum_12=27:309, sum=119:12165)
- Layer 37: `92`, `93`, `88`, `91`, `}<?` (target ranks: fact_1=21:38319, fact_2=6:111113, fact_3=92:1, prefix_sum_12=27:17563, sum=119:8089)
- Layer 38: `}<?`, `92`, `93`, ` soft`, ` softening` (target ranks: fact_1=21:99860, fact_2=6:119133, fact_3=92:2, prefix_sum_12=27:122442, sum=119:8372)
- Layer 39: `}<?`, `odea`, `tanle`, `音符`, ` smoothing` (target ranks: fact_1=21:24913, fact_2=6:127870, fact_3=92:30367, prefix_sum_12=27:120165, sum=119:20686)
- Layer 40: ` talags`, ` atomic`, `atomic`, ` smoothing`, ` overwhelming` (target ranks: fact_1=21:791, fact_2=6:116542, fact_3=92:2833, prefix_sum_12=27:92163, sum=119:8944)
- Layer 41: ` .`, `耘`, `我已经`, ` .↵↵`, ` ..` (target ranks: fact_1=21:8667, fact_2=6:52392, fact_3=92:17273, prefix_sum_12=27:49174, sum=119:29462)

### Filler position 2 (absolute token 517, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: fact_1=21:122683, fact_2=6:125205, fact_3=92:120537, prefix_sum_12=27:120729, sum=119:118344)
- Layer 10: ` Walker`, `从哪里`, `Walker`, `atile`, `ait` (target ranks: fact_1=21:17329, fact_2=6:6640, fact_3=92:27723, prefix_sum_12=27:19155, sum=119:41064)
- Layer 20: ` .----`, `往常`, ` Millenniums`, `াথে`, `ologists` (target ranks: fact_1=21:126338, fact_2=6:124879, fact_3=92:129060, prefix_sum_12=27:128128, sum=119:129227)
- Layer 30: ` talags`, ` hilabihan`, ` dekameters`, ` gilay`, ` pakig` (target ranks: fact_1=21:124272, fact_2=6:124133, fact_3=92:129204, prefix_sum_12=27:128733, sum=119:128690)
- Layer 35: ` hilabihan`, ` .`, `}<?`, ` talags`, `enclose` (target ranks: fact_1=21:119401, fact_2=6:123834, fact_3=92:128612, prefix_sum_12=27:125797, sum=119:128427)
- Layer 36: ` hilabihan`, ` .`, ` talags`, `enclose`, `停` (target ranks: fact_1=21:70104, fact_2=6:70119, fact_3=92:121819, prefix_sum_12=27:87389, sum=119:121418)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, `aplenty`, ` Erkännande` (target ranks: fact_1=21:124433, fact_2=6:127728, fact_3=92:128064, prefix_sum_12=27:123579, sum=119:123696)
- Layer 38: ` .`, `}<?`, ` hilabihan`, ` .↵↵`, `繁体` (target ranks: fact_1=21:107746, fact_2=6:125680, fact_3=92:127525, prefix_sum_12=27:118198, sum=119:121749)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` +:+`, `}<?` (target ranks: fact_1=21:124749, fact_2=6:125689, fact_3=92:127856, prefix_sum_12=27:123678, sum=119:124597)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: fact_1=21:100150, fact_2=6:88207, fact_3=92:122096, prefix_sum_12=27:93111, sum=119:107237)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `美` (target ranks: fact_1=21:66700, fact_2=6:29889, fact_3=92:95378, prefix_sum_12=27:28951, sum=119:76264)

### Filler position 3 (absolute token 518, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:125037, fact_2=6:127326, fact_3=92:123100, prefix_sum_12=27:123668, sum=119:119623)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: fact_1=21:8572, fact_2=6:3843, fact_3=92:11909, prefix_sum_12=27:10035, sum=119:22157)
- Layer 20: ` calculator`, `�`, `足`, `ka`, ` ` (target ranks: fact_1=21:751, fact_2=6:583, fact_3=92:4554, prefix_sum_12=27:6859, sum=119:26478)
- Layer 30: ` atomic`, `atomic`, ` Scand`, ` Atomic`, `Atomic` (target ranks: fact_1=21:20665, fact_2=6:20834, fact_3=92:54742, prefix_sum_12=27:34342, sum=119:33411)
- Layer 35: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `原子` (target ranks: fact_1=21:2095, fact_2=6:9052, fact_3=92:13928, prefix_sum_12=27:13835, sum=119:17821)
- Layer 36: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `原子` (target ranks: fact_1=21:6227, fact_2=6:13695, fact_3=92:24881, prefix_sum_12=27:15686, sum=119:17952)
- Layer 37: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `原子` (target ranks: fact_1=21:21587, fact_2=6:81690, fact_3=92:82308, prefix_sum_12=27:54911, sum=119:31695)
- Layer 38: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `�` (target ranks: fact_1=21:20696, fact_2=6:88783, fact_3=92:84732, prefix_sum_12=27:49866, sum=119:34800)
- Layer 39: ` atomic`, `.Sc`, ` Sc`, `atomic`, `/sc` (target ranks: fact_1=21:32268, fact_2=6:121302, fact_3=92:118921, prefix_sum_12=27:112078, sum=119:96958)
- Layer 40: ` atomic`, `atomic`, ` Ne`, `�`, `外壳` (target ranks: fact_1=21:1022, fact_2=6:91283, fact_3=92:94540, prefix_sum_12=27:67631, sum=119:73274)
- Layer 41: ` .`, ` atomic`, `袄`, `atomic`, `人人都` (target ranks: fact_1=21:1718, fact_2=6:33660, fact_3=92:68770, prefix_sum_12=27:32243, sum=119:49302)

### Filler position 4 (absolute token 519, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=21:125558, fact_2=6:127520, fact_3=92:123407, prefix_sum_12=27:124067, sum=119:120493)
- Layer 10: ` Walker`, `ait`, `Walker`, `锁定`, `忑` (target ranks: fact_1=21:12282, fact_2=6:5665, fact_3=92:17871, prefix_sum_12=27:13987, sum=119:26725)
- Layer 20: `ait`, `cape`, ` ES`, `能被`, ` LS` (target ranks: fact_1=21:14211, fact_2=6:2063, fact_3=92:21746, prefix_sum_12=27:21301, sum=119:49244)
- Layer 30: `一百`, `}<?`, `Conc`, `turn`, `109` (target ranks: fact_1=21:5006, fact_2=6:27983, fact_3=92:256, prefix_sum_12=27:3110, sum=119:1122)
- Layer 35: `136`, `138`, `打法`, ` calculator`, `286` (target ranks: fact_1=21:5989, fact_2=6:5810, fact_3=92:33, prefix_sum_12=27:11770, sum=119:110)
- Layer 36: `109`, `138`, `136`, `114`, `107` (target ranks: fact_1=21:24700, fact_2=6:17662, fact_3=92:46, prefix_sum_12=27:30721, sum=119:23)
- Layer 37: `92`, `292`, `uran`, `109`, `本题分析` (target ranks: fact_1=21:33183, fact_2=6:52816, fact_3=92:1, prefix_sum_12=27:80039, sum=119:21)
- Layer 38: `}<?`, `本题分析`, `109`, ` transcend`, `/Tropical` (target ranks: fact_1=21:57270, fact_2=6:93063, fact_3=92:18, prefix_sum_12=27:106493, sum=119:12)
- Layer 39: `}<?`, `本题分析`, `东海`, ` mempun`, `opters` (target ranks: fact_1=21:94226, fact_2=6:123396, fact_3=92:80159, prefix_sum_12=27:127721, sum=119:122)
- Layer 40: `Ald`, ` atomic`, ` Ald`, ` ald`, `重在` (target ranks: fact_1=21:44061, fact_2=6:91890, fact_3=92:61758, prefix_sum_12=27:125294, sum=119:811)
- Layer 41: ` .`, `Answer`, `�`, ` fused`, `样子` (target ranks: fact_1=21:14798, fact_2=6:20909, fact_3=92:55706, prefix_sum_12=27:91263, sum=119:4217)

### Filler position 5 (absolute token 520, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=21:125369, fact_2=6:127317, fact_3=92:123033, prefix_sum_12=27:123686, sum=119:120352)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, `挪` (target ranks: fact_1=21:11125, fact_2=6:5422, fact_3=92:16666, prefix_sum_12=27:13723, sum=119:26525)
- Layer 20: ` LS`, `能被`, `幽`, `挪`, `LS` (target ranks: fact_1=21:3145, fact_2=6:438, fact_3=92:8838, prefix_sum_12=27:5885, sum=119:22689)
- Layer 30: ` pakig`, `}<?`, `acons`, ` uranium`, `carbon` (target ranks: fact_1=21:5652, fact_2=6:15095, fact_3=92:14300, prefix_sum_12=27:1074, sum=119:35112)
- Layer 35: `88`, `92`, `86`, `opan`, `ianhi` (target ranks: fact_1=21:185, fact_2=6:2326, fact_3=92:2, prefix_sum_12=27:437, sum=119:6346)
- Layer 36: `88`, `92`, `}<?`, `87`, `89` (target ranks: fact_1=21:6349, fact_2=6:21446, fact_3=92:2, prefix_sum_12=27:4264, sum=119:8387)
- Layer 37: `92`, `88`, ` ninety`, `93`, `九十` (target ranks: fact_1=21:30420, fact_2=6:89007, fact_3=92:1, prefix_sum_12=27:53066, sum=119:7013)
- Layer 38: `92`, `98`, ` ninety`, `}<?`, ` soft` (target ranks: fact_1=21:94237, fact_2=6:118348, fact_3=92:1, prefix_sum_12=27:127425, sum=119:5600)
- Layer 39: `98`, `<｜place▁holder▁no▁703｜>`, `}<?`, `东海`, `098` (target ranks: fact_1=21:47745, fact_2=6:126648, fact_3=92:4173, prefix_sum_12=27:124994, sum=119:1375)
- Layer 40: ` atomic`, `atomic`, ` Atomic`, `98`, `大意` (target ranks: fact_1=21:3467, fact_2=6:114113, fact_3=92:418, prefix_sum_12=27:119374, sum=119:786)
- Layer 41: ` atomic`, `atomic`, `新时代中国特色社会主义`, ` dekameters`, `原子` (target ranks: fact_1=21:4974, fact_2=6:42841, fact_3=92:17049, prefix_sum_12=27:106888, sum=119:16908)

### Filler position 6 (absolute token 521, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=21:125032, fact_2=6:127071, fact_3=92:122672, prefix_sum_12=27:123162, sum=119:119893)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:9950, fact_2=6:4279, fact_3=92:12868, prefix_sum_12=27:10785, sum=119:23381)
- Layer 20: `足`, `鞍`, `cape`, `ting`, `距` (target ranks: fact_1=21:7723, fact_2=6:3546, fact_3=92:15304, prefix_sum_12=27:18360, sum=119:42777)
- Layer 30: `tap`, ` Answer`, `回答`, `Answer`, ` answer` (target ranks: fact_1=21:3298, fact_2=6:2988, fact_3=92:1863, prefix_sum_12=27:7849, sum=119:34801)
- Layer 35: `acks`, `足`, ` smile`, ` tib`, ` repetition` (target ranks: fact_1=21:545, fact_2=6:1497, fact_3=92:488, prefix_sum_12=27:385, sum=119:2261)
- Layer 36: `acks`, `agli`, ` stabil`, ` anxious`, `容易出现` (target ranks: fact_1=21:3202, fact_2=6:9561, fact_3=92:2843, prefix_sum_12=27:1257, sum=119:4840)
- Layer 37: `acks`, `agli`, `�`, ` decom`, `反思` (target ranks: fact_1=21:10721, fact_2=6:29439, fact_3=92:6273, prefix_sum_12=27:5071, sum=119:2807)
- Layer 38: ` Rutherford`, ` talags`, ` pakig`, ` RES`, ` RESP` (target ranks: fact_1=21:30880, fact_2=6:44972, fact_3=92:13330, prefix_sum_12=27:16499, sum=119:2002)
- Layer 39: `<｜begin▁of▁sentence｜>`, `ophe`, ` Rutherford`, ` Dominic`, `ulum` (target ranks: fact_1=21:116469, fact_2=6:124745, fact_3=92:111738, prefix_sum_12=27:127589, sum=119:29149)
- Layer 40: `<｜begin▁of▁sentence｜>`, `ophe`, ` Rutherford`, ` talags`, `资` (target ranks: fact_1=21:109567, fact_2=6:115007, fact_3=92:100347, prefix_sum_12=27:127944, sum=119:19413)
- Layer 41: ` .`, `人人都`, `试一试`, ` Rutherford`, ` dotted` (target ranks: fact_1=21:93348, fact_2=6:102962, fact_3=92:108559, prefix_sum_12=27:125781, sum=119:73342)

### Filler position 7 (absolute token 522, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=21:124910, fact_2=6:126954, fact_3=92:122544, prefix_sum_12=27:122935, sum=119:119809)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:9809, fact_2=6:4359, fact_3=92:13239, prefix_sum_12=27:10983, sum=119:23677)
- Layer 20: ` smile`, `锁定`, ` cheer`, `ait`, `us` (target ranks: fact_1=21:2830, fact_2=6:777, fact_3=92:4967, prefix_sum_12=27:4473, sum=119:20203)
- Layer 30: ` consum`, `s`, ` receptive`, `Tap`, ` Riv` (target ranks: fact_1=21:1524, fact_2=6:7570, fact_3=92:960, prefix_sum_12=27:1919, sum=119:2182)
- Layer 35: `Tap`, ` tap`, `保留`, ` Tap`, ` future` (target ranks: fact_1=21:176, fact_2=6:2048, fact_3=92:110, prefix_sum_12=27:198, sum=119:109)
- Layer 36: `anium`, `保留`, `匹配`, ` tap`, `容易出现` (target ranks: fact_1=21:3191, fact_2=6:15247, fact_3=92:615, prefix_sum_12=27:1032, sum=119:127)
- Layer 37: `anium`, `}<?`, ` Erkännande`, ` pakig`, ` talags` (target ranks: fact_1=21:17992, fact_2=6:60724, fact_3=92:490, prefix_sum_12=27:10254, sum=119:137)
- Layer 38: `}<?`, `ucl`, ` pakig`, `斋`, ` Erkännande` (target ranks: fact_1=21:56462, fact_2=6:102522, fact_3=92:6147, prefix_sum_12=27:33630, sum=119:616)
- Layer 39: `}<?`, `hemer`, `osit`, `osos`, `词的` (target ranks: fact_1=21:99554, fact_2=6:124892, fact_3=92:101758, prefix_sum_12=27:120789, sum=119:12763)
- Layer 40: ` aure`, `装`, `资`, `anium`, ` anxious` (target ranks: fact_1=21:77137, fact_2=6:101738, fact_3=92:92641, prefix_sum_12=27:118765, sum=119:9743)
- Layer 41: ` .`, `文明实践`, ` uninter`, `太多了`, `有下列` (target ranks: fact_1=21:70420, fact_2=6:89939, fact_3=92:105546, prefix_sum_12=27:111253, sum=119:35753)

### Filler position 8 (absolute token 523, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=21:124851, fact_2=6:126902, fact_3=92:122556, prefix_sum_12=27:122787, sum=119:119676)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=21:7539, fact_2=6:2954, fact_3=92:10891, prefix_sum_12=27:8860, sum=119:20554)
- Layer 20: `锁定`, `ait`, `足`, `拆`, ` smile` (target ranks: fact_1=21:4242, fact_2=6:1145, fact_3=92:10811, prefix_sum_12=27:8297, sum=119:29363)
- Layer 30: `sum`, ` summing`, ` suma`, `加起来`, ` сумма` (target ranks: fact_1=21:22596, fact_2=6:8702, fact_3=92:57246, prefix_sum_12=27:32635, sum=119:68871)
- Layer 35: `sum`, ` suma`, ` Sum`, ` calculator`, `Sum` (target ranks: fact_1=21:3350, fact_2=6:756, fact_3=92:21774, prefix_sum_12=27:4563, sum=119:20910)
- Layer 36: ` Sum`, `sum`, `Sum`, ` sum`, ` sums` (target ranks: fact_1=21:11332, fact_2=6:2978, fact_3=92:49157, prefix_sum_12=27:13041, sum=119:23634)
- Layer 37: ` Sum`, ` sum`, `Sum`, `sum`, ` sums` (target ranks: fact_1=21:26600, fact_2=6:15511, fact_3=92:83236, prefix_sum_12=27:24889, sum=119:34621)
- Layer 38: ` Sum`, ` sum`, `sum`, `Sum`, ` sums` (target ranks: fact_1=21:28720, fact_2=6:18385, fact_3=92:81540, prefix_sum_12=27:11055, sum=119:45895)
- Layer 39: ` Sum`, `}<?`, ` sum`, `osum`, `Sum` (target ranks: fact_1=21:77355, fact_2=6:89315, fact_3=92:112253, prefix_sum_12=27:88296, sum=119:86220)
- Layer 40: `atomic`, ` Rutherford`, `珍珠`, ` `, `留存` (target ranks: fact_1=21:25197, fact_2=6:23637, fact_3=92:107881, prefix_sum_12=27:47878, sum=119:52724)
- Layer 41: ` .`, `我曾经`, `<｜end▁of▁sentence｜>`, `鹉`, ` ` (target ranks: fact_1=21:52197, fact_2=6:17456, fact_3=92:94737, prefix_sum_12=27:48222, sum=119:55883)

### Filler position 9 (absolute token 524, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124405, fact_2=6:126532, fact_3=92:122139, prefix_sum_12=27:122204, sum=119:119096)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=21:7636, fact_2=6:2933, fact_3=92:10972, prefix_sum_12=27:8767, sum=119:20467)
- Layer 20: `锁定`, `挪`, ` ternary`, `能被`, `ait` (target ranks: fact_1=21:1908, fact_2=6:527, fact_3=92:4530, prefix_sum_12=27:2593, sum=119:14307)
- Layer 30: `加起来`, `相加`, `合计`, `33`, ` cumulative` (target ranks: fact_1=21:8607, fact_2=6:29673, fact_3=92:1257, prefix_sum_12=27:46, sum=119:8155)
- Layer 35: `88`, `93`, `92`, `86`, `78` (target ranks: fact_1=21:5276, fact_2=6:9381, fact_3=92:3, prefix_sum_12=27:55, sum=119:1200)
- Layer 36: `93`, `88`, `92`, `86`, `89` (target ranks: fact_1=21:55018, fact_2=6:52587, fact_3=92:3, prefix_sum_12=27:1230, sum=119:300)
- Layer 37: `92`, `93`, `88`, `91`, `九十` (target ranks: fact_1=21:75858, fact_2=6:99569, fact_3=92:1, prefix_sum_12=27:31881, sum=119:272)
- Layer 38: `}<?`, `92`, `98`, `107`, `93` (target ranks: fact_1=21:111059, fact_2=6:112902, fact_3=92:2, prefix_sum_12=27:122346, sum=119:135)
- Layer 39: `}<?`, `107`, `<｜place▁holder▁no▁703｜>`, `<｜place▁holder▁no▁691｜>`, `<｜place▁holder▁no▁693｜>` (target ranks: fact_1=21:21587, fact_2=6:122801, fact_3=92:685, prefix_sum_12=27:105214, sum=119:431)
- Layer 40: `<｜begin▁of▁file｜>`, `}<?`, ` atomic`, `atomic`, `uker` (target ranks: fact_1=21:1030, fact_2=6:108948, fact_3=92:335, prefix_sum_12=27:86815, sum=119:646)
- Layer 41: `癫�`, ` atomic`, `<｜begin▁of▁file｜>`, `我曾经`, `出不穷` (target ranks: fact_1=21:3347, fact_2=6:36727, fact_3=92:4163, prefix_sum_12=27:74474, sum=119:16058)

### Filler position 10 (absolute token 525, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124516, fact_2=6:126661, fact_3=92:122475, prefix_sum_12=27:122287, sum=119:119306)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:7811, fact_2=6:2992, fact_3=92:11729, prefix_sum_12=27:9309, sum=119:21663)
- Layer 20: `胃癌`, `挪`, `足`, `cape`, `幽` (target ranks: fact_1=21:2020, fact_2=6:577, fact_3=92:6203, prefix_sum_12=27:3199, sum=119:22412)
- Layer 30: `Tap`, ` tap`, ` Tap`, `acin`, `西洋` (target ranks: fact_1=21:4593, fact_2=6:2994, fact_3=92:29660, prefix_sum_12=27:2792, sum=119:43917)
- Layer 35: `Sc`, `atomic`, ` atomic`, ` Scand`, ` Sc` (target ranks: fact_1=21:435, fact_2=6:1673, fact_3=92:26046, prefix_sum_12=27:1640, sum=119:37234)
- Layer 36: `Sc`, ` Scand`, ` atomic`, `atomic`, ` Sc` (target ranks: fact_1=21:1333, fact_2=6:7833, fact_3=92:64794, prefix_sum_12=27:4018, sum=119:40375)
- Layer 37: ` atomic`, `atomic`, ` Scand`, ` Atomic`, `Sc` (target ranks: fact_1=21:3428, fact_2=6:49012, fact_3=92:108752, prefix_sum_12=27:16519, sum=119:69566)
- Layer 38: ` Scand`, ` atomic`, `atomic`, `�`, `}<?` (target ranks: fact_1=21:88, fact_2=6:70564, fact_3=92:115421, prefix_sum_12=27:20861, sum=119:57462)
- Layer 39: ` Scand`, ` Sc`, `Sc`, `.Sc`, `斯科` (target ranks: fact_1=21:2205, fact_2=6:99750, fact_3=92:120914, prefix_sum_12=27:85652, sum=119:80611)
- Layer 40: `atomic`, ` Scand`, `Sc`, ` atomic`, `scr` (target ranks: fact_1=21:187, fact_2=6:33063, fact_3=92:98384, prefix_sum_12=27:36508, sum=119:52503)
- Layer 41: `atomic`, ` .`, ` atomic`, `鹉`, ` ` (target ranks: fact_1=21:122, fact_2=6:4004, fact_3=92:57519, prefix_sum_12=27:9551, sum=119:23576)

### Filler position 11 (absolute token 526, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124639, fact_2=6:126677, fact_3=92:122556, prefix_sum_12=27:122253, sum=119:119545)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:7196, fact_2=6:2759, fact_3=92:11356, prefix_sum_12=27:8961, sum=119:20990)
- Layer 20: `锁定`, `挪`, `ait`, ` smile`, ` Wig` (target ranks: fact_1=21:2774, fact_2=6:920, fact_3=92:6527, prefix_sum_12=27:4271, sum=119:19584)
- Layer 30: `幽`, ` Cogn`, `Walker`, ` future`, `future` (target ranks: fact_1=21:3304, fact_2=6:7919, fact_3=92:4533, prefix_sum_12=27:3176, sum=119:20671)
- Layer 35: `锁定`, ` future`, ` Cogn`, ` labor`, `future` (target ranks: fact_1=21:4006, fact_2=6:4932, fact_3=92:700, prefix_sum_12=27:3939, sum=119:5941)
- Layer 36: ` consuming`, `冰冰`, `któber`, `}<?`, ` Lob` (target ranks: fact_1=21:37678, fact_2=6:46640, fact_3=92:3462, prefix_sum_12=27:40637, sum=119:3435)
- Layer 37: `}<?`, `Quintal`, `?datasetId`, `ajes`, `图画` (target ranks: fact_1=21:76029, fact_2=6:111874, fact_3=92:1005, prefix_sum_12=27:97726, sum=119:8239)
- Layer 38: `}<?`, `ucl`, `iota`, `?datasetId`, `图画` (target ranks: fact_1=21:89626, fact_2=6:118719, fact_3=92:13367, prefix_sum_12=27:118907, sum=119:8927)
- Layer 39: `}<?`, `叶子`, `防护`, `ocyst`, `东海` (target ranks: fact_1=21:90711, fact_2=6:125689, fact_3=92:114349, prefix_sum_12=27:123795, sum=119:373)
- Layer 40: `}<?`, `装`, `amn`, `冰冰`, `水土` (target ranks: fact_1=21:21476, fact_2=6:102407, fact_3=92:75473, prefix_sum_12=27:106772, sum=119:299)
- Layer 41: `鹉`, ` .`, `太多了`, `atomic`, ` atomic` (target ranks: fact_1=21:16307, fact_2=6:48790, fact_3=92:80191, prefix_sum_12=27:80460, sum=119:6094)

### Filler position 12 (absolute token 527, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124513, fact_2=6:126594, fact_3=92:122601, prefix_sum_12=27:122119, sum=119:119400)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:6532, fact_2=6:2241, fact_3=92:10116, prefix_sum_12=27:7744, sum=119:19791)
- Layer 20: `锁定`, `ait`, `挪`, ` smile`, ` Walker` (target ranks: fact_1=21:5402, fact_2=6:1435, fact_3=92:9546, prefix_sum_12=27:7461, sum=119:29336)
- Layer 30: `重复`, ` repetition`, ` repetitions`, ` repeated`, ` repetitive` (target ranks: fact_1=21:26194, fact_2=6:1032, fact_3=92:58620, prefix_sum_12=27:42731, sum=119:68010)
- Layer 35: `重复`, ` repetition`, ` repeated`, `询问`, ` repetitions` (target ranks: fact_1=21:10552, fact_2=6:871, fact_3=92:46044, prefix_sum_12=27:16417, sum=119:45403)
- Layer 36: ` repeated`, `重复`, `询问`, ` tap`, `Tap` (target ranks: fact_1=21:15143, fact_2=6:2064, fact_3=92:43057, prefix_sum_12=27:15014, sum=119:32764)
- Layer 37: `提问`, `冰冰`, ` repeated`, `}<?`, ` tap` (target ranks: fact_1=21:52895, fact_2=6:17434, fact_3=92:98013, prefix_sum_12=27:46453, sum=119:59500)
- Layer 38: `}<?`, `acons`, `冰冰`, `累`, ` polar` (target ranks: fact_1=21:82872, fact_2=6:44021, fact_3=92:112161, prefix_sum_12=27:74193, sum=119:76611)
- Layer 39: `}<?`, `acons`, `<｜begin▁of▁sentence｜>`, `�乐`, `ocyst` (target ranks: fact_1=21:92274, fact_2=6:115533, fact_3=92:115334, prefix_sum_12=27:102010, sum=119:71489)
- Layer 40: `冰冰`, ` .`, ` capsule`, `acl`, `acons` (target ranks: fact_1=21:39144, fact_2=6:70565, fact_3=92:97767, prefix_sum_12=27:54968, sum=119:43758)
- Layer 41: ` .`, `鹉`, `猕猴`, `矶`, ` ` (target ranks: fact_1=21:30641, fact_2=6:23375, fact_3=92:63431, prefix_sum_12=27:27523, sum=119:19182)

### Filler position 13 (absolute token 528, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124635, fact_2=6:126726, fact_3=92:122803, prefix_sum_12=27:122218, sum=119:119489)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7857, fact_2=6:3091, fact_3=92:12111, prefix_sum_12=27:9338, sum=119:21504)
- Layer 20: ` LS`, `挪`, `锁定`, `LS`, `ative` (target ranks: fact_1=21:1739, fact_2=6:421, fact_3=92:5970, prefix_sum_12=27:3105, sum=119:14958)
- Layer 30: `obin`, ` labor`, ` Heim`, ` Cogn`, `碳` (target ranks: fact_1=21:2923, fact_2=6:403, fact_3=92:24592, prefix_sum_12=27:2448, sum=119:32688)
- Layer 35: `6`, ` six`, ` Six`, `six`, `-six` (target ranks: fact_1=21:39440, fact_2=6:1, fact_3=92:74376, prefix_sum_12=27:28189, sum=119:66384)
- Layer 36: `6`, ` six`, ` Sixth`, ` Six`, `six` (target ranks: fact_1=21:89136, fact_2=6:1, fact_3=92:97750, prefix_sum_12=27:68647, sum=119:69607)
- Layer 37: ` Sixth`, ` sixth`, ` six`, ` šest`, ` Six` (target ranks: fact_1=21:122456, fact_2=6:6, fact_3=92:119911, prefix_sum_12=27:116763, sum=119:89956)
- Layer 38: ` Sixth`, ` sixth`, ` šest`, ` Six`, `六` (target ranks: fact_1=21:120836, fact_2=6:7, fact_3=92:114063, prefix_sum_12=27:112176, sum=119:76719)
- Layer 39: ` Sixth`, ` Six`, `六`, ` sixth`, ` šest` (target ranks: fact_1=21:55443, fact_2=6:72, fact_3=92:119551, prefix_sum_12=27:105992, sum=119:87518)
- Layer 40: `atomic`, ` atomic`, ` Atomic`, ` Six`, `装` (target ranks: fact_1=21:8722, fact_2=6:11, fact_3=92:78893, prefix_sum_12=27:92824, sum=119:56745)
- Layer 41: `atomic`, ` atomic`, ` .`, `装`, `鹉` (target ranks: fact_1=21:7350, fact_2=6:90, fact_3=92:49086, prefix_sum_12=27:54068, sum=119:35303)

### Filler position 14 (absolute token 529, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=21:124802, fact_2=6:126762, fact_3=92:123085, prefix_sum_12=27:122175, sum=119:119836)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7381, fact_2=6:2900, fact_3=92:11523, prefix_sum_12=27:8301, sum=119:20894)
- Layer 20: `ait`, `锁定`, `挪`, `cape`, `us` (target ranks: fact_1=21:2658, fact_2=6:818, fact_3=92:11375, prefix_sum_12=27:4804, sum=119:25134)
- Layer 30: ` Heim`, `obin`, `平行`, `ayi`, `碳` (target ranks: fact_1=21:7021, fact_2=6:1906, fact_3=92:37200, prefix_sum_12=27:5817, sum=119:60377)
- Layer 35: `6`, ` Six`, ` six`, `six`, `六` (target ranks: fact_1=21:69859, fact_2=6:1, fact_3=92:70580, prefix_sum_12=27:55214, sum=119:89206)
- Layer 36: `6`, ` Six`, ` six`, ` Sixth`, `Six` (target ranks: fact_1=21:113175, fact_2=6:1, fact_3=92:110978, prefix_sum_12=27:99267, sum=119:98777)
- Layer 37: ` Sixth`, ` Six`, ` šest`, ` six`, ` sixth` (target ranks: fact_1=21:127357, fact_2=6:9, fact_3=92:125874, prefix_sum_12=27:125322, sum=119:113947)
- Layer 38: ` Sixth`, `ocyst`, `ocarbon`, `carbon`, ` šest` (target ranks: fact_1=21:126254, fact_2=6:59, fact_3=92:123532, prefix_sum_12=27:122889, sum=119:108578)
- Layer 39: `}<?`, `ocyst`, `osit`, ` Sixth`, ` Rutherford` (target ranks: fact_1=21:76279, fact_2=6:6082, fact_3=92:125995, prefix_sum_12=27:118084, sum=119:111605)
- Layer 40: `atomic`, ` atomic`, ` Atomic`, ` Rutherford`, `Atomic` (target ranks: fact_1=21:10115, fact_2=6:2664, fact_3=92:97227, prefix_sum_12=27:98439, sum=119:75178)
- Layer 41: `atomic`, ` atomic`, ` .`, ` Atomic`, `装` (target ranks: fact_1=21:8180, fact_2=6:2143, fact_3=92:68406, prefix_sum_12=27:56097, sum=119:52255)

### Filler position 15 (absolute token 530, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125021, fact_2=6:126945, fact_3=92:123600, prefix_sum_12=27:122430, sum=119:120255)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7370, fact_2=6:2923, fact_3=92:11630, prefix_sum_12=27:8294, sum=119:21374)
- Layer 20: `锁定`, `挪`, `ait`, ` LS`, ` Walker` (target ranks: fact_1=21:1727, fact_2=6:506, fact_3=92:6318, prefix_sum_12=27:2341, sum=119:15371)
- Layer 30: `acos`, `adic`, `acin`, `三十六`, `aci` (target ranks: fact_1=21:1435, fact_2=6:6450, fact_3=92:7540, prefix_sum_12=27:145, sum=119:24612)
- Layer 35: `28`, `apan`, `烟的`, ` pan`, `adic` (target ranks: fact_1=21:776, fact_2=6:1121, fact_3=92:735, prefix_sum_12=27:16, sum=119:9069)
- Layer 36: `38`, `三十六`, ` pan`, `二十八`, `二十九` (target ranks: fact_1=21:21741, fact_2=6:15368, fact_3=92:5921, prefix_sum_12=27:78, sum=119:24988)
- Layer 37: `92`, `uran`, `93`, `91`, `89` (target ranks: fact_1=21:39334, fact_2=6:96958, fact_3=92:1, prefix_sum_12=27:8908, sum=119:5804)
- Layer 38: `92`, `党群`, `天尊`, `九天`, ` ninety` (target ranks: fact_1=21:70169, fact_2=6:119644, fact_3=92:1, prefix_sum_12=27:101922, sum=119:5689)
- Layer 39: `东海`, `<｜place▁holder▁no▁703｜>`, `宰`, `uran`, `现金` (target ranks: fact_1=21:36063, fact_2=6:91869, fact_3=92:17904, prefix_sum_12=27:113441, sum=119:1894)
- Layer 40: ` atomic`, `atomic`, `uran`, ` Atomic`, `党群` (target ranks: fact_1=21:7120, fact_2=6:35277, fact_3=92:2103, prefix_sum_12=27:78440, sum=119:2662)
- Layer 41: ` atomic`, `atomic`, `原子`, ` .`, `我曾经` (target ranks: fact_1=21:5531, fact_2=6:3155, fact_3=92:7945, prefix_sum_12=27:48725, sum=119:15882)

### Filler position 16 (absolute token 531, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:124959, fact_2=6:126838, fact_3=92:123590, prefix_sum_12=27:122122, sum=119:120425)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7419, fact_2=6:2922, fact_3=92:11981, prefix_sum_12=27:8686, sum=119:21332)
- Layer 20: `ait`, ` LS`, ` ternary`, `锁定`, `LS` (target ranks: fact_1=21:982, fact_2=6:116, fact_3=92:2301, prefix_sum_12=27:1040, sum=119:8425)
- Layer 30: ` uranium`, `acos`, `uran`, `aci`, ` Rac` (target ranks: fact_1=21:3675, fact_2=6:32581, fact_3=92:305, prefix_sum_12=27:30, sum=119:5445)
- Layer 35: `88`, `93`, `78`, `89`, `87` (target ranks: fact_1=21:297, fact_2=6:2892, fact_3=92:12, prefix_sum_12=27:15, sum=119:2877)
- Layer 36: `88`, `93`, `apan`, `87`, ` pan` (target ranks: fact_1=21:7558, fact_2=6:20306, fact_3=92:11, prefix_sum_12=27:60, sum=119:1367)
- Layer 37: `92`, `93`, `91`, `89`, `88` (target ranks: fact_1=21:18508, fact_2=6:77303, fact_3=92:1, prefix_sum_12=27:7909, sum=119:261)
- Layer 38: `}<?`, `92`, `107`, `93`, `105` (target ranks: fact_1=21:100970, fact_2=6:106816, fact_3=92:2, prefix_sum_12=27:97111, sum=119:1336)
- Layer 39: `105`, `107`, `104`, `102`, `108` (target ranks: fact_1=21:37074, fact_2=6:108248, fact_3=92:5276, prefix_sum_12=27:101453, sum=119:4092)
- Layer 40: `<｜begin▁of▁file｜>`, ` atomic`, `uker`, `atomic`, `auri` (target ranks: fact_1=21:2929, fact_2=6:81399, fact_3=92:1183, prefix_sum_12=27:74041, sum=119:6064)
- Layer 41: ` atomic`, `我曾经`, `atomic`, `因为这些`, `癫�` (target ranks: fact_1=21:4143, fact_2=6:6863, fact_3=92:5325, prefix_sum_12=27:50337, sum=119:27553)

### Filler position 17 (absolute token 532, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125089, fact_2=6:126914, fact_3=92:123696, prefix_sum_12=27:122259, sum=119:120510)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8988, fact_2=6:3905, fact_3=92:14066, prefix_sum_12=27:10689, sum=119:23213)
- Layer 20: `锁定`, `胃癌`, ` smile`, ` Walker`, `Walker` (target ranks: fact_1=21:5640, fact_2=6:1601, fact_3=92:13432, prefix_sum_12=27:8411, sum=119:24085)
- Layer 30: `acos`, `支配`, ` ES`, ` appendix`, ` reserved` (target ranks: fact_1=21:14248, fact_2=6:28770, fact_3=92:55402, prefix_sum_12=27:63465, sum=119:72717)
- Layer 35: `�`, ` cadmium`, ` plut`, ` Rh`, `铂` (target ranks: fact_1=21:6018, fact_2=6:11830, fact_3=92:49652, prefix_sum_12=27:42968, sum=119:44108)
- Layer 36: `�`, ` plut`, ` Rh`, `铂`, `anium` (target ranks: fact_1=21:14880, fact_2=6:13497, fact_3=92:15714, prefix_sum_12=27:36223, sum=119:19775)
- Layer 37: `�`, ` plut`, `�`, ` Plut`, `�` (target ranks: fact_1=21:48523, fact_2=6:52834, fact_3=92:32531, prefix_sum_12=27:84350, sum=119:18203)
- Layer 38: `�`, ` plut`, ` Plut`, `�`, ` Rutherford` (target ranks: fact_1=21:62672, fact_2=6:69143, fact_3=92:51595, prefix_sum_12=27:77948, sum=119:28538)
- Layer 39: `�`, ` Plut`, ` plut`, ` Cur`, ` cur` (target ranks: fact_1=21:45875, fact_2=6:75976, fact_3=92:73712, prefix_sum_12=27:68708, sum=119:46885)
- Layer 40: `�`, ` Rutherford`, `B`, `翻`, `坏的` (target ranks: fact_1=21:15949, fact_2=6:8584, fact_3=92:55641, prefix_sum_12=27:31010, sum=119:11771)
- Layer 41: ` .`, `less`, ` `, ` fused`, `�` (target ranks: fact_1=21:3193, fact_2=6:119, fact_3=92:8983, prefix_sum_12=27:4960, sum=119:5348)

### Filler position 18 (absolute token 533, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125253, fact_2=6:127006, fact_3=92:124046, prefix_sum_12=27:122323, sum=119:121013)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8010, fact_2=6:3296, fact_3=92:12477, prefix_sum_12=27:9341, sum=119:22531)
- Layer 20: ` Walker`, `锁定`, `Walker`, `ait`, ` smile` (target ranks: fact_1=21:6610, fact_2=6:3325, fact_3=92:15127, prefix_sum_12=27:7656, sum=119:28851)
- Layer 30: `�`, `幽`, `鞍`, `拆`, `Tap` (target ranks: fact_1=21:6809, fact_2=6:2768, fact_3=92:18309, prefix_sum_12=27:6435, sum=119:28082)
- Layer 35: `羊`, `aty`, ` atomic`, `锁定`, ` Atomic` (target ranks: fact_1=21:1985, fact_2=6:1460, fact_3=92:6506, prefix_sum_12=27:1790, sum=119:10647)
- Layer 36: `羊`, `留存`, ` atomic`, ` Atomic`, `atomic` (target ranks: fact_1=21:6252, fact_2=6:3523, fact_3=92:16162, prefix_sum_12=27:3055, sum=119:8771)
- Layer 37: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `}<?` (target ranks: fact_1=21:24005, fact_2=6:36202, fact_3=92:47808, prefix_sum_12=27:15257, sum=119:16213)
- Layer 38: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `zat` (target ranks: fact_1=21:20026, fact_2=6:46635, fact_3=92:43240, prefix_sum_12=27:6791, sum=119:22164)
- Layer 39: ` atomic`, ` Atomic`, `}<?`, `atomic`, `�` (target ranks: fact_1=21:8886, fact_2=6:85181, fact_3=92:80556, prefix_sum_12=27:28883, sum=119:54458)
- Layer 40: ` atomic`, `atomic`, `eland`, `留存`, ` Atomic` (target ranks: fact_1=21:730, fact_2=6:33695, fact_3=92:39576, prefix_sum_12=27:5859, sum=119:30169)
- Layer 41: ` atomic`, `atomic`, ` .`, ` `, `鹉` (target ranks: fact_1=21:445, fact_2=6:1035, fact_3=92:14137, prefix_sum_12=27:855, sum=119:14458)

### Filler position 19 (absolute token 534, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125347, fact_2=6:127044, fact_3=92:124193, prefix_sum_12=27:122434, sum=119:121093)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7559, fact_2=6:2967, fact_3=92:11769, prefix_sum_12=27:8628, sum=119:21232)
- Layer 20: `ait`, `锁定`, ` Walker`, `拆`, `足` (target ranks: fact_1=21:5558, fact_2=6:3518, fact_3=92:14329, prefix_sum_12=27:7793, sum=119:30336)
- Layer 30: ` Scand`, `scan`, `斯卡`, `Scan`, ` SC` (target ranks: fact_1=21:10190, fact_2=6:10357, fact_3=92:37690, prefix_sum_12=27:12574, sum=119:50472)
- Layer 35: `Sc`, ` Scand`, `斯卡`, ` SC`, ` Sc` (target ranks: fact_1=21:3349, fact_2=6:7395, fact_3=92:29909, prefix_sum_12=27:5599, sum=119:24712)
- Layer 36: `Sc`, ` SC`, ` Scand`, `SC`, `羊` (target ranks: fact_1=21:7988, fact_2=6:13537, fact_3=92:45073, prefix_sum_12=27:9044, sum=119:19152)
- Layer 37: ` Scand`, ` SC`, ` atomic`, `Sc`, `SC` (target ranks: fact_1=21:23015, fact_2=6:78541, fact_3=92:91946, prefix_sum_12=27:29424, sum=119:33449)
- Layer 38: ` Scand`, `}<?`, `�`, ` atomic`, `scr` (target ranks: fact_1=21:25707, fact_2=6:94486, fact_3=92:91600, prefix_sum_12=27:28535, sum=119:41149)
- Layer 39: `�`, `}<?`, ` atomic`, `atomic`, ` Scand` (target ranks: fact_1=21:19361, fact_2=6:106768, fact_3=92:100504, prefix_sum_12=27:44476, sum=119:60242)
- Layer 40: `atomic`, ` atomic`, `�`, `留存`, `anium` (target ranks: fact_1=21:1747, fact_2=6:54508, fact_3=92:57628, prefix_sum_12=27:11129, sum=119:26875)
- Layer 41: ` atomic`, `atomic`, ` .`, ` Atomic`, ` ` (target ranks: fact_1=21:898, fact_2=6:4295, fact_3=92:27767, prefix_sum_12=27:2104, sum=119:14980)

### Filler position 20 (absolute token 535, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125410, fact_2=6:127101, fact_3=92:124479, prefix_sum_12=27:122442, sum=119:121275)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7312, fact_2=6:2845, fact_3=92:11163, prefix_sum_12=27:8309, sum=119:19693)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, ` engaging` (target ranks: fact_1=21:6608, fact_2=6:4319, fact_3=92:17236, prefix_sum_12=27:10113, sum=119:37224)
- Layer 30: `Sc`, ` Scand`, ` SC`, `斯卡`, ` Sc` (target ranks: fact_1=21:5175, fact_2=6:7735, fact_3=92:35697, prefix_sum_12=27:8252, sum=119:83002)
- Layer 35: `Sc`, ` Scand`, ` Sc`, ` SC`, `斯卡` (target ranks: fact_1=21:127, fact_2=6:12571, fact_3=92:42951, prefix_sum_12=27:6151, sum=119:66414)
- Layer 36: `Sc`, ` Scand`, ` SC`, ` Sc`, `SC` (target ranks: fact_1=21:387, fact_2=6:22072, fact_3=92:60778, prefix_sum_12=27:12443, sum=119:51162)
- Layer 37: ` Scand`, `Sc`, ` Sc`, ` SC`, `SC` (target ranks: fact_1=21:497, fact_2=6:92830, fact_3=92:103754, prefix_sum_12=27:41274, sum=119:77354)
- Layer 38: ` Scand`, ` Sc`, `Sc`, `二十一`, `21` (target ranks: fact_1=21:5, fact_2=6:114361, fact_3=92:120481, prefix_sum_12=27:39082, sum=119:80235)
- Layer 39: ` Scand`, ` Sc`, `Sc`, ` SC`, ` scand` (target ranks: fact_1=21:303, fact_2=6:123656, fact_3=92:125518, prefix_sum_12=27:100475, sum=119:106650)
- Layer 40: ` Scand`, ` Sc`, `Sc`, `atomic`, ` Uran` (target ranks: fact_1=21:991, fact_2=6:107064, fact_3=92:122449, prefix_sum_12=27:85777, sum=119:97516)
- Layer 41: ` atomic`, `atomic`, ` uranium`, ` Uran`, `Sc` (target ranks: fact_1=21:491, fact_2=6:16362, fact_3=92:94086, prefix_sum_12=27:32801, sum=119:82888)

### Filler position 21 (absolute token 536, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125137, fact_2=6:126951, fact_3=92:124346, prefix_sum_12=27:122107, sum=119:120929)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:7374, fact_2=6:2920, fact_3=92:11342, prefix_sum_12=27:8567, sum=119:19945)
- Layer 20: `锁定`, `ait`, ` Walker`, `能被`, `Walker` (target ranks: fact_1=21:9362, fact_2=6:5067, fact_3=92:22372, prefix_sum_12=27:14611, sum=119:37363)
- Layer 30: ` gold`, ` neon`, ` Ne`, ` Gold`, ` Thor` (target ranks: fact_1=21:13532, fact_2=6:16036, fact_3=92:20494, prefix_sum_12=27:20082, sum=119:52625)
- Layer 35: ` Ne`, ` neon`, ` Neon`, `Ne`, ` gold` (target ranks: fact_1=21:6300, fact_2=6:5286, fact_3=92:17988, prefix_sum_12=27:11210, sum=119:46384)
- Layer 36: ` Ne`, ` neon`, ` Neon`, ` gold`, ` Gold` (target ranks: fact_1=21:14254, fact_2=6:11466, fact_3=92:23035, prefix_sum_12=27:19505, sum=119:25890)
- Layer 37: ` gold`, ` Gold`, `gold`, `Gold`, ` prot` (target ranks: fact_1=21:50654, fact_2=6:50296, fact_3=92:57298, prefix_sum_12=27:51156, sum=119:46883)
- Layer 38: ` Gold`, ` gold`, `gold`, `Gold`, `�` (target ranks: fact_1=21:66219, fact_2=6:56437, fact_3=92:67566, prefix_sum_12=27:52874, sum=119:43244)
- Layer 39: `�`, ` Gold`, `gold`, ` gold`, ` boron` (target ranks: fact_1=21:81026, fact_2=6:90541, fact_3=92:100769, prefix_sum_12=27:90455, sum=119:89175)
- Layer 40: `�`, ` helium`, ` Rutherford`, `helium`, ` Uran` (target ranks: fact_1=21:36326, fact_2=6:32810, fact_3=92:84876, prefix_sum_12=27:59189, sum=119:53042)
- Layer 41: ` .`, `冰冰`, ` helium`, `anganese`, ` chromium` (target ranks: fact_1=21:13846, fact_2=6:1952, fact_3=92:41162, prefix_sum_12=27:21416, sum=119:44902)

### Filler position 22 (absolute token 537, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125234, fact_2=6:127009, fact_3=92:124559, prefix_sum_12=27:122134, sum=119:121157)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:6636, fact_2=6:2419, fact_3=92:10641, prefix_sum_12=27:7735, sum=119:19271)
- Layer 20: `ait`, `锁定`, ` smile`, `胃癌`, ` Walker` (target ranks: fact_1=21:4388, fact_2=6:1031, fact_3=92:9247, prefix_sum_12=27:6951, sum=119:24585)
- Layer 30: ` Ne`, ` gold`, `Ne`, ` Gold`, `Gold` (target ranks: fact_1=21:10250, fact_2=6:5153, fact_3=92:17403, prefix_sum_12=27:13432, sum=119:40028)
- Layer 35: ` Ne`, ` cobalt`, `Ne`, ` neon`, ` Neon` (target ranks: fact_1=21:4220, fact_2=6:2922, fact_3=92:16960, prefix_sum_12=27:3071, sum=119:44063)
- Layer 36: ` cobalt`, ` Ne`, ` gold`, ` Neon`, ` neon` (target ranks: fact_1=21:10824, fact_2=6:7992, fact_3=92:28815, prefix_sum_12=27:7666, sum=119:36966)
- Layer 37: ` cobalt`, ` gold`, `gold`, ` Gold`, `Gold` (target ranks: fact_1=21:39748, fact_2=6:39186, fact_3=92:72526, prefix_sum_12=27:23100, sum=119:60350)
- Layer 38: ` cobalt`, `gold`, ` Gold`, ` gold`, ` Ne` (target ranks: fact_1=21:56136, fact_2=6:51320, fact_3=92:85071, prefix_sum_12=27:30026, sum=119:56351)
- Layer 39: ` Gold`, `gold`, ` gold`, ` cobalt`, ` Ne` (target ranks: fact_1=21:45006, fact_2=6:92911, fact_3=92:109295, prefix_sum_12=27:69818, sum=119:99964)
- Layer 40: `冰冰`, `�`, ` cobalt`, `anium`, `俯` (target ranks: fact_1=21:9650, fact_2=6:33716, fact_3=92:94471, prefix_sum_12=27:36494, sum=119:62401)
- Layer 41: ` .`, `冰冰`, ` atomic`, ` `, `atomic` (target ranks: fact_1=21:3115, fact_2=6:1570, fact_3=92:53305, prefix_sum_12=27:15867, sum=119:56412)

### Filler position 23 (absolute token 538, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125489, fact_2=6:127186, fact_3=92:124886, prefix_sum_12=27:122406, sum=119:121655)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=21:7235, fact_2=6:2850, fact_3=92:11866, prefix_sum_12=27:8622, sum=119:20721)
- Layer 20: ` Tears`, `足`, `锁定`, `cape`, `幽` (target ranks: fact_1=21:2162, fact_2=6:691, fact_3=92:8133, prefix_sum_12=27:4951, sum=119:23963)
- Layer 30: `�`, `atan`, `西洋`, `Tap`, ` tap` (target ranks: fact_1=21:5345, fact_2=6:1210, fact_3=92:23796, prefix_sum_12=27:7637, sum=119:34745)
- Layer 35: `元素`, `�`, `羊`, `cape`, `斯卡` (target ranks: fact_1=21:5487, fact_2=6:2381, fact_3=92:34712, prefix_sum_12=27:10990, sum=119:30352)
- Layer 36: `元素`, `元素的`, `�`, ` Elements`, `Elements` (target ranks: fact_1=21:13418, fact_2=6:4366, fact_3=92:56025, prefix_sum_12=27:23489, sum=119:24025)
- Layer 37: `元素的`, `元素`, `atomic`, ` atomic`, ` Elements` (target ranks: fact_1=21:51495, fact_2=6:43897, fact_3=92:111014, prefix_sum_12=27:62723, sum=119:51212)
- Layer 38: `�`, ` atomic`, `atomic`, `}<?`, `zat` (target ranks: fact_1=21:70131, fact_2=6:65425, fact_3=92:115515, prefix_sum_12=27:74692, sum=119:62636)
- Layer 39: `�`, `atomic`, ` atomic`, `romic`, `�` (target ranks: fact_1=21:41540, fact_2=6:85260, fact_3=92:116772, prefix_sum_12=27:88519, sum=119:66554)
- Layer 40: `atomic`, ` atomic`, `�`, `坏`, `坏的` (target ranks: fact_1=21:6325, fact_2=6:21918, fact_3=92:88002, prefix_sum_12=27:46689, sum=119:35291)
- Layer 41: `atomic`, ` atomic`, ` .`, ` `, ` fused` (target ranks: fact_1=21:7610, fact_2=6:5411, fact_3=92:82710, prefix_sum_12=27:26233, sum=119:53584)

### Filler position 24 (absolute token 539, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125559, fact_2=6:127230, fact_3=92:124998, prefix_sum_12=27:122517, sum=119:121709)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=21:7049, fact_2=6:2629, fact_3=92:11071, prefix_sum_12=27:7929, sum=119:20445)
- Layer 20: ` smile`, `足`, ` LS`, `ative`, `甸` (target ranks: fact_1=21:3054, fact_2=6:837, fact_3=92:9423, prefix_sum_12=27:5687, sum=119:30543)
- Layer 30: `拆`, `Tap`, ` tap`, `�`, ` ternary` (target ranks: fact_1=21:10717, fact_2=6:1654, fact_3=92:33088, prefix_sum_12=27:11986, sum=119:44431)
- Layer 35: `Tap`, ` tap`, ` equation`, `足`, ` Tap` (target ranks: fact_1=21:4164, fact_2=6:1177, fact_3=92:36026, prefix_sum_12=27:7020, sum=119:33149)
- Layer 36: `加法`, `acin`, ` addition`, ` Sum`, `羊` (target ranks: fact_1=21:11701, fact_2=6:3802, fact_3=92:68124, prefix_sum_12=27:14726, sum=119:36018)
- Layer 37: `加法`, `adding`, ` addition`, `Addition`, `相加` (target ranks: fact_1=21:39453, fact_2=6:31210, fact_3=92:115775, prefix_sum_12=27:39224, sum=119:62864)
- Layer 38: ` Sum`, `adding`, ` addition`, `不加`, `osit` (target ranks: fact_1=21:70919, fact_2=6:60031, fact_3=92:121470, prefix_sum_12=27:63497, sum=119:70484)
- Layer 39: `<｜begin▁of▁sentence｜>`, `osit`, `}<?`, `�`, `hatic` (target ranks: fact_1=21:16731, fact_2=6:92686, fact_3=92:107594, prefix_sum_12=27:30964, sum=119:56159)
- Layer 40: `osit`, `eland`, ` embargo`, ` forty`, `冰冰` (target ranks: fact_1=21:1485, fact_2=6:29492, fact_3=92:76770, prefix_sum_12=27:6810, sum=119:19798)
- Layer 41: ` .`, ` `, `atomic`, `然而`, ` atomic` (target ranks: fact_1=21:3001, fact_2=6:3764, fact_3=92:56750, prefix_sum_12=27:3021, sum=119:28005)

### Filler position 25 (absolute token 540, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125555, fact_2=6:127205, fact_3=92:125019, prefix_sum_12=27:122455, sum=119:121777)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7973, fact_2=6:3237, fact_3=92:12762, prefix_sum_12=27:8981, sum=119:22172)
- Layer 20: `足`, ` smile`, `锁定`, `距`, `ait` (target ranks: fact_1=21:2823, fact_2=6:1124, fact_3=92:8198, prefix_sum_12=27:3762, sum=119:19354)
- Layer 30: `atomic`, ` atomic`, ` Atomic`, ` calculator`, `atan` (target ranks: fact_1=21:4570, fact_2=6:3023, fact_3=92:29391, prefix_sum_12=27:8829, sum=119:20652)
- Layer 35: ` atomic`, `atomic`, ` Scand`, `斯卡`, ` Atomic` (target ranks: fact_1=21:1052, fact_2=6:2756, fact_3=92:28621, prefix_sum_12=27:4344, sum=119:24140)
- Layer 36: ` atomic`, `atomic`, `scr`, ` Scand`, `羊` (target ranks: fact_1=21:4501, fact_2=6:8165, fact_3=92:46343, prefix_sum_12=27:7795, sum=119:21478)
- Layer 37: ` atomic`, `atomic`, ` Atomic`, `Atomic`, ` Scand` (target ranks: fact_1=21:1009, fact_2=6:68355, fact_3=92:73650, prefix_sum_12=27:15210, sum=119:21912)
- Layer 38: ` atomic`, `atomic`, ` Scand`, ` Atomic`, `Atomic` (target ranks: fact_1=21:241, fact_2=6:91039, fact_3=92:65488, prefix_sum_12=27:8432, sum=119:28077)
- Layer 39: ` atomic`, `atomic`, ` Scand`, ` Atomic`, `斯科` (target ranks: fact_1=21:59, fact_2=6:101418, fact_3=92:107198, prefix_sum_12=27:25240, sum=119:57869)
- Layer 40: `21`, ` Scand`, `二十一`, `eland`, `atomic` (target ranks: fact_1=21:1, fact_2=6:47672, fact_3=92:65945, prefix_sum_12=27:2414, sum=119:27807)
- Layer 41: `21`, ` atomic`, `atomic`, `二十一`, `不加` (target ranks: fact_1=21:1, fact_2=6:3298, fact_3=92:46891, prefix_sum_12=27:936, sum=119:22695)

### Filler position 26 (absolute token 541, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:125741, fact_2=6:127324, fact_3=92:125375, prefix_sum_12=27:122505, sum=119:122338)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7426, fact_2=6:2866, fact_3=92:11496, prefix_sum_12=27:8100, sum=119:20353)
- Layer 20: `ait`, ` Walker`, `锁定`, `拆`, `足` (target ranks: fact_1=21:5627, fact_2=6:2127, fact_3=92:10206, prefix_sum_12=27:7112, sum=119:24172)
- Layer 30: `atomic`, ` atomic`, `atri`, `atan`, `斯卡` (target ranks: fact_1=21:11423, fact_2=6:6412, fact_3=92:23048, prefix_sum_12=27:12016, sum=119:38693)
- Layer 35: ` Scand`, `Sc`, `斯卡`, ` atomic`, `atomic` (target ranks: fact_1=21:4713, fact_2=6:7429, fact_3=92:30751, prefix_sum_12=27:10896, sum=119:41225)
- Layer 36: ` Scand`, `Sc`, `SC`, `斯卡`, ` SC` (target ranks: fact_1=21:13857, fact_2=6:19245, fact_3=92:50658, prefix_sum_12=27:23146, sum=119:37825)
- Layer 37: ` Scand`, ` atomic`, `atomic`, ` Atomic`, ` scand` (target ranks: fact_1=21:25428, fact_2=6:88329, fact_3=92:91618, prefix_sum_12=27:56502, sum=119:49813)
- Layer 38: ` Scand`, ` atomic`, `atomic`, ` scand`, ` Atomic` (target ranks: fact_1=21:21359, fact_2=6:99977, fact_3=92:94182, prefix_sum_12=27:52113, sum=119:53188)
- Layer 39: ` Scand`, ` atomic`, `atomic`, `�`, ` scand` (target ranks: fact_1=21:5178, fact_2=6:103956, fact_3=92:106066, prefix_sum_12=27:46952, sum=119:63221)
- Layer 40: `atomic`, ` atomic`, ` Scand`, `eland`, `金黄` (target ranks: fact_1=21:187, fact_2=6:63117, fact_3=92:72442, prefix_sum_12=27:11078, sum=119:30346)
- Layer 41: `atomic`, ` atomic`, ` waterfall`, ` Atomic`, `不加` (target ranks: fact_1=21:33, fact_2=6:4735, fact_3=92:37239, prefix_sum_12=27:2299, sum=119:28068)

### Filler position 27 (absolute token 542, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `ivables` (target ranks: fact_1=21:125899, fact_2=6:127411, fact_3=92:125750, prefix_sum_12=27:122553, sum=119:122888)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7266, fact_2=6:2950, fact_3=92:11376, prefix_sum_12=27:8116, sum=119:19465)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `拆` (target ranks: fact_1=21:7310, fact_2=6:3183, fact_3=92:12808, prefix_sum_12=27:9699, sum=119:31871)
- Layer 30: ` labor`, `sett`, `粥`, `锁定`, `acin` (target ranks: fact_1=21:11030, fact_2=6:11613, fact_3=92:17703, prefix_sum_12=27:5799, sum=119:58312)
- Layer 35: `粥`, `锁定`, ` labor`, `重复`, ` tap` (target ranks: fact_1=21:10161, fact_2=6:7223, fact_3=92:33998, prefix_sum_12=27:2964, sum=119:65801)
- Layer 36: `粥`, `留存`, ` tap`, `水土`, `反复` (target ranks: fact_1=21:20430, fact_2=6:11164, fact_3=92:38160, prefix_sum_12=27:5345, sum=119:51407)
- Layer 37: `}<?`, `isis`, `装`, `不急`, `翻了` (target ranks: fact_1=21:70964, fact_2=6:70961, fact_3=92:91407, prefix_sum_12=27:31936, sum=119:70794)
- Layer 38: `}<?`, `坏`, `打磨`, `zat`, `acet` (target ranks: fact_1=21:69099, fact_2=6:67498, fact_3=92:102865, prefix_sum_12=27:27830, sum=119:86986)
- Layer 39: `}<?`, `打磨`, ` talags`, `铎`, `osit` (target ranks: fact_1=21:35521, fact_2=6:82838, fact_3=92:93643, prefix_sum_12=27:38160, sum=119:71694)
- Layer 40: `scr`, ` talags`, ` Rutherford`, `等待着`, ` .` (target ranks: fact_1=21:6510, fact_2=6:28297, fact_3=92:37662, prefix_sum_12=27:8802, sum=119:41720)
- Layer 41: ` .`, ` `, `等待`, `<｜end▁of▁sentence｜>`, ` .↵↵` (target ranks: fact_1=21:2663, fact_2=6:949, fact_3=92:19093, prefix_sum_12=27:2207, sum=119:11127)

### Filler position 28 (absolute token 543, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=21:125789, fact_2=6:127402, fact_3=92:125675, prefix_sum_12=27:122576, sum=119:122581)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:7117, fact_2=6:2817, fact_3=92:11273, prefix_sum_12=27:8084, sum=119:19053)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, `Walker` (target ranks: fact_1=21:5022, fact_2=6:2152, fact_3=92:11612, prefix_sum_12=27:7488, sum=119:27963)
- Layer 30: ` labor`, `锁定`, ` tap`, ` strike`, `Tap` (target ranks: fact_1=21:8021, fact_2=6:4349, fact_3=92:10469, prefix_sum_12=27:14501, sum=119:21274)
- Layer 35: ` tap`, `Tap`, ` Tap`, `锁定`, ` strike` (target ranks: fact_1=21:6052, fact_2=6:4194, fact_3=92:17155, prefix_sum_12=27:8708, sum=119:20047)
- Layer 36: ` tap`, `俯`, ` drip`, `tap`, ` strike` (target ranks: fact_1=21:14381, fact_2=6:9460, fact_3=92:26187, prefix_sum_12=27:13072, sum=119:13902)
- Layer 37: `}<?`, `装`, `acl`, `坏`, `isis` (target ranks: fact_1=21:56204, fact_2=6:49894, fact_3=92:69245, prefix_sum_12=27:44006, sum=119:21145)
- Layer 38: `}<?`, `zat`, `坏`, `ِّف`, `等待着` (target ranks: fact_1=21:60476, fact_2=6:53459, fact_3=92:79328, prefix_sum_12=27:54966, sum=119:18956)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ِّف`, `坏的`, `zat` (target ranks: fact_1=21:72451, fact_2=6:96366, fact_3=92:103032, prefix_sum_12=27:84502, sum=119:51481)
- Layer 40: `<｜begin▁of▁sentence｜>`, `scr`, `坏`, `坏的`, `等待着` (target ranks: fact_1=21:26975, fact_2=6:36780, fact_3=92:65541, prefix_sum_12=27:45501, sum=119:25192)
- Layer 41: ` .`, `等待`, `装`, ` waiting`, ` ` (target ranks: fact_1=21:9962, fact_2=6:2762, fact_3=92:32552, prefix_sum_12=27:11817, sum=119:9321)

### Filler position 29 (absolute token 544, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=21:125864, fact_2=6:127453, fact_3=92:125789, prefix_sum_12=27:122666, sum=119:122704)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:7347, fact_2=6:3008, fact_3=92:12141, prefix_sum_12=27:8832, sum=119:20031)
- Layer 20: `锁定`, ` LS`, `cape`, `ait`, `能被` (target ranks: fact_1=21:1218, fact_2=6:458, fact_3=92:5891, prefix_sum_12=27:2561, sum=119:11233)
- Layer 30: `cape`, `拒`, `eder`, `atan`, ` tear` (target ranks: fact_1=21:1195, fact_2=6:2063, fact_3=92:8245, prefix_sum_12=27:1415, sum=119:27651)
- Layer 35: `92`, ` uranium`, `86`, `uran`, ` Uran` (target ranks: fact_1=21:6922, fact_2=6:739, fact_3=92:1, prefix_sum_12=27:7023, sum=119:7031)
- Layer 36: `92`, `93`, ` ninety`, `91`, `94` (target ranks: fact_1=21:41904, fact_2=6:17104, fact_3=92:1, prefix_sum_12=27:46563, sum=119:11140)
- Layer 37: `92`, ` ninety`, `922`, `93`, `91` (target ranks: fact_1=21:92653, fact_2=6:88589, fact_3=92:1, prefix_sum_12=27:113429, sum=119:15107)
- Layer 38: `92`, `uran`, `迷惑`, ` Uran`, `ensing` (target ranks: fact_1=21:72943, fact_2=6:86459, fact_3=92:1, prefix_sum_12=27:116142, sum=119:4986)
- Layer 39: `东海`, `}<?`, `�`, `uran`, `迷惑` (target ranks: fact_1=21:31901, fact_2=6:80276, fact_3=92:7416, prefix_sum_12=27:115644, sum=119:31)
- Layer 40: `atomic`, `�`, `omit`, `114`, `装` (target ranks: fact_1=21:5475, fact_2=6:23777, fact_3=92:47216, prefix_sum_12=27:96916, sum=119:42)
- Layer 41: ` atomic`, `atomic`, `装`, `样子`, `一句话` (target ranks: fact_1=21:2428, fact_2=6:3318, fact_3=92:57600, prefix_sum_12=27:52106, sum=119:1340)

### Filler position 30 (absolute token 545, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=21:126078, fact_2=6:127559, fact_3=92:126034, prefix_sum_12=27:122845, sum=119:123111)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:6777, fact_2=6:2523, fact_3=92:11133, prefix_sum_12=27:7950, sum=119:19466)
- Layer 20: ` smile`, `锁定`, `胃癌`, `atile`, ` wig` (target ranks: fact_1=21:5048, fact_2=6:1484, fact_3=92:12614, prefix_sum_12=27:8402, sum=119:29290)
- Layer 30: `/hess`, ` ES`, ` reserved`, `reve`, `忑` (target ranks: fact_1=21:11068, fact_2=6:19763, fact_3=92:64175, prefix_sum_12=27:46771, sum=119:76991)
- Layer 35: `�`, `铂`, ` platinum`, `镁`, ` mercury` (target ranks: fact_1=21:3230, fact_2=6:7171, fact_3=92:58288, prefix_sum_12=27:27422, sum=119:46517)
- Layer 36: `�`, `铂`, `镁`, ` Rh`, ` mercury` (target ranks: fact_1=21:7179, fact_2=6:6000, fact_3=92:23885, prefix_sum_12=27:22107, sum=119:19502)
- Layer 37: `�`, ` platinum`, `�`, ` Platinum`, `铂` (target ranks: fact_1=21:23524, fact_2=6:31592, fact_3=92:59422, prefix_sum_12=27:55048, sum=119:18603)
- Layer 38: `�`, ` Platinum`, ` platinum`, ` Titan`, `�` (target ranks: fact_1=21:34856, fact_2=6:39805, fact_3=92:61384, prefix_sum_12=27:58143, sum=119:24455)
- Layer 39: `�`, ` Platinum`, ` Titan`, `�`, ` Copper` (target ranks: fact_1=21:14806, fact_2=6:44270, fact_3=92:83960, prefix_sum_12=27:34759, sum=119:42931)
- Layer 40: `�`, ` Nitrogen`, ` Titan`, ` Iron`, ` Oxygen` (target ranks: fact_1=21:5101, fact_2=6:6730, fact_3=92:79114, prefix_sum_12=27:13718, sum=119:15474)
- Layer 41: ` oxygen`, ` `, ` chlorine`, ` Zinc`, ` Oxygen` (target ranks: fact_1=21:548, fact_2=6:204, fact_3=92:19610, prefix_sum_12=27:913, sum=119:12083)

### Filler position 31 (absolute token 546, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126525, fact_2=6:127908, fact_3=92:126668, prefix_sum_12=27:123438, sum=119:124202)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:6671, fact_2=6:2307, fact_3=92:10844, prefix_sum_12=27:7505, sum=119:19620)
- Layer 20: `锁定`, ` smile`, `ait`, ` LS`, `甸` (target ranks: fact_1=21:3525, fact_2=6:1189, fact_3=92:6977, prefix_sum_12=27:5753, sum=119:18933)
- Layer 30: ` tap`, `鞍`, `Tap`, ` Tap`, `锁定` (target ranks: fact_1=21:6914, fact_2=6:1983, fact_3=92:12747, prefix_sum_12=27:7523, sum=119:19761)
- Layer 35: `锁定`, ` tap`, `鞍`, ` Tap`, `重复` (target ranks: fact_1=21:3177, fact_2=6:2661, fact_3=92:14218, prefix_sum_12=27:3105, sum=119:15990)
- Layer 36: ` tap`, ` Tap`, `锁定`, `Tap`, ` stabil` (target ranks: fact_1=21:6304, fact_2=6:3409, fact_3=92:16205, prefix_sum_12=27:3317, sum=119:12446)
- Layer 37: `坏`, `}<?`, `冰冰`, `坏了`, `陪伴` (target ranks: fact_1=21:30831, fact_2=6:28666, fact_3=92:56445, prefix_sum_12=27:15417, sum=119:19167)
- Layer 38: `坏`, `冰冰`, `差错`, `坏了`, `}<?` (target ranks: fact_1=21:37700, fact_2=6:35217, fact_3=92:68774, prefix_sum_12=27:16698, sum=119:17409)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `铎`, `�`, `osit` (target ranks: fact_1=21:72521, fact_2=6:98269, fact_3=92:95917, prefix_sum_12=27:68080, sum=119:45856)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, `铎`, `scr`, `透过` (target ranks: fact_1=21:37008, fact_2=6:41011, fact_3=92:59155, prefix_sum_12=27:42535, sum=119:24782)
- Layer 41: ` .`, `叮`, ` .↵↵`, ` ,`, ` ` (target ranks: fact_1=21:23256, fact_2=6:4577, fact_3=92:39052, prefix_sum_12=27:17182, sum=119:13350)

### Filler position 32 (absolute token 547, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126496, fact_2=6:127898, fact_3=92:126542, prefix_sum_12=27:123443, sum=119:124096)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:6671, fact_2=6:2321, fact_3=92:10118, prefix_sum_12=27:7278, sum=119:18689)
- Layer 20: `锁定`, ` LS`, `甸`, `ait`, ` smile` (target ranks: fact_1=21:2815, fact_2=6:863, fact_3=92:8014, prefix_sum_12=27:4935, sum=119:17651)
- Layer 30: `回答`, ` answer`, ` Answer`, `Answer`, `回答问题` (target ranks: fact_1=21:15356, fact_2=6:9415, fact_3=92:38303, prefix_sum_12=27:29577, sum=119:34570)
- Layer 35: ` repetition`, `锁定`, `重复`, ` tap`, `Tap` (target ranks: fact_1=21:6428, fact_2=6:5530, fact_3=92:32162, prefix_sum_12=27:16042, sum=119:29875)
- Layer 36: ` tap`, `Tap`, `重复`, ` stabil`, `eder` (target ranks: fact_1=21:12407, fact_2=6:10033, fact_3=92:38155, prefix_sum_12=27:18219, sum=119:23405)
- Layer 37: `acam`, `tap`, ` tap`, ` immediate`, `<｜begin▁of▁sentence｜>` (target ranks: fact_1=21:24470, fact_2=6:44596, fact_3=92:83394, prefix_sum_12=27:36388, sum=119:38041)
- Layer 38: `<｜begin▁of▁sentence｜>`, `acam`, `指令`, ` immediate`, ` capsule` (target ranks: fact_1=21:24361, fact_2=6:47350, fact_3=92:87572, prefix_sum_12=27:35860, sum=119:34323)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `下沉`, `osit`, ` immediate` (target ranks: fact_1=21:33042, fact_2=6:85364, fact_3=92:100229, prefix_sum_12=27:53433, sum=119:53987)
- Layer 40: `<｜begin▁of▁sentence｜>`, `}<?`, `scr`, `anium`, `下沉` (target ranks: fact_1=21:18208, fact_2=6:22369, fact_3=92:73185, prefix_sum_12=27:31241, sum=119:38414)
- Layer 41: ` .`, ` until`, ` ativid`, `叮`, `猕猴` (target ranks: fact_1=21:19427, fact_2=6:4051, fact_3=92:66316, prefix_sum_12=27:23321, sum=119:45229)

### Filler position 33 (absolute token 548, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126403, fact_2=6:127822, fact_3=92:126462, prefix_sum_12=27:123220, sum=119:123907)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:6791, fact_2=6:2473, fact_3=92:10128, prefix_sum_12=27:7413, sum=119:18608)
- Layer 20: `ait`, `锁定`, ` LS`, ` Walker`, `LS` (target ranks: fact_1=21:1562, fact_2=6:455, fact_3=92:5647, prefix_sum_12=27:2043, sum=119:12591)
- Layer 30: `acos`, `acin`, `aci`, ` pakig`, `atomic` (target ranks: fact_1=21:3773, fact_2=6:16316, fact_3=92:15463, prefix_sum_12=27:994, sum=119:26511)
- Layer 35: ` met`, `38`, `apan`, `28`, ` dip` (target ranks: fact_1=21:2230, fact_2=6:4098, fact_3=92:3455, prefix_sum_12=27:80, sum=119:10263)
- Layer 36: `38`, `三十五`, `三十六`, `37`, `36` (target ranks: fact_1=21:27539, fact_2=6:18961, fact_3=92:11441, prefix_sum_12=27:322, sum=119:22752)
- Layer 37: `92`, `86`, `otas`, `uran`, `三十六` (target ranks: fact_1=21:28840, fact_2=6:89527, fact_3=92:1, prefix_sum_12=27:16511, sum=119:2324)
- Layer 38: `92`, `九天`, `天尊`, `uran`, `党群` (target ranks: fact_1=21:37283, fact_2=6:116835, fact_3=92:1, prefix_sum_12=27:94404, sum=119:1072)
- Layer 39: `<｜place▁holder▁no▁703｜>`, `<｜place▁holder▁no▁682｜>`, `<｜place▁holder▁no▁693｜>`, `uran`, `<｜place▁holder▁no▁698｜>` (target ranks: fact_1=21:6632, fact_2=6:121383, fact_3=92:21244, prefix_sum_12=27:106719, sum=119:333)
- Layer 40: `<｜begin▁of▁file｜>`, `uker`, `uran`, `atomic`, ` atomic` (target ranks: fact_1=21:944, fact_2=6:96361, fact_3=92:1239, prefix_sum_12=27:51995, sum=119:456)
- Layer 41: `出不穷`, `我曾经`, ` atomic`, `因为这些`, `询` (target ranks: fact_1=21:12262, fact_2=6:41581, fact_3=92:28360, prefix_sum_12=27:71838, sum=119:27239)

### Filler position 34 (absolute token 549, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126555, fact_2=6:127908, fact_3=92:126667, prefix_sum_12=27:123501, sum=119:124162)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:6890, fact_2=6:2522, fact_3=92:10500, prefix_sum_12=27:7603, sum=119:19154)
- Layer 20: `ait`, `足`, `能被`, `锁定`, ` Walker` (target ranks: fact_1=21:1529, fact_2=6:805, fact_3=92:7142, prefix_sum_12=27:2445, sum=119:17775)
- Layer 30: `acos`, ` dy`, `acin`, `保留`, `锁定` (target ranks: fact_1=21:2158, fact_2=6:9958, fact_3=92:12115, prefix_sum_12=27:714, sum=119:35674)
- Layer 35: `锁定`, `acin`, ` dy`, `出生`, ` reserve` (target ranks: fact_1=21:151, fact_2=6:3148, fact_3=92:1492, prefix_sum_12=27:153, sum=119:24381)
- Layer 36: `37`, `orty`, `36`, `三十六`, `acin` (target ranks: fact_1=21:4598, fact_2=6:19056, fact_3=92:3781, prefix_sum_12=27:1386, sum=119:23450)
- Layer 37: `}<?`, `?datasetId`, ` dekameters`, `Hakutulos`, `asca` (target ranks: fact_1=21:12454, fact_2=6:98441, fact_3=92:32, prefix_sum_12=27:44326, sum=119:5626)
- Layer 38: `}<?`, `院内`, ` dekameters`, `生活习惯`, `王子` (target ranks: fact_1=21:70737, fact_2=6:96951, fact_3=92:254, prefix_sum_12=27:116408, sum=119:8397)
- Layer 39: `107`, `108`, `<｜place▁holder▁no▁699｜>`, `}<?`, `<｜place▁holder▁no▁703｜>` (target ranks: fact_1=21:7398, fact_2=6:110501, fact_3=92:23274, prefix_sum_12=27:108768, sum=119:527)
- Layer 40: ` smoothing`, `}<?`, `留存`, `scr`, `107` (target ranks: fact_1=21:558, fact_2=6:65326, fact_3=92:17075, prefix_sum_12=27:96223, sum=119:629)
- Layer 41: ` dekameters`, `太多了`, ` smoothing`, `因为这些`, `不是吗` (target ranks: fact_1=21:746, fact_2=6:4836, fact_3=92:26491, prefix_sum_12=27:51757, sum=119:5060)

### Filler position 35 (absolute token 550, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126721, fact_2=6:128029, fact_3=92:126936, prefix_sum_12=27:123639, sum=119:124603)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7638, fact_2=6:3121, fact_3=92:12090, prefix_sum_12=27:8729, sum=119:20563)
- Layer 20: `足`, `幽`, `胃癌`, `cape`, `能被` (target ranks: fact_1=21:1382, fact_2=6:624, fact_3=92:7281, prefix_sum_12=27:3147, sum=119:16996)
- Layer 30: `acos`, `acet`, `}<?`, `atan`, ` Min` (target ranks: fact_1=21:5504, fact_2=6:26587, fact_3=92:16869, prefix_sum_12=27:1436, sum=119:32460)
- Layer 35: `锁定`, `出生`, ` Sm`, `atan`, `水土` (target ranks: fact_1=21:430, fact_2=6:8478, fact_3=92:1945, prefix_sum_12=27:78, sum=119:16935)
- Layer 36: `}<?`, ` reper`, ` Sm`, ` sumala`, `acos` (target ranks: fact_1=21:19331, fact_2=6:47506, fact_3=92:9206, prefix_sum_12=27:1194, sum=119:12887)
- Layer 37: `}<?`, `}using`, `Quintal`, `92`, `借此` (target ranks: fact_1=21:35351, fact_2=6:107338, fact_3=92:4, prefix_sum_12=27:44800, sum=119:936)
- Layer 38: `}<?`, `王子`, `借此`, `生活习惯`, `osaurus` (target ranks: fact_1=21:98322, fact_2=6:108017, fact_3=92:170, prefix_sum_12=27:121042, sum=119:2985)
- Layer 39: `108`, `109`, `107`, `}<?`, `105` (target ranks: fact_1=21:50711, fact_2=6:120745, fact_3=92:34853, prefix_sum_12=27:124745, sum=119:459)
- Layer 40: ` smoothing`, `108`, `109`, ` atomic`, `水土` (target ranks: fact_1=21:5450, fact_2=6:97358, fact_3=92:13824, prefix_sum_12=27:116749, sum=119:202)
- Layer 41: ` atomic`, ` smoothing`, `因为这些`, `下场`, ` because` (target ranks: fact_1=21:2705, fact_2=6:11806, fact_3=92:12476, prefix_sum_12=27:52471, sum=119:2353)

### Filler position 36 (absolute token 551, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126677, fact_2=6:127985, fact_3=92:126852, prefix_sum_12=27:123563, sum=119:124398)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8041, fact_2=6:3480, fact_3=92:12956, prefix_sum_12=27:9457, sum=119:21910)
- Layer 20: `ait`, `能被`, `足`, `锁定`, ` smile` (target ranks: fact_1=21:2640, fact_2=6:1465, fact_3=92:9479, prefix_sum_12=27:4850, sum=119:21424)
- Layer 30: `}<?`, `acos`, `�`, ` ES`, `总体` (target ranks: fact_1=21:7903, fact_2=6:43131, fact_3=92:14478, prefix_sum_12=27:1768, sum=119:34180)
- Layer 35: ` ES`, `锁定`, ` academy`, ` vertical`, `保留` (target ranks: fact_1=21:2739, fact_2=6:10111, fact_3=92:1835, prefix_sum_12=27:858, sum=119:8669)
- Layer 36: `}<?`, `翻`, ` vertical`, ` reper`, ` upright` (target ranks: fact_1=21:41686, fact_2=6:62816, fact_3=92:11788, prefix_sum_12=27:13606, sum=119:3521)
- Layer 37: `}<?`, `cault`, `Quintal`, `院内`, `zat` (target ranks: fact_1=21:44888, fact_2=6:112062, fact_3=92:21, prefix_sum_12=27:66717, sum=119:911)
- Layer 38: `}<?`, `院内`, `109`, ` dekameters`, `107` (target ranks: fact_1=21:113989, fact_2=6:94637, fact_3=92:13805, prefix_sum_12=27:126321, sum=119:587)
- Layer 39: `}<?`, `109`, `108`, `经纬`, ` smoothing` (target ranks: fact_1=21:29610, fact_2=6:118510, fact_3=92:94600, prefix_sum_12=27:120182, sum=119:4283)
- Layer 40: `}<?`, ` atomic`, ` smoothing`, `ове`, `less` (target ranks: fact_1=21:1356, fact_2=6:97172, fact_3=92:72858, prefix_sum_12=27:105036, sum=119:2586)
- Layer 41: `因为这些`, ` atomic`, `太多了`, `我曾经`, ` because` (target ranks: fact_1=21:1614, fact_2=6:17946, fact_3=92:51599, prefix_sum_12=27:51308, sum=119:10678)

### Filler position 37 (absolute token 552, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126779, fact_2=6:128100, fact_3=92:127071, prefix_sum_12=27:123825, sum=119:124854)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8204, fact_2=6:3449, fact_3=92:13347, prefix_sum_12=27:9750, sum=119:23051)
- Layer 20: `能被`, ` Walker`, `ait`, `忑`, ` ES` (target ranks: fact_1=21:2346, fact_2=6:1228, fact_3=92:9383, prefix_sum_12=27:3253, sum=119:20815)
- Layer 30: `acos`, ` pakig`, ` Gle`, ` gilay`, `}<?` (target ranks: fact_1=21:827, fact_2=6:63038, fact_3=92:30732, prefix_sum_12=27:336, sum=119:44899)
- Layer 35: `37`, `39`, `78`, `38`, `21` (target ranks: fact_1=21:5, fact_2=6:10619, fact_3=92:2852, prefix_sum_12=27:12, sum=119:33871)
- Layer 36: `37`, `}<?`, `43`, `38`, `39` (target ranks: fact_1=21:501, fact_2=6:60022, fact_3=92:21802, prefix_sum_12=27:181, sum=119:26328)
- Layer 37: `?datasetId`, `}<?`, `92`, `93`, `gom` (target ranks: fact_1=21:1181, fact_2=6:121073, fact_3=92:3, prefix_sum_12=27:25799, sum=119:6838)
- Layer 38: `<｜begin▁of▁file｜>`, `}<?`, `天尊`, ` dekameters`, `-Geiger` (target ranks: fact_1=21:44342, fact_2=6:113062, fact_3=92:13, prefix_sum_12=27:112229, sum=119:8537)
- Layer 39: `105`, `107`, `108`, `106`, `109` (target ranks: fact_1=21:18330, fact_2=6:125760, fact_3=92:8055, prefix_sum_12=27:113966, sum=119:1927)
- Layer 40: ` atomic`, ` ons`, `<｜place▁holder▁no▁702｜>`, `atomic`, `radesh` (target ranks: fact_1=21:1225, fact_2=6:123731, fact_3=92:13390, prefix_sum_12=27:113094, sum=119:4384)
- Layer 41: ` atomic`, `因为这些`, `出不穷`, ` answer`, `atomic` (target ranks: fact_1=21:4221, fact_2=6:62350, fact_3=92:27478, prefix_sum_12=27:86488, sum=119:21780)

### Filler position 38 (absolute token 553, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126666, fact_2=6:127995, fact_3=92:126912, prefix_sum_12=27:123614, sum=119:124681)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7576, fact_2=6:2969, fact_3=92:12328, prefix_sum_12=27:8946, sum=119:21964)
- Layer 20: `忑`, `ait`, `atile`, `能被`, ` ES` (target ranks: fact_1=21:6561, fact_2=6:3193, fact_3=92:16809, prefix_sum_12=27:10420, sum=119:38241)
- Layer 30: `清楚楚`, ` Pop`, ` dy`, `reve`, ` Mim` (target ranks: fact_1=21:5366, fact_2=6:32363, fact_3=92:57760, prefix_sum_12=27:26614, sum=119:73321)
- Layer 35: `�`, ` manganese`, ` cadmium`, ` mercury`, `锰` (target ranks: fact_1=21:1408, fact_2=6:14618, fact_3=92:66210, prefix_sum_12=27:12154, sum=119:34790)
- Layer 36: `�`, ` mercury`, ` Rh`, `镁`, ` manganese` (target ranks: fact_1=21:2275, fact_2=6:7595, fact_3=92:25804, prefix_sum_12=27:7561, sum=119:9765)
- Layer 37: `�`, `�`, ` chromium`, ` manganese`, ` mercury` (target ranks: fact_1=21:6385, fact_2=6:27837, fact_3=92:56181, prefix_sum_12=27:20915, sum=119:10002)
- Layer 38: `�`, `�`, `adium`, ` chromium`, ` manganese` (target ranks: fact_1=21:6054, fact_2=6:26201, fact_3=92:49901, prefix_sum_12=27:14134, sum=119:6976)
- Layer 39: `�`, `�`, ` Mercury`, `铎`, `adium` (target ranks: fact_1=21:5882, fact_2=6:38652, fact_3=92:52159, prefix_sum_12=27:8382, sum=119:8553)
- Layer 40: `�`, `osit`, `scr`, ` `, `尾巴` (target ranks: fact_1=21:1975, fact_2=6:13458, fact_3=92:32745, prefix_sum_12=27:3261, sum=119:2312)
- Layer 41: ` `, ` .`, ` waiting`, `等待`, `回答道` (target ranks: fact_1=21:423, fact_2=6:454, fact_3=92:6024, prefix_sum_12=27:401, sum=119:569)

### Filler position 39 (absolute token 554, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126451, fact_2=6:127859, fact_3=92:126677, prefix_sum_12=27:123309, sum=119:124197)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8004, fact_2=6:3220, fact_3=92:12376, prefix_sum_12=27:9198, sum=119:21791)
- Layer 20: `ait`, ` ES`, `锁定`, `鞍`, `能被` (target ranks: fact_1=21:5948, fact_2=6:2557, fact_3=92:9380, prefix_sum_12=27:7750, sum=119:28786)
- Layer 30: `}<?`, `acet`, `acos`, `迎接`, `iret` (target ranks: fact_1=21:14241, fact_2=6:73073, fact_3=92:4303, prefix_sum_12=27:2607, sum=119:59609)
- Layer 35: `93`, `88`, `79`, `锁定`, `87` (target ranks: fact_1=21:2441, fact_2=6:15285, fact_3=92:28, prefix_sum_12=27:261, sum=119:10803)
- Layer 36: `}<?`, `93`, `88`, `87`, `78` (target ranks: fact_1=21:24510, fact_2=6:65777, fact_3=92:13, prefix_sum_12=27:3758, sum=119:2034)
- Layer 37: `}<?`, `92`, `93`, `88`, `?datasetId` (target ranks: fact_1=21:36365, fact_2=6:115977, fact_3=92:2, prefix_sum_12=27:38363, sum=119:1982)
- Layer 38: `}<?`, `院内`, `高山`, `93`, `105` (target ranks: fact_1=21:64666, fact_2=6:116581, fact_3=92:18, prefix_sum_12=27:100394, sum=119:873)
- Layer 39: `}<?`, `105`, `107`, `<｜place▁holder▁no▁703｜>`, `103` (target ranks: fact_1=21:39595, fact_2=6:121415, fact_3=92:55727, prefix_sum_12=27:103056, sum=119:1993)
- Layer 40: `}<?`, ` atomic`, `auri`, `atomic`, ` overwhelming` (target ranks: fact_1=21:1562, fact_2=6:84610, fact_3=92:23510, prefix_sum_12=27:69124, sum=119:1242)
- Layer 41: ` atomic`, `太多了`, `atomic`, ` `, `因为这些` (target ranks: fact_1=21:238, fact_2=6:2780, fact_3=92:21985, prefix_sum_12=27:17544, sum=119:3403)

### Filler position 40 (absolute token 555, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126378, fact_2=6:127809, fact_3=92:126700, prefix_sum_12=27:123138, sum=119:124344)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7877, fact_2=6:3210, fact_3=92:12205, prefix_sum_12=27:9183, sum=119:21629)
- Layer 20: `ait`, `锁定`, `鞍`, ` LS`, `胃癌` (target ranks: fact_1=21:3916, fact_2=6:1750, fact_3=92:9836, prefix_sum_12=27:6592, sum=119:22665)
- Layer 30: `acos`, `acet`, `俯`, `}<?`, `otos` (target ranks: fact_1=21:7108, fact_2=6:59578, fact_3=92:19121, prefix_sum_12=27:5779, sum=119:43298)
- Layer 35: `锁定`, `分解`, `apan`, `打完`, `79` (target ranks: fact_1=21:1890, fact_2=6:22791, fact_3=92:408, prefix_sum_12=27:2405, sum=119:8370)
- Layer 36: `}<?`, `opan`, `apan`, `orty`, `otas` (target ranks: fact_1=21:26098, fact_2=6:67461, fact_3=92:1523, prefix_sum_12=27:33453, sum=119:1757)
- Layer 37: `}<?`, `Quintal`, `?datasetId`, `amn`, `uran` (target ranks: fact_1=21:35668, fact_2=6:112764, fact_3=92:7, prefix_sum_12=27:91822, sum=119:2106)
- Layer 38: `}<?`, `?datasetId`, ` dekameters`, `高山`, `院内` (target ranks: fact_1=21:50497, fact_2=6:115953, fact_3=92:227, prefix_sum_12=27:102626, sum=119:1458)
- Layer 39: `105`, `}<?`, `104`, `107`, `103` (target ranks: fact_1=21:68178, fact_2=6:117825, fact_3=92:49431, prefix_sum_12=27:112120, sum=119:44)
- Layer 40: `}<?`, ` atomic`, `水土`, `105`, `103` (target ranks: fact_1=21:15770, fact_2=6:87050, fact_3=92:22582, prefix_sum_12=27:93576, sum=119:93)
- Layer 41: ` atomic`, `太多了`, `因为这些`, ` `, `atomic` (target ranks: fact_1=21:4379, fact_2=6:7130, fact_3=92:14749, prefix_sum_12=27:38928, sum=119:378)

### Filler position 41 (absolute token 556, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126377, fact_2=6:127810, fact_3=92:126673, prefix_sum_12=27:123161, sum=119:124290)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8039, fact_2=6:3207, fact_3=92:12812, prefix_sum_12=27:9566, sum=119:22063)
- Layer 20: `锁定`, ` smile`, `ession`, `足`, `胃癌` (target ranks: fact_1=21:2469, fact_2=6:1378, fact_3=92:11664, prefix_sum_12=27:5431, sum=119:26051)
- Layer 30: `保留`, `俯`, ` reserved`, `scan`, `柿子` (target ranks: fact_1=21:3043, fact_2=6:8124, fact_3=92:35527, prefix_sum_12=27:3307, sum=119:62801)
- Layer 35: `21`, `二十一`, ` Scand`, ` XXI`, ` Sc` (target ranks: fact_1=21:1, fact_2=6:44057, fact_3=92:89646, prefix_sum_12=27:1346, sum=119:84231)
- Layer 36: `21`, `二十一`, ` Scand`, `Sc`, ` XXI` (target ranks: fact_1=21:1, fact_2=6:69223, fact_3=92:105548, prefix_sum_12=27:4619, sum=119:88630)
- Layer 37: `二十一`, `21`, `}<?`, ` XXI`, ` Scand` (target ranks: fact_1=21:2, fact_2=6:119821, fact_3=92:121738, prefix_sum_12=27:28369, sum=119:107484)
- Layer 38: `二十一`, `21`, ` Scand`, `}<?`, ` XXI` (target ranks: fact_1=21:2, fact_2=6:123893, fact_3=92:126488, prefix_sum_12=27:40319, sum=119:101231)
- Layer 39: ` Scand`, ` Scar`, ` Sc`, `二十一`, ` Scarlet` (target ranks: fact_1=21:12, fact_2=6:125635, fact_3=92:116053, prefix_sum_12=27:28586, sum=119:96596)
- Layer 40: ` twenty`, ` Twenty`, `twenty`, `Twenty`, `俯` (target ranks: fact_1=21:15, fact_2=6:98805, fact_3=92:45673, prefix_sum_12=27:4546, sum=119:36309)
- Layer 41: ` .`, `.,`, ` compounded`, ` atomic`, ` twenty` (target ranks: fact_1=21:24, fact_2=6:3903, fact_3=92:16394, prefix_sum_12=27:815, sum=119:14831)

### Filler position 42 (absolute token 557, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126821, fact_2=6:128143, fact_3=92:127064, prefix_sum_12=27:124008, sum=119:124793)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7800, fact_2=6:3135, fact_3=92:12944, prefix_sum_12=27:9452, sum=119:22173)
- Layer 20: ` smile`, `锁定`, `cape`, `足`, `ession` (target ranks: fact_1=21:3411, fact_2=6:1975, fact_3=92:15469, prefix_sum_12=27:7826, sum=119:28670)
- Layer 30: `�`, `保留`, `冰`, ` reserved`, `atan` (target ranks: fact_1=21:11090, fact_2=6:7957, fact_3=92:43782, prefix_sum_12=27:6777, sum=119:56821)
- Layer 35: `沛`, `�`, `周期`, ` periodic`, ` period` (target ranks: fact_1=21:331, fact_2=6:4380, fact_3=92:5937, prefix_sum_12=27:2278, sum=119:7748)
- Layer 36: `沛`, ` periodic`, `�`, `周期`, `留存` (target ranks: fact_1=21:4079, fact_2=6:19873, fact_3=92:26497, prefix_sum_12=27:11537, sum=119:8931)
- Layer 37: `}<?`, ` periodic`, `�`, ` Periodic`, `焯` (target ranks: fact_1=21:9251, fact_2=6:81224, fact_3=92:61576, prefix_sum_12=27:30763, sum=119:13684)
- Layer 38: `}<?`, `�`, `zat`, `ophyll`, `duc` (target ranks: fact_1=21:13721, fact_2=6:100743, fact_3=92:73879, prefix_sum_12=27:30000, sum=119:18683)
- Layer 39: `}<?`, `�`, `二十一`, ` twenty`, `twenty` (target ranks: fact_1=21:21, fact_2=6:125055, fact_3=92:120874, prefix_sum_12=27:13505, sum=119:78800)
- Layer 40: `二十一`, ` twenty`, `21`, `twenty`, ` Twenty` (target ranks: fact_1=21:3, fact_2=6:107626, fact_3=92:110845, prefix_sum_12=27:1631, sum=119:62604)
- Layer 41: `二十一`, `21`, ` twenty`, ` .`, `二十` (target ranks: fact_1=21:2, fact_2=6:13342, fact_3=92:89215, prefix_sum_12=27:574, sum=119:40220)

### Filler position 43 (absolute token 558, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126429, fact_2=6:127865, fact_3=92:126669, prefix_sum_12=27:123380, sum=119:124273)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7752, fact_2=6:3008, fact_3=92:12823, prefix_sum_12=27:9316, sum=119:23064)
- Layer 20: `足`, ` LS`, ` smile`, `cape`, `LS` (target ranks: fact_1=21:1596, fact_2=6:540, fact_3=92:6616, prefix_sum_12=27:2177, sum=119:18107)
- Layer 30: ` picnic`, ` QR`, `code`, `柿子`, `沛` (target ranks: fact_1=21:8350, fact_2=6:1214, fact_3=92:41230, prefix_sum_12=27:3490, sum=119:41390)
- Layer 35: ` Six`, ` six`, `6`, `six`, `Six` (target ranks: fact_1=21:62155, fact_2=6:3, fact_3=92:103601, prefix_sum_12=27:42491, sum=119:88053)
- Layer 36: ` six`, ` Six`, `6`, ` Sixth`, `Six` (target ranks: fact_1=21:109458, fact_2=6:3, fact_3=92:117639, prefix_sum_12=27:84818, sum=119:85773)
- Layer 37: ` Sixth`, ` sixth`, `Six`, ` Six`, ` six` (target ranks: fact_1=21:124135, fact_2=6:11, fact_3=92:126919, prefix_sum_12=27:120437, sum=119:102011)
- Layer 38: ` Sixth`, ` šest`, ` sixth`, `Six`, ` Six` (target ranks: fact_1=21:123154, fact_2=6:20, fact_3=92:126066, prefix_sum_12=27:117634, sum=119:81398)
- Layer 39: `}<?`, ` Sixth`, `二十一`, ` medief`, `tanle` (target ranks: fact_1=21:89, fact_2=6:1201, fact_3=92:123189, prefix_sum_12=27:35693, sum=119:78033)
- Layer 40: `二十一`, ` twenty`, `21`, ` Twenty`, `twenty` (target ranks: fact_1=21:3, fact_2=6:425, fact_3=92:85854, prefix_sum_12=27:10471, sum=119:32731)
- Layer 41: `二十一`, ` twenty`, `21`, `二十`, `因为这些` (target ranks: fact_1=21:3, fact_2=6:505, fact_3=92:57948, prefix_sum_12=27:3441, sum=119:31155)

### Filler position 44 (absolute token 559, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126325, fact_2=6:127788, fact_3=92:126585, prefix_sum_12=27:123159, sum=119:124210)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:7887, fact_2=6:3066, fact_3=92:12595, prefix_sum_12=27:9354, sum=119:22963)
- Layer 20: `能被`, `锁定`, `ait`, ` ES`, `LS` (target ranks: fact_1=21:3294, fact_2=6:1277, fact_3=92:7286, prefix_sum_12=27:3128, sum=119:15817)
- Layer 30: ` pakig`, `acos`, ` ---|---|---|---|---|---|---`, `otor`, ` ---|---|---|---` (target ranks: fact_1=21:11414, fact_2=6:93943, fact_3=92:18003, prefix_sum_12=27:347, sum=119:30030)
- Layer 35: `39`, `37`, `78`, `38`, `79` (target ranks: fact_1=21:73, fact_2=6:24095, fact_3=92:271, prefix_sum_12=27:17, sum=119:14925)
- Layer 36: `39`, `37`, `43`, `38`, `42` (target ranks: fact_1=21:2780, fact_2=6:80567, fact_3=92:4113, prefix_sum_12=27:179, sum=119:10541)
- Layer 37: `92`, `93`, `<｜begin▁of▁file｜>`, `42`, `}<?` (target ranks: fact_1=21:10771, fact_2=6:116302, fact_3=92:1, prefix_sum_12=27:15297, sum=119:1715)
- Layer 38: `<｜begin▁of▁file｜>`, `}<?`, ` dekameters`, `天尊`, `105` (target ranks: fact_1=21:70778, fact_2=6:113510, fact_3=92:16, prefix_sum_12=27:92768, sum=119:5520)
- Layer 39: `105`, `107`, `tanle`, `}<?`, `经纬` (target ranks: fact_1=21:6658, fact_2=6:125262, fact_3=92:8365, prefix_sum_12=27:77081, sum=119:11135)
- Layer 40: `<｜begin▁of▁file｜>`, ` atomic`, ` dátummal`, `atomic`, `<｜place▁holder▁no▁687｜>` (target ranks: fact_1=21:199, fact_2=6:121616, fact_3=92:5993, prefix_sum_12=27:64640, sum=119:23151)
- Layer 41: ` atomic`, `出不穷`, `我曾经`, `atomic`, `<｜begin▁of▁file｜>` (target ranks: fact_1=21:4612, fact_2=6:95508, fact_3=92:70800, prefix_sum_12=27:95348, sum=119:93485)

### Filler position 45 (absolute token 560, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126426, fact_2=6:127839, fact_3=92:126799, prefix_sum_12=27:123233, sum=119:124557)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=21:8412, fact_2=6:3315, fact_3=92:12490, prefix_sum_12=27:9558, sum=119:22554)
- Layer 20: `ait`, `会成为`, `妇`, `平行`, `锁定` (target ranks: fact_1=21:13969, fact_2=6:11576, fact_3=92:35311, prefix_sum_12=27:13940, sum=119:49023)
- Layer 30: `acin`, `二十八`, `acic`, `acos`, ` reserved` (target ranks: fact_1=21:20813, fact_2=6:33408, fact_3=92:48673, prefix_sum_12=27:9066, sum=119:57213)
- Layer 35: `acic`, `锁定`, `打完`, `二十八`, `acin` (target ranks: fact_1=21:11096, fact_2=6:16094, fact_3=92:46827, prefix_sum_12=27:4088, sum=119:41492)
- Layer 36: `留存`, `acin`, `打完`, `二十八`, `acic` (target ranks: fact_1=21:18653, fact_2=6:22935, fact_3=92:54508, prefix_sum_12=27:5750, sum=119:33670)
- Layer 37: `}<?`, `acet`, `铎`, `isis`, `等待着` (target ranks: fact_1=21:73853, fact_2=6:93987, fact_3=92:102928, prefix_sum_12=27:32976, sum=119:51696)
- Layer 38: `}<?`, `acet`, `等待着`, ` fusion`, `铎` (target ranks: fact_1=21:63782, fact_2=6:69696, fact_3=92:98859, prefix_sum_12=27:21147, sum=119:50314)
- Layer 39: `}<?`, `铎`, `等待着`, `osit`, `繁体` (target ranks: fact_1=21:47480, fact_2=6:92175, fact_3=92:75977, prefix_sum_12=27:39699, sum=119:54689)
- Layer 40: ` .`, `scr`, `等待着`, ` Mercury`, ` Rutherford` (target ranks: fact_1=21:12699, fact_2=6:36176, fact_3=92:21630, prefix_sum_12=27:11699, sum=119:14498)
- Layer 41: ` .`, `.,`, `留存`, `<｜end▁of▁sentence｜>`, ` wherever` (target ranks: fact_1=21:10249, fact_2=6:2489, fact_3=92:15750, prefix_sum_12=27:5496, sum=119:9510)

### Filler position 46 (absolute token 561, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126214, fact_2=6:127714, fact_3=92:126440, prefix_sum_12=27:123103, sum=119:123986)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=21:8193, fact_2=6:3108, fact_3=92:11859, prefix_sum_12=27:9180, sum=119:21288)
- Layer 20: ` spac`, ` blanks`, `school`, `选取`, `blank` (target ranks: fact_1=21:26983, fact_2=6:79348, fact_3=92:117077, prefix_sum_12=27:47184, sum=119:106600)
- Layer 30: ` spac`, `}using`, `?datasetId`, `坝`, `}<?` (target ranks: fact_1=21:99444, fact_2=6:117871, fact_3=92:122559, prefix_sum_12=27:107415, sum=119:121213)
- Layer 35: `}using`, `?datasetId`, `绵绵`, `}<?`, ` panc` (target ranks: fact_1=21:70492, fact_2=6:105402, fact_3=92:103793, prefix_sum_12=27:63578, sum=119:109919)
- Layer 36: `足足`, `ancock`, `integr`, `ovel`, `放下` (target ranks: fact_1=21:21919, fact_2=6:42870, fact_3=92:51200, prefix_sum_12=27:15058, sum=119:67493)
- Layer 37: `}<?`, `integr`, ` harmon`, `放下`, `足足` (target ranks: fact_1=21:56524, fact_2=6:90650, fact_3=92:97073, prefix_sum_12=27:25972, sum=119:81522)
- Layer 38: ` .`, `足足`, `陪`, ` Mercury`, ` divers` (target ranks: fact_1=21:23963, fact_2=6:53732, fact_3=92:74723, prefix_sum_12=27:14472, sum=119:75733)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` Mercury`, `罢`, `陪` (target ranks: fact_1=21:39583, fact_2=6:86094, fact_3=92:82648, prefix_sum_12=27:32014, sum=119:96421)
- Layer 40: ` .`, ` Mercury`, ` .↵↵`, `<｜begin▁of▁sentence｜>`, ` nasod` (target ranks: fact_1=21:11422, fact_2=6:37451, fact_3=92:55946, prefix_sum_12=27:10933, sum=119:69985)
- Layer 41: ` .`, ` .↵↵`, ` `, `久久`, `刚` (target ranks: fact_1=21:1239, fact_2=6:2454, fact_3=92:16152, prefix_sum_12=27:1948, sum=119:24767)

### Filler position 47 (absolute token 562, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126545, fact_2=6:127980, fact_3=92:126849, prefix_sum_12=27:123696, sum=119:124434)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=21:7713, fact_2=6:2941, fact_3=92:11447, prefix_sum_12=27:8878, sum=119:20782)
- Layer 20: `}<?`, `)Skip`, `东海`, `aharoa`, ` pennyweights` (target ranks: fact_1=21:53653, fact_2=6:103643, fact_3=92:123433, prefix_sum_12=27:89900, sum=119:106853)
- Layer 30: `}<?`, `codeline`, `东京`, `}using`, `AssemblyVersion` (target ranks: fact_1=21:80354, fact_2=6:98559, fact_3=92:118674, prefix_sum_12=27:100550, sum=119:115133)
- Layer 35: `codeline`, `ِّف`, `}using`, `切割`, `}<?` (target ranks: fact_1=21:72105, fact_2=6:115742, fact_3=92:106533, prefix_sum_12=27:93771, sum=119:117199)
- Layer 36: `足足`, `生生`, `ancock`, `切割`, `锯` (target ranks: fact_1=21:33740, fact_2=6:67067, fact_3=92:61989, prefix_sum_12=27:37579, sum=119:74778)
- Layer 37: `}<?`, `东京`, `简体`, `磨损`, `在东` (target ranks: fact_1=21:49351, fact_2=6:103113, fact_3=92:105990, prefix_sum_12=27:36336, sum=119:83629)
- Layer 38: ` .`, `遁`, `保有`, ` Fusion`, `切割` (target ranks: fact_1=21:42627, fact_2=6:99349, fact_3=92:104850, prefix_sum_12=27:29839, sum=119:81085)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `简体`, ` covari`, `遁` (target ranks: fact_1=21:46800, fact_2=6:107440, fact_3=92:91284, prefix_sum_12=27:36476, sum=119:63180)
- Layer 40: ` .`, ` .↵↵`, `�`, `<｜begin▁of▁sentence｜>`, ` .↵` (target ranks: fact_1=21:23668, fact_2=6:57152, fact_3=92:66575, prefix_sum_12=27:16488, sum=119:34484)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: fact_1=21:4490, fact_2=6:5749, fact_3=92:23469, prefix_sum_12=27:3061, sum=119:17192)

### Filler position 48 (absolute token 563, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126548, fact_2=6:128005, fact_3=92:126848, prefix_sum_12=27:123699, sum=119:124412)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=21:7313, fact_2=6:2766, fact_3=92:11407, prefix_sum_12=27:8627, sum=119:21311)
- Layer 20: ` instantaneous`, `aharoa`, `aplenty`, `}<?`, `)Skip` (target ranks: fact_1=21:67808, fact_2=6:77844, fact_3=92:106454, prefix_sum_12=27:87353, sum=119:83045)
- Layer 30: `codeline`, `东京`, ` writ`, ` Answer`, `雄` (target ranks: fact_1=21:45067, fact_2=6:41056, fact_3=92:98798, prefix_sum_12=27:84353, sum=119:101317)
- Layer 35: `codeline`, ` doubly`, `白雪`, ` germ`, `雄` (target ranks: fact_1=21:39097, fact_2=6:74773, fact_3=92:100861, prefix_sum_12=27:79762, sum=119:120195)
- Layer 36: `/hess`, ` nasod`, ` soci`, `停`, ` predictions` (target ranks: fact_1=21:33950, fact_2=6:29202, fact_3=92:72045, prefix_sum_12=27:45142, sum=119:88998)
- Layer 37: `codeline`, `Quintal`, `镶嵌`, `悬挂`, `TreeLabel` (target ranks: fact_1=21:73368, fact_2=6:92377, fact_3=92:120886, prefix_sum_12=27:87924, sum=119:111862)
- Layer 38: ` germ`, `悬`, `悬挂`, `镶嵌`, ` crev` (target ranks: fact_1=21:47079, fact_2=6:62971, fact_3=92:117465, prefix_sum_12=27:53168, sum=119:102973)
- Layer 39: ` encomp`, ` germ`, ` .↵↵`, ` .`, ` unflagged` (target ranks: fact_1=21:67242, fact_2=6:115708, fact_3=92:118928, prefix_sum_12=27:85577, sum=119:112116)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` germ`, `镶嵌` (target ranks: fact_1=21:35806, fact_2=6:74228, fact_3=92:108967, prefix_sum_12=27:62458, sum=119:102873)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` germ` (target ranks: fact_1=21:22386, fact_2=6:44920, fact_3=92:85752, prefix_sum_12=27:28222, sum=119:91789)

### Filler position 49 (absolute token 564, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=21:126639, fact_2=6:128055, fact_3=92:126912, prefix_sum_12=27:123851, sum=119:124553)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=21:7455, fact_2=6:2705, fact_3=92:11761, prefix_sum_12=27:8670, sum=119:22577)
- Layer 20: `文本`, `站`, `裸露`, ` grounds`, ` Box` (target ranks: fact_1=21:19497, fact_2=6:1851, fact_3=92:56508, prefix_sum_12=27:17448, sum=119:66052)
- Layer 30: ` Answer`, `答案是`, ` ответ`, ` answer`, `答案` (target ranks: fact_1=21:118481, fact_2=6:113279, fact_3=92:124656, prefix_sum_12=27:124080, sum=119:121991)
- Layer 35: ` Answer`, ` answer`, `oNames`, `codeline`, ` ответ` (target ranks: fact_1=21:108136, fact_2=6:110496, fact_3=92:77441, prefix_sum_12=27:119503, sum=119:106627)
- Layer 36: ` Answer`, ` answer`, `坏`, ` reply`, `回答` (target ranks: fact_1=21:40192, fact_2=6:50875, fact_3=92:23923, prefix_sum_12=27:71784, sum=119:59141)
- Layer 37: `oNames`, `codeline`, ` encomp`, `}<?`, `lv` (target ranks: fact_1=21:102341, fact_2=6:113463, fact_3=92:109362, prefix_sum_12=27:119160, sum=119:117429)
- Layer 38: `oNames`, ` encomp`, `tanle`, `codeline`, `高等` (target ranks: fact_1=21:112053, fact_2=6:118390, fact_3=92:116750, prefix_sum_12=27:121698, sum=119:120962)
- Layer 39: `-ulo`, `�`, `oxygen`, ` cryptocur`, ` disadvant` (target ranks: fact_1=21:82946, fact_2=6:111853, fact_3=92:94071, prefix_sum_12=27:97986, sum=119:111339)
- Layer 40: ` .↵↵`, ` Answer`, ` .`, ` .↵`, `esez` (target ranks: fact_1=21:10315, fact_2=6:24681, fact_3=92:24424, prefix_sum_12=27:21575, sum=119:67856)
- Layer 41: ` Answer`, `Answer`, ` .↵↵`, ` .`, ` .↵` (target ranks: fact_1=21:2837, fact_2=6:2336, fact_3=92:10110, prefix_sum_12=27:5532, sum=119:47128)

### Filler position 50 (absolute token 565, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `-ulo` (target ranks: fact_1=21:122703, fact_2=6:126796, fact_3=92:121958, prefix_sum_12=27:121718, sum=119:114536)
- Layer 10: `EDMF`, ` dével`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=21:124163, fact_2=6:128468, fact_3=92:126246, prefix_sum_12=27:125964, sum=119:119876)
- Layer 20: `ait`, `能被`, `��`, ` Submission`, `平行` (target ranks: fact_1=21:11324, fact_2=6:3262, fact_3=92:13438, prefix_sum_12=27:21020, sum=119:68326)
- Layer 30: ` dekameters`, ` Paglin`, ` المطلع`, ` Uran`, ` encomp` (target ranks: fact_1=21:91481, fact_2=6:125511, fact_3=92:46623, prefix_sum_12=27:16103, sum=119:66438)
- Layer 35: `92`, ` Uran`, ` uranium`, `93`, `uran` (target ranks: fact_1=21:84458, fact_2=6:77834, fact_3=92:1, prefix_sum_12=27:13857, sum=119:3156)
- Layer 36: `92`, `93`, `88`, ` ninety`, `96` (target ranks: fact_1=21:125815, fact_2=6:104364, fact_3=92:1, prefix_sum_12=27:75212, sum=119:657)
- Layer 37: `92`, `93`, ` ninety`, ` noventa`, ` Ninety` (target ranks: fact_1=21:123984, fact_2=6:121323, fact_3=92:1, prefix_sum_12=27:116780, sum=119:2615)
- Layer 38: `92`, `98`, `99`, `93`, ` ninety` (target ranks: fact_1=21:92632, fact_2=6:124198, fact_3=92:1, prefix_sum_12=27:119523, sum=119:1180)
- Layer 39: `索`, `<｜place▁holder▁no▁689｜>`, `齐`, ` softening`, `}<?` (target ranks: fact_1=21:65420, fact_2=6:124154, fact_3=92:327, prefix_sum_12=27:122606, sum=119:7773)
- Layer 40: ` Answer`, `Answer`, ` answer`, ` atomic`, `atomic` (target ranks: fact_1=21:32162, fact_2=6:115161, fact_3=92:483, prefix_sum_12=27:123391, sum=119:4423)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: fact_1=21:1601, fact_2=6:1731, fact_3=92:603, prefix_sum_12=27:23057, sum=119:3440)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a question that requires adding three values together. Answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 50 filler tokens (a sequence of dots) before you answer.<｜User｜>Question: What is the atomic number of Helium plus the atomic number of Neon plus the atomic number of Sulfur?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>28<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Cobalt plus the atomic number of Selenium plus the atomic number of Promethium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>122<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Europium plus the atomic number of Tantalum plus the atomic number of Rhenium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>211<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Protactinium plus the atomic number of Thorium plus the atomic number of Tellurium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>233<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Neptunium plus the atomic number of Boron plus the atomic number of Gold?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>177<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Scandium plus the atomic number of Carbon plus the atomic number of Uranium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
