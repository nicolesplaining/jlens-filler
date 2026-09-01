# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `185` (incorrect).
- No-filler answer: `229` (incorrect).
- Filler tokens: 25 tokens at absolute indices 667–691.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=64` | 1 (L24, filler 8) | L23, filler 8 (rank 8) |
| J-Lens | `first_product=128` | 113 (L35, filler 8) | Never |
| J-Lens | `bound_value=125` | 1 (L35, filler 10) | L31, filler 10 (rank 8) |
| J-Lens | `second_product=250` | 2 (L36, filler 10) | L35, filler 10 (rank 7) |
| J-Lens | `answer=235` | 26 (L38, filler 21) | Never |
| Logit lens | `base_value=64` | 1 (L27, filler 8) | L24, filler 8 (rank 7) |
| Logit lens | `first_product=128` | 189 (L5, filler 1) | Never |
| Logit lens | `bound_value=125` | 1 (L35, filler 10) | L35, filler 10 (rank 1) |
| Logit lens | `second_product=250` | 7 (L38, filler 10) | L38, filler 10 (rank 7) |
| Logit lens | `answer=235` | 29 (L34, filler 21) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 667, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=64:119571, first_product=128:114541, bound_value=125:112752, second_product=250:117386, answer=235:115380)
- Layer 10: `anta`, `fine`, `locked`, `sem`, `cape` (target ranks: base_value=64:63030, first_product=128:49731, bound_value=125:50739, second_product=250:44310, answer=235:70608)
- Layer 20: `扣`, `足`, `期望`, `垂`, `grown` (target ranks: base_value=64:708, first_product=128:16209, bound_value=125:14745, second_product=250:33172, answer=235:42990)
- Layer 30: ` Kur`, `kur`, ` kur`, ` Kurdish`, ` Kurd` (target ranks: base_value=64:411, first_product=128:58779, bound_value=125:59269, second_product=250:99686, answer=235:99603)
- Layer 35: ` Kur`, `kur`, ` kur`, ` Kurd`, ` Kurdish` (target ranks: base_value=64:240, first_product=128:55899, bound_value=125:44728, second_product=250:66586, answer=235:82365)
- Layer 36: ` Kur`, ` kur`, `kur`, ` Kurd`, ` Kurdish` (target ranks: base_value=64:444, first_product=128:32705, bound_value=125:34869, second_product=250:60327, answer=235:88349)
- Layer 37: ` Kur`, ` kur`, `kur`, `cur`, ` Kurs` (target ranks: base_value=64:1080, first_product=128:55403, bound_value=125:54753, second_product=250:93696, answer=235:113026)
- Layer 38: ` Kur`, ` kur`, `kur`, ` Kurs`, `-cur` (target ranks: base_value=64:2031, first_product=128:80935, bound_value=125:54755, second_product=250:90169, answer=235:111242)
- Layer 39: ` Kur`, ` kur`, `kur`, `Kadaghanon`, `本题分析` (target ranks: base_value=64:99532, first_product=128:124386, bound_value=125:51436, second_product=250:109227, answer=235:106060)
- Layer 40: ` talags`, ` kur`, `oooo`, `留存`, ` x` (target ranks: base_value=64:62325, first_product=128:113460, bound_value=125:16558, second_product=250:85823, answer=235:65193)
- Layer 41: ` .`, ` .↵↵`, `oooo`, ` kur`, ` .↵` (target ranks: base_value=64:60048, first_product=128:87354, bound_value=125:9334, second_product=250:26367, answer=235:40867)

### Filler position 2 (absolute token 668, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=64:121839, first_product=128:118784, bound_value=125:118062, second_product=250:120806, answer=235:119183)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `挪` (target ranks: base_value=64:20288, first_product=128:37572, bound_value=125:35853, second_product=250:33394, answer=235:33797)
- Layer 20: ` .`, `外向`, ` tall`, `�`, ` distant` (target ranks: base_value=64:4423, first_product=128:99134, bound_value=125:65249, second_product=250:83136, answer=235:49862)
- Layer 30: `翻`, `Quintal`, `反向`, `�`, ` dekameters` (target ranks: base_value=64:8292, first_product=128:107378, bound_value=125:45021, second_product=250:70028, answer=235:21024)
- Layer 35: `�`, `185`, `acin`, ` Heim`, `松松` (target ranks: base_value=64:20809, first_product=128:79885, bound_value=125:8851, second_product=250:60077, answer=235:552)
- Layer 36: ` Parehong`, `185`, ` gihulagway`, `积雪`, `ographs` (target ranks: base_value=64:50802, first_product=128:77241, bound_value=125:13523, second_product=250:92614, answer=235:50)
- Layer 37: `185`, `aplenty`, ` Parehong`, `?datasetId`, `زياح` (target ranks: base_value=64:88422, first_product=128:90568, bound_value=125:10084, second_product=250:100536, answer=235:114)
- Layer 38: `185`, `aplenty`, `困`, `}<?`, ` dekameters` (target ranks: base_value=64:126461, first_product=128:114256, bound_value=125:7937, second_product=250:102019, answer=235:38)
- Layer 39: `185`, `本题分析`, `tanle`, ` Nij`, `otan` (target ranks: base_value=64:127051, first_product=128:125256, bound_value=125:61699, second_product=250:126526, answer=235:5661)
- Layer 40: `185`, ` ld`, `实在`, ` ald`, `igrams` (target ranks: base_value=64:123331, first_product=128:111116, bound_value=125:23788, second_product=250:117134, answer=235:5642)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `.,`, `潜水` (target ranks: base_value=64:120585, first_product=128:112960, bound_value=125:44549, second_product=250:108508, answer=235:15928)

### Filler position 3 (absolute token 669, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125413, first_product=128:121165, bound_value=125:120673, second_product=250:123202, answer=235:121371)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: base_value=64:16573, first_product=128:25506, bound_value=125:26968, second_product=250:25247, answer=235:24962)
- Layer 20: `ait`, `忑`, `锁定`, `ashi`, `atile` (target ranks: base_value=64:8723, first_product=128:44271, bound_value=125:28722, second_product=250:53008, answer=235:29714)
- Layer 30: ` declar`, `平行`, ` décl`, ` unpack`, ` declarations` (target ranks: base_value=64:12227, first_product=128:114311, bound_value=125:92323, second_product=250:124770, answer=235:118905)
- Layer 35: ` variable`, ` variables`, `variable`, ` Variables`, `variables` (target ranks: base_value=64:5989, first_product=128:105856, bound_value=125:97651, second_product=250:117694, answer=235:111830)
- Layer 36: `变量的`, ` variables`, ` variable`, `定义的`, `variables` (target ranks: base_value=64:10911, first_product=128:89226, bound_value=125:85637, second_product=250:114462, answer=235:110821)
- Layer 37: `}<?`, `变量的`, `variables`, ` variables`, ` перемен` (target ranks: base_value=64:74555, first_product=128:113056, bound_value=125:111049, second_product=250:126551, answer=235:121681)
- Layer 38: `}<?`, `variables`, `打磨`, `混乱`, `定义了` (target ranks: base_value=64:89098, first_product=128:115923, bound_value=125:116248, second_product=250:127625, answer=235:122868)
- Layer 39: `}<?`, `script`, `文字的`, `珍珠`, `embl` (target ranks: base_value=64:121462, first_product=128:125846, bound_value=125:83779, second_product=250:124357, answer=235:120204)
- Layer 40: `dots`, `mmmm`, ` dotted`, ` .`, `oooo` (target ranks: base_value=64:100035, first_product=128:119644, bound_value=125:19971, second_product=250:113554, answer=235:106139)
- Layer 41: ` .`, ` dotted`, ` dots`, `试一试`, `一个一个` (target ranks: base_value=64:71781, first_product=128:93349, bound_value=125:7271, second_product=250:65588, answer=235:71436)

### Filler position 4 (absolute token 670, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125936, first_product=128:122683, bound_value=125:122213, second_product=250:124056, answer=235:122737)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=64:13664, first_product=128:23139, bound_value=125:23830, second_product=250:20621, answer=235:21328)
- Layer 20: `ait`, `atile`, `cape`, `胃癌`, ` wig` (target ranks: base_value=64:5916, first_product=128:40771, bound_value=125:38869, second_product=250:43596, answer=235:40853)
- Layer 30: ` tap`, `acos`, ` pros`, `tap`, `ERG` (target ranks: base_value=64:77327, first_product=128:122147, bound_value=125:122246, second_product=250:123527, answer=235:122816)
- Layer 35: ` tap`, `ERG`, ` pros`, `Tap`, ` Niagara` (target ranks: base_value=64:68598, first_product=128:124127, bound_value=125:123376, second_product=250:122499, answer=235:121742)
- Layer 36: ` dynam`, `ERG`, ` tap`, `动态`, ` rip` (target ranks: base_value=64:53002, first_product=128:113686, bound_value=125:104981, second_product=250:111855, answer=235:112761)
- Layer 37: `ERG`, `oug`, ` dynam`, `actors`, `house` (target ranks: base_value=64:88731, first_product=128:119999, bound_value=125:109328, second_product=250:120740, answer=235:120997)
- Layer 38: `本题分析`, `zyw`, `ERG`, `ozygous`, `oug` (target ranks: base_value=64:102056, first_product=128:121994, bound_value=125:107634, second_product=250:122514, answer=235:121547)
- Layer 39: `本题分析`, `}<?`, `oug`, ` talags`, ` Nij` (target ranks: base_value=64:112923, first_product=128:127647, bound_value=125:98838, second_product=250:115616, answer=235:117358)
- Layer 40: ` talags`, `oug`, `anj`, ` rip`, `ERG` (target ranks: base_value=64:102511, first_product=128:125745, bound_value=125:73418, second_product=250:103870, answer=235:113635)
- Layer 41: ` .`, `试一试`, `Question`, ` talags`, `乐乐` (target ranks: base_value=64:66081, first_product=128:106506, bound_value=125:24630, second_product=250:50887, answer=235:65330)

### Filler position 5 (absolute token 671, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125777, first_product=128:122913, bound_value=125:122507, second_product=250:123931, answer=235:122886)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:16160, first_product=128:26731, bound_value=125:27817, second_product=250:23672, answer=235:24545)
- Layer 20: `cape`, `幽`, `锁定`, ` future`, `鞍` (target ranks: base_value=64:9277, first_product=128:28771, bound_value=125:21908, second_product=250:23990, answer=235:23208)
- Layer 30: `推算`, ` kahaboga`, ` calcul`, ` calculated`, `算出` (target ranks: base_value=64:12601, first_product=128:64189, bound_value=125:14987, second_product=250:57350, answer=235:8075)
- Layer 35: `推算`, `特`, `ukiran`, `�`, `退出` (target ranks: base_value=64:79076, first_product=128:116972, bound_value=125:20635, second_product=250:37849, answer=235:742)
- Layer 36: `ukiran`, `radesh`, `推算`, `calcul`, ` calculated` (target ranks: base_value=64:117486, first_product=128:122267, bound_value=125:36921, second_product=250:55134, answer=235:2490)
- Layer 37: `}<?`, `Quintal`, `EDMF`, `aharan`, `-ulo` (target ranks: base_value=64:125903, first_product=128:123812, bound_value=125:35018, second_product=250:84479, answer=235:3168)
- Layer 38: `}<?`, `-ulo`, `EDMF`, `aharan`, `hemer` (target ranks: base_value=64:127842, first_product=128:127250, bound_value=125:63195, second_product=250:93623, answer=235:2577)
- Layer 39: `}<?`, `hemer`, `-ulo`, `aharan`, `EDMF` (target ranks: base_value=64:127988, first_product=128:128546, bound_value=125:93110, second_product=250:103225, answer=235:4684)
- Layer 40: ` talags`, `hemer`, `omit`, `反复`, `acl` (target ranks: base_value=64:124727, first_product=128:128056, bound_value=125:53147, second_product=250:69598, answer=235:1762)
- Layer 41: ` .`, ` .↵↵`, `试一试`, `不如`, ` ,` (target ranks: base_value=64:110491, first_product=128:125451, bound_value=125:29635, second_product=250:37848, answer=235:2203)

### Filler position 6 (absolute token 672, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125301, first_product=128:122465, bound_value=125:121971, second_product=250:123261, answer=235:122396)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:15099, first_product=128:23994, bound_value=125:25764, second_product=250:22260, answer=235:22634)
- Layer 20: `<｜begin▁of▁file｜>`, ` unflagged`, ` замен`, ` поха`, `替换` (target ranks: base_value=64:118381, first_product=128:112853, bound_value=125:114067, second_product=250:107503, answer=235:109684)
- Layer 30: `高明`, `turn`, ` turn`, `推算`, ` step` (target ranks: base_value=64:63866, first_product=128:75342, bound_value=125:55484, second_product=250:51646, answer=235:95829)
- Layer 35: ` step`, `高明`, `acks`, ` Tw`, ` Step` (target ranks: base_value=64:65423, first_product=128:69670, bound_value=125:61343, second_product=250:53714, answer=235:90308)
- Layer 36: ` Tw`, ` step`, `反复`, `高明`, ` twice` (target ranks: base_value=64:70043, first_product=128:47941, bound_value=125:47032, second_product=250:53387, answer=235:91142)
- Layer 37: ` step`, ` Tw`, `高明`, ` TW`, ` Step` (target ranks: base_value=64:91040, first_product=128:76656, bound_value=125:68822, second_product=250:73368, answer=235:108706)
- Layer 38: ` Tw`, ` TW`, `Tw`, `tw`, `xes` (target ranks: base_value=64:92994, first_product=128:90339, bound_value=125:76242, second_product=250:90313, answer=235:111718)
- Layer 39: ` talags`, `树叶`, ` nasod`, `ozygous`, `MMMMMMMM` (target ranks: base_value=64:117780, first_product=128:122062, bound_value=125:61941, second_product=250:98937, answer=235:117903)
- Layer 40: ` nasod`, ` Tw`, ` talags`, `dots`, ` dots` (target ranks: base_value=64:92592, first_product=128:114049, bound_value=125:30977, second_product=250:77967, answer=235:102951)
- Layer 41: ` .`, ` dots`, `试一试`, `dots`, ` dotted` (target ranks: base_value=64:83344, first_product=128:109705, bound_value=125:35421, second_product=250:45420, answer=235:89290)

### Filler position 7 (absolute token 673, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125181, first_product=128:122203, bound_value=125:121707, second_product=250:123071, answer=235:122150)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13537, first_product=128:23462, bound_value=125:25105, second_product=250:22216, answer=235:22579)
- Layer 20: `锁定`, ` smile`, `ait`, `鞍`, ` future` (target ranks: base_value=64:14640, first_product=128:33872, bound_value=125:41756, second_product=250:47514, answer=235:43896)
- Layer 30: `鞍`, `acks`, `容易被`, `提取`, ` Cogn` (target ranks: base_value=64:2115, first_product=128:17459, bound_value=125:22971, second_product=250:44246, answer=235:13626)
- Layer 35: `鞍`, `acks`, ` anxious`, ` repetition`, ` tap` (target ranks: base_value=64:1286, first_product=128:12112, bound_value=125:12843, second_product=250:19466, answer=235:8595)
- Layer 36: `acin`, `反复`, `acks`, `特`, `漂` (target ranks: base_value=64:3101, first_product=128:9152, bound_value=125:15190, second_product=250:23129, answer=235:8778)
- Layer 37: `}<?`, `anium`, `anj`, `冰冰`, `radesh` (target ranks: base_value=64:22579, first_product=128:16512, bound_value=125:29379, second_product=250:69827, answer=235:17464)
- Layer 38: `}<?`, `ocyst`, `radesh`, `acons`, `anium` (target ranks: base_value=64:42694, first_product=128:24039, bound_value=125:44665, second_product=250:76872, answer=235:19738)
- Layer 39: `}<?`, `hemer`, `文字的`, `ocyst`, `叶子` (target ranks: base_value=64:126116, first_product=128:127343, bound_value=125:74999, second_product=250:110162, answer=235:19463)
- Layer 40: ` talags`, ` mosunod`, `不思`, `银杏`, `下沉` (target ranks: base_value=64:123315, first_product=128:127737, bound_value=125:53854, second_product=250:100071, answer=235:4953)
- Layer 41: ` .`, `试一试`, `因为这些`, `))))`, `不如` (target ranks: base_value=64:105979, first_product=128:122897, bound_value=125:32266, second_product=250:43395, answer=235:1703)

### Filler position 8 (absolute token 674, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125286, first_product=128:122416, bound_value=125:121859, second_product=250:123182, answer=235:122249)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:12537, first_product=128:22821, bound_value=125:24163, second_product=250:21000, answer=235:21721)
- Layer 20: `ait`, ` Walker`, `锁定`, `挪`, `能被` (target ranks: base_value=64:8643, first_product=128:30295, bound_value=125:32097, second_product=250:36639, answer=235:33723)
- Layer 30: `64`, `kur`, ` Kaw`, ` repetitions`, ` kur` (target ranks: base_value=64:1, first_product=128:433, bound_value=125:38764, second_product=250:119422, answer=235:94074)
- Layer 35: `64`, `kur`, `鞍`, ` repetitions`, `akak` (target ranks: base_value=64:1, first_product=128:113, bound_value=125:11268, second_product=250:73865, answer=235:69390)
- Layer 36: `64`, ` Kur`, ` kur`, `留存`, `kur` (target ranks: base_value=64:1, first_product=128:146, bound_value=125:17529, second_product=250:79009, answer=235:81342)
- Layer 37: `}<?`, `64`, ` Kur`, `殿堂`, ` multipliers` (target ranks: base_value=64:2, first_product=128:509, bound_value=125:47117, second_product=250:117280, answer=235:119341)
- Layer 38: `}<?`, ` Kur`, `覆`, `殿堂`, `取了` (target ranks: base_value=64:18, first_product=128:10145, bound_value=125:72528, second_product=250:117121, answer=235:119466)
- Layer 39: `}<?`, `本题分析`, `覆`, `polar`, `ocyst` (target ranks: base_value=64:4314, first_product=128:59165, bound_value=125:77168, second_product=250:89456, answer=235:102910)
- Layer 40: `kur`, ` kur`, ` Kur`, ` talags`, `}<?` (target ranks: base_value=64:4980, first_product=128:48694, bound_value=125:16298, second_product=250:28184, answer=235:30160)
- Layer 41: ` kur`, ` .`, `kur`, ` Kur`, `那一` (target ranks: base_value=64:14135, first_product=128:50414, bound_value=125:10448, second_product=250:9790, answer=235:30573)

### Filler position 9 (absolute token 675, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125255, first_product=128:122420, bound_value=125:121914, second_product=250:123337, answer=235:122379)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12448, first_product=128:23456, bound_value=125:24419, second_product=250:21048, answer=235:22050)
- Layer 20: `锁定`, `ait`, ` Walker`, `能被`, `Walker` (target ranks: base_value=64:13291, first_product=128:37254, bound_value=125:38181, second_product=250:40535, answer=235:34511)
- Layer 30: ` twice`, `atan`, `Tap`, `鞍`, ` tap` (target ranks: base_value=64:9518, first_product=128:64568, bound_value=125:90146, second_product=250:104931, answer=235:75280)
- Layer 35: `Tap`, ` tap`, `鞍`, ` Tw`, ` Tap` (target ranks: base_value=64:6133, first_product=128:46999, bound_value=125:60312, second_product=250:74753, answer=235:65858)
- Layer 36: ` tap`, `Tap`, ` Tap`, `留存`, ` Tw` (target ranks: base_value=64:10342, first_product=128:34952, bound_value=125:56480, second_product=250:67303, answer=235:62209)
- Layer 37: `}<?`, `覆`, `acos`, `筋`, `ота` (target ranks: base_value=64:40493, first_product=128:48136, bound_value=125:73082, second_product=250:98020, answer=235:85406)
- Layer 38: `}<?`, `覆`, `筋`, `zat`, `ота` (target ranks: base_value=64:53012, first_product=128:68351, bound_value=125:73295, second_product=250:107238, answer=235:89878)
- Layer 39: `}<?`, `�`, `覆`, `筋`, `东海` (target ranks: base_value=64:82215, first_product=128:90295, bound_value=125:63393, second_product=250:108438, answer=235:78916)
- Layer 40: `筋`, `覆`, `留存`, ` x`, `保有` (target ranks: base_value=64:24532, first_product=128:53241, bound_value=125:13980, second_product=250:77597, answer=235:46021)
- Layer 41: ` .`, `留存`, `鹉`, `覆`, ` ` (target ranks: base_value=64:9577, first_product=128:18226, bound_value=125:6499, second_product=250:41001, answer=235:22715)

### Filler position 10 (absolute token 676, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125238, first_product=128:122642, bound_value=125:122098, second_product=250:123518, answer=235:122607)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11832, first_product=128:22144, bound_value=125:23961, second_product=250:19816, answer=235:21901)
- Layer 20: ` Walker`, `ait`, `能被`, `Walker`, `拆` (target ranks: base_value=64:14270, first_product=128:52203, bound_value=125:54529, second_product=250:45834, answer=235:51926)
- Layer 30: `鞍`, `洋`, `拆`, ` ES`, `Translate` (target ranks: base_value=64:55, first_product=128:2243, bound_value=125:1303, second_product=250:12754, answer=235:34759)
- Layer 35: `125`, ` Kaw`, `羊`, ` binomial`, ` smile` (target ranks: base_value=64:1000, first_product=128:3741, bound_value=125:1, second_product=250:7, answer=235:26185)
- Layer 36: `125`, `250`, `期望`, `去掉`, `alski` (target ranks: base_value=64:10187, first_product=128:7492, bound_value=125:1, second_product=250:2, answer=235:40683)
- Layer 37: `125`, `}<?`, `oNames`, `250`, `覆` (target ranks: base_value=64:50857, first_product=128:18151, bound_value=125:1, second_product=250:4, answer=235:71018)
- Layer 38: `125`, `}<?`, `覆`, `oNames`, `师徒` (target ranks: base_value=64:73234, first_product=128:22762, bound_value=125:1, second_product=250:13, answer=235:82057)
- Layer 39: `}<?`, `ULO`, `125`, `覆`, `-ulo` (target ranks: base_value=64:73608, first_product=128:48835, bound_value=125:3, second_product=250:217, answer=235:38308)
- Layer 40: `俯`, `覆`, `125`, `翻`, `}<?` (target ranks: base_value=64:31066, first_product=128:17862, bound_value=125:3, second_product=250:78, answer=235:4256)
- Layer 41: ` .`, `试一试`, ` without`, `实在`, `没有被` (target ranks: base_value=64:39292, first_product=128:29966, bound_value=125:6, second_product=250:37, answer=235:4984)

### Filler position 11 (absolute token 677, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125234, first_product=128:122886, bound_value=125:122381, second_product=250:123732, answer=235:122924)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12539, first_product=128:23527, bound_value=125:25335, second_product=250:20943, answer=235:22915)
- Layer 20: `ait`, ` Walker`, `锁定`, ` smile`, `忑` (target ranks: base_value=64:16819, first_product=128:48526, bound_value=125:38007, second_product=250:41895, answer=235:47290)
- Layer 30: ` tap`, `Tap`, ` rip`, ` consum`, ` tear` (target ranks: base_value=64:50055, first_product=128:120406, bound_value=125:108980, second_product=250:112132, answer=235:108969)
- Layer 35: `Tap`, ` tap`, ` Tap`, `tap`, ` rip` (target ranks: base_value=64:69977, first_product=128:114551, bound_value=125:99946, second_product=250:91705, answer=235:108564)
- Layer 36: ` tap`, ` zad`, `Tap`, ` Tap`, `zim` (target ranks: base_value=64:52097, first_product=128:99472, bound_value=125:66216, second_product=250:64469, answer=235:93024)
- Layer 37: `}<?`, `zat`, `zim`, `zam`, ` Mir` (target ranks: base_value=64:96804, first_product=128:111875, bound_value=125:86199, second_product=250:77929, answer=235:105976)
- Layer 38: `}<?`, `zat`, `�`, ` sip`, `polar` (target ranks: base_value=64:102592, first_product=128:114903, bound_value=125:87934, second_product=250:98836, answer=235:113334)
- Layer 39: `}<?`, `zat`, `�`, ` Nij`, `zam` (target ranks: base_value=64:98606, first_product=128:116692, bound_value=125:76499, second_product=250:91363, answer=235:96254)
- Layer 40: `zat`, `zim`, `�`, `殿堂`, `冰冰` (target ranks: base_value=64:55696, first_product=128:84777, bound_value=125:30665, second_product=250:53009, answer=235:67779)
- Layer 41: `鹉`, `坏`, ` .`, `冰冰`, ` ` (target ranks: base_value=64:25055, first_product=128:25330, bound_value=125:5066, second_product=250:18039, answer=235:16856)

### Filler position 12 (absolute token 678, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125066, first_product=128:122711, bound_value=125:122144, second_product=250:123459, answer=235:122716)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11653, first_product=128:22689, bound_value=125:25249, second_product=250:20788, answer=235:22409)
- Layer 20: `ait`, ` Walker`, `锁定`, `忑`, ` wig` (target ranks: base_value=64:13757, first_product=128:41994, bound_value=125:38727, second_product=250:43982, answer=235:44452)
- Layer 30: ` Kur`, `kur`, ` kur`, `鞍`, ` Kaw` (target ranks: base_value=64:8211, first_product=128:96568, bound_value=125:70518, second_product=250:76426, answer=235:92714)
- Layer 35: ` Kur`, `kur`, ` kur`, `鞍`, ` Kurdish` (target ranks: base_value=64:3899, first_product=128:84628, bound_value=125:59884, second_product=250:45339, answer=235:85619)
- Layer 36: ` Kur`, ` kur`, `kur`, `留存`, `ikuha` (target ranks: base_value=64:4512, first_product=128:63201, bound_value=125:47575, second_product=250:33639, answer=235:84715)
- Layer 37: ` Kur`, ` kur`, `kur`, ` kurs`, ` Kurs` (target ranks: base_value=64:35949, first_product=128:110161, bound_value=125:89485, second_product=250:71500, answer=235:111263)
- Layer 38: ` kur`, ` Kur`, `kur`, `}<?`, `�` (target ranks: base_value=64:54910, first_product=128:118653, bound_value=125:99633, second_product=250:90938, answer=235:112258)
- Layer 39: `}<?`, ` Kur`, `殿堂`, ` kur`, `otomy` (target ranks: base_value=64:95309, first_product=128:121191, bound_value=125:90701, second_product=250:89694, answer=235:109711)
- Layer 40: `留存`, `殿堂`, ` talags`, `acl`, `步骤如下` (target ranks: base_value=64:63912, first_product=128:112181, bound_value=125:56848, second_product=250:68790, answer=235:80327)
- Layer 41: `试一试`, `acular`, `步骤如下`, `abd`, `留存` (target ranks: base_value=64:45432, first_product=128:94302, bound_value=125:23415, second_product=250:29287, answer=235:53958)

### Filler position 13 (absolute token 679, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125011, first_product=128:122575, bound_value=125:121994, second_product=250:123320, answer=235:122605)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12692, first_product=128:23610, bound_value=125:25855, second_product=250:21567, answer=235:23571)
- Layer 20: `锁定`, `ait`, ` Walker`, `忑`, `Walker` (target ranks: base_value=64:16440, first_product=128:34398, bound_value=125:42701, second_product=250:41966, answer=235:37265)
- Layer 30: ` labor`, `鞍`, ` tap`, `锁定`, `拆` (target ranks: base_value=64:20683, first_product=128:55715, bound_value=125:57897, second_product=250:78149, answer=235:35593)
- Layer 35: `锁定`, ` labor`, ` tap`, ` var`, ` calculator` (target ranks: base_value=64:12527, first_product=128:36977, bound_value=125:45855, second_product=250:52903, answer=235:29950)
- Layer 36: ` tap`, `反复`, ` drip`, `柿子`, `重复` (target ranks: base_value=64:12699, first_product=128:25347, bound_value=125:46434, second_product=250:45031, answer=235:32610)
- Layer 37: `}<?`, `不急`, `流淌`, `冰冰`, `滴` (target ranks: base_value=64:38466, first_product=128:33562, bound_value=125:66845, second_product=250:72391, answer=235:45005)
- Layer 38: `冰冰`, ` nasod`, `}<?`, `筋`, `下沉` (target ranks: base_value=64:32015, first_product=128:35708, bound_value=125:71686, second_product=250:87169, answer=235:58302)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `�`, `下沉`, `打磨` (target ranks: base_value=64:74900, first_product=128:77188, bound_value=125:55305, second_product=250:94118, answer=235:73222)
- Layer 40: `下沉`, `语言文字`, ` nasod`, ` .`, `筋` (target ranks: base_value=64:14923, first_product=128:40811, bound_value=125:9864, second_product=250:48415, answer=235:39351)
- Layer 41: ` .`, `鹃`, ` .↵↵`, `我没有`, ` ` (target ranks: base_value=64:8070, first_product=128:24137, bound_value=125:5348, second_product=250:17750, answer=235:15082)

### Filler position 14 (absolute token 680, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125437, first_product=128:122999, bound_value=125:122436, second_product=250:123802, answer=235:122955)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11421, first_product=128:21881, bound_value=125:24163, second_product=250:20001, answer=235:21641)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=64:9865, first_product=128:27473, bound_value=125:33958, second_product=250:33235, answer=235:25977)
- Layer 30: ` x`, `avia`, ` X`, ` parallel`, ` xanth` (target ranks: base_value=64:31318, first_product=128:108772, bound_value=125:108669, second_product=250:119282, answer=235:87332)
- Layer 35: ` x`, ` X`, `avia`, `avat`, ` Kav` (target ranks: base_value=64:9207, first_product=128:83278, bound_value=125:74541, second_product=250:84042, answer=235:51854)
- Layer 36: `avia`, `留存`, ` x`, ` X`, `不急` (target ranks: base_value=64:9815, first_product=128:62589, bound_value=125:63389, second_product=250:58998, answer=235:40730)
- Layer 37: `avian`, `}<?`, `avia`, `xv`, `yv` (target ranks: base_value=64:55526, first_product=128:88622, bound_value=125:99141, second_product=250:104149, answer=235:64446)
- Layer 38: `avian`, `}<?`, `avl`, `avit`, `yv` (target ranks: base_value=64:45965, first_product=128:88044, bound_value=125:84948, second_product=250:98826, answer=235:58083)
- Layer 39: ` Xavier`, ` XAF`, ` X`, ` xanth`, ` x` (target ranks: base_value=64:75093, first_product=128:85014, bound_value=125:73508, second_product=250:96500, answer=235:65498)
- Layer 40: `kur`, ` kur`, ` x`, ` Kur`, `留存` (target ranks: base_value=64:18740, first_product=128:68882, bound_value=125:33498, second_product=250:55376, answer=235:41959)
- Layer 41: `kur`, ` kur`, `转载请`, `留存`, ` talags` (target ranks: base_value=64:4752, first_product=128:18945, bound_value=125:10034, second_product=250:19505, answer=235:11044)

### Filler position 15 (absolute token 681, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125258, first_product=128:123052, bound_value=125:122507, second_product=250:123871, answer=235:123089)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11224, first_product=128:21624, bound_value=125:23645, second_product=250:19026, answer=235:21089)
- Layer 20: `锁定`, `ait`, ` Walker`, ` cheer`, `Walker` (target ranks: base_value=64:8282, first_product=128:23751, bound_value=125:22495, second_product=250:24210, answer=235:18780)
- Layer 30: ` parallel`, `kur`, `平行`, ` repetitions`, ` kur` (target ranks: base_value=64:9366, first_product=128:103163, bound_value=125:84899, second_product=250:97507, answer=235:82661)
- Layer 35: ` repetition`, ` repetitions`, ` kur`, ` q`, `kur` (target ranks: base_value=64:11075, first_product=128:97350, bound_value=125:60868, second_product=250:67037, answer=235:70496)
- Layer 36: `留存`, ` repetitions`, `acin`, ` stabil`, ` repetition` (target ranks: base_value=64:13574, first_product=128:65583, bound_value=125:33737, second_product=250:41962, answer=235:52740)
- Layer 37: `}<?`, `isis`, `筋`, `acos`, `放下` (target ranks: base_value=64:76553, first_product=128:107320, bound_value=125:77208, second_product=250:88356, answer=235:79934)
- Layer 38: `}<?`, `isis`, `筋`, `文字的`, `zat` (target ranks: base_value=64:68373, first_product=128:105101, bound_value=125:80711, second_product=250:89581, answer=235:74641)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `文字的`, `?datasetId`, `覆` (target ranks: base_value=64:79099, first_product=128:107622, bound_value=125:82891, second_product=250:92527, answer=235:82188)
- Layer 40: `留存`, `筋`, `ses`, `kur`, `冰冰` (target ranks: base_value=64:17890, first_product=128:65057, bound_value=125:22627, second_product=250:56657, answer=235:43610)
- Layer 41: `留存`, ` .`, `kur`, `ses`, ` variables` (target ranks: base_value=64:5906, first_product=128:26614, bound_value=125:7512, second_product=250:24759, answer=235:12674)

### Filler position 16 (absolute token 682, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125529, first_product=128:123375, bound_value=125:122833, second_product=250:124103, answer=235:123446)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12104, first_product=128:22343, bound_value=125:24769, second_product=250:19716, answer=235:22296)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, `而此时` (target ranks: base_value=64:7538, first_product=128:25437, bound_value=125:26354, second_product=250:25667, answer=235:31367)
- Layer 30: `kur`, ` Kur`, ` kur`, ` Kaw`, `重复` (target ranks: base_value=64:30, first_product=128:40667, bound_value=125:66561, second_product=250:82607, answer=235:68045)
- Layer 35: ` Kur`, `kur`, ` kur`, ` Kaw`, `kurs` (target ranks: base_value=64:28, first_product=128:41937, bound_value=125:51966, second_product=250:58042, answer=235:66851)
- Layer 36: ` Kur`, ` kur`, `kur`, `ikuha`, ` Kaw` (target ranks: base_value=64:56, first_product=128:23712, bound_value=125:41250, second_product=250:38799, answer=235:64988)
- Layer 37: ` Kur`, ` kur`, `kur`, `cur`, ` кур` (target ranks: base_value=64:363, first_product=128:68323, bound_value=125:86098, second_product=250:83771, answer=235:103783)
- Layer 38: ` Kur`, `kur`, ` kur`, `覆`, ` Kurs` (target ranks: base_value=64:824, first_product=128:90471, bound_value=125:90932, second_product=250:86806, answer=235:102134)
- Layer 39: ` Kur`, ` kur`, `kur`, `覆`, `东海` (target ranks: base_value=64:44212, first_product=128:109734, bound_value=125:83833, second_product=250:70464, answer=235:85083)
- Layer 40: ` kur`, `kur`, `留存`, `覆`, ` x` (target ranks: base_value=64:11330, first_product=128:70462, bound_value=125:28475, second_product=250:26107, answer=235:34205)
- Layer 41: ` kur`, `kur`, ` .`, `步骤如下`, `的计算` (target ranks: base_value=64:4134, first_product=128:22016, bound_value=125:6961, second_product=250:6286, answer=235:8849)

### Filler position 17 (absolute token 683, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125805, first_product=128:123698, bound_value=125:123114, second_product=250:124473, answer=235:123721)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:14524, first_product=128:25008, bound_value=125:27702, second_product=250:22027, answer=235:25117)
- Layer 20: `锁定`, `ait`, `而此时`, ` Walker`, ` smile` (target ranks: base_value=64:9909, first_product=128:25026, bound_value=125:23167, second_product=250:21768, answer=235:26730)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `atan` (target ranks: base_value=64:2801, first_product=128:29002, bound_value=125:33120, second_product=250:25676, answer=235:29799)
- Layer 35: ` Tw`, `Tw`, ` twice`, `tw`, ` quadr` (target ranks: base_value=64:1387, first_product=128:19733, bound_value=125:19412, second_product=250:18337, answer=235:26946)
- Layer 36: ` Tw`, `询问`, `翻`, `Tw`, `反复` (target ranks: base_value=64:4625, first_product=128:25221, bound_value=125:35660, second_product=250:23648, answer=235:45622)
- Layer 37: `}<?`, ` doubling`, ` doubled`, `翻`, ` doubles` (target ranks: base_value=64:21652, first_product=128:33352, bound_value=125:67939, second_product=250:63745, answer=235:78047)
- Layer 38: `}<?`, ` doubling`, `覆`, `zat`, ` doubled` (target ranks: base_value=64:35374, first_product=128:58972, bound_value=125:85464, second_product=250:81458, answer=235:95448)
- Layer 39: `}<?`, `东海`, ` doubling`, `覆`, ` Nij` (target ranks: base_value=64:28251, first_product=128:59989, bound_value=125:61784, second_product=250:81558, answer=235:90584)
- Layer 40: `kur`, ` Kur`, ` Tw`, ` kur`, `覆` (target ranks: base_value=64:1475, first_product=128:30108, bound_value=125:9748, second_product=250:38543, answer=235:51265)
- Layer 41: `kur`, ` `, ` kur`, ` .`, ` twist` (target ranks: base_value=64:1300, first_product=128:14688, bound_value=125:4892, second_product=250:23409, answer=235:39372)

### Filler position 18 (absolute token 684, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125738, first_product=128:123869, bound_value=125:123355, second_product=250:124609, answer=235:123913)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13275, first_product=128:24358, bound_value=125:28035, second_product=250:22606, answer=235:24560)
- Layer 20: `忑`, `ait`, ` Walker`, `会成为`, `能被` (target ranks: base_value=64:15236, first_product=128:33961, bound_value=125:36542, second_product=250:33795, answer=235:41115)
- Layer 30: `算出`, ` twice`, ` kahaboga`, ` calculator`, `鞍` (target ranks: base_value=64:494, first_product=128:19179, bound_value=125:27885, second_product=250:47661, answer=235:55373)
- Layer 35: ` twice`, `算出`, ` repetition`, ` calculator`, `重复` (target ranks: base_value=64:2695, first_product=128:17226, bound_value=125:18047, second_product=250:10897, answer=235:34717)
- Layer 36: `算出`, `翻`, `重复`, ` twice`, `calcul` (target ranks: base_value=64:7441, first_product=128:46201, bound_value=125:43095, second_product=250:11835, answer=235:52375)
- Layer 37: `}<?`, ` doubling`, `珍珠`, ` doubles`, ` doubled` (target ranks: base_value=64:42413, first_product=128:86491, bound_value=125:70897, second_product=250:33778, answer=235:89855)
- Layer 38: `}<?`, `珍珠`, ` doubling`, ` doubled`, `东海` (target ranks: base_value=64:59780, first_product=128:93689, bound_value=125:78048, second_product=250:49774, answer=235:97999)
- Layer 39: `}<?`, `Quintal`, ` Nij`, `东海`, `uerak` (target ranks: base_value=64:89737, first_product=128:96327, bound_value=125:56167, second_product=250:24392, answer=235:83600)
- Layer 40: ` Kur`, `kur`, ` kur`, `100`, ` talags` (target ranks: base_value=64:16292, first_product=128:60481, bound_value=125:4037, second_product=250:6095, answer=235:40856)
- Layer 41: `kur`, ` kur`, ` Kur`, ` `, ` without` (target ranks: base_value=64:5077, first_product=128:35769, bound_value=125:2231, second_product=250:1525, answer=235:18263)

### Filler position 19 (absolute token 685, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125855, first_product=128:123794, bound_value=125:123271, second_product=250:124565, answer=235:123951)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11695, first_product=128:22938, bound_value=125:26379, second_product=250:21253, answer=235:22863)
- Layer 20: `忑`, `ait`, `会成为`, ` engaging`, ` Walker` (target ranks: base_value=64:21451, first_product=128:45752, bound_value=125:41295, second_product=250:42454, answer=235:45664)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=64:14606, first_product=128:53217, bound_value=125:53152, second_product=250:63057, answer=235:63094)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=64:7694, first_product=128:30615, bound_value=125:34360, second_product=250:21488, answer=235:52582)
- Layer 36: ` Tw`, `Tw`, `.tw`, `tw`, ` twice` (target ranks: base_value=64:8400, first_product=128:14926, bound_value=125:21002, second_product=250:11849, answer=235:39133)
- Layer 37: ` Tw`, `Tw`, ` Number`, ` number`, `calcul` (target ranks: base_value=64:36755, first_product=128:37686, bound_value=125:50431, second_product=250:35190, answer=235:71647)
- Layer 38: ` Tw`, `Tw`, `}<?`, ` twist`, ` Number` (target ranks: base_value=64:40920, first_product=128:56081, bound_value=125:61802, second_product=250:44987, answer=235:87659)
- Layer 39: `}<?`, `interpret`, `覆`, ` Fylke`, `东海` (target ranks: base_value=64:40538, first_product=128:56822, bound_value=125:53301, second_product=250:51661, answer=235:87399)
- Layer 40: `覆`, `inkle`, `šk`, `下沉`, ` evalu` (target ranks: base_value=64:6145, first_product=128:27783, bound_value=125:10211, second_product=250:22070, answer=235:55370)
- Layer 41: `不求`, ` without`, `šk`, `覆`, `inkle` (target ranks: base_value=64:982, first_product=128:4802, bound_value=125:1840, second_product=250:2951, answer=235:11834)

### Filler position 20 (absolute token 686, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125985, first_product=128:123889, bound_value=125:123338, second_product=250:124608, answer=235:123946)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11415, first_product=128:22334, bound_value=125:25193, second_product=250:20942, answer=235:22565)
- Layer 20: `ait`, ` Walker`, `会成为`, `平行`, `Walker` (target ranks: base_value=64:17722, first_product=128:43613, bound_value=125:57112, second_product=250:49440, answer=235:47557)
- Layer 30: `提问`, ` question`, ` questions`, `询问`, ` Question` (target ranks: base_value=64:27717, first_product=128:78046, bound_value=125:99407, second_product=250:74529, answer=235:44118)
- Layer 35: `询问`, ` question`, `提问`, ` Question`, ` equation` (target ranks: base_value=64:14689, first_product=128:36068, bound_value=125:63292, second_product=250:29907, answer=235:25474)
- Layer 36: ` question`, `询问`, ` Question`, `提问`, `Question` (target ranks: base_value=64:24600, first_product=128:33949, bound_value=125:72921, second_product=250:25498, answer=235:33870)
- Layer 37: ` Question`, `提问`, ` question`, `.question`, `Question` (target ranks: base_value=64:54116, first_product=128:46918, bound_value=125:85300, second_product=250:46881, answer=235:41098)
- Layer 38: `}<?`, `asking`, ` Question`, ` question`, `acos` (target ranks: base_value=64:49030, first_product=128:60557, bound_value=125:89964, second_product=250:47525, answer=235:35659)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `下沉`, `打磨`, `fluoro` (target ranks: base_value=64:87123, first_product=128:64525, bound_value=125:81380, second_product=250:64443, answer=235:58170)
- Layer 40: `下沉`, `kle`, `<｜begin▁of▁sentence｜>`, `留存`, `mmmm` (target ranks: base_value=64:31088, first_product=128:31809, bound_value=125:25000, second_product=250:21406, answer=235:44651)
- Layer 41: ` Question`, `Question`, `šk`, ` question`, `留存` (target ranks: base_value=64:6659, first_product=128:5925, bound_value=125:6078, second_product=250:3277, answer=235:5333)

### Filler position 21 (absolute token 687, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126319, first_product=128:124389, bound_value=125:123861, second_product=250:125094, answer=235:124367)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11525, first_product=128:22708, bound_value=125:24377, second_product=250:20579, answer=235:22409)
- Layer 20: `距`, `能被`, `ait`, ` Tact`, `Tw` (target ranks: base_value=64:12312, first_product=128:38060, bound_value=125:37578, second_product=250:32844, answer=235:37493)
- Layer 30: `}<?`, `Quintal`, `henera`, `?datasetId`, `ِّف` (target ranks: base_value=64:27806, first_product=128:58239, bound_value=125:21123, second_product=250:18981, answer=235:7973)
- Layer 35: `}using`, ` ninete`, `henera`, `馆长`, `185` (target ranks: base_value=64:65304, first_product=128:73032, bound_value=125:8747, second_product=250:21465, answer=235:502)
- Layer 36: `}using`, `eltemperaturen`, `185`, `?datasetId`, ` Parehong` (target ranks: base_value=64:93465, first_product=128:54334, bound_value=125:22249, second_product=250:56728, answer=235:67)
- Layer 37: `eltemperaturen`, `?datasetId`, `}using`, `}<?`, `185` (target ranks: base_value=64:108521, first_product=128:59274, bound_value=125:13410, second_product=250:65473, answer=235:82)
- Layer 38: `185`, `eltemperaturen`, `}<?`, `187`, `?datasetId` (target ranks: base_value=64:126733, first_product=128:95981, bound_value=125:19645, second_product=250:84538, answer=235:26)
- Layer 39: `185`, `187`, `aharan`, `本题分析`, `ozygous` (target ranks: base_value=64:128081, first_product=128:122661, bound_value=125:88459, second_product=250:121082, answer=235:2250)
- Layer 40: `185`, `187`, `atche`, `如实`, `}using` (target ranks: base_value=64:123598, first_product=128:84327, bound_value=125:40455, second_product=250:96850, answer=235:1616)
- Layer 41: ` .`, `185`, `.,`, `塔尔`, ` ` (target ranks: base_value=64:107531, first_product=128:89657, bound_value=125:38948, second_product=250:63259, answer=235:1811)

### Filler position 22 (absolute token 688, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126628, first_product=128:124783, bound_value=125:124261, second_product=250:125489, answer=235:124806)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11135, first_product=128:22293, bound_value=125:23984, second_product=250:20419, answer=235:22075)
- Layer 20: ` quadr`, ` tall`, `auce`, ` sideways`, ` smile` (target ranks: base_value=64:1509, first_product=128:16023, bound_value=125:9168, second_product=250:11992, answer=235:38763)
- Layer 30: `Quintal`, `陪`, ` pessimistic`, ` accompan`, `陪着` (target ranks: base_value=64:156, first_product=128:7319, bound_value=125:3820, second_product=250:27759, answer=235:65570)
- Layer 35: `二十五`, `adaghan`, `25`, `陪`, `放下` (target ranks: base_value=64:11728, first_product=128:31179, bound_value=125:7, second_product=250:52, answer=235:41085)
- Layer 36: `陪`, `igesimal`, `放下`, `陪着`, `}using` (target ranks: base_value=64:31071, first_product=128:31944, bound_value=125:8, second_product=250:41, answer=235:55153)
- Layer 37: `}<?`, `?datasetId`, `oNames`, `ِّف`, `}using` (target ranks: base_value=64:78688, first_product=128:68191, bound_value=125:396, second_product=250:1470, answer=235:68449)
- Layer 38: `}<?`, `ِّف`, `zat`, ` doubling`, `陪` (target ranks: base_value=64:79190, first_product=128:65144, bound_value=125:272, second_product=250:1351, answer=235:54676)
- Layer 39: `}using`, `}<?`, `zat`, `erer`, `叶子` (target ranks: base_value=64:74789, first_product=128:81486, bound_value=125:2952, second_product=250:7151, answer=235:51372)
- Layer 40: ` .`, ` dro`, `坏`, `试一试`, `二十五` (target ranks: base_value=64:23219, first_product=128:34517, bound_value=125:1045, second_product=250:962, answer=235:7942)
- Layer 41: ` .`, ` .↵↵`, `二十五`, `试一试`, ` .↵` (target ranks: base_value=64:9770, first_product=128:13725, bound_value=125:156, second_product=250:66, answer=235:750)

### Filler position 23 (absolute token 689, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126478, first_product=128:125066, bound_value=125:124520, second_product=250:125769, answer=235:124991)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=64:10960, first_product=128:23034, bound_value=125:24015, second_product=250:20250, answer=235:21931)
- Layer 20: `iganos`, `Dutch`, `leans`, ` Unc`, `吞` (target ranks: base_value=64:57855, first_product=128:54364, bound_value=125:27779, second_product=250:17875, answer=235:55790)
- Layer 30: ` tails`, `codeline`, ` doubling`, `日`, ` accompanying` (target ranks: base_value=64:97025, first_product=128:79944, bound_value=125:65386, second_product=250:73296, answer=235:82736)
- Layer 35: `codeline`, ` nasod`, ` doubly`, `坏`, ` Alt` (target ranks: base_value=64:117598, first_product=128:99941, bound_value=125:71996, second_product=250:79447, answer=235:118459)
- Layer 36: ` nasod`, `兜`, ` Colleg`, ` soci`, ` Predict` (target ranks: base_value=64:84867, first_product=128:64627, bound_value=125:49727, second_product=250:51361, answer=235:96353)
- Layer 37: `Quintal`, `肤`, `镶嵌`, `codeline`, ` doubled` (target ranks: base_value=64:117885, first_product=128:91298, bound_value=125:103544, second_product=250:84013, answer=235:110029)
- Layer 38: `肤`, ` .`, ` germ`, ` doubled`, `动` (target ranks: base_value=64:99681, first_product=128:90757, bound_value=125:70604, second_product=250:78103, answer=235:99511)
- Layer 39: ` .`, ` germ`, `肤`, ` encomp`, ` .↵↵` (target ranks: base_value=64:122417, first_product=128:79812, bound_value=125:32959, second_product=250:66641, answer=235:80391)
- Layer 40: ` .`, ` .↵↵`, `肤`, ` .↵`, `点点` (target ranks: base_value=64:110581, first_product=128:47267, bound_value=125:7406, second_product=250:33344, answer=235:44868)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `点点` (target ranks: base_value=64:71610, first_product=128:5137, bound_value=125:252, second_product=250:5840, answer=235:3966)

### Filler position 24 (absolute token 690, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126413, first_product=128:124926, bound_value=125:124406, second_product=250:125581, answer=235:124887)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: base_value=64:9849, first_product=128:21882, bound_value=125:23308, second_product=250:19252, answer=235:20891)
- Layer 20: ` smile`, `站`, `足`, ` grin`, `😂` (target ranks: base_value=64:1409, first_product=128:12910, bound_value=125:18476, second_product=250:14016, answer=235:19322)
- Layer 30: `codeline`, ` Answer`, `答案是`, `答案为`, `</think>` (target ranks: base_value=64:86601, first_product=128:118867, bound_value=125:121373, second_product=250:108043, answer=235:121360)
- Layer 35: `codeline`, ` Answer`, ` doubly`, `oNames`, ` doubling` (target ranks: base_value=64:113359, first_product=128:123492, bound_value=125:113389, second_product=250:97253, answer=235:126634)
- Layer 36: `codeline`, ` Answer`, `oNames`, ` doubly`, ` nasod` (target ranks: base_value=64:65446, first_product=128:97453, bound_value=125:79821, second_product=250:67585, answer=235:123949)
- Layer 37: `codeline`, `oNames`, `本题分析`, `/MODIS`, `aharoa` (target ranks: base_value=64:122375, first_product=128:120811, bound_value=125:115007, second_product=250:119964, answer=235:124731)
- Layer 38: `codeline`, `oNames`, `оду`, `hatic`, ` retard` (target ranks: base_value=64:122121, first_product=128:105579, bound_value=125:93266, second_product=250:100805, answer=235:108490)
- Layer 39: `树叶`, `}<?`, `本题分析`, ` instantaneous`, `叶子` (target ranks: base_value=64:102943, first_product=128:110916, bound_value=125:72737, second_product=250:96902, answer=235:59247)
- Layer 40: ` Answer`, ` .↵↵`, `Answer`, ` konder`, ` rall` (target ranks: base_value=64:35341, first_product=128:77659, bound_value=125:21175, second_product=250:67788, answer=235:9277)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` Answer`, `Answer` (target ranks: base_value=64:8712, first_product=128:19212, bound_value=125:2628, second_product=250:17366, answer=235:1916)

### Filler position 25 (absolute token 691, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `-ulo` (target ranks: base_value=64:122325, first_product=128:115163, bound_value=125:112815, second_product=250:114539, answer=235:113992)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, `aplenty` (target ranks: base_value=64:128377, first_product=128:118642, bound_value=125:106702, second_product=250:110022, answer=235:114104)
- Layer 20: ` reluct`, ` dekameters`, `?datasetId`, `aintiff`, `ethodology` (target ranks: base_value=64:117257, first_product=128:122913, bound_value=125:119719, second_product=250:123269, answer=235:127103)
- Layer 30: ` Paglin`, ` giiniton`, ` گزار`, `?datasetId`, `aplenty` (target ranks: base_value=64:73359, first_product=128:104862, bound_value=125:105568, second_product=250:117063, answer=235:123217)
- Layer 35: `答案是`, `答案为`, `答案`, ` ninete`, `答え` (target ranks: base_value=64:127833, first_product=128:129176, bound_value=125:122401, second_product=250:102130, answer=235:79701)
- Layer 36: `答案`, `答案为`, `答案是`, ` Paglin`, `参考答案` (target ranks: base_value=64:125123, first_product=128:128384, bound_value=125:118732, second_product=250:97353, answer=235:64836)
- Layer 37: `EDMF`, `aplenty`, `祭`, ` Paglin`, `cault` (target ranks: base_value=64:127192, first_product=128:127569, bound_value=125:101290, second_product=250:89789, answer=235:58286)
- Layer 38: ` Paglin`, `lut`, `oNames`, ` medief`, `aplenty` (target ranks: base_value=64:126770, first_product=128:127743, bound_value=125:106600, second_product=250:105660, answer=235:44550)
- Layer 39: `答案`, ` Antwort`, ` ответ`, `答案是`, ` answer` (target ranks: base_value=64:115617, first_product=128:125321, bound_value=125:64398, second_product=250:57221, answer=235:6042)
- Layer 40: ` Answer`, `Answer`, ` answer`, `_answer`, `答案` (target ranks: base_value=64:83505, first_product=128:96928, bound_value=125:22989, second_product=250:27046, answer=235:6517)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=64:30992, first_product=128:47186, bound_value=125:4842, second_product=250:6239, answer=235:6385)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>qin = 67
xag = 23
kur = 64
rek = twice the number for kur minus 28
xav = twice the number for kur minus 3
Question: What is twice the number for xav minus 15?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
