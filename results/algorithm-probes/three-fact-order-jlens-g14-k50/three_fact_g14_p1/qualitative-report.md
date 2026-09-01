# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `119` (correct).
- No-filler answer: `119` (correct).
- Filler tokens: 50 tokens at absolute indices 516–565.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `fact_1=6` | 2 (L41, filler 32) | L35, filler 42 (rank 9) |
| J-Lens | `fact_2=92` | 1 (L35, filler 1) | L34, filler 1 (rank 6) |
| J-Lens | `fact_3=21` | 1 (L34, filler 29) | L34, filler 29 (rank 1) |
| J-Lens | `prefix_sum_12=98` | 3 (L38, filler 50) | L35, filler 39 (rank 10) |
| J-Lens | `sum=119` | 3 (L39, filler 9) | L38, filler 9 (rank 10) |
| Logit lens | `fact_1=6` | 1 (L39, filler 32) | L35, filler 32 (rank 8) |
| Logit lens | `fact_2=92` | 1 (L35, filler 1) | L34, filler 9 (rank 5) |
| Logit lens | `fact_3=21` | 1 (L34, filler 37) | L34, filler 14 (rank 8) |
| Logit lens | `prefix_sum_12=98` | 32 (L36, filler 39) | Never |
| Logit lens | `sum=119` | 3 (L39, filler 9) | L39, filler 9 (rank 3) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 516, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: fact_1=6:125205, fact_2=92:117841, fact_3=21:120940, prefix_sum_12=98:118736, sum=119:114401)
- Layer 10: `anta`, `locked`, `fine`, `Walker`, `s` (target ranks: fact_1=6:25136, fact_2=92:46950, fact_3=21:33592, prefix_sum_12=98:32460, sum=119:50296)
- Layer 20: `足`, `甸`, `表面`, `旬`, `abric` (target ranks: fact_1=6:41, fact_2=92:1283, fact_3=21:657, prefix_sum_12=98:494, sum=119:20399)
- Layer 30: ` pakig`, ` talags`, `uir`, ` procedural`, `期望` (target ranks: fact_1=6:18518, fact_2=92:1682, fact_3=21:18545, prefix_sum_12=98:5470, sum=119:31520)
- Layer 35: `92`, `93`, `88`, `86`, `90` (target ranks: fact_1=6:2922, fact_2=92:1, fact_3=21:2188, prefix_sum_12=98:24, sum=119:19969)
- Layer 36: `92`, `93`, `88`, `86`, `九十` (target ranks: fact_1=6:18141, fact_2=92:1, fact_3=21:30150, prefix_sum_12=98:19, sum=119:7266)
- Layer 37: `92`, `93`, `}<?`, ` ninety`, `九十` (target ranks: fact_1=6:82323, fact_2=92:1, fact_3=21:43142, prefix_sum_12=98:26, sum=119:9664)
- Layer 38: `}<?`, `92`, `93`, ` ninety`, ` Ninety` (target ranks: fact_1=6:104493, fact_2=92:2, fact_3=21:91657, prefix_sum_12=98:13, sum=119:1210)
- Layer 39: `}<?`, `本题分析`, `tanle`, `ople`, `odea` (target ranks: fact_1=6:45215, fact_2=92:30312, fact_3=21:64692, prefix_sum_12=98:26232, sum=119:9289)
- Layer 40: ` talags`, `atomic`, `scrib`, `}<?`, ` atomic` (target ranks: fact_1=6:1490, fact_2=92:18320, fact_3=21:11141, prefix_sum_12=98:26390, sum=119:6081)
- Layer 41: ` .`, `癫�`, `我已经`, ` .↵↵`, ` ...` (target ranks: fact_1=6:7706, fact_2=92:31827, fact_3=21:15908, prefix_sum_12=98:29217, sum=119:29485)

### Filler position 2 (absolute token 517, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: fact_1=6:125172, fact_2=92:120523, fact_3=21:122636, prefix_sum_12=98:121114, sum=119:118417)
- Layer 10: ` Walker`, `从哪里`, `Walker`, `ait`, `atile` (target ranks: fact_1=6:6774, fact_2=92:28205, fact_3=21:17314, prefix_sum_12=98:26953, sum=119:41555)
- Layer 20: ` .----`, `往常`, ` .`, `平日里`, ` Millenniums` (target ranks: fact_1=6:124019, fact_2=92:129006, fact_3=21:125029, prefix_sum_12=98:128302, sum=119:129200)
- Layer 30: ` talags`, ` dekameters`, ` hilabihan`, ` pakig`, ` gilay` (target ranks: fact_1=6:124156, fact_2=92:129200, fact_3=21:124193, prefix_sum_12=98:127277, sum=119:128702)
- Layer 35: ` hilabihan`, ` .`, `}<?`, ` talags`, ` gihulagway` (target ranks: fact_1=6:124912, fact_2=92:128651, fact_3=21:118177, prefix_sum_12=98:124538, sum=119:128401)
- Layer 36: ` hilabihan`, `enclose`, ` .`, ` talags`, `停` (target ranks: fact_1=6:74349, fact_2=92:122405, fact_3=21:63100, prefix_sum_12=98:92632, sum=119:120538)
- Layer 37: `}<?`, ` hilabihan`, `�乐`, `aplenty`, `EDMF` (target ranks: fact_1=6:127876, fact_2=92:128240, fact_3=21:123893, prefix_sum_12=98:112755, sum=119:122525)
- Layer 38: ` .`, `}<?`, ` hilabihan`, `繁体`, ` .↵↵` (target ranks: fact_1=6:126100, fact_2=92:127677, fact_3=21:107387, prefix_sum_12=98:112429, sum=119:119888)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, ` +:+`, ` talags`, `}<?` (target ranks: fact_1=6:125641, fact_2=92:128141, fact_3=21:124464, prefix_sum_12=98:125251, sum=119:123987)
- Layer 40: ` .`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` .↵`, ` nasod` (target ranks: fact_1=6:84771, fact_2=92:123343, fact_3=21:93568, prefix_sum_12=98:108473, sum=119:98969)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `美`, ` ,` (target ranks: fact_1=6:24576, fact_2=92:98986, fact_3=21:63375, prefix_sum_12=98:37609, sum=119:63521)

### Filler position 3 (absolute token 518, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=6:127366, fact_2=92:123161, fact_3=21:125106, prefix_sum_12=98:123939, sum=119:119785)
- Layer 10: ` Walker`, `锁定`, `ait`, `Walker`, `忑` (target ranks: fact_1=6:4191, fact_2=92:12668, fact_3=21:8974, prefix_sum_12=98:12428, sum=119:22794)
- Layer 20: `ative`, `cape`, `3`, ` ternary`, `ka` (target ranks: fact_1=6:33, fact_2=92:1882, fact_3=21:105, prefix_sum_12=98:847, sum=119:13116)
- Layer 30: ` Heim`, ` radioactive`, `atomic`, ` cosmic`, `sac` (target ranks: fact_1=6:43277, fact_2=92:9227, fact_3=21:2158, prefix_sum_12=98:9732, sum=119:24474)
- Layer 35: `92`, `}<?`, `91`, `uran`, `二十一` (target ranks: fact_1=6:106444, fact_2=92:1, fact_3=21:7, prefix_sum_12=98:195, sum=119:16609)
- Layer 36: `92`, `91`, `二十一`, ` ninety`, `}<?` (target ranks: fact_1=6:126295, fact_2=92:1, fact_3=21:7, prefix_sum_12=98:335, sum=119:31262)
- Layer 37: `92`, `91`, `二十一`, ` ninety`, ` XXI` (target ranks: fact_1=6:128480, fact_2=92:1, fact_3=21:7, prefix_sum_12=98:358, sum=119:33960)
- Layer 38: `92`, `91`, `二十一`, ` ninety`, `21` (target ranks: fact_1=6:128193, fact_2=92:1, fact_3=21:5, prefix_sum_12=98:538, sum=119:7595)
- Layer 39: `二十一`, `21`, ` XXI`, `ucl`, `}<?` (target ranks: fact_1=6:48518, fact_2=92:17, fact_3=21:2, prefix_sum_12=98:72431, sum=119:11203)
- Layer 40: `二十一`, `}<?`, `uran`, `<｜begin▁of▁file｜>`, `anium` (target ranks: fact_1=6:271, fact_2=92:61, fact_3=21:11, prefix_sum_12=98:35165, sum=119:1239)
- Layer 41: ` .`, `��`, ` .↵↵`, `人人都`, ` ,` (target ranks: fact_1=6:536, fact_2=92:4686, fact_3=21:541, prefix_sum_12=98:36433, sum=119:33591)

### Filler position 4 (absolute token 519, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:127629, fact_2=92:123645, fact_3=21:125736, prefix_sum_12=98:124256, sum=119:120877)
- Layer 10: ` Walker`, `ait`, `Walker`, `锁定`, `忑` (target ranks: fact_1=6:5549, fact_2=92:17696, fact_3=21:12288, prefix_sum_12=98:15849, sum=119:26697)
- Layer 20: `ait`, `忑`, `cape`, `atable`, ` wig` (target ranks: fact_1=6:3256, fact_2=92:24549, fact_3=21:16094, prefix_sum_12=98:33649, sum=119:47974)
- Layer 30: `期望`, `回答`, `Tap`, `answers`, `tap` (target ranks: fact_1=6:1345, fact_2=92:9884, fact_3=21:5973, prefix_sum_12=98:29380, sum=119:23160)
- Layer 35: `acks`, `期望`, `回答`, `�`, ` dy` (target ranks: fact_1=6:1581, fact_2=92:4654, fact_3=21:2023, prefix_sum_12=98:8065, sum=119:4906)
- Layer 36: `期望`, `acks`, ` dy`, ` repeated`, `期待` (target ranks: fact_1=6:1384, fact_2=92:1715, fact_3=21:4391, prefix_sum_12=98:2243, sum=119:1129)
- Layer 37: `本题分析`, `期望`, `136`, `114`, ` RI` (target ranks: fact_1=6:8429, fact_2=92:1109, fact_3=21:14584, prefix_sum_12=98:2595, sum=119:280)
- Layer 38: `本题分析`, ` Erkännande`, `interpret`, `}<?`, `打磨` (target ranks: fact_1=6:23504, fact_2=92:13541, fact_3=21:50947, prefix_sum_12=98:17959, sum=119:1341)
- Layer 39: `本题分析`, `}<?`, `东海`, `ophe`, `hemer` (target ranks: fact_1=6:86014, fact_2=92:87072, fact_3=21:110598, prefix_sum_12=98:29284, sum=119:2683)
- Layer 40: `apon`, `105`, ` repeated`, `脏`, ` cent` (target ranks: fact_1=6:19364, fact_2=92:77878, fact_3=21:89433, prefix_sum_12=98:13939, sum=119:1059)
- Layer 41: ` .`, `样子`, `你觉得`, `Answer`, ` ` (target ranks: fact_1=6:3434, fact_2=92:67301, fact_3=21:39175, prefix_sum_12=98:16511, sum=119:9553)

### Filler position 5 (absolute token 520, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:127385, fact_2=92:123197, fact_3=21:125532, prefix_sum_12=98:123748, sum=119:120781)
- Layer 10: ` Walker`, `Walker`, `锁定`, `ait`, `挪` (target ranks: fact_1=6:5163, fact_2=92:16112, fact_3=21:10882, prefix_sum_12=98:14611, sum=119:26078)
- Layer 20: ` LS`, `能被`, `幽`, `挪`, `LS` (target ranks: fact_1=6:532, fact_2=92:8706, fact_3=21:3476, prefix_sum_12=98:5712, sum=119:23452)
- Layer 30: ` pakig`, ` uranium`, ` proced`, ` radioactive`, ` atomic` (target ranks: fact_1=6:22364, fact_2=92:12411, fact_3=21:18565, prefix_sum_12=98:12615, sum=119:24341)
- Layer 35: ` uranium`, ` Uran`, `92`, `铀`, ` Uranus` (target ranks: fact_1=6:3659, fact_2=92:3, fact_3=21:26563, prefix_sum_12=98:201, sum=119:5674)
- Layer 36: `92`, ` Uran`, ` ninety`, `九十`, ` uranium` (target ranks: fact_1=6:34806, fact_2=92:1, fact_3=21:118866, prefix_sum_12=98:39, sum=119:8005)
- Layer 37: `92`, ` ninety`, `九十`, `91`, ` noventa` (target ranks: fact_1=6:93121, fact_2=92:1, fact_3=21:122466, prefix_sum_12=98:21, sum=119:4011)
- Layer 38: `92`, ` ninety`, ` Uran`, ` Ninety`, ` uranium` (target ranks: fact_1=6:119758, fact_2=92:1, fact_3=21:126994, prefix_sum_12=98:8, sum=119:3548)
- Layer 39: ` Uran`, `}<?`, `uran`, ` uranium`, `ucl` (target ranks: fact_1=6:79970, fact_2=92:1683, fact_3=21:45178, prefix_sum_12=98:3535, sum=119:2792)
- Layer 40: ` Uran`, `atomic`, ` atomic`, ` uranium`, `uran` (target ranks: fact_1=6:9108, fact_2=92:937, fact_3=21:6840, prefix_sum_12=98:1994, sum=119:1887)
- Layer 41: ` .`, ` atomic`, `atomic`, `人人都`, `大意` (target ranks: fact_1=6:1575, fact_2=92:15248, fact_3=21:7932, prefix_sum_12=98:19712, sum=119:22211)

### Filler position 6 (absolute token 521, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:127044, fact_2=92:122658, fact_3=21:125019, prefix_sum_12=98:123131, sum=119:120049)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:4235, fact_2=92:12772, fact_3=21:9850, prefix_sum_12=98:12203, sum=119:23484)
- Layer 20: `足`, `ting`, `cape`, `鞍`, `�` (target ranks: fact_1=6:4084, fact_2=92:17245, fact_3=21:8769, prefix_sum_12=98:25599, sum=119:44958)
- Layer 30: `回答`, ` Answer`, `鞍`, `tap`, ` answer` (target ranks: fact_1=6:2075, fact_2=92:586, fact_3=21:2371, prefix_sum_12=98:2869, sum=119:20962)
- Layer 35: `acks`, `回答`, ` smile`, `足`, ` tib` (target ranks: fact_1=6:1222, fact_2=92:90, fact_3=21:261, prefix_sum_12=98:311, sum=119:442)
- Layer 36: `acks`, `agli`, ` rip`, ` anxious`, ` stabil` (target ranks: fact_1=6:10021, fact_2=92:991, fact_3=21:2303, prefix_sum_12=98:1737, sum=119:1570)
- Layer 37: `acks`, `agli`, `贤`, `诚`, `理性的` (target ranks: fact_1=6:26516, fact_2=92:3840, fact_3=21:7130, prefix_sum_12=98:7858, sum=119:784)
- Layer 38: ` medief`, ` Rutherford`, `贤`, ` talags`, ` pakig` (target ranks: fact_1=6:31630, fact_2=92:8574, fact_3=21:29316, prefix_sum_12=98:14797, sum=119:507)
- Layer 39: `<｜begin▁of▁sentence｜>`, `ophe`, ` Rutherford`, ` Dominic`, `lier` (target ranks: fact_1=6:114388, fact_2=92:106365, fact_3=21:95711, prefix_sum_12=98:74654, sum=119:15199)
- Layer 40: `ophe`, `<｜begin▁of▁sentence｜>`, ` Rutherford`, `atomic`, ` talags` (target ranks: fact_1=6:86032, fact_2=92:97318, fact_3=21:78256, prefix_sum_12=98:55495, sum=119:13586)
- Layer 41: ` .`, `人人都`, `less`, `atomic`, ` atomic` (target ranks: fact_1=6:53100, fact_2=92:99566, fact_3=21:70832, prefix_sum_12=98:63065, sum=119:58256)

