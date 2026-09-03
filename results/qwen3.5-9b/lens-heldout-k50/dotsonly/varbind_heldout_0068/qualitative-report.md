# First qualitative filler readout

These are **logit-lens token readouts** (final norm + unembedding applied to each block's residual); no Jacobian lens was used.

## Outcome

- Filler answer: `113` (correct).
- No-filler answer: `109` (incorrect).
- Filler tokens: 50 tokens at absolute indices 876–925.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| Logit lens | `base_value=17` | 13 (L5, filler 3) | Never |
| Logit lens | `first_product=34` | 3 (L29, filler 12) | L29, filler 12 (rank 3) |
| Logit lens | `bound_value=50` | 5 (L30, filler 12) | L30, filler 12 (rank 5) |
| Logit lens | `second_product=100` | 13 (L5, filler 3) | Never |
| Logit lens | `answer=113` | 13 (L5, filler 3) | Never |

## Logit lens top-5 by filler position

### Filler position 1 (absolute token 876, surface ` .`)

- Layer 0: ` `, `-`, `<|endoftext|>`, `↵`, `s` (target ranks: base_value=17:24, first_product=34:110, bound_value=50:289, second_product=100:24, answer=113:24)
- Layer 8: `�`, `s`, `�`, `f`, `us` (target ranks: base_value=17:300, first_product=34:6858, bound_value=50:3457, second_product=100:300, answer=113:300)
- Layer 16: `utable`, `基数`, `再`, `Tac`, ` const` (target ranks: base_value=17:26258, first_product=34:57908, bound_value=50:19725, second_product=100:26258, answer=113:26258)
- Layer 24: `:x`, `基数`, `变量`, `"x`, `%X` (target ranks: base_value=17:240733, first_product=34:244085, bound_value=50:238048, second_product=100:240733, answer=113:240733)
- Layer 25: `基数`, `基础`, `变量`, `的基础`, `:x` (target ranks: base_value=17:232893, first_product=34:239239, bound_value=50:233578, second_product=100:232893, answer=113:232893)
- Layer 26: `基础`, `基数`, `的基础`, `变量`, ` base` (target ranks: base_value=17:241976, first_product=34:237142, bound_value=50:229094, second_product=100:241976, answer=113:241976)
- Layer 27: ` x`, `*x`, `"x`, `;x`, `+x` (target ranks: base_value=17:241274, first_product=34:238296, bound_value=50:241938, second_product=100:241274, answer=113:241274)
- Layer 28: ` x`, `*x`, `"x`, `+x`, `;x` (target ranks: base_value=17:230111, first_product=34:183149, bound_value=50:185285, second_product=100:230111, answer=113:230111)
- Layer 29: ` x`, `x`, `+x`, `*x`, `-x` (target ranks: base_value=17:71554, first_product=34:40944, bound_value=50:44349, second_product=100:71554, answer=113:71554)
- Layer 30: ` x`, `x`, ` .`, `-x`, ` X` (target ranks: base_value=17:395, first_product=34:299, bound_value=50:308, second_product=100:395, answer=113:395)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` x`, ` />` (target ranks: base_value=17:99, first_product=34:338, bound_value=50:606, second_product=100:99, answer=113:99)

### Filler position 2 (absolute token 877, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:21, first_product=34:170, bound_value=50:293, second_product=100:21, answer=113:21)
- Layer 8: `us`, `m`, `c`, `�`, `i` (target ranks: base_value=17:189, first_product=34:2553, bound_value=50:2759, second_product=100:189, answer=113:189)
- Layer 16: `utable`, `提`, `阁`, `基数`, `心` (target ranks: base_value=17:27524, first_product=34:100228, bound_value=50:21539, second_product=100:27524, answer=113:27524)
- Layer 24: `:x`, `/xhtml`, `xca`, `"x`, ` x` (target ranks: base_value=17:229348, first_product=34:246110, bound_value=50:239760, second_product=100:229348, answer=113:229348)
- Layer 25: ` x`, `xca`, `:x`, `/xhtml`, `"x` (target ranks: base_value=17:219882, first_product=34:245364, bound_value=50:237880, second_product=100:219882, answer=113:219882)
- Layer 26: `新加坡`, `xca`, `xbe`, `xdd`, `相辅相成` (target ranks: base_value=17:231532, first_product=34:243519, bound_value=50:233258, second_product=100:231532, answer=113:231532)
- Layer 27: ` x`, `*x`, `.x`, `	x`, `"x` (target ranks: base_value=17:228349, first_product=34:240092, bound_value=50:239450, second_product=100:228349, answer=113:228349)
- Layer 28: ` x`, `.x`, `*x`, ` .`, `+x` (target ranks: base_value=17:188105, first_product=34:187659, bound_value=50:183091, second_product=100:188105, answer=113:188105)
- Layer 29: ` x`, ` .`, `.x`, `x`, `�` (target ranks: base_value=17:44575, first_product=34:70615, bound_value=50:76843, second_product=100:44575, answer=113:44575)
- Layer 30: ` x`, ` .`, `x`, `.x`, `-x` (target ranks: base_value=17:235, first_product=34:409, bound_value=50:567, second_product=100:235, answer=113:235)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` x`, ` ,` (target ranks: base_value=17:47, first_product=34:112, bound_value=50:116, second_product=100:47, answer=113:47)

### Filler position 3 (absolute token 878, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `B` (target ranks: base_value=17:20, first_product=34:172, bound_value=50:294, second_product=100:20, answer=113:20)
- Layer 8: `er`, `en`, `us`, `in`, `o` (target ranks: base_value=17:683, first_product=34:8416, bound_value=50:2974, second_product=100:683, answer=113:683)
- Layer 16: `站`, `再加上`, `米`, `+m`, `orgen` (target ranks: base_value=17:29601, first_product=34:95222, bound_value=50:30654, second_product=100:29601, answer=113:29601)
- Layer 24: `吁`, `四十`, `ит`, `λεί`, `闲` (target ranks: base_value=17:247635, first_product=34:173329, bound_value=50:234503, second_product=100:247635, answer=113:247635)
- Layer 25: `吁`, `七十`, ` seventy`, `sas`, `燃` (target ranks: base_value=17:241248, first_product=34:182424, bound_value=50:234824, second_product=100:241248, answer=113:241248)
- Layer 26: `enang`, `спен`, `吁`, `九十`, `onders` (target ranks: base_value=17:222040, first_product=34:241955, bound_value=50:237864, second_product=100:222040, answer=113:222040)
- Layer 27: `九十`, ` eighty`, ` ninety`, `八十`, ` cien` (target ranks: base_value=17:235038, first_product=34:248319, bound_value=50:248299, second_product=100:235038, answer=113:235038)
- Layer 28: `九十`, ` cien`, ` ninety`, ` eighty`, `兴国` (target ranks: base_value=17:236315, first_product=34:248316, bound_value=50:248305, second_product=100:236315, answer=113:236315)
- Layer 29: `九十`, ` ninety`, `�`, ` cien`, `九` (target ranks: base_value=17:76102, first_product=34:248234, bound_value=50:248311, second_product=100:76102, answer=113:76102)
- Layer 30: `九十`, ` cien`, `九`, `9`, ` Nin` (target ranks: base_value=17:350, first_product=34:96088, bound_value=50:171145, second_product=100:350, answer=113:350)
- Layer 31: ` .`, `.`, ` ,`, ` `, ` :` (target ranks: base_value=17:2166, first_product=34:168021, bound_value=50:245674, second_product=100:2166, answer=113:2166)

### Filler position 4 (absolute token 879, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:21, first_product=34:173, bound_value=50:293, second_product=100:21, answer=113:21)
- Layer 8: `an`, `emo`, `ri`, `ut`, `us` (target ranks: base_value=17:3172, first_product=34:20758, bound_value=50:19081, second_product=100:3172, answer=113:3172)
- Layer 16: `uto`, `ällen`, `乱`, `name`, `ож` (target ranks: base_value=17:183272, first_product=34:204437, bound_value=50:42861, second_product=100:183272, answer=113:183272)
- Layer 24: `变量`, ` variables`, ` variable`, `-variable`, ` Variable` (target ranks: base_value=17:211315, first_product=34:236740, bound_value=50:164267, second_product=100:211315, answer=113:211315)
- Layer 25: `变量`, ` variables`, ` variable`, `-variable`, ` definitions` (target ranks: base_value=17:181787, first_product=34:228561, bound_value=50:151377, second_product=100:181787, answer=113:181787)
- Layer 26: `定义`, ` definitions`, ` definition`, `定义的`, ` defined` (target ranks: base_value=17:153093, first_product=34:204292, bound_value=50:113457, second_product=100:153093, answer=113:153093)
- Layer 27: ` variable`, `variable`, `变量`, ` Variable`, `Variable` (target ranks: base_value=17:240814, first_product=34:241457, bound_value=50:228129, second_product=100:240814, answer=113:240814)
- Layer 28: ` variable`, `variable`, `变量`, ` variables`, ` definitions` (target ranks: base_value=17:211874, first_product=34:176950, bound_value=50:177405, second_product=100:211874, answer=113:211874)
- Layer 29: ` definitions`, `定义`, ` variable`, `定义的`, ` variables` (target ranks: base_value=17:43253, first_product=34:54926, bound_value=50:74990, second_product=100:43253, answer=113:43253)
- Layer 30: ` .`, ` definitions`, ` var`, ` variable`, `定义的` (target ranks: base_value=17:914, first_product=34:1761, bound_value=50:4935, second_product=100:914, answer=113:914)
- Layer 31: ` .`, `<|im_end|>`, ` ..`, ` ,`, ` :` (target ranks: base_value=17:48, first_product=34:206, bound_value=50:503, second_product=100:48, answer=113:48)

### Filler position 5 (absolute token 880, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `<|endoftext|>` (target ranks: base_value=17:21, first_product=34:169, bound_value=50:294, second_product=100:21, answer=113:21)
- Layer 8: `触`, `istrator`, `ary`, `pring`, `us` (target ranks: base_value=17:16127, first_product=34:57296, bound_value=50:55849, second_product=100:16127, answer=113:16127)
- Layer 16: `utable`, `�`, `:normal`, `基数`, `ament` (target ranks: base_value=17:38108, first_product=34:150818, bound_value=50:48181, second_product=100:38108, answer=113:38108)
- Layer 24: `:x`, `*x`, `+x`, `psilon`, `ukt` (target ranks: base_value=17:115812, first_product=34:226737, bound_value=50:188033, second_product=100:115812, answer=113:115812)
- Layer 25: `:x`, `*x`, `licit`, `基数`, `ukt` (target ranks: base_value=17:123148, first_product=34:212245, bound_value=50:156671, second_product=100:123148, answer=113:123148)
- Layer 26: `加拿大`, `新加坡`, `êng`, `ièrement`, `基数` (target ranks: base_value=17:164038, first_product=34:206381, bound_value=50:152913, second_product=100:164038, answer=113:164038)
- Layer 27: ` x`, `*x`, `+x`, `:x`, `olang` (target ranks: base_value=17:27178, first_product=34:140437, bound_value=50:165314, second_product=100:27178, answer=113:27178)
- Layer 28: ` x`, `*x`, `️`, ` ‎`, `+x` (target ranks: base_value=17:4892, first_product=34:27966, bound_value=50:73565, second_product=100:4892, answer=113:4892)
- Layer 29: ` x`, `x`, ` .`, `*x`, `️` (target ranks: base_value=17:226, first_product=34:4182, bound_value=50:12410, second_product=100:226, answer=113:226)
- Layer 30: ` x`, ` .`, `x`, `-x`, ` ` (target ranks: base_value=17:29, first_product=34:214, bound_value=50:506, second_product=100:29, answer=113:29)
- Layer 31: ` .`, `<|im_end|>`, ` ,`, ` ..`, ` ` (target ranks: base_value=17:58, first_product=34:170, bound_value=50:283, second_product=100:58, answer=113:58)

### Filler position 6 (absolute token 881, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `.` (target ranks: base_value=17:21, first_product=34:169, bound_value=50:286, second_product=100:21, answer=113:21)
- Layer 8: `ainer`, `an`, `�`, `t`, `s` (target ranks: base_value=17:3790, first_product=34:18064, bound_value=50:10840, second_product=100:3790, answer=113:3790)
- Layer 16: `扣`, `明`, `地`, `旗`, `禁` (target ranks: base_value=17:19874, first_product=34:50922, bound_value=50:8427, second_product=100:19874, answer=113:19874)
- Layer 24: `/filepath`, `ာ`, `stery`, `员`, `帼` (target ranks: base_value=17:148680, first_product=34:159929, bound_value=50:62646, second_product=100:148680, answer=113:148680)
- Layer 25: `/filepath`, `帼`, `asi`, `ာ`, `ambda` (target ranks: base_value=17:133724, first_product=34:138268, bound_value=50:44253, second_product=100:133724, answer=113:133724)
- Layer 26: `erm`, `usercontent`, `imensional`, `umeric`, `ćen` (target ranks: base_value=17:146573, first_product=34:97812, bound_value=50:37678, second_product=100:146573, answer=113:146573)
- Layer 27: ` .`, `-.`, `．`, ` `.`, ` $.` (target ranks: base_value=17:172534, first_product=34:171985, bound_value=50:118117, second_product=100:172534, answer=113:172534)
- Layer 28: ` .`, `-.`, `．`, `!.`, `/.` (target ranks: base_value=17:70619, first_product=34:53383, bound_value=50:43836, second_product=100:70619, answer=113:70619)
- Layer 29: ` .`, `-.`, `!.`, `．`, `_.` (target ranks: base_value=17:3276, first_product=34:8331, bound_value=50:5824, second_product=100:3276, answer=113:3276)
- Layer 30: ` .`, ` `.`, ` ..`, ` ,`, ` ."` (target ranks: base_value=17:195, first_product=34:348, bound_value=50:607, second_product=100:195, answer=113:195)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ,` (target ranks: base_value=17:35, first_product=34:165, bound_value=50:195, second_product=100:35, answer=113:35)

### Filler position 7 (absolute token 882, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `B` (target ranks: base_value=17:20, first_product=34:167, bound_value=50:284, second_product=100:20, answer=113:20)
- Layer 8: `�`, `u`, `�`, `istrator`, `r` (target ranks: base_value=17:8826, first_product=34:17746, bound_value=50:14053, second_product=100:8826, answer=113:8826)
- Layer 16: `禁`, ` `, `明`, `成立`, `截` (target ranks: base_value=17:5164, first_product=34:15379, bound_value=50:10966, second_product=100:5164, answer=113:5164)
- Layer 24: `ariate`, `່`, `/filepath`, `ons`, `雨露` (target ranks: base_value=17:149399, first_product=34:156976, bound_value=50:88361, second_product=100:149399, answer=113:149399)
- Layer 25: `ariate`, `/filepath`, `່`, `极`, `yyyy` (target ranks: base_value=17:105953, first_product=34:93496, bound_value=50:37488, second_product=100:105953, answer=113:105953)
- Layer 26: `յ`, `usercontent`, `雨露`, `undreds`, `ariate` (target ranks: base_value=17:145844, first_product=34:72582, bound_value=50:48879, second_product=100:145844, answer=113:145844)
- Layer 27: ` .`, ` `.`, `-.`, `/.`, `．` (target ranks: base_value=17:190974, first_product=34:168063, bound_value=50:124623, second_product=100:190974, answer=113:190974)
- Layer 28: ` .`, `-.`, ` `.`, `/.`, ` {.` (target ranks: base_value=17:80634, first_product=34:34693, bound_value=50:35687, second_product=100:80634, answer=113:80634)
- Layer 29: ` .`, `-.`, ` `.`, `!.`, ` {.` (target ranks: base_value=17:4635, first_product=34:4398, bound_value=50:2876, second_product=100:4635, answer=113:4635)
- Layer 30: ` .`, ` `.`, ` ..`, ` ."`, ` ,` (target ranks: base_value=17:310, first_product=34:228, bound_value=50:248, second_product=100:310, answer=113:310)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, `↵` (target ranks: base_value=17:56, first_product=34:164, bound_value=50:148, second_product=100:56, answer=113:56)

### Filler position 8 (absolute token 883, surface ` .`)

- Layer 0: ` `, `↵`, `-`, `_`, `B` (target ranks: base_value=17:21, first_product=34:166, bound_value=50:284, second_product=100:21, answer=113:21)
- Layer 8: `u`, `t`, `i`, `m`, `en` (target ranks: base_value=17:264, first_product=34:6101, bound_value=50:3872, second_product=100:264, answer=113:264)
- Layer 16: `erce`, `aring`, `orial`, `基础`, `王星` (target ranks: base_value=17:47057, first_product=34:117340, bound_value=50:26410, second_product=100:47057, answer=113:47057)
- Layer 24: `吁`, `四十`, `λεί`, `燃`, `ит` (target ranks: base_value=17:245028, first_product=34:125859, bound_value=50:198235, second_product=100:245028, answer=113:245028)
- Layer 25: `七十`, `八十`, `燃`, `吁`, ` seventy` (target ranks: base_value=17:217732, first_product=34:107246, bound_value=50:185154, second_product=100:217732, answer=113:217732)
- Layer 26: `olygon`, `菁`, `燃`, `九十`, `enang` (target ranks: base_value=17:194116, first_product=34:211658, bound_value=50:202604, second_product=100:194116, answer=113:194116)
- Layer 27: `九十`, `八十`, ` eighty`, ` ninety`, `�` (target ranks: base_value=17:221340, first_product=34:248320, bound_value=50:248002, second_product=100:221340, answer=113:221340)
- Layer 28: `九十`, ` eighty`, `�`, ` ninety`, `八十` (target ranks: base_value=17:220103, first_product=34:248308, bound_value=50:248297, second_product=100:220103, answer=113:220103)
- Layer 29: `九十`, `九`, ` ninety`, `�`, `八` (target ranks: base_value=17:36977, first_product=34:246855, bound_value=50:248297, second_product=100:36977, answer=113:36977)
- Layer 30: ` .`, `九十`, `9`, `九`, ` ninety` (target ranks: base_value=17:1414, first_product=34:14689, bound_value=50:46441, second_product=100:1414, answer=113:1414)
- Layer 31: ` .`, ` ,`, ` :`, ` `, ` =` (target ranks: base_value=17:179, first_product=34:4371, bound_value=50:22455, second_product=100:179, answer=113:179)

### Filler position 9 (absolute token 884, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:165, bound_value=50:283, second_product=100:19, answer=113:19)
- Layer 8: `�`, `en`, `ar`, `�`, `u` (target ranks: base_value=17:9464, first_product=34:22983, bound_value=50:11246, second_product=100:9464, answer=113:9464)
- Layer 16: `<think>`, `地方`, `stery`, `再加上`, `ero` (target ranks: base_value=17:25576, first_product=34:46780, bound_value=50:19109, second_product=100:25576, answer=113:25576)
- Layer 24: `ит`, `吁`, `五十`, `四十`, `�` (target ranks: base_value=17:236816, first_product=34:149615, bound_value=50:70423, second_product=100:236816, answer=113:236816)
- Layer 25: `七十`, ` seventy`, `四十`, `六十`, `五十` (target ranks: base_value=17:216123, first_product=34:87733, bound_value=50:67510, second_product=100:216123, answer=113:216123)
- Layer 26: `燃`, `九十`, `菁`, `enang`, `巧` (target ranks: base_value=17:137488, first_product=34:194361, bound_value=50:55835, second_product=100:137488, answer=113:137488)
- Layer 27: `九十`, `�`, ` ninety`, `八十`, `一百` (target ranks: base_value=17:210931, first_product=34:248319, bound_value=50:247530, second_product=100:210931, answer=113:210931)
- Layer 28: `九十`, `�`, ` ninety`, `�`, `九` (target ranks: base_value=17:163236, first_product=34:248312, bound_value=50:248315, second_product=100:163236, answer=113:163236)
- Layer 29: `九`, `九十`, `�`, ` ninety`, `9` (target ranks: base_value=17:4753, first_product=34:247946, bound_value=50:248316, second_product=100:4753, answer=113:4753)
- Layer 30: ` .`, `9`, `九`, `九十`, ` ninety` (target ranks: base_value=17:29, first_product=34:12173, bound_value=50:27160, second_product=100:29, answer=113:29)
- Layer 31: ` .`, ` ,`, ` :`, `<|im_end|>`, ` ..` (target ranks: base_value=17:97, first_product=34:13918, bound_value=50:53621, second_product=100:97, answer=113:97)

### Filler position 10 (absolute token 885, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:165, bound_value=50:282, second_product=100:19, answer=113:19)
- Layer 8: `和`, `o`, `u`, `en`, `用` (target ranks: base_value=17:3066, first_product=34:14947, bound_value=50:10920, second_product=100:3066, answer=113:3066)
- Layer 16: `提`, `服`, `内`, `地`, `�` (target ranks: base_value=17:7072, first_product=34:21931, bound_value=50:27273, second_product=100:7072, answer=113:7072)
- Layer 24: `յ`, `longleftrightarrow`, `ariate`, `cket`, `�` (target ranks: base_value=17:214076, first_product=34:233195, bound_value=50:209275, second_product=100:214076, answer=113:214076)
- Layer 25: `յ`, `longleftrightarrow`, `�`, `cket`, `asi` (target ranks: base_value=17:194305, first_product=34:218620, bound_value=50:174110, second_product=100:194305, answer=113:194305)
- Layer 26: `յ`, `ćen`, `最新发布`, `asi`, `�` (target ranks: base_value=17:190925, first_product=34:181563, bound_value=50:148190, second_product=100:190925, answer=113:190925)
- Layer 27: ` .`, `-.`, ` `.`, ` $.`, `．` (target ranks: base_value=17:179627, first_product=34:217124, bound_value=50:198902, second_product=100:179627, answer=113:179627)
- Layer 28: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=17:105770, first_product=34:104629, bound_value=50:107651, second_product=100:105770, answer=113:105770)
- Layer 29: ` .`, `-.`, `!.`, ` `.`, `．` (target ranks: base_value=17:7241, first_product=34:11773, bound_value=50:8476, second_product=100:7241, answer=113:7241)
- Layer 30: ` .`, ` ..`, ` `.`, `-.`, `(.` (target ranks: base_value=17:234, first_product=34:222, bound_value=50:513, second_product=100:234, answer=113:234)
- Layer 31: ` .`, `<|im_end|>`, ` `, `↵↵`, ` ..` (target ranks: base_value=17:45, first_product=34:194, bound_value=50:273, second_product=100:45, answer=113:45)

### Filler position 11 (absolute token 886, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:163, bound_value=50:282, second_product=100:19, answer=113:19)
- Layer 8: `�`, `�`, `u`, `干`, `和` (target ranks: base_value=17:2964, first_product=34:4049, bound_value=50:3242, second_product=100:2964, answer=113:2964)
- Layer 16: `地`, `提`, `服`, `ံ`, `有效` (target ranks: base_value=17:5722, first_product=34:23763, bound_value=50:23332, second_product=100:5722, answer=113:5722)
- Layer 24: `ာ`, `员`, `之`, `յ`, `世` (target ranks: base_value=17:200498, first_product=34:220832, bound_value=50:184908, second_product=100:200498, answer=113:200498)
- Layer 25: `յ`, `ာ`, ` .`, `之`, `longleftrightarrow` (target ranks: base_value=17:166179, first_product=34:193158, bound_value=50:143151, second_product=100:166179, answer=113:166179)
- Layer 26: `յ`, ` .`, `ာ`, `而又`, `ек` (target ranks: base_value=17:197346, first_product=34:178357, bound_value=50:134658, second_product=100:197346, answer=113:197346)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=17:187090, first_product=34:213267, bound_value=50:177018, second_product=100:187090, answer=113:187090)
- Layer 28: ` .`, `-.`, `．`, ` `.`, `而又` (target ranks: base_value=17:132252, first_product=34:102517, bound_value=50:94339, second_product=100:132252, answer=113:132252)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=17:11753, first_product=34:11558, bound_value=50:7110, second_product=100:11753, answer=113:11753)
- Layer 30: ` .`, ` ..`, ` `.`, `-.`, `/.` (target ranks: base_value=17:780, first_product=34:394, bound_value=50:512, second_product=100:780, answer=113:780)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:82, first_product=34:169, bound_value=50:148, second_product=100:82, answer=113:82)

### Filler position 12 (absolute token 887, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:159, bound_value=50:281, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `有`, `en`, `t` (target ranks: base_value=17:367, first_product=34:3675, bound_value=50:1652, second_product=100:367, answer=113:367)
- Layer 16: `erm`, `�`, `踏`, `ermen`, `王星` (target ranks: base_value=17:17211, first_product=34:47021, bound_value=50:21572, second_product=100:17211, answer=113:17211)
- Layer 24: `piring`, `zni`, `十三条`, `ourcing`, `OBO` (target ranks: base_value=17:245882, first_product=34:62061, bound_value=50:201955, second_product=100:245882, answer=113:245882)
- Layer 25: `piring`, `十三条`, `二十二`, `رم`, `OBO` (target ranks: base_value=17:234981, first_product=34:9630, bound_value=50:161245, second_product=100:234981, answer=113:234981)
- Layer 26: `十三条`, `piring`, `三十`, `رم`, `lectual` (target ranks: base_value=17:241966, first_product=34:882, bound_value=50:203060, second_product=100:241966, answer=113:241966)
- Layer 27: ` x`, `*x`, `三十`, `�`, `四十` (target ranks: base_value=17:247194, first_product=34:775, bound_value=50:75802, second_product=100:247194, answer=113:247194)
- Layer 28: ` x`, `OBO`, `x`, `ascular`, `非` (target ranks: base_value=17:215648, first_product=34:4918, bound_value=50:6436, second_product=100:215648, answer=113:215648)
- Layer 29: ` x`, `x`, `3`, `�`, `非` (target ranks: base_value=17:13327, first_product=34:3, bound_value=50:79, second_product=100:13327, answer=113:13327)
- Layer 30: ` .`, ` x`, `x`, `4`, `5` (target ranks: base_value=17:2830, first_product=34:6, bound_value=50:5, second_product=100:2830, answer=113:2830)
- Layer 31: ` .`, ` ,`, ` ..`, ` `, `<|im_end|>` (target ranks: base_value=17:172, first_product=34:186, bound_value=50:241, second_product=100:172, answer=113:172)

### Filler position 13 (absolute token 888, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:161, bound_value=50:280, second_product=100:19, answer=113:19)
- Layer 8: `�`, `�`, `s`, `m`, `r` (target ranks: base_value=17:7327, first_product=34:10395, bound_value=50:13246, second_product=100:7327, answer=113:7327)
- Layer 16: `提`, `ersi`, `�`, `ံ`, ` ...` (target ranks: base_value=17:58979, first_product=34:132567, bound_value=50:88196, second_product=100:58979, answer=113:58979)
- Layer 24: `longleftrightarrow`, `ariate`, `cket`, `íguez`, `յ` (target ranks: base_value=17:225562, first_product=34:230471, bound_value=50:217166, second_product=100:225562, answer=113:225562)
- Layer 25: `յ`, `cket`, `longleftrightarrow`, `而又`, ` .` (target ranks: base_value=17:214491, first_product=34:215158, bound_value=50:190790, second_product=100:214491, answer=113:214491)
- Layer 26: `յ`, ` .`, `scht`, `longleftrightarrow`, `而又` (target ranks: base_value=17:205255, first_product=34:174843, bound_value=50:176354, second_product=100:205255, answer=113:205255)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:209624, first_product=34:221061, bound_value=50:210279, second_product=100:209624, answer=113:209624)
- Layer 28: ` .`, ` `.`, `-.`, `!.`, ` ..` (target ranks: base_value=17:128948, first_product=34:45602, bound_value=50:108812, second_product=100:128948, answer=113:128948)
- Layer 29: ` .`, `-.`, ` `.`, `!.`, `．` (target ranks: base_value=17:6856, first_product=34:1653, bound_value=50:5332, second_product=100:6856, answer=113:6856)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `/.` (target ranks: base_value=17:252, first_product=34:40, bound_value=50:114, second_product=100:252, answer=113:252)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:90, first_product=34:132, bound_value=50:176, second_product=100:90, answer=113:90)

### Filler position 14 (absolute token 889, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:161, bound_value=50:278, second_product=100:19, answer=113:19)
- Layer 8: `u`, `和`, `表示`, `ers`, `有` (target ranks: base_value=17:1053, first_product=34:12417, bound_value=50:3918, second_product=100:1053, answer=113:1053)
- Layer 16: `ံ`, `地`, `提`, `望`, `服` (target ranks: base_value=17:24213, first_product=34:89822, bound_value=50:36668, second_product=100:24213, answer=113:24213)
- Layer 24: `longleftrightarrow`, `յ`, `ек`, `ာ`, `家` (target ranks: base_value=17:218351, first_product=34:228401, bound_value=50:197742, second_product=100:218351, answer=113:218351)
- Layer 25: `յ`, `longleftrightarrow`, `家`, `ек`, `ာ` (target ranks: base_value=17:198623, first_product=34:213672, bound_value=50:165943, second_product=100:198623, answer=113:198623)
- Layer 26: `յ`, `ек`, `longleftrightarrow`, `ာ`, `်` (target ranks: base_value=17:196896, first_product=34:179438, bound_value=50:136385, second_product=100:196896, answer=113:196896)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` .$` (target ranks: base_value=17:190781, first_product=34:217769, bound_value=50:188085, second_product=100:190781, answer=113:190781)
- Layer 28: ` .`, `-.`, `．`, ` `.`, ` ..` (target ranks: base_value=17:100174, first_product=34:98493, bound_value=50:82640, second_product=100:100174, answer=113:100174)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `!.` (target ranks: base_value=17:7811, first_product=34:10839, bound_value=50:4774, second_product=100:7811, answer=113:7811)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:602, first_product=34:466, bound_value=50:297, second_product=100:602, answer=113:602)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:116, first_product=34:324, bound_value=50:190, second_product=100:116, answer=113:116)

