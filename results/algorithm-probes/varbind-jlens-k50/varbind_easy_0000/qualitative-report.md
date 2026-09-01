# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `219` (correct).
- No-filler answer: `219` (correct).
- Filler tokens: 50 tokens at absolute indices 809–858.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=59` | 1 (L27, filler 19) | L24, filler 19 (rank 8) |
| J-Lens | `first_product=118` | 2 (L30, filler 36) | L30, filler 36 (rank 2) |
| J-Lens | `bound_value=117` | 1 (L30, filler 15) | L30, filler 15 (rank 1) |
| J-Lens | `second_product=234` | 1 (L33, filler 16) | L31, filler 15 (rank 6) |
| J-Lens | `answer=219` | 1 (L36, filler 10) | L35, filler 10 (rank 10) |
| Logit lens | `base_value=59` | 1 (L26, filler 15) | L24, filler 10 (rank 4) |
| Logit lens | `first_product=118` | 9 (L28, filler 15) | L28, filler 15 (rank 9) |
| Logit lens | `bound_value=117` | 1 (L29, filler 15) | L29, filler 15 (rank 1) |
| Logit lens | `second_product=234` | 1 (L33, filler 15) | L32, filler 15 (rank 5) |
| Logit lens | `answer=219` | 1 (L36, filler 10) | L31, filler 14 (rank 5) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 809, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=59:120155, first_product=118:111517, bound_value=117:111444, second_product=234:113126, answer=219:113751)
- Layer 10: `anta`, `fine`, `忑`, `locked`, `钩` (target ranks: base_value=59:37240, first_product=118:50293, bound_value=117:43763, second_product=234:47983, answer=219:61698)
- Layer 20: `足`, `扣`, `垂`, `旬`, `abric` (target ranks: base_value=59:1745, first_product=118:29993, bound_value=117:15943, second_product=234:15582, answer=219:34154)
- Layer 30: ` pakig`, `acin`, ` Hood`, ` eserc`, `推算` (target ranks: base_value=59:180, first_product=118:4094, bound_value=117:358, second_product=234:2715, answer=219:1915)
- Layer 35: ` labor`, `acin`, `期望`, `往外`, ` Hood` (target ranks: base_value=59:184, first_product=118:13909, bound_value=117:773, second_product=234:3576, answer=219:209)
- Layer 36: `acin`, `期待的`, `期望`, `期盼`, `期待` (target ranks: base_value=59:1271, first_product=118:14501, bound_value=117:499, second_product=234:5442, answer=219:339)
- Layer 37: ` talags`, ` الجرم`, ` pakig`, `}<?`, `在北京` (target ranks: base_value=59:40588, first_product=118:29067, bound_value=117:636, second_product=234:9720, answer=219:40)
- Layer 38: ` talags`, `}<?`, `tanle`, ` Thom`, `aharan` (target ranks: base_value=59:76991, first_product=118:88069, bound_value=117:6368, second_product=234:43909, answer=219:704)
- Layer 39: ` talags`, ` Millenniums`, `tanle`, `yyyy`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=59:124229, first_product=118:115533, bound_value=117:38518, second_product=234:62476, answer=219:484)
- Layer 40: ` talags`, `yyyy`, ` LD`, ` ald`, ` ld` (target ranks: base_value=59:125155, first_product=118:92199, bound_value=117:27783, second_product=234:43606, answer=219:90)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` separately`, `表现出来的` (target ranks: base_value=59:109090, first_product=118:61870, bound_value=117:23015, second_product=234:33041, answer=219:291)

### Filler position 2 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=59:121655, first_product=118:114651, bound_value=117:114926, second_product=234:113611, answer=219:118770)
- Layer 10: ` Walker`, `Walker`, `ait`, `挪`, `锁定` (target ranks: base_value=59:15025, first_product=118:32548, bound_value=117:27039, second_product=234:25790, answer=219:37485)
- Layer 20: ` .----`, `往常`, `ools`, ` procedural`, `平日里` (target ranks: base_value=59:126262, first_product=118:128816, bound_value=117:127992, second_product=234:114868, answer=219:128738)
- Layer 30: ` talags`, ` pakig`, ` gilay`, ` dekameters`, ` procedural` (target ranks: base_value=59:122441, first_product=118:125975, bound_value=117:124053, second_product=234:103071, answer=219:126524)
- Layer 35: ` hilabihan`, `滴水`, ` silic`, ` .`, ` pakig` (target ranks: base_value=59:125444, first_product=118:122128, bound_value=117:121407, second_product=234:112183, answer=219:128379)
- Layer 36: `停`, `幽`, ` tall`, `adows`, `往外` (target ranks: base_value=59:87214, first_product=118:88342, bound_value=117:90779, second_product=234:80397, answer=219:123590)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, `�乐`, `EDMF` (target ranks: base_value=59:126929, first_product=118:123470, bound_value=117:124389, second_product=234:115263, answer=219:128531)
- Layer 38: ` .`, `繁体`, ` hilabihan`, `}<?`, `用了` (target ranks: base_value=59:119469, first_product=118:119478, bound_value=117:116019, second_product=234:86122, answer=219:125486)
- Layer 39: ` .`, ` hilabihan`, ` talags`, ` .↵↵`, `}<?` (target ranks: base_value=59:108315, first_product=118:115024, bound_value=117:96144, second_product=234:38570, answer=219:114575)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, ` filler` (target ranks: base_value=59:57928, first_product=118:64540, bound_value=117:44950, second_product=234:14421, answer=219:55599)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `忏`, ` ,` (target ranks: base_value=59:17335, first_product=118:20247, bound_value=117:6716, second_product=234:1663, answer=219:7722)

### Filler position 3 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:125044, first_product=118:117413, bound_value=117:117907, second_product=234:114740, answer=219:121030)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: base_value=59:13868, first_product=118:27286, bound_value=117:26187, second_product=234:25990, answer=219:27708)
- Layer 20: `ait`, `忑`, `ashi`, `能被`, `锁定` (target ranks: base_value=59:10074, first_product=118:48476, bound_value=117:38318, second_product=234:22649, answer=219:42879)
- Layer 30: `Y`, ` Y`, `看看吧`, ` y`, `y` (target ranks: base_value=59:28579, first_product=118:99616, bound_value=117:94410, second_product=234:73669, answer=219:114250)
- Layer 35: ` y`, ` Y`, `Y`, `y`, `看看吧` (target ranks: base_value=59:4345, first_product=118:78829, bound_value=117:54876, second_product=234:39069, answer=219:75540)
- Layer 36: ` y`, `y`, ` Y`, `Y`, `看看吧` (target ranks: base_value=59:12640, first_product=118:81844, bound_value=117:57486, second_product=234:43205, answer=219:86032)
- Layer 37: `y`, ` y`, `yv`, `.y`, `}<?` (target ranks: base_value=59:45061, first_product=118:106933, bound_value=117:87505, second_product=234:68567, answer=219:107909)
- Layer 38: `}<?`, `oses`, `asi`, `yv`, `y` (target ranks: base_value=59:51971, first_product=118:113224, bound_value=117:99608, second_product=234:78431, answer=219:114697)
- Layer 39: `.y`, `yv`, ` y`, ` Yuk`, ` 𝑦` (target ranks: base_value=59:75637, first_product=118:123355, bound_value=117:104031, second_product=234:93916, answer=219:99813)
- Layer 40: ` y`, ` x`, ` talags`, `y`, ` Y` (target ranks: base_value=59:38907, first_product=118:107703, bound_value=117:70056, second_product=234:63504, answer=219:42334)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` ,`, ` .↵↵`, ` unless` (target ranks: base_value=59:10058, first_product=118:75824, bound_value=117:38110, second_product=234:29113, answer=219:13308)

### Filler position 4 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=59:125305, first_product=118:118441, bound_value=117:119063, second_product=234:115963, answer=219:122349)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=59:10697, first_product=118:22923, bound_value=117:21383, second_product=234:22921, answer=219:22864)
- Layer 20: `ait`, `cape`, `挪`, `atile`, `atable` (target ranks: base_value=59:8349, first_product=118:45866, bound_value=117:35631, second_product=234:35723, answer=219:34714)
- Layer 30: ` Niagara`, `tap`, `ERG`, `Tap`, ` tap` (target ranks: base_value=59:94780, first_product=118:124478, bound_value=117:105163, second_product=234:77310, answer=219:76859)
- Layer 35: ` tap`, ` Niagara`, `Tap`, `tap`, ` dynam` (target ranks: base_value=59:64553, first_product=118:123747, bound_value=117:93784, second_product=234:59739, answer=219:53999)
- Layer 36: ` dynam`, `动态`, ` tap`, ` Niagara`, `期望` (target ranks: base_value=59:57689, first_product=118:117015, bound_value=117:83062, second_product=234:37785, answer=219:47861)
- Layer 37: ` talags`, `oug`, ` Nim`, ` RNS`, ` dynam` (target ranks: base_value=59:96933, first_product=118:122462, bound_value=117:106695, second_product=234:74243, answer=219:80926)
- Layer 38: ` talags`, `本题分析`, `lez`, `zyw`, ` Zed` (target ranks: base_value=59:111267, first_product=118:125303, bound_value=117:119431, second_product=234:82474, answer=219:98900)
- Layer 39: ` talags`, ` Nij`, `oug`, `本题分析`, ` Zed` (target ranks: base_value=59:106447, first_product=118:126449, bound_value=117:111505, second_product=234:67387, answer=219:58984)
- Layer 40: ` talags`, `oug`, ` Nij`, ` Nim`, `zij` (target ranks: base_value=59:110199, first_product=118:120683, bound_value=117:89821, second_product=234:77683, answer=219:23585)
- Layer 41: ` .`, `Question`, ` Question`, ` careful`, ` ,` (target ranks: base_value=59:50565, first_product=118:84740, bound_value=117:29716, second_product=234:36262, answer=219:1075)

### Filler position 5 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=59:124996, first_product=118:118410, bound_value=117:119230, second_product=234:116290, answer=219:122504)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: base_value=59:12237, first_product=118:25600, bound_value=117:23947, second_product=234:26360, answer=219:27778)
- Layer 20: `锁定`, `幽`, `鞍`, `挪`, ` emot` (target ranks: base_value=59:9816, first_product=118:31555, bound_value=117:29093, second_product=234:28423, answer=219:24372)
- Layer 30: ` tap`, `Tap`, `鞍`, ` Tap`, `�` (target ranks: base_value=59:37450, first_product=118:94041, bound_value=117:63567, second_product=234:52381, answer=219:39226)
- Layer 35: ` tap`, `Tap`, ` Tap`, `�`, `鞍` (target ranks: base_value=59:24654, first_product=118:88947, bound_value=117:51194, second_product=234:45345, answer=219:25829)
- Layer 36: ` tap`, ` rip`, ` zad`, `鞍`, `acin` (target ranks: base_value=59:48586, first_product=118:96473, bound_value=117:66966, second_product=234:42841, answer=219:34360)
- Layer 37: `acos`, ` Zad`, `oug`, ` talags`, `覆` (target ranks: base_value=59:93586, first_product=118:111256, bound_value=117:91474, second_product=234:87174, answer=219:72178)
- Layer 38: `}<?`, `zat`, ` talags`, `zyw`, `hemer` (target ranks: base_value=59:114607, first_product=118:118417, bound_value=117:104686, second_product=234:91790, answer=219:94382)
- Layer 39: `}<?`, `hemer`, ` talags`, ` Nij`, `东海` (target ranks: base_value=59:111240, first_product=118:124624, bound_value=117:101815, second_product=234:94900, answer=219:78528)
- Layer 40: ` talags`, ` rip`, `反复`, `冰冰`, ` repetition` (target ranks: base_value=59:109477, first_product=118:113614, bound_value=117:78131, second_product=234:85850, answer=219:41844)
- Layer 41: ` .`, `冰冰`, ` careful`, `鹉`, `实在` (target ranks: base_value=59:71130, first_product=118:81868, bound_value=117:36562, second_product=234:57160, answer=219:8270)

### Filler position 6 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=59:124568, first_product=118:117615, bound_value=117:118664, second_product=234:115665, answer=219:121828)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=59:11679, first_product=118:24290, bound_value=117:23566, second_product=234:24568, answer=219:25262)
- Layer 20: ` unflagged`, `修罗`, `这一步`, `试一试`, `盒子` (target ranks: base_value=59:82519, first_product=118:90520, bound_value=117:91639, second_product=234:85236, answer=219:96747)
- Layer 30: ` step`, `高明`, `一步步`, `推算`, `一步一步` (target ranks: base_value=59:24208, first_product=118:76818, bound_value=117:100457, second_product=234:105688, answer=219:54353)
- Layer 35: ` Tw`, ` step`, `acks`, ` resolve`, `Tw` (target ranks: base_value=59:4829, first_product=118:59827, bound_value=117:76966, second_product=234:49570, answer=219:43000)
- Layer 36: ` Tw`, ` tw`, ` step`, `Tw`, ` resolve` (target ranks: base_value=59:11052, first_product=118:52154, bound_value=117:78407, second_product=234:46121, answer=219:44635)
- Layer 37: ` Tw`, ` step`, ` Step`, `高明`, `tw` (target ranks: base_value=59:32395, first_product=118:90935, bound_value=117:108195, second_product=234:62924, answer=219:83561)
- Layer 38: ` Tw`, `tw`, ` step`, `一步步`, ` tw` (target ranks: base_value=59:43179, first_product=118:106754, bound_value=117:117805, second_product=234:67377, answer=219:111189)
- Layer 39: ` Fif`, ` nasod`, `MMMMMMMM`, `ophe`, `替换` (target ranks: base_value=59:89058, first_product=118:126878, bound_value=117:125393, second_product=234:112492, answer=219:121573)
- Layer 40: ` y`, `y`, ` nasod`, ` gihulagway`, ` talags` (target ranks: base_value=59:64349, first_product=118:120587, bound_value=117:117201, second_product=234:89579, answer=219:100795)
- Layer 41: `试一试`, ` .`, `ucay`, `那颗`, `一个一个` (target ranks: base_value=59:89608, first_product=118:123652, bound_value=117:122437, second_product=234:107480, answer=219:103498)

### Filler position 7 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124580, first_product=118:117482, bound_value=117:118565, second_product=234:115456, answer=219:121523)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:10633, first_product=118:23336, bound_value=117:22587, second_product=234:23615, answer=219:23923)
- Layer 20: `鞍`, `幽`, `锁定`, `ait`, `足` (target ranks: base_value=59:13660, first_product=118:52313, bound_value=117:36591, second_product=234:37957, answer=219:45246)
- Layer 30: `鞍`, `回答`, `输出的`, ` repetition`, `Respons` (target ranks: base_value=59:11549, first_product=118:68147, bound_value=117:32395, second_product=234:65610, answer=219:39196)
- Layer 35: `鞍`, `acks`, ` repetition`, `输出的`, `重复` (target ranks: base_value=59:2532, first_product=118:38880, bound_value=117:15520, second_product=234:35751, answer=219:24096)
- Layer 36: `输出的`, `acks`, `输出`, `鞍`, `包袱` (target ranks: base_value=59:6816, first_product=118:44717, bound_value=117:23447, second_product=234:43944, answer=219:33862)
- Layer 37: `输出的`, `输出`, ` Ll`, ` LL`, `Ll` (target ranks: base_value=59:21846, first_product=118:75075, bound_value=117:33033, second_product=234:73165, answer=219:55774)
- Layer 38: ` Ll`, `冰冰`, ` LL`, ` prompt`, `响应` (target ranks: base_value=59:26017, first_product=118:89618, bound_value=117:46699, second_product=234:59364, answer=219:70289)
- Layer 39: `aharan`, ` LL`, `hemer`, `acons`, `树叶` (target ranks: base_value=59:85415, first_product=118:125167, bound_value=117:105870, second_product=234:111749, answer=219:107955)
- Layer 40: ` talags`, `šk`, ` Ll`, ` LL`, `下沉` (target ranks: base_value=59:51899, first_product=118:111789, bound_value=117:73260, second_product=234:105977, answer=219:72730)
- Layer 41: ` .`, `我曾经`, `šk`, `干干净净`, `我没有` (target ranks: base_value=59:29020, first_product=118:92168, bound_value=117:55664, second_product=234:68343, answer=219:36530)

### Filler position 8 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124584, first_product=118:117485, bound_value=117:118603, second_product=234:115585, answer=219:121539)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: base_value=59:9559, first_product=118:22173, bound_value=117:21360, second_product=234:23175, answer=219:23286)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, `Walker` (target ranks: base_value=59:13981, first_product=118:55549, bound_value=117:37813, second_product=234:38653, answer=219:45265)
- Layer 30: ` y`, ` variable`, ` yak`, ` dy`, ` Y` (target ranks: base_value=59:8343, first_product=118:114302, bound_value=117:88282, second_product=234:107149, answer=219:95733)
- Layer 35: ` variable`, ` var`, `variable`, `变量`, ` Variable` (target ranks: base_value=59:967, first_product=118:74041, bound_value=117:41101, second_product=234:58109, answer=219:57181)
- Layer 36: ` variable`, `variable`, ` var`, ` variables`, `变量的` (target ranks: base_value=59:5394, first_product=118:77466, bound_value=117:48581, second_product=234:68568, answer=219:63924)
- Layer 37: `变量的`, ` variable`, `variable`, `variables`, ` variables` (target ranks: base_value=59:29244, first_product=118:104908, bound_value=117:82143, second_product=234:91808, answer=219:97973)
- Layer 38: ` initial`, `变量的`, `variables`, ` variables`, `Variables` (target ranks: base_value=59:36829, first_product=118:110397, bound_value=117:97342, second_product=234:65943, answer=219:111264)
- Layer 39: `}<?`, ` 𝑦`, `acons`, `yv`, `embl` (target ranks: base_value=59:91963, first_product=118:123230, bound_value=117:112064, second_product=234:109665, answer=219:119444)
- Layer 40: `šk`, ` y`, `y`, `殿堂`, `外壳` (target ranks: base_value=59:53819, first_product=118:112018, bound_value=117:87816, second_product=234:110030, answer=219:74038)
- Layer 41: ` .`, `转载请`, `šk`, `试一试`, `鹉` (target ranks: base_value=59:33814, first_product=118:99801, bound_value=117:77599, second_product=234:83620, answer=219:26380)

### Filler position 9 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124552, first_product=118:117492, bound_value=117:118682, second_product=234:115579, answer=219:121609)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9546, first_product=118:22521, bound_value=117:21827, second_product=234:23144, answer=219:23837)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `挪` (target ranks: base_value=59:10128, first_product=118:38641, bound_value=117:26559, second_product=234:24966, answer=219:35433)
- Layer 30: `Y`, ` y`, ` Yok`, ` Y`, `_Y` (target ranks: base_value=59:5758, first_product=118:104614, bound_value=117:78039, second_product=234:84320, answer=219:86425)
- Layer 35: ` y`, `Y`, ` Y`, ` yak`, `YG` (target ranks: base_value=59:779, first_product=118:61762, bound_value=117:21542, second_product=234:46235, answer=219:46876)
- Layer 36: ` y`, `Y`, `y`, ` Y`, ` yak` (target ranks: base_value=59:4977, first_product=118:59802, bound_value=117:18397, second_product=234:44689, answer=219:54666)
- Layer 37: ` y`, `y`, ` Y`, `.y`, `	y` (target ranks: base_value=59:6871, first_product=118:83164, bound_value=117:23327, second_product=234:44330, answer=219:51211)
- Layer 38: `y`, ` y`, ` Yuk`, `}<?`, `yu` (target ranks: base_value=59:12528, first_product=118:96734, bound_value=117:48684, second_product=234:52552, answer=219:82255)
- Layer 39: ` Yuk`, `.y`, `	y`, ` 𝑦`, ` y` (target ranks: base_value=59:64781, first_product=118:123378, bound_value=117:86331, second_product=234:84219, answer=219:101905)
- Layer 40: ` y`, `y`, ` Y`, `duc`, `.y` (target ranks: base_value=59:30564, first_product=118:102231, bound_value=117:39062, second_product=234:53678, answer=219:42106)
- Layer 41: `鹉`, ` .`, `试一试`, `acular`, `出不穷` (target ranks: base_value=59:9488, first_product=118:72229, bound_value=117:20698, second_product=234:43869, answer=219:13876)

### Filler position 10 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124583, first_product=118:117736, bound_value=117:118975, second_product=234:116083, answer=219:121817)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9710, first_product=118:23061, bound_value=117:22352, second_product=234:23974, answer=219:24817)
- Layer 20: `ait`, `锁定`, `幽`, `挪`, ` Walker` (target ranks: base_value=59:2304, first_product=118:20219, bound_value=117:13298, second_product=234:15399, answer=219:18846)
- Layer 30: `67`, `59`, `103`, `93`, `69` (target ranks: base_value=59:2, first_product=118:2197, bound_value=117:112, second_product=234:3535, answer=219:365)
- Layer 35: `235`, `234`, `233`, `223`, `229` (target ranks: base_value=59:74, first_product=118:33489, bound_value=117:2678, second_product=234:2, answer=219:10)
- Layer 36: `219`, `221`, `217`, `215`, ` Marcos` (target ranks: base_value=59:16750, first_product=118:21040, bound_value=117:2380, second_product=234:3891, answer=219:1)
- Layer 37: `219`, `217`, `221`, ` Marcos`, `215` (target ranks: base_value=59:43092, first_product=118:16427, bound_value=117:1931, second_product=234:4072, answer=219:1)
- Layer 38: `219`, `217`, `221`, `215`, `213` (target ranks: base_value=59:67724, first_product=118:29014, bound_value=117:2437, second_product=234:30608, answer=219:1)
- Layer 39: `219`, `217`, `221`, `218`, `215` (target ranks: base_value=59:84154, first_product=118:117838, bound_value=117:51770, second_product=234:29080, answer=219:1)
- Layer 40: ` talags`, `219`, `217`, `221`, ` mosunod` (target ranks: base_value=59:111975, first_product=118:116340, bound_value=117:41778, second_product=234:30289, answer=219:2)
- Layer 41: `219`, ` nuest`, `217`, `笔趣`, ` talags` (target ranks: base_value=59:86796, first_product=118:96335, bound_value=117:38717, second_product=234:54171, answer=219:1)

### Filler position 11 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124753, first_product=118:118188, bound_value=117:119396, second_product=234:116523, answer=219:122404)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:8771, first_product=118:22383, bound_value=117:21455, second_product=234:23564, answer=219:24411)
- Layer 20: `锁定`, `ait`, ` smile`, ` Walker`, `挪` (target ranks: base_value=59:8231, first_product=118:37227, bound_value=117:27244, second_product=234:33685, answer=219:25393)
- Layer 30: ` tap`, `Tap`, ` Tap`, `tap`, `�` (target ranks: base_value=59:611, first_product=118:52773, bound_value=117:29561, second_product=234:68079, answer=219:28562)
- Layer 35: `Tap`, ` tap`, ` Tap`, ` smile`, `锁定` (target ranks: base_value=59:600, first_product=118:33132, bound_value=117:16628, second_product=234:49601, answer=219:26079)
- Layer 36: ` tap`, ` Tap`, `Tap`, ` smile`, `calcul` (target ranks: base_value=59:1482, first_product=118:26390, bound_value=117:14921, second_product=234:57626, answer=219:26822)
- Layer 37: `}<?`, `不急`, ` calc`, `calcul`, `冰冰` (target ranks: base_value=59:14306, first_product=118:47046, bound_value=117:20989, second_product=234:89827, answer=219:65414)
- Layer 38: `}<?`, ` Calc`, ` calc`, `不急`, `冰冰` (target ranks: base_value=59:19919, first_product=118:51205, bound_value=117:26096, second_product=234:81438, answer=219:74318)
- Layer 39: `东海`, `}<?`, `ocyst`, `芦`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=59:56055, first_product=118:90387, bound_value=117:42437, second_product=234:75089, answer=219:60356)
- Layer 40: ` nasod`, ` .`, `冰冰`, ` talags`, `坏` (target ranks: base_value=59:16881, first_product=118:47738, bound_value=117:11934, second_product=234:45490, answer=219:3935)
- Layer 41: ` .`, ` .↵↵`, ` `, `<｜end▁of▁sentence｜>`, `鹉` (target ranks: base_value=59:5672, first_product=118:27741, bound_value=117:5546, second_product=234:23444, answer=219:499)

### Filler position 12 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124594, first_product=118:117979, bound_value=117:119128, second_product=234:116583, answer=219:122180)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8933, first_product=118:22651, bound_value=117:21868, second_product=234:24562, answer=219:24167)
- Layer 20: `ait`, `锁定`, ` smile`, `atable`, `忑` (target ranks: base_value=59:9555, first_product=118:41813, bound_value=117:30742, second_product=234:34654, answer=219:31957)
- Layer 30: `Tap`, ` tap`, ` Tap`, `鞍`, `锁定` (target ranks: base_value=59:3894, first_product=118:70015, bound_value=117:38967, second_product=234:56067, answer=219:30389)
- Layer 35: ` tap`, `Tap`, `锁定`, ` Tap`, `acin` (target ranks: base_value=59:1631, first_product=118:40507, bound_value=117:16806, second_product=234:33751, answer=219:22901)
- Layer 36: ` tap`, `acin`, ` Tap`, `Tap`, ` repeated` (target ranks: base_value=59:2204, first_product=118:26661, bound_value=117:13180, second_product=234:31383, answer=219:21312)
- Layer 37: `acin`, `冰冰`, ` tap`, `acons`, `itore` (target ranks: base_value=59:8088, first_product=118:42963, bound_value=117:15931, second_product=234:50472, answer=219:44112)
- Layer 38: `acons`, ` Reson`, `acin`, `院内`, ` RES` (target ranks: base_value=59:16859, first_product=118:44506, bound_value=117:17966, second_product=234:42107, answer=219:46512)
- Layer 39: `acons`, ` talags`, `ocyst`, `东海`, `osit` (target ranks: base_value=59:46227, first_product=118:105000, bound_value=117:57154, second_product=234:71695, answer=219:55414)
- Layer 40: ` talags`, ` nasod`, ` seventy`, ` Seventy`, ` seventeen` (target ranks: base_value=59:15003, first_product=118:78890, bound_value=117:30516, second_product=234:59722, answer=219:4850)
- Layer 41: ` .`, `有下列`, `thirty`, ` repeated`, ` thirty` (target ranks: base_value=59:3996, first_product=118:46487, bound_value=117:15294, second_product=234:36453, answer=219:858)

### Filler position 13 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124684, first_product=118:118018, bound_value=117:119162, second_product=234:116670, answer=219:122157)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9217, first_product=118:22773, bound_value=117:22139, second_product=234:24421, answer=219:24471)
- Layer 20: `锁定`, `ait`, `忑`, ` Walker`, `挪` (target ranks: base_value=59:12145, first_product=118:37905, bound_value=117:28744, second_product=234:24363, answer=219:34341)
- Layer 30: ` resolve`, ` Resolution`, ` resolution`, ` resolves`, ` resolved` (target ranks: base_value=59:14027, first_product=118:80184, bound_value=117:54432, second_product=234:44415, answer=219:60035)
- Layer 35: ` resolve`, ` Resolution`, ` resolution`, `resolve`, ` resolving` (target ranks: base_value=59:5097, first_product=118:53796, bound_value=117:30098, second_product=234:24878, answer=219:36743)
- Layer 36: ` Resolution`, ` resolve`, ` resolution`, ` definitions`, ` resolves` (target ranks: base_value=59:5921, first_product=118:30852, bound_value=117:15375, second_product=234:18341, answer=219:25879)
- Layer 37: ` definitions`, `Definitions`, ` Definitions`, `calcul`, `定义` (target ranks: base_value=59:13920, first_product=118:52510, bound_value=117:23708, second_product=234:28764, answer=219:42213)
- Layer 38: ` Res`, ` Resolution`, ` resolutions`, ` resolve`, ` definitions` (target ranks: base_value=59:20882, first_product=118:68621, bound_value=117:34279, second_product=234:20714, answer=219:65163)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` rese`, ` Res`, `hemer`, `下沉` (target ranks: base_value=59:59888, first_product=118:107819, bound_value=117:83280, second_product=234:51934, answer=219:92432)
- Layer 40: `冰冰`, `下沉`, `inking`, ` fifty`, ` Tw` (target ranks: base_value=59:31616, first_product=118:81871, bound_value=117:61216, second_product=234:48391, answer=219:55742)
- Layer 41: ` .`, ` `, `冰冰`, `xxxxxxxx`, `ffff` (target ranks: base_value=59:21292, first_product=118:54072, bound_value=117:44802, second_product=234:34825, answer=219:10508)

### Filler position 14 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124769, first_product=118:118319, bound_value=117:119411, second_product=234:116769, answer=219:122514)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8532, first_product=118:21944, bound_value=117:21046, second_product=234:23214, answer=219:23160)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, ` smile` (target ranks: base_value=59:4206, first_product=118:21855, bound_value=117:15285, second_product=234:16034, answer=219:20142)
- Layer 30: `67`, `79`, `55`, ` dripping`, ` seventy` (target ranks: base_value=59:6, first_product=118:4191, bound_value=117:249, second_product=234:8939, answer=219:370)
- Layer 35: `退出`, `acin`, ` Heim`, ` Behaviour`, `235` (target ranks: base_value=59:66, first_product=118:24898, bound_value=117:3365, second_product=234:328, answer=219:18)
- Layer 36: ` talags`, ` Parehong`, `推理`, `219`, ` behaviours` (target ranks: base_value=59:2888, first_product=118:29595, bound_value=117:3358, second_product=234:6161, answer=219:4)
- Layer 37: ` Parehong`, ` talags`, ` embar`, `内膜`, ` Marcos` (target ranks: base_value=59:32834, first_product=118:33311, bound_value=117:4274, second_product=234:9333, answer=219:14)
- Layer 38: ` talags`, `本题分析`, `}<?`, ` anomaly`, ` hydrodynamic` (target ranks: base_value=59:60001, first_product=118:82508, bound_value=117:11751, second_product=234:49855, answer=219:10)
- Layer 39: `219`, `211`, `213`, `221`, `本题分析` (target ranks: base_value=59:110674, first_product=118:116369, bound_value=117:55878, second_product=234:23134, answer=219:1)
- Layer 40: `219`, ` talags`, `213`, `217`, `211` (target ranks: base_value=59:103755, first_product=118:95075, bound_value=117:37036, second_product=234:6293, answer=219:1)
- Layer 41: `219`, ` .`, `217`, `笔趣`, `221` (target ranks: base_value=59:69500, first_product=118:83482, bound_value=117:45908, second_product=234:21394, answer=219:1)

### Filler position 15 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:124777, first_product=118:118495, bound_value=117:119715, second_product=234:117024, answer=219:122698)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8584, first_product=118:21874, bound_value=117:20940, second_product=234:22911, answer=219:22777)
- Layer 20: `ait`, `锁定`, ` Walker`, `距`, `能被` (target ranks: base_value=59:5265, first_product=118:19165, bound_value=117:16017, second_product=234:23833, answer=219:24025)
- Layer 30: `117`, `116`, `114`, `119`, `sett` (target ranks: base_value=59:50, first_product=118:12, bound_value=117:1, second_product=234:516, answer=219:1219)
- Layer 35: `234`, `235`, `233`, `237`, `232` (target ranks: base_value=59:52491, first_product=118:36030, bound_value=117:16, second_product=234:1, answer=219:142)
- Layer 36: `234`, `235`, `233`, `栓`, `寨` (target ranks: base_value=59:126040, first_product=118:31817, bound_value=117:129, second_product=234:1, answer=219:283)
- Layer 37: `234`, `235`, `233`, ` AFC`, ` sabwag` (target ranks: base_value=59:127592, first_product=118:46797, bound_value=117:591, second_product=234:1, answer=219:610)
- Layer 38: `234`, `235`, `233`, `223`, `金丹` (target ranks: base_value=59:126789, first_product=118:98691, bound_value=117:894, second_product=234:1, answer=219:45)
- Layer 39: `233`, `234`, ` MSE`, `oan`, `235` (target ranks: base_value=59:121419, first_product=118:108927, bound_value=117:1436, second_product=234:2, answer=219:12)
- Layer 40: `217`, `219`, `233`, ` fountain`, ` assumption` (target ranks: base_value=59:118169, first_product=118:113623, bound_value=117:2343, second_product=234:8, answer=219:2)
- Layer 41: `217`, `219`, ` assumption`, `}}}`, `到哪里` (target ranks: base_value=59:115186, first_product=118:109306, bound_value=117:7507, second_product=234:59, answer=219:2)

### Filler position 16 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:125116, first_product=118:119415, bound_value=117:120474, second_product=234:117791, answer=219:123464)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9652, first_product=118:23012, bound_value=117:22041, second_product=234:23923, answer=219:24127)
- Layer 20: `ait`, `能被`, `锁定`, `拆`, `幽` (target ranks: base_value=59:6421, first_product=118:38625, bound_value=117:23767, second_product=234:28456, answer=219:29591)
- Layer 30: `期望`, `胃癌`, ` repetitions`, ` expecting`, `117` (target ranks: base_value=59:71, first_product=118:199, bound_value=117:5, second_product=234:1095, answer=219:2373)
- Layer 35: `234`, `235`, `117`, `233`, ` cataract` (target ranks: base_value=59:3373, first_product=118:27008, bound_value=117:3, second_product=234:1, answer=219:3133)
- Layer 36: `234`, `117`, `235`, `}<?`, `沛` (target ranks: base_value=59:49930, first_product=118:28057, bound_value=117:2, second_product=234:1, answer=219:19712)
- Layer 37: `234`, `}<?`, ` sabwag`, `acons`, ` ASE` (target ranks: base_value=59:103378, first_product=118:41322, bound_value=117:10, second_product=234:1, answer=219:38035)
- Layer 38: `234`, `}<?`, `acons`, ` Gon`, `235` (target ranks: base_value=59:99279, first_product=118:55248, bound_value=117:17, second_product=234:1, answer=219:34448)
- Layer 39: `234`, `}<?`, `东海`, ` Gon`, ` ASE` (target ranks: base_value=59:60501, first_product=118:61875, bound_value=117:14, second_product=234:1, answer=219:5927)
- Layer 40: `234`, `219`, `117`, `apon`, `ses` (target ranks: base_value=59:17232, first_product=118:50976, bound_value=117:3, second_product=234:1, answer=219:2)
- Layer 41: `234`, ` .`, ` waiting`, `那两个`, ` two` (target ranks: base_value=59:12942, first_product=118:58824, bound_value=117:203, second_product=234:1, answer=219:8)

### Filler position 17 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:125203, first_product=118:119667, bound_value=117:120697, second_product=234:118021, answer=219:123621)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:10252, first_product=118:24465, bound_value=117:23481, second_product=234:25273, answer=219:26069)
- Layer 20: ` smile`, `而此时`, `距`, `能被`, `锁定` (target ranks: base_value=59:10118, first_product=118:32496, bound_value=117:21699, second_product=234:28002, answer=219:29136)
- Layer 30: ` twice`, ` Tw`, `Tw`, `tw`, `.tw` (target ranks: base_value=59:759, first_product=118:30977, bound_value=117:30809, second_product=234:56674, answer=219:36198)
- Layer 35: ` Tw`, `Tw`, `tw`, ` twice`, `.tw` (target ranks: base_value=59:278, first_product=118:23631, bound_value=117:19473, second_product=234:42371, answer=219:33071)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, ` doubling` (target ranks: base_value=59:1441, first_product=118:16557, bound_value=117:15817, second_product=234:41210, answer=219:32291)
- Layer 37: ` doubling`, `}<?`, ` Tw`, ` doubled`, ` doubles` (target ranks: base_value=59:3623, first_product=118:23989, bound_value=117:22816, second_product=234:67067, answer=219:48991)
- Layer 38: ` doubling`, `}<?`, ` Nij`, ` doubled`, ` Tw` (target ranks: base_value=59:6156, first_product=118:25563, bound_value=117:23413, second_product=234:61588, answer=219:57110)
- Layer 39: `}<?`, ` Nij`, `férés`, ` Douglass`, `覆` (target ranks: base_value=59:19117, first_product=118:41142, bound_value=117:21352, second_product=234:32279, answer=219:26808)
- Layer 40: `坏`, `}<?`, ` F`, `f`, ` f` (target ranks: base_value=59:4791, first_product=118:10653, bound_value=117:1784, second_product=234:5800, answer=219:1521)
- Layer 41: ` .`, ` `, `acular`, ` first`, `每次` (target ranks: base_value=59:1127, first_product=118:6967, bound_value=117:915, second_product=234:1985, answer=219:125)

### Filler position 18 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:125184, first_product=118:119635, bound_value=117:120788, second_product=234:118345, answer=219:123698)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9344, first_product=118:23980, bound_value=117:23119, second_product=234:24832, answer=219:25028)
- Layer 20: `ait`, ` engaging`, `会成为`, ` Walker`, `忑` (target ranks: base_value=59:16258, first_product=118:46612, bound_value=117:41198, second_product=234:44567, answer=219:51203)
- Layer 30: ` Tw`, ` formulas`, `鞍`, `atan`, `算出` (target ranks: base_value=59:16118, first_product=118:68694, bound_value=117:66161, second_product=234:62183, answer=219:82629)
- Layer 35: ` var`, ` Tw`, `atan`, `Tw`, ` formulas` (target ranks: base_value=59:3421, first_product=118:39736, bound_value=117:26949, second_product=234:33931, answer=219:49642)
- Layer 36: ` definitions`, ` formulas`, ` Tw`, `定义的`, `atan` (target ranks: base_value=59:4219, first_product=118:27333, bound_value=117:18315, second_product=234:25543, answer=219:42066)
- Layer 37: ` definitions`, `定义`, `Definitions`, `定义的`, `定义了` (target ranks: base_value=59:12671, first_product=118:44902, bound_value=117:33345, second_product=234:49125, answer=219:68503)
- Layer 38: `}<?`, ` Mir`, `ота`, `defining`, `计算公式` (target ranks: base_value=59:15660, first_product=118:52521, bound_value=117:42673, second_product=234:36598, answer=219:82066)
- Layer 39: `}<?`, `殿堂`, `script`, `迷惑`, `zat` (target ranks: base_value=59:40387, first_product=118:76556, bound_value=117:58575, second_product=234:57669, answer=219:89676)
- Layer 40: `šk`, `殿堂`, ` Tw`, `zij`, ` forty` (target ranks: base_value=59:15660, first_product=118:28338, bound_value=117:22003, second_product=234:38548, answer=219:29606)
- Layer 41: ` .`, ` mim`, `那颗`, `那一`, `每次` (target ranks: base_value=59:5410, first_product=118:24922, bound_value=117:19288, second_product=234:18912, answer=219:8371)

### Filler position 19 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=59:125344, first_product=118:119674, bound_value=117:120817, second_product=234:118378, answer=219:123707)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9000, first_product=118:22979, bound_value=117:22266, second_product=234:24659, answer=219:23741)
- Layer 20: `ait`, `忑`, ` engaging`, `能被`, ` Walker` (target ranks: base_value=59:5662, first_product=118:34651, bound_value=117:24729, second_product=234:39527, answer=219:34639)
- Layer 30: `59`, `58`, ` dy`, `yak`, `Y` (target ranks: base_value=59:1, first_product=118:27836, bound_value=117:20746, second_product=234:57217, answer=219:22776)
- Layer 35: `59`, `YG`, `Y`, ` y`, ` Y` (target ranks: base_value=59:1, first_product=118:14596, bound_value=117:5645, second_product=234:35192, answer=219:9378)
- Layer 36: `59`, `y`, ` start`, ` y`, ` Y` (target ranks: base_value=59:1, first_product=118:17348, bound_value=117:6346, second_product=234:41439, answer=219:17726)
- Layer 37: `y`, ` 𝑦`, `}<?`, `59`, ` y` (target ranks: base_value=59:4, first_product=118:41956, bound_value=117:25305, second_product=234:72358, answer=219:29488)
- Layer 38: `}<?`, `y`, `殿堂`, ` doubling`, `迷惑` (target ranks: base_value=59:18, first_product=118:68123, bound_value=117:52279, second_product=234:79057, answer=219:61527)
- Layer 39: ` 𝑦`, `.y`, ` y`, `}<?`, `	y` (target ranks: base_value=59:7405, first_product=118:84515, bound_value=117:48491, second_product=234:48472, answer=219:56721)
- Layer 40: ` y`, `y`, `yat`, `.y`, `殿堂` (target ranks: base_value=59:12100, first_product=118:25075, bound_value=117:3062, second_product=234:3612, answer=219:4198)
- Layer 41: ` .`, `acular`, `y`, `<｜end▁of▁sentence｜>`, `步骤如下` (target ranks: base_value=59:3203, first_product=118:7626, bound_value=117:733, second_product=234:366, answer=219:97)

### Filler position 20 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:125582, first_product=118:120016, bound_value=117:121194, second_product=234:118812, answer=219:123950)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8833, first_product=118:21711, bound_value=117:20932, second_product=234:23890, answer=219:23028)
- Layer 20: `ait`, `能被`, ` Walker`, `锁定`, `距` (target ranks: base_value=59:2212, first_product=118:25824, bound_value=117:15012, second_product=234:25567, answer=219:22444)
- Layer 30: ` dripping`, ` Pop`, ` pop`, ` seventy`, `Pop` (target ranks: base_value=59:11, first_product=118:14834, bound_value=117:915, second_product=234:7286, answer=219:2920)
- Layer 35: `234`, `235`, ` dy`, ` Dy`, `233` (target ranks: base_value=59:1056, first_product=118:82816, bound_value=117:8819, second_product=234:1, answer=219:70)
- Layer 36: `219`, `221`, `217`, `院长`, ` EMB` (target ranks: base_value=59:35462, first_product=118:8222, bound_value=117:1838, second_product=234:34, answer=219:1)
- Layer 37: `219`, `221`, `院长`, `217`, ` Markov` (target ranks: base_value=59:72602, first_product=118:8077, bound_value=117:2305, second_product=234:56, answer=219:1)
- Layer 38: `219`, `217`, ` ninete`, `十九章`, `十九` (target ranks: base_value=59:42341, first_product=118:11318, bound_value=117:3207, second_product=234:1850, answer=219:1)
- Layer 39: `219`, `221`, `319`, `419`, `217` (target ranks: base_value=59:104347, first_product=118:122244, bound_value=117:111588, second_product=234:11700, answer=219:1)
- Layer 40: `219`, `<｜begin▁of▁file｜>`, ` talags`, `221`, `217` (target ranks: base_value=59:119326, first_product=118:118929, bound_value=117:79803, second_product=234:8068, answer=219:1)
- Layer 41: `219`, ` Expressible`, `--------------------------------------------------------------------------------`, `}}}`, `................................................` (target ranks: base_value=59:89478, first_product=118:81442, bound_value=117:46678, second_product=234:7088, answer=219:1)

### Filler position 21 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:125714, first_product=118:120535, bound_value=117:121545, second_product=234:118910, answer=219:124261)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:8448, first_product=118:21264, bound_value=117:20265, second_product=234:23279, answer=219:22781)
- Layer 20: `ait`, `锁定`, `距`, `能被`, ` Walker` (target ranks: base_value=59:5054, first_product=118:26359, bound_value=117:17352, second_product=234:25844, answer=219:24697)
- Layer 30: `acos`, ` drip`, `acin`, `akai`, `alal` (target ranks: base_value=59:36, first_product=118:1876, bound_value=117:395, second_product=234:6125, answer=219:2932)
- Layer 35: `235`, `234`, ` dy`, ` Dy`, `233` (target ranks: base_value=59:627, first_product=118:28332, bound_value=117:1751, second_product=234:2, answer=219:113)
- Layer 36: `219`, ` Labour`, `院长`, `内膜`, ` embedded` (target ranks: base_value=59:37189, first_product=118:7293, bound_value=117:2666, second_product=234:428, answer=219:1)
- Layer 37: `219`, `院长`, `内膜`, ` embar`, `院長` (target ranks: base_value=59:83013, first_product=118:8939, bound_value=117:3002, second_product=234:459, answer=219:1)
- Layer 38: `219`, `十九`, `119`, ` Nin`, `第十九` (target ranks: base_value=59:52073, first_product=118:2240, bound_value=117:733, second_product=234:9321, answer=219:1)
- Layer 39: `219`, `221`, `220`, `719`, `419` (target ranks: base_value=59:105693, first_product=118:109493, bound_value=117:99107, second_product=234:43389, answer=219:1)
- Layer 40: `219`, ` talags`, `实在`, `ophyll`, ` accumulating` (target ranks: base_value=59:93130, first_product=118:72345, bound_value=117:36858, second_product=234:27803, answer=219:1)
- Layer 41: `219`, ` .`, `笔趣`, ` sometimes`, `))))` (target ranks: base_value=59:40430, first_product=118:38324, bound_value=117:21689, second_product=234:12839, answer=219:1)

### Filler position 22 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:125810, first_product=118:120862, bound_value=117:121811, second_product=234:119261, answer=219:124473)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:8102, first_product=118:21283, bound_value=117:20142, second_product=234:22758, answer=219:22730)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `距` (target ranks: base_value=59:7586, first_product=118:31810, bound_value=117:23159, second_product=234:28769, answer=219:36999)
- Layer 30: ` Tw`, `atan`, `Tw`, `幽`, `鞍` (target ranks: base_value=59:7, first_product=118:10433, bound_value=117:10534, second_product=234:25583, answer=219:11811)
- Layer 35: `59`, ` repetition`, ` Tw`, ` repeated`, `分解` (target ranks: base_value=59:1, first_product=118:2638, bound_value=117:1845, second_product=234:10325, answer=219:6211)
- Layer 36: `分解`, ` repeated`, ` Tw`, `59`, `留存` (target ranks: base_value=59:4, first_product=118:2624, bound_value=117:1772, second_product=234:14985, answer=219:9850)
- Layer 37: ` doubling`, `}<?`, `59`, `分解`, ` doubles` (target ranks: base_value=59:3, first_product=118:2628, bound_value=117:1829, second_product=234:24990, answer=219:15722)
- Layer 38: `}<?`, ` doubling`, `zat`, ` doubles`, ` doubled` (target ranks: base_value=59:7, first_product=118:14224, bound_value=117:10941, second_product=234:42483, answer=219:47997)
- Layer 39: `}<?`, ` doubling`, ` doubled`, `arana`, `uerak` (target ranks: base_value=59:43, first_product=118:42902, bound_value=117:32607, second_product=234:45355, answer=219:30171)
- Layer 40: ` Tw`, `}<?`, `acl`, `俯`, `arella` (target ranks: base_value=59:152, first_product=118:32314, bound_value=117:18627, second_product=234:44922, answer=219:4869)
- Layer 41: ` `, ` .`, `2`, `俯`, ` twist` (target ranks: base_value=59:65, first_product=118:15166, bound_value=117:8706, second_product=234:23161, answer=219:231)

### Filler position 23 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126183, first_product=118:121869, bound_value=117:122703, second_product=234:119796, answer=219:125166)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=59:9092, first_product=118:23062, bound_value=117:21999, second_product=234:23705, answer=219:23859)
- Layer 20: ` smile`, `距`, ` LS`, `能被`, `足` (target ranks: base_value=59:5854, first_product=118:19123, bound_value=117:17077, second_product=234:19703, answer=219:19544)
- Layer 30: `atan`, `反复`, ` repetitions`, ` repetition`, `西洋` (target ranks: base_value=59:25, first_product=118:199, bound_value=117:39, second_product=234:1710, answer=219:4558)
- Layer 35: `235`, `234`, `117`, ` Behavior`, ` Widget` (target ranks: base_value=59:2299, first_product=118:1331, bound_value=117:3, second_product=234:2, answer=219:571)
- Layer 36: `235`, `234`, `117`, `留存`, `歌唱` (target ranks: base_value=59:61181, first_product=118:1596, bound_value=117:3, second_product=234:2, answer=219:2547)
- Layer 37: `}<?`, `235`, `234`, `117`, ` smoothed` (target ranks: base_value=59:111539, first_product=118:6387, bound_value=117:4, second_product=234:3, answer=219:17571)
- Layer 38: `117`, `235`, `}<?`, `234`, `233` (target ranks: base_value=59:105384, first_product=118:2761, bound_value=117:1, second_product=234:4, answer=219:5958)
- Layer 39: `}<?`, `干`, `233`, `117`, `东海` (target ranks: base_value=59:100677, first_product=118:22277, bound_value=117:4, second_product=234:34, answer=219:3551)
- Layer 40: ` rub`, `ynd`, `117`, `亲身`, `留存` (target ranks: base_value=59:59706, first_product=118:12912, bound_value=117:3, second_product=234:152, answer=219:13)
- Layer 41: ` .`, `上文`, ` waiting`, `219`, `那两个` (target ranks: base_value=59:30363, first_product=118:6620, bound_value=117:39, second_product=234:75, answer=219:4)

### Filler position 24 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126025, first_product=118:121341, bound_value=117:122281, second_product=234:119815, answer=219:124822)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=59:9344, first_product=118:23717, bound_value=117:23079, second_product=234:24214, answer=219:24238)
- Layer 20: `ait`, `锁定`, ` LS`, ` smile`, `挪` (target ranks: base_value=59:6223, first_product=118:26403, bound_value=117:20407, second_product=234:20113, answer=219:26036)
- Layer 30: ` irrelevant`, ` redundant`, `不需要`, ` unnecessary`, `没必要` (target ranks: base_value=59:10044, first_product=118:56911, bound_value=117:42611, second_product=234:50563, answer=219:77145)
- Layer 35: ` var`, ` redundant`, ` unused`, ` Tw`, `冗余` (target ranks: base_value=59:3430, first_product=118:46868, bound_value=117:36282, second_product=234:51901, answer=219:59128)
- Layer 36: ` definitions`, ` var`, `acin`, ` Tw`, ` defined` (target ranks: base_value=59:4952, first_product=118:31747, bound_value=117:22092, second_product=234:46317, answer=219:56756)
- Layer 37: `不急`, `定义了`, ` definitions`, `定义`, `defined` (target ranks: base_value=59:20768, first_product=118:53834, bound_value=117:43841, second_product=234:80761, answer=219:90535)
- Layer 38: `不急`, `arel`, `不加`, ` Mir`, ` unnecessary` (target ranks: base_value=59:28307, first_product=118:45919, bound_value=117:48608, second_product=234:58451, answer=219:78570)
- Layer 39: `迷惑`, `东海`, `šk`, `枝叶`, `acons` (target ranks: base_value=59:48767, first_product=118:64057, bound_value=117:54905, second_product=234:70970, answer=219:71383)
- Layer 40: `acl`, `殿堂`, `šk`, `装`, `不急` (target ranks: base_value=59:19787, first_product=118:25533, bound_value=117:24176, second_product=234:56595, answer=219:17229)
- Layer 41: ` .`, `从前`, ` waiting`, ` `, ` careful` (target ranks: base_value=59:8409, first_product=118:11735, bound_value=117:10423, second_product=234:23518, answer=219:593)

### Filler position 25 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126162, first_product=118:121784, bound_value=117:122588, second_product=234:119907, answer=219:124995)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9350, first_product=118:24374, bound_value=117:23733, second_product=234:24681, answer=219:24361)
- Layer 20: `锁定`, `ait`, ` Walker`, ` smile`, `Walker` (target ranks: base_value=59:6104, first_product=118:26820, bound_value=117:20874, second_product=234:21025, answer=219:23958)
- Layer 30: ` dy`, `atar`, `aty`, `acin`, `Tap` (target ranks: base_value=59:239, first_product=118:4220, bound_value=117:1274, second_product=234:8206, answer=219:6202)
- Layer 35: ` dy`, `Dy`, ` Dy`, ` Behavior`, `234` (target ranks: base_value=59:879, first_product=118:44523, bound_value=117:15384, second_product=234:5, answer=219:404)
- Layer 36: ` Antar`, `219`, ` Labour`, `出院`, ` discharge` (target ranks: base_value=59:22476, first_product=118:4681, bound_value=117:4406, second_product=234:1449, answer=219:2)
- Layer 37: `内膜`, ` embar`, `院长`, `219`, `<｜place▁holder▁no▁173｜>` (target ranks: base_value=59:69528, first_product=118:5579, bound_value=117:6371, second_product=234:3298, answer=219:4)
- Layer 38: `219`, `十九章`, `第十九`, ` ninete`, `泡沫` (target ranks: base_value=59:42939, first_product=118:3083, bound_value=117:5230, second_product=234:45006, answer=219:1)
- Layer 39: `219`, `220`, `221`, `218`, `419` (target ranks: base_value=59:99893, first_product=118:103363, bound_value=117:106306, second_product=234:49749, answer=219:1)
- Layer 40: `219`, `217`, ` talags`, `第二百`, `上场` (target ranks: base_value=59:100573, first_product=118:87932, bound_value=117:63009, second_product=234:40702, answer=219:1)
- Layer 41: `219`, `相比之下`, ` .`, `................................................`, `.,` (target ranks: base_value=59:54933, first_product=118:75036, bound_value=117:55552, second_product=234:23873, answer=219:1)

### Filler position 26 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126273, first_product=118:121925, bound_value=117:122733, second_product=234:120073, answer=219:125086)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8666, first_product=118:22820, bound_value=117:21834, second_product=234:23355, answer=219:22242)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `拆` (target ranks: base_value=59:8788, first_product=118:33944, bound_value=117:23616, second_product=234:27025, answer=219:36257)
- Layer 30: ` labor`, ` dy`, `yj`, `y`, `yak` (target ranks: base_value=59:3952, first_product=118:82809, bound_value=117:52078, second_product=234:61811, answer=219:80695)
- Layer 35: ` var`, ` labor`, `分解`, ` equations`, ` variable` (target ranks: base_value=59:3193, first_product=118:69361, bound_value=117:41702, second_product=234:50727, answer=219:59726)
- Layer 36: ` definitions`, ` Definitions`, `Definitions`, `分解`, ` equations` (target ranks: base_value=59:5627, first_product=118:62480, bound_value=117:37582, second_product=234:49157, answer=219:56458)
- Layer 37: ` definitions`, `}<?`, `Definitions`, ` variables`, ` Definitions` (target ranks: base_value=59:33179, first_product=118:96098, bound_value=117:76207, second_product=234:90821, answer=219:92014)
- Layer 38: `}<?`, ` definitions`, `Definitions`, ` Definitions`, `y` (target ranks: base_value=59:32065, first_product=118:92516, bound_value=117:78861, second_product=234:74348, answer=219:92173)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `acons`, `迷惑`, `yv` (target ranks: base_value=59:52597, first_product=118:111589, bound_value=117:89156, second_product=234:84966, answer=219:90610)
- Layer 40: `y`, `ses`, `acl`, `迷惑`, ` y` (target ranks: base_value=59:19931, first_product=118:86223, bound_value=117:64146, second_product=234:81919, answer=219:33511)
- Layer 41: `y`, ` .`, ` maze`, ` `, `不加` (target ranks: base_value=59:3159, first_product=118:32863, bound_value=117:18003, second_product=234:26654, answer=219:839)

### Filler position 27 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126295, first_product=118:122228, bound_value=117:122979, second_product=234:120254, answer=219:125325)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8447, first_product=118:21960, bound_value=117:20671, second_product=234:23271, answer=219:21648)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` engaging` (target ranks: base_value=59:8260, first_product=118:32614, bound_value=117:24150, second_product=234:29176, answer=219:34932)
- Layer 30: ` Tw`, `Tw`, `鞍`, ` labor`, `拆` (target ranks: base_value=59:6896, first_product=118:47601, bound_value=117:41487, second_product=234:35075, answer=219:53699)
- Layer 35: ` Tw`, `Tw`, `tw`, ` labor`, `Tap` (target ranks: base_value=59:2004, first_product=118:37156, bound_value=117:28210, second_product=234:27028, answer=219:39515)
- Layer 36: ` Tw`, `Tw`, `留存`, `分解`, `退出` (target ranks: base_value=59:3839, first_product=118:23202, bound_value=117:18567, second_product=234:24968, answer=219:35505)
- Layer 37: ` Tw`, ` doubling`, `翻`, `翻了`, ` Min` (target ranks: base_value=59:12137, first_product=118:33511, bound_value=117:25196, second_product=234:43086, answer=219:55423)
- Layer 38: ` doubling`, ` Tw`, `zat`, ` Duc`, `}<?` (target ranks: base_value=59:20509, first_product=118:49003, bound_value=117:42505, second_product=234:51305, answer=219:79099)
- Layer 39: `}<?`, ` Tw`, `zat`, ` Duc`, ` doubling` (target ranks: base_value=59:15360, first_product=118:68155, bound_value=117:59541, second_product=234:47555, answer=219:57585)
- Layer 40: `y`, `acl`, ` x`, ` y`, `duc` (target ranks: base_value=59:2003, first_product=118:29830, bound_value=117:21472, second_product=234:30982, answer=219:9963)
- Layer 41: `y`, ` `, `俯`, `plier`, `等待` (target ranks: base_value=59:332, first_product=118:10190, bound_value=117:5899, second_product=234:8522, answer=219:295)

### Filler position 28 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=59:126347, first_product=118:122364, bound_value=117:123185, second_product=234:120354, answer=219:125507)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:8768, first_product=118:21571, bound_value=117:20594, second_product=234:24209, answer=219:22794)
- Layer 20: `能被`, `ait`, ` Walker`, `拆`, `Walker` (target ranks: base_value=59:4429, first_product=118:22132, bound_value=117:14681, second_product=234:27799, answer=219:23507)
- Layer 30: `粥`, ` iceberg`, `acin`, `adows`, `退出` (target ranks: base_value=59:37, first_product=118:2894, bound_value=117:405, second_product=234:5239, answer=219:4679)
- Layer 35: `234`, `235`, ` Aure`, ` aure`, ` Behaviour` (target ranks: base_value=59:989, first_product=118:28571, bound_value=117:883, second_product=234:1, answer=219:132)
- Layer 36: `219`, ` Labour`, `内膜`, ` labour`, ` EMB` (target ranks: base_value=59:40596, first_product=118:3024, bound_value=117:1246, second_product=234:188, answer=219:1)
- Layer 37: `219`, `<｜place▁holder▁no▁173｜>`, ` embar`, `内膜`, ` Forum` (target ranks: base_value=59:84590, first_product=118:3881, bound_value=117:1408, second_product=234:275, answer=219:1)
- Layer 38: `219`, `119`, `217`, `十九`, `椿` (target ranks: base_value=59:79816, first_product=118:545, bound_value=117:694, second_product=234:2885, answer=219:1)
- Layer 39: `219`, `221`, `218`, `220`, `217` (target ranks: base_value=59:114483, first_product=118:75736, bound_value=117:89073, second_product=234:22196, answer=219:1)
- Layer 40: `219`, ` talags`, `217`, ` mosunod`, ` careg` (target ranks: base_value=59:116463, first_product=118:65137, bound_value=117:25310, second_product=234:3547, answer=219:1)
- Layer 41: `219`, ` nuest`, `}}}`, ` Expressible`, `))))` (target ranks: base_value=59:90532, first_product=118:53800, bound_value=117:38131, second_product=234:7581, answer=219:1)

### Filler position 29 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=59:126432, first_product=118:122509, bound_value=117:123310, second_product=234:120469, answer=219:125574)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:9323, first_product=118:22543, bound_value=117:21655, second_product=234:25096, answer=219:24121)
- Layer 20: `能被`, ` smile`, `距`, `锁定`, ` engaging` (target ranks: base_value=59:8106, first_product=118:24569, bound_value=117:18278, second_product=234:40607, answer=219:29662)
- Layer 30: `59`, `分解`, `出生`, `生日`, `yg` (target ranks: base_value=59:1, first_product=118:30, bound_value=117:32, second_product=234:20860, answer=219:10387)
- Layer 35: `117`, `分解`, ` Wil`, `Wil`, `radesh` (target ranks: base_value=59:18, first_product=118:37, bound_value=117:1, second_product=234:2881, answer=219:34578)
- Layer 36: `117`, `}<?`, `radesh`, `翻`, ` Wil` (target ranks: base_value=59:3902, first_product=118:18, bound_value=117:1, second_product=234:7774, answer=219:96209)
- Layer 37: `}<?`, `117`, ` doubles`, ` doubling`, `奶` (target ranks: base_value=59:15155, first_product=118:76, bound_value=117:2, second_product=234:24626, answer=219:119443)
- Layer 38: `}<?`, `117`, ` gonad`, ` Gon`, ` doubles` (target ranks: base_value=59:9879, first_product=118:57, bound_value=117:2, second_product=234:24654, answer=219:123782)
- Layer 39: `}<?`, ` Gon`, ` gon`, ` lut`, `叶子` (target ranks: base_value=59:8752, first_product=118:2785, bound_value=117:6, second_product=234:34425, answer=219:123646)
- Layer 40: `}<?`, `翻`, `俯`, ` Tw`, ` ` (target ranks: base_value=59:15060, first_product=118:15802, bound_value=117:21, second_product=234:23670, answer=219:68933)
- Layer 41: ` .`, `因为`, ` `, `太多了`, ` waiting` (target ranks: base_value=59:3655, first_product=118:2691, bound_value=117:10, second_product=234:7046, answer=219:11201)

### Filler position 30 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=59:126689, first_product=118:123185, bound_value=117:123911, second_product=234:120975, answer=219:126018)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8837, first_product=118:21716, bound_value=117:21107, second_product=234:24146, answer=219:22770)
- Layer 20: `cape`, `ait`, `锁定`, ` wig`, ` smile` (target ranks: base_value=59:7483, first_product=118:19840, bound_value=117:13876, second_product=234:19520, answer=219:19259)
- Layer 30: `Tap`, ` tap`, `鞍`, `tap`, ` Tap` (target ranks: base_value=59:9752, first_product=118:64172, bound_value=117:44635, second_product=234:40424, answer=219:30493)
- Layer 35: ` tap`, ` vertical`, `Tap`, `重复`, ` sequential` (target ranks: base_value=59:2587, first_product=118:67248, bound_value=117:50582, second_product=234:36911, answer=219:24513)
- Layer 36: ` tap`, `反复`, `重复`, ` vertical`, ` stabil` (target ranks: base_value=59:5252, first_product=118:52273, bound_value=117:46707, second_product=234:48298, answer=219:30651)
- Layer 37: `comp`, `}<?`, `数学`, `差错`, `itore` (target ranks: base_value=59:21780, first_product=118:85191, bound_value=117:80159, second_product=234:91135, answer=219:64912)
- Layer 38: `差错`, `ozygous`, ` lenker`, `}<?`, `�` (target ranks: base_value=59:27114, first_product=118:74734, bound_value=117:80909, second_product=234:78581, answer=219:57157)
- Layer 39: `aharan`, ` lenker`, `<｜begin▁of▁sentence｜>`, `}<?`, `�` (target ranks: base_value=59:34893, first_product=118:87335, bound_value=117:77284, second_product=234:66748, answer=219:30938)
- Layer 40: `acular`, ` fifty`, `inkle`, ` doubly`, `差错` (target ranks: base_value=59:9721, first_product=118:33035, bound_value=117:18207, second_product=234:50425, answer=219:256)
- Layer 41: ` .`, `219`, ` number`, `y`, `<｜end▁of▁sentence｜>` (target ranks: base_value=59:569, first_product=118:2960, bound_value=117:1281, second_product=234:5886, answer=219:2)

### Filler position 31 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=59:126762, first_product=118:123465, bound_value=117:124161, second_product=234:121166, answer=219:126226)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8127, first_product=118:20742, bound_value=117:20165, second_product=234:23550, answer=219:22025)
- Layer 20: `锁定`, `鞍`, ` smile`, `ait`, ` LS` (target ranks: base_value=59:8011, first_product=118:21357, bound_value=117:18034, second_product=234:17304, answer=219:18174)
- Layer 30: ` Answer`, `Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=59:4973, first_product=118:38180, bound_value=117:9442, second_product=234:17203, answer=219:4449)
- Layer 35: ` Answer`, `Answer`, ` answer`, `answer`, `回答` (target ranks: base_value=59:1778, first_product=118:18995, bound_value=117:2066, second_product=234:9420, answer=219:1653)
- Layer 36: ` Answer`, ` answer`, `Answer`, ` tap`, `鞍` (target ranks: base_value=59:2765, first_product=118:14489, bound_value=117:3293, second_product=234:9356, answer=219:3597)
- Layer 37: `}<?`, ` Answer`, ` reson`, `rational`, ` rational` (target ranks: base_value=59:19101, first_product=118:38554, bound_value=117:7643, second_product=234:23809, answer=219:10600)
- Layer 38: `}<?`, `aharan`, `不加`, `ivit`, ` Reson` (target ranks: base_value=59:45989, first_product=118:36656, bound_value=117:10219, second_product=234:17102, answer=219:12505)
- Layer 39: `}<?`, `aharan`, `<｜begin▁of▁sentence｜>`, `hatic`, `迷惑` (target ranks: base_value=59:78590, first_product=118:78717, bound_value=117:24877, second_product=234:28427, answer=219:7618)
- Layer 40: `radesh`, `留存`, `219`, `acular`, `坏的` (target ranks: base_value=59:44620, first_product=118:55088, bound_value=117:8103, second_product=234:13005, answer=219:3)
- Layer 41: `219`, ` .`, `y`, `217`, `yat` (target ranks: base_value=59:8625, first_product=118:11539, bound_value=117:1193, second_product=234:2884, answer=219:1)

