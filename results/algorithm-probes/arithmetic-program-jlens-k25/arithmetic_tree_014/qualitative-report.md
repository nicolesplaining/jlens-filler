# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `116` (correct).
- No-filler answer: `116` (correct).
- Filler tokens: 25 tokens at absolute indices 733–757.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `p1=20` | 2 (L40, filler 15) | L40, filler 15 (rank 2) |
| J-Lens | `p2=4` | 23 (L21, filler 4) | Never |
| J-Lens | `p3=18` | 1 (L38, filler 16) | L31, filler 9 (rank 3) |
| J-Lens | `p4=2` | 81 (L35, filler 18) | Never |
| J-Lens | `m1=80` | 47 (L35, filler 3) | Never |
| J-Lens | `m2=36` | 1 (L31, filler 4) | L31, filler 4 (rank 1) |
| J-Lens | `y=116` | 2 (L37, filler 4) | L37, filler 4 (rank 2) |
| Logit lens | `p1=20` | 2 (L41, filler 15) | L39, filler 15 (rank 6) |
| Logit lens | `p2=4` | 9 (L31, filler 11) | L31, filler 11 (rank 9) |
| Logit lens | `p3=18` | 1 (L29, filler 9) | L28, filler 9 (rank 7) |
| Logit lens | `p4=2` | 4 (L30, filler 9) | L29, filler 9 (rank 7) |
| Logit lens | `m1=80` | 99 (L35, filler 25) | Never |
| Logit lens | `m2=36` | 1 (L26, filler 7) | L25, filler 7 (rank 4) |
| Logit lens | `y=116` | 9 (L39, filler 4) | L39, filler 4 (rank 9) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 733, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: p1=20:119764, p2=4:125783, p3=18:121550, p4=2:126023, m1=80:120217, m2=36:119759, y=116:108680)
- Layer 10: `忑`, `anta`, `fine`, ` Walker`, `locked` (target ranks: p1=20:28457, p2=4:20528, p3=18:32689, p4=2:22077, m1=80:35714, m2=36:32724, y=116:48928)
- Layer 20: ` .`, `/.`, `dots`, ` dots`, `Dot` (target ranks: p1=20:7315, p2=4:8135, p3=18:17436, p4=2:22815, m1=80:13528, m2=36:24133, y=116:95375)
- Layer 30: ` pakig`, ` talags`, `tap`, `希望能够`, ` پاسخ` (target ranks: p1=20:22448, p2=4:43946, p3=18:33559, p4=2:65877, m1=80:18809, m2=36:41918, y=116:80020)
- Layer 35: `oooo`, `应答`, ` tap`, ` پاسخ`, `Tap` (target ranks: p1=20:1688, p2=4:6928, p3=18:4849, p4=2:12335, m1=80:592, m2=36:4411, y=116:38497)
- Layer 36: ` talags`, `期望`, ` tap`, `私`, ` Tap` (target ranks: p1=20:3157, p2=4:11054, p3=18:7161, p4=2:16394, m1=80:1656, m2=36:4495, y=116:27119)
- Layer 37: ` talags`, ` pakig`, `}<?`, `在北京`, `ِّف` (target ranks: p1=20:65887, p2=4:91633, p3=18:64727, p4=2:101315, m1=80:40891, m2=36:73841, y=116:55096)
- Layer 38: ` talags`, ` pakig`, `}<?`, `ِّف`, `osit` (target ranks: p1=20:86357, p2=4:93898, p3=18:90054, p4=2:111145, m1=80:41207, m2=36:94990, y=116:41117)
- Layer 39: ` talags`, `}<?`, ` pakig`, `+-+-+-+-`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: p1=20:109725, p2=4:119633, p3=18:121082, p4=2:120461, m1=80:109953, m2=36:110310, y=116:108508)
- Layer 40: ` talags`, ` .`, `dots`, ` nasod`, `一个一个` (target ranks: p1=20:59824, p2=4:63981, p3=18:101335, p4=2:54600, m1=80:86376, m2=36:65349, y=116:94326)
- Layer 41: ` .`, `我没有`, ` .↵↵`, ` .↵`, `一个一个` (target ranks: p1=20:72154, p2=4:59517, p3=18:53880, p4=2:40988, m1=80:94266, m2=36:42754, y=116:74901)

### Filler position 2 (absolute token 734, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: p1=20:121417, p2=4:125830, p3=18:122848, p4=2:126395, m1=80:122299, m2=36:120744, y=116:114168)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: p1=20:16755, p2=4:5547, p3=18:16843, p4=2:6187, m1=80:21168, m2=36:18125, y=116:40149)
- Layer 20: ` .`, ` .----`, ` .↵↵`, ` .↵`, `往常` (target ranks: p1=20:63734, p2=4:76387, p3=18:106083, p4=2:98557, m1=80:103325, m2=36:111164, y=116:117807)
- Layer 30: ` dekameters`, ` etxek`, ` hilabihan`, ` pakig`, ` .----` (target ranks: p1=20:77731, p2=4:120251, p3=18:110152, p4=2:125019, m1=80:118810, m2=36:121680, y=116:110238)
- Layer 35: ` .`, `enclose`, ` silic`, ` hilabihan`, ` ninete` (target ranks: p1=20:69572, p2=4:110168, p3=18:83844, p4=2:108906, m1=80:117910, m2=36:122931, y=116:118391)
- Layer 36: `停`, ` .`, `enclose`, `空空`, ` nasod` (target ranks: p1=20:33955, p2=4:63599, p3=18:34401, p4=2:59692, m1=80:86500, m2=36:104196, y=116:92017)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, ` Erkännande`, `TreeLabel` (target ranks: p1=20:114736, p2=4:124396, p3=18:110630, p4=2:126271, m1=80:120328, m2=36:126735, y=116:114520)
- Layer 38: ` .`, ` hilabihan`, `}<?`, `繁体`, `�乐` (target ranks: p1=20:89466, p2=4:115306, p3=18:81862, p4=2:124831, m1=80:106964, m2=36:121513, y=116:92878)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` hilabihan`, ` talags`, `不急` (target ranks: p1=20:81502, p2=4:114852, p3=18:92538, p4=2:119859, m1=80:97355, m2=36:114547, y=116:89401)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, `不急` (target ranks: p1=20:31854, p2=4:60683, p3=18:51902, p4=2:69876, m1=80:80165, m2=36:92791, y=116:68585)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `不急`, `不不` (target ranks: p1=20:20952, p2=4:8494, p3=18:24749, p4=2:4679, m1=80:49599, m2=36:49741, y=116:19347)

### Filler position 3 (absolute token 735, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:124862, p2=4:127927, p3=18:125671, p4=2:128233, m1=80:125921, m2=36:124752, y=116:117609)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, `挪` (target ranks: p1=20:11654, p2=4:4354, p3=18:11310, p4=2:4528, m1=80:14305, m2=36:11856, y=116:26860)
- Layer 20: `ait`, `忑`, `cape`, `锁定`, ` wig` (target ranks: p1=20:9551, p2=4:1731, p3=18:12812, p4=2:4256, m1=80:8280, m2=36:5691, y=116:34543)
- Layer 30: `esper`, `Tap`, ` esper`, ` waterfall`, `tap` (target ranks: p1=20:6535, p2=4:2824, p3=18:9873, p4=2:13895, m1=80:2181, m2=36:1974, y=116:16510)
- Layer 35: ` answer`, `acks`, ` Answer`, `ANSWER`, ` ANSWER` (target ranks: p1=20:1226, p2=4:899, p3=18:5455, p4=2:5954, m1=80:47, m2=36:212, y=116:2649)
- Layer 36: `期待`, `calcul`, `acks`, `期待的`, `计算的` (target ranks: p1=20:6597, p2=4:4163, p3=18:17674, p4=2:15009, m1=80:348, m2=36:614, y=116:3997)
- Layer 37: `等待着`, `计算的`, `算计`, `calcul`, `计算` (target ranks: p1=20:23765, p2=4:18977, p3=18:54014, p4=2:46686, m1=80:629, m2=36:4134, y=116:2698)
- Layer 38: `ocyst`, `思想的`, `}<?`, `桃花`, `本题分析` (target ranks: p1=20:74982, p2=4:63242, p3=18:102527, p4=2:101127, m1=80:8859, m2=36:41023, y=116:15510)
- Layer 39: `}<?`, `思想的`, `迷惑`, `hatic`, `叶子` (target ranks: p1=20:96283, p2=4:99446, p3=18:110308, p4=2:115379, m1=80:54450, m2=36:70222, y=116:64695)
- Layer 40: ` `, `迷惑`, ` ANSWER`, `叮`, `语言文字` (target ranks: p1=20:51234, p2=4:32438, p3=18:92247, p4=2:58759, m1=80:27460, m2=36:37548, y=116:32568)
- Layer 41: ` .`, `试一试`, ` wherever`, `等待`, ` without` (target ranks: p1=20:21229, p2=4:13690, p3=18:67693, p4=2:9562, m1=80:49534, m2=36:43624, y=116:28316)