### Filler position 15 (absolute token 890, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:161, bound_value=50:279, second_product=100:19, answer=113:19)
- Layer 8: `u`, `s`, `和`, `ared`, `t` (target ranks: base_value=17:1507, first_product=34:5735, bound_value=50:3313, second_product=100:1507, answer=113:1507)
- Layer 16: `提`, `ံ`, `地`, `始`, `服` (target ranks: base_value=17:17675, first_product=34:56410, bound_value=50:37341, second_product=100:17675, answer=113:17675)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ambda`, `家` (target ranks: base_value=17:205523, first_product=34:219396, bound_value=50:166734, second_product=100:205523, answer=113:205523)
- Layer 25: `յ`, `之`, `家`, ` .`, `longleftrightarrow` (target ranks: base_value=17:176406, first_product=34:196590, bound_value=50:129900, second_product=100:176406, answer=113:176406)
- Layer 26: `յ`, ` .`, `uks`, `longleftrightarrow`, `itan` (target ranks: base_value=17:187769, first_product=34:169536, bound_value=50:101804, second_product=100:187769, answer=113:187769)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, `-.` (target ranks: base_value=17:201678, first_product=34:219773, bound_value=50:179055, second_product=100:201678, answer=113:201678)
- Layer 28: ` .`, ` `.`, `-.`, `．`, `!.` (target ranks: base_value=17:124606, first_product=34:117294, bound_value=50:102599, second_product=100:124606, answer=113:124606)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `!.` (target ranks: base_value=17:10233, first_product=34:12530, bound_value=50:7043, second_product=100:10233, answer=113:10233)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:1351, first_product=34:1077, bound_value=50:582, second_product=100:1351, answer=113:1351)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:152, first_product=34:510, bound_value=50:255, second_product=100:152, answer=113:152)

