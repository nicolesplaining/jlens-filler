# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `165` (correct).
- No-filler answer: `165` (correct).
- Filler tokens: 25 tokens at absolute indices 733–757.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `p1=21` | 1 (L37, filler 15) | L35, filler 15 (rank 6) |
| J-Lens | `p2=5` | 114 (L20, filler 22) | Never |
| J-Lens | `p3=20` | 107 (L20, filler 22) | Never |
| J-Lens | `p4=3` | 9 (L30, filler 16) | L30, filler 16 (rank 9) |
| J-Lens | `m1=105` | 6 (L36, filler 25) | L36, filler 25 (rank 6) |
| J-Lens | `m2=60` | 1 (L35, filler 9) | L35, filler 9 (rank 1) |
| J-Lens | `y=165` | 35 (L37, filler 4) | Never |
| Logit lens | `p1=21` | 2 (L39, filler 15) | L32, filler 7 (rank 7) |
| Logit lens | `p2=5` | 48 (L31, filler 9) | Never |
| Logit lens | `p3=20` | 2 (L32, filler 9) | L31, filler 9 (rank 7) |
| Logit lens | `p4=3` | 1 (L29, filler 16) | L29, filler 11 (rank 8) |
| Logit lens | `m1=105` | 7 (L32, filler 25) | L32, filler 25 (rank 7) |
| Logit lens | `m2=60` | 1 (L34, filler 9) | L32, filler 9 (rank 5) |
| Logit lens | `y=165` | 32 (L39, filler 7) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 733, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: p1=21:121718, p2=5:126003, p3=20:119776, p4=3:126119, m1=105:113166, m2=60:119975, y=165:116076)
- Layer 10: `忑`, `anta`, `fine`, ` Walker`, `locked` (target ranks: p1=21:32860, p2=5:19383, p3=20:28903, p4=3:20626, m1=105:38425, m2=60:28338, y=165:38181)
- Layer 20: ` .`, `/.`, `dots`, ` dots`, `Dot` (target ranks: p1=21:27409, p2=5:3497, p3=20:6124, p4=3:12545, m1=105:69663, m2=60:22378, y=165:96446)
- Layer 30: ` pakig`, ` talags`, `回答`, `期望`, `tap` (target ranks: p1=21:48150, p2=5:12349, p3=20:14210, p4=3:39582, m1=105:33435, m2=60:16222, y=165:74819)
- Layer 35: `oooo`, `应答`, `垂`, ` tap`, `私` (target ranks: p1=21:17515, p2=5:5889, p3=20:1696, p4=3:16334, m1=105:7630, m2=60:490, y=165:32520)
- Layer 36: ` talags`, `期望`, `oooo`, `私`, ` Tap` (target ranks: p1=21:16458, p2=5:8099, p3=20:2650, p4=3:19532, m1=105:2962, m2=60:919, y=165:26143)
- Layer 37: ` talags`, ` pakig`, `}<?`, `ِّف`, `在北京` (target ranks: p1=21:87408, p2=5:107225, p3=20:71752, p4=3:117915, m1=105:32953, m2=60:36574, y=165:64255)
- Layer 38: ` talags`, ` pakig`, `}<?`, `ِّف`, `在北京` (target ranks: p1=21:108726, p2=5:109886, p3=20:100987, p4=3:119778, m1=105:25704, m2=60:58813, y=165:65835)
- Layer 39: ` talags`, `}<?`, ` pakig`, ` +:+`, ` hilabihan` (target ranks: p1=21:122487, p2=5:112557, p3=20:119371, p4=3:124419, m1=105:56977, m2=60:122048, y=165:95116)
- Layer 40: ` .`, ` talags`, `dots`, ` nasod`, ` dots` (target ranks: p1=21:93146, p2=5:36488, p3=20:95603, p4=3:76617, m1=105:7464, m2=60:105808, y=165:50287)
- Layer 41: ` .`, ` .↵↵`, `我没有`, ` .↵`, `一个一个` (target ranks: p1=21:96861, p2=5:15017, p3=20:100349, p4=3:52445, m1=105:12135, m2=60:99621, y=165:31240)