### Filler position 4 (absolute token 736, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125760, p2=4:128393, p3=18:126494, p4=2:128635, m1=80:126717, m2=36:125472, y=116:119409)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=20:11889, p2=4:3650, p3=18:10999, p4=2:3848, m1=80:13337, m2=36:11589, y=116:25771)
- Layer 20: ` LS`, `ait`, `cape`, `ative`, ` quadr` (target ranks: p1=20:3308, p2=4:26, p3=18:3085, p4=2:238, m1=80:3418, m2=36:2240, y=116:20679)
- Layer 30: `acons`, `乘积`, `apons`, ` consum`, `得分` (target ranks: p1=20:38797, p2=4:8983, p3=18:2395, p4=2:21364, m1=80:68111, m2=36:630, y=116:47464)
- Layer 35: `}<?`, ` Gikuha`, `036`, ` talags`, `otechnical` (target ranks: p1=20:128192, p2=4:43623, p3=18:2687, p4=2:123516, m1=80:87044, m2=36:69, y=116:26354)
- Layer 36: ` dátummal`, `}<?`, ` ---|---|---|---|---|---|---`, ` ---|---|---|---`, `兄弟` (target ranks: p1=20:120975, p2=4:98012, p3=18:2901, p4=2:120336, m1=80:65526, m2=36:198, y=116:70)
- Layer 37: `76`, `116`, ` böjnings`, ` Fylke`, ` Brother` (target ranks: p1=20:113898, p2=4:72933, p3=18:3889, p4=2:105849, m1=80:42089, m2=36:214, y=116:2)
- Layer 38: `76`, `116`, `兄弟`, ` sibling`, `56` (target ranks: p1=20:108288, p2=4:64829, p3=18:248, p4=2:118579, m1=80:54242, m2=36:44, y=116:2)
- Layer 39: `76`, `116`, `56`, ` dátummal`, `118` (target ranks: p1=20:93235, p2=4:105747, p3=18:21457, p4=2:119461, m1=80:2346, m2=36:531, y=116:2)
- Layer 40: `76`, `116`, ` seventy`, ` dátummal`, ` eighty` (target ranks: p1=20:77082, p2=4:65235, p3=18:13612, p4=2:96778, m1=80:324, m2=36:150, y=116:2)
- Layer 41: ` .`, `推荐文章`, `错过了`, `错过`, `满足了` (target ranks: p1=20:38636, p2=4:43572, p3=18:9577, p4=2:33895, m1=80:8136, m2=36:7653, y=116:54)

### Filler position 5 (absolute token 737, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125588, p2=4:128339, p3=18:126234, p4=2:128604, m1=80:126350, m2=36:125117, y=116:119480)
- Layer 10: ` Walker`, `锁定`, `挪`, `Walker`, `ait` (target ranks: p1=20:12213, p2=4:4399, p3=18:11315, p4=2:4514, m1=80:13929, m2=36:12766, y=116:28348)
- Layer 20: `幽`, ` LS`, `鞍`, `锁定`, `挪` (target ranks: p1=20:10423, p2=4:3181, p3=18:10378, p4=2:2451, m1=80:12030, m2=36:12602, y=116:30957)
- Layer 30: `acos`, `�`, `鞍`, `接近`, ` corona` (target ranks: p1=20:37434, p2=4:22425, p3=18:41872, p4=2:22008, m1=80:72817, m2=36:49014, y=116:83062)
- Layer 35: `羊`, ` var`, `旅`, ` repetition`, `�` (target ranks: p1=20:20682, p2=4:9802, p3=18:26165, p4=2:7696, m1=80:52518, m2=36:45529, y=116:70883)
- Layer 36: `berg`, `羊`, `bergh`, ` talags`, `反复` (target ranks: p1=20:35256, p2=4:21257, p3=18:40988, p4=2:16069, m1=80:66413, m2=36:55692, y=116:53103)
- Layer 37: ` talags`, `}<?`, `acos`, `轨迹`, `hemer` (target ranks: p1=20:84818, p2=4:70665, p3=18:88094, p4=2:56077, m1=80:101516, m2=36:97863, y=116:75931)
- Layer 38: `}<?`, `hemer`, ` talags`, `�`, `onis` (target ranks: p1=20:110141, p2=4:92450, p3=18:100372, p4=2:83360, m1=80:117361, m2=36:111148, y=116:97477)
- Layer 39: ` talags`, `hemer`, `迷惑`, `}<?`, `�` (target ranks: p1=20:114032, p2=4:114160, p3=18:108922, p4=2:102660, m1=80:122997, m2=36:113871, y=116:110967)
- Layer 40: ` talags`, ` nasod`, `坏`, ` x`, `тельными` (target ranks: p1=20:88411, p2=4:63533, p3=18:70156, p4=2:38025, m1=80:116898, m2=36:82108, y=116:84424)
- Layer 41: ` .`, `鹉`, `<｜end▁of▁sentence｜>`, `下面是`, `坏` (target ranks: p1=20:46398, p2=4:26047, p3=18:46407, p4=2:6353, m1=80:107321, m2=36:65638, y=116:62642)

### Filler position 6 (absolute token 738, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125436, p2=4:128287, p3=18:126042, p4=2:128558, m1=80:126148, m2=36:124903, y=116:119562)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=20:11613, p2=4:4209, p3=18:10787, p4=2:4387, m1=80:13674, m2=36:11533, y=116:26229)
- Layer 20: ` unflagged`, `修罗`, ` corrected`, ` notations`, `notations` (target ranks: p1=20:96700, p2=4:107100, p3=18:95391, p4=2:116777, m1=80:105498, m2=36:93111, y=116:116132)
- Layer 30: `高明`, `分解`, `推算`, `梯`, ` combinator` (target ranks: p1=20:16326, p2=4:19471, p3=18:7257, p4=2:25405, m1=80:21218, m2=36:24711, y=116:47302)
- Layer 35: `高明`, `acks`, ` lab`, `幽`, ` voids` (target ranks: p1=20:8916, p2=4:34396, p3=18:8456, p4=2:42868, m1=80:16955, m2=36:24248, y=116:68874)
- Layer 36: `高明`, ` pakig`, `acks`, ` voids`, `柿子` (target ranks: p1=20:10718, p2=4:36261, p3=18:10147, p4=2:49726, m1=80:16233, m2=36:39320, y=116:48833)
- Layer 37: ` pakig`, `高明`, `跃`, ` Rutherford`, ` Perl` (target ranks: p1=20:32271, p2=4:99500, p3=18:32645, p4=2:98798, m1=80:41746, m2=36:82935, y=116:88489)
- Layer 38: ` pakig`, `高明`, `跃`, `蒲公英`, ` ladder` (target ranks: p1=20:42530, p2=4:101092, p3=18:37588, p4=2:105204, m1=80:59749, m2=36:82780, y=116:85344)
- Layer 39: `}<?`, ` pakig`, ` talags`, `dividers`, `MMMMMMMM` (target ranks: p1=20:112774, p2=4:126788, p3=18:81997, p4=2:124786, m1=80:124922, m2=36:124317, y=116:124836)
- Layer 40: ` Fifteen`, ` talags`, ` dotted`, ` fifteen`, ` pakig` (target ranks: p1=20:83803, p2=4:110152, p3=18:41206, p4=2:78046, m1=80:122007, m2=36:118414, y=116:114832)
- Layer 41: ` .`, ` Fifteen`, `一个一个`, ` filler`, ` dotted` (target ranks: p1=20:63543, p2=4:51992, p3=18:41026, p4=2:18247, m1=80:117599, m2=36:111262, y=116:89884)

