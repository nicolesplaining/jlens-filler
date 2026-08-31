# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `31` (incorrect).
- No-filler answer: `15` (correct).
- Filler tokens: 10 tokens at absolute indices 448–457.
- Final-head closure max absolute logit error: `7.62939453125e-06`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `x_1=15` | 261 (L40, filler 3) | Never |
| Logit lens | `x_1=15` | 158 (L38, filler 3) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 448, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `(migrations` (target ranks: x_1=15:121033)
- Layer 10: `anta`, `fine`, `钩`, `忑`, `Walker` (target ranks: x_1=15:46331)
- Layer 20: `足`, `扣`, `表面`, `垂`, `adows` (target ranks: x_1=15:1271)
- Layer 30: `期望`, `期待的`, ` expecting`, ` calculator`, `931` (target ranks: x_1=15:32368)
- Layer 35: `961`, `962`, `951`, `971`, `966` (target ranks: x_1=15:3602)
- Layer 36: `961`, `962`, ` talags`, `期望`, `951` (target ranks: x_1=15:7898)
- Layer 37: `961`, `471`, `962`, `441`, `期望` (target ranks: x_1=15:21668)
- Layer 38: `381`, `IPA`, `408`, `441`, `961` (target ranks: x_1=15:21799)
- Layer 39: `本题分析`, `IPA`, `osine`, ` talags`, `叶子` (target ranks: x_1=15:113497)
- Layer 40: ` talags`, ` Mat`, ` torn`, `处以`, ` ald` (target ranks: x_1=15:109326)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `耘`, `知乎` (target ranks: x_1=15:34110)

### Filler position 2 (absolute token 449, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: x_1=15:123404)
- Layer 10: ` Walker`, `从哪里`, `忑`, `ait`, `Walker` (target ranks: x_1=15:24170)
- Layer 20: ` .`, ` .----`, ` .↵↵`, `ozoic`, `ools` (target ranks: x_1=15:121424)
- Layer 30: ` dekameters`, ` .`, ` hilabihan`, ` .----`, ` "."` (target ranks: x_1=15:111780)
- Layer 35: ` .`, `拖延`, ` camou`, `ilig`, ` .↵↵` (target ranks: x_1=15:117288)
- Layer 36: ` .`, `odor`, ` reserved`, `拖延`, `tober` (target ranks: x_1=15:81907)
- Layer 37: `}<?`, ` Erkännande`, `心地`, ` licensierad`, `鼓起` (target ranks: x_1=15:125858)
- Layer 38: ` .`, ` .↵↵`, ` .↵`, `}<?`, `心地` (target ranks: x_1=15:119536)
- Layer 39: ` .`, ` .↵↵`, ` .↵`, ` .----`, `铎` (target ranks: x_1=15:122092)
- Layer 40: ` .`, ` filler`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: x_1=15:92145)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` filler`, ` ↵` (target ranks: x_1=15:41301)

### Filler position 3 (absolute token 450, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126216)
- Layer 10: ` Walker`, `锁定`, `ait`, `忑`, `Walker` (target ranks: x_1=15:14154)
- Layer 20: `足`, `�`, `能被`, ` ternary`, `ative` (target ranks: x_1=15:1928)
- Layer 30: `}<?`, ` Septy`, `aned`, ` dekameters`, `otan` (target ranks: x_1=15:73700)
- Layer 35: ` Alban`, `}<?`, `LikeLike`, `Judge`, `竹子` (target ranks: x_1=15:5852)
- Layer 36: `}<?`, ` Septy`, `506`, `476`, `509` (target ranks: x_1=15:25995)
- Layer 37: `科学院`, `505`, `506`, `在线阅读`, `509` (target ranks: x_1=15:9437)
- Layer 38: `科学院`, ` assimil`, `抗疫`, `在线阅读`, `各区` (target ranks: x_1=15:1491)
- Layer 39: `本题分析`, `各区`, `malink`, `在海`, `iaux` (target ranks: x_1=15:5018)
- Layer 40: `本题分析`, `gener`, `))))`, ` talags`, `anin` (target ranks: x_1=15:261)
- Layer 41: ` .`, ` nuest`, ` 。`, ` disadvant`, `余` (target ranks: x_1=15:1784)

