# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `256` (correct).
- No-filler answer: `16` (incorrect).
- Filler tokens: 10 tokens at absolute indices 448–457.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `x_1=86` | 64 (L35, filler 6) | Never |
| J-Lens | `x_2=70` | 337 (L41, filler 10) | Never |
| J-Lens | `x_3=16` | 501 (L41, filler 10) | Never |
| J-Lens | `x_4=256` | 201 (L41, filler 10) | Never |
| Logit lens | `x_1=86` | 65 (L41, filler 10) | Never |
| Logit lens | `x_2=70` | 107 (L5, filler 1) | Never |
| Logit lens | `x_3=16` | 501 (L41, filler 10) | Never |
| Logit lens | `x_4=256` | 175 (L40, filler 10) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 448, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `?datasetId` (target ranks: x_1=86:118159, x_2=70:116921, x_3=16:120891, x_4=256:114630)
- Layer 10: `Walker`, ` Walker`, `锁定`, `anta`, `fine` (target ranks: x_1=86:22082, x_2=70:23321, x_3=16:23056, x_4=256:34785)
- Layer 20: `甸`, `旬`, `足`, `cape`, `表面` (target ranks: x_1=86:862, x_2=70:842, x_3=16:2025, x_4=256:16785)
- Layer 30: `提问`, `重复`, ` question`, ` repetitions`, `询问` (target ranks: x_1=86:35837, x_2=70:32827, x_3=16:32859, x_4=256:97753)
- Layer 35: `重复`, ` Question`, ` question`, ` repetitions`, `Question` (target ranks: x_1=86:11723, x_2=70:14746, x_3=16:8387, x_4=256:73837)
- Layer 36: `重复`, `期望`, `泛`, ` Question`, `询问` (target ranks: x_1=86:8693, x_2=70:11938, x_3=16:10037, x_4=256:48941)
- Layer 37: ` Question`, `泛`, ` question`, ` prompt`, `提问` (target ranks: x_1=86:24768, x_2=70:45711, x_3=16:29566, x_4=256:87931)
- Layer 38: ` Question`, ` prompt`, `提问`, `Question`, ` question` (target ranks: x_1=86:43604, x_2=70:51278, x_3=16:40469, x_4=256:104732)
- Layer 39: `�`, `迷惑`, `额外`, ` talags`, `hatic` (target ranks: x_1=86:112501, x_2=70:89096, x_3=16:124878, x_4=256:113382)
- Layer 40: ` talags`, ` filler`, `oooo`, `dots`, `�` (target ranks: x_1=86:84919, x_2=70:42723, x_3=16:111948, x_4=256:107437)
- Layer 41: ` .`, ` .↵↵`, `耘`, ` without`, ` separately` (target ranks: x_1=86:58696, x_2=70:47096, x_3=16:88614, x_4=256:67476)