### Filler position 7 (absolute token 522, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:126988, fact_2=92:122609, fact_3=21:125000, prefix_sum_12=98:123074, sum=119:120096)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:4247, fact_2=92:12958, fact_3=21:9656, prefix_sum_12=98:12266, sum=119:23361)
- Layer 20: `锁定`, `ait`, `足`, `us`, `cape` (target ranks: fact_1=6:658, fact_2=92:4655, fact_3=21:2390, prefix_sum_12=98:3982, sum=119:18001)
- Layer 30: `保留`, ` pakig`, `acos`, ` IR`, ` الذ` (target ranks: fact_1=6:17890, fact_2=92:330, fact_3=21:18377, prefix_sum_12=98:964, sum=119:12226)
- Layer 35: `86`, `92`, `88`, `84`, `93` (target ranks: fact_1=6:4563, fact_2=92:2, fact_3=21:10898, prefix_sum_12=98:42, sum=119:3003)
- Layer 36: `88`, `93`, `86`, `306`, `96` (target ranks: fact_1=6:45537, fact_2=92:6, fact_3=21:77387, prefix_sum_12=98:51, sum=119:714)
- Layer 37: `92`, `}<?`, `93`, `86`, `96` (target ranks: fact_1=6:68607, fact_2=92:1, fact_3=21:84631, prefix_sum_12=98:30, sum=119:792)
- Layer 38: `}<?`, `305`, `306`, `105`, `107` (target ranks: fact_1=6:94558, fact_2=92:37, fact_3=21:105252, prefix_sum_12=98:35, sum=119:184)
- Layer 39: `}<?`, `lisitry`, `本题分析`, `图画`, ` embar` (target ranks: fact_1=6:30192, fact_2=92:42928, fact_3=21:21366, prefix_sum_12=98:13602, sum=119:8997)
- Layer 40: `lisitry`, `}<?`, `风气`, ` atomic`, `行礼` (target ranks: fact_1=6:906, fact_2=92:14344, fact_3=21:1244, prefix_sum_12=98:7228, sum=119:2108)
- Layer 41: ` atomic`, `癫�`, `出不穷`, `图中的`, `笔趣` (target ranks: fact_1=6:1030, fact_2=92:47235, fact_3=21:3301, prefix_sum_12=98:24702, sum=119:19929)

### Filler position 8 (absolute token 523, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:126801, fact_2=92:122377, fact_3=21:124777, prefix_sum_12=98:122803, sum=119:119707)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=6:2844, fact_2=92:10575, fact_3=21:7367, prefix_sum_12=98:10239, sum=119:20230)
- Layer 20: `锁定`, ` smile`, `足`, `Ta`, `ait` (target ranks: fact_1=6:1019, fact_2=92:9353, fact_3=21:3546, prefix_sum_12=98:8150, sum=119:26410)
- Layer 30: ` calculator`, `加起来`, `sum`, ` summing`, ` suma` (target ranks: fact_1=6:7586, fact_2=92:58172, fact_3=21:19973, prefix_sum_12=98:33383, sum=119:68088)
- Layer 35: `sum`, ` calculator`, ` suma`, ` Sum`, ` equation` (target ranks: fact_1=6:682, fact_2=92:18127, fact_3=21:2052, prefix_sum_12=98:3641, sum=119:20787)
- Layer 36: ` Sum`, `sum`, ` sum`, `Sum`, ` sums` (target ranks: fact_1=6:2702, fact_2=92:43204, fact_3=21:7570, prefix_sum_12=98:4781, sum=119:22154)
- Layer 37: ` Sum`, ` sum`, ` sums`, `Sum`, `sum` (target ranks: fact_1=6:18584, fact_2=92:84958, fact_3=21:18521, prefix_sum_12=98:15423, sum=119:36410)
- Layer 38: ` Sum`, ` sum`, ` sums`, `Sum`, `sum` (target ranks: fact_1=6:22222, fact_2=92:82631, fact_3=21:22543, prefix_sum_12=98:19268, sum=119:46068)
- Layer 39: `}<?`, ` Sum`, ` sum`, `累`, `osum` (target ranks: fact_1=6:80875, fact_2=92:110644, fact_3=21:75346, prefix_sum_12=98:59085, sum=119:85008)
- Layer 40: `atomic`, ` Rutherford`, ` Atomic`, ` atomic`, `留存` (target ranks: fact_1=6:13685, fact_2=92:108716, fact_3=21:26760, prefix_sum_12=98:34558, sum=119:53167)
- Layer 41: ` .`, `鹉`, ` atomic`, `atomic`, `<｜end▁of▁sentence｜>` (target ranks: fact_1=6:6073, fact_2=92:93777, fact_3=21:38472, prefix_sum_12=98:26288, sum=119:54822)

### Filler position 9 (absolute token 524, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:126620, fact_2=92:122229, fact_3=21:124611, prefix_sum_12=98:122652, sum=119:119507)
- Layer 10: ` Walker`, `锁定`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=6:3007, fact_2=92:11052, fact_3=21:7710, prefix_sum_12=98:10494, sum=119:20463)
- Layer 20: `锁定`, `挪`, ` Agri`, `ait`, `能被` (target ranks: fact_1=6:453, fact_2=92:3800, fact_3=21:1740, prefix_sum_12=98:3449, sum=119:11652)
- Layer 30: `加起来`, ` encomp`, `总和`, `相加`, ` ---|---|---|---|---|---|---` (target ranks: fact_1=6:50792, fact_2=92:1437, fact_3=21:48318, prefix_sum_12=98:2323, sum=119:10897)
- Layer 35: `92`, `93`, `88`, `86`, `90` (target ranks: fact_1=6:11425, fact_2=92:1, fact_3=21:29446, prefix_sum_12=98:20, sum=119:366)
- Layer 36: `92`, `93`, `88`, ` Ninety`, `九十` (target ranks: fact_1=6:65780, fact_2=92:1, fact_3=21:114238, prefix_sum_12=98:19, sum=119:50)
- Layer 37: `92`, `93`, ` ninety`, `九十`, ` Ninety` (target ranks: fact_1=6:84528, fact_2=92:1, fact_3=21:115341, prefix_sum_12=98:18, sum=119:77)
- Layer 38: `}<?`, `105`, `92`, `106`, `103` (target ranks: fact_1=6:90218, fact_2=92:3, fact_3=21:120323, prefix_sum_12=98:26, sum=119:10)
- Layer 39: `}<?`, `本题分析`, `119`, `105`, `116` (target ranks: fact_1=6:38871, fact_2=92:11220, fact_3=21:39418, prefix_sum_12=98:19467, sum=119:3)
- Layer 40: `<｜begin▁of▁file｜>`, `lisitry`, `}<?`, ` atomic`, `106` (target ranks: fact_1=6:4250, fact_2=92:3872, fact_3=21:17813, prefix_sum_12=98:13568, sum=119:6)
- Layer 41: `癫�`, `<｜begin▁of▁file｜>`, `��`, `出不穷`, `因为这些` (target ranks: fact_1=6:1451, fact_2=92:18772, fact_3=21:10988, prefix_sum_12=98:19705, sum=119:782)

### Filler position 10 (absolute token 525, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:126740, fact_2=92:122447, fact_3=21:124715, prefix_sum_12=98:122793, sum=119:119569)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2920, fact_2=92:11258, fact_3=21:7693, prefix_sum_12=98:10533, sum=119:21203)
- Layer 20: `足`, `胃癌`, `幽`, `能被`, `cape` (target ranks: fact_1=6:574, fact_2=92:5292, fact_3=21:2068, prefix_sum_12=98:3136, sum=119:25997)
- Layer 30: ` atomic`, `atomic`, ` Atomic`, `Atomic`, ` Carbon` (target ranks: fact_1=6:5325, fact_2=92:37843, fact_3=21:8770, prefix_sum_12=98:15928, sum=119:46590)
- Layer 35: `碳`, ` Carbon`, ` carbon`, `Carbon`, `carbon` (target ranks: fact_1=6:168, fact_2=92:14406, fact_3=21:3364, prefix_sum_12=98:3492, sum=119:46006)
- Layer 36: `碳`, ` carbon`, ` Carbon`, `Carbon`, `carbon` (target ranks: fact_1=6:177, fact_2=92:31650, fact_3=21:12123, prefix_sum_12=98:7364, sum=119:52406)
- Layer 37: ` Carbon`, `Carbon`, ` carbon`, `carbon`, `碳` (target ranks: fact_1=6:310, fact_2=92:95898, fact_3=21:54402, prefix_sum_12=98:47354, sum=119:86099)
- Layer 38: ` Carbon`, `carbon`, `Carbon`, ` carbon`, `碳` (target ranks: fact_1=6:405, fact_2=92:110583, fact_3=21:73160, prefix_sum_12=98:74863, sum=119:94141)
- Layer 39: ` C`, ` Carbon`, `Carbon`, `carbon`, ` atomic` (target ranks: fact_1=6:7182, fact_2=92:114302, fact_3=21:89843, prefix_sum_12=98:86339, sum=119:88538)
- Layer 40: ` C`, `atomic`, ` atomic`, `C`, ` Atomic` (target ranks: fact_1=6:162, fact_2=92:88957, fact_3=21:30054, prefix_sum_12=98:36507, sum=119:52791)
- Layer 41: ` atomic`, `atomic`, ` .`, ` Atomic`, `原子` (target ranks: fact_1=6:34, fact_2=92:55231, fact_3=21:6733, prefix_sum_12=98:18461, sum=119:41809)

### Filler position 11 (absolute token 526, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: fact_1=6:126696, fact_2=92:122568, fact_3=21:124711, prefix_sum_12=98:122867, sum=119:119768)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2665, fact_2=92:11203, fact_3=21:7077, prefix_sum_12=98:10112, sum=119:20829)
- Layer 20: `ait`, `锁定`, `挪`, ` LS`, `幽` (target ranks: fact_1=6:535, fact_2=92:4007, fact_3=21:2047, prefix_sum_12=98:3378, sum=119:13906)
- Layer 30: `acos`, ` الجرم`, `保留`, ` pakig`, ` ---|---|---|---|---|---|---` (target ranks: fact_1=6:10991, fact_2=92:350, fact_3=21:8009, prefix_sum_12=98:388, sum=119:11344)
- Layer 35: `76`, `锁定`, `保留`, `acos`, `86` (target ranks: fact_1=6:5424, fact_2=92:27, fact_3=21:4305, prefix_sum_12=98:324, sum=119:5310)
- Layer 36: `}<?`, `acos`, ` scor`, `关`, `apan` (target ranks: fact_1=6:46842, fact_2=92:83, fact_3=21:63623, prefix_sum_12=98:649, sum=119:850)
- Layer 37: `}<?`, `Quintal`, ` المطلع`, `关`, ` الجرم` (target ranks: fact_1=6:96574, fact_2=92:40, fact_3=21:93688, prefix_sum_12=98:2109, sum=119:560)
- Layer 38: `}<?`, `ucl`, `-ulo`, `本题分析`, `acos` (target ranks: fact_1=6:96009, fact_2=92:1887, fact_3=21:117020, prefix_sum_12=98:4237, sum=119:361)
- Layer 39: `}<?`, `东海`, `-ulo`, `慕`, `叶子` (target ranks: fact_1=6:37331, fact_2=92:94563, fact_3=21:68317, prefix_sum_12=98:46633, sum=119:449)
- Layer 40: `水土`, `留存`, `行礼`, `apon`, ` atomic` (target ranks: fact_1=6:1073, fact_2=92:57821, fact_3=21:14201, prefix_sum_12=98:12947, sum=119:90)
- Layer 41: ` .`, ` atomic`, `太多了`, `癫�`, `装甲` (target ranks: fact_1=6:196, fact_2=92:45081, fact_3=21:13737, prefix_sum_12=98:11307, sum=119:2226)

### Filler position 12 (absolute token 527, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=6:126569, fact_2=92:122557, fact_3=21:124557, prefix_sum_12=98:122767, sum=119:119671)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2222, fact_2=92:10114, fact_3=21:6484, prefix_sum_12=98:9248, sum=119:19872)
- Layer 20: `锁定`, ` wig`, ` smile`, `ait`, `挪` (target ranks: fact_1=6:1627, fact_2=92:10381, fact_3=21:6546, prefix_sum_12=98:9558, sum=119:27495)
- Layer 30: `重复`, ` repetition`, ` repetitions`, `随机`, ` repeated` (target ranks: fact_1=6:2104, fact_2=92:51794, fact_3=21:22266, prefix_sum_12=98:23281, sum=119:68478)
- Layer 35: `重复`, ` repetitions`, ` repetition`, `询问`, ` tap` (target ranks: fact_1=6:1366, fact_2=92:44595, fact_3=21:9351, prefix_sum_12=98:9856, sum=119:41950)
- Layer 36: ` repeated`, `重复`, `询问`, `反复`, ` tap` (target ranks: fact_1=6:2027, fact_2=92:41077, fact_3=21:12502, prefix_sum_12=98:4691, sum=119:26863)
- Layer 37: `}<?`, ` random`, `随机`, `提问`, ` repeated` (target ranks: fact_1=6:27325, fact_2=92:106777, fact_3=21:55430, prefix_sum_12=98:39054, sum=119:53390)
- Layer 38: `}<?`, ` random`, `随机`, `变异`, `random` (target ranks: fact_1=6:50946, fact_2=92:116997, fact_3=21:80668, prefix_sum_12=98:67059, sum=119:69526)
- Layer 39: `}<?`, `<｜begin▁of▁sentence｜>`, `�乐`, `acons`, `ocyst` (target ranks: fact_1=6:113782, fact_2=92:121782, fact_3=21:113252, prefix_sum_12=98:89425, sum=119:87511)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` .`, `冰冰`, `šk`, ` capsule` (target ranks: fact_1=6:71693, fact_2=92:107963, fact_3=21:82361, prefix_sum_12=98:60026, sum=119:64971)
- Layer 41: ` .`, `鹉`, `矶`, `猕猴`, ` repeated` (target ranks: fact_1=6:14633, fact_2=92:84431, fact_3=21:71585, prefix_sum_12=98:27968, sum=119:37510)

