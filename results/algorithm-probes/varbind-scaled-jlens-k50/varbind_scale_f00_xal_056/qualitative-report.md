# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `271` (correct).
- No-filler answer: `295` (incorrect).
- Filler tokens: 50 tokens at absolute indices 801–850.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=56` | 1 (L24, filler 15) | L24, filler 15 (rank 1) |
| J-Lens | `first_product=112` | 1073 (L31, filler 15) | Never |
| J-Lens | `bound_value=126` | 1 (L30, filler 5) | L30, filler 5 (rank 1) |
| J-Lens | `second_product=252` | 1 (L32, filler 17) | L31, filler 5 (rank 2) |
| J-Lens | `answer=271` | 1 (L35, filler 20) | L31, filler 17 (rank 3) |
| Logit lens | `base_value=56` | 1 (L30, filler 16) | L25, filler 15 (rank 5) |
| Logit lens | `first_product=112` | 106 (L32, filler 41) | Never |
| Logit lens | `bound_value=126` | 1 (L30, filler 5) | L29, filler 28 (rank 3) |
| Logit lens | `second_product=252` | 1 (L31, filler 41) | L31, filler 5 (rank 8) |
| Logit lens | `answer=271` | 1 (L36, filler 21) | L34, filler 21 (rank 9) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 801, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=56:119296, first_product=112:111393, bound_value=126:109093, second_product=252:118041, answer=271:117147)
- Layer 10: `anta`, `fine`, `忑`, `钩`, `Hook` (target ranks: base_value=56:62583, first_product=112:74739, bound_value=126:72475, second_product=252:72524, answer=271:76662)
- Layer 20: `足`, `重`, ` LS`, `扣`, `abric` (target ranks: base_value=56:3037, first_product=112:24909, bound_value=126:31453, second_product=252:22448, answer=271:20150)
- Layer 30: ` pakig`, ` talags`, `期望`, ` calculator`, `calculator` (target ranks: base_value=56:2951, first_product=112:7536, bound_value=126:14430, second_product=252:6841, answer=271:1339)
- Layer 35: `期望`, `期盼`, `期待`, ` labor`, `期待的` (target ranks: base_value=56:17840, first_product=112:44374, bound_value=126:34516, second_product=252:2816, answer=271:6)
- Layer 36: `期盼`, `期望`, `295`, `271`, `期待的` (target ranks: base_value=56:63854, first_product=112:47712, bound_value=126:32444, second_product=252:2146, answer=271:4)
- Layer 37: `271`, `291`, `295`, `315`, `269` (target ranks: base_value=56:110635, first_product=112:55299, bound_value=126:37041, second_product=252:2818, answer=271:1)
- Layer 38: `291`, `295`, ` talags`, `}<?`, ` Noruwega` (target ranks: base_value=56:127762, first_product=112:97335, bound_value=126:82181, second_product=252:16390, answer=271:8)
- Layer 39: ` talags`, ` Nij`, ` Noruwega`, `叶子`, ` clam` (target ranks: base_value=56:127340, first_product=112:127129, bound_value=126:128147, second_product=252:91882, answer=271:33)
- Layer 40: ` talags`, ` Ald`, ` ald`, `Ald`, ` LD` (target ranks: base_value=56:125367, first_product=112:123474, bound_value=126:127395, second_product=252:67812, answer=271:24)
- Layer 41: ` .`, `我已经`, ` .↵↵`, `一个一个`, ` .↵` (target ranks: base_value=56:92154, first_product=112:103807, bound_value=126:122102, second_product=252:30766, answer=271:138)

### Filler position 2 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=56:120865, first_product=112:116732, bound_value=126:115514, second_product=252:121953, answer=271:119785)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=56:20705, first_product=112:40929, bound_value=126:42064, second_product=252:35248, answer=271:32905)
- Layer 20: ` .----`, `往常`, `oraly`, `ools`, `ophers` (target ranks: base_value=56:126710, first_product=112:127826, bound_value=126:127419, second_product=252:127930, answer=271:128593)
- Layer 30: ` talags`, ` hilabihan`, ` pakig`, ` gilay`, ` dekameters` (target ranks: base_value=56:115365, first_product=112:119211, bound_value=126:123947, second_product=252:118993, answer=271:127919)
- Layer 35: ` hilabihan`, ` talags`, ` pakig`, `密密`, `空空` (target ranks: base_value=56:120086, first_product=112:106464, bound_value=126:124380, second_product=252:122874, answer=271:122580)
- Layer 36: ` talags`, ` hilabihan`, `幽`, `空空`, `停` (target ranks: base_value=56:75409, first_product=112:71977, bound_value=126:97230, second_product=252:82082, answer=271:95720)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, `EDMF`, `�乐` (target ranks: base_value=56:119176, first_product=112:99377, bound_value=126:124645, second_product=252:119853, answer=271:125880)
- Layer 38: ` .`, `}<?`, ` Erkännande`, ` hilabihan`, `繁体` (target ranks: base_value=56:95270, first_product=112:84435, bound_value=126:118121, second_product=252:95168, answer=271:118730)
- Layer 39: ` .`, ` talags`, ` hilabihan`, `}<?`, ` .↵↵` (target ranks: base_value=56:91070, first_product=112:88592, bound_value=126:102462, second_product=252:74464, answer=271:94188)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` assignment` (target ranks: base_value=56:40899, first_product=112:38496, bound_value=126:55121, second_product=252:31461, answer=271:41149)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `忏` (target ranks: base_value=56:5855, first_product=112:6357, bound_value=126:13655, second_product=252:2340, answer=271:5908)

### Filler position 3 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124690, first_product=112:119862, bound_value=126:117634, second_product=252:123554, answer=271:121116)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=56:18135, first_product=112:30146, bound_value=126:36372, second_product=252:26561, answer=271:26196)
- Layer 20: `ait`, `Ta`, `ative`, `cape`, ` wig` (target ranks: base_value=56:3236, first_product=112:19806, bound_value=126:18134, second_product=252:11604, answer=271:18854)
- Layer 30: `计算出`, `算出`, ` calculating`, `计算的`, ` calculate` (target ranks: base_value=56:6580, first_product=112:41783, bound_value=126:64843, second_product=252:37284, answer=271:69877)
- Layer 35: `第一步`, `计算`, `计算的`, `calcul`, ` calculate` (target ranks: base_value=56:5534, first_product=112:41767, bound_value=126:60870, second_product=252:32516, answer=271:52430)
- Layer 36: `calcul`, `计算`, `计算的`, ` calculations`, ` calculate` (target ranks: base_value=56:7017, first_product=112:32514, bound_value=126:16215, second_product=252:12742, answer=271:49611)
- Layer 37: `计算`, `calcul`, `计算的`, ` calculations`, `计算方法` (target ranks: base_value=56:14614, first_product=112:47075, bound_value=126:25497, second_product=252:28232, answer=271:101941)
- Layer 38: ` Zem`, `}<?`, `calcul`, `计算`, `计算方法` (target ranks: base_value=56:50645, first_product=112:90043, bound_value=126:66435, second_product=252:77416, answer=271:114867)
- Layer 39: `淤泥`, `ked`, ` duc`, `无言`, `orten` (target ranks: base_value=56:15287, first_product=112:107387, bound_value=126:100030, second_product=252:87774, answer=271:126675)
- Layer 40: ` talags`, ` duc`, `zac`, `duc`, `zem` (target ranks: base_value=56:1585, first_product=112:88565, bound_value=126:76318, second_product=252:51868, answer=271:124892)
- Layer 41: ` .`, ` fifty`, `<｜end▁of▁sentence｜>`, ` zem`, ` repeated` (target ranks: base_value=56:775, first_product=112:76592, bound_value=126:28487, second_product=252:27599, answer=271:111089)

### Filler position 4 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:125016, first_product=112:120846, bound_value=126:119215, second_product=252:124205, answer=271:121812)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=56:13397, first_product=112:25879, bound_value=126:29774, second_product=252:20416, answer=271:21030)
- Layer 20: `ait`, `挪`, `cape`, `甸`, `足` (target ranks: base_value=56:11326, first_product=112:38856, bound_value=126:54573, second_product=252:32140, answer=271:38842)
- Layer 30: `提问`, ` tap`, `tap`, `Tap`, `期望` (target ranks: base_value=56:52953, first_product=112:52065, bound_value=126:110262, second_product=252:83173, answer=271:108161)
- Layer 35: ` tap`, `提问`, ` Niagara`, `Tap`, `tap` (target ranks: base_value=56:32416, first_product=112:55774, bound_value=126:114052, second_product=252:66441, answer=271:83217)
- Layer 36: `提问`, ` tap`, ` Zad`, `动态`, ` dynam` (target ranks: base_value=56:26372, first_product=112:39883, bound_value=126:77107, second_product=252:44009, answer=271:66601)
- Layer 37: ` talags`, ` Erkännande`, ` dynam`, `提问`, ` Zad` (target ranks: base_value=56:51144, first_product=112:58734, bound_value=126:87094, second_product=252:75236, answer=271:87119)
- Layer 38: ` talags`, `本题分析`, ` Erkännande`, `打磨`, `hemer` (target ranks: base_value=56:80166, first_product=112:98410, bound_value=126:107835, second_product=252:101243, answer=271:101521)
- Layer 39: ` talags`, `本题分析`, ` hilabihan`, ` spectator`, ` Nij` (target ranks: base_value=56:77080, first_product=112:100199, bound_value=126:118969, second_product=252:109290, answer=271:113167)
- Layer 40: ` talags`, `提问`, ` spectator`, `oug`, `Question` (target ranks: base_value=56:59455, first_product=112:72321, bound_value=126:110858, second_product=252:96374, answer=271:92264)
- Layer 41: ` .`, `Question`, `上证`, `提问`, ` last` (target ranks: base_value=56:41400, first_product=112:71769, bound_value=126:72743, second_product=252:65078, answer=271:71373)

### Filler position 5 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:124431, first_product=112:120787, bound_value=126:119446, second_product=252:124068, answer=271:121727)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: base_value=56:13577, first_product=112:27621, bound_value=126:31943, second_product=252:21544, answer=271:21903)
- Layer 20: `幽`, `能被`, ` LS`, `啦啦`, `挪` (target ranks: base_value=56:17239, first_product=112:32321, bound_value=126:49700, second_product=252:29400, answer=271:30020)
- Layer 30: `126`, `}<?`, ` corona`, `鞍`, `反复` (target ranks: base_value=56:169, first_product=112:2942, bound_value=126:1, second_product=252:96, answer=271:30471)
- Layer 35: `252`, `126`, `251`, ` Out`, `西瓜` (target ranks: base_value=56:12551, first_product=112:10041, bound_value=126:2, second_product=252:1, answer=271:20507)
- Layer 36: `252`, `126`, `251`, `253`, `西瓜` (target ranks: base_value=56:59935, first_product=112:12309, bound_value=126:2, second_product=252:1, answer=271:31106)
- Layer 37: `252`, `126`, `251`, `253`, `祭` (target ranks: base_value=56:87201, first_product=112:19370, bound_value=126:2, second_product=252:1, answer=271:45544)
- Layer 38: `252`, `126`, `251`, `253`, `祭` (target ranks: base_value=56:104386, first_product=112:20600, bound_value=126:2, second_product=252:1, answer=271:44550)
- Layer 39: `252`, `}<?`, `126`, ` turtles`, `ospor` (target ranks: base_value=56:119662, first_product=112:101488, bound_value=126:3, second_product=252:1, answer=271:73608)
- Layer 40: ` outp`, `252`, ` wr`, ` kinahabogang`, `elsk` (target ranks: base_value=56:123487, first_product=112:109468, bound_value=126:2136, second_product=252:2, answer=271:27182)
- Layer 41: ` .`, `有些不`, `omit`, `袄`, `出不穷` (target ranks: base_value=56:114959, first_product=112:119278, bound_value=126:6451, second_product=252:49, answer=271:79517)

### Filler position 6 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:124128, first_product=112:120463, bound_value=126:118914, second_product=252:123663, answer=271:121331)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:12770, first_product=112:25281, bound_value=126:29327, second_product=252:19510, answer=271:19784)
- Layer 20: ` unflagged`, `替换`, `答案是`, `答案`, `<｜begin▁of▁file｜>` (target ranks: base_value=56:102333, first_product=112:112412, bound_value=126:62004, second_product=252:58048, answer=271:88375)
- Layer 30: `高明`, `Sequ`, ` Tw`, `推算`, `turn` (target ranks: base_value=56:20040, first_product=112:34696, bound_value=126:14531, second_product=252:16643, answer=271:53853)
- Layer 35: ` Tw`, `acks`, `Tw`, `高明`, ` tw` (target ranks: base_value=56:6132, first_product=112:12082, bound_value=126:11288, second_product=252:5663, answer=271:27806)
- Layer 36: ` Tw`, `Tw`, ` tw`, `.tw`, ` TW` (target ranks: base_value=56:13283, first_product=112:15119, bound_value=126:6254, second_product=252:10529, answer=271:49830)
- Layer 37: ` Tw`, `Tw`, ` tw`, `tw`, ` TW` (target ranks: base_value=56:34251, first_product=112:24261, bound_value=126:9016, second_product=252:21408, answer=271:79129)
- Layer 38: ` Tw`, `Tw`, ` tw`, `tw`, ` TW` (target ranks: base_value=56:33960, first_product=112:24998, bound_value=126:8910, second_product=252:23284, answer=271:90578)
- Layer 39: `hemer`, ` Tw`, ` Dominic`, ` nasod`, `ophe` (target ranks: base_value=56:35005, first_product=112:108132, bound_value=126:85910, second_product=252:107285, answer=271:127624)
- Layer 40: ` Tw`, ` nasod`, `tw`, `省略`, ` twice` (target ranks: base_value=56:19926, first_product=112:102523, bound_value=126:67512, second_product=252:95162, answer=271:125663)
- Layer 41: ` .`, ` dotted`, ` dots`, `省略`, `ldots` (target ranks: base_value=56:58649, first_product=112:117438, bound_value=126:62937, second_product=252:99868, answer=271:124028)

### Filler position 7 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124193, first_product=112:120311, bound_value=126:118636, second_product=252:123487, answer=271:121152)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:12231, first_product=112:24293, bound_value=126:28338, second_product=252:18903, answer=271:20019)
- Layer 20: `锁定`, `ait`, ` Walker`, `挪`, `atable` (target ranks: base_value=56:11348, first_product=112:35802, bound_value=126:39530, second_product=252:28022, answer=271:26984)
- Layer 30: ` Zem`, `第一步`, `calcul`, ` zem`, `计算的` (target ranks: base_value=56:8333, first_product=112:46318, bound_value=126:90222, second_product=252:89265, answer=271:79795)
- Layer 35: ` Tw`, `Tw`, ` Zem`, ` zem`, `acks` (target ranks: base_value=56:10620, first_product=112:43322, bound_value=126:72298, second_product=252:68145, answer=271:46240)
- Layer 36: ` Zem`, ` Tw`, `calcul`, ` zem`, ` Zad` (target ranks: base_value=56:19191, first_product=112:40416, bound_value=126:39859, second_product=252:56414, answer=271:48138)
- Layer 37: ` Zem`, ` zem`, `calcul`, ` Zad`, `zem` (target ranks: base_value=56:28379, first_product=112:47052, bound_value=126:50929, second_product=252:88009, answer=271:90886)
- Layer 38: ` Zem`, ` zem`, `zem`, `}<?`, `zp` (target ranks: base_value=56:55251, first_product=112:73473, bound_value=126:78095, second_product=252:110631, answer=271:112550)
- Layer 39: ` spectator`, `}<?`, `金黄`, `script`, `殿堂` (target ranks: base_value=56:21055, first_product=112:73924, bound_value=126:86139, second_product=252:107019, answer=271:119585)
- Layer 40: ` talags`, ` spectator`, `acl`, `留存`, `段落` (target ranks: base_value=56:2718, first_product=112:44317, bound_value=126:47193, second_product=252:79727, answer=271:113306)
- Layer 41: `zac`, ` .`, `试一试`, ` fifty`, `叮` (target ranks: base_value=56:1489, first_product=112:36522, bound_value=126:14452, second_product=252:34474, answer=271:84658)

### Filler position 8 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124281, first_product=112:120418, bound_value=126:118497, second_product=252:123494, answer=271:121232)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11716, first_product=112:25310, bound_value=126:28908, second_product=252:19666, answer=271:20817)
- Layer 20: `ait`, `挪`, `锁定`, ` Walker`, `Walker` (target ranks: base_value=56:9698, first_product=112:29580, bound_value=126:42492, second_product=252:31337, answer=271:27851)
- Layer 30: `询问`, `提问`, ` asked`, `需要的`, `asked` (target ranks: base_value=56:9593, first_product=112:35170, bound_value=126:85194, second_product=252:72807, answer=271:76896)
- Layer 35: `询问`, ` question`, `提问`, ` quadr`, ` asked` (target ranks: base_value=56:5511, first_product=112:22710, bound_value=126:61160, second_product=252:43415, answer=271:37899)
- Layer 36: `询问`, ` question`, `提问`, ` asked`, ` Question` (target ranks: base_value=56:7893, first_product=112:26085, bound_value=126:42826, second_product=252:44940, answer=271:43784)
- Layer 37: ` question`, `提问`, ` Question`, `Question`, `询问` (target ranks: base_value=56:10497, first_product=112:26761, bound_value=126:61915, second_product=252:78826, answer=271:75659)
- Layer 38: ` question`, ` Question`, `殿堂`, `提问`, `Question` (target ranks: base_value=56:18789, first_product=112:40544, bound_value=126:71108, second_product=252:93282, answer=271:81663)
- Layer 39: `殿堂`, `script`, `.question`, ` question`, ` Question` (target ranks: base_value=56:23400, first_product=112:74141, bound_value=126:81777, second_product=252:105336, answer=271:101789)
- Layer 40: `acl`, `šk`, `殿堂`, `zij`, ` Tw` (target ranks: base_value=56:9872, first_product=112:28899, bound_value=126:48436, second_product=252:89040, answer=271:86921)
- Layer 41: `zac`, `zij`, ` .`, `袄`, `šk` (target ranks: base_value=56:4425, first_product=112:32472, bound_value=126:16869, second_product=252:56708, answer=271:59070)

### Filler position 9 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124564, first_product=112:120840, bound_value=126:118991, second_product=252:123833, answer=271:121542)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=56:12347, first_product=112:26111, bound_value=126:29919, second_product=252:20730, answer=271:21636)
- Layer 20: `ait`, ` Walker`, `挪`, `锁定`, `Walker` (target ranks: base_value=56:14436, first_product=112:33938, bound_value=126:48360, second_product=252:37517, answer=271:30900)
- Layer 30: ` Zem`, ` zem`, `zem`, ` zam`, ` Zam` (target ranks: base_value=56:33132, first_product=112:76216, bound_value=126:126374, second_product=252:125575, answer=271:90811)
- Layer 35: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=56:25344, first_product=112:61035, bound_value=126:117329, second_product=252:111447, answer=271:48109)
- Layer 36: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=56:35935, first_product=112:57439, bound_value=126:92304, second_product=252:100533, answer=271:58874)
- Layer 37: ` Zem`, ` zem`, `zem`, ` Zad`, ` Zel` (target ranks: base_value=56:77746, first_product=112:81700, bound_value=126:109335, second_product=252:120030, answer=271:101658)
- Layer 38: ` Zem`, `zem`, ` zem`, `zat`, `}<?` (target ranks: base_value=56:90053, first_product=112:99111, bound_value=126:109948, second_product=252:122729, answer=271:113269)
- Layer 39: ` Zem`, `zem`, ` zem`, `}<?`, `zam` (target ranks: base_value=56:86048, first_product=112:103186, bound_value=126:111777, second_product=252:122931, answer=271:117877)
- Layer 40: `acl`, `šk`, `amn`, `的计算`, `忍耐` (target ranks: base_value=56:26089, first_product=112:57224, bound_value=126:68538, second_product=252:102802, answer=271:115638)
- Layer 41: `鹉`, ` .`, `zac`, `acular`, `叮` (target ranks: base_value=56:4369, first_product=112:38668, bound_value=126:16519, second_product=252:50964, answer=271:75353)

### Filler position 10 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124437, first_product=112:120787, bound_value=126:118794, second_product=252:123764, answer=271:121479)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10886, first_product=112:24353, bound_value=126:27475, second_product=252:18768, answer=271:20065)
- Layer 20: `ait`, ` Walker`, `锁定`, `挪`, `Walker` (target ranks: base_value=56:13008, first_product=112:35482, bound_value=126:45504, second_product=252:37738, answer=271:32329)
- Layer 30: `alal`, `adal`, `平行`, ` parallel`, `鞍` (target ranks: base_value=56:1171, first_product=112:39587, bound_value=126:60151, second_product=252:92027, answer=271:57067)
- Layer 35: `alal`, `adal`, `Tap`, `羊`, ` tap` (target ranks: base_value=56:780, first_product=112:31019, bound_value=126:61676, second_product=252:62298, answer=271:28986)
- Layer 36: `adal`, `alal`, `acl`, `不急`, `留存` (target ranks: base_value=56:3524, first_product=112:43240, bound_value=126:61654, second_product=252:79836, answer=271:51125)
- Layer 37: `}<?`, `acl`, `enal`, `不急`, `amol` (target ranks: base_value=56:9399, first_product=112:62563, bound_value=126:84480, second_product=252:111260, answer=271:95741)
- Layer 38: `}<?`, `zat`, `zal`, `acl`, `enal` (target ranks: base_value=56:15481, first_product=112:74980, bound_value=126:76381, second_product=252:115419, answer=271:95450)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ocyst`, `hemer`, `zat` (target ranks: base_value=56:51019, first_product=112:102776, bound_value=126:104833, second_product=252:123516, answer=271:112546)
- Layer 40: `acl`, `<｜begin▁of▁sentence｜>`, `留存`, `šk`, `实在` (target ranks: base_value=56:29868, first_product=112:82592, bound_value=126:98885, second_product=252:121631, answer=271:112106)
- Layer 41: `鹉`, ` .`, `实在`, `zij`, `zac` (target ranks: base_value=56:15401, first_product=112:60349, bound_value=126:40603, second_product=252:87951, answer=271:67162)

