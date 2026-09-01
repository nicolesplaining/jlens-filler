# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `374` (correct).
- No-filler answer: `322` (incorrect).
- Filler tokens: 50 tokens at absolute indices 801–850.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=97` | 1 (L24, filler 15) | L24, filler 4 (rank 5) |
| J-Lens | `first_product=194` | 27 (L31, filler 35) | Never |
| J-Lens | `bound_value=173` | 1 (L31, filler 4) | L31, filler 4 (rank 1) |
| J-Lens | `second_product=346` | 1 (L31, filler 15) | L31, filler 4 (rank 3) |
| J-Lens | `answer=374` | 1 (L36, filler 10) | L35, filler 12 (rank 10) |
| Logit lens | `base_value=97` | 1 (L24, filler 14) | L24, filler 14 (rank 1) |
| Logit lens | `first_product=194` | 11 (L30, filler 10) | Never |
| Logit lens | `bound_value=173` | 1 (L31, filler 16) | L31, filler 4 (rank 10) |
| Logit lens | `second_product=346` | 1 (L33, filler 4) | L31, filler 15 (rank 4) |
| Logit lens | `answer=374` | 1 (L36, filler 10) | L35, filler 10 (rank 8) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 801, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=97:117821, first_product=194:111583, bound_value=173:113877, second_product=346:112985, answer=374:113134)
- Layer 10: `anta`, `fine`, `locked`, `钩`, `勾` (target ranks: base_value=97:51964, first_product=194:52264, bound_value=173:60109, second_product=346:39043, answer=374:49275)
- Layer 20: ` .`, `足`, `扣`, `垂`, `梯` (target ranks: base_value=97:5695, first_product=194:22342, bound_value=173:20204, second_product=346:9494, answer=374:19482)
- Layer 30: ` talags`, ` pakig`, `期望`, `回答`, `त्तर` (target ranks: base_value=97:14761, first_product=194:33358, bound_value=173:76829, second_product=346:75074, answer=374:21492)
- Layer 35: `计算`, `68`, `calcul`, `推算`, `计算的` (target ranks: base_value=97:269, first_product=194:1810, bound_value=173:1949, second_product=346:1719, answer=374:587)
- Layer 36: ` talags`, `calcul`, `acin`, `计算`, `计算的` (target ranks: base_value=97:931, first_product=194:5349, bound_value=173:2128, second_product=346:1236, answer=374:724)
- Layer 37: ` talags`, ` hydrodynamic`, ` Paglin`, ` floating`, `geal` (target ranks: base_value=97:15220, first_product=194:23402, bound_value=173:7359, second_product=346:5154, answer=374:1724)
- Layer 38: ` talags`, ` hydrodynamic`, `geal`, `打磨`, `osine` (target ranks: base_value=97:48936, first_product=194:25649, bound_value=173:11267, second_product=346:8337, answer=374:5014)
- Layer 39: ` talags`, `-ulo`, `-ulan`, ` hilabihan`, ` hydrodynamic` (target ranks: base_value=97:127231, first_product=194:118848, bound_value=173:109143, second_product=346:31962, answer=374:50820)
- Layer 40: ` talags`, `oooo`, ` nasod`, `onos`, `一个一个` (target ranks: base_value=97:127328, first_product=194:118920, bound_value=173:96649, second_product=346:8603, answer=374:41265)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` separately` (target ranks: base_value=97:120674, first_product=194:96632, bound_value=173:75187, second_product=346:38154, answer=374:39998)

### Filler position 2 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: base_value=97:119385, first_product=194:113690, bound_value=173:116341, second_product=346:118918, answer=374:117106)
- Layer 10: ` Walker`, `ait`, `Walker`, `挪`, `atile` (target ranks: base_value=97:25761, first_product=194:33906, bound_value=173:40769, second_product=346:29505, answer=374:35157)
- Layer 20: ` .----`, `往常`, `oraly`, `}<?`, `ools` (target ranks: base_value=97:128782, first_product=194:123815, bound_value=173:128788, second_product=346:125159, answer=374:127378)
- Layer 30: ` pakig`, ` talags`, `��`, ` gilay`, ` .` (target ranks: base_value=97:121540, first_product=194:122316, bound_value=173:128837, second_product=346:118907, answer=374:113057)
- Layer 35: `滴水`, ` hilabihan`, ` .`, `ilig`, `空空` (target ranks: base_value=97:117320, first_product=194:124138, bound_value=173:128106, second_product=346:112759, answer=374:123115)
- Layer 36: `停`, ` talags`, `adows`, `幽`, `空空` (target ranks: base_value=97:91350, first_product=194:119371, bound_value=173:122996, second_product=346:89916, answer=374:115655)
- Layer 37: `}<?`, ` Erkännande`, ` hilabihan`, `�乐`, `aplenty` (target ranks: base_value=97:122858, first_product=194:126524, bound_value=173:127193, second_product=346:113058, answer=374:126648)
- Layer 38: ` .`, ` Erkännande`, `enclose`, ` .↵↵`, `繁体` (target ranks: base_value=97:125310, first_product=194:121417, bound_value=173:125124, second_product=346:103303, answer=374:125672)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>`, ` nasod` (target ranks: base_value=97:125678, first_product=194:106246, bound_value=173:99856, second_product=346:86009, answer=374:113707)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` filler` (target ranks: base_value=97:107643, first_product=194:71502, bound_value=173:52843, second_product=346:44039, answer=374:78233)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` 。` (target ranks: base_value=97:37226, first_product=194:16783, bound_value=173:10388, second_product=346:10508, answer=374:19969)

### Filler position 3 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122708, first_product=194:115154, bound_value=173:117421, second_product=346:121282, answer=374:119418)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=97:16779, first_product=194:28059, bound_value=173:29143, second_product=346:25348, answer=374:29414)
- Layer 20: `ait`, `忑`, `saurus`, `ashi`, ` ternary` (target ranks: base_value=97:11108, first_product=194:23000, bound_value=173:30848, second_product=346:23617, answer=374:36162)
- Layer 30: ` variable`, `variable`, `虚构`, ` variables`, ` Variable` (target ranks: base_value=97:25796, first_product=194:61964, bound_value=173:71809, second_product=346:81758, answer=374:68673)
- Layer 35: ` variable`, ` Variable`, `variable`, ` variables`, `Variable` (target ranks: base_value=97:11207, first_product=194:29514, bound_value=173:63001, second_product=346:63262, answer=374:55910)
- Layer 36: ` variable`, ` variables`, `变量的`, `variable`, ` definitions` (target ranks: base_value=97:8565, first_product=194:36399, bound_value=173:61563, second_product=346:73082, answer=374:60162)
- Layer 37: `变量的`, ` variables`, ` variable`, `variables`, `Variables` (target ranks: base_value=97:45623, first_product=194:71746, bound_value=173:96832, second_product=346:111029, answer=374:90620)
- Layer 38: `变量的`, `variables`, ` variables`, `混乱`, ` перемен` (target ranks: base_value=97:88285, first_product=194:84834, bound_value=173:100791, second_product=346:99674, answer=374:94350)
- Layer 39: `script`, `hemer`, `树叶`, `文字的`, `繁体` (target ranks: base_value=97:118628, first_product=194:128073, bound_value=173:121608, second_product=346:111261, answer=374:116743)
- Layer 40: ` dotted`, `acl`, `script`, `hemer`, `定义的` (target ranks: base_value=97:107172, first_product=194:127962, bound_value=173:106502, second_product=346:114040, answer=374:119016)
- Layer 41: ` .`, ` dotted`, ` dots`, ` ,`, `试一试` (target ranks: base_value=97:78078, first_product=194:119546, bound_value=173:87006, second_product=346:45968, answer=374:80071)

### Filler position 4 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:123557, first_product=194:117258, bound_value=173:118329, second_product=346:122463, answer=374:121155)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: base_value=97:14439, first_product=194:25444, bound_value=173:25392, second_product=346:21806, answer=374:26861)
- Layer 20: `幽`, `ait`, `足`, ` LS`, `Ta` (target ranks: base_value=97:14343, first_product=194:25060, bound_value=173:45302, second_product=346:25781, answer=374:27814)
- Layer 30: `otta`, `常规`, `反复`, `聂`, `escap` (target ranks: base_value=97:5660, first_product=194:12458, bound_value=173:43, second_product=346:10922, answer=374:28619)
- Layer 35: `346`, `345`, ` dinhi`, ` sumala`, ` dripping` (target ranks: base_value=97:125438, first_product=194:96696, bound_value=173:28947, second_product=346:1, answer=374:24635)
- Layer 36: `346`, `345`, `aplenty`, ` proiektuak`, `Giya` (target ranks: base_value=97:128543, first_product=194:122791, bound_value=173:9801, second_product=346:1, answer=374:25519)
- Layer 37: `346`, `345`, `思`, `زياح`, `326` (target ranks: base_value=97:128813, first_product=194:121651, bound_value=173:7790, second_product=346:1, answer=374:20260)
- Layer 38: `346`, `345`, `膝`, `326`, ` Epic` (target ranks: base_value=97:127928, first_product=194:119382, bound_value=173:6603, second_product=346:1, answer=374:13132)
- Layer 39: `346`, `迷惑`, ` Engle`, `膝`, `思` (target ranks: base_value=97:128353, first_product=194:123032, bound_value=173:62655, second_product=346:1, answer=374:57013)
- Layer 40: `346`, `思`, `所思`, `arina`, `anine` (target ranks: base_value=97:128559, first_product=194:123056, bound_value=173:101416, second_product=346:1, answer=374:53363)
- Layer 41: `346`, ` .`, `所思`, ` woo`, `因为` (target ranks: base_value=97:127643, first_product=194:121930, bound_value=173:96020, second_product=346:1, answer=374:75099)

### Filler position 5 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:122741, first_product=194:117141, bound_value=173:118045, second_product=346:122148, answer=374:120857)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: base_value=97:15486, first_product=194:28416, bound_value=173:27628, second_product=346:23882, answer=374:29146)
- Layer 20: `幽`, ` LS`, `能被`, `鞍`, `足` (target ranks: base_value=97:34716, first_product=194:38665, bound_value=173:51288, second_product=346:27296, answer=374:33782)
- Layer 30: ` No`, `推算`, ` Nova`, `算出`, `计算` (target ranks: base_value=97:14692, first_product=194:57612, bound_value=173:116916, second_product=346:107961, answer=374:38711)
- Layer 35: `推算`, ` No`, `分解`, ` Ho`, `计算` (target ranks: base_value=97:6406, first_product=194:55529, bound_value=173:110870, second_product=346:97609, answer=374:39315)
- Layer 36: `推算`, `calcul`, `分解`, `计算方法`, `计算` (target ranks: base_value=97:10059, first_product=194:49388, bound_value=173:107724, second_product=346:73232, answer=374:21907)
- Layer 37: `计算方法`, `wof`, ` Nij`, `rof`, `calcul` (target ranks: base_value=97:32043, first_product=194:64930, bound_value=173:112965, second_product=346:102376, answer=374:25462)
- Layer 38: `wof`, `}<?`, `osz`, `东海`, `计算方法` (target ranks: base_value=97:48912, first_product=194:56977, bound_value=173:113151, second_product=346:105476, answer=374:38834)
- Layer 39: ` Noruwega`, `东海`, ` Nog`, ` No`, `wof` (target ranks: base_value=97:104754, first_product=194:118446, bound_value=173:126127, second_product=346:121228, answer=374:84294)
- Layer 40: ` no`, `无`, ` No`, ` talags`, `坏` (target ranks: base_value=97:87524, first_product=194:111978, bound_value=173:114777, second_product=346:98945, answer=374:60853)
- Layer 41: ` .`, `坏`, `鹉`, ` no`, `实在` (target ranks: base_value=97:57657, first_product=194:98765, bound_value=173:83270, second_product=346:35767, answer=374:35136)

### Filler position 6 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:122508, first_product=194:116812, bound_value=173:117854, second_product=346:121830, answer=374:120491)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:13555, first_product=194:25431, bound_value=173:24892, second_product=346:21406, answer=374:25861)
- Layer 20: `鞍`, `足`, `cape`, `挪`, `胃癌` (target ranks: base_value=97:15041, first_product=194:26843, bound_value=173:34137, second_product=346:24988, answer=374:28851)
- Layer 30: `calcul`, `计算的`, `计算`, `算出`, ` calculate` (target ranks: base_value=97:4302, first_product=194:4177, bound_value=173:25015, second_product=346:15873, answer=374:4474)
- Layer 35: `calcul`, ` calculator`, `计算的`, `推算`, `计算` (target ranks: base_value=97:972, first_product=194:1657, bound_value=173:1894, second_product=346:844, answer=374:811)
- Layer 36: `calcul`, `推算`, `计算的`, `计算`, ` calcul` (target ranks: base_value=97:3684, first_product=194:3916, bound_value=173:4021, second_product=346:1148, answer=374:730)
- Layer 37: `calcul`, `计算的`, ` calcul`, `计算方法`, `计算` (target ranks: base_value=97:13581, first_product=194:4469, bound_value=173:1595, second_product=346:419, answer=374:148)
- Layer 38: `calcul`, `}<?`, ` talags`, ` calcul`, `计算方法` (target ranks: base_value=97:49333, first_product=194:9637, bound_value=173:5823, second_product=346:931, answer=374:401)
- Layer 39: `}<?`, `orten`, ` talags`, ` Noruwega`, `迷惑` (target ranks: base_value=97:128356, first_product=194:126410, bound_value=173:124303, second_product=346:16802, answer=374:34283)
- Layer 40: ` talags`, `323`, `orten`, `冰冰`, `迷惑` (target ranks: base_value=97:128314, first_product=194:128149, bound_value=173:127561, second_product=346:21500, answer=374:81666)
- Layer 41: ` .`, `323`, `鹉`, ` word`, `冰冰` (target ranks: base_value=97:125966, first_product=194:127001, bound_value=173:124496, second_product=346:20023, answer=374:74478)

