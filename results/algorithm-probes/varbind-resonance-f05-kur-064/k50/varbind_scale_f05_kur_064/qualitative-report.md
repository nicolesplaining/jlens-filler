# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `235` (correct).
- No-filler answer: `229` (incorrect).
- Filler tokens: 50 tokens at absolute indices 792–841.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=64` | 1 (L23, filler 44) | L22, filler 1 (rank 10) |
| J-Lens | `first_product=128` | 72 (L36, filler 22) | Never |
| J-Lens | `bound_value=125` | 1 (L31, filler 13) | L30, filler 13 (rank 2) |
| J-Lens | `second_product=250` | 1 (L32, filler 43) | L31, filler 43 (rank 2) |
| J-Lens | `answer=235` | 1 (L31, filler 14) | L31, filler 14 (rank 1) |
| Logit lens | `base_value=64` | 1 (L25, filler 1) | L24, filler 1 (rank 6) |
| Logit lens | `first_product=128` | 35 (L29, filler 40) | Never |
| Logit lens | `bound_value=125` | 1 (L31, filler 13) | L29, filler 40 (rank 8) |
| Logit lens | `second_product=250` | 1 (L32, filler 43) | L31, filler 43 (rank 2) |
| Logit lens | `answer=235` | 1 (L31, filler 14) | L31, filler 14 (rank 1) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 792, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=64:119242, first_product=128:114621, bound_value=125:112740, second_product=250:117543, answer=235:115374)
- Layer 10: `anta`, `hook`, `fine`, ` kinain`, `Hook` (target ranks: base_value=64:97874, first_product=128:81963, bound_value=125:80139, second_product=250:75721, answer=235:95746)
- Layer 20: `足`, `扣`, `重`, `表面`, `期望` (target ranks: base_value=64:222, first_product=128:13939, bound_value=125:9777, second_product=250:20263, answer=235:17569)
- Layer 30: `69`, `65`, `93`, `68`, `97` (target ranks: base_value=64:56, first_product=128:19184, bound_value=125:7344, second_product=250:57802, answer=235:16223)
- Layer 35: `acin`, `185`, ` Heim`, `85`, `泳` (target ranks: base_value=64:4925, first_product=128:90504, bound_value=125:20869, second_product=250:71614, answer=235:1096)
- Layer 36: `185`, `85`, `173`, `165`, `169` (target ranks: base_value=64:29006, first_product=128:117911, bound_value=125:20397, second_product=250:103998, answer=235:220)
- Layer 37: `185`, `زياح`, `165`, `祭`, `173` (target ranks: base_value=64:58319, first_product=128:120990, bound_value=125:12110, second_product=250:108086, answer=235:317)
- Layer 38: `185`, ` Nixon`, `故宫`, ` talags`, `}<?` (target ranks: base_value=64:119302, first_product=128:126388, bound_value=125:31641, second_product=250:116129, answer=235:715)
- Layer 39: `185`, ` NFT`, `ocyst`, `干`, ` Nij` (target ranks: base_value=64:93903, first_product=128:126467, bound_value=125:70296, second_product=250:120750, answer=235:9130)
- Layer 40: ` talags`, ` ld`, ` LD`, `实在`, ` ald` (target ranks: base_value=64:34487, first_product=128:105993, bound_value=125:35349, second_product=250:86783, answer=235:7179)
- Layer 41: ` .`, `NET`, ` .↵↵`, ` .↵`, `net` (target ranks: base_value=64:90194, first_product=128:116611, bound_value=125:73849, second_product=250:72659, answer=235:35950)

### Filler position 2 (absolute token 793, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=64:121549, first_product=128:118827, bound_value=125:118134, second_product=250:120684, answer=235:119221)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `挪` (target ranks: base_value=64:19062, first_product=128:35114, bound_value=125:33606, second_product=250:31551, answer=235:30884)
- Layer 20: ` .----`, `往常`, `oraly`, ` Millenniums`, `ools` (target ranks: base_value=64:125665, first_product=128:128796, bound_value=125:126396, second_product=250:127965, answer=235:123883)
- Layer 30: ` talags`, ` dekameters`, ` hilabihan`, ` pakig`, ` gilay` (target ranks: base_value=64:121125, first_product=128:123873, bound_value=125:120117, second_product=250:128951, answer=235:112225)
- Layer 35: ` hilabihan`, ` pakig`, ` .`, ` talags`, `滴水` (target ranks: base_value=64:124942, first_product=128:126371, bound_value=125:119532, second_product=250:128093, answer=235:119738)
- Layer 36: ` talags`, ` hilabihan`, ` nasod`, ` tall`, `enclose` (target ranks: base_value=64:89247, first_product=128:102419, bound_value=125:89762, second_product=250:118278, answer=235:93858)
- Layer 37: `}<?`, ` Erkännande`, ` hilabihan`, ` licensierad`, `aplenty` (target ranks: base_value=64:126207, first_product=128:121878, bound_value=125:102202, second_product=250:127095, answer=235:118695)
- Layer 38: ` .`, ` Erkännande`, `}<?`, ` nasod`, ` hilabihan` (target ranks: base_value=64:116099, first_product=128:103697, bound_value=125:67626, second_product=250:124289, answer=235:107330)
- Layer 39: ` .`, ` hilabihan`, ` talags`, `}<?`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=64:120303, first_product=128:101838, bound_value=125:30958, second_product=250:118211, answer=235:83964)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, `忏` (target ranks: base_value=64:59880, first_product=128:46546, bound_value=125:2786, second_product=250:77943, answer=235:44836)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `忏` (target ranks: base_value=64:16615, first_product=128:23247, bound_value=125:403, second_product=250:26558, answer=235:11271)

### Filler position 3 (absolute token 794, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125063, first_product=128:120843, bound_value=125:120178, second_product=250:122685, answer=235:120968)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:16949, first_product=128:26910, bound_value=125:27569, second_product=250:26545, answer=235:25751)
- Layer 20: `ait`, `ative`, `忑`, `tas`, `cape` (target ranks: base_value=64:4079, first_product=128:29708, bound_value=125:18117, second_product=250:37182, answer=235:21593)
- Layer 30: `vari`, ` repetition`, ` variable`, `保持一致`, ` repetitions` (target ranks: base_value=64:20389, first_product=128:89206, bound_value=125:86971, second_product=250:108952, answer=235:100171)
- Layer 35: ` puzzle`, ` var`, ` variable`, ` puzzles`, ` variables` (target ranks: base_value=64:10901, first_product=128:84693, bound_value=125:100306, second_product=250:94175, answer=235:87592)
- Layer 36: ` puzzle`, ` definitions`, ` puzzles`, ` variables`, `变量的` (target ranks: base_value=64:19089, first_product=128:88173, bound_value=125:109206, second_product=250:101841, answer=235:104367)
- Layer 37: `variables`, `变量的`, ` variables`, `Variables`, ` puzzle` (target ranks: base_value=64:76588, first_product=128:113949, bound_value=125:123691, second_product=250:120716, answer=235:121485)
- Layer 38: `variables`, `}<?`, `变量的`, `混乱`, ` puzzle` (target ranks: base_value=64:89406, first_product=128:121297, bound_value=125:126900, second_product=250:124028, answer=235:117659)
- Layer 39: `script`, `笔墨`, `osos`, `文字的`, `erer` (target ranks: base_value=64:84415, first_product=128:118606, bound_value=125:111819, second_product=250:123419, answer=235:118715)
- Layer 40: ` dotted`, `akak`, ` dummy`, ` `, ` interd` (target ranks: base_value=64:27968, first_product=128:93607, bound_value=125:51529, second_product=250:104158, answer=235:115986)
- Layer 41: ` .`, ` dotted`, `<｜end▁of▁sentence｜>`, ` `, ` without` (target ranks: base_value=64:26397, first_product=128:50952, bound_value=125:14113, second_product=250:65226, answer=235:77310)

### Filler position 4 (absolute token 795, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125795, first_product=128:122707, bound_value=125:122079, second_product=250:124013, answer=235:122644)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=64:14085, first_product=128:23549, bound_value=125:23730, second_product=250:20691, answer=235:21323)
- Layer 20: `ait`, `cape`, `挪`, `atile`, `锁定` (target ranks: base_value=64:7328, first_product=128:44303, bound_value=125:37126, second_product=250:46370, answer=235:36855)
- Layer 30: ` Niagara`, `tap`, `Tap`, ` tap`, `acos` (target ranks: base_value=64:91718, first_product=128:118394, bound_value=125:121760, second_product=250:125880, answer=235:121574)
- Layer 35: ` tap`, ` Niagara`, `Tap`, ` dynam`, `tap` (target ranks: base_value=64:69717, first_product=128:121708, bound_value=125:121812, second_product=250:121411, answer=235:120199)
- Layer 36: ` dynam`, `动态`, ` tap`, `提问`, `期望` (target ranks: base_value=64:35181, first_product=128:106359, bound_value=125:101796, second_product=250:106900, answer=235:110175)
- Layer 37: ` dynam`, `oug`, `打磨`, ` talags`, `ERG` (target ranks: base_value=64:68394, first_product=128:116746, bound_value=125:106500, second_product=250:116914, answer=235:119110)
- Layer 38: ` talags`, `本题分析`, `zyw`, `东海`, `打磨` (target ranks: base_value=64:91050, first_product=128:124609, bound_value=125:118283, second_product=250:122626, answer=235:123779)
- Layer 39: ` Nij`, ` talags`, `oug`, `本题分析`, `东海` (target ranks: base_value=64:68134, first_product=128:125367, bound_value=125:103467, second_product=250:120049, answer=235:120451)
- Layer 40: ` talags`, `oug`, `Question`, ` Question`, `pon` (target ranks: base_value=64:40700, first_product=128:115766, bound_value=125:68434, second_product=250:104680, answer=235:113194)
- Layer 41: ` .`, `Question`, ` Question`, `提问`, `试一试` (target ranks: base_value=64:16305, first_product=128:62859, bound_value=125:23780, second_product=250:60005, answer=235:84068)

### Filler position 5 (absolute token 796, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125593, first_product=128:123024, bound_value=125:122427, second_product=250:123948, answer=235:122876)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:15755, first_product=128:25954, bound_value=125:26955, second_product=250:22866, answer=235:23775)
- Layer 20: `挪`, `锁定`, `幽`, `cape`, ` LS` (target ranks: base_value=64:13790, first_product=128:38131, bound_value=125:36109, second_product=250:42000, answer=235:40776)
- Layer 30: ` rip`, `�`, ` tap`, `Tap`, ` tear` (target ranks: base_value=64:40087, first_product=128:108419, bound_value=125:117520, second_product=250:119844, answer=235:115665)
- Layer 35: ` tap`, ` rip`, `Tap`, `�`, `acin` (target ranks: base_value=64:58033, first_product=128:110449, bound_value=125:119328, second_product=250:112833, answer=235:116599)
- Layer 36: ` rip`, ` drip`, ` tap`, ` zad`, `acin` (target ranks: base_value=64:58707, first_product=128:105246, bound_value=125:109529, second_product=250:102658, answer=235:113983)
- Layer 37: ` Nij`, `zim`, `覆`, ` rip`, `zat` (target ranks: base_value=64:101305, first_product=128:116672, bound_value=125:118639, second_product=250:114519, answer=235:122134)
- Layer 38: `zat`, `zyw`, `}<?`, `�`, `覆` (target ranks: base_value=64:106732, first_product=128:119199, bound_value=125:114829, second_product=250:121392, answer=235:123253)
- Layer 39: `wof`, ` Nij`, `�`, `}<?`, `zat` (target ranks: base_value=64:101700, first_product=128:122716, bound_value=125:114986, second_product=250:121146, answer=235:119786)
- Layer 40: `wof`, ` rip`, `zim`, ` talags`, ` fum` (target ranks: base_value=64:83263, first_product=128:102762, bound_value=125:99557, second_product=250:109883, answer=235:116240)
- Layer 41: `坏`, `我怎么`, ` fum`, `zel`, ` .` (target ranks: base_value=64:58017, first_product=128:38735, bound_value=125:45822, second_product=250:66129, answer=235:57966)

### Filler position 6 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125021, first_product=128:122450, bound_value=125:121815, second_product=250:123202, answer=235:122316)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13749, first_product=128:22717, bound_value=125:24276, second_product=250:21163, answer=235:21557)
- Layer 20: ` unflagged`, `替换`, ` corrected`, `答案是`, `答案` (target ranks: base_value=64:101612, first_product=128:104112, bound_value=125:116563, second_product=250:112121, answer=235:110038)
- Layer 30: ` step`, ` Tw`, `高明`, `推算`, ` resolve` (target ranks: base_value=64:86247, first_product=128:63567, bound_value=125:64923, second_product=250:85709, answer=235:111139)
- Layer 35: ` Tw`, `Tw`, ` tw`, `tw`, ` step` (target ranks: base_value=64:38797, first_product=128:34752, bound_value=125:42209, second_product=250:36775, answer=235:78269)
- Layer 36: ` Tw`, `Tw`, ` tw`, `tw`, `.tw` (target ranks: base_value=64:53246, first_product=128:31571, bound_value=125:38324, second_product=250:39333, answer=235:87898)
- Layer 37: ` Tw`, `Tw`, `tw`, ` tw`, ` TW` (target ranks: base_value=64:66166, first_product=128:50268, bound_value=125:65951, second_product=250:50712, answer=235:111139)
- Layer 38: ` Tw`, `Tw`, `tw`, ` tw`, ` TW` (target ranks: base_value=64:78808, first_product=128:66718, bound_value=125:69700, second_product=250:63583, answer=235:109059)
- Layer 39: ` nasod`, `klar`, ` Tw`, `�`, ` Dominic` (target ranks: base_value=64:98187, first_product=128:82267, bound_value=125:93355, second_product=250:123598, answer=235:126839)
- Layer 40: ` x`, ` nasod`, `klar`, `kus`, `kur` (target ranks: base_value=64:65772, first_product=128:73983, bound_value=125:77324, second_product=250:122393, answer=235:125022)
- Layer 41: `<｜begin▁of▁file｜>`, `那两个`, ` .`, `工作任务`, `癫�` (target ranks: base_value=64:104826, first_product=128:99385, bound_value=125:103834, second_product=250:120740, answer=235:126181)

### Filler position 7 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125156, first_product=128:122396, bound_value=125:121780, second_product=250:123082, answer=235:122234)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13222, first_product=128:23225, bound_value=125:24619, second_product=250:21627, answer=235:22157)
- Layer 20: `锁定`, `ait`, `挪`, `鞍`, ` smile` (target ranks: base_value=64:7100, first_product=128:21679, bound_value=125:22363, second_product=250:27966, answer=235:24402)
- Layer 30: ` calculator`, `鞍`, `calculator`, `calcul`, ` riv` (target ranks: base_value=64:598, first_product=128:12404, bound_value=125:8679, second_product=250:29761, answer=235:3854)
- Layer 35: `保留`, `鞍`, ` labor`, ` smile`, `acks` (target ranks: base_value=64:452, first_product=128:12004, bound_value=125:4487, second_product=250:14976, answer=235:4060)
- Layer 36: `acin`, `保留`, `calcul`, `退出`, `特` (target ranks: base_value=64:2129, first_product=128:13527, bound_value=125:3438, second_product=250:22118, answer=235:3326)
- Layer 37: `}<?`, ` pakig`, `ocyst`, `radesh`, ` talags` (target ranks: base_value=64:16843, first_product=128:38814, bound_value=125:4969, second_product=250:43657, answer=235:2241)
- Layer 38: `}<?`, `ocyst`, `aharan`, `apper`, `思想的` (target ranks: base_value=64:62323, first_product=128:71679, bound_value=125:12770, second_product=250:67811, answer=235:5657)
- Layer 39: `}<?`, `ocyst`, `aharan`, `叶子`, `糊涂` (target ranks: base_value=64:122236, first_product=128:128579, bound_value=125:89082, second_product=250:107233, answer=235:8668)
- Layer 40: ` talags`, `留存`, `银杏`, `ocyst`, `期待的` (target ranks: base_value=64:117695, first_product=128:128497, bound_value=125:92916, second_product=250:116300, answer=235:9282)
- Layer 41: `留存`, ` .`, `秆`, `李克`, `))))` (target ranks: base_value=64:107862, first_product=128:127829, bound_value=125:83302, second_product=250:105231, answer=235:13018)

### Filler position 8 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124766, first_product=128:122044, bound_value=125:121374, second_product=250:122780, answer=235:121913)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11499, first_product=128:21648, bound_value=125:22658, second_product=250:20242, answer=235:20835)
- Layer 20: `ait`, `锁定`, `挪`, ` Walker`, `us` (target ranks: base_value=64:8038, first_product=128:26560, bound_value=125:25883, second_product=250:37731, answer=235:33391)
- Layer 30: ` Kur`, ` kur`, `kur`, ` Kuro`, ` Kurdish` (target ranks: base_value=64:4355, first_product=128:105082, bound_value=125:103081, second_product=250:111097, answer=235:117479)
- Layer 35: ` Kur`, ` kur`, `kur`, ` Kurdish`, ` Kuro` (target ranks: base_value=64:1676, first_product=128:78892, bound_value=125:65665, second_product=250:59195, answer=235:91760)
- Layer 36: ` Kur`, ` kur`, `kur`, ` Kurdish`, `留存` (target ranks: base_value=64:2045, first_product=128:56665, bound_value=125:60659, second_product=250:52816, answer=235:88106)
- Layer 37: ` Kur`, ` kur`, `kur`, ` Kurs`, ` kurs` (target ranks: base_value=64:15386, first_product=128:94444, bound_value=125:97568, second_product=250:91844, answer=235:109195)
- Layer 38: ` Kur`, ` kur`, `kur`, `}<?`, ` Kurs` (target ranks: base_value=64:26320, first_product=128:110728, bound_value=125:107461, second_product=250:105531, answer=235:110330)
- Layer 39: ` Kur`, `}<?`, ` kur`, `kur`, `urin` (target ranks: base_value=64:56806, first_product=128:105681, bound_value=125:104496, second_product=250:118709, answer=235:113689)
- Layer 40: ` talags`, ` kur`, `kur`, `留存`, ` pakig` (target ranks: base_value=64:15919, first_product=128:75043, bound_value=125:75472, second_product=250:116332, answer=235:99976)
- Layer 41: ` kur`, ` .`, `kur`, `转载请`, ` talags` (target ranks: base_value=64:17614, first_product=128:36527, bound_value=125:31730, second_product=250:78465, answer=235:63829)

### Filler position 9 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124994, first_product=128:122410, bound_value=125:121715, second_product=250:123117, answer=235:122276)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11884, first_product=128:22440, bound_value=125:23461, second_product=250:20623, answer=235:21412)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, ` smile` (target ranks: base_value=64:9654, first_product=128:33645, bound_value=125:30992, second_product=250:34005, answer=235:34038)
- Layer 30: ` var`, `直接`, ` variable`, ` tap`, `输入的` (target ranks: base_value=64:23850, first_product=128:90234, bound_value=125:79823, second_product=250:100450, answer=235:83369)
- Layer 35: ` var`, ` variable`, `锁定`, ` reserved`, `acin` (target ranks: base_value=64:10942, first_product=128:65998, bound_value=125:69201, second_product=250:76043, answer=235:63114)
- Layer 36: ` directly`, `直接`, `Direct`, ` direct`, `acin` (target ranks: base_value=64:23197, first_product=128:65580, bound_value=125:78145, second_product=250:84181, answer=235:74717)
- Layer 37: `简单`, ` variables`, `Variables`, `variables`, `变量的` (target ranks: base_value=64:59710, first_product=128:85554, bound_value=125:99672, second_product=250:108657, answer=235:86211)
- Layer 38: `简单`, ` variables`, `}<?`, `Variables`, `变量的` (target ranks: base_value=64:69104, first_product=128:96160, bound_value=125:96191, second_product=250:115716, answer=235:86812)
- Layer 39: `}<?`, `树叶`, `acons`, `迷惑`, `hemer` (target ranks: base_value=64:69126, first_product=128:79649, bound_value=125:88789, second_product=250:124103, answer=235:107475)
- Layer 40: `acl`, `殿堂`, `kur`, `šk`, `amn` (target ranks: base_value=64:23704, first_product=128:59427, bound_value=125:43765, second_product=250:117627, answer=235:106472)
- Layer 41: ` .`, `kur`, ` kur`, `简单`, `毕竟` (target ranks: base_value=64:13616, first_product=128:31924, bound_value=125:23904, second_product=250:88859, answer=235:65527)

### Filler position 10 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124930, first_product=128:122489, bound_value=125:121770, second_product=250:123204, answer=235:122442)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11684, first_product=128:22497, bound_value=125:23693, second_product=250:20124, answer=235:21462)
- Layer 20: `ait`, ` Walker`, `能被`, `挪`, `Walker` (target ranks: base_value=64:11721, first_product=128:43302, bound_value=125:40380, second_product=250:38393, answer=235:42908)
- Layer 30: `64`, `鞍`, `洋`, `拆`, ` dy` (target ranks: base_value=64:1, first_product=128:593, bound_value=125:357, second_product=250:24920, answer=235:53926)
- Layer 35: `125`, ` dig`, ` strike`, ` smile`, ` Kaw` (target ranks: base_value=64:23, first_product=128:3166, bound_value=125:1, second_product=250:960, answer=235:54682)
- Layer 36: `125`, `计算方法`, `去掉`, `空了`, ` Wil` (target ranks: base_value=64:895, first_product=128:4487, bound_value=125:1, second_product=250:30, answer=235:76294)
- Layer 37: `125`, `}<?`, `otis`, `计算方法`, `Quintal` (target ranks: base_value=64:6481, first_product=128:9969, bound_value=125:1, second_product=250:102, answer=235:92094)
- Layer 38: `125`, `}<?`, `叶子`, `师徒`, `取了` (target ranks: base_value=64:21620, first_product=128:19503, bound_value=125:1, second_product=250:443, answer=235:100401)
- Layer 39: `125`, `}<?`, `otis`, `acons`, `-ulo` (target ranks: base_value=64:39509, first_product=128:45051, bound_value=125:1, second_product=250:5725, answer=235:75731)
- Layer 40: `125`, ` kur`, `kten`, ` tal`, `šk` (target ranks: base_value=64:32431, first_product=128:27651, bound_value=125:1, second_product=250:4023, answer=235:44360)
- Layer 41: `125`, ` .`, `试一试`, ` tal`, `没有被` (target ranks: base_value=64:39711, first_product=128:23600, bound_value=125:1, second_product=250:1468, answer=235:31795)

### Filler position 11 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124943, first_product=128:122608, bound_value=125:121912, second_product=250:123341, answer=235:122626)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11597, first_product=128:22918, bound_value=125:24104, second_product=250:20293, answer=235:21745)
- Layer 20: `ait`, `锁定`, ` Walker`, ` smile`, `拆` (target ranks: base_value=64:13405, first_product=128:49423, bound_value=125:42128, second_product=250:43134, answer=235:44844)
- Layer 30: `第一步`, `算出`, ` calculate`, `计算`, `计算出` (target ranks: base_value=64:16686, first_product=128:89329, bound_value=125:91542, second_product=250:91586, answer=235:90524)
- Layer 35: `第一步`, ` Tw`, ` calculate`, `calcul`, `算出` (target ranks: base_value=64:6950, first_product=128:54977, bound_value=125:72211, second_product=250:57829, answer=235:75552)
- Layer 36: `第一步`, `calcul`, ` first`, ` calculate`, `计算` (target ranks: base_value=64:12997, first_product=128:52239, bound_value=125:76699, second_product=250:60032, answer=235:85182)
- Layer 37: `calcul`, `计算`, `计算的`, ` calculations`, `計算` (target ranks: base_value=64:22022, first_product=128:66065, bound_value=125:98763, second_product=250:93217, answer=235:102952)
- Layer 38: `}<?`, `calcul`, `的计算`, ` cál`, ` calculations` (target ranks: base_value=64:43520, first_product=128:96073, bound_value=125:109743, second_product=250:110279, answer=235:115176)
- Layer 39: `东海`, `}<?`, `ocyst`, `�`, `opters` (target ranks: base_value=64:60591, first_product=128:80672, bound_value=125:98896, second_product=250:116196, answer=235:113169)
- Layer 40: ` nasod`, `不急`, `amd`, `šk`, `殿堂` (target ranks: base_value=64:14083, first_product=128:49209, bound_value=125:49445, second_product=250:98421, answer=235:105761)
- Layer 41: ` .`, `鹉`, `叮`, `šk`, `kir` (target ranks: base_value=64:1375, first_product=128:7623, bound_value=125:8628, second_product=250:29999, answer=235:60231)

### Filler position 12 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124594, first_product=128:122438, bound_value=125:121780, second_product=250:123175, answer=235:122547)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11250, first_product=128:22113, bound_value=125:23808, second_product=250:20460, answer=235:21493)
- Layer 20: `ait`, `锁定`, ` Walker`, `atable`, `挪` (target ranks: base_value=64:3964, first_product=128:22024, bound_value=125:21202, second_product=250:23689, answer=235:24190)
- Layer 30: ` Pop`, ` pop`, `75`, `67`, `泳` (target ranks: base_value=64:272, first_product=128:22420, bound_value=125:2751, second_product=250:7785, answer=235:2260)
- Layer 35: `185`, `退出`, ` Heim`, `225`, `85` (target ranks: base_value=64:6762, first_product=128:54866, bound_value=125:897, second_product=250:487, answer=235:7)
- Layer 36: `185`, `235`, `85`, `181`, `385` (target ranks: base_value=64:73436, first_product=128:85047, bound_value=125:6898, second_product=250:9657, answer=235:2)
- Layer 37: `185`, `235`, `181`, `225`, ` Parehong` (target ranks: base_value=64:101432, first_product=128:85326, bound_value=125:3498, second_product=250:17164, answer=235:2)
- Layer 38: `185`, `235`, `}<?`, ` markup`, `225` (target ranks: base_value=64:128318, first_product=128:126942, bound_value=125:34906, second_product=250:29824, answer=235:2)
- Layer 39: `185`, `本题分析`, `zat`, `olars`, `235` (target ranks: base_value=64:127456, first_product=128:128423, bound_value=125:110673, second_product=250:112019, answer=235:5)
- Layer 40: `185`, ` talags`, `脑筋`, ` kinahabogang`, `acular` (target ranks: base_value=64:121535, first_product=128:126693, bound_value=125:70715, second_product=250:84529, answer=235:6)
- Layer 41: `相比之下`, ` talags`, `))))`, `185`, ` .` (target ranks: base_value=64:103792, first_product=128:113475, bound_value=125:30930, second_product=250:44629, answer=235:43)

### Filler position 13 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124829, first_product=128:122527, bound_value=125:121862, second_product=250:123209, answer=235:122594)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11292, first_product=128:21962, bound_value=125:23615, second_product=250:19894, answer=235:21383)
- Layer 20: ` Walker`, `能被`, `Walker`, `ait`, `忑` (target ranks: base_value=64:9184, first_product=128:32884, bound_value=125:37540, second_product=250:37982, answer=235:36549)
- Layer 30: `鞍`, `125`, ` receptive`, `二十五`, ` Heim` (target ranks: base_value=64:155, first_product=128:662, bound_value=125:2, second_product=250:4196, answer=235:34703)
- Layer 35: `125`, `250`, `二十五`, `25`, ` dilat` (target ranks: base_value=64:37110, first_product=128:22046, bound_value=125:1, second_product=250:2, answer=235:7241)
- Layer 36: `125`, `250`, `二十五`, ` Lange`, `25` (target ranks: base_value=64:101010, first_product=128:24322, bound_value=125:1, second_product=250:2, answer=235:12305)
- Layer 37: `125`, `250`, `二十五`, `?datasetId`, `}<?` (target ranks: base_value=64:123069, first_product=128:32795, bound_value=125:1, second_product=250:2, answer=235:13950)
- Layer 38: `125`, `250`, `?datasetId`, `-ulo`, `cault` (target ranks: base_value=64:127851, first_product=128:68866, bound_value=125:1, second_product=250:2, answer=235:11197)
- Layer 39: `125`, `-ulo`, `250`, `}<?`, `aharan` (target ranks: base_value=64:105077, first_product=128:112424, bound_value=125:1, second_product=250:3, answer=235:31919)
- Layer 40: `125`, `omit`, `留存`, `acl`, `250` (target ranks: base_value=64:80571, first_product=128:96241, bound_value=125:1, second_product=250:5, answer=235:5325)
- Layer 41: ` .`, `omit`, `没有被`, `125`, ` number` (target ranks: base_value=64:83293, first_product=128:82913, bound_value=125:4, second_product=250:24, answer=235:6972)

### Filler position 14 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124726, first_product=128:122321, bound_value=125:121573, second_product=250:122948, answer=235:122250)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10609, first_product=128:21965, bound_value=125:23088, second_product=250:19339, answer=235:20706)
- Layer 20: `锁定`, `ait`, `能被`, ` LS`, ` Walker` (target ranks: base_value=64:1640, first_product=128:14793, bound_value=125:16983, second_product=250:17462, answer=235:14617)
- Layer 30: `67`, ` maximal`, ` pakig`, `65`, `acos` (target ranks: base_value=64:1208, first_product=128:15056, bound_value=125:344, second_product=250:2203, answer=235:200)
- Layer 35: `235`, `215`, `185`, ` smug`, `203` (target ranks: base_value=64:32985, first_product=128:107446, bound_value=125:5197, second_product=250:566, answer=235:1)
- Layer 36: `235`, ` talags`, `233`, `185`, ` pakig` (target ranks: base_value=64:84007, first_product=128:56774, bound_value=125:14695, second_product=250:11966, answer=235:1)
- Layer 37: `235`, `185`, ` talags`, `内膜`, ` Parehong` (target ranks: base_value=64:94229, first_product=128:45377, bound_value=125:3270, second_product=250:7648, answer=235:1)
- Layer 38: `235`, `185`, `三十五`, `233`, ` ninete` (target ranks: base_value=64:127801, first_product=128:109649, bound_value=125:23224, second_product=250:30416, answer=235:1)
- Layer 39: `235`, `本题分析`, `185`, `233`, `金星` (target ranks: base_value=64:127203, first_product=128:127367, bound_value=125:76772, second_product=250:102878, answer=235:1)
- Layer 40: `235`, ` talags`, `<｜begin▁of▁file｜>`, `185`, `187` (target ranks: base_value=64:123521, first_product=128:124579, bound_value=125:9886, second_product=250:52302, answer=235:1)
- Layer 41: `235`, `))))`, ` talags`, ` .`, `185` (target ranks: base_value=64:84203, first_product=128:99626, bound_value=125:4121, second_product=250:14221, answer=235:1)

### Filler position 15 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124994, first_product=128:122635, bound_value=125:121939, second_product=250:123339, answer=235:122631)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10449, first_product=128:21774, bound_value=125:22861, second_product=250:19149, answer=235:20251)
- Layer 20: `锁定`, `ait`, ` future`, ` smile`, `能被` (target ranks: base_value=64:2215, first_product=128:16500, bound_value=125:16410, second_product=250:18668, answer=235:14359)
- Layer 30: `65`, `acos`, `67`, `acin`, `75` (target ranks: base_value=64:586, first_product=128:16958, bound_value=125:631, second_product=250:4752, answer=235:329)
- Layer 35: `185`, `225`, `235`, `205`, `退出` (target ranks: base_value=64:14852, first_product=128:76194, bound_value=125:491, second_product=250:330, answer=235:3)
- Layer 36: `185`, ` Parehong`, `235`, `85`, `金石` (target ranks: base_value=64:69923, first_product=128:71961, bound_value=125:4528, second_product=250:5552, answer=235:3)
- Layer 37: `185`, ` Parehong`, ` dirty`, `235`, `}<?` (target ranks: base_value=64:93636, first_product=128:66472, bound_value=125:2223, second_product=250:11444, answer=235:4)
- Layer 38: `185`, `235`, `本题分析`, ` markup`, `}<?` (target ranks: base_value=64:128324, first_product=128:123491, bound_value=125:24712, second_product=250:33843, answer=235:2)
- Layer 39: `185`, `本题分析`, ` dirty`, `235`, `zat` (target ranks: base_value=64:127849, first_product=128:128042, bound_value=125:86161, second_product=250:99417, answer=235:4)
- Layer 40: `185`, `235`, `asted`, ` talags`, `187` (target ranks: base_value=64:121715, first_product=128:124951, bound_value=125:12879, second_product=250:43886, answer=235:2)
- Layer 41: `185`, ` .`, `))))`, ` guarante`, `相比之下` (target ranks: base_value=64:96967, first_product=128:112556, bound_value=125:7379, second_product=250:13810, answer=235:7)

### Filler position 16 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125202, first_product=128:122917, bound_value=125:122236, second_product=250:123599, answer=235:122940)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11231, first_product=128:22283, bound_value=125:23953, second_product=250:19486, answer=235:21043)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, ` smile` (target ranks: base_value=64:7456, first_product=128:30899, bound_value=125:30214, second_product=250:32079, answer=235:33399)
- Layer 30: `kur`, ` Kur`, ` kur`, ` Kaw`, `鞍` (target ranks: base_value=64:2771, first_product=128:83793, bound_value=125:74042, second_product=250:112022, answer=235:95528)
- Layer 35: `kur`, ` Kur`, ` kur`, ` Kaw`, `鞍` (target ranks: base_value=64:1030, first_product=128:55012, bound_value=125:41524, second_product=250:61057, answer=235:59224)
- Layer 36: ` Kur`, ` kur`, `kur`, ` Kaw`, `ikuha` (target ranks: base_value=64:1234, first_product=128:43417, bound_value=125:33817, second_product=250:51498, answer=235:65604)
- Layer 37: ` Kur`, ` kur`, `kur`, ` Kav`, ` KV` (target ranks: base_value=64:3438, first_product=128:63300, bound_value=125:60557, second_product=250:89378, answer=235:98534)
- Layer 38: ` Kur`, ` kur`, `kur`, ` Kav`, `东海` (target ranks: base_value=64:6684, first_product=128:75480, bound_value=125:57742, second_product=250:91315, answer=235:90307)
- Layer 39: ` Xavier`, ` Kur`, ` x`, ` X`, `xp` (target ranks: base_value=64:36274, first_product=128:77405, bound_value=125:56027, second_product=250:98778, answer=235:78980)
- Layer 40: ` kur`, ` x`, `kur`, ` Kur`, ` kinahabogang` (target ranks: base_value=64:3990, first_product=128:36091, bound_value=125:11842, second_product=250:51413, answer=235:26713)
- Layer 41: ` kur`, ` first`, `kur`, `第一步`, `留存` (target ranks: base_value=64:558, first_product=128:5114, bound_value=125:1207, second_product=250:8255, answer=235:6765)

### Filler position 17 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125339, first_product=128:123330, bound_value=125:122573, second_product=250:123950, answer=235:123361)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12572, first_product=128:23266, bound_value=125:25509, second_product=250:20626, answer=235:22504)
- Layer 20: `能被`, `距`, ` smile`, ` engaging`, ` Engaging` (target ranks: base_value=64:16441, first_product=128:38722, bound_value=125:42006, second_product=250:33901, answer=235:39278)
- Layer 30: ` twice`, ` Tw`, `Tw`, `tw`, `.tw` (target ranks: base_value=64:8, first_product=128:6948, bound_value=125:45554, second_product=250:74169, answer=235:57544)
- Layer 35: ` Tw`, ` twice`, `Tw`, `tw`, `.tw` (target ranks: base_value=64:6, first_product=128:6129, bound_value=125:41168, second_product=250:63520, answer=235:60737)
- Layer 36: ` Tw`, ` twice`, `分解`, `calcul`, `翻` (target ranks: base_value=64:10, first_product=128:3992, bound_value=125:50322, second_product=250:58969, answer=235:69385)
- Layer 37: ` doubling`, `}<?`, ` doubled`, ` doubles`, `isis` (target ranks: base_value=64:12, first_product=128:6557, bound_value=125:84645, second_product=250:98054, answer=235:103303)
- Layer 38: `}<?`, ` doubling`, `覆`, `东海`, `isis` (target ranks: base_value=64:102, first_product=128:23540, bound_value=125:99219, second_product=250:107304, answer=235:110742)
- Layer 39: `}<?`, `uerak`, `覆`, `东海`, ` doubling` (target ranks: base_value=64:4482, first_product=128:29304, bound_value=125:87079, second_product=250:98496, answer=235:100109)
- Layer 40: ` kur`, ` Kur`, `kur`, ` talags`, `翻` (target ranks: base_value=64:2352, first_product=128:14338, bound_value=125:12695, second_product=250:50581, answer=235:31746)
- Layer 41: ` kur`, ` .`, `kur`, `less`, ` ` (target ranks: base_value=64:2647, first_product=128:8775, bound_value=125:5932, second_product=250:16392, answer=235:28802)

### Filler position 18 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125466, first_product=128:123446, bound_value=125:122723, second_product=250:124128, answer=235:123507)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11699, first_product=128:22727, bound_value=125:25164, second_product=250:21013, answer=235:22043)
- Layer 20: `ait`, `忑`, ` Walker`, ` engaging`, `会成为` (target ranks: base_value=64:24687, first_product=128:51027, bound_value=125:49839, second_product=250:52031, answer=235:53049)
- Layer 30: `算出`, ` resolve`, ` resolves`, ` resolved`, ` calculate` (target ranks: base_value=64:18677, first_product=128:73443, bound_value=125:74322, second_product=250:89786, answer=235:97834)
- Layer 35: ` resolve`, ` resolves`, ` resolution`, ` resol`, ` calculator` (target ranks: base_value=64:9749, first_product=128:45351, bound_value=125:60885, second_product=250:59601, answer=235:77737)
- Layer 36: `calcul`, `分解`, `计算的`, ` calculator`, ` Calculators` (target ranks: base_value=64:9176, first_product=128:28584, bound_value=125:47055, second_product=250:46575, answer=235:69274)
- Layer 37: `calcul`, `计算的`, ` Calculators`, ` calcul`, `}<?` (target ranks: base_value=64:38898, first_product=128:51869, bound_value=125:76424, second_product=250:81927, answer=235:99095)
- Layer 38: `}<?`, ` RES`, `zat`, ` Calculators`, `calcul` (target ranks: base_value=64:54770, first_product=128:78600, bound_value=125:93365, second_product=250:101430, answer=235:98472)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `zat`, ` RES`, `殿堂` (target ranks: base_value=64:58555, first_product=128:41367, bound_value=125:58835, second_product=250:89244, answer=235:78355)
- Layer 40: `zat`, `殿堂`, `šk`, `acl`, `不急` (target ranks: base_value=64:12054, first_product=128:14727, bound_value=125:12741, second_product=250:54951, answer=235:65059)
- Layer 41: ` .`, ` without`, `不求`, ` `, ` sublim` (target ranks: base_value=64:5543, first_product=128:6876, bound_value=125:5096, second_product=250:19298, answer=235:34458)

### Filler position 19 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125341, first_product=128:123152, bound_value=125:122460, second_product=250:123872, answer=235:123365)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10791, first_product=128:21723, bound_value=125:23800, second_product=250:20172, answer=235:21202)
- Layer 20: `ait`, `忑`, ` Walker`, `锁定`, ` engaging` (target ranks: base_value=64:13659, first_product=128:42108, bound_value=125:40474, second_product=250:44181, answer=235:43202)
- Layer 30: ` Tw`, `Tw`, ` calculator`, `calculator`, `tw` (target ranks: base_value=64:9515, first_product=128:44815, bound_value=125:40626, second_product=250:69274, answer=235:65010)
- Layer 35: ` Tw`, `Tw`, `tw`, ` calculator`, ` tap` (target ranks: base_value=64:5372, first_product=128:33256, bound_value=125:35036, second_product=250:58250, answer=235:58960)
- Layer 36: ` Tw`, `Tw`, ` tap`, `翻`, ` Zad` (target ranks: base_value=64:5500, first_product=128:18194, bound_value=125:28245, second_product=250:49130, answer=235:58318)
- Layer 37: `}<?`, ` Tw`, `翻`, ` Zad`, ` sublim` (target ranks: base_value=64:30160, first_product=128:24920, bound_value=125:32483, second_product=250:70776, answer=235:77025)
- Layer 38: `}<?`, ` sublim`, `zat`, `翻`, ` Zad` (target ranks: base_value=64:48978, first_product=128:45280, bound_value=125:58428, second_product=250:94726, answer=235:103526)
- Layer 39: `}<?`, ` sublim`, `<｜begin▁of▁sentence｜>`, `东海`, `ozygous` (target ranks: base_value=64:54670, first_product=128:46665, bound_value=125:53359, second_product=250:105690, answer=235:94706)
- Layer 40: `}<?`, ` sublim`, `翻`, `acular`, ` nasod` (target ranks: base_value=64:7349, first_product=128:15819, bound_value=125:9660, second_product=250:70671, answer=235:63552)
- Layer 41: ` .`, ` `, `<｜end▁of▁sentence｜>`, ` ;`, ` sublim` (target ranks: base_value=64:2808, first_product=128:3837, bound_value=125:2873, second_product=250:30902, answer=235:20930)

### Filler position 20 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125507, first_product=128:123363, bound_value=125:122616, second_product=250:124032, answer=235:123459)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9941, first_product=128:20064, bound_value=125:22126, second_product=250:18861, answer=235:20050)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `Walker` (target ranks: base_value=64:8204, first_product=128:31426, bound_value=125:37652, second_product=250:38812, answer=235:34068)
- Layer 30: `算出`, `第一步`, `calcul`, `�`, `计算的` (target ranks: base_value=64:2103, first_product=128:59980, bound_value=125:73981, second_product=250:76857, answer=235:49202)
- Layer 35: ` calculator`, `calcul`, `第一步`, `分解`, `calculator` (target ranks: base_value=64:430, first_product=128:33359, bound_value=125:33719, second_product=250:31240, answer=235:30370)
- Layer 36: `calcul`, `留存`, ` calculator`, `算出`, `计算的` (target ranks: base_value=64:802, first_product=128:15368, bound_value=125:26598, second_product=250:27806, answer=235:34600)
- Layer 37: `calcul`, `}<?`, `计算的`, ` Calculators`, `计算方法` (target ranks: base_value=64:2227, first_product=128:20805, bound_value=125:47794, second_product=250:60587, answer=235:65349)
- Layer 38: `}<?`, `calcul`, ` Erkännande`, `计算方法`, `zat` (target ranks: base_value=64:4067, first_product=128:43747, bound_value=125:62175, second_product=250:67235, answer=235:67318)
- Layer 39: `}<?`, `ocyst`, `替换`, ` sublim`, `打磨` (target ranks: base_value=64:18861, first_product=128:59928, bound_value=125:73506, second_product=250:84218, answer=235:64633)
- Layer 40: `calcul`, `kur`, ` Tw`, ` twist`, ` kur` (target ranks: base_value=64:1532, first_product=128:19799, bound_value=125:20279, second_product=250:59310, answer=235:20956)
- Layer 41: ` twist`, ` `, ` Tw`, ` .`, `围观` (target ranks: base_value=64:1703, first_product=128:7747, bound_value=125:7048, second_product=250:29054, answer=235:9671)

### Filler position 21 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125903, first_product=128:123849, bound_value=125:123233, second_product=250:124490, answer=235:123842)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9673, first_product=128:20389, bound_value=125:22011, second_product=250:18624, answer=235:19855)
- Layer 20: `能被`, ` engaging`, `ait`, `距`, ` Walker` (target ranks: base_value=64:10459, first_product=128:38982, bound_value=125:40261, second_product=250:43926, answer=235:34619)
- Layer 30: `鞍`, ` receptive`, `释放`, ` dy`, `acos` (target ranks: base_value=64:52, first_product=128:1131, bound_value=125:197, second_product=250:11466, answer=235:25013)
- Layer 35: `250`, `二十五`, `125`, `俯`, `柿子` (target ranks: base_value=64:5333, first_product=128:28104, bound_value=125:3, second_product=250:1, answer=235:41986)
- Layer 36: `250`, `125`, ` Berl`, `俯`, ` Berlin` (target ranks: base_value=64:41527, first_product=128:25175, bound_value=125:2, second_product=250:1, answer=235:54329)
- Layer 37: `}<?`, `?datasetId`, `250`, `125`, ` smoothed` (target ranks: base_value=64:83987, first_product=128:43438, bound_value=125:4, second_product=250:3, answer=235:79982)
- Layer 38: `}<?`, `250`, `125`, ` smoothing`, ` Tub` (target ranks: base_value=64:94678, first_product=128:45216, bound_value=125:3, second_product=250:2, answer=235:64342)
- Layer 39: `}<?`, `acons`, `ocyst`, ` Spo`, `打包` (target ranks: base_value=64:51972, first_product=128:58030, bound_value=125:14, second_product=250:26, answer=235:15966)
- Layer 40: `ching`, `俯`, `125`, `250`, ` twisted` (target ranks: base_value=64:16886, first_product=128:25612, bound_value=125:3, second_product=250:4, answer=235:957)
- Layer 41: ` .`, ` `, `没有被`, `125`, `俯` (target ranks: base_value=64:16908, first_product=128:14153, bound_value=125:4, second_product=250:9, answer=235:791)

### Filler position 22 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125922, first_product=128:123969, bound_value=125:123351, second_product=250:124697, answer=235:124036)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9338, first_product=128:20629, bound_value=125:21849, second_product=250:18631, answer=235:19663)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, ` smile` (target ranks: base_value=64:6756, first_product=128:26752, bound_value=125:21496, second_product=250:28743, answer=235:33364)
- Layer 30: `64`, `acin`, `分解`, ` Kaw`, `atan` (target ranks: base_value=64:1, first_product=128:983, bound_value=125:38209, second_product=250:112302, answer=235:97828)
- Layer 35: `64`, `分解`, `acin`, `obin`, `保留` (target ranks: base_value=64:1, first_product=128:232, bound_value=125:8259, second_product=250:84173, answer=235:79933)
- Layer 36: `64`, `acin`, `留存`, `分解`, `ikuha` (target ranks: base_value=64:1, first_product=128:72, bound_value=125:5201, second_product=250:72446, answer=235:81807)
- Layer 37: `}<?`, `殿堂`, `64`, `acos`, `radesh` (target ranks: base_value=64:3, first_product=128:335, bound_value=125:20720, second_product=250:116865, answer=235:120523)
- Layer 38: `}<?`, `殿堂`, `迷惑`, `arent`, `覆` (target ranks: base_value=64:18, first_product=128:4139, bound_value=125:40565, second_product=250:118719, answer=235:122426)
- Layer 39: `}<?`, `�`, `殿堂`, `迷惑`, `不加` (target ranks: base_value=64:4011, first_product=128:34613, bound_value=125:46299, second_product=250:88320, answer=235:96967)
- Layer 40: `kur`, ` kur`, ` reper`, ` Re`, `留存` (target ranks: base_value=64:18057, first_product=128:30435, bound_value=125:1887, second_product=250:35841, answer=235:20489)
- Layer 41: ` .`, ` kur`, `kur`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:14154, first_product=128:12898, bound_value=125:1548, second_product=250:12869, answer=235:9237)

### Filler position 23 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126083, first_product=128:124373, bound_value=125:123743, second_product=250:125065, answer=235:124417)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10832, first_product=128:21442, bound_value=125:23058, second_product=250:19375, answer=235:20979)
- Layer 20: ` smile`, `ait`, ` emot`, `足`, ` Tears` (target ranks: base_value=64:13788, first_product=128:25870, bound_value=125:22597, second_product=250:30195, answer=235:33084)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=64:11804, first_product=128:33157, bound_value=125:41424, second_product=250:69631, answer=235:79633)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=64:11056, first_product=128:30726, bound_value=125:33349, second_product=250:55255, answer=235:65813)
- Layer 36: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=64:17516, first_product=128:25528, bound_value=125:32345, second_product=250:57368, answer=235:72177)
- Layer 37: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=64:55518, first_product=128:40769, bound_value=125:57813, second_product=250:91230, answer=235:87136)
- Layer 38: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=64:67500, first_product=128:59663, bound_value=125:59319, second_product=250:97609, answer=235:106473)
- Layer 39: ` Tw`, `Tw`, `.tw`, ` doubling`, ` twice` (target ranks: base_value=64:20183, first_product=128:32630, bound_value=125:46461, second_product=250:103573, answer=235:102302)
- Layer 40: `坏`, ` Tw`, ` "`, `殿堂`, `calcul` (target ranks: base_value=64:1293, first_product=128:7393, bound_value=125:7584, second_product=250:75133, answer=235:70841)
- Layer 41: `计算公式`, ` twice`, `坏`, ` .`, ` first` (target ranks: base_value=64:629, first_product=128:1506, bound_value=125:3441, second_product=250:48627, answer=235:34269)