### Filler position 11 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124410, first_product=112:120848, bound_value=126:118966, second_product=252:123830, answer=271:121610)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: base_value=56:10652, first_product=112:23881, bound_value=126:27418, second_product=252:18240, answer=271:19742)
- Layer 20: `锁定`, `ait`, ` smile`, `挪`, `幽` (target ranks: base_value=56:9374, first_product=112:24572, bound_value=126:34335, second_product=252:19518, answer=271:25067)
- Layer 30: `Tap`, ` tap`, ` Tap`, `鞍`, ` glacier` (target ranks: base_value=56:14984, first_product=112:38270, bound_value=126:64946, second_product=252:41918, answer=271:63527)
- Layer 35: ` tap`, `Tap`, ` Tap`, ` glacier`, `acks` (target ranks: base_value=56:11299, first_product=112:44365, bound_value=126:77700, second_product=252:41685, answer=271:55875)
- Layer 36: ` tap`, ` Zad`, ` drip`, ` zad`, `问候` (target ranks: base_value=56:21059, first_product=112:50780, bound_value=126:59122, second_product=252:44957, answer=271:69822)
- Layer 37: `}<?`, `acos`, ` Zad`, ` cargo`, ` Trib` (target ranks: base_value=56:37095, first_product=112:57444, bound_value=126:71126, second_product=252:73515, answer=271:101739)
- Layer 38: `}<?`, `�`, `�`, `ozygous`, `打磨` (target ranks: base_value=56:58533, first_product=112:88504, bound_value=126:88184, second_product=252:95999, answer=271:107382)
- Layer 39: `}<?`, `ozygous`, `hemer`, ` Nij`, `�` (target ranks: base_value=56:56728, first_product=112:100919, bound_value=126:102594, second_product=252:105254, answer=271:115761)
- Layer 40: `pac`, ` Zad`, `acl`, ` drip`, `zam` (target ranks: base_value=56:28483, first_product=112:68552, bound_value=126:82271, second_product=252:94682, answer=271:105381)
- Layer 41: `鹉`, `有下列`, ` .`, `叮`, `试一试` (target ranks: base_value=56:7922, first_product=112:44608, bound_value=126:23618, second_product=252:34689, answer=271:56178)

### Filler position 12 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124196, first_product=112:120655, bound_value=126:118725, second_product=252:123740, answer=271:121567)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:10968, first_product=112:24563, bound_value=126:28226, second_product=252:18474, answer=271:19594)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `挪` (target ranks: base_value=56:8573, first_product=112:31281, bound_value=126:36440, second_product=252:25711, answer=271:21851)
- Layer 30: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=56:8126, first_product=112:86976, bound_value=126:107642, second_product=252:113663, answer=271:62898)
- Layer 35: ` Zem`, ` zem`, ` zad`, ` Zad`, `zem` (target ranks: base_value=56:4667, first_product=112:73640, bound_value=126:84682, second_product=252:87867, answer=271:36535)
- Layer 36: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=56:12016, first_product=112:67607, bound_value=126:54158, second_product=252:96421, answer=271:52082)
- Layer 37: ` Zem`, ` zem`, `zem`, ` Zad`, `zel` (target ranks: base_value=56:26775, first_product=112:79007, bound_value=126:69175, second_product=252:114242, answer=271:84122)
- Layer 38: ` Zem`, `zem`, ` zem`, `zat`, `zal` (target ranks: base_value=56:52066, first_product=112:92896, bound_value=126:72506, second_product=252:121040, answer=271:103980)
- Layer 39: ` Zem`, `zem`, ` zem`, `zat`, `}<?` (target ranks: base_value=56:71121, first_product=112:93068, bound_value=126:83471, second_product=252:121555, answer=271:102604)
- Layer 40: `amol`, ` x`, ` pals`, `acl`, `留存` (target ranks: base_value=56:9896, first_product=112:43384, bound_value=126:35236, second_product=252:105663, answer=271:96724)
- Layer 41: `zij`, `zl`, `试一试`, `zel`, `从前` (target ranks: base_value=56:1561, first_product=112:33075, bound_value=126:6691, second_product=252:58264, answer=271:46743)

