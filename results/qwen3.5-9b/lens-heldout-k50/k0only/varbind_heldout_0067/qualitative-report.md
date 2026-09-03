# First qualitative filler readout

These are **logit-lens token readouts** (final norm + unembedding applied to each block's residual); no Jacobian lens was used.

## Outcome

- Filler answer: `203` (correct).
- No-filler answer: `203` (correct).
- Filler tokens: 50 tokens at absolute indices 877–926.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| Logit lens | `base_value=43` | 19 (L31, filler 11) | Never |
| Logit lens | `first_product=86` | 1 (L23, filler 21) | L23, filler 3 (rank 4) |
| Logit lens | `bound_value=99` | 4 (L23, filler 21) | L23, filler 21 (rank 4) |
| Logit lens | `second_product=198` | 3 (L30, filler 24) | L30, filler 10 (rank 4) |
| Logit lens | `answer=203` | 5 (L30, filler 22) | L2, filler 4 (rank 9) |

## Logit lens top-5 by filler position

### Filler position 1 (absolute token 877, surface ` .`)

- Layer 0: ` `, `s`, `-`, `<|endoftext|>`, `↵` (target ranks: base_value=43:156, first_product=86:401, bound_value=99:259, second_product=198:26, answer=203:32)
- Layer 8: `o`, `ot`, `该`, `地`, `来` (target ranks: base_value=43:3262, first_product=86:7285, bound_value=99:5929, second_product=198:967, answer=203:1871)
- Layer 16: `沉`, `内`, `漫`, `յ`, `世界` (target ranks: base_value=43:69170, first_product=86:22287, bound_value=99:34357, second_product=198:14588, answer=203:12168)
- Layer 24: `longleftrightarrow`, `cket`, `utando`, `յ`, `pickle` (target ranks: base_value=43:220157, first_product=86:201685, bound_value=99:205687, second_product=198:237077, answer=203:233391)
- Layer 25: ` .`, `յ`, `cket`, `longleftrightarrow`, `DOCTYPE` (target ranks: base_value=43:199983, first_product=86:158769, bound_value=99:168850, second_product=198:213724, answer=203:206861)
- Layer 26: ` .`, ` dot`, `-dot`, ` '.',`, `(dot` (target ranks: base_value=43:141204, first_product=86:133220, bound_value=99:147934, second_product=198:202913, answer=203:173230)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=43:181257, first_product=86:226074, bound_value=99:213827, second_product=198:226529, answer=203:213199)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:83961, first_product=86:137400, bound_value=99:169518, second_product=198:172042, answer=203:146423)
- Layer 29: ` .`, `-.`, ` `.`, `!.`, `．` (target ranks: base_value=43:4210, first_product=86:31262, bound_value=99:41597, second_product=198:14823, answer=203:8866)
- Layer 30: ` .`, ` ..`, ` `.`, `-.`, ` ,` (target ranks: base_value=43:162, first_product=86:1885, bound_value=99:1494, second_product=198:1149, answer=203:228)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` `.`, ` ` (target ranks: base_value=43:37, first_product=86:151, bound_value=99:111, second_product=198:93, answer=203:49)

### Filler position 2 (absolute token 878, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `_` (target ranks: base_value=43:134, first_product=86:214, bound_value=99:151, second_product=198:21, answer=203:45)
- Layer 8: `o`, `�`, `u`, `省`, `以` (target ranks: base_value=43:3260, first_product=86:15694, bound_value=99:23755, second_product=198:717, answer=203:2924)
- Layer 16: `enas`, `宕`, `erm`, `漫`, `̀` (target ranks: base_value=43:91618, first_product=86:89516, bound_value=99:139103, second_product=198:91322, answer=203:48309)
- Layer 24: `longleftrightarrow`, `ី`, `cket`, `յ`, `之` (target ranks: base_value=43:221930, first_product=86:220848, bound_value=99:216657, second_product=198:240784, answer=203:239810)
- Layer 25: ` .`, `longleftrightarrow`, `cket`, `յ`, `之` (target ranks: base_value=43:212973, first_product=86:203623, bound_value=99:205036, second_product=198:233958, answer=203:233323)
- Layer 26: ` .`, `յ`, `ី`, `xdd`, `根据权利要求` (target ranks: base_value=43:198664, first_product=86:207350, bound_value=99:204733, second_product=198:243839, answer=203:237226)
- Layer 27: ` .`, ` `.`, `/.`, `．`, `-.` (target ranks: base_value=43:156110, first_product=86:226398, bound_value=99:194934, second_product=198:225956, answer=203:217786)
- Layer 28: ` .`, ` `.`, `-.`, `/.`, ` ..` (target ranks: base_value=43:84705, first_product=86:144266, bound_value=99:165805, second_product=198:208089, answer=203:197396)
- Layer 29: ` .`, `-.`, ` `.`, `/.`, `!.` (target ranks: base_value=43:7384, first_product=86:51976, bound_value=99:60514, second_product=198:42141, answer=203:35360)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, `/.` (target ranks: base_value=43:402, first_product=86:6334, bound_value=99:5137, second_product=198:7401, answer=203:1020)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` `, `↵` (target ranks: base_value=43:75, first_product=86:349, bound_value=99:217, second_product=198:207, answer=203:136)

### Filler position 3 (absolute token 879, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=43:144, first_product=86:222, bound_value=99:155, second_product=198:21, answer=203:44)
- Layer 8: `is`, `us`, `er`, `erm`, `o` (target ranks: base_value=43:18408, first_product=86:23049, bound_value=99:21364, second_product=198:1715, answer=203:5145)
- Layer 16: `翰`, `imonial`, `目的`, `的人`, `站` (target ranks: base_value=43:28951, first_product=86:20091, bound_value=99:72748, second_product=198:22326, answer=203:44016)
- Layer 24: `zgl`, `λεί`, ` eighty`, ` esplic`, `�` (target ranks: base_value=43:209147, first_product=86:526, bound_value=99:25192, second_product=198:239522, answer=203:243511)
- Layer 25: `�`, `спен`, `zgl`, `oglob`, `琪` (target ranks: base_value=43:145481, first_product=86:3474, bound_value=99:7775, second_product=198:210921, answer=203:206870)
- Layer 26: `两百`, `一百`, `九十`, ` Afinal`, `百年` (target ranks: base_value=43:216012, first_product=86:42768, bound_value=99:10114, second_product=198:184757, answer=203:214336)
- Layer 27: `十九`, `inete`, ` ninete`, `十九章`, ` nineteen` (target ranks: base_value=43:246512, first_product=86:247575, bound_value=99:31271, second_product=198:134628, answer=203:142378)
- Layer 28: `十九`, `inete`, ` nineteen`, ` ninete`, `十九章` (target ranks: base_value=43:242444, first_product=86:248050, bound_value=99:138020, second_product=198:5433, answer=203:37807)
- Layer 29: `inete`, `十九章`, ` nineteenth`, ` Nin`, `十九` (target ranks: base_value=43:241137, first_product=86:241599, bound_value=99:202680, second_product=198:13780, answer=203:45629)
- Layer 30: `inete`, `惊魂`, ` ninete`, `_editor`, ` sb` (target ranks: base_value=43:115212, first_product=86:93746, bound_value=99:157517, second_product=198:13, answer=203:990)
- Layer 31: ` .`, `.`, ` ,`, ` ..`, ` :` (target ranks: base_value=43:19623, first_product=86:28969, bound_value=99:185358, second_product=198:10175, answer=203:17353)

### Filler position 4 (absolute token 880, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=43:147, first_product=86:216, bound_value=99:160, second_product=198:20, answer=203:47)
- Layer 8: `an`, `d`, `t`, `emo`, `m` (target ranks: base_value=43:22297, first_product=86:33198, bound_value=99:15777, second_product=198:10736, answer=203:12214)
- Layer 16: `加上`, `再加上`, `imonial`, `�`, ` +` (target ranks: base_value=43:20385, first_product=86:27072, bound_value=99:39002, second_product=198:10334, answer=203:6120)
- Layer 24: `ound`, `位`, `madan`, `erialization`, `ění` (target ranks: base_value=43:126188, first_product=86:3785, bound_value=99:2995, second_product=198:99392, answer=203:124721)
- Layer 25: `�`, `pent`, `相当`, `madan`, `位` (target ranks: base_value=43:86465, first_product=86:2730, bound_value=99:334, second_product=198:57442, answer=203:74942)
- Layer 26: `olygon`, `�`, `一百`, `九十`, `民` (target ranks: base_value=43:142871, first_product=86:1577, bound_value=99:119, second_product=198:23765, answer=203:43201)
- Layer 27: `araq`, `燃`, `�`, `本站`, `️` (target ranks: base_value=43:234965, first_product=86:126543, bound_value=99:2487, second_product=198:21049, answer=203:71813)
- Layer 28: `十九`, `一百`, `рос`, `adh`, `戌` (target ranks: base_value=43:184559, first_product=86:171448, bound_value=99:22719, second_product=198:5557, answer=203:19497)
- Layer 29: `熙`, `adh`, `受益`, ` -`, `�` (target ranks: base_value=43:68141, first_product=86:84573, bound_value=99:49267, second_product=198:1873, answer=203:4894)
- Layer 30: ` .`, ` ..`, `ens`, `рос`, ` them` (target ranks: base_value=43:4088, first_product=86:15382, bound_value=99:18473, second_product=198:156, answer=203:44)
- Layer 31: ` .`, ` ,`, `<|im_end|>`, ` :`, ` ..` (target ranks: base_value=43:91, first_product=86:257, bound_value=99:331, second_product=198:318, answer=203:257)

### Filler position 5 (absolute token 881, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=43:144, first_product=86:205, bound_value=99:160, second_product=198:20, answer=203:47)
- Layer 8: `uff`, `r`, `�`, `յ`, `�` (target ranks: base_value=43:29023, first_product=86:35106, bound_value=99:31864, second_product=198:3792, answer=203:10483)
- Layer 16: `�`, `�`, `激`, `imonial`, `翰` (target ranks: base_value=43:78327, first_product=86:56003, bound_value=99:112979, second_product=198:85429, answer=203:110688)
- Layer 24: `�`, `ound`, `琪`, `�`, `崎` (target ranks: base_value=43:105741, first_product=86:570, bound_value=99:1210, second_product=198:121973, answer=203:173210)
- Layer 25: `�`, `圃`, `崎`, `九十`, `熙` (target ranks: base_value=43:62446, first_product=86:621, bound_value=99:94, second_product=198:76159, answer=203:88314)
- Layer 26: `一百`, `�`, `九十`, `圃`, `�` (target ranks: base_value=43:142165, first_product=86:9538, bound_value=99:265, second_product=198:87029, answer=203:84467)
- Layer 27: `️`, `�`, `antium`, `根据权利要求`, `�` (target ranks: base_value=43:217843, first_product=86:172728, bound_value=99:3428, second_product=198:40514, answer=203:63742)
- Layer 28: `️`, `十九`, ` .`, `adh`, `atement` (target ranks: base_value=43:82766, first_product=86:193750, bound_value=99:14486, second_product=198:8838, answer=203:7018)
- Layer 29: ` .`, `熙`, `ates`, `adh`, `固` (target ranks: base_value=43:18481, first_product=86:77561, bound_value=99:36911, second_product=198:4029, answer=203:1090)
- Layer 30: ` .`, ` ..`, `熙`, ` .$`, `固` (target ranks: base_value=43:508, first_product=86:9736, bound_value=99:13405, second_product=198:252, answer=203:16)
- Layer 31: ` .`, ` ,`, `<|im_end|>`, ` :`, ` ..` (target ranks: base_value=43:50, first_product=86:210, bound_value=99:371, second_product=198:540, answer=203:365)

