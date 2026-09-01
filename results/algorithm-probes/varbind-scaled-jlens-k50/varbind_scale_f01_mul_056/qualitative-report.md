# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `225` (correct).
- No-filler answer: `233` (incorrect).
- Filler tokens: 50 tokens at absolute indices 785–834.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=56` | 1 (L24, filler 15) | L23, filler 15 (rank 4) |
| J-Lens | `first_product=112` | 2 (L36, filler 15) | L35, filler 15 (rank 5) |
| J-Lens | `bound_value=120` | 1 (L35, filler 5) | L33, filler 28 (rank 7) |
| J-Lens | `second_product=240` | 1 (L31, filler 38) | L31, filler 1 (rank 5) |
| J-Lens | `answer=225` | 1 (L31, filler 36) | L31, filler 1 (rank 3) |
| Logit lens | `base_value=56` | 3 (L31, filler 43) | L25, filler 40 (rank 10) |
| Logit lens | `first_product=112` | 35 (L38, filler 44) | Never |
| Logit lens | `bound_value=120` | 1 (L35, filler 28) | L35, filler 8 (rank 6) |
| Logit lens | `second_product=240` | 1 (L35, filler 38) | L31, filler 1 (rank 3) |
| Logit lens | `answer=225` | 1 (L31, filler 1) | L30, filler 21 (rank 2) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 785, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=56:119047, first_product=112:110656, bound_value=120:111721, second_product=240:114761, answer=225:118184)
- Layer 10: `anta`, `hook`, `fine`, `Hook`, `咫` (target ranks: base_value=56:84982, first_product=112:92156, bound_value=120:64611, second_product=240:65762, answer=225:84123)
- Layer 20: `期望`, `足`, `重`, `期待`, ` Feldman` (target ranks: base_value=56:886, first_product=112:19943, bound_value=120:10167, second_product=240:8108, answer=225:16351)
- Layer 30: `65`, `69`, `sett`, ` Sett`, `93` (target ranks: base_value=56:340, first_product=112:5578, bound_value=120:1016, second_product=240:105, answer=225:91)
- Layer 35: `245`, `241`, `240`, `225`, `237` (target ranks: base_value=56:18219, first_product=112:59930, bound_value=120:78764, second_product=240:3, answer=225:4)
- Layer 36: `225`, `ppg`, `245`, `229`, `227` (target ranks: base_value=56:63522, first_product=112:115749, bound_value=120:115699, second_product=240:267, answer=225:1)
- Layer 37: `ppg`, `225`, ` unflagged`, `Kadaghanon`, ` Underground` (target ranks: base_value=56:108393, first_product=112:111047, bound_value=120:68296, second_product=240:389, answer=225:2)
- Layer 38: `225`, `245`, `ppg`, `235`, `227` (target ranks: base_value=56:128285, first_product=112:121725, bound_value=120:119166, second_product=240:828, answer=225:1)
- Layer 39: `225`, `227`, `229`, `-ulo`, `二百` (target ranks: base_value=56:127886, first_product=112:125060, bound_value=120:123651, second_product=240:15592, answer=225:1)
- Layer 40: `225`, ` talags`, `227`, `iap`, `实在` (target ranks: base_value=56:127250, first_product=112:124092, bound_value=120:103274, second_product=240:14776, answer=225:1)
- Layer 41: `225`, ` .`, `耘`, `他就是`, `以待` (target ranks: base_value=56:115984, first_product=112:111382, bound_value=120:104163, second_product=240:34394, answer=225:1)

### Filler position 2 (absolute token 786, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=56:121064, first_product=112:116874, bound_value=120:116711, second_product=240:120704, answer=225:122037)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=56:21175, first_product=112:40383, bound_value=120:31333, second_product=240:31594, answer=225:27163)
- Layer 20: ` .----`, `往常`, ` .`, `ozoic`, `ools` (target ranks: base_value=56:122760, first_product=112:125602, bound_value=120:128404, second_product=240:128469, answer=225:114447)
- Layer 30: ` talags`, ` pakig`, ` hilabihan`, ` gilay`, ` dekameters` (target ranks: base_value=56:118954, first_product=112:110900, bound_value=120:127910, second_product=240:129168, answer=225:100024)
- Layer 35: ` hilabihan`, ` pakig`, ` talags`, ` gilay`, `滴水` (target ranks: base_value=56:125673, first_product=112:105619, bound_value=120:127731, second_product=240:128936, answer=225:114443)
- Layer 36: ` talags`, ` hilabihan`, `enclose`, `空空`, `停` (target ranks: base_value=56:97060, first_product=112:73168, bound_value=120:115696, second_product=240:127114, answer=225:67884)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, ` licensierad`, `�乐` (target ranks: base_value=56:123301, first_product=112:104875, bound_value=120:124709, second_product=240:128562, answer=225:115461)
- Layer 38: ` .`, ` Erkännande`, ` .↵↵`, ` nasod`, `用了` (target ranks: base_value=56:101956, first_product=112:84136, bound_value=120:111303, second_product=240:126647, answer=225:75985)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` nasod`, ` hilabihan` (target ranks: base_value=56:77762, first_product=112:91466, bound_value=120:85517, second_product=240:120060, answer=225:64352)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, ` filler` (target ranks: base_value=56:35149, first_product=112:51003, bound_value=120:25683, second_product=240:84519, answer=225:10759)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` 。` (target ranks: base_value=56:5531, first_product=112:13029, bound_value=120:6296, second_product=240:16524, answer=225:876)

### Filler position 3 (absolute token 787, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:125022, first_product=112:120214, bound_value=120:119982, second_product=240:123017, answer=225:123978)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=56:18409, first_product=112:30543, bound_value=120:28887, second_product=240:29641, answer=225:22802)
- Layer 20: `ait`, `能被`, ` ternary`, `�`, `忑` (target ranks: base_value=56:12350, first_product=112:47735, bound_value=120:38123, second_product=240:58448, answer=225:27101)
- Layer 30: `计算的`, `进行计算`, `calcul`, `算出`, `计算` (target ranks: base_value=56:20737, first_product=112:50124, bound_value=120:84349, second_product=240:101817, answer=225:41753)
- Layer 35: `calcul`, `计算的`, `计算`, ` calculations`, `进行计算` (target ranks: base_value=56:14168, first_product=112:37419, bound_value=120:87299, second_product=240:82026, answer=225:20393)
- Layer 36: `calcul`, `计算的`, `定义的`, `计算`, ` definitions` (target ranks: base_value=56:21152, first_product=112:49181, bound_value=120:90315, second_product=240:86997, answer=225:17886)
- Layer 37: ` cál`, `定义`, `Mul`, `mul`, ` mul` (target ranks: base_value=56:55057, first_product=112:75615, bound_value=120:114113, second_product=240:115919, answer=225:46287)
- Layer 38: ` Mul`, `Mul`, `oses`, `mul`, ` cál` (target ranks: base_value=56:73698, first_product=112:96365, bound_value=120:115024, second_product=240:119301, answer=225:78174)
- Layer 39: ` Mul`, `oses`, ` Noruwega`, `mul`, `Mul` (target ranks: base_value=56:69408, first_product=112:109311, bound_value=120:120303, second_product=240:122915, answer=225:77882)
- Layer 40: ` mul`, `mul`, `Mul`, ` Mul`, ` c` (target ranks: base_value=56:18239, first_product=112:67310, bound_value=120:86481, second_product=240:111589, answer=225:17049)
- Layer 41: ` .`, `试一试`, ` ,`, `不急`, `<｜end▁of▁sentence｜>` (target ranks: base_value=56:2132, first_product=112:52276, bound_value=120:48032, second_product=240:82389, answer=225:6765)

### Filler position 4 (absolute token 788, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:125383, first_product=112:121262, bound_value=120:121197, second_product=240:123944, answer=225:125083)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=56:13800, first_product=112:27317, bound_value=120:24412, second_product=240:23902, answer=225:19211)
- Layer 20: `ait`, `幽`, `cape`, ` quadr`, `足` (target ranks: base_value=56:11460, first_product=112:43643, bound_value=120:64180, second_product=240:68378, answer=225:45253)
- Layer 30: ` dripping`, `anic`, `expected`, `表现的`, `考的` (target ranks: base_value=56:187, first_product=112:5264, bound_value=120:28025, second_product=240:57355, answer=225:23732)
- Layer 35: `舍弃`, `放弃`, `鞍`, `高空`, ` Niagara` (target ranks: base_value=56:4724, first_product=112:3856, bound_value=120:12564, second_product=240:17294, answer=225:105)
- Layer 36: ` Gelijk`, `radesh`, ` spectator`, `SPJ`, `放下` (target ranks: base_value=56:54094, first_product=112:4010, bound_value=120:17497, second_product=240:67981, answer=225:1757)
- Layer 37: ` Gelijk`, ` spectator`, `lez`, `hatic`, `?datasetId` (target ranks: base_value=56:96192, first_product=112:6213, bound_value=120:997, second_product=240:39015, answer=225:18723)
- Layer 38: ` Gelijk`, `125`, ` spectator`, `127`, `osz` (target ranks: base_value=56:121218, first_product=112:402, bound_value=120:414, second_product=240:76674, answer=225:744)
- Layer 39: `225`, `opters`, `227`, `osz`, ` tons` (target ranks: base_value=56:127069, first_product=112:19801, bound_value=120:97427, second_product=240:74992, answer=225:1)
- Layer 40: `225`, `227`, ` tons`, `舍弃`, `Ald` (target ranks: base_value=56:127503, first_product=112:8490, bound_value=120:51876, second_product=240:17313, answer=225:1)
- Layer 41: ` .`, `225`, `样子`, `*....|`, `总支` (target ranks: base_value=56:119130, first_product=112:48312, bound_value=120:79935, second_product=240:56597, answer=225:2)

### Filler position 5 (absolute token 789, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:124869, first_product=112:121060, bound_value=120:121006, second_product=240:123719, answer=225:125274)
- Layer 10: ` Walker`, `Walker`, `锁定`, `挪`, `ait` (target ranks: base_value=56:14587, first_product=112:29092, bound_value=120:25950, second_product=240:25106, answer=225:21073)
- Layer 20: `幽`, ` LS`, `能被`, `鞍`, `啦啦` (target ranks: base_value=56:16630, first_product=112:23693, bound_value=120:50908, second_product=240:48709, answer=225:21842)
- Layer 30: `鞍`, `乘`, `多少次`, `Tail`, `粥` (target ranks: base_value=56:143, first_product=112:3881, bound_value=120:7606, second_product=240:17670, answer=225:46802)
- Layer 35: `120`, `六十`, ` Kaw`, `�`, `鞍` (target ranks: base_value=56:3289, first_product=112:7485, bound_value=120:1, second_product=240:1722, answer=225:46960)
- Layer 36: `120`, `radesh`, `支持`, `ppg`, `期望` (target ranks: base_value=56:34665, first_product=112:34389, bound_value=120:1, second_product=240:2699, answer=225:54193)
- Layer 37: `}<?`, `120`, `radesh`, `ppg`, `igit` (target ranks: base_value=56:54385, first_product=112:34880, bound_value=120:2, second_product=240:15633, answer=225:88937)
- Layer 38: `}<?`, `120`, `ocyst`, `radesh`, `ivit` (target ranks: base_value=56:84104, first_product=112:51980, bound_value=120:2, second_product=240:34007, answer=225:101998)
- Layer 39: `}<?`, ` Fif`, `东海`, `hemer`, `叶子` (target ranks: base_value=56:63081, first_product=112:98064, bound_value=120:1078, second_product=240:95733, answer=225:84666)
- Layer 40: `实在`, `igit`, `叮`, `俯`, `翻` (target ranks: base_value=56:60187, first_product=112:55360, bound_value=120:63, second_product=240:47661, answer=225:13727)
- Layer 41: ` .`, `实在`, `叮`, `*....|`, ` ;` (target ranks: base_value=56:46342, first_product=112:66008, bound_value=120:190, second_product=240:56244, answer=225:11122)

### Filler position 6 (absolute token 790, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:124499, first_product=112:120758, bound_value=120:120586, second_product=240:123163, answer=225:125178)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:13477, first_product=112:26203, bound_value=120:25163, second_product=240:23420, answer=225:19033)
- Layer 20: ` calculator`, ` answer`, `�`, `答案`, `calculator` (target ranks: base_value=56:35706, first_product=112:71331, bound_value=120:48319, second_product=240:45469, answer=225:30423)
- Layer 30: ` Tw`, `算出`, `计算的`, ` twice`, `进行计算` (target ranks: base_value=56:20989, first_product=112:29164, bound_value=120:8190, second_product=240:46544, answer=225:25130)
- Layer 35: ` Tw`, `Tw`, `第一步`, ` calculator`, `tw` (target ranks: base_value=56:9415, first_product=112:19744, bound_value=120:7695, second_product=240:27717, answer=225:11458)
- Layer 36: ` Tw`, `Tw`, `calcul`, ` tw`, `计算的` (target ranks: base_value=56:12588, first_product=112:14626, bound_value=120:5129, second_product=240:26087, answer=225:7029)
- Layer 37: ` Tw`, `计算`, `计算的`, `calcul`, ` calculation` (target ranks: base_value=56:16704, first_product=112:12242, bound_value=120:4995, second_product=240:42326, answer=225:11045)
- Layer 38: ` Tw`, `计算`, `计算的`, ` Calculators`, `calcul` (target ranks: base_value=56:24427, first_product=112:12205, bound_value=120:3150, second_product=240:38748, answer=225:12837)
- Layer 39: ` Tw`, ` nasod`, ` Fif`, `<｜begin▁of▁sentence｜>`, ` TW` (target ranks: base_value=56:73807, first_product=112:106384, bound_value=120:104577, second_product=240:127875, answer=225:101571)
- Layer 40: ` c`, ` talags`, ` nasod`, ` C`, `mul` (target ranks: base_value=56:36642, first_product=112:100157, bound_value=120:81455, second_product=240:126773, answer=225:71837)
- Layer 41: ` .`, `鹃`, `圆圆`, `criptor`, `试一试` (target ranks: base_value=56:44265, first_product=112:101946, bound_value=120:74891, second_product=240:125404, answer=225:63121)

### Filler position 7 (absolute token 791, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124412, first_product=112:120391, bound_value=120:120051, second_product=240:122710, answer=225:124891)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=56:13534, first_product=112:26147, bound_value=120:24416, second_product=240:22962, answer=225:18735)
- Layer 20: `能被`, `us`, `ait`, ` Walker`, ` calculator` (target ranks: base_value=56:9350, first_product=112:34606, bound_value=120:35442, second_product=240:42540, answer=225:26290)
- Layer 30: `算出`, ` Tw`, `计算的`, `计算`, `第一步` (target ranks: base_value=56:10393, first_product=112:34906, bound_value=120:86503, second_product=240:86329, answer=225:56148)
- Layer 35: ` Tw`, `Tw`, `第一步`, `tw`, `.tw` (target ranks: base_value=56:5254, first_product=112:27654, bound_value=120:63639, second_product=240:70678, answer=225:20557)
- Layer 36: ` Tw`, `Tw`, `calcul`, `第一步`, `.tw` (target ranks: base_value=56:10759, first_product=112:23510, bound_value=120:59461, second_product=240:69510, answer=225:17225)
- Layer 37: `calcul`, ` mul`, `计算`, `Mul`, `计算的` (target ranks: base_value=56:19887, first_product=112:24816, bound_value=120:78640, second_product=240:98677, answer=225:35444)
- Layer 38: ` mul`, ` Mul`, `Mul`, `mul`, `calcul` (target ranks: base_value=56:40945, first_product=112:50482, bound_value=120:84899, second_product=240:110109, answer=225:63728)
- Layer 39: ` Mul`, ` mul`, `mul`, `Mul`, `script` (target ranks: base_value=56:52029, first_product=112:93347, bound_value=120:116818, second_product=240:125521, answer=225:94666)
- Layer 40: ` c`, `留存`, `scr`, `duc`, `acl` (target ranks: base_value=56:12891, first_product=112:68876, bound_value=120:89802, second_product=240:117589, answer=225:42110)
- Layer 41: ` .`, `试一试`, `鹉`, `acular`, `留存` (target ranks: base_value=56:2431, first_product=112:40463, bound_value=120:40620, second_product=240:85036, answer=225:16328)

### Filler position 8 (absolute token 792, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124392, first_product=112:120240, bound_value=120:119812, second_product=240:122444, answer=225:124684)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11660, first_product=112:24968, bound_value=120:22934, second_product=240:22757, answer=225:18372)
- Layer 20: ` Walker`, `能被`, `锁定`, `Walker`, `挪` (target ranks: base_value=56:5919, first_product=112:24293, bound_value=120:27715, second_product=240:28693, answer=225:15267)
- Layer 30: `鞍`, `往外`, `期望`, `六十`, `atar` (target ranks: base_value=56:16, first_product=112:5439, bound_value=120:1349, second_product=240:17343, answer=225:40248)
- Layer 35: `120`, `六十`, `鞍`, `分解`, ` sixty` (target ranks: base_value=56:311, first_product=112:1349, bound_value=120:1, second_product=240:3733, answer=225:38142)
- Layer 36: `120`, ` Wil`, `radesh`, ` sag`, `支持` (target ranks: base_value=56:7268, first_product=112:16464, bound_value=120:1, second_product=240:5595, answer=225:67689)
- Layer 37: `120`, `}<?`, `radesh`, `ascals`, `陪` (target ranks: base_value=56:22335, first_product=112:26037, bound_value=120:1, second_product=240:24058, answer=225:107129)
- Layer 38: `120`, `}<?`, `radesh`, `osit`, `igit` (target ranks: base_value=56:57729, first_product=112:48497, bound_value=120:1, second_product=240:47275, answer=225:118371)
- Layer 39: `}<?`, `ozygous`, `osit`, ` Fif`, `东海` (target ranks: base_value=56:64193, first_product=112:100713, bound_value=120:130, second_product=240:101705, answer=225:103873)
- Layer 40: `实在`, `osit`, `radesh`, `igit`, `scr` (target ranks: base_value=56:52150, first_product=112:64205, bound_value=120:6, second_product=240:51299, answer=225:21296)
- Layer 41: ` .`, `实在`, `袄`, `有两种`, `叮` (target ranks: base_value=56:26475, first_product=112:72544, bound_value=120:13, second_product=240:35681, answer=225:9489)

### Filler position 9 (absolute token 793, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124499, first_product=112:120588, bound_value=120:120148, second_product=240:122715, answer=225:124932)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:12100, first_product=112:26265, bound_value=120:23837, second_product=240:24109, answer=225:19308)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, `Walker` (target ranks: base_value=56:9573, first_product=112:24998, bound_value=120:38300, second_product=240:45148, answer=225:20338)
- Layer 30: `Mul`, ` mul`, `mul`, `acos`, ` c` (target ranks: base_value=56:10381, first_product=112:34239, bound_value=120:122212, second_product=240:120710, answer=225:52351)
- Layer 35: ` c`, ` mul`, `acin`, `acos`, `acks` (target ranks: base_value=56:11007, first_product=112:27918, bound_value=120:116457, second_product=240:114837, answer=225:36055)
- Layer 36: ` mul`, `Mul`, `acl`, `留存`, `acos` (target ranks: base_value=56:20073, first_product=112:16933, bound_value=120:109726, second_product=240:105387, answer=225:21708)
- Layer 37: ` mul`, `Mul`, `mul`, ` Mul`, `acos` (target ranks: base_value=56:37923, first_product=112:21157, bound_value=120:119070, second_product=240:118417, answer=225:45748)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=56:47224, first_product=112:34341, bound_value=120:117335, second_product=240:121441, answer=225:60314)
- Layer 39: ` Mul`, ` mul`, `mul`, `Mul`, `}<?` (target ranks: base_value=56:57981, first_product=112:59972, bound_value=120:120436, second_product=240:124338, answer=225:75526)
- Layer 40: ` mul`, `mul`, `acl`, `Mul`, ` Mul` (target ranks: base_value=56:11745, first_product=112:17641, bound_value=120:91469, second_product=240:118761, answer=225:26119)
- Layer 41: ` mul`, `鹉`, ` .`, `acular`, `acl` (target ranks: base_value=56:1331, first_product=112:11011, bound_value=120:34712, second_product=240:98295, answer=225:6729)

### Filler position 10 (absolute token 794, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124352, first_product=112:120506, bound_value=120:120057, second_product=240:122634, answer=225:124946)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:12156, first_product=112:26690, bound_value=120:23502, second_product=240:23396, answer=225:19455)
- Layer 20: `ait`, `锁定`, ` smile`, `cape`, `幽` (target ranks: base_value=56:8118, first_product=112:21738, bound_value=120:30198, second_product=240:30673, answer=225:16658)
- Layer 30: `鞍`, ` calculator`, ` calculate`, `calcul`, `Tap` (target ranks: base_value=56:2369, first_product=112:7679, bound_value=120:20146, second_product=240:26645, answer=225:9929)
- Layer 35: ` calculator`, `calcul`, ` tap`, `锁定`, `Tap` (target ranks: base_value=56:1185, first_product=112:5698, bound_value=120:15201, second_product=240:21739, answer=225:3944)
- Layer 36: `calcul`, `acin`, ` tap`, ` stabil`, `冰冰` (target ranks: base_value=56:3910, first_product=112:7150, bound_value=120:13892, second_product=240:27891, answer=225:2407)
- Layer 37: `calcul`, `冰冰`, `anium`, `}<?`, `不急` (target ranks: base_value=56:11491, first_product=112:5472, bound_value=120:20765, second_product=240:50022, answer=225:3309)
- Layer 38: `}<?`, `冰冰`, `calcul`, `不急`, `筋` (target ranks: base_value=56:25113, first_product=112:9475, bound_value=120:21986, second_product=240:57024, answer=225:3679)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ocyst`, `筋`, `osit` (target ranks: base_value=56:98434, first_product=112:92161, bound_value=120:55302, second_product=240:106761, answer=225:27150)
- Layer 40: ` Res`, `acl`, `radesh`, `不急`, `留存` (target ranks: base_value=56:74935, first_product=112:69707, bound_value=120:23285, second_product=240:73759, answer=225:683)
- Layer 41: ` .`, `鹉`, ` just`, ` `, `留存` (target ranks: base_value=56:23320, first_product=112:33289, bound_value=120:2980, second_product=240:26012, answer=225:86)