### Filler position 13 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124417, first_product=112:121108, bound_value=126:119238, second_product=252:124096, answer=271:121855)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11417, first_product=112:25609, bound_value=126:29209, second_product=252:19361, answer=271:19954)
- Layer 20: `锁定`, `ait`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=56:18817, first_product=112:41659, bound_value=126:55510, second_product=252:37309, answer=271:30576)
- Layer 30: ` Zem`, ` zem`, `acin`, `�`, `平行` (target ranks: base_value=56:8620, first_product=112:71650, bound_value=126:95075, second_product=252:97643, answer=271:82086)
- Layer 35: ` tap`, `锁定`, ` Tap`, `acin`, `Tap` (target ranks: base_value=56:4519, first_product=112:41808, bound_value=126:63542, second_product=252:50960, answer=271:33205)
- Layer 36: ` tap`, `adal`, `acin`, `留存`, ` Tap` (target ranks: base_value=56:5934, first_product=112:38554, bound_value=126:42719, second_product=252:47843, answer=271:41472)
- Layer 37: `}<?`, `翻`, `坏`, `殿堂`, `铎` (target ranks: base_value=56:18479, first_product=112:51434, bound_value=126:68873, second_product=252:88170, answer=271:94030)
- Layer 38: `}<?`, `铎`, `坏`, `殿堂`, `pac` (target ranks: base_value=56:28410, first_product=112:59979, bound_value=126:64022, second_product=252:98888, answer=271:93906)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `繁体`, `embl`, `ocyst` (target ranks: base_value=56:64692, first_product=112:100183, bound_value=126:100008, second_product=252:117936, answer=271:114632)
- Layer 40: `enclose`, ` nasod`, `坏`, `acl`, ` .` (target ranks: base_value=56:25490, first_product=112:64490, bound_value=126:67992, second_product=252:99625, answer=271:100996)
- Layer 41: ` .`, `鹉`, ` `, ` .↵↵`, ` :` (target ranks: base_value=56:7831, first_product=112:51276, bound_value=126:29892, second_product=252:47650, answer=271:61335)

### Filler position 14 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124550, first_product=112:121204, bound_value=126:119271, second_product=252:124139, answer=271:121964)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11055, first_product=112:24896, bound_value=126:28219, second_product=252:18962, answer=271:19640)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `会成为` (target ranks: base_value=56:14128, first_product=112:37060, bound_value=126:49434, second_product=252:40160, answer=271:37353)
- Layer 30: ` pakig`, `acos`, `算出`, `acin`, `alal` (target ranks: base_value=56:395, first_product=112:57342, bound_value=126:101554, second_product=252:117644, answer=271:109495)
- Layer 35: `adal`, `alal`, `antal`, `udal`, `aci` (target ranks: base_value=56:123, first_product=112:36815, bound_value=126:52761, second_product=252:73861, answer=271:78833)
- Layer 36: `adal`, `antal`, ` talags`, ` XCT`, ` tal` (target ranks: base_value=56:703, first_product=112:36975, bound_value=126:34484, second_product=252:78990, answer=271:98814)
- Layer 37: `}<?`, `geal`, `alc`, ` pals`, `Quintal` (target ranks: base_value=56:3502, first_product=112:43232, bound_value=126:51947, second_product=252:101479, answer=271:116764)
- Layer 38: `}<?`, `geal`, `zal`, ` pals`, `alc` (target ranks: base_value=56:5870, first_product=112:51912, bound_value=126:45409, second_product=252:102191, answer=271:115514)
- Layer 39: ` x`, `}<?`, ` Xavier`, ` XCT`, ` xyl` (target ranks: base_value=56:46195, first_product=112:80066, bound_value=126:89325, second_product=252:115381, answer=271:114938)
- Layer 40: ` x`, ` pals`, ` talags`, ` p`, `acl` (target ranks: base_value=56:11921, first_product=112:42937, bound_value=126:66701, second_product=252:108300, answer=271:108321)
- Layer 41: `鹉`, ` .`, `zij`, ` pals`, `zac` (target ranks: base_value=56:1347, first_product=112:37930, bound_value=126:15524, second_product=252:44840, answer=271:48220)

### Filler position 15 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:124754, first_product=112:121519, bound_value=126:119493, second_product=252:124343, answer=271:122135)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10679, first_product=112:24099, bound_value=126:27297, second_product=252:18257, answer=271:19239)
- Layer 20: `ait`, `锁定`, `能被`, `会成为`, ` LS` (target ranks: base_value=56:6881, first_product=112:26613, bound_value=126:31161, second_product=252:24990, answer=271:23246)
- Layer 30: `126`, `56`, `往外`, `反复`, `125` (target ranks: base_value=56:2, first_product=112:1349, bound_value=126:1, second_product=252:188, answer=271:28995)
- Layer 35: `126`, `252`, `梧桐`, `125`, `iram` (target ranks: base_value=56:343, first_product=112:2643, bound_value=126:1, second_product=252:2, answer=271:28106)
- Layer 36: `126`, `252`, `梧桐`, `253`, ` lesion` (target ranks: base_value=56:3748, first_product=112:4371, bound_value=126:1, second_product=252:2, answer=271:40738)
- Layer 37: `126`, `252`, `dividers`, `}<?`, `geries` (target ranks: base_value=56:14578, first_product=112:11640, bound_value=126:1, second_product=252:2, answer=271:75702)
- Layer 38: `126`, `252`, `dividers`, `结点的`, `geries` (target ranks: base_value=56:19972, first_product=112:12810, bound_value=126:1, second_product=252:2, answer=271:79360)
- Layer 39: `126`, ` doubles`, ` doubling`, `geries`, `}<?` (target ranks: base_value=56:29965, first_product=112:52072, bound_value=126:1, second_product=252:19, answer=271:90940)
- Layer 40: ` doubling`, ` doubles`, ` doubled`, ` outp`, ` Dou` (target ranks: base_value=56:24670, first_product=112:52465, bound_value=126:34, second_product=252:160, answer=271:48870)
- Layer 41: ` .`, `出不穷`, `况且`, ` outp`, `实在` (target ranks: base_value=56:21769, first_product=112:73918, bound_value=126:28, second_product=252:461, answer=271:61050)

### Filler position 16 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=56:125079, first_product=112:121945, bound_value=126:120025, second_product=252:124651, answer=271:122506)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11203, first_product=112:24906, bound_value=126:28112, second_product=252:18661, answer=271:19461)
- Layer 20: `ait`, `锁定`, ` smile`, `幽`, ` Walker` (target ranks: base_value=56:5859, first_product=112:26951, bound_value=126:34079, second_product=252:23036, answer=271:17666)
- Layer 30: `56`, `反复`, `粥`, `acin`, `鞍` (target ranks: base_value=56:1, first_product=112:2170, bound_value=126:31, second_product=252:5263, answer=271:16276)
- Layer 35: `126`, `56`, `acin`, ` reserve`, ` Reserve` (target ranks: base_value=56:2, first_product=112:1963, bound_value=126:1, second_product=252:155, answer=271:6214)
- Layer 36: `126`, `acin`, ` stabil`, `acy`, `往外` (target ranks: base_value=56:14, first_product=112:6443, bound_value=126:1, second_product=252:147, answer=271:15605)
- Layer 37: `126`, `}<?`, `ocyst`, ` doubles`, `师徒` (target ranks: base_value=56:229, first_product=112:16712, bound_value=126:1, second_product=252:2551, answer=271:57512)
- Layer 38: `126`, `}<?`, `ocyst`, `国王`, `geries` (target ranks: base_value=56:763, first_product=112:28801, bound_value=126:1, second_product=252:7944, answer=271:59062)
- Layer 39: `}<?`, `ocyst`, `acons`, ` doubles`, `东海` (target ranks: base_value=56:5443, first_product=112:77854, bound_value=126:3573, second_product=252:80780, answer=271:77209)
- Layer 40: `知识点`, `osit`, ` pals`, `radesh`, ` Fifty` (target ranks: base_value=56:1933, first_product=112:45772, bound_value=126:2582, second_product=252:38152, answer=271:27160)
- Layer 41: ` .`, `知识点`, ` fifty`, `没有什么`, ` Fifty` (target ranks: base_value=56:1404, first_product=112:75310, bound_value=126:3026, second_product=252:40681, answer=271:48750)

### Filler position 17 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:124939, first_product=112:121709, bound_value=126:119753, second_product=252:124456, answer=271:122383)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11283, first_product=112:25256, bound_value=126:28896, second_product=252:19167, answer=271:19928)
- Layer 20: `锁定`, ` smile`, `幽`, `ait`, `而此时` (target ranks: base_value=56:7479, first_product=112:22061, bound_value=126:33621, second_product=252:17890, answer=271:13681)
- Layer 30: `acos`, `Difficulty`, `翻`, ` Difficulty`, ` усили` (target ranks: base_value=56:519, first_product=112:5982, bound_value=126:4078, second_product=252:1499, answer=271:76)
- Layer 35: `252`, `271`, `251`, `295`, `267` (target ranks: base_value=56:18316, first_product=112:38448, bound_value=126:106846, second_product=252:1, answer=271:2)
- Layer 36: `271`, `272`, `273`, `274`, `270` (target ranks: base_value=56:110815, first_product=112:7084, bound_value=126:125937, second_product=252:16, answer=271:1)
- Layer 37: `271`, `272`, `273`, `uker`, `274` (target ranks: base_value=56:123619, first_product=112:16820, bound_value=126:123228, second_product=252:18, answer=271:1)
- Layer 38: `271`, `272`, `273`, `270`, `ukiran` (target ranks: base_value=56:129196, first_product=112:59788, bound_value=126:129034, second_product=252:1361, answer=271:1)
- Layer 39: `271`, `272`, `本题分析`, `(migrations`, `uker` (target ranks: base_value=56:128923, first_product=112:127904, bound_value=126:129261, second_product=252:90565, answer=271:1)
- Layer 40: `271`, ` kinahabogang`, `ekak`, `uker`, `aldehyde` (target ranks: base_value=56:128477, first_product=112:128225, bound_value=126:128577, second_product=252:102255, answer=271:1)
- Layer 41: `271`, ` nuest`, `(migrations`, `等待`, `olkien` (target ranks: base_value=56:126937, first_product=112:128152, bound_value=126:128281, second_product=252:102565, answer=271:1)

### Filler position 18 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125258, first_product=112:122428, bound_value=126:120570, second_product=252:124983, answer=271:122896)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10677, first_product=112:24688, bound_value=126:28330, second_product=252:18907, answer=271:19722)
- Layer 20: `ait`, ` Walker`, `忑`, `会成为`, `锁定` (target ranks: base_value=56:15069, first_product=112:40207, bound_value=126:51131, second_product=252:42521, answer=271:34940)
- Layer 30: ` Tw`, `算出`, `Tw`, ` calculator`, ` resolve` (target ranks: base_value=56:2456, first_product=112:31396, bound_value=126:46441, second_product=252:75686, answer=271:76155)
- Layer 35: ` resolve`, ` Tw`, ` resolves`, `Tw`, `resolve` (target ranks: base_value=56:5527, first_product=112:34057, bound_value=126:57176, second_product=252:79159, answer=271:49200)
- Layer 36: ` Tw`, `calcul`, `计算的`, ` resolves`, ` resolve` (target ranks: base_value=56:3850, first_product=112:23925, bound_value=126:23957, second_product=252:68622, answer=271:35910)
- Layer 37: `calcul`, `}<?`, `referent`, `计算的`, ` Nij` (target ranks: base_value=56:13325, first_product=112:53883, bound_value=126:44249, second_product=252:112937, answer=271:88323)
- Layer 38: `}<?`, ` RES`, ` Res`, `referent`, `-res` (target ranks: base_value=56:24383, first_product=112:68661, bound_value=126:62353, second_product=252:117659, answer=271:86942)
- Layer 39: ` Res`, ` RES`, `<｜begin▁of▁sentence｜>`, ` Resident`, `-res` (target ranks: base_value=56:13160, first_product=112:89487, bound_value=126:61060, second_product=252:114161, answer=271:85575)
- Layer 40: `殿堂`, `šk`, `acl`, ` Tw`, `留存` (target ranks: base_value=56:2185, first_product=112:25300, bound_value=126:21922, second_product=252:86340, answer=271:56327)
- Layer 41: ` .`, ` `, ` dotted`, `不求`, ` twist` (target ranks: base_value=56:750, first_product=112:33683, bound_value=126:9182, second_product=252:51832, answer=271:43859)

