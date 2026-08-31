# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `256` (incorrect).
- No-filler answer: `31` (incorrect).
- Filler tokens: 10 tokens at absolute indices 448–457.
- Final-head closure max absolute logit error: `0.000965118408203125`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `x_1=15` | 2569 (L20, filler 1) | Never |
| J-Lens | `x_2=225` | 23 (L36, filler 4) | Never |
| J-Lens | `x_3=14` | 2898 (L21, filler 4) | Never |
| J-Lens | `x_4=196` | 366 (L35, filler 4) | Never |
| J-Lens | `x_5=103` | 2157 (L36, filler 4) | Never |
| J-Lens | `x_6=203` | 187 (L36, filler 4) | Never |
| J-Lens | `x_7=58` | 148 (L35, filler 4) | Never |
| J-Lens | `x_8=53` | 31 (L35, filler 4) | Never |
| Logit lens | `x_1=15` | 178 (L5, filler 1) | Never |
| Logit lens | `x_2=225` | 3 (L36, filler 4) | L30, filler 4 (rank 7) |
| Logit lens | `x_3=14` | 1036 (L24, filler 4) | Never |
| Logit lens | `x_4=196` | 92 (L31, filler 4) | Never |
| Logit lens | `x_5=103` | 233 (L30, filler 4) | Never |
| Logit lens | `x_6=203` | 76 (L36, filler 4) | Never |
| Logit lens | `x_7=58` | 168 (L34, filler 4) | Never |
| Logit lens | `x_8=53` | 58 (L34, filler 4) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 448, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `(migrations` (target ranks: x_1=15:121066, x_2=225:118015, x_3=14:121831, x_4=196:113913, x_5=103:111964, x_6=203:109417, x_7=58:118784, x_8=53:118540)
- Layer 10: `Walker`, ` Walker`, `锁定`, `fine`, `cape` (target ranks: x_1=15:22189, x_2=225:32988, x_3=14:28540, x_4=196:38253, x_5=103:35467, x_6=203:39185, x_7=58:22545, x_8=53:27459)
- Layer 20: `cape`, `足`, `甸`, `旬`, `表面` (target ranks: x_1=15:2569, x_2=225:26296, x_3=14:3857, x_4=196:13728, x_5=103:13451, x_6=203:23192, x_7=58:1870, x_8=53:2460)
- Layer 30: `期望`, `提问`, ` question`, ` recurs`, `重复` (target ranks: x_1=15:42830, x_2=225:102093, x_3=14:49812, x_4=196:91204, x_5=103:66596, x_6=203:30561, x_7=58:59548, x_8=53:72815)
- Layer 35: ` Question`, ` question`, `Question`, `重复`, `提问` (target ranks: x_1=15:7392, x_2=225:62717, x_3=14:7877, x_4=196:69846, x_5=103:49703, x_6=203:18900, x_7=58:24802, x_8=53:29463)
- Layer 36: `重复`, ` Question`, ` question`, `期望`, `询问` (target ranks: x_1=15:4257, x_2=225:28665, x_3=14:5396, x_4=196:49989, x_5=103:17930, x_6=203:9915, x_7=58:15251, x_8=53:16374)
- Layer 37: ` question`, ` Question`, ` floating`, `/question`, `提问` (target ranks: x_1=15:21297, x_2=225:36420, x_3=14:33839, x_4=196:86836, x_5=103:61956, x_6=203:32015, x_7=58:76179, x_8=53:79325)
- Layer 38: ` talags`, ` Question`, ` floating`, ` random`, `/question` (target ranks: x_1=15:49685, x_2=225:71074, x_3=14:66216, x_4=196:100075, x_5=103:83371, x_6=203:58204, x_7=58:95714, x_8=53:101383)
- Layer 39: ` talags`, `hatic`, ` Noruwega`, `tanle`, `到了一` (target ranks: x_1=15:114949, x_2=225:113823, x_3=14:127256, x_4=196:126621, x_5=103:121221, x_6=203:125207, x_7=58:112328, x_8=53:112996)
- Layer 40: ` talags`, `dots`, ` dots`, ` filler`, `oooo` (target ranks: x_1=15:79052, x_2=225:91731, x_3=14:120485, x_4=196:121074, x_5=103:92372, x_6=203:123610, x_7=58:81448, x_8=53:68320)
- Layer 41: ` .`, ` .↵↵`, `准备好了`, ` separately`, ` .↵` (target ranks: x_1=15:47813, x_2=225:36751, x_3=14:92681, x_4=196:106341, x_5=103:63120, x_6=203:102267, x_7=58:16289, x_8=53:43210)