### Filler position 11 (absolute token 795, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124429, first_product=112:120750, bound_value=120:120291, second_product=240:122850, answer=225:125144)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11972, first_product=112:26302, bound_value=120:22608, second_product=240:22779, answer=225:18759)
- Layer 20: `能被`, `啦啦`, `幽`, `ait`, `距` (target ranks: base_value=56:7172, first_product=112:29289, bound_value=120:36135, second_product=240:35066, answer=225:14076)
- Layer 30: `65`, `essa`, ` backward`, `笑笑`, `松动` (target ranks: base_value=56:3229, first_product=112:28576, bound_value=120:21183, second_product=240:6875, answer=225:18)
- Layer 35: `225`, `245`, `正气`, `585`, `185` (target ranks: base_value=56:21305, first_product=112:60579, bound_value=120:109762, second_product=240:259, answer=225:1)
- Layer 36: `225`, `Kadaghanon`, `}<?`, `105`, `正气` (target ranks: base_value=56:89973, first_product=112:106083, bound_value=120:122143, second_product=240:13083, answer=225:1)
- Layer 37: `}<?`, `225`, `Kadaghanon`, ` Gelijk`, `?datasetId` (target ranks: base_value=56:118375, first_product=112:96891, bound_value=120:70155, second_product=240:3663, answer=225:2)
- Layer 38: `225`, `}<?`, `acons`, `ppg`, `离开了` (target ranks: base_value=56:129061, first_product=112:120094, bound_value=120:113544, second_product=240:3328, answer=225:1)
- Layer 39: `225`, `}<?`, `二百`, `本题分析`, `-ulo` (target ranks: base_value=56:128228, first_product=112:127042, bound_value=120:123467, second_product=240:3978, answer=225:1)
- Layer 40: `225`, ` kinahabogang`, `}<?`, ` talags`, ` prime` (target ranks: base_value=56:127108, first_product=112:121950, bound_value=120:76068, second_product=240:877, answer=225:1)
- Layer 41: `225`, ` nuest`, `))))`, ` mediabestanden`, `溉` (target ranks: base_value=56:117909, first_product=112:116565, bound_value=120:68164, second_product=240:10431, answer=225:1)

### Filler position 12 (absolute token 796, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124373, first_product=112:120892, bound_value=120:120414, second_product=240:122909, answer=225:125276)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11445, first_product=112:25394, bound_value=120:22790, second_product=240:22408, answer=225:18576)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, ` wig` (target ranks: base_value=56:12218, first_product=112:34905, bound_value=120:45201, second_product=240:49560, answer=225:30164)
- Layer 30: `Tap`, ` tap`, ` Tap`, `acos`, `tap` (target ranks: base_value=56:14653, first_product=112:66608, bound_value=120:119764, second_product=240:107535, answer=225:63228)
- Layer 35: ` tap`, `Tap`, ` Tap`, ` rip`, ` met` (target ranks: base_value=56:21446, first_product=112:66099, bound_value=120:121913, second_product=240:109519, answer=225:56237)
- Layer 36: ` tap`, ` rip`, ` riv`, `acin`, `Tap` (target ranks: base_value=56:17054, first_product=112:48540, bound_value=120:101446, second_product=240:83376, answer=225:31816)
- Layer 37: `acos`, ` rip`, ` Zad`, ` talags`, ` dynam` (target ranks: base_value=56:34476, first_product=112:66477, bound_value=120:117425, second_product=240:111682, answer=225:73011)
- Layer 38: `}<?`, `zat`, `�`, ` zaz`, `aje` (target ranks: base_value=56:63738, first_product=112:86220, bound_value=120:120043, second_product=240:119137, answer=225:91875)
- Layer 39: `zat`, `�`, `}<?`, `zam`, `-ulo` (target ranks: base_value=56:85640, first_product=112:95325, bound_value=120:119388, second_product=240:114579, answer=225:61102)
- Layer 40: ` talags`, `zel`, `zat`, `zal`, ` fum` (target ranks: base_value=56:51545, first_product=112:67098, bound_value=120:100891, second_product=240:97317, answer=225:6093)
- Layer 41: ` .`, `鹉`, ` fum`, `吾尔`, `zel` (target ranks: base_value=56:6543, first_product=112:17050, bound_value=120:23575, second_product=240:22030, answer=225:26)

