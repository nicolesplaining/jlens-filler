# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `276` (correct).
- No-filler answer: `268` (incorrect).
- Filler tokens: 50 tokens at absolute indices 793–842.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=64` | 1 (L24, filler 15) | L22, filler 44 (rank 9) |
| J-Lens | `first_product=128` | 2 (L31, filler 43) | L30, filler 43 (rank 6) |
| J-Lens | `bound_value=144` | 1 (L31, filler 43) | L27, filler 15 (rank 7) |
| J-Lens | `second_product=288` | 1 (L30, filler 15) | L30, filler 15 (rank 1) |
| J-Lens | `answer=276` | 1 (L34, filler 1) | L31, filler 1 (rank 2) |
| Logit lens | `base_value=64` | 1 (L27, filler 44) | L25, filler 1 (rank 2) |
| Logit lens | `first_product=128` | 8 (L29, filler 40) | L29, filler 40 (rank 8) |
| Logit lens | `bound_value=144` | 1 (L35, filler 16) | L29, filler 15 (rank 3) |
| Logit lens | `second_product=288` | 1 (L30, filler 15) | L30, filler 15 (rank 1) |
| Logit lens | `answer=276` | 1 (L35, filler 1) | L31, filler 1 (rank 6) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 793, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=64:119824, first_product=128:115072, bound_value=144:109649, second_product=288:114505, answer=276:113049)
- Layer 10: `anta`, `fine`, `hook`, `Hook`, `locked` (target ranks: base_value=64:79938, first_product=128:68884, bound_value=144:69842, second_product=288:67016, answer=276:69975)
- Layer 20: `足`, `扣`, `重`, `表面`, `期望` (target ranks: base_value=64:514, first_product=128:15993, bound_value=144:12792, second_product=288:22529, answer=276:13929)
- Layer 30: `68`, ` الشعاعيه`, `76`, `69`, `sett` (target ranks: base_value=64:1544, first_product=128:213, bound_value=144:1350, second_product=288:176, answer=276:78)
- Layer 35: `276`, `278`, `279`, `277`, `280` (target ranks: base_value=64:12109, first_product=128:6570, bound_value=144:62119, second_product=288:22, answer=276:1)
- Layer 36: `268`, `266`, `276`, `267`, `269` (target ranks: base_value=64:12569, first_product=128:2774, bound_value=144:44683, second_product=288:9, answer=276:3)
- Layer 37: `268`, `266`, `276`, `267`, `269` (target ranks: base_value=64:66350, first_product=128:16677, bound_value=144:75032, second_product=288:9, answer=276:3)
- Layer 38: `268`, `276`, `266`, `267`, `264` (target ranks: base_value=64:107158, first_product=128:39800, bound_value=144:73632, second_product=288:10, answer=276:2)
- Layer 39: `268`, `266`, `267`, `269`, `264` (target ranks: base_value=64:122598, first_product=128:108312, bound_value=144:110418, second_product=288:63, answer=276:59)
- Layer 40: `268`, `266`, `267`, ` talags`, `269` (target ranks: base_value=64:124317, first_product=128:65474, bound_value=144:100879, second_product=288:37, answer=276:296)
- Layer 41: ` nuest`, `266`, ` .`, `267`, `我已经` (target ranks: base_value=64:100839, first_product=128:86773, bound_value=144:91941, second_product=288:1280, answer=276:775)

### Filler position 2 (absolute token 794, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=64:121613, first_product=128:118852, bound_value=144:114758, second_product=288:120096, answer=276:116259)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `挪` (target ranks: base_value=64:20170, first_product=128:36107, bound_value=144:35272, second_product=288:34868, answer=276:31972)
- Layer 20: ` .----`, `往常`, `ools`, `ophers`, `一堂` (target ranks: base_value=64:122764, first_product=128:128854, bound_value=144:128191, second_product=288:129132, answer=276:128983)
- Layer 30: ` talags`, ` pakig`, ` hilabihan`, ` gilay`, ` gihulagway` (target ranks: base_value=64:114289, first_product=128:122867, bound_value=144:127455, second_product=288:125665, answer=276:128985)
- Layer 35: ` hilabihan`, ` .`, `空空`, ` pakig`, `enclose` (target ranks: base_value=64:125517, first_product=128:127358, bound_value=144:128536, second_product=288:127236, answer=276:128428)
- Layer 36: `停`, `幽`, `enclose`, `空空`, ` talags` (target ranks: base_value=64:90135, first_product=128:108613, bound_value=144:125048, second_product=288:102081, answer=276:125768)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, `aplenty`, `�乐` (target ranks: base_value=64:127111, first_product=128:124637, bound_value=144:128494, second_product=288:123422, answer=276:128448)
- Layer 38: ` .`, ` Erkännande`, `enclose`, `繁体`, ` nasod` (target ranks: base_value=64:115581, first_product=128:109545, bound_value=144:125871, second_product=288:113460, answer=276:127548)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` nasod`, ` .↵↵`, ` hilabihan` (target ranks: base_value=64:114760, first_product=128:88986, bound_value=144:117550, second_product=288:104476, answer=276:120127)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=64:60704, first_product=128:33437, bound_value=144:80949, second_product=288:56606, answer=276:88136)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `cab`, ` 。` (target ranks: base_value=64:22689, first_product=128:14049, bound_value=144:33446, second_product=288:20947, answer=276:32881)

### Filler position 3 (absolute token 795, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125264, first_product=128:121079, bound_value=144:118044, second_product=288:123333, answer=276:118576)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:17353, first_product=128:27187, bound_value=144:32027, second_product=288:30082, answer=276:31462)
- Layer 20: `ait`, `忑`, `能被`, ` ternary`, `ashi` (target ranks: base_value=64:6769, first_product=128:37339, bound_value=144:28685, second_product=288:53291, answer=276:45735)
- Layer 30: `计算的`, `calcul`, `算出`, `计算出`, `计算` (target ranks: base_value=64:8366, first_product=128:101704, bound_value=144:56714, second_product=288:72692, answer=276:120417)
- Layer 35: `calcul`, `第一步`, `计算的`, `计算`, ` calculations` (target ranks: base_value=64:3629, first_product=128:82851, bound_value=144:64810, second_product=288:37896, answer=276:106201)
- Layer 36: `calcul`, `计算的`, `计算`, ` calculations`, ` first` (target ranks: base_value=64:5809, first_product=128:61525, bound_value=144:78801, second_product=288:28022, answer=276:106021)
- Layer 37: `calcul`, `计算`, `计算的`, `計算`, ` calculations` (target ranks: base_value=64:9184, first_product=128:74559, bound_value=144:102694, second_product=288:61210, answer=276:118875)
- Layer 38: `}<?`, `asi`, `oses`, ` cál`, `lez` (target ranks: base_value=64:23035, first_product=128:100754, bound_value=144:105241, second_product=288:89936, answer=276:120528)
- Layer 39: ` duc`, ` Duc`, `asi`, `ked`, `ต้` (target ranks: base_value=64:46033, first_product=128:108766, bound_value=144:108409, second_product=288:109531, answer=276:120736)
- Layer 40: ` diz`, `duc`, ` dup`, `d`, ` k` (target ranks: base_value=64:6808, first_product=128:73287, bound_value=144:83372, second_product=288:83942, answer=276:103667)
- Layer 41: ` .`, ` twisted`, ` zad`, ` diz`, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:7065, first_product=128:37992, bound_value=144:72154, second_product=288:53094, answer=276:52129)

### Filler position 4 (absolute token 796, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125829, first_product=128:122673, bound_value=144:119728, second_product=288:124685, answer=276:119805)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:14829, first_product=128:23945, bound_value=144:27883, second_product=288:24561, answer=276:25120)
- Layer 20: `ait`, `atile`, `忑`, `挪`, `锁定` (target ranks: base_value=64:10865, first_product=128:58258, bound_value=144:41820, second_product=288:59510, answer=276:47674)
- Layer 30: ` dripping`, `期望`, `acos`, `简明`, ` esper` (target ranks: base_value=64:28479, first_product=128:101580, bound_value=144:69043, second_product=288:56021, answer=276:124622)
- Layer 35: ` simplified`, ` talags`, `calcul`, `计算`, `計算` (target ranks: base_value=64:12106, first_product=128:66735, bound_value=144:27716, second_product=288:15554, answer=276:93175)
- Layer 36: ` talags`, `calcul`, ` torn`, `期望`, `计算` (target ranks: base_value=64:12848, first_product=128:32826, bound_value=144:23406, second_product=288:10964, answer=276:82385)
- Layer 37: ` talags`, ` resist`, ` Erkännande`, `打磨`, `本题分析` (target ranks: base_value=64:35727, first_product=128:38514, bound_value=144:33778, second_product=288:11318, answer=276:50921)
- Layer 38: `hemer`, `opters`, `interpret`, ` talags`, ` Erkännande` (target ranks: base_value=64:71471, first_product=128:64097, bound_value=144:59230, second_product=288:17975, answer=276:57917)
- Layer 39: `hemer`, `ucl`, `opters`, ` spectator`, ` talags` (target ranks: base_value=64:107649, first_product=128:108290, bound_value=144:99761, second_product=288:18675, answer=276:16966)
- Layer 40: ` talags`, `叮`, ` accustomed`, `oug`, ` drip` (target ranks: base_value=64:99852, first_product=128:113159, bound_value=144:101351, second_product=288:12466, answer=276:3813)
- Layer 41: ` .`, `叮`, `Question`, `提问`, `鹉` (target ranks: base_value=64:83204, first_product=128:84533, bound_value=144:82851, second_product=288:17162, answer=276:2160)

### Filler position 5 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125554, first_product=128:122948, bound_value=144:119907, second_product=288:124644, answer=276:119859)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:16428, first_product=128:26924, bound_value=144:32336, second_product=288:26513, answer=276:28426)
- Layer 20: `幽`, `能被`, `鞍`, `挪`, ` LS` (target ranks: base_value=64:25566, first_product=128:53452, bound_value=144:53463, second_product=288:64389, answer=276:64147)
- Layer 30: ` diz`, ` zad`, ` Zad`, `推算`, `Dict` (target ranks: base_value=64:17211, first_product=128:96561, bound_value=144:73389, second_product=288:70809, answer=276:127186)
- Layer 35: ` diz`, `推算`, ` dig`, ` dip`, ` zad` (target ranks: base_value=64:14864, first_product=128:93709, bound_value=144:81470, second_product=288:48323, answer=276:122396)
- Layer 36: `推算`, ` diz`, ` dri`, ` drip`, ` dig` (target ranks: base_value=64:15705, first_product=128:64718, bound_value=144:83435, second_product=288:29415, answer=276:116826)
- Layer 37: `niz`, ` diz`, ` Zad`, `زياح`, `zat` (target ranks: base_value=64:37577, first_product=128:85144, bound_value=144:98994, second_product=288:55508, answer=276:124454)
- Layer 38: `zat`, ` diz`, `niz`, ` zaz`, `زياح` (target ranks: base_value=64:50045, first_product=128:94912, bound_value=144:94233, second_product=288:59723, answer=276:123546)
- Layer 39: `zat`, `覆`, `ouz`, `hemer`, `东海` (target ranks: base_value=64:62089, first_product=128:78280, bound_value=144:95052, second_product=288:75128, answer=276:117100)
- Layer 40: ` zad`, `hemer`, `覆`, ` z`, `duc` (target ranks: base_value=64:29048, first_product=128:32680, bound_value=144:71191, second_product=288:44533, answer=276:96661)
- Layer 41: ` .`, `叮`, ` zad`, ` twisted`, `急` (target ranks: base_value=64:20366, first_product=128:15877, bound_value=144:57440, second_product=288:25663, answer=276:35829)

### Filler position 6 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125098, first_product=128:122477, bound_value=144:119206, second_product=288:124068, answer=276:119082)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:14291, first_product=128:23648, bound_value=144:30012, second_product=288:23576, answer=276:26157)
- Layer 20: ` answer`, `答案`, `�`, `暂无`, ` calculator` (target ranks: base_value=64:55735, first_product=128:77283, bound_value=144:100815, second_product=288:113639, answer=276:107307)
- Layer 30: `推算`, ` calculator`, `思考`, ` answer`, `回答` (target ranks: base_value=64:28526, first_product=128:16826, bound_value=144:33315, second_product=288:29266, answer=276:59968)
- Layer 35: ` Tw`, `acks`, `Tw`, ` calculator`, ` tw` (target ranks: base_value=64:8928, first_product=128:8724, bound_value=144:15264, second_product=288:8886, answer=276:26741)
- Layer 36: ` Tw`, `calcul`, `推算`, `acks`, ` tw` (target ranks: base_value=64:24308, first_product=128:10809, bound_value=144:30377, second_product=288:15899, answer=276:41801)
- Layer 37: ` Tw`, ` Calculators`, `calcul`, `推算`, `acks` (target ranks: base_value=64:63043, first_product=128:21564, bound_value=144:60077, second_product=288:49296, answer=276:64431)
- Layer 38: ` Tw`, ` Calculators`, `calcul`, ` nasod`, `推算` (target ranks: base_value=64:81969, first_product=128:19772, bound_value=144:43965, second_product=288:34383, answer=276:46668)
- Layer 39: ` Dominic`, ` nasod`, `ophe`, `-ulo`, `替换` (target ranks: base_value=64:84807, first_product=128:75915, bound_value=144:121596, second_product=288:126337, answer=276:122047)
- Layer 40: ` Tw`, ` nasod`, `Tw`, `klar`, ` talags` (target ranks: base_value=64:58359, first_product=128:76137, bound_value=144:122304, second_product=288:124978, answer=276:121373)
- Layer 41: ` Tw`, ` .`, `婷婷`, `试一试`, ` dekameters` (target ranks: base_value=64:77378, first_product=128:76909, bound_value=144:123631, second_product=288:123515, answer=276:108189)

### Filler position 7 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:124953, first_product=128:122279, bound_value=144:118976, second_product=288:123844, answer=276:118971)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13100, first_product=128:23050, bound_value=144:28585, second_product=288:24226, answer=276:26422)
- Layer 20: `锁定`, `ait`, `Ta`, `cape`, `足` (target ranks: base_value=64:4577, first_product=128:15954, bound_value=144:19724, second_product=288:29538, answer=276:28795)
- Layer 30: ` calculator`, ` Cogn`, `鞍`, `yg`, `calculator` (target ranks: base_value=64:137, first_product=128:4564, bound_value=144:4295, second_product=288:2367, answer=276:15091)
- Layer 35: ` smile`, ` labor`, `Subt`, `保留`, ` future` (target ranks: base_value=64:147, first_product=128:3656, bound_value=144:3798, second_product=288:1121, answer=276:4321)
- Layer 36: `anium`, `acin`, `calcul`, `aci`, `特` (target ranks: base_value=64:559, first_product=128:2202, bound_value=144:6799, second_product=288:1165, answer=276:7975)
- Layer 37: `anium`, `}<?`, `polar`, `ocyst`, `思想的` (target ranks: base_value=64:9681, first_product=128:7426, bound_value=144:18635, second_product=288:1220, answer=276:2153)
- Layer 38: `}<?`, `ocyst`, `-ulo`, `思想的`, `polar` (target ranks: base_value=64:25604, first_product=128:12348, bound_value=144:26029, second_product=288:4871, answer=276:3111)
- Layer 39: `-ulo`, `}<?`, `ocyst`, `叶子`, `思想的` (target ranks: base_value=64:111962, first_product=128:118319, bound_value=144:122429, second_product=288:25369, answer=276:3112)
- Layer 40: ` talags`, `悬念`, `留存`, `隐私`, `语言文字` (target ranks: base_value=64:115931, first_product=128:125142, bound_value=144:127138, second_product=288:20749, answer=276:1947)
- Layer 41: ` .`, `悬念`, `癫�`, `老乡`, `))))` (target ranks: base_value=64:108739, first_product=128:115468, bound_value=144:123639, second_product=288:23062, answer=276:2541)

### Filler position 8 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124756, first_product=128:121953, bound_value=144:118635, second_product=288:123484, answer=276:118685)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11866, first_product=128:21913, bound_value=144:28095, second_product=288:22975, answer=276:24781)
- Layer 20: `ait`, ` Walker`, `锁定`, `挪`, `Walker` (target ranks: base_value=64:18404, first_product=128:52723, bound_value=144:47444, second_product=288:62473, answer=276:69373)
- Layer 30: `coding`, ` diz`, ` pakig`, `cod`, ` coding` (target ranks: base_value=64:48812, first_product=128:125233, bound_value=144:118119, second_product=288:117577, answer=276:128621)
- Layer 35: ` diz`, `coding`, ` dig`, `cod`, ` coding` (target ranks: base_value=64:23393, first_product=128:113710, bound_value=144:104090, second_product=288:93716, answer=276:126812)
- Layer 36: ` dri`, `留存`, `coding`, `cod`, ` drip` (target ranks: base_value=64:25041, first_product=128:100357, bound_value=144:107933, second_product=288:78999, answer=276:127273)
- Layer 37: `}<?`, `cod`, `coding`, `acos`, ` diz` (target ranks: base_value=64:62807, first_product=128:118852, bound_value=144:122344, second_product=288:108256, answer=276:128440)
- Layer 38: `}<?`, `迷惑`, `zat`, ` sublim`, ` pakig` (target ranks: base_value=64:63810, first_product=128:118093, bound_value=144:121841, second_product=288:105498, answer=276:127936)
- Layer 39: `}<?`, `迷惑`, `糊涂`, `ocyst`, `繁体` (target ranks: base_value=64:69315, first_product=128:106831, bound_value=144:122044, second_product=288:119094, answer=276:127933)
- Layer 40: ` v`, `šk`, `留存`, `殿堂`, ` sublim` (target ranks: base_value=64:21218, first_product=128:62946, bound_value=144:109079, second_product=288:109152, answer=276:125670)
- Layer 41: ` .`, `acular`, `鹉`, `šk`, `留存` (target ranks: base_value=64:13346, first_product=128:24454, bound_value=144:76561, second_product=288:74662, answer=276:98855)

### Filler position 9 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124805, first_product=128:122124, bound_value=144:118885, second_product=288:123687, answer=276:118887)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12111, first_product=128:22725, bound_value=144:28982, second_product=288:23134, answer=276:25064)
- Layer 20: `ait`, ` Walker`, `锁定`, `挪`, `Walker` (target ranks: base_value=64:12563, first_product=128:40767, bound_value=144:34211, second_product=288:46457, answer=276:50447)
- Layer 30: ` variable`, ` var`, `variable`, `Variable`, ` Variable` (target ranks: base_value=64:39759, first_product=128:101440, bound_value=144:71555, second_product=288:81594, answer=276:122701)
- Layer 35: ` var`, ` variable`, `Variable`, ` Variable`, `variable` (target ranks: base_value=64:9299, first_product=128:56515, bound_value=144:51209, second_product=288:40903, answer=276:97540)
- Layer 36: ` definitions`, ` variable`, ` var`, `输入的`, ` variables` (target ranks: base_value=64:21068, first_product=128:67892, bound_value=144:67672, second_product=288:50022, answer=276:114767)
- Layer 37: `Variables`, ` definitions`, ` variable`, ` variables`, ` Variables` (target ranks: base_value=64:63784, first_product=128:91545, bound_value=144:88989, second_product=288:73525, answer=276:125440)
- Layer 38: `Variables`, ` Variables`, ` Variable`, ` variable`, `Variable` (target ranks: base_value=64:69281, first_product=128:91189, bound_value=144:97058, second_product=288:51680, answer=276:124096)
- Layer 39: ` Variable`, ` перемен`, ` Variables`, `Variables`, `variables` (target ranks: base_value=64:74038, first_product=128:78838, bound_value=144:108085, second_product=288:102445, answer=276:127398)
- Layer 40: `šk`, ` definitions`, ` prompt`, `下沉`, ` Zad` (target ranks: base_value=64:34755, first_product=128:54285, bound_value=144:91694, second_product=288:92981, answer=276:127555)
- Layer 41: ` .`, ` definitions`, ` variable`, ` variables`, `猕猴` (target ranks: base_value=64:29423, first_product=128:31399, bound_value=144:80996, second_product=288:81808, answer=276:112355)

### Filler position 10 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124544, first_product=128:121953, bound_value=144:118885, second_product=288:123670, answer=276:118911)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11705, first_product=128:22396, bound_value=144:28635, second_product=288:22922, answer=276:24698)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, ` smile` (target ranks: base_value=64:8864, first_product=128:40375, bound_value=144:42257, second_product=288:54332, answer=276:49556)
- Layer 30: `Tap`, ` tap`, ` Tap`, `acos`, ` rip` (target ranks: base_value=64:18900, first_product=128:116084, bound_value=144:91717, second_product=288:88468, answer=276:123348)
- Layer 35: `Tap`, ` tap`, ` Tap`, `tap`, `acin` (target ranks: base_value=64:35336, first_product=128:105119, bound_value=144:87414, second_product=288:46691, answer=276:113507)
- Layer 36: ` tap`, ` riv`, ` drip`, `Tap`, ` zad` (target ranks: base_value=64:28689, first_product=128:92228, bound_value=144:75333, second_product=288:19607, answer=276:94731)
- Layer 37: `amol`, ` nac`, `zim`, ` Riv`, `pac` (target ranks: base_value=64:66237, first_product=128:107626, bound_value=144:86820, second_product=288:39663, answer=276:114460)
- Layer 38: `zat`, `�`, `}<?`, `pac`, `本题分析` (target ranks: base_value=64:80985, first_product=128:114499, bound_value=144:99626, second_product=288:66907, answer=276:121349)
- Layer 39: `�`, `zat`, ` Nij`, `zel`, `斐` (target ranks: base_value=64:55824, first_product=128:98466, bound_value=144:62327, second_product=288:36973, answer=276:102717)
- Layer 40: `zel`, ` fum`, `zat`, `pac`, `amn` (target ranks: base_value=64:27576, first_product=128:56450, bound_value=144:36380, second_product=288:12861, answer=276:87292)
- Layer 41: `zel`, ` fum`, ` bamb`, ` mim`, `我怎么` (target ranks: base_value=64:15011, first_product=128:9309, bound_value=144:8692, second_product=288:3744, answer=276:9341)

### Filler position 11 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124589, first_product=128:122151, bound_value=144:119174, second_product=288:123813, answer=276:119029)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11192, first_product=128:22381, bound_value=144:28234, second_product=288:22123, answer=276:23708)
- Layer 20: ` Walker`, ` smile`, `Walker`, `忑`, `能被` (target ranks: base_value=64:14150, first_product=128:47558, bound_value=144:42772, second_product=288:57012, answer=276:52910)
- Layer 30: `64`, `反复`, ` repeated`, `退出`, ` pooling` (target ranks: base_value=64:1, first_product=128:604, bound_value=144:64, second_product=288:498, answer=276:63717)
- Layer 35: `144`, `288`, `64`, `翻`, ` repeated` (target ranks: base_value=64:3, first_product=128:301, bound_value=144:1, second_product=288:2, answer=276:24663)
- Layer 36: `288`, `144`, `radesh`, `翻`, `calcul` (target ranks: base_value=64:26, first_product=128:653, bound_value=144:2, second_product=288:1, answer=276:64432)
- Layer 37: `radesh`, `144`, `}<?`, `殿堂`, ` doubling` (target ranks: base_value=64:233, first_product=128:1846, bound_value=144:2, second_product=288:6, answer=276:108358)
- Layer 38: `}<?`, `oNames`, `殿堂`, `Divisors`, `radesh` (target ranks: base_value=64:1983, first_product=128:9356, bound_value=144:21, second_product=288:84, answer=276:109468)
- Layer 39: `}<?`, `-ulo`, `东海`, `ocyst`, `树叶` (target ranks: base_value=64:10033, first_product=128:19706, bound_value=144:343, second_product=288:1784, answer=276:97330)
- Layer 40: `zam`, ` twisted`, `翻`, `俯`, `etted` (target ranks: base_value=64:16785, first_product=128:19389, bound_value=144:1087, second_product=288:2507, answer=276:66971)
- Layer 41: ` .`, `zam`, `zel`, `zp`, `叮` (target ranks: base_value=64:5230, first_product=128:2266, bound_value=144:168, second_product=288:259, answer=276:14268)

### Filler position 12 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124488, first_product=128:122132, bound_value=144:119212, second_product=288:123776, answer=276:118932)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11303, first_product=128:22555, bound_value=144:28506, second_product=288:22263, answer=276:24495)
- Layer 20: `ait`, `锁定`, ` smile`, ` ES`, ` wig` (target ranks: base_value=64:7116, first_product=128:30453, bound_value=144:30951, second_product=288:40405, answer=276:33736)
- Layer 30: `Tap`, ` tap`, `tap`, ` Tap`, ` glacier` (target ranks: base_value=64:45017, first_product=128:67080, bound_value=144:63397, second_product=288:27607, answer=276:87703)
- Layer 35: ` tap`, `冰冰`, ` glacier`, `Tap`, `acin` (target ranks: base_value=64:54977, first_product=128:81095, bound_value=144:99173, second_product=288:49394, answer=276:104917)
- Layer 36: ` tap`, `acin`, `冰冰`, ` glacier`, `agia` (target ranks: base_value=64:29109, first_product=128:43688, bound_value=144:92057, second_product=288:34680, answer=276:91150)
- Layer 37: `冰冰`, `acos`, ` resist`, `覆`, `}<?` (target ranks: base_value=64:72719, first_product=128:65825, bound_value=144:112421, second_product=288:65385, answer=276:113677)
- Layer 38: `冰冰`, `}<?`, `�`, `acons`, `ocyst` (target ranks: base_value=64:89488, first_product=128:83449, bound_value=144:114022, second_product=288:58888, answer=276:105177)
- Layer 39: `hemer`, `东海`, `ocyst`, `}<?`, `hatic` (target ranks: base_value=64:47664, first_product=128:75356, bound_value=144:99416, second_product=288:89829, answer=276:111452)
- Layer 40: `冰冰`, ` Zad`, ` nasod`, `acl`, `试一试` (target ranks: base_value=64:7511, first_product=128:35110, bound_value=144:71531, second_product=288:60972, answer=276:97501)
- Layer 41: ` .`, `试一试`, `鹉`, `叮`, `提问` (target ranks: base_value=64:1724, first_product=128:8107, bound_value=144:31979, second_product=288:26072, answer=276:18849)

### Filler position 13 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124435, first_product=128:122150, bound_value=144:119266, second_product=288:123779, answer=276:118911)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10895, first_product=128:22075, bound_value=144:28203, second_product=288:22367, answer=276:24298)
- Layer 20: `ait`, `锁定`, ` Walker`, `忑`, `Walker` (target ranks: base_value=64:11560, first_product=128:32558, bound_value=144:31553, second_product=288:44785, answer=276:41157)
- Layer 30: ` Heim`, `acos`, `acin`, `Tw`, ` twice` (target ranks: base_value=64:9410, first_product=128:16855, bound_value=144:13008, second_product=288:5588, answer=276:21480)
- Layer 35: ` Heim`, ` calculator`, `acin`, `保留`, `obin` (target ranks: base_value=64:11928, first_product=128:37449, bound_value=144:25319, second_product=288:659, answer=276:522)
- Layer 36: ` Zad`, ` Carlisle`, `acin`, `anium`, `翻` (target ranks: base_value=64:29802, first_product=128:19068, bound_value=144:31034, second_product=288:467, answer=276:318)
- Layer 37: `}<?`, `覆`, `anium`, `urin`, `殿堂` (target ranks: base_value=64:82931, first_product=128:31674, bound_value=144:60379, second_product=288:1462, answer=276:431)
- Layer 38: `}<?`, `EDMF`, `覆`, `殿堂`, `Noiz` (target ranks: base_value=64:89961, first_product=128:51818, bound_value=144:76586, second_product=288:4532, answer=276:532)
- Layer 39: `}<?`, `268`, `下沉`, `urin`, `叶子` (target ranks: base_value=64:71765, first_product=128:84152, bound_value=144:70328, second_product=288:1291, answer=276:280)
- Layer 40: `268`, `}<?`, `下沉`, `enclose`, ` drip` (target ranks: base_value=64:33996, first_product=128:61365, bound_value=144:67832, second_product=288:380, answer=276:650)
- Layer 41: ` .`, `266`, ` `, `zl`, `268` (target ranks: base_value=64:32565, first_product=128:45357, bound_value=144:53934, second_product=288:1647, answer=276:801)

### Filler position 14 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124724, first_product=128:122383, bound_value=144:119786, second_product=288:124123, answer=276:119244)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9935, first_product=128:21079, bound_value=144:26793, second_product=288:21350, answer=276:22877)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` smile` (target ranks: base_value=64:8615, first_product=128:29884, bound_value=144:28488, second_product=288:39576, answer=276:37310)
- Layer 30: `提问`, `询问`, ` question`, ` questions`, `回答问题` (target ranks: base_value=64:11649, first_product=128:52433, bound_value=144:49648, second_product=288:31686, answer=276:91667)
- Layer 35: `询问`, ` Tw`, `ask`, `提问`, ` question` (target ranks: base_value=64:4106, first_product=128:36401, bound_value=144:29349, second_product=288:24880, answer=276:78897)
- Layer 36: ` final`, ` question`, `询问`, `提问`, ` Question` (target ranks: base_value=64:10184, first_product=128:40233, bound_value=144:45927, second_product=288:33116, answer=276:100432)
- Layer 37: `}<?`, ` final`, ` question`, `提问`, `asking` (target ranks: base_value=64:34448, first_product=128:64901, bound_value=144:79054, second_product=288:70696, answer=276:120020)
- Layer 38: `}<?`, `珍珠`, `计算公式`, `打磨`, `calcul` (target ranks: base_value=64:38035, first_product=128:76147, bound_value=144:84156, second_product=288:65466, answer=276:115709)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `珍珠`, `殿堂`, `打磨` (target ranks: base_value=64:54135, first_product=128:60716, bound_value=144:89783, second_product=288:94491, answer=276:123299)
- Layer 40: `scr`, `殿堂`, `šk`, `留存`, ` Tw` (target ranks: base_value=64:14376, first_product=128:33779, bound_value=144:74307, second_product=288:73829, answer=276:122043)
- Layer 41: ` .`, `鹉`, `工作任务`, ` `, `zac` (target ranks: base_value=64:5362, first_product=128:9647, bound_value=144:39959, second_product=288:53293, answer=276:87425)

### Filler position 15 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125126, first_product=128:122822, bound_value=144:120250, second_product=288:124439, answer=276:119741)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10064, first_product=128:21383, bound_value=144:26868, second_product=288:21363, answer=276:22668)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, `距` (target ranks: base_value=64:4616, first_product=128:22618, bound_value=144:22701, second_product=288:26756, answer=276:32676)
- Layer 30: `288`, `144`, `289`, `286`, `688` (target ranks: base_value=64:874, first_product=128:404, bound_value=144:2, second_product=288:1, answer=276:9824)
- Layer 35: `288`, `289`, `287`, `286`, `IPE` (target ranks: base_value=64:94934, first_product=128:61672, bound_value=144:69, second_product=288:1, answer=276:4501)
- Layer 36: `288`, `287`, `289`, `286`, `桃子` (target ranks: base_value=64:121456, first_product=128:32336, bound_value=144:1347, second_product=288:1, answer=276:6970)
- Layer 37: `288`, `287`, `289`, `286`, `桃子` (target ranks: base_value=64:125885, first_product=128:34302, bound_value=144:3836, second_product=288:1, answer=276:8586)
- Layer 38: `288`, `287`, `289`, `286`, `蟠` (target ranks: base_value=64:126474, first_product=128:55959, bound_value=144:12546, second_product=288:1, answer=276:14259)
- Layer 39: `288`, `287`, `289`, ` dátummal`, `麝` (target ranks: base_value=64:124741, first_product=128:118107, bound_value=144:39645, second_product=288:1, answer=276:34825)
- Layer 40: `288`, `287`, ` dátummal`, ` loose`, `289` (target ranks: base_value=64:124234, first_product=128:116729, bound_value=144:92356, second_product=288:1, answer=276:12722)
- Layer 41: `288`, ` dátummal`, `出不穷`, `因为`, `告辞` (target ranks: base_value=64:126099, first_product=128:120796, bound_value=144:101120, second_product=288:1, answer=276:44366)

### Filler position 16 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125121, first_product=128:122989, bound_value=144:120409, second_product=288:124582, answer=276:119813)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11305, first_product=128:22087, bound_value=144:28131, second_product=288:21944, answer=276:23349)
- Layer 20: `ait`, `能被`, `距`, ` Walker`, ` smile` (target ranks: base_value=64:6220, first_product=128:32418, bound_value=144:30062, second_product=288:40606, answer=276:41876)
- Layer 30: `acos`, `144`, `acin`, `Dynamic`, `鞍` (target ranks: base_value=64:29, first_product=128:737, bound_value=144:2, second_product=288:8, answer=276:32698)
- Layer 35: `144`, `288`, `ukiran`, `289`, ` fibr` (target ranks: base_value=64:11325, first_product=128:35049, bound_value=144:1, second_product=288:2, answer=276:20095)
- Layer 36: `288`, `144`, ` Steiner`, ` fibr`, `Quintal` (target ranks: base_value=64:23964, first_product=128:43177, bound_value=144:2, second_product=288:1, answer=276:40320)
- Layer 37: `288`, `144`, `Quintal`, `师徒`, `桃子` (target ranks: base_value=64:59143, first_product=128:55312, bound_value=144:2, second_product=288:1, answer=276:58374)
- Layer 38: `288`, `144`, `师徒`, `桃子`, `蟠` (target ranks: base_value=64:83997, first_product=128:72416, bound_value=144:2, second_product=288:1, answer=276:65016)
- Layer 39: `288`, `桃子`, `-ulo`, `144`, ` spectator` (target ranks: base_value=64:91151, first_product=128:89842, bound_value=144:4, second_product=288:1, answer=276:26296)
- Layer 40: `288`, ` spectator`, ` loose`, `289`, `144` (target ranks: base_value=64:66135, first_product=128:68237, bound_value=144:5, second_product=288:1, answer=276:5661)
- Layer 41: `288`, ` .`, `也没有`, `样子`, `不会被` (target ranks: base_value=64:77677, first_product=128:64727, bound_value=144:98, second_product=288:1, answer=276:5825)

### Filler position 17 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125231, first_product=128:123162, bound_value=144:120720, second_product=288:124773, answer=276:120098)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12157, first_product=128:22936, bound_value=144:29500, second_product=288:22834, answer=276:24635)
- Layer 20: `距`, ` smile`, `能被`, ` Engaging`, ` engaging` (target ranks: base_value=64:22640, first_product=128:43576, bound_value=144:46036, second_product=288:53106, answer=276:47092)
- Layer 30: ` twice`, ` Tw`, ` repeated`, `反复`, `Tw` (target ranks: base_value=64:23, first_product=128:9098, bound_value=144:14375, second_product=288:5083, answer=276:54937)
- Layer 35: ` Tw`, ` repeated`, ` smile`, ` twice`, `Tw` (target ranks: base_value=64:9, first_product=128:6564, bound_value=144:10990, second_product=288:2747, answer=276:41683)
- Layer 36: ` repeated`, `反复`, `分解`, `翻`, `cod` (target ranks: base_value=64:44, first_product=128:8187, bound_value=144:27063, second_product=288:3388, answer=276:66073)
- Layer 37: `}<?`, ` doubling`, `radesh`, `翻`, `zat` (target ranks: base_value=64:29, first_product=128:12293, bound_value=144:39065, second_product=288:8402, answer=276:96333)
- Layer 38: `}<?`, `zat`, ` doubling`, `覆`, `radesh` (target ranks: base_value=64:366, first_product=128:22898, bound_value=144:45404, second_product=288:16207, answer=276:94016)
- Layer 39: `}<?`, `uerak`, `覆`, `uffman`, `-ulo` (target ranks: base_value=64:1728, first_product=128:36338, bound_value=144:83090, second_product=288:47889, answer=276:112110)
- Layer 40: `坏`, `坏的`, `}<?`, `覆`, `duc` (target ranks: base_value=64:1423, first_product=128:27387, bound_value=144:69975, second_product=288:29960, answer=276:114259)
- Layer 41: ` .`, `less`, ` `, `坏`, `外层` (target ranks: base_value=64:2379, first_product=128:28561, bound_value=144:77660, second_product=288:22703, answer=276:79730)

### Filler position 18 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125142, first_product=128:122977, bound_value=144:120586, second_product=288:124593, answer=276:119924)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11117, first_product=128:22174, bound_value=144:28475, second_product=288:22658, answer=276:24415)
- Layer 20: `ait`, ` Walker`, `锁定`, ` engaging`, `忑` (target ranks: base_value=64:16145, first_product=128:41209, bound_value=144:42041, second_product=288:59549, answer=276:58014)
- Layer 30: `算出`, `计算出`, ` calculator`, `计算的`, `calcul` (target ranks: base_value=64:10712, first_product=128:65230, bound_value=144:60745, second_product=288:81717, answer=276:118402)
- Layer 35: ` Tw`, `calcul`, `Tw`, `计算的`, ` calculator` (target ranks: base_value=64:6513, first_product=128:48978, bound_value=144:65045, second_product=288:55151, answer=276:111215)
- Layer 36: `calcul`, ` Tw`, `计算的`, `Tw`, ` calculator` (target ranks: base_value=64:8460, first_product=128:35410, bound_value=144:82975, second_product=288:42215, answer=276:114181)
- Layer 37: `calcul`, `}<?`, `计算的`, ` Calculators`, `不加` (target ranks: base_value=64:24530, first_product=128:54862, bound_value=144:113455, second_product=288:79782, answer=276:125354)
- Layer 38: `}<?`, `zat`, `calcul`, `计算的`, ` Nij` (target ranks: base_value=64:38682, first_product=128:71735, bound_value=144:114781, second_product=288:93215, answer=276:124383)
- Layer 39: `zat`, `}<?`, ` Nij`, `殿堂`, `�` (target ranks: base_value=64:40462, first_product=128:51344, bound_value=144:106378, second_product=288:92757, answer=276:125479)
- Layer 40: `zat`, `zij`, `šk`, ` zad`, `殿堂` (target ranks: base_value=64:8078, first_product=128:21256, bound_value=144:76103, second_product=288:49651, answer=276:119953)
- Layer 41: ` zad`, `zij`, `šk`, `叮`, ` .` (target ranks: base_value=64:2521, first_product=128:10178, bound_value=144:57038, second_product=288:27591, answer=276:87913)

### Filler position 19 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125351, first_product=128:123454, bound_value=144:121226, second_product=288:124996, answer=276:120343)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10271, first_product=128:21028, bound_value=144:27169, second_product=288:21885, answer=276:23513)
- Layer 20: `忑`, `ait`, ` engaging`, ` Walker`, `锁定` (target ranks: base_value=64:14162, first_product=128:45554, bound_value=144:37641, second_product=288:58798, answer=276:67923)
- Layer 30: ` diz`, ` dy`, ` dia`, ` dice`, ` Dia` (target ranks: base_value=64:3510, first_product=128:101732, bound_value=144:80338, second_product=288:67688, answer=276:125101)
- Layer 35: ` diz`, ` dia`, ` dip`, ` dy`, ` dig` (target ranks: base_value=64:1436, first_product=128:89121, bound_value=144:72097, second_product=288:52870, answer=276:118410)
- Layer 36: ` diz`, `留存`, ` dri`, ` dice`, ` dio` (target ranks: base_value=64:1258, first_product=128:78005, bound_value=144:87612, second_product=288:46867, answer=276:123369)
- Layer 37: ` diz`, `niz`, ` Liz`, `}<?`, `迷惑` (target ranks: base_value=64:5303, first_product=128:112786, bound_value=144:115403, second_product=288:90350, answer=276:128001)
- Layer 38: ` diz`, `niz`, `}<?`, `迷惑`, ` Liz` (target ranks: base_value=64:8870, first_product=128:119432, bound_value=144:115700, second_product=288:98427, answer=276:126582)
- Layer 39: `迷惑`, ` diz`, `niz`, `}<?`, `打磨` (target ranks: base_value=64:28487, first_product=128:107666, bound_value=144:111787, second_product=288:92045, answer=276:125455)
- Layer 40: ` sublim`, `迷惑`, ` diz`, `acular`, `ked` (target ranks: base_value=64:9154, first_product=128:67698, bound_value=144:89718, second_product=288:51651, answer=276:115908)
- Layer 41: ` .`, `acular`, ` diz`, `鹉`, `zij` (target ranks: base_value=64:3871, first_product=128:19391, bound_value=144:54950, second_product=288:18857, answer=276:68211)

### Filler position 20 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125447, first_product=128:123470, bound_value=144:121197, second_product=288:125065, answer=276:120423)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9988, first_product=128:20024, bound_value=144:26664, second_product=288:21234, answer=276:22815)
- Layer 20: `ait`, `能被`, ` Walker`, `拆`, `锁定` (target ranks: base_value=64:7134, first_product=128:32880, bound_value=144:26300, second_product=288:39663, answer=276:42211)
- Layer 30: `Subt`, `EDER`, `subt`, ` basal`, ` Cogn` (target ranks: base_value=64:4480, first_product=128:2081, bound_value=144:247, second_product=288:185, answer=276:608)
- Layer 35: `288`, `268`, `289`, `388`, `280` (target ranks: base_value=64:32391, first_product=128:11300, bound_value=144:90684, second_product=288:1, answer=276:8)
- Layer 36: `268`, `276`, `267`, `274`, `260` (target ranks: base_value=64:57206, first_product=128:8484, bound_value=144:110271, second_product=288:11, answer=276:2)
- Layer 37: `276`, `268`, `278`, `urin`, `267` (target ranks: base_value=64:88516, first_product=128:11346, bound_value=144:109534, second_product=288:11, answer=276:1)
- Layer 38: `276`, `268`, `274`, `266`, `260` (target ranks: base_value=64:96074, first_product=128:73975, bound_value=144:115746, second_product=288:22, answer=276:1)
- Layer 39: `276`, `268`, `277`, `274`, `476` (target ranks: base_value=64:114022, first_product=128:124064, bound_value=144:126466, second_product=288:3809, answer=276:1)
- Layer 40: `276`, `268`, `274`, ` nahimutangan`, ` gihulagway` (target ranks: base_value=64:122676, first_product=128:122270, bound_value=144:127049, second_product=288:852, answer=276:1)
- Layer 41: `276`, ` nuest`, `iented`, `................................................`, ` nahimutangan` (target ranks: base_value=64:95999, first_product=128:113574, bound_value=144:124178, second_product=288:11686, answer=276:1)

### Filler position 21 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125735, first_product=128:123868, bound_value=144:121756, second_product=288:125387, answer=276:120780)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9513, first_product=128:20328, bound_value=144:26829, second_product=288:21349, answer=276:22677)
- Layer 20: `ait`, ` engaging`, `距`, `锁定`, `能被` (target ranks: base_value=64:13974, first_product=128:36436, bound_value=144:28455, second_product=288:44908, answer=276:48701)
- Layer 30: `acos`, ` consuming`, `上市的`, `asting`, ` kinainitan` (target ranks: base_value=64:3697, first_product=128:10028, bound_value=144:1611, second_product=288:1553, answer=276:9013)
- Layer 35: `280`, `acin`, `外向`, `漂流`, `asting` (target ranks: base_value=64:5210, first_product=128:18675, bound_value=144:12643, second_product=288:966, answer=276:459)
- Layer 36: `漂流`, `外向`, `asting`, `280`, `868` (target ranks: base_value=64:4273, first_product=128:8418, bound_value=144:3225, second_product=288:376, answer=276:1788)
- Layer 37: ` hectometers`, ` dekameters`, `漂流`, `udeau`, `osm` (target ranks: base_value=64:25401, first_product=128:20215, bound_value=144:6884, second_product=288:2707, answer=276:10586)
- Layer 38: ` hectometers`, ` dekameters`, `院内`, `精英`, `odecimal` (target ranks: base_value=64:50688, first_product=128:14469, bound_value=144:8826, second_product=288:1285, answer=276:589)
- Layer 39: `268`, `266`, `267`, `galan`, `264` (target ranks: base_value=64:97889, first_product=128:85888, bound_value=144:84599, second_product=288:1153, answer=276:94)
- Layer 40: `268`, ` hectometers`, ` drip`, `isted`, ` dekameters` (target ranks: base_value=64:111034, first_product=128:77287, bound_value=144:71838, second_product=288:111, answer=276:143)
- Layer 41: ` .`, `268`, `266`, ` dekameters`, ` hectometers` (target ranks: base_value=64:89532, first_product=128:66558, bound_value=144:61870, second_product=288:390, answer=276:108)

### Filler position 22 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125845, first_product=128:124110, bound_value=144:122013, second_product=288:125535, answer=276:120861)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: base_value=64:9252, first_product=128:20410, bound_value=144:26538, second_product=288:20852, answer=276:21708)
- Layer 20: `ait`, `锁定`, `距`, ` smile`, ` Walker` (target ranks: base_value=64:10149, first_product=128:30167, bound_value=144:24792, second_product=288:35835, answer=276:39280)
- Layer 30: `coding`, `cod`, `code`, `分解`, ` Zad` (target ranks: base_value=64:6637, first_product=128:37337, bound_value=144:32726, second_product=288:33926, answer=276:108764)
- Layer 35: `cod`, `coding`, `kod`, ` Tw`, `分解` (target ranks: base_value=64:7081, first_product=128:29781, bound_value=144:30708, second_product=288:32524, answer=276:95629)
- Layer 36: ` Zad`, `cod`, `coding`, `分解`, `kod` (target ranks: base_value=64:9368, first_product=128:16035, bound_value=144:41906, second_product=288:26377, answer=276:100561)
- Layer 37: `zat`, ` Zad`, `cod`, `coding`, `}<?` (target ranks: base_value=64:31156, first_product=128:20145, bound_value=144:76772, second_product=288:62305, answer=276:121421)
- Layer 38: `zat`, ` z`, ` Zad`, `}<?`, `pac` (target ranks: base_value=64:40535, first_product=128:36321, bound_value=144:77207, second_product=288:63500, answer=276:116773)
- Layer 39: `zat`, ` z`, ` Zij`, `zv`, ` Z` (target ranks: base_value=64:28684, first_product=128:26303, bound_value=144:71309, second_product=288:49908, answer=276:110453)
- Layer 40: `zat`, ` z`, ` Z`, `z`, `zij` (target ranks: base_value=64:5892, first_product=128:6771, bound_value=144:27485, second_product=288:14968, answer=276:89774)
- Layer 41: `z`, ` .`, ` `, `zij`, ` twist` (target ranks: base_value=64:1588, first_product=128:1713, bound_value=144:17455, second_product=288:5135, answer=276:24919)

### Filler position 23 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125962, first_product=128:124317, bound_value=144:122198, second_product=288:125753, answer=276:121020)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10561, first_product=128:21182, bound_value=144:27883, second_product=288:21232, answer=276:22603)
- Layer 20: ` smile`, `足`, ` Tears`, `ait`, `锁定` (target ranks: base_value=64:7505, first_product=128:20683, bound_value=144:17327, second_product=288:27385, answer=276:33803)
- Layer 30: `cod`, `coding`, ` Zad`, `kod`, ` zad` (target ranks: base_value=64:10181, first_product=128:55504, bound_value=144:35407, second_product=288:36856, answer=276:115756)
- Layer 35: `cod`, `coding`, `kod`, ` z`, `Cod` (target ranks: base_value=64:15108, first_product=128:56458, bound_value=144:53269, second_product=288:45965, answer=276:112332)
- Layer 36: `cod`, `coding`, ` Zad`, `kod`, `radesh` (target ranks: base_value=64:18091, first_product=128:35183, bound_value=144:62243, second_product=288:40567, answer=276:111872)
- Layer 37: `zat`, ` Zad`, `cod`, `}<?`, ` zap` (target ranks: base_value=64:64532, first_product=128:50961, bound_value=144:107437, second_product=288:88499, answer=276:126590)
- Layer 38: `zat`, `zel`, ` z`, `𝑧`, `zor` (target ranks: base_value=64:75257, first_product=128:66376, bound_value=144:100830, second_product=288:87506, answer=276:124024)
- Layer 39: `zat`, ` z`, `𝑧`, `.z`, ` Zij` (target ranks: base_value=64:51397, first_product=128:48068, bound_value=144:91489, second_product=288:69669, answer=276:116482)
- Layer 40: ` z`, `zat`, ` diz`, `zij`, ` zad` (target ranks: base_value=64:12980, first_product=128:18613, bound_value=144:41419, second_product=288:28610, answer=276:101172)
- Layer 41: ` .`, ` diz`, ` first`, `zel`, `坏` (target ranks: base_value=64:1893, first_product=128:2274, bound_value=144:14432, second_product=288:4742, answer=276:26198)

### Filler position 24 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125806, first_product=128:124279, bound_value=144:122186, second_product=288:125741, answer=276:120962)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10995, first_product=128:21767, bound_value=144:28759, second_product=288:20919, answer=276:22805)
- Layer 20: `足`, ` smile`, `锁定`, `ait`, ` LS` (target ranks: base_value=64:8326, first_product=128:21729, bound_value=144:21792, second_product=288:33290, answer=276:38583)
- Layer 30: ` ignored`, ` ignoring`, `忽略`, `Ign`, ` ignore` (target ranks: base_value=64:15370, first_product=128:38472, bound_value=144:24671, second_product=288:41470, answer=276:92512)
- Layer 35: ` ignoring`, `询问`, ` v`, ` unused`, `重复` (target ranks: base_value=64:10706, first_product=128:23381, bound_value=144:27422, second_product=288:27418, answer=276:76497)
- Layer 36: `询问`, `忽略`, ` ignoring`, `失效`, `不急` (target ranks: base_value=64:15187, first_product=128:18755, bound_value=144:42258, second_product=288:26445, answer=276:78931)
- Layer 37: `不急`, ` medief`, `关切`, `观望`, `坏` (target ranks: base_value=64:60714, first_product=128:40354, bound_value=144:84309, second_product=288:64206, answer=276:115804)
- Layer 38: `不急`, ` unflagged`, ` medief`, `}<?`, ` irrelevant` (target ranks: base_value=64:55366, first_product=128:51188, bound_value=144:96425, second_product=288:62419, answer=276:116610)
- Layer 39: `殿堂`, ` medief`, `不急`, `}<?`, `迷惑` (target ranks: base_value=64:66251, first_product=128:50625, bound_value=144:104723, second_product=288:88464, answer=276:123609)
- Layer 40: `殿堂`, `不急`, `zat`, `坏`, `zij` (target ranks: base_value=64:39579, first_product=128:50064, bound_value=144:95733, second_product=288:86812, answer=276:123893)
- Layer 41: ` .`, `zij`, ` uninter`, `不急`, `矶` (target ranks: base_value=64:16021, first_product=128:28548, bound_value=144:73792, second_product=288:75091, answer=276:99046)

### Filler position 25 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126100, first_product=128:124497, bound_value=144:122577, second_product=288:125869, answer=276:121311)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11103, first_product=128:22823, bound_value=144:29293, second_product=288:21682, answer=276:23231)
- Layer 20: ` smile`, `锁定`, `足`, ` LS`, `ait` (target ranks: base_value=64:10656, first_product=128:25285, bound_value=144:26589, second_product=288:33159, answer=276:32634)
- Layer 30: `回答`, ` answer`, ` answers`, `Answer`, ` Answer` (target ranks: base_value=64:13308, first_product=128:44713, bound_value=144:32020, second_product=288:21273, answer=276:38424)
- Layer 35: `回答`, ` answer`, ` calculator`, ` repetition`, `Answer` (target ranks: base_value=64:9872, first_product=128:45826, bound_value=144:35460, second_product=288:20100, answer=276:48463)
- Layer 36: `回答`, `calcul`, ` answer`, ` calculator`, ` answers` (target ranks: base_value=64:15091, first_product=128:43470, bound_value=144:54201, second_product=288:18459, answer=276:49454)
- Layer 37: `calcul`, ` ответ`, ` answer`, `回答`, ` پاسخ` (target ranks: base_value=64:49905, first_product=128:80660, bound_value=144:95540, second_product=288:36105, answer=276:88021)
- Layer 38: `calcul`, ` calcul`, ` follow`, ` calculation`, `遵循` (target ranks: base_value=64:47552, first_product=128:77525, bound_value=144:99086, second_product=288:30189, answer=276:78791)
- Layer 39: `}<?`, ` RES`, ` Res`, `小女孩`, ` Resident` (target ranks: base_value=64:68943, first_product=128:70431, bound_value=144:111878, second_product=288:65716, answer=276:105979)
- Layer 40: ` talags`, `calcul`, ` Res`, ` follow`, `acl` (target ranks: base_value=64:33350, first_product=128:55518, bound_value=144:99169, second_product=288:39968, answer=276:85949)
- Layer 41: `因为这些`, ` just`, ` .`, `Answer`, `zij` (target ranks: base_value=64:14450, first_product=128:12848, bound_value=144:57613, second_product=288:25914, answer=276:30989)

### Filler position 26 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126252, first_product=128:124640, bound_value=144:122701, second_product=288:125991, answer=276:121306)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10825, first_product=128:22239, bound_value=144:28165, second_product=288:21639, answer=276:22726)
- Layer 20: `ait`, ` Walker`, `Walker`, `锁定`, `拆` (target ranks: base_value=64:8395, first_product=128:33836, bound_value=144:28480, second_product=288:40778, answer=276:46084)
- Layer 30: ` labor`, `vn`, `capt`, ` quadr`, ` dy` (target ranks: base_value=64:9467, first_product=128:70941, bound_value=144:70942, second_product=288:48035, answer=276:119155)
- Layer 35: ` labor`, `分解`, ` stabil`, ` v`, `锁定` (target ranks: base_value=64:11890, first_product=128:69610, bound_value=144:73934, second_product=288:42228, answer=276:112244)
- Layer 36: `分解`, ` stabil`, `留存`, ` equations`, ` tap` (target ranks: base_value=64:18150, first_product=128:55692, bound_value=144:88634, second_product=288:27721, answer=276:116749)
- Layer 37: `}<?`, `薇薇`, `yv`, `不加`, ` BV` (target ranks: base_value=64:65199, first_product=128:94039, bound_value=144:117850, second_product=288:60797, answer=276:125748)
- Layer 38: `}<?`, `zat`, `yv`, `不加`, `zv` (target ranks: base_value=64:73386, first_product=128:108330, bound_value=144:120345, second_product=288:65920, answer=276:125519)
- Layer 39: `yv`, `}<?`, `迷惑`, `zat`, `variables` (target ranks: base_value=64:59211, first_product=128:79858, bound_value=144:107490, second_product=288:59011, answer=276:124715)
- Layer 40: `Definitions`, ` definitions`, ` Definitions`, `zat`, `迷惑` (target ranks: base_value=64:23586, first_product=128:52014, bound_value=144:89527, second_product=288:38624, answer=276:120338)
- Layer 41: ` definitions`, `Define`, ` zad`, `zij`, ` Definitions` (target ranks: base_value=64:3429, first_product=128:10998, bound_value=144:45383, second_product=288:7923, answer=276:65455)

### Filler position 27 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126315, first_product=128:124613, bound_value=144:122673, second_product=288:125938, answer=276:121270)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10036, first_product=128:20538, bound_value=144:26618, second_product=288:20536, answer=276:21867)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `Walker` (target ranks: base_value=64:11013, first_product=128:32724, bound_value=144:27079, second_product=288:36510, answer=276:42069)
- Layer 30: ` labor`, ` calculator`, `acin`, `atan`, `鞍` (target ranks: base_value=64:3842, first_product=128:46062, bound_value=144:30252, second_product=288:36445, answer=276:83943)
- Layer 35: ` Tw`, ` labor`, `Tw`, ` reserved`, ` calculator` (target ranks: base_value=64:2678, first_product=128:25717, bound_value=144:20892, second_product=288:19562, answer=276:65864)
- Layer 36: `留存`, ` Tw`, `翻`, `adal`, `分解` (target ranks: base_value=64:2751, first_product=128:15578, bound_value=144:31098, second_product=288:15010, answer=276:80804)
- Layer 37: `}<?`, `翻`, `翻了`, ` Number`, `不加` (target ranks: base_value=64:12190, first_product=128:22460, bound_value=144:61319, second_product=288:32431, answer=276:108683)
- Layer 38: `zat`, `}<?`, `不加`, `zor`, `umber` (target ranks: base_value=64:11772, first_product=128:27630, bound_value=144:55709, second_product=288:28517, answer=276:100286)
- Layer 39: `zat`, ` Zahl`, ` Number`, `umber`, `zor` (target ranks: base_value=64:12131, first_product=128:25577, bound_value=144:56875, second_product=288:36416, answer=276:103598)
- Layer 40: `z`, ` z`, `zat`, ` Z`, `zor` (target ranks: base_value=64:1031, first_product=128:6972, bound_value=144:20950, second_product=288:5903, answer=276:76968)
- Layer 41: `z`, `zl`, ` `, `oz`, `acular` (target ranks: base_value=64:291, first_product=128:893, bound_value=144:9454, second_product=288:962, answer=276:15016)

### Filler position 28 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126592, first_product=128:125061, bound_value=144:123309, second_product=288:126371, answer=276:121917)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:10269, first_product=128:20637, bound_value=144:27274, second_product=288:20747, answer=276:22389)
- Layer 20: `能被`, `拆`, `ait`, ` engaging`, ` Walker` (target ranks: base_value=64:7211, first_product=128:36934, bound_value=144:23662, second_product=288:39377, answer=276:45343)
- Layer 30: `64`, `分解`, ` Intel`, `算出`, ` sixty` (target ranks: base_value=64:1, first_product=128:68, bound_value=144:666, second_product=288:1578, answer=276:74655)
- Layer 35: `64`, `分解`, ` dual`, ` calculator`, ` decompose` (target ranks: base_value=64:1, first_product=128:30, bound_value=144:145, second_product=288:345, answer=276:55301)
- Layer 36: `分解`, `翻`, ` decom`, ` dual`, `calcul` (target ranks: base_value=64:6, first_product=128:53, bound_value=144:1029, second_product=288:538, answer=276:76561)
- Layer 37: `}<?`, ` doubling`, `翻了`, `dividers`, ` doubles` (target ranks: base_value=64:30, first_product=128:136, bound_value=144:4533, second_product=288:6432, answer=276:107801)
- Layer 38: `}<?`, ` doubling`, `覆`, `殿堂`, `ocyst` (target ranks: base_value=64:199, first_product=128:2033, bound_value=144:19954, second_product=288:26550, answer=276:112915)
- Layer 39: `}<?`, `覆`, `ocyst`, `殿堂`, ` dirty` (target ranks: base_value=64:3055, first_product=128:10457, bound_value=144:45769, second_product=288:32418, answer=276:112182)
- Layer 40: ` Tw`, ` diz`, ` decom`, ` twisted`, ` drip` (target ranks: base_value=64:10379, first_product=128:7173, bound_value=144:32980, second_product=288:3140, answer=276:78454)
- Layer 41: `z`, ` diz`, `zij`, `zel`, ` ` (target ranks: base_value=64:3761, first_product=128:1190, bound_value=144:23849, second_product=288:1863, answer=276:34246)

### Filler position 29 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126457, first_product=128:124928, bound_value=144:123183, second_product=288:126279, answer=276:121697)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:10653, first_product=128:21029, bound_value=144:28271, second_product=288:21115, answer=276:22883)
- Layer 20: `能被`, `锁定`, `ait`, `ession`, `啦啦` (target ranks: base_value=64:10971, first_product=128:33463, bound_value=144:24143, second_product=288:50444, answer=276:55982)
- Layer 30: ` v`, `�`, `闲置`, `v`, ` reserved` (target ranks: base_value=64:10639, first_product=128:32678, bound_value=144:24499, second_product=288:34003, answer=276:87533)
- Layer 35: ` reserved`, `锁定`, ` v`, `分解`, ` tap` (target ranks: base_value=64:10975, first_product=128:26643, bound_value=144:22487, second_product=288:28907, answer=276:79196)
- Layer 36: ` reserved`, `留存`, ` tap`, `分解`, `俯` (target ranks: base_value=64:15270, first_product=128:24061, bound_value=144:27646, second_product=288:30799, answer=276:95519)
- Layer 37: `radesh`, `}<?`, `坏`, `冰冰`, `俯` (target ranks: base_value=64:42931, first_product=128:41080, bound_value=144:45163, second_product=288:50436, answer=276:114523)
- Layer 38: `坏`, `zat`, `radesh`, `迷惑`, `冰冰` (target ranks: base_value=64:31567, first_product=128:38838, bound_value=144:51630, second_product=288:48069, answer=276:108569)
- Layer 39: `}<?`, `坏`, `<｜begin▁of▁sentence｜>`, `迷惑`, `坏的` (target ranks: base_value=64:57328, first_product=128:63499, bound_value=144:80048, second_product=288:88084, answer=276:123750)
- Layer 40: `坏`, `坏的`, `殿堂`, `冰冰`, `坏了` (target ranks: base_value=64:20424, first_product=128:48886, bound_value=144:60943, second_product=288:73604, answer=276:122341)
- Layer 41: `坏`, ` .`, `没有被`, `从前`, ` ` (target ranks: base_value=64:5316, first_product=128:13295, bound_value=144:29796, second_product=288:52233, answer=276:94713)

### Filler position 30 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126620, first_product=128:125130, bound_value=144:123380, second_product=288:126440, answer=276:121964)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9905, first_product=128:19978, bound_value=144:27155, second_product=288:20465, answer=276:22664)
- Layer 20: `atile`, `锁定`, ` LS`, ` smile`, `cape` (target ranks: base_value=64:6039, first_product=128:19193, bound_value=144:22287, second_product=288:34530, answer=276:44020)
- Layer 30: ` Zad`, ` zad`, ` Zan`, ` Bax`, ` fab` (target ranks: base_value=64:31658, first_product=128:116964, bound_value=144:103318, second_product=288:87168, answer=276:119777)
- Layer 35: ` fab`, ` Rot`, `Rot`, ` tap`, `Tap` (target ranks: base_value=64:38887, first_product=128:101133, bound_value=144:70186, second_product=288:32637, answer=276:103716)
- Layer 36: ` riv`, ` zad`, ` tap`, ` Bax`, ` fab` (target ranks: base_value=64:24921, first_product=128:69876, bound_value=144:56572, second_product=288:14515, answer=276:88498)
- Layer 37: ` mim`, `amol`, ` Bev`, ` zad`, `cov` (target ranks: base_value=64:72885, first_product=128:96566, bound_value=144:77098, second_product=288:26257, answer=276:110207)
- Layer 38: `本题分析`, `zat`, `疑惑`, `ked`, `gev` (target ranks: base_value=64:87692, first_product=128:114548, bound_value=144:100279, second_product=288:54202, answer=276:121224)
- Layer 39: ` Nij`, `本题分析`, `ked`, `zat`, `斐` (target ranks: base_value=64:62139, first_product=128:105948, bound_value=144:72717, second_product=288:36922, answer=276:105290)
- Layer 40: `y`, `zel`, `zat`, `zij`, ` Nij` (target ranks: base_value=64:40847, first_product=128:80117, bound_value=144:59923, second_product=288:20197, answer=276:103174)
- Layer 41: `zel`, `zij`, ` mim`, `坏的`, `坏` (target ranks: base_value=64:15075, first_product=128:14180, bound_value=144:26076, second_product=288:5581, answer=276:22543)

### Filler position 31 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126529, first_product=128:125194, bound_value=144:123458, second_product=288:126547, answer=276:122044)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9259, first_product=128:18935, bound_value=144:25995, second_product=288:19789, answer=276:21799)
- Layer 20: `锁定`, `ait`, ` smile`, `鞍`, ` LS` (target ranks: base_value=64:7743, first_product=128:18688, bound_value=144:21505, second_product=288:29733, answer=276:33594)
- Layer 30: ` answer`, `回答`, ` Answer`, `答案`, `鞍` (target ranks: base_value=64:1774, first_product=128:34083, bound_value=144:21283, second_product=288:10268, answer=276:33968)
- Layer 35: ` tap`, `鞍`, ` answer`, `calcul`, ` Respons` (target ranks: base_value=64:1787, first_product=128:12410, bound_value=144:5707, second_product=288:1948, answer=276:14236)
- Layer 36: `calcul`, ` stabil`, `acin`, ` tap`, `鞍` (target ranks: base_value=64:2740, first_product=128:7614, bound_value=144:9931, second_product=288:2024, answer=276:16176)
- Layer 37: `}<?`, ` rational`, ` Reson`, ` reson`, `calcul` (target ranks: base_value=64:20952, first_product=128:18980, bound_value=144:25537, second_product=288:1334, answer=276:4796)
- Layer 38: `}<?`, ` RES`, ` Reson`, `ocyst`, `acons` (target ranks: base_value=64:46080, first_product=128:31535, bound_value=144:34127, second_product=288:2352, answer=276:7336)
- Layer 39: `}<?`, `ocyst`, `hatic`, `-ulo`, `opters` (target ranks: base_value=64:91328, first_product=128:94367, bound_value=144:95619, second_product=288:6593, answer=276:5795)
- Layer 40: `acular`, `坏`, `acl`, `坏的`, `坏了` (target ranks: base_value=64:68526, first_product=128:101778, bound_value=144:96664, second_product=288:822, answer=276:342)
- Layer 41: `zion`, `acular`, `步骤如下`, `Answer`, `zel` (target ranks: base_value=64:33324, first_product=128:51119, bound_value=144:55530, second_product=288:713, answer=276:92)

### Filler position 32 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126641, first_product=128:125224, bound_value=144:123561, second_product=288:126565, answer=276:122132)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9166, first_product=128:18753, bound_value=144:25855, second_product=288:20154, answer=276:21025)
- Layer 20: ` ES`, ` engaging`, `距`, ` Walker`, ` LS` (target ranks: base_value=64:8288, first_product=128:18944, bound_value=144:24764, second_product=288:31537, answer=276:37881)
- Layer 30: ` Ries`, `EDER`, `eder`, ` basal`, ` ES` (target ranks: base_value=64:1001, first_product=128:8681, bound_value=144:1035, second_product=288:39, answer=276:10721)
- Layer 35: `292`, `280`, `282`, `296`, `286` (target ranks: base_value=64:11889, first_product=128:42814, bound_value=144:18644, second_product=288:6, answer=276:22)
- Layer 36: `280`, `292`, `279`, `282`, `281` (target ranks: base_value=64:45585, first_product=128:17372, bound_value=144:20318, second_product=288:17, answer=276:11)
- Layer 37: `280`, `292`, `279`, `282`, `枝条` (target ranks: base_value=64:110500, first_product=128:38774, bound_value=144:52891, second_product=288:13, answer=276:17)
- Layer 38: `280`, `292`, `279`, `282`, `276` (target ranks: base_value=64:110307, first_product=128:73254, bound_value=144:67976, second_product=288:33, answer=276:5)
- Layer 39: `280`, `枝条`, `268`, `�`, `ULO` (target ranks: base_value=64:110792, first_product=128:117855, bound_value=144:121954, second_product=288:5638, answer=276:18)
- Layer 40: `asking`, ` basal`, ` view`, `268`, ` Dirty` (target ranks: base_value=64:117884, first_product=128:112756, bound_value=144:119600, second_product=288:575, answer=276:22)
- Layer 41: `................................................`, ` dekameters`, `zion`, `有的时候`, `..........................................` (target ranks: base_value=64:105466, first_product=128:77130, bound_value=144:103496, second_product=288:1512, answer=276:34)

### Filler position 33 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:126946, first_product=128:125698, bound_value=144:124145, second_product=288:126957, answer=276:122564)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:8856, first_product=128:19065, bound_value=144:25573, second_product=288:20389, answer=276:20724)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` LS` (target ranks: base_value=64:7776, first_product=128:20280, bound_value=144:21602, second_product=288:32458, answer=276:41821)
- Layer 30: ` diz`, ` Dice`, ` dice`, ` Dian`, ` Dib` (target ranks: base_value=64:85, first_product=128:59536, bound_value=144:45599, second_product=288:55404, answer=276:125490)
- Layer 35: ` diz`, ` dip`, ` dio`, ` Dib`, ` Dio` (target ranks: base_value=64:23, first_product=128:29634, bound_value=144:18980, second_product=288:27583, answer=276:106471)
- Layer 36: ` diz`, `留存`, ` dio`, ` Dio`, ` dice` (target ranks: base_value=64:26, first_product=128:19370, bound_value=144:32571, second_product=288:22497, answer=276:112426)
- Layer 37: ` diz`, `}<?`, `迷惑`, `niz`, ` Dio` (target ranks: base_value=64:164, first_product=128:46668, bound_value=144:55568, second_product=288:51301, answer=276:121957)
- Layer 38: ` diz`, `}<?`, `迷惑`, `zat`, ` Dio` (target ranks: base_value=64:779, first_product=128:73602, bound_value=144:71431, second_product=288:69073, answer=276:121351)
- Layer 39: `迷惑`, `}<?`, ` diz`, `niz`, `本题分析` (target ranks: base_value=64:18706, first_product=128:66224, bound_value=144:67914, second_product=288:39246, answer=276:110446)
- Layer 40: ` diz`, `迷惑`, `amic`, `zij`, ` compounding` (target ranks: base_value=64:3048, first_product=128:19106, bound_value=144:25434, second_product=288:3919, answer=276:57144)
- Layer 41: ` diz`, ` .`, `zij`, `迷惑`, ` ` (target ranks: base_value=64:1548, first_product=128:9865, bound_value=144:10806, second_product=288:1338, answer=276:16145)

### Filler position 34 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:126985, first_product=128:125754, bound_value=144:124180, second_product=288:126937, answer=276:122596)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9262, first_product=128:19615, bound_value=144:25798, second_product=288:20453, answer=276:20736)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` smile` (target ranks: base_value=64:10897, first_product=128:33339, bound_value=144:24892, second_product=288:40751, answer=276:51751)
- Layer 30: ` ز`, `acin`, ` z`, ` Z`, ` zad` (target ranks: base_value=64:18019, first_product=128:88384, bound_value=144:45904, second_product=288:75227, answer=276:122110)
- Layer 35: ` z`, ` ز`, `zag`, ` reserved`, ` Z` (target ranks: base_value=64:12686, first_product=128:69783, bound_value=144:39979, second_product=288:69417, answer=276:113592)
- Layer 36: ` z`, `留存`, ` zad`, `zag`, ` Zad` (target ranks: base_value=64:19862, first_product=128:57063, bound_value=144:48752, second_product=288:65234, answer=276:116867)
- Layer 37: `zat`, ` z`, `}<?`, `zas`, ` Zad` (target ranks: base_value=64:65542, first_product=128:88467, bound_value=144:89215, second_product=288:97123, answer=276:126736)
- Layer 38: `zat`, ` z`, `zij`, `取样`, `取舍` (target ranks: base_value=64:61837, first_product=128:103290, bound_value=144:86760, second_product=288:92539, answer=276:123020)
- Layer 39: `zat`, ` z`, `zij`, ` Zij`, `zv` (target ranks: base_value=64:37813, first_product=128:86066, bound_value=144:78346, second_product=288:77868, answer=276:119597)
- Layer 40: ` z`, `zij`, ` diz`, `zat`, `z` (target ranks: base_value=64:11222, first_product=128:55567, bound_value=144:57223, second_product=288:49313, answer=276:116897)
- Layer 41: ` diz`, `zij`, `zel`, `zion`, `z` (target ranks: base_value=64:2440, first_product=128:19334, bound_value=144:36151, second_product=288:28118, answer=276:77295)

### Filler position 35 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:126990, first_product=128:125881, bound_value=144:124355, second_product=288:127035, answer=276:122687)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10572, first_product=128:20535, bound_value=144:27185, second_product=288:21051, answer=276:21759)
- Layer 20: `ait`, ` smile`, `足`, `幽`, `能被` (target ranks: base_value=64:2920, first_product=128:12618, bound_value=144:13685, second_product=288:22433, answer=276:19559)
- Layer 30: `328`, `油箱`, `296`, `68`, `EDER` (target ranks: base_value=64:3185, first_product=128:420, bound_value=144:232, second_product=288:69, answer=276:84)
- Layer 35: `288`, `268`, `289`, `286`, `278` (target ranks: base_value=64:13180, first_product=128:7818, bound_value=144:26701, second_product=288:1, answer=276:9)
- Layer 36: `276`, `268`, `278`, `376`, `267` (target ranks: base_value=64:27157, first_product=128:3132, bound_value=144:71972, second_product=288:9, answer=276:1)
- Layer 37: `276`, `268`, `278`, `267`, `288` (target ranks: base_value=64:59196, first_product=128:6985, bound_value=144:75942, second_product=288:5, answer=276:1)
- Layer 38: `276`, `268`, `260`, `274`, `266` (target ranks: base_value=64:75200, first_product=128:32189, bound_value=144:98135, second_product=288:20, answer=276:1)
- Layer 39: `276`, `277`, `268`, `278`, `-ulo` (target ranks: base_value=64:117987, first_product=128:119031, bound_value=144:127580, second_product=288:88, answer=276:1)
- Layer 40: `276`, `278`, `277`, `268`, `274` (target ranks: base_value=64:121644, first_product=128:107141, bound_value=144:126572, second_product=288:15, answer=276:1)
- Layer 41: `276`, ` nuest`, `zetek`, `zion`, `zel` (target ranks: base_value=64:94340, first_product=128:109161, bound_value=144:124197, second_product=288:2076, answer=276:1)

### Filler position 36 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127094, first_product=128:126026, bound_value=144:124600, second_product=288:127200, answer=276:122952)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11674, first_product=128:21843, bound_value=144:29609, second_product=288:22265, answer=276:23270)
- Layer 20: `能被`, ` engaging`, `ait`, ` Engaging`, `距` (target ranks: base_value=64:15719, first_product=128:36526, bound_value=144:40572, second_product=288:49043, answer=276:51064)
- Layer 30: `290`, `328`, `286`, `292`, `296` (target ranks: base_value=64:16461, first_product=128:3487, bound_value=144:3312, second_product=288:12, answer=276:869)
- Layer 35: `288`, `289`, `290`, `287`, `268` (target ranks: base_value=64:58094, first_product=128:15182, bound_value=144:63918, second_product=288:1, answer=276:109)
- Layer 36: `276`, `376`, `278`, `277`, `288` (target ranks: base_value=64:106576, first_product=128:1535, bound_value=144:109036, second_product=288:5, answer=276:1)
- Layer 37: `276`, `278`, `376`, `277`, `288` (target ranks: base_value=64:120574, first_product=128:3193, bound_value=144:108802, second_product=288:5, answer=276:1)
- Layer 38: `276`, `278`, `277`, `376`, `275` (target ranks: base_value=64:122135, first_product=128:18036, bound_value=144:124055, second_product=288:39, answer=276:1)
- Layer 39: `276`, `278`, `277`, `476`, `076` (target ranks: base_value=64:124603, first_product=128:114673, bound_value=144:128145, second_product=288:2518, answer=276:1)
- Layer 40: `276`, `278`, `277`, `�`, ` elev` (target ranks: base_value=64:126535, first_product=128:100206, bound_value=144:128017, second_product=288:462, answer=276:1)
- Layer 41: `276`, `278`, ` nuest`, `zion`, `277` (target ranks: base_value=64:112929, first_product=128:82156, bound_value=144:125646, second_product=288:6311, answer=276:1)

### Filler position 37 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=64:127068, first_product=128:125896, bound_value=144:124450, second_product=288:126995, answer=276:122895)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11603, first_product=128:22480, bound_value=144:30288, second_product=288:22769, answer=276:24159)
- Layer 20: ` engaging`, `能被`, `ätte`, `ait`, `sl` (target ranks: base_value=64:19958, first_product=128:57541, bound_value=144:44843, second_product=288:74620, answer=276:73829)
- Layer 30: `coding`, `cod`, `code`, `忽略`, ` coding` (target ranks: base_value=64:17556, first_product=128:61465, bound_value=144:57130, second_product=288:68519, answer=276:113426)
- Layer 35: `coding`, `cod`, `code`, `忽略`, `重复` (target ranks: base_value=64:15351, first_product=128:53532, bound_value=144:57176, second_product=288:58769, answer=276:112525)
- Layer 36: `忽略`, `留存`, `重复`, `coding`, `cod` (target ranks: base_value=64:13799, first_product=128:36656, bound_value=144:60958, second_product=288:55428, answer=276:109664)
- Layer 37: `}<?`, `不急`, `radesh`, `坏`, `用了` (target ranks: base_value=64:66789, first_product=128:78327, bound_value=144:102391, second_product=288:106258, answer=276:126468)
- Layer 38: `}<?`, `zat`, `不急`, `radesh`, `坏` (target ranks: base_value=64:42603, first_product=128:74833, bound_value=144:106034, second_product=288:103471, answer=276:124738)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `�乐`, `ocyst`, `语言文字` (target ranks: base_value=64:43115, first_product=128:51231, bound_value=144:94763, second_product=288:92186, answer=276:117165)
- Layer 40: `acular`, `坏`, ` Tw`, ` nasod`, `坏了` (target ranks: base_value=64:6876, first_product=128:20845, bound_value=144:57414, second_product=288:50104, answer=276:85770)
- Layer 41: ` .`, ` `, `<｜end▁of▁sentence｜>`, ` because`, `等待` (target ranks: base_value=64:1265, first_product=128:3046, bound_value=144:22719, second_product=288:11958, answer=276:15933)

### Filler position 38 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127119, first_product=128:126028, bound_value=144:124592, second_product=288:127069, answer=276:123033)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10557, first_product=128:21304, bound_value=144:29028, second_product=288:21662, answer=276:23150)
- Layer 20: `ait`, `忑`, ` engaging`, `能被`, ` Walker` (target ranks: base_value=64:16823, first_product=128:40445, bound_value=144:35920, second_product=288:60271, answer=276:60320)
- Layer 30: `coding`, ` dy`, `zilla`, `acic`, `sl` (target ranks: base_value=64:8786, first_product=128:69493, bound_value=144:65591, second_product=288:83757, answer=276:118026)
- Layer 35: ` dio`, ` dip`, ` dy`, `留存`, `分解` (target ranks: base_value=64:10525, first_product=128:58624, bound_value=144:61776, second_product=288:71422, answer=276:116849)
- Layer 36: `留存`, ` zad`, `翻`, ` stabil`, ` dio` (target ranks: base_value=64:10563, first_product=128:31236, bound_value=144:59135, second_product=288:54085, answer=276:115773)
- Layer 37: `}<?`, `留存`, `迷惑`, `翻了`, `翻` (target ranks: base_value=64:40974, first_product=128:51686, bound_value=144:86440, second_product=288:85852, answer=276:125439)
- Layer 38: `}<?`, `zat`, `迷惑`, ` sublim`, `dividers` (target ranks: base_value=64:40142, first_product=128:61929, bound_value=144:99596, second_product=288:90855, answer=276:123106)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `迷惑`, `覆`, `hemer` (target ranks: base_value=64:53140, first_product=128:55656, bound_value=144:100388, second_product=288:92737, answer=276:120705)
- Layer 40: `acular`, `冰冰`, `留存`, `下沉`, `等待着` (target ranks: base_value=64:15717, first_product=128:27168, bound_value=144:77453, second_product=288:63809, answer=276:86923)
- Layer 41: `acular`, `从前`, ` `, ` .`, `没有被` (target ranks: base_value=64:1697, first_product=128:1997, bound_value=144:20474, second_product=288:10273, answer=276:14041)

### Filler position 39 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127296, first_product=128:126172, bound_value=144:124758, second_product=288:127146, answer=276:123053)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10272, first_product=128:20102, bound_value=144:28143, second_product=288:21562, answer=276:22488)
- Layer 20: `ait`, `锁定`, ` Walker`, ` smile`, ` ES` (target ranks: base_value=64:5625, first_product=128:18180, bound_value=144:17043, second_product=288:27763, answer=276:29092)
- Layer 30: `subt`, `292`, `328`, `Subt`, `286` (target ranks: base_value=64:2894, first_product=128:1362, bound_value=144:764, second_product=288:167, answer=276:162)
- Layer 35: `268`, `292`, `276`, `264`, `260` (target ranks: base_value=64:7914, first_product=128:16200, bound_value=144:16099, second_product=288:14, answer=276:3)
- Layer 36: `268`, `260`, `284`, `276`, `266` (target ranks: base_value=64:20165, first_product=128:5370, bound_value=144:24456, second_product=288:22, answer=276:4)
- Layer 37: `268`, `}<?`, `urin`, `?datasetId`, `叶子` (target ranks: base_value=64:79001, first_product=128:26678, bound_value=144:56181, second_product=288:44, answer=276:7)
- Layer 38: `268`, `桃子`, `}<?`, `urin`, `260` (target ranks: base_value=64:105363, first_product=128:60767, bound_value=144:72096, second_product=288:291, answer=276:6)
- Layer 39: `276`, `268`, `桃子`, `iota`, `tanle` (target ranks: base_value=64:113520, first_product=128:114536, bound_value=144:103135, second_product=288:4516, answer=276:1)
- Layer 40: `ess`, `acular`, `dividers`, `留存`, `观的` (target ranks: base_value=64:117573, first_product=128:119474, bound_value=144:118411, second_product=288:3238, answer=276:7)
- Layer 41: `276`, `zl`, `zion`, `268`, `266` (target ranks: base_value=64:72033, first_product=128:91020, bound_value=144:82273, second_product=288:901, answer=276:1)

### Filler position 40 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127217, first_product=128:126082, bound_value=144:124666, second_product=288:127150, answer=276:122969)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11077, first_product=128:20912, bound_value=144:29236, second_product=288:22172, answer=276:22873)
- Layer 20: `能被`, `ait`, ` LS`, `鞍`, `ätte` (target ranks: base_value=64:4091, first_product=128:18936, bound_value=144:19654, second_product=288:35346, answer=276:33026)
- Layer 30: `328`, `292`, `二十八`, `68`, `EDER` (target ranks: base_value=64:4417, first_product=128:691, bound_value=144:1869, second_product=288:42, answer=276:341)
- Layer 35: `288`, `289`, `287`, `268`, `286` (target ranks: base_value=64:29795, first_product=128:1304, bound_value=144:27444, second_product=288:1, answer=276:32)
- Layer 36: `276`, `278`, `268`, `277`, `376` (target ranks: base_value=64:92209, first_product=128:2976, bound_value=144:99754, second_product=288:6, answer=276:1)
- Layer 37: `276`, `278`, `268`, `376`, `277` (target ranks: base_value=64:112280, first_product=128:7708, bound_value=144:97143, second_product=288:6, answer=276:1)
- Layer 38: `276`, `277`, `275`, `274`, `278` (target ranks: base_value=64:120032, first_product=128:60780, bound_value=144:119539, second_product=288:19, answer=276:1)
- Layer 39: `276`, `277`, `278`, `275`, `476` (target ranks: base_value=64:126358, first_product=128:122628, bound_value=144:127813, second_product=288:1451, answer=276:1)
- Layer 40: `276`, `277`, `pek`, `278`, `实在` (target ranks: base_value=64:127696, first_product=128:119345, bound_value=144:128055, second_product=288:352, answer=276:1)
- Layer 41: `276`, ` nuest`, `................................................`, `))))`, `换句话说` (target ranks: base_value=64:106107, first_product=128:96729, bound_value=144:123796, second_product=288:3011, answer=276:1)

### Filler position 41 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127232, first_product=128:126194, bound_value=144:124746, second_product=288:127199, answer=276:123028)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11077, first_product=128:21141, bound_value=144:28750, second_product=288:22049, answer=276:22209)
- Layer 20: `能被`, ` LS`, `LS`, `锁定`, `ait` (target ranks: base_value=64:5144, first_product=128:16795, bound_value=144:17322, second_product=288:25937, answer=276:31034)
- Layer 30: `288`, `144`, `88`, ` stretched`, `退` (target ranks: base_value=64:293, first_product=128:362, bound_value=144:2, second_product=288:1, answer=276:18510)
- Layer 35: `288`, `289`, `287`, `286`, `290` (target ranks: base_value=64:22813, first_product=128:11904, bound_value=144:548, second_product=288:1, answer=276:1774)
- Layer 36: `288`, `289`, `287`, `286`, `290` (target ranks: base_value=64:105969, first_product=128:20175, bound_value=144:14515, second_product=288:1, answer=276:6208)
- Layer 37: `288`, `287`, `289`, `286`, `290` (target ranks: base_value=64:123078, first_product=128:29595, bound_value=144:33637, second_product=288:1, answer=276:11651)
- Layer 38: `288`, `287`, `289`, `286`, `蟠` (target ranks: base_value=64:124997, first_product=128:69372, bound_value=144:57294, second_product=288:1, answer=276:14794)
- Layer 39: `288`, `287`, `289`, `麝`, `ULO` (target ranks: base_value=64:121703, first_product=128:111566, bound_value=144:99242, second_product=288:1, answer=276:14941)
- Layer 40: `288`, `289`, `287`, ` loose`, ` twisted` (target ranks: base_value=64:110154, first_product=128:88493, bound_value=144:109817, second_product=288:1, answer=276:32)
- Layer 41: `288`, ` .`, `287`, `zion`, ` waiting` (target ranks: base_value=64:92641, first_product=128:76299, bound_value=144:94253, second_product=288:1, answer=276:73)

### Filler position 42 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127251, first_product=128:126257, bound_value=144:124838, second_product=288:127338, answer=276:123122)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11906, first_product=128:21857, bound_value=144:29684, second_product=288:22728, answer=276:22649)
- Layer 20: `鞍`, `锁定`, `cape`, `能被`, `ession` (target ranks: base_value=64:10372, first_product=128:19389, bound_value=144:25175, second_product=288:27088, answer=276:23717)
- Layer 30: `iab`, ` basal`, `acos`, `二十八`, `EDER` (target ranks: base_value=64:26504, first_product=128:21948, bound_value=144:33084, second_product=288:2353, answer=276:6215)
- Layer 35: `院内`, ` reper`, ` dunay`, ` EC`, `setting` (target ranks: base_value=64:33942, first_product=128:20972, bound_value=144:37326, second_product=288:20, answer=276:764)
- Layer 36: `院内`, `宫内`, `setting`, `otechnical`, `rounded` (target ranks: base_value=64:47021, first_product=128:6777, bound_value=144:58201, second_product=288:501, answer=276:72)
- Layer 37: `宫内`, `院内`, `rounded`, `polar`, `}<?` (target ranks: base_value=64:91730, first_product=128:11662, bound_value=144:51487, second_product=288:4287, answer=276:1776)
- Layer 38: `院内`, `本题分析`, `宫内`, `rounded`, ` Fro` (target ranks: base_value=64:92059, first_product=128:5641, bound_value=144:46689, second_product=288:4309, answer=276:145)
- Layer 39: `276`, `本题分析`, `268`, `-ulo`, `278` (target ranks: base_value=64:124793, first_product=128:80430, bound_value=144:116697, second_product=288:386, answer=276:1)
- Layer 40: `276`, `acular`, `268`, `坏`, `278` (target ranks: base_value=64:123663, first_product=128:68462, bound_value=144:114229, second_product=288:175, answer=276:1)
- Layer 41: ` .`, `276`, ` because`, `278`, ` ` (target ranks: base_value=64:98864, first_product=128:50904, bound_value=144:80582, second_product=288:526, answer=276:2)

### Filler position 43 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127138, first_product=128:126011, bound_value=144:124429, second_product=288:127126, answer=276:122810)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11397, first_product=128:21393, bound_value=144:29429, second_product=288:22638, answer=276:22552)
- Layer 20: `LS`, ` LS`, ` smile`, `锁定`, `距` (target ranks: base_value=64:6477, first_product=128:14347, bound_value=144:22879, second_product=288:25718, answer=276:26970)
- Layer 30: `64`, `退出`, ` mun`, `裕`, ` eighty` (target ranks: base_value=64:1, first_product=128:6, bound_value=144:17, second_product=288:32, answer=276:27926)
- Layer 35: `144`, `radesh`, `288`, `ukiran`, `二十八` (target ranks: base_value=64:43, first_product=128:45, bound_value=144:1, second_product=288:3, answer=276:7770)
- Layer 36: `144`, `radesh`, `288`, `�`, `往外` (target ranks: base_value=64:1452, first_product=128:21, bound_value=144:1, second_product=288:3, answer=276:17744)
- Layer 37: `144`, `radesh`, `联通`, `-ulo`, ` medief` (target ranks: base_value=64:8862, first_product=128:76, bound_value=144:1, second_product=288:38, answer=276:65675)
- Layer 38: `144`, `radesh`, `桃子`, `师徒`, `-ulo` (target ranks: base_value=64:35426, first_product=128:261, bound_value=144:1, second_product=288:252, answer=276:82233)
- Layer 39: `144`, `桃子`, `-ulo`, `�`, ` Goss` (target ranks: base_value=64:65045, first_product=128:8169, bound_value=144:1, second_product=288:104, answer=276:24335)
- Layer 40: ` loose`, ` twisted`, `院内`, ` twist`, `288` (target ranks: base_value=64:39933, first_product=128:15189, bound_value=144:8, second_product=288:5, answer=276:94)
- Layer 41: ` .`, `zion`, `院内`, ` because`, `278` (target ranks: base_value=64:31902, first_product=128:8433, bound_value=144:47, second_product=288:10, answer=276:13)

### Filler position 44 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127257, first_product=128:126150, bound_value=144:124825, second_product=288:127295, answer=276:123251)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11967, first_product=128:21431, bound_value=144:29846, second_product=288:23130, answer=276:23248)
- Layer 20: `能被`, `锁定`, `ait`, ` ES`, `距` (target ranks: base_value=64:8347, first_product=128:17394, bound_value=144:25956, second_product=288:35088, answer=276:36890)
- Layer 30: `64`, ` sixty`, `算出`, ` seventy`, ` Sixty` (target ranks: base_value=64:1, first_product=128:38, bound_value=144:2237, second_product=288:11661, answer=276:79644)
- Layer 35: `64`, ` twice`, `算出`, ` calculator`, ` double` (target ranks: base_value=64:1, first_product=128:2549, bound_value=144:1773, second_product=288:4243, answer=276:61097)
- Layer 36: `翻`, `64`, ` stabil`, ` Tw`, `翻了` (target ranks: base_value=64:2, first_product=128:1478, bound_value=144:5617, second_product=288:3716, answer=276:55584)
- Layer 37: `}<?`, `翻了`, `dividers`, ` doubling`, ` doubles` (target ranks: base_value=64:349, first_product=128:10037, bound_value=144:18353, second_product=288:28320, answer=276:101995)
- Layer 38: `}<?`, ` doubling`, `polar`, `osit`, `dividers` (target ranks: base_value=64:852, first_product=128:19152, bound_value=144:36693, second_product=288:38386, answer=276:103943)
- Layer 39: `}<?`, `urin`, `ounder`, `polar`, `-ulo` (target ranks: base_value=64:13825, first_product=128:27707, bound_value=144:53360, second_product=288:6295, answer=276:22852)
- Layer 40: ` Tw`, ` twist`, ` diz`, ` `, `izk` (target ranks: base_value=64:16156, first_product=128:19870, bound_value=144:36163, second_product=288:120, answer=276:47)
- Layer 41: ` .`, `276`, ` `, `278`, `282` (target ranks: base_value=64:4679, first_product=128:2804, bound_value=144:7484, second_product=288:21, answer=276:2)

### Filler position 45 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127403, first_product=128:126365, bound_value=144:125071, second_product=288:127455, answer=276:123470)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11447, first_product=128:20855, bound_value=144:28548, second_product=288:22465, answer=276:22512)
- Layer 20: `ait`, ` Walker`, `妇`, `会成为`, ` engaging` (target ranks: base_value=64:18610, first_product=128:31688, bound_value=144:33760, second_product=288:52779, answer=276:51676)
- Layer 30: ` Dian`, ` diz`, ` Diam`, ` Diet`, `备` (target ranks: base_value=64:17317, first_product=128:103961, bound_value=144:102106, second_product=288:108350, answer=276:127852)
- Layer 35: ` diz`, ` Dian`, ` dich`, ` Tw`, ` dy` (target ranks: base_value=64:7905, first_product=128:94752, bound_value=144:77130, second_product=288:105297, answer=276:123924)
- Layer 36: `留存`, ` Dian`, ` diz`, `otas`, ` dich` (target ranks: base_value=64:7478, first_product=128:51411, bound_value=144:76610, second_product=288:84708, answer=276:115705)
- Layer 37: `}<?`, ` diz`, `翻了`, `acos`, `otan` (target ranks: base_value=64:24137, first_product=128:76419, bound_value=144:100601, second_product=288:108092, answer=276:123673)
- Layer 38: ` diz`, `zat`, `迷惑`, `}<?`, `ertz` (target ranks: base_value=64:15950, first_product=128:87212, bound_value=144:103899, second_product=288:104621, answer=276:118586)
- Layer 39: `迷惑`, `oug`, `文字的`, `打磨`, `淤泥` (target ranks: base_value=64:29818, first_product=128:47634, bound_value=144:72209, second_product=288:39615, answer=276:54261)
- Layer 40: ` Tw`, `迷惑`, `留存`, `oug`, `anin` (target ranks: base_value=64:3796, first_product=128:9841, bound_value=144:38430, second_product=288:7952, answer=276:2122)
- Layer 41: ` `, ` .`, `<｜end▁of▁sentence｜>`, `.,`, `####` (target ranks: base_value=64:828, first_product=128:1180, bound_value=144:12713, second_product=288:822, answer=276:60)