### Filler position 2 (absolute token 449, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: x_1=15:123665, x_2=225:121769, x_3=14:122839, x_4=196:117484, x_5=103:118678, x_6=203:117207, x_7=58:121305, x_8=53:121355)
- Layer 10: ` Walker`, `从哪里`, `忑`, `ait`, `anta` (target ranks: x_1=15:25907, x_2=225:34490, x_3=14:24189, x_4=196:34799, x_5=103:50060, x_6=203:58054, x_7=58:28037, x_8=53:34845)
- Layer 20: ` .`, ` .----`, `/.`, `ools`, ` .↵↵` (target ranks: x_1=15:114462, x_2=225:108391, x_3=14:107668, x_4=196:96246, x_5=103:120670, x_6=203:124407, x_7=58:94376, x_8=53:117686)
- Layer 30: ` dekameters`, ` hilabihan`, ` .----`, ` .`, `dot` (target ranks: x_1=15:119610, x_2=225:110630, x_3=14:121858, x_4=196:121776, x_5=103:125697, x_6=203:126976, x_7=58:125600, x_8=53:127955)
- Layer 35: ` .`, ` hilabihan`, `dot`, ` dot`, `Dot` (target ranks: x_1=15:109532, x_2=225:119767, x_3=14:97605, x_4=196:121712, x_5=103:125327, x_6=203:128520, x_7=58:124377, x_8=53:125819)
- Layer 36: ` Theodor`, `dots`, `odor`, `dot`, ` .` (target ranks: x_1=15:73952, x_2=225:93346, x_3=14:62053, x_4=196:114850, x_5=103:111690, x_6=203:127907, x_7=58:98063, x_8=53:114225)
- Layer 37: ` hilabihan`, ` Erkännande`, ` licensierad`, `}<?`, `EDMF` (target ranks: x_1=15:122188, x_2=225:113713, x_3=14:122444, x_4=196:113435, x_5=103:123130, x_6=203:128504, x_7=58:122306, x_8=53:124473)
- Layer 38: ` .`, ` .↵↵`, `用了`, ` .↵`, `殿堂` (target ranks: x_1=15:106740, x_2=225:95579, x_3=14:107779, x_4=196:100443, x_5=103:118097, x_6=203:128560, x_7=58:111424, x_8=53:120588)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, ` hilabihan`, ` .----` (target ranks: x_1=15:117196, x_2=225:98547, x_3=14:119816, x_4=196:113403, x_5=103:112833, x_6=203:128058, x_7=58:117012, x_8=53:117344)
- Layer 40: ` .`, ` filler`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: x_1=15:84386, x_2=225:32882, x_3=14:79051, x_4=196:70683, x_5=103:75432, x_6=203:119240, x_7=58:86045, x_8=53:71430)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` filler`, ` ,` (target ranks: x_1=15:38209, x_2=225:4875, x_3=14:28077, x_4=196:34207, x_5=103:33324, x_6=203:82269, x_7=58:22113, x_8=53:27400)

