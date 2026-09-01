# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `324` (incorrect).
- No-filler answer: `322` (incorrect).
- Filler tokens: 5 tokens at absolute indices 576–580.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=97` | 17 (L24, filler 5) | Never |
| J-Lens | `first_product=194` | 1939 (L31, filler 1) | Never |
| J-Lens | `bound_value=173` | 48 (L29, filler 5) | Never |
| J-Lens | `second_product=346` | 1 (L35, filler 5) | L35, filler 5 (rank 1) |
| J-Lens | `answer=374` | 89 (L38, filler 1) | Never |
| Logit lens | `base_value=97` | 5 (L24, filler 5) | L24, filler 5 (rank 5) |
| Logit lens | `first_product=194` | 206 (L32, filler 1) | Never |
| Logit lens | `bound_value=173` | 73 (L29, filler 5) | Never |
| Logit lens | `second_product=346` | 1 (L35, filler 5) | L35, filler 5 (rank 1) |
| Logit lens | `answer=374` | 152 (L38, filler 1) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 576, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=97:117849, first_product=194:111214, bound_value=173:113378, second_product=346:112597, answer=374:112722)
- Layer 10: `anta`, `Walker`, ` Walker`, `忑`, `锁定` (target ranks: base_value=97:36945, first_product=194:41535, bound_value=173:41568, second_product=346:30062, answer=374:38811)
- Layer 20: `足`, `甸`, `扣`, `旬`, `天平` (target ranks: base_value=97:6850, first_product=194:21697, bound_value=173:13533, second_product=346:5705, answer=374:8687)
- Layer 30: `calcul`, `计算`, ` talags`, `计算的`, ` calculator` (target ranks: base_value=97:3893, first_product=194:3295, bound_value=173:5845, second_product=346:3267, answer=374:2022)
- Layer 35: `68`, `期望`, ` calculator`, `扣`, `282` (target ranks: base_value=97:2595, first_product=194:2112, bound_value=173:2631, second_product=346:118, answer=374:927)
- Layer 36: `期望`, ` volta`, `期待`, `68`, `364` (target ranks: base_value=97:13046, first_product=194:5179, bound_value=173:9162, second_product=346:109, answer=374:689)
- Layer 37: `328`, `372`, `364`, `pload`, `282` (target ranks: base_value=97:79327, first_product=194:20737, bound_value=173:14189, second_product=346:82, answer=374:242)
- Layer 38: `328`, `364`, `308`, `372`, `306` (target ranks: base_value=97:118599, first_product=194:30984, bound_value=173:42878, second_product=346:27, answer=374:89)
- Layer 39: `三百`, `-ulo`, `殿堂`, `-ulan`, `oplankton` (target ranks: base_value=97:128754, first_product=194:128272, bound_value=173:123217, second_product=346:721, answer=374:11465)
- Layer 40: ` Ald`, ` ald`, `Ald`, ` ld`, ` alde` (target ranks: base_value=97:128694, first_product=194:128646, bound_value=173:124813, second_product=346:781, answer=374:28480)
- Layer 41: ` .`, ` .↵↵`, `一个一个`, `٫`, `庭审` (target ranks: base_value=97:127871, first_product=194:122784, bound_value=173:109788, second_product=346:36563, answer=374:51351)

### Filler position 2 (absolute token 577, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: base_value=97:119726, first_product=194:114135, bound_value=173:116942, second_product=346:118449, answer=374:117328)
- Layer 10: ` Walker`, `Walker`, `ait`, `挪`, `从哪里` (target ranks: base_value=97:27307, first_product=194:32022, bound_value=173:39061, second_product=346:29064, answer=374:36614)
- Layer 20: ` .`, `憬`, `之夜`, `s`, `sled` (target ranks: base_value=97:83695, first_product=194:60045, bound_value=173:95694, second_product=346:28650, answer=374:87103)
- Layer 30: `Quintal`, `翻`, `翻转`, `ools`, `?datasetId` (target ranks: base_value=97:103379, first_product=194:48926, bound_value=173:54499, second_product=346:34613, answer=374:63641)
- Layer 35: `翻`, ` soci`, `漂`, ` Soci`, `三百` (target ranks: base_value=97:114398, first_product=194:23889, bound_value=173:94930, second_product=346:14, answer=374:4548)
- Layer 36: `三百`, `第三百`, `收割`, ` extrac`, `322` (target ranks: base_value=97:127930, first_product=194:105454, bound_value=173:89564, second_product=346:155, answer=374:147)
- Layer 37: `?datasetId`, ` hydrodynamic`, `三百`, `第三百`, ` extrac` (target ranks: base_value=97:128625, first_product=194:117551, bound_value=173:107437, second_product=346:2895, answer=374:1212)
- Layer 38: ` hydrodynamic`, `三百`, `第三百`, `}<?`, `?datasetId` (target ranks: base_value=97:128734, first_product=194:123510, bound_value=173:116813, second_product=346:1296, answer=374:389)
- Layer 39: `}<?`, ` Erl`, ` hydrodynamic`, `叶子`, `三百` (target ranks: base_value=97:128525, first_product=194:126094, bound_value=173:128278, second_product=346:52032, answer=374:11511)
- Layer 40: ` talags`, ` ald`, `inea`, `收割`, ` ld` (target ranks: base_value=97:128370, first_product=194:126785, bound_value=173:124748, second_product=346:45705, answer=374:34440)
- Layer 41: ` .`, ` .↵↵`, ` nuest`, ` .↵`, `.,` (target ranks: base_value=97:127085, first_product=194:109433, bound_value=173:105051, second_product=346:76219, answer=374:26787)

### Filler position 3 (absolute token 578, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123492, first_product=194:116564, bound_value=173:118705, second_product=346:121878, answer=374:120796)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: base_value=97:17133, first_product=194:28113, bound_value=173:29205, second_product=346:25904, answer=374:30728)
- Layer 20: `�`, `�`, ` stitching`, `Cot`, `会成为` (target ranks: base_value=97:34713, first_product=194:37725, bound_value=173:94543, second_product=346:64283, answer=374:80379)
- Layer 30: `Quintal`, `经贸`, `长寿`, ` Fuk`, `寿` (target ranks: base_value=97:52608, first_product=194:99041, bound_value=173:126453, second_product=346:127144, answer=374:111977)
- Layer 35: `Quintal`, `寿`, ` nac`, `otan`, ` wart` (target ranks: base_value=97:13326, first_product=194:99885, bound_value=173:126052, second_product=346:127040, answer=374:103134)
- Layer 36: `otan`, `因素的影响`, `Quintal`, `寿`, `不急` (target ranks: base_value=97:20264, first_product=194:107803, bound_value=173:125342, second_product=346:121584, answer=374:97433)
- Layer 37: `Quintal`, `本题分析`, `}<?`, `?datasetId`, `Noiz` (target ranks: base_value=97:60730, first_product=194:114227, bound_value=173:125426, second_product=346:125730, answer=374:109518)
- Layer 38: `本题分析`, `Noiz`, `}<?`, `?datasetId`, `ucl` (target ranks: base_value=97:76684, first_product=194:113705, bound_value=173:124182, second_product=346:123482, answer=374:110725)
- Layer 39: `}<?`, `本题分析`, `把事情`, `codeline`, `桃子` (target ranks: base_value=97:126119, first_product=194:127602, bound_value=173:126025, second_product=346:125467, answer=374:119939)
- Layer 40: `声响`, ` .`, `一个一个`, `试一试`, ` wart` (target ranks: base_value=97:123721, first_product=194:127775, bound_value=173:121056, second_product=346:123326, answer=374:114095)
- Layer 41: ` .`, ` .↵↵`, ` ,`, `试一试`, `等待` (target ranks: base_value=97:76421, first_product=194:106342, bound_value=173:73377, second_product=346:88223, answer=374:34177)

### Filler position 4 (absolute token 579, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:124285, first_product=194:119081, bound_value=173:119659, second_product=346:123239, answer=374:122681)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:12984, first_product=194:22960, bound_value=173:25852, second_product=346:20631, answer=374:25032)
- Layer 20: ` Covid`, ` covid`, ` quadr`, `oooo`, `梯` (target ranks: base_value=97:30358, first_product=194:31529, bound_value=173:78192, second_product=346:34458, answer=374:21786)
- Layer 30: `?datasetId`, `codeline`, `Quintal`, `}<?`, `aplenty` (target ranks: base_value=97:84376, first_product=194:69814, bound_value=173:98921, second_product=346:89856, answer=374:67906)
- Layer 35: `codeline`, `?datasetId`, `}<?`, `oze`, `ozy` (target ranks: base_value=97:109891, first_product=194:90749, bound_value=173:121401, second_product=346:85110, answer=374:79356)
- Layer 36: `oze`, `ozy`, `?datasetId`, `codeline`, `ожа` (target ranks: base_value=97:108544, first_product=194:80400, bound_value=173:120432, second_product=346:40049, answer=374:33248)
- Layer 37: `?datasetId`, `codeline`, `}<?`, `.”#`, `oNames` (target ranks: base_value=97:122877, first_product=194:97035, bound_value=173:125747, second_product=346:90089, answer=374:69033)
- Layer 38: `?datasetId`, `}<?`, `oNames`, `codeline`, `lampi` (target ranks: base_value=97:118682, first_product=194:103865, bound_value=173:125266, second_product=346:87774, answer=374:68590)
- Layer 39: `}<?`, `?datasetId`, `学着`, `codeline`, `叶子` (target ranks: base_value=97:125435, first_product=194:113305, bound_value=173:125887, second_product=346:84108, answer=374:56139)
- Layer 40: ` .↵↵`, ` .`, `dots`, ` dú`, ` .↵` (target ranks: base_value=97:93265, first_product=194:77669, bound_value=173:112130, second_product=346:21622, answer=374:5385)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, `Answer`, `<｜end▁of▁sentence｜>` (target ranks: base_value=97:46283, first_product=194:39500, bound_value=173:84578, second_product=346:9167, answer=374:1679)