### Filler position 13 (absolute token 528, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=6:126697, fact_2=92:122851, fact_3=21:124718, prefix_sum_12=98:122988, sum=119:119860)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3340, fact_2=92:12511, fact_3=21:8142, prefix_sum_12=98:11199, sum=119:22114)
- Layer 20: ` LS`, `挪`, `锁定`, `LS`, `胃癌` (target ranks: fact_1=6:651, fact_2=92:6312, fact_3=21:2163, prefix_sum_12=98:5112, sum=119:18472)
- Layer 30: `acin`, ` Reich`, `acos`, `尾`, `三十六` (target ranks: fact_1=6:10228, fact_2=92:11799, fact_3=21:3475, prefix_sum_12=98:5242, sum=119:43761)
- Layer 35: `92`, ` uranium`, ` Uran`, `uran`, `铀` (target ranks: fact_1=6:8729, fact_2=92:1, fact_3=21:19278, prefix_sum_12=98:52, sum=119:18034)
- Layer 36: `92`, ` ninety`, `922`, `93`, ` uranium` (target ranks: fact_1=6:84799, fact_2=92:1, fact_3=21:87703, prefix_sum_12=98:46, sum=119:34490)
- Layer 37: `92`, ` ninety`, `922`, ` Ninety`, `九十` (target ranks: fact_1=6:124007, fact_2=92:1, fact_3=21:117849, prefix_sum_12=98:209, sum=119:44506)
- Layer 38: `92`, ` ninety`, ` Uran`, `}<?`, ` uranium` (target ranks: fact_1=6:120403, fact_2=92:1, fact_3=21:124975, prefix_sum_12=98:1041, sum=119:25479)
- Layer 39: ` Uran`, `}<?`, `atomic`, ` uranium`, `pac` (target ranks: fact_1=6:101108, fact_2=92:6, fact_3=21:102020, prefix_sum_12=98:49585, sum=119:22819)
- Layer 40: `atomic`, ` atomic`, ` Atomic`, ` molar`, `Atomic` (target ranks: fact_1=6:30991, fact_2=92:28404, fact_3=21:37993, prefix_sum_12=98:34051, sum=119:8432)
- Layer 41: `atomic`, ` atomic`, ` .`, `鹉`, ` Atomic` (target ranks: fact_1=6:4734, fact_2=92:58345, fact_3=21:48824, prefix_sum_12=98:36790, sum=119:32283)

### Filler position 14 (absolute token 529, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: fact_1=6:126816, fact_2=92:123201, fact_3=21:124888, prefix_sum_12=98:123297, sum=119:120103)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2869, fact_2=92:11175, fact_3=21:7269, prefix_sum_12=98:10138, sum=119:20585)
- Layer 20: `锁定`, `挪`, `ait`, ` Walker`, `Walker` (target ranks: fact_1=6:702, fact_2=92:6568, fact_3=21:2609, prefix_sum_12=98:5588, sum=119:20390)
- Layer 30: ` Heim`, `柿子`, ` thoracic`, `acos`, `sce` (target ranks: fact_1=6:19710, fact_2=92:36943, fact_3=21:367, prefix_sum_12=98:11374, sum=119:48292)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, `twenty` (target ranks: fact_1=6:48469, fact_2=92:68402, fact_3=21:1, prefix_sum_12=98:43077, sum=119:62461)
- Layer 36: `二十一`, `21`, ` XXI`, `}<?`, ` twenty` (target ranks: fact_1=6:105897, fact_2=92:108768, fact_3=21:2, prefix_sum_12=98:103041, sum=119:93833)
- Layer 37: `二十一`, `21`, ` XXI`, ` twenty`, `二十` (target ranks: fact_1=6:117017, fact_2=92:23742, fact_3=21:2, prefix_sum_12=98:60299, sum=119:58429)
- Layer 38: `二十一`, `21`, ` XXI`, `rá`, `听课` (target ranks: fact_1=6:116926, fact_2=92:11684, fact_3=21:2, prefix_sum_12=98:82823, sum=119:67202)
- Layer 39: `-ulo`, `二十一`, `ucl`, `累`, `tanle` (target ranks: fact_1=6:21065, fact_2=92:69914, fact_3=21:16, prefix_sum_12=98:104197, sum=119:22929)
- Layer 40: ` atomic`, `atomic`, `二十一`, ` outp`, ` Atomic` (target ranks: fact_1=6:178, fact_2=92:55104, fact_3=21:9, prefix_sum_12=98:71937, sum=119:4726)
- Layer 41: ` atomic`, `二十一`, `鹉`, ` uncovered`, `atomic` (target ranks: fact_1=6:271, fact_2=92:62915, fact_3=21:264, prefix_sum_12=98:32800, sum=119:25882)

### Filler position 15 (absolute token 530, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126975, fact_2=92:123645, fact_3=21:125082, prefix_sum_12=98:123654, sum=119:120497)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3022, fact_2=92:11471, fact_3=21:7456, prefix_sum_12=98:10582, sum=119:21246)
- Layer 20: `Ta`, `ait`, ` LS`, `cape`, `LS` (target ranks: fact_1=6:390, fact_2=92:4571, fact_3=21:1615, prefix_sum_12=98:4446, sum=119:16633)
- Layer 30: `acos`, `�`, `总体`, ` consuming`, ` ternary` (target ranks: fact_1=6:23383, fact_2=92:8136, fact_3=21:2957, prefix_sum_12=98:6195, sum=119:38437)
- Layer 35: `acos`, ` met`, `61`, ` Heim`, `认` (target ranks: fact_1=6:3379, fact_2=92:4405, fact_3=21:254, prefix_sum_12=98:10303, sum=119:53545)
- Layer 36: `三十六`, `otas`, `36`, ` consuming`, `acos` (target ranks: fact_1=6:10334, fact_2=92:12507, fact_3=21:8061, prefix_sum_12=98:18451, sum=119:44061)
- Layer 37: `}<?`, `图画`, `斋`, `师徒`, `}using` (target ranks: fact_1=6:53916, fact_2=92:4396, fact_3=21:4911, prefix_sum_12=98:25167, sum=119:22105)
- Layer 38: `斋`, `}<?`, ` transcend`, `党群`, `图画` (target ranks: fact_1=6:27324, fact_2=92:3522, fact_3=21:53426, prefix_sum_12=98:17100, sum=119:18107)
- Layer 39: `tanle`, `107`, `ucl`, ` transcend`, `106` (target ranks: fact_1=6:262, fact_2=92:105832, fact_3=21:7425, prefix_sum_12=98:67478, sum=119:2408)
- Layer 40: ` atomic`, `atomic`, ` Atomic`, `atri`, `原子` (target ranks: fact_1=6:17, fact_2=92:71699, fact_3=21:2265, prefix_sum_12=98:28604, sum=119:1084)
- Layer 41: ` atomic`, `atomic`, ` .`, `原子`, ` Atomic` (target ranks: fact_1=6:20, fact_2=92:38478, fact_3=21:2590, prefix_sum_12=98:10598, sum=119:2497)

### Filler position 16 (absolute token 531, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126823, fact_2=92:123500, fact_3=21:124914, prefix_sum_12=98:123423, sum=119:120219)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2975, fact_2=92:12056, fact_3=21:7527, prefix_sum_12=98:10769, sum=119:21576)
- Layer 20: `锁定`, `ait`, ` LS`, `能被`, `Ta` (target ranks: fact_1=6:163, fact_2=92:2208, fact_3=21:1169, prefix_sum_12=98:2229, sum=119:10389)
- Layer 30: `acos`, ` pakig`, `ASCAR`, `ascar`, `俯` (target ranks: fact_1=6:19469, fact_2=92:9988, fact_3=21:6279, prefix_sum_12=98:13674, sum=119:27915)
- Layer 35: `acos`, ` met`, `53`, `61`, `62` (target ranks: fact_1=6:6060, fact_2=92:9154, fact_3=21:77, prefix_sum_12=98:20106, sum=119:33541)
- Layer 36: `}<?`, `43`, `68`, `?datasetId`, `54` (target ranks: fact_1=6:39412, fact_2=92:23950, fact_3=21:5350, prefix_sum_12=98:33013, sum=119:15969)
- Layer 37: `}<?`, `?datasetId`, `图画`, `ucl`, `odea` (target ranks: fact_1=6:60544, fact_2=92:1026, fact_3=21:3023, prefix_sum_12=98:9864, sum=119:1985)
- Layer 38: `}<?`, `斋`, `图画`, ` transcend`, `劳` (target ranks: fact_1=6:59610, fact_2=92:506, fact_3=21:50001, prefix_sum_12=98:2772, sum=119:4065)
- Layer 39: `107`, `109`, `108`, `105`, `113` (target ranks: fact_1=6:22365, fact_2=92:34690, fact_3=21:39684, prefix_sum_12=98:4033, sum=119:51)
- Layer 40: `107`, `103`, `109`, `106`, `105` (target ranks: fact_1=6:294, fact_2=92:4291, fact_3=21:10172, prefix_sum_12=98:334, sum=119:20)
- Layer 41: ` atomic`, `原子`, `atomic`, ` uncovered`, ` Atomic` (target ranks: fact_1=6:135, fact_2=92:15485, fact_3=21:12869, prefix_sum_12=98:1324, sum=119:844)

### Filler position 17 (absolute token 532, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126885, fact_2=92:123580, fact_3=21:124990, prefix_sum_12=98:123453, sum=119:120236)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3875, fact_2=92:13936, fact_3=21:8912, prefix_sum_12=98:12349, sum=119:23028)
- Layer 20: `锁定`, `胃癌`, ` smile`, `挪`, `幽` (target ranks: fact_1=6:1392, fact_2=92:12346, fact_3=21:4980, prefix_sum_12=98:8639, sum=119:23585)
- Layer 30: ` Ne`, ` prot`, ` neon`, ` gold`, `Ne` (target ranks: fact_1=6:14859, fact_2=92:28870, fact_3=21:20587, prefix_sum_12=98:12007, sum=119:51710)
- Layer 35: ` Ne`, `Ne`, ` Neon`, ` neon`, ` prot` (target ranks: fact_1=6:5226, fact_2=92:23559, fact_3=21:9369, prefix_sum_12=98:9282, sum=119:51813)
- Layer 36: ` Ne`, ` Neon`, ` neon`, ` prot`, `Ne` (target ranks: fact_1=6:10546, fact_2=92:28713, fact_3=21:21171, prefix_sum_12=98:8005, sum=119:33389)
- Layer 37: ` prot`, ` gold`, ` Prot`, ` Ne`, `gold` (target ranks: fact_1=6:55298, fact_2=92:81019, fact_3=21:68367, prefix_sum_12=98:31346, sum=119:56494)
- Layer 38: `�`, `gold`, ` Thor`, ` gold`, ` prot` (target ranks: fact_1=6:70037, fact_2=92:90641, fact_3=21:85137, prefix_sum_12=98:44303, sum=119:48450)
- Layer 39: ` Ne`, `�`, ` Gold`, ` gold`, `gold` (target ranks: fact_1=6:96583, fact_2=92:100839, fact_3=21:99270, prefix_sum_12=98:68833, sum=119:95094)
- Layer 40: `�`, ` Neon`, ` Rutherford`, ` Ne`, `坏` (target ranks: fact_1=6:28981, fact_2=92:78992, fact_3=21:37502, prefix_sum_12=98:28487, sum=119:55741)
- Layer 41: ` .`, ` atomic`, ` .↵↵`, ` fused`, ` because` (target ranks: fact_1=6:2744, fact_2=92:42505, fact_3=21:30655, prefix_sum_12=98:6513, sum=119:34679)

### Filler position 18 (absolute token 533, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126941, fact_2=92:123779, fact_3=21:125140, prefix_sum_12=98:123671, sum=119:120642)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3127, fact_2=92:12162, fact_3=21:7806, prefix_sum_12=98:10870, sum=119:22072)
- Layer 20: ` Walker`, `锁定`, `ait`, ` smile`, `Walker` (target ranks: fact_1=6:2612, fact_2=92:12100, fact_3=21:5569, prefix_sum_12=98:7313, sum=119:26921)
- Layer 30: `�`, `Tap`, `拆`, ` tap`, `幽` (target ranks: fact_1=6:2886, fact_2=92:19952, fact_3=21:5561, prefix_sum_12=98:4051, sum=119:35231)
- Layer 35: `Tap`, `aty`, `羊`, ` tap`, `拆` (target ranks: fact_1=6:1224, fact_2=92:8276, fact_3=21:1638, prefix_sum_12=98:992, sum=119:18470)
- Layer 36: `留存`, `acin`, `羊`, ` tap`, `洋` (target ranks: fact_1=6:2611, fact_2=92:16882, fact_3=21:4773, prefix_sum_12=98:1860, sum=119:19349)
- Layer 37: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `原子` (target ranks: fact_1=6:27423, fact_2=92:64621, fact_3=21:18248, prefix_sum_12=98:11958, sum=119:37994)
- Layer 38: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `zat` (target ranks: fact_1=6:37493, fact_2=92:67921, fact_3=21:15990, prefix_sum_12=98:18095, sum=119:47510)
- Layer 39: ` atomic`, `atomic`, ` Atomic`, `<｜begin▁of▁sentence｜>`, `打磨` (target ranks: fact_1=6:25693, fact_2=92:66305, fact_3=21:19507, prefix_sum_12=98:26036, sum=119:49540)
- Layer 40: `atomic`, ` atomic`, `eland`, `zij`, `留存` (target ranks: fact_1=6:1538, fact_2=92:32982, fact_3=21:3385, prefix_sum_12=98:7658, sum=119:25740)
- Layer 41: `atomic`, ` atomic`, ` `, ` .`, `袄` (target ranks: fact_1=6:23, fact_2=92:15662, fact_3=21:3739, prefix_sum_12=98:1713, sum=119:12623)

