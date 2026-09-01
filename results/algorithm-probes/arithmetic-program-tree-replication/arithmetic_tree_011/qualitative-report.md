# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `100` (correct).
- No-filler answer: `100` (correct).
- Filler tokens: 25 tokens at absolute indices 733–757.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `p1=12` | 3 (L40, filler 15) | L40, filler 15 (rank 3) |
| J-Lens | `p2=3` | 105 (L20, filler 22) | Never |
| J-Lens | `p3=16` | 7 (L35, filler 22) | L35, filler 22 (rank 7) |
| J-Lens | `p4=4` | 32 (L20, filler 24) | Never |
| J-Lens | `m1=36` | 2 (L36, filler 22) | L33, filler 22 (rank 9) |
| J-Lens | `m2=64` | 11 (L35, filler 9) | Never |
| J-Lens | `y=100` | 43 (L31, filler 7) | Never |
| Logit lens | `p1=12` | 5 (L31, filler 22) | L26, filler 7 (rank 7) |
| Logit lens | `p2=3` | 64 (L36, filler 8) | Never |
| Logit lens | `p3=16` | 3 (L33, filler 22) | L31, filler 22 (rank 4) |
| Logit lens | `p4=4` | 4 (L29, filler 16) | L28, filler 16 (rank 8) |
| Logit lens | `m1=36` | 1 (L27, filler 7) | L23, filler 7 (rank 9) |
| Logit lens | `m2=64` | 2 (L25, filler 7) | L25, filler 7 (rank 2) |
| Logit lens | `y=100` | 1 (L24, filler 7) | L22, filler 7 (rank 3) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 733, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: p1=12:121784, p2=3:126110, p3=16:121943, p4=4:125774, m1=36:119723, m2=64:120560, y=100:116667)
- Layer 10: `忑`, `anta`, ` Walker`, `锁定`, `fine` (target ranks: p1=12:28348, p2=3:16848, p3=16:31232, p4=4:17474, m1=36:29657, m2=64:36764, y=100:26356)
- Layer 20: ` .`, `足`, `垂`, `Dot`, `dots` (target ranks: p1=12:16141, p2=3:2695, p3=16:10838, p4=4:1365, m1=36:8744, m2=64:2873, y=100:5143)
- Layer 30: `回答`, `Tap`, `tap`, ` tap`, `计算的` (target ranks: p1=12:14581, p2=3:12937, p3=16:22148, p4=4:9349, m1=36:6642, m2=64:2147, y=100:3800)
- Layer 35: `应答`, `回答`, `68`, ` tap`, ` پاسخ` (target ranks: p1=12:5375, p2=3:7329, p3=16:7238, p4=4:2989, m1=36:837, m2=64:114, y=100:371)
- Layer 36: `期望`, ` talags`, ` tap`, `私`, `期待` (target ranks: p1=12:15953, p2=3:21317, p3=16:22414, p4=4:9510, m1=36:2594, m2=64:485, y=100:1048)
- Layer 37: ` talags`, ` pakig`, `}<?`, ` tra`, `在北京` (target ranks: p1=12:85907, p2=3:116271, p3=16:95006, p4=4:93904, m1=36:49921, m2=64:11883, y=100:11488)
- Layer 38: ` talags`, `}<?`, ` pakig`, ` tra`, `替换` (target ranks: p1=12:105381, p2=3:119843, p3=16:120030, p4=4:100780, m1=36:90781, m2=64:23562, y=100:10781)
- Layer 39: `}<?`, ` talags`, ` pakig`, `替换`, `叶子` (target ranks: p1=12:116500, p2=3:125159, p3=16:126192, p4=4:118131, m1=36:94834, m2=64:84314, y=100:53534)
- Layer 40: ` talags`, ` .`, `dots`, `oooo`, ` nasod` (target ranks: p1=12:80348, p2=3:88209, p3=16:118328, p4=4:65983, m1=36:49557, m2=64:31275, y=100:7294)
- Layer 41: ` .`, ` .↵↵`, `我没有`, ` .↵`, `我也` (target ranks: p1=12:77096, p2=3:47954, p3=16:102081, p4=4:52611, m1=36:26613, m2=64:56919, y=100:19866)

### Filler position 2 (absolute token 734, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `-ulo`, `�乐` (target ranks: p1=12:122124, p2=3:125972, p3=16:122945, p4=4:125801, m1=36:120677, m2=64:122218, y=100:120205)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: p1=12:13920, p2=3:4186, p3=16:16751, p4=4:4949, m1=36:17272, m2=64:19393, y=100:21647)
- Layer 20: ` .`, ` .----`, ` .↵↵`, `往常`, ` procedural` (target ranks: p1=12:124780, p2=3:76585, p3=16:112384, p4=4:86044, m1=36:116262, m2=64:99236, y=100:97224)
- Layer 30: ` hilabihan`, ` etxek`, ` dekameters`, ` .----`, ` pakig` (target ranks: p1=12:118769, p2=3:122552, p3=16:98827, p4=4:121509, m1=36:122746, m2=64:117181, y=100:115703)
- Layer 35: ` .`, ` hilabihan`, `enclose`, ` silic`, ` ninete` (target ranks: p1=12:103090, p2=3:120526, p3=16:86021, p4=4:113599, m1=36:123074, m2=64:126915, y=100:101943)
- Layer 36: `enclose`, ` hilabihan`, ` .`, `漏斗`, `停` (target ranks: p1=12:69419, p2=3:79875, p3=16:44616, p4=4:65981, m1=36:100550, m2=64:109208, y=100:52681)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, ` Erkännande`, `TreeLabel` (target ranks: p1=12:119104, p2=3:127176, p3=16:108299, p4=4:124829, m1=36:125347, m2=64:124183, y=100:100348)
- Layer 38: ` hilabihan`, ` .`, `}<?`, `繁体`, ` talags` (target ranks: p1=12:85288, p2=3:124646, p3=16:49218, p4=4:115112, m1=36:116488, m2=64:112318, y=100:60487)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, ` hilabihan`, ` talags`, `}<?` (target ranks: p1=12:83629, p2=3:122668, p3=16:92547, p4=4:115994, m1=36:110287, m2=64:109059, y=100:40952)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, `<｜begin▁of▁sentence｜>` (target ranks: p1=12:23196, p2=3:76720, p3=16:44058, p4=4:62942, m1=36:83481, m2=64:70072, y=100:11825)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `中书` (target ranks: p1=12:10550, p2=3:11833, p3=16:22360, p4=4:10429, m1=36:43430, m2=64:44553, y=100:3138)

### Filler position 3 (absolute token 735, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=12:125304, p2=3:128044, p3=16:125517, p4=4:127907, m1=36:124697, m2=64:125722, y=100:123930)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, `忑` (target ranks: p1=12:9920, p2=3:3948, p3=16:10532, p4=4:4383, m1=36:12114, m2=64:13610, y=100:19164)
- Layer 20: `ait`, `锁定`, `忑`, `cape`, ` wig` (target ranks: p1=12:11205, p2=3:1505, p3=16:12770, p4=4:2585, m1=36:6459, m2=64:9479, y=100:12428)
- Layer 30: ` repetition`, ` repetitions`, `打法`, ` waterfall`, `重复` (target ranks: p1=12:9588, p2=3:9284, p3=16:25833, p4=4:2949, m1=36:7283, m2=64:27372, y=100:4567)
- Layer 35: ` repetition`, ` repetitions`, ` arithmetic`, ` sequential`, `sequential` (target ranks: p1=12:4566, p2=3:8767, p3=16:10983, p4=4:1869, m1=36:2462, m2=64:8705, y=100:3524)
- Layer 36: `sequential`, `输入的`, ` sequential`, ` repeated`, ` repetition` (target ranks: p1=12:7709, p2=3:11732, p3=16:19329, p4=4:3298, m1=36:2050, m2=64:10688, y=100:6009)
- Layer 37: ` arithmetic`, `arithm`, ` Zad`, `sequences`, `ithmetic` (target ranks: p1=12:25110, p2=3:48621, p3=16:46505, p4=4:19637, m1=36:6418, m2=64:36535, y=100:16450)
- Layer 38: `}<?`, ` arithmetic`, `打磨`, `�`, `混乱` (target ranks: p1=12:52254, p2=3:88934, p3=16:78677, p4=4:51046, m1=36:24155, m2=64:61925, y=100:29254)
- Layer 39: `}<?`, `hatic`, `�`, `迷惑`, `本题分析` (target ranks: p1=12:85609, p2=3:122475, p3=16:112372, p4=4:116130, m1=36:81483, m2=64:97099, y=100:71081)
- Layer 40: ` filler`, `程序的`, `程序`, `幻觉`, ` repetition` (target ranks: p1=12:23617, p2=3:83546, p3=16:75298, p4=4:56484, m1=36:35322, m2=64:60228, y=100:30572)
- Layer 41: ` .`, `试一试`, ` without`, `Answer`, `程序` (target ranks: p1=12:11113, p2=3:25474, p3=16:58084, p4=4:31179, m1=36:38363, m2=64:57426, y=100:11982)