### Filler position 32 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=59:126705, first_product=118:123221, bound_value=117:123899, second_product=234:120968, answer=219:126004)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8245, first_product=118:20741, bound_value=117:19857, second_product=234:22450, answer=219:21718)
- Layer 20: ` Walker`, ` ES`, `锁定`, `ait`, ` LS` (target ranks: base_value=59:7457, first_product=118:23933, bound_value=117:17094, second_product=234:14355, answer=219:25880)
- Layer 30: ` Xen`, ` x`, `xes`, ` xen`, ` X` (target ranks: base_value=59:28683, first_product=118:64001, bound_value=117:69640, second_product=234:58336, answer=219:63363)
- Layer 35: ` x`, ` Tw`, ` X`, `-x`, ` Xen` (target ranks: base_value=59:3055, first_product=118:16272, bound_value=117:15223, second_product=234:27859, answer=219:26056)
- Layer 36: ` x`, ` Tw`, ` X`, `第一步`, `留存` (target ranks: base_value=59:7774, first_product=118:6592, bound_value=117:6778, second_product=234:20233, answer=219:18746)
- Layer 37: ` x`, ` XCT`, ` xyl`, ` 𝑥`, `xv` (target ranks: base_value=59:31177, first_product=118:8319, bound_value=117:10522, second_product=234:31913, answer=219:23838)
- Layer 38: ` x`, ` XCT`, ` xyl`, `zel`, ` doubling` (target ranks: base_value=59:44731, first_product=118:7194, bound_value=117:11038, second_product=234:31171, answer=219:25663)
- Layer 39: ` x`, ` Xavier`, ` xyl`, ` XCT`, ` X` (target ranks: base_value=59:66908, first_product=118:27790, bound_value=117:22068, second_product=234:19258, answer=219:9514)
- Layer 40: ` x`, `x`, ` X`, ` pals`, `坏的` (target ranks: base_value=59:10527, first_product=118:6595, bound_value=117:2374, second_product=234:10114, answer=219:257)
- Layer 41: `y`, `步骤如下`, ` first`, ` x`, `219` (target ranks: base_value=59:2619, first_product=118:1061, bound_value=117:1010, second_product=234:1331, answer=219:5)