### Filler position 7 (absolute token 739, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125292, p2=4:128247, p3=18:125922, p4=2:128506, m1=80:125881, m2=36:124698, y=116:119328)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=20:10225, p2=4:3328, p3=18:9237, p4=2:3396, m1=80:11908, m2=36:10158, y=116:24442)
- Layer 20: `锁定`, `ait`, `鞍`, ` cheer`, ` smile` (target ranks: p1=20:4925, p2=4:596, p3=18:4209, p4=2:1221, m1=80:2631, m2=36:2701, y=116:17729)
- Layer 30: `输入的`, `鞍`, ` strike`, `yg`, `幽` (target ranks: p1=20:661, p2=4:781, p3=18:1420, p4=2:3711, m1=80:215, m2=36:49, y=116:689)
- Layer 35: `锁定`, `86`, `鞍`, ` labor`, `特` (target ranks: p1=20:379, p2=4:599, p3=18:1629, p4=2:1930, m1=80:120, m2=36:36, y=116:492)
- Layer 36: `特`, ` stabil`, `86`, ` pakig`, `特异` (target ranks: p1=20:3003, p2=4:4081, p3=18:8283, p4=2:11791, m1=80:328, m2=36:52, y=116:172)
- Layer 37: ` pakig`, `ocyst`, ` Septy`, `ozygous`, ` talags` (target ranks: p1=20:31960, p2=4:31590, p3=18:38942, p4=2:56214, m1=80:6970, m2=36:328, y=116:105)
- Layer 38: `}<?`, `ocyst`, ` Noruwega`, `opters`, `本题分析` (target ranks: p1=20:72966, p2=4:82260, p3=18:85276, p4=2:105081, m1=80:35910, m2=36:5048, y=116:2573)
- Layer 39: `}<?`, `ocyst`, `opters`, ` pakig`, `ozygous` (target ranks: p1=20:117026, p2=4:111698, p3=18:80863, p4=2:116672, m1=80:35844, m2=36:16423, y=116:2571)
- Layer 40: ` pakig`, ` talags`, `留存`, `反复`, ` drip` (target ranks: p1=20:111769, p2=4:72156, p3=18:51356, p4=2:78745, m1=80:28371, m2=36:8645, y=116:829)
- Layer 41: ` .`, `试一试`, `秆`, `潜伏`, `我曾经` (target ranks: p1=20:85119, p2=4:49663, p3=18:28649, p4=2:26226, m1=80:57473, m2=36:28411, y=116:1878)

### Filler position 8 (absolute token 740, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125267, p2=4:128256, p3=18:125933, p4=2:128518, m1=80:125920, m2=36:124696, y=116:119608)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: p1=20:10693, p2=4:3626, p3=18:9725, p4=2:3691, m1=80:12031, m2=36:10583, y=116:25241)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, ` smile` (target ranks: p1=20:6965, p2=4:1362, p3=18:7449, p4=2:2089, m1=80:7597, m2=36:5538, y=116:31592)
- Layer 30: `acos`, `鞍`, `acin`, `特`, `平行` (target ranks: p1=20:29153, p2=4:22791, p3=18:28235, p4=2:34865, m1=80:34798, m2=36:12765, y=116:44446)
- Layer 35: ` met`, `acks`, `忑`, ` repetition`, ` Propri` (target ranks: p1=20:11110, p2=4:2680, p3=18:15312, p4=2:4456, m1=80:18046, m2=36:10344, y=116:31877)
- Layer 36: ` tap`, `adal`, ` Tap`, `特`, `Tap` (target ranks: p1=20:12497, p2=4:2487, p3=18:13158, p4=2:5275, m1=80:17436, m2=36:6813, y=116:16664)
- Layer 37: ` Zad`, `acos`, `关`, `特`, `}<?` (target ranks: p1=20:39381, p2=4:10238, p3=18:59793, p4=2:27486, m1=80:40008, m2=36:20603, y=116:19768)
- Layer 38: `}<?`, ` Zad`, `坏`, `pac`, `等待着` (target ranks: p1=20:71117, p2=4:31460, p3=18:76122, p4=2:59992, m1=80:64846, m2=36:40272, y=116:47170)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `osos`, ` talags`, `迷惑` (target ranks: p1=20:69422, p2=4:81470, p3=18:67800, p4=2:93324, m1=80:82153, m2=36:57348, y=116:71897)
- Layer 40: ` talags`, ` .`, `scr`, `留存`, `下沉` (target ranks: p1=20:24471, p2=4:20653, p3=18:24126, p4=2:28063, m1=80:58698, m2=36:17251, y=116:33421)
- Layer 41: ` .`, `有下列`, `试一试`, `一个一个`, `下面是` (target ranks: p1=20:17263, p2=4:14623, p3=18:13597, p4=2:12651, m1=80:71424, m2=36:16601, y=116:26000)

### Filler position 9 (absolute token 741, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125234, p2=4:128253, p3=18:125949, p4=2:128521, m1=80:125913, m2=36:124673, y=116:119725)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `挪` (target ranks: p1=20:10134, p2=4:3442, p3=18:9185, p4=2:3413, m1=80:11598, m2=36:10394, y=116:25088)
- Layer 20: `锁定`, ` Walker`, `ait`, `能被`, ` cheer` (target ranks: p1=20:5073, p2=4:840, p3=18:4612, p4=2:1038, m1=80:4884, m2=36:4996, y=116:23166)
- Layer 30: `acos`, ` glacier`, `柿子`, `期望`, `冰` (target ranks: p1=20:22102, p2=4:15950, p3=18:22, p4=2:5270, m1=80:27446, m2=36:794, y=116:44309)
- Layer 35: ` eighteen`, `十八`, `18`, `三十六`, `obin` (target ranks: p1=20:54257, p2=4:21878, p3=18:3, p4=2:21979, m1=80:26008, m2=36:9, y=116:15941)
- Layer 36: `三十六`, `}<?`, ` eighteen`, `十八`, ` pakig` (target ranks: p1=20:95008, p2=4:41598, p3=18:11, p4=2:33802, m1=80:84395, m2=36:7, y=116:12774)
- Layer 37: `十八`, `三十六`, `}<?`, `覆`, ` eighteen` (target ranks: p1=20:101950, p2=4:40143, p3=18:11, p4=2:35314, m1=80:98127, m2=36:31, y=116:11160)
- Layer 38: `}<?`, `三十六`, `覆`, `窃`, ` polar` (target ranks: p1=20:98058, p2=4:33823, p3=18:13, p4=2:24446, m1=80:107771, m2=36:7, y=116:10279)
- Layer 39: `}<?`, `ozygous`, `东海`, `oscel`, `?datasetId` (target ranks: p1=20:121736, p2=4:81093, p3=18:56631, p4=2:84364, m1=80:96006, m2=36:8144, y=116:9192)
- Layer 40: `}<?`, ` unint`, `ascals`, ` ons`, ` .` (target ranks: p1=20:99791, p2=4:28681, p3=18:59765, p4=2:28757, m1=80:63872, m2=36:13210, y=116:1790)
- Layer 41: ` .`, `那两个`, ` .↵↵`, `况且`, `鹉` (target ranks: p1=20:88803, p2=4:26498, p3=18:34606, p4=2:12443, m1=80:62429, m2=36:12715, y=116:2853)

