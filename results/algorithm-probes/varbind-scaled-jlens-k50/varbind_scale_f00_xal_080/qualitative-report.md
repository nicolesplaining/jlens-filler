# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `367` (correct).
- No-filler answer: `383` (incorrect).
- Filler tokens: 50 tokens at absolute indices 801–850.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=80` | 1 (L24, filler 15) | L24, filler 15 (rank 1) |
| J-Lens | `first_product=160` | 6 (L31, filler 44) | L31, filler 44 (rank 6) |
| J-Lens | `bound_value=174` | 1 (L31, filler 5) | L30, filler 15 (rank 2) |
| J-Lens | `second_product=348` | 1 (L31, filler 16) | L31, filler 15 (rank 8) |
| J-Lens | `answer=367` | 1 (L36, filler 11) | L31, filler 11 (rank 4) |
| Logit lens | `base_value=80` | 1 (L30, filler 44) | L27, filler 44 (rank 3) |
| Logit lens | `first_product=160` | 8 (L29, filler 40) | L29, filler 40 (rank 8) |
| Logit lens | `bound_value=174` | 1 (L29, filler 40) | L28, filler 40 (rank 2) |
| Logit lens | `second_product=348` | 1 (L31, filler 16) | L31, filler 16 (rank 1) |
| Logit lens | `answer=367` | 1 (L31, filler 11) | L29, filler 11 (rank 6) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 801, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=80:119589, first_product=160:111631, bound_value=174:109990, second_product=348:112139, answer=367:109327)
- Layer 10: `anta`, `fine`, `忑`, `钩`, `Hook` (target ranks: base_value=80:58464, first_product=160:61321, bound_value=174:71148, second_product=348:59845, answer=367:47101)
- Layer 20: `足`, `重`, `扣`, ` LS`, `abric` (target ranks: base_value=80:603, first_product=160:20992, bound_value=174:16501, second_product=348:22908, answer=367:5402)
- Layer 30: ` pakig`, ` talags`, `期望`, ` ninete`, `期待的` (target ranks: base_value=80:16623, first_product=160:7172, bound_value=174:737, second_product=348:28476, answer=367:399)
- Layer 35: `期盼`, ` labor`, `期望`, `363`, `往外` (target ranks: base_value=80:83880, first_product=160:94784, bound_value=174:7373, second_product=348:6569, answer=367:23)
- Layer 36: `355`, `383`, `375`, `363`, `359` (target ranks: base_value=80:127169, first_product=160:103633, bound_value=174:8127, second_product=348:2336, answer=367:28)
- Layer 37: `355`, `383`, `375`, `359`, `371` (target ranks: base_value=80:128520, first_product=160:120979, bound_value=174:12720, second_product=348:2056, answer=367:12)
- Layer 38: `375`, `383`, `355`, `373`, `387` (target ranks: base_value=80:128785, first_product=160:128441, bound_value=174:59602, second_product=348:7609, answer=367:10)
- Layer 39: `383`, `tanle`, ` spectator`, ` Noruwega`, `373` (target ranks: base_value=80:128387, first_product=160:128469, bound_value=174:123395, second_product=348:68645, answer=367:69)
- Layer 40: ` ald`, ` talags`, `Ald`, ` Ald`, ` LD` (target ranks: base_value=80:128484, first_product=160:128545, bound_value=174:122453, second_product=348:63465, answer=367:34)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `我已经`, `我记得` (target ranks: base_value=80:120451, first_product=160:117839, bound_value=174:91642, second_product=348:47526, answer=367:867)

### Filler position 2 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=80:121472, first_product=160:117262, bound_value=174:113067, second_product=348:118355, answer=367:114514)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=80:22195, first_product=160:31825, bound_value=174:41126, second_product=348:41820, answer=367:36165)
- Layer 20: ` .----`, `往常`, `ools`, `OOL`, `ophers` (target ranks: base_value=80:126396, first_product=160:128550, bound_value=174:128682, second_product=348:129143, answer=367:128073)
- Layer 30: ` talags`, ` hilabihan`, ` gilay`, ` pakig`, ` dekameters` (target ranks: base_value=80:120264, first_product=160:128787, bound_value=174:128328, second_product=348:128591, answer=367:127820)
- Layer 35: ` hilabihan`, `密密`, ` pakig`, ` .`, ` talags` (target ranks: base_value=80:109613, first_product=160:128538, bound_value=174:126753, second_product=348:127337, answer=367:127358)
- Layer 36: ` talags`, ` hilabihan`, `幽`, `adows`, `停` (target ranks: base_value=80:66719, first_product=160:124399, bound_value=174:112781, second_product=348:113215, answer=367:122134)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, `aplenty`, ` licensierad` (target ranks: base_value=80:114683, first_product=160:126358, bound_value=174:126712, second_product=348:117030, answer=367:122299)
- Layer 38: ` .`, `}<?`, ` hilabihan`, ` Erkännande`, `用了` (target ranks: base_value=80:86030, first_product=160:119815, bound_value=174:118674, second_product=348:113736, answer=367:121618)
- Layer 39: ` .`, ` hilabihan`, ` talags`, ` .↵↵`, `}<?` (target ranks: base_value=80:105695, first_product=160:115356, bound_value=174:94103, second_product=348:96129, answer=367:110831)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, `忏` (target ranks: base_value=80:72452, first_product=160:81566, bound_value=174:37495, second_product=348:46483, answer=367:70523)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `忏`, ` ,` (target ranks: base_value=80:28031, first_product=160:10150, bound_value=174:4767, second_product=348:4918, answer=367:18322)

### Filler position 3 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124950, first_product=160:120807, bound_value=174:115581, second_product=348:120809, answer=367:117564)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=80:19014, first_product=160:31233, bound_value=174:34709, second_product=348:33112, answer=367:32164)
- Layer 20: `ait`, `Ta`, `cape`, `ative`, ` ternary` (target ranks: base_value=80:1806, first_product=160:19301, bound_value=174:16800, second_product=348:26516, answer=367:23047)
- Layer 30: `算出`, `计算的`, `进行计算`, `计算出`, `计算` (target ranks: base_value=80:11622, first_product=160:45283, bound_value=174:49343, second_product=348:112603, answer=367:63943)
- Layer 35: `第一步`, `计算的`, `calcul`, `计算`, ` calculations` (target ranks: base_value=80:2185, first_product=160:39893, bound_value=174:38063, second_product=348:81206, answer=367:47014)
- Layer 36: `calcul`, `计算的`, `计算`, ` calculations`, `第一步` (target ranks: base_value=80:2995, first_product=160:30768, bound_value=174:38021, second_product=348:54442, answer=367:49105)
- Layer 37: `calcul`, `计算`, `计算的`, ` calculations`, `計算` (target ranks: base_value=80:6734, first_product=160:40114, bound_value=174:56702, second_product=348:86475, answer=367:79942)
- Layer 38: `calcul`, `计算`, ` cál`, `}<?`, `计算的` (target ranks: base_value=80:20004, first_product=160:78816, bound_value=174:88471, second_product=348:107349, answer=367:108431)
- Layer 39: ` duc`, `淤泥`, `ked`, `金黄`, `ilos` (target ranks: base_value=80:75599, first_product=160:125007, bound_value=174:95468, second_product=348:109869, answer=367:110023)
- Layer 40: ` p`, `duc`, ` duc`, `zac`, ` k` (target ranks: base_value=80:65188, first_product=160:119777, bound_value=174:72209, second_product=348:116176, answer=367:103841)
- Layer 41: ` .`, ` fifty`, `<｜end▁of▁sentence｜>`, `试一试`, ` ` (target ranks: base_value=80:66181, first_product=160:101300, bound_value=174:57263, second_product=348:67371, answer=367:86178)

### Filler position 4 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125573, first_product=160:122348, bound_value=174:116701, second_product=348:122309, answer=367:119340)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: base_value=80:14460, first_product=160:24132, bound_value=174:28951, second_product=348:24983, answer=367:25730)
- Layer 20: `ait`, `atile`, `挪`, `cape`, `atable` (target ranks: base_value=80:18107, first_product=160:47695, bound_value=174:44081, second_product=348:52462, answer=367:39513)
- Layer 30: ` tap`, `Tap`, ` Niagara`, `tap`, ` Tap` (target ranks: base_value=80:108418, first_product=160:102890, bound_value=174:88128, second_product=348:123192, answer=367:113900)
- Layer 35: ` tap`, ` Niagara`, `Tap`, ` Tap`, `tap` (target ranks: base_value=80:109063, first_product=160:103801, bound_value=174:56095, second_product=348:116815, answer=367:116833)
- Layer 36: ` tap`, `动态`, ` dynam`, `Tap`, ` Niagara` (target ranks: base_value=80:91204, first_product=160:90726, bound_value=174:41506, second_product=348:102616, answer=367:106572)
- Layer 37: ` dynam`, `动态`, `oug`, ` talags`, ` Niagara` (target ranks: base_value=80:114613, first_product=160:107075, bound_value=174:61446, second_product=348:114480, answer=367:118329)
- Layer 38: `本题分析`, ` talags`, `actors`, `geal`, `oug` (target ranks: base_value=80:122768, first_product=160:119901, bound_value=174:95743, second_product=348:122766, answer=367:124473)
- Layer 39: ` Nij`, `oug`, `本题分析`, ` talags`, `东海` (target ranks: base_value=80:114485, first_product=160:121284, bound_value=174:90300, second_product=348:112496, answer=367:115561)
- Layer 40: `oug`, ` talags`, `提问`, ` spectator`, `Question` (target ranks: base_value=80:109743, first_product=160:117554, bound_value=174:71672, second_product=348:106067, answer=367:79544)
- Layer 41: ` .`, `Question`, ` Question`, `提问`, `试一试` (target ranks: base_value=80:99405, first_product=160:90573, bound_value=174:27679, second_product=348:66414, answer=367:54430)

### Filler position 5 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125129, first_product=160:121959, bound_value=174:116417, second_product=348:122252, answer=367:119145)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: base_value=80:14339, first_product=160:25453, bound_value=174:31080, second_product=348:26336, answer=367:28205)
- Layer 20: `幽`, `能被`, ` LS`, `啦啦`, `挪` (target ranks: base_value=80:15347, first_product=160:49825, bound_value=174:49540, second_product=348:34717, answer=367:34926)
- Layer 30: `któber`, ` formulae`, `}<?`, ` Nure`, `待人` (target ranks: base_value=80:5939, first_product=160:16232, bound_value=174:195, second_product=348:12100, answer=367:23146)
- Layer 35: `174`, `173`, `774`, `374`, ` Stef` (target ranks: base_value=80:80763, first_product=160:127303, bound_value=174:1, second_product=348:142, answer=367:110710)
- Layer 36: `174`, ` Bernie`, `173`, `ukiran`, ` проп` (target ranks: base_value=80:110156, first_product=160:118950, bound_value=174:1, second_product=348:6, answer=367:111966)
- Layer 37: `174`, `�`, ` Bernie`, `�`, `348` (target ranks: base_value=80:112793, first_product=160:119328, bound_value=174:1, second_product=348:5, answer=367:107410)
- Layer 38: `174`, ` Bernie`, `�`, `348`, `�` (target ranks: base_value=80:115273, first_product=160:122518, bound_value=174:1, second_product=348:4, answer=367:101615)
- Layer 39: `174`, `�`, `348`, `<｜begin▁of▁sentence｜>`, `慧` (target ranks: base_value=80:109588, first_product=160:124411, bound_value=174:1, second_product=348:3, answer=367:43495)
- Layer 40: `174`, `�`, ` kinahabogang`, ` lur`, `<｜place▁holder▁no▁36｜>` (target ranks: base_value=80:110868, first_product=160:126469, bound_value=174:1, second_product=348:39, answer=367:6919)
- Layer 41: `174`, ` .`, ` waiting`, ` lur`, `<｜place▁holder▁no▁36｜>` (target ranks: base_value=80:113328, first_product=160:123425, bound_value=174:1, second_product=348:341, answer=367:33215)

### Filler position 6 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:124684, first_product=160:121336, bound_value=174:115894, second_product=348:122023, answer=367:118476)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13783, first_product=160:23636, bound_value=174:27206, second_product=348:23695, answer=367:25433)
- Layer 20: ` unflagged`, `<｜begin▁of▁file｜>`, `答案是`, `答案`, `�` (target ranks: base_value=80:88195, first_product=160:57199, bound_value=174:94120, second_product=348:121916, answer=367:38825)
- Layer 30: `推算`, `算出`, ` calculator`, ` Tw`, `Sequ` (target ranks: base_value=80:11711, first_product=160:19430, bound_value=174:20585, second_product=348:100473, answer=367:24741)
- Layer 35: ` Tw`, `acks`, `化解`, `Tw`, ` step` (target ranks: base_value=80:2024, first_product=160:13633, bound_value=174:4311, second_product=348:47089, answer=367:17474)
- Layer 36: ` Tw`, `Tw`, ` tw`, `柿子`, `化解` (target ranks: base_value=80:2549, first_product=160:11310, bound_value=174:6862, second_product=348:36597, answer=367:28685)
- Layer 37: ` Tw`, ` step`, `Tw`, `化解`, ` tw` (target ranks: base_value=80:3576, first_product=160:17037, bound_value=174:9393, second_product=348:69785, answer=367:30845)
- Layer 38: ` Tw`, `Tw`, `tw`, ` tw`, ` nasod` (target ranks: base_value=80:3372, first_product=160:15239, bound_value=174:9298, second_product=348:74488, answer=367:38032)
- Layer 39: ` nasod`, ` Dominic`, `把事情`, `hemer`, `ophe` (target ranks: base_value=80:52793, first_product=160:123845, bound_value=174:78332, second_product=348:120553, answer=367:99896)
- Layer 40: ` Tw`, ` nasod`, `省略`, `tw`, `Tw` (target ranks: base_value=80:44250, first_product=160:123662, bound_value=174:62434, second_product=348:121252, answer=367:100492)
- Layer 41: ` .`, ` dotted`, `那两个`, ` word`, `婷婷` (target ranks: base_value=80:93310, first_product=160:118289, bound_value=174:71557, second_product=348:111728, answer=367:106723)

### Filler position 7 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124624, first_product=160:121013, bound_value=174:115793, second_product=348:121888, answer=367:118106)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13006, first_product=160:22854, bound_value=174:26868, second_product=348:23680, answer=367:24941)
- Layer 20: `挪`, `锁定`, `atable`, `ait`, ` Walker` (target ranks: base_value=80:8305, first_product=160:33741, bound_value=174:36146, second_product=348:35554, answer=367:31235)
- Layer 30: ` Tw`, ` Zem`, `算出`, `Tw`, `calcul` (target ranks: base_value=80:9546, first_product=160:50061, bound_value=174:44920, second_product=348:107589, answer=367:51904)
- Layer 35: ` Tw`, `Tw`, ` Zem`, `acks`, `calcul` (target ranks: base_value=80:8615, first_product=160:43083, bound_value=174:36086, second_product=348:75877, answer=367:44872)
- Layer 36: ` Tw`, ` Zem`, `calcul`, `Tw`, ` zem` (target ranks: base_value=80:15008, first_product=160:44082, bound_value=174:40568, second_product=348:59735, answer=367:56127)
- Layer 37: ` Zem`, ` zem`, `calcul`, ` Zad`, ` Tw` (target ranks: base_value=80:28185, first_product=160:64966, bound_value=174:65683, second_product=348:87609, answer=367:80112)
- Layer 38: ` Zem`, ` zem`, `zem`, ` Zad`, `zac` (target ranks: base_value=80:46272, first_product=160:101031, bound_value=174:100891, second_product=348:110378, answer=367:109553)
- Layer 39: ` Zem`, ` spectator`, `zem`, `zam`, `金黄` (target ranks: base_value=80:83876, first_product=160:126264, bound_value=174:93361, second_product=348:109862, answer=367:108285)
- Layer 40: `zac`, ` spectator`, `留存`, ` talags`, `duc` (target ranks: base_value=80:68596, first_product=160:123800, bound_value=174:69542, second_product=348:105491, answer=367:96846)
- Layer 41: `zac`, ` .`, `试一试`, `留存`, `acular` (target ranks: base_value=80:65329, first_product=160:109708, bound_value=174:50508, second_product=348:70080, answer=367:76581)

### Filler position 8 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124665, first_product=160:121027, bound_value=174:115815, second_product=348:121995, answer=367:117975)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12159, first_product=160:23424, bound_value=174:27638, second_product=348:24244, answer=367:26534)
- Layer 20: `挪`, `ait`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=80:10394, first_product=160:35607, bound_value=174:33408, second_product=348:33752, answer=367:35572)
- Layer 30: ` Zem`, ` zem`, `atan`, `鞍`, `第一步` (target ranks: base_value=80:14287, first_product=160:70325, bound_value=174:70329, second_product=348:104207, answer=367:97968)
- Layer 35: ` Zem`, ` zem`, `Tap`, `鞍`, ` labor` (target ranks: base_value=80:7876, first_product=160:52664, bound_value=174:49249, second_product=348:79198, answer=367:86076)
- Layer 36: ` Zem`, ` zem`, ` dri`, `adal`, ` tap` (target ranks: base_value=80:10289, first_product=160:45233, bound_value=174:43956, second_product=348:60447, answer=367:89854)
- Layer 37: ` Zem`, ` zem`, `zem`, ` Zad`, `zac` (target ranks: base_value=80:20972, first_product=160:60132, bound_value=174:64377, second_product=348:92780, answer=367:109760)
- Layer 38: ` Zem`, ` zem`, `zem`, `zat`, ` Zel` (target ranks: base_value=80:31436, first_product=160:87096, bound_value=174:95987, second_product=348:114115, answer=367:121199)
- Layer 39: ` Zem`, `zem`, ` zem`, ` Zel`, `zat` (target ranks: base_value=80:61975, first_product=160:117012, bound_value=174:87243, second_product=348:114756, answer=367:119430)
- Layer 40: ` pals`, `acl`, ` x`, `zac`, ` Zem` (target ranks: base_value=80:49022, first_product=160:111927, bound_value=174:69155, second_product=348:110847, answer=367:103667)
- Layer 41: `鹉`, `试一试`, `acular`, `叮`, ` .` (target ranks: base_value=80:45681, first_product=160:82683, bound_value=174:47102, second_product=348:75851, answer=367:88412)

### Filler position 9 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124962, first_product=160:121449, bound_value=174:116311, second_product=348:122413, answer=367:118339)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12670, first_product=160:23967, bound_value=174:28797, second_product=348:25440, answer=367:27310)
- Layer 20: `ait`, `挪`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=80:13313, first_product=160:40438, bound_value=174:40049, second_product=348:43681, answer=367:38255)
- Layer 30: ` Zem`, ` zem`, `zem`, ` zam`, ` Zam` (target ranks: base_value=80:46414, first_product=160:90665, bound_value=174:100503, second_product=348:119072, answer=367:105700)
- Layer 35: ` Zem`, ` zem`, `zem`, ` zad`, ` Zad` (target ranks: base_value=80:20291, first_product=160:66406, bound_value=174:52112, second_product=348:94843, answer=367:88887)
- Layer 36: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=80:25212, first_product=160:64830, bound_value=174:47885, second_product=348:85252, answer=367:96728)
- Layer 37: ` Zem`, ` zem`, `zem`, ` Zad`, `因素的影响` (target ranks: base_value=80:52878, first_product=160:86064, bound_value=174:79564, second_product=348:106399, answer=367:106186)
- Layer 38: `zem`, ` Zem`, ` zem`, `}<?`, `zat` (target ranks: base_value=80:65077, first_product=160:105648, bound_value=174:104284, second_product=348:118946, answer=367:116726)
- Layer 39: ` Zem`, `zem`, ` zem`, `}<?`, `zam` (target ranks: base_value=80:88203, first_product=160:123558, bound_value=174:99274, second_product=348:121170, answer=367:117707)
- Layer 40: `y`, `šk`, ` y`, `留存`, `duc` (target ranks: base_value=80:58751, first_product=160:119979, bound_value=174:83411, second_product=348:118224, answer=367:107461)
- Layer 41: `鹉`, ` .`, `šk`, `试一试`, `acular` (target ranks: base_value=80:45488, first_product=160:94332, bound_value=174:51090, second_product=348:72764, answer=367:70021)

### Filler position 10 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124700, first_product=160:121117, bound_value=174:116044, second_product=348:122279, answer=367:117952)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11275, first_product=160:21831, bound_value=174:26700, second_product=348:23592, answer=367:25579)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `拆` (target ranks: base_value=80:11911, first_product=160:34362, bound_value=174:40263, second_product=348:39724, answer=367:36375)
- Layer 30: `�`, `alal`, `adal`, `第一步`, `平行` (target ranks: base_value=80:1570, first_product=160:29816, bound_value=174:66363, second_product=348:107878, answer=367:62821)
- Layer 35: `adal`, `alal`, `Tap`, `分解`, ` X` (target ranks: base_value=80:76, first_product=160:13015, bound_value=174:23462, second_product=348:77354, answer=367:55812)
- Layer 36: `adal`, `留存`, `分解`, ` start`, `acl` (target ranks: base_value=80:455, first_product=160:14537, bound_value=174:32453, second_product=348:83351, answer=367:72625)
- Layer 37: `}<?`, `acl`, `enal`, `翻了`, ` Zem` (target ranks: base_value=80:937, first_product=160:21198, bound_value=174:52907, second_product=348:105176, answer=367:87034)
- Layer 38: `}<?`, `zal`, `zat`, `enal`, `geal` (target ranks: base_value=80:2580, first_product=160:36959, bound_value=174:63193, second_product=348:107695, answer=367:97343)
- Layer 39: ` Xavier`, `}<?`, `𝑋`, ` xyl`, ` X` (target ranks: base_value=80:32737, first_product=160:101338, bound_value=174:79898, second_product=348:115566, answer=367:106621)
- Layer 40: ` x`, ` talags`, `acl`, `留存`, ` pals` (target ranks: base_value=80:17453, first_product=160:85095, bound_value=174:53393, second_product=348:107852, answer=367:65740)
- Layer 41: `鹉`, ` .`, `实在`, `不如`, `acular` (target ranks: base_value=80:7620, first_product=160:30872, bound_value=174:21847, second_product=348:46798, answer=367:28054)

### Filler position 11 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124728, first_product=160:121221, bound_value=174:116220, second_product=348:122466, answer=367:118084)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11462, first_product=160:22223, bound_value=174:26933, second_product=348:24144, answer=367:25818)
- Layer 20: `ait`, `锁定`, `能被`, ` smile`, ` Walker` (target ranks: base_value=80:8609, first_product=160:27175, bound_value=174:35375, second_product=348:30581, answer=367:26197)
- Layer 30: ` Mim`, `翻`, `slide`, ` mimic`, `guided` (target ranks: base_value=80:46717, first_product=160:5644, bound_value=174:1597, second_product=348:15787, answer=367:15)
- Layer 35: `347`, `349`, `383`, `367`, `359` (target ranks: base_value=80:76573, first_product=160:56568, bound_value=174:19669, second_product=348:16, answer=367:4)
- Layer 36: `367`, `368`, `369`, `383`, ` dátummal` (target ranks: base_value=80:123414, first_product=160:22633, bound_value=174:42829, second_product=348:45999, answer=367:1)
- Layer 37: `367`, `368`, `369`, `383`, `371` (target ranks: base_value=80:125661, first_product=160:21942, bound_value=174:20313, second_product=348:23545, answer=367:1)
- Layer 38: `367`, `368`, `383`, `369`, `379` (target ranks: base_value=80:129163, first_product=160:123068, bound_value=174:117000, second_product=348:67331, answer=367:1)
- Layer 39: `367`, `368`, `369`, `383`, ` Lamar` (target ranks: base_value=80:127220, first_product=160:124720, bound_value=174:127185, second_product=348:122152, answer=367:1)
- Layer 40: `367`, `368`, `clam`, `风华`, ` +:+` (target ranks: base_value=80:128222, first_product=160:126768, bound_value=174:122688, second_product=348:123735, answer=367:1)
- Layer 41: `367`, `印书馆`, ` nuest`, `沫若`, `需要注意的是` (target ranks: base_value=80:112362, first_product=160:114034, bound_value=174:111686, second_product=348:114229, answer=367:1)

### Filler position 12 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124501, first_product=160:120934, bound_value=174:116046, second_product=348:122326, answer=367:117850)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11736, first_product=160:22441, bound_value=174:27035, second_product=348:23416, answer=367:25815)
- Layer 20: `ait`, `锁定`, ` smile`, ` wig`, `挪` (target ranks: base_value=80:9484, first_product=160:28035, bound_value=174:29790, second_product=348:32508, answer=367:30110)
- Layer 30: `鞍`, ` tap`, `Tap`, ` Tap`, `tap` (target ranks: base_value=80:7421, first_product=160:18751, bound_value=174:11909, second_product=348:35215, answer=367:1965)
- Layer 35: `鞍`, ` tap`, `锁定`, `Tap`, ` Tap` (target ranks: base_value=80:6685, first_product=160:16651, bound_value=174:2537, second_product=348:7255, answer=367:1320)
- Layer 36: `acin`, ` tap`, `calcul`, `Tap`, ` Tap` (target ranks: base_value=80:16970, first_product=160:17678, bound_value=174:2595, second_product=348:3224, answer=367:1490)
- Layer 37: `acons`, ` talags`, `acin`, `calcul`, `冰冰` (target ranks: base_value=80:32414, first_product=160:19840, bound_value=174:2640, second_product=348:5924, answer=367:1306)
- Layer 38: `acons`, ` talags`, `}<?`, `ocyst`, `解放` (target ranks: base_value=80:75078, first_product=160:31371, bound_value=174:4097, second_product=348:15910, answer=367:4569)
- Layer 39: ` talags`, `}<?`, `ocyst`, `acons`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=80:117983, first_product=160:127523, bound_value=174:88329, second_product=348:67250, answer=367:2784)
- Layer 40: ` talags`, `语言文字`, ` embargo`, `渗出`, `秆` (target ranks: base_value=80:116065, first_product=160:128239, bound_value=174:97970, second_product=348:81959, answer=367:53)
- Layer 41: ` .`, `375`, `371`, `383`, `thirty` (target ranks: base_value=80:93557, first_product=160:121953, bound_value=174:45948, second_product=348:16459, answer=367:10)

### Filler position 13 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124720, first_product=160:121371, bound_value=174:116468, second_product=348:122677, answer=367:118084)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12216, first_product=160:23192, bound_value=174:27591, second_product=348:24328, answer=367:26226)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `能被` (target ranks: base_value=80:12123, first_product=160:39237, bound_value=174:36658, second_product=348:39612, answer=367:36515)
- Layer 30: ` Zem`, ` zem`, `zem`, ` Zenith`, ` Zad` (target ranks: base_value=80:41632, first_product=160:107302, bound_value=174:104531, second_product=348:121227, answer=367:108792)
- Layer 35: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=80:16283, first_product=160:87111, bound_value=174:62605, second_product=348:105150, answer=367:103065)
- Layer 36: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=80:15080, first_product=160:67734, bound_value=174:42943, second_product=348:75864, answer=367:97728)
- Layer 37: ` Zem`, `zem`, ` zem`, ` Zad`, ` Zel` (target ranks: base_value=80:32493, first_product=160:86118, bound_value=174:68422, second_product=348:93563, answer=367:101076)
- Layer 38: ` Zem`, `zem`, ` zem`, `zat`, `zel` (target ranks: base_value=80:56368, first_product=160:101986, bound_value=174:93977, second_product=348:112307, answer=367:107775)
- Layer 39: ` Zem`, `}<?`, `zem`, `zat`, ` zem` (target ranks: base_value=80:70747, first_product=160:116846, bound_value=174:87080, second_product=348:110823, answer=367:99468)
- Layer 40: ` talags`, ` pals`, `留存`, `acl`, `scr` (target ranks: base_value=80:42093, first_product=160:111089, bound_value=174:65648, second_product=348:106335, answer=367:60308)
- Layer 41: `鹉`, ` .`, `acular`, `没有被`, `ffff` (target ranks: base_value=80:18198, first_product=160:66729, bound_value=174:22417, second_product=348:43008, answer=367:10682)

### Filler position 14 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124933, first_product=160:121438, bound_value=174:116743, second_product=348:122835, answer=367:118065)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11665, first_product=160:22432, bound_value=174:26720, second_product=348:23486, answer=367:25334)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `会成为` (target ranks: base_value=80:11244, first_product=160:32463, bound_value=174:32437, second_product=348:34107, answer=367:33863)
- Layer 30: ` twice`, `平行`, ` basal`, ` Tw`, `acos` (target ranks: base_value=80:1153, first_product=160:55864, bound_value=174:25724, second_product=348:100450, answer=367:73234)
- Layer 35: ` Tw`, `Tw`, ` reserved`, `tw`, ` twice` (target ranks: base_value=80:23, first_product=160:23797, bound_value=174:3586, second_product=348:66260, answer=367:62061)
- Layer 36: ` talags`, `}<?`, ` Zem`, `留存`, ` Zad` (target ranks: base_value=80:316, first_product=160:33693, bound_value=174:8901, second_product=348:87168, answer=367:91434)
- Layer 37: `}<?`, ` doubling`, ` doubled`, ` talags`, ` doubles` (target ranks: base_value=80:1858, first_product=160:46754, bound_value=174:28051, second_product=348:104583, answer=367:101103)
- Layer 38: `}<?`, ` doubling`, `迷惑`, ` doubled`, ` doubles` (target ranks: base_value=80:7803, first_product=160:74063, bound_value=174:53048, second_product=348:115984, answer=367:114108)
- Layer 39: `}<?`, `替换`, `迷惑`, ` замен`, `叶子` (target ranks: base_value=80:36331, first_product=160:114657, bound_value=174:53056, second_product=348:102384, answer=367:88962)
- Layer 40: ` talags`, `scr`, `留存`, `zij`, `下沉` (target ranks: base_value=80:9620, first_product=160:107149, bound_value=174:16244, second_product=348:55674, answer=367:19176)
- Layer 41: ` .`, `鹉`, `zij`, `留存`, `šk` (target ranks: base_value=80:10747, first_product=160:76763, bound_value=174:8529, second_product=348:19335, answer=367:6277)

### Filler position 15 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125030, first_product=160:121572, bound_value=174:116903, second_product=348:122965, answer=367:118183)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10952, first_product=160:21151, bound_value=174:25455, second_product=348:22349, answer=367:23940)
- Layer 20: `ait`, `锁定`, `能被`, `会成为`, ` LS` (target ranks: base_value=80:6716, first_product=160:30244, bound_value=174:32164, second_product=348:26841, answer=367:26028)
- Layer 30: ` pakig`, `174`, ` eighty`, `参赛`, ` formulae` (target ranks: base_value=80:1010, first_product=160:2697, bound_value=174:2, second_product=348:3067, answer=367:15870)
- Layer 35: `174`, `774`, `374`, `348`, ` Franz` (target ranks: base_value=80:36909, first_product=160:119495, bound_value=174:1, second_product=348:4, answer=367:59971)
- Layer 36: `174`, `348`, `合规`, `贝尔`, ` Bernie` (target ranks: base_value=80:102104, first_product=160:109705, bound_value=174:1, second_product=348:2, answer=367:77398)
- Layer 37: `174`, `348`, `}<?`, `ianhi`, `�` (target ranks: base_value=80:114401, first_product=160:113950, bound_value=174:1, second_product=348:2, answer=367:75829)
- Layer 38: `174`, `348`, `�`, `�`, `蕙` (target ranks: base_value=80:114092, first_product=160:119382, bound_value=174:1, second_product=348:2, answer=367:49241)
- Layer 39: `174`, `348`, `�`, `<｜begin▁of▁sentence｜>`, `慧` (target ranks: base_value=80:101309, first_product=160:119131, bound_value=174:1, second_product=348:2, answer=367:22080)
- Layer 40: `174`, `348`, `<｜begin▁of▁file｜>`, ` lur`, `oscel` (target ranks: base_value=80:99923, first_product=160:123377, bound_value=174:1, second_product=348:2, answer=367:2859)
- Layer 41: `174`, ` twisted`, `348`, `harmonic`, ` waiting` (target ranks: base_value=80:85445, first_product=160:115835, bound_value=174:1, second_product=348:3, answer=367:9501)

### Filler position 16 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125326, first_product=160:121977, bound_value=174:117405, second_product=348:123445, answer=367:118492)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12364, first_product=160:21918, bound_value=174:26755, second_product=348:22536, answer=367:24814)
- Layer 20: `ait`, `锁定`, `幽`, ` LS`, ` smile` (target ranks: base_value=80:5834, first_product=160:26604, bound_value=174:25921, second_product=348:22460, answer=367:18919)
- Layer 30: `sets`, `往外`, `反复`, `acic`, ` simplified` (target ranks: base_value=80:2984, first_product=160:9223, bound_value=174:742, second_product=348:1066, answer=367:3397)
- Layer 35: `348`, `349`, `347`, `346`, `345` (target ranks: base_value=80:87412, first_product=160:106568, bound_value=174:995, second_product=348:1, answer=367:47)
- Layer 36: `348`, `368`, `349`, `361`, `362` (target ranks: base_value=80:127458, first_product=160:97817, bound_value=174:11409, second_product=348:1, answer=367:39)
- Layer 37: `348`, `368`, `349`, `362`, `361` (target ranks: base_value=80:127837, first_product=160:107125, bound_value=174:15470, second_product=348:1, answer=367:31)
- Layer 38: `348`, `362`, `361`, `368`, `363` (target ranks: base_value=80:129144, first_product=160:125537, bound_value=174:87828, second_product=348:1, answer=367:13)
- Layer 39: `362`, `361`, `363`, `368`, `红衣` (target ranks: base_value=80:128379, first_product=160:128227, bound_value=174:123756, second_product=348:6, answer=367:46)
- Layer 40: `361`, `aira`, ` grand`, `362`, ` double` (target ranks: base_value=80:128242, first_product=160:128453, bound_value=174:124303, second_product=348:125, answer=367:222)
- Layer 41: ` .`, `361`, `两句`, `第三百`, `362` (target ranks: base_value=80:124297, first_product=160:125524, bound_value=174:101726, second_product=348:31, answer=367:333)

### Filler position 17 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125394, first_product=160:121993, bound_value=174:117731, second_product=348:123518, answer=367:118679)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12213, first_product=160:22662, bound_value=174:27019, second_product=348:23332, answer=367:25413)
- Layer 20: ` smile`, `能被`, `而此时`, `距`, `ait` (target ranks: base_value=80:7915, first_product=160:23874, bound_value=174:25061, second_product=348:28382, answer=367:21811)
- Layer 30: ` twice`, ` Tw`, `Tw`, ` repeated`, `.tw` (target ranks: base_value=80:2028, first_product=160:11414, bound_value=174:20799, second_product=348:36837, answer=367:9795)
- Layer 35: ` Tw`, ` twice`, `Tw`, `tw`, `.tw` (target ranks: base_value=80:1258, first_product=160:8753, bound_value=174:5094, second_product=348:21823, answer=367:7341)
- Layer 36: ` Tw`, `翻`, `calcul`, ` twice`, `反复` (target ranks: base_value=80:3543, first_product=160:7243, bound_value=174:4898, second_product=348:19143, answer=367:11406)
- Layer 37: `}<?`, `翻`, `calcul`, ` doubling`, ` Nij` (target ranks: base_value=80:10049, first_product=160:9769, bound_value=174:12898, second_product=348:42457, answer=367:19306)
- Layer 38: `}<?`, `zat`, ` doubling`, ` Nij`, `calcul` (target ranks: base_value=80:21639, first_product=160:21722, bound_value=174:21621, second_product=348:58120, answer=367:28773)
- Layer 39: `}<?`, `uerak`, `ophe`, ` Nij`, ` Zwe` (target ranks: base_value=80:38917, first_product=160:100946, bound_value=174:35780, second_product=348:78098, answer=367:61201)
- Layer 40: ` Tw`, ` nasod`, `坏`, `eland`, `语言文字` (target ranks: base_value=80:24147, first_product=160:92816, bound_value=174:8153, second_product=348:37855, answer=367:31605)
- Layer 41: ` .`, ` `, `<｜end▁of▁sentence｜>`, `2`, `鹉` (target ranks: base_value=80:37148, first_product=160:77045, bound_value=174:4435, second_product=348:18650, answer=367:16010)

### Filler position 18 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125589, first_product=160:122418, bound_value=174:117983, second_product=348:123855, answer=367:119009)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12190, first_product=160:22760, bound_value=174:27135, second_product=348:24094, answer=367:25573)
- Layer 20: `ait`, ` Walker`, `锁定`, `忑`, `Walker` (target ranks: base_value=80:13813, first_product=160:32502, bound_value=174:34680, second_product=348:45437, answer=367:42480)
- Layer 30: ` resolve`, ` resolves`, ` resolved`, ` calculator`, ` resol` (target ranks: base_value=80:8955, first_product=160:30167, bound_value=174:26401, second_product=348:81952, answer=367:24119)
- Layer 35: ` resolve`, ` resolves`, ` resolved`, `resolve`, ` Tw` (target ranks: base_value=80:10871, first_product=160:26829, bound_value=174:18561, second_product=348:87436, answer=367:27245)
- Layer 36: `calcul`, ` Tw`, `计算的`, ` resolves`, ` resolve` (target ranks: base_value=80:7820, first_product=160:9428, bound_value=174:7930, second_product=348:61988, answer=367:11077)
- Layer 37: `calcul`, `计算的`, ` calcul`, ` Nij`, ` Calculators` (target ranks: base_value=80:23936, first_product=160:28349, bound_value=174:28527, second_product=348:97227, answer=367:19982)
- Layer 38: ` RES`, ` Res`, `-res`, ` resol`, `Res` (target ranks: base_value=80:32779, first_product=160:50395, bound_value=174:51156, second_product=348:104689, answer=367:26464)
- Layer 39: ` Res`, ` RES`, ` Resident`, `<｜begin▁of▁sentence｜>`, `-res` (target ranks: base_value=80:29002, first_product=160:67063, bound_value=174:51519, second_product=348:106961, answer=367:41028)
- Layer 40: ` Tw`, `šk`, `Tw`, `殿堂`, ` Nij` (target ranks: base_value=80:15744, first_product=160:45514, bound_value=174:18011, second_product=348:82632, answer=367:32551)
- Layer 41: ` twice`, ` .`, ` `, `tw`, ` Tw` (target ranks: base_value=80:16137, first_product=160:53397, bound_value=174:17933, second_product=348:63836, answer=367:28621)

### Filler position 19 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125851, first_product=160:122527, bound_value=174:118261, second_product=348:124096, answer=367:119170)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12120, first_product=160:21879, bound_value=174:26850, second_product=348:24048, answer=367:25044)
- Layer 20: `忑`, `ait`, ` Walker`, ` engaging`, `会成为` (target ranks: base_value=80:14594, first_product=160:45367, bound_value=174:46090, second_product=348:56557, answer=367:48688)
- Layer 30: ` pakig`, `oze`, `sar`, `zim`, ` consum` (target ranks: base_value=80:79051, first_product=160:120310, bound_value=174:126604, second_product=348:127987, answer=367:93605)
- Layer 35: ` riv`, ` vib`, `zim`, ` tap`, ` Rot` (target ranks: base_value=80:30045, first_product=160:102336, bound_value=174:100439, second_product=348:114127, answer=367:93726)
- Layer 36: ` riv`, ` vib`, `zim`, ` zad`, ` Riv` (target ranks: base_value=80:29133, first_product=160:82025, bound_value=174:72607, second_product=348:98177, answer=367:89387)
- Layer 37: `Quintal`, `amol`, `斐`, `zim`, `oze` (target ranks: base_value=80:54891, first_product=160:95097, bound_value=174:95716, second_product=348:114996, answer=367:103742)
- Layer 38: `zat`, `zor`, `gev`, `斐`, `}<?` (target ranks: base_value=80:74434, first_product=160:103565, bound_value=174:106695, second_product=348:111643, answer=367:110042)
- Layer 39: `斐`, ` Nij`, `zat`, `gev`, `ked` (target ranks: base_value=80:86066, first_product=160:101328, bound_value=174:86281, second_product=348:101572, answer=367:87620)
- Layer 40: `zim`, `zel`, `y`, `zat`, `zij` (target ranks: base_value=80:86372, first_product=160:107140, bound_value=174:75394, second_product=348:99917, answer=367:45483)
- Layer 41: `zel`, ` mim`, `zij`, `外商投资`, `因为这些` (target ranks: base_value=80:59002, first_product=160:42124, bound_value=174:11423, second_product=348:43267, answer=367:8733)

### Filler position 20 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125992, first_product=160:122562, bound_value=174:118506, second_product=348:124255, answer=367:119165)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11844, first_product=160:20965, bound_value=174:26443, second_product=348:22606, answer=367:24515)
- Layer 20: `ait`, ` Walker`, `锁定`, ` engaging`, `能被` (target ranks: base_value=80:11284, first_product=160:34424, bound_value=174:38398, second_product=348:33236, answer=367:31157)
- Layer 30: ` belly`, ` kahaboga`, ` pakig`, ` Mim`, `slide` (target ranks: base_value=80:46938, first_product=160:7803, bound_value=174:443, second_product=348:1787, answer=367:160)
- Layer 35: `349`, `347`, `359`, `348`, `379` (target ranks: base_value=80:72300, first_product=160:79494, bound_value=174:6370, second_product=348:4, answer=367:9)
- Layer 36: `368`, `369`, `367`, `383`, `363` (target ranks: base_value=80:126575, first_product=160:38049, bound_value=174:55590, second_product=348:106, answer=367:3)
- Layer 37: `369`, `368`, `367`, `366`, `363` (target ranks: base_value=80:127821, first_product=160:52173, bound_value=174:58935, second_product=348:313, answer=367:3)
- Layer 38: `368`, `369`, `367`, `365`, `363` (target ranks: base_value=80:129070, first_product=160:123865, bound_value=174:123640, second_product=348:712, answer=367:3)
- Layer 39: `369`, `368`, `367`, `363`, `365` (target ranks: base_value=80:126810, first_product=160:126638, bound_value=174:129054, second_product=348:122684, answer=367:3)
- Layer 40: `369`, `368`, `367`, `utum`, `attend` (target ranks: base_value=80:128361, first_product=160:127811, bound_value=174:128282, second_product=348:127577, answer=367:3)
- Layer 41: `印书馆`, `369`, `---------------+---------------+`, `))))`, `amar` (target ranks: base_value=80:122472, first_product=160:123723, bound_value=174:125964, second_product=348:121374, answer=367:8)

### Filler position 21 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126340, first_product=160:123023, bound_value=174:119011, second_product=348:124538, answer=367:119640)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10938, first_product=160:20336, bound_value=174:25337, second_product=348:21828, answer=367:24375)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `距` (target ranks: base_value=80:13499, first_product=160:30416, bound_value=174:36975, second_product=348:27728, answer=367:27054)
- Layer 30: ` tap`, `重复`, `tap`, `锁定`, ` repetition` (target ranks: base_value=80:24271, first_product=160:53849, bound_value=174:50910, second_product=348:49779, answer=367:21989)
- Layer 35: `重复`, ` tap`, `锁定`, ` repetition`, `反复` (target ranks: base_value=80:20577, first_product=160:53851, bound_value=174:28161, second_product=348:56280, answer=367:19003)
- Layer 36: `反复`, ` repeated`, ` tap`, `重复`, ` drip` (target ranks: base_value=80:13296, first_product=160:32680, bound_value=174:17732, second_product=348:29267, answer=367:15659)
- Layer 37: `反复`, ` repeated`, `冰冰`, `坏`, `}<?` (target ranks: base_value=80:21911, first_product=160:32108, bound_value=174:39944, second_product=348:52221, answer=367:12936)
- Layer 38: `}<?`, `坏`, `打磨`, `冰冰`, ` repeated` (target ranks: base_value=80:23593, first_product=160:45060, bound_value=174:53026, second_product=348:67909, answer=367:23892)
- Layer 39: `打磨`, `}<?`, `坏`, `铎`, `isis` (target ranks: base_value=80:40891, first_product=160:94146, bound_value=174:58441, second_product=348:69161, answer=367:33848)
- Layer 40: `坏`, ` .`, `isis`, `坏的`, `乐乐` (target ranks: base_value=80:17670, first_product=160:63589, bound_value=174:16834, second_product=348:32808, answer=367:11639)
- Layer 41: ` .`, ` `, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` repeated` (target ranks: base_value=80:25645, first_product=160:45544, bound_value=174:10816, second_product=348:7211, answer=367:5156)

### Filler position 22 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126419, first_product=160:123351, bound_value=174:119430, second_product=348:124896, answer=367:119851)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:10423, first_product=160:20125, bound_value=174:24981, second_product=348:21358, answer=367:24375)
- Layer 20: `ait`, `距`, `锁定`, ` Walker`, `能被` (target ranks: base_value=80:8544, first_product=160:19676, bound_value=174:28044, second_product=348:18717, answer=367:23178)
- Layer 30: ` iceberg`, `aci`, `冰冰`, `eder`, ` appendix` (target ranks: base_value=80:2227, first_product=160:967, bound_value=174:10, second_product=348:382, answer=367:4294)
- Layer 35: `348`, `349`, `354`, `347`, `358` (target ranks: base_value=80:30774, first_product=160:66399, bound_value=174:221, second_product=348:1, answer=367:211)
- Layer 36: `368`, `374`, ` hilabihan`, `488`, ` ---|---|---|---|---|---|---` (target ranks: base_value=80:119006, first_product=160:51638, bound_value=174:1846, second_product=348:7, answer=367:223)
- Layer 37: `tagHelper`, `374`, `368`, ` Liber`, `殿堂` (target ranks: base_value=80:122765, first_product=160:75309, bound_value=174:839, second_product=348:11, answer=367:439)
- Layer 38: `368`, `388`, `348`, `374`, `tagHelper` (target ranks: base_value=80:125744, first_product=160:118060, bound_value=174:13629, second_product=348:3, answer=367:89)
- Layer 39: `368`, `362`, `374`, `388`, `慕` (target ranks: base_value=80:118195, first_product=160:121866, bound_value=174:54669, second_product=348:17, answer=367:31)
- Layer 40: `368`, `ching`, `ekak`, `�`, `quire` (target ranks: base_value=80:115808, first_product=160:125154, bound_value=174:62131, second_product=348:181, answer=367:290)
- Layer 41: `))))`, `茶馆`, `�`, `}}}}`, `第三百` (target ranks: base_value=80:103588, first_product=160:120653, bound_value=174:50892, second_product=348:438, answer=367:1417)

### Filler position 23 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126667, first_product=160:123877, bound_value=174:119880, second_product=348:125398, answer=367:120233)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11635, first_product=160:21169, bound_value=174:26148, second_product=348:22387, answer=367:24345)
- Layer 20: ` smile`, `足`, `幽`, ` LS`, `距` (target ranks: base_value=80:4718, first_product=160:18919, bound_value=174:19568, second_product=348:16987, answer=367:16897)
- Layer 30: ` Tw`, ` twice`, `Tw`, `14`, `atan` (target ranks: base_value=80:4376, first_product=160:16167, bound_value=174:1560, second_product=348:21736, answer=367:22648)
- Layer 35: ` Tw`, `Tw`, `28`, `14`, ` twice` (target ranks: base_value=80:1399, first_product=160:14039, bound_value=174:1243, second_product=348:28661, answer=367:30127)
- Layer 36: ` Tw`, `28`, ` repeated`, `atan`, `留存` (target ranks: base_value=80:4447, first_product=160:16512, bound_value=174:3715, second_product=348:31374, answer=367:51169)
- Layer 37: ` doubling`, `}<?`, ` doubled`, `28`, ` doubles` (target ranks: base_value=80:18017, first_product=160:36537, bound_value=174:8211, second_product=348:73357, answer=367:99067)
- Layer 38: ` doubling`, `}<?`, `zat`, ` doubled`, `明珠` (target ranks: base_value=80:48891, first_product=160:73477, bound_value=174:33417, second_product=348:94327, answer=367:114735)
- Layer 39: `}<?`, ` doubling`, `uerak`, ` doubled`, `东海` (target ranks: base_value=80:84008, first_product=160:109085, bound_value=174:69819, second_product=348:107027, answer=367:117551)
- Layer 40: ` Zem`, ` zem`, `zem`, `坏`, ` Tw` (target ranks: base_value=80:43398, first_product=160:103223, bound_value=174:33542, second_product=348:85945, answer=367:90262)
- Layer 41: ` zem`, ` Zem`, `zij`, `坏`, `zwe` (target ranks: base_value=80:47679, first_product=160:55555, bound_value=174:9829, second_product=348:61007, answer=367:55123)

### Filler position 24 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126592, first_product=160:123817, bound_value=174:119839, second_product=348:125405, answer=367:120094)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11940, first_product=160:21379, bound_value=174:27072, second_product=348:22287, answer=367:24264)
- Layer 20: ` smile`, `ait`, `足`, `挪`, `锁定` (target ranks: base_value=80:4570, first_product=160:18062, bound_value=174:19050, second_product=348:21286, answer=367:23816)
- Layer 30: ` X`, ` x`, `adal`, `alal`, `atan` (target ranks: base_value=80:3019, first_product=160:38409, bound_value=174:11188, second_product=348:41708, answer=367:19294)
- Layer 35: ` X`, `adal`, `alal`, `重复`, ` repetition` (target ranks: base_value=80:345, first_product=160:24710, bound_value=174:7358, second_product=348:34313, answer=367:21185)
- Layer 36: `adal`, ` X`, `alal`, `羊`, `calcul` (target ranks: base_value=80:558, first_product=160:15779, bound_value=174:5495, second_product=348:22997, answer=367:23228)
- Layer 37: `}<?`, `acl`, `不急`, `calcul`, `adal` (target ranks: base_value=80:1587, first_product=160:33074, bound_value=174:16880, second_product=348:53010, answer=367:30979)
- Layer 38: `}<?`, `不急`, `acl`, `acy`, `calcul` (target ranks: base_value=80:1832, first_product=160:38345, bound_value=174:24704, second_product=348:65968, answer=367:40351)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `殿堂`, `eland`, `hemer` (target ranks: base_value=80:15188, first_product=160:86699, bound_value=174:29668, second_product=348:65436, answer=367:63865)
- Layer 40: `eland`, ` Tw`, `acl`, `坏`, `殿堂` (target ranks: base_value=80:12209, first_product=160:80451, bound_value=174:15988, second_product=348:57078, answer=367:43041)
- Layer 41: ` .`, `矶`, `omit`, `从前`, ` Tw` (target ranks: base_value=80:22479, first_product=160:79318, bound_value=174:15409, second_product=348:34560, answer=367:38976)

### Filler position 25 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126761, first_product=160:123779, bound_value=174:119985, second_product=348:125404, answer=367:120034)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12706, first_product=160:23005, bound_value=174:28119, second_product=348:23635, answer=367:25051)
- Layer 20: `ait`, ` Walker`, `锁定`, ` LS`, ` smile` (target ranks: base_value=80:7009, first_product=160:27869, bound_value=174:23090, second_product=348:27195, answer=367:26622)
- Layer 30: ` labor`, `鞍`, `atan`, `�`, `重复` (target ranks: base_value=80:15174, first_product=160:61610, bound_value=174:45800, second_product=348:84018, answer=367:44899)
- Layer 35: ` var`, ` labor`, ` equations`, ` repetition`, `锁定` (target ranks: base_value=80:12223, first_product=160:68088, bound_value=174:37998, second_product=348:73409, answer=367:50570)
- Layer 36: ` equations`, ` stabil`, ` definitions`, ` var`, `方程的` (target ranks: base_value=80:10102, first_product=160:51232, bound_value=174:22522, second_product=348:41276, answer=367:35609)
- Layer 37: ` variables`, ` definitions`, `Variables`, `变量的`, ` Variables` (target ranks: base_value=80:34360, first_product=160:95359, bound_value=174:65310, second_product=348:84852, answer=367:55142)
- Layer 38: `}<?`, `Variables`, ` Zad`, ` definitions`, ` Variables` (target ranks: base_value=80:33480, first_product=160:110973, bound_value=174:75307, second_product=348:82712, answer=367:35878)
- Layer 39: `}<?`, `script`, `<｜begin▁of▁sentence｜>`, `殿堂`, `acons` (target ranks: base_value=80:62488, first_product=160:119153, bound_value=174:73785, second_product=348:94808, answer=367:60953)
- Layer 40: ` Zem`, `zij`, `zp`, ` zem`, `殿堂` (target ranks: base_value=80:62366, first_product=160:105040, bound_value=174:52787, second_product=348:97622, answer=367:56844)
- Layer 41: `zp`, `zij`, `zion`, ` zem`, `告辞` (target ranks: base_value=80:40790, first_product=160:71654, bound_value=174:23881, second_product=348:42880, answer=367:43078)

### Filler position 26 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126857, first_product=160:123971, bound_value=174:120144, second_product=348:125579, answer=367:120225)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12266, first_product=160:22814, bound_value=174:27009, second_product=348:23136, answer=367:24410)
- Layer 20: `ait`, ` Walker`, `Walker`, `忑`, `锁定` (target ranks: base_value=80:11658, first_product=160:35015, bound_value=174:38682, second_product=348:40650, answer=367:42602)
- Layer 30: ` var`, ` labor`, ` Walker`, `Walker`, ` equations` (target ranks: base_value=80:36151, first_product=160:83036, bound_value=174:59484, second_product=348:90391, answer=367:49754)
- Layer 35: ` var`, ` variable`, ` equations`, ` labor`, `variable` (target ranks: base_value=80:15058, first_product=160:59844, bound_value=174:29557, second_product=348:58352, answer=367:35216)
- Layer 36: ` definitions`, ` var`, ` variable`, ` Definitions`, `Definitions` (target ranks: base_value=80:16531, first_product=160:56395, bound_value=174:27471, second_product=348:42582, answer=367:26798)
- Layer 37: ` definitions`, `变量的`, ` variables`, `Variables`, `Definitions` (target ranks: base_value=80:47972, first_product=160:89346, bound_value=174:63292, second_product=348:76252, answer=367:47922)
- Layer 38: ` definitions`, `Definitions`, ` Definitions`, ` definition`, `定义` (target ranks: base_value=80:61653, first_product=160:109641, bound_value=174:81922, second_product=348:81542, answer=367:26047)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, ` sublim`, ` DEF`, `下沉` (target ranks: base_value=80:77181, first_product=160:117729, bound_value=174:82505, second_product=348:107792, answer=367:73533)
- Layer 40: `下沉`, ` sublim`, `ses`, `acl`, ` consum` (target ranks: base_value=80:77012, first_product=160:110453, bound_value=174:72347, second_product=348:111131, answer=367:79419)
- Layer 41: `zij`, ` .`, `等待着`, `xyz`, `那颗` (target ranks: base_value=80:44846, first_product=160:73191, bound_value=174:40475, second_product=348:58499, answer=367:47889)

### Filler position 27 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126935, first_product=160:124154, bound_value=174:120470, second_product=348:125751, answer=367:120445)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11469, first_product=160:21357, bound_value=174:25882, second_product=348:22189, answer=367:23661)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=80:9731, first_product=160:24723, bound_value=174:29176, second_product=348:27513, answer=367:30874)
- Layer 30: ` Tw`, `Tw`, `鞍`, `重复`, ` repeated` (target ranks: base_value=80:8623, first_product=160:38870, bound_value=174:39512, second_product=348:31270, answer=367:21004)
- Layer 35: ` Tw`, `Tw`, `Number`, ` Number`, ` number` (target ranks: base_value=80:8980, first_product=160:25343, bound_value=174:28563, second_product=348:23993, answer=367:17404)
- Layer 36: ` Tw`, `Tw`, ` Number`, `Number`, ` number` (target ranks: base_value=80:10904, first_product=160:18395, bound_value=174:25545, second_product=348:13076, answer=367:14691)
- Layer 37: ` Number`, ` number`, `Number`, ` Tw`, `umber` (target ranks: base_value=80:20535, first_product=160:17340, bound_value=174:40101, second_product=348:26451, answer=367:19203)
- Layer 38: `umber`, ` Number`, ` number`, `číslo`, `zat` (target ranks: base_value=80:30994, first_product=160:38056, bound_value=174:60600, second_product=348:44719, answer=367:30368)
- Layer 39: `umber`, ` Number`, `.number`, ` number`, ` Zahl` (target ranks: base_value=80:39986, first_product=160:55414, bound_value=174:54455, second_product=348:55937, answer=367:55839)
- Layer 40: ` Tw`, `Tw`, `acl`, `oz`, `zij` (target ranks: base_value=80:25047, first_product=160:48646, bound_value=174:32409, second_product=348:57023, answer=367:44198)
- Layer 41: `zij`, `oz`, ` twice`, ` Tw`, `Tw` (target ranks: base_value=80:33093, first_product=160:38532, bound_value=174:14589, second_product=348:19797, answer=367:24442)

### Filler position 28 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127234, first_product=160:124668, bound_value=174:121063, second_product=348:126190, answer=367:120842)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11490, first_product=160:21219, bound_value=174:26392, second_product=348:22432, answer=367:24575)
- Layer 20: `ait`, `能被`, ` engaging`, `拆`, ` Walker` (target ranks: base_value=80:8321, first_product=160:23235, bound_value=174:36100, second_product=348:29950, answer=367:33854)
- Layer 30: `acin`, `第一步`, `退出`, ` expecting`, `aci` (target ranks: base_value=80:113, first_product=160:3379, bound_value=174:657, second_product=348:6372, answer=367:11881)
- Layer 35: `348`, `349`, `347`, `174`, `346` (target ranks: base_value=80:13751, first_product=160:113606, bound_value=174:4, second_product=348:1, answer=367:14719)
- Layer 36: `348`, `349`, `347`, `174`, `烦恼` (target ranks: base_value=80:97038, first_product=160:119883, bound_value=174:4, second_product=348:1, answer=367:3448)
- Layer 37: `348`, `347`, `349`, `174`, ` Naamsvermelding` (target ranks: base_value=80:116017, first_product=160:122882, bound_value=174:4, second_product=348:1, answer=367:1497)
- Layer 38: `348`, `347`, `349`, `�`, `346` (target ranks: base_value=80:114982, first_product=160:126067, bound_value=174:11, second_product=348:1, answer=367:1465)
- Layer 39: `348`, `347`, `349`, `�`, `烦恼` (target ranks: base_value=80:97901, first_product=160:124847, bound_value=174:15, second_product=348:1, answer=367:5205)
- Layer 40: `348`, `347`, `349`, `plier`, `ching` (target ranks: base_value=80:102373, first_product=160:126031, bound_value=174:93, second_product=348:1, answer=367:972)
- Layer 41: `348`, `347`, `349`, ` twisted`, `plier` (target ranks: base_value=80:75402, first_product=160:111469, bound_value=174:40, second_product=348:1, answer=367:1140)

### Filler position 29 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127030, first_product=160:124323, bound_value=174:120595, second_product=348:125958, answer=367:120336)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11701, first_product=160:21559, bound_value=174:26793, second_product=348:23047, answer=367:24967)
- Layer 20: `能被`, ` smile`, `ession`, `锁定`, `aty` (target ranks: base_value=80:7353, first_product=160:13989, bound_value=174:18610, second_product=348:21800, answer=367:25800)
- Layer 30: ` Zem`, ` zem`, `忽略`, `zem`, ` ignored` (target ranks: base_value=80:34064, first_product=160:44238, bound_value=174:23367, second_product=348:95783, answer=367:32032)
- Layer 35: ` Zem`, ` zem`, `忽略`, ` ignoring`, `感兴趣` (target ranks: base_value=80:21142, first_product=160:42522, bound_value=174:15349, second_product=348:92769, answer=367:43026)
- Layer 36: ` Zem`, `忽略`, ` zem`, `感兴趣`, `感兴趣的` (target ranks: base_value=80:22548, first_product=160:26944, bound_value=174:9831, second_product=348:83921, answer=367:49791)
- Layer 37: ` Zem`, `}<?`, ` zem`, `zem`, `yat` (target ranks: base_value=80:47184, first_product=160:46654, bound_value=174:32709, second_product=348:111217, answer=367:74212)
- Layer 38: ` Zem`, ` zem`, `zem`, `}<?`, `yat` (target ranks: base_value=80:34771, first_product=160:53513, bound_value=174:40868, second_product=348:115996, answer=367:93495)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, ` Zem`, `叶子`, `迷惑` (target ranks: base_value=80:72941, first_product=160:97967, bound_value=174:62518, second_product=348:119967, answer=367:102769)
- Layer 40: `坏`, `y`, ` Tw`, ` consum`, `坏的` (target ranks: base_value=80:46766, first_product=160:86855, bound_value=174:36169, second_product=348:107800, answer=367:73769)
- Layer 41: ` .`, ` waiting`, `等待`, `坏`, `从前` (target ranks: base_value=80:28287, first_product=160:43940, bound_value=174:6235, second_product=348:28948, answer=367:26392)

### Filler position 30 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127165, first_product=160:124562, bound_value=174:120783, second_product=348:126160, answer=367:120698)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11343, first_product=160:20684, bound_value=174:25870, second_product=348:22225, answer=367:24367)
- Layer 20: ` smile`, `ait`, ` LS`, `atile`, `锁定` (target ranks: base_value=80:6030, first_product=160:19467, bound_value=174:21457, second_product=348:27294, answer=367:34011)
- Layer 30: `code`, ` SK`, `�`, `yg`, ` tap` (target ranks: base_value=80:31919, first_product=160:90700, bound_value=174:66815, second_product=348:101314, answer=367:79190)
- Layer 35: ` tap`, ` Wil`, `Tap`, ` flip`, `退出` (target ranks: base_value=80:30431, first_product=160:97777, bound_value=174:34096, second_product=348:93948, answer=367:95034)
- Layer 36: ` dynam`, ` rip`, `acin`, ` tap`, ` Tw` (target ranks: base_value=80:18695, first_product=160:67474, bound_value=174:21689, second_product=348:64747, answer=367:80868)
- Layer 37: `}<?`, ` tare`, ` dynam`, ` orb`, `edip` (target ranks: base_value=80:40601, first_product=160:90585, bound_value=174:44436, second_product=348:100631, answer=367:103781)
- Layer 38: `}<?`, `zat`, ` duc`, `pac`, `zos` (target ranks: base_value=80:60655, first_product=160:105548, bound_value=174:75553, second_product=348:112938, answer=367:112518)
- Layer 39: `}<?`, ` rib`, ` duc`, ` Nij`, `本题分析` (target ranks: base_value=80:82231, first_product=160:110320, bound_value=174:82463, second_product=348:96668, answer=367:96069)
- Layer 40: `zel`, ` rib`, ` fum`, `zik`, ` rov` (target ranks: base_value=80:65532, first_product=160:95406, bound_value=174:54093, second_product=348:70575, answer=367:69244)
- Layer 41: `Question`, ` tare`, ` Question`, `zel`, ` fum` (target ranks: base_value=80:38342, first_product=160:31542, bound_value=174:5018, second_product=348:22013, answer=367:11967)

### Filler position 31 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127444, first_product=160:124959, bound_value=174:121495, second_product=348:126476, answer=367:121370)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11025, first_product=160:19930, bound_value=174:25153, second_product=348:21641, answer=367:23639)
- Layer 20: `锁定`, ` smile`, `ait`, `鞍`, ` wig` (target ranks: base_value=80:6748, first_product=160:19124, bound_value=174:19061, second_product=348:20812, answer=367:25471)
- Layer 30: ` tap`, `答案`, `回答`, ` answer`, `tap` (target ranks: base_value=80:57899, first_product=160:72716, bound_value=174:19894, second_product=348:70899, answer=367:46896)
- Layer 35: ` answer`, ` پاسخ`, ` rational`, ` Answer`, `rational` (target ranks: base_value=80:60505, first_product=160:61291, bound_value=174:2645, second_product=348:67054, answer=367:65435)
- Layer 36: ` tap`, ` riv`, ` answer`, `Tap`, `ikuha` (target ranks: base_value=80:19754, first_product=160:18611, bound_value=174:1575, second_product=348:18706, answer=367:50019)
- Layer 37: `rational`, ` rational`, `issors`, `}<?`, ` پاسخ` (target ranks: base_value=80:32632, first_product=160:18536, bound_value=174:2379, second_product=348:30017, answer=367:66504)
- Layer 38: `}<?`, `rational`, ` nasod`, ` RES`, `aharan` (target ranks: base_value=80:43012, first_product=160:14595, bound_value=174:3199, second_product=348:30720, answer=367:58173)
- Layer 39: `}<?`, `aharan`, `<｜begin▁of▁sentence｜>`, `hemer`, ` heavenly` (target ranks: base_value=80:68495, first_product=160:89816, bound_value=174:18232, second_product=348:65382, answer=367:89843)
- Layer 40: ` Answer`, ` nasod`, `acular`, `acl`, `Answer` (target ranks: base_value=80:31208, first_product=160:66862, bound_value=174:2220, second_product=348:25441, answer=367:8184)
- Layer 41: `Answer`, `试一试`, `y`, ` Answer`, ` .` (target ranks: base_value=80:19519, first_product=160:27132, bound_value=174:218, second_product=348:3919, answer=367:1679)

### Filler position 32 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127284, first_product=160:124657, bound_value=174:121052, second_product=348:126338, answer=367:120624)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10876, first_product=160:19980, bound_value=174:24247, second_product=348:20837, answer=367:23435)
- Layer 20: ` Walker`, ` ES`, ` engaging`, `ait`, `Walker` (target ranks: base_value=80:6912, first_product=160:21915, bound_value=174:21397, second_product=348:17904, answer=367:29484)
- Layer 30: `算出`, ` x`, `antal`, `�`, ` X` (target ranks: base_value=80:2276, first_product=160:41168, bound_value=174:53327, second_product=348:98216, answer=367:99208)
- Layer 35: ` x`, ` X`, `antal`, `第一步`, `adal` (target ranks: base_value=80:239, first_product=160:16973, bound_value=174:21623, second_product=348:69063, answer=367:82426)
- Layer 36: ` x`, `antal`, ` XCT`, ` X`, `第一步` (target ranks: base_value=80:265, first_product=160:10094, bound_value=174:15900, second_product=348:42924, answer=367:85828)
- Layer 37: ` XCT`, ` pals`, ` x`, `udal`, `}<?` (target ranks: base_value=80:705, first_product=160:6269, bound_value=174:20738, second_product=348:68926, answer=367:97284)
- Layer 38: ` XCT`, ` x`, ` pals`, ` Pax`, `geal` (target ranks: base_value=80:993, first_product=160:11276, bound_value=174:26812, second_product=348:82530, answer=367:104957)
- Layer 39: ` x`, ` XCT`, ` X`, ` Xavier`, ` XAF` (target ranks: base_value=80:13935, first_product=160:49683, bound_value=174:30385, second_product=348:62472, answer=367:94406)
- Layer 40: ` pals`, ` x`, `坏的`, `calcul`, ` p` (target ranks: base_value=80:9506, first_product=160:37169, bound_value=174:12502, second_product=348:40035, answer=367:34058)
- Layer 41: ` pals`, `步骤如下`, ` .`, ` compounded`, `那两个` (target ranks: base_value=80:11508, first_product=160:12277, bound_value=174:3665, second_product=348:19186, answer=367:16871)

### Filler position 33 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127569, first_product=160:125262, bound_value=174:121843, second_product=348:126726, answer=367:121506)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10410, first_product=160:20098, bound_value=174:23664, second_product=348:20436, answer=367:22636)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=80:7176, first_product=160:24551, bound_value=174:21758, second_product=348:20087, answer=367:27908)
- Layer 30: `adal`, `antal`, ` Zem`, ` basal`, `acin` (target ranks: base_value=80:7209, first_product=160:66150, bound_value=174:38737, second_product=348:67218, answer=367:42109)
- Layer 35: `adal`, `antal`, ` Zem`, `alal`, ` repetition` (target ranks: base_value=80:1656, first_product=160:31182, bound_value=174:7191, second_product=348:30203, answer=367:26011)
- Layer 36: `adal`, `留存`, `antal`, ` Zem`, `反复` (target ranks: base_value=80:4068, first_product=160:30807, bound_value=174:8158, second_product=348:25091, answer=367:32725)
- Layer 37: ` Zem`, `}<?`, `zem`, `TreeLabel`, `不加` (target ranks: base_value=80:16093, first_product=160:56994, bound_value=174:23172, second_product=348:54992, answer=367:49897)
- Layer 38: ` Zem`, `}<?`, `zem`, `zat`, `不加` (target ranks: base_value=80:15727, first_product=160:65874, bound_value=174:34834, second_product=348:75173, answer=367:61532)
- Layer 39: ` Zem`, `zem`, `}<?`, ` Zahl`, `迷惑` (target ranks: base_value=80:29656, first_product=160:94880, bound_value=174:49832, second_product=348:99801, answer=367:99971)
- Layer 40: ` Zem`, ` zem`, `留存`, ` pals`, `zem` (target ranks: base_value=80:7896, first_product=160:66063, bound_value=174:24263, second_product=348:73307, answer=367:50503)
- Layer 41: ` compounding`, ` whichever`, ` zem`, ` Zem`, ` ` (target ranks: base_value=80:8011, first_product=160:36670, bound_value=174:11102, second_product=348:29915, answer=367:28952)

### Filler position 34 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127699, first_product=160:125436, bound_value=174:122129, second_product=348:126864, answer=367:121670)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10980, first_product=160:20865, bound_value=174:24207, second_product=348:20910, answer=367:22816)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, `Walker` (target ranks: base_value=80:7919, first_product=160:27385, bound_value=174:23689, second_product=348:22325, answer=367:25853)
- Layer 30: `重复`, `锁定`, ` dy`, `acin`, ` reserved` (target ranks: base_value=80:14147, first_product=160:49350, bound_value=174:34381, second_product=348:54343, answer=367:40738)
- Layer 35: `询问`, ` quadr`, ` question`, ` reserved`, ` Question` (target ranks: base_value=80:8482, first_product=160:44865, bound_value=174:24609, second_product=348:41945, answer=367:40062)
- Layer 36: ` question`, ` Question`, `询问`, `提问`, `Question` (target ranks: base_value=80:13473, first_product=160:31630, bound_value=174:21899, second_product=348:33791, answer=367:35169)
- Layer 37: `.question`, ` question`, ` Question`, `提问`, `Question` (target ranks: base_value=80:35745, first_product=160:53749, bound_value=174:45840, second_product=348:69231, answer=367:51202)
- Layer 38: ` Question`, `.question`, ` question`, ` প্রশ`, `zat` (target ranks: base_value=80:35351, first_product=160:66710, bound_value=174:47248, second_product=348:70621, answer=367:64105)
- Layer 39: `.question`, ` Question`, `}<?`, `迷惑`, `/question` (target ranks: base_value=80:51606, first_product=160:81712, bound_value=174:50783, second_product=348:92875, answer=367:86351)
- Layer 40: ` Zem`, `zij`, ` zem`, `zem`, `acl` (target ranks: base_value=80:40385, first_product=160:61183, bound_value=174:27601, second_product=348:85762, answer=367:65138)
- Layer 41: `zij`, ` compounded`, ` zem`, `zel`, ` whichever` (target ranks: base_value=80:23264, first_product=160:25379, bound_value=174:7651, second_product=348:43672, answer=367:38701)

### Filler position 35 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127643, first_product=160:125227, bound_value=174:121868, second_product=348:126719, answer=367:121382)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12168, first_product=160:21833, bound_value=174:25820, second_product=348:21971, answer=367:24020)
- Layer 20: ` smile`, `足`, `ait`, `锁定`, `幽` (target ranks: base_value=80:3952, first_product=160:12400, bound_value=174:17335, second_product=348:15871, answer=367:14575)
- Layer 30: `Conc`, `383`, `219`, ` simplified`, `379` (target ranks: base_value=80:32229, first_product=160:1533, bound_value=174:211, second_product=348:7003, answer=367:49)
- Layer 35: `383`, `保留`, `379`, `359`, `387` (target ranks: base_value=80:72404, first_product=160:77183, bound_value=174:4750, second_product=348:988, answer=367:10)
- Layer 36: `383`, `371`, `389`, `387`, `359` (target ranks: base_value=80:120556, first_product=160:80090, bound_value=174:5961, second_product=348:510, answer=367:17)
- Layer 37: `383`, `}<?`, `387`, `371`, `367` (target ranks: base_value=80:126687, first_product=160:101136, bound_value=174:17489, second_product=348:756, answer=367:5)
- Layer 38: `}<?`, `383`, `387`, ` sumala`, ` Noruwega` (target ranks: base_value=80:127945, first_product=160:121871, bound_value=174:46615, second_product=348:3734, answer=367:6)
- Layer 39: `}<?`, `interpret`, `慕`, `ozygous`, `本题分析` (target ranks: base_value=80:127900, first_product=160:127906, bound_value=174:119650, second_product=348:70123, answer=367:23)
- Layer 40: `aldehyde`, `}<?`, `靴`, ` kinahabogang`, `坏` (target ranks: base_value=80:128011, first_product=160:128210, bound_value=174:123051, second_product=348:87079, answer=367:24)
- Layer 41: ` Question`, `需要注意的是`, `有的时候`, `然而`, `zel` (target ranks: base_value=80:106589, first_product=160:113678, bound_value=174:71858, second_product=348:34858, answer=367:17)

### Filler position 36 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127699, first_product=160:125583, bound_value=174:122222, second_product=348:126979, answer=367:121812)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13325, first_product=160:23298, bound_value=174:28729, second_product=348:23749, answer=367:26151)
- Layer 20: `ait`, `能被`, ` Walker`, ` engaging`, `距` (target ranks: base_value=80:9892, first_product=160:27651, bound_value=174:27953, second_product=348:25174, answer=367:28941)
- Layer 30: ` twice`, ` Tw`, `算出`, `Tw`, `乘` (target ranks: base_value=80:10512, first_product=160:5224, bound_value=174:3830, second_product=348:17997, answer=367:8650)
- Layer 35: ` Tw`, `cape`, `算出`, `acic`, ` twice` (target ranks: base_value=80:7807, first_product=160:18303, bound_value=174:554, second_product=348:133, answer=367:1878)
- Layer 36: `算出`, `calcul`, `计算的`, `}<?`, `陪` (target ranks: base_value=80:30503, first_product=160:21380, bound_value=174:985, second_product=348:99, answer=367:4728)
- Layer 37: `}<?`, ` Nij`, `ajes`, `aje`, `Tinubdan` (target ranks: base_value=80:59707, first_product=160:38324, bound_value=174:3011, second_product=348:439, answer=367:10708)
- Layer 38: `}<?`, ` Nij`, `ajes`, `zat`, `aje` (target ranks: base_value=80:66339, first_product=160:57683, bound_value=174:11415, second_product=348:1653, answer=367:28402)
- Layer 39: `}<?`, ` Nij`, `ajes`, `zat`, `interpret` (target ranks: base_value=80:70300, first_product=160:89665, bound_value=174:31236, second_product=348:11069, answer=367:44493)
- Layer 40: `}<?`, ` substr`, `zij`, ` Nij`, `duc` (target ranks: base_value=80:44575, first_product=160:76392, bound_value=174:9520, second_product=348:4830, answer=367:6407)
- Layer 41: `2`, ` `, ` twist`, `zel`, `zij` (target ranks: base_value=80:17244, first_product=160:43417, bound_value=174:4838, second_product=348:1248, answer=367:2395)

### Filler position 37 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127652, first_product=160:125523, bound_value=174:122119, second_product=348:126940, answer=367:121670)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13232, first_product=160:22944, bound_value=174:29066, second_product=348:24405, answer=367:25988)
- Layer 20: ` engaging`, `能被`, `忑`, ` Engaging`, ` smile` (target ranks: base_value=80:12353, first_product=160:34479, bound_value=174:32659, second_product=348:48722, answer=367:46780)
- Layer 30: ` twice`, `Tw`, ` Tw`, `.tw`, `atan` (target ranks: base_value=80:377, first_product=160:24347, bound_value=174:45295, second_product=348:83965, answer=367:74741)
- Layer 35: ` twice`, ` Tw`, `80`, `Tw`, `出生` (target ranks: base_value=80:3, first_product=160:17046, bound_value=174:29932, second_product=348:77062, answer=367:90138)
- Layer 36: `}<?`, ` doubling`, `翻`, `留存`, `radesh` (target ranks: base_value=80:24, first_product=160:20406, bound_value=174:41418, second_product=348:78158, answer=367:108828)
- Layer 37: `}<?`, ` doubles`, ` doubling`, ` doubled`, `TreeLabel` (target ranks: base_value=80:82, first_product=160:29688, bound_value=174:75881, second_product=348:102768, answer=367:114090)
- Layer 38: `}<?`, `不加`, `dividers`, ` doubling`, `zat` (target ranks: base_value=80:356, first_product=160:66185, bound_value=174:103220, second_product=348:119724, answer=367:125097)
- Layer 39: `}<?`, `迷惑`, `dividers`, `ounder`, `�乐` (target ranks: base_value=80:7230, first_product=160:87019, bound_value=174:70869, second_product=348:93890, answer=367:103715)
- Layer 40: `acular`, ` substr`, `留存`, `accur`, ` germ` (target ranks: base_value=80:758, first_product=160:65210, bound_value=174:23995, second_product=348:33100, answer=367:34231)
- Layer 41: ` `, ` .`, `从前`, `步骤如下`, ` waiting` (target ranks: base_value=80:1087, first_product=160:33024, bound_value=174:10435, second_product=348:6757, answer=367:13252)

### Filler position 38 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127768, first_product=160:125703, bound_value=174:122440, second_product=348:127120, answer=367:121934)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12137, first_product=160:21414, bound_value=174:27162, second_product=348:23130, answer=367:24848)
- Layer 20: `忑`, `ait`, `能被`, ` engaging`, `会成为` (target ranks: base_value=80:14989, first_product=160:41925, bound_value=174:45862, second_product=348:50445, answer=367:49192)
- Layer 30: ` kahaboga`, ` Mim`, ` belly`, `翻`, `下沉` (target ranks: base_value=80:35487, first_product=160:20650, bound_value=174:2999, second_product=348:6023, answer=367:1130)
- Layer 35: `349`, `347`, `383`, `399`, `359` (target ranks: base_value=80:53436, first_product=160:75789, bound_value=174:10090, second_product=348:9, answer=367:15)
- Layer 36: `368`, `383`, `369`, `367`, `389` (target ranks: base_value=80:119212, first_product=160:48906, bound_value=174:34619, second_product=348:1474, answer=367:4)
- Layer 37: `368`, `369`, `367`, `383`, `379` (target ranks: base_value=80:122992, first_product=160:54553, bound_value=174:33042, second_product=348:2083, answer=367:3)
- Layer 38: `368`, `367`, `369`, `383`, `379` (target ranks: base_value=80:128914, first_product=160:127206, bound_value=174:120646, second_product=348:3133, answer=367:2)
- Layer 39: `368`, `369`, `367`, `383`, `363` (target ranks: base_value=80:125286, first_product=160:126967, bound_value=174:127793, second_product=348:111221, answer=367:3)
- Layer 40: ` burge`, `369`, `368`, `iator`, `clam` (target ranks: base_value=80:126676, first_product=160:127424, bound_value=174:125522, second_product=348:116310, answer=367:19)
- Layer 41: `zion`, `印书馆`, `需要注意的是`, ` twice`, `))))` (target ranks: base_value=80:89447, first_product=160:112609, bound_value=174:99884, second_product=348:83180, answer=367:85)

### Filler position 39 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127920, first_product=160:125767, bound_value=174:122634, second_product=348:127195, answer=367:121878)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11747, first_product=160:20895, bound_value=174:26152, second_product=348:22125, answer=367:24704)
- Layer 20: `锁定`, `ait`, `忑`, `鞍`, ` Walker` (target ranks: base_value=80:7530, first_product=160:21874, bound_value=174:24632, second_product=348:30880, answer=367:30587)
- Layer 30: `sac`, `689`, `79`, ` calculator`, `退出` (target ranks: base_value=80:1080, first_product=160:4497, bound_value=174:1318, second_product=348:8993, answer=367:725)
- Layer 35: `退出`, ` calculator`, `打完`, ` future`, `obin` (target ranks: base_value=80:2316, first_product=160:12320, bound_value=174:553, second_product=348:2674, answer=367:638)
- Layer 36: `aci`, `退出`, `等待着`, `北京的`, `acin` (target ranks: base_value=80:8774, first_product=160:9656, bound_value=174:1023, second_product=348:1069, answer=367:657)
- Layer 37: `}<?`, `在北京`, `北京的`, `381`, `382` (target ranks: base_value=80:65353, first_product=160:19827, bound_value=174:2297, second_product=348:992, answer=367:118)
- Layer 38: `}<?`, ` Noruwega`, ` mach`, `malink`, ` smoot` (target ranks: base_value=80:86484, first_product=160:54225, bound_value=174:7870, second_product=348:5312, answer=367:712)
- Layer 39: `}<?`, ` Noruwega`, `书馆`, `?datasetId`, `aharoa` (target ranks: base_value=80:126646, first_product=160:128502, bound_value=174:102047, second_product=348:24716, answer=367:204)
- Layer 40: `369`, `渗出`, `367`, `oug`, `368` (target ranks: base_value=80:127788, first_product=160:128710, bound_value=174:120175, second_product=348:47105, answer=367:3)
- Layer 41: `369`, `367`, `375`, ` waiting`, `383` (target ranks: base_value=80:118604, first_product=160:127911, bound_value=174:78694, second_product=348:24807, answer=367:2)

### Filler position 40 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=80:127967, first_product=160:125979, bound_value=174:122914, second_product=348:127364, answer=367:122157)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12160, first_product=160:21344, bound_value=174:26966, second_product=348:22088, answer=367:26003)
- Layer 20: `ait`, `能被`, ` Walker`, `锁定`, `Walker` (target ranks: base_value=80:5503, first_product=160:20686, bound_value=174:31465, second_product=348:19532, answer=367:27297)
- Layer 30: ` belly`, ` perturb`, ` chaper`, `iahy`, ` bubble` (target ranks: base_value=80:19765, first_product=160:223, bound_value=174:76, second_product=348:72, answer=367:374)
- Layer 35: `348`, `349`, `347`, `368`, `346` (target ranks: base_value=80:101186, first_product=160:80373, bound_value=174:3336, second_product=348:1, answer=367:7)
- Layer 36: `368`, `367`, `366`, `361`, `364` (target ranks: base_value=80:128498, first_product=160:18818, bound_value=174:70896, second_product=348:10, answer=367:2)
- Layer 37: `368`, `367`, `366`, `364`, `361` (target ranks: base_value=80:128665, first_product=160:19315, bound_value=174:56128, second_product=348:13, answer=367:2)
- Layer 38: `368`, `367`, `365`, `363`, `366` (target ranks: base_value=80:129206, first_product=160:103433, bound_value=174:116740, second_product=348:29, answer=367:2)
- Layer 39: `367`, `368`, `363`, `365`, `362` (target ranks: base_value=80:128289, first_product=160:123058, bound_value=174:128663, second_product=348:69153, answer=367:1)
- Layer 40: `367`, `368`, `363`, `<｜begin▁of▁file｜>`, `erin` (target ranks: base_value=80:128603, first_product=160:126673, bound_value=174:127625, second_product=348:106775, answer=367:1)
- Layer 41: `367`, `<｜begin▁of▁file｜>`, `---------------+---------------+`, `))))`, ` +:+` (target ranks: base_value=80:123499, first_product=160:115767, bound_value=174:115798, second_product=348:83315, answer=367:1)

### Filler position 41 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=80:128019, first_product=160:126132, bound_value=174:123018, second_product=348:127472, answer=367:122166)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12112, first_product=160:21423, bound_value=174:26692, second_product=348:22162, answer=367:25927)
- Layer 20: `ait`, `锁定`, `能被`, ` LS`, ` smile` (target ranks: base_value=80:6128, first_product=160:19664, bound_value=174:20029, second_product=348:16267, answer=367:23733)
- Layer 30: `}<?`, `三十六`, ` smoot`, `iab`, `平滑` (target ranks: base_value=80:8778, first_product=160:8603, bound_value=174:285, second_product=348:1286, answer=367:5080)
- Layer 35: `348`, `349`, `374`, `347`, ` sumala` (target ranks: base_value=80:97101, first_product=160:126978, bound_value=174:6, second_product=348:1, answer=367:1862)
- Layer 36: `348`, `374`, `349`, `347`, `174` (target ranks: base_value=80:124217, first_product=160:110158, bound_value=174:5, second_product=348:1, answer=367:2768)
- Layer 37: `348`, `349`, `374`, `347`, `174` (target ranks: base_value=80:126469, first_product=160:105899, bound_value=174:5, second_product=348:1, answer=367:622)
- Layer 38: `348`, `349`, `374`, `347`, `372` (target ranks: base_value=80:128628, first_product=160:121152, bound_value=174:20, second_product=348:1, answer=367:563)
- Layer 39: `348`, `349`, `347`, `桃花`, `374` (target ranks: base_value=80:126850, first_product=160:121886, bound_value=174:194, second_product=348:1, answer=367:3866)
- Layer 40: `348`, `349`, `374`, `372`, `347` (target ranks: base_value=80:121871, first_product=160:120817, bound_value=174:95, second_product=348:1, answer=367:51)
- Layer 41: `348`, `349`, `374`, ` expectation`, ` waiting` (target ranks: base_value=80:107885, first_product=160:110371, bound_value=174:107, second_product=348:1, answer=367:289)

### Filler position 42 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127920, first_product=160:125802, bound_value=174:122523, second_product=348:127183, answer=367:121916)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12640, first_product=160:21787, bound_value=174:26626, second_product=348:22432, answer=367:25770)
- Layer 20: ` smile`, `锁定`, `鞍`, ` LS`, `ession` (target ranks: base_value=80:4305, first_product=160:13008, bound_value=174:13166, second_product=348:11646, answer=367:17146)
- Layer 30: ` ninete`, `acos`, `ukiran`, `duct`, ` smoot` (target ranks: base_value=80:43152, first_product=160:15383, bound_value=174:2379, second_product=348:5417, answer=367:1123)
- Layer 35: `349`, `鞍`, `保留`, `ensky`, ` Kaw` (target ranks: base_value=80:23088, first_product=160:21415, bound_value=174:7769, second_product=348:19, answer=367:424)
- Layer 36: `ottenham`, ` XIX`, `保温`, `坏`, `368` (target ranks: base_value=80:84407, first_product=160:16997, bound_value=174:52342, second_product=348:5239, answer=367:32)
- Layer 37: `Liber`, ` Liber`, `368`, `367`, `-ulo` (target ranks: base_value=80:112312, first_product=160:18929, bound_value=174:50930, second_product=348:3607, answer=367:4)
- Layer 38: `367`, ` ninete`, `368`, ` ---|---|---|---|---|---|---`, `-ulo` (target ranks: base_value=80:128186, first_product=160:118120, bound_value=174:122720, second_product=348:12722, answer=367:1)
- Layer 39: `367`, `-ulo`, `368`, `�`, `ospor` (target ranks: base_value=80:125799, first_product=160:125951, bound_value=174:127596, second_product=348:97191, answer=367:1)
- Layer 40: `语言文字`, ` bund`, `坏`, ` bursting`, `клад` (target ranks: base_value=80:125344, first_product=160:127518, bound_value=174:125968, second_product=348:108668, answer=367:34)
- Layer 41: `zion`, ` .`, ` twice`, `�`, ` */` (target ranks: base_value=80:75285, first_product=160:98959, bound_value=174:65967, second_product=348:30351, answer=367:17)

### Filler position 43 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=80:127991, first_product=160:125990, bound_value=174:122834, second_product=348:127350, answer=367:122311)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12617, first_product=160:22181, bound_value=174:26602, second_product=348:22977, answer=367:25432)
- Layer 20: `忑`, `锁定`, `ait`, ` ES`, ` smile` (target ranks: base_value=80:6888, first_product=160:19082, bound_value=174:25480, second_product=348:21399, answer=367:28877)
- Layer 30: `退出`, ` reliably`, ` Heidelberg`, `iab`, `exerc` (target ranks: base_value=80:398, first_product=160:2852, bound_value=174:323, second_product=348:46636, answer=367:25563)
- Layer 35: `174`, `173`, ` President`, ` Concern`, `Conc` (target ranks: base_value=80:11158, first_product=160:75730, bound_value=174:1, second_product=348:4000, answer=367:89250)
- Layer 36: `174`, `}<?`, `�`, ` Franz`, `adir` (target ranks: base_value=80:45260, first_product=160:39042, bound_value=174:1, second_product=348:7344, answer=367:107975)
- Layer 37: `174`, `}<?`, `�`, `adir`, `副院长` (target ranks: base_value=80:85308, first_product=160:34001, bound_value=174:1, second_product=348:15963, answer=367:117502)
- Layer 38: `174`, `副院长`, `}<?`, `�`, `院长` (target ranks: base_value=80:94308, first_product=160:44486, bound_value=174:1, second_product=348:23886, answer=367:117020)
- Layer 39: `174`, `�`, `}<?`, `院长`, `opters` (target ranks: base_value=80:77206, first_product=160:54630, bound_value=174:1, second_product=348:1763, answer=367:55458)
- Layer 40: `174`, `菁`, `}<?`, `院长`, `anium` (target ranks: base_value=80:55459, first_product=160:58815, bound_value=174:1, second_product=348:344, answer=367:210)
- Layer 41: `174`, ` .`, ` number`, `的计算`, `院长` (target ranks: base_value=80:43824, first_product=160:37584, bound_value=174:1, second_product=348:537, answer=367:138)

### Filler position 44 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=80:127993, first_product=160:126029, bound_value=174:122879, second_product=348:127453, answer=367:122107)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13275, first_product=160:22771, bound_value=174:27392, second_product=348:23525, answer=367:25866)
- Layer 20: `忑`, `会成为`, `能被`, `ait`, ` engaging` (target ranks: base_value=80:4618, first_product=160:23459, bound_value=174:27912, second_product=348:25724, answer=367:26912)
- Layer 30: `八十`, ` eighty`, ` Eighty`, ` pakig`, `80` (target ranks: base_value=80:5, first_product=160:43, bound_value=174:16835, second_product=348:103208, answer=367:55324)
- Layer 35: ` eighty`, `八十`, `80`, `174`, ` Eighty` (target ranks: base_value=80:3, first_product=160:23, bound_value=174:4, second_product=348:36194, answer=367:66910)
- Layer 36: `翻`, `八十`, `往外`, `80`, `翻了` (target ranks: base_value=80:4, first_product=160:70, bound_value=174:14, second_product=348:31308, answer=367:86644)
- Layer 37: `}<?`, `ounder`, ` Nij`, `翻了`, `ASI` (target ranks: base_value=80:124, first_product=160:553, bound_value=174:159, second_product=348:76097, answer=367:115590)
- Layer 38: `}<?`, ` doubling`, `ounder`, `ASI`, ` Nij` (target ranks: base_value=80:323, first_product=160:1916, bound_value=174:790, second_product=348:85101, answer=367:118995)
- Layer 39: `}<?`, `ounder`, ` Nij`, `ermal`, `�乐` (target ranks: base_value=80:2354, first_product=160:13872, bound_value=174:2867, second_product=348:34107, answer=367:71137)
- Layer 40: ` fifty`, ` forty`, `二十八`, ` pals`, ` eighty` (target ranks: base_value=80:314, first_product=160:13398, bound_value=174:141, second_product=348:135, answer=367:635)
- Layer 41: ` .`, ` `, `贝尔`, `))))`, `�` (target ranks: base_value=80:1397, first_product=160:3931, bound_value=174:106, second_product=348:434, answer=367:495)

### Filler position 45 (absolute token 845, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127935, first_product=160:125830, bound_value=174:122681, second_product=348:127206, answer=367:121988)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12881, first_product=160:22266, bound_value=174:26498, second_product=348:22637, answer=367:24916)
- Layer 20: `ait`, `会成为`, `清楚楚`, ` Walker`, ` engaging` (target ranks: base_value=80:10729, first_product=160:29390, bound_value=174:39735, second_product=348:35655, answer=367:36865)
- Layer 30: ` x`, ` X`, ` Xer`, `udal`, `alal` (target ranks: base_value=80:1663, first_product=160:60655, bound_value=174:100439, second_product=348:122926, answer=367:61927)
- Layer 35: ` x`, ` X`, `adal`, `alal`, ` Xer` (target ranks: base_value=80:25, first_product=160:10524, bound_value=174:35650, second_product=348:97075, answer=367:46097)
- Layer 36: `adal`, ` x`, ` X`, `留存`, `antal` (target ranks: base_value=80:36, first_product=160:6066, bound_value=174:36073, second_product=348:81440, answer=367:41863)
- Layer 37: `}<?`, `enal`, `Quintal`, ` Halle`, `eal` (target ranks: base_value=80:149, first_product=160:7017, bound_value=174:50696, second_product=348:98956, answer=367:43881)
- Layer 38: `}<?`, `zal`, `enal`, `geal`, `Quintal` (target ranks: base_value=80:111, first_product=160:8524, bound_value=174:50491, second_product=348:103563, answer=367:59958)
- Layer 39: ` X`, ` x`, ` xanth`, `𝑋`, `}<?` (target ranks: base_value=80:1980, first_product=160:49056, bound_value=174:56669, second_product=348:87744, answer=367:51197)
- Layer 40: ` x`, ` X`, `留存`, `oug`, ` Tw` (target ranks: base_value=80:618, first_product=160:48186, bound_value=174:32674, second_product=348:65848, answer=367:16748)
- Layer 41: ` compounded`, ` `, `鹉`, ` compounding`, ` Tw` (target ranks: base_value=80:144, first_product=160:9584, bound_value=174:4379, second_product=348:16457, answer=367:1979)

### Filler position 46 (absolute token 846, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127947, first_product=160:125820, bound_value=174:122708, second_product=348:127226, answer=367:121956)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12381, first_product=160:21495, bound_value=174:26109, second_product=348:21898, answer=367:25059)
- Layer 20: `平行`, ` adtong`, ` spac`, `ait`, `俯` (target ranks: base_value=80:54029, first_product=160:52950, bound_value=174:91729, second_product=348:68346, answer=367:63350)
- Layer 30: ` spac`, `}using`, ` dekameters`, `坝`, `?datasetId` (target ranks: base_value=80:116458, first_product=160:108101, bound_value=174:122922, second_product=348:123438, answer=367:90293)
- Layer 35: `俯`, `坏`, `足足`, ` reduct`, `}using` (target ranks: base_value=80:94025, first_product=160:111402, bound_value=174:82060, second_product=348:109850, answer=367:64708)
- Layer 36: `俯`, `足足`, `ancock`, ` reduct`, ` surveying` (target ranks: base_value=80:51384, first_product=160:78095, bound_value=174:39374, second_product=348:67129, answer=367:42496)
- Layer 37: `}<?`, `俯`, `onana`, `isis`, `放下` (target ranks: base_value=80:76972, first_product=160:78303, bound_value=174:72626, second_product=348:64574, answer=367:45051)
- Layer 38: ` .`, `坏`, `错过`, `俯`, `水土` (target ranks: base_value=80:38707, first_product=160:62607, bound_value=174:64599, second_product=348:59950, answer=367:70655)
- Layer 39: `}<?`, `铎`, ` .`, `�`, `oxygen` (target ranks: base_value=80:57639, first_product=160:108564, bound_value=174:53941, second_product=348:49274, answer=367:39244)
- Layer 40: ` .`, ` .↵↵`, `oh`, `tal`, ` x` (target ranks: base_value=80:21682, first_product=160:87131, bound_value=174:38954, second_product=348:24455, answer=367:18757)
- Layer 41: ` .`, ` .↵↵`, ` `, ` .↵`, `<｜end▁of▁sentence｜>` (target ranks: base_value=80:12423, first_product=160:30031, bound_value=174:8496, second_product=348:5305, answer=367:5578)

### Filler position 47 (absolute token 847, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=80:127919, first_product=160:125821, bound_value=174:122689, second_product=348:127233, answer=367:121942)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=80:11864, first_product=160:21187, bound_value=174:26095, second_product=348:21677, answer=367:25125)
- Layer 20: `}<?`, ` partly`, `东海`, `)Skip`, ` honoured` (target ranks: base_value=80:88985, first_product=160:81731, bound_value=174:120364, second_product=348:106824, answer=367:115479)
- Layer 30: `}<?`, `codeline`, `dividers`, `}using`, `?datasetId` (target ranks: base_value=80:86069, first_product=160:108220, bound_value=174:118606, second_product=348:119767, answer=367:114374)
- Layer 35: `codeline`, `蜗`, `}<?`, `lett`, `}using` (target ranks: base_value=80:89468, first_product=160:124176, bound_value=174:118707, second_product=348:124340, answer=367:118141)
- Layer 36: `锯`, `切割`, ` fit`, `足足`, `直觉` (target ranks: base_value=80:44397, first_product=160:102674, bound_value=174:90607, second_product=348:104824, answer=367:111691)
- Layer 37: `}<?`, `Quintal`, `磨损`, `东京`, ` doubles` (target ranks: base_value=80:64955, first_product=160:95304, bound_value=174:93798, second_product=348:92581, answer=367:114190)
- Layer 38: ` .`, `遁`, ` prese`, `lett`, `坏` (target ranks: base_value=80:35258, first_product=160:57649, bound_value=174:85473, second_product=348:74369, answer=367:110078)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, `lett`, `坏`, ` .↵↵` (target ranks: base_value=80:80375, first_product=160:92957, bound_value=174:73977, second_product=348:62638, answer=367:93149)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `�`, `坏` (target ranks: base_value=80:52642, first_product=160:69782, bound_value=174:48112, second_product=348:24032, answer=367:69619)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `坏`, `<｜end▁of▁sentence｜>` (target ranks: base_value=80:13675, first_product=160:12160, bound_value=174:4185, second_product=348:1418, answer=367:15886)

### Filler position 48 (absolute token 848, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127846, first_product=160:125744, bound_value=174:122551, second_product=348:127209, answer=367:121756)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=80:11659, first_product=160:21373, bound_value=174:27089, second_product=348:22188, answer=367:25027)
- Layer 20: `东海`, ` instantaneous`, `aharoa`, `}<?`, `\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\` (target ranks: base_value=80:25350, first_product=160:24223, bound_value=174:61063, second_product=348:69003, answer=367:94239)
- Layer 30: `Quintal`, `codeline`, `?datasetId`, `}<?`, `Pulgada` (target ranks: base_value=80:67198, first_product=160:45991, bound_value=174:51993, second_product=348:86113, answer=367:66313)
- Layer 35: `codeline`, `?datasetId`, `Pulgada`, `叠`, ` slipp` (target ranks: base_value=80:66734, first_product=160:97667, bound_value=174:103427, second_product=348:23354, answer=367:310)
- Layer 36: `坏`, `383`, `坏的`, `395`, `第三百` (target ranks: base_value=80:85503, first_product=160:79305, bound_value=174:91390, second_product=348:11145, answer=367:145)
- Layer 37: `codeline`, `TreeLabel`, `Pulgada`, `Quintal`, `悬挂` (target ranks: base_value=80:98340, first_product=160:105919, bound_value=174:121648, second_product=348:83781, answer=367:20936)
- Layer 38: `codeline`, `悬挂`, `otan`, `ophyll`, ` Tribune` (target ranks: base_value=80:111405, first_product=160:116191, bound_value=174:118744, second_product=348:97891, answer=367:25065)
- Layer 39: `}using`, `叶子`, `�`, `树叶`, ` Dou` (target ranks: base_value=80:107736, first_product=160:123161, bound_value=174:126139, second_product=348:108532, answer=367:82237)
- Layer 40: ` .`, ` .↵↵`, `}using`, ` .↵`, ` Rees` (target ranks: base_value=80:93494, first_product=160:111150, bound_value=174:120910, second_product=348:106809, answer=367:80266)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `圆圆` (target ranks: base_value=80:33839, first_product=160:52568, bound_value=174:67349, second_product=348:42899, answer=367:28763)

### Filler position 49 (absolute token 849, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=80:127935, first_product=160:125966, bound_value=174:122831, second_product=348:127363, answer=367:122090)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11876, first_product=160:21718, bound_value=174:27960, second_product=348:22848, answer=367:24518)
- Layer 20: `aplenty`, ` licensierad`, `codeline`, ` instantaneous`, ` originalet` (target ranks: base_value=80:74917, first_product=160:84029, bound_value=174:76766, second_product=348:104772, answer=367:109396)
- Layer 30: ` Answer`, `答案是`, ` ответ`, `答案`, `codeline` (target ranks: base_value=80:112981, first_product=160:116700, bound_value=174:113446, second_product=348:126516, answer=367:125117)
- Layer 35: ` Answer`, `codeline`, `oNames`, `AED`, ` answer` (target ranks: base_value=80:73233, first_product=160:115620, bound_value=174:111275, second_product=348:122198, answer=367:126060)
- Layer 36: ` Answer`, `坏`, ` nasod`, `绽`, ` answer` (target ranks: base_value=80:19248, first_product=160:78501, bound_value=174:71791, second_product=348:99377, answer=367:113595)
- Layer 37: `oNames`, `codeline`, `insic`, `arit`, `金星` (target ranks: base_value=80:99964, first_product=160:115334, bound_value=174:103436, second_product=348:123715, answer=367:128430)
- Layer 38: `oNames`, `<|EOT|>`, ` retard`, `�`, `�` (target ranks: base_value=80:97924, first_product=160:117490, bound_value=174:109589, second_product=348:124099, answer=367:128540)
- Layer 39: `�`, `oxygen`, `deen`, ` unflagged`, `-ulo` (target ranks: base_value=80:89086, first_product=160:122498, bound_value=174:106593, second_product=348:102659, answer=367:116976)
- Layer 40: ` .↵↵`, ` .`, ` wink`, ` Answer`, `丝的` (target ranks: base_value=80:14057, first_product=160:95801, bound_value=174:59107, second_product=348:64413, answer=367:69318)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` wink`, ` mister` (target ranks: base_value=80:7108, first_product=160:67705, bound_value=174:17058, second_product=348:32859, answer=367:31388)

### Filler position 50 (absolute token 850, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=80:121107, first_product=160:111199, bound_value=174:110114, second_product=348:113649, answer=367:107019)
- Layer 10: `EDMF`, ` dével`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126323, first_product=160:103074, bound_value=174:117890, second_product=348:118200, answer=367:100736)
- Layer 20: `能被`, `答复`, ` Submission`, `EDER`, `差分` (target ranks: base_value=80:6532, first_product=160:27621, bound_value=174:52591, second_product=348:24668, answer=367:29783)
- Layer 30: `nze`, `aplenty`, ` dátummal`, `?datasetId`, ` sumala` (target ranks: base_value=80:114705, first_product=160:43970, bound_value=174:14014, second_product=348:24785, answer=367:45021)
- Layer 35: `349`, `348`, `359`, `347`, `368` (target ranks: base_value=80:127731, first_product=160:103674, bound_value=174:39315, second_product=348:2, answer=367:21)
- Layer 36: `368`, `369`, `373`, `370`, `383` (target ranks: base_value=80:129216, first_product=160:102671, bound_value=174:69863, second_product=348:35, answer=367:15)
- Layer 37: `368`, `369`, `373`, `383`, `374` (target ranks: base_value=80:129153, first_product=160:106230, bound_value=174:66425, second_product=348:48, answer=367:7)
- Layer 38: `373`, `368`, `367`, `369`, `365` (target ranks: base_value=80:129275, first_product=160:126925, bound_value=174:113274, second_product=348:261, answer=367:3)
- Layer 39: `369`, `367`, `373`, `383`, ` sumala` (target ranks: base_value=80:128701, first_product=160:128586, bound_value=174:125612, second_product=348:91908, answer=367:2)
- Layer 40: ` Answer`, `Answer`, ` answer`, `答`, `answer` (target ranks: base_value=80:128475, first_product=160:127177, bound_value=174:88524, second_product=348:74172, answer=367:11804)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=80:92037, first_product=160:86883, bound_value=174:47612, second_product=348:43639, answer=367:8928)

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
xal = 80
puc = twice the number for xal plus 14
dof = twice the number for puc plus 26
Question: What is twice the number for puc plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
