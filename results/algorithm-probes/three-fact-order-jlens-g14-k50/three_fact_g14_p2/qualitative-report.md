# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `119` (correct).
- No-filler answer: `119` (correct).
- Filler tokens: 50 tokens at absolute indices 516–565.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `fact_1=92` | 1 (L34, filler 1) | L34, filler 1 (rank 1) |
| J-Lens | `fact_2=21` | 1 (L34, filler 15) | L34, filler 15 (rank 1) |
| J-Lens | `fact_3=6` | 1 (L35, filler 14) | L34, filler 29 (rank 8) |
| J-Lens | `prefix_sum_12=113` | 2 (L40, filler 5) | L39, filler 5 (rank 6) |
| J-Lens | `sum=119` | 5 (L38, filler 1) | L38, filler 1 (rank 5) |
| Logit lens | `fact_1=92` | 1 (L35, filler 9) | L34, filler 1 (rank 5) |
| Logit lens | `fact_2=21` | 1 (L35, filler 15) | L32, filler 15 (rank 10) |
| Logit lens | `fact_3=6` | 2 (L37, filler 29) | L34, filler 14 (rank 5) |
| Logit lens | `prefix_sum_12=113` | 6 (L39, filler 16) | L37, filler 44 (rank 8) |
| Logit lens | `sum=119` | 9 (L39, filler 44) | L37, filler 44 (rank 10) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 516, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: fact_1=92:117899, fact_2=21:120996, fact_3=6:125221, prefix_sum_12=113:109361, sum=119:114359)
- Layer 10: `anta`, `s`, `fine`, `sem`, `locked` (target ranks: fact_1=92:53860, fact_2=21:39966, fact_3=6:32611, prefix_sum_12=113:56808, sum=119:55480)
- Layer 20: `足`, `扣`, `甸`, `表面`, `梯` (target ranks: fact_1=92:2163, fact_2=21:1041, fact_3=6:63, prefix_sum_12=113:13704, sum=119:20882)
- Layer 30: ` pakig`, ` talags`, `期望`, `拐`, `sett` (target ranks: fact_1=92:2295, fact_2=21:19704, fact_3=6:19203, prefix_sum_12=113:706, sum=119:7985)
- Layer 35: `92`, `93`, `238`, `98`, `96` (target ranks: fact_1=92:1, fact_2=21:22059, fact_3=6:5448, prefix_sum_12=113:267, sum=119:41)
- Layer 36: `92`, `93`, `238`, `105`, `98` (target ranks: fact_1=92:1, fact_2=21:75472, fact_3=6:23455, prefix_sum_12=113:72, sum=119:16)
- Layer 37: `92`, `93`, `238`, `98`, `斋` (target ranks: fact_1=92:1, fact_2=21:114607, fact_3=6:71947, prefix_sum_12=113:178, sum=119:30)
- Layer 38: `92`, `105`, `93`, `238`, `119` (target ranks: fact_1=92:1, fact_2=21:92855, fact_3=6:80262, prefix_sum_12=113:21, sum=119:5)
- Layer 39: `odea`, `105`, `ophe`, `ople`, `音符` (target ranks: fact_1=92:5373, fact_2=21:125286, fact_3=6:97096, prefix_sum_12=113:443, sum=119:11)
- Layer 40: `105`, ` ald`, ` dekameters`, `Ald`, ` talags` (target ranks: fact_1=92:176, fact_2=21:101683, fact_3=6:23091, prefix_sum_12=113:46, sum=119:9)
- Layer 41: ` .`, ` .↵↵`, `我已经`, ` ,`, `我只是` (target ranks: fact_1=92:7241, fact_2=21:87096, fact_3=6:15135, prefix_sum_12=113:3697, sum=119:3400)

### Filler position 2 (absolute token 517, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: fact_1=92:120497, fact_2=21:122667, fact_3=6:125201, prefix_sum_12=113:113637, sum=119:118261)
- Layer 10: ` Walker`, `从哪里`, `Walker`, `ait`, `atile` (target ranks: fact_1=92:27919, fact_2=21:17530, fact_3=6:6752, prefix_sum_12=113:43249, sum=119:41918)
- Layer 20: ` .----`, `往常`, ` .`, `平日里`, `ologists` (target ranks: fact_1=92:128882, fact_2=21:123318, fact_3=6:122326, prefix_sum_12=113:127149, sum=119:129166)
- Layer 30: ` dekameters`, ` hilabihan`, ` talags`, ` gihulagway`, ` pakig` (target ranks: fact_1=92:129059, fact_2=21:116010, fact_3=6:121056, prefix_sum_12=113:126076, sum=119:128350)
- Layer 35: ` hilabihan`, ` gihulagway`, ` .`, `}<?`, ` talags` (target ranks: fact_1=92:128407, fact_2=21:114972, fact_3=6:125922, prefix_sum_12=113:127004, sum=119:128442)
- Layer 36: ` hilabihan`, ` talags`, `enclose`, ` dunay`, ` .` (target ranks: fact_1=92:120496, fact_2=21:69686, fact_3=6:93754, prefix_sum_12=113:112201, sum=119:122915)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, `EDMF`, `繁体` (target ranks: fact_1=92:127861, fact_2=21:123296, fact_3=6:128362, prefix_sum_12=113:113613, sum=119:123342)
- Layer 38: ` .`, `}<?`, ` hilabihan`, `繁体`, ` talags` (target ranks: fact_1=92:126565, fact_2=21:104463, fact_3=6:126891, prefix_sum_12=113:107608, sum=119:119940)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `}<?`, ` hilabihan`, ` talags` (target ranks: fact_1=92:127714, fact_2=21:125677, fact_3=6:125974, prefix_sum_12=113:113180, sum=119:120072)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: fact_1=92:119879, fact_2=21:103654, fact_3=6:90251, prefix_sum_12=113:68756, sum=119:87238)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `美` (target ranks: fact_1=92:88145, fact_2=21:69463, fact_3=6:21630, prefix_sum_12=113:17924, sum=119:55483)

### Filler position 3 (absolute token 518, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:123148, fact_2=21:125069, fact_3=6:127350, prefix_sum_12=113:116740, sum=119:119800)
- Layer 10: `锁定`, ` Walker`, `ait`, `忑`, `Walker` (target ranks: fact_1=92:12809, fact_2=21:9365, fact_3=6:4315, prefix_sum_12=113:27349, sum=119:24164)
- Layer 20: `�`, `ka`, ` calculator`, `�`, `cape` (target ranks: fact_1=92:4780, fact_2=21:654, fact_3=6:587, prefix_sum_12=113:25099, sum=119:24228)
- Layer 30: ` Uran`, ` atomic`, ` Atomic`, `atomic`, `Atomic` (target ranks: fact_1=92:33081, fact_2=21:21426, fact_3=6:15167, prefix_sum_12=113:66769, sum=119:43430)
- Layer 35: ` atomic`, ` Atomic`, `atomic`, ` Uran`, `Atomic` (target ranks: fact_1=92:1027, fact_2=21:3802, fact_3=6:5681, prefix_sum_12=113:36885, sum=119:11291)
- Layer 36: ` atomic`, ` Atomic`, `atomic`, ` Uran`, `Atomic` (target ranks: fact_1=92:1895, fact_2=21:11176, fact_3=6:11782, prefix_sum_12=113:33692, sum=119:10118)
- Layer 37: ` Uran`, ` atomic`, ` uranium`, ` Atomic`, `atomic` (target ranks: fact_1=92:5441, fact_2=21:57274, fact_3=6:78132, prefix_sum_12=113:41638, sum=119:16255)
- Layer 38: ` Uran`, ` atomic`, ` uranium`, ` Atomic`, `atomic` (target ranks: fact_1=92:5371, fact_2=21:54563, fact_3=6:89443, prefix_sum_12=113:36272, sum=119:16430)
- Layer 39: ` Uran`, ` atomic`, ` uranium`, `ucl`, `�` (target ranks: fact_1=92:45809, fact_2=21:113108, fact_3=6:102996, prefix_sum_12=113:107567, sum=119:84914)
- Layer 40: ` Uran`, `U`, ` U`, ` Ne`, ` atomic` (target ranks: fact_1=92:3705, fact_2=21:88894, fact_3=6:38736, prefix_sum_12=113:61859, sum=119:45069)
- Layer 41: ` .`, ` atomic`, `atomic`, ` Uran`, `袄` (target ranks: fact_1=92:9124, fact_2=21:59281, fact_3=6:12779, prefix_sum_12=113:48097, sum=119:50342)

### Filler position 4 (absolute token 519, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:123433, fact_2=21:125625, fact_3=6:127549, prefix_sum_12=113:117972, sum=119:120601)
- Layer 10: ` Walker`, `ait`, `Walker`, `忑`, `锁定` (target ranks: fact_1=92:18253, fact_2=21:12734, fact_3=6:5928, prefix_sum_12=113:31488, sum=119:27159)
- Layer 20: `ait`, `忑`, `能被`, `胃癌`, `甸` (target ranks: fact_1=92:22372, fact_2=21:13696, fact_3=6:1693, prefix_sum_12=113:57671, sum=119:50982)
- Layer 30: `提问`, ` question`, `Tap`, ` glacier`, ` tap` (target ranks: fact_1=92:35693, fact_2=21:23937, fact_3=6:2620, prefix_sum_12=113:33171, sum=119:90784)
- Layer 35: `提问`, ` Question`, ` question`, `Question`, `question` (target ranks: fact_1=92:26731, fact_2=21:9594, fact_3=6:2943, prefix_sum_12=113:19184, sum=119:64453)
- Layer 36: `提问`, ` question`, ` Question`, `Question`, `询问` (target ranks: fact_1=92:21576, fact_2=21:13873, fact_3=6:6710, prefix_sum_12=113:18444, sum=119:43977)
- Layer 37: `提问`, `疑问`, ` question`, ` Question`, `.question` (target ranks: fact_1=92:41642, fact_2=21:25981, fact_3=6:22376, prefix_sum_12=113:13019, sum=119:48042)
- Layer 38: `提问`, `疑问`, `打磨`, `疑問`, `.question` (target ranks: fact_1=92:75691, fact_2=21:33993, fact_3=6:31093, prefix_sum_12=113:19127, sum=119:52649)
- Layer 39: `<｜begin▁of▁sentence｜>`, `�`, `orten`, ` Rutherford`, `提问` (target ranks: fact_1=92:95623, fact_2=21:106397, fact_3=6:94791, prefix_sum_12=113:51807, sum=119:63901)
- Layer 40: `提问`, ` Rutherford`, `eter`, `<｜begin▁of▁sentence｜>`, ` prompt` (target ranks: fact_1=92:64254, fact_2=21:82556, fact_3=6:44366, prefix_sum_12=113:26878, sum=119:24410)
- Layer 41: ` .`, `提问`, `袄`, `Answer`, `试一试` (target ranks: fact_1=92:38058, fact_2=21:42283, fact_3=6:10261, prefix_sum_12=113:21530, sum=119:18601)

### Filler position 5 (absolute token 520, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122944, fact_2=21:125326, fact_3=6:127280, prefix_sum_12=113:117845, sum=119:120391)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, `挪` (target ranks: fact_1=92:16353, fact_2=21:11088, fact_3=6:5322, prefix_sum_12=113:29622, sum=119:26504)
- Layer 20: ` LS`, `幽`, `LS`, `能被`, `cape` (target ranks: fact_1=92:8651, fact_2=21:2947, fact_3=6:534, prefix_sum_12=113:18754, sum=119:23706)
- Layer 30: ` pakig`, ` الشعاعيه`, `相加`, ` picnic`, `打完` (target ranks: fact_1=92:23126, fact_2=21:615, fact_3=6:6357, prefix_sum_12=113:7082, sum=119:36285)
- Layer 35: `21`, ` XXI`, ` تضيف`, `加入`, `二十一` (target ranks: fact_1=92:18941, fact_2=21:1, fact_3=6:1366, prefix_sum_12=113:20730, sum=119:35191)
- Layer 36: `21`, ` XXI`, `二十一`, `?datasetId`, ` الجرم` (target ranks: fact_1=92:107578, fact_2=21:1, fact_3=6:5798, prefix_sum_12=113:57270, sum=119:54793)
- Layer 37: `二十一`, `21`, ` XXI`, `?datasetId`, ` الجرم` (target ranks: fact_1=92:8585, fact_2=21:2, fact_3=6:8882, prefix_sum_12=113:27662, sum=119:23019)
- Layer 38: `}<?`, ` transcend`, ` المطلع`, `二十一`, `21` (target ranks: fact_1=92:4714, fact_2=21:5, fact_3=6:61570, prefix_sum_12=113:2058, sum=119:35523)
- Layer 39: `-ulo`, ` transcend`, ` šest`, ` embar`, `ople` (target ranks: fact_1=92:55586, fact_2=21:47968, fact_3=6:2901, prefix_sum_12=113:6, sum=119:1325)
- Layer 40: ` šest`, `113`, `117`, ` six`, `zik` (target ranks: fact_1=92:12771, fact_2=21:14324, fact_3=6:43, prefix_sum_12=113:2, sum=119:179)
- Layer 41: ` atomic`, ` .`, `*....|`, `秆`, ` uncovered` (target ranks: fact_1=92:25974, fact_2=21:11988, fact_3=6:1020, prefix_sum_12=113:48, sum=119:5181)

### Filler position 6 (absolute token 521, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122618, fact_2=21:125053, fact_3=6:127080, prefix_sum_12=113:117638, sum=119:120059)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12929, fact_2=21:10177, fact_3=6:4372, prefix_sum_12=113:27254, sum=119:23733)
- Layer 20: `top`, `ting`, `锁定`, `�`, `Username` (target ranks: fact_1=92:21231, fact_2=21:25204, fact_3=6:5119, prefix_sum_12=113:52474, sum=119:53406)
- Layer 30: `回答`, `acks`, `鞍`, `锁定`, ` answer` (target ranks: fact_1=92:5293, fact_2=21:5187, fact_3=6:2653, prefix_sum_12=113:48673, sum=119:48719)
- Layer 35: `acks`, ` smile`, `回答`, ` stimulus`, `刺激` (target ranks: fact_1=92:10918, fact_2=21:8542, fact_3=6:5749, prefix_sum_12=113:31111, sum=119:39664)
- Layer 36: `acks`, `刺激`, `agli`, `acl`, `ake` (target ranks: fact_1=92:18571, fact_2=21:19724, fact_3=6:13019, prefix_sum_12=113:36395, sum=119:43251)
- Layer 37: `刺激`, `acks`, `诚`, `acl`, ` pakig` (target ranks: fact_1=92:68050, fact_2=21:57384, fact_3=6:52067, prefix_sum_12=113:42620, sum=119:66779)
- Layer 38: ` pakig`, `acks`, `刺激`, `osit`, `itten` (target ranks: fact_1=92:88540, fact_2=21:77252, fact_3=6:59024, prefix_sum_12=113:55890, sum=119:82030)
- Layer 39: `lier`, ` Tit`, ` Rutherford`, `<｜begin▁of▁sentence｜>`, `osit` (target ranks: fact_1=92:126802, fact_2=21:120690, fact_3=6:122910, prefix_sum_12=113:126547, sum=119:126927)
- Layer 40: `dots`, ` dots`, ` talags`, `atomic`, ` dotted` (target ranks: fact_1=92:122694, fact_2=21:109916, fact_3=6:105044, prefix_sum_12=113:122689, sum=119:125317)
- Layer 41: ` .`, ` dotted`, ` dots`, ` filler`, `dots` (target ranks: fact_1=92:111042, fact_2=21:93110, fact_3=6:62125, prefix_sum_12=113:97737, sum=119:116030)