### Filler position 19 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125367, first_product=112:122622, bound_value=126:120731, second_product=252:125057, answer=271:123062)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10700, first_product=112:23970, bound_value=126:27328, second_product=252:18449, answer=271:19692)
- Layer 20: `忑`, ` Walker`, `ait`, ` engaging`, `能被` (target ranks: base_value=56:14242, first_product=112:41905, bound_value=126:56731, second_product=252:48896, answer=271:42782)
- Layer 30: ` pakig`, `oze`, `sar`, `?datasetId`, ` xor` (target ranks: base_value=56:26273, first_product=112:113802, bound_value=126:125870, second_product=252:125085, answer=271:108286)
- Layer 35: ` riv`, ` vib`, ` tap`, `清楚楚`, `zim` (target ranks: base_value=56:16454, first_product=112:102465, bound_value=126:125493, second_product=252:109997, answer=271:90471)
- Layer 36: ` riv`, ` vib`, ` zad`, `zim`, ` tap` (target ranks: base_value=56:16186, first_product=112:76820, bound_value=126:110770, second_product=252:105372, answer=271:92501)
- Layer 37: `Quintal`, `amol`, `斐`, `zim`, `oze` (target ranks: base_value=56:43123, first_product=112:85581, bound_value=126:120426, second_product=252:119470, answer=271:120533)
- Layer 38: `zat`, `}<?`, `斐`, `ked`, `本题分析` (target ranks: base_value=56:72225, first_product=112:90257, bound_value=126:120707, second_product=252:117072, answer=271:120249)
- Layer 39: `斐`, ` Nij`, `Quintal`, `ked`, `�` (target ranks: base_value=56:70583, first_product=112:69346, bound_value=126:119182, second_product=252:111058, answer=271:102624)
- Layer 40: `y`, `zim`, `zel`, `zat`, `zij` (target ranks: base_value=56:54101, first_product=112:78190, bound_value=126:116911, second_product=252:104828, answer=271:93542)
- Layer 41: `zel`, `zij`, ` mim`, `zet`, `zion` (target ranks: base_value=56:8260, first_product=112:46829, bound_value=126:33963, second_product=252:42773, answer=271:33106)

### Filler position 20 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125505, first_product=112:122659, bound_value=126:120722, second_product=252:125132, answer=271:123134)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11018, first_product=112:23374, bound_value=126:26733, second_product=252:18284, answer=271:19279)
- Layer 20: `ait`, `能被`, ` engaging`, ` Walker`, `锁定` (target ranks: base_value=56:6191, first_product=112:25052, bound_value=126:38028, second_product=252:29946, answer=271:19443)
- Layer 30: ` pakig`, ` kahaboga`, ` Mim`, `acos`, `slide` (target ranks: base_value=56:733, first_product=112:10197, bound_value=126:2283, second_product=252:1182, answer=271:313)
- Layer 35: `271`, `Dip`, `252`, ` unfolded`, `陌生` (target ranks: base_value=56:6737, first_product=112:24812, bound_value=126:107673, second_product=252:3, answer=271:1)
- Layer 36: `271`, `272`, `273`, `274`, `黄花` (target ranks: base_value=56:38104, first_product=112:2831, bound_value=126:118951, second_product=252:1802, answer=271:1)
- Layer 37: `271`, `272`, `371`, `273`, `galan` (target ranks: base_value=56:64855, first_product=112:7309, bound_value=126:110096, second_product=252:3839, answer=271:1)
- Layer 38: `271`, `272`, `371`, `270`, `273` (target ranks: base_value=56:127146, first_product=112:60368, bound_value=126:128040, second_product=252:39247, answer=271:1)
- Layer 39: `271`, `(migrations`, ` dátummal`, `urin`, `/Tropical` (target ranks: base_value=56:128323, first_product=112:126824, bound_value=126:128714, second_product=252:107139, answer=271:1)
- Layer 40: `271`, ` dátummal`, ` kinahabogang`, `uker`, `gies` (target ranks: base_value=56:128361, first_product=112:126548, bound_value=126:128346, second_product=252:98029, answer=271:1)
- Layer 41: `271`, ` dátummal`, ` nuest`, `(migrations`, `erat` (target ranks: base_value=56:119761, first_product=112:122136, bound_value=126:126371, second_product=252:90095, answer=271:1)

### Filler position 21 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125956, first_product=112:123241, bound_value=126:121461, second_product=252:125575, answer=271:123707)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10398, first_product=112:22598, bound_value=126:26316, second_product=252:18037, answer=271:18708)
- Layer 20: `ait`, `锁定`, `距`, `拆`, `能被` (target ranks: base_value=56:11819, first_product=112:24185, bound_value=126:45147, second_product=252:27941, answer=271:21693)
- Layer 30: `分解`, `aci`, `acos`, ` consuming`, ` reserved` (target ranks: base_value=56:362, first_product=112:4585, bound_value=126:4249, second_product=252:3518, answer=271:4494)
- Layer 35: `锁定`, `271`, `295`, `282`, ` drip` (target ranks: base_value=56:1561, first_product=112:15728, bound_value=126:119447, second_product=252:176, answer=271:2)
- Layer 36: `271`, `281`, `272`, `282`, `274` (target ranks: base_value=56:10116, first_product=112:3474, bound_value=126:107015, second_product=252:1649, answer=271:1)
- Layer 37: `271`, `281`, `272`, `282`, `274` (target ranks: base_value=56:36251, first_product=112:6275, bound_value=126:104583, second_product=252:3795, answer=271:1)
- Layer 38: `271`, `281`, `278`, `282`, `287` (target ranks: base_value=56:61523, first_product=112:52357, bound_value=126:118357, second_product=252:17012, answer=271:1)
- Layer 39: `271`, `281`, `看书`, ` Rutherford`, `}<?` (target ranks: base_value=56:103659, first_product=112:112471, bound_value=126:127682, second_product=252:97452, answer=271:1)
- Layer 40: `271`, `abd`, `ekak`, `ching`, `vil` (target ranks: base_value=56:112403, first_product=112:104484, bound_value=126:126687, second_product=252:80808, answer=271:1)
- Layer 41: `271`, ` .`, ` computed`, ` waiting`, `))))` (target ranks: base_value=56:41944, first_product=112:83961, bound_value=126:112211, second_product=252:40058, answer=271:1)

### Filler position 22 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:125738, first_product=112:123115, bound_value=126:121286, second_product=252:125488, answer=271:123541)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:9446, first_product=112:22110, bound_value=126:25505, second_product=252:17445, answer=271:18006)
- Layer 20: `ait`, `距`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=56:8063, first_product=112:24302, bound_value=126:32076, second_product=252:25814, answer=271:25086)
- Layer 30: `14`, ` fourteen`, `atan`, `粥`, `保留` (target ranks: base_value=56:23, first_product=112:16166, bound_value=126:46955, second_product=252:32819, answer=271:22816)
- Layer 35: `55`, ` twice`, `分解`, ` Tw`, `2` (target ranks: base_value=56:65, first_product=112:5792, bound_value=126:29468, second_product=252:51828, answer=271:12393)
- Layer 36: `55`, `分解`, `水土`, ` decom`, `留存` (target ranks: base_value=56:430, first_product=112:7748, bound_value=126:25088, second_product=252:71859, answer=271:28282)
- Layer 37: ` doubling`, `55`, `退役`, `}<?`, ` Tub` (target ranks: base_value=56:4438, first_product=112:19796, bound_value=126:57966, second_product=252:109131, answer=271:76110)
- Layer 38: `}<?`, ` doubling`, `zat`, `退役`, ` Tub` (target ranks: base_value=56:13465, first_product=112:43018, bound_value=126:74670, second_product=252:118945, answer=271:94450)
- Layer 39: `}<?`, ` doubling`, `erer`, `叶子`, `东海` (target ranks: base_value=56:73926, first_product=112:60836, bound_value=126:70789, second_product=252:87586, answer=271:58510)
- Layer 40: ` Tw`, `isis`, `Tw`, `俯`, `殿堂` (target ranks: base_value=56:23491, first_product=112:13600, bound_value=126:14033, second_product=252:17392, answer=271:1149)
- Layer 41: ` Tw`, ` `, ` .`, `Tw`, `zwe` (target ranks: base_value=56:4761, first_product=112:14405, bound_value=126:3386, second_product=252:3778, answer=271:197)

### Filler position 23 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126209, first_product=112:123829, bound_value=126:122006, second_product=252:125987, answer=271:123858)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:10626, first_product=112:23494, bound_value=126:26845, second_product=252:17947, answer=271:18603)
- Layer 20: ` smile`, `足`, `幽`, ` LS`, `锁定` (target ranks: base_value=56:6867, first_product=112:17277, bound_value=126:16932, second_product=252:14461, answer=271:12952)
- Layer 30: ` twice`, ` Tw`, `Tw`, ` repeated`, `tw` (target ranks: base_value=56:193, first_product=112:2324, bound_value=126:5290, second_product=252:14788, answer=271:14056)
- Layer 35: ` Tw`, ` twice`, `Tw`, `14`, ` repeated` (target ranks: base_value=56:106, first_product=112:1898, bound_value=126:3874, second_product=252:12530, answer=271:9248)
- Layer 36: ` Tw`, ` repeated`, ` twice`, `Tw`, `14` (target ranks: base_value=56:459, first_product=112:2409, bound_value=126:2827, second_product=252:19602, answer=271:17714)
- Layer 37: ` doubling`, ` doubled`, `}<?`, ` doubles`, `明珠` (target ranks: base_value=56:1705, first_product=112:3541, bound_value=126:3335, second_product=252:45839, answer=271:60335)
- Layer 38: `}<?`, ` doubling`, `明珠`, ` doubled`, `珍珠` (target ranks: base_value=56:10864, first_product=112:20047, bound_value=126:14440, second_product=252:78118, answer=271:72173)
- Layer 39: `}<?`, ` doubling`, ` doubled`, `叶子`, `东海` (target ranks: base_value=56:43867, first_product=112:85556, bound_value=126:81804, second_product=252:104511, answer=271:86353)
- Layer 40: ` Zem`, ` zem`, `zem`, `zij`, ` Tw` (target ranks: base_value=56:10595, first_product=112:45219, bound_value=126:37259, second_product=252:71216, answer=271:45522)
- Layer 41: ` zem`, `zem`, `zij`, ` Zem`, ` twice` (target ranks: base_value=56:15038, first_product=112:35129, bound_value=126:21842, second_product=252:41560, answer=271:42867)

### Filler position 24 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126350, first_product=112:124106, bound_value=126:122401, second_product=252:126197, answer=271:124066)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:10449, first_product=112:24132, bound_value=126:27528, second_product=252:17968, answer=271:18393)
- Layer 20: `足`, ` smile`, `ait`, ` LS`, `锁定` (target ranks: base_value=56:6498, first_product=112:25787, bound_value=126:27351, second_product=252:20965, answer=271:16202)
- Layer 30: `adal`, `alal`, ` X`, ` x`, `atan` (target ranks: base_value=56:869, first_product=112:39246, bound_value=126:44695, second_product=252:70868, answer=271:25541)
- Layer 35: `adal`, `alal`, ` X`, `usal`, ` repetition` (target ranks: base_value=56:896, first_product=112:49346, bound_value=126:52739, second_product=252:62058, answer=271:23523)
- Layer 36: `adal`, ` X`, `alal`, `usal`, ` repeated` (target ranks: base_value=56:1299, first_product=112:42062, bound_value=126:25731, second_product=252:52955, answer=271:30223)
- Layer 37: `adal`, `}<?`, `enal`, `acl`, `yal` (target ranks: base_value=56:3787, first_product=112:72561, bound_value=126:55925, second_product=252:97913, answer=271:76223)
- Layer 38: `zal`, `}<?`, `enal`, `geal`, ` x` (target ranks: base_value=56:6388, first_product=112:82292, bound_value=126:51767, second_product=252:107974, answer=271:78864)
- Layer 39: `}<?`, ` x`, `𝑋`, ` X`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=56:20383, first_product=112:93126, bound_value=126:69586, second_product=252:114363, answer=271:85507)
- Layer 40: `eland`, ` pals`, `acl`, ` x`, `殿堂` (target ranks: base_value=56:5392, first_product=112:67246, bound_value=126:52356, second_product=252:104408, answer=271:62319)
- Layer 41: ` .`, `eland`, ` `, ` twist`, `然而` (target ranks: base_value=56:2115, first_product=112:66380, bound_value=126:21817, second_product=252:64107, answer=271:28582)

### Filler position 25 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126133, first_product=112:123719, bound_value=126:121884, second_product=252:125894, answer=271:123757)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10911, first_product=112:25627, bound_value=126:28826, second_product=252:19081, answer=271:19344)
- Layer 20: `ait`, `锁定`, ` Walker`, `忑`, ` ES` (target ranks: base_value=56:10223, first_product=112:30957, bound_value=126:38268, second_product=252:26616, answer=271:24420)
- Layer 30: ` labor`, `calcul`, `acin`, `算出`, `第一步` (target ranks: base_value=56:2204, first_product=112:53373, bound_value=126:81194, second_product=252:92273, answer=271:79111)
- Layer 35: ` labor`, `分解`, `acin`, `calcul`, `第一步` (target ranks: base_value=56:1813, first_product=112:44515, bound_value=126:54739, second_product=252:61824, answer=271:46097)
- Layer 36: `留存`, `calcul`, `acin`, `羊`, `分解` (target ranks: base_value=56:1574, first_product=112:32206, bound_value=126:22897, second_product=252:42653, answer=271:43746)
- Layer 37: `}<?`, `calcul`, `翻了`, ` p`, `翻` (target ranks: base_value=56:4551, first_product=112:56746, bound_value=126:44414, second_product=252:94629, answer=271:103377)
- Layer 38: ` p`, `calcul`, `}<?`, ` Duc`, ` pals` (target ranks: base_value=56:3975, first_product=112:46018, bound_value=126:23385, second_product=252:83848, answer=271:81805)
- Layer 39: `}<?`, ` p`, ` duc`, ` Duc`, `殿堂` (target ranks: base_value=56:14673, first_product=112:87501, bound_value=126:61694, second_product=252:110560, answer=271:98576)
- Layer 40: ` p`, ` Tw`, ` Zem`, ` twist`, `Tw` (target ranks: base_value=56:3129, first_product=112:50446, bound_value=126:29933, second_product=252:93406, answer=271:48166)
- Layer 41: ` .`, `zp`, `zij`, ` twist`, ` Tw` (target ranks: base_value=56:497, first_product=112:27549, bound_value=126:4091, second_product=252:23130, answer=271:5233)