### Filler position 4 (absolute token 736, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126528, p2=3:128498, p3=16:126331, p4=4:128397, m1=36:125512, m2=64:126704, y=100:125129)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=12:9203, p2=3:3205, p3=16:9235, p4=4:3249, m1=36:10910, m2=64:12332, y=100:16353)
- Layer 20: `ait`, `cape`, `atile`, ` LS`, `胃癌` (target ranks: p1=12:7287, p2=3:2169, p3=16:6575, p4=4:502, m1=36:8062, m2=64:5175, y=100:17523)
- Layer 30: `Tap`, `tap`, ` tap`, ` Tap`, `打法` (target ranks: p1=12:14391, p2=3:15595, p3=16:10662, p4=4:2822, m1=36:4008, m2=64:4726, y=100:47778)
- Layer 35: `Tap`, ` tap`, `打法`, `期待`, `tap` (target ranks: p1=12:3809, p2=3:16080, p3=16:8135, p4=4:2887, m1=36:1515, m2=64:517, y=100:13726)
- Layer 36: ` tap`, `Tap`, `期待`, `打法`, `期望` (target ranks: p1=12:4874, p2=3:16811, p3=16:14010, p4=4:3667, m1=36:1633, m2=64:755, y=100:16143)
- Layer 37: `本题分析`, `abits`, `anic`, ` inde`, `小青` (target ranks: p1=12:17871, p2=3:53279, p3=16:24459, p4=4:16449, m1=36:6185, m2=64:1979, y=100:30756)
- Layer 38: `本题分析`, `ozygous`, `迷惑`, `osine`, `糊涂` (target ranks: p1=12:55520, p2=3:87842, p3=16:80714, p4=4:56475, m1=36:24934, m2=64:10553, y=100:38500)
- Layer 39: `本题分析`, `迷惑`, `糊涂`, `思想的`, ` consonant` (target ranks: p1=12:91638, p2=3:108341, p3=16:101319, p4=4:103916, m1=36:78397, m2=64:34593, y=100:54730)
- Layer 40: `语言文字`, `迷惑`, `amam`, `叮`, `冰冰` (target ranks: p1=12:45850, p2=3:59435, p3=16:71081, p4=4:53361, m1=36:52011, m2=64:15385, y=100:20451)
- Layer 41: ` .`, `试一试`, `语言文字`, `袄`, `小程序` (target ranks: p1=12:22137, p2=3:9898, p3=16:53075, p4=4:17039, m1=36:53556, m2=64:35755, y=100:29370)

### Filler position 5 (absolute token 737, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126436, p2=3:128413, p3=16:126093, p4=4:128323, m1=36:125082, m2=64:126359, y=100:124617)
- Layer 10: ` Walker`, `锁定`, `挪`, `Walker`, `ait` (target ranks: p1=12:10428, p2=3:3967, p3=16:10728, p4=4:4325, m1=36:12620, m2=64:14259, y=100:16960)
- Layer 20: `幽`, `锁定`, `鞍`, ` LS`, `挪` (target ranks: p1=12:10395, p2=3:2265, p3=16:10355, p4=4:3080, m1=36:10768, m2=64:10075, y=100:12077)
- Layer 30: `�`, `acos`, `鞍`, `acin`, ` corona` (target ranks: p1=12:13233, p2=3:19349, p3=16:48520, p4=4:16087, m1=36:21564, m2=64:18593, y=100:6379)
- Layer 35: `羊`, ` var`, ` repetition`, `Tap`, ` Rip` (target ranks: p1=12:3268, p2=3:5519, p3=16:33838, p4=4:4644, m1=36:38706, m2=64:34588, y=100:7805)
- Layer 36: `羊`, `berg`, `分解`, ` Rip`, ` talags` (target ranks: p1=12:11815, p2=3:22624, p3=16:75991, p4=4:16075, m1=36:61081, m2=64:61826, y=100:6166)
- Layer 37: `}<?`, ` talags`, `acos`, `滴`, `轨迹` (target ranks: p1=12:24774, p2=3:60002, p3=16:107624, p4=4:45782, m1=36:103374, m2=64:98313, y=100:16332)
- Layer 38: `}<?`, ` talags`, `迷惑`, `坏`, `hemer` (target ranks: p1=12:38020, p2=3:84746, p3=16:120943, p4=4:73142, m1=36:117410, m2=64:115821, y=100:31777)
- Layer 39: `}<?`, `迷惑`, ` talags`, `𝑋`, `�` (target ranks: p1=12:82761, p2=3:108360, p3=16:121422, p4=4:108617, m1=36:116019, m2=64:117167, y=100:76120)
- Layer 40: ` x`, ` talags`, ` nasod`, ` X`, `тельными` (target ranks: p1=12:41119, p2=3:59557, p3=16:103060, p4=4:56283, m1=36:93102, m2=64:101508, y=100:36911)
- Layer 41: ` .`, `鹉`, `坏`, `省略`, `<｜end▁of▁sentence｜>` (target ranks: p1=12:27552, p2=3:14458, p3=16:73063, p4=4:21958, m1=36:64896, m2=64:69082, y=100:7258)

### Filler position 6 (absolute token 738, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126363, p2=3:128374, p3=16:126010, p4=4:128286, m1=36:124908, m2=64:126288, y=100:124537)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=12:9907, p2=3:3938, p3=16:9864, p4=4:4209, m1=36:11535, m2=64:13000, y=100:17807)
- Layer 20: `答案`, `�`, ` answer`, `试一试`, ` unflagged` (target ranks: p1=12:80982, p2=3:61360, p3=16:60364, p4=4:48518, m1=36:75563, m2=64:62639, y=100:14810)
- Layer 30: `推算`, `算出`, ` step`, ` calculator`, `分解` (target ranks: p1=12:9234, p2=3:8260, p3=16:13269, p4=4:5648, m1=36:22711, m2=64:27808, y=100:5122)
- Layer 35: ` step`, ` Step`, ` steps`, `acks`, ` STEP` (target ranks: p1=12:7168, p2=3:17965, p3=16:17568, p4=4:14198, m1=36:21216, m2=64:40216, y=100:14563)
- Layer 36: ` step`, ` Step`, ` pakig`, `Step`, ` Ta` (target ranks: p1=12:6859, p2=3:15318, p3=16:21593, p4=4:12922, m1=36:24150, m2=64:42915, y=100:8236)
- Layer 37: ` pakig`, ` step`, ` Step`, ` passo`, ` steps` (target ranks: p1=12:17153, p2=3:64256, p3=16:41661, p4=4:56788, m1=36:59695, m2=64:85893, y=100:14457)
- Layer 38: ` pakig`, ` Step`, ` step`, `一步步`, ` paso` (target ranks: p1=12:13436, p2=3:75537, p3=16:34398, p4=4:64013, m1=36:54029, m2=64:91678, y=100:15160)
- Layer 39: ` pakig`, `<｜begin▁of▁sentence｜>`, `}<?`, ` talags`, ` Rutherford` (target ranks: p1=12:47941, p2=3:115640, p3=16:53123, p4=4:121716, m1=36:118692, m2=64:119556, y=100:101694)
- Layer 40: ` pakig`, ` talags`, ` Fifteen`, ` fifteen`, `试一试` (target ranks: p1=12:10652, p2=3:59184, p3=16:20803, p4=4:83147, m1=36:106882, m2=64:102658, y=100:73794)
- Layer 41: ` .`, `试一试`, ` F`, ` Fifteen`, `一个一个` (target ranks: p1=12:13943, p2=3:20033, p3=16:41673, p4=4:42522, m1=36:102389, m2=64:95786, y=100:57669)