### Filler position 24 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126268, first_product=128:124690, bound_value=125:124035, second_product=250:125286, answer=235:124655)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10302, first_product=128:20919, bound_value=125:23024, second_product=250:18781, answer=235:20602)
- Layer 20: `ait`, `足`, ` smile`, `atile`, `锁定` (target ranks: base_value=64:8726, first_product=128:27609, bound_value=125:24994, second_product=250:27407, answer=235:33899)
- Layer 30: ` q`, `忽略`, ` QR`, ` Q`, ` ignored` (target ranks: base_value=64:8676, first_product=128:64531, bound_value=125:61110, second_product=250:81691, answer=235:101241)
- Layer 35: ` q`, ` QR`, `忽略`, ` Q`, `q` (target ranks: base_value=64:10553, first_product=128:51405, bound_value=125:47903, second_product=250:55919, answer=235:86981)
- Layer 36: ` q`, `忽略`, `acin`, `忽视`, `省略` (target ranks: base_value=64:19888, first_product=128:47152, bound_value=125:45890, second_product=250:49374, answer=235:96405)
- Layer 37: `}<?`, `不急`, ` q`, `筋`, `忽略` (target ranks: base_value=64:80114, first_product=128:80526, bound_value=125:74903, second_product=250:80617, answer=235:111995)
- Layer 38: `}<?`, `不急`, `acin`, `筋`, `pac` (target ranks: base_value=64:68181, first_product=128:89369, bound_value=125:84132, second_product=250:97956, answer=235:112474)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `不急`, `urin`, `romic` (target ranks: base_value=64:46960, first_product=128:80433, bound_value=125:84059, second_product=250:102581, answer=235:113075)
- Layer 40: `不急`, `筋`, `calcul`, `acl`, `omit` (target ranks: base_value=64:8522, first_product=128:44348, bound_value=125:23959, second_product=250:61704, answer=235:97787)
- Layer 41: ` .`, ` waiting`, `不求`, `不急`, `omit` (target ranks: base_value=64:1510, first_product=128:16366, bound_value=125:8562, second_product=250:36605, answer=235:52786)

