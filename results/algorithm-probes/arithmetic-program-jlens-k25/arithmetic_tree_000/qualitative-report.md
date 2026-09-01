# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `148` (correct).
- No-filler answer: `146` (incorrect).
- Filler tokens: 25 tokens at absolute indices 733–757.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `p1=17` | 71 (L35, filler 15) | Never |
| J-Lens | `p2=4` | 26 (L21, filler 4) | Never |
| J-Lens | `p3=16` | 75 (L35, filler 15) | Never |
| J-Lens | `p4=5` | 33 (L35, filler 18) | Never |
| J-Lens | `m1=68` | 1 (L35, filler 1) | L35, filler 1 (rank 1) |
| J-Lens | `m2=80` | 2 (L35, filler 4) | L35, filler 4 (rank 2) |
| J-Lens | `y=148` | 14 (L39, filler 4) | Never |
| Logit lens | `p1=17` | 52 (L35, filler 15) | Never |
| Logit lens | `p2=4` | 40 (L29, filler 16) | Never |
| Logit lens | `p3=16` | 50 (L35, filler 15) | Never |
| Logit lens | `p4=5` | 1 (L29, filler 16) | L28, filler 16 (rank 5) |
| Logit lens | `m1=68` | 11 (L35, filler 1) | Never |
| Logit lens | `m2=80` | 8 (L34, filler 4) | L34, filler 4 (rank 8) |
| Logit lens | `y=148` | 67 (L39, filler 22) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 733, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: p1=17:120987, p2=4:125761, p3=16:121905, p4=5:125979, m1=68:121019, m2=80:120130, y=148:109481)
- Layer 10: `忑`, `anta`, `fine`, ` Walker`, `钩` (target ranks: p1=17:38345, p2=4:21260, p3=16:35324, p4=5:19133, m1=68:30882, m2=80:36772, y=148:48183)
- Layer 20: ` .`, `足`, `s`, `Dot`, `dots` (target ranks: p1=17:13258, p2=4:1674, p3=16:12396, p4=5:967, m1=68:2500, m2=80:5823, y=148:45069)
- Layer 30: ` pakig`, ` talags`, `期望`, `期待的`, `计算的` (target ranks: p1=17:6167, p2=4:5608, p3=16:13333, p4=5:2975, m1=68:80, m2=80:5784, y=148:47510)
- Layer 35: `68`, `认`, `期望`, `打法`, `Tap` (target ranks: p1=17:1003, p2=4:1456, p3=16:5139, p4=5:969, m1=68:1, m2=80:669, y=148:25013)
- Layer 36: `期望`, `期待`, `期待的`, ` talags`, `68` (target ranks: p1=17:3830, p2=4:6243, p3=16:22910, p4=5:5643, m1=68:5, m2=80:2591, y=148:24841)
- Layer 37: ` talags`, ` pakig`, `}<?`, ` tra`, `斐` (target ranks: p1=17:40626, p2=4:78591, p3=16:92841, p4=5:80449, m1=68:319, m2=80:41078, y=148:38068)
- Layer 38: ` talags`, `}<?`, ` pakig`, ` tra`, `替换` (target ranks: p1=17:88601, p2=4:93706, p3=16:119190, p4=5:94265, m1=68:3854, m2=80:55985, y=148:47900)
- Layer 39: ` talags`, `}<?`, ` pakig`, `替换`, `斐` (target ranks: p1=17:117448, p2=4:119905, p3=16:124772, p4=5:112134, m1=68:45100, m2=80:120143, y=148:38516)
- Layer 40: ` talags`, ` .`, ` pakig`, ` ald`, `oooo` (target ranks: p1=17:89677, p2=4:65336, p3=16:109940, p4=5:45635, m1=68:14311, m2=80:113727, y=148:12383)
- Layer 41: ` .`, ` .↵↵`, `我没有`, ` .↵`, `我知道` (target ranks: p1=17:38873, p2=4:55348, p3=16:94263, p4=5:11392, m1=68:17401, m2=80:105078, y=148:15349)

