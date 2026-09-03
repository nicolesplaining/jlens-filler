# First qualitative filler readout

These are **logit-lens token readouts** (final norm + unembedding applied to each block's residual); no Jacobian lens was used.

## Outcome

- Filler answer: `113` (correct).
- No-filler answer: `113` (correct).
- Filler tokens: 50 tokens at absolute indices 876–925.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| Logit lens | `base_value=17` | 4 (L30, filler 9) | L30, filler 9 (rank 4) |
| Logit lens | `first_product=34` | 23 (L30, filler 5) | Never |
| Logit lens | `bound_value=50` | 4 (L30, filler 17) | L30, filler 17 (rank 4) |
| Logit lens | `second_product=100` | 4 (L30, filler 9) | L30, filler 9 (rank 4) |
| Logit lens | `answer=113` | 4 (L30, filler 9) | L30, filler 9 (rank 4) |

## Logit lens top-5 by filler position

### Filler position 1 (absolute token 876, surface ` .`)

- Layer 0: ` `, `-`, `s`, `<|endoftext|>`, `↵` (target ranks: base_value=17:26, first_product=34:115, bound_value=50:302, second_product=100:26, answer=113:26)
- Layer 8: `o`, `ot`, `该`, `以`, `�` (target ranks: base_value=17:822, first_product=34:1613, bound_value=50:1962, second_product=100:822, answer=113:822)
- Layer 16: `沉`, `漫`, `内`, `յ`, `走` (target ranks: base_value=17:8928, first_product=34:9589, bound_value=50:11664, second_product=100:8928, answer=113:8928)
- Layer 24: `longleftrightarrow`, `cket`, `յ`, `utando`, `pickle` (target ranks: base_value=17:230890, first_product=34:225798, bound_value=50:170844, second_product=100:230890, answer=113:230890)
- Layer 25: ` .`, `յ`, `cket`, `longleftrightarrow`, `DOCTYPE` (target ranks: base_value=17:205397, first_product=34:207572, bound_value=50:131434, second_product=100:205397, answer=113:205397)
- Layer 26: ` .`, ` dot`, `-dot`, `յ`, ` '.',` (target ranks: base_value=17:195717, first_product=34:165096, bound_value=50:119216, second_product=100:195717, answer=113:195717)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:221504, first_product=34:231066, bound_value=50:190542, second_product=100:221504, answer=113:221504)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:147237, first_product=34:134139, bound_value=50:84992, second_product=100:147237, answer=113:147237)
- Layer 29: ` .`, `-.`, ` `.`, `!.`, `．` (target ranks: base_value=17:10661, first_product=34:12359, bound_value=50:3157, second_product=100:10661, answer=113:10661)
- Layer 30: ` .`, ` ..`, ` `.`, `-.`, ` :` (target ranks: base_value=17:723, first_product=34:509, bound_value=50:306, second_product=100:723, answer=113:723)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` `, ` `.` (target ranks: base_value=17:76, first_product=34:177, bound_value=50:137, second_product=100:76, answer=113:76)

### Filler position 2 (absolute token 877, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `_` (target ranks: base_value=17:21, first_product=34:171, bound_value=50:297, second_product=100:21, answer=113:21)
- Layer 8: `o`, `地`, `u`, `�`, `以` (target ranks: base_value=17:1367, first_product=34:4998, bound_value=50:5371, second_product=100:1367, answer=113:1367)
- Layer 16: `消`, `漫`, `�`, `繁`, `波` (target ranks: base_value=17:56096, first_product=34:64810, bound_value=50:86914, second_product=100:56096, answer=113:56096)
- Layer 24: `longleftrightarrow`, `ី`, `pickle`, `itudes`, `ံ` (target ranks: base_value=17:239579, first_product=34:234506, bound_value=50:218086, second_product=100:239579, answer=113:239579)
- Layer 25: ` .`, `longleftrightarrow`, `ံ`, `子`, `之` (target ranks: base_value=17:230730, first_product=34:227222, bound_value=50:198120, second_product=100:230730, answer=113:230730)
- Layer 26: ` .`, `յ`, `冀`, `根据权利要求`, ` '.',` (target ranks: base_value=17:241044, first_product=34:219563, bound_value=50:206924, second_product=100:241044, answer=113:241044)
- Layer 27: ` .`, ` `.`, `．`, `/.`, ` .$` (target ranks: base_value=17:221444, first_product=34:221958, bound_value=50:179781, second_product=100:221444, answer=113:221444)
- Layer 28: ` .`, ` `.`, `-.`, `/.`, `．` (target ranks: base_value=17:170213, first_product=34:129652, bound_value=50:99331, second_product=100:170213, answer=113:170213)
- Layer 29: ` .`, `-.`, ` `.`, `/.`, `．` (target ranks: base_value=17:17937, first_product=34:13679, bound_value=50:6945, second_product=100:17937, answer=113:17937)
- Layer 30: ` .`, ` ..`, ` `.`, `/.`, `-.` (target ranks: base_value=17:4726, first_product=34:1635, bound_value=50:1023, second_product=100:4726, answer=113:4726)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` `, ` `.` (target ranks: base_value=17:174, first_product=34:225, bound_value=50:148, second_product=100:174, answer=113:174)

### Filler position 3 (absolute token 878, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:21, first_product=34:174, bound_value=50:305, second_product=100:21, answer=113:21)
- Layer 8: `is`, `in`, `�`, `d`, `are` (target ranks: base_value=17:2038, first_product=34:30791, bound_value=50:17888, second_product=100:2038, answer=113:2038)
- Layer 16: `站`, `翰`, `担`, `out`, `立` (target ranks: base_value=17:8006, first_product=34:62041, bound_value=50:24891, second_product=100:8006, answer=113:8006)
- Layer 24: `吁`, `四十`, `ит`, `erre`, `闲` (target ranks: base_value=17:247341, first_product=34:88798, bound_value=50:216455, second_product=100:247341, answer=113:247341)
- Layer 25: `吁`, `七十`, `cribe`, ` seventy`, `ит` (target ranks: base_value=17:233506, first_product=34:81697, bound_value=50:185255, second_product=100:233506, answer=113:233506)
- Layer 26: `enang`, `吁`, `onders`, `спен`, `uple` (target ranks: base_value=17:209654, first_product=34:201561, bound_value=50:186280, second_product=100:209654, answer=113:209654)
- Layer 27: `九十`, ` ninety`, `八十`, ` eighty`, `roid` (target ranks: base_value=17:243341, first_product=34:248319, bound_value=50:241115, second_product=100:243341, answer=113:243341)
- Layer 28: `九十`, `roid`, `�`, ` eighty`, `兴国` (target ranks: base_value=17:238685, first_product=34:248310, bound_value=50:248254, second_product=100:238685, answer=113:238685)
- Layer 29: `九十`, `九`, `�`, `9`, ` ninety` (target ranks: base_value=17:91840, first_product=34:247729, bound_value=50:248283, second_product=100:91840, answer=113:91840)
- Layer 30: ` .`, `九十`, `9`, `九`, `.` (target ranks: base_value=17:5203, first_product=34:85831, bound_value=50:159813, second_product=100:5203, answer=113:5203)
- Layer 31: ` .`, `.`, ` ,`, ` :`, ` .=` (target ranks: base_value=17:13301, first_product=34:125125, bound_value=50:228656, second_product=100:13301, answer=113:13301)

### Filler position 4 (absolute token 879, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:21, first_product=34:173, bound_value=50:304, second_product=100:21, answer=113:21)
- Layer 8: `an`, `d`, `emo`, `istrator`, `ament` (target ranks: base_value=17:21633, first_product=34:49327, bound_value=50:22407, second_product=100:21633, answer=113:21633)
- Layer 16: `uth`, `orc`, ` irrelevant`, `lant`, `rength` (target ranks: base_value=17:56527, first_product=34:135785, bound_value=50:84928, second_product=100:56527, answer=113:56527)
- Layer 24: ` y`, `:y`, `�`, `*y`, ` Y` (target ranks: base_value=17:209278, first_product=34:226538, bound_value=50:162169, second_product=100:209278, answer=113:209278)
- Layer 25: `�`, `olicy`, ` y`, `órios`, `西亚` (target ranks: base_value=17:166454, first_product=34:187192, bound_value=50:99223, second_product=100:166454, answer=113:166454)
- Layer 26: `�`, `ients`, `órios`, `西亚`, `ièrement` (target ranks: base_value=17:217550, first_product=34:189537, bound_value=50:134039, second_product=100:217550, answer=113:217550)
- Layer 27: ` y`, `�`, `:y`, `.y`, `�` (target ranks: base_value=17:164437, first_product=34:217690, bound_value=50:162161, second_product=100:164437, answer=113:164437)
- Layer 28: ` y`, `.y`, `�`, `:y`, `anies` (target ranks: base_value=17:78720, first_product=34:94009, bound_value=50:174393, second_product=100:78720, answer=113:78720)
- Layer 29: ` y`, ` .`, `.y`, ` `, `8` (target ranks: base_value=17:4421, first_product=34:6241, bound_value=50:44496, second_product=100:4421, answer=113:4421)
- Layer 30: ` .`, ` y`, `-y`, ` Y`, `.y` (target ranks: base_value=17:1595, first_product=34:1160, bound_value=50:9806, second_product=100:1595, answer=113:1595)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` `, ` ..` (target ranks: base_value=17:87, first_product=34:182, bound_value=50:409, second_product=100:87, answer=113:87)

### Filler position 5 (absolute token 880, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:172, bound_value=50:303, second_product=100:20, answer=113:20)
- Layer 8: `uff`, `r`, `atia`, `um`, `u` (target ranks: base_value=17:4221, first_product=34:42210, bound_value=50:17443, second_product=100:4221, answer=113:4221)
- Layer 16: `�`, `兢`, `璀`, `明`, `�` (target ranks: base_value=17:82462, first_product=34:143021, bound_value=50:159901, second_product=100:82462, answer=113:82462)
- Layer 24: `itin`, `ons`, `es`, `�`, `é` (target ranks: base_value=17:3715, first_product=34:19435, bound_value=50:25851, second_product=100:3715, answer=113:3715)
- Layer 25: `�`, `itin`, `é`, `es`, `ach` (target ranks: base_value=17:2576, first_product=34:9854, bound_value=50:13553, second_product=100:2576, answer=113:2576)
- Layer 26: ` `, `<|endoftext|>`, `-`, ` .`, `é` (target ranks: base_value=17:47, first_product=34:266, bound_value=50:530, second_product=100:47, answer=113:47)
- Layer 27: ` .`, `雨露`, `ates`, `️`, `ons` (target ranks: base_value=17:5296, first_product=34:14773, bound_value=50:17752, second_product=100:5296, answer=113:5296)
- Layer 28: ` .`, `️`, `雨露`, `asi`, `itin` (target ranks: base_value=17:6445, first_product=34:1818, bound_value=50:17693, second_product=100:6445, answer=113:6445)
- Layer 29: ` .`, `·`, ` `, `<|endoftext|>`, `雨露` (target ranks: base_value=17:106, first_product=34:74, bound_value=50:351, second_product=100:106, answer=113:106)
- Layer 30: ` .`, ` ·`, ` `, ` ..`, `2` (target ranks: base_value=17:45, first_product=34:23, bound_value=50:71, second_product=100:45, answer=113:45)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` :`, ` ..` (target ranks: base_value=17:119, first_product=34:242, bound_value=50:216, second_product=100:119, answer=113:119)