### Filler position 25 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126325, first_product=128:124612, bound_value=125:123943, second_product=250:125216, answer=235:124598)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11574, first_product=128:22898, bound_value=125:25417, second_product=250:20109, answer=235:22131)
- Layer 20: `ait`, ` Walker`, ` smile`, `足`, `锁定` (target ranks: base_value=64:9359, first_product=128:25478, bound_value=125:29196, second_product=250:30587, answer=235:27668)
- Layer 30: `kur`, ` Kur`, ` kur`, `第一步`, `算出` (target ranks: base_value=64:3398, first_product=128:63051, bound_value=125:64369, second_product=250:62565, answer=235:72982)
- Layer 35: `kur`, ` Kur`, ` kur`, `kä`, ` Kurdish` (target ranks: base_value=64:2466, first_product=128:50650, bound_value=125:43666, second_product=250:37964, answer=235:69715)
- Layer 36: `kur`, ` Kur`, ` kur`, `kä`, `kus` (target ranks: base_value=64:3020, first_product=128:30872, bound_value=125:36326, second_product=250:28830, answer=235:78375)
- Layer 37: `kur`, ` Kur`, ` kur`, ` Kurs`, `cur` (target ranks: base_value=64:12382, first_product=128:63022, bound_value=125:60169, second_product=250:50152, answer=235:109650)
- Layer 38: `kur`, ` Kur`, ` kur`, `ked`, ` Kurs` (target ranks: base_value=64:21608, first_product=128:88747, bound_value=125:79850, second_product=250:71478, answer=235:114906)
- Layer 39: ` Kur`, `kur`, ` kur`, ` Kurs`, ` Noruwega` (target ranks: base_value=64:32282, first_product=128:90766, bound_value=125:82242, second_product=250:79619, answer=235:109800)
- Layer 40: `kur`, ` kur`, ` Kur`, `kus`, `ked` (target ranks: base_value=64:4489, first_product=128:41728, bound_value=125:36494, second_product=250:62144, answer=235:75418)
- Layer 41: `kur`, ` kur`, ` x`, `出不穷`, `kus` (target ranks: base_value=64:1068, first_product=128:13953, bound_value=125:10817, second_product=250:15362, answer=235:45037)

