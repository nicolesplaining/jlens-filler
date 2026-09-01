# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `235` (correct).
- No-filler answer: `229` (incorrect).
- Filler tokens: 5 tokens at absolute indices 567–571.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=64` | 1122 (L25, filler 5) | Never |
| J-Lens | `first_product=128` | 16336 (L17, filler 5) | Never |
| J-Lens | `bound_value=125` | 2971 (L34, filler 2) | Never |
| J-Lens | `second_product=250` | 697 (L34, filler 2) | Never |
| J-Lens | `answer=235` | 1 (L36, filler 2) | L35, filler 2 (rank 4) |
| Logit lens | `base_value=64` | 101 (L25, filler 5) | Never |
| Logit lens | `first_product=128` | 193 (L3, filler 1) | Never |
| Logit lens | `bound_value=125` | 1371 (L2, filler 1) | Never |
| Logit lens | `second_product=250` | 988 (L35, filler 5) | Never |
| Logit lens | `answer=235` | 8 (L37, filler 2) | L37, filler 2 (rank 8) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 567, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=64:119359, first_product=128:114143, bound_value=125:112312, second_product=250:116968, answer=235:115046)
- Layer 10: `anta`, `Walker`, ` Walker`, `忑`, `fine` (target ranks: base_value=64:42791, first_product=128:40893, bound_value=125:43136, second_product=250:36744, answer=235:49271)
- Layer 20: `足`, `扣`, `甸`, `梯`, `cape` (target ranks: base_value=64:2033, first_product=128:37203, bound_value=125:27791, second_product=250:41116, answer=235:53136)
- Layer 30: ` Kur`, ` kur`, `kur`, `计算`, `计算的` (target ranks: base_value=64:2563, first_product=128:77873, bound_value=125:74239, second_product=250:79645, answer=235:98191)
- Layer 35: ` Kur`, ` kur`, `kur`, `cur`, ` Kaw` (target ranks: base_value=64:1380, first_product=128:63011, bound_value=125:52529, second_product=250:45952, answer=235:70540)
- Layer 36: ` Kur`, ` kur`, `kur`, `cur`, ` Kaw` (target ranks: base_value=64:2174, first_product=128:38716, bound_value=125:45600, second_product=250:42818, answer=235:74566)
- Layer 37: ` Kur`, ` kur`, `kur`, `cur`, `计算` (target ranks: base_value=64:5231, first_product=128:69905, bound_value=125:79543, second_product=250:86794, answer=235:111049)
- Layer 38: ` Kur`, ` kur`, `kur`, `cur`, ` cur` (target ranks: base_value=64:11128, first_product=128:99609, bound_value=125:88539, second_product=250:87373, answer=235:114542)
- Layer 39: ` Kur`, ` kur`, `本题分析`, ` talags`, `}<?` (target ranks: base_value=64:113322, first_product=128:127198, bound_value=125:68574, second_product=250:95431, answer=235:107875)
- Layer 40: `oooo`, ` kur`, ` talags`, `pon`, `有声` (target ranks: base_value=64:72916, first_product=128:117739, bound_value=125:19561, second_product=250:47821, answer=235:66075)
- Layer 41: ` .`, ` .↵↵`, `oooo`, ` kur`, ` .↵` (target ranks: base_value=64:56780, first_product=128:103863, bound_value=125:15562, second_product=250:14394, answer=235:32016)

### Filler position 2 (absolute token 568, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=64:121911, first_product=128:118904, bound_value=125:118170, second_product=250:121207, answer=235:119409)
- Layer 10: ` Walker`, `Walker`, `ait`, `挪`, `从哪里` (target ranks: base_value=64:22158, first_product=128:38299, bound_value=125:37409, second_product=250:32795, answer=235:37063)
- Layer 20: ` .`, `之夜`, `各部分`, ` Procedure`, ` repeating` (target ranks: base_value=64:3953, first_product=128:70613, bound_value=125:66079, second_product=250:82578, answer=235:67015)
- Layer 30: `翻`, `Quintal`, `翻转`, `翻了`, `反向` (target ranks: base_value=64:29924, first_product=128:94811, bound_value=125:43698, second_product=250:57574, answer=235:10426)
- Layer 35: `翻`, `松松`, `otan`, `235`, ` torn` (target ranks: base_value=64:60451, first_product=128:107174, bound_value=125:18518, second_product=250:906, answer=235:4)
- Layer 36: `235`, `233`, ` talags`, `�`, ` kahaboga` (target ranks: base_value=64:108790, first_product=128:106773, bound_value=125:49203, second_product=250:9939, answer=235:1)
- Layer 37: `?datasetId`, `235`, `}<?`, `tanle`, `cault` (target ranks: base_value=64:125249, first_product=128:112062, bound_value=125:35110, second_product=250:18106, answer=235:2)
- Layer 38: `235`, `tanle`, `三十五`, `本题分析`, ` talags` (target ranks: base_value=64:129264, first_product=128:128127, bound_value=125:89479, second_product=250:54756, answer=235:1)
- Layer 39: `235`, `本题分析`, `otan`, `tanle`, `zat` (target ranks: base_value=64:128536, first_product=128:128692, bound_value=125:125178, second_product=250:121845, answer=235:1)
- Layer 40: `otan`, ` dots`, `oba`, `dots`, ` mosunod` (target ranks: base_value=64:128015, first_product=128:128468, bound_value=125:115863, second_product=250:98147, answer=235:151)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` nuest`, ` ,` (target ranks: base_value=64:113283, first_product=128:123201, bound_value=125:74133, second_product=250:46869, answer=235:50)

### Filler position 3 (absolute token 569, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125592, first_product=128:121351, bound_value=125:121027, second_product=250:123658, answer=235:121716)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:16914, first_product=128:26946, bound_value=125:28472, second_product=250:25868, answer=235:26177)
- Layer 20: `�`, `�`, `会成为`, `s`, ` labeled` (target ranks: base_value=64:18262, first_product=128:89780, bound_value=125:53894, second_product=250:99905, answer=235:75746)
- Layer 30: ` Kur`, ` kur`, `kur`, `Quintal`, `替换` (target ranks: base_value=64:22495, first_product=128:124056, bound_value=125:115337, second_product=250:122367, answer=235:125946)
- Layer 35: ` Kur`, ` kur`, `kur`, `otan`, `кур` (target ranks: base_value=64:6952, first_product=128:121773, bound_value=125:106851, second_product=250:111772, answer=235:123177)
- Layer 36: ` Kur`, ` kur`, `kur`, `otan`, `pek` (target ranks: base_value=64:9386, first_product=128:100571, bound_value=125:91619, second_product=250:93797, answer=235:111469)
- Layer 37: `Quintal`, ` kur`, ` Kur`, `pek`, `otan` (target ranks: base_value=64:47787, first_product=128:111330, bound_value=125:106065, second_product=250:115282, answer=235:118632)
- Layer 38: `?datasetId`, `本题分析`, `}<?`, `医科`, `Quintal` (target ranks: base_value=64:62393, first_product=128:119002, bound_value=125:112497, second_product=250:115077, answer=235:118959)
- Layer 39: `本题分析`, `}<?`, `?datasetId`, `-ulo`, `替换` (target ranks: base_value=64:123087, first_product=128:127858, bound_value=125:99438, second_product=250:104595, answer=235:110566)
- Layer 40: ` .`, `声响`, ` beads`, `试一试`, ` dotted` (target ranks: base_value=64:114301, first_product=128:126045, bound_value=125:54067, second_product=250:70278, answer=235:62489)
- Layer 41: ` .`, ` .↵↵`, `片刻`, ` ,`, ` .↵` (target ranks: base_value=64:57576, first_product=128:105888, bound_value=125:16594, second_product=250:14515, answer=235:25582)

### Filler position 4 (absolute token 570, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:126501, first_product=128:123303, bound_value=125:123014, second_product=250:124843, answer=235:123440)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12163, first_product=128:23821, bound_value=125:23957, second_product=250:20278, answer=235:22232)
- Layer 20: ` quadr`, `oooo`, ` Covid`, `之夜`, `梯` (target ranks: base_value=64:6402, first_product=128:82942, bound_value=125:84150, second_product=250:85426, answer=235:57926)
- Layer 30: ` Answer`, ` ответ`, ` ANSWER`, `答案是`, `codeline` (target ranks: base_value=64:111634, first_product=128:117389, bound_value=125:123514, second_product=250:116938, answer=235:119899)
- Layer 35: ` Answer`, `codeline`, `</think>`, `malink`, `理性的` (target ranks: base_value=64:120910, first_product=128:125656, bound_value=125:125448, second_product=250:110071, answer=235:126891)
- Layer 36: ` Answer`, `</think>`, `理性的`, `冻结`, ` cog` (target ranks: base_value=64:90380, first_product=128:109023, bound_value=125:114555, second_product=250:92146, answer=235:125041)
- Layer 37: `codeline`, `?datasetId`, `oNames`, ` cryptocur`, ` dú` (target ranks: base_value=64:119186, first_product=128:117412, bound_value=125:123482, second_product=250:117032, answer=235:124706)
- Layer 38: ` dú`, `codeline`, `oNames`, `</think>`, `lampi` (target ranks: base_value=64:120988, first_product=128:113547, bound_value=125:118847, second_product=250:107206, answer=235:120699)
- Layer 39: `lampi`, `}<?`, `?datasetId`, `本题分析`, ` dú` (target ranks: base_value=64:104066, first_product=128:102943, bound_value=125:105074, second_product=250:79787, answer=235:91671)
- Layer 40: ` .↵↵`, ` .`, ` .↵`, ` dú`, `</think>` (target ranks: base_value=64:38144, first_product=128:67949, bound_value=125:53751, second_product=250:26226, answer=235:21338)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, ` thought`, ` too` (target ranks: base_value=64:10821, first_product=128:32666, bound_value=125:15741, second_product=250:5165, answer=235:3825)

### Filler position 5 (absolute token 571, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `-ulo`, `�乐` (target ranks: base_value=64:120869, first_product=128:114110, bound_value=125:111871, second_product=250:114727, answer=235:113928)
- Layer 10: `xjzy`, ` kinain`, `anta`, `основним`, `<｜begin▁of▁file｜>` (target ranks: base_value=64:127128, first_product=128:105605, bound_value=125:85380, second_product=250:81647, answer=235:95823)
- Layer 20: ` reluct`, `答案为`, ` dekameters`, ` Numerade`, `答案是` (target ranks: base_value=64:107258, first_product=128:122426, bound_value=125:124360, second_product=250:125093, answer=235:126888)
- Layer 30: ` Paglin`, ` giiniton`, ` রয়`, ` Fuchs`, ` Jew` (target ranks: base_value=64:83756, first_product=128:92223, bound_value=125:71495, second_product=250:110644, answer=235:116033)
- Layer 35: ` ninete`, ` المطلع`, `无忧`, `190`, ` Nineteenth` (target ranks: base_value=64:122683, first_product=128:128846, bound_value=125:81694, second_product=250:5654, answer=235:2910)
- Layer 36: ` Nineteenth`, ` ninete`, `北海`, `igesimal`, ` giiniton` (target ranks: base_value=64:120092, first_product=128:127585, bound_value=125:71748, second_product=250:10398, answer=235:2038)
- Layer 37: `oraly`, `TreeLabel`, `white`, `北海`, ` medief` (target ranks: base_value=64:126052, first_product=128:127875, bound_value=125:56997, second_product=250:11346, answer=235:4930)
- Layer 38: ` hilabihan`, `aplenty`, `}<?`, `white`, ` sumala` (target ranks: base_value=64:128448, first_product=128:128380, bound_value=125:63692, second_product=250:16573, answer=235:529)
- Layer 39: `interpret`, `anker`, `二百`, ` Thom`, `北海` (target ranks: base_value=64:128380, first_product=128:128393, bound_value=125:60446, second_product=250:48475, answer=235:183)
- Layer 40: ` Answer`, `Answer`, ` answer`, `答案`, ` answers` (target ranks: base_value=64:127298, first_product=128:126288, bound_value=125:21346, second_product=250:7286, answer=235:21)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=64:90846, first_product=128:108831, bound_value=125:7361, second_product=250:1149, answer=235:68)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 5 filler tokens (a sequence of dots) before you answer.<｜User｜>zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . .

Answer:<｜Assistant｜></think>176<｜end▁of▁sentence｜><｜User｜>cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . .

Answer:<｜Assistant｜></think>59<｜end▁of▁sentence｜><｜User｜>gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . .

Answer:<｜Assistant｜></think>351<｜end▁of▁sentence｜><｜User｜>mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . .

Answer:<｜Assistant｜></think>229<｜end▁of▁sentence｜><｜User｜>kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>qin = 67
xag = 23
kur = 64
rek = twice the number for kur minus 28
xav = twice the number for kur minus 3
Question: What is twice the number for xav minus 15?

Filler: . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