### Filler position 26 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126492, first_product=112:124260, bound_value=126:122453, second_product=252:126270, answer=271:124100)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10534, first_product=112:24229, bound_value=126:27170, second_product=252:18226, answer=271:18503)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `拆` (target ranks: base_value=56:11056, first_product=112:33336, bound_value=126:44171, second_product=252:30398, answer=271:28932)
- Layer 30: ` exercises`, `ession`, `题库`, ` repetition`, `sets` (target ranks: base_value=56:13633, first_product=112:70626, bound_value=126:98615, second_product=252:81049, answer=271:76515)
- Layer 35: ` var`, ` variable`, `分解`, ` labor`, ` equations` (target ranks: base_value=56:13933, first_product=112:51295, bound_value=126:85902, second_product=252:54695, answer=271:39929)
- Layer 36: ` definitions`, ` zad`, ` var`, ` equations`, ` list` (target ranks: base_value=56:14182, first_product=112:39351, bound_value=126:75626, second_product=252:47950, answer=271:31914)
- Layer 37: ` definitions`, ` list`, ` variables`, `变量的`, `Variables` (target ranks: base_value=56:45920, first_product=112:70719, bound_value=126:111455, second_product=252:96437, answer=271:81511)
- Layer 38: ` definitions`, ` variables`, ` maze`, `变量的`, `variables` (target ranks: base_value=56:60479, first_product=112:61466, bound_value=126:119800, second_product=252:108893, answer=271:84059)
- Layer 39: `script`, `变量的`, `variables`, `}<?`, ` variables` (target ranks: base_value=56:65929, first_product=112:74695, bound_value=126:118490, second_product=252:117415, answer=271:106775)
- Layer 40: ` definitions`, ` Definitions`, `Definitions`, `ses`, `acl` (target ranks: base_value=56:34552, first_product=112:49290, bound_value=126:109349, second_product=252:107173, answer=271:102828)
- Layer 41: ` definitions`, `zij`, `zp`, ` Definitions`, ` assignment` (target ranks: base_value=56:2755, first_product=112:19301, bound_value=126:27598, second_product=252:24920, answer=271:36992)

### Filler position 27 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=56:126444, first_product=112:124345, bound_value=126:122620, second_product=252:126338, answer=271:124260)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10063, first_product=112:22303, bound_value=126:25304, second_product=252:17217, answer=271:17657)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `Walker` (target ranks: base_value=56:10476, first_product=112:25167, bound_value=126:37155, second_product=252:25940, answer=271:22712)
- Layer 30: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:8465, first_product=112:24810, bound_value=126:50702, second_product=252:63094, answer=271:65345)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:8166, first_product=112:26700, bound_value=126:49461, second_product=252:55552, answer=271:43876)
- Layer 36: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:8917, first_product=112:20024, bound_value=126:30373, second_product=252:57364, answer=271:44048)
- Layer 37: ` Tw`, `Tw`, `tw`, ` twice`, ` doubling` (target ranks: base_value=56:31149, first_product=112:37764, bound_value=126:53565, second_product=252:96755, answer=271:92598)
- Layer 38: ` Tw`, `Tw`, `tw`, `.tw`, ` twist` (target ranks: base_value=56:48509, first_product=112:42326, bound_value=126:66332, second_product=252:100979, answer=271:109156)
- Layer 39: ` Tw`, `Tw`, ` Twist`, ` twist`, `tw` (target ranks: base_value=56:23619, first_product=112:48121, bound_value=126:62416, second_product=252:99949, answer=271:104890)
- Layer 40: `zij`, `eland`, `acl`, `zat`, `计算的` (target ranks: base_value=56:5008, first_product=112:33515, bound_value=126:36921, second_product=252:81138, answer=271:43173)
- Layer 41: `zij`, `z`, `zx`, `oz`, ` ` (target ranks: base_value=56:849, first_product=112:20165, bound_value=126:6595, second_product=252:30194, answer=271:18559)

### Filler position 28 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:126838, first_product=112:124933, bound_value=126:123124, second_product=252:126685, answer=271:124575)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:10317, first_product=112:22610, bound_value=126:25718, second_product=252:17647, answer=271:18103)
- Layer 20: `ait`, ` Walker`, `能被`, ` engaging`, `拆` (target ranks: base_value=56:10115, first_product=112:21800, bound_value=126:33175, second_product=252:23955, answer=271:20720)
- Layer 30: ` mun`, `放弃`, `aci`, ` diet`, `分解` (target ranks: base_value=56:61, first_product=112:10143, bound_value=126:192, second_product=252:934, answer=271:4053)
- Layer 35: `252`, `262`, `271`, `251`, `282` (target ranks: base_value=56:3465, first_product=112:32559, bound_value=126:78958, second_product=252:1, answer=271:3)
- Layer 36: `271`, `272`, `267`, `262`, `269` (target ranks: base_value=56:50381, first_product=112:14694, bound_value=126:78176, second_product=252:37, answer=271:1)
- Layer 37: `271`, `263`, `272`, `267`, `262` (target ranks: base_value=56:78899, first_product=112:31507, bound_value=126:55315, second_product=252:37, answer=271:1)
- Layer 38: `271`, `267`, `265`, `268`, `263` (target ranks: base_value=56:115997, first_product=112:115073, bound_value=126:110842, second_product=252:339, answer=271:1)
- Layer 39: `267`, `271`, `265`, `266`, `269` (target ranks: base_value=56:126952, first_product=112:127715, bound_value=126:127236, second_product=252:57319, answer=271:2)
- Layer 40: `271`, `267`, `265`, `ustin`, `uker` (target ranks: base_value=56:126833, first_product=112:127184, bound_value=126:123472, second_product=252:27976, answer=271:1)
- Layer 41: `267`, `271`, ` nuest`, `))))`, ` burujabe` (target ranks: base_value=56:104926, first_product=112:126107, bound_value=126:114533, second_product=252:61127, answer=271:2)

### Filler position 29 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:126491, first_product=112:124461, bound_value=126:122677, second_product=252:126376, answer=271:124271)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11042, first_product=112:24043, bound_value=126:27286, second_product=252:18840, answer=271:18968)
- Layer 20: `锁定`, ` smile`, `ession`, `能被`, `aty` (target ranks: base_value=56:10450, first_product=112:25425, bound_value=126:36154, second_product=252:29327, answer=271:22055)
- Layer 30: ` Zem`, ` zem`, `忽略`, `zem`, ` ignored` (target ranks: base_value=56:10058, first_product=112:36952, bound_value=126:70612, second_product=252:100240, answer=271:61078)
- Layer 35: ` Zem`, ` zem`, `忽略`, `感兴趣的`, `感兴趣` (target ranks: base_value=56:14371, first_product=112:39171, bound_value=126:69340, second_product=252:78156, answer=271:26615)
- Layer 36: ` Zem`, `忽略`, ` zem`, `感兴趣的`, `感兴趣` (target ranks: base_value=56:17340, first_product=112:31919, bound_value=126:44035, second_product=252:75065, answer=271:28027)
- Layer 37: ` Zem`, `}<?`, ` zem`, `坏`, `zem` (target ranks: base_value=56:47975, first_product=112:57158, bound_value=126:71179, second_product=252:107731, answer=271:77226)
- Layer 38: ` Zem`, `}<?`, `zem`, ` zem`, `迷惑` (target ranks: base_value=56:38867, first_product=112:58018, bound_value=126:67042, second_product=252:113288, answer=271:74489)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `迷惑`, ` Zem`, `叶子` (target ranks: base_value=56:72277, first_product=112:101738, bound_value=126:99612, second_product=252:121991, answer=271:107467)
- Layer 40: `坏`, `坏的`, `y`, ` Tw`, ` consum` (target ranks: base_value=56:15765, first_product=112:70000, bound_value=126:49012, second_product=252:95383, answer=271:61763)
- Layer 41: ` .`, `坏`, `没有被`, `鹃`, `等待` (target ranks: base_value=56:3221, first_product=112:34575, bound_value=126:11482, second_product=252:38333, answer=271:14161)

### Filler position 30 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:126755, first_product=112:124755, bound_value=126:122942, second_product=252:126556, answer=271:124436)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10223, first_product=112:22886, bound_value=126:26621, second_product=252:18066, answer=271:18323)
- Layer 20: ` LS`, `atile`, ` smile`, `cape`, `ait` (target ranks: base_value=56:7408, first_product=112:21859, bound_value=126:28424, second_product=252:27243, answer=271:25348)
- Layer 30: `yg`, ` tap`, `�`, ` tail`, ` SK` (target ranks: base_value=56:17241, first_product=112:94424, bound_value=126:106847, second_product=252:119442, answer=271:89993)
- Layer 35: ` tap`, ` Wil`, `Tap`, `�`, `tap` (target ranks: base_value=56:30862, first_product=112:101549, bound_value=126:110623, second_product=252:111304, answer=271:71183)
- Layer 36: ` dynam`, ` tap`, ` rip`, `坏`, ` riv` (target ranks: base_value=56:26245, first_product=112:74757, bound_value=126:69620, second_product=252:82308, answer=271:48250)
- Layer 37: `}<?`, `疑惑`, ` sip`, ` duc`, ` orb` (target ranks: base_value=56:73658, first_product=112:96382, bound_value=126:93416, second_product=252:118311, answer=271:101073)
- Layer 38: `oNames`, ` duc`, `}<?`, `zat`, `迷惑` (target ranks: base_value=56:82615, first_product=112:93529, bound_value=126:94741, second_product=252:119962, answer=271:104258)
- Layer 39: ` duc`, ` Nij`, `}<?`, `ked`, ` rib` (target ranks: base_value=56:98918, first_product=112:95767, bound_value=126:109584, second_product=252:112216, answer=271:68521)
- Layer 40: ` fum`, `zel`, ` torn`, ` rov`, ` rif` (target ranks: base_value=56:78316, first_product=112:77751, bound_value=126:79001, second_product=252:96128, answer=271:15379)
- Layer 41: `zel`, `zij`, `ugi`, ` fum`, `坏` (target ranks: base_value=56:18624, first_product=112:44871, bound_value=126:13167, second_product=252:26837, answer=271:1389)

### Filler position 31 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=56:126982, first_product=112:125285, bound_value=126:123572, second_product=252:126885, answer=271:124890)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9741, first_product=112:22360, bound_value=126:25294, second_product=252:17467, answer=271:17933)
- Layer 20: `锁定`, ` smile`, `ait`, `鞍`, ` LS` (target ranks: base_value=56:8430, first_product=112:19011, bound_value=126:25677, second_product=252:19258, answer=271:17566)
- Layer 30: ` answer`, ` Answer`, `Answer`, `答案`, `回答` (target ranks: base_value=56:3287, first_product=112:23914, bound_value=126:36825, second_product=252:28031, answer=271:14176)
- Layer 35: ` answer`, ` Answer`, `Answer`, `answer`, ` ANSWER` (target ranks: base_value=56:2122, first_product=112:15632, bound_value=126:27251, second_product=252:13547, answer=271:3351)
- Layer 36: ` answer`, `鞍`, ` Answer`, `acin`, `Answer` (target ranks: base_value=56:2952, first_product=112:22856, bound_value=126:13970, second_product=252:13312, answer=271:7230)
- Layer 37: ` Answer`, `rational`, `}<?`, ` rational`, ` resonator` (target ranks: base_value=56:17500, first_product=112:36008, bound_value=126:16681, second_product=252:33260, answer=271:12519)
- Layer 38: `}<?`, `aharan`, `rational`, `osit`, `等待着` (target ranks: base_value=56:45255, first_product=112:42780, bound_value=126:12821, second_product=252:31037, answer=271:10740)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `aharan`, `ocyst`, `opters` (target ranks: base_value=56:95054, first_product=112:113775, bound_value=126:95000, second_product=252:75643, answer=271:4440)
- Layer 40: ` talags`, `acl`, ` Answer`, `acular`, `271` (target ranks: base_value=56:68409, first_product=112:114196, bound_value=126:76731, second_product=252:53513, answer=271:5)
- Layer 41: ` talags`, `271`, `Answer`, `试一试`, ` .` (target ranks: base_value=56:24510, first_product=112:96963, bound_value=126:26488, second_product=252:8332, answer=271:2)