### Filler position 26 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126353, first_product=128:124596, bound_value=125:123902, second_product=250:125201, answer=235:124547)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10344, first_product=128:21511, bound_value=125:23418, second_product=250:18860, answer=235:20407)
- Layer 20: `ait`, ` Walker`, `Walker`, `锁定`, ` LS` (target ranks: base_value=64:8146, first_product=128:32414, bound_value=125:33001, second_product=250:30903, answer=235:27295)
- Layer 30: ` q`, `kur`, ` kur`, ` Kur`, ` QR` (target ranks: base_value=64:12795, first_product=128:100387, bound_value=125:98619, second_product=250:84896, answer=235:78137)
- Layer 35: ` q`, ` kur`, `kur`, ` Kur`, `q` (target ranks: base_value=64:9896, first_product=128:86740, bound_value=125:77318, second_product=250:62740, answer=235:72547)
- Layer 36: ` q`, ` kur`, `kur`, ` Kur`, `q` (target ranks: base_value=64:10870, first_product=128:71073, bound_value=125:70011, second_product=250:51847, answer=235:73695)
- Layer 37: ` q`, ` kur`, `kur`, `}<?`, ` Kur` (target ranks: base_value=64:46428, first_product=128:108952, bound_value=125:99090, second_product=250:92544, answer=235:97617)
- Layer 38: `}<?`, ` kur`, ` q`, `筋`, `kur` (target ranks: base_value=64:54732, first_product=128:118077, bound_value=125:110294, second_product=250:110059, answer=235:110733)
- Layer 39: `}<?`, ` q`, `筋`, ` Q`, `迷惑` (target ranks: base_value=64:42349, first_product=128:106517, bound_value=125:105598, second_product=250:106687, answer=235:106887)
- Layer 40: `筋`, ` q`, ` kur`, ` talags`, `留存` (target ranks: base_value=64:8476, first_product=128:64801, bound_value=125:64097, second_product=250:85883, answer=235:84269)
- Layer 41: ` kur`, `kur`, `留存`, `筋`, `zij` (target ranks: base_value=64:897, first_product=128:13202, bound_value=125:25827, second_product=250:37335, answer=235:34352)