### Filler position 7 (absolute token 522, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122414, fact_2=21:124873, fact_3=6:126919, prefix_sum_12=113:117534, sum=119:119766)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12782, fact_2=21:9736, fact_3=6:4250, prefix_sum_12=113:26953, sum=119:23230)
- Layer 20: ` smile`, `锁定`, `ait`, ` cheer`, `足` (target ranks: fact_1=92:5149, fact_2=21:3426, fact_3=6:934, prefix_sum_12=113:20027, sum=119:21887)
- Layer 30: `Subt`, `缓`, ` Riv`, ` Cogn`, ` lung` (target ranks: fact_1=92:2660, fact_2=21:7421, fact_3=6:19190, prefix_sum_12=113:6941, sum=119:6134)
- Layer 35: ` future`, ` Heim`, ` met`, `Subt`, ` lung` (target ranks: fact_1=92:111, fact_2=21:1654, fact_3=6:5859, prefix_sum_12=113:531, sum=119:114)
- Layer 36: `anium`, ` biolog`, `匹配`, `109`, ` calculator` (target ranks: fact_1=92:459, fact_2=21:11069, fact_3=6:21215, prefix_sum_12=113:203, sum=119:36)
- Layer 37: `anium`, `}<?`, `114`, `理赔`, ` Erkännande` (target ranks: fact_1=92:152, fact_2=21:44761, fact_3=6:69104, prefix_sum_12=113:96, sum=119:39)
- Layer 38: `}<?`, `斋`, `�`, `iota`, `殿堂` (target ranks: fact_1=92:2028, fact_2=21:78033, fact_3=6:102268, prefix_sum_12=113:151, sum=119:65)
- Layer 39: `}<?`, `防护`, `ophe`, `hemer`, `opters` (target ranks: fact_1=92:102271, fact_2=21:118554, fact_3=6:110847, prefix_sum_12=113:1633, sum=119:166)
- Layer 40: ` talags`, `一百`, `反复`, ` repeated`, `anium` (target ranks: fact_1=92:75970, fact_2=21:97601, fact_3=6:51050, prefix_sum_12=113:597, sum=119:288)
- Layer 41: ` .`, `出不穷`, `我曾经`, ` repeatedly`, ` waiting` (target ranks: fact_1=92:88961, fact_2=21:92796, fact_3=6:43836, prefix_sum_12=113:12370, sum=119:9428)

### Filler position 8 (absolute token 523, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122176, fact_2=21:124674, fact_3=6:126717, prefix_sum_12=113:117374, sum=119:119550)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=92:10787, fact_2=21:7538, fact_3=6:2935, prefix_sum_12=113:24314, sum=119:20499)
- Layer 20: `足`, `锁定`, ` smile`, `Ta`, `ait` (target ranks: fact_1=92:10684, fact_2=21:4086, fact_3=6:1139, prefix_sum_12=113:24196, sum=119:30237)
- Layer 30: `sum`, ` calculator`, ` summing`, `加起来`, `Subt` (target ranks: fact_1=92:51273, fact_2=21:18529, fact_3=6:6461, prefix_sum_12=113:39653, sum=119:62966)
- Layer 35: `sum`, ` calculator`, ` suma`, ` equation`, ` Sum` (target ranks: fact_1=92:15891, fact_2=21:1881, fact_3=6:738, prefix_sum_12=113:6962, sum=119:18931)
- Layer 36: `sum`, ` Sum`, `Sum`, ` sum`, ` suma` (target ranks: fact_1=92:35115, fact_2=21:6175, fact_3=6:2536, prefix_sum_12=113:8805, sum=119:18475)
- Layer 37: ` Sum`, ` sum`, `Sum`, `sum`, ` sums` (target ranks: fact_1=92:54729, fact_2=21:12005, fact_3=6:13533, prefix_sum_12=113:6493, sum=119:22541)
- Layer 38: ` Sum`, ` sum`, `sum`, ` sums`, `Sum` (target ranks: fact_1=92:61300, fact_2=21:19275, fact_3=6:22592, prefix_sum_12=113:12957, sum=119:37158)
- Layer 39: `}<?`, ` Sum`, `累`, ` sum`, `osum` (target ranks: fact_1=92:105081, fact_2=21:91370, fact_3=6:85488, prefix_sum_12=113:86218, sum=119:93587)
- Layer 40: ` Rutherford`, `乐乐`, `enclose`, `留存`, `累` (target ranks: fact_1=92:101745, fact_2=21:54390, fact_3=6:25023, prefix_sum_12=113:28500, sum=119:70185)
- Layer 41: ` .`, `鹉`, `我曾经`, ` Rutherford`, ` ` (target ranks: fact_1=92:99192, fact_2=21:88282, fact_3=6:15692, prefix_sum_12=113:34285, sum=119:79720)

### Filler position 9 (absolute token 524, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122235, fact_2=21:124499, fact_3=6:126605, prefix_sum_12=113:117094, sum=119:119331)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11039, fact_2=21:7732, fact_3=6:2981, prefix_sum_12=113:24463, sum=119:20503)
- Layer 20: `能被`, ` ternary`, ` Agri`, `挪`, `锁定` (target ranks: fact_1=92:4387, fact_2=21:1745, fact_3=6:419, prefix_sum_12=113:15761, sum=119:12780)
- Layer 30: `加起来`, `寨`, ` ---|---|---|---|---|---|---`, ` encomp`, `总体` (target ranks: fact_1=92:630, fact_2=21:9552, fact_3=6:35571, prefix_sum_12=113:888, sum=119:4482)
- Layer 35: `92`, `93`, `90`, `79`, `88` (target ranks: fact_1=92:1, fact_2=21:5743, fact_3=6:2680, prefix_sum_12=113:496, sum=119:74)
- Layer 36: `92`, `93`, `九十`, `94`, `90` (target ranks: fact_1=92:1, fact_2=21:78597, fact_3=6:20051, prefix_sum_12=113:123, sum=119:37)
- Layer 37: `92`, `93`, ` ninety`, `九十`, `91` (target ranks: fact_1=92:1, fact_2=21:118515, fact_3=6:70573, prefix_sum_12=113:1051, sum=119:100)
- Layer 38: `92`, `93`, ` ninety`, ` Ninety`, `99` (target ranks: fact_1=92:1, fact_2=21:115613, fact_3=6:72930, prefix_sum_12=113:188, sum=119:24)
- Layer 39: `105`, `106`, `103`, `102`, `107` (target ranks: fact_1=92:1474, fact_2=21:124777, fact_3=6:14029, prefix_sum_12=113:79, sum=119:7)
- Layer 40: ` dekameters`, `lisitry`, `106`, `107`, `119` (target ranks: fact_1=92:180, fact_2=21:119639, fact_3=6:1551, prefix_sum_12=113:67, sum=119:5)
- Layer 41: ` atomic`, `��`, `因为这些`, `))))`, `出不穷` (target ranks: fact_1=92:2152, fact_2=21:93282, fact_3=6:652, prefix_sum_12=113:963, sum=119:238)

### Filler position 10 (absolute token 525, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=92:122028, fact_2=21:124360, fact_3=6:126447, prefix_sum_12=113:116982, sum=119:119275)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11243, fact_2=21:7495, fact_3=6:2874, prefix_sum_12=113:25021, sum=119:20887)
- Layer 20: `挪`, ` Walker`, `胃癌`, `锁定`, `幽` (target ranks: fact_1=92:6038, fact_2=21:2329, fact_3=6:575, prefix_sum_12=113:20221, sum=119:18524)
- Layer 30: ` tap`, `Tap`, `obin`, `tap`, `幽` (target ranks: fact_1=92:2774, fact_2=21:1962, fact_3=6:1861, prefix_sum_12=113:26107, sum=119:25151)
- Layer 35: `92`, ` uranium`, ` Uran`, `922`, `88` (target ranks: fact_1=92:1, fact_2=21:12426, fact_3=6:4217, prefix_sum_12=113:9691, sum=119:3490)
- Layer 36: `92`, `922`, `93`, ` ninety`, `092` (target ranks: fact_1=92:1, fact_2=21:64106, fact_3=6:45368, prefix_sum_12=113:30455, sum=119:9730)
- Layer 37: `92`, ` ninety`, `922`, ` Ninety`, `93` (target ranks: fact_1=92:1, fact_2=21:121540, fact_3=6:120693, prefix_sum_12=113:57357, sum=119:21531)
- Layer 38: `92`, ` ninety`, `}<?`, `922`, ` uranium` (target ranks: fact_1=92:1, fact_2=21:125014, fact_3=6:124083, prefix_sum_12=113:78636, sum=119:40335)
- Layer 39: `92`, `}<?`, ` dekameters`, `桃子`, `anic` (target ranks: fact_1=92:1, fact_2=21:107957, fact_3=6:118052, prefix_sum_12=113:112635, sum=119:91546)
- Layer 40: `atomic`, `}<?`, ` atomic`, `等待着`, ` talags` (target ranks: fact_1=92:15308, fact_2=21:62192, fact_3=6:68277, prefix_sum_12=113:55397, sum=119:49932)
- Layer 41: `atomic`, ` .`, ` atomic`, `着了`, `!!!!!!!!` (target ranks: fact_1=92:26634, fact_2=21:53769, fact_3=6:4811, prefix_sum_12=113:35212, sum=119:55254)

### Filler position 11 (absolute token 526, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:122269, fact_2=21:124496, fact_3=6:126541, prefix_sum_12=113:117165, sum=119:119348)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11014, fact_2=21:7244, fact_3=6:2686, prefix_sum_12=113:24462, sum=119:20610)
- Layer 20: `锁定`, `胃癌`, `幽`, `足`, ` Tears` (target ranks: fact_1=92:9795, fact_2=21:3562, fact_3=6:1173, prefix_sum_12=113:23163, sum=119:27457)
- Layer 30: `�`, `acin`, ` Atomic`, `atomic`, ` Attorney` (target ranks: fact_1=92:32843, fact_2=21:11619, fact_3=6:5991, prefix_sum_12=113:31158, sum=119:47457)
- Layer 35: `锁定`, `幽`, ` Younger`, `重复`, ` tap` (target ranks: fact_1=92:26859, fact_2=21:5503, fact_3=6:3043, prefix_sum_12=113:33459, sum=119:42887)
- Layer 36: `反复`, ` repeated`, ` tap`, `熟悉`, `羊` (target ranks: fact_1=92:24141, fact_2=21:6595, fact_3=6:2885, prefix_sum_12=113:29536, sum=119:29181)
- Layer 37: `itore`, `坏`, `银杏`, `enclose`, ` Atomic` (target ranks: fact_1=92:84785, fact_2=21:35447, fact_3=6:32326, prefix_sum_12=113:27267, sum=119:38211)
- Layer 38: ` Atomic`, `坏`, `�`, ` fusion`, ` atomic` (target ranks: fact_1=92:103516, fact_2=21:45738, fact_3=6:49983, prefix_sum_12=113:40706, sum=119:49672)
- Layer 39: `<｜begin▁of▁sentence｜>`, `�`, ` Rutherford`, `}<?`, `繁体` (target ranks: fact_1=92:106380, fact_2=21:82745, fact_3=6:99038, prefix_sum_12=113:92434, sum=119:101892)
- Layer 40: ` .`, ` Rutherford`, `<｜begin▁of▁sentence｜>`, `enclose`, `šk` (target ranks: fact_1=92:63985, fact_2=21:47420, fact_3=6:47380, prefix_sum_12=113:48613, sum=119:87224)
- Layer 41: ` .`, ` `, `鹉`, ` .↵↵`, `矶` (target ranks: fact_1=92:27758, fact_2=21:44435, fact_3=6:7884, prefix_sum_12=113:15237, sum=119:51186)

### Filler position 12 (absolute token 527, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:122387, fact_2=21:124399, fact_3=6:126537, prefix_sum_12=113:116925, sum=119:119185)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:10185, fact_2=21:6654, fact_3=6:2300, prefix_sum_12=113:23821, sum=119:19735)
- Layer 20: ` LS`, `LS`, `ait`, `挪`, `锁定` (target ranks: fact_1=92:3152, fact_2=21:1602, fact_3=6:275, prefix_sum_12=113:13123, sum=119:10797)
- Layer 30: `aci`, ` Cage`, `总体`, `柿子`, ` cage` (target ranks: fact_1=92:6514, fact_2=21:1006, fact_3=6:3095, prefix_sum_12=113:13118, sum=119:14153)
- Layer 35: `ilig`, `28`, ` labor`, `29`, ` ternary` (target ranks: fact_1=92:651, fact_2=21:64, fact_3=6:641, prefix_sum_12=113:4798, sum=119:3998)
- Layer 36: `}<?`, `43`, `做出`, `36`, `acy` (target ranks: fact_1=92:4288, fact_2=21:40, fact_3=6:20149, prefix_sum_12=113:3619, sum=119:2856)
- Layer 37: `}<?`, `92`, ` confusing`, `做出`, `93` (target ranks: fact_1=92:2, fact_2=21:1646, fact_3=6:67719, prefix_sum_12=113:205, sum=119:174)
- Layer 38: `}<?`, ` Cooper`, `轻`, `做出`, `軽` (target ranks: fact_1=92:20, fact_2=21:12835, fact_3=6:109649, prefix_sum_12=113:588, sum=119:116)
- Layer 39: `103`, `107`, `109`, `105`, `106` (target ranks: fact_1=92:41110, fact_2=21:111466, fact_3=6:97354, prefix_sum_12=113:11, sum=119:12)
- Layer 40: `103`, `107`, `109`, ` dekameters`, `106` (target ranks: fact_1=92:78, fact_2=21:92913, fact_3=6:42972, prefix_sum_12=113:9, sum=119:19)
- Layer 41: ` atomic`, `atomic`, `原子`, ` Atomic`, `装甲` (target ranks: fact_1=92:2379, fact_2=21:72836, fact_3=6:9862, prefix_sum_12=113:225, sum=119:3866)

