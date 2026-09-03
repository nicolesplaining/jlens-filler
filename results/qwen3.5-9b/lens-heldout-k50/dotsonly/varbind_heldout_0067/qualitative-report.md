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
| Logit lens | `base_value=43` | 17 (L31, filler 35) | Never |
| Logit lens | `first_product=86` | 21 (L23, filler 8) | Never |
| Logit lens | `bound_value=99` | 103 (L31, filler 10) | Never |
| Logit lens | `second_product=198` | 4 (L30, filler 9) | L5, filler 3 (rank 9) |
| Logit lens | `answer=203` | 9 (L2, filler 4) | L2, filler 4 (rank 9) |

## Logit lens top-5 by filler position

### Filler position 1 (absolute token 877, surface ` .`)

- Layer 0: ` `, `-`, `<|endoftext|>`, `s`, `↵` (target ranks: base_value=43:148, first_product=86:383, bound_value=99:254, second_product=198:25, answer=203:28)
- Layer 8: `�`, `�`, `s`, `累`, `f` (target ranks: base_value=43:7148, first_product=86:4301, bound_value=99:13064, second_product=198:320, answer=203:679)
- Layer 16: `再`, `又`, `提`, `得`, `联` (target ranks: base_value=43:22899, first_product=86:10518, bound_value=99:10088, second_product=198:12614, answer=203:5966)
- Layer 24: ` reference`, `参考`, `参照`, ` Reference`, `/reference` (target ranks: base_value=43:218930, first_product=86:181073, bound_value=99:225363, second_product=198:196138, answer=203:112221)
- Layer 25: `基础`, ` referenced`, ` reference`, `参照`, `参考` (target ranks: base_value=43:195362, first_product=86:160034, bound_value=99:177874, second_product=198:154300, answer=203:70612)
- Layer 26: ` references`, ` refer`, ` reference`, `基础`, `参考` (target ranks: base_value=43:153885, first_product=86:99465, bound_value=99:150605, second_product=198:136894, answer=203:43261)
- Layer 27: `mik`, ` mik`, ` Mik`, `微`, ` micro` (target ranks: base_value=43:245508, first_product=86:243763, bound_value=99:245133, second_product=198:247596, answer=203:229227)
- Layer 28: `mik`, ` mik`, ` Mik`, `微`, ` micro` (target ranks: base_value=43:243213, first_product=86:234979, bound_value=99:246203, second_product=198:248018, answer=203:224525)
- Layer 29: `mik`, ` mik`, ` micro`, ` Mik`, `微` (target ranks: base_value=43:149475, first_product=86:127863, bound_value=99:218854, second_product=198:196807, answer=203:75867)
- Layer 30: ` .`, ` mik`, `mik`, ` micro`, ` ru` (target ranks: base_value=43:2881, first_product=86:8698, bound_value=99:23688, second_product=198:3205, answer=203:615)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` ru`, ` :` (target ranks: base_value=43:195, first_product=86:404, bound_value=99:291, second_product=198:71, answer=203:162)

### Filler position 2 (absolute token 878, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:127, first_product=86:201, bound_value=99:134, second_product=198:22, answer=203:39)
- Layer 8: `�`, `us`, `m`, `c`, `i` (target ranks: base_value=43:2036, first_product=86:2832, bound_value=99:12323, second_product=198:223, answer=203:266)
- Layer 16: `提`, ` a`, `基础`, `先`, `yst` (target ranks: base_value=43:24046, first_product=86:17870, bound_value=99:15370, second_product=198:4085, answer=203:2724)
- Layer 24: ` variables`, `变量`, ` Variables`, `变量的`, `ukt` (target ranks: base_value=43:193601, first_product=86:201857, bound_value=99:216431, second_product=198:140325, answer=203:119141)
- Layer 25: ` variables`, `变量`, ` Variables`, `变量的`, ` variable` (target ranks: base_value=43:177109, first_product=86:188065, bound_value=99:181002, second_product=198:110926, answer=203:90989)
- Layer 26: ` variables`, ` Variables`, `变量`, `变量的`, `基础` (target ranks: base_value=43:184032, first_product=86:177647, bound_value=99:190488, second_product=198:163633, answer=203:111158)
- Layer 27: ` ru`, `mik`, ` mik`, ` RU`, ` ру` (target ranks: base_value=43:242382, first_product=86:245163, bound_value=99:244676, second_product=198:246884, answer=203:237160)
- Layer 28: ` ru`, `mik`, ` mik`, `微`, ` ру` (target ranks: base_value=43:232538, first_product=86:237585, bound_value=99:245333, second_product=198:246684, answer=203:221186)
- Layer 29: ` ru`, ` mik`, `mik`, `RU`, ` micro` (target ranks: base_value=43:119170, first_product=86:148510, bound_value=99:216430, second_product=198:154565, answer=203:79222)
- Layer 30: ` .`, ` ru`, `RU`, ` mik`, ` micro` (target ranks: base_value=43:1622, first_product=86:11714, bound_value=99:28371, second_product=198:3503, answer=203:611)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` ,`, ` ru` (target ranks: base_value=43:75, first_product=86:292, bound_value=99:234, second_product=198:52, answer=203:81)

### Filler position 3 (absolute token 879, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=43:132, first_product=86:198, bound_value=99:139, second_product=198:21, answer=203:39)
- Layer 8: `o`, `us`, `en`, `u`, `er` (target ranks: base_value=43:11410, first_product=86:11444, bound_value=99:21064, second_product=198:1188, answer=203:2280)
- Layer 16: `站`, `azi`, `+self`, `-sales`, `翰` (target ranks: base_value=43:39413, first_product=86:23732, bound_value=99:76864, second_product=198:19446, answer=203:27174)
- Layer 24: ` esplic`, `λεί`, `zgl`, `้ง`, ` eighty` (target ranks: base_value=43:227281, first_product=86:2701, bound_value=99:64317, second_product=198:243992, answer=203:243992)
- Layer 25: `莽`, `спен`, `oglob`, `ณะ`, `�` (target ranks: base_value=43:184050, first_product=86:14180, bound_value=99:26844, second_product=198:223069, answer=203:216247)
- Layer 26: `一百`, `两百`, `莽`, ` ratus`, `二百` (target ranks: base_value=43:233806, first_product=86:55924, bound_value=99:18618, second_product=198:187749, answer=203:206181)
- Layer 27: `inete`, `十九`, ` ninete`, `十九章`, `第二百零` (target ranks: base_value=43:247316, first_product=86:248006, bound_value=99:36837, second_product=198:124552, answer=203:137693)
- Layer 28: `十九`, `inete`, ` nineteen`, ` ninete`, `十九章` (target ranks: base_value=43:245185, first_product=86:248123, bound_value=99:142020, second_product=198:7245, answer=203:89524)
- Layer 29: `inete`, `十九章`, `惊魂`, ` ninete`, ` Nin` (target ranks: base_value=43:244724, first_product=86:241978, bound_value=99:224067, second_product=198:29897, answer=203:120385)
- Layer 30: `惊魂`, `inete`, `_editor`, ` Bros`, ` sb` (target ranks: base_value=43:95479, first_product=86:40231, bound_value=99:142397, second_product=198:9, answer=203:1765)
- Layer 31: ` .`, ` :`, `.`, ` ,`, ` ..` (target ranks: base_value=43:21074, first_product=86:7633, bound_value=99:151179, second_product=198:3180, answer=203:4749)

### Filler position 4 (absolute token 880, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:140, first_product=86:199, bound_value=99:142, second_product=198:21, answer=203:41)
- Layer 8: `an`, `i`, `ut`, `通`, `ri` (target ranks: base_value=43:9040, first_product=86:14514, bound_value=99:8512, second_product=198:2137, answer=203:1097)
- Layer 16: `ällen`, `uto`, `屋`, `cü`, `明` (target ranks: base_value=43:165036, first_product=86:85839, bound_value=99:77799, second_product=198:172193, answer=203:35973)
- Layer 24: `变量`, ` variables`, ` variable`, ` Variables`, `变量的` (target ranks: base_value=43:240573, first_product=86:225371, bound_value=99:214886, second_product=198:236521, answer=203:217749)
- Layer 25: `变量`, ` variables`, ` variable`, ` Variables`, ` Variable` (target ranks: base_value=43:232712, first_product=86:222447, bound_value=99:189171, second_product=198:215480, answer=203:183994)
- Layer 26: `定义`, ` definitions`, ` variables`, `变量`, ` definition` (target ranks: base_value=43:177576, first_product=86:122370, bound_value=99:124900, second_product=198:142981, answer=203:113610)
- Layer 27: ` variable`, `变量`, `variable`, ` variables`, ` Variable` (target ranks: base_value=43:236419, first_product=86:219617, bound_value=99:204113, second_product=198:242207, answer=203:219076)
- Layer 28: ` variable`, `变量`, ` variables`, `variable`, ` Variable` (target ranks: base_value=43:227751, first_product=86:125850, bound_value=99:192741, second_product=198:232755, answer=203:162711)
- Layer 29: ` definitions`, `定义`, ` variable`, ` variables`, ` var` (target ranks: base_value=43:98785, first_product=86:28860, bound_value=99:122338, second_product=198:58518, answer=203:45164)
- Layer 30: ` .`, ` ..`, ` definitions`, ` var`, ` variables` (target ranks: base_value=43:3486, first_product=86:4300, bound_value=99:29399, second_product=198:1899, answer=203:733)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` :`, ` ` (target ranks: base_value=43:308, first_product=86:462, bound_value=99:566, second_product=198:55, answer=203:173)

### Filler position 5 (absolute token 881, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=43:140, first_product=86:190, bound_value=99:142, second_product=198:21, answer=203:40)
- Layer 8: `触`, `istrator`, `pring`, `�`, `us` (target ranks: base_value=43:39910, first_product=86:47396, bound_value=99:42346, second_product=198:24847, answer=203:27354)
- Layer 16: `orial`, `ient`, `提`, `派`, `地` (target ranks: base_value=43:126700, first_product=86:68732, bound_value=99:91905, second_product=198:90513, answer=203:99724)
- Layer 24: `的值`, `ationale`, `cript`, `uations`, `olygon` (target ranks: base_value=43:143069, first_product=86:159930, bound_value=99:210948, second_product=198:164324, answer=203:55184)
- Layer 25: `的值`, `<think>`, ` twice`, `等于`, `ationale` (target ranks: base_value=43:83167, first_product=86:115470, bound_value=99:123814, second_product=198:113743, answer=203:18757)
- Layer 26: ` twice`, `的值`, `等于`, `️`, ` Twice` (target ranks: base_value=43:57451, first_product=86:94310, bound_value=99:126357, second_product=198:108465, answer=203:9001)
- Layer 27: ` mik`, `mik`, ` Mik`, ` mic`, ` micro` (target ranks: base_value=43:175994, first_product=86:216394, bound_value=99:226161, second_product=198:231757, answer=203:89838)
- Layer 28: ` mik`, `mik`, ` Mik`, ` micro`, ` mic` (target ranks: base_value=43:146053, first_product=86:152428, bound_value=99:213851, second_product=198:210635, answer=203:27824)
- Layer 29: ` mik`, `mik`, ` Mik`, ` micro`, ` mic` (target ranks: base_value=43:33617, first_product=86:51513, bound_value=99:147057, second_product=198:41111, answer=203:4452)
- Layer 30: ` mik`, `mik`, ` micro`, ` Mik`, ` mic` (target ranks: base_value=43:976, first_product=86:7130, bound_value=99:21776, second_product=198:1019, answer=203:115)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` :`, ` ` (target ranks: base_value=43:100, first_product=86:538, bound_value=99:635, second_product=198:87, answer=203:117)