### Filler position 6 (absolute token 881, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:172, bound_value=50:300, second_product=100:20, answer=113:20)
- Layer 8: `u`, `in`, `en`, `�`, `s` (target ranks: base_value=17:353, first_product=34:6018, bound_value=50:1758, second_product=100:353, answer=113:353)
- Layer 16: `基数`, `闷`, ` +`, `站`, `at` (target ranks: base_value=17:4450, first_product=34:21047, bound_value=50:5257, second_product=100:4450, answer=113:4450)
- Layer 24: `吁`, `ит`, `λεί`, `四十`, `ására` (target ranks: base_value=17:246017, first_product=34:33714, bound_value=50:212201, second_product=100:246017, answer=113:246017)
- Layer 25: `吁`, `-License`, `sas`, `四十`, `cribe` (target ranks: base_value=17:232728, first_product=34:47520, bound_value=50:185929, second_product=100:232728, answer=113:232728)
- Layer 26: `enang`, `吁`, `-License`, ` seventy`, `olygon` (target ranks: base_value=17:204245, first_product=34:153947, bound_value=50:145406, second_product=100:204245, answer=113:204245)
- Layer 27: `九十`, ` ninety`, `八十`, ` eighty`, `oit` (target ranks: base_value=17:230778, first_product=34:248319, bound_value=50:148493, second_product=100:230778, answer=113:230778)
- Layer 28: `九十`, `8`, `.bp`, `roid`, `�` (target ranks: base_value=17:227032, first_product=34:248303, bound_value=50:247944, second_product=100:227032, answer=113:227032)
- Layer 29: `8`, `九十`, `八`, `endre`, `�` (target ranks: base_value=17:62452, first_product=34:231485, bound_value=50:248183, second_product=100:62452, answer=113:62452)
- Layer 30: `8`, ` .`, `9`, `пей`, `九十` (target ranks: base_value=17:15082, first_product=34:44554, bound_value=50:139597, second_product=100:15082, answer=113:15082)
- Layer 31: ` .`, ` ,`, ` :`, ` ·`, ` ` (target ranks: base_value=17:685, first_product=34:11446, bound_value=50:145558, second_product=100:685, answer=113:685)

### Filler position 7 (absolute token 882, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:172, bound_value=50:296, second_product=100:20, answer=113:20)
- Layer 8: `atur`, `u`, `s`, `o`, `m` (target ranks: base_value=17:1272, first_product=34:20549, bound_value=50:5851, second_product=100:1272, answer=113:1272)
- Layer 16: `�`, `竿`, `翰`, `基础`, `�` (target ranks: base_value=17:43193, first_product=34:133753, bound_value=50:47429, second_product=100:43193, answer=113:43193)
- Layer 24: `吁`, `ит`, `λεί`, `ásával`, `erre` (target ranks: base_value=17:247987, first_product=34:103137, bound_value=50:214410, second_product=100:247987, answer=113:247987)
- Layer 25: `七十`, `吁`, `�`, ` seventy`, `ит` (target ranks: base_value=17:244348, first_product=34:104618, bound_value=50:192754, second_product=100:244348, answer=113:244348)
- Layer 26: `小七`, `enang`, `olygon`, `isson`, `_argument` (target ranks: base_value=17:217585, first_product=34:213144, bound_value=50:197864, second_product=100:217585, answer=113:217585)
- Layer 27: `九十`, `roid`, ` ninety`, `八十`, `�` (target ranks: base_value=17:217924, first_product=34:248320, bound_value=50:246448, second_product=100:217924, answer=113:217924)
- Layer 28: `九十`, `.bp`, `�`, ` ninety`, `兴国` (target ranks: base_value=17:203941, first_product=34:248315, bound_value=50:248310, second_product=100:203941, answer=113:203941)
- Layer 29: `九十`, `九`, `9`, ` ninety`, `�` (target ranks: base_value=17:19436, first_product=34:247292, bound_value=50:248316, second_product=100:19436, answer=113:19436)
- Layer 30: `9`, `九`, `九十`, ` .`, ` ninety` (target ranks: base_value=17:267, first_product=34:8217, bound_value=50:40027, second_product=100:267, answer=113:267)
- Layer 31: ` .`, ` ,`, ` :`, ` ..`, ` ·` (target ranks: base_value=17:147, first_product=34:10389, bound_value=50:76359, second_product=100:147, answer=113:147)

### Filler position 8 (absolute token 883, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:172, bound_value=50:296, second_product=100:20, answer=113:20)
- Layer 8: `u`, `田`, `á`, `窟`, `�` (target ranks: base_value=17:2506, first_product=34:66760, bound_value=50:25458, second_product=100:2506, answer=113:2506)
- Layer 16: `漫`, `之`, `依`, `望`, `ာ` (target ranks: base_value=17:26641, first_product=34:82709, bound_value=50:45208, second_product=100:26641, answer=113:26641)
- Layer 24: `longleftrightarrow`, `cket`, `່`, `յ`, `ာ` (target ranks: base_value=17:241068, first_product=34:242803, bound_value=50:236791, second_product=100:241068, answer=113:241068)
- Layer 25: `յ`, ` .`, `່`, `longleftrightarrow`, `cket` (target ranks: base_value=17:232963, first_product=34:232963, bound_value=50:213572, second_product=100:232963, answer=113:232963)
- Layer 26: ` .`, `յ`, `ာ`, `antium`, `longleftrightarrow` (target ranks: base_value=17:240669, first_product=34:226063, bound_value=50:221545, second_product=100:240669, answer=113:240669)
- Layer 27: ` .`, `．`, `-.`, ` `.`, ` .=` (target ranks: base_value=17:211872, first_product=34:224087, bound_value=50:216722, second_product=100:211872, answer=113:211872)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:150646, first_product=34:110739, bound_value=50:152365, second_product=100:150646, answer=113:150646)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `.` (target ranks: base_value=17:13540, first_product=34:14035, bound_value=50:16887, second_product=100:13540, answer=113:13540)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, ` .$` (target ranks: base_value=17:2122, first_product=34:1128, bound_value=50:2685, second_product=100:2122, answer=113:2122)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, ` ,` (target ranks: base_value=17:83, first_product=34:178, bound_value=50:210, second_product=100:83, answer=113:83)

### Filler position 9 (absolute token 884, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:170, bound_value=50:294, second_product=100:20, answer=113:20)
- Layer 8: `u`, `d`, `o`, `�`, `en` (target ranks: base_value=17:2167, first_product=34:21186, bound_value=50:13286, second_product=100:2167, answer=113:2167)
- Layer 16: `<think>`, `再加上`, `ering`, `拉德`, `erce` (target ranks: base_value=17:28536, first_product=34:62510, bound_value=50:27450, second_product=100:28536, answer=113:28536)
- Layer 24: `吁`, `四十`, `ит`, `八十`, `七十` (target ranks: base_value=17:245879, first_product=34:186944, bound_value=50:167873, second_product=100:245879, answer=113:245879)
- Layer 25: `七十`, ` seventy`, `燃`, `吁`, `八十` (target ranks: base_value=17:230255, first_product=34:125704, bound_value=50:166543, second_product=100:230255, answer=113:230255)
- Layer 26: `燃`, `enang`, `九十`, `吁`, `onders` (target ranks: base_value=17:173006, first_product=34:241507, bound_value=50:187504, second_product=100:173006, answer=113:173006)
- Layer 27: `九十`, ` ninety`, `�`, ` девя`, `第九` (target ranks: base_value=17:155015, first_product=34:248319, bound_value=50:248300, second_product=100:155015, answer=113:155015)
- Layer 28: `九十`, `�`, ` cien`, `兴国`, `immer` (target ranks: base_value=17:111016, first_product=34:248310, bound_value=50:248317, second_product=100:111016, answer=113:111016)
- Layer 29: `九十`, ` cien`, `一百`, `�`, `玖` (target ranks: base_value=17:993, first_product=34:248099, bound_value=50:248319, second_product=100:993, answer=113:993)
- Layer 30: `一百`, `十`, ` cien`, `1`, `十点` (target ranks: base_value=17:4, first_product=34:70117, bound_value=50:118894, second_product=100:4, answer=113:4)
- Layer 31: ` .`, `.`, ` ,`, ` .=`, ` ..` (target ranks: base_value=17:798, first_product=34:192441, bound_value=50:225401, second_product=100:798, answer=113:798)

### Filler position 10 (absolute token 885, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:170, bound_value=50:293, second_product=100:20, answer=113:20)
- Layer 8: `u`, `en`, `o`, `յ`, `和` (target ranks: base_value=17:506, first_product=34:11102, bound_value=50:2786, second_product=100:506, answer=113:506)
- Layer 16: `ament`, `束`, `子`, `utable`, `orial` (target ranks: base_value=17:1982, first_product=34:19370, bound_value=50:6632, second_product=100:1982, answer=113:1982)
- Layer 24: `蟀`, `erialization`, `erm`, `λεί`, `-License` (target ranks: base_value=17:248067, first_product=34:69488, bound_value=50:98080, second_product=100:248067, answer=113:248067)
- Layer 25: `-License`, `erte`, `erm`, `睹`, `有道` (target ranks: base_value=17:243482, first_product=34:21606, bound_value=50:55060, second_product=100:243482, answer=113:243482)
- Layer 26: `-License`, `民`, `有道`, `رم`, `睹` (target ranks: base_value=17:231038, first_product=34:45606, bound_value=50:51709, second_product=100:231038, answer=113:231038)
- Layer 27: `inciple`, `arian`, `�`, `六一`, `途` (target ranks: base_value=17:226221, first_product=34:248037, bound_value=50:18912, second_product=100:226221, answer=113:226221)
- Layer 28: `�`, ` bảy`, `adh`, `ност`, `小七` (target ranks: base_value=17:148140, first_product=34:248203, bound_value=50:246088, second_product=100:148140, answer=113:148140)
- Layer 29: `adh`, `�`, `情`, `共`, `芷` (target ranks: base_value=17:45465, first_product=34:184490, bound_value=50:245409, second_product=100:45465, answer=113:45465)
- Layer 30: ` .`, `inary`, ` ,`, `oid`, `营` (target ranks: base_value=17:6055, first_product=34:2499, bound_value=50:23021, second_product=100:6055, answer=113:6055)
- Layer 31: ` .`, ` ,`, ` :`, `．`, ` ·` (target ranks: base_value=17:133, first_product=34:543, bound_value=50:1530, second_product=100:133, answer=113:133)

### Filler position 11 (absolute token 886, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `B` (target ranks: base_value=17:20, first_product=34:170, bound_value=50:292, second_product=100:20, answer=113:20)
- Layer 8: `s`, `u`, `o`, ` ...`, `，` (target ranks: base_value=17:221, first_product=34:3028, bound_value=50:1092, second_product=100:221, answer=113:221)
- Layer 16: `漫`, `率`, `地`, `之`, `依` (target ranks: base_value=17:16444, first_product=34:32477, bound_value=50:41975, second_product=100:16444, answer=113:16444)
- Layer 24: `յ`, `ာ`, `longleftrightarrow`, `之`, `cket` (target ranks: base_value=17:238478, first_product=34:238903, bound_value=50:228365, second_product=100:238478, answer=113:238478)
- Layer 25: `յ`, `ာ`, ` .`, `longleftrightarrow`, `cket` (target ranks: base_value=17:227447, first_product=34:227447, bound_value=50:201973, second_product=100:227447, answer=113:227447)
- Layer 26: `յ`, ` .`, `ာ`, `longleftrightarrow`, `imensional` (target ranks: base_value=17:243912, first_product=34:233481, bound_value=50:222801, second_product=100:243912, answer=113:243912)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, `-.` (target ranks: base_value=17:221114, first_product=34:227657, bound_value=50:220607, second_product=100:221114, answer=113:221114)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:193885, first_product=34:163706, bound_value=50:162007, second_product=100:193885, answer=113:193885)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `_.` (target ranks: base_value=17:21559, first_product=34:18786, bound_value=50:13233, second_product=100:21559, answer=113:21559)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:1691, first_product=34:694, bound_value=50:965, second_product=100:1691, answer=113:1691)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, `↵↵` (target ranks: base_value=17:69, first_product=34:144, bound_value=50:122, second_product=100:69, answer=113:69)

### Filler position 12 (absolute token 887, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `_` (target ranks: base_value=17:20, first_product=34:169, bound_value=50:293, second_product=100:20, answer=113:20)
- Layer 8: `�`, `en`, `m`, `�`, `atur` (target ranks: base_value=17:415, first_product=34:9878, bound_value=50:5881, second_product=100:415, answer=113:415)
- Layer 16: `uple`, `ament`, `提`, `暗淡`, `yt` (target ranks: base_value=17:86288, first_product=34:190579, bound_value=50:139144, second_product=100:86288, answer=113:86288)
- Layer 24: `oit`, `*q`, `quisites`, `群`, `quisite` (target ranks: base_value=17:89063, first_product=34:99293, bound_value=50:48854, second_product=100:89063, answer=113:89063)
- Layer 25: `erox`, `quisites`, `*q`, `quisite`, `oit` (target ranks: base_value=17:123083, first_product=34:128631, bound_value=50:62812, second_product=100:123083, answer=113:123083)
- Layer 26: `erox`, `quisites`, `ож`, `quisite`, `avier` (target ranks: base_value=17:227889, first_product=34:205774, bound_value=50:156160, second_product=100:227889, answer=113:227889)
- Layer 27: `Qur`, `avier`, `eur`, `eurs`, `aturas` (target ranks: base_value=17:222276, first_product=34:231045, bound_value=50:202317, second_product=100:222276, answer=113:222276)
- Layer 28: `Qur`, `avier`, `eur`, `EUR`, `郁` (target ranks: base_value=17:125041, first_product=34:54034, bound_value=50:122006, second_product=100:125041, answer=113:125041)
- Layer 29: `Qur`, `eur`, ` qu`, `EUR`, `ur` (target ranks: base_value=17:4418, first_product=34:2022, bound_value=50:8003, second_product=100:4418, answer=113:4418)
- Layer 30: ` .`, ` qu`, ` q`, `-qu`, `/qu` (target ranks: base_value=17:748, first_product=34:362, bound_value=50:1231, second_product=100:748, answer=113:748)
- Layer 31: ` .`, ` ,`, `<|im_end|>`, ` :`, ` ;` (target ranks: base_value=17:120, first_product=34:197, bound_value=50:229, second_product=100:120, answer=113:120)

### Filler position 13 (absolute token 888, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `<|endoftext|>`, `_` (target ranks: base_value=17:20, first_product=34:170, bound_value=50:293, second_product=100:20, answer=113:20)
- Layer 8: `�`, `缈`, `�`, `唯一`, `触` (target ranks: base_value=17:2712, first_product=34:17471, bound_value=50:10804, second_product=100:2712, answer=113:2712)
- Layer 16: `站`, `igungs`, `ipline`, `基数`, `计算` (target ranks: base_value=17:73984, first_product=34:143506, bound_value=50:43897, second_product=100:73984, answer=113:73984)
- Layer 24: `吁`, `四十`, `λεί`, `ит`, `erre` (target ranks: base_value=17:247740, first_product=34:90566, bound_value=50:220898, second_product=100:247740, answer=113:247740)
- Layer 25: `吁`, `七十`, ` seventy`, `四十`, `sas` (target ranks: base_value=17:240865, first_product=34:89046, bound_value=50:199996, second_product=100:240865, answer=113:240865)
- Layer 26: `enang`, `吁`, `onders`, `小七`, `燃` (target ranks: base_value=17:219004, first_product=34:227349, bound_value=50:200983, second_product=100:219004, answer=113:219004)
- Layer 27: `九十`, ` ninety`, `roid`, ` eighty`, `�` (target ranks: base_value=17:221138, first_product=34:248320, bound_value=50:247099, second_product=100:221138, answer=113:221138)
- Layer 28: `九十`, `�`, ` ninety`, `兴国`, `roid` (target ranks: base_value=17:198459, first_product=34:248311, bound_value=50:248310, second_product=100:198459, answer=113:198459)
- Layer 29: `九十`, `九`, `9`, ` ninety`, `�` (target ranks: base_value=17:14023, first_product=34:247494, bound_value=50:248315, second_product=100:14023, answer=113:14023)
- Layer 30: `九`, `9`, `九十`, ` ninety`, `十点` (target ranks: base_value=17:226, first_product=34:30245, bound_value=50:74482, second_product=100:226, answer=113:226)
- Layer 31: ` .`, ` ,`, `.`, ` .=`, ` ·` (target ranks: base_value=17:1415, first_product=34:62381, bound_value=50:151210, second_product=100:1415, answer=113:1415)

### Filler position 14 (absolute token 889, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:170, bound_value=50:292, second_product=100:20, answer=113:20)
- Layer 8: `杈`, `u`, `…`, `t`, `横` (target ranks: base_value=17:808, first_product=34:43372, bound_value=50:9560, second_product=100:808, answer=113:808)
- Layer 16: `漫`, `地`, `望`, `白`, `之` (target ranks: base_value=17:9896, first_product=34:52701, bound_value=50:59854, second_product=100:9896, answer=113:9896)
- Layer 24: `longleftrightarrow`, `ာ`, `之`, `cket`, `յ` (target ranks: base_value=17:237839, first_product=34:241307, bound_value=50:232886, second_product=100:237839, answer=113:237839)
- Layer 25: `longleftrightarrow`, `ာ`, ` .`, `յ`, `�` (target ranks: base_value=17:223940, first_product=34:230828, bound_value=50:208197, second_product=100:223940, answer=113:223940)
- Layer 26: `ာ`, `longleftrightarrow`, ` .`, `最新发布`, `յ` (target ranks: base_value=17:238481, first_product=34:228477, bound_value=50:217119, second_product=100:238481, answer=113:238481)
- Layer 27: ` .`, `．`, `-.`, ` .$`, ` `.` (target ranks: base_value=17:184688, first_product=34:213314, bound_value=50:206605, second_product=100:184688, answer=113:184688)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:111623, first_product=34:89409, bound_value=50:141444, second_product=100:111623, answer=113:111623)
- Layer 29: ` .`, `．`, `-.`, `.`, ` `.` (target ranks: base_value=17:8722, first_product=34:9031, bound_value=50:14981, second_product=100:8722, answer=113:8722)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` .*` (target ranks: base_value=17:2222, first_product=34:941, bound_value=50:2813, second_product=100:2222, answer=113:2222)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ,`, ` ..` (target ranks: base_value=17:103, first_product=34:195, bound_value=50:257, second_product=100:103, answer=113:103)