### Filler position 2 (absolute token 734, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: p1=17:122494, p2=4:125829, p3=16:122955, p4=5:125926, m1=68:121952, m2=80:122284, y=148:114817)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: p1=17:19812, p2=4:5578, p3=16:18265, p4=5:5277, m1=68:18317, m2=80:21940, y=148:41790)
- Layer 20: ` .`, ` .----`, `往常`, ` procedural`, ` .↵↵` (target ranks: p1=17:120851, p2=4:103860, p3=16:119104, p4=5:96079, m1=68:93484, m2=80:113360, y=148:128054)
- Layer 30: ` etxek`, ` hilabihan`, ` .`, ` pakig`, ` dekameters` (target ranks: p1=17:96507, p2=4:117197, p3=16:89516, p4=5:105208, m1=68:74485, m2=80:116694, y=148:125368)
- Layer 35: ` .`, ` hilabihan`, `enclose`, ` pakig`, ` silic` (target ranks: p1=17:64824, p2=4:107866, p3=16:81296, p4=5:97353, m1=68:109141, m2=80:116846, y=148:124358)
- Layer 36: ` hilabihan`, ` .`, ` talags`, `漏斗`, `enclose` (target ranks: p1=17:26456, p2=4:60075, p3=16:42945, p4=5:42022, m1=68:56710, m2=80:85011, y=148:100182)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, ` Erkännande`, ` talags` (target ranks: p1=17:108617, p2=4:123220, p3=16:104153, p4=5:124128, m1=68:100717, m2=80:115447, y=148:110341)
- Layer 38: ` hilabihan`, ` .`, ` talags`, `}<?`, `�乐` (target ranks: p1=17:80363, p2=4:111915, p3=16:42776, p4=5:113859, m1=68:83928, m2=80:94953, y=148:101544)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` hilabihan`, ` talags`, `}<?` (target ranks: p1=17:90155, p2=4:114087, p3=16:87690, p4=5:109164, m1=68:81409, m2=80:101405, y=148:91702)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>` (target ranks: p1=17:42223, p2=4:58221, p3=16:40357, p4=5:47147, m1=68:46665, m2=80:81431, y=148:53063)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `中书`, ` ,` (target ranks: p1=17:15328, p2=4:6276, p3=16:15574, p4=5:3803, m1=68:18987, m2=80:45738, y=148:13307)

### Filler position 3 (absolute token 735, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=17:125454, p2=4:127938, p3=16:125578, p4=5:128010, m1=68:125347, m2=80:125922, y=148:118647)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, `忑` (target ranks: p1=17:11770, p2=4:4226, p3=16:9966, p4=5:3988, m1=68:11412, m2=80:14113, y=148:28351)
- Layer 20: `ait`, `忑`, `cape`, `足`, `锁定` (target ranks: p1=17:15746, p2=4:2096, p3=16:12443, p4=5:2191, m1=68:8742, m2=80:9370, y=148:40756)
- Layer 30: `esper`, ` esper`, ` Rutherford`, `打完`, `Tap` (target ranks: p1=17:24335, p2=4:2851, p3=16:17984, p4=5:8212, m1=68:17782, m2=80:22572, y=148:38968)
- Layer 35: ` answer`, ` ANSWER`, ` Answer`, `ANSWER`, `answer` (target ranks: p1=17:9862, p2=4:1620, p3=16:10053, p4=5:9750, m1=68:4497, m2=80:8547, y=148:28672)
- Layer 36: ` output`, `acks`, `Tap`, `期待`, ` answer` (target ranks: p1=17:15999, p2=4:5246, p3=16:19240, p4=5:17928, m1=68:5786, m2=80:12712, y=148:25878)
- Layer 37: `等待着`, `calcul`, ` ANSWER`, `智慧的`, `算计` (target ranks: p1=17:42959, p2=4:20341, p3=16:41260, p4=5:59439, m1=68:19622, m2=80:25115, y=148:33982)
- Layer 38: `思想的`, ` Rutherford`, `ocyst`, `}<?`, `ofer` (target ranks: p1=17:94262, p2=4:58003, p3=16:93887, p4=5:102823, m1=68:56737, m2=80:56506, y=148:49793)
- Layer 39: `思想的`, `ophe`, `}<?`, `opters`, `hatic` (target ranks: p1=17:98112, p2=4:110494, p3=16:102136, p4=5:113971, m1=68:82874, m2=80:120449, y=148:83939)
- Layer 40: ` ANSWER`, ` Answer`, `ANSWER`, `算计`, `Answer` (target ranks: p1=17:60184, p2=4:53694, p3=16:75181, p4=5:68984, m1=68:68002, m2=80:116610, y=148:59080)
- Layer 41: ` .`, `Answer`, `试一试`, `等待`, ` wherever` (target ranks: p1=17:20570, p2=4:14385, p3=16:35468, p4=5:7575, m1=68:66676, m2=80:101396, y=148:38595)

### Filler position 4 (absolute token 736, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126490, p2=4:128412, p3=16:126350, p4=5:128466, m1=68:125923, m2=80:126767, y=148:120761)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=17:11076, p2=4:3374, p3=16:9512, p4=5:3502, m1=68:10932, m2=80:12861, y=148:26129)
- Layer 20: `ait`, ` LS`, `cape`, ` quadr`, `拆` (target ranks: p1=17:6691, p2=4:78, p3=16:3899, p4=5:292, m1=68:1866, m2=80:4736, y=148:28298)
- Layer 30: `acos`, ` consum`, `Quintal`, `ipl`, `Subt` (target ranks: p1=17:55465, p2=4:31865, p3=16:43410, p4=5:3094, m1=68:24072, m2=80:12307, y=148:108862)
- Layer 35: `八十`, `80`, `65`, ` eighty`, `75` (target ranks: p1=17:58059, p2=4:73743, p3=16:110219, p4=5:7393, m1=68:373, m2=80:2, y=148:56935)
- Layer 36: `105`, `}<?`, `115`, ` ---|---|---|---`, `110` (target ranks: p1=17:122606, p2=4:116400, p3=16:118694, p4=5:77023, m1=68:18829, m2=80:118, y=148:2257)
- Layer 37: `105`, `115`, `125`, `110`, `116` (target ranks: p1=17:122153, p2=4:104686, p3=16:106237, p4=5:74015, m1=68:30236, m2=80:286, y=148:334)
- Layer 38: `}<?`, `105`, `116`, `108`, `EDMF` (target ranks: p1=17:103433, p2=4:122384, p3=16:66774, p4=5:121672, m1=68:32930, m2=80:15789, y=148:660)
- Layer 39: `116`, `}<?`, `108`, `156`, `rá` (target ranks: p1=17:76108, p2=4:117879, p3=16:39411, p4=5:120203, m1=68:32313, m2=80:41218, y=148:14)
- Layer 40: `136`, `116`, `rá`, `108`, `132` (target ranks: p1=17:45699, p2=4:115599, p3=16:63763, p4=5:120716, m1=68:9523, m2=80:46852, y=148:15)
- Layer 41: `忑`, `告辞`, `我曾经`, `我之前`, `饪` (target ranks: p1=17:14701, p2=4:40588, p3=16:38647, p4=5:24735, m1=68:16118, m2=80:47635, y=148:2707)

### Filler position 5 (absolute token 737, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126117, p2=4:128275, p3=16:125966, p4=5:128328, m1=68:125169, m2=80:126132, y=148:120356)
- Layer 10: ` Walker`, `锁定`, `挪`, `Walker`, `ait` (target ranks: p1=17:11468, p2=4:4147, p3=16:10432, p4=5:3901, m1=68:11702, m2=80:13134, y=148:28406)
- Layer 20: `幽`, `锁定`, ` LS`, `鞍`, `挪` (target ranks: p1=17:14042, p2=4:3267, p3=16:12402, p4=5:1612, m1=68:9705, m2=80:12183, y=148:32400)
- Layer 30: `�`, `鞍`, `acos`, `Tap`, ` corona` (target ranks: p1=17:58042, p2=4:31084, p3=16:70849, p4=5:11776, m1=68:26907, m2=80:58374, y=148:102725)
- Layer 35: `羊`, `Tap`, ` repetition`, ` var`, `鞍` (target ranks: p1=17:32855, p2=4:15282, p3=16:42325, p4=5:3208, m1=68:36366, m2=80:43092, y=148:80313)
- Layer 36: `berg`, `羊`, `bergh`, ` start`, ` talags` (target ranks: p1=17:55442, p2=4:36575, p3=16:72671, p4=5:11634, m1=68:36833, m2=80:61484, y=148:63169)
- Layer 37: `acos`, `}<?`, `轨迹`, `滴`, ` talags` (target ranks: p1=17:97221, p2=4:91004, p3=16:105323, p4=5:57822, m1=68:77042, m2=80:97673, y=148:86659)
- Layer 38: `hemer`, ` talags`, `}<?`, `迷惑`, `zat` (target ranks: p1=17:109423, p2=4:103859, p3=16:115903, p4=5:73179, m1=68:105828, m2=80:110201, y=148:103831)
- Layer 39: ` talags`, `}<?`, `hemer`, `迷惑`, `东海` (target ranks: p1=17:104328, p2=4:120088, p3=16:118569, p4=5:113645, m1=68:110016, m2=80:124131, y=148:116204)
- Layer 40: ` talags`, ` x`, ` nasod`, `тельными`, `坏` (target ranks: p1=17:70453, p2=4:80433, p3=16:96301, p4=5:69421, m1=68:98910, m2=80:121137, y=148:100755)
- Layer 41: ` .`, `鹉`, `下面是`, `<｜end▁of▁sentence｜>`, ` dotted` (target ranks: p1=17:36640, p2=4:31790, p3=16:72735, p4=5:13921, m1=68:85638, m2=80:113065, y=148:66229)

### Filler position 6 (absolute token 738, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126166, p2=4:128279, p3=16:126001, p4=5:128331, m1=68:124959, m2=80:126126, y=148:120464)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: p1=17:11194, p2=4:4155, p3=16:9809, p4=5:3999, m1=68:11335, m2=80:13616, y=148:26710)
- Layer 20: ` combinator`, `ting`, ` answer`, `试一试`, `�` (target ranks: p1=17:40582, p2=4:39496, p3=16:34443, p4=5:38426, m1=68:64153, m2=80:51642, y=148:89867)
- Layer 30: `梯`, `分解`, `高明`, `梯度`, ` combinator` (target ranks: p1=17:18366, p2=4:22791, p3=16:14596, p4=5:8175, m1=68:35736, m2=80:23883, y=148:63402)
- Layer 35: `高明`, `acks`, ` smile`, `yg`, `幽` (target ranks: p1=17:15059, p2=4:42521, p3=16:17683, p4=5:16448, m1=68:27818, m2=80:25012, y=148:83994)
- Layer 36: `yg`, `柿子`, `高明`, ` pakig`, `刺激` (target ranks: p1=17:18378, p2=4:37422, p3=16:22625, p4=5:15452, m1=68:19792, m2=80:18125, y=148:64232)
- Layer 37: ` pakig`, ` Rutherford`, ` Tenth`, `刺激`, `高明` (target ranks: p1=17:48933, p2=4:103807, p3=16:51888, p4=5:69651, m1=68:60844, m2=80:42241, y=148:104504)
- Layer 38: ` pakig`, `itten`, ` ladder`, ` Rutherford`, `蒲公英` (target ranks: p1=17:63492, p2=4:105194, p3=16:59890, p4=5:86892, m1=68:81972, m2=80:61035, y=148:107312)
- Layer 39: ` pakig`, `}<?`, ` talags`, `<｜begin▁of▁sentence｜>`, `ucchi` (target ranks: p1=17:59804, p2=4:127085, p3=16:66660, p4=5:120981, m1=68:109361, m2=80:123579, y=148:127777)
- Layer 40: ` Fifteen`, ` dotted`, ` pakig`, ` fifteen`, ` talags` (target ranks: p1=17:16586, p2=4:116160, p3=16:25686, p4=5:89376, m1=68:104475, m2=80:122083, y=148:125439)
- Layer 41: ` .`, ` Fifteen`, ` x`, `一个一个`, ` dotted` (target ranks: p1=17:9116, p2=4:51450, p3=16:30051, p4=5:21229, m1=68:94831, m2=80:113240, y=148:100628)

### Filler position 7 (absolute token 739, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126033, p2=4:128241, p3=16:125942, p4=5:128291, m1=68:124657, m2=80:125874, y=148:120087)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=17:10061, p2=4:3493, p3=16:8720, p4=5:3398, m1=68:9975, m2=80:12182, y=148:25408)
- Layer 20: `锁定`, `ait`, `鞍`, ` cheer`, `幽` (target ranks: p1=17:5781, p2=4:670, p3=16:3500, p4=5:879, m1=68:2483, m2=80:2973, y=148:16003)
- Layer 30: `鞍`, `69`, `Subt`, `64`, `54` (target ranks: p1=17:734, p2=4:2761, p3=16:861, p4=5:4383, m1=68:16, m2=80:741, y=148:1960)
- Layer 35: `鞍`, ` stabil`, ` met`, `Subt`, `洋` (target ranks: p1=17:3036, p2=4:2100, p3=16:4500, p4=5:3414, m1=68:40, m2=80:781, y=148:2140)
- Layer 36: ` stabil`, `calcul`, `银杏`, ` cascade`, `鞍` (target ranks: p1=17:20377, p2=4:12133, p3=16:35767, p4=5:20664, m1=68:42, m2=80:1968, y=148:1087)
- Layer 37: `anium`, `}<?`, ` tra`, `殿堂`, `ocyst` (target ranks: p1=17:48472, p2=4:54424, p3=16:60907, p4=5:71466, m1=68:365, m2=80:10858, y=148:578)
- Layer 38: `}<?`, `ocyst`, ` Noruwega`, `opters`, `糊涂` (target ranks: p1=17:95519, p2=4:95479, p3=16:100810, p4=5:105834, m1=68:10766, m2=80:40943, y=148:6569)
- Layer 39: `}<?`, `ocyst`, `opters`, `糊涂`, `叶子` (target ranks: p1=17:100739, p2=4:116405, p3=16:85116, p4=5:116889, m1=68:51616, m2=80:72574, y=148:1760)
- Layer 40: ` drip`, `留存`, ` `, `糊涂`, `反复` (target ranks: p1=17:80448, p2=4:73238, p3=16:48972, p4=5:76779, m1=68:38994, m2=80:62853, y=148:1165)
- Layer 41: ` .`, `试一试`, `鹉`, `袄`, ` ` (target ranks: p1=17:46188, p2=4:25965, p3=16:40034, p4=5:10863, m1=68:45594, m2=80:58018, y=148:6726)

### Filler position 8 (absolute token 740, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:125948, p2=4:128212, p3=16:125882, p4=5:128252, m1=68:124427, m2=80:125816, y=148:120003)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: p1=17:10304, p2=4:3620, p3=16:8863, p4=5:3614, m1=68:10183, m2=80:12092, y=148:25491)
- Layer 20: `锁定`, `ait`, ` smile`, ` Walker`, `胃癌` (target ranks: p1=17:6813, p2=4:1057, p3=16:4938, p4=5:1626, m1=68:3621, m2=80:7028, y=148:22963)
- Layer 30: `重复`, ` repetitions`, ` repetition`, `Tap`, ` repeated` (target ranks: p1=17:21057, p2=4:14737, p3=16:29462, p4=5:11096, m1=68:24742, m2=80:35743, y=148:48989)
- Layer 35: `acks`, `重复`, ` repetition`, ` repetitions`, `acos` (target ranks: p1=17:9307, p2=4:2254, p3=16:15792, p4=5:2493, m1=68:7912, m2=80:22661, y=148:54577)
- Layer 36: `重复`, ` repeated`, `反复`, ` repetition`, `acks` (target ranks: p1=17:8000, p2=4:1778, p3=16:15480, p4=5:2609, m1=68:2173, m2=80:12563, y=148:21244)
- Layer 37: `acos`, `}<?`, ` follow`, ` covari`, `反复` (target ranks: p1=17:18472, p2=4:10522, p3=16:27656, p4=5:18082, m1=68:8883, m2=80:41035, y=148:32805)
- Layer 38: `}<?`, `acos`, `acons`, ` complicate`, `�` (target ranks: p1=17:46562, p2=4:32360, p3=16:56287, p4=5:53584, m1=68:38608, m2=80:77112, y=148:64928)
- Layer 39: ` talags`, `}<?`, ` consonant`, `替换`, `acons` (target ranks: p1=17:28836, p2=4:97565, p3=16:52170, p4=5:89232, m1=68:55507, m2=80:114711, y=148:113344)
- Layer 40: ` talags`, `留存`, `兑`, `试一试`, ` mosunod` (target ranks: p1=17:3514, p2=4:33000, p3=16:12021, p4=5:25250, m1=68:36014, m2=80:111409, y=148:102865)
- Layer 41: ` .`, `试一试`, `有下列`, ` seventeen`, `下面是` (target ranks: p1=17:2942, p2=4:21932, p3=16:21644, p4=5:10237, m1=68:53237, m2=80:113661, y=148:93104)

### Filler position 9 (absolute token 741, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126164, p2=4:128318, p3=16:126156, p4=5:128357, m1=68:124602, m2=80:126088, y=148:120430)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `挪` (target ranks: p1=17:9553, p2=4:3356, p3=16:8408, p4=5:3184, m1=68:9904, m2=80:11512, y=148:24680)
- Layer 20: ` Walker`, `锁定`, `Walker`, `ait`, `能被` (target ranks: p1=17:6965, p2=4:1978, p3=16:5403, p4=5:1578, m1=68:4846, m2=80:7015, y=148:29993)
- Layer 30: `acos`, `退出`, `enes`, ` sequential`, `分解` (target ranks: p1=17:21838, p2=4:20652, p3=16:23598, p4=5:8524, m1=68:14503, m2=80:35866, y=148:103239)
- Layer 35: ` sequential`, `Tap`, ` repetition`, `分解`, ` cascade` (target ranks: p1=17:7865, p2=4:3318, p3=16:7764, p4=5:1408, m1=68:5629, m2=80:12576, y=148:59993)
- Layer 36: `分解`, ` Zad`, ` drip`, ` cascade`, `sequential` (target ranks: p1=17:16432, p2=4:10303, p3=16:21548, p4=5:4743, m1=68:5209, m2=80:17425, y=148:51312)
- Layer 37: `}<?`, `acos`, ` Zad`, `滴`, ` cascade` (target ranks: p1=17:35751, p2=4:39569, p3=16:43385, p4=5:25497, m1=68:19641, m2=80:53079, y=148:76729)
- Layer 38: `}<?`, `打磨`, `zat`, ` Zad`, `acos` (target ranks: p1=17:62934, p2=4:59497, p3=16:66983, p4=5:41412, m1=68:38624, m2=80:75236, y=148:97476)
- Layer 39: `}<?`, `替换`, `东海`, `打磨`, ` Mul` (target ranks: p1=17:67941, p2=4:104805, p3=16:80620, p4=5:84880, m1=68:58880, m2=80:102565, y=148:109662)
- Layer 40: `留存`, `}<?`, ` talags`, `坏`, ` spare` (target ranks: p1=17:22707, p2=4:43113, p3=16:37945, p4=5:28013, m1=68:36047, m2=80:92254, y=148:91371)
- Layer 41: ` .`, `那一`, ` `, `特`, ` spare` (target ranks: p1=17:12605, p2=4:28091, p3=16:43342, p4=5:8190, m1=68:45810, m2=80:96258, y=148:64047)

### Filler position 10 (absolute token 742, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=17:126272, p2=4:128353, p3=16:126267, p4=5:128401, m1=68:124568, m2=80:126203, y=148:120718)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `挪` (target ranks: p1=17:9403, p2=4:3417, p3=16:8373, p4=5:3245, m1=68:9937, m2=80:11388, y=148:25303)
- Layer 20: ` Walker`, `拆`, `ait`, `Walker`, `挪` (target ranks: p1=17:15836, p2=4:7260, p3=16:11017, p4=5:6766, m1=68:11096, m2=80:11272, y=148:50772)
- Layer 30: `分解`, `计算的`, ` calculator`, `calcul`, `拆` (target ranks: p1=17:13736, p2=4:4968, p3=16:8140, p4=5:3262, m1=68:8691, m2=80:9975, y=148:51901)
- Layer 35: `分解`, ` Execution`, ` calculator`, `每一步`, ` sequential` (target ranks: p1=17:11886, p2=4:4727, p3=16:6967, p4=5:3381, m1=68:4336, m2=80:5838, y=148:42991)
- Layer 36: `分解`, `calcul`, ` Execution`, `计算的`, `第一步` (target ranks: p1=17:27397, p2=4:17888, p3=16:21226, p4=5:14379, m1=68:4486, m2=80:10242, y=148:33999)
- Layer 37: `程序的`, `}<?`, `calcul`, `步骤`, `程序` (target ranks: p1=17:60123, p2=4:75062, p3=16:43418, p4=5:61890, m1=68:15953, m2=80:34389, y=148:59525)
- Layer 38: `}<?`, `zat`, `程序的`, `calcul`, ` cál` (target ranks: p1=17:85443, p2=4:102808, p3=16:69493, p4=5:91257, m1=68:31797, m2=80:59334, y=148:78994)
- Layer 39: `}<?`, `zat`, `<｜begin▁of▁sentence｜>`, ` каль`, `替换` (target ranks: p1=17:85939, p2=4:117167, p3=16:78786, p4=5:103722, m1=68:42306, m2=80:87792, y=148:101838)
- Layer 40: `留存`, `zat`, `}<?`, `停顿`, `šk` (target ranks: p1=17:28981, p2=4:58591, p3=16:33011, p4=5:39310, m1=68:17452, m2=80:59839, y=148:78866)
- Layer 41: ` .`, `鹉`, `留存`, ` `, `<｜end▁of▁sentence｜>` (target ranks: p1=17:18576, p2=4:17992, p3=16:25585, p4=5:4915, m1=68:19709, m2=80:48300, y=148:40100)

### Filler position 11 (absolute token 743, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126549, p2=4:128476, p3=16:126534, p4=5:128511, m1=68:124731, m2=80:126600, y=148:121561)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `挪` (target ranks: p1=17:10248, p2=4:3619, p3=16:9035, p4=5:3496, m1=68:10384, m2=80:12705, y=148:27914)
- Layer 20: `锁定`, `挪`, ` LS`, ` smile`, `幽` (target ranks: p1=17:3256, p2=4:262, p3=16:2596, p4=5:321, m1=68:2485, m2=80:2978, y=148:25695)
- Layer 30: ` consuming`, ` consum`, `acos`, `钻石`, ` pent` (target ranks: p1=17:33846, p2=4:26620, p3=16:39843, p4=5:597, m1=68:23195, m2=80:6344, y=148:121752)
- Layer 35: `25`, `二十五`, `75`, `65`, `45` (target ranks: p1=17:66427, p2=4:68875, p3=16:117073, p4=5:1755, m1=68:4248, m2=80:42, y=148:119394)
- Layer 36: `Quintal`, `105`, ` Holid`, `}<?`, `?datasetId` (target ranks: p1=17:125433, p2=4:109733, p3=16:126623, p4=5:25296, m1=68:6619, m2=80:747, y=148:93150)
- Layer 37: `Quintal`, `105`, `?datasetId`, ` KLIMA`, ` Quinary` (target ranks: p1=17:123890, p2=4:100698, p3=16:122922, p4=5:25103, m1=68:7743, m2=80:1284, y=148:55771)
- Layer 38: `93`, `九十`, ` ninety`, `91`, ` noventa` (target ranks: p1=17:94805, p2=4:126490, p3=16:118576, p4=5:94348, m1=68:37699, m2=80:7791, y=148:117224)
- Layer 39: `93`, `91`, `汀`, ` ninety`, ` noventa` (target ranks: p1=17:49996, p2=4:121226, p3=16:100803, p4=5:97264, m1=68:36971, m2=80:16490, y=148:42484)
- Layer 40: `rá`, ` ninety`, ` noventa`, `}<?`, ` ons` (target ranks: p1=17:16102, p2=4:105309, p3=16:86624, p4=5:73578, m1=68:16948, m2=80:9891, y=148:6394)
- Layer 41: `到这里`, `�ျေးရွ`, `辄`, `忑`, `来这里` (target ranks: p1=17:12085, p2=4:46356, p3=16:53478, p4=5:23330, m1=68:30905, m2=80:23492, y=148:13878)

### Filler position 12 (absolute token 744, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: p1=17:126398, p2=4:128456, p3=16:126414, p4=5:128484, m1=68:124613, m2=80:126445, y=148:121323)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=17:9977, p2=4:3311, p3=16:8425, p4=5:3252, m1=68:10166, m2=80:12732, y=148:26433)
- Layer 20: `ait`, `锁定`, ` wig`, ` smile`, ` Walker` (target ranks: p1=17:9129, p2=4:1263, p3=16:6328, p4=5:1548, m1=68:5576, m2=80:9002, y=148:26015)
- Layer 30: `Tap`, `tap`, ` tap`, ` Tap`, `打完` (target ranks: p1=17:35045, p2=4:26354, p3=16:28990, p4=5:7994, m1=68:44247, m2=80:62225, y=148:56819)
- Layer 35: ` tap`, `acks`, `Tap`, `tap`, ` Tap` (target ranks: p1=17:16406, p2=4:5332, p3=16:10816, p4=5:1936, m1=68:18934, m2=80:46745, y=148:50732)
- Layer 36: ` tap`, `期望`, `Tap`, `adal`, `acks` (target ranks: p1=17:9748, p2=4:1410, p3=16:6891, p4=5:798, m1=68:4137, m2=80:23689, y=148:21759)
- Layer 37: `acons`, `acet`, `坏`, `acos`, `EDAC` (target ranks: p1=17:32124, p2=4:18228, p3=16:24581, p4=5:16137, m1=68:19518, m2=80:59996, y=148:41435)
- Layer 38: `acons`, `}<?`, `坏`, `acet`, `打包` (target ranks: p1=17:61033, p2=4:42164, p3=16:54429, p4=5:48364, m1=68:42191, m2=80:75468, y=148:61802)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `+-+-+-+-`, `东海`, `acons` (target ranks: p1=17:65114, p2=4:113626, p3=16:75080, p4=5:88672, m1=68:55257, m2=80:104649, y=148:111200)
- Layer 40: `试一试`, ` mosunod`, ` Twenty`, ` ANSWER`, ` nasod` (target ranks: p1=17:8129, p2=4:51602, p3=16:20730, p4=5:19133, m1=68:23367, m2=80:70663, y=148:83417)
- Layer 41: ` .`, `试一试`, `ldots`, `等待`, `Answer` (target ranks: p1=17:7081, p2=4:24762, p3=16:17157, p4=5:4302, m1=68:34147, m2=80:80814, y=148:60443)

### Filler position 13 (absolute token 745, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126654, p2=4:128563, p3=16:126653, p4=5:128589, m1=68:124945, m2=80:126794, y=148:122056)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=17:10383, p2=4:3828, p3=16:9086, p4=5:3719, m1=68:10465, m2=80:12421, y=148:25793)
- Layer 20: `锁定`, `忑`, `ait`, ` Walker`, ` engaging` (target ranks: p1=17:17965, p2=4:5653, p3=16:11927, p4=5:6603, m1=68:10332, m2=80:12728, y=148:24815)
- Layer 30: `鞍`, `题库`, ` repetitions`, ` exercises`, `Tasks` (target ranks: p1=17:41308, p2=4:12753, p3=16:27029, p4=5:11923, m1=68:18165, m2=80:25110, y=148:48243)
- Layer 35: `Tasks`, `task`, ` exercises`, ` Task`, ` task` (target ranks: p1=17:16701, p2=4:2319, p3=16:4410, p4=5:2145, m1=68:5714, m2=80:9947, y=148:20677)
- Layer 36: `Tasks`, ` tasks`, ` task`, ` Task`, `tasks` (target ranks: p1=17:28632, p2=4:4514, p3=16:8120, p4=5:4743, m1=68:2835, m2=80:11317, y=148:12640)
- Layer 37: ` tasks`, ` task`, `Tasks`, `tasks`, ` Aufgabe` (target ranks: p1=17:62127, p2=4:24337, p3=16:20220, p4=5:24860, m1=68:10623, m2=80:30966, y=148:22117)
- Layer 38: `}<?`, `冰冰`, ` tasks`, `下沉`, `坏` (target ranks: p1=17:93369, p2=4:47878, p3=16:44847, p4=5:56926, m1=68:25993, m2=80:66164, y=148:34572)
- Layer 39: `}<?`, `下沉`, `romic`, `累`, `坏的` (target ranks: p1=17:115039, p2=4:115918, p3=16:94402, p4=5:114002, m1=68:68073, m2=80:114600, y=148:68326)
- Layer 40: `冰冰`, `程序的`, `坏的`, `ark`, ` program` (target ranks: p1=17:80470, p2=4:67563, p3=16:51911, p4=5:60673, m1=68:54205, m2=80:108889, y=148:58325)
- Layer 41: ` .`, ` program`, ` .↵↵`, `那两个`, `oooo` (target ranks: p1=17:38123, p2=4:31161, p3=16:44966, p4=5:7540, m1=68:54564, m2=80:97361, y=148:27299)

### Filler position 14 (absolute token 746, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126841, p2=4:128646, p3=16:126858, p4=5:128662, m1=68:125252, m2=80:127058, y=148:122547)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: p1=17:9640, p2=4:3417, p3=16:8054, p4=5:3405, m1=68:9386, m2=80:11474, y=148:23892)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `拆` (target ranks: p1=17:13266, p2=4:2925, p3=16:6354, p4=5:4282, m1=68:8202, m2=80:9664, y=148:29049)
- Layer 30: `赋值`, ` initialize`, ` assignment`, ` initialized`, `平行` (target ranks: p1=17:60789, p2=4:27456, p3=16:25639, p4=5:30952, m1=68:39592, m2=80:38674, y=148:105969)
- Layer 35: `输入的`, ` var`, ` future`, ` variable`, ` preset` (target ranks: p1=17:30514, p2=4:3692, p3=16:7424, p4=5:4216, m1=68:9258, m2=80:8202, y=148:57476)
- Layer 36: `输入的`, ` assignment`, `柿子`, ` initial`, ` variables` (target ranks: p1=17:54679, p2=4:11161, p3=16:21109, p4=5:13187, m1=68:10192, m2=80:12154, y=148:46315)
- Layer 37: `变量的`, `variables`, ` variables`, ` initial`, `Variables` (target ranks: p1=17:102050, p2=4:71898, p3=16:64681, p4=5:79504, m1=68:49739, m2=80:50379, y=148:80975)
- Layer 38: `}<?`, `variables`, `变量的`, `dividers`, `文字的` (target ranks: p1=17:112315, p2=4:86813, p3=16:80962, p4=5:93162, m1=68:69557, m2=80:71882, y=148:94060)
- Layer 39: `}<?`, `acons`, `<｜begin▁of▁sentence｜>`, `树叶`, `文字的` (target ranks: p1=17:105868, p2=4:115790, p3=16:86789, p4=5:114508, m1=68:86393, m2=80:103367, y=148:109386)
- Layer 40: ` talags`, `留存`, `scr`, `下沉`, `šk` (target ranks: p1=17:68505, p2=4:62685, p3=16:42328, p4=5:66480, m1=68:68799, m2=80:99171, y=148:105388)
- Layer 41: ` .`, ` dotted`, `外商投资`, `那两个`, ` ` (target ranks: p1=17:50160, p2=4:26106, p3=16:40612, p4=5:13434, m1=68:70427, m2=80:93088, y=148:78701)

### Filler position 15 (absolute token 747, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: p1=17:126759, p2=4:128632, p3=16:126828, p4=5:128648, m1=68:125184, m2=80:126976, y=148:122160)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=17:9696, p2=4:3377, p3=16:8102, p4=5:3350, m1=68:9642, m2=80:11695, y=148:24258)
- Layer 20: `ait`, `锁定`, `拆`, `距`, `cape` (target ranks: p1=17:5983, p2=4:952, p3=16:3040, p4=5:1286, m1=68:4913, m2=80:4923, y=148:22567)
- Layer 30: `第一步`, ` step`, `算出`, `打完`, ` Step` (target ranks: p1=17:4237, p2=4:7257, p3=16:4872, p4=5:5460, m1=68:18412, m2=80:20598, y=148:74335)
- Layer 35: ` reserved`, `分解`, ` p`, ` step`, ` Step` (target ranks: p1=17:71, p2=4:3071, p3=16:75, p4=5:1246, m1=68:2764, m2=80:3711, y=148:38718)
- Layer 36: `留存`, ` reserved`, `分解`, `俯`, `ession` (target ranks: p1=17:82, p2=4:6003, p3=16:163, p4=5:3776, m1=68:3233, m2=80:7437, y=148:31230)
- Layer 37: `}<?`, `acos`, `筋`, `累`, ` p` (target ranks: p1=17:113, p2=4:63842, p3=16:533, p4=5:47032, m1=68:19849, m2=80:38110, y=148:60187)
- Layer 38: `}<?`, ` p`, `累`, `?datasetId`, `计算方法` (target ranks: p1=17:794, p2=4:88952, p3=16:3009, p4=5:73884, m1=68:38568, m2=80:73411, y=148:80912)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, ` seventeen`, `累`, `替换` (target ranks: p1=17:1916, p2=4:112594, p3=16:18811, p4=5:105960, m1=68:58921, m2=80:107860, y=148:116684)
- Layer 40: ` seventeen`, ` p`, `留存`, ` sixteen`, `累` (target ranks: p1=17:464, p2=4:78651, p3=16:9402, p4=5:74744, m1=68:31801, m2=80:111568, y=148:116976)
- Layer 41: ` .`, ` seventeen`, `步骤如下`, `试一试`, `ascals` (target ranks: p1=17:1240, p2=4:36961, p3=16:16274, p4=5:16215, m1=68:56943, m2=80:101762, y=148:93188)

### Filler position 16 (absolute token 748, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `Noiz` (target ranks: p1=17:126776, p2=4:128631, p3=16:126847, p4=5:128654, m1=68:125054, m2=80:127078, y=148:122384)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: p1=17:11107, p2=4:4065, p3=16:9307, p4=5:4035, m1=68:11160, m2=80:13558, y=148:25592)
- Layer 20: `锁定`, `ait`, ` smile`, `cape`, `能被` (target ranks: p1=17:3850, p2=4:395, p3=16:2382, p4=5:693, m1=68:2637, m2=80:4236, y=148:24955)
- Layer 30: `acos`, ` expecting`, `柿子`, `交替`, `粥` (target ranks: p1=17:32443, p2=4:24411, p3=16:24000, p4=5:734, m1=68:11799, m2=80:16840, y=148:99714)
- Layer 35: `25`, `75`, `40`, `95`, `acin` (target ranks: p1=17:13230, p2=4:9486, p3=16:41559, p4=5:248, m1=68:342, m2=80:17, y=148:19978)
- Layer 36: `105`, `125`, `95`, ` Holt`, `زياح` (target ranks: p1=17:44530, p2=4:43513, p3=16:86745, p4=5:4660, m1=68:249, m2=80:401, y=148:17587)
- Layer 37: `105`, `زياح`, `125`, `95`, `115` (target ranks: p1=17:60338, p2=4:63575, p3=16:85702, p4=5:12657, m1=68:1830, m2=80:1814, y=148:14879)
- Layer 38: `107`, `105`, `红柿`, `زياح`, `108` (target ranks: p1=17:57489, p2=4:94441, p3=16:85003, p4=5:48421, m1=68:6893, m2=80:7472, y=148:25970)
- Layer 39: `125`, `159`, `زياح`, `142`, `133` (target ranks: p1=17:34818, p2=4:85760, p3=16:25787, p4=5:65421, m1=68:28366, m2=80:21614, y=148:132)
- Layer 40: `136`, `125`, `116`, `135`, `126` (target ranks: p1=17:16757, p2=4:41126, p3=16:16682, p4=5:28553, m1=68:24319, m2=80:18840, y=148:82)
- Layer 41: ` .`, `有的时候`, `那两个`, `况且`, `来这里` (target ranks: p1=17:13370, p2=4:26132, p3=16:26882, p4=5:10567, m1=68:32820, m2=80:28171, y=148:1049)

### Filler position 17 (absolute token 749, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=17:126614, p2=4:128588, p3=16:126728, p4=5:128599, m1=68:124752, m2=80:126855, y=148:122096)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=17:11628, p2=4:4850, p3=16:10442, p4=5:4535, m1=68:12758, m2=80:14881, y=148:28973)
- Layer 20: `锁定`, `cape`, ` smile`, `ession`, ` emot` (target ranks: p1=17:2738, p2=4:1460, p3=16:3154, p4=5:1387, m1=68:3032, m2=80:3657, y=148:20785)
- Layer 30: `acos`, `鞍`, `柿子`, ` Ries`, ` Imp` (target ranks: p1=17:24368, p2=4:26538, p3=16:32553, p4=5:1804, m1=68:4656, m2=80:14031, y=148:75041)
- Layer 35: `鞍`, `柿子`, ` labor`, `acin`, `cape` (target ranks: p1=17:5801, p2=4:8402, p3=16:19934, p4=5:653, m1=68:226, m2=80:1111, y=148:22109)
- Layer 36: `坏`, ` upright`, `反复`, `鞍`, `停` (target ranks: p1=17:32261, p2=4:35149, p3=16:78681, p4=5:3693, m1=68:152, m2=80:17367, y=148:38929)
- Layer 37: `}<?`, `Quintal`, `onana`, ` compete`, `cault` (target ranks: p1=17:72534, p2=4:84110, p3=16:92229, p4=5:30448, m1=68:5318, m2=80:48673, y=148:50878)
- Layer 38: `}<?`, `onana`, `坏`, `oNames`, `在北京` (target ranks: p1=17:99559, p2=4:95280, p3=16:101386, p4=5:58306, m1=68:9998, m2=80:55672, y=148:79672)
- Layer 39: `}<?`, `坏`, `-ulo`, `ozygous`, `铎` (target ranks: p1=17:98342, p2=4:107774, p3=16:86761, p4=5:92811, m1=68:12098, m2=80:58709, y=148:34608)
- Layer 40: `坏`, ` .`, ` dotted`, `语言文字`, ` concaten` (target ranks: p1=17:39107, p2=4:43527, p3=16:37961, p4=5:34107, m1=68:2436, m2=80:27790, y=148:4924)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `一个一个` (target ranks: p1=17:18885, p2=4:23557, p3=16:35397, p4=5:5829, m1=68:4959, m2=80:28349, y=148:951)

### Filler position 18 (absolute token 750, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `Noiz` (target ranks: p1=17:126840, p2=4:128662, p3=16:126947, p4=5:128666, m1=68:124977, m2=80:127175, y=148:122742)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=17:10456, p2=4:3814, p3=16:8952, p4=5:3765, m1=68:11146, m2=80:13513, y=148:28110)
- Layer 20: ` Walker`, `能被`, `ait`, `锁定`, ` smile` (target ranks: p1=17:7483, p2=4:2411, p3=16:6169, p4=5:2636, m1=68:6988, m2=80:9020, y=148:35188)
- Layer 30: `鞍`, `acos`, ` expecting`, ` consum`, `aloh` (target ranks: p1=17:54723, p2=4:23005, p3=16:51044, p4=5:440, m1=68:37993, m2=80:32288, y=148:118033)
- Layer 35: `鞍`, ` labor`, `acin`, `35`, `�` (target ranks: p1=17:9827, p2=4:6480, p3=16:26699, p4=5:33, m1=68:6478, m2=80:924, y=148:72147)
- Layer 36: `鞍`, `adal`, `otan`, `规范的`, `mot` (target ranks: p1=17:5641, p2=4:26643, p3=16:55038, p4=5:95, m1=68:1141, m2=80:5750, y=148:63711)
- Layer 37: `}<?`, `Quintal`, `otan`, `mot`, `onana` (target ranks: p1=17:11053, p2=4:71252, p3=16:78604, p4=5:1092, m1=68:8583, m2=80:24993, y=148:76833)
- Layer 38: `}<?`, `芦`, `osan`, `otan`, `galan` (target ranks: p1=17:29778, p2=4:102919, p3=16:106702, p4=5:5459, m1=68:19745, m2=80:38931, y=148:92073)
- Layer 39: `}<?`, `芦`, `hatic`, ` Nij`, `迷惑` (target ranks: p1=17:31638, p2=4:121927, p3=16:63117, p4=5:50667, m1=68:18416, m2=80:35411, y=148:4885)
- Layer 40: `135`, `}<?`, `136`, ` .`, `šk` (target ranks: p1=17:9594, p2=4:92695, p3=16:39460, p4=5:9375, m1=68:13785, m2=80:15564, y=148:1040)
- Layer 41: ` .`, ` waiting`, ` :`, ` `, ` because` (target ranks: p1=17:6417, p2=4:42807, p3=16:32508, p4=5:823, m1=68:15679, m2=80:16981, y=148:1273)

### Filler position 19 (absolute token 751, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `Noiz` (target ranks: p1=17:126968, p2=4:128732, p3=16:127104, p4=5:128740, m1=68:125311, m2=80:127359, y=148:123043)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=17:9754, p2=4:3444, p3=16:8501, p4=5:3374, m1=68:10568, m2=80:12931, y=148:27618)
- Layer 20: ` Walker`, `ait`, `忑`, `锁定`, `Walker` (target ranks: p1=17:7367, p2=4:5265, p3=16:5482, p4=5:4774, m1=68:8628, m2=80:10096, y=148:35260)
- Layer 30: ` repetitions`, ` randomized`, ` repetition`, ` randomization`, `随机` (target ranks: p1=17:12879, p2=4:9492, p3=16:10468, p4=5:8661, m1=68:13539, m2=80:27360, y=148:68304)
- Layer 35: ` exercises`, ` repetitions`, ` repetition`, ` var`, `题库` (target ranks: p1=17:3972, p2=4:3272, p3=16:1555, p4=5:2773, m1=68:11731, m2=80:14063, y=148:42667)
- Layer 36: ` pattern`, ` exercises`, ` var`, ` Type`, `反复` (target ranks: p1=17:5123, p2=4:7696, p3=16:2715, p4=5:6120, m1=68:6544, m2=80:15165, y=148:31234)
- Layer 37: ` pattern`, `}<?`, `pattern`, `variant`, ` variations` (target ranks: p1=17:14848, p2=4:44349, p3=16:8023, p4=5:43370, m1=68:28159, m2=80:48339, y=148:50527)
- Layer 38: `}<?`, ` variations`, ` variation`, `variant`, ` pattern` (target ranks: p1=17:33891, p2=4:62500, p3=16:19667, p4=5:71638, m1=68:45479, m2=80:66088, y=148:66533)
- Layer 39: `}<?`, `pattern`, ` pattern`, ` template`, ` variation` (target ranks: p1=17:73715, p2=4:107241, p3=16:64712, p4=5:104866, m1=68:55691, m2=80:98739, y=148:80041)
- Layer 40: `程序的`, ` program`, `程式`, `程序`, `}<?` (target ranks: p1=17:14378, p2=4:38135, p3=16:18415, p4=5:35834, m1=68:32236, m2=80:71012, y=148:56471)
- Layer 41: ` .`, ` program`, `程序的`, ` arithmetic`, `程序` (target ranks: p1=17:14481, p2=4:30159, p3=16:34273, p4=5:8316, m1=68:72756, m2=80:77651, y=148:35985)

### Filler position 20 (absolute token 752, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `-ulo`, `aplenty` (target ranks: p1=17:127326, p2=4:128846, p3=16:127390, p4=5:128839, m1=68:125872, m2=80:127752, y=148:123665)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: p1=17:10735, p2=4:3854, p3=16:9089, p4=5:3812, m1=68:10575, m2=80:12979, y=148:26496)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `平行` (target ranks: p1=17:16011, p2=4:8302, p3=16:11440, p4=5:8534, m1=68:10268, m2=80:13053, y=148:34393)
- Layer 30: `清楚楚`, `平行`, `sl`, ` parallel`, ` dy` (target ranks: p1=17:21331, p2=4:4516, p3=16:12697, p4=5:10333, m1=68:14073, m2=80:25031, y=148:41466)
- Layer 35: ` tap`, ` met`, ` equation`, `沛`, ` calculator` (target ranks: p1=17:9008, p2=4:899, p3=16:2747, p4=5:4327, m1=68:6885, m2=80:12158, y=148:23148)
- Layer 36: ` tap`, `留存`, `俯`, `otas`, ` equations` (target ranks: p1=17:11720, p2=4:1752, p3=16:4382, p4=5:9810, m1=68:3579, m2=80:11569, y=148:11837)
- Layer 37: `俯`, `留存`, `班的`, `otas`, `dividers` (target ranks: p1=17:34602, p2=4:5979, p3=16:8329, p4=5:52058, m1=68:14194, m2=80:35369, y=148:18206)
- Layer 38: `下沉`, `otan`, `calcul`, `dividers`, `y` (target ranks: p1=17:54699, p2=4:8080, p3=16:15310, p4=5:74581, m1=68:24532, m2=80:48074, y=148:28482)
- Layer 39: `}<?`, `东海`, `<｜begin▁of▁sentence｜>`, `下沉`, `迷惑` (target ranks: p1=17:60339, p2=4:75536, p3=16:40854, p4=5:95737, m1=68:37058, m2=80:77556, y=148:70356)
- Layer 40: `y`, `留存`, ` .`, `俯`, `acular` (target ranks: p1=17:33047, p2=4:35416, p3=16:20194, p4=5:53023, m1=68:20862, m2=80:76858, y=148:58450)
- Layer 41: ` .`, ` `, ` .↵↵`, `y`, `留存` (target ranks: p1=17:21164, p2=4:10393, p3=16:13288, p4=5:5417, m1=68:31055, m2=80:63354, y=148:22636)

### Filler position 21 (absolute token 753, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=17:127189, p2=4:128800, p3=16:127281, p4=5:128794, m1=68:125560, m2=80:127578, y=148:123320)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: p1=17:10435, p2=4:3801, p3=16:8973, p4=5:3719, m1=68:10457, m2=80:12575, y=148:26681)
- Layer 20: ` TA`, ` Corporation`, `ait`, ` biotic`, `锁定` (target ranks: p1=17:30878, p2=4:36036, p3=16:28926, p4=5:28428, m1=68:26782, m2=80:39505, y=148:68823)
- Layer 30: `}using`, `}<?`, ` spac`, `dividers`, `acos` (target ranks: p1=17:88397, p2=4:119835, p3=16:96841, p4=5:116056, m1=68:69396, m2=80:102247, y=148:116978)
- Layer 35: `二十二`, `}using`, `dividers`, `滴水`, ` .` (target ranks: p1=17:29793, p2=4:103360, p3=16:56591, p4=5:83888, m1=68:27974, m2=80:101538, y=148:105090)
- Layer 36: `陌生`, `反复`, `滴水`, ` blank`, `水土` (target ranks: p1=17:10932, p2=4:48879, p3=16:31046, p4=5:32266, m1=68:4007, m2=80:63341, y=148:61176)
- Layer 37: `}<?`, `坏`, ` covari`, `合并`, `铎` (target ranks: p1=17:46247, p2=4:87291, p3=16:53186, p4=5:86923, m1=68:18978, m2=80:86717, y=148:61922)
- Layer 38: ` .`, ` covari`, `坏`, ` club`, ` .↵↵` (target ranks: p1=17:16408, p2=4:62171, p3=16:16898, p4=5:75691, m1=68:7360, m2=80:61201, y=148:85289)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `坏`, `铎`, ` covari` (target ranks: p1=17:44518, p2=4:111323, p3=16:65289, p4=5:102627, m1=68:29298, m2=80:96368, y=148:112388)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: p1=17:13616, p2=4:66526, p3=16:28091, p4=5:49686, m1=68:17133, m2=80:72608, y=148:82878)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `这就是`, ` except` (target ranks: p1=17:4612, p2=4:8710, p3=16:8619, p4=5:6682, m1=68:7888, m2=80:47617, y=148:37662)

### Filler position 22 (absolute token 754, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `datasetId` (target ranks: p1=17:127516, p2=4:128919, p3=16:127640, p4=5:128911, m1=68:125933, m2=80:127899, y=148:123781)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: p1=17:9687, p2=4:3327, p3=16:8277, p4=5:3382, m1=68:9585, m2=80:11823, y=148:26061)
- Layer 20: ` quadr`, `ait`, ` smile`, `cape`, `锁定` (target ranks: p1=17:1894, p2=4:192, p3=16:1050, p4=5:673, m1=68:978, m2=80:625, y=148:23133)
- Layer 30: ` pessimistic`, `setting`, `俯`, ` optimistic`, ` accompan` (target ranks: p1=17:8972, p2=4:72635, p3=16:24861, p4=5:69319, m1=68:1510, m2=80:3977, y=148:80931)
- Layer 35: `114`, `138`, `136`, ` Pop`, `168` (target ranks: p1=17:1656, p2=4:15605, p3=16:7431, p4=5:27191, m1=68:23, m2=80:481, y=148:1612)
- Layer 36: `138`, `136`, `114`, `116`, `}using` (target ranks: p1=17:13667, p2=4:20855, p3=16:11590, p4=5:39803, m1=68:116, m2=80:991, y=148:88)
- Layer 37: `本题分析`, `?datasetId`, `codeline`, `祭`, `}using` (target ranks: p1=17:59478, p2=4:74765, p3=16:34463, p4=5:99264, m1=68:3751, m2=80:9536, y=148:235)
- Layer 38: `本题分析`, `}<?`, `}using`, `?datasetId`, `ucl` (target ranks: p1=17:93097, p2=4:87322, p3=16:49474, p4=5:112524, m1=68:9600, m2=80:17133, y=148:416)
- Layer 39: `}<?`, `东海`, `ozygous`, `}using`, `opters` (target ranks: p1=17:94700, p2=4:107544, p3=16:84520, p4=5:119299, m1=68:26630, m2=80:29468, y=148:182)
- Layer 40: `136`, `138`, `114`, `135`, ` ` (target ranks: p1=17:41191, p2=4:38749, p3=16:40828, p4=5:63888, m1=68:6694, m2=80:7306, y=148:121)
- Layer 41: ` .`, ` `, ` .↵↵`, `随便`, `<｜end▁of▁sentence｜>` (target ranks: p1=17:19124, p2=4:10210, p3=16:20124, p4=5:8364, m1=68:3734, m2=80:9016, y=148:901)

### Filler position 23 (absolute token 755, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `aplenty`, `-ulo` (target ranks: p1=17:127385, p2=4:128876, p3=16:127492, p4=5:128874, m1=68:125761, m2=80:127794, y=148:123636)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: p1=17:8935, p2=4:3034, p3=16:7815, p4=5:3021, m1=68:9042, m2=80:11498, y=148:26286)
- Layer 20: `Dutch`, `)Skip`, ` Dutch`, `吞`, `tails` (target ranks: p1=17:16102, p2=4:7943, p3=16:30494, p4=5:12621, m1=68:21679, m2=80:14516, y=148:28972)
- Layer 30: `codeline`, `东京`, ` singly`, `)Skip`, `东海` (target ranks: p1=17:83249, p2=4:86200, p3=16:100086, p4=5:96492, m1=68:82132, m2=80:64666, y=148:102326)
- Layer 35: `codeline`, `坏`, ` nasod`, `删`, `�` (target ranks: p1=17:56760, p2=4:83646, p3=16:102377, p4=5:89202, m1=68:60127, m2=80:41709, y=148:119755)
- Layer 36: `坏`, `停`, ` nasod`, ` soci`, `告诉我们` (target ranks: p1=17:33409, p2=4:46775, p3=16:77980, p4=5:50962, m1=68:16333, m2=80:15678, y=148:86641)
- Layer 37: `镶嵌`, `肤`, `贻`, ` germ`, ` tide` (target ranks: p1=17:88969, p2=4:65234, p3=16:106746, p4=5:99024, m1=68:68854, m2=80:57487, y=148:123001)
- Layer 38: `肤`, ` germ`, `镶嵌`, `锚`, ` .` (target ranks: p1=17:48300, p2=4:53577, p3=16:59885, p4=5:76164, m1=68:50574, m2=80:66716, y=148:120492)
- Layer 39: ` encomp`, ` .`, ` unflagged`, `肤`, ` germ` (target ranks: p1=17:85407, p2=4:118096, p3=16:110682, p4=5:116749, m1=68:105758, m2=80:107454, y=148:119043)
- Layer 40: ` .`, ` .↵↵`, `肤`, ` .↵`, `镶嵌` (target ranks: p1=17:52738, p2=4:95356, p3=16:90225, p4=5:90949, m1=68:108627, m2=80:103779, y=148:118587)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `一个个` (target ranks: p1=17:15809, p2=4:62395, p3=16:39006, p4=5:46665, m1=68:79445, m2=80:56069, y=148:88265)

### Filler position 24 (absolute token 756, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `aplenty` (target ranks: p1=17:127438, p2=4:128897, p3=16:127583, p4=5:128891, m1=68:125869, m2=80:127860, y=148:123705)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: p1=17:9035, p2=4:2990, p3=16:7638, p4=5:3073, m1=68:8997, m2=80:11456, y=148:25218)
- Layer 20: ` smile`, `cape`, `足`, `站`, `肩` (target ranks: p1=17:1605, p2=4:34, p3=16:629, p4=5:335, m1=68:349, m2=80:842, y=148:9596)
- Layer 30: `codeline`, `</think>`, ` Answer`, `hatic`, `答案是` (target ranks: p1=17:115488, p2=4:109170, p3=16:114312, p4=5:107445, m1=68:91918, m2=80:116885, y=148:119774)
- Layer 35: `codeline`, `AED`, ` Answer`, ` tagged`, ` sleep` (target ranks: p1=17:115900, p2=4:99239, p3=16:112894, p4=5:98998, m1=68:59106, m2=80:69676, y=148:127471)
- Layer 36: ` nasod`, `codeline`, `坏`, ` Answer`, `良` (target ranks: p1=17:62820, p2=4:39643, p3=16:53381, p4=5:32089, m1=68:5572, m2=80:11902, y=148:113228)
- Layer 37: `codeline`, `hatic`, `oNames`, `okens`, `�` (target ranks: p1=17:116202, p2=4:107857, p3=16:117642, p4=5:119203, m1=68:110730, m2=80:87978, y=148:117838)
- Layer 38: `hatic`, `codeline`, `okens`, `oNames`, `�` (target ranks: p1=17:117724, p2=4:108264, p3=16:121411, p4=5:115796, m1=68:103241, m2=80:61279, y=148:113680)
- Layer 39: `hatic`, `codeline`, `-ulo`, ` begg`, `oxygen` (target ranks: p1=17:104893, p2=4:115921, p3=16:113413, p4=5:110992, m1=68:74063, m2=80:81655, y=148:114617)
- Layer 40: ` Answer`, `Answer`, ` .↵↵`, `叮`, ` begg` (target ranks: p1=17:38898, p2=4:35933, p3=16:54292, p4=5:26757, m1=68:20084, m2=80:22084, y=148:93984)
- Layer 41: ` Answer`, ` .`, ` .↵↵`, `Answer`, ` .↵` (target ranks: p1=17:11739, p2=4:10891, p3=16:10304, p4=5:4675, m1=68:22988, m2=80:13876, y=148:59783)

### Filler position 25 (absolute token 757, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `EDMF` (target ranks: p1=17:121482, p2=4:126598, p3=16:122440, p4=5:126522, m1=68:121791, m2=80:120982, y=148:108405)
- Layer 10: `tas`, `cookie`, `eine`, `Achie`, `ej` (target ranks: p1=17:51365, p2=4:41899, p3=16:56848, p4=5:41432, m1=68:54491, m2=80:59839, y=148:28259)
- Layer 20: `ait`, `能被`, `坷`, `忑`, ` Submission` (target ranks: p1=17:13661, p2=4:3824, p3=16:9804, p4=5:2758, m1=68:6493, m2=80:8893, y=148:41842)
- Layer 30: ` Paglin`, `北辰`, `malink`, `有意`, ` dátummal` (target ranks: p1=17:7129, p2=4:120000, p3=16:11018, p4=5:109465, m1=68:4077, m2=80:41300, y=148:39535)
- Layer 35: `129`, `135`, `138`, `正确答案`, `105` (target ranks: p1=17:5184, p2=4:96506, p3=16:43885, p4=5:63009, m1=68:3003, m2=80:13496, y=148:232)
- Layer 36: `155`, `135`, `正确答案`, `105`, `149` (target ranks: p1=17:27866, p2=4:92376, p3=16:72055, p4=5:49598, m1=68:21826, m2=80:39151, y=148:37)
- Layer 37: ` Paglin`, `155`, `135`, `roma`, ` Cottage` (target ranks: p1=17:71350, p2=4:120404, p3=16:103426, p4=5:103923, m1=68:82218, m2=80:93357, y=148:173)
- Layer 38: ` Paglin`, `生意`, `agem`, `清气`, `romes` (target ranks: p1=17:104791, p2=4:124445, p3=16:120131, p4=5:116874, m1=68:110215, m2=80:108121, y=148:2832)
- Layer 39: ` Answer`, `答案`, ` Paglin`, ` Antwort`, ` answer` (target ranks: p1=17:116393, p2=4:122601, p3=16:119734, p4=5:119067, m1=68:112331, m2=80:95867, y=148:20928)
- Layer 40: ` Answer`, `Answer`, ` answer`, `回答`, `_answer` (target ranks: p1=17:51902, p2=4:69061, p3=16:56430, p4=5:59736, m1=68:80245, m2=80:35536, y=148:7854)
- Layer 41: `Answer`, ` Answer`, ` answer`, `回答`, `answer` (target ranks: p1=17:5737, p2=4:1746, p3=16:3414, p4=5:1260, m1=68:21627, m2=80:7942, y=148:2683)

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

Answer:<｜Assistant｜></think>80<｜end▁of▁sentence｜><｜User｜>a = 9
b = 8
c = 10
d = 6
e = 6
f = 10
g = 7
h = 2
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