### Filler position 16 (absolute token 891, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:157, bound_value=50:278, second_product=100:19, answer=113:19)
- Layer 8: `s`, `r`, `u`, `m`, `�` (target ranks: base_value=17:2109, first_product=34:8388, bound_value=50:6460, second_product=100:2109, answer=113:2109)
- Layer 16: `提`, `ods`, `始`, ` ...`, `ံ` (target ranks: base_value=17:22979, first_product=34:103488, bound_value=50:43821, second_product=100:22979, answer=113:22979)
- Layer 24: `յ`, `longleftrightarrow`, `cket`, `íguez`, `家` (target ranks: base_value=17:217520, first_product=34:228113, bound_value=50:187838, second_product=100:217520, answer=113:217520)
- Layer 25: `յ`, `longleftrightarrow`, `家`, `cket`, ` .` (target ranks: base_value=17:194544, first_product=34:212026, bound_value=50:159404, second_product=100:194544, answer=113:194544)
- Layer 26: `յ`, `uks`, ` .`, `scht`, `longleftrightarrow` (target ranks: base_value=17:218045, first_product=34:203025, bound_value=50:166155, second_product=100:218045, answer=113:218045)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .=` (target ranks: base_value=17:218426, first_product=34:231530, bound_value=50:209612, second_product=100:218426, answer=113:218426)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:132553, first_product=34:128322, bound_value=50:121637, second_product=100:132553, answer=113:132553)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `().` (target ranks: base_value=17:14209, first_product=34:16377, bound_value=50:11759, second_product=100:14209, answer=113:14209)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:1455, first_product=34:1339, bound_value=50:812, second_product=100:1455, answer=113:1455)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:131, first_product=34:554, bound_value=50:284, second_product=100:131, answer=113:131)

### Filler position 17 (absolute token 892, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:159, bound_value=50:277, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `r`, `m` (target ranks: base_value=17:1464, first_product=34:10950, bound_value=50:5864, second_product=100:1464, answer=113:1464)
- Layer 16: `提`, `地`, `ံ`, ` ...`, `内` (target ranks: base_value=17:16920, first_product=34:109183, bound_value=50:36906, second_product=100:16920, answer=113:16920)
- Layer 24: `յ`, `longleftrightarrow`, `ек`, `ambda`, `之` (target ranks: base_value=17:205427, first_product=34:219236, bound_value=50:162459, second_product=100:205427, answer=113:205427)
- Layer 25: `յ`, `longleftrightarrow`, `ек`, `家`, ` .` (target ranks: base_value=17:182602, first_product=34:197668, bound_value=50:126636, second_product=100:182602, answer=113:182602)
- Layer 26: `յ`, `uks`, `ек`, ` .`, `longleftrightarrow` (target ranks: base_value=17:206524, first_product=34:185972, bound_value=50:127696, second_product=100:206524, answer=113:206524)
- Layer 27: ` .`, ` `.`, `．`, ` .$`, ` ..` (target ranks: base_value=17:196059, first_product=34:219333, bound_value=50:185377, second_product=100:196059, answer=113:196059)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:100581, first_product=34:98371, bound_value=50:90445, second_product=100:100581, answer=113:100581)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:7911, first_product=34:10635, bound_value=50:6339, second_product=100:7911, answer=113:7911)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` ."` (target ranks: base_value=17:735, first_product=34:825, bound_value=50:404, second_product=100:735, answer=113:735)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:140, first_product=34:687, bound_value=50:294, second_product=100:140, answer=113:140)