### Filler position 6 (absolute token 882, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=43:143, first_product=86:197, bound_value=99:160, second_product=198:20, answer=203:47)
- Layer 8: `u`, `in`, `en`, `�`, `s` (target ranks: base_value=43:2118, first_product=86:3051, bound_value=99:5604, second_product=198:249, answer=203:555)
- Layer 16: `得`, `+self`, `�`, `orks`, `站` (target ranks: base_value=43:15757, first_product=86:7850, bound_value=99:54707, second_product=198:16832, answer=203:13862)
- Layer 24: `λεί`, `�`, ` eighty`, `zgl`, `琪` (target ranks: base_value=43:203608, first_product=86:96, bound_value=99:6538, second_product=198:233966, answer=203:242531)
- Layer 25: `�`, `спен`, `九十`, `莽`, `琪` (target ranks: base_value=43:142535, first_product=86:1370, bound_value=99:1613, second_product=198:210068, answer=203:207416)
- Layer 26: `九十`, `一百`, `百年`, `�`, `莽` (target ranks: base_value=43:218789, first_product=86:31591, bound_value=99:1904, second_product=198:181800, answer=203:212853)
- Layer 27: `十九`, `inete`, `十九章`, ` ninete`, ` nineteenth` (target ranks: base_value=43:245888, first_product=86:245987, bound_value=99:17283, second_product=198:87558, answer=203:147235)
- Layer 28: `十九`, `inete`, `十八`, ` nineteen`, ` nineteenth` (target ranks: base_value=43:219022, first_product=86:246708, bound_value=99:116803, second_product=198:2974, answer=203:42088)
- Layer 29: `inete`, ` nineteenth`, `惊魂`, `十九章`, `zan` (target ranks: base_value=43:221687, first_product=86:190046, bound_value=99:199017, second_product=198:5400, answer=203:52586)
- Layer 30: `inete`, `惊魂`, ` sb`, ` ninete`, `审` (target ranks: base_value=43:81120, first_product=86:38546, bound_value=99:128826, second_product=198:17, answer=203:1174)
- Layer 31: ` .`, ` ,`, `.`, ` :`, ` ` (target ranks: base_value=43:1237, first_product=86:2644, bound_value=99:28465, second_product=198:1305, answer=203:13647)

### Filler position 7 (absolute token 883, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `.` (target ranks: base_value=43:141, first_product=86:192, bound_value=99:158, second_product=198:20, answer=203:47)
- Layer 8: `atur`, `u`, `s`, `m`, `哪` (target ranks: base_value=43:6654, first_product=86:13208, bound_value=99:12482, second_product=198:1709, answer=203:2875)
- Layer 16: `�`, `<think>`, `�`, `略`, `射` (target ranks: base_value=43:55663, first_product=86:40934, bound_value=99:109558, second_product=198:68188, answer=203:41188)
- Layer 24: `λεί`, `�`, `zgl`, `崎`, `ēr` (target ranks: base_value=43:218287, first_product=86:4272, bound_value=99:37845, second_product=198:239124, answer=203:243767)
- Layer 25: `崎`, `�`, `圃`, `спен`, `usercontent` (target ranks: base_value=43:166743, first_product=86:15243, bound_value=99:11696, second_product=198:225472, answer=203:224006)
- Layer 26: `一百`, `两百`, `崎`, `四百`, `二百` (target ranks: base_value=43:202350, first_product=86:96953, bound_value=99:14451, second_product=198:183162, answer=203:205817)
- Layer 27: `十九`, `inete`, `第二百零`, `十九章`, ` nineteen` (target ranks: base_value=43:244406, first_product=86:247959, bound_value=99:111088, second_product=198:137331, answer=203:108690)
- Layer 28: `十九`, `inete`, ` nineteen`, ` nineteenth`, `十九章` (target ranks: base_value=43:221248, first_product=86:247925, bound_value=99:197626, second_product=198:29943, answer=203:5302)
- Layer 29: `inete`, `第二百零`, `adh`, `entieth`, `十九章` (target ranks: base_value=43:221663, first_product=86:218937, bound_value=99:225124, second_product=198:71232, answer=203:6853)
- Layer 30: `inete`, ` .`, ` sb`, `第二百零`, `惊魂` (target ranks: base_value=43:37388, first_product=86:14059, bound_value=99:88185, second_product=198:24, answer=203:27)
- Layer 31: ` .`, ` ,`, ` :`, `.`, ` ..` (target ranks: base_value=43:631, first_product=86:840, bound_value=99:6911, second_product=198:3047, answer=203:2907)

### Filler position 8 (absolute token 884, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `.` (target ranks: base_value=43:141, first_product=86:189, bound_value=99:159, second_product=198:20, answer=203:45)
- Layer 8: `u`, `田`, `á`, `�`, `en` (target ranks: base_value=43:21288, first_product=86:31435, bound_value=99:29131, second_product=198:2629, answer=203:10984)
- Layer 16: `漫`, `依`, `之`, `ာ`, `�` (target ranks: base_value=43:94767, first_product=86:35868, bound_value=99:94203, second_product=198:29827, answer=203:19825)
- Layer 24: `longleftrightarrow`, `cket`, `່`, `յ`, `@if` (target ranks: base_value=43:241800, first_product=86:225272, bound_value=99:227244, second_product=198:240411, answer=203:233651)
- Layer 25: `cket`, `່`, `longleftrightarrow`, `յ`, ` .` (target ranks: base_value=43:235256, first_product=86:200128, bound_value=99:208726, second_product=198:232762, answer=203:221491)
- Layer 26: ` .`, `յ`, `antium`, `anic`, `ာ` (target ranks: base_value=43:201454, first_product=86:144454, bound_value=99:172772, second_product=198:223555, answer=203:191712)
- Layer 27: ` .`, ` `.`, `-.`, `．`, ` .=` (target ranks: base_value=43:164947, first_product=86:188948, bound_value=99:169008, second_product=198:195976, answer=203:171130)
- Layer 28: ` .`, `-.`, `．`, ` `.`, ` $.` (target ranks: base_value=43:91858, first_product=86:83482, bound_value=99:133117, second_product=198:157138, answer=203:129438)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=43:5389, first_product=86:16348, bound_value=99:32826, second_product=198:14419, answer=203:9032)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, ` .$` (target ranks: base_value=43:478, first_product=86:1531, bound_value=99:2821, second_product=198:2268, answer=203:312)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, ` ,` (target ranks: base_value=43:49, first_product=86:119, bound_value=99:94, second_product=198:91, answer=203:59)

### Filler position 9 (absolute token 885, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `B` (target ranks: base_value=43:140, first_product=86:187, bound_value=99:156, second_product=198:20, answer=203:47)
- Layer 8: `u`, `o`, `�`, `d`, `en` (target ranks: base_value=43:9149, first_product=86:8290, bound_value=99:13285, second_product=198:2191, answer=203:3480)
- Layer 16: `<think>`, `�`, `米`, `ering`, `得` (target ranks: base_value=43:2815, first_product=86:3648, bound_value=99:12980, second_product=198:3886, answer=203:2606)
- Layer 24: ` eighty`, `λεί`, `�`, `zgl`, `琛` (target ranks: base_value=43:222028, first_product=86:2802, bound_value=99:53132, second_product=198:236208, answer=203:237854)
- Layer 25: `�`, `崎`, `九十`, `琛`, `спен` (target ranks: base_value=43:171367, first_product=86:7654, bound_value=99:14719, second_product=198:213900, answer=203:208175)
- Layer 26: `一百`, `两百`, `九十`, `二百`, `百` (target ranks: base_value=43:235357, first_product=86:69872, bound_value=99:20727, second_product=198:178005, answer=203:213755)
- Layer 27: `十九`, `inete`, ` ninete`, `十九章`, `第二百零` (target ranks: base_value=43:247465, first_product=86:247887, bound_value=99:44085, second_product=198:105636, answer=203:124871)
- Layer 28: `十九`, `inete`, ` nineteen`, ` ninete`, ` nineteenth` (target ranks: base_value=43:244604, first_product=86:248143, bound_value=99:168545, second_product=198:6479, answer=203:31688)
- Layer 29: `inete`, `十九章`, ` nineteenth`, `惊魂`, `十九` (target ranks: base_value=43:243952, first_product=86:244948, bound_value=99:224839, second_product=198:10657, answer=203:36280)
- Layer 30: `inete`, `惊魂`, ` sb`, ` ninete`, ` Bros` (target ranks: base_value=43:148148, first_product=86:99066, bound_value=99:181089, second_product=198:19, answer=203:1194)
- Layer 31: ` .`, `.`, ` ,`, ` ..`, ` :` (target ranks: base_value=43:48802, first_product=86:46338, bound_value=99:194952, second_product=198:26586, answer=203:42573)

### Filler position 10 (absolute token 886, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `B` (target ranks: base_value=43:138, first_product=86:183, bound_value=99:158, second_product=198:20, answer=203:45)
- Layer 8: `u`, `en`, `o`, `和`, `յ` (target ranks: base_value=43:5893, first_product=86:6611, bound_value=99:5542, second_product=198:459, answer=203:3091)
- Layer 16: `以`, `慕`, `禁`, `翰`, `明` (target ranks: base_value=43:12730, first_product=86:4835, bound_value=99:46465, second_product=198:2145, answer=203:2398)
- Layer 24: `�`, ` con`, `allax`, `熙`, `ound` (target ranks: base_value=43:140566, first_product=86:174, bound_value=99:532, second_product=198:68082, answer=203:108771)
- Layer 25: ` con`, `熙`, `antages`, `�`, `allax` (target ranks: base_value=43:56152, first_product=86:79, bound_value=99:9, second_product=198:36259, answer=203:39879)
- Layer 26: `九十`, `熙`, `体现`, `一百`, `圃` (target ranks: base_value=43:109955, first_product=86:371, bound_value=99:23, second_product=198:26004, answer=203:19231)
- Layer 27: `熙`, `一百`, `根据权利要求`, `️`, `共` (target ranks: base_value=43:195365, first_product=86:52646, bound_value=99:146, second_product=198:4410, answer=203:10859)
- Layer 28: `一百`, `熙`, `十九`, `️`, `adh` (target ranks: base_value=43:135494, first_product=86:60055, bound_value=99:1233, second_product=198:293, answer=203:2809)
- Layer 29: `熙`, `adh`, `享`, `ates`, `正式` (target ranks: base_value=43:42156, first_product=86:84506, bound_value=99:30522, second_product=198:30, answer=203:278)
- Layer 30: ` .`, `的一次`, `熙`, `1`, `一百` (target ranks: base_value=43:17202, first_product=86:39489, bound_value=99:49349, second_product=198:4, answer=203:92)
- Layer 31: ` .`, ` ,`, ` :`, `.`, `<|im_end|>` (target ranks: base_value=43:231, first_product=86:893, bound_value=99:719, second_product=198:1024, answer=203:1138)

### Filler position 11 (absolute token 887, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `B` (target ranks: base_value=43:136, first_product=86:182, bound_value=99:160, second_product=198:20, answer=203:47)
- Layer 8: `s`, `u`, `o`, ` ...`, `，` (target ranks: base_value=43:915, first_product=86:5676, bound_value=99:4502, second_product=198:228, answer=203:939)
- Layer 16: `漫`, `率`, `白`, `地`, `ာ` (target ranks: base_value=43:61311, first_product=86:8295, bound_value=99:35062, second_product=198:14111, answer=203:10443)
- Layer 24: `յ`, `ာ`, `longleftrightarrow`, `之`, `cket` (target ranks: base_value=43:235296, first_product=86:211249, bound_value=99:215158, second_product=198:239773, answer=203:231952)
- Layer 25: `յ`, `ာ`, `cket`, `longleftrightarrow`, ` .` (target ranks: base_value=43:228601, first_product=86:186858, bound_value=99:193419, second_product=198:233293, answer=203:221795)
- Layer 26: `յ`, ` .`, `ာ`, `antium`, `longleftrightarrow` (target ranks: base_value=43:217295, first_product=86:179738, bound_value=99:199438, second_product=198:242590, answer=203:228610)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, `-.` (target ranks: base_value=43:170863, first_product=86:195391, bound_value=99:187287, second_product=198:217966, answer=203:197982)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=43:114335, first_product=86:116860, bound_value=99:163880, second_product=198:198103, answer=203:154857)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `!.` (target ranks: base_value=43:5633, first_product=86:23531, bound_value=99:36755, second_product=198:21646, answer=203:10252)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` .*` (target ranks: base_value=43:157, first_product=86:1305, bound_value=99:1804, second_product=198:1148, answer=203:187)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, `↵↵` (target ranks: base_value=43:19, first_product=86:117, bound_value=99:88, second_product=198:73, answer=203:44)