### Filler position 33 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `Noiz`, `�乐` (target ranks: base_value=59:126715, first_product=118:123422, bound_value=117:124071, second_product=234:121171, answer=219:126207)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:7902, first_product=118:20429, bound_value=117:19225, second_product=234:21326, answer=219:20850)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=59:8341, first_product=118:27766, bound_value=117:17490, second_product=234:20350, answer=219:29237)
- Layer 30: `Y`, ` Y`, ` y`, `y`, ` Yok` (target ranks: base_value=59:4856, first_product=118:93343, bound_value=117:59927, second_product=234:48920, answer=219:74451)
- Layer 35: ` y`, ` Y`, `Y`, `y`, ` reserved` (target ranks: base_value=59:671, first_product=118:63897, bound_value=117:26458, second_product=234:26897, answer=219:52233)
- Layer 36: `y`, ` y`, `adal`, `留存`, ` Y` (target ranks: base_value=59:3102, first_product=118:48970, bound_value=117:16580, second_product=234:24526, answer=219:55253)
- Layer 37: `}<?`, `y`, `不加`, ` y`, `referent` (target ranks: base_value=59:13151, first_product=118:82819, bound_value=117:43097, second_product=234:43060, answer=219:79206)
- Layer 38: `}<?`, `不加`, `Base`, ` base`, `迷惑` (target ranks: base_value=59:16712, first_product=118:78761, bound_value=117:52990, second_product=234:42199, answer=219:90597)
- Layer 39: `}<?`, `uerak`, `迷惑`, ` BASIS`, `.y` (target ranks: base_value=59:28121, first_product=118:96133, bound_value=117:66168, second_product=234:55091, answer=219:80495)
- Layer 40: ` y`, `y`, `不加`, ` Y`, ` talags` (target ranks: base_value=59:3950, first_product=118:44801, bound_value=117:19726, second_product=234:32724, answer=219:17033)
- Layer 41: `不加`, ` .`, `外商投资`, `不思`, `没有被` (target ranks: base_value=59:1508, first_product=118:28449, bound_value=117:13221, second_product=234:14758, answer=219:3556)

