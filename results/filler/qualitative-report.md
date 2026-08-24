# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `80` (correct).
- No-filler answer: `80` (correct).
- Filler tokens: 10 tokens at absolute indices 278–287.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `74` | 1 (L36, filler 4) | L35, filler 4 (rank 10) |
| J-Lens | `6` | 5 (L36, filler 8) | L35, filler 8 (rank 10) |
| J-Lens | `80` | 89 (L41, filler 10) | Never |
| Logit lens | `74` | 2 (L37, filler 5) | L37, filler 5 (rank 2) |
| Logit lens | `6` | 12 (L36, filler 8) | Never |
| Logit lens | `80` | 77 (L40, filler 10) | Never |

The clearest filler-localized signal is the tungsten value: J-Lens reads `74` as top-1 at layer 36/filler 4 and at several nearby late-layer cells. The numeric token `6` reaches rank 5 at layer 36/filler 8, where the top readout is the lexical token ` six`. The lexical sum form ` eighty` is top-1 at layer 40/filler 4, even though the numeric sum token `80` never reaches the filler-cell top 10; numeric `80` becomes rank 2 only at the layer-40 answer-prediction position before the final block.

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 278, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `(migrations` (target ranks: 74=117385, 6=125187, 80=119034)
- Layer 10: `cape`, `锁定`, `Walker`, ` Walker`, ` cheer` (target ranks: 74=21160, 6=7720, 80=17987)
- Layer 20: `足`, `扣`, `旬`, `甸`, `表面` (target ranks: 74=1255, 6=97, 80=719)
- Layer 30: ` tungsten`, `钨`, ` capitalized`, ` Tung`, ` capitalization` (target ranks: 74=16521, 6=12341, 80=24700)
- Layer 35: ` tungsten`, `元素`, `钨`, `元素的`, `cape` (target ranks: 74=4217, 6=2924, 80=11730)
- Layer 36: `元素`, `元素的`, ` Element`, ` element`, `cape` (target ranks: 74=5401, 6=5313, 80=17396)
- Layer 37: `元素的`, `元素`, ` Element`, ` element`, `要素` (target ranks: 74=22700, 6=36958, 80=35831)
- Layer 38: `元素的`, `元素`, ` Element`, ` elemental`, ` capitalization` (target ranks: 74=36119, 6=52455, 80=32826)
- Layer 39: ` Tung`, `多多`, `迷惑`, `MMMMMMMM`, `防护` (target ranks: 74=90271, 6=120255, 80=91365)
- Layer 40: ` talags`, ` Tung`, ` LD`, `oooo`, `akak` (target ranks: 74=37218, 6=72967, 80=68104)
- Layer 41: ` .`, ` patiently`, ` .↵↵`, ` .↵`, `人人都` (target ranks: 74=10296, 6=17689, 80=47725)