### Filler position 7 (absolute token 739, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126294, p2=3:128340, p3=16:125980, p4=4:128261, m1=36:124733, m2=64:126050, y=100:124259)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=12:8891, p2=3:3258, p3=16:8761, p4=4:3529, m1=36:10534, m2=64:11642, y=100:16539)
- Layer 20: `锁定`, `ait`, ` cheer`, `幽`, ` smile` (target ranks: p1=12:3811, p2=3:629, p3=16:3276, p4=4:550, m1=36:2797, m2=64:3437, y=100:5017)
- Layer 30: `69`, `79`, `yg`, `82`, `72` (target ranks: p1=12:870, p2=3:6017, p3=16:1555, p4=4:2351, m1=36:30, m2=64:17, y=100:44)
- Layer 35: ` labor`, `足`, ` lab`, ` colon`, `yg` (target ranks: p1=12:15179, p2=3:12082, p3=16:33749, p4=4:8304, m1=36:10844, m2=64:417, y=100:171)
- Layer 36: `138`, `159`, `139`, `158`, `110` (target ranks: p1=12:38497, p2=3:33543, p3=16:85752, p4=4:21293, m1=36:25954, m2=64:779, y=100:71)
- Layer 37: `158`, `138`, `156`, `159`, `110` (target ranks: p1=12:69084, p2=3:72097, p3=16:99974, p4=4:60332, m1=36:41812, m2=64:4075, y=100:277)
- Layer 38: `}<?`, `本题分析`, `?datasetId`, ` mencap`, `ozygous` (target ranks: p1=12:76834, p2=3:104854, p3=16:115280, p4=4:96240, m1=36:85244, m2=64:33739, y=100:1560)
- Layer 39: `}<?`, ` pakig`, `东海`, `ozygous`, `opters` (target ranks: p1=12:78089, p2=3:115308, p3=16:105926, p4=4:112109, m1=36:91535, m2=64:26416, y=100:2405)
- Layer 40: ` drip`, ` pakig`, ` trick`, `留存`, ` talags` (target ranks: p1=12:42936, p2=3:71215, p3=16:79162, p4=4:72342, m1=36:55355, m2=64:6916, y=100:126)
- Layer 41: ` .`, `有的时候`, `有点`, ` `, `满足了` (target ranks: p1=12:11817, p2=3:7017, p3=16:46914, p4=4:19988, m1=36:34144, m2=64:4474, y=100:109)

### Filler position 8 (absolute token 740, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126187, p2=3:128295, p3=16:125942, p4=4:128222, m1=36:124613, m2=64:125918, y=100:124207)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: p1=12:8847, p2=3:3272, p3=16:8702, p4=4:3505, m1=36:10363, m2=64:11445, y=100:16227)
- Layer 20: `锁定`, `ait`, ` smile`, `胃癌`, ` Walker` (target ranks: p1=12:6147, p2=3:1444, p3=16:4521, p4=4:802, m1=36:4425, m2=64:5084, y=100:10355)
- Layer 30: `acos`, `Tap`, `tap`, ` tap`, ` Tap` (target ranks: p1=12:28324, p2=3:35713, p3=16:16018, p4=4:14766, m1=36:3070, m2=64:33325, y=100:28096)
- Layer 35: ` tap`, `Tap`, `acos`, ` Tap`, `tap` (target ranks: p1=12:2270, p2=3:8417, p3=16:8146, p4=4:1295, m1=36:3124, m2=64:12207, y=100:29411)
- Layer 36: ` tap`, ` Tap`, `Tap`, `输入的`, `ereg` (target ranks: p1=12:987, p2=3:4573, p3=16:6283, p4=4:527, m1=36:1356, m2=64:6267, y=100:7920)
- Layer 37: `acos`, `}<?`, `anium`, `瞧着`, `ereg` (target ranks: p1=12:5027, p2=3:35872, p3=16:14640, p4=4:7088, m1=36:6429, m2=64:26560, y=100:14495)
- Layer 38: `}<?`, `�`, `瞧着`, ` complicate`, `本题分析` (target ranks: p1=12:11268, p2=3:59736, p3=16:33266, p4=4:21578, m1=36:17457, m2=64:52610, y=100:30571)
- Layer 39: `}<?`, ` consonant`, `东海`, ` talags`, `把事情` (target ranks: p1=12:28327, p2=3:82248, p3=16:56705, p4=4:81323, m1=36:60359, m2=64:68079, y=100:61562)
- Layer 40: ` .`, `留存`, `语言文字`, `试一试`, `šk` (target ranks: p1=12:1588, p2=3:14097, p3=16:14769, p4=4:15697, m1=36:21219, m2=64:26393, y=100:20828)
- Layer 41: ` .`, `试一试`, `有下列`, `<｜end▁of▁sentence｜>`, `秆` (target ranks: p1=12:2696, p2=3:5221, p3=16:19694, p4=4:8921, m1=36:19158, m2=64:30276, y=100:24015)

### Filler position 9 (absolute token 741, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=12:126203, p2=3:128308, p3=16:125967, p4=4:128237, m1=36:124602, m2=64:125892, y=100:124131)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `挪` (target ranks: p1=12:8607, p2=3:3095, p3=16:8499, p4=4:3420, m1=36:10381, m2=64:11439, y=100:15681)
- Layer 20: `锁定`, `ait`, `能被`, ` Walker`, `距` (target ranks: p1=12:5846, p2=3:1209, p3=16:4560, p4=4:1020, m1=36:5074, m2=64:5573, y=100:10502)
- Layer 30: `acos`, ` Heim`, ` expecting`, ` receptive`, `Tap` (target ranks: p1=12:6244, p2=3:14974, p3=16:4630, p4=4:2861, m1=36:1467, m2=64:1637, y=100:24309)
- Layer 35: `Tap`, ` tap`, `tap`, ` Tap`, ` colon` (target ranks: p1=12:3870, p2=3:7816, p3=16:1814, p4=4:1951, m1=36:126, m2=64:11, y=100:2890)
- Layer 36: `期望`, `83`, ` Vo`, `86`, `石榴` (target ranks: p1=12:42183, p2=3:31173, p3=16:49839, p4=4:9900, m1=36:1939, m2=64:55, y=100:1007)
- Layer 37: `}<?`, `覆`, `oze`, ` complicate`, `关` (target ranks: p1=12:82711, p2=3:85417, p3=16:77861, p4=4:60412, m1=36:9985, m2=64:1020, y=100:14176)
- Layer 38: `}<?`, `覆`, `oze`, `osos`, `打包` (target ranks: p1=12:96705, p2=3:105628, p3=16:104835, p4=4:80432, m1=36:34557, m2=64:6487, y=100:28342)
- Layer 39: `}<?`, `替换`, `ozygous`, ` eighty`, `覆` (target ranks: p1=12:87507, p2=3:106626, p3=16:111872, p4=4:97414, m1=36:72391, m2=64:6483, y=100:9083)
- Layer 40: ` eighty`, `}<?`, ` reper`, ` .`, ` ninety` (target ranks: p1=12:44852, p2=3:51991, p3=16:88947, p4=4:37461, m1=36:36951, m2=64:2151, y=100:1622)
- Layer 41: ` .`, `鹉`, ` beginning`, ` .↵↵`, ` ...` (target ranks: p1=12:50500, p2=3:19708, p3=16:84187, p4=4:23408, m1=36:52151, m2=64:9922, y=100:5279)