### Filler position 13 (absolute token 528, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:122540, fact_2=21:124513, fact_3=6:126557, prefix_sum_12=113:117191, sum=119:119343)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12255, fact_2=21:7937, fact_3=6:3184, prefix_sum_12=113:25743, sum=119:21679)
- Layer 20: `锁定`, ` ES`, `忑`, `ait`, ` smile` (target ranks: fact_1=92:14982, fact_2=21:7450, fact_3=6:2439, prefix_sum_12=113:25858, sum=119:33626)
- Layer 30: `鞍`, `Tap`, ` tap`, ` future`, ` ES` (target ranks: fact_1=92:29479, fact_2=21:3049, fact_3=6:7779, prefix_sum_12=113:11432, sum=119:45564)
- Layer 35: ` labor`, `ilig`, `Cos`, ` met`, `锁定` (target ranks: fact_1=92:58559, fact_2=21:53, fact_3=6:6315, prefix_sum_12=113:39809, sum=119:56665)
- Layer 36: `二十一`, `21`, `adal`, ` tap`, ` stabil` (target ranks: fact_1=92:83840, fact_2=21:2, fact_3=6:9615, prefix_sum_12=113:66372, sum=119:53379)
- Layer 37: `二十一`, `冻`, `acons`, `acos`, ` consum` (target ranks: fact_1=92:120509, fact_2=21:20, fact_3=6:51794, prefix_sum_12=113:67782, sum=119:72405)
- Layer 38: `二十一`, `acons`, `}<?`, `21`, `累` (target ranks: fact_1=92:124072, fact_2=21:4, fact_3=6:76570, prefix_sum_12=113:72432, sum=119:91537)
- Layer 39: `hemer`, `�乐`, `�`, `}<?`, `累` (target ranks: fact_1=92:115839, fact_2=21:15512, fact_3=6:103430, prefix_sum_12=113:63103, sum=119:87122)
- Layer 40: `carbon`, `�`, `冰冰`, ` Rutherford`, `关` (target ranks: fact_1=92:41651, fact_2=21:8648, fact_3=6:42795, prefix_sum_12=113:15435, sum=119:42293)
- Layer 41: ` .`, `鹉`, `矶`, ` .↵↵`, `等着` (target ranks: fact_1=92:28017, fact_2=21:16497, fact_3=6:9889, prefix_sum_12=113:6357, sum=119:30211)

### Filler position 14 (absolute token 529, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:122944, fact_2=21:124745, fact_3=6:126773, prefix_sum_12=113:117645, sum=119:119716)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11379, fact_2=21:7435, fact_3=6:2943, prefix_sum_12=113:25075, sum=119:20891)
- Layer 20: `锁定`, `挪`, `ait`, `cape`, `us` (target ranks: fact_1=92:12076, fact_2=21:2680, fact_3=6:914, prefix_sum_12=113:29925, sum=119:32829)
- Layer 30: ` Heim`, `平行`, `ayi`, `cape`, `acic` (target ranks: fact_1=92:36560, fact_2=21:6286, fact_3=6:1748, prefix_sum_12=113:43948, sum=119:61846)
- Layer 35: `6`, ` six`, ` Six`, `six`, `-six` (target ranks: fact_1=92:66294, fact_2=21:33744, fact_3=6:1, prefix_sum_12=113:83756, sum=119:84550)
- Layer 36: `6`, ` six`, ` Six`, ` Sixth`, `six` (target ranks: fact_1=92:102952, fact_2=21:84052, fact_3=6:1, prefix_sum_12=113:91735, sum=119:87250)
- Layer 37: ` Sixth`, ` six`, ` sixth`, ` šest`, ` Six` (target ranks: fact_1=92:126636, fact_2=21:123523, fact_3=6:7, prefix_sum_12=113:115014, sum=119:109043)
- Layer 38: ` Sixth`, ` sixth`, `碳`, ` šest`, `六` (target ranks: fact_1=92:115360, fact_2=21:119117, fact_3=6:23, prefix_sum_12=113:109753, sum=119:107108)
- Layer 39: ` Sixth`, ` Six`, `六`, ` šest`, ` carbon` (target ranks: fact_1=92:126050, fact_2=21:98311, fact_3=6:93, prefix_sum_12=113:115655, sum=119:116090)
- Layer 40: `atomic`, ` atomic`, ` Rutherford`, `六`, ` Six` (target ranks: fact_1=92:106627, fact_2=21:71384, fact_3=6:26, prefix_sum_12=113:68386, sum=119:79894)
- Layer 41: `atomic`, ` atomic`, ` .`, `鹉`, ` Atomic` (target ranks: fact_1=92:68056, fact_2=21:48186, fact_3=6:165, prefix_sum_12=113:33543, sum=119:49974)

### Filler position 15 (absolute token 530, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=92:123268, fact_2=21:124927, fact_3=6:126848, prefix_sum_12=113:118261, sum=119:120159)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11706, fact_2=21:7472, fact_3=6:2996, prefix_sum_12=113:25574, sum=119:21397)
- Layer 20: ` LS`, `LS`, `cape`, `Ta`, `挪` (target ranks: fact_1=92:5358, fact_2=21:1181, fact_3=6:307, prefix_sum_12=113:18486, sum=119:18313)
- Layer 30: ` Heim`, ` ternary`, `柿子`, ` labor`, `Ternary` (target ranks: fact_1=92:13963, fact_2=21:164, fact_3=6:6939, prefix_sum_12=113:21948, sum=119:42541)
- Layer 35: `二十一`, `21`, ` XXI`, ` Sc`, ` Scand` (target ranks: fact_1=92:116997, fact_2=21:2, fact_3=6:97469, prefix_sum_12=113:94383, sum=119:61232)
- Layer 36: `二十一`, `21`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=92:124296, fact_2=21:2, fact_3=6:119948, prefix_sum_12=113:123545, sum=119:108665)
- Layer 37: `二十一`, `21`, ` XXI`, `twenty`, ` twenty` (target ranks: fact_1=92:119006, fact_2=21:2, fact_3=6:124258, prefix_sum_12=113:123348, sum=119:111205)
- Layer 38: `二十一`, `21`, ` XXI`, `散射`, `斯科` (target ranks: fact_1=92:110683, fact_2=21:2, fact_3=6:124908, prefix_sum_12=113:82846, sum=119:96640)
- Layer 39: `二十一`, `orten`, `lier`, ` transcend`, ` Nij` (target ranks: fact_1=92:102251, fact_2=21:64, fact_3=6:79127, prefix_sum_12=113:102234, sum=119:103402)
- Layer 40: `二十一`, `}<?`, ` ple`, `orten`, `atomic` (target ranks: fact_1=92:43295, fact_2=21:18, fact_3=6:12443, prefix_sum_12=113:54342, sum=119:44682)
- Layer 41: `二十一`, ` atomic`, `atomic`, ` .`, ` twenty` (target ranks: fact_1=92:52548, fact_2=21:113, fact_3=6:839, prefix_sum_12=113:56152, sum=119:75624)

### Filler position 16 (absolute token 531, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:123187, fact_2=21:124707, fact_3=6:126637, prefix_sum_12=113:118160, sum=119:120029)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12127, fact_2=21:7540, fact_3=6:2991, prefix_sum_12=113:26088, sum=119:21463)
- Layer 20: ` LS`, `锁定`, `LS`, `Ta`, `ait` (target ranks: fact_1=92:2514, fact_2=21:767, fact_3=6:101, prefix_sum_12=113:11633, sum=119:8520)
- Layer 30: ` ---|---|---|---|---|---|---`, ` pakig`, `俯`, `36`, `45` (target ranks: fact_1=92:3291, fact_2=21:4580, fact_3=6:22104, prefix_sum_12=113:6265, sum=119:10779)
- Layer 35: `45`, `43`, `37`, `49`, `55` (target ranks: fact_1=92:2436, fact_2=21:190, fact_3=6:9336, prefix_sum_12=113:2972, sum=119:8635)
- Layer 36: `45`, `43`, `49`, `37`, `36` (target ranks: fact_1=92:9734, fact_2=21:20552, fact_3=6:31711, prefix_sum_12=113:2004, sum=119:5557)
- Layer 37: `}<?`, `49`, `47`, ` ---|---|---|---|---|---|---`, `46` (target ranks: fact_1=92:18, fact_2=21:70456, fact_3=6:66278, prefix_sum_12=113:759, sum=119:903)
- Layer 38: `}<?`, `斋`, ` transcend`, `图画`, `rá` (target ranks: fact_1=92:221, fact_2=21:120934, fact_3=6:83866, prefix_sum_12=113:3427, sum=119:3693)
- Layer 39: `107`, `103`, `109`, `106`, `117` (target ranks: fact_1=92:46375, fact_2=21:116113, fact_3=6:14335, prefix_sum_12=113:7, sum=119:34)
- Layer 40: ` atomic`, `107`, `atomic`, ` Atomic`, `103` (target ranks: fact_1=92:174, fact_2=21:96639, fact_3=6:788, prefix_sum_12=113:11, sum=119:24)
- Layer 41: ` atomic`, `atomic`, `原子`, ` Atomic`, `Atomic` (target ranks: fact_1=92:421, fact_2=21:55561, fact_3=6:153, prefix_sum_12=113:79, sum=119:330)

### Filler position 17 (absolute token 532, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:123500, fact_2=21:124994, fact_3=6:126849, prefix_sum_12=113:118498, sum=119:120252)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:13390, fact_2=21:8547, fact_3=6:3624, prefix_sum_12=113:27105, sum=119:22611)
- Layer 20: `能被`, `ait`, `距`, `ative`, ` Tears` (target ranks: fact_1=92:7244, fact_2=21:2379, fact_3=6:795, prefix_sum_12=113:13845, sum=119:17078)
- Layer 30: `acos`, `�`, ` EC`, `总体`, ` ES` (target ranks: fact_1=92:36518, fact_2=21:8737, fact_3=6:12749, prefix_sum_12=113:12701, sum=119:48032)
- Layer 35: `ilig`, `水土`, `俯`, `锁定`, `劳动关系` (target ranks: fact_1=92:20600, fact_2=21:926, fact_3=6:8157, prefix_sum_12=113:22052, sum=119:44933)
- Layer 36: `俯`, ` upright`, `cod`, `结构化`, ` EC` (target ranks: fact_1=92:42100, fact_2=21:2478, fact_3=6:23736, prefix_sum_12=113:12345, sum=119:26098)
- Layer 37: `}<?`, `acons`, `关`, `透过`, `学法` (target ranks: fact_1=92:90961, fact_2=21:26769, fact_3=6:100192, prefix_sum_12=113:22049, sum=119:43326)
- Layer 38: `}<?`, `zat`, `acons`, `打包`, `fusion` (target ranks: fact_1=92:79411, fact_2=21:96972, fact_3=6:109911, prefix_sum_12=113:21970, sum=119:36335)
- Layer 39: `}<?`, `zat`, `坏的`, `打磨`, `繁体` (target ranks: fact_1=92:60087, fact_2=21:85790, fact_3=6:87972, prefix_sum_12=113:6439, sum=119:10120)
- Layer 40: ` atomic`, `atomic`, `坏`, `坏的`, ` Atomic` (target ranks: fact_1=92:918, fact_2=21:42963, fact_3=6:26672, prefix_sum_12=113:301, sum=119:1364)
- Layer 41: ` .`, ` atomic`, `atomic`, ` .↵↵`, ` ,` (target ranks: fact_1=92:805, fact_2=21:32260, fact_3=6:2433, prefix_sum_12=113:147, sum=119:1384)

### Filler position 18 (absolute token 533, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:123949, fact_2=21:125280, fact_3=6:127037, prefix_sum_12=113:119142, sum=119:120794)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12238, fact_2=21:7856, fact_3=6:3174, prefix_sum_12=113:26717, sum=119:22188)
- Layer 20: ` Walker`, ` smile`, `锁定`, `Walker`, `ait` (target ranks: fact_1=92:10681, fact_2=21:4816, fact_3=6:2313, prefix_sum_12=113:22859, sum=119:24235)
- Layer 30: `Wil`, `atan`, `Tap`, `�`, ` Wil` (target ranks: fact_1=92:7236, fact_2=21:2686, fact_3=6:2131, prefix_sum_12=113:18197, sum=119:24381)
- Layer 35: `obin`, ` Wil`, `�`, `Wil`, `92` (target ranks: fact_1=92:5, fact_2=21:2674, fact_3=6:3252, prefix_sum_12=113:16219, sum=119:4985)
- Layer 36: `92`, `留存`, `�`, ` Wil`, ` uranium` (target ranks: fact_1=92:1, fact_2=21:25705, fact_3=6:30995, prefix_sum_12=113:19555, sum=119:5759)
- Layer 37: ` Uran`, `}<?`, ` uranium`, `92`, `uran` (target ranks: fact_1=92:4, fact_2=21:89734, fact_3=6:113202, prefix_sum_12=113:16255, sum=119:6578)
- Layer 38: `}<?`, ` Uran`, ` uranium`, `ucl`, `uran` (target ranks: fact_1=92:6, fact_2=21:104473, fact_3=6:122335, prefix_sum_12=113:38702, sum=119:21153)
- Layer 39: `}<?`, ` Uran`, `92`, ` uranium`, `�` (target ranks: fact_1=92:3, fact_2=21:101455, fact_3=6:108303, prefix_sum_12=113:94312, sum=119:56910)
- Layer 40: ` Uran`, `}<?`, `atomic`, ` uranium`, ` Ur` (target ranks: fact_1=92:344, fact_2=21:79602, fact_3=6:54500, prefix_sum_12=113:48917, sum=119:53398)
- Layer 41: `atomic`, ` atomic`, ` Uran`, ` uranium`, `less` (target ranks: fact_1=92:115, fact_2=21:36314, fact_3=6:5032, prefix_sum_12=113:20982, sum=119:37015)