### Filler position 10 (absolute token 742, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125263, p2=4:128296, p3=18:126046, p4=2:128550, m1=80:126014, m2=36:124692, y=116:119901)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `挪` (target ranks: p1=20:9861, p2=4:3471, p3=18:9019, p4=2:3484, m1=80:11384, m2=36:10243, y=116:25119)
- Layer 20: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=20:8437, p2=4:4924, p3=18:9550, p4=2:4128, m1=80:9969, m2=36:12371, y=116:40063)
- Layer 30: ` sequential`, `sequential`, `Sequ`, `重复`, ` repeated` (target ranks: p1=20:30247, p2=4:19328, p3=18:26114, p4=2:13850, m1=80:32817, m2=36:38570, y=116:57967)
- Layer 35: ` sequential`, `sequential`, ` repetition`, `Sequ`, `分解` (target ranks: p1=20:17139, p2=4:10954, p3=18:14776, p4=2:5329, m1=80:17014, m2=36:19167, y=116:31024)
- Layer 36: `sequential`, ` sequential`, `分解`, ` sequence`, `Sequ` (target ranks: p1=20:27689, p2=4:29674, p3=18:25010, p4=2:17011, m1=80:23550, m2=36:28280, y=116:30853)
- Layer 37: `}<?`, `sequence`, `sequential`, `程序的`, ` sequence` (target ranks: p1=20:55947, p2=4:81795, p3=18:53902, p4=2:50711, m1=80:53279, m2=36:63322, y=116:39851)
- Layer 38: `}<?`, `程序的`, `sequence`, `structured`, `sequences` (target ranks: p1=20:69516, p2=4:92536, p3=18:65825, p4=2:65130, m1=80:55949, m2=36:60573, y=116:41987)
- Layer 39: `}<?`, `程序的`, `sequence`, `替换`, `structured` (target ranks: p1=20:84078, p2=4:114618, p3=18:95958, p4=2:98761, m1=80:98554, m2=36:98890, y=116:79011)
- Layer 40: `}<?`, `程序的`, ` talags`, ` drip`, `程序` (target ranks: p1=20:52743, p2=4:68615, p3=18:57699, p4=2:34386, m1=80:77907, m2=36:58910, y=116:62053)
- Layer 41: ` .`, ` without`, `程序`, `F`, `程序的` (target ranks: p1=20:13166, p2=4:12871, p3=18:29589, p4=2:1443, m1=80:45451, m2=36:36877, y=116:29419)

### Filler position 11 (absolute token 743, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125478, p2=4:128419, p3=18:126353, p4=2:128653, m1=80:126417, m2=36:124875, y=116:120830)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `挪` (target ranks: p1=20:10441, p2=4:3510, p3=18:9742, p4=2:3497, m1=80:12373, m2=36:10676, y=116:26947)
- Layer 20: ` LS`, ` smile`, `锁定`, `Ta`, `挪` (target ranks: p1=20:1215, p2=4:107, p3=18:1503, p4=2:187, m1=80:1530, m2=36:791, y=116:17192)
- Layer 30: `iret`, ` consuming`, ` pakig`, ` ---|---|---|---|---|---|---`, `acons` (target ranks: p1=20:6695, p2=4:4931, p3=18:6076, p4=2:11696, m1=80:18405, m2=36:234, y=116:60843)
- Layer 35: ` pakig`, ` Gikuha`, `守法`, `otechnical`, `寨` (target ranks: p1=20:102805, p2=4:9079, p3=18:861, p4=2:102605, m1=80:40516, m2=36:5729, y=116:35151)
- Layer 36: `兄弟`, ` dátummal`, ` Brother`, `}<?`, ` brother` (target ranks: p1=20:60726, p2=4:74712, p3=18:413, p4=2:120904, m1=80:59816, m2=36:7302, y=116:1273)
- Layer 37: ` Brother`, `兄弟`, `二十八`, ` Fylke`, ` Gikuha` (target ranks: p1=20:49739, p2=4:49555, p3=18:444, p4=2:98492, m1=80:39334, m2=36:8871, y=116:227)
- Layer 38: `二十八`, `兄弟`, `十八条`, ` Brother`, `118` (target ranks: p1=20:74069, p2=4:47100, p3=18:129, p4=2:113216, m1=80:63067, m2=36:11567, y=116:291)
- Layer 39: `84`, `88`, `桃子`, ` eighty`, `}<?` (target ranks: p1=20:62032, p2=4:71927, p3=18:20894, p4=2:111779, m1=80:2574, m2=36:12844, y=116:482)
- Layer 40: `84`, ` eighty`, ` dátummal`, `<｜begin▁of▁file｜>`, ` dekameters` (target ranks: p1=20:64486, p2=4:36117, p3=18:8677, p4=2:93777, m1=80:1775, m2=36:9222, y=116:106)
- Layer 41: ` nuest`, `茶馆`, `培养了`, ` provided`, ` .` (target ranks: p1=20:38531, p2=4:18724, p3=18:6852, p4=2:17755, m1=80:7065, m2=36:12135, y=116:364)

### Filler position 12 (absolute token 744, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125530, p2=4:128464, p3=18:126407, p4=2:128685, m1=80:126498, m2=36:124932, y=116:121063)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=20:10542, p2=4:3393, p3=18:9768, p4=2:3357, m1=80:12883, m2=36:10204, y=116:26437)
- Layer 20: `ait`, `锁定`, ` wig`, ` smile`, ` Walker` (target ranks: p1=20:8619, p2=4:1428, p3=18:9909, p4=2:2806, m1=80:10079, m2=36:7427, y=116:37486)
- Layer 30: `Tap`, `tap`, ` tap`, ` Tap`, `打完` (target ranks: p1=20:7255, p2=4:28024, p3=18:35881, p4=2:62467, m1=80:55437, m2=36:5880, y=116:63325)
- Layer 35: ` tap`, `Tap`, `tap`, ` Tap`, `acks` (target ranks: p1=20:2079, p2=4:4085, p3=18:19153, p4=2:15925, m1=80:47031, m2=36:6028, y=116:31428)
- Layer 36: `期望`, ` tap`, `Tap`, ` Tap`, `tap` (target ranks: p1=20:1394, p2=4:1315, p3=18:9153, p4=2:7740, m1=80:27607, m2=36:4912, y=116:19306)
- Layer 37: `坏`, `acet`, `EDAC`, `等待着`, ` resist` (target ranks: p1=20:6575, p2=4:13511, p3=18:32401, p4=2:40117, m1=80:58393, m2=36:25480, y=116:38030)
- Layer 38: `坏`, `}<?`, `等待着`, `acons`, `等着` (target ranks: p1=20:16577, p2=4:29069, p3=18:47176, p4=2:66483, m1=80:71203, m2=36:33208, y=116:49591)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `东海`, ` talags`, `繁体` (target ranks: p1=20:63261, p2=4:104167, p3=18:81715, p4=2:105442, m1=80:102903, m2=36:76497, y=116:114722)
- Layer 40: ` mosunod`, ` Twenty`, `试一试`, ` ANSWER`, `省略` (target ranks: p1=20:15298, p2=4:30362, p3=18:28731, p4=2:33236, m1=80:67239, m2=36:19333, y=116:72502)
- Layer 41: ` .`, `试一试`, `等待`, ` answer`, `ldots` (target ranks: p1=20:13133, p2=4:15844, p3=18:34255, p4=2:6789, m1=80:77612, m2=36:18123, y=116:58646)

### Filler position 13 (absolute token 745, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125721, p2=4:128532, p3=18:126581, p4=2:128742, m1=80:126704, m2=36:125163, y=116:121454)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=20:10439, p2=4:3710, p3=18:9499, p4=2:3640, m1=80:12198, m2=36:10853, y=116:26468)
- Layer 20: `锁定`, `忑`, `ait`, ` Walker`, `Walker` (target ranks: p1=20:14455, p2=4:6618, p3=18:17094, p4=2:7749, m1=80:13821, m2=36:17801, y=116:43289)
- Layer 30: ` calculator`, `平行`, `鞍`, ` repetitions`, ` parallel` (target ranks: p1=20:33187, p2=4:15942, p3=18:42063, p4=2:22250, m1=80:22022, m2=36:14003, y=116:66324)
- Layer 35: ` calculator`, ` equations`, `锁定`, ` exercises`, ` program` (target ranks: p1=20:11724, p2=4:4240, p3=18:18670, p4=2:4088, m1=80:12774, m2=36:3809, y=116:31861)
- Layer 36: ` program`, ` tap`, ` equations`, ` calculator`, `程式` (target ranks: p1=20:15461, p2=4:5143, p3=18:19981, p4=2:4878, m1=80:15313, m2=36:3301, y=116:26694)
- Layer 37: ` program`, `程序的`, `程序`, `程式`, `program` (target ranks: p1=20:56356, p2=4:40814, p3=18:78374, p4=2:29337, m1=80:47876, m2=36:13713, y=116:45301)
- Layer 38: `}<?`, `程序的`, ` program`, `程序`, `程式` (target ranks: p1=20:63863, p2=4:63303, p3=18:97144, p4=2:57269, m1=80:75411, m2=36:30700, y=116:65358)
- Layer 39: `}<?`, `坏的`, `�乐`, `下沉`, `acons` (target ranks: p1=20:81243, p2=4:116268, p3=18:114924, p4=2:105183, m1=80:103465, m2=36:85209, y=116:104361)
- Layer 40: `坏的`, `}<?`, `坏`, ` .`, ` lion` (target ranks: p1=20:40454, p2=4:65420, p3=18:81521, p4=2:31257, m1=80:92170, m2=36:40164, y=116:81301)
- Layer 41: ` .`, ` .↵↵`, ` `, ` awaiting`, `那两个` (target ranks: p1=20:39918, p2=4:39470, p3=18:58240, p4=2:8141, m1=80:76396, m2=36:33213, y=116:56117)