### Filler position 27 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126329, first_product=128:124651, bound_value=125:123967, second_product=250:125206, answer=235:124535)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9951, first_product=128:20699, bound_value=125:22230, second_product=250:18168, answer=235:19689)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `拆` (target ranks: base_value=64:11591, first_product=128:40549, bound_value=125:38431, second_product=250:32737, answer=235:29719)
- Layer 30: `分解`, `avat`, ` labor`, `鞍`, ` dy` (target ranks: base_value=64:14076, first_product=128:84367, bound_value=125:62592, second_product=250:76462, answer=235:40789)
- Layer 35: `分解`, `avat`, ` labor`, ` dy`, ` Walker` (target ranks: base_value=64:9773, first_product=128:70916, bound_value=125:48485, second_product=250:60466, answer=235:30296)
- Layer 36: `分解`, `翻`, `留存`, `俯`, ` stabil` (target ranks: base_value=64:13372, first_product=128:61833, bound_value=125:48034, second_product=250:51716, answer=235:32798)
- Layer 37: `翻`, `}<?`, `翻了`, `分解`, `xv` (target ranks: base_value=64:54121, first_product=128:90761, bound_value=125:60750, second_product=250:89069, answer=235:44909)
- Layer 38: `}<?`, `zat`, ` x`, `xv`, `翻` (target ranks: base_value=64:56560, first_product=128:101689, bound_value=125:66014, second_product=250:97775, answer=235:52617)
- Layer 39: ` x`, ` X`, `xp`, ` Xavier`, `xv` (target ranks: base_value=64:62755, first_product=128:90798, bound_value=125:82648, second_product=250:108060, answer=235:84297)
- Layer 40: ` x`, `x`, `翻`, `acl`, `筋` (target ranks: base_value=64:28904, first_product=128:66365, bound_value=125:44478, second_product=250:88892, answer=235:66702)
- Layer 41: `分解`, `翻`, `俯`, ` `, ` twist` (target ranks: base_value=64:4777, first_product=128:16486, bound_value=125:9346, second_product=250:29647, answer=235:17596)

### Filler position 28 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126492, first_product=128:124739, bound_value=125:124112, second_product=250:125313, answer=235:124666)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:10189, first_product=128:20587, bound_value=125:22033, second_product=250:18394, answer=235:20312)
- Layer 20: `ait`, ` Walker`, `锁定`, `能被`, ` engaging` (target ranks: base_value=64:10858, first_product=128:41964, bound_value=125:39819, second_product=250:36725, answer=235:36003)
- Layer 30: ` Qin`, ` q`, `acin`, ` Q`, `QG` (target ranks: base_value=64:6885, first_product=128:43897, bound_value=125:72655, second_product=250:93992, answer=235:56950)
- Layer 35: ` q`, `obin`, `acin`, ` reserved`, ` qi` (target ranks: base_value=64:6068, first_product=128:27373, bound_value=125:50262, second_product=250:62967, answer=235:44332)
- Layer 36: `acin`, `俯`, `留存`, `分解`, ` q` (target ranks: base_value=64:16208, first_product=128:36243, bound_value=125:64309, second_product=250:69653, answer=235:57331)
- Layer 37: `}<?`, `acin`, `俯`, `观望`, ` Qin` (target ranks: base_value=64:51869, first_product=128:56819, bound_value=125:92253, second_product=250:103949, answer=235:78955)
- Layer 38: `}<?`, `acin`, `zat`, ` Qin`, `zyn` (target ranks: base_value=64:34459, first_product=128:65501, bound_value=125:100278, second_product=250:110977, answer=235:88011)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `覆`, ` Nij`, `zat` (target ranks: base_value=64:55293, first_product=128:86253, bound_value=125:114160, second_product=250:120959, answer=235:111099)
- Layer 40: `kur`, `覆`, `俯`, `坏的`, ` Rees` (target ranks: base_value=64:14402, first_product=128:55694, bound_value=125:74937, second_product=250:106801, answer=235:103562)
- Layer 41: `kur`, `坏`, `俯`, ` .`, ` ` (target ranks: base_value=64:5482, first_product=128:14653, bound_value=125:34622, second_product=250:71504, answer=235:53726)

### Filler position 29 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126629, first_product=128:125118, bound_value=125:124463, second_product=250:125685, answer=235:125016)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11174, first_product=128:21421, bound_value=125:23396, second_product=250:19339, answer=235:21679)
- Layer 20: `能被`, ` engaging`, `ait`, `锁定`, `距` (target ranks: base_value=64:10970, first_product=128:31760, bound_value=125:28599, second_product=250:34597, answer=235:39748)
- Layer 30: `64`, `分解`, `atan`, `鞍`, ` dy` (target ranks: base_value=64:1, first_product=128:662, bound_value=125:26962, second_product=250:95246, answer=235:79010)
- Layer 35: `64`, `分解`, `ession`, `退出`, `obin` (target ranks: base_value=64:1, first_product=128:728, bound_value=125:18495, second_product=250:69104, answer=235:72192)
- Layer 36: `64`, `分解`, `留存`, `radesh`, `退出` (target ranks: base_value=64:1, first_product=128:513, bound_value=125:26206, second_product=250:69945, answer=235:93748)
- Layer 37: `}<?`, `radesh`, `64`, `殿堂`, ` doubling` (target ranks: base_value=64:3, first_product=128:4951, bound_value=125:69420, second_product=250:113309, answer=235:119522)
- Layer 38: `}<?`, `殿堂`, `dividers`, `迷惑`, ` doubling` (target ranks: base_value=64:11, first_product=128:24140, bound_value=125:91802, second_product=250:118931, answer=235:124231)
- Layer 39: `}<?`, `殿堂`, `ocyst`, `zat`, `迷惑` (target ranks: base_value=64:10064, first_product=128:61975, bound_value=125:85898, second_product=250:87088, answer=235:107236)
- Layer 40: `kur`, ` Kur`, ` kur`, ` Re`, `klar` (target ranks: base_value=64:17087, first_product=128:29329, bound_value=125:8699, second_product=250:24849, answer=235:28423)
- Layer 41: `kur`, ` kur`, ` Kur`, ` `, `本` (target ranks: base_value=64:16031, first_product=128:12430, bound_value=125:4876, second_product=250:10942, answer=235:22228)

### Filler position 30 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126759, first_product=128:125344, bound_value=125:124689, second_product=250:125874, answer=235:125269)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10062, first_product=128:20218, bound_value=125:22377, second_product=250:18828, answer=235:20741)
- Layer 20: ` smile`, `锁定`, `atile`, `鞍`, `ait` (target ranks: base_value=64:9821, first_product=128:26849, bound_value=125:26341, second_product=250:34400, answer=235:38930)
- Layer 30: ` rip`, ` riv`, `�`, ` tear`, ` Rhe` (target ranks: base_value=64:44177, first_product=128:115388, bound_value=125:102497, second_product=250:107505, answer=235:116070)
- Layer 35: ` tap`, `Tap`, ` rip`, `�`, ` top` (target ranks: base_value=64:65417, first_product=128:105587, bound_value=125:93794, second_product=250:86903, answer=235:116511)
- Layer 36: ` tap`, `坏`, `adal`, ` riv`, ` rip` (target ranks: base_value=64:38109, first_product=128:78538, bound_value=125:57701, second_product=250:52884, answer=235:100087)
- Layer 37: `坏`, `zat`, `radesh`, `坏的`, ` Tub` (target ranks: base_value=64:95237, first_product=128:106706, bound_value=125:89738, second_product=250:83634, answer=235:121114)
- Layer 38: `zat`, `坏`, `zel`, ` duc`, `疑惑` (target ranks: base_value=64:93113, first_product=128:111392, bound_value=125:97006, second_product=250:102825, answer=235:124212)
- Layer 39: `zat`, ` Nij`, ` duc`, `zel`, ` fif` (target ranks: base_value=64:96051, first_product=128:110160, bound_value=125:106381, second_product=250:112477, answer=235:120930)
- Layer 40: `zat`, `zel`, ` fum`, `殿堂`, `坏` (target ranks: base_value=64:64651, first_product=128:81217, bound_value=125:77964, second_product=250:91084, answer=235:111305)
- Layer 41: `坏`, `zel`, `坏的`, ` fum`, `zij` (target ranks: base_value=64:19594, first_product=128:20305, bound_value=125:40229, second_product=250:55150, answer=235:55883)

### Filler position 31 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=64:126846, first_product=128:125454, bound_value=125:124857, second_product=250:125989, answer=235:125443)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9564, first_product=128:19270, bound_value=125:21951, second_product=250:18101, answer=235:20052)
- Layer 20: `ait`, `锁定`, `鞍`, ` smile`, ` LS` (target ranks: base_value=64:7616, first_product=128:20312, bound_value=125:21755, second_product=250:26356, answer=235:25633)
- Layer 30: ` ES`, `鞍`, `�`, ` tap`, `acos` (target ranks: base_value=64:25054, first_product=128:96411, bound_value=125:86759, second_product=250:78816, answer=235:92096)
- Layer 35: ` tap`, `Tap`, ` repetition`, ` labor`, ` rip` (target ranks: base_value=64:25043, first_product=128:87598, bound_value=125:83247, second_product=250:79356, answer=235:96173)
- Layer 36: ` tap`, ` rip`, ` Tw`, ` stabil`, ` zad` (target ranks: base_value=64:18348, first_product=128:59804, bound_value=125:64283, second_product=250:56813, answer=235:85873)
- Layer 37: `}<?`, `acos`, ` Zad`, ` fat`, `acam` (target ranks: base_value=64:71146, first_product=128:97965, bound_value=125:90280, second_product=250:98828, answer=235:114576)
- Layer 38: `}<?`, `zat`, `zos`, `pac`, `amol` (target ranks: base_value=64:72475, first_product=128:108233, bound_value=125:96391, second_product=250:116227, answer=235:121069)
- Layer 39: `}<?`, ` duc`, `zat`, `hemer`, `迷惑` (target ranks: base_value=64:60753, first_product=128:109315, bound_value=125:107760, second_product=250:115088, answer=235:121398)
- Layer 40: ` Question`, `Question`, `zij`, ` pals`, `zel` (target ranks: base_value=64:19732, first_product=128:67789, bound_value=125:65707, second_product=250:103614, answer=235:115174)
- Layer 41: `Question`, ` Question`, `坏`, `acular`, `cab` (target ranks: base_value=64:3698, first_product=128:18925, bound_value=125:34422, second_product=250:66577, answer=235:70929)