### Filler position 2 (absolute token 449, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: x_1=86:120289, x_2=70:119977, x_3=16:122823, x_4=256:119349)
- Layer 10: ` Walker`, `从哪里`, `ait`, `Walker`, `atile` (target ranks: x_1=86:27893, x_2=70:30169, x_3=16:24503, x_4=256:39673)
- Layer 20: ` .`, `外向`, `auce`, ` distant`, `�` (target ranks: x_1=86:25913, x_2=70:21816, x_3=16:36420, x_4=256:63697)
- Layer 30: ` .`, `oooo`, ` tears`, `ilig`, `翻` (target ranks: x_1=86:48319, x_2=70:70978, x_3=16:65583, x_4=256:85524)
- Layer 35: ` .`, `ilig`, `私`, ` dots`, `幽` (target ranks: x_1=86:68620, x_2=70:81656, x_3=16:91604, x_4=256:122242)
- Layer 36: `odor`, ` .`, `私`, `幽`, `匣` (target ranks: x_1=86:58319, x_2=70:68873, x_3=16:82639, x_4=256:110711)
- Layer 37: `}<?`, ` Erkännande`, `enclose`, ` .`, `tanle` (target ranks: x_1=86:114561, x_2=70:114679, x_3=16:124034, x_4=256:127761)
- Layer 38: ` .`, ` .↵↵`, `}<?`, `enclose`, ` .↵` (target ranks: x_1=86:110160, x_2=70:105558, x_3=16:118146, x_4=256:127659)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>`, ` nasod` (target ranks: x_1=86:112884, x_2=70:107899, x_3=16:123673, x_4=256:117644)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` filler` (target ranks: x_1=86:91851, x_2=70:62118, x_3=16:99561, x_4=256:97529)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `美`, ` nasod` (target ranks: x_1=86:47458, x_2=70:36759, x_3=16:57649, x_4=256:60288)

### Filler position 3 (absolute token 450, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:123869, x_2=70:123858, x_3=16:125362, x_4=256:122558)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: x_1=86:12324, x_2=70:15604, x_3=16:11057, x_4=256:23059)
- Layer 20: `足`, `s`, `ait`, `�`, `che` (target ranks: x_1=86:1897, x_2=70:8069, x_3=16:3807, x_4=256:14741)
- Layer 30: ` repetitions`, ` repeated`, `反复`, ` repetition`, ` repeating` (target ranks: x_1=86:5825, x_2=70:55426, x_3=16:9870, x_4=256:11999)
- Layer 35: ` repeated`, ` repetitions`, ` repetition`, `重复`, ` repeating` (target ranks: x_1=86:3531, x_2=70:43051, x_3=16:5808, x_4=256:17106)
- Layer 36: ` repeated`, `重复`, ` repetition`, ` repetitions`, `反复` (target ranks: x_1=86:2075, x_2=70:30563, x_3=16:14147, x_4=256:9050)
- Layer 37: ` repeated`, `反复`, `重复`, ` repetitions`, ` repetition` (target ranks: x_1=86:10825, x_2=70:98309, x_3=16:50385, x_4=256:13063)
- Layer 38: ` repeated`, ` quadratic`, ` squ`, `反复`, ` Blum` (target ranks: x_1=86:25009, x_2=70:111635, x_3=16:77325, x_4=256:26719)
- Layer 39: ` Blum`, ` Bl`, `大王`, `打磨`, ` repeated` (target ranks: x_1=86:84960, x_2=70:107504, x_3=16:117539, x_4=256:103522)
- Layer 40: ` repeated`, ` x`, ` `, `反复`, ` repetition` (target ranks: x_1=86:45946, x_2=70:69625, x_3=16:65118, x_4=256:83804)
- Layer 41: ` .`, ` `, ` accumulating`, ` fused`, ` dots` (target ranks: x_1=86:20353, x_2=70:53444, x_3=16:38646, x_4=256:54760)

### Filler position 4 (absolute token 451, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:124501, x_2=70:124535, x_3=16:126042, x_4=256:123686)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: x_1=86:13714, x_2=70:15453, x_3=16:11500, x_4=256:24045)
- Layer 20: `ait`, `幽`, `cape`, `atile`, `足` (target ranks: x_1=86:3061, x_2=70:7449, x_3=16:3968, x_4=256:18417)
- Layer 30: ` expecting`, `保留`, ` quadr`, `30`, ` executable` (target ranks: x_1=86:4249, x_2=70:3949, x_3=16:37210, x_4=256:30475)
- Layer 35: `900`, `九百`, `909`, `904`, `902` (target ranks: x_1=86:3301, x_2=70:9992, x_3=16:16817, x_4=256:9689)
- Layer 36: `900`, `九百`, `904`, `909`, `902` (target ranks: x_1=86:710, x_2=70:12167, x_3=16:29436, x_4=256:1578)
- Layer 37: `900`, `九百`, `904`, `909`, `902` (target ranks: x_1=86:1236, x_2=70:13611, x_3=16:30393, x_4=256:1811)
- Layer 38: `900`, `九百`, `904`, `901`, `902` (target ranks: x_1=86:1524, x_2=70:18931, x_3=16:29357, x_4=256:4333)
- Layer 39: `}<?`, `九百`, `900`, `Nin`, `青青` (target ranks: x_1=86:64317, x_2=70:79078, x_3=16:117852, x_4=256:31824)
- Layer 40: `}<?`, `青青`, `صد`, ` Noise`, `九百` (target ranks: x_1=86:25978, x_2=70:45254, x_3=16:67844, x_4=256:4488)
- Layer 41: ` .`, ` fused`, `青青`, ` ,`, `试一试` (target ranks: x_1=86:36671, x_2=70:75222, x_3=16:58555, x_4=256:9030)

### Filler position 5 (absolute token 452, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: x_1=86:124523, x_2=70:124413, x_3=16:126166, x_4=256:123843)
- Layer 10: ` Walker`, `Walker`, `锁定`, `挪`, `ait` (target ranks: x_1=86:18892, x_2=70:21403, x_3=16:15878, x_4=256:29478)
- Layer 20: `鞍`, `锁定`, `幽`, `挪`, `足` (target ranks: x_1=86:14410, x_2=70:18307, x_3=16:21033, x_4=256:31097)
- Layer 30: `反复`, `步骤`, `calcul`, `一步步`, `算出` (target ranks: x_1=86:3932, x_2=70:19680, x_3=16:48980, x_4=256:36298)
- Layer 35: `反复`, `步骤`, `每一步`, ` repetition`, `第一步` (target ranks: x_1=86:2500, x_2=70:19154, x_3=16:29723, x_4=256:24194)
- Layer 36: `反复`, `步骤`, `calcul`, `进行计算`, `翻` (target ranks: x_1=86:7079, x_2=70:39758, x_3=16:71399, x_4=256:23316)
- Layer 37: `}<?`, `殿堂`, `oNames`, `覆`, `otechnical` (target ranks: x_1=86:28806, x_2=70:87479, x_3=16:101559, x_4=256:43954)
- Layer 38: `oNames`, `hemer`, `}<?`, `otechnical`, `殿堂` (target ranks: x_1=86:48949, x_2=70:100284, x_3=16:114878, x_4=256:60500)
- Layer 39: `hemer`, `}<?`, `oNames`, `叶子`, `覆` (target ranks: x_1=86:95632, x_2=70:112907, x_3=16:123215, x_4=256:63129)
- Layer 40: ` .`, `hemer`, ` x`, `语言文字`, `etted` (target ranks: x_1=86:68761, x_2=70:89254, x_3=16:102065, x_4=256:37503)
- Layer 41: ` .`, ` .↵↵`, ` because`, `.,`, ` waiting` (target ranks: x_1=86:37010, x_2=70:61126, x_3=16:76398, x_4=256:26336)

### Filler position 6 (absolute token 453, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:124133, x_2=70:123773, x_3=16:125916, x_4=256:123573)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=86:14367, x_2=70:16774, x_3=16:12111, x_4=256:24578)
- Layer 20: `鞍`, `锁定`, `挪`, `忑`, ` smile` (target ranks: x_1=86:4041, x_2=70:5711, x_3=16:7262, x_4=256:19211)
- Layer 30: `鞍`, `步骤`, ` basal`, ` tap`, `反复` (target ranks: x_1=86:218, x_2=70:899, x_3=16:12945, x_4=256:10604)
- Layer 35: ` stabil`, `鞍`, ` waterfall`, `忑`, ` tap` (target ranks: x_1=86:64, x_2=70:493, x_3=16:3786, x_4=256:8829)
- Layer 36: ` stabil`, `筋`, `悬`, `ess`, `反复` (target ranks: x_1=86:365, x_2=70:1880, x_3=16:21479, x_4=256:11270)
- Layer 37: `筋`, `}<?`, `悬`, `悬挂`, ` clos` (target ranks: x_1=86:3063, x_2=70:18622, x_3=16:45022, x_4=256:18907)
- Layer 38: `}<?`, `osine`, ` politic`, `筋`, `ucl` (target ranks: x_1=86:17387, x_2=70:48948, x_3=16:83882, x_4=256:40646)
- Layer 39: `}<?`, `-ulo`, `叶子`, `?datasetId`, `hemer` (target ranks: x_1=86:94719, x_2=70:101125, x_3=16:114765, x_4=256:49735)
- Layer 40: ` talags`, `试一试`, `筋`, `不思`, `一个个` (target ranks: x_1=86:74524, x_2=70:83928, x_3=16:76980, x_4=256:24751)
- Layer 41: ` .`, `试一试`, ` waiting`, `试试`, ` .↵↵` (target ranks: x_1=86:63023, x_2=70:79287, x_3=16:73631, x_4=256:43872)

### Filler position 7 (absolute token 454, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:124103, x_2=70:123617, x_3=16:125877, x_4=256:123386)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: x_1=86:14868, x_2=70:16466, x_3=16:12382, x_4=256:25386)
- Layer 20: `锁定`, `鞍`, ` smile`, `忑`, ` Walker` (target ranks: x_1=86:9137, x_2=70:5937, x_3=16:12480, x_4=256:20800)
- Layer 30: ` step`, `一步步`, `步骤`, ` Step`, `第一步` (target ranks: x_1=86:6204, x_2=70:2412, x_3=16:69076, x_4=256:94983)
- Layer 35: ` step`, ` Step`, `步骤`, `Step`, `三步` (target ranks: x_1=86:3804, x_2=70:1278, x_3=16:26749, x_4=256:60259)
- Layer 36: ` step`, ` Step`, `步骤`, `Step`, `三步` (target ranks: x_1=86:6643, x_2=70:3409, x_3=16:55552, x_4=256:44807)
- Layer 37: ` Step`, ` step`, `步骤`, `-step`, `三步` (target ranks: x_1=86:26278, x_2=70:12741, x_3=16:96448, x_4=256:86334)
- Layer 38: ` Step`, ` step`, `步骤`, `-step`, ` Steps` (target ranks: x_1=86:45129, x_2=70:21102, x_3=16:109615, x_4=256:96436)
- Layer 39: `}<?`, ` Step`, `一步步`, `hemer`, `步步` (target ranks: x_1=86:106947, x_2=70:69171, x_3=16:123720, x_4=256:116564)
- Layer 40: ` fifty`, `五十`, `一个个`, ` Step`, ` step` (target ranks: x_1=86:84965, x_2=70:29409, x_3=16:107968, x_4=256:110507)
- Layer 41: ` .`, `一个个`, ` .↵↵`, `一个好`, ` fifty` (target ranks: x_1=86:59801, x_2=70:19400, x_3=16:91957, x_4=256:79354)

### Filler position 8 (absolute token 455, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:124126, x_2=70:123529, x_3=16:125853, x_4=256:123220)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=86:13076, x_2=70:14108, x_3=16:10330, x_4=256:22765)
- Layer 20: ` Walker`, ` smile`, ` quadr`, `ait`, `Walker` (target ranks: x_1=86:6367, x_2=70:3833, x_3=16:3712, x_4=256:22460)
- Layer 30: ` spac`, `codeline`, `dividers`, `东京`, ` Cosm` (target ranks: x_1=86:39328, x_2=70:69548, x_3=16:97119, x_4=256:125073)
- Layer 35: ` .`, `川`, `不急`, ` soci`, `耐心` (target ranks: x_1=86:17907, x_2=70:62032, x_3=16:57040, x_4=256:117618)
- Layer 36: ` soci`, `长大的`, `odor`, `重复`, `留存` (target ranks: x_1=86:6921, x_2=70:28932, x_3=16:32361, x_4=256:82242)
- Layer 37: `codeline`, `悬挂`, `挂`, `Quintal`, ` .` (target ranks: x_1=86:49179, x_2=70:95928, x_3=16:92435, x_4=256:119159)
- Layer 38: ` .`, `悬挂`, ` .↵↵`, `usk`, `静静` (target ranks: x_1=86:37193, x_2=70:89153, x_3=16:66414, x_4=256:113538)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `okens`, `悬挂` (target ranks: x_1=86:88463, x_2=70:93255, x_3=16:102725, x_4=256:110545)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` dots`, `dots` (target ranks: x_1=86:51229, x_2=70:48836, x_3=16:59370, x_4=256:70398)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `oooo`, ` ,` (target ranks: x_1=86:21630, x_2=70:21415, x_3=16:30491, x_4=256:31553)

### Filler position 9 (absolute token 456, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=86:123868, x_2=70:123268, x_3=16:125729, x_4=256:123237)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `挪` (target ranks: x_1=86:12861, x_2=70:13891, x_3=16:10233, x_4=256:22084)
- Layer 20: `洪荒`, ` covid`, `题的`, ` unconscious`, ` splash` (target ranks: x_1=86:33494, x_2=70:42193, x_3=16:41349, x_4=256:74614)
- Layer 30: ` Answer`, `}<?`, ` ответ`, `uze`, ` Antwort` (target ranks: x_1=86:100693, x_2=70:124770, x_3=16:120482, x_4=256:121804)
- Layer 35: ` Answer`, ` Antwort`, ` answer`, ` doub`, ` doubling` (target ranks: x_1=86:73892, x_2=70:109867, x_3=16:123380, x_4=256:112216)
- Layer 36: ` Answer`, ` reply`, ` answer`, ` پاسخ`, ` Reply` (target ranks: x_1=86:47602, x_2=70:72592, x_3=16:105555, x_4=256:89715)
- Layer 37: `oNames`, `�`, `心地`, `uze`, `-ulo` (target ranks: x_1=86:110736, x_2=70:119540, x_3=16:119894, x_4=256:117953)
- Layer 38: `oNames`, `聽`, `�`, `高等`, `►▼` (target ranks: x_1=86:99803, x_2=70:113765, x_3=16:121394, x_4=256:115338)
- Layer 39: ` .↵↵`, ` turtles`, `把事情`, ` Paglin`, `树叶` (target ranks: x_1=86:63144, x_2=70:64567, x_3=16:86080, x_4=256:81796)
- Layer 40: ` .↵↵`, ` .↵`, ` .`, ` Answer`, ` nasod` (target ranks: x_1=86:3472, x_2=70:4908, x_3=16:10053, x_4=256:14632)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, ` Answer`, `Answer` (target ranks: x_1=86:468, x_2=70:522, x_3=16:651, x_4=256:3093)

### Filler position 10 (absolute token 457, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `-ulo` (target ranks: x_1=86:119307, x_2=70:118705, x_3=16:121212, x_4=256:114451)
- Layer 10: `основним`, ` everydaycalculation`, `xjzy`, `eva`, ` Saysay` (target ranks: x_1=86:128415, x_2=70:128812, x_3=16:126717, x_4=256:110089)
- Layer 20: `Sequ`, `忑`, `ait`, `坷`, `答复` (target ranks: x_1=86:19123, x_2=70:33319, x_3=16:15129, x_4=256:38213)
- Layer 30: `答案`, ` answer`, `回答`, `答案是`, ` Answer` (target ranks: x_1=86:25717, x_2=70:79335, x_3=16:64039, x_4=256:32459)
- Layer 35: ` Answer`, `答案`, ` answer`, `答案是`, `Answer` (target ranks: x_1=86:16819, x_2=70:87236, x_3=16:54831, x_4=256:15555)
- Layer 36: ` answer`, ` Answer`, `答案`, `回答`, `Answer` (target ranks: x_1=86:8724, x_2=70:46873, x_3=16:14401, x_4=256:2029)
- Layer 37: ` Answer`, `答案`, ` answer`, `Answer`, `amina` (target ranks: x_1=86:22950, x_2=70:86686, x_3=16:32425, x_4=256:4618)
- Layer 38: ` Answer`, `Answer`, `答案`, ` answer`, ` ответ` (target ranks: x_1=86:31328, x_2=70:96114, x_3=16:57623, x_4=256:8698)
- Layer 39: ` Answer`, `Answer`, ` answer`, `答案`, `answer` (target ranks: x_1=86:19147, x_2=70:37831, x_3=16:63243, x_4=256:6578)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `答案` (target ranks: x_1=86:669, x_2=70:1182, x_3=16:7604, x_4=256:405)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `答` (target ranks: x_1=86:65, x_2=70:337, x_3=16:501, x_4=256:201)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given integers x, N, and T. Set x_0 = x mod N, then repeatedly apply x_t = x_(t-1)^2 mod N exactly T times. Answer immediately with just x_T as a base-10 integer, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be some filler tokens (a sequence of dots) to give you extra space to process the problem before answering.<｜User｜>Question: Starting with x_0 = 2 mod 55, repeatedly apply x_t = x_(t-1)^2 mod 55 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>36<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 3 mod 77, repeatedly apply x_t = x_(t-1)^2 mod 77 for exactly 4 steps. What is x_4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>25<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 5 mod 143, repeatedly apply x_t = x_(t-1)^2 mod 143 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>92<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 7 mod 221, repeatedly apply x_t = x_(t-1)^2 mod 221 for exactly 4 steps. What is x_4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>35<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 11 mod 247, repeatedly apply x_t = x_(t-1)^2 mod 247 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 30 mod 407, repeatedly apply x_t = x_(t-1)^2 mod 407 for exactly 4 steps. What is x_4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