### Filler position 14 (absolute token 746, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125840, p2=4:128607, p3=18:126754, p4=2:128799, m1=80:126917, m2=36:125309, y=116:121891)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=20:9749, p2=4:3423, p3=18:8819, p4=2:3438, m1=80:11487, m2=36:9732, y=116:24142)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, `拆` (target ranks: p1=20:10301, p2=4:3517, p3=18:11343, p4=2:5270, m1=80:10650, m2=36:10897, y=116:31912)
- Layer 30: `计算的`, `acos`, `平行`, `acin`, `打完` (target ranks: p1=20:20738, p2=4:9758, p3=18:38580, p4=2:25559, m1=80:22946, m2=36:12001, y=116:69094)
- Layer 35: ` calculator`, `计算的`, `calcul`, ` equations`, `柿子` (target ranks: p1=20:8114, p2=4:5155, p3=18:19320, p4=2:11537, m1=80:10405, m2=36:5105, y=116:31800)
- Layer 36: `计算的`, `柿子`, `俯`, `留存`, `calcul` (target ranks: p1=20:13702, p2=4:9968, p3=18:25118, p4=2:24676, m1=80:13340, m2=36:9640, y=116:23639)
- Layer 37: `}<?`, `acos`, `dividers`, `放下`, `班的` (target ranks: p1=20:61415, p2=4:68225, p3=18:80857, p4=2:89692, m1=80:50074, m2=36:41225, y=116:33121)
- Layer 38: `}<?`, `acons`, `ِّف`, `dividers`, `acos` (target ranks: p1=20:85215, p2=4:87765, p3=18:89579, p4=2:107997, m1=80:74757, m2=36:62331, y=116:47886)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, ` talags`, ` Noruwega`, `hatic` (target ranks: p1=20:70713, p2=4:112750, p3=18:104982, p4=2:116986, m1=80:91227, m2=36:88285, y=116:89727)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, `scr`, `下沉`, `留存` (target ranks: p1=20:27423, p2=4:51061, p3=18:58557, p4=2:59315, m1=80:72654, m2=36:52201, y=116:66812)
- Layer 41: ` .`, ` .↵↵`, ` `, `<｜end▁of▁sentence｜>`, ` because` (target ranks: p1=20:26516, p2=4:18691, p3=18:46405, p4=2:11182, m1=80:50160, m2=36:40292, y=116:50118)

### Filler position 15 (absolute token 747, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=20:125810, p2=4:128610, p3=18:126750, p4=2:128805, m1=80:126903, m2=36:125297, y=116:121889)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=20:9760, p2=4:3366, p3=18:8928, p4=2:3350, m1=80:11749, m2=36:9889, y=116:24669)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, ` smile` (target ranks: p1=20:5142, p2=4:911, p3=18:5050, p4=2:1890, m1=80:5354, m2=36:3897, y=116:21655)
- Layer 30: `11`, `+a`, `sets`, `打完`, `acos` (target ranks: p1=20:8078, p2=4:8224, p3=18:3777, p4=2:21970, m1=80:19209, m2=36:3698, y=116:8033)
- Layer 35: `11`, `分解`, ` eleven`, `俯`, ` dy` (target ranks: p1=20:633, p2=4:4323, p3=18:291, p4=2:11251, m1=80:5968, m2=36:560, y=116:5910)
- Layer 36: `11`, `留存`, `俯`, ` eleven`, `分解` (target ranks: p1=20:1650, p2=4:12699, p3=18:803, p4=2:27050, m1=80:14954, m2=36:1837, y=116:5087)
- Layer 37: `11`, `acos`, ` eleven`, `不加`, `}<?` (target ranks: p1=20:187, p2=4:73311, p3=18:2116, p4=2:95435, m1=80:44706, m2=36:12875, y=116:12732)
- Layer 38: `}<?`, `osit`, `不加`, `Hakutulos`, `11` (target ranks: p1=20:4214, p2=4:98547, p3=18:16228, p4=2:118066, m1=80:85869, m2=36:41057, y=116:33355)
- Layer 39: `}<?`, ` Twentieth`, `迷惑`, `opters`, `erer` (target ranks: p1=20:75, p2=4:116390, p3=18:61434, p4=2:121896, m1=80:82750, m2=36:101112, y=116:86643)
- Layer 40: `二十`, `20`, ` twenty`, `留存`, ` Twenty` (target ranks: p1=20:2, p2=4:52608, p3=18:11996, p4=2:74113, m1=80:48329, m2=36:50206, y=116:87000)
- Layer 41: ` .`, `20`, `转载请`, `二十`, `试一试` (target ranks: p1=20:2, p2=4:19534, p3=18:23495, p4=2:14259, m1=80:38910, m2=36:51866, y=116:52569)

### Filler position 16 (absolute token 748, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=20:125658, p2=4:128590, p3=18:126715, p4=2:128797, m1=80:126939, m2=36:125172, y=116:122257)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=20:11510, p2=4:4064, p3=18:10373, p4=2:4217, m1=80:13608, m2=36:11143, y=116:26687)
- Layer 20: `锁定`, `ait`, ` smile`, ` LS`, `cape` (target ranks: p1=20:4120, p2=4:533, p3=18:3525, p4=2:1064, m1=80:5108, m2=36:1934, y=116:24252)
- Layer 30: `交替`, `十八`, ` eighteen`, `acin`, ` Rig` (target ranks: p1=20:33630, p2=4:17771, p3=18:11, p4=2:41498, m1=80:40089, m2=36:527, y=116:103199)
- Layer 35: ` eighteen`, `十八`, ` XVIII`, ` eighteenth`, `18` (target ranks: p1=20:28706, p2=4:43859, p3=18:5, p4=2:66476, m1=80:7045, m2=36:11, y=116:37591)
- Layer 36: ` eighteen`, `十八`, `三十六`, `18`, ` XVIII` (target ranks: p1=20:24270, p2=4:29047, p3=18:4, p4=2:31865, m1=80:3764, m2=36:8, y=116:18315)
- Layer 37: `十八`, ` eighteen`, `18`, `第十八`, ` eighteenth` (target ranks: p1=20:40414, p2=4:40890, p3=18:3, p4=2:45135, m1=80:9576, m2=36:17, y=116:20446)
- Layer 38: `18`, `十八`, ` eighteen`, `第十八`, ` eighteenth` (target ranks: p1=20:28333, p2=4:29534, p3=18:1, p4=2:34180, m1=80:8111, m2=36:9, y=116:27330)
- Layer 39: `}<?`, `东海`, `?datasetId`, `-ulo`, `gon` (target ranks: p1=20:18013, p2=4:84594, p3=18:18696, p4=2:82656, m1=80:22172, m2=36:7432, y=116:66220)
- Layer 40: `}<?`, `伺候`, ` twenty`, ` incon`, ` eighty` (target ranks: p1=20:2361, p2=4:27795, p3=18:18740, p4=2:30565, m1=80:7368, m2=36:7072, y=116:40194)
- Layer 41: ` .`, `�`, `因为`, ` because`, `随便` (target ranks: p1=20:6930, p2=4:23100, p3=18:51154, p4=2:12440, m1=80:31424, m2=36:28491, y=116:35314)