### Filler position 19 (absolute token 534, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124181, fact_2=21:125314, fact_3=6:127029, prefix_sum_12=113:119515, sum=119:121087)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11640, fact_2=21:7496, fact_3=6:2925, prefix_sum_12=113:26047, sum=119:21176)
- Layer 20: `ait`, `锁定`, `拆`, ` Walker`, ` engaging` (target ranks: fact_1=92:18657, fact_2=21:6374, fact_3=6:4667, prefix_sum_12=113:36039, sum=119:37668)
- Layer 30: `拆`, ` calculator`, `calculator`, `Calculator`, `Subt` (target ranks: fact_1=92:41148, fact_2=21:12379, fact_3=6:9868, prefix_sum_12=113:43948, sum=119:59683)
- Layer 35: ` calculator`, `足`, `calculator`, `锁定`, `加法` (target ranks: fact_1=92:33843, fact_2=21:5574, fact_3=6:5778, prefix_sum_12=113:21891, sum=119:33427)
- Layer 36: ` calculator`, `询问`, ` tap`, `calculator`, ` addition` (target ranks: fact_1=92:33231, fact_2=21:8047, fact_3=6:9725, prefix_sum_12=113:13681, sum=119:24130)
- Layer 37: `加减`, ` addition`, `加法`, `}<?`, `adding` (target ranks: fact_1=92:72409, fact_2=21:27494, fact_3=6:56382, prefix_sum_12=113:13511, sum=119:35396)
- Layer 38: `加减`, `}<?`, ` Sum`, ` sums`, ` addition` (target ranks: fact_1=92:83058, fact_2=21:45066, fact_3=6:76175, prefix_sum_12=113:13740, sum=119:35698)
- Layer 39: `}<?`, `下沉`, `铎`, `acons`, ` Rutherford` (target ranks: fact_1=92:61646, fact_2=21:65096, fact_3=6:101161, prefix_sum_12=113:30876, sum=119:40866)
- Layer 40: `下沉`, `冰冰`, `留存`, ` consum`, `}<?` (target ranks: fact_1=92:28562, fact_2=21:18423, fact_3=6:41414, prefix_sum_12=113:2672, sum=119:16679)
- Layer 41: ` .`, ` `, `冰冰`, `有下列`, `留存` (target ranks: fact_1=92:9929, fact_2=21:26205, fact_3=6:13438, prefix_sum_12=113:6721, sum=119:20490)

### Filler position 20 (absolute token 535, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124337, fact_2=21:125303, fact_3=6:127065, prefix_sum_12=113:119443, sum=119:121020)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11130, fact_2=21:7359, fact_3=6:2842, prefix_sum_12=113:25014, sum=119:19854)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `忑` (target ranks: fact_1=92:19296, fact_2=21:7448, fact_3=6:4845, prefix_sum_12=113:40822, sum=119:41726)
- Layer 30: ` uranium`, ` Uran`, `U`, ` U`, `好啊` (target ranks: fact_1=92:22322, fact_2=21:7968, fact_3=6:13996, prefix_sum_12=113:60545, sum=119:88755)
- Layer 35: ` Uran`, ` uranium`, ` U`, ` UR`, ` Ur` (target ranks: fact_1=92:14, fact_2=21:4313, fact_3=6:6915, prefix_sum_12=113:18288, sum=119:8150)
- Layer 36: ` Uran`, ` uranium`, `92`, ` Ur`, `uran` (target ranks: fact_1=92:3, fact_2=21:29007, fact_3=6:36870, prefix_sum_12=113:25735, sum=119:11458)
- Layer 37: ` Uran`, ` uranium`, `uran`, `铀`, ` Uranus` (target ranks: fact_1=92:8, fact_2=21:91766, fact_3=6:102593, prefix_sum_12=113:24424, sum=119:15091)
- Layer 38: ` Uran`, ` uranium`, `uran`, `}<?`, `铀` (target ranks: fact_1=92:15, fact_2=21:104869, fact_3=6:116317, prefix_sum_12=113:34388, sum=119:25037)
- Layer 39: ` Uran`, ` uranium`, `uran`, `}<?`, `铀` (target ranks: fact_1=92:7485, fact_2=21:95463, fact_3=6:98482, prefix_sum_12=113:102868, sum=119:83278)
- Layer 40: ` Uran`, ` uranium`, `U`, ` U`, `uran` (target ranks: fact_1=92:17736, fact_2=21:62499, fact_3=6:44756, prefix_sum_12=113:58482, sum=119:79497)
- Layer 41: ` Uran`, ` uranium`, ` atomic`, `atomic`, `铀` (target ranks: fact_1=92:960, fact_2=21:9130, fact_3=6:1705, prefix_sum_12=113:16374, sum=119:34950)

### Filler position 21 (absolute token 536, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124416, fact_2=21:125254, fact_3=6:126998, prefix_sum_12=113:119545, sum=119:121049)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11475, fact_2=21:7397, fact_3=6:2940, prefix_sum_12=113:24607, sum=119:20069)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, `能被` (target ranks: fact_1=92:20623, fact_2=21:8726, fact_3=6:5093, prefix_sum_12=113:36539, sum=119:36427)
- Layer 30: `acos`, `ragma`, `支配`, `锁定`, ` reserved` (target ranks: fact_1=92:66394, fact_2=21:27358, fact_3=6:45016, prefix_sum_12=113:61671, sum=119:89112)
- Layer 35: `�`, ` plut`, ` Plut`, `anium`, `铂` (target ranks: fact_1=92:29525, fact_2=21:7361, fact_3=6:10127, prefix_sum_12=113:37001, sum=119:52001)
- Layer 36: ` plut`, ` Plut`, `�`, `anium`, ` Pluto` (target ranks: fact_1=92:7602, fact_2=21:22622, fact_3=6:16559, prefix_sum_12=113:12262, sum=119:33096)
- Layer 37: ` plut`, ` Plut`, `�`, ` Pluto`, `�` (target ranks: fact_1=92:17830, fact_2=21:62961, fact_3=6:67154, prefix_sum_12=113:9819, sum=119:37276)
- Layer 38: ` Plut`, ` plut`, `�`, ` Pluto`, `�` (target ranks: fact_1=92:29041, fact_2=21:71380, fact_3=6:81950, prefix_sum_12=113:14428, sum=119:50478)
- Layer 39: ` Plut`, ` plut`, ` Pluto`, `�`, ` Americ` (target ranks: fact_1=92:47202, fact_2=21:71076, fact_3=6:82574, prefix_sum_12=113:43825, sum=119:57075)
- Layer 40: `�`, ` Rutherford`, `B`, ` Americ`, ` Law` (target ranks: fact_1=92:27732, fact_2=21:39017, fact_3=6:10048, prefix_sum_12=113:15901, sum=119:12567)
- Layer 41: ` Uran`, ` uranium`, ` Bism`, ` Rutherford`, `utherford` (target ranks: fact_1=92:4199, fact_2=21:16795, fact_3=6:673, prefix_sum_12=113:10896, sum=119:9036)

### Filler position 22 (absolute token 537, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124427, fact_2=21:125269, fact_3=6:127002, prefix_sum_12=113:119606, sum=119:121079)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:10875, fact_2=21:6838, fact_3=6:2538, prefix_sum_12=113:23853, sum=119:19621)
- Layer 20: `ait`, ` smile`, `锁定`, `胃癌`, `幽` (target ranks: fact_1=92:11582, fact_2=21:4101, fact_3=6:942, prefix_sum_12=113:23375, sum=119:26359)
- Layer 30: `acin`, `�`, `平行`, ` tap`, `碳` (target ranks: fact_1=92:42603, fact_2=21:11635, fact_3=6:3856, prefix_sum_12=113:35389, sum=119:62339)
- Layer 35: `锁定`, `羊`, ` tap`, ` reserved`, `俯` (target ranks: fact_1=92:47266, fact_2=21:11492, fact_3=6:3278, prefix_sum_12=113:34686, sum=119:61570)
- Layer 36: `羊`, ` tap`, `俯`, `acin`, `反复` (target ranks: fact_1=92:39234, fact_2=21:14274, fact_3=6:2683, prefix_sum_12=113:25213, sum=119:40109)
- Layer 37: `}<?`, `坏`, `carbon`, `anium`, `俯` (target ranks: fact_1=92:97648, fact_2=21:50392, fact_3=6:26832, prefix_sum_12=113:29050, sum=119:54697)
- Layer 38: `坏`, `}<?`, `anium`, `carbon`, `osit` (target ranks: fact_1=92:96003, fact_2=21:47731, fact_3=6:33881, prefix_sum_12=113:39110, sum=119:53460)
- Layer 39: `}<?`, `�`, `�`, `坏`, `<｜begin▁of▁sentence｜>` (target ranks: fact_1=92:92109, fact_2=21:73027, fact_3=6:72272, prefix_sum_12=113:56568, sum=119:78942)
- Layer 40: `�`, `坏`, ` Rutherford`, ` .`, `osit` (target ranks: fact_1=92:37923, fact_2=21:26254, fact_3=6:12505, prefix_sum_12=113:19675, sum=119:49917)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, ` uranium`, `袄` (target ranks: fact_1=92:12730, fact_2=21:14893, fact_3=6:540, prefix_sum_12=113:7077, sum=119:29129)

### Filler position 23 (absolute token 538, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124866, fact_2=21:125523, fact_3=6:127163, prefix_sum_12=113:120340, sum=119:121671)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=92:11884, fact_2=21:7282, fact_3=6:2865, prefix_sum_12=113:24754, sum=119:20728)
- Layer 20: ` Tears`, `足`, `cape`, ` smile`, `锁定` (target ranks: fact_1=92:8096, fact_2=21:2329, fact_3=6:620, prefix_sum_12=113:18921, sum=119:22804)
- Layer 30: `�`, `atan`, `幽`, ` tap`, `cape` (target ranks: fact_1=92:18692, fact_2=21:6098, fact_3=6:1150, prefix_sum_12=113:33459, sum=119:38598)
- Layer 35: `�`, `atan`, `cape`, ` repetition`, ` tap` (target ranks: fact_1=92:26247, fact_2=21:3710, fact_3=6:1352, prefix_sum_12=113:25468, sum=119:30206)
- Layer 36: `�`, `询问`, ` tap`, `atan`, `acin` (target ranks: fact_1=92:46651, fact_2=21:10368, fact_3=6:2394, prefix_sum_12=113:24773, sum=119:24894)
- Layer 37: ` Uran`, ` uranium`, `�`, ` atomic`, `atomic` (target ranks: fact_1=92:110123, fact_2=21:43603, fact_3=6:26886, prefix_sum_12=113:32444, sum=119:53273)
- Layer 38: ` Uran`, ` uranium`, `�`, `}<?`, ` atomic` (target ranks: fact_1=92:110609, fact_2=21:49820, fact_3=6:45028, prefix_sum_12=113:42517, sum=119:60985)
- Layer 39: ` Uran`, `�`, ` uranium`, `打磨`, ` Rutherford` (target ranks: fact_1=92:52161, fact_2=21:67052, fact_3=6:76170, prefix_sum_12=113:57985, sum=119:65647)
- Layer 40: `�`, `atomic`, ` atomic`, `打磨`, ` ` (target ranks: fact_1=92:14136, fact_2=21:27799, fact_3=6:19767, prefix_sum_12=113:15739, sum=119:37620)
- Layer 41: ` Uran`, ` .`, ` `, ` uranium`, ` atomic` (target ranks: fact_1=92:2363, fact_2=21:17835, fact_3=6:756, prefix_sum_12=113:4468, sum=119:16817)

### Filler position 24 (absolute token 539, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:125012, fact_2=21:125542, fact_3=6:127173, prefix_sum_12=113:120709, sum=119:122011)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=92:10751, fact_2=21:6841, fact_3=6:2447, prefix_sum_12=113:23906, sum=119:20317)
- Layer 20: ` LS`, ` smile`, `ait`, `足`, `锁定` (target ranks: fact_1=92:11094, fact_2=21:3956, fact_3=6:942, prefix_sum_12=113:23497, sum=119:24877)
- Layer 30: `拆`, `西洋`, ` picnic`, ` dy`, `Tap` (target ranks: fact_1=92:33826, fact_2=21:17786, fact_3=6:2623, prefix_sum_12=113:55441, sum=119:58552)
- Layer 35: `羊`, `重复`, ` repetition`, `Tap`, ` tap` (target ranks: fact_1=92:29598, fact_2=21:6431, fact_3=6:1417, prefix_sum_12=113:47750, sum=119:43881)
- Layer 36: `羊`, `询问`, ` riv`, ` tap`, `重复` (target ranks: fact_1=92:33838, fact_2=21:11009, fact_3=6:2206, prefix_sum_12=113:35571, sum=119:34905)
- Layer 37: ` Zad`, ` ripple`, `柚子`, ` tare`, ` riv` (target ranks: fact_1=92:87006, fact_2=21:40797, fact_3=6:11122, prefix_sum_12=113:48623, sum=119:63957)
- Layer 38: `<｜begin▁of▁sentence｜>`, `�`, `叶子`, ` fusion`, ` Zad` (target ranks: fact_1=92:110206, fact_2=21:77808, fact_3=6:28706, prefix_sum_12=113:63884, sum=119:80626)
- Layer 39: `<｜begin▁of▁sentence｜>`, `�`, `叶子`, `osit`, `繁体` (target ranks: fact_1=92:95211, fact_2=21:78974, fact_3=6:85193, prefix_sum_12=113:79716, sum=119:90219)
- Layer 40: `<｜begin▁of▁sentence｜>`, `�`, ` aure`, `eland`, ` Rutherford` (target ranks: fact_1=92:59260, fact_2=21:36556, fact_3=6:23207, prefix_sum_12=113:34799, sum=119:62598)
- Layer 41: ` .`, `装`, ` aure`, `叮`, `有下列` (target ranks: fact_1=92:43568, fact_2=21:62280, fact_3=6:3638, prefix_sum_12=113:23994, sum=119:59788)

### Filler position 25 (absolute token 540, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=92:124909, fact_2=21:125464, fact_3=6:127106, prefix_sum_12=113:120541, sum=119:121852)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12786, fact_2=21:7982, fact_3=6:3244, prefix_sum_12=113:26301, sum=119:22216)
- Layer 20: `足`, `距`, ` Walker`, ` smile`, `锁定` (target ranks: fact_1=92:12191, fact_2=21:3679, fact_3=6:1762, prefix_sum_12=113:21496, sum=119:22430)
- Layer 30: `atan`, `Subt`, ` calculator`, `obin`, `柿子` (target ranks: fact_1=92:18730, fact_2=21:3209, fact_3=6:2207, prefix_sum_12=113:27034, sum=119:19570)
- Layer 35: `obin`, `羊`, ` Wil`, ` calculator`, `atan` (target ranks: fact_1=92:6241, fact_2=21:869, fact_3=6:918, prefix_sum_12=113:14789, sum=119:9364)
- Layer 36: `留存`, `obin`, ` Wil`, `acin`, `atan` (target ranks: fact_1=92:12612, fact_2=21:6130, fact_3=6:3737, prefix_sum_12=113:13679, sum=119:8881)
- Layer 37: ` Uran`, `uran`, `}<?`, ` uranium`, ` atomic` (target ranks: fact_1=92:17, fact_2=21:22260, fact_3=6:53481, prefix_sum_12=113:3072, sum=119:1337)
- Layer 38: ` Uran`, `}<?`, ` uranium`, `uran`, `ucl` (target ranks: fact_1=92:9, fact_2=21:55573, fact_3=6:88555, prefix_sum_12=113:4778, sum=119:2737)
- Layer 39: `}<?`, ` Uran`, `92`, ` uranium`, ` ninety` (target ranks: fact_1=92:3, fact_2=21:119160, fact_3=6:99049, prefix_sum_12=113:60376, sum=119:42376)
- Layer 40: `atomic`, ` atomic`, ` cascade`, `92`, `scr` (target ranks: fact_1=92:4, fact_2=21:123013, fact_3=6:75951, prefix_sum_12=113:53332, sum=119:66854)
- Layer 41: ` atomic`, `atomic`, `原子`, `老乡`, ` cascade` (target ranks: fact_1=92:15, fact_2=21:86468, fact_3=6:7029, prefix_sum_12=113:42089, sum=119:85071)