### Filler position 32 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=64:126804, first_product=128:125314, bound_value=125:124725, second_product=250:125851, answer=235:125264)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:8870, first_product=128:18694, bound_value=125:21175, second_product=250:17315, answer=235:19012)
- Layer 20: `锁定`, `ait`, ` smile`, ` ES`, ` LS` (target ranks: base_value=64:5379, first_product=128:14288, bound_value=125:20666, second_product=250:23532, answer=235:16775)
- Layer 30: ` Answer`, ` answer`, `Answer`, `回答`, `答案` (target ranks: base_value=64:5977, first_product=128:35713, bound_value=125:36854, second_product=250:18439, answer=235:7222)
- Layer 35: ` answer`, ` Answer`, `退出`, `Answer`, `回答` (target ranks: base_value=64:1703, first_product=128:14491, bound_value=125:7119, second_product=250:4324, answer=235:2568)
- Layer 36: `退出`, ` riv`, `acin`, ` tap`, ` stabil` (target ranks: base_value=64:2684, first_product=128:13586, bound_value=125:9926, second_product=250:4754, answer=235:4433)
- Layer 37: `}<?`, ` rational`, `rational`, `覆`, `理性的` (target ranks: base_value=64:23819, first_product=128:37885, bound_value=125:21037, second_product=250:22031, answer=235:8324)
- Layer 38: `}<?`, ` talags`, `不加`, `opters`, `下沉` (target ranks: base_value=64:46844, first_product=128:46749, bound_value=125:30975, second_product=250:33285, answer=235:10961)
- Layer 39: `}<?`, `opters`, `aharan`, `<｜begin▁of▁sentence｜>`, ` talags` (target ranks: base_value=64:73895, first_product=128:108966, bound_value=125:68152, second_product=250:82810, answer=235:34499)
- Layer 40: ` talags`, `}<?`, `不加`, ` fum`, ` embargo` (target ranks: base_value=64:27807, first_product=128:105152, bound_value=125:22177, second_product=250:67129, answer=235:8829)
- Layer 41: ` talags`, ` hilabihan`, `试一试`, `Answer`, `等待着` (target ranks: base_value=64:6572, first_product=128:38533, bound_value=125:5201, second_product=250:15462, answer=235:709)

### Filler position 33 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127263, first_product=128:125995, bound_value=125:125458, second_product=250:126533, answer=235:125866)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9234, first_product=128:19243, bound_value=125:21651, second_product=250:17542, answer=235:18986)
- Layer 20: `ait`, ` Walker`, ` LS`, `LS`, `Walker` (target ranks: base_value=64:4245, first_product=128:16948, bound_value=125:22439, second_product=250:24782, answer=235:23584)
- Layer 30: ` metas`, `往外`, `64`, ` receptive`, ` Kaw` (target ranks: base_value=64:3, first_product=128:611, bound_value=125:245, second_product=250:11603, answer=235:41087)
- Layer 35: `100`, `二十五`, `退出`, ` Kaw`, `125` (target ranks: base_value=64:1419, first_product=128:10869, bound_value=125:5, second_product=250:40, answer=235:28028)
- Layer 36: `100`, ` сто`, `放下`, `一百`, ` hundred` (target ranks: base_value=64:15082, first_product=128:21695, bound_value=125:7, second_product=250:13, answer=235:45283)
- Layer 37: `}<?`, `100`, `言语`, `宫内`, ` hundred` (target ranks: base_value=64:57000, first_product=128:46906, bound_value=125:18, second_product=250:67, answer=235:39109)
- Layer 38: `100`, ` hundred`, `言语`, `}<?`, ` Hundred` (target ranks: base_value=64:71342, first_product=128:53548, bound_value=125:42, second_product=250:27, answer=235:10784)
- Layer 39: `}<?`, ` Naz`, `宫内`, ` Nij`, ` Tara` (target ranks: base_value=64:95088, first_product=128:123583, bound_value=125:2088, second_product=250:1067, answer=235:1505)
- Layer 40: ` Kur`, ` kur`, `185`, `kur`, `187` (target ranks: base_value=64:23591, first_product=128:106965, bound_value=125:39, second_product=250:375, answer=235:27)
- Layer 41: `kur`, ` kur`, `185`, ` Kur`, `要不` (target ranks: base_value=64:19256, first_product=128:83552, bound_value=125:193, second_product=250:430, answer=235:103)

### Filler position 34 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127226, first_product=128:125954, bound_value=125:125397, second_product=250:126435, answer=235:125811)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9737, first_product=128:20155, bound_value=125:22165, second_product=250:17972, answer=235:19621)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=64:8604, first_product=128:25012, bound_value=125:23232, second_product=250:29727, answer=235:30389)
- Layer 30: ` Kur`, `kur`, ` kur`, ` Kurt`, ` Kurdish` (target ranks: base_value=64:2557, first_product=128:79185, bound_value=125:54521, second_product=250:68858, answer=235:88309)
- Layer 35: `kur`, ` Kur`, ` kur`, `cur`, ` Kurdish` (target ranks: base_value=64:387, first_product=128:27551, bound_value=125:13725, second_product=250:14661, answer=235:46308)
- Layer 36: ` Kur`, ` kur`, `kur`, `留存`, ` Kurt` (target ranks: base_value=64:497, first_product=128:12169, bound_value=125:9249, second_product=250:9302, answer=235:45593)
- Layer 37: ` Kur`, ` kur`, `kur`, ` Kurs`, ` kurs` (target ranks: base_value=64:5617, first_product=128:25185, bound_value=125:15131, second_product=250:19480, answer=235:63960)
- Layer 38: ` kur`, ` Kur`, `kur`, ` Kurs`, `}<?` (target ranks: base_value=64:6218, first_product=128:48376, bound_value=125:32967, second_product=250:40597, answer=235:71499)
- Layer 39: ` Kur`, ` kur`, `kur`, `}<?`, ` Kurs` (target ranks: base_value=64:19057, first_product=128:96926, bound_value=125:58572, second_product=250:76523, answer=235:85982)
- Layer 40: ` kur`, `kur`, ` Kur`, ` x`, `留存` (target ranks: base_value=64:1251, first_product=128:65327, bound_value=125:16421, second_product=250:66616, answer=235:43918)
- Layer 41: ` kur`, `kur`, ` Kur`, ` x`, ` whichever` (target ranks: base_value=64:213, first_product=128:21244, bound_value=125:6028, second_product=250:22447, answer=235:17185)

### Filler position 35 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127255, first_product=128:126053, bound_value=125:125476, second_product=250:126561, answer=235:125946)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11004, first_product=128:21166, bound_value=125:23125, second_product=250:18732, answer=235:21508)
- Layer 20: ` smile`, `ait`, `足`, `能被`, ` engaging` (target ranks: base_value=64:10844, first_product=128:29023, bound_value=125:25006, second_product=250:22985, answer=235:35603)
- Layer 30: `atan`, `鞍`, `重复`, `锁定`, ` repetition` (target ranks: base_value=64:10738, first_product=128:45171, bound_value=125:42100, second_product=250:37710, answer=235:60605)
- Layer 35: ` var`, ` reserved`, ` repetition`, `锁定`, `重复` (target ranks: base_value=64:12119, first_product=128:39464, bound_value=125:35141, second_product=250:24642, answer=235:58801)
- Layer 36: ` var`, ` x`, `acin`, `留存`, ` reserved` (target ranks: base_value=64:26090, first_product=128:35489, bound_value=125:46849, second_product=250:23810, answer=235:88719)
- Layer 37: `}<?`, `变量的`, ` variable`, `radesh`, ` x` (target ranks: base_value=64:86047, first_product=128:71814, bound_value=125:86166, second_product=250:65398, answer=235:110741)
- Layer 38: `}<?`, `zat`, ` x`, `pac`, `坏` (target ranks: base_value=64:81093, first_product=128:77877, bound_value=125:91456, second_product=250:71253, answer=235:108093)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `pac`, `zat`, ` x` (target ranks: base_value=64:55360, first_product=128:53194, bound_value=125:72989, second_product=250:76958, answer=235:104836)
- Layer 40: ` x`, `acl`, `坏`, `kur`, ` kinahabogang` (target ranks: base_value=64:10782, first_product=128:14395, bound_value=125:15852, second_product=250:43486, answer=235:85339)
- Layer 41: ` x`, ` .`, ` `, ` kur`, `kur` (target ranks: base_value=64:2437, first_product=128:3714, bound_value=125:4977, second_product=250:17849, answer=235:42982)

### Filler position 36 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127247, first_product=128:126207, bound_value=125:125654, second_product=250:126736, answer=235:126131)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11371, first_product=128:21475, bound_value=125:24091, second_product=250:19248, answer=235:22764)
- Layer 20: `能被`, `ait`, ` smile`, ` Walker`, `距` (target ranks: base_value=64:12881, first_product=128:29767, bound_value=125:26247, second_product=250:23652, answer=235:41872)
- Layer 30: `kur`, ` Kur`, ` kur`, `算出`, `cur` (target ranks: base_value=64:6535, first_product=128:71113, bound_value=125:67938, second_product=250:51846, answer=235:92175)
- Layer 35: `kur`, ` Kur`, ` kur`, `cur`, `кур` (target ranks: base_value=64:2563, first_product=128:41621, bound_value=125:26494, second_product=250:14463, answer=235:64541)
- Layer 36: `kur`, ` Kur`, ` kur`, `кур`, `cur` (target ranks: base_value=64:5787, first_product=128:24685, bound_value=125:24832, second_product=250:9618, answer=235:76611)
- Layer 37: `kur`, ` Kur`, ` kur`, `}<?`, `кур` (target ranks: base_value=64:34456, first_product=128:49213, bound_value=125:43474, second_product=250:27843, answer=235:93933)
- Layer 38: `kur`, ` Kur`, `}<?`, ` kur`, `zat` (target ranks: base_value=64:36472, first_product=128:73651, bound_value=125:55825, second_product=250:38896, answer=235:99836)
- Layer 39: ` Kur`, `kur`, `}<?`, `zat`, ` kur` (target ranks: base_value=64:45750, first_product=128:81428, bound_value=125:72663, second_product=250:64398, answer=235:103201)
- Layer 40: `kur`, ` x`, ` kur`, `留存`, `翻` (target ranks: base_value=64:4955, first_product=128:26321, bound_value=125:17614, second_product=250:36094, answer=235:56642)
- Layer 41: `kur`, ` x`, ` kur`, `acular`, `abd` (target ranks: base_value=64:289, first_product=128:3781, bound_value=125:2722, second_product=250:3973, answer=235:19809)

### Filler position 37 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127261, first_product=128:126092, bound_value=125:125495, second_product=250:126604, answer=235:126058)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11654, first_product=128:22152, bound_value=125:25652, second_product=250:20217, answer=235:23738)
- Layer 20: `能被`, ` engaging`, `ait`, `atile`, `sl` (target ranks: base_value=64:20300, first_product=128:49433, bound_value=125:38933, second_product=250:41155, answer=235:71122)
- Layer 30: `忽略`, ` ignored`, ` q`, ` ignoring`, ` ignore` (target ranks: base_value=64:14552, first_product=128:55784, bound_value=125:35882, second_product=250:53040, answer=235:101633)
- Layer 35: ` q`, `忽略`, ` ignoring`, ` Q`, ` QR` (target ranks: base_value=64:13387, first_product=128:50730, bound_value=125:31206, second_product=250:39961, answer=235:94916)
- Layer 36: `忽略`, ` q`, ` ignoring`, `省略`, ` ignored` (target ranks: base_value=64:18146, first_product=128:40004, bound_value=125:26379, second_product=250:33177, answer=235:98979)
- Layer 37: `}<?`, `不急`, `遗漏`, `忽略`, ` q` (target ranks: base_value=64:74043, first_product=128:83148, bound_value=125:53115, second_product=250:75416, answer=235:121273)
- Layer 38: `}<?`, `不急`, `zat`, ` q`, `坏` (target ranks: base_value=64:43474, first_product=128:84411, bound_value=125:55480, second_product=250:82879, answer=235:118352)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `不急`, `迷惑`, ` sublim` (target ranks: base_value=64:49039, first_product=128:84915, bound_value=125:68138, second_product=250:86422, answer=235:118218)
- Layer 40: `不急`, `kur`, `acular`, `坏`, `等待着` (target ranks: base_value=64:12533, first_product=128:41870, bound_value=125:19920, second_product=250:62616, answer=235:111122)
- Layer 41: `从前`, `kur`, `坏`, ` .`, `acular` (target ranks: base_value=64:2507, first_product=128:11274, bound_value=125:5519, second_product=250:23512, answer=235:70745)