### Filler position 17 (absolute token 749, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125435, p2=4:128531, p3=18:126546, p4=2:128748, m1=80:126727, m2=36:124990, y=116:121843)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=20:12255, p2=4:5029, p3=18:11176, p4=2:4945, m1=80:15187, m2=36:12810, y=116:30599)
- Layer 20: ` smile`, `锁定`, `cape`, `ession`, `幽` (target ranks: p1=20:3034, p2=4:1440, p3=18:2343, p4=2:1699, m1=80:4535, m2=36:3620, y=116:21456)
- Layer 30: `翻`, `柿子`, ` Closure`, ` Imp`, ` closure` (target ranks: p1=20:29705, p2=4:19981, p3=18:17713, p4=2:8419, m1=80:45126, m2=36:11270, y=116:29043)
- Layer 35: ` transl`, `adic`, `翻`, ` closure`, `�` (target ranks: p1=20:10694, p2=4:2216, p3=18:8543, p4=2:6489, m1=80:8239, m2=36:12623, y=116:3562)
- Layer 36: `翻`, `�`, ` transl`, `翻了`, `itore` (target ranks: p1=20:11553, p2=4:10916, p3=18:37834, p4=2:14116, m1=80:19577, m2=36:26809, y=116:5754)
- Layer 37: `}<?`, `cault`, `olat`, ` Duc`, `زياح` (target ranks: p1=20:40260, p2=4:41080, p3=18:76825, p4=2:38284, m1=80:37935, m2=36:67509, y=116:10201)
- Layer 38: `}<?`, `cault`, `为人`, ` Lit`, ` polishing` (target ranks: p1=20:18021, p2=4:40018, p3=18:28192, p4=2:24988, m1=80:23402, m2=36:28456, y=116:10857)
- Layer 39: `}<?`, `-ulo`, `内膜`, `cault`, ` Zel` (target ranks: p1=20:35595, p2=4:93008, p3=18:72939, p4=2:112669, m1=80:2519, m2=36:26351, y=116:1364)
- Layer 40: ` .`, ` eighty`, ` seventy`, ` concaten`, ` udalerria` (target ranks: p1=20:22921, p2=4:35774, p3=18:61765, p4=2:74094, m1=80:927, m2=36:24002, y=116:388)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `况且`, ` ` (target ranks: p1=20:23101, p2=4:21842, p3=18:30484, p4=2:18919, m1=80:3938, m2=36:29191, y=116:947)

### Filler position 18 (absolute token 750, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=20:125451, p2=4:128550, p3=18:126572, p4=2:128751, m1=80:126789, m2=36:124954, y=116:122109)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=20:10631, p2=4:3787, p3=18:9678, p4=2:3769, m1=80:13209, m2=36:10668, y=116:27784)
- Layer 20: `锁定`, `ait`, ` smile`, `忑`, ` Walker` (target ranks: p1=20:4841, p2=4:1613, p3=18:5351, p4=2:2139, m1=80:7488, m2=36:3613, y=116:31953)
- Layer 30: `atan`, `obin`, `柿子`, `希望能够`, ` ternary` (target ranks: p1=20:7382, p2=4:10319, p3=18:439, p4=2:8470, m1=80:24540, m2=36:975, y=116:66644)
- Layer 35: ` eighteen`, `obin`, `18`, `十八`, ` Wil` (target ranks: p1=20:5022, p2=4:3021, p3=18:3, p4=2:81, m1=80:12266, m2=36:27, y=116:38432)
- Layer 36: `翻`, ` eighteen`, `十八`, `18`, `radesh` (target ranks: p1=20:12626, p2=4:11454, p3=18:4, p4=2:119, m1=80:27864, m2=36:238, y=116:42107)
- Layer 37: `}<?`, ` doubled`, ` doubles`, `翻了`, `oxygen` (target ranks: p1=20:34749, p2=4:65820, p3=18:19, p4=2:125, m1=80:64668, m2=36:3913, y=116:77472)
- Layer 38: ` doubled`, `}<?`, `oxygen`, `otan`, ` doubling` (target ranks: p1=20:42264, p2=4:80404, p3=18:34, p4=2:313, m1=80:75739, m2=36:5967, y=116:83724)
- Layer 39: `}<?`, `ozygous`, `迷惑`, ` Nij`, `oxygen` (target ranks: p1=20:55996, p2=4:97304, p3=18:9224, p4=2:23404, m1=80:29067, m2=36:8877, y=116:22941)
- Layer 40: ` .`, `迷惑`, ` `, `}<?`, ` eighty` (target ranks: p1=20:13774, p2=4:39903, p3=18:2473, p4=2:2025, m1=80:7334, m2=36:1646, y=116:4827)
- Layer 41: ` .`, `那两个`, ` because`, ` `, ` ;` (target ranks: p1=20:10652, p2=4:14775, p3=18:1869, p4=2:716, m1=80:6044, m2=36:3284, y=116:2669)

### Filler position 19 (absolute token 751, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `Noiz` (target ranks: p1=20:125995, p2=4:128730, p3=18:127075, p4=2:128909, m1=80:127318, m2=36:125638, y=116:123066)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=20:9970, p2=4:3426, p3=18:9282, p4=2:3326, m1=80:12814, m2=36:10599, y=116:27332)
- Layer 20: `忑`, ` Walker`, `ait`, `锁定`, `会成为` (target ranks: p1=20:6115, p2=4:6075, p3=18:11314, p4=2:6775, m1=80:10094, m2=36:9719, y=116:43177)
- Layer 30: ` randomization`, ` randomized`, `随机`, `禀`, ` Randomized` (target ranks: p1=20:6632, p2=4:20880, p3=18:32543, p4=2:39525, m1=80:19854, m2=36:14042, y=116:87277)
- Layer 35: ` var`, ` repetition`, ` repetitions`, `输入的`, `重复` (target ranks: p1=20:1508, p2=4:5564, p3=18:9971, p4=2:9985, m1=80:6960, m2=36:3751, y=116:55675)
- Layer 36: `输入的`, ` var`, `反复`, `输入`, ` repetitions` (target ranks: p1=20:1499, p2=4:10687, p3=18:10214, p4=2:17726, m1=80:8477, m2=36:3858, y=116:44847)
- Layer 37: `}<?`, `变量的`, ` variables`, `variables`, ` concaten` (target ranks: p1=20:9036, p2=4:68669, p3=18:41088, p4=2:81027, m1=80:29489, m2=36:15880, y=116:70648)
- Layer 38: `}<?`, `变量的`, `variables`, ` variables`, ` vals` (target ranks: p1=20:24865, p2=4:90736, p3=18:54469, p4=2:106950, m1=80:50346, m2=36:31625, y=116:75652)
- Layer 39: `}<?`, `斐`, `?datasetId`, `acons`, `树叶` (target ranks: p1=20:46707, p2=4:118303, p3=18:78497, p4=2:116371, m1=80:92423, m2=36:66956, y=116:105276)
- Layer 40: ` talags`, ` .`, `okens`, ` repetitions`, ` filler` (target ranks: p1=20:7314, p2=4:59837, p3=18:18007, p4=2:48502, m1=80:68455, m2=36:16438, y=116:74042)
- Layer 41: ` .`, ` waiting`, `外商投资`, `ldots`, ` ` (target ranks: p1=20:9654, p2=4:26467, p3=18:13428, p4=2:8615, m1=80:63659, m2=36:18044, y=116:57624)