### Filler position 12 (absolute token 888, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `B` (target ranks: base_value=43:133, first_product=86:181, bound_value=99:159, second_product=198:20, answer=203:45)
- Layer 8: `�`, `en`, `m`, `�`, `ant` (target ranks: base_value=43:3998, first_product=86:5516, bound_value=99:4451, second_product=198:575, answer=203:291)
- Layer 16: `erlo`, `翰`, `erator`, `imonial`, `孩` (target ranks: base_value=43:207604, first_product=86:154932, bound_value=99:212878, second_product=198:174927, answer=203:124355)
- Layer 24: `ellaneous`, `禾`, `intosh`, `eting`, `olygon` (target ranks: base_value=43:12701, first_product=86:23093, bound_value=99:23728, second_product=198:7372, answer=203:1463)
- Layer 25: `ellaneous`, `禾`, `intosh`, `olygon`, `eting` (target ranks: base_value=43:10311, first_product=86:15963, bound_value=99:12076, second_product=198:4707, answer=203:770)
- Layer 26: `ellaneous`, `intosh`, `roring`, `禾`, `乎其` (target ranks: base_value=43:24339, first_product=86:34331, bound_value=99:28494, second_product=198:29261, answer=203:3947)
- Layer 27: ` mik`, `微`, ` Mik`, ` micro`, ` mic` (target ranks: base_value=43:132280, first_product=86:158568, bound_value=99:138111, second_product=198:158006, answer=203:81488)
- Layer 28: ` mik`, `微`, ` micro`, ` Mik`, ` mic` (target ranks: base_value=43:69323, first_product=86:31246, bound_value=99:68763, second_product=198:95243, answer=203:42236)
- Layer 29: ` mik`, `微`, ` Mik`, ` micro`, ` mic` (target ranks: base_value=43:6048, first_product=86:6198, bound_value=99:19524, second_product=198:11054, answer=203:3351)
- Layer 30: ` .`, ` mik`, ` Mik`, ` micro`, ` mic` (target ranks: base_value=43:707, first_product=86:3342, bound_value=99:4717, second_product=198:1778, answer=203:367)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` :`, ` -` (target ranks: base_value=43:114, first_product=86:605, bound_value=99:265, second_product=198:161, answer=203:260)

### Filler position 13 (absolute token 889, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:132, first_product=86:179, bound_value=99:157, second_product=198:20, answer=203:45)
- Layer 8: `�`, `缈`, `唯一`, `o`, `�` (target ranks: base_value=43:11065, first_product=86:3143, bound_value=99:2943, second_product=198:2434, answer=203:1583)
- Layer 16: `<think>`, `汽`, `破`, `ipline`, `载` (target ranks: base_value=43:67193, first_product=86:40254, bound_value=99:97262, second_product=198:92798, answer=203:41321)
- Layer 24: `λεί`, `�`, ` eighty`, `zgl`, `崎` (target ranks: base_value=43:230850, first_product=86:1138, bound_value=99:27579, second_product=198:239698, answer=203:243994)
- Layer 25: `�`, `崎`, `九十`, `спен`, `oglob` (target ranks: base_value=43:170024, first_product=86:4342, bound_value=99:5467, second_product=198:216273, answer=203:213106)
- Layer 26: `两百`, `一百`, `九十`, `四百`, `二百` (target ranks: base_value=43:229532, first_product=86:75476, bound_value=99:12914, second_product=198:202226, answer=203:224724)
- Layer 27: `十九`, `inete`, `十九章`, ` nineteen`, `第二百零` (target ranks: base_value=43:244728, first_product=86:247822, bound_value=99:65598, second_product=198:137906, answer=203:136969)
- Layer 28: `十九`, `inete`, ` nineteen`, `十八`, ` nineteenth` (target ranks: base_value=43:235759, first_product=86:247985, bound_value=99:171265, second_product=198:4551, answer=203:34456)
- Layer 29: `inete`, ` nineteenth`, `十九章`, ` Nin`, `一九` (target ranks: base_value=43:231934, first_product=86:229305, bound_value=99:212626, second_product=198:6999, answer=203:32010)
- Layer 30: `惊魂`, `inete`, ` sb`, ` Ig`, `chn` (target ranks: base_value=43:90236, first_product=86:57510, bound_value=99:182060, second_product=198:16, answer=203:1743)
- Layer 31: ` .`, ` ,`, `.`, ` :`, ` *` (target ranks: base_value=43:8806, first_product=86:10949, bound_value=99:139664, second_product=198:17147, answer=203:43484)

