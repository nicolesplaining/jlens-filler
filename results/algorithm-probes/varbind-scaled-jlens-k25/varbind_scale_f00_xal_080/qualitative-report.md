# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `367` (correct).
- No-filler answer: `383` (incorrect).
- Filler tokens: 25 tokens at absolute indices 676–700.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=80` | 13 (L27, filler 4) | Never |
| J-Lens | `first_product=160` | 231 (L31, filler 9) | Never |
| J-Lens | `bound_value=174` | 1 (L31, filler 4) | L29, filler 25 (rank 2) |
| J-Lens | `second_product=348` | 1 (L33, filler 4) | L31, filler 4 (rank 4) |
| J-Lens | `answer=367` | 1 (L36, filler 24) | L31, filler 17 (rank 7) |
| Logit lens | `base_value=80` | 6 (L27, filler 9) | L27, filler 9 (rank 6) |
| Logit lens | `first_product=160` | 79 (L31, filler 9) | Never |
| Logit lens | `bound_value=174` | 1 (L31, filler 4) | L29, filler 16 (rank 2) |
| Logit lens | `second_product=348` | 1 (L35, filler 4) | L31, filler 16 (rank 6) |
| Logit lens | `answer=367` | 1 (L38, filler 17) | L31, filler 17 (rank 8) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 676, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=80:119450, first_product=160:111137, bound_value=174:109541, second_product=348:111740, answer=367:108842)
- Layer 10: `anta`, ` kinain`, `fine`, `hook`, `sem` (target ranks: base_value=80:93673, first_product=160:74124, bound_value=174:99863, second_product=348:83638, answer=367:55378)
- Layer 20: `足`, `扣`, ` .`, `重`, `tas` (target ranks: base_value=80:664, first_product=160:22045, bound_value=174:18738, second_product=348:31993, answer=367:4560)
- Layer 30: ` pakig`, ` talags`, ` procedural`, `expected`, `翻了` (target ranks: base_value=80:30215, first_product=160:9946, bound_value=174:1406, second_product=348:15165, answer=367:2342)
- Layer 35: `369`, `383`, `368`, `349`, `389` (target ranks: base_value=80:60265, first_product=160:111317, bound_value=174:24517, second_product=348:108, answer=367:35)
- Layer 36: `383`, `369`, `393`, `373`, `389` (target ranks: base_value=80:127418, first_product=160:122303, bound_value=174:44176, second_product=348:282, answer=367:27)
- Layer 37: `383`, `369`, `373`, `368`, `385` (target ranks: base_value=80:128881, first_product=160:125966, bound_value=174:47657, second_product=348:885, answer=367:16)
- Layer 38: `383`, `373`, `369`, `393`, `385` (target ranks: base_value=80:129261, first_product=160:129231, bound_value=174:121409, second_product=348:10227, answer=367:11)
- Layer 39: `383`, `慕`, `387`, ` Millenniums`, `�` (target ranks: base_value=80:128314, first_product=160:128562, bound_value=174:128161, second_product=348:124003, answer=367:999)
- Layer 40: `实在`, ` talags`, `實在`, ` ald`, `383` (target ranks: base_value=80:128371, first_product=160:128583, bound_value=174:125339, second_product=348:125057, answer=367:1812)
- Layer 41: ` .`, `我已经`, `就到了`, ` .↵↵`, `秆` (target ranks: base_value=80:104453, first_product=160:114701, bound_value=174:93403, second_product=348:87999, answer=367:6909)

### Filler position 2 (absolute token 677, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: base_value=80:122047, first_product=160:117324, bound_value=174:113442, second_product=348:118311, answer=367:114899)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: base_value=80:23406, first_product=160:31942, bound_value=174:43319, second_product=348:44036, answer=367:37692)
- Layer 20: ` .`, ` tall`, `外向`, ` esper`, `外层` (target ranks: base_value=80:37373, first_product=160:114923, bound_value=174:115690, second_product=348:126875, answer=367:108303)
- Layer 30: `}<?`, ` pakig`, `翻`, ` الشعاعيه`, `翻了` (target ranks: base_value=80:95583, first_product=160:91693, bound_value=174:78772, second_product=348:116099, answer=367:57573)
- Layer 35: ` labor`, `漂`, ` Labor`, `期待的`, ` tib` (target ranks: base_value=80:85896, first_product=160:111311, bound_value=174:66564, second_product=348:39534, answer=367:6766)
- Layer 36: `}<?`, `LikeLike`, `漂`, `轨`, `翻` (target ranks: base_value=80:124011, first_product=160:111336, bound_value=174:96270, second_product=348:58784, answer=367:3343)
- Layer 37: `}<?`, ` Erkännande`, `?datasetId`, `LikeLike`, `ihar` (target ranks: base_value=80:126616, first_product=160:101602, bound_value=174:93649, second_product=348:45237, answer=367:202)
- Layer 38: `}<?`, `?datasetId`, ` Erkännande`, `图画`, `croft` (target ranks: base_value=80:128538, first_product=160:127367, bound_value=174:125245, second_product=348:65802, answer=367:39)
- Layer 39: `}<?`, `Kadaghanon`, ` Millenniums`, `tanle`, `本题分析` (target ranks: base_value=80:127930, first_product=160:126526, bound_value=174:127899, second_product=348:123917, answer=367:594)
- Layer 40: `}<?`, ` ald`, ` LD`, ` alde`, `语言文字` (target ranks: base_value=80:128322, first_product=160:127570, bound_value=174:127415, second_product=348:125149, answer=367:1138)
- Layer 41: ` .`, ` .↵↵`, `Kadaghanon`, `LikeLike`, ` .↵` (target ranks: base_value=80:124956, first_product=160:122115, bound_value=174:122916, second_product=348:112343, answer=367:3863)

### Filler position 3 (absolute token 678, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125324, first_product=160:120857, bound_value=174:115866, second_product=348:120764, answer=367:117915)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=80:17184, first_product=160:28835, bound_value=174:32688, second_product=348:30605, answer=367:30564)
- Layer 20: `ait`, `能被`, `忑`, `锁定`, `足` (target ranks: base_value=80:5080, first_product=160:34870, bound_value=174:27929, second_product=348:37008, answer=367:30930)
- Layer 30: `计算的`, `calcul`, `进行计算`, ` unpack`, `计算` (target ranks: base_value=80:43264, first_product=160:99137, bound_value=174:99066, second_product=348:127152, answer=367:92283)
- Layer 35: ` resolve`, ` resolving`, `solve`, ` resolves`, `resolve` (target ranks: base_value=80:21575, first_product=160:92587, bound_value=174:73161, second_product=348:119022, answer=367:61866)
- Layer 36: `calcul`, `计算的`, ` sequentially`, `计算`, `化解` (target ranks: base_value=80:26837, first_product=160:71376, bound_value=174:71556, second_product=348:103695, answer=367:40630)
- Layer 37: `}<?`, `解的`, `calcul`, `逐步`, ` calcul` (target ranks: base_value=80:61525, first_product=160:95553, bound_value=174:102815, second_product=348:124615, answer=367:85554)
- Layer 38: `}<?`, `解的`, `calcul`, ` evalu`, `notations` (target ranks: base_value=80:48839, first_product=160:104648, bound_value=174:107923, second_product=348:125977, answer=367:70072)
- Layer 39: `script`, `}<?`, `文字的`, `语言文字`, `一个一个` (target ranks: base_value=80:124713, first_product=160:128662, bound_value=174:127776, second_product=348:128358, answer=367:109147)
- Layer 40: `一个一个`, `试一试`, `mmmm`, `语言文字`, `留存` (target ranks: base_value=80:123687, first_product=160:128507, bound_value=174:125145, second_product=348:127953, answer=367:103028)
- Layer 41: ` .`, `试一试`, `一个一个`, `一个个`, ` ;` (target ranks: base_value=80:114078, first_product=160:121843, bound_value=174:105616, second_product=348:114206, answer=367:61671)

### Filler position 4 (absolute token 679, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125894, first_product=160:122406, bound_value=174:117035, second_product=348:122276, answer=367:119681)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: base_value=80:13417, first_product=160:22885, bound_value=174:27508, second_product=348:23790, answer=367:24451)
- Layer 20: `能被`, `ait`, ` quadr`, ` LS`, `幽` (target ranks: base_value=80:7801, first_product=160:39598, bound_value=174:37893, second_product=348:35300, answer=367:31547)
- Layer 30: `erer`, `}<?`, `erten`, `参赛`, ` eighty` (target ranks: base_value=80:1411, first_product=160:8416, bound_value=174:54, second_product=348:19613, answer=367:52065)
- Layer 35: `348`, `349`, `174`, `347`, `344` (target ranks: base_value=80:34633, first_product=160:109503, bound_value=174:3, second_product=348:1, answer=367:20473)
- Layer 36: `348`, `349`, `174`, `Giya`, ` radi` (target ranks: base_value=80:109183, first_product=160:119064, bound_value=174:3, second_product=348:1, answer=367:28076)
- Layer 37: `348`, `349`, `Giya`, ` radi`, `174` (target ranks: base_value=80:110213, first_product=160:121316, bound_value=174:5, second_product=348:1, answer=367:31321)
- Layer 38: `348`, `349`, `打包`, `红衣`, `ADI` (target ranks: base_value=80:123656, first_product=160:126984, bound_value=174:22, second_product=348:1, answer=367:30770)
- Layer 39: `348`, `�`, `349`, `ophe`, `ADI` (target ranks: base_value=80:126039, first_product=160:128696, bound_value=174:362, second_product=348:1, answer=367:62199)
- Layer 40: `348`, `打包`, `发声`, `<｜place▁holder▁no▁36｜>`, `解说` (target ranks: base_value=80:127522, first_product=160:128723, bound_value=174:7699, second_product=348:1, answer=367:9730)
- Layer 41: `试一试`, ` .`, `348`, `温馨提示`, `anteed` (target ranks: base_value=80:127776, first_product=160:128593, bound_value=174:15530, second_product=348:3, answer=367:15306)

### Filler position 5 (absolute token 680, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125669, first_product=160:122298, bound_value=174:116958, second_product=348:122464, answer=367:119706)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=80:14582, first_product=160:24800, bound_value=174:30326, second_product=348:25484, answer=367:27306)
- Layer 20: `cape`, `幽`, ` smile`, `锁定`, `鞍` (target ranks: base_value=80:12613, first_product=160:38186, bound_value=174:32072, second_product=348:33037, answer=367:27481)
- Layer 30: ` tap`, `Tap`, `tap`, ` Tap`, `炭` (target ranks: base_value=80:80264, first_product=160:54203, bound_value=174:50697, second_product=348:98566, answer=367:61919)
- Layer 35: ` rip`, `冰冰`, ` tap`, `推算`, ` Niagara` (target ranks: base_value=80:108553, first_product=160:101197, bound_value=174:71481, second_product=348:112547, answer=367:98198)
- Layer 36: ` rip`, `推算`, `冰冰`, `反复`, ` tap` (target ranks: base_value=80:100265, first_product=160:74374, bound_value=174:69678, second_product=348:100664, answer=367:101062)
- Layer 37: `hemer`, `anium`, `romic`, `}<?`, ` floating` (target ranks: base_value=80:114230, first_product=160:85558, bound_value=174:89753, second_product=348:115209, answer=367:105229)
- Layer 38: `}<?`, `hemer`, `�`, ` hydrodynamic`, `romic` (target ranks: base_value=80:119310, first_product=160:94373, bound_value=174:103056, second_product=348:114205, answer=367:111855)
- Layer 39: `hemer`, `-ulo`, `}<?`, `romic`, `本题分析` (target ranks: base_value=80:125253, first_product=160:122608, bound_value=174:114167, second_product=348:120761, answer=367:114152)
- Layer 40: ` nasod`, `乐乐`, `语言文字`, `试一试`, `inking` (target ranks: base_value=80:118061, first_product=160:115485, bound_value=174:81345, second_product=348:112150, answer=367:49930)
- Layer 41: ` .`, `试一试`, `我没有`, `答案`, `鹉` (target ranks: base_value=80:105038, first_product=160:85035, bound_value=174:19766, second_product=348:54053, answer=367:5132)

### Filler position 6 (absolute token 681, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125277, first_product=160:121921, bound_value=174:116582, second_product=348:122388, answer=367:119264)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:14170, first_product=160:23991, bound_value=174:27784, second_product=348:24071, answer=367:26016)
- Layer 20: ` поха`, `-ulo`, `本题分析`, `ใ`, ` unflagged` (target ranks: base_value=80:122296, first_product=160:98435, bound_value=174:102716, second_product=348:121907, answer=367:90911)
- Layer 30: `高明`, `turn`, `kä`, ` slowed`, `cale` (target ranks: base_value=80:21709, first_product=160:25158, bound_value=174:8323, second_product=348:89736, answer=367:20743)
- Layer 35: `高明`, ` Tw`, `acks`, `.tw`, ` TW` (target ranks: base_value=80:26176, first_product=160:42401, bound_value=174:1219, second_product=348:52654, answer=367:69920)
- Layer 36: ` Tw`, `.tw`, `反复`, ` tw`, `Tw` (target ranks: base_value=80:26402, first_product=160:37355, bound_value=174:3321, second_product=348:43195, answer=367:90890)
- Layer 37: ` Tw`, `高明`, ` Pt`, ` doubly`, `蒲公英` (target ranks: base_value=80:47217, first_product=160:60913, bound_value=174:14836, second_product=348:87387, answer=367:99244)
- Layer 38: ` Tw`, ` doubly`, `漂`, `蒲公英`, `不负` (target ranks: base_value=80:60459, first_product=160:73874, bound_value=174:23267, second_product=348:95949, answer=367:100337)
- Layer 39: ` talags`, `�`, `把事情`, `deen`, `蒲公英` (target ranks: base_value=80:120979, first_product=160:126998, bound_value=174:114810, second_product=348:125341, answer=367:117143)
- Layer 40: `dots`, ` dots`, ` dotted`, ` dot`, ` talags` (target ranks: base_value=80:115807, first_product=160:126969, bound_value=174:112462, second_product=348:122461, answer=367:107347)
- Layer 41: ` .`, ` dots`, ` dotted`, `dots`, `试一试` (target ranks: base_value=80:116218, first_product=160:119693, bound_value=174:92385, second_product=348:105963, answer=367:76428)

### Filler position 7 (absolute token 682, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125192, first_product=160:121700, bound_value=174:116399, second_product=348:122358, answer=367:118935)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:13733, first_product=160:23416, bound_value=174:27712, second_product=348:24137, answer=367:25542)
- Layer 20: `锁定`, `ait`, ` Walker`, `挪`, `Walker` (target ranks: base_value=80:7105, first_product=160:29119, bound_value=174:31968, second_product=348:29243, answer=367:28763)
- Layer 30: ` Tw`, `Tw`, ` twice`, `.tw`, `tw` (target ranks: base_value=80:4503, first_product=160:37876, bound_value=174:66019, second_product=348:116090, answer=367:72321)
- Layer 35: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=80:4424, first_product=160:33706, bound_value=174:51416, second_product=348:90779, answer=367:73680)
- Layer 36: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=80:8401, first_product=160:34340, bound_value=174:59051, second_product=348:77841, answer=367:85926)
- Layer 37: ` Tw`, `Tw`, ` twice`, `.tw`, ` doubly` (target ranks: base_value=80:10573, first_product=160:25994, bound_value=174:62742, second_product=348:90234, answer=367:95057)
- Layer 38: `}<?`, ` duc`, ` Duc`, ` doubling`, ` cál` (target ranks: base_value=80:17026, first_product=160:46365, bound_value=174:80467, second_product=348:99783, answer=367:107493)
- Layer 39: `}<?`, ` duc`, ` Noruwega`, `本题分析`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=80:79653, first_product=160:107544, bound_value=174:97507, second_product=348:100390, answer=367:95245)
- Layer 40: ` nasod`, `duc`, ` duc`, ` p`, `scr` (target ranks: base_value=80:60347, first_product=160:99015, bound_value=174:69265, second_product=348:76328, answer=367:45748)
- Layer 41: `试一试`, ` .`, `试试`, `鹉`, `步骤如下` (target ranks: base_value=80:55688, first_product=160:63947, bound_value=174:43158, second_product=348:43989, answer=367:20932)

### Filler position 8 (absolute token 683, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125131, first_product=160:121409, bound_value=174:116504, second_product=348:122295, answer=367:118551)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13275, first_product=160:23876, bound_value=174:28777, second_product=348:25127, answer=367:26344)
- Layer 20: `ait`, ` Walker`, `锁定`, ` cheer`, `Walker` (target ranks: base_value=80:8307, first_product=160:30731, bound_value=174:31435, second_product=348:26283, answer=367:26752)
- Layer 30: ` Tw`, `Tw`, ` twice`, `.tw`, `Tap` (target ranks: base_value=80:7437, first_product=160:47558, bound_value=174:53495, second_product=348:57007, answer=367:39905)
- Layer 35: ` Tw`, `Tw`, `tw`, `Tap`, `.tw` (target ranks: base_value=80:8282, first_product=160:38545, bound_value=174:28165, second_product=348:35698, answer=367:35555)
- Layer 36: ` Tw`, ` value`, `留存`, `Tw`, ` number` (target ranks: base_value=80:18571, first_product=160:47050, bound_value=174:31583, second_product=348:30978, answer=367:52304)
- Layer 37: ` value`, ` number`, `}<?`, ` Zahl`, `价值` (target ranks: base_value=80:39701, first_product=160:48442, bound_value=174:36761, second_product=348:39756, answer=367:69506)
- Layer 38: `}<?`, `珍珠`, `覆`, `pac`, ` Zahl` (target ranks: base_value=80:48393, first_product=160:72884, bound_value=174:60093, second_product=348:57104, answer=367:84392)
- Layer 39: `}<?`, `umber`, ` Zahl`, `.number`, ` NUMBER` (target ranks: base_value=80:86037, first_product=160:111946, bound_value=174:81603, second_product=348:87847, answer=367:88231)
- Layer 40: ` p`, `šk`, `p`, `zij`, `odecimal` (target ranks: base_value=80:60838, first_product=160:107374, bound_value=174:60178, second_product=348:74985, answer=367:49589)
- Layer 41: `鹉`, ` .`, `odecimal`, ` number`, `留存` (target ranks: base_value=80:55047, first_product=160:89930, bound_value=174:51016, second_product=348:57001, answer=367:27592)

### Filler position 9 (absolute token 684, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125319, first_product=160:121642, bound_value=174:116705, second_product=348:122553, answer=367:118653)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13268, first_product=160:23820, bound_value=174:29035, second_product=348:24550, answer=367:26517)
- Layer 20: `锁定`, ` Walker`, `ait`, `能被`, `挪` (target ranks: base_value=80:6890, first_product=160:23516, bound_value=174:27715, second_product=348:20519, answer=367:17501)
- Layer 30: `Tap`, ` tap`, `tap`, `Tail`, ` Tap` (target ranks: base_value=80:63, first_product=160:1103, bound_value=174:270, second_product=348:26039, answer=367:10292)
- Layer 35: `174`, `774`, `74`, `974`, `374` (target ranks: base_value=80:2718, first_product=160:37863, bound_value=174:1, second_product=348:2457, answer=367:70971)
- Layer 36: `174`, `出去了`, `ijani`, `anium`, `�` (target ranks: base_value=80:27034, first_product=160:23668, bound_value=174:1, second_product=348:6768, answer=367:103953)
- Layer 37: `174`, `}<?`, `odecimal`, `副院长`, `�` (target ranks: base_value=80:68343, first_product=160:35720, bound_value=174:1, second_product=348:24519, answer=367:119805)
- Layer 38: `174`, `}<?`, `副院长`, `院长`, `�` (target ranks: base_value=80:87938, first_product=160:51071, bound_value=174:1, second_product=348:33498, answer=367:118470)
- Layer 39: `174`, `}<?`, `polar`, `�`, `opters` (target ranks: base_value=80:98818, first_product=160:88117, bound_value=174:1, second_product=348:32913, answer=367:100865)
- Layer 40: `留存`, `}<?`, `漏`, `odecimal`, `pline` (target ranks: base_value=80:78506, first_product=160:92303, bound_value=174:28, second_product=348:26308, answer=367:8812)
- Layer 41: `婷婷`, `试一试`, `odecimal`, `温馨提示`, ` .` (target ranks: base_value=80:62959, first_product=160:69271, bound_value=174:57, second_product=348:22599, answer=367:12078)

### Filler position 10 (absolute token 685, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125232, first_product=160:121619, bound_value=174:116705, second_product=348:122604, answer=367:118746)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11787, first_product=160:22430, bound_value=174:27474, second_product=348:23074, answer=367:24849)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `拆` (target ranks: base_value=80:17781, first_product=160:39213, bound_value=174:40552, second_product=348:40252, answer=367:40707)
- Layer 30: `�`, `分解`, `acin`, `拆`, `alal` (target ranks: base_value=80:3287, first_product=160:29214, bound_value=174:69360, second_product=348:102876, answer=367:67912)
- Layer 35: `分解`, `羊`, `adal`, `Tap`, `alal` (target ranks: base_value=80:664, first_product=160:20654, bound_value=174:37811, second_product=348:79475, answer=367:57925)
- Layer 36: `分解`, `adal`, `翻`, `羊`, `俯` (target ranks: base_value=80:1894, first_product=160:17094, bound_value=174:38517, second_product=348:75209, answer=367:59271)
- Layer 37: `}<?`, `翻了`, `翻`, `acl`, `zat` (target ranks: base_value=80:5029, first_product=160:28551, bound_value=174:71645, second_product=348:107655, answer=367:82573)
- Layer 38: `}<?`, `zat`, `zal`, `geal`, `覆` (target ranks: base_value=80:7248, first_product=160:38337, bound_value=174:79044, second_product=348:110674, answer=367:94376)
- Layer 39: `}<?`, `zat`, ` X`, ` x`, ` Xavier` (target ranks: base_value=80:49995, first_product=160:84007, bound_value=174:97877, second_product=348:117881, answer=367:105813)
- Layer 40: ` x`, `zat`, `俯`, `acl`, `xim` (target ranks: base_value=80:34214, first_product=160:60251, bound_value=174:62653, second_product=348:98013, answer=367:57446)
- Layer 41: `鹉`, ` .`, `俯`, `覆`, `实在` (target ranks: base_value=80:40079, first_product=160:33575, bound_value=174:28297, second_product=348:43535, answer=367:30436)

### Filler position 11 (absolute token 686, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125236, first_product=160:121885, bound_value=174:116852, second_product=348:122911, answer=367:118896)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13549, first_product=160:23821, bound_value=174:29094, second_product=348:24652, answer=367:25972)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=80:14588, first_product=160:37019, bound_value=174:37668, second_product=348:41647, answer=367:37911)
- Layer 30: ` Zem`, `alal`, `�`, ` parallel`, `平行` (target ranks: base_value=80:3413, first_product=160:65211, bound_value=174:92922, second_product=348:120262, answer=367:74837)
- Layer 35: `羊`, ` Zem`, `alal`, `分解`, `�` (target ranks: base_value=80:1524, first_product=160:60380, bound_value=174:76620, second_product=348:104718, answer=367:75588)
- Layer 36: ` Zem`, `calcul`, ` Zad`, `adal`, `acl` (target ranks: base_value=80:3956, first_product=160:53307, bound_value=174:75552, second_product=348:100457, answer=367:85557)
- Layer 37: `}<?`, ` Zem`, ` Zad`, ` zem`, `acl` (target ranks: base_value=80:19898, first_product=160:87525, bound_value=174:111894, second_product=348:121107, answer=367:104915)
- Layer 38: `}<?`, `zat`, ` Zem`, `zal`, ` zem` (target ranks: base_value=80:25610, first_product=160:102063, bound_value=174:118067, second_product=348:122963, answer=367:108607)
- Layer 39: `}<?`, `zat`, ` Zem`, `�`, `zal` (target ranks: base_value=80:72647, first_product=160:112066, bound_value=174:113082, second_product=348:121686, answer=367:96409)
- Layer 40: `zij`, ` Zad`, `zat`, `acl`, ` Zem` (target ranks: base_value=80:51756, first_product=160:93491, bound_value=174:91953, second_product=348:112154, answer=367:61652)
- Layer 41: `试一试`, `鹉`, ` .`, `的计算`, `zij` (target ranks: base_value=80:29917, first_product=160:37569, bound_value=174:41123, second_product=348:65387, answer=367:30543)

### Filler position 12 (absolute token 687, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125138, first_product=160:121864, bound_value=174:117026, second_product=348:123002, answer=367:118845)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12862, first_product=160:22367, bound_value=174:27971, second_product=348:23592, answer=367:25141)
- Layer 20: `ait`, ` smile`, ` wig`, `锁定`, ` ES` (target ranks: base_value=80:11151, first_product=160:37356, bound_value=174:33688, second_product=348:37459, answer=367:34827)
- Layer 30: ` tap`, `Tap`, ` rip`, ` Cogn`, `acin` (target ranks: base_value=80:42017, first_product=160:87799, bound_value=174:99959, second_product=348:88502, answer=367:31548)
- Layer 35: ` tap`, `Tap`, ` rip`, ` Tap`, `tap` (target ranks: base_value=80:47571, first_product=160:93189, bound_value=174:82537, second_product=348:75471, answer=367:49957)
- Layer 36: ` rip`, ` tap`, `acin`, ` dynam`, ` dy` (target ranks: base_value=80:42395, first_product=160:75294, bound_value=174:68390, second_product=348:73777, answer=367:53068)
- Layer 37: ` rip`, `}<?`, `疑惑`, `ako`, `amol` (target ranks: base_value=80:84675, first_product=160:101443, bound_value=174:104143, second_product=348:106761, answer=367:79187)
- Layer 38: `}<?`, `疑惑`, `zat`, ` Noruwega`, ` Pax` (target ranks: base_value=80:93955, first_product=160:115355, bound_value=174:115076, second_product=348:110834, answer=367:97998)
- Layer 39: `}<?`, ` Nij`, ` Noruwega`, `�`, `pac` (target ranks: base_value=80:107885, first_product=160:115856, bound_value=174:116898, second_product=348:106169, answer=367:78364)
- Layer 40: `amn`, ` fum`, ` rip`, `�`, `pon` (target ranks: base_value=80:98431, first_product=160:111805, bound_value=174:101048, second_product=348:93137, answer=367:46099)
- Layer 41: `Question`, ` Question`, ` fum`, `试一试`, `amn` (target ranks: base_value=80:67516, first_product=160:66014, bound_value=174:63277, second_product=348:55891, answer=367:12717)

### Filler position 13 (absolute token 688, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125329, first_product=160:122107, bound_value=174:117270, second_product=348:123297, answer=367:118908)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=80:13663, first_product=160:23703, bound_value=174:28864, second_product=348:24379, answer=367:26740)
- Layer 20: `锁定`, ` engaging`, `忑`, ` Walker`, `ait` (target ranks: base_value=80:20947, first_product=160:50633, bound_value=174:46935, second_product=348:40222, answer=367:40488)
- Layer 30: `acin`, `锁定`, `平行`, `鞍`, ` tap` (target ranks: base_value=80:20377, first_product=160:77915, bound_value=174:79241, second_product=348:77742, answer=367:62884)
- Layer 35: `锁定`, ` tap`, ` future`, `Tap`, ` Tap` (target ranks: base_value=80:9793, first_product=160:37463, bound_value=174:31388, second_product=348:51128, answer=367:41802)
- Layer 36: ` tap`, `锁定`, ` aug`, `留存`, `羊` (target ranks: base_value=80:11829, first_product=160:28437, bound_value=174:29034, second_product=348:36152, answer=367:43021)
- Layer 37: `翻`, `留存`, `装`, ` August`, ` po` (target ranks: base_value=80:28370, first_product=160:30055, bound_value=174:55583, second_product=348:55735, answer=367:41321)
- Layer 38: `留存`, `翻`, `pac`, `寒风`, ` embargo` (target ranks: base_value=80:47064, first_product=160:41691, bound_value=174:64482, second_product=348:71850, answer=367:58527)
- Layer 39: `}<?`, `铎`, ` talags`, `东海`, `覆` (target ranks: base_value=80:100838, first_product=160:107048, bound_value=174:108376, second_product=348:110331, answer=367:93163)
- Layer 40: `下沉`, `留存`, `捆绑`, ` talags`, ` .` (target ranks: base_value=80:95807, first_product=160:98032, bound_value=174:87902, second_product=348:94647, answer=367:71838)
- Layer 41: ` .`, ` .↵↵`, `鹉`, ` .↵`, `我没有` (target ranks: base_value=80:78865, first_product=160:59992, bound_value=174:54643, second_product=348:56239, answer=367:28865)

### Filler position 14 (absolute token 689, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125542, first_product=160:122298, bound_value=174:117670, second_product=348:123577, answer=367:119131)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11832, first_product=160:21995, bound_value=174:26026, second_product=348:22480, answer=367:24660)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `会成为` (target ranks: base_value=80:12615, first_product=160:29326, bound_value=174:28896, second_product=348:32527, answer=367:38918)
- Layer 30: ` Zem`, ` zem`, `zem`, `зем`, ` Zad` (target ranks: base_value=80:30195, first_product=160:86586, bound_value=174:69427, second_product=348:107902, answer=367:74731)
- Layer 35: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=80:17540, first_product=160:62629, bound_value=174:45801, second_product=348:87430, answer=367:70553)
- Layer 36: ` Zem`, ` zem`, `zem`, ` Zad`, ` zad` (target ranks: base_value=80:25597, first_product=160:58441, bound_value=174:48605, second_product=348:64749, answer=367:73857)
- Layer 37: ` Zem`, ` zem`, `zem`, ` Zad`, `зем` (target ranks: base_value=80:67673, first_product=160:86205, bound_value=174:91182, second_product=348:102171, answer=367:94034)
- Layer 38: ` Zem`, `zem`, ` zem`, `zat`, `}<?` (target ranks: base_value=80:77850, first_product=160:98163, bound_value=174:106971, second_product=348:109454, answer=367:100456)
- Layer 39: ` Zem`, `zem`, ` zem`, `zam`, `zat` (target ranks: base_value=80:81555, first_product=160:110981, bound_value=174:107563, second_product=348:112364, answer=367:88778)
- Layer 40: ` Zem`, ` zem`, `zem`, `zij`, ` p` (target ranks: base_value=80:51695, first_product=160:93761, bound_value=174:81702, second_product=348:110107, answer=367:62260)
- Layer 41: ` zem`, ` Zem`, `abd`, `xyz`, ` duc` (target ranks: base_value=80:19954, first_product=160:31306, bound_value=174:32118, second_product=348:58384, answer=367:24216)

### Filler position 15 (absolute token 690, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125668, first_product=160:122405, bound_value=174:117855, second_product=348:123677, answer=367:119139)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12047, first_product=160:21904, bound_value=174:26220, second_product=348:22243, answer=367:23767)
- Layer 20: `ait`, `锁定`, ` Walker`, `而此时`, `Walker` (target ranks: base_value=80:8695, first_product=160:25260, bound_value=174:24084, second_product=348:24687, answer=367:30110)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=80:11718, first_product=160:53341, bound_value=174:46832, second_product=348:88223, answer=367:42224)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=80:12566, first_product=160:46677, bound_value=174:35105, second_product=348:66112, answer=367:55862)
- Layer 36: ` Tw`, `Tw`, `.tw`, `adal`, ` Wil` (target ranks: base_value=80:11109, first_product=160:44878, bound_value=174:37456, second_product=348:52490, answer=367:59993)
- Layer 37: `}<?`, ` Tw`, `acos`, ` number`, ` twist` (target ranks: base_value=80:38044, first_product=160:78620, bound_value=174:77178, second_product=348:96937, answer=367:91044)
- Layer 38: `}<?`, `zat`, ` twist`, ` doubling`, `ِّف` (target ranks: base_value=80:39558, first_product=160:97162, bound_value=174:99437, second_product=348:105770, answer=367:100173)
- Layer 39: `}<?`, `ِّف`, ` Zahl`, `zat`, `andem` (target ranks: base_value=80:52131, first_product=160:107190, bound_value=174:100543, second_product=348:113209, answer=367:106442)
- Layer 40: `zij`, ` Zem`, `zat`, ` zem`, `scr` (target ranks: base_value=80:22101, first_product=160:89772, bound_value=174:79067, second_product=348:108256, answer=367:93087)
- Layer 41: `zij`, ` .`, ` zem`, `<｜end▁of▁sentence｜>`, `abd` (target ranks: base_value=80:24492, first_product=160:54441, bound_value=174:44413, second_product=348:72296, answer=367:65282)

### Filler position 16 (absolute token 691, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125705, first_product=160:122386, bound_value=174:117864, second_product=348:123788, answer=367:119073)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13421, first_product=160:22958, bound_value=174:27151, second_product=348:22633, answer=367:24544)
- Layer 20: `ait`, `能被`, `锁定`, ` Walker`, `而此时` (target ranks: base_value=80:7353, first_product=160:29213, bound_value=174:27376, second_product=348:21625, answer=367:26523)
- Layer 30: `sets`, `atan`, `tail`, `打完`, `反复` (target ranks: base_value=80:3135, first_product=160:6316, bound_value=174:39, second_product=348:2204, answer=367:11984)
- Layer 35: `174`, `348`, `374`, `349`, `347` (target ranks: base_value=80:41869, first_product=160:112910, bound_value=174:1, second_product=348:2, answer=367:21820)
- Layer 36: `174`, `348`, `349`, `anium`, `347` (target ranks: base_value=80:101652, first_product=160:108413, bound_value=174:1, second_product=348:2, answer=367:33104)
- Layer 37: `348`, `174`, `349`, `perian`, `打包` (target ranks: base_value=80:116828, first_product=160:118041, bound_value=174:2, second_product=348:1, answer=367:23748)
- Layer 38: `348`, `174`, `349`, `打包`, `347` (target ranks: base_value=80:113777, first_product=160:121156, bound_value=174:2, second_product=348:1, answer=367:12851)
- Layer 39: `348`, `<｜begin▁of▁sentence｜>`, `349`, `慧`, `347` (target ranks: base_value=80:112664, first_product=160:123548, bound_value=174:8, second_product=348:1, answer=367:4737)
- Layer 40: `348`, `iator`, `349`, `留守`, ` kinahabogang` (target ranks: base_value=80:112863, first_product=160:126228, bound_value=174:39, second_product=348:1, answer=367:857)
- Layer 41: `348`, ` waiting`, ` twisted`, ` twisting`, `plier` (target ranks: base_value=80:95675, first_product=160:118847, bound_value=174:33, second_product=348:1, answer=367:4997)

### Filler position 17 (absolute token 692, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125828, first_product=160:122571, bound_value=174:118159, second_product=348:123970, answer=367:119269)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:16670, first_product=160:26646, bound_value=174:32271, second_product=348:26470, answer=367:28710)
- Layer 20: `能被`, `锁定`, `距`, `ession`, ` smile` (target ranks: base_value=80:15049, first_product=160:33569, bound_value=174:33958, second_product=348:29811, answer=367:22002)
- Layer 30: `翻`, `翻了`, ` усили`, ` kahaboga`, `orget` (target ranks: base_value=80:34964, first_product=160:3505, bound_value=174:131, second_product=348:551, answer=367:47)
- Layer 35: `349`, `347`, `359`, `348`, `383` (target ranks: base_value=80:58750, first_product=160:46160, bound_value=174:2869, second_product=348:4, answer=367:7)
- Layer 36: `368`, `369`, `367`, `366`, `383` (target ranks: base_value=80:124317, first_product=160:13862, bound_value=174:20374, second_product=348:370, answer=367:3)
- Layer 37: `369`, `368`, `367`, `366`, `365` (target ranks: base_value=80:126856, first_product=160:17636, bound_value=174:30625, second_product=348:1199, answer=367:3)
- Layer 38: `367`, `368`, `369`, `366`, `365` (target ranks: base_value=80:129100, first_product=160:120089, bound_value=174:119588, second_product=348:1142, answer=367:1)
- Layer 39: `369`, `367`, `368`, ` Kiel`, ` SGD` (target ranks: base_value=80:126543, first_product=160:125659, bound_value=174:128459, second_product=348:121144, answer=367:2)
- Layer 40: `aldehyde`, `语言文字`, ` bund`, `cust`, `crumb` (target ranks: base_value=80:127972, first_product=160:127167, bound_value=174:127884, second_product=348:127075, answer=367:55)
- Layer 41: ` nuest`, `需要注意的是`, `zion`, ` .`, `印书馆` (target ranks: base_value=80:109652, first_product=160:114766, bound_value=174:118670, second_product=348:118116, answer=367:117)

### Filler position 18 (absolute token 693, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125856, first_product=160:122803, bound_value=174:118328, second_product=348:124281, answer=367:119428)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:14458, first_product=160:25531, bound_value=174:30231, second_product=348:25402, answer=367:27423)
- Layer 20: `忑`, ` Walker`, `ait`, ` engaging`, `锁定` (target ranks: base_value=80:12526, first_product=160:32931, bound_value=174:31433, second_product=348:34404, answer=367:37916)
- Layer 30: `Tw`, ` Tw`, ` twice`, `atan`, `28` (target ranks: base_value=80:11688, first_product=160:33653, bound_value=174:8574, second_product=348:43589, answer=367:52725)
- Layer 35: `28`, `二十八`, ` Tw`, `Tw`, ` repeated` (target ranks: base_value=80:2824, first_product=160:22233, bound_value=174:2702, second_product=348:33564, answer=367:48218)
- Layer 36: `28`, `二十八`, `adal`, `atan`, ` repeated` (target ranks: base_value=80:13002, first_product=160:34720, bound_value=174:12477, second_product=348:51975, answer=367:81261)
- Layer 37: `28`, `二十八`, `}<?`, ` doubling`, ` doubled` (target ranks: base_value=80:32039, first_product=160:52305, bound_value=174:27673, second_product=348:90962, answer=367:106222)
- Layer 38: `}<?`, `28`, `?datasetId`, ` doubling`, `二十八` (target ranks: base_value=80:73428, first_product=160:89220, bound_value=174:64371, second_product=348:102859, answer=367:117387)
- Layer 39: `}<?`, `Quintal`, `东海`, ` doubling`, `?datasetId` (target ranks: base_value=80:97354, first_product=160:93126, bound_value=174:74790, second_product=348:98436, answer=367:98486)
- Layer 40: `zat`, `acular`, ` sublim`, `zij`, `kten` (target ranks: base_value=80:64219, first_product=160:69647, bound_value=174:32330, second_product=348:45791, answer=367:41000)
- Layer 41: ` .`, `acular`, ` `, `那一`, `转载请` (target ranks: base_value=80:58273, first_product=160:54727, bound_value=174:22047, second_product=348:26525, answer=367:19702)

### Filler position 19 (absolute token 694, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126100, first_product=160:122815, bound_value=174:118556, second_product=348:124379, answer=367:119494)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13045, first_product=160:23865, bound_value=174:29421, second_product=348:24802, answer=367:26763)
- Layer 20: `忑`, `会成为`, `ait`, ` engaging`, `平行` (target ranks: base_value=80:21953, first_product=160:51699, bound_value=174:50340, second_product=348:64033, answer=367:54740)
- Layer 30: ` repetitions`, ` var`, ` repetition`, `重复`, ` repeating` (target ranks: base_value=80:28289, first_product=160:56116, bound_value=174:48460, second_product=348:89175, answer=367:40691)
- Layer 35: ` var`, ` repetition`, `重复`, ` exercises`, ` repetitions` (target ranks: base_value=80:16976, first_product=160:48820, bound_value=174:21535, second_product=348:58795, answer=367:23381)
- Layer 36: ` var`, `重复`, ` repetition`, ` Tw`, `反复` (target ranks: base_value=80:15683, first_product=160:32389, bound_value=174:16674, second_product=348:39220, answer=367:19038)
- Layer 37: `}<?`, `变量的`, ` variables`, ` variable`, ` follow` (target ranks: base_value=80:40157, first_product=160:51353, bound_value=174:44478, second_product=348:79781, answer=367:27619)
- Layer 38: `}<?`, `变量的`, `下沉`, ` variables`, ` variable` (target ranks: base_value=80:43961, first_product=160:64956, bound_value=174:54577, second_product=348:86809, answer=367:18319)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `下沉`, `?datasetId`, `acons` (target ranks: base_value=80:73977, first_product=160:105641, bound_value=174:81482, second_product=348:98302, answer=367:41439)
- Layer 40: `下沉`, ` .`, `šk`, ` sublim`, ` consum` (target ranks: base_value=80:53393, first_product=160:95427, bound_value=174:44300, second_product=348:73574, answer=367:23367)
- Layer 41: ` .`, `有下列`, ` .↵↵`, `下沉`, `.,` (target ranks: base_value=80:40308, first_product=160:50491, bound_value=174:39171, second_product=348:30291, answer=367:17511)

### Filler position 20 (absolute token 695, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126249, first_product=160:123122, bound_value=174:118942, second_product=348:124675, answer=367:119648)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13038, first_product=160:22998, bound_value=174:28451, second_product=348:23494, answer=367:26978)
- Layer 20: `ait`, `会成为`, `距`, `锁定`, `能被` (target ranks: base_value=80:5590, first_product=160:18235, bound_value=174:26052, second_product=348:23024, answer=367:29761)
- Layer 30: ` pakig`, `?datasetId`, `henera`, `}<?`, ` talags` (target ranks: base_value=80:43998, first_product=160:4613, bound_value=174:2285, second_product=348:2521, answer=367:136)
- Layer 35: `349`, `347`, `383`, `379`, `387` (target ranks: base_value=80:56670, first_product=160:63879, bound_value=174:9092, second_product=348:6, answer=367:7)
- Layer 36: `383`, `368`, `367`, `369`, `387` (target ranks: base_value=80:121969, first_product=160:51336, bound_value=174:38227, second_product=348:61, answer=367:3)
- Layer 37: `368`, `367`, `383`, `369`, `366` (target ranks: base_value=80:125288, first_product=160:56436, bound_value=174:38476, second_product=348:88, answer=367:2)
- Layer 38: `367`, `383`, `368`, `369`, `379` (target ranks: base_value=80:129157, first_product=160:123384, bound_value=174:116125, second_product=348:279, answer=367:1)
- Layer 39: `367`, `383`, `369`, `368`, `387` (target ranks: base_value=80:126559, first_product=160:122975, bound_value=174:123700, second_product=348:53743, answer=367:1)
- Layer 40: `367`, `383`, `369`, `387`, `368` (target ranks: base_value=80:127666, first_product=160:123050, bound_value=174:113084, second_product=348:73998, answer=367:1)
- Layer 41: `印书馆`, ` Calculators`, `需要注意的是`, `383`, ` nuest` (target ranks: base_value=80:118859, first_product=160:118043, bound_value=174:105168, second_product=348:71857, answer=367:6)

### Filler position 21 (absolute token 696, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126761, first_product=160:123694, bound_value=174:119786, second_product=348:125114, answer=367:120349)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12952, first_product=160:22646, bound_value=174:28925, second_product=348:23010, answer=367:27396)
- Layer 20: `能被`, `cessive`, ` spinner`, `平行`, ` Tact` (target ranks: base_value=80:11740, first_product=160:23490, bound_value=174:42815, second_product=348:15134, answer=367:33870)
- Layer 30: `}<?`, `?datasetId`, `henera`, `Quintal`, `覆` (target ranks: base_value=80:34033, first_product=160:17125, bound_value=174:4316, second_product=348:6440, answer=367:5624)
- Layer 35: `henera`, `349`, ` freezer`, ` kahaboga`, `348` (target ranks: base_value=80:94235, first_product=160:100847, bound_value=174:4621, second_product=348:5, answer=367:576)
- Layer 36: `?datasetId`, `}<?`, `henera`, `}using`, `attend` (target ranks: base_value=80:123254, first_product=160:78771, bound_value=174:19064, second_product=348:7344, answer=367:1998)
- Layer 37: `?datasetId`, `}<?`, `书馆`, `}using`, `图画` (target ranks: base_value=80:117821, first_product=160:80541, bound_value=174:22121, second_product=348:12180, answer=367:2598)
- Layer 38: `?datasetId`, `}<?`, `书馆`, ` ---|---|---|---`, `attend` (target ranks: base_value=80:127352, first_product=160:121795, bound_value=174:82641, second_product=348:10250, answer=367:425)
- Layer 39: `}<?`, `?datasetId`, `}using`, `笔墨`, `书馆` (target ranks: base_value=80:105982, first_product=160:114602, bound_value=174:124316, second_product=348:119151, answer=367:41762)
- Layer 40: `}using`, `}<?`, ` dot`, ` dekameters`, ` Dot` (target ranks: base_value=80:68810, first_product=160:94543, bound_value=174:106732, second_product=348:112795, answer=367:76144)
- Layer 41: ` .`, ` Let`, ` .↵↵`, ` let`, `笔画` (target ranks: base_value=80:38571, first_product=160:62145, bound_value=174:54540, second_product=348:76630, answer=367:39406)

### Filler position 22 (absolute token 697, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126736, first_product=160:123696, bound_value=174:119833, second_product=348:125181, answer=367:120362)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11784, first_product=160:21923, bound_value=174:27205, second_product=348:21605, answer=367:25815)
- Layer 20: ` quadr`, ` sideways`, ` smile`, `auce`, ` tall` (target ranks: base_value=80:604, first_product=160:4332, bound_value=174:12190, second_product=348:4402, answer=367:11815)
- Layer 30: `Quintal`, `}<?`, `?datasetId`, `东京`, `AssemblyVersion` (target ranks: base_value=80:53850, first_product=160:27949, bound_value=174:19440, second_product=348:36887, answer=367:4592)
- Layer 35: ` Kaw`, ` sled`, `保留`, ` academy`, `坝` (target ranks: base_value=80:71707, first_product=160:68620, bound_value=174:37788, second_product=348:319, answer=367:622)
- Layer 36: `?datasetId`, `坏`, `规制`, `坏的`, `oteksti` (target ranks: base_value=80:100953, first_product=160:38644, bound_value=174:61049, second_product=348:34939, answer=367:288)
- Layer 37: `?datasetId`, `书馆`, `}<?`, `galan`, `ozygous` (target ranks: base_value=80:90542, first_product=160:51835, bound_value=174:70444, second_product=348:44817, answer=367:1337)
- Layer 38: `}<?`, `?datasetId`, `尷`, `galan`, `ozygous` (target ranks: base_value=80:113488, first_product=160:96241, bound_value=174:114561, second_product=348:95001, answer=367:568)
- Layer 39: `ozygous`, `}<?`, `osaurus`, ` Fletcher`, `galan` (target ranks: base_value=80:101969, first_product=160:120634, bound_value=174:125629, second_product=348:119605, answer=367:1198)
- Layer 40: `犹豫`, `�`, ` dotted`, ` torn`, `点滴` (target ranks: base_value=80:65938, first_product=160:107114, bound_value=174:105625, second_product=348:106238, answer=367:4965)
- Layer 41: ` .`, `随便`, ` .↵↵`, `坏`, `让我们` (target ranks: base_value=80:23339, first_product=160:55311, bound_value=174:49288, second_product=348:50390, answer=367:1481)

### Filler position 23 (absolute token 698, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126889, first_product=160:123994, bound_value=174:120056, second_product=348:125441, answer=367:120542)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=80:11918, first_product=160:22087, bound_value=174:27866, second_product=348:22463, answer=367:24874)
- Layer 20: `iganos`, `Dutch`, `leans`, `)Skip`, ` Unc` (target ranks: base_value=80:36979, first_product=160:32232, bound_value=174:56139, second_product=348:35783, answer=367:47197)
- Layer 30: `codeline`, `东京`, `pac`, `日`, ` accompanying` (target ranks: base_value=80:48810, first_product=160:83683, bound_value=174:106157, second_product=348:118365, answer=367:95346)
- Layer 35: `codeline`, ` nasod`, `坏`, ` soci`, ` Alt` (target ranks: base_value=80:71861, first_product=160:121321, bound_value=174:124669, second_product=348:127309, answer=367:109972)
- Layer 36: `兜`, ` nasod`, ` soci`, `坏`, ` Predict` (target ranks: base_value=80:34418, first_product=160:93890, bound_value=174:107152, second_product=348:116229, answer=367:94179)
- Layer 37: `Quintal`, `codeline`, `肤`, `悬挂`, `镶嵌` (target ranks: base_value=80:60215, first_product=160:84843, bound_value=174:118955, second_product=348:124677, answer=367:121101)
- Layer 38: ` .`, `肤`, `兜`, ` germ`, ` .↵↵` (target ranks: base_value=80:65901, first_product=160:69507, bound_value=174:114185, second_product=348:124109, answer=367:117595)
- Layer 39: ` .`, ` .↵↵`, `飘飘`, ` germ`, `肤` (target ranks: base_value=80:113046, first_product=160:106214, bound_value=174:111405, second_product=348:117844, answer=367:105836)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, `点点` (target ranks: base_value=80:108807, first_product=160:76280, bound_value=174:85627, second_product=348:110140, answer=367:96378)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, ` Answer` (target ranks: base_value=80:56104, first_product=160:16320, bound_value=174:10613, second_product=348:46462, answer=367:38304)

### Filler position 24 (absolute token 699, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126797, first_product=160:124124, bound_value=174:120197, second_product=348:125669, answer=367:120470)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: base_value=80:10997, first_product=160:20701, bound_value=174:26874, second_product=348:21833, answer=367:22799)
- Layer 20: `站`, ` smile`, ` Error`, `😂`, ` meta` (target ranks: base_value=80:213, first_product=160:2027, bound_value=174:9828, second_product=348:8034, answer=367:24688)
- Layer 30: `aplenty`, `codeline`, `?datasetId`, `Quintal`, `-ulo` (target ranks: base_value=80:118487, first_product=160:67220, bound_value=174:65469, second_product=348:70642, answer=367:60676)
- Layer 35: `349`, `359`, `347`, `367`, ` böjnings` (target ranks: base_value=80:127009, first_product=160:113665, bound_value=174:69782, second_product=348:9, answer=367:4)
- Layer 36: `367`, `369`, `363`, `359`, `368` (target ranks: base_value=80:128596, first_product=160:80817, bound_value=174:63045, second_product=348:51, answer=367:1)
- Layer 37: `369`, `367`, `363`, `368`, `-ulo` (target ranks: base_value=80:128717, first_product=160:90493, bound_value=174:82712, second_product=348:674, answer=367:2)
- Layer 38: `367`, `369`, `-ulo`, `363`, `359` (target ranks: base_value=80:129184, first_product=160:126261, bound_value=174:118783, second_product=348:2771, answer=367:1)
- Layer 39: `tanle`, ` поха`, `}<?`, `本题分析`, ` Erl` (target ranks: base_value=80:127938, first_product=160:127063, bound_value=174:127221, second_product=348:85298, answer=367:9)
- Layer 40: ` Answer`, `Answer`, `369`, ` Antwort`, `作答` (target ranks: base_value=80:127685, first_product=160:124258, bound_value=174:121353, second_product=348:78376, answer=367:9)
- Layer 41: ` Answer`, `Answer`, ` answer`, `369`, `367` (target ranks: base_value=80:109094, first_product=160:95571, bound_value=174:83443, second_product=348:40312, answer=367:5)

### Filler position 25 (absolute token 700, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `-ulo` (target ranks: base_value=80:121062, first_product=160:111151, bound_value=174:109949, second_product=348:113598, answer=367:107781)
- Layer 10: `EDMF`, ` dével`, `-ulo`, ` поха`, `�乐` (target ranks: base_value=80:128275, first_product=160:101392, bound_value=174:121331, second_product=348:120466, answer=367:100051)
- Layer 20: ` dekameters`, `得分`, ` Numerade`, ` reluct`, `具体的` (target ranks: base_value=80:22830, first_product=160:53649, bound_value=174:102431, second_product=348:83197, answer=367:52249)
- Layer 30: `aplenty`, `nze`, `?datasetId`, ` dátummal`, `widet` (target ranks: base_value=80:86618, first_product=160:28206, bound_value=174:7795, second_product=348:30101, answer=367:50888)
- Layer 35: `348`, `349`, `347`, `346`, `368` (target ranks: base_value=80:122233, first_product=160:106801, bound_value=174:8966, second_product=348:1, answer=367:10)
- Layer 36: `368`, ` поха`, `361`, `367`, `369` (target ranks: base_value=80:129162, first_product=160:38617, bound_value=174:105029, second_product=348:34, answer=367:4)
- Layer 37: `368`, ` поха`, `(migrations`, `367`, `361` (target ranks: base_value=80:129168, first_product=160:39315, bound_value=174:98206, second_product=348:98, answer=367:4)
- Layer 38: `367`, `368`, `362`, `363`, `365` (target ranks: base_value=80:129235, first_product=160:91415, bound_value=174:126513, second_product=348:1520, answer=367:1)
- Layer 39: `367`, `362`, `368`, `zam`, `363` (target ranks: base_value=80:127962, first_product=160:124608, bound_value=174:128605, second_product=348:120824, answer=367:1)
- Layer 40: ` Answer`, ` answer`, `答`, `Answer`, `_answer` (target ranks: base_value=80:128092, first_product=160:95267, bound_value=174:105733, second_product=348:111495, answer=367:1115)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=80:87004, first_product=160:38830, bound_value=174:75032, second_product=348:101353, answer=367:892)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 25 filler tokens (a sequence of dots) before you answer.<｜User｜>zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>176<｜end▁of▁sentence｜><｜User｜>cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>59<｜end▁of▁sentence｜><｜User｜>gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>351<｜end▁of▁sentence｜><｜User｜>mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>229<｜end▁of▁sentence｜><｜User｜>kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zem = 14
yoh = twice the number for zem plus 27
xal = 80
puc = twice the number for xal plus 14
dof = twice the number for puc plus 26
Question: What is twice the number for puc plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