### Filler position 2 (absolute token 734, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `-ulo`, `�乐` (target ranks: p1=21:123118, p2=5:125933, p3=20:121415, p4=3:125999, m1=105:118816, m2=60:122768, y=165:119568)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: p1=21:15437, p2=5:4773, p3=20:16127, p4=3:4174, m1=105:32060, m2=60:16848, y=165:25075)
- Layer 20: ` .----`, `往常`, ` .`, `ools`, `ologists` (target ranks: p1=21:117146, p2=5:107138, p3=20:100862, p4=3:103922, m1=105:121065, m2=60:112366, y=165:120572)
- Layer 30: ` pakig`, ` hilabihan`, ` gilay`, ` talags`, ` dekameters` (target ranks: p1=21:96784, p2=5:106484, p3=20:70733, p4=3:114716, m1=105:107689, m2=60:120030, y=165:110627)
- Layer 35: ` .`, ` hilabihan`, `enclose`, ` silic`, ` pakig` (target ranks: p1=21:61018, p2=5:98475, p3=20:56184, p4=3:111686, m1=105:113275, m2=60:123955, y=165:125594)
- Layer 36: `停`, `enclose`, ` nasod`, ` .`, `空空` (target ranks: p1=21:28349, p2=5:45018, p3=20:28675, p4=3:65315, m1=105:67781, m2=60:98643, y=165:108496)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, ` Erkännande`, `TreeLabel` (target ranks: p1=21:107392, p2=5:124475, p3=20:107262, p4=3:125965, m1=105:115819, m2=60:123805, y=165:122199)
- Layer 38: ` .`, `}<?`, ` hilabihan`, `繁体`, `�乐` (target ranks: p1=21:58490, p2=5:115161, p3=20:71226, p4=3:121370, m1=105:71346, m2=60:117983, y=165:94676)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` nasod`, ` .↵↵`, ` hilabihan` (target ranks: p1=21:76068, p2=5:105926, p3=20:89125, p4=3:119969, m1=105:42381, m2=60:117338, y=165:63765)
- Layer 40: ` .`, ` nasod`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵` (target ranks: p1=21:19871, p2=5:43178, p3=20:40755, p4=3:68076, m1=105:10111, m2=60:99867, y=165:20360)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `中书`, ` ,` (target ranks: p1=21:10946, p2=5:5122, p3=20:25977, p4=3:8129, m1=105:5046, m2=60:70342, y=165:4333)

### Filler position 3 (absolute token 735, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126078, p2=5:128030, p3=20:124927, p4=3:128105, m1=105:122421, m2=60:126263, y=165:122205)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, `忑` (target ranks: p1=21:9780, p2=5:4095, p3=20:11939, p4=3:3893, m1=105:23618, m2=60:12816, y=165:21102)
- Layer 20: `ait`, `忑`, `能被`, `锁定`, `cape` (target ranks: p1=21:4623, p2=5:2384, p3=20:9945, p4=3:1259, m1=105:18345, m2=60:12044, y=165:24990)
- Layer 30: ` repetitions`, ` repetition`, `Tap`, `esper`, `重复` (target ranks: p1=21:5429, p2=5:6782, p3=20:14059, p4=3:15393, m1=105:12772, m2=60:58013, y=165:39466)
- Layer 35: ` repetitions`, ` arithmetic`, ` repetition`, `重复`, `acks` (target ranks: p1=21:1688, p2=5:4946, p3=20:7477, p4=3:11861, m1=105:6674, m2=60:25338, y=165:33347)
- Layer 36: ` repeated`, ` repetitions`, ` repetition`, `sequential`, `重复` (target ranks: p1=21:3733, p2=5:8303, p3=20:11644, p4=3:14992, m1=105:4930, m2=60:28622, y=165:35892)
- Layer 37: ` arithmetic`, `ithmetic`, `arithm`, `sequences`, `打磨` (target ranks: p1=21:16990, p2=5:52225, p3=20:45769, p4=3:65505, m1=105:16407, m2=60:80264, y=165:73964)
- Layer 38: `}<?`, `打磨`, ` arithmetic`, `本题分析`, `模拟` (target ranks: p1=21:41323, p2=5:91054, p3=20:65255, p4=3:100494, m1=105:29881, m2=60:90884, y=165:93654)
- Layer 39: `}<?`, `本题分析`, `�`, ` Rutherford`, `hatic` (target ranks: p1=21:90543, p2=5:117324, p3=20:110019, p4=3:119188, m1=105:57273, m2=60:125365, y=165:99027)
- Layer 40: `程序的`, `幻觉`, ` talags`, `程序`, ` filler` (target ranks: p1=21:42544, p2=5:65715, p3=20:68673, p4=3:65891, m1=105:21836, m2=60:119547, y=165:67330)
- Layer 41: ` .`, `试一试`, `程序`, ` without`, ` ,` (target ranks: p1=21:17131, p2=5:14142, p3=20:28429, p4=3:16369, m1=105:17168, m2=60:112905, y=165:31805)

### Filler position 4 (absolute token 736, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126879, p2=5:128433, p3=20:125750, p4=3:128474, m1=105:123264, m2=60:126793, y=165:122884)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=21:9266, p2=5:3378, p3=20:11282, p4=3:3225, m1=105:21980, m2=60:11442, y=165:18596)
- Layer 20: `ait`, `cape`, ` LS`, ` quadr`, `ative` (target ranks: p1=21:3193, p2=5:267, p3=20:5562, p4=3:729, m1=105:22586, m2=60:6634, y=165:21537)
- Layer 30: `Subt`, ` consum`, `subt`, `acos`, `上市` (target ranks: p1=21:6434, p2=5:5493, p3=20:15386, p4=3:7004, m1=105:17691, m2=60:10479, y=165:48533)
- Layer 35: `apon`, ` Nil`, `Nil`, `垂`, ` ternary` (target ranks: p1=21:9561, p2=5:38077, p3=20:47631, p4=3:33214, m1=105:1269, m2=60:1958, y=165:18863)
- Layer 36: `}<?`, `135`, `115`, ` dátummal`, `白玉` (target ranks: p1=21:111953, p2=5:98046, p3=20:117332, p4=3:73072, m1=105:83, m2=60:4160, y=165:302)
- Layer 37: `/Tropical`, `115`, `}<?`, `135`, `153` (target ranks: p1=21:117895, p2=5:94244, p3=20:118185, p4=3:64307, m1=105:111, m2=60:11083, y=165:35)
- Layer 38: `}<?`, `/Tropical`, ` premi`, `灵力`, ` dekameters` (target ranks: p1=21:96180, p2=5:106689, p3=20:117614, p4=3:102347, m1=105:422, m2=60:11514, y=165:347)
- Layer 39: `}<?`, `/Tropical`, ` Nij`, `135`, `141` (target ranks: p1=21:98541, p2=5:119478, p3=20:123695, p4=3:111293, m1=105:1086, m2=60:49947, y=165:193)
- Layer 40: `135`, `}<?`, ` dekameters`, `<｜place▁holder▁no▁694｜>`, `ржа` (target ranks: p1=21:59971, p2=5:89762, p3=20:122023, p4=3:61287, m1=105:77, m2=60:29910, y=165:53)
- Layer 41: ` loses`, `错过了`, `走出了`, ` dekameters`, ` begun` (target ranks: p1=21:18157, p2=5:16108, p3=20:64964, p4=3:13124, m1=105:1579, m2=60:29602, y=165:382)

### Filler position 5 (absolute token 737, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126613, p2=5:128361, p3=20:125496, p4=3:128394, m1=105:122558, m2=60:126235, y=165:122463)
- Layer 10: ` Walker`, `锁定`, `挪`, `Walker`, `ait` (target ranks: p1=21:9633, p2=5:3941, p3=20:11777, p4=3:3841, m1=105:22179, m2=60:12065, y=165:20024)
- Layer 20: `幽`, `锁定`, ` LS`, `鞍`, `而此时` (target ranks: p1=21:7430, p2=5:1590, p3=20:11571, p4=3:2904, m1=105:22567, m2=60:13010, y=165:18971)
- Layer 30: `�`, `acos`, `鞍`, `selling`, `wap` (target ranks: p1=21:41167, p2=5:10693, p3=20:62247, p4=3:37787, m1=105:76074, m2=60:51642, y=165:87452)
- Layer 35: `�`, `羊`, ` Xi`, ` var`, `Tap` (target ranks: p1=21:15438, p2=5:1612, p3=20:31828, p4=3:14047, m1=105:43659, m2=60:43313, y=165:66436)
- Layer 36: `berg`, ` talags`, `bergh`, ` start`, `羊` (target ranks: p1=21:30073, p2=5:5652, p3=20:52408, p4=3:35386, m1=105:20717, m2=60:64355, y=165:55685)
- Layer 37: ` talags`, `坏`, `acos`, `轨迹`, `itore` (target ranks: p1=21:53783, p2=5:26944, p3=20:94311, p4=3:76484, m1=105:45772, m2=60:108444, y=165:92636)
- Layer 38: ` talags`, `hemer`, `}<?`, `坏`, `�` (target ranks: p1=21:73107, p2=5:50928, p3=20:115641, p4=3:95126, m1=105:69989, m2=60:122783, y=165:109440)
- Layer 39: ` talags`, `hemer`, `�`, `}<?`, `迷惑` (target ranks: p1=21:95731, p2=5:103936, p3=20:114218, p4=3:111231, m1=105:94877, m2=60:126837, y=165:110010)
- Layer 40: ` talags`, ` nasod`, `坏`, `тельными`, `冰冰` (target ranks: p1=21:51178, p2=5:55665, p3=20:91371, p4=3:64729, m1=105:59082, m2=60:124766, y=165:83368)
- Layer 41: ` .`, `坏`, `鹉`, `下面是`, `省略` (target ranks: p1=21:18206, p2=5:11457, p3=20:49520, p4=3:14189, m1=105:31378, m2=60:105281, y=165:29347)

### Filler position 6 (absolute token 738, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126612, p2=5:128359, p3=20:125481, p4=3:128403, m1=105:122810, m2=60:126251, y=165:122661)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=21:9748, p2=5:3967, p3=20:11447, p4=3:3836, m1=105:22072, m2=60:11929, y=165:18823)
- Layer 20: `试一试`, ` combinator`, `答案`, ` answer`, `试试` (target ranks: p1=21:62287, p2=5:38240, p3=20:49385, p4=3:43868, m1=105:81704, m2=60:86220, y=165:72504)
- Layer 30: `推算`, `算出`, `高明`, ` calculating`, ` calculator` (target ranks: p1=21:2884, p2=5:6103, p3=20:13476, p4=3:6849, m1=105:19237, m2=60:12731, y=165:59851)
- Layer 35: ` step`, `高明`, ` Step`, ` lab`, `acks` (target ranks: p1=21:3232, p2=5:11398, p3=20:8606, p4=3:16531, m1=105:18152, m2=60:10037, y=165:57670)
- Layer 36: ` step`, ` Step`, ` pakig`, `calcul`, `推算` (target ranks: p1=21:5889, p2=5:15832, p3=20:10637, p4=3:21230, m1=105:6852, m2=60:13966, y=165:48779)
- Layer 37: ` pakig`, ` step`, ` Step`, `高明`, ` passo` (target ranks: p1=21:19227, p2=5:69933, p3=20:37821, p4=3:84050, m1=105:28331, m2=60:42584, y=165:97554)
- Layer 38: ` pakig`, ` Step`, ` step`, ` Calculators`, ` ladder` (target ranks: p1=21:26015, p2=5:90757, p3=20:41207, p4=3:95189, m1=105:21607, m2=60:41839, y=165:104765)
- Layer 39: ` pakig`, `<｜begin▁of▁sentence｜>`, `}<?`, ` talags`, ` Rutherford` (target ranks: p1=21:81850, p2=5:117027, p3=20:95539, p4=3:119401, m1=105:117911, m2=60:127438, y=165:127699)
- Layer 40: ` pakig`, ` talags`, `<｜begin▁of▁sentence｜>`, ` x`, `试一试` (target ranks: p1=21:34436, p2=5:76868, p3=20:64540, p4=3:71212, m1=105:104850, m2=60:125564, y=165:124504)
- Layer 41: ` .`, `试一试`, `一个一个`, `外层`, ` .↵↵` (target ranks: p1=21:28293, p2=5:22865, p3=20:44286, p4=3:20814, m1=105:88644, m2=60:122660, y=165:111981)

### Filler position 7 (absolute token 739, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126453, p2=5:128321, p3=20:125322, p4=3:128335, m1=105:122484, m2=60:125934, y=165:122474)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=21:8788, p2=5:3443, p3=20:10519, p4=3:3258, m1=105:21159, m2=60:10843, y=165:18364)
- Layer 20: `锁定`, `ait`, ` cheer`, `鞍`, ` smile` (target ranks: p1=21:3364, p2=5:959, p3=20:5224, p4=3:990, m1=105:12153, m2=60:4719, y=165:10681)
- Layer 30: `69`, ` rhe`, `yg`, `Subt`, `54` (target ranks: p1=21:69, p2=5:7533, p3=20:4071, p4=3:5850, m1=105:71, m2=60:628, y=165:499)
- Layer 35: `189`, ` labor`, `69`, `369`, `75` (target ranks: p1=21:52, p2=5:6881, p3=20:48503, p4=3:2377, m1=105:31, m2=60:8528, y=165:162)
- Layer 36: `189`, `特异`, `黄花`, `159`, `117` (target ranks: p1=21:1744, p2=5:42005, p3=20:111292, p4=3:18558, m1=105:11, m2=60:29606, y=165:247)
- Layer 37: `?datasetId`, `189`, ` Nou`, `lisitry`, ` Frid` (target ranks: p1=21:10015, p2=5:75472, p3=20:118582, p4=3:47487, m1=105:113, m2=60:67624, y=165:190)
- Layer 38: `}<?`, `?datasetId`, ` Frid`, ` Nou`, ` Noruwega` (target ranks: p1=21:34787, p2=5:104410, p3=20:124075, p4=3:83390, m1=105:716, m2=60:97781, y=165:744)
- Layer 39: `}<?`, ` clam`, ` Nij`, ` Noruwega`, `叶子` (target ranks: p1=21:83160, p2=5:103948, p3=20:114596, p4=3:99372, m1=105:14844, m2=60:117498, y=165:938)
- Layer 40: ` outp`, ` drip`, ` clam`, ` fountain`, `135` (target ranks: p1=21:24002, p2=5:36657, p3=20:89013, p4=3:31804, m1=105:2714, m2=60:107072, y=165:94)
- Layer 41: ` .`, `\`, ` `, ` waterfall`, ` ,` (target ranks: p1=21:5762, p2=5:7059, p3=20:41288, p4=3:7128, m1=105:10878, m2=60:97823, y=165:501)

### Filler position 8 (absolute token 740, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126437, p2=5:128309, p3=20:125286, p4=3:128331, m1=105:122575, m2=60:125938, y=165:122622)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: p1=21:8890, p2=5:3589, p3=20:10632, p4=3:3377, m1=105:21493, m2=60:10770, y=165:18462)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, `胃癌` (target ranks: p1=21:4535, p2=5:1194, p3=20:5856, p4=3:1556, m1=105:24561, m2=60:8261, y=165:18265)
- Layer 30: `acos`, `acin`, `鞍`, ` irreducible`, `Tap` (target ranks: p1=21:29411, p2=5:9714, p3=20:26687, p4=3:34663, m1=105:64245, m2=60:43071, y=165:93367)
- Layer 35: ` met`, ` tap`, `特`, `acks`, ` stabil` (target ranks: p1=21:12053, p2=5:1753, p3=20:9466, p4=3:5495, m1=105:40947, m2=60:13277, y=165:64603)
- Layer 36: `特`, ` tap`, `adal`, `留存`, ` stabil` (target ranks: p1=21:7697, p2=5:2008, p3=20:7209, p4=3:5656, m1=105:14594, m2=60:11476, y=165:31999)
- Layer 37: `acos`, ` Zad`, `xs`, `特`, `pac` (target ranks: p1=21:30994, p2=5:18702, p3=20:24374, p4=3:40137, m1=105:27603, m2=60:41982, y=165:73397)
- Layer 38: ` Zad`, `}<?`, `pac`, `xs`, `acos` (target ranks: p1=21:48311, p2=5:31815, p3=20:55154, p4=3:57724, m1=105:33430, m2=60:65432, y=165:84837)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `替换`, `osos`, `𝑋` (target ranks: p1=21:40848, p2=5:74152, p3=20:54770, p4=3:85473, m1=105:61190, m2=60:107071, y=165:104961)
- Layer 40: ` x`, ` talags`, `留存`, ` nasod`, `x` (target ranks: p1=21:5090, p2=5:19790, p3=20:15870, p4=3:22646, m1=105:23704, m2=60:87678, y=165:55784)
- Layer 41: ` .`, `有下列`, `鹃`, `鹉`, `试一试` (target ranks: p1=21:3900, p2=5:5107, p3=20:11472, p4=3:8465, m1=105:29263, m2=60:75013, y=165:37016)

### Filler position 9 (absolute token 741, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126379, p2=5:128289, p3=20:125188, p4=3:128321, m1=105:122524, m2=60:125844, y=165:122665)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `挪` (target ranks: p1=21:8425, p2=5:3307, p3=20:10118, p4=3:3117, m1=105:20951, m2=60:10309, y=165:18054)
- Layer 20: `锁定`, `ait`, `能被`, ` cheer`, `cape` (target ranks: p1=21:2074, p2=5:666, p3=20:3913, p4=3:632, m1=105:12082, m2=60:5502, y=165:12479)
- Layer 30: `acos`, ` Ries`, ` pakig`, ` consuming`, `石榴` (target ranks: p1=21:3637, p2=5:2682, p3=20:2247, p4=3:4299, m1=105:25476, m2=60:4472, y=165:48377)
- Layer 35: `60`, `柿子`, ` labor`, `粥`, `期望` (target ranks: p1=21:12398, p2=5:4309, p3=20:136, p4=3:5148, m1=105:822, m2=60:1, y=165:12251)
- Layer 36: `60`, `六十`, `期望`, `柿子`, ` sixty` (target ranks: p1=21:102265, p2=5:15776, p3=20:5274, p4=3:20522, m1=105:285, m2=60:1, y=165:6266)
- Layer 37: `六十`, `60`, `}<?`, ` sixty`, `060` (target ranks: p1=21:114246, p2=5:36030, p3=20:5082, p4=3:35958, m1=105:1439, m2=60:2, y=165:4430)
- Layer 38: `六十`, `60`, `}<?`, `osit`, ` pakig` (target ranks: p1=21:109138, p2=5:44543, p3=20:30110, p4=3:56029, m1=105:1013, m2=60:2, y=165:4428)
- Layer 39: `}<?`, ` dekameters`, ` Nij`, `osos`, ` hectometers` (target ranks: p1=21:61601, p2=5:75960, p3=20:73661, p4=3:101170, m1=105:12855, m2=60:19602, y=165:16027)
- Layer 40: ` dekameters`, `}<?`, ` response`, `响应`, ` responses` (target ranks: p1=21:17381, p2=5:23160, p3=20:35871, p4=3:40906, m1=105:2442, m2=60:18707, y=165:2915)
- Layer 41: ` .`, ` begun`, ` .↵↵`, ` ...`, `况且` (target ranks: p1=21:11788, p2=5:3777, p3=20:13507, p4=3:16703, m1=105:3915, m2=60:29246, y=165:3665)

### Filler position 10 (absolute token 742, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126583, p2=5:128372, p3=20:125375, p4=3:128427, m1=105:122978, m2=60:126120, y=165:123076)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `挪` (target ranks: p1=21:7987, p2=5:3221, p3=20:9734, p4=3:3121, m1=105:21138, m2=60:10119, y=165:18301)
- Layer 20: ` Walker`, `Walker`, `ait`, `挪`, `锁定` (target ranks: p1=21:8171, p2=5:4495, p3=20:8751, p4=3:5990, m1=105:37228, m2=60:12151, y=165:27814)
- Layer 30: ` sequential`, `sequential`, `Sequ`, ` Sequential`, ` linear` (target ranks: p1=21:16325, p2=5:11299, p3=20:26866, p4=3:31705, m1=105:75845, m2=60:26936, y=165:54322)
- Layer 35: ` sequential`, `sequential`, `Sequ`, `分解`, ` waterfall` (target ranks: p1=21:10794, p2=5:6338, p3=20:15891, p4=3:10185, m1=105:42031, m2=60:18193, y=165:26171)
- Layer 36: `sequential`, ` sequential`, ` linear`, ` sequence`, `sequence` (target ranks: p1=21:33259, p2=5:27973, p3=20:33611, p4=3:38017, m1=105:35320, m2=60:35388, y=165:31075)
- Layer 37: `sequential`, `sequence`, `linear`, ` linear`, ` sequence` (target ranks: p1=21:48668, p2=5:74256, p3=20:51853, p4=3:89373, m1=105:50482, m2=60:66548, y=165:45788)
- Layer 38: `}<?`, `linear`, `sequence`, ` linear`, `程序的` (target ranks: p1=21:71032, p2=5:93641, p3=20:68323, p4=3:100566, m1=105:66049, m2=60:79199, y=165:50591)
- Layer 39: `sequence`, `}<?`, `程序的`, ` sequence`, ` Sequence` (target ranks: p1=21:101321, p2=5:113394, p3=20:84565, p4=3:114839, m1=105:90728, m2=60:114751, y=165:74738)
- Layer 40: `程序的`, `程序`, `程序中`, ` program`, `sequence` (target ranks: p1=21:49539, p2=5:70354, p3=20:50091, p4=3:67094, m1=105:46085, m2=60:98960, y=165:48640)
- Layer 41: `程序`, ` .`, ` program`, `程序的`, `程序中` (target ranks: p1=21:31195, p2=5:9801, p3=20:23201, p4=3:11072, m1=105:35654, m2=60:76966, y=165:37370)

### Filler position 11 (absolute token 743, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126770, p2=5:128470, p3=20:125544, p4=3:128513, m1=105:123554, m2=60:126441, y=165:123556)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: p1=21:8324, p2=5:3389, p3=20:10519, p4=3:3284, m1=105:22918, m2=60:11034, y=165:19702)
- Layer 20: ` LS`, `ait`, `锁定`, `挪`, ` smile` (target ranks: p1=21:950, p2=5:216, p3=20:1812, p4=3:243, m1=105:9615, m2=60:2312, y=165:12175)
- Layer 30: `Ternary`, ` ternary`, ` triplet`, ` grapes`, `乘积` (target ranks: p1=21:2472, p2=5:7210, p3=20:11053, p4=3:1232, m1=105:8265, m2=60:2821, y=165:42162)
- Layer 35: `apon`, ` Labor`, ` Kor`, ` labor`, ` ternary` (target ranks: p1=21:3889, p2=5:49360, p3=20:37873, p4=3:21684, m1=105:3895, m2=60:7760, y=165:36356)
- Layer 36: `}<?`, ` Trib`, `ာအုပ်စ`, `白玉`, `Kingdom` (target ranks: p1=21:73656, p2=5:111940, p3=20:117754, p4=3:71546, m1=105:1230, m2=60:7648, y=165:6399)
- Layer 37: `}<?`, ` premi`, `/Tropical`, ` Trib`, `Kingdom` (target ranks: p1=21:84968, p2=5:109202, p3=20:119364, p4=3:54777, m1=105:907, m2=60:12273, y=165:499)
- Layer 38: `}<?`, `/Tropical`, ` premi`, `黄豆`, `ာအုပ်စ` (target ranks: p1=21:79585, p2=5:120841, p3=20:105518, p4=3:90566, m1=105:6044, m2=60:12697, y=165:3723)
- Layer 39: `}<?`, `/Tropical`, `cault`, ` premi`, ` Humph` (target ranks: p1=21:66897, p2=5:113774, p3=20:107694, p4=3:110315, m1=105:10376, m2=60:62505, y=165:3344)
- Layer 40: `}<?`, ` dekameters`, ` dátummal`, `rá`, `错过了` (target ranks: p1=21:40817, p2=5:81260, p3=20:98318, p4=3:69874, m1=105:1603, m2=60:52040, y=165:1112)
- Layer 41: ` dátummal`, `错过了`, `就到了`, ` dekameters`, ` nuest` (target ranks: p1=21:26712, p2=5:20626, p3=20:60833, p4=3:18001, m1=105:6044, m2=60:51867, y=165:2696)

### Filler position 12 (absolute token 744, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126692, p2=5:128453, p3=20:125414, p4=3:128474, m1=105:123266, m2=60:126241, y=165:123298)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=21:8266, p2=5:3204, p3=20:10320, p4=3:2954, m1=105:22881, m2=60:10559, y=165:19406)
- Layer 20: `ait`, `锁定`, ` smile`, ` wig`, `cape` (target ranks: p1=21:6275, p2=5:1353, p3=20:7378, p4=3:2451, m1=105:27145, m2=60:10513, y=165:27237)
- Layer 30: `Tap`, `tap`, ` tap`, ` Tap`, `打完` (target ranks: p1=21:10577, p2=5:11974, p3=20:8790, p4=3:53587, m1=105:27931, m2=60:46513, y=165:68984)
- Layer 35: ` tap`, `Tap`, ` Tap`, ` met`, `tap` (target ranks: p1=21:2155, p2=5:2834, p3=20:3473, p4=3:23501, m1=105:38662, m2=60:25679, y=165:77995)
- Layer 36: `期望`, ` tap`, `adal`, `Tap`, ` bel` (target ranks: p1=21:1316, p2=5:582, p3=20:1016, p4=3:5691, m1=105:9110, m2=60:8249, y=165:42773)
- Layer 37: `坏`, `acons`, `EDAC`, ` Erkännande`, `等待着` (target ranks: p1=21:14497, p2=5:20588, p3=20:7043, p4=3:54830, m1=105:41664, m2=60:40765, y=165:82304)
- Layer 38: `}<?`, `坏`, `acons`, ` Erkännande`, `等待着` (target ranks: p1=21:29477, p2=5:51644, p3=20:15358, p4=3:80372, m1=105:36316, m2=60:60264, y=165:95821)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `acons`, `繁体`, `eteen` (target ranks: p1=21:67025, p2=5:96525, p3=20:53450, p4=3:106972, m1=105:92044, m2=60:120812, y=165:117798)
- Layer 40: ` Twenty`, ` nasod`, ` twenty`, ` .`, ` mosunod` (target ranks: p1=21:12962, p2=5:26401, p3=20:10320, p4=3:32382, m1=105:48548, m2=60:103624, y=165:86569)
- Layer 41: ` .`, `ldots`, `试一试`, ` Twenty`, ` twenty` (target ranks: p1=21:6641, p2=5:7574, p3=20:4469, p4=3:7199, m1=105:37230, m2=60:93608, y=165:62398)

### Filler position 13 (absolute token 745, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:127078, p2=5:128617, p3=20:125865, p4=3:128631, m1=105:124073, m2=60:126674, y=165:123904)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=21:8728, p2=5:3612, p3=20:10434, p4=3:3329, m1=105:21562, m2=60:10643, y=165:18779)
- Layer 20: `锁定`, `忑`, ` Walker`, `Walker`, ` engaging` (target ranks: p1=21:10758, p2=5:7944, p3=20:14744, p4=3:7681, m1=105:34663, m2=60:21323, y=165:25230)
- Layer 30: ` calculator`, ` equations`, `每一步`, ` program`, ` repetitions` (target ranks: p1=21:32940, p2=5:22782, p3=20:47207, p4=3:38699, m1=105:94566, m2=60:36710, y=165:65340)
- Layer 35: ` calculator`, ` program`, ` equations`, `锁定`, `方程的` (target ranks: p1=21:8343, p2=5:5967, p3=20:16495, p4=3:8987, m1=105:60134, m2=60:16903, y=165:30729)
- Layer 36: ` program`, ` Program`, `程序`, `Program`, `program` (target ranks: p1=21:13370, p2=5:8999, p3=20:21121, p4=3:12033, m1=105:48990, m2=60:21483, y=165:31460)
- Layer 37: ` program`, `程序的`, `程序`, `program`, ` Program` (target ranks: p1=21:46437, p2=5:67162, p3=20:73147, p4=3:67654, m1=105:97648, m2=60:93884, y=165:86895)
- Layer 38: `}<?`, ` program`, `程序的`, `程序`, ` Program` (target ranks: p1=21:61446, p2=5:86542, p3=20:74637, p4=3:79704, m1=105:91383, m2=60:112632, y=165:87246)
- Layer 39: `}<?`, `�乐`, ` pakig`, `覆`, `坏的` (target ranks: p1=21:91812, p2=5:116432, p3=20:88676, p4=3:115532, m1=105:115241, m2=60:126186, y=165:115959)
- Layer 40: ` .`, `坏`, `坏的`, `}<?`, `下沉` (target ranks: p1=21:33403, p2=5:61409, p3=20:46247, p4=3:49422, m1=105:94268, m2=60:122521, y=165:89650)
- Layer 41: ` .`, ` .↵↵`, ` `, ` ,`, `oooo` (target ranks: p1=21:33694, p2=5:10905, p3=20:32528, p4=3:17564, m1=105:44811, m2=60:117471, y=165:48030)

### Filler position 14 (absolute token 746, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=21:126994, p2=5:128581, p3=20:125698, p4=3:128607, m1=105:124143, m2=60:126667, y=165:124042)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=21:8065, p2=5:3426, p3=20:9753, p4=3:3202, m1=105:20804, m2=60:9992, y=165:17899)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, `拆` (target ranks: p1=21:9878, p2=5:4483, p3=20:9644, p4=3:5324, m1=105:28690, m2=60:16702, y=165:20764)
- Layer 30: `acos`, `平行`, `acin`, `sets`, `分解` (target ranks: p1=21:20782, p2=5:21564, p3=20:25730, p4=3:50252, m1=105:97127, m2=60:52005, y=165:87614)
- Layer 35: `羊`, `obin`, `柿子`, ` future`, `足` (target ranks: p1=21:2879, p2=5:6477, p3=20:4250, p4=3:17799, m1=105:56016, m2=60:17261, y=165:48997)
- Layer 36: `留存`, `柿子`, `俯`, ` stabil`, `羊` (target ranks: p1=21:12048, p2=5:20576, p3=20:8537, p4=3:43831, m1=105:40622, m2=60:42601, y=165:43523)
- Layer 37: `}<?`, `dividers`, `不加`, `acos`, `班的` (target ranks: p1=21:29355, p2=5:97386, p3=20:25167, p4=3:114292, m1=105:91942, m2=60:100704, y=165:86529)
- Layer 38: `}<?`, `不加`, `dividers`, ` Noruwega`, `ِّف` (target ranks: p1=21:39597, p2=5:107694, p3=20:41174, p4=3:119165, m1=105:100819, m2=60:112009, y=165:95685)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `?datasetId`, `文字的`, `tanle` (target ranks: p1=21:58732, p2=5:121456, p3=20:78916, p4=3:124631, m1=105:117218, m2=60:126809, y=165:116178)
- Layer 40: ` talags`, `留存`, `scr`, `šk`, `坏的` (target ranks: p1=21:9675, p2=5:89666, p3=20:40015, p4=3:98544, m1=105:98051, m2=60:125454, y=165:96691)
- Layer 41: ` .`, ` `, ` without`, `那两个`, ` assignment` (target ranks: p1=21:6413, p2=5:27990, p3=20:26787, p4=3:43373, m1=105:72822, m2=60:119295, y=165:64926)

### Filler position 15 (absolute token 747, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:127085, p2=5:128628, p3=20:125786, p4=3:128656, m1=105:124020, m2=60:126712, y=165:123936)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=21:7846, p2=5:3287, p3=20:9644, p4=3:3068, m1=105:20641, m2=60:10083, y=165:18191)
- Layer 20: `锁定`, `ait`, `距`, ` LS`, `拆` (target ranks: p1=21:3437, p2=5:1099, p3=20:5356, p4=3:1106, m1=105:13900, m2=60:7285, y=165:14718)
- Layer 30: `+a`, `acos`, `第一步`, ` dy`, `分解` (target ranks: p1=21:2130, p2=5:8610, p3=20:11424, p4=3:19988, m1=105:32693, m2=60:10439, y=165:58336)
- Layer 35: `12`, `分解`, ` dy`, `俯`, `第一步` (target ranks: p1=21:6, p2=5:3093, p3=20:828, p4=3:7243, m1=105:9154, m2=60:1230, y=165:27857)
- Layer 36: `留存`, `俯`, `分解`, ` pipeline`, `欢迎` (target ranks: p1=21:74, p2=5:9004, p3=20:2555, p4=3:19477, m1=105:5431, m2=60:6000, y=165:29661)
- Layer 37: `21`, `}<?`, `acos`, ` Aub`, `Hakutulos` (target ranks: p1=21:1, p2=5:67179, p3=20:2077, p4=3:91971, m1=105:21729, m2=60:32502, y=165:82247)
- Layer 38: `}<?`, `Hakutulos`, `21`, `uerak`, `ajes` (target ranks: p1=21:3, p2=5:97062, p3=20:12242, p4=3:114292, m1=105:55926, m2=60:75393, y=165:112991)
- Layer 39: `二十一`, `21`, `}<?`, `orten`, `?datasetId` (target ranks: p1=21:2, p2=5:119416, p3=20:51269, p4=3:123590, m1=105:71261, m2=60:122479, y=165:124610)
- Layer 40: `二十一`, `21`, ` twenty`, `留存`, ` Twenty` (target ranks: p1=21:2, p2=5:85582, p3=20:23770, p4=3:99079, m1=105:41145, m2=60:119287, y=165:119177)
- Layer 41: ` .`, `二十一`, `试一试`, `21`, `留存` (target ranks: p1=21:4, p2=5:14814, p3=20:33477, p4=3:26724, m1=105:32150, m2=60:112107, y=165:95048)

### Filler position 16 (absolute token 748, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=21:126954, p2=5:128563, p3=20:125475, p4=3:128587, m1=105:124067, m2=60:126506, y=165:123892)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=21:9343, p2=5:4035, p3=20:11460, p4=3:3901, m1=105:23018, m2=60:11751, y=165:19958)
- Layer 20: `锁定`, `ait`, `挪`, ` smile`, ` LS` (target ranks: p1=21:2539, p2=5:549, p3=20:2964, p4=3:672, m1=105:17203, m2=60:4960, y=165:15920)
- Layer 30: ` ternary`, `Ternary`, ` Ternary`, `atri`, `三星` (target ranks: p1=21:17754, p2=5:5221, p3=20:24712, p4=3:9, m1=105:46163, m2=60:8954, y=165:74076)
- Layer 35: `03`, `粥`, ` ternary`, ` patriotic`, `atri` (target ranks: p1=21:1226, p2=5:12666, p3=20:11354, p4=3:42, m1=105:516, m2=60:3361, y=165:18765)
- Layer 36: `}<?`, ` triplet`, `许诺`, ` rigor`, ` nine` (target ranks: p1=21:9809, p2=5:73419, p3=20:83202, p4=3:788, m1=105:456, m2=60:2885, y=165:3333)
- Layer 37: `}<?`, ` Nij`, ` triplet`, ` trio`, `进修` (target ranks: p1=21:27024, p2=5:103782, p3=20:105843, p4=3:1792, m1=105:1668, m2=60:11349, y=165:3993)
- Layer 38: `}<?`, ` Nij`, ` triplet`, ` trio`, `殿堂` (target ranks: p1=21:23499, p2=5:108939, p3=20:105183, p4=3:5126, m1=105:3691, m2=60:7417, y=165:3674)
- Layer 39: `}<?`, ` Nij`, ` dátummal`, `东海`, `花瓣` (target ranks: p1=21:815, p2=5:84881, p3=20:64828, p4=3:72702, m1=105:3129, m2=60:41110, y=165:1946)
- Layer 40: ` consum`, `}<?`, ` filler`, ` structured`, ` Nij` (target ranks: p1=21:143, p2=5:31376, p3=20:36386, p4=3:19618, m1=105:501, m2=60:26762, y=165:1068)
- Layer 41: ` .`, `anine`, ` .↵↵`, ` ,`, ` permitting` (target ranks: p1=21:527, p2=5:6167, p3=20:24039, p4=3:6190, m1=105:5482, m2=60:53401, y=165:8710)

### Filler position 17 (absolute token 749, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=21:126955, p2=5:128572, p3=20:125494, p4=3:128608, m1=105:124230, m2=60:126578, y=165:124088)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=21:9798, p2=5:4582, p3=20:12014, p4=3:4446, m1=105:24518, m2=60:12840, y=165:22179)
- Layer 20: `锁定`, ` smile`, `ession`, `距`, `cape` (target ranks: p1=21:3253, p2=5:2433, p3=20:4617, p4=3:3019, m1=105:17795, m2=60:10932, y=165:14517)
- Layer 30: `锁定`, `鞍`, `acin`, ` picnic`, ` reserved` (target ranks: p1=21:12270, p2=5:10150, p3=20:19981, p4=3:23765, m1=105:31418, m2=60:11147, y=165:26201)
- Layer 35: `锁定`, ` .`, `重复`, ` EC`, ` reserved` (target ranks: p1=21:2643, p2=5:3353, p3=20:6198, p4=3:8891, m1=105:16150, m2=60:5999, y=165:22047)
- Layer 36: `反复`, `坏`, `羊`, `停`, `锁定` (target ranks: p1=21:3885, p2=5:5457, p3=20:9536, p4=3:11869, m1=105:9247, m2=60:7634, y=165:18075)
- Layer 37: `}<?`, `坏`, `不急`, `铎`, `用了` (target ranks: p1=21:28223, p2=5:53043, p3=20:65684, p4=3:69070, m1=105:37127, m2=60:63327, y=165:47440)
- Layer 38: `坏`, `}<?`, `铎`, `不急`, `壞` (target ranks: p1=21:48660, p2=5:71909, p3=20:84294, p4=3:90559, m1=105:43846, m2=60:93083, y=165:66190)
- Layer 39: `坏`, `铎`, `}<?`, `东海`, `不急` (target ranks: p1=21:11339, p2=5:90905, p3=20:84099, p4=3:102920, m1=105:71602, m2=60:117137, y=165:94771)
- Layer 40: ` .`, `坏`, `不急`, ` .↵↵`, ` nasod` (target ranks: p1=21:568, p2=5:30748, p3=20:43139, p4=3:41256, m1=105:31350, m2=60:97103, y=165:45743)
- Layer 41: ` .`, ` .↵↵`, `坏`, ` .↵`, ` ` (target ranks: p1=21:1016, p2=5:4702, p3=20:32213, p4=3:12148, m1=105:12731, m2=60:69355, y=165:23895)

### Filler position 18 (absolute token 750, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `Noiz` (target ranks: p1=21:127055, p2=5:128618, p3=20:125600, p4=3:128645, m1=105:124541, m2=60:126716, y=165:124316)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=21:8759, p2=5:3689, p3=20:10627, p4=3:3494, m1=105:23995, m2=60:11196, y=165:20970)
- Layer 20: `忑`, ` smile`, ` Walker`, `ait`, `锁定` (target ranks: p1=21:6639, p2=5:4595, p3=20:5926, p4=3:5486, m1=105:31609, m2=60:13475, y=165:27660)
- Layer 30: `鞍`, `atan`, ` ternary`, `acin`, ` Ries` (target ranks: p1=21:8376, p2=5:5657, p3=20:11292, p4=3:1437, m1=105:72289, m2=60:14180, y=165:67547)
- Layer 35: ` met`, `足`, `羊`, `鞍`, ` quadr` (target ranks: p1=21:3311, p2=5:346, p3=20:2495, p4=3:1874, m1=105:35427, m2=60:9421, y=165:42671)
- Layer 36: `adal`, `留存`, `羊`, ` stabil`, `翻` (target ranks: p1=21:8572, p2=5:490, p3=20:3382, p4=3:4140, m1=105:21072, m2=60:14187, y=165:39513)
- Layer 37: `}<?`, `otan`, `班上`, `翻了`, `不急` (target ranks: p1=21:46673, p2=5:800, p3=20:18498, p4=3:29705, m1=105:43271, m2=60:75857, y=165:81907)
- Layer 38: `}<?`, `otan`, `dividers`, `不急`, `osit` (target ranks: p1=21:80997, p2=5:5781, p3=20:46948, p4=3:65068, m1=105:58764, m2=60:104001, y=165:91474)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `东海`, `迷惑`, `下沉` (target ranks: p1=21:27385, p2=5:44511, p3=20:52269, p4=3:115699, m1=105:93396, m2=60:121717, y=165:105977)
- Layer 40: ` .`, `}<?`, `等待着`, `下沉`, ` E` (target ranks: p1=21:4014, p2=5:5394, p3=20:18995, p4=3:79357, m1=105:55669, m2=60:115147, y=165:74917)
- Layer 41: ` .`, ` `, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` ;` (target ranks: p1=21:3982, p2=5:1415, p3=20:16763, p4=3:25818, m1=105:38730, m2=60:102949, y=165:66609)

### Filler position 19 (absolute token 751, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=21:127345, p2=5:128755, p3=20:126042, p4=3:128783, m1=105:124945, m2=60:127128, y=165:124731)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=21:8472, p2=5:3395, p3=20:10120, p4=3:3209, m1=105:23518, m2=60:10882, y=165:20366)
- Layer 20: ` Walker`, `ait`, `忑`, `Walker`, `会成为` (target ranks: p1=21:7824, p2=5:7038, p3=20:7745, p4=3:8288, m1=105:35488, m2=60:16983, y=165:36489)
- Layer 30: `重复`, `两类`, ` repetitions`, ` exercises`, `平行` (target ranks: p1=21:12876, p2=5:10813, p3=20:13365, p4=3:17961, m1=105:53990, m2=60:27102, y=165:68994)
- Layer 35: ` Type`, ` alternating`, ` repetition`, ` repetitions`, ` quadr` (target ranks: p1=21:4447, p2=5:6340, p3=20:9403, p4=3:13739, m1=105:23283, m2=60:13563, y=165:42222)
- Layer 36: ` Type`, ` quadr`, ` pattern`, `Type`, `形式` (target ranks: p1=21:7565, p2=5:12169, p3=20:10183, p4=3:22582, m1=105:7760, m2=60:16380, y=165:38827)
- Layer 37: ` pattern`, ` Type`, ` Pattern`, `pattern`, ` alternating` (target ranks: p1=21:15554, p2=5:54126, p3=20:25286, p4=3:90938, m1=105:16536, m2=60:55148, y=165:81294)
- Layer 38: `}<?`, `交替`, ` pattern`, ` alternating`, ` Type` (target ranks: p1=21:31801, p2=5:91383, p3=20:36679, p4=3:108656, m1=105:29448, m2=60:71722, y=165:103355)
- Layer 39: `pattern`, ` pattern`, ` Pattern`, `}<?`, `Pattern` (target ranks: p1=21:59527, p2=5:109481, p3=20:50507, p4=3:114326, m1=105:59053, m2=60:97320, y=165:108792)
- Layer 40: `程序的`, ` program`, ` pattern`, `程序`, ` Program` (target ranks: p1=21:9370, p2=5:55060, p3=20:21283, p4=3:68642, m1=105:23627, m2=60:74754, y=165:70256)
- Layer 41: ` .`, ` program`, ` pattern`, `程序的`, `程序` (target ranks: p1=21:10385, p2=5:6341, p3=20:14571, p4=3:28552, m1=105:12895, m2=60:74899, y=165:61927)

### Filler position 20 (absolute token 752, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `-ulo`, `aplenty` (target ranks: p1=21:127580, p2=5:128834, p3=20:126354, p4=3:128887, m1=105:125532, m2=60:127531, y=165:125320)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=21:9311, p2=5:3815, p3=20:10827, p4=3:3561, m1=105:23345, m2=60:10927, y=165:19948)
- Layer 20: `ait`, ` Walker`, `平行`, ` engaging`, `锁定` (target ranks: p1=21:12913, p2=5:11334, p3=20:11057, p4=3:11407, m1=105:41352, m2=60:17494, y=165:37486)
- Layer 30: `清楚楚`, `算出`, `+p`, `第一步`, `calcul` (target ranks: p1=21:1047, p2=5:19428, p3=20:14945, p4=3:35555, m1=105:57284, m2=60:21989, y=165:85702)
- Layer 35: ` calculator`, ` p`, `清楚楚`, `calcul`, ` tap` (target ranks: p1=21:240, p2=5:6072, p3=20:4136, p4=3:10520, m1=105:23121, m2=60:4715, y=165:45433)
- Layer 36: `清楚楚`, `俯`, `calcul`, ` tap`, `留存` (target ranks: p1=21:385, p2=5:9421, p3=20:4507, p4=3:15413, m1=105:9886, m2=60:8726, y=165:28216)
- Layer 37: ` p`, `calcul`, `清楚楚`, `俯`, `进行计算` (target ranks: p1=21:335, p2=5:55850, p3=20:11326, p4=3:75486, m1=105:19354, m2=60:34274, y=165:65167)
- Layer 38: ` p`, `calcul`, `p`, `进行计算`, `计算的` (target ranks: p1=21:749, p2=5:75138, p3=20:15291, p4=3:86520, m1=105:18593, m2=60:40379, y=165:77439)
- Layer 39: ` p`, `p`, `}<?`, `zp`, `}p` (target ranks: p1=21:2699, p2=5:89596, p3=20:20581, p4=3:99926, m1=105:29316, m2=60:60757, y=165:97345)
- Layer 40: ` p`, `p`, `坏`, `ess`, `留存` (target ranks: p1=21:286, p2=5:51235, p3=20:8459, p4=3:64736, m1=105:20843, m2=60:63741, y=165:69616)
- Layer 41: ` .`, ` `, `外商投资`, ` Calculators`, `试一试` (target ranks: p1=21:225, p2=5:4854, p3=20:4512, p4=3:12994, m1=105:11866, m2=60:54658, y=165:53562)

### Filler position 21 (absolute token 753, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `Noiz`, `-ulo` (target ranks: p1=21:127466, p2=5:128787, p3=20:126221, p4=3:128851, m1=105:125319, m2=60:127367, y=165:125098)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=21:9302, p2=5:3826, p3=20:10800, p4=3:3557, m1=105:22692, m2=60:10839, y=165:19973)
- Layer 20: `俯`, ` TA`, ` biotic`, ` remembering`, `corpor` (target ranks: p1=21:3822, p2=5:36977, p3=20:8297, p4=3:28552, m1=105:41448, m2=60:36154, y=165:79898)
- Layer 30: `}using`, ` spac`, `acos`, ` dekameters`, `}<?` (target ranks: p1=21:13854, p2=5:111693, p3=20:32563, p4=3:115013, m1=105:109973, m2=60:89814, y=165:97255)
- Layer 35: `二十二`, `}using`, `二十三`, ` twenty`, `滴水` (target ranks: p1=21:352, p2=5:76496, p3=20:4448, p4=3:84506, m1=105:118486, m2=60:94811, y=165:109427)
- Layer 36: `陌生`, `反复`, `滴水`, `ancock`, ` blank` (target ranks: p1=21:153, p2=5:29810, p3=20:1752, p4=3:36198, m1=105:83614, m2=60:44731, y=165:80180)
- Layer 37: `}<?`, `坏`, ` covari`, `ِّف`, `isis` (target ranks: p1=21:4984, p2=5:91170, p3=20:18483, p4=3:89295, m1=105:111077, m2=60:82729, y=165:108429)
- Layer 38: ` .`, ` covari`, ` club`, `坏`, ` .↵↵` (target ranks: p1=21:1366, p2=5:89238, p3=20:6509, p4=3:76060, m1=105:76186, m2=60:68963, y=165:79759)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` covari`, `坏` (target ranks: p1=21:14677, p2=5:109159, p3=20:41654, p4=3:116952, m1=105:103766, m2=60:111740, y=165:106106)
- Layer 40: ` .`, ` .↵↵`, `<｜begin▁of▁sentence｜>`, ` .↵`, `坏` (target ranks: p1=21:2264, p2=5:60022, p3=20:15787, p4=3:75037, m1=105:58078, m2=60:90397, y=165:59030)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `这就是`, ` except` (target ranks: p1=21:852, p2=5:9590, p3=20:5905, p4=3:12215, m1=105:27639, m2=60:68715, y=165:32524)

### Filler position 22 (absolute token 754, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=21:127758, p2=5:128906, p3=20:126551, p4=3:128974, m1=105:125779, m2=60:127749, y=165:125594)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: p1=21:8515, p2=5:3397, p3=20:10187, p4=3:3199, m1=105:22128, m2=60:10168, y=165:19455)
- Layer 20: ` quadr`, `cape`, `同步`, ` smile`, `auce` (target ranks: p1=21:177, p2=5:114, p3=20:107, p4=3:84, m1=105:11085, m2=60:174, y=165:11568)
- Layer 30: `}<?`, `opters`, `Quintal`, ` سما`, `东京` (target ranks: p1=21:26884, p2=5:60567, p3=20:25330, p4=3:41670, m1=105:56587, m2=60:12972, y=165:77429)
- Layer 35: `apon`, `}<?`, `备课`, `陪`, `ikuha` (target ranks: p1=21:3067, p2=5:83401, p3=20:23640, p4=3:42847, m1=105:19613, m2=60:5478, y=165:47944)
- Layer 36: `}<?`, `本题分析`, `ာအုပ်စ`, ` forbid`, `黄豆` (target ranks: p1=21:13886, p2=5:115541, p3=20:58762, p4=3:71179, m1=105:27463, m2=60:8169, y=165:19309)
- Layer 37: `}<?`, `本题分析`, ` premi`, `)Skip`, `黄豆` (target ranks: p1=21:39736, p2=5:112446, p3=20:90495, p4=3:84079, m1=105:27553, m2=60:30063, y=165:4228)
- Layer 38: `}<?`, `garan`, `白玉`, ` premi`, `黄豆` (target ranks: p1=21:34435, p2=5:120021, p3=20:81071, p4=3:116754, m1=105:64490, m2=60:22780, y=165:10575)
- Layer 39: `}<?`, `cault`, `garan`, `hemer`, ` consonant` (target ranks: p1=21:30867, p2=5:116876, p3=20:62296, p4=3:123678, m1=105:88532, m2=60:56739, y=165:13685)
- Layer 40: `错过了`, `garan`, ` responses`, `发声`, `错过` (target ranks: p1=21:6169, p2=5:80100, p3=20:34147, p4=3:105487, m1=105:55534, m2=60:35305, y=165:4739)
- Layer 41: ` .`, `错过了`, ` .↵↵`, `错过`, ` .↵` (target ranks: p1=21:688, p2=5:18084, p3=20:8650, p4=3:21759, m1=105:48875, m2=60:29043, y=165:5057)

### Filler position 23 (absolute token 755, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `datasetId` (target ranks: p1=21:127636, p2=5:128868, p3=20:126396, p4=3:128932, m1=105:125792, m2=60:127633, y=165:125586)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=21:7563, p2=5:3038, p3=20:9550, p4=3:2861, m1=105:21916, m2=60:9748, y=165:19479)
- Layer 20: `Dutch`, ` Dutch`, `tered`, `tails`, `吞` (target ranks: p1=21:3852, p2=5:11245, p3=20:7696, p4=3:9863, m1=105:56768, m2=60:18399, y=165:42542)
- Layer 30: `codeline`, `东京`, `)Skip`, `东海`, `okens` (target ranks: p1=21:55661, p2=5:101935, p3=20:62654, p4=3:110639, m1=105:107934, m2=60:80638, y=165:117927)
- Layer 35: `codeline`, `坏`, `删`, ` fif`, ` gears` (target ranks: p1=21:21117, p2=5:93247, p3=20:34652, p4=3:98409, m1=105:116335, m2=60:68758, y=165:125952)
- Layer 36: `坏`, `告诉我们`, `/hess`, `停`, ` soci` (target ranks: p1=21:24376, p2=5:56148, p3=20:35659, p4=3:59036, m1=105:85369, m2=60:19784, y=165:111018)
- Layer 37: `镶嵌`, `肤`, `贻`, ` tide`, ` germ` (target ranks: p1=21:37555, p2=5:98382, p3=20:71028, p4=3:96792, m1=105:115989, m2=60:47010, y=165:119694)
- Layer 38: `肤`, ` germ`, `镶嵌`, `锚`, `itore` (target ranks: p1=21:26494, p2=5:82064, p3=20:51302, p4=3:87191, m1=105:91470, m2=60:35801, y=165:105573)
- Layer 39: ` encomp`, `肤`, ` .`, ` germ`, ` .↵↵` (target ranks: p1=21:42441, p2=5:117095, p3=20:84344, p4=3:113768, m1=105:99791, m2=60:108001, y=165:117031)
- Layer 40: ` .`, ` .↵↵`, `肤`, ` .↵`, `镶嵌` (target ranks: p1=21:25984, p2=5:96633, p3=20:71051, p4=3:84469, m1=105:77723, m2=60:107387, y=165:110231)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, ` ,` (target ranks: p1=21:7735, p2=5:52044, p3=20:21951, p4=3:48318, m1=105:29221, m2=60:61386, y=165:64271)

### Filler position 24 (absolute token 756, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `-ulo` (target ranks: p1=21:127814, p2=5:128934, p3=20:126569, p4=3:128987, m1=105:125935, m2=60:127756, y=165:125687)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: p1=21:7849, p2=5:3097, p3=20:9574, p4=3:2910, m1=105:22508, m2=60:9521, y=165:19182)
- Layer 20: ` smile`, `站`, `cape`, `肩`, `足` (target ranks: p1=21:2178, p2=5:348, p3=20:1460, p4=3:709, m1=105:36581, m2=60:2623, y=165:13316)
- Layer 30: `codeline`, `</think>`, ` Answer`, `oNames`, `hatic` (target ranks: p1=21:100903, p2=5:103441, p3=20:96028, p4=3:119533, m1=105:113038, m2=60:116554, y=165:120965)
- Layer 35: `codeline`, `AED`, ` Answer`, ` tagged`, ` autoc` (target ranks: p1=21:57016, p2=5:99765, p3=20:75715, p4=3:101839, m1=105:89715, m2=60:76008, y=165:110530)
- Layer 36: `codeline`, ` Answer`, `坏`, ` nasod`, `良` (target ranks: p1=21:12603, p2=5:37330, p3=20:25611, p4=3:51101, m1=105:38402, m2=60:20985, y=165:77734)
- Layer 37: `codeline`, `hatic`, `oNames`, `okens`, `�` (target ranks: p1=21:75841, p2=5:119768, p3=20:90281, p4=3:123168, m1=105:89724, m2=60:96599, y=165:113658)
- Layer 38: `hatic`, `codeline`, `oNames`, `okens`, `<|EOT|>` (target ranks: p1=21:79801, p2=5:116574, p3=20:78657, p4=3:123756, m1=105:49968, m2=60:83988, y=165:89156)
- Layer 39: `hatic`, `codeline`, `-ulo`, `deen`, `贻` (target ranks: p1=21:37671, p2=5:109676, p3=20:63352, p4=3:121482, m1=105:58628, m2=60:69105, y=165:104320)
- Layer 40: ` Answer`, ` .↵↵`, `叮`, ` ingenu`, ` unflagged` (target ranks: p1=21:2317, p2=5:27860, p3=20:10680, p4=3:59455, m1=105:25974, m2=60:26229, y=165:69336)
- Layer 41: ` .`, ` .↵↵`, ` Answer`, `Answer`, ` .↵` (target ranks: p1=21:728, p2=5:4346, p3=20:3748, p4=3:16866, m1=105:26961, m2=60:17568, y=165:53605)

### Filler position 25 (absolute token 757, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `EDMF` (target ranks: p1=21:122713, p2=5:126531, p3=20:120961, p4=3:126769, m1=105:112944, m2=60:121874, y=165:114836)
- Layer 10: `eine`, `tas`, `ej`, `som`, `Achie` (target ranks: p1=21:31431, p2=5:42250, p3=20:33250, p4=3:41171, m1=105:11092, m2=60:33594, y=165:15789)
- Layer 20: ` Submission`, `平行`, `鸯`, `能被`, `Sequ` (target ranks: p1=21:7213, p2=5:8359, p3=20:6737, p4=3:15390, m1=105:20113, m2=60:15157, y=165:33174)
- Layer 30: ` Paglin`, ` Maur`, ` الجرم`, `cot`, ` المطلع` (target ranks: p1=21:9310, p2=5:104273, p3=20:25139, p4=3:98132, m1=105:7552, m2=60:29801, y=165:62124)
- Layer 35: `129`, ` Paglin`, `答案是`, `tang`, `堂` (target ranks: p1=21:8723, p2=5:113867, p3=20:114887, p4=3:112292, m1=105:34, m2=60:34764, y=165:890)
- Layer 36: `129`, ` Paglin`, `135`, `111`, `159` (target ranks: p1=21:62137, p2=5:111667, p3=20:124056, p4=3:92903, m1=105:6, m2=60:38198, y=165:213)
- Layer 37: ` Paglin`, `?datasetId`, `灵感`, `129`, `135` (target ranks: p1=21:92667, p2=5:122732, p3=20:126202, p4=3:115493, m1=105:46, m2=60:90606, y=165:630)
- Layer 38: ` Paglin`, `灵力`, `ulam`, `zam`, ` lamin` (target ranks: p1=21:99572, p2=5:127692, p3=20:125938, p4=3:125011, m1=105:280, m2=60:108113, y=165:1744)
- Layer 39: ` Answer`, `答案`, ` Paglin`, ` Antwort`, ` ответ` (target ranks: p1=21:119218, p2=5:125633, p3=20:112799, p4=3:126784, m1=105:9646, m2=60:100628, y=165:16382)
- Layer 40: ` Answer`, `Answer`, ` answer`, `回答`, `答案` (target ranks: p1=21:63638, p2=5:82631, p3=20:50684, p4=3:78939, m1=105:698, m2=60:42424, y=165:3252)
- Layer 41: `Answer`, ` Answer`, ` answer`, `回答`, `答案` (target ranks: p1=21:6459, p2=5:2450, p3=20:4776, p4=3:3552, m1=105:1328, m2=60:9367, y=165:1891)

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

Answer:<｜Assistant｜></think>80<｜end▁of▁sentence｜><｜User｜>a = 12
b = 9
c = 11
d = 6
e = 8
f = 12
g = 9
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

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