### Filler position 14 (absolute token 890, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `B` (target ranks: base_value=43:131, first_product=86:179, bound_value=99:155, second_product=198:20, answer=203:43)
- Layer 8: `杈`, `u`, `…`, `t`, ` ...` (target ranks: base_value=43:14982, first_product=86:12153, bound_value=99:19764, second_product=198:832, answer=203:17762)
- Layer 16: `漫`, `地`, `白`, `望`, `ာ` (target ranks: base_value=43:65657, first_product=86:14281, bound_value=99:61843, second_product=198:9356, answer=203:19093)
- Layer 24: `longleftrightarrow`, `ာ`, `之`, `່`, `cket` (target ranks: base_value=43:238326, first_product=86:215698, bound_value=99:222252, second_product=198:232210, answer=203:232210)
- Layer 25: `longleftrightarrow`, `ာ`, `�`, ` .`, `之` (target ranks: base_value=43:229509, first_product=86:187822, bound_value=99:202199, second_product=198:213152, answer=203:216280)
- Layer 26: `ာ`, `longleftrightarrow`, ` .`, `最新发布`, `antium` (target ranks: base_value=43:208894, first_product=86:134760, bound_value=99:179899, second_product=198:215746, answer=203:203104)
- Layer 27: ` .`, `-.`, `．`, ` `.`, ` .$` (target ranks: base_value=43:141601, first_product=86:157236, bound_value=99:153303, second_product=198:153303, answer=203:144635)
- Layer 28: ` .`, `．`, `-.`, ` `.`, `!.` (target ranks: base_value=43:88101, first_product=86:58315, bound_value=99:129540, second_product=198:107273, answer=203:88101)
- Layer 29: ` .`, `-.`, `．`, `.`, ` `.` (target ranks: base_value=43:5086, first_product=86:10064, bound_value=99:33069, second_product=198:7087, answer=203:4512)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:540, first_product=86:1371, bound_value=99:5435, second_product=198:2405, answer=203:456)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, `↵` (target ranks: base_value=43:58, first_product=86:163, bound_value=99:151, second_product=198:130, answer=203:87)

### Filler position 15 (absolute token 891, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:131, first_product=86:179, bound_value=99:157, second_product=198:20, answer=203:43)
- Layer 8: `o`, `田`, `↵`, `us`, `յ` (target ranks: base_value=43:1234, first_product=86:4027, bound_value=99:3675, second_product=198:319, answer=203:931)
- Layer 16: `以`, `目的`, `的人`, `�`, `公司` (target ranks: base_value=43:16791, first_product=86:10381, bound_value=99:58117, second_product=198:2688, answer=203:6005)
- Layer 24: `λεί`, `�`, `刺激`, ` eighty`, `zgl` (target ranks: base_value=43:187135, first_product=86:74, bound_value=99:3946, second_product=198:228972, answer=203:242348)
- Layer 25: `�`, `спен`, `刺激`, `莽`, `九十` (target ranks: base_value=43:105910, first_product=86:861, bound_value=99:419, second_product=198:184870, answer=203:177464)
- Layer 26: `九十`, `�`, `一百`, `莽`, `第九章` (target ranks: base_value=43:210491, first_product=86:27584, bound_value=99:475, second_product=198:162467, answer=203:196301)
- Layer 27: `十九`, `inete`, `十九章`, ` ninete`, ` nineteen` (target ranks: base_value=43:244828, first_product=86:246844, bound_value=99:5435, second_product=198:51041, answer=203:109622)
- Layer 28: `十九`, `inete`, ` nineteen`, ` ninete`, ` nineteenth` (target ranks: base_value=43:221389, first_product=86:247565, bound_value=99:51429, second_product=198:3783, answer=203:21956)
- Layer 29: `inete`, ` Nin`, ` nineteenth`, `一九`, `十九` (target ranks: base_value=43:224097, first_product=86:236381, bound_value=99:187065, second_product=198:3714, answer=203:25438)
- Layer 30: `inete`, `审`, ` sb`, `惊魂`, `第一百` (target ranks: base_value=43:157312, first_product=86:132334, bound_value=99:212302, second_product=198:10, answer=203:678)
- Layer 31: ` .`, `.`, ` ,`, ` :`, ` ..` (target ranks: base_value=43:11797, first_product=86:23842, bound_value=99:144616, second_product=198:8560, answer=203:30323)

### Filler position 16 (absolute token 892, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:131, first_product=86:178, bound_value=99:154, second_product=198:20, answer=203:43)
- Layer 8: `o`, `uff`, `um`, ` ...`, `U` (target ranks: base_value=43:3043, first_product=86:5447, bound_value=99:4588, second_product=198:152, answer=203:970)
- Layer 16: `以`, `�`, `翰`, `ältä`, `得` (target ranks: base_value=43:26448, first_product=86:7658, bound_value=99:56478, second_product=198:20652, answer=203:18963)
- Layer 24: `λεί`, `�`, `�`, `zgl`, `刺激` (target ranks: base_value=43:223361, first_product=86:1150, bound_value=99:23183, second_product=198:241965, answer=203:246629)
- Layer 25: `�`, `崎`, `спен`, `圃`, `oglob` (target ranks: base_value=43:159134, first_product=86:9366, bound_value=99:7473, second_product=198:225237, answer=203:223321)
- Layer 26: ` Afinal`, `刺激`, `�`, `一百`, `崎` (target ranks: base_value=43:206540, first_product=86:67361, bound_value=99:7536, second_product=198:175093, answer=203:204724)
- Layer 27: `十九`, `inete`, `ք`, `十九章`, `第二百零` (target ranks: base_value=43:245223, first_product=86:246524, bound_value=99:87803, second_product=198:100392, answer=203:125255)
- Layer 28: `十九`, `inete`, `十八`, ` nineteenth`, ` nineteen` (target ranks: base_value=43:212558, first_product=86:245225, bound_value=99:166964, second_product=198:9594, answer=203:34468)
- Layer 29: `inete`, `adh`, ` nineteenth`, `itters`, `丹` (target ranks: base_value=43:178434, first_product=86:135919, bound_value=99:203683, second_product=198:6781, answer=203:22690)
- Layer 30: ` .`, `审`, `chn`, ` Nin`, ` sb` (target ranks: base_value=43:73424, first_product=86:34528, bound_value=99:150643, second_product=198:7, answer=203:247)
- Layer 31: ` .`, ` ,`, ` :`, `.`, ` &` (target ranks: base_value=43:739, first_product=86:1302, bound_value=99:9784, second_product=198:1321, answer=203:3373)

### Filler position 17 (absolute token 893, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:131, first_product=86:177, bound_value=99:154, second_product=198:20, answer=203:43)
- Layer 8: `o`, `uff`, `um`, `�`, ` ...` (target ranks: base_value=43:6289, first_product=86:10206, bound_value=99:11697, second_product=198:332, answer=203:1629)
- Layer 16: `igungs`, `束`, `得`, `子`, `信念` (target ranks: base_value=43:74450, first_product=86:62992, bound_value=99:71952, second_product=198:11934, answer=203:6832)
- Layer 24: `λεί`, `�`, `�`, `�`, `erialization` (target ranks: base_value=43:134056, first_product=86:104, bound_value=99:1088, second_product=198:216005, answer=203:237899)
- Layer 25: `�`, `第九章`, `九十`, `спен`, `λεί` (target ranks: base_value=43:88773, first_product=86:151, bound_value=99:26, second_product=198:170936, answer=203:179306)
- Layer 26: `九十`, `�`, `第九章`, ` ninety`, ` Afinal` (target ranks: base_value=43:188594, first_product=86:4191, bound_value=99:16, second_product=198:146429, answer=203:174694)
- Layer 27: `本站`, `️`, `�`, `antium`, `十九章` (target ranks: base_value=43:239036, first_product=86:195201, bound_value=99:477, second_product=198:35672, answer=203:100533)
- Layer 28: `一百`, `十九`, `本站`, `十九章`, `inete` (target ranks: base_value=43:141980, first_product=86:234421, bound_value=99:2959, second_product=198:5974, answer=203:58833)
- Layer 29: `熙`, `adh`, `一百`, `本站`, `固` (target ranks: base_value=43:121797, first_product=86:209950, bound_value=99:67714, second_product=198:3936, answer=203:74964)
- Layer 30: ` .`, `一百`, `第一百`, `рос`, `ienes` (target ranks: base_value=43:22000, first_product=86:55632, bound_value=99:54113, second_product=198:6, answer=203:1109)
- Layer 31: ` .`, ` ,`, ` :`, `.`, ` ..` (target ranks: base_value=43:147, first_product=86:863, bound_value=99:918, second_product=198:446, answer=203:1356)

### Filler position 18 (absolute token 894, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:128, first_product=86:174, bound_value=99:153, second_product=198:20, answer=203:43)
- Layer 8: `o`, ` ...`, `�`, `�`, `um` (target ranks: base_value=43:11236, first_product=86:10148, bound_value=99:8461, second_product=198:729, answer=203:1737)
- Layer 16: `�`, `明`, `��`, `BUFF`, `漫` (target ranks: base_value=43:237658, first_product=86:238090, bound_value=99:221272, second_product=198:236393, answer=203:157384)
- Layer 24: `变量`, `变量的`, ` variables`, ` Variables`, `Variables` (target ranks: base_value=43:247414, first_product=86:241803, bound_value=99:239042, second_product=198:247717, answer=203:243005)
- Layer 25: `变量`, ` Variables`, `变量的`, ` variables`, `Variables` (target ranks: base_value=43:247297, first_product=86:242947, bound_value=99:236664, second_product=198:246958, answer=203:241660)
- Layer 26: `变量`, ` Variables`, `变量的`, `Variables`, ` variables` (target ranks: base_value=43:246894, first_product=86:240224, bound_value=99:237357, second_product=198:247576, answer=203:242262)
- Layer 27: `变量`, ` variable`, `Variable`, `变量的`, ` Variables` (target ranks: base_value=43:242895, first_product=86:240642, bound_value=99:229720, second_product=198:244965, answer=203:231310)
- Layer 28: `变量`, `变量的`, ` variable`, ` Variables`, `Variable` (target ranks: base_value=43:243190, first_product=86:223975, bound_value=99:239730, second_product=198:247978, answer=203:245486)
- Layer 29: `变量`, ` var`, `变量的`, ` variable`, `Variable` (target ranks: base_value=43:199097, first_product=86:140371, bound_value=99:197149, second_product=198:242920, answer=203:221210)
- Layer 30: ` var`, `var`, ` vari`, `变量`, ` variable` (target ranks: base_value=43:16444, first_product=86:16967, bound_value=99:37961, second_product=198:56491, answer=203:18222)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` ..`, ` :` (target ranks: base_value=43:194, first_product=86:641, bound_value=99:430, second_product=198:292, answer=203:392)

### Filler position 19 (absolute token 895, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:124, first_product=86:174, bound_value=99:153, second_product=198:20, answer=203:43)
- Layer 8: `o`, `u`, `�`, ` ...`, `�` (target ranks: base_value=43:25102, first_product=86:21997, bound_value=99:17630, second_product=198:1474, answer=203:5786)
- Layer 16: `禁`, `漫`, `清`, `igungs`, `市` (target ranks: base_value=43:39017, first_product=86:21654, bound_value=99:51773, second_product=198:5161, answer=203:2768)
- Layer 24: `�`, `madan`, `ounding`, `ound`, `了` (target ranks: base_value=43:164525, first_product=86:1167, bound_value=99:3059, second_product=198:119496, answer=203:76053)
- Layer 25: `�`, ` con`, `了`, `ounding`, `圃` (target ranks: base_value=43:78535, first_product=86:276, bound_value=99:101, second_product=198:66663, answer=203:29550)
- Layer 26: `�`, `ounding`, `erman`, `usercontent`, `zni` (target ranks: base_value=43:227948, first_product=86:4319, bound_value=99:597, second_product=198:147913, answer=203:96381)
- Layer 27: `�`, `淼`, `一百`, `️`, ` .` (target ranks: base_value=43:225231, first_product=86:35337, bound_value=99:298, second_product=198:8331, answer=203:30623)
- Layer 28: `一百`, `erm`, ` .`, `️`, `erman` (target ranks: base_value=43:177909, first_product=86:27894, bound_value=99:143, second_product=198:173, answer=203:10673)
- Layer 29: ` .`, `熙`, `erm`, `享`, `一百` (target ranks: base_value=43:95775, first_product=86:39643, bound_value=99:2325, second_product=198:13, answer=203:2572)
- Layer 30: ` .`, ` ..`, ` .$`, `的一次`, ` ,` (target ranks: base_value=43:11593, first_product=86:11418, bound_value=99:4298, second_product=198:8, answer=203:666)
- Layer 31: ` .`, ` ,`, `<|im_end|>`, ` :`, ` ..` (target ranks: base_value=43:206, first_product=86:490, bound_value=99:274, second_product=198:104, answer=203:490)

### Filler position 20 (absolute token 896, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `<|endoftext|>`, `_` (target ranks: base_value=43:122, first_product=86:174, bound_value=99:150, second_product=198:20, answer=203:42)
- Layer 8: `u`, `o`, `�`, `�`, ` ...` (target ranks: base_value=43:7648, first_product=86:11910, bound_value=99:13405, second_product=198:1040, answer=203:3431)
- Layer 16: `漫`, `望`, `内`, `égr`, `晴` (target ranks: base_value=43:76281, first_product=86:29648, bound_value=99:96987, second_product=198:21056, answer=203:20321)
- Layer 24: `longleftrightarrow`, `erer`, `cket`, `égr`, `ី` (target ranks: base_value=43:232260, first_product=86:208738, bound_value=99:210715, second_product=198:235288, answer=203:206423)
- Layer 25: `cket`, `longleftrightarrow`, `յ`, `égr`, `�` (target ranks: base_value=43:216659, first_product=86:168732, bound_value=99:179548, second_product=198:221809, answer=203:184703)
- Layer 26: `յ`, `longleftrightarrow`, ` .`, `uks`, `ာ` (target ranks: base_value=43:200022, first_product=86:141335, bound_value=99:158612, second_product=198:231324, answer=203:175680)
- Layer 27: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=43:123507, first_product=86:165791, bound_value=99:149695, second_product=198:177328, answer=203:117345)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=43:61909, first_product=86:53595, bound_value=99:100005, second_product=198:122533, answer=203:61196)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=43:3751, first_product=86:8651, bound_value=99:18070, second_product=198:11440, answer=203:3808)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:193, first_product=86:652, bound_value=99:1425, second_product=198:1125, answer=203:200)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, `↵↵` (target ranks: base_value=43:40, first_product=86:144, bound_value=99:121, second_product=198:126, answer=203:64)

### Filler position 21 (absolute token 897, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=43:121, first_product=86:171, bound_value=99:151, second_product=198:20, answer=203:42)
- Layer 8: `en`, `�`, `o`, `enary`, `�` (target ranks: base_value=43:6279, first_product=86:15755, bound_value=99:8625, second_product=198:457, answer=203:1017)
- Layer 16: `以`, `提`, `+self`, `ած`, `uty` (target ranks: base_value=43:66704, first_product=86:41388, bound_value=99:72414, second_product=198:22542, answer=203:37922)
- Layer 24: `�`, `�`, `λεί`, `8`, ` con` (target ranks: base_value=43:179045, first_product=86:4, bound_value=99:79, second_product=198:167999, answer=203:237027)
- Layer 25: `�`, `第九章`, `九十`, `9`, ` ninety` (target ranks: base_value=43:134857, first_product=86:12, bound_value=99:4, second_product=198:105571, answer=203:143140)
- Layer 26: `九十`, `第九章`, ` ninety`, `�`, `百年` (target ranks: base_value=43:185730, first_product=86:1739, bound_value=99:7, second_product=198:100998, answer=203:151627)
- Layer 27: `十九章`, `一百`, ` Nin`, `十九`, `�` (target ranks: base_value=43:241110, first_product=86:226863, bound_value=99:84, second_product=198:18222, answer=203:98397)
- Layer 28: `一百`, `esion`, `第一百`, `十九`, ` Nin` (target ranks: base_value=43:210413, first_product=86:241881, bound_value=99:971, second_product=198:1087, answer=203:128781)
- Layer 29: `熙`, `丹`, `一百`, `�`, `第一百` (target ranks: base_value=43:215029, first_product=86:238784, bound_value=99:110150, second_product=198:267, answer=203:97210)
- Layer 30: ` Hundred`, ` .`, `一百`, `第一百`, `是一次` (target ranks: base_value=43:98115, first_product=86:110863, bound_value=99:140776, second_product=198:34, answer=203:10794)
- Layer 31: ` .`, `.`, ` ,`, ` :`, ` ?` (target ranks: base_value=43:836, first_product=86:6179, bound_value=99:12882, second_product=198:1515, answer=203:11252)

### Filler position 22 (absolute token 898, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=43:121, first_product=86:172, bound_value=99:149, second_product=198:20, answer=203:42)
- Layer 8: `o`, `u`, `委`, `田`, `↵` (target ranks: base_value=43:8938, first_product=86:6655, bound_value=99:12275, second_product=198:218, answer=203:2029)
- Layer 16: `禁`, `�`, `派`, `享`, `ermo` (target ranks: base_value=43:15183, first_product=86:2324, bound_value=99:38134, second_product=198:8064, answer=203:4817)
- Layer 24: `-License`, `ит`, `刺激`, `燃`, `应对` (target ranks: base_value=43:228341, first_product=86:6016, bound_value=99:5897, second_product=198:164226, answer=203:197134)
- Layer 25: `下水`, `刺激`, `olygon`, `相当`, `办` (target ranks: base_value=43:204164, first_product=86:8758, bound_value=99:5438, second_product=198:125605, answer=203:112823)
- Layer 26: `徒`, `刺激`, `olygon`, `一百`, `anen` (target ranks: base_value=43:164380, first_product=86:61308, bound_value=99:31220, second_product=198:124681, answer=203:104753)
- Layer 27: `�`, `erialized`, `ք`, `燃`, `法规和` (target ranks: base_value=43:207376, first_product=86:246409, bound_value=99:231177, second_product=198:27982, answer=203:5696)
- Layer 28: `非凡`, `adh`, `二百`, `�`, `erialized` (target ranks: base_value=43:179956, first_product=86:247911, bound_value=99:247806, second_product=198:14969, answer=203:2031)
- Layer 29: `adh`, `�`, `erialized`, `лей`, `受益` (target ranks: base_value=43:170568, first_product=86:110969, bound_value=99:177985, second_product=198:4118, answer=203:67)
- Layer 30: `二百`, `腹`, `preter`, ` .`, `2` (target ranks: base_value=43:68643, first_product=86:45979, bound_value=99:83356, second_product=198:55, answer=203:5)
- Layer 31: ` .`, ` ,`, `.`, ` :`, ` 。` (target ranks: base_value=43:2354, first_product=86:912, bound_value=99:873, second_product=198:1920, answer=203:346)

### Filler position 23 (absolute token 899, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:122, first_product=86:170, bound_value=99:150, second_product=198:20, answer=203:42)
- Layer 8: `o`, `↵`, `sn`, `田`, `о` (target ranks: base_value=43:6264, first_product=86:6613, bound_value=99:5958, second_product=198:511, answer=203:1853)
- Layer 16: `漫`, `内`, `依`, `晴`, `望` (target ranks: base_value=43:49907, first_product=86:13086, bound_value=99:55363, second_product=198:7839, answer=203:8118)
- Layer 24: `longleftrightarrow`, `之`, `cket`, `յ`, `ာ` (target ranks: base_value=43:213525, first_product=86:190487, bound_value=99:194258, second_product=198:232781, answer=203:203684)
- Layer 25: `longleftrightarrow`, `յ`, `之`, `�`, `cket` (target ranks: base_value=43:201725, first_product=86:158893, bound_value=99:161831, second_product=198:220759, answer=203:189178)
- Layer 26: `longleftrightarrow`, ` .`, `յ`, `最新发布`, `�` (target ranks: base_value=43:186635, first_product=86:143192, bound_value=99:162638, second_product=198:237200, answer=203:202444)
- Layer 27: ` .`, `．`, ` .$`, ` `.`, `-.` (target ranks: base_value=43:125178, first_product=86:173471, bound_value=99:159123, second_product=198:193222, answer=203:163112)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=43:70808, first_product=86:88599, bound_value=99:109694, second_product=198:162147, answer=203:113255)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `!.` (target ranks: base_value=43:2923, first_product=86:14555, bound_value=99:16985, second_product=198:12599, answer=203:5887)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:128, first_product=86:721, bound_value=99:1336, second_product=198:1252, answer=203:186)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, `↵` (target ranks: base_value=43:32, first_product=86:132, bound_value=99:108, second_product=198:124, answer=203:59)