### Filler position 4 (absolute token 451, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126996)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: x_1=15:11900)
- Layer 20: `ait`, `挪`, `cape`, `atile`, `胃癌` (target ranks: x_1=15:8895)
- Layer 30: `期望`, ` expecting`, `calculator`, ` calculator`, ` Calculator` (target ranks: x_1=15:91508)
- Layer 35: `961`, `962`, `969`, `967`, `966` (target ranks: x_1=15:32162)
- Layer 36: `961`, `969`, ` noise`, `962`, `960` (target ranks: x_1=15:47516)
- Layer 37: `961`, `962`, `960`, ` noise`, ` Pari` (target ranks: x_1=15:39575)
- Layer 38: `961`, `408`, `960`, `497`, `441` (target ranks: x_1=15:22009)
- Layer 39: `本题分析`, `ozygous`, `�乐`, ` Pari`, `处以` (target ranks: x_1=15:93109)
- Layer 40: `处以`, ` XAF`, `imat`, ` reper`, `焦` (target ranks: x_1=15:72517)
- Layer 41: ` .`, ` fibr`, ` .↵↵`, `一般而言`, `.` (target ranks: x_1=15:2882)

### Filler position 5 (absolute token 452, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:127045)
- Layer 10: ` Walker`, `Walker`, `挪`, `锁定`, `勾` (target ranks: x_1=15:16030)
- Layer 20: `忑`, `锁定`, `鞍`, ` LS`, `挪` (target ranks: x_1=15:18655)
- Layer 30: `�`, ` impulse`, `起始`, `反复`, ` start` (target ranks: x_1=15:63904)
- Layer 35: ` repetition`, `反复`, ` start`, `重复`, `起始` (target ranks: x_1=15:20819)
- Layer 36: `反复`, ` repetition`, ` rip`, ` ri`, `重复` (target ranks: x_1=15:24153)
- Layer 37: `}<?`, `滴`, `htaking`, `覆`, `反复` (target ranks: x_1=15:61910)
- Layer 38: `}<?`, `覆`, `hemer`, `不急`, `滴` (target ranks: x_1=15:81703)
- Layer 39: `hemer`, `}<?`, `东海`, `�`, `aharan` (target ranks: x_1=15:115906)
- Layer 40: ` .`, `oooo`, `省略`, `hemer`, ` repetition` (target ranks: x_1=15:92335)
- Layer 41: ` .`, ` .↵↵`, ` ,`, ` fused`, ` ..` (target ranks: x_1=15:24101)

### Filler position 6 (absolute token 453, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126762)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, `挪` (target ranks: x_1=15:12450)
- Layer 20: `挪`, `鞍`, `ait`, ` smile`, `cape` (target ranks: x_1=15:13609)
- Layer 30: `itore`, `重复`, ` question`, `提问`, ` tap` (target ranks: x_1=15:83558)
- Layer 35: ` Question`, `反复`, `重复`, `Question`, ` question` (target ranks: x_1=15:70036)
- Layer 36: ` Question`, `重复`, `反复`, ` question`, `询问` (target ranks: x_1=15:55623)
- Layer 37: ` follow`, `anium`, `本题分析`, ` Question`, `追问` (target ranks: x_1=15:103056)
- Layer 38: `本题分析`, `hemer`, `}<?`, `�`, `�` (target ranks: x_1=15:122214)
- Layer 39: `hemer`, `本题分析`, `额外`, `aharan`, `<｜begin▁of▁sentence｜>` (target ranks: x_1=15:122830)
- Layer 40: ` .`, ` talags`, ` dotted`, ` follow`, `hemer` (target ranks: x_1=15:105806)
- Layer 41: ` .`, ` .↵↵`, ` ..`, `Question`, `问` (target ranks: x_1=15:24074)

### Filler position 7 (absolute token 454, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126595)
- Layer 10: ` Walker`, `锁定`, `Walker`, `挪`, `ait` (target ranks: x_1=15:12617)
- Layer 20: `锁定`, `鞍`, ` smile`, `足`, ` cheer` (target ranks: x_1=15:4843)
- Layer 30: `31`, ` x`, ` 𝑥`, ` squares`, ` squared` (target ranks: x_1=15:33994)
- Layer 35: `31`, ` x`, ` step`, `第一步`, ` Step` (target ranks: x_1=15:14377)
- Layer 36: `31`, ` x`, `第一步`, ` step`, ` 𝑥` (target ranks: x_1=15:37147)
- Layer 37: `31`, `otan`, ` 𝑥`, ` Squ`, ` squared` (target ranks: x_1=15:89340)
- Layer 38: `}<?`, `本题分析`, `ampu`, `?datasetId`, `otan` (target ranks: x_1=15:115638)
- Layer 39: `hemer`, `一个好`, `本题分析`, `}<?`, `?datasetId` (target ranks: x_1=15:123396)
- Layer 40: `hemer`, ` talags`, `覆`, `留存`, `otan` (target ranks: x_1=15:117544)
- Layer 41: ` .`, `一个好`, ` .↵↵`, ` without`, ` ,` (target ranks: x_1=15:75571)