### Filler position 13 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124411, first_product=112:120845, bound_value=120:120319, second_product=240:122811, answer=225:125180)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11891, first_product=112:26076, bound_value=120:23342, second_product=240:22979, answer=225:18739)
- Layer 20: `锁定`, `ait`, ` Walker`, ` smile`, `能被` (target ranks: base_value=56:11548, first_product=112:33875, bound_value=120:46118, second_product=240:44063, answer=225:20404)
- Layer 30: ` tap`, `Tap`, `acin`, `退出`, `笑笑` (target ranks: base_value=56:1117, first_product=112:13973, bound_value=120:53095, second_product=240:32119, answer=225:82)
- Layer 35: `225`, `退出`, `acin`, `adal`, `ilig` (target ranks: base_value=56:10066, first_product=112:14436, bound_value=120:114241, second_product=240:9028, answer=225:1)
- Layer 36: `225`, `}<?`, `acin`, `ilig`, `Kadaghanon` (target ranks: base_value=56:47903, first_product=112:32902, bound_value=120:125445, second_product=240:21983, answer=225:1)
- Layer 37: `}<?`, `polar`, `?datasetId`, `ppg`, `225` (target ranks: base_value=56:100092, first_product=112:46807, bound_value=120:113379, second_product=240:10853, answer=225:5)
- Layer 38: `}<?`, `225`, `?datasetId`, `polar`, `acons` (target ranks: base_value=56:127243, first_product=112:87656, bound_value=120:126109, second_product=240:22697, answer=225:2)
- Layer 39: `}<?`, `ocyst`, `acons`, `-ulo`, `polar` (target ranks: base_value=56:126476, first_product=112:114667, bound_value=120:123487, second_product=240:36338, answer=225:6)
- Layer 40: ` talags`, `225`, `判`, ` pakig`, `acl` (target ranks: base_value=56:115729, first_product=112:89667, bound_value=120:104392, second_product=240:7662, answer=225:2)
- Layer 41: ` .`, `225`, `判`, `鹉`, `笔者认为` (target ranks: base_value=56:77465, first_product=112:66316, bound_value=120:86261, second_product=240:12883, answer=225:2)

### Filler position 14 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124724, first_product=112:121281, bound_value=120:120649, second_product=240:123008, answer=225:125316)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11015, first_product=112:24866, bound_value=120:22048, second_product=240:21989, answer=225:17646)
- Layer 20: ` Walker`, `ait`, `能被`, `锁定`, `Walker` (target ranks: base_value=56:10272, first_product=112:28022, bound_value=120:50915, second_product=240:43941, answer=225:19137)
- Layer 30: `acos`, ` pakig`, ` August`, `acin`, `鞍` (target ranks: base_value=56:746, first_product=112:9144, bound_value=120:45978, second_product=240:62758, answer=225:41432)
- Layer 35: `acos`, ` August`, `冰冰`, `川`, ` expecting` (target ranks: base_value=56:180, first_product=112:805, bound_value=120:2677, second_product=240:22341, answer=225:9265)
- Layer 36: `翻`, `radesh`, `期望`, `期盼`, `放大` (target ranks: base_value=56:1442, first_product=112:3422, bound_value=120:2592, second_product=240:23170, answer=225:8372)
- Layer 37: `}<?`, `ascals`, `牺牲`, `参赛`, `放下` (target ranks: base_value=56:21758, first_product=112:12053, bound_value=120:25409, second_product=240:81082, answer=225:44974)
- Layer 38: `}<?`, `ocyst`, `oxygen`, `osit`, `fluoro` (target ranks: base_value=56:44201, first_product=112:27706, bound_value=120:38254, second_product=240:97822, answer=225:62613)
- Layer 39: `}<?`, `ocyst`, `oxygen`, `hemer`, `ozygous` (target ranks: base_value=56:41590, first_product=112:41862, bound_value=120:17184, second_product=240:101895, answer=225:58705)
- Layer 40: `scr`, ` Tw`, `}<?`, `enclose`, `留存` (target ranks: base_value=56:6279, first_product=112:6627, bound_value=120:394, second_product=240:55551, answer=225:3055)
- Layer 41: ` .`, ` .↵↵`, ` ;`, ` because`, `<｜end▁of▁sentence｜>` (target ranks: base_value=56:4391, first_product=112:4559, bound_value=120:250, second_product=240:18638, answer=225:408)

### Filler position 15 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124785, first_product=112:121459, bound_value=120:120850, second_product=240:123194, answer=225:125427)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10687, first_product=112:24250, bound_value=120:21826, second_product=240:21379, answer=225:17050)
- Layer 20: `ait`, `锁定`, `能被`, `距`, ` Walker` (target ranks: base_value=56:4798, first_product=112:23953, bound_value=120:31423, second_product=240:30020, answer=225:14572)
- Layer 30: `56`, `acos`, `分解`, `平行`, `粥` (target ranks: base_value=56:1, first_product=112:1817, bound_value=120:55318, second_product=240:85247, answer=225:50379)
- Layer 35: ` twice`, `56`, `分解`, `116`, `112` (target ranks: base_value=56:2, first_product=112:5, bound_value=120:2206, second_product=240:72679, answer=225:20390)
- Layer 36: `116`, `112`, `radesh`, `分解`, ` multipliers` (target ranks: base_value=56:8, first_product=112:2, bound_value=120:2821, second_product=240:75468, answer=225:16761)
- Layer 37: `}<?`, `凌霄`, ` doubled`, ` doubles`, ` doubling` (target ranks: base_value=56:55, first_product=112:19, bound_value=120:8699, second_product=240:108404, answer=225:47264)
- Layer 38: `}<?`, `ocyst`, `凌霄`, `ounder`, ` doubled` (target ranks: base_value=56:571, first_product=112:125, bound_value=120:20933, second_product=240:114826, answer=225:63933)
- Layer 39: `}<?`, `ounder`, `ocyst`, `hemer`, `替换` (target ranks: base_value=56:2066, first_product=112:7649, bound_value=120:80418, second_product=240:114484, answer=225:71752)
- Layer 40: ` mul`, ` Mul`, `Mul`, `mul`, `anic` (target ranks: base_value=56:1932, first_product=112:2048, bound_value=120:12763, second_product=240:29441, answer=225:302)
- Layer 41: ` .`, ` `, `转载请`, ` multiplier`, `<｜end▁of▁sentence｜>` (target ranks: base_value=56:1148, first_product=112:3963, bound_value=120:14401, second_product=240:21787, answer=225:153)

### Filler position 16 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125191, first_product=112:122153, bound_value=120:121546, second_product=240:123663, answer=225:125817)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11115, first_product=112:25570, bound_value=120:22802, second_product=240:21875, answer=225:18243)
- Layer 20: `ait`, `锁定`, `幽`, `能被`, ` smile` (target ranks: base_value=56:6418, first_product=112:29200, bound_value=120:37932, second_product=240:33801, answer=225:20542)
- Layer 30: ` ignoring`, `忽略`, ` ignore`, ` ignored`, `Ign` (target ranks: base_value=56:2860, first_product=112:37730, bound_value=120:80207, second_product=240:76319, answer=225:15492)
- Layer 35: ` ignoring`, `忽略`, ` ignore`, ` Ign`, ` calculate` (target ranks: base_value=56:5676, first_product=112:28298, bound_value=120:80059, second_product=240:72766, answer=225:26719)
- Layer 36: `忽略`, `感兴趣的`, `感兴趣`, `calcul`, ` ignoring` (target ranks: base_value=56:5303, first_product=112:15838, bound_value=120:56321, second_product=240:54580, answer=225:11554)
- Layer 37: `acos`, `calcul`, `relevant`, `忽略`, `不急` (target ranks: base_value=56:15890, first_product=112:32954, bound_value=120:103522, second_product=240:103915, answer=225:35764)
- Layer 38: `relevant`, ` Relevant`, `不急`, `referent`, `�` (target ranks: base_value=56:28795, first_product=112:46462, bound_value=120:105721, second_product=240:114804, answer=225:48385)
- Layer 39: `<｜begin▁of▁sentence｜>`, `referent`, ` Relevant`, `殿堂`, `relevant` (target ranks: base_value=56:36972, first_product=112:80401, bound_value=120:105596, second_product=240:124094, answer=225:75220)
- Layer 40: ` Relevant`, `acl`, ` mul`, `mul`, `步骤如下` (target ranks: base_value=56:4821, first_product=112:37994, bound_value=120:66229, second_product=240:118332, answer=225:29778)
- Layer 41: ` .`, `步骤如下`, ` necessary`, `上证`, ` because` (target ranks: base_value=56:90, first_product=112:18593, bound_value=120:28207, second_product=240:103390, answer=225:8128)

### Filler position 17 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125337, first_product=112:122409, bound_value=120:121910, second_product=240:123922, answer=225:126082)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11373, first_product=112:25844, bound_value=120:23677, second_product=240:22666, answer=225:18922)
- Layer 20: ` smile`, `锁定`, `能被`, `距`, `而此时` (target ranks: base_value=56:9304, first_product=112:27291, bound_value=120:43840, second_product=240:39448, answer=225:18694)
- Layer 30: ` twice`, ` multipliers`, `反复`, ` c`, ` EC` (target ranks: base_value=56:2183, first_product=112:22610, bound_value=120:89706, second_product=240:68608, answer=225:40664)
- Layer 35: ` c`, ` Tw`, ` twice`, `c`, `Tw` (target ranks: base_value=56:3516, first_product=112:31259, bound_value=120:89872, second_product=240:75901, answer=225:34957)
- Layer 36: ` c`, ` twice`, ` EC`, ` multipliers`, ` Tw` (target ranks: base_value=56:5918, first_product=112:28604, bound_value=120:89183, second_product=240:73927, answer=225:23824)
- Layer 37: `niz`, ` doubling`, `mul`, `Mul`, ` mul` (target ranks: base_value=56:19929, first_product=112:32000, bound_value=120:95400, second_product=240:84933, answer=225:44873)
- Layer 38: `zat`, `niz`, `Mul`, `mul`, ` Mul` (target ranks: base_value=56:24615, first_product=112:35946, bound_value=120:74425, second_product=240:83604, answer=225:45439)
- Layer 39: ` Mul`, `mul`, ` mul`, `覆`, `Mul` (target ranks: base_value=56:48551, first_product=112:69702, bound_value=120:97503, second_product=240:119468, answer=225:88336)
- Layer 40: ` mul`, `坏`, `mul`, ` c`, ` Mul` (target ranks: base_value=56:9143, first_product=112:23233, bound_value=120:44102, second_product=240:101275, answer=225:29229)
- Layer 41: ` .`, `坏`, ` multipliers`, `czenie`, `less` (target ranks: base_value=56:868, first_product=112:21640, bound_value=120:16758, second_product=240:76825, answer=225:16491)

### Filler position 18 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:125347, first_product=112:122740, bound_value=120:122216, second_product=240:124300, answer=225:126320)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10633, first_product=112:25293, bound_value=120:23561, second_product=240:22974, answer=225:18533)
- Layer 20: ` Walker`, `ait`, `锁定`, `忑`, `Walker` (target ranks: base_value=56:13153, first_product=112:43628, bound_value=120:47512, second_product=240:54635, answer=225:31722)
- Layer 30: `Mul`, ` mul`, `mul`, ` Mul`, ` Mull` (target ranks: base_value=56:1962, first_product=112:46482, bound_value=120:120639, second_product=240:114634, answer=225:41317)
- Layer 35: ` mul`, `Mul`, `mul`, ` Mul`, ` Mull` (target ranks: base_value=56:1233, first_product=112:46825, bound_value=120:112755, second_product=240:100755, answer=225:22062)
- Layer 36: ` mul`, `Mul`, `mul`, ` Mul`, ` Mull` (target ranks: base_value=56:4487, first_product=112:47048, bound_value=120:106282, second_product=240:95936, answer=225:17019)
- Layer 37: ` mul`, ` Mul`, `mul`, `Mul`, `}<?` (target ranks: base_value=56:20056, first_product=112:61685, bound_value=120:117736, second_product=240:117834, answer=225:39390)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=56:28727, first_product=112:72362, bound_value=120:111569, second_product=240:119232, answer=225:58378)
- Layer 39: ` mul`, ` Mul`, `mul`, `Mul`, `}<?` (target ranks: base_value=56:59960, first_product=112:92321, bound_value=120:117911, second_product=240:123569, answer=225:78819)
- Layer 40: ` mul`, `mul`, ` Mul`, `Mul`, ` multiplier` (target ranks: base_value=56:14436, first_product=112:58376, bound_value=120:88987, second_product=240:118636, answer=225:31599)
- Layer 41: ` mul`, `mul`, `acular`, ` .`, `鹉` (target ranks: base_value=56:3736, first_product=112:53983, bound_value=120:52250, second_product=240:103755, answer=225:14079)