### Filler position 3 (absolute token 450, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126326, x_2=225:124195, x_3=14:125507, x_4=196:119128, x_5=103:121482, x_6=203:120842, x_7=58:124792, x_8=53:124831)
- Layer 10: ` Walker`, `ait`, `锁定`, `忑`, `Walker` (target ranks: x_1=15:13325, x_2=225:19701, x_3=14:11929, x_4=196:23127, x_5=103:28195, x_6=203:30962, x_7=58:14857, x_8=53:16085)
- Layer 20: `�`, `s`, `�`, `足`, ` ternary` (target ranks: x_1=15:12944, x_2=225:13797, x_3=14:10449, x_4=196:39812, x_5=103:31538, x_6=203:29431, x_7=58:16222, x_8=53:4717)
- Layer 30: ` calculator`, ` modulus`, `计算的`, ` repetitions`, `calcul` (target ranks: x_1=15:9011, x_2=225:4424, x_3=14:11718, x_4=196:14253, x_5=103:53637, x_6=203:12076, x_7=58:22960, x_8=53:7542)
- Layer 35: ` repeated`, ` repetitions`, ` repetition`, ` squares`, `重复` (target ranks: x_1=15:7053, x_2=225:1770, x_3=14:5646, x_4=196:12889, x_5=103:27342, x_6=203:6305, x_7=58:14950, x_8=53:3479)
- Layer 36: ` repeated`, `重复`, ` repetitions`, `反复`, ` Repeated` (target ranks: x_1=15:8800, x_2=225:517, x_3=14:8036, x_4=196:8434, x_5=103:16352, x_6=203:3591, x_7=58:10015, x_8=53:2905)
- Layer 37: ` repeated`, `反复`, ` modular`, ` squ`, ` repetitions` (target ranks: x_1=15:32868, x_2=225:514, x_3=14:29528, x_4=196:17975, x_5=103:22448, x_6=203:4845, x_7=58:40296, x_8=53:13061)
- Layer 38: ` squ`, ` Squ`, ` modular`, ` repeated`, ` quadratic` (target ranks: x_1=15:63117, x_2=225:2572, x_3=14:53733, x_4=196:41773, x_5=103:34800, x_6=203:11081, x_7=58:63210, x_8=53:26781)
- Layer 39: ` iter`, ` repeated`, `反复`, `ologists`, ` repeatedly` (target ranks: x_1=15:109756, x_2=225:82044, x_3=14:114501, x_4=196:122688, x_5=103:125389, x_6=203:126359, x_7=58:106383, x_8=53:108831)
- Layer 40: ` repeated`, ` x`, `反复`, ` repeatedly`, ` repeating` (target ranks: x_1=15:54038, x_2=225:45597, x_3=14:68083, x_4=196:108118, x_5=103:121216, x_6=203:118871, x_7=58:70619, x_8=53:66530)
- Layer 41: ` .`, ` patiently`, ` repeatedly`, ` repeated`, ` dots` (target ranks: x_1=15:33076, x_2=225:21863, x_3=14:33370, x_4=196:56253, x_5=103:100710, x_6=203:106892, x_7=58:15488, x_8=53:45793)

### Filler position 4 (absolute token 451, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126993, x_2=225:125432, x_3=14:126468, x_4=196:120265, x_5=103:122946, x_6=203:121966, x_7=58:125348, x_8=53:125270)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: x_1=15:11175, x_2=225:18337, x_3=14:10750, x_4=196:23172, x_5=103:25809, x_6=203:28535, x_7=58:14071, x_8=53:14943)
- Layer 20: `ait`, `cape`, `锁定`, `幽`, `胃癌` (target ranks: x_1=15:3693, x_2=225:12179, x_3=14:3792, x_4=196:20485, x_5=103:16207, x_6=203:23382, x_7=58:2397, x_8=53:2477)
- Layer 30: ` resort`, `保留`, `473`, `472`, `Tap` (target ranks: x_1=15:13093, x_2=225:1038, x_3=14:24594, x_4=196:911, x_5=103:2210, x_6=203:2527, x_7=58:2004, x_8=53:732)
- Layer 35: `保留`, `47`, `474`, `67`, ` repetition` (target ranks: x_1=15:6440, x_2=225:208, x_3=14:3827, x_4=196:366, x_5=103:4396, x_6=203:1695, x_7=58:148, x_8=53:31)
- Layer 36: `保留`, `474`, `296`, `354`, `bergh` (target ranks: x_1=15:32676, x_2=225:23, x_3=14:13252, x_4=196:986, x_5=103:2157, x_6=203:187, x_7=58:855, x_8=53:585)
- Layer 37: `354`, `替换`, `474`, `anin`, `第三百` (target ranks: x_1=15:55802, x_2=225:79, x_3=14:24249, x_4=196:2396, x_5=103:7794, x_6=203:641, x_7=58:4570, x_8=53:4844)
- Layer 38: `替换`, `本题分析`, ` dekameters`, ` pac`, `第三百` (target ranks: x_1=15:67663, x_2=225:81, x_3=14:22903, x_4=196:3786, x_5=103:6530, x_6=203:1139, x_7=58:6298, x_8=53:5851)
- Layer 39: `lez`, `本题分析`, `}<?`, ` prejud`, `osz` (target ranks: x_1=15:77961, x_2=225:2888, x_3=14:44883, x_4=196:15974, x_5=103:26346, x_6=203:9086, x_7=58:39663, x_8=53:31399)
- Layer 40: `anin`, `anine`, `anium`, ` ferm`, ` ` (target ranks: x_1=15:22604, x_2=225:168, x_3=14:10257, x_4=196:2203, x_5=103:6086, x_6=203:1349, x_7=58:16982, x_8=53:5955)
- Layer 41: ` .`, `anine`, ` .↵↵`, ` careful`, ` ,` (target ranks: x_1=15:14767, x_2=225:2722, x_3=14:12418, x_4=196:12114, x_5=103:22748, x_6=203:15283, x_7=58:6604, x_8=53:13689)