### Filler position 32 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=56:126889, first_product=112:124990, bound_value=126:123295, second_product=252:126699, answer=271:124710)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9649, first_product=112:21989, bound_value=126:24977, second_product=252:17316, answer=271:17955)
- Layer 20: ` Walker`, ` engaging`, `Walker`, `锁定`, ` LS` (target ranks: base_value=56:9901, first_product=112:20609, bound_value=126:28175, second_product=252:25691, answer=271:18386)
- Layer 30: `antal`, `鞍`, `�`, `平行`, ` Zem` (target ranks: base_value=56:1447, first_product=112:44760, bound_value=126:84626, second_product=252:111806, answer=271:38645)
- Layer 35: `antal`, ` Zem`, `adal`, `鞍`, ` reserved` (target ranks: base_value=56:562, first_product=112:38468, bound_value=126:55867, second_product=252:86284, answer=271:18836)
- Layer 36: ` Zem`, `留存`, `antal`, `adal`, `退出` (target ranks: base_value=56:1505, first_product=112:29410, bound_value=126:26578, second_product=252:79375, answer=271:21672)
- Layer 37: ` Zem`, `}<?`, ` doubling`, `zem`, `acam` (target ranks: base_value=56:6207, first_product=112:48185, bound_value=126:54512, second_product=252:109841, answer=271:53651)
- Layer 38: ` Zem`, `}<?`, `迷惑`, `zem`, ` doubling` (target ranks: base_value=56:13539, first_product=112:64023, bound_value=126:54378, second_product=252:113765, answer=271:51615)
- Layer 39: ` Zem`, `}<?`, `迷惑`, ` pals`, ` Zahl` (target ranks: base_value=56:28675, first_product=112:82915, bound_value=126:77346, second_product=252:119138, answer=271:65899)
- Layer 40: ` Zem`, ` talags`, ` pals`, `eland`, `zij` (target ranks: base_value=56:1909, first_product=112:29467, bound_value=126:19935, second_product=252:93379, answer=271:22710)
- Layer 41: ` number`, ` pals`, `数目`, `zij`, `acular` (target ranks: base_value=56:747, first_product=112:32275, bound_value=126:4431, second_product=252:35214, answer=271:7940)

### Filler position 33 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127206, first_product=112:125719, bound_value=126:124157, second_product=252:127208, answer=271:125239)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9045, first_product=112:21425, bound_value=126:24680, second_product=252:16546, answer=271:17040)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=56:8911, first_product=112:21249, bound_value=126:30953, second_product=252:23740, answer=271:19904)
- Layer 30: ` Zem`, ` zem`, `鞍`, `antal`, `�` (target ranks: base_value=56:1569, first_product=112:20836, bound_value=126:68483, second_product=252:58765, answer=271:32066)
- Layer 35: ` Zem`, ` var`, ` reserved`, ` value`, ` absorbing` (target ranks: base_value=56:722, first_product=112:19503, bound_value=126:55717, second_product=252:44856, answer=271:11939)
- Layer 36: ` Zem`, ` value`, `留存`, `adal`, ` talags` (target ranks: base_value=56:1383, first_product=112:20759, bound_value=126:40910, second_product=252:46042, answer=271:14608)
- Layer 37: ` Zem`, ` talags`, ` value`, `数值`, `不加` (target ranks: base_value=56:6346, first_product=112:39752, bound_value=126:71852, second_product=252:89536, answer=271:43879)
- Layer 38: ` Zem`, `zem`, `referent`, `不加`, `zat` (target ranks: base_value=56:10947, first_product=112:56005, bound_value=126:90041, second_product=252:104320, answer=271:37840)
- Layer 39: ` Zem`, `zem`, `osit`, `迷惑`, ` zem` (target ranks: base_value=56:15851, first_product=112:82360, bound_value=126:97913, second_product=252:117552, answer=271:66009)
- Layer 40: ` Zem`, ` zem`, `zem`, `zij`, ` talags` (target ranks: base_value=56:1842, first_product=112:47243, bound_value=126:54640, second_product=252:90756, answer=271:45162)
- Layer 41: ` zem`, ` Zem`, `zij`, `zem`, ` whichever` (target ranks: base_value=56:328, first_product=112:55180, bound_value=126:22116, second_product=252:55659, answer=271:23790)

### Filler position 34 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127382, first_product=112:125970, bound_value=126:124388, second_product=252:127372, answer=271:125402)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:9601, first_product=112:22206, bound_value=126:25144, second_product=252:16805, answer=271:17400)
- Layer 20: `ait`, ` Walker`, `锁定`, ` smile`, `Walker` (target ranks: base_value=56:7751, first_product=112:24777, bound_value=126:28554, second_product=252:25304, answer=271:18588)
- Layer 30: ` Tw`, `Tw`, `tw`, ` twice`, `.tw` (target ranks: base_value=56:9795, first_product=112:30176, bound_value=126:35974, second_product=252:77677, answer=271:78442)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:6072, first_product=112:27574, bound_value=126:33587, second_product=252:53185, answer=271:50074)
- Layer 36: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=56:8238, first_product=112:19763, bound_value=126:18331, second_product=252:56162, answer=271:38097)
- Layer 37: ` Tw`, ` doubling`, `Tw`, ` twice`, `tw` (target ranks: base_value=56:25767, first_product=112:35039, bound_value=126:28741, second_product=252:83388, answer=271:77015)
- Layer 38: ` Tw`, ` doubling`, `Tw`, `.tw`, ` twisting` (target ranks: base_value=56:43300, first_product=112:47687, bound_value=126:43028, second_product=252:88930, answer=271:98641)
- Layer 39: ` Tw`, `Tw`, ` doubling`, ` twist`, ` Twist` (target ranks: base_value=56:34937, first_product=112:49022, bound_value=126:47374, second_product=252:94836, answer=271:100934)
- Layer 40: ` twice`, ` Tw`, `Tw`, ` Zem`, ` twist` (target ranks: base_value=56:5061, first_product=112:25552, bound_value=126:20391, second_product=252:80694, answer=271:29411)
- Layer 41: ` twice`, `Tw`, `tw`, ` twist`, `zij` (target ranks: base_value=56:735, first_product=112:33774, bound_value=126:6179, second_product=252:40899, answer=271:16791)

### Filler position 35 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127380, first_product=112:125917, bound_value=126:124301, second_product=252:127337, answer=271:125345)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10898, first_product=112:23769, bound_value=126:26146, second_product=252:17904, answer=271:18675)
- Layer 20: ` smile`, `足`, `ait`, `幽`, `胃癌` (target ranks: base_value=56:3745, first_product=112:12734, bound_value=126:15497, second_product=252:8315, answer=271:10200)
- Layer 30: `Conc`, `}<?`, ` السماويه`, `翻了`, `296` (target ranks: base_value=56:1217, first_product=112:4606, bound_value=126:1149, second_product=252:666, answer=271:391)
- Layer 35: `271`, `295`, `267`, `锁定`, ` reserved` (target ranks: base_value=56:10522, first_product=112:63861, bound_value=126:87776, second_product=252:1946, answer=271:1)
- Layer 36: `271`, `295`, `283`, `303`, `267` (target ranks: base_value=56:55383, first_product=112:58640, bound_value=126:109629, second_product=252:4835, answer=271:1)
- Layer 37: `271`, `295`, `283`, `263`, `267` (target ranks: base_value=56:98235, first_product=112:70310, bound_value=126:109216, second_product=252:5764, answer=271:1)
- Layer 38: `295`, `271`, `303`, `291`, `283` (target ranks: base_value=56:127324, first_product=112:113860, bound_value=126:127151, second_product=252:47882, answer=271:2)
- Layer 39: `271`, `本题分析`, ` Noruwega`, `zat`, `SPJ` (target ranks: base_value=56:127755, first_product=112:126283, bound_value=126:128539, second_product=252:113492, answer=271:1)
- Layer 40: `271`, `radesh`, ` burge`, `点滴`, `enk` (target ranks: base_value=56:128213, first_product=112:126204, bound_value=126:128551, second_product=252:116535, answer=271:1)
- Layer 41: `zion`, `需要注意的是`, `zij`, `271`, `辙` (target ranks: base_value=56:116500, first_product=112:121312, bound_value=126:127303, second_product=252:101210, answer=271:4)

### Filler position 36 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127299, first_product=112:125886, bound_value=126:124306, second_product=252:127313, answer=271:125323)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11791, first_product=112:25401, bound_value=126:27969, second_product=252:19071, answer=271:20144)
- Layer 20: `能被`, ` Walker`, `ait`, ` engaging`, ` smile` (target ranks: base_value=56:14603, first_product=112:30895, bound_value=126:36071, second_product=252:25026, answer=271:21590)
- Layer 30: ` усили`, ` vertical`, ` уси`, ` substr`, `79` (target ranks: base_value=56:1033, first_product=112:7734, bound_value=126:3434, second_product=252:2147, answer=271:867)
- Layer 35: `252`, `翻`, `282`, `271`, `Dip` (target ranks: base_value=56:7231, first_product=112:15983, bound_value=126:72213, second_product=252:1, answer=271:4)
- Layer 36: `271`, `272`, `273`, `274`, `270` (target ranks: base_value=56:90552, first_product=112:2980, bound_value=126:119938, second_product=252:6, answer=271:1)
- Layer 37: `272`, `271`, `}<?`, `273`, `uker` (target ranks: base_value=56:119927, first_product=112:11235, bound_value=126:116024, second_product=252:12, answer=271:2)
- Layer 38: `271`, `272`, `270`, `273`, `371` (target ranks: base_value=56:129177, first_product=112:26489, bound_value=126:128314, second_product=252:765, answer=271:1)
- Layer 39: `271`, `(migrations`, ` dátummal`, `}<?`, `�` (target ranks: base_value=56:128033, first_product=112:126416, bound_value=126:128659, second_product=252:70872, answer=271:1)
- Layer 40: `gies`, `ekak`, `uker`, `271`, `ocalorie` (target ranks: base_value=56:128046, first_product=112:127399, bound_value=126:128339, second_product=252:85034, answer=271:4)
- Layer 41: ` nuest`, ` expectation`, `Answer`, `========================================================================`, ` usual` (target ranks: base_value=56:108202, first_product=112:124458, bound_value=126:126200, second_product=252:49153, answer=271:13)

### Filler position 37 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127275, first_product=112:125814, bound_value=126:124165, second_product=252:127226, answer=271:125202)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11530, first_product=112:25506, bound_value=126:28271, second_product=252:19229, answer=271:20414)
- Layer 20: `能被`, ` engaging`, `忑`, ` Walker`, ` Engaging` (target ranks: base_value=56:18514, first_product=112:52090, bound_value=126:49045, second_product=252:42410, answer=271:35250)
- Layer 30: ` twice`, `算出`, `Tw`, ` Tw`, `第一步` (target ranks: base_value=56:98, first_product=112:54812, bound_value=126:53877, second_product=252:104117, answer=271:94557)
- Layer 35: ` twice`, ` Tw`, `Tw`, `usal`, `adal` (target ranks: base_value=56:49, first_product=112:36672, bound_value=126:29352, second_product=252:62559, answer=271:65627)
- Layer 36: ` doubling`, ` Tw`, ` twice`, `翻`, ` doubled` (target ranks: base_value=56:234, first_product=112:30428, bound_value=126:9806, second_product=252:62387, answer=271:75256)
- Layer 37: `}<?`, ` doubling`, ` doubled`, ` doubles`, ` doubly` (target ranks: base_value=56:1001, first_product=112:44537, bound_value=126:25726, second_product=252:91900, answer=271:116708)
- Layer 38: ` doubling`, `}<?`, ` doubled`, ` doubles`, `zat` (target ranks: base_value=56:822, first_product=112:49416, bound_value=126:27807, second_product=252:103323, answer=271:115061)
- Layer 39: `}<?`, ` doubling`, ` doubled`, ` doubles`, ` x` (target ranks: base_value=56:11476, first_product=112:80664, bound_value=126:55851, second_product=252:103184, answer=271:94656)
- Layer 40: ` x`, `acular`, `acl`, ` Tw`, ` substr` (target ranks: base_value=56:1224, first_product=112:41414, bound_value=126:20128, second_product=252:63066, answer=271:25436)
- Layer 41: `acular`, ` `, `从前`, ` .`, `zx` (target ranks: base_value=56:124, first_product=112:20726, bound_value=126:1054, second_product=252:5977, answer=271:1369)