### Filler position 19 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125251, first_product=112:122158, bound_value=120:121655, second_product=240:123683, answer=225:125912)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10843, first_product=112:24356, bound_value=120:22670, second_product=240:22402, answer=225:17751)
- Layer 20: `ait`, `忑`, ` Walker`, `会成为`, ` engaging` (target ranks: base_value=56:16291, first_product=112:47302, bound_value=120:57660, second_product=240:64491, answer=225:31211)
- Layer 30: `算出`, ` calculator`, `calcul`, `calculator`, `计算出` (target ranks: base_value=56:2074, first_product=112:37303, bound_value=120:84516, second_product=240:88532, answer=225:18625)
- Layer 35: ` calculator`, `calcul`, ` Tw`, `calculator`, `算出` (target ranks: base_value=56:6244, first_product=112:54803, bound_value=120:92592, second_product=240:92148, answer=225:12308)
- Layer 36: `calcul`, ` calculator`, `留存`, ` Calculators`, ` Tw` (target ranks: base_value=56:7604, first_product=112:48320, bound_value=120:78806, second_product=240:78457, answer=225:7360)
- Layer 37: `calcul`, `}<?`, ` Calculators`, `不急`, `计算的` (target ranks: base_value=56:14575, first_product=112:73622, bound_value=120:110401, second_product=240:110282, answer=225:15575)
- Layer 38: `}<?`, `zat`, ` sublim`, `不大`, `殿堂` (target ranks: base_value=56:22537, first_product=112:88757, bound_value=120:111255, second_product=240:115812, answer=225:33711)
- Layer 39: `}<?`, `mul`, ` sublim`, ` mul`, `ocyst` (target ranks: base_value=56:24335, first_product=112:88484, bound_value=120:117360, second_product=240:124101, answer=225:45865)
- Layer 40: `mul`, ` mul`, `mult`, ` c`, ` multipliers` (target ranks: base_value=56:2170, first_product=112:42496, bound_value=120:84572, second_product=240:111889, answer=225:7781)
- Layer 41: ` .`, `矶`, `鹉`, `mul`, ` multipliers` (target ranks: base_value=56:448, first_product=112:42099, bound_value=120:46236, second_product=240:89554, answer=225:2139)

### Filler position 20 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125457, first_product=112:122476, bound_value=120:121913, second_product=240:123880, answer=225:126064)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10985, first_product=112:23490, bound_value=120:21592, second_product=240:21400, answer=225:17038)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `忑` (target ranks: base_value=56:12430, first_product=112:33761, bound_value=120:50783, second_product=240:49857, answer=225:25598)
- Layer 30: ` tap`, `Tap`, ` Tap`, `tap`, `鞍` (target ranks: base_value=56:7157, first_product=112:23941, bound_value=120:92043, second_product=240:84343, answer=225:18423)
- Layer 35: ` repetition`, `重复`, ` tap`, `acin`, ` repetitions` (target ranks: base_value=56:1739, first_product=112:4260, bound_value=120:42972, second_product=240:38219, answer=225:662)
- Layer 36: `acin`, `冰冰`, `calcul`, `反复`, `留存` (target ranks: base_value=56:3370, first_product=112:5984, bound_value=120:42235, second_product=240:43021, answer=225:526)
- Layer 37: `}<?`, `acons`, `冰冰`, ` resist`, ` talags` (target ranks: base_value=56:28961, first_product=112:17161, bound_value=120:64696, second_product=240:70039, answer=225:2698)
- Layer 38: `}<?`, `acons`, `dividers`, ` talags`, `osit` (target ranks: base_value=56:61928, first_product=112:33760, bound_value=120:69685, second_product=240:75365, answer=225:4096)
- Layer 39: `}<?`, `ocyst`, `acons`, `?datasetId`, `hatic` (target ranks: base_value=56:112726, first_product=112:89774, bound_value=120:74810, second_product=240:54306, answer=225:1133)
- Layer 40: `225`, `radesh`, `osit`, `acl`, ` udalerria` (target ranks: base_value=56:98892, first_product=112:91042, bound_value=120:48554, second_product=240:18488, answer=225:1)
- Layer 41: ` .`, `225`, ` `, ` ;`, `鹉` (target ranks: base_value=56:40361, first_product=112:52051, bound_value=120:23710, second_product=240:7977, answer=225:2)

### Filler position 21 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125399, first_product=112:122412, bound_value=120:121869, second_product=240:123836, answer=225:126039)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10497, first_product=112:22939, bound_value=120:21065, second_product=240:20927, answer=225:16752)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, `拆` (target ranks: base_value=56:9011, first_product=112:20101, bound_value=120:39192, second_product=240:31246, answer=225:14761)
- Layer 30: `粥`, `肺癌`, `acos`, ` dripping`, `adal` (target ranks: base_value=56:1274, first_product=112:3507, bound_value=120:2037, second_product=240:547, answer=225:33)
- Layer 35: `225`, `itetsdata`, `akah`, `585`, `240` (target ranks: base_value=56:9820, first_product=112:20308, bound_value=120:72364, second_product=240:5, answer=225:1)
- Layer 36: `225`, `ppg`, `迷惑`, ` Parehong`, `Kadaghanon` (target ranks: base_value=56:32160, first_product=112:63337, bound_value=120:101753, second_product=240:1063, answer=225:1)
- Layer 37: `?datasetId`, `ppg`, ` Parehong`, `225`, `迷惑` (target ranks: base_value=56:75979, first_product=112:67747, bound_value=120:66508, second_product=240:420, answer=225:4)
- Layer 38: `225`, `}<?`, `ppg`, `�`, `?datasetId` (target ranks: base_value=56:119053, first_product=112:83505, bound_value=120:92325, second_product=240:622, answer=225:1)
- Layer 39: `225`, ` Loy`, `}<?`, ` Oy`, `CLC` (target ranks: base_value=56:126421, first_product=112:114116, bound_value=120:123179, second_product=240:4748, answer=225:1)
- Layer 40: `225`, ` kinahabogang`, ` Parehong`, `}<?`, `usercontent` (target ranks: base_value=56:117296, first_product=112:97898, bound_value=120:103315, second_product=240:2060, answer=225:1)
- Layer 41: `225`, ` .`, `鹉`, `笔者`, ` guarante` (target ranks: base_value=56:68269, first_product=112:76734, bound_value=120:85880, second_product=240:12744, answer=225:1)

### Filler position 22 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125680, first_product=112:122856, bound_value=120:122257, second_product=240:124089, answer=225:126209)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9843, first_product=112:22636, bound_value=120:20823, second_product=240:20342, answer=225:16726)
- Layer 20: `ait`, `锁定`, `距`, ` engaging`, ` Walker` (target ranks: base_value=56:11286, first_product=112:27592, bound_value=120:41324, second_product=240:40211, answer=225:25255)
- Layer 30: ` Tw`, `Tw`, ` twice`, `.tw`, `tw` (target ranks: base_value=56:4929, first_product=112:16638, bound_value=120:69282, second_product=240:74175, answer=225:29544)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:3865, first_product=112:14799, bound_value=120:71231, second_product=240:69997, answer=225:17723)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=56:3925, first_product=112:10370, bound_value=120:69086, second_product=240:64925, answer=225:8966)
- Layer 37: ` Tw`, `Tw`, `.tw`, ` twice`, `}<?` (target ranks: base_value=56:10626, first_product=112:20024, bound_value=120:101968, second_product=240:94473, answer=225:14737)
- Layer 38: ` Tw`, `Tw`, `.tw`, `}<?`, ` doubling` (target ranks: base_value=56:16503, first_product=112:27748, bound_value=120:98869, second_product=240:106991, answer=225:29099)
- Layer 39: ` Tw`, `Tw`, `}<?`, ` Twist`, ` twist` (target ranks: base_value=56:10050, first_product=112:15320, bound_value=120:76843, second_product=240:109081, answer=225:45145)
- Layer 40: ` Tw`, `zat`, ` mul`, ` Mul`, `mul` (target ranks: base_value=56:199, first_product=112:2062, bound_value=120:26229, second_product=240:85338, answer=225:2527)
- Layer 41: ` .`, ` twice`, ` `, ` twist`, `计算公式` (target ranks: base_value=56:33, first_product=112:3639, bound_value=120:16339, second_product=240:76645, answer=225:2363)

### Filler position 23 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126136, first_product=112:123667, bound_value=120:123209, second_product=240:124828, answer=225:126720)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:11293, first_product=112:24510, bound_value=120:22286, second_product=240:21416, answer=225:17686)
- Layer 20: `锁定`, ` smile`, `幽`, `ait`, `足` (target ranks: base_value=56:12439, first_product=112:27515, bound_value=120:36272, second_product=240:36651, answer=225:16011)
- Layer 30: ` Tw`, ` resolve`, `算出`, `atan`, ` resolves` (target ranks: base_value=56:3581, first_product=112:16069, bound_value=120:50414, second_product=240:75604, answer=225:26244)
- Layer 35: ` resolve`, ` resolves`, ` resolution`, `resolve`, `calcul` (target ranks: base_value=56:3674, first_product=112:25133, bound_value=120:57596, second_product=240:69324, answer=225:17276)
- Layer 36: `calcul`, `�`, `分解`, ` calculate`, ` resolve` (target ranks: base_value=56:4161, first_product=112:27510, bound_value=120:52969, second_product=240:65602, answer=225:6848)
- Layer 37: `calcul`, `radesh`, `计算的`, `calculated`, `计算方法` (target ranks: base_value=56:9510, first_product=112:43563, bound_value=120:94037, second_product=240:106962, answer=225:13113)
- Layer 38: `calcul`, ` RES`, ` Res`, `殿堂`, `referent` (target ranks: base_value=56:22218, first_product=112:51272, bound_value=120:84426, second_product=240:106880, answer=225:16284)
- Layer 39: ` RES`, `殿堂`, ` Res`, `�`, `reso` (target ranks: base_value=56:35285, first_product=112:81880, bound_value=120:83546, second_product=240:117047, answer=225:44048)
- Layer 40: `殿堂`, ` c`, `acl`, `c`, ` first` (target ranks: base_value=56:13765, first_product=112:27402, bound_value=120:42687, second_product=240:104856, answer=225:6935)
- Layer 41: ` .`, ` first`, `本`, ` `, `然而` (target ranks: base_value=56:1724, first_product=112:20124, bound_value=120:24219, second_product=240:82045, answer=225:1737)

### Filler position 24 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125899, first_product=112:123259, bound_value=120:122759, second_product=240:124401, answer=225:126454)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:10857, first_product=112:25039, bound_value=120:22432, second_product=240:22352, answer=225:18404)
- Layer 20: `足`, ` smile`, `ait`, ` LS`, ` ES` (target ranks: base_value=56:4998, first_product=112:24857, bound_value=120:25098, second_product=240:30116, answer=225:16189)
- Layer 30: ` ignoring`, `忽略`, ` ignored`, ` ignore`, `Ign` (target ranks: base_value=56:3244, first_product=112:48770, bound_value=120:71291, second_product=240:88128, answer=225:20480)
- Layer 35: ` repetition`, `重复`, `calcul`, ` calculate`, ` ignoring` (target ranks: base_value=56:7585, first_product=112:55536, bound_value=120:82186, second_product=240:100874, answer=225:42355)
- Layer 36: `calcul`, `忽略`, ` repeated`, ` calculate`, `重复` (target ranks: base_value=56:5771, first_product=112:42404, bound_value=120:58505, second_product=240:88905, answer=225:19939)
- Layer 37: `calcul`, `不急`, `acl`, `radesh`, `殿堂` (target ranks: base_value=56:16655, first_product=112:69508, bound_value=120:103436, second_product=240:122179, answer=225:45270)
- Layer 38: `不急`, `殿堂`, `calcul`, `acl`, `}<?` (target ranks: base_value=56:29032, first_product=112:71095, bound_value=120:106916, second_product=240:125352, answer=225:56417)
- Layer 39: `<｜begin▁of▁sentence｜>`, `殿堂`, `ocyst`, `script`, `radesh` (target ranks: base_value=56:62504, first_product=112:98470, bound_value=120:104680, second_product=240:126975, answer=225:88521)
- Layer 40: `acl`, `殿堂`, `不急`, ` nasod`, ` mul` (target ranks: base_value=56:25745, first_product=112:63759, bound_value=120:72660, second_product=240:123527, answer=225:35901)
- Layer 41: ` .`, `然而`, ` `, `鹃`, `每次` (target ranks: base_value=56:2646, first_product=112:25615, bound_value=120:21406, second_product=240:102951, answer=225:4948)

