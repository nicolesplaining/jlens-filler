# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `256` (correct).
- No-filler answer: `255` (incorrect).
- Filler tokens: 50 tokens at absolute indices 796–845.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=72` | 1 (L24, filler 15) | L22, filler 1 (rank 5) |
| J-Lens | `first_product=144` | 2 (L35, filler 22) | L31, filler 22 (rank 6) |
| J-Lens | `bound_value=135` | 1 (L28, filler 1) | L28, filler 1 (rank 1) |
| J-Lens | `second_product=270` | 1 (L31, filler 1) | L30, filler 43 (rank 5) |
| J-Lens | `answer=256` | 1 (L36, filler 1) | L36, filler 1 (rank 1) |
| Logit lens | `base_value=72` | 1 (L27, filler 44) | L24, filler 41 (rank 6) |
| Logit lens | `first_product=144` | 7 (L28, filler 40) | L28, filler 16 (rank 9) |
| Logit lens | `bound_value=135` | 1 (L28, filler 1) | L27, filler 33 (rank 5) |
| Logit lens | `second_product=270` | 1 (L31, filler 1) | L30, filler 16 (rank 10) |
| Logit lens | `answer=256` | 1 (L38, filler 28) | L36, filler 1 (rank 6) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 796, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=72:118320, first_product=144:109591, bound_value=135:112015, second_product=270:112968, answer=256:115193)
- Layer 10: `anta`, `fine`, `hook`, `Hook`, `咫` (target ranks: base_value=72:70426, first_product=144:76687, bound_value=135:73985, second_product=270:77521, answer=256:81946)
- Layer 20: `足`, `重`, `扣`, `垂`, `abric` (target ranks: base_value=72:91, first_product=144:11223, bound_value=135:10062, second_product=270:7676, answer=256:10218)
- Layer 30: `68`, ` kahaboga`, ` pakig`, `69`, `去掉` (target ranks: base_value=72:98, first_product=144:5400, bound_value=135:1146, second_product=270:66, answer=256:1896)
- Layer 35: `270`, `271`, `269`, `260`, `262` (target ranks: base_value=72:5122, first_product=144:123352, bound_value=135:69396, second_product=270:1, answer=256:14)
- Layer 36: `256`, `244`, `255`, `260`, `iahy` (target ranks: base_value=72:56107, first_product=144:113191, bound_value=135:39366, second_product=270:11, answer=256:1)
- Layer 37: `256`, `iahy`, `244`, `255`, ` medief` (target ranks: base_value=72:79181, first_product=144:120808, bound_value=135:68487, second_product=270:24, answer=256:1)
- Layer 38: `256`, `244`, ` medief`, `255`, `246` (target ranks: base_value=72:109835, first_product=144:124021, bound_value=135:117510, second_product=270:131, answer=256:1)
- Layer 39: ` medief`, `256`, `枝条`, `tanle`, ` Polygon` (target ranks: base_value=72:114325, first_product=144:127848, bound_value=135:127442, second_product=270:25567, answer=256:2)
- Layer 40: ` talags`, `Ald`, `催`, ` ald`, ` itandi` (target ranks: base_value=72:109659, first_product=144:128144, bound_value=135:118178, second_product=270:47607, answer=256:131)
- Layer 41: ` .`, `条`, `当地时间`, `那两个`, `��` (target ranks: base_value=72:111538, first_product=144:124825, bound_value=135:112735, second_product=270:48572, answer=256:1630)

### Filler position 2 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=72:118232, first_product=144:115291, bound_value=135:115890, second_product=270:117642, answer=256:119981)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `挪` (target ranks: base_value=72:18182, first_product=144:34677, bound_value=135:28985, second_product=270:40588, answer=256:29783)
- Layer 20: ` .----`, `往常`, `oraly`, `ools`, `中书` (target ranks: base_value=72:128763, first_product=144:128225, bound_value=135:126034, second_product=270:129079, answer=256:125939)
- Layer 30: ` talags`, ` hilabihan`, ` pakig`, ` dekameters`, ` gilay` (target ranks: base_value=72:128702, first_product=144:126866, bound_value=135:89852, second_product=270:129172, answer=256:124411)
- Layer 35: ` hilabihan`, ` pakig`, ` .`, `滴水`, ` talags` (target ranks: base_value=72:126488, first_product=144:128271, bound_value=135:123117, second_product=270:128268, answer=256:127919)
- Layer 36: `幽`, ` talags`, `空空`, ` hilabihan`, `往外` (target ranks: base_value=72:110606, first_product=144:123469, bound_value=135:84120, second_product=270:118627, answer=256:118295)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, ` licensierad`, `aplenty` (target ranks: base_value=72:127877, first_product=144:128566, bound_value=135:121099, second_product=270:127849, answer=256:128145)
- Layer 38: ` .`, ` Erkännande`, `}<?`, `enclose`, ` nasod` (target ranks: base_value=72:126101, first_product=144:126418, bound_value=135:84932, second_product=270:119818, answer=256:126880)
- Layer 39: ` .`, `}<?`, ` .↵↵`, `�乐`, ` hilabihan` (target ranks: base_value=72:126408, first_product=144:124719, bound_value=135:71738, second_product=270:100650, answer=256:111344)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, ` assignment` (target ranks: base_value=72:101721, first_product=144:99651, bound_value=135:22402, second_product=270:52612, answer=256:51883)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` 。` (target ranks: base_value=72:50651, first_product=144:34891, bound_value=135:8528, second_product=270:8024, answer=256:4873)

### Filler position 3 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:122503, first_product=144:118463, bound_value=135:118653, second_product=270:120076, answer=256:122745)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=72:18389, first_product=144:34421, bound_value=135:27638, second_product=270:36662, answer=256:29682)
- Layer 20: `ait`, `忑`, `能被`, `ashi`, ` ternary` (target ranks: base_value=72:10258, first_product=144:34359, bound_value=135:27671, second_product=270:59253, answer=256:41671)
- Layer 30: `s`, ` Vo`, `�`, `平行`, ` unpack` (target ranks: base_value=72:28399, first_product=144:61503, bound_value=135:72746, second_product=270:114723, answer=256:112556)
- Layer 35: ` Vo`, ` variables`, ` variable`, ` vo`, ` Variables` (target ranks: base_value=72:13950, first_product=144:82369, bound_value=135:63815, second_product=270:94249, answer=256:112239)
- Layer 36: ` variables`, ` Vo`, ` definitions`, `变量的`, `calcul` (target ranks: base_value=72:28615, first_product=144:105863, bound_value=135:64120, second_product=270:103410, answer=256:108329)
- Layer 37: `variables`, `变量的`, `}<?`, ` variables`, `定义` (target ranks: base_value=72:59440, first_product=144:119114, bound_value=135:98855, second_product=270:117667, answer=256:120407)
- Layer 38: `}<?`, `oses`, `variables`, ` bases`, `基底` (target ranks: base_value=72:65826, first_product=144:121196, bound_value=135:84637, second_product=270:112555, answer=256:122551)
- Layer 39: ` sublim`, `}<?`, `无言`, `树叶`, ` Noruwega` (target ranks: base_value=72:70838, first_product=144:122178, bound_value=135:95173, second_product=270:124846, answer=256:119144)
- Layer 40: ` su`, ` ni`, `nipp`, `打发`, ` nip` (target ranks: base_value=72:25149, first_product=144:110149, bound_value=135:59951, second_product=270:124024, answer=256:89612)
- Layer 41: ` .`, `wo`, ` `, ` ,`, `<｜end▁of▁sentence｜>` (target ranks: base_value=72:33168, first_product=144:91984, bound_value=135:46754, second_product=270:108604, answer=256:47818)

### Filler position 4 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=72:122641, first_product=144:120225, bound_value=135:119966, second_product=270:120973, answer=256:123837)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=72:13628, first_product=144:27208, bound_value=135:22701, second_product=270:28403, answer=256:22361)
- Layer 20: `ait`, `cape`, `甸`, `幽`, `atile` (target ranks: base_value=72:10531, first_product=144:30096, bound_value=135:39535, second_product=270:41004, answer=256:33995)
- Layer 30: ` Niagara`, ` tap`, `tap`, `Tap`, ` Tap` (target ranks: base_value=72:108621, first_product=144:92690, bound_value=135:113749, second_product=270:115450, answer=256:103322)
- Layer 35: ` tap`, ` Niagara`, `Tap`, ` Tap`, `tap` (target ranks: base_value=72:90352, first_product=144:85979, bound_value=135:103850, second_product=270:89020, answer=256:102075)
- Layer 36: ` tap`, ` dynam`, `动态`, `Tap`, ` Niagara` (target ranks: base_value=72:69284, first_product=144:87495, bound_value=135:82663, second_product=270:74447, answer=256:79004)
- Layer 37: ` talags`, ` dynam`, `本题分析`, ` Niagara`, `动态` (target ranks: base_value=72:105214, first_product=144:95174, bound_value=135:110439, second_product=270:99134, answer=256:103759)
- Layer 38: `本题分析`, ` talags`, `actors`, `�`, `ofer` (target ranks: base_value=72:113176, first_product=144:110626, bound_value=135:110415, second_product=270:104485, answer=256:115406)
- Layer 39: ` talags`, `本题分析`, ` Nij`, `oug`, `romic` (target ranks: base_value=72:95000, first_product=144:111773, bound_value=135:113897, second_product=270:120203, answer=256:110420)
- Layer 40: ` talags`, `Question`, `提问`, ` Question`, `oug` (target ranks: base_value=72:68449, first_product=144:98842, bound_value=135:87234, second_product=270:114423, answer=256:87832)
- Layer 41: `Question`, ` .`, `提问`, ` Question`, `Answer` (target ranks: base_value=72:61527, first_product=144:79826, bound_value=135:64148, second_product=270:94856, answer=256:42264)

### Filler position 5 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=72:121634, first_product=144:119965, bound_value=135:119718, second_product=270:120022, answer=256:123364)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=72:15555, first_product=144:31864, bound_value=135:24645, second_product=270:30204, answer=256:24851)
- Layer 20: `幽`, `锁定`, `挪`, `cape`, `鞍` (target ranks: base_value=72:12945, first_product=144:37091, bound_value=135:32652, second_product=270:35053, answer=256:28085)
- Layer 30: ` tap`, `Tap`, ` Tap`, ` repetition`, `反复` (target ranks: base_value=72:26660, first_product=144:52189, bound_value=135:69526, second_product=270:65642, answer=256:60078)
- Layer 35: ` tap`, `Tap`, ` Tap`, ` repetition`, `推算` (target ranks: base_value=72:22893, first_product=144:67158, bound_value=135:80378, second_product=270:62801, answer=256:70224)
- Layer 36: `推算`, ` tap`, `acin`, `calcul`, `反复` (target ranks: base_value=72:38749, first_product=144:73743, bound_value=135:57916, second_product=270:58307, answer=256:55842)
- Layer 37: ` Zad`, `radesh`, `hemer`, `acos`, `冰冰` (target ranks: base_value=72:58239, first_product=144:80545, bound_value=135:84575, second_product=270:81931, answer=256:78207)
- Layer 38: `hemer`, ` Zad`, `}<?`, `覆`, `树叶` (target ranks: base_value=72:67162, first_product=144:86677, bound_value=135:71265, second_product=270:80480, answer=256:91116)
- Layer 39: `hemer`, `aharan`, `romic`, ` talags`, `东海` (target ranks: base_value=72:74419, first_product=144:113143, bound_value=135:100998, second_product=270:114686, answer=256:110233)
- Layer 40: ` nasod`, ` talags`, `pon`, `省略`, `ekak` (target ranks: base_value=72:29180, first_product=144:97356, bound_value=135:59552, second_product=270:104526, answer=256:93369)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, `省略`, ` `, ` ;` (target ranks: base_value=72:31858, first_product=144:76438, bound_value=135:37923, second_product=270:85911, answer=256:46175)

### Filler position 6 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=72:120640, first_product=144:119648, bound_value=135:119568, second_product=270:119517, answer=256:122976)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:13485, first_product=144:28563, bound_value=135:23294, second_product=270:26830, answer=256:21766)
- Layer 20: `答案`, ` answer`, ` unflagged`, `Answered`, `暂无` (target ranks: base_value=72:94311, first_product=144:92564, bound_value=135:66420, second_product=270:90016, answer=256:70356)
- Layer 30: `高明`, `推算`, `Sequ`, `turn`, `计算的` (target ranks: base_value=72:27881, first_product=144:35405, bound_value=135:45483, second_product=270:60322, answer=256:103404)
- Layer 35: ` Tw`, `acks`, `Tw`, ` Walker`, ` tw` (target ranks: base_value=72:4844, first_product=144:28739, bound_value=135:48450, second_product=270:26714, answer=256:52561)
- Layer 36: ` Tw`, ` tw`, `Tw`, `tw`, `acks` (target ranks: base_value=72:8748, first_product=144:46552, bound_value=135:40372, second_product=270:34616, answer=256:59166)
- Layer 37: ` Tw`, `acks`, ` tw`, `tw`, ` step` (target ranks: base_value=72:6632, first_product=144:64294, bound_value=135:54060, second_product=270:36096, answer=256:72053)
- Layer 38: ` Tw`, `tw`, ` tw`, ` Calculators`, `Tw` (target ranks: base_value=72:14166, first_product=144:71387, bound_value=135:60053, second_product=270:40097, answer=256:85140)
- Layer 39: `klar`, ` Rutherford`, ` nasod`, ` Fif`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=72:35578, first_product=144:118996, bound_value=135:113325, second_product=270:126516, answer=256:124195)
- Layer 40: ` nasod`, ` gihulagway`, ` su`, ` nip`, ` explanatory` (target ranks: base_value=72:24766, first_product=144:112110, bound_value=135:95885, second_product=270:126756, answer=256:121706)
- Layer 41: `<｜begin▁of▁file｜>`, `那两个`, `印书馆`, `aliation`, `ucher` (target ranks: base_value=72:109984, first_product=144:127328, bound_value=135:123599, second_product=270:128136, answer=256:126377)

### Filler position 7 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=72:120392, first_product=144:119171, bound_value=135:119217, second_product=270:118939, answer=256:122597)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12840, first_product=144:27983, bound_value=135:23012, second_product=270:26795, answer=256:21351)
- Layer 20: `锁定`, `挪`, `ait`, ` Walker`, `拆` (target ranks: base_value=72:8138, first_product=144:28852, bound_value=135:27006, second_product=270:29715, answer=256:29121)
- Layer 30: `算出`, `计算的`, `calcul`, `计算出`, `计算` (target ranks: base_value=72:9306, first_product=144:62837, bound_value=135:63518, second_product=270:86924, answer=256:116729)
- Layer 35: ` Tw`, ` calculate`, `calcul`, `计算的`, `Tw` (target ranks: base_value=72:3135, first_product=144:69328, bound_value=135:53409, second_product=270:51879, answer=256:81619)
- Layer 36: `calcul`, ` calculate`, `计算的`, `计算`, ` calculations` (target ranks: base_value=72:6103, first_product=144:93309, bound_value=135:50819, second_product=270:61186, answer=256:78140)
- Layer 37: `calcul`, `计算的`, ` calculations`, `计算`, `comput` (target ranks: base_value=72:7621, first_product=144:113870, bound_value=135:77073, second_product=270:90541, answer=256:98810)
- Layer 38: `calcul`, ` cál`, `comput`, ` calculations`, `计算的` (target ranks: base_value=72:33042, first_product=144:119016, bound_value=135:89766, second_product=270:100842, answer=256:116980)
- Layer 39: ` duc`, `duc`, ` Noruwega`, `东海`, `声响` (target ranks: base_value=72:39410, first_product=144:115712, bound_value=135:87239, second_product=270:121146, answer=256:111990)
- Layer 40: `duc`, ` su`, ` duc`, ` dup`, `dup` (target ranks: base_value=72:19347, first_product=144:101106, bound_value=135:61559, second_product=270:118753, answer=256:89667)
- Layer 41: `wo`, ` duc`, ` sublim`, `duc`, ` wo` (target ranks: base_value=72:27267, first_product=144:98119, bound_value=135:52182, second_product=270:109162, answer=256:58707)

### Filler position 8 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120573, first_product=144:119123, bound_value=135:119314, second_product=270:118939, answer=256:122526)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:11585, first_product=144:27909, bound_value=135:22526, second_product=270:26235, answer=256:21096)
- Layer 20: `ait`, ` Walker`, `挪`, `锁定`, `Walker` (target ranks: base_value=72:12492, first_product=144:31164, bound_value=135:35084, second_product=270:34783, answer=256:32841)
- Layer 30: ` Ni`, `Ni`, ` ni`, ` Su`, ` Niagara` (target ranks: base_value=72:56936, first_product=144:78667, bound_value=135:93951, second_product=270:115757, answer=256:125177)
- Layer 35: ` Su`, ` SU`, ` ni`, ` su`, ` Niagara` (target ranks: base_value=72:19224, first_product=144:69197, bound_value=135:72868, second_product=270:75975, answer=256:113834)
- Layer 36: ` ni`, ` su`, ` SU`, ` Su`, ` Niagara` (target ranks: base_value=72:25709, first_product=144:71750, bound_value=135:61410, second_product=270:79250, answer=256:104199)
- Layer 37: ` su`, ` Su`, ` ni`, ` SU`, ` Ni` (target ranks: base_value=72:49373, first_product=144:84554, bound_value=135:79404, second_product=270:113863, answer=256:122083)
- Layer 38: ` su`, ` Su`, ` SU`, ` SUV`, ` Nij` (target ranks: base_value=72:69861, first_product=144:90360, bound_value=135:71355, second_product=270:111920, answer=256:123812)
- Layer 39: ` Su`, ` su`, ` SU`, `-su`, `Su` (target ranks: base_value=72:75579, first_product=144:101933, bound_value=135:91485, second_product=270:123704, answer=256:123793)
- Layer 40: ` ni`, ` su`, `ni`, `nipp`, ` Ni` (target ranks: base_value=72:35516, first_product=144:88259, bound_value=135:65781, second_product=270:120299, answer=256:112674)
- Layer 41: ` su`, ` suc`, ` ni`, `鹉`, ` .` (target ranks: base_value=72:19893, first_product=144:78556, bound_value=135:46384, second_product=270:105512, answer=256:87626)

### Filler position 9 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120207, first_product=144:119204, bound_value=135:119337, second_product=270:118861, answer=256:122540)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=72:12058, first_product=144:29375, bound_value=135:23414, second_product=270:27589, answer=256:21619)
- Layer 20: `ait`, ` Walker`, `锁定`, `挪`, `Walker` (target ranks: base_value=72:15624, first_product=144:32107, bound_value=135:36838, second_product=270:39824, answer=256:32398)
- Layer 30: ` Ni`, `Ni`, ` ni`, ` Niagara`, ` NI` (target ranks: base_value=72:67940, first_product=144:77368, bound_value=135:100110, second_product=270:114816, answer=256:116807)
- Layer 35: ` ni`, ` Ni`, `Ni`, ` Niagara`, ` Su` (target ranks: base_value=72:46089, first_product=144:76285, bound_value=135:83195, second_product=270:84066, answer=256:106735)
- Layer 36: ` ni`, ` Ni`, ` Niagara`, ` Su`, ` NI` (target ranks: base_value=72:66751, first_product=144:91489, bound_value=135:83141, second_product=270:97383, answer=256:104960)
- Layer 37: ` Ni`, ` ni`, ` NI`, ` Nij`, `Ni` (target ranks: base_value=72:102384, first_product=144:104763, bound_value=135:108384, second_product=270:116686, answer=256:117216)
- Layer 38: ` Ni`, ` ni`, ` Nij`, ` NI`, `}<?` (target ranks: base_value=72:94103, first_product=144:88016, bound_value=135:92440, second_product=270:106544, answer=256:118669)
- Layer 39: ` Ni`, ` NI`, ` Nij`, ` ni`, `Ni` (target ranks: base_value=72:101754, first_product=144:101474, bound_value=135:106702, second_product=270:122761, answer=256:122325)
- Layer 40: ` ni`, `ni`, ` NI`, ` Ni`, `nipp` (target ranks: base_value=72:76472, first_product=144:90578, bound_value=135:89806, second_product=270:120489, answer=256:119387)
- Layer 41: ` ni`, `鹉`, ` .`, `acular`, `ffff` (target ranks: base_value=72:35280, first_product=144:68871, bound_value=135:53619, second_product=270:94217, answer=256:61953)

### Filler position 10 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120235, first_product=144:119399, bound_value=135:119568, second_product=270:119084, answer=256:122537)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11708, first_product=144:28700, bound_value=135:22877, second_product=270:26980, answer=256:21393)
- Layer 20: `能被`, ` Walker`, `ait`, `Walker`, `挪` (target ranks: base_value=72:4946, first_product=144:20793, bound_value=135:24504, second_product=270:25478, answer=256:20089)
- Layer 30: `135`, `鞍`, ` Lange`, `水土`, `反复` (target ranks: base_value=72:81, first_product=144:284, bound_value=135:1, second_product=270:11, answer=256:17800)
- Layer 35: `270`, `269`, `271`, `135`, `警戒` (target ranks: base_value=72:6183, first_product=144:75730, bound_value=135:4, second_product=270:1, answer=256:1366)
- Layer 36: `270`, `269`, `260`, `271`, ` proiektuak` (target ranks: base_value=72:25403, first_product=144:86512, bound_value=135:9, second_product=270:1, answer=256:164)
- Layer 37: `270`, `269`, `271`, `260`, `255` (target ranks: base_value=72:24940, first_product=144:76748, bound_value=135:8, second_product=270:1, answer=256:228)
- Layer 38: `270`, `269`, `260`, `255`, `271` (target ranks: base_value=72:68384, first_product=144:97353, bound_value=135:24, second_product=270:1, answer=256:47)
- Layer 39: `270`, `-ulo`, `cault`, `Giya`, `utu` (target ranks: base_value=72:106727, first_product=144:121269, bound_value=135:5804, second_product=270:1, answer=256:56)
- Layer 40: `270`, ` kinahabogang`, ` smoothing`, ` alternating`, `enclose` (target ranks: base_value=72:99693, first_product=144:125496, bound_value=135:13287, second_product=270:1, answer=256:291)
- Layer 41: `��`, ` alternating`, `这种事情`, ` .`, `那两个` (target ranks: base_value=72:112014, first_product=144:127730, bound_value=135:51637, second_product=270:29, answer=256:6524)

### Filler position 11 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120083, first_product=144:119907, bound_value=135:119980, second_product=270:119399, answer=256:122760)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:11797, first_product=144:28954, bound_value=135:22613, second_product=270:26403, answer=256:21446)
- Layer 20: ` smile`, `ait`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=72:13000, first_product=144:37139, bound_value=135:34366, second_product=270:39440, answer=256:29180)
- Layer 30: `提问`, `询问`, ` asked`, ` question`, `asked` (target ranks: base_value=72:18131, first_product=144:29330, bound_value=135:36589, second_product=270:91475, answer=256:73168)
- Layer 35: `询问`, `提问`, ` asked`, `asking`, `ask` (target ranks: base_value=72:11225, first_product=144:20446, bound_value=135:33446, second_product=270:56358, answer=256:52185)
- Layer 36: `询问`, `提问`, `asking`, ` asked`, `asked` (target ranks: base_value=72:31098, first_product=144:41220, bound_value=135:39981, second_product=270:77832, answer=256:67871)
- Layer 37: `提问`, `asking`, `询问`, ` question`, `asked` (target ranks: base_value=72:50289, first_product=144:51181, bound_value=135:58292, second_product=270:101554, answer=256:91965)
- Layer 38: `}<?`, `asking`, `ascar`, `覆`, `打磨` (target ranks: base_value=72:53219, first_product=144:50307, bound_value=135:36185, second_product=270:74837, answer=256:92255)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `�`, `ocyst`, `东海` (target ranks: base_value=72:59792, first_product=144:74635, bound_value=135:52449, second_product=270:91888, answer=256:101965)
- Layer 40: `šk`, `asking`, ` nasod`, `不急`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=72:15503, first_product=144:42672, bound_value=135:18497, second_product=270:86723, answer=256:87733)
- Layer 41: `鹉`, ` .`, `šk`, ` repeated`, `每次` (target ranks: base_value=72:7679, first_product=144:20829, bound_value=135:12115, second_product=270:69807, answer=256:39764)

### Filler position 12 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:119918, first_product=144:119690, bound_value=135:119780, second_product=270:119077, answer=256:122602)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11558, first_product=144:28505, bound_value=135:23105, second_product=270:26467, answer=256:21373)
- Layer 20: `锁定`, `ait`, ` smile`, ` Walker`, `挪` (target ranks: base_value=72:8275, first_product=144:26084, bound_value=135:28716, second_product=270:34171, answer=256:20911)
- Layer 30: `Tap`, ` resort`, `EDER`, `匹配`, ` Gol` (target ranks: base_value=72:433, first_product=144:2804, bound_value=135:14612, second_product=270:4186, answer=256:7370)
- Layer 35: `270`, `271`, `269`, ` matching`, ` Matching` (target ranks: base_value=72:573, first_product=144:40384, bound_value=135:27957, second_product=270:1, answer=256:28)
- Layer 36: `256`, `244`, `iahy`, `56`, `260` (target ranks: base_value=72:8452, first_product=144:25571, bound_value=135:21737, second_product=270:117, answer=256:1)
- Layer 37: `256`, ` Parehong`, `cault`, `pole`, ` Pole` (target ranks: base_value=72:27569, first_product=144:43976, bound_value=135:48228, second_product=270:456, answer=256:1)
- Layer 38: `256`, ` medief`, ` dekameters`, `406`, `-ulo` (target ranks: base_value=72:52618, first_product=144:67585, bound_value=135:112257, second_product=270:766, answer=256:1)
- Layer 39: `256`, ` medief`, `cault`, `irit`, `本题分析` (target ranks: base_value=72:113834, first_product=144:124550, bound_value=135:127669, second_product=270:8871, answer=256:1)
- Layer 40: ` dekameters`, ` postup`, `256`, `知之`, `irit` (target ranks: base_value=72:122228, first_product=144:126173, bound_value=135:125844, second_product=270:43056, answer=256:3)
- Layer 41: `��`, `此项`, `))))`, `也不必`, `本条例` (target ranks: base_value=72:99706, first_product=144:116198, bound_value=135:117409, second_product=270:29561, answer=256:18)

### Filler position 13 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:119920, first_product=144:119878, bound_value=135:119945, second_product=270:119253, answer=256:122708)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11783, first_product=144:28539, bound_value=135:23222, second_product=270:26452, answer=256:20924)
- Layer 20: `锁定`, `ait`, ` smile`, `鞍`, ` Walker` (target ranks: base_value=72:11146, first_product=144:30546, bound_value=135:26574, second_product=270:33434, answer=256:20277)
- Layer 30: `鞍`, ` tap`, `Tap`, ` Cogn`, `acin` (target ranks: base_value=72:453, first_product=144:5985, bound_value=135:7238, second_product=270:30696, answer=256:13270)
- Layer 35: ` tap`, `鞍`, `Tap`, `锁定`, `acin` (target ranks: base_value=72:367, first_product=144:7715, bound_value=135:3299, second_product=270:8301, answer=256:3343)
- Layer 36: `acin`, `aci`, ` tap`, `退出`, `特` (target ranks: base_value=72:1453, first_product=144:14818, bound_value=135:2011, second_product=270:15145, answer=256:2849)
- Layer 37: `ocyst`, `acin`, ` fat`, `冰冰`, `脂肪` (target ranks: base_value=72:16629, first_product=144:33828, bound_value=135:5976, second_product=270:6381, answer=256:730)
- Layer 38: `ocyst`, `}<?`, `下沉`, ` talags`, `解放` (target ranks: base_value=72:31743, first_product=144:44257, bound_value=135:31971, second_product=270:8938, answer=256:1756)
- Layer 39: `-ulo`, `hatic`, `ocyst`, `}<?`, `文字的` (target ranks: base_value=72:125239, first_product=144:126739, bound_value=135:119855, second_product=270:9234, answer=256:318)
- Layer 40: ` talags`, `语言文字`, `256`, ` drip`, `下沉` (target ranks: base_value=72:126611, first_product=144:128208, bound_value=135:123542, second_product=270:8586, answer=256:3)
- Layer 41: ` .`, `茶馆`, `))))`, `256`, `特` (target ranks: base_value=72:122852, first_product=144:126825, bound_value=135:118075, second_product=270:10110, answer=256:4)

### Filler position 14 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120279, first_product=144:119865, bound_value=135:120000, second_product=270:119261, answer=256:122727)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11051, first_product=144:27658, bound_value=135:22870, second_product=270:25721, answer=256:20293)
- Layer 20: `ait`, `锁定`, ` Walker`, ` smile`, ` LS` (target ranks: base_value=72:4898, first_product=144:17913, bound_value=135:19037, second_product=270:23195, answer=256:15750)
- Layer 30: `匹配`, `七十`, ` kahaboga`, `EDER`, `82` (target ranks: base_value=72:110, first_product=144:1984, bound_value=135:4934, second_product=270:844, answer=256:8934)
- Layer 35: `270`, `271`, `269`, `268`, `370` (target ranks: base_value=72:511, first_product=144:58129, bound_value=135:28657, second_product=270:1, answer=256:36)
- Layer 36: `256`, ` Parehong`, `244`, `56`, `260` (target ranks: base_value=72:18296, first_product=144:48749, bound_value=135:25356, second_product=270:22, answer=256:1)
- Layer 37: `256`, ` Parehong`, `yata`, `244`, `iahy` (target ranks: base_value=72:29470, first_product=144:62551, bound_value=135:38177, second_product=270:63, answer=256:1)
- Layer 38: `256`, ` medief`, `406`, ` Parehong`, `244` (target ranks: base_value=72:78272, first_product=144:89614, bound_value=135:119152, second_product=270:511, answer=256:1)
- Layer 39: `256`, ` medief`, `-ulo`, ` Parehong`, `irit` (target ranks: base_value=72:113469, first_product=144:122859, bound_value=135:127225, second_product=270:3913, answer=256:1)
- Layer 40: `催`, ` pressing`, `256`, ` dekameters`, ` lat` (target ranks: base_value=72:116305, first_product=144:127148, bound_value=135:125984, second_product=270:27612, answer=256:3)
- Layer 41: `说吧`, `那股`, `此项`, `癫�`, `那两个` (target ranks: base_value=72:99856, first_product=144:124700, bound_value=135:122177, second_product=270:31669, answer=256:46)

### Filler position 15 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120540, first_product=144:120226, bound_value=135:120345, second_product=270:119664, answer=256:122970)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10076, first_product=144:26815, bound_value=135:21935, second_product=270:24531, answer=256:19428)
- Layer 20: `ait`, `能被`, `锁定`, `拆`, ` Walker` (target ranks: base_value=72:6739, first_product=144:19976, bound_value=135:24989, second_product=270:23209, answer=256:17921)
- Layer 30: `72`, `七十二`, ` subtract`, ` subtracting`, ` seventy` (target ranks: base_value=72:1, first_product=144:26, bound_value=135:3804, second_product=270:19811, answer=256:94407)
- Layer 35: `135`, `七十二`, ` cart`, `72`, `acin` (target ranks: base_value=72:4, first_product=144:36, bound_value=135:1, second_product=270:16130, answer=256:109142)
- Layer 36: `135`, ` stabil`, `acin`, ` cart`, ` Wil` (target ranks: base_value=72:39, first_product=144:446, bound_value=135:1, second_product=270:15012, answer=256:100109)
- Layer 37: `135`, `}<?`, `Quintal`, `Kadaghanon`, ` doubled` (target ranks: base_value=72:158, first_product=144:1622, bound_value=135:1, second_product=270:60507, answer=256:124668)
- Layer 38: `135`, `}<?`, `本题分析`, ` doubled`, `Quintal` (target ranks: base_value=72:573, first_product=144:6841, bound_value=135:1, second_product=270:88459, answer=256:126986)
- Layer 39: `}<?`, `opters`, `ocyst`, `-ulo`, `135` (target ranks: base_value=72:5879, first_product=144:24566, bound_value=135:5, second_product=270:46125, answer=256:69261)
- Layer 40: `}<?`, `135`, `enclose`, `ASI`, `俯` (target ranks: base_value=72:23064, first_product=144:41811, bound_value=135:2, second_product=270:9024, answer=256:1489)
- Layer 41: ` .`, `omit`, `实在`, ` `, `温馨提示` (target ranks: base_value=72:18360, first_product=144:31354, bound_value=135:7, second_product=270:4289, answer=256:318)

### Filler position 16 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:120333, first_product=144:120229, bound_value=135:120370, second_product=270:119630, answer=256:122983)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11166, first_product=144:28046, bound_value=135:23259, second_product=270:25601, answer=256:20069)
- Layer 20: `ait`, `锁定`, `能被`, `幽`, ` Walker` (target ranks: base_value=72:7066, first_product=144:26347, bound_value=135:28571, second_product=270:28636, answer=256:21552)
- Layer 30: ` dy`, `Tap`, `adal`, `tap`, `羊` (target ranks: base_value=72:93, first_product=144:770, bound_value=135:94, second_product=270:74, answer=256:8396)
- Layer 35: `270`, `锁定`, ` orient`, ` lung`, `Ori` (target ranks: base_value=72:1279, first_product=144:52988, bound_value=135:2000, second_product=270:1, answer=256:7347)
- Layer 36: `270`, `255`, `285`, ` antibiotic`, `水土` (target ranks: base_value=72:8196, first_product=144:73757, bound_value=135:318, second_product=270:1, answer=256:25)
- Layer 37: `270`, `255`, ` fuzzy`, `285`, ` pess` (target ranks: base_value=72:15026, first_product=144:94292, bound_value=135:783, second_product=270:1, answer=256:629)
- Layer 38: `255`, `270`, `225`, `285`, `手柄` (target ranks: base_value=72:43385, first_product=144:106504, bound_value=135:2045, second_product=270:2, answer=256:92)
- Layer 39: `255`, `本题分析`, ` medief`, ` fuzzy`, ` smoothing` (target ranks: base_value=72:63162, first_product=144:121621, bound_value=135:73388, second_product=270:134, answer=256:19)
- Layer 40: `255`, ` kinahabogang`, ` smoothing`, `叹气`, `enclose` (target ranks: base_value=72:23302, first_product=144:100887, bound_value=135:35010, second_product=270:1565, answer=256:72)
- Layer 41: `255`, ` .`, `那两个`, ` waiting`, `此项` (target ranks: base_value=72:25267, first_product=144:102479, bound_value=135:54877, second_product=270:6079, answer=256:246)

### Filler position 17 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120565, first_product=144:120476, bound_value=135:120556, second_product=270:119828, answer=256:123035)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12613, first_product=144:29773, bound_value=135:23993, second_product=270:27372, answer=256:20777)
- Layer 20: `能被`, ` smile`, `距`, `ait`, `锁定` (target ranks: base_value=72:11531, first_product=144:34825, bound_value=135:27483, second_product=270:33528, answer=256:21110)
- Layer 30: `Skill`, `鞍`, `adal`, ` Skills`, `水土` (target ranks: base_value=72:129, first_product=144:1888, bound_value=135:100, second_product=270:185, answer=256:14460)
- Layer 35: `270`, `锁定`, ` labor`, `水土`, `羊` (target ranks: base_value=72:1060, first_product=144:63263, bound_value=135:1025, second_product=270:1, answer=256:9347)
- Layer 36: `270`, `负载`, `记载`, `水土`, `橙` (target ranks: base_value=72:7928, first_product=144:95705, bound_value=135:376, second_product=270:1, answer=256:976)
- Layer 37: `270`, ` smoothed`, `取向`, `打磨`, ` smoothing` (target ranks: base_value=72:11026, first_product=144:101144, bound_value=135:1591, second_product=270:1, answer=256:14419)
- Layer 38: `270`, `手柄`, `打磨`, ` optimistic`, ` smoothed` (target ranks: base_value=72:32878, first_product=144:112231, bound_value=135:2976, second_product=270:1, answer=256:11574)
- Layer 39: `}<?`, `-ulo`, `aharan`, `本题分析`, `270` (target ranks: base_value=72:73552, first_product=144:125843, bound_value=135:68799, second_product=270:5, answer=256:489)
- Layer 40: `}<?`, `enclose`, ` Spo`, `坏`, `记载` (target ranks: base_value=72:26466, first_product=144:118681, bound_value=135:47787, second_product=270:163, answer=256:590)
- Layer 41: `那两个`, ` .`, ` waiting`, `这两位`, `坏` (target ranks: base_value=72:33001, first_product=144:102991, bound_value=135:22067, second_product=270:241, answer=256:492)

### Filler position 18 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=72:120902, first_product=144:121385, bound_value=135:121350, second_product=270:120495, answer=256:123704)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12051, first_product=144:29114, bound_value=135:24329, second_product=270:26915, answer=256:20960)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` engaging` (target ranks: base_value=72:19554, first_product=144:40880, bound_value=135:41686, second_product=270:44559, answer=256:42130)
- Layer 30: ` SUV`, `算出`, ` Su`, `SUV`, ` SU` (target ranks: base_value=72:8011, first_product=144:52025, bound_value=135:53471, second_product=270:46011, answer=256:92659)
- Layer 35: ` SUV`, ` Su`, ` SU`, `SUV`, `外商投资` (target ranks: base_value=72:4829, first_product=144:53145, bound_value=135:50389, second_product=270:37705, answer=256:91071)
- Layer 36: ` SUV`, ` Su`, ` SU`, `SUV`, ` su` (target ranks: base_value=72:10120, first_product=144:67820, bound_value=135:40376, second_product=270:32533, answer=256:68363)
- Layer 37: `}<?`, ` SUV`, ` Su`, ` su`, `yv` (target ranks: base_value=72:14567, first_product=144:80796, bound_value=135:63765, second_product=270:62296, answer=256:99934)
- Layer 38: `}<?`, ` sublim`, ` su`, ` SUV`, `覆` (target ranks: base_value=72:17732, first_product=144:73966, bound_value=135:46758, second_product=270:57947, answer=256:102461)
- Layer 39: `}<?`, ` Su`, ` sublim`, ` su`, ` Suzanne` (target ranks: base_value=72:34983, first_product=144:91737, bound_value=135:69429, second_product=270:81375, answer=256:89992)
- Layer 40: `calcul`, ` su`, `šk`, ` sublim`, `的计算` (target ranks: base_value=72:3868, first_product=144:45660, bound_value=135:17666, second_product=270:44936, answer=256:20106)
- Layer 41: ` .`, `的计算`, ` sublim`, `acular`, `wo` (target ranks: base_value=72:805, first_product=144:19838, bound_value=135:4816, second_product=270:10793, answer=256:939)

### Filler position 19 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:120885, first_product=144:121433, bound_value=135:121472, second_product=270:120590, answer=256:123767)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11477, first_product=144:27817, bound_value=135:23574, second_product=270:25112, answer=256:20696)
- Layer 20: `ait`, `忑`, `锁定`, `能被`, ` Walker` (target ranks: base_value=72:14685, first_product=144:33714, bound_value=135:38287, second_product=270:40812, answer=256:32964)
- Layer 30: `acos`, ` rip`, ` Rees`, `yg`, ` consum` (target ranks: base_value=72:47741, first_product=144:103495, bound_value=135:99424, second_product=270:100378, answer=256:96030)
- Layer 35: ` tap`, `Tap`, ` rip`, ` Tap`, ` Wil` (target ranks: base_value=72:27719, first_product=144:93392, bound_value=135:74503, second_product=270:68505, answer=256:93735)
- Layer 36: ` zad`, ` tap`, ` rip`, ` drip`, ` Zad` (target ranks: base_value=72:22470, first_product=144:86000, bound_value=135:39937, second_product=270:53702, answer=256:74393)
- Layer 37: `}<?`, ` Zed`, `zat`, `zim`, ` sip` (target ranks: base_value=72:46212, first_product=144:101769, bound_value=135:59645, second_product=270:85971, answer=256:107305)
- Layer 38: `zat`, `}<?`, ` sip`, ` Zed`, `zv` (target ranks: base_value=72:76813, first_product=144:108251, bound_value=135:57294, second_product=270:102454, answer=256:110131)
- Layer 39: `zat`, ` Zed`, `zel`, `yel`, `}<?` (target ranks: base_value=72:87604, first_product=144:98981, bound_value=135:88385, second_product=270:88837, answer=256:70106)
- Layer 40: `zel`, `zat`, ` talags`, `zet`, `y` (target ranks: base_value=72:73928, first_product=144:83221, bound_value=135:62154, second_product=270:82774, answer=256:19018)
- Layer 41: `zel`, ` fum`, `zat`, `zac`, `zij` (target ranks: base_value=72:30109, first_product=144:28240, bound_value=135:5059, second_product=270:28388, answer=256:746)

### Filler position 20 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:120927, first_product=144:121623, bound_value=135:121546, second_product=270:120734, answer=256:123848)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11428, first_product=144:26962, bound_value=135:22980, second_product=270:24457, answer=256:19985)
- Layer 20: `ait`, `锁定`, ` Walker`, `拆`, `忑` (target ranks: base_value=72:9908, first_product=144:29118, bound_value=135:36953, second_product=270:36043, answer=256:30116)
- Layer 30: `acin`, `拆`, `acos`, `�`, ` tap` (target ranks: base_value=72:27890, first_product=144:39557, bound_value=135:56120, second_product=270:84902, answer=256:89893)
- Layer 35: `锁定`, `分解`, ` repetition`, `重复`, `羊` (target ranks: base_value=72:14702, first_product=144:36043, bound_value=135:44627, second_product=270:39211, answer=256:85622)
- Layer 36: `柿子`, `羊`, `分解`, `反复`, `重复` (target ranks: base_value=72:18313, first_product=144:40782, bound_value=135:27983, second_product=270:37659, answer=256:81553)
- Layer 37: `}<?`, `不急`, `班的`, `翻了`, `翻` (target ranks: base_value=72:49365, first_product=144:66179, bound_value=135:56468, second_product=270:80765, answer=256:122155)
- Layer 38: `}<?`, `不急`, `zat`, `打磨`, `冰冰` (target ranks: base_value=72:71522, first_product=144:97502, bound_value=135:67995, second_product=270:78481, answer=256:125861)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `打磨`, `ocyst`, `把事情` (target ranks: base_value=72:68534, first_product=144:97635, bound_value=135:61946, second_product=270:84081, answer=256:118265)
- Layer 40: `<｜begin▁of▁sentence｜>`, `下沉`, ` follow`, `heck`, `scr` (target ranks: base_value=72:19301, first_product=144:62135, bound_value=135:19159, second_product=270:54945, answer=256:99865)
- Layer 41: ` .`, ` `, `<｜end▁of▁sentence｜>`, ` .↵↵`, `有下列` (target ranks: base_value=72:11808, first_product=144:35762, bound_value=135:9558, second_product=270:18813, answer=256:42200)

### Filler position 21 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:121640, first_product=144:121838, bound_value=135:121826, second_product=270:121040, answer=256:124057)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11097, first_product=144:26621, bound_value=135:22280, second_product=270:24435, answer=256:18981)
- Layer 20: `能被`, `ait`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=72:11040, first_product=144:23556, bound_value=135:34279, second_product=270:32068, answer=256:18812)
- Layer 30: `acin`, ` dy`, `acos`, ` dilation`, `平行` (target ranks: base_value=72:67, first_product=144:185, bound_value=135:842, second_product=270:6622, answer=256:24410)
- Layer 35: `135`, `acin`, ` cart`, `分解`, ` tail` (target ranks: base_value=72:796, first_product=144:7244, bound_value=135:1, second_product=270:206, answer=256:26402)
- Layer 36: `135`, `acin`, ` cart`, `zyn`, `adal` (target ranks: base_value=72:7816, first_product=144:17196, bound_value=135:1, second_product=270:38, answer=256:25644)
- Layer 37: `135`, `}<?`, `Tinubdan`, `牺牲`, `放下` (target ranks: base_value=72:22914, first_product=144:37143, bound_value=135:1, second_product=270:702, answer=256:69311)
- Layer 38: `135`, `}<?`, `打磨`, `zat`, `放下` (target ranks: base_value=72:25968, first_product=144:49100, bound_value=135:1, second_product=270:173, answer=256:56242)
- Layer 39: `}<?`, `�`, `zat`, `opters`, `�` (target ranks: base_value=72:41258, first_product=144:91029, bound_value=135:26, second_product=270:6448, answer=256:18256)
- Layer 40: `}<?`, `omit`, `俯`, `arella`, ` twisted` (target ranks: base_value=72:24850, first_product=144:104467, bound_value=135:338, second_product=270:3412, answer=256:2879)
- Layer 41: ` .`, `omit`, ` spare`, `有的时候`, ` ;` (target ranks: base_value=72:44088, first_product=144:104566, bound_value=135:1535, second_product=270:6061, answer=256:2763)

### Filler position 22 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:121447, first_product=144:121981, bound_value=135:122014, second_product=270:121274, answer=256:124195)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:10324, first_product=144:26442, bound_value=135:21809, second_product=270:24303, answer=256:18551)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` smile` (target ranks: base_value=72:6209, first_product=144:16730, bound_value=135:26894, second_product=270:25058, answer=256:16813)
- Layer 30: `72`, `七十二`, `分解`, ` repeated`, ` Tw` (target ranks: base_value=72:1, first_product=144:94, bound_value=135:20270, second_product=270:22028, answer=256:83374)
- Layer 35: `72`, `144`, `七十二`, ` Tw`, ` twice` (target ranks: base_value=72:1, first_product=144:2, bound_value=135:3293, second_product=270:10224, answer=256:57305)
- Layer 36: ` repeated`, `ikuha`, `72`, `分解`, `翻` (target ranks: base_value=72:3, first_product=144:8, bound_value=135:4996, second_product=270:12958, answer=256:50175)
- Layer 37: ` doubling`, ` doubled`, `}<?`, ` doubles`, ` double` (target ranks: base_value=72:8, first_product=144:6, bound_value=135:13185, second_product=270:29504, answer=256:88237)
- Layer 38: `}<?`, ` doubling`, ` doubled`, ` doubles`, `-ulo` (target ranks: base_value=72:135, first_product=144:97, bound_value=135:28759, second_product=270:54368, answer=256:112325)
- Layer 39: `}<?`, ` doubling`, ` doubled`, `aharan`, `opters` (target ranks: base_value=72:1338, first_product=144:640, bound_value=135:35208, second_product=270:53600, answer=256:78705)
- Layer 40: ` su`, `arella`, ` sublim`, `坏`, `isis` (target ranks: base_value=72:5725, first_product=144:5471, bound_value=135:9019, second_product=270:23867, answer=256:26257)
- Layer 41: ` su`, ` .`, `arella`, ` `, `swer` (target ranks: base_value=72:5807, first_product=144:4169, bound_value=135:14381, second_product=270:23426, answer=256:14973)

### Filler position 23 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:121753, first_product=144:122210, bound_value=135:122288, second_product=270:121452, answer=256:124318)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=72:11319, first_product=144:28009, bound_value=135:22738, second_product=270:25804, answer=256:19224)
- Layer 20: ` smile`, `足`, `ait`, `锁定`, `幽` (target ranks: base_value=72:4508, first_product=144:16513, bound_value=135:17818, second_product=270:21722, answer=256:16669)
- Layer 30: `算出`, ` calculate`, `calcul`, `计算的`, `计算` (target ranks: base_value=72:4881, first_product=144:13293, bound_value=135:31962, second_product=270:56568, answer=256:55065)
- Layer 35: ` first`, `沃`, ` Tw`, ` Wo`, `第一步` (target ranks: base_value=72:5477, first_product=144:30242, bound_value=135:40948, second_product=270:53915, answer=256:59801)
- Layer 36: ` first`, `ikuha`, `calcul`, `第一步`, `first` (target ranks: base_value=72:8797, first_product=144:35339, bound_value=135:34445, second_product=270:45666, answer=256:39340)
- Layer 37: `wof`, ` first`, `calcul`, `坏`, `计算方法` (target ranks: base_value=72:14445, first_product=144:59616, bound_value=135:63527, second_product=270:76427, answer=256:74049)
- Layer 38: `wof`, ` Woolf`, `�`, ` Noruwega`, `东海` (target ranks: base_value=72:37832, first_product=144:73098, bound_value=135:61482, second_product=270:79205, answer=256:102622)
- Layer 39: `wof`, `东海`, ` Woolf`, `�`, ` duc` (target ranks: base_value=72:38325, first_product=144:70115, bound_value=135:73985, second_product=270:88816, answer=256:91040)
- Layer 40: ` first`, ` su`, `calcul`, `坏`, `的计算` (target ranks: base_value=72:5761, first_product=144:27137, bound_value=135:35594, second_product=270:58358, answer=256:50656)
- Layer 41: ` first`, ` wo`, ` su`, `wo`, `坏` (target ranks: base_value=72:427, first_product=144:10317, bound_value=135:7790, second_product=270:8935, answer=256:1794)

### Filler position 24 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122091, first_product=144:123065, bound_value=135:123029, second_product=270:122353, answer=256:124838)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=72:11173, first_product=144:28032, bound_value=135:23304, second_product=270:25879, answer=256:19218)
- Layer 20: `ait`, ` smile`, `挪`, `足`, `锁定` (target ranks: base_value=72:6429, first_product=144:21296, bound_value=135:25076, second_product=270:26830, answer=256:22207)
- Layer 30: ` Ni`, `Ni`, ` Niagara`, ` ni`, `ni` (target ranks: base_value=72:15261, first_product=144:16031, bound_value=135:23716, second_product=270:72470, answer=256:71777)
- Layer 35: ` Ni`, ` Niagara`, `Ni`, ` ni`, `ni` (target ranks: base_value=72:14561, first_product=144:34737, bound_value=135:40078, second_product=270:46283, answer=256:74996)
- Layer 36: ` Ni`, ` Niagara`, ` NI`, ` ni`, `忽略` (target ranks: base_value=72:25379, first_product=144:61986, bound_value=135:37020, second_product=270:51617, answer=256:74179)
- Layer 37: ` Ni`, ` Niagara`, ` NI`, `不急`, ` Nij` (target ranks: base_value=72:70015, first_product=144:105354, bound_value=135:81066, second_product=270:89310, answer=256:108754)
- Layer 38: `不急`, `}<?`, ` Ni`, ` Nij`, ` NI` (target ranks: base_value=72:70589, first_product=144:113231, bound_value=135:58815, second_product=270:87847, answer=256:111552)
- Layer 39: ` Ni`, ` Nij`, ` NI`, `}<?`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=72:56726, first_product=144:113298, bound_value=135:65554, second_product=270:97037, answer=256:112397)
- Layer 40: `不急`, `pac`, `坏`, ` uncovered`, `坏的` (target ranks: base_value=72:21708, first_product=144:87165, bound_value=135:37965, second_product=270:89371, answer=256:103532)
- Layer 41: `不急`, ` .`, ` uncovered`, ` uninter`, `矶` (target ranks: base_value=72:10873, first_product=144:75308, bound_value=135:20184, second_product=270:60300, answer=256:53626)

### Filler position 25 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122288, first_product=144:122772, bound_value=135:122803, second_product=270:121938, answer=256:124622)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12127, first_product=144:29784, bound_value=135:24850, second_product=270:27303, answer=256:20771)
- Layer 20: `足`, ` smile`, ` Walker`, ` LS`, `ait` (target ranks: base_value=72:4150, first_product=144:20193, bound_value=135:19246, second_product=270:17997, answer=256:18067)
- Layer 30: ` Tw`, `算出`, `Tw`, `计算的`, `第一步` (target ranks: base_value=72:5643, first_product=144:47646, bound_value=135:40979, second_product=270:49235, answer=256:57505)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, `TW` (target ranks: base_value=72:5227, first_product=144:72877, bound_value=135:53654, second_product=270:48597, answer=256:59887)
- Layer 36: ` Tw`, `ikuha`, `calcul`, `Tw`, `.tw` (target ranks: base_value=72:9195, first_product=144:86174, bound_value=135:42669, second_product=270:35841, answer=256:40530)
- Layer 37: `不加`, `calcul`, `comput`, `计算的`, `计算方法` (target ranks: base_value=72:34093, first_product=144:118466, bound_value=135:90284, second_product=270:82516, answer=256:79103)
- Layer 38: ` Noruwega`, ` Duc`, `不加`, `}<?`, ` duc` (target ranks: base_value=72:53608, first_product=144:113443, bound_value=135:83878, second_product=270:81294, answer=256:90521)
- Layer 39: ` su`, ` Noruwega`, ` duc`, ` sublim`, `东海` (target ranks: base_value=72:46738, first_product=144:96299, bound_value=135:68383, second_product=270:77178, answer=256:75689)
- Layer 40: ` su`, `calcul`, `计算的`, ` wo`, `算计` (target ranks: base_value=72:10231, first_product=144:59153, bound_value=135:22124, second_product=270:40894, answer=256:28856)
- Layer 41: `wo`, ` wo`, ` su`, `计算的`, ` ` (target ranks: base_value=72:2042, first_product=144:45037, bound_value=135:16469, second_product=270:23828, answer=256:13687)

### Filler position 26 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122474, first_product=144:123087, bound_value=135:123124, second_product=270:122288, answer=256:124910)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11627, first_product=144:28444, bound_value=135:23983, second_product=270:25408, answer=256:20000)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=72:6977, first_product=144:24119, bound_value=135:24653, second_product=270:25822, answer=256:24926)
- Layer 30: ` Ni`, ` Niagara`, ` ni`, ` labor`, `Ni` (target ranks: base_value=72:20029, first_product=144:66739, bound_value=135:61378, second_product=270:67553, answer=256:88904)
- Layer 35: ` ni`, `ni`, ` Ni`, ` labor`, ` repetition` (target ranks: base_value=72:38660, first_product=144:79276, bound_value=135:68685, second_product=270:64451, answer=256:103713)
- Layer 36: ` ni`, `ni`, ` stabil`, `留存`, ` riv` (target ranks: base_value=72:45057, first_product=144:84206, bound_value=135:43398, second_product=270:48322, answer=256:88997)
- Layer 37: ` NI`, ` Ni`, ` ni`, ` Nij`, `}<?` (target ranks: base_value=72:97481, first_product=144:118368, bound_value=135:87797, second_product=270:89542, answer=256:121554)
- Layer 38: ` Ni`, ` NI`, ` ni`, ` Nij`, `}<?` (target ranks: base_value=72:90484, first_product=144:105568, bound_value=135:76392, second_product=270:68473, answer=256:118845)
- Layer 39: ` NI`, ` Ni`, ` Nij`, ` ni`, `NI` (target ranks: base_value=72:82500, first_product=144:109232, bound_value=135:93604, second_product=270:95184, answer=256:119127)
- Layer 40: ` ni`, ` NI`, `ni`, ` Ni`, `NI` (target ranks: base_value=72:48493, first_product=144:92485, bound_value=135:52850, second_product=270:82565, answer=256:101158)
- Layer 41: ` ni`, `ffff`, `aci`, `奶茶`, ` wherever` (target ranks: base_value=72:17646, first_product=144:61041, bound_value=135:19301, second_product=270:39108, answer=256:50108)

### Filler position 27 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122196, first_product=144:123042, bound_value=135:123161, second_product=270:122289, answer=256:124865)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10904, first_product=144:26836, bound_value=135:22422, second_product=270:23162, answer=256:18955)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=72:10206, first_product=144:25475, bound_value=135:26218, second_product=270:27400, answer=256:25702)
- Layer 30: `分解`, `外商投资`, `沃`, `�`, `kah` (target ranks: base_value=72:24326, first_product=144:46922, bound_value=135:39182, second_product=270:52255, answer=256:84259)
- Layer 35: `分解`, `外商投资`, ` WO`, `kah`, ` Wo` (target ranks: base_value=72:24702, first_product=144:45855, bound_value=135:31086, second_product=270:41221, answer=256:75089)
- Layer 36: `分解`, `留存`, `otas`, ` WO`, `外商投资` (target ranks: base_value=72:27402, first_product=144:52271, bound_value=135:19800, second_product=270:31928, answer=256:62381)
- Layer 37: `}<?`, `分解`, `翻了`, `翻`, `ahabogang` (target ranks: base_value=72:54501, first_product=144:90275, bound_value=135:46306, second_product=270:69240, answer=256:105665)
- Layer 38: `}<?`, `osit`, `ses`, ` sublim`, `oses` (target ranks: base_value=72:87941, first_product=144:105356, bound_value=135:49765, second_product=270:74052, answer=256:117906)
- Layer 39: `}<?`, `osit`, ` sublim`, `oses`, ` Su` (target ranks: base_value=72:89259, first_product=144:105019, bound_value=135:86550, second_product=270:94842, answer=256:118612)
- Layer 40: `ses`, `osit`, ` sublim`, `分解`, `筋` (target ranks: base_value=72:62927, first_product=144:95339, bound_value=135:58630, second_product=270:81226, answer=256:104599)
- Layer 41: `šk`, `分解`, `ses`, ` `, `鹉` (target ranks: base_value=72:28848, first_product=144:61030, bound_value=135:36109, second_product=270:45804, answer=256:56298)

### Filler position 28 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122354, first_product=144:123453, bound_value=135:123488, second_product=270:122662, answer=256:125147)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:11187, first_product=144:27080, bound_value=135:22544, second_product=270:23300, answer=256:19172)
- Layer 20: `ait`, `能被`, ` Walker`, `Walker`, `ession` (target ranks: base_value=72:8738, first_product=144:20086, bound_value=135:24726, second_product=270:29748, answer=256:25826)
- Layer 30: ` kahaboga`, `adal`, `sms`, `79`, ` drip` (target ranks: base_value=72:255, first_product=144:2024, bound_value=135:2507, second_product=270:272, answer=256:4758)
- Layer 35: `270`, `271`, `269`, ` labour`, `370` (target ranks: base_value=72:2592, first_product=144:32478, bound_value=135:19473, second_product=270:1, answer=256:188)
- Layer 36: `256`, ` leisurely`, `56`, `270`, `244` (target ranks: base_value=72:26620, first_product=144:39049, bound_value=135:13104, second_product=270:4, answer=256:1)
- Layer 37: `256`, `方针`, `Kapunoang`, `洋洋`, ` membership` (target ranks: base_value=72:38919, first_product=144:48656, bound_value=135:19045, second_product=270:6, answer=256:1)
- Layer 38: `256`, `556`, `406`, `poly`, `方针` (target ranks: base_value=72:106775, first_product=144:96542, bound_value=135:71441, second_product=270:753, answer=256:1)
- Layer 39: `256`, `244`, `556`, `utu`, `856` (target ranks: base_value=72:124461, first_product=144:122052, bound_value=135:124822, second_product=270:2062, answer=256:1)
- Layer 40: `256`, `}<?`, `方针`, `spo`, `aldehyde` (target ranks: base_value=72:121943, first_product=144:126794, bound_value=135:115990, second_product=270:14591, answer=256:1)
- Layer 41: `256`, `))))`, `经营活动`, `来吧`, `)))` (target ranks: base_value=72:101070, first_product=144:116015, bound_value=135:84639, second_product=270:18114, answer=256:1)

### Filler position 29 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122231, first_product=144:123137, bound_value=135:123309, second_product=270:122313, answer=256:124980)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:11982, first_product=144:28560, bound_value=135:23325, second_product=270:24780, answer=256:19599)
- Layer 20: `锁定`, `ait`, ` smile`, `aty`, `啦啦` (target ranks: base_value=72:9097, first_product=144:24144, bound_value=135:25871, second_product=270:30233, answer=256:25403)
- Layer 30: ` Ni`, ` Niagara`, ` ni`, `Ni`, ` NI` (target ranks: base_value=72:31210, first_product=144:15146, bound_value=135:26604, second_product=270:97169, answer=256:70063)
- Layer 35: ` Niagara`, ` Ni`, ` ni`, `cape`, `Ni` (target ranks: base_value=72:26516, first_product=144:20767, bound_value=135:27701, second_product=270:66507, answer=256:64545)
- Layer 36: ` Niagara`, ` Ni`, `cape`, `留存`, `俯` (target ranks: base_value=72:35576, first_product=144:27924, bound_value=135:25208, second_product=270:72471, answer=256:62689)
- Layer 37: ` Ni`, ` Niagara`, ` Nij`, ` NI`, ` ni` (target ranks: base_value=72:63725, first_product=144:52035, bound_value=135:57164, second_product=270:109384, answer=256:95523)
- Layer 38: ` Ni`, ` Nij`, ` Niagara`, `}<?`, `冰冰` (target ranks: base_value=72:62007, first_product=144:63620, bound_value=135:57905, second_product=270:95006, answer=256:98206)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, ` Nij`, `ocyst`, ` Ni` (target ranks: base_value=72:67518, first_product=144:85438, bound_value=135:70311, second_product=270:101902, answer=256:109863)
- Layer 40: `坏`, `坏的`, `<｜begin▁of▁sentence｜>`, `俯`, `省略` (target ranks: base_value=72:23517, first_product=144:57799, bound_value=135:41028, second_product=270:80598, answer=256:84440)
- Layer 41: ` .`, `坏`, ` `, `从前`, `坏的` (target ranks: base_value=72:16055, first_product=144:37631, bound_value=135:24681, second_product=270:67618, answer=256:40815)

### Filler position 30 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=72:122465, first_product=144:123842, bound_value=135:123928, second_product=270:122937, answer=256:125466)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11325, first_product=144:27458, bound_value=135:22890, second_product=270:24301, answer=256:19037)
- Layer 20: `cape`, `ait`, ` smile`, ` LS`, `足` (target ranks: base_value=72:5672, first_product=144:16689, bound_value=135:18057, second_product=270:24679, answer=256:16248)
- Layer 30: ` kahaboga`, `eder`, `atan`, `鞍`, `cape` (target ranks: base_value=72:79, first_product=144:2881, bound_value=135:1693, second_product=270:244, answer=256:4043)
- Layer 35: `262`, `266`, ` drip`, `286`, ` kahaboga` (target ranks: base_value=72:3101, first_product=144:62206, bound_value=135:65306, second_product=270:8, answer=256:38)
- Layer 36: `262`, `244`, `286`, `256`, `246` (target ranks: base_value=72:21386, first_product=144:81031, bound_value=135:70547, second_product=270:47, answer=256:4)
- Layer 37: `262`, `244`, `interpret`, ` interpretive`, `248` (target ranks: base_value=72:40641, first_product=144:91046, bound_value=135:87928, second_product=270:294, answer=256:7)
- Layer 38: `262`, `244`, ` interpretive`, `interpret`, `256` (target ranks: base_value=72:80273, first_product=144:116983, bound_value=135:123669, second_product=270:1336, answer=256:5)
- Layer 39: `256`, `244`, `262`, `250`, `246` (target ranks: base_value=72:120560, first_product=144:123177, bound_value=135:128029, second_product=270:8353, answer=256:1)
- Layer 40: `256`, ` postup`, ` drip`, ` trough`, `}<?` (target ranks: base_value=72:109945, first_product=144:125888, bound_value=135:120802, second_product=270:25072, answer=256:1)
- Layer 41: `那两个`, `256`, ` .`, ` dekameters`, `那股` (target ranks: base_value=72:76367, first_product=144:107307, bound_value=135:102422, second_product=270:13604, answer=256:2)

### Filler position 31 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=72:122826, first_product=144:124299, bound_value=135:124304, second_product=270:123369, answer=256:125737)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10683, first_product=144:26861, bound_value=135:22648, second_product=270:24256, answer=256:18626)
- Layer 20: `锁定`, `鞍`, `ait`, ` smile`, ` wig` (target ranks: base_value=72:6645, first_product=144:19664, bound_value=135:18550, second_product=270:27169, answer=256:17113)
- Layer 30: ` tap`, `Tap`, `tap`, `回答`, ` answer` (target ranks: base_value=72:10180, first_product=144:35910, bound_value=135:41987, second_product=270:78808, answer=256:27280)
- Layer 35: ` tap`, ` answer`, `tap`, ` rational`, `Tap` (target ranks: base_value=72:4957, first_product=144:19673, bound_value=135:32030, second_product=270:57235, answer=256:23423)
- Layer 36: ` tap`, `Tap`, ` rational`, `tap`, ` Tap` (target ranks: base_value=72:4039, first_product=144:21106, bound_value=135:12423, second_product=270:46307, answer=256:14760)
- Layer 37: `rational`, ` rational`, ` Rational`, `radesh`, `冰冰` (target ranks: base_value=72:10472, first_product=144:32261, bound_value=135:25454, second_product=270:75633, answer=256:29542)
- Layer 38: `rational`, `}<?`, ` rational`, `ocyst`, `坏` (target ranks: base_value=72:15343, first_product=144:20855, bound_value=135:12485, second_product=270:44167, answer=256:23064)
- Layer 39: `ocyst`, `}<?`, `-ulo`, ` lenker`, `aharan` (target ranks: base_value=72:48584, first_product=144:60028, bound_value=135:57430, second_product=270:9557, answer=256:710)
- Layer 40: ` Answer`, `256`, `acular`, `Answer`, `坏` (target ranks: base_value=72:10338, first_product=144:41217, bound_value=135:28029, second_product=270:655, answer=256:2)
- Layer 41: `256`, `Answer`, ` .`, ` Answer`, `坏` (target ranks: base_value=72:9750, first_product=144:15821, bound_value=135:16658, second_product=270:241, answer=256:1)

### Filler position 32 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=72:122943, first_product=144:124502, bound_value=135:124516, second_product=270:123620, answer=256:125892)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10168, first_product=144:26590, bound_value=135:22603, second_product=270:24082, answer=256:17994)
- Layer 20: `锁定`, `ait`, `足`, ` Walker`, ` LS` (target ranks: base_value=72:5532, first_product=144:19174, bound_value=135:18094, second_product=270:20258, answer=256:15491)
- Layer 30: `询问`, `提问`, ` questions`, ` question`, ` asked` (target ranks: base_value=72:14209, first_product=144:50733, bound_value=135:51242, second_product=270:79736, answer=256:58707)
- Layer 35: `询问`, ` question`, `ask`, ` asking`, ` Question` (target ranks: base_value=72:10974, first_product=144:23893, bound_value=135:34913, second_product=270:39924, answer=256:27118)
- Layer 36: `询问`, ` question`, ` Question`, `Question`, `提问` (target ranks: base_value=72:17891, first_product=144:33942, bound_value=135:33592, second_product=270:37585, answer=256:21065)
- Layer 37: ` question`, ` Question`, ` final`, `提问`, `Question` (target ranks: base_value=72:33154, first_product=144:40311, bound_value=135:55442, second_product=270:55578, answer=256:36031)
- Layer 38: ` question`, `asking`, ` final`, ` target`, ` Question` (target ranks: base_value=72:39087, first_product=144:47728, bound_value=135:46099, second_product=270:39538, answer=256:39044)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` final`, `}<?`, `缠绕`, `明珠` (target ranks: base_value=72:32219, first_product=144:51740, bound_value=135:64157, second_product=270:46141, answer=256:51299)
- Layer 40: `asking`, `缠绕`, ` question`, ` final`, ` number` (target ranks: base_value=72:7886, first_product=144:38539, bound_value=135:29430, second_product=270:49743, answer=256:35931)
- Layer 41: `Question`, ` question`, ` Question`, ` number`, ` Number` (target ranks: base_value=72:3174, first_product=144:7698, bound_value=135:9887, second_product=270:21513, answer=256:4173)

### Filler position 33 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=72:123063, first_product=144:124381, bound_value=135:124420, second_product=270:123519, answer=256:125840)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10023, first_product=144:26271, bound_value=135:22723, second_product=270:24163, answer=256:18011)
- Layer 20: `ait`, ` Walker`, ` LS`, `LS`, `Walker` (target ranks: base_value=72:5432, first_product=144:16151, bound_value=135:20396, second_product=270:20442, answer=256:13414)
- Layer 30: `往外`, `尾`, `135`, `exerc`, ` eserc` (target ranks: base_value=72:20, first_product=144:45, bound_value=135:3, second_product=270:2517, answer=256:34307)
- Layer 35: `135`, ` cart`, ` tail`, `acin`, `射手` (target ranks: base_value=72:584, first_product=144:3405, bound_value=135:1, second_product=270:1382, answer=256:74980)
- Layer 36: `135`, ` cart`, ` Katz`, ` Goldstein`, `往外` (target ranks: base_value=72:2590, first_product=144:8902, bound_value=135:1, second_product=270:365, answer=256:51924)
- Layer 37: `135`, `}<?`, `射出`, `放下`, `Tinubdan` (target ranks: base_value=72:26426, first_product=144:37819, bound_value=135:1, second_product=270:1822, answer=256:93766)
- Layer 38: `135`, `}<?`, `射出`, ` Goldstein`, ` Tub` (target ranks: base_value=72:35809, first_product=144:48943, bound_value=135:1, second_product=270:3492, answer=256:91923)
- Layer 39: `135`, `}<?`, `ASI`, `�`, `明珠` (target ranks: base_value=72:30551, first_product=144:64438, bound_value=135:1, second_product=270:6049, answer=256:33245)
- Layer 40: `135`, `}<?`, ` su`, `amn`, `漏` (target ranks: base_value=72:5217, first_product=144:40733, bound_value=135:1, second_product=270:4123, answer=256:5947)
- Layer 41: `135`, ` su`, ` .`, `asu`, `然而` (target ranks: base_value=72:4822, first_product=144:42071, bound_value=135:1, second_product=270:6905, answer=256:5721)

### Filler position 34 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=72:123480, first_product=144:124834, bound_value=135:124908, second_product=270:123944, answer=256:126191)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:10102, first_product=144:26450, bound_value=135:22717, second_product=270:23966, answer=256:18022)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=72:8902, first_product=144:22620, bound_value=135:27352, second_product=270:29621, answer=256:18414)
- Layer 30: ` SUV`, `SUV`, ` Su`, ` SU`, ` su` (target ranks: base_value=72:4634, first_product=144:51105, bound_value=135:55837, second_product=270:46911, answer=256:70786)
- Layer 35: ` SUV`, ` Su`, `SUV`, ` SU`, ` su` (target ranks: base_value=72:2129, first_product=144:32360, bound_value=135:33603, second_product=270:26283, answer=256:46909)
- Layer 36: ` SUV`, ` Su`, ` SU`, `SUV`, ` su` (target ranks: base_value=72:2792, first_product=144:34574, bound_value=135:22003, second_product=270:18523, answer=256:26742)
- Layer 37: ` SUV`, ` Su`, ` su`, `SUV`, ` SU` (target ranks: base_value=72:8885, first_product=144:62555, bound_value=135:57302, second_product=270:40337, answer=256:53366)
- Layer 38: ` su`, ` SUV`, ` uv`, ` Su`, `}<?` (target ranks: base_value=72:7120, first_product=144:51163, bound_value=135:42163, second_product=270:34604, answer=256:69412)
- Layer 39: ` su`, ` sublim`, ` Su`, ` SUV`, `�` (target ranks: base_value=72:33982, first_product=144:93479, bound_value=135:91119, second_product=270:71329, answer=256:80775)
- Layer 40: ` su`, `ked`, `acular`, `漏`, `acl` (target ranks: base_value=72:5448, first_product=144:61522, bound_value=135:57938, second_product=270:44777, answer=256:23964)
- Layer 41: ` su`, `zij`, `Question`, `acular`, `Answer` (target ranks: base_value=72:979, first_product=144:31789, bound_value=135:20001, second_product=270:15772, answer=256:3763)

### Filler position 35 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=72:123444, first_product=144:124825, bound_value=135:124934, second_product=270:124001, answer=256:126150)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11506, first_product=144:28156, bound_value=135:23994, second_product=270:25301, answer=256:18995)
- Layer 20: `ait`, ` smile`, `ession`, `能被`, `幽` (target ranks: base_value=72:8172, first_product=144:27343, bound_value=135:27718, second_product=270:35544, answer=256:23380)
- Layer 30: ` Su`, ` SUV`, ` Sup`, ` SU`, ` su` (target ranks: base_value=72:14259, first_product=144:31201, bound_value=135:35703, second_product=270:62076, answer=256:89635)
- Layer 35: ` Su`, ` SU`, ` SUV`, ` su`, `分解` (target ranks: base_value=72:18610, first_product=144:36882, bound_value=135:35479, second_product=270:52658, answer=256:75368)
- Layer 36: ` Su`, ` SU`, `radesh`, ` SUV`, ` su` (target ranks: base_value=72:31832, first_product=144:47167, bound_value=135:25446, second_product=270:50165, answer=256:68977)
- Layer 37: `}<?`, `radesh`, ` su`, ` Su`, `放下` (target ranks: base_value=72:49391, first_product=144:77909, bound_value=135:63922, second_product=270:89078, answer=256:99347)
- Layer 38: `}<?`, `wof`, `取样`, `radesh`, `zat` (target ranks: base_value=72:72600, first_product=144:91658, bound_value=135:59920, second_product=270:85237, answer=256:111845)
- Layer 39: ` Su`, ` SU`, ` su`, ` Suk`, ` Suz` (target ranks: base_value=72:84792, first_product=144:93352, bound_value=135:84199, second_product=270:97878, answer=256:105374)
- Layer 40: `坏`, ` su`, `ascript`, ` w`, `坏的` (target ranks: base_value=72:33474, first_product=144:64539, bound_value=135:49545, second_product=270:78073, answer=256:65502)
- Layer 41: `坏`, ` su`, ` compounding`, ` compounded`, ` ` (target ranks: base_value=72:4994, first_product=144:19564, bound_value=135:10434, second_product=270:19004, answer=256:5096)

### Filler position 36 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=72:123542, first_product=144:124913, bound_value=135:125072, second_product=270:124127, answer=256:126202)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12490, first_product=144:29433, bound_value=135:25283, second_product=270:26007, answer=256:19603)
- Layer 20: `ession`, `能被`, ` smile`, `cape`, `ait` (target ranks: base_value=72:10086, first_product=144:30529, bound_value=135:24723, second_product=270:30284, answer=256:26861)
- Layer 30: ` Ni`, ` Niagara`, `Ni`, ` NI`, ` ni` (target ranks: base_value=72:39723, first_product=144:42026, bound_value=135:40856, second_product=270:89724, answer=256:85678)
- Layer 35: ` Ni`, ` Niagara`, ` NI`, `Ni`, ` ni` (target ranks: base_value=72:28090, first_product=144:37964, bound_value=135:40624, second_product=270:58420, answer=256:69716)
- Layer 36: ` Ni`, ` NI`, ` Niagara`, `尼亚`, ` Nij` (target ranks: base_value=72:53094, first_product=144:66922, bound_value=135:50647, second_product=270:73994, answer=256:82778)
- Layer 37: ` Nij`, ` Ni`, `}<?`, ` NI`, ` Niagara` (target ranks: base_value=72:84501, first_product=144:98624, bound_value=135:88427, second_product=270:111406, answer=256:110316)
- Layer 38: ` Nij`, ` Ni`, `}<?`, ` NI`, `zat` (target ranks: base_value=72:70607, first_product=144:95831, bound_value=135:70698, second_product=270:101780, answer=256:112600)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, ` Nij`, ` Ni`, `坏的` (target ranks: base_value=72:76945, first_product=144:105883, bound_value=135:79481, second_product=270:98905, answer=256:111250)
- Layer 40: `<｜begin▁of▁sentence｜>`, `坏`, `坏的`, ` nasod`, `坏了` (target ranks: base_value=72:24879, first_product=144:66189, bound_value=135:40324, second_product=270:72090, answer=256:88638)
- Layer 41: ` .`, `坏`, `鹃`, ` `, ` because` (target ranks: base_value=72:11023, first_product=144:38406, bound_value=135:14100, second_product=270:36915, answer=256:22143)

### Filler position 37 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=72:123778, first_product=144:125476, bound_value=135:125487, second_product=270:124585, answer=256:126484)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12626, first_product=144:30177, bound_value=135:26035, second_product=270:26939, answer=256:19990)
- Layer 20: `能被`, ` engaging`, `ait`, `sl`, `ätte` (target ranks: base_value=72:19545, first_product=144:51695, bound_value=135:49714, second_product=270:61456, answer=256:63441)
- Layer 30: ` Ni`, `Ni`, ` ni`, ` Niagara`, ` NI` (target ranks: base_value=72:45211, first_product=144:30967, bound_value=135:22750, second_product=270:83832, answer=256:83676)
- Layer 35: ` Ni`, ` NI`, ` ni`, `Ni`, ` Niagara` (target ranks: base_value=72:48802, first_product=144:48756, bound_value=135:36131, second_product=270:72032, answer=256:76444)
- Layer 36: ` Ni`, ` NI`, ` ni`, ` Niagara`, `Ni` (target ranks: base_value=72:52129, first_product=144:64142, bound_value=135:27115, second_product=270:64045, answer=256:62933)
- Layer 37: ` Ni`, ` NI`, ` Nij`, `Ni`, ` ni` (target ranks: base_value=72:98466, first_product=144:95069, bound_value=135:60775, second_product=270:108702, answer=256:94952)
- Layer 38: ` Ni`, ` Nij`, ` NI`, `Ni`, ` Niem` (target ranks: base_value=72:87800, first_product=144:105359, bound_value=135:55102, second_product=270:99692, answer=256:95135)
- Layer 39: ` Ni`, ` Nij`, ` NI`, `Ni`, ` ni` (target ranks: base_value=72:82971, first_product=144:107383, bound_value=135:78131, second_product=270:95629, answer=256:96947)
- Layer 40: ` Nij`, `不急`, `calcul`, `坏的`, ` consum` (target ranks: base_value=72:38695, first_product=144:86095, bound_value=135:46462, second_product=270:79410, answer=256:83316)
- Layer 41: `从前`, `坏`, `鹃`, ` .`, `步骤如下` (target ranks: base_value=72:21611, first_product=144:71421, bound_value=135:27007, second_product=270:48423, answer=256:26802)

### Filler position 38 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=72:123818, first_product=144:124887, bound_value=135:125000, second_product=270:124018, answer=256:126084)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11777, first_product=144:28859, bound_value=135:24726, second_product=270:25608, answer=256:19506)
- Layer 20: `ait`, `忑`, `能被`, ` engaging`, ` Walker` (target ranks: base_value=72:9860, first_product=144:34626, bound_value=135:33027, second_product=270:34290, answer=256:38946)
- Layer 30: `79`, ` kahaboga`, ` coloring`, ` dy`, `eder` (target ranks: base_value=72:305, first_product=144:7944, bound_value=135:797, second_product=270:87, answer=256:8449)
- Layer 35: `270`, `269`, `271`, ` waiting`, ` Zukunft` (target ranks: base_value=72:8048, first_product=144:95704, bound_value=135:33665, second_product=270:1, answer=256:292)
- Layer 36: `256`, `260`, `244`, `255`, `250` (target ranks: base_value=72:58603, first_product=144:103838, bound_value=135:20007, second_product=270:6, answer=256:1)
- Layer 37: `260`, `256`, `255`, `250`, `244` (target ranks: base_value=72:85362, first_product=144:114383, bound_value=135:37266, second_product=270:10, answer=256:2)
- Layer 38: `256`, `255`, `253`, `244`, `241` (target ranks: base_value=72:123426, first_product=144:127316, bound_value=135:103000, second_product=270:69, answer=256:1)
- Layer 39: `256`, `244`, `250`, `255`, `utu` (target ranks: base_value=72:117810, first_product=144:124771, bound_value=135:126784, second_product=270:4415, answer=256:1)
- Layer 40: ` dekameters`, ` loose`, `alde`, `方针`, ` foul` (target ranks: base_value=72:116027, first_product=144:127167, bound_value=135:113489, second_product=270:22386, answer=256:15)
- Layer 41: `那股`, ` dekameters`, `那两个`, ` waiting`, `那句话` (target ranks: base_value=72:90616, first_product=144:123327, bound_value=135:91748, second_product=270:27244, answer=256:25)

### Filler position 39 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=72:123570, first_product=144:125112, bound_value=135:125264, second_product=270:124275, answer=256:126311)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11238, first_product=144:27854, bound_value=135:23931, second_product=270:24659, answer=256:18854)
- Layer 20: `ait`, `锁定`, `能被`, `拆`, ` Walker` (target ranks: base_value=72:11054, first_product=144:23381, bound_value=135:19330, second_product=270:27515, answer=256:21672)
- Layer 30: `subt`, `sac`, ` riv`, `sl`, `79` (target ranks: base_value=72:109, first_product=144:1162, bound_value=135:2117, second_product=270:2574, answer=256:3385)
- Layer 35: `退出`, `eder`, `obin`, ` smile`, ` future` (target ranks: base_value=72:223, first_product=144:1234, bound_value=135:796, second_product=270:470, answer=256:653)
- Layer 36: `退出`, `custom`, `acin`, `aci`, ` sacrifice` (target ranks: base_value=72:1459, first_product=144:5478, bound_value=135:805, second_product=270:971, answer=256:493)
- Layer 37: `脂肪`, `}<?`, `在北京`, `polar`, ` Geographic` (target ranks: base_value=72:39684, first_product=144:32703, bound_value=135:6105, second_product=270:326, answer=256:88)
- Layer 38: `}<?`, ` mach`, `脂肪`, `tanle`, ` Geographic` (target ranks: base_value=72:57841, first_product=144:47441, bound_value=135:22841, second_product=270:807, answer=256:392)
- Layer 39: `-ulo`, `}<?`, `hatic`, `aharoa`, `polar` (target ranks: base_value=72:126067, first_product=144:124081, bound_value=135:115832, second_product=270:877, answer=256:17)
- Layer 40: `256`, `argon`, ` drip`, `elf`, `隐藏` (target ranks: base_value=72:126472, first_product=144:127767, bound_value=135:122992, second_product=270:527, answer=256:1)
- Layer 41: `256`, `步骤如下`, ` .`, ` waterfall`, ` waiting` (target ranks: base_value=72:120935, first_product=144:126667, bound_value=135:121094, second_product=270:6601, answer=256:1)

### Filler position 40 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=72:123976, first_product=144:125339, bound_value=135:125436, second_product=270:124577, answer=256:126427)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11465, first_product=144:28434, bound_value=135:24030, second_product=270:24905, answer=256:19402)
- Layer 20: `ait`, `锁定`, `鞍`, ` LS`, `能被` (target ranks: base_value=72:4923, first_product=144:13396, bound_value=135:13774, second_product=270:19588, answer=256:11890)
- Layer 30: `79`, `328`, ` kahaboga`, ` seventy`, `七十` (target ranks: base_value=72:218, first_product=144:911, bound_value=135:2479, second_product=270:98, answer=256:1544)
- Layer 35: `270`, `271`, `269`, `268`, `274` (target ranks: base_value=72:1390, first_product=144:48388, bound_value=135:10145, second_product=270:1, answer=256:68)
- Layer 36: `256`, ` Parehong`, `260`, `406`, `255` (target ranks: base_value=72:56206, first_product=144:48927, bound_value=135:3983, second_product=270:11, answer=256:1)
- Layer 37: `256`, ` Parehong`, `yata`, `255`, `260` (target ranks: base_value=72:74145, first_product=144:63593, bound_value=135:9050, second_product=270:16, answer=256:1)
- Layer 38: `256`, `406`, `255`, `yata`, ` Parehong` (target ranks: base_value=72:119633, first_product=144:111239, bound_value=135:81979, second_product=270:88, answer=256:1)
- Layer 39: `256`, ` medief`, `856`, `-ulo`, `cault` (target ranks: base_value=72:121260, first_product=144:124334, bound_value=135:125251, second_product=270:2838, answer=256:1)
- Layer 40: `256`, `oys`, `埋伏`, `<｜begin▁of▁file｜>`, `vat` (target ranks: base_value=72:114508, first_product=144:125658, bound_value=135:109238, second_product=270:12977, answer=256:1)
- Layer 41: `那股`, `�`, `ijs`, `说吧`, `来吧` (target ranks: base_value=72:97617, first_product=144:121714, bound_value=135:92850, second_product=270:40654, answer=256:34)

### Filler position 41 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=72:123613, first_product=144:124956, bound_value=135:125159, second_product=270:124139, answer=256:126235)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11931, first_product=144:29465, bound_value=135:24707, second_product=270:26002, answer=256:19802)
- Layer 20: `ait`, `锁定`, ` smile`, `能被`, `ätte` (target ranks: base_value=72:6839, first_product=144:23217, bound_value=135:25058, second_product=270:24450, answer=256:17924)
- Layer 30: ` kahaboga`, ` coloring`, `79`, `328`, ` seventy` (target ranks: base_value=72:200, first_product=144:3941, bound_value=135:22260, second_product=270:804, answer=256:5017)
- Layer 35: `270`, `271`, `370`, `269`, `itetsdata` (target ranks: base_value=72:1660, first_product=144:44337, bound_value=135:28548, second_product=270:1, answer=256:442)
- Layer 36: `256`, `56`, ` пуним`, ` Parehong`, `406` (target ranks: base_value=72:34079, first_product=144:26873, bound_value=135:3735, second_product=270:202, answer=256:1)
- Layer 37: `256`, ` Parehong`, ` Bates`, `406`, `856` (target ranks: base_value=72:47827, first_product=144:26283, bound_value=135:6066, second_product=270:283, answer=256:1)
- Layer 38: `256`, `56`, `856`, `556`, `406` (target ranks: base_value=72:88814, first_product=144:84689, bound_value=135:78372, second_product=270:1081, answer=256:1)
- Layer 39: `256`, `856`, `956`, `356`, ` medief` (target ranks: base_value=72:111230, first_product=144:119500, bound_value=135:120437, second_product=270:3401, answer=256:1)
- Layer 40: `256`, `vat`, `埋伏`, `odecimal`, `上当` (target ranks: base_value=72:100035, first_product=144:121308, bound_value=135:98478, second_product=270:18786, answer=256:1)
- Layer 41: `木齐`, `ijs`, ` Vigesimal`, ` milimetro`, `来吧` (target ranks: base_value=72:70948, first_product=144:99169, bound_value=135:56850, second_product=270:24532, answer=256:27)

### Filler position 42 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=72:123794, first_product=144:125087, bound_value=135:125271, second_product=270:124265, answer=256:126291)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12019, first_product=144:29935, bound_value=135:24915, second_product=270:26099, answer=256:19839)
- Layer 20: `锁定`, ` smile`, `cape`, `ession`, `鞍` (target ranks: base_value=72:5618, first_product=144:19587, bound_value=135:13846, second_product=270:18810, answer=256:10582)
- Layer 30: `iab`, `�`, ` smoot`, ` smooth`, `平滑` (target ranks: base_value=72:2797, first_product=144:49151, bound_value=135:23333, second_product=270:9376, answer=256:16592)
- Layer 35: `271`, `�`, ` Karn`, ` Hess`, ` reserved` (target ranks: base_value=72:10439, first_product=144:71970, bound_value=135:22729, second_product=270:386, answer=256:13250)
- Layer 36: `cault`, `�`, ` resting`, `内膜`, `坏` (target ranks: base_value=72:36070, first_product=144:81248, bound_value=135:6611, second_product=270:32681, answer=256:101)
- Layer 37: `cault`, `内膜`, `在北京`, `yai`, `文字的` (target ranks: base_value=72:67152, first_product=144:93513, bound_value=135:11338, second_product=270:76769, answer=256:986)
- Layer 38: ` medief`, `cault`, `本题分析`, `坏的`, `装箱` (target ranks: base_value=72:114210, first_product=144:118827, bound_value=135:23317, second_product=270:102388, answer=256:202)
- Layer 39: `256`, ` medief`, `本题分析`, `cault`, `-ulo` (target ranks: base_value=72:119378, first_product=144:125283, bound_value=135:94525, second_product=270:24615, answer=256:1)
- Layer 40: `256`, `潜伏`, `装箱`, `不急`, `inine` (target ranks: base_value=72:111975, first_product=144:118754, bound_value=135:46845, second_product=270:27571, answer=256:1)
- Layer 41: ` .`, `256`, `上面的`, ` waiting`, ` ` (target ranks: base_value=72:68759, first_product=144:80710, bound_value=135:26747, second_product=270:12495, answer=256:2)

### Filler position 43 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=72:123815, first_product=144:125158, bound_value=135:125397, second_product=270:124382, answer=256:126364)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11431, first_product=144:29770, bound_value=135:24798, second_product=270:25633, answer=256:19717)
- Layer 20: `LS`, ` LS`, `锁定`, `距`, `忑` (target ranks: base_value=72:5588, first_product=144:20845, bound_value=135:16550, second_product=270:17679, answer=256:13902)
- Layer 30: `iab`, `�`, `陪伴`, ` Lange`, `270` (target ranks: base_value=72:22, first_product=144:9421, bound_value=135:63, second_product=270:5, answer=256:10431)
- Layer 35: `270`, `269`, `271`, ` orient`, ` Karn` (target ranks: base_value=72:5209, first_product=144:107835, bound_value=135:866, second_product=270:1, answer=256:6627)
- Layer 36: `270`, `269`, `370`, `271`, `羽毛` (target ranks: base_value=72:6128, first_product=144:108858, bound_value=135:639, second_product=270:1, answer=256:1482)
- Layer 37: `270`, `269`, `370`, `271`, `770` (target ranks: base_value=72:7738, first_product=144:114705, bound_value=135:1941, second_product=270:1, answer=256:3527)
- Layer 38: `270`, `269`, `271`, `268`, ` geop` (target ranks: base_value=72:50459, first_product=144:118882, bound_value=135:4823, second_product=270:1, answer=256:142)
- Layer 39: `270`, `-ulo`, `cault`, `256`, ` Fuzzy` (target ranks: base_value=72:85359, first_product=144:123688, bound_value=135:56536, second_product=270:1, answer=256:4)
- Layer 40: `270`, `256`, `第二百`, ` Sage`, ` lat` (target ranks: base_value=72:49490, first_product=144:122768, bound_value=135:57895, second_product=270:1, answer=256:2)
- Layer 41: `270`, ` .`, `��`, `256`, `Answer` (target ranks: base_value=72:27917, first_product=144:109363, bound_value=135:45193, second_product=270:1, answer=256:4)

### Filler position 44 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=72:124038, first_product=144:125387, bound_value=135:125504, second_product=270:124625, answer=256:126406)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:11761, first_product=144:29651, bound_value=135:24845, second_product=270:25227, answer=256:20222)
- Layer 20: `忑`, `ait`, `能被`, `距`, ` Walker` (target ranks: base_value=72:6479, first_product=144:21545, bound_value=135:18322, second_product=270:19617, answer=256:16145)
- Layer 30: `72`, `七十二`, ` seventy`, ` Seventy`, ` twice` (target ranks: base_value=72:1, first_product=144:1215, bound_value=135:23045, second_product=270:62707, answer=256:97030)
- Layer 35: `72`, `七十二`, ` Tw`, ` twice`, ` seventy` (target ranks: base_value=72:1, first_product=144:4171, bound_value=135:13409, second_product=270:34001, answer=256:83370)
- Layer 36: `72`, `七十二`, ` Tw`, ` quadru`, ` doubling` (target ranks: base_value=72:1, first_product=144:16539, bound_value=135:10096, second_product=270:32638, answer=256:54902)
- Layer 37: ` doubling`, `72`, `七十二`, ` doubled`, ` doubles` (target ranks: base_value=72:2, first_product=144:34093, bound_value=135:22387, second_product=270:60374, answer=256:101940)
- Layer 38: ` doubling`, `}<?`, `七十二`, ` doubled`, `72` (target ranks: base_value=72:5, first_product=144:59113, bound_value=135:25214, second_product=270:71676, answer=256:109069)
- Layer 39: `}<?`, `urin`, `文字的`, `erer`, ` doubled` (target ranks: base_value=72:1245, first_product=144:71720, bound_value=135:17614, second_product=270:14078, answer=256:9097)
- Layer 40: ` su`, ` seventy`, ` fifty`, `二百`, `不急` (target ranks: base_value=72:1854, first_product=144:57758, bound_value=135:957, second_product=270:1398, answer=256:34)
- Layer 41: `256`, `不求`, ` su`, `沛`, ` number` (target ranks: base_value=72:442, first_product=144:13157, bound_value=135:111, second_product=270:243, answer=256:1)

### Filler position 45 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=72:124194, first_product=144:125645, bound_value=135:125776, second_product=270:124905, answer=256:126667)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=72:12718, first_product=144:29348, bound_value=135:24966, second_product=270:25392, answer=256:20210)
- Layer 20: `ait`, ` Walker`, `会成为`, `能被`, ` engaging` (target ranks: base_value=72:14216, first_product=144:31555, bound_value=135:27139, second_product=270:29368, answer=256:24264)
- Layer 30: ` SUV`, `SUV`, ` Su`, ` su`, ` SU` (target ranks: base_value=72:9820, first_product=144:98683, bound_value=135:65991, second_product=270:95882, answer=256:113923)
- Layer 35: ` Su`, ` SUV`, ` su`, ` SU`, `SUV` (target ranks: base_value=72:3309, first_product=144:79043, bound_value=135:38043, second_product=270:64680, answer=256:105064)
- Layer 36: ` su`, `留存`, ` SU`, ` Su`, ` SUV` (target ranks: base_value=72:2585, first_product=144:69743, bound_value=135:12590, second_product=270:35731, answer=256:54169)
- Layer 37: `}<?`, ` su`, ` sublim`, `不加`, ` SUV` (target ranks: base_value=72:20818, first_product=144:99665, bound_value=135:38057, second_product=270:75311, answer=256:105350)
- Layer 38: `}<?`, `东海`, ` su`, ` sublim`, `不加` (target ranks: base_value=72:17292, first_product=144:96444, bound_value=135:28515, second_product=270:58803, answer=256:100030)
- Layer 39: ` sublim`, `}<?`, `东海`, `文字的`, `迷惑` (target ranks: base_value=72:34038, first_product=144:97579, bound_value=135:46825, second_product=270:58280, answer=256:53944)
- Layer 40: ` su`, ` fifty`, ` seventy`, ` forty`, ` Seventy` (target ranks: base_value=72:2914, first_product=144:59911, bound_value=135:10020, second_product=270:25440, answer=256:4448)
- Layer 41: ` .`, ` fifty`, ` seventy`, ` `, `五十` (target ranks: base_value=72:697, first_product=144:22983, bound_value=135:2121, second_product=270:5883, answer=256:359)

### Filler position 46 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=72:123802, first_product=144:125231, bound_value=135:125443, second_product=270:124478, answer=256:126455)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=72:12674, first_product=144:28677, bound_value=135:24013, second_product=270:24808, answer=256:19621)
- Layer 20: ` adtong`, ` blanks`, `平行`, `俯`, `school` (target ranks: base_value=72:107084, first_product=144:92565, bound_value=135:76326, second_product=270:105542, answer=256:55650)
- Layer 30: ` spac`, `坝`, ` dekameters`, `?datasetId`, `}using` (target ranks: base_value=72:108903, first_product=144:98642, bound_value=135:70558, second_product=270:122804, answer=256:110141)
- Layer 35: `俯`, `足足`, `坏`, `滴水`, ` spac` (target ranks: base_value=72:62383, first_product=144:112011, bound_value=135:92678, second_product=270:111082, answer=256:101198)
- Layer 36: `俯`, `足足`, `ancock`, ` reduct`, `滴水` (target ranks: base_value=72:20773, first_product=144:91785, bound_value=135:49728, second_product=270:62948, answer=256:49568)
- Layer 37: `}<?`, `放下`, `俯`, `onana`, `放下了` (target ranks: base_value=72:75983, first_product=144:112635, bound_value=135:71820, second_product=270:86480, answer=256:84788)
- Layer 38: ` .`, `错过`, `俯`, `坏`, ` divers` (target ranks: base_value=72:38861, first_product=144:116417, bound_value=135:29605, second_product=270:51024, answer=256:79897)
- Layer 39: ` .`, `}<?`, `oxygen`, `ozygous`, `铎` (target ranks: base_value=72:67686, first_product=144:118830, bound_value=135:28446, second_product=270:12243, answer=256:35085)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` x`, ` .↵` (target ranks: base_value=72:20206, first_product=144:95588, bound_value=135:5239, second_product=270:3017, answer=256:17323)
- Layer 41: ` .`, ` .↵↵`, ` `, ` .↵`, ` ↵↵` (target ranks: base_value=72:17286, first_product=144:53819, bound_value=135:1432, second_product=270:536, answer=256:1791)

### Filler position 47 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=72:123864, first_product=144:125334, bound_value=135:125544, second_product=270:124563, answer=256:126547)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=72:12370, first_product=144:28457, bound_value=135:23601, second_product=270:24962, answer=256:19252)
- Layer 20: `}<?`, ` partly`, ` sideways`, `adaghan`, `锯` (target ranks: base_value=72:124453, first_product=144:112468, bound_value=135:108012, second_product=270:123396, answer=256:119053)
- Layer 30: `}<?`, `东京`, `dividers`, `codeline`, `lett` (target ranks: base_value=72:90893, first_product=144:94594, bound_value=135:94744, second_product=270:115769, answer=256:122713)
- Layer 35: `切割`, `lett`, `codeline`, `锯`, `浪费` (target ranks: base_value=72:82490, first_product=144:121005, bound_value=135:123565, second_product=270:117428, answer=256:122370)
- Layer 36: `锯`, `足足`, ` nasod`, `切割`, `ancock` (target ranks: base_value=72:36447, first_product=144:105336, bound_value=135:89571, second_product=270:77018, answer=256:98643)
- Layer 37: `磨损`, `东京`, `}<?`, `在东`, `الميل` (target ranks: base_value=72:79123, first_product=144:103537, bound_value=135:109154, second_product=270:71683, answer=256:94813)
- Layer 38: ` .`, `切割`, `lett`, `遁`, `收割` (target ranks: base_value=72:49580, first_product=144:108133, bound_value=135:56339, second_product=270:45307, answer=256:73740)
- Layer 39: ` .`, ` unflagged`, `磨损`, `lett`, `�` (target ranks: base_value=72:104676, first_product=144:117857, bound_value=135:47440, second_product=270:11095, answer=256:12170)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, `�` (target ranks: base_value=72:59736, first_product=144:91162, bound_value=135:12597, second_product=270:1458, answer=256:2459)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=72:24264, first_product=144:42644, bound_value=135:2939, second_product=270:135, answer=256:117)

### Filler position 48 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=72:123408, first_product=144:125023, bound_value=135:125258, second_product=270:124147, answer=256:126310)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=72:11925, first_product=144:28554, bound_value=135:23819, second_product=270:24954, answer=256:19290)
- Layer 20: `东海`, `aharoa`, ` instantaneous`, `}<?`, `)Skip` (target ranks: base_value=72:104404, first_product=144:85388, bound_value=135:100089, second_product=270:112305, answer=256:110759)
- Layer 30: `codeline`, `东京`, `lett`, `日产`, ` doubly` (target ranks: base_value=72:71764, first_product=144:113656, bound_value=135:74868, second_product=270:104136, answer=256:120861)
- Layer 35: `codeline`, ` nasod`, ` fif`, ` doubly`, ` soci` (target ranks: base_value=72:59237, first_product=144:125004, bound_value=135:110289, second_product=270:104125, answer=256:121746)
- Layer 36: ` nasod`, ` reduct`, ` soci`, `兜`, `yss` (target ranks: base_value=72:32693, first_product=144:115964, bound_value=135:67481, second_product=270:79992, answer=256:99171)
- Layer 37: `codeline`, `Quintal`, `TreeLabel`, `镶嵌`, `悬挂` (target ranks: base_value=72:116938, first_product=144:126946, bound_value=135:120242, second_product=270:88837, answer=256:106450)
- Layer 38: `悬挂`, `自闭`, ` .`, ` crev`, `肤` (target ranks: base_value=72:98659, first_product=144:124799, bound_value=135:93996, second_product=270:75299, answer=256:109188)
- Layer 39: ` encomp`, ` unflagged`, ` .`, ` .↵↵`, `贻` (target ranks: base_value=72:108997, first_product=144:125285, bound_value=135:93469, second_product=270:81939, answer=256:104249)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` nasod` (target ranks: base_value=72:100053, first_product=144:117844, bound_value=135:56743, second_product=270:60649, answer=256:81702)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=72:47655, first_product=144:53760, bound_value=135:15883, second_product=270:11429, answer=256:13199)

### Filler position 49 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=72:123917, first_product=144:125360, bound_value=135:125599, second_product=270:124685, answer=256:126537)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=72:12448, first_product=144:29601, bound_value=135:25094, second_product=270:26187, answer=256:20475)
- Layer 20: ` licensierad`, `aplenty`, `codeline`, ` instantaneous`, ` grounds` (target ranks: base_value=72:91130, first_product=144:80819, bound_value=135:86809, second_product=270:104539, answer=256:94282)
- Layer 30: ` Answer`, `答案是`, ` ответ`, ` answer`, `答案` (target ranks: base_value=72:95319, first_product=144:120218, bound_value=135:76008, second_product=270:102606, answer=256:106382)
- Layer 35: ` Answer`, `codeline`, `AED`, `oNames`, ` Antwort` (target ranks: base_value=72:82780, first_product=144:126822, bound_value=135:83702, second_product=270:80111, answer=256:104626)
- Layer 36: ` Answer`, `坏`, `停`, `停顿`, `绽` (target ranks: base_value=72:32924, first_product=144:121278, bound_value=135:41500, second_product=270:47017, answer=256:66536)
- Layer 37: `oNames`, `codeline`, ` consum`, `insic`, `orbic` (target ranks: base_value=72:109313, first_product=144:121864, bound_value=135:111749, second_product=270:110086, answer=256:117325)
- Layer 38: `oNames`, ` retard`, `<|EOT|>`, `�`, `оду` (target ranks: base_value=72:107685, first_product=144:120565, bound_value=135:105417, second_product=270:91303, answer=256:107669)
- Layer 39: `�`, `oxygen`, ` unflagged`, `-ulo`, `ต้` (target ranks: base_value=72:56632, first_product=144:116219, bound_value=135:109391, second_product=270:70159, answer=256:82563)
- Layer 40: ` Answer`, ` .`, ` .↵↵`, ` wink`, `Answer` (target ranks: base_value=72:5901, first_product=144:93055, bound_value=135:50723, second_product=270:21901, answer=256:16485)
- Layer 41: ` Answer`, `Answer`, ` .`, ` .↵↵`, ` twenty` (target ranks: base_value=72:2169, first_product=144:70975, bound_value=135:64270, second_product=270:11862, answer=256:5025)

### Filler position 50 (absolute token 845, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=72:120589, first_product=144:108473, bound_value=135:111560, second_product=270:109979, answer=256:115606)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, `aplenty` (target ranks: base_value=72:127165, first_product=144:106681, bound_value=135:110541, second_product=270:112322, answer=256:113984)
- Layer 20: `能被`, `ait`, `忑`, `坷`, `能吃` (target ranks: base_value=72:12629, first_product=144:42471, bound_value=135:57783, second_product=270:70256, answer=256:33403)
- Layer 30: ` dátummal`, `enment`, `nze`, ` unflagged`, ` الجرم` (target ranks: base_value=72:45631, first_product=144:17472, bound_value=135:31918, second_product=270:60826, answer=256:34783)
- Layer 35: `260`, `266`, `257`, `261`, `262` (target ranks: base_value=72:113612, first_product=144:121338, bound_value=135:84737, second_product=270:15, answer=256:14)
- Layer 36: `260`, `257`, `261`, `262`, `259` (target ranks: base_value=72:102585, first_product=144:117255, bound_value=135:43628, second_product=270:19, answer=256:15)
- Layer 37: `260`, `pole`, ` Paglin`, `257`, ` Pole` (target ranks: base_value=72:126408, first_product=144:124513, bound_value=135:86352, second_product=270:38, answer=256:19)
- Layer 38: `pole`, ` Paglin`, ` Whitehead`, `桃子`, `260` (target ranks: base_value=72:126076, first_product=144:124396, bound_value=135:100391, second_product=270:354, answer=256:33)
- Layer 39: `答案`, ` Answer`, ` Antwort`, ` answer`, ` Pole` (target ranks: base_value=72:123359, first_product=144:126475, bound_value=135:117556, second_product=270:4394, answer=256:99)
- Layer 40: ` Answer`, `Answer`, ` answer`, `_answer`, `answer` (target ranks: base_value=72:101222, first_product=144:124385, bound_value=135:83916, second_product=270:6380, answer=256:59)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=72:35703, first_product=144:102541, bound_value=135:57760, second_product=270:6966, answer=256:140)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>niw = 20
kog = 37
suv = 72
woh = twice the number for suv minus 9
voz = twice the number for woh minus 15
Question: What is twice the number for woh minus 14?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