### Filler position 24 (absolute token 900, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:119, first_product=86:172, bound_value=99:148, second_product=198:20, answer=203:42)
- Layer 8: `�`, `�`, `o`, `t`, `d` (target ranks: base_value=43:6666, first_product=86:7495, bound_value=99:5325, second_product=198:500, answer=203:863)
- Layer 16: `igungs`, `imonial`, `足`, `得`, `派` (target ranks: base_value=43:52198, first_product=86:92160, bound_value=99:79561, second_product=198:14301, answer=203:12217)
- Layer 24: `λεί`, `�`, ` eighty`, `�`, `刺激` (target ranks: base_value=43:211268, first_product=86:274, bound_value=99:13304, second_product=198:235465, answer=203:240552)
- Layer 25: `�`, `спен`, `刺激`, `พล`, ` معا` (target ranks: base_value=43:106765, first_product=86:396, bound_value=99:1102, second_product=198:188754, answer=203:181796)
- Layer 26: `�`, `一百`, `спен`, ` ninety`, `九十` (target ranks: base_value=43:221800, first_product=86:16130, bound_value=99:1659, second_product=198:161448, answer=203:209676)
- Layer 27: `十九`, `inete`, `十九章`, ` nineteenth`, ` nineteen` (target ranks: base_value=43:246413, first_product=86:244709, bound_value=99:10429, second_product=198:27124, answer=203:67524)
- Layer 28: `十九`, `inete`, ` nineteenth`, ` nineteen`, `十八` (target ranks: base_value=43:236787, first_product=86:246921, bound_value=99:91384, second_product=198:2204, answer=203:33815)
- Layer 29: `inete`, `一九`, ` nineteenth`, `十九`, `itters` (target ranks: base_value=43:222272, first_product=86:217119, bound_value=99:201260, second_product=198:464, answer=203:21551)
- Layer 30: `inete`, `第一百`, `1`, `一百`, `惊魂` (target ranks: base_value=43:170179, first_product=86:130926, bound_value=99:214017, second_product=198:3, answer=203:1655)
- Layer 31: ` .`, `.`, ` ,`, ` :`, ` -` (target ranks: base_value=43:7108, first_product=86:10290, bound_value=99:60630, second_product=198:1646, answer=203:11296)

### Filler position 25 (absolute token 901, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:117, first_product=86:169, bound_value=99:149, second_product=198:20, answer=203:42)
- Layer 8: `�`, `o`, `�`, `u`, `额` (target ranks: base_value=43:24015, first_product=86:20769, bound_value=99:18551, second_product=198:558, answer=203:2622)
- Layer 16: `派`, `�`, `cü`, `usių`, `把握` (target ranks: base_value=43:33504, first_product=86:54804, bound_value=99:50869, second_product=198:29171, answer=203:6973)
- Layer 24: `່`, `�`, `ャ`, `年一季度`, `owanie` (target ranks: base_value=43:85188, first_product=86:102427, bound_value=99:31742, second_product=198:174304, answer=203:135965)
- Layer 25: `�`, `່`, `órios`, `共`, `allax` (target ranks: base_value=43:58644, first_product=86:51740, bound_value=99:16682, second_product=198:145544, answer=203:102373)
- Layer 26: `四百`, `�`, `国强`, `百`, `osing` (target ranks: base_value=43:87970, first_product=86:54482, bound_value=99:20483, second_product=198:184211, answer=203:109390)
- Layer 27: `*q`, ` q`, `[q`, `$q`, `/q` (target ranks: base_value=43:99373, first_product=86:196267, bound_value=99:131072, second_product=198:178843, answer=203:79226)
- Layer 28: ` q`, `*q`, `[q`, `/q`, `$q` (target ranks: base_value=43:143635, first_product=86:195646, bound_value=99:69206, second_product=198:21759, answer=203:3467)
- Layer 29: ` q`, `[q`, `*q`, `/q`, `群` (target ranks: base_value=43:55037, first_product=86:201138, bound_value=99:71145, second_product=198:834, answer=203:71)
- Layer 30: ` q`, ` .`, `q`, `,q`, `(q` (target ranks: base_value=43:4471, first_product=86:14613, bound_value=99:12536, second_product=198:7, answer=203:8)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` :`, ` ```` (target ranks: base_value=43:515, first_product=86:815, bound_value=99:446, second_product=198:174, answer=203:223)

### Filler position 26 (absolute token 902, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:118, first_product=86:171, bound_value=99:149, second_product=198:20, answer=203:41)
- Layer 8: `u`, `↵`, `t`, ` t`, `s` (target ranks: base_value=43:12865, first_product=86:8877, bound_value=99:9462, second_product=198:703, answer=203:4261)
- Layer 16: `漫`, `望`, `内`, `白`, `ာ` (target ranks: base_value=43:21609, first_product=86:12682, bound_value=99:56275, second_product=198:4381, answer=203:5084)
- Layer 24: `longleftrightarrow`, `之`, `cket`, `ာ`, `յ` (target ranks: base_value=43:190655, first_product=86:170019, bound_value=99:175483, second_product=198:210171, answer=203:177637)
- Layer 25: `longleftrightarrow`, `cket`, `յ`, `�`, `之` (target ranks: base_value=43:180535, first_product=86:141603, bound_value=99:147887, second_product=198:195313, answer=203:166971)
- Layer 26: `յ`, `longleftrightarrow`, `最新发布`, `ာ`, ` .` (target ranks: base_value=43:185413, first_product=86:141615, bound_value=99:150348, second_product=198:231736, answer=203:193991)
- Layer 27: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=43:90220, first_product=86:148557, bound_value=99:116534, second_product=198:147386, answer=203:117134)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=43:48569, first_product=86:66529, bound_value=99:62383, second_product=198:92984, answer=203:64838)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=43:2519, first_product=86:10743, bound_value=99:8856, second_product=198:5519, answer=203:3563)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:170, first_product=86:780, bound_value=99:955, second_product=198:729, answer=203:185)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, `↵` (target ranks: base_value=43:41, first_product=86:215, bound_value=99:119, second_product=198:141, answer=203:97)

### Filler position 27 (absolute token 903, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:116, first_product=86:169, bound_value=99:148, second_product=198:20, answer=203:41)
- Layer 8: `↵`, `t`, `了`, `u`, `s` (target ranks: base_value=43:3004, first_product=86:3058, bound_value=99:1575, second_product=198:231, answer=203:652)
- Layer 16: `禁`, `再`, `市`, `ած`, `imensional` (target ranks: base_value=43:17954, first_product=86:30388, bound_value=99:73782, second_product=198:4403, answer=203:4571)
- Layer 24: `λεί`, `刺激`, `�`, ` con`, `位` (target ranks: base_value=43:211361, first_product=86:1973, bound_value=99:25224, second_product=198:233461, answer=203:235737)
- Layer 25: `�`, `刺激`, `спен`, `崎`, `λεί` (target ranks: base_value=43:140304, first_product=86:7537, bound_value=99:5409, second_product=198:201928, answer=203:179944)
- Layer 26: `一百`, `两百`, ` Afinal`, `�`, `九十` (target ranks: base_value=43:220604, first_product=86:124299, bound_value=99:5939, second_product=198:150103, answer=203:169450)
- Layer 27: `十九`, `inete`, `十九章`, `第二百零`, ` nineteen` (target ranks: base_value=43:242618, first_product=86:248165, bound_value=99:24551, second_product=198:18152, answer=203:16748)
- Layer 28: `十九`, `inete`, ` nineteen`, ` nineteenth`, `十九章` (target ranks: base_value=43:223135, first_product=86:247733, bound_value=99:90082, second_product=198:3183, answer=203:1754)
- Layer 29: `inete`, `一九`, ` nineteenth`, `十九`, `十九章` (target ranks: base_value=43:220353, first_product=86:212728, bound_value=99:187129, second_product=198:1195, answer=203:5802)
- Layer 30: `inete`, `第二百零`, `审`, `第一百`, ` sb` (target ranks: base_value=43:160068, first_product=86:122599, bound_value=99:209909, second_product=198:6, answer=203:329)
- Layer 31: ` .`, `.`, ` ,`, ` :`, `．` (target ranks: base_value=43:12632, first_product=86:17516, bound_value=99:78623, second_product=198:6280, answer=203:17805)

### Filler position 28 (absolute token 904, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:116, first_product=86:171, bound_value=99:148, second_product=198:20, answer=203:41)
- Layer 8: `�`, `o`, `�`, `↵`, `о` (target ranks: base_value=43:6593, first_product=86:5312, bound_value=99:5465, second_product=198:90, answer=203:973)
- Layer 16: `漫`, `再`, `禁`, `密`, `望` (target ranks: base_value=43:40733, first_product=86:40030, bound_value=99:89459, second_product=198:20655, answer=203:9539)
- Layer 24: `itics`, `了`, `iteli`, `ujući`, `յ` (target ranks: base_value=43:150432, first_product=86:168429, bound_value=99:170294, second_product=198:208592, answer=203:136518)
- Layer 25: `յ`, `itics`, `ujući`, `�`, `ож` (target ranks: base_value=43:134443, first_product=86:149505, bound_value=99:146893, second_product=198:201824, answer=203:124311)
- Layer 26: ` .`, `最新发布`, `�`, `ож`, `յ` (target ranks: base_value=43:89883, first_product=86:102554, bound_value=99:106454, second_product=198:188184, answer=203:85386)
- Layer 27: ` .`, ` ..`, `-.`, `．`, ` .=` (target ranks: base_value=43:65517, first_product=86:157693, bound_value=99:142889, second_product=198:174173, answer=203:92505)
- Layer 28: ` .`, `．`, `-.`, ` ..`, `!.` (target ranks: base_value=43:63545, first_product=86:69366, bound_value=99:112402, second_product=198:165359, answer=203:93180)
- Layer 29: ` .`, `．`, `-.`, `·`, `!.` (target ranks: base_value=43:5636, first_product=86:23520, bound_value=99:45365, second_product=198:31237, answer=203:10314)
- Layer 30: ` .`, ` ..`, ` ,`, ` `.`, ` ·` (target ranks: base_value=43:256, first_product=86:1402, bound_value=99:6155, second_product=198:2121, answer=203:283)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, `↵↵`, ` ..` (target ranks: base_value=43:61, first_product=86:175, bound_value=99:163, second_product=198:160, answer=203:101)

### Filler position 29 (absolute token 905, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:113, first_product=86:171, bound_value=99:148, second_product=198:20, answer=203:41)
- Layer 8: `o`, `�`, `�`, `↵`, `u` (target ranks: base_value=43:23982, first_product=86:20818, bound_value=99:14553, second_product=198:215, answer=203:2914)
- Layer 16: `漫`, `内`, `iti`, `信`, `曜` (target ranks: base_value=43:34785, first_product=86:13770, bound_value=99:62942, second_product=198:4404, answer=203:5212)
- Layer 24: `յ`, `yta`, `ек`, `longleftrightarrow`, `之` (target ranks: base_value=43:195090, first_product=86:180960, bound_value=99:177782, second_product=198:226558, answer=203:203972)
- Layer 25: `յ`, `ек`, `cket`, `viders`, `之` (target ranks: base_value=43:175659, first_product=86:140487, bound_value=99:128581, second_product=198:206952, answer=203:175158)
- Layer 26: `յ`, `ек`, ` .`, `uks`, `erness` (target ranks: base_value=43:124496, first_product=86:113562, bound_value=99:104415, second_product=198:214545, answer=203:155240)
- Layer 27: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:88734, first_product=86:163493, bound_value=99:138254, second_product=198:175179, answer=203:141811)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `/.` (target ranks: base_value=43:42782, first_product=86:72406, bound_value=99:95760, second_product=198:133157, answer=203:88212)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `/.` (target ranks: base_value=43:1566, first_product=86:9399, bound_value=99:15450, second_product=198:7475, answer=203:4205)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=43:121, first_product=86:664, bound_value=99:1315, second_product=198:812, answer=203:166)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=43:39, first_product=86:148, bound_value=99:126, second_product=198:120, answer=203:61)