### Filler position 5 (absolute token 452, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126962, x_2=225:125613, x_3=14:126546, x_4=196:120177, x_5=103:123051, x_6=203:121634, x_7=58:125185, x_8=53:125088)
- Layer 10: ` Walker`, `Walker`, `锁定`, `挪`, `勾` (target ranks: x_1=15:15690, x_2=225:24972, x_3=14:16172, x_4=196:30957, x_5=103:31845, x_6=203:37915, x_7=58:19924, x_8=53:21654)
- Layer 20: `幽`, `足`, `鞍`, ` LS`, `锁定` (target ranks: x_1=15:16343, x_2=225:25838, x_3=14:25285, x_4=196:39913, x_5=103:36865, x_6=203:43935, x_7=58:17818, x_8=53:25177)
- Layer 30: `每一步`, `一步步`, `步步`, `第一步`, `步骤` (target ranks: x_1=15:29319, x_2=225:20477, x_3=14:33582, x_4=196:36361, x_5=103:21642, x_6=203:14633, x_7=58:17014, x_8=53:18157)
- Layer 35: ` Step`, ` step`, `步骤`, `Step`, ` Schritt` (target ranks: x_1=15:30344, x_2=225:28647, x_3=14:45176, x_4=196:49572, x_5=103:16919, x_6=203:14703, x_7=58:38325, x_8=53:31673)
- Layer 36: ` Step`, ` step`, `步骤`, `Step`, `一步` (target ranks: x_1=15:52626, x_2=225:19136, x_3=14:61581, x_4=196:43364, x_5=103:6649, x_6=203:6283, x_7=58:53011, x_8=53:49525)
- Layer 37: ` Step`, ` step`, `步骤`, `Step`, `-step` (target ranks: x_1=15:98122, x_2=225:41542, x_3=14:102922, x_4=196:81083, x_5=103:12980, x_6=203:9937, x_7=58:97375, x_8=53:92383)
- Layer 38: ` Step`, ` step`, `步骤`, `-step`, `一步` (target ranks: x_1=15:103698, x_2=225:42715, x_3=14:101926, x_4=196:76562, x_5=103:10810, x_6=203:20255, x_7=58:102722, x_8=53:95296)
- Layer 39: ` Step`, `步步`, `覆`, `一步`, `oNames` (target ranks: x_1=15:115835, x_2=225:108203, x_3=14:122191, x_4=196:119507, x_5=103:114642, x_6=203:122088, x_7=58:113150, x_8=53:120546)
- Layer 40: ` step`, `步骤`, `一步`, ` Step`, ` talags` (target ranks: x_1=15:97823, x_2=225:94571, x_3=14:106997, x_4=196:101928, x_5=103:91929, x_6=203:119603, x_7=58:98092, x_8=53:111403)
- Layer 41: ` .`, ` step`, ` careful`, `不如`, `步骤` (target ranks: x_1=15:70361, x_2=225:59474, x_3=14:80337, x_4=196:68948, x_5=103:70628, x_6=203:92730, x_7=58:30329, x_8=53:84022)