### Filler position 6 (absolute token 882, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:137, first_product=86:186, bound_value=99:142, second_product=198:21, answer=203:40)
- Layer 8: `ainer`, `an`, `�`, `t`, `触` (target ranks: base_value=43:19083, first_product=86:27626, bound_value=99:20780, second_product=198:5095, answer=203:4503)
- Layer 16: `漫`, `扣`, `�`, `旗`, `明` (target ranks: base_value=43:67509, first_product=86:103708, bound_value=99:71185, second_product=198:56044, answer=203:13678)
- Layer 24: `/filepath`, `່`, `stery`, `ာ`, `员` (target ranks: base_value=43:149382, first_product=86:133258, bound_value=99:105137, second_product=198:176059, answer=203:177184)
- Layer 25: `/filepath`, `່`, `asi`, `而又`, `ာ` (target ranks: base_value=43:135056, first_product=86:125523, bound_value=99:95521, second_product=198:157658, answer=203:152775)
- Layer 26: `յ`, `asi`, `Lorem`, `່`, `usercontent` (target ranks: base_value=43:64327, first_product=86:75374, bound_value=99:58260, second_product=198:161222, answer=203:110048)
- Layer 27: ` .`, `-.`, ` `.`, `．`, ` ..` (target ranks: base_value=43:104780, first_product=86:169288, bound_value=99:121192, second_product=198:181451, answer=203:166594)
- Layer 28: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=43:58199, first_product=86:68756, bound_value=99:96735, second_product=198:124606, answer=203:76048)
- Layer 29: ` .`, `-.`, `．`, `!.`, ` {.` (target ranks: base_value=43:6357, first_product=86:18218, bound_value=99:35512, second_product=198:11627, answer=203:5493)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:147, first_product=86:683, bound_value=99:1589, second_product=198:646, answer=203:92)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=43:41, first_product=86:93, bound_value=99:135, second_product=198:42, answer=203:37)

### Filler position 7 (absolute token 883, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=43:134, first_product=86:178, bound_value=99:143, second_product=198:20, answer=203:38)
- Layer 8: `u`, `�`, `�`, `质`, `istrator` (target ranks: base_value=43:20670, first_product=86:24610, bound_value=99:24680, second_product=198:10971, answer=203:5294)
- Layer 16: `漫`, `禁`, `�`, ` `, `地` (target ranks: base_value=43:8935, first_product=86:11464, bound_value=99:18043, second_product=198:2304, answer=203:274)
- Layer 24: `່`, `ariate`, `cket`, `ာ`, `íguez` (target ranks: base_value=43:113484, first_product=86:138666, bound_value=99:123138, second_product=198:164640, answer=203:111123)
- Layer 25: `່`, `ariate`, `cket`, ` .`, `而又` (target ranks: base_value=43:82575, first_product=86:98090, bound_value=99:88080, second_product=198:141707, answer=203:82850)
- Layer 26: `յ`, ` .`, `etes`, `osing`, `ာ` (target ranks: base_value=43:45184, first_product=86:88728, bound_value=99:77647, second_product=198:165100, answer=203:62620)
- Layer 27: ` .`, ` `.`, ` ..`, `．`, `-.` (target ranks: base_value=43:82108, first_product=86:174673, bound_value=99:158576, second_product=198:196706, answer=203:134167)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:37018, first_product=86:61913, bound_value=99:102515, second_product=198:144118, answer=203:44616)
- Layer 29: ` .`, `-.`, ` `.`, `．`, ` ..` (target ranks: base_value=43:1771, first_product=86:10877, bound_value=99:21941, second_product=198:6323, answer=203:1517)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=43:126, first_product=86:808, bound_value=99:1388, second_product=198:638, answer=203:123)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=43:33, first_product=86:129, bound_value=99:164, second_product=198:68, answer=203:60)

### Filler position 8 (absolute token 884, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:133, first_product=86:176, bound_value=99:141, second_product=198:18, answer=203:38)
- Layer 8: `u`, `t`, `i`, `青`, `�` (target ranks: base_value=43:1821, first_product=86:1428, bound_value=99:6933, second_product=198:253, answer=203:639)
- Layer 16: `azi`, `erce`, `得`, `计算`, `�` (target ranks: base_value=43:14800, first_product=86:5920, bound_value=99:38551, second_product=198:25932, answer=203:13344)
- Layer 24: `�`, `λεί`, ` eighty`, `吁`, ` esplic` (target ranks: base_value=43:229001, first_product=86:2225, bound_value=99:45360, second_product=198:242458, answer=203:243413)
- Layer 25: `�`, `oglob`, `莽`, `спен`, `CursorPosition` (target ranks: base_value=43:194770, first_product=86:13770, bound_value=99:19835, second_product=198:218576, answer=203:215640)
- Layer 26: `一百`, `两百`, `二百`, `莽`, `�` (target ranks: base_value=43:234143, first_product=86:90305, bound_value=99:23084, second_product=198:184389, answer=203:197413)
- Layer 27: `十九`, `inete`, `第二百零`, ` ninete`, `十九章` (target ranks: base_value=43:247246, first_product=86:248150, bound_value=99:59381, second_product=198:90586, answer=203:100834)
- Layer 28: `十九`, `inete`, ` nineteen`, ` ninete`, `十九章` (target ranks: base_value=43:241240, first_product=86:247912, bound_value=99:173626, second_product=198:12640, answer=203:31674)
- Layer 29: `inete`, `十九章`, `惊魂`, ` nineteenth`, ` Bros` (target ranks: base_value=43:226550, first_product=86:172729, bound_value=99:201647, second_product=198:19236, answer=203:38212)
- Layer 30: ` .`, ` Bros`, `_editor`, ` sb`, `惊魂` (target ranks: base_value=43:56913, first_product=86:20130, bound_value=99:96392, second_product=198:10, answer=203:330)
- Layer 31: ` .`, ` ,`, ` :`, ` `, `.` (target ranks: base_value=43:816, first_product=86:965, bound_value=99:15506, second_product=198:376, answer=203:661)

### Filler position 9 (absolute token 885, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:131, first_product=86:173, bound_value=99:143, second_product=198:21, answer=203:38)
- Layer 8: `�`, `en`, `�`, `o`, `u` (target ranks: base_value=43:18423, first_product=86:6122, bound_value=99:7342, second_product=198:10159, answer=203:11302)
- Layer 16: `<think>`, `得`, `地方`, `�`, `azi` (target ranks: base_value=43:4984, first_product=86:3717, bound_value=99:9756, second_product=198:8393, answer=203:5636)
- Layer 24: `�`, `λεί`, `usercontent`, `吁`, ` eighty` (target ranks: base_value=43:219470, first_product=86:5559, bound_value=99:42146, second_product=198:227205, answer=203:236260)
- Layer 25: `�`, `崎`, `usercontent`, `oglob`, `спен` (target ranks: base_value=43:179302, first_product=86:15048, bound_value=99:14555, second_product=198:205890, answer=203:212051)
- Layer 26: `一百`, `两百`, `�`, `九十`, `二百` (target ranks: base_value=43:230486, first_product=86:65555, bound_value=99:9019, second_product=198:106542, answer=203:179293)
- Layer 27: `十九`, `inete`, `第二百零`, `十九章`, `一百` (target ranks: base_value=43:247925, first_product=86:247935, bound_value=99:39257, second_product=198:53215, answer=203:105130)
- Layer 28: `十九`, `inete`, ` nineteen`, `十九章`, ` nineteenth` (target ranks: base_value=43:240250, first_product=86:248003, bound_value=99:160918, second_product=198:9634, answer=203:102932)
- Layer 29: `inete`, `熙`, ` Bros`, `丹`, `adh` (target ranks: base_value=43:213971, first_product=86:176141, bound_value=99:196901, second_product=198:8695, answer=203:60472)
- Layer 30: ` .`, ` Bros`, ` ..`, `1`, ` sb` (target ranks: base_value=43:43314, first_product=86:13781, bound_value=99:65522, second_product=198:4, answer=203:368)
- Layer 31: ` .`, ` ,`, `<|im_end|>`, `.`, ` :` (target ranks: base_value=43:361, first_product=86:492, bound_value=99:4430, second_product=198:357, answer=203:521)

### Filler position 10 (absolute token 886, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:131, first_product=86:173, bound_value=99:140, second_product=198:19, answer=203:38)
- Layer 8: `和`, `o`, `en`, `u`, `­` (target ranks: base_value=43:13634, first_product=86:13515, bound_value=99:12972, second_product=198:4001, answer=203:9616)
- Layer 16: `服`, `提`, `内`, `地`, `�` (target ranks: base_value=43:53009, first_product=86:22458, bound_value=99:80986, second_product=198:7393, answer=203:6570)
- Layer 24: `յ`, `�`, `cket`, `ěn`, `enser` (target ranks: base_value=43:224049, first_product=86:199507, bound_value=99:210907, second_product=198:211646, answer=203:176266)
- Layer 25: `յ`, `cket`, `�`, `longleftrightarrow`, `ож` (target ranks: base_value=43:210505, first_product=86:162554, bound_value=99:185722, second_product=198:197051, answer=203:157080)
- Layer 26: `�`, `յ`, `asi`, `最新发布`, `ек` (target ranks: base_value=43:144278, first_product=86:79129, bound_value=99:124737, second_product=198:161187, answer=203:95178)
- Layer 27: ` .`, `-.`, ` `.`, ` $.`, `．` (target ranks: base_value=43:177882, first_product=86:177882, bound_value=99:180883, second_product=198:176830, answer=203:168496)
- Layer 28: ` .`, `-.`, `!.`, ` `.`, ` $.` (target ranks: base_value=43:115898, first_product=86:76497, bound_value=99:166796, second_product=198:153430, answer=203:115283)
- Layer 29: ` .`, `-.`, `!.`, ` `.`, `．` (target ranks: base_value=43:11425, first_product=86:12209, bound_value=99:54632, second_product=198:17273, answer=203:9885)
- Layer 30: ` .`, ` ..`, ` `.`, `-.`, `.` (target ranks: base_value=43:267, first_product=86:391, bound_value=99:1231, second_product=198:763, answer=203:162)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=43:83, first_product=86:95, bound_value=99:103, second_product=198:54, answer=203:61)

### Filler position 11 (absolute token 887, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:131, first_product=86:170, bound_value=99:140, second_product=198:18, answer=203:37)
- Layer 8: `�`, `�`, `u`, `干`, `和` (target ranks: base_value=43:4437, first_product=86:10108, bound_value=99:13199, second_product=198:3388, answer=203:3012)
- Layer 16: `提`, `地`, `服`, `ံ`, `率` (target ranks: base_value=43:37794, first_product=86:22839, bound_value=99:85297, second_product=198:7397, answer=203:6442)
- Layer 24: `之`, `员`, `ာ`, `յ`, `家` (target ranks: base_value=43:188566, first_product=86:183018, bound_value=99:178253, second_product=198:207466, answer=203:171102)
- Layer 25: `յ`, `ာ`, `之`, `而又`, `家` (target ranks: base_value=43:162350, first_product=86:144683, bound_value=99:142786, second_product=198:182249, answer=203:140865)
- Layer 26: `յ`, `而又`, `ек`, ` .`, `ာ` (target ranks: base_value=43:109509, first_product=86:107401, bound_value=99:124777, second_product=198:203634, answer=203:129241)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=43:96657, first_product=86:166470, bound_value=99:176834, second_product=198:192232, answer=203:160176)
- Layer 28: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=43:48806, first_product=86:79378, bound_value=99:163860, second_product=198:173249, answer=203:110186)
- Layer 29: ` .`, `-.`, `!.`, ` `.`, `．` (target ranks: base_value=43:2851, first_product=86:16427, bound_value=99:55262, second_product=198:19461, answer=203:9158)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=43:140, first_product=86:966, bound_value=99:3068, second_product=198:1581, answer=203:210)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:26, first_product=86:116, bound_value=99:160, second_product=198:89, answer=203:46)