### Filler position 10 (absolute token 742, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=12:126376, p2=3:128403, p3=16:126158, p4=4:128311, m1=36:124741, m2=64:126064, y=100:124280)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `挪` (target ranks: p1=12:8528, p2=3:3165, p3=16:8388, p4=4:3433, m1=36:10234, m2=64:11357, y=100:15829)
- Layer 20: ` Walker`, `ait`, `锁定`, `挪`, ` smile` (target ranks: p1=12:8297, p2=3:5823, p3=16:8474, p4=4:4601, m1=36:10829, m2=64:10212, y=100:17514)
- Layer 30: ` sequential`, `Sequ`, `sequential`, `重复`, ` repeated` (target ranks: p1=12:12518, p2=3:24462, p3=16:18596, p4=4:16114, m1=36:39984, m2=64:19946, y=100:34640)
- Layer 35: ` sequential`, `sequential`, `Sequ`, ` repetition`, `分解` (target ranks: p1=12:5263, p2=3:12719, p3=16:7876, p4=4:10306, m1=36:17006, m2=64:11540, y=100:24561)
- Layer 36: `sequential`, ` sequential`, ` sequence`, ` linear`, `Sequ` (target ranks: p1=12:7962, p2=3:40183, p3=16:22532, p4=4:31191, m1=36:29885, m2=64:19481, y=100:22870)
- Layer 37: `sequence`, `sequential`, ` sequence`, ` sequential`, `sequences` (target ranks: p1=12:19842, p2=3:88302, p3=16:38591, p4=4:79508, m1=36:62484, m2=64:45066, y=100:44605)
- Layer 38: `linear`, `}<?`, `sequence`, ` linear`, `sequences` (target ranks: p1=12:32230, p2=3:99669, p3=16:62835, p4=4:97012, m1=36:67282, m2=64:52816, y=100:43138)
- Layer 39: `}<?`, `sequence`, `替换`, `olina`, `zat` (target ranks: p1=12:56547, p2=3:115049, p3=16:99827, p4=4:119643, m1=36:101372, m2=64:88502, y=100:68929)
- Layer 40: ` talags`, `程序的`, ` filler`, `程序`, `程序中` (target ranks: p1=12:15418, p2=3:75829, p3=16:68787, p4=4:81929, m1=36:56760, m2=64:58900, y=100:39211)
- Layer 41: ` .`, `程序`, `程序的`, `程序中`, ` without` (target ranks: p1=12:5443, p2=3:17533, p3=16:49480, p4=4:21719, m1=36:50856, m2=64:39651, y=100:29780)

### Filler position 11 (absolute token 743, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126662, p2=3:128525, p3=16:126453, p4=4:128441, m1=36:124969, m2=64:126398, y=100:124838)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `挪` (target ranks: p1=12:9326, p2=3:3212, p3=16:8778, p4=4:3480, m1=36:10615, m2=64:11948, y=100:16384)
- Layer 20: `锁定`, ` wig`, ` smile`, ` Walker`, `ait` (target ranks: p1=12:7645, p2=3:1850, p3=16:6606, p4=4:1300, m1=36:6175, m2=64:7674, y=100:8183)
- Layer 30: `Tap`, `tap`, ` tap`, `打完`, ` Tap` (target ranks: p1=12:18740, p2=3:30702, p3=16:18139, p4=4:13067, m1=36:5866, m2=64:33738, y=100:5884)
- Layer 35: ` tap`, `radesh`, `Tap`, ` Tap`, `tap` (target ranks: p1=12:2646, p2=3:21313, p3=16:16202, p4=4:3263, m1=36:11975, m2=64:28224, y=100:10547)
- Layer 36: `radesh`, ` tap`, `期望`, `打完`, ` Zad` (target ranks: p1=12:1967, p2=3:13891, p3=16:14943, p4=4:1534, m1=36:10951, m2=64:21569, y=100:4478)
- Layer 37: ` Erkännande`, `}<?`, `radesh`, `坏`, ` competit` (target ranks: p1=12:6964, p2=3:56838, p3=16:34027, p4=4:18472, m1=36:35274, m2=64:58170, y=100:10306)
- Layer 38: `}<?`, `ozygous`, ` Erkännande`, `radesh`, `�` (target ranks: p1=12:22585, p2=3:82852, p3=16:61851, p4=4:40351, m1=36:56010, m2=64:74104, y=100:15597)
- Layer 39: `}<?`, ` consonant`, `ozygous`, `繁体`, `叶子` (target ranks: p1=12:54585, p2=3:106931, p3=16:84093, p4=4:111079, m1=36:92351, m2=64:87351, y=100:55255)
- Layer 40: `坏`, ` .`, ` nasod`, `试一试`, ` filler` (target ranks: p1=12:5079, p2=3:31006, p3=16:27464, p4=4:44034, m1=36:38998, m2=64:38519, y=100:13661)
- Layer 41: ` .`, `秆`, `<｜end▁of▁sentence｜>`, ` `, `试一试` (target ranks: p1=12:4941, p2=3:11151, p3=16:29149, p4=4:25491, m1=36:31146, m2=64:34511, y=100:10510)

### Filler position 12 (absolute token 744, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126682, p2=3:128509, p3=16:126426, p4=4:128451, m1=36:124885, m2=64:126402, y=100:124605)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=12:9169, p2=3:2950, p3=16:8315, p4=4:3256, m1=36:10010, m2=64:11617, y=100:16183)
- Layer 20: `ait`, `锁定`, ` smile`, ` wig`, ` Walker` (target ranks: p1=12:8840, p2=3:3173, p3=16:7257, p4=4:1865, m1=36:8425, m2=64:7187, y=100:13258)
- Layer 30: `Tap`, ` tap`, `tap`, ` Tap`, `打完` (target ranks: p1=12:16660, p2=3:22629, p3=16:19374, p4=4:10801, m1=36:2688, m2=64:17607, y=100:3969)
- Layer 35: ` met`, ` tap`, `acks`, `acin`, ` anxious` (target ranks: p1=12:2615, p2=3:11546, p3=16:13275, p4=4:3190, m1=36:5154, m2=64:11616, y=100:9117)
- Layer 36: `adal`, `期望`, ` tap`, `acin`, ` familiar` (target ranks: p1=12:1514, p2=3:6525, p3=16:11510, p4=4:1218, m1=36:4683, m2=64:7584, y=100:3771)
- Layer 37: `坏`, `等待着`, `等着`, `冰冰`, `acet` (target ranks: p1=12:4703, p2=3:43862, p3=16:30020, p4=4:14933, m1=36:23065, m2=64:29903, y=100:6225)
- Layer 38: `}<?`, `坏`, `acons`, ` Erkännande`, `等待着` (target ranks: p1=12:19335, p2=3:83025, p3=16:72068, p4=4:50792, m1=36:51238, m2=64:62138, y=100:21251)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `hatic`, `东海`, `ocyst` (target ranks: p1=12:58363, p2=3:108740, p3=16:89383, p4=4:112453, m1=36:84247, m2=64:75818, y=100:53870)
- Layer 40: `坏`, ` ANSWER`, ` wait`, ` Answer`, `等待` (target ranks: p1=12:10177, p2=3:39944, p3=16:40373, p4=4:55692, m1=36:33228, m2=64:33640, y=100:15487)
- Layer 41: ` .`, `等待`, `Answer`, `试一试`, ` a` (target ranks: p1=12:5684, p2=3:12292, p3=16:26210, p4=4:26231, m1=36:18219, m2=64:25069, y=100:13828)