### Filler position 26 (absolute token 541, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:125443, fact_2=21:125738, fact_3=6:127343, prefix_sum_12=113:121117, sum=119:122328)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11404, fact_2=21:7180, fact_3=6:2776, prefix_sum_12=113:24229, sum=119:20080)
- Layer 20: ` Walker`, `ait`, `Walker`, ` ES`, `忑` (target ranks: fact_1=92:14067, fact_2=21:7202, fact_3=6:2293, prefix_sum_12=113:32362, sum=119:25803)
- Layer 30: ` Invent`, `ragma`, `acos`, `Invent`, ` Reve` (target ranks: fact_1=92:69373, fact_2=21:32572, fact_3=6:44306, prefix_sum_12=113:83117, sum=119:94913)
- Layer 35: ` manganese`, ` titanium`, `�`, ` cadmium`, ` mercury` (target ranks: fact_1=92:48397, fact_2=21:8693, fact_3=6:21227, prefix_sum_12=113:101754, sum=119:92701)
- Layer 36: `�`, ` titanium`, ` manganese`, `钛`, ` mercury` (target ranks: fact_1=92:13973, fact_2=21:12665, fact_3=6:12002, prefix_sum_12=113:41512, sum=119:39072)
- Layer 37: ` titanium`, `�`, ` Titan`, ` manganese`, `钛` (target ranks: fact_1=92:30590, fact_2=21:37007, fact_3=6:45102, prefix_sum_12=113:37799, sum=119:40097)
- Layer 38: ` Titan`, ` titanium`, `�`, ` manganese`, `�` (target ranks: fact_1=92:37328, fact_2=21:46513, fact_3=6:54832, prefix_sum_12=113:31794, sum=119:34500)
- Layer 39: `�`, ` Titan`, ` titanium`, `�`, ` Nickel` (target ranks: fact_1=92:68670, fact_2=21:35959, fact_3=6:40060, prefix_sum_12=113:66385, sum=119:57729)
- Layer 40: `�`, ` Nitrogen`, ` Titan`, ` Nickel`, ` Ni` (target ranks: fact_1=92:42314, fact_2=21:17889, fact_3=6:6017, prefix_sum_12=113:34625, sum=119:21984)
- Layer 41: ` Uran`, ` uranium`, `�`, ` Bism`, ` oxygen` (target ranks: fact_1=92:5088, fact_2=21:5302, fact_3=6:302, prefix_sum_12=113:22420, sum=119:8286)

### Filler position 27 (absolute token 542, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:125971, fact_2=21:126104, fact_3=6:127585, prefix_sum_12=113:121983, sum=119:122988)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11333, fact_2=21:7231, fact_3=6:2869, prefix_sum_12=113:23723, sum=119:19451)
- Layer 20: `ait`, `锁定`, ` Walker`, `距`, `拆` (target ranks: fact_1=92:8024, fact_2=21:4395, fact_3=6:1856, prefix_sum_12=113:22438, sum=119:20441)
- Layer 30: `Walker`, ` consum`, `柿子`, ` consuming`, `akin` (target ranks: fact_1=92:650, fact_2=21:23461, fact_3=6:32700, prefix_sum_12=113:4401, sum=119:11714)
- Layer 35: `93`, `92`, `96`, `锁定`, `79` (target ranks: fact_1=92:2, fact_2=21:17373, fact_3=6:15397, prefix_sum_12=113:1015, sum=119:449)
- Layer 36: `93`, `105`, `92`, `96`, `107` (target ranks: fact_1=92:3, fact_2=21:74993, fact_3=6:60912, prefix_sum_12=113:70, sum=119:49)
- Layer 37: `}<?`, `92`, `93`, `uran`, ` dekameters` (target ranks: fact_1=92:2, fact_2=21:108963, fact_3=6:108670, prefix_sum_12=113:685, sum=119:277)
- Layer 38: `}<?`, `105`, ` dekameters`, ` hectometers`, `107` (target ranks: fact_1=92:94, fact_2=21:100310, fact_3=6:118810, prefix_sum_12=113:33, sum=119:50)
- Layer 39: `105`, `107`, `}<?`, `106`, `ophe` (target ranks: fact_1=92:91124, fact_2=21:115124, fact_3=6:101181, prefix_sum_12=113:19, sum=119:71)
- Layer 40: ` atomic`, `uran`, `atomic`, ` dekameters`, `107` (target ranks: fact_1=92:2836, fact_2=21:76662, fact_3=6:62491, prefix_sum_12=113:85, sum=119:177)
- Layer 41: ` atomic`, `吾尔`, `笔趣`, `因为这些`, `外商投资` (target ranks: fact_1=92:3243, fact_2=21:50853, fact_3=6:8207, prefix_sum_12=113:1703, sum=119:8880)

### Filler position 28 (absolute token 543, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:125849, fact_2=21:125936, fact_3=6:127506, prefix_sum_12=113:121749, sum=119:122843)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11227, fact_2=21:7058, fact_3=6:2775, prefix_sum_12=113:23446, sum=119:19149)
- Layer 20: `ait`, ` smile`, `锁定`, ` Walker`, `拆` (target ranks: fact_1=92:13175, fact_2=21:5763, fact_3=6:2382, prefix_sum_12=113:32088, sum=119:30913)
- Layer 30: ` repetition`, ` repetitions`, `锁定`, ` labor`, ` sequential` (target ranks: fact_1=92:30173, fact_2=21:23101, fact_3=6:8654, prefix_sum_12=113:47434, sum=119:56003)
- Layer 35: `锁定`, `重复`, ` repetition`, ` repeated`, `足` (target ranks: fact_1=92:36580, fact_2=21:15950, fact_3=6:6514, prefix_sum_12=113:47924, sum=119:46376)
- Layer 36: ` repeated`, `俯`, `反复`, `重复`, ` stabil` (target ranks: fact_1=92:37943, fact_2=21:24632, fact_3=6:7972, prefix_sum_12=113:40299, sum=119:30644)
- Layer 37: `}<?`, `俯`, `坏`, ` ripple`, ` capsule` (target ranks: fact_1=92:84115, fact_2=21:77293, fact_3=6:45773, prefix_sum_12=113:52242, sum=119:48378)
- Layer 38: `}<?`, `坏`, `等待着`, `俯`, ` capsule` (target ranks: fact_1=92:87009, fact_2=21:68560, fact_3=6:46599, prefix_sum_12=113:59376, sum=119:47759)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `繁体`, `坏`, ` dekameters` (target ranks: fact_1=92:101205, fact_2=21:96941, fact_3=6:93620, prefix_sum_12=113:93076, sum=119:80908)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` .`, `}<?`, `装`, ` dotted` (target ranks: fact_1=92:75579, fact_2=21:65878, fact_3=6:39076, prefix_sum_12=113:59241, sum=119:66492)
- Layer 41: ` .`, ` `, `装`, ` .↵↵`, `<｜end▁of▁sentence｜>` (target ranks: fact_1=92:26346, fact_2=21:48865, fact_3=6:2299, prefix_sum_12=113:16289, sum=119:20290)

### Filler position 29 (absolute token 544, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:125690, fact_2=21:125801, fact_3=6:127417, prefix_sum_12=113:121628, sum=119:122708)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11934, fact_2=21:7321, fact_3=6:2958, prefix_sum_12=113:24354, sum=119:19920)
- Layer 20: ` LS`, `cape`, `能被`, `锁定`, ` smile` (target ranks: fact_1=92:7757, fact_2=21:939, fact_3=6:388, prefix_sum_12=113:14924, sum=119:14493)
- Layer 30: `cape`, ` ternary`, `obin`, ` EC`, ` tear` (target ranks: fact_1=92:21650, fact_2=21:1166, fact_3=6:206, prefix_sum_12=113:18429, sum=119:29402)
- Layer 35: `6`, ` six`, ` Six`, `six`, `六` (target ranks: fact_1=92:45622, fact_2=21:17536, fact_3=6:1, prefix_sum_12=113:59765, sum=119:61449)
- Layer 36: `6`, ` six`, ` Six`, ` Sixth`, `six` (target ranks: fact_1=92:80247, fact_2=21:55256, fact_3=6:1, prefix_sum_12=113:68118, sum=119:68055)
- Layer 37: ` Sixth`, ` sixth`, ` six`, `6`, `六` (target ranks: fact_1=92:115915, fact_2=21:100164, fact_3=6:4, prefix_sum_12=113:84418, sum=119:76016)
- Layer 38: ` Sixth`, ` sixth`, `carbon`, `碳`, `uttered` (target ranks: fact_1=92:109442, fact_2=21:95094, fact_3=6:7, prefix_sum_12=113:66563, sum=119:66591)
- Layer 39: ` Sixth`, `六`, `}<?`, ` šest`, ` Six` (target ranks: fact_1=92:113198, fact_2=21:83542, fact_3=6:58, prefix_sum_12=113:33090, sum=119:36360)
- Layer 40: `atomic`, `装`, ` atomic`, ` consum`, `zat` (target ranks: fact_1=92:69386, fact_2=21:47875, fact_3=6:32, prefix_sum_12=113:2987, sum=119:4244)
- Layer 41: `装`, ` `, ` .`, ` mediabestanden`, ` atomic` (target ranks: fact_1=92:39380, fact_2=21:33637, fact_3=6:9, prefix_sum_12=113:1781, sum=119:2208)

### Filler position 30 (absolute token 545, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:125921, fact_2=21:125987, fact_3=6:127512, prefix_sum_12=113:122004, sum=119:123039)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:11099, fact_2=21:6821, fact_3=6:2538, prefix_sum_12=113:23740, sum=119:19563)
- Layer 20: ` smile`, `锁定`, `胃癌`, `atile`, ` LS` (target ranks: fact_1=92:12942, fact_2=21:5327, fact_3=6:1693, prefix_sum_12=113:29535, sum=119:29233)
- Layer 30: ` reserved`, ` kahaboga`, `忑`, `reve`, ` ES` (target ranks: fact_1=92:49644, fact_2=21:8508, fact_3=6:20598, prefix_sum_12=113:52811, sum=119:77157)
- Layer 35: `�`, `铂`, ` cadmium`, ` mercury`, `mium` (target ranks: fact_1=92:48529, fact_2=21:1529, fact_3=6:7396, prefix_sum_12=113:22299, sum=119:43030)
- Layer 36: `�`, ` Rh`, `铂`, ` mercury`, `Rh` (target ranks: fact_1=92:19430, fact_2=21:4904, fact_3=6:6163, prefix_sum_12=113:4572, sum=119:17407)
- Layer 37: `�`, `�`, ` platinum`, `�`, `铂` (target ranks: fact_1=92:48179, fact_2=21:23598, fact_3=6:37554, prefix_sum_12=113:2604, sum=119:16923)
- Layer 38: `�`, ` platinum`, `adium`, `�`, `�` (target ranks: fact_1=92:59573, fact_2=21:32586, fact_3=6:48017, prefix_sum_12=113:3490, sum=119:26718)
- Layer 39: `�`, `�`, ` Ind`, `�`, ` platinum` (target ranks: fact_1=92:69633, fact_2=21:31935, fact_3=6:58682, prefix_sum_12=113:22357, sum=119:48154)
- Layer 40: `�`, ` Ind`, ` Neon`, ` Mercury`, `�` (target ranks: fact_1=92:64278, fact_2=21:17706, fact_3=6:12909, prefix_sum_12=113:10547, sum=119:19209)
- Layer 41: ` .`, ` Bism`, ` `, `�`, `�` (target ranks: fact_1=92:14066, fact_2=21:5064, fact_3=6:226, prefix_sum_12=113:9841, sum=119:12990)

### Filler position 31 (absolute token 546, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:126052, fact_2=21:126111, fact_3=6:127581, prefix_sum_12=113:122433, sum=119:123387)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:10801, fact_2=21:6662, fact_3=6:2286, prefix_sum_12=113:23494, sum=119:19526)
- Layer 20: `锁定`, ` smile`, `甸`, `足`, ` LS` (target ranks: fact_1=92:5557, fact_2=21:2592, fact_3=6:602, prefix_sum_12=113:16093, sum=119:16742)
- Layer 30: `回答`, ` answer`, `鞍`, ` answers`, ` Answer` (target ranks: fact_1=92:27714, fact_2=21:13974, fact_3=6:3301, prefix_sum_12=113:23148, sum=119:32191)
- Layer 35: `锁定`, ` tap`, `鞍`, ` repetition`, `重复` (target ranks: fact_1=92:30156, fact_2=21:8591, fact_3=6:5061, prefix_sum_12=113:20838, sum=119:28633)
- Layer 36: ` tap`, `鞍`, ` Tap`, `Tap`, `锁定` (target ranks: fact_1=92:34365, fact_2=21:13106, fact_3=6:5668, prefix_sum_12=113:18611, sum=119:21155)
- Layer 37: `坏`, `冰冰`, ` tap`, `asking`, `陪伴` (target ranks: fact_1=92:77523, fact_2=21:40037, fact_3=6:35144, prefix_sum_12=113:16500, sum=119:30697)
- Layer 38: `坏`, `冰冰`, `叮`, `asking`, `}<?` (target ranks: fact_1=92:89840, fact_2=21:37301, fact_3=6:40119, prefix_sum_12=113:16953, sum=119:27748)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `铎`, `下沉`, `坏` (target ranks: fact_1=92:85333, fact_2=21:85676, fact_3=6:94617, prefix_sum_12=113:51009, sum=119:57234)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` .`, `铎`, `透过`, `装` (target ranks: fact_1=92:49018, fact_2=21:69363, fact_3=6:41777, prefix_sum_12=113:24430, sum=119:41230)
- Layer 41: ` .`, `叮`, ` just`, ` wherever`, ` dotted` (target ranks: fact_1=92:31612, fact_2=21:57468, fact_3=6:5872, prefix_sum_12=113:8104, sum=119:27158)