### Filler position 12 (absolute token 888, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:130, first_product=86:169, bound_value=99:140, second_product=198:19, answer=203:37)
- Layer 8: `u`, `s`, `有`, `t`, `en` (target ranks: base_value=43:1325, first_product=86:2626, bound_value=99:2665, second_product=198:340, answer=203:359)
- Layer 16: `�`, `提`, `再`, `兀`, `漫` (target ranks: base_value=43:40236, first_product=86:14162, bound_value=99:53382, second_product=198:20015, answer=203:7399)
- Layer 24: `íguez`, `յ`, `longleftrightarrow`, `ာ`, `世` (target ranks: base_value=43:199249, first_product=86:199249, bound_value=99:180968, second_product=198:224881, answer=203:204429)
- Layer 25: `յ`, `cket`, `longleftrightarrow`, `而又`, `ာ` (target ranks: base_value=43:191222, first_product=86:187227, bound_value=99:169833, second_product=198:211371, answer=203:189290)
- Layer 26: `յ`, `scht`, ` .`, `ож`, `longleftrightarrow` (target ranks: base_value=43:169351, first_product=86:191001, bound_value=99:169351, second_product=198:232546, answer=203:199142)
- Layer 27: ` .`, ` `.`, ` .$`, `．`, ` ..` (target ranks: base_value=43:155971, first_product=86:222257, bound_value=99:205137, second_product=198:225759, answer=203:208748)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:90823, first_product=86:140184, bound_value=99:185568, second_product=198:195542, answer=203:136517)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=43:4774, first_product=86:27419, bound_value=99:52351, second_product=198:20101, answer=203:8799)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:288, first_product=86:2826, bound_value=99:6406, second_product=198:3448, answer=203:499)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:42, first_product=86:216, bound_value=99:281, second_product=198:147, answer=203:109)

### Filler position 13 (absolute token 889, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:127, first_product=86:169, bound_value=99:139, second_product=198:19, answer=203:37)
- Layer 8: `�`, `�`, `s`, `r`, `青` (target ranks: base_value=43:8870, first_product=86:9480, bound_value=99:16939, second_product=198:6509, answer=203:2067)
- Layer 16: `提`, `ံ`, `望`, `�`, `ersi` (target ranks: base_value=43:111073, first_product=86:41702, bound_value=99:100492, second_product=198:68997, answer=203:26756)
- Layer 24: `յ`, `scht`, `cket`, `longleftrightarrow`, `íguez` (target ranks: base_value=43:214550, first_product=86:208887, bound_value=99:205071, second_product=198:230646, answer=203:206598)
- Layer 25: `յ`, `cket`, `scht`, `atórios`, `viders` (target ranks: base_value=43:202182, first_product=86:186689, bound_value=99:185195, second_product=198:219069, answer=203:190140)
- Layer 26: `յ`, `scht`, `uks`, `viders`, `schen` (target ranks: base_value=43:184743, first_product=86:185761, bound_value=99:182286, second_product=198:232589, answer=203:191797)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` .=` (target ranks: base_value=43:171359, first_product=86:219376, bound_value=99:214586, second_product=198:223093, answer=203:205607)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `!.` (target ranks: base_value=43:109097, first_product=86:124778, bound_value=99:189156, second_product=198:180581, answer=203:125970)
- Layer 29: ` .`, ` `.`, `-.`, `!.`, `．` (target ranks: base_value=43:9689, first_product=86:31843, bound_value=99:71151, second_product=198:25557, answer=203:10604)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=43:243, first_product=86:1445, bound_value=99:3712, second_product=198:2058, answer=203:336)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:53, first_product=86:218, bound_value=99:272, second_product=198:159, answer=203:145)

