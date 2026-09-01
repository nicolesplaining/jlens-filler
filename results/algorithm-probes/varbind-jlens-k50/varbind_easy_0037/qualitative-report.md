# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `387` (incorrect).
- No-filler answer: `383` (incorrect).
- Filler tokens: 50 tokens at absolute indices 803–852.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=91` | 1 (L27, filler 1) | L22, filler 36 (rank 10) |
| J-Lens | `first_product=182` | 2 (L28, filler 34) | L28, filler 34 (rank 2) |
| J-Lens | `bound_value=187` | 1 (L30, filler 30) | L27, filler 34 (rank 4) |
| J-Lens | `second_product=374` | 1 (L31, filler 26) | L31, filler 1 (rank 7) |
| J-Lens | `answer=385` | 1 (L36, filler 13) | L31, filler 13 (rank 7) |
| Logit lens | `base_value=91` | 1 (L27, filler 29) | L27, filler 29 (rank 1) |
| Logit lens | `first_product=182` | 2 (L30, filler 34) | L28, filler 34 (rank 3) |
| Logit lens | `bound_value=187` | 1 (L29, filler 25) | L28, filler 21 (rank 4) |
| Logit lens | `second_product=374` | 1 (L35, filler 21) | L31, filler 26 (rank 10) |
| Logit lens | `answer=385` | 1 (L30, filler 15) | L28, filler 15 (rank 4) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 803, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=91:119023, first_product=182:114759, bound_value=187:114474, second_product=374:113411, answer=385:113644)
- Layer 10: `anta`, `fine`, `Hook`, `钩`, `hook` (target ranks: base_value=91:70876, first_product=182:72694, bound_value=187:67540, second_product=374:61542, answer=385:82811)
- Layer 20: `足`, ` LS`, `重`, `abric`, `扣` (target ranks: base_value=91:1107, first_product=182:18140, bound_value=187:9949, second_product=374:6706, answer=385:7859)
- Layer 30: ` talags`, ` pakig`, `期望`, `期待的`, `372` (target ranks: base_value=91:603, first_product=182:7588, bound_value=187:2482, second_product=374:40, answer=385:308)
- Layer 35: `387`, `375`, `379`, `383`, `381` (target ranks: base_value=91:30522, first_product=182:119498, bound_value=187:9783, second_product=374:22, answer=385:24)
- Layer 36: `775`, `375`, `387`, `795`, `755` (target ranks: base_value=91:56098, first_product=182:122846, bound_value=187:3366, second_product=374:52, answer=385:39)
- Layer 37: `775`, `375`, `387`, `755`, `767` (target ranks: base_value=91:88254, first_product=182:124732, bound_value=187:7926, second_product=374:55, answer=385:40)
- Layer 38: `775`, `387`, `375`, `795`, `767` (target ranks: base_value=91:110132, first_product=182:127134, bound_value=187:20607, second_product=374:156, answer=385:32)
- Layer 39: `775`, `387`, ` Clay`, `779`, ` clay` (target ranks: base_value=91:123846, first_product=182:128434, bound_value=187:54101, second_product=374:13343, answer=385:95)
- Layer 40: ` ald`, `Ald`, ` talags`, ` Ald`, `实在` (target ranks: base_value=91:125854, first_product=182:127509, bound_value=187:55351, second_product=374:9301, answer=385:1450)
- Layer 41: ` .`, `我对`, `样子`, `我已经`, `实践证明` (target ranks: base_value=91:111541, first_product=182:118080, bound_value=187:69538, second_product=374:37289, answer=385:5559)

### Filler position 2 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=91:120781, first_product=182:119216, bound_value=187:117491, second_product=374:117596, answer=385:120789)
- Layer 10: ` Walker`, `Walker`, `ait`, `挪`, `锁定` (target ranks: base_value=91:23441, first_product=182:39947, bound_value=187:34552, second_product=374:35751, answer=385:44079)
- Layer 20: ` .----`, `往常`, `oraly`, `ools`, `�乐` (target ranks: base_value=91:129205, first_product=182:128229, bound_value=187:125612, second_product=374:127512, answer=385:128394)
- Layer 30: ` pakig`, ` talags`, ` gilay`, ` hilabihan`, ` dekameters` (target ranks: base_value=91:129057, first_product=182:128015, bound_value=187:114834, second_product=374:114513, answer=385:122277)
- Layer 35: ` hilabihan`, ` pakig`, ` talags`, `enclose`, `滴水` (target ranks: base_value=91:128519, first_product=182:128222, bound_value=187:123398, second_product=374:126243, answer=385:126114)
- Layer 36: ` talags`, ` hilabihan`, `enclose`, `幽`, `停` (target ranks: base_value=91:123194, first_product=182:126685, bound_value=187:109814, second_product=374:117487, answer=385:111621)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, `�乐`, `aplenty` (target ranks: base_value=91:129158, first_product=182:127183, bound_value=187:126225, second_product=374:126248, answer=385:111282)
- Layer 38: ` .`, ` Erkännande`, ` hilabihan`, `繁体`, `enclose` (target ranks: base_value=91:127761, first_product=182:116668, bound_value=187:123044, second_product=374:124105, answer=385:79774)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` hilabihan`, ` .↵↵`, ` talags` (target ranks: base_value=91:127700, first_product=182:104499, bound_value=187:114360, second_product=374:102859, answer=385:40387)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, ` filler` (target ranks: base_value=91:118289, first_product=182:76646, bound_value=187:68379, second_product=374:64814, answer=385:14359)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `忏` (target ranks: base_value=91:75812, first_product=182:24905, bound_value=187:23275, second_product=374:12268, answer=385:2233)

### Filler position 3 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:122977, first_product=182:121387, bound_value=187:120032, second_product=374:119625, answer=385:123380)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=91:14473, first_product=182:31099, bound_value=187:27946, second_product=374:30462, answer=385:31172)
- Layer 20: `ait`, `忑`, `会成为`, `ashi`, `距` (target ranks: base_value=91:17748, first_product=182:54975, bound_value=187:45977, second_product=374:42833, answer=385:35254)
- Layer 30: ` dy`, ` variable`, ` variables`, `看看吧`, `赋值` (target ranks: base_value=91:52676, first_product=182:102984, bound_value=187:108479, second_product=374:99187, answer=385:81009)
- Layer 35: ` variables`, ` variable`, `变量的`, ` Variables`, `variables` (target ranks: base_value=91:32265, first_product=182:98707, bound_value=187:103985, second_product=374:77686, answer=385:66101)
- Layer 36: ` variables`, ` variable`, `变量的`, ` definitions`, `定义的` (target ranks: base_value=91:27661, first_product=182:83185, bound_value=187:81671, second_product=374:71689, answer=385:41612)
- Layer 37: `变量的`, ` variables`, `给定`, `variables`, `given` (target ranks: base_value=91:86520, first_product=182:107643, bound_value=187:117349, second_product=374:101160, answer=385:59530)
- Layer 38: `}<?`, `oses`, `asi`, `解释`, ` cál` (target ranks: base_value=91:95212, first_product=182:114335, bound_value=187:123391, second_product=374:110969, answer=385:61005)
- Layer 39: `ต้`, ` duc`, `繁体`, `asi`, `文字的` (target ranks: base_value=91:123590, first_product=182:128006, bound_value=187:119760, second_product=374:120714, answer=385:93742)
- Layer 40: ` dup`, `duc`, ` k`, ` mi`, `dup` (target ranks: base_value=91:117705, first_product=182:127665, bound_value=187:109509, second_product=374:112598, answer=385:71257)
- Layer 41: ` .`, ` ,`, `<｜end▁of▁sentence｜>`, `试一试`, ` fifty` (target ranks: base_value=91:81390, first_product=182:112362, bound_value=187:84220, second_product=374:72178, answer=385:24163)

### Filler position 4 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=91:123287, first_product=182:123146, bound_value=187:121968, second_product=374:121273, answer=385:124501)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=91:11824, first_product=182:24805, bound_value=187:22942, second_product=374:25266, answer=385:25312)
- Layer 20: `ait`, `cape`, `atile`, `胃癌`, ` immobil` (target ranks: base_value=91:10280, first_product=182:37059, bound_value=187:34226, second_product=374:29246, answer=385:41125)
- Layer 30: ` tap`, `Tap`, `acos`, ` Tap`, ` consum` (target ranks: base_value=91:74747, first_product=182:89542, bound_value=187:76116, second_product=374:46268, answer=385:105869)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, ` rip` (target ranks: base_value=91:36838, first_product=182:84402, bound_value=187:45642, second_product=374:33575, answer=385:81955)
- Layer 36: ` dynam`, ` tap`, `动态`, ` drip`, `期望` (target ranks: base_value=91:32470, first_product=182:74242, bound_value=187:38376, second_product=374:32006, answer=385:72702)
- Layer 37: `oug`, ` dynam`, ` Nim`, ` Zed`, `ERG` (target ranks: base_value=91:80599, first_product=182:88195, bound_value=187:83891, second_product=374:58216, answer=385:100235)
- Layer 38: `本题分析`, `zat`, `uze`, `oug`, `zos` (target ranks: base_value=91:102649, first_product=182:94817, bound_value=187:104838, second_product=374:76936, answer=385:105094)
- Layer 39: `oug`, `本题分析`, ` Nij`, ` talags`, ` Zed` (target ranks: base_value=91:118139, first_product=182:120278, bound_value=187:107848, second_product=374:76900, answer=385:100178)
- Layer 40: ` talags`, `oug`, ` Question`, `zij`, `zac` (target ranks: base_value=91:112167, first_product=182:120818, bound_value=187:97983, second_product=374:69649, answer=385:64272)
- Layer 41: ` Question`, `Question`, ` .`, `袄`, ` fum` (target ranks: base_value=91:70608, first_product=182:78030, bound_value=187:60259, second_product=374:20087, answer=385:19682)

### Filler position 5 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=91:122710, first_product=182:123202, bound_value=187:122151, second_product=374:121232, answer=385:124379)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=91:13499, first_product=182:28359, bound_value=187:25348, second_product=374:28577, answer=385:26668)
- Layer 20: `幽`, `鞍`, `锁定`, ` Tears`, `挪` (target ranks: base_value=91:18343, first_product=182:39632, bound_value=187:33286, second_product=374:30060, answer=385:28681)
- Layer 30: ` Miy`, ` MI`, `算出`, `推算`, `计算` (target ranks: base_value=91:30442, first_product=182:40581, bound_value=187:72062, second_product=374:48410, answer=385:65554)
- Layer 35: ` Tw`, ` Miy`, `推算`, `第一步`, ` first` (target ranks: base_value=91:24159, first_product=182:68062, bound_value=187:85473, second_product=374:42887, answer=385:54147)
- Layer 36: `推算`, `calcul`, ` Miy`, ` MI`, ` Tw` (target ranks: base_value=91:36217, first_product=182:69809, bound_value=187:78133, second_product=374:33460, answer=385:34639)
- Layer 37: ` MI`, ` Miy`, `calcul`, `MI`, `计算方法` (target ranks: base_value=91:73446, first_product=182:86107, bound_value=187:99903, second_product=374:43096, answer=385:42999)
- Layer 38: ` MI`, ` Mif`, ` Miy`, ` mir`, ` mim` (target ranks: base_value=91:94839, first_product=182:99745, bound_value=187:97805, second_product=374:49172, answer=385:38045)
- Layer 39: ` MI`, ` Mif`, `MI`, ` Mika`, `米尔` (target ranks: base_value=91:117750, first_product=182:124951, bound_value=187:111797, second_product=374:79115, answer=385:73842)
- Layer 40: `外壳`, `duc`, ` v`, ` mim`, ` duplicates` (target ranks: base_value=91:109400, first_product=182:121342, bound_value=187:94144, second_product=374:51115, answer=385:27904)
- Layer 41: ` .`, `鹉`, `地`, `acular`, `叮` (target ranks: base_value=91:81542, first_product=182:105364, bound_value=187:90245, second_product=374:36075, answer=385:20673)

### Filler position 6 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=91:122681, first_product=182:122768, bound_value=187:121809, second_product=374:120841, answer=385:123927)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:12295, first_product=182:26313, bound_value=187:24327, second_product=374:26073, answer=385:25335)
- Layer 20: ` unflagged`, `答案`, `暂无`, `替换`, ` corrected` (target ranks: base_value=91:70374, first_product=182:110660, bound_value=187:101770, second_product=374:56121, answer=385:59690)
- Layer 30: `Sequ`, `高明`, `acks`, `turn`, `code` (target ranks: base_value=91:7885, first_product=182:33541, bound_value=187:28865, second_product=374:44542, answer=385:69318)
- Layer 35: `acks`, ` Tw`, ` tw`, `高明`, `推算` (target ranks: base_value=91:2781, first_product=182:17490, bound_value=187:23275, second_product=374:17565, answer=385:41199)
- Layer 36: ` Tw`, `acks`, ` tw`, `高明`, `柿子` (target ranks: base_value=91:5006, first_product=182:36686, bound_value=187:35199, second_product=374:29738, answer=385:63005)
- Layer 37: ` Tw`, `acks`, `支`, `高明`, `刺激` (target ranks: base_value=91:12980, first_product=182:47663, bound_value=187:62841, second_product=374:41544, answer=385:69562)
- Layer 38: ` Tw`, `支`, ` tw`, ` TW`, `Tw` (target ranks: base_value=91:16361, first_product=182:44374, bound_value=187:54537, second_product=374:49638, answer=385:59658)
- Layer 39: ` Dominic`, `ophe`, `叶子`, `MMMMMMMM`, `把事情` (target ranks: base_value=91:117032, first_product=182:128195, bound_value=187:118750, second_product=374:121328, answer=385:119861)
- Layer 40: ` Tw`, ` TW`, `.tw`, ` tw`, ` nasod` (target ranks: base_value=91:102562, first_product=182:128224, bound_value=187:109883, second_product=374:117444, answer=385:118301)
- Layer 41: ` .`, `那两个`, ` Tw`, `婷婷`, ` Seventy` (target ranks: base_value=91:113770, first_product=182:127828, bound_value=187:118502, second_product=374:120674, answer=385:115792)

### Filler position 7 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=91:122526, first_product=182:122459, bound_value=187:121493, second_product=374:120592, answer=385:123703)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11732, first_product=182:25462, bound_value=187:23295, second_product=374:26484, answer=385:25334)
- Layer 20: `Ta`, `锁定`, ` smile`, `足`, ` Ta` (target ranks: base_value=91:3699, first_product=182:19771, bound_value=187:11025, second_product=374:7260, answer=385:8219)
- Layer 30: `算计`, `calcul`, `计算`, ` calcul`, `计算的` (target ranks: base_value=91:272, first_product=182:1268, bound_value=187:218, second_product=374:350, answer=385:146)
- Layer 35: `381`, `推算`, `保留`, ` labor`, `371` (target ranks: base_value=91:674, first_product=182:3285, bound_value=187:336, second_product=374:118, answer=385:27)
- Layer 36: `381`, `413`, `特`, `芝`, `推算` (target ranks: base_value=91:3318, first_product=182:15909, bound_value=187:947, second_product=374:105, answer=385:12)
- Layer 37: `381`, `385`, ` medief`, `371`, `393` (target ranks: base_value=91:8407, first_product=182:14885, bound_value=187:623, second_product=374:25, answer=385:2)
- Layer 38: ` Noruwega`, `}<?`, ` medief`, `393`, ` pakig` (target ranks: base_value=91:27224, first_product=182:62830, bound_value=187:1735, second_product=374:103, answer=385:7)
- Layer 39: ` spectator`, ` Noruwega`, `书馆`, `osus`, `树叶` (target ranks: base_value=91:127026, first_product=182:128736, bound_value=187:78193, second_product=374:38395, answer=385:1696)
- Layer 40: ` talags`, `留存`, ` spectator`, ` pakig`, `袄` (target ranks: base_value=91:128138, first_product=182:128740, bound_value=187:99351, second_product=374:44165, answer=385:494)
- Layer 41: ` .`, `袄`, `试一试`, `留存`, `秆` (target ranks: base_value=91:124869, first_product=182:128454, bound_value=187:92112, second_product=374:43678, answer=385:713)

### Filler position 8 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:122720, first_product=182:122269, bound_value=187:121328, second_product=374:120333, answer=385:123546)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: base_value=91:10738, first_product=182:24415, bound_value=187:22880, second_product=374:25660, answer=385:24684)
- Layer 20: `锁定`, `鞍`, `幽`, `足`, `ait` (target ranks: base_value=91:14298, first_product=182:44694, bound_value=187:23766, second_product=374:27988, answer=385:23149)
- Layer 30: `鞍`, `输出的`, ` repetitions`, ` repetition`, `反复` (target ranks: base_value=91:45485, first_product=182:28700, bound_value=187:7109, second_product=374:13009, answer=385:13727)
- Layer 35: `鞍`, `输出的`, ` repetition`, `反复`, ` tap` (target ranks: base_value=91:25376, first_product=182:20032, bound_value=187:4290, second_product=374:4132, answer=385:6276)
- Layer 36: `输出的`, `反复`, `鞍`, `输出`, `acin` (target ranks: base_value=91:35529, first_product=182:37058, bound_value=187:4481, second_product=374:4018, answer=385:3907)
- Layer 37: `输出的`, `响应`, `输出`, ` immediate`, `acin` (target ranks: base_value=91:77619, first_product=182:33791, bound_value=187:8944, second_product=374:5668, answer=385:2751)
- Layer 38: `响应`, `输出`, `}<?`, `冰冰`, `下沉` (target ranks: base_value=91:86944, first_product=182:39136, bound_value=187:12636, second_product=374:11718, answer=385:3230)
- Layer 39: `}<?`, `ocyst`, `打磨`, `响应`, ` talags` (target ranks: base_value=91:120505, first_product=182:125099, bound_value=187:63708, second_product=374:74687, answer=385:27379)
- Layer 40: ` .`, `šk`, `响应`, `留存`, `下沉` (target ranks: base_value=91:107827, first_product=182:121842, bound_value=187:32956, second_product=374:54801, answer=385:6624)
- Layer 41: ` .`, `šk`, ` `, `叮`, `<｜end▁of▁sentence｜>` (target ranks: base_value=91:82272, first_product=182:114198, bound_value=187:46599, second_product=374:24335, answer=385:2601)

### Filler position 9 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:122908, first_product=182:122615, bound_value=187:121781, second_product=374:120679, answer=385:123878)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=91:10325, first_product=182:23860, bound_value=187:22021, second_product=374:25303, answer=385:24290)
- Layer 20: `ait`, `锁定`, ` Walker`, `幽`, `挪` (target ranks: base_value=91:7863, first_product=182:36538, bound_value=187:26217, second_product=374:24258, answer=385:22311)
- Layer 30: ` Miy`, ` mi`, ` MI`, `推算`, `算出` (target ranks: base_value=91:22233, first_product=182:78406, bound_value=187:61060, second_product=374:84241, answer=385:62892)
- Layer 35: ` Miy`, ` mi`, ` labor`, ` tap`, `Tap` (target ranks: base_value=91:17730, first_product=182:80360, bound_value=187:70483, second_product=374:69522, answer=385:54325)
- Layer 36: ` Miy`, ` mi`, `mi`, ` MI`, ` mir` (target ranks: base_value=91:17968, first_product=182:80234, bound_value=187:56474, second_product=374:61117, answer=385:38395)
- Layer 37: ` Miy`, ` MI`, ` mi`, `mi`, ` mir` (target ranks: base_value=91:39753, first_product=182:85997, bound_value=187:73964, second_product=374:69005, answer=385:33362)
- Layer 38: ` Miy`, ` MI`, ` mir`, ` mi`, `mi` (target ranks: base_value=91:66940, first_product=182:98879, bound_value=187:88256, second_product=374:85583, answer=385:40403)
- Layer 39: ` MI`, ` Miy`, ` mi`, `mi`, ` mir` (target ranks: base_value=91:95175, first_product=182:113783, bound_value=187:91427, second_product=374:72557, answer=385:44136)
- Layer 40: `留存`, `殿堂`, `金黄`, `scr`, `y` (target ranks: base_value=91:68592, first_product=182:104880, bound_value=187:59845, second_product=374:43260, answer=385:9030)
- Layer 41: `鹉`, ` .`, ` `, `漏`, `试一试` (target ranks: base_value=91:25875, first_product=182:60215, bound_value=187:35026, second_product=374:13470, answer=385:5467)

### Filler position 10 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:123019, first_product=182:122597, bound_value=187:121795, second_product=374:120605, answer=385:123755)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11046, first_product=182:24124, bound_value=187:22385, second_product=374:26582, answer=385:24975)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=91:13520, first_product=182:38719, bound_value=187:27847, second_product=374:31170, answer=385:29147)
- Layer 30: `vn`, `输入的`, `vf`, ` vot`, ` v` (target ranks: base_value=91:7128, first_product=182:95566, bound_value=187:52248, second_product=374:64991, answer=385:54788)
- Layer 35: ` vot`, ` v`, `v`, ` tap`, `Tap` (target ranks: base_value=91:1741, first_product=182:68957, bound_value=187:35380, second_product=374:32525, answer=385:33477)
- Layer 36: `adal`, ` dri`, `留存`, ` tap`, `年开始` (target ranks: base_value=91:2336, first_product=182:75765, bound_value=187:31926, second_product=374:31018, answer=385:24592)
- Layer 37: `}<?`, ` Mif`, ` rif`, `oof`, ` bif` (target ranks: base_value=91:7091, first_product=182:94878, bound_value=187:52104, second_product=374:45810, answer=385:28556)
- Layer 38: `}<?`, ` Mif`, `zuf`, `zat`, ` VIP` (target ranks: base_value=91:20958, first_product=182:110320, bound_value=187:69906, second_product=374:73983, answer=385:36472)
- Layer 39: ` v`, `}<?`, ` vip`, `v`, ` Mif` (target ranks: base_value=91:93278, first_product=182:124827, bound_value=187:94533, second_product=374:91945, answer=385:76465)
- Layer 40: ` v`, `v`, `殿堂`, ` mim`, ` vip` (target ranks: base_value=91:76611, first_product=182:120111, bound_value=187:70632, second_product=374:80762, answer=385:32466)
- Layer 41: `鹉`, ` .`, `acular`, ` mim`, `实在` (target ranks: base_value=91:49495, first_product=182:96861, bound_value=187:33710, second_product=374:30741, answer=385:15282)

### Filler position 11 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:123350, first_product=182:123038, bound_value=187:122331, second_product=374:121084, answer=385:124245)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=91:11324, first_product=182:25100, bound_value=187:23226, second_product=374:27088, answer=385:25345)
- Layer 20: ` Walker`, `锁定`, `Walker`, `ait`, ` smile` (target ranks: base_value=91:16811, first_product=182:41870, bound_value=187:28491, second_product=374:33075, answer=385:30177)
- Layer 30: ` tap`, `yak`, ` dy`, `Tap`, ` Tap` (target ranks: base_value=91:86346, first_product=182:103098, bound_value=187:65755, second_product=374:66276, answer=385:68871)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, `羊` (target ranks: base_value=91:38148, first_product=182:76016, bound_value=187:46245, second_product=374:31422, answer=385:33999)
- Layer 36: ` tap`, ` Tap`, `Tap`, `adal`, `留存` (target ranks: base_value=91:52707, first_product=182:88837, bound_value=187:44339, second_product=374:24585, answer=385:21282)
- Layer 37: `}<?`, `ота`, ` Zad`, ` tap`, `不急` (target ranks: base_value=91:100082, first_product=182:100109, bound_value=187:72893, second_product=374:34401, answer=385:21776)
- Layer 38: `}<?`, `zat`, `pac`, `ота`, `覆` (target ranks: base_value=91:98352, first_product=182:113094, bound_value=187:91235, second_product=374:68365, answer=385:30571)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `东海`, `ocyst`, `zat` (target ranks: base_value=91:118838, first_product=182:126271, bound_value=187:108239, second_product=374:103339, answer=385:79657)
- Layer 40: ` y`, `y`, `殿堂`, `语言文字`, `留存` (target ranks: base_value=91:100523, first_product=182:121698, bound_value=187:85829, second_product=374:83521, answer=385:43585)
- Layer 41: `鹉`, ` .`, `<｜end▁of▁sentence｜>`, ` `, `留存` (target ranks: base_value=91:46952, first_product=182:104299, bound_value=187:75281, second_product=374:40992, answer=385:21847)

### Filler position 12 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:123568, first_product=182:123155, bound_value=187:122454, second_product=374:121182, answer=385:124353)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10937, first_product=182:24453, bound_value=187:22762, second_product=374:26407, answer=385:25003)
- Layer 20: `ait`, `锁定`, `挪`, ` smile`, ` Walker` (target ranks: base_value=91:7566, first_product=182:27290, bound_value=187:19655, second_product=374:23775, answer=385:24655)
- Layer 30: `Tap`, ` tap`, `tap`, ` Tap`, `Rational` (target ranks: base_value=91:11326, first_product=182:35409, bound_value=187:13147, second_product=374:14435, answer=385:30496)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, `Task` (target ranks: base_value=91:11443, first_product=182:67144, bound_value=187:19268, second_product=374:16280, answer=385:36786)
- Layer 36: ` tap`, `Tap`, ` Tap`, ` Zad`, ` zad` (target ranks: base_value=91:17906, first_product=182:72603, bound_value=187:20866, second_product=374:18698, answer=385:40214)
- Layer 37: ` Zad`, `冰冰`, ` tap`, ` zad`, `支` (target ranks: base_value=91:40563, first_product=182:78939, bound_value=187:42577, second_product=374:33236, answer=385:44161)
- Layer 38: ` Zad`, `冰冰`, `ocyst`, `�`, `�` (target ranks: base_value=91:64540, first_product=182:87790, bound_value=187:67772, second_product=374:54729, answer=385:41091)
- Layer 39: `ocyst`, `}<?`, `hemer`, `�`, `ozygous` (target ranks: base_value=91:96266, first_product=182:124894, bound_value=187:81962, second_product=374:82643, answer=385:62707)
- Layer 40: ` mim`, ` seventy`, ` fifty`, ` Seventy`, `试一试` (target ranks: base_value=91:66772, first_product=182:116283, bound_value=187:39964, second_product=374:53373, answer=385:34846)
- Layer 41: `鹉`, ` .`, `试一试`, ` seventy`, ` mim` (target ranks: base_value=91:20028, first_product=182:79450, bound_value=187:25587, second_product=374:11457, answer=385:6026)

### Filler position 13 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:123476, first_product=182:123132, bound_value=187:122401, second_product=374:121203, answer=385:124241)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11057, first_product=182:24431, bound_value=187:22821, second_product=374:26331, answer=385:25074)
- Layer 20: `ait`, `锁定`, ` Walker`, ` smile`, `忑` (target ranks: base_value=91:9771, first_product=182:34710, bound_value=187:22472, second_product=374:24836, answer=385:24224)
- Layer 30: `冰川`, `393`, ` Mim`, ` glacier`, ` pakig` (target ranks: base_value=91:2834, first_product=182:13570, bound_value=187:279, second_product=374:186, answer=385:100)
- Layer 35: `389`, `387`, `383`, `388`, `385` (target ranks: base_value=91:14517, first_product=182:103008, bound_value=187:1982, second_product=374:27, answer=385:5)
- Layer 36: `385`, `389`, `387`, `383`, `388` (target ranks: base_value=91:31481, first_product=182:103768, bound_value=187:618, second_product=374:30, answer=385:1)
- Layer 37: `385`, `387`, `389`, `383`, `395` (target ranks: base_value=91:72356, first_product=182:95748, bound_value=187:1283, second_product=374:41, answer=385:1)
- Layer 38: `389`, `385`, `395`, `387`, `393` (target ranks: base_value=91:112791, first_product=182:124396, bound_value=187:18553, second_product=374:473, answer=385:2)
- Layer 39: `389`, `395`, `385`, `399`, `393` (target ranks: base_value=91:124039, first_product=182:127911, bound_value=187:88685, second_product=374:20464, answer=385:3)
- Layer 40: `389`, `385`, `399`, `383`, `393` (target ranks: base_value=91:126009, first_product=182:128194, bound_value=187:98090, second_product=374:14281, answer=385:2)
- Layer 41: `385`, `383`, ` .`, `399`, `389` (target ranks: base_value=91:94496, first_product=182:118847, bound_value=187:83438, second_product=374:8456, answer=385:1)

### Filler position 14 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:123724, first_product=182:122996, bound_value=187:122356, second_product=374:121075, answer=385:124148)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11132, first_product=182:23666, bound_value=187:22116, second_product=374:25551, answer=385:24490)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `能被` (target ranks: base_value=91:19631, first_product=182:48187, bound_value=187:28676, second_product=374:38700, answer=385:37136)
- Layer 30: ` Miy`, `yi`, `yg`, `sl`, `锁定` (target ranks: base_value=91:51879, first_product=182:80719, bound_value=187:34262, second_product=374:48214, answer=385:46441)
- Layer 35: `锁定`, ` reserved`, ` yak`, ` Tap`, ` tap` (target ranks: base_value=91:30490, first_product=182:58656, bound_value=187:27374, second_product=374:33925, answer=385:31935)
- Layer 36: ` Ta`, `反复`, ` tap`, `留存`, ` Tap` (target ranks: base_value=91:20155, first_product=182:53997, bound_value=187:16035, second_product=374:20731, answer=385:17741)
- Layer 37: `}<?`, `班的`, `不急`, `班`, `滴` (target ranks: base_value=91:65225, first_product=182:62500, bound_value=187:35046, second_product=374:34363, answer=385:16719)
- Layer 38: `}<?`, `不急`, ` nasod`, `班的`, `ِّف` (target ranks: base_value=91:62643, first_product=182:74296, bound_value=187:51515, second_product=374:63250, answer=385:18939)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `打磨`, `ِّف`, `�乐` (target ranks: base_value=91:101938, first_product=182:117002, bound_value=187:79660, second_product=374:92237, answer=385:49279)
- Layer 40: ` nasod`, `<｜begin▁of▁sentence｜>`, ` .`, `留存`, `enclose` (target ranks: base_value=91:76875, first_product=182:101257, bound_value=187:35388, second_product=374:72620, answer=385:28102)
- Layer 41: ` .`, ` .↵↵`, ` `, ` :`, ` .↵` (target ranks: base_value=91:52974, first_product=182:78425, bound_value=187:19975, second_product=374:39483, answer=385:10595)

### Filler position 15 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:124099, first_product=182:123440, bound_value=187:122800, second_product=374:121503, answer=385:124623)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:9997, first_product=182:22146, bound_value=187:20930, second_product=374:24294, answer=385:23269)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, `距` (target ranks: base_value=91:8987, first_product=182:29976, bound_value=187:23648, second_product=374:23037, answer=385:21905)
- Layer 30: `<｜end▁of▁file▁name｜>`, `平行`, `acos`, ` appendix`, `ragma` (target ranks: base_value=91:1129, first_product=182:2902, bound_value=187:402, second_product=374:255, answer=385:134)
- Layer 35: `79`, `774`, `390`, `382`, `792` (target ranks: base_value=91:8745, first_product=182:81190, bound_value=187:26203, second_product=374:37, answer=385:18)
- Layer 36: `792`, `795`, `790`, `79`, `796` (target ranks: base_value=91:8886, first_product=182:71468, bound_value=187:23795, second_product=374:109, answer=385:82)
- Layer 37: `792`, `790`, `794`, `796`, `795` (target ranks: base_value=91:33750, first_product=182:87007, bound_value=187:70278, second_product=374:547, answer=385:276)
- Layer 38: `795`, `790`, `799`, `792`, `796` (target ranks: base_value=91:37856, first_product=182:105086, bound_value=187:82156, second_product=374:3238, answer=385:190)
- Layer 39: `书馆`, `�`, ` Nij`, ` Tub`, `打磨` (target ranks: base_value=91:48241, first_product=182:112465, bound_value=187:89359, second_product=374:112335, answer=385:27064)
- Layer 40: `留存`, `acl`, ` Nij`, ` twist`, ` view` (target ranks: base_value=91:23924, first_product=182:81701, bound_value=187:30738, second_product=374:94884, answer=385:36017)
- Layer 41: ` .`, ` twist`, `那两个`, `那个`, `看看吧` (target ranks: base_value=91:25917, first_product=182:70767, bound_value=187:71221, second_product=374:98994, answer=385:54639)

### Filler position 16 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:124323, first_product=182:123518, bound_value=187:122910, second_product=374:121577, answer=385:124589)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11024, first_product=182:23823, bound_value=187:21957, second_product=374:25210, answer=385:24290)
- Layer 20: `ait`, `锁定`, ` Walker`, `而此时`, ` smile` (target ranks: base_value=91:10711, first_product=182:30447, bound_value=187:25083, second_product=374:26449, answer=385:28863)
- Layer 30: ` Miy`, `acin`, `算出`, `计算的`, ` calculate` (target ranks: base_value=91:30356, first_product=182:26821, bound_value=187:36462, second_product=374:44718, answer=385:48061)
- Layer 35: `分解`, ` Miy`, `羊`, ` Tw`, ` met` (target ranks: base_value=91:21050, first_product=182:25404, bound_value=187:43632, second_product=374:38213, answer=385:33275)
- Layer 36: `分解`, ` Miy`, `羊`, `acin`, `留存` (target ranks: base_value=91:20139, first_product=182:15512, bound_value=187:20938, second_product=374:16604, answer=385:15144)
- Layer 37: `radesh`, ` mir`, `acin`, ` Miy`, `acos` (target ranks: base_value=91:50930, first_product=182:17068, bound_value=187:37670, second_product=374:21493, answer=385:15709)
- Layer 38: ` mir`, ` Mir`, ` polar`, `acos`, `otomy` (target ranks: base_value=91:54798, first_product=182:28526, bound_value=187:42644, second_product=374:23258, answer=385:14409)
- Layer 39: `<｜begin▁of▁sentence｜>`, `romic`, ` Mir`, ` mir`, `otomy` (target ranks: base_value=91:77018, first_product=182:99482, bound_value=187:80104, second_product=374:67453, answer=385:37415)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` duplicates`, `留存`, `俯`, ` duplicated` (target ranks: base_value=91:40621, first_product=182:72060, bound_value=187:33160, second_product=374:45852, answer=385:15994)
- Layer 41: ` .`, `鹉`, ` `, `等待`, `<｜end▁of▁sentence｜>` (target ranks: base_value=91:22736, first_product=182:66640, bound_value=187:39919, second_product=374:27983, answer=385:19653)

### Filler position 17 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:124601, first_product=182:123769, bound_value=187:123159, second_product=374:121838, answer=385:124790)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11848, first_product=182:24783, bound_value=187:22392, second_product=374:26383, answer=385:24575)
- Layer 20: `锁定`, ` smile`, `ait`, `距`, `而此时` (target ranks: base_value=91:10937, first_product=182:25630, bound_value=187:14868, second_product=374:22205, answer=385:18471)
- Layer 30: ` Tw`, `Tw`, `tw`, `锁定`, `Tap` (target ranks: base_value=91:23076, first_product=182:15481, bound_value=187:8036, second_product=374:24215, answer=385:19136)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=91:21122, first_product=182:21747, bound_value=187:11826, second_product=374:20716, answer=385:15869)
- Layer 36: ` Tw`, `Tw`, `.tw`, `tw`, `反复` (target ranks: base_value=91:27680, first_product=182:23046, bound_value=187:6923, second_product=374:11758, answer=385:8303)
- Layer 37: ` Tw`, `radesh`, `Tw`, `.tw`, ` doubling` (target ranks: base_value=91:69095, first_product=182:36319, bound_value=187:16889, second_product=374:21572, answer=385:11759)
- Layer 38: ` Tw`, `.tw`, `Tw`, ` doubling`, `radesh` (target ranks: base_value=91:99067, first_product=182:63822, bound_value=187:38893, second_product=374:43930, answer=385:28322)
- Layer 39: ` Tw`, `}<?`, `<｜begin▁of▁sentence｜>`, `覆`, `radesh` (target ranks: base_value=91:110625, first_product=182:114781, bound_value=187:76817, second_product=374:85543, answer=385:45837)
- Layer 40: `radesh`, `<｜begin▁of▁sentence｜>`, `坏`, `坏的`, `语言文字` (target ranks: base_value=91:81629, first_product=182:108956, bound_value=187:44998, second_product=374:73841, answer=385:29595)
- Layer 41: `鹉`, ` .`, `每次`, `本`, ` ` (target ranks: base_value=91:61813, first_product=182:82061, bound_value=187:40246, second_product=374:36747, answer=385:25387)

### Filler position 18 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=91:124776, first_product=182:124175, bound_value=187:123621, second_product=374:122250, answer=385:125124)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11693, first_product=182:24506, bound_value=187:22525, second_product=374:27340, answer=385:25192)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, ` smile` (target ranks: base_value=91:16243, first_product=182:33168, bound_value=187:24992, second_product=374:31774, answer=385:34624)
- Layer 30: `算出`, `calcul`, ` calculator`, `计算的`, ` calculate` (target ranks: base_value=91:17613, first_product=182:30183, bound_value=187:21210, second_product=374:27139, answer=385:30217)
- Layer 35: `calcul`, ` calculator`, `计算的`, ` calculate`, `calculator` (target ranks: base_value=91:14282, first_product=182:35227, bound_value=187:20714, second_product=374:30858, answer=385:27688)
- Layer 36: `calcul`, `计算的`, ` calculator`, `分解`, ` calculations` (target ranks: base_value=91:15218, first_product=182:18876, bound_value=187:8839, second_product=374:18641, answer=385:10497)
- Layer 37: `calcul`, `计算的`, ` Calculators`, ` calculations`, `计算` (target ranks: base_value=91:61035, first_product=182:27776, bound_value=187:22264, second_product=374:32921, answer=385:17181)
- Layer 38: `calcul`, `计算的`, ` Calculators`, `-step`, `comput` (target ranks: base_value=91:79306, first_product=182:64613, bound_value=187:51880, second_product=374:49261, answer=385:18588)
- Layer 39: `殿堂`, ` Tra`, ` rese`, `zat`, ` paso` (target ranks: base_value=91:51161, first_product=182:75614, bound_value=187:37225, second_product=374:40465, answer=385:12376)
- Layer 40: `殿堂`, ` mir`, `acl`, `zat`, `sequ` (target ranks: base_value=91:34825, first_product=182:36939, bound_value=187:8266, second_product=374:30233, answer=385:5865)
- Layer 41: `zl`, `zij`, ` .`, ` `, `又是` (target ranks: base_value=91:15508, first_product=182:15512, bound_value=187:9721, second_product=374:19337, answer=385:3606)

### Filler position 19 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:125139, first_product=182:124383, bound_value=187:123860, second_product=374:122498, answer=385:125260)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10869, first_product=182:23937, bound_value=187:21997, second_product=374:26052, answer=385:24372)
- Layer 20: `ait`, `忑`, `锁定`, ` Walker`, `Walker` (target ranks: base_value=91:14891, first_product=182:34228, bound_value=187:23541, second_product=374:31326, answer=385:31310)
- Layer 30: ` repetition`, ` calculator`, ` zad`, ` sequential`, ` Aufgabe` (target ranks: base_value=91:29674, first_product=182:46141, bound_value=187:10585, second_product=374:37135, answer=385:19697)
- Layer 35: ` var`, ` calculator`, ` repetition`, ` zad`, ` labor` (target ranks: base_value=91:22563, first_product=182:57948, bound_value=187:17977, second_product=374:26375, answer=385:19082)
- Layer 36: ` var`, ` zad`, ` calculator`, ` Aufgabe`, `柿子` (target ranks: base_value=91:24308, first_product=182:67503, bound_value=187:17898, second_product=374:19322, answer=385:13739)
- Layer 37: ` Zad`, ` zad`, ` Aufgabe`, `calcul`, `冰冰` (target ranks: base_value=91:69729, first_product=182:96378, bound_value=187:46276, second_product=374:37252, answer=385:19217)
- Layer 38: ` Zad`, `}<?`, `冰冰`, ` zad`, `calcul` (target ranks: base_value=91:83034, first_product=182:101427, bound_value=187:77941, second_product=374:58116, answer=385:18952)
- Layer 39: `}<?`, `acons`, `下沉`, `打磨`, `ocyst` (target ranks: base_value=91:106071, first_product=182:120198, bound_value=187:73224, second_product=374:95691, answer=385:43285)
- Layer 40: `下沉`, `acl`, ` consum`, `冰冰`, `殿堂` (target ranks: base_value=91:78960, first_product=182:105535, bound_value=187:58514, second_product=374:86606, answer=385:25629)
- Layer 41: ` .`, ` mim`, ` `, ` until`, `冰冰` (target ranks: base_value=91:37527, first_product=182:73866, bound_value=187:47066, second_product=374:55498, answer=385:8058)

### Filler position 20 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:125205, first_product=182:124557, bound_value=187:124021, second_product=374:122680, answer=385:125478)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10415, first_product=182:22906, bound_value=187:21319, second_product=374:24499, answer=385:23348)
- Layer 20: `ait`, `锁定`, ` Walker`, `忑`, `Walker` (target ranks: base_value=91:12906, first_product=182:35540, bound_value=187:22790, second_product=374:33035, answer=385:30611)
- Layer 30: ` calculator`, `calculator`, `calcul`, `退出`, `计算的` (target ranks: base_value=91:2680, first_product=182:11090, bound_value=187:620, second_product=374:1660, answer=385:850)
- Layer 35: ` calculator`, `锁定`, `退出`, ` labor`, `保留` (target ranks: base_value=91:4498, first_product=182:42532, bound_value=187:1297, second_product=374:801, answer=385:86)
- Layer 36: `退出`, `381`, `calcul`, `389`, `留存` (target ranks: base_value=91:8242, first_product=182:45143, bound_value=187:606, second_product=374:393, answer=385:21)
- Layer 37: `381`, `387`, `393`, `389`, `}<?` (target ranks: base_value=91:33544, first_product=182:47714, bound_value=187:828, second_product=374:71, answer=385:8)
- Layer 38: `}<?`, `381`, ` spectator`, `馆长`, `覆` (target ranks: base_value=91:51714, first_product=182:70531, bound_value=187:3434, second_product=374:702, answer=385:11)
- Layer 39: `}<?`, `urin`, `ocyst`, `?datasetId`, ` spectator` (target ranks: base_value=91:115837, first_product=182:125955, bound_value=187:25306, second_product=374:14591, answer=385:25)
- Layer 40: `acl`, `留存`, `下沉`, `冰冰`, `heres` (target ranks: base_value=91:119577, first_product=182:126117, bound_value=187:33897, second_product=374:10051, answer=385:8)
- Layer 41: `393`, `矶`, ` `, `冰冰`, ` .` (target ranks: base_value=91:81794, first_product=182:108732, bound_value=187:21349, second_product=374:5075, answer=385:7)

### Filler position 21 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:125399, first_product=182:124659, bound_value=187:124167, second_product=374:122718, answer=385:125509)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10254, first_product=182:22800, bound_value=187:21478, second_product=374:24473, answer=385:23107)
- Layer 20: `ait`, `锁定`, `能被`, `距`, ` Walker` (target ranks: base_value=91:12169, first_product=182:29210, bound_value=187:20031, second_product=374:22221, answer=385:16087)
- Layer 30: ` pakig`, `}<?`, `187`, `平行`, ` tournament` (target ranks: base_value=91:3132, first_product=182:231, bound_value=187:3, second_product=374:891, answer=385:361)
- Layer 35: `374`, `187`, `372`, `375`, `373` (target ranks: base_value=91:92390, first_product=182:64697, bound_value=187:2, second_product=374:1, answer=385:260)
- Layer 36: `374`, `187`, `375`, `376`, `372` (target ranks: base_value=91:113249, first_product=182:86323, bound_value=187:2, second_product=374:1, answer=385:993)
- Layer 37: `374`, `187`, `375`, `}<?`, `?datasetId` (target ranks: base_value=91:121441, first_product=182:71157, bound_value=187:2, second_product=374:1, answer=385:1900)
- Layer 38: `374`, `187`, `375`, `376`, `372` (target ranks: base_value=91:124602, first_product=182:81908, bound_value=187:2, second_product=374:1, answer=385:1294)
- Layer 39: `374`, `187`, `375`, `}<?`, ` hemorrhage` (target ranks: base_value=91:127472, first_product=182:116336, bound_value=187:2, second_product=374:1, answer=385:6857)
- Layer 40: `374`, `375`, `373`, `376`, `372` (target ranks: base_value=91:128026, first_product=182:122710, bound_value=187:12, second_product=374:1, answer=385:150)
- Layer 41: `374`, `375`, `376`, `omorphism`, `omit` (target ranks: base_value=91:120911, first_product=182:104182, bound_value=187:34, second_product=374:1, answer=385:1070)

### Filler position 22 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:125529, first_product=182:124809, bound_value=187:124346, second_product=374:122946, answer=385:125718)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10489, first_product=182:22414, bound_value=187:21545, second_product=374:24943, answer=385:23384)
- Layer 20: `ait`, `锁定`, `距`, ` Walker`, ` smile` (target ranks: base_value=91:11330, first_product=182:26699, bound_value=187:22345, second_product=374:20885, answer=385:21272)
- Layer 30: `acos`, `acic`, `平行`, `adal`, `泳` (target ranks: base_value=91:2660, first_product=182:3804, bound_value=187:2072, second_product=374:1758, answer=385:660)
- Layer 35: `388`, `389`, `itetsdata`, `分解`, `390` (target ranks: base_value=91:46556, first_product=182:88211, bound_value=187:12989, second_product=374:3146, answer=385:35)
- Layer 36: `389`, ` Hoff`, `388`, ` decomposed`, ` Hof` (target ranks: base_value=91:59919, first_product=182:102730, bound_value=187:8522, second_product=374:1917, answer=385:26)
- Layer 37: `轨迹`, `389`, `388`, `馆长`, ` Hoff` (target ranks: base_value=91:103130, first_product=182:95764, bound_value=187:10961, second_product=374:1682, answer=385:50)
- Layer 38: `389`, `馆长`, ` Hoff`, `399`, `393` (target ranks: base_value=91:110798, first_product=182:120429, bound_value=187:42515, second_product=374:8105, answer=385:138)
- Layer 39: `书馆`, `399`, `}<?`, `389`, `馆长` (target ranks: base_value=91:126878, first_product=182:125314, bound_value=187:87185, second_product=374:12431, answer=385:218)
- Layer 40: `389`, `399`, `393`, ` expectation`, ` Hoff` (target ranks: base_value=91:124498, first_product=182:119064, bound_value=187:40471, second_product=374:859, answer=385:15)
- Layer 41: `399`, `389`, ` expectation`, `393`, `的出现` (target ranks: base_value=91:85351, first_product=182:74475, bound_value=187:33766, second_product=374:374, answer=385:10)

### Filler position 23 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:126057, first_product=182:125493, bound_value=187:125099, second_product=374:123593, answer=385:126488)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=91:11368, first_product=182:23498, bound_value=187:22127, second_product=374:25293, answer=385:24096)
- Layer 20: ` smile`, `足`, ` LS`, `ait`, `锁定` (target ranks: base_value=91:11793, first_product=182:29842, bound_value=187:23423, second_product=374:24323, answer=385:20944)
- Layer 30: ` twice`, ` Tw`, ` repeated`, `Tw`, ` repetition` (target ranks: base_value=91:298, first_product=182:3413, bound_value=187:5225, second_product=374:15501, answer=385:12132)
- Layer 35: ` repeated`, ` Tw`, ` repetition`, `重复`, `Tw` (target ranks: base_value=91:49, first_product=182:1360, bound_value=187:2695, second_product=374:9780, answer=385:4100)
- Layer 36: ` repeated`, ` Tw`, `反复`, `重复`, `分解` (target ranks: base_value=91:185, first_product=182:1741, bound_value=187:2213, second_product=374:11866, answer=385:3974)
- Layer 37: `}<?`, `radesh`, ` doubling`, `翻`, `calcul` (target ranks: base_value=91:396, first_product=182:847, bound_value=187:2522, second_product=374:16545, answer=385:8973)
- Layer 38: `}<?`, `radesh`, `zat`, ` doubling`, `副院长` (target ranks: base_value=91:8017, first_product=182:16495, bound_value=187:21858, second_product=374:75528, answer=385:26553)
- Layer 39: `}<?`, `uerak`, `覆`, `uffman`, `radesh` (target ranks: base_value=91:71510, first_product=182:88610, bound_value=187:62320, second_product=374:109044, answer=385:82550)
- Layer 40: `duc`, `radesh`, `坏`, ` Tw`, `ekak` (target ranks: base_value=91:73287, first_product=182:100209, bound_value=187:6987, second_product=374:88845, answer=385:59813)
- Layer 41: ` .`, `鹉`, ` `, ` mim`, `外层` (target ranks: base_value=91:47474, first_product=182:87651, bound_value=187:11316, second_product=374:51604, answer=385:50047)

### Filler position 24 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=91:126062, first_product=182:125510, bound_value=187:125173, second_product=374:123687, answer=385:126448)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=91:10849, first_product=182:22881, bound_value=187:21397, second_product=374:24472, answer=385:24076)
- Layer 20: ` smile`, `ait`, `锁定`, ` LS`, `足` (target ranks: base_value=91:10009, first_product=182:24697, bound_value=187:18981, second_product=374:27005, answer=385:29566)
- Layer 30: ` ignored`, `忽略`, ` y`, ` dy`, ` ignore` (target ranks: base_value=91:14488, first_product=182:58861, bound_value=187:26770, second_product=374:31645, answer=385:59932)
- Layer 35: ` y`, ` Y`, `Y`, `yg`, `YG` (target ranks: base_value=91:12277, first_product=182:66901, bound_value=187:38572, second_product=374:26191, answer=385:61115)
- Layer 36: `不急`, `Y`, `yg`, ` y`, ` Y` (target ranks: base_value=91:11133, first_product=182:52158, bound_value=187:35727, second_product=374:16926, answer=385:37505)
- Layer 37: `不急`, `}<?`, `y`, `acy`, ` y` (target ranks: base_value=91:51413, first_product=182:81492, bound_value=187:87707, second_product=374:37710, answer=385:59925)
- Layer 38: `不急`, `}<?`, `y`, `acy`, `yv` (target ranks: base_value=91:34875, first_product=182:99935, bound_value=187:93062, second_product=374:58866, answer=385:60972)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `yv`, `叶子`, `不急` (target ranks: base_value=91:75175, first_product=182:116640, bound_value=187:83946, second_product=374:94309, answer=385:83492)
- Layer 40: `y`, ` y`, `不急`, ` Tw`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=91:39968, first_product=182:100251, bound_value=187:40569, second_product=374:81141, answer=385:47422)
- Layer 41: ` .`, `y`, ` `, ` y`, ` twist` (target ranks: base_value=91:14419, first_product=182:66774, bound_value=187:33717, second_product=374:39400, answer=385:27407)

### Filler position 25 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=91:126214, first_product=182:125578, bound_value=187:125279, second_product=374:123729, answer=385:126562)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11288, first_product=182:23612, bound_value=187:21946, second_product=374:24854, answer=385:24967)
- Layer 20: ` smile`, `锁定`, `ait`, `距`, `足` (target ranks: base_value=91:6560, first_product=182:11430, bound_value=187:8726, second_product=374:13660, answer=385:13994)
- Layer 30: ` calculator`, `望`, `187`, ` labor`, `79` (target ranks: base_value=91:1018, first_product=182:373, bound_value=187:3, second_product=374:394, answer=385:655)
- Layer 35: ` labor`, ` smile`, ` Heim`, `389`, `锁定` (target ranks: base_value=91:7227, first_product=182:33429, bound_value=187:312, second_product=374:759, answer=385:119)
- Layer 36: `389`, `393`, `391`, `403`, `409` (target ranks: base_value=91:16857, first_product=182:33672, bound_value=187:224, second_product=374:396, answer=385:64)
- Layer 37: `389`, `393`, `387`, `403`, `391` (target ranks: base_value=91:54611, first_product=182:43353, bound_value=187:368, second_product=374:144, answer=385:31)
- Layer 38: `}<?`, ` Noruwega`, `403`, `393`, `殿堂` (target ranks: base_value=91:77497, first_product=182:74328, bound_value=187:2225, second_product=374:1065, answer=385:45)
- Layer 39: ` Noruwega`, `}<?`, `393`, `宫内`, `叶子` (target ranks: base_value=91:123641, first_product=182:118900, bound_value=187:16585, second_product=374:4319, answer=385:41)
- Layer 40: `393`, ` dich`, `acl`, `389`, ` talags` (target ranks: base_value=91:127337, first_product=182:114498, bound_value=187:17836, second_product=374:1092, answer=385:27)
- Layer 41: `393`, `因为这些`, ` waterfall`, `))))`, ` ` (target ranks: base_value=91:108230, first_product=182:78398, bound_value=187:17136, second_product=374:715, answer=385:29)

### Filler position 26 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:126209, first_product=182:125581, bound_value=187:125211, second_product=374:123722, answer=385:126604)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11702, first_product=182:23858, bound_value=187:21827, second_product=374:25179, answer=385:24872)
- Layer 20: `ait`, ` Walker`, ` LS`, `锁定`, `Walker` (target ranks: base_value=91:9368, first_product=182:28137, bound_value=187:23987, second_product=374:23490, answer=385:23221)
- Layer 30: ` pakig`, ` talags`, `Wil`, `392`, `威尔` (target ranks: base_value=91:1904, first_product=182:994, bound_value=187:16, second_product=374:87, answer=385:90)
- Layer 35: `374`, `375`, `377`, `379`, `376` (target ranks: base_value=91:103363, first_product=182:103692, bound_value=187:208, second_product=374:1, answer=385:16)
- Layer 36: `374`, `375`, `377`, `379`, `387` (target ranks: base_value=91:125717, first_product=182:83055, bound_value=187:34, second_product=374:1, answer=385:16)
- Layer 37: `374`, `375`, `377`, `376`, `379` (target ranks: base_value=91:127945, first_product=182:71701, bound_value=187:58, second_product=374:1, answer=385:11)
- Layer 38: `374`, `375`, `377`, `379`, `381` (target ranks: base_value=91:127711, first_product=182:72657, bound_value=187:193, second_product=374:1, answer=385:11)
- Layer 39: `381`, `379`, `375`, `377`, `380` (target ranks: base_value=91:128297, first_product=182:126465, bound_value=187:6853, second_product=374:6, answer=385:13)
- Layer 40: `375`, `374`, `379`, `381`, `387` (target ranks: base_value=91:128226, first_product=182:120560, bound_value=187:1881, second_product=374:2, answer=385:35)
- Layer 41: `375`, `中书`, `379`, `砚`, `374` (target ranks: base_value=91:125065, first_product=182:103001, bound_value=187:9050, second_product=374:5, answer=385:83)

### Filler position 27 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:126312, first_product=182:125684, bound_value=187:125306, second_product=374:123749, answer=385:126720)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10858, first_product=182:23077, bound_value=187:21041, second_product=374:23900, answer=385:23185)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=91:11205, first_product=182:27960, bound_value=187:18803, second_product=374:24128, answer=385:23792)
- Layer 30: `vf`, `vn`, `分解`, ` violet`, ` vio` (target ranks: base_value=91:5569, first_product=182:67001, bound_value=187:21410, second_product=374:50182, answer=385:35735)
- Layer 35: `分解`, `vf`, ` labor`, `羊`, ` repetition` (target ranks: base_value=91:672, first_product=182:38828, bound_value=187:13960, second_product=374:24083, answer=385:14544)
- Layer 36: `分解`, `留存`, `adal`, ` Wil`, ` wil` (target ranks: base_value=91:598, first_product=182:32475, bound_value=187:6467, second_product=374:20308, answer=385:7938)
- Layer 37: `}<?`, `翻了`, ` Mif`, `翻`, ` rif` (target ranks: base_value=91:3324, first_product=182:61014, bound_value=187:21194, second_product=374:44414, answer=385:16087)
- Layer 38: `}<?`, `zat`, ` Mif`, `迷惑`, `殿堂` (target ranks: base_value=91:7445, first_product=182:68966, bound_value=187:27939, second_product=374:48447, answer=385:13908)
- Layer 39: ` v`, ` V`, `}<?`, `v`, ` Mif` (target ranks: base_value=91:23557, first_product=182:103226, bound_value=187:44319, second_product=374:81627, answer=385:41212)
- Layer 40: `v`, ` v`, `vian`, `殿堂`, `留存` (target ranks: base_value=91:6899, first_product=182:68699, bound_value=187:4590, second_product=374:30292, answer=385:1903)
- Layer 41: ` .`, ` `, `acular`, ` mischief`, `鹉` (target ranks: base_value=91:1339, first_product=182:21918, bound_value=187:1113, second_product=374:4072, answer=385:933)

### Filler position 28 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=91:126380, first_product=182:125534, bound_value=187:125178, second_product=374:123623, answer=385:126511)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=91:10674, first_product=182:23219, bound_value=187:21110, second_product=374:24048, answer=385:23256)
- Layer 20: `ait`, `能被`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=91:13780, first_product=182:33859, bound_value=187:24158, second_product=374:31958, answer=385:28203)
- Layer 30: ` dy`, ` reserved`, ` parallel`, `闲置`, `分解` (target ranks: base_value=91:14192, first_product=182:59324, bound_value=187:11631, second_product=374:34766, answer=385:40955)
- Layer 35: ` reserved`, `分解`, `cape`, `锁定`, `俯` (target ranks: base_value=91:6026, first_product=182:44466, bound_value=187:7954, second_product=374:18573, answer=385:26638)
- Layer 36: `分解`, `俯`, `留存`, ` reserved`, `cape` (target ranks: base_value=91:7425, first_product=182:47374, bound_value=187:6910, second_product=374:14286, answer=385:21629)
- Layer 37: `}<?`, `俯`, `yat`, `分解`, `翻` (target ranks: base_value=91:27440, first_product=182:72027, bound_value=187:18606, second_product=374:27678, answer=385:32021)
- Layer 38: `}<?`, `yat`, `zat`, `y`, `不急` (target ranks: base_value=91:13140, first_product=182:72962, bound_value=187:22080, second_product=374:45231, answer=385:26143)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `东海`, ` dekameters`, `yv` (target ranks: base_value=91:83784, first_product=182:117755, bound_value=187:57696, second_product=374:86533, answer=385:68097)
- Layer 40: `y`, `俯`, ` y`, `坏`, `留存` (target ranks: base_value=91:50376, first_product=182:103495, bound_value=187:31641, second_product=374:67457, answer=385:45083)
- Layer 41: ` .`, `y`, `俯`, ` `, `没有被` (target ranks: base_value=91:16733, first_product=182:73284, bound_value=187:21096, second_product=374:22784, answer=385:18514)

### Filler position 29 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=91:126373, first_product=182:125577, bound_value=187:125236, second_product=374:123543, answer=385:126558)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=91:11399, first_product=182:24222, bound_value=187:22332, second_product=374:25176, answer=385:24045)
- Layer 20: `能被`, `ession`, ` engaging`, `距`, `ait` (target ranks: base_value=91:13551, first_product=182:35495, bound_value=187:25514, second_product=374:31104, answer=385:23472)
- Layer 30: `91`, ` ninety`, `分解`, ` tear`, `九十` (target ranks: base_value=91:1, first_product=182:1242, bound_value=187:3007, second_product=374:20464, answer=385:8440)
- Layer 35: `91`, `分解`, `radesh`, `cape`, ` reserved` (target ranks: base_value=91:1, first_product=182:3967, bound_value=187:4941, second_product=374:24963, answer=385:13353)
- Layer 36: `91`, `radesh`, ` start`, `分解`, `翻` (target ranks: base_value=91:1, first_product=182:10584, bound_value=187:10277, second_product=374:44166, answer=385:19622)
- Layer 37: `}<?`, `radesh`, ` Nij`, ` doubled`, ` doubles` (target ranks: base_value=91:9, first_product=182:24038, bound_value=187:31548, second_product=374:78384, answer=385:50449)
- Layer 38: `}<?`, `radesh`, ` Nij`, `ozygous`, `zat` (target ranks: base_value=91:148, first_product=182:52724, bound_value=187:61243, second_product=374:100304, answer=385:55292)
- Layer 39: `}<?`, `ozygous`, `ocyst`, ` Nij`, `树叶` (target ranks: base_value=91:3322, first_product=182:79283, bound_value=187:67251, second_product=374:90868, answer=385:50181)
- Layer 40: `坏`, `坏的`, `殿堂`, `acl`, `坏了` (target ranks: base_value=91:7538, first_product=182:68607, bound_value=187:19338, second_product=374:40279, answer=385:9475)
- Layer 41: `坏`, ` .`, `从前`, ` `, `acular` (target ranks: base_value=91:2029, first_product=182:45023, bound_value=187:18963, second_product=374:19009, answer=385:5789)

### Filler position 30 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=91:126561, first_product=182:126076, bound_value=187:125755, second_product=374:124103, answer=385:127042)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10906, first_product=182:22816, bound_value=187:21738, second_product=374:24953, answer=385:23526)
- Layer 20: `ait`, ` LS`, ` wig`, `锁定`, ` smile` (target ranks: base_value=91:8092, first_product=182:22974, bound_value=187:21805, second_product=374:19610, answer=385:20049)
- Layer 30: `187`, ` Behavior`, ` Prussian`, ` Ries`, `哪天` (target ranks: base_value=91:95, first_product=182:23, bound_value=187:1, second_product=374:510, answer=385:2168)
- Layer 35: `187`, `洋`, `鞍`, `Wik`, ` Wil` (target ranks: base_value=91:4817, first_product=182:31831, bound_value=187:1, second_product=374:7, answer=385:1335)
- Layer 36: `187`, `374`, ` Berlin`, ` Wikidata`, `376` (target ranks: base_value=91:33153, first_product=182:36955, bound_value=187:1, second_product=374:2, answer=385:3411)
- Layer 37: `187`, `李鸿章`, ` Leipzig`, ` Berlin`, `374` (target ranks: base_value=91:61787, first_product=182:10220, bound_value=187:1, second_product=374:5, answer=385:4544)
- Layer 38: `187`, `李鸿章`, ` Wikidata`, ` Leipzig`, `光绪` (target ranks: base_value=91:93455, first_product=182:11028, bound_value=187:1, second_product=374:6, answer=385:2289)
- Layer 39: `187`, ` Leipzig`, `李鸿章`, `387`, `�` (target ranks: base_value=91:120149, first_product=182:107043, bound_value=187:1, second_product=374:44, answer=385:5574)
- Layer 40: ` mir`, `留存`, `ologue`, `dard`, ` dich` (target ranks: base_value=91:117607, first_product=182:120883, bound_value=187:8, second_product=374:100, answer=385:2610)
- Layer 41: ` waiting`, `dard`, `有这样`, ` mim`, ` because` (target ranks: base_value=91:72393, first_product=182:92514, bound_value=187:57, second_product=374:51, answer=385:2463)

### Filler position 31 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=91:126762, first_product=182:126182, bound_value=187:125883, second_product=374:124218, answer=385:127197)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:9997, first_product=182:21255, bound_value=187:20412, second_product=374:24161, answer=385:23232)
- Layer 20: `锁定`, `ait`, ` smile`, `忑`, `鞍` (target ranks: base_value=91:8498, first_product=182:20760, bound_value=187:16283, second_product=374:24212, answer=385:21772)
- Layer 30: `Rational`, `rational`, ` rational`, ` Rational`, ` tap` (target ranks: base_value=91:39780, first_product=182:44021, bound_value=187:12067, second_product=374:28411, answer=385:52337)
- Layer 35: `rational`, ` rational`, `Rational`, ` Lé`, ` tap` (target ranks: base_value=91:43288, first_product=182:94613, bound_value=187:36606, second_product=374:34770, answer=385:72699)
- Layer 36: ` tap`, ` Aufgabe`, `kä`, ` rip`, `Tap` (target ranks: base_value=91:12886, first_product=182:56136, bound_value=187:20466, second_product=374:20712, answer=385:50209)
- Layer 37: `comp`, `rational`, ` tap`, ` rational`, `冰冰` (target ranks: base_value=91:30007, first_product=182:70553, bound_value=187:59293, second_product=374:33245, answer=385:67073)
- Layer 38: `�`, `}<?`, `rational`, `打包`, `覆` (target ranks: base_value=91:54720, first_product=182:73713, bound_value=187:67540, second_product=374:44668, answer=385:67412)
- Layer 39: `�`, `aharan`, `hemer`, `}<?`, `orten` (target ranks: base_value=91:81660, first_product=182:115533, bound_value=187:49264, second_product=374:29692, answer=385:40332)
- Layer 40: ` mimic`, ` Number`, `acular`, ` forty`, `试一试` (target ranks: base_value=91:39887, first_product=182:82835, bound_value=187:11262, second_product=374:8128, answer=385:3084)
- Layer 41: ` .`, `Answer`, `试一试`, ` Answer`, ` number` (target ranks: base_value=91:12420, first_product=182:28393, bound_value=187:4032, second_product=374:352, answer=385:225)

### Filler position 32 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=91:126566, first_product=182:125946, bound_value=187:125659, second_product=374:124019, answer=385:126988)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:9887, first_product=182:21610, bound_value=187:20330, second_product=374:23129, answer=385:23494)
- Layer 20: ` Walker`, ` LS`, `锁定`, `ait`, `Walker` (target ranks: base_value=91:8077, first_product=182:19191, bound_value=187:11583, second_product=374:21531, answer=385:18601)
- Layer 30: ` labor`, ` dy`, ` y`, ` Y`, `y` (target ranks: base_value=91:37701, first_product=182:68692, bound_value=187:33315, second_product=374:94458, answer=385:82079)
- Layer 35: ` labor`, ` y`, ` var`, ` stabil`, ` dy` (target ranks: base_value=91:25696, first_product=182:54266, bound_value=187:31290, second_product=374:62618, answer=385:58582)
- Layer 36: ` definitions`, `y`, ` y`, ` stabil`, `Definitions` (target ranks: base_value=91:29014, first_product=182:42928, bound_value=187:22479, second_product=374:53705, answer=385:36376)
- Layer 37: `}<?`, ` definitions`, `Definitions`, `y`, `定义` (target ranks: base_value=91:79391, first_product=182:63178, bound_value=187:63504, second_product=374:81124, answer=385:53574)
- Layer 38: `}<?`, `Definitions`, ` definitions`, `y`, `yv` (target ranks: base_value=91:77034, first_product=182:61242, bound_value=187:67248, second_product=374:72169, answer=385:30715)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `yv`, `.y`, `yel` (target ranks: base_value=91:68179, first_product=182:94461, bound_value=187:70299, second_product=374:95573, answer=385:62952)
- Layer 40: ` y`, `y`, `留存`, `}<?`, `殿堂` (target ranks: base_value=91:20508, first_product=182:82708, bound_value=187:44933, second_product=374:96150, answer=385:27528)
- Layer 41: ` .`, `等待`, ` waiting`, `y`, ` ` (target ranks: base_value=91:3903, first_product=182:42758, bound_value=187:28384, second_product=374:49680, answer=385:8463)

### Filler position 33 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=91:126864, first_product=182:126266, bound_value=187:125992, second_product=374:124376, answer=385:127346)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:9703, first_product=182:21494, bound_value=187:20089, second_product=374:22268, answer=385:23157)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `足` (target ranks: base_value=91:8965, first_product=182:23428, bound_value=187:15138, second_product=374:18410, answer=385:20145)
- Layer 30: ` Miy`, `算出`, `ayi`, ` MI`, ` Mir` (target ranks: base_value=91:15071, first_product=182:24377, bound_value=187:21455, second_product=374:55644, answer=385:40614)
- Layer 35: ` Miy`, ` mir`, ` Mir`, `留存`, `Mir` (target ranks: base_value=91:14658, first_product=182:28410, bound_value=187:28678, second_product=374:44953, answer=385:34503)
- Layer 36: ` Miy`, `留存`, ` mir`, `反复`, ` Mir` (target ranks: base_value=91:14010, first_product=182:23385, bound_value=187:17631, second_product=374:34091, answer=385:23707)
- Layer 37: ` Miy`, ` MI`, ` mir`, ` Mir`, `mi` (target ranks: base_value=91:49885, first_product=182:32221, bound_value=187:36608, second_product=374:48353, answer=385:32786)
- Layer 38: ` Miy`, ` mir`, ` MI`, ` Mir`, `明珠` (target ranks: base_value=91:56731, first_product=182:39805, bound_value=187:44503, second_product=374:49612, answer=385:30466)
- Layer 39: ` MI`, ` mir`, ` Mir`, ` Miy`, ` Mi` (target ranks: base_value=91:69530, first_product=182:69800, bound_value=187:55325, second_product=374:70295, answer=385:59743)
- Layer 40: `留存`, `scr`, ` mir`, `zij`, `殿堂` (target ranks: base_value=91:25606, first_product=182:37932, bound_value=187:12585, second_product=374:43031, answer=385:14372)
- Layer 41: ` `, ` .`, `不思`, `zij`, `没有被` (target ranks: base_value=91:5616, first_product=182:9644, bound_value=187:7081, second_product=374:15424, answer=385:10757)

### Filler position 34 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=91:126908, first_product=182:126434, bound_value=187:126133, second_product=374:124572, answer=385:127377)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:10620, first_product=182:22525, bound_value=187:20992, second_product=374:23570, answer=385:23685)
- Layer 20: `ait`, ` Walker`, `锁定`, ` LS`, `能被` (target ranks: base_value=91:9029, first_product=182:26832, bound_value=187:20183, second_product=374:15591, answer=385:17119)
- Layer 30: `187`, `182`, `184`, `189`, `胃癌` (target ranks: base_value=91:129, first_product=182:2, bound_value=187:1, second_product=374:3343, answer=385:1128)
- Layer 35: `187`, `同治`, `186`, ` Prussian`, `洋` (target ranks: base_value=91:30997, first_product=182:30429, bound_value=187:1, second_product=374:1045, answer=385:26589)
- Layer 36: `187`, `同治`, ` Prussian`, `Wik`, ` Berlin` (target ranks: base_value=91:49193, first_product=182:30525, bound_value=187:1, second_product=374:147, answer=385:53946)
- Layer 37: `187`, `同治`, `李鸿章`, ` Berlin`, ` Prussian` (target ranks: base_value=91:86184, first_product=182:18204, bound_value=187:1, second_product=374:626, answer=385:77058)
- Layer 38: `187`, `同治`, `李鸿章`, ` Prussian`, `�` (target ranks: base_value=91:107050, first_product=182:28634, bound_value=187:1, second_product=374:1236, answer=385:82964)
- Layer 39: `187`, `同治`, `�`, ` Leipzig`, ` Trou` (target ranks: base_value=91:118774, first_product=182:98497, bound_value=187:1, second_product=374:9343, answer=385:93324)
- Layer 40: `187`, ` mir`, ` mirrored`, `坏`, ` vine` (target ranks: base_value=91:118301, first_product=182:112547, bound_value=187:1, second_product=374:17976, answer=385:60947)
- Layer 41: ` y`, `187`, `y`, `有这样`, ` unless` (target ranks: base_value=91:81128, first_product=182:79935, bound_value=187:2, second_product=374:4025, answer=385:31386)

### Filler position 35 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=91:127210, first_product=182:126626, bound_value=187:126341, second_product=374:124806, answer=385:127580)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11610, first_product=182:23810, bound_value=187:21477, second_product=374:24439, answer=385:24471)
- Layer 20: `ait`, ` smile`, `足`, ` engaging`, ` Walker` (target ranks: base_value=91:11958, first_product=182:22956, bound_value=187:10832, second_product=374:18663, answer=385:20983)
- Layer 30: ` Tw`, `Tw`, ` twice`, `.tw`, `tw` (target ranks: base_value=91:33375, first_product=182:21074, bound_value=187:11198, second_product=374:40509, answer=385:28585)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=91:17920, first_product=182:16205, bound_value=187:9378, second_product=374:18369, answer=385:12638)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=91:26564, first_product=182:12615, bound_value=187:6262, second_product=374:13118, answer=385:9216)
- Layer 37: ` Tw`, `Tw`, ` doubling`, `坏`, ` twice` (target ranks: base_value=91:77470, first_product=182:29057, bound_value=187:19156, second_product=374:23980, answer=385:12379)
- Layer 38: ` Tw`, ` doubling`, `Tw`, `.tw`, `坏` (target ranks: base_value=91:86277, first_product=182:38738, bound_value=187:26754, second_product=374:33904, answer=385:16921)
- Layer 39: `}<?`, ` Tw`, ` doubling`, `坏`, `东海` (target ranks: base_value=91:62536, first_product=182:41667, bound_value=187:19854, second_product=374:56467, answer=385:23763)
- Layer 40: `坏`, `坏的`, ` Tw`, `坏了`, `壞` (target ranks: base_value=91:17589, first_product=182:16857, bound_value=187:2572, second_product=374:36854, answer=385:12423)
- Layer 41: ` .`, `坏`, ` `, ` because`, `.,` (target ranks: base_value=91:4043, first_product=182:2046, bound_value=187:520, second_product=374:2821, answer=385:1836)

### Filler position 36 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127255, first_product=182:126785, bound_value=187:126563, second_product=374:124960, answer=385:127792)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:12258, first_product=182:24819, bound_value=187:22250, second_product=374:25780, answer=385:25697)
- Layer 20: `能被`, ` Walker`, `ait`, ` smile`, `LS` (target ranks: base_value=91:5836, first_product=182:19699, bound_value=187:12295, second_product=374:13377, answer=385:16089)
- Layer 30: `91`, ` ninety`, `题库`, `九十`, `算出` (target ranks: base_value=91:1, first_product=182:79, bound_value=187:257, second_product=374:28142, answer=385:18848)
- Layer 35: `91`, ` twice`, `adaghan`, `分解`, ` Tw` (target ranks: base_value=91:1, first_product=182:33, bound_value=187:41, second_product=374:33385, answer=385:19700)
- Layer 36: ` doubled`, `91`, `radesh`, `分解`, `翻` (target ranks: base_value=91:2, first_product=182:83, bound_value=187:64, second_product=374:52853, answer=385:42963)
- Layer 37: `}<?`, ` doubled`, ` doubling`, ` Nij`, ` doubles` (target ranks: base_value=91:94, first_product=182:142, bound_value=187:145, second_product=374:89985, answer=385:81952)
- Layer 38: `}<?`, ` doubled`, ` doubling`, ` Nij`, ` doubles` (target ranks: base_value=91:866, first_product=182:1363, bound_value=187:1063, second_product=374:113676, answer=385:81568)
- Layer 39: `}<?`, ` doubled`, ` Nij`, ` doubling`, `ASI` (target ranks: base_value=91:32073, first_product=182:13231, bound_value=187:25477, second_product=374:109876, answer=385:101493)
- Layer 40: ` Tw`, `.tw`, `Tw`, `}<?`, ` mir` (target ranks: base_value=91:49281, first_product=182:22814, bound_value=187:1115, second_product=374:47358, answer=385:43223)
- Layer 41: ` Tw`, `.tw`, `Tw`, ` .`, ` twist` (target ranks: base_value=91:13058, first_product=182:7040, bound_value=187:1135, second_product=374:10200, answer=385:22280)

### Filler position 37 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127309, first_product=182:126996, bound_value=187:126746, second_product=374:125206, answer=385:127860)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11513, first_product=182:23818, bound_value=187:21931, second_product=374:25865, answer=385:25119)
- Layer 20: `能被`, `忑`, `距`, ` Walker`, `ait` (target ranks: base_value=91:10830, first_product=182:30663, bound_value=187:18351, second_product=374:24126, answer=385:34166)
- Layer 30: `生日`, `前`, ` vertical`, ` trunk`, `enna` (target ranks: base_value=91:606, first_product=182:3404, bound_value=187:176, second_product=374:992, answer=385:3971)
- Layer 35: `374`, `372`, `375`, `373`, `obin` (target ranks: base_value=91:16962, first_product=182:54416, bound_value=187:1580, second_product=374:1, answer=385:1526)
- Layer 36: `374`, `874`, `372`, `376`, `}<?` (target ranks: base_value=91:72473, first_product=182:95615, bound_value=187:1317, second_product=374:1, answer=385:8495)
- Layer 37: `374`, `}<?`, `874`, `图画`, `宰` (target ranks: base_value=91:103036, first_product=182:64124, bound_value=187:1002, second_product=374:1, answer=385:17893)
- Layer 38: `374`, `}<?`, `图画`, `院长`, `372` (target ranks: base_value=91:97050, first_product=182:71999, bound_value=187:2185, second_product=374:1, answer=385:10773)
- Layer 39: `374`, `}<?`, `372`, `ozygous`, ` Hamburg` (target ranks: base_value=91:114378, first_product=182:94411, bound_value=187:665, second_product=374:1, answer=385:12094)
- Layer 40: `374`, `acular`, `留存`, `院长`, ` dich` (target ranks: base_value=91:87759, first_product=182:69119, bound_value=187:1250, second_product=374:1, answer=385:826)
- Layer 41: `374`, `375`, ` Tw`, `372`, ` twist` (target ranks: base_value=91:21447, first_product=182:14362, bound_value=187:986, second_product=374:1, answer=385:326)

### Filler position 38 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127292, first_product=182:126954, bound_value=187:126734, second_product=374:125100, answer=385:127790)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11843, first_product=182:23796, bound_value=187:22490, second_product=374:26390, answer=385:25218)
- Layer 20: `忑`, `能被`, `ait`, ` engaging`, ` ES` (target ranks: base_value=91:21678, first_product=182:47458, bound_value=187:38016, second_product=374:42044, answer=385:44970)
- Layer 30: ` kahaboga`, ` Mim`, ` mimic`, `Dy`, `退出` (target ranks: base_value=91:5867, first_product=182:18900, bound_value=187:572, second_product=374:780, answer=385:69)
- Layer 35: `375`, `387`, `374`, `379`, `373` (target ranks: base_value=91:52883, first_product=182:108010, bound_value=187:1291, second_product=374:3, answer=385:70)
- Layer 36: `387`, `375`, `388`, `383`, `385` (target ranks: base_value=91:53977, first_product=182:87513, bound_value=187:135, second_product=374:13, answer=385:5)
- Layer 37: `387`, `375`, `385`, `383`, `388` (target ranks: base_value=91:73269, first_product=182:67809, bound_value=187:103, second_product=374:16, answer=385:3)
- Layer 38: `385`, `387`, `375`, `383`, `395` (target ranks: base_value=91:124359, first_product=182:125486, bound_value=187:2787, second_product=374:81, answer=385:1)
- Layer 39: `385`, `387`, `395`, `386`, `399` (target ranks: base_value=91:126895, first_product=182:126111, bound_value=187:10175, second_product=374:2959, answer=385:1)
- Layer 40: `387`, `385`, `<｜begin▁of▁file｜>`, `399`, `395` (target ranks: base_value=91:121528, first_product=182:110936, bound_value=187:3561, second_product=374:322, answer=385:2)
- Layer 41: `385`, `387`, `399`, `}}}}`, `<｜begin▁of▁file｜>` (target ranks: base_value=91:69009, first_product=182:97186, bound_value=187:7861, second_product=374:3223, answer=385:1)

### Filler position 39 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127326, first_product=182:127105, bound_value=187:126905, second_product=374:125279, answer=385:128014)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11427, first_product=182:23084, bound_value=187:21858, second_product=374:25257, answer=385:24575)
- Layer 20: `ait`, `锁定`, ` engaging`, ` ES`, ` Engaging` (target ranks: base_value=91:15835, first_product=182:36563, bound_value=187:23627, second_product=374:33679, answer=385:34780)
- Layer 30: `Quintal`, `}<?`, `Noiz`, `acet`, `CopyWith` (target ranks: base_value=91:9148, first_product=182:11066, bound_value=187:396, second_product=374:999, answer=385:1168)
- Layer 35: `387`, `381`, `382`, `392`, `379` (target ranks: base_value=91:39475, first_product=182:107189, bound_value=187:6253, second_product=374:85, answer=385:33)
- Layer 36: `387`, `399`, `395`, `392`, `381` (target ranks: base_value=91:57803, first_product=182:107119, bound_value=187:2856, second_product=374:114, answer=385:47)
- Layer 37: `书馆`, `387`, `399`, `395`, `391` (target ranks: base_value=91:93721, first_product=182:112754, bound_value=187:11421, second_product=374:345, answer=385:55)
- Layer 38: `399`, `395`, `书馆`, `387`, `795` (target ranks: base_value=91:114250, first_product=182:122078, bound_value=187:24177, second_product=374:1894, answer=385:52)
- Layer 39: `书馆`, `399`, `看书`, `395`, `宫内` (target ranks: base_value=91:123633, first_product=182:127086, bound_value=187:57954, second_product=374:43875, answer=385:273)
- Layer 40: `399`, ` `, `观的`, `387`, `积淀` (target ranks: base_value=91:122447, first_product=182:126035, bound_value=187:30431, second_product=374:20351, answer=385:184)
- Layer 41: `399`, `391`, ` `, `393`, `387` (target ranks: base_value=91:70500, first_product=182:96150, bound_value=187:12142, second_product=374:3361, answer=385:59)

### Filler position 40 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127446, first_product=182:126956, bound_value=187:126761, second_product=374:125070, answer=385:127914)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11299, first_product=182:23013, bound_value=187:22156, second_product=374:25291, answer=385:24102)
- Layer 20: `ait`, `锁定`, `鞍`, ` LS`, `ätte` (target ranks: base_value=91:8711, first_product=182:27259, bound_value=187:19681, second_product=374:24695, answer=385:19119)
- Layer 30: `acos`, `Quintal`, `opan`, `}<?`, ` Tour` (target ranks: base_value=91:8799, first_product=182:22363, bound_value=187:400, second_product=374:448, answer=385:435)
- Layer 35: `749`, `743`, `75`, `754`, `755` (target ranks: base_value=91:55325, first_product=182:108132, bound_value=187:25685, second_product=374:35, answer=385:60)
- Layer 36: `749`, `755`, `759`, `754`, `775` (target ranks: base_value=91:95444, first_product=182:117184, bound_value=187:26314, second_product=374:84, answer=385:49)
- Layer 37: `759`, `755`, `749`, `761`, `754` (target ranks: base_value=91:116056, first_product=182:114863, bound_value=187:60372, second_product=374:129, answer=385:70)
- Layer 38: `759`, `749`, `765`, `761`, `755` (target ranks: base_value=91:120903, first_product=182:122186, bound_value=187:64828, second_product=374:268, answer=385:69)
- Layer 39: `759`, `769`, `761`, `765`, `767` (target ranks: base_value=91:122448, first_product=182:126913, bound_value=187:98038, second_product=374:38363, answer=385:374)
- Layer 40: `放下`, ` view`, ` `, `留存`, `749` (target ranks: base_value=91:115926, first_product=182:123451, bound_value=187:47807, second_product=374:20600, answer=385:170)
- Layer 41: ` .`, ` `, ` */`, `))))`, ` :)` (target ranks: base_value=91:57694, first_product=182:83349, bound_value=187:26682, second_product=374:5530, answer=385:82)

### Filler position 41 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127222, first_product=182:126702, bound_value=187:126537, second_product=374:124854, answer=385:127732)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11242, first_product=182:22806, bound_value=187:22403, second_product=374:25343, answer=385:24171)
- Layer 20: `锁定`, `ait`, ` smile`, ` LS`, `能被` (target ranks: base_value=91:7229, first_product=182:25137, bound_value=187:18406, second_product=374:18654, answer=385:19167)
- Layer 30: `Quintal`, `陪`, ` perturb`, ` kahaboga`, `otan` (target ranks: base_value=91:6389, first_product=182:16460, bound_value=187:379, second_product=374:377, answer=385:95)
- Layer 35: `375`, `374`, `379`, `387`, `367` (target ranks: base_value=91:61339, first_product=182:106064, bound_value=187:372, second_product=374:2, answer=385:38)
- Layer 36: `387`, `375`, `383`, `385`, `388` (target ranks: base_value=91:91550, first_product=182:93426, bound_value=187:97, second_product=374:8, answer=385:4)
- Layer 37: `387`, `375`, `383`, `385`, `384` (target ranks: base_value=91:106470, first_product=182:68207, bound_value=187:130, second_product=374:7, answer=385:4)
- Layer 38: `385`, `387`, `375`, `383`, `395` (target ranks: base_value=91:127394, first_product=182:125170, bound_value=187:2055, second_product=374:27, answer=385:1)
- Layer 39: `385`, `387`, `383`, `386`, `395` (target ranks: base_value=91:127685, first_product=182:127111, bound_value=187:4820, second_product=374:3882, answer=385:1)
- Layer 40: `387`, `385`, `399`, `383`, `395` (target ranks: base_value=91:124681, first_product=182:117580, bound_value=187:1503, second_product=374:411, answer=385:2)
- Layer 41: `387`, `385`, `�`, ` expectation`, `}}}}` (target ranks: base_value=91:73196, first_product=182:104835, bound_value=187:7298, second_product=374:1798, answer=385:2)

### Filler position 42 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127430, first_product=182:127037, bound_value=187:126823, second_product=374:125214, answer=385:128035)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:12873, first_product=182:23887, bound_value=187:23432, second_product=374:27378, answer=385:25596)
- Layer 20: ` smile`, `锁定`, `距`, `鞍`, `ession` (target ranks: base_value=91:12744, first_product=182:22774, bound_value=187:15875, second_product=374:18710, answer=385:18670)
- Layer 30: ` trunk`, ` Prussian`, `iab`, ` ninety`, ` ninete` (target ranks: base_value=91:487, first_product=182:1458, bound_value=187:1127, second_product=374:36110, answer=385:17459)
- Layer 35: `鞍`, `187`, ` trunk`, `分解`, `错过` (target ranks: base_value=91:1062, first_product=182:15142, bound_value=187:2, second_product=374:20796, answer=385:17692)
- Layer 36: `radesh`, `翻`, `陪`, `187`, `骨架` (target ranks: base_value=91:10196, first_product=182:16173, bound_value=187:4, second_product=374:19056, answer=385:20686)
- Layer 37: `}<?`, `radesh`, ` Nij`, `187`, ` Sheffield` (target ranks: base_value=91:38231, first_product=182:11031, bound_value=187:4, second_product=374:33742, answer=385:37551)
- Layer 38: `}<?`, ` Sheffield`, `radesh`, ` Nij`, `东海` (target ranks: base_value=91:53828, first_product=182:18747, bound_value=187:11, second_product=374:50797, answer=385:33410)
- Layer 39: `}<?`, ` Nij`, `-ulo`, `uerak`, `东海` (target ranks: base_value=91:91907, first_product=182:56566, bound_value=187:248, second_product=374:42982, answer=385:20409)
- Layer 40: ` Tw`, `坏`, ` `, `.tw`, `duc` (target ranks: base_value=91:49565, first_product=182:46057, bound_value=187:36, second_product=374:19360, answer=385:582)
- Layer 41: ` .`, ` `, ` Tw`, ` because`, `坏` (target ranks: base_value=91:16746, first_product=182:22323, bound_value=187:65, second_product=374:2781, answer=385:178)

### Filler position 43 (absolute token 845, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127375, first_product=182:127051, bound_value=187:126889, second_product=374:125259, answer=385:128039)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:12191, first_product=182:23506, bound_value=187:22453, second_product=374:27167, answer=385:25724)
- Layer 20: `锁定`, ` ES`, `ait`, ` smile`, `距` (target ranks: base_value=91:10887, first_product=182:23888, bound_value=187:18493, second_product=374:23556, answer=385:21900)
- Layer 30: `iab`, `反复`, ` repeat`, ` trunk`, `187` (target ranks: base_value=91:1741, first_product=182:321, bound_value=187:5, second_product=374:781, answer=385:846)
- Layer 35: `374`, `375`, `373`, `372`, `377` (target ranks: base_value=91:94496, first_product=182:107764, bound_value=187:1109, second_product=374:1, answer=385:279)
- Layer 36: `374`, `375`, `974`, `874`, `774` (target ranks: base_value=91:122411, first_product=182:124232, bound_value=187:1725, second_product=374:1, answer=385:7408)
- Layer 37: `374`, `974`, `宰`, `874`, `375` (target ranks: base_value=91:128318, first_product=182:123192, bound_value=187:6354, second_product=374:1, answer=385:24184)
- Layer 38: `374`, `宰`, `375`, ` mdl`, ` Hamburg` (target ranks: base_value=91:127610, first_product=182:126471, bound_value=187:12326, second_product=374:1, answer=385:17393)
- Layer 39: `374`, ` mdl`, `375`, `erger`, `-ulo` (target ranks: base_value=91:127425, first_product=182:126901, bound_value=187:32558, second_product=374:1, answer=385:19801)
- Layer 40: `374`, `悬念`, ` waiting`, ` mark`, `留存` (target ranks: base_value=91:121856, first_product=182:124239, bound_value=187:20188, second_product=374:1, answer=385:195)
- Layer 41: `374`, `375`, ` waiting`, ` number`, `悬念` (target ranks: base_value=91:79254, first_product=182:96268, bound_value=187:19482, second_product=374:1, answer=385:139)

### Filler position 44 (absolute token 846, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127282, first_product=182:126690, bound_value=187:126520, second_product=374:124873, answer=385:127755)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:12184, first_product=182:23326, bound_value=187:21951, second_product=374:26766, answer=385:25259)
- Layer 20: `ait`, `忑`, `距`, ` ES`, `锁定` (target ranks: base_value=91:14555, first_product=182:27936, bound_value=187:20087, second_product=374:30121, answer=385:26806)
- Layer 30: ` twice`, ` ninete`, `iab`, `反复`, `eas` (target ranks: base_value=91:215, first_product=182:1160, bound_value=187:56, second_product=374:14548, answer=385:6048)
- Layer 35: `382`, `374`, `384`, `381`, `Wil` (target ranks: base_value=91:13751, first_product=182:32292, bound_value=187:305, second_product=374:2, answer=385:62)
- Layer 36: `374`, `382`, `384`, `}<?`, ` Sheffield` (target ranks: base_value=91:64788, first_product=182:60126, bound_value=187:332, second_product=374:1, answer=385:234)
- Layer 37: `}<?`, `374`, `dividers`, ` Sheffield`, `382` (target ranks: base_value=91:103678, first_product=182:56009, bound_value=187:1893, second_product=374:2, answer=385:2599)
- Layer 38: `}<?`, `本题分析`, `374`, `东海`, `院长` (target ranks: base_value=91:104312, first_product=182:62442, bound_value=187:3555, second_product=374:3, answer=385:2659)
- Layer 39: `}<?`, `东海`, `�`, ` Kiel`, `hemer` (target ranks: base_value=91:108338, first_product=182:72214, bound_value=187:3488, second_product=374:29, answer=385:2336)
- Layer 40: ` Tw`, `Tw`, `留存`, `387`, ` mir` (target ranks: base_value=91:88635, first_product=182:71388, bound_value=187:110, second_product=374:87, answer=385:19)
- Layer 41: `387`, `375`, `382`, ` .`, ` Tw` (target ranks: base_value=91:47814, first_product=182:18371, bound_value=187:117, second_product=374:9, answer=385:8)

### Filler position 45 (absolute token 847, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `datasetId`, `Noiz`, `�乐` (target ranks: base_value=91:127714, first_product=182:127304, bound_value=187:127161, second_product=374:125656, answer=385:128202)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=91:11755, first_product=182:22598, bound_value=187:21437, second_product=374:25342, answer=385:24085)
- Layer 20: `ait`, ` Walker`, `锁定`, `会成为`, `能被` (target ranks: base_value=91:16524, first_product=182:33088, bound_value=187:21215, second_product=374:37565, answer=385:31412)
- Layer 30: ` Miy`, ` Mir`, ` MI`, `第一步`, ` step` (target ranks: base_value=91:57782, first_product=182:70945, bound_value=187:39006, second_product=374:109403, answer=385:78807)
- Layer 35: `viol`, ` Miy`, ` print`, `留存`, ` viol` (target ranks: base_value=91:47190, first_product=182:73988, bound_value=187:35511, second_product=374:67437, answer=385:55777)
- Layer 36: `留存`, `反复`, ` Bly`, ` Bonn`, ` live` (target ranks: base_value=91:27400, first_product=182:34018, bound_value=187:11828, second_product=374:38300, answer=385:15492)
- Layer 37: `}<?`, ` Liv`, ` Bly`, `班的`, ` polar` (target ranks: base_value=91:82240, first_product=182:69403, bound_value=187:44328, second_product=374:64436, answer=385:24810)
- Layer 38: `}<?`, `班的`, ` polar`, ` Liv`, `本题分析` (target ranks: base_value=91:74022, first_product=182:74745, bound_value=187:39975, second_product=374:51486, answer=385:16704)
- Layer 39: `}<?`, ` Kiel`, ` sublim`, `polar`, `本题分析` (target ranks: base_value=91:70125, first_product=182:87677, bound_value=187:30104, second_product=374:49632, answer=385:19578)
- Layer 40: `留存`, ` Seventy`, ` seventy`, ` sixty`, `不思` (target ranks: base_value=91:17960, first_product=182:31897, bound_value=187:1435, second_product=374:13247, answer=385:323)
- Layer 41: ` .`, ` `, `<｜end▁of▁sentence｜>`, ` seventy`, `留存` (target ranks: base_value=91:3473, first_product=182:8381, bound_value=187:410, second_product=374:839, answer=385:37)

### Filler position 46 (absolute token 848, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127478, first_product=182:127015, bound_value=187:126847, second_product=374:125196, answer=385:128042)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=91:12241, first_product=182:23021, bound_value=187:21986, second_product=374:25944, answer=385:24131)
- Layer 20: ` Blank`, ` blanks`, `blank`, ` blank`, `空白` (target ranks: base_value=91:105879, first_product=182:88412, bound_value=187:39998, second_product=374:95069, answer=385:72933)
- Layer 30: `?datasetId`, ` spac`, ` dekameters`, `}using`, `}<?` (target ranks: base_value=91:123593, first_product=182:106599, bound_value=187:22520, second_product=374:101959, answer=385:89872)
- Layer 35: `ovel`, `放下`, `足足`, `}using`, `dividers` (target ranks: base_value=91:118797, first_product=182:96814, bound_value=187:25421, second_product=374:52203, answer=385:88364)
- Layer 36: `足足`, `俯`, `ancock`, ` reserved`, ` spare` (target ranks: base_value=91:73388, first_product=182:55952, bound_value=187:5946, second_product=374:25069, answer=385:32419)
- Layer 37: `}<?`, `放下`, `onana`, `放下了`, `isis` (target ranks: base_value=91:107769, first_product=182:67166, bound_value=187:26407, second_product=374:50218, answer=385:27452)
- Layer 38: ` .`, ` Wilson`, `坏`, `错过`, `俯` (target ranks: base_value=91:71987, first_product=182:48527, bound_value=187:14777, second_product=374:41796, answer=385:8953)
- Layer 39: ` .`, `osaurus`, `oxygen`, `�`, `hatic` (target ranks: base_value=91:110177, first_product=182:105062, bound_value=187:23967, second_product=374:32383, answer=385:6243)
- Layer 40: ` .`, ` nasod`, `�`, ` .↵↵`, ` x` (target ranks: base_value=91:71271, first_product=182:63095, bound_value=187:3506, second_product=374:10674, answer=385:1558)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=91:28527, first_product=182:15498, bound_value=187:285, second_product=374:626, answer=385:119)

### Filler position 47 (absolute token 849, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=91:127473, first_product=182:126927, bound_value=187:126745, second_product=374:125053, answer=385:127987)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=91:11714, first_product=182:23064, bound_value=187:21681, second_product=374:25520, answer=385:23849)
- Layer 20: `}<?`, `东海`, ` partly`, `)Skip`, `ozygous` (target ranks: base_value=91:126862, first_product=182:119252, bound_value=187:97996, second_product=374:118073, answer=385:116854)
- Layer 30: `}<?`, `dividers`, `codeline`, `}using`, `lett` (target ranks: base_value=91:120682, first_product=182:110441, bound_value=187:69381, second_product=374:114286, answer=385:119331)
- Layer 35: `codeline`, `lett`, `ِّف`, `蜗`, `切割` (target ranks: base_value=91:119712, first_product=182:118283, bound_value=187:96341, second_product=374:105477, answer=385:123134)
- Layer 36: ` nasod`, `足足`, `坏`, `直觉`, ` fit` (target ranks: base_value=91:88506, first_product=182:99600, bound_value=187:54880, second_product=374:86949, answer=385:98171)
- Layer 37: `磨损`, `}<?`, `东京`, ` doubles`, ` prose` (target ranks: base_value=91:116684, first_product=182:93409, bound_value=187:78342, second_product=374:94599, answer=385:79643)
- Layer 38: ` .`, `遁`, `切割`, `坏`, ` prese` (target ranks: base_value=91:111482, first_product=182:59480, bound_value=187:37988, second_product=374:86915, answer=385:54553)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, `遁`, `�`, `坏` (target ranks: base_value=91:125243, first_product=182:100085, bound_value=187:45409, second_product=374:70568, answer=385:48393)
- Layer 40: ` .`, ` .↵↵`, `�`, `坏`, ` .↵` (target ranks: base_value=91:115659, first_product=182:72127, bound_value=187:18936, second_product=374:35239, answer=385:16572)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: base_value=91:63588, first_product=182:12598, bound_value=187:2057, second_product=374:2011, answer=385:1090)

### Filler position 48 (absolute token 850, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127431, first_product=182:127033, bound_value=187:126865, second_product=374:125167, answer=385:128102)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=91:11204, first_product=182:23291, bound_value=187:21484, second_product=374:25619, answer=385:23531)
- Layer 20: `东海`, ` instantaneous`, `aharoa`, `}<?`, `)Skip` (target ranks: base_value=91:115714, first_product=182:95411, bound_value=187:68067, second_product=374:91554, answer=385:108967)
- Layer 30: `东京`, ` accompanying`, `codeline`, ` accompan`, `日产` (target ranks: base_value=91:74239, first_product=182:63153, bound_value=187:89185, second_product=374:90276, answer=385:99081)
- Layer 35: `codeline`, ` soci`, ` doubly`, ` fif`, ` caterpillar` (target ranks: base_value=91:75422, first_product=182:94643, bound_value=187:101932, second_product=374:94981, answer=385:111164)
- Layer 36: ` soci`, ` nasod`, ` Predict`, `停`, `兜` (target ranks: base_value=91:45512, first_product=182:84534, bound_value=187:79419, second_product=374:78926, answer=385:85822)
- Layer 37: `codeline`, `TreeLabel`, `镶嵌`, `Quintal`, `悬挂` (target ranks: base_value=91:111708, first_product=182:92886, bound_value=187:116643, second_product=374:105896, answer=385:72720)
- Layer 38: `肤`, ` .`, ` germ`, ` crev`, `悬挂` (target ranks: base_value=91:95088, first_product=182:61078, bound_value=187:109247, second_product=374:108085, answer=385:77711)
- Layer 39: ` .`, ` .↵↵`, ` unflagged`, ` encomp`, ` germ` (target ranks: base_value=91:121539, first_product=182:80637, bound_value=187:95816, second_product=374:119201, answer=385:87351)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` germ` (target ranks: base_value=91:108714, first_product=182:63616, bound_value=187:80930, second_product=374:101072, answer=385:59114)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `圆圆`, `肤` (target ranks: base_value=91:53438, first_product=182:12838, bound_value=187:20159, second_product=374:35858, answer=385:12607)

### Filler position 49 (absolute token 851, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `datasetId`, `�乐` (target ranks: base_value=91:127557, first_product=182:127165, bound_value=187:127002, second_product=374:125386, answer=385:128172)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=91:11121, first_product=182:23470, bound_value=187:21406, second_product=374:25776, answer=385:23526)
- Layer 20: ` licensierad`, `codeline`, ` instantaneous`, ` grounds`, ` originalet` (target ranks: base_value=91:94484, first_product=182:78252, bound_value=187:48869, second_product=374:83374, answer=385:100507)
- Layer 30: ` Answer`, `答案是`, ` ответ`, ` Antwort`, `答案` (target ranks: base_value=91:114707, first_product=182:84458, bound_value=187:108322, second_product=374:107694, answer=385:102832)
- Layer 35: ` Answer`, `codeline`, `AED`, ` Antwort`, ` answer` (target ranks: base_value=91:92896, first_product=182:85483, bound_value=187:110434, second_product=374:95241, answer=385:124321)
- Layer 36: ` Answer`, `沉思`, `坏`, ` answer`, `停` (target ranks: base_value=91:22260, first_product=182:40509, bound_value=187:74099, second_product=374:49164, answer=385:99295)
- Layer 37: `oNames`, `codeline`, `insic`, `orbic`, ` consum` (target ranks: base_value=91:88932, first_product=182:87058, bound_value=187:121875, second_product=374:95181, answer=385:108964)
- Layer 38: `oNames`, ` retard`, `<|EOT|>`, `园的`, `оду` (target ranks: base_value=91:99208, first_product=182:90871, bound_value=187:118658, second_product=374:96180, answer=385:97709)
- Layer 39: ` unflagged`, `�`, `deen`, `oxygen`, ` dú` (target ranks: base_value=91:100138, first_product=182:93160, bound_value=187:107855, second_product=374:76419, answer=385:66668)
- Layer 40: ` .`, ` .↵↵`, ` Answer`, ` nasod`, ` unflagged` (target ranks: base_value=91:34330, first_product=182:65394, bound_value=187:52664, second_product=374:31215, answer=385:26643)
- Layer 41: ` .`, ` .↵↵`, ` Answer`, `叮`, `Answer` (target ranks: base_value=91:17276, first_product=182:14205, bound_value=187:20649, second_product=374:10460, answer=385:17334)

### Filler position 50 (absolute token 852, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=91:122019, first_product=182:111850, bound_value=187:112062, second_product=374:112006, answer=385:112577)
- Layer 10: `EDMF`, ` dével`, `-ulo`, ` поха`, `�乐` (target ranks: base_value=91:127474, first_product=182:116557, bound_value=187:121291, second_product=374:119172, answer=385:112110)
- Layer 20: `能被`, `ait`, `忑`, `Sequ`, `坷` (target ranks: base_value=91:7320, first_product=182:52976, bound_value=187:34812, second_product=374:40379, answer=385:47766)
- Layer 30: ` talags`, `CopyWith`, ` mosunod`, ` dátummal`, ` unflagged` (target ranks: base_value=91:81167, first_product=182:64801, bound_value=187:20982, second_product=374:6715, answer=385:12576)
- Layer 35: `759`, `七百`, `755`, `751`, `775` (target ranks: base_value=91:113657, first_product=182:128982, bound_value=187:75538, second_product=374:224, answer=385:307)
- Layer 36: `775`, `755`, `759`, `七百`, `751` (target ranks: base_value=91:113550, first_product=182:128111, bound_value=187:49324, second_product=374:200, answer=385:179)
- Layer 37: `775`, `七百`, `755`, `751`, `759` (target ranks: base_value=91:123709, first_product=182:127947, bound_value=187:73764, second_product=374:479, answer=385:384)
- Layer 38: `775`, `765`, `755`, `767`, `759` (target ranks: base_value=91:122916, first_product=182:127735, bound_value=187:83742, second_product=374:4307, answer=385:593)
- Layer 39: ` Clay`, `书馆`, `775`, `UIT`, `八百` (target ranks: base_value=91:126570, first_product=182:127706, bound_value=187:70029, second_product=374:73501, answer=385:5413)
- Layer 40: ` Answer`, `Answer`, ` answer`, `答`, `_answer` (target ranks: base_value=91:125311, first_product=182:115593, bound_value=187:88675, second_product=374:71967, answer=385:31611)
- Layer 41: `Answer`, ` Answer`, ` answer`, `_answer`, `answer` (target ranks: base_value=91:54576, first_product=182:49182, bound_value=187:16375, second_product=374:48462, answer=385:13860)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>yav = 67
vif = 91
miy = twice the number for vif plus 5
yir = twice the number for miy plus 25
duf = twice the number for yir plus 19
Question: What is twice the number for miy plus 11?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