### Filler position 13 (absolute token 745, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126967, p2=3:128620, p3=16:126671, p4=4:128574, m1=36:125220, m2=64:126792, y=100:124995)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=12:9233, p2=3:3274, p3=16:8748, p4=4:3663, m1=36:10770, m2=64:11525, y=100:15748)
- Layer 20: `锁定`, `忑`, `ait`, ` Walker`, `Walker` (target ranks: p1=12:15980, p2=3:7558, p3=16:11567, p4=4:6431, m1=36:16689, m2=64:12673, y=100:16893)
- Layer 30: ` calculator`, `鞍`, ` labor`, `平行`, ` Calculator` (target ranks: p1=12:40701, p2=3:21515, p3=16:14346, p4=4:17052, m1=36:13012, m2=64:11018, y=100:16136)
- Layer 35: ` calculator`, ` Arithmetic`, ` arithmetic`, ` labor`, `锁定` (target ranks: p1=12:7947, p2=3:5527, p3=16:4027, p4=4:2999, m1=36:3391, m2=64:4539, y=100:4991)
- Layer 36: ` program`, ` calculator`, ` tap`, `Tasks`, ` equations` (target ranks: p1=12:11239, p2=3:7841, p3=16:7049, p4=4:3527, m1=36:3232, m2=64:5141, y=100:3313)
- Layer 37: ` program`, `程序的`, ` arithmetic`, `程序`, ` Arithmetic` (target ranks: p1=12:31469, p2=3:36380, p3=16:19045, p4=4:27109, m1=36:8192, m2=64:21311, y=100:10371)
- Layer 38: `程序的`, ` arithmetic`, `程序`, ` program`, ` Arithmetic` (target ranks: p1=12:48904, p2=3:50076, p3=16:33281, p4=4:41293, m1=36:12787, m2=64:29711, y=100:21926)
- Layer 39: `}<?`, `坏的`, `覆`, `下沉`, `坏` (target ranks: p1=12:74133, p2=3:96892, p3=16:79262, p4=4:102932, m1=36:63714, m2=64:86006, y=100:50215)
- Layer 40: `坏的`, `坏`, `下沉`, `ark`, `脏` (target ranks: p1=12:23633, p2=3:39803, p3=16:48073, p4=4:55832, m1=36:32314, m2=64:45248, y=100:24067)
- Layer 41: ` .`, ` `, ` .↵↵`, `oooo`, ` awaiting` (target ranks: p1=12:16007, p2=3:12210, p3=16:54275, p4=4:30483, m1=36:33869, m2=64:50418, y=100:5984)

### Filler position 14 (absolute token 746, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=12:126997, p2=3:128646, p3=16:126749, p4=4:128601, m1=36:125287, m2=64:126892, y=100:125025)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:8256, p2=3:3221, p3=16:8038, p4=4:3445, m1=36:9790, m2=64:10586, y=100:15367)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `拆` (target ranks: p1=12:10959, p2=3:5181, p3=16:6217, p4=4:3538, m1=36:10108, m2=64:8587, y=100:18061)
- Layer 30: `平行`, ` reserved`, ` step`, `acos`, ` Anthrop` (target ranks: p1=12:33726, p2=3:39202, p3=16:15632, p4=4:21228, m1=36:22742, m2=64:13677, y=100:49454)
- Layer 35: ` equations`, ` future`, `输入的`, ` reserved`, `锁定` (target ranks: p1=12:6599, p2=3:10422, p3=16:3878, p4=4:4364, m1=36:7579, m2=64:5050, y=100:17050)
- Layer 36: `柿子`, `输入的`, ` equations`, `俯`, ` initial` (target ranks: p1=12:20080, p2=3:35897, p3=16:11937, p4=4:13785, m1=36:13511, m2=64:14709, y=100:23675)
- Layer 37: `}<?`, `变量的`, `variables`, ` initial`, ` variables` (target ranks: p1=12:59094, p2=3:105673, p3=16:38951, p4=4:80096, m1=36:50702, m2=64:67767, y=100:73468)
- Layer 38: `}<?`, `文字的`, `ِّف`, `变量的`, `variables` (target ranks: p1=12:59837, p2=3:112415, p3=16:54714, p4=4:89211, m1=36:64859, m2=64:79826, y=100:89755)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` talags`, `}<?`, `文字的`, `替换` (target ranks: p1=12:93316, p2=3:115988, p3=16:95787, p4=4:114423, m1=36:93212, m2=64:107851, y=100:93421)
- Layer 40: ` talags`, `scr`, ` .`, `下沉`, `变量的` (target ranks: p1=12:39498, p2=3:58841, p3=16:54447, p4=4:57365, m1=36:51348, m2=64:70409, y=100:55473)
- Layer 41: ` .`, ` dotted`, ` assignment`, ` `, `那两个` (target ranks: p1=12:39756, p2=3:19154, p3=16:52822, p4=4:27914, m1=36:41051, m2=64:64519, y=100:40326)

### Filler position 15 (absolute token 747, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=12:126998, p2=3:128641, p3=16:126754, p4=4:128594, m1=36:125254, m2=64:126789, y=100:124836)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:8328, p2=3:3059, p3=16:8051, p4=4:3303, m1=36:9823, m2=64:10880, y=100:15067)
- Layer 20: `ait`, `锁定`, `能被`, ` smile`, `cape` (target ranks: p1=12:5035, p2=3:1080, p3=16:2562, p4=4:794, m1=36:3714, m2=64:3824, y=100:9674)
- Layer 30: `第一步`, `算出`, ` dy`, ` step`, `acos` (target ranks: p1=12:8095, p2=3:19062, p3=16:12072, p4=4:7731, m1=36:6791, m2=64:3271, y=100:26366)
- Layer 35: ` dy`, ` reserved`, ` step`, `ession`, `分解` (target ranks: p1=12:117, p2=3:5172, p3=16:679, p4=4:2252, m1=36:1135, m2=64:907, y=100:13378)
- Layer 36: `留存`, `分解`, ` reserved`, `俯`, `ession` (target ranks: p1=12:217, p2=3:12724, p3=16:2321, p4=4:5395, m1=36:2922, m2=64:2666, y=100:18537)
- Layer 37: `acos`, `留存`, `珍珠`, ` Seventh`, `不加` (target ranks: p1=12:187, p2=3:65209, p3=16:10433, p4=4:44839, m1=36:8751, m2=64:13568, y=100:69431)
- Layer 38: `}<?`, `本题分析`, `珍珠`, `不加`, `actors` (target ranks: p1=12:2562, p2=3:104707, p3=16:45305, p4=4:89853, m1=36:35933, m2=64:52291, y=100:100587)
- Layer 39: `}<?`, ` twelve`, `替换`, `迷惑`, `opters` (target ranks: p1=12:212, p2=3:112726, p3=16:93491, p4=4:109532, m1=36:40883, m2=64:83090, y=100:98807)
- Layer 40: ` twelve`, ` Twelve`, `12`, `留存`, ` udalerria` (target ranks: p1=12:3, p2=3:60726, p3=16:61862, p4=4:53316, m1=36:9086, m2=64:45013, y=100:57042)
- Layer 41: ` .`, `步骤如下`, `试一试`, ` twelve`, `转载请` (target ranks: p1=12:17, p2=3:22836, p3=16:68408, p4=4:34095, m1=36:14595, m2=64:63260, y=100:48409)

