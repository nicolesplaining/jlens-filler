# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `l` (correct).
- No-filler answer: `l` (correct).
- Filler tokens: 10 tokens at absolute indices 265–274.
- Final-head closure max absolute logit error: `0.00025177001953125`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `retrieved_name=Silver` | 1 (L33, filler 3) | L32, filler 3 (rank 7) |
| J-Lens | `answer_letter=l` | 21 (L41, filler 9) | Never |
| Logit lens | `retrieved_name=Silver` | 1 (L35, filler 3) | L33, filler 3 (rank 3) |
| Logit lens | `answer_letter=l` | 21 (L41, filler 9) | Never |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 265, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `(migrations` (target ranks: retrieved_name=Silver:58653, answer_letter=l:107125)
- Layer 10: `s`, `sem`, `anta`, `fine`, `cape` (target ranks: retrieved_name=Silver:40817, answer_letter=l:3773)
- Layer 20: `足`, `扣`, `甸`, `cape`, `表面` (target ranks: retrieved_name=Silver:77558, answer_letter=l:2445)
- Layer 30: `期望`, `希望能够`, `acin`, `原子`, `元素` (target ranks: retrieved_name=Silver:5282, answer_letter=l:56799)
- Layer 35: ` argent`, `元素`, ` silver`, ` Silver`, ` atomic` (target ranks: retrieved_name=Silver:4, answer_letter=l:45291)
- Layer 36: `元素`, ` Element`, ` element`, ` Silver`, `元素的` (target ranks: retrieved_name=Silver:4, answer_letter=l:48600)
- Layer 37: `元素`, ` Silver`, ` silver`, ` atomic`, `Silver` (target ranks: retrieved_name=Silver:2, answer_letter=l:72064)
- Layer 38: ` atomic`, ` Silver`, `atomic`, `Silver`, ` silver` (target ranks: retrieved_name=Silver:2, answer_letter=l:66003)
- Layer 39: ` Silver`, `金银`, `Silver`, ` silver`, `银` (target ranks: retrieved_name=Silver:1, answer_letter=l:75377)
- Layer 40: ` Silver`, `Silver`, ` talags`, `atomic`, `sil` (target ranks: retrieved_name=Silver:1, answer_letter=l:15944)
- Layer 41: ` .`, ` .↵↵`, `人人都`, ` ,`, ` .↵` (target ranks: retrieved_name=Silver:210, answer_letter=l:2976)