### Filler position 7 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122322, first_product=194:116544, bound_value=173:117850, second_product=346:121788, answer=374:120311)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13337, first_product=194:25253, bound_value=173:24718, second_product=346:21342, answer=374:26365)
- Layer 20: `锁定`, `cape`, `Ta`, `ait`, `鞍` (target ranks: base_value=97:9778, first_product=194:23000, bound_value=173:32263, second_product=346:21109, answer=374:23059)
- Layer 30: ` calculator`, ` pakig`, `计算的`, `calculator`, `calcul` (target ranks: base_value=97:239, first_product=194:1313, bound_value=173:10796, second_product=346:8337, answer=374:1653)
- Layer 35: `328`, `保留`, `928`, `528`, ` calculator` (target ranks: base_value=97:2750, first_product=194:201, bound_value=173:10703, second_product=346:523, answer=374:375)
- Layer 36: ` pakig`, ` talags`, `328`, ` Septy`, `推断` (target ranks: base_value=97:23190, first_product=194:522, bound_value=173:28134, second_product=346:410, answer=374:232)
- Layer 37: ` pakig`, `}<?`, `328`, ` Septy`, `radesh` (target ranks: base_value=97:59381, first_product=194:2435, bound_value=173:21427, second_product=346:210, answer=374:115)
- Layer 38: `}<?`, `328`, `殿堂`, ` pakig`, `324` (target ranks: base_value=97:108452, first_product=194:4424, bound_value=173:36348, second_product=346:197, answer=374:84)
- Layer 39: `}<?`, `324`, `叶子`, `三百`, `hemer` (target ranks: base_value=97:128459, first_product=194:124854, bound_value=173:128048, second_product=346:941, answer=374:6925)
- Layer 40: `324`, `325`, `323`, `316`, `322` (target ranks: base_value=97:128309, first_product=194:128168, bound_value=173:127650, second_product=346:160, answer=374:11631)
- Layer 41: `323`, `325`, `324`, `316`, ` .` (target ranks: base_value=97:125306, first_product=194:126512, bound_value=173:123574, second_product=346:544, answer=374:28138)

### Filler position 8 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122292, first_product=194:116299, bound_value=173:117855, second_product=346:121744, answer=374:120132)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12313, first_product=194:24725, bound_value=173:24260, second_product=346:20900, answer=374:26541)
- Layer 20: `ait`, ` Walker`, `挪`, `锁定`, `会成为` (target ranks: base_value=97:16977, first_product=194:40117, bound_value=173:54451, second_product=346:32510, answer=374:42389)
- Layer 30: `第一步`, `计算的`, `算出`, `推算`, `的第一步` (target ranks: base_value=97:25155, first_product=194:75792, bound_value=173:121109, second_product=346:115437, answer=374:101266)
- Layer 35: `Tap`, ` tap`, `asuk`, ` x`, `鞍` (target ranks: base_value=97:11365, first_product=194:30933, bound_value=173:90472, second_product=346:87364, answer=374:59191)
- Layer 36: `私`, `留存`, `年开始`, ` tap`, `分解` (target ranks: base_value=97:13281, first_product=194:36615, bound_value=173:102523, second_product=346:86039, answer=374:58778)
- Layer 37: `}<?`, `zuf`, ` Zad`, `明珠`, `退役` (target ranks: base_value=97:38379, first_product=194:56034, bound_value=173:116395, second_product=346:113228, answer=374:72315)
- Layer 38: `}<?`, ` duc`, ` Duc`, `zat`, `zuf` (target ranks: base_value=97:50417, first_product=194:73634, bound_value=173:120422, second_product=346:115896, answer=374:94161)
- Layer 39: ` duc`, `}<?`, ` Duc`, `duc`, `zat` (target ranks: base_value=97:86840, first_product=194:116582, bound_value=173:123793, second_product=346:118137, answer=374:96672)
- Layer 40: `duc`, `šk`, ` duc`, `zuf`, `ukt` (target ranks: base_value=97:62718, first_product=194:117839, bound_value=173:119541, second_product=346:106830, answer=374:79888)
- Layer 41: ` .`, `鹉`, `<｜end▁of▁sentence｜>`, `šk`, ` ` (target ranks: base_value=97:32499, first_product=194:80631, bound_value=173:84618, second_product=346:38025, answer=374:27400)