### Filler position 16 (absolute token 748, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=12:126989, p2=3:128666, p3=16:126775, p4=4:128606, m1=36:125286, m2=64:126841, y=100:124933)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:9811, p2=3:3910, p3=16:9300, p4=4:4068, m1=36:11213, m2=64:12563, y=100:16783)
- Layer 20: `ait`, `锁定`, ` smile`, `能被`, ` LS` (target ranks: p1=12:3512, p2=3:804, p3=16:2881, p4=4:435, m1=36:2195, m2=64:2896, y=100:10447)
- Layer 30: `交替`, ` expecting`, `柿子`, `acos`, `粥` (target ranks: p1=12:3252, p2=3:16630, p3=16:2597, p4=4:1904, m1=36:851, m2=64:1056, y=100:71536)
- Layer 35: `32`, `68`, `adak`, `八十`, `44` (target ranks: p1=12:4341, p2=3:44065, p3=16:1263, p4=4:33266, m1=36:135, m2=64:28, y=100:61106)
- Layer 36: ` ---|---|---|---|---|---|---`, `44`, `八十`, ` Berl`, `本题分析` (target ranks: p1=12:47607, p2=3:91140, p3=16:34285, p4=4:58617, m1=36:786, m2=64:116, y=100:55471)
- Layer 37: `本题分析`, ` Parehong`, `44`, `八十`, `osz` (target ranks: p1=12:69732, p2=3:108358, p3=16:55885, p4=4:88765, m1=36:2601, m2=64:395, y=100:84597)
- Layer 38: `44`, `八十`, `osz`, `总管`, `68` (target ranks: p1=12:82586, p2=3:117907, p3=16:53799, p4=4:86192, m1=36:2347, m2=64:214, y=100:76028)
- Layer 39: `92`, `68`, `八十`, ` Berl`, ` Hardy` (target ranks: p1=12:73411, p2=3:124997, p3=16:90424, p4=4:109271, m1=36:23457, m2=64:378, y=100:27576)
- Layer 40: ` eighty`, `八十`, ` Eighty`, `告辞`, `92` (target ranks: p1=12:71256, p2=3:119967, p3=16:95189, p4=4:94726, m1=36:10110, m2=64:278, y=100:24524)
- Layer 41: `告辞`, ` assumption`, ` .`, `oslov`, `培养了` (target ranks: p1=12:38119, p2=3:51223, p3=16:77572, p4=4:76170, m1=36:32553, m2=64:6625, y=100:31976)

### Filler position 17 (absolute token 749, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=12:126840, p2=3:128613, p3=16:126668, p4=4:128553, m1=36:125036, m2=64:126642, y=100:124802)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=12:11143, p2=3:4572, p3=16:10617, p4=4:5032, m1=36:12717, m2=64:14598, y=100:17505)
- Layer 20: `锁定`, ` smile`, `ession`, `cape`, ` emot` (target ranks: p1=12:7465, p2=3:2457, p3=16:3737, p4=4:2032, m1=36:4414, m2=64:8568, y=100:9445)
- Layer 30: `acos`, `冰`, `柿子`, `�`, `冰冻` (target ranks: p1=12:16078, p2=3:67314, p3=16:7096, p4=4:10480, m1=36:1456, m2=64:8521, y=100:42314)
- Layer 35: ` labor`, ` vertical`, ` repetition`, `tap`, ` tap` (target ranks: p1=12:841, p2=3:18985, p3=16:2267, p4=4:3155, m1=36:8, m2=64:369, y=100:8371)
- Layer 36: `大方`, `坏`, `覆`, `}<?`, ` finishing` (target ranks: p1=12:13683, p2=3:79940, p3=16:21240, p4=4:12970, m1=36:10, m2=64:89, y=100:6837)
- Layer 37: `在北京`, `}<?`, `cault`, ` Quizlet`, ` peas` (target ranks: p1=12:29483, p2=3:114291, p3=16:31193, p4=4:49347, m1=36:502, m2=64:1679, y=100:38996)
- Layer 38: `}<?`, ` peas`, `cault`, `桃子`, `在北京` (target ranks: p1=12:42509, p2=3:120802, p3=16:39332, p4=4:49848, m1=36:3072, m2=64:1581, y=100:34597)
- Layer 39: `}<?`, ` peas`, `东海`, `桃子`, ` Zel` (target ranks: p1=12:78548, p2=3:121350, p3=16:88923, p4=4:113365, m1=36:15517, m2=64:522, y=100:11616)
- Layer 40: ` .`, `acular`, `省略`, ` Seventy`, ` eighty` (target ranks: p1=12:46020, p2=3:94585, p3=16:76328, p4=4:74603, m1=36:15549, m2=64:465, y=100:2830)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, ` because` (target ranks: p1=12:23635, p2=3:21339, p3=16:51575, p4=4:34044, m1=36:13233, m2=64:2242, y=100:2463)

### Filler position 18 (absolute token 750, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=12:127130, p2=3:128727, p3=16:126963, p4=4:128664, m1=36:125376, m2=64:126952, y=100:125322)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:9687, p2=3:3592, p3=16:8938, p4=4:3814, m1=36:10762, m2=64:12382, y=100:16986)
- Layer 20: `忑`, `锁定`, `ait`, ` smile`, ` Walker` (target ranks: p1=12:8442, p2=3:3859, p3=16:6075, p4=4:2867, m1=36:6692, m2=64:9408, y=100:17708)
- Layer 30: `平行`, `atan`, `鞍`, ` dy`, `禀` (target ranks: p1=12:16117, p2=3:18172, p3=16:7845, p4=4:6837, m1=36:9284, m2=64:8001, y=100:29469)
- Layer 35: ` repetition`, ` quadr`, `重复`, ` var`, ` repetitions` (target ranks: p1=12:4253, p2=3:7893, p3=16:1799, p4=4:3273, m1=36:4126, m2=64:5468, y=100:19509)
- Layer 36: `acin`, ` quadr`, `重复`, `adal`, ` repetition` (target ranks: p1=12:9771, p2=3:27333, p3=16:5705, p4=4:10206, m1=36:5766, m2=64:10656, y=100:17246)
- Layer 37: `}<?`, `acos`, ` concaten`, `下沉`, `班的` (target ranks: p1=12:45758, p2=3:98743, p3=16:31753, p4=4:73030, m1=36:28084, m2=64:63753, y=100:59389)
- Layer 38: `}<?`, `zat`, `不加`, `下沉`, `dividers` (target ranks: p1=12:68036, p2=3:115015, p3=16:63619, p4=4:94173, m1=36:51157, m2=64:90489, y=100:85390)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `东海`, `迷惑`, `zat` (target ranks: p1=12:65442, p2=3:117058, p3=16:83540, p4=4:120075, m1=36:65431, m2=64:97880, y=100:78162)
- Layer 40: `}<?`, ` .`, ` udalerria`, `acular`, `程序的` (target ranks: p1=12:16469, p2=3:69080, p3=16:46393, p4=4:84140, m1=36:21026, m2=64:63629, y=100:36227)
- Layer 41: ` .`, ` assignment`, ` `, ` assembly`, `acular` (target ranks: p1=12:14578, p2=3:34981, p3=16:55017, p4=4:54503, m1=36:28542, m2=64:60094, y=100:35148)

### Filler position 19 (absolute token 751, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `Noiz`, `aplenty` (target ranks: p1=12:127467, p2=3:128831, p3=16:127214, p4=4:128788, m1=36:125825, m2=64:127250, y=100:125645)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:9202, p2=3:3206, p3=16:8471, p4=4:3451, m1=36:10682, m2=64:11579, y=100:15409)
- Layer 20: ` Walker`, `ait`, `忑`, `锁定`, `Walker` (target ranks: p1=12:15152, p2=3:5790, p3=16:7693, p4=4:5996, m1=36:11514, m2=64:11413, y=100:18654)
- Layer 30: `平行`, ` parallel`, `重复`, ` repetitions`, ` exercises` (target ranks: p1=12:21272, p2=3:14027, p3=16:9859, p4=4:11491, m1=36:23460, m2=64:18746, y=100:28198)
- Layer 35: ` repetition`, ` quadr`, `平行`, ` repetitions`, ` exercises` (target ranks: p1=12:8301, p2=3:7486, p3=16:1615, p4=4:7079, m1=36:11318, m2=64:9008, y=100:18785)
- Layer 36: ` quadr`, ` parallel`, ` Type`, ` pattern`, `重复` (target ranks: p1=12:12053, p2=3:17288, p3=16:3675, p4=4:15813, m1=36:14096, m2=64:9698, y=100:9009)
- Layer 37: ` pattern`, ` multipliers`, ` concaten`, `加法`, `加减` (target ranks: p1=12:27460, p2=3:71076, p3=16:10089, p4=4:64809, m1=36:39661, m2=64:46273, y=100:25090)
- Layer 38: `}<?`, ` multipliers`, `mul`, ` multiplier`, ` pattern` (target ranks: p1=12:49515, p2=3:99315, p3=16:26981, p4=4:94759, m1=36:64690, m2=64:69231, y=100:40942)
- Layer 39: `}<?`, `mul`, ` Mul`, `Mul`, ` mul` (target ranks: p1=12:51472, p2=3:112830, p3=16:59423, p4=4:116569, m1=36:84836, m2=64:70942, y=100:45267)
- Layer 40: `程序的`, ` program`, `}<?`, ` p`, ` udalerria` (target ranks: p1=12:11591, p2=3:64691, p3=16:31416, p4=4:71357, m1=36:27744, m2=64:36947, y=100:17653)
- Layer 41: ` .`, ` program`, `程序的`, `那颗`, `不求` (target ranks: p1=12:6626, p2=3:32029, p3=16:44140, p4=4:38986, m1=36:30018, m2=64:40308, y=100:10867)