### Filler position 46 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=64:127343, first_product=128:126431, bound_value=144:125204, second_product=288:127579, answer=276:123547)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11210, first_product=128:20651, bound_value=144:28272, second_product=288:21647, answer=276:22371)
- Layer 20: `平行`, `俯`, ` adtong`, ` spac`, `school` (target ranks: base_value=64:63838, first_product=128:79795, bound_value=144:78605, second_product=288:103467, answer=276:86796)
- Layer 30: `?datasetId`, `}using`, ` spac`, `dividers`, `}<?` (target ranks: base_value=64:104106, first_product=128:89203, bound_value=144:98274, second_product=288:115879, answer=276:122668)
- Layer 35: `}using`, `俯`, `ovel`, `足足`, `坏` (target ranks: base_value=64:83176, first_product=128:60716, bound_value=144:102716, second_product=288:110118, answer=276:101421)
- Layer 36: `俯`, `足足`, `ancock`, ` reduct`, `ovel` (target ranks: base_value=64:22778, first_product=128:16449, bound_value=144:78911, second_product=288:66164, answer=276:71487)
- Layer 37: `}<?`, `俯`, `放下`, `放下了`, `onana` (target ranks: base_value=64:58591, first_product=128:31934, bound_value=144:103123, second_product=288:95133, answer=276:93200)
- Layer 38: `俯`, ` .`, `错过`, ` Wilson`, `坏` (target ranks: base_value=64:33631, first_product=128:31167, bound_value=144:111603, second_product=288:87109, answer=276:92356)
- Layer 39: `hatic`, `osaurus`, ` .`, `罢`, `ozygous` (target ranks: base_value=64:54251, first_product=128:43767, bound_value=144:112503, second_product=288:71339, answer=276:70573)
- Layer 40: ` .`, ` x`, ` nasod`, ` .↵↵`, `�` (target ranks: base_value=64:7119, first_product=128:12629, bound_value=144:76531, second_product=288:29771, answer=276:35411)
- Layer 41: ` .`, ` .↵↵`, ` `, ` .↵`, ` ↵↵` (target ranks: base_value=64:2352, first_product=128:2040, bound_value=144:29646, second_product=288:7837, answer=276:3100)