### Filler position 18 (absolute token 893, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:155, bound_value=50:277, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `�`, `r` (target ranks: base_value=17:1711, first_product=34:11104, bound_value=50:5970, second_product=100:1711, answer=113:1711)
- Layer 16: `提`, `ံ`, `ods`, `始`, `地` (target ranks: base_value=17:22292, first_product=34:114171, bound_value=50:47696, second_product=100:22292, answer=113:22292)
- Layer 24: `յ`, `longleftrightarrow`, `家`, `ек`, `之` (target ranks: base_value=17:217917, first_product=34:230324, bound_value=50:187913, second_product=100:217917, answer=113:217917)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `之`, `ек` (target ranks: base_value=17:194280, first_product=34:214605, bound_value=50:157290, second_product=100:194280, answer=113:194280)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ာ`, `家` (target ranks: base_value=17:215688, first_product=34:205261, bound_value=50:150817, second_product=100:215688, answer=113:215688)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` .$` (target ranks: base_value=17:205211, first_product=34:227867, bound_value=50:194847, second_product=100:205211, answer=113:205211)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:111556, first_product=34:122173, bound_value=50:101550, second_product=100:111556, answer=113:111556)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `!.` (target ranks: base_value=17:9017, first_product=34:14851, bound_value=50:7383, second_product=100:9017, answer=113:9017)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:962, first_product=34:1147, bound_value=50:526, second_product=100:962, answer=113:962)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:140, first_product=34:569, bound_value=50:257, second_product=100:140, answer=113:140)

### Filler position 19 (absolute token 894, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:158, bound_value=50:276, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `�`, `r` (target ranks: base_value=17:2393, first_product=34:13713, bound_value=50:7861, second_product=100:2393, answer=113:2393)
- Layer 16: `提`, `ံ`, `ods`, `地`, `内` (target ranks: base_value=17:17128, first_product=34:89358, bound_value=50:40983, second_product=100:17128, answer=113:17128)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ек`, `家` (target ranks: base_value=17:211038, first_product=34:224021, bound_value=50:173468, second_product=100:211038, answer=113:211038)
- Layer 25: `յ`, `longleftrightarrow`, `家`, `之`, `ек` (target ranks: base_value=17:188347, first_product=34:205253, bound_value=50:138971, second_product=100:188347, answer=113:188347)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `scht`, ` .` (target ranks: base_value=17:204251, first_product=34:186069, bound_value=50:128420, second_product=100:204251, answer=113:204251)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:201036, first_product=34:222457, bound_value=50:183610, second_product=100:201036, answer=113:201036)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:104137, first_product=34:110748, bound_value=50:93781, second_product=100:104137, answer=113:104137)
- Layer 29: ` .`, ` `.`, `-.`, `．`, `!.` (target ranks: base_value=17:8302, first_product=34:13644, bound_value=50:7274, second_product=100:8302, answer=113:8302)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:929, first_product=34:1123, bound_value=50:534, second_product=100:929, answer=113:929)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:152, first_product=34:649, bound_value=50:305, second_product=100:152, answer=113:152)

### Filler position 20 (absolute token 895, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:153, bound_value=50:277, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `r`, `�` (target ranks: base_value=17:3159, first_product=34:15286, bound_value=50:9222, second_product=100:3159, answer=113:3159)
- Layer 16: `提`, `壁`, `口`, `地`, `ods` (target ranks: base_value=17:13687, first_product=34:68657, bound_value=50:38757, second_product=100:13687, answer=113:13687)
- Layer 24: `յ`, `longleftrightarrow`, `ек`, `之`, `家` (target ranks: base_value=17:206113, first_product=34:218658, bound_value=50:164921, second_product=100:206113, answer=113:206113)
- Layer 25: `յ`, `longleftrightarrow`, `家`, `之`, `ек` (target ranks: base_value=17:184147, first_product=34:198465, bound_value=50:129105, second_product=100:184147, answer=113:184147)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ож`, `年一季度` (target ranks: base_value=17:205651, first_product=34:181028, bound_value=50:125691, second_product=100:205651, answer=113:205651)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:197724, first_product=34:218235, bound_value=50:180507, second_product=100:197724, answer=113:197724)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:98393, first_product=34:102923, bound_value=50:87076, second_product=100:98393, answer=113:98393)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:8430, first_product=34:12436, bound_value=50:6418, second_product=100:8430, answer=113:8430)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:916, first_product=34:1014, bound_value=50:518, second_product=100:916, answer=113:916)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:145, first_product=34:619, bound_value=50:275, second_product=100:145, answer=113:145)

### Filler position 21 (absolute token 896, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:155, bound_value=50:274, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `r`, `o`, `t` (target ranks: base_value=17:3637, first_product=34:13732, bound_value=50:9216, second_product=100:3637, answer=113:3637)
- Layer 16: `提`, `壁`, `地`, `内`, `口` (target ranks: base_value=17:11771, first_product=34:55165, bound_value=50:37147, second_product=100:11771, answer=113:11771)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ек`, `家` (target ranks: base_value=17:198948, first_product=34:214297, bound_value=50:157832, second_product=100:198948, answer=113:198948)
- Layer 25: `յ`, `家`, `longleftrightarrow`, `之`, `ек` (target ranks: base_value=17:174776, first_product=34:193168, bound_value=50:123725, second_product=100:174776, answer=113:174776)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ек` (target ranks: base_value=17:201493, first_product=34:179339, bound_value=50:122275, second_product=100:201493, answer=113:201493)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:191688, first_product=34:217070, bound_value=50:178399, second_product=100:191688, answer=113:191688)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:90717, first_product=34:101811, bound_value=50:84673, second_product=100:90717, answer=113:90717)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:6786, first_product=34:11772, bound_value=50:5918, second_product=100:6786, answer=113:6786)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, ` .*` (target ranks: base_value=17:802, first_product=34:900, bound_value=50:471, second_product=100:802, answer=113:802)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:143, first_product=34:543, bound_value=50:261, second_product=100:143, answer=113:143)

### Filler position 22 (absolute token 897, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:154, bound_value=50:274, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `r`, `o`, `t` (target ranks: base_value=17:3569, first_product=34:13017, bound_value=50:9083, second_product=100:3569, answer=113:3569)
- Layer 16: `提`, `壁`, `内`, `地`, `ods` (target ranks: base_value=17:11112, first_product=34:52889, bound_value=50:36929, second_product=100:11112, answer=113:11112)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ек`, `家` (target ranks: base_value=17:194504, first_product=34:209909, bound_value=50:152734, second_product=100:194504, answer=113:194504)
- Layer 25: `յ`, `之`, `家`, `longleftrightarrow`, `ек` (target ranks: base_value=17:171669, first_product=34:188321, bound_value=50:121960, second_product=100:171669, answer=113:171669)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ек` (target ranks: base_value=17:197931, first_product=34:173346, bound_value=50:121337, second_product=100:197931, answer=113:197931)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:184948, first_product=34:212511, bound_value=50:172935, second_product=100:184948, answer=113:184948)
- Layer 28: ` .`, ` `.`, `-.`, `．`, ` ..` (target ranks: base_value=17:83404, first_product=34:95275, bound_value=50:80267, second_product=100:83404, answer=113:83404)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:5451, first_product=34:10507, bound_value=50:5378, second_product=100:5451, answer=113:5451)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:694, first_product=34:813, bound_value=50:437, second_product=100:694, answer=113:694)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:142, first_product=34:535, bound_value=50:265, second_product=100:142, answer=113:142)

### Filler position 23 (absolute token 898, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:151, bound_value=50:275, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `r`, `�` (target ranks: base_value=17:3694, first_product=34:15403, bound_value=50:9858, second_product=100:3694, answer=113:3694)
- Layer 16: `提`, `壁`, `内`, `ods`, `地` (target ranks: base_value=17:13042, first_product=34:63080, bound_value=50:42892, second_product=100:13042, answer=113:13042)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ек`, `家` (target ranks: base_value=17:193550, first_product=34:208065, bound_value=50:152168, second_product=100:193550, answer=113:193550)
- Layer 25: `յ`, `之`, `家`, `longleftrightarrow`, `ек` (target ranks: base_value=17:171383, first_product=34:186596, bound_value=50:120442, second_product=100:171383, answer=113:171383)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ာ`, `年一季度` (target ranks: base_value=17:197090, first_product=34:171262, bound_value=50:121195, second_product=100:197090, answer=113:197090)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:180927, first_product=34:209654, bound_value=50:169639, second_product=100:180927, answer=113:180927)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:80409, first_product=34:96051, bound_value=50:79896, second_product=100:80409, answer=113:80409)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:5131, first_product=34:10922, bound_value=50:5426, second_product=100:5131, answer=113:5131)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:662, first_product=34:836, bound_value=50:470, second_product=100:662, answer=113:662)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:143, first_product=34:533, bound_value=50:283, second_product=100:143, answer=113:143)

### Filler position 24 (absolute token 899, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:152, bound_value=50:274, second_product=100:19, answer=113:19)
- Layer 8: `s`, `o`, `u`, `�`, `r` (target ranks: base_value=17:3894, first_product=34:16188, bound_value=50:9990, second_product=100:3894, answer=113:3894)
- Layer 16: `提`, `壁`, `内`, `ods`, `地` (target ranks: base_value=17:13193, first_product=34:63546, bound_value=50:41549, second_product=100:13193, answer=113:13193)
- Layer 24: `յ`, `longleftrightarrow`, `之`, `ек`, `家` (target ranks: base_value=17:193946, first_product=34:210305, bound_value=50:153816, second_product=100:193946, answer=113:193946)
- Layer 25: `յ`, `之`, `longleftrightarrow`, `家`, `ек` (target ranks: base_value=17:171305, first_product=34:187525, bound_value=50:120774, second_product=100:171305, answer=113:171305)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ек` (target ranks: base_value=17:198913, first_product=34:175581, bound_value=50:123619, second_product=100:198913, answer=113:198913)
- Layer 27: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:180595, first_product=34:210081, bound_value=50:168763, second_product=100:180595, answer=113:180595)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:83983, first_product=34:102036, bound_value=50:83983, second_product=100:83983, answer=113:83983)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:5049, first_product=34:11309, bound_value=50:5511, second_product=100:5049, answer=113:5049)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:619, first_product=34:779, bound_value=50:453, second_product=100:619, answer=113:619)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:134, first_product=34:488, bound_value=50:266, second_product=100:134, answer=113:134)

