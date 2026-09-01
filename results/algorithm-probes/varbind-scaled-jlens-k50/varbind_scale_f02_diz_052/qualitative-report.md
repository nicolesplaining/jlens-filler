# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `228` (correct).
- No-filler answer: `220` (incorrect).
- Filler tokens: 50 tokens at absolute indices 793–842.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=52` | 1 (L24, filler 15) | L24, filler 15 (rank 1) |
| J-Lens | `first_product=104` | 2 (L29, filler 1) | L28, filler 1 (rank 4) |
| J-Lens | `bound_value=120` | 1 (L31, filler 43) | L31, filler 15 (rank 3) |
| J-Lens | `second_product=240` | 1 (L31, filler 15) | L31, filler 1 (rank 8) |
| J-Lens | `answer=228` | 1 (L31, filler 14) | L30, filler 14 (rank 5) |
| Logit lens | `base_value=52` | 1 (L28, filler 44) | L24, filler 1 (rank 8) |
| Logit lens | `first_product=104` | 59 (L31, filler 14) | Never |
| Logit lens | `bound_value=120` | 1 (L35, filler 43) | L35, filler 43 (rank 1) |
| Logit lens | `second_product=240` | 1 (L31, filler 15) | L31, filler 15 (rank 1) |
| Logit lens | `answer=228` | 1 (L30, filler 14) | L29, filler 14 (rank 2) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 793, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=52:120269, first_product=104:108038, bound_value=120:111927, second_product=240:114850, answer=228:117225)
- Layer 10: `anta`, `fine`, ` kinain`, `hook`, `locked` (target ranks: base_value=52:77225, first_product=104:77254, bound_value=120:58462, second_product=240:56794, answer=228:81409)
- Layer 20: `扣`, `重`, `足`, `期望`, `adows` (target ranks: base_value=52:1178, first_product=104:5829, bound_value=120:11995, second_product=240:10182, answer=228:25152)
- Layer 30: ` الشعاعيه`, `104`, `108`, `116`, `93` (target ranks: base_value=52:10, first_product=104:2, bound_value=120:452, second_product=240:536, answer=228:843)
- Layer 35: `240`, `232`, `212`, `228`, `214` (target ranks: base_value=52:2674, first_product=104:1353, bound_value=120:16753, second_product=240:1, answer=228:4)
- Layer 36: `228`, `232`, `229`, `208`, `224` (target ranks: base_value=52:6295, first_product=104:3539, bound_value=120:24302, second_product=240:8, answer=228:1)
- Layer 37: `228`, `232`, `240`, `230`, `229` (target ranks: base_value=52:45077, first_product=104:28247, bound_value=120:21931, second_product=240:3, answer=228:1)
- Layer 38: `228`, `232`, `第二百`, `230`, `208` (target ranks: base_value=52:98451, first_product=104:47349, bound_value=120:62226, second_product=240:6, answer=228:1)
- Layer 39: `228`, `229`, `232`, `230`, `桃子` (target ranks: base_value=52:113228, first_product=104:108988, bound_value=120:106645, second_product=240:174, answer=228:1)
- Layer 40: `228`, ` talags`, ` ald`, `Ald`, `yyyy` (target ranks: base_value=52:89926, first_product=104:88533, bound_value=120:49288, second_product=240:219, answer=228:1)
- Layer 41: ` nuest`, ` .`, `NET`, `我只`, `我没有` (target ranks: base_value=52:18354, first_product=104:83178, bound_value=120:91552, second_product=240:8620, answer=228:25)

### Filler position 2 (absolute token 794, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=52:121493, first_product=104:115818, bound_value=120:116602, second_product=240:120593, answer=228:119849)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=52:18189, first_product=104:44063, bound_value=120:31358, second_product=240:31394, answer=228:32454)
- Layer 20: ` .`, `外向`, ` esper`, ` distant`, `�` (target ranks: base_value=52:53344, first_product=104:97179, bound_value=120:124327, second_product=240:122820, answer=228:88099)
- Layer 30: ` pakig`, ` talags`, ` dekameters`, `日常`, `}<?` (target ranks: base_value=52:55393, first_product=104:81491, bound_value=120:111490, second_product=240:120840, answer=228:41159)
- Layer 35: ` Nij`, ` dekameters`, `空空`, ` extrac`, `私` (target ranks: base_value=52:28163, first_product=104:40032, bound_value=120:89431, second_product=240:101124, answer=228:13964)
- Layer 36: ` Erkännande`, ` Nij`, ` talags`, `空空`, `培养` (target ranks: base_value=52:47557, first_product=104:20551, bound_value=120:64224, second_product=240:69326, answer=228:5161)
- Layer 37: ` Erkännande`, `}<?`, `�乐`, ` hilabihan`, `EDMF` (target ranks: base_value=52:114646, first_product=104:86678, bound_value=120:107686, second_product=240:117888, answer=228:61539)
- Layer 38: ` Erkännande`, `}<?`, `�乐`, ` Rae`, ` hilabihan` (target ranks: base_value=52:117456, first_product=104:36264, bound_value=120:74543, second_product=240:108230, answer=228:23237)
- Layer 39: ` hilabihan`, ` talags`, `}<?`, ` Rae`, `ziej` (target ranks: base_value=52:120259, first_product=104:59496, bound_value=120:70650, second_product=240:63593, answer=228:7239)
- Layer 40: ` .`, ` talags`, ` nasod`, ` +:+`, `语言文字` (target ranks: base_value=52:85228, first_product=104:20052, bound_value=120:19972, second_product=240:9742, answer=228:69)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` :` (target ranks: base_value=52:58096, first_product=104:15889, bound_value=120:26856, second_product=240:9718, answer=228:98)

### Filler position 3 (absolute token 795, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124685, first_product=104:119573, bound_value=120:119847, second_product=240:122887, answer=228:120922)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=52:15595, first_product=104:37414, bound_value=120:29157, second_product=240:29314, answer=228:27173)
- Layer 20: `ait`, `能被`, `忑`, `cks`, ` ternary` (target ranks: base_value=52:11493, first_product=104:44088, bound_value=120:44043, second_product=240:63786, answer=228:43289)
- Layer 30: ` diz`, `kod`, `coding`, `yz`, ` Liz` (target ranks: base_value=52:17267, first_product=104:102217, bound_value=120:121473, second_product=240:125457, answer=228:124609)
- Layer 35: ` diz`, ` zad`, ` dip`, ` Zad`, `yz` (target ranks: base_value=52:4334, first_product=104:80128, bound_value=120:101239, second_product=240:100312, answer=228:96502)
- Layer 36: ` diz`, ` Zad`, ` zad`, ` dic`, ` dri` (target ranks: base_value=52:20537, first_product=104:73202, bound_value=120:105422, second_product=240:107492, answer=228:83826)
- Layer 37: ` diz`, `lez`, `niz`, `}<?`, `基底` (target ranks: base_value=52:49889, first_product=104:92233, bound_value=120:119225, second_product=240:121634, answer=228:108887)
- Layer 38: ` diz`, `lez`, ` Naz`, `niz`, `本题分析` (target ranks: base_value=52:51854, first_product=104:101627, bound_value=120:112961, second_product=240:122347, answer=228:114642)
- Layer 39: `lez`, `无言`, `本题分析`, `迷惑`, `script` (target ranks: base_value=52:74799, first_product=104:106045, bound_value=120:118638, second_product=240:122352, answer=228:120686)
- Layer 40: `kten`, ` explanatory`, `script`, `留存`, `akak` (target ranks: base_value=52:49154, first_product=104:83729, bound_value=120:101094, second_product=240:107660, answer=228:90608)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, ` unless`, ` ,` (target ranks: base_value=52:10778, first_product=104:35834, bound_value=120:28145, second_product=240:26140, answer=228:16672)

### Filler position 4 (absolute token 796, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=52:125171, first_product=104:121085, bound_value=120:121382, second_product=240:124178, answer=228:122345)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=52:12691, first_product=104:30165, bound_value=120:24123, second_product=240:23737, answer=228:23369)
- Layer 20: `ait`, `atile`, `挪`, `atable`, `忑` (target ranks: base_value=52:10087, first_product=104:33174, bound_value=120:58909, second_product=240:65300, answer=228:50997)
- Layer 30: `acos`, `简明`, ` consum`, `提问`, `卖的` (target ranks: base_value=52:83130, first_product=104:79302, bound_value=120:122494, second_product=240:122430, answer=228:84122)
- Layer 35: ` simplified`, `简化`, `简明`, ` resist`, `Respond` (target ranks: base_value=52:54878, first_product=104:57926, bound_value=120:119871, second_product=240:117260, answer=228:48402)
- Layer 36: ` talags`, ` Erkännande`, `简化`, ` simplified`, ` resist` (target ranks: base_value=52:46017, first_product=104:24612, bound_value=120:100176, second_product=240:100476, answer=228:21393)
- Layer 37: ` Erkännande`, `}<?`, `打磨`, ` talags`, `斐` (target ranks: base_value=52:79257, first_product=104:42587, bound_value=120:106032, second_product=240:114407, answer=228:41863)
- Layer 38: ` Erkännande`, `hemer`, `}<?`, `ozygous`, `东海` (target ranks: base_value=52:100917, first_product=104:65830, bound_value=120:112047, second_product=240:114492, answer=228:46779)
- Layer 39: ` talags`, `东海`, `lez`, `hemer`, `ozygous` (target ranks: base_value=52:94050, first_product=104:77444, bound_value=120:101636, second_product=240:99289, answer=228:63002)
- Layer 40: ` talags`, `提问`, ` uninter`, `oug`, `inking` (target ranks: base_value=52:52516, first_product=104:53546, bound_value=120:84341, second_product=240:53126, answer=228:12754)
- Layer 41: ` .`, `试一试`, ` `, `提问`, ` intended` (target ranks: base_value=52:6617, first_product=104:22280, bound_value=120:34304, second_product=240:20878, answer=228:1537)

### Filler position 5 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=52:124794, first_product=104:120624, bound_value=120:121067, second_product=240:123848, answer=228:122385)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=52:13336, first_product=104:30875, bound_value=120:26000, second_product=240:24376, answer=228:24023)
- Layer 20: `幽`, `锁定`, `鞍`, `挪`, ` immobil` (target ranks: base_value=52:16782, first_product=104:39449, bound_value=120:54827, second_product=240:57267, answer=228:37220)
- Layer 30: `�`, `acos`, ` rip`, ` tap`, ` picnic` (target ranks: base_value=52:60842, first_product=104:88373, bound_value=120:125110, second_product=240:117396, answer=228:89221)
- Layer 35: ` rip`, ` tap`, `�`, `acin`, `Tap` (target ranks: base_value=52:55282, first_product=104:75367, bound_value=120:124332, second_product=240:111001, answer=228:48672)
- Layer 36: ` rip`, ` drip`, `acos`, `灵动`, `ilig` (target ranks: base_value=52:78150, first_product=104:58779, bound_value=120:120386, second_product=240:105325, answer=228:30177)
- Layer 37: `}<?`, ` Nij`, `覆`, ` proced`, `zim` (target ranks: base_value=52:112295, first_product=104:78086, bound_value=120:126156, second_product=240:120399, answer=228:66950)
- Layer 38: `}<?`, `zat`, `�`, `覆`, ` zaz` (target ranks: base_value=52:114968, first_product=104:87107, bound_value=120:123077, second_product=240:122697, answer=228:81757)
- Layer 39: `-ulo`, `}<?`, `hemer`, `�`, ` Nij` (target ranks: base_value=52:114587, first_product=104:67021, bound_value=120:108078, second_product=240:97024, answer=228:65032)
- Layer 40: ` talags`, ` rip`, `amn`, `hemer`, `声望` (target ranks: base_value=52:107110, first_product=104:38337, bound_value=120:88387, second_product=240:66430, answer=228:22750)
- Layer 41: ` .`, `我怎么`, `zel`, `冰冰`, `鹉` (target ranks: base_value=52:46108, first_product=104:15651, bound_value=120:17935, second_product=240:11268, answer=228:1211)

### Filler position 6 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=52:124443, first_product=104:119865, bound_value=120:120493, second_product=240:123111, answer=228:121746)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:11672, first_product=104:29142, bound_value=120:24366, second_product=240:23037, answer=228:21270)
- Layer 20: ` calculator`, ` future`, `Username`, ` Dia`, `ait` (target ranks: base_value=52:5881, first_product=104:36791, bound_value=120:27544, second_product=240:26993, answer=228:32641)
- Layer 30: `calcul`, ` Answer`, `推算`, `计算的`, ` calculator` (target ranks: base_value=52:6393, first_product=104:4208, bound_value=120:4135, second_product=240:30283, answer=228:20200)
- Layer 35: `acks`, `重复`, ` calculator`, `推算`, `反复` (target ranks: base_value=52:2586, first_product=104:5712, bound_value=120:1819, second_product=240:21939, answer=228:12187)
- Layer 36: `反复`, ` repeated`, `calcul`, `柿子`, ` stabil` (target ranks: base_value=52:10193, first_product=104:2606, bound_value=120:996, second_product=240:20765, answer=228:11543)
- Layer 37: `}<?`, ` stabil`, ` tra`, ` ladder`, ` talags` (target ranks: base_value=52:43397, first_product=104:13806, bound_value=120:6251, second_product=240:60034, answer=228:42149)
- Layer 38: `}<?`, ` nasod`, ` talags`, ` tra`, ` ladder` (target ranks: base_value=52:72852, first_product=104:18367, bound_value=120:15671, second_product=240:78922, answer=228:46744)
- Layer 39: ` nasod`, `ophe`, ` tra`, ` talags`, `}<?` (target ranks: base_value=52:74306, first_product=104:92918, bound_value=120:73062, second_product=240:121049, answer=228:114459)
- Layer 40: ` nasod`, ` talags`, ` dotted`, `试一试`, ` dekameters` (target ranks: base_value=52:39541, first_product=104:68335, bound_value=120:45105, second_product=240:110071, answer=228:99342)
- Layer 41: ` .`, ` dotted`, ` Answer`, `Answer`, `试一试` (target ranks: base_value=52:9631, first_product=104:45065, bound_value=120:26381, second_product=240:75436, answer=228:54695)

### Filler position 7 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=52:124400, first_product=104:119382, bound_value=120:120110, second_product=240:122777, answer=228:121551)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:11666, first_product=104:29100, bound_value=120:24123, second_product=240:22810, answer=228:21539)
- Layer 20: `锁定`, `足`, `挪`, `鞍`, `Ta` (target ranks: base_value=52:5275, first_product=104:20432, bound_value=120:26118, second_product=240:25021, answer=228:18504)
- Layer 30: `鞍`, `yg`, ` Cogn`, ` smile`, ` calculator` (target ranks: base_value=52:49, first_product=104:857, bound_value=120:9279, second_product=240:10436, answer=228:1229)
- Layer 35: ` labor`, `特`, `Subt`, ` Heim`, `推算` (target ranks: base_value=52:169, first_product=104:1182, bound_value=120:35674, second_product=240:10666, answer=228:94)
- Layer 36: ` pakig`, `anium`, ` talags`, `acin`, `推算` (target ranks: base_value=52:3510, first_product=104:1026, bound_value=120:37199, second_product=240:8981, answer=228:10)
- Layer 37: `}<?`, ` pakig`, `?datasetId`, `iganos`, ` talags` (target ranks: base_value=52:42201, first_product=104:7077, bound_value=120:38001, second_product=240:5322, answer=228:34)
- Layer 38: `}<?`, `?datasetId`, `-ulo`, `ocyst`, `脂肪` (target ranks: base_value=52:76746, first_product=104:15669, bound_value=120:46507, second_product=240:12974, answer=228:700)
- Layer 39: `}<?`, `-ulo`, `?datasetId`, ` dátummal`, `ocyst` (target ranks: base_value=52:120339, first_product=104:96331, bound_value=120:81921, second_product=240:1559, answer=228:18)
- Layer 40: ` talags`, `留存`, ` mosunod`, ` pakig`, `228` (target ranks: base_value=52:122209, first_product=104:110295, bound_value=120:67553, second_product=240:286, answer=228:5)
- Layer 41: ` .`, `因为这些`, `acular`, `我只`, `也不必` (target ranks: base_value=52:100683, first_product=104:109182, bound_value=120:74579, second_product=240:5243, answer=228:22)

### Filler position 8 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124235, first_product=104:118976, bound_value=120:119766, second_product=240:122458, answer=228:121204)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:10288, first_product=104:28260, bound_value=120:22419, second_product=240:22441, answer=228:20898)
- Layer 20: `ait`, ` Walker`, `挪`, `锁定`, `Walker` (target ranks: base_value=52:16493, first_product=104:47272, bound_value=120:55279, second_product=240:65198, answer=228:40736)
- Layer 30: `表述`, ` expressions`, ` repeated`, `Tap`, ` Tap` (target ranks: base_value=52:28241, first_product=104:76555, bound_value=120:104496, second_product=240:116323, answer=228:70542)
- Layer 35: ` expressions`, ` Tw`, `Tap`, `锁定`, ` definitions` (target ranks: base_value=52:11903, first_product=104:34625, bound_value=120:79021, second_product=240:90331, answer=228:26547)
- Layer 36: ` definitions`, ` expressions`, `calcul`, `定义`, `Definitions` (target ranks: base_value=52:22535, first_product=104:22988, bound_value=120:77238, second_product=240:97610, answer=228:13909)
- Layer 37: `定义`, ` definitions`, `defining`, `calcul`, `Definitions` (target ranks: base_value=52:55396, first_product=104:45920, bound_value=120:110566, second_product=240:122774, answer=228:32335)
- Layer 38: `}<?`, `calcul`, `枝叶`, `定义`, `defining` (target ranks: base_value=52:54398, first_product=104:59914, bound_value=120:107881, second_product=240:123931, answer=228:25737)
- Layer 39: `}<?`, `script`, `<｜begin▁of▁sentence｜>`, `hemer`, `文字的` (target ranks: base_value=52:61173, first_product=104:71680, bound_value=120:106982, second_product=240:124750, answer=228:73488)
- Layer 40: `šk`, `下沉`, `amn`, `acl`, ` fragment` (target ranks: base_value=52:17730, first_product=104:49619, bound_value=120:91079, second_product=240:118111, answer=228:43662)
- Layer 41: ` .`, ` dotted`, ` variable`, ` `, ` fragment` (target ranks: base_value=52:12721, first_product=104:50259, bound_value=120:71308, second_product=240:112698, answer=228:30524)

### Filler position 9 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124421, first_product=104:119147, bound_value=120:120103, second_product=240:122719, answer=228:121583)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10683, first_product=104:29187, bound_value=120:23056, second_product=240:23292, answer=228:21789)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=52:11967, first_product=104:32060, bound_value=120:47323, second_product=240:54646, answer=228:32249)
- Layer 30: ` variable`, `variable`, ` var`, `coding`, ` Variables` (target ranks: base_value=52:45028, first_product=104:95101, bound_value=120:123939, second_product=240:126164, answer=228:119906)
- Layer 35: ` var`, ` variable`, `variable`, ` v`, `Variable` (target ranks: base_value=52:17016, first_product=104:50346, bound_value=120:99856, second_product=240:101541, answer=228:59761)
- Layer 36: ` definitions`, `定义`, ` variable`, ` variables`, `Variables` (target ranks: base_value=52:50736, first_product=104:43733, bound_value=120:107795, second_product=240:109026, answer=228:49859)
- Layer 37: `定义`, `Variables`, `}<?`, `variables`, `变量的` (target ranks: base_value=52:82359, first_product=104:73599, bound_value=120:119097, second_product=240:120246, answer=228:77397)
- Layer 38: `}<?`, `Variables`, `variables`, `变量的`, `定义` (target ranks: base_value=52:83956, first_product=104:90669, bound_value=120:120756, second_product=240:125873, answer=228:81844)
- Layer 39: `}<?`, ` перемен`, `variables`, `变量的`, `Variables` (target ranks: base_value=52:63499, first_product=104:82565, bound_value=120:113204, second_product=240:124886, answer=228:95814)
- Layer 40: ` consum`, `acl`, `amn`, `šk`, `留存` (target ranks: base_value=52:15007, first_product=104:60030, bound_value=120:90656, second_product=240:116259, answer=228:53672)
- Layer 41: ` .`, `试一试`, ` `, ` repeated`, `然而` (target ranks: base_value=52:5005, first_product=104:47200, bound_value=120:51714, second_product=240:106092, answer=228:31533)

### Filler position 10 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124256, first_product=104:118912, bound_value=120:119993, second_product=240:122720, answer=228:121568)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10345, first_product=104:28617, bound_value=120:22712, second_product=240:22567, answer=228:21462)
- Layer 20: `ait`, ` Walker`, `锁定`, ` smile`, `挪` (target ranks: base_value=52:8617, first_product=104:31695, bound_value=120:44970, second_product=240:44292, answer=228:27358)
- Layer 30: `Tap`, `68`, `题库`, ` Tap`, `acos` (target ranks: base_value=52:52, first_product=104:2684, bound_value=120:9026, second_product=240:3583, answer=228:50)
- Layer 35: `240`, ` Zad`, ` Heim`, ` gihulagway`, ` talags` (target ranks: base_value=52:1333, first_product=104:1386, bound_value=120:60492, second_product=240:1, answer=228:12)
- Layer 36: `228`, ` talags`, `海中`, ` gihulagway`, `�סט` (target ranks: base_value=52:674, first_product=104:22080, bound_value=120:55249, second_product=240:62, answer=228:1)
- Layer 37: `228`, `.nextToken`, `�סט`, `海中`, `fat` (target ranks: base_value=52:13158, first_product=104:50689, bound_value=120:43833, second_product=240:20, answer=228:1)
- Layer 38: `228`, `428`, `227`, `528`, `229` (target ranks: base_value=52:63025, first_product=104:43887, bound_value=120:85390, second_product=240:14, answer=228:1)
- Layer 39: `228`, `428`, `229`, `227`, `528` (target ranks: base_value=52:117998, first_product=104:121921, bound_value=120:122732, second_product=240:1632, answer=228:1)
- Layer 40: `228`, ` dekameters`, `227`, ` Didžiulis`, `第二百` (target ranks: base_value=52:122376, first_product=104:125055, bound_value=120:119763, second_product=240:1362, answer=228:1)
- Layer 41: `228`, ` nuest`, ` Didžiulis`, `iolary`, `印书馆` (target ranks: base_value=52:75014, first_product=104:101622, bound_value=120:103243, second_product=240:12166, answer=228:1)

### Filler position 11 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124274, first_product=104:119118, bound_value=120:120170, second_product=240:122903, answer=228:121800)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:10116, first_product=104:27235, bound_value=120:22057, second_product=240:21699, answer=228:20892)
- Layer 20: ` Walker`, ` smile`, `能被`, `Walker`, `ait` (target ranks: base_value=52:16588, first_product=104:46519, bound_value=120:53492, second_product=240:50117, answer=228:38149)
- Layer 30: ` diz`, ` Diam`, `算出`, `52`, `�` (target ranks: base_value=52:4, first_product=104:34684, bound_value=120:110288, second_product=240:102885, answer=228:46630)
- Layer 35: `52`, ` diz`, `计算`, `推算`, `calcul` (target ranks: base_value=52:1, first_product=104:20310, bound_value=120:90456, second_product=240:83364, answer=228:15869)
- Layer 36: `calcul`, `翻`, `计算的`, ` diz`, `计算` (target ranks: base_value=52:34, first_product=104:11075, bound_value=120:97220, second_product=240:94475, answer=228:10444)
- Layer 37: `niz`, ` diz`, `}<?`, ` Dich`, `计算方法` (target ranks: base_value=52:36, first_product=104:16029, bound_value=120:102523, second_product=240:114418, answer=228:24481)
- Layer 38: `}<?`, ` diz`, `niz`, `计算方法`, `zat` (target ranks: base_value=52:257, first_product=104:18669, bound_value=120:93435, second_product=240:117374, answer=228:46208)
- Layer 39: `}<?`, `东海`, `niz`, ` diz`, `lez` (target ranks: base_value=52:8931, first_product=104:21281, bound_value=120:72243, second_product=240:65298, answer=228:10765)
- Layer 40: `zel`, ` diz`, `zac`, `calcul`, `d` (target ranks: base_value=52:10131, first_product=104:6493, bound_value=120:31795, second_product=240:8949, answer=228:71)
- Layer 41: ` .`, ` `, `的计算`, `计算方法`, `叮` (target ranks: base_value=52:2432, first_product=104:5572, bound_value=120:12065, second_product=240:2398, answer=228:12)

### Filler position 12 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124279, first_product=104:118990, bound_value=120:120058, second_product=240:122729, answer=228:121695)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10396, first_product=104:28464, bound_value=120:22537, second_product=240:22310, answer=228:21220)
- Layer 20: `ait`, ` smile`, ` wig`, `锁定`, ` ES` (target ranks: base_value=52:6957, first_product=104:32953, bound_value=120:44941, second_product=240:47907, answer=228:35213)
- Layer 30: `Tap`, ` tap`, `acos`, ` Tap`, ` glacier` (target ranks: base_value=52:41582, first_product=104:45202, bound_value=120:106776, second_product=240:98064, answer=228:66713)
- Layer 35: ` tap`, `Tap`, ` Tap`, `acin`, `acos` (target ranks: base_value=52:27662, first_product=104:47070, bound_value=120:102081, second_product=240:100559, answer=228:52865)
- Layer 36: `acin`, `acos`, ` tap`, ` Zad`, `yg` (target ranks: base_value=52:25175, first_product=104:21350, bound_value=120:74094, second_product=240:77672, answer=228:30213)
- Layer 37: `acos`, `}<?`, ` Zad`, `acons`, `冰冰` (target ranks: base_value=52:66498, first_product=104:36165, bound_value=120:97002, second_product=240:105869, answer=228:55756)
- Layer 38: `}<?`, `�`, `acons`, `东海`, `omer` (target ranks: base_value=52:84590, first_product=104:53929, bound_value=120:109508, second_product=240:116964, answer=228:75981)
- Layer 39: `东海`, `hemer`, `hatic`, `<｜begin▁of▁sentence｜>`, `opters` (target ranks: base_value=52:61530, first_product=104:42032, bound_value=120:78483, second_product=240:88781, answer=228:57772)
- Layer 40: ` talags`, `acl`, `乐乐`, `冰冰`, ` Zad` (target ranks: base_value=52:13064, first_product=104:11331, bound_value=120:29906, second_product=240:40468, answer=228:5169)
- Layer 41: ` .`, `鹉`, ` Aufgabe`, `Question`, ` unless` (target ranks: base_value=52:620, first_product=104:1769, bound_value=120:4692, second_product=240:8359, answer=228:84)

### Filler position 13 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:123971, first_product=104:118555, bound_value=120:119625, second_product=240:122408, answer=228:121507)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10393, first_product=104:28068, bound_value=120:22526, second_product=240:22376, answer=228:20687)
- Layer 20: `ait`, `忑`, ` Walker`, `锁定`, ` engaging` (target ranks: base_value=52:16258, first_product=104:39699, bound_value=120:59867, second_product=240:51117, answer=228:26996)
- Layer 30: `提问`, ` question`, `询问`, ` calculator`, ` questions` (target ranks: base_value=52:10578, first_product=104:61730, bound_value=120:102626, second_product=240:89770, answer=228:45383)
- Layer 35: ` calculator`, ` Tw`, `calcul`, `询问`, `第一步` (target ranks: base_value=52:4213, first_product=104:36913, bound_value=120:73630, second_product=240:65311, answer=228:18917)
- Layer 36: `calcul`, ` Zad`, ` final`, `询问`, ` calculator` (target ranks: base_value=52:15836, first_product=104:30266, bound_value=120:83945, second_product=240:79707, answer=228:14400)
- Layer 37: `calcul`, `}<?`, ` Zad`, ` final`, ` calculations` (target ranks: base_value=52:46410, first_product=104:58928, bound_value=120:112347, second_product=240:117591, answer=228:41482)
- Layer 38: `}<?`, `calcul`, ` Zad`, `进行计算`, ` calcul` (target ranks: base_value=52:59183, first_product=104:57222, bound_value=120:106268, second_product=240:119933, answer=228:53153)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `东海`, `殿堂`, `ocyst` (target ranks: base_value=52:58884, first_product=104:65825, bound_value=120:88509, second_product=240:118938, answer=228:61497)
- Layer 40: `留存`, `殿堂`, `外壳`, ` z`, `acl` (target ranks: base_value=52:12495, first_product=104:32178, bound_value=120:64760, second_product=240:101213, answer=228:21965)
- Layer 41: ` .`, `鹉`, `z`, `zac`, `留存` (target ranks: base_value=52:3736, first_product=104:29718, bound_value=120:39268, second_product=240:73880, answer=228:5303)

### Filler position 14 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124505, first_product=104:119562, bound_value=120:120490, second_product=240:123110, answer=228:122124)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9153, first_product=104:26154, bound_value=120:21212, second_product=240:20927, answer=228:19142)
- Layer 20: `锁定`, `ait`, ` LS`, ` Walker`, `能被` (target ranks: base_value=52:2196, first_product=104:10957, bound_value=120:16716, second_product=240:15689, answer=228:10035)
- Layer 30: `68`, `328`, ` basal`, `116`, `228` (target ranks: base_value=52:9, first_product=104:25, bound_value=120:7075, second_product=240:485, answer=228:5)
- Layer 35: `240`, `228`, ` talags`, ` dunay`, ` Subt` (target ranks: base_value=52:667, first_product=104:381, bound_value=120:72451, second_product=240:1, answer=228:2)
- Layer 36: `228`, `230`, `229`, ` talags`, `428` (target ranks: base_value=52:2461, first_product=104:21464, bound_value=120:59672, second_product=240:8, answer=228:1)
- Layer 37: `228`, `230`, `240`, `229`, `232` (target ranks: base_value=52:29547, first_product=104:47702, bound_value=120:48628, second_product=240:3, answer=228:1)
- Layer 38: `228`, `229`, `ianhi`, `adtong`, ` mempun` (target ranks: base_value=52:104848, first_product=104:57707, bound_value=120:102418, second_product=240:13, answer=228:1)
- Layer 39: `228`, `229`, `428`, ` Paglin`, `227` (target ranks: base_value=52:123679, first_product=104:121082, bound_value=120:125476, second_product=240:2908, answer=228:1)
- Layer 40: `228`, ` mosunod`, ` dri`, ` talags`, `akume` (target ranks: base_value=52:124901, first_product=104:122289, bound_value=120:114267, second_product=240:1053, answer=228:1)
- Layer 41: ` nuest`, `228`, `iolary`, `印书馆`, ` Didžiulis` (target ranks: base_value=52:87625, first_product=104:101506, bound_value=120:93713, second_product=240:4513, answer=228:2)

### Filler position 15 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=52:124698, first_product=104:119695, bound_value=120:120796, second_product=240:123164, answer=228:122206)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9042, first_product=104:25954, bound_value=120:21112, second_product=240:20473, answer=228:18931)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, `距` (target ranks: base_value=52:4679, first_product=104:21883, bound_value=120:33124, second_product=240:31167, answer=228:23250)
- Layer 30: ` twice`, ` Tail`, `Tail`, `adows`, `肩` (target ranks: base_value=52:279, first_product=104:512, bound_value=120:82, second_product=240:99, answer=228:3598)
- Layer 35: `240`, `241`, `239`, `二十四`, `242` (target ranks: base_value=52:92573, first_product=104:113372, bound_value=120:18044, second_product=240:1, answer=228:2328)
- Layer 36: `240`, `239`, `241`, `238`, `浆` (target ranks: base_value=52:120202, first_product=104:116308, bound_value=120:5860, second_product=240:1, answer=228:1900)
- Layer 37: `240`, `239`, `241`, ` Turing`, `238` (target ranks: base_value=52:125955, first_product=104:125917, bound_value=120:9520, second_product=240:1, answer=228:4904)
- Layer 38: `240`, `239`, `241`, `�`, `238` (target ranks: base_value=52:119716, first_product=104:128302, bound_value=120:54205, second_product=240:1, answer=228:4718)
- Layer 39: `240`, `�`, ` dátummal`, `abella`, `238` (target ranks: base_value=52:89283, first_product=104:111244, bound_value=120:83922, second_product=240:1, answer=228:1458)
- Layer 40: `240`, ` pals`, `238`, `�`, ` dekameters` (target ranks: base_value=52:60007, first_product=104:110751, bound_value=120:73623, second_product=240:1, answer=228:7)
- Layer 41: `240`, `那两个`, ` .`, `这两位`, `告辞` (target ranks: base_value=52:40232, first_product=104:92365, bound_value=120:49081, second_product=240:1, answer=228:26)

### Filler position 16 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:124892, first_product=104:119987, bound_value=120:121208, second_product=240:123530, answer=228:122553)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10036, first_product=104:27235, bound_value=120:22304, second_product=240:21354, answer=228:19794)
- Layer 20: `ait`, `能被`, `锁定`, ` Walker`, ` smile` (target ranks: base_value=52:6235, first_product=104:27703, bound_value=120:41380, second_product=240:35598, answer=228:28629)
- Layer 30: `鞍`, `Tail`, ` Tail`, `tail`, `atan` (target ranks: base_value=52:910, first_product=104:4035, bound_value=120:945, second_product=240:1630, answer=228:10145)
- Layer 35: `240`, `二十四`, ` Howard`, ` Kaw`, `241` (target ranks: base_value=52:68079, first_product=104:78821, bound_value=120:7, second_product=240:1, answer=228:7005)
- Layer 36: `240`, `120`, ` Kaw`, ` display`, ` Howard` (target ranks: base_value=52:117235, first_product=104:97847, bound_value=120:2, second_product=240:1, answer=228:11683)
- Layer 37: `240`, `120`, `ascals`, `交友`, `极化` (target ranks: base_value=52:125542, first_product=104:115489, bound_value=120:2, second_product=240:1, answer=228:43757)
- Layer 38: `240`, `polar`, `120`, ` polarized`, ` peritoneal` (target ranks: base_value=52:121449, first_product=104:113845, bound_value=120:3, second_product=240:1, answer=228:34158)
- Layer 39: `240`, `�`, `ozygous`, `polar`, ` doubling` (target ranks: base_value=52:99011, first_product=104:89577, bound_value=120:177, second_product=240:1, answer=228:10762)
- Layer 40: `240`, `ascals`, ` Dou`, ` doubly`, ` doubling` (target ranks: base_value=52:53565, first_product=104:75070, bound_value=120:215, second_product=240:1, answer=228:37)
- Layer 41: ` .`, `240`, `那两个`, `ascals`, ` repeatedly` (target ranks: base_value=52:43446, first_product=104:75056, bound_value=120:586, second_product=240:2, answer=228:392)

### Filler position 17 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125030, first_product=104:119881, bound_value=120:121226, second_product=240:123474, answer=228:122656)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:10758, first_product=104:28173, bound_value=120:23461, second_product=240:22410, answer=228:20958)
- Layer 20: ` smile`, `距`, `能被`, ` Engaging`, ` engaging` (target ranks: base_value=52:22220, first_product=104:47314, bound_value=120:59648, second_product=240:51256, answer=228:22463)
- Layer 30: ` twice`, ` Tw`, `反复`, `Tw`, `重复` (target ranks: base_value=52:136, first_product=104:4352, bound_value=120:53593, second_product=240:53126, answer=228:6171)
- Layer 35: ` Tw`, ` twice`, ` repeated`, ` calculator`, `重复` (target ranks: base_value=52:90, first_product=104:1633, bound_value=120:25219, second_product=240:38860, answer=228:2226)
- Layer 36: `翻`, ` repeated`, ` Tw`, `calcul`, `反复` (target ranks: base_value=52:675, first_product=104:701, bound_value=120:26095, second_product=240:42290, answer=228:1168)
- Layer 37: `}<?`, `翻`, `calcul`, `radesh`, `翻了` (target ranks: base_value=52:3368, first_product=104:306, bound_value=120:30828, second_product=240:77876, answer=228:1897)
- Layer 38: `}<?`, `radesh`, `calcul`, `翻`, `的计算` (target ranks: base_value=52:6374, first_product=104:251, bound_value=120:30767, second_product=240:89542, answer=228:4309)
- Layer 39: `}<?`, `覆`, `ophe`, `radesh`, `ophen` (target ranks: base_value=52:5735, first_product=104:2212, bound_value=120:72516, second_product=240:106622, answer=228:14557)
- Layer 40: `ekak`, `坏`, `}<?`, ` nasod`, `覆` (target ranks: base_value=52:2795, first_product=104:1951, bound_value=120:44614, second_product=240:67282, answer=228:2131)
- Layer 41: ` .`, ` `, `然后`, `less`, `<｜end▁of▁sentence｜>` (target ranks: base_value=52:3604, first_product=104:12410, bound_value=120:52726, second_product=240:62165, answer=228:1624)

### Filler position 18 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125100, first_product=104:120095, bound_value=120:121281, second_product=240:123602, answer=228:122821)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10161, first_product=104:28228, bound_value=120:23421, second_product=240:22809, answer=228:20954)
- Layer 20: `ait`, `忑`, ` Walker`, ` engaging`, `锁定` (target ranks: base_value=52:18322, first_product=104:44275, bound_value=120:47328, second_product=240:55058, answer=228:39653)
- Layer 30: `算出`, ` calculator`, `第一步`, `计算的`, `计算出` (target ranks: base_value=52:21311, first_product=104:58581, bound_value=120:87035, second_product=240:99487, answer=228:94371)
- Layer 35: ` Tw`, ` first`, `第一步`, `calcul`, `算出` (target ranks: base_value=52:11321, first_product=104:37980, bound_value=120:82504, second_product=240:88320, answer=228:60083)
- Layer 36: ` first`, `calcul`, `first`, ` Zad`, `计算的` (target ranks: base_value=52:28748, first_product=104:20979, bound_value=120:83872, second_product=240:91820, answer=228:35411)
- Layer 37: `}<?`, `calcul`, ` Zad`, `计算的`, `不加` (target ranks: base_value=52:58111, first_product=104:25830, bound_value=120:103904, second_product=240:116246, answer=228:65915)
- Layer 38: `}<?`, `zat`, `calcul`, `zel`, ` zaz` (target ranks: base_value=52:67775, first_product=104:35169, bound_value=120:95600, second_product=240:116627, answer=228:89697)
- Layer 39: `zat`, `}<?`, `zel`, ` duc`, ` Zad` (target ranks: base_value=52:32167, first_product=104:16547, bound_value=120:70743, second_product=240:90552, answer=228:46936)
- Layer 40: ` z`, `zat`, ` zad`, `zl`, `zij` (target ranks: base_value=52:8125, first_product=104:3542, bound_value=120:35510, second_product=240:48617, answer=228:4242)
- Layer 41: ` zad`, `zl`, `acular`, ` .`, ` intentional` (target ranks: base_value=52:761, first_product=104:1454, bound_value=120:4231, second_product=240:7236, answer=228:167)

### Filler position 19 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125214, first_product=104:120197, bound_value=120:121461, second_product=240:123672, answer=228:123011)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9754, first_product=104:27551, bound_value=120:21946, second_product=240:21715, answer=228:19852)
- Layer 20: `忑`, `清楚楚`, ` engaging`, `能被`, `平行` (target ranks: base_value=52:17311, first_product=104:52186, bound_value=120:61347, second_product=240:66754, answer=228:56032)
- Layer 30: ` diz`, ` Dian`, ` dice`, ` Dice`, ` dij` (target ranks: base_value=52:1372, first_product=104:74881, bound_value=120:116847, second_product=240:121084, answer=228:109392)
- Layer 35: ` diz`, ` dia`, ` dip`, ` dy`, ` dig` (target ranks: base_value=52:593, first_product=104:51600, bound_value=120:107007, second_product=240:105119, answer=228:75203)
- Layer 36: ` diz`, ` dio`, ` dri`, ` dice`, ` stabil` (target ranks: base_value=52:1740, first_product=104:31297, bound_value=120:106665, second_product=240:107046, answer=228:60929)
- Layer 37: ` diz`, `niz`, `翻了`, `}<?`, ` dio` (target ranks: base_value=52:7211, first_product=104:50371, bound_value=120:119518, second_product=240:125299, answer=228:94891)
- Layer 38: ` diz`, `}<?`, `niz`, `迷惑`, `zat` (target ranks: base_value=52:10276, first_product=104:58469, bound_value=120:112926, second_product=240:126681, answer=228:100190)
- Layer 39: `迷惑`, `}<?`, `niz`, `明珠`, `殿堂` (target ranks: base_value=52:31096, first_product=104:45964, bound_value=120:96953, second_product=240:109198, answer=228:47002)
- Layer 40: ` sublim`, ` talags`, `ked`, `迷惑`, ` udalerria` (target ranks: base_value=52:21007, first_product=104:24567, bound_value=120:76876, second_product=240:59551, answer=228:3282)
- Layer 41: ` .`, `acular`, ` `, ` sublim`, ` without` (target ranks: base_value=52:6561, first_product=104:26039, bound_value=120:35788, second_product=240:25859, answer=228:440)

### Filler position 20 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125296, first_product=104:120322, bound_value=120:121673, second_product=240:123781, answer=228:123082)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9554, first_product=104:26901, bound_value=120:21078, second_product=240:20838, answer=228:18880)
- Layer 20: `ait`, `能被`, `忑`, ` Walker`, `锁定` (target ranks: base_value=52:7255, first_product=104:32293, bound_value=120:47728, second_product=240:44898, answer=228:24773)
- Layer 30: `acin`, `漏斗`, `atar`, ` basal`, ` calculator` (target ranks: base_value=52:177, first_product=104:3591, bound_value=120:4671, second_product=240:1204, answer=228:363)
- Layer 35: ` talags`, ` Zad`, `240`, `acin`, `228` (target ranks: base_value=52:232, first_product=104:5093, bound_value=120:89321, second_product=240:3, answer=228:5)
- Layer 36: `228`, `252`, `232`, `学堂`, `acin` (target ranks: base_value=52:6, first_product=104:8036, bound_value=120:80628, second_product=240:340, answer=228:1)
- Layer 37: `228`, ` channels`, ` Channels`, ` dekameters`, `太监` (target ranks: base_value=52:243, first_product=104:36092, bound_value=120:77575, second_product=240:172, answer=228:1)
- Layer 38: `228`, `252`, ` dekameters`, `232`, `<｜place▁holder▁no▁376｜>` (target ranks: base_value=52:502, first_product=104:47894, bound_value=120:91170, second_product=240:65, answer=228:1)
- Layer 39: `228`, `227`, `229`, ` Paglin`, `252` (target ranks: base_value=52:8308, first_product=104:111427, bound_value=120:118421, second_product=240:1625, answer=228:1)
- Layer 40: `228`, ` dekameters`, ` Didžiulis`, `226`, ` embra` (target ranks: base_value=52:8871, first_product=104:106831, bound_value=120:98148, second_product=240:919, answer=228:1)
- Layer 41: ` Didžiulis`, `228`, `iolary`, ` nuest`, `印书馆` (target ranks: base_value=52:6224, first_product=104:90374, bound_value=120:81254, second_product=240:20032, answer=228:2)

### Filler position 21 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125657, first_product=104:121051, bound_value=120:122416, second_product=240:124357, answer=228:123569)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:8945, first_product=104:25872, bound_value=120:20572, second_product=240:20466, answer=228:18651)
- Layer 20: `ait`, `锁定`, `距`, `能被`, `拆` (target ranks: base_value=52:7988, first_product=104:28045, bound_value=120:44338, second_product=240:34150, answer=228:14736)
- Layer 30: `acos`, `冰冰`, `acin`, `粥`, `理性` (target ranks: base_value=52:418, first_product=104:4987, bound_value=120:4707, second_product=240:1177, answer=228:58)
- Layer 35: `acin`, ` talags`, `冰冰`, ` drip`, ` Zad` (target ranks: base_value=52:325, first_product=104:4687, bound_value=120:63607, second_product=240:697, answer=228:86)
- Layer 36: ` talags`, `228`, ` vrijgegeven`, ` gihulagway`, ` Zad` (target ranks: base_value=52:213, first_product=104:28682, bound_value=120:84273, second_product=240:15362, answer=228:2)
- Layer 37: ` vrijgegeven`, `}<?`, `殿堂`, `覆`, ` Zad` (target ranks: base_value=52:5884, first_product=104:49716, bound_value=120:73926, second_product=240:13492, answer=228:8)
- Layer 38: `228`, `殿堂`, ` talags`, `覆`, `328` (target ranks: base_value=52:8699, first_product=104:36414, bound_value=120:72156, second_product=240:17101, answer=228:1)
- Layer 39: `228`, `428`, `229`, `227`, `}<?` (target ranks: base_value=52:45152, first_product=104:98716, bound_value=120:105507, second_product=240:12694, answer=228:1)
- Layer 40: `228`, ` dekameters`, `galan`, `ark`, `232` (target ranks: base_value=52:32506, first_product=104:81795, bound_value=120:76628, second_product=240:5729, answer=228:1)
- Layer 41: `228`, ` .`, ` concentrate`, ` Didžiulis`, ` ` (target ranks: base_value=52:6886, first_product=104:52710, bound_value=120:65086, second_product=240:13187, answer=228:1)

### Filler position 22 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125682, first_product=104:121132, bound_value=120:122557, second_product=240:124392, answer=228:123563)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:8754, first_product=104:25397, bound_value=120:20850, second_product=240:20547, answer=228:19157)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, `cape` (target ranks: base_value=52:7692, first_product=104:30708, bound_value=120:38762, second_product=240:33294, answer=228:22581)
- Layer 30: `第一步`, ` Tw`, `算出`, ` Zad`, `coding` (target ranks: base_value=52:5378, first_product=104:49010, bound_value=120:85758, second_product=240:77836, answer=228:37211)
- Layer 35: ` Tw`, `Tw`, `分解`, `第一步`, ` twice` (target ranks: base_value=52:6935, first_product=104:59927, bound_value=120:103980, second_product=240:94770, answer=228:22119)
- Layer 36: ` Zad`, ` Tw`, `分解`, `calcul`, ` first` (target ranks: base_value=52:15092, first_product=104:32532, bound_value=120:89518, second_product=240:77298, answer=228:5556)
- Layer 37: `}<?`, `zat`, `acos`, ` Zad`, `calcul` (target ranks: base_value=52:36245, first_product=104:58754, bound_value=120:113584, second_product=240:110098, answer=228:16662)
- Layer 38: `zat`, `}<?`, `东海`, ` doubling`, `计算方法` (target ranks: base_value=52:51359, first_product=104:67340, bound_value=120:107233, second_product=240:113329, answer=228:33092)
- Layer 39: `zat`, `东海`, `opters`, `}<?`, `�` (target ranks: base_value=52:18565, first_product=104:39427, bound_value=120:81494, second_product=240:78987, answer=228:8795)
- Layer 40: `zat`, `calcul`, `坏`, `zij`, ` Tw` (target ranks: base_value=52:1368, first_product=104:8578, bound_value=120:45270, second_product=240:29639, answer=228:126)
- Layer 41: ` .`, ` compounded`, ` first`, ` `, `第一步` (target ranks: base_value=52:264, first_product=104:4192, bound_value=120:11054, second_product=240:6184, answer=228:6)

### Filler position 23 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125618, first_product=104:121151, bound_value=120:122612, second_product=240:124468, answer=228:123595)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=52:9962, first_product=104:26247, bound_value=120:21958, second_product=240:21188, answer=228:19728)
- Layer 20: ` smile`, `幽`, `足`, ` Tears`, `ait` (target ranks: base_value=52:9302, first_product=104:32695, bound_value=120:32277, second_product=240:31790, answer=228:17107)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=52:2167, first_product=104:20942, bound_value=120:47965, second_product=240:48198, answer=228:23770)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=52:2068, first_product=104:13893, bound_value=120:46638, second_product=240:47270, answer=228:14001)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=52:4335, first_product=104:6661, bound_value=120:45225, second_product=240:47544, answer=228:6591)
- Layer 37: ` Tw`, `Tw`, `}<?`, ` doubling`, `calcul` (target ranks: base_value=52:18921, first_product=104:10853, bound_value=120:74471, second_product=240:84090, answer=228:15655)
- Layer 38: ` Tw`, `}<?`, ` doubling`, `calcul`, `Tw` (target ranks: base_value=52:29209, first_product=104:17357, bound_value=120:72774, second_product=240:96469, answer=228:24638)
- Layer 39: `}<?`, ` Tw`, `Tw`, ` twisted`, ` twist` (target ranks: base_value=52:5382, first_product=104:6790, bound_value=120:67960, second_product=240:97334, answer=228:22517)
- Layer 40: ` Tw`, `坏`, `duc`, `calcul`, ` twisted` (target ranks: base_value=52:170, first_product=104:660, bound_value=120:30888, second_product=240:55608, answer=228:1095)
- Layer 41: ` .`, ` twist`, ` `, `坏`, ` first` (target ranks: base_value=52:108, first_product=104:3702, bound_value=120:25121, second_product=240:51076, answer=228:397)

### Filler position 24 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125844, first_product=104:121360, bound_value=120:122988, second_product=240:124650, answer=228:123855)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=52:9963, first_product=104:27774, bound_value=120:22184, second_product=240:22009, answer=228:20621)
- Layer 20: ` smile`, `足`, `锁定`, `ait`, `atile` (target ranks: base_value=52:7028, first_product=104:25266, bound_value=120:20320, second_product=240:30329, answer=228:17539)
- Layer 30: ` ignored`, ` v`, `coding`, `忽略`, `/v` (target ranks: base_value=52:16806, first_product=104:56208, bound_value=120:69315, second_product=240:90457, answer=228:49158)
- Layer 35: ` v`, `重复`, ` ignoring`, `忽略`, ` ignored` (target ranks: base_value=52:8130, first_product=104:36859, bound_value=120:47896, second_product=240:77094, answer=228:36312)
- Layer 36: `忽略`, `重复`, ` v`, ` ignoring`, ` ignored` (target ranks: base_value=52:19185, first_product=104:21134, bound_value=120:42486, second_product=240:75763, answer=228:27338)
- Layer 37: `不急`, ` v`, `观望`, ` V`, `坏` (target ranks: base_value=52:54533, first_product=104:39220, bound_value=120:83167, second_product=240:115109, answer=228:57260)
- Layer 38: `不急`, `迷惑`, `坏`, `不着`, ` medief` (target ranks: base_value=52:63752, first_product=104:44780, bound_value=120:88128, second_product=240:120586, answer=228:69584)
- Layer 39: `迷惑`, `殿堂`, `不急`, `东海`, ` medief` (target ranks: base_value=52:62451, first_product=104:56481, bound_value=120:88822, second_product=240:114044, answer=228:66366)
- Layer 40: `不急`, `殿堂`, `acular`, `迷惑`, `坏` (target ranks: base_value=52:17483, first_product=104:36222, bound_value=120:64174, second_product=240:86681, answer=228:19247)
- Layer 41: ` `, `不急`, ` .`, `不需要`, `不会被` (target ranks: base_value=52:4739, first_product=104:26591, bound_value=120:29909, second_product=240:60562, answer=228:4529)

### Filler position 25 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125817, first_product=104:121287, bound_value=120:122864, second_product=240:124563, answer=228:123845)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10307, first_product=104:29427, bound_value=120:23196, second_product=240:23386, answer=228:21255)
- Layer 20: ` smile`, `锁定`, `ait`, `足`, ` LS` (target ranks: base_value=52:10480, first_product=104:27276, bound_value=120:31902, second_product=240:32208, answer=228:16595)
- Layer 30: `纯粹的`, `回答`, `鞍`, ` answer`, `纯粹` (target ranks: base_value=52:21895, first_product=104:35905, bound_value=120:60955, second_product=240:53570, answer=228:21787)
- Layer 35: ` repetition`, `回答`, ` calculator`, ` answer`, `重复` (target ranks: base_value=52:10702, first_product=104:31067, bound_value=120:54324, second_product=240:44015, answer=228:12830)
- Layer 36: `回答`, `calcul`, ` calculator`, ` answer`, ` repetition` (target ranks: base_value=52:16074, first_product=104:29345, bound_value=120:56963, second_product=240:48107, answer=228:7941)
- Layer 37: `calcul`, ` immediate`, `计算的`, ` ответ`, ` follow` (target ranks: base_value=52:46488, first_product=104:51843, bound_value=120:101993, second_product=240:99630, answer=228:16736)
- Layer 38: `calcul`, ` calcul`, ` follow`, `计算的`, `遵循` (target ranks: base_value=52:49042, first_product=104:49501, bound_value=120:101632, second_product=240:107529, answer=228:18047)
- Layer 39: ` RES`, ` Res`, `}<?`, `-res`, ` Resident` (target ranks: base_value=52:43993, first_product=104:62384, bound_value=120:95060, second_product=240:112303, answer=228:29584)
- Layer 40: `calcul`, ` Res`, ` talags`, ` follow`, ` RES` (target ranks: base_value=52:15848, first_product=104:50198, bound_value=120:75905, second_product=240:94236, answer=228:11027)
- Layer 41: `因为这些`, ` just`, `Answer`, `的计算`, ` number` (target ranks: base_value=52:1043, first_product=104:21503, bound_value=120:23061, second_product=240:41011, answer=228:525)

### Filler position 26 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:125985, first_product=104:121623, bound_value=120:123202, second_product=240:124709, answer=228:123969)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9482, first_product=104:27279, bound_value=120:22032, second_product=240:21347, answer=228:19139)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `拆` (target ranks: base_value=52:8435, first_product=104:27628, bound_value=120:37326, second_product=240:39451, answer=228:23027)
- Layer 30: ` diz`, `算出`, ` dio`, ` calculator`, `计算的` (target ranks: base_value=52:7669, first_product=104:53792, bound_value=120:108243, second_product=240:103766, answer=228:75817)
- Layer 35: ` Tw`, ` dy`, ` diz`, ` dip`, ` drip` (target ranks: base_value=52:4721, first_product=104:36161, bound_value=120:103826, second_product=240:90177, answer=228:34874)
- Layer 36: ` drip`, ` dri`, ` diz`, ` dio`, `留存` (target ranks: base_value=52:8416, first_product=104:17542, bound_value=120:105846, second_product=240:90112, answer=228:11736)
- Layer 37: ` diz`, `}<?`, `翻了`, ` drip`, ` dic` (target ranks: base_value=52:35436, first_product=104:29035, bound_value=120:124346, second_product=240:117846, answer=228:26931)
- Layer 38: `}<?`, `zat`, ` diz`, `迷惑`, `殿堂` (target ranks: base_value=52:53972, first_product=104:39340, bound_value=120:121823, second_product=240:120290, answer=228:53138)
- Layer 39: `迷惑`, `zat`, ` duc`, `}<?`, `殿堂` (target ranks: base_value=52:18905, first_product=104:25336, bound_value=120:106659, second_product=240:98798, answer=228:22281)
- Layer 40: `scr`, `calcul`, ` Tw`, ` udalerria`, `计算的` (target ranks: base_value=52:5694, first_product=104:10873, bound_value=120:81802, second_product=240:60886, answer=228:972)
- Layer 41: `计算的`, `zl`, `šk`, `步骤如下`, ` Calculators` (target ranks: base_value=52:679, first_product=104:6308, bound_value=120:33626, second_product=240:22737, answer=228:74)

### Filler position 27 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126034, first_product=104:121576, bound_value=120:123158, second_product=240:124638, answer=228:123838)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9431, first_product=104:25660, bound_value=120:21335, second_product=240:20024, answer=228:18373)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `距` (target ranks: base_value=52:8632, first_product=104:27163, bound_value=120:36924, second_product=240:33324, answer=228:20132)
- Layer 30: ` diz`, `第一步`, ` dip`, ` dio`, ` dilat` (target ranks: base_value=52:7197, first_product=104:40053, bound_value=120:103070, second_product=240:82764, answer=228:48193)
- Layer 35: ` dip`, ` dy`, ` drip`, ` dio`, ` diz` (target ranks: base_value=52:7105, first_product=104:44927, bound_value=120:110128, second_product=240:85012, answer=228:30168)
- Layer 36: ` dri`, ` drip`, `留存`, ` dio`, ` diz` (target ranks: base_value=52:17158, first_product=104:25896, bound_value=120:107975, second_product=240:77916, answer=228:11684)
- Layer 37: ` diz`, ` drip`, `翻了`, ` dic`, ` dio` (target ranks: base_value=52:50970, first_product=104:40342, bound_value=120:123693, second_product=240:109075, answer=228:21167)
- Layer 38: `zat`, ` diz`, ` Dio`, ` dio`, `殿堂` (target ranks: base_value=52:62459, first_product=104:51801, bound_value=120:121686, second_product=240:114418, answer=228:42999)
- Layer 39: `zat`, ` diz`, `迷惑`, `殿堂`, ` Dio` (target ranks: base_value=52:22110, first_product=104:40621, bound_value=120:111282, second_product=240:97505, answer=228:30120)
- Layer 40: `calcul`, ` diz`, `zat`, `的计算`, `计算的` (target ranks: base_value=52:9232, first_product=104:20146, bound_value=120:90554, second_product=240:51882, answer=228:1542)
- Layer 41: `的计算`, `acular`, `ffff`, ` `, `计算结果` (target ranks: base_value=52:2502, first_product=104:7735, bound_value=120:29670, second_product=240:19662, answer=228:64)

### Filler position 28 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126471, first_product=104:122494, bound_value=120:123933, second_product=240:125249, answer=228:124447)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:9745, first_product=104:25703, bound_value=120:21244, second_product=240:20504, answer=228:19148)
- Layer 20: `能被`, `ait`, `拆`, ` Walker`, ` engaging` (target ranks: base_value=52:9269, first_product=104:28842, bound_value=120:35589, second_product=240:31184, answer=228:21378)
- Layer 30: `52`, `分解`, `acin`, ` calculator`, ` parallel` (target ranks: base_value=52:1, first_product=104:241, bound_value=120:65711, second_product=240:80351, answer=228:4349)
- Layer 35: `分解`, `52`, ` calculator`, ` decompose`, `acin` (target ranks: base_value=52:2, first_product=104:172, bound_value=120:25361, second_product=240:61022, answer=228:4024)
- Layer 36: `分解`, `翻`, ` decom`, `acin`, ` stabil` (target ranks: base_value=52:10, first_product=104:108, bound_value=120:25065, second_product=240:59343, answer=228:3002)
- Layer 37: `}<?`, `翻了`, `翻`, `radesh`, `分解` (target ranks: base_value=52:17, first_product=104:153, bound_value=120:48982, second_product=240:110949, answer=228:16525)
- Layer 38: `}<?`, `覆`, `殿堂`, `osit`, `科学院` (target ranks: base_value=52:137, first_product=104:889, bound_value=120:65235, second_product=240:119712, answer=228:30867)
- Layer 39: `}<?`, `覆`, `殿堂`, `galan`, `ocyst` (target ranks: base_value=52:110, first_product=104:4276, bound_value=120:90908, second_product=240:102531, answer=228:35625)
- Layer 40: ` diz`, `殿堂`, ` Tw`, `翻`, ` twist` (target ranks: base_value=52:588, first_product=104:4994, bound_value=120:49649, second_product=240:24129, answer=228:2429)
- Layer 41: ` diz`, ` .`, ` `, `实在`, ` dic` (target ranks: base_value=52:176, first_product=104:3729, bound_value=120:18418, second_product=240:16257, answer=228:713)

### Filler position 29 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126410, first_product=104:122301, bound_value=120:123807, second_product=240:125118, answer=228:124376)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:10205, first_product=104:26491, bound_value=120:21828, second_product=240:21521, answer=228:19920)
- Layer 20: `能被`, ` smile`, `锁定`, `ession`, `ait` (target ranks: base_value=52:12532, first_product=104:31944, bound_value=120:37509, second_product=240:37012, answer=228:20742)
- Layer 30: `ession`, `�`, ` tear`, ` reserved`, ` v` (target ranks: base_value=52:15982, first_product=104:35280, bound_value=120:66518, second_product=240:86947, answer=228:37197)
- Layer 35: ` reserved`, `锁定`, `分解`, `重复`, ` tears` (target ranks: base_value=52:6000, first_product=104:20275, bound_value=120:43770, second_product=240:69785, answer=228:21611)
- Layer 36: `分解`, ` reserved`, `留存`, `俯`, ` drib` (target ranks: base_value=52:13119, first_product=104:12909, bound_value=120:43233, second_product=240:65770, answer=228:14479)
- Layer 37: `radesh`, `}<?`, `坏`, `冰冰`, ` torn` (target ranks: base_value=52:25612, first_product=104:17927, bound_value=120:70066, second_product=240:101106, answer=228:21508)
- Layer 38: `zat`, `坏`, `radesh`, `冰冰`, `}<?` (target ranks: base_value=52:23424, first_product=104:14157, bound_value=120:71836, second_product=240:103662, answer=228:22194)
- Layer 39: `<｜begin▁of▁sentence｜>`, `坏`, `}<?`, `zat`, `覆` (target ranks: base_value=52:46505, first_product=104:50989, bound_value=120:103341, second_product=240:121002, answer=228:68233)
- Layer 40: `坏`, `冰冰`, `坏了`, `坏的`, `殿堂` (target ranks: base_value=52:13374, first_product=104:29977, bound_value=120:81900, second_product=240:101267, answer=228:25106)
- Layer 41: ` .`, `坏`, `没有被`, `从前`, `坏了` (target ranks: base_value=52:10020, first_product=104:20556, bound_value=120:42310, second_product=240:76563, answer=228:4092)

### Filler position 30 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126437, first_product=104:122220, bound_value=120:123798, second_product=240:125061, answer=228:124289)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9565, first_product=104:25790, bound_value=120:21078, second_product=240:20772, answer=228:19148)
- Layer 20: `atile`, `cape`, `鞍`, ` wig`, `ait` (target ranks: base_value=52:10278, first_product=104:26749, bound_value=120:28270, second_product=240:34293, answer=228:29041)
- Layer 30: ` rip`, ` Zad`, ` riv`, ` zad`, ` Zig` (target ranks: base_value=52:58212, first_product=104:88810, bound_value=120:120834, second_product=240:103012, answer=228:114718)
- Layer 35: `Tap`, ` tap`, ` rip`, ` vib`, ` riv` (target ranks: base_value=52:32971, first_product=104:62629, bound_value=120:119718, second_product=240:96751, answer=228:77946)
- Layer 36: ` riv`, `坏`, ` tap`, ` rip`, ` zad` (target ranks: base_value=52:34442, first_product=104:27540, bound_value=120:97606, second_product=240:71236, answer=228:44721)
- Layer 37: `坏`, `amol`, `坏的`, `zat`, ` mim` (target ranks: base_value=52:68055, first_product=104:42216, bound_value=120:118108, second_product=240:104344, answer=228:76520)
- Layer 38: `本题分析`, `zat`, `}<?`, `疑惑`, `gev` (target ranks: base_value=52:96016, first_product=104:67926, bound_value=120:113008, second_product=240:114094, answer=228:91680)
- Layer 39: `zat`, ` Nij`, `polar`, `oNames`, `gev` (target ranks: base_value=52:70587, first_product=104:31845, bound_value=120:104601, second_product=240:102618, answer=228:60444)
- Layer 40: `zel`, `y`, `zij`, `zat`, `殿堂` (target ranks: base_value=52:55326, first_product=104:31820, bound_value=120:95377, second_product=240:95028, answer=228:45175)
- Layer 41: `zel`, `zij`, `坏`, `坏的`, ` mim` (target ranks: base_value=52:28653, first_product=104:34379, bound_value=120:52820, second_product=240:65485, answer=228:25362)

### Filler position 31 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126474, first_product=104:122494, bound_value=120:124099, second_product=240:125353, answer=228:124594)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9131, first_product=104:25332, bound_value=120:20213, second_product=240:20601, answer=228:18903)
- Layer 20: `锁定`, `ait`, `鞍`, ` LS`, ` smile` (target ranks: base_value=52:7843, first_product=104:22307, bound_value=120:25130, second_product=240:31985, answer=228:19698)
- Layer 30: `鞍`, ` tap`, `Tap`, ` labor`, `锁定` (target ranks: base_value=52:11012, first_product=104:54495, bound_value=120:50998, second_product=240:75721, answer=228:29792)
- Layer 35: `锁定`, ` tap`, ` labor`, `鞍`, `cape` (target ranks: base_value=52:11176, first_product=104:44445, bound_value=120:36360, second_product=240:74554, answer=228:20478)
- Layer 36: ` tap`, ` stabil`, `柿子`, `cape`, `Tap` (target ranks: base_value=52:11147, first_product=104:24931, bound_value=120:22633, second_product=240:62764, answer=228:10119)
- Layer 37: ` nasod`, `冰冰`, `坏`, ` stabil`, `留存` (target ranks: base_value=52:33046, first_product=104:42518, bound_value=120:43306, second_product=240:110798, answer=228:18476)
- Layer 38: ` nasod`, `冰冰`, `坏`, `radesh`, `寒风` (target ranks: base_value=52:68215, first_product=104:50422, bound_value=120:58896, second_product=240:119005, answer=228:25788)
- Layer 39: `<｜begin▁of▁sentence｜>`, `打磨`, `acular`, `ocyst`, `殿堂` (target ranks: base_value=52:37632, first_product=104:60013, bound_value=120:70063, second_product=240:121938, answer=228:46373)
- Layer 40: `acular`, ` nasod`, `<｜begin▁of▁sentence｜>`, `坏`, `坏了` (target ranks: base_value=52:4225, first_product=104:32297, bound_value=120:35610, second_product=240:111273, answer=228:25045)
- Layer 41: ` .`, ` `, `坏`, `acular`, `冰冰` (target ranks: base_value=52:1401, first_product=104:24900, bound_value=120:21126, second_product=240:91020, answer=228:8327)

### Filler position 32 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=52:126543, first_product=104:122736, bound_value=120:124217, second_product=240:125457, answer=228:124593)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:8779, first_product=104:25048, bound_value=120:19567, second_product=240:20861, answer=228:18420)
- Layer 20: ` ES`, ` Walker`, ` LS`, `Walker`, `ait` (target ranks: base_value=52:7587, first_product=104:21220, bound_value=120:23619, second_product=240:30891, answer=228:15223)
- Layer 30: `鞍`, ` Ries`, `eder`, `acin`, `acic` (target ranks: base_value=52:446, first_product=104:909, bound_value=120:7299, second_product=240:10976, answer=228:2073)
- Layer 35: ` Behavior`, `232`, `acin`, ` labor`, ` familiar` (target ranks: base_value=52:1180, first_product=104:1413, bound_value=120:34666, second_product=240:78, answer=228:136)
- Layer 36: `acin`, ` familiar`, `232`, `熟悉`, ` talags` (target ranks: base_value=52:7440, first_product=104:1118, bound_value=120:29537, second_product=240:42, answer=228:17)
- Layer 37: `}<?`, ` fat`, ` Montreal`, `迷惑`, `交友` (target ranks: base_value=52:69135, first_product=104:11061, bound_value=120:53966, second_product=240:28, answer=228:107)
- Layer 38: `冒出`, ` fat`, `殿堂`, `摸了`, `迷惑` (target ranks: base_value=52:52812, first_product=104:5634, bound_value=120:70135, second_product=240:220, answer=228:25)
- Layer 39: `228`, `232`, `}<?`, `radesh`, `东海` (target ranks: base_value=52:29190, first_product=104:1887, bound_value=120:60553, second_product=240:197, answer=228:1)
- Layer 40: `228`, `227`, ` talags`, `232`, `zel` (target ranks: base_value=52:4333, first_product=104:1735, bound_value=120:30182, second_product=240:77, answer=228:1)
- Layer 41: `228`, ` .`, ` twice`, ` `, ` awaiting` (target ranks: base_value=52:4042, first_product=104:7410, bound_value=120:47024, second_product=240:1921, answer=228:1)

### Filler position 33 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:126795, first_product=104:123253, bound_value=120:124765, second_product=240:125822, answer=228:124930)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:8330, first_product=104:24694, bound_value=120:19697, second_product=240:20545, answer=228:17790)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=52:7706, first_product=104:23921, bound_value=120:33055, second_product=240:40183, answer=228:20206)
- Layer 30: ` diz`, `acin`, ` dy`, ` basal`, ` Diet` (target ranks: base_value=52:6402, first_product=104:67778, bound_value=120:107745, second_product=240:113423, answer=228:90125)
- Layer 35: ` diz`, ` dip`, ` dy`, ` dio`, `留存` (target ranks: base_value=52:2969, first_product=104:36470, bound_value=120:90677, second_product=240:90016, answer=228:53486)
- Layer 36: `留存`, `年开始`, `ayi`, ` stabil`, ` starting` (target ranks: base_value=52:5038, first_product=104:19871, bound_value=120:86918, second_product=240:90648, answer=228:31749)
- Layer 37: `}<?`, ` talags`, `acos`, `Tinubdan`, `不加` (target ranks: base_value=52:19705, first_product=104:43986, bound_value=120:116101, second_product=240:120839, answer=228:61675)
- Layer 38: `}<?`, `zat`, ` BASIS`, ` Basis`, `殿堂` (target ranks: base_value=52:21351, first_product=104:53129, bound_value=120:117190, second_product=240:122840, answer=228:74795)
- Layer 39: `迷惑`, `}<?`, ` sublim`, ` BASIS`, `zat` (target ranks: base_value=52:6337, first_product=104:57962, bound_value=120:117669, second_product=240:123534, answer=228:85272)
- Layer 40: ` diz`, `zij`, ` sublim`, ` talags`, ` compounding` (target ranks: base_value=52:275, first_product=104:24390, bound_value=120:99610, second_product=240:105343, answer=228:24031)
- Layer 41: ` diz`, `zij`, ` whichever`, ` compounding`, `xyz` (target ranks: base_value=52:51, first_product=104:27921, bound_value=120:76838, second_product=240:93014, answer=228:6649)

### Filler position 34 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=52:126802, first_product=104:123108, bound_value=120:124746, second_product=240:125777, answer=228:124933)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:8640, first_product=104:24859, bound_value=120:20410, second_product=240:20107, answer=228:17571)
- Layer 20: `ait`, `锁定`, ` Walker`, ` smile`, `Walker` (target ranks: base_value=52:8856, first_product=104:26571, bound_value=120:43464, second_product=240:40024, answer=228:24511)
- Layer 30: `coding`, `cod`, `kod`, ` coding`, ` cod` (target ranks: base_value=52:5313, first_product=104:37590, bound_value=120:102453, second_product=240:109210, answer=228:77194)
- Layer 35: `coding`, `cod`, `kod`, ` coding`, `code` (target ranks: base_value=52:4301, first_product=104:34230, bound_value=120:90093, second_product=240:101698, answer=228:44001)
- Layer 36: `coding`, `cod`, ` Zad`, ` coding`, `kod` (target ranks: base_value=52:9725, first_product=104:18938, bound_value=120:81282, second_product=240:95711, answer=228:25027)
- Layer 37: `zat`, `}<?`, ` Zad`, `coding`, ` Zij` (target ranks: base_value=52:21493, first_product=104:35893, bound_value=120:99779, second_product=240:118770, answer=228:41516)
- Layer 38: `zat`, ` z`, ` Zad`, `zas`, `zuf` (target ranks: base_value=52:21954, first_product=104:35196, bound_value=120:87823, second_product=240:115838, answer=228:46926)
- Layer 39: `zat`, ` z`, ` Zij`, `zij`, `zv` (target ranks: base_value=52:6908, first_product=104:51791, bound_value=120:94843, second_product=240:118050, answer=228:44118)
- Layer 40: ` z`, `zij`, ` Z`, `zat`, `z` (target ranks: base_value=52:946, first_product=104:32572, bound_value=120:76916, second_product=240:107105, answer=228:13228)
- Layer 41: `zij`, `z`, ` compounded`, ` compounding`, `zel` (target ranks: base_value=52:119, first_product=104:19408, bound_value=120:39219, second_product=240:69615, answer=228:952)

### Filler position 35 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:126864, first_product=104:123442, bound_value=120:125019, second_product=240:125948, answer=228:125100)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10053, first_product=104:26303, bound_value=120:22063, second_product=240:21215, answer=228:18869)
- Layer 20: `ait`, ` smile`, `锁定`, `足`, `cape` (target ranks: base_value=52:5595, first_product=104:17882, bound_value=120:23338, second_product=240:18613, answer=228:10815)
- Layer 30: `68`, `328`, `sets`, `228`, `题库` (target ranks: base_value=52:223, first_product=104:541, bound_value=120:877, second_product=240:99, answer=228:4)
- Layer 35: `240`, ` Zad`, `akak`, `228`, ` dunay` (target ranks: base_value=52:951, first_product=104:362, bound_value=120:57380, second_product=240:1, answer=228:4)
- Layer 36: `228`, `229`, `428`, `232`, `海中` (target ranks: base_value=52:399, first_product=104:16696, bound_value=120:64285, second_product=240:13, answer=228:1)
- Layer 37: `228`, `240`, `232`, ` fat`, `fat` (target ranks: base_value=52:8279, first_product=104:46286, bound_value=120:49978, second_product=240:2, answer=228:1)
- Layer 38: `228`, `229`, `428`, `232`, `248` (target ranks: base_value=52:12814, first_product=104:51603, bound_value=120:68114, second_product=240:8, answer=228:1)
- Layer 39: `228`, `229`, `428`, `227`, ` Paglin` (target ranks: base_value=52:95985, first_product=104:122580, bound_value=120:120888, second_product=240:878, answer=228:1)
- Layer 40: `228`, ` dekameters`, `229`, `}using`, ` guarante` (target ranks: base_value=52:77305, first_product=104:120462, bound_value=120:106690, second_product=240:628, answer=228:1)
- Layer 41: `228`, ` nuest`, `iolary`, ` Didžiulis`, `印书馆` (target ranks: base_value=52:22729, first_product=104:97978, bound_value=120:97252, second_product=240:10302, answer=228:1)

### Filler position 36 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:126858, first_product=104:123291, bound_value=120:124979, second_product=240:125919, answer=228:125013)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:11255, first_product=104:28640, bound_value=120:23373, second_product=240:22987, answer=228:20865)
- Layer 20: ` engaging`, `能被`, ` Engaging`, `拆`, `距` (target ranks: base_value=52:22988, first_product=104:51908, bound_value=120:51093, second_product=240:46834, answer=228:36081)
- Layer 30: `算出`, ` diz`, ` dez`, ` dice`, ` Zad` (target ranks: base_value=52:905, first_product=104:50350, bound_value=120:111953, second_product=240:102776, answer=228:73041)
- Layer 35: ` diz`, `算出`, ` dice`, ` dez`, `cod` (target ranks: base_value=52:568, first_product=104:35478, bound_value=120:104781, second_product=240:86655, answer=228:41098)
- Layer 36: ` diz`, `辞`, ` dice`, `算出`, `翻` (target ranks: base_value=52:1558, first_product=104:14011, bound_value=120:94794, second_product=240:72516, answer=228:14533)
- Layer 37: ` diz`, `zat`, `niz`, `翻了`, `ertz` (target ranks: base_value=52:2617, first_product=104:18348, bound_value=120:102109, second_product=240:99456, answer=228:23776)
- Layer 38: `zat`, ` diz`, `zel`, `zal`, `ertz` (target ranks: base_value=52:4393, first_product=104:16213, bound_value=120:79734, second_product=240:100535, answer=228:29377)
- Layer 39: `zat`, `zal`, `zel`, ` zav`, `lez` (target ranks: base_value=52:6926, first_product=104:27670, bound_value=120:94130, second_product=240:86428, answer=228:9480)
- Layer 40: ` z`, `zat`, ` Z`, `.z`, `zel` (target ranks: base_value=52:1382, first_product=104:9844, bound_value=120:65529, second_product=240:24480, answer=228:36)
- Layer 41: `228`, ` zad`, `zl`, `zel`, ` ` (target ranks: base_value=52:144, first_product=104:4014, bound_value=120:14851, second_product=240:4137, answer=228:1)

### Filler position 37 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:126930, first_product=104:123450, bound_value=120:125060, second_product=240:125962, answer=228:125134)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10927, first_product=104:29110, bound_value=120:23155, second_product=240:22927, answer=228:21322)
- Layer 20: `能被`, ` engaging`, `ait`, `ätte`, `sl` (target ranks: base_value=52:25180, first_product=104:52023, bound_value=120:50239, second_product=240:60943, answer=228:45382)
- Layer 30: `coding`, `cod`, `kod`, ` Kod`, ` kod` (target ranks: base_value=52:34526, first_product=104:58360, bound_value=120:80306, second_product=240:110677, answer=228:95053)
- Layer 35: `kod`, `cod`, `coding`, `code`, ` Kod` (target ranks: base_value=52:14895, first_product=104:41142, bound_value=120:55548, second_product=240:95722, answer=228:63255)
- Layer 36: `cod`, `coding`, `kod`, `忽略`, `留存` (target ranks: base_value=52:26855, first_product=104:23558, bound_value=120:46179, second_product=240:94046, answer=228:51025)
- Layer 37: `}<?`, `cod`, `coding`, `不急`, `zat` (target ranks: base_value=52:66313, first_product=104:42339, bound_value=120:79565, second_product=240:122846, answer=228:85002)
- Layer 38: `zat`, `}<?`, `不急`, `迷惑`, `cod` (target ranks: base_value=52:65986, first_product=104:42602, bound_value=120:80557, second_product=240:124499, answer=228:92732)
- Layer 39: `<｜begin▁of▁sentence｜>`, `迷惑`, `语言文字`, `打磨`, `zat` (target ranks: base_value=52:66610, first_product=104:58417, bound_value=120:82987, second_product=240:122631, answer=228:74381)
- Layer 40: `<｜begin▁of▁sentence｜>`, `acular`, `不急`, `坏`, `不加` (target ranks: base_value=52:19802, first_product=104:33423, bound_value=120:42803, second_product=240:107177, answer=228:22206)
- Layer 41: ` `, ` .`, `不重要`, `less`, `语言文字` (target ranks: base_value=52:5818, first_product=104:18535, bound_value=120:13431, second_product=240:77192, answer=228:4173)

### Filler position 38 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127014, first_product=104:123452, bound_value=120:125084, second_product=240:125960, answer=228:125241)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10240, first_product=104:28099, bound_value=120:21915, second_product=240:22038, answer=228:19810)
- Layer 20: `ait`, `忑`, `能被`, ` engaging`, ` ES` (target ranks: base_value=52:12306, first_product=104:37856, bound_value=120:34880, second_product=240:43806, answer=228:32680)
- Layer 30: `acic`, `adak`, `acin`, `Tw`, ` calculator` (target ranks: base_value=52:114, first_product=104:1073, bound_value=120:12241, second_product=240:31726, answer=228:10217)
- Layer 35: `acic`, `acin`, `退出`, `obin`, ` Behavior` (target ranks: base_value=52:1646, first_product=104:374, bound_value=120:37921, second_product=240:2233, answer=228:808)
- Layer 36: `acin`, ` talags`, `aci`, `院内`, ` familiar` (target ranks: base_value=52:7341, first_product=104:430, bound_value=120:35932, second_product=240:1343, answer=228:15)
- Layer 37: `}<?`, `?datasetId`, `院内`, `ajes`, `殿堂` (target ranks: base_value=52:62555, first_product=104:2908, bound_value=120:49379, second_product=240:629, answer=228:31)
- Layer 38: `院内`, `凌霄`, `殿堂`, `院长`, `故宫` (target ranks: base_value=52:71388, first_product=104:3192, bound_value=120:57891, second_product=240:552, answer=228:14)
- Layer 39: `228`, `第二百`, `东海`, `故宫`, `214` (target ranks: base_value=52:95142, first_product=104:35563, bound_value=120:90403, second_product=240:3765, answer=228:1)
- Layer 40: `228`, `第二百`, `zel`, `zl`, ` dekameters` (target ranks: base_value=52:70379, first_product=104:43504, bound_value=120:65149, second_product=240:786, answer=228:1)
- Layer 41: `228`, `zl`, ` .`, `zel`, `z` (target ranks: base_value=52:21766, first_product=104:25861, bound_value=120:52289, second_product=240:2482, answer=228:1)

### Filler position 39 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=52:127022, first_product=104:123322, bound_value=120:124890, second_product=240:125768, answer=228:125053)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:9995, first_product=104:26848, bound_value=120:21586, second_product=240:21366, answer=228:19199)
- Layer 20: `ait`, `锁定`, ` Walker`, `忑`, ` ES` (target ranks: base_value=52:6979, first_product=104:22151, bound_value=120:28022, second_product=240:25468, answer=228:16735)
- Layer 30: `打完`, `eder`, `下沉`, ` calculator`, `Tw` (target ranks: base_value=52:221, first_product=104:698, bound_value=120:36803, second_product=240:17509, answer=228:581)
- Layer 35: `acin`, `Subt`, ` Subt`, `测算`, `obin` (target ranks: base_value=52:910, first_product=104:455, bound_value=120:89765, second_product=240:6417, answer=228:11)
- Layer 36: `228`, `acin`, ` Zad`, `院内`, `anium` (target ranks: base_value=52:11215, first_product=104:1030, bound_value=120:89663, second_product=240:7621, answer=228:1)
- Layer 37: `}<?`, `?datasetId`, `白马`, ` smoot`, `228` (target ranks: base_value=52:78321, first_product=104:11769, bound_value=120:95124, second_product=240:5253, answer=228:5)
- Layer 38: `}<?`, `本题分析`, `iota`, `?datasetId`, `院内` (target ranks: base_value=52:105998, first_product=104:18287, bound_value=120:103084, second_product=240:12219, answer=228:25)
- Layer 39: `228`, `?datasetId`, `}<?`, `aharoa`, `第二百` (target ranks: base_value=52:124040, first_product=104:102141, bound_value=120:116540, second_product=240:3595, answer=228:1)
- Layer 40: `228`, `acular`, `留存`, `227`, `第二百` (target ranks: base_value=52:123892, first_product=104:113349, bound_value=120:117167, second_product=240:1926, answer=228:1)
- Layer 41: `228`, `因为这些`, `227`, `zl`, `这个词` (target ranks: base_value=52:67698, first_product=104:88716, bound_value=120:102974, second_product=240:7237, answer=228:1)

### Filler position 40 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127162, first_product=104:123652, bound_value=120:125305, second_product=240:126008, answer=228:125303)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10539, first_product=104:27989, bound_value=120:22031, second_product=240:22273, answer=228:19726)
- Layer 20: `ait`, `能被`, ` LS`, `鞍`, `ätte` (target ranks: base_value=52:3585, first_product=104:18375, bound_value=120:21853, second_product=240:24931, answer=228:13258)
- Layer 30: `68`, `328`, `方便`, `六十`, `76` (target ranks: base_value=52:81, first_product=104:397, bound_value=120:1449, second_product=240:257, answer=228:25)
- Layer 35: `240`, `akak`, `228`, `二百`, ` polarized` (target ranks: base_value=52:1224, first_product=104:488, bound_value=120:38412, second_product=240:1, answer=228:3)
- Layer 36: `228`, `229`, `232`, `230`, `227` (target ranks: base_value=52:1373, first_product=104:23201, bound_value=120:45602, second_product=240:9, answer=228:1)
- Layer 37: `228`, `230`, `232`, `229`, ` vrijgegeven` (target ranks: base_value=52:29419, first_product=104:63055, bound_value=120:48271, second_product=240:6, answer=228:1)
- Layer 38: `228`, `229`, `227`, `230`, `232` (target ranks: base_value=52:96559, first_product=104:90983, bound_value=120:108364, second_product=240:9, answer=228:1)
- Layer 39: `228`, `229`, `227`, `428`, ` Paglin` (target ranks: base_value=52:121730, first_product=104:124239, bound_value=120:125679, second_product=240:7993, answer=228:1)
- Layer 40: `228`, ` dekameters`, `inz`, `实在`, ` Didžiulis` (target ranks: base_value=52:116086, first_product=104:119843, bound_value=120:118918, second_product=240:9104, answer=228:1)
- Layer 41: ` nuest`, `228`, `iolary`, ` Didžiulis`, `等待` (target ranks: base_value=52:86160, first_product=104:92879, bound_value=120:98959, second_product=240:17213, answer=228:2)

### Filler position 41 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=52:126933, first_product=104:123176, bound_value=120:124950, second_product=240:125796, answer=228:125043)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10488, first_product=104:27953, bound_value=120:21630, second_product=240:22027, answer=228:19547)
- Layer 20: `能被`, `锁定`, `ait`, ` LS`, `LS` (target ranks: base_value=52:8016, first_product=104:23433, bound_value=120:27501, second_product=240:26721, answer=228:20864)
- Layer 30: `tail`, ` tail`, ` Tail`, `Tail`, `tails` (target ranks: base_value=52:1105, first_product=104:4646, bound_value=120:699, second_product=240:302, answer=228:2072)
- Layer 35: `240`, `239`, `akak`, `241`, `四十` (target ranks: base_value=52:13556, first_product=104:47151, bound_value=120:87215, second_product=240:1, answer=228:1044)
- Layer 36: `240`, `239`, ` Toyota`, `交友`, `241` (target ranks: base_value=52:50966, first_product=104:60859, bound_value=120:48628, second_product=240:1, answer=228:435)
- Layer 37: `240`, `239`, ` Turing`, `交友`, ` Toyota` (target ranks: base_value=52:91372, first_product=104:95799, bound_value=120:52609, second_product=240:1, answer=228:2514)
- Layer 38: `240`, `239`, `241`, ` Toy`, `<｜place▁holder▁no▁93｜>` (target ranks: base_value=52:28932, first_product=104:98397, bound_value=120:121466, second_product=240:1, answer=228:145)
- Layer 39: `228`, ` dátummal`, `238`, `226`, `�` (target ranks: base_value=52:7615, first_product=104:37200, bound_value=120:123599, second_product=240:13, answer=228:1)
- Layer 40: `228`, ` dekameters`, `第二百`, `227`, ` backdrop` (target ranks: base_value=52:9949, first_product=104:55378, bound_value=120:118730, second_product=240:14, answer=228:1)
- Layer 41: `228`, ` dekameters`, `这两位`, ` .`, ` waiting` (target ranks: base_value=52:9590, first_product=104:45622, bound_value=120:93394, second_product=240:553, answer=228:1)

### Filler position 42 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127106, first_product=104:123616, bound_value=120:125303, second_product=240:126051, answer=228:125251)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:11024, first_product=104:28520, bound_value=120:21953, second_product=240:22348, answer=228:19893)
- Layer 20: `锁定`, `cape`, `鞍`, ` smile`, `ait` (target ranks: base_value=52:9516, first_product=104:27073, bound_value=120:26415, second_product=240:24414, answer=228:13741)
- Layer 30: `iab`, `tails`, `鞍`, `二十八`, `twenty` (target ranks: base_value=52:3089, first_product=104:48377, bound_value=120:52510, second_product=240:12699, answer=228:816)
- Layer 35: `acic`, `�`, `沛`, ` dunay`, ` Theodore` (target ranks: base_value=52:2327, first_product=104:11198, bound_value=120:62300, second_product=240:155, answer=228:205)
- Layer 36: `228`, `二十八`, ` talags`, `受教育`, `edback` (target ranks: base_value=52:1178, first_product=104:57383, bound_value=120:70575, second_product=240:3127, answer=228:1)
- Layer 37: `edback`, `228`, `宫内`, `观的`, `受教育` (target ranks: base_value=52:17115, first_product=104:80373, bound_value=120:54477, second_product=240:1940, answer=228:2)
- Layer 38: `228`, `二十八`, `本题分析`, `ianhi`, `宫内` (target ranks: base_value=52:75219, first_product=104:82667, bound_value=120:55387, second_product=240:2253, answer=228:1)
- Layer 39: `228`, `229`, `本题分析`, `428`, `227` (target ranks: base_value=52:123696, first_product=104:122121, bound_value=120:108920, second_product=240:3197, answer=228:1)
- Layer 40: `228`, `第二百`, `ekak`, `二百`, `本题分析` (target ranks: base_value=52:122005, first_product=104:121262, bound_value=120:97027, second_product=240:1180, answer=228:1)
- Layer 41: `228`, ` nuest`, ` .`, `本题分析`, `因为这些` (target ranks: base_value=52:58334, first_product=104:84857, bound_value=120:69874, second_product=240:5427, answer=228:1)

### Filler position 43 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127049, first_product=104:123549, bound_value=120:125236, second_product=240:126016, answer=228:125160)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10650, first_product=104:28371, bound_value=120:21462, second_product=240:22767, answer=228:20069)
- Layer 20: `LS`, `锁定`, ` smile`, ` LS`, `距` (target ranks: base_value=52:10853, first_product=104:26760, bound_value=120:20178, second_product=240:24581, answer=228:21557)
- Layer 30: `鞍`, `eas`, `沛`, `eder`, `atan` (target ranks: base_value=52:4333, first_product=104:1616, bound_value=120:117, second_product=240:2461, answer=228:24218)
- Layer 35: `120`, `119`, `121`, `分解`, `沛` (target ranks: base_value=52:14861, first_product=104:8243, bound_value=120:1, second_product=240:42, answer=228:53513)
- Layer 36: `120`, `119`, `第一百`, ` Wings`, `radesh` (target ranks: base_value=52:93030, first_product=104:22073, bound_value=120:1, second_product=240:32, answer=228:74542)
- Layer 37: `120`, `119`, `第一百`, ` Wings`, `七彩` (target ranks: base_value=52:123523, first_product=104:56638, bound_value=120:1, second_product=240:223, answer=228:121845)
- Layer 38: `120`, `119`, `七彩`, `zat`, `zyw` (target ranks: base_value=52:122740, first_product=104:62201, bound_value=120:1, second_product=240:1441, answer=228:124944)
- Layer 39: `120`, `�`, ` Jal`, `ozygous`, `东海` (target ranks: base_value=52:95585, first_product=104:84827, bound_value=120:1, second_product=240:13, answer=228:8647)
- Layer 40: `120`, `228`, `230`, `240`, `220` (target ranks: base_value=52:45136, first_product=104:66908, bound_value=120:1, second_product=240:4, answer=228:2)
- Layer 41: ` .`, `228`, `120`, ` twice`, `因为这些` (target ranks: base_value=52:12110, first_product=104:49677, bound_value=120:3, second_product=240:11, answer=228:2)

### Filler position 44 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127180, first_product=104:123646, bound_value=120:125324, second_product=240:126078, answer=228:125293)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:11329, first_product=104:30281, bound_value=120:22195, second_product=240:23573, answer=228:20614)
- Layer 20: `ait`, `锁定`, `能被`, `忑`, ` Walker` (target ranks: base_value=52:11956, first_product=104:31593, bound_value=120:23474, second_product=240:37089, answer=228:24909)
- Layer 30: `52`, ` fifty`, `coding`, ` forty`, `53` (target ranks: base_value=52:1, first_product=104:21299, bound_value=120:96342, second_product=240:120816, answer=228:62845)
- Layer 35: `52`, `51`, ` Dian`, `53`, ` Diet` (target ranks: base_value=52:1, first_product=104:16887, bound_value=120:96111, second_product=240:107802, answer=228:28292)
- Layer 36: `52`, `翻`, ` stabil`, ` mun`, `年开始` (target ranks: base_value=52:1, first_product=104:10262, bound_value=120:88111, second_product=240:107417, answer=228:28799)
- Layer 37: `52`, `}<?`, ` doubling`, `翻了`, `otan` (target ranks: base_value=52:1, first_product=104:32413, bound_value=120:107407, second_product=240:121413, answer=228:53652)
- Layer 38: `}<?`, `迷惑`, `lez`, `amina`, `izia` (target ranks: base_value=52:7, first_product=104:55787, bound_value=120:111937, second_product=240:125367, answer=228:77047)
- Layer 39: `迷惑`, `polar`, `无言`, `lez`, `}<?` (target ranks: base_value=52:2449, first_product=104:13309, bound_value=120:38592, second_product=240:12853, answer=228:253)
- Layer 40: `228`, `230`, `227`, `izk`, `220` (target ranks: base_value=52:2727, first_product=104:3920, bound_value=120:2455, second_product=240:28, answer=228:1)
- Layer 41: `228`, `227`, ` .`, `230`, `220` (target ranks: base_value=52:1363, first_product=104:4356, bound_value=120:906, second_product=240:47, answer=228:1)

### Filler position 45 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127308, first_product=104:123917, bound_value=120:125506, second_product=240:126171, answer=228:125425)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=52:10609, first_product=104:29043, bound_value=120:22010, second_product=240:22333, answer=228:19517)
- Layer 20: `ait`, ` Walker`, `妇`, `会成为`, ` engaging` (target ranks: base_value=52:17011, first_product=104:40955, bound_value=120:38476, second_product=240:52556, answer=228:33455)
- Layer 30: ` diz`, ` Dian`, ` Diam`, `acet`, `备` (target ranks: base_value=52:34185, first_product=104:89205, bound_value=120:112232, second_product=240:126866, answer=228:120290)
- Layer 35: ` diz`, ` Dian`, ` dich`, ` dy`, ` dio` (target ranks: base_value=52:10187, first_product=104:63230, bound_value=120:96811, second_product=240:119357, answer=228:92452)
- Layer 36: `留存`, ` diz`, ` Dian`, `otas`, `翻了` (target ranks: base_value=52:13666, first_product=104:26946, bound_value=120:59841, second_product=240:101005, answer=228:60359)
- Layer 37: `}<?`, `翻了`, ` diz`, `迷惑`, `acos` (target ranks: base_value=52:40751, first_product=104:48918, bound_value=120:83507, second_product=240:116491, answer=228:78609)
- Layer 38: `}<?`, `迷惑`, ` diz`, `zat`, `文字的` (target ranks: base_value=52:32063, first_product=104:55899, bound_value=120:84204, second_product=240:120000, answer=228:82018)
- Layer 39: `迷惑`, `文字的`, `无言`, `本题分析`, `东海` (target ranks: base_value=52:19894, first_product=104:29256, bound_value=120:50894, second_product=240:65481, answer=228:10291)
- Layer 40: ` Tw`, `留存`, `acular`, `等待着`, `无言` (target ranks: base_value=52:2198, first_product=104:10764, bound_value=120:19775, second_product=240:13601, answer=228:26)
- Layer 41: ` .`, `228`, ` `, `因为这些`, `227` (target ranks: base_value=52:72, first_product=104:3010, bound_value=120:3225, second_product=240:2490, answer=228:2)

### Filler position 46 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=52:127348, first_product=104:124201, bound_value=120:125783, second_product=240:126459, answer=228:125644)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=52:10319, first_product=104:28073, bound_value=120:22052, second_product=240:21514, answer=228:19354)
- Layer 20: ` spac`, `平行`, `俯`, ` adtong`, `ait` (target ranks: base_value=52:62804, first_product=104:93338, bound_value=120:92400, second_product=240:75063, answer=228:55355)
- Layer 30: ` spac`, `}using`, `坝`, `acos`, `?datasetId` (target ranks: base_value=52:103889, first_product=104:111832, bound_value=120:112057, second_product=240:123409, answer=228:81162)
- Layer 35: `}using`, `dividers`, `坏`, `俯`, `足足` (target ranks: base_value=52:68304, first_product=104:97490, bound_value=120:87299, second_product=240:125168, answer=228:61881)
- Layer 36: `俯`, `足足`, `ancock`, ` reduct`, ` dro` (target ranks: base_value=52:18174, first_product=104:52644, bound_value=120:46083, second_product=240:103561, answer=228:16305)
- Layer 37: `}<?`, `俯`, `放下`, `onana`, `放下了` (target ranks: base_value=52:75090, first_product=104:79428, bound_value=120:58234, second_product=240:107857, answer=228:59280)
- Layer 38: ` .`, ` nasod`, `俯`, `坏`, ` Wilson` (target ranks: base_value=52:30355, first_product=104:32848, bound_value=120:33775, second_product=240:94959, answer=228:38749)
- Layer 39: `hatic`, `oxygen`, `mac`, `�`, ` Latitude` (target ranks: base_value=52:36888, first_product=104:41321, bound_value=120:38321, second_product=240:36402, answer=228:5864)
- Layer 40: ` .`, ` x`, ` nasod`, `�`, ` baff` (target ranks: base_value=52:3159, first_product=104:9446, bound_value=120:5853, second_product=240:10814, answer=228:1098)
- Layer 41: ` .`, ` .↵↵`, ` `, ` ↵↵`, ` bears` (target ranks: base_value=52:2053, first_product=104:5925, bound_value=120:2398, second_product=240:3879, answer=228:43)

### Filler position 47 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=52:127243, first_product=104:124045, bound_value=120:125649, second_product=240:126341, answer=228:125551)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=52:10192, first_product=104:27789, bound_value=120:22115, second_product=240:21514, answer=228:19489)
- Layer 20: `}<?`, `东海`, `)Skip`, `ozygous`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=52:117248, first_product=104:124265, bound_value=120:96928, second_product=240:99719, answer=228:112006)
- Layer 30: `}<?`, `codeline`, `dividers`, `}using`, `?datasetId` (target ranks: base_value=52:109026, first_product=104:122075, bound_value=120:91890, second_product=240:121668, answer=228:89970)
- Layer 35: `codeline`, `ِّف`, `lett`, `dividers`, `浪费` (target ranks: base_value=52:109274, first_product=104:125460, bound_value=120:98579, second_product=240:127935, answer=228:102083)
- Layer 36: `足足`, `切割`, `锯`, `ancock`, ` nasod` (target ranks: base_value=52:70390, first_product=104:111006, bound_value=120:46486, second_product=240:119028, answer=228:56247)
- Layer 37: `الميل`, `磨损`, `}<?`, `东京`, `切割` (target ranks: base_value=52:105927, first_product=104:119394, bound_value=120:71603, second_product=240:112287, answer=228:61782)
- Layer 38: ` .`, `切割`, `遁`, ` prese`, `lett` (target ranks: base_value=52:57158, first_product=104:74387, bound_value=120:32483, second_product=240:106226, answer=228:48638)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` unflagged`, `�`, `lett` (target ranks: base_value=52:82183, first_product=104:76642, bound_value=120:27610, second_product=240:55654, answer=228:11229)
- Layer 40: ` .`, ` .↵↵`, `�`, ` nasod`, ` .↵` (target ranks: base_value=52:43023, first_product=104:36994, bound_value=120:4531, second_product=240:17578, answer=228:841)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: base_value=52:9908, first_product=104:10633, bound_value=120:1454, second_product=240:2034, answer=228:41)

### Filler position 48 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=52:127188, first_product=104:123727, bound_value=120:125473, second_product=240:126155, answer=228:125373)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=52:10200, first_product=104:28480, bound_value=120:22148, second_product=240:21718, answer=228:20124)
- Layer 20: `东海`, `}<?`, `aharoa`, ` instantaneous`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=52:101778, first_product=104:110407, bound_value=120:37867, second_product=240:76670, answer=228:100700)
- Layer 30: `codeline`, ` accompanying`, `lett`, `磨`, `东京` (target ranks: base_value=52:62413, first_product=104:107867, bound_value=120:28778, second_product=240:94349, answer=228:65689)
- Layer 35: `codeline`, `白雪`, ` doubly`, `AssemblyVersion`, ` fif` (target ranks: base_value=52:70353, first_product=104:124647, bound_value=120:36130, second_product=240:119598, answer=228:75382)
- Layer 36: ` Predict`, ` nasod`, ` reduct`, ` soci`, `yss` (target ranks: base_value=52:38951, first_product=104:103936, bound_value=120:14903, second_product=240:82594, answer=228:50147)
- Layer 37: `codeline`, `TreeLabel`, `镶嵌`, `Quintal`, `悬挂` (target ranks: base_value=52:100073, first_product=104:123097, bound_value=120:31804, second_product=240:96113, answer=228:83661)
- Layer 38: ` .`, ` crev`, ` germ`, `codeline`, `兑` (target ranks: base_value=52:57439, first_product=104:94624, bound_value=120:19369, second_product=240:89096, answer=228:90838)
- Layer 39: ` .`, ` .↵↵`, ` unflagged`, `贻`, ` germ` (target ranks: base_value=52:77483, first_product=104:94685, bound_value=120:23940, second_product=240:106870, answer=228:82600)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` unflagged` (target ranks: base_value=52:46832, first_product=104:58402, bound_value=120:7215, second_product=240:65489, answer=228:53094)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `圆圆`, `肤` (target ranks: base_value=52:4122, first_product=104:6503, bound_value=120:489, second_product=240:14254, answer=228:12201)

### Filler position 49 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=52:127239, first_product=104:123848, bound_value=120:125601, second_product=240:126227, answer=228:125449)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=52:10438, first_product=104:28879, bound_value=120:22376, second_product=240:21992, answer=228:20766)
- Layer 20: ` licensierad`, `aplenty`, `codeline`, ` instantaneous`, ` grounds` (target ranks: base_value=52:95057, first_product=104:98993, bound_value=120:69185, second_product=240:77765, answer=228:94798)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, ` Antwort` (target ranks: base_value=52:96972, first_product=104:115151, bound_value=120:86980, second_product=240:117516, answer=228:113561)
- Layer 35: ` Answer`, `codeline`, `AED`, `oNames`, ` Antwort` (target ranks: base_value=52:90709, first_product=104:107883, bound_value=120:53197, second_product=240:106443, answer=228:98378)
- Layer 36: ` Answer`, `坏`, `停`, `绽`, `醒` (target ranks: base_value=52:32002, first_product=104:66018, bound_value=120:19694, second_product=240:62094, answer=228:68335)
- Layer 37: `oNames`, `codeline`, `insic`, ` consum`, ` retard` (target ranks: base_value=52:79968, first_product=104:75078, bound_value=120:96968, second_product=240:114787, answer=228:103103)
- Layer 38: `oNames`, ` retard`, `оду`, `codeline`, `<|EOT|>` (target ranks: base_value=52:92445, first_product=104:80694, bound_value=120:86208, second_product=240:110127, answer=228:96003)
- Layer 39: `deen`, `�`, ` unflagged`, `oxygen`, ` Douglass` (target ranks: base_value=52:52061, first_product=104:64515, bound_value=120:85825, second_product=240:97549, answer=228:40770)
- Layer 40: ` .`, ` .↵↵`, ` wink`, ` nasod`, `esez` (target ranks: base_value=52:2532, first_product=104:16201, bound_value=120:28337, second_product=240:54800, answer=228:5866)
- Layer 41: ` .`, ` .↵↵`, `叮`, ` mister`, ` Answer` (target ranks: base_value=52:795, first_product=104:16401, bound_value=120:10725, second_product=240:20430, answer=228:842)

### Filler position 50 (absolute token 842, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=52:122100, first_product=104:109261, bound_value=120:112446, second_product=240:111115, answer=228:113487)
- Layer 10: `EDMF`, ` dével`, `�乐`, `-ulo`, `aplenty` (target ranks: base_value=52:125776, first_product=104:110749, bound_value=120:107735, second_product=240:100616, answer=228:110952)
- Layer 20: `答复`, `能被`, ` Submission`, `EDER`, `能得到` (target ranks: base_value=52:20700, first_product=104:57918, bound_value=120:29288, second_product=240:45104, answer=228:58178)
- Layer 30: `堂`, `lisitry`, ` Pole`, `malink`, `polar` (target ranks: base_value=52:30660, first_product=104:25906, bound_value=120:2123, second_product=240:13435, answer=228:11718)
- Layer 35: `240`, ` dunay`, `239`, `248`, `238` (target ranks: base_value=52:60235, first_product=104:55988, bound_value=120:40421, second_product=240:1, answer=228:25)
- Layer 36: `240`, `228`, `248`, ` talags`, `230` (target ranks: base_value=52:42478, first_product=104:88935, bound_value=120:3198, second_product=240:1, answer=228:2)
- Layer 37: `240`, `228`, `230`, `方针`, `248` (target ranks: base_value=52:106085, first_product=104:117930, bound_value=120:2629, second_product=240:1, answer=228:2)
- Layer 38: `228`, `248`, `240`, `238`, `239` (target ranks: base_value=52:116535, first_product=104:115339, bound_value=120:50622, second_product=240:3, answer=228:1)
- Layer 39: `228`, ` Paglin`, `malink`, `本题分析`, ` guarante` (target ranks: base_value=52:86758, first_product=104:120298, bound_value=120:93703, second_product=240:50, answer=228:1)
- Layer 40: `Answer`, ` Answer`, ` answer`, `_answer`, `答案` (target ranks: base_value=52:64472, first_product=104:96287, bound_value=120:34650, second_product=240:1041, answer=228:11)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=52:6603, first_product=104:44085, bound_value=120:8710, second_product=240:1289, answer=228:16)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>vub = 88
diz = 52
kod = twice the number for diz plus 11
zaf = twice the number for diz plus 16
xev = 97
Question: What is twice the number for zaf minus 12?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