### Filler position 14 (absolute token 890, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:126, first_product=86:169, bound_value=99:139, second_product=198:19, answer=203:37)
- Layer 8: `u`, `和`, `表示`, `及`, `有` (target ranks: base_value=43:3689, first_product=86:5195, bound_value=99:6486, second_product=198:1077, answer=203:3030)
- Layer 16: `ံ`, `望`, `地`, `提`, `口` (target ranks: base_value=43:59711, first_product=86:17521, bound_value=99:87211, second_product=198:20515, answer=203:19388)
- Layer 24: `յ`, `longleftrightarrow`, `ек`, `家`, `ာ` (target ranks: base_value=43:217096, first_product=86:191674, bound_value=99:209715, second_product=198:220083, answer=203:198518)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `ек`, `itical` (target ranks: base_value=43:203310, first_product=86:164964, bound_value=99:184456, second_product=198:201718, answer=203:179378)
- Layer 26: `յ`, `ек`, `ာ`, `uks`, `longleftrightarrow` (target ranks: base_value=43:150732, first_product=86:113460, bound_value=99:137813, second_product=198:198821, answer=203:140227)
- Layer 27: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:132793, first_product=86:187648, bound_value=99:186765, second_product=198:190413, answer=203:166032)
- Layer 28: ` .`, `-.`, ` `.`, `．`, ` ..` (target ranks: base_value=43:76083, first_product=86:95415, bound_value=99:151562, second_product=198:126021, answer=203:80644)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `.` (target ranks: base_value=43:6239, first_product=86:19633, bound_value=99:45402, second_product=198:12595, answer=203:6343)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:217, first_product=86:980, bound_value=99:2411, second_product=198:1194, answer=203:254)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:53, first_product=86:185, bound_value=99:211, second_product=198:148, answer=203:108)

### Filler position 15 (absolute token 891, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:124, first_product=86:166, bound_value=99:137, second_product=198:19, answer=203:37)
- Layer 8: `u`, `ared`, `s`, `和`, `t` (target ranks: base_value=43:2630, first_product=86:5364, bound_value=99:4225, second_product=198:1495, answer=203:1579)
- Layer 16: `提`, `ံ`, `ods`, `地`, `依` (target ranks: base_value=43:53131, first_product=86:24965, bound_value=99:86970, second_product=198:15957, answer=203:9692)
- Layer 24: `յ`, `之`, `家`, `longleftrightarrow`, `ambda` (target ranks: base_value=43:181451, first_product=86:186529, bound_value=99:175019, second_product=198:203538, answer=203:158530)
- Layer 25: `յ`, `家`, `之`, `longleftrightarrow`, `而又` (target ranks: base_value=43:160820, first_product=86:157196, bound_value=99:143320, second_product=198:179642, answer=203:132928)
- Layer 26: `յ`, `uks`, ` .`, `而又`, `longleftrightarrow` (target ranks: base_value=43:104814, first_product=86:127631, bound_value=99:120840, second_product=198:195070, answer=203:121400)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `-.` (target ranks: base_value=43:111669, first_product=86:195661, bound_value=99:188606, second_product=198:204478, answer=203:168167)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:58942, first_product=86:111386, bound_value=99:160034, second_product=198:159452, answer=203:91317)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=43:3204, first_product=86:23478, bound_value=99:42355, second_product=198:16697, answer=203:5376)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:213, first_product=86:2058, bound_value=99:4635, second_product=198:2593, answer=203:343)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:46, first_product=86:242, bound_value=99:298, second_product=198:193, answer=203:115)

### Filler position 16 (absolute token 892, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:119, first_product=86:166, bound_value=99:137, second_product=198:19, answer=203:36)
- Layer 8: `s`, `r`, `u`, `m`, `o` (target ranks: base_value=43:4242, first_product=86:7780, bound_value=99:9254, second_product=198:1561, answer=203:1106)
- Layer 16: `提`, `ods`, `ံ`, `始`, `内` (target ranks: base_value=43:44698, first_product=86:29027, bound_value=99:87112, second_product=198:28180, answer=203:18273)
- Layer 24: `յ`, `longleftrightarrow`, `家`, `scht`, `íguez` (target ranks: base_value=43:194321, first_product=86:209229, bound_value=99:199462, second_product=198:225735, answer=203:190995)
- Layer 25: `յ`, `家`, `cket`, `scht`, `longleftrightarrow` (target ranks: base_value=43:183206, first_product=86:189172, bound_value=99:174029, second_product=198:211849, answer=203:177905)
- Layer 26: `յ`, `uks`, `scht`, `longleftrightarrow`, `年一季度` (target ranks: base_value=43:158366, first_product=86:194159, bound_value=99:175035, second_product=198:230620, answer=203:186754)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=43:144188, first_product=86:224057, bound_value=99:210780, second_product=198:223534, answer=203:199717)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:82266, first_product=86:148537, bound_value=99:185094, second_product=198:174224, answer=203:111065)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `().` (target ranks: base_value=43:7214, first_product=86:43990, bound_value=99:68717, second_product=198:26922, answer=203:10522)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:270, first_product=86:2851, bound_value=99:5847, second_product=198:2936, answer=203:435)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:48, first_product=86:276, bound_value=99:339, second_product=198:178, answer=203:106)

### Filler position 17 (absolute token 893, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:117, first_product=86:166, bound_value=99:132, second_product=198:19, answer=203:36)
- Layer 8: `s`, `u`, `o`, `r`, `m` (target ranks: base_value=43:5438, first_product=86:9393, bound_value=99:11114, second_product=198:1578, answer=203:1528)
- Layer 16: `提`, `地`, `ods`, `内`, `壁` (target ranks: base_value=43:79655, first_product=86:26174, bound_value=99:81195, second_product=198:16377, answer=203:16910)
- Layer 24: `յ`, `家`, `ек`, `longleftrightarrow`, `ambda` (target ranks: base_value=43:186195, first_product=86:200606, bound_value=99:198274, second_product=198:213382, answer=203:192477)
- Layer 25: `յ`, `家`, `ек`, `longleftrightarrow`, `cket` (target ranks: base_value=43:170903, first_product=86:175323, bound_value=99:166480, second_product=198:195785, answer=203:176375)
- Layer 26: `յ`, `uks`, `ек`, `scht`, `ာ` (target ranks: base_value=43:139173, first_product=86:166882, bound_value=99:153128, second_product=198:215637, answer=203:174743)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` ..` (target ranks: base_value=43:126057, first_product=86:207346, bound_value=99:199852, second_product=198:202939, answer=203:186891)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:61609, first_product=86:112449, bound_value=99:165771, second_product=198:142150, answer=203:101330)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:4319, first_product=86:25803, bound_value=99:51271, second_product=198:15057, answer=203:8528)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=43:150, first_product=86:1529, bound_value=99:3151, second_product=198:1432, answer=203:248)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:47, first_product=86:250, bound_value=99:365, second_product=198:183, answer=203:121)

### Filler position 18 (absolute token 894, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:114, first_product=86:166, bound_value=99:131, second_product=198:19, answer=203:36)
- Layer 8: `s`, `o`, `u`, `r`, `�` (target ranks: base_value=43:6511, first_product=86:12021, bound_value=99:13132, second_product=198:2157, answer=203:1985)
- Layer 16: `提`, `ods`, `ံ`, `地`, `壁` (target ranks: base_value=43:92477, first_product=86:28874, bound_value=99:103681, second_product=198:18902, answer=203:16663)
- Layer 24: `յ`, `longleftrightarrow`, `家`, `ек`, `íguez` (target ranks: base_value=43:208504, first_product=86:206964, bound_value=99:204575, second_product=198:221089, answer=203:209997)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `ек`, `之` (target ranks: base_value=43:199393, first_product=86:189469, bound_value=99:179359, second_product=198:206638, answer=203:199393)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ာ`, `家` (target ranks: base_value=43:160926, first_product=86:172929, bound_value=99:156384, second_product=198:219672, answer=203:188649)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=43:134828, first_product=86:212742, bound_value=99:200708, second_product=198:208031, answer=203:194113)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:71650, first_product=86:129457, bound_value=99:165997, second_product=198:144812, answer=203:103326)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=43:5075, first_product=86:27819, bound_value=99:45379, second_product=198:14330, answer=203:7883)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .$` (target ranks: base_value=43:202, first_product=86:1769, bound_value=99:3531, second_product=198:1588, answer=203:350)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:47, first_product=86:241, bound_value=99:332, second_product=198:163, answer=203:125)

### Filler position 19 (absolute token 895, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:111, first_product=86:163, bound_value=99:131, second_product=198:19, answer=203:35)
- Layer 8: `s`, `o`, `u`, `r`, `�` (target ranks: base_value=43:8235, first_product=86:14093, bound_value=99:14732, second_product=198:2860, answer=203:2688)
- Layer 16: `提`, `ods`, `ံ`, `蓬`, `地` (target ranks: base_value=43:90191, first_product=86:28289, bound_value=99:85974, second_product=198:16390, answer=203:13799)
- Layer 24: `յ`, `longleftrightarrow`, `家`, `之`, `ек` (target ranks: base_value=43:187311, first_product=86:204959, bound_value=99:189672, second_product=198:208933, answer=203:183843)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `之`, `�` (target ranks: base_value=43:171176, first_product=86:181927, bound_value=99:159413, second_product=198:192428, answer=203:170033)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `scht`, `amped` (target ranks: base_value=43:122679, first_product=86:166919, bound_value=99:140158, second_product=198:206786, answer=203:157272)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:115176, first_product=86:211009, bound_value=99:195992, second_product=198:203217, answer=203:181445)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `/.` (target ranks: base_value=43:55213, first_product=86:124784, bound_value=99:156866, second_product=198:135408, answer=203:86726)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=43:3719, first_product=86:31939, bound_value=99:45152, second_product=198:13283, answer=203:6180)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=43:176, first_product=86:1802, bound_value=99:3626, second_product=198:1453, answer=203:316)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:42, first_product=86:258, bound_value=99:381, second_product=198:181, answer=203:127)

### Filler position 20 (absolute token 896, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:111, first_product=86:159, bound_value=99:130, second_product=198:19, answer=203:35)
- Layer 8: `s`, `u`, `o`, `r`, `ared` (target ranks: base_value=43:7747, first_product=86:13398, bound_value=99:13596, second_product=198:2848, answer=203:2668)
- Layer 16: `提`, `壁`, `ods`, `口`, `地` (target ranks: base_value=43:71402, first_product=86:21681, bound_value=99:72360, second_product=198:12303, answer=203:12061)
- Layer 24: `յ`, `家`, `longleftrightarrow`, `ек`, `之` (target ranks: base_value=43:182386, first_product=86:201022, bound_value=99:190795, second_product=198:205109, answer=203:176553)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `cket`, `ек` (target ranks: base_value=43:168126, first_product=86:179172, bound_value=99:161125, second_product=198:190675, answer=203:166395)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `amped` (target ranks: base_value=43:127213, first_product=86:171738, bound_value=99:145365, second_product=198:209588, answer=203:157539)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:111971, first_product=86:210479, bound_value=99:196393, second_product=198:201189, answer=203:177854)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:52068, first_product=86:120289, bound_value=99:157613, second_product=198:130318, answer=203:82027)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:3664, first_product=86:29233, bound_value=99:45999, second_product=198:12908, answer=203:6236)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=43:174, first_product=86:1692, bound_value=99:3227, second_product=198:1379, answer=203:298)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:44, first_product=86:248, bound_value=99:359, second_product=198:171, answer=203:121)

### Filler position 21 (absolute token 897, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:109, first_product=86:159, bound_value=99:129, second_product=198:19, answer=203:35)
- Layer 8: `s`, `u`, `o`, `t`, `ared` (target ranks: base_value=43:7916, first_product=86:13671, bound_value=99:13294, second_product=198:3692, answer=203:2876)
- Layer 16: `提`, `壁`, `地`, `ods`, `口` (target ranks: base_value=43:72283, first_product=86:20647, bound_value=99:73308, second_product=198:11953, answer=203:12703)
- Layer 24: `յ`, `家`, `ек`, `longleftrightarrow`, `之` (target ranks: base_value=43:173715, first_product=86:195795, bound_value=99:182154, second_product=198:202027, answer=203:181658)
- Layer 25: `յ`, `家`, `ек`, `之`, `longleftrightarrow` (target ranks: base_value=43:158568, first_product=86:170597, bound_value=99:148843, second_product=198:184414, answer=203:169515)
- Layer 26: `յ`, `uks`, `年一季度`, `longleftrightarrow`, `ာ` (target ranks: base_value=43:124042, first_product=86:167244, bound_value=99:136308, second_product=198:210819, answer=203:169397)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:104421, first_product=86:204877, bound_value=99:187586, second_product=198:196348, answer=203:178911)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:47399, first_product=86:113536, bound_value=99:145833, second_product=198:123515, answer=203:84023)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2976, first_product=86:24978, bound_value=99:38879, second_product=198:10747, answer=203:5942)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=43:148, first_product=86:1480, bound_value=99:2775, second_product=198:1217, answer=203:272)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:38, first_product=86:241, bound_value=99:344, second_product=198:166, answer=203:116)

### Filler position 22 (absolute token 898, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:107, first_product=86:159, bound_value=99:128, second_product=198:19, answer=203:35)
- Layer 8: `s`, `u`, `o`, `t`, `r` (target ranks: base_value=43:9366, first_product=86:14656, bound_value=99:13402, second_product=198:3894, answer=203:3247)
- Layer 16: `提`, `壁`, `内`, `ods`, `地` (target ranks: base_value=43:72312, first_product=86:17412, bound_value=99:68908, second_product=198:9943, answer=203:9943)
- Layer 24: `յ`, `家`, `longleftrightarrow`, `ек`, `之` (target ranks: base_value=43:167849, first_product=86:187042, bound_value=99:171758, second_product=198:195525, answer=203:182018)
- Layer 25: `յ`, `家`, `之`, `ек`, `longleftrightarrow` (target ranks: base_value=43:154219, first_product=86:162496, bound_value=99:138170, second_product=198:177608, answer=203:169452)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ာ` (target ranks: base_value=43:118484, first_product=86:158704, bound_value=99:126409, second_product=198:203391, answer=203:166929)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:96539, first_product=86:198978, bound_value=99:179225, second_product=198:187728, answer=203:175327)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:45278, first_product=86:109930, bound_value=99:139385, second_product=198:113460, answer=203:80779)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2724, first_product=86:23512, bound_value=99:35413, second_product=198:8924, answer=203:5439)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:144, first_product=86:1342, bound_value=99:2525, second_product=198:1030, answer=203:265)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:40, first_product=86:235, bound_value=99:331, second_product=198:160, answer=203:118)

### Filler position 23 (absolute token 899, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:103, first_product=86:157, bound_value=99:128, second_product=198:19, answer=203:35)
- Layer 8: `s`, `o`, `u`, `�`, `r` (target ranks: base_value=43:10191, first_product=86:15874, bound_value=99:14751, second_product=198:3440, answer=203:3381)
- Layer 16: `提`, `壁`, `ods`, `内`, `蓬` (target ranks: base_value=43:81627, first_product=86:20207, bound_value=99:75069, second_product=198:11634, answer=203:10931)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `家` (target ranks: base_value=43:165581, first_product=86:184606, bound_value=99:168401, second_product=198:194254, answer=203:184082)
- Layer 25: `յ`, `家`, `之`, `ек`, `longleftrightarrow` (target ranks: base_value=43:154196, first_product=86:161443, bound_value=99:136727, second_product=198:179796, answer=203:174444)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ာ` (target ranks: base_value=43:114663, first_product=86:157006, bound_value=99:124218, second_product=198:201838, answer=203:167482)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:94934, first_product=86:196337, bound_value=99:178040, second_product=198:187418, answer=203:177011)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:42345, first_product=86:105103, bound_value=99:135593, second_product=198:109151, answer=203:78166)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2640, first_product=86:23488, bound_value=99:34193, second_product=198:8412, answer=203:5164)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:138, first_product=86:1288, bound_value=99:2419, second_product=198:965, answer=203:267)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:39, first_product=86:233, bound_value=99:330, second_product=198:158, answer=203:122)

### Filler position 24 (absolute token 900, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:103, first_product=86:159, bound_value=99:124, second_product=198:19, answer=203:35)
- Layer 8: `s`, `o`, `�`, `u`, `�` (target ranks: base_value=43:11928, first_product=86:18249, bound_value=99:17909, second_product=198:4216, answer=203:3829)
- Layer 16: `提`, `壁`, `ods`, `内`, `蓬` (target ranks: base_value=43:91335, first_product=86:25294, bound_value=99:83203, second_product=198:13715, answer=203:13034)
- Layer 24: `յ`, `ек`, `longleftrightarrow`, `之`, `家` (target ranks: base_value=43:166295, first_product=86:189146, bound_value=99:174727, second_product=198:194393, answer=203:184229)
- Layer 25: `յ`, `家`, `之`, `ек`, `longleftrightarrow` (target ranks: base_value=43:150685, first_product=86:162168, bound_value=99:139402, second_product=198:175667, answer=203:170256)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ာ` (target ranks: base_value=43:116176, first_product=86:162048, bound_value=99:129787, second_product=198:201888, answer=203:167525)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:91486, first_product=86:195689, bound_value=99:178304, second_product=198:184851, answer=203:174322)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=43:42074, first_product=86:109419, bound_value=99:135764, second_product=198:105293, answer=203:74538)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2525, first_product=86:24373, bound_value=99:33357, second_product=198:7600, answer=203:4576)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:128, first_product=86:1217, bound_value=99:2255, second_product=198:848, answer=203:249)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:37, first_product=86:229, bound_value=99:307, second_product=198:149, answer=203:114)