### Filler position 6 (absolute token 453, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126809, x_2=225:125669, x_3=14:126349, x_4=196:119800, x_5=103:122925, x_6=203:121257, x_7=58:124870, x_8=53:124784)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=15:12059, x_2=225:20286, x_3=14:11659, x_4=196:23872, x_5=103:27197, x_6=203:28392, x_7=58:14679, x_8=53:15211)
- Layer 20: `鞍`, `cape`, `锁定`, ` smile`, `挪` (target ranks: x_1=15:10891, x_2=225:23114, x_3=14:10685, x_4=196:25992, x_5=103:31314, x_6=203:30456, x_7=58:8673, x_8=53:7619)
- Layer 30: ` rational`, `理性的`, ` Rational`, ` rationality`, `Rational` (target ranks: x_1=15:50884, x_2=225:57523, x_3=14:36159, x_4=196:26658, x_5=103:41837, x_6=203:32793, x_7=58:33260, x_8=53:19310)
- Layer 35: ` rip`, ` repetition`, `重复`, `反复`, `ilig` (target ranks: x_1=15:21187, x_2=225:20299, x_3=14:12563, x_4=196:7679, x_5=103:14076, x_6=203:16283, x_7=58:2221, x_8=53:1314)
- Layer 36: ` rip`, `反复`, ` stabil`, `重复`, ` repeated` (target ranks: x_1=15:30983, x_2=225:17270, x_3=14:17853, x_4=196:7651, x_5=103:9064, x_6=203:14000, x_7=58:4422, x_8=53:2467)
- Layer 37: `anium`, `oNames`, ` stabil`, ` follow`, `onana` (target ranks: x_1=15:79820, x_2=225:24672, x_3=14:62100, x_4=196:28835, x_5=103:24944, x_6=203:44158, x_7=58:41477, x_8=53:27688)
- Layer 38: `}<?`, `oNames`, `aharan`, `下沉`, `hemer` (target ranks: x_1=15:114709, x_2=225:42958, x_3=14:99453, x_4=196:53977, x_5=103:30101, x_6=203:61724, x_7=58:66079, x_8=53:46934)
- Layer 39: `aharan`, `额外`, `繁体`, `把事情`, `hemer` (target ranks: x_1=15:115160, x_2=225:118965, x_3=14:120606, x_4=196:125043, x_5=103:126889, x_6=203:128573, x_7=58:114899, x_8=53:122517)
- Layer 40: ` dotted`, ` talags`, ` .`, ` dots`, `一个一个` (target ranks: x_1=15:88975, x_2=225:104227, x_3=14:97905, x_4=196:119520, x_5=103:122424, x_6=203:128317, x_7=58:90661, x_8=53:107627)
- Layer 41: ` .`, ` dotted`, ` .↵↵`, `一个一个`, ` ,` (target ranks: x_1=15:42262, x_2=225:44398, x_3=14:51305, x_4=196:80663, x_5=103:100590, x_6=203:118724, x_7=58:21765, x_8=53:68606)

