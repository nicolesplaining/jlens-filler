# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `80` (correct).
- No-filler answer: `144` (incorrect).
- Filler tokens: 10 tokens at absolute indices 448–457.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `x_1=158` | 51 (L37, filler 3) | Never |
| J-Lens | `x_2=93` | 28 (L36, filler 3) | Never |
| J-Lens | `x_3=80` | 411 (L35, filler 3) | Never |
| Logit lens | `x_1=158` | 61 (L38, filler 3) | Never |
| Logit lens | `x_2=93` | 67 (L37, filler 3) | Never |
| Logit lens | `x_3=80` | 148 (L37, filler 3) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 448, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `?datasetId` (target ranks: x_1=158:106987, x_2=93:119593, x_3=80:118627)
- Layer 10: `Walker`, ` Walker`, `锁定`, `cape`, `勾` (target ranks: x_1=158:33240, x_2=93:19195, x_3=80:23638)
- Layer 20: `甸`, `表面`, `旬`, `足`, `垂` (target ranks: x_1=158:22172, x_2=93:2773, x_3=80:1254)
- Layer 30: ` repetitions`, `重复`, ` repetition`, ` pattern`, `提问` (target ranks: x_1=158:62130, x_2=93:51171, x_3=80:66595)
- Layer 35: ` questions`, `重复`, ` repetitions`, `询问`, ` repetition` (target ranks: x_1=158:58477, x_2=93:37947, x_3=80:32189)
- Layer 36: `重复`, `询问`, `期望`, ` pattern`, ` tap` (target ranks: x_1=158:35133, x_2=93:28096, x_3=80:33538)
- Layer 37: ` pattern`, `pattern`, ` Pattern`, ` patterns`, `Pattern` (target ranks: x_1=158:56116, x_2=93:89066, x_3=80:75380)
- Layer 38: ` pattern`, ` prompt`, `模仿`, ` tra`, `期望` (target ranks: x_1=158:67527, x_2=93:96076, x_3=80:75048)
- Layer 39: `olat`, `�`, `osz`, ` tra`, `花朵` (target ranks: x_1=158:124994, x_2=93:128128, x_3=80:110081)
- Layer 40: ` filler`, ` talags`, `oooo`, ` dots`, ` dotted` (target ranks: x_1=158:107200, x_2=93:120520, x_3=80:89034)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` done` (target ranks: x_1=158:76138, x_2=93:89957, x_3=80:85542)