### Filler position 25 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126262, first_product=112:123788, bound_value=120:123300, second_product=240:124689, answer=225:126719)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11353, first_product=112:26418, bound_value=120:23780, second_product=240:24126, answer=225:19036)
- Layer 20: `锁定`, ` smile`, `足`, `鞍`, `竹` (target ranks: base_value=56:9893, first_product=112:27499, bound_value=120:34715, second_product=240:27728, answer=225:13438)
- Layer 30: `calcul`, `计算的`, `计算`, ` calculator`, ` calculate` (target ranks: base_value=56:979, first_product=112:4657, bound_value=120:10308, second_product=240:11175, answer=225:1624)
- Layer 35: ` calculator`, `calcul`, `计算的`, `计算`, ` calculations` (target ranks: base_value=56:559, first_product=112:2759, bound_value=120:7491, second_product=240:5346, answer=225:357)
- Layer 36: `calcul`, `计算的`, ` calculations`, ` calculator`, `计算` (target ranks: base_value=56:1552, first_product=112:2968, bound_value=120:8115, second_product=240:2814, answer=225:142)
- Layer 37: `}<?`, ` Parehong`, ` pakig`, `calcul`, `计算方法` (target ranks: base_value=56:14003, first_product=112:3120, bound_value=120:1561, second_product=240:626, answer=225:347)
- Layer 38: `}<?`, ` Parehong`, ` Noruwega`, ` pakig`, ` Duc` (target ranks: base_value=56:48418, first_product=112:5353, bound_value=120:1087, second_product=240:128, answer=225:399)
- Layer 39: `}<?`, `?datasetId`, `hatic`, `ocyst`, ` Parehong` (target ranks: base_value=56:122551, first_product=112:104384, bound_value=120:26290, second_product=240:573, answer=225:995)
- Layer 40: ` talags`, ` pakig`, `radesh`, `paragraph`, ` serving` (target ranks: base_value=56:121334, first_product=112:117427, bound_value=120:12444, second_product=240:579, answer=225:12)
- Layer 41: `步骤如下`, ` paragraph`, ` serving`, `因为这些`, `信箱` (target ranks: base_value=56:94559, first_product=112:98956, bound_value=120:7069, second_product=240:900, answer=225:46)

### Filler position 26 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126345, first_product=112:124018, bound_value=120:123559, second_product=240:124925, answer=225:126871)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10656, first_product=112:24443, bound_value=120:22957, second_product=240:22315, answer=225:17363)
- Layer 20: ` Walker`, `ait`, `Walker`, `锁定`, ` LS` (target ranks: base_value=56:9536, first_product=112:28705, bound_value=120:38159, second_product=240:39440, answer=225:20643)
- Layer 30: `EQ`, ` EQ`, `ragma`, `aq`, `acin` (target ranks: base_value=56:8250, first_product=112:50602, bound_value=120:123861, second_product=240:125737, answer=225:66979)
- Layer 35: `daq`, `大河`, `EQ`, ` EQ`, `adal` (target ranks: base_value=56:9534, first_product=112:53189, bound_value=120:123196, second_product=240:125352, answer=225:45002)
- Layer 36: `adal`, ` stabil`, `acl`, `daq`, `因素的影响` (target ranks: base_value=56:7508, first_product=112:33560, bound_value=120:114739, second_product=240:118504, answer=225:23333)
- Layer 37: ` mul`, `daq`, `}<?`, `mul`, `Quintal` (target ranks: base_value=56:22481, first_product=112:49399, bound_value=120:122601, second_product=240:125960, answer=225:51859)
- Layer 38: ` mul`, `}<?`, `Quintal`, `zat`, `mul` (target ranks: base_value=56:33829, first_product=112:69463, bound_value=120:123531, second_product=240:127681, answer=225:71697)
- Layer 39: ` mul`, `mul`, `acons`, ` Mul`, `Quintal` (target ranks: base_value=56:46212, first_product=112:65752, bound_value=120:120819, second_product=240:127703, answer=225:64100)
- Layer 40: `daq`, `acl`, `ascals`, ` Da`, `ascript` (target ranks: base_value=56:8204, first_product=112:30925, bound_value=120:99249, second_product=240:122455, answer=225:13401)
- Layer 41: `ascals`, `矶`, `鹉`, ` waterfall`, ` .` (target ranks: base_value=56:353, first_product=112:12779, bound_value=120:39258, second_product=240:91267, answer=225:1593)

### Filler position 27 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126552, first_product=112:124433, bound_value=120:123957, second_product=240:125201, answer=225:127029)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10195, first_product=112:22513, bound_value=120:21613, second_product=240:20255, answer=225:16033)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` engaging` (target ranks: base_value=56:8072, first_product=112:22197, bound_value=120:34973, second_product=240:29421, answer=225:15531)
- Layer 30: `Mul`, ` mul`, `mul`, ` Mul`, ` Mull` (target ranks: base_value=56:774, first_product=112:31905, bound_value=120:126218, second_product=240:106935, answer=225:21493)
- Layer 35: `Mul`, ` mul`, ` Mull`, ` Mul`, `mul` (target ranks: base_value=56:568, first_product=112:35047, bound_value=120:123912, second_product=240:101485, answer=225:17058)
- Layer 36: `Mul`, ` mul`, ` Mul`, ` Mull`, `mul` (target ranks: base_value=56:1544, first_product=112:22745, bound_value=120:119584, second_product=240:95087, answer=225:10154)
- Layer 37: `Mul`, ` mul`, `mul`, ` Mul`, `}<?` (target ranks: base_value=56:9876, first_product=112:41245, bound_value=120:126250, second_product=240:119688, answer=225:33277)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=56:13806, first_product=112:47705, bound_value=120:122323, second_product=240:119910, answer=225:41227)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `zat` (target ranks: base_value=56:45688, first_product=112:70069, bound_value=120:124022, second_product=240:122122, answer=225:59251)
- Layer 40: ` mul`, `mul`, `zat`, `acl`, `Mul` (target ranks: base_value=56:11492, first_product=112:37037, bound_value=120:112359, second_product=240:115263, answer=225:14085)
- Layer 41: ` mul`, `mul`, `acular`, `zij`, `鹉` (target ranks: base_value=56:1535, first_product=112:26704, bound_value=120:72216, second_product=240:85698, answer=225:2495)

### Filler position 28 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126373, first_product=112:123966, bound_value=120:123405, second_product=240:124745, answer=225:126737)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:10349, first_product=112:22698, bound_value=120:21262, second_product=240:20526, answer=225:16649)
- Layer 20: `ait`, `能被`, `拆`, ` Walker`, ` engaging` (target ranks: base_value=56:7183, first_product=112:17463, bound_value=120:30337, second_product=240:25831, answer=225:15431)
- Layer 30: `粥`, ` expecting`, `生日`, `打完`, `六十` (target ranks: base_value=56:198, first_product=112:3907, bound_value=120:2484, second_product=240:7241, answer=225:29205)
- Layer 35: `120`, `粥`, `六十`, ` Ginhadi`, `分解` (target ranks: base_value=56:4663, first_product=112:32275, bound_value=120:1, second_product=240:375, answer=225:43750)
- Layer 36: `120`, ` Ginhadi`, `粥`, ` sag`, `acin` (target ranks: base_value=56:26848, first_product=112:53156, bound_value=120:1, second_product=240:404, answer=225:59818)
- Layer 37: `120`, `}<?`, `?datasetId`, `zat`, `ppg` (target ranks: base_value=56:74440, first_product=112:85030, bound_value=120:1, second_product=240:2162, answer=225:106303)
- Layer 38: `120`, `zat`, `}<?`, `ivit`, `igit` (target ranks: base_value=56:93937, first_product=112:98726, bound_value=120:1, second_product=240:5510, answer=225:113794)
- Layer 39: `120`, `}<?`, `zat`, `ocyst`, `ozygous` (target ranks: base_value=56:78018, first_product=112:93636, bound_value=120:1, second_product=240:19695, answer=225:90944)
- Layer 40: `120`, `俯`, `zat`, ` twofold`, ` doubled` (target ranks: base_value=56:23777, first_product=112:49382, bound_value=120:1, second_product=240:8216, answer=225:15609)
- Layer 41: `120`, ` twice`, `实在`, ` nowhere`, ` accustomed` (target ranks: base_value=56:5827, first_product=112:51102, bound_value=120:1, second_product=240:7322, answer=225:16922)

### Filler position 29 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126372, first_product=112:123977, bound_value=120:123453, second_product=240:124789, answer=225:126775)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:10860, first_product=112:23663, bound_value=120:21965, second_product=240:21697, answer=225:17676)
- Layer 20: `锁定`, `ession`, ` smile`, `aty`, `幽` (target ranks: base_value=56:12017, first_product=112:23704, bound_value=120:36778, second_product=240:36345, answer=225:21888)
- Layer 30: `daq`, `DAQ`, ` EQ`, `EQ`, ` Da` (target ranks: base_value=56:13933, first_product=112:24148, bound_value=120:102166, second_product=240:124011, answer=225:57058)
- Layer 35: `daq`, `cape`, `DAQ`, `感兴趣`, `分解` (target ranks: base_value=56:11843, first_product=112:25222, bound_value=120:88802, second_product=240:120438, answer=225:34793)
- Layer 36: `俯`, `坏`, `感兴趣`, `daq`, `感兴趣的` (target ranks: base_value=56:15938, first_product=112:26126, bound_value=120:78960, second_product=240:113742, answer=225:26991)
- Layer 37: `}<?`, `翻了`, `坏`, `isis`, `覆` (target ranks: base_value=56:35852, first_product=112:46293, bound_value=120:111268, second_product=240:126440, answer=225:52457)
- Layer 38: `}<?`, `zat`, `坏`, `覆`, `迷惑` (target ranks: base_value=56:29865, first_product=112:47887, bound_value=120:109074, second_product=240:127394, answer=225:57111)
- Layer 39: `}<?`, ` unflagged`, `<｜begin▁of▁sentence｜>`, `覆`, `东海` (target ranks: base_value=56:75170, first_product=112:93552, bound_value=120:120009, second_product=240:128356, answer=225:94558)
- Layer 40: `坏`, `坏的`, ` Tw`, `不急`, `acl` (target ranks: base_value=56:28437, first_product=112:56179, bound_value=120:106421, second_product=240:123822, answer=225:41210)
- Layer 41: `坏`, `没有被`, `从前`, ` .`, ` ` (target ranks: base_value=56:4312, first_product=112:33170, bound_value=120:53201, second_product=240:105484, answer=225:11646)

### Filler position 30 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126847, first_product=112:124726, bound_value=120:124189, second_product=240:125270, answer=225:127156)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10151, first_product=112:22742, bound_value=120:21037, second_product=240:20899, answer=225:17186)
- Layer 20: `cape`, `鞍`, ` smile`, `ait`, `锁定` (target ranks: base_value=56:7847, first_product=112:17811, bound_value=120:21294, second_product=240:25549, answer=225:15568)
- Layer 30: ` tap`, `Tap`, `鞍`, `tap`, ` Tap` (target ranks: base_value=56:12620, first_product=112:68860, bound_value=120:59239, second_product=240:37315, answer=225:47769)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, ` answer` (target ranks: base_value=56:7054, first_product=112:73382, bound_value=120:67348, second_product=240:53694, answer=225:47392)
- Layer 36: ` tap`, `Tap`, ` Tap`, `tap`, ` Tw` (target ranks: base_value=56:5724, first_product=112:58136, bound_value=120:41734, second_product=240:34754, answer=225:26211)
- Layer 37: `}<?`, ` lenker`, `radesh`, ` tap`, `rational` (target ranks: base_value=56:13674, first_product=112:66159, bound_value=120:71142, second_product=240:72870, answer=225:52631)
- Layer 38: `}<?`, ` lenker`, `dividers`, `�`, `rational` (target ranks: base_value=56:13435, first_product=112:69355, bound_value=120:62119, second_product=240:69676, answer=225:41283)
- Layer 39: `}<?`, `ocyst`, ` lenker`, `dividers`, `�` (target ranks: base_value=56:55950, first_product=112:68754, bound_value=120:46343, second_product=240:47982, answer=225:11035)
- Layer 40: `acular`, `acl`, ` Answer`, `的计算`, `Answer` (target ranks: base_value=56:20374, first_product=112:24307, bound_value=120:12911, second_product=240:13589, answer=225:8)
- Layer 41: `Answer`, `225`, ` Answer`, `cab`, `acular` (target ranks: base_value=56:2056, first_product=112:2727, bound_value=120:1280, second_product=240:1820, answer=225:2)

### Filler position 31 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126777, first_product=112:124656, bound_value=120:124128, second_product=240:125157, answer=225:127136)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9824, first_product=112:22311, bound_value=120:20464, second_product=240:20985, answer=225:16796)
- Layer 20: `锁定`, `鞍`, `ait`, ` smile`, ` LS` (target ranks: base_value=56:8361, first_product=112:20347, bound_value=120:23921, second_product=240:26903, answer=225:14695)
- Layer 30: `鞍`, ` tap`, ` labor`, `Tap`, ` ES` (target ranks: base_value=56:3056, first_product=112:38635, bound_value=120:57738, second_product=240:67470, answer=225:18627)
- Layer 35: ` tap`, `鞍`, ` labor`, `cape`, `锁定` (target ranks: base_value=56:5720, first_product=112:38789, bound_value=120:56490, second_product=240:71379, answer=225:16322)
- Layer 36: ` tap`, ` stabil`, `calcul`, `柿子`, `留存` (target ranks: base_value=56:5661, first_product=112:36425, bound_value=120:43780, second_product=240:63740, answer=225:10065)
- Layer 37: `不急`, `calcul`, `坏`, `}<?`, `冰冰` (target ranks: base_value=56:14167, first_product=112:48643, bound_value=120:82424, second_product=240:104674, answer=225:16008)
- Layer 38: `不急`, `}<?`, `坏`, `冰冰`, `第一步` (target ranks: base_value=56:21393, first_product=112:59235, bound_value=120:91987, second_product=240:114948, answer=225:19325)
- Layer 39: `<｜begin▁of▁sentence｜>`, `ocyst`, `}<?`, `殿堂`, `radesh` (target ranks: base_value=56:46546, first_product=112:58723, bound_value=120:70580, second_product=240:108989, answer=225:18155)
- Layer 40: `mul`, `acular`, ` mul`, `不急`, `calcul` (target ranks: base_value=56:5559, first_product=112:12581, bound_value=120:19432, second_product=240:65884, answer=225:352)
- Layer 41: ` .`, `c`, `cab`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=56:550, first_product=112:3384, bound_value=120:2070, second_product=240:18834, answer=225:70)