### Filler position 34 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `Noiz`, `�乐` (target ranks: base_value=59:126851, first_product=118:123610, bound_value=117:124208, second_product=234:120994, answer=219:126204)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8361, first_product=118:21694, bound_value=117:20292, second_product=234:22026, answer=219:21525)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` smile` (target ranks: base_value=59:9396, first_product=118:32734, bound_value=117:20130, second_product=234:23395, answer=219:30662)
- Layer 30: ` dy`, `acos`, `保留`, `�`, `退出` (target ranks: base_value=59:10526, first_product=118:69587, bound_value=117:57518, second_product=234:43452, answer=219:66575)
- Layer 35: ` y`, ` Y`, `Y`, `YO`, ` Yok` (target ranks: base_value=59:2250, first_product=118:62203, bound_value=117:40596, second_product=234:30142, answer=219:39551)
- Layer 36: `留存`, ` y`, `y`, `yel`, ` Y` (target ranks: base_value=59:7143, first_product=118:51642, bound_value=117:29835, second_product=234:26463, answer=219:40984)
- Layer 37: `yel`, `}<?`, `取舍`, `Quintal`, `放下了` (target ranks: base_value=59:37038, first_product=118:88183, bound_value=117:69926, second_product=234:53822, answer=219:70392)
- Layer 38: `yel`, `取舍`, `}<?`, `迷惑`, `zat` (target ranks: base_value=59:30061, first_product=118:79823, bound_value=117:68893, second_product=234:55518, answer=219:76978)
- Layer 39: `yel`, ` y`, `.y`, ` 𝑦`, `}<?` (target ranks: base_value=59:43949, first_product=118:94216, bound_value=117:78282, second_product=234:55534, answer=219:55411)
- Layer 40: ` x`, `yel`, ` y`, `y`, `留存` (target ranks: base_value=59:8130, first_product=118:46322, bound_value=117:26664, second_product=234:28505, answer=219:5848)
- Layer 41: ` compounding`, ` compounded`, `zij`, `acular`, `留存` (target ranks: base_value=59:2154, first_product=118:18775, bound_value=117:7814, second_product=234:5537, answer=219:291)