### Filler position 19 (absolute token 534, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:127001, fact_2=92:124129, fact_3=21:125225, prefix_sum_12=98:123922, sum=119:121026)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3038, fact_2=92:11927, fact_3=21:7607, prefix_sum_12=98:10551, sum=119:21315)
- Layer 20: `ait`, `锁定`, ` Walker`, `足`, ` engaging` (target ranks: fact_1=6:3623, fact_2=92:14723, fact_3=21:5317, prefix_sum_12=98:9935, sum=119:31361)
- Layer 30: ` remembering`, `熟悉`, ` remembered`, `�`, `atri` (target ranks: fact_1=6:8666, fact_2=92:28962, fact_3=21:8645, prefix_sum_12=98:9396, sum=119:36327)
- Layer 35: `足`, `熟悉`, `Tap`, `分解`, ` repetition` (target ranks: fact_1=6:5152, fact_2=92:18949, fact_3=21:2838, prefix_sum_12=98:5632, sum=119:24027)
- Layer 36: `留存`, `熟悉`, ` familiar`, `acin`, `分解` (target ranks: fact_1=6:9771, fact_2=92:25688, fact_3=21:6609, prefix_sum_12=98:6047, sum=119:20826)
- Layer 37: ` atomic`, `atomic`, ` Atomic`, `留存`, `查阅` (target ranks: fact_1=6:60920, fact_2=92:72387, fact_3=21:25444, prefix_sum_12=98:28450, sum=119:36554)
- Layer 38: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `查找` (target ranks: fact_1=6:85859, fact_2=92:83470, fact_3=21:40043, prefix_sum_12=98:52984, sum=119:42591)
- Layer 39: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `acons` (target ranks: fact_1=6:95790, fact_2=92:96764, fact_3=21:66553, prefix_sum_12=98:58196, sum=119:50790)
- Layer 40: `atomic`, ` atomic`, ` Atomic`, `留存`, `Atomic` (target ranks: fact_1=6:31004, fact_2=92:66998, fact_3=21:22956, prefix_sum_12=98:27530, sum=119:20326)
- Layer 41: ` atomic`, `atomic`, ` Atomic`, `原子`, ` .` (target ranks: fact_1=6:1219, fact_2=92:39849, fact_3=21:16466, prefix_sum_12=98:12065, sum=119:19164)

### Filler position 20 (absolute token 535, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:127101, fact_2=92:124462, fact_3=21:125382, prefix_sum_12=98:124196, sum=119:121255)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2996, fact_2=92:11502, fact_3=21:7541, prefix_sum_12=98:10364, sum=119:20076)
- Layer 20: `ait`, `锁定`, ` Walker`, ` engaging`, `Walker` (target ranks: fact_1=6:3927, fact_2=92:14456, fact_3=21:5691, prefix_sum_12=98:9943, sum=119:38850)
- Layer 30: ` Carbon`, `碳`, ` carbon`, `Carbon`, `carbon` (target ranks: fact_1=6:12249, fact_2=92:43917, fact_3=21:11742, prefix_sum_12=98:14366, sum=119:67852)
- Layer 35: ` Carbon`, `碳`, `Carbon`, ` carbon`, `carbon` (target ranks: fact_1=6:155, fact_2=92:21087, fact_3=21:10906, prefix_sum_12=98:6071, sum=119:61679)
- Layer 36: ` Carbon`, `碳`, ` carbon`, `Carbon`, `carbon` (target ranks: fact_1=6:104, fact_2=92:31924, fact_3=21:40759, prefix_sum_12=98:9213, sum=119:63906)
- Layer 37: ` Carbon`, `Carbon`, `carbon`, ` carbon`, `碳` (target ranks: fact_1=6:62, fact_2=92:85236, fact_3=21:89444, prefix_sum_12=98:46656, sum=119:103009)
- Layer 38: ` Carbon`, `carbon`, `Carbon`, ` carbon`, `碳` (target ranks: fact_1=6:241, fact_2=92:106225, fact_3=21:107229, prefix_sum_12=98:78153, sum=119:112349)
- Layer 39: ` Carbon`, `carbon`, `Carbon`, ` carbon`, `-carbon` (target ranks: fact_1=6:6119, fact_2=92:113294, fact_3=21:99684, prefix_sum_12=98:92048, sum=119:100649)
- Layer 40: ` atomic`, `atomic`, ` Atomic`, ` Carbon`, `ses` (target ranks: fact_1=6:752, fact_2=92:84973, fact_3=21:54009, prefix_sum_12=98:45909, sum=119:78239)
- Layer 41: ` atomic`, `atomic`, `原子`, ` Atomic`, ` Uran` (target ranks: fact_1=6:27, fact_2=92:25775, fact_3=21:10054, prefix_sum_12=98:10459, sum=119:49325)

### Filler position 21 (absolute token 536, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126920, fact_2=92:124367, fact_3=21:125207, prefix_sum_12=98:124095, sum=119:121141)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2915, fact_2=92:11418, fact_3=21:7364, prefix_sum_12=98:10417, sum=119:20101)
- Layer 20: `锁定`, `ait`, ` Walker`, `能被`, ` engaging` (target ranks: fact_1=6:5605, fact_2=92:25137, fact_3=21:10391, prefix_sum_12=98:21609, sum=119:41491)
- Layer 30: `acos`, `平行`, `俯`, `保留`, ` reserved` (target ranks: fact_1=6:45030, fact_2=92:85791, fact_3=21:19954, prefix_sum_12=98:58050, sum=119:90690)
- Layer 35: `�`, ` cadmium`, `esium`, ` mercury`, `anium` (target ranks: fact_1=6:16240, fact_2=92:73348, fact_3=21:5518, prefix_sum_12=98:30290, sum=119:67410)
- Layer 36: `�`, `anium`, ` mercury`, ` Rh`, ` cadmium` (target ranks: fact_1=6:27626, fact_2=92:39987, fact_3=21:12309, prefix_sum_12=98:11439, sum=119:40352)
- Layer 37: `�`, `�`, `anium`, ` Bism`, `�` (target ranks: fact_1=6:81863, fact_2=92:72975, fact_3=21:42605, prefix_sum_12=98:20874, sum=119:42752)
- Layer 38: `�`, ` Bism`, `�`, `anium`, ` Rutherford` (target ranks: fact_1=6:83184, fact_2=92:72144, fact_3=21:43174, prefix_sum_12=98:22296, sum=119:42650)
- Layer 39: `�`, `�`, ` Rutherford`, ` Mercury`, `�` (target ranks: fact_1=6:57221, fact_2=92:80187, fact_3=21:25627, prefix_sum_12=98:47715, sum=119:49751)
- Layer 40: `�`, ` Rutherford`, `�`, `anium`, ` ` (target ranks: fact_1=6:6838, fact_2=92:49666, fact_3=21:4852, prefix_sum_12=98:26994, sum=119:12250)
- Layer 41: ` `, ` .`, ` zircon`, `冰冰`, `<｜end▁of▁sentence｜>` (target ranks: fact_1=6:88, fact_2=92:21934, fact_3=21:2982, prefix_sum_12=98:4449, sum=119:12152)

### Filler position 22 (absolute token 537, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:126939, fact_2=92:124361, fact_3=21:125221, prefix_sum_12=98:124098, sum=119:121065)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2440, fact_2=92:10689, fact_3=21:6686, prefix_sum_12=98:9766, sum=119:19359)
- Layer 20: `ait`, `锁定`, ` smile`, ` Walker`, ` LS` (target ranks: fact_1=6:1208, fact_2=92:9331, fact_3=21:4558, prefix_sum_12=98:10175, sum=119:24379)
- Layer 30: `Tap`, ` tap`, `tap`, ` Tap`, `scan` (target ranks: fact_1=6:1368, fact_2=92:11390, fact_3=21:2990, prefix_sum_12=98:11939, sum=119:21550)
- Layer 35: ` tap`, `锁定`, `Tap`, ` Tap`, `羊` (target ranks: fact_1=6:737, fact_2=92:14176, fact_3=21:1210, prefix_sum_12=98:6432, sum=119:16429)
- Layer 36: `acin`, ` tap`, `俯`, `adal`, `羊` (target ranks: fact_1=6:933, fact_2=92:18342, fact_3=21:3190, prefix_sum_12=98:8028, sum=119:12081)
- Layer 37: `俯`, `acin`, ` tap`, `acos`, `tap` (target ranks: fact_1=6:6220, fact_2=92:50805, fact_3=21:9591, prefix_sum_12=98:23036, sum=119:13861)
- Layer 38: `acin`, `坏`, `俯`, `}<?`, `acos` (target ranks: fact_1=6:7596, fact_2=92:65427, fact_3=21:30278, prefix_sum_12=98:33608, sum=119:17562)
- Layer 39: `<｜begin▁of▁sentence｜>`, `osit`, `}<?`, `�`, `�` (target ranks: fact_1=6:43161, fact_2=92:96349, fact_3=21:26724, prefix_sum_12=98:75897, sum=119:57531)
- Layer 40: `osit`, `俯`, `<｜begin▁of▁sentence｜>`, `装`, ` ` (target ranks: fact_1=6:5465, fact_2=92:37768, fact_3=21:3591, prefix_sum_12=98:33575, sum=119:33209)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, `.,`, `装` (target ranks: fact_1=6:145, fact_2=92:18589, fact_3=21:2624, prefix_sum_12=98:9716, sum=119:21363)

### Filler position 23 (absolute token 538, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:127069, fact_2=92:124586, fact_3=21:125426, prefix_sum_12=98:124349, sum=119:121493)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=6:2872, fact_2=92:11935, fact_3=21:7297, prefix_sum_12=98:10701, sum=119:20882)
- Layer 20: ` Tears`, `足`, `cape`, ` smile`, `幽` (target ranks: fact_1=6:554, fact_2=92:8083, fact_3=21:2230, prefix_sum_12=98:7071, sum=119:24774)
- Layer 30: `�`, `幽`, ` tap`, `Tap`, `碳` (target ranks: fact_1=6:941, fact_2=92:36836, fact_3=21:4989, prefix_sum_12=98:18100, sum=119:34815)
- Layer 35: `碳`, ` Carbon`, `cape`, ` carbon`, `�` (target ranks: fact_1=6:975, fact_2=92:30720, fact_3=21:2935, prefix_sum_12=98:7639, sum=119:18985)
- Layer 36: `carbon`, `碳`, ` carbon`, ` Carbon`, `�` (target ranks: fact_1=6:2340, fact_2=92:52196, fact_3=21:8294, prefix_sum_12=98:9281, sum=119:16136)
- Layer 37: `carbon`, ` Carbon`, ` carbon`, `Carbon`, `碳` (target ranks: fact_1=6:27295, fact_2=92:100983, fact_3=21:29400, prefix_sum_12=98:35522, sum=119:28453)
- Layer 38: `}<?`, `carbon`, `�`, ` Carbon`, `zat` (target ranks: fact_1=6:37174, fact_2=92:97178, fact_3=21:42330, prefix_sum_12=98:38672, sum=119:37837)
- Layer 39: `}<?`, `�`, `romic`, `<｜begin▁of▁sentence｜>`, `打磨` (target ranks: fact_1=6:55224, fact_2=92:101535, fact_3=21:47273, prefix_sum_12=98:53491, sum=119:49859)
- Layer 40: `atomic`, ` atomic`, ` `, `�`, `坏` (target ranks: fact_1=6:3550, fact_2=92:47272, fact_3=21:8522, prefix_sum_12=98:15464, sum=119:19637)
- Layer 41: ` atomic`, `atomic`, ` .`, ` `, `<｜end▁of▁sentence｜>` (target ranks: fact_1=6:45, fact_2=92:27142, fact_3=21:3874, prefix_sum_12=98:6325, sum=119:17107)

### Filler position 24 (absolute token 539, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:127195, fact_2=92:124991, fact_3=21:125554, prefix_sum_12=98:124650, sum=119:121801)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=6:2516, fact_2=92:10884, fact_3=21:6898, prefix_sum_12=98:9580, sum=119:20163)
- Layer 20: ` smile`, ` LS`, `LS`, `胃癌`, ` wig` (target ranks: fact_1=6:951, fact_2=92:8616, fact_3=21:3890, prefix_sum_12=98:8866, sum=119:24123)
- Layer 30: ` ES`, ` Rh`, ` Mim`, ` Ob`, ` ED` (target ranks: fact_1=6:15888, fact_2=92:36526, fact_3=21:7223, prefix_sum_12=98:27387, sum=119:73403)
- Layer 35: `�`, ` tungsten`, ` cadmium`, `钨`, ` manganese` (target ranks: fact_1=6:7676, fact_2=92:28625, fact_3=21:1723, prefix_sum_12=98:11096, sum=119:62285)
- Layer 36: `�`, ` Rh`, `钨`, `Rh`, ` tungsten` (target ranks: fact_1=6:6133, fact_2=92:8610, fact_3=21:4822, prefix_sum_12=98:2873, sum=119:28021)
- Layer 37: `�`, `�`, `�`, ` cadmium`, ` titanium` (target ranks: fact_1=6:30208, fact_2=92:17680, fact_3=21:16276, prefix_sum_12=98:3487, sum=119:25892)
- Layer 38: `�`, `�`, `�`, `adium`, ` chromium` (target ranks: fact_1=6:45203, fact_2=92:26201, fact_3=21:29797, prefix_sum_12=98:5959, sum=119:31703)
- Layer 39: `�`, `�`, `�`, ` Titan`, `�` (target ranks: fact_1=6:42814, fact_2=92:50372, fact_3=21:16713, prefix_sum_12=98:31570, sum=119:58366)
- Layer 40: `�`, ` Ni`, ` Nitrogen`, ` Rutherford`, ` Ind` (target ranks: fact_1=6:4109, fact_2=92:45437, fact_3=21:5793, prefix_sum_12=98:25667, sum=119:15609)
- Layer 41: `�`, ` Zinc`, ` Uran`, ` arsenic`, ` uranium` (target ranks: fact_1=6:85, fact_2=92:16113, fact_3=21:1929, prefix_sum_12=98:2683, sum=119:19081)

### Filler position 25 (absolute token 540, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: fact_1=6:127290, fact_2=92:125144, fact_3=21:125632, prefix_sum_12=98:124741, sum=119:121812)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3193, fact_2=92:12679, fact_3=21:7934, prefix_sum_12=98:10825, sum=119:22245)
- Layer 20: ` smile`, `足`, `锁定`, ` Walker`, `ait` (target ranks: fact_1=6:1357, fact_2=92:9304, fact_3=21:2952, prefix_sum_12=98:6628, sum=119:19896)
- Layer 30: ` calculator`, `atomic`, `计算的`, ` atomic`, `calcul` (target ranks: fact_1=6:3541, fact_2=92:33779, fact_3=21:4125, prefix_sum_12=98:23179, sum=119:22918)
- Layer 35: ` calculator`, `分解`, ` atomic`, ` labor`, ` smile` (target ranks: fact_1=6:3123, fact_2=92:33753, fact_3=21:1308, prefix_sum_12=98:15346, sum=119:30037)
- Layer 36: `留存`, `羊`, ` smile`, ` organic`, `分解` (target ranks: fact_1=6:6060, fact_2=92:39609, fact_3=21:5144, prefix_sum_12=98:19148, sum=119:22087)
- Layer 37: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `原子` (target ranks: fact_1=6:13868, fact_2=92:57206, fact_3=21:9490, prefix_sum_12=98:38111, sum=119:28540)
- Layer 38: ` atomic`, ` Atomic`, `atomic`, `Atomic`, `}<?` (target ranks: fact_1=6:8239, fact_2=92:54805, fact_3=21:14214, prefix_sum_12=98:43390, sum=119:41424)
- Layer 39: ` atomic`, `atomic`, ` Atomic`, `Atomic`, `原子` (target ranks: fact_1=6:4684, fact_2=92:102932, fact_3=21:53075, prefix_sum_12=98:79964, sum=119:79150)
- Layer 40: `atomic`, ` atomic`, ` Atomic`, `eland`, `留存` (target ranks: fact_1=6:46, fact_2=92:58493, fact_3=21:21243, prefix_sum_12=98:33371, sum=119:44494)
- Layer 41: ` atomic`, `atomic`, ` Atomic`, ` `, ` .` (target ranks: fact_1=6:8, fact_2=92:54817, fact_3=21:19840, prefix_sum_12=98:16493, sum=119:54905)