### Filler position 32 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:126963, first_product=112:124947, bound_value=120:124456, second_product=240:125426, answer=225:127291)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9799, first_product=112:22199, bound_value=120:20024, second_product=240:21334, answer=225:16567)
- Layer 20: ` ES`, ` LS`, ` Walker`, `锁定`, `ait` (target ranks: base_value=56:9074, first_product=112:21415, bound_value=120:28367, second_product=240:35297, answer=225:15123)
- Layer 30: ` twice`, ` Tw`, `Tw`, `鞍`, ` metas` (target ranks: base_value=56:12, first_product=112:493, bound_value=120:21228, second_product=240:63729, answer=225:33392)
- Layer 35: ` Tw`, ` twice`, ` repetition`, ` calculator`, ` smile` (target ranks: base_value=56:20, first_product=112:24, bound_value=120:512, second_product=240:18030, answer=225:4002)
- Layer 36: `antal`, `羊`, `感兴趣`, ` stabil`, ` Tw` (target ranks: base_value=56:169, first_product=112:71, bound_value=120:1202, second_product=240:20765, answer=225:3158)
- Layer 37: ` doubling`, `}<?`, `计算公式`, `凌霄`, `ascals` (target ranks: base_value=56:458, first_product=112:28, bound_value=120:920, second_product=240:38363, answer=225:10537)
- Layer 38: `}<?`, ` doubling`, `?datasetId`, `殿堂`, ` pals` (target ranks: base_value=56:1934, first_product=112:363, bound_value=120:4232, second_product=240:85255, answer=225:27912)
- Layer 39: ` doubling`, `}<?`, `urin`, `opters`, `etic` (target ranks: base_value=56:4672, first_product=112:13343, bound_value=120:16203, second_product=240:82475, answer=225:50180)
- Layer 40: ` talags`, `antal`, `eland`, `mul`, ` fum` (target ranks: base_value=56:144, first_product=112:3678, bound_value=120:1535, second_product=240:55400, answer=225:7636)
- Layer 41: ` fum`, `瘫�`, ` Tw`, `etic`, ` complication` (target ranks: base_value=56:54, first_product=112:5343, bound_value=120:2436, second_product=240:64791, answer=225:7205)

### Filler position 33 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:127037, first_product=112:125117, bound_value=120:124636, second_product=240:125577, answer=225:127349)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9387, first_product=112:21733, bound_value=120:19897, second_product=240:20647, answer=225:15863)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=56:9181, first_product=112:24524, bound_value=120:33191, second_product=240:40724, answer=225:16332)
- Layer 30: `acin`, `adal`, ` basal`, `平行`, `acos` (target ranks: base_value=56:1074, first_product=112:16246, bound_value=120:82424, second_product=240:95981, answer=225:23712)
- Layer 35: `adal`, ` mun`, ` Mull`, ` repetition`, `acin` (target ranks: base_value=56:333, first_product=112:11639, bound_value=120:73487, second_product=240:74167, answer=225:5895)
- Layer 36: `adal`, `留存`, `Mul`, ` mun`, ` mul` (target ranks: base_value=56:975, first_product=112:11532, bound_value=120:72446, second_product=240:80922, answer=225:3130)
- Layer 37: `Mul`, ` mul`, ` Mul`, `mul`, `}<?` (target ranks: base_value=56:5128, first_product=112:27245, bound_value=120:104465, second_product=240:106473, answer=225:13571)
- Layer 38: ` Mul`, `Mul`, ` mul`, `mul`, `}<?` (target ranks: base_value=56:5454, first_product=112:43783, bound_value=120:101156, second_product=240:110459, answer=225:22178)
- Layer 39: ` Mul`, `Mul`, ` mul`, `mul`, `}<?` (target ranks: base_value=56:22463, first_product=112:54285, bound_value=120:104925, second_product=240:120069, answer=225:53105)
- Layer 40: ` mul`, `mul`, `Mul`, ` Mul`, ` talags` (target ranks: base_value=56:870, first_product=112:9230, bound_value=120:36261, second_product=240:94249, answer=225:6393)
- Layer 41: ` mul`, `mul`, `Mul`, ` whichever`, ` Mul` (target ranks: base_value=56:142, first_product=112:17482, bound_value=120:24234, second_product=240:91342, answer=225:4271)

### Filler position 34 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:127014, first_product=112:125114, bound_value=120:124651, second_product=240:125609, answer=225:127346)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9675, first_product=112:22475, bound_value=120:20986, second_product=240:20671, answer=225:16181)
- Layer 20: `ait`, `锁定`, ` smile`, `足`, ` Walker` (target ranks: base_value=56:7361, first_product=112:26598, bound_value=120:42124, second_product=240:37874, answer=225:18754)
- Layer 30: `acin`, `adal`, `atan`, `acos`, `sets` (target ranks: base_value=56:3448, first_product=112:24721, bound_value=120:109961, second_product=240:96757, answer=225:29201)
- Layer 35: `adal`, `acin`, ` repetition`, ` reserved`, `acic` (target ranks: base_value=56:2707, first_product=112:33320, bound_value=120:111572, second_product=240:97249, answer=225:27005)
- Layer 36: `adal`, `留存`, `acin`, `acl`, `acic` (target ranks: base_value=56:4747, first_product=112:30069, bound_value=120:108510, second_product=240:93848, answer=225:13609)
- Layer 37: ` mul`, `}<?`, `Mul`, ` Mul`, `mul` (target ranks: base_value=56:16552, first_product=112:62524, bound_value=120:125977, second_product=240:120721, answer=225:36630)
- Layer 38: ` mul`, ` Mul`, `zat`, `Mul`, `mul` (target ranks: base_value=56:16580, first_product=112:79848, bound_value=120:125765, second_product=240:120640, answer=225:49785)
- Layer 39: ` Mul`, ` mul`, `mul`, `Mul`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=56:35030, first_product=112:88097, bound_value=120:125506, second_product=240:124328, answer=225:73799)
- Layer 40: ` mul`, `mul`, `c`, `Mul`, `acl` (target ranks: base_value=56:6129, first_product=112:34152, bound_value=120:101140, second_product=240:112228, answer=225:25028)
- Layer 41: ` mul`, `mul`, `acular`, `zij`, ` whichever` (target ranks: base_value=56:181, first_product=112:15235, bound_value=120:63607, second_product=240:83727, answer=225:4324)

### Filler position 35 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127318, first_product=112:125654, bound_value=120:125206, second_product=240:125994, answer=225:127584)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10988, first_product=112:24190, bound_value=120:22648, second_product=240:21904, answer=225:17636)
- Layer 20: `ait`, ` smile`, `足`, `cape`, `能被` (target ranks: base_value=56:8403, first_product=112:28740, bound_value=120:39360, second_product=240:33290, answer=225:16639)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=56:9152, first_product=112:28992, bound_value=120:60662, second_product=240:65980, answer=225:36500)
- Layer 35: ` Tw`, `Tw`, ` twice`, `tw`, `询问` (target ranks: base_value=56:7964, first_product=112:32167, bound_value=120:67104, second_product=240:71151, answer=225:29376)
- Layer 36: ` Tw`, `询问`, `Tw`, `.tw`, ` twice` (target ranks: base_value=56:10295, first_product=112:33799, bound_value=120:63691, second_product=240:62499, answer=225:17153)
- Layer 37: ` Tw`, ` doubling`, `提问`, `询问`, `}<?` (target ranks: base_value=56:25761, first_product=112:61374, bound_value=120:103890, second_product=240:103488, answer=225:40142)
- Layer 38: ` Tw`, ` doubling`, `Tw`, `.tw`, ` twist` (target ranks: base_value=56:22701, first_product=112:73471, bound_value=120:96154, second_product=240:106423, answer=225:45375)
- Layer 39: ` doubling`, ` Tw`, ` doubled`, `}<?`, `zat` (target ranks: base_value=56:8295, first_product=112:43707, bound_value=120:68466, second_product=240:109958, answer=225:49646)
- Layer 40: `c`, ` mul`, ` c`, `mul`, ` Mul` (target ranks: base_value=56:1092, first_product=112:12643, bound_value=120:20562, second_product=240:64443, answer=225:6416)
- Layer 41: ` multipliers`, ` mul`, ` multiplier`, `c`, ` ` (target ranks: base_value=56:40, first_product=112:1738, bound_value=120:4068, second_product=240:29358, answer=225:373)

### Filler position 36 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127352, first_product=112:125752, bound_value=120:125371, second_product=240:126108, answer=225:127648)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11860, first_product=112:25598, bound_value=120:23668, second_product=240:23226, answer=225:19541)
- Layer 20: `能被`, `距`, `ait`, `拆`, ` Walker` (target ranks: base_value=56:9045, first_product=112:27558, bound_value=120:27373, second_product=240:29787, answer=225:23398)
- Layer 30: `放弃`, `退出`, `adal`, `65`, ` dich` (target ranks: base_value=56:3378, first_product=112:16313, bound_value=120:9389, second_product=240:2199, answer=225:46)
- Layer 35: `225`, `245`, `polar`, `Quintal`, ` Polar` (target ranks: base_value=56:48376, first_product=112:38247, bound_value=120:80028, second_product=240:14, answer=225:1)
- Layer 36: `225`, `105`, `quit`, `打扰`, `ppg` (target ranks: base_value=56:101108, first_product=112:72065, bound_value=120:103962, second_product=240:1042, answer=225:1)
- Layer 37: `225`, `cault`, `polar`, ` konts`, `ppg` (target ranks: base_value=56:121218, first_product=112:82897, bound_value=120:70111, second_product=240:500, answer=225:1)
- Layer 38: `225`, `第二百`, ` konts`, `235`, `229` (target ranks: base_value=56:128581, first_product=112:118536, bound_value=120:119470, second_product=240:895, answer=225:1)
- Layer 39: `225`, `第二百`, ` Toy`, ` mempun`, `二百` (target ranks: base_value=56:128210, first_product=112:126005, bound_value=120:125545, second_product=240:18331, answer=225:1)
- Layer 40: `225`, ` kinahabogang`, ` talags`, `第二百`, `二百` (target ranks: base_value=56:126616, first_product=112:121207, bound_value=120:95486, second_product=240:4585, answer=225:1)
- Layer 41: `225`, ` mediabestanden`, ` nuest`, `俩人`, `印书馆` (target ranks: base_value=56:109520, first_product=112:112096, bound_value=120:77211, second_product=240:22051, answer=225:1)

### Filler position 37 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127513, first_product=112:125968, bound_value=120:125579, second_product=240:126199, answer=225:127728)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11772, first_product=112:25812, bound_value=120:23534, second_product=240:23496, answer=225:20128)
- Layer 20: `能被`, `忑`, `距`, ` engaging`, ` dy` (target ranks: base_value=56:13244, first_product=112:47487, bound_value=120:37796, second_product=240:52438, answer=225:31292)
- Layer 30: `atan`, `atar`, ` absorbing`, `adak`, ` dy` (target ranks: base_value=56:391, first_product=112:7678, bound_value=120:4588, second_product=240:17332, answer=225:14040)
- Layer 35: `adal`, `obin`, `�`, `舍弃`, ` vertical` (target ranks: base_value=56:1804, first_product=112:20404, bound_value=120:31060, second_product=240:5870, answer=225:848)
- Layer 36: `radesh`, `igesimal`, `adal`, `)Skip`, `放下` (target ranks: base_value=56:4336, first_product=112:7674, bound_value=120:27520, second_product=240:12180, answer=225:1779)
- Layer 37: `)Skip`, `}<?`, `?datasetId`, `hatic`, `lez` (target ranks: base_value=56:42742, first_product=112:22290, bound_value=120:6697, second_product=240:7436, answer=225:21706)
- Layer 38: `}<?`, `桃子`, `ocyst`, `polar`, ` Pole` (target ranks: base_value=56:56628, first_product=112:3008, bound_value=120:4100, second_product=240:15246, answer=225:1684)
- Layer 39: `}<?`, `opters`, `不及`, `225`, ` duc` (target ranks: base_value=56:120504, first_product=112:43760, bound_value=120:103253, second_product=240:49873, answer=225:4)
- Layer 40: `225`, `不急`, `不加`, `不及`, `acular` (target ranks: base_value=56:109232, first_product=112:37292, bound_value=120:71587, second_product=240:17607, answer=225:1)
- Layer 41: `225`, ` .`, ` twice`, `zilla`, `227` (target ranks: base_value=56:64606, first_product=112:24728, bound_value=120:36125, second_product=240:8253, answer=225:1)

