# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `321` (correct).
- No-filler answer: `313` (incorrect).
- Filler tokens: 50 tokens at absolute indices 785–834.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=80` | 1 (L25, filler 37) | L22, filler 15 (rank 9) |
| J-Lens | `first_product=160` | 10 (L28, filler 4) | L28, filler 4 (rank 10) |
| J-Lens | `bound_value=168` | 1 (L33, filler 8) | L31, filler 8 (rank 3) |
| J-Lens | `second_product=336` | 1 (L34, filler 50) | L33, filler 40 (rank 5) |
| J-Lens | `answer=321` | 1 (L35, filler 28) | L33, filler 28 (rank 10) |
| Logit lens | `base_value=80` | 2 (L37, filler 14) | L28, filler 14 (rank 8) |
| Logit lens | `first_product=160` | 17 (L28, filler 12) | Never |
| Logit lens | `bound_value=168` | 1 (L35, filler 8) | L33, filler 8 (rank 8) |
| Logit lens | `second_product=336` | 1 (L33, filler 40) | L31, filler 40 (rank 2) |
| Logit lens | `answer=321` | 1 (L36, filler 4) | L35, filler 28 (rank 2) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 785, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=80:119578, first_product=160:111256, bound_value=168:115393, second_product=336:115076, answer=321:113008)
- Layer 10: `anta`, ` kinain`, `aith`, `hook`, `s` (target ranks: base_value=80:96198, first_product=160:84635, bound_value=168:76536, second_product=336:91907, answer=321:93614)
- Layer 20: `足`, ` .`, `adows`, `abric`, `扣` (target ranks: base_value=80:519, first_product=160:20350, bound_value=168:8822, second_product=336:30653, answer=321:20857)
- Layer 30: ` pakig`, `八十`, ` talags`, ` eighty`, ` Kaw` (target ranks: base_value=80:14, first_product=160:893, bound_value=168:4752, second_product=336:85287, answer=321:120985)
- Layer 35: `obin`, ` Kaw`, ` twice`, ` Tw`, ` tap` (target ranks: base_value=80:19, first_product=160:811, bound_value=168:75, second_product=336:14853, answer=321:74831)
- Layer 36: ` Wil`, `往外`, `期望`, `acin`, `obin` (target ranks: base_value=80:327, first_product=160:2697, bound_value=168:228, second_product=336:14347, answer=321:93150)
- Layer 37: `geries`, ` pakig`, ` premi`, ` udalerria`, ` talags` (target ranks: base_value=80:1474, first_product=160:5430, bound_value=168:137, second_product=336:42627, answer=321:124603)
- Layer 38: ` premi`, `geries`, ` udalerria`, ` talags`, ` ump` (target ranks: base_value=80:4748, first_product=160:13891, bound_value=168:440, second_product=336:45126, answer=321:122171)
- Layer 39: ` talags`, `MMMMMMMM`, `osit`, `osz`, `hemer` (target ranks: base_value=80:58219, first_product=160:114970, bound_value=168:69008, second_product=336:108888, answer=321:126231)
- Layer 40: ` talags`, ` c`, ` pakig`, `oooo`, `pon` (target ranks: base_value=80:66027, first_product=160:117058, bound_value=168:12071, second_product=336:68694, answer=321:93703)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `NET` (target ranks: base_value=80:99227, first_product=160:111361, bound_value=168:14585, second_product=336:51579, answer=321:89730)

### Filler position 2 (absolute token 786, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=80:121702, first_product=160:117517, bound_value=168:120091, second_product=336:120921, answer=321:118119)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=80:21958, first_product=160:31068, bound_value=168:34347, second_product=336:38257, answer=321:27856)
- Layer 20: ` .`, `往常`, `外在`, `�`, ` distant` (target ranks: base_value=80:62136, first_product=160:122548, bound_value=168:113331, second_product=336:125565, answer=321:107196)
- Layer 30: ` pakig`, ` talags`, ` hilabihan`, ` gilay`, `翻` (target ranks: base_value=80:96117, first_product=160:125881, bound_value=168:100797, second_product=336:118861, answer=321:110414)
- Layer 35: ` pakig`, ` hilabihan`, ` talags`, ` .`, `滴水` (target ranks: base_value=80:101237, first_product=160:128395, bound_value=168:123269, second_product=336:125846, answer=321:113311)
- Layer 36: ` talags`, ` hilabihan`, ` Erkännande`, `停`, ` pakig` (target ranks: base_value=80:68372, first_product=160:126200, bound_value=168:109065, second_product=336:115095, answer=321:107576)
- Layer 37: ` Erkännande`, `}<?`, ` hilabihan`, `�乐`, ` licensierad` (target ranks: base_value=80:110078, first_product=160:123823, bound_value=168:127213, second_product=336:123925, answer=321:104818)
- Layer 38: ` Erkännande`, ` .`, ` nasod`, `}<?`, ` .↵↵` (target ranks: base_value=80:69896, first_product=160:106838, bound_value=168:120279, second_product=336:109832, answer=321:60220)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` nasod`, ` .↵↵`, ` .↵` (target ranks: base_value=80:90343, first_product=160:100617, bound_value=168:93191, second_product=336:85847, answer=321:56699)
- Layer 40: ` .`, ` nasod`, ` .↵↵`, ` .↵`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=80:55639, first_product=160:60913, bound_value=168:42262, second_product=336:23991, answer=321:11713)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` 。`, ` ,` (target ranks: base_value=80:24931, first_product=160:10685, bound_value=168:4383, second_product=336:3866, answer=321:1448)

### Filler position 3 (absolute token 787, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125312, first_product=160:121318, bound_value=168:122122, second_product=336:122342, answer=321:120802)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=80:19373, first_product=160:31089, bound_value=168:24392, second_product=336:29060, answer=321:23734)
- Layer 20: `ait`, `ashi`, `能被`, `锁定`, `忑` (target ranks: base_value=80:13086, first_product=160:54432, bound_value=168:27160, second_product=336:45451, answer=321:22582)
- Layer 30: ` variable`, `variable`, ` variables`, `变量`, ` var` (target ranks: base_value=80:37640, first_product=160:89686, bound_value=168:82784, second_product=336:88919, answer=321:94621)
- Layer 35: ` variable`, `variable`, ` Variable`, ` var`, `Variable` (target ranks: base_value=80:12839, first_product=160:70416, bound_value=168:38124, second_product=336:60095, answer=321:53561)
- Layer 36: ` variable`, `变量的`, `variable`, ` var`, ` variables` (target ranks: base_value=80:25155, first_product=160:76708, bound_value=168:41241, second_product=336:50484, answer=321:64312)
- Layer 37: `变量的`, ` variable`, ` перемен`, ` variables`, `variables` (target ranks: base_value=80:65834, first_product=160:98498, bound_value=168:86852, second_product=336:89420, answer=321:104825)
- Layer 38: `变量的`, ` перемен`, `variables`, `}<?`, ` variables` (target ranks: base_value=80:72964, first_product=160:117920, bound_value=168:104583, second_product=336:85690, answer=321:106296)
- Layer 39: `script`, `文字的`, `树叶`, `变量的`, `�` (target ranks: base_value=80:104043, first_product=160:126897, bound_value=168:111285, second_product=336:118744, answer=321:124409)
- Layer 40: ` c`, `ilos`, `acl`, `ses`, ` talags` (target ranks: base_value=80:85732, first_product=160:123469, bound_value=168:85661, second_product=336:116918, answer=321:111993)
- Layer 41: ` .`, ` dotted`, ` ,`, ` `, ` ;` (target ranks: base_value=80:67533, first_product=160:105892, bound_value=168:66421, second_product=336:73990, answer=321:58599)

### Filler position 4 (absolute token 788, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125865, first_product=160:122413, bound_value=168:122786, second_product=336:122834, answer=321:121886)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=80:15724, first_product=160:24486, bound_value=168:19489, second_product=336:23204, answer=321:20453)
- Layer 20: `ait`, `幽`, `atile`, `足`, `拆` (target ranks: base_value=80:20134, first_product=160:54655, bound_value=168:28017, second_product=336:61325, answer=321:49495)
- Layer 30: ` blinding`, `Quintal`, `为难`, ` blinded`, ` perturb` (target ranks: base_value=80:71244, first_product=160:362, bound_value=168:1559, second_product=336:12990, answer=321:40589)
- Layer 35: `329`, `321`, `328`, `323`, `325` (target ranks: base_value=80:119137, first_product=160:111449, bound_value=168:101573, second_product=336:155, answer=321:2)
- Layer 36: `321`, `313`, `311`, `329`, `312` (target ranks: base_value=80:129162, first_product=160:113088, bound_value=168:117289, second_product=336:145, answer=321:1)
- Layer 37: `321`, `313`, `311`, `329`, `312` (target ranks: base_value=80:129141, first_product=160:116089, bound_value=168:97348, second_product=336:129, answer=321:1)
- Layer 38: `313`, `321`, `311`, `329`, `305` (target ranks: base_value=80:129272, first_product=160:128391, bound_value=168:127155, second_product=336:84, answer=321:2)
- Layer 39: `321`, `313`, `311`, `本题分析`, `第三百` (target ranks: base_value=80:128806, first_product=160:128515, bound_value=168:129121, second_product=336:43410, answer=321:1)
- Layer 40: `321`, `313`, ` talags`, `311`, `Kadaghanon` (target ranks: base_value=80:128549, first_product=160:128621, bound_value=168:128237, second_product=336:23050, answer=321:1)
- Layer 41: `321`, `313`, `311`, ` .`, `笔者` (target ranks: base_value=80:122045, first_product=160:126466, bound_value=168:125283, second_product=336:34136, answer=321:1)

### Filler position 5 (absolute token 789, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:125495, first_product=160:122168, bound_value=168:122569, second_product=336:122804, answer=321:121694)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=80:15893, first_product=160:26934, bound_value=168:22127, second_product=336:25153, answer=321:22505)
- Layer 20: `幽`, `能被`, `鞍`, `锁定`, `cape` (target ranks: base_value=80:13295, first_product=160:38268, bound_value=168:23041, second_product=336:38604, answer=321:19092)
- Layer 30: ` twice`, ` Tw`, `Tw`, `calc`, `算出` (target ranks: base_value=80:7098, first_product=160:30718, bound_value=168:62115, second_product=336:91560, answer=321:91653)
- Layer 35: ` Tw`, `Tw`, `.tw`, ` calculate`, `第一步` (target ranks: base_value=80:6484, first_product=160:39922, bound_value=168:50314, second_product=336:68296, answer=321:56331)
- Layer 36: ` Tw`, `Tw`, `.tw`, `calcul`, ` calculate` (target ranks: base_value=80:12408, first_product=160:29171, bound_value=168:23006, second_product=336:45510, answer=321:63198)
- Layer 37: ` cál`, `计算`, `calcul`, `calculation`, ` doubling` (target ranks: base_value=80:28705, first_product=160:37500, bound_value=168:34301, second_product=336:60826, answer=321:86090)
- Layer 38: ` cál`, ` Mul`, ` mul`, `}<?`, `calculation` (target ranks: base_value=80:36847, first_product=160:56480, bound_value=168:52990, second_product=336:85643, answer=321:102815)
- Layer 39: `hemer`, `东海`, `ocyst`, `树叶`, `ople` (target ranks: base_value=80:76132, first_product=160:112791, bound_value=168:91755, second_product=336:107857, answer=321:108415)
- Layer 40: ` c`, `�`, ` nasod`, `duc`, `c` (target ranks: base_value=80:40004, first_product=160:94734, bound_value=168:23211, second_product=336:66367, answer=321:55866)
- Layer 41: ` .`, `鹉`, ` first`, `叮`, `本` (target ranks: base_value=80:43530, first_product=160:66162, bound_value=168:21110, second_product=336:31126, answer=321:8768)

### Filler position 6 (absolute token 790, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=80:124970, first_product=160:121486, bound_value=168:122193, second_product=336:122345, answer=321:121080)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:14489, first_product=160:24528, bound_value=168:19685, second_product=336:22467, answer=321:20639)
- Layer 20: ` calculator`, ` answer`, `答案`, `�`, `�` (target ranks: base_value=80:9578, first_product=160:11948, bound_value=168:34693, second_product=336:48505, answer=321:3371)
- Layer 30: ` Tw`, `Tw`, ` twice`, `.tw`, `计算的` (target ranks: base_value=80:11345, first_product=160:32965, bound_value=168:60623, second_product=336:92861, answer=321:56483)
- Layer 35: ` Tw`, `Tw`, `.tw`, ` tw`, `tw` (target ranks: base_value=80:2698, first_product=160:20035, bound_value=168:29583, second_product=336:59460, answer=321:28168)
- Layer 36: ` Tw`, `Tw`, ` tw`, `.tw`, `tw` (target ranks: base_value=80:3259, first_product=160:16057, bound_value=168:20596, second_product=336:44639, answer=321:36872)
- Layer 37: ` Tw`, `Tw`, ` tw`, `tw`, `.tw` (target ranks: base_value=80:5697, first_product=160:23346, bound_value=168:36767, second_product=336:67073, answer=321:55618)
- Layer 38: ` Tw`, `Tw`, ` Calculators`, ` doubly`, ` tw` (target ranks: base_value=80:5838, first_product=160:14463, bound_value=168:29136, second_product=336:57567, answer=321:85149)
- Layer 39: ` nasod`, `ocyst`, `把事情`, `<｜begin▁of▁sentence｜>`, `叶子` (target ranks: base_value=80:45534, first_product=160:125596, bound_value=168:112615, second_product=336:120725, answer=321:117983)
- Layer 40: ` talags`, ` nasod`, ` Tw`, `留存`, ` hilabihan` (target ranks: base_value=80:23084, first_product=160:124618, bound_value=168:90650, second_product=336:108472, answer=321:83859)
- Layer 41: ` .`, `鹃`, `婷婷`, ` line`, `圆圆` (target ranks: base_value=80:59735, first_product=160:118809, bound_value=168:94733, second_product=336:97987, answer=321:62331)

### Filler position 7 (absolute token 791, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124758, first_product=160:120946, bound_value=168:121963, second_product=336:122053, answer=321:120679)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:14175, first_product=160:23982, bound_value=168:19554, second_product=336:22360, answer=321:20388)
- Layer 20: `ait`, `能被`, `us`, ` Walker`, `忑` (target ranks: base_value=80:5570, first_product=160:31977, bound_value=168:19493, second_product=336:42515, answer=321:26302)
- Layer 30: `Mul`, ` mul`, ` c`, `推算`, `计算的` (target ranks: base_value=80:3391, first_product=160:77853, bound_value=168:103286, second_product=336:108306, answer=321:122920)
- Layer 35: ` c`, ` Tw`, ` cig`, `acks`, `cj` (target ranks: base_value=80:2122, first_product=160:56715, bound_value=168:77546, second_product=336:91012, answer=321:88200)
- Layer 36: ` c`, ` stabil`, ` Tw`, `cid`, `留存` (target ranks: base_value=80:3420, first_product=160:47230, bound_value=168:51108, second_product=336:71069, answer=321:89896)
- Layer 37: `Mul`, ` mul`, ` Mul`, `mul`, `cid` (target ranks: base_value=80:7815, first_product=160:54738, bound_value=168:72700, second_product=336:99988, answer=321:108092)
- Layer 38: ` Mul`, `Mul`, ` mul`, `mul`, `木兰` (target ranks: base_value=80:19895, first_product=160:87381, bound_value=168:99483, second_product=336:114071, answer=321:113529)
- Layer 39: ` Mul`, `Mul`, ` mul`, `mul`, ` multil` (target ranks: base_value=80:49996, first_product=160:120069, bound_value=168:111453, second_product=336:120414, answer=321:111740)
- Layer 40: ` mul`, ` talags`, `scr`, ` pakig`, `留存` (target ranks: base_value=80:27031, first_product=160:117444, bound_value=168:64682, second_product=336:108927, answer=321:74641)
- Layer 41: `鹉`, ` .`, `试一试`, `acular`, `叮` (target ranks: base_value=80:17864, first_product=160:81852, bound_value=168:49370, second_product=336:75405, answer=321:18346)

### Filler position 8 (absolute token 792, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124777, first_product=160:120864, bound_value=168:122057, second_product=336:122064, answer=321:120545)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12067, first_product=160:22612, bound_value=168:18438, second_product=336:21967, answer=321:20130)
- Layer 20: ` Walker`, `能被`, `锁定`, `挪`, `Walker` (target ranks: base_value=80:4937, first_product=160:22288, bound_value=168:14271, second_product=336:25928, answer=321:16612)
- Layer 30: `八十`, ` eighty`, ` pakig`, ` Eighty`, `漂` (target ranks: base_value=80:7, first_product=160:256, bound_value=168:359, second_product=336:21527, answer=321:109346)
- Layer 35: `168`, `旺`, `obin`, `八十`, `68` (target ranks: base_value=80:28, first_product=160:7549, bound_value=168:1, second_product=336:3964, answer=321:78317)
- Layer 36: `168`, ` pakig`, `康熙`, `打包`, ` Wil` (target ranks: base_value=80:380, first_product=160:5298, bound_value=168:1, second_product=336:445, answer=321:109148)
- Layer 37: `168`, `}<?`, `康熙`, `打包`, ` pakig` (target ranks: base_value=80:4361, first_product=160:26552, bound_value=168:1, second_product=336:3439, answer=321:123272)
- Layer 38: `168`, `}<?`, ` pakig`, `康熙`, `打包` (target ranks: base_value=80:15083, first_product=160:41856, bound_value=168:1, second_product=336:7649, answer=321:122765)
- Layer 39: `}<?`, `看书`, ` multipl`, `script`, ` Douglass` (target ranks: base_value=80:18115, first_product=160:117964, bound_value=168:10, second_product=336:71149, answer=321:118617)
- Layer 40: ` talags`, `留存`, `amam`, `装`, `pon` (target ranks: base_value=80:28603, first_product=160:127265, bound_value=168:105, second_product=336:66543, answer=321:80360)
- Layer 41: ` .`, ` careful`, `装`, `实在`, `三十五` (target ranks: base_value=80:28695, first_product=160:116046, bound_value=168:26, second_product=336:23940, answer=321:21338)

### Filler position 9 (absolute token 793, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124752, first_product=160:120898, bound_value=168:122182, second_product=336:122139, answer=321:120569)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12335, first_product=160:23816, bound_value=168:19280, second_product=336:22971, answer=321:20872)
- Layer 20: `ait`, `锁定`, `挪`, ` Walker`, ` smile` (target ranks: base_value=80:7764, first_product=160:28263, bound_value=168:19151, second_product=336:30447, answer=321:21322)
- Layer 30: `acos`, `第一步`, `acin`, `平行`, ` tap` (target ranks: base_value=80:15472, first_product=160:72347, bound_value=168:105624, second_product=336:74965, answer=321:101126)
- Layer 35: `acos`, `分解`, ` tap`, `acks`, `留存` (target ranks: base_value=80:10327, first_product=160:60437, bound_value=168:79673, second_product=336:57248, answer=321:69495)
- Layer 36: `acos`, `留存`, `acl`, `分解`, ` tap` (target ranks: base_value=80:20383, first_product=160:49785, bound_value=168:71702, second_product=336:43023, answer=321:74289)
- Layer 37: `}<?`, `acos`, ` mul`, `mul`, `acl` (target ranks: base_value=80:57625, first_product=160:82887, bound_value=168:103452, second_product=336:73766, answer=321:106160)
- Layer 38: `}<?`, ` mul`, `mul`, `zat`, `acos` (target ranks: base_value=80:55131, first_product=160:96637, bound_value=168:105673, second_product=336:83581, answer=321:111496)
- Layer 39: ` mul`, `mul`, ` Mul`, `}<?`, `Mul` (target ranks: base_value=80:60339, first_product=160:112317, bound_value=168:109018, second_product=336:101075, answer=321:116954)
- Layer 40: `留存`, ` mul`, `acl`, `mul`, `zat` (target ranks: base_value=80:21390, first_product=160:90945, bound_value=168:56493, second_product=336:72013, answer=321:87008)
- Layer 41: ` .`, `鹉`, `留存`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=80:12604, first_product=160:50423, bound_value=168:34870, second_product=336:40324, answer=321:44471)

### Filler position 10 (absolute token 794, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124771, first_product=160:121053, bound_value=168:122450, second_product=336:122300, answer=321:120627)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12309, first_product=160:23536, bound_value=168:19350, second_product=336:22637, answer=321:21278)
- Layer 20: `ait`, ` smile`, `锁定`, `cape`, `幽` (target ranks: base_value=80:5354, first_product=160:19322, bound_value=168:16013, second_product=336:23753, answer=321:16720)
- Layer 30: `鞍`, ` strike`, `165`, `巩固`, `泳` (target ranks: base_value=80:9887, first_product=160:86, bound_value=168:359, second_product=336:320, answer=321:2740)
- Layer 35: `保留`, `鞍`, ` matching`, `羊`, `328` (target ranks: base_value=80:30617, first_product=160:11684, bound_value=168:11995, second_product=336:311, answer=321:39)
- Layer 36: `313`, `翻`, `acin`, `珍珠`, `321` (target ranks: base_value=80:108681, first_product=160:24294, bound_value=168:38239, second_product=336:327, answer=321:5)
- Layer 37: `}<?`, `313`, `珍珠`, ` pakig`, `321` (target ranks: base_value=80:125527, first_product=160:51759, bound_value=168:20817, second_product=336:62, answer=321:5)
- Layer 38: `}<?`, `313`, ` hydrodynamic`, ` pakig`, `329` (target ranks: base_value=80:128260, first_product=160:92081, bound_value=168:55097, second_product=336:104, answer=321:6)
- Layer 39: `}<?`, `本题分析`, `叶子`, `ocyst`, ` hydrodynamic` (target ranks: base_value=80:117425, first_product=160:115261, bound_value=168:124132, second_product=336:50625, answer=321:16)
- Layer 40: ` talags`, ` pakig`, `留存`, `}<?`, `语言文字` (target ranks: base_value=80:102125, first_product=160:104424, bound_value=168:76190, second_product=336:15258, answer=321:10)
- Layer 41: ` .`, `acular`, `鹉`, `试一试`, `我怎么` (target ranks: base_value=80:66070, first_product=160:78390, bound_value=168:63943, second_product=336:4730, answer=321:7)

### Filler position 11 (absolute token 795, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124787, first_product=160:121259, bound_value=168:122628, second_product=336:122531, answer=321:120765)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11764, first_product=160:22314, bound_value=168:18790, second_product=336:22277, answer=321:20638)
- Layer 20: `能被`, `ait`, `啦啦`, ` Walker`, ` smile` (target ranks: base_value=80:5276, first_product=160:28686, bound_value=168:18735, second_product=336:33077, answer=321:16400)
- Layer 30: `acos`, ` August`, `Tap`, `鞍`, ` eighty` (target ranks: base_value=80:599, first_product=160:3298, bound_value=168:1286, second_product=336:10410, answer=321:98478)
- Layer 35: ` tap`, `obin`, `装`, `鞍`, `Tap` (target ranks: base_value=80:1168, first_product=160:21906, bound_value=168:15, second_product=336:6828, answer=321:65723)
- Layer 36: `}<?`, `装`, `翻`, ` pakig`, `radesh` (target ranks: base_value=80:5428, first_product=160:27281, bound_value=168:13, second_product=336:6471, answer=321:97933)
- Layer 37: `}<?`, `Klase`, `polar`, `ajes`, `ocyst` (target ranks: base_value=80:26416, first_product=160:55985, bound_value=168:91, second_product=336:24917, answer=321:120458)
- Layer 38: `}<?`, `ocyst`, `polar`, `Klase`, `解放` (target ranks: base_value=80:41463, first_product=160:73062, bound_value=168:406, second_product=336:38128, answer=321:119243)
- Layer 39: `}<?`, `ocyst`, `繁体`, `polar`, `内膜` (target ranks: base_value=80:41502, first_product=160:88974, bound_value=168:23, second_product=336:25890, answer=321:99161)
- Layer 40: `168`, `冰冰`, `装`, `scr`, `enclose` (target ranks: base_value=80:11156, first_product=160:75747, bound_value=168:1, second_product=336:2895, answer=321:26553)
- Layer 41: ` .`, `168`, `冰冰`, `鹉`, `装` (target ranks: base_value=80:13480, first_product=160:48575, bound_value=168:2, second_product=336:474, answer=321:5152)

### Filler position 12 (absolute token 796, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124687, first_product=160:121181, bound_value=168:122613, second_product=336:122455, answer=321:120745)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12275, first_product=160:22454, bound_value=168:18734, second_product=336:22221, answer=321:20327)
- Layer 20: `锁定`, `ait`, ` smile`, `挪`, ` Walker` (target ranks: base_value=80:9151, first_product=160:25383, bound_value=168:17088, second_product=336:27619, answer=321:21306)
- Layer 30: `未经`, `泳`, `acos`, `328`, `退出` (target ranks: base_value=80:8827, first_product=160:91, bound_value=168:208, second_product=336:250, answer=321:3385)
- Layer 35: `329`, `328`, `321`, `325`, `adal` (target ranks: base_value=80:79695, first_product=160:33972, bound_value=168:31825, second_product=336:20, answer=321:3)
- Layer 36: `313`, `321`, `329`, `311`, `312` (target ranks: base_value=80:127354, first_product=160:39355, bound_value=168:75154, second_product=336:93, answer=321:2)
- Layer 37: `313`, `321`, `329`, `312`, ` Pagbuok` (target ranks: base_value=80:128537, first_product=160:58914, bound_value=168:52720, second_product=336:95, answer=321:2)
- Layer 38: `313`, `321`, `311`, `329`, `第三百` (target ranks: base_value=80:129239, first_product=160:115301, bound_value=168:112620, second_product=336:96, answer=321:2)
- Layer 39: `321`, `313`, `本题分析`, `311`, `-ulo` (target ranks: base_value=80:127720, first_product=160:126547, bound_value=168:129084, second_product=336:61887, answer=321:1)
- Layer 40: `321`, ` talags`, `313`, `Kadaghanon`, ` pakig` (target ranks: base_value=80:124526, first_product=160:126462, bound_value=168:125529, second_product=336:15661, answer=321:1)
- Layer 41: `321`, `313`, ` .`, `Kadaghanon`, `笔者认为` (target ranks: base_value=80:87729, first_product=160:112935, bound_value=168:110097, second_product=336:6357, answer=321:1)

### Filler position 13 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124726, first_product=160:121166, bound_value=168:122643, second_product=336:122464, answer=321:120652)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12531, first_product=160:22846, bound_value=168:19154, second_product=336:22711, answer=321:20576)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, ` smile` (target ranks: base_value=80:8589, first_product=160:28633, bound_value=168:21303, second_product=336:25764, answer=321:19921)
- Layer 30: `acos`, ` pakig`, ` dripping`, `acons`, `未经` (target ranks: base_value=80:7023, first_product=160:1090, bound_value=168:3348, second_product=336:1267, answer=321:9408)
- Layer 35: `329`, `321`, `328`, `325`, `adal` (target ranks: base_value=80:77201, first_product=160:69378, bound_value=168:47763, second_product=336:46, answer=321:2)
- Layer 36: `321`, `313`, `329`, `311`, `312` (target ranks: base_value=80:126064, first_product=160:76471, bound_value=168:101988, second_product=336:306, answer=321:1)
- Layer 37: `321`, `313`, `}<?`, ` Pagbuok`, `polar` (target ranks: base_value=80:127825, first_product=160:86904, bound_value=168:83026, second_product=336:347, answer=321:1)
- Layer 38: `321`, `313`, `}<?`, `329`, `第三百` (target ranks: base_value=80:129240, first_product=160:125514, bound_value=168:123595, second_product=336:279, answer=321:1)
- Layer 39: `321`, `本题分析`, `313`, `-ulo`, ` Parehong` (target ranks: base_value=80:127571, first_product=160:127710, bound_value=168:129178, second_product=336:41634, answer=321:1)
- Layer 40: `321`, ` talags`, ` pakig`, ` Parehong`, ` mosunod` (target ranks: base_value=80:124743, first_product=160:128223, bound_value=168:127542, second_product=336:11482, answer=321:1)
- Layer 41: `321`, ` .`, `笔者认为`, ` nuest`, `313` (target ranks: base_value=80:86759, first_product=160:121476, bound_value=168:114873, second_product=336:3287, answer=321:1)

### Filler position 14 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:124945, first_product=160:121333, bound_value=168:122922, second_product=336:122566, answer=321:120754)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10907, first_product=160:21134, bound_value=168:17718, second_product=336:21320, answer=321:19192)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `能被` (target ranks: base_value=80:11497, first_product=160:33105, bound_value=168:24335, second_product=336:34964, answer=321:28648)
- Layer 30: `八十`, `Mul`, `mul`, ` eighty`, ` mul` (target ranks: base_value=80:8, first_product=160:14493, bound_value=168:87960, second_product=336:103623, answer=321:124117)
- Layer 35: `八十`, `80`, ` eighty`, `Mul`, ` Eighty` (target ranks: base_value=80:2, first_product=160:6133, bound_value=168:35420, second_product=336:83921, answer=321:110879)
- Layer 36: `Mul`, ` Mul`, ` mul`, `八十`, `80` (target ranks: base_value=80:5, first_product=160:8720, bound_value=168:31519, second_product=336:83083, answer=321:120409)
- Layer 37: ` Mul`, `Mul`, `mul`, ` mul`, `}<?` (target ranks: base_value=80:17, first_product=160:21395, bound_value=168:60278, second_product=336:98872, answer=321:123603)
- Layer 38: ` Mul`, `mul`, ` mul`, `Mul`, `}<?` (target ranks: base_value=80:114, first_product=160:44314, bound_value=168:77320, second_product=336:104039, answer=321:124025)
- Layer 39: ` Mul`, `Mul`, `mul`, ` mul`, `}<?` (target ranks: base_value=80:2700, first_product=160:88396, bound_value=168:86476, second_product=336:94195, answer=321:116760)
- Layer 40: ` mul`, `mul`, ` talags`, `scr`, ` Mul` (target ranks: base_value=80:826, first_product=160:78778, bound_value=168:10479, second_product=336:29361, answer=321:44658)
- Layer 41: ` .`, `鹉`, ` mul`, ` eighty`, ` ` (target ranks: base_value=80:1229, first_product=160:39687, bound_value=168:10380, second_product=336:10418, answer=321:7623)

### Filler position 15 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125218, first_product=160:121726, bound_value=168:123304, second_product=336:122959, answer=321:121152)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11061, first_product=160:21586, bound_value=168:17564, second_product=336:21115, answer=321:18925)
- Layer 20: `ait`, `锁定`, ` Walker`, `能被`, `距` (target ranks: base_value=80:6690, first_product=160:25719, bound_value=168:13779, second_product=336:25034, answer=321:18690)
- Layer 30: `Mul`, ` Mul`, `mul`, ` mul`, ` multipliers` (target ranks: base_value=80:11, first_product=160:41399, bound_value=168:94375, second_product=336:106016, answer=321:113339)
- Layer 35: `Mul`, ` Mul`, ` mul`, `mul`, ` Mull` (target ranks: base_value=80:6, first_product=160:23016, bound_value=168:61171, second_product=336:95299, answer=321:95474)
- Layer 36: `Mul`, ` Mul`, ` mul`, `mul`, ` multipliers` (target ranks: base_value=80:9, first_product=160:24090, bound_value=168:50479, second_product=336:97662, answer=321:115459)
- Layer 37: `Mul`, ` Mul`, `mul`, ` mul`, ` multipl` (target ranks: base_value=80:138, first_product=160:47811, bound_value=168:87311, second_product=336:113533, answer=321:120308)
- Layer 38: `mul`, ` Mul`, ` mul`, `Mul`, ` multipl` (target ranks: base_value=80:1255, first_product=160:62775, bound_value=168:102276, second_product=336:117290, answer=321:116791)
- Layer 39: ` Mul`, `mul`, ` mul`, `Mul`, `}<?` (target ranks: base_value=80:51690, first_product=160:111913, bound_value=168:111604, second_product=336:103404, answer=321:98721)
- Layer 40: ` mul`, `mul`, `scr`, `mult`, ` talags` (target ranks: base_value=80:27527, first_product=160:100299, bound_value=168:25704, second_product=336:24506, answer=321:10116)
- Layer 41: ` .`, ` mul`, `鹉`, `mul`, ` twist` (target ranks: base_value=80:29269, first_product=160:65051, bound_value=168:31532, second_product=336:13610, answer=321:1324)

### Filler position 16 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125352, first_product=160:121879, bound_value=168:123580, second_product=336:123056, answer=321:121231)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12151, first_product=160:22155, bound_value=168:17917, second_product=336:21444, answer=321:19657)
- Layer 20: `ait`, `锁定`, `幽`, ` smile`, ` Walker` (target ranks: base_value=80:7979, first_product=160:25465, bound_value=168:13303, second_product=336:29090, answer=321:22231)
- Layer 30: `acin`, `tap`, `忽略`, ` dy`, ` parallel` (target ranks: base_value=80:29111, first_product=160:50351, bound_value=168:47733, second_product=336:49628, answer=321:99575)
- Layer 35: `重复`, ` repeated`, ` repetition`, ` repetitions`, `acin` (target ranks: base_value=80:34003, first_product=160:65182, bound_value=168:43885, second_product=336:54461, answer=321:89485)
- Layer 36: ` repeated`, `重复`, `反复`, ` repetition`, `adal` (target ranks: base_value=80:26986, first_product=160:42302, bound_value=168:20935, second_product=336:31156, answer=321:70182)
- Layer 37: `坏`, `不急`, ` repeated`, `acos`, `用了` (target ranks: base_value=80:76677, first_product=160:74357, bound_value=168:60126, second_product=336:65766, answer=321:110823)
- Layer 38: `坏`, `不急`, ` repeated`, `用了`, `acons` (target ranks: base_value=80:80243, first_product=160:87554, bound_value=168:74628, second_product=336:73645, answer=321:111579)
- Layer 39: `东海`, `坏`, `ocyst`, `<｜begin▁of▁sentence｜>`, `otomy` (target ranks: base_value=80:74889, first_product=160:113261, bound_value=168:92905, second_product=336:101019, answer=321:117163)
- Layer 40: `坏`, ` consum`, ` .`, ` repeated`, ` nasod` (target ranks: base_value=80:49833, first_product=160:100194, bound_value=168:53790, second_product=336:75835, answer=321:78631)
- Layer 41: ` .`, ` repeated`, `坏`, `<｜end▁of▁sentence｜>`, `鹉` (target ranks: base_value=80:21115, first_product=160:62072, bound_value=168:15691, second_product=336:24070, answer=321:25054)

### Filler position 17 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125638, first_product=160:122157, bound_value=168:123900, second_product=336:123387, answer=321:121557)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12703, first_product=160:23245, bound_value=168:18785, second_product=336:22120, answer=321:20418)
- Layer 20: `锁定`, ` smile`, `ait`, `而此时`, `能被` (target ranks: base_value=80:7420, first_product=160:23449, bound_value=168:18172, second_product=336:27182, answer=321:15947)
- Layer 30: `算出`, ` calculate`, `计算出`, `calcul`, `calc` (target ranks: base_value=80:10367, first_product=160:34726, bound_value=168:41291, second_product=336:30058, answer=321:76320)
- Layer 35: ` calculator`, `calc`, `calcul`, `分解`, `算出` (target ranks: base_value=80:6093, first_product=160:28419, bound_value=168:26112, second_product=336:15703, answer=321:39706)
- Layer 36: `calcul`, `分解`, ` value`, `反复`, `radesh` (target ranks: base_value=80:8219, first_product=160:18561, bound_value=168:16483, second_product=336:8680, answer=321:44393)
- Layer 37: `calcul`, `radesh`, `}<?`, `坏`, `不急` (target ranks: base_value=80:23777, first_product=160:32745, bound_value=168:40053, second_product=336:21004, answer=321:68725)
- Layer 38: `calcul`, `}<?`, `zat`, `不急`, `的计算` (target ranks: base_value=80:27313, first_product=160:41391, bound_value=168:47663, second_product=336:25292, answer=321:79618)
- Layer 39: `}<?`, `覆`, `zat`, `东海`, ` Noruwega` (target ranks: base_value=80:29317, first_product=160:79145, bound_value=168:70408, second_product=336:68342, answer=321:103636)
- Layer 40: ` c`, `c`, `坏`, `radesh`, `坏的` (target ranks: base_value=80:9261, first_product=160:38247, bound_value=168:10209, second_product=336:30071, answer=321:50802)
- Layer 41: ` .`, `鹉`, `less`, ` first`, ` ` (target ranks: base_value=80:4716, first_product=160:20681, bound_value=168:6197, second_product=336:14183, answer=321:10360)

### Filler position 18 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125879, first_product=160:122737, bound_value=168:124257, second_product=336:123853, answer=321:121923)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12133, first_product=160:22980, bound_value=168:18074, second_product=336:21854, answer=321:19986)
- Layer 20: `ait`, ` Walker`, `忑`, `锁定`, `Walker` (target ranks: base_value=80:14190, first_product=160:37176, bound_value=168:25504, second_product=336:47397, answer=321:34024)
- Layer 30: `Mul`, ` mul`, `mul`, ` Mul`, ` multipliers` (target ranks: base_value=80:10506, first_product=160:56039, bound_value=168:82927, second_product=336:83387, answer=321:91066)
- Layer 35: ` mul`, `Mul`, `mul`, ` Mul`, ` mun` (target ranks: base_value=80:6454, first_product=160:44607, bound_value=168:75623, second_product=336:82034, answer=321:70996)
- Layer 36: ` mul`, `Mul`, ` mun`, ` multipliers`, ` Mul` (target ranks: base_value=80:7293, first_product=160:32465, bound_value=168:53479, second_product=336:62413, answer=321:81427)
- Layer 37: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=80:46506, first_product=160:52450, bound_value=168:94110, second_product=336:88584, answer=321:105822)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=80:54874, first_product=160:60513, bound_value=168:98510, second_product=336:95340, answer=321:100711)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=80:30805, first_product=160:73478, bound_value=168:95414, second_product=336:105145, answer=321:107578)
- Layer 40: ` mul`, `mul`, `zij`, `amol`, ` sublim` (target ranks: base_value=80:8250, first_product=160:47858, bound_value=168:37587, second_product=336:71294, answer=321:57586)
- Layer 41: `acular`, `鹉`, ` .`, ` mul`, `有这样` (target ranks: base_value=80:10374, first_product=160:34156, bound_value=168:29955, second_product=336:57077, answer=321:26975)

### Filler position 19 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125555, first_product=160:122053, bound_value=168:123790, second_product=336:123275, answer=321:121389)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12269, first_product=160:22512, bound_value=168:18505, second_product=336:21962, answer=321:20021)
- Layer 20: `忑`, `ait`, ` Walker`, `会成为`, ` engaging` (target ranks: base_value=80:17545, first_product=160:47010, bound_value=168:40190, second_product=336:50401, answer=321:40360)
- Layer 30: ` calculator`, `calcul`, `计算的`, `calculator`, `每一步` (target ranks: base_value=80:23319, first_product=160:53530, bound_value=168:66568, second_product=336:43186, answer=321:89926)
- Layer 35: ` calculator`, `calcul`, ` calculations`, `第一步`, `计算的` (target ranks: base_value=80:10800, first_product=160:36120, bound_value=168:31860, second_product=336:23704, answer=321:51137)
- Layer 36: `calcul`, ` calculations`, `计算的`, ` Tw`, ` calculator` (target ranks: base_value=80:12375, first_product=160:22429, bound_value=168:15674, second_product=336:16310, answer=321:49851)
- Layer 37: `}<?`, `calcul`, ` calculations`, ` step`, `不急` (target ranks: base_value=80:47634, first_product=160:55338, bound_value=168:48947, second_product=336:34775, answer=321:102932)
- Layer 38: `}<?`, `calcul`, `不急`, ` step`, ` calculations` (target ranks: base_value=80:48717, first_product=160:63885, bound_value=168:61004, second_product=336:42388, answer=321:110448)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, ` sublim`, `script`, `ozygous` (target ranks: base_value=80:53255, first_product=160:100228, bound_value=168:76974, second_product=336:81196, answer=321:115580)
- Layer 40: `acl`, ` sublim`, `留存`, `殿堂`, `enclose` (target ranks: base_value=80:30504, first_product=160:81484, bound_value=168:50418, second_product=336:54684, answer=321:80104)
- Layer 41: ` .`, `有下列`, `<｜end▁of▁sentence｜>`, `留存`, ` fifty` (target ranks: base_value=80:10448, first_product=160:39425, bound_value=168:26086, second_product=336:15415, answer=321:27594)

### Filler position 20 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125845, first_product=160:122274, bound_value=168:124129, second_product=336:123451, answer=321:121557)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11976, first_product=160:21204, bound_value=168:17825, second_product=336:21045, answer=321:19441)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, `距` (target ranks: base_value=80:8439, first_product=160:26214, bound_value=168:19710, second_product=336:29738, answer=321:24372)
- Layer 30: `328`, `未经`, `退出`, ` pools`, `泳` (target ranks: base_value=80:5940, first_product=160:150, bound_value=168:311, second_product=336:340, answer=321:5187)
- Layer 35: `329`, `328`, `325`, `321`, `323` (target ranks: base_value=80:83425, first_product=160:70965, bound_value=168:63345, second_product=336:20, answer=321:4)
- Layer 36: `321`, `313`, `329`, `311`, `323` (target ranks: base_value=80:127372, first_product=160:73818, bound_value=168:94887, second_product=336:98, answer=321:1)
- Layer 37: `321`, `313`, `329`, `323`, `311` (target ranks: base_value=80:128720, first_product=160:95062, bound_value=168:92638, second_product=336:111, answer=321:1)
- Layer 38: `313`, `321`, `329`, `311`, `305` (target ranks: base_value=80:129241, first_product=160:125799, bound_value=168:124610, second_product=336:81, answer=321:2)
- Layer 39: `321`, `313`, `本题分析`, `322`, ` Parehong` (target ranks: base_value=80:128218, first_product=160:127314, bound_value=168:128704, second_product=336:49280, answer=321:1)
- Layer 40: `321`, `<｜begin▁of▁file｜>`, `313`, ` pakig`, ` mosunod` (target ranks: base_value=80:127942, first_product=160:128289, bound_value=168:128361, second_product=336:42198, answer=321:1)
- Layer 41: `321`, `印书馆`, `313`, `试一试`, ` Expressible` (target ranks: base_value=80:107194, first_product=160:122345, bound_value=168:123944, second_product=336:27571, answer=321:1)

### Filler position 21 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:125724, first_product=160:122319, bound_value=168:124151, second_product=336:123489, answer=321:121549)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11074, first_product=160:20496, bound_value=168:17408, second_product=336:20814, answer=321:18668)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=80:14677, first_product=160:34396, bound_value=168:26720, second_product=336:38529, answer=321:27952)
- Layer 30: `acos`, `俯`, `acin`, `�`, ` tear` (target ranks: base_value=80:83099, first_product=160:93454, bound_value=168:97013, second_product=336:81272, answer=321:80398)
- Layer 35: `acos`, ` tap`, `俯`, `Tap`, ` dip` (target ranks: base_value=80:66466, first_product=160:88802, bound_value=168:62946, second_product=336:65354, answer=321:58905)
- Layer 36: `acos`, ` drip`, `俯`, ` rip`, `滴` (target ranks: base_value=80:62441, first_product=160:62345, bound_value=168:50521, second_product=336:30328, answer=321:48255)
- Layer 37: `}<?`, `acos`, `zat`, ` sip`, `zim` (target ranks: base_value=80:90535, first_product=160:80904, bound_value=168:78478, second_product=336:49221, answer=321:83302)
- Layer 38: `}<?`, `zat`, ` sip`, `acos`, ` Pax` (target ranks: base_value=80:95217, first_product=160:88512, bound_value=168:78623, second_product=336:56289, answer=321:75889)
- Layer 39: `}<?`, `zat`, `oug`, ` Nij`, `zam` (target ranks: base_value=80:92324, first_product=160:98882, bound_value=168:94760, second_product=336:37345, answer=321:43015)
- Layer 40: `zat`, `acos`, `zim`, `zij`, `冰冰` (target ranks: base_value=80:74495, first_product=160:79154, bound_value=168:35507, second_product=336:5332, answer=321:350)
- Layer 41: ` Question`, `Question`, `325`, `俯`, ` fum` (target ranks: base_value=80:44114, first_product=160:20116, bound_value=168:5350, second_product=336:240, answer=321:16)

### Filler position 22 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126059, first_product=160:122626, bound_value=168:124478, second_product=336:123795, answer=321:121765)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10635, first_product=160:20232, bound_value=168:16769, second_product=336:20616, answer=321:18199)
- Layer 20: `ait`, `锁定`, ` Walker`, `距`, ` engaging` (target ranks: base_value=80:11205, first_product=160:24058, bound_value=168:18292, second_product=336:36092, answer=321:24650)
- Layer 30: ` Tw`, `Tw`, ` twice`, `tw`, `.tw` (target ranks: base_value=80:2590, first_product=160:11520, bound_value=168:19147, second_product=336:39907, answer=321:50568)
- Layer 35: ` Tw`, `Tw`, `tw`, ` twice`, `.tw` (target ranks: base_value=80:1586, first_product=160:4614, bound_value=168:9833, second_product=336:22771, answer=321:38654)
- Layer 36: ` Tw`, `Tw`, `.tw`, ` twice`, `tw` (target ranks: base_value=80:1419, first_product=160:1854, bound_value=168:3478, second_product=336:13733, answer=321:45726)
- Layer 37: ` Tw`, `Tw`, ` doubling`, `}<?`, ` twice` (target ranks: base_value=80:6873, first_product=160:3974, bound_value=168:11280, second_product=336:26623, answer=321:81915)
- Layer 38: `}<?`, ` doubling`, ` Tw`, `zat`, `Tw` (target ranks: base_value=80:6971, first_product=160:7018, bound_value=168:16779, second_product=336:44024, answer=321:91819)
- Layer 39: `}<?`, `zat`, ` Tw`, ` twist`, `orten` (target ranks: base_value=80:2142, first_product=160:29600, bound_value=168:23393, second_product=336:89794, answer=321:111514)
- Layer 40: ` eighty`, `zat`, ` Tw`, ` mul`, `mul` (target ranks: base_value=80:100, first_product=160:17275, bound_value=168:905, second_product=336:46034, answer=321:61619)
- Layer 41: ` `, ` .`, ` twist`, `的计算`, `俯` (target ranks: base_value=80:421, first_product=160:12432, bound_value=168:1135, second_product=336:38763, answer=321:39038)

### Filler position 23 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126229, first_product=160:123092, bound_value=168:124746, second_product=336:124173, answer=321:122110)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11972, first_product=160:21437, bound_value=168:18039, second_product=336:21365, answer=321:18567)
- Layer 20: ` smile`, `锁定`, `ait`, ` Tears`, `足` (target ranks: base_value=80:6795, first_product=160:20679, bound_value=168:10984, second_product=336:23409, answer=321:11888)
- Layer 30: ` Tw`, ` twice`, `atan`, `Tw`, `第一步` (target ranks: base_value=80:4467, first_product=160:21718, bound_value=168:23755, second_product=336:32126, answer=321:54196)
- Layer 35: ` Tw`, ` first`, `Tw`, ` twice`, ` repetition` (target ranks: base_value=80:7561, first_product=160:24944, bound_value=168:23780, second_product=336:26315, answer=321:48495)
- Layer 36: ` Tw`, ` first`, `calcul`, `反复`, ` EC` (target ranks: base_value=80:7338, first_product=160:14796, bound_value=168:10371, second_product=336:16800, answer=321:55203)
- Layer 37: `}<?`, `坏`, `calcul`, `acos`, `radesh` (target ranks: base_value=80:25379, first_product=160:26830, bound_value=168:28396, second_product=336:37816, answer=321:87109)
- Layer 38: `}<?`, `zat`, `坏`, `覆`, `radesh` (target ranks: base_value=80:28046, first_product=160:36681, bound_value=168:44709, second_product=336:48648, answer=321:92831)
- Layer 39: `}<?`, `zat`, `-ulo`, ` Noruwega`, `ocyst` (target ranks: base_value=80:23767, first_product=160:70025, bound_value=168:53865, second_product=336:68470, answer=321:92513)
- Layer 40: ` c`, `c`, `坏`, ` mul`, `mul` (target ranks: base_value=80:3407, first_product=160:31353, bound_value=168:4972, second_product=336:22786, answer=321:23343)
- Layer 41: ` .`, ` first`, `坏`, `acular`, `本` (target ranks: base_value=80:1868, first_product=160:10937, bound_value=168:1209, second_product=336:5229, answer=321:3152)

### Filler position 24 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126116, first_product=160:123084, bound_value=168:124734, second_product=336:124184, answer=321:122102)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:12431, first_product=160:22030, bound_value=168:18582, second_product=336:21896, answer=321:19102)
- Layer 20: `足`, ` smile`, ` LS`, `ait`, ` ES` (target ranks: base_value=80:6965, first_product=160:28392, bound_value=168:14915, second_product=336:36122, answer=321:19996)
- Layer 30: ` ignoring`, `忽略`, ` ignore`, ` ignored`, `Ign` (target ranks: base_value=80:15408, first_product=160:28812, bound_value=168:29519, second_product=336:28000, answer=321:67942)
- Layer 35: ` ignoring`, `忽略`, ` ignore`, ` Ign`, `Ign` (target ranks: base_value=80:20877, first_product=160:51110, bound_value=168:41030, second_product=336:42299, answer=321:69043)
- Layer 36: `忽略`, ` ignoring`, ` ignore`, ` ignored`, ` Ign` (target ranks: base_value=80:21405, first_product=160:33962, bound_value=168:26747, second_product=336:21826, answer=321:61118)
- Layer 37: `不急`, `relevant`, `忽略`, ` Relevant`, `calcul` (target ranks: base_value=80:70282, first_product=160:76791, bound_value=168:76916, second_product=336:51167, answer=321:107709)
- Layer 38: `relevant`, ` Relevant`, `不急`, `殿堂`, `}<?` (target ranks: base_value=80:69855, first_product=160:97002, bound_value=168:91221, second_product=336:48512, answer=321:105815)
- Layer 39: `<｜begin▁of▁sentence｜>`, `殿堂`, ` Relevant`, `iota`, `枝叶` (target ranks: base_value=80:63895, first_product=160:118014, bound_value=168:99422, second_product=336:75321, answer=321:115487)
- Layer 40: `殿堂`, ` Relevant`, `acl`, `冰冰`, ` mul` (target ranks: base_value=80:39607, first_product=160:111867, bound_value=168:86766, second_product=336:66748, answer=321:82354)
- Layer 41: ` .`, `步骤如下`, ` `, `鹃`, ` Relevant` (target ranks: base_value=80:20589, first_product=160:73103, bound_value=168:43660, second_product=336:32070, answer=321:25722)

### Filler position 25 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126525, first_product=160:123436, bound_value=168:125036, second_product=336:124438, answer=321:122437)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12985, first_product=160:23730, bound_value=168:19727, second_product=336:23010, answer=321:20562)
- Layer 20: ` smile`, `拆`, `锁定`, `竹`, ` Walker` (target ranks: base_value=80:7396, first_product=160:17526, bound_value=168:16031, second_product=336:26399, answer=321:15702)
- Layer 30: `算出`, `calcul`, `计算的`, `计算`, ` calculator` (target ranks: base_value=80:3058, first_product=160:7542, bound_value=168:31337, second_product=336:51888, answer=321:72015)
- Layer 35: `calcul`, ` calculations`, ` Tw`, `计算的`, ` calculator` (target ranks: base_value=80:1504, first_product=160:8690, bound_value=168:25412, second_product=336:45724, answer=321:39510)
- Layer 36: `calcul`, ` calculations`, ` Tw`, `计算的`, ` calculation` (target ranks: base_value=80:1323, first_product=160:3456, bound_value=168:10695, second_product=336:27182, answer=321:56264)
- Layer 37: `}<?`, `calcul`, ` calculations`, `的计算`, `计算方法` (target ranks: base_value=80:2349, first_product=160:5418, bound_value=168:18279, second_product=336:38404, answer=321:78794)
- Layer 38: `}<?`, `的计算`, ` cál`, ` duc`, `mul` (target ranks: base_value=80:2813, first_product=160:3483, bound_value=168:14179, second_product=336:50755, answer=321:88796)
- Layer 39: `}<?`, `mul`, `orten`, `tanle`, ` mul` (target ranks: base_value=80:14645, first_product=160:58505, bound_value=168:60075, second_product=336:96560, answer=321:101148)
- Layer 40: ` mul`, `mul`, ` talags`, ` pakig`, ` Tw` (target ranks: base_value=80:1574, first_product=160:28712, bound_value=168:10802, second_product=336:48457, answer=321:25084)
- Layer 41: `步骤如下`, `mul`, ` .`, `筋`, ` mul` (target ranks: base_value=80:2468, first_product=160:14776, bound_value=168:5289, second_product=336:23916, answer=321:11415)

### Filler position 26 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126634, first_product=160:123598, bound_value=168:125224, second_product=336:124587, answer=321:122593)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12216, first_product=160:22948, bound_value=168:18752, second_product=336:21656, answer=321:19856)
- Layer 20: ` Walker`, `ait`, `Walker`, `锁定`, `拆` (target ranks: base_value=80:8207, first_product=160:26864, bound_value=168:20732, second_product=336:35199, answer=321:36133)
- Layer 30: ` labor`, `acin`, ` dy`, `ragma`, `acic` (target ranks: base_value=80:19450, first_product=160:63674, bound_value=168:98321, second_product=336:90461, answer=321:115605)
- Layer 35: ` labor`, ` dy`, `分解`, ` equations`, `大河` (target ranks: base_value=80:13772, first_product=160:55696, bound_value=168:87586, second_product=336:74604, answer=321:99124)
- Layer 36: ` definitions`, ` stabil`, `分解`, `adal`, ` equations` (target ranks: base_value=80:18722, first_product=160:41656, bound_value=168:73535, second_product=336:49289, answer=321:106974)
- Layer 37: `}<?`, `dividers`, `定义了`, ` definitions`, `zat` (target ranks: base_value=80:64325, first_product=160:73294, bound_value=168:103159, second_product=336:72136, answer=321:123571)
- Layer 38: `}<?`, `zat`, `定义了`, `不加`, `dividers` (target ranks: base_value=80:61991, first_product=160:90930, bound_value=168:99879, second_product=336:68207, answer=321:120748)
- Layer 39: `zat`, `}<?`, ` mul`, `mul`, `dividers` (target ranks: base_value=80:29833, first_product=160:86937, bound_value=168:87538, second_product=336:79321, answer=321:118805)
- Layer 40: ` mul`, `mul`, `zat`, ` multipliers`, `daq` (target ranks: base_value=80:10341, first_product=160:47413, bound_value=168:56788, second_product=336:69237, answer=321:82241)
- Layer 41: ` waterfall`, `瘫�`, `每次`, `水`, ` mul` (target ranks: base_value=80:2310, first_product=160:9230, bound_value=168:13830, second_product=336:15172, answer=321:32474)

### Filler position 27 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126885, first_product=160:123828, bound_value=168:125468, second_product=336:124841, answer=321:122895)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11317, first_product=160:21233, bound_value=168:17462, second_product=336:20326, answer=321:18647)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, ` engaging` (target ranks: base_value=80:7162, first_product=160:23170, bound_value=168:18884, second_product=336:31247, answer=321:25278)
- Layer 30: `Mul`, ` mul`, `mul`, ` Mul`, `acin` (target ranks: base_value=80:19855, first_product=160:62185, bound_value=168:106120, second_product=336:93332, answer=321:114457)
- Layer 35: `Mul`, ` mul`, ` mun`, ` Mull`, `分解` (target ranks: base_value=80:14605, first_product=160:67989, bound_value=168:102792, second_product=336:98158, answer=321:107871)
- Layer 36: ` mul`, `Mul`, ` Mul`, `分解`, `adal` (target ranks: base_value=80:15699, first_product=160:50486, bound_value=168:86370, second_product=336:71899, answer=321:110138)
- Layer 37: ` mul`, `Mul`, `mul`, ` Mul`, `}<?` (target ranks: base_value=80:66708, first_product=160:75189, bound_value=168:113014, second_product=336:94169, answer=321:119577)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `zat` (target ranks: base_value=80:52657, first_product=160:74290, bound_value=168:107133, second_product=336:93592, answer=321:112353)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `zat` (target ranks: base_value=80:35245, first_product=160:83272, bound_value=168:103373, second_product=336:107068, answer=321:119908)
- Layer 40: ` mul`, `zat`, `mul`, `acl`, `ses` (target ranks: base_value=80:16139, first_product=160:58736, bound_value=168:59394, second_product=336:80156, answer=321:100535)
- Layer 41: `鹉`, ` mul`, ` wherever`, `<｜end▁of▁sentence｜>`, ` whichever` (target ranks: base_value=80:3288, first_product=160:11852, bound_value=168:9191, second_product=336:19872, answer=321:43593)

### Filler position 28 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126663, first_product=160:123553, bound_value=168:125264, second_product=336:124577, answer=321:122574)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11258, first_product=160:21101, bound_value=168:17834, second_product=336:20564, answer=321:18991)
- Layer 20: `能被`, `ait`, ` Walker`, `拆`, `Walker` (target ranks: base_value=80:5691, first_product=160:19193, bound_value=168:16611, second_product=336:27587, answer=321:17183)
- Layer 30: `exerc`, `粥`, `柿子`, ` exercises`, ` engaging` (target ranks: base_value=80:8096, first_product=160:1713, bound_value=168:1941, second_product=336:1243, answer=321:13459)
- Layer 35: `321`, `328`, `329`, `361`, `353` (target ranks: base_value=80:71142, first_product=160:76913, bound_value=168:41983, second_product=336:6, answer=321:1)
- Layer 36: `321`, `361`, ` Pagbuok`, `}<?`, `)Skip` (target ranks: base_value=80:122276, first_product=160:103879, bound_value=168:68343, second_product=336:6, answer=321:1)
- Layer 37: ` Pagbuok`, `321`, `}<?`, ` Gelijk`, `361` (target ranks: base_value=80:124977, first_product=160:103522, bound_value=168:47730, second_product=336:7, answer=321:2)
- Layer 38: `321`, `361`, `329`, `336`, `}<?` (target ranks: base_value=80:128655, first_product=160:126253, bound_value=168:80243, second_product=336:4, answer=321:1)
- Layer 39: `321`, `Liver`, ` dátummal`, ` commissioner`, `ometrics` (target ranks: base_value=80:126047, first_product=160:127614, bound_value=168:128410, second_product=336:3803, answer=321:1)
- Layer 40: `321`, ` kinahabogang`, `骥`, ` mosunod`, ` forgotten` (target ranks: base_value=80:119631, first_product=160:127382, bound_value=168:124750, second_product=336:3675, answer=321:1)
- Layer 41: `321`, ` expectation`, ` .`, ` terg`, `便于` (target ranks: base_value=80:88251, first_product=160:124002, bound_value=168:113443, second_product=336:3746, answer=321:1)

### Filler position 29 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126625, first_product=160:123551, bound_value=168:125252, second_product=336:124576, answer=321:122591)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:11697, first_product=160:21641, bound_value=168:18413, second_product=336:21397, answer=321:19060)
- Layer 20: `ession`, `幽`, `aty`, `锁定`, ` smile` (target ranks: base_value=80:5774, first_product=160:16107, bound_value=168:14752, second_product=336:34310, answer=321:16164)
- Layer 30: `daq`, ` EQ`, `EQ`, `DAQ`, `aq` (target ranks: base_value=80:13972, first_product=160:33546, bound_value=168:59338, second_product=336:62102, answer=321:99555)
- Layer 35: `daq`, `cape`, `分解`, `DAQ`, ` tap` (target ranks: base_value=80:5287, first_product=160:21830, bound_value=168:38834, second_product=336:62986, answer=321:88235)
- Layer 36: `cape`, `坏`, `俯`, `分解`, `留存` (target ranks: base_value=80:7724, first_product=160:12958, bound_value=168:31250, second_product=336:50097, answer=321:98573)
- Layer 37: `}<?`, `坏`, `daq`, ` Daisy`, `翻了` (target ranks: base_value=80:23481, first_product=160:29565, bound_value=168:59959, second_product=336:86657, answer=321:119654)
- Layer 38: `}<?`, `坏`, `zat`, `覆`, ` unflagged` (target ranks: base_value=80:15161, first_product=160:51239, bound_value=168:69885, second_product=336:91165, answer=321:116950)
- Layer 39: `}<?`, ` unflagged`, `<｜begin▁of▁sentence｜>`, `ocyst`, `覆` (target ranks: base_value=80:43847, first_product=160:99585, bound_value=168:100473, second_product=336:113748, answer=321:123582)
- Layer 40: `坏`, `坏的`, ` Tw`, `acl`, `坏了` (target ranks: base_value=80:16034, first_product=160:84043, bound_value=168:62562, second_product=336:74679, answer=321:80345)
- Layer 41: ` .`, `坏`, `从前`, `没有被`, ` ` (target ranks: base_value=80:5537, first_product=160:37250, bound_value=168:22759, second_product=336:31850, answer=321:27121)

### Filler position 30 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126945, first_product=160:124078, bound_value=168:125776, second_product=336:124994, answer=321:123002)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11290, first_product=160:20796, bound_value=168:17565, second_product=336:21065, answer=321:18333)
- Layer 20: `cape`, `atile`, `鞍`, `锁定`, ` smile` (target ranks: base_value=80:6114, first_product=160:17917, bound_value=168:13640, second_product=336:26151, answer=321:13069)
- Layer 30: ` rip`, ` Lex`, `坏`, ` fif`, ` Bax` (target ranks: base_value=80:48492, first_product=160:106290, bound_value=168:124499, second_product=336:115343, answer=321:93851)
- Layer 35: ` tap`, `Tap`, ` rip`, `tap`, ` vib` (target ranks: base_value=80:28902, first_product=160:104178, bound_value=168:112044, second_product=336:113853, answer=321:83450)
- Layer 36: `坏`, ` tap`, ` zad`, ` rip`, ` vib` (target ranks: base_value=80:20189, first_product=160:67218, bound_value=168:84544, second_product=336:65746, answer=321:56747)
- Layer 37: `zat`, `坏`, `坏的`, `本题分析`, `zim` (target ranks: base_value=80:47099, first_product=160:88250, bound_value=168:111828, second_product=336:86254, answer=321:96394)
- Layer 38: `本题分析`, `zat`, `疑惑`, `oNames`, `}<?` (target ranks: base_value=80:70990, first_product=160:102737, bound_value=168:114405, second_product=336:100649, answer=321:100476)
- Layer 39: `zat`, `zel`, `本题分析`, ` duc`, `polar` (target ranks: base_value=80:72032, first_product=160:96645, bound_value=168:109976, second_product=336:108778, answer=321:103124)
- Layer 40: `zel`, `y`, `zat`, `zij`, `坏的` (target ranks: base_value=80:63413, first_product=160:98164, bound_value=168:93687, second_product=336:94494, answer=321:66045)
- Layer 41: ` mim`, `zel`, `坏的`, `zij`, `坏` (target ranks: base_value=80:39341, first_product=160:37880, bound_value=168:32452, second_product=336:29825, answer=321:31647)

### Filler position 31 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:126944, first_product=160:123903, bound_value=168:125713, second_product=336:124862, answer=321:122882)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10876, first_product=160:19865, bound_value=168:16770, second_product=336:20574, answer=321:18198)
- Layer 20: `锁定`, `鞍`, `ait`, ` smile`, `忑` (target ranks: base_value=80:6362, first_product=160:19335, bound_value=168:15723, second_product=336:25278, answer=321:15473)
- Layer 30: ` tap`, `Tap`, `tap`, ` Tap`, `鞍` (target ranks: base_value=80:38845, first_product=160:58372, bound_value=168:70397, second_product=336:51485, answer=321:38406)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, ` vertical` (target ranks: base_value=80:21042, first_product=160:56048, bound_value=168:58688, second_product=336:47899, answer=321:33156)
- Layer 36: ` tap`, `Tap`, ` stabil`, ` Tap`, `tap` (target ranks: base_value=80:11704, first_product=160:32447, bound_value=168:44578, second_product=336:26173, answer=321:32753)
- Layer 37: `冰冰`, ` tap`, `comp`, `坏`, ` follow` (target ranks: base_value=80:21031, first_product=160:46773, bound_value=168:85086, second_product=336:43425, answer=321:60597)
- Layer 38: `冰冰`, `}<?`, `坏`, `寒风`, `acons` (target ranks: base_value=80:40474, first_product=160:67444, bound_value=168:92959, second_product=336:42372, answer=321:66801)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, ` lenker`, `ocyst`, `dividers` (target ranks: base_value=80:27873, first_product=160:92746, bound_value=168:91656, second_product=336:49618, answer=321:49265)
- Layer 40: `冰冰`, `坏`, `acular`, `<｜begin▁of▁sentence｜>`, `acl` (target ranks: base_value=80:7873, first_product=160:69276, bound_value=168:66457, second_product=336:16506, answer=321:3943)
- Layer 41: ` .`, ` mim`, ` unless`, `鹃`, ` because` (target ranks: base_value=80:7366, first_product=160:34957, bound_value=168:27325, second_product=336:2282, answer=321:385)

### Filler position 32 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127223, first_product=160:124430, bound_value=168:126071, second_product=336:125342, answer=321:123366)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10978, first_product=160:19918, bound_value=168:16549, second_product=336:20446, answer=321:18649)
- Layer 20: ` Walker`, ` ES`, ` engaging`, `ait`, ` LS` (target ranks: base_value=80:7000, first_product=160:22928, bound_value=168:19998, second_product=336:33965, answer=321:21259)
- Layer 30: ` twice`, ` Tw`, `Tw`, `算出`, `鞍` (target ranks: base_value=80:190, first_product=160:20828, bound_value=168:66616, second_product=336:53060, answer=321:95518)
- Layer 35: ` Tw`, ` twice`, `Tw`, `tw`, ` c` (target ranks: base_value=80:19, first_product=160:6937, bound_value=168:28378, second_product=336:35253, answer=321:70669)
- Layer 36: ` Tw`, ` twice`, `留存`, `Tw`, ` stabil` (target ranks: base_value=80:16, first_product=160:5130, bound_value=168:18877, second_product=336:25077, answer=321:82332)
- Layer 37: `Mul`, ` doubling`, ` Mul`, ` mul`, `mul` (target ranks: base_value=80:67, first_product=160:7430, bound_value=168:36107, second_product=336:45849, answer=321:103510)
- Layer 38: `Mul`, ` Mul`, ` doubling`, ` mul`, ` MPI` (target ranks: base_value=80:120, first_product=160:14373, bound_value=168:46673, second_product=336:64330, answer=321:113215)
- Layer 39: `八十`, `Mul`, ` eighty`, ` Mul`, `mul` (target ranks: base_value=80:141, first_product=160:57660, bound_value=168:55287, second_product=336:88705, answer=321:113231)
- Layer 40: ` eighty`, `Mul`, ` mul`, `八十`, ` Mul` (target ranks: base_value=80:20, first_product=160:44166, bound_value=168:9553, second_product=336:49643, answer=321:63071)
- Layer 41: ` eighty`, ` mul`, `八十`, `mul`, `acular` (target ranks: base_value=80:61, first_product=160:21932, bound_value=168:6595, second_product=336:32487, answer=321:29253)

### Filler position 33 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=80:127337, first_product=160:124583, bound_value=168:126142, second_product=336:125463, answer=321:123508)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:10638, first_product=160:20183, bound_value=168:16158, second_product=336:20145, answer=321:18111)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `足` (target ranks: base_value=80:7430, first_product=160:24658, bound_value=168:20358, second_product=336:31565, answer=321:24607)
- Layer 30: `acin`, `鞍`, `锁定`, `adal`, `�` (target ranks: base_value=80:2830, first_product=160:33401, bound_value=168:44009, second_product=336:28018, answer=321:64687)
- Layer 35: ` var`, `acin`, `锁定`, ` number`, ` Number` (target ranks: base_value=80:2527, first_product=160:26034, bound_value=168:26216, second_product=336:12491, answer=321:29064)
- Layer 36: `acin`, `引用`, ` talags`, ` references`, ` number` (target ranks: base_value=80:3933, first_product=160:20139, bound_value=168:21050, second_product=336:7223, answer=321:34616)
- Layer 37: `referent`, `引用`, ` talags`, `数值`, `}<?` (target ranks: base_value=80:13368, first_product=160:43777, bound_value=168:47096, second_product=336:17055, answer=321:76017)
- Layer 38: `referent`, `}<?`, `引用`, `数值`, `变量的` (target ranks: base_value=80:13055, first_product=160:59533, bound_value=168:48282, second_product=336:14109, answer=321:63465)
- Layer 39: `umber`, ` talags`, ` Number`, ` NUMBER`, `osit` (target ranks: base_value=80:6698, first_product=160:79736, bound_value=168:71752, second_product=336:74648, answer=321:105357)
- Layer 40: ` talags`, ` eighty`, `留存`, `acin`, `殿堂` (target ranks: base_value=80:1256, first_product=160:66186, bound_value=168:36733, second_product=336:53727, answer=321:78283)
- Layer 41: ` .`, ` number`, `从前`, `留存`, ` ` (target ranks: base_value=80:1575, first_product=160:51108, bound_value=168:33288, second_product=336:54152, answer=321:47942)

### Filler position 34 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: base_value=80:127447, first_product=160:124764, bound_value=168:126288, second_product=336:125565, answer=321:123625)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11057, first_product=160:21035, bound_value=168:16346, second_product=336:20135, answer=321:18074)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, `足` (target ranks: base_value=80:7416, first_product=160:27013, bound_value=168:15078, second_product=336:28717, answer=321:24468)
- Layer 30: `Mul`, `acin`, ` mul`, `mul`, `acos` (target ranks: base_value=80:12517, first_product=160:55927, bound_value=168:75008, second_product=336:62179, answer=321:103733)
- Layer 35: `Mul`, ` mul`, `acic`, ` Mull`, ` Mul` (target ranks: base_value=80:20700, first_product=160:61985, bound_value=168:94500, second_product=336:75646, answer=321:94800)
- Layer 36: `Mul`, ` mul`, ` Mul`, ` multiplic`, ` Mull` (target ranks: base_value=80:18908, first_product=160:34462, bound_value=168:65221, second_product=336:46052, answer=321:89741)
- Layer 37: ` mul`, `Mul`, ` Mul`, `mul`, `acos` (target ranks: base_value=80:62678, first_product=160:61615, bound_value=168:102431, second_product=336:87405, answer=321:115869)
- Layer 38: ` mul`, ` Mul`, `Mul`, `mul`, ` multiplic` (target ranks: base_value=80:55679, first_product=160:67171, bound_value=168:99261, second_product=336:79881, answer=321:107023)
- Layer 39: ` mul`, `mul`, ` Mul`, `Mul`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=80:37187, first_product=160:81405, bound_value=168:100089, second_product=336:96827, answer=321:110693)
- Layer 40: ` mul`, ` c`, `c`, `mul`, `acl` (target ranks: base_value=80:13149, first_product=160:57382, bound_value=168:46731, second_product=336:62716, answer=321:78716)
- Layer 41: ` compounded`, `acular`, ` whichever`, ` mul`, ` compounding` (target ranks: base_value=80:6240, first_product=160:23620, bound_value=168:13434, second_product=336:20307, answer=321:29029)

### Filler position 35 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127553, first_product=160:125093, bound_value=168:126524, second_product=336:125866, answer=321:123927)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12191, first_product=160:22186, bound_value=168:17709, second_product=336:20720, answer=321:19213)
- Layer 20: `ait`, `足`, ` smile`, `cape`, `锁定` (target ranks: base_value=80:3820, first_product=160:16162, bound_value=168:10971, second_product=336:19434, answer=321:15012)
- Layer 30: ` Tw`, ` twice`, `Tw`, `算出`, `反复` (target ranks: base_value=80:7896, first_product=160:27282, bound_value=168:61469, second_product=336:54296, answer=321:110579)
- Layer 35: ` Tw`, `Tw`, ` twice`, `分解`, `calc` (target ranks: base_value=80:4737, first_product=160:25998, bound_value=168:50038, second_product=336:30647, answer=321:85734)
- Layer 36: ` Tw`, `calcul`, `分解`, `acos`, `反复` (target ranks: base_value=80:8514, first_product=160:18934, bound_value=168:30943, second_product=336:18107, answer=321:94292)
- Layer 37: `}<?`, ` doubling`, `acos`, ` doubled`, ` multipliers` (target ranks: base_value=80:27896, first_product=160:40250, bound_value=168:61264, second_product=336:36840, answer=321:110087)
- Layer 38: `}<?`, `zat`, ` multipliers`, ` doubling`, ` multiplic` (target ranks: base_value=80:19364, first_product=160:54735, bound_value=168:64908, second_product=336:41471, answer=321:107392)
- Layer 39: `zat`, `mul`, `}<?`, ` mul`, ` multipliers` (target ranks: base_value=80:17907, first_product=160:69909, bound_value=168:75866, second_product=336:57402, answer=321:102974)
- Layer 40: ` mul`, `mul`, `mult`, ` multipliers`, `Mul` (target ranks: base_value=80:2184, first_product=160:35800, bound_value=168:19125, second_product=336:18365, answer=321:40959)
- Layer 41: `mul`, ` mul`, ` multipliers`, ` multiplier`, `mult` (target ranks: base_value=80:366, first_product=160:5178, bound_value=168:2244, second_product=336:1839, answer=321:3285)

### Filler position 36 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127466, first_product=160:125001, bound_value=168:126467, second_product=336:125782, answer=321:123770)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13101, first_product=160:23119, bound_value=168:19068, second_product=336:21862, answer=321:20702)
- Layer 20: `能被`, `拆`, `ait`, ` Walker`, `距` (target ranks: base_value=80:4819, first_product=160:23553, bound_value=168:18023, second_product=336:28297, answer=321:20976)
- Layer 30: `adaghan`, ` pools`, `卸`, `328`, ` unpack` (target ranks: base_value=80:5372, first_product=160:337, bound_value=168:2273, second_product=336:1524, answer=321:5941)
- Layer 35: `329`, `321`, `328`, `324`, `337` (target ranks: base_value=80:84867, first_product=160:54385, bound_value=168:61050, second_product=336:12, answer=321:2)
- Layer 36: `321`, `329`, `313`, `)Skip`, `311` (target ranks: base_value=80:128182, first_product=160:62028, bound_value=168:95873, second_product=336:34, answer=321:1)
- Layer 37: `321`, `329`, `313`, `)Skip`, `323` (target ranks: base_value=80:128893, first_product=160:87948, bound_value=168:90911, second_product=336:51, answer=321:1)
- Layer 38: `321`, `313`, `329`, `323`, `311` (target ranks: base_value=80:129271, first_product=160:127762, bound_value=168:125983, second_product=336:50, answer=321:1)
- Layer 39: `321`, `本题分析`, `322`, `313`, `323` (target ranks: base_value=80:128952, first_product=160:127494, bound_value=168:128274, second_product=336:45251, answer=321:1)
- Layer 40: `321`, `<｜begin▁of▁file｜>`, ` unflagged`, ` kinahabogang`, `本题分析` (target ranks: base_value=80:128447, first_product=160:128278, bound_value=168:126305, second_product=336:60622, answer=321:1)
- Layer 41: `321`, `印书馆`, ` dinhi`, `这种东西`, `试一试` (target ranks: base_value=80:114353, first_product=160:124049, bound_value=168:114864, second_product=336:72177, answer=321:1)

### Filler position 37 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127702, first_product=160:125252, bound_value=168:126702, second_product=336:125973, answer=321:124082)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13060, first_product=160:22981, bound_value=168:19125, second_product=336:22547, answer=321:21179)
- Layer 20: `能被`, `忑`, ` engaging`, `距`, ` smile` (target ranks: base_value=80:6523, first_product=160:30589, bound_value=168:21232, second_product=336:46572, answer=321:26141)
- Layer 30: `八十`, ` eighty`, `80`, ` Eighty`, `sac` (target ranks: base_value=80:3, first_product=160:199, bound_value=168:5848, second_product=336:43868, answer=321:107895)
- Layer 35: `168`, `obin`, `装`, ` binary`, `装了` (target ranks: base_value=80:12, first_product=160:7939, bound_value=168:1, second_product=336:23336, answer=321:107124)
- Layer 36: `168`, `翻`, `装`, `往外`, `radesh` (target ranks: base_value=80:64, first_product=160:3465, bound_value=168:1, second_product=336:12087, answer=321:112966)
- Layer 37: `168`, `}<?`, ` doubled`, `看书`, ` doubling` (target ranks: base_value=80:584, first_product=160:9114, bound_value=168:1, second_product=336:27536, answer=321:125111)
- Layer 38: `}<?`, `168`, ` doubled`, ` doubling`, `打包` (target ranks: base_value=80:1955, first_product=160:26460, bound_value=168:2, second_product=336:47555, answer=321:125398)
- Layer 39: `}<?`, ` Nij`, `enal`, ` doubled`, `东海` (target ranks: base_value=80:11733, first_product=160:79041, bound_value=168:1787, second_product=336:42948, answer=321:54460)
- Layer 40: `}<?`, ` triplet`, `erat`, `acular`, `翻` (target ranks: base_value=80:9967, first_product=160:78828, bound_value=168:91, second_product=336:1372, answer=321:30)
- Layer 41: ` triplet`, `erat`, `acular`, `321`, ` thirty` (target ranks: base_value=80:12735, first_product=160:44521, bound_value=168:50, second_product=336:919, answer=321:4)

### Filler position 38 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127735, first_product=160:125390, bound_value=168:126762, second_product=336:126061, answer=321:124221)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12243, first_product=160:21659, bound_value=168:18070, second_product=336:21408, answer=321:20021)
- Layer 20: `ait`, `忑`, `atile`, ` Walker`, ` ES` (target ranks: base_value=80:9950, first_product=160:39411, bound_value=168:27967, second_product=336:43515, answer=321:38219)
- Layer 30: `sac`, ` tap`, `acos`, `�`, `Tap` (target ranks: base_value=80:36669, first_product=160:97890, bound_value=168:95492, second_product=336:88403, answer=321:111566)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, `obin` (target ranks: base_value=80:20339, first_product=160:101034, bound_value=168:100769, second_product=336:101743, answer=321:93487)
- Layer 36: ` tap`, `留存`, `yg`, ` stabil`, `y` (target ranks: base_value=80:13218, first_product=160:66370, bound_value=168:78126, second_product=336:70632, answer=321:77788)
- Layer 37: `}<?`, `acet`, `dividers`, `acons`, `放下` (target ranks: base_value=80:25772, first_product=160:82456, bound_value=168:106453, second_product=336:93544, answer=321:92849)
- Layer 38: `}<?`, `zat`, `dividers`, `�`, `acet` (target ranks: base_value=80:27497, first_product=160:96350, bound_value=168:111027, second_product=336:97193, answer=321:85318)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `dividers`, `hemer`, `东海` (target ranks: base_value=80:46886, first_product=160:107343, bound_value=168:110874, second_product=336:82059, answer=321:59186)
- Layer 40: `acular`, `y`, `冰冰`, `zij`, ` Tw` (target ranks: base_value=80:13315, first_product=160:77801, bound_value=168:66468, second_product=336:31558, answer=321:1138)
- Layer 41: ` .`, ` `, `有下列`, `�`, `鹃` (target ranks: base_value=80:3174, first_product=160:17732, bound_value=168:8070, second_product=336:1339, answer=321:28)

### Filler position 39 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127750, first_product=160:125327, bound_value=168:126733, second_product=336:126024, answer=321:124156)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:11657, first_product=160:20993, bound_value=168:17631, second_product=336:20790, answer=321:19375)
- Layer 20: `ait`, `锁定`, `能被`, `鞍`, ` ES` (target ranks: base_value=80:6225, first_product=160:23197, bound_value=168:16752, second_product=336:25841, answer=321:23845)
- Layer 30: `acin`, ` pools`, `essa`, ` pool`, `obin` (target ranks: base_value=80:7479, first_product=160:541, bound_value=168:1032, second_product=336:1352, answer=321:16058)
- Layer 35: `329`, `328`, `321`, `essa`, `acin` (target ranks: base_value=80:41270, first_product=160:43381, bound_value=168:52199, second_product=336:178, answer=321:3)
- Layer 36: `321`, `313`, `329`, `305`, `328` (target ranks: base_value=80:113581, first_product=160:53124, bound_value=168:76104, second_product=336:148, answer=321:1)
- Layer 37: `}<?`, `321`, `313`, `329`, `ocyst` (target ranks: base_value=80:124796, first_product=160:81611, bound_value=168:84050, second_product=336:258, answer=321:2)
- Layer 38: `313`, `}<?`, `321`, `305`, `329` (target ranks: base_value=80:128393, first_product=160:122382, bound_value=168:121785, second_product=336:223, answer=321:3)
- Layer 39: `321`, `313`, `本题分析`, ` Fulton`, ` juicy` (target ranks: base_value=80:126613, first_product=160:126903, bound_value=168:128688, second_product=336:43484, answer=321:1)
- Layer 40: `321`, `acular`, ` mosunod`, `313`, `oise` (target ranks: base_value=80:124835, first_product=160:128074, bound_value=168:128573, second_product=336:48282, answer=321:1)
- Layer 41: `321`, `313`, ` .`, ` nuest`, ` waiting` (target ranks: base_value=80:58190, first_product=160:114589, bound_value=168:121174, second_product=336:9832, answer=321:1)

### Filler position 40 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127779, first_product=160:125497, bound_value=168:126861, second_product=336:126163, answer=321:124307)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12446, first_product=160:21912, bound_value=168:18753, second_product=336:21751, answer=321:20375)
- Layer 20: `ait`, `能被`, `啦啦`, ` Walker`, `鞍` (target ranks: base_value=80:3297, first_product=160:17203, bound_value=168:16074, second_product=336:17817, answer=321:18377)
- Layer 30: `acos`, ` smoot`, `陪`, `328`, `漂` (target ranks: base_value=80:2065, first_product=160:738, bound_value=168:129, second_product=336:620, answer=321:52497)
- Layer 35: `336`, `三十六`, `acin`, `陪`, `328` (target ranks: base_value=80:46017, first_product=160:48617, bound_value=168:1667, second_product=336:1, answer=321:1225)
- Layer 36: `336`, `三十六`, ` Pagbuok`, `326`, ` Gelijk` (target ranks: base_value=80:120978, first_product=160:49504, bound_value=168:16018, second_product=336:1, answer=321:105)
- Layer 37: `336`, ` Pagbuok`, ` hydrodynamic`, ` Gelijk`, `polar` (target ranks: base_value=80:121936, first_product=160:54433, bound_value=168:7239, second_product=336:1, answer=321:648)
- Layer 38: `336`, `326`, ` hydrodynamic`, `321`, `328` (target ranks: base_value=80:122904, first_product=160:54394, bound_value=168:4876, second_product=336:1, answer=321:4)
- Layer 39: `321`, `326`, `第三百`, `本题分析`, ` hydrodynamic` (target ranks: base_value=80:125512, first_product=160:127525, bound_value=168:127859, second_product=336:97, answer=321:1)
- Layer 40: `321`, `326`, ` mosunod`, `pping`, `思潮` (target ranks: base_value=80:99683, first_product=160:126589, bound_value=168:117384, second_product=336:36, answer=321:1)
- Layer 41: `321`, `326`, `329`, ` .`, `327` (target ranks: base_value=80:32440, first_product=160:97742, bound_value=168:51738, second_product=336:8, answer=321:1)

### Filler position 41 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127627, first_product=160:125282, bound_value=168:126691, second_product=336:125991, answer=321:124065)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12196, first_product=160:21664, bound_value=168:18334, second_product=336:21469, answer=321:19926)
- Layer 20: `ait`, `锁定`, ` smile`, `ession`, ` LS` (target ranks: base_value=80:4765, first_product=160:18147, bound_value=168:12377, second_product=336:22597, answer=321:16861)
- Layer 30: ` eighty`, `八十`, `acos`, `tail`, `陪` (target ranks: base_value=80:582, first_product=160:1610, bound_value=168:297, second_product=336:25614, answer=321:116888)
- Layer 35: `168`, `tub`, `康熙`, `装`, ` tub` (target ranks: base_value=80:1107, first_product=160:52041, bound_value=168:1, second_product=336:4558, answer=321:101864)
- Layer 36: `168`, `康熙`, ` Tub`, `tub`, `}<?` (target ranks: base_value=80:3435, first_product=160:28843, bound_value=168:1, second_product=336:358, answer=321:112151)
- Layer 37: `168`, `}<?`, ` Tub`, `康熙`, `tub` (target ranks: base_value=80:24111, first_product=160:58413, bound_value=168:1, second_product=336:2799, answer=321:122627)
- Layer 38: `168`, `}<?`, ` Tub`, `康熙`, `打包` (target ranks: base_value=80:42647, first_product=160:59821, bound_value=168:1, second_product=336:4407, answer=321:118723)
- Layer 39: `}<?`, `本题分析`, `看书`, `�`, `erer` (target ranks: base_value=80:47634, first_product=160:111871, bound_value=168:73, second_product=336:12209, answer=321:60346)
- Layer 40: ` multiply`, `}<?`, ` multiplic`, ` triplet`, ` Tw` (target ranks: base_value=80:7320, first_product=160:107361, bound_value=168:1004, second_product=336:1422, answer=321:165)
- Layer 41: ` .`, ` triplet`, ` Tw`, ` multiplier`, ` ;` (target ranks: base_value=80:3746, first_product=160:69828, bound_value=168:124, second_product=336:253, answer=321:23)

### Filler position 42 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127743, first_product=160:125369, bound_value=168:126761, second_product=336:126037, answer=321:124161)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12502, first_product=160:21765, bound_value=168:18191, second_product=336:21393, answer=321:20193)
- Layer 20: ` smile`, `鞍`, `锁定`, `cape`, `足` (target ranks: base_value=80:4289, first_product=160:13148, bound_value=168:8931, second_product=336:16142, answer=321:10288)
- Layer 30: `acos`, `陪`, ` amplified`, ` iceberg`, `反复` (target ranks: base_value=80:11295, first_product=160:5815, bound_value=168:11345, second_product=336:4069, answer=321:33486)
- Layer 35: `陪`, `�`, `兴趣`, ` reverber`, `radesh` (target ranks: base_value=80:37126, first_product=160:53895, bound_value=168:68241, second_product=336:3129, answer=321:2270)
- Layer 36: `bergh`, `radesh`, `陪`, `汉堡`, ` Gikuha` (target ranks: base_value=80:83218, first_product=160:58647, bound_value=168:93462, second_product=336:8381, answer=321:530)
- Layer 37: `}<?`, `polar`, `-ulo`, `本题分析`, `)Skip` (target ranks: base_value=80:108038, first_product=160:71721, bound_value=168:86181, second_product=336:8802, answer=321:2967)
- Layer 38: `}<?`, `polar`, `本题分析`, ` polar`, `把孩子` (target ranks: base_value=80:121520, first_product=160:94708, bound_value=168:100060, second_product=336:5183, answer=321:94)
- Layer 39: `321`, `本题分析`, `-ulo`, `329`, `313` (target ranks: base_value=80:117942, first_product=160:124339, bound_value=168:127903, second_product=336:5888, answer=321:1)
- Layer 40: `321`, `313`, ` `, `329`, ` .` (target ranks: base_value=80:82303, first_product=160:119316, bound_value=168:114265, second_product=336:1713, answer=321:1)
- Layer 41: `321`, ` .`, `313`, `329`, ` ` (target ranks: base_value=80:9441, first_product=160:64430, bound_value=168:55893, second_product=336:184, answer=321:1)

### Filler position 43 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127790, first_product=160:125558, bound_value=168:126872, second_product=336:126204, answer=321:124339)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12698, first_product=160:22064, bound_value=168:18220, second_product=336:21759, answer=321:20941)
- Layer 20: ` smile`, `ait`, `锁定`, `鞍`, ` LS` (target ranks: base_value=80:3535, first_product=160:14426, bound_value=168:11966, second_product=336:23181, answer=321:16880)
- Layer 30: ` eighty`, `iab`, `八十`, ` twice`, `otan` (target ranks: base_value=80:343, first_product=160:614, bound_value=168:378, second_product=336:8237, answer=321:113952)
- Layer 35: `336`, `335`, `冰冰`, ` Gikuha`, `337` (target ranks: base_value=80:3461, first_product=160:67201, bound_value=168:44, second_product=336:1, answer=321:75839)
- Layer 36: `336`, `335`, `337`, `}<?`, `<｜place▁holder▁no▁381｜>` (target ranks: base_value=80:27683, first_product=160:74920, bound_value=168:61, second_product=336:1, answer=321:67915)
- Layer 37: `336`, `}<?`, `)Skip`, `337`, `335` (target ranks: base_value=80:41908, first_product=160:64370, bound_value=168:19, second_product=336:1, answer=321:108627)
- Layer 38: `336`, `}<?`, `337`, `<｜place▁holder▁no▁381｜>`, `335` (target ranks: base_value=80:34133, first_product=160:84349, bound_value=168:29, second_product=336:1, answer=321:87940)
- Layer 39: `336`, `337`, `}<?`, `335`, `语言文字` (target ranks: base_value=80:19918, first_product=160:101199, bound_value=168:402, second_product=336:1, answer=321:15637)
- Layer 40: `336`, `语言文字`, ` multiplied`, `337`, ` multiply` (target ranks: base_value=80:2771, first_product=160:89428, bound_value=168:352, second_product=336:1, answer=321:17)
- Layer 41: `336`, `337`, ` triplet`, `313`, `321` (target ranks: base_value=80:456, first_product=160:30988, bound_value=168:86, second_product=336:1, answer=321:5)

### Filler position 44 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127787, first_product=160:125390, bound_value=168:126790, second_product=336:126041, answer=321:124224)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:13344, first_product=160:22656, bound_value=168:18356, second_product=336:21493, answer=321:21700)
- Layer 20: `能被`, `ait`, ` Walker`, ` ES`, `距` (target ranks: base_value=80:5947, first_product=160:21368, bound_value=168:17797, second_product=336:32834, answer=321:29321)
- Layer 30: ` eighty`, ` pakig`, `sar`, ` smoot`, `八十` (target ranks: base_value=80:415, first_product=160:605, bound_value=168:1440, second_product=336:6881, answer=321:105715)
- Layer 35: `三十六`, `冰冰`, `acin`, `336`, ` ternary` (target ranks: base_value=80:978, first_product=160:41707, bound_value=168:830, second_product=336:4, answer=321:56008)
- Layer 36: `}<?`, `336`, `翻了`, ` polar`, `冰冰` (target ranks: base_value=80:11564, first_product=160:47861, bound_value=168:682, second_product=336:2, answer=321:69088)
- Layer 37: `}<?`, `ivin`, `polar`, `336`, ` polar` (target ranks: base_value=80:31278, first_product=160:42208, bound_value=168:72, second_product=336:4, answer=321:113046)
- Layer 38: `}<?`, `polar`, `ivin`, ` polar`, `336` (target ranks: base_value=80:44905, first_product=160:43516, bound_value=168:40, second_product=336:5, answer=321:94832)
- Layer 39: `336`, `三百`, `}<?`, `polar`, `文字的` (target ranks: base_value=80:59400, first_product=160:111550, bound_value=168:5058, second_product=336:1, answer=321:758)
- Layer 40: `321`, `336`, `313`, `三百`, `337` (target ranks: base_value=80:20363, first_product=160:101114, bound_value=168:1142, second_product=336:2, answer=321:1)
- Layer 41: `321`, `336`, `313`, ` .`, `337` (target ranks: base_value=80:6402, first_product=160:47628, bound_value=168:330, second_product=336:2, answer=321:1)

### Filler position 45 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=80:127893, first_product=160:125593, bound_value=168:126917, second_product=336:126231, answer=321:124436)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=80:12826, first_product=160:22147, bound_value=168:17703, second_product=336:20893, answer=321:20780)
- Layer 20: `ait`, ` Walker`, `会成为`, `妇`, `锁定` (target ranks: base_value=80:9829, first_product=160:25460, bound_value=168:20475, second_product=336:38293, answer=321:42968)
- Layer 30: `Mul`, `mul`, ` mul`, ` Mul`, ` mulch` (target ranks: base_value=80:35732, first_product=160:88837, bound_value=168:117505, second_product=336:113415, answer=321:127661)
- Layer 35: ` mul`, `Mul`, ` Mul`, `mul`, ` mun` (target ranks: base_value=80:14169, first_product=160:69127, bound_value=168:113846, second_product=336:107840, answer=321:121079)
- Layer 36: ` mul`, ` Mul`, `mul`, `Mul`, `留存` (target ranks: base_value=80:10760, first_product=160:34448, bound_value=168:79341, second_product=336:68816, answer=321:113261)
- Layer 37: ` mul`, `mul`, ` Mul`, `Mul`, `}<?` (target ranks: base_value=80:34996, first_product=160:60146, bound_value=168:106543, second_product=336:90904, answer=321:119656)
- Layer 38: ` mul`, `mul`, ` Mul`, `Mul`, `mult` (target ranks: base_value=80:23343, first_product=160:58451, bound_value=168:105417, second_product=336:84826, answer=321:108083)
- Layer 39: `mul`, ` mul`, ` Mul`, `Mul`, `mult` (target ranks: base_value=80:29138, first_product=160:72817, bound_value=168:94508, second_product=336:49911, answer=321:78738)
- Layer 40: `mul`, ` mul`, `mult`, ` Mul`, `Mul` (target ranks: base_value=80:2889, first_product=160:36531, bound_value=168:30497, second_product=336:8468, answer=321:2508)
- Layer 41: `mul`, ` mul`, ` .`, ` whichever`, ` seventy` (target ranks: base_value=80:1029, first_product=160:10873, bound_value=168:8674, second_product=336:1354, answer=321:159)

### Filler position 46 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127730, first_product=160:125379, bound_value=168:126814, second_product=336:126033, answer=321:124160)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=80:12452, first_product=160:21641, bound_value=168:17682, second_product=336:20798, answer=321:20235)
- Layer 20: `blank`, ` blanks`, ` Blank`, `空白`, ` blank` (target ranks: base_value=80:66162, first_product=160:52545, bound_value=168:76653, second_product=336:81741, answer=321:112018)
- Layer 30: ` spac`, `?datasetId`, `坝`, ` dekameters`, `}using` (target ranks: base_value=80:112078, first_product=160:96271, bound_value=168:111578, second_product=336:102299, answer=321:118893)
- Layer 35: `足足`, `}using`, `坏`, `dots`, `俯` (target ranks: base_value=80:92307, first_product=160:110297, bound_value=168:112172, second_product=336:104152, answer=321:121068)
- Layer 36: `足足`, `俯`, `ancock`, ` blank`, ` reduct` (target ranks: base_value=80:42354, first_product=160:72535, bound_value=168:69249, second_product=336:72774, answer=321:104175)
- Layer 37: `}<?`, `isis`, `onana`, `放下`, ` doubling` (target ranks: base_value=80:66178, first_product=160:82205, bound_value=168:111007, second_product=336:80207, answer=321:105542)
- Layer 38: ` .`, `坏`, ` Wilson`, `错过`, ` Weston` (target ranks: base_value=80:26693, first_product=160:60618, bound_value=168:89277, second_product=336:78803, answer=321:98894)
- Layer 39: `hatic`, ` .`, `aharan`, `ozygous`, `}<?` (target ranks: base_value=80:48959, first_product=160:95778, bound_value=168:92200, second_product=336:47908, answer=321:46478)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, `�`, ` x` (target ranks: base_value=80:11583, first_product=160:55157, bound_value=168:45055, second_product=336:13185, answer=321:8700)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=80:4457, first_product=160:8628, bound_value=168:7166, second_product=336:1372, answer=321:604)

### Filler position 47 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127768, first_product=160:125415, bound_value=168:126880, second_product=336:126099, answer=321:124247)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=80:11944, first_product=160:21245, bound_value=168:17710, second_product=336:20589, answer=321:19865)
- Layer 20: `}<?`, `东海`, `ozygous`, ` partly`, ` DeWalt` (target ranks: base_value=80:93225, first_product=160:74422, bound_value=168:111563, second_product=336:105912, answer=321:117558)
- Layer 30: `}<?`, `codeline`, `?datasetId`, `}using`, `dividers` (target ranks: base_value=80:90672, first_product=160:101245, bound_value=168:108007, second_product=336:107601, answer=321:120339)
- Layer 35: `codeline`, `ِّف`, `}using`, `浪费`, `dividers` (target ranks: base_value=80:98111, first_product=160:122780, bound_value=168:121656, second_product=336:119454, answer=321:126556)
- Layer 36: ` nasod`, `足足`, `锯`, `切割`, ` fit` (target ranks: base_value=80:47083, first_product=160:98757, bound_value=168:96352, second_product=336:98399, answer=321:121648)
- Layer 37: `磨损`, `在东`, `الميل`, `}<?`, `东京` (target ranks: base_value=80:61024, first_product=160:86057, bound_value=168:107566, second_product=336:79424, answer=321:114443)
- Layer 38: ` .`, ` prese`, `遁`, `lett`, `切割` (target ranks: base_value=80:30738, first_product=160:52540, bound_value=168:88569, second_product=336:71107, answer=321:105894)
- Layer 39: ` .`, `坏`, `lett`, ` unflagged`, `磨损` (target ranks: base_value=80:82678, first_product=160:85543, bound_value=168:89504, second_product=336:48547, answer=321:48252)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, `坏` (target ranks: base_value=80:38484, first_product=160:50693, bound_value=168:45721, second_product=336:14691, answer=321:13310)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` ` (target ranks: base_value=80:11441, first_product=160:7353, bound_value=168:8880, second_product=336:674, answer=321:353)

### Filler position 48 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127789, first_product=160:125421, bound_value=168:126898, second_product=336:126097, answer=321:124269)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=80:11811, first_product=160:21311, bound_value=168:17938, second_product=336:20455, answer=321:19901)
- Layer 20: `}<?`, `aharoa`, `aplenty`, `)Skip`, `东海` (target ranks: base_value=80:83093, first_product=160:64927, bound_value=168:93615, second_product=336:103745, answer=321:103105)
- Layer 30: `codeline`, ` slipp`, ` accompanying`, `Quintal`, `lett` (target ranks: base_value=80:37316, first_product=160:69835, bound_value=168:103199, second_product=336:83988, answer=321:116663)
- Layer 35: `codeline`, `AssemblyVersion`, ` doubly`, ` fif`, `白雪` (target ranks: base_value=80:18556, first_product=160:111934, bound_value=168:123507, second_product=336:102829, answer=321:121100)
- Layer 36: ` soci`, ` nasod`, `yss`, `停`, ` reduct` (target ranks: base_value=80:6080, first_product=160:71996, bound_value=168:104095, second_product=336:72473, answer=321:115644)
- Layer 37: `codeline`, `TreeLabel`, `镶嵌`, `Quintal`, `cault` (target ranks: base_value=80:37697, first_product=160:79615, bound_value=168:119058, second_product=336:80949, answer=321:122190)
- Layer 38: `肤`, ` .`, ` germ`, ` nasod`, `悬` (target ranks: base_value=80:29944, first_product=160:73903, bound_value=168:116836, second_product=336:78976, answer=321:111430)
- Layer 39: ` .`, ` unflagged`, ` .↵↵`, `肤`, ` encomp` (target ranks: base_value=80:83048, first_product=160:100707, bound_value=168:113342, second_product=336:88345, answer=321:104417)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` germ` (target ranks: base_value=80:54297, first_product=160:70345, bound_value=168:102135, second_product=336:67716, answer=321:72483)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=80:11913, first_product=160:12056, bound_value=168:26601, second_product=336:13158, answer=321:14780)

### Filler position 49 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=80:127610, first_product=160:125224, bound_value=168:126694, second_product=336:125932, answer=321:124069)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=80:11855, first_product=160:21650, bound_value=168:18348, second_product=336:20975, answer=321:20057)
- Layer 20: ` licensierad`, `aplenty`, ` instantaneous`, ` grounds`, `zv` (target ranks: base_value=80:70019, first_product=160:85344, bound_value=168:98780, second_product=336:101208, answer=321:78808)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, `答案为` (target ranks: base_value=80:116689, first_product=160:118681, bound_value=168:128783, second_product=336:113849, answer=321:125669)
- Layer 35: ` Answer`, `codeline`, `oNames`, `理性的`, ` retard` (target ranks: base_value=80:83719, first_product=160:114255, bound_value=168:128558, second_product=336:120574, answer=321:122956)
- Layer 36: `坏`, ` Answer`, `停顿`, `停`, ` nasod` (target ranks: base_value=80:25275, first_product=160:83170, bound_value=168:124085, second_product=336:95059, answer=321:110158)
- Layer 37: `oNames`, ` consum`, `codeline`, `insic`, `оду` (target ranks: base_value=80:114414, first_product=160:114852, bound_value=168:128043, second_product=336:121492, answer=321:128239)
- Layer 38: `oNames`, ` retard`, `оду`, `<|EOT|>`, `.Advertisement` (target ranks: base_value=80:111933, first_product=160:114834, bound_value=168:127560, second_product=336:117535, answer=321:127035)
- Layer 39: ` unflagged`, `�`, `oxygen`, `deen`, ` Totient` (target ranks: base_value=80:91000, first_product=160:120863, bound_value=168:125981, second_product=336:87588, answer=321:98517)
- Layer 40: ` .`, ` .↵↵`, ` Answer`, ` nasod`, ` wink` (target ranks: base_value=80:21359, first_product=160:89950, bound_value=168:105985, second_product=336:34269, answer=321:23416)
- Layer 41: ` .`, ` .↵↵`, ` Answer`, `Answer`, `叮` (target ranks: base_value=80:14559, first_product=160:65323, bound_value=168:71758, second_product=336:27198, answer=321:22226)

### Filler position 50 (absolute token 834, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=80:121162, first_product=160:111205, bound_value=168:115775, second_product=336:114382, answer=321:114023)
- Layer 10: `EDMF`, ` dével`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=80:125283, first_product=160:103708, bound_value=168:117510, second_product=336:113697, answer=321:108068)
- Layer 20: `能被`, ` Submission`, `ait`, ` ChatGPT`, `能得到` (target ranks: base_value=80:15452, first_product=160:53207, bound_value=168:52345, second_product=336:72335, answer=321:34383)
- Layer 30: `nze`, ` unflagged`, ` mach`, ` dátummal`, ` interpretations` (target ranks: base_value=80:60355, first_product=160:1962, bound_value=168:5747, second_product=336:16927, answer=321:68234)
- Layer 35: `336`, `332`, `329`, `335`, `331` (target ranks: base_value=80:120295, first_product=160:90565, bound_value=168:64182, second_product=336:1, answer=321:44)
- Layer 36: `321`, `336`, `329`, `326`, ` giiniton` (target ranks: base_value=80:128702, first_product=160:102430, bound_value=168:51826, second_product=336:2, answer=321:1)
- Layer 37: `336`, `321`, ` giiniton`, `329`, ` Pagbuok` (target ranks: base_value=80:128697, first_product=160:104789, bound_value=168:31020, second_product=336:1, answer=321:2)
- Layer 38: `321`, `336`, `326`, `341`, `329` (target ranks: base_value=80:129047, first_product=160:124683, bound_value=168:53738, second_product=336:2, answer=321:1)
- Layer 39: `321`, ` dátummal`, `320`, `秧`, `341` (target ranks: base_value=80:128836, first_product=160:128806, bound_value=168:126094, second_product=336:2482, answer=321:1)
- Layer 40: `Answer`, ` Answer`, `_answer`, ` answer`, `answer` (target ranks: base_value=80:127477, first_product=160:126868, bound_value=168:110811, second_product=336:2210, answer=321:7)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `_answer` (target ranks: base_value=80:42255, first_product=160:66904, bound_value=168:29054, second_product=336:2836, answer=321:24)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a list of variable definitions followed by a question. Each variable equals either a number or an expression that refers to an earlier variable (for example 'twice the number for X plus 3'). Resolve the references to work out the value the question asks for, then answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 50 filler tokens (a sequence of dots) before you answer.<｜User｜>zab = 45
piy = 43
xoc = twice the number for zab plus 7
lej = twice the number for zab plus 3
kox = 45
Question: What is twice the number for xoc minus 18?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>176<｜end▁of▁sentence｜><｜User｜>cem = 20
pij = twice the number for cem plus 20
kes = twice the number for pij minus 30
kaq = twice the number for cem minus 21
ciq = twice the number for kaq plus 7
Question: What is twice the number for kaq plus 21?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>59<｜end▁of▁sentence｜><｜User｜>gew = 78
xop = twice the number for gew plus 17
doq = twice the number for gew minus 18
ful = twice the number for gew plus 10
biv = twice the number for ful plus 28
Question: What is twice the number for xop plus 5?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>351<｜end▁of▁sentence｜><｜User｜>mec = 40
xad = twice the number for mec plus 25
gow = twice the number for mec minus 17
juj = twice the number for xad minus 22
vof = twice the number for juj plus 3
Question: What is twice the number for xad plus 19?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>229<｜end▁of▁sentence｜><｜User｜>kac = 52
duk = twice the number for kac minus 7
jaf = twice the number for duk minus 14
cac = twice the number for jaf minus 26
zub = twice the number for duk plus 6
Question: What is twice the number for duk minus 16?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>daq = 75
neq = 72
mul = 80
ciz = twice the number for mul plus 8
ziz = 63
Question: What is twice the number for ciz minus 15?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