### Filler position 25 (absolute token 900, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:18, first_product=34:151, bound_value=50:273, second_product=100:18, answer=113:18)
- Layer 8: `s`, `o`, `u`, `�`, `r` (target ranks: base_value=17:3561, first_product=34:16403, bound_value=50:10399, second_product=100:3561, answer=113:3561)
- Layer 16: `提`, `壁`, `ods`, `内`, `地` (target ranks: base_value=17:13883, first_product=34:64733, bound_value=50:42125, second_product=100:13883, answer=113:13883)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=17:191257, first_product=34:208457, bound_value=50:151051, second_product=100:191257, answer=113:191257)
- Layer 25: `յ`, `之`, `家`, `ек`, `longleftrightarrow` (target ranks: base_value=17:167389, first_product=34:184444, bound_value=50:117832, second_product=100:167389, answer=113:167389)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ек` (target ranks: base_value=17:194616, first_product=34:170257, bound_value=50:119782, second_product=100:194616, answer=113:194616)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:175330, first_product=34:206343, bound_value=50:164615, second_product=100:175330, answer=113:175330)
- Layer 28: ` .`, ` `.`, `．`, `-.`, ` ..` (target ranks: base_value=17:77406, first_product=34:95879, bound_value=50:79932, second_product=100:77406, answer=113:77406)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:4703, first_product=34:11273, bound_value=50:5417, second_product=100:4703, answer=113:4703)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:618, first_product=34:792, bound_value=50:470, second_product=100:618, answer=113:618)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:125, first_product=34:473, bound_value=50:266, second_product=100:125, answer=113:125)

### Filler position 26 (absolute token 901, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:151, bound_value=50:275, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `�`, `r` (target ranks: base_value=17:4013, first_product=34:18351, bound_value=50:12541, second_product=100:4013, answer=113:4013)
- Layer 16: `提`, `壁`, `ods`, `地`, `内` (target ranks: base_value=17:11350, first_product=34:53228, bound_value=50:38528, second_product=100:11350, answer=113:11350)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=17:185151, first_product=34:202333, bound_value=50:144226, second_product=100:185151, answer=113:185151)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:157004, first_product=34:173603, bound_value=50:107142, second_product=100:157004, answer=113:157004)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `年一季度`, `ек` (target ranks: base_value=17:191390, first_product=34:162878, bound_value=50:114242, second_product=100:191390, answer=113:191390)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:170128, first_product=34:200948, bound_value=50:158787, second_product=100:170128, answer=113:170128)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:74928, first_product=34:91368, bound_value=50:76421, second_product=100:74928, answer=113:74928)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:4505, first_product=34:10301, bound_value=50:4969, second_product=100:4505, answer=113:4505)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:587, first_product=34:707, bound_value=50:444, second_product=100:587, answer=113:587)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:123, first_product=34:445, bound_value=50:264, second_product=100:123, answer=113:123)

### Filler position 27 (absolute token 902, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:150, bound_value=50:269, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `o`, `�`, `�` (target ranks: base_value=17:5207, first_product=34:18958, bound_value=50:13516, second_product=100:5207, answer=113:5207)
- Layer 16: `提`, `内`, `壁`, `地`, `ods` (target ranks: base_value=17:8782, first_product=34:42214, bound_value=50:31077, second_product=100:8782, answer=113:8782)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=17:183566, first_product=34:202664, bound_value=50:142459, second_product=100:183566, answer=113:183566)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:157404, first_product=34:175645, bound_value=50:107479, second_product=100:157404, answer=113:157404)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ек`, `年一季度` (target ranks: base_value=17:194350, first_product=34:167881, bound_value=50:118182, second_product=100:194350, answer=113:194350)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:170468, first_product=34:202718, bound_value=50:159663, second_product=100:170468, answer=113:170468)
- Layer 28: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:74849, first_product=34:95682, bound_value=50:77605, second_product=100:74849, answer=113:74849)
- Layer 29: ` .`, `-.`, ` `.`, `．`, `().` (target ranks: base_value=17:4002, first_product=34:10368, bound_value=50:4681, second_product=100:4002, answer=113:4002)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:592, first_product=34:726, bound_value=50:439, second_product=100:592, answer=113:592)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:118, first_product=34:416, bound_value=50:257, second_product=100:118, answer=113:118)

### Filler position 28 (absolute token 903, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:151, bound_value=50:271, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `�`, `�`, `o` (target ranks: base_value=17:6971, first_product=34:20357, bound_value=50:14977, second_product=100:6971, answer=113:6971)
- Layer 16: `提`, `内`, `壁`, `地`, `ods` (target ranks: base_value=17:8687, first_product=34:40431, bound_value=50:31386, second_product=100:8687, answer=113:8687)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=17:178750, first_product=34:197855, bound_value=50:134590, second_product=100:178750, answer=113:178750)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:153228, first_product=34:170472, bound_value=50:100804, second_product=100:153228, answer=113:153228)
- Layer 26: `յ`, `uks`, `ек`, `longleftrightarrow`, `年一季度` (target ranks: base_value=17:190209, first_product=34:162656, bound_value=50:111699, second_product=100:190209, answer=113:190209)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:160171, first_product=34:195866, bound_value=50:150283, second_product=100:160171, answer=113:160171)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=17:70638, first_product=34:92249, bound_value=50:74684, second_product=100:70638, answer=113:70638)
- Layer 29: ` .`, `-.`, `．`, ` `.`, `().` (target ranks: base_value=17:3550, first_product=34:9713, bound_value=50:4399, second_product=100:3550, answer=113:3550)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:498, first_product=34:604, bound_value=50:368, second_product=100:498, answer=113:498)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:110, first_product=34:378, bound_value=50:241, second_product=100:110, answer=113:110)

### Filler position 29 (absolute token 904, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:150, bound_value=50:271, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `�`, `�`, `o` (target ranks: base_value=17:6831, first_product=34:20623, bound_value=50:15655, second_product=100:6831, answer=113:6831)
- Layer 16: `提`, `内`, `壁`, `ods`, `地` (target ranks: base_value=17:9062, first_product=34:45860, bound_value=50:34059, second_product=100:9062, answer=113:9062)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `家` (target ranks: base_value=17:178948, first_product=34:199808, bound_value=50:136866, second_product=100:178948, answer=113:178948)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:153656, first_product=34:171396, bound_value=50:103004, second_product=100:153656, answer=113:153656)
- Layer 26: `յ`, `uks`, `longleftrightarrow`, `ာ`, `itionally` (target ranks: base_value=17:191223, first_product=34:164871, bound_value=50:114081, second_product=100:191223, answer=113:191223)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:159144, first_product=34:195073, bound_value=50:149073, second_product=100:159144, answer=113:159144)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=17:68301, first_product=34:93450, bound_value=50:74484, second_product=100:68301, answer=113:68301)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:3437, first_product=34:10166, bound_value=50:4481, second_product=100:3437, answer=113:3437)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:496, first_product=34:623, bound_value=50:383, second_product=100:496, answer=113:496)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:105, first_product=34:368, bound_value=50:229, second_product=100:105, answer=113:105)

### Filler position 30 (absolute token 905, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `-`, `.` (target ranks: base_value=17:19, first_product=34:150, bound_value=50:271, second_product=100:19, answer=113:19)
- Layer 8: `s`, `�`, `�`, `o`, `u` (target ranks: base_value=17:9345, first_product=34:25002, bound_value=50:19312, second_product=100:9345, answer=113:9345)
- Layer 16: `提`, `内`, `ods`, `壁`, `佩` (target ranks: base_value=17:10209, first_product=34:50473, bound_value=50:35855, second_product=100:10209, answer=113:10209)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `家` (target ranks: base_value=17:182107, first_product=34:202750, bound_value=50:138910, second_product=100:182107, answer=113:182107)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:153014, first_product=34:171230, bound_value=50:100496, second_product=100:153014, answer=113:153014)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `ек` (target ranks: base_value=17:194843, first_product=34:169978, bound_value=50:116676, second_product=100:194843, answer=113:194843)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:157252, first_product=34:194433, bound_value=50:147704, second_product=100:157252, answer=113:157252)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=17:68931, first_product=34:96806, bound_value=50:75259, second_product=100:68931, answer=113:68931)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:3291, first_product=34:10443, bound_value=50:4507, second_product=100:3291, answer=113:3291)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:476, first_product=34:640, bound_value=50:399, second_product=100:476, answer=113:476)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:99, first_product=34:360, bound_value=50:232, second_product=100:99, answer=113:99)

### Filler position 31 (absolute token 906, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:151, bound_value=50:272, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `o`, `u` (target ranks: base_value=17:8534, first_product=34:24667, bound_value=50:19117, second_product=100:8534, answer=113:8534)
- Layer 16: `提`, `内`, `ods`, `壁`, `佩` (target ranks: base_value=17:11031, first_product=34:55190, bound_value=50:35530, second_product=100:11031, answer=113:11031)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `家` (target ranks: base_value=17:181284, first_product=34:201715, bound_value=50:137895, second_product=100:181284, answer=113:181284)
- Layer 25: `յ`, `之`, `ек`, `家`, `longleftrightarrow` (target ranks: base_value=17:153613, first_product=34:172426, bound_value=50:102556, second_product=100:153613, answer=113:153613)
- Layer 26: `յ`, `uks`, `ာ`, `longleftrightarrow`, `itionally` (target ranks: base_value=17:193705, first_product=34:170221, bound_value=50:118347, second_product=100:193705, answer=113:193705)
- Layer 27: ` .`, `．`, ` `.`, `-.`, ` ..` (target ranks: base_value=17:155627, first_product=34:194434, bound_value=50:147759, second_product=100:155627, answer=113:155627)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=17:67761, first_product=34:97219, bound_value=50:75958, second_product=100:67761, answer=113:67761)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:3206, first_product=34:10791, bound_value=50:4632, second_product=100:3206, answer=113:3206)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `-.` (target ranks: base_value=17:464, first_product=34:636, bound_value=50:409, second_product=100:464, answer=113:464)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:92, first_product=34:333, bound_value=50:222, second_product=100:92, answer=113:92)