### Filler position 9 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122477, first_product=194:116540, bound_value=173:118244, second_product=346:121931, answer=374:120353)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12954, first_product=194:25597, bound_value=173:25291, second_product=346:21883, answer=374:27334)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `挪` (target ranks: base_value=97:23701, first_product=194:37466, bound_value=173:50316, second_product=346:32619, answer=374:37820)
- Layer 30: ` tap`, `Tap`, ` Tap`, `平行`, `acos` (target ranks: base_value=97:11878, first_product=194:35128, bound_value=173:81744, second_product=346:61073, answer=374:20793)
- Layer 35: ` tap`, `Tap`, ` Tap`, `锁定`, `tap` (target ranks: base_value=97:3180, first_product=194:18802, bound_value=173:54263, second_product=346:46952, answer=374:14240)
- Layer 36: ` tap`, `留存`, ` Tap`, `Tap`, `翻` (target ranks: base_value=97:2782, first_product=194:16096, bound_value=173:57718, second_product=346:41283, answer=374:10037)
- Layer 37: `}<?`, `翻`, ` tap`, `留存`, `漏` (target ranks: base_value=97:8857, first_product=194:37493, bound_value=173:85238, second_product=346:71423, answer=374:15004)
- Layer 38: `}<?`, `zat`, `覆`, `筋`, `冰冰` (target ranks: base_value=97:17094, first_product=194:44328, bound_value=173:88630, second_product=346:78137, answer=374:36536)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ocyst`, `embl`, `打磨` (target ranks: base_value=97:86468, first_product=194:110071, bound_value=173:116908, second_product=346:110755, answer=374:87396)
- Layer 40: `冰冰`, `筋`, `语言文字`, `<｜begin▁of▁sentence｜>`, `zij` (target ranks: base_value=97:53516, first_product=194:97622, bound_value=173:95635, second_product=346:91017, answer=374:70700)
- Layer 41: ` .`, `鹉`, `<｜end▁of▁sentence｜>`, `省略`, ` ` (target ranks: base_value=97:26933, first_product=194:61652, bound_value=173:54705, second_product=346:47934, answer=374:36792)

### Filler position 10 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122686, first_product=194:116691, bound_value=173:118476, second_product=346:121980, answer=374:120383)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12505, first_product=194:25200, bound_value=173:24733, second_product=346:21486, answer=374:26937)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `挪` (target ranks: base_value=97:13800, first_product=194:23806, bound_value=173:36893, second_product=346:18125, answer=374:24604)
- Layer 30: `sett`, `328`, ` Sett`, ` settle`, ` Dietrich` (target ranks: base_value=97:2003, first_product=194:254, bound_value=173:1183, second_product=346:236, answer=374:206)
- Layer 35: `346`, `345`, `366`, `386`, `354` (target ranks: base_value=97:88575, first_product=194:344, bound_value=173:56871, second_product=346:1, answer=374:11)
- Layer 36: `374`, `376`, `373`, `366`, `370` (target ranks: base_value=97:121844, first_product=194:27600, bound_value=173:3342, second_product=346:19, answer=374:1)
- Layer 37: `374`, `376`, `366`, `373`, `372` (target ranks: base_value=97:125337, first_product=194:36391, bound_value=173:7194, second_product=346:20, answer=374:1)
- Layer 38: `374`, `373`, `372`, `376`, `366` (target ranks: base_value=97:129069, first_product=194:103478, bound_value=173:52582, second_product=346:37, answer=374:1)
- Layer 39: `374`, `372`, `373`, `370`, `375` (target ranks: base_value=97:128642, first_product=194:90959, bound_value=173:127592, second_product=346:5030, answer=374:1)
- Layer 40: `374`, `372`, `322`, `373`, `318` (target ranks: base_value=97:128694, first_product=194:101022, bound_value=173:121613, second_product=346:166, answer=374:1)
- Layer 41: `374`, `372`, `376`, `322`, `有的时候` (target ranks: base_value=97:125711, first_product=194:68901, bound_value=173:106324, second_product=346:1801, answer=374:1)

### Filler position 11 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122666, first_product=194:116932, bound_value=173:118689, second_product=346:122241, answer=374:120600)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12201, first_product=194:25318, bound_value=173:24530, second_product=346:21413, answer=374:26455)
- Layer 20: `ait`, ` smile`, `锁定`, ` wig`, `挪` (target ranks: base_value=97:15774, first_product=194:23932, bound_value=173:28154, second_product=346:25540, answer=374:28250)
- Layer 30: ` tap`, `Tap`, `acos`, ` glacier`, ` Tap` (target ranks: base_value=97:37589, first_product=194:41692, bound_value=173:95110, second_product=346:89461, answer=374:43590)
- Layer 35: ` tap`, `Tap`, ` Tap`, ` Gol`, ` Cogn` (target ranks: base_value=97:27892, first_product=194:41486, bound_value=173:90842, second_product=346:95038, answer=374:39829)
- Layer 36: `acin`, ` tap`, ` Gol`, ` rip`, `acos` (target ranks: base_value=97:23143, first_product=194:46549, bound_value=173:71083, second_product=346:61378, answer=374:26415)
- Layer 37: `acos`, `}<?`, ` Zad`, `ako`, `EDAC` (target ranks: base_value=97:60687, first_product=194:61735, bound_value=173:101742, second_product=346:88868, answer=374:41622)
- Layer 38: `}<?`, `zat`, `pac`, `�`, `�` (target ranks: base_value=97:81057, first_product=194:91129, bound_value=173:114661, second_product=346:102301, answer=374:78609)
- Layer 39: `}<?`, `zat`, `hemer`, ` Nij`, `?datasetId` (target ranks: base_value=97:96067, first_product=194:86405, bound_value=173:115930, second_product=346:62793, answer=374:38675)
- Layer 40: `zat`, `pac`, ` talags`, `zel`, `poons` (target ranks: base_value=97:68674, first_product=194:55960, bound_value=173:99777, second_product=346:31196, answer=374:9419)
- Layer 41: `鹉`, `所谓`, ` .`, ` Question`, `Question` (target ranks: base_value=97:23186, first_product=194:22367, bound_value=173:38042, second_product=346:4137, answer=374:247)

### Filler position 12 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122431, first_product=194:117007, bound_value=173:118710, second_product=346:122286, answer=374:120609)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12283, first_product=194:25835, bound_value=173:24380, second_product=346:21064, answer=374:25966)
- Layer 20: `锁定`, ` smile`, `ait`, `挪`, `鞍` (target ranks: base_value=97:11132, first_product=194:23451, bound_value=173:27085, second_product=346:18097, answer=374:20665)
- Layer 30: `acin`, ` Cogn`, ` rhe`, ` calculator`, `鞍` (target ranks: base_value=97:2716, first_product=194:598, bound_value=173:5762, second_product=346:2854, answer=374:384)
- Layer 35: `382`, `368`, `364`, `392`, `362` (target ranks: base_value=97:25250, first_product=194:351, bound_value=173:25766, second_product=346:11, answer=374:10)
- Layer 36: `376`, `382`, `368`, `374`, `364` (target ranks: base_value=97:86307, first_product=194:2433, bound_value=173:24846, second_product=346:11, answer=374:4)
- Layer 37: `376`, `382`, `368`, `366`, `374` (target ranks: base_value=97:120649, first_product=194:12704, bound_value=173:43286, second_product=346:13, answer=374:5)
- Layer 38: `368`, `366`, `376`, `}<?`, `364` (target ranks: base_value=97:126583, first_product=194:39602, bound_value=173:99160, second_product=346:20, answer=374:7)
- Layer 39: `372`, `374`, `}<?`, ` hydrodynamic`, `ozygous` (target ranks: base_value=97:128111, first_product=194:89201, bound_value=173:126130, second_product=346:235, answer=374:2)
- Layer 40: `374`, `324`, `372`, ` talags`, `下沉` (target ranks: base_value=97:128024, first_product=194:112624, bound_value=173:123853, second_product=346:145, answer=374:1)
- Layer 41: ` .`, `372`, `324`, `322`, `那两个` (target ranks: base_value=97:123799, first_product=194:98226, bound_value=173:104940, second_product=346:1639, answer=374:7)

### Filler position 13 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122324, first_product=194:116819, bound_value=173:118568, second_product=346:122198, answer=374:120506)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12421, first_product=194:25777, bound_value=173:24703, second_product=346:21624, answer=374:26288)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `忑` (target ranks: base_value=97:15702, first_product=194:29205, bound_value=173:40244, second_product=346:29710, answer=374:34512)
- Layer 30: `zuk`, `ukk`, ` basal`, `yak`, `zk` (target ranks: base_value=97:30727, first_product=194:83331, bound_value=173:125148, second_product=346:117662, answer=374:83501)
- Layer 35: `zuk`, ` zad`, ` Zad`, `auk`, ` Z` (target ranks: base_value=97:18683, first_product=194:47038, bound_value=173:118124, second_product=346:106277, answer=374:54726)
- Layer 36: `zuk`, ` Zad`, ` zad`, `留存`, `年开始` (target ranks: base_value=97:18137, first_product=194:49798, bound_value=173:115183, second_product=346:97123, answer=374:49430)
- Layer 37: `}<?`, `zuk`, ` Zad`, `ukkan`, `zak` (target ranks: base_value=97:59540, first_product=194:87548, bound_value=173:124160, second_product=346:118132, answer=374:82117)
- Layer 38: `}<?`, `zat`, `zuk`, `zv`, `ukkan` (target ranks: base_value=97:71715, first_product=194:100047, bound_value=173:125572, second_product=346:112133, answer=374:97250)
- Layer 39: `}<?`, `zat`, `zee`, `zyw`, `zv` (target ranks: base_value=97:108552, first_product=194:117498, bound_value=173:126689, second_product=346:111510, answer=374:101410)
- Layer 40: ` z`, ` Z`, `z`, `zij`, `.z` (target ranks: base_value=97:81678, first_product=194:119969, bound_value=173:120719, second_product=346:79099, answer=374:77081)
- Layer 41: ` .`, `鹉`, `那两个`, `没有被`, `出不穷` (target ranks: base_value=97:55976, first_product=194:86695, bound_value=173:87916, second_product=346:29670, answer=374:30466)

### Filler position 14 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122776, first_product=194:117029, bound_value=173:119055, second_product=346:122490, answer=374:120670)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12066, first_product=194:24350, bound_value=173:24536, second_product=346:20888, answer=374:25179)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `能被` (target ranks: base_value=97:10395, first_product=194:22060, bound_value=173:33941, second_product=346:18950, answer=374:24362)
- Layer 30: `acos`, `参赛`, `嫁`, `zko`, ` opera` (target ranks: base_value=97:35, first_product=194:12274, bound_value=173:818, second_product=346:4955, answer=374:26441)
- Layer 35: `346`, `345`, `347`, `acos`, ` dinhi` (target ranks: base_value=97:56481, first_product=194:66889, bound_value=173:4081, second_product=346:1, answer=374:28934)
- Layer 36: `346`, `345`, `Giya`, `347`, `aplenty` (target ranks: base_value=97:125165, first_product=194:118314, bound_value=173:4377, second_product=346:1, answer=374:26316)
- Layer 37: `346`, `aplenty`, `Giya`, `345`, ` sumala` (target ranks: base_value=97:128098, first_product=194:116426, bound_value=173:5266, second_product=346:1, answer=374:39942)
- Layer 38: `346`, ` sumala`, `345`, `oNames`, ` dinhi` (target ranks: base_value=97:128940, first_product=194:119363, bound_value=173:6708, second_product=346:1, answer=374:58769)
- Layer 39: `346`, ` sumala`, `iota`, `345`, `绳` (target ranks: base_value=97:128484, first_product=194:122414, bound_value=173:63031, second_product=346:1, answer=374:100020)
- Layer 40: `346`, `ascals`, `}<?`, ` sumala`, `scribe` (target ranks: base_value=97:128495, first_product=194:126388, bound_value=173:118937, second_product=346:1, answer=374:55349)
- Layer 41: `346`, ` .`, `那两个`, `ascals`, `有的时候` (target ranks: base_value=97:125999, first_product=194:116797, bound_value=173:87002, second_product=346:1, answer=374:29945)

### Filler position 15 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122786, first_product=194:117206, bound_value=173:119140, second_product=346:122563, answer=374:120778)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11726, first_product=194:23559, bound_value=173:24447, second_product=346:20477, answer=374:24561)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, `拆` (target ranks: base_value=97:10297, first_product=194:23059, bound_value=173:37296, second_product=346:18317, answer=374:23359)
- Layer 30: `反复`, `往外`, `�`, `熊`, `zko` (target ranks: base_value=97:624, first_product=194:12802, bound_value=173:22, second_product=346:842, answer=374:17535)
- Layer 35: `346`, `345`, `347`, `344`, `349` (target ranks: base_value=97:123410, first_product=194:90892, bound_value=173:31413, second_product=346:1, answer=374:14654)
- Layer 36: `346`, `345`, `326`, `347`, `aplenty` (target ranks: base_value=97:129073, first_product=194:125380, bound_value=173:30705, second_product=346:1, answer=374:11461)
- Layer 37: `346`, `345`, `326`, `aplenty`, `347` (target ranks: base_value=97:129221, first_product=194:125632, bound_value=173:43165, second_product=346:1, answer=374:18785)
- Layer 38: `346`, `326`, `345`, ` sumala`, `膝` (target ranks: base_value=97:129209, first_product=194:126280, bound_value=173:56904, second_product=346:1, answer=374:23398)
- Layer 39: `346`, `345`, ` sumala`, `窦`, `迷惑` (target ranks: base_value=97:129117, first_product=194:124844, bound_value=173:115415, second_product=346:1, answer=374:86639)
- Layer 40: `346`, `思`, ` sumala`, `所思`, `oine` (target ranks: base_value=97:128675, first_product=194:126909, bound_value=173:128103, second_product=346:1, answer=374:33537)
- Layer 41: `346`, `所思`, ` filler`, `因为`, `因为这些` (target ranks: base_value=97:128193, first_product=194:120556, bound_value=173:125261, second_product=346:1, answer=374:30870)

### Filler position 16 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122998, first_product=194:117655, bound_value=173:119690, second_product=346:122910, answer=374:121147)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12375, first_product=194:24224, bound_value=173:24327, second_product=346:20259, answer=374:25336)
- Layer 20: `ait`, `能被`, `锁定`, ` LS`, ` Walker` (target ranks: base_value=97:6377, first_product=194:18561, bound_value=173:27079, second_product=346:13860, answer=374:16652)
- Layer 30: `反复`, ` repeated`, ` repetitions`, `sets`, `93` (target ranks: base_value=97:44, first_product=194:3336, bound_value=173:11, second_product=346:2398, answer=374:6598)
- Layer 35: `173`, `346`, `373`, ` dinhi`, `347` (target ranks: base_value=97:42052, first_product=194:48716, bound_value=173:1, second_product=346:2, answer=374:11729)
- Layer 36: `346`, `173`, `陂`, `绳`, `Giya` (target ranks: base_value=97:120108, first_product=194:105539, bound_value=173:2, second_product=346:1, answer=374:33041)
- Layer 37: `346`, `173`, `bergh`, `绳`, `Giya` (target ranks: base_value=97:125604, first_product=194:90453, bound_value=173:2, second_product=346:1, answer=374:28740)
- Layer 38: `346`, `173`, `膝`, `anea`, `绳` (target ranks: base_value=97:127825, first_product=194:102642, bound_value=173:2, second_product=346:1, answer=374:40759)
- Layer 39: `346`, `绳`, `瞿`, `�`, `迷惑` (target ranks: base_value=97:128271, first_product=194:120866, bound_value=173:29, second_product=346:1, answer=374:85128)
- Layer 40: `346`, `ascals`, `bergh`, `解释`, `�` (target ranks: base_value=97:128063, first_product=194:125592, bound_value=173:14320, second_product=346:1, answer=374:40380)
- Layer 41: ` .`, `346`, `那两个`, `笔画`, `有的时候` (target ranks: base_value=97:123853, first_product=194:121105, bound_value=173:8844, second_product=346:2, answer=374:22432)

### Filler position 17 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:123176, first_product=194:117646, bound_value=173:119639, second_product=346:122792, answer=374:121038)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12923, first_product=194:24934, bound_value=173:24632, second_product=346:21317, answer=374:26003)
- Layer 20: ` smile`, `距`, `锁定`, `而此时`, ` engaging` (target ranks: base_value=97:13974, first_product=194:23501, bound_value=173:21197, second_product=346:19342, answer=374:19612)
- Layer 30: ` Tw`, ` twice`, `Tw`, `tw`, `.tw` (target ranks: base_value=97:3327, first_product=194:12921, bound_value=173:44884, second_product=346:30274, answer=374:14101)
- Layer 35: ` Tw`, `Tw`, `tw`, ` twice`, `.tw` (target ranks: base_value=97:801, first_product=194:5441, bound_value=173:27693, second_product=346:26859, answer=374:8999)
- Layer 36: ` Tw`, ` repeated`, `Tw`, `反复`, `翻` (target ranks: base_value=97:1033, first_product=194:4078, bound_value=173:30200, second_product=346:23879, answer=374:7038)
- Layer 37: ` Tw`, `翻`, ` doubling`, `calcul`, `}<?` (target ranks: base_value=97:1343, first_product=194:6068, bound_value=173:50484, second_product=346:60252, answer=374:13557)
- Layer 38: ` doubling`, `}<?`, ` Tw`, `zat`, `radesh` (target ranks: base_value=97:6254, first_product=194:6964, bound_value=173:58262, second_product=346:57739, answer=374:22476)
- Layer 39: `}<?`, `uerak`, `覆`, `uffman`, ` polar` (target ranks: base_value=97:32603, first_product=194:65397, bound_value=173:102098, second_product=346:91555, answer=374:67147)
- Layer 40: `坏`, ` Tw`, `ekak`, `俯`, `翻` (target ranks: base_value=97:11636, first_product=194:58404, bound_value=173:62494, second_product=346:29761, answer=374:47217)
- Layer 41: ` .`, `鹉`, ` `, `每次`, `坏` (target ranks: base_value=97:8307, first_product=194:44376, bound_value=173:52782, second_product=346:17412, answer=374:19720)

### Filler position 18 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:123573, first_product=194:118163, bound_value=173:120322, second_product=346:123480, answer=374:121683)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12136, first_product=194:24365, bound_value=173:24633, second_product=346:20769, answer=374:25582)
- Layer 20: ` Walker`, `ait`, ` engaging`, `忑`, `锁定` (target ranks: base_value=97:22332, first_product=194:33867, bound_value=173:43567, second_product=346:32600, answer=374:38382)
- Layer 30: `算出`, `计算的`, `计算出`, ` calculate`, `第一步` (target ranks: base_value=97:12025, first_product=194:41565, bound_value=173:90220, second_product=346:89745, answer=374:57912)
- Layer 35: ` first`, `第一步`, ` Ho`, `first`, ` calculator` (target ranks: base_value=97:3579, first_product=194:25446, bound_value=173:69398, second_product=346:64158, answer=374:44918)
- Layer 36: ` first`, `first`, `第一步`, `calcul`, ` primero` (target ranks: base_value=97:3773, first_product=194:25524, bound_value=173:67726, second_product=346:50021, answer=374:38352)
- Layer 37: `}<?`, ` first`, ` fir`, `FIR`, `不急` (target ranks: base_value=97:18102, first_product=194:44569, bound_value=173:96201, second_product=346:97934, answer=374:63425)
- Layer 38: `}<?`, `zat`, ` fir`, `ucl`, `ukkan` (target ranks: base_value=97:47233, first_product=194:54565, bound_value=173:112436, second_product=346:108006, answer=374:71094)
- Layer 39: `}<?`, ` fir`, `zat`, `-ulo`, `�` (target ranks: base_value=97:61959, first_product=194:68393, bound_value=173:109012, second_product=346:85813, answer=374:46289)
- Layer 40: ` h`, ` first`, `šk`, ` Tw`, ` pals` (target ranks: base_value=97:26250, first_product=194:71974, bound_value=173:77698, second_product=346:28947, answer=374:30338)
- Layer 41: `鹉`, ` first`, `šk`, ` no`, ` .` (target ranks: base_value=97:1100, first_product=194:27513, bound_value=173:17330, second_product=346:2299, answer=374:1414)

### Filler position 19 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:123820, first_product=194:118653, bound_value=173:120631, second_product=346:123706, answer=374:121964)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11990, first_product=194:24687, bound_value=173:24723, second_product=346:20354, answer=374:25076)
- Layer 20: `忑`, `ait`, ` Walker`, `锁定`, `能被` (target ranks: base_value=97:16048, first_product=194:36631, bound_value=173:37974, second_product=346:32665, answer=374:39365)
- Layer 30: `zim`, `oze`, ` pakig`, ` Zad`, ` rip` (target ranks: base_value=97:30367, first_product=194:121344, bound_value=173:127620, second_product=346:122716, answer=374:98585)
- Layer 35: ` riv`, `清楚楚`, ` Rot`, ` tap`, `zim` (target ranks: base_value=97:19049, first_product=194:93644, bound_value=173:120019, second_product=346:108316, answer=374:90108)
- Layer 36: ` zad`, ` riv`, `清楚楚`, `zim`, ` mim` (target ranks: base_value=97:27364, first_product=194:81832, bound_value=173:113020, second_product=346:83450, answer=374:76318)
- Layer 37: `斐`, `amol`, ` mim`, `zim`, `zor` (target ranks: base_value=97:71381, first_product=194:87724, bound_value=173:120523, second_product=346:108796, answer=374:85295)
- Layer 38: `本题分析`, `ked`, `斐`, `zat`, ` mim` (target ranks: base_value=97:95419, first_product=194:90775, bound_value=173:121041, second_product=346:106898, answer=374:96551)
- Layer 39: `ked`, `斐`, ` Nij`, `zat`, ` Zij` (target ranks: base_value=97:92785, first_product=194:96872, bound_value=173:118324, second_product=346:98336, answer=374:80045)
- Layer 40: `y`, `ked`, `zij`, `zor`, `迷惑` (target ranks: base_value=97:77711, first_product=194:106049, bound_value=173:109639, second_product=346:82005, answer=374:73233)
- Layer 41: `zel`, ` mim`, `外商投资`, ` .`, `zion` (target ranks: base_value=97:15285, first_product=194:38042, bound_value=173:72571, second_product=346:15877, answer=374:17356)

### Filler position 20 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:123665, first_product=194:118605, bound_value=173:120712, second_product=346:123858, answer=374:122018)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11857, first_product=194:24285, bound_value=173:23833, second_product=346:19594, answer=374:24667)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=97:12348, first_product=194:26432, bound_value=173:33652, second_product=346:22496, answer=374:24671)
- Layer 30: ` talags`, `acin`, `Tw`, ` pakig`, `calculator` (target ranks: base_value=97:8962, first_product=194:14831, bound_value=173:31729, second_product=346:17288, answer=374:4911)
- Layer 35: `346`, `345`, `382`, `368`, `364` (target ranks: base_value=97:45664, first_product=194:3244, bound_value=173:74017, second_product=346:1, answer=374:26)
- Layer 36: `376`, `368`, `366`, `370`, `374` (target ranks: base_value=97:121693, first_product=194:46623, bound_value=173:83762, second_product=346:13, answer=374:5)
- Layer 37: `376`, `368`, `366`, `362`, `372` (target ranks: base_value=97:126924, first_product=194:72927, bound_value=173:97066, second_product=346:16, answer=374:8)
- Layer 38: `368`, `366`, `364`, `376`, `374` (target ranks: base_value=97:128317, first_product=194:104295, bound_value=173:123675, second_product=346:27, answer=374:5)
- Layer 39: `374`, `372`, `364`, `368`, `370` (target ranks: base_value=97:128258, first_product=194:81949, bound_value=173:127356, second_product=346:937, answer=374:1)
- Layer 40: `374`, `372`, `368`, `376`, `364` (target ranks: base_value=97:128234, first_product=194:95801, bound_value=173:126158, second_product=346:110, answer=374:1)
- Layer 41: `374`, `372`, `376`, ` .`, `375` (target ranks: base_value=97:109695, first_product=194:64388, bound_value=173:106482, second_product=346:331, answer=374:1)

### Filler position 21 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:123751, first_product=194:118671, bound_value=173:120869, second_product=346:123979, answer=374:122106)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11327, first_product=194:23394, bound_value=173:23506, second_product=346:19583, answer=374:24403)
- Layer 20: `ait`, `锁定`, ` engaging`, ` Walker`, `距` (target ranks: base_value=97:18277, first_product=194:29563, bound_value=173:31702, second_product=346:21346, answer=374:32288)
- Layer 30: `acos`, `acin`, `嫁`, `平行`, `328` (target ranks: base_value=97:11286, first_product=194:2958, bound_value=173:9942, second_product=346:8102, answer=374:4626)
- Layer 35: `346`, `345`, `344`, `368`, ` surveying` (target ranks: base_value=97:32926, first_product=194:3325, bound_value=173:33813, second_product=346:1, answer=374:92)
- Layer 36: `368`, `370`, `372`, `376`, `373` (target ranks: base_value=97:103420, first_product=194:60597, bound_value=173:12835, second_product=346:26, answer=374:7)
- Layer 37: `376`, `368`, `372`, `370`, `373` (target ranks: base_value=97:115857, first_product=194:83075, bound_value=173:18205, second_product=346:32, answer=374:7)
- Layer 38: `374`, `372`, `373`, `368`, `376` (target ranks: base_value=97:126504, first_product=194:105621, bound_value=173:75319, second_product=346:88, answer=374:1)
- Layer 39: `374`, `372`, `370`, `373`, `368` (target ranks: base_value=97:127573, first_product=194:85661, bound_value=173:127751, second_product=346:15433, answer=374:1)
- Layer 40: `374`, `372`, `370`, `373`, `368` (target ranks: base_value=97:127569, first_product=194:89167, bound_value=173:120762, second_product=346:1198, answer=374:1)
- Layer 41: `372`, ` .`, `374`, `随便`, `有的时候` (target ranks: base_value=97:92975, first_product=194:72949, bound_value=173:96001, second_product=346:3884, answer=374:3)

### Filler position 22 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124206, first_product=194:119022, bound_value=173:121143, second_product=346:123981, answer=374:122289)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11275, first_product=194:23243, bound_value=173:23382, second_product=346:19267, answer=374:24260)
- Layer 20: `ait`, ` Walker`, `距`, `Walker`, `能被` (target ranks: base_value=97:13750, first_product=194:25066, bound_value=173:31290, second_product=346:15741, answer=374:24050)
- Layer 30: `acin`, `ession`, `粥`, `hg`, ` dy` (target ranks: base_value=97:211, first_product=194:19317, bound_value=173:56161, second_product=346:29752, answer=374:42385)
- Layer 35: `141`, `ession`, `分解`, `洋`, `acin` (target ranks: base_value=97:184, first_product=194:27831, bound_value=173:68058, second_product=346:33262, answer=374:44000)
- Layer 36: `}<?`, `141`, `tub`, `洋`, `期望` (target ranks: base_value=97:1556, first_product=194:45366, bound_value=173:97483, second_product=346:45714, answer=374:57137)
- Layer 37: `}<?`, `?datasetId`, ` Tub`, `tub`, `ASI` (target ranks: base_value=97:4756, first_product=194:59376, bound_value=173:105595, second_product=346:90188, answer=374:93429)
- Layer 38: `}<?`, `?datasetId`, ` Tub`, `ASI`, `取样` (target ranks: base_value=97:15545, first_product=194:78393, bound_value=173:116756, second_product=346:100731, answer=374:112208)
- Layer 39: `}<?`, `?datasetId`, `ASI`, `叶子`, `aharan` (target ranks: base_value=97:35838, first_product=194:99066, bound_value=173:124282, second_product=346:91377, answer=374:104444)
- Layer 40: `}<?`, ` Tw`, ` mediabestanden`, ` decom`, `arella` (target ranks: base_value=97:18450, first_product=194:81859, bound_value=173:82809, second_product=346:1859, answer=374:30624)
- Layer 41: ` .`, `不加`, ` `, ` (`, ` Tw` (target ranks: base_value=97:1820, first_product=194:39180, bound_value=173:59541, second_product=346:288, answer=374:7672)

### Filler position 23 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124234, first_product=194:119005, bound_value=173:121342, second_product=346:124115, answer=374:122268)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:11665, first_product=194:23958, bound_value=173:23642, second_product=346:19751, answer=374:24020)
- Layer 20: ` smile`, `足`, `幽`, `距`, ` LS` (target ranks: base_value=97:5214, first_product=194:12103, bound_value=173:17384, second_product=346:9891, answer=374:11969)
- Layer 30: `97`, ` twice`, ` Tw`, `96`, `Tw` (target ranks: base_value=97:1, first_product=194:1494, bound_value=173:45532, second_product=346:39207, answer=374:6610)
- Layer 35: `97`, ` twice`, ` Tw`, `Tw`, `tw` (target ranks: base_value=97:1, first_product=194:1604, bound_value=173:35040, second_product=346:32957, answer=374:20838)
- Layer 36: `97`, ` twice`, ` doubling`, ` Tw`, `970` (target ranks: base_value=97:1, first_product=194:1740, bound_value=173:49630, second_product=346:37372, answer=374:21800)
- Layer 37: `97`, ` doubling`, ` doubled`, ` doubles`, ` Nij` (target ranks: base_value=97:1, first_product=194:6225, bound_value=173:72671, second_product=346:79293, answer=374:46856)
- Layer 38: ` doubling`, ` doubled`, `97`, `}<?`, ` doubles` (target ranks: base_value=97:3, first_product=194:12986, bound_value=173:89887, second_product=346:89479, answer=374:70412)
- Layer 39: ` Noruwega`, ` Nij`, ` doubled`, `polar`, ` doubling` (target ranks: base_value=97:19, first_product=194:71475, bound_value=173:119507, second_product=346:64776, answer=374:43496)
- Layer 40: ` Tw`, ` n`, ` no`, `Tw`, ` No` (target ranks: base_value=97:5962, first_product=194:69572, bound_value=173:88359, second_product=346:3794, answer=374:4383)
- Layer 41: ` no`, ` .`, ` first`, `首先`, ` twisted` (target ranks: base_value=97:421, first_product=194:32930, bound_value=173:36071, second_product=346:98, answer=374:462)

### Filler position 24 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124630, first_product=194:119492, bound_value=173:121890, second_product=346:124358, answer=374:122673)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:11819, first_product=194:24932, bound_value=173:24445, second_product=346:19794, answer=374:24813)
- Layer 20: `足`, `ait`, ` smile`, `挪`, ` LS` (target ranks: base_value=97:6749, first_product=194:18661, bound_value=173:17284, second_product=346:13796, answer=374:21125)
- Layer 30: ` parallel`, `acin`, `平行`, `留存`, ` ES` (target ranks: base_value=97:1310, first_product=194:35272, bound_value=173:42133, second_product=346:31841, answer=374:13930)
- Layer 35: ` repetition`, `重复`, `羊`, `锁定`, `留存` (target ranks: base_value=97:416, first_product=194:29810, bound_value=173:46607, second_product=346:28301, answer=374:13655)
- Layer 36: `留存`, `羊`, `重复`, ` repeated`, ` repetition` (target ranks: base_value=97:347, first_product=194:22004, bound_value=173:47560, second_product=346:19983, answer=374:9412)
- Layer 37: `不急`, `}<?`, `坏`, `留存`, ` Nog` (target ranks: base_value=97:4539, first_product=194:48543, bound_value=173:91676, second_product=346:49612, answer=374:23070)
- Layer 38: `不急`, `}<?`, `坏`, `acy`, `留存` (target ranks: base_value=97:6681, first_product=194:44871, bound_value=173:89294, second_product=346:47550, answer=374:41194)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `东海`, `叶子`, `殿堂` (target ranks: base_value=97:40201, first_product=194:87645, bound_value=173:106762, second_product=346:67268, answer=374:64756)
- Layer 40: `坏`, ` Tw`, `<｜begin▁of▁sentence｜>`, `留存`, `殿堂` (target ranks: base_value=97:7897, first_product=194:49082, bound_value=173:74136, second_product=346:28606, answer=374:32492)
- Layer 41: ` .`, ` `, `每次`, ` no`, ` because` (target ranks: base_value=97:1849, first_product=194:20950, bound_value=173:40444, second_product=346:9486, answer=374:7424)

### Filler position 25 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124866, first_product=194:120106, bound_value=173:122484, second_product=346:124587, answer=374:123065)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11860, first_product=194:25230, bound_value=173:25356, second_product=346:20708, answer=374:25169)
- Layer 20: ` Walker`, `锁定`, `ait`, `Walker`, ` smile` (target ranks: base_value=97:8890, first_product=194:23879, bound_value=173:26796, second_product=346:19691, answer=374:26533)
- Layer 30: ` step`, ` labor`, `第一步`, ` Skills`, `Tw` (target ranks: base_value=97:25835, first_product=194:43823, bound_value=173:92575, second_product=346:86408, answer=374:56313)
- Layer 35: ` labor`, ` Tw`, ` step`, `Tw`, ` repetition` (target ranks: base_value=97:14375, first_product=194:42669, bound_value=173:97684, second_product=346:69062, answer=374:34811)
- Layer 36: ` Tw`, `留存`, ` Zad`, ` step`, `翻` (target ranks: base_value=97:14921, first_product=194:34964, bound_value=173:89312, second_product=346:50353, answer=374:24030)
- Layer 37: `}<?`, ` Zad`, `翻了`, `given`, `giv` (target ranks: base_value=97:85867, first_product=194:78244, bound_value=173:120285, second_product=346:104636, answer=374:64058)
- Layer 38: `}<?`, `zat`, `zv`, ` Zad`, `zp` (target ranks: base_value=97:92886, first_product=194:94536, bound_value=173:125144, second_product=346:113036, answer=374:94422)
- Layer 39: `}<?`, `zat`, `zv`, `zp`, `zam` (target ranks: base_value=97:113428, first_product=194:114480, bound_value=173:124076, second_product=346:105696, answer=374:95126)
- Layer 40: `zij`, `zat`, ` z`, `zl`, `zp` (target ranks: base_value=97:68618, first_product=194:104136, bound_value=173:114683, second_product=346:85428, answer=374:66358)
- Layer 41: `zij`, `zl`, `步骤如下`, ` .`, `šk` (target ranks: base_value=97:13404, first_product=194:37147, bound_value=173:65448, second_product=346:16305, answer=374:16550)

### Filler position 26 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124732, first_product=194:120005, bound_value=173:122479, second_product=346:124786, answer=374:123151)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11648, first_product=194:24100, bound_value=173:24909, second_product=346:20179, answer=374:23856)
- Layer 20: `ait`, ` Walker`, `Walker`, `锁定`, `拆` (target ranks: base_value=97:11235, first_product=194:24943, bound_value=173:31619, second_product=346:24999, answer=374:30551)
- Layer 30: ` labor`, ` Walker`, `Walker`, `acic`, ` eserc` (target ranks: base_value=97:40729, first_product=194:74219, bound_value=173:97880, second_product=346:76646, answer=374:73112)
- Layer 35: ` var`, ` labor`, `分解`, ` variable`, ` Walker` (target ranks: base_value=97:24604, first_product=194:49441, bound_value=173:86093, second_product=346:63932, answer=374:47587)
- Layer 36: ` Zad`, `分解`, ` zad`, ` var`, ` stabil` (target ranks: base_value=97:25866, first_product=194:49171, bound_value=173:81893, second_product=346:59850, answer=374:35102)
- Layer 37: `Variables`, `变量的`, ` variables`, `variables`, ` Variables` (target ranks: base_value=97:89449, first_product=194:92795, bound_value=173:115577, second_product=346:101353, answer=374:60791)
- Layer 38: `interpret`, `Variables`, `}<?`, ` definitions`, `变量的` (target ranks: base_value=97:100967, first_product=194:95655, bound_value=173:116872, second_product=346:92180, answer=374:64248)
- Layer 39: `变量的`, `variables`, ` Variables`, ` перемен`, `Variables` (target ranks: base_value=97:100686, first_product=194:112492, bound_value=173:111389, second_product=346:93516, answer=374:65789)
- Layer 40: `zij`, ` Zad`, `zat`, ` zad`, `扎` (target ranks: base_value=97:36359, first_product=194:106146, bound_value=173:85712, second_product=346:94256, answer=374:55801)
- Layer 41: ` definitions`, ` .`, `zij`, `zp`, `变量的` (target ranks: base_value=97:3077, first_product=194:46404, bound_value=173:42515, second_product=346:17391, answer=374:12948)

### Filler position 27 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124693, first_product=194:119982, bound_value=173:122537, second_product=346:124933, answer=374:123212)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11504, first_product=194:23208, bound_value=173:23888, second_product=346:19658, answer=374:23171)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` engaging` (target ranks: base_value=97:13426, first_product=194:23444, bound_value=173:33163, second_product=346:24185, answer=374:25875)
- Layer 30: `第一步`, `分解`, ` calculator`, `算出`, `calcul` (target ranks: base_value=97:5507, first_product=194:15496, bound_value=173:81751, second_product=346:50577, answer=374:25091)
- Layer 35: `分解`, ` calculator`, `第一步`, `calcul`, ` Tw` (target ranks: base_value=97:3923, first_product=194:10422, bound_value=173:85921, second_product=346:34515, answer=374:21522)
- Layer 36: `分解`, `第一步`, `calcul`, ` calculator`, `留存` (target ranks: base_value=97:5349, first_product=194:9284, bound_value=173:82399, second_product=346:26397, answer=374:12750)
- Layer 37: `calcul`, `分解`, `第一步`, `计算的`, `}<?` (target ranks: base_value=97:31814, first_product=194:23331, bound_value=173:111860, second_product=346:65614, answer=374:33662)
- Layer 38: `}<?`, `zat`, `calcul`, `覆`, `计算方法` (target ranks: base_value=97:40471, first_product=194:30581, bound_value=173:118689, second_product=346:78654, answer=374:50985)
- Layer 39: `zat`, `覆`, `迷惑`, `}<?`, ` Nij` (target ranks: base_value=97:66403, first_product=194:63291, bound_value=173:120441, second_product=346:88412, answer=374:52613)
- Layer 40: `zij`, `zat`, `oz`, `留存`, ` Tw` (target ranks: base_value=97:26033, first_product=194:40897, bound_value=173:101332, second_product=346:59093, answer=374:25534)
- Layer 41: ` no`, `zij`, `zl`, `oz`, `步骤如下` (target ranks: base_value=97:4295, first_product=194:16800, bound_value=173:41226, second_product=346:16188, answer=374:6838)

### Filler position 28 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:125128, first_product=194:120162, bound_value=173:122832, second_product=346:125020, answer=374:123329)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:11946, first_product=194:23700, bound_value=173:24037, second_product=346:19702, answer=374:24195)
- Layer 20: `ait`, `能被`, ` Walker`, `拆`, `Walker` (target ranks: base_value=97:14252, first_product=194:26976, bound_value=173:30907, second_product=346:16446, answer=374:22174)
- Layer 30: ` talags`, ` consuming`, `打交道`, `打完`, `entiful` (target ranks: base_value=97:295, first_product=194:6921, bound_value=173:2034, second_product=346:4041, answer=374:7030)
- Layer 35: `346`, `345`, `340`, `344`, `349` (target ranks: base_value=97:37334, first_product=194:16347, bound_value=173:52316, second_product=346:1, answer=374:840)
- Layer 36: `346`, `340`, `345`, `349`, `370` (target ranks: base_value=97:107847, first_product=194:67477, bound_value=173:44656, second_product=346:1, answer=374:78)
- Layer 37: `346`, `340`, `345`, `349`, `360` (target ranks: base_value=97:122884, first_product=194:61788, bound_value=173:45455, second_product=346:1, answer=374:61)
- Layer 38: `346`, `340`, `345`, `360`, `349` (target ranks: base_value=97:125552, first_product=194:88601, bound_value=173:93278, second_product=346:1, answer=374:43)
- Layer 39: `340`, `}<?`, `-ulo`, `370`, `迷惑` (target ranks: base_value=97:127479, first_product=194:95834, bound_value=173:123926, second_product=346:10, answer=374:49)
- Layer 40: `346`, `迷惑`, `三百`, `340`, ` twisted` (target ranks: base_value=97:126317, first_product=194:111593, bound_value=173:126545, second_product=346:1, answer=374:21)
- Layer 41: ` .`, `346`, ` waiting`, ` no`, `第三百` (target ranks: base_value=97:109750, first_product=194:88348, bound_value=173:104654, second_product=346:2, answer=374:31)

### Filler position 29 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124916, first_product=194:119847, bound_value=173:122462, second_product=346:124905, answer=374:123092)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12167, first_product=194:25144, bound_value=173:24728, second_product=346:20633, answer=374:25014)
- Layer 20: `ait`, `锁定`, `能被`, ` engaging`, `ession` (target ranks: base_value=97:16785, first_product=194:32940, bound_value=173:24422, second_product=346:17793, answer=374:27243)
- Layer 30: ` X`, ` x`, `拒`, `不值得`, `zuk` (target ranks: base_value=97:31152, first_product=194:26073, bound_value=173:54765, second_product=346:71224, answer=374:34006)
- Layer 35: ` X`, ` reserved`, ` x`, `感兴趣的`, `感兴趣` (target ranks: base_value=97:14094, first_product=194:19110, bound_value=173:49083, second_product=346:57080, answer=374:29493)
- Layer 36: `感兴趣`, `留存`, `感兴趣的`, ` X`, ` reserved` (target ranks: base_value=97:9455, first_product=194:18228, bound_value=173:52900, second_product=346:49599, answer=374:24747)
- Layer 37: `}<?`, `留存`, ` X`, ` XCT`, `zat` (target ranks: base_value=97:30188, first_product=194:31001, bound_value=173:82994, second_product=346:80170, answer=374:39539)
- Layer 38: `}<?`, `zat`, ` XCT`, ` x`, `迷惑` (target ranks: base_value=97:28345, first_product=194:39370, bound_value=173:90412, second_product=346:81577, answer=374:56690)
- Layer 39: `}<?`, `zat`, `迷惑`, `ozygous`, `东海` (target ranks: base_value=97:84499, first_product=194:100617, bound_value=173:113503, second_product=346:98763, answer=374:85941)
- Layer 40: ` x`, `坏`, `坏的`, `留存`, `坏了` (target ranks: base_value=97:52008, first_product=194:94008, bound_value=173:93750, second_product=346:59339, answer=374:58793)
- Layer 41: ` .`, ` waiting`, `等待`, ` `, `鹃` (target ranks: base_value=97:13868, first_product=194:44403, bound_value=173:52063, second_product=346:19652, answer=374:20981)

### Filler position 30 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124951, first_product=194:119944, bound_value=173:122412, second_product=346:124738, answer=374:123034)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11277, first_product=194:24742, bound_value=173:23614, second_product=346:19947, answer=374:23888)
- Layer 20: `cape`, ` smile`, `ait`, `足`, `锁定` (target ranks: base_value=97:10525, first_product=194:25554, bound_value=173:20947, second_product=346:17900, answer=374:24547)
- Layer 30: `第一步`, ` basal`, ` dy`, `yak`, `atan` (target ranks: base_value=97:19096, first_product=194:40930, bound_value=173:95575, second_product=346:97669, answer=374:50646)
- Layer 35: ` zad`, ` top`, `zuk`, ` tap`, `留存` (target ranks: base_value=97:31430, first_product=194:50505, bound_value=173:106065, second_product=346:112025, answer=374:56794)
- Layer 36: `留存`, ` zad`, `坏`, `radesh`, `zuk` (target ranks: base_value=97:29396, first_product=194:49628, bound_value=173:94360, second_product=346:101137, answer=374:43715)
- Layer 37: `}<?`, `zuk`, `radesh`, `ruk`, `坏` (target ranks: base_value=97:97730, first_product=194:82203, bound_value=173:118123, second_product=346:122293, answer=374:71378)
- Layer 38: `}<?`, `zat`, `迷惑`, `ukkan`, `zuk` (target ranks: base_value=97:95522, first_product=194:103014, bound_value=173:122881, second_product=346:121772, answer=374:98807)
- Layer 39: `}<?`, `zat`, `ozygous`, `zv`, `zyw` (target ranks: base_value=97:101634, first_product=194:113412, bound_value=173:121784, second_product=346:116181, answer=374:97349)
- Layer 40: `坏`, `acular`, `坏了`, `差错`, `acl` (target ranks: base_value=97:53514, first_product=194:108460, bound_value=173:109738, second_product=346:88995, answer=374:73424)
- Layer 41: `acular`, `鹉`, ` .`, ` no`, `zij` (target ranks: base_value=97:11932, first_product=194:51629, bound_value=173:65586, second_product=346:23178, answer=374:16701)

### Filler position 31 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:125346, first_product=194:120622, bound_value=173:123169, second_product=346:125326, answer=374:123663)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:10568, first_product=194:23504, bound_value=173:22827, second_product=346:19810, answer=374:23476)
- Layer 20: `锁定`, `鞍`, `ait`, ` smile`, ` LS` (target ranks: base_value=97:10484, first_product=194:19677, bound_value=173:21616, second_product=346:18391, answer=374:20847)
- Layer 30: `鞍`, ` tap`, `Tap`, `tap`, `calcul` (target ranks: base_value=97:18056, first_product=194:14397, bound_value=173:45661, second_product=346:28825, answer=374:11964)
- Layer 35: ` step`, ` tap`, `第一步`, `步骤`, `Tap` (target ranks: base_value=97:24570, first_product=194:18811, bound_value=173:44713, second_product=346:36192, answer=374:14435)
- Layer 36: ` tap`, ` step`, ` stabil`, `calcul`, `留存` (target ranks: base_value=97:16504, first_product=194:15821, bound_value=173:37180, second_product=346:32506, answer=374:11295)
- Layer 37: `}<?`, `不急`, `步骤`, ` step`, `radesh` (target ranks: base_value=97:56306, first_product=194:40453, bound_value=173:69198, second_product=346:72092, answer=374:23363)
- Layer 38: `}<?`, `不急`, `radesh`, `差错`, ` RES` (target ranks: base_value=97:72273, first_product=194:39076, bound_value=173:64343, second_product=346:74632, answer=374:29759)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ocyst`, ` RES`, `hemer` (target ranks: base_value=97:101648, first_product=194:73532, bound_value=173:75693, second_product=346:51329, answer=374:28061)
- Layer 40: `坏`, `坏的`, ` nasod`, ` embargo`, `acular` (target ranks: base_value=97:53364, first_product=194:39643, bound_value=173:41681, second_product=346:22793, answer=374:4349)
- Layer 41: ` .`, `坏`, `等待`, `<｜end▁of▁sentence｜>`, ` because` (target ranks: base_value=97:16543, first_product=194:16643, bound_value=173:13783, second_product=346:1982, answer=374:526)