### Filler position 15 (absolute token 890, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:167, bound_value=50:291, second_product=100:20, answer=113:20)
- Layer 8: `田`, `o`, `↵`, `us`, `t` (target ranks: base_value=17:277, first_product=34:4194, bound_value=50:1247, second_product=100:277, answer=113:277)
- Layer 16: `担`, `�`, `的人`, `目的`, `ած` (target ranks: base_value=17:4649, first_product=34:47102, bound_value=50:13992, second_product=100:4649, answer=113:4649)
- Layer 24: `吁`, `λεί`, `enang`, `ит`, `四十` (target ranks: base_value=17:247342, first_product=34:63029, bound_value=50:219627, second_product=100:247342, answer=113:247342)
- Layer 25: `吁`, `-License`, `arian`, `enang`, `λεί` (target ranks: base_value=17:240342, first_product=34:42006, bound_value=50:183399, second_product=100:240342, answer=113:240342)
- Layer 26: `enang`, `吁`, `_argument`, `-License`, `arians` (target ranks: base_value=17:224832, first_product=34:149514, bound_value=50:142944, second_product=100:224832, answer=113:224832)
- Layer 27: `九十`, `oit`, `roid`, `小七`, ` ninety` (target ranks: base_value=17:242416, first_product=34:248319, bound_value=50:115101, second_product=100:242416, answer=113:242416)
- Layer 28: `roid`, `8`, `.bp`, `�`, `ouples` (target ranks: base_value=17:242091, first_product=34:248307, bound_value=50:248023, second_product=100:242091, answer=113:242091)
- Layer 29: `八`, `8`, ` tám`, ` eighth`, ` eighty` (target ranks: base_value=17:115834, first_product=34:241489, bound_value=50:248291, second_product=100:115834, answer=113:115834)
- Layer 30: ` .`, `8`, `八`, `八点`, ` eight` (target ranks: base_value=17:83887, first_product=34:126846, bound_value=50:200013, second_product=100:83887, answer=113:83887)
- Layer 31: ` .`, ` ,`, `．`, ` ·`, `.` (target ranks: base_value=17:6482, first_product=34:62285, bound_value=50:152359, second_product=100:6482, answer=113:6482)

### Filler position 16 (absolute token 891, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:166, bound_value=50:291, second_product=100:20, answer=113:20)
- Layer 8: `o`, `uff`, `um`, `U`, `u` (target ranks: base_value=17:144, first_product=34:6554, bound_value=50:2200, second_product=100:144, answer=113:144)
- Layer 16: `�`, `�`, `提`, `翰`, `担` (target ranks: base_value=17:13004, first_product=34:82337, bound_value=50:15634, second_product=100:13004, answer=113:13004)
- Layer 24: `λεί`, `ит`, `吁`, `�`, `erm` (target ranks: base_value=17:246721, first_product=34:28583, bound_value=50:117647, second_product=100:246721, answer=113:246721)
- Layer 25: `四十`, `七十`, `界`, `相互`, `集中` (target ranks: base_value=17:239235, first_product=34:9792, bound_value=50:98638, second_product=100:239235, answer=113:239235)
- Layer 26: `小七`, `�`, `ouples`, `enang`, `管制` (target ranks: base_value=17:195451, first_product=34:86334, bound_value=50:139237, second_product=100:195451, answer=113:195451)
- Layer 27: `小七`, `九十`, `�`, `addGroup`, `roid` (target ranks: base_value=17:172688, first_product=34:248311, bound_value=50:222066, second_product=100:172688, answer=113:172688)
- Layer 28: `九十`, `�`, `小七`, `�`, `addGroup` (target ranks: base_value=17:58082, first_product=34:248229, bound_value=50:248279, second_product=100:58082, answer=113:58082)
- Layer 29: `九`, `9`, `�`, `第九`, `九十` (target ranks: base_value=17:1124, first_product=34:230059, bound_value=50:248255, second_product=100:1124, answer=113:1124)
- Layer 30: ` .`, `九`, `9`, ` Nin`, ` ninety` (target ranks: base_value=17:374, first_product=34:11663, bound_value=50:35467, second_product=100:374, answer=113:374)
- Layer 31: ` .`, ` ,`, ` ·`, ` :`, ` ..` (target ranks: base_value=17:191, first_product=34:8793, bound_value=50:11495, second_product=100:191, answer=113:191)

### Filler position 17 (absolute token 892, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:166, bound_value=50:290, second_product=100:20, answer=113:20)
- Layer 8: `o`, `uff`, `um`, `�`, `u` (target ranks: base_value=17:291, first_product=34:10822, bound_value=50:2904, second_product=100:291, answer=113:291)
- Layer 16: `isson`, `酵`, `束`, `器`, `igungs` (target ranks: base_value=17:40472, first_product=34:101663, bound_value=50:41626, second_product=100:40472, answer=113:40472)
- Layer 24: `λεί`, `anit`, `erialization`, `�`, `ourcing` (target ranks: base_value=17:247971, first_product=34:38442, bound_value=50:146117, second_product=100:247971, answer=113:247971)
- Layer 25: `erte`, `anit`, `λεί`, `erm`, `-License` (target ranks: base_value=17:245877, first_product=34:7296, bound_value=50:117139, second_product=100:245877, answer=113:245877)
- Layer 26: `zon`, `رم`, `ourcing`, `anit`, `erman` (target ranks: base_value=17:246274, first_product=34:11870, bound_value=50:115300, second_product=100:246274, answer=113:246274)
- Layer 27: `五十`, `六十`, `onian`, `λεί`, `arian` (target ranks: base_value=17:248202, first_product=34:247292, bound_value=50:2235, second_product=100:248202, answer=113:248202)
- Layer 28: `erializer`, `ariate`, `inic`, `pent`, `相互` (target ranks: base_value=17:245749, first_product=34:248251, bound_value=50:3562, second_product=100:245749, answer=113:245749)
- Layer 29: `六`, `6`, `pent`, `非`, `第六` (target ranks: base_value=17:159066, first_product=34:244973, bound_value=50:275, second_product=100:159066, answer=113:159066)
- Layer 30: ` .`, `6`, `不必`, `六`, `5` (target ranks: base_value=17:20626, first_product=34:31626, bound_value=50:4, second_product=100:20626, answer=113:20626)
- Layer 31: ` .`, ` ,`, ` ·`, `．`, ` ..` (target ranks: base_value=17:971, first_product=34:6452, bound_value=50:528, second_product=100:971, answer=113:971)