### Filler position 47 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127330, first_product=128:126364, bound_value=144:125114, second_product=288:127446, answer=276:123352)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=64:10809, first_product=128:20638, bound_value=144:28082, second_product=288:21102, answer=276:22322)
- Layer 20: `}<?`, `东海`, ` partly`, ` sideways`, `ozygous` (target ranks: base_value=64:122419, first_product=128:126258, bound_value=144:113608, second_product=288:123116, answer=276:119900)
- Layer 30: `}<?`, `codeline`, `dividers`, `}using`, `?datasetId` (target ranks: base_value=64:112122, first_product=128:114799, bound_value=144:101952, second_product=288:108887, answer=276:122969)
- Layer 35: `codeline`, `ِّف`, `lett`, `}using`, `dividers` (target ranks: base_value=64:109045, first_product=128:113751, bound_value=144:122988, second_product=288:118183, answer=276:121266)
- Layer 36: `切割`, ` nasod`, `锯`, `ancock`, `足足` (target ranks: base_value=64:52195, first_product=128:61792, bound_value=144:107283, second_product=288:79995, answer=276:103815)
- Layer 37: `磨损`, `الميل`, `在东`, `切割`, `东京` (target ranks: base_value=64:83878, first_product=128:47767, bound_value=144:107955, second_product=288:72841, answer=276:83605)
- Layer 38: ` .`, `切割`, `遁`, ` prese`, `坏` (target ranks: base_value=64:30185, first_product=128:28650, bound_value=144:112394, second_product=288:62900, answer=276:86611)
- Layer 39: ` .`, `lett`, `磨损`, `坏`, ` unflagged` (target ranks: base_value=64:69531, first_product=128:40215, bound_value=144:112491, second_product=288:45168, answer=276:31975)
- Layer 40: ` .`, ` .↵↵`, `�`, ` nasod`, `坏` (target ranks: base_value=64:22635, first_product=128:10598, bound_value=144:90973, second_product=288:15491, answer=276:15371)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: base_value=64:3662, first_product=128:2377, bound_value=144:32393, second_product=288:3420, answer=276:831)