### Filler position 25 (absolute token 901, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:101, first_product=86:156, bound_value=99:125, second_product=198:19, answer=203:33)
- Layer 8: `s`, `o`, `�`, `�`, `u` (target ranks: base_value=43:12117, first_product=86:18394, bound_value=99:18569, second_product=198:3841, answer=203:3624)
- Layer 16: `提`, `壁`, `ods`, `蓬`, `内` (target ranks: base_value=43:86419, first_product=86:25115, bound_value=99:79502, second_product=198:12470, answer=203:11567)
- Layer 24: `յ`, `ек`, `之`, `longleftrightarrow`, `家` (target ranks: base_value=43:158264, first_product=86:188342, bound_value=99:172642, second_product=198:187293, answer=203:177038)
- Layer 25: `յ`, `之`, `家`, `ек`, `longleftrightarrow` (target ranks: base_value=43:140646, first_product=86:159695, bound_value=99:135597, second_product=198:167234, answer=203:162061)
- Layer 26: `յ`, `uks`, `年一季度`, `longleftrightarrow`, `ာ` (target ranks: base_value=43:105744, first_product=86:160514, bound_value=99:126776, second_product=198:196354, answer=203:161073)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:82256, first_product=86:191034, bound_value=99:172411, second_product=198:177133, answer=203:165004)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=43:37534, first_product=86:105833, bound_value=99:130420, second_product=198:97801, answer=203:68470)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2298, first_product=86:24117, bound_value=99:32098, second_product=198:6716, answer=203:4201)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:115, first_product=86:1136, bound_value=99:2013, second_product=198:737, answer=203:225)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:36, first_product=86:224, bound_value=99:305, second_product=198:142, answer=203:110)

### Filler position 26 (absolute token 902, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=43:102, first_product=86:159, bound_value=99:125, second_product=198:19, answer=203:33)
- Layer 8: `s`, `o`, `u`, `�`, `r` (target ranks: base_value=43:12243, first_product=86:18257, bound_value=99:19116, second_product=198:3968, answer=203:4161)
- Layer 16: `提`, `壁`, `ods`, `地`, `蓬` (target ranks: base_value=43:79780, first_product=86:22237, bound_value=99:71334, second_product=198:10485, answer=203:9986)
- Layer 24: `յ`, `ек`, `之`, `longleftrightarrow`, `家` (target ranks: base_value=43:154606, first_product=86:184912, bound_value=99:170474, second_product=198:182861, answer=203:173275)
- Layer 25: `յ`, `家`, `之`, `ек`, `longleftrightarrow` (target ranks: base_value=43:135539, first_product=86:154310, bound_value=99:131144, second_product=198:162058, answer=203:157317)
- Layer 26: `յ`, `uks`, `年一季度`, `ек`, `longleftrightarrow` (target ranks: base_value=43:101095, first_product=86:157574, bound_value=99:122537, second_product=198:193736, answer=203:157574)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:78395, first_product=86:188568, bound_value=99:168916, second_product=198:175320, answer=203:162361)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:35162, first_product=86:103108, bound_value=99:125185, second_product=198:95148, answer=203:66617)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:2050, first_product=86:22405, bound_value=99:29774, second_product=198:6269, answer=203:3939)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:106, first_product=86:1075, bound_value=99:1887, second_product=198:706, answer=203:211)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:32, first_product=86:222, bound_value=99:293, second_product=198:136, answer=203:107)

### Filler position 27 (absolute token 903, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:102, first_product=86:158, bound_value=99:125, second_product=198:19, answer=203:34)
- Layer 8: `s`, `�`, `o`, `�`, `u` (target ranks: base_value=43:15798, first_product=86:22351, bound_value=99:22851, second_product=198:7038, answer=203:5720)
- Layer 16: `提`, `内`, `壁`, `ods`, `地` (target ranks: base_value=43:72864, first_product=86:18942, bound_value=99:64031, second_product=198:9359, answer=203:9463)
- Layer 24: `յ`, `ек`, `之`, `longleftrightarrow`, `家` (target ranks: base_value=43:147820, first_product=86:182261, bound_value=99:168161, second_product=198:179687, answer=203:173215)
- Layer 25: `յ`, `ек`, `之`, `家`, `longleftrightarrow` (target ranks: base_value=43:131110, first_product=86:152966, bound_value=99:129884, second_product=198:160181, answer=203:159579)
- Layer 26: `յ`, `uks`, `ек`, `年一季度`, `scht` (target ranks: base_value=43:98473, first_product=86:157603, bound_value=99:122183, second_product=198:194390, answer=203:160902)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:71706, first_product=86:183740, bound_value=99:163408, second_product=198:168267, answer=203:159082)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:32484, first_product=86:100143, bound_value=99:119814, second_product=198:88779, answer=203:64708)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=43:1864, first_product=86:21175, bound_value=99:27344, second_product=198:5441, answer=203:3663)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:101, first_product=86:966, bound_value=99:1706, second_product=198:643, answer=203:204)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:31, first_product=86:210, bound_value=99:285, second_product=198:133, answer=203:106)

### Filler position 28 (absolute token 904, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:98, first_product=86:155, bound_value=99:122, second_product=198:19, answer=203:34)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=43:17223, first_product=86:21948, bound_value=99:20553, second_product=198:7210, answer=203:5883)
- Layer 16: `提`, `内`, `壁`, `ods`, `地` (target ranks: base_value=43:66468, first_product=86:16090, bound_value=99:60384, second_product=198:8474, answer=203:7748)
- Layer 24: `յ`, `ек`, `之`, `longleftrightarrow`, `家` (target ranks: base_value=43:142313, first_product=86:178144, bound_value=99:164932, second_product=198:179775, answer=203:175967)
- Layer 25: `յ`, `ек`, `之`, `家`, `longleftrightarrow` (target ranks: base_value=43:127875, first_product=86:151051, bound_value=99:129119, second_product=198:161205, answer=203:163028)
- Layer 26: `յ`, `uks`, `年一季度`, `ек`, `ာ` (target ranks: base_value=43:94904, first_product=86:154582, bound_value=99:119866, second_product=198:194601, answer=203:164023)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:66601, first_product=86:177809, bound_value=99:157236, second_product=198:163212, answer=203:156093)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:30323, first_product=86:97451, bound_value=99:116998, second_product=198:85815, answer=203:63849)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `().` (target ranks: base_value=43:1665, first_product=86:19631, bound_value=99:25811, second_product=198:4767, answer=203:3410)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:97, first_product=86:943, bound_value=99:1697, second_product=198:612, answer=203:209)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:31, first_product=86:203, bound_value=99:283, second_product=198:129, answer=203:104)

### Filler position 29 (absolute token 905, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:97, first_product=86:156, bound_value=99:122, second_product=198:19, answer=203:32)
- Layer 8: `s`, `�`, `o`, `�`, `u` (target ranks: base_value=43:18531, first_product=86:22833, bound_value=99:21871, second_product=198:7747, answer=203:6370)
- Layer 16: `提`, `内`, `ods`, `壁`, `地` (target ranks: base_value=43:68750, first_product=86:16297, bound_value=99:61641, second_product=198:8916, answer=203:7618)
- Layer 24: `յ`, `ек`, `之`, `longleftrightarrow`, `家` (target ranks: base_value=43:144380, first_product=86:180429, bound_value=99:168574, second_product=198:182049, answer=203:180429)
- Layer 25: `յ`, `ек`, `之`, `家`, `longleftrightarrow` (target ranks: base_value=43:128929, first_product=86:152136, bound_value=99:131474, second_product=198:165199, answer=203:168096)
- Layer 26: `յ`, `uks`, `年一季度`, `ек`, `ာ` (target ranks: base_value=43:94464, first_product=86:156122, bound_value=99:121914, second_product=198:195417, answer=203:166075)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:68407, first_product=86:179572, bound_value=99:159753, second_product=198:166681, answer=203:159197)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:31668, first_product=86:101712, bound_value=99:120130, second_product=198:88722, answer=203:65937)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `().` (target ranks: base_value=43:1686, first_product=86:20682, bound_value=99:26005, second_product=198:4804, answer=203:3319)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:84, first_product=86:875, bound_value=99:1515, second_product=198:541, answer=203:182)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=43:28, first_product=86:193, bound_value=99:262, second_product=198:112, answer=203:97)

### Filler position 30 (absolute token 906, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:98, first_product=86:154, bound_value=99:120, second_product=198:19, answer=203:33)
- Layer 8: `s`, `�`, `o`, `�`, `�` (target ranks: base_value=43:21179, first_product=86:25432, bound_value=99:23976, second_product=198:9190, answer=203:7507)
- Layer 16: `提`, `内`, `ods`, `壁`, `佩` (target ranks: base_value=43:68045, first_product=86:16051, bound_value=99:60178, second_product=198:8470, answer=203:7448)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=43:144274, first_product=86:181450, bound_value=99:169011, second_product=198:183011, answer=203:181450)
- Layer 25: `յ`, `ек`, `之`, `家`, `longleftrightarrow` (target ranks: base_value=43:125032, first_product=86:149654, bound_value=99:130070, second_product=198:162191, answer=203:165692)
- Layer 26: `յ`, `uks`, `ာ`, `ек`, `itionally` (target ranks: base_value=43:93871, first_product=86:157578, bound_value=99:122220, second_product=198:196125, answer=203:168026)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:63469, first_product=86:174160, bound_value=99:154309, second_product=198:160947, answer=203:153200)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:30962, first_product=86:100477, bound_value=99:118294, second_product=198:86997, answer=203:64829)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=43:1677, first_product=86:20660, bound_value=99:25547, second_product=198:4595, answer=203:3339)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:82, first_product=86:871, bound_value=99:1491, second_product=198:521, answer=203:180)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:28, first_product=86:186, bound_value=99:257, second_product=198:109, answer=203:93)