### Filler position 38 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127435, first_product=112:125827, bound_value=120:125401, second_product=240:126071, answer=225:127663)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10978, first_product=112:24083, bound_value=120:22246, second_product=240:22346, answer=225:18538)
- Layer 20: `ait`, `能被`, ` LS`, `忑`, `cape` (target ranks: base_value=56:6602, first_product=112:28070, bound_value=120:23403, second_product=240:26284, answer=225:14811)
- Layer 30: `adak`, `65`, `肺癌`, `essa`, ` smile` (target ranks: base_value=56:1183, first_product=112:8045, bound_value=120:213, second_product=240:52, answer=225:423)
- Layer 35: `240`, `itetsdata`, `245`, `241`, ` escape` (target ranks: base_value=56:7327, first_product=112:33856, bound_value=120:23436, second_product=240:1, answer=225:15)
- Layer 36: `225`, `}<?`, ` Parehong`, `ppg`, `迷惑` (target ranks: base_value=56:11959, first_product=112:97695, bound_value=120:100482, second_product=240:191, answer=225:1)
- Layer 37: ` Parehong`, `}<?`, `祭`, `225`, `迷惑` (target ranks: base_value=56:38175, first_product=112:91176, bound_value=120:51544, second_product=240:55, answer=225:4)
- Layer 38: `225`, `245`, ` careg`, `205`, `235` (target ranks: base_value=56:85454, first_product=112:103250, bound_value=120:89816, second_product=240:274, answer=225:1)
- Layer 39: `225`, ` careg`, `}<?`, `227`, ` unflagged` (target ranks: base_value=56:122977, first_product=112:111629, bound_value=120:106534, second_product=240:3696, answer=225:1)
- Layer 40: `225`, ` careg`, `227`, ` dekameters`, `二百` (target ranks: base_value=56:100470, first_product=112:72288, bound_value=120:40615, second_product=240:778, answer=225:1)
- Layer 41: `225`, `笔者认为`, ` careg`, `227`, ` .` (target ranks: base_value=56:54196, first_product=112:38591, bound_value=120:28366, second_product=240:1207, answer=225:1)

### Filler position 39 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127476, first_product=112:125885, bound_value=120:125508, second_product=240:126178, answer=225:127698)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10722, first_product=112:23220, bound_value=120:21601, second_product=240:21488, answer=225:17471)
- Layer 20: `ait`, `锁定`, ` smile`, `能被`, `鞍` (target ranks: base_value=56:7419, first_product=112:25742, bound_value=120:29882, second_product=240:27974, answer=225:15574)
- Layer 30: `essa`, ` calculator`, `sac`, `下沉`, ` seventeen` (target ranks: base_value=56:773, first_product=112:10054, bound_value=120:33103, second_product=240:24040, answer=225:75)
- Layer 35: `退出`, `obin`, ` calculator`, `essa`, `acin` (target ranks: base_value=56:6873, first_product=112:17085, bound_value=120:69169, second_product=240:37119, answer=225:27)
- Layer 36: `退出`, `留存`, `acin`, `essa`, `obin` (target ranks: base_value=56:13919, first_product=112:12528, bound_value=120:67798, second_product=240:39374, answer=225:56)
- Layer 37: `}<?`, `白马`, `Quintal`, `?datasetId`, ` resist` (target ranks: base_value=56:62879, first_product=112:29433, bound_value=120:52839, second_product=240:12118, answer=225:145)
- Layer 38: `}<?`, `?datasetId`, ` Pari`, `ocyst`, `白马` (target ranks: base_value=56:103924, first_product=112:40059, bound_value=120:68893, second_product=240:14891, answer=225:43)
- Layer 39: `}<?`, `?datasetId`, `tanle`, `ocyst`, `225` (target ranks: base_value=56:124083, first_product=112:94816, bound_value=120:100486, second_product=240:9201, answer=225:5)
- Layer 40: `225`, `}<?`, `ess`, `anin`, `留存` (target ranks: base_value=56:119273, first_product=112:97520, bound_value=120:95870, second_product=240:5169, answer=225:1)
- Layer 41: `225`, ` .`, `等待着`, ` `, `227` (target ranks: base_value=56:94222, first_product=112:77551, bound_value=120:92474, second_product=240:7572, answer=225:1)

### Filler position 40 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127359, first_product=112:125724, bound_value=120:125293, second_product=240:125992, answer=225:127605)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11396, first_product=112:24370, bound_value=120:22380, second_product=240:22683, answer=225:18615)
- Layer 20: `ait`, ` LS`, `锁定`, `能被`, `鞍` (target ranks: base_value=56:5788, first_product=112:19569, bound_value=120:22691, second_product=240:23803, answer=225:12088)
- Layer 30: `acos`, ` consuming`, `陪`, `退出`, `肺癌` (target ranks: base_value=56:1621, first_product=112:7122, bound_value=120:1268, second_product=240:620, answer=225:652)
- Layer 35: `放下`, `迷惑`, `陪`, `ubMed`, `Quintal` (target ranks: base_value=56:9850, first_product=112:21112, bound_value=120:55135, second_product=240:17, answer=225:101)
- Layer 36: `ppg`, `}<?`, ` markup`, `uerak`, `Quintal` (target ranks: base_value=56:12487, first_product=112:65164, bound_value=120:93861, second_product=240:7761, answer=225:10)
- Layer 37: `ppg`, `}<?`, ` Parehong`, ` markup`, `lez` (target ranks: base_value=56:41374, first_product=112:65538, bound_value=120:52357, second_product=240:2174, answer=225:49)
- Layer 38: `225`, `}<?`, ` markup`, `ppg`, ` mediabestanden` (target ranks: base_value=56:90374, first_product=112:56472, bound_value=120:76875, second_product=240:3171, answer=225:1)
- Layer 39: `225`, `227`, `}<?`, `-ulo`, `opters` (target ranks: base_value=56:123766, first_product=112:67605, bound_value=120:108208, second_product=240:14043, answer=225:1)
- Layer 40: `225`, `227`, `二百`, `otan`, `229` (target ranks: base_value=56:98948, first_product=112:24294, bound_value=120:35078, second_product=240:1960, answer=225:1)
- Layer 41: `225`, ` .`, `227`, ` guarante`, `要不` (target ranks: base_value=56:50905, first_product=112:6675, bound_value=120:22098, second_product=240:1610, answer=225:1)

### Filler position 41 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127309, first_product=112:125709, bound_value=120:125322, second_product=240:126019, answer=225:127606)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11304, first_product=112:24404, bound_value=120:22245, second_product=240:22402, answer=225:18365)
- Layer 20: `ait`, ` LS`, ` smile`, `锁定`, `ession` (target ranks: base_value=56:6864, first_product=112:25826, bound_value=120:22535, second_product=240:23738, answer=225:12528)
- Layer 30: `陪`, `tail`, `六十`, ` sixty`, `acos` (target ranks: base_value=56:125, first_product=112:22083, bound_value=120:6380, second_product=240:37822, answer=225:80822)
- Layer 35: `120`, `分解`, `陪`, `radesh`, ` twice` (target ranks: base_value=56:1455, first_product=112:19254, bound_value=120:1, second_product=240:14219, answer=225:64902)
- Layer 36: `120`, `radesh`, `陪`, `放下`, `}<?` (target ranks: base_value=56:11935, first_product=112:39454, bound_value=120:1, second_product=240:11517, answer=225:62951)
- Layer 37: `}<?`, `120`, `?datasetId`, `放下`, `ocyst` (target ranks: base_value=56:43846, first_product=112:59272, bound_value=120:2, second_product=240:27014, answer=225:107276)
- Layer 38: `}<?`, `120`, `ocyst`, `zat`, `perian` (target ranks: base_value=56:69454, first_product=112:72780, bound_value=120:2, second_product=240:42017, answer=225:104723)
- Layer 39: `}<?`, `ocyst`, `120`, ` Duc`, `romes` (target ranks: base_value=56:52591, first_product=112:63343, bound_value=120:3, second_product=240:20651, answer=225:29344)
- Layer 40: `120`, `radesh`, ` `, `225`, `放下` (target ranks: base_value=56:8177, first_product=112:14165, bound_value=120:1, second_product=240:984, answer=225:4)
- Layer 41: ` .`, `225`, `120`, ` twice`, ` successively` (target ranks: base_value=56:1541, first_product=112:9974, bound_value=120:3, second_product=240:595, answer=225:2)

### Filler position 42 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127465, first_product=112:125804, bound_value=120:125391, second_product=240:126055, answer=225:127645)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11463, first_product=112:24847, bound_value=120:22071, second_product=240:22516, answer=225:18458)
- Layer 20: ` smile`, `锁定`, `鞍`, ` LS`, `ession` (target ranks: base_value=56:9496, first_product=112:25886, bound_value=120:22566, second_product=240:23913, answer=225:10311)
- Layer 30: `陪`, `tap`, ` tap`, `�`, `Dynamic` (target ranks: base_value=56:2895, first_product=112:31792, bound_value=120:30888, second_product=240:18802, answer=225:9961)
- Layer 35: `�`, `放下`, `陪`, `radesh`, `尾` (target ranks: base_value=56:10681, first_product=112:71522, bound_value=120:96605, second_product=240:2787, answer=225:1563)
- Layer 36: `放下`, `}<?`, `radesh`, `陪`, ` amplified` (target ranks: base_value=56:33182, first_product=112:94104, bound_value=120:100793, second_product=240:4566, answer=225:357)
- Layer 37: `}<?`, `lez`, `-ulo`, `放下`, `cault` (target ranks: base_value=56:85357, first_product=112:103344, bound_value=120:84980, second_product=240:6068, answer=225:7621)
- Layer 38: `}<?`, `polar`, `zat`, `迷惑`, `放下` (target ranks: base_value=56:84215, first_product=112:79030, bound_value=120:78174, second_product=240:7770, answer=225:1337)
- Layer 39: `}<?`, `-ulo`, `lez`, `东海`, `polar` (target ranks: base_value=56:64320, first_product=112:37107, bound_value=120:9676, second_product=240:3738, answer=225:709)
- Layer 40: `225`, ` Tw`, ` `, ` mediabestanden`, `acular` (target ranks: base_value=56:2938, first_product=112:2277, bound_value=120:43, second_product=240:220, answer=225:1)
- Layer 41: `225`, ` .`, ` `, ` .↵↵`, ` twice` (target ranks: base_value=56:270, first_product=112:342, bound_value=120:12, second_product=240:59, answer=225:1)

### Filler position 43 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127529, first_product=112:126002, bound_value=120:125631, second_product=240:126258, answer=225:127779)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11506, first_product=112:25272, bound_value=120:21884, second_product=240:23274, answer=225:18817)
- Layer 20: ` smile`, ` Engaging`, ` engaging`, `ait`, `锁定` (target ranks: base_value=56:10508, first_product=112:26437, bound_value=120:19849, second_product=240:25116, answer=225:10441)
- Layer 30: ` twice`, ` Tw`, `mul`, ` multipliers`, `Tw` (target ranks: base_value=56:6, first_product=112:13001, bound_value=120:86515, second_product=240:87647, answer=225:42052)
- Layer 35: ` Tw`, ` twice`, `Tw`, `56`, `tw` (target ranks: base_value=56:4, first_product=112:12906, bound_value=120:50494, second_product=240:70216, answer=225:15076)
- Layer 36: ` Tw`, ` twice`, `Tw`, ` mun`, `.tw` (target ranks: base_value=56:7, first_product=112:12355, bound_value=120:44681, second_product=240:74189, answer=225:13297)
- Layer 37: ` Mul`, `mul`, `Mul`, ` mul`, ` doubling` (target ranks: base_value=56:18, first_product=112:12030, bound_value=120:41496, second_product=240:89711, answer=225:33182)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `mult` (target ranks: base_value=56:48, first_product=112:12607, bound_value=120:36891, second_product=240:100225, answer=225:38647)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `东海` (target ranks: base_value=56:3438, first_product=112:40447, bound_value=120:29776, second_product=240:82886, answer=225:44791)
- Layer 40: ` mul`, ` c`, `c`, `mul`, `duc` (target ranks: base_value=56:1271, first_product=112:4922, bound_value=120:308, second_product=240:11760, answer=225:125)
- Layer 41: `mul`, `225`, ` Tw`, ` mul`, ` .` (target ranks: base_value=56:38, first_product=112:454, bound_value=120:20, second_product=240:486, answer=225:2)

### Filler position 44 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127424, first_product=112:125795, bound_value=120:125424, second_product=240:126049, answer=225:127682)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11766, first_product=112:25208, bound_value=120:22175, second_product=240:23641, answer=225:19003)
- Layer 20: `能被`, `ait`, `距`, ` Walker`, `锁定` (target ranks: base_value=56:9952, first_product=112:30880, bound_value=120:21993, second_product=240:32312, answer=225:12764)
- Layer 30: `atar`, `柿子`, ` smile`, `鞍`, ` smoot` (target ranks: base_value=56:1678, first_product=112:6603, bound_value=120:288, second_product=240:1975, answer=225:4855)
- Layer 35: `adal`, `鞍`, `240`, `沛`, `acin` (target ranks: base_value=56:734, first_product=112:7068, bound_value=120:164, second_product=240:3, answer=225:882)
- Layer 36: `放下`, `)Skip`, `陪`, `erat`, `鞍` (target ranks: base_value=56:2049, first_product=112:623, bound_value=120:180, second_product=240:974, answer=225:1817)
- Layer 37: `)Skip`, `120`, `堂`, `放下`, `erat` (target ranks: base_value=56:17275, first_product=112:528, bound_value=120:2, second_product=240:192, answer=225:16399)
- Layer 38: `120`, `128`, ` careg`, ` mediabestanden`, `115` (target ranks: base_value=56:32418, first_product=112:15, bound_value=120:1, second_product=240:1347, answer=225:148)
- Layer 39: `225`, `二百`, ` medief`, `228`, `自然而` (target ranks: base_value=56:115394, first_product=112:309, bound_value=120:550, second_product=240:537, answer=225:1)
- Layer 40: `225`, `227`, `228`, ` twist`, ` twice` (target ranks: base_value=56:86437, first_product=112:47, bound_value=120:43, second_product=240:98, answer=225:1)
- Layer 41: `225`, ` twice`, `227`, `228`, ` multiplier` (target ranks: base_value=56:22809, first_product=112:124, bound_value=120:37, second_product=240:45, answer=225:1)