### Filler position 20 (absolute token 752, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=20:126193, p2=4:128782, p3=18:127205, p4=2:128951, m1=80:127488, m2=36:125870, y=116:123122)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=20:10875, p2=4:3873, p3=18:10028, p4=2:3854, m1=80:12933, m2=36:11500, y=116:26920)
- Layer 20: `ait`, ` Walker`, `平行`, `会成为`, ` engaging` (target ranks: p1=20:10254, p2=4:11511, p3=18:18783, p4=2:11509, m1=80:14363, m2=36:19022, y=116:55523)
- Layer 30: `清楚楚`, `算出`, `第一步`, `+p`, ` step` (target ranks: p1=20:11586, p2=4:20859, p3=18:13350, p4=2:37512, m1=80:25037, m2=36:16336, y=116:46405)
- Layer 35: ` calculator`, `清楚楚`, `分解`, ` tap`, ` p` (target ranks: p1=20:2590, p2=4:9326, p3=18:4871, p4=2:14745, m1=80:6183, m2=36:5753, y=116:30881)
- Layer 36: `清楚楚`, `calcul`, `分解`, `俯`, ` tap` (target ranks: p1=20:2463, p2=4:15464, p3=18:4964, p4=2:24994, m1=80:6887, m2=36:6742, y=116:20776)
- Layer 37: ` p`, `calcul`, `俯`, `进行计算`, `清楚楚` (target ranks: p1=20:3086, p2=4:72714, p3=18:14657, p4=2:77717, m1=80:14954, m2=36:28331, y=116:35090)
- Layer 38: ` p`, `p`, `calcul`, `进行计算`, `zp` (target ranks: p1=20:4215, p2=4:85252, p3=18:17992, p4=2:92315, m1=80:23496, m2=36:25208, y=116:42557)
- Layer 39: ` p`, `p`, `}<?`, `迷惑`, ` Pell` (target ranks: p1=20:4941, p2=4:105210, p3=18:33078, p4=2:100630, m1=80:32262, m2=36:46926, y=116:65905)
- Layer 40: ` p`, `p`, ` twenty`, `y`, `坏的` (target ranks: p1=20:781, p2=4:64728, p3=18:11426, p4=2:59983, m1=80:31422, m2=36:28858, y=116:52504)
- Layer 41: ` .`, ` `, ` Calculators`, `外商投资`, `那两个` (target ranks: p1=20:839, p2=4:26155, p3=18:12652, p4=2:12030, m1=80:30606, m2=36:34049, y=116:29275)

### Filler position 21 (absolute token 753, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `-ulo`, `aplenty` (target ranks: p1=20:126478, p2=4:128889, p3=18:127557, p4=2:129057, m1=80:127857, m2=36:126255, y=116:124233)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=20:10524, p2=4:3719, p3=18:9447, p4=2:3690, m1=80:12387, m2=36:11387, y=116:27073)
- Layer 20: `俯`, ` TA`, ` biotic`, `ait`, `corpor` (target ranks: p1=20:8858, p2=4:35758, p3=18:36630, p4=2:35584, m1=80:36410, m2=36:47968, y=116:67400)
- Layer 30: `}using`, `dividers`, `}<?`, ` spac`, `acos` (target ranks: p1=20:35292, p2=4:114814, p3=18:74644, p4=2:124620, m1=80:89239, m2=36:53491, y=116:94201)
- Layer 35: `二十二`, `}using`, `二十三`, ` twenty`, `dividers` (target ranks: p1=20:7478, p2=4:103095, p3=18:28459, p4=2:95719, m1=80:91705, m2=36:11895, y=116:66756)
- Layer 36: `陌生`, `反复`, `俯`, `足足`, `滴水` (target ranks: p1=20:2501, p2=4:46667, p3=18:7646, p4=2:29744, m1=80:52508, m2=36:3243, y=116:40930)
- Layer 37: `}<?`, `坏`, `onana`, ` covari`, `合并` (target ranks: p1=20:19584, p2=4:86764, p3=18:42809, p4=2:83245, m1=80:78726, m2=36:15972, y=116:54005)
- Layer 38: ` .`, ` covari`, ` club`, `坏`, ` .↵↵` (target ranks: p1=20:5105, p2=4:63390, p3=18:10136, p4=2:73276, m1=80:55082, m2=36:3733, y=116:64318)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, `坏`, ` covari`, ` .↵↵` (target ranks: p1=20:29487, p2=4:103363, p3=18:57047, p4=2:96933, m1=80:91468, m2=36:22062, y=116:105275)
- Layer 40: ` .`, ` .↵↵`, `<｜begin▁of▁sentence｜>`, ` .↵`, `坏` (target ranks: p1=20:12350, p2=4:60368, p3=18:23451, p4=2:36439, m1=80:72169, m2=36:7584, y=116:85215)
- Layer 41: ` .`, ` .↵↵`, `这就是`, ` .↵`, `坏` (target ranks: p1=20:5439, p2=4:8295, p3=18:6370, p4=2:2532, m1=80:45383, m2=36:3602, y=116:43614)

### Filler position 22 (absolute token 754, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=20:126489, p2=4:128901, p3=18:127558, p4=2:129060, m1=80:127842, m2=36:126286, y=116:124102)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: p1=20:10152, p2=4:3332, p3=18:8739, p4=2:3385, m1=80:11863, m2=36:10482, y=116:26458)
- Layer 20: ` quadr`, `cape`, `同步`, ` smile`, `ait` (target ranks: p1=20:210, p2=4:89, p3=18:636, p4=2:220, m1=80:447, m2=36:311, y=116:15784)
- Layer 30: `东京`, `陪`, ` Conc`, `Quintal`, ` doubling` (target ranks: p1=20:11088, p2=4:38405, p3=18:30578, p4=2:54138, m1=80:19867, m2=36:7653, y=116:41880)
- Layer 35: `otechnical`, `技法`, `04`, ` Gikuha`, `竖直` (target ranks: p1=20:18810, p2=4:5418, p3=18:5555, p4=2:97123, m1=80:7944, m2=36:9774, y=116:29716)
- Layer 36: ` Gikuha`, `24`, `东京`, `竖直`, `84` (target ranks: p1=20:6857, p2=4:12185, p3=18:6446, p4=2:97858, m1=80:14781, m2=36:3351, y=116:3220)
- Layer 37: `东京`, ` Gikuha`, `codeline`, `)Skip`, ` Holid` (target ranks: p1=20:16772, p2=4:18554, p3=18:15118, p4=2:97861, m1=80:14514, m2=36:6915, y=116:1787)
- Layer 38: `二十四`, `24`, `cault`, `兄弟`, `姊妹` (target ranks: p1=20:18125, p2=4:15194, p3=18:4562, p4=2:104498, m1=80:36501, m2=36:2101, y=116:2965)
- Layer 39: `84`, `124`, `二十四`, `cault`, ` eighty` (target ranks: p1=20:51448, p2=4:92077, p3=18:23456, p4=2:117049, m1=80:2899, m2=36:1006, y=116:253)
- Layer 40: `84`, `二十四`, ` eighty`, ` seventy`, `发声` (target ranks: p1=20:40987, p2=4:55650, p3=18:16043, p4=2:101651, m1=80:2820, m2=36:1522, y=116:429)
- Layer 41: ` .`, `错过`, ` .↵↵`, `错过了`, `放过` (target ranks: p1=20:14426, p2=4:19694, p3=18:4877, p4=2:17368, m1=80:9626, m2=36:2667, y=116:2022)

### Filler position 23 (absolute token 755, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=20:126390, p2=4:128869, p3=18:127456, p4=2:129029, m1=80:127754, m2=36:126127, y=116:123924)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=20:9540, p2=4:3054, p3=18:8341, p4=2:2981, m1=80:11480, m2=36:10175, y=116:26953)
- Layer 20: `Dutch`, `)Skip`, ` Dutch`, `吞`, `tered` (target ranks: p1=20:7659, p2=4:8642, p3=18:8354, p4=2:18279, m1=80:14599, m2=36:20803, y=116:51490)
- Layer 30: `codeline`, `东京`, `)Skip`, `okens`, `东海` (target ranks: p1=20:54858, p2=4:87564, p3=18:52031, p4=2:115199, m1=80:62820, m2=36:78771, y=116:117777)
- Layer 35: `codeline`, `坏`, `删`, ` germ`, ` fif` (target ranks: p1=20:33314, p2=4:81208, p3=18:37773, p4=2:107444, m1=80:35213, m2=36:56294, y=116:125134)
- Layer 36: `坏`, `停`, `/hess`, ` soci`, `告诉我们` (target ranks: p1=20:31367, p2=4:43032, p3=18:18861, p4=2:66255, m1=80:12428, m2=36:24482, y=116:101091)
- Layer 37: `镶嵌`, `肤`, ` tide`, `贻`, `itore` (target ranks: p1=20:61330, p2=4:56488, p3=18:45873, p4=2:85041, m1=80:48836, m2=36:57422, y=116:101367)
- Layer 38: `肤`, `锚`, ` germ`, `镶嵌`, `itore` (target ranks: p1=20:40912, p2=4:41182, p3=18:29704, p4=2:68006, m1=80:50862, m2=36:19971, y=116:42500)
- Layer 39: ` encomp`, `肤`, ` .`, ` germ`, ` unflagged` (target ranks: p1=20:71696, p2=4:111903, p3=18:73399, p4=2:105051, m1=80:100206, m2=36:72356, y=116:76776)
- Layer 40: ` .`, ` .↵↵`, `肤`, ` .↵`, `镶嵌` (target ranks: p1=20:57019, p2=4:87434, p3=18:42774, p4=2:71237, m1=80:97822, m2=36:51928, y=116:74445)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `一个个` (target ranks: p1=20:19111, p2=4:55995, p3=18:20006, p4=2:41041, m1=80:53934, m2=36:27168, y=116:35217)