### Filler position 38 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127225, first_product=112:125856, bound_value=126:124230, second_product=252:127268, answer=271:125226)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10649, first_product=112:23751, bound_value=126:26924, second_product=252:18015, answer=271:19408)
- Layer 20: `忑`, `ait`, `能被`, ` engaging`, `会成为` (target ranks: base_value=56:15933, first_product=112:49256, bound_value=126:43626, second_product=252:34735, answer=271:28626)
- Layer 30: ` calculator`, `aci`, `adak`, `eder`, `calculator` (target ranks: base_value=56:45, first_product=112:18017, bound_value=126:911, second_product=252:6669, answer=271:9141)
- Layer 35: `281`, `锁定`, `calc`, ` calculator`, `acic` (target ranks: base_value=56:1922, first_product=112:34423, bound_value=126:92394, second_product=252:342, answer=271:43)
- Layer 36: `281`, `286`, `301`, `280`, `271` (target ranks: base_value=56:3406, first_product=112:25568, bound_value=126:76698, second_product=252:1731, answer=271:5)
- Layer 37: `281`, `301`, `282`, `}<?`, `280` (target ranks: base_value=56:23212, first_product=112:40210, bound_value=126:86059, second_product=252:4465, answer=271:7)
- Layer 38: `281`, `301`, `286`, `284`, `287` (target ranks: base_value=56:48887, first_product=112:74284, bound_value=126:100396, second_product=252:12982, answer=271:13)
- Layer 39: `}<?`, `281`, `271`, `287`, `301` (target ranks: base_value=56:79466, first_product=112:113647, bound_value=126:121598, second_product=252:42776, answer=271:3)
- Layer 40: `271`, `}<?`, ` burge`, `281`, `acular` (target ranks: base_value=56:86256, first_product=112:103850, bound_value=126:119180, second_product=252:28756, answer=271:1)
- Layer 41: `271`, ` waiting`, `Answer`, ` twice`, `zl` (target ranks: base_value=56:20204, first_product=112:77120, bound_value=126:91993, second_product=252:8078, answer=271:1)

### Filler position 39 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=56:127503, first_product=112:126331, bound_value=126:124911, second_product=252:127596, answer=271:125590)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:10547, first_product=112:23277, bound_value=126:26191, second_product=252:17778, answer=271:19128)
- Layer 20: `ait`, `锁定`, ` engaging`, ` smile`, ` ES` (target ranks: base_value=56:8264, first_product=112:27575, bound_value=126:32316, second_product=252:22799, answer=271:18263)
- Layer 30: `calculator`, ` calculator`, `下沉`, ` seventy`, `79` (target ranks: base_value=56:1243, first_product=112:10950, bound_value=126:28165, second_product=252:13689, answer=271:1195)
- Layer 35: ` calculator`, `锁定`, `退出`, `obin`, ` smile` (target ranks: base_value=56:3808, first_product=112:27072, bound_value=126:42266, second_product=252:3854, answer=271:15)
- Layer 36: `翻`, `退出`, `295`, `calcul`, `acin` (target ranks: base_value=56:10477, first_product=112:36447, bound_value=126:32342, second_product=252:2355, answer=271:12)
- Layer 37: `}<?`, `Quintal`, `267`, `271`, `翻了` (target ranks: base_value=56:48866, first_product=112:41761, bound_value=126:45104, second_product=252:5668, answer=271:4)
- Layer 38: `}<?`, ` Noruwega`, `?datasetId`, `urin`, `zat` (target ranks: base_value=56:101502, first_product=112:88166, bound_value=126:88099, second_product=252:23795, answer=271:25)
- Layer 39: `}<?`, `urin`, `ocyst`, `叶子`, ` dirty` (target ranks: base_value=56:120537, first_product=112:116773, bound_value=126:123756, second_product=252:49439, answer=271:13)
- Layer 40: `271`, `等待着`, `281`, `accur`, `273` (target ranks: base_value=56:119258, first_product=112:121193, bound_value=126:125265, second_product=252:48846, answer=271:1)
- Layer 41: `271`, ` waiting`, `273`, ` `, `281` (target ranks: base_value=56:69529, first_product=112:89621, bound_value=126:105197, second_product=252:13632, answer=271:1)

### Filler position 40 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=56:127586, first_product=112:126301, bound_value=126:124782, second_product=252:127560, answer=271:125499)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11127, first_product=112:23861, bound_value=126:27030, second_product=252:18030, answer=271:19842)
- Layer 20: `ait`, `能被`, ` LS`, ` ES`, `LS` (target ranks: base_value=56:6698, first_product=112:23565, bound_value=126:24717, second_product=252:23639, answer=271:19903)
- Layer 30: `放下`, `79`, ` rede`, ` Concern`, ` Difficulty` (target ranks: base_value=56:1373, first_product=112:12172, bound_value=126:341, second_product=252:2234, answer=271:542)
- Layer 35: `252`, `271`, `289`, `251`, `283` (target ranks: base_value=56:12940, first_product=112:23640, bound_value=126:64204, second_product=252:1, answer=271:2)
- Layer 36: `271`, `272`, `273`, `274`, `275` (target ranks: base_value=56:98791, first_product=112:8264, bound_value=126:83047, second_product=252:39, answer=271:1)
- Layer 37: `271`, `272`, `273`, `274`, `275` (target ranks: base_value=56:119786, first_product=112:22286, bound_value=126:71820, second_product=252:54, answer=271:1)
- Layer 38: `271`, `277`, `281`, `275`, `272` (target ranks: base_value=56:129182, first_product=112:99278, bound_value=126:126520, second_product=252:1163, answer=271:1)
- Layer 39: `271`, `281`, `277`, `urin`, `267` (target ranks: base_value=56:128584, first_product=112:126878, bound_value=126:128026, second_product=252:47626, answer=271:1)
- Layer 40: `271`, `<｜begin▁of▁file｜>`, `uker`, ` neperian`, `花儿` (target ranks: base_value=56:128718, first_product=112:127763, bound_value=126:127515, second_product=252:93908, answer=271:1)
- Layer 41: `271`, ` Answer`, `Answer`, `))))`, ` expectation` (target ranks: base_value=56:124769, first_product=112:123485, bound_value=126:120014, second_product=252:69112, answer=271:1)

### Filler position 41 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=56:127582, first_product=112:126287, bound_value=126:124756, second_product=252:127539, answer=271:125487)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11211, first_product=112:24386, bound_value=126:27504, second_product=252:18068, answer=271:19811)
- Layer 20: `ait`, `锁定`, `能被`, ` smile`, ` Walker` (target ranks: base_value=56:10213, first_product=112:27836, bound_value=126:25748, second_product=252:22518, answer=271:18990)
- Layer 30: `放下`, `deal`, ` udalerria`, `sat`, `acos` (target ranks: base_value=56:1166, first_product=112:12504, bound_value=126:62, second_product=252:1033, answer=271:6826)
- Layer 35: `252`, `352`, `251`, `272`, `Dip` (target ranks: base_value=56:3236, first_product=112:9334, bound_value=126:44445, second_product=252:1, answer=271:16)
- Layer 36: `272`, `252`, `271`, `265`, `雍正` (target ranks: base_value=56:55164, first_product=112:1224, bound_value=126:61070, second_product=252:2, answer=271:3)
- Layer 37: `252`, `272`, `265`, `uker`, ` Ub` (target ranks: base_value=56:81401, first_product=112:2246, bound_value=126:35560, second_product=252:1, answer=271:6)
- Layer 38: `271`, `265`, `272`, `267`, `270` (target ranks: base_value=56:126469, first_product=112:48980, bound_value=126:98232, second_product=252:63, answer=271:1)
- Layer 39: `271`, ` dátummal`, `urin`, `-ulo`, `�` (target ranks: base_value=56:127007, first_product=112:123870, bound_value=126:123865, second_product=252:5733, answer=271:1)
- Layer 40: `271`, `ekak`, `花儿`, `uker`, `erb` (target ranks: base_value=56:126239, first_product=112:121370, bound_value=126:103930, second_product=252:2470, answer=271:1)
- Layer 41: `271`, `Answer`, ` nuest`, ` waiting`, ` Answer` (target ranks: base_value=56:80440, first_product=112:90668, bound_value=126:78924, second_product=252:1709, answer=271:1)

### Filler position 42 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127541, first_product=112:126142, bound_value=126:124622, second_product=252:127463, answer=271:125372)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11551, first_product=112:24867, bound_value=126:27987, second_product=252:18583, answer=271:20133)
- Layer 20: ` smile`, `锁定`, `鞍`, `胃癌`, `ait` (target ranks: base_value=56:8515, first_product=112:23357, bound_value=126:21385, second_product=252:16902, answer=271:13144)
- Layer 30: ` nasod`, `acos`, `巩固`, ` vertical`, ` Heidelberg` (target ranks: base_value=56:3134, first_product=112:41662, bound_value=126:28160, second_product=252:45592, answer=271:7557)
- Layer 35: `atan`, `缓`, `鞍`, ` Kaw`, `锁定` (target ranks: base_value=56:4844, first_product=112:51216, bound_value=126:90310, second_product=252:60870, answer=271:841)
- Layer 36: ` Heidelberg`, ` error`, ` erg`, `radesh`, `翻` (target ranks: base_value=56:12277, first_product=112:44321, bound_value=126:112095, second_product=252:100853, answer=271:94)
- Layer 37: ` Noruwega`, `}<?`, ` Heidelberg`, ` erg`, `在北京` (target ranks: base_value=56:53512, first_product=112:47944, bound_value=126:111885, second_product=252:111689, answer=271:29)
- Layer 38: `}<?`, ` Noruwega`, ` Heidelberg`, ` rul`, `本题分析` (target ranks: base_value=56:108650, first_product=112:106784, bound_value=126:127014, second_product=252:123437, answer=271:19)
- Layer 39: `本题分析`, `-ulo`, ` Noruwega`, `rinnings`, `271` (target ranks: base_value=56:127629, first_product=112:127474, bound_value=126:128740, second_product=252:122613, answer=271:5)
- Layer 40: `271`, `坏`, `语言文字`, `本题分析`, ` ` (target ranks: base_value=56:127540, first_product=112:126408, bound_value=126:128637, second_product=252:118746, answer=271:1)
- Layer 41: `271`, ` .`, ` `, ` waiting`, `Answer` (target ranks: base_value=56:83806, first_product=112:109416, bound_value=126:123492, second_product=252:62034, answer=271:1)

### Filler position 43 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=56:127588, first_product=112:126382, bound_value=126:124980, second_product=252:127627, answer=271:125692)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11388, first_product=112:25048, bound_value=126:28096, second_product=252:18728, answer=271:20532)
- Layer 20: `忑`, `锁定`, `ait`, ` ES`, ` smile` (target ranks: base_value=56:10634, first_product=112:28895, bound_value=126:24274, second_product=252:24156, answer=271:21423)
- Layer 30: ` dinhi`, `126`, ` mun`, `raind`, `沛` (target ranks: base_value=56:121, first_product=112:18293, bound_value=126:2, second_product=252:1558, answer=271:55049)
- Layer 35: `126`, `252`, ` Out`, `assic`, `出击` (target ranks: base_value=56:1671, first_product=112:57070, bound_value=126:1, second_product=252:2, answer=271:51102)
- Layer 36: `126`, `252`, ` Dou`, ` lesion`, `溺` (target ranks: base_value=56:18325, first_product=112:48886, bound_value=126:1, second_product=252:2, answer=271:64902)
- Layer 37: `126`, `252`, `cault`, `祭`, ` Dou` (target ranks: base_value=56:44195, first_product=112:55155, bound_value=126:1, second_product=252:2, answer=271:93981)
- Layer 38: `126`, `252`, ` Dou`, `cault`, `251` (target ranks: base_value=56:58744, first_product=112:42488, bound_value=126:1, second_product=252:2, answer=271:70287)
- Layer 39: `252`, ` Kiel`, `看书`, `无言`, `126` (target ranks: base_value=56:116235, first_product=112:108472, bound_value=126:5, second_product=252:1, answer=271:1947)
- Layer 40: `271`, `252`, `283`, ` Dou`, `281` (target ranks: base_value=56:115141, first_product=112:110214, bound_value=126:290, second_product=252:2, answer=271:1)
- Layer 41: `271`, `252`, ` `, `要不`, `283` (target ranks: base_value=56:61209, first_product=112:101114, bound_value=126:230, second_product=252:2, answer=271:1)

### Filler position 44 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127394, first_product=112:126010, bound_value=126:124503, second_product=252:127386, answer=271:125344)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11840, first_product=112:25383, bound_value=126:28926, second_product=252:19092, answer=271:21015)
- Layer 20: `忑`, `能被`, `ait`, `会成为`, ` engaging` (target ranks: base_value=56:10851, first_product=112:31718, bound_value=126:27670, second_product=252:25537, answer=271:19526)
- Layer 30: `56`, ` Reese`, ` seventy`, ` mun`, ` Diet` (target ranks: base_value=56:1, first_product=112:1668, bound_value=126:41, second_product=252:18556, answer=271:41157)
- Layer 35: `126`, `125`, `二十六`, `136`, `三十六` (target ranks: base_value=56:14, first_product=112:3026, bound_value=126:1, second_product=252:2153, answer=271:33372)
- Layer 36: `126`, `ASI`, `往外`, `125`, ` Dou` (target ranks: base_value=56:882, first_product=112:15167, bound_value=126:1, second_product=252:3894, answer=271:56190)
- Layer 37: `126`, `ASI`, ` doubling`, `}<?`, ` doubles` (target ranks: base_value=56:7391, first_product=112:38545, bound_value=126:1, second_product=252:32011, answer=271:119526)
- Layer 38: `126`, ` doubling`, ` Dou`, `ASI`, ` doubled` (target ranks: base_value=56:15136, first_product=112:42057, bound_value=126:1, second_product=252:42441, answer=271:117306)
- Layer 39: `}<?`, ` chlorine`, `-ulo`, `ASI`, ` Kiel` (target ranks: base_value=56:44186, first_product=112:87000, bound_value=126:706, second_product=252:39631, answer=271:36348)
- Layer 40: ` Dou`, ` Tw`, ` `, ` fifty`, ` Fifty` (target ranks: base_value=56:22535, first_product=112:54208, bound_value=126:148, second_product=252:4927, answer=271:22)
- Layer 41: ` .`, `271`, `没有什么`, ` `, ` because` (target ranks: base_value=56:1756, first_product=112:25512, bound_value=126:7, second_product=252:412, answer=271:2)