### Filler position 18 (absolute token 893, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:165, bound_value=50:290, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `�`, `u`, `um` (target ranks: base_value=17:669, first_product=34:9683, bound_value=50:4293, second_product=100:669, answer=113:669)
- Layer 16: `�`, `漫`, `adero`, `erm`, `修` (target ranks: base_value=17:239533, first_product=34:243378, bound_value=50:183253, second_product=100:239533, answer=113:239533)
- Layer 24: `psilon`, `/filepath`, `erm`, `aliser`, `相似文献` (target ranks: base_value=17:248296, first_product=34:248204, bound_value=50:248142, second_product=100:248296, answer=113:248296)
- Layer 25: `psilon`, `相似文献`, `allax`, `�`, `/filepath` (target ranks: base_value=17:248252, first_product=34:247968, bound_value=50:247925, second_product=100:248252, answer=113:248252)
- Layer 26: `旗下`, `psilon`, `allax`, `erm`, `相似文献` (target ranks: base_value=17:248316, first_product=34:248041, bound_value=50:248126, second_product=100:248316, answer=113:248316)
- Layer 27: `chure`, `olang`, `eload`, `潮`, `psilon` (target ranks: base_value=17:247868, first_product=34:246195, bound_value=50:247484, second_product=100:247868, answer=113:247868)
- Layer 28: `chure`, `ച`, ` ​​`, `emoth`, `olang` (target ranks: base_value=17:248054, first_product=34:233639, bound_value=50:239843, second_product=100:248054, answer=113:248054)
- Layer 29: `自已`, `toFixed`, `�`, `commended`, `�` (target ranks: base_value=17:241109, first_product=34:175162, bound_value=50:168701, second_product=100:241109, answer=113:241109)
- Layer 30: ` .`, ` cor`, `asi`, `最新文章`, `erm` (target ranks: base_value=17:56990, first_product=34:16315, bound_value=50:4122, second_product=100:56990, answer=113:56990)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` 。`, ` :` (target ranks: base_value=17:505, first_product=34:1679, bound_value=50:211, second_product=100:505, answer=113:505)

### Filler position 19 (absolute token 894, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:164, bound_value=50:287, second_product=100:20, answer=113:20)
- Layer 8: `o`, `u`, `�`, `@`, `�` (target ranks: base_value=17:1319, first_product=34:32653, bound_value=50:9829, second_product=100:1319, answer=113:1319)
- Layer 16: `提`, `漫`, `明`, `破`, `派` (target ranks: base_value=17:13774, first_product=34:63021, bound_value=50:32427, second_product=100:13774, answer=113:13774)
- Layer 24: `ariate`, `erer`, `�`, `了`, `յ` (target ranks: base_value=17:198892, first_product=34:199316, bound_value=50:162286, second_product=100:198892, answer=113:198892)
- Layer 25: ` .`, `�`, `յ`, `�`, `ariate` (target ranks: base_value=17:184561, first_product=34:164785, bound_value=50:121312, second_product=100:184561, answer=113:184561)
- Layer 26: ` .`, `�`, `յ`, ` ..`, `erm` (target ranks: base_value=17:209277, first_product=34:148616, bound_value=50:140392, second_product=100:209277, answer=113:209277)
- Layer 27: ` .`, `．`, ` ..`, `-.`, ` .=` (target ranks: base_value=17:176635, first_product=34:163844, bound_value=50:151712, second_product=100:176635, answer=113:176635)
- Layer 28: ` .`, `．`, ` ..`, `-.`, ` .$` (target ranks: base_value=17:59201, first_product=34:18114, bound_value=50:10603, second_product=100:59201, answer=113:59201)
- Layer 29: ` .`, `．`, `-.`, ` ..`, `_.` (target ranks: base_value=17:5004, first_product=34:2558, bound_value=50:1290, second_product=100:5004, answer=113:5004)
- Layer 30: ` .`, ` ..`, ` ,`, ` `.`, ` ."` (target ranks: base_value=17:885, first_product=34:388, bound_value=50:60, second_product=100:885, answer=113:885)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ,`, ` ..` (target ranks: base_value=17:123, first_product=34:198, bound_value=50:62, second_product=100:123, answer=113:123)

### Filler position 20 (absolute token 895, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:164, bound_value=50:285, second_product=100:20, answer=113:20)
- Layer 8: `u`, `o`, `�`, `�`, `窟` (target ranks: base_value=17:1302, first_product=34:15782, bound_value=50:5059, second_product=100:1302, answer=113:1302)
- Layer 16: `漫`, `望`, `内`, `依`, `朔` (target ranks: base_value=17:15337, first_product=34:45997, bound_value=50:73234, second_product=100:15337, answer=113:15337)
- Layer 24: `longleftrightarrow`, `erer`, `égr`, `cket`, `յ` (target ranks: base_value=17:236790, first_product=34:231640, bound_value=50:223931, second_product=100:236790, answer=113:236790)
- Layer 25: `longleftrightarrow`, `յ`, ` .`, `égr`, `cket` (target ranks: base_value=17:218828, first_product=34:207097, bound_value=50:186658, second_product=100:218828, answer=113:218828)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `根据权利要求`, `最新发布` (target ranks: base_value=17:237749, first_product=34:205752, bound_value=50:209247, second_product=100:237749, answer=113:237749)
- Layer 27: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:189256, first_product=34:192828, bound_value=50:193738, second_product=100:189256, answer=113:189256)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:117398, first_product=34:75993, bound_value=50:71796, second_product=100:117398, answer=113:117398)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `!.` (target ranks: base_value=17:10900, first_product=34:6452, bound_value=50:4248, second_product=100:10900, answer=113:10900)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:1653, first_product=34:538, bound_value=50:200, second_product=100:1653, answer=113:1653)
- Layer 31: ` .`, `<|im_end|>`, ` `, ` ..`, `↵↵` (target ranks: base_value=17:113, first_product=34:174, bound_value=50:95, second_product=100:113, answer=113:113)

### Filler position 21 (absolute token 896, surface ` .`)

- Layer 0: ` `, `-`, `↵`, `_`, `<|endoftext|>` (target ranks: base_value=17:20, first_product=34:164, bound_value=50:285, second_product=100:20, answer=113:20)
- Layer 8: `en`, `�`, `u`, `enary`, `i` (target ranks: base_value=17:515, first_product=34:10346, bound_value=50:4664, second_product=100:515, answer=113:515)
- Layer 16: `提`, `utable`, `igungs`, `倍`, `担` (target ranks: base_value=17:7194, first_product=34:62300, bound_value=50:22796, second_product=100:7194, answer=113:7194)
- Layer 24: `吁`, `λεί`, `ит`, `-License`, `�` (target ranks: base_value=17:245331, first_product=34:13748, bound_value=50:187257, second_product=100:245331, answer=113:245331)
- Layer 25: `-License`, `吁`, `λεί`, `四十`, `pill` (target ranks: base_value=17:232422, first_product=34:15856, bound_value=50:152232, second_product=100:232422, answer=113:232422)
- Layer 26: `-License`, `enang`, `_argument`, `吁`, ` seventy` (target ranks: base_value=17:217930, first_product=34:97505, bound_value=50:111338, second_product=100:217930, answer=113:217930)
- Layer 27: `九十`, `oit`, `�`, `roid`, ` ninety` (target ranks: base_value=17:222868, first_product=34:248319, bound_value=50:20693, second_product=100:222868, answer=113:222868)
- Layer 28: `.bp`, `ellers`, `�`, `roid`, ` bảy` (target ranks: base_value=17:236365, first_product=34:248296, bound_value=50:242392, second_product=100:236365, answer=113:236365)
- Layer 29: `�`, `8`, `endre`, `八`, `onter` (target ranks: base_value=17:130101, first_product=34:210611, bound_value=50:247474, second_product=100:130101, answer=113:130101)
- Layer 30: ` .`, `8`, `пей`, `八`, `Messenger` (target ranks: base_value=17:104786, first_product=34:70266, bound_value=50:182190, second_product=100:104786, answer=113:104786)
- Layer 31: ` .`, ` ,`, `．`, ` ·`, ` *` (target ranks: base_value=17:1099, first_product=34:11977, bound_value=50:69882, second_product=100:1099, answer=113:1099)

### Filler position 22 (absolute token 897, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:164, bound_value=50:285, second_product=100:20, answer=113:20)
- Layer 8: `o`, `u`, `田`, `�`, `↵` (target ranks: base_value=17:235, first_product=34:7120, bound_value=50:4216, second_product=100:235, answer=113:235)
- Layer 16: `之`, `子`, `束`, `器`, `orial` (target ranks: base_value=17:4415, first_product=34:27733, bound_value=50:8164, second_product=100:4415, answer=113:4415)
- Layer 24: `λεί`, `吁`, `erm`, `�`, `-License` (target ranks: base_value=17:248140, first_product=34:65773, bound_value=50:133976, second_product=100:248140, answer=113:248140)
- Layer 25: `-License`, ` seventy`, `�`, `erm`, `ourcing` (target ranks: base_value=17:246413, first_product=34:36764, bound_value=50:75707, second_product=100:246413, answer=113:246413)
- Layer 26: `erman`, `小七`, `-License`, `enang`, `ourcing` (target ranks: base_value=17:228997, first_product=34:121661, bound_value=50:71313, second_product=100:228997, answer=113:228997)
- Layer 27: `九十`, `roid`, `小七`, `�`, `oit` (target ranks: base_value=17:219694, first_product=34:248319, bound_value=50:119290, second_product=100:219694, answer=113:219694)
- Layer 28: `九十`, `roid`, `�`, `小七`, ` bảy` (target ranks: base_value=17:212978, first_product=34:248309, bound_value=50:247211, second_product=100:212978, answer=113:212978)
- Layer 29: `八`, `九`, `8`, `九十`, `�` (target ranks: base_value=17:77505, first_product=34:239844, bound_value=50:247931, second_product=100:77505, answer=113:77505)
- Layer 30: ` .`, `8`, `八`, `9`, `пей` (target ranks: base_value=17:11126, first_product=34:21311, bound_value=50:84642, second_product=100:11126, answer=113:11126)
- Layer 31: ` .`, ` ,`, `．`, ` ·`, ` :` (target ranks: base_value=17:337, first_product=34:20830, bound_value=50:57659, second_product=100:337, answer=113:337)

### Filler position 23 (absolute token 898, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:162, bound_value=50:286, second_product=100:20, answer=113:20)
- Layer 8: `o`, `↵`, `sn`, `田`, `о` (target ranks: base_value=17:431, first_product=34:1895, bound_value=50:2061, second_product=100:431, answer=113:431)
- Layer 16: `内`, `漫`, `依`, `人`, `晴` (target ranks: base_value=17:8772, first_product=34:12906, bound_value=50:31119, second_product=100:8772, answer=113:8772)
- Layer 24: `longleftrightarrow`, `յ`, `之`, `ာ`, `່` (target ranks: base_value=17:240655, first_product=34:232580, bound_value=50:210543, second_product=100:240655, answer=113:240655)
- Layer 25: `յ`, `longleftrightarrow`, ` .`, `�`, `之` (target ranks: base_value=17:231900, first_product=34:214582, bound_value=50:173213, second_product=100:231900, answer=113:231900)
- Layer 26: `յ`, `longleftrightarrow`, ` .`, `ာ`, `最新发布` (target ranks: base_value=17:244579, first_product=34:223427, bound_value=50:200370, second_product=100:244579, answer=113:244579)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, ` .=` (target ranks: base_value=17:216053, first_product=34:216053, bound_value=50:198117, second_product=100:216053, answer=113:216053)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=17:167099, first_product=34:115262, bound_value=50:88252, second_product=100:167099, answer=113:167099)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `!.` (target ranks: base_value=17:17212, first_product=34:11975, bound_value=50:5199, second_product=100:17212, answer=113:17212)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:1071, first_product=34:353, bound_value=50:322, second_product=100:1071, answer=113:1071)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=17:98, first_product=34:175, bound_value=50:140, second_product=100:98, answer=113:98)