### Filler position 26 (absolute token 541, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=6:127379, fact_2=92:125539, fact_3=21:125805, prefix_sum_12=98:125087, sum=119:122644)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2817, fact_2=92:11368, fact_3=21:7259, prefix_sum_12=98:9811, sum=119:20036)
- Layer 20: ` LS`, ` Walker`, `LS`, `ait`, `锁定` (target ranks: fact_1=6:1233, fact_2=92:7943, fact_3=21:3566, prefix_sum_12=98:4517, sum=119:18174)
- Layer 30: `obin`, `eder`, `acin`, `胶`, ` Dist` (target ranks: fact_1=6:3195, fact_2=92:3741, fact_3=21:2596, prefix_sum_12=98:2210, sum=119:27856)
- Layer 35: `92`, ` uranium`, `uran`, `88`, `86` (target ranks: fact_1=6:3458, fact_2=92:1, fact_3=21:12492, prefix_sum_12=98:56, sum=119:7793)
- Layer 36: `92`, `93`, ` ninety`, ` Ninety`, `91` (target ranks: fact_1=6:53735, fact_2=92:1, fact_3=21:68724, prefix_sum_12=98:46, sum=119:17443)
- Layer 37: `92`, ` ninety`, `}<?`, `uran`, `93` (target ranks: fact_1=6:122090, fact_2=92:1, fact_3=21:114446, prefix_sum_12=98:275, sum=119:26111)
- Layer 38: `92`, `}<?`, `uran`, `<｜begin▁of▁file｜>`, ` uranium` (target ranks: fact_1=6:120611, fact_2=92:1, fact_3=21:124280, prefix_sum_12=98:5693, sum=119:15347)
- Layer 39: `}<?`, `uran`, `ucl`, ` uranium`, `ASI` (target ranks: fact_1=6:4090, fact_2=92:12, fact_3=21:29061, prefix_sum_12=98:98483, sum=119:6257)
- Layer 40: `atomic`, ` atomic`, `uir`, `等待着`, `}<?` (target ranks: fact_1=6:6, fact_2=92:37793, fact_3=21:1677, prefix_sum_12=98:92148, sum=119:2943)
- Layer 41: `atomic`, ` atomic`, `碳`, ` Atomic`, `6` (target ranks: fact_1=6:5, fact_2=92:43503, fact_3=21:8076, prefix_sum_12=98:57328, sum=119:27774)

### Filler position 27 (absolute token 542, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=6:127484, fact_2=92:125745, fact_3=21:125913, prefix_sum_12=98:125271, sum=119:122776)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2913, fact_2=92:11322, fact_3=21:7260, prefix_sum_12=98:9940, sum=119:19412)
- Layer 20: `ait`, `锁定`, ` Walker`, `拆`, `Walker` (target ranks: fact_1=6:2962, fact_2=92:11556, fact_3=21:6564, prefix_sum_12=98:9265, sum=119:29294)
- Layer 30: `回答`, `纯粹的`, ` answer`, `答复`, `回答问题` (target ranks: fact_1=6:8439, fact_2=92:19750, fact_3=21:13561, prefix_sum_12=98:14970, sum=119:37614)
- Layer 35: ` repetition`, `重复`, `回答`, `锁定`, ` repetitions` (target ranks: fact_1=6:6886, fact_2=92:15037, fact_3=21:6171, prefix_sum_12=98:7577, sum=119:23514)
- Layer 36: `重复`, `羊`, `回答`, ` repetition`, `留存` (target ranks: fact_1=6:14693, fact_2=92:24279, fact_3=21:11409, prefix_sum_12=98:7216, sum=119:19263)
- Layer 37: `留存`, `回答问题`, ` drip`, `回答`, `回答道` (target ranks: fact_1=6:55380, fact_2=92:53207, fact_3=21:22332, prefix_sum_12=98:19827, sum=119:24915)
- Layer 38: `歇`, `出声`, `不加`, `留存`, `响应` (target ranks: fact_1=6:65957, fact_2=92:69673, fact_3=21:24614, prefix_sum_12=98:29757, sum=119:27472)
- Layer 39: `}<?`, `响应`, `下沉`, `Respond`, `<｜begin▁of▁sentence｜>` (target ranks: fact_1=6:76837, fact_2=92:96921, fact_3=21:47605, prefix_sum_12=98:57720, sum=119:54235)
- Layer 40: `}<?`, `acl`, `swer`, `anium`, ` talags` (target ranks: fact_1=6:35979, fact_2=92:75563, fact_3=21:38250, prefix_sum_12=98:39104, sum=119:46737)
- Layer 41: `Answer`, `装`, ` ativid`, `回答道`, ` just` (target ranks: fact_1=6:1825, fact_2=92:42622, fact_3=21:27853, prefix_sum_12=98:15909, sum=119:27492)

### Filler position 28 (absolute token 543, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=6:127420, fact_2=92:125734, fact_3=21:125831, prefix_sum_12=98:125227, sum=119:122770)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2721, fact_2=92:11053, fact_3=21:6963, prefix_sum_12=98:9588, sum=119:18849)
- Layer 20: `ait`, ` smile`, `锁定`, ` Walker`, `距` (target ranks: fact_1=6:1533, fact_2=92:10721, fact_3=21:4270, prefix_sum_12=98:8501, sum=119:24604)
- Layer 30: ` repetition`, ` repetitions`, ` sequential`, `aty`, `重复` (target ranks: fact_1=6:5684, fact_2=92:25394, fact_3=21:13853, prefix_sum_12=98:14311, sum=119:42771)
- Layer 35: `重复`, `锁定`, ` reserved`, ` sequential`, ` repetition` (target ranks: fact_1=6:4420, fact_2=92:28220, fact_3=21:6976, prefix_sum_12=98:6448, sum=119:35490)
- Layer 36: `反复`, ` repeated`, `俯`, `重复`, ` stabil` (target ranks: fact_1=6:7809, fact_2=92:35384, fact_3=21:14349, prefix_sum_12=98:6496, sum=119:26609)
- Layer 37: `}<?`, `坏`, `俯`, ` ripple`, `观望` (target ranks: fact_1=6:40574, fact_2=92:77739, fact_3=21:47438, prefix_sum_12=98:21154, sum=119:31985)
- Layer 38: `}<?`, `坏`, `等待着`, `等待`, `留存` (target ranks: fact_1=6:46193, fact_2=92:94356, fact_3=21:51209, prefix_sum_12=98:27397, sum=119:36525)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, `坏`, ` dekameters`, `坏的` (target ranks: fact_1=6:89675, fact_2=92:114149, fact_3=21:95249, prefix_sum_12=98:80537, sum=119:72791)
- Layer 40: `<｜begin▁of▁sentence｜>`, `}<?`, ` .`, `坏`, `装` (target ranks: fact_1=6:37152, fact_2=92:94722, fact_3=21:63070, prefix_sum_12=98:65236, sum=119:57879)
- Layer 41: ` .`, `等待`, `装`, `<｜end▁of▁sentence｜>`, ` .↵↵` (target ranks: fact_1=6:863, fact_2=92:42458, fact_3=21:46559, prefix_sum_12=98:12797, sum=119:19107)

### Filler position 29 (absolute token 544, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `ivables` (target ranks: fact_1=6:127369, fact_2=92:125678, fact_3=21:125807, prefix_sum_12=98:125258, sum=119:122787)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2962, fact_2=92:11868, fact_3=21:7280, prefix_sum_12=98:10208, sum=119:19829)
- Layer 20: `cape`, ` LS`, ` Tears`, `锁定`, `甸` (target ranks: fact_1=6:254, fact_2=92:5646, fact_3=21:792, prefix_sum_12=98:4059, sum=119:11345)
- Layer 30: `cape`, `eder`, `拒`, `柿子`, ` ternary` (target ranks: fact_1=6:1063, fact_2=92:15897, fact_3=21:94, prefix_sum_12=98:6608, sum=119:18538)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=6:44036, fact_2=92:101452, fact_3=21:1, prefix_sum_12=98:41297, sum=119:67580)
- Layer 36: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=6:92231, fact_2=92:112218, fact_3=21:1, prefix_sum_12=98:99883, sum=119:94453)
- Layer 37: `二十一`, `21`, ` XXI`, ` Sc`, `cault` (target ranks: fact_1=6:115324, fact_2=92:118948, fact_3=21:2, prefix_sum_12=98:106515, sum=119:82026)
- Layer 38: `21`, `二十一`, ` Sc`, `Sc`, ` Scrum` (target ranks: fact_1=6:109751, fact_2=92:96667, fact_3=21:1, prefix_sum_12=98:94844, sum=119:69742)
- Layer 39: `二十一`, `21`, `}<?`, ` Nij`, `otomy` (target ranks: fact_1=6:9179, fact_2=92:111423, fact_3=21:2, prefix_sum_12=98:114734, sum=119:71620)
- Layer 40: ` consum`, `二十一`, ` ple`, ` catch`, `21` (target ranks: fact_1=6:87, fact_2=92:108119, fact_3=21:5, prefix_sum_12=98:97662, sum=119:27815)
- Layer 41: ` waiting`, ` fused`, ` because`, ` awaiting`, `耘` (target ranks: fact_1=6:319, fact_2=92:98981, fact_3=21:663, prefix_sum_12=98:61729, sum=119:70570)

### Filler position 30 (absolute token 545, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=6:127518, fact_2=92:125996, fact_3=21:126009, prefix_sum_12=98:125517, sum=119:123156)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2531, fact_2=92:11129, fact_3=21:6825, prefix_sum_12=98:9612, sum=119:19570)
- Layer 20: ` smile`, `锁定`, `atile`, `足`, ` LS` (target ranks: fact_1=6:1650, fact_2=92:13311, fact_3=21:4672, prefix_sum_12=98:10342, sum=119:28664)
- Layer 30: `�`, `忑`, `锁定`, `鞍`, ` reserved` (target ranks: fact_1=6:4587, fact_2=92:43032, fact_3=21:13003, prefix_sum_12=98:19072, sum=119:58260)
- Layer 35: `锁定`, `羊`, ` reserved`, ` tap`, `足` (target ranks: fact_1=6:2421, fact_2=92:41491, fact_3=21:6785, prefix_sum_12=98:11598, sum=119:43342)
- Layer 36: `羊`, ` tap`, ` stabil`, `留存`, ` reserved` (target ranks: fact_1=6:2262, fact_2=92:40593, fact_3=21:10122, prefix_sum_12=98:7536, sum=119:30662)
- Layer 37: `坏`, `}<?`, `atinum`, `殿堂`, ` platinum` (target ranks: fact_1=6:21932, fact_2=92:103208, fact_3=21:51134, prefix_sum_12=98:38345, sum=119:46892)
- Layer 38: `坏`, `osit`, `�`, `坏的`, `殿堂` (target ranks: fact_1=6:37326, fact_2=92:109559, fact_3=21:68681, prefix_sum_12=98:53793, sum=119:45033)
- Layer 39: `<｜begin▁of▁sentence｜>`, `osit`, `�`, `}<?`, `坏` (target ranks: fact_1=6:87881, fact_2=92:119616, fact_3=21:91006, prefix_sum_12=98:87291, sum=119:80762)
- Layer 40: `<｜begin▁of▁sentence｜>`, ` .`, `osit`, `装`, `坏` (target ranks: fact_1=6:27840, fact_2=92:97599, fact_3=21:51212, prefix_sum_12=98:54755, sum=119:60449)
- Layer 41: ` .`, `装`, `袄`, `鹃`, `<｜end▁of▁sentence｜>` (target ranks: fact_1=6:1350, fact_2=92:66975, fact_3=21:31629, prefix_sum_12=98:13438, sum=119:39818)

### Filler position 31 (absolute token 546, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `ivables` (target ranks: fact_1=6:127475, fact_2=92:125991, fact_3=21:126019, prefix_sum_12=98:125558, sum=119:123499)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2248, fact_2=92:10697, fact_3=21:6599, prefix_sum_12=98:9137, sum=119:19422)
- Layer 20: `锁定`, ` smile`, `ait`, ` LS`, `甸` (target ranks: fact_1=6:1088, fact_2=92:5930, fact_3=21:3369, prefix_sum_12=98:5501, sum=119:16941)
- Layer 30: `鞍`, `Tap`, `Subt`, ` Cogn`, `总体` (target ranks: fact_1=6:7411, fact_2=92:664, fact_3=21:12442, prefix_sum_12=98:1350, sum=119:8071)
- Layer 35: ` labor`, `328`, `锁定`, `301`, `足` (target ranks: fact_1=6:4538, fact_2=92:694, fact_3=21:15414, prefix_sum_12=98:340, sum=119:1979)
- Layer 36: `328`, `306`, `296`, `308`, `286` (target ranks: fact_1=6:15844, fact_2=92:622, fact_3=21:51411, prefix_sum_12=98:278, sum=119:227)
- Layer 37: `306`, `296`, `328`, `308`, `292` (target ranks: fact_1=6:37883, fact_2=92:124, fact_3=21:69743, prefix_sum_12=98:325, sum=119:158)
- Layer 38: `306`, `296`, `295`, `305`, `309` (target ranks: fact_1=6:61184, fact_2=92:1712, fact_3=21:82075, prefix_sum_12=98:1112, sum=119:52)
- Layer 39: `}<?`, `覆`, `东海`, `plet`, ` sixth` (target ranks: fact_1=6:490, fact_2=92:76193, fact_3=21:14957, prefix_sum_12=98:30931, sum=119:582)
- Layer 40: `覆`, ` embargo`, `6`, `omit`, ` atomic` (target ranks: fact_1=6:3, fact_2=92:54641, fact_3=21:1779, prefix_sum_12=98:30235, sum=119:1741)
- Layer 41: `出不穷`, ` waiting`, `需要注意的是`, ` awaiting`, `因为这些` (target ranks: fact_1=6:36, fact_2=92:101828, fact_3=21:4463, prefix_sum_12=98:64992, sum=119:24159)