### Filler position 32 (absolute token 547, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `ivables` (target ranks: fact_1=92:125992, fact_2=21:126073, fact_3=6:127547, prefix_sum_12=113:122406, sum=119:123316)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:9838, fact_2=21:6531, fact_3=6:2210, prefix_sum_12=113:22327, sum=119:18378)
- Layer 20: `锁定`, `足`, `ait`, ` smile`, `甸` (target ranks: fact_1=92:7400, fact_2=21:3367, fact_3=6:1246, prefix_sum_12=113:18124, sum=119:16396)
- Layer 30: `Tap`, ` tap`, `tap`, ` remembering`, `锁定` (target ranks: fact_1=92:14656, fact_2=21:7578, fact_3=6:2600, prefix_sum_12=113:43224, sum=119:29954)
- Layer 35: `足`, `锁定`, ` tap`, ` labor`, `Tap` (target ranks: fact_1=92:20139, fact_2=21:3423, fact_3=6:1879, prefix_sum_12=113:33909, sum=119:34887)
- Layer 36: `留存`, ` tap`, ` stabil`, `Tap`, `熟悉` (target ranks: fact_1=92:26288, fact_2=21:7613, fact_3=6:2242, prefix_sum_12=113:29474, sum=119:29324)
- Layer 37: `漏`, `留存`, `坏`, `acet`, `翻` (target ranks: fact_1=92:65027, fact_2=21:30738, fact_3=6:22561, prefix_sum_12=113:30312, sum=119:42306)
- Layer 38: `}<?`, `累`, `acet`, `坏`, `留存` (target ranks: fact_1=92:56166, fact_2=21:38881, fact_3=6:34285, prefix_sum_12=113:30682, sum=119:46093)
- Layer 39: `<｜begin▁of▁sentence｜>`, `累`, ` Rutherford`, `osit`, `}<?` (target ranks: fact_1=92:45129, fact_2=21:73525, fact_3=6:75955, prefix_sum_12=113:54004, sum=119:69256)
- Layer 40: `<｜begin▁of▁sentence｜>`, `留存`, `atomic`, `scr`, ` Rutherford` (target ranks: fact_1=92:2035, fact_2=21:38344, fact_3=6:17510, prefix_sum_12=113:11487, sum=119:34974)
- Layer 41: ` .`, ` atomic`, ` dotted`, `atomic`, ` ` (target ranks: fact_1=92:2722, fact_2=21:41136, fact_3=6:918, prefix_sum_12=113:6839, sum=119:32706)

### Filler position 33 (absolute token 548, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126466, fact_2=21:126400, fact_3=6:127831, prefix_sum_12=113:123264, sum=119:124017)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:10250, fact_2=21:6853, fact_3=6:2499, prefix_sum_12=113:22736, sum=119:18741)
- Layer 20: ` LS`, `ait`, ` Walker`, `足`, `锁定` (target ranks: fact_1=92:6172, fact_2=21:1405, fact_3=6:358, prefix_sum_12=113:16425, sum=119:14622)
- Layer 30: `柿子`, `scan`, `acos`, `acin`, ` Heim` (target ranks: fact_1=92:38605, fact_2=21:2926, fact_3=6:7239, prefix_sum_12=113:17717, sum=119:22945)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=92:112740, fact_2=21:1, fact_3=6:88893, prefix_sum_12=113:68501, sum=119:55045)
- Layer 36: `二十一`, `21`, ` XXI`, ` Twenty`, ` twenty` (target ranks: fact_1=92:119962, fact_2=21:2, fact_3=6:119135, prefix_sum_12=113:116159, sum=119:108777)
- Layer 37: `二十一`, `21`, ` XXI`, `twenty`, ` Twenty` (target ranks: fact_1=92:95811, fact_2=21:2, fact_3=6:124635, prefix_sum_12=113:115067, sum=119:107100)
- Layer 38: `二十一`, `21`, ` XXI`, `<｜begin▁of▁file｜>`, `acons` (target ranks: fact_1=92:88347, fact_2=21:2, fact_3=6:125982, prefix_sum_12=113:69966, sum=119:84703)
- Layer 39: `二十一`, `orten`, ` Gai`, `}<?`, ` tran` (target ranks: fact_1=92:50548, fact_2=21:14, fact_3=6:23564, prefix_sum_12=113:41245, sum=119:62407)
- Layer 40: `anium`, `}<?`, `atomic`, ` catch`, `uran` (target ranks: fact_1=92:381, fact_2=21:154, fact_3=6:723, prefix_sum_12=113:6069, sum=119:6590)
- Layer 41: ` atomic`, `atomic`, `冶`, ` uranium`, `有的时候` (target ranks: fact_1=92:995, fact_2=21:538, fact_3=6:87, prefix_sum_12=113:16940, sum=119:39349)

### Filler position 34 (absolute token 549, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126776, fact_2=21:126606, fact_3=6:127936, prefix_sum_12=113:123698, sum=119:124371)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:10519, fact_2=21:6931, fact_3=6:2529, prefix_sum_12=113:23396, sum=119:19178)
- Layer 20: `ait`, `锁定`, `足`, ` Walker`, `胃癌` (target ranks: fact_1=92:9688, fact_2=21:2813, fact_3=6:1072, prefix_sum_12=113:25241, sum=119:18860)
- Layer 30: `atan`, `acin`, `�`, `acic`, `分解` (target ranks: fact_1=92:35764, fact_2=21:13658, fact_3=6:8048, prefix_sum_12=113:59166, sum=119:57093)
- Layer 35: `分解`, ` repetition`, ` reserved`, `acic`, `锁定` (target ranks: fact_1=92:26767, fact_2=21:8777, fact_3=6:2801, prefix_sum_12=113:43976, sum=119:35137)
- Layer 36: `留存`, `分解`, ` stabil`, `羊`, `acin` (target ranks: fact_1=92:39124, fact_2=21:23347, fact_3=6:5520, prefix_sum_12=113:39575, sum=119:27957)
- Layer 37: ` atomic`, `atomic`, ` Atomic`, `acos`, `anium` (target ranks: fact_1=92:95488, fact_2=21:71096, fact_3=6:40858, prefix_sum_12=113:48930, sum=119:49380)
- Layer 38: ` atomic`, `atomic`, ` Atomic`, ` Uran`, `�` (target ranks: fact_1=92:90677, fact_2=21:69121, fact_3=6:53608, prefix_sum_12=113:44988, sum=119:41654)
- Layer 39: `atomic`, ` atomic`, ` Atomic`, ` Uran`, `�` (target ranks: fact_1=92:49807, fact_2=21:65753, fact_3=6:74714, prefix_sum_12=113:40069, sum=119:49689)
- Layer 40: `atomic`, ` atomic`, ` Rutherford`, `留存`, `�` (target ranks: fact_1=92:13658, fact_2=21:35246, fact_3=6:27629, prefix_sum_12=113:9508, sum=119:26895)
- Layer 41: `atomic`, ` atomic`, ` Atomic`, ` .`, ` Uran` (target ranks: fact_1=92:5183, fact_2=21:16898, fact_3=6:820, prefix_sum_12=113:6360, sum=119:18025)

### Filler position 35 (absolute token 550, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126873, fact_2=21:126698, fact_3=6:128016, prefix_sum_12=113:123795, sum=119:124429)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12319, fact_2=21:7759, fact_3=6:3207, prefix_sum_12=113:25722, sum=119:20813)
- Layer 20: ` smile`, `ait`, `胃癌`, `足`, `距` (target ranks: fact_1=92:9914, fact_2=21:2025, fact_3=6:852, prefix_sum_12=113:23965, sum=119:21591)
- Layer 30: ` tap`, `acin`, `�`, `tap`, ` repetitions` (target ranks: fact_1=92:57814, fact_2=21:34794, fact_3=6:17380, prefix_sum_12=113:47760, sum=119:33214)
- Layer 35: `重复`, `锁定`, `粥`, ` tap`, ` repetition` (target ranks: fact_1=92:51895, fact_2=21:23841, fact_3=6:13486, prefix_sum_12=113:58595, sum=119:34392)
- Layer 36: `粥`, `重复`, `反复`, ` stabil`, ` tap` (target ranks: fact_1=92:45564, fact_2=21:30617, fact_3=6:13660, prefix_sum_12=113:48958, sum=119:22181)
- Layer 37: `}<?`, `坏`, `用了`, `acet`, ` compounding` (target ranks: fact_1=92:106557, fact_2=21:89479, fact_3=6:78471, prefix_sum_12=113:66239, sum=119:35846)
- Layer 38: `}<?`, `坏`, `陪`, `pac`, ` nasod` (target ranks: fact_1=92:104132, fact_2=21:87495, fact_3=6:83461, prefix_sum_12=113:67640, sum=119:35762)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `坏`, ` nasod`, `ِّف` (target ranks: fact_1=92:111402, fact_2=21:88875, fact_3=6:109527, prefix_sum_12=113:92163, sum=119:80206)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` nasod`, `坏`, ` wait` (target ranks: fact_1=92:90404, fact_2=21:51174, fact_3=6:63729, prefix_sum_12=113:53518, sum=119:68107)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, `.,`, ` .↵↵` (target ranks: fact_1=92:32704, fact_2=21:28962, fact_3=6:4264, prefix_sum_12=113:9171, sum=119:30659)

### Filler position 36 (absolute token 551, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126840, fact_2=21:126783, fact_3=6:128082, prefix_sum_12=113:123808, sum=119:124454)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:13183, fact_2=21:8215, fact_3=6:3587, prefix_sum_12=113:27670, sum=119:22309)
- Layer 20: ` smile`, `足`, `ait`, `距`, `cape` (target ranks: fact_1=92:13205, fact_2=21:2106, fact_3=6:983, prefix_sum_12=113:34026, sum=119:27926)
- Layer 30: ` filler`, ` repetition`, ` repetitions`, `fill`, `重复` (target ranks: fact_1=92:68212, fact_2=21:13872, fact_3=6:5356, prefix_sum_12=113:57258, sum=119:69344)
- Layer 35: ` filler`, ` repetition`, `重复`, ` repetitions`, ` repeating` (target ranks: fact_1=92:43476, fact_2=21:7917, fact_3=6:3888, prefix_sum_12=113:46270, sum=119:42455)
- Layer 36: ` filler`, ` repetition`, `重复`, `填料`, ` fill` (target ranks: fact_1=92:66283, fact_2=21:30130, fact_3=6:18674, prefix_sum_12=113:58474, sum=119:43612)
- Layer 37: ` filler`, `}<?`, `填料`, ` fill`, `填充` (target ranks: fact_1=92:107295, fact_2=21:77869, fact_3=6:79296, prefix_sum_12=113:76793, sum=119:60715)
- Layer 38: ` filler`, `}<?`, `zat`, `坏`, `pac` (target ranks: fact_1=92:103806, fact_2=21:80943, fact_3=6:78148, prefix_sum_12=113:68427, sum=119:59096)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `下沉`, `坏`, `pac` (target ranks: fact_1=92:104712, fact_2=21:89210, fact_3=6:107536, prefix_sum_12=113:84726, sum=119:75656)
- Layer 40: `<｜begin▁of▁sentence｜>`, `}<?`, `下沉`, `坏`, ` structured` (target ranks: fact_1=92:66124, fact_2=21:52825, fact_3=6:56966, prefix_sum_12=113:39945, sum=119:47791)
- Layer 41: ` .`, ` until`, ` dotted`, ` because`, `坏` (target ranks: fact_1=92:36457, fact_2=21:61825, fact_3=6:11041, prefix_sum_12=113:27451, sum=119:51964)

### Filler position 37 (absolute token 552, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126822, fact_2=21:126571, fact_3=6:127925, prefix_sum_12=113:123719, sum=119:124383)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:13194, fact_2=21:8050, fact_3=6:3347, prefix_sum_12=113:27737, sum=119:22851)
- Layer 20: ` engaging`, `能被`, `忑`, `ait`, `距` (target ranks: fact_1=92:18817, fact_2=21:4154, fact_3=6:3594, prefix_sum_12=113:37275, sum=119:30441)
- Layer 30: `sac`, `eder`, `cape`, `cury`, `code` (target ranks: fact_1=92:5209, fact_2=21:2089, fact_3=6:8117, prefix_sum_12=113:46119, sum=119:42529)
- Layer 35: `92`, ` uranium`, ` Uran`, `uran`, `93` (target ranks: fact_1=92:1, fact_2=21:13243, fact_3=6:9688, prefix_sum_12=113:11150, sum=119:1238)
- Layer 36: `92`, `93`, ` ninety`, `922`, `092` (target ranks: fact_1=92:1, fact_2=21:74660, fact_3=6:75251, prefix_sum_12=113:28496, sum=119:6435)
- Layer 37: `92`, ` ninety`, `922`, `}<?`, `93` (target ranks: fact_1=92:1, fact_2=21:123094, fact_3=6:125754, prefix_sum_12=113:58736, sum=119:16996)
- Layer 38: `92`, ` uranium`, ` ninety`, `}<?`, ` Uran` (target ranks: fact_1=92:1, fact_2=21:124768, fact_3=6:124500, prefix_sum_12=113:71133, sum=119:21585)
- Layer 39: `92`, `}<?`, ` uranium`, `桃子`, ` dekameters` (target ranks: fact_1=92:1, fact_2=21:81054, fact_3=6:112593, prefix_sum_12=113:69479, sum=119:20647)
- Layer 40: `atomic`, `}<?`, ` atomic`, `uir`, ` ` (target ranks: fact_1=92:24005, fact_2=21:39606, fact_3=6:67616, prefix_sum_12=113:16219, sum=119:8065)
- Layer 41: `atomic`, ` atomic`, `................................................`, ` aggregate`, `袄` (target ranks: fact_1=92:43816, fact_2=21:39123, fact_3=6:13043, prefix_sum_12=113:35827, sum=119:37331)