### Filler position 35 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=59:126824, first_product=118:123641, bound_value=117:124266, second_product=234:121236, answer=219:126273)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9524, first_product=118:23453, bound_value=117:22182, second_product=234:24102, answer=219:23102)
- Layer 20: `ait`, `足`, ` smile`, `幽`, `锁定` (target ranks: base_value=59:6060, first_product=118:21331, bound_value=117:12215, second_product=234:16466, answer=219:17401)
- Layer 30: `回答`, `锁定`, ` answer`, `应答`, `tap` (target ranks: base_value=59:5796, first_product=118:11783, bound_value=117:4316, second_product=234:13170, answer=219:10816)
- Layer 35: ` answer`, `cape`, `应答`, `锁定`, ` repetition` (target ranks: base_value=59:1587, first_product=118:5219, bound_value=117:1883, second_product=234:8108, answer=219:5522)
- Layer 36: ` immediate`, `calcul`, ` Immediate`, ` answer`, ` tap` (target ranks: base_value=59:4128, first_product=118:3132, bound_value=117:1856, second_product=234:10181, answer=219:6366)
- Layer 37: ` immediate`, ` Immediate`, `}<?`, `calcul`, `instant` (target ranks: base_value=59:15191, first_product=118:8170, bound_value=117:4741, second_product=234:28096, answer=219:19528)
- Layer 38: `calcul`, ` immediate`, `}<?`, ` Immediate`, `坏` (target ranks: base_value=59:10789, first_product=118:5745, bound_value=117:3785, second_product=234:23009, answer=219:20964)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `响应`, ` RES`, ` Res` (target ranks: base_value=59:36698, first_product=118:23877, bound_value=117:14059, second_product=234:22454, answer=219:23254)
- Layer 40: `坏`, `<｜begin▁of▁sentence｜>`, ` Res`, `asking`, `响应` (target ranks: base_value=59:12041, first_product=118:5871, bound_value=117:3765, second_product=234:11306, answer=219:1236)
- Layer 41: ` compounding`, `Answer`, `坏`, ` .`, ` ` (target ranks: base_value=59:631, first_product=118:455, bound_value=117:256, second_product=234:1204, answer=219:30)