### Filler position 31 (absolute token 907, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:97, first_product=86:156, bound_value=99:116, second_product=198:19, answer=203:33)
- Layer 8: `s`, `�`, `�`, `o`, `�` (target ranks: base_value=43:20821, first_product=86:25359, bound_value=99:23734, second_product=198:8005, answer=203:6678)
- Layer 16: `提`, `ods`, `内`, `壁`, `佩` (target ranks: base_value=43:69118, first_product=86:17110, bound_value=99:60148, second_product=198:8793, answer=203:7238)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=43:137981, first_product=86:177200, bound_value=99:163876, second_product=198:177739, answer=203:176657)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=43:115181, first_product=86:141861, bound_value=99:122255, second_product=198:153578, answer=203:157084)
- Layer 26: `յ`, `uks`, `ာ`, `年一季度`, `itionally` (target ranks: base_value=43:90923, first_product=86:155049, bound_value=99:118711, second_product=198:194528, answer=203:167204)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:60488, first_product=86:171444, bound_value=99:150644, second_product=198:157963, answer=203:150062)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:27488, first_product=86:95174, bound_value=99:111727, second_product=198:81032, answer=203:60694)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=43:1476, first_product=86:18691, bound_value=99:23244, second_product=198:3883, answer=203:2962)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:75, first_product=86:810, bound_value=99:1374, second_product=198:472, answer=203:165)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:28, first_product=86:189, bound_value=99:249, second_product=198:103, answer=203:84)

### Filler position 32 (absolute token 908, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:95, first_product=86:156, bound_value=99:122, second_product=198:19, answer=203:33)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:23370, first_product=86:27956, bound_value=99:27333, second_product=198:10067, answer=203:8150)
- Layer 16: `提`, `ods`, `内`, `佩`, `壁` (target ranks: base_value=43:69226, first_product=86:18018, bound_value=99:59368, second_product=198:9474, answer=203:7242)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=43:132359, first_product=86:176206, bound_value=99:163304, second_product=198:176206, answer=203:173504)
- Layer 25: `յ`, `之`, `ек`, `家`, `般` (target ranks: base_value=43:108809, first_product=86:139409, bound_value=99:120431, second_product=198:150634, answer=203:153663)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `年一季度` (target ranks: base_value=43:84845, first_product=86:152076, bound_value=99:116113, second_product=198:193094, answer=203:163808)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=43:55572, first_product=86:166097, bound_value=99:144778, second_product=198:153143, answer=203:144228)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:24760, first_product=86:90667, bound_value=99:105690, second_product=198:74484, answer=203:54791)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=43:1369, first_product=86:18291, bound_value=99:22071, second_product=198:3548, answer=203:2686)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=43:72, first_product=86:779, bound_value=99:1260, second_product=198:421, answer=203:158)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:26, first_product=86:185, bound_value=99:241, second_product=198:98, answer=203:80)

### Filler position 33 (absolute token 909, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:96, first_product=86:156, bound_value=99:121, second_product=198:19, answer=203:32)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=43:19504, first_product=86:23075, bound_value=99:23845, second_product=198:9126, answer=203:6788)
- Layer 16: `提`, `ods`, `内`, `佩`, `壁` (target ranks: base_value=43:58681, first_product=86:16238, bound_value=99:54380, second_product=198:8213, answer=203:6413)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=43:123201, first_product=86:169359, bound_value=99:157195, second_product=198:168253, answer=203:166593)
- Layer 25: `յ`, `之`, `ек`, `家`, `般` (target ranks: base_value=43:99196, first_product=86:130142, bound_value=99:113202, second_product=198:140365, answer=203:145268)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `年一季度` (target ranks: base_value=43:77899, first_product=86:145830, bound_value=99:110742, second_product=198:186826, answer=203:158800)
- Layer 27: ` .`, `．`, ` `.`, ` ..`, `-.` (target ranks: base_value=43:50157, first_product=86:159119, bound_value=99:138370, second_product=198:144075, answer=203:136656)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=43:23218, first_product=86:86498, bound_value=99:100459, second_product=198:69412, answer=203:52773)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=43:1287, first_product=86:16778, bound_value=99:20304, second_product=198:3128, answer=203:2550)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=43:73, first_product=86:703, bound_value=99:1146, second_product=198:389, answer=203:162)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:25, first_product=86:184, bound_value=99:232, second_product=198:90, answer=203:75)

### Filler position 34 (absolute token 910, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:96, first_product=86:152, bound_value=99:122, second_product=198:19, answer=203:32)
- Layer 8: `s`, `�`, `u`, `�`, `�` (target ranks: base_value=43:24628, first_product=86:24397, bound_value=99:24906, second_product=198:13254, answer=203:8631)
- Layer 16: `提`, `内`, `佩`, `ods`, ` $` (target ranks: base_value=43:56903, first_product=86:14852, bound_value=99:50360, second_product=198:7945, answer=203:6534)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `ာ` (target ranks: base_value=43:120157, first_product=86:168213, bound_value=99:160050, second_product=198:174318, answer=203:173737)
- Layer 25: `յ`, `之`, `ек`, `般`, `家` (target ranks: base_value=43:95105, first_product=86:127347, bound_value=99:113628, second_product=198:144207, answer=203:150966)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `scht` (target ranks: base_value=43:78552, first_product=86:147481, bound_value=99:114404, second_product=198:194942, answer=203:169841)
- Layer 27: ` .`, `．`, ` `.`, ` ..`, `().` (target ranks: base_value=43:49401, first_product=86:155878, bound_value=99:137503, second_product=198:146557, answer=203:140920)
- Layer 28: ` .`, `．`, `而又`, ` `.`, `-.` (target ranks: base_value=43:22115, first_product=86:85619, bound_value=99:100304, second_product=198:71499, answer=203:55713)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=43:1176, first_product=86:16487, bound_value=99:20098, second_product=198:3105, answer=203:2623)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=43:62, first_product=86:639, bound_value=99:1047, second_product=198:361, answer=203:147)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:20, first_product=86:174, bound_value=99:221, second_product=198:85, answer=203:72)

### Filler position 35 (absolute token 911, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:96, first_product=86:153, bound_value=99:117, second_product=198:17, answer=203:32)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:26794, first_product=86:26938, bound_value=99:26078, second_product=198:12768, answer=203:9473)
- Layer 16: `提`, `内`, `佩`, `ods`, ` $` (target ranks: base_value=43:56170, first_product=86:13982, bound_value=99:48396, second_product=198:7660, answer=203:5967)
- Layer 24: `յ`, `之`, `ек`, `ာ`, `longleftrightarrow` (target ranks: base_value=43:121761, first_product=86:165553, bound_value=99:159167, second_product=198:176235, answer=203:176777)
- Layer 25: `յ`, `之`, `ек`, `般`, `家` (target ranks: base_value=43:97242, first_product=86:125930, bound_value=99:114632, second_product=198:146644, answer=203:153928)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `scht` (target ranks: base_value=43:76221, first_product=86:143059, bound_value=99:111390, second_product=198:192222, answer=203:167526)
- Layer 27: ` .`, `．`, ` ..`, ` `.`, `().` (target ranks: base_value=43:49891, first_product=86:154721, bound_value=99:136328, second_product=198:147074, answer=203:141443)
- Layer 28: ` .`, `．`, `而又`, ` `.`, ` ..` (target ranks: base_value=43:23957, first_product=86:87388, bound_value=99:101390, second_product=198:72953, answer=203:56153)
- Layer 29: ` .`, `．`, `-.`, `().`, `.` (target ranks: base_value=43:1226, first_product=86:16092, bound_value=99:19654, second_product=198:2917, answer=203:2483)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=43:61, first_product=86:621, bound_value=99:1027, second_product=198:346, answer=203:141)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:17, first_product=86:169, bound_value=99:201, second_product=198:73, answer=203:64)

### Filler position 36 (absolute token 912, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:154, bound_value=99:118, second_product=198:17, answer=203:31)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:22873, first_product=86:26359, bound_value=99:24308, second_product=198:9238, answer=203:7590)
- Layer 16: `提`, `内`, `ods`, ` $`, `佩` (target ranks: base_value=43:64163, first_product=86:17628, bound_value=99:57797, second_product=198:9325, answer=203:6832)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `ာ` (target ranks: base_value=43:116826, first_product=86:164019, bound_value=99:154654, second_product=198:168123, answer=203:168123)
- Layer 25: `յ`, `之`, `ек`, `般`, `家` (target ranks: base_value=43:89418, first_product=86:121527, bound_value=99:109627, second_product=198:136742, answer=203:142895)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `scht` (target ranks: base_value=43:67709, first_product=86:133326, bound_value=99:101401, second_product=198:179948, answer=203:153477)
- Layer 27: ` .`, `．`, ` ..`, `().`, `__.` (target ranks: base_value=43:45919, first_product=86:148438, bound_value=99:130275, second_product=198:138337, answer=203:129057)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `__.` (target ranks: base_value=43:21471, first_product=86:81946, bound_value=99:96325, second_product=198:67417, answer=203:50160)
- Layer 29: ` .`, `．`, `-.`, `.`, `().` (target ranks: base_value=43:1135, first_product=86:15277, bound_value=99:19115, second_product=198:2723, answer=203:2230)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=43:53, first_product=86:524, bound_value=99:867, second_product=198:285, answer=203:119)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:17, first_product=86:167, bound_value=99:197, second_product=198:70, answer=203:62)

### Filler position 37 (absolute token 913, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:153, bound_value=99:118, second_product=198:17, answer=203:33)
- Layer 8: `s`, `�`, `�`, `�`, `�` (target ranks: base_value=43:22517, first_product=86:26649, bound_value=99:25099, second_product=198:10836, answer=203:7339)
- Layer 16: `提`, `ods`, `内`, `佩`, ` $` (target ranks: base_value=43:65462, first_product=86:19281, bound_value=99:57114, second_product=198:9994, answer=203:6600)
- Layer 24: `յ`, `之`, `ек`, `ာ`, `scht` (target ranks: base_value=43:119793, first_product=86:164742, bound_value=99:158866, second_product=198:171110, answer=203:168840)
- Layer 25: `յ`, `之`, `ек`, `般`, `家` (target ranks: base_value=43:90443, first_product=86:119881, bound_value=99:111636, second_product=198:139420, answer=203:142567)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `scht` (target ranks: base_value=43:72477, first_product=86:136798, bound_value=99:106580, second_product=198:187622, answer=203:159155)
- Layer 27: ` .`, `．`, ` ..`, `__.`, `().` (target ranks: base_value=43:47421, first_product=86:147838, bound_value=99:129537, second_product=198:140505, answer=203:129537)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `__.` (target ranks: base_value=43:23344, first_product=86:82189, bound_value=99:93585, second_product=198:64159, answer=203:47167)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=43:1293, first_product=86:15764, bound_value=99:18251, second_product=198:2428, answer=203:2034)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=43:57, first_product=86:516, bound_value=99:794, second_product=198:250, answer=203:113)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=43:17, first_product=86:162, bound_value=99:192, second_product=198:62, answer=203:57)

### Filler position 38 (absolute token 914, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:95, first_product=86:151, bound_value=99:114, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:22532, first_product=86:25948, bound_value=99:24185, second_product=198:9909, answer=203:7609)
- Layer 16: `提`, `佩`, `内`, ` $`, `ods` (target ranks: base_value=43:57251, first_product=86:15683, bound_value=99:47498, second_product=198:7396, answer=203:5177)
- Layer 24: `յ`, `之`, `ек`, `scht`, `ာ` (target ranks: base_value=43:112951, first_product=86:160794, bound_value=99:153667, second_product=198:165409, answer=203:164271)
- Layer 25: `յ`, `之`, `ек`, `般`, `scht` (target ranks: base_value=43:78273, first_product=86:109941, bound_value=99:101030, second_product=198:126361, answer=203:131386)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `scht` (target ranks: base_value=43:62626, first_product=86:127180, bound_value=99:96956, second_product=198:177875, answer=203:149639)
- Layer 27: ` .`, `．`, ` ..`, `__.`, `().` (target ranks: base_value=43:43105, first_product=86:139673, bound_value=99:122865, second_product=198:131040, answer=203:121718)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `__.` (target ranks: base_value=43:19918, first_product=86:73634, bound_value=99:85922, second_product=198:57533, answer=203:42931)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=43:1109, first_product=86:14101, bound_value=99:16406, second_product=198:2096, answer=203:1872)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=43:50, first_product=86:473, bound_value=99:714, second_product=198:228, answer=203:99)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ↵↵` (target ranks: base_value=43:17, first_product=86:163, bound_value=99:185, second_product=198:61, answer=203:56)