### Filler position 24 (absolute token 899, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:161, bound_value=50:284, second_product=100:20, answer=113:20)
- Layer 8: `�`, `�`, `o`, `t`, `d` (target ranks: base_value=17:434, first_product=34:1324, bound_value=50:2145, second_product=100:434, answer=113:434)
- Layer 16: `�`, `器`, `束`, `尺`, `ած` (target ranks: base_value=17:48920, first_product=34:145496, bound_value=50:60590, second_product=100:48920, answer=113:48920)
- Layer 24: `λεί`, `吁`, `-License`, `ит`, `-routing` (target ranks: base_value=17:248049, first_product=34:113510, bound_value=50:163184, second_product=100:248049, answer=113:248049)
- Layer 25: `-License`, `pill`, `λεί`, `粽`, ` seventy` (target ranks: base_value=17:246062, first_product=34:67300, bound_value=50:118640, second_product=100:246062, answer=113:246062)
- Layer 26: `enang`, `-License`, `谷雨`, `小七`, `ourcing` (target ranks: base_value=17:239163, first_product=34:184246, bound_value=50:98730, second_product=100:239163, answer=113:239163)
- Layer 27: `九十`, `roid`, `小七`, ` ninety`, `oit` (target ranks: base_value=17:235815, first_product=34:248319, bound_value=50:115696, second_product=100:235815, answer=113:235815)
- Layer 28: `ellers`, `roid`, ` bảy`, `.bp`, `8` (target ranks: base_value=17:243906, first_product=34:248310, bound_value=50:248241, second_product=100:243906, answer=113:243906)
- Layer 29: `八`, `8`, `�`, ` tám`, `endre` (target ranks: base_value=17:193061, first_product=34:238704, bound_value=50:248306, second_product=100:193061, answer=113:193061)
- Layer 30: ` .`, `8`, `八`, ` ·`, `пей` (target ranks: base_value=17:95910, first_product=34:108432, bound_value=50:163749, second_product=100:95910, answer=113:95910)
- Layer 31: ` .`, ` ,`, `．`, ` ·`, ` :` (target ranks: base_value=17:2130, first_product=34:78776, bound_value=50:132037, second_product=100:2130, answer=113:2130)

### Filler position 25 (absolute token 900, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:161, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `�`, `额`, `u` (target ranks: base_value=17:583, first_product=34:11453, bound_value=50:11375, second_product=100:583, answer=113:583)
- Layer 16: `派`, `明`, `索`, `存`, `�` (target ranks: base_value=17:46325, first_product=34:102429, bound_value=50:28692, second_product=100:46325, answer=113:46325)
- Layer 24: `psilon`, `allax`, `່`, `erm`, `ambda` (target ranks: base_value=17:245231, first_product=34:243904, bound_value=50:238236, second_product=100:245231, answer=113:245231)
- Layer 25: `allax`, `յ`, `相似文献`, `່`, `psilon` (target ranks: base_value=17:243492, first_product=34:240565, bound_value=50:232693, second_product=100:243492, answer=113:243492)
- Layer 26: `allax`, `erm`, `旗下`, `uks`, `相似文献` (target ranks: base_value=17:245054, first_product=34:235399, bound_value=50:230866, second_product=100:245054, answer=113:245054)
- Layer 27: ` .`, `olang`, `emoth`, `️`, `．` (target ranks: base_value=17:240631, first_product=34:239605, bound_value=50:238267, second_product=100:240631, answer=113:240631)
- Layer 28: ` .`, `olang`, `．`, `emoth`, ` ​​` (target ranks: base_value=17:244997, first_product=34:173027, bound_value=50:227863, second_product=100:244997, answer=113:244997)
- Layer 29: ` .`, `erm`, `．`, `emoth`, `olang` (target ranks: base_value=17:213443, first_product=34:93447, bound_value=50:146977, second_product=100:213443, answer=113:213443)
- Layer 30: ` .`, ` ..`, ` ,`, ` ."`, ` ·` (target ranks: base_value=17:56396, first_product=34:6793, bound_value=50:24542, second_product=100:56396, answer=113:56396)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, `↵↵`, ` ..` (target ranks: base_value=17:222, first_product=34:221, bound_value=50:249, second_product=100:222, answer=113:222)

### Filler position 26 (absolute token 901, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:161, bound_value=50:283, second_product=100:20, answer=113:20)
- Layer 8: `u`, `t`, `↵`, ` t`, `o` (target ranks: base_value=17:654, first_product=34:8012, bound_value=50:6746, second_product=100:654, answer=113:654)
- Layer 16: `望`, `漫`, `内`, `人`, `白` (target ranks: base_value=17:4340, first_product=34:13705, bound_value=50:26903, second_product=100:4340, answer=113:4340)
- Layer 24: `longleftrightarrow`, `յ`, `ာ`, `ី`, `cket` (target ranks: base_value=17:220140, first_product=34:208438, bound_value=50:174769, second_product=100:220140, answer=113:220140)
- Layer 25: `յ`, `longleftrightarrow`, ` .`, `�`, `ာ` (target ranks: base_value=17:196781, first_product=34:181605, bound_value=50:124583, second_product=100:196781, answer=113:196781)
- Layer 26: `յ`, ` .`, `ာ`, `longleftrightarrow`, `最新发布` (target ranks: base_value=17:231350, first_product=34:188754, bound_value=50:155490, second_product=100:231350, answer=113:231350)
- Layer 27: ` .`, `．`, `-.`, ` `.`, ` .$` (target ranks: base_value=17:157850, first_product=34:166612, bound_value=50:135745, second_product=100:157850, answer=113:157850)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=17:100373, first_product=34:59244, bound_value=50:45372, second_product=100:100373, answer=113:100373)
- Layer 29: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=17:5845, first_product=34:3791, bound_value=50:2314, second_product=100:5845, answer=113:5845)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:783, first_product=34:241, bound_value=50:181, second_product=100:783, answer=113:783)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, `↵` (target ranks: base_value=17:121, first_product=34:165, bound_value=50:113, second_product=100:121, answer=113:121)

### Filler position 27 (absolute token 902, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:161, bound_value=50:283, second_product=100:20, answer=113:20)
- Layer 8: `↵`, `t`, `u`, `了`, `s` (target ranks: base_value=17:226, first_product=34:1330, bound_value=50:1347, second_product=100:226, answer=113:226)
- Layer 16: `漫`, `提`, `内`, `望`, `ံ` (target ranks: base_value=17:17757, first_product=34:47252, bound_value=50:51681, second_product=100:17757, answer=113:17757)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ambda`, `ာ` (target ranks: base_value=17:229933, first_product=34:220861, bound_value=50:188101, second_product=100:229933, answer=113:229933)
- Layer 25: `յ`, `之`, ` .`, `longleftrightarrow`, `ambda` (target ranks: base_value=17:217353, first_product=34:206296, bound_value=50:159855, second_product=100:217353, answer=113:217353)
- Layer 26: `յ`, ` .`, `imensional`, `longleftrightarrow`, `ာ` (target ranks: base_value=17:236655, first_product=34:202416, bound_value=50:172113, second_product=100:236655, answer=113:236655)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:193527, first_product=34:194448, bound_value=50:167362, second_product=100:193527, answer=113:193527)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:171905, first_product=34:65488, bound_value=50:78890, second_product=100:171905, answer=113:171905)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `/.` (target ranks: base_value=17:19798, first_product=34:4304, bound_value=50:5490, second_product=100:19798, answer=113:19798)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` .*` (target ranks: base_value=17:2834, first_product=34:293, bound_value=50:704, second_product=100:2834, answer=113:2834)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:153, first_product=34:139, bound_value=50:162, second_product=100:153, answer=113:153)

### Filler position 28 (absolute token 903, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:159, bound_value=50:283, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `�`, `↵`, `u` (target ranks: base_value=17:95, first_product=34:2212, bound_value=50:1780, second_product=100:95, answer=113:95)
- Layer 16: `漫`, `提`, `内`, `望`, `久` (target ranks: base_value=17:38106, first_product=34:66895, bound_value=50:54047, second_product=100:38106, answer=113:38106)
- Layer 24: `յ`, `erer`, `andalone`, `viders`, `了` (target ranks: base_value=17:218396, first_product=34:224807, bound_value=50:189532, second_product=100:218396, answer=113:218396)
- Layer 25: `յ`, `andalone`, `�`, `viders`, `ож` (target ranks: base_value=17:205154, first_product=34:213389, bound_value=50:167040, second_product=100:205154, answer=113:205154)
- Layer 26: `յ`, `�`, `ож`, ` .`, `viders` (target ranks: base_value=17:212155, first_product=34:196143, bound_value=50:160897, second_product=100:212155, answer=113:212155)
- Layer 27: ` .`, `-.`, ` `.`, `/.`, `．` (target ranks: base_value=17:214292, first_product=34:223595, bound_value=50:193985, second_product=100:214292, answer=113:214292)
- Layer 28: ` .`, `-.`, ` `.`, `．`, `/.` (target ranks: base_value=17:185298, first_product=34:38986, bound_value=50:92327, second_product=100:185298, answer=113:185298)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `/.` (target ranks: base_value=17:47871, first_product=34:3728, bound_value=50:15394, second_product=100:47871, answer=113:47871)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, ` ,` (target ranks: base_value=17:6740, first_product=34:235, bound_value=50:1831, second_product=100:6740, answer=113:6740)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:146, first_product=34:88, bound_value=50:182, second_product=100:146, answer=113:146)

### Filler position 29 (absolute token 904, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `�`, `↵`, `u` (target ranks: base_value=17:218, first_product=34:8799, bound_value=50:5705, second_product=100:218, answer=113:218)
- Layer 16: `漫`, `内`, `iti`, `吐`, `信` (target ranks: base_value=17:4885, first_product=34:19933, bound_value=50:11618, second_product=100:4885, answer=113:4885)
- Layer 24: `յ`, `longleftrightarrow`, `yta`, `ек`, `cket` (target ranks: base_value=17:227406, first_product=34:221403, bound_value=50:174594, second_product=100:227406, answer=113:227406)
- Layer 25: `յ`, ` .`, `longleftrightarrow`, `viders`, `yta` (target ranks: base_value=17:200767, first_product=34:191580, bound_value=50:117840, second_product=100:200767, answer=113:200767)
- Layer 26: `յ`, ` .`, `uks`, `erness`, `viders` (target ranks: base_value=17:219918, first_product=34:178133, bound_value=50:128291, second_product=100:219918, answer=113:219918)
- Layer 27: ` .`, `．`, ` `.`, ` .=`, `-.` (target ranks: base_value=17:176675, first_product=34:194212, bound_value=50:164498, second_product=100:176675, answer=113:176675)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:120072, first_product=34:72416, bound_value=50:70193, second_product=100:120072, answer=113:120072)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `/.` (target ranks: base_value=17:6137, first_product=34:4195, bound_value=50:3056, second_product=100:6137, answer=113:6137)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=17:566, first_product=34:185, bound_value=50:269, second_product=100:566, answer=113:566)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:126, first_product=34:239, bound_value=50:227, second_product=100:126, answer=113:126)

### Filler position 30 (absolute token 905, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `↵`, `u`, `t` (target ranks: base_value=17:325, first_product=34:2833, bound_value=50:2425, second_product=100:325, answer=113:325)
- Layer 16: `漫`, `内`, `ights`, `白`, `派` (target ranks: base_value=17:9402, first_product=34:35508, bound_value=50:45118, second_product=100:9402, answer=113:9402)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ာ`, `ights` (target ranks: base_value=17:217549, first_product=34:221052, bound_value=50:181374, second_product=100:217549, answer=113:217549)
- Layer 25: `յ`, `之`, `longleftrightarrow`, ` .`, `�` (target ranks: base_value=17:189055, first_product=34:200428, bound_value=50:138202, second_product=100:189055, answer=113:189055)
- Layer 26: `յ`, `imensional`, `longleftrightarrow`, `ာ`, ` .` (target ranks: base_value=17:225893, first_product=34:205406, bound_value=50:155922, second_product=100:225893, answer=113:225893)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, `-.` (target ranks: base_value=17:165669, first_product=34:201561, bound_value=50:160720, second_product=100:165669, answer=113:165669)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=17:120483, first_product=34:88643, bound_value=50:72160, second_product=100:120483, answer=113:120483)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `.` (target ranks: base_value=17:9861, first_product=34:9013, bound_value=50:4449, second_product=100:9861, answer=113:9861)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:4021, first_product=34:1249, bound_value=50:1219, second_product=100:4021, answer=113:4021)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:133, first_product=34:186, bound_value=50:149, second_product=100:133, answer=113:133)