### Filler position 32 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:125330, first_product=194:120639, bound_value=173:123211, second_product=346:125377, answer=374:123713)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:10672, first_product=194:22413, bound_value=173:22568, second_product=346:19427, answer=374:23561)
- Layer 20: ` ES`, ` LS`, ` Walker`, ` engaging`, `Walker` (target ranks: base_value=97:11309, first_product=194:22039, bound_value=173:24577, second_product=346:14518, answer=374:20102)
- Layer 30: `97`, `退出`, `acin`, `eder`, ` twice` (target ranks: base_value=97:1, first_product=194:5121, bound_value=173:4725, second_product=346:22509, answer=374:9325)
- Layer 35: `173`, `退出`, `退`, `退了`, ` twice` (target ranks: base_value=97:216, first_product=194:11490, bound_value=173:1, second_product=346:6624, answer=374:17864)
- Layer 36: `173`, `astro`, `�`, `iator`, `otrop` (target ranks: base_value=97:4014, first_product=194:28801, bound_value=173:1, second_product=346:4136, answer=374:44363)
- Layer 37: `173`, `}<?`, `TreeLabel`, `?datasetId`, `iator` (target ranks: base_value=97:23896, first_product=194:40407, bound_value=173:1, second_product=346:9150, answer=374:69668)
- Layer 38: `173`, `迷雾`, `副院长`, ` pals`, `TreeLabel` (target ranks: base_value=97:39011, first_product=194:70428, bound_value=173:1, second_product=346:11253, answer=374:88129)
- Layer 39: `173`, `迷雾`, `pet`, `acet`, `tanle` (target ranks: base_value=97:43263, first_product=194:71449, bound_value=173:1, second_product=346:6539, answer=374:60639)
- Layer 40: `迷雾`, `iator`, ` embargo`, ` pals`, `empel` (target ranks: base_value=97:46203, first_product=194:83699, bound_value=173:78, second_product=346:877, answer=374:15581)
- Layer 41: ` .`, `迷雾`, ` everywhere`, `步骤如下`, `2` (target ranks: base_value=97:12891, first_product=194:17080, bound_value=173:8, second_product=346:107, answer=374:3782)