### Filler position 8 (absolute token 455, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126543)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: x_1=15:11149)
- Layer 20: ` quadr`, ` Walker`, ` smile`, `锁定`, `Walker` (target ranks: x_1=15:3446)
- Layer 30: `Quintal`, `东京`, `dividers`, `累`, `下沉` (target ranks: x_1=15:88591)
- Layer 35: `不急`, `保留`, `县的`, ` .`, `稍稍` (target ranks: x_1=15:11041)
- Layer 36: `保留`, `重复`, `反复`, `不急`, ` quadr` (target ranks: x_1=15:7141)
- Layer 37: `悬挂`, `codeline`, `采集`, `悬`, `isl` (target ranks: x_1=15:44735)
- Layer 38: `悬挂`, ` .`, `悬`, `usk`, `懸` (target ranks: x_1=15:56378)
- Layer 39: ` .`, ` .↵↵`, ` Fusion`, `悬挂`, `一个个` (target ranks: x_1=15:88043)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `ooo`, `šk` (target ranks: x_1=15:30131)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `<｜end▁of▁sentence｜>` (target ranks: x_1=15:7130)

### Filler position 9 (absolute token 456, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: x_1=15:126430)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `挪` (target ranks: x_1=15:10541)
- Layer 20: ` Tact`, ` pandemic`, ` pandemia`, `重复`, ` .` (target ranks: x_1=15:7935)
- Layer 30: ` Answer`, `}<?`, ` Antwort`, `答案是`, `codeline` (target ranks: x_1=15:118342)
- Layer 35: ` Answer`, `应答`, ` Antwort`, ` answer`, ` ANSWER` (target ranks: x_1=15:113711)
- Layer 36: ` Answer`, ` Reply`, ` answer`, `应答`, ` reply` (target ranks: x_1=15:76036)
- Layer 37: `oNames`, `uze`, `�`, `оду`, `聽` (target ranks: x_1=15:114055)
- Layer 38: `聽`, `oNames`, `�`, `�`, ` inve` (target ranks: x_1=15:116840)
- Layer 39: ` .↵↵`, ` mno`, ` .----`, ` .↵`, `树叶` (target ranks: x_1=15:97335)
- Layer 40: ` .↵↵`, ` .`, ` .↵`, ` Answer`, `�` (target ranks: x_1=15:17865)
- Layer 41: ` .↵↵`, ` .`, ` .↵`, ` .=`, ` ./` (target ranks: x_1=15:423)

### Filler position 10 (absolute token 457, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `(migrations`, `�乐`, `-ulo` (target ranks: x_1=15:121445)
- Layer 10: `основним`, ` everydaycalculation`, ` Saysay`, `{enclose`, `eva` (target ranks: x_1=15:127060)
- Layer 20: `ait`, ` Walker`, `忑`, `Walker`, ` smile` (target ranks: x_1=15:14731)
- Layer 30: `回答`, ` answer`, ` Answer`, `答案`, `Answer` (target ranks: x_1=15:52222)
- Layer 35: ` answer`, `回答`, ` Answer`, `解答`, `(answer` (target ranks: x_1=15:32615)
- Layer 36: ` answer`, ` Answer`, `回答`, ` dátummal`, `answer` (target ranks: x_1=15:23817)
- Layer 37: ` dátummal`, ` Answer`, ` answer`, ` medief`, `回答` (target ranks: x_1=15:63587)
- Layer 38: ` Answer`, `Answer`, ` answer`, ` dátummal`, `answer` (target ranks: x_1=15:94912)
- Layer 39: ` Answer`, `Answer`, ` answer`, `answer`, `(answer` (target ranks: x_1=15:80633)
- Layer 40: `Answer`, ` Answer`, ` answer`, `answer`, `回答` (target ranks: x_1=15:23899)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `答` (target ranks: x_1=15:1424)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>Question: Starting with x_0 = 31 mod 473, repeatedly apply x_t = x_(t-1)^2 mod 473 for exactly 1 steps. What is x_1?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