### Filler position 7 (absolute token 454, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126669, x_2=225:125558, x_3=14:126239, x_4=196:119480, x_5=103:122685, x_6=203:120821, x_7=58:124707, x_8=53:124645)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: x_1=15:12604, x_2=225:21430, x_3=14:12523, x_4=196:25639, x_5=103:28831, x_6=203:30925, x_7=58:15018, x_8=53:16284)
- Layer 20: `锁定`, `鞍`, `忑`, ` smile`, ` cheer` (target ranks: x_1=15:7070, x_2=225:15826, x_3=14:13358, x_4=196:29270, x_5=103:29047, x_6=203:27339, x_7=58:8824, x_8=53:9681)
- Layer 30: `一步步`, ` step`, `步骤`, `步步`, `一步一步` (target ranks: x_1=15:55064, x_2=225:48955, x_3=14:99159, x_4=196:81814, x_5=103:58687, x_6=203:51323, x_7=58:25986, x_8=53:19015)
- Layer 35: ` step`, `步骤`, ` Step`, ` steps`, `Step` (target ranks: x_1=15:28084, x_2=225:34679, x_3=14:64789, x_4=196:56947, x_5=103:29927, x_6=203:38892, x_7=58:13836, x_8=53:10430)
- Layer 36: ` step`, ` Step`, `步骤`, `Step`, ` steps` (target ranks: x_1=15:29175, x_2=225:18690, x_3=14:51386, x_4=196:47471, x_5=103:10849, x_6=203:20932, x_7=58:15166, x_8=53:13309)
- Layer 37: ` step`, ` Step`, `步骤`, `步步`, `三步` (target ranks: x_1=15:67814, x_2=225:27420, x_3=14:97788, x_4=196:82725, x_5=103:20566, x_6=203:39660, x_7=58:44881, x_8=53:42637)
- Layer 38: ` Step`, ` step`, `步步`, `步骤`, `一步步` (target ranks: x_1=15:94711, x_2=225:45284, x_3=14:106120, x_4=196:89662, x_5=103:24586, x_6=203:53616, x_7=58:72781, x_8=53:71293)
- Layer 39: `个好`, `一个好`, ` Fusion`, `繁体`, `厚厚的` (target ranks: x_1=15:113354, x_2=225:114876, x_3=14:119360, x_4=196:123565, x_5=103:120592, x_6=203:127231, x_7=58:102333, x_8=53:117231)
- Layer 40: ` .`, ` dotted`, ` fifty`, `五十`, `留存` (target ranks: x_1=15:73627, x_2=225:91122, x_3=14:86755, x_4=196:114803, x_5=103:105226, x_6=203:124475, x_7=58:54199, x_8=53:89795)
- Layer 41: ` .`, ` .↵↵`, ` fifty`, `一个好`, ` ..` (target ranks: x_1=15:51788, x_2=225:50992, x_3=14:57900, x_4=196:84975, x_5=103:82327, x_6=203:109876, x_7=58:14165, x_8=53:56176)

### Filler position 8 (absolute token 455, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126484, x_2=225:125330, x_3=14:126044, x_4=196:119072, x_5=103:122383, x_6=203:120518, x_7=58:124608, x_8=53:124588)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=15:11072, x_2=225:19916, x_3=14:10781, x_4=196:23046, x_5=103:26784, x_6=203:29451, x_7=58:13209, x_8=53:14183)
- Layer 20: ` Walker`, ` quadr`, ` smile`, `锁定`, `ait` (target ranks: x_1=15:4734, x_2=225:28037, x_3=14:11151, x_4=196:25124, x_5=103:39044, x_6=203:33020, x_7=58:4772, x_8=53:9145)
- Layer 30: `codeline`, ` spac`, `东京`, `dividers`, `Quintal` (target ranks: x_1=15:97290, x_2=225:118170, x_3=14:123815, x_4=196:120440, x_5=103:72823, x_6=203:109851, x_7=58:88439, x_8=53:96286)
- Layer 35: ` .`, `不急`, `川`, `耐心的`, `重复` (target ranks: x_1=15:37327, x_2=225:110365, x_3=14:99699, x_4=196:113772, x_5=103:65846, x_6=203:114346, x_7=58:59805, x_8=53:53414)
- Layer 36: `重复`, ` soci`, ` Soci`, `留存`, `川` (target ranks: x_1=15:15311, x_2=225:89139, x_3=14:74417, x_4=196:99237, x_5=103:21416, x_6=203:90526, x_7=58:24635, x_8=53:29113)
- Layer 37: `codeline`, `悬挂`, `Quintal`, `TreeLabel`, `挂` (target ranks: x_1=15:85027, x_2=225:112764, x_3=14:116008, x_4=196:113455, x_5=103:84009, x_6=203:118214, x_7=58:87089, x_8=53:93654)
- Layer 38: ` .`, `悬挂`, ` .↵↵`, `oooo`, `usk` (target ranks: x_1=15:61968, x_2=225:76721, x_3=14:94792, x_4=196:108408, x_5=103:44725, x_6=203:95613, x_7=58:70832, x_8=53:68354)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `aharan`, `悬挂` (target ranks: x_1=15:98232, x_2=225:101604, x_3=14:116792, x_4=196:118841, x_5=103:109899, x_6=203:121400, x_7=58:88001, x_8=53:98671)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `dots`, ` dots` (target ranks: x_1=15:62959, x_2=225:57176, x_3=14:89098, x_4=196:111422, x_5=103:81760, x_6=203:110210, x_7=58:45823, x_8=53:60692)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `oooo`, ` ,` (target ranks: x_1=15:19105, x_2=225:12622, x_3=14:54655, x_4=196:59813, x_5=103:25614, x_6=203:72587, x_7=58:6903, x_8=53:19310)