### Filler position 20 (absolute token 752, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `-ulo`, `aplenty` (target ranks: p1=12:127650, p2=3:128893, p3=16:127396, p4=4:128857, m1=36:126115, m2=64:127540, y=100:125908)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=12:9711, p2=3:3645, p3=16:9175, p4=4:3912, m1=36:11562, m2=64:11864, y=100:15931)
- Layer 20: `ait`, ` Walker`, `平行`, ` engaging`, `锁定` (target ranks: p1=12:20238, p2=3:11378, p3=16:13036, p4=4:11099, m1=36:17741, m2=64:14898, y=100:22243)
- Layer 30: `清楚楚`, ` calculator`, `sl`, `算出`, `分解` (target ranks: p1=12:8722, p2=3:19212, p3=16:16323, p4=4:12690, m1=36:10561, m2=64:21063, y=100:24348)
- Layer 35: ` calculator`, `分解`, ` met`, ` p`, `calcul` (target ranks: p1=12:931, p2=3:7130, p3=16:2245, p4=4:6693, m1=36:2247, m2=64:7665, y=100:8713)
- Layer 36: `留存`, `分解`, `calcul`, `俯`, ` calculator` (target ranks: p1=12:1313, p2=3:17066, p3=16:4098, p4=4:14928, m1=36:3341, m2=64:9131, y=100:4572)
- Layer 37: `calcul`, ` p`, `计算的`, `俯`, ` Calculators` (target ranks: p1=12:4917, p2=3:71762, p3=16:9146, p4=4:64548, m1=36:9459, m2=64:32779, y=100:14542)
- Layer 38: ` p`, `calcul`, `计算的`, `进行计算`, `}<?` (target ranks: p1=12:9148, p2=3:93919, p3=16:19590, p4=4:84918, m1=36:14793, m2=64:34156, y=100:22606)
- Layer 39: `}<?`, ` p`, `p`, `迷惑`, `?datasetId` (target ranks: p1=12:20734, p2=3:106320, p3=16:47722, p4=4:107256, m1=36:40049, m2=64:61126, y=100:30626)
- Layer 40: ` p`, `p`, `y`, `留存`, ` cascade` (target ranks: p1=12:5433, p2=3:67244, p3=16:27133, p4=4:65450, m1=36:19065, m2=64:31063, y=100:18591)
- Layer 41: ` .`, ` `, `鹉`, `y`, ` .↵↵` (target ranks: p1=12:2081, p2=3:18106, p3=16:11974, p4=4:18190, m1=36:13766, m2=64:26953, y=100:6327)