### Filler position 30 (absolute token 906, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:113, first_product=86:170, bound_value=99:148, second_product=198:20, answer=203:41)
- Layer 8: `o`, `�`, `↵`, `u`, `↵↵` (target ranks: base_value=43:6891, first_product=86:4867, bound_value=99:4962, second_product=198:325, answer=203:1280)
- Layer 16: `漫`, `内`, `白`, `ights`, `ာ` (target ranks: base_value=43:57287, first_product=86:24182, bound_value=99:97143, second_product=198:8098, answer=203:7610)
- Layer 24: `longleftrightarrow`, `յ`, `之`, `ာ`, `kelse` (target ranks: base_value=43:220952, first_product=86:211392, bound_value=99:200244, second_product=198:225721, answer=203:217971)
- Layer 25: `յ`, `之`, `longleftrightarrow`, `�`, ` .` (target ranks: base_value=43:208187, first_product=86:186498, bound_value=99:166915, second_product=198:202819, answer=203:201190)
- Layer 26: `յ`, `imensional`, `longleftrightarrow`, `ာ`, `之` (target ranks: base_value=43:181865, first_product=86:159191, bound_value=99:138623, second_product=198:221612, answer=203:200137)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, `-.` (target ranks: base_value=43:115573, first_product=86:186638, bound_value=99:145922, second_product=198:164101, answer=203:149984)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=43:82142, first_product=86:99670, bound_value=99:107061, second_product=198:121745, answer=203:108166)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `.` (target ranks: base_value=43:5920, first_product=86:18108, bound_value=99:22321, second_product=198:9582, answer=203:8469)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:820, first_product=86:2876, bound_value=99:5157, second_product=198:3976, answer=203:1013)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:71, first_product=86:210, bound_value=99:160, second_product=198:149, answer=203:104)

### Filler position 31 (absolute token 907, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:115, first_product=86:171, bound_value=99:148, second_product=198:20, answer=203:41)
- Layer 8: `�`, `o`, `↵`, `u`, `↵↵` (target ranks: base_value=43:9149, first_product=86:6034, bound_value=99:5909, second_product=198:290, answer=203:1172)
- Layer 16: `漫`, `内`, `提`, `ံ`, `再` (target ranks: base_value=43:43152, first_product=86:22945, bound_value=99:70015, second_product=198:5093, answer=203:4403)
- Layer 24: `յ`, `longleftrightarrow`, `kelse`, `ံ`, `yta` (target ranks: base_value=43:224849, first_product=86:233845, bound_value=99:217925, second_product=198:240042, answer=203:215320)
- Layer 25: `յ`, `longleftrightarrow`, `之`, `ံ`, `�` (target ranks: base_value=43:205270, first_product=86:212037, bound_value=99:184803, second_product=198:222954, answer=203:189745)
- Layer 26: `յ`, `uks`, ` .`, `longleftrightarrow`, `scht` (target ranks: base_value=43:160366, first_product=86:197242, bound_value=99:162651, second_product=198:227340, answer=203:175730)
- Layer 27: ` .`, ` `.`, `．`, ` .=`, `-.` (target ranks: base_value=43:118865, first_product=86:224008, bound_value=99:197718, second_product=198:203338, answer=203:178768)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:75930, first_product=86:146956, bound_value=99:153830, second_product=198:156117, answer=203:125238)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:4454, first_product=86:44512, bound_value=99:40631, second_product=198:15247, answer=203:9730)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:369, first_product=86:4163, bound_value=99:5799, second_product=198:3132, answer=203:765)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:50, first_product=86:253, bound_value=99:209, second_product=198:177, answer=203:111)

### Filler position 32 (absolute token 908, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:109, first_product=86:169, bound_value=99:147, second_product=198:20, answer=203:40)
- Layer 8: `o`, `�`, `↵`, `u`, `s` (target ranks: base_value=43:8131, first_product=86:7411, bound_value=99:6090, second_product=198:250, answer=203:1856)
- Layer 16: `漫`, `吐`, `↵`, `望`, `内` (target ranks: base_value=43:27364, first_product=86:25115, bound_value=99:58182, second_product=198:10027, answer=203:8302)
- Layer 24: `յ`, `longleftrightarrow`, `égr`, `ож`, `yta` (target ranks: base_value=43:232263, first_product=86:238966, bound_value=99:234020, second_product=198:243642, answer=203:207068)
- Layer 25: `յ`, `égr`, `ож`, `longleftrightarrow`, `ီ` (target ranks: base_value=43:220875, first_product=86:225119, bound_value=99:213049, second_product=198:236455, answer=203:190594)
- Layer 26: `յ`, `uks`, `ож`, `longleftrightarrow`, `viders` (target ranks: base_value=43:209262, first_product=86:229644, bound_value=99:212452, second_product=198:244172, answer=203:197325)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .=` (target ranks: base_value=43:141385, first_product=86:234276, bound_value=99:206479, second_product=198:226241, answer=203:173678)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:92214, first_product=86:153421, bound_value=99:155636, second_product=198:186653, answer=203:112615)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `().` (target ranks: base_value=43:9623, first_product=86:65824, bound_value=99:52125, second_product=198:40503, answer=203:13457)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, ` .$` (target ranks: base_value=43:731, first_product=86:10915, bound_value=99:10553, second_product=198:8912, answer=203:1228)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:55, first_product=86:381, bound_value=99:226, second_product=198:201, answer=203:82)

### Filler position 33 (absolute token 909, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:109, first_product=86:169, bound_value=99:147, second_product=198:20, answer=203:40)
- Layer 8: `�`, `↵`, `u`, `o`, `�` (target ranks: base_value=43:3115, first_product=86:4005, bound_value=99:3379, second_product=198:219, answer=203:872)
- Layer 16: `内`, `长`, `佩`, `漫`, `吐` (target ranks: base_value=43:28434, first_product=86:24460, bound_value=99:33279, second_product=198:2806, answer=203:4109)
- Layer 24: `յ`, `之`, `longleftrightarrow`, ` .`, `égr` (target ranks: base_value=43:178448, first_product=86:199500, bound_value=99:179438, second_product=198:206829, answer=203:186003)
- Layer 25: `յ`, ` .`, `之`, `�`, `�` (target ranks: base_value=43:163012, first_product=86:175061, bound_value=99:141023, second_product=198:178606, answer=203:163588)
- Layer 26: `յ`, ` .`, `erness`, ` .$`, `的那些` (target ranks: base_value=43:147438, first_product=86:177589, bound_value=99:134887, second_product=198:217444, answer=203:180401)
- Layer 27: ` .`, ` `.`, `．`, `/.`, ` .$` (target ranks: base_value=43:98099, first_product=86:194780, bound_value=99:156444, second_product=198:172523, answer=203:151966)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:63464, first_product=86:106867, bound_value=99:122426, second_product=198:144545, answer=203:122996)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `/.` (target ranks: base_value=43:4752, first_product=86:28917, bound_value=99:32602, second_product=198:19091, answer=203:15068)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, `/.` (target ranks: base_value=43:258, first_product=86:2902, bound_value=99:3403, second_product=198:2369, answer=203:480)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=43:51, first_product=86:388, bound_value=99:231, second_product=198:170, answer=203:103)

### Filler position 34 (absolute token 910, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:110, first_product=86:169, bound_value=99:147, second_product=198:20, answer=203:40)
- Layer 8: `�`, `o`, `↵`, `杈`, `↵↵` (target ranks: base_value=43:4940, first_product=86:4679, bound_value=99:5791, second_product=198:126, answer=203:995)
- Layer 16: `内`, `长`, `ights`, `漫`, `三` (target ranks: base_value=43:45678, first_product=86:11439, bound_value=99:41425, second_product=198:5543, answer=203:3558)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `elage`, `最新发布` (target ranks: base_value=43:228539, first_product=86:217558, bound_value=99:202138, second_product=198:241250, answer=203:235979)
- Layer 25: `յ`, `longleftrightarrow`, ` .`, `之`, `dddd` (target ranks: base_value=43:225773, first_product=86:206416, bound_value=99:177155, second_product=198:232747, answer=203:228022)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `最新发布`, `dddd` (target ranks: base_value=43:212535, first_product=86:211225, bound_value=99:178263, second_product=198:241976, answer=203:233030)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=43:181145, first_product=86:229145, bound_value=99:203045, second_product=198:228319, answer=203:216248)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:133762, first_product=86:160582, bound_value=99:170066, second_product=198:204895, answer=203:188798)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:16605, first_product=86:58355, bound_value=99:57497, second_product=198:49116, answer=203:38936)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:693, first_product=86:5298, bound_value=99:7317, second_product=198:6786, answer=203:1566)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, `↵`, ` ` (target ranks: base_value=43:48, first_product=86:257, bound_value=99:188, second_product=198:145, answer=203:77)

### Filler position 35 (absolute token 911, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:106, first_product=86:169, bound_value=99:147, second_product=198:20, answer=203:40)
- Layer 8: `o`, `�`, `↵`, `↵↵`, `u` (target ranks: base_value=43:11837, first_product=86:7970, bound_value=99:8182, second_product=198:130, answer=203:1741)
- Layer 16: `内`, `ာ`, `ံ`, `ights`, `长` (target ranks: base_value=43:81648, first_product=86:19842, bound_value=99:63652, second_product=198:10494, answer=203:5123)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `yta`, `kelse` (target ranks: base_value=43:222333, first_product=86:205072, bound_value=99:204293, second_product=198:239747, answer=203:237410)
- Layer 25: `յ`, `之`, `longleftrightarrow`, `viders`, `kelse` (target ranks: base_value=43:207416, first_product=86:178083, bound_value=99:168324, second_product=198:225623, answer=203:222702)
- Layer 26: `յ`, `viders`, `longleftrightarrow`, `ာ`, `kelse` (target ranks: base_value=43:189793, first_product=86:185334, bound_value=99:169290, second_product=198:239402, answer=203:227552)
- Layer 27: ` .`, ` `.`, `．`, `/.`, `-.` (target ranks: base_value=43:138683, first_product=86:201685, bound_value=99:180482, second_product=198:208179, answer=203:205399)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:74997, first_product=86:103147, bound_value=99:133159, second_product=198:167849, answer=203:163093)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:4729, first_product=86:24406, bound_value=99:32640, second_product=198:18986, answer=203:18246)
- Layer 30: ` .`, ` `.`, ` ..`, ` ,`, ` .$` (target ranks: base_value=43:283, first_product=86:2216, bound_value=99:4177, second_product=198:3341, answer=203:846)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ,` (target ranks: base_value=43:53, first_product=86:249, bound_value=99:270, second_product=198:228, answer=203:156)

### Filler position 36 (absolute token 912, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:107, first_product=86:169, bound_value=99:147, second_product=198:20, answer=203:40)
- Layer 8: `o`, `↵`, `�`, `↵↵`, `sn` (target ranks: base_value=43:5655, first_product=86:3896, bound_value=99:3974, second_product=198:239, answer=203:986)
- Layer 16: `ံ`, `内`, `漫`, `ာ`, `蓬` (target ranks: base_value=43:78025, first_product=86:19082, bound_value=99:69104, second_product=198:10848, answer=203:7266)
- Layer 24: `յ`, `longleftrightarrow`, `ights`, `ာ`, `yta` (target ranks: base_value=43:239788, first_product=86:236852, bound_value=99:229952, second_product=198:244900, answer=203:241835)
- Layer 25: `յ`, `longleftrightarrow`, `�`, `ာ`, `之` (target ranks: base_value=43:229884, first_product=86:219985, bound_value=99:201519, second_product=198:236314, answer=203:232581)
- Layer 26: `յ`, `ာ`, `longleftrightarrow`, `antium`, `xdd` (target ranks: base_value=43:212102, first_product=86:211445, bound_value=99:183552, second_product=198:242222, answer=203:229730)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `-.` (target ranks: base_value=43:145111, first_product=86:215749, bound_value=99:180461, second_product=198:204715, answer=203:190386)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=43:85301, first_product=86:129209, bound_value=99:131554, second_product=198:155089, answer=203:133727)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:9125, first_product=86:43136, bound_value=99:35670, second_product=198:23075, answer=203:16631)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:1062, first_product=86:6714, bound_value=99:8167, second_product=198:7993, answer=203:2341)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` `, `↵↵` (target ranks: base_value=43:67, first_product=86:300, bound_value=99:224, second_product=198:220, answer=203:142)