### Filler position 33 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:125322, first_product=194:120781, bound_value=173:123292, second_product=346:125462, answer=374:123797)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:10241, first_product=194:22142, bound_value=173:22757, second_product=346:19151, answer=374:22634)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=97:9764, first_product=194:17931, bound_value=173:26145, second_product=346:14661, answer=374:23165)
- Layer 30: `鞍`, `acin`, `�`, `平行`, `sets` (target ranks: base_value=97:17279, first_product=194:49211, bound_value=173:74515, second_product=346:31727, answer=374:46028)
- Layer 35: ` var`, `adal`, ` quadr`, `acin`, `锁定` (target ranks: base_value=97:7404, first_product=194:24755, bound_value=173:38689, second_product=346:14008, answer=374:25152)
- Layer 36: ` talags`, `acin`, `adal`, `留存`, ` Min` (target ranks: base_value=97:11042, first_product=194:25932, bound_value=173:48272, second_product=346:13030, answer=374:19876)
- Layer 37: ` talags`, `}<?`, `不加`, ` Min`, `放下` (target ranks: base_value=97:41946, first_product=194:56232, bound_value=173:85048, second_product=346:37742, answer=374:33058)
- Layer 38: `}<?`, `不加`, `值班`, `osit`, `dividers` (target ranks: base_value=97:41750, first_product=194:44693, bound_value=173:83828, second_product=346:25201, answer=374:39517)
- Layer 39: `}<?`, `osit`, ` Harl`, ` talags`, `殿堂` (target ranks: base_value=97:65703, first_product=194:80799, bound_value=173:97574, second_product=346:67017, answer=374:77392)
- Layer 40: ` talags`, `留存`, `殿堂`, `šk`, `acular` (target ranks: base_value=97:17583, first_product=194:65690, bound_value=173:66185, second_product=346:61658, answer=374:69053)
- Layer 41: `没有被`, ` whichever`, `留存`, ` `, `šk` (target ranks: base_value=97:3071, first_product=194:35039, bound_value=173:38206, second_product=346:21282, answer=374:33894)