### Filler position 9 (absolute token 456, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126578, x_2=225:125618, x_3=14:126112, x_4=196:119293, x_5=103:122675, x_6=203:120861, x_7=58:124579, x_8=53:124606)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `挪` (target ranks: x_1=15:10386, x_2=225:19048, x_3=14:10107, x_4=196:21344, x_5=103:25248, x_6=203:30056, x_7=58:12678, x_8=53:13981)
- Layer 20: `eight`, ` pandemic`, ` coronavirus`, ` pandemia`, `重复` (target ranks: x_1=15:38083, x_2=225:79804, x_3=14:77899, x_4=196:11130, x_5=103:111584, x_6=203:103373, x_7=58:66261, x_8=53:42352)
- Layer 30: `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`, `}<?`, `?datasetId`, `aplenty`, `codeline` (target ranks: x_1=15:121062, x_2=225:124242, x_3=14:126613, x_4=196:107401, x_5=103:125427, x_6=203:119120, x_7=58:114794, x_8=53:108734)
- Layer 35: `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`, `}<?`, `?datasetId`, `\\\\\\\\\\\\\\\\`, `洪荒` (target ranks: x_1=15:120032, x_2=225:123945, x_3=14:128442, x_4=196:102970, x_5=103:121657, x_6=203:118021, x_7=58:121949, x_8=53:111052)
- Layer 36: `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`, ` doubling`, `oNames`, ` doubled`, `洪荒` (target ranks: x_1=15:104753, x_2=225:122630, x_3=14:126604, x_4=196:103807, x_5=103:112851, x_6=203:111898, x_7=58:111747, x_8=53:105993)
- Layer 37: `本题分析`, `ِّف`, `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`, `}<?`, ` Erkännande` (target ranks: x_1=15:111808, x_2=225:113959, x_3=14:123402, x_4=196:84352, x_5=103:122605, x_6=203:117499, x_7=58:124008, x_8=53:119569)
- Layer 38: `�`, `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`, `}<?`, `本题分析`, ` Thom` (target ranks: x_1=15:119394, x_2=225:102777, x_3=14:125308, x_4=196:103301, x_5=103:120203, x_6=203:111640, x_7=58:122028, x_8=53:116486)
- Layer 39: ` .----`, `本题分析`, ` Erkännande`, `树叶`, `寵` (target ranks: x_1=15:121814, x_2=225:62481, x_3=14:127185, x_4=196:103969, x_5=103:96277, x_6=203:69269, x_7=58:116572, x_8=53:105884)
- Layer 40: ` .↵↵`, ` .`, ` .↵`, ` Answer`, `oooo` (target ranks: x_1=15:81247, x_2=225:9646, x_3=14:113894, x_4=196:65251, x_5=103:35296, x_6=203:40091, x_7=58:68956, x_8=53:38249)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, ` ..`, ` ...` (target ranks: x_1=15:17829, x_2=225:2875, x_3=14:45560, x_4=196:23065, x_5=103:34727, x_6=203:21814, x_7=58:12811, x_8=53:6037)