### Filler position 45 (absolute token 845, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=56:127629, first_product=112:126345, bound_value=126:124894, second_product=252:127601, answer=271:125600)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=56:11542, first_product=112:24187, bound_value=126:27712, second_product=252:18269, answer=271:19949)
- Layer 20: `ait`, `会成为`, `平行`, `清楚楚`, ` engaging` (target ranks: base_value=56:18457, first_product=112:46017, bound_value=126:42098, second_product=252:38925, answer=271:28201)
- Layer 30: `udal`, ` x`, ` X`, `alal`, ` fifty` (target ranks: base_value=56:12, first_product=112:62605, bound_value=126:84506, second_product=252:118148, answer=271:89243)
- Layer 35: ` x`, ` X`, `adal`, `56`, `alal` (target ranks: base_value=56:4, first_product=112:32394, bound_value=126:57908, second_product=252:64191, answer=271:35932)
- Layer 36: `adal`, ` x`, `otas`, `留存`, ` X` (target ranks: base_value=56:6, first_product=112:22882, bound_value=126:31359, second_product=252:55068, answer=271:44231)
- Layer 37: `enal`, `}<?`, `Quintal`, ` Halle`, `eal` (target ranks: base_value=56:15, first_product=112:49932, bound_value=126:62934, second_product=252:98800, answer=271:94484)
- Layer 38: `}<?`, `enal`, `geal`, `zal`, ` x` (target ranks: base_value=56:21, first_product=112:56318, bound_value=126:67315, second_product=252:98296, answer=271:93089)
- Layer 39: ` x`, ` X`, `}<?`, `xp`, ` 𝑥` (target ranks: base_value=56:5101, first_product=112:92178, bound_value=126:103434, second_product=252:102851, answer=271:59980)
- Layer 40: ` x`, `留存`, ` Tw`, ` X`, ` twist` (target ranks: base_value=56:1070, first_product=112:48634, bound_value=126:79695, second_product=252:74075, answer=271:14672)
- Layer 41: `�`, ` `, ` .`, `留存`, ` Tw` (target ranks: base_value=56:71, first_product=112:31817, bound_value=126:18212, second_product=252:17524, answer=271:1413)

### Filler position 46 (absolute token 846, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127508, first_product=112:126142, bound_value=126:124638, second_product=252:127496, answer=271:125444)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=56:11401, first_product=112:23504, bound_value=126:26697, second_product=252:17688, answer=271:19420)
- Layer 20: `ait`, `平行`, ` adtong`, `俯`, `妇` (target ranks: base_value=56:48989, first_product=112:72354, bound_value=126:79107, second_product=252:65962, answer=271:37411)
- Layer 30: ` spac`, `acos`, `坝`, `}using`, ` dekameters` (target ranks: base_value=56:89271, first_product=112:100905, bound_value=126:108418, second_product=252:122406, answer=271:91769)
- Layer 35: `坏`, `俯`, `ustomed`, `足足`, ` reduct` (target ranks: base_value=56:26893, first_product=112:68310, bound_value=126:80170, second_product=252:108742, answer=271:40392)
- Layer 36: `俯`, `ancock`, ` dro`, `足足`, ` reserved` (target ranks: base_value=56:5690, first_product=112:46831, bound_value=126:46329, second_product=252:68436, answer=271:22817)
- Layer 37: `}<?`, `坏`, `铎`, `俯`, `放下` (target ranks: base_value=56:35145, first_product=112:72094, bound_value=126:76907, second_product=252:101351, answer=271:68014)
- Layer 38: `坏`, ` .`, `}<?`, `铎`, `acet` (target ranks: base_value=56:17503, first_product=112:89298, bound_value=126:93261, second_product=252:95805, answer=271:81807)
- Layer 39: `}<?`, `分院`, `坏`, `heck`, `ozygous` (target ranks: base_value=56:39861, first_product=112:117330, bound_value=126:96020, second_product=252:91330, answer=271:52910)
- Layer 40: ` .`, ` .↵↵`, ` x`, `oh`, `坏` (target ranks: base_value=56:6573, first_product=112:95208, bound_value=126:62438, second_product=252:59632, answer=271:23831)
- Layer 41: ` .`, ` .↵↵`, ` `, ` .↵`, ` However` (target ranks: base_value=56:1788, first_product=112:35045, bound_value=126:16741, second_product=252:14236, answer=271:2879)

### Filler position 47 (absolute token 847, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=56:127508, first_product=112:126111, bound_value=126:124549, second_product=252:127451, answer=271:125423)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=56:11033, first_product=112:23357, bound_value=126:26247, second_product=252:17637, answer=271:19097)
- Layer 20: `}<?`, ` partly`, `东海`, ` DeWalt`, `Quintal` (target ranks: base_value=56:116357, first_product=112:116359, bound_value=126:114322, second_product=252:119304, answer=271:117784)
- Layer 30: `}<?`, `codeline`, `dividers`, `}using`, `?datasetId` (target ranks: base_value=56:76845, first_product=112:96298, bound_value=126:107204, second_product=252:120700, answer=271:111044)
- Layer 35: `codeline`, `蜗`, `}<?`, `lett`, `ِّف` (target ranks: base_value=56:72123, first_product=112:108689, bound_value=126:96081, second_product=252:123476, answer=271:110124)
- Layer 36: `锯`, `足足`, ` Colleg`, `切割`, ` fit` (target ranks: base_value=56:25196, first_product=112:88215, bound_value=126:60956, second_product=252:107265, answer=271:76641)
- Layer 37: `}<?`, `磨损`, `Quintal`, `ِّف`, `东京` (target ranks: base_value=56:49702, first_product=112:109782, bound_value=126:81067, second_product=252:112792, answer=271:90347)
- Layer 38: ` .`, `遁`, `lett`, `坏`, ` .↵↵` (target ranks: base_value=56:18183, first_product=112:92270, bound_value=126:85920, second_product=252:93350, answer=271:61756)
- Layer 39: ` .`, `�`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, `lett` (target ranks: base_value=56:74695, first_product=112:115732, bound_value=126:110480, second_product=252:96736, answer=271:37754)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, `坏` (target ranks: base_value=56:49346, first_product=112:102082, bound_value=126:81643, second_product=252:73855, answer=271:12524)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, `坏` (target ranks: base_value=56:7974, first_product=112:59085, bound_value=126:18910, second_product=252:16470, answer=271:464)

### Filler position 48 (absolute token 848, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=56:127501, first_product=112:126203, bound_value=126:124711, second_product=252:127518, answer=271:125476)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=56:10885, first_product=112:24550, bound_value=126:27248, second_product=252:18331, answer=271:19224)
- Layer 20: `东海`, ` instantaneous`, ` partly`, `的一半`, `Partly` (target ranks: base_value=56:65725, first_product=112:90880, bound_value=126:66292, second_product=252:86099, answer=271:100771)
- Layer 30: `Quintal`, `}<?`, `codeline`, `?datasetId`, `Pulgada` (target ranks: base_value=56:37231, first_product=112:94243, bound_value=126:55603, second_product=252:79383, answer=271:81203)
- Layer 35: `codeline`, `自重`, `ipada`, `Pulgada`, ` Cater` (target ranks: base_value=56:67334, first_product=112:123922, bound_value=126:127273, second_product=252:31117, answer=271:532)
- Layer 36: `303`, `302`, `306`, `308`, `313` (target ranks: base_value=56:84865, first_product=112:95546, bound_value=126:122169, second_product=252:39536, answer=271:18)
- Layer 37: `codeline`, `Quintal`, `�`, `悬挂`, `edip` (target ranks: base_value=56:125256, first_product=112:125272, bound_value=126:128160, second_product=252:118875, answer=271:4815)
- Layer 38: `codeline`, `悬挂`, `第三百`, `Quintal`, `�` (target ranks: base_value=56:124173, first_product=112:126500, bound_value=126:126661, second_product=252:124181, answer=271:2832)
- Layer 39: `�`, `}using`, `叶子`, `湍`, `树叶` (target ranks: base_value=56:107621, first_product=112:124343, bound_value=126:122783, second_product=252:126041, answer=271:23195)
- Layer 40: ` .`, ` .↵↵`, ` Rees`, `兑`, ` crev` (target ranks: base_value=56:79658, first_product=112:105762, bound_value=126:113559, second_product=252:114556, answer=271:13558)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ;`, `圆圆` (target ranks: base_value=56:39163, first_product=112:85009, bound_value=126:65305, second_product=252:83060, answer=271:5042)

### Filler position 49 (absolute token 849, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=56:127554, first_product=112:126315, bound_value=126:124895, second_product=252:127572, answer=271:125551)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=56:11015, first_product=112:25424, bound_value=126:28387, second_product=252:18876, answer=271:19250)
- Layer 20: ` licensierad`, `aplenty`, `codeline`, ` instantaneous`, ` originalet` (target ranks: base_value=56:102310, first_product=112:110633, bound_value=126:89878, second_product=252:111928, answer=271:101293)
- Layer 30: ` Answer`, `答案是`, ` ответ`, `codeline`, ` Antwort` (target ranks: base_value=56:86391, first_product=112:115231, bound_value=126:124444, second_product=252:112968, answer=271:115244)
- Layer 35: ` Answer`, `codeline`, `AED`, `坏`, ` doubly` (target ranks: base_value=56:75305, first_product=112:99641, bound_value=126:125552, second_product=252:92721, answer=271:98208)
- Layer 36: `坏`, ` Answer`, ` nasod`, ` percept`, `绽` (target ranks: base_value=56:20882, first_product=112:67172, bound_value=126:97536, second_product=252:46221, answer=271:54808)
- Layer 37: `oNames`, `insic`, `codeline`, `坏`, ` consum` (target ranks: base_value=56:112439, first_product=112:104795, bound_value=126:122500, second_product=252:111873, answer=271:107693)
- Layer 38: `oNames`, `<|EOT|>`, ` retard`, `�`, `insic` (target ranks: base_value=56:109435, first_product=112:104346, bound_value=126:121631, second_product=252:110881, answer=271:92855)
- Layer 39: `�`, `oxygen`, `deen`, ` consonant`, ` dú` (target ranks: base_value=56:62987, first_product=112:104572, bound_value=126:112152, second_product=252:86559, answer=271:53335)
- Layer 40: ` .`, ` .↵↵`, ` wink`, `丝的`, ` nasod` (target ranks: base_value=56:5551, first_product=112:58802, bound_value=126:88143, second_product=252:37551, answer=271:13249)
- Layer 41: ` .`, ` .↵↵`, ` wink`, `叮`, ` mister` (target ranks: base_value=56:1120, first_product=112:23125, bound_value=126:41658, second_product=252:7925, answer=271:2020)

### Filler position 50 (absolute token 850, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=56:122138, first_product=112:113537, bound_value=126:108212, second_product=252:116664, answer=271:114653)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=56:127397, first_product=112:118044, bound_value=126:110365, second_product=252:118587, answer=271:113122)
- Layer 20: `能被`, `答复`, `EDER`, ` Submission`, `忑` (target ranks: base_value=56:5566, first_product=112:33773, bound_value=126:34564, second_product=252:31367, answer=271:24628)
- Layer 30: `nze`, `aplenty`, `malink`, `datasetId`, ` MK` (target ranks: base_value=56:24149, first_product=112:97847, bound_value=126:5480, second_product=252:21440, answer=271:80859)
- Layer 35: `252`, `282`, `260`, `280`, `265` (target ranks: base_value=56:69062, first_product=112:107226, bound_value=126:98166, second_product=252:1, answer=271:9)
- Layer 36: `272`, `271`, `270`, `274`, `269` (target ranks: base_value=56:107014, first_product=112:47178, bound_value=126:84050, second_product=252:36, answer=271:2)
- Layer 37: `272`, `270`, `271`, `269`, `274` (target ranks: base_value=56:118054, first_product=112:84048, bound_value=126:77138, second_product=252:38, answer=271:3)
- Layer 38: `278`, `277`, `279`, `271`, `270` (target ranks: base_value=56:126102, first_product=112:126244, bound_value=126:92879, second_product=252:745, answer=271:4)
- Layer 39: `278`, `277`, `�`, `267`, `271` (target ranks: base_value=56:128407, first_product=112:128696, bound_value=126:126977, second_product=252:111485, answer=271:5)
- Layer 40: ` Answer`, `Answer`, ` answer`, `_answer`, `answer` (target ranks: base_value=56:128399, first_product=112:126771, bound_value=126:127342, second_product=252:84660, answer=271:105)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=56:88438, first_product=112:88170, bound_value=126:111747, second_product=252:27835, answer=271:100)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zem = 14
yoh = twice the number for zem plus 27
xal = 56
puc = twice the number for xal plus 14
dof = twice the number for puc plus 26
Question: What is twice the number for puc plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