### Filler position 31 (absolute token 906, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `u`, `t` (target ranks: base_value=17:271, first_product=34:3158, bound_value=50:2235, second_product=100:271, answer=113:271)
- Layer 16: `漫`, `内`, `提`, `ံ`, `长` (target ranks: base_value=17:5425, first_product=34:20032, bound_value=50:30321, second_product=100:5425, answer=113:5425)
- Layer 24: `յ`, `longleftrightarrow`, `kelse`, `yta`, `ံ` (target ranks: base_value=17:238906, first_product=34:234511, bound_value=50:198406, second_product=100:238906, answer=113:238906)
- Layer 25: `յ`, `longleftrightarrow`, ` .`, `之`, `�` (target ranks: base_value=17:220387, first_product=34:218599, bound_value=50:154824, second_product=100:220387, answer=113:220387)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, ` .=`, `uks` (target ranks: base_value=17:229228, first_product=34:200641, bound_value=50:148273, second_product=100:229228, answer=113:229228)
- Layer 27: ` .`, ` `.`, `．`, ` .=`, ` .$` (target ranks: base_value=17:205861, first_product=34:220808, bound_value=50:176171, second_product=100:205861, answer=113:205861)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:157734, first_product=34:103223, bound_value=50:85481, second_product=100:157734, answer=113:157734)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:15964, first_product=34:10852, bound_value=50:5129, second_product=100:15964, answer=113:15964)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=17:3308, first_product=34:891, bound_value=50:744, second_product=100:3308, answer=113:3308)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:130, first_product=34:264, bound_value=50:157, second_product=100:130, answer=113:130)

### Filler position 32 (absolute token 907, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `u`, `↵`, `s` (target ranks: base_value=17:228, first_product=34:3408, bound_value=50:2579, second_product=100:228, answer=113:228)
- Layer 16: `漫`, `吐`, `յ`, `↵`, `望` (target ranks: base_value=17:13188, first_product=34:28284, bound_value=50:34411, second_product=100:13188, answer=113:13188)
- Layer 24: `յ`, `longleftrightarrow`, `égr`, `ож`, `yta` (target ranks: base_value=17:243449, first_product=34:242340, bound_value=50:222186, second_product=100:243449, answer=113:243449)
- Layer 25: `յ`, `égr`, `ож`, `longleftrightarrow`, `viders` (target ranks: base_value=17:236035, first_product=34:235725, bound_value=50:195371, second_product=100:236035, answer=113:236035)
- Layer 26: `յ`, `ож`, `uks`, `longleftrightarrow`, `viders` (target ranks: base_value=17:244540, first_product=34:235528, bound_value=50:210402, second_product=100:244540, answer=113:244540)
- Layer 27: ` .`, ` `.`, `．`, ` .=`, `-.` (target ranks: base_value=17:226984, first_product=34:234133, bound_value=50:208778, second_product=100:226984, answer=113:226984)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=17:186277, first_product=34:109229, bound_value=50:112131, second_product=100:186277, answer=113:186277)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `().` (target ranks: base_value=17:40547, first_product=34:16430, bound_value=50:12265, second_product=100:40547, answer=113:40547)
- Layer 30: ` .`, ` ..`, ` `.`, ` .*`, ` ."` (target ranks: base_value=17:10754, first_product=34:2231, bound_value=50:2406, second_product=100:10754, answer=113:10754)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:155, first_product=34:247, bound_value=50:219, second_product=100:155, answer=113:155)

### Filler position 33 (absolute token 908, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:283, second_product=100:20, answer=113:20)
- Layer 8: `�`, `↵`, `u`, `o`, `s` (target ranks: base_value=17:216, first_product=34:2786, bound_value=50:1492, second_product=100:216, answer=113:216)
- Layer 16: `内`, `长`, `漫`, `佩`, `吐` (target ranks: base_value=17:3457, first_product=34:16032, bound_value=50:19036, second_product=100:3457, answer=113:3457)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `égr`, `了` (target ranks: base_value=17:207612, first_product=34:209749, bound_value=50:150930, second_product=100:207612, answer=113:207612)
- Layer 25: `յ`, ` .`, `之`, `�`, `ား` (target ranks: base_value=17:178394, first_product=34:182825, bound_value=50:105932, second_product=100:178394, answer=113:178394)
- Layer 26: `յ`, ` .`, `erness`, ` .$`, `ီ` (target ranks: base_value=17:222303, first_product=34:196747, bound_value=50:127522, second_product=100:222303, answer=113:222303)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `/.` (target ranks: base_value=17:183388, first_product=34:204803, bound_value=50:163866, second_product=100:183388, answer=113:183388)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:143358, first_product=34:66334, bound_value=50:80024, second_product=100:143358, answer=113:143358)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `/.` (target ranks: base_value=17:16943, first_product=34:5277, bound_value=50:6279, second_product=100:16943, answer=113:16943)
- Layer 30: ` .`, ` ..`, ` `.`, ` ."`, ` .*` (target ranks: base_value=17:2433, first_product=34:344, bound_value=50:742, second_product=100:2433, answer=113:2433)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:146, first_product=34:174, bound_value=50:217, second_product=100:146, answer=113:146)

### Filler position 34 (absolute token 909, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `杈`, `u` (target ranks: base_value=17:145, first_product=34:4149, bound_value=50:1574, second_product=100:145, answer=113:145)
- Layer 16: `内`, `长`, `ights`, `吐`, `漫` (target ranks: base_value=17:5716, first_product=34:15690, bound_value=50:15052, second_product=100:5716, answer=113:5716)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ာ`, `最新发布` (target ranks: base_value=17:241539, first_product=34:234675, bound_value=50:218698, second_product=100:241539, answer=113:241539)
- Layer 25: `յ`, ` .`, `longleftrightarrow`, `之`, `ား` (target ranks: base_value=17:231548, first_product=34:223705, bound_value=50:196887, second_product=100:231548, answer=113:231548)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `最新发布`, `clearfix` (target ranks: base_value=17:242657, first_product=34:228225, bound_value=50:212987, second_product=100:242657, answer=113:242657)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:229016, first_product=34:231323, bound_value=50:222427, second_product=100:229016, answer=113:229016)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:203717, first_product=34:131833, bound_value=50:149867, second_product=100:203717, answer=113:203717)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `/.` (target ranks: base_value=17:45729, first_product=34:17784, bound_value=50:19742, second_product=100:45729, answer=113:45729)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:7317, first_product=34:1154, bound_value=50:2158, second_product=100:7317, answer=113:7317)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:126, first_product=34:136, bound_value=50:193, second_product=100:126, answer=113:126)

### Filler position 35 (absolute token 910, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `↵`, `u`, `↵↵` (target ranks: base_value=17:130, first_product=34:4172, bound_value=50:2268, second_product=100:130, answer=113:130)
- Layer 16: `内`, `ာ`, `ights`, `长`, `ံ` (target ranks: base_value=17:11965, first_product=34:29390, bound_value=50:35300, second_product=100:11965, answer=113:11965)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `yta`, `ာ` (target ranks: base_value=17:239188, first_product=34:235257, bound_value=50:207190, second_product=100:239188, answer=113:239188)
- Layer 25: `յ`, `之`, `longleftrightarrow`, ` .`, `viders` (target ranks: base_value=17:224453, first_product=34:220751, bound_value=50:167889, second_product=100:224453, answer=113:224453)
- Layer 26: `յ`, ` .`, `ာ`, `longleftrightarrow`, `viders` (target ranks: base_value=17:240499, first_product=34:224596, bound_value=50:194309, second_product=100:240499, answer=113:240499)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `/.` (target ranks: base_value=17:212480, first_product=34:228936, bound_value=50:209213, second_product=100:212480, answer=113:212480)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:166091, first_product=34:97819, bound_value=50:126679, second_product=100:166091, answer=113:166091)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:19409, first_product=34:9568, bound_value=50:10961, second_product=100:19409, answer=113:19409)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=17:4203, first_product=34:740, bound_value=50:1391, second_product=100:4203, answer=113:4203)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ,` (target ranks: base_value=17:203, first_product=34:331, bound_value=50:369, second_product=100:203, answer=113:203)

### Filler position 36 (absolute token 911, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:155, bound_value=50:279, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `↵`, `↵↵`, `s` (target ranks: base_value=17:207, first_product=34:2634, bound_value=50:988, second_product=100:207, answer=113:207)
- Layer 16: `ံ`, `内`, `漫`, `蓬`, `长` (target ranks: base_value=17:10525, first_product=34:27957, bound_value=50:36316, second_product=100:10525, answer=113:10525)
- Layer 24: `յ`, `longleftrightarrow`, `ာ`, `ights`, `yta` (target ranks: base_value=17:244586, first_product=34:242802, bound_value=50:227046, second_product=100:244586, answer=113:244586)
- Layer 25: `յ`, `longleftrightarrow`, `�`, `ာ`, `之` (target ranks: base_value=17:235001, first_product=34:234663, bound_value=50:196420, second_product=100:235001, answer=113:235001)
- Layer 26: `յ`, `ာ`, `antium`, `longleftrightarrow`, `xdd` (target ranks: base_value=17:242924, first_product=34:232796, bound_value=50:204709, second_product=100:242924, answer=113:242924)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `-.` (target ranks: base_value=17:209065, first_product=34:229210, bound_value=50:204820, second_product=100:209065, answer=113:209065)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:153876, first_product=34:114942, bound_value=50:117190, second_product=100:153876, answer=113:153876)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:23366, first_product=34:19146, bound_value=50:11929, second_product=100:23366, answer=113:23366)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:9821, first_product=34:3071, bound_value=50:3192, second_product=100:9821, answer=113:9821)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=17:196, first_product=34:320, bound_value=50:248, second_product=100:196, answer=113:196)

### Filler position 37 (absolute token 912, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:156, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `om`, `о`, `u` (target ranks: base_value=17:386, first_product=34:5936, bound_value=50:2356, second_product=100:386, answer=113:386)
- Layer 16: `内`, `佩`, `ံ`, `漫`, `提` (target ranks: base_value=17:7879, first_product=34:14257, bound_value=50:37020, second_product=100:7879, answer=113:7879)
- Layer 24: `յ`, `longleftrightarrow`, `ီ`, `ા`, `之` (target ranks: base_value=17:243728, first_product=34:237460, bound_value=50:219015, second_product=100:243728, answer=113:243728)
- Layer 25: `յ`, `longleftrightarrow`, `ီ`, `之`, `ackers` (target ranks: base_value=17:232740, first_product=34:219230, bound_value=50:175236, second_product=100:232740, answer=113:232740)
- Layer 26: `յ`, `usercontent`, `ီ`, ` .`, `ackers` (target ranks: base_value=17:243156, first_product=34:218813, bound_value=50:188938, second_product=100:243156, answer=113:243156)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:223333, first_product=34:229103, bound_value=50:209005, second_product=100:223333, answer=113:223333)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:174409, first_product=34:89032, bound_value=50:124774, second_product=100:174409, answer=113:174409)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:28343, first_product=34:12050, bound_value=50:14107, second_product=100:28343, answer=113:28343)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ."` (target ranks: base_value=17:7860, first_product=34:1829, bound_value=50:2949, second_product=100:7860, answer=113:7860)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:170, first_product=34:333, bound_value=50:333, second_product=100:170, answer=113:170)