### Filler position 38 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127323, first_product=128:126207, bound_value=125:125630, second_product=250:126711, answer=235:126104)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10830, first_product=128:21160, bound_value=125:24108, second_product=250:19681, answer=235:22448)
- Layer 20: `忑`, `ait`, ` Walker`, `能被`, ` engaging` (target ranks: base_value=64:13243, first_product=128:43616, bound_value=125:45331, second_product=250:50511, answer=235:56300)
- Layer 30: `Tw`, ` Tw`, `acos`, `�`, `sac` (target ranks: base_value=64:19051, first_product=128:81122, bound_value=125:83335, second_product=250:80134, answer=235:93839)
- Layer 35: ` Tw`, ` tap`, `Tw`, `acin`, ` repetition` (target ranks: base_value=64:13745, first_product=128:79171, bound_value=125:79963, second_product=250:80056, answer=235:100696)
- Layer 36: ` Tw`, ` tap`, `Tw`, `翻`, ` Zad` (target ranks: base_value=64:12296, first_product=128:45136, bound_value=125:63680, second_product=250:59593, answer=235:91271)
- Layer 37: `}<?`, `翻了`, ` ---|---|---|---|---|---|---`, ` Zad`, `翻` (target ranks: base_value=64:49610, first_product=128:68686, bound_value=125:69083, second_product=250:85207, answer=235:105577)
- Layer 38: `}<?`, `zat`, `zv`, `�`, `不加` (target ranks: base_value=64:35328, first_product=128:93987, bound_value=125:85123, second_product=250:102917, answer=235:119142)
- Layer 39: `}<?`, ` Nij`, `�`, `hatic`, `umber` (target ranks: base_value=64:46810, first_product=128:78570, bound_value=125:69877, second_product=250:86886, answer=235:110280)
- Layer 40: ` Question`, `Question`, ` fum`, ` Tw`, `y` (target ranks: base_value=64:6202, first_product=128:28377, bound_value=125:13697, second_product=250:53088, answer=235:84791)
- Layer 41: `Question`, ` Question`, ` `, ` number`, ` Number` (target ranks: base_value=64:1137, first_product=128:1509, bound_value=125:1487, second_product=250:13919, answer=235:13540)

### Filler position 39 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127268, first_product=128:126129, bound_value=125:125559, second_product=250:126616, answer=235:126028)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10254, first_product=128:19978, bound_value=125:22650, second_product=250:18897, answer=235:21196)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, ` smile` (target ranks: base_value=64:8888, first_product=128:25029, bound_value=125:29470, second_product=250:31910, answer=235:24615)
- Layer 30: `sl`, `sac`, `subt`, ` calculator`, `calcul` (target ranks: base_value=64:79, first_product=128:9299, bound_value=125:9679, second_product=250:8107, answer=235:1576)
- Layer 35: `退出`, `锁定`, ` smile`, `打完`, `79` (target ranks: base_value=64:385, first_product=128:4414, bound_value=125:1682, second_product=250:3544, answer=235:1467)
- Layer 36: `退出`, `acin`, `放下`, `留存`, `等待着` (target ranks: base_value=64:1022, first_product=128:3654, bound_value=125:3028, second_product=250:4639, answer=235:2182)
- Layer 37: `}<?`, `oug`, `放下`, `覆`, `清洗` (target ranks: base_value=64:16821, first_product=128:31492, bound_value=125:9823, second_product=250:13008, answer=235:1602)
- Layer 38: `}<?`, `oug`, `zat`, `覆`, `eltemperaturen` (target ranks: base_value=64:33306, first_product=128:71310, bound_value=125:24629, second_product=250:20491, answer=235:4349)
- Layer 39: `}<?`, `ocyst`, `}using`, `eltemperaturen`, `oug` (target ranks: base_value=64:99746, first_product=128:122742, bound_value=125:62309, second_product=250:33219, answer=235:2445)
- Layer 40: `}<?`, `等待着`, `185`, `acular`, `oug` (target ranks: base_value=64:70224, first_product=128:125215, bound_value=125:36369, second_product=250:34679, answer=235:129)
- Layer 41: `等待着`, `185`, ` waiting`, ` `, ` dekameters` (target ranks: base_value=64:26152, first_product=128:101911, bound_value=125:15219, second_product=250:12935, answer=235:38)

### Filler position 40 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127435, first_product=128:126451, bound_value=125:125925, second_product=250:126917, answer=235:126329)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10857, first_product=128:20920, bound_value=125:23061, second_product=250:18989, answer=235:21457)
- Layer 20: `ait`, `锁定`, `能被`, `鞍`, `ätte` (target ranks: base_value=64:4985, first_product=128:19144, bound_value=125:19079, second_product=250:19559, answer=235:17669)
- Layer 30: `65`, ` Sm`, `acos`, ` consuming`, ` seventy` (target ranks: base_value=64:391, first_product=128:2975, bound_value=125:356, second_product=250:1729, answer=235:1555)
- Layer 35: `245`, `235`, `229`, `185`, `205` (target ranks: base_value=64:22717, first_product=128:29293, bound_value=125:263, second_product=250:8, answer=235:2)
- Layer 36: `235`, `233`, `229`, `185`, `245` (target ranks: base_value=64:104165, first_product=128:43950, bound_value=125:1779, second_product=250:133, answer=235:1)
- Layer 37: `235`, `233`, `185`, `eltemperaturen`, `229` (target ranks: base_value=64:116111, first_product=128:54186, bound_value=125:1709, second_product=250:494, answer=235:1)
- Layer 38: `235`, `233`, `229`, `237`, `185` (target ranks: base_value=64:128466, first_product=128:116248, bound_value=125:17299, second_product=250:2456, answer=235:1)
- Layer 39: `235`, `233`, `本题分析`, `zat`, `}<?` (target ranks: base_value=64:128274, first_product=128:128285, bound_value=125:106534, second_product=250:86506, answer=235:1)
- Layer 40: `235`, `233`, `otan`, `185`, `229` (target ranks: base_value=64:125931, first_product=128:126173, bound_value=125:48190, second_product=250:41201, answer=235:1)
- Layer 41: `235`, `233`, `))))`, `185`, `}}}}` (target ranks: base_value=64:87414, first_product=128:112961, bound_value=125:31547, second_product=250:13223, answer=235:1)

### Filler position 41 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127350, first_product=128:126461, bound_value=125:125877, second_product=250:126928, answer=235:126300)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11552, first_product=128:21594, bound_value=125:23770, second_product=250:19145, answer=235:22037)
- Layer 20: `ait`, `能被`, `锁定`, `ätte`, `距` (target ranks: base_value=64:12091, first_product=128:25752, bound_value=125:26930, second_product=250:30017, answer=235:31051)
- Layer 30: ` kahaboga`, `zcz`, `65`, `acos`, ` metas` (target ranks: base_value=64:2540, first_product=128:7521, bound_value=125:110, second_product=250:1403, answer=235:3264)
- Layer 35: `235`, `250`, `249`, `229`, `205` (target ranks: base_value=64:40891, first_product=128:68565, bound_value=125:291, second_product=250:2, answer=235:1)
- Layer 36: `235`, `237`, `233`, ` markup`, `229` (target ranks: base_value=64:99668, first_product=128:68038, bound_value=125:3224, second_product=250:76, answer=235:1)
- Layer 37: `235`, `237`, ` markup`, `233`, `清洗` (target ranks: base_value=64:114697, first_product=128:74773, bound_value=125:2584, second_product=250:225, answer=235:1)
- Layer 38: `235`, `237`, `233`, `229`, `232` (target ranks: base_value=64:129190, first_product=128:126448, bound_value=125:31313, second_product=250:618, answer=235:1)
- Layer 39: `235`, `233`, `本题分析`, `232`, `234` (target ranks: base_value=64:128399, first_product=128:128588, bound_value=125:106892, second_product=250:49881, answer=235:1)
- Layer 40: `235`, `233`, ` markup`, `237`, ` dekameters` (target ranks: base_value=64:127838, first_product=128:128059, bound_value=125:48315, second_product=250:28144, answer=235:1)
- Layer 41: `235`, ` mediab`, `233`, `))))`, `}}}}` (target ranks: base_value=64:109556, first_product=128:122196, bound_value=125:23943, second_product=250:10083, answer=235:1)

### Filler position 42 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127551, first_product=128:126569, bound_value=125:126034, second_product=250:127029, answer=235:126445)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12002, first_product=128:21855, bound_value=125:23879, second_product=250:19184, answer=235:22146)
- Layer 20: ` smile`, `锁定`, `距`, `鞍`, `ait` (target ranks: base_value=64:10431, first_product=128:17874, bound_value=125:15401, second_product=250:14374, answer=235:19245)
- Layer 30: `二十五`, `鞍`, `�`, ` iceberg`, `25` (target ranks: base_value=64:7516, first_product=128:20740, bound_value=125:417, second_product=250:1071, answer=235:11656)
- Layer 35: `�`, `尾`, `退出`, ` closure`, `acos` (target ranks: base_value=64:36610, first_product=128:81738, bound_value=125:4370, second_product=250:3334, answer=235:1584)
- Layer 36: `夫妻`, `夫妇`, `cou`, `cault`, ` smoot` (target ranks: base_value=64:67236, first_product=128:49994, bound_value=125:14948, second_product=250:23252, answer=235:146)
- Layer 37: `本题分析`, `aharan`, `cault`, `}<?`, `eltemperaturen` (target ranks: base_value=64:103256, first_product=128:53638, bound_value=125:10251, second_product=250:38041, answer=235:363)
- Layer 38: `本题分析`, `eltemperaturen`, `185`, ` smoot`, `东海` (target ranks: base_value=64:127875, first_product=128:52183, bound_value=125:10097, second_product=250:65690, answer=235:78)
- Layer 39: `185`, `本题分析`, `aharan`, `233`, `zat` (target ranks: base_value=64:128108, first_product=128:119541, bound_value=125:48771, second_product=250:67966, answer=235:6)
- Layer 40: `185`, `233`, ` mare`, `187`, ` ` (target ranks: base_value=64:123283, first_product=128:94888, bound_value=125:7412, second_product=250:27454, answer=235:13)
- Layer 41: `185`, ` .`, `233`, ` `, `183` (target ranks: base_value=64:85642, first_product=128:58592, bound_value=125:3945, second_product=250:7048, answer=235:10)

### Filler position 43 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127366, first_product=128:126440, bound_value=125:125934, second_product=250:126970, answer=235:126391)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11497, first_product=128:21538, bound_value=125:24058, second_product=250:19087, answer=235:22001)
- Layer 20: `LS`, ` LS`, ` smile`, `锁定`, `距` (target ranks: base_value=64:5828, first_product=128:13362, bound_value=125:14008, second_product=250:12181, answer=235:17890)
- Layer 30: `二十五`, `鞍`, `125`, `25`, ` Feldman` (target ranks: base_value=64:25, first_product=128:1463, bound_value=125:3, second_product=250:74, answer=235:34759)
- Layer 35: `250`, `二十五`, `249`, `德国`, ` Generator` (target ranks: base_value=64:37910, first_product=128:109527, bound_value=125:159, second_product=250:1, answer=235:37711)
- Layer 36: `250`, ` Generator`, `249`, `德国`, ` generator` (target ranks: base_value=64:99055, first_product=128:120303, bound_value=125:105, second_product=250:1, answer=235:58123)
- Layer 37: `250`, `249`, `150`, `atinum`, ` Berlin` (target ranks: base_value=64:114917, first_product=128:117945, bound_value=125:116, second_product=250:1, answer=235:46773)
- Layer 38: `250`, `249`, ` Garland`, `atinum`, `平滑` (target ranks: base_value=64:124322, first_product=128:124349, bound_value=125:254, second_product=250:1, answer=235:26534)
- Layer 39: `250`, `第二百`, `二百`, `249`, ` George` (target ranks: base_value=64:119950, first_product=128:126020, bound_value=125:964, second_product=250:1, answer=235:556)
- Layer 40: `250`, `185`, `187`, `第二百`, `二百` (target ranks: base_value=64:114160, first_product=128:124615, bound_value=125:372, second_product=250:1, answer=235:18)
- Layer 41: `250`, `185`, ` number`, `要不`, `第二百` (target ranks: base_value=64:86582, first_product=128:117571, bound_value=125:1781, second_product=250:1, answer=235:247)

### Filler position 44 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=64:127516, first_product=128:126432, bound_value=125:125918, second_product=250:126973, answer=235:126394)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11674, first_product=128:21549, bound_value=125:24469, second_product=250:19304, answer=235:22053)
- Layer 20: `ait`, `忑`, `距`, `能被`, `锁定` (target ranks: base_value=64:8043, first_product=128:19491, bound_value=125:17652, second_product=250:18541, answer=235:26638)
- Layer 30: `64`, ` sixty`, ` Kur`, `kur`, ` twice` (target ranks: base_value=64:1, first_product=128:12894, bound_value=125:57346, second_product=250:93610, answer=235:99538)
- Layer 35: `64`, `起始`, ` Kur`, ` sixty`, ` start` (target ranks: base_value=64:1, first_product=128:11190, bound_value=125:39268, second_product=250:50084, answer=235:84132)
- Layer 36: `64`, ` start`, `起始`, ` quadru`, `留存` (target ranks: base_value=64:1, first_product=128:6947, bound_value=125:37942, second_product=250:30365, answer=235:87997)
- Layer 37: `}<?`, `otan`, `本题分析`, ` doubling`, ` Kur` (target ranks: base_value=64:13, first_product=128:42463, bound_value=125:61804, second_product=250:48042, answer=235:108171)
- Layer 38: `}<?`, ` Kur`, `otan`, `ounder`, `本题分析` (target ranks: base_value=64:147, first_product=128:88010, bound_value=125:88577, second_product=250:60216, answer=235:112230)
- Layer 39: `}<?`, `ounder`, `本题分析`, `otan`, `mult` (target ranks: base_value=64:51271, first_product=128:82403, bound_value=125:27568, second_product=250:6983, answer=235:15418)
- Layer 40: ` kur`, `kur`, ` Kur`, `kten`, `185` (target ranks: base_value=64:48615, first_product=128:57059, bound_value=125:261, second_product=250:125, answer=235:15)
- Layer 41: ` kur`, `kur`, `185`, `187`, `183` (target ranks: base_value=64:22574, first_product=128:13243, bound_value=125:30, second_product=250:15, answer=235:9)