### Filler position 48 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127264, first_product=128:126207, bound_value=144:124794, second_product=288:127273, answer=276:123092)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=64:10689, first_product=128:21240, bound_value=144:28664, second_product=288:21105, answer=276:22499)
- Layer 20: `}<?`, `aplenty`, `aharoa`, `东海`, ` instantaneous` (target ranks: base_value=64:116752, first_product=128:112800, bound_value=144:93355, second_product=288:109588, answer=276:108265)
- Layer 30: `codeline`, ` accompanying`, `东京`, `磨`, `Quintal` (target ranks: base_value=64:101312, first_product=128:101979, bound_value=144:113855, second_product=288:88605, answer=276:116606)
- Layer 35: `codeline`, ` doubly`, `删`, `白雪`, ` fif` (target ranks: base_value=64:111148, first_product=128:111589, bound_value=144:126775, second_product=288:100598, answer=276:124759)
- Layer 36: ` soci`, ` nasod`, `yss`, ` reduct`, ` Predict` (target ranks: base_value=64:63660, first_product=128:59595, bound_value=144:118321, second_product=288:58412, answer=276:111961)
- Layer 37: `codeline`, `TreeLabel`, `Quintal`, `镶嵌`, `悬挂` (target ranks: base_value=64:115437, first_product=128:89381, bound_value=144:127287, second_product=288:86601, answer=276:116741)
- Layer 38: `肤`, `悬挂`, ` germ`, `立德`, ` crev` (target ranks: base_value=64:74581, first_product=128:89015, bound_value=144:124638, second_product=288:84014, answer=276:113417)
- Layer 39: ` .↵↵`, ` .`, ` encomp`, `贻`, `肤` (target ranks: base_value=64:106154, first_product=128:94110, bound_value=144:124636, second_product=288:102266, answer=276:111635)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` germ` (target ranks: base_value=64:80706, first_product=128:76065, bound_value=144:119553, second_product=288:84826, answer=276:105803)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=64:37866, first_product=128:30504, bound_value=144:76823, second_product=288:45689, answer=276:51349)