### Filler position 24 (absolute token 756, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `-ulo` (target ranks: p1=20:126583, p2=4:128949, p3=18:127678, p4=2:129096, m1=80:127999, m2=36:126361, y=116:124618)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: p1=20:9337, p2=4:2931, p3=18:8393, p4=2:2892, m1=80:11237, m2=36:9492, y=116:25865)
- Layer 20: ` smile`, `cape`, `站`, `足`, ` grin` (target ranks: p1=20:1204, p2=4:57, p3=18:888, p4=2:766, m1=80:1177, m2=36:359, y=116:20572)
- Layer 30: `codeline`, `</think>`, ` Answer`, `oNames`, `答案是` (target ranks: p1=20:93438, p2=4:111403, p3=18:104528, p4=2:127067, m1=80:117424, m2=36:100244, y=116:126995)
- Layer 35: `codeline`, ` Answer`, `AED`, ` tagged`, ` nasod` (target ranks: p1=20:54647, p2=4:88363, p3=18:85859, p4=2:102852, m1=80:70518, m2=36:96363, y=116:126671)
- Layer 36: ` nasod`, ` Answer`, `良`, `codeline`, `坏` (target ranks: p1=20:14580, p2=4:33624, p3=18:21515, p4=2:39170, m1=80:16543, m2=36:34159, y=116:110723)
- Layer 37: `codeline`, `hatic`, `oNames`, `�`, `本题分析` (target ranks: p1=20:83700, p2=4:109254, p3=18:90254, p4=2:103968, m1=80:93326, m2=36:117116, y=116:102349)
- Layer 38: `codeline`, `hatic`, `oNames`, `okens`, `�` (target ranks: p1=20:74902, p2=4:109782, p3=18:88172, p4=2:103355, m1=80:68361, m2=36:101470, y=116:58548)
- Layer 39: `hatic`, `codeline`, `-ulo`, ` begg`, ` Fusion` (target ranks: p1=20:41532, p2=4:109597, p3=18:68548, p4=2:89555, m1=80:70961, m2=36:49441, y=116:65210)
- Layer 40: ` Answer`, `Answer`, ` .↵↵`, ` .`, ` unflagged` (target ranks: p1=20:3999, p2=4:29239, p3=18:12282, p4=2:16623, m1=80:14365, m2=36:6612, y=116:30506)
- Layer 41: ` .`, ` Answer`, ` .↵↵`, `Answer`, ` .↵` (target ranks: p1=20:1168, p2=4:6587, p3=18:3467, p4=2:2461, m1=80:7889, m2=36:4126, y=116:19695)

### Filler position 25 (absolute token 757, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `EDMF` (target ranks: p1=20:120978, p2=4:126623, p3=18:121822, p4=2:126656, m1=80:121032, m2=36:121591, y=116:108474)
- Layer 10: `tas`, `eine`, `ej`, `cookie`, `Achie` (target ranks: p1=20:31164, p2=4:36766, p3=18:49165, p4=2:29767, m1=80:53871, m2=36:61116, y=116:31092)
- Layer 20: ` Submission`, `鸯`, `ait`, `能被`, `平行` (target ranks: p1=20:9200, p2=4:17421, p3=18:25013, p4=2:32321, m1=80:18591, m2=36:21130, y=116:79847)
- Layer 30: ` Paglin`, `malink`, `堂`, ` الجرم`, `Quintal` (target ranks: p1=20:10617, p2=4:110383, p3=18:78897, p4=2:121285, m1=80:51495, m2=36:17351, y=116:37361)
- Layer 35: `CopyWith`, ` Paglin`, ` dekameters`, `堂`, `四十` (target ranks: p1=20:7312, p2=4:107952, p3=18:90240, p4=2:124503, m1=80:222, m2=36:8103, y=116:15912)
- Layer 36: ` Paglin`, `堂`, `捧`, `romes`, `白马` (target ranks: p1=20:14623, p2=4:81090, p3=18:110424, p4=2:108126, m1=80:54, m2=36:13473, y=116:357)
- Layer 37: ` Paglin`, `romes`, `/Tropical`, `EDMF`, `-ulo` (target ranks: p1=20:63259, p2=4:115456, p3=18:121544, p4=2:124409, m1=80:3667, m2=36:72523, y=116:4208)
- Layer 38: ` Paglin`, `romes`, `EDMF`, `-ulo`, ` dekameters` (target ranks: p1=20:96411, p2=4:113191, p3=18:127156, p4=2:125848, m1=80:17859, m2=36:104201, y=116:14753)
- Layer 39: ` Answer`, ` Antwort`, ` answer`, `答案`, `Answer` (target ranks: p1=20:102208, p2=4:114345, p3=18:108290, p4=2:120906, m1=80:22298, m2=36:87114, y=116:5386)
- Layer 40: ` Answer`, `Answer`, ` answer`, `回答`, `_answer` (target ranks: p1=20:48772, p2=4:59970, p3=18:44768, p4=2:70373, m1=80:2060, m2=36:15199, y=116:254)
- Layer 41: `Answer`, ` Answer`, ` answer`, `回答`, `answer` (target ranks: p1=20:3244, p2=4:1756, p3=18:2493, p4=2:1780, m1=80:561, m2=36:6559, y=116:141)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given integer inputs followed by a straight-line arithmetic program. Execute the assignments exactly in the order shown. Answer immediately with just the queried integer, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 25 filler tokens (a sequence of dots) before you answer.<｜User｜>a = 4
b = 3
c = 12
d = 4
e = 11
f = 11
g = 12
h = 10
p1 = a + b
p2 = c - d
p3 = e + f
p4 = g - h
m1 = p1 * p2
m2 = p3 * p4
y = m1 + m2
Question: What is the value of y?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>100<｜end▁of▁sentence｜><｜User｜>x0 = 6
a = 6
b = 3
c = 9
d = 6
e = 3
f = 5
g = 7
x1 = x0 + a
x2 = x1 * b
x3 = x2 - c
x4 = x3 + d
x5 = x4 * e
x6 = x5 - f
y = x6 + g
Question: What is the value of y?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>101<｜end▁of▁sentence｜><｜User｜>a = 11
b = 6
c = 10
d = 8
e = 10
f = 6
g = 11
h = 6
p1 = a + b
p2 = c - d
p3 = e + f
p4 = g - h
m1 = p1 * p2
m2 = p3 * p4
y = m1 + m2
Question: What is the value of y?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>114<｜end▁of▁sentence｜><｜User｜>x0 = 9
a = 6
b = 2
c = 6
d = 3
e = 3
f = 8
g = 7
x1 = x0 + a
x2 = x1 * b
x3 = x2 - c
x4 = x3 + d
x5 = x4 * e
x6 = x5 - f
y = x6 + g
Question: What is the value of y?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>80<｜end▁of▁sentence｜><｜User｜>a = 11
b = 9
c = 9
d = 5
e = 7
f = 11
g = 11
h = 9
p1 = a + b
p2 = c - d
p3 = e + f
p4 = g - h
m1 = p1 * p2
m2 = p3 * p4
y = m1 + m2
Question: What is the value of y?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