### Filler position 37 (absolute token 913, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:105, first_product=86:168, bound_value=99:148, second_product=198:20, answer=203:40)
- Layer 8: `�`, `o`, `om`, `↵↵`, `о` (target ranks: base_value=43:13667, first_product=86:7671, bound_value=99:5772, second_product=198:418, answer=203:1337)
- Layer 16: `内`, `佩`, `ံ`, `漫`, `յ` (target ranks: base_value=43:62939, first_product=86:21785, bound_value=99:52205, second_product=198:8396, answer=203:4909)
- Layer 24: `յ`, `longleftrightarrow`, `ီ`, `ા`, `yta` (target ranks: base_value=43:233282, first_product=86:239038, bound_value=99:229418, second_product=198:244927, answer=203:229002)
- Layer 25: `յ`, `ီ`, `之`, `longleftrightarrow`, `ackers` (target ranks: base_value=43:213070, first_product=86:218640, bound_value=99:197594, second_product=198:236261, answer=203:206601)
- Layer 26: `յ`, `usercontent`, `ီ`, `ackers`, `uks` (target ranks: base_value=43:195303, first_product=86:220675, bound_value=99:189784, second_product=198:243926, answer=203:209658)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=43:146379, first_product=86:229327, bound_value=99:209331, second_product=198:221054, answer=203:187110)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:88717, first_product=86:144135, bound_value=99:164739, second_product=198:176862, answer=203:126990)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:8262, first_product=86:57264, bound_value=99:52927, second_product=198:29433, answer=203:13600)
- Layer 30: ` .`, ` `.`, ` ..`, ` .$`, ` ,` (target ranks: base_value=43:694, first_product=86:6744, bound_value=99:7846, second_product=198:6508, answer=203:1525)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:56, first_product=86:315, bound_value=99:286, second_product=198:211, answer=203:103)

### Filler position 38 (absolute token 914, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:105, first_product=86:168, bound_value=99:148, second_product=198:20, answer=203:40)
- Layer 8: `o`, `�`, `u`, `杈`, `↵` (target ranks: base_value=43:17739, first_product=86:11861, bound_value=99:11058, second_product=198:345, answer=203:2828)
- Layer 16: `↵`, `佩`, `吐`, `漫`, `三` (target ranks: base_value=43:47603, first_product=86:10485, bound_value=99:41997, second_product=198:5556, answer=203:5722)
- Layer 24: `յ`, `cket`, `longleftrightarrow`, `ာ`, `itical` (target ranks: base_value=43:213965, first_product=86:225637, bound_value=99:221408, second_product=198:239232, answer=203:207313)
- Layer 25: `յ`, `cket`, `之`, `ား`, `itical` (target ranks: base_value=43:191292, first_product=86:198331, bound_value=99:189432, second_product=198:223027, answer=203:181246)
- Layer 26: `յ`, `ာ`, `uks`, `�`, `ож` (target ranks: base_value=43:194063, first_product=86:217238, bound_value=99:197230, second_product=198:242865, answer=203:202588)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .=` (target ranks: base_value=43:119308, first_product=86:216220, bound_value=99:187197, second_product=198:205437, answer=203:152243)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:64050, first_product=86:110228, bound_value=99:136041, second_product=198:156602, answer=203:95843)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `().` (target ranks: base_value=43:5695, first_product=86:36953, bound_value=99:42124, second_product=198:26825, answer=203:12046)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ."` (target ranks: base_value=43:728, first_product=86:8044, bound_value=99:10052, second_product=198:9367, answer=203:1595)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:54, first_product=86:359, bound_value=99:283, second_product=198:222, answer=203:100)

### Filler position 39 (absolute token 915, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:106, first_product=86:168, bound_value=99:148, second_product=198:20, answer=203:38)
- Layer 8: `o`, `�`, `↵`, `s`, `u` (target ranks: base_value=43:6603, first_product=86:7610, bound_value=99:6201, second_product=198:375, answer=203:1777)
- Layer 16: `佩`, `内`, `提`, `长`, `往` (target ranks: base_value=43:38888, first_product=86:13337, bound_value=99:29045, second_product=198:3567, answer=203:4444)
- Layer 24: `յ`, `之`, `ာ`, `ား`, `longleftrightarrow` (target ranks: base_value=43:139794, first_product=86:169388, bound_value=99:145920, second_product=198:193376, answer=203:162674)
- Layer 25: `յ`, `之`, ` .`, `�`, `ား` (target ranks: base_value=43:120619, first_product=86:138179, bound_value=99:103999, second_product=198:155402, answer=203:132157)
- Layer 26: `յ`, ` .`, `之`, `ီ`, `的那些` (target ranks: base_value=43:98736, first_product=86:140915, bound_value=99:97345, second_product=198:201185, answer=203:147345)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=43:73944, first_product=86:164505, bound_value=99:144826, second_product=198:161289, answer=203:124150)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:37061, first_product=86:73901, bound_value=99:112574, second_product=198:127990, answer=203:89727)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:2058, first_product=86:14412, bound_value=99:25946, second_product=198:13482, answer=203:7319)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:188, first_product=86:1798, bound_value=99:3492, second_product=198:2472, answer=203:405)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=43:40, first_product=86:280, bound_value=99:308, second_product=198:184, answer=203:104)

### Filler position 40 (absolute token 916, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:103, first_product=86:168, bound_value=99:145, second_product=198:20, answer=203:38)
- Layer 8: `o`, `�`, `↵`, `↵↵`, `�` (target ranks: base_value=43:6836, first_product=86:10876, bound_value=99:9002, second_product=198:235, answer=203:1166)
- Layer 16: `内`, `三`, `白`, `博`, `避` (target ranks: base_value=43:42017, first_product=86:12614, bound_value=99:21361, second_product=198:7436, answer=203:3551)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ာ`, `ား` (target ranks: base_value=43:204211, first_product=86:216809, bound_value=99:191738, second_product=198:237714, answer=203:220437)
- Layer 25: `յ`, `longleftrightarrow`, `之`, `ား`, ` .` (target ranks: base_value=43:195654, first_product=86:201748, bound_value=99:161780, second_product=198:225907, answer=203:207184)
- Layer 26: `յ`, `longleftrightarrow`, `ာ`, `viders`, ` .` (target ranks: base_value=43:163552, first_product=86:206797, bound_value=99:160772, second_product=198:237673, answer=203:210220)
- Layer 27: ` .`, ` `.`, `．`, ` .=`, ` .$` (target ranks: base_value=43:140030, first_product=86:228246, bound_value=99:204298, second_product=198:226512, answer=203:196042)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:87620, first_product=86:152912, bound_value=99:169221, second_product=198:196421, answer=203:151302)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:8509, first_product=86:52272, bound_value=99:58206, second_product=198:45329, answer=203:24530)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:475, first_product=86:4686, bound_value=99:8473, second_product=198:7555, answer=203:1374)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, `↵`, ` ` (target ranks: base_value=43:38, first_product=86:242, bound_value=99:262, second_product=198:170, answer=203:84)

### Filler position 41 (absolute token 917, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:105, first_product=86:168, bound_value=99:144, second_product=198:20, answer=203:38)
- Layer 8: `o`, `�`, `↵`, `↵↵`, `杈` (target ranks: base_value=43:8413, first_product=86:6325, bound_value=99:10356, second_product=198:159, answer=203:1538)
- Layer 16: `内`, `三`, `atur`, `ာ`, `长` (target ranks: base_value=43:41219, first_product=86:6966, bound_value=99:23280, second_product=198:3621, answer=203:2351)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ား`, `ာ` (target ranks: base_value=43:173976, first_product=86:189222, bound_value=99:182325, second_product=198:221202, answer=203:209095)
- Layer 25: `յ`, `之`, `longleftrightarrow`, `ား`, `ီ` (target ranks: base_value=43:141300, first_product=86:148722, bound_value=99:130173, second_product=198:188069, answer=203:175624)
- Layer 26: `յ`, `ီ`, `kelse`, `ာ`, `viders` (target ranks: base_value=43:123219, first_product=86:167609, bound_value=99:139458, second_product=198:221606, answer=203:187324)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=43:77159, first_product=86:179391, bound_value=99:162716, second_product=198:182591, answer=203:165817)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:23762, first_product=86:75963, bound_value=99:110775, second_product=198:131675, answer=203:116560)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:958, first_product=86:14419, bound_value=99:25304, second_product=198:11359, answer=203:9147)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:100, first_product=86:1260, bound_value=99:2889, second_product=198:2300, answer=203:494)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ,` (target ranks: base_value=43:25, first_product=86:223, bound_value=99:292, second_product=198:229, answer=203:149)

### Filler position 42 (absolute token 918, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:145, second_product=198:20, answer=203:38)
- Layer 8: `↵`, `o`, `↵↵`, `�`, `;` (target ranks: base_value=43:3800, first_product=86:3100, bound_value=99:3223, second_product=198:161, answer=203:709)
- Layer 16: `内`, `ံ`, `三`, `提`, `避` (target ranks: base_value=43:42630, first_product=86:10670, bound_value=99:38597, second_product=198:7948, answer=203:4735)
- Layer 24: `յ`, `ာ`, `ား`, `longleftrightarrow`, `之` (target ranks: base_value=43:210920, first_product=86:225666, bound_value=99:211577, second_product=198:238460, answer=203:231731)
- Layer 25: `յ`, `ား`, `ာ`, `longleftrightarrow`, `之` (target ranks: base_value=43:195618, first_product=86:204928, bound_value=99:177435, second_product=198:223610, answer=203:219784)
- Layer 26: `յ`, `ာ`, `longleftrightarrow`, `ား`, `ા` (target ranks: base_value=43:163272, first_product=86:200894, bound_value=99:159615, second_product=198:238133, answer=203:220481)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, ` .=` (target ranks: base_value=43:82803, first_product=86:198511, bound_value=99:158152, second_product=198:182307, answer=203:166075)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=43:34553, first_product=86:106294, bound_value=99:112575, second_product=198:132051, answer=203:116581)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `/.` (target ranks: base_value=43:2006, first_product=86:23037, bound_value=99:24848, second_product=198:13403, answer=203:11548)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:263, first_product=86:3296, bound_value=99:5141, second_product=198:4615, answer=203:1527)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:34, first_product=86:225, bound_value=99:237, second_product=198:209, answer=203:138)

### Filler position 43 (absolute token 919, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:144, second_product=198:20, answer=203:38)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `om` (target ranks: base_value=43:6553, first_product=86:5321, bound_value=99:5131, second_product=198:222, answer=203:895)
- Layer 16: `内`, `提`, `ံ`, `与现实`, `佩` (target ranks: base_value=43:39085, first_product=86:15643, bound_value=99:33261, second_product=198:11980, answer=203:4602)
- Layer 24: `յ`, `longleftrightarrow`, `ာ`, `ા`, `kelse` (target ranks: base_value=43:215653, first_product=86:240644, bound_value=99:227537, second_product=198:245014, answer=203:220197)
- Layer 25: `յ`, `longleftrightarrow`, `ા`, `�`, `之` (target ranks: base_value=43:192529, first_product=86:226162, bound_value=99:200843, second_product=198:238963, answer=203:204737)
- Layer 26: `յ`, `ackers`, `usercontent`, `kelse`, `longleftrightarrow` (target ranks: base_value=43:164795, first_product=86:230254, bound_value=99:197734, second_product=198:245213, answer=203:211614)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `-.` (target ranks: base_value=43:110759, first_product=86:232680, bound_value=99:216381, second_product=198:225753, answer=203:182707)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:55164, first_product=86:167445, bound_value=99:176828, second_product=198:187316, answer=203:125246)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:3353, first_product=86:64757, bound_value=99:54477, second_product=198:30576, answer=203:12539)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ."` (target ranks: base_value=43:374, first_product=86:9357, bound_value=99:11517, second_product=198:9257, answer=203:2443)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:29, first_product=86:314, bound_value=99:324, second_product=198:180, answer=203:89)