### Filler position 5 (absolute token 580, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `-ulo`, `�乐` (target ranks: base_value=97:117298, first_product=194:109200, bound_value=173:109101, second_product=346:113373, answer=374:112580)
- Layer 10: `忑`, `anta`, `能吃`, `fine`, ` kinain` (target ranks: base_value=97:73354, first_product=194:74747, bound_value=173:63794, second_product=346:63612, answer=374:77843)
- Layer 20: `datasetId`, ` reluct`, `?datasetId`, ` giiniton`, `opter` (target ranks: base_value=97:119965, first_product=194:125576, bound_value=173:109199, second_product=346:120480, answer=374:125242)
- Layer 30: `?datasetId`, `aplenty`, `�乐`, `datasetId`, `-ulo` (target ranks: base_value=97:79466, first_product=194:94349, bound_value=173:16584, second_product=346:64145, answer=374:94735)
- Layer 35: `346`, `aplenty`, ` dinhi`, `345`, `oNames` (target ranks: base_value=97:125492, first_product=194:88248, bound_value=173:61981, second_product=346:1, answer=374:16736)
- Layer 36: `aplenty`, ` proiektuak`, `346`, `alista`, `325` (target ranks: base_value=97:129041, first_product=194:122514, bound_value=173:53059, second_product=346:3, answer=374:1077)
- Layer 37: `aplenty`, `alista`, ` sumala`, `346`, `-ulo` (target ranks: base_value=97:129087, first_product=194:124888, bound_value=173:60273, second_product=346:4, answer=374:1233)
- Layer 38: `322`, `323`, `alista`, `325`, `346` (target ranks: base_value=97:128597, first_product=194:127512, bound_value=173:88983, second_product=346:5, answer=374:558)
- Layer 39: `322`, `323`, `alista`, `桃子`, `324` (target ranks: base_value=97:127600, first_product=194:127360, bound_value=173:124148, second_product=346:173, answer=374:7540)
- Layer 40: ` Answer`, `Answer`, ` answer`, `答案`, `回答` (target ranks: base_value=97:127543, first_product=194:124425, bound_value=173:120874, second_product=346:308, answer=374:14372)
- Layer 41: `Answer`, ` Answer`, `答案`, ` answer`, `回答` (target ranks: base_value=97:89995, first_product=194:99770, bound_value=173:108200, second_product=346:574, answer=374:11688)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zuk = 78
xuf = twice the number for zuk minus 15
nof = 97
hoz = twice the number for nof minus 21
hoh = twice the number for nof minus 26
Question: What is twice the number for hoz plus 28?

Filler: . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