### Filler position 38 (absolute token 913, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:156, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `u`, `杈`, `↵` (target ranks: base_value=17:354, first_product=34:10747, bound_value=50:3943, second_product=100:354, answer=113:354)
- Layer 16: `↵`, `佩`, `吐`, `提`, `长` (target ranks: base_value=17:6689, first_product=34:17294, bound_value=50:50925, second_product=100:6689, answer=113:6689)
- Layer 24: `յ`, `longleftrightarrow`, `ာ`, `cket`, `itical` (target ranks: base_value=17:237571, first_product=34:227482, bound_value=50:211944, second_product=100:237571, answer=113:237571)
- Layer 25: `յ`, `ား`, `cket`, ` .`, `之` (target ranks: base_value=17:220236, first_product=34:205438, bound_value=50:171349, second_product=100:220236, answer=113:220236)
- Layer 26: `յ`, `ာ`, `�`, `uks`, `ож` (target ranks: base_value=17:242184, first_product=34:218175, bound_value=50:203926, second_product=100:242184, answer=113:242184)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .=` (target ranks: base_value=17:207471, first_product=34:217357, bound_value=50:202535, second_product=100:207471, answer=113:207471)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=17:147192, first_product=34:75767, bound_value=50:109446, second_product=100:147192, answer=113:147192)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `().` (target ranks: base_value=17:22152, first_product=34:8032, bound_value=50:11884, second_product=100:22152, answer=113:22152)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` .*` (target ranks: base_value=17:9862, first_product=34:1847, bound_value=50:3781, second_product=100:9862, answer=113:9862)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:192, first_product=34:269, bound_value=50:326, second_product=100:192, answer=113:192)

### Filler position 39 (absolute token 914, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:279, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `u`, `s` (target ranks: base_value=17:393, first_product=34:5799, bound_value=50:1931, second_product=100:393, answer=113:393)
- Layer 16: `内`, `佩`, `提`, `长`, `吐` (target ranks: base_value=17:3997, first_product=34:16039, bound_value=50:34263, second_product=100:3997, answer=113:3997)
- Layer 24: `յ`, `之`, `ာ`, `ား`, `longleftrightarrow` (target ranks: base_value=17:193084, first_product=34:170630, bound_value=50:133375, second_product=100:193084, answer=113:193084)
- Layer 25: `յ`, ` .`, `之`, `ား`, `�` (target ranks: base_value=17:155718, first_product=34:136211, bound_value=50:92262, second_product=100:155718, answer=113:155718)
- Layer 26: `յ`, ` .`, `之`, `ီ`, `ာ` (target ranks: base_value=17:209190, first_product=34:151821, bound_value=50:111340, second_product=100:209190, answer=113:209190)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:167138, first_product=34:180294, bound_value=50:159111, second_product=100:167138, answer=113:167138)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:121343, first_product=34:48729, bound_value=50:78049, second_product=100:121343, answer=113:121343)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:11153, first_product=34:3025, bound_value=50:5530, second_product=100:11153, answer=113:11153)
- Layer 30: ` .`, ` ..`, ` `.`, ` ."`, ` .$` (target ranks: base_value=17:2561, first_product=34:327, bound_value=50:1091, second_product=100:2561, answer=113:2561)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:163, first_product=34:188, bound_value=50:264, second_product=100:163, answer=113:163)

### Filler position 40 (absolute token 915, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:284, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `u`, `↵↵` (target ranks: base_value=17:227, first_product=34:6095, bound_value=50:1669, second_product=100:227, answer=113:227)
- Layer 16: `内`, `三`, `博`, `白`, `有` (target ranks: base_value=17:7625, first_product=34:20728, bound_value=50:27846, second_product=100:7625, answer=113:7625)
- Layer 24: `յ`, `longleftrightarrow`, `ား`, `ာ`, `之` (target ranks: base_value=17:237990, first_product=34:219176, bound_value=50:204111, second_product=100:237990, answer=113:237990)
- Layer 25: `յ`, `longleftrightarrow`, ` .`, `ား`, `之` (target ranks: base_value=17:225366, first_product=34:201069, bound_value=50:180021, second_product=100:225366, answer=113:225366)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `ာ`, `imensional` (target ranks: base_value=17:238085, first_product=34:196731, bound_value=50:193837, second_product=100:238085, answer=113:238085)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:226559, first_product=34:218407, bound_value=50:214903, second_product=100:226559, answer=113:226559)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:188572, first_product=34:91367, bound_value=50:132883, second_product=100:188572, answer=113:188572)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:38309, first_product=34:10390, bound_value=50:15555, second_product=100:38309, answer=113:38309)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=17:7651, first_product=34:938, bound_value=50:2658, second_product=100:7651, answer=113:7651)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:146, first_product=34:146, bound_value=50:227, second_product=100:146, answer=113:146)

### Filler position 41 (absolute token 916, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:156, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `杈`, `↵↵` (target ranks: base_value=17:148, first_product=34:5743, bound_value=50:1877, second_product=100:148, answer=113:148)
- Layer 16: `内`, `三`, `atur`, `长`, `ာ` (target ranks: base_value=17:4376, first_product=34:10449, bound_value=50:29408, second_product=100:4376, answer=113:4376)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ား`, `ာ` (target ranks: base_value=17:221193, first_product=34:209685, bound_value=50:177293, second_product=100:221193, answer=113:221193)
- Layer 25: `յ`, `之`, `ား`, `longleftrightarrow`, `ီ` (target ranks: base_value=17:187282, first_product=34:175821, bound_value=50:121113, second_product=100:187282, answer=113:187282)
- Layer 26: `յ`, `ီ`, `ာ`, `kelse`, `硷` (target ranks: base_value=17:221788, first_product=34:182321, bound_value=50:154836, second_product=100:221788, answer=113:221788)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:189169, first_product=34:203013, bound_value=50:188275, second_product=100:189169, answer=113:189169)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:128470, first_product=34:60495, bound_value=50:98026, second_product=100:128470, answer=113:128470)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:11019, first_product=34:4555, bound_value=50:6491, second_product=100:11019, answer=113:11019)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=17:2502, first_product=34:438, bound_value=50:999, second_product=100:2502, answer=113:2502)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ,` (target ranks: base_value=17:198, first_product=34:385, bound_value=50:431, second_product=100:198, answer=113:198)

### Filler position 42 (absolute token 917, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `↵`, `o`, `�`, `↵↵`, `;` (target ranks: base_value=17:148, first_product=34:1634, bound_value=50:682, second_product=100:148, answer=113:148)
- Layer 16: `内`, `ံ`, `提`, `三`, `�` (target ranks: base_value=17:7632, first_product=34:14742, bound_value=50:44638, second_product=100:7632, answer=113:7632)
- Layer 24: `յ`, `ာ`, `ား`, `longleftrightarrow`, `之` (target ranks: base_value=17:236551, first_product=34:225014, bound_value=50:204944, second_product=100:236551, answer=113:236551)
- Layer 25: `յ`, `ား`, `ာ`, `longleftrightarrow`, `之` (target ranks: base_value=17:220814, first_product=34:211393, bound_value=50:175329, second_product=100:220814, answer=113:220814)
- Layer 26: `յ`, `ာ`, `longleftrightarrow`, `ား`, ` .$` (target ranks: base_value=17:239016, first_product=34:213055, bound_value=50:187712, second_product=100:239016, answer=113:239016)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, ` .=` (target ranks: base_value=17:188174, first_product=34:204124, bound_value=50:183639, second_product=100:188174, answer=113:188174)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=17:126895, first_product=34:76024, bound_value=50:93739, second_product=100:126895, answer=113:126895)
- Layer 29: ` .`, `．`, ` `.`, `-.`, `().` (target ranks: base_value=17:12385, first_product=34:7345, bound_value=50:6424, second_product=100:12385, answer=113:12385)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ,` (target ranks: base_value=17:5270, first_product=34:1281, bound_value=50:1970, second_product=100:5270, answer=113:5270)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:191, first_product=34:263, bound_value=50:233, second_product=100:191, answer=113:191)

### Filler position 43 (absolute token 918, surface ` .`)

- Layer 0: ` `, `_`, `-`, `↵`, `.` (target ranks: base_value=17:20, first_product=34:154, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `om` (target ranks: base_value=17:192, first_product=34:2531, bound_value=50:1076, second_product=100:192, answer=113:192)
- Layer 16: `内`, `提`, `ံ`, `与现实`, `佩` (target ranks: base_value=17:10999, first_product=34:10724, bound_value=50:37730, second_product=100:10999, answer=113:10999)
- Layer 24: `յ`, `longleftrightarrow`, `ာ`, `ા`, `ား` (target ranks: base_value=17:244804, first_product=34:231628, bound_value=50:214725, second_product=100:244804, answer=113:244804)
- Layer 25: `յ`, `longleftrightarrow`, `ား`, `ા`, `ာ` (target ranks: base_value=17:239002, first_product=34:217262, bound_value=50:185747, second_product=100:239002, answer=113:239002)
- Layer 26: `յ`, `longleftrightarrow`, `ા`, `ာ`, `ackers` (target ranks: base_value=17:245598, first_product=34:218243, bound_value=50:200372, second_product=100:245598, answer=113:245598)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=17:228258, first_product=34:222805, bound_value=50:209909, second_product=100:228258, answer=113:228258)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:185010, first_product=34:100223, bound_value=50:130462, second_product=100:185010, answer=113:185010)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:30077, first_product=34:11801, bound_value=50:12344, second_product=100:30077, answer=113:30077)
- Layer 30: ` .`, ` ..`, ` `.`, ` .$`, ` ."` (target ranks: base_value=17:10582, first_product=34:2238, bound_value=50:3190, second_product=100:10582, answer=113:10582)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:147, first_product=34:218, bound_value=50:239, second_product=100:147, answer=113:147)

### Filler position 44 (absolute token 919, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:158, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `o`, `�`, `om`, `u`, `↵` (target ranks: base_value=17:215, first_product=34:6602, bound_value=50:2715, second_product=100:215, answer=113:215)
- Layer 16: `提`, `佩`, `内`, `三`, `板` (target ranks: base_value=17:7316, first_product=34:9779, bound_value=50:46524, second_product=100:7316, answer=113:7316)
- Layer 24: `յ`, `longleftrightarrow`, `cket`, `ာ`, `erer` (target ranks: base_value=17:236142, first_product=34:205954, bound_value=50:192018, second_product=100:236142, answer=113:236142)
- Layer 25: `յ`, `ား`, `cket`, `longleftrightarrow`, `之` (target ranks: base_value=17:226636, first_product=34:186646, bound_value=50:157305, second_product=100:226636, answer=113:226636)
- Layer 26: `յ`, `ာ`, `uks`, `longleftrightarrow`, `ож` (target ranks: base_value=17:244557, first_product=34:208481, bound_value=50:201187, second_product=100:244557, answer=113:244557)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .=` (target ranks: base_value=17:219119, first_product=34:215179, bound_value=50:206907, second_product=100:219119, answer=113:219119)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=17:172263, first_product=34:88117, bound_value=50:129709, second_product=100:172263, answer=113:172263)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:25417, first_product=34:8920, bound_value=50:12485, second_product=100:25417, answer=113:25417)
- Layer 30: ` .`, ` ..`, ` `.`, ` ."`, ` ,` (target ranks: base_value=17:8115, first_product=34:1731, bound_value=50:3240, second_product=100:8115, answer=113:8115)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:193, first_product=34:263, bound_value=50:317, second_product=100:193, answer=113:193)

