# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `320` (incorrect).
- No-filler answer: `322` (incorrect).
- Filler tokens: 25 tokens at absolute indices 676–700.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=97` | 1 (L27, filler 4) | L24, filler 4 (rank 6) |
| J-Lens | `first_product=194` | 222 (L31, filler 20) | Never |
| J-Lens | `bound_value=173` | 1 (L31, filler 4) | L31, filler 4 (rank 1) |
| J-Lens | `second_product=346` | 1 (L33, filler 1) | L31, filler 4 (rank 2) |
| J-Lens | `answer=374` | 1 (L38, filler 7) | L36, filler 7 (rank 2) |
| Logit lens | `base_value=97` | 1 (L24, filler 16) | L24, filler 1 (rank 8) |
| Logit lens | `first_product=194` | 26 (L30, filler 20) | Never |
| Logit lens | `bound_value=173` | 1 (L31, filler 16) | L31, filler 16 (rank 1) |
| Logit lens | `second_product=346` | 1 (L33, filler 16) | L31, filler 16 (rank 7) |
| Logit lens | `answer=374` | 1 (L38, filler 7) | L36, filler 7 (rank 2) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 676, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=97:118044, first_product=194:111616, bound_value=173:113798, second_product=346:112987, answer=374:113039)
- Layer 10: `anta`, `fine`, `咫`, `钩`, `忑` (target ranks: base_value=97:67729, first_product=194:61783, bound_value=173:72580, second_product=346:49591, answer=374:63173)
- Layer 20: ` .`, `期望`, `足`, `扣`, `重` (target ranks: base_value=97:5773, first_product=194:30123, bound_value=173:24461, second_product=346:5667, answer=374:15461)
- Layer 30: ` pakig`, ` talags`, `期望`, `期待的`, `ASCAR` (target ranks: base_value=97:2099, first_product=194:38077, bound_value=173:645, second_product=346:23162, answer=374:43829)
- Layer 35: `346`, `345`, `349`, `366`, `340` (target ranks: base_value=97:72247, first_product=194:12217, bound_value=173:39211, second_product=346:1, answer=374:603)
- Layer 36: `370`, `316`, `376`, `366`, `346` (target ranks: base_value=97:128294, first_product=194:84449, bound_value=173:58943, second_product=346:5, answer=374:28)
- Layer 37: `316`, `366`, `376`, `370`, `372` (target ranks: base_value=97:129216, first_product=194:116838, bound_value=173:101759, second_product=346:10, answer=374:51)
- Layer 38: `316`, `366`, `376`, `370`, `372` (target ranks: base_value=97:128836, first_product=194:124406, bound_value=173:122032, second_product=346:8, answer=374:21)
- Layer 39: `372`, `rossover`, `三百`, ` crossover`, ` gang` (target ranks: base_value=97:128664, first_product=194:126742, bound_value=173:128464, second_product=346:4478, answer=374:661)
- Layer 40: ` talags`, ` ald`, `Ald`, `ALD`, ` Ald` (target ranks: base_value=97:128669, first_product=194:127173, bound_value=173:127792, second_product=346:4112, answer=374:4783)
- Layer 41: ` .`, ` .↵↵`, `我没有`, ` .↵`, `我已经` (target ranks: base_value=97:126862, first_product=194:113146, bound_value=173:117586, second_product=346:25539, answer=374:19997)

### Filler position 2 (absolute token 677, surface ` .`)

- Layer 0: `aplenty`, `尷`, `?datasetId`, `�乐`, `-ulo` (target ranks: base_value=97:119766, first_product=194:114166, bound_value=173:116772, second_product=346:118861, answer=374:117536)
- Layer 10: ` Walker`, `ait`, `Walker`, `从哪里`, `atile` (target ranks: base_value=97:29866, first_product=194:36079, bound_value=173:44631, second_product=346:32528, answer=374:38780)
- Layer 20: ` .`, ` .----`, `往常`, `小男孩`, `小女孩` (target ranks: base_value=97:122088, first_product=194:111512, bound_value=173:126061, second_product=346:91920, answer=374:118024)
- Layer 30: `}<?`, `?datasetId`, ` pakig`, ` الشعاعيه`, ` Nij` (target ranks: base_value=97:96181, first_product=194:61532, bound_value=173:94546, second_product=346:82901, answer=374:72734)
- Layer 35: `翻`, ` dekameters`, ` Ric`, `opan`, `Ric` (target ranks: base_value=97:111074, first_product=194:14010, bound_value=173:109948, second_product=346:180, answer=374:1661)
- Layer 36: ` Nij`, `翻`, `376`, `三百`, `372` (target ranks: base_value=97:125629, first_product=194:69240, bound_value=173:89149, second_product=346:675, answer=374:42)
- Layer 37: ` hydrodynamic`, `}<?`, `?datasetId`, `زياح`, `aplenty` (target ranks: base_value=97:127234, first_product=194:88769, bound_value=173:97583, second_product=346:5485, answer=374:246)
- Layer 38: `}<?`, ` dekameters`, ` hydrodynamic`, `为人`, `oraly` (target ranks: base_value=97:128328, first_product=194:92959, bound_value=173:108945, second_product=346:729, answer=374:26)
- Layer 39: `}<?`, ` hydrodynamic`, ` Millenniums`, `三百`, `势力的` (target ranks: base_value=97:128602, first_product=194:115909, bound_value=173:127902, second_product=346:8326, answer=374:68)
- Layer 40: ` ald`, ` talags`, ` dekameters`, ` Erkännande`, `三百` (target ranks: base_value=97:128692, first_product=194:125227, bound_value=173:126916, second_product=346:5012, answer=374:634)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` nuest`, `翻` (target ranks: base_value=97:127915, first_product=194:115679, bound_value=173:121730, second_product=346:25800, answer=374:4349)

### Filler position 3 (absolute token 678, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123255, first_product=194:115741, bound_value=173:117793, second_product=346:121331, answer=374:119841)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: base_value=97:15337, first_product=194:25491, bound_value=173:27147, second_product=346:23656, answer=374:26833)
- Layer 20: `ait`, `cape`, `锁定`, `足`, ` ternary` (target ranks: base_value=97:8427, first_product=194:11917, bound_value=173:26755, second_product=346:18952, answer=374:20366)
- Layer 30: `进行计算`, `计算的`, `calcul`, `计算`, ` calcul` (target ranks: base_value=97:29387, first_product=194:32055, bound_value=173:111445, second_product=346:104385, answer=374:100041)
- Layer 35: ` Step`, `calcul`, ` calculations`, `第一步`, ` let` (target ranks: base_value=97:5029, first_product=194:16537, bound_value=173:86734, second_product=346:62151, answer=374:67709)
- Layer 36: `calcul`, `计算的`, ` calculations`, ` let`, `计算` (target ranks: base_value=97:9644, first_product=194:27167, bound_value=173:85821, second_product=346:64622, answer=374:77338)
- Layer 37: `}<?`, `calcul`, ` calcul`, ` Step`, `计算的` (target ranks: base_value=97:45284, first_product=194:45510, bound_value=173:104848, second_product=346:99380, answer=374:107859)
- Layer 38: `}<?`, ` cál`, `calcul`, ` calcul`, ` calculations` (target ranks: base_value=97:60779, first_product=194:52542, bound_value=173:111448, second_product=346:105087, answer=374:106501)
- Layer 39: `}<?`, `文字的`, `ilos`, `ucl`, `tanle` (target ranks: base_value=97:124367, first_product=194:125621, bound_value=173:126235, second_product=346:122758, answer=374:124060)
- Layer 40: `ilos`, `oooo`, `留存`, `语言文字`, ` последова` (target ranks: base_value=97:118927, first_product=194:126829, bound_value=173:124475, second_product=346:124372, answer=374:122583)
- Layer 41: ` .`, ` let`, `<｜end▁of▁sentence｜>`, ` .↵↵`, `人民群众` (target ranks: base_value=97:95924, first_product=194:114443, bound_value=173:104544, second_product=346:93253, answer=374:90708)

### Filler position 4 (absolute token 679, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:123822, first_product=194:117702, bound_value=173:118577, second_product=346:122440, answer=374:121434)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `挪` (target ranks: base_value=97:13350, first_product=194:24270, bound_value=173:24679, second_product=346:20866, answer=374:25663)
- Layer 20: `能被`, `忑`, `ait`, ` LS`, `幽` (target ranks: base_value=97:14769, first_product=194:27841, bound_value=173:48595, second_product=346:23560, answer=374:29406)
- Layer 30: `反复`, ` Subtract`, ` repetitions`, ` subtract`, `amic` (target ranks: base_value=97:6, first_product=194:6604, bound_value=173:247, second_product=346:4430, answer=374:16837)
- Layer 35: `346`, `345`, `347`, ` kinaug`, `nica` (target ranks: base_value=97:78040, first_product=194:64328, bound_value=173:127, second_product=346:1, answer=374:44937)
- Layer 36: `346`, `膝`, `Giya`, `aplenty`, ` Epic` (target ranks: base_value=97:126606, first_product=194:122301, bound_value=173:46, second_product=346:1, answer=374:67556)
- Layer 37: `346`, `Giya`, `膝`, `aplenty`, `攀` (target ranks: base_value=97:128482, first_product=194:122667, bound_value=173:81, second_product=346:1, answer=374:86037)
- Layer 38: `346`, ` Epic`, `膝`, `绳子`, ` Lama` (target ranks: base_value=97:128956, first_product=194:127251, bound_value=173:210, second_product=346:1, answer=374:100081)
- Layer 39: `346`, `codeline`, ` macOS`, `ozygous`, ` sumala` (target ranks: base_value=97:128539, first_product=194:126120, bound_value=173:21998, second_product=346:1, answer=374:115251)
- Layer 40: `ascals`, `346`, `scribe`, `花儿`, `inking` (target ranks: base_value=97:128679, first_product=194:127373, bound_value=173:86688, second_product=346:2, answer=374:108123)
- Layer 41: `346`, `的计算`, `ascals`, `沛`, ` .` (target ranks: base_value=97:128021, first_product=194:123750, bound_value=173:61549, second_product=346:1, answer=374:69271)

### Filler position 5 (absolute token 680, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:123539, first_product=194:118001, bound_value=173:118632, second_product=346:122391, answer=374:121512)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=97:16293, first_product=194:28151, bound_value=173:27823, second_product=346:23576, answer=374:29161)
- Layer 20: `幽`, ` LS`, `啦啦`, `锁定`, `足` (target ranks: base_value=97:26065, first_product=194:28997, bound_value=173:35829, second_product=346:23069, answer=374:27561)
- Layer 30: ` NO`, ` No`, `诺`, ` Nova`, `N` (target ranks: base_value=97:10945, first_product=194:67805, bound_value=173:112405, second_product=346:104637, answer=374:40656)
- Layer 35: ` NO`, `诺`, ` No`, `�`, `N` (target ranks: base_value=97:5439, first_product=194:69756, bound_value=173:104001, second_product=346:95682, answer=374:45878)
- Layer 36: `反复`, `�`, `coding`, `诺`, ` NO` (target ranks: base_value=97:12249, first_product=194:71014, bound_value=173:104394, second_product=346:78191, answer=374:35305)
- Layer 37: `wof`, ` Naf`, ` Nij`, ` NOK`, `覆` (target ranks: base_value=97:24679, first_product=194:77673, bound_value=173:112700, second_product=346:104832, answer=374:42379)
- Layer 38: `覆`, ` Noruwega`, `wof`, `东海`, `polar` (target ranks: base_value=97:28840, first_product=194:72306, bound_value=173:102328, second_product=346:96277, answer=374:58545)
- Layer 39: ` Noruwega`, ` Nog`, `覆`, ` Naf`, ` Nij` (target ranks: base_value=97:99350, first_product=194:119149, bound_value=173:122982, second_product=346:120690, answer=374:93524)
- Layer 40: ` talags`, `n`, ` nasod`, `hemer`, `duc` (target ranks: base_value=97:77707, first_product=194:109769, bound_value=173:108444, second_product=346:98538, answer=374:45668)
- Layer 41: ` .`, `鹉`, `悬念`, ` enclosing`, `我没有` (target ranks: base_value=97:35225, first_product=194:73040, bound_value=173:51933, second_product=346:49454, answer=374:10394)

### Filler position 6 (absolute token 681, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=97:123040, first_product=194:117552, bound_value=173:118390, second_product=346:122214, answer=374:121092)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, ` cheer` (target ranks: base_value=97:14397, first_product=194:25899, bound_value=173:25386, second_product=346:21843, answer=374:26594)
- Layer 20: `<｜begin▁of▁file｜>`, ` unflagged`, ` corrected`, `计算方法`, ` 계산` (target ranks: base_value=97:95870, first_product=194:90292, bound_value=173:98663, second_product=346:110573, answer=374:71673)
- Layer 30: `<｜begin▁of▁file｜>`, `一步步`, `先将`, ` step`, `推算` (target ranks: base_value=97:74080, first_product=194:60213, bound_value=173:97542, second_product=346:124345, answer=374:95781)
- Layer 35: `<｜begin▁of▁file｜>`, `acks`, ` step`, ` Tw`, ` Step` (target ranks: base_value=97:76756, first_product=194:50929, bound_value=173:107077, second_product=346:119597, answer=374:91758)
- Layer 36: ` Tw`, ` repeated`, ` tw`, ` stretch`, `反复` (target ranks: base_value=97:47737, first_product=194:39445, bound_value=173:93490, second_product=346:96510, answer=374:77716)
- Layer 37: ` Tw`, ` nasod`, `展开`, ` step`, ` Calculators` (target ranks: base_value=97:88158, first_product=194:59957, bound_value=173:117189, second_product=346:119646, answer=374:110910)
- Layer 38: ` Tw`, ` nasod`, `漂`, ` tw`, ` Calculators` (target ranks: base_value=97:92426, first_product=194:66155, bound_value=173:116448, second_product=346:123298, answer=374:119357)
- Layer 39: `树叶`, ` nasod`, `无言`, `叶子`, `ozygous` (target ranks: base_value=97:127363, first_product=194:127385, bound_value=173:126105, second_product=346:126150, answer=374:125974)
- Layer 40: ` Tw`, ` nasod`, `乐乐`, `.tw`, ` dots` (target ranks: base_value=97:123678, first_product=194:127374, bound_value=173:124690, second_product=346:121873, answer=374:122255)
- Layer 41: `<｜begin▁of▁file｜>`, `<｜begin▁of▁sentence｜>`, ` dots`, `乐乐`, ` dotted` (target ranks: base_value=97:122811, first_product=194:127192, bound_value=173:126143, second_product=346:119894, answer=374:117431)

### Filler position 7 (absolute token 682, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122889, first_product=194:117276, bound_value=173:118297, second_product=346:122067, answer=374:120857)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13683, first_product=194:25122, bound_value=173:24888, second_product=346:21240, answer=374:27000)
- Layer 20: `ait`, `忑`, `锁定`, `挪`, `能被` (target ranks: base_value=97:12567, first_product=194:27782, bound_value=173:35115, second_product=346:19663, answer=374:27758)
- Layer 30: ` pakig`, ` talags`, `七十二`, `66`, `328` (target ranks: base_value=97:3866, first_product=194:750, bound_value=173:1027, second_product=346:1708, answer=374:1341)
- Layer 35: `346`, `345`, `376`, `348`, `366` (target ranks: base_value=97:88999, first_product=194:589, bound_value=173:32918, second_product=346:1, answer=374:15)
- Layer 36: `376`, `374`, `370`, `372`, `366` (target ranks: base_value=97:114455, first_product=194:64497, bound_value=173:11071, second_product=346:18, answer=374:2)
- Layer 37: `376`, `374`, `366`, `373`, `375` (target ranks: base_value=97:117636, first_product=194:59234, bound_value=173:13914, second_product=346:20, answer=374:2)
- Layer 38: `374`, `376`, `366`, `375`, `372` (target ranks: base_value=97:128856, first_product=194:107926, bound_value=173:88522, second_product=346:40, answer=374:1)
- Layer 39: `374`, `372`, `376`, `375`, `370` (target ranks: base_value=97:129010, first_product=194:98067, bound_value=173:128976, second_product=346:1680, answer=374:1)
- Layer 40: `374`, `372`, `376`, ` talags`, `370` (target ranks: base_value=97:128745, first_product=194:117799, bound_value=173:127155, second_product=346:640, answer=374:1)
- Layer 41: `374`, ` nuest`, `376`, `372`, `375` (target ranks: base_value=97:127434, first_product=194:94112, bound_value=173:123070, second_product=346:5691, answer=374:1)

### Filler position 8 (absolute token 683, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:122976, first_product=194:117310, bound_value=173:118547, second_product=346:122181, answer=374:120885)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13816, first_product=194:25962, bound_value=173:26146, second_product=346:21596, answer=374:27802)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=97:15514, first_product=194:28250, bound_value=173:37531, second_product=346:21465, answer=374:28613)
- Layer 30: `acos`, `平行`, `Tap`, `输入的`, ` parallel` (target ranks: base_value=97:33964, first_product=194:60073, bound_value=173:110805, second_product=346:88318, answer=374:67171)
- Layer 35: `Tap`, ` tap`, `留存`, `羊`, `保留` (target ranks: base_value=97:14441, first_product=194:28205, bound_value=173:77475, second_product=346:51913, answer=374:47796)
- Layer 36: `留存`, ` dri`, ` tap`, ` valore`, `Tap` (target ranks: base_value=97:21732, first_product=194:31641, bound_value=173:83883, second_product=346:44728, answer=374:36683)
- Layer 37: `}<?`, `覆`, `acos`, ` polar`, `ота` (target ranks: base_value=97:51153, first_product=194:45272, bound_value=173:110401, second_product=346:77040, answer=374:60116)
- Layer 38: `}<?`, `zat`, `覆`, `aje`, `acons` (target ranks: base_value=97:69376, first_product=194:71957, bound_value=173:117356, second_product=346:79866, answer=374:76446)
- Layer 39: `}<?`, `zat`, `acons`, `覆`, `本题分析` (target ranks: base_value=97:111430, first_product=194:102459, bound_value=173:119334, second_product=346:99351, answer=374:85173)
- Layer 40: `šk`, `留存`, `zij`, `oz`, `scr` (target ranks: base_value=97:84052, first_product=194:100876, bound_value=173:108807, second_product=346:83729, answer=374:57957)
- Layer 41: `鹉`, ` .`, `oz`, `šk`, ` ` (target ranks: base_value=97:37374, first_product=194:83849, bound_value=173:93731, second_product=346:54285, answer=374:19021)

### Filler position 9 (absolute token 684, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123151, first_product=194:117345, bound_value=173:118788, second_product=346:122372, answer=374:120987)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:14102, first_product=194:25998, bound_value=173:26460, second_product=346:21924, answer=374:27735)
- Layer 20: `锁定`, `ait`, ` Walker`, ` smile`, `Walker` (target ranks: base_value=97:18629, first_product=194:28588, bound_value=173:37561, second_product=346:21750, answer=374:28242)
- Layer 30: ` Tw`, ` repetitions`, `Tap`, `Tw`, ` tap` (target ranks: base_value=97:50336, first_product=194:58373, bound_value=173:95822, second_product=346:81080, answer=374:66357)
- Layer 35: `Tap`, ` Tw`, ` tap`, ` Tap`, `Tw` (target ranks: base_value=97:32950, first_product=194:27003, bound_value=173:75168, second_product=346:64394, answer=374:49295)
- Layer 36: ` tap`, `Tap`, ` equations`, `acos`, ` Tap` (target ranks: base_value=97:33743, first_product=194:32096, bound_value=173:78121, second_product=346:62583, answer=374:41421)
- Layer 37: `}<?`, `acos`, `筋`, `语言文字`, `któber` (target ranks: base_value=97:80509, first_product=194:52874, bound_value=173:108229, second_product=346:97770, answer=374:72898)
- Layer 38: `}<?`, `筋`, `冰冰`, `覆`, `枝叶` (target ranks: base_value=97:95964, first_product=194:62413, bound_value=173:112763, second_product=346:89703, answer=374:84648)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `语言文字`, `树叶`, `acons` (target ranks: base_value=97:116477, first_product=194:104655, bound_value=173:110944, second_product=346:101914, answer=374:93409)
- Layer 40: `amn`, `šk`, `留存`, `下沉`, `冰冰` (target ranks: base_value=97:87961, first_product=194:95912, bound_value=173:75408, second_product=346:92358, answer=374:76272)
- Layer 41: ` .`, ` repeated`, `aaaaaaaa`, `语言文字`, ` ` (target ranks: base_value=97:61566, first_product=194:80841, bound_value=173:63762, second_product=346:74731, answer=374:44217)

### Filler position 10 (absolute token 685, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123122, first_product=194:117585, bound_value=173:119185, second_product=346:122457, answer=374:121171)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `挪` (target ranks: base_value=97:13057, first_product=194:24524, bound_value=173:24748, second_product=346:20789, answer=374:26688)
- Layer 20: ` Walker`, `Walker`, `锁定`, `ait`, ` smile` (target ranks: base_value=97:26327, first_product=194:38354, bound_value=173:36429, second_product=346:22644, answer=374:33684)
- Layer 30: ` Tw`, `询问`, `提问`, `Tw`, ` question` (target ranks: base_value=97:37031, first_product=194:54029, bound_value=173:82359, second_product=346:51555, answer=374:44978)
- Layer 35: `询问`, ` Tw`, `提问`, `Tw`, ` question` (target ranks: base_value=97:18847, first_product=194:22681, bound_value=173:60082, second_product=346:28823, answer=374:34227)
- Layer 36: `询问`, `提问`, ` question`, `質問`, ` Question` (target ranks: base_value=97:23801, first_product=194:23596, bound_value=173:73072, second_product=346:29662, answer=374:28248)
- Layer 37: `提问`, ` question`, `.question`, `}<?`, `質問` (target ranks: base_value=97:61084, first_product=194:44098, bound_value=173:107300, second_product=346:64889, answer=374:56224)
- Layer 38: `}<?`, `asking`, `覆`, `鹦鹉`, `zat` (target ranks: base_value=97:65401, first_product=194:49950, bound_value=173:106073, second_product=346:65891, answer=374:64232)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `ellationToken`, `东海`, `ozygous` (target ranks: base_value=97:102105, first_product=194:81217, bound_value=173:112052, second_product=346:80083, answer=374:77739)
- Layer 40: `ellationToken`, `šk`, ` Tw`, ` repeated`, `}<?` (target ranks: base_value=97:82994, first_product=194:57883, bound_value=173:77264, second_product=346:67576, answer=374:47890)
- Layer 41: ` .`, `鹉`, ` ativid`, ` repeated`, ` without` (target ranks: base_value=97:32203, first_product=194:28773, bound_value=173:36572, second_product=346:34084, answer=374:13826)

### Filler position 11 (absolute token 686, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123095, first_product=194:117752, bound_value=173:119347, second_product=346:122679, answer=374:121308)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13438, first_product=194:26721, bound_value=173:25692, second_product=346:21764, answer=374:27026)
- Layer 20: `ait`, ` Walker`, `锁定`, `cape`, `能被` (target ranks: base_value=97:17402, first_product=194:34917, bound_value=173:34449, second_product=346:22601, answer=374:32844)
- Layer 30: ` rip`, ` consum`, `zim`, ` Zad`, `�` (target ranks: base_value=97:62479, first_product=194:109662, bound_value=173:124311, second_product=346:100952, answer=374:82251)
- Layer 35: `Tap`, `zim`, ` tap`, ` Tap`, `Rot` (target ranks: base_value=97:35350, first_product=194:85016, bound_value=173:112338, second_product=346:93257, answer=374:85159)
- Layer 36: `zim`, ` zad`, ` tap`, `溃`, `Tap` (target ranks: base_value=97:33649, first_product=194:63583, bound_value=173:96451, second_product=346:48082, answer=374:55345)
- Layer 37: `zim`, `斐`, `zos`, `zam`, `zat` (target ranks: base_value=97:74933, first_product=194:84106, bound_value=173:113094, second_product=346:85030, answer=374:72108)
- Layer 38: `zat`, `zos`, `}<?`, `�`, `斐` (target ranks: base_value=97:90351, first_product=194:95237, bound_value=173:117828, second_product=346:98209, answer=374:93748)
- Layer 39: `斐`, `zat`, `�`, ` Nij`, ` Lent` (target ranks: base_value=97:111185, first_product=194:103053, bound_value=173:115110, second_product=346:72952, answer=374:51558)
- Layer 40: `zim`, `zat`, ` decom`, `zel`, `heer` (target ranks: base_value=97:105655, first_product=194:101813, bound_value=173:97108, second_product=346:47063, answer=374:26087)
- Layer 41: ` Question`, ` mim`, `zel`, `Question`, `�` (target ranks: base_value=97:42409, first_product=194:48242, bound_value=173:51572, second_product=346:8326, answer=374:7324)

### Filler position 12 (absolute token 687, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123034, first_product=194:117758, bound_value=173:119251, second_product=346:122612, answer=374:121173)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12726, first_product=194:26272, bound_value=173:25023, second_product=346:21077, answer=374:26278)
- Layer 20: `ait`, ` smile`, ` wig`, ` ES`, `锁定` (target ranks: base_value=97:15695, first_product=194:33490, bound_value=173:30128, second_product=346:21151, answer=374:30327)
- Layer 30: ` tap`, `Tap`, `tap`, ` Tap`, `提问` (target ranks: base_value=97:52976, first_product=194:75595, bound_value=173:89845, second_product=346:75063, answer=374:41093)
- Layer 35: ` tap`, ` rip`, `幼`, `Tap`, `小青` (target ranks: base_value=97:55067, first_product=194:70264, bound_value=173:77631, second_product=346:64736, answer=374:34108)
- Layer 36: ` rip`, ` tap`, ` dynam`, `acl`, `agia` (target ranks: base_value=97:37533, first_product=194:66830, bound_value=173:63157, second_product=346:39718, answer=374:27486)
- Layer 37: ` dynam`, ` rip`, `acl`, `覆`, `}<?` (target ranks: base_value=97:91969, first_product=194:93225, bound_value=173:83918, second_product=346:65956, answer=374:54054)
- Layer 38: `}<?`, `acons`, `dividers`, `�`, `ozygous` (target ranks: base_value=97:107977, first_product=194:111442, bound_value=173:101252, second_product=346:78151, answer=374:74952)
- Layer 39: `}<?`, `dividers`, `script`, `romes`, `东海` (target ranks: base_value=97:122648, first_product=194:116228, bound_value=173:104280, second_product=346:65676, answer=374:37244)
- Layer 40: ` kinahabogang`, `acl`, `的计算`, `词语`, `步骤如下` (target ranks: base_value=97:106794, first_product=194:99840, bound_value=173:87742, second_product=346:35927, answer=374:2961)
- Layer 41: `试一试`, `Answer`, `Question`, `步骤如下`, `Explanation` (target ranks: base_value=97:74807, first_product=194:72564, bound_value=173:44875, second_product=346:16314, answer=374:254)

### Filler position 13 (absolute token 688, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123055, first_product=194:117846, bound_value=173:119442, second_product=346:122775, answer=374:121342)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=97:14237, first_product=194:26446, bound_value=173:25841, second_product=346:22413, answer=374:27703)
- Layer 20: `忑`, ` engaging`, `锁定`, ` Walker`, `ait` (target ranks: base_value=97:29382, first_product=194:44555, bound_value=173:53402, second_product=346:32957, answer=374:44584)
- Layer 30: `zuk`, ` pakig`, `yak`, `zung`, `第一步` (target ranks: base_value=97:55527, first_product=194:83230, bound_value=173:115863, second_product=346:110234, answer=374:82264)
- Layer 35: `zuk`, ` tap`, ` zad`, `zung`, ` Z` (target ranks: base_value=97:37645, first_product=194:47958, bound_value=173:99993, second_product=346:85031, answer=374:47519)
- Layer 36: `留存`, ` tap`, `年开始`, `zuk`, ` start` (target ranks: base_value=97:41779, first_product=194:47618, bound_value=173:91447, second_product=346:76832, answer=374:44464)
- Layer 37: `}<?`, `zuk`, `覆`, `ukkan`, ` pakig` (target ranks: base_value=97:95123, first_product=194:84286, bound_value=173:121862, second_product=346:111752, answer=374:84628)
- Layer 38: `}<?`, `zuk`, `zat`, ` z`, `覆` (target ranks: base_value=97:101008, first_product=194:102657, bound_value=173:125441, second_product=346:105922, answer=374:98162)
- Layer 39: `zat`, `}<?`, ` z`, `zos`, `𝑧` (target ranks: base_value=97:119898, first_product=194:116464, bound_value=173:125331, second_product=346:111275, answer=374:103165)
- Layer 40: ` z`, ` Z`, `z`, `zos`, `zij` (target ranks: base_value=97:109203, first_product=194:119391, bound_value=173:117611, second_product=346:92959, answer=374:80654)
- Layer 41: ` .`, `鹉`, `出不穷`, `翻`, `zza` (target ranks: base_value=97:73381, first_product=194:69726, bound_value=173:77720, second_product=346:55625, answer=374:39900)

### Filler position 14 (absolute token 689, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123260, first_product=194:117919, bound_value=173:119721, second_product=346:122979, answer=374:121464)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12393, first_product=194:23922, bound_value=173:24293, second_product=346:20526, answer=374:24959)
- Layer 20: `ait`, `锁定`, ` Walker`, `会成为`, ` engaging` (target ranks: base_value=97:26697, first_product=194:33053, bound_value=173:47755, second_product=346:27084, answer=374:45043)
- Layer 30: `zuk`, ` step`, `第一步`, ` Zu`, ` Zad` (target ranks: base_value=97:48864, first_product=194:84771, bound_value=173:124195, second_product=346:113377, answer=374:107975)
- Layer 35: `zuk`, ` step`, `asuk`, ` zad`, ` ز` (target ranks: base_value=97:36705, first_product=194:47967, bound_value=173:114664, second_product=346:86645, answer=374:68763)
- Layer 36: `zuk`, `留存`, `ikuha`, `calcul`, ` zad` (target ranks: base_value=97:48659, first_product=194:57989, bound_value=173:113502, second_product=346:82594, answer=374:78635)
- Layer 37: `}<?`, `zuk`, `ukkan`, ` zav`, `本题分析` (target ranks: base_value=97:105420, first_product=194:88809, bound_value=173:125420, second_product=346:111389, answer=374:101516)
- Layer 38: `}<?`, `?datasetId`, `zat`, `ukkan`, `本题分析` (target ranks: base_value=97:106381, first_product=194:100528, bound_value=173:126262, second_product=346:112524, answer=374:109131)
- Layer 39: `}<?`, `zat`, `?datasetId`, `ziako`, `zv` (target ranks: base_value=97:118917, first_product=194:112587, bound_value=173:125367, second_product=346:104919, answer=374:98808)
- Layer 40: `calcul`, ` calculations`, `zos`, `变量的`, ` zad` (target ranks: base_value=97:101123, first_product=194:111665, bound_value=173:117490, second_product=346:85905, answer=374:70458)
- Layer 41: ` calculations`, ` Calculators`, ` Calculations`, `鹉`, `šk` (target ranks: base_value=97:43638, first_product=194:48535, bound_value=173:82777, second_product=346:27270, answer=374:24908)

### Filler position 15 (absolute token 690, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123484, first_product=194:118112, bound_value=173:119947, second_product=346:123090, answer=374:121560)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:12617, first_product=194:24246, bound_value=173:24895, second_product=346:20719, answer=374:24806)
- Layer 20: `锁定`, `ait`, ` Walker`, `会成为`, `而此时` (target ranks: base_value=97:16947, first_product=194:25343, bound_value=173:38640, second_product=346:22673, answer=374:29724)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=97:32172, first_product=194:56744, bound_value=173:100961, second_product=346:64626, answer=374:67550)
- Layer 35: ` Tw`, `Tw`, `tw`, `.tw`, ` twice` (target ranks: base_value=97:11266, first_product=194:29236, bound_value=173:80746, second_product=346:55790, answer=374:56612)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=97:10482, first_product=194:34452, bound_value=173:88691, second_product=346:70424, answer=374:58084)
- Layer 37: `}<?`, ` Tw`, `Tw`, `计算的`, ` twist` (target ranks: base_value=97:39201, first_product=194:63107, bound_value=173:117922, second_product=346:109435, answer=374:90673)
- Layer 38: `}<?`, ` Tw`, ` twist`, `Tw`, `interpret` (target ranks: base_value=97:57693, first_product=194:75091, bound_value=173:121974, second_product=346:113688, answer=374:101124)
- Layer 39: `}<?`, `interpret`, `覆`, `东海`, ` Fylke` (target ranks: base_value=97:79157, first_product=194:97614, bound_value=173:121612, second_product=346:112240, answer=374:97046)
- Layer 40: ` follow`, `覆`, `的计算`, `zij`, `计算的` (target ranks: base_value=97:31530, first_product=194:85120, bound_value=173:100187, second_product=346:110405, answer=374:81270)
- Layer 41: `的计算`, ` follow`, `步骤如下`, ` .`, `zij` (target ranks: base_value=97:15348, first_product=194:79929, bound_value=173:83554, second_product=346:93280, answer=374:45921)

### Filler position 16 (absolute token 691, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123311, first_product=194:117960, bound_value=173:119948, second_product=346:123154, answer=374:121530)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13699, first_product=194:24844, bound_value=173:24733, second_product=346:20501, answer=374:25317)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, `挪` (target ranks: base_value=97:11891, first_product=194:26321, bound_value=173:31881, second_product=346:17377, answer=374:22114)
- Layer 30: `反复`, ` repetitions`, ` repeated`, ` repetition`, `重复` (target ranks: base_value=97:100, first_product=194:3848, bound_value=173:18, second_product=346:864, answer=374:6932)
- Layer 35: `346`, `347`, `345`, `344`, `348` (target ranks: base_value=97:84048, first_product=194:38890, bound_value=173:7, second_product=346:1, answer=374:3411)
- Layer 36: `346`, `347`, `345`, `173`, ` Lambda` (target ranks: base_value=97:127164, first_product=194:110968, bound_value=173:4, second_product=346:1, answer=374:12523)
- Layer 37: `346`, `347`, `345`, ` Lambda`, `Lambda` (target ranks: base_value=97:128857, first_product=194:112863, bound_value=173:7, second_product=346:1, answer=374:15960)
- Layer 38: `346`, `347`, `345`, ` Epic`, `膝` (target ranks: base_value=97:129036, first_product=194:120797, bound_value=173:8, second_product=346:1, answer=374:27710)
- Layer 39: `346`, `347`, ` sumala`, `345`, `瞿` (target ranks: base_value=97:128379, first_product=194:124737, bound_value=173:1572, second_product=346:1, answer=374:107039)
- Layer 40: `346`, `iator`, `思`, `ponen`, `scribe` (target ranks: base_value=97:128433, first_product=194:127428, bound_value=173:104119, second_product=346:1, answer=374:91356)
- Layer 41: `346`, `可以先`, `可以向`, `的计算`, `我也想` (target ranks: base_value=97:126105, first_product=194:126324, bound_value=173:92209, second_product=346:1, answer=374:79263)

### Filler position 17 (absolute token 692, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123584, first_product=194:118371, bound_value=173:120326, second_product=346:123451, answer=374:121865)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:17596, first_product=194:27869, bound_value=173:28972, second_product=346:23866, answer=374:30373)
- Layer 20: `锁定`, `能被`, `ait`, ` Walker`, `而此时` (target ranks: base_value=97:15796, first_product=194:27613, bound_value=173:29308, second_product=346:17179, answer=374:22955)
- Layer 30: `反复`, ` twice`, ` repetitions`, `夫人`, `柿子` (target ranks: base_value=97:401, first_product=194:9087, bound_value=173:9934, second_product=346:4856, answer=374:5921)
- Layer 35: `328`, `柿子`, `304`, ` retreat`, `翻` (target ranks: base_value=97:3187, first_product=194:4980, bound_value=173:36736, second_product=346:11, answer=374:552)
- Layer 36: `翻`, `柿子`, `328`, `翻了`, ` retreat` (target ranks: base_value=97:36653, first_product=194:25634, bound_value=173:72117, second_product=346:28, answer=374:727)
- Layer 37: `}<?`, `翻了`, `翻`, `覆`, `�` (target ranks: base_value=97:96189, first_product=194:50785, bound_value=173:82435, second_product=346:225, answer=374:2643)
- Layer 38: `}<?`, `覆`, `东海`, `�`, `翻了` (target ranks: base_value=97:113110, first_product=194:68757, bound_value=173:100788, second_product=346:1684, answer=374:9452)
- Layer 39: `}<?`, `三百`, `东海`, `第三百`, `覆` (target ranks: base_value=97:126609, first_product=194:104829, bound_value=173:108589, second_product=346:309, answer=374:2257)
- Layer 40: `三百`, `翻`, ` `, `第三百`, `坏` (target ranks: base_value=97:124276, first_product=194:97446, bound_value=173:79029, second_product=346:6, answer=374:120)
- Layer 41: ` .`, ` `, `第三百`, `翻`, ` .↵↵` (target ranks: base_value=97:112356, first_product=194:79255, bound_value=173:71407, second_product=346:27, answer=374:191)

### Filler position 18 (absolute token 693, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=97:123646, first_product=194:118514, bound_value=173:120527, second_product=346:123732, answer=374:122045)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:14535, first_product=194:25985, bound_value=173:27171, second_product=346:22417, answer=374:28402)
- Layer 20: `忑`, `ait`, ` Walker`, `锁定`, `能被` (target ranks: base_value=97:21584, first_product=194:30665, bound_value=173:38838, second_product=346:27085, answer=374:36611)
- Layer 30: ` NO`, ` Nog`, ` No`, `NO`, `诺` (target ranks: base_value=97:6264, first_product=194:75308, bound_value=173:122659, second_product=346:98824, answer=374:90699)
- Layer 35: ` NO`, `诺`, ` noc`, `NO`, ` No` (target ranks: base_value=97:1000, first_product=194:40916, bound_value=173:97433, second_product=346:54048, answer=374:55044)
- Layer 36: `留存`, `期望`, ` Nog`, `noj`, ` hoof` (target ranks: base_value=97:1206, first_product=194:41213, bound_value=173:101601, second_product=346:43841, answer=374:57792)
- Layer 37: `}<?`, ` Nog`, `rof`, `不急`, `ofer` (target ranks: base_value=97:5428, first_product=194:65712, bound_value=173:116008, second_product=346:74308, answer=374:72301)
- Layer 38: `}<?`, ` Nog`, `覆`, `ofer`, `不大` (target ranks: base_value=97:10672, first_product=194:67421, bound_value=173:105730, second_product=346:65643, answer=374:78653)
- Layer 39: ` Nog`, ` Noruwega`, `覆`, `}<?`, ` NO` (target ranks: base_value=97:76782, first_product=194:107797, bound_value=173:122354, second_product=346:81581, answer=374:81485)
- Layer 40: `zij`, `zat`, `下沉`, `无`, `acular` (target ranks: base_value=97:59460, first_product=194:94670, bound_value=173:104943, second_product=346:31365, answer=374:36672)
- Layer 41: ` .`, `acular`, `zl`, `zij`, ` waiting` (target ranks: base_value=97:15189, first_product=194:62044, bound_value=173:49179, second_product=346:5659, answer=374:2858)

### Filler position 19 (absolute token 694, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124020, first_product=194:118816, bound_value=173:120790, second_product=346:123873, answer=374:122182)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13453, first_product=194:25791, bound_value=173:26801, second_product=346:22484, answer=374:27602)
- Layer 20: `忑`, `会成为`, ` engaging`, `ait`, `平行` (target ranks: base_value=97:29508, first_product=194:47776, bound_value=173:63435, second_product=346:49553, answer=374:53857)
- Layer 30: ` repetition`, ` repetitions`, `题库`, ` exercises`, ` sequential` (target ranks: base_value=97:38126, first_product=194:65518, bound_value=173:88037, second_product=346:83157, answer=374:83637)
- Layer 35: ` var`, ` exercises`, ` repetition`, `题库`, `重复` (target ranks: base_value=97:19113, first_product=194:32526, bound_value=173:57732, second_product=346:45230, answer=374:43768)
- Layer 36: ` var`, `重复`, `柿子`, `前后的`, ` exercises` (target ranks: base_value=97:13961, first_product=194:35705, bound_value=173:55158, second_product=346:37907, answer=374:39316)
- Layer 37: `}<?`, `变量的`, ` variable`, ` variables`, ` var` (target ranks: base_value=97:36690, first_product=194:56343, bound_value=173:87057, second_product=346:74140, answer=374:58311)
- Layer 38: `}<?`, `不急`, ` labyrinth`, `下沉`, `acet` (target ranks: base_value=97:68448, first_product=194:69153, bound_value=173:90004, second_product=346:52561, answer=374:63575)
- Layer 39: `}<?`, `acons`, `下沉`, `<｜begin▁of▁sentence｜>`, `语言文字` (target ranks: base_value=97:106337, first_product=194:108103, bound_value=173:106623, second_product=346:74828, answer=374:89339)
- Layer 40: `下沉`, ` consum`, `}<?`, `šk`, `Tokens` (target ranks: base_value=97:69427, first_product=194:97010, bound_value=173:71323, second_product=346:68493, answer=374:65572)
- Layer 41: ` .`, `oooo`, `外商投资`, ` without`, ` ` (target ranks: base_value=97:36308, first_product=194:73277, bound_value=173:45450, second_product=346:28355, answer=374:26685)

### Filler position 20 (absolute token 695, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124224, first_product=194:119230, bound_value=173:121183, second_product=346:124111, answer=374:122582)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=97:13903, first_product=194:25279, bound_value=173:26620, second_product=346:21673, answer=374:27315)
- Layer 20: `ait`, `能被`, `锁定`, `会成为`, ` Walker` (target ranks: base_value=97:13816, first_product=194:18662, bound_value=173:34963, second_product=346:20602, answer=374:31246)
- Layer 30: ` talags`, `henera`, `}<?`, `?datasetId`, ` pakig` (target ranks: base_value=97:5996, first_product=194:488, bound_value=173:4274, second_product=346:1984, answer=374:2522)
- Layer 35: `346`, `345`, `348`, `344`, `347` (target ranks: base_value=97:59990, first_product=194:239, bound_value=173:32898, second_product=346:1, answer=374:22)
- Layer 36: `376`, `370`, `366`, `374`, `372` (target ranks: base_value=97:119626, first_product=194:46349, bound_value=173:27815, second_product=346:19, answer=374:4)
- Layer 37: `376`, `366`, `374`, `372`, `368` (target ranks: base_value=97:123250, first_product=194:62021, bound_value=173:43593, second_product=346:24, answer=374:3)
- Layer 38: `374`, `376`, `366`, `372`, `368` (target ranks: base_value=97:128482, first_product=194:92958, bound_value=173:106550, second_product=346:25, answer=374:1)
- Layer 39: `374`, `370`, `372`, `368`, `366` (target ranks: base_value=97:128568, first_product=194:92967, bound_value=173:128612, second_product=346:776, answer=374:1)
- Layer 40: `374`, `370`, `372`, `368`, `366` (target ranks: base_value=97:128701, first_product=194:100952, bound_value=173:127736, second_product=346:162, answer=374:1)
- Layer 41: ` nuest`, `374`, `因为这些`, `饪`, `<｜begin▁of▁file｜>` (target ranks: base_value=97:127053, first_product=194:79353, bound_value=173:126184, second_product=346:17532, answer=374:2)

### Filler position 21 (absolute token 696, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124432, first_product=194:119518, bound_value=173:121585, second_product=346:124425, answer=374:122866)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:14670, first_product=194:25121, bound_value=173:27023, second_product=346:21697, answer=374:28354)
- Layer 20: `俯`, ` spinner`, `平行`, `sl`, ` Tact` (target ranks: base_value=97:83835, first_product=194:41115, bound_value=173:94816, second_product=346:48537, answer=374:80904)
- Layer 30: ` spac`, `acos`, `}using`, ` baj`, `俯` (target ranks: base_value=97:90692, first_product=194:21768, bound_value=173:84391, second_product=346:49546, answer=374:62205)
- Layer 35: `滴水`, ` let`, `俯`, ` .`, ` dots` (target ranks: base_value=97:78387, first_product=194:46918, bound_value=173:87544, second_product=346:32161, answer=374:21187)
- Layer 36: `反复`, `调节`, `俯`, `滴水`, `ancock` (target ranks: base_value=97:39521, first_product=194:35622, bound_value=173:57512, second_product=346:17024, answer=374:15959)
- Layer 37: `}<?`, `滴滴`, `滴`, `dividers`, `isis` (target ranks: base_value=97:61868, first_product=194:52659, bound_value=173:63608, second_product=346:24497, answer=374:30113)
- Layer 38: ` .`, `}<?`, `坏`, ` hollow`, `滴滴` (target ranks: base_value=97:79169, first_product=194:32928, bound_value=173:75950, second_product=346:42323, answer=374:52960)
- Layer 39: `}<?`, ` .`, `<｜begin▁of▁sentence｜>`, `把事情`, `�` (target ranks: base_value=97:118467, first_product=194:82723, bound_value=173:107127, second_product=346:81944, answer=374:61918)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, `坏`, `�` (target ranks: base_value=97:90374, first_product=194:49969, bound_value=173:55854, second_product=346:43286, answer=374:27830)
- Layer 41: ` .`, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` `, ` .↵` (target ranks: base_value=97:27837, first_product=194:16429, bound_value=173:20175, second_product=346:17492, answer=374:5769)

### Filler position 22 (absolute token 697, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124455, first_product=194:119560, bound_value=173:121671, second_product=346:124431, answer=374:122892)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=97:13241, first_product=194:23836, bound_value=173:25810, second_product=346:20130, answer=374:26558)
- Layer 20: ` quadr`, ` smile`, `auce`, `cape`, ` sideways` (target ranks: base_value=97:18051, first_product=194:5841, bound_value=173:15359, second_product=346:4716, answer=374:15883)
- Layer 30: `?datasetId`, `封`, `陪`, `codeline`, `}<?` (target ranks: base_value=97:61173, first_product=194:10067, bound_value=173:11270, second_product=346:11048, answer=374:28128)
- Layer 35: `346`, `adaghan`, `345`, `366`, `386` (target ranks: base_value=97:100229, first_product=194:5050, bound_value=173:88804, second_product=346:1, answer=374:446)
- Layer 36: `370`, `366`, `386`, `372`, `374` (target ranks: base_value=97:119936, first_product=194:39234, bound_value=173:45022, second_product=346:13, answer=374:5)
- Layer 37: ` sabwag`, ` Bradford`, `ozygous`, `370`, `366` (target ranks: base_value=97:126178, first_product=194:47938, bound_value=173:74471, second_product=346:77, answer=374:13)
- Layer 38: `374`, ` Erl`, `366`, `370`, `轨迹` (target ranks: base_value=97:128570, first_product=194:109529, bound_value=173:116755, second_product=346:264, answer=374:1)
- Layer 39: `374`, `370`, `372`, `ozygous`, `慕` (target ranks: base_value=97:128431, first_product=194:101247, bound_value=173:128689, second_product=346:10785, answer=374:1)
- Layer 40: `ozygous`, `370`, `374`, ` .`, `crib` (target ranks: base_value=97:128535, first_product=194:109485, bound_value=173:128110, second_product=346:7132, answer=374:3)
- Layer 41: ` .`, `因为`, `�`, `Answer`, ` .↵↵` (target ranks: base_value=97:124870, first_product=194:76076, bound_value=173:117421, second_product=346:9665, answer=374:8)

### Filler position 23 (absolute token 698, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:124639, first_product=194:119723, bound_value=173:121858, second_product=346:124467, answer=374:122934)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=97:12673, first_product=194:24008, bound_value=173:26528, second_product=346:20664, answer=374:26238)
- Layer 20: `iganos`, `Dutch`, `leans`, ` Unc`, ` Dutch` (target ranks: base_value=97:68602, first_product=194:26338, bound_value=173:71353, second_product=346:39224, answer=374:37820)
- Layer 30: `codeline`, `东京`, `pac`, ` spac`, ` accompanying` (target ranks: base_value=97:111770, first_product=194:71755, bound_value=173:120279, second_product=346:112527, answer=374:93027)
- Layer 35: `codeline`, `坏`, ` nasod`, ` .↵↵`, ` doubly` (target ranks: base_value=97:114119, first_product=194:124193, bound_value=173:124824, second_product=346:122067, answer=374:102102)
- Layer 36: `兜`, ` nasod`, `坏`, ` soci`, ` Predict` (target ranks: base_value=97:88608, first_product=194:117300, bound_value=173:105755, second_product=346:102345, answer=374:85037)
- Layer 37: `肤`, `镶嵌`, `Quintal`, `悬挂`, `立德` (target ranks: base_value=97:120279, first_product=194:126526, bound_value=173:120034, second_product=346:118047, answer=374:102396)
- Layer 38: ` .`, `肤`, ` .↵↵`, `动`, ` dyn` (target ranks: base_value=97:116474, first_product=194:120896, bound_value=173:108454, second_product=346:112852, answer=374:110896)
- Layer 39: ` .`, ` .↵↵`, `飘飘`, `肤`, `贻` (target ranks: base_value=97:127999, first_product=194:124085, bound_value=173:109755, second_product=346:110534, answer=374:103440)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, `飘飘` (target ranks: base_value=97:127335, first_product=194:122630, bound_value=173:91355, second_product=346:102128, answer=374:85725)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, ` Answer` (target ranks: base_value=97:116723, first_product=194:79292, bound_value=173:25844, second_product=346:65982, answer=374:19644)

### Filler position 24 (absolute token 699, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=97:125015, first_product=194:120421, bound_value=173:122660, second_product=346:124865, answer=374:123386)
- Layer 10: `锁定`, ` Walker`, `ait`, ` cheer`, `Walker` (target ranks: base_value=97:11679, first_product=194:23924, bound_value=173:25607, second_product=346:19780, answer=374:24570)
- Layer 20: ` smile`, `站`, `足`, `肩`, `😂` (target ranks: base_value=97:12859, first_product=194:5662, bound_value=173:33306, second_product=346:10270, answer=374:12005)
- Layer 30: `codeline`, `oNames`, `答案是`, ` Answer`, `</think>` (target ranks: base_value=97:95187, first_product=194:93494, bound_value=173:127577, second_product=346:109728, answer=374:93313)
- Layer 35: `codeline`, `oNames`, ` Zür`, ` doubling`, ` doubled` (target ranks: base_value=97:84942, first_product=194:92928, bound_value=173:123777, second_product=346:105613, answer=374:87580)
- Layer 36: `codeline`, `oNames`, `insic`, `AED`, `坏` (target ranks: base_value=97:38603, first_product=194:48685, bound_value=173:109218, second_product=346:74476, answer=374:46409)
- Layer 37: `codeline`, `oNames`, `本题分析`, ` instantaneous`, `}<?` (target ranks: base_value=97:103818, first_product=194:105327, bound_value=173:120924, second_product=346:102574, answer=374:97587)
- Layer 38: `oNames`, `codeline`, `hatic`, `malink`, `оду` (target ranks: base_value=97:98904, first_product=194:74734, bound_value=173:100123, second_product=346:70458, answer=374:57248)
- Layer 39: ` mdl`, ` medief`, ` поха`, `oxygen`, `bilt` (target ranks: base_value=97:123737, first_product=194:92835, bound_value=173:113512, second_product=346:26216, answer=374:1968)
- Layer 40: ` .↵↵`, ` Answer`, `Answer`, ` .↵`, ` .` (target ranks: base_value=97:106077, first_product=194:71556, bound_value=173:100636, second_product=346:2825, answer=374:7)
- Layer 41: ` Answer`, `Answer`, ` .↵↵`, ` .`, ` .↵` (target ranks: base_value=97:77789, first_product=194:35557, bound_value=173:59848, second_product=346:1470, answer=374:9)

### Filler position 25 (absolute token 700, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `(migrations`, `-ulo` (target ranks: base_value=97:120258, first_product=194:110717, bound_value=173:110828, second_product=346:114370, answer=374:112501)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, ` Saysay` (target ranks: base_value=97:128278, first_product=194:121942, bound_value=173:119409, second_product=346:116848, answer=374:119903)
- Layer 20: ` dátummal`, ` reluct`, ` dekameters`, ` ChatGPT`, ` Numerade` (target ranks: base_value=97:58961, first_product=194:113666, bound_value=173:79159, second_product=346:91472, answer=374:110541)
- Layer 30: `?datasetId`, ` dátummal`, `nze`, `oNames`, ` talags` (target ranks: base_value=97:45669, first_product=194:84693, bound_value=173:12756, second_product=346:41397, answer=374:82007)
- Layer 35: `346`, `345`, `344`, `347`, `348` (target ranks: base_value=97:124797, first_product=194:67080, bound_value=173:103119, second_product=346:1, answer=374:343)
- Layer 36: `323`, `373`, `三百`, `322`, `第三百` (target ranks: base_value=97:124732, first_product=194:121683, bound_value=173:5528, second_product=346:27, answer=374:19)
- Layer 37: `373`, `323`, `366`, `372`, `371` (target ranks: base_value=97:125991, first_product=194:126333, bound_value=173:20667, second_product=346:31, answer=374:13)
- Layer 38: `323`, `373`, `324`, `374`, `322` (target ranks: base_value=97:128471, first_product=194:128311, bound_value=173:54469, second_product=346:83, answer=374:4)
- Layer 39: `374`, `324`, `373`, `322`, `323` (target ranks: base_value=97:127860, first_product=194:119865, bound_value=173:124737, second_product=346:14162, answer=374:1)
- Layer 40: ` Answer`, `Answer`, ` answer`, `_answer`, `answer` (target ranks: base_value=97:127034, first_product=194:108487, bound_value=173:84403, second_product=346:955, answer=374:41)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=97:79671, first_product=194:24522, bound_value=173:50934, second_product=346:2117, answer=374:73)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 25 filler tokens (a sequence of dots) before you answer.<｜User｜>zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>176<｜end▁of▁sentence｜><｜User｜>cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>59<｜end▁of▁sentence｜><｜User｜>gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>351<｜end▁of▁sentence｜><｜User｜>mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>229<｜end▁of▁sentence｜><｜User｜>kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>zuk = 78
xuf = twice the number for zuk minus 15
nof = 97
hoz = twice the number for nof minus 21
hoh = twice the number for nof minus 26
Question: What is twice the number for hoz plus 28?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