### Filler position 49 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127313, first_product=128:126331, bound_value=144:124997, second_product=288:127368, answer=276:123278)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10536, first_product=128:22664, bound_value=144:28988, second_product=288:21172, answer=276:22601)
- Layer 20: ` licensierad`, ` grounds`, ` instantaneous`, `zv`, `文本` (target ranks: base_value=64:74919, first_product=128:84850, bound_value=144:75549, second_product=288:108358, answer=276:92608)
- Layer 30: ` Answer`, `答案是`, ` ответ`, ` Antwort`, `codeline` (target ranks: base_value=64:94800, first_product=128:106701, bound_value=144:125673, second_product=288:102951, answer=276:108149)
- Layer 35: ` Answer`, `codeline`, `AED`, `oNames`, ` Antwort` (target ranks: base_value=64:110649, first_product=128:110647, bound_value=144:127299, second_product=288:102339, answer=276:106877)
- Layer 36: ` Answer`, `坏`, ` nasod`, `停`, `AED` (target ranks: base_value=64:59342, first_product=128:48794, bound_value=144:121372, second_product=288:62937, answer=276:77874)
- Layer 37: `oNames`, `codeline`, `insic`, ` consum`, ` retard` (target ranks: base_value=64:125145, first_product=128:107676, bound_value=144:122881, second_product=288:113381, answer=276:102981)
- Layer 38: `oNames`, ` retard`, `оду`, `<|EOT|>`, `codeline` (target ranks: base_value=64:126486, first_product=128:115988, bound_value=144:125102, second_product=288:118183, answer=276:91546)
- Layer 39: `�`, `deen`, `oxygen`, ` unflagged`, `►▼` (target ranks: base_value=64:106447, first_product=128:112600, bound_value=144:118017, second_product=288:79417, answer=276:74180)
- Layer 40: ` Answer`, ` .`, ` .↵↵`, ` nasod`, ` wink` (target ranks: base_value=64:33463, first_product=128:69035, bound_value=144:100935, second_product=288:31750, answer=276:30565)
- Layer 41: ` .`, ` Answer`, `Answer`, ` .↵↵`, `叮` (target ranks: base_value=64:13021, first_product=128:39119, bound_value=144:77808, second_product=288:12686, answer=276:7687)

