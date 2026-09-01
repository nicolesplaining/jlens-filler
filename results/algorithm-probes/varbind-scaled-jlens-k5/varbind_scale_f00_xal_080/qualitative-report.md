# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `367` (correct).
- No-filler answer: `383` (incorrect).
- Filler tokens: 5 tokens at absolute indices 576–580.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=80` | 1 (L23, filler 3) | L23, filler 3 (rank 1) |
| J-Lens | `first_product=160` | 58 (L29, filler 3) | Never |
| J-Lens | `bound_value=174` | 9 (L29, filler 3) | L29, filler 3 (rank 9) |
| J-Lens | `second_product=348` | 1 (L34, filler 5) | L31, filler 5 (rank 5) |
| J-Lens | `answer=367` | 1 (L38, filler 2) | L35, filler 2 (rank 10) |
| Logit lens | `base_value=80` | 35 (L26, filler 3) | Never |
| Logit lens | `first_product=160` | 106 (L29, filler 3) | Never |
| Logit lens | `bound_value=174` | 27 (L29, filler 5) | Never |
| Logit lens | `second_product=348` | 1 (L31, filler 5) | L31, filler 5 (rank 1) |
| Logit lens | `answer=367` | 3 (L36, filler 3) | L35, filler 3 (rank 7) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 576, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=80:119458, first_product=160:110801, bound_value=174:109250, second_product=348:111347, answer=367:108873)
- Layer 10: `anta`, `忑`, `Walker`, ` Walker`, `锁定` (target ranks: base_value=80:38660, first_product=160:42802, bound_value=174:48211, second_product=348:40204, answer=367:35384)
- Layer 20: `天平`, `足`, `垂`, `s`, `梯` (target ranks: base_value=80:1917, first_product=160:36900, bound_value=174:29723, second_product=348:45831, answer=367:5917)
- Layer 30: `回答`, `重复`, `期望`, ` talags`, `答复` (target ranks: base_value=80:27100, first_product=160:61974, bound_value=174:37139, second_product=348:77941, answer=367:29322)
- Layer 35: `重复`, `tap`, ` tap`, ` repetition`, ` calculator` (target ranks: base_value=80:10723, first_product=160:21905, bound_value=174:6169, second_product=348:32140, answer=367:22383)
- Layer 36: `期望`, `重复`, `期待`, `tap`, ` tap` (target ranks: base_value=80:14376, first_product=160:19292, bound_value=174:15972, second_product=348:30416, answer=367:32825)
- Layer 37: ` talags`, `步骤`, ` floating`, `计算`, `calcul` (target ranks: base_value=80:37419, first_product=160:21585, bound_value=174:25689, second_product=348:70252, answer=367:47112)
- Layer 38: ` talags`, ` floating`, `}<?`, `步骤`, `解答` (target ranks: base_value=80:45654, first_product=160:22290, bound_value=174:39279, second_product=348:84563, answer=367:59550)
- Layer 39: `一个一个`, ` talags`, `一个个`, `滴滴`, `个个` (target ranks: base_value=80:127758, first_product=160:127160, bound_value=174:120626, second_product=348:124957, answer=367:119035)
- Layer 40: `一个一个`, `oooo`, ` talags`, ` dotted`, ` dots` (target ranks: base_value=80:126175, first_product=160:125758, bound_value=174:113229, second_product=348:119361, answer=367:110907)
- Layer 41: ` .`, `一个一个`, ` .↵↵`, `一个个`, ` .↵` (target ranks: base_value=80:112631, first_product=160:103483, bound_value=174:65214, second_product=348:85030, answer=367:79422)

### Filler position 2 (absolute token 577, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: base_value=80:122274, first_product=160:116966, bound_value=174:113412, second_product=348:118062, answer=367:114962)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `挪` (target ranks: base_value=80:21314, first_product=160:31506, bound_value=174:41134, second_product=348:40231, answer=367:37237)
- Layer 20: ` .`, `s`, `各部分`, `sl`, ` repeating` (target ranks: base_value=80:2365, first_product=160:46346, bound_value=174:63652, second_product=348:72837, answer=367:45447)
- Layer 30: `Quintal`, `翻`, `翻了`, `LikeLike`, `翻转` (target ranks: base_value=80:37998, first_product=160:24419, bound_value=174:17091, second_product=348:22384, answer=367:26134)
- Layer 35: `349`, `347`, `348`, ` Labor`, ` labor` (target ranks: base_value=80:61878, first_product=160:78049, bound_value=174:20103, second_product=348:3, answer=367:10)
- Layer 36: `368`, `369`, `367`, `365`, `388` (target ranks: base_value=80:126354, first_product=160:59887, bound_value=174:81054, second_product=348:37, answer=367:3)
- Layer 37: `368`, `369`, `367`, `366`, `365` (target ranks: base_value=80:127664, first_product=160:61683, bound_value=174:90889, second_product=348:893, answer=367:3)
- Layer 38: `367`, `368`, `369`, `365`, `366` (target ranks: base_value=80:129167, first_product=160:123241, bound_value=174:125610, second_product=348:7152, answer=367:1)
- Layer 39: `367`, `}<?`, `leaf`, `本题分析`, `叶子` (target ranks: base_value=80:128117, first_product=160:127573, bound_value=174:129272, second_product=348:126455, answer=367:1)
- Layer 40: ` dots`, `acles`, `dots`, `dot`, ` dotted` (target ranks: base_value=80:128538, first_product=160:127570, bound_value=174:128762, second_product=348:128506, answer=367:1417)
- Layer 41: ` .`, ` dotted`, `日历`, ` nuest`, ` dots` (target ranks: base_value=80:125838, first_product=160:116533, bound_value=174:128484, second_product=348:124924, answer=367:1159)

### Filler position 3 (absolute token 578, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125838, first_product=160:121497, bound_value=174:116689, second_product=348:121453, answer=367:118931)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: base_value=80:16846, first_product=160:28746, bound_value=174:32338, second_product=348:30648, answer=367:30780)
- Layer 20: `能被`, `足`, `ait`, `auce`, `距` (target ranks: base_value=80:176, first_product=160:6788, bound_value=174:11442, second_product=348:12706, answer=367:5454)
- Layer 30: `Quintal`, `ocr`, `翻了`, ` decor`, `}<?` (target ranks: base_value=80:30645, first_product=160:3406, bound_value=174:1574, second_product=348:3711, answer=367:417)
- Layer 35: `349`, `347`, `348`, `359`, `368` (target ranks: base_value=80:69290, first_product=160:62014, bound_value=174:3288, second_product=348:3, answer=367:7)
- Layer 36: `368`, `369`, `383`, `367`, `363` (target ranks: base_value=80:122925, first_product=160:44989, bound_value=174:32613, second_product=348:36, answer=367:4)
- Layer 37: `368`, `-ulo`, `369`, `书馆`, `367` (target ranks: base_value=80:125907, first_product=160:49232, bound_value=174:44571, second_product=348:677, answer=367:5)
- Layer 38: `368`, `367`, `369`, `书馆`, `363` (target ranks: base_value=80:129081, first_product=160:120223, bound_value=174:109206, second_product=348:2863, answer=367:2)
- Layer 39: `}<?`, `ozygous`, `367`, `本题分析`, `ked` (target ranks: base_value=80:127906, first_product=160:126930, bound_value=174:128514, second_product=348:125790, answer=367:3)
- Layer 40: ` dots`, ` dotted`, `dots`, `dot`, ` rede` (target ranks: base_value=80:128198, first_product=160:125162, bound_value=174:128180, second_product=348:128336, answer=367:25001)
- Layer 41: ` .`, ` dots`, ` dotted`, ` waiting`, `dots` (target ranks: base_value=80:116848, first_product=160:97910, bound_value=174:122600, second_product=348:120780, answer=367:14421)

### Filler position 4 (absolute token 579, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:126724, first_product=160:123390, bound_value=174:118362, second_product=348:123301, answer=367:121244)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11775, first_product=160:22245, bound_value=174:27862, second_product=348:23934, answer=367:24267)
- Layer 20: ` Covid`, `oooo`, ` covid`, `…..`, ` horiz` (target ranks: base_value=80:43670, first_product=160:82835, bound_value=174:96380, second_product=348:89136, answer=367:66165)
- Layer 30: `codeline`, ` Answer`, `Quintal`, ` ответ`, `答案是` (target ranks: base_value=80:119307, first_product=160:115631, bound_value=174:118060, second_product=348:123371, answer=367:112295)
- Layer 35: `codeline`, `</think>`, `oNames`, `malink`, ` doubly` (target ranks: base_value=80:118862, first_product=160:120792, bound_value=174:117450, second_product=348:121769, answer=367:124229)
- Layer 36: `codeline`, `oNames`, `</think>`, ` doubly`, `理性的` (target ranks: base_value=80:93116, first_product=160:100419, bound_value=174:92158, second_product=348:100885, answer=367:117808)
- Layer 37: `codeline`, `oNames`, `}<?`, `?datasetId`, `/MODIS` (target ranks: base_value=80:117482, first_product=160:119104, bound_value=174:108657, second_product=348:107742, answer=367:124588)
- Layer 38: `oNames`, `codeline`, `?datasetId`, `}<?`, `/MODIS` (target ranks: base_value=80:108990, first_product=160:109980, bound_value=174:95447, second_product=348:97366, answer=367:123784)
- Layer 39: `}<?`, `?datasetId`, `lampi`, `oNames`, `codeline` (target ranks: base_value=80:118409, first_product=160:105907, bound_value=174:82404, second_product=348:77117, answer=367:88260)
- Layer 40: ` .`, ` .↵↵`, `</think>`, ` sesu`, ` dú` (target ranks: base_value=80:82023, first_product=160:62165, bound_value=174:35423, second_product=348:25709, answer=367:13800)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` begg`, ` too` (target ranks: base_value=80:42932, first_product=160:36924, bound_value=174:8768, second_product=348:21038, answer=367:5270)

### Filler position 5 (absolute token 580, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `-ulo`, `�乐` (target ranks: base_value=80:119450, first_product=160:110663, bound_value=174:108005, second_product=348:112293, answer=367:108877)
- Layer 10: `xjzy`, `anta`, ` kinain`, `忑`, `能吃` (target ranks: base_value=80:119986, first_product=160:61258, bound_value=174:110109, second_product=348:96675, answer=367:68765)
- Layer 20: ` Numerade`, `答案为`, `答案是`, `参考答案`, `答道` (target ranks: base_value=80:31953, first_product=160:46752, bound_value=174:101311, second_product=348:86717, answer=367:58436)
- Layer 30: `?datasetId`, `aplenty`, `nze`, `datasetId`, `udeau` (target ranks: base_value=80:108744, first_product=160:50888, bound_value=174:18318, second_product=348:22888, answer=367:62628)
- Layer 35: `348`, `349`, `347`, `346`, `368` (target ranks: base_value=80:121789, first_product=160:94456, bound_value=174:4943, second_product=348:1, answer=367:11)
- Layer 36: `368`, `361`, `348`, `362`, `363` (target ranks: base_value=80:129089, first_product=160:57636, bound_value=174:76482, second_product=348:3, answer=367:21)
- Layer 37: `368`, `361`, `362`, `348`, `363` (target ranks: base_value=80:128890, first_product=160:55692, bound_value=174:64696, second_product=348:4, answer=367:10)
- Layer 38: `362`, `363`, `361`, `368`, `373` (target ranks: base_value=80:129196, first_product=160:108848, bound_value=174:117075, second_product=348:25, answer=367:12)
- Layer 39: `362`, `363`, `361`, `369`, `371` (target ranks: base_value=80:128570, first_product=160:127069, bound_value=174:127846, second_product=348:95598, answer=367:16)
- Layer 40: ` Answer`, ` answer`, `Answer`, `(answer`, `_answer` (target ranks: base_value=80:128658, first_product=160:125984, bound_value=174:126133, second_product=348:114841, answer=367:5659)
- Layer 41: `Answer`, ` Answer`, `答案`, ` answer`, `답` (target ranks: base_value=80:110440, first_product=160:87166, bound_value=174:97525, second_product=348:73986, answer=367:3967)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zem = 14
yoh = twice the number for zem plus 27
xal = 80
puc = twice the number for xal plus 14
dof = twice the number for puc plus 26
Question: What is twice the number for puc plus 19?

Filler: . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