### Filler position 10 (absolute token 457, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `-ulo` (target ranks: x_1=15:121442, x_2=225:115870, x_3=14:121505, x_4=196:112230, x_5=103:110759, x_6=203:109940, x_7=58:120283, x_8=53:119860)
- Layer 10: `основним`, ` everydaycalculation`, `xjzy`, `eva`, `som` (target ranks: x_1=15:124172, x_2=225:91215, x_3=14:128571, x_4=196:113740, x_5=103:85850, x_6=203:110467, x_7=58:128890, x_8=53:128616)
- Layer 20: `Sequ`, `答复`, `哪位`, `ait`, `回答` (target ranks: x_1=15:12823, x_2=225:43425, x_3=14:24525, x_4=196:35749, x_5=103:31171, x_6=203:28624, x_7=58:20325, x_8=53:15303)
- Layer 30: ` Answer`, `答案`, ` answer`, ` ответ`, `答案是` (target ranks: x_1=15:82705, x_2=225:110993, x_3=14:103750, x_4=196:73893, x_5=103:77967, x_6=203:7557, x_7=58:95691, x_8=53:105816)
- Layer 35: ` dátummal`, ` Answer`, `解答`, ` licensierad`, ` medief` (target ranks: x_1=15:62314, x_2=225:125228, x_3=14:103138, x_4=196:90319, x_5=103:102085, x_6=203:40801, x_7=58:55821, x_8=53:93216)
- Layer 36: ` Answer`, ` dátummal`, ` answer`, `_answer`, `想了` (target ranks: x_1=15:55038, x_2=225:124667, x_3=14:88223, x_4=196:87816, x_5=103:95294, x_6=203:41330, x_7=58:35246, x_8=53:82986)
- Layer 37: ` Answer`, ` dátummal`, ` licensierad`, `Answer`, `_answer` (target ranks: x_1=15:81311, x_2=225:113406, x_3=14:102942, x_4=196:91723, x_5=103:81333, x_6=203:36190, x_7=58:76864, x_8=53:92313)
- Layer 38: ` Answer`, `Answer`, `_answer`, `answer`, ` answer` (target ranks: x_1=15:104344, x_2=225:102500, x_3=14:107440, x_4=196:78032, x_5=103:48644, x_6=203:39099, x_7=58:78849, x_8=53:95512)
- Layer 39: ` Answer`, `Answer`, `(answer`, `_answer`, `answer` (target ranks: x_1=15:97234, x_2=225:101938, x_3=14:117946, x_4=196:90000, x_5=103:100066, x_6=203:74283, x_7=58:113403, x_8=53:107779)
- Layer 40: `Answer`, ` Answer`, ` answer`, `答`, `_answer` (target ranks: x_1=15:27527, x_2=225:27059, x_3=14:54513, x_4=196:22569, x_5=103:49785, x_6=203:27998, x_7=58:36552, x_8=53:25283)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `答` (target ranks: x_1=15:2683, x_2=225:12326, x_3=14:5832, x_4=196:7441, x_5=103:25903, x_6=203:23329, x_7=58:7122, x_8=53:7326)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given integers x, N, and T. Set x_0 = x mod N, then repeatedly apply x_t = x_(t-1)^2 mod N exactly T times. Answer immediately with just x_T as a base-10 integer, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be some filler tokens (a sequence of dots) to give you extra space to process the problem before answering.<｜User｜>Question: Starting with x_0 = 2 mod 55, repeatedly apply x_t = x_(t-1)^2 mod 55 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>36<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 3 mod 77, repeatedly apply x_t = x_(t-1)^2 mod 77 for exactly 4 steps. What is x_4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>25<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 5 mod 143, repeatedly apply x_t = x_(t-1)^2 mod 143 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>92<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 7 mod 221, repeatedly apply x_t = x_(t-1)^2 mod 221 for exactly 4 steps. What is x_4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>35<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 11 mod 247, repeatedly apply x_t = x_(t-1)^2 mod 247 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 31 mod 473, repeatedly apply x_t = x_(t-1)^2 mod 473 for exactly 8 steps. What is x_8?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