### Filler position 32 (absolute token 547, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127824, fact_2=92:126380, fact_3=21:126325, prefix_sum_12=98:126009, sum=119:123846)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2256, fact_2=92:9936, fact_3=21:6573, prefix_sum_12=98:8568, sum=119:18559)
- Layer 20: `锁定`, `足`, ` smile`, `ait`, `甸` (target ranks: fact_1=6:873, fact_2=92:5873, fact_3=21:2592, prefix_sum_12=98:4198, sum=119:14895)
- Layer 30: `碳`, ` carbon`, ` Carbon`, `Tap`, `carbon` (target ranks: fact_1=6:1506, fact_2=92:21843, fact_3=21:5797, prefix_sum_12=98:12519, sum=119:21047)
- Layer 35: `碳`, ` carbon`, ` Carbon`, `Carbon`, `carbon` (target ranks: fact_1=6:215, fact_2=92:10353, fact_3=21:2240, prefix_sum_12=98:5070, sum=119:17742)
- Layer 36: `碳`, ` carbon`, ` Carbon`, `carbon`, `Carbon` (target ranks: fact_1=6:454, fact_2=92:16154, fact_3=21:10813, prefix_sum_12=98:6841, sum=119:12181)
- Layer 37: ` carbon`, `碳`, `carbon`, ` Carbon`, `Carbon` (target ranks: fact_1=6:85, fact_2=92:9687, fact_3=21:35118, prefix_sum_12=98:4304, sum=119:6820)
- Layer 38: `carbon`, ` carbon`, ` Carbon`, `碳`, `ocarbon` (target ranks: fact_1=6:84, fact_2=92:11774, fact_3=21:59335, prefix_sum_12=98:8955, sum=119:17497)
- Layer 39: `}<?`, `carbon`, ` carbon`, ` Carbon`, `炭` (target ranks: fact_1=6:613, fact_2=92:74067, fact_3=21:71880, prefix_sum_12=98:38214, sum=119:45573)
- Layer 40: `scr`, `留存`, `atomic`, `6`, ` embargo` (target ranks: fact_1=6:4, fact_2=92:17012, fact_3=21:23758, prefix_sum_12=98:5115, sum=119:7615)
- Layer 41: ` .`, `6`, ` `, `留存`, ` atomic` (target ranks: fact_1=6:2, fact_2=92:24686, fact_3=21:26300, prefix_sum_12=98:4832, sum=119:16581)

### Filler position 33 (absolute token 548, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127809, fact_2=92:126501, fact_3=21:126370, prefix_sum_12=98:126031, sum=119:124074)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2469, fact_2=92:10029, fact_3=21:6796, prefix_sum_12=98:8893, sum=119:18531)
- Layer 20: ` LS`, `ait`, ` Walker`, `锁定`, `Walker` (target ranks: fact_1=6:471, fact_2=92:5778, fact_3=21:1428, prefix_sum_12=98:3515, sum=119:13494)
- Layer 30: `acin`, `acos`, ` Reich`, `柿子`, ` labor` (target ranks: fact_1=6:8222, fact_2=92:37324, fact_3=21:2058, prefix_sum_12=98:7756, sum=119:22082)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, `twenty` (target ranks: fact_1=6:75516, fact_2=92:112985, fact_3=21:1, prefix_sum_12=98:46652, sum=119:75052)
- Layer 36: `二十一`, `21`, ` XXI`, ` Twenty`, ` twenty` (target ranks: fact_1=6:118145, fact_2=92:125205, fact_3=21:2, prefix_sum_12=98:115644, sum=119:113894)
- Layer 37: `二十一`, `21`, ` XXI`, `}<?`, `?datasetId` (target ranks: fact_1=6:121680, fact_2=92:120039, fact_3=21:2, prefix_sum_12=98:111681, sum=119:102767)
- Layer 38: `二十一`, `21`, `散射`, `acons`, ` sumala` (target ranks: fact_1=6:112942, fact_2=92:92776, fact_3=21:2, prefix_sum_12=98:103791, sum=119:91629)
- Layer 39: `二十一`, `-ulo`, `}<?`, ` milimetro`, `宰` (target ranks: fact_1=6:23922, fact_2=92:109623, fact_3=21:7, prefix_sum_12=98:110052, sum=119:25067)
- Layer 40: `二十一`, `}<?`, `anium`, ` milimetro`, ` catch` (target ranks: fact_1=6:629, fact_2=92:94935, fact_3=21:8, prefix_sum_12=98:60613, sum=119:2408)
- Layer 41: `二十一`, `有的时候`, ` atomic`, ` milimetro`, `^^^^^^^^` (target ranks: fact_1=6:190, fact_2=92:97044, fact_3=21:197, prefix_sum_12=98:35372, sum=119:21912)

### Filler position 34 (absolute token 549, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127896, fact_2=92:126569, fact_3=21:126499, prefix_sum_12=98:126141, sum=119:124104)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2477, fact_2=92:10453, fact_3=21:6897, prefix_sum_12=98:9261, sum=119:19107)
- Layer 20: `足`, `锁定`, `ait`, `cape`, `胃癌` (target ranks: fact_1=6:1242, fact_2=92:13113, fact_3=21:2973, prefix_sum_12=98:9268, sum=119:23581)
- Layer 30: `保留`, `atan`, `acin`, `acic`, `�` (target ranks: fact_1=6:3270, fact_2=92:30316, fact_3=21:7944, prefix_sum_12=98:18061, sum=119:37336)
- Layer 35: `碳`, ` carbon`, ` Carbon`, `carbon`, `Carbon` (target ranks: fact_1=6:431, fact_2=92:3871, fact_3=21:5970, prefix_sum_12=98:1857, sum=119:10820)
- Layer 36: ` carbon`, `碳`, `留存`, `carbon`, ` Carbon` (target ranks: fact_1=6:349, fact_2=92:4780, fact_3=21:15998, prefix_sum_12=98:2661, sum=119:5999)
- Layer 37: ` atomic`, `atomic`, `carbon`, ` carbon`, ` Atomic` (target ranks: fact_1=6:1937, fact_2=92:19250, fact_3=21:63783, prefix_sum_12=98:9266, sum=119:8338)
- Layer 38: ` atomic`, `atomic`, `carbon`, ` Pt`, `zat` (target ranks: fact_1=6:4351, fact_2=92:22565, fact_3=21:72188, prefix_sum_12=98:13274, sum=119:11233)
- Layer 39: `atomic`, ` atomic`, `�`, ` sublim`, ` Pt` (target ranks: fact_1=6:8754, fact_2=92:57940, fact_3=21:51096, prefix_sum_12=98:46057, sum=119:29541)
- Layer 40: `atomic`, ` atomic`, `留存`, `scr`, ` Uran` (target ranks: fact_1=6:458, fact_2=92:21261, fact_3=21:17138, prefix_sum_12=98:12600, sum=119:7943)
- Layer 41: `atomic`, ` atomic`, ` Atomic`, `原子`, `留存` (target ranks: fact_1=6:6, fact_2=92:11247, fact_3=21:3875, prefix_sum_12=98:6861, sum=119:6259)

### Filler position 35 (absolute token 550, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127896, fact_2=92:126589, fact_3=21:126540, prefix_sum_12=98:126158, sum=119:124101)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3326, fact_2=92:12554, fact_3=21:7908, prefix_sum_12=98:10915, sum=119:20927)
- Layer 20: ` smile`, `胃癌`, `足`, `ait`, `cape` (target ranks: fact_1=6:857, fact_2=92:9607, fact_3=21:2040, prefix_sum_12=98:6931, sum=119:23017)
- Layer 30: `acin`, ` tap`, `acic`, `Tap`, `tap` (target ranks: fact_1=6:7837, fact_2=92:27348, fact_3=21:11953, prefix_sum_12=98:13762, sum=119:31245)
- Layer 35: `锁定`, `acic`, `重复`, ` tap`, `粥` (target ranks: fact_1=6:4732, fact_2=92:32842, fact_3=21:10273, prefix_sum_12=98:8432, sum=119:24111)
- Layer 36: ` tap`, `坏`, `反复`, `粥`, ` Tap` (target ranks: fact_1=6:5540, fact_2=92:35931, fact_3=21:16671, prefix_sum_12=98:7947, sum=119:15468)
- Layer 37: `}<?`, `坏`, ` compounding`, `acet`, `装` (target ranks: fact_1=6:40010, fact_2=92:98939, fact_3=21:55813, prefix_sum_12=98:33505, sum=119:27872)
- Layer 38: `坏`, `}<?`, `acet`, ` nasod`, `pac` (target ranks: fact_1=6:41171, fact_2=92:91670, fact_3=21:62079, prefix_sum_12=98:35614, sum=119:27585)
- Layer 39: `}<?`, `坏`, `坏的`, `陪`, ` nasod` (target ranks: fact_1=6:91093, fact_2=92:113336, fact_3=21:65583, prefix_sum_12=98:82963, sum=119:66305)
- Layer 40: ` .`, `坏`, ` nasod`, `坏的`, `装` (target ranks: fact_1=6:38494, fact_2=92:82337, fact_3=21:25703, prefix_sum_12=98:50844, sum=119:51392)
- Layer 41: ` .`, ` .↵↵`, `<｜end▁of▁sentence｜>`, `.,`, ` ` (target ranks: fact_1=6:692, fact_2=92:31652, fact_3=21:8445, prefix_sum_12=98:8461, sum=119:13011)

### Filler position 36 (absolute token 551, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127926, fact_2=92:126798, fact_3=21:126559, prefix_sum_12=98:126319, sum=119:124283)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3482, fact_2=92:12963, fact_3=21:8023, prefix_sum_12=98:11259, sum=119:21946)
- Layer 20: `ait`, `足`, ` smile`, `能被`, `胃癌` (target ranks: fact_1=6:1322, fact_2=92:10416, fact_3=21:2576, prefix_sum_12=98:6468, sum=119:22563)
- Layer 30: `总体`, ` SK`, `�`, `acet`, `acic` (target ranks: fact_1=6:20481, fact_2=92:19708, fact_3=21:12534, prefix_sum_12=98:8395, sum=119:47425)
- Layer 35: `锁定`, ` vertical`, `Tap`, `cape`, ` academy` (target ranks: fact_1=6:4487, fact_2=92:1941, fact_3=21:4896, prefix_sum_12=98:686, sum=119:6092)
- Layer 36: `}<?`, ` vertical`, `cod`, `翻`, ` triplet` (target ranks: fact_1=6:28130, fact_2=92:2596, fact_3=21:40821, prefix_sum_12=98:1108, sum=119:965)
- Layer 37: `}<?`, `zat`, `interpret`, `轨迹`, ` dekameters` (target ranks: fact_1=6:79737, fact_2=92:1841, fact_3=21:51322, prefix_sum_12=98:5156, sum=119:1598)
- Layer 38: `}<?`, `interpret`, `院内`, `zat`, `殿堂` (target ranks: fact_1=6:68024, fact_2=92:8369, fact_3=21:80906, prefix_sum_12=98:6847, sum=119:799)
- Layer 39: `}<?`, `interpret`, `zat`, `108`, ` smoothed` (target ranks: fact_1=6:5761, fact_2=92:113822, fact_3=21:10545, prefix_sum_12=98:36996, sum=119:147)
- Layer 40: `}<?`, `zat`, ` `, `留存`, `106` (target ranks: fact_1=6:300, fact_2=92:94674, fact_3=21:1088, prefix_sum_12=98:23740, sum=119:497)
- Layer 41: `相比之下`, ` compounded`, ` interpreted`, ` because`, ` interpretation` (target ranks: fact_1=6:118, fact_2=92:77675, fact_3=21:952, prefix_sum_12=98:15599, sum=119:5573)

### Filler position 37 (absolute token 552, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127912, fact_2=92:126766, fact_3=21:126531, prefix_sum_12=98:126286, sum=119:124304)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3394, fact_2=92:13229, fact_3=21:8136, prefix_sum_12=98:11434, sum=119:22777)
- Layer 20: `能被`, ` LS`, `LS`, `ait`, `cape` (target ranks: fact_1=6:527, fact_2=92:10098, fact_3=21:1074, prefix_sum_12=98:4612, sum=119:20637)
- Layer 30: `eder`, `sac`, `obin`, `耐`, `拒` (target ranks: fact_1=6:2396, fact_2=92:39406, fact_3=21:47, prefix_sum_12=98:7885, sum=119:27229)
- Layer 35: `21`, `二十一`, ` XXI`, ` twenty`, ` Twenty` (target ranks: fact_1=6:66321, fact_2=92:120515, fact_3=21:1, prefix_sum_12=98:44617, sum=119:69354)
- Layer 36: `21`, `二十一`, ` XXI`, ` Twenty`, ` twenty` (target ranks: fact_1=6:116291, fact_2=92:125381, fact_3=21:1, prefix_sum_12=98:111813, sum=119:110750)
- Layer 37: `二十一`, `21`, ` XXI`, ` Twenty`, `}<?` (target ranks: fact_1=6:125231, fact_2=92:126294, fact_3=21:2, prefix_sum_12=98:117681, sum=119:103942)
- Layer 38: `21`, `二十一`, ` XXI`, `斯科`, ` Sc` (target ranks: fact_1=6:119877, fact_2=92:120971, fact_3=21:1, prefix_sum_12=98:112253, sum=119:79784)
- Layer 39: `二十一`, `}<?`, `21`, ` XXI`, ` Gai` (target ranks: fact_1=6:25479, fact_2=92:101820, fact_3=21:3, prefix_sum_12=98:108808, sum=119:31866)
- Layer 40: `二十一`, `}<?`, `21`, `atomic`, ` consum` (target ranks: fact_1=6:601, fact_2=92:82574, fact_3=21:3, prefix_sum_12=98:76869, sum=119:3041)
- Layer 41: ` atomic`, `二十一`, `atomic`, ` waiting`, `等待` (target ranks: fact_1=6:49, fact_2=92:53833, fact_3=21:22, prefix_sum_12=98:18532, sum=119:12483)

### Filler position 38 (absolute token 553, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:128022, fact_2=92:126937, fact_3=21:126688, prefix_sum_12=98:126519, sum=119:124593)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2940, fact_2=92:12336, fact_3=21:7547, prefix_sum_12=98:10612, sum=119:21865)
- Layer 20: `忑`, `ait`, `能被`, ` ES`, ` engaging` (target ranks: fact_1=6:3675, fact_2=92:17672, fact_3=21:8053, prefix_sum_12=98:9996, sum=119:40229)
- Layer 30: `鞍`, `Subt`, ` Rhe`, ` neon`, ` Neon` (target ranks: fact_1=6:14386, fact_2=92:40741, fact_3=21:7996, prefix_sum_12=98:18077, sum=119:82542)
- Layer 35: `羊`, `镁`, `鞍`, ` tap`, ` prot` (target ranks: fact_1=6:5081, fact_2=92:31152, fact_3=21:3689, prefix_sum_12=98:9133, sum=119:45935)
- Layer 36: `羊`, ` stabil`, `镁`, `acin`, ` tap` (target ranks: fact_1=6:5339, fact_2=92:24645, fact_3=21:4860, prefix_sum_12=98:5016, sum=119:19867)
- Layer 37: ` prot`, ` gold`, `anium`, `�`, `镁` (target ranks: fact_1=6:22765, fact_2=92:50404, fact_3=21:12535, prefix_sum_12=98:11139, sum=119:28370)
- Layer 38: `�`, `�`, `�`, `anium`, `镁` (target ranks: fact_1=6:33001, fact_2=92:71359, fact_3=21:19859, prefix_sum_12=98:28441, sum=119:35050)
- Layer 39: `<｜begin▁of▁sentence｜>`, `�`, `osit`, `打磨`, `}<?` (target ranks: fact_1=6:83661, fact_2=92:97496, fact_3=21:52955, prefix_sum_12=98:53056, sum=119:70056)
- Layer 40: ` helium`, `osit`, `�`, `helium`, `装` (target ranks: fact_1=6:34278, fact_2=92:82354, fact_3=21:22952, prefix_sum_12=98:28438, sum=119:50755)
- Layer 41: ` .`, ` chromium`, `装`, `瘤`, ` waiting` (target ranks: fact_1=6:1445, fact_2=92:39290, fact_3=21:10973, prefix_sum_12=98:6899, sum=119:26045)