### Filler position 2 (absolute token 449, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: x_1=158:114921, x_2=93:121311, x_3=80:122421)
- Layer 10: ` Walker`, `从哪里`, `Walker`, `忑`, `atile` (target ranks: x_1=158:50375, x_2=93:29530, x_3=80:31264)
- Layer 20: ` .`, ` Procedure`, `外向`, ` distant`, ` .↵↵` (target ranks: x_1=158:93774, x_2=93:89324, x_3=80:22880)
- Layer 30: ` .`, `oooo`, `ilig`, `期待的`, `翻` (target ranks: x_1=158:64968, x_2=93:119122, x_3=80:89278)
- Layer 35: ` .`, `ilig`, `拖延`, `cult`, `私` (target ranks: x_1=158:106084, x_2=93:117188, x_3=80:75931)
- Layer 36: `odor`, ` .`, `cult`, `停`, `私` (target ranks: x_1=158:59555, x_2=93:88729, x_3=80:50456)
- Layer 37: `}<?`, ` Erkännande`, `enclose`, ` .`, `殿堂` (target ranks: x_1=158:91677, x_2=93:124491, x_3=80:100505)
- Layer 38: ` .`, ` .↵↵`, ` .↵`, ` nasod`, `enclose` (target ranks: x_1=158:102918, x_2=93:122302, x_3=80:84609)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>`, ` .----` (target ranks: x_1=158:98988, x_2=93:124281, x_3=80:94301)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` filler` (target ranks: x_1=158:47777, x_2=93:108887, x_3=80:65488)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` ↵` (target ranks: x_1=158:23989, x_2=93:66963, x_3=80:48062)

### Filler position 3 (absolute token 450, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:118332, x_2=93:123289, x_3=80:125885)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: x_1=158:30307, x_2=93:10788, x_3=80:15248)
- Layer 20: `ait`, `�`, ` ternary`, `足`, `s` (target ranks: x_1=158:20380, x_2=93:1335, x_3=80:2997)
- Layer 30: `s`, `容易出现`, `容易被`, `eas`, `aug` (target ranks: x_1=158:753, x_2=93:264, x_3=80:7230)
- Layer 35: `144`, `86`, `96`, ` compute`, `224` (target ranks: x_1=158:387, x_2=93:34, x_3=80:411)
- Layer 36: `86`, `calcul`, ` Wil`, `aho`, `obin` (target ranks: x_1=158:86, x_2=93:28, x_3=80:479)
- Layer 37: `ocyst`, `}<?`, `144`, `155`, `164` (target ranks: x_1=158:51, x_2=93:190, x_3=80:1850)
- Layer 38: `}<?`, `ocyst`, ` Naz`, `-ulo`, `本题分析` (target ranks: x_1=158:577, x_2=93:2635, x_3=80:7607)
- Layer 39: `}<?`, `ologists`, `个好`, `ocyst`, ` dekameters` (target ranks: x_1=158:6329, x_2=93:35694, x_3=80:23813)
- Layer 40: ` drip`, ` `, ` butt`, ` .`, ` dekameters` (target ranks: x_1=158:1767, x_2=93:21815, x_3=80:15058)
- Layer 41: ` .`, `人人都`, ` because`, ` without`, ` dekameters` (target ranks: x_1=158:4791, x_2=93:29742, x_3=80:38761)

### Filler position 4 (absolute token 451, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:119545, x_2=93:123651, x_3=80:126461)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: x_1=158:30926, x_2=93:12221, x_3=80:16227)
- Layer 20: `足`, `ait`, `cape`, `幽`, `atile` (target ranks: x_1=158:22068, x_2=93:5056, x_3=80:3873)
- Layer 30: `024`, `保留`, `24`, `二十四`, ` expecting` (target ranks: x_1=158:15727, x_2=93:14478, x_3=80:65731)
- Layer 35: `576`, `585`, `574`, `586`, `578` (target ranks: x_1=158:2204, x_2=93:932, x_3=80:10483)
- Layer 36: `576`, `585`, `586`, `574`, `578` (target ranks: x_1=158:3063, x_2=93:10717, x_3=80:21912)
- Layer 37: `576`, `585`, `586`, `574`, `578` (target ranks: x_1=158:6295, x_2=93:32756, x_3=80:22525)
- Layer 38: `576`, `585`, `586`, `577`, `574` (target ranks: x_1=158:9407, x_2=93:33721, x_3=80:17234)
- Layer 39: `576`, ` Halle`, `�`, `Pent`, `lut` (target ranks: x_1=158:81237, x_2=93:109060, x_3=80:57753)
- Layer 40: ` uninter`, `叮`, `ald`, `chet`, `house` (target ranks: x_1=158:78520, x_2=93:109495, x_3=80:60838)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `试一试`, ` fruit` (target ranks: x_1=158:45280, x_2=93:84803, x_3=80:49927)

### Filler position 5 (absolute token 452, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: x_1=158:119859, x_2=93:123650, x_3=80:126321)
- Layer 10: ` Walker`, `Walker`, `锁定`, `挪`, `ait` (target ranks: x_1=158:35178, x_2=93:16560, x_3=80:19669)
- Layer 20: `鞍`, `幽`, `忑`, `锁定`, `足` (target ranks: x_1=158:29195, x_2=93:20661, x_3=80:15656)
- Layer 30: `一步步`, `第一步`, `步步`, `反复`, `每一步` (target ranks: x_1=158:29923, x_2=93:59984, x_3=80:41670)
- Layer 35: ` Step`, ` step`, `步骤`, `第一步`, `Step` (target ranks: x_1=158:45443, x_2=93:68100, x_3=80:47933)
- Layer 36: ` Step`, `步骤`, ` step`, `第一步`, ` steps` (target ranks: x_1=158:29679, x_2=93:75641, x_3=80:62736)
- Layer 37: ` Step`, ` step`, `步骤`, ` Steps`, `Step` (target ranks: x_1=158:50759, x_2=93:112856, x_3=80:91773)
- Layer 38: ` Step`, ` step`, `步骤`, `-step`, `-Step` (target ranks: x_1=158:58842, x_2=93:113673, x_3=80:96465)
- Layer 39: ` Step`, `覆`, `步步`, `hemer`, `}<?` (target ranks: x_1=158:113102, x_2=93:128117, x_3=80:116021)
- Layer 40: ` Step`, `坏`, `覆`, ` step`, `hemer` (target ranks: x_1=158:89238, x_2=93:123688, x_3=80:107480)
- Layer 41: ` .`, `滴`, ` .↵↵`, `坏`, ` ` (target ranks: x_1=158:37530, x_2=93:102225, x_3=80:83778)

### Filler position 6 (absolute token 453, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:119115, x_2=93:123612, x_3=80:125883)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=158:30187, x_2=93:12075, x_3=80:16176)
- Layer 20: `鞍`, `锁定`, `cape`, `挪`, `足` (target ranks: x_1=158:16974, x_2=93:5842, x_3=80:4413)
- Layer 30: `步骤`, `下沉`, `保留`, ` basal`, ` tail` (target ranks: x_1=158:2049, x_2=93:3364, x_3=80:4914)
- Layer 35: `保留`, ` repetition`, `容易出现`, ` Propri`, ` waterfall` (target ranks: x_1=158:1105, x_2=93:1122, x_3=80:997)
- Layer 36: `保留`, `肩`, `留存`, `irie`, `容易出现` (target ranks: x_1=158:411, x_2=93:1246, x_3=80:1435)
- Layer 37: `osine`, `oNames`, `ocyst`, `悬挂`, `referent` (target ranks: x_1=158:1088, x_2=93:16208, x_3=80:11211)
- Layer 38: `osine`, `}<?`, `ocyst`, `oNames`, `本题分析` (target ranks: x_1=158:8768, x_2=93:37507, x_3=80:33074)
- Layer 39: `叶子`, `ocyst`, `}<?`, `oNames`, `一个个` (target ranks: x_1=158:39555, x_2=93:106323, x_3=80:65586)
- Layer 40: ` talags`, `试一试`, ` dots`, `留存`, ` .` (target ranks: x_1=158:15878, x_2=93:76784, x_3=80:30594)
- Layer 41: ` .`, ` .↵↵`, `试一试`, ` waiting`, `一个个` (target ranks: x_1=158:8124, x_2=93:45976, x_3=80:31523)

### Filler position 7 (absolute token 454, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:119430, x_2=93:123632, x_3=80:125831)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: x_1=158:30287, x_2=93:12705, x_3=80:16166)
- Layer 20: `锁定`, `鞍`, ` smile`, `忑`, ` Walker` (target ranks: x_1=158:22523, x_2=93:12260, x_3=80:8943)
- Layer 30: ` step`, ` Step`, `步骤`, `一步步`, `第一步` (target ranks: x_1=158:50063, x_2=93:53224, x_3=80:15624)
- Layer 35: ` step`, ` Step`, `步骤`, `Step`, `step` (target ranks: x_1=158:37100, x_2=93:31732, x_3=80:4828)
- Layer 36: ` step`, ` Step`, `步骤`, `Step`, `step` (target ranks: x_1=158:29885, x_2=93:55859, x_3=80:14064)
- Layer 37: ` Step`, ` step`, `步骤`, `Step`, `-step` (target ranks: x_1=158:56050, x_2=93:107721, x_3=80:52677)
- Layer 38: ` Step`, ` step`, `-step`, `步骤`, ` Steps` (target ranks: x_1=158:71570, x_2=93:110670, x_3=80:64396)
- Layer 39: `}<?`, ` Step`, `hemer`, `一个好`, `个好` (target ranks: x_1=158:100908, x_2=93:126935, x_3=80:97462)
- Layer 40: ` Step`, `留存`, `一个个`, `二十四`, ` tap` (target ranks: x_1=158:77576, x_2=93:122066, x_3=80:82943)
- Layer 41: ` .`, ` .↵↵`, `一个个`, `一个好`, `二十四` (target ranks: x_1=158:33981, x_2=93:101112, x_3=80:66215)

### Filler position 8 (absolute token 455, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:119085, x_2=93:123553, x_3=80:125564)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=158:28646, x_2=93:11538, x_3=80:14645)
- Layer 20: ` smile`, `ait`, ` Walker`, ` quadr`, `锁定` (target ranks: x_1=158:22237, x_2=93:16845, x_3=80:8395)
- Layer 30: `dividers`, `codeline`, ` spac`, `东京`, ` Cosm` (target ranks: x_1=158:112740, x_2=93:114052, x_3=80:120836)
- Layer 35: ` .`, `川`, ` soci`, ` press`, ` Soci` (target ranks: x_1=158:111045, x_2=93:115896, x_3=80:110495)
- Layer 36: `重复`, `odor`, ` soci`, `川`, ` Soci` (target ranks: x_1=158:82421, x_2=93:82360, x_3=80:74055)
- Layer 37: `悬挂`, `codeline`, `东京`, `挂`, ` .` (target ranks: x_1=158:95578, x_2=93:112805, x_3=80:110275)
- Layer 38: ` .`, `悬挂`, ` .↵↵`, `usk`, `悬` (target ranks: x_1=158:87173, x_2=93:107478, x_3=80:107515)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, ` Harm`, `悬挂` (target ranks: x_1=158:89437, x_2=93:115795, x_3=80:111034)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `dots`, `ooo` (target ranks: x_1=158:52788, x_2=93:95147, x_3=80:93048)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `ldots` (target ranks: x_1=158:6958, x_2=93:31178, x_3=80:46241)

### Filler position 9 (absolute token 456, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=158:119443, x_2=93:123512, x_3=80:125657)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `挪` (target ranks: x_1=158:28304, x_2=93:11034, x_3=80:13484)
- Layer 20: `洪荒`, ` covid`, ` unconscious`, ` splash`, `ๆ` (target ranks: x_1=158:42117, x_2=93:28463, x_3=80:38488)
- Layer 30: ` Answer`, ` ответ`, `}<?`, ` Antwort`, `答案是` (target ranks: x_1=158:95254, x_2=93:84218, x_3=80:127126)
- Layer 35: ` Answer`, ` Antwort`, ` Reply`, ` answer`, ` reply` (target ranks: x_1=158:103922, x_2=93:69085, x_3=80:115166)
- Layer 36: ` Answer`, ` reply`, ` Reply`, ` پاسخ`, ` answer` (target ranks: x_1=158:97918, x_2=93:38780, x_3=80:95491)
- Layer 37: `�`, `�`, ` Didži`, `心地`, `/MODIS` (target ranks: x_1=158:119072, x_2=93:103886, x_3=80:122856)
- Layer 38: `聽`, `叶子`, `洪荒`, `oNames`, `�` (target ranks: x_1=158:120206, x_2=93:99873, x_3=80:118675)
- Layer 39: ` .↵↵`, `树叶`, `叶子`, `膜的`, ` turtles` (target ranks: x_1=158:70259, x_2=93:94416, x_3=80:98115)
- Layer 40: ` .↵↵`, ` .↵`, ` .`, ` Answer`, ` nasod` (target ranks: x_1=158:10429, x_2=93:24675, x_3=80:22405)
- Layer 41: ` .↵↵`, ` .↵`, ` .`, `叮`, `Answer` (target ranks: x_1=158:3203, x_2=93:1450, x_3=80:4727)

### Filler position 10 (absolute token 457, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `-ulo` (target ranks: x_1=158:106628, x_2=93:120658, x_3=80:119359)
- Layer 10: `основним`, ` everydaycalculation`, `xjzy`, `eva`, `som` (target ranks: x_1=158:100587, x_2=93:127781, x_3=80:128510)
- Layer 20: `Sequ`, `ait`, `忑`, `批复`, `坷` (target ranks: x_1=158:57571, x_2=93:16109, x_3=80:33564)
- Layer 30: `答案`, `回答`, ` answer`, `答案为`, ` Answer` (target ranks: x_1=158:97670, x_2=93:25317, x_3=80:106063)
- Layer 35: ` Answer`, ` answer`, `答案`, `答案是`, `回答` (target ranks: x_1=158:86611, x_2=93:21671, x_3=80:73467)
- Layer 36: ` answer`, `回答`, `答案`, ` Answer`, `Answer` (target ranks: x_1=158:56094, x_2=93:15208, x_3=80:34676)
- Layer 37: `答案`, ` Answer`, `amina`, ` answer`, ` Paglin` (target ranks: x_1=158:72161, x_2=93:53720, x_3=80:54749)
- Layer 38: ` Answer`, `Answer`, `答案`, ` answer`, `answer` (target ranks: x_1=158:78128, x_2=93:72272, x_3=80:85014)
- Layer 39: `Answer`, ` Answer`, `答案`, ` answer`, `answer` (target ranks: x_1=158:57959, x_2=93:34535, x_3=80:40764)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `答案` (target ranks: x_1=158:8220, x_2=93:2278, x_3=80:3733)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: x_1=158:1490, x_2=93:469, x_3=80:1018)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 24 mod 209, repeatedly apply x_t = x_(t-1)^2 mod 209 for exactly 3 steps. What is x_3?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