### Filler position 39 (absolute token 915, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:151, bound_value=99:114, second_product=198:18, answer=203:33)
- Layer 8: `s`, `�`, `�`, `�`, `u` (target ranks: base_value=43:23697, first_product=86:26991, bound_value=99:24433, second_product=198:10440, answer=203:8606)
- Layer 16: `提`, `ods`, `佩`, ` $`, `内` (target ranks: base_value=43:57911, first_product=86:15936, bound_value=99:49414, second_product=198:8275, answer=203:5487)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `ек` (target ranks: base_value=43:109328, first_product=86:155056, bound_value=99:148280, second_product=198:162182, answer=203:164521)
- Layer 25: `յ`, `之`, `般`, `ек`, `ား` (target ranks: base_value=43:80533, first_product=86:110413, bound_value=99:102334, second_product=198:128661, answer=203:138697)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `年一季度` (target ranks: base_value=43:67890, first_product=86:131926, bound_value=99:99018, second_product=198:183933, answer=203:160918)
- Layer 27: ` .`, `．`, ` ..`, `__.`, `().` (target ranks: base_value=43:42037, first_product=86:137552, bound_value=99:116676, second_product=198:131191, answer=203:122498)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `__.` (target ranks: base_value=43:21482, first_product=86:74733, bound_value=99:83236, second_product=198:58557, answer=203:45111)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=43:1178, first_product=86:12972, bound_value=99:14745, second_product=198:2031, answer=203:1887)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=43:56, first_product=86:476, bound_value=99:696, second_product=198:226, answer=203:113)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ↵↵` (target ranks: base_value=43:17, first_product=86:156, bound_value=99:181, second_product=198:56, answer=203:56)

### Filler position 40 (absolute token 916, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:95, first_product=86:151, bound_value=99:114, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `�`, `u` (target ranks: base_value=43:26189, first_product=86:26421, bound_value=99:23434, second_product=198:13755, answer=203:9351)
- Layer 16: `提`, `佩`, `内`, `ods`, ` $` (target ranks: base_value=43:53151, first_product=86:14485, bound_value=99:43241, second_product=198:7546, answer=203:4884)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `ек` (target ranks: base_value=43:92921, first_product=86:147549, bound_value=99:137598, second_product=198:152401, answer=203:151771)
- Layer 25: `յ`, `之`, `般`, ` .`, `itionally` (target ranks: base_value=43:61103, first_product=86:96086, bound_value=99:85721, second_product=198:112678, answer=203:119007)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `scht` (target ranks: base_value=43:49133, first_product=86:113285, bound_value=99:81834, second_product=198:167723, answer=203:141073)
- Layer 27: ` .`, `．`, ` ..`, `.`, `__.` (target ranks: base_value=43:35951, first_product=86:128237, bound_value=99:107812, second_product=198:122493, answer=203:112447)
- Layer 28: ` .`, `．`, ` ..`, `而又`, `__.` (target ranks: base_value=43:16207, first_product=86:65140, bound_value=99:73197, second_product=198:51187, answer=203:38539)
- Layer 29: ` .`, `．`, `.`, `↵↵`, `().` (target ranks: base_value=43:902, first_product=86:11820, bound_value=99:12943, second_product=198:1698, answer=203:1564)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=43:46, first_product=86:385, bound_value=99:542, second_product=198:186, answer=203:92)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ↵↵` (target ranks: base_value=43:17, first_product=86:144, bound_value=99:167, second_product=198:57, answer=203:52)