### Filler position 34 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:125756, first_product=194:121527, bound_value=173:124027, second_product=346:125953, answer=374:124451)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:10889, first_product=194:22074, bound_value=173:23049, second_product=346:19289, answer=374:22504)
- Layer 20: `ait`, ` Walker`, `锁定`, `能被`, `Walker` (target ranks: base_value=97:11742, first_product=194:24319, bound_value=173:28200, second_product=346:16356, answer=374:21423)
- Layer 30: ` twice`, ` Tw`, `Tw`, `tw`, `.tw` (target ranks: base_value=97:2363, first_product=194:9233, bound_value=173:54623, second_product=346:30915, answer=374:16092)
- Layer 35: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=97:1013, first_product=194:4777, bound_value=173:27067, second_product=346:22484, answer=374:9861)
- Layer 36: ` Tw`, ` twice`, `calcul`, `Tw`, `计算的` (target ranks: base_value=97:1484, first_product=194:5069, bound_value=173:34324, second_product=346:27966, answer=374:9483)
- Layer 37: ` doubling`, `acos`, `进行计算`, `calcul`, `计算的` (target ranks: base_value=97:9244, first_product=194:10126, bound_value=173:62853, second_product=346:63016, answer=374:23111)
- Layer 38: ` doubling`, `的计算`, `进行计算`, `计算的`, `计算方法` (target ranks: base_value=97:19423, first_product=194:14198, bound_value=173:78145, second_product=346:64518, answer=374:34791)
- Layer 39: `的计算`, `}<?`, ` doubling`, ` Tw`, ` doubled` (target ranks: base_value=97:27936, first_product=194:34341, bound_value=173:73144, second_product=346:33216, answer=374:17725)
- Layer 40: ` Tw`, `zij`, `的计算`, `eland`, ` ` (target ranks: base_value=97:1331, first_product=194:17868, bound_value=173:15068, second_product=346:1665, answer=374:3560)
- Layer 41: ` `, ` twist`, `2`, `的计算`, ` twice` (target ranks: base_value=97:340, first_product=194:5756, bound_value=173:11216, second_product=346:516, answer=374:414)

### Filler position 35 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=97:125724, first_product=194:121243, bound_value=173:123832, second_product=346:125730, answer=374:124141)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12203, first_product=194:23122, bound_value=173:23682, second_product=346:20035, answer=374:23483)
- Layer 20: ` smile`, `ait`, `足`, `胃癌`, `锁定` (target ranks: base_value=97:7415, first_product=194:11387, bound_value=173:13306, second_product=346:11731, answer=374:13171)
- Layer 30: `328`, `acet`, `翻了`, `Conc`, `382` (target ranks: base_value=97:6084, first_product=194:172, bound_value=173:1638, second_product=346:5542, answer=374:1063)
- Layer 35: `368`, `382`, `364`, `392`, `384` (target ranks: base_value=97:39332, first_product=194:126, bound_value=173:16608, second_product=346:9, answer=374:17)
- Layer 36: `368`, `376`, `382`, `366`, `370` (target ranks: base_value=97:114205, first_product=194:4241, bound_value=173:24296, second_product=346:19, answer=374:8)
- Layer 37: `368`, `376`, `382`, `366`, `374` (target ranks: base_value=97:125762, first_product=194:19266, bound_value=173:37256, second_product=346:23, answer=374:5)
- Layer 38: `368`, `374`, `366`, `376`, `370` (target ranks: base_value=97:127501, first_product=194:33255, bound_value=173:87282, second_product=346:37, answer=374:2)
- Layer 39: `374`, `368`, `372`, `370`, `384` (target ranks: base_value=97:128197, first_product=194:52339, bound_value=173:120221, second_product=346:130, answer=374:1)
- Layer 40: `374`, `372`, `368`, `376`, `324` (target ranks: base_value=97:128520, first_product=194:97684, bound_value=173:120825, second_product=346:88, answer=374:1)
- Layer 41: `374`, `372`, `376`, `zilla`, `因为这些` (target ranks: base_value=97:119540, first_product=194:57791, bound_value=173:90752, second_product=346:530, answer=374:1)

### Filler position 36 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:125997, first_product=194:121570, bound_value=173:124313, second_product=346:125950, answer=374:124463)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13287, first_product=194:25091, bound_value=173:25157, second_product=346:21199, answer=374:25874)
- Layer 20: `能被`, `ait`, ` Walker`, ` engaging`, `拆` (target ranks: base_value=97:19269, first_product=194:31245, bound_value=173:29542, second_product=346:17338, answer=374:25858)
- Layer 30: `328`, `selling`, `}<?`, ` kahaboga`, `sett` (target ranks: base_value=97:5875, first_product=194:3147, bound_value=173:1682, second_product=346:462, answer=374:3878)
- Layer 35: `346`, `345`, `366`, `344`, `376` (target ranks: base_value=97:82654, first_product=194:4881, bound_value=173:28009, second_product=346:1, answer=374:21)
- Layer 36: `376`, `373`, `374`, `370`, `372` (target ranks: base_value=97:111472, first_product=194:72380, bound_value=173:253, second_product=346:30, answer=374:3)
- Layer 37: `376`, `373`, `374`, `372`, `375` (target ranks: base_value=97:114956, first_product=194:87525, bound_value=173:316, second_product=346:34, answer=374:3)
- Layer 38: `374`, `373`, `372`, `376`, `375` (target ranks: base_value=97:128867, first_product=194:119423, bound_value=173:18185, second_product=346:412, answer=374:1)
- Layer 39: `374`, `373`, `372`, `375`, `371` (target ranks: base_value=97:127893, first_product=194:112530, bound_value=173:117066, second_product=346:5085, answer=374:1)
- Layer 40: `374`, `372`, `373`, `370`, `371` (target ranks: base_value=97:127673, first_product=194:112854, bound_value=173:100934, second_product=346:2261, answer=374:1)
- Layer 41: `374`, `372`, `373`, `375`, `有的时候` (target ranks: base_value=97:112773, first_product=194:82710, bound_value=173:94835, second_product=346:7237, answer=374:1)

### Filler position 37 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=97:126171, first_product=194:122028, bound_value=173:124697, second_product=346:126163, answer=374:124752)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12929, first_product=194:25516, bound_value=173:25481, second_product=346:21722, answer=374:26542)
- Layer 20: `能被`, ` engaging`, `忑`, ` Walker`, ` Engaging` (target ranks: base_value=97:17212, first_product=194:35522, bound_value=173:28685, second_product=346:24354, answer=374:26733)
- Layer 30: `78`, ` dy`, `退出`, `acin`, `算出` (target ranks: base_value=97:843, first_product=194:27614, bound_value=173:50572, second_product=346:48411, answer=374:35167)
- Layer 35: `141`, `出生`, `ession`, `78`, `忽略` (target ranks: base_value=97:3090, first_product=194:50806, bound_value=173:39942, second_product=346:48682, answer=374:40545)
- Layer 36: `141`, `翻`, `}<?`, `ASI`, `radesh` (target ranks: base_value=97:20379, first_product=194:76856, bound_value=173:74245, second_product=346:82047, answer=374:52293)
- Layer 37: `}<?`, `141`, `?datasetId`, `ASI`, `ajes` (target ranks: base_value=97:68288, first_product=194:81051, bound_value=173:85780, second_product=346:107182, answer=374:73722)
- Layer 38: `}<?`, `zat`, `141`, ` polar`, `polar` (target ranks: base_value=97:89292, first_product=194:91137, bound_value=173:97515, second_product=346:112222, answer=374:100823)
- Layer 39: `}<?`, `�乐`, `叶子`, `ounder`, `ozygous` (target ranks: base_value=97:105781, first_product=194:105827, bound_value=173:108866, second_product=346:77387, answer=374:55407)
- Layer 40: `}<?`, `empel`, `zat`, `迷惑`, `acular` (target ranks: base_value=97:51307, first_product=194:86401, bound_value=173:70860, second_product=346:11349, answer=374:2770)
- Layer 41: ` `, ` because`, ` without`, ` waiting`, ` .` (target ranks: base_value=97:8829, first_product=194:24632, bound_value=173:28001, second_product=346:661, answer=374:54)