### Filler position 39 (absolute token 554, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127822, fact_2=92:126724, fact_3=21:126428, prefix_sum_12=98:126229, sum=119:124372)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3233, fact_2=92:12365, fact_3=21:8044, prefix_sum_12=98:10952, sum=119:21844)
- Layer 20: `ait`, `锁定`, ` Walker`, ` ES`, `鞍` (target ranks: fact_1=6:2684, fact_2=92:8523, fact_3=21:5747, prefix_sum_12=98:5769, sum=119:22354)
- Layer 30: `uir`, `acet`, `subt`, ` consum`, `iret` (target ranks: fact_1=6:63903, fact_2=92:2761, fact_3=21:26089, prefix_sum_12=98:1112, sum=119:25013)
- Layer 35: `79`, `86`, `286`, `78`, `294` (target ranks: fact_1=6:7779, fact_2=92:19, fact_3=21:12520, prefix_sum_12=98:10, sum=119:496)
- Layer 36: `286`, `294`, `296`, `86`, `93` (target ranks: fact_1=6:32071, fact_2=92:28, fact_3=21:68383, prefix_sum_12=98:16, sum=119:117)
- Layer 37: `}<?`, `?datasetId`, ` Zed`, `AMI`, ` ---|---|---|---|---|---|---` (target ranks: fact_1=6:72840, fact_2=92:12, fact_3=21:85810, prefix_sum_12=98:44, sum=119:548)
- Layer 38: `}<?`, `296`, `294`, `295`, `292` (target ranks: fact_1=6:69587, fact_2=92:68, fact_3=21:79309, prefix_sum_12=98:47, sum=119:72)
- Layer 39: `}<?`, `覆`, `instant`, `tanle`, `amina` (target ranks: fact_1=6:53485, fact_2=92:46990, fact_3=21:54268, prefix_sum_12=98:7237, sum=119:1483)
- Layer 40: `}<?`, `等待着`, ` atomic`, `amn`, `覆` (target ranks: fact_1=6:5766, fact_2=92:29739, fact_3=21:10681, prefix_sum_12=98:10603, sum=119:2784)
- Layer 41: `))))`, `因为这些`, `太多了`, `}}}}`, ` atomic` (target ranks: fact_1=6:51, fact_2=92:37535, fact_3=21:2376, prefix_sum_12=98:13489, sum=119:8405)

### Filler position 40 (absolute token 555, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127844, fact_2=92:126670, fact_3=21:126383, prefix_sum_12=98:126211, sum=119:124184)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3218, fact_2=92:12255, fact_3=21:7888, prefix_sum_12=98:11023, sum=119:21625)
- Layer 20: `ait`, `锁定`, `鞍`, ` LS`, `ätte` (target ranks: fact_1=6:1660, fact_2=92:9103, fact_3=21:3853, prefix_sum_12=98:6561, sum=119:21735)
- Layer 30: `}<?`, `acos`, `acet`, `otos`, `iret` (target ranks: fact_1=6:81172, fact_2=92:16188, fact_3=21:24115, prefix_sum_12=98:12753, sum=119:42539)
- Layer 35: `锁定`, `79`, ` static`, ` lock`, `柿子` (target ranks: fact_1=6:18991, fact_2=92:36, fact_3=21:5980, prefix_sum_12=98:279, sum=119:2092)
- Layer 36: `}<?`, `93`, `79`, `uran`, `iret` (target ranks: fact_1=6:61762, fact_2=92:33, fact_3=21:45925, prefix_sum_12=98:352, sum=119:71)
- Layer 37: `}<?`, `?datasetId`, `uran`, `93`, `Quintal` (target ranks: fact_1=6:99289, fact_2=92:6, fact_3=21:57334, prefix_sum_12=98:462, sum=119:181)
- Layer 38: `}<?`, `105`, `院内`, `102`, `本题分析` (target ranks: fact_1=6:96219, fact_2=92:80, fact_3=21:77668, prefix_sum_12=98:150, sum=119:34)
- Layer 39: `}<?`, `105`, `104`, `灵气`, `107` (target ranks: fact_1=6:67376, fact_2=92:69934, fact_3=21:24010, prefix_sum_12=98:18107, sum=119:65)
- Layer 40: `}<?`, ` atomic`, `留存`, `atomic`, `amn` (target ranks: fact_1=6:14736, fact_2=92:39028, fact_3=21:2903, prefix_sum_12=98:11718, sum=119:286)
- Layer 41: ` atomic`, `因为这些`, `太多了`, `笔趣`, ` dekameters` (target ranks: fact_1=6:92, fact_2=92:40869, fact_3=21:718, prefix_sum_12=98:11782, sum=119:2175)

### Filler position 41 (absolute token 556, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127857, fact_2=92:126716, fact_3=21:126451, prefix_sum_12=98:126277, sum=119:124449)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3207, fact_2=92:12698, fact_3=21:8008, prefix_sum_12=98:11418, sum=119:22029)
- Layer 20: `锁定`, ` smile`, `ession`, `胃癌`, `距` (target ranks: fact_1=6:984, fact_2=92:6629, fact_3=21:2080, prefix_sum_12=98:3717, sum=119:19712)
- Layer 30: `acos`, `俯`, `保留`, ` tap`, ` picnic` (target ranks: fact_1=6:6894, fact_2=92:17960, fact_3=21:6165, prefix_sum_12=98:5244, sum=119:47560)
- Layer 35: ` Gol`, `�`, `anium`, `eder`, `acos` (target ranks: fact_1=6:343, fact_2=92:7, fact_3=21:11148, prefix_sum_12=98:227, sum=119:18540)
- Layer 36: `92`, `anium`, `留存`, `acos`, `eder` (target ranks: fact_1=6:654, fact_2=92:1, fact_3=21:53926, prefix_sum_12=98:505, sum=119:13811)
- Layer 37: `}<?`, `92`, `acos`, ` Uran`, ` uranium` (target ranks: fact_1=6:3214, fact_2=92:2, fact_3=21:89075, prefix_sum_12=98:1133, sum=119:16587)
- Layer 38: `}<?`, `92`, `本题分析`, ` Sixth`, ` Uran` (target ranks: fact_1=6:159, fact_2=92:2, fact_3=21:92274, prefix_sum_12=98:3313, sum=119:14505)
- Layer 39: `}<?`, ` Sixth`, ` sixth`, ` šest`, ` six` (target ranks: fact_1=6:81, fact_2=92:337, fact_3=21:22653, prefix_sum_12=98:93866, sum=119:17297)
- Layer 40: `留存`, ` `, `坏`, `}<?`, ` six` (target ranks: fact_1=6:15, fact_2=92:64036, fact_3=21:773, prefix_sum_12=98:53912, sum=119:6968)
- Layer 41: ` .`, ` `, ` compounded`, ` smooth`, ` because` (target ranks: fact_1=6:20, fact_2=92:62486, fact_3=21:1284, prefix_sum_12=98:33638, sum=119:10375)

### Filler position 42 (absolute token 557, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127912, fact_2=92:126705, fact_3=21:126508, prefix_sum_12=98:126300, sum=119:124241)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3122, fact_2=92:13032, fact_3=21:7812, prefix_sum_12=98:11526, sum=119:22296)
- Layer 20: `ession`, ` smile`, `锁定`, `足`, `cape` (target ranks: fact_1=6:1566, fact_2=92:13302, fact_3=21:2547, prefix_sum_12=98:6183, sum=119:23067)
- Layer 30: `�`, `atan`, `保留`, ` reserved`, `柿子` (target ranks: fact_1=6:7392, fact_2=92:55401, fact_3=21:6553, prefix_sum_12=98:16074, sum=119:53251)
- Layer 35: `沛`, `�`, `碳`, `six`, ` six` (target ranks: fact_1=6:9, fact_2=92:6818, fact_3=21:9118, prefix_sum_12=98:1608, sum=119:33328)
- Layer 36: ` six`, `沛`, ` Sixth`, `�`, `six` (target ranks: fact_1=6:9, fact_2=92:18797, fact_3=21:67461, prefix_sum_12=98:10747, sum=119:31849)
- Layer 37: ` Sixth`, ` sixth`, ` six`, `}<?`, ` šest` (target ranks: fact_1=6:37, fact_2=92:64026, fact_3=21:116717, prefix_sum_12=98:44452, sum=119:48559)
- Layer 38: `}<?`, ` medief`, `romic`, `ophyll`, `radesh` (target ranks: fact_1=6:1383, fact_2=92:62201, fact_3=21:118751, prefix_sum_12=98:41232, sum=119:43242)
- Layer 39: `}<?`, ` medief`, `�`, `东海`, `romic` (target ranks: fact_1=6:2966, fact_2=92:28191, fact_3=21:1316, prefix_sum_12=98:91604, sum=119:60022)
- Layer 40: ` twenty`, ` Twenty`, `二十一`, `21`, `二十` (target ranks: fact_1=6:141, fact_2=92:8989, fact_3=21:4, prefix_sum_12=98:28724, sum=119:24528)
- Layer 41: ` .`, ` twenty`, ` atomic`, `二十一`, `二十` (target ranks: fact_1=6:10, fact_2=92:5249, fact_3=21:6, prefix_sum_12=98:13547, sum=119:14185)

### Filler position 43 (absolute token 558, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127834, fact_2=92:126614, fact_3=21:126376, prefix_sum_12=98:126231, sum=119:124217)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:2950, fact_2=92:12785, fact_3=21:7657, prefix_sum_12=98:11218, sum=119:23080)
- Layer 20: `LS`, ` LS`, ` ES`, `能被`, `锁定` (target ranks: fact_1=6:607, fact_2=92:4588, fact_3=21:1806, prefix_sum_12=98:2677, sum=119:14090)
- Layer 30: ` pakig`, ` total`, `acos`, ` uranium`, `加起来` (target ranks: fact_1=6:56210, fact_2=92:21938, fact_3=21:10391, prefix_sum_12=98:15535, sum=119:30828)
- Layer 35: ` carbon`, `六十`, `碳`, `86`, `carbon` (target ranks: fact_1=6:1170, fact_2=92:625, fact_3=21:430, prefix_sum_12=98:2733, sum=119:19930)
- Layer 36: `三十六`, `大王`, `三十五`, `86`, ` Ginhadi` (target ranks: fact_1=6:1873, fact_2=92:1804, fact_3=21:33783, prefix_sum_12=98:19152, sum=119:29490)
- Layer 37: `86`, `92`, `大王`, `76`, `uran` (target ranks: fact_1=6:10952, fact_2=92:2, fact_3=21:27739, prefix_sum_12=98:2723, sum=119:8331)
- Layer 38: `}<?`, `92`, `大王`, `本题分析`, ` transcend` (target ranks: fact_1=6:23041, fact_2=92:2, fact_3=21:62431, prefix_sum_12=98:591, sum=119:4677)
- Layer 39: ` Sixth`, ` sixth`, `-ulo`, `tanle`, ` šest` (target ranks: fact_1=6:142, fact_2=92:56919, fact_3=21:345, prefix_sum_12=98:82939, sum=119:4162)
- Layer 40: ` atomic`, ` six`, `atomic`, `6`, ` šest` (target ranks: fact_1=6:4, fact_2=92:42187, fact_3=21:131, prefix_sum_12=98:41468, sum=119:4779)
- Layer 41: ` atomic`, `}}}}`, `atomic`, `}}}`, `))))` (target ranks: fact_1=6:53, fact_2=92:72075, fact_3=21:2332, prefix_sum_12=98:44108, sum=119:26943)

### Filler position 44 (absolute token 559, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127788, fact_2=92:126617, fact_3=21:126349, prefix_sum_12=98:126231, sum=119:124322)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3101, fact_2=92:12685, fact_3=21:7981, prefix_sum_12=98:11258, sum=119:23049)
- Layer 20: `锁定`, ` ES`, `ait`, `能被`, `忑` (target ranks: fact_1=6:1828, fact_2=92:11713, fact_3=21:4529, prefix_sum_12=98:6402, sum=119:21862)
- Layer 30: `acos`, ` SK`, `otor`, `acet`, ` Rig` (target ranks: fact_1=6:65601, fact_2=92:20103, fact_3=21:28763, prefix_sum_12=98:7248, sum=119:51353)
- Layer 35: `78`, `79`, `38`, `37`, `57` (target ranks: fact_1=6:24682, fact_2=92:1874, fact_3=21:2424, prefix_sum_12=98:994, sum=119:13765)
- Layer 36: `}<?`, `78`, `79`, `68`, `77` (target ranks: fact_1=6:69118, fact_2=92:1301, fact_3=21:28244, prefix_sum_12=98:754, sum=119:1279)
- Layer 37: `}<?`, `?datasetId`, `Quintal`, `78`, `79` (target ranks: fact_1=6:97973, fact_2=92:181, fact_3=21:33228, prefix_sum_12=98:493, sum=119:326)
- Layer 38: `}<?`, `enal`, `院内`, ` honors`, `oye` (target ranks: fact_1=6:82537, fact_2=92:298, fact_3=21:73254, prefix_sum_12=98:647, sum=119:235)
- Layer 39: `}<?`, `instant`, `tanle`, `东海`, `odea` (target ranks: fact_1=6:7699, fact_2=92:82905, fact_3=21:2398, prefix_sum_12=98:44200, sum=119:5855)
- Layer 40: `}<?`, ` atomic`, `处以`, `关照`, `留存` (target ranks: fact_1=6:307, fact_2=92:78740, fact_3=21:460, prefix_sum_12=98:29296, sum=119:4107)
- Layer 41: ` atomic`, `}}}}`, `))))`, `我曾经`, `出不穷` (target ranks: fact_1=6:64, fact_2=92:85864, fact_3=21:3269, prefix_sum_12=98:34965, sum=119:12720)