### Filler position 38 (absolute token 553, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126758, fact_2=21:126439, fact_3=6:127826, prefix_sum_12=113:123841, sum=119:124525)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12373, fact_2=21:7539, fact_3=6:2925, prefix_sum_12=113:26678, sum=119:21891)
- Layer 20: `ait`, `忑`, `能被`, ` ES`, ` engaging` (target ranks: fact_1=92:19553, fact_2=21:9097, fact_3=6:4569, prefix_sum_12=113:45276, sum=119:40766)
- Layer 30: ` gold`, ` Gold`, `Gold`, `gold`, `黄金` (target ranks: fact_1=92:15501, fact_2=21:4352, fact_3=6:14490, prefix_sum_12=113:20200, sum=119:48924)
- Layer 35: ` gold`, ` prot`, ` Gold`, `Gold`, `gold` (target ranks: fact_1=92:10637, fact_2=21:1616, fact_3=6:5846, prefix_sum_12=113:16282, sum=119:30064)
- Layer 36: ` gold`, ` prot`, `gold`, ` Gold`, ` Ne` (target ranks: fact_1=92:10682, fact_2=21:2473, fact_3=6:8549, prefix_sum_12=113:7065, sum=119:12936)
- Layer 37: ` gold`, `gold`, ` Gold`, ` prot`, `Gold` (target ranks: fact_1=92:23175, fact_2=21:7119, fact_3=6:39436, prefix_sum_12=113:6468, sum=119:15633)
- Layer 38: ` gold`, `gold`, ` Gold`, `Gold`, `黄金` (target ranks: fact_1=92:37727, fact_2=21:12997, fact_3=6:61797, prefix_sum_12=113:8692, sum=119:20156)
- Layer 39: `gold`, ` gold`, ` Gold`, `Gold`, ` Prot` (target ranks: fact_1=92:26654, fact_2=21:48402, fact_3=6:85503, prefix_sum_12=113:19064, sum=119:46013)
- Layer 40: ` helium`, `�`, `argon`, ` Uran`, `atomic` (target ranks: fact_1=92:17196, fact_2=21:24874, fact_3=6:34096, prefix_sum_12=113:6668, sum=119:29789)
- Layer 41: ` helium`, ` atomic`, `atomic`, ` oxygen`, ` chromium` (target ranks: fact_1=92:6203, fact_2=21:11335, fact_3=6:3582, prefix_sum_12=113:6394, sum=119:27389)

### Filler position 39 (absolute token 554, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126993, fact_2=21:126731, fact_3=6:128081, prefix_sum_12=113:124048, sum=119:124593)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12520, fact_2=21:8050, fact_3=6:3292, prefix_sum_12=113:26852, sum=119:21982)
- Layer 20: `ait`, ` engaging`, `锁定`, `能被`, ` Engaging` (target ranks: fact_1=92:18672, fact_2=21:8021, fact_3=6:7128, prefix_sum_12=113:45329, sum=119:43616)
- Layer 30: `acin`, `subt`, `Subt`, `acos`, `obin` (target ranks: fact_1=92:19184, fact_2=21:7494, fact_3=6:21858, prefix_sum_12=113:57495, sum=119:72538)
- Layer 35: `obin`, `锁定`, `acin`, ` tap`, `eder` (target ranks: fact_1=92:4611, fact_2=21:1398, fact_3=6:6884, prefix_sum_12=113:14014, sum=119:23205)
- Layer 36: `acin`, `obin`, `留存`, `eder`, `退出` (target ranks: fact_1=92:2705, fact_2=21:3365, fact_3=6:12250, prefix_sum_12=113:5913, sum=119:8898)
- Layer 37: `}<?`, `?datasetId`, `iator`, `zat`, `打包` (target ranks: fact_1=92:232, fact_2=21:13989, fact_3=6:69092, prefix_sum_12=113:7319, sum=119:8257)
- Layer 38: `}<?`, `zat`, `?datasetId`, `打包`, `acet` (target ranks: fact_1=92:571, fact_2=21:23920, fact_3=6:71725, prefix_sum_12=113:6976, sum=119:11331)
- Layer 39: `}<?`, `zat`, `tanle`, `<｜place▁holder▁no▁703｜>`, `覆` (target ranks: fact_1=92:72616, fact_2=21:31652, fact_3=6:32736, prefix_sum_12=113:4203, sum=119:3873)
- Layer 40: `}<?`, `留存`, `等待着`, ` `, `cha` (target ranks: fact_1=92:22626, fact_2=21:10355, fact_3=6:3985, prefix_sum_12=113:2617, sum=119:3175)
- Layer 41: ` .`, `等待着`, ` `, `装`, `.,` (target ranks: fact_1=92:23075, fact_2=21:7728, fact_3=6:634, prefix_sum_12=113:3913, sum=119:8769)

### Filler position 40 (absolute token 555, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126759, fact_2=21:126459, fact_3=6:127886, prefix_sum_12=113:123654, sum=119:124290)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12297, fact_2=21:7910, fact_3=6:3228, prefix_sum_12=113:26517, sum=119:21758)
- Layer 20: `锁定`, `ait`, `鞍`, ` ES`, ` engaging` (target ranks: fact_1=92:12179, fact_2=21:4992, fact_3=6:2435, prefix_sum_12=113:30125, sum=119:27128)
- Layer 30: `退出`, `acos`, `冰冰`, `俯`, `冰川` (target ranks: fact_1=92:62383, fact_2=21:25246, fact_3=6:41510, prefix_sum_12=113:82303, sum=119:118203)
- Layer 35: `退出`, ` Rational`, ` rational`, `冰冰`, ` vertical` (target ranks: fact_1=92:30727, fact_2=21:4766, fact_3=6:24100, prefix_sum_12=113:30037, sum=119:72356)
- Layer 36: `退出`, `打包`, `提示`, `冰冰`, `atch` (target ranks: fact_1=92:15461, fact_2=21:2966, fact_3=6:15558, prefix_sum_12=113:15479, sum=119:51647)
- Layer 37: `}<?`, `打包`, `冰冰`, `oug`, `在北京` (target ranks: fact_1=92:40080, fact_2=21:18029, fact_3=6:64906, prefix_sum_12=113:17957, sum=119:59606)
- Layer 38: `}<?`, `打包`, `打磨`, `osit`, `<｜begin▁of▁sentence｜>` (target ranks: fact_1=92:70789, fact_2=21:25813, fact_3=6:72424, prefix_sum_12=113:29661, sum=119:66734)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `erer`, `osit`, `ozygous` (target ranks: fact_1=92:75577, fact_2=21:94228, fact_3=6:106624, prefix_sum_12=113:53172, sum=119:70122)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` Answer`, `}<?`, `留存`, ` پاسخ` (target ranks: fact_1=92:17677, fact_2=21:54090, fact_3=6:47583, prefix_sum_12=113:9410, sum=119:15901)
- Layer 41: `Answer`, ` .`, ` Answer`, ` answer`, ` ` (target ranks: fact_1=92:7901, fact_2=21:26270, fact_3=6:4882, prefix_sum_12=113:7141, sum=119:12246)

### Filler position 41 (absolute token 556, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126492, fact_2=21:126259, fact_3=6:127740, prefix_sum_12=113:123357, sum=119:124004)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12966, fact_2=21:8115, fact_3=6:3280, prefix_sum_12=113:27275, sum=119:22271)
- Layer 20: `锁定`, ` smile`, `ait`, `cape`, `ession` (target ranks: fact_1=92:9957, fact_2=21:2501, fact_3=6:1044, prefix_sum_12=113:23009, sum=119:19331)
- Layer 30: `柿子`, `陪`, `Wait`, ` wait`, `Difficulty` (target ranks: fact_1=92:67595, fact_2=21:3535, fact_3=6:15747, prefix_sum_12=113:38703, sum=119:44182)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=92:124535, fact_2=21:1, fact_3=6:95598, prefix_sum_12=113:93568, sum=119:79339)
- Layer 36: `21`, `二十一`, ` XXI`, ` Twenty`, ` twenty` (target ranks: fact_1=92:125287, fact_2=21:1, fact_3=6:112805, prefix_sum_12=113:117089, sum=119:100914)
- Layer 37: `21`, `二十一`, ` XXI`, `}<?`, ` Twenty` (target ranks: fact_1=92:126989, fact_2=21:1, fact_3=6:123335, prefix_sum_12=113:113214, sum=119:107122)
- Layer 38: `21`, `二十一`, ` XXI`, `}<?`, `زياح` (target ranks: fact_1=92:127189, fact_2=21:1, fact_3=6:122184, prefix_sum_12=113:83433, sum=119:79402)
- Layer 39: ` šest`, `lier`, `zat`, `�`, ` Nij` (target ranks: fact_1=92:106023, fact_2=21:75, fact_3=6:3802, prefix_sum_12=113:77660, sum=119:80335)
- Layer 40: ` six`, `anium`, ` šest`, ` Six`, `六` (target ranks: fact_1=92:19156, fact_2=21:1295, fact_3=6:15, prefix_sum_12=113:13910, sum=119:10218)
- Layer 41: ` compounded`, `atomic`, `因为这些`, ` waiting`, ` mediabestanden` (target ranks: fact_1=92:12750, fact_2=21:6848, fact_3=6:12, prefix_sum_12=113:18039, sum=119:29388)

### Filler position 42 (absolute token 557, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126958, fact_2=21:126704, fact_3=6:128056, prefix_sum_12=113:124255, sum=119:124743)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:13406, fact_2=21:8081, fact_3=6:3267, prefix_sum_12=113:27768, sum=119:22861)
- Layer 20: ` smile`, `锁定`, `cape`, `ession`, `甸` (target ranks: fact_1=92:12540, fact_2=21:2907, fact_3=6:1599, prefix_sum_12=113:22528, sum=119:22986)
- Layer 30: `柿子`, `atan`, `鞍`, ` thoracic`, `保留` (target ranks: fact_1=92:62409, fact_2=21:2763, fact_3=6:7547, prefix_sum_12=113:25468, sum=119:55018)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=92:113394, fact_2=21:1, fact_3=6:49484, prefix_sum_12=113:84122, sum=119:83227)
- Layer 36: `21`, `二十一`, ` XXI`, ` Twenty`, ` twenty` (target ranks: fact_1=92:126271, fact_2=21:1, fact_3=6:99285, prefix_sum_12=113:114030, sum=119:102135)
- Layer 37: `二十一`, `21`, `}<?`, ` XXI`, `cault` (target ranks: fact_1=92:128502, fact_2=21:2, fact_3=6:123894, prefix_sum_12=113:113001, sum=119:111508)
- Layer 38: `}<?`, `二十一`, `21`, `cault`, `erget` (target ranks: fact_1=92:128659, fact_2=21:3, fact_3=6:124987, prefix_sum_12=113:95967, sum=119:100893)
- Layer 39: `�`, `}<?`, ` Nij`, `ophyll`, `-ulo` (target ranks: fact_1=92:124303, fact_2=21:217, fact_3=6:47888, prefix_sum_12=113:104086, sum=119:107366)
- Layer 40: `anium`, `�`, `ophyll`, `�`, ` twenty` (target ranks: fact_1=92:77036, fact_2=21:986, fact_3=6:852, prefix_sum_12=113:34134, sum=119:32198)
- Layer 41: ` .`, ` because`, ` `, ` twenty`, ` six` (target ranks: fact_1=92:33741, fact_2=21:876, fact_3=6:10, prefix_sum_12=113:16223, sum=119:20532)

### Filler position 43 (absolute token 558, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126632, fact_2=21:126451, fact_3=6:127881, prefix_sum_12=113:123452, sum=119:124141)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:13036, fact_2=21:7830, fact_3=6:3060, prefix_sum_12=113:27855, sum=119:23381)
- Layer 20: `cape`, `LS`, ` LS`, `锁定`, ` smile` (target ranks: fact_1=92:6886, fact_2=21:2064, fact_3=6:636, prefix_sum_12=113:19462, sum=119:17033)
- Layer 30: ` ternary`, `总体`, `柿子`, `打完`, ` mun` (target ranks: fact_1=92:85444, fact_2=21:4083, fact_3=6:14126, prefix_sum_12=113:48066, sum=119:55092)
- Layer 35: ` ternary`, `19`, ` SK`, `ilig`, `/hess` (target ranks: fact_1=92:51599, fact_2=21:376, fact_3=6:12612, prefix_sum_12=113:27306, sum=119:25323)
- Layer 36: ` ninete`, `radesh`, ` nineteen`, `十九`, `19` (target ranks: fact_1=92:81255, fact_2=21:223, fact_3=6:94874, prefix_sum_12=113:10916, sum=119:10426)
- Layer 37: `}<?`, ` ninete`, `radesh`, `?datasetId`, ` Nij` (target ranks: fact_1=92:4330, fact_2=21:6877, fact_3=6:116635, prefix_sum_12=113:4411, sum=119:1788)
- Layer 38: `}<?`, `院内`, ` ninete`, `劳`, `大王` (target ranks: fact_1=92:6000, fact_2=21:22243, fact_3=6:116847, prefix_sum_12=113:4461, sum=119:1598)
- Layer 39: `107`, `}<?`, `109`, `tanle`, `-ulo` (target ranks: fact_1=92:57268, fact_2=21:17114, fact_3=6:3321, prefix_sum_12=113:63, sum=119:203)
- Layer 40: ` ons`, `107`, `<｜place▁holder▁no▁697｜>`, `109`, `}<?` (target ranks: fact_1=92:6665, fact_2=21:6579, fact_3=6:144, prefix_sum_12=113:41, sum=119:190)
- Layer 41: `我曾经`, ` množine`, `因为这些`, ` .`, `上文` (target ranks: fact_1=92:20012, fact_2=21:5788, fact_3=6:192, prefix_sum_12=113:1711, sum=119:8015)

### Filler position 44 (absolute token 559, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126622, fact_2=21:126379, fact_3=6:127851, prefix_sum_12=113:123416, sum=119:124146)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12737, fact_2=21:7884, fact_3=6:3077, prefix_sum_12=113:27366, sum=119:23136)
- Layer 20: `能被`, `锁定`, ` ES`, `LS`, `ait` (target ranks: fact_1=92:9619, fact_2=21:3494, fact_3=6:1150, prefix_sum_12=113:23094, sum=119:17772)
- Layer 30: ` SK`, `acet`, `acos`, `Om`, ` Pop` (target ranks: fact_1=92:36725, fact_2=21:3443, fact_3=6:26794, prefix_sum_12=113:31806, sum=119:38477)
- Layer 35: `49`, ` SK`, `79`, ` ST`, `59` (target ranks: fact_1=92:18680, fact_2=21:475, fact_3=6:11941, prefix_sum_12=113:17164, sum=119:6092)
- Layer 36: `43`, `}<?`, `49`, `37`, `39` (target ranks: fact_1=92:11496, fact_2=21:5127, fact_3=6:71381, prefix_sum_12=113:382, sum=119:357)
- Layer 37: `}<?`, `107`, ` dekameters`, `?datasetId`, `祭` (target ranks: fact_1=92:582, fact_2=21:59990, fact_3=6:99221, prefix_sum_12=113:39, sum=119:36)
- Layer 38: `}<?`, `107`, ` fles`, `109`, ` Latitude` (target ranks: fact_1=92:639, fact_2=21:111635, fact_3=6:85192, prefix_sum_12=113:38, sum=119:21)
- Layer 39: `107`, `109`, `103`, `106`, `105` (target ranks: fact_1=92:86759, fact_2=21:119879, fact_3=6:23518, prefix_sum_12=113:6, sum=119:9)
- Layer 40: `107`, `}<?`, `109`, `103`, `106` (target ranks: fact_1=92:8051, fact_2=21:113874, fact_3=6:6978, prefix_sum_12=113:6, sum=119:9)
- Layer 41: `上文`, `我曾经`, `出不穷`, ` .`, `癫�` (target ranks: fact_1=92:16787, fact_2=21:77806, fact_3=6:781, prefix_sum_12=113:71, sum=119:281)