### Filler position 38 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:126064, first_product=194:122005, bound_value=173:124502, second_product=346:126029, answer=374:124629)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11645, first_product=194:24459, bound_value=173:24216, second_product=346:20925, answer=374:24868)
- Layer 20: `忑`, `ait`, `能被`, ` engaging`, ` ES` (target ranks: base_value=97:13213, first_product=194:33439, bound_value=173:43897, second_product=346:30808, answer=374:36285)
- Layer 30: `北斗`, ` Dietrich`, ` kahaboga`, ` Nova`, `selling` (target ranks: base_value=97:3906, first_product=194:3431, bound_value=173:3806, second_product=346:2884, answer=374:8290)
- Layer 35: `346`, `345`, `366`, `382`, `386` (target ranks: base_value=97:86410, first_product=194:6848, bound_value=173:81401, second_product=346:1, answer=374:42)
- Layer 36: `376`, `366`, `370`, `372`, `374` (target ranks: base_value=97:119693, first_product=194:75586, bound_value=173:22615, second_product=346:16, answer=374:5)
- Layer 37: `376`, `366`, `368`, `374`, `370` (target ranks: base_value=97:120592, first_product=194:80176, bound_value=173:37000, second_product=346:21, answer=374:4)
- Layer 38: `374`, `376`, `366`, `368`, `372` (target ranks: base_value=97:128105, first_product=194:123446, bound_value=173:110460, second_product=346:33, answer=374:1)
- Layer 39: `368`, `374`, `372`, `370`, `369` (target ranks: base_value=97:127636, first_product=194:112123, bound_value=173:128693, second_product=346:1192, answer=374:2)
- Layer 40: `368`, `372`, `374`, `370`, `366` (target ranks: base_value=97:128285, first_product=194:117835, bound_value=173:128160, second_product=346:214, answer=374:3)
- Layer 41: `372`, ` nuest`, `376`, `374`, `368` (target ranks: base_value=97:118013, first_product=194:82636, bound_value=173:120663, second_product=346:4274, answer=374:4)

### Filler position 39 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:125885, first_product=194:121608, bound_value=173:124283, second_product=346:125969, answer=374:124370)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:11817, first_product=194:23612, bound_value=173:23620, second_product=346:19859, answer=374:23996)
- Layer 20: `ait`, `能被`, `忑`, `锁定`, ` engaging` (target ranks: base_value=97:9087, first_product=194:21402, bound_value=173:27076, second_product=346:14647, answer=374:20167)
- Layer 30: `328`, `}<?`, `292`, `selling`, ` seventy` (target ranks: base_value=97:3399, first_product=194:1076, bound_value=173:787, second_product=346:486, answer=374:974)
- Layer 35: `346`, `345`, `366`, `347`, `344` (target ranks: base_value=97:70653, first_product=194:909, bound_value=173:28389, second_product=346:1, answer=374:21)
- Layer 36: `366`, `370`, `373`, `374`, `376` (target ranks: base_value=97:113294, first_product=194:60164, bound_value=173:3106, second_product=346:16, answer=374:4)
- Layer 37: `366`, `374`, `373`, `376`, `370` (target ranks: base_value=97:114912, first_product=194:63030, bound_value=173:6936, second_product=346:17, answer=374:2)
- Layer 38: `374`, `366`, `373`, `372`, `370` (target ranks: base_value=97:128564, first_product=194:109581, bound_value=173:52789, second_product=346:24, answer=374:1)
- Layer 39: `374`, `372`, `370`, `373`, `368` (target ranks: base_value=97:128237, first_product=194:103291, bound_value=173:123631, second_product=346:402, answer=374:1)
- Layer 40: `374`, `372`, `370`, `373`, `366` (target ranks: base_value=97:128237, first_product=194:112992, bound_value=173:110758, second_product=346:32, answer=374:1)
- Layer 41: `374`, `372`, `<｜begin▁of▁file｜>`, `zony`, `因为这些` (target ranks: base_value=97:116900, first_product=194:75276, bound_value=173:91324, second_product=346:723, answer=374:1)

### Filler position 40 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:126076, first_product=194:121570, bound_value=173:124399, second_product=346:125942, answer=374:124324)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12975, first_product=194:24490, bound_value=173:25304, second_product=346:20928, answer=374:26206)
- Layer 20: `ait`, `锁定`, ` engaging`, ` Engaging`, `ätte` (target ranks: base_value=97:14111, first_product=194:31482, bound_value=173:27155, second_product=346:24542, answer=374:35883)
- Layer 30: `?datasetId`, `acos`, `}<?`, `sar`, `ِّف` (target ranks: base_value=97:6167, first_product=194:15279, bound_value=173:9434, second_product=346:28212, answer=374:33367)
- Layer 35: `346`, `345`, `366`, `俯`, `opan` (target ranks: base_value=97:30507, first_product=194:8863, bound_value=173:35963, second_product=346:1, answer=374:537)
- Layer 36: `366`, `368`, `370`, `372`, `323` (target ranks: base_value=97:98646, first_product=194:87701, bound_value=173:11463, second_product=346:81, answer=374:12)
- Layer 37: `366`, `368`, `372`, `370`, `371` (target ranks: base_value=97:109639, first_product=194:93647, bound_value=173:24911, second_product=346:212, answer=374:12)
- Layer 38: `366`, `368`, `372`, `322`, `323` (target ranks: base_value=97:126009, first_product=194:123773, bound_value=173:84889, second_product=346:155, answer=374:9)
- Layer 39: `368`, `372`, `366`, `370`, `374` (target ranks: base_value=97:128601, first_product=194:122609, bound_value=173:127550, second_product=346:15802, answer=374:5)
- Layer 40: `372`, `322`, `三百`, `374`, `368` (target ranks: base_value=97:128469, first_product=194:125400, bound_value=173:125888, second_product=346:1959, answer=374:4)
- Layer 41: `372`, `322`, `374`, `366`, `318` (target ranks: base_value=97:108607, first_product=194:80971, bound_value=173:79805, second_product=346:934, answer=374:3)

### Filler position 41 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=97:126164, first_product=194:121719, bound_value=173:124452, second_product=346:125971, answer=374:124400)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12738, first_product=194:23931, bound_value=173:24864, second_product=346:20495, answer=374:25856)
- Layer 20: `锁定`, `ait`, ` LS`, `LS`, `cape` (target ranks: base_value=97:6239, first_product=194:17507, bound_value=173:17995, second_product=346:10796, answer=374:14193)
- Layer 30: ` smoot`, ` basal`, `acos`, `sar`, `七十` (target ranks: base_value=97:207, first_product=194:24918, bound_value=173:2061, second_product=346:12113, answer=374:19300)
- Layer 35: `三十五`, `radesh`, `346`, `345`, ` dripping` (target ranks: base_value=97:18908, first_product=194:23588, bound_value=173:1843, second_product=346:3, answer=374:7510)
- Layer 36: `bergh`, `内膜`, `radesh`, `翻转`, ` mediabestanden` (target ranks: base_value=97:102286, first_product=194:39475, bound_value=173:1163, second_product=346:33, answer=374:2048)
- Layer 37: `内膜`, `翻转`, ` crossover`, `radesh`, `迷雾` (target ranks: base_value=97:118803, first_product=194:43657, bound_value=173:2171, second_product=346:66, answer=374:6763)
- Layer 38: `迷惑`, `内膜`, `迷雾`, `高山`, `radesh` (target ranks: base_value=97:126098, first_product=194:64300, bound_value=173:8847, second_product=346:353, answer=374:25704)
- Layer 39: `iota`, `-ulo`, `迷惑`, ` Leonardo`, `内膜` (target ranks: base_value=97:126436, first_product=194:101826, bound_value=173:77552, second_product=346:4962, answer=374:20337)
- Layer 40: ` dekameters`, `迷惑`, `菁`, `radesh`, `ching` (target ranks: base_value=97:123095, first_product=194:100428, bound_value=173:57028, second_product=346:56, answer=374:121)
- Layer 41: ` .`, `第三百`, ` waiting`, `因为这些`, ` potentially` (target ranks: base_value=97:78629, first_product=194:53665, bound_value=173:24313, second_product=346:27, answer=374:58)

### Filler position 42 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=97:126130, first_product=194:121488, bound_value=173:124231, second_product=346:125833, answer=374:124210)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13143, first_product=194:23867, bound_value=173:24599, second_product=346:20486, answer=374:25887)
- Layer 20: `锁定`, ` LS`, ` smile`, `鞍`, `挪` (target ranks: base_value=97:11394, first_product=194:22309, bound_value=173:20594, second_product=346:12395, answer=374:17182)
- Layer 30: `反复`, `sets`, `ensky`, `�`, `腿` (target ranks: base_value=97:21, first_product=194:10907, bound_value=173:455, second_product=346:12100, answer=374:28007)
- Layer 35: `173`, `�`, `73`, ` dinhi`, `bergh` (target ranks: base_value=97:50633, first_product=194:96293, bound_value=173:1, second_product=346:168, answer=374:51843)
- Layer 36: `173`, `bergh`, `�`, ` dinhi`, `迷雾` (target ranks: base_value=97:117997, first_product=194:123728, bound_value=173:1, second_product=346:8, answer=374:86163)
- Layer 37: `173`, `bergh`, `�`, `?datasetId`, ` acetone` (target ranks: base_value=97:126654, first_product=194:120612, bound_value=173:1, second_product=346:15, answer=374:93829)
- Layer 38: `173`, `bergh`, ` acetone`, `迷雾`, `�` (target ranks: base_value=97:127894, first_product=194:123775, bound_value=173:1, second_product=346:26, answer=374:103840)
- Layer 39: `173`, `pet`, `迷雾`, ` Petr`, ` acetone` (target ranks: base_value=97:127398, first_product=194:125266, bound_value=173:1, second_product=346:41, answer=374:81518)
- Layer 40: `iator`, `ponen`, `的计算`, `ching`, ` explanatory` (target ranks: base_value=97:124653, first_product=194:124578, bound_value=173:53, second_product=346:49, answer=374:2422)
- Layer 41: ` .`, ` dinhi`, ` waiting`, ` Explanation`, ` measured` (target ranks: base_value=97:102571, first_product=194:94227, bound_value=173:115, second_product=346:26, answer=374:871)

### Filler position 43 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:126199, first_product=194:121758, bound_value=173:124504, second_product=346:126043, answer=374:124536)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12928, first_product=194:23589, bound_value=173:24844, second_product=346:20570, answer=374:26105)
- Layer 20: `锁定`, `LS`, ` LS`, `距`, `能被` (target ranks: base_value=97:10564, first_product=194:19121, bound_value=173:20683, second_product=346:15512, answer=374:17920)
- Layer 30: `iab`, `反复`, `otan`, ` reduct`, `sets` (target ranks: base_value=97:178, first_product=194:8710, bound_value=173:1215, second_product=346:12667, answer=374:21427)
- Layer 35: `346`, `otan`, ` dinhi`, `347`, ` repeat` (target ranks: base_value=97:66304, first_product=194:54292, bound_value=173:2333, second_product=346:1, answer=374:20725)
- Layer 36: `346`, `347`, `往返`, ` dinhi`, ` sumala` (target ranks: base_value=97:123798, first_product=194:106369, bound_value=173:1611, second_product=346:1, answer=374:30747)
- Layer 37: `346`, ` dinhi`, ` sumala`, `زياح`, `lampi` (target ranks: base_value=97:128026, first_product=194:95401, bound_value=173:2160, second_product=346:1, answer=374:53655)
- Layer 38: `346`, ` sumala`, ` dinhi`, `amic`, ` itandi` (target ranks: base_value=97:128282, first_product=194:94093, bound_value=173:1818, second_product=346:1, answer=374:47555)
- Layer 39: `346`, ` sumala`, `迷惑`, `-ulo`, ` dinhi` (target ranks: base_value=97:128449, first_product=194:117397, bound_value=173:61883, second_product=346:1, answer=374:19452)
- Layer 40: `346`, `三百`, `iator`, `第三百`, `empel` (target ranks: base_value=97:127277, first_product=194:120526, bound_value=173:104106, second_product=346:1, answer=374:88)
- Layer 41: `346`, ` .`, `326`, `第三百`, `Answer` (target ranks: base_value=97:94976, first_product=194:76026, bound_value=173:49986, second_product=346:1, answer=374:20)

### Filler position 44 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:126199, first_product=194:121675, bound_value=173:124388, second_product=346:125995, answer=374:124472)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13586, first_product=194:24164, bound_value=173:25457, second_product=346:21083, answer=374:27399)
- Layer 20: `忑`, `能被`, `ait`, `锁定`, ` Walker` (target ranks: base_value=97:11633, first_product=194:24431, bound_value=173:31034, second_product=346:22970, answer=374:27276)
- Layer 30: `97`, ` seventy`, ` talags`, ` ninete`, ` pakig` (target ranks: base_value=97:1, first_product=194:1648, bound_value=173:5950, second_product=346:34773, answer=374:10234)
- Layer 35: ` seventy`, ` concaten`, `97`, `七十`, `放下` (target ranks: base_value=97:3, first_product=194:3276, bound_value=173:1936, second_product=346:42424, answer=374:11521)
- Layer 36: `放下`, `反复`, ` concaten`, ` Wil`, `翻了` (target ranks: base_value=97:98, first_product=194:12197, bound_value=173:8890, second_product=346:56351, answer=374:20010)
- Layer 37: `}<?`, `TreeLabel`, `Quintal`, `-ulo`, `?datasetId` (target ranks: base_value=97:10841, first_product=194:50458, bound_value=173:74532, second_product=346:119491, answer=374:81679)
- Layer 38: `}<?`, `�乐`, `TreeLabel`, `本题分析`, `宫内` (target ranks: base_value=97:29997, first_product=194:57537, bound_value=173:83291, second_product=346:116561, answer=374:97674)
- Layer 39: `�乐`, `}<?`, `-ulo`, ` sumala`, `�` (target ranks: base_value=97:76165, first_product=194:98276, bound_value=173:109435, second_product=346:63720, answer=374:35071)
- Layer 40: ` Tw`, ` fifty`, ` Question`, ` .`, `二十八` (target ranks: base_value=97:61390, first_product=194:80139, bound_value=173:39498, second_product=346:831, answer=374:539)
- Layer 41: ` .`, ` Question`, `Question`, ` thirty`, ` .↵↵` (target ranks: base_value=97:11347, first_product=194:21882, bound_value=173:6163, second_product=346:79, answer=374:35)