### Filler position 45 (absolute token 560, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127699, fact_2=92:126513, fact_3=21:126247, prefix_sum_12=98:126103, sum=119:124164)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: fact_1=6:3364, fact_2=92:12606, fact_3=21:8521, prefix_sum_12=98:11457, sum=119:22742)
- Layer 20: `ait`, `会成为`, `妇`, `平行`, ` Walker` (target ranks: fact_1=6:9324, fact_2=92:32851, fact_3=21:12323, prefix_sum_12=98:16706, sum=119:47437)
- Layer 30: `二十八`, `acin`, `acos`, `acic`, `沛` (target ranks: fact_1=6:51277, fact_2=92:57078, fact_3=21:27751, prefix_sum_12=98:10512, sum=119:68760)
- Layer 35: `二十八`, `28`, `acic`, `acin`, `打完` (target ranks: fact_1=6:27392, fact_2=92:58702, fact_3=21:9821, prefix_sum_12=98:3136, sum=119:43649)
- Layer 36: `二十八`, `留存`, `acin`, `28`, `acic` (target ranks: fact_1=6:38887, fact_2=92:66531, fact_3=21:18979, prefix_sum_12=98:3543, sum=119:35372)
- Layer 37: `}<?`, `acet`, `冰冰`, `isis`, `铎` (target ranks: fact_1=6:100441, fact_2=92:108080, fact_3=21:68600, prefix_sum_12=98:21888, sum=119:50940)
- Layer 38: `}<?`, `acet`, `冰冰`, `铎`, ` Erkännande` (target ranks: fact_1=6:81228, fact_2=92:111126, fact_3=21:67718, prefix_sum_12=98:28155, sum=119:54667)
- Layer 39: `}<?`, `铎`, ` dekameters`, `acet`, ` sublim` (target ranks: fact_1=6:92380, fact_2=92:79515, fact_3=21:41254, prefix_sum_12=98:38878, sum=119:49178)
- Layer 40: ` .`, `等待着`, ` Mercury`, `铎`, ` Rutherford` (target ranks: fact_1=6:22561, fact_2=92:17067, fact_3=21:4194, prefix_sum_12=98:7548, sum=119:10154)
- Layer 41: ` .`, ` .↵↵`, `.,`, ` `, `))))` (target ranks: fact_1=6:1249, fact_2=92:11384, fact_3=21:9130, prefix_sum_12=98:3246, sum=119:5602)

### Filler position 46 (absolute token 561, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127805, fact_2=92:126653, fact_3=21:126339, prefix_sum_12=98:126178, sum=119:124204)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: fact_1=6:2989, fact_2=92:11587, fact_3=21:7937, prefix_sum_12=98:10614, sum=119:20908)
- Layer 20: ` blanks`, ` spac`, `blank`, `选取`, ` Blank` (target ranks: fact_1=6:78024, fact_2=92:117299, fact_3=21:21899, prefix_sum_12=98:101317, sum=119:107360)
- Layer 30: ` spac`, `?datasetId`, `}using`, `坝`, ` dekameters` (target ranks: fact_1=6:116996, fact_2=92:122537, fact_3=21:94116, prefix_sum_12=98:117073, sum=119:120158)
- Layer 35: `}using`, `绵绵`, ` panc`, `ovel`, ` integrals` (target ranks: fact_1=6:111448, fact_2=92:108534, fact_3=21:62960, prefix_sum_12=98:82031, sum=119:102341)
- Layer 36: `足足`, `俯`, `ovel`, `ancock`, ` panc` (target ranks: fact_1=6:52550, fact_2=92:57096, fact_3=21:19122, prefix_sum_12=98:30975, sum=119:53897)
- Layer 37: `}<?`, `integr`, `放下`, ` doubling`, `放下了` (target ranks: fact_1=6:100307, fact_2=92:106408, fact_3=21:53729, prefix_sum_12=98:71977, sum=119:73959)
- Layer 38: ` .`, ` Mercury`, `俯`, ` divers`, `坏` (target ranks: fact_1=6:67522, fact_2=92:84948, fact_3=21:27654, prefix_sum_12=98:62807, sum=119:64755)
- Layer 39: ` .`, `<｜begin▁of▁sentence｜>`, ` Mercury`, `铎`, `heck` (target ranks: fact_1=6:84731, fact_2=92:76123, fact_3=21:29005, prefix_sum_12=98:83614, sum=119:82797)
- Layer 40: ` .`, ` Mercury`, `<｜begin▁of▁sentence｜>`, ` .↵↵`, ` nasod` (target ranks: fact_1=6:39657, fact_2=92:51087, fact_3=21:11980, prefix_sum_12=98:53376, sum=119:54349)
- Layer 41: ` .`, ` .↵↵`, ` Mercury`, `这就是`, ` .↵` (target ranks: fact_1=6:3360, fact_2=92:21140, fact_3=21:5294, prefix_sum_12=98:13546, sum=119:20785)

### Filler position 47 (absolute token 562, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127950, fact_2=92:126777, fact_3=21:126485, prefix_sum_12=98:126367, sum=119:124259)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: fact_1=6:3009, fact_2=92:11577, fact_3=21:7797, prefix_sum_12=98:10588, sum=119:20922)
- Layer 20: `}<?`, `)Skip`, `aharoa`, `ozygous`, `东海` (target ranks: fact_1=6:93195, fact_2=92:121669, fact_3=21:41269, prefix_sum_12=98:117613, sum=119:104940)
- Layer 30: `}<?`, `codeline`, `东京`, `AssemblyVersion`, `}using` (target ranks: fact_1=6:104086, fact_2=92:121001, fact_3=21:86553, prefix_sum_12=98:110789, sum=119:116824)
- Layer 35: `codeline`, `ِّف`, `lett`, `}using`, `切割` (target ranks: fact_1=6:115925, fact_2=92:109684, fact_3=21:64107, prefix_sum_12=98:76350, sum=119:119141)
- Layer 36: `足足`, `lett`, `切割`, `生生`, `锯` (target ranks: fact_1=6:72592, fact_2=92:71030, fact_3=21:33621, prefix_sum_12=98:29504, sum=119:80986)
- Layer 37: `}<?`, `磨损`, `东京`, `简体`, `TreeLabel` (target ranks: fact_1=6:105064, fact_2=92:108647, fact_3=21:50029, prefix_sum_12=98:55025, sum=119:89534)
- Layer 38: ` .`, `遁`, `保有`, ` covari`, `切割` (target ranks: fact_1=6:93487, fact_2=92:107834, fact_3=21:34957, prefix_sum_12=98:52939, sum=119:84019)
- Layer 39: `<｜begin▁of▁sentence｜>`, ` .`, `简体`, `遁`, `�` (target ranks: fact_1=6:107694, fact_2=92:101719, fact_3=21:40477, prefix_sum_12=98:68272, sum=119:66736)
- Layer 40: ` .`, ` .↵↵`, `�`, ` .↵`, `<｜begin▁of▁sentence｜>` (target ranks: fact_1=6:57426, fact_2=92:75793, fact_3=21:17451, prefix_sum_12=98:44200, sum=119:35131)
- Layer 41: ` .`, ` .↵↵`, `<｜end▁of▁sentence｜>`, ` .↵`, ` ` (target ranks: fact_1=6:4463, fact_2=92:24946, fact_3=21:3118, prefix_sum_12=98:5172, sum=119:16013)

### Filler position 48 (absolute token 563, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:127971, fact_2=92:126841, fact_3=21:126539, prefix_sum_12=98:126442, sum=119:124444)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: fact_1=6:2792, fact_2=92:11482, fact_3=21:7326, prefix_sum_12=98:10442, sum=119:21382)
- Layer 20: ` instantaneous`, `aplenty`, `aharoa`, `}<?`, `东海` (target ranks: fact_1=6:72587, fact_2=92:107085, fact_3=21:65050, prefix_sum_12=98:99114, sum=119:82746)
- Layer 30: `codeline`, `东京`, ` writ`, `ennettuna`, `Quintal` (target ranks: fact_1=6:45416, fact_2=92:101887, fact_3=21:50118, prefix_sum_12=98:72719, sum=119:99759)
- Layer 35: `codeline`, ` doubly`, `AssemblyVersion`, `白雪`, `删` (target ranks: fact_1=6:75596, fact_2=92:103235, fact_3=21:40435, prefix_sum_12=98:66102, sum=119:118757)
- Layer 36: ` soci`, `/hess`, ` nasod`, `兜`, ` predictions` (target ranks: fact_1=6:29067, fact_2=92:78570, fact_3=21:36410, prefix_sum_12=98:29680, sum=119:86624)
- Layer 37: `Quintal`, `codeline`, `悬挂`, `镶嵌`, `TreeLabel` (target ranks: fact_1=6:86181, fact_2=92:121823, fact_3=21:70372, prefix_sum_12=98:67796, sum=119:109082)
- Layer 38: ` germ`, `悬`, `悬挂`, ` Germ`, ` crev` (target ranks: fact_1=6:51950, fact_2=92:116838, fact_3=21:42114, prefix_sum_12=98:56475, sum=119:93060)
- Layer 39: ` encomp`, ` germ`, ` .↵↵`, ` .`, `贻` (target ranks: fact_1=6:116840, fact_2=92:121067, fact_3=21:68186, prefix_sum_12=98:103146, sum=119:109579)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` germ`, `肤` (target ranks: fact_1=6:77503, fact_2=92:113315, fact_3=21:36043, prefix_sum_12=98:89471, sum=119:101798)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `<｜end▁of▁sentence｜>`, ` germ` (target ranks: fact_1=6:50266, fact_2=92:97421, fact_3=21:29579, prefix_sum_12=98:56030, sum=119:88532)

### Filler position 49 (absolute token 564, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: fact_1=6:128080, fact_2=92:126915, fact_3=21:126686, prefix_sum_12=98:126515, sum=119:124521)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: fact_1=6:2711, fact_2=92:11884, fact_3=21:7515, prefix_sum_12=98:10580, sum=119:22760)
- Layer 20: `文本`, ` grounds`, `裸露`, `站`, `队的` (target ranks: fact_1=6:2852, fact_2=92:64845, fact_3=21:28346, prefix_sum_12=98:27423, sum=119:64443)
- Layer 30: ` Answer`, `答案是`, `codeline`, ` ответ`, ` answer` (target ranks: fact_1=6:120734, fact_2=92:125918, fact_3=21:123146, prefix_sum_12=98:99855, sum=119:123926)
- Layer 35: ` Answer`, `codeline`, ` answer`, `oNames`, ` ответ` (target ranks: fact_1=6:118279, fact_2=92:92330, fact_3=21:113110, prefix_sum_12=98:47526, sum=119:111190)
- Layer 36: ` Answer`, ` answer`, `坏`, `回答`, `Answer` (target ranks: fact_1=6:61602, fact_2=92:34936, fact_3=21:45524, prefix_sum_12=98:3558, sum=119:65924)
- Layer 37: `oNames`, `codeline`, ` encomp`, `оду`, `/MODIS` (target ranks: fact_1=6:113081, fact_2=92:110698, fact_3=21:103852, prefix_sum_12=98:83895, sum=119:120019)
- Layer 38: `oNames`, ` encomp`, `codeline`, `�`, `高等` (target ranks: fact_1=6:115839, fact_2=92:113927, fact_3=21:111024, prefix_sum_12=98:91983, sum=119:119940)
- Layer 39: `-ulo`, ` cryptocur`, ` disadvant`, `►▼`, `�` (target ranks: fact_1=6:110867, fact_2=92:87026, fact_3=21:83099, prefix_sum_12=98:96703, sum=119:110734)
- Layer 40: ` Answer`, ` .↵↵`, ` .`, `Answer`, `esez` (target ranks: fact_1=6:22228, fact_2=92:18386, fact_3=21:10117, prefix_sum_12=98:26846, sum=119:63892)
- Layer 41: ` Answer`, `Answer`, ` .↵↵`, ` .`, ` .↵` (target ranks: fact_1=6:1664, fact_2=92:7577, fact_3=21:3265, prefix_sum_12=98:11715, sum=119:46429)

### Filler position 50 (absolute token 565, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `-ulo` (target ranks: fact_1=6:126799, fact_2=92:121994, fact_3=21:122708, prefix_sum_12=98:121816, sum=119:114605)
- Layer 10: `EDMF`, ` dével`, `�乐`, `aplenty`, `-ulo` (target ranks: fact_1=6:128468, fact_2=92:126292, fact_3=21:124285, prefix_sum_12=98:125345, sum=119:119980)
- Layer 20: `能被`, `��`, ` Submission`, `ait`, `马上就` (target ranks: fact_1=6:7228, fact_2=92:17532, fact_3=21:16282, prefix_sum_12=98:22759, sum=119:69324)
- Layer 30: ` dekameters`, ` المطلع`, ` ---|---|---|---`, ` encomp`, ` Paglin` (target ranks: fact_1=6:120786, fact_2=92:64708, fact_3=21:104413, prefix_sum_12=98:65798, sum=119:81376)
- Layer 35: `92`, ` Uran`, ` uranium`, `uran`, ` Uranus` (target ranks: fact_1=6:14208, fact_2=92:1, fact_3=21:91745, prefix_sum_12=98:62, sum=119:5505)
- Layer 36: `92`, `93`, ` ninety`, ` Ninety`, ` noventa` (target ranks: fact_1=6:33598, fact_2=92:1, fact_3=21:124616, prefix_sum_12=98:21, sum=119:3330)
- Layer 37: `92`, `93`, ` ninety`, ` noventa`, ` Ninety` (target ranks: fact_1=6:63247, fact_2=92:1, fact_3=21:116022, prefix_sum_12=98:34, sum=119:7053)
- Layer 38: `92`, `99`, `98`, ` ninety`, `索` (target ranks: fact_1=6:100622, fact_2=92:1, fact_3=21:89108, prefix_sum_12=98:3, sum=119:338)
- Layer 39: `索`, `本题分析`, `}<?`, ` Uran`, `uran` (target ranks: fact_1=6:81791, fact_2=92:27561, fact_3=21:93736, prefix_sum_12=98:3144, sum=119:2578)
- Layer 40: ` Answer`, ` answer`, `答案`, `Answer`, ` atomic` (target ranks: fact_1=6:32749, fact_2=92:35783, fact_3=21:77713, prefix_sum_12=98:4012, sum=119:626)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: fact_1=6:186, fact_2=92:13763, fact_3=21:7680, prefix_sum_12=98:3446, sum=119:1118)

## Exact rendered prompt

```text
<｜begin▁of▁sentence｜>You will be given a question that requires adding three values together. Answer immediately with just the number, nothing else. No explanation, no words, no reasoning, just the number. After the question, there will be 50 filler tokens (a sequence of dots) before you answer.<｜User｜>Question: What is the atomic number of Helium plus the atomic number of Neon plus the atomic number of Sulfur?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>28<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Cobalt plus the atomic number of Selenium plus the atomic number of Promethium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>122<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Europium plus the atomic number of Tantalum plus the atomic number of Rhenium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>211<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Protactinium plus the atomic number of Thorium plus the atomic number of Tellurium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>233<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Neptunium plus the atomic number of Boron plus the atomic number of Gold?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>177<｜end▁of▁sentence｜><｜User｜>Question: What is the atomic number of Carbon plus the atomic number of Uranium plus the atomic number of Scandium?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