### Filler position 50 (absolute token 842, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=64:122364, first_product=128:115152, bound_value=144:108340, second_product=288:112884, answer=276:109485)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, `aplenty` (target ranks: base_value=64:126608, first_product=128:116728, bound_value=144:105436, second_product=288:114353, answer=276:111806)
- Layer 20: `能被`, `答复`, ` Submission`, `EDER`, `差分` (target ranks: base_value=64:4376, first_product=128:42618, bound_value=144:30618, second_product=288:61237, answer=276:74279)
- Layer 30: `nze`, ` dátummal`, `lisitry`, ` المطلع`, `ritu` (target ranks: base_value=64:49888, first_product=128:29135, bound_value=144:889, second_product=288:1940, answer=276:16426)
- Layer 35: `280`, `288`, `286`, `287`, `279` (target ranks: base_value=64:93714, first_product=128:40172, bound_value=144:56186, second_product=288:2, answer=276:14)
- Layer 36: `280`, `279`, `276`, `278`, `288` (target ranks: base_value=64:121612, first_product=128:64753, bound_value=144:59332, second_product=288:5, answer=276:3)
- Layer 37: `280`, `279`, `288`, `276`, `278` (target ranks: base_value=64:127945, first_product=128:76678, bound_value=144:67989, second_product=288:3, answer=276:4)
- Layer 38: `276`, `280`, `279`, `278`, `288` (target ranks: base_value=64:128759, first_product=128:118689, bound_value=144:86593, second_product=288:5, answer=276:1)
- Layer 39: `276`, `�`, ` dátummal`, `pole`, `dv` (target ranks: base_value=64:127814, first_product=128:124371, bound_value=144:117754, second_product=288:140, answer=276:1)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `_answer` (target ranks: base_value=64:128340, first_product=128:92826, bound_value=144:119487, second_product=288:4040, answer=276:64)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=64:90052, first_product=128:36208, bound_value=144:74515, second_product=288:3691, answer=276:57)

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
diz = 64
kod = twice the number for diz plus 11
zaf = twice the number for diz plus 16
xev = 97
Question: What is twice the number for zaf minus 12?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