### Filler position 36 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=59:126933, first_product=118:123947, bound_value=117:124495, second_product=234:121654, answer=219:126427)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:10385, first_product=118:24659, bound_value=117:23406, second_product=234:26626, answer=219:25009)
- Layer 20: ` Walker`, `能被`, `距`, `ait`, ` engaging` (target ranks: base_value=59:11399, first_product=118:34503, bound_value=117:25417, second_product=234:39744, answer=219:29684)
- Layer 30: `117`, `118`, `}<?`, `生日`, `119` (target ranks: base_value=59:358, first_product=118:2, bound_value=117:1, second_product=234:4144, answer=219:4575)
- Layer 35: `117`, ` catar`, ` cataract`, `234`, `}<?` (target ranks: base_value=59:12517, first_product=118:49, bound_value=117:1, second_product=234:4, answer=219:16296)
- Layer 36: `117`, `}<?`, `234`, ` catar`, ` cataract` (target ranks: base_value=59:99268, first_product=118:74, bound_value=117:1, second_product=234:3, answer=219:73926)
- Layer 37: `117`, `}<?`, ` Nij`, ` Fathers`, ` gonad` (target ranks: base_value=59:118696, first_product=118:260, bound_value=117:1, second_product=234:6, answer=219:109551)
- Layer 38: `117`, `}<?`, `234`, ` gonad`, ` Gon` (target ranks: base_value=59:117463, first_product=118:81, bound_value=117:1, second_product=234:3, answer=219:104562)
- Layer 39: `117`, `}<?`, ` Gon`, `234`, `<｜place▁holder▁no▁694｜>` (target ranks: base_value=59:101801, first_product=118:1149, bound_value=117:1, second_product=234:4, answer=219:80360)
- Layer 40: `117`, `}<?`, `apon`, `234`, `apoda` (target ranks: base_value=59:79416, first_product=118:9198, bound_value=117:1, second_product=234:4, answer=219:1993)
- Layer 41: `117`, `因为这些`, `234`, `ynd`, ` dich` (target ranks: base_value=59:16991, first_product=118:3111, bound_value=117:1, second_product=234:3, answer=219:461)

### Filler position 37 (absolute token 845, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=59:127008, first_product=118:124129, bound_value=117:124658, second_product=234:121519, answer=219:126484)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9833, first_product=118:24875, bound_value=117:23271, second_product=234:26735, answer=219:25138)
- Layer 20: `忑`, `能被`, `距`, ` Walker`, `ait` (target ranks: base_value=59:10827, first_product=118:37281, bound_value=117:26315, second_product=234:44059, answer=219:37543)
- Layer 30: `Tw`, `117`, ` granul`, `鞍`, `atar` (target ranks: base_value=59:65, first_product=118:129, bound_value=117:2, second_product=234:3830, answer=219:7573)
- Layer 35: `234`, `117`, ` cataract`, ` catar`, `出生` (target ranks: base_value=59:8084, first_product=118:6998, bound_value=117:2, second_product=234:1, answer=219:8136)
- Layer 36: `234`, `117`, `}<?`, `养护`, ` cataract` (target ranks: base_value=59:93549, first_product=118:13055, bound_value=117:2, second_product=234:1, answer=219:65819)
- Layer 37: `234`, `}<?`, `117`, `?datasetId`, ` Nij` (target ranks: base_value=59:120943, first_product=118:20046, bound_value=117:3, second_product=234:1, answer=219:99534)
- Layer 38: `234`, `}<?`, `117`, ` Gon`, `本题分析` (target ranks: base_value=59:119415, first_product=118:19424, bound_value=117:3, second_product=234:1, answer=219:90444)
- Layer 39: `234`, `}<?`, `117`, ` Gon`, `东海` (target ranks: base_value=59:91268, first_product=118:17703, bound_value=117:3, second_product=234:1, answer=219:20327)
- Layer 40: `234`, `117`, `}<?`, `二百`, ` ` (target ranks: base_value=59:53684, first_product=118:21793, bound_value=117:2, second_product=234:1, answer=219:14)
- Layer 41: `234`, `因为这些`, `117`, `217`, `219` (target ranks: base_value=59:21938, first_product=118:6899, bound_value=117:3, second_product=234:1, answer=219:5)

### Filler position 38 (absolute token 846, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=59:127024, first_product=118:124255, bound_value=117:124784, second_product=234:121841, answer=219:126561)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9180, first_product=118:23241, bound_value=117:22079, second_product=234:25695, answer=219:23551)
- Layer 20: `忑`, `ait`, `能被`, ` ES`, `atile` (target ranks: base_value=59:10830, first_product=118:50762, bound_value=117:37640, second_product=234:41471, answer=219:39489)
- Layer 30: `acos`, `sac`, ` tap`, ` Sop`, ` Rhe` (target ranks: base_value=59:46772, first_product=118:127462, bound_value=117:119481, second_product=234:101061, answer=219:107827)
- Layer 35: ` tap`, `zim`, ` Wil`, ` zain`, `Tap` (target ranks: base_value=59:38423, first_product=118:123750, bound_value=117:105853, second_product=234:83324, answer=219:81917)
- Layer 36: ` zad`, ` tap`, `zim`, ` zain`, ` Wil` (target ranks: base_value=59:32640, first_product=118:118114, bound_value=117:82542, second_product=234:61272, answer=219:61092)
- Layer 37: `zim`, ` Zed`, ` Nij`, ` Nim`, `zat` (target ranks: base_value=59:70905, first_product=118:123836, bound_value=117:105901, second_product=234:89120, answer=219:90556)
- Layer 38: `zat`, `}<?`, ` Nij`, `本题分析`, `zos` (target ranks: base_value=59:92376, first_product=118:124452, bound_value=117:114863, second_product=234:103948, answer=219:109888)
- Layer 39: `zim`, ` Nij`, `zos`, ` Zed`, `zor` (target ranks: base_value=59:100951, first_product=118:116187, bound_value=117:95976, second_product=234:41949, answer=219:12477)
- Layer 40: `zim`, `zij`, `zel`, `zos`, `zor` (target ranks: base_value=59:87990, first_product=118:105414, bound_value=117:65290, second_product=234:29523, answer=219:545)
- Layer 41: `zij`, `zel`, `219`, `ugi`, `zos` (target ranks: base_value=59:28614, first_product=118:15461, bound_value=117:2563, second_product=234:2383, answer=219:3)