### Filler position 32 (absolute token 907, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:151, bound_value=50:271, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=17:7687, first_product=34:24695, bound_value=50:19700, second_product=100:7687, answer=113:7687)
- Layer 16: `提`, `内`, `壁`, `ods`, `佩` (target ranks: base_value=17:9962, first_product=34:54439, bound_value=50:35934, second_product=100:9962, answer=113:9962)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `家` (target ranks: base_value=17:169813, first_product=34:193558, bound_value=50:125287, second_product=100:169813, answer=113:169813)
- Layer 25: `յ`, `之`, `ек`, `般`, `家` (target ranks: base_value=17:142638, first_product=34:161008, bound_value=50:89879, second_product=100:142638, answer=113:142638)
- Layer 26: `յ`, `uks`, `itionally`, `年一季度`, `ာ` (target ranks: base_value=17:183354, first_product=34:157836, bound_value=50:103731, second_product=100:183354, answer=113:183354)
- Layer 27: ` .`, `．`, ` `.`, ` ..`, `-.` (target ranks: base_value=17:149580, first_product=34:187891, bound_value=50:139867, second_product=100:149580, answer=113:149580)
- Layer 28: ` .`, `．`, ` `.`, `-.`, `而又` (target ranks: base_value=17:63581, first_product=34:90968, bound_value=50:70953, second_product=100:63581, answer=113:63581)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:2749, first_product=34:9320, bound_value=50:4159, second_product=100:2749, answer=113:2749)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=17:417, first_product=34:548, bound_value=50:365, second_product=100:417, answer=113:417)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` `, ` ..` (target ranks: base_value=17:88, first_product=34:316, bound_value=50:209, second_product=100:88, answer=113:88)

### Filler position 33 (absolute token 908, surface ` .`)

- Layer 0: ` `, `_`, `↵`, `.`, `-` (target ranks: base_value=17:19, first_product=34:150, bound_value=50:269, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `�`, `�`, `r` (target ranks: base_value=17:8740, first_product=34:23615, bound_value=50:20031, second_product=100:8740, answer=113:8740)
- Layer 16: `提`, `内`, `壁`, `ods`, `佩` (target ranks: base_value=17:9938, first_product=34:49232, bound_value=50:34178, second_product=100:9938, answer=113:9938)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `家` (target ranks: base_value=17:164166, first_product=34:187903, bound_value=50:117706, second_product=100:164166, answer=113:164166)
- Layer 25: `յ`, `之`, `般`, `ек`, `家` (target ranks: base_value=17:131202, first_product=34:151101, bound_value=50:81259, second_product=100:131202, answer=113:131202)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `年一季度` (target ranks: base_value=17:180825, first_product=34:153249, bound_value=50:100801, second_product=100:180825, answer=113:180825)
- Layer 27: ` .`, `．`, ` `.`, ` ..`, `-.` (target ranks: base_value=17:144766, first_product=34:182900, bound_value=50:134968, second_product=100:144766, answer=113:144766)
- Layer 28: ` .`, `．`, `-.`, ` `.`, `而又` (target ranks: base_value=17:60989, first_product=34:88186, bound_value=50:67375, second_product=100:60989, answer=113:60989)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:2621, first_product=34:8981, bound_value=50:3893, second_product=100:2621, answer=113:2621)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=17:416, first_product=34:541, bound_value=50:363, second_product=100:416, answer=113:416)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:78, first_product=34:290, bound_value=50:195, second_product=100:78, answer=113:78)

### Filler position 34 (absolute token 909, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:19, first_product=34:150, bound_value=50:268, second_product=100:19, answer=113:19)
- Layer 8: `s`, `u`, `�`, `�`, `�` (target ranks: base_value=17:10970, first_product=34:24237, bound_value=50:21231, second_product=100:10970, answer=113:10970)
- Layer 16: `提`, `内`, `佩`, `壁`, `ods` (target ranks: base_value=17:7692, first_product=34:37220, bound_value=50:28006, second_product=100:7692, answer=113:7692)
- Layer 24: `յ`, `之`, `ек`, `longleftrightarrow`, `ာ` (target ranks: base_value=17:160777, first_product=34:186897, bound_value=50:114002, second_product=100:160777, answer=113:160777)
- Layer 25: `յ`, `之`, `般`, `ек`, `家` (target ranks: base_value=17:126400, first_product=34:147054, bound_value=50:75318, second_product=100:126400, answer=113:126400)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `年一季度` (target ranks: base_value=17:179088, first_product=34:153107, bound_value=50:97579, second_product=100:179088, answer=113:179088)
- Layer 27: ` .`, `．`, ` `.`, ` ..`, `().` (target ranks: base_value=17:136854, first_product=34:177591, bound_value=50:128170, second_product=100:136854, answer=113:136854)
- Layer 28: ` .`, `．`, `而又`, ` `.`, `-.` (target ranks: base_value=17:58391, first_product=34:87045, bound_value=50:65368, second_product=100:58391, answer=113:58391)
- Layer 29: ` .`, `．`, `-.`, ` `.`, `().` (target ranks: base_value=17:2454, first_product=34:8745, bound_value=50:3839, second_product=100:2454, answer=113:2454)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=17:367, first_product=34:473, bound_value=50:324, second_product=100:367, answer=113:367)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:73, first_product=34:279, bound_value=50:192, second_product=100:73, answer=113:73)

### Filler position 35 (absolute token 910, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:150, bound_value=50:268, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `u`, `�`, `�` (target ranks: base_value=17:10167, first_product=34:24303, bound_value=50:20642, second_product=100:10167, answer=113:10167)
- Layer 16: `提`, `内`, `壁`, `佩`, `ods` (target ranks: base_value=17:9191, first_product=34:45476, bound_value=50:30487, second_product=100:9191, answer=113:9191)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `ာ` (target ranks: base_value=17:169739, first_product=34:193400, bound_value=50:120934, second_product=100:169739, answer=113:169739)
- Layer 25: `յ`, `之`, `般`, `ек`, `家` (target ranks: base_value=17:139026, first_product=34:157940, bound_value=50:84943, second_product=100:139026, answer=113:139026)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `xaf` (target ranks: base_value=17:187344, first_product=34:163715, bound_value=50:108471, second_product=100:187344, answer=113:187344)
- Layer 27: ` .`, `．`, ` ..`, ` `.`, `().` (target ranks: base_value=17:141275, first_product=34:183471, bound_value=50:133137, second_product=100:141275, answer=113:141275)
- Layer 28: ` .`, `．`, `而又`, ` ..`, ` `.` (target ranks: base_value=17:61107, first_product=34:94023, bound_value=50:68446, second_product=100:61107, answer=113:61107)
- Layer 29: ` .`, `．`, `-.`, `.`, `().` (target ranks: base_value=17:2551, first_product=34:9800, bound_value=50:4089, second_product=100:2551, answer=113:2551)
- Layer 30: ` .`, ` ..`, ` `.`, ` ,`, `．` (target ranks: base_value=17:397, first_product=34:526, bound_value=50:346, second_product=100:397, answer=113:397)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:68, first_product=34:265, bound_value=50:184, second_product=100:68, answer=113:68)

### Filler position 36 (absolute token 911, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:150, bound_value=50:268, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `u`, `�` (target ranks: base_value=17:10013, first_product=34:23872, bound_value=50:20531, second_product=100:10013, answer=113:10013)
- Layer 16: `提`, `内`, `佩`, `壁`, `ods` (target ranks: base_value=17:11069, first_product=34:55493, bound_value=50:35710, second_product=100:11069, answer=113:11069)
- Layer 24: `յ`, `之`, `longleftrightarrow`, `ек`, `ာ` (target ranks: base_value=17:165365, first_product=34:191309, bound_value=50:116996, second_product=100:165365, answer=113:165365)
- Layer 25: `յ`, `之`, `般`, `ек`, `家` (target ranks: base_value=17:128511, first_product=34:150233, bound_value=50:77035, second_product=100:128511, answer=113:128511)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `xaf` (target ranks: base_value=17:179952, first_product=34:158603, bound_value=50:100526, second_product=100:179952, answer=113:179952)
- Layer 27: ` .`, `．`, ` ..`, ` `.`, `().` (target ranks: base_value=17:136128, first_product=34:178945, bound_value=50:126948, second_product=100:136128, answer=113:136128)
- Layer 28: ` .`, `．`, `而又`, ` ..`, ` `.` (target ranks: base_value=17:57352, first_product=34:89441, bound_value=50:64931, second_product=100:57352, answer=113:57352)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=17:2271, first_product=34:9098, bound_value=50:3950, second_product=100:2271, answer=113:2271)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=17:308, first_product=34:452, bound_value=50:301, second_product=100:308, answer=113:308)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:67, first_product=34:252, bound_value=50:177, second_product=100:67, answer=113:67)

### Filler position 37 (absolute token 912, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:149, bound_value=50:268, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `�`, `u` (target ranks: base_value=17:10714, first_product=34:26563, bound_value=50:22079, second_product=100:10714, answer=113:10714)
- Layer 16: `提`, `内`, `ods`, `佩`, ` $` (target ranks: base_value=17:11924, first_product=34:56689, bound_value=50:34791, second_product=100:11924, answer=113:11924)
- Layer 24: `յ`, `之`, `ာ`, `longleftrightarrow`, `ек` (target ranks: base_value=17:165991, first_product=34:190465, bound_value=50:117091, second_product=100:165991, answer=113:165991)
- Layer 25: `յ`, `之`, `般`, `家`, `ек` (target ranks: base_value=17:127898, first_product=34:149208, bound_value=50:75510, second_product=100:127898, answer=113:127898)
- Layer 26: `յ`, `uks`, `ာ`, `itionally`, `xaf` (target ranks: base_value=17:181394, first_product=34:158529, bound_value=50:100300, second_product=100:181394, answer=113:181394)
- Layer 27: ` .`, `．`, ` ..`, `().`, `.` (target ranks: base_value=17:134388, first_product=34:176458, bound_value=50:123398, second_product=100:134388, answer=113:134388)
- Layer 28: ` .`, `．`, `而又`, ` ..`, ` `.` (target ranks: base_value=17:56064, first_product=34:88686, bound_value=50:63309, second_product=100:56064, answer=113:56064)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=17:2335, first_product=34:9469, bound_value=50:4036, second_product=100:2335, answer=113:2335)
- Layer 30: ` .`, ` ..`, ` `.`, `↵↵`, `．` (target ranks: base_value=17:310, first_product=34:433, bound_value=50:298, second_product=100:310, answer=113:310)
- Layer 31: ` .`, `<|im_end|>`, `↵↵`, ` ..`, ` ` (target ranks: base_value=17:60, first_product=34:223, bound_value=50:156, second_product=100:60, answer=113:60)