### Filler position 44 (absolute token 920, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:145, second_product=198:20, answer=203:38)
- Layer 8: `o`, `�`, `杈`, `om`, `�` (target ranks: base_value=43:15767, first_product=86:11823, bound_value=99:12513, second_product=198:266, answer=203:1865)
- Layer 16: `提`, `佩`, `三`, `内`, `板` (target ranks: base_value=43:36376, first_product=86:8558, bound_value=99:33886, second_product=198:6793, answer=203:3230)
- Layer 24: `յ`, `longleftrightarrow`, `cket`, `ာ`, `之` (target ranks: base_value=43:163049, first_product=86:205910, bound_value=99:211094, second_product=198:234322, answer=203:167063)
- Layer 25: `յ`, `cket`, `ား`, `之`, `longleftrightarrow` (target ranks: base_value=43:140467, first_product=86:175948, bound_value=99:179618, second_product=198:222693, answer=203:146586)
- Layer 26: `յ`, `uks`, `ာ`, `viders`, `ackers` (target ranks: base_value=43:153131, first_product=86:211349, bound_value=99:202968, second_product=198:244008, answer=203:186857)
- Layer 27: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:91428, first_product=86:204082, bound_value=99:204082, second_product=198:213887, answer=203:133027)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:43554, first_product=86:104041, bound_value=99:160048, second_product=198:172150, answer=203:82699)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:2598, first_product=86:29243, bound_value=99:47618, second_product=198:26859, answer=203:6637)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=43:284, first_product=86:4456, bound_value=99:7701, second_product=198:6629, answer=203:985)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:29, first_product=86:244, bound_value=99:265, second_product=198:213, answer=203:75)

### Filler position 45 (absolute token 921, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:144, second_product=198:20, answer=203:38)
- Layer 8: `o`, `�`, `u`, `↵`, `杈` (target ranks: base_value=43:8126, first_product=86:8845, bound_value=99:10436, second_product=198:324, answer=203:2287)
- Layer 16: `内`, `提`, `佩`, `白`, `三` (target ranks: base_value=43:24321, first_product=86:9021, bound_value=99:23412, second_product=198:3664, answer=203:2638)
- Layer 24: `之`, `յ`, `ာ`, `ား`, `longleftrightarrow` (target ranks: base_value=43:103574, first_product=86:133682, bound_value=99:140462, second_product=198:171782, answer=203:129319)
- Layer 25: `յ`, `之`, `�`, `ား`, ` .` (target ranks: base_value=43:89689, first_product=86:102545, bound_value=99:96085, second_product=198:136141, answer=203:106505)
- Layer 26: `յ`, `之`, `ာ`, `erness`, ` .` (target ranks: base_value=43:68792, first_product=86:95680, bound_value=99:83448, second_product=198:182301, answer=203:116567)
- Layer 27: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:45693, first_product=86:114591, bound_value=99:132438, second_product=198:142785, answer=203:86029)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:18867, first_product=86:41141, bound_value=99:99674, second_product=198:105155, answer=203:57260)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:768, first_product=86:5107, bound_value=99:20106, second_product=198:8611, answer=203:3556)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:118, first_product=86:820, bound_value=99:2999, second_product=198:2036, answer=203:326)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=43:25, first_product=86:183, bound_value=99:280, second_product=198:193, answer=203:83)

### Filler position 46 (absolute token 922, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:145, second_product=198:20, answer=203:39)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `;` (target ranks: base_value=43:3886, first_product=86:6010, bound_value=99:5660, second_product=198:238, answer=203:968)
- Layer 16: `内`, `佩`, `提`, `白`, `三` (target ranks: base_value=43:41655, first_product=86:17689, bound_value=99:34902, second_product=198:14532, answer=203:6231)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ာ`, `�` (target ranks: base_value=43:149865, first_product=86:176548, bound_value=99:152272, second_product=198:214487, answer=203:197928)
- Layer 25: `յ`, `之`, `longleftrightarrow`, `�`, ` .` (target ranks: base_value=43:135923, first_product=86:151551, bound_value=99:117958, second_product=198:191490, answer=203:180499)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `之`, `imensional` (target ranks: base_value=43:101532, first_product=86:152574, bound_value=99:113241, second_product=198:216682, answer=203:188712)
- Layer 27: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:86113, first_product=86:188617, bound_value=99:178246, second_product=198:199592, answer=203:178246)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:52134, first_product=86:103164, bound_value=99:142441, second_product=198:159668, answer=203:136024)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=43:2944, first_product=86:18937, bound_value=99:34878, second_product=198:20987, answer=203:15834)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=43:265, first_product=86:2008, bound_value=99:6833, second_product=198:4832, answer=203:1215)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, `↵`, ` ..` (target ranks: base_value=43:32, first_product=86:185, bound_value=99:259, second_product=198:162, answer=203:103)

### Filler position 47 (absolute token 923, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:146, second_product=198:20, answer=203:37)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `杈` (target ranks: base_value=43:6337, first_product=86:5818, bound_value=99:7197, second_product=198:143, answer=203:1148)
- Layer 16: `内`, `atur`, `佩`, `振`, `ev` (target ranks: base_value=43:40600, first_product=86:11687, bound_value=99:33336, second_product=198:14941, answer=203:5412)
- Layer 24: `յ`, `viders`, `之`, `longleftrightarrow`, `ambda` (target ranks: base_value=43:130539, first_product=86:161129, bound_value=99:144096, second_product=198:213675, answer=203:172510)
- Layer 25: `յ`, `viders`, `之`, `longleftrightarrow`, `�` (target ranks: base_value=43:96227, first_product=86:121074, bound_value=99:93440, second_product=198:181449, answer=203:136648)
- Layer 26: `յ`, `viders`, `uks`, `ာ`, `longleftrightarrow` (target ranks: base_value=43:74965, first_product=86:132825, bound_value=99:94848, second_product=198:208671, answer=203:146028)
- Layer 27: ` .`, ` `.`, `．`, `/.`, `-.` (target ranks: base_value=43:64982, first_product=86:175554, bound_value=99:155075, second_product=198:205876, answer=203:165538)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:29795, first_product=86:76360, bound_value=99:99916, second_product=198:161551, answer=203:118704)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:1372, first_product=86:15433, bound_value=99:23254, second_product=198:20515, answer=203:10406)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=43:143, first_product=86:1452, bound_value=99:3045, second_product=198:3552, answer=203:776)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:24, first_product=86:168, bound_value=99:199, second_product=198:165, answer=203:99)

### Filler position 48 (absolute token 924, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:167, bound_value=99:146, second_product=198:20, answer=203:40)
- Layer 8: `o`, `�`, `↵`, `↵↵`, `om` (target ranks: base_value=43:6828, first_product=86:4798, bound_value=99:5009, second_product=198:153, answer=203:992)
- Layer 16: `内`, `佩`, `避`, `ာ`, `吐` (target ranks: base_value=43:33349, first_product=86:5925, bound_value=99:27669, second_product=198:8338, answer=203:3689)
- Layer 24: `ာ`, `之`, `յ`, `ား`, `allax` (target ranks: base_value=43:136088, first_product=86:151845, bound_value=99:164037, second_product=198:212885, answer=203:182259)
- Layer 25: `յ`, `之`, `allax`, `ာ`, `ား` (target ranks: base_value=43:115538, first_product=86:126891, bound_value=99:119217, second_product=198:184018, answer=203:162377)
- Layer 26: `ာ`, `յ`, `allax`, `uks`, `viders` (target ranks: base_value=43:112875, first_product=86:152687, bound_value=99:126785, second_product=198:229943, answer=203:193534)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=43:57787, first_product=86:146190, bound_value=99:104447, second_product=198:195395, answer=203:150072)
- Layer 28: ` .`, `-.`, `．`, ` `.`, ` ..` (target ranks: base_value=43:20534, first_product=86:58671, bound_value=99:69506, second_product=198:163366, answer=203:121361)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `().` (target ranks: base_value=43:949, first_product=86:10253, bound_value=99:13530, second_product=198:13720, answer=203:8465)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:105, first_product=86:1199, bound_value=99:1637, second_product=198:2351, answer=203:605)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, `↵↵`, ` ` (target ranks: base_value=43:20, first_product=86:179, bound_value=99:173, second_product=198:197, answer=203:152)

### Filler position 49 (absolute token 925, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:167, bound_value=99:146, second_product=198:20, answer=203:40)
- Layer 8: `�`, `o`, `om`, `↵↵`, `↵` (target ranks: base_value=43:10117, first_product=86:6579, bound_value=99:5194, second_product=198:301, answer=203:1272)
- Layer 16: `内`, `有`, `走`, `吐`, `提` (target ranks: base_value=43:17555, first_product=86:2850, bound_value=99:4579, second_product=198:2500, answer=203:1304)
- Layer 24: `յ`, `ား`, `ာ`, `း`, `ältä` (target ranks: base_value=43:104959, first_product=86:99268, bound_value=99:90803, second_product=198:199185, answer=203:154586)
- Layer 25: `յ`, `ား`, `ာ`, `之`, `�` (target ranks: base_value=43:59936, first_product=86:54929, bound_value=99:40388, second_product=198:150022, answer=203:106873)
- Layer 26: `յ`, `ာ`, ` .=`, `ား`, `️` (target ranks: base_value=43:48373, first_product=86:62008, bound_value=99:41463, second_product=198:220569, answer=203:160282)
- Layer 27: ` .`, `．`, ` ..`, `․`, ` .=` (target ranks: base_value=43:9755, first_product=86:16845, bound_value=99:9033, second_product=198:87132, answer=203:36668)
- Layer 28: ` .`, `．`, ` ..`, `․`, `️` (target ranks: base_value=43:3525, first_product=86:6050, bound_value=99:7278, second_product=198:69612, answer=203:30689)
- Layer 29: ` .`, `．`, `.`, ` ..`, `․` (target ranks: base_value=43:262, first_product=86:1254, bound_value=99:1594, second_product=198:2620, answer=203:1744)
- Layer 30: ` .`, ` ..`, ` ."`, `．`, `↵↵` (target ranks: base_value=43:53, first_product=86:198, bound_value=99:395, second_product=198:675, answer=203:251)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:19, first_product=86:81, bound_value=99:86, second_product=198:162, answer=203:114)

### Filler position 50 (absolute token 926, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:104, first_product=86:168, bound_value=99:145, second_product=198:20, answer=203:40)
- Layer 8: `�`, `o`, `om`, `杈`, `昊` (target ranks: base_value=43:24706, first_product=86:16195, bound_value=99:11415, second_product=198:499, answer=203:2682)
- Layer 16: `居`, `提`, `内`, `有`, `摸` (target ranks: base_value=43:40738, first_product=86:4354, bound_value=99:2848, second_product=198:3567, answer=203:5845)
- Layer 24: `↵↵`, `答案`, `ambda`, `(answer`, ` answer` (target ranks: base_value=43:79975, first_product=86:70900, bound_value=99:60928, second_product=198:132864, answer=203:105675)
- Layer 25: `↵↵`, `答案`, ` answer`, `Answer`, ` Answer` (target ranks: base_value=43:42673, first_product=86:32895, bound_value=99:25565, second_product=198:82997, answer=203:65478)
- Layer 26: `↵↵`, `答案`, `յ`, `ож`, `及答案` (target ranks: base_value=43:61626, first_product=86:50821, bound_value=99:49814, second_product=198:174700, answer=203:125173)
- Layer 27: ` Answer`, `Answer`, ` answer`, `↵↵`, `回答` (target ranks: base_value=43:37544, first_product=86:50332, bound_value=99:30806, second_product=198:66662, answer=203:38718)
- Layer 28: `↵↵`, ` Answer`, `Answer`, ` answer`, `回答` (target ranks: base_value=43:32025, first_product=86:20522, bound_value=99:15221, second_product=198:25493, answer=203:12321)
- Layer 29: `↵↵`, `Answer`, ` Answer`, ` answer`, `答案` (target ranks: base_value=43:539, first_product=86:909, bound_value=99:575, second_product=198:241, answer=203:161)
- Layer 30: `↵↵`, ` Answer`, `↵`, `Answer`, ` answer` (target ranks: base_value=43:59, first_product=86:81, bound_value=99:71, second_product=198:67, answer=203:63)
- Layer 31: `↵↵`, `<|im_end|>`, `↵`, ` ↵↵`, ` .` (target ranks: base_value=43:29, first_product=86:62, bound_value=99:42, second_product=198:20, answer=203:20)

## Exact rendered prompt

```text
<|im_start|>system
You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 50 filler tokens (a sequence of dots) before you answer.<|im_end|>
<|im_start|>user
zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
176<|im_end|>
<|im_start|>user
cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
59<|im_end|>
<|im_start|>user
gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
351<|im_end|>
<|im_start|>user
mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
229<|im_end|>
<|im_start|>user
kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
178<|im_end|>
<|im_start|>user
ruw = 43
mik = twice the number for ruw plus 13
los = twice the number for mik plus 27
qot = twice the number for mik plus 21
jez = twice the number for mik plus 16
Question: What is twice the number for mik plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
<think>

</think>


```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