### Filler position 45 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127678, first_product=128:126663, bound_value=125:126186, second_product=250:127217, answer=235:126562)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11437, first_product=128:20730, bound_value=125:23609, second_product=250:19008, answer=235:21794)
- Layer 20: `ait`, `会成为`, ` Walker`, ` engaging`, `能被` (target ranks: base_value=64:20054, first_product=128:34108, bound_value=125:34978, second_product=250:29181, answer=235:32141)
- Layer 30: ` Kur`, `kur`, ` kur`, ` Curt`, ` Kaw` (target ranks: base_value=64:16243, first_product=128:98021, bound_value=125:75357, second_product=250:93271, answer=235:83884)
- Layer 35: ` Kur`, `kur`, ` kur`, ` Curt`, ` Kaw` (target ranks: base_value=64:7129, first_product=128:78446, bound_value=125:35005, second_product=250:49380, answer=235:65989)
- Layer 36: ` Kur`, ` kur`, `kur`, ` Curt`, ` Kaw` (target ranks: base_value=64:4064, first_product=128:30249, bound_value=125:18340, second_product=250:21438, answer=235:56296)
- Layer 37: ` Kur`, ` kur`, `kur`, ` KV`, `}<?` (target ranks: base_value=64:31918, first_product=128:63595, bound_value=125:40349, second_product=250:56013, answer=235:89580)
- Layer 38: ` Kur`, `kur`, ` kur`, `}<?`, `zat` (target ranks: base_value=64:25454, first_product=128:71020, bound_value=125:34954, second_product=250:57980, answer=235:82994)
- Layer 39: ` Kur`, `kur`, ` kur`, `迷惑`, `}<?` (target ranks: base_value=64:20241, first_product=128:55941, bound_value=125:31214, second_product=250:30857, answer=235:38168)
- Layer 40: ` x`, `x`, `kur`, ` X`, `留存` (target ranks: base_value=64:1556, first_product=128:17267, bound_value=125:3562, second_product=250:12953, answer=235:5688)
- Layer 41: ` x`, ` `, ` .`, `kur`, ` Answer` (target ranks: base_value=64:284, first_product=128:3230, bound_value=125:580, second_product=250:1506, answer=235:528)

### Filler position 46 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127521, first_product=128:126504, bound_value=125:125979, second_product=250:126998, answer=235:126388)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11225, first_product=128:20455, bound_value=125:22679, second_product=250:18706, answer=235:21399)
- Layer 20: ` adtong`, `平行`, `俯`, ` spac`, `ait` (target ranks: base_value=64:63551, first_product=128:79415, bound_value=125:77304, second_product=250:64656, answer=235:74141)
- Layer 30: ` spac`, `}using`, `?datasetId`, `坝`, ` dekameters` (target ranks: base_value=64:100932, first_product=128:92081, bound_value=125:85258, second_product=250:101303, answer=235:85199)
- Layer 35: `坏`, `}using`, `俯`, `ancock`, `足足` (target ranks: base_value=64:88634, first_product=128:76333, bound_value=125:52536, second_product=250:68648, answer=235:92264)
- Layer 36: `俯`, `足足`, `ancock`, ` reduct`, `滴水` (target ranks: base_value=64:26280, first_product=128:27595, bound_value=125:26222, second_product=250:25105, answer=235:40304)
- Layer 37: `}<?`, `onana`, `放下`, `俯`, `合并` (target ranks: base_value=64:63832, first_product=128:48215, bound_value=125:18831, second_product=250:44339, answer=235:31895)
- Layer 38: ` .`, `错过`, `坏`, `俯`, ` Weston` (target ranks: base_value=64:36006, first_product=128:40705, bound_value=125:8860, second_product=250:29155, answer=235:25928)
- Layer 39: `osaurus`, `罢`, `oxygen`, ` Maj`, `}<?` (target ranks: base_value=64:67424, first_product=128:74558, bound_value=125:12732, second_product=250:51387, answer=235:7540)
- Layer 40: ` .`, ` x`, ` nasod`, ` .↵↵`, `俯` (target ranks: base_value=64:8906, first_product=128:25194, bound_value=125:372, second_product=250:16554, answer=235:1529)
- Layer 41: ` .`, ` .↵↵`, ` `, ` bears`, ` .↵` (target ranks: base_value=64:4809, first_product=128:4268, bound_value=125:38, second_product=250:5667, answer=235:109)

### Filler position 47 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127384, first_product=128:126390, bound_value=125:125842, second_product=250:126907, answer=235:126271)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=64:10817, first_product=128:20661, bound_value=125:22544, second_product=250:19007, answer=235:21263)
- Layer 20: `}<?`, `东海`, `ozygous`, ` partly`, `adaghan` (target ranks: base_value=64:120397, first_product=128:126059, bound_value=125:115320, second_product=250:87753, answer=235:123073)
- Layer 30: `}<?`, `codeline`, `}using`, `dividers`, `东京` (target ranks: base_value=64:108685, first_product=128:115415, bound_value=125:107768, second_product=250:99530, answer=235:114526)
- Layer 35: `codeline`, `ِّف`, `切割`, `浪费`, `lett` (target ranks: base_value=64:106162, first_product=128:114044, bound_value=125:97365, second_product=250:101525, answer=235:125577)
- Layer 36: `锯`, `足足`, `切割`, `坏`, ` nasod` (target ranks: base_value=64:50468, first_product=128:66914, bound_value=125:64921, second_product=250:51114, answer=235:108501)
- Layer 37: `磨损`, `}<?`, `东京`, `�`, `在东` (target ranks: base_value=64:85443, first_product=128:57821, bound_value=125:77264, second_product=250:61574, answer=235:91999)
- Layer 38: ` .`, `遁`, `切割`, `坏`, `lett` (target ranks: base_value=64:28585, first_product=128:34982, bound_value=125:36801, second_product=250:35139, answer=235:70210)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` unflagged`, ` .`, `遁`, `�` (target ranks: base_value=64:71072, first_product=128:57335, bound_value=125:34400, second_product=250:43143, answer=235:29610)
- Layer 40: ` .`, ` .↵↵`, `�`, ` nasod`, ` .↵` (target ranks: base_value=64:17960, first_product=128:17051, bound_value=125:6427, second_product=250:16597, answer=235:9020)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, `坏` (target ranks: base_value=64:3518, first_product=128:4789, bound_value=125:1070, second_product=250:2610, answer=235:864)

### Filler position 48 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127441, first_product=128:126478, bound_value=125:125929, second_product=250:127006, answer=235:126378)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=64:10552, first_product=128:21383, bound_value=125:23245, second_product=250:19381, answer=235:21635)
- Layer 20: `东海`, `aharoa`, ` instantaneous`, `}<?`, `aplenty` (target ranks: base_value=64:113518, first_product=128:114483, bound_value=125:99182, second_product=250:74176, answer=235:118902)
- Layer 30: `codeline`, `东京`, `磨`, `lett`, `日产` (target ranks: base_value=64:106356, first_product=128:112872, bound_value=125:106299, second_product=250:90548, answer=235:110137)
- Layer 35: `codeline`, ` doubly`, `AssemblyVersion`, `白雪`, ` soci` (target ranks: base_value=64:111162, first_product=128:114519, bound_value=125:94856, second_product=250:83416, answer=235:124826)
- Layer 36: ` soci`, ` nasod`, `兜`, ` reduct`, ` Colleg` (target ranks: base_value=64:65487, first_product=128:70296, bound_value=125:69691, second_product=250:54384, answer=235:109452)
- Layer 37: `codeline`, `镶嵌`, `Quintal`, `TreeLabel`, `悬挂` (target ranks: base_value=64:113527, first_product=128:86277, bound_value=125:108651, second_product=250:80812, answer=235:111698)
- Layer 38: `肤`, `悬挂`, ` germ`, `悬`, ` .` (target ranks: base_value=64:70176, first_product=128:86507, bound_value=125:74821, second_product=250:65141, answer=235:91929)
- Layer 39: ` .`, ` .↵↵`, ` encomp`, ` unflagged`, `贻` (target ranks: base_value=64:104072, first_product=128:91528, bound_value=125:56529, second_product=250:70465, answer=235:90885)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, `�` (target ranks: base_value=64:67813, first_product=128:62565, bound_value=125:19327, second_product=250:39621, answer=235:59944)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=64:13663, first_product=128:11937, bound_value=125:2275, second_product=250:7366, answer=235:17353)

### Filler position 49 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127456, first_product=128:126485, bound_value=125:125946, second_product=250:127023, answer=235:126422)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10625, first_product=128:22722, bound_value=125:24550, second_product=250:19933, answer=235:22370)
- Layer 20: ` licensierad`, ` grounds`, `codeline`, `文本`, ` instantaneous` (target ranks: base_value=64:63236, first_product=128:79514, bound_value=125:81632, second_product=250:88316, answer=235:96116)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, ` Antwort` (target ranks: base_value=64:95991, first_product=128:105469, bound_value=125:103188, second_product=250:112707, answer=235:121517)
- Layer 35: ` Answer`, `codeline`, `oNames`, ` Antwort`, `AED` (target ranks: base_value=64:108825, first_product=128:105788, bound_value=125:76194, second_product=250:98023, answer=235:125015)
- Layer 36: ` Answer`, `坏`, `停`, ` answer`, ` nasod` (target ranks: base_value=64:60154, first_product=128:44691, bound_value=125:27550, second_product=250:65728, answer=235:118788)
- Layer 37: `oNames`, `codeline`, `insic`, ` consum`, ` retard` (target ranks: base_value=64:123877, first_product=128:109345, bound_value=125:96237, second_product=250:114246, answer=235:124687)
- Layer 38: `oNames`, ` retard`, `codeline`, `оду`, `�` (target ranks: base_value=64:126033, first_product=128:114441, bound_value=125:93100, second_product=250:109112, answer=235:119687)
- Layer 39: `�`, `oxygen`, `oNames`, `-ulo`, `deen` (target ranks: base_value=64:103408, first_product=128:116729, bound_value=125:73362, second_product=250:111338, answer=235:94559)
- Layer 40: ` wink`, ` .`, ` nasod`, ` Answer`, ` .↵↵` (target ranks: base_value=64:25621, first_product=128:82807, bound_value=125:22515, second_product=250:83389, answer=235:41738)
- Layer 41: ` .`, ` wink`, ` .↵↵`, ` Answer`, `叮` (target ranks: base_value=64:10284, first_product=128:49812, bound_value=125:9283, second_product=250:38345, answer=235:17705)

### Filler position 50 (absolute token 841, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=64:122444, first_product=128:115209, bound_value=125:112962, second_product=250:114199, answer=235:113859)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, `aplenty` (target ranks: base_value=64:127100, first_product=128:117727, bound_value=125:109457, second_product=250:106793, answer=235:112059)
- Layer 20: `能被`, `忑`, `ait`, `坷`, `��` (target ranks: base_value=64:9630, first_product=128:44301, bound_value=125:61084, second_product=250:46079, answer=235:65074)
- Layer 30: ` unflagged`, ` گزار`, `�`, `Descriptors`, ` 맞` (target ranks: base_value=64:23843, first_product=128:82806, bound_value=125:97458, second_product=250:107172, answer=235:124734)
- Layer 35: ` ninete`, `答案是`, ` Nineteenth`, `答案为`, ` talags` (target ranks: base_value=64:116101, first_product=128:128536, bound_value=125:125823, second_product=250:92662, answer=235:96267)
- Layer 36: ` Nineteenth`, `oNames`, `答案`, ` talags`, ` Paglin` (target ranks: base_value=64:93561, first_product=128:125693, bound_value=125:119918, second_product=250:89440, answer=235:86148)
- Layer 37: `oNames`, ` Nineteenth`, ` المتح`, `白光`, ` Paglin` (target ranks: base_value=64:117406, first_product=128:124333, bound_value=125:101450, second_product=250:78956, answer=235:67499)
- Layer 38: `oNames`, `lut`, ` المتح`, ` Paglin`, `创作` (target ranks: base_value=64:116966, first_product=128:123791, bound_value=125:113273, second_product=250:105160, answer=235:54706)
- Layer 39: `答案`, ` Answer`, ` answer`, ` Antwort`, ` ответ` (target ranks: base_value=64:120783, first_product=128:124601, bound_value=125:98364, second_product=250:90853, answer=235:15530)
- Layer 40: ` Answer`, `Answer`, ` answer`, `_answer`, `answer` (target ranks: base_value=64:93905, first_product=128:86633, bound_value=125:50735, second_product=250:53223, answer=235:9422)
- Layer 41: `Answer`, ` Answer`, ` answer`, `answer`, `答案` (target ranks: base_value=64:31975, first_product=128:43252, bound_value=125:17924, second_product=250:17403, answer=235:14535)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>qin = 67
xag = 23
kur = 64
rek = twice the number for kur minus 28
xav = twice the number for kur minus 3
Question: What is twice the number for xav minus 15?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