### Filler position 21 (absolute token 753, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=12:127586, p2=3:128889, p3=16:127357, p4=4:128837, m1=36:126091, m2=64:127391, y=100:125877)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=12:9467, p2=3:3450, p3=16:8927, p4=4:3793, m1=36:11519, m2=64:11951, y=100:15548)
- Layer 20: ` biotic`, ` TA`, `俯`, ` Corporation`, `corpor` (target ranks: p1=12:38760, p2=3:22190, p3=16:31489, p4=4:34388, m1=36:44904, m2=64:32165, y=100:19608)
- Layer 30: `}using`, `dividers`, `}<?`, `acos`, ` dekameters` (target ranks: p1=12:90440, p2=3:116002, p3=16:88936, p4=4:113545, m1=36:58302, m2=64:73895, y=100:83862)
- Layer 35: `二十二`, `}using`, `滴水`, `dividers`, ` twenty` (target ranks: p1=12:34175, p2=3:87318, p3=16:48829, p4=4:95112, m1=36:12598, m2=64:69477, y=100:42282)
- Layer 36: `陌生`, `滴水`, ` reserved`, `俯`, `反复` (target ranks: p1=12:13875, p2=3:31952, p3=16:26270, p4=4:39491, m1=36:3941, m2=64:22870, y=100:16344)
- Layer 37: `}<?`, ` covari`, `坏`, `onana`, `放下了` (target ranks: p1=12:57789, p2=3:84784, p3=16:53224, p4=4:85117, m1=36:20143, m2=64:50993, y=100:42930)
- Layer 38: ` .`, ` covari`, `坏`, ` club`, ` .↵↵` (target ranks: p1=12:19156, p2=3:57233, p3=16:13617, p4=4:57120, m1=36:5840, m2=64:26787, y=100:18040)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `坏`, `斐`, ` covari` (target ranks: p1=12:41595, p2=3:103888, p3=16:60094, p4=4:102000, m1=36:26243, m2=64:53305, y=100:34673)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵`, `�` (target ranks: p1=12:12420, p2=3:48430, p3=16:25435, p4=4:53934, m1=36:7821, m2=64:19506, y=100:12511)
- Layer 41: ` .`, ` .↵↵`, `这就是`, ` .↵`, `坏` (target ranks: p1=12:3417, p2=3:6396, p3=16:7972, p4=4:7057, m1=36:2994, m2=64:14385, y=100:3891)

### Filler position 22 (absolute token 754, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=12:127830, p2=3:128978, p3=16:127656, p4=4:128928, m1=36:126393, m2=64:127623, y=100:126165)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: p1=12:8744, p2=3:3152, p3=16:8256, p4=4:3312, m1=36:10433, m2=64:11074, y=100:15475)
- Layer 20: ` quadr`, `同步`, `cape`, ` smile`, `auce` (target ranks: p1=12:236, p2=3:105, p3=16:494, p4=4:37, m1=36:151, m2=64:435, y=100:1314)
- Layer 30: `Quintal`, `东京`, `AssemblyVersion`, `}<?`, `opters` (target ranks: p1=12:9405, p2=3:104192, p3=16:10223, p4=4:37956, m1=36:2206, m2=64:22842, y=100:89958)
- Layer 35: ` sixteen`, `216`, `24`, `三十六`, `36` (target ranks: p1=12:263, p2=3:78987, p3=16:7, p4=4:65730, m1=36:5, m2=64:197, y=100:86590)
- Layer 36: `三十六`, `36`, `二十四`, `七十二`, `24` (target ranks: p1=12:18932, p2=3:112368, p3=16:16616, p4=4:97472, m1=36:2, m2=64:40, y=100:71925)
- Layer 37: `三十六`, `36`, `桃子`, `七十二`, ` Quizlet` (target ranks: p1=12:30299, p2=3:116544, p3=16:17865, p4=4:102131, m1=36:2, m2=64:97, y=100:101897)
- Layer 38: `三十六`, `48`, `七十二`, `桃子`, `齐` (target ranks: p1=12:47172, p2=3:123458, p3=16:56183, p4=4:109354, m1=36:13, m2=64:31, y=100:93100)
- Layer 39: `}<?`, `七十二`, `桃子`, `72`, `76` (target ranks: p1=12:58273, p2=3:125489, p3=16:53375, p4=4:121505, m1=36:426, m2=64:14, y=100:23091)
- Layer 40: `七十二`, ` seventy`, ` eighty`, `72`, ` Seventy` (target ranks: p1=12:45925, p2=3:115701, p3=16:44791, p4=4:111827, m1=36:607, m2=64:12, y=100:10795)
- Layer 41: ` .`, `错过`, `错过了`, `到了`, `七十二` (target ranks: p1=12:12930, p2=3:14361, p3=16:19712, p4=4:53617, m1=36:2729, m2=64:40, y=100:12587)

### Filler position 23 (absolute token 755, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=12:127710, p2=3:128940, p3=16:127534, p4=4:128883, m1=36:126191, m2=64:127546, y=100:125944)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=12:8436, p2=3:2835, p3=16:7842, p4=4:3037, m1=36:10150, m2=64:10573, y=100:14802)
- Layer 20: `Dutch`, `吞`, ` Dutch`, `tered`, `iganos` (target ranks: p1=12:14020, p2=3:11892, p3=16:24706, p4=4:7932, m1=36:17484, m2=64:31488, y=100:10897)
- Layer 30: `codeline`, `东京`, ` ادام`, `okens`, `)Skip` (target ranks: p1=12:71591, p2=3:109050, p3=16:97813, p4=4:87867, m1=36:75896, m2=64:99053, y=100:55813)
- Layer 35: `codeline`, `坏`, `�`, ` nasod`, `删` (target ranks: p1=12:41443, p2=3:96190, p3=16:99946, p4=4:81132, m1=36:55683, m2=64:99000, y=100:44944)
- Layer 36: `坏`, ` nasod`, ` soci`, `停`, `/hess` (target ranks: p1=12:24360, p2=3:55954, p3=16:75691, p4=4:44832, m1=36:26517, m2=64:52927, y=100:13962)
- Layer 37: `镶嵌`, `肤`, ` tide`, `Quintal`, `贻` (target ranks: p1=12:78639, p2=3:98973, p3=16:107957, p4=4:61536, m1=36:64889, m2=64:100157, y=100:28314)
- Layer 38: `肤`, `锚`, ` germ`, `镶嵌`, ` .` (target ranks: p1=12:56333, p2=3:78788, p3=16:63405, p4=4:44083, m1=36:22940, m2=64:70590, y=100:23979)
- Layer 39: ` .`, `肤`, ` encomp`, ` .↵↵`, ` germ` (target ranks: p1=12:91847, p2=3:111492, p3=16:110563, p4=4:111147, m1=36:73374, m2=64:109845, y=100:41632)
- Layer 40: ` .`, ` .↵↵`, `肤`, ` .↵`, ` germ` (target ranks: p1=12:65902, p2=3:78491, p3=16:90295, p4=4:83367, m1=36:53551, m2=64:105321, y=100:21299)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, ` ,` (target ranks: p1=12:32583, p2=3:46890, p3=16:40043, p4=4:50814, m1=36:27460, m2=64:68229, y=100:6968)

### Filler position 24 (absolute token 756, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `aplenty` (target ranks: p1=12:127881, p2=3:129007, p3=16:127711, p4=4:128955, m1=36:126373, m2=64:127694, y=100:126274)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: p1=12:8349, p2=3:2884, p3=16:7587, p4=4:2976, m1=36:9585, m2=64:9965, y=100:14774)
- Layer 20: ` smile`, `cape`, `站`, ` grin`, ` Error` (target ranks: p1=12:539, p2=3:675, p3=16:849, p4=4:32, m1=36:376, m2=64:438, y=100:12458)
- Layer 30: `codeline`, `</think>`, ` Answer`, `oNames`, `答案` (target ranks: p1=12:79626, p2=3:118917, p3=16:109375, p4=4:103857, m1=36:97224, m2=64:73969, y=100:112590)
- Layer 35: `codeline`, ` Answer`, `AED`, ` tagged`, ` sleep` (target ranks: p1=12:18719, p2=3:86634, p3=16:104630, p4=4:83727, m1=36:85893, m2=64:81615, y=100:79666)
- Layer 36: ` nasod`, `坏`, ` Answer`, `良`, `微笑` (target ranks: p1=12:2493, p2=3:28057, p3=16:44188, p4=4:22965, m1=36:32737, m2=64:22244, y=100:30582)
- Layer 37: `codeline`, `hatic`, `oNames`, ` tagged`, `�` (target ranks: p1=12:99623, p2=3:118201, p3=16:114700, p4=4:101324, m1=36:113692, m2=64:115787, y=100:72426)
- Layer 38: `hatic`, `codeline`, `oNames`, ` retard`, `<|EOT|>` (target ranks: p1=12:107188, p2=3:120244, p3=16:120456, p4=4:106487, m1=36:102803, m2=64:114277, y=100:71065)
- Layer 39: `hatic`, `codeline`, ` begg`, `-ulo`, `deen` (target ranks: p1=12:65367, p2=3:121210, p3=16:113402, p4=4:114624, m1=36:64438, m2=64:85255, y=100:85993)
- Layer 40: ` Answer`, `Answer`, ` .↵↵`, `叮`, ` begg` (target ranks: p1=12:10134, p2=3:47113, p3=16:46436, p4=4:29919, m1=36:10705, m2=64:22011, y=100:25806)
- Layer 41: ` Answer`, ` .`, ` .↵↵`, `Answer`, ` begg` (target ranks: p1=12:2088, p2=3:12923, p3=16:8830, p4=4:6734, m1=36:5104, m2=64:10288, y=100:12668)

### Filler position 25 (absolute token 757, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `EDMF` (target ranks: p1=12:122639, p2=3:126764, p3=16:122444, p4=4:126603, m1=36:121542, m2=64:122250, y=100:115614)
- Layer 10: `eine`, `som`, `tas`, `ej`, `edited` (target ranks: p1=12:67842, p2=3:56258, p3=16:72562, p4=4:58405, m1=36:80953, m2=64:78597, y=100:10047)
- Layer 20: `鸯`, ` Submission`, `能被`, `平行`, `ait` (target ranks: p1=12:26509, p2=3:22668, p3=16:31839, p4=4:24306, m1=36:25974, m2=64:21532, y=100:42180)
- Layer 30: ` Paglin`, ` NK`, `malink`, `NK`, `nk` (target ranks: p1=12:53159, p2=3:121605, p3=16:27094, p4=4:114946, m1=36:11218, m2=64:12468, y=100:29821)
- Layer 35: ` Paglin`, `答案是`, ` Vale`, `回答`, ` المطلع` (target ranks: p1=12:84373, p2=3:120439, p3=16:27968, p4=4:116213, m1=36:53782, m2=64:6037, y=100:4322)
- Layer 36: ` Paglin`, `回答`, `答案`, ` answers`, ` answer` (target ranks: p1=12:50973, p2=3:90455, p3=16:27069, p4=4:73542, m1=36:40276, m2=64:2288, y=100:193)
- Layer 37: ` Paglin`, ` المطلع`, `malink`, ` premi`, `rinnings` (target ranks: p1=12:104438, p2=3:124679, p3=16:79951, p4=4:121040, m1=36:102741, m2=64:44791, y=100:9934)
- Layer 38: ` Paglin`, `oNames`, `malink`, `romes`, `-ulo` (target ranks: p1=12:111994, p2=3:125527, p3=16:111901, p4=4:124077, m1=36:115486, m2=64:66102, y=100:32218)
- Layer 39: ` Answer`, ` Antwort`, `答案`, ` answer`, ` ответ` (target ranks: p1=12:90659, p2=3:119966, p3=16:104510, p4=4:115760, m1=36:108747, m2=64:64056, y=100:37552)
- Layer 40: ` Answer`, `Answer`, ` answer`, `回答`, ` Antwort` (target ranks: p1=12:28817, p2=3:51137, p3=16:31636, p4=4:48020, m1=36:39134, m2=64:16581, y=100:6040)
- Layer 41: `Answer`, ` Answer`, ` answer`, `回答`, `答案` (target ranks: p1=12:1526, p2=3:3485, p3=16:1684, p4=4:1705, m1=36:12199, m2=64:2247, y=100:1566)

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

Answer:<｜Assistant｜></think>80<｜end▁of▁sentence｜><｜User｜>a = 7
b = 5
c = 9
d = 6
e = 7
f = 9
g = 9
h = 5
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