### Filler position 38 (absolute token 913, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:149, bound_value=50:269, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `�`, `u` (target ranks: base_value=17:10106, first_product=34:26482, bound_value=50:22544, second_product=100:10106, answer=113:10106)
- Layer 16: `提`, `内`, `佩`, `ods`, ` $` (target ranks: base_value=17:8649, first_product=34:46529, bound_value=50:29737, second_product=100:8649, answer=113:8649)
- Layer 24: `յ`, `之`, `ာ`, `ек`, `longleftrightarrow` (target ranks: base_value=17:158642, first_product=34:184243, bound_value=50:107448, second_product=100:158642, answer=113:158642)
- Layer 25: `յ`, `之`, `般`, ` .`, `itionally` (target ranks: base_value=17:115504, first_product=34:136856, bound_value=50:63325, second_product=100:115504, answer=113:115504)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `xaf` (target ranks: base_value=17:169083, first_product=34:145603, bound_value=50:85878, second_product=100:169083, answer=113:169083)
- Layer 27: ` .`, `．`, ` ..`, `().`, `.` (target ranks: base_value=17:123245, first_product=34:166312, bound_value=50:111093, second_product=100:123245, answer=113:123245)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `().` (target ranks: base_value=17:50591, first_product=34:81249, bound_value=50:56106, second_product=100:50591, answer=113:50591)
- Layer 29: ` .`, `．`, `.`, `-.`, `().` (target ranks: base_value=17:1839, first_product=34:7835, bound_value=50:3230, second_product=100:1839, answer=113:1839)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=17:250, first_product=34:359, bound_value=50:233, second_product=100:250, answer=113:250)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ` (target ranks: base_value=17:59, first_product=34:223, bound_value=50:154, second_product=100:59, answer=113:59)

### Filler position 39 (absolute token 914, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:266, second_product=100:18, answer=113:18)
- Layer 8: `s`, `u`, `�`, `�`, `�` (target ranks: base_value=17:9452, first_product=34:25302, bound_value=50:21985, second_product=100:9452, answer=113:9452)
- Layer 16: `提`, `内`, `佩`, `ods`, ` $` (target ranks: base_value=17:8058, first_product=34:47340, bound_value=50:30365, second_product=100:8058, answer=113:8058)
- Layer 24: `յ`, `之`, `ာ`, `longleftrightarrow`, `cket` (target ranks: base_value=17:154737, first_product=34:182536, bound_value=50:106325, second_product=100:154737, answer=113:154737)
- Layer 25: `յ`, `般`, `之`, ` .`, `itionally` (target ranks: base_value=17:117114, first_product=34:140254, bound_value=50:66645, second_product=100:117114, answer=113:117114)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `xaf` (target ranks: base_value=17:171459, first_product=34:149812, bound_value=50:89509, second_product=100:171459, answer=113:171459)
- Layer 27: ` .`, `．`, ` ..`, `.`, `յ` (target ranks: base_value=17:124035, first_product=34:166068, bound_value=50:110567, second_product=100:124035, answer=113:124035)
- Layer 28: ` .`, `．`, `而又`, ` ..`, `.` (target ranks: base_value=17:49025, first_product=34:82140, bound_value=50:54844, second_product=100:49025, answer=113:49025)
- Layer 29: ` .`, `．`, `.`, `↵↵`, `().` (target ranks: base_value=17:1782, first_product=34:7926, bound_value=50:3145, second_product=100:1782, answer=113:1782)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=17:250, first_product=34:357, bound_value=50:233, second_product=100:250, answer=113:250)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ` (target ranks: base_value=17:53, first_product=34:202, bound_value=50:141, second_product=100:53, answer=113:53)

### Filler position 40 (absolute token 915, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:265, second_product=100:18, answer=113:18)
- Layer 8: `s`, `u`, `�`, `�`, `�` (target ranks: base_value=17:12611, first_product=34:26235, bound_value=50:24063, second_product=100:12611, answer=113:12611)
- Layer 16: `提`, `内`, `佩`, ` $`, `ods` (target ranks: base_value=17:7355, first_product=34:37066, bound_value=50:26516, second_product=100:7355, answer=113:7355)
- Layer 24: `յ`, `之`, `ာ`, `່`, `ား` (target ranks: base_value=17:147026, first_product=34:173052, bound_value=50:95045, second_product=100:147026, answer=113:147026)
- Layer 25: `յ`, `之`, `般`, ` .`, `itionally` (target ranks: base_value=17:102847, first_product=34:122363, bound_value=50:53251, second_product=100:102847, answer=113:102847)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `xaf` (target ranks: base_value=17:154766, first_product=34:129496, bound_value=50:73436, second_product=100:154766, answer=113:154766)
- Layer 27: ` .`, `．`, ` ..`, `.`, `յ` (target ranks: base_value=17:113218, first_product=34:154252, bound_value=50:99419, second_product=100:113218, answer=113:113218)
- Layer 28: ` .`, `．`, ` ..`, `而又`, `.` (target ranks: base_value=17:43602, first_product=34:70200, bound_value=50:46976, second_product=100:43602, answer=113:43602)
- Layer 29: ` .`, `．`, `.`, `↵↵`, `().` (target ranks: base_value=17:1430, first_product=34:6118, bound_value=50:2602, second_product=100:1430, answer=113:1430)
- Layer 30: ` .`, ` ..`, `↵↵`, ` `.`, `．` (target ranks: base_value=17:204, first_product=34:276, bound_value=50:196, second_product=100:204, answer=113:204)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ` (target ranks: base_value=17:49, first_product=34:189, bound_value=50:130, second_product=100:49, answer=113:49)

### Filler position 41 (absolute token 916, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:265, second_product=100:18, answer=113:18)
- Layer 8: `s`, `u`, `�`, `�`, `�` (target ranks: base_value=17:10665, first_product=34:25174, bound_value=50:22522, second_product=100:10665, answer=113:10665)
- Layer 16: `提`, `内`, ` $`, `佩`, `ods` (target ranks: base_value=17:6543, first_product=34:35078, bound_value=50:24453, second_product=100:6543, answer=113:6543)
- Layer 24: `յ`, `之`, `ာ`, `=""`, `cket` (target ranks: base_value=17:153965, first_product=34:179689, bound_value=50:100859, second_product=100:153965, answer=113:153965)
- Layer 25: `յ`, `般`, `之`, `↵↵`, ` .` (target ranks: base_value=17:108625, first_product=34:131064, bound_value=50:57552, second_product=100:108625, answer=113:108625)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=17:165788, first_product=34:142261, bound_value=50:81826, second_product=100:165788, answer=113:165788)
- Layer 27: ` .`, `．`, `.`, `յ`, ` ..` (target ranks: base_value=17:116272, first_product=34:157831, bound_value=50:98953, second_product=100:116272, answer=113:116272)
- Layer 28: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=17:41802, first_product=34:73443, bound_value=50:44888, second_product=100:41802, answer=113:41802)
- Layer 29: ` .`, `．`, `.`, `↵↵`, `().` (target ranks: base_value=17:1345, first_product=34:6478, bound_value=50:2386, second_product=100:1345, answer=113:1345)
- Layer 30: ` .`, ` ..`, `↵↵`, `．`, ` ↵↵` (target ranks: base_value=17:190, first_product=34:266, bound_value=50:178, second_product=100:190, answer=113:190)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ..`, ` ↵↵` (target ranks: base_value=17:48, first_product=34:174, bound_value=50:110, second_product=100:48, answer=113:48)

### Filler position 42 (absolute token 917, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `u`, `�` (target ranks: base_value=17:11344, first_product=34:26127, bound_value=50:23751, second_product=100:11344, answer=113:11344)
- Layer 16: `提`, `内`, `佩`, ` $`, `ods` (target ranks: base_value=17:6248, first_product=34:34601, bound_value=50:23551, second_product=100:6248, answer=113:6248)
- Layer 24: `յ`, `之`, `ာ`, `=""`, `cket` (target ranks: base_value=17:150225, first_product=34:181526, bound_value=50:100104, second_product=100:150225, answer=113:150225)
- Layer 25: `յ`, `般`, `↵↵`, `之`, ` .` (target ranks: base_value=17:97178, first_product=34:124288, bound_value=50:51904, second_product=100:97178, answer=113:97178)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=17:153139, first_product=34:136885, bound_value=50:75201, second_product=100:153139, answer=113:153139)
- Layer 27: ` .`, `．`, ` ..`, `յ`, `.` (target ranks: base_value=17:105698, first_product=34:152919, bound_value=50:91852, second_product=100:105698, answer=113:105698)
- Layer 28: ` .`, `．`, `↵↵`, `般`, ` ..` (target ranks: base_value=17:38600, first_product=34:71555, bound_value=50:42732, second_product=100:38600, answer=113:38600)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=17:1185, first_product=34:5921, bound_value=50:2194, second_product=100:1185, answer=113:1185)
- Layer 30: ` .`, ` ..`, `↵↵`, `．`, ` ↵↵` (target ranks: base_value=17:139, first_product=34:213, bound_value=50:146, second_product=100:139, answer=113:139)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:46, first_product=34:172, bound_value=50:118, second_product=100:46, answer=113:46)

### Filler position 43 (absolute token 918, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:268, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `�`, `u` (target ranks: base_value=17:10352, first_product=34:25545, bound_value=50:22057, second_product=100:10352, answer=113:10352)
- Layer 16: `提`, `内`, `ods`, ` $`, `佩` (target ranks: base_value=17:8194, first_product=34:44636, bound_value=50:29222, second_product=100:8194, answer=113:8194)
- Layer 24: `յ`, `之`, `ာ`, `=""`, `ား` (target ranks: base_value=17:151910, first_product=34:184261, bound_value=50:105173, second_product=100:151910, answer=113:151910)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, `之` (target ranks: base_value=17:100128, first_product=34:129092, bound_value=50:56122, second_product=100:100128, answer=113:100128)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=17:158435, first_product=34:145038, bound_value=50:83048, second_product=100:158435, answer=113:158435)
- Layer 27: ` .`, `．`, `.`, `յ`, ` ..` (target ranks: base_value=17:100843, first_product=34:150005, bound_value=50:89926, second_product=100:100843, answer=113:100843)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `=""` (target ranks: base_value=17:34661, first_product=34:70375, bound_value=50:41751, second_product=100:34661, answer=113:34661)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=17:1031, first_product=34:5992, bound_value=50:2125, second_product=100:1031, answer=113:1031)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:124, first_product=34:221, bound_value=50:149, second_product=100:124, answer=113:124)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:45, first_product=34:166, bound_value=50:100, second_product=100:45, answer=113:45)

### Filler position 44 (absolute token 919, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `u`, `�` (target ranks: base_value=17:9101, first_product=34:25462, bound_value=50:21554, second_product=100:9101, answer=113:9101)
- Layer 16: `提`, `内`, `ods`, ` $`, `佩` (target ranks: base_value=17:7528, first_product=34:42660, bound_value=50:27544, second_product=100:7528, answer=113:7528)
- Layer 24: `յ`, `之`, `=""`, `ာ`, `cket` (target ranks: base_value=17:148322, first_product=34:181584, bound_value=50:101194, second_product=100:148322, answer=113:148322)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, `之` (target ranks: base_value=17:90486, first_product=34:120255, bound_value=50:49228, second_product=100:90486, answer=113:90486)
- Layer 26: `յ`, `uks`, `itionally`, `ာ`, `=""` (target ranks: base_value=17:144801, first_product=34:132071, bound_value=50:73082, second_product=100:144801, answer=113:144801)
- Layer 27: ` .`, `．`, ` ..`, `յ`, `.` (target ranks: base_value=17:91921, first_product=34:140612, bound_value=50:81571, second_product=100:91921, answer=113:91921)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `=""` (target ranks: base_value=17:30608, first_product=34:63298, bound_value=50:37415, second_product=100:30608, answer=113:30608)
- Layer 29: ` .`, `．`, `↵↵`, `.`, `().` (target ranks: base_value=17:850, first_product=34:5037, bound_value=50:1852, second_product=100:850, answer=113:850)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:107, first_product=34:192, bound_value=50:121, second_product=100:107, answer=113:107)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:45, first_product=34:157, bound_value=50:107, second_product=100:45, answer=113:45)

### Filler position 45 (absolute token 920, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `u`, `o` (target ranks: base_value=17:9346, first_product=34:25360, bound_value=50:22720, second_product=100:9346, answer=113:9346)
- Layer 16: `提`, `内`, `ods`, `佩`, `三` (target ranks: base_value=17:6032, first_product=34:33914, bound_value=50:24217, second_product=100:6032, answer=113:6032)
- Layer 24: `յ`, `之`, `=""`, `ာ`, `cket` (target ranks: base_value=17:138270, first_product=34:173487, bound_value=50:92315, second_product=100:138270, answer=113:138270)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, `itionally` (target ranks: base_value=17:80749, first_product=34:112970, bound_value=50:43235, second_product=100:80749, answer=113:80749)
- Layer 26: `յ`, `uks`, `itionally`, `=""`, `ာ` (target ranks: base_value=17:137031, first_product=34:125853, bound_value=50:66829, second_product=100:137031, answer=113:137031)
- Layer 27: ` .`, `．`, `յ`, `.`, `↵↵` (target ranks: base_value=17:88170, first_product=34:136541, bound_value=50:76645, second_product=100:88170, answer=113:88170)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `=""` (target ranks: base_value=17:29537, first_product=34:63657, bound_value=50:35529, second_product=100:29537, answer=113:29537)
- Layer 29: ` .`, `．`, `↵↵`, `.`, ` ..` (target ranks: base_value=17:811, first_product=34:4932, bound_value=50:1657, second_product=100:811, answer=113:811)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:107, first_product=34:181, bound_value=50:112, second_product=100:107, answer=113:107)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:46, first_product=34:149, bound_value=50:96, second_product=100:46, answer=113:46)

### Filler position 46 (absolute token 921, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:269, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=17:8699, first_product=34:24941, bound_value=50:22187, second_product=100:8699, answer=113:8699)
- Layer 16: `提`, `内`, `佩`, `ods`, ` $` (target ranks: base_value=17:5188, first_product=34:32940, bound_value=50:23362, second_product=100:5188, answer=113:5188)
- Layer 24: `յ`, `之`, `=""`, `ာ`, `cket` (target ranks: base_value=17:136431, first_product=34:175112, bound_value=50:92447, second_product=100:136431, answer=113:136431)
- Layer 25: `յ`, `↵↵`, ` .`, `般`, `itionally` (target ranks: base_value=17:77230, first_product=34:110831, bound_value=50:41620, second_product=100:77230, answer=113:77230)
- Layer 26: `յ`, `uks`, `itionally`, `=""`, `ာ` (target ranks: base_value=17:136447, first_product=34:127357, bound_value=50:67715, second_product=100:136447, answer=113:136447)
- Layer 27: ` .`, `．`, `յ`, `.`, `↵↵` (target ranks: base_value=17:84040, first_product=34:135079, bound_value=50:74530, second_product=100:84040, answer=113:84040)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `=""` (target ranks: base_value=17:26614, first_product=34:60755, bound_value=50:32887, second_product=100:26614, answer=113:26614)
- Layer 29: ` .`, `↵↵`, `．`, `.`, `().` (target ranks: base_value=17:685, first_product=34:4439, bound_value=50:1495, second_product=100:685, answer=113:685)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:91, first_product=34:156, bound_value=50:99, second_product=100:91, answer=113:91)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:43, first_product=34:146, bound_value=50:94, second_product=100:43, answer=113:43)

### Filler position 47 (absolute token 922, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=17:9304, first_product=34:24037, bound_value=50:20495, second_product=100:9304, answer=113:9304)
- Layer 16: `提`, `内`, `佩`, `三`, ` $` (target ranks: base_value=17:4592, first_product=34:25329, bound_value=50:22919, second_product=100:4592, answer=113:4592)
- Layer 24: `յ`, `之`, `=""`, `ာ`, `cket` (target ranks: base_value=17:133661, first_product=34:169216, bound_value=50:90972, second_product=100:133661, answer=113:133661)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, `之` (target ranks: base_value=17:73960, first_product=34:104952, bound_value=50:41194, second_product=100:73960, answer=113:73960)
- Layer 26: `յ`, `uks`, `itionally`, `=""`, `ာ` (target ranks: base_value=17:130875, first_product=34:119897, bound_value=50:65998, second_product=100:130875, answer=113:130875)
- Layer 27: ` .`, `．`, `↵↵`, `յ`, `.` (target ranks: base_value=17:81249, first_product=34:128668, bound_value=50:71862, second_product=100:81249, answer=113:81249)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `.` (target ranks: base_value=17:24472, first_product=34:56594, bound_value=50:31196, second_product=100:24472, answer=113:24472)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ..` (target ranks: base_value=17:580, first_product=34:3966, bound_value=50:1366, second_product=100:580, answer=113:580)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:82, first_product=34:150, bound_value=50:100, second_product=100:82, answer=113:82)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:42, first_product=34:141, bound_value=50:93, second_product=100:42, answer=113:42)