### Filler position 39 (absolute token 847, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=59:127005, first_product=118:124344, bound_value=117:124854, second_product=234:121927, answer=219:126677)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:8737, first_product=118:22611, bound_value=117:21448, second_product=234:24793, answer=219:23047)
- Layer 20: `ait`, `锁定`, ` Walker`, `鞍`, ` smile` (target ranks: base_value=59:6835, first_product=118:30284, bound_value=117:18315, second_product=234:23205, answer=219:25422)
- Layer 30: `sms`, ` seventy`, `yata`, `79`, `67` (target ranks: base_value=59:66, first_product=118:11025, bound_value=117:280, second_product=234:1557, answer=219:1153)
- Layer 35: `退出`, `acin`, `抽`, ` dy`, ` smooth` (target ranks: base_value=59:3975, first_product=118:73647, bound_value=117:13037, second_product=234:17, answer=219:20)
- Layer 36: `抽`, ` talags`, `acin`, `yg`, `219` (target ranks: base_value=59:36946, first_product=118:64845, bound_value=117:9412, second_product=234:7567, answer=219:5)
- Layer 37: `}<?`, ` smoot`, ` talags`, `ocyst`, `217` (target ranks: base_value=59:91223, first_product=118:72711, bound_value=117:13906, second_product=234:10212, answer=219:9)
- Layer 38: `}<?`, ` talags`, `219`, `217`, ` anomaly` (target ranks: base_value=59:69271, first_product=118:85276, bound_value=117:16728, second_product=234:60490, answer=219:3)
- Layer 39: `219`, ` talags`, `tanle`, `ocyst`, `}<?` (target ranks: base_value=59:84921, first_product=118:114101, bound_value=117:52249, second_product=234:19323, answer=219:1)
- Layer 40: ` talags`, `219`, `217`, `第二百`, `acular` (target ranks: base_value=59:88100, first_product=118:112698, bound_value=117:49479, second_product=234:14736, answer=219:2)
- Layer 41: `219`, `217`, ` waiting`, `第二百`, `等待` (target ranks: base_value=59:40683, first_product=118:66423, bound_value=117:19883, second_product=234:9635, answer=219:1)

### Filler position 40 (absolute token 848, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127091, first_product=118:124600, bound_value=117:125012, second_product=234:122009, answer=219:126811)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9331, first_product=118:22868, bound_value=117:22069, second_product=234:25369, answer=219:23874)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, `距` (target ranks: base_value=59:6891, first_product=118:31522, bound_value=117:22452, second_product=234:29644, answer=219:28488)
- Layer 30: `acos`, ` Dy`, `Dy`, ` seventy`, `79` (target ranks: base_value=59:22, first_product=118:3335, bound_value=117:147, second_product=234:3643, answer=219:4466)
- Layer 35: `234`, `235`, `233`, `135`, `134` (target ranks: base_value=59:2806, first_product=118:72661, bound_value=117:6649, second_product=234:1, answer=219:28)
- Layer 36: `219`, `erger`, `221`, `酒吧`, `<｜place▁holder▁no▁173｜>` (target ranks: base_value=59:50418, first_product=118:5036, bound_value=117:4701, second_product=234:20, answer=219:1)
- Layer 37: `219`, `<｜place▁holder▁no▁173｜>`, ` Markov`, `erger`, `院长` (target ranks: base_value=59:80856, first_product=118:5205, bound_value=117:5750, second_product=234:39, answer=219:1)
- Layer 38: `219`, ` ninete`, `十九章`, `第十九`, `十九` (target ranks: base_value=59:36680, first_product=118:3452, bound_value=117:9297, second_product=234:871, answer=219:1)
- Layer 39: `219`, `319`, `419`, `119`, `719` (target ranks: base_value=59:103942, first_product=118:125425, bound_value=117:125714, second_product=234:33144, answer=219:1)
- Layer 40: `219`, `<｜begin▁of▁file｜>`, `จจ`, `LikeLike`, ` embra` (target ranks: base_value=59:114543, first_product=118:113468, bound_value=117:73485, second_product=234:12591, answer=219:1)
- Layer 41: `219`, `}}}`, ` dátummal`, `}}}}`, `))))` (target ranks: base_value=59:72681, first_product=118:70809, bound_value=117:46044, second_product=234:6338, answer=219:1)

### Filler position 41 (absolute token 849, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=59:126921, first_product=118:124253, bound_value=117:124788, second_product=234:121650, answer=219:126617)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9574, first_product=118:23162, bound_value=117:22534, second_product=234:25409, answer=219:24049)
- Layer 20: `锁定`, `ait`, ` smile`, ` LS`, `LS` (target ranks: base_value=59:7645, first_product=118:27369, bound_value=117:20861, second_product=234:23216, answer=219:19908)
- Layer 30: `陪`, `保留`, `Dy`, `放弃`, `acos` (target ranks: base_value=59:71, first_product=118:7473, bound_value=117:905, second_product=234:12023, answer=219:4659)
- Layer 35: `234`, `235`, `134`, ` imperial`, ` Dy` (target ranks: base_value=59:11622, first_product=118:86328, bound_value=117:17067, second_product=234:1, answer=219:48)
- Layer 36: `219`, `221`, `234`, ` Markov`, `酒吧` (target ranks: base_value=59:74722, first_product=118:4145, bound_value=117:3894, second_product=234:3, answer=219:1)
- Layer 37: `219`, `<｜place▁holder▁no▁173｜>`, ` Markov`, `院长`, `234` (target ranks: base_value=59:102425, first_product=118:3459, bound_value=117:4420, second_product=234:5, answer=219:1)
- Layer 38: `219`, `十九章`, `第十九`, ` ninete`, `十九` (target ranks: base_value=59:32472, first_product=118:1644, bound_value=117:8681, second_product=234:136, answer=219:1)
- Layer 39: `219`, `319`, `119`, ` torped`, ` markup` (target ranks: base_value=59:117723, first_product=118:114736, bound_value=117:121331, second_product=234:8714, answer=219:1)
- Layer 40: `219`, `inz`, `全场`, `}<?`, ` talags` (target ranks: base_value=59:103269, first_product=118:73904, bound_value=117:34268, second_product=234:1423, answer=219:1)
- Layer 41: `219`, `}}}`, ` nuest`, `}}}↵↵`, ` inference` (target ranks: base_value=59:39856, first_product=118:27551, bound_value=117:16058, second_product=234:1463, answer=219:1)

### Filler position 42 (absolute token 850, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127255, first_product=118:125072, bound_value=117:125450, second_product=234:122506, answer=219:127060)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:10242, first_product=118:23986, bound_value=117:23439, second_product=234:25814, answer=219:24754)
- Layer 20: `锁定`, ` smile`, `ait`, `鞍`, `cape` (target ranks: base_value=59:7800, first_product=118:22141, bound_value=117:18930, second_product=234:20405, answer=219:16488)
- Layer 30: ` Tw`, ` twice`, `Tw`, `询问`, `tw` (target ranks: base_value=59:11135, first_product=118:42780, bound_value=117:53021, second_product=234:50966, answer=219:37232)
- Layer 35: ` Tw`, `询问`, `Tw`, `tw`, ` twice` (target ranks: base_value=59:1792, first_product=118:18667, bound_value=117:22005, second_product=234:25320, answer=219:12658)
- Layer 36: `询问`, ` Tw`, `提问`, ` expression`, ` Expression` (target ranks: base_value=59:3346, first_product=118:18085, bound_value=117:23147, second_product=234:39703, answer=219:21616)
- Layer 37: `提问`, `询问`, `}<?`, ` question`, `asking` (target ranks: base_value=59:9791, first_product=118:22905, bound_value=117:27694, second_product=234:52647, answer=219:33780)
- Layer 38: `}<?`, `zat`, ` requested`, `asking`, ` doubling` (target ranks: base_value=59:11151, first_product=118:25932, bound_value=117:23976, second_product=234:54096, answer=219:35240)
- Layer 39: `}<?`, `东海`, ` doubling`, ` smoothing`, `打磨` (target ranks: base_value=59:14907, first_product=118:42757, bound_value=117:21202, second_product=234:34826, answer=219:21243)
- Layer 40: ` Tw`, `Tw`, ` twice`, `.tw`, ` doubling` (target ranks: base_value=59:816, first_product=118:3606, bound_value=117:746, second_product=234:9959, answer=219:396)
- Layer 41: ` `, ` number`, ` twice`, ` .`, `院内` (target ranks: base_value=59:148, first_product=118:381, bound_value=117:163, second_product=234:2631, answer=219:12)

### Filler position 43 (absolute token 851, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127251, first_product=118:125011, bound_value=117:125399, second_product=234:122641, answer=219:127082)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9930, first_product=118:24004, bound_value=117:23690, second_product=234:25246, answer=219:24696)
- Layer 20: ` smile`, `锁定`, ` Engaging`, ` engaging`, `距` (target ranks: base_value=59:12104, first_product=118:25072, bound_value=117:21195, second_product=234:21351, answer=219:17211)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=59:11, first_product=118:15460, bound_value=117:22483, second_product=234:53296, answer=219:16858)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=59:10, first_product=118:8660, bound_value=117:10617, second_product=234:36416, answer=219:12582)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=59:12, first_product=118:5522, bound_value=117:8462, second_product=234:37033, answer=219:20721)
- Layer 37: ` doubling`, ` Tw`, ` doubled`, `}<?`, `Tw` (target ranks: base_value=59:123, first_product=118:23747, bound_value=117:28177, second_product=234:76149, answer=219:46250)
- Layer 38: ` doubling`, `东海`, `}<?`, `duc`, ` doubled` (target ranks: base_value=59:407, first_product=118:36756, bound_value=117:37949, second_product=234:88203, answer=219:71562)
- Layer 39: `东海`, `}<?`, ` Tw`, ` doubling`, `interpret` (target ranks: base_value=59:8943, first_product=118:54233, bound_value=117:36691, second_product=234:38623, answer=219:22960)
- Layer 40: ` Tw`, ` y`, `Tw`, `y`, ` x` (target ranks: base_value=59:1036, first_product=118:14881, bound_value=117:4441, second_product=234:11673, answer=219:214)
- Layer 41: `219`, ` y`, ` Tw`, `Answer`, `y` (target ranks: base_value=59:36, first_product=118:425, bound_value=117:116, second_product=234:882, answer=219:1)

### Filler position 44 (absolute token 852, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127251, first_product=118:124775, bound_value=117:125217, second_product=234:122530, answer=219:126863)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:10598, first_product=118:24523, bound_value=117:24010, second_product=234:25778, answer=219:25338)
- Layer 20: `忑`, `ait`, `会成为`, ` engaging`, ` ES` (target ranks: base_value=59:17059, first_product=118:35769, bound_value=117:25677, second_product=234:31989, answer=219:29813)
- Layer 30: ` Tw`, ` twice`, `Tw`, `tw`, `算出` (target ranks: base_value=59:11, first_product=118:44245, bound_value=117:39887, second_product=234:89197, answer=219:61313)
- Layer 35: ` Tw`, `Tw`, `tw`, ` twice`, `.tw` (target ranks: base_value=59:11, first_product=118:27134, bound_value=117:17688, second_product=234:68154, answer=219:41371)
- Layer 36: ` Tw`, `Tw`, ` doubling`, ` twice`, `.tw` (target ranks: base_value=59:45, first_product=118:14743, bound_value=117:10633, second_product=234:56183, answer=219:41194)
- Layer 37: ` doubling`, ` doubled`, ` doubles`, ` Dou`, ` Tw` (target ranks: base_value=59:196, first_product=118:45382, bound_value=117:37780, second_product=234:85221, answer=219:62392)
- Layer 38: ` doubling`, ` doubled`, ` doubles`, ` Dou`, `东海` (target ranks: base_value=59:522, first_product=118:52193, bound_value=117:48537, second_product=234:92083, answer=219:82530)
- Layer 39: `东海`, `yv`, ` doubling`, `}<?`, `文字的` (target ranks: base_value=59:50656, first_product=118:74447, bound_value=117:47908, second_product=234:41464, answer=219:53444)
- Layer 40: ` x`, `y`, ` y`, ` talags`, `yat` (target ranks: base_value=59:35433, first_product=118:19631, bound_value=117:4035, second_product=234:6948, answer=219:3095)
- Layer 41: ` `, `y`, ` number`, ` .`, `不求` (target ranks: base_value=59:1845, first_product=118:936, bound_value=117:155, second_product=234:208, answer=219:16)