### Filler position 45 (absolute token 560, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126633, fact_2=21:126320, fact_3=6:127757, prefix_sum_12=113:123706, sum=119:124413)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=92:12693, fact_2=21:8549, fact_3=6:3392, prefix_sum_12=113:26994, sum=119:22807)
- Layer 20: `ait`, `锁定`, ` ES`, ` Walker`, `会成为` (target ranks: fact_1=92:20041, fact_2=21:8378, fact_3=6:5187, prefix_sum_12=113:34882, sum=119:31598)
- Layer 30: `acet`, `acos`, `acin`, `仰`, `otos` (target ranks: fact_1=92:45164, fact_2=21:47697, fact_3=6:99105, prefix_sum_12=113:44160, sum=119:75445)
- Layer 35: `otas`, ` dekameters`, `acic`, `acin`, ` Kaw` (target ranks: fact_1=92:2674, fact_2=21:33806, fact_3=6:63159, prefix_sum_12=113:14440, sum=119:17504)
- Layer 36: `otas`, ` dekameters`, `anin`, `凑`, `acet` (target ranks: fact_1=92:1436, fact_2=21:76404, fact_3=6:87860, prefix_sum_12=113:2979, sum=119:6317)
- Layer 37: `}<?`, `?datasetId`, ` dekameters`, `Quintal`, `acet` (target ranks: fact_1=92:1590, fact_2=21:111661, fact_3=6:113448, prefix_sum_12=113:6341, sum=119:9300)
- Layer 38: `}<?`, `oye`, ` dekameters`, `院内`, `打包` (target ranks: fact_1=92:1493, fact_2=21:87431, fact_3=6:108515, prefix_sum_12=113:2015, sum=119:4882)
- Layer 39: `}<?`, `<｜place▁holder▁no▁703｜>`, `opters`, `经纬`, ` Latitude` (target ranks: fact_1=92:104085, fact_2=21:72166, fact_3=6:72389, prefix_sum_12=113:180, sum=119:456)
- Layer 40: `103`, `等待着`, `105`, `106`, `}<?` (target ranks: fact_1=92:35654, fact_2=21:26364, fact_3=6:12530, prefix_sum_12=113:40, sum=119:140)
- Layer 41: ` .`, ` `, `.,`, `因为这些`, `))))` (target ranks: fact_1=92:22838, fact_2=21:10346, fact_3=6:947, prefix_sum_12=113:149, sum=119:513)

### Filler position 46 (absolute token 561, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126478, fact_2=21:126240, fact_3=6:127710, prefix_sum_12=113:123305, sum=119:124076)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=92:11710, fact_2=21:8071, fact_3=6:3042, prefix_sum_12=113:25720, sum=119:21206)
- Layer 20: ` blanks`, ` Blank`, `空白`, ` blank`, ` spac` (target ranks: fact_1=92:111603, fact_2=21:15366, fact_3=6:55253, prefix_sum_12=113:102135, sum=119:104148)
- Layer 30: ` spac`, `}using`, `?datasetId`, `坝`, ` spacer` (target ranks: fact_1=92:124260, fact_2=21:91691, fact_3=6:115110, prefix_sum_12=113:121758, sum=119:123882)
- Layer 35: `}using`, `足足`, `绵绵`, `放下`, `ovel` (target ranks: fact_1=92:112309, fact_2=21:62838, fact_3=6:105588, prefix_sum_12=113:117321, sum=119:110753)
- Layer 36: `足足`, `俯`, `放下`, `ovel`, `ancock` (target ranks: fact_1=92:63932, fact_2=21:18718, fact_3=6:45443, prefix_sum_12=113:79128, sum=119:67921)
- Layer 37: `}<?`, `放下`, `放下了`, `足足`, ` doubling` (target ranks: fact_1=92:108571, fact_2=21:58955, fact_3=6:95501, prefix_sum_12=113:90313, sum=119:90595)
- Layer 38: ` .`, `足足`, ` Mercury`, ` .↵↵`, `陪` (target ranks: fact_1=92:82785, fact_2=21:25136, fact_3=6:60394, prefix_sum_12=113:88900, sum=119:77760)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` Mercury`, `陪`, `铎` (target ranks: fact_1=92:75836, fact_2=21:39533, fact_3=6:81595, prefix_sum_12=113:82458, sum=119:95741)
- Layer 40: ` .`, ` Mercury`, ` .↵↵`, `<｜begin▁of▁sentence｜>`, `�` (target ranks: fact_1=92:47924, fact_2=21:16174, fact_3=6:35974, prefix_sum_12=113:47689, sum=119:69389)
- Layer 41: ` .`, ` .↵↵`, ` Mercury`, `<｜end▁of▁sentence｜>`, ` .↵` (target ranks: fact_1=92:16588, fact_2=21:4932, fact_3=6:3644, prefix_sum_12=113:26932, sum=119:32970)

### Filler position 47 (absolute token 562, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126795, fact_2=21:126490, fact_3=6:127943, prefix_sum_12=113:123818, sum=119:124370)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=92:11552, fact_2=21:7782, fact_3=6:2992, prefix_sum_12=113:25606, sum=119:20939)
- Layer 20: `}<?`, ` partly`, `Partly`, `ozygous`, ` honoured` (target ranks: fact_1=92:120583, fact_2=21:21815, fact_3=6:71664, prefix_sum_12=113:109230, sum=119:103499)
- Layer 30: `}<?`, `codeline`, `}using`, `东京`, ` spac` (target ranks: fact_1=92:120604, fact_2=21:79597, fact_3=6:95760, prefix_sum_12=113:114737, sum=119:116066)
- Layer 35: `切割`, `}using`, `ِّف`, `东京`, `codeline` (target ranks: fact_1=92:107308, fact_2=21:59228, fact_3=6:110207, prefix_sum_12=113:123682, sum=119:115966)
- Layer 36: `足足`, `切割`, `ancock`, `锯`, ` disposed` (target ranks: fact_1=92:66813, fact_2=21:29048, fact_3=6:63146, prefix_sum_12=113:105560, sum=119:74746)
- Layer 37: `}<?`, `磨损`, `东京`, `简体`, `切割` (target ranks: fact_1=92:106244, fact_2=21:47535, fact_3=6:96895, prefix_sum_12=113:100848, sum=119:83833)
- Layer 38: `遁`, `切割`, ` .`, ` covari`, ` Fusion` (target ranks: fact_1=92:105075, fact_2=21:36104, fact_3=6:89713, prefix_sum_12=113:111160, sum=119:80964)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `简体`, `遁`, ` covari` (target ranks: fact_1=92:97924, fact_2=21:48531, fact_3=6:103145, prefix_sum_12=113:98071, sum=119:70500)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, `�` (target ranks: fact_1=92:75771, fact_2=21:24777, fact_3=6:50259, prefix_sum_12=113:63461, sum=119:44050)
- Layer 41: ` .`, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` .↵`, ` ` (target ranks: fact_1=92:28388, fact_2=21:4839, fact_3=6:4340, prefix_sum_12=113:28406, sum=119:25583)

### Filler position 48 (absolute token 563, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126844, fact_2=21:126532, fact_3=6:127971, prefix_sum_12=113:123854, sum=119:124493)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=92:11554, fact_2=21:7384, fact_3=6:2803, prefix_sum_12=113:26383, sum=119:21544)
- Layer 20: ` instantaneous`, `aharoa`, `东海`, `}<?`, `)Skip` (target ranks: fact_1=92:95960, fact_2=21:46751, fact_3=6:57708, prefix_sum_12=113:81417, sum=119:70091)
- Layer 30: `codeline`, `东京`, ` writ`, ` probable`, `叠` (target ranks: fact_1=92:98972, fact_2=21:36585, fact_3=6:42226, prefix_sum_12=113:94065, sum=119:100425)
- Layer 35: `codeline`, ` doubly`, `白雪`, ` germ`, `蜗` (target ranks: fact_1=92:105909, fact_2=21:33679, fact_3=6:71309, prefix_sum_12=113:123157, sum=119:120610)
- Layer 36: ` Predict`, ` nasod`, `停`, ` predictions`, ` soci` (target ranks: fact_1=92:67580, fact_2=21:27738, fact_3=6:24076, prefix_sum_12=113:95840, sum=119:86934)
- Layer 37: `Quintal`, `codeline`, `TreeLabel`, `悬挂`, `镶嵌` (target ranks: fact_1=92:118279, fact_2=21:64941, fact_3=6:86932, prefix_sum_12=113:95362, sum=119:109806)
- Layer 38: ` germ`, ` crev`, `悬挂`, `悬`, ` .` (target ranks: fact_1=92:117305, fact_2=21:37824, fact_3=6:58088, prefix_sum_12=113:81110, sum=119:95967)
- Layer 39: `�`, ` encomp`, ` germ`, `<｜begin▁of▁sentence｜>`, ` Dou` (target ranks: fact_1=92:118978, fact_2=21:66179, fact_3=6:112572, prefix_sum_12=113:97348, sum=119:102050)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, ` germ` (target ranks: fact_1=92:103698, fact_2=21:32210, fact_3=6:62788, prefix_sum_12=113:65254, sum=119:80132)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: fact_1=92:78164, fact_2=21:19627, fact_3=6:25008, prefix_sum_12=113:38379, sum=119:57847)

### Filler position 49 (absolute token 564, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=92:126925, fact_2=21:126645, fact_3=6:128060, prefix_sum_12=113:123980, sum=119:124556)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=92:11797, fact_2=21:7452, fact_3=6:2682, prefix_sum_12=113:26672, sum=119:22790)
- Layer 20: ` grounds`, `文本`, ` handwritten`, `子的`, ` impactful` (target ranks: fact_1=92:75923, fact_2=21:38079, fact_3=6:6570, prefix_sum_12=113:43935, sum=119:74925)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, ` answer` (target ranks: fact_1=92:126343, fact_2=21:120186, fact_3=6:117962, prefix_sum_12=113:97718, sum=119:122494)
- Layer 35: `codeline`, ` Answer`, `oNames`, `AED`, `�` (target ranks: fact_1=92:102935, fact_2=21:109973, fact_3=6:117454, prefix_sum_12=113:109648, sum=119:115372)
- Layer 36: ` Answer`, `坏`, ` answer`, `oNames`, ` reply` (target ranks: fact_1=92:49614, fact_2=21:40632, fact_3=6:60254, prefix_sum_12=113:69503, sum=119:72774)
- Layer 37: `oNames`, `codeline`, `�`, ` encomp`, `追加` (target ranks: fact_1=92:114536, fact_2=21:96401, fact_3=6:109070, prefix_sum_12=113:74214, sum=119:118000)
- Layer 38: `oNames`, ` encomp`, `codeline`, `�`, `tanle` (target ranks: fact_1=92:115633, fact_2=21:100204, fact_3=6:110686, prefix_sum_12=113:86491, sum=119:119472)
- Layer 39: `-ulo`, ` cryptocur`, ` encomp`, `�`, ` disadvant` (target ranks: fact_1=92:81956, fact_2=21:80146, fact_3=6:109216, prefix_sum_12=113:92010, sum=119:112315)
- Layer 40: ` .↵↵`, ` .`, ` Answer`, ` .↵`, ` tare` (target ranks: fact_1=92:11405, fact_2=21:8995, fact_3=6:20084, prefix_sum_12=113:36503, sum=119:72588)
- Layer 41: ` .`, ` .↵↵`, ` Answer`, `Answer`, ` .↵` (target ranks: fact_1=92:3473, fact_2=21:2311, fact_3=6:1207, prefix_sum_12=113:14890, sum=119:50137)

### Filler position 50 (absolute token 565, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: fact_1=92:121886, fact_2=21:122662, fact_3=6:126752, prefix_sum_12=113:109670, sum=119:114551)
- Layer 10: `EDMF`, ` dével`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=92:126316, fact_2=21:124534, fact_3=6:128492, prefix_sum_12=113:114386, sum=119:120071)
- Layer 20: `ait`, `能被`, `坷`, `平行`, `钩` (target ranks: fact_1=92:17649, fact_2=21:15708, fact_3=6:10520, prefix_sum_12=113:54864, sum=119:65202)
- Layer 30: ` Paglin`, ` dekameters`, ` المطلع`, `得分`, `批` (target ranks: fact_1=92:24475, fact_2=21:87889, fact_3=6:121908, prefix_sum_12=113:32758, sum=119:45762)
- Layer 35: ` Uran`, ` المطلع`, `296`, `uran`, ` Quote` (target ranks: fact_1=92:76, fact_2=21:83381, fact_3=6:114198, prefix_sum_12=113:5835, sum=119:2398)
- Layer 36: `296`, `297`, `306`, `286`, `285` (target ranks: fact_1=92:24, fact_2=21:115178, fact_3=6:93253, prefix_sum_12=113:529, sum=119:123)
- Layer 37: ` Paglin`, `uran`, `92`, ` المطلع`, ` المجره` (target ranks: fact_1=92:3, fact_2=21:125943, fact_3=6:119119, prefix_sum_12=113:7198, sum=119:1901)
- Layer 38: ` Paglin`, `uran`, ` perturb`, `}<?`, ` Tucker` (target ranks: fact_1=92:6, fact_2=21:119354, fact_3=6:123791, prefix_sum_12=113:4199, sum=119:1190)
- Layer 39: ` Paglin`, `索赔`, `音符`, `orsch`, `陆地` (target ranks: fact_1=92:61409, fact_2=21:118246, fact_3=6:121854, prefix_sum_12=113:1407, sum=119:1199)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `答案` (target ranks: fact_1=92:18155, fact_2=21:101491, fact_3=6:92722, prefix_sum_12=113:1188, sum=119:448)
- Layer 41: `Answer`, ` Answer`, ` answer`, `answer`, `答案` (target ranks: fact_1=92:4134, fact_2=21:10877, fact_3=6:1373, prefix_sum_12=113:1371, sum=119:401)

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

Answer:<｜Assistant｜></think>177<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Uranium plus the atomic number of Scandium plus the atomic number of Carbon?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