### Filler position 45 (absolute token 920, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:20, first_product=34:153, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `u`, `↵`, `s` (target ranks: base_value=17:284, first_product=34:6642, bound_value=50:2417, second_product=100:284, answer=113:284)
- Layer 16: `内`, `提`, `佩`, `白`, `三` (target ranks: base_value=17:3776, first_product=34:12647, bound_value=50:31249, second_product=100:3776, answer=113:3776)
- Layer 24: `յ`, `之`, `ာ`, `ား`, `longleftrightarrow` (target ranks: base_value=17:167389, first_product=34:132513, bound_value=50:106597, second_product=100:167389, answer=113:167389)
- Layer 25: `յ`, `之`, ` .`, `ား`, `�` (target ranks: base_value=17:133756, first_product=34:107435, bound_value=50:75033, second_product=100:133756, answer=113:133756)
- Layer 26: `յ`, `之`, ` .`, `ာ`, `erness` (target ranks: base_value=17:193572, first_product=34:117733, bound_value=50:91880, second_product=100:193572, answer=113:193572)
- Layer 27: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:149801, first_product=34:159581, bound_value=50:146457, second_product=100:149801, answer=113:149801)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:98726, first_product=34:44506, bound_value=50:72665, second_product=100:98726, answer=113:98726)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:6764, first_product=34:2389, bound_value=50:4147, second_product=100:6764, answer=113:6764)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=17:2030, first_product=34:387, bound_value=50:870, second_product=100:2030, answer=113:2030)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, `↵` (target ranks: base_value=17:166, first_product=34:198, bound_value=50:228, second_product=100:166, answer=113:166)

### Filler position 46 (absolute token 921, surface ` .`)

- Layer 0: ` `, `_`, `-`, `↵`, `.` (target ranks: base_value=17:20, first_product=34:154, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `s` (target ranks: base_value=17:226, first_product=34:3374, bound_value=50:1039, second_product=100:226, answer=113:226)
- Layer 16: `内`, `佩`, `提`, `白`, `三` (target ranks: base_value=17:14063, first_product=34:29955, bound_value=50:44610, second_product=100:14063, answer=113:14063)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ာ`, `ား` (target ranks: base_value=17:209797, first_product=34:174675, bound_value=50:148369, second_product=100:209797, answer=113:209797)
- Layer 25: `յ`, `之`, ` .`, `longleftrightarrow`, `ား` (target ranks: base_value=17:187868, first_product=34:155138, bound_value=50:125589, second_product=100:187868, answer=113:187868)
- Layer 26: `յ`, ` .`, `longleftrightarrow`, `之`, `imensional` (target ranks: base_value=17:218935, first_product=34:150917, bound_value=50:145634, second_product=100:218935, answer=113:218935)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:199857, first_product=34:195867, bound_value=50:185267, second_product=100:199857, answer=113:199857)
- Layer 28: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:153016, first_product=34:80777, bound_value=50:110752, second_product=100:153016, answer=113:153016)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:18751, first_product=34:6193, bound_value=50:8687, second_product=100:18751, answer=113:18751)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=17:4577, first_product=34:705, bound_value=50:1693, second_product=100:4577, answer=113:4577)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, `↵`, ` ` (target ranks: base_value=17:142, first_product=34:148, bound_value=50:204, second_product=100:142, answer=113:142)

### Filler position 47 (absolute token 922, surface ` .`)

- Layer 0: ` `, `_`, `-`, `↵`, `.` (target ranks: base_value=17:20, first_product=34:155, bound_value=50:282, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `杈` (target ranks: base_value=17:138, first_product=34:4290, bound_value=50:1328, second_product=100:138, answer=113:138)
- Layer 16: `内`, `atur`, `佩`, `ev`, `振` (target ranks: base_value=17:15603, first_product=34:26032, bound_value=50:36000, second_product=100:15603, answer=113:15603)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ambda`, `viders` (target ranks: base_value=17:208387, first_product=34:170012, bound_value=50:121488, second_product=100:208387, answer=113:208387)
- Layer 25: `յ`, `viders`, `之`, `longleftrightarrow`, `ား` (target ranks: base_value=17:174877, first_product=34:130214, bound_value=50:81514, second_product=100:174877, answer=113:174877)
- Layer 26: `յ`, `viders`, `uks`, `ာ`, `longleftrightarrow` (target ranks: base_value=17:205847, first_product=34:125190, bound_value=50:109322, second_product=100:205847, answer=113:205847)
- Layer 27: ` .`, ` `.`, `．`, `/.`, `-.` (target ranks: base_value=17:208335, first_product=34:192829, bound_value=50:179973, second_product=100:208335, answer=113:208335)
- Layer 28: ` .`, ` `.`, `．`, `/.`, `-.` (target ranks: base_value=17:153437, first_product=34:55402, bound_value=50:102088, second_product=100:153437, answer=113:153437)
- Layer 29: ` .`, ` `.`, `．`, `-.`, `/.` (target ranks: base_value=17:17191, first_product=34:3843, bound_value=50:7292, second_product=100:17191, answer=113:17191)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=17:3629, first_product=34:480, bound_value=50:1248, second_product=100:3629, answer=113:3629)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:139, first_product=34:166, bound_value=50:254, second_product=100:139, answer=113:139)

### Filler position 48 (absolute token 923, surface ` .`)

- Layer 0: ` `, `_`, `-`, `↵`, `.` (target ranks: base_value=17:20, first_product=34:154, bound_value=50:280, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `↵`, `↵↵`, `om` (target ranks: base_value=17:148, first_product=34:3507, bound_value=50:1127, second_product=100:148, answer=113:148)
- Layer 16: `内`, `佩`, `吐`, `ာ`, `避` (target ranks: base_value=17:7497, first_product=34:19506, bound_value=50:28429, second_product=100:7497, answer=113:7497)
- Layer 24: `ာ`, `之`, `յ`, `ား`, `allax` (target ranks: base_value=17:209814, first_product=34:191278, bound_value=50:161129, second_product=100:209814, answer=113:209814)
- Layer 25: `յ`, `ား`, `之`, `ာ`, `allax` (target ranks: base_value=17:180960, first_product=34:166644, bound_value=50:127792, second_product=100:180960, answer=113:180960)
- Layer 26: `յ`, `ာ`, `allax`, `uks`, `ား` (target ranks: base_value=17:228696, first_product=34:183746, bound_value=50:170861, second_product=100:228696, answer=113:228696)
- Layer 27: ` .`, `．`, ` `.`, ` .$`, `-.` (target ranks: base_value=17:197766, first_product=34:196993, bound_value=50:184994, second_product=100:197766, answer=113:197766)
- Layer 28: ` .`, `．`, `-.`, ` `.`, ` ..` (target ranks: base_value=17:150218, first_product=34:66913, bound_value=50:116918, second_product=100:150218, answer=113:150218)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `().` (target ranks: base_value=17:11933, first_product=34:4502, bound_value=50:8423, second_product=100:11933, answer=113:11933)
- Layer 30: ` .`, ` ..`, ` ,`, ` `.`, ` ."` (target ranks: base_value=17:2099, first_product=34:505, bound_value=50:1272, second_product=100:2099, answer=113:2099)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:166, first_product=34:247, bound_value=50:323, second_product=100:166, answer=113:166)

### Filler position 49 (absolute token 924, surface ` .`)

- Layer 0: ` `, `_`, `-`, `↵`, `.` (target ranks: base_value=17:20, first_product=34:154, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `om`, `↵↵`, `s` (target ranks: base_value=17:288, first_product=34:5197, bound_value=50:1591, second_product=100:288, answer=113:288)
- Layer 16: `内`, `有`, `吐`, `tin`, `提` (target ranks: base_value=17:2308, first_product=34:4980, bound_value=50:15812, second_product=100:2308, answer=113:2308)
- Layer 24: `յ`, `ား`, `ာ`, `း`, `了` (target ranks: base_value=17:202985, first_product=34:182240, bound_value=50:106371, second_product=100:202985, answer=113:202985)
- Layer 25: `յ`, `ား`, `ာ`, `之`, ` .` (target ranks: base_value=17:160008, first_product=34:134010, bound_value=50:61767, second_product=100:160008, answer=113:160008)
- Layer 26: `յ`, `ာ`, ` .=`, `ား`, `::.` (target ranks: base_value=17:232167, first_product=34:176379, bound_value=50:95709, second_product=100:232167, answer=113:232167)
- Layer 27: ` .`, `．`, ` ..`, `․`, ` .=` (target ranks: base_value=17:96675, first_product=34:70221, bound_value=50:34003, second_product=100:96675, answer=113:96675)
- Layer 28: ` .`, `．`, ` ..`, `․`, `️` (target ranks: base_value=17:68587, first_product=34:11543, bound_value=50:19276, second_product=100:68587, answer=113:68587)
- Layer 29: ` .`, `．`, `.`, ` ..`, `․` (target ranks: base_value=17:3337, first_product=34:974, bound_value=50:1305, second_product=100:3337, answer=113:3337)
- Layer 30: ` .`, ` ..`, ` ."`, `．`, ` ,` (target ranks: base_value=17:780, first_product=34:230, bound_value=50:552, second_product=100:780, answer=113:780)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:151, first_product=34:219, bound_value=50:266, second_product=100:151, answer=113:151)

### Filler position 50 (absolute token 925, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:20, first_product=34:155, bound_value=50:281, second_product=100:20, answer=113:20)
- Layer 8: `�`, `o`, `om`, `杈`, `s` (target ranks: base_value=17:429, first_product=34:11501, bound_value=50:3774, second_product=100:429, answer=113:429)
- Layer 16: `居`, `提`, `内`, `有`, `与现实` (target ranks: base_value=17:3275, first_product=34:9030, bound_value=50:31258, second_product=100:3275, answer=113:3275)
- Layer 24: `↵↵`, `答案`, `(answer`, ` answer`, `ambda` (target ranks: base_value=17:139976, first_product=34:136658, bound_value=50:73467, second_product=100:139976, answer=113:139976)
- Layer 25: `↵↵`, `答案`, ` answer`, `Answer`, ` Answer` (target ranks: base_value=17:95016, first_product=34:95333, bound_value=50:36919, second_product=100:95016, answer=113:95016)
- Layer 26: `答案`, `յ`, `↵↵`, `答案是`, `ာ` (target ranks: base_value=17:191464, first_product=34:147206, bound_value=50:85565, second_product=100:191464, answer=113:191464)
- Layer 27: ` Answer`, `Answer`, ` answer`, `↵↵`, `回答` (target ranks: base_value=17:76970, first_product=34:69636, bound_value=50:54688, second_product=100:76970, answer=113:76970)
- Layer 28: `↵↵`, ` Answer`, `Answer`, ` answer`, `答案` (target ranks: base_value=17:52888, first_product=34:37320, bound_value=50:25867, second_product=100:52888, answer=113:52888)
- Layer 29: `↵↵`, `Answer`, ` Answer`, ` answer`, `答案` (target ranks: base_value=17:401, first_product=34:548, bound_value=50:250, second_product=100:401, answer=113:401)
- Layer 30: `↵↵`, `↵`, ` Answer`, `Answer`, ` answer` (target ranks: base_value=17:99, first_product=34:82, bound_value=50:64, second_product=100:99, answer=113:99)
- Layer 31: `↵↵`, `<|im_end|>`, `↵`, ` .`, ` ↵↵` (target ranks: base_value=17:23, first_product=34:48, bound_value=50:34, second_product=100:23, answer=113:23)

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
qav = 83
yef = twice the number for qav plus 6
xew = 17
qur = twice the number for xew plus 16
doj = twice the number for qur minus 11
Question: What is twice the number for qur plus 13?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<|im_end|>
<|im_start|>assistant
<think>

</think>


```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