### Filler position 45 (absolute token 853, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=59:127180, first_product=118:124650, bound_value=117:125079, second_product=234:122315, answer=219:126686)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=59:9850, first_product=118:23617, bound_value=117:22772, second_product=234:25216, answer=219:24459)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `会成为` (target ranks: base_value=59:12446, first_product=118:43758, bound_value=117:23765, second_product=234:29615, answer=219:40461)
- Layer 30: `acos`, `acet`, ` x`, `sled`, `第一步` (target ranks: base_value=59:33039, first_product=118:112477, bound_value=117:96842, second_product=234:98279, answer=219:97613)
- Layer 35: ` x`, `acos`, `yata`, ` X`, `acic` (target ranks: base_value=59:11988, first_product=118:82923, bound_value=117:52001, second_product=234:58330, answer=219:75816)
- Layer 36: `留存`, ` x`, `反复`, `acos`, `yat` (target ranks: base_value=59:14584, first_product=118:53108, bound_value=117:25924, second_product=234:38641, answer=219:52283)
- Layer 37: `}<?`, `本题分析`, `铎`, ` sublim`, `acet` (target ranks: base_value=59:62633, first_product=118:95134, bound_value=117:56975, second_product=234:76218, answer=219:84706)
- Layer 38: `}<?`, `本题分析`, `铎`, `Quintal`, ` sublim` (target ranks: base_value=59:52330, first_product=118:78421, bound_value=117:53576, second_product=234:68639, answer=219:72544)
- Layer 39: `}<?`, `本题分析`, `东海`, ` sublim`, `文字的` (target ranks: base_value=59:58949, first_product=118:74962, bound_value=117:42815, second_product=234:27366, answer=219:30355)
- Layer 40: ` x`, `acular`, ` Tw`, `anin`, `留存` (target ranks: base_value=59:7788, first_product=118:33855, bound_value=117:9621, second_product=234:8348, answer=219:1069)
- Layer 41: ` `, ` .`, ` waterfall`, `<｜end▁of▁sentence｜>`, `acular` (target ranks: base_value=59:427, first_product=118:9494, bound_value=117:2215, second_product=234:1172, answer=219:35)

### Filler position 46 (absolute token 854, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127184, first_product=118:124886, bound_value=117:125218, second_product=234:122292, answer=219:126899)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=59:9560, first_product=118:22965, bound_value=117:21947, second_product=234:25308, answer=219:24426)
- Layer 20: `ait`, `俯`, ` adtong`, `sl`, ` spac` (target ranks: base_value=59:25834, first_product=118:62439, bound_value=117:24902, second_product=234:67868, answer=219:75863)
- Layer 30: ` spac`, `}using`, `坝`, ` dekameters`, `}<?` (target ranks: base_value=59:77798, first_product=118:113504, bound_value=117:93090, second_product=234:98729, answer=219:101546)
- Layer 35: `俯`, `ancock`, `滴水`, ` settling`, `dots` (target ranks: base_value=59:43149, first_product=118:102940, bound_value=117:65189, second_product=234:80150, answer=219:90457)
- Layer 36: `俯`, `ancock`, ` dro`, ` surveying`, `足足` (target ranks: base_value=59:10897, first_product=118:63876, bound_value=117:37953, second_product=234:44893, answer=219:55087)
- Layer 37: `}<?`, `俯`, `放下`, `isis`, `onana` (target ranks: base_value=59:42546, first_product=118:101546, bound_value=117:69037, second_product=234:48085, answer=219:88251)
- Layer 38: ` .`, `俯`, `错过`, ` nasod`, `坏` (target ranks: base_value=59:17229, first_product=118:89417, bound_value=117:64627, second_product=234:28211, answer=219:92199)
- Layer 39: `分院`, `osaurus`, `�`, ` .`, `oxygen` (target ranks: base_value=59:37920, first_product=118:108202, bound_value=117:65746, second_product=234:12199, answer=219:57719)
- Layer 40: ` .`, ` x`, ` nasod`, `�`, `俯` (target ranks: base_value=59:6769, first_product=118:71622, bound_value=117:26426, second_product=234:6791, answer=219:14735)
- Layer 41: ` .`, ` .↵↵`, ` `, ` bears`, `<｜end▁of▁sentence｜>` (target ranks: base_value=59:1272, first_product=118:19093, bound_value=117:2725, second_product=234:640, answer=219:219)

### Filler position 47 (absolute token 855, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127352, first_product=118:125195, bound_value=117:125595, second_product=234:122525, answer=219:127096)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=59:9199, first_product=118:22564, bound_value=117:21450, second_product=234:25214, answer=219:24397)
- Layer 20: `}<?`, ` partly`, `东海`, ` DeWalt`, `ozygous` (target ranks: base_value=59:100956, first_product=118:91993, bound_value=117:70240, second_product=234:124652, answer=219:111065)
- Layer 30: `}<?`, `}using`, `codeline`, `dividers`, ` spac` (target ranks: base_value=59:85986, first_product=118:93360, bound_value=117:98279, second_product=234:117251, answer=219:109033)
- Layer 35: `codeline`, `lett`, `蜗`, `浪费`, `ِّف` (target ranks: base_value=59:64210, first_product=118:113337, bound_value=117:104118, second_product=234:119917, answer=219:116607)
- Layer 36: `锯`, ` nasod`, `ancock`, ` fit`, `lett` (target ranks: base_value=59:15034, first_product=118:81846, bound_value=117:70140, second_product=234:98484, answer=219:97260)
- Layer 37: `}<?`, `磨损`, `ِّف`, `الميل`, `焯` (target ranks: base_value=59:37114, first_product=118:107460, bound_value=117:109664, second_product=234:58103, answer=219:104371)
- Layer 38: `遁`, ` .`, `切割`, `坏`, ` covari` (target ranks: base_value=59:13797, first_product=118:86925, bound_value=117:87071, second_product=234:37558, answer=219:105916)
- Layer 39: `�`, `磨损`, ` Fusion`, `lett`, ` .` (target ranks: base_value=59:55415, first_product=118:110803, bound_value=117:99172, second_product=234:36509, answer=219:79858)
- Layer 40: ` .`, `�`, ` .↵↵`, ` nasod`, ` .↵` (target ranks: base_value=59:15362, first_product=118:70632, bound_value=117:48581, second_product=234:18743, answer=219:30609)
- Layer 41: ` .`, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` `, ` .↵` (target ranks: base_value=59:2501, first_product=118:33712, bound_value=117:15265, second_product=234:2445, answer=219:3327)

### Filler position 48 (absolute token 856, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127184, first_product=118:125169, bound_value=117:125537, second_product=234:122416, answer=219:127034)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=59:9499, first_product=118:23456, bound_value=117:22229, second_product=234:26177, answer=219:25532)
- Layer 20: `aharoa`, `东海`, ` instantaneous`, `}<?`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=59:92791, first_product=118:65819, bound_value=117:66320, second_product=234:115885, answer=219:83384)
- Layer 30: `codeline`, `东京`, `Quintal`, ` equator`, `雄` (target ranks: base_value=59:41456, first_product=118:84788, bound_value=117:82276, second_product=234:121546, answer=219:93311)
- Layer 35: `codeline`, `AssemblyVersion`, ` Predict`, ` germ`, `删` (target ranks: base_value=59:54145, first_product=118:97667, bound_value=117:112095, second_product=234:124246, answer=219:115491)
- Layer 36: ` Predict`, `坏`, ` predictions`, ` nasod`, ` germ` (target ranks: base_value=59:22126, first_product=118:62984, bound_value=117:74614, second_product=234:118274, answer=219:112737)
- Layer 37: `codeline`, `Quintal`, `TreeLabel`, `镶嵌`, `悬挂` (target ranks: base_value=59:66514, first_product=118:90496, bound_value=117:109402, second_product=234:120138, answer=219:114329)
- Layer 38: `codeline`, ` germ`, `肤`, ` crev`, `牺牲` (target ranks: base_value=59:35056, first_product=118:73988, bound_value=117:83540, second_product=234:111081, answer=219:117992)
- Layer 39: ` unflagged`, ` .↵↵`, ` .`, ` encomp`, ` germ` (target ranks: base_value=59:56308, first_product=118:65885, bound_value=117:83437, second_product=234:113563, answer=219:99472)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` unflagged`, `肤` (target ranks: base_value=59:26216, first_product=118:43152, bound_value=117:59342, second_product=234:89570, answer=219:64865)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, ` guarante` (target ranks: base_value=59:4113, first_product=118:7826, bound_value=117:6807, second_product=234:25045, answer=219:8217)

### Filler position 49 (absolute token 857, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=59:127026, first_product=118:124778, bound_value=117:125201, second_product=234:122180, answer=219:126760)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=59:9498, first_product=118:24384, bound_value=117:22493, second_product=234:26537, answer=219:26226)
- Layer 20: ` licensierad`, ` originalet`, `文本`, ` grounds`, ` instantaneous` (target ranks: base_value=59:95781, first_product=118:82860, bound_value=117:88604, second_product=234:107245, answer=219:98982)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` Antwort`, `答案` (target ranks: base_value=59:73858, first_product=118:121797, bound_value=117:117664, second_product=234:127778, answer=219:120117)
- Layer 35: ` Answer`, `codeline`, ` Antwort`, ` retard`, ` answer` (target ranks: base_value=59:61259, first_product=118:120851, bound_value=117:124411, second_product=234:123016, answer=219:123960)
- Layer 36: ` Answer`, `坏`, ` answer`, `回答`, ` germ` (target ranks: base_value=59:17651, first_product=118:99368, bound_value=117:104653, second_product=234:111433, answer=219:120158)
- Layer 37: `oNames`, `codeline`, ` retard`, `�`, `insic` (target ranks: base_value=59:86879, first_product=118:119062, bound_value=117:108877, second_product=234:118509, answer=219:125176)
- Layer 38: `oNames`, `codeline`, ` retard`, `оду`, `�` (target ranks: base_value=59:95299, first_product=118:114885, bound_value=117:108657, second_product=234:112599, answer=219:122950)
- Layer 39: `�`, `-ulo`, `oxygen`, `deen`, `codeline` (target ranks: base_value=59:85406, first_product=118:115479, bound_value=117:111385, second_product=234:95792, answer=219:105053)
- Layer 40: ` Answer`, ` .`, ` wink`, `Answer`, ` tare` (target ranks: base_value=59:8762, first_product=118:56293, bound_value=117:56970, second_product=234:56371, answer=219:36987)
- Layer 41: ` Answer`, `Answer`, ` .`, ` twenty`, ` .↵↵` (target ranks: base_value=59:7191, first_product=118:40067, bound_value=117:41853, second_product=234:25995, answer=219:19815)

### Filler position 50 (absolute token 858, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=59:122340, first_product=118:112329, bound_value=117:111724, second_product=234:108732, answer=219:113032)
- Layer 10: `EDMF`, ` dével`, ` поха`, `-ulo`, ` Saysay` (target ranks: base_value=59:126211, first_product=118:113650, bound_value=117:114872, second_product=234:112837, answer=219:109780)
- Layer 20: `能被`, `平行`, ` Submission`, `差分`, `忑` (target ranks: base_value=59:16296, first_product=118:61134, bound_value=117:74880, second_product=234:88980, answer=219:51913)
- Layer 30: ` dátummal`, `nze`, `迷糊`, ` گزار`, ` Pole` (target ranks: base_value=59:17844, first_product=118:7811, bound_value=117:11746, second_product=234:52344, answer=219:14857)
- Layer 35: ` Behaviour`, ` dátummal`, `CopyWith`, ` Antar`, ` chains` (target ranks: base_value=59:35144, first_product=118:51811, bound_value=117:42159, second_product=234:6, answer=219:133)
- Layer 36: ` الجرم`, ` Ginhadi`, `盖章`, ` Lager`, ` giiniton` (target ranks: base_value=59:110489, first_product=118:14578, bound_value=117:5514, second_product=234:8849, answer=219:6)
- Layer 37: ` الجرم`, `缠绵`, ` سرعه`, ` giiniton`, ` поха` (target ranks: base_value=59:122638, first_product=118:19797, bound_value=117:7802, second_product=234:7070, answer=219:25)
- Layer 38: `219`, `217`, ` الجرم`, `东山`, `CopyWith` (target ranks: base_value=59:116612, first_product=118:14088, bound_value=117:18817, second_product=234:44226, answer=219:1)
- Layer 39: ` Answer`, ` Antwort`, `答案`, ` answer`, `219` (target ranks: base_value=59:89537, first_product=118:59708, bound_value=117:53204, second_product=234:79921, answer=219:5)
- Layer 40: ` Answer`, `Answer`, ` answer`, `answer`, `答` (target ranks: base_value=59:36707, first_product=118:29264, bound_value=117:13842, second_product=234:79572, answer=219:102)
- Layer 41: `Answer`, ` Answer`, ` answer`, `answer`, `答` (target ranks: base_value=59:5274, first_product=118:10841, bound_value=117:2936, second_product=234:22557, answer=219:75)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 50 filler tokens (a sequence of dots) before you answer.<｜User｜>zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>176<｜end▁of▁sentence｜><｜User｜>cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>59<｜end▁of▁sentence｜><｜User｜>gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>351<｜end▁of▁sentence｜><｜User｜>mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>229<｜end▁of▁sentence｜><｜User｜>kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>yuf = 59
fiv = twice the number for yuf minus 11
xel = twice the number for yuf minus 1
qub = twice the number for xel minus 7
wej = twice the number for xel minus 22
Question: What is twice the number for xel minus 15?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