### Filler position 2 (absolute token 266, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `�乐`, `-ulo` (target ranks: retrieved_name=Silver:65153, answer_letter=l:109857)
- Layer 10: ` Walker`, `从哪里`, `Walker`, `ait`, `atile` (target ranks: retrieved_name=Silver:54553, answer_letter=l:12754)
- Layer 20: ` .`, ` distant`, `ooo`, `外向`, `oooo` (target ranks: retrieved_name=Silver:108136, answer_letter=l:8009)
- Layer 30: ` .`, `�`, `翻`, ` stitching`, ` picnic` (target ranks: retrieved_name=Silver:82594, answer_letter=l:28310)
- Layer 35: ` .`, `ilig`, `笑笑`, ` dots`, ` dot` (target ranks: retrieved_name=Silver:59058, answer_letter=l:33332)
- Layer 36: `笑笑`, ` dots`, ` .`, `反复`, ` nasod` (target ranks: retrieved_name=Silver:68113, answer_letter=l:28217)
- Layer 37: `}<?`, ` Erkännande`, ` hilabihan`, `enclose`, ` talags` (target ranks: retrieved_name=Silver:55840, answer_letter=l:70254)
- Layer 38: ` .`, ` Erkännande`, ` nasod`, `enclose`, `}<?` (target ranks: retrieved_name=Silver:55236, answer_letter=l:32573)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `}<?`, `棕`, ` nasod` (target ranks: retrieved_name=Silver:25793, answer_letter=l:42842)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` .`, ` nasod`, `enclose`, `棕` (target ranks: retrieved_name=Silver:1386, answer_letter=l:5057)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>`, `美` (target ranks: retrieved_name=Silver:15247, answer_letter=l:290)

### Filler position 3 (absolute token 267, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: retrieved_name=Silver:59464, answer_letter=l:115256)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, `挪` (target ranks: retrieved_name=Silver:56663, answer_letter=l:12396)
- Layer 20: `ait`, `螺丝`, `足`, `胃癌`, `cape` (target ranks: retrieved_name=Silver:55363, answer_letter=l:7372)
- Layer 30: ` Rhe`, `acin`, `镍`, `银杏`, `大王` (target ranks: retrieved_name=Silver:40, answer_letter=l:49668)
- Layer 35: ` silver`, ` Silver`, `Silver`, ` argent`, `ilver` (target ranks: retrieved_name=Silver:2, answer_letter=l:23115)
- Layer 36: ` Silver`, ` silver`, `Silver`, `银`, `ilver` (target ranks: retrieved_name=Silver:1, answer_letter=l:12483)
- Layer 37: ` Silver`, ` silver`, `Silver`, `银`, `ilver` (target ranks: retrieved_name=Silver:1, answer_letter=l:18680)
- Layer 38: ` Silver`, ` silver`, `Silver`, `银`, `ilver` (target ranks: retrieved_name=Silver:1, answer_letter=l:18865)
- Layer 39: ` Silver`, `Silver`, ` silver`, `argent`, `ilver` (target ranks: retrieved_name=Silver:1, answer_letter=l:16873)
- Layer 40: `散的`, `�`, `�`, `consistent`, `dg` (target ranks: retrieved_name=Silver:3624, answer_letter=l:423)
- Layer 41: ` .`, ` fused`, `人人都`, ` demand`, `essential` (target ranks: retrieved_name=Silver:6791, answer_letter=l:2608)

### Filler position 4 (absolute token 268, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: retrieved_name=Silver:60353, answer_letter=l:115583)
- Layer 10: ` Walker`, `ait`, `Walker`, `锁定`, `挪` (target ranks: retrieved_name=Silver:61897, answer_letter=l:10593)
- Layer 20: `ait`, `atile`, `忑`, `cape`, `胃癌` (target ranks: retrieved_name=Silver:66817, answer_letter=l:4502)
- Layer 30: `Tap`, `tap`, ` tap`, `提问`, ` Tap` (target ranks: retrieved_name=Silver:23663, answer_letter=l:12511)
- Layer 35: `提问`, `回答`, ` tap`, ` Question`, ` question` (target ranks: retrieved_name=Silver:23120, answer_letter=l:10768)
- Layer 36: `acin`, `提问`, ` repeated`, `羊`, ` tap` (target ranks: retrieved_name=Silver:24151, answer_letter=l:13145)
- Layer 37: `提问`, ` torn`, `反问`, `差错`, `追问` (target ranks: retrieved_name=Silver:32916, answer_letter=l:8559)
- Layer 38: `提问`, `ere`, `差错`, `onis`, `反问` (target ranks: retrieved_name=Silver:24147, answer_letter=l:14352)
- Layer 39: `<｜begin▁of▁sentence｜>`, `�`, ` Nij`, `romic`, `乐乐` (target ranks: retrieved_name=Silver:6315, answer_letter=l:44133)
- Layer 40: `inking`, `叮`, `乐乐`, `<｜begin▁of▁sentence｜>`, `�` (target ranks: retrieved_name=Silver:80, answer_letter=l:3599)
- Layer 41: ` .`, `试一试`, `叮`, `一句`, `冰冰` (target ranks: retrieved_name=Silver:2261, answer_letter=l:1925)

### Filler position 5 (absolute token 269, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: retrieved_name=Silver:61181, answer_letter=l:114954)
- Layer 10: ` Walker`, `Walker`, `ait`, `锁定`, `忑` (target ranks: retrieved_name=Silver:56915, answer_letter=l:12993)
- Layer 20: `幽`, `忑`, `鞍`, `宜`, ` Engaging` (target ranks: retrieved_name=Silver:88769, answer_letter=l:14966)
- Layer 30: ` third`, `第三`, ` letters`, ` letter`, `第三步` (target ranks: retrieved_name=Silver:103284, answer_letter=l:15880)
- Layer 35: ` letters`, `letters`, ` letter`, `Letters`, ` LETTER` (target ranks: retrieved_name=Silver:75473, answer_letter=l:23281)
- Layer 36: ` letters`, `letters`, `Letters`, ` letter`, ` LETTER` (target ranks: retrieved_name=Silver:58347, answer_letter=l:54963)
- Layer 37: ` letters`, `letters`, `Letters`, ` letter`, `letter` (target ranks: retrieved_name=Silver:57437, answer_letter=l:88741)
- Layer 38: `letters`, ` letters`, `letter`, ` letter`, `Letters` (target ranks: retrieved_name=Silver:21881, answer_letter=l:91394)
- Layer 39: `�`, `letters`, ` letters`, `letter`, ` LETTER` (target ranks: retrieved_name=Silver:3452, answer_letter=l:104471)
- Layer 40: ` letters`, ` letter`, ` LETTER`, `letters`, `�` (target ranks: retrieved_name=Silver:14, answer_letter=l:45318)
- Layer 41: ` .`, ` letters`, `仔细`, `人人都`, ` letter` (target ranks: retrieved_name=Silver:250, answer_letter=l:11480)

### Filler position 6 (absolute token 270, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: retrieved_name=Silver:61286, answer_letter=l:114043)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, ` cheer` (target ranks: retrieved_name=Silver:58888, answer_letter=l:12170)
- Layer 20: `忑`, ` smile`, `鞍`, `cape`, ` future` (target ranks: retrieved_name=Silver:76376, answer_letter=l:9680)
- Layer 30: ` repetition`, ` repetitions`, `重复`, `反复`, `鞍` (target ranks: retrieved_name=Silver:53497, answer_letter=l:15881)
- Layer 35: ` repetition`, `重复`, `反复`, ` repeated`, `询问` (target ranks: retrieved_name=Silver:46020, answer_letter=l:14933)
- Layer 36: `反复`, `询问`, ` repeated`, `重复`, ` repetition` (target ranks: retrieved_name=Silver:39263, answer_letter=l:26428)
- Layer 37: `反复`, ` prompt`, `询问`, ` stabil`, `坏` (target ranks: retrieved_name=Silver:61817, answer_letter=l:41252)
- Layer 38: ` prompt`, `银杏`, ` .`, `反复`, `不急` (target ranks: retrieved_name=Silver:40082, answer_letter=l:44441)
- Layer 39: `乐乐`, `下沉`, `繁体`, `铎`, `inking` (target ranks: retrieved_name=Silver:17094, answer_letter=l:66743)
- Layer 40: ` dotted`, ` .`, ` dots`, `inking`, `乐乐` (target ranks: retrieved_name=Silver:122, answer_letter=l:13526)
- Layer 41: ` .`, ` dotted`, `一个个`, `银杏`, ` dots` (target ranks: retrieved_name=Silver:3395, answer_letter=l:2801)

### Filler position 7 (absolute token 271, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: retrieved_name=Silver:60594, answer_letter=l:113738)
- Layer 10: ` Walker`, `Walker`, `锁定`, ` cheer`, `ait` (target ranks: retrieved_name=Silver:60335, answer_letter=l:11440)
- Layer 20: `锁定`, `忑`, ` smile`, `会成为`, `学生` (target ranks: retrieved_name=Silver:93856, answer_letter=l:11567)
- Layer 30: `sku`, ` Element`, `反复`, ` tap`, `名称` (target ranks: retrieved_name=Silver:51802, answer_letter=l:22272)
- Layer 35: `元素`, ` Element`, ` element`, `元素的`, ` Symbols` (target ranks: retrieved_name=Silver:20096, answer_letter=l:20632)
- Layer 36: `元素`, ` Element`, `元素的`, ` element`, `element` (target ranks: retrieved_name=Silver:12768, answer_letter=l:32801)
- Layer 37: `元素`, `元素的`, ` Element`, ` symbols`, ` element` (target ranks: retrieved_name=Silver:6099, answer_letter=l:38837)
- Layer 38: ` symbols`, ` symbol`, `名字`, `oNames`, ` Symbol` (target ranks: retrieved_name=Silver:5195, answer_letter=l:54006)
- Layer 39: ` симв`, ` symbol`, ` symbols`, `<｜begin▁of▁sentence｜>`, `滴滴` (target ranks: retrieved_name=Silver:268, answer_letter=l:80178)
- Layer 40: `银`, `滴滴`, ` symbols`, `一个个`, ` Silver` (target ranks: retrieved_name=Silver:5, answer_letter=l:27077)
- Layer 41: ` .`, ` symbols`, ` .↵↵`, `滴滴`, `一个个` (target ranks: retrieved_name=Silver:92, answer_letter=l:10848)

### Filler position 8 (absolute token 272, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: retrieved_name=Silver:60609, answer_letter=l:113628)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: retrieved_name=Silver:60328, answer_letter=l:10422)
- Layer 20: ` quadr`, ` smile`, `s`, ` Walker`, `sl` (target ranks: retrieved_name=Silver:73244, answer_letter=l:6528)
- Layer 30: ` spac`, ` Cosm`, `Cos`, `有意思`, ` cosm` (target ranks: retrieved_name=Silver:55616, answer_letter=l:30917)
- Layer 35: `县的`, `重复`, `反复`, ` Barnett`, `Cos` (target ranks: retrieved_name=Silver:11164, answer_letter=l:24409)
- Layer 36: `反复`, `匹配`, `长大的`, `重复`, ` riv` (target ranks: retrieved_name=Silver:5546, answer_letter=l:21936)
- Layer 37: `悬挂`, `悬`, `挂`, `懸`, `anium` (target ranks: retrieved_name=Silver:8875, answer_letter=l:35383)
- Layer 38: `悬挂`, `悬`, `�`, `静静`, ` .` (target ranks: retrieved_name=Silver:5859, answer_letter=l:35618)
- Layer 39: `乐乐`, `�`, `codeline`, `贻`, `悬挂` (target ranks: retrieved_name=Silver:1505, answer_letter=l:47653)
- Layer 40: ` .`, `乐乐`, `�`, ` .↵↵`, ` dot` (target ranks: retrieved_name=Silver:125, answer_letter=l:7132)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `一个个`, `静静` (target ranks: retrieved_name=Silver:404, answer_letter=l:677)

### Filler position 9 (absolute token 273, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: retrieved_name=Silver:60347, answer_letter=l:113174)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: retrieved_name=Silver:58511, answer_letter=l:11047)
- Layer 20: `子的`, `题的`, `受访`, `͡`, ` Respondents` (target ranks: retrieved_name=Silver:72140, answer_letter=l:17210)
- Layer 30: `codeline`, `}<?`, `答案是`, ` ответ`, ` Answer` (target ranks: retrieved_name=Silver:44988, answer_letter=l:82283)
- Layer 35: ` Answer`, ` ответ`, `答案是`, ` Antwort`, `本题分析` (target ranks: retrieved_name=Silver:16218, answer_letter=l:67079)
- Layer 36: ` Answer`, ` ответ`, ` answer`, ` پاسخ`, ` reply` (target ranks: retrieved_name=Silver:8590, answer_letter=l:41015)
- Layer 37: `本题分析`, `�`, `</think>`, ` instantaneous`, `听完` (target ranks: retrieved_name=Silver:10582, answer_letter=l:59875)
- Layer 38: `</think>`, `�`, `聽`, `本题分析`, `�` (target ranks: retrieved_name=Silver:4835, answer_letter=l:57487)
- Layer 39: `-ulo`, `tanle`, `�`, ` instantaneous`, `�乐` (target ranks: retrieved_name=Silver:2133, answer_letter=l:45192)
- Layer 40: ` Answer`, ` silver`, `银`, `美`, ` Thought` (target ranks: retrieved_name=Silver:37, answer_letter=l:4984)
- Layer 41: ` Answer`, `Answer`, ` .`, ` .↵↵`, ` silver` (target ranks: retrieved_name=Silver:145, answer_letter=l:21)

### Filler position 10 (absolute token 274, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `-ulo` (target ranks: retrieved_name=Silver:53984, answer_letter=l:111420)
- Layer 10: ` everydaycalculation`, ` Saysay`, `EDMF`, `основним`, `{enclose` (target ranks: retrieved_name=Silver:4039, answer_letter=l:63222)
- Layer 20: `ait`, `鸯`, ` Submission`, `坷`, `哪位` (target ranks: retrieved_name=Silver:47277, answer_letter=l:31610)
- Layer 30: ` dekameters`, `解释`, `oNames`, `rinnings`, ` dátummal` (target ranks: retrieved_name=Silver:4851, answer_letter=l:93169)
- Layer 35: ` Silver`, ` silver`, `Silver`, `银`, `銀` (target ranks: retrieved_name=Silver:1, answer_letter=l:62419)
- Layer 36: `銀`, `银`, `rinnings`, `Argent`, `银色` (target ranks: retrieved_name=Silver:10, answer_letter=l:49918)
- Layer 37: `银色`, ` silver`, `ilver`, `Silver`, `銀` (target ranks: retrieved_name=Silver:4, answer_letter=l:37857)
- Layer 38: ` Silver`, `Silver`, ` silver`, `ilver`, `银色` (target ranks: retrieved_name=Silver:1, answer_letter=l:29197)
- Layer 39: ` Silver`, `Silver`, `ilver`, `银色`, ` silver` (target ranks: retrieved_name=Silver:1, answer_letter=l:3479)
- Layer 40: ` Answer`, `回答`, ` answer`, `Answer`, `答` (target ranks: retrieved_name=Silver:15, answer_letter=l:113)
- Layer 41: `Answer`, ` Answer`, ` answer`, `回答`, `答案` (target ranks: retrieved_name=Silver:38, answer_letter=l:358)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a question asking for a specific letter. Answer immediately with just the single lowercase letter, nothing else. No explanation, no words, no reasoning, just the letter. After the question, there will be 10 filler tokens (a sequence of dots) before you answer.<｜User｜>Question: What is the third letter of the chemical element with atomic number 4?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>r<｜end▁of▁sentence｜><｜User｜>Question: What is the last letter of the chemical element with atomic number 15?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>s<｜end▁of▁sentence｜><｜User｜>Question: What is the second letter of the chemical element with atomic number 36?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>r<｜end▁of▁sentence｜><｜User｜>Question: What is the third letter of the chemical element with atomic number 82?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>a<｜end▁of▁sentence｜><｜User｜>Question: What is the last letter of the chemical element with atomic number 95?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>m<｜end▁of▁sentence｜><｜User｜>Question: What is the third letter of the chemical element with atomic number 47?

Filler: . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