### Filler position 2 (absolute token 279, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: 74=117647, 6=125485, 80=122196)
- Layer 10: ` Walker`, `从哪里`, `atile`, `Walker`, `ait` (target ranks: 74=24368, 6=7055, 80=24855)
- Layer 20: ` .`, ` .----`, `ools`, ` kodea`, `OOL` (target ranks: 74=113729, 6=103320, 80=103764)
- Layer 30: `dot`, ` dekameters`, `Dot`, `dots`, ` .` (target ranks: 74=121507, 6=85540, 80=101479)
- Layer 35: ` .`, `dot`, `Dot`, ` Propri`, ` dot` (target ranks: 74=122448, 6=74170, 80=79263)
- Layer 36: ` reserved`, `odor`, ` Theodor`, ` Propri`, ` .` (target ranks: 74=113131, 6=44490, 80=69990)
- Layer 37: `}<?`, ` Erkännande`, `ernet`, ` hilabihan`, `aharan` (target ranks: 74=125490, 6=127888, 80=104854)
- Layer 38: ` .`, `}<?`, ` .↵↵`, `ernet`, `殿堂` (target ranks: 74=126414, 6=128054, 80=80546)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, `�乐`, `+-+-+-+-` (target ranks: 74=122108, 6=126741, 80=90540)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` Response` (target ranks: 74=99596, 6=107568, 80=73289)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ..`, ` ,` (target ranks: 74=62526, 6=38702, 80=51629)

### Filler position 3 (absolute token 280, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: 74=121230, 6=127566, 80=125247)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: 74=13574, 6=3781, 80=13129)
- Layer 20: `s`, `足`, `�`, `cape`, `ka` (target ranks: 74=5523, 6=777, 80=6741)
- Layer 30: ` tungsten`, `钨`, ` Tung`, ` atomic`, ` tung` (target ranks: 74=45517, 6=20798, 80=44027)
- Layer 35: ` tungsten`, ` Tung`, `钨`, ` tung`, ` atomic` (target ranks: 74=405, 6=3282, 80=5099)
- Layer 36: ` tungsten`, ` Tung`, `钨`, ` tung`, ` atomic` (target ranks: 74=450, 6=3890, 80=4916)
- Layer 37: ` Tung`, ` tungsten`, ` atomic`, `钨`, ` tung` (target ranks: 74=2162, 6=37955, 80=13804)
- Layer 38: ` Tung`, ` tungsten`, ` atomic`, ` Atomic`, ` tung` (target ranks: 74=6281, 6=60886, 80=19559)
- Layer 39: ` Tung`, ` tung`, ` tungsten`, ` atomic`, ` Atomic` (target ranks: 74=53358, 6=112313, 80=84306)
- Layer 40: ` atomic`, `atomic`, ` Tung`, ` Atomic`, `Atomic` (target ranks: 74=13934, 6=62224, 80=55006)
- Layer 41: ` .`, ` atomic`, `atomic`, ` fused`, `人人都` (target ranks: 74=9089, 6=18990, 80=21594)

### Filler position 4 (absolute token 281, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: 74=121327, 6=127819, 80=125672)
- Layer 10: ` Walker`, `ait`, `Walker`, `锁定`, `忑` (target ranks: 74=16166, 6=4727, 80=15634)
- Layer 20: `ait`, `cape`, `挪`, `胃癌`, `足` (target ranks: 74=9594, 6=1535, 80=10204)
- Layer 30: ` dy`, `Tap`, ` pairing`, ` Tap`, `tap` (target ranks: 74=2480, 6=1781, 80=7520)
- Layer 35: ` dy`, `Tap`, ` Tap`, ` tap`, `匹配` (target ranks: 74=10, 6=1156, 80=281)
- Layer 36: `74`, ` Tap`, ` stabil`, ` tap`, `期望` (target ranks: 74=1, 6=2073, 80=393)
- Layer 37: `74`, `七十二`, ` Seventy`, ` seventy`, `acons` (target ranks: 74=1, 6=22786, 80=5242)
- Layer 38: `74`, `主人的`, ` transcend`, `打包`, `lisitry` (target ranks: 74=1, 6=22049, 80=2510)
- Layer 39: `八十`, ` eighty`, `86`, ` Eighty`, `ucl` (target ranks: 74=23346, 6=108407, 80=171)
- Layer 40: ` eighty`, ` atomic`, `八十`, `atomic`, ` Tung` (target ranks: 74=26711, 6=93270, 80=240)
- Layer 41: ` .`, ` atomic`, ` fused`, `atomic`, ` Rutherford` (target ranks: 74=17015, 6=18349, 80=755)

### Filler position 5 (absolute token 282, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: 74=120417, 6=127634, 80=125319)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, `挪` (target ranks: 74=20230, 6=6671, 80=19342)
- Layer 20: `鞍`, `幽`, `足`, ` smile`, `cape` (target ranks: 74=13194, 6=3569, 80=9698)
- Layer 30: ` picnic`, ` tap`, `Tap`, `打完`, ` Tap` (target ranks: 74=3108, 6=3305, 80=6704)
- Layer 35: ` picnic`, `打完`, `保留`, `obin`, `操作` (target ranks: 74=345, 6=2917, 80=4512)
- Layer 36: `保留`, `打完`, ` picnic`, `ilig`, `推算` (target ranks: 74=1163, 6=15250, 80=18387)
- Layer 37: `74`, `}<?`, `额外`, `hemer`, `otechnical` (target ranks: 74=1, 6=96746, 80=35213)
- Layer 38: `}<?`, `hemer`, `74`, `殿堂`, `otechnical` (target ranks: 74=3, 6=98526, 80=44021)
- Layer 39: `}<?`, `-ulo`, `hemer`, `东海`, `acons` (target ranks: 74=9, 6=128168, 80=15227)
- Layer 40: `hemer`, `74`, `ilig`, ` pancre`, `venture` (target ranks: 74=2, 6=127862, 80=20338)
- Layer 41: ` .`, `不如`, `鹉`, `人人都`, `特异` (target ranks: 74=23, 6=111919, 80=11915)

### Filler position 6 (absolute token 283, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: 74=119593, 6=127366, 80=124709)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: 74=17119, 6=5543, 80=16902)
- Layer 20: `鞍`, ` smile`, `足`, `锁定`, `cape` (target ranks: 74=6053, 6=2284, 80=3746)
- Layer 30: `anium`, `Conc`, ` spac`, ` rhe`, ` picnic` (target ranks: 74=2648, 6=22549, 80=3299)
- Layer 35: ` binding`, `认`, `ilig`, ` future`, ` soci` (target ranks: 74=203, 6=2232, 80=2836)
- Layer 36: `iahy`, `igesimal`, `acons`, `anium`, ` structural` (target ranks: 74=407, 6=9188, 80=9598)
- Layer 37: `}<?`, `?datasetId`, `院内`, `74`, `<｜begin▁of▁sentence｜>` (target ranks: 74=4, 6=69231, 80=31310)
- Layer 38: `}<?`, `-ulo`, `院内`, `acons`, `?datasetId` (target ranks: 74=16, 6=96662, 80=13960)
- Layer 39: `-ulo`, `}<?`, `东海`, `本题分析`, ` eighty` (target ranks: 74=1822, 6=127252, 80=9040)
- Layer 40: `anium`, ` eighty`, ` seventy`, `下沉`, `海滨` (target ranks: 74=3934, 6=126467, 80=28139)
- Layer 41: ` .`, `人人都`, ` eighty`, ` seventy`, ` .↵↵` (target ranks: 74=1008, 6=91570, 80=15058)

### Filler position 7 (absolute token 284, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: 74=119222, 6=127247, 80=124385)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: 74=17229, 6=5323, 80=16171)
- Layer 20: ` smile`, `锁定`, `忑`, ` cheer`, `能被` (target ranks: 74=8826, 6=3951, 80=6413)
- Layer 30: ` Atomic`, ` atomic`, `Atomic`, `atomic`, ` tap` (target ranks: 74=20093, 6=43562, 80=24591)
- Layer 35: `反复`, ` August`, ` tungsten`, `钨`, ` Atomic` (target ranks: 74=3740, 6=10025, 80=12146)
- Layer 36: `反复`, ` August`, ` smile`, ` biolog`, ` tap` (target ranks: 74=1970, 6=5035, 80=7242)
- Layer 37: `德华`, ` Atomic`, ` spac`, `onica`, `反复` (target ranks: 74=9327, 6=31018, 80=14550)
- Layer 38: ` .`, ` hollow`, ` Atomic`, `otechnical`, `onica` (target ranks: 74=16084, 6=54427, 80=25948)
- Layer 39: `�`, ` Fusion`, ` .`, ` CET`, `�乐` (target ranks: 74=80353, 6=118390, 80=76676)
- Layer 40: ` .`, ` .↵↵`, ` dotted`, `一点点`, ` WW` (target ranks: 74=36853, 6=83986, 80=53278)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `一个一个`, ` ,` (target ranks: 74=2970, 6=28630, 80=13307)

### Filler position 8 (absolute token 285, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: 74=119142, 6=127230, 80=124302)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: 74=14803, 6=4227, 80=14055)
- Layer 20: ` smile`, ` Walker`, `ait`, `cape`, `Walker` (target ranks: 74=4125, 6=885, 80=3599)
- Layer 30: `Quintal`, ` Cosm`, `不急`, ` spac`, `安全的` (target ranks: 74=40906, 6=50811, 80=82014)
- Layer 35: `six`, ` six`, `六`, ` hexagonal`, `六月` (target ranks: 74=19680, 6=10, 80=64060)
- Layer 36: ` six`, ` Sixth`, `六`, `six`, `6` (target ranks: 74=16077, 6=5, 80=49690)
- Layer 37: ` Sixth`, ` sixth`, ` hexagonal`, ` six`, `六` (target ranks: 74=92227, 6=31, 80=88984)
- Layer 38: `anium`, `悬挂`, `纳税`, `rily`, ` covari` (target ranks: 74=75770, 6=49877, 80=52881)
- Layer 39: `东海`, `codeline`, `稍稍`, `晶莹`, ` Fusion` (target ranks: 74=104949, 6=122151, 80=82312)
- Layer 40: ` .`, ` .↵↵`, ` dot`, `静静`, `小狗` (target ranks: 74=53783, 6=103874, 80=51149)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, ` seventy` (target ranks: 74=11060, 6=47916, 80=16532)

### Filler position 9 (absolute token 286, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: 74=118693, 6=127127, 80=124181)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: 74=14083, 6=3837, 80=13505)
- Layer 20: `子的`, `eight`, `受访`, `评分`, ` Tail` (target ranks: 74=62943, 6=6912, 80=37609)
- Layer 30: `}<?`, `codeline`, `}using`, ` Answer`, `答案是` (target ranks: 74=116722, 6=117943, 80=126587)
- Layer 35: ` Answer`, ` Hint`, `答案是`, ` answer`, ` ANSWER` (target ranks: 74=120250, 6=112035, 80=119271)
- Layer 36: ` Answer`, `应答`, ` پاسخ`, ` Reply`, ` answer` (target ranks: 74=90767, 6=75118, 80=85722)
- Layer 37: `</think>`, ` consum`, `�`, `оду`, `聽` (target ranks: 74=105473, 6=84189, 80=98490)
- Layer 38: `�`, `�`, `оду`, `oNames`, ` Thor` (target ranks: 74=116421, 6=102219, 80=104569)
- Layer 39: ` .↵↵`, `树叶`, ` .↵`, ` .`, ` dú` (target ranks: 74=103294, 6=117685, 80=100883)
- Layer 40: ` .↵↵`, ` .`, ` .↵`, ` Reply`, ` Answer` (target ranks: 74=31765, 6=51141, 80=27306)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, `叮`, ` thought` (target ranks: 74=3525, 6=3228, 80=4968)

### Filler position 10 (absolute token 287, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `-ulo` (target ranks: 74=118343, 6=125798, 80=119725)
- Layer 10: `EDMF`, ` Saysay`, ` everydaycalculation`, ` dével`, `{enclose` (target ranks: 74=128824, 6=128959, 80=128307)
- Layer 20: ` ChatGPT`, ` Submission`, `鸯`, `禀`, `ait` (target ranks: 74=40836, 6=21757, 80=38805)
- Layer 30: `回答`, `答案为`, `答案是`, `答案`, ` answer` (target ranks: 74=101368, 6=98848, 80=116882)
- Layer 35: `答案是`, ` Answer`, ` answer`, `答案为`, `答案` (target ranks: 74=104079, 6=87872, 80=85838)
- Layer 36: ` answer`, ` Answer`, `回答`, `答案`, `解答` (target ranks: 74=88693, 6=76252, 80=74704)
- Layer 37: ` Paglin`, ` dátummal`, `malink`, `/Tropical`, `amina` (target ranks: 74=107997, 6=117132, 80=91143)
- Layer 38: ` Answer`, `malink`, `amina`, ` medief`, ` dátummal` (target ranks: 74=100152, 6=113996, 80=78317)
- Layer 39: `Answer`, ` Answer`, `answer`, ` answer`, ` Antwort` (target ranks: 74=1832, 6=101115, 80=5852)
- Layer 40: `Answer`, ` Answer`, ` answer`, `回答`, ` Antwort` (target ranks: 74=66, 6=16076, 80=117)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: 74=38, 6=928, 80=89)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a question that requires adding two values together. Answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be some filler tokens (a sequence of dots) to give you extra space to process the problem before answering.<｜User｜>Question: What is the atomic number of Helium plus the atomic number of Neon?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>12<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Sulfur plus the atomic number of Cobalt?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>43<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Selenium plus the atomic number of Promethium?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>95<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Europium plus the atomic number of Tantalum?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>136<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Rhenium plus the atomic number of Protactinium?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>166<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of tungsten plus the atomic number of carbon?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