### Filler position 41 (absolute token 917, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:91, first_product=86:151, bound_value=99:114, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `u`, `�` (target ranks: base_value=43:23907, first_product=86:24029, bound_value=99:21195, second_product=198:10857, answer=203:8569)
- Layer 16: `提`, `内`, `ods`, ` $`, `佩` (target ranks: base_value=43:45124, first_product=86:10617, bound_value=99:35126, second_product=198:5952, answer=203:4063)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `ား` (target ranks: base_value=43:98255, first_product=86:146043, bound_value=99:142977, second_product=198:160395, answer=203:160935)
- Layer 25: `յ`, `↵↵`, `之`, `般`, `itionally` (target ranks: base_value=43:64636, first_product=86:93656, bound_value=99:89392, second_product=198:119503, answer=203:128193)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:55003, first_product=86:115018, bound_value=99:86840, second_product=198:179252, answer=203:154297)
- Layer 27: ` .`, `．`, `.`, ` ..`, `յ` (target ranks: base_value=43:37775, first_product=86:125010, bound_value=99:105844, second_product=198:126147, answer=203:116303)
- Layer 28: ` .`, `．`, `↵↵`, `而又`, ` ..` (target ranks: base_value=43:18674, first_product=86:62384, bound_value=99:69743, second_product=198:48136, answer=203:37054)
- Layer 29: ` .`, `．`, `.`, `↵↵`, `().` (target ranks: base_value=43:1021, first_product=86:10602, bound_value=99:11753, second_product=198:1440, answer=203:1440)
- Layer 30: ` .`, ` ..`, `↵↵`, `．`, ` ↵↵` (target ranks: base_value=43:47, first_product=86:333, bound_value=99:460, second_product=198:152, answer=203:90)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ↵↵` (target ranks: base_value=43:19, first_product=86:145, bound_value=99:157, second_product=198:51, answer=203:48)

### Filler position 42 (absolute token 918, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:95, first_product=86:151, bound_value=99:116, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `o`, `�`, `�` (target ranks: base_value=43:24079, first_product=86:24923, bound_value=99:20666, second_product=198:10657, answer=203:7996)
- Layer 16: `提`, `内`, `佩`, ` $`, `ods` (target ranks: base_value=43:48584, first_product=86:10878, bound_value=99:34766, second_product=198:5155, answer=203:3835)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `ား` (target ranks: base_value=43:96601, first_product=86:141768, bound_value=99:135434, second_product=198:155127, answer=203:160482)
- Layer 25: `յ`, `↵↵`, `之`, `般`, `itionally` (target ranks: base_value=43:58199, first_product=86:84544, bound_value=99:79025, second_product=198:109225, answer=203:121615)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:49030, first_product=86:102895, bound_value=99:74585, second_product=198:169214, answer=203:148162)
- Layer 27: ` .`, `．`, ` ..`, `յ`, `.` (target ranks: base_value=43:34252, first_product=86:115320, bound_value=99:95928, second_product=198:116434, answer=203:110564)
- Layer 28: ` .`, `．`, `↵↵`, ` ..`, `.` (target ranks: base_value=43:16838, first_product=86:56162, bound_value=99:64033, second_product=198:44770, answer=203:35856)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=43:856, first_product=86:9312, bound_value=99:10012, second_product=198:1268, answer=203:1290)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:43, first_product=86:285, bound_value=99:358, second_product=198:113, answer=203:68)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:19, first_product=86:156, bound_value=99:156, second_product=198:47, answer=203:51)

### Filler position 43 (absolute token 919, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:92, first_product=86:151, bound_value=99:116, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `�`, `�` (target ranks: base_value=43:24347, first_product=86:25756, bound_value=99:20966, second_product=198:10184, answer=203:7122)
- Layer 16: `提`, `ods`, `内`, ` $`, `佩` (target ranks: base_value=43:57613, first_product=86:12691, bound_value=99:39783, second_product=198:7012, answer=203:4565)
- Layer 24: `յ`, `ာ`, `之`, `scht`, `ား` (target ranks: base_value=43:102831, first_product=86:145494, bound_value=99:141784, second_product=198:158217, answer=203:167037)
- Layer 25: `յ`, `↵↵`, `之`, `般`, `ား` (target ranks: base_value=43:61875, first_product=86:86756, bound_value=99:83509, second_product=198:108333, answer=203:125198)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:54286, first_product=86:109185, bound_value=99:80722, second_product=198:170266, answer=203:154084)
- Layer 27: ` .`, `．`, `.`, ` ..`, `յ` (target ranks: base_value=43:34194, first_product=86:114823, bound_value=99:93496, second_product=198:110691, answer=203:106021)
- Layer 28: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=43:18461, first_product=86:57768, bound_value=99:61204, second_product=198:38127, answer=203:31855)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=43:1020, first_product=86:10090, bound_value=99:9705, second_product=198:1020, answer=203:1186)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:43, first_product=86:260, bound_value=99:319, second_product=198:97, answer=203:70)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:26, first_product=86:145, bound_value=99:145, second_product=198:45, answer=203:49)

### Filler position 44 (absolute token 920, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:92, first_product=86:151, bound_value=99:116, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `o`, `�` (target ranks: base_value=43:22585, first_product=86:25956, bound_value=99:23292, second_product=198:8836, answer=203:6632)
- Layer 16: `提`, `ods`, ` $`, `内`, `佩` (target ranks: base_value=43:55485, first_product=86:12255, bound_value=99:36397, second_product=198:5988, answer=203:3839)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `=""` (target ranks: base_value=43:94989, first_product=86:143084, bound_value=99:136174, second_product=198:149756, answer=203:157542)
- Layer 25: `յ`, `↵↵`, `之`, `般`, `itionally` (target ranks: base_value=43:53159, first_product=86:80855, bound_value=99:76310, second_product=198:97425, answer=203:112767)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:43111, first_product=86:96836, bound_value=99:69390, second_product=198:152283, answer=203:135816)
- Layer 27: ` .`, `．`, `.`, ` ..`, `յ` (target ranks: base_value=43:30493, first_product=86:107423, bound_value=99:88401, second_product=198:101248, answer=203:95665)
- Layer 28: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=43:15364, first_product=86:51744, bound_value=99:54577, second_product=198:32314, answer=203:26823)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=43:877, first_product=86:9371, bound_value=99:8629, second_product=198:877, answer=203:1011)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:44, first_product=86:262, bound_value=99:288, second_product=198:82, answer=203:66)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:24, first_product=86:151, bound_value=99:143, second_product=198:44, answer=203:48)

### Filler position 45 (absolute token 921, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:93, first_product=86:153, bound_value=99:123, second_product=198:18, answer=203:32)
- Layer 8: `s`, `�`, `�`, `o`, `�` (target ranks: base_value=43:21305, first_product=86:25246, bound_value=99:24687, second_product=198:9251, answer=203:7111)
- Layer 16: `提`, `ods`, `佩`, ` $`, `三` (target ranks: base_value=43:51056, first_product=86:11479, bound_value=99:33286, second_product=198:5047, answer=203:3374)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `=""` (target ranks: base_value=43:93870, first_product=86:140291, bound_value=99:135197, second_product=198:145884, answer=203:156772)
- Layer 25: `յ`, `↵↵`, `itionally`, ` .`, `般` (target ranks: base_value=43:51552, first_product=86:76891, bound_value=99:73924, second_product=198:92350, answer=203:113099)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:44437, first_product=86:96566, bound_value=99:69091, second_product=198:154595, answer=203:139813)
- Layer 27: ` .`, `．`, `↵↵`, `.`, `յ` (target ranks: base_value=43:30578, first_product=86:105065, bound_value=99:84275, second_product=198:100471, answer=203:96035)
- Layer 28: ` .`, `．`, `↵↵`, `.`, `=""` (target ranks: base_value=43:17545, first_product=86:51763, bound_value=99:51450, second_product=198:30641, answer=203:26446)
- Layer 29: ` .`, `↵↵`, `．`, `.`, `().` (target ranks: base_value=43:989, first_product=86:8923, bound_value=99:7846, second_product=198:807, answer=203:1004)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:42, first_product=86:244, bound_value=99:254, second_product=198:73, answer=203:64)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:28, first_product=86:154, bound_value=99:137, second_product=198:44, answer=203:47)

### Filler position 46 (absolute token 922, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:151, bound_value=99:119, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `o`, `�`, `u` (target ranks: base_value=43:22315, first_product=86:25560, bound_value=99:25688, second_product=198:10450, answer=203:7911)
- Layer 16: `提`, `佩`, `ods`, `内`, ` $` (target ranks: base_value=43:48997, first_product=86:10210, bound_value=99:30933, second_product=198:4607, answer=203:3341)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `cket` (target ranks: base_value=43:89463, first_product=86:136426, bound_value=99:130074, second_product=198:142095, answer=203:156713)
- Layer 25: `յ`, `↵↵`, ` .`, `itionally`, `之` (target ranks: base_value=43:45953, first_product=86:70584, bound_value=99:66918, second_product=198:84218, answer=203:108520)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:41885, first_product=86:92350, bound_value=99:65186, second_product=198:150498, answer=203:141911)
- Layer 27: ` .`, `．`, `.`, `↵↵`, `յ` (target ranks: base_value=43:27920, first_product=86:99143, bound_value=99:79712, second_product=198:94315, answer=203:93755)
- Layer 28: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=43:16091, first_product=86:48180, bound_value=99:47807, second_product=198:27583, answer=203:25685)
- Layer 29: ` .`, `↵↵`, `．`, `.`, `().` (target ranks: base_value=43:896, first_product=86:8030, bound_value=99:7064, second_product=198:642, answer=203:938)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:42, first_product=86:231, bound_value=99:243, second_product=198:69, answer=203:62)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:29, first_product=86:157, bound_value=99:139, second_product=198:43, answer=203:48)

### Filler position 47 (absolute token 923, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:153, bound_value=99:119, second_product=198:18, answer=203:32)
- Layer 8: `s`, `�`, `o`, `�`, `�` (target ranks: base_value=43:25670, first_product=86:26272, bound_value=99:23816, second_product=198:10890, answer=203:8132)
- Layer 16: `提`, `内`, `佩`, ` $`, `ods` (target ranks: base_value=43:47736, first_product=86:8620, bound_value=99:28769, second_product=198:4218, answer=203:3169)
- Layer 24: `յ`, `之`, `ာ`, `scht`, `=""` (target ranks: base_value=43:85520, first_product=86:131972, bound_value=99:125590, second_product=198:140780, answer=203:157693)
- Layer 25: `յ`, `↵↵`, ` .`, `般`, `之` (target ranks: base_value=43:42361, first_product=86:67124, bound_value=99:63530, second_product=198:81664, answer=203:107539)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=43:38251, first_product=86:85839, bound_value=99:59479, second_product=198:145944, answer=203:139198)
- Layer 27: ` .`, `．`, `.`, `↵↵`, `յ` (target ranks: base_value=43:27323, first_product=86:95097, bound_value=99:75445, second_product=198:92480, answer=203:93597)
- Layer 28: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=43:14293, first_product=86:43414, bound_value=99:42699, second_product=198:25154, answer=203:24546)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ..` (target ranks: base_value=43:743, first_product=86:7022, bound_value=99:5904, second_product=198:549, answer=203:830)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:42, first_product=86:217, bound_value=99:217, second_product=198:61, answer=203:58)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:32, first_product=86:152, bound_value=99:139, second_product=198:43, answer=203:51)

### Filler position 48 (absolute token 924, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:93, first_product=86:153, bound_value=99:119, second_product=198:18, answer=203:32)
- Layer 8: `s`, `�`, `o`, `�`, `�` (target ranks: base_value=43:26050, first_product=86:26893, bound_value=99:22454, second_product=198:10692, answer=203:8005)
- Layer 16: `提`, `内`, `ods`, ` $`, `三` (target ranks: base_value=43:48102, first_product=86:8149, bound_value=99:29035, second_product=198:4502, answer=203:3345)
- Layer 24: `յ`, `之`, `ာ`, `=""`, `↵↵` (target ranks: base_value=43:86833, first_product=86:130058, bound_value=99:125564, second_product=198:143740, answer=203:162968)
- Layer 25: `յ`, `↵↵`, ` .`, `般`, `itionally` (target ranks: base_value=43:43347, first_product=86:66089, bound_value=99:63330, second_product=198:84375, answer=203:114475)
- Layer 26: `յ`, `itionally`, `uks`, `ာ`, `=""` (target ranks: base_value=43:37663, first_product=86:82413, bound_value=99:57213, second_product=198:147577, answer=203:144242)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=43:26170, first_product=86:90674, bound_value=99:70346, second_product=198:90359, answer=203:92051)
- Layer 28: ` .`, `．`, `↵↵`, `=""`, `.` (target ranks: base_value=43:15006, first_product=86:42209, bound_value=99:39435, second_product=198:21654, answer=203:21970)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=43:773, first_product=86:6770, bound_value=99:5273, second_product=198:416, answer=203:707)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:41, first_product=86:217, bound_value=99:192, second_product=198:49, answer=203:56)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:39, first_product=86:163, bound_value=99:140, second_product=198:42, answer=203:53)

### Filler position 49 (absolute token 925, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:94, first_product=86:151, bound_value=99:119, second_product=198:18, answer=203:32)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:23656, first_product=86:28258, bound_value=99:23091, second_product=198:10560, answer=203:6819)
- Layer 16: `提`, `内`, `ods`, ` $`, `佩` (target ranks: base_value=43:40539, first_product=86:7654, bound_value=99:24834, second_product=198:3744, answer=203:2487)
- Layer 24: `յ`, `ာ`, `↵↵`, `之`, `=""` (target ranks: base_value=43:87316, first_product=86:132686, bound_value=99:122535, second_product=198:144610, answer=203:159144)
- Layer 25: `յ`, `↵↵`, ` .`, `般`, `itionally` (target ranks: base_value=43:38004, first_product=86:60358, bound_value=99:55239, second_product=198:78051, answer=203:100585)
- Layer 26: `յ`, `itionally`, `uks`, `ာ`, `=""` (target ranks: base_value=43:33806, first_product=86:75667, bound_value=99:50522, second_product=198:141091, answer=203:133307)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=43:24158, first_product=86:83028, bound_value=99:64616, second_product=198:84050, answer=203:83293)
- Layer 28: ` .`, `↵↵`, `．`, ` ↵↵`, `=""` (target ranks: base_value=43:13015, first_product=86:36370, bound_value=99:34376, second_product=198:17834, answer=203:17465)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=43:692, first_product=86:5906, bound_value=99:4430, second_product=198:350, answer=203:534)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=43:33, first_product=86:160, bound_value=99:139, second_product=198:39, answer=203:45)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:38, first_product=86:162, bound_value=99:132, second_product=198:40, answer=203:50)

### Filler position 50 (absolute token 926, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=43:93, first_product=86:153, bound_value=99:120, second_product=198:18, answer=203:31)
- Layer 8: `s`, `�`, `�`, `�`, `o` (target ranks: base_value=43:26184, first_product=86:30366, bound_value=99:26303, second_product=198:10890, answer=203:6863)
- Layer 16: `提`, `ods`, ` $`, `内`, `三` (target ranks: base_value=43:42903, first_product=86:6957, bound_value=99:23898, second_product=198:3595, answer=203:2489)
- Layer 24: `յ`, `↵↵`, `ာ`, `=""`, `之` (target ranks: base_value=43:93225, first_product=86:132999, bound_value=99:129789, second_product=198:143599, answer=203:166020)
- Layer 25: `↵↵`, `յ`, ` .`, `itionally`, ` ↵↵` (target ranks: base_value=43:42388, first_product=86:62882, bound_value=99:63117, second_product=198:80369, answer=203:110724)
- Layer 26: `յ`, `itionally`, `uks`, `ာ`, `=""` (target ranks: base_value=43:42880, first_product=86:84385, bound_value=99:61639, second_product=198:152004, answer=203:150881)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=43:24496, first_product=86:78662, bound_value=99:62526, second_product=198:75673, answer=203:78662)
- Layer 28: ` .`, `↵↵`, `．`, ` ↵↵`, `=""` (target ranks: base_value=43:14427, first_product=86:34038, bound_value=99:31655, second_product=198:13098, answer=203:14817)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=43:675, first_product=86:4693, bound_value=99:3542, second_product=198:194, answer=203:384)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `↵` (target ranks: base_value=43:33, first_product=86:142, bound_value=99:120, second_product=198:23, answer=203:37)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=43:46, first_product=86:186, bound_value=99:148, second_product=198:38, answer=203:53)

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