### Filler position 45 (absolute token 845, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=97:126269, first_product=194:122016, bound_value=173:124814, second_product=346:126309, answer=374:124775)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12852, first_product=194:23644, bound_value=173:24372, second_product=346:20472, answer=374:25864)
- Layer 20: `ait`, `会成为`, ` Walker`, `妇`, `能被` (target ranks: base_value=97:18882, first_product=194:30046, bound_value=173:35291, second_product=346:38542, answer=374:42681)
- Layer 30: ` Nog`, `acet`, `acos`, `进货`, `nog` (target ranks: base_value=97:5393, first_product=194:71720, bound_value=173:115494, second_product=346:110780, answer=374:72707)
- Layer 35: `留存`, ` Nog`, ` Tw`, `acos`, ` No` (target ranks: base_value=97:267, first_product=194:38011, bound_value=173:83491, second_product=346:76614, answer=374:38309)
- Layer 36: `留存`, ` Nog`, `otas`, ` Tw`, `acos` (target ranks: base_value=97:361, first_product=194:34901, bound_value=173:74389, second_product=346:54549, answer=374:36727)
- Layer 37: `}<?`, ` Nog`, `acos`, `留存`, `acet` (target ranks: base_value=97:6581, first_product=194:62668, bound_value=173:100215, second_product=346:83942, answer=374:55562)
- Layer 38: `留存`, `}<?`, ` Nog`, `不加`, `acos` (target ranks: base_value=97:9581, first_product=194:57116, bound_value=173:73615, second_product=346:59213, answer=374:53502)
- Layer 39: `}<?`, ` Nog`, `本题分析`, `文字的`, `polar` (target ranks: base_value=97:22080, first_product=194:95682, bound_value=173:101739, second_product=346:78948, answer=374:47941)
- Layer 40: ` Tw`, ` seventy`, ` Seventy`, `n`, `留存` (target ranks: base_value=97:1516, first_product=194:63068, bound_value=173:40958, second_product=346:15454, answer=374:3943)
- Layer 41: ` seventy`, ` `, ` .`, ` Question`, `Question` (target ranks: base_value=97:179, first_product=194:24525, bound_value=173:9841, second_product=346:1656, answer=374:292)

### Filler position 46 (absolute token 846, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=97:126265, first_product=194:122068, bound_value=173:124727, second_product=346:126233, answer=374:124756)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:12886, first_product=194:23315, bound_value=173:23764, second_product=346:20088, answer=374:25214)
- Layer 20: `平行`, `俯`, ` spac`, `school`, ` blanks` (target ranks: base_value=97:81855, first_product=194:49872, bound_value=173:106608, second_product=346:86252, answer=374:97511)
- Layer 30: `?datasetId`, ` spac`, `}using`, `坝`, ` dekameters` (target ranks: base_value=97:102036, first_product=194:77197, bound_value=173:125286, second_product=346:102592, answer=374:105054)
- Layer 35: `俯`, `足足`, `ovel`, `坏`, ` panc` (target ranks: base_value=97:49225, first_product=194:95816, bound_value=173:118188, second_product=346:88559, answer=374:48058)
- Layer 36: `俯`, `足足`, `ancock`, ` surveying`, ` reserved` (target ranks: base_value=97:15962, first_product=194:49215, bound_value=173:85227, second_product=346:40301, answer=374:26214)
- Layer 37: `}<?`, `俯`, `放下`, `onana`, `放下了` (target ranks: base_value=97:60868, first_product=194:77448, bound_value=173:110386, second_product=346:52569, answer=374:41810)
- Layer 38: ` .`, `俯`, `坏`, `错过`, `停` (target ranks: base_value=97:24461, first_product=194:38052, bound_value=173:90868, second_product=346:69250, answer=374:37020)
- Layer 39: `ozygous`, `osaurus`, `oxygen`, `乐乐`, `铎` (target ranks: base_value=97:76656, first_product=194:83359, bound_value=173:117863, second_product=346:102411, answer=374:39012)
- Layer 40: ` .`, ` x`, ` .↵↵`, ` nasod`, `�` (target ranks: base_value=97:31410, first_product=194:59454, bound_value=173:95609, second_product=346:67131, answer=374:16275)
- Layer 41: ` .`, ` .↵↵`, ` `, ` .↵`, `<｜end▁of▁sentence｜>` (target ranks: base_value=97:15342, first_product=194:19754, bound_value=173:65210, second_product=346:21915, answer=374:1141)

### Filler position 47 (absolute token 847, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=97:126210, first_product=194:121957, bound_value=173:124759, second_product=346:126193, answer=374:124686)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=97:12685, first_product=194:22981, bound_value=173:23581, second_product=346:19625, answer=374:25169)
- Layer 20: `}<?`, ` partly`, `ozygous`, `)Skip`, ` sideways` (target ranks: base_value=97:126195, first_product=194:100779, bound_value=173:122953, second_product=346:105965, answer=374:120370)
- Layer 30: `}<?`, `codeline`, `dividers`, `}using`, `东京` (target ranks: base_value=97:120062, first_product=194:97457, bound_value=173:119446, second_product=346:108112, answer=374:115879)
- Layer 35: `codeline`, `lett`, `ِّف`, `}<?`, `dividers` (target ranks: base_value=97:97217, first_product=194:125159, bound_value=173:119138, second_product=346:110812, answer=374:101916)
- Layer 36: `足足`, `锯`, `切割`, ` fit`, ` nasod` (target ranks: base_value=97:50148, first_product=194:111765, bound_value=173:86850, second_product=346:81035, answer=374:86108)
- Layer 37: `}<?`, `东京`, `磨损`, `Quintal`, ` doubles` (target ranks: base_value=97:89620, first_product=194:115069, bound_value=173:109532, second_product=346:76453, answer=374:86236)
- Layer 38: ` .`, `遁`, `lett`, `切割`, ` prese` (target ranks: base_value=97:71060, first_product=194:84643, bound_value=173:93979, second_product=346:76508, answer=374:79468)
- Layer 39: ` .`, `lett`, `<｜begin▁of▁sentence｜>`, `�`, ` .↵↵` (target ranks: base_value=97:112125, first_product=194:103103, bound_value=173:104323, second_product=346:90711, answer=374:48558)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, ` nasod` (target ranks: base_value=97:78031, first_product=194:87019, bound_value=173:78918, second_product=346:50686, answer=374:21389)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: base_value=97:31059, first_product=194:28319, bound_value=173:31435, second_product=346:8844, answer=374:816)

### Filler position 48 (absolute token 848, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=97:126318, first_product=194:122033, bound_value=173:124813, second_product=346:126260, answer=374:124754)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=97:12627, first_product=194:23761, bound_value=173:24626, second_product=346:20198, answer=374:25962)
- Layer 20: `东海`, `}<?`, `aharoa`, ` instantaneous`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=97:115015, first_product=194:69132, bound_value=173:91124, second_product=346:94287, answer=374:99817)
- Layer 30: `codeline`, ` accompanying`, `东京`, ` accompan`, `lett` (target ranks: base_value=97:116962, first_product=194:83548, bound_value=173:118831, second_product=346:116179, answer=374:101506)
- Layer 35: `codeline`, ` fif`, `白雪`, `AssemblyVersion`, ` caterpillar` (target ranks: base_value=97:116617, first_product=194:124493, bound_value=173:125821, second_product=346:118624, answer=374:100218)
- Layer 36: ` nasod`, ` soci`, ` Predict`, ` reduct`, `yss` (target ranks: base_value=97:90975, first_product=194:110969, bound_value=173:109710, second_product=346:98463, answer=374:77294)
- Layer 37: `codeline`, `Quintal`, `TreeLabel`, `悬挂`, `镶嵌` (target ranks: base_value=97:122297, first_product=194:123970, bound_value=173:123140, second_product=346:113402, answer=374:96250)
- Layer 38: ` crev`, `肤`, ` .`, `悬挂`, ` nasod` (target ranks: base_value=97:115721, first_product=194:121258, bound_value=173:118136, second_product=346:102329, answer=374:102108)
- Layer 39: `�`, ` .`, ` .↵↵`, `贻`, ` unflagged` (target ranks: base_value=97:124622, first_product=194:123779, bound_value=173:110132, second_product=346:104763, answer=374:102048)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, `肤` (target ranks: base_value=97:117184, first_product=194:121046, bound_value=173:86873, second_product=346:92354, answer=374:67373)
- Layer 41: ` .`, ` .↵↵`, `圆圆`, ` .↵`, `�` (target ranks: base_value=97:63520, first_product=194:65257, bound_value=173:26948, second_product=346:38860, answer=374:13702)

### Filler position 49 (absolute token 849, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=97:126232, first_product=194:122179, bound_value=173:124933, second_product=346:126347, answer=374:124871)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:12566, first_product=194:25088, bound_value=173:25996, second_product=346:21129, answer=374:26511)
- Layer 20: ` licensierad`, `codeline`, `aplenty`, `文本`, ` grounds` (target ranks: base_value=97:106993, first_product=194:65679, bound_value=173:98406, second_product=346:103297, answer=374:81903)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, ` Antwort` (target ranks: base_value=97:108185, first_product=194:83142, bound_value=173:125972, second_product=346:121328, answer=374:96188)
- Layer 35: `codeline`, ` Answer`, `AED`, `oNames`, ` Antwort` (target ranks: base_value=97:89248, first_product=194:76543, bound_value=173:122725, second_product=346:106933, answer=374:98432)
- Layer 36: ` Answer`, `坏`, ` nasod`, `停顿`, `停` (target ranks: base_value=97:37739, first_product=194:34201, bound_value=173:103216, second_product=346:74897, answer=374:62351)
- Layer 37: `oNames`, `codeline`, `insic`, ` consum`, ` konder` (target ranks: base_value=97:97334, first_product=194:102543, bound_value=173:116255, second_product=346:103087, answer=374:107294)
- Layer 38: `oNames`, ` retard`, `оду`, `codeline`, `insic` (target ranks: base_value=97:107152, first_product=194:91248, bound_value=173:114321, second_product=346:100195, answer=374:102314)
- Layer 39: `�`, `oxygen`, `deen`, `►▼`, `-ulo` (target ranks: base_value=97:109151, first_product=194:100431, bound_value=173:120232, second_product=346:81046, answer=374:72400)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` wink`, `pro` (target ranks: base_value=97:51366, first_product=194:69135, bound_value=173:98355, second_product=346:47112, answer=374:15163)
- Layer 41: ` .`, ` .↵↵`, `叮`, ` Answer`, ` wink` (target ranks: base_value=97:25994, first_product=194:34755, bound_value=173:53428, second_product=346:22847, answer=374:3442)

### Filler position 50 (absolute token 850, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=97:120660, first_product=194:110474, bound_value=173:111038, second_product=346:114437, answer=374:112011)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:126304, first_product=194:116570, bound_value=173:115903, second_product=346:115636, answer=374:116940)
- Layer 20: `答复`, `能被`, ` ChatGPT`, `EDER`, `憬` (target ranks: base_value=97:28590, first_product=194:77662, bound_value=173:43825, second_product=346:33397, answer=374:62965)
- Layer 30: `?datasetId`, `aplenty`, ` dátummal`, ` mach`, `/MODIS` (target ranks: base_value=97:77349, first_product=194:77245, bound_value=173:16089, second_product=346:37948, answer=374:79814)
- Layer 35: `346`, `345`, `349`, `344`, `347` (target ranks: base_value=97:128676, first_product=194:95551, bound_value=173:108418, second_product=346:1, answer=374:427)
- Layer 36: `323`, `三百`, `325`, `321`, `322` (target ranks: base_value=97:129232, first_product=194:125751, bound_value=173:79135, second_product=346:16, answer=374:42)
- Layer 37: `323`, `325`, `三百`, `第三百`, `326` (target ranks: base_value=97:129221, first_product=194:127691, bound_value=173:89372, second_product=346:10, answer=374:37)
- Layer 38: `323`, `321`, `322`, `325`, `324` (target ranks: base_value=97:129225, first_product=194:128563, bound_value=173:117074, second_product=346:28, answer=374:51)
- Layer 39: `323`, `321`, `322`, `324`, `319` (target ranks: base_value=97:127594, first_product=194:126035, bound_value=173:124121, second_product=346:983, answer=374:82)
- Layer 40: ` Answer`, `Answer`, ` answer`, `answer`, `_answer` (target ranks: base_value=97:128099, first_product=194:126928, bound_value=173:117830, second_product=346:626, answer=374:164)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=97:89443, first_product=194:81537, bound_value=173:86061, second_product=346:2806, answer=374:1363)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zuk = 78
xuf = twice the number for zuk minus 15
nof = 97
hoz = twice the number for nof minus 21
hoh = twice the number for nof minus 26
Question: What is twice the number for hoz plus 28?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