### Filler position 45 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127517, first_product=112:126053, bound_value=120:125678, second_product=240:126289, answer=225:127796)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11680, first_product=112:24379, bound_value=120:22336, second_product=240:22738, answer=225:18296)
- Layer 20: `ait`, ` Walker`, `会成为`, `锁定`, `能被` (target ranks: base_value=56:15054, first_product=112:34167, bound_value=120:30676, second_product=240:42330, answer=225:14224)
- Layer 30: `mul`, `Mul`, ` mul`, ` Mul`, ` multipliers` (target ranks: base_value=56:1745, first_product=112:44757, bound_value=120:109112, second_product=240:122843, answer=225:57764)
- Layer 35: ` mul`, ` Mul`, `mul`, `Mul`, ` Tw` (target ranks: base_value=56:1046, first_product=112:33303, bound_value=120:84190, second_product=240:116662, answer=225:25681)
- Layer 36: ` mul`, ` Mul`, `Mul`, `mul`, ` multipliers` (target ranks: base_value=56:594, first_product=112:7820, bound_value=120:38324, second_product=240:86075, answer=225:7266)
- Layer 37: ` mul`, ` Mul`, `mul`, `Mul`, `}<?` (target ranks: base_value=56:5514, first_product=112:25499, bound_value=120:61368, second_product=240:100785, answer=225:22346)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `mult` (target ranks: base_value=56:4514, first_product=112:20883, bound_value=120:51791, second_product=240:99423, answer=225:18278)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `mult` (target ranks: base_value=56:18958, first_product=112:34215, bound_value=120:38959, second_product=240:62163, answer=225:7379)
- Layer 40: ` mul`, `225`, `mul`, ` udalerria`, `acic` (target ranks: base_value=56:1058, first_product=112:2280, bound_value=120:1562, second_product=240:5213, answer=225:2)
- Layer 41: `225`, ` .`, ` `, `cab`, `<｜end▁of▁sentence｜>` (target ranks: base_value=56:82, first_product=112:764, bound_value=120:262, second_product=240:1161, answer=225:1)

### Filler position 46 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127462, first_product=112:125951, bound_value=120:125516, second_product=240:126136, answer=225:127726)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11563, first_product=112:23676, bound_value=120:22288, second_product=240:21645, answer=225:17484)
- Layer 20: ` procedural`, `刚开始`, ` blanks`, `blank`, ` DeWalt` (target ranks: base_value=56:101354, first_product=112:105019, bound_value=120:99975, second_product=240:86850, answer=225:81805)
- Layer 30: ` spac`, `?datasetId`, ` ---|---|---|---|---|---|---`, `坝`, ` dekameters` (target ranks: base_value=56:79012, first_product=112:88880, bound_value=120:113402, second_product=240:120157, answer=225:71398)
- Layer 35: `足足`, `坏`, `}using`, `dots`, `dividers` (target ranks: base_value=56:27671, first_product=112:66953, bound_value=120:89582, second_product=240:123614, answer=225:62830)
- Layer 36: `足足`, `俯`, ` blank`, ` reduct`, `ancock` (target ranks: base_value=56:3625, first_product=112:38462, bound_value=120:46970, second_product=240:99142, answer=225:20184)
- Layer 37: `}<?`, `isis`, `onana`, `放下`, ` doubling` (target ranks: base_value=56:34578, first_product=112:81581, bound_value=120:87185, second_product=240:110873, answer=225:31577)
- Layer 38: ` .`, `坏`, ` .↵↵`, `瞧`, `错过` (target ranks: base_value=56:10827, first_product=112:70712, bound_value=120:60162, second_product=240:102147, answer=225:11024)
- Layer 39: `hatic`, ` .`, `oxygen`, `onos`, `ozygous` (target ranks: base_value=56:69795, first_product=112:85401, bound_value=120:42855, second_product=240:72041, answer=225:4401)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` x`, ` .↵` (target ranks: base_value=56:20378, first_product=112:38971, bound_value=120:6730, second_product=240:28445, answer=225:269)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, ` ↵↵` (target ranks: base_value=56:3541, first_product=112:6993, bound_value=120:1510, second_product=240:4418, answer=225:7)

### Filler position 47 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127469, first_product=112:125902, bound_value=120:125480, second_product=240:126169, answer=225:127712)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=56:11210, first_product=112:23728, bound_value=120:22211, second_product=240:21713, answer=225:17659)
- Layer 20: `}<?`, ` partly`, `东海`, ` DeWalt`, ` sideways` (target ranks: base_value=56:113299, first_product=112:112833, bound_value=120:86869, second_product=240:91574, answer=225:119669)
- Layer 30: `}<?`, `}using`, `dividers`, `codeline`, `?datasetId` (target ranks: base_value=56:81195, first_product=112:89993, bound_value=120:94183, second_product=240:116904, answer=225:113856)
- Layer 35: `codeline`, `ِّف`, `浪费`, `}using`, `切割` (target ranks: base_value=56:79630, first_product=112:111505, bound_value=120:90482, second_product=240:126945, answer=225:122562)
- Layer 36: `切割`, `锯`, ` fit`, ` nasod`, `足足` (target ranks: base_value=56:34211, first_product=112:92967, bound_value=120:40320, second_product=240:114363, answer=225:100517)
- Layer 37: `}<?`, `磨损`, `在东`, `东京`, `ِّف` (target ranks: base_value=56:67473, first_product=112:109964, bound_value=120:75127, second_product=240:106036, answer=225:79291)
- Layer 38: ` .`, `遁`, `切割`, ` covari`, `lett` (target ranks: base_value=56:27074, first_product=112:92168, bound_value=120:39347, second_product=240:96865, answer=225:44433)
- Layer 39: ` unflagged`, ` Naz`, ` .`, `lett`, `aharan` (target ranks: base_value=56:98190, first_product=112:100582, bound_value=120:30351, second_product=240:48109, answer=225:3331)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, `�`, ` .↵` (target ranks: base_value=56:53874, first_product=112:60881, bound_value=120:2606, second_product=240:11170, answer=225:92)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, `225` (target ranks: base_value=56:12268, first_product=112:27953, bound_value=120:884, second_product=240:837, answer=225:5)

### Filler position 48 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127431, first_product=112:125924, bound_value=120:125526, second_product=240:126161, answer=225:127759)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=56:11100, first_product=112:24681, bound_value=120:22179, second_product=240:21790, answer=225:18431)
- Layer 20: `}<?`, `aplenty`, `aharoa`, `东海`, `)Skip` (target ranks: base_value=56:117855, first_product=112:115584, bound_value=120:70817, second_product=240:97304, answer=225:115659)
- Layer 30: `codeline`, `Quintal`, `东京`, ` slipp`, `}<?` (target ranks: base_value=56:77767, first_product=112:100518, bound_value=120:49730, second_product=240:112407, answer=225:110563)
- Layer 35: `codeline`, `AssemblyVersion`, ` fif`, `白雪`, ` doubly` (target ranks: base_value=56:97960, first_product=112:120843, bound_value=120:34155, second_product=240:121094, answer=225:109275)
- Layer 36: ` soci`, ` nasod`, `yss`, ` altitude`, ` Alt` (target ranks: base_value=56:70104, first_product=112:108251, bound_value=120:13757, second_product=240:97593, answer=225:84916)
- Layer 37: `codeline`, `Quintal`, `TreeLabel`, `镶嵌`, `肤` (target ranks: base_value=56:112446, first_product=112:117265, bound_value=120:38042, second_product=240:113166, answer=225:103776)
- Layer 38: `肤`, ` germ`, `悬挂`, `悬`, ` .` (target ranks: base_value=56:70139, first_product=112:101005, bound_value=120:21764, second_product=240:106062, answer=225:75736)
- Layer 39: `肤`, ` .`, ` .↵↵`, ` unflagged`, ` encomp` (target ranks: base_value=56:87624, first_product=112:109682, bound_value=120:34808, second_product=240:117547, answer=225:64823)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` crev` (target ranks: base_value=56:66759, first_product=112:89972, bound_value=120:17447, second_product=240:99326, answer=225:23376)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=56:16309, first_product=112:23558, bound_value=120:2365, second_product=240:51481, answer=225:3539)

### Filler position 49 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:127441, first_product=112:125901, bound_value=120:125479, second_product=240:126044, answer=225:127685)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:11345, first_product=112:25993, bound_value=120:22462, second_product=240:22192, answer=225:18809)
- Layer 20: ` licensierad`, ` grounds`, ` instantaneous`, `aplenty`, `zv` (target ranks: base_value=56:96857, first_product=112:105821, bound_value=120:58814, second_product=240:77362, answer=225:89451)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, `答案为` (target ranks: base_value=56:88679, first_product=112:116865, bound_value=120:92155, second_product=240:120816, answer=225:117221)
- Layer 35: `codeline`, ` Answer`, `oNames`, `AED`, `理性的` (target ranks: base_value=56:100121, first_product=112:105779, bound_value=120:53622, second_product=240:108743, answer=225:113409)
- Layer 36: `坏`, ` Answer`, `oNames`, ` nasod`, `停顿` (target ranks: base_value=56:41224, first_product=112:74572, bound_value=120:18110, second_product=240:78942, answer=225:83391)
- Layer 37: `oNames`, ` consum`, `codeline`, `оду`, ` konder` (target ranks: base_value=56:122934, first_product=112:105652, bound_value=120:100051, second_product=240:118353, answer=225:115374)
- Layer 38: `oNames`, `оду`, ` retard`, `<|EOT|>`, `�` (target ranks: base_value=56:122165, first_product=112:104684, bound_value=120:80670, second_product=240:111158, answer=225:105596)
- Layer 39: ` unflagged`, `�`, `oxygen`, `oNames`, `deen` (target ranks: base_value=56:99372, first_product=112:85277, bound_value=120:88094, second_product=240:106705, answer=225:27594)
- Layer 40: ` Answer`, ` .`, ` .↵↵`, ` nasod`, `Answer` (target ranks: base_value=56:24065, first_product=112:24050, bound_value=120:27237, second_product=240:65073, answer=225:1354)
- Layer 41: ` .`, ` Answer`, ` .↵↵`, `Answer`, `叮` (target ranks: base_value=56:10831, first_product=112:6602, bound_value=120:8895, second_product=240:27108, answer=225:226)

### Filler position 50 (absolute token 834, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=56:122196, first_product=112:113610, bound_value=120:112612, second_product=240:111185, answer=225:116680)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:126709, first_product=112:116871, bound_value=120:109097, second_product=240:101464, answer=225:113649)
- Layer 20: `能被`, ` Submission`, `答复`, ` ChatGPT`, `差分` (target ranks: base_value=56:6322, first_product=112:45356, bound_value=120:25579, second_product=240:38308, answer=225:34825)
- Layer 30: `堂`, `polar`, ` گزار`, `報`, ` المطلع` (target ranks: base_value=56:15016, first_product=112:29627, bound_value=120:70, second_product=240:817, answer=225:30111)
- Layer 35: `240`, `241`, ` المطلع`, `239`, `245` (target ranks: base_value=56:47976, first_product=112:73399, bound_value=120:48480, second_product=240:1, answer=225:228)
- Layer 36: ` Paglin`, `把孩子`, ` unflagged`, ` markup`, `225` (target ranks: base_value=56:27418, first_product=112:115686, bound_value=120:93442, second_product=240:112, answer=225:5)
- Layer 37: ` unflagged`, ` поха`, ` markup`, `把孩子`, ` Gelijk` (target ranks: base_value=56:66862, first_product=112:118148, bound_value=120:38803, second_product=240:19, answer=225:15)
- Layer 38: `225`, `245`, `235`, `255`, `227` (target ranks: base_value=56:100555, first_product=112:91917, bound_value=120:101259, second_product=240:89, answer=225:1)
- Layer 39: `225`, `227`, `esez`, ` Gelijk`, `王爷` (target ranks: base_value=56:125587, first_product=112:103508, bound_value=120:102877, second_product=240:1979, answer=225:1)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `_answer` (target ranks: base_value=56:123922, first_product=112:33582, bound_value=120:35116, second_product=240:7067, answer=225:10)
- Layer 41: `Answer`, ` Answer`, ` answer`, `answer`, `_answer` (target ranks: base_value=56:72424, first_product=112:15223, bound_value=120:8254, second_product=240:8222, answer=225:25)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>daq = 75
neq = 72
mul = 56
ciz = twice the number for mul plus 8
ziz = 63
Question: What is twice the number for ciz minus 15?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