### Filler position 48 (absolute token 923, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `u`, `�`, `o` (target ranks: base_value=17:9010, first_product=34:22808, bound_value=50:19703, second_product=100:9010, answer=113:9010)
- Layer 16: `提`, `内`, `ods`, ` $`, `三` (target ranks: base_value=17:5008, first_product=34:25613, bound_value=50:25363, second_product=100:5008, answer=113:5008)
- Layer 24: `յ`, `=""`, `之`, `ာ`, `↵↵` (target ranks: base_value=17:141651, first_product=34:177032, bound_value=50:98151, second_product=100:141651, answer=113:141651)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, `=""` (target ranks: base_value=17:77021, first_product=34:110110, bound_value=50:43699, second_product=100:77021, answer=113:77021)
- Layer 26: `յ`, `uks`, `itionally`, `=""`, `ာ` (target ranks: base_value=17:136857, first_product=34:128657, bound_value=50:69442, second_product=100:136857, answer=113:136857)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=17:78143, first_product=34:126830, bound_value=50:66824, second_product=100:78143, answer=113:78143)
- Layer 28: ` .`, `．`, `↵↵`, `般`, `=""` (target ranks: base_value=17:22966, first_product=34:57498, bound_value=50:29242, second_product=100:22966, answer=113:22966)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=17:542, first_product=34:4031, bound_value=50:1237, second_product=100:542, answer=113:542)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:78, first_product=34:142, bound_value=50:93, second_product=100:78, answer=113:78)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:45, first_product=34:147, bound_value=50:93, second_product=100:45, answer=113:45)

### Filler position 49 (absolute token 924, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:267, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `o`, `�` (target ranks: base_value=17:10661, first_product=34:25420, bound_value=50:21670, second_product=100:10661, answer=113:10661)
- Layer 16: `提`, `内`, `ods`, `佩`, `三` (target ranks: base_value=17:4982, first_product=34:21818, bound_value=50:21624, second_product=100:4982, answer=113:4982)
- Layer 24: `յ`, `=""`, `↵↵`, `ာ`, `之` (target ranks: base_value=17:138444, first_product=34:173575, bound_value=50:92392, second_product=100:138444, answer=113:138444)
- Layer 25: `յ`, `↵↵`, `般`, ` .`, ` ↵↵` (target ranks: base_value=17:73015, first_product=34:103789, bound_value=50:38544, second_product=100:73015, answer=113:73015)
- Layer 26: `յ`, `itionally`, `uks`, `=""`, `ာ` (target ranks: base_value=17:133287, first_product=34:124288, bound_value=50:64410, second_product=100:133287, answer=113:133287)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=17:73964, first_product=34:121332, bound_value=50:60335, second_product=100:73964, answer=113:73964)
- Layer 28: ` .`, `↵↵`, `．`, `般`, `=""` (target ranks: base_value=17:19792, first_product=34:51291, bound_value=50:25220, second_product=100:19792, answer=113:19792)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=17:419, first_product=34:3230, bound_value=50:1025, second_product=100:419, answer=113:419)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `．` (target ranks: base_value=17:63, first_product=34:121, bound_value=50:79, second_product=100:63, answer=113:63)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:42, first_product=34:144, bound_value=50:92, second_product=100:42, answer=113:42)

### Filler position 50 (absolute token 925, surface ` .`)

- Layer 0: ` `, `↵`, `_`, `.`, `-` (target ranks: base_value=17:18, first_product=34:148, bound_value=50:266, second_product=100:18, answer=113:18)
- Layer 8: `s`, `�`, `�`, `o`, `u` (target ranks: base_value=17:8957, first_product=34:25340, bound_value=50:20312, second_product=100:8957, answer=113:8957)
- Layer 16: `提`, `内`, `ods`, `三`, ` $` (target ranks: base_value=17:4761, first_product=34:24032, bound_value=50:23303, second_product=100:4761, answer=113:4761)
- Layer 24: `յ`, `↵↵`, `=""`, `ာ`, `cket` (target ranks: base_value=17:139440, first_product=34:178140, bound_value=50:95104, second_product=100:139440, answer=113:139440)
- Layer 25: `↵↵`, `յ`, `般`, ` .`, ` ↵↵` (target ranks: base_value=17:70918, first_product=34:105801, bound_value=50:38224, second_product=100:70918, answer=113:70918)
- Layer 26: `յ`, `itionally`, `uks`, `=""`, `ာ` (target ranks: base_value=17:135001, first_product=34:131098, bound_value=50:67155, second_product=100:135001, answer=113:135001)
- Layer 27: ` .`, `．`, `↵↵`, ` ↵↵`, `յ` (target ranks: base_value=17:65722, first_product=34:116254, bound_value=50:54452, second_product=100:65722, answer=113:65722)
- Layer 28: ` .`, `↵↵`, `．`, `般`, ` ↵↵` (target ranks: base_value=17:16359, first_product=34:48871, bound_value=50:22366, second_product=100:16359, answer=113:16359)
- Layer 29: ` .`, `↵↵`, `．`, `.`, ` ↵↵` (target ranks: base_value=17:306, first_product=34:2726, bound_value=50:752, second_product=100:306, answer=113:306)
- Layer 30: ` .`, `↵↵`, ` ..`, ` ↵↵`, `↵` (target ranks: base_value=17:57, first_product=34:107, bound_value=50:69, second_product=100:57, answer=113:57)
- Layer 31: ` .`, `↵↵`, `<|im_end|>`, ` ↵↵`, ` ..` (target ranks: base_value=17:43, first_product=34:153, bound_value=50:95, second_product=100:43, answer=113:43)

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
