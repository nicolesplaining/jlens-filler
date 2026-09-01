# First qualitative filler readout

These are **J-Lens token readouts**, not the paper's formal sparse J-space decomposition.

## Outcome

- Filler answer: `224` (correct).
- No-filler answer: `225` (incorrect).
- Filler tokens: 50 tokens at absolute indices 796–845.
- Final-head closure max absolute logit error: `0.0`.

## Direct target-rank summary over filler cells

| Readout | Target | Best filler-cell rank | First rank ≤ 10 |
|---|---|---:|---|
| J-Lens | `base_value=64` | 1 (L23, filler 34) | L22, filler 34 (rank 4) |
| J-Lens | `first_product=128` | 12 (L37, filler 34) | Never |
| J-Lens | `bound_value=119` | 1 (L31, filler 15) | L30, filler 10 (rank 2) |
| J-Lens | `second_product=238` | 1 (L33, filler 41) | L31, filler 10 (rank 4) |
| J-Lens | `answer=224` | 1 (L33, filler 11) | L31, filler 1 (rank 9) |
| Logit lens | `base_value=64` | 1 (L25, filler 40) | L23, filler 34 (rank 9) |
| Logit lens | `first_product=128` | 14 (L35, filler 34) | Never |
| Logit lens | `bound_value=119` | 1 (L31, filler 15) | L29, filler 10 (rank 2) |
| Logit lens | `second_product=238` | 1 (L33, filler 41) | L31, filler 10 (rank 4) |
| Logit lens | `answer=224` | 1 (L36, filler 28) | L30, filler 28 (rank 9) |

## J-Lens top-5 by filler position

### Filler position 1 (absolute token 796, surface ` .`)

- Layer 0: `aplenty`, `尷`, `�乐`, `?datasetId`, `-ulo` (target ranks: base_value=64:119657, first_product=128:114955, bound_value=119:114500, second_product=238:113541, answer=224:115181)
- Layer 10: `anta`, `fine`, `hook`, `Hook`, ` kinain` (target ranks: base_value=64:95814, first_product=128:78160, bound_value=119:84559, second_product=238:78192, answer=224:87936)
- Layer 20: `足`, `扣`, `重`, `垂`, `abric` (target ranks: base_value=64:379, first_product=128:17801, bound_value=119:23349, second_product=238:25851, answer=224:14181)
- Layer 30: `匹配`, `卸`, `66`, `技术与`, `放大` (target ranks: base_value=64:442, first_product=128:39482, bound_value=119:617, second_product=238:1771, answer=224:514)
- Layer 35: `238`, `216`, `234`, `236`, `228` (target ranks: base_value=64:28454, first_product=128:73966, bound_value=119:11241, second_product=238:1, answer=224:14)
- Layer 36: `216`, `acin`, `206`, `224`, `222` (target ranks: base_value=64:102265, first_product=128:63408, bound_value=119:33801, second_product=238:281, answer=224:4)
- Layer 37: `216`, `206`, ` AFP`, `204`, ` Ingg` (target ranks: base_value=64:120665, first_product=128:88801, bound_value=119:52087, second_product=238:457, answer=224:12)
- Layer 38: `216`, `204`, ` dekameters`, `212`, `206` (target ranks: base_value=64:125969, first_product=128:121482, bound_value=119:90869, second_product=238:3689, answer=224:6)
- Layer 39: `204`, ` proiektuak`, `tanle`, `楹`, ` AAI` (target ranks: base_value=64:119564, first_product=128:126620, bound_value=119:119293, second_product=238:31831, answer=224:19)
- Layer 40: ` talags`, ` fountain`, `实在`, ` ald`, ` LD` (target ranks: base_value=64:117148, first_product=128:123087, bound_value=119:116657, second_product=238:54613, answer=224:1159)
- Layer 41: `��`, ` .`, `豆瓣`, ` nuest`, ` oun` (target ranks: base_value=64:104834, first_product=128:116886, bound_value=119:112750, second_product=238:21780, answer=224:4774)

### Filler position 2 (absolute token 797, surface ` .`)

- Layer 0: `尷`, `aplenty`, `?datasetId`, `-ulo`, `�乐` (target ranks: base_value=64:121900, first_product=128:119093, bound_value=119:118845, second_product=238:119097, answer=224:118946)
- Layer 10: ` Walker`, `Walker`, `ait`, `从哪里`, `atile` (target ranks: base_value=64:19837, first_product=128:35796, bound_value=119:36217, second_product=238:35245, answer=224:37899)
- Layer 20: ` .----`, `往常`, `oraly`, `ools`, `中书` (target ranks: base_value=64:126012, first_product=128:128863, bound_value=119:129167, second_product=238:126513, answer=224:127749)
- Layer 30: ` talags`, ` hilabihan`, ` pakig`, ` dekameters`, ` gilay` (target ranks: base_value=64:119961, first_product=128:124789, bound_value=119:128374, second_product=238:120537, answer=224:108260)
- Layer 35: ` hilabihan`, ` pakig`, ` .`, ` talags`, `滴水` (target ranks: base_value=64:126199, first_product=128:127827, bound_value=119:127999, second_product=238:124760, answer=224:100351)
- Layer 36: ` talags`, ` hilabihan`, `停`, `enclose`, `幽` (target ranks: base_value=64:100070, first_product=128:117426, bound_value=119:115041, second_product=238:94429, answer=224:50879)
- Layer 37: `}<?`, ` hilabihan`, ` Erkännande`, ` licensierad`, `aplenty` (target ranks: base_value=64:126452, first_product=128:126151, bound_value=119:124191, second_product=238:118990, answer=224:103275)
- Layer 38: ` .`, ` Erkännande`, `}<?`, `enclose`, ` nasod` (target ranks: base_value=64:115207, first_product=128:115500, bound_value=119:119138, second_product=238:108953, answer=224:78414)
- Layer 39: ` .`, `}<?`, ` .↵↵`, ` Erkännande`, `�乐` (target ranks: base_value=64:123114, first_product=128:109573, bound_value=119:121977, second_product=238:101035, answer=224:54018)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, ` nasod`, ` filler` (target ranks: base_value=64:70938, first_product=128:52199, bound_value=119:71774, second_product=238:58352, answer=224:6940)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` ,`, `不不` (target ranks: base_value=64:12104, first_product=128:13890, bound_value=119:27264, second_product=238:4614, answer=224:214)

### Filler position 3 (absolute token 798, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125412, first_product=128:121393, bound_value=119:120398, second_product=238:120752, answer=224:120735)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:18941, first_product=128:29086, bound_value=119:28640, second_product=238:32072, answer=224:28607)
- Layer 20: `ait`, `忑`, `ashi`, `能被`, `锁定` (target ranks: base_value=64:7303, first_product=128:47006, bound_value=119:45145, second_product=238:55200, answer=224:24168)
- Layer 30: `s`, ` Su`, `�`, ` SUV`, `su` (target ranks: base_value=64:5582, first_product=128:115775, bound_value=119:111670, second_product=238:126818, answer=224:66089)
- Layer 35: ` su`, ` Su`, ` Vo`, ` SU`, ` vo` (target ranks: base_value=64:2325, first_product=128:105810, bound_value=119:100343, second_product=238:121914, answer=224:53510)
- Layer 36: `calcul`, ` su`, ` Vo`, ` Wil`, `计算的` (target ranks: base_value=64:5470, first_product=128:94614, bound_value=119:88937, second_product=238:118217, answer=224:50181)
- Layer 37: ` su`, `}<?`, `calcul`, `计算方法`, `进行计算` (target ranks: base_value=64:17262, first_product=128:115047, bound_value=119:116305, second_product=238:126683, answer=224:75689)
- Layer 38: `}<?`, `oses`, ` su`, ` bases`, `基底` (target ranks: base_value=64:33886, first_product=128:123036, bound_value=119:114445, second_product=238:123746, answer=224:97275)
- Layer 39: ` su`, `ked`, `oses`, ` sublim`, `无言` (target ranks: base_value=64:60451, first_product=128:125945, bound_value=119:121404, second_product=238:121959, answer=224:113128)
- Layer 40: ` ni`, ` su`, `nipp`, `k`, ` Nij` (target ranks: base_value=64:15780, first_product=128:99345, bound_value=119:98281, second_product=238:113983, answer=224:56461)
- Layer 41: ` .`, `wo`, ` given`, `<｜end▁of▁sentence｜>`, ` ,` (target ranks: base_value=64:14458, first_product=128:57692, bound_value=119:77474, second_product=238:83352, answer=224:34641)

### Filler position 4 (absolute token 799, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:126048, first_product=128:123012, bound_value=119:121193, second_product=238:122233, answer=224:122020)
- Layer 10: ` Walker`, `ait`, `锁定`, `Walker`, `挪` (target ranks: base_value=64:14287, first_product=128:23918, bound_value=119:22813, second_product=238:24650, answer=224:23954)
- Layer 20: `拆`, `幽`, `能被`, `ait`, `足` (target ranks: base_value=64:6295, first_product=128:52132, bound_value=119:45945, second_product=238:68792, answer=224:21410)
- Layer 30: ` SUV`, `SUV`, ` Su`, ` su`, ` SU` (target ranks: base_value=64:7, first_product=128:67952, bound_value=119:117434, second_product=238:125915, answer=224:51997)
- Layer 35: ` SUV`, ` Su`, `SUV`, ` su`, ` SU` (target ranks: base_value=64:7, first_product=128:64162, bound_value=119:97350, second_product=238:113330, answer=224:27991)
- Layer 36: ` SUV`, ` su`, ` Su`, `SUV`, ` SU` (target ranks: base_value=64:10, first_product=128:46278, bound_value=119:79901, second_product=238:99584, answer=224:28201)
- Layer 37: ` su`, ` SUV`, ` Su`, `SUV`, `gev` (target ranks: base_value=64:16, first_product=128:59121, bound_value=119:91804, second_product=238:119291, answer=224:42937)
- Layer 38: ` su`, ` SUV`, `gev`, ` Su`, `SUV` (target ranks: base_value=64:158, first_product=128:97836, bound_value=119:92249, second_product=238:116412, answer=224:73023)
- Layer 39: ` su`, ` Su`, ` SUV`, ` Sue`, ` sublim` (target ranks: base_value=64:42275, first_product=128:115900, bound_value=119:110575, second_product=238:109431, answer=224:73681)
- Layer 40: ` su`, ` wo`, `wo`, ` s`, `wof` (target ranks: base_value=64:44254, first_product=128:83881, bound_value=119:50917, second_product=238:59029, answer=224:13409)
- Layer 41: ` su`, ` wo`, ` .`, `wo`, ` woo` (target ranks: base_value=64:62735, first_product=128:60872, bound_value=119:51137, second_product=238:67698, answer=224:11902)

### Filler position 5 (absolute token 800, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125624, first_product=128:122936, bound_value=119:120523, second_product=238:122082, answer=224:121762)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:15747, first_product=128:26103, bound_value=119:25259, second_product=238:27467, answer=224:25847)
- Layer 20: `挪`, `幽`, `锁定`, ` wig`, `ait` (target ranks: base_value=64:15145, first_product=128:36053, bound_value=119:39646, second_product=238:46295, answer=224:24779)
- Layer 30: ` tap`, `Tap`, `tap`, ` Tap`, ` rationality` (target ranks: base_value=64:91290, first_product=128:89743, bound_value=119:110070, second_product=238:103932, answer=224:58563)
- Layer 35: ` tap`, ` rip`, ` Niagara`, `Tap`, ` Tap` (target ranks: base_value=64:78988, first_product=128:100880, bound_value=119:104743, second_product=238:115005, answer=224:46164)
- Layer 36: ` rip`, ` tap`, ` dynam`, ` Zad`, `动态` (target ranks: base_value=64:62833, first_product=128:77561, bound_value=119:86535, second_product=238:103922, answer=224:28043)
- Layer 37: `hemer`, `打磨`, ` dynam`, `�`, ` rip` (target ranks: base_value=64:96736, first_product=128:100869, bound_value=119:103271, second_product=238:119935, answer=224:46189)
- Layer 38: `hemer`, `�`, `打磨`, `aharan`, `东海` (target ranks: base_value=64:107175, first_product=128:112632, bound_value=119:113264, second_product=238:120061, answer=224:59813)
- Layer 39: `hemer`, ` talags`, `�`, `东海`, `-ulo` (target ranks: base_value=64:78311, first_product=128:120371, bound_value=119:125486, second_product=238:126005, answer=224:88962)
- Layer 40: ` talags`, `pon`, ` nasod`, ` Nij`, `acl` (target ranks: base_value=64:42782, first_product=128:110541, bound_value=119:108703, second_product=238:124962, answer=224:50654)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, `叮`, ` careful` (target ranks: base_value=64:17435, first_product=128:45033, bound_value=119:71917, second_product=238:98198, answer=224:21116)

### Filler position 6 (absolute token 801, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `-ulo`, `aplenty`, `�乐` (target ranks: base_value=64:125218, first_product=128:122701, bound_value=119:120084, second_product=238:121827, answer=224:121448)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:13209, first_product=128:22418, bound_value=119:22193, second_product=238:24184, answer=224:23017)
- Layer 20: `答案`, ` answer`, `暂无`, `参考答案`, `Answered` (target ranks: base_value=64:58722, first_product=128:82208, bound_value=119:109765, second_product=238:114703, answer=224:49122)
- Layer 30: `高明`, `推算`, `算出`, `计算的`, ` step` (target ranks: base_value=64:59254, first_product=128:51498, bound_value=119:44293, second_product=238:115381, answer=224:27720)
- Layer 35: ` Tw`, `acks`, ` step`, `高明`, `第一步` (target ranks: base_value=64:23957, first_product=128:36917, bound_value=119:44073, second_product=238:63630, answer=224:12872)
- Layer 36: ` Tw`, ` tw`, `Tw`, ` step`, `acks` (target ranks: base_value=64:36563, first_product=128:38148, bound_value=119:40980, second_product=238:69615, answer=224:15150)
- Layer 37: ` Tw`, ` step`, ` tw`, ` Step`, `acks` (target ranks: base_value=64:44341, first_product=128:58333, bound_value=119:67572, second_product=238:97960, answer=224:27958)
- Layer 38: ` Tw`, `tw`, ` tw`, `Tw`, ` Calculators` (target ranks: base_value=64:61463, first_product=128:81167, bound_value=119:84458, second_product=238:102923, answer=224:31487)
- Layer 39: ` nasod`, `klar`, `替换`, ` Fif`, ` Rutherford` (target ranks: base_value=64:85839, first_product=128:111210, bound_value=119:126847, second_product=238:125541, answer=224:117718)
- Layer 40: ` nasod`, `klar`, `ket`, `<｜begin▁of▁sentence｜>`, `省略` (target ranks: base_value=64:52718, first_product=128:101617, bound_value=119:124072, second_product=238:124244, answer=224:118044)
- Layer 41: `<｜begin▁of▁file｜>`, `印书馆`, `那两个`, ` fourteenth`, `ucay` (target ranks: base_value=64:102841, first_product=128:118383, bound_value=119:127203, second_product=238:125996, answer=224:122567)

### Filler position 7 (absolute token 802, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124982, first_product=128:122358, bound_value=119:119646, second_product=238:121490, answer=224:121006)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12828, first_product=128:22203, bound_value=119:21687, second_product=238:24545, answer=224:22686)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, `Walker` (target ranks: base_value=64:10690, first_product=128:36022, bound_value=119:40150, second_product=238:58991, answer=224:26740)
- Layer 30: `算出`, `calcul`, `第一步`, `计算的`, `计算` (target ranks: base_value=64:15002, first_product=128:92132, bound_value=119:92617, second_product=238:123828, answer=224:64788)
- Layer 35: ` Tw`, `calcul`, `第一步`, `Tw`, ` calculate` (target ranks: base_value=64:8174, first_product=128:65135, bound_value=119:68278, second_product=238:100833, answer=224:30496)
- Layer 36: `calcul`, ` calculate`, `计算的`, `第一步`, ` calculations` (target ranks: base_value=64:12866, first_product=128:59029, bound_value=119:59322, second_product=238:98313, answer=224:26894)
- Layer 37: `calcul`, ` calculations`, `计算的`, `计算`, `comput` (target ranks: base_value=64:28580, first_product=128:81427, bound_value=119:83599, second_product=238:120346, answer=224:47416)
- Layer 38: `calcul`, ` cál`, ` calculations`, `计算的`, `计算` (target ranks: base_value=64:52328, first_product=128:110584, bound_value=119:96202, second_product=238:124899, answer=224:82665)
- Layer 39: ` duc`, `金黄`, `声响`, `东海`, ` Noruwega` (target ranks: base_value=64:62761, first_product=128:108044, bound_value=119:112822, second_product=238:123201, answer=224:106333)
- Layer 40: `duc`, ` su`, ` duc`, ` dup`, `留存` (target ranks: base_value=64:26391, first_product=128:87613, bound_value=119:93813, second_product=238:119360, answer=224:94066)
- Layer 41: `鹉`, ` sublim`, ` waterfall`, `出不穷`, `šk` (target ranks: base_value=64:31120, first_product=128:57715, bound_value=119:92227, second_product=238:103999, answer=224:75513)

### Filler position 8 (absolute token 803, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125065, first_product=128:122249, bound_value=119:119737, second_product=238:121375, answer=224:120942)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11619, first_product=128:22012, bound_value=119:21786, second_product=238:24795, answer=224:23201)
- Layer 20: `ait`, ` Walker`, `挪`, `锁定`, `Walker` (target ranks: base_value=64:8009, first_product=128:31261, bound_value=119:33390, second_product=238:51735, answer=224:25920)
- Layer 30: ` Ni`, `Ni`, ` ni`, ` Niagara`, ` Su` (target ranks: base_value=64:13095, first_product=128:111692, bound_value=119:97562, second_product=238:127720, answer=224:106359)
- Layer 35: ` ni`, ` SU`, ` Su`, ` Ni`, `ni` (target ranks: base_value=64:9661, first_product=128:94475, bound_value=119:79488, second_product=238:120849, answer=224:81264)
- Layer 36: ` ni`, ` SU`, ` su`, ` Su`, `ni` (target ranks: base_value=64:9854, first_product=128:78925, bound_value=119:57313, second_product=238:115842, answer=224:68509)
- Layer 37: ` ni`, ` Ni`, ` su`, `Ni`, ` Su` (target ranks: base_value=64:36470, first_product=128:98672, bound_value=119:64675, second_product=238:125761, answer=224:96960)
- Layer 38: ` su`, ` Nij`, ` Ni`, ` ni`, `}<?` (target ranks: base_value=64:57567, first_product=128:114353, bound_value=119:58598, second_product=238:125604, answer=224:109601)
- Layer 39: ` Nij`, ` Ni`, ` Su`, ` su`, ` NI` (target ranks: base_value=64:83800, first_product=128:119203, bound_value=119:87396, second_product=238:126900, answer=224:119099)
- Layer 40: ` ni`, ` Ni`, `ni`, ` su`, ` NI` (target ranks: base_value=64:35315, first_product=128:78871, bound_value=119:59271, second_product=238:120920, answer=224:103782)
- Layer 41: ` ni`, ` su`, ` .`, `留存`, ` waterfall` (target ranks: base_value=64:29098, first_product=128:43666, bound_value=119:47404, second_product=238:98377, answer=224:82677)

### Filler position 9 (absolute token 804, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125024, first_product=128:122368, bound_value=119:119842, second_product=238:121587, answer=224:120973)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, `挪` (target ranks: base_value=64:11837, first_product=128:22995, bound_value=119:22198, second_product=238:25597, answer=224:23949)
- Layer 20: `ait`, `锁定`, ` Walker`, `挪`, ` cheer` (target ranks: base_value=64:9099, first_product=128:32565, bound_value=119:30154, second_product=238:52828, answer=224:26656)
- Layer 30: ` Ni`, `Ni`, ` ni`, ` Niagara`, ` NI` (target ranks: base_value=64:17479, first_product=128:97122, bound_value=119:93473, second_product=238:128501, answer=224:104886)
- Layer 35: ` Ni`, ` ni`, `Ni`, ` NI`, `ni` (target ranks: base_value=64:10929, first_product=128:82942, bound_value=119:84614, second_product=238:124656, answer=224:76302)
- Layer 36: ` Ni`, ` ni`, ` NI`, `Ni`, `ni` (target ranks: base_value=64:28265, first_product=128:79644, bound_value=119:81908, second_product=238:122671, answer=224:59925)
- Layer 37: ` Ni`, ` NI`, ` ni`, `Ni`, ` Nij` (target ranks: base_value=64:73509, first_product=128:97496, bound_value=119:92511, second_product=238:124216, answer=224:82232)
- Layer 38: ` Ni`, `}<?`, ` NI`, ` Nij`, ` ni` (target ranks: base_value=64:76462, first_product=128:102515, bound_value=119:95909, second_product=238:121153, answer=224:88767)
- Layer 39: ` Ni`, ` Nij`, ` NI`, `}<?`, `Ni` (target ranks: base_value=64:78817, first_product=128:95304, bound_value=119:111899, second_product=238:124678, answer=224:110220)
- Layer 40: ` ni`, `ni`, `acl`, ` Nij`, `nipp` (target ranks: base_value=64:26598, first_product=128:77097, bound_value=119:90192, second_product=238:125756, answer=224:105874)
- Layer 41: `叮`, ` .`, ` ni`, ` twist`, `毕竟` (target ranks: base_value=64:16925, first_product=128:40966, bound_value=119:61150, second_product=238:111675, answer=224:84328)

### Filler position 10 (absolute token 805, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124900, first_product=128:122420, bound_value=119:119855, second_product=238:121711, answer=224:121097)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11651, first_product=128:22411, bound_value=119:21611, second_product=238:24907, answer=224:23827)
- Layer 20: `能被`, ` Walker`, `ait`, `Walker`, ` LS` (target ranks: base_value=64:3335, first_product=128:23216, bound_value=119:25531, second_product=238:37103, answer=224:17745)
- Layer 30: `116`, `119`, `114`, `59`, `66` (target ranks: base_value=64:168, first_product=128:13459, bound_value=119:2, second_product=238:140, answer=224:398)
- Layer 35: `238`, `237`, `236`, `239`, `235` (target ranks: base_value=64:30323, first_product=128:6215, bound_value=119:332, second_product=238:1, answer=224:83)
- Layer 36: `238`, `228`, `226`, `224`, `225` (target ranks: base_value=64:85604, first_product=128:362, bound_value=119:8981, second_product=238:1, answer=224:4)
- Layer 37: `238`, `228`, ` interpreters`, `226`, `ucl` (target ranks: base_value=64:110073, first_product=128:1142, bound_value=119:10339, second_product=238:1, answer=224:10)
- Layer 38: `224`, `238`, `二十四`, `223`, `225` (target ranks: base_value=64:88000, first_product=128:17347, bound_value=119:19311, second_product=238:2, answer=224:1)
- Layer 39: `224`, `<｜place▁holder▁no▁176｜>`, `124`, ` Didžiulis`, `洪荒` (target ranks: base_value=64:114685, first_product=128:108096, bound_value=119:77695, second_product=238:408, answer=224:1)
- Layer 40: ` talags`, `ekak`, `实在`, `贤`, `224` (target ranks: base_value=64:110785, first_product=128:115067, bound_value=119:87135, second_product=238:8204, answer=224:5)
- Layer 41: `那两个`, ` nuest`, `茶馆`, `ekak`, `也别` (target ranks: base_value=64:96169, first_product=128:105156, bound_value=119:85906, second_product=238:9242, answer=224:21)

### Filler position 11 (absolute token 806, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125006, first_product=128:122623, bound_value=119:120064, second_product=238:122123, answer=224:121395)
- Layer 10: ` Walker`, `锁定`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11462, first_product=128:22913, bound_value=119:21727, second_product=238:25252, answer=224:24162)
- Layer 20: ` smile`, `锁定`, `cape`, `ait`, `幽` (target ranks: base_value=64:4931, first_product=128:24877, bound_value=119:27886, second_product=238:33503, answer=224:15667)
- Layer 30: ` glacier`, ` smile`, ` dripping`, `slide`, `54` (target ranks: base_value=64:97, first_product=128:17642, bound_value=119:1218, second_product=238:4756, answer=224:357)
- Layer 35: `238`, `228`, `224`, `216`, `236` (target ranks: base_value=64:1594, first_product=128:11696, bound_value=119:3340, second_product=238:1, answer=224:3)
- Layer 36: `224`, `228`, `216`, `222`, `226` (target ranks: base_value=64:7673, first_product=128:3574, bound_value=119:7522, second_product=238:11, answer=224:1)
- Layer 37: `224`, `228`, `216`, `把孩子`, `ocyst` (target ranks: base_value=64:42232, first_product=128:8985, bound_value=119:17079, second_product=238:23, answer=224:1)
- Layer 38: `224`, `216`, `polar`, `把孩子`, `殿堂` (target ranks: base_value=64:78636, first_product=128:48216, bound_value=119:58243, second_product=238:283, answer=224:1)
- Layer 39: `}<?`, `tanle`, `-ulo`, `224`, `本题分析` (target ranks: base_value=64:115305, first_product=128:113413, bound_value=119:110893, second_product=238:6827, answer=224:4)
- Layer 40: ` talags`, `enclose`, ` fountain`, `实在`, ` recogn` (target ranks: base_value=64:116027, first_product=128:105140, bound_value=119:107905, second_product=238:13309, answer=224:10)
- Layer 41: `��`, `相比之下`, `有的时候`, ` subter`, `因为这些` (target ranks: base_value=64:86631, first_product=128:75188, bound_value=119:100036, second_product=238:6994, answer=224:16)

### Filler position 12 (absolute token 807, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124854, first_product=128:122465, bound_value=119:119913, second_product=238:121940, answer=224:121244)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11429, first_product=128:22703, bound_value=119:22073, second_product=238:25310, answer=224:24132)
- Layer 20: `锁定`, `ait`, ` smile`, `鞍`, `挪` (target ranks: base_value=64:4247, first_product=128:16405, bound_value=119:26481, second_product=238:32042, answer=224:16555)
- Layer 30: `鞍`, ` smile`, ` Cogn`, `Tap`, `匹配` (target ranks: base_value=64:510, first_product=128:15957, bound_value=119:3574, second_product=238:13229, answer=224:3588)
- Layer 35: `匹配`, `acin`, `鞍`, ` Cogn`, ` matching` (target ranks: base_value=64:2672, first_product=128:39804, bound_value=119:12718, second_product=238:7316, answer=224:1025)
- Layer 36: `acin`, `特`, `ilig`, `enclose`, `往外` (target ranks: base_value=64:5879, first_product=128:44379, bound_value=119:15546, second_product=238:7736, answer=224:423)
- Layer 37: `ocyst`, `殿堂`, `院内`, `}<?`, `Quintal` (target ranks: base_value=64:49394, first_product=128:73652, bound_value=119:34714, second_product=238:9316, answer=224:1859)
- Layer 38: `ocyst`, `}<?`, `殿堂`, `院内`, `?datasetId` (target ranks: base_value=64:78172, first_product=128:83054, bound_value=119:74459, second_product=238:34354, answer=224:3108)
- Layer 39: `}<?`, `ocyst`, `ozygous`, `殿堂`, `东海` (target ranks: base_value=64:111390, first_product=128:123357, bound_value=119:113264, second_product=238:65741, answer=224:5987)
- Layer 40: `enclose`, `下沉`, `}<?`, `acular`, ` recogn` (target ranks: base_value=64:93185, first_product=128:109749, bound_value=119:94157, second_product=238:63908, answer=224:1005)
- Layer 41: ` .`, `到这里`, ` repeatedly`, ` `, `特` (target ranks: base_value=64:59361, first_product=128:83169, bound_value=119:74118, second_product=238:29370, answer=224:591)

### Filler position 13 (absolute token 808, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:124930, first_product=128:122594, bound_value=119:120084, second_product=238:122088, answer=224:121368)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11234, first_product=128:22310, bound_value=119:22018, second_product=238:24894, answer=224:23658)
- Layer 20: `ait`, `锁定`, ` Walker`, `鞍`, ` smile` (target ranks: base_value=64:13224, first_product=128:31329, bound_value=119:43284, second_product=238:45157, answer=224:24388)
- Layer 30: ` tap`, `Tap`, `鞍`, `tap`, ` Tap` (target ranks: base_value=64:17869, first_product=128:44333, bound_value=119:97059, second_product=238:81038, answer=224:48109)
- Layer 35: ` tap`, `Tap`, ` Tap`, `tap`, `acin` (target ranks: base_value=64:13290, first_product=128:47477, bound_value=119:82773, second_product=238:91336, answer=224:29102)
- Layer 36: ` tap`, `Tap`, ` Tap`, `acin`, `反复` (target ranks: base_value=64:11234, first_product=128:22387, bound_value=119:53026, second_product=238:66159, answer=224:16098)
- Layer 37: `冰冰`, `不急`, `}<?`, ` prer`, `acons` (target ranks: base_value=64:32363, first_product=128:28798, bound_value=119:69038, second_product=238:104021, answer=224:30071)
- Layer 38: `}<?`, `冰冰`, `不急`, `acons`, `打磨` (target ranks: base_value=64:38810, first_product=128:28895, bound_value=119:66906, second_product=238:102066, answer=224:18696)
- Layer 39: `}<?`, `ocyst`, ` talags`, `铎`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=64:36727, first_product=128:55642, bound_value=119:106384, second_product=238:105851, answer=224:19228)
- Layer 40: ` nasod`, ` .`, ` Erkännande`, `šk`, `冰冰` (target ranks: base_value=64:5958, first_product=128:24259, bound_value=119:72856, second_product=238:87732, answer=224:1184)
- Layer 41: ` .`, ` `, `有下列`, ` .↵↵`, ` because` (target ranks: base_value=64:4968, first_product=128:5017, bound_value=119:44258, second_product=238:27632, answer=224:203)

### Filler position 14 (absolute token 809, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125058, first_product=128:122577, bound_value=119:120154, second_product=238:122046, answer=224:121130)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10562, first_product=128:21868, bound_value=119:21157, second_product=238:24057, answer=224:22742)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `拆` (target ranks: base_value=64:10561, first_product=128:34165, bound_value=119:37493, second_product=238:43154, answer=224:25180)
- Layer 30: `提问`, `询问`, ` question`, ` questions`, `asking` (target ranks: base_value=64:35601, first_product=128:103669, bound_value=119:105466, second_product=238:110912, answer=224:68790)
- Layer 35: `询问`, ` question`, `提问`, `詢問`, `asking` (target ranks: base_value=64:16513, first_product=128:64704, bound_value=119:87376, second_product=238:85247, answer=224:28898)
- Layer 36: `询问`, ` question`, `提问`, `詢問`, `asking` (target ranks: base_value=64:27725, first_product=128:62991, bound_value=119:84644, second_product=238:83031, answer=224:24004)
- Layer 37: ` question`, `提问`, `询问`, `asking`, `.question` (target ranks: base_value=64:55461, first_product=128:78760, bound_value=119:99443, second_product=238:100400, answer=224:36436)
- Layer 38: `}<?`, `asking`, `殿堂`, `追问`, `.question` (target ranks: base_value=64:69869, first_product=128:95652, bound_value=119:111056, second_product=238:104352, answer=224:55484)
- Layer 39: `}<?`, `殿堂`, `<｜begin▁of▁sentence｜>`, `树叶`, `acons` (target ranks: base_value=64:85836, first_product=128:91763, bound_value=119:116014, second_product=238:115797, answer=224:90705)
- Layer 40: `šk`, `asking`, `殿堂`, `acl`, `下沉` (target ranks: base_value=64:42657, first_product=128:70045, bound_value=119:102893, second_product=238:115732, answer=224:85182)
- Layer 41: ` .`, `šk`, ` wo`, ` `, `装作` (target ranks: base_value=64:17636, first_product=128:25633, bound_value=119:78554, second_product=238:82910, answer=224:41218)

### Filler position 15 (absolute token 810, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125207, first_product=128:122801, bound_value=119:120430, second_product=238:122222, answer=224:121136)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10770, first_product=128:21989, bound_value=119:21145, second_product=238:24137, answer=224:22244)
- Layer 20: `ait`, `能被`, `锁定`, ` Walker`, ` smile` (target ranks: base_value=64:4412, first_product=128:25814, bound_value=119:25025, second_product=238:39706, answer=224:16975)
- Layer 30: ` expecting`, `鞍`, `幽`, ` Ries`, ` dy` (target ranks: base_value=64:182, first_product=128:9242, bound_value=119:197, second_product=238:16322, answer=224:5741)
- Layer 35: `238`, `119`, `239`, `Wil`, `尾` (target ranks: base_value=64:8542, first_product=128:50367, bound_value=119:2, second_product=238:1, answer=224:2811)
- Layer 36: `238`, `119`, ` ICM`, ` ICD`, `239` (target ranks: base_value=64:68705, first_product=128:56224, bound_value=119:2, second_product=238:1, answer=224:3721)
- Layer 37: `238`, `119`, ` ICM`, ` ICD`, ` LCM` (target ranks: base_value=64:106644, first_product=128:84755, bound_value=119:2, second_product=238:1, answer=224:19918)
- Layer 38: `238`, `119`, ` ICM`, ` ICD`, ` UIC` (target ranks: base_value=64:117649, first_product=128:112733, bound_value=119:2, second_product=238:1, answer=224:25804)
- Layer 39: `238`, `119`, ` ICM`, ` LCM`, `script` (target ranks: base_value=64:61856, first_product=128:107248, bound_value=119:2, second_product=238:1, answer=224:32160)
- Layer 40: `俯`, `238`, `scribe`, `提示`, ` su` (target ranks: base_value=64:50400, first_product=128:99531, bound_value=119:11, second_product=238:2, answer=224:5311)
- Layer 41: ` .`, `238`, `提示`, `温馨提示`, `因为这些` (target ranks: base_value=64:51367, first_product=128:83476, bound_value=119:50, second_product=238:2, answer=224:7705)

### Filler position 16 (absolute token 811, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125202, first_product=128:122817, bound_value=119:120394, second_product=238:122267, answer=224:121182)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10928, first_product=128:21772, bound_value=119:20851, second_product=238:23619, answer=224:21663)
- Layer 20: `ait`, `锁定`, `幽`, `能被`, ` Walker` (target ranks: base_value=64:5808, first_product=128:31267, bound_value=119:31276, second_product=238:39222, answer=224:19898)
- Layer 30: ` VO`, ` Vo`, ` vo`, `VO`, `Vo` (target ranks: base_value=64:4535, first_product=128:95972, bound_value=119:78717, second_product=238:110956, answer=224:62630)
- Layer 35: ` VO`, ` Vo`, ` vo`, `Vo`, `VO` (target ranks: base_value=64:3710, first_product=128:77165, bound_value=119:63126, second_product=238:80814, answer=224:33644)
- Layer 36: ` Vo`, ` VO`, ` vo`, `Vo`, `VO` (target ranks: base_value=64:6286, first_product=128:74979, bound_value=119:44473, second_product=238:78667, answer=224:26472)
- Layer 37: ` Vo`, ` vo`, ` VO`, ` voz`, `}<?` (target ranks: base_value=64:19940, first_product=128:94454, bound_value=119:60766, second_product=238:100045, answer=224:48251)
- Layer 38: ` vo`, ` Vo`, ` voz`, ` VO`, `}<?` (target ranks: base_value=64:34867, first_product=128:107007, bound_value=119:53084, second_product=238:100073, answer=224:69213)
- Layer 39: ` vo`, `}<?`, ` Vo`, ` VO`, ` voz` (target ranks: base_value=64:63822, first_product=128:105421, bound_value=119:76085, second_product=238:97869, answer=224:74374)
- Layer 40: ` w`, ` su`, `实在`, `俯`, `osit` (target ranks: base_value=64:46325, first_product=128:57371, bound_value=119:45540, second_product=238:57478, answer=224:14264)
- Layer 41: `实在`, `转载请`, `鹉`, ` .`, `那两个` (target ranks: base_value=64:17225, first_product=128:22678, bound_value=119:16366, second_product=238:20557, answer=224:2905)

### Filler position 17 (absolute token 812, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125263, first_product=128:123010, bound_value=119:120602, second_product=238:122624, answer=224:121455)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12227, first_product=128:22912, bound_value=119:22136, second_product=238:25356, answer=224:23524)
- Layer 20: `能被`, ` smile`, ` Walker`, `距`, `锁定` (target ranks: base_value=64:8369, first_product=128:29473, bound_value=119:29749, second_product=238:38676, answer=224:13575)
- Layer 30: `幽`, `鞍`, ` iceberg`, ` Ries`, `adal` (target ranks: base_value=64:185, first_product=128:4345, bound_value=119:122, second_product=238:19836, answer=224:2090)
- Layer 35: `119`, ` spider`, `蜘蛛`, ` Spider`, `十九` (target ranks: base_value=64:1473, first_product=128:38960, bound_value=119:1, second_product=238:9509, answer=224:16691)
- Layer 36: `119`, `防火`, `幽冥`, `蜘蛛`, `大火` (target ranks: base_value=64:12393, first_product=128:54483, bound_value=119:1, second_product=238:1630, answer=224:28363)
- Layer 37: `119`, `防火`, `幽冥`, `出家`, `香油` (target ranks: base_value=64:58129, first_product=128:83786, bound_value=119:1, second_product=238:12144, answer=224:86013)
- Layer 38: `119`, ` ICD`, `院长`, `防火`, `出家` (target ranks: base_value=64:74853, first_product=128:97786, bound_value=119:1, second_product=238:27864, answer=224:97089)
- Layer 39: `119`, `鱼的`, `芦`, `acons`, ` ICM` (target ranks: base_value=64:64892, first_product=128:57260, bound_value=119:1, second_product=238:4295, answer=224:29564)
- Layer 40: `119`, `俯`, `duc`, `pañ`, `scribe` (target ranks: base_value=64:73825, first_product=128:64983, bound_value=119:1, second_product=238:17381, answer=224:4446)
- Layer 41: ` .`, `那两个`, ` substitute`, ` without`, `Explanation` (target ranks: base_value=64:76934, first_product=128:58323, bound_value=119:36, second_product=238:8200, answer=224:8406)

### Filler position 18 (absolute token 813, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `-ulo`, `�乐` (target ranks: base_value=64:125617, first_product=128:123628, bound_value=119:121244, second_product=238:123337, answer=224:122029)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11286, first_product=128:22377, bound_value=119:21840, second_product=238:25561, answer=224:23118)
- Layer 20: ` Walker`, `ait`, `锁定`, `Walker`, `忑` (target ranks: base_value=64:15699, first_product=128:36686, bound_value=119:36150, second_product=238:58972, answer=224:26368)
- Layer 30: ` SUV`, ` Su`, `SUV`, ` SU`, `鞍` (target ranks: base_value=64:6312, first_product=128:110025, bound_value=119:108642, second_product=238:125744, answer=224:87804)
- Layer 35: ` Su`, ` SUV`, ` SU`, `SUV`, `鞍` (target ranks: base_value=64:2790, first_product=128:96683, bound_value=119:86776, second_product=238:117997, answer=224:65727)
- Layer 36: ` Su`, ` SUV`, ` SU`, ` riv`, ` su` (target ranks: base_value=64:4665, first_product=128:73677, bound_value=119:56282, second_product=238:102279, answer=224:48580)
- Layer 37: `}<?`, ` Su`, ` su`, ` SUV`, `不加` (target ranks: base_value=64:26686, first_product=128:99341, bound_value=119:61223, second_product=238:122584, answer=224:77564)
- Layer 38: `}<?`, ` siv`, ` sublim`, ` Nij`, ` su` (target ranks: base_value=64:37234, first_product=128:111457, bound_value=119:62430, second_product=238:110776, answer=224:84110)
- Layer 39: `}<?`, ` sublim`, `ked`, `�`, ` Nij` (target ranks: base_value=64:66659, first_product=128:106174, bound_value=119:83703, second_product=238:103074, answer=224:67843)
- Layer 40: ` su`, `殿堂`, `ked`, `acular`, ` Nij` (target ranks: base_value=64:24652, first_product=128:53213, bound_value=119:18248, second_product=238:74412, answer=224:9178)
- Layer 41: ` .`, `acular`, `zij`, ` Nij`, `那两个` (target ranks: base_value=64:38327, first_product=128:62779, bound_value=119:33979, second_product=238:72670, answer=224:12204)

### Filler position 19 (absolute token 814, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125644, first_product=128:123718, bound_value=119:121368, second_product=238:123415, answer=224:121991)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10782, first_product=128:21727, bound_value=119:20949, second_product=238:25645, answer=224:22125)
- Layer 20: `ait`, `忑`, `锁定`, `能被`, ` engaging` (target ranks: base_value=64:11675, first_product=128:48141, bound_value=119:39558, second_product=238:70066, answer=224:31669)
- Layer 30: `acos`, ` rip`, ` Zad`, ` zad`, ` consum` (target ranks: base_value=64:31855, first_product=128:125964, bound_value=119:118948, second_product=238:127840, answer=224:104781)
- Layer 35: ` tap`, ` zad`, ` Wil`, `Tap`, `Wil` (target ranks: base_value=64:32999, first_product=128:117861, bound_value=119:107359, second_product=238:124247, answer=224:69758)
- Layer 36: ` zad`, ` drip`, ` Zad`, `zim`, ` rip` (target ranks: base_value=64:29325, first_product=128:110342, bound_value=119:90506, second_product=238:119484, answer=224:58493)
- Layer 37: ` Zed`, `zim`, `zat`, `amol`, `}<?` (target ranks: base_value=64:73519, first_product=128:120694, bound_value=119:108178, second_product=238:125507, answer=224:86008)
- Layer 38: `zat`, `}<?`, ` Zed`, `apper`, ` Pax` (target ranks: base_value=64:78581, first_product=128:122020, bound_value=119:87500, second_product=238:125642, answer=224:89526)
- Layer 39: `zat`, ` Zed`, `zel`, `ked`, `zal` (target ranks: base_value=64:70020, first_product=128:117605, bound_value=119:84763, second_product=238:119032, answer=224:55536)
- Layer 40: `zel`, `zat`, `y`, ` fum`, `zij` (target ranks: base_value=64:41640, first_product=128:91930, bound_value=119:76699, second_product=238:117471, answer=224:23349)
- Layer 41: `zel`, ` fum`, `zij`, `yb`, `zat` (target ranks: base_value=64:13999, first_product=128:22612, bound_value=119:26411, second_product=238:58685, answer=224:1824)

### Filler position 20 (absolute token 815, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125633, first_product=128:123650, bound_value=119:121369, second_product=238:123348, answer=224:121999)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10154, first_product=128:20745, bound_value=119:19984, second_product=238:24837, answer=224:21125)
- Layer 20: `ait`, `锁定`, ` Walker`, `Walker`, `拆` (target ranks: base_value=64:9362, first_product=128:40985, bound_value=119:44738, second_product=238:61419, answer=224:25014)
- Layer 30: `acos`, ` tap`, `acin`, ` labor`, ` ES` (target ranks: base_value=64:48995, first_product=128:105134, bound_value=119:119965, second_product=238:116801, answer=224:73485)
- Layer 35: ` tap`, ` repetition`, ` zad`, ` drip`, ` Zad` (target ranks: base_value=64:30685, first_product=128:90297, bound_value=119:103213, second_product=238:102001, answer=224:42901)
- Layer 36: ` Zad`, ` zad`, ` Tw`, ` tap`, ` drip` (target ranks: base_value=64:28762, first_product=128:68479, bound_value=119:92499, second_product=238:93475, answer=224:37389)
- Layer 37: `}<?`, ` Zad`, `打磨`, `acos`, `dividers` (target ranks: base_value=64:68627, first_product=128:78703, bound_value=119:104359, second_product=238:111407, answer=224:55957)
- Layer 38: `}<?`, `打磨`, `dividers`, `zat`, ` Zad` (target ranks: base_value=64:78398, first_product=128:102027, bound_value=119:115171, second_product=238:116772, answer=224:75727)
- Layer 39: `}<?`, ` talags`, `ozygous`, `打磨`, `dividers` (target ranks: base_value=64:72474, first_product=128:99605, bound_value=119:115037, second_product=238:115524, answer=224:72808)
- Layer 40: ` talags`, `acl`, `zij`, `下沉`, `冰冰` (target ranks: base_value=64:22772, first_product=128:67612, bound_value=119:83508, second_product=238:106089, answer=224:22453)
- Layer 41: ` .`, ` `, `Question`, ` Question`, `鹉` (target ranks: base_value=64:3792, first_product=128:9441, bound_value=119:27003, second_product=238:15912, answer=224:1414)

### Filler position 21 (absolute token 816, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126082, first_product=128:124160, bound_value=119:121969, second_product=238:123761, answer=224:122274)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9685, first_product=128:20551, bound_value=119:19623, second_product=238:23482, answer=224:20735)
- Layer 20: `能被`, `ait`, ` Walker`, `锁定`, `拆` (target ranks: base_value=64:6923, first_product=128:38725, bound_value=119:35789, second_product=238:36668, answer=224:14517)
- Layer 30: `粥`, `acos`, `平行`, `atar`, ` consuming` (target ranks: base_value=64:105, first_product=128:27203, bound_value=119:1034, second_product=238:4033, answer=224:465)
- Layer 35: `itetsdata`, `烟`, ` Sm`, `95`, `akah` (target ranks: base_value=64:586, first_product=128:56108, bound_value=119:10117, second_product=238:45, answer=224:514)
- Layer 36: `95`, `85`, `105`, `adal`, `肺` (target ranks: base_value=64:9089, first_product=128:71456, bound_value=119:22735, second_product=238:503, answer=224:982)
- Layer 37: ` soft`, ` Soft`, ` ICE`, `oze`, `azan` (target ranks: base_value=64:45974, first_product=128:90462, bound_value=119:25790, second_product=238:1247, answer=224:2750)
- Layer 38: `205`, `225`, ` soft`, `oze`, `95` (target ranks: base_value=64:80809, first_product=128:110597, bound_value=119:48177, second_product=238:6205, answer=224:1962)
- Layer 39: ` dirty`, `205`, `智慧的`, ` Nij`, `爸爸妈妈` (target ranks: base_value=64:87187, first_product=128:112861, bound_value=119:89535, second_product=238:18243, answer=224:351)
- Layer 40: `225`, `224`, ` dekameters`, `aira`, ` ICE` (target ranks: base_value=64:85852, first_product=128:103799, bound_value=119:89258, second_product=238:23116, answer=224:2)
- Layer 41: `那两个`, ` .`, `父`, ` dekameters`, `225` (target ranks: base_value=64:66293, first_product=128:68585, bound_value=119:61827, second_product=238:4258, answer=224:9)

### Filler position 22 (absolute token 817, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:125935, first_product=128:124052, bound_value=119:121925, second_product=238:123690, answer=224:122081)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:8997, first_product=128:20262, bound_value=119:19260, second_product=238:22850, answer=224:20706)
- Layer 20: `ait`, ` Walker`, `锁定`, `拆`, `Walker` (target ranks: base_value=64:5891, first_product=128:31133, bound_value=119:29437, second_product=238:37716, answer=224:16607)
- Layer 30: `64`, `分解`, ` expecting`, `atar`, `退出` (target ranks: base_value=64:1, first_product=128:482, bound_value=119:5480, second_product=238:43109, answer=224:4116)
- Layer 35: `64`, `分解`, `119`, `Binary`, ` binary` (target ranks: base_value=64:1, first_product=128:57, bound_value=119:3, second_product=238:70664, answer=224:3755)
- Layer 36: `119`, `退出`, `分解`, ` expectation`, `64` (target ranks: base_value=64:5, first_product=128:253, bound_value=119:1, second_product=238:72155, answer=224:10392)
- Layer 37: `}<?`, `119`, `取了`, ` reper`, `arent` (target ranks: base_value=64:19, first_product=128:622, bound_value=119:2, second_product=238:105564, answer=224:28063)
- Layer 38: `}<?`, `取了`, `119`, `ocyst`, `interpret` (target ranks: base_value=64:326, first_product=128:5348, bound_value=119:3, second_product=238:115396, answer=224:58174)
- Layer 39: `}<?`, `ocyst`, `ounder`, `anic`, `ospheric` (target ranks: base_value=64:2717, first_product=128:3267, bound_value=119:6, second_product=238:44379, answer=224:9879)
- Layer 40: `俯`, `anic`, `119`, ` su`, ` ` (target ranks: base_value=64:11989, first_product=128:6229, bound_value=119:3, second_product=238:6608, answer=224:332)
- Layer 41: ` .`, ` `, `119`, ` su`, `没有被` (target ranks: base_value=64:7460, first_product=128:2956, bound_value=119:3, second_product=238:4375, answer=224:166)

### Filler position 23 (absolute token 818, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126173, first_product=128:124418, bound_value=119:122356, second_product=238:124134, answer=224:122419)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10656, first_product=128:21496, bound_value=119:20589, second_product=238:24255, answer=224:22099)
- Layer 20: ` smile`, `ait`, ` Tears`, ` LS`, `锁定` (target ranks: base_value=64:8941, first_product=128:23827, bound_value=119:24287, second_product=238:30881, answer=224:13513)
- Layer 30: `算出`, `�`, `计算`, ` calculate`, `沃` (target ranks: base_value=64:2804, first_product=128:57146, bound_value=119:61537, second_product=238:102998, answer=224:35898)
- Layer 35: ` Wo`, ` first`, `沃`, ` WO`, `aloh` (target ranks: base_value=64:6976, first_product=128:64607, bound_value=119:59026, second_product=238:92342, answer=224:24762)
- Layer 36: ` first`, `沃`, `�`, ` Wo`, `ikuha` (target ranks: base_value=64:8897, first_product=128:36215, bound_value=119:27388, second_product=238:68007, answer=224:12471)
- Layer 37: `wof`, `}<?`, `radesh`, `坏`, ` doubling` (target ranks: base_value=64:24256, first_product=128:48245, bound_value=119:36538, second_product=238:99680, answer=224:18081)
- Layer 38: `wof`, `}<?`, `东海`, ` Wort`, `取了` (target ranks: base_value=64:53945, first_product=128:96266, bound_value=119:47619, second_product=238:113762, answer=224:43815)
- Layer 39: `wof`, `东海`, `�`, ` Woolf`, `ked` (target ranks: base_value=64:54595, first_product=128:87859, bound_value=119:54524, second_product=238:98262, answer=224:36878)
- Layer 40: ` w`, ` su`, ` first`, `kten`, `wof` (target ranks: base_value=64:7702, first_product=128:16215, bound_value=119:4675, second_product=238:15490, answer=224:862)
- Layer 41: ` .`, ` first`, `wo`, ` wo`, `坏` (target ranks: base_value=64:2420, first_product=128:3152, bound_value=119:1967, second_product=238:3268, answer=224:89)

### Filler position 24 (absolute token 819, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126416, first_product=128:124945, bound_value=119:122965, second_product=238:124570, answer=224:122799)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10350, first_product=128:21102, bound_value=119:20813, second_product=238:23876, answer=224:22751)
- Layer 20: `足`, `ait`, ` smile`, ` LS`, `鞍` (target ranks: base_value=64:11041, first_product=128:29250, bound_value=119:32223, second_product=238:40960, answer=224:20821)
- Layer 30: `省略`, `忽略`, `鞍`, `跳过`, ` tap` (target ranks: base_value=64:2745, first_product=128:37669, bound_value=119:34623, second_product=238:79597, answer=224:19821)
- Layer 35: ` repetition`, `重复`, `忽略`, `cape`, ` var` (target ranks: base_value=64:7083, first_product=128:44299, bound_value=119:51107, second_product=238:77206, answer=224:27070)
- Layer 36: `省略`, `忽略`, `calcul`, `跳过`, ` repeated` (target ranks: base_value=64:11273, first_product=128:33862, bound_value=119:40634, second_product=238:63996, answer=224:15797)
- Layer 37: `不急`, `calcul`, `省略`, ` Skip`, `}<?` (target ranks: base_value=64:43946, first_product=128:61803, bound_value=119:71028, second_product=238:98854, answer=224:33402)
- Layer 38: ` skip`, `不急`, ` Skip`, `}<?`, `跳过` (target ranks: base_value=64:39518, first_product=128:71209, bound_value=119:79587, second_product=238:100611, answer=224:47559)
- Layer 39: `<｜begin▁of▁sentence｜>`, `殿堂`, `pac`, `}<?`, ` medief` (target ranks: base_value=64:32896, first_product=128:62213, bound_value=119:88134, second_product=238:102382, answer=224:59914)
- Layer 40: `殿堂`, `pac`, `acl`, `不急`, `<｜begin▁of▁sentence｜>` (target ranks: base_value=64:11719, first_product=128:45604, bound_value=119:51917, second_product=238:98762, answer=224:36559)
- Layer 41: ` .`, `然而`, `鹃`, ` su`, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:1942, first_product=128:8960, bound_value=119:11562, second_product=238:59365, answer=224:11149)

### Filler position 25 (absolute token 820, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126480, first_product=128:124691, bound_value=119:122746, second_product=238:124206, answer=224:122589)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11762, first_product=128:23064, bound_value=119:22605, second_product=238:25418, answer=224:24529)
- Layer 20: `足`, ` smile`, ` Walker`, `Walker`, `距` (target ranks: base_value=64:9217, first_product=128:23442, bound_value=119:26027, second_product=238:38267, answer=224:10760)
- Layer 30: ` Tw`, `Tw`, `calcul`, `算出`, `计算的` (target ranks: base_value=64:2517, first_product=128:49830, bound_value=119:82395, second_product=238:110943, answer=224:50217)
- Layer 35: ` Tw`, `Tw`, `tw`, `TW`, `.tw` (target ranks: base_value=64:4596, first_product=128:58886, bound_value=119:98724, second_product=238:108434, answer=224:44683)
- Layer 36: ` Tw`, `calcul`, `Tw`, `kä`, `计算的` (target ranks: base_value=64:7080, first_product=128:36318, bound_value=119:74426, second_product=238:88877, answer=224:27156)
- Layer 37: `calcul`, `comput`, ` su`, `不加`, `计算的` (target ranks: base_value=64:35157, first_product=128:75532, bound_value=119:107766, second_product=238:114941, answer=224:66818)
- Layer 38: ` Noruwega`, ` su`, `不加`, ` Duc`, `}<?` (target ranks: base_value=64:40956, first_product=128:95922, bound_value=119:108063, second_product=238:114137, answer=224:79261)
- Layer 39: ` su`, ` Noruwega`, ` duc`, `东海`, ` sublim` (target ranks: base_value=64:53679, first_product=128:81900, bound_value=119:100553, second_product=238:100788, answer=224:64180)
- Layer 40: ` su`, `calcul`, `计算的`, `殿堂`, ` sublim` (target ranks: base_value=64:14631, first_product=128:25868, bound_value=119:50274, second_product=238:65772, answer=224:20593)
- Layer 41: ` wo`, `wo`, ` su`, `步骤如下`, `zij` (target ranks: base_value=64:12437, first_product=128:15905, bound_value=119:40195, second_product=238:60755, answer=224:15679)

### Filler position 26 (absolute token 821, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126670, first_product=128:125027, bound_value=119:123164, second_product=238:124556, answer=224:122844)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10923, first_product=128:22171, bound_value=119:21098, second_product=238:24438, answer=224:22223)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, `距` (target ranks: base_value=64:8544, first_product=128:29252, bound_value=119:29051, second_product=238:38925, answer=224:17996)
- Layer 30: ` SUV`, ` SU`, `SUV`, ` riv`, `鞍` (target ranks: base_value=64:1743, first_product=128:67474, bound_value=119:79961, second_product=238:97498, answer=224:43507)
- Layer 35: ` SU`, `羊`, ` SUV`, `外商投资`, ` Su` (target ranks: base_value=64:860, first_product=128:55001, bound_value=119:61045, second_product=238:84500, answer=224:29923)
- Layer 36: ` riv`, ` SU`, `adal`, `羊`, ` stabil` (target ranks: base_value=64:1017, first_product=128:39441, bound_value=119:42465, second_product=238:68482, answer=224:16275)
- Layer 37: `}<?`, ` su`, ` sublim`, `翻了`, `不加` (target ranks: base_value=64:4601, first_product=128:69007, bound_value=119:73082, second_product=238:100839, answer=224:39908)
- Layer 38: `}<?`, ` sublim`, ` su`, `覆`, `不加` (target ranks: base_value=64:3471, first_product=128:85307, bound_value=119:74459, second_product=238:88683, answer=224:45858)
- Layer 39: `}<?`, ` sublim`, ` su`, ` Su`, `osit` (target ranks: base_value=64:13311, first_product=128:95634, bound_value=119:107057, second_product=238:108416, answer=224:75473)
- Layer 40: `殿堂`, ` su`, `acl`, `šk`, ` sublim` (target ranks: base_value=64:4297, first_product=128:49138, bound_value=119:58829, second_product=238:86929, answer=224:30511)
- Layer 41: `šk`, ` sublim`, ` .`, ` su`, `那两个` (target ranks: base_value=64:3561, first_product=128:20328, bound_value=119:33295, second_product=238:37407, answer=224:13973)

### Filler position 27 (absolute token 822, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126509, first_product=128:124929, bound_value=119:123083, second_product=238:124533, answer=224:122759)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10267, first_product=128:20917, bound_value=119:19640, second_product=238:23322, answer=224:20341)
- Layer 20: `ait`, ` Walker`, `锁定`, `Walker`, ` engaging` (target ranks: base_value=64:8580, first_product=128:30121, bound_value=119:27071, second_product=238:36237, answer=224:16095)
- Layer 30: ` SUV`, ` SU`, ` Su`, `s`, `SUV` (target ranks: base_value=64:1817, first_product=128:55989, bound_value=119:69805, second_product=238:81185, answer=224:34573)
- Layer 35: ` SU`, ` labor`, ` Su`, `外商投资`, `分解` (target ranks: base_value=64:1176, first_product=128:38261, bound_value=119:42846, second_product=238:54923, answer=224:17657)
- Layer 36: `分解`, `留存`, `adal`, ` SU`, `俯` (target ranks: base_value=64:1837, first_product=128:27781, bound_value=119:28576, second_product=238:41156, answer=224:9522)
- Layer 37: `}<?`, ` su`, `翻了`, `翻`, ` sublim` (target ranks: base_value=64:13215, first_product=128:55021, bound_value=119:53679, second_product=238:69972, answer=224:23349)
- Layer 38: `}<?`, ` sublim`, ` su`, `覆`, `退役` (target ranks: base_value=64:6872, first_product=128:69098, bound_value=119:56427, second_product=238:54825, answer=224:26402)
- Layer 39: `}<?`, ` sublim`, `osit`, `覆`, ` su` (target ranks: base_value=64:26136, first_product=128:90406, bound_value=119:103660, second_product=238:95067, answer=224:67320)
- Layer 40: `acl`, `殿堂`, `osit`, `acular`, ` su` (target ranks: base_value=64:5937, first_product=128:31351, bound_value=119:43943, second_product=238:65115, answer=224:15193)
- Layer 41: ` su`, ` sublim`, ` .`, `zij`, `俯` (target ranks: base_value=64:3643, first_product=128:13027, bound_value=119:22525, second_product=238:24706, answer=224:5212)

### Filler position 28 (absolute token 823, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126686, first_product=128:125289, bound_value=119:123393, second_product=238:124922, answer=224:123101)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:9886, first_product=128:20365, bound_value=119:19259, second_product=238:23590, answer=224:20425)
- Layer 20: `ait`, `能被`, ` Walker`, `Walker`, `锁定` (target ranks: base_value=64:6000, first_product=128:28132, bound_value=119:25248, second_product=238:37175, answer=224:16542)
- Layer 30: `adal`, `eder`, `退出`, ` kahaboga`, ` drip` (target ranks: base_value=64:287, first_product=128:26039, bound_value=119:72, second_product=238:155, answer=224:59)
- Layer 35: `238`, `237`, `239`, `236`, `冰冰` (target ranks: base_value=64:5308, first_product=128:5499, bound_value=119:1392, second_product=238:1, answer=224:17)
- Layer 36: `238`, `224`, `228`, `226`, `akang` (target ranks: base_value=64:31718, first_product=128:237, bound_value=119:9146, second_product=238:1, answer=224:2)
- Layer 37: `238`, `224`, `228`, ` Cover`, ` ICE` (target ranks: base_value=64:65893, first_product=128:886, bound_value=119:21464, second_product=238:1, answer=224:2)
- Layer 38: `224`, `二十四`, `204`, `228`, `第二百` (target ranks: base_value=64:48383, first_product=128:7769, bound_value=119:45999, second_product=238:11, answer=224:1)
- Layer 39: `224`, `殿堂`, `324`, `124`, `924` (target ranks: base_value=64:114613, first_product=128:86351, bound_value=119:109670, second_product=238:1501, answer=224:1)
- Layer 40: `224`, `贤`, `賢`, `vell`, `ekak` (target ranks: base_value=64:107895, first_product=128:102626, bound_value=119:117571, second_product=238:26434, answer=224:1)
- Layer 41: `相比之下`, `224`, `生日快乐`, ` nuest`, `��` (target ranks: base_value=64:71976, first_product=128:57761, bound_value=119:87305, second_product=238:9380, answer=224:2)

### Filler position 29 (absolute token 824, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126672, first_product=128:125066, bound_value=119:123244, second_product=238:124642, answer=224:122776)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:10775, first_product=128:21055, bound_value=119:20203, second_product=238:24836, answer=224:22239)
- Layer 20: ` smile`, `ait`, `锁定`, ` engaging`, ` Walker` (target ranks: base_value=64:9682, first_product=128:32490, bound_value=119:27576, second_product=238:46467, answer=224:18886)
- Layer 30: ` tear`, `�`, `acin`, `分解`, ` cage` (target ranks: base_value=64:24516, first_product=128:78497, bound_value=119:76194, second_product=238:105176, answer=224:40445)
- Layer 35: `分解`, ` tap`, `�`, `Tap`, `tap` (target ranks: base_value=64:36213, first_product=128:87240, bound_value=119:68031, second_product=238:99299, answer=224:30917)
- Layer 36: `分解`, `退出`, `坏`, `翻`, ` rip` (target ranks: base_value=64:30996, first_product=128:56469, bound_value=119:50284, second_product=238:83701, answer=224:15814)
- Layer 37: `坏`, `}<?`, `zat`, ` torn`, ` rip` (target ranks: base_value=64:70031, first_product=128:72901, bound_value=119:64923, second_product=238:104711, answer=224:30455)
- Layer 38: `zat`, `}<?`, `坏`, ` habitual`, `打磨` (target ranks: base_value=64:61084, first_product=128:85172, bound_value=119:74944, second_product=238:112979, answer=224:39612)
- Layer 39: `}<?`, `zat`, `�`, `殿堂`, `迷惑` (target ranks: base_value=64:70227, first_product=128:92733, bound_value=119:99964, second_product=238:111019, answer=224:34631)
- Layer 40: `坏`, `zat`, `殿堂`, `acl`, `坏的` (target ranks: base_value=64:25272, first_product=128:46508, bound_value=119:63492, second_product=238:94413, answer=224:8027)
- Layer 41: `坏`, ` `, ` .`, ` waiting`, `zel` (target ranks: base_value=64:4681, first_product=128:3435, bound_value=119:16395, second_product=238:11885, answer=224:232)

### Filler position 30 (absolute token 825, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=64:126919, first_product=128:125636, bound_value=119:123881, second_product=238:125345, answer=224:123258)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10177, first_product=128:20283, bound_value=119:19879, second_product=238:24333, answer=224:21728)
- Layer 20: `ait`, `锁定`, `atile`, `aty`, ` smile` (target ranks: base_value=64:11953, first_product=128:23371, bound_value=119:26954, second_product=238:36670, answer=224:18292)
- Layer 30: ` Ni`, ` Niagara`, `Ni`, ` ni`, ` NI` (target ranks: base_value=64:12821, first_product=128:63511, bound_value=119:47955, second_product=238:118781, answer=224:59940)
- Layer 35: ` Ni`, ` Niagara`, ` NI`, ` ni`, `Ni` (target ranks: base_value=64:13346, first_product=128:51015, bound_value=119:39713, second_product=238:114135, answer=224:57994)
- Layer 36: ` Niagara`, ` Ni`, ` NI`, ` ni`, `感兴趣` (target ranks: base_value=64:13483, first_product=128:30535, bound_value=119:22511, second_product=238:96531, answer=224:38241)
- Layer 37: ` Ni`, ` NI`, ` Niagara`, ` Nij`, `Ni` (target ranks: base_value=64:23504, first_product=128:41525, bound_value=119:20004, second_product=238:118839, answer=224:51898)
- Layer 38: ` Ni`, ` NI`, ` Nij`, ` ni`, ` Niagara` (target ranks: base_value=64:22333, first_product=128:66198, bound_value=119:30678, second_product=238:120117, answer=224:67334)
- Layer 39: ` Ni`, ` Nij`, ` NI`, `}<?`, `Ni` (target ranks: base_value=64:41776, first_product=128:78262, bound_value=119:85095, second_product=238:122985, answer=224:83748)
- Layer 40: `坏的`, `不急`, `坏`, `acl`, `acular` (target ranks: base_value=64:7893, first_product=128:34752, bound_value=119:47790, second_product=238:109667, answer=224:44996)
- Layer 41: ` .`, `坏`, `鹃`, ` waiting`, `从前` (target ranks: base_value=64:2668, first_product=128:9218, bound_value=119:19169, second_product=238:68132, answer=224:18060)

### Filler position 31 (absolute token 826, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:126973, first_product=128:125625, bound_value=119:123945, second_product=238:125247, answer=224:123179)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9943, first_product=128:19869, bound_value=119:20084, second_product=238:23996, answer=224:22368)
- Layer 20: `锁定`, `ait`, ` smile`, `鞍`, `cape` (target ranks: base_value=64:8780, first_product=128:18821, bound_value=119:23981, second_product=238:27359, answer=224:16798)
- Layer 30: ` tap`, `tap`, `Tap`, `回答`, ` answer` (target ranks: base_value=64:17254, first_product=128:54094, bound_value=119:86809, second_product=238:65641, answer=224:61202)
- Layer 35: ` tap`, ` answer`, ` vertical`, ` Answer`, `回答` (target ranks: base_value=64:25831, first_product=128:64381, bound_value=119:80479, second_product=238:89641, answer=224:52343)
- Layer 36: ` tap`, `Tap`, `tap`, ` riv`, ` answer` (target ranks: base_value=64:13778, first_product=128:30957, bound_value=119:47769, second_product=238:58339, answer=224:28731)
- Layer 37: ` rational`, `rational`, `comp`, ` tap`, `radesh` (target ranks: base_value=64:39475, first_product=128:54258, bound_value=119:74002, second_product=238:90738, answer=224:50573)
- Layer 38: `}<?`, `rational`, `�`, ` lenker`, ` rational` (target ranks: base_value=64:45556, first_product=128:62935, bound_value=119:69492, second_product=238:95850, answer=224:37679)
- Layer 39: ` lenker`, `<｜begin▁of▁sentence｜>`, `ocyst`, `}<?`, `�` (target ranks: base_value=64:28783, first_product=128:88060, bound_value=119:107249, second_product=238:96961, answer=224:30938)
- Layer 40: ` Answer`, `acular`, `<｜begin▁of▁sentence｜>`, `Answer`, ` forty` (target ranks: base_value=64:3091, first_product=128:53555, bound_value=119:47377, second_product=238:62751, answer=224:1440)
- Layer 41: `Answer`, ` Answer`, ` .`, ` waiting`, `坏` (target ranks: base_value=64:889, first_product=128:9087, bound_value=119:23205, second_product=238:16994, answer=224:143)

### Filler position 32 (absolute token 827, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `Noiz` (target ranks: base_value=64:127061, first_product=128:125771, bound_value=119:124091, second_product=238:125386, answer=224:123292)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9416, first_product=128:19467, bound_value=119:19508, second_product=238:22929, answer=224:21243)
- Layer 20: `ait`, `锁定`, ` Walker`, ` LS`, ` smile` (target ranks: base_value=64:8219, first_product=128:18863, bound_value=119:23984, second_product=238:29821, answer=224:15070)
- Layer 30: ` verk`, ` labor`, `�`, ` var`, ` reduct` (target ranks: base_value=64:15905, first_product=128:79434, bound_value=119:70673, second_product=238:105400, answer=224:71734)
- Layer 35: ` var`, ` variable`, ` equations`, ` definitions`, ` variables` (target ranks: base_value=64:11425, first_product=128:58223, bound_value=119:72043, second_product=238:78271, answer=224:41262)
- Layer 36: ` definitions`, ` equations`, ` Definitions`, ` var`, `Definitions` (target ranks: base_value=64:18080, first_product=128:50251, bound_value=119:55242, second_product=238:63093, answer=224:28194)
- Layer 37: ` definitions`, ` Definitions`, `Definitions`, `定义`, ` variables` (target ranks: base_value=64:61315, first_product=128:85383, bound_value=119:81985, second_product=238:89976, answer=224:60154)
- Layer 38: ` definitions`, ` Definitions`, `Definitions`, `}<?`, `定义` (target ranks: base_value=64:74294, first_product=128:91796, bound_value=119:88558, second_product=238:82078, answer=224:68518)
- Layer 39: `<｜begin▁of▁sentence｜>`, `}<?`, ` DEF`, ` def`, `variables` (target ranks: base_value=64:80618, first_product=128:88927, bound_value=119:104127, second_product=238:109323, answer=224:99280)
- Layer 40: ` definitions`, ` Definitions`, `殿堂`, `Definitions`, ` variables` (target ranks: base_value=64:43179, first_product=128:75829, bound_value=119:83676, second_product=238:116157, answer=224:90220)
- Layer 41: `acular`, ` definitions`, ` mim`, `然而`, `变量的` (target ranks: base_value=64:9046, first_product=128:16590, bound_value=119:30511, second_product=238:94673, answer=224:45300)

### Filler position 33 (absolute token 828, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `aplenty`, `�乐`, `-ulo` (target ranks: base_value=64:127031, first_product=128:125674, bound_value=119:124002, second_product=238:125293, answer=224:123196)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9491, first_product=128:19707, bound_value=119:19349, second_product=238:22382, answer=224:20633)
- Layer 20: `ait`, ` Walker`, ` LS`, `Walker`, `LS` (target ranks: base_value=64:5787, first_product=128:18963, bound_value=119:17956, second_product=238:31871, answer=224:11602)
- Layer 30: ` SUV`, ` Su`, `SUV`, ` SU`, `�` (target ranks: base_value=64:6456, first_product=128:88664, bound_value=119:85281, second_product=238:119757, answer=224:87042)
- Layer 35: ` SUV`, ` Su`, `SUV`, ` SU`, ` su` (target ranks: base_value=64:4877, first_product=128:77329, bound_value=119:71219, second_product=238:111947, answer=224:69393)
- Layer 36: ` SUV`, `留存`, ` Su`, `SUV`, ` SU` (target ranks: base_value=64:5870, first_product=128:46280, bound_value=119:35859, second_product=238:90183, answer=224:44785)
- Layer 37: ` su`, `}<?`, ` SUV`, `不加`, ` Su` (target ranks: base_value=64:34689, first_product=128:77381, bound_value=119:50172, second_product=238:114568, answer=224:85785)
- Layer 38: ` su`, `}<?`, `不加`, ` SUV`, ` Nij` (target ranks: base_value=64:48182, first_product=128:106866, bound_value=119:48653, second_product=238:114525, answer=224:97247)
- Layer 39: ` Su`, ` su`, ` Nij`, ` Suzanne`, ` SUV` (target ranks: base_value=64:51006, first_product=128:107975, bound_value=119:71615, second_product=238:115830, answer=224:98890)
- Layer 40: ` su`, `殿堂`, `迷惑`, `交替`, `zij` (target ranks: base_value=64:10760, first_product=128:34061, bound_value=119:15937, second_product=238:78727, answer=224:42159)
- Layer 41: `zij`, `没有被`, ` su`, ` whichever`, `šk` (target ranks: base_value=64:10291, first_product=128:32792, bound_value=119:20793, second_product=238:68907, answer=224:26403)

### Filler position 34 (absolute token 829, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127294, first_product=128:126033, bound_value=119:124478, second_product=238:125548, answer=224:123352)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:9658, first_product=128:20016, bound_value=119:19489, second_product=238:22323, answer=224:19969)
- Layer 20: `ait`, ` Walker`, ` LS`, `Walker`, `LS` (target ranks: base_value=64:3874, first_product=128:21692, bound_value=119:21917, second_product=238:32435, answer=224:12308)
- Layer 30: `64`, ` repeated`, ` metas`, ` repetitions`, ` dy` (target ranks: base_value=64:1, first_product=128:226, bound_value=119:13450, second_product=238:49308, answer=224:11060)
- Layer 35: `64`, `分解`, `出生`, ` repeated`, ` repetition` (target ranks: base_value=64:1, first_product=128:15, bound_value=119:1677, second_product=238:23713, answer=224:2843)
- Layer 36: `64`, ` repeated`, `留存`, `分解`, `重复` (target ranks: base_value=64:1, first_product=128:28, bound_value=119:1859, second_product=238:18621, answer=224:3951)
- Layer 37: `64`, `radesh`, ` doubling`, `殿堂`, `翻了` (target ranks: base_value=64:1, first_product=128:12, bound_value=119:2994, second_product=238:44154, answer=224:9679)
- Layer 38: ` doubling`, `殿堂`, ` doubled`, ` multiplic`, `radesh` (target ranks: base_value=64:10, first_product=128:308, bound_value=119:13024, second_product=238:71499, answer=224:30613)
- Layer 39: `殿堂`, `}<?`, ` Haley`, `ounder`, ` doubling` (target ranks: base_value=64:73, first_product=128:1182, bound_value=119:60973, second_product=238:96434, answer=224:55053)
- Layer 40: ` su`, `ess`, `S`, `swer`, ` sublim` (target ranks: base_value=64:2446, first_product=128:5925, bound_value=119:9842, second_product=238:42815, answer=224:30524)
- Layer 41: ` su`, `swer`, ` `, ` compounded`, `每次` (target ranks: base_value=64:2577, first_product=128:1601, bound_value=119:5468, second_product=238:28618, answer=224:7864)

### Filler position 35 (absolute token 830, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `aplenty`, `Noiz` (target ranks: base_value=64:127310, first_product=128:126170, bound_value=119:124655, second_product=238:125701, answer=224:123489)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11117, first_product=128:21265, bound_value=119:20742, second_product=238:23552, answer=224:21455)
- Layer 20: `ait`, `足`, ` smile`, `cape`, `锁定` (target ranks: base_value=64:5495, first_product=128:21353, bound_value=119:19993, second_product=238:23482, answer=224:10306)
- Layer 30: ` twice`, ` Tw`, `算出`, ` subtract`, `Tw` (target ranks: base_value=64:513, first_product=128:11866, bound_value=119:9079, second_product=238:14893, answer=224:4744)
- Layer 35: ` Tw`, `calc`, ` twice`, ` calc`, `calcul` (target ranks: base_value=64:236, first_product=128:2523, bound_value=119:1026, second_product=238:5579, answer=224:989)
- Layer 36: `calcul`, ` calc`, `calc`, `计算的`, ` Tw` (target ranks: base_value=64:1040, first_product=128:1855, bound_value=119:637, second_product=238:4042, answer=224:758)
- Layer 37: `}<?`, `calcul`, ` doubling`, ` calc`, `算式` (target ranks: base_value=64:7123, first_product=128:2582, bound_value=119:608, second_product=238:5635, answer=224:1520)
- Layer 38: `}<?`, ` doubling`, `calcul`, `计算方法`, ` doubled` (target ranks: base_value=64:14497, first_product=128:10615, bound_value=119:2590, second_product=238:14224, answer=224:3796)
- Layer 39: `}<?`, ` doubling`, `东海`, `pet`, ` Nationals` (target ranks: base_value=64:24737, first_product=128:33823, bound_value=119:32224, second_product=238:41173, answer=224:11470)
- Layer 40: `duc`, `坏`, ` Tw`, `装`, `acl` (target ranks: base_value=64:3560, first_product=128:8642, bound_value=119:3517, second_product=238:21573, answer=224:3737)
- Layer 41: ` su`, ` compounded`, ` w`, ` first`, ` ` (target ranks: base_value=64:438, first_product=128:956, bound_value=119:732, second_product=238:3183, answer=224:357)

### Filler position 36 (absolute token 831, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127365, first_product=128:126202, bound_value=119:124768, second_product=238:125829, answer=224:123725)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11473, first_product=128:21764, bound_value=119:21585, second_product=238:24844, answer=224:23084)
- Layer 20: `能被`, ` smile`, ` Engaging`, ` engaging`, `距` (target ranks: base_value=64:8766, first_product=128:27552, bound_value=119:24086, second_product=238:45909, answer=224:14474)
- Layer 30: `64`, ` twice`, `Tw`, ` Tw`, ` sixty` (target ranks: base_value=64:1, first_product=128:4724, bound_value=119:43941, second_product=238:66022, answer=224:7956)
- Layer 35: `64`, `分解`, `adaghan`, ` twice`, `63` (target ranks: base_value=64:1, first_product=128:4781, bound_value=119:29064, second_product=238:57382, answer=224:7719)
- Layer 36: `64`, `adaghan`, ` doubled`, `翻`, ` doubling` (target ranks: base_value=64:1, first_product=128:8839, bound_value=119:38839, second_product=238:62811, answer=224:10033)
- Layer 37: `}<?`, ` doubling`, ` doubled`, ` doubles`, `64` (target ranks: base_value=64:5, first_product=128:43437, bound_value=119:75615, second_product=238:92898, answer=224:35038)
- Layer 38: `}<?`, ` doubled`, ` doubling`, ` doubles`, `dividers` (target ranks: base_value=64:32, first_product=128:78005, bound_value=119:92639, second_product=238:104975, answer=224:56922)
- Layer 39: `}<?`, ` doubled`, ` doubling`, ` doubles`, `ounder` (target ranks: base_value=64:367, first_product=128:34481, bound_value=119:60506, second_product=238:63144, answer=224:26841)
- Layer 40: ` su`, `acular`, ` doubled`, `翻`, ` twist` (target ranks: base_value=64:171, first_product=128:7169, bound_value=119:960, second_product=238:3745, answer=224:1498)
- Layer 41: ` su`, `acular`, ` `, ` twist`, ` compounded` (target ranks: base_value=64:80, first_product=128:873, bound_value=119:299, second_product=238:1061, answer=224:244)

### Filler position 37 (absolute token 832, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127537, first_product=128:126487, bound_value=119:125098, second_product=238:126184, answer=224:123998)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11630, first_product=128:22265, bound_value=119:22847, second_product=238:25929, answer=224:24256)
- Layer 20: `ait`, `能被`, `忑`, ` engaging`, `atile` (target ranks: base_value=64:19542, first_product=128:44003, bound_value=119:49286, second_product=238:74240, answer=224:29347)
- Layer 30: ` Ni`, `Ni`, ` Niagara`, ` ni`, ` NI` (target ranks: base_value=64:22127, first_product=128:72199, bound_value=119:83380, second_product=238:125120, answer=224:65810)
- Layer 35: ` Ni`, ` NI`, `Ni`, ` Niagara`, ` ni` (target ranks: base_value=64:18386, first_product=128:60195, bound_value=119:71679, second_product=238:119989, answer=224:57344)
- Layer 36: ` Ni`, ` NI`, ` Niagara`, ` ni`, `尼亚` (target ranks: base_value=64:28178, first_product=128:47712, bound_value=119:57614, second_product=238:113930, answer=224:38966)
- Layer 37: ` Ni`, ` Nij`, ` NI`, `}<?`, `Ni` (target ranks: base_value=64:82454, first_product=128:83219, bound_value=119:90203, second_product=238:124510, answer=224:71788)
- Layer 38: ` Nij`, ` Ni`, ` NI`, `}<?`, `zat` (target ranks: base_value=64:56247, first_product=128:96607, bound_value=119:94104, second_product=238:123977, answer=224:74237)
- Layer 39: ` Nij`, `<｜begin▁of▁sentence｜>`, ` Ni`, `}<?`, ` NI` (target ranks: base_value=64:52055, first_product=128:90477, bound_value=119:105123, second_product=238:121660, answer=224:72135)
- Layer 40: `acular`, `calcul`, `不急`, `坏`, ` sublim` (target ranks: base_value=64:8753, first_product=128:35089, bound_value=119:64643, second_product=238:109552, answer=224:32657)
- Layer 41: ` .`, `鹃`, `从前`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:846, first_product=128:5089, bound_value=119:20144, second_product=238:56810, answer=224:6766)

### Filler position 38 (absolute token 833, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127503, first_product=128:126355, bound_value=119:124974, second_product=238:125947, answer=224:123811)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10704, first_product=128:21158, bound_value=119:21526, second_product=238:24864, answer=224:22860)
- Layer 20: `ait`, ` engaging`, `忑`, `能被`, `平行` (target ranks: base_value=64:20348, first_product=128:50058, bound_value=119:56367, second_product=238:75177, answer=224:34152)
- Layer 30: `算出`, `�`, `aloh`, `calcul`, `计算出` (target ranks: base_value=64:21909, first_product=128:86899, bound_value=119:88966, second_product=238:118773, answer=224:64560)
- Layer 35: `aloh`, ` Woo`, ` WO`, ` Wo`, `外商投资` (target ranks: base_value=64:23393, first_product=128:68152, bound_value=119:70869, second_product=238:108133, answer=224:50206)
- Layer 36: `留存`, ` Wo`, ` Woo`, `�`, ` WO` (target ranks: base_value=64:24953, first_product=128:46551, bound_value=119:41374, second_product=238:98702, answer=224:35206)
- Layer 37: `}<?`, `asi`, `ота`, `殿堂`, `osit` (target ranks: base_value=64:69956, first_product=128:65773, bound_value=119:53103, second_product=238:119236, answer=224:53099)
- Layer 38: `wof`, `}<?`, `osit`, `asi`, ` Wort` (target ranks: base_value=64:94649, first_product=128:106931, bound_value=119:54554, second_product=238:124424, answer=224:68098)
- Layer 39: `}<?`, `osit`, ` Nij`, `wof`, `本题分析` (target ranks: base_value=64:64972, first_product=128:103863, bound_value=119:80950, second_product=238:124500, answer=224:74446)
- Layer 40: `calcul`, ` sublim`, `殿堂`, ` su`, `acular` (target ranks: base_value=64:14932, first_product=128:41167, bound_value=119:38877, second_product=238:103340, answer=224:24399)
- Layer 41: `步骤如下`, `abd`, ` `, `acular`, `鹉` (target ranks: base_value=64:3406, first_product=128:8893, bound_value=119:19158, second_product=238:54555, answer=224:4992)

### Filler position 39 (absolute token 834, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127464, first_product=128:126555, bound_value=119:125243, second_product=238:126168, answer=224:123928)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10056, first_product=128:19845, bound_value=119:20398, second_product=238:23477, answer=224:21804)
- Layer 20: `ait`, `锁定`, ` engaging`, `鞍`, `拆` (target ranks: base_value=64:9645, first_product=128:26255, bound_value=119:35601, second_product=238:43524, answer=224:19613)
- Layer 30: `sac`, `下沉`, `custom`, `sms`, `calcul` (target ranks: base_value=64:2115, first_product=128:21830, bound_value=119:22986, second_product=238:27602, answer=224:5888)
- Layer 35: `calcul`, `退出`, `放下`, ` calculator`, `custom` (target ranks: base_value=64:5748, first_product=128:11516, bound_value=119:5732, second_product=238:7344, answer=224:1298)
- Layer 36: `calcul`, `退出`, `custom`, `反复`, `acin` (target ranks: base_value=64:11057, first_product=128:8293, bound_value=119:9832, second_product=238:8472, answer=224:1321)
- Layer 37: `}<?`, `在北京`, `覆`, `放下`, `北京的` (target ranks: base_value=64:76149, first_product=128:12170, bound_value=119:21904, second_product=238:6275, answer=224:105)
- Layer 38: `}<?`, `覆`, ` Peking`, `malink`, `apper` (target ranks: base_value=64:84966, first_product=128:34373, bound_value=119:38188, second_product=238:21150, answer=224:260)
- Layer 39: `}<?`, `hatic`, `dividers`, ` Peking`, `ounder` (target ranks: base_value=64:97772, first_product=128:100591, bound_value=119:107495, second_product=238:48698, answer=224:43)
- Layer 40: `224`, `}<?`, `calcul`, `ess`, `覆` (target ranks: base_value=64:97486, first_product=128:111891, bound_value=119:108648, second_product=238:62301, answer=224:1)
- Layer 41: `224`, ` .`, `等待着`, `Answer`, ` waiting` (target ranks: base_value=64:52938, first_product=128:68508, bound_value=119:66710, second_product=238:28817, answer=224:1)

### Filler position 40 (absolute token 835, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `datasetId` (target ranks: base_value=64:127533, first_product=128:126507, bound_value=119:125153, second_product=238:126181, answer=224:123980)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:10930, first_product=128:20980, bound_value=119:21193, second_product=238:23833, answer=224:22470)
- Layer 20: `ait`, `锁定`, `鞍`, `能被`, `ätte` (target ranks: base_value=64:4609, first_product=128:18913, bound_value=119:23603, second_product=238:27580, answer=224:14720)
- Layer 30: `退出`, `acos`, ` competitive`, `放下`, ` practiced` (target ranks: base_value=64:129, first_product=128:9590, bound_value=119:157, second_product=238:143, answer=224:336)
- Layer 35: `238`, `237`, `239`, `236`, `228` (target ranks: base_value=64:13817, first_product=128:1008, bound_value=119:1887, second_product=238:1, answer=224:15)
- Layer 36: `228`, `224`, `238`, `225`, `226` (target ranks: base_value=64:63172, first_product=128:53, bound_value=119:12577, second_product=238:3, answer=224:2)
- Layer 37: `228`, `224`, `238`, `225`, `226` (target ranks: base_value=64:100855, first_product=128:290, bound_value=119:25831, second_product=238:3, answer=224:2)
- Layer 38: `224`, `225`, `226`, `222`, `228` (target ranks: base_value=64:107244, first_product=128:17148, bound_value=119:74949, second_product=238:10, answer=224:1)
- Layer 39: `224`, `225`, `226`, `324`, `424` (target ranks: base_value=64:110398, first_product=128:67875, bound_value=119:98627, second_product=238:442, answer=224:1)
- Layer 40: `224`, ` talags`, `贤`, `賢`, `zilla` (target ranks: base_value=64:88771, first_product=128:65624, bound_value=119:106263, second_product=238:4348, answer=224:1)
- Layer 41: `224`, `��`, `zilla`, `相比之下`, ` nuest` (target ranks: base_value=64:50661, first_product=128:41360, bound_value=119:77160, second_product=238:2807, answer=224:1)

### Filler position 41 (absolute token 836, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127477, first_product=128:126516, bound_value=119:125146, second_product=238:126040, answer=224:123861)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11378, first_product=128:21483, bound_value=119:21859, second_product=238:24137, answer=224:23292)
- Layer 20: `ait`, `锁定`, `能被`, ` Walker`, ` smile` (target ranks: base_value=64:9382, first_product=128:22991, bound_value=119:31570, second_product=238:29548, answer=224:17563)
- Layer 30: ` popcorn`, `冰`, ` decline`, ` coloring`, `陪` (target ranks: base_value=64:161, first_product=128:12581, bound_value=119:37, second_product=238:82, answer=224:468)
- Layer 35: `238`, `237`, `239`, `236`, `138` (target ranks: base_value=64:16340, first_product=128:943, bound_value=119:1527, second_product=238:1, answer=224:66)
- Layer 36: `238`, `224`, `228`, `二十四`, `225` (target ranks: base_value=64:40432, first_product=128:58, bound_value=119:6957, second_product=238:1, answer=224:2)
- Layer 37: `238`, `224`, `228`, `/tbsp`, `225` (target ranks: base_value=64:66738, first_product=128:144, bound_value=119:13179, second_product=238:1, answer=224:2)
- Layer 38: `224`, `二十四`, `24`, `124`, `244` (target ranks: base_value=64:44440, first_product=128:8008, bound_value=119:44560, second_product=238:11, answer=224:1)
- Layer 39: `224`, `324`, `124`, `524`, `724` (target ranks: base_value=64:90804, first_product=128:66275, bound_value=119:70100, second_product=238:235, answer=224:1)
- Layer 40: `224`, ` talags`, `)?`, `贤`, `賢` (target ranks: base_value=64:68745, first_product=128:67409, bound_value=119:71803, second_product=238:3079, answer=224:1)
- Layer 41: `224`, ` nuest`, `没有得到`, `��`, `相比之下` (target ranks: base_value=64:68007, first_product=128:64919, bound_value=119:66749, second_product=238:8271, answer=224:1)

### Filler position 42 (absolute token 837, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127532, first_product=128:126450, bound_value=119:125152, second_product=238:126020, answer=224:123777)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:12264, first_product=128:22269, bound_value=119:22290, second_product=238:24882, answer=224:24153)
- Layer 20: `锁定`, ` smile`, `鞍`, `ession`, `cape` (target ranks: base_value=64:11166, first_product=128:16421, bound_value=119:27164, second_product=238:19215, answer=224:12300)
- Layer 30: `冰冻`, `冰`, `�`, ` iceberg`, `iab` (target ranks: base_value=64:3400, first_product=128:33593, bound_value=119:5373, second_product=238:4486, answer=224:2400)
- Layer 35: `238`, `�`, `冰冰`, `冰`, `ukiran` (target ranks: base_value=64:6142, first_product=128:13121, bound_value=119:14414, second_product=238:1, answer=224:853)
- Layer 36: ` quadru`, `�`, `238`, ` ICE`, `冰冰` (target ranks: base_value=64:7914, first_product=128:613, bound_value=119:27952, second_product=238:3, answer=224:34)
- Layer 37: ` ICE`, `冰冰`, ` quadru`, `polar`, `在北京` (target ranks: base_value=64:41643, first_product=128:2728, bound_value=119:51606, second_product=238:9, answer=224:129)
- Layer 38: ` quadru`, `东海`, `放下`, `殿堂`, `打包` (target ranks: base_value=64:45605, first_product=128:6847, bound_value=119:58792, second_product=238:188, answer=224:6)
- Layer 39: `224`, `本题分析`, `殿堂`, `智慧的`, `打包` (target ranks: base_value=64:114313, first_product=128:35067, bound_value=119:89926, second_product=238:201, answer=224:1)
- Layer 40: `224`, ` `, `沛`, `acular`, `放下` (target ranks: base_value=64:103951, first_product=128:25580, bound_value=119:85425, second_product=238:546, answer=224:1)
- Layer 41: ` .`, ` `, `相比之下`, `iven`, `224` (target ranks: base_value=64:59958, first_product=128:10814, bound_value=119:57686, second_product=238:241, answer=224:5)

### Filler position 43 (absolute token 838, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=64:127482, first_product=128:126459, bound_value=119:125171, second_product=238:126024, answer=224:123807)
- Layer 10: ` Walker`, `锁定`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11639, first_product=128:21847, bound_value=119:22412, second_product=238:24875, answer=224:24416)
- Layer 20: `锁定`, ` smile`, `LS`, `距`, `忑` (target ranks: base_value=64:6503, first_product=128:16583, bound_value=119:24372, second_product=238:28305, answer=224:14636)
- Layer 30: `atar`, `反复`, ` repeated`, `鞍`, `sets` (target ranks: base_value=64:329, first_product=128:2900, bound_value=119:27, second_product=238:13283, answer=224:9066)
- Layer 35: `119`, `十九`, `19`, ` XIX`, `第十九` (target ranks: base_value=64:5628, first_product=128:23739, bound_value=119:1, second_product=238:347, answer=224:22516)
- Layer 36: `119`, `防火`, `大火`, `幽冥`, `消防` (target ranks: base_value=64:42166, first_product=128:28361, bound_value=119:1, second_product=238:124, answer=224:52086)
- Layer 37: `119`, `防火`, `火灾`, ` ICM`, `幽冥` (target ranks: base_value=64:112752, first_product=128:62877, bound_value=119:1, second_product=238:928, answer=224:102077)
- Layer 38: `119`, ` ICD`, `防火`, ` ICM`, `院长` (target ranks: base_value=64:118574, first_product=128:87360, bound_value=119:1, second_product=238:3056, answer=224:102384)
- Layer 39: `119`, ` ICM`, `duc`, ` duc`, `龙虾` (target ranks: base_value=64:68779, first_product=128:60146, bound_value=119:1, second_product=238:238, answer=224:29856)
- Layer 40: `119`, `duc`, ` su`, `epen`, `安全保障` (target ranks: base_value=64:44957, first_product=128:50141, bound_value=119:1, second_product=238:200, answer=224:458)
- Layer 41: `Explanation`, `两声`, `119`, `步骤如下`, `<｜begin▁of▁file｜>` (target ranks: base_value=64:53503, first_product=128:83633, bound_value=119:3, second_product=238:653, answer=224:4914)

### Filler position 44 (absolute token 839, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `�乐`, `Noiz`, `aplenty` (target ranks: base_value=64:127517, first_product=128:126336, bound_value=119:125075, second_product=238:125937, answer=224:123720)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11608, first_product=128:21529, bound_value=119:22716, second_product=238:24821, answer=224:23564)
- Layer 20: `忑`, `ait`, ` Walker`, `距`, `锁定` (target ranks: base_value=64:7348, first_product=128:18394, bound_value=119:28933, second_product=238:35876, answer=224:18204)
- Layer 30: `64`, `atar`, ` twice`, `79`, ` Tw` (target ranks: base_value=64:1, first_product=128:1700, bound_value=119:3411, second_product=238:47356, answer=224:18751)
- Layer 35: `119`, ` binary`, ` twice`, `64`, `79` (target ranks: base_value=64:4, first_product=128:7520, bound_value=119:1, second_product=238:31015, answer=224:31145)
- Layer 36: `119`, ` quadru`, `翻`, ` Ter`, `�` (target ranks: base_value=64:16, first_product=128:14074, bound_value=119:1, second_product=238:27196, answer=224:44774)
- Layer 37: `119`, `}<?`, `院长`, `ounder`, `iram` (target ranks: base_value=64:6281, first_product=128:42007, bound_value=119:1, second_product=238:38554, answer=224:96032)
- Layer 38: `119`, `院长`, `东海`, `叶子`, ` doubles` (target ranks: base_value=64:9431, first_product=128:56227, bound_value=119:1, second_product=238:51085, answer=224:101751)
- Layer 39: `ounder`, `acons`, `东海`, `叶子`, `}<?` (target ranks: base_value=64:17469, first_product=128:33132, bound_value=119:57, second_product=238:17926, answer=224:22429)
- Layer 40: ` `, ` su`, ` sublim`, `放下`, `accur` (target ranks: base_value=64:9186, first_product=128:21022, bound_value=119:15, second_product=238:1525, answer=224:108)
- Layer 41: ` .`, ` `, `第二百`, ` twice`, ` ;` (target ranks: base_value=64:4880, first_product=128:9911, bound_value=119:35, second_product=238:468, answer=224:41)

### Filler position 45 (absolute token 840, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127629, first_product=128:126703, bound_value=119:125513, second_product=238:126253, answer=224:123953)
- Layer 10: `锁定`, ` Walker`, `Walker`, `ait`, ` cheer` (target ranks: base_value=64:11631, first_product=128:20963, bound_value=119:22636, second_product=238:24156, answer=224:22827)
- Layer 20: `ait`, ` Walker`, `会成为`, `能被`, `锁定` (target ranks: base_value=64:15836, first_product=128:28805, bound_value=119:47346, second_product=238:46888, answer=224:22392)
- Layer 30: ` SUV`, `SUV`, ` Su`, `su`, ` su` (target ranks: base_value=64:18317, first_product=128:86212, bound_value=119:95648, second_product=238:114932, answer=224:75142)
- Layer 35: ` Su`, ` SUV`, ` SU`, ` su`, `SUV` (target ranks: base_value=64:20956, first_product=128:87873, bound_value=119:82670, second_product=238:100153, answer=224:60085)
- Layer 36: ` su`, ` SU`, ` Su`, ` SUV`, `留存` (target ranks: base_value=64:9677, first_product=128:31533, bound_value=119:38877, second_product=238:46776, answer=224:18672)
- Layer 37: `}<?`, ` su`, ` SUV`, ` Sund`, ` sublim` (target ranks: base_value=64:60878, first_product=128:69680, bound_value=119:71566, second_product=238:96419, answer=224:53696)
- Layer 38: `}<?`, ` su`, ` sublim`, ` SUV`, ` fusion` (target ranks: base_value=64:38671, first_product=128:75822, bound_value=119:66314, second_product=238:74049, answer=224:57157)
- Layer 39: `}<?`, ` sublim`, ` su`, `东海`, `polar` (target ranks: base_value=64:35178, first_product=128:52567, bound_value=119:75302, second_product=238:51470, answer=224:33860)
- Layer 40: ` Tw`, ` seventy`, ` Seventy`, `acular`, ` fifty` (target ranks: base_value=64:6315, first_product=128:6876, bound_value=119:16612, second_product=238:21402, answer=224:2250)
- Layer 41: ` .`, `<｜end▁of▁sentence｜>`, ` `, ` .↵↵`, `有下列` (target ranks: base_value=64:1775, first_product=128:1633, bound_value=119:4471, second_product=238:3889, answer=224:227)

### Filler position 46 (absolute token 841, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=64:127460, first_product=128:126466, bound_value=119:125216, second_product=238:126040, answer=224:123666)
- Layer 10: `锁定`, ` Walker`, `Walker`, ` cheer`, `ait` (target ranks: base_value=64:11460, first_product=128:20949, bound_value=119:21922, second_product=238:23528, answer=224:22380)
- Layer 20: ` blanks`, ` Blank`, `blank`, `空白`, ` blank` (target ranks: base_value=64:75829, first_product=128:74158, bound_value=119:101712, second_product=238:47127, answer=224:61055)
- Layer 30: ` spac`, `?datasetId`, `坝`, `}using`, ` dekameters` (target ranks: base_value=64:100799, first_product=128:79236, bound_value=119:117302, second_product=238:78600, answer=224:79533)
- Layer 35: `足足`, `俯`, `放下`, `坏`, `}using` (target ranks: base_value=64:77378, first_product=128:65429, bound_value=119:91555, second_product=238:64405, answer=224:71862)
- Layer 36: `足足`, `俯`, ` reserved`, `ancock`, ` reduct` (target ranks: base_value=64:18011, first_product=128:19538, bound_value=119:45229, second_product=238:16942, answer=224:29072)
- Layer 37: `}<?`, `放下`, `onana`, `合并`, `放下了` (target ranks: base_value=64:51475, first_product=128:25615, bound_value=119:58122, second_product=238:36523, answer=224:45689)
- Layer 38: ` .`, `错过`, ` Wilson`, `坏`, `俯` (target ranks: base_value=64:19589, first_product=128:17782, bound_value=119:42261, second_product=238:25582, answer=224:20536)
- Layer 39: ` .`, `hatic`, `罢`, ` .↵↵`, `�` (target ranks: base_value=64:37605, first_product=128:37965, bound_value=119:73186, second_product=238:32131, answer=224:2565)
- Layer 40: ` .`, ` .↵↵`, ` fifty`, ` .↵`, ` nasod` (target ranks: base_value=64:3771, first_product=128:8418, bound_value=119:25415, second_product=238:16455, answer=224:553)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:1972, first_product=128:1300, bound_value=119:8587, second_product=238:3383, answer=224:35)

### Filler position 47 (absolute token 842, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=64:127567, first_product=128:126531, bound_value=119:125284, second_product=238:126029, answer=224:123705)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `Walker`, `ait` (target ranks: base_value=64:10893, first_product=128:20906, bound_value=119:21339, second_product=238:23332, answer=224:22640)
- Layer 20: `}<?`, ` partly`, ` sideways`, `adaghan`, ` Extra` (target ranks: base_value=64:121701, first_product=128:126323, bound_value=119:113295, second_product=238:86889, answer=224:114967)
- Layer 30: `}<?`, `东京`, `dividers`, `codeline`, `lett` (target ranks: base_value=64:108368, first_product=128:111366, bound_value=119:110540, second_product=238:76047, answer=224:103689)
- Layer 35: `切割`, `锯`, `浪费`, `lett`, `ِّف` (target ranks: base_value=64:96409, first_product=128:105495, bound_value=119:110932, second_product=238:78195, answer=224:114713)
- Layer 36: `锯`, ` nasod`, `切割`, `足足`, ` reduct` (target ranks: base_value=64:36882, first_product=128:50781, bound_value=119:65751, second_product=238:30407, answer=224:83924)
- Layer 37: `}<?`, `磨损`, `在东`, `الميل`, `切割` (target ranks: base_value=64:76537, first_product=128:42223, bound_value=119:85319, second_product=238:33036, answer=224:76239)
- Layer 38: ` .`, `切割`, `遁`, ` .↵↵`, `lett` (target ranks: base_value=64:26644, first_product=128:24551, bound_value=119:63336, second_product=238:19500, answer=224:51578)
- Layer 39: ` .`, `替换`, `磨损`, `�`, ` Fusion` (target ranks: base_value=64:64098, first_product=128:39184, bound_value=119:97243, second_product=238:17550, answer=224:3803)
- Layer 40: ` .`, ` .↵↵`, ` nasod`, ` .↵`, `�` (target ranks: base_value=64:13054, first_product=128:8128, bound_value=119:51224, second_product=238:4498, answer=224:392)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, ` `, `<｜end▁of▁sentence｜>` (target ranks: base_value=64:1556, first_product=128:1248, bound_value=119:21086, second_product=238:535, answer=224:13)

### Filler position 48 (absolute token 843, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `aplenty` (target ranks: base_value=64:127513, first_product=128:126567, bound_value=119:125321, second_product=238:126119, answer=224:123756)
- Layer 10: `锁定`, ` Walker`, ` cheer`, `ait`, `Walker` (target ranks: base_value=64:10563, first_product=128:21415, bound_value=119:21545, second_product=238:23621, answer=224:23081)
- Layer 20: `东海`, ` instantaneous`, `aharoa`, `}<?`, `)Skip` (target ranks: base_value=64:110744, first_product=128:113028, bound_value=119:90860, second_product=238:92275, answer=224:111666)
- Layer 30: `codeline`, `东京`, `lett`, ` accompanying`, `切割` (target ranks: base_value=64:97904, first_product=128:105100, bound_value=119:98269, second_product=238:84289, answer=224:108501)
- Layer 35: `codeline`, ` nasod`, ` soci`, ` fif`, ` doubly` (target ranks: base_value=64:101554, first_product=128:105339, bound_value=119:111020, second_product=238:105461, answer=224:110684)
- Layer 36: ` nasod`, `兜`, ` reduct`, `yss`, ` soci` (target ranks: base_value=64:56515, first_product=128:64359, bound_value=119:83467, second_product=238:75590, answer=224:90615)
- Layer 37: `codeline`, `Quintal`, `悬挂`, `TreeLabel`, `zens` (target ranks: base_value=64:115010, first_product=128:88214, bound_value=119:109363, second_product=238:68073, answer=224:98454)
- Layer 38: ` .`, `悬挂`, `悬`, `肤`, ` crev` (target ranks: base_value=64:74303, first_product=128:86856, bound_value=119:85454, second_product=238:77961, answer=224:92460)
- Layer 39: ` encomp`, ` .`, ` .↵↵`, ` unflagged`, `贻` (target ranks: base_value=64:106312, first_product=128:93544, bound_value=119:103819, second_product=238:75669, answer=224:72452)
- Layer 40: ` .`, ` .↵↵`, ` .↵`, `肤`, ` nasod` (target ranks: base_value=64:77291, first_product=128:60422, bound_value=119:92819, second_product=238:58878, answer=224:35317)
- Layer 41: ` .`, ` .↵↵`, ` .↵`, `肤`, `圆圆` (target ranks: base_value=64:19339, first_product=128:9678, bound_value=119:32993, second_product=238:14707, answer=224:3127)

### Filler position 49 (absolute token 844, surface ` .`)

- Layer 0: `尷`, `?datasetId`, `Noiz`, `�乐`, `datasetId` (target ranks: base_value=64:127545, first_product=128:126628, bound_value=119:125433, second_product=238:126189, answer=224:123797)
- Layer 10: `锁定`, ` Walker`, `ait`, `Walker`, ` cheer` (target ranks: base_value=64:10827, first_product=128:22883, bound_value=119:23161, second_product=238:24639, answer=224:24538)
- Layer 20: ` licensierad`, `aplenty`, `codeline`, ` instantaneous`, `}<?` (target ranks: base_value=64:83964, first_product=128:88610, bound_value=119:93324, second_product=238:98000, answer=224:92810)
- Layer 30: ` Answer`, `答案是`, ` ответ`, `答案`, ` answer` (target ranks: base_value=64:86596, first_product=128:99665, bound_value=119:109970, second_product=238:117546, answer=224:89504)
- Layer 35: ` Answer`, `codeline`, `AED`, `oNames`, ` Antwort` (target ranks: base_value=64:112768, first_product=128:113615, bound_value=119:90619, second_product=238:121495, answer=224:107553)
- Layer 36: ` Answer`, `坏`, ` answer`, ` Antwort`, ` پاسخ` (target ranks: base_value=64:58029, first_product=128:48705, bound_value=119:45647, second_product=238:90851, answer=224:72838)
- Layer 37: `oNames`, `orbic`, `insic`, `codeline`, ` consum` (target ranks: base_value=64:122902, first_product=128:106895, bound_value=119:97298, second_product=238:116233, answer=224:100813)
- Layer 38: `oNames`, ` retard`, `.Advertisement`, `оду`, `园的` (target ranks: base_value=64:124664, first_product=128:110785, bound_value=119:90003, second_product=238:110206, answer=224:75162)
- Layer 39: `oxygen`, `�`, ` unflagged`, ` Douglass`, ` consonant` (target ranks: base_value=64:93410, first_product=128:111850, bound_value=119:112241, second_product=238:71478, answer=224:19995)
- Layer 40: ` Answer`, ` .`, ` .↵↵`, `丝的`, `框中` (target ranks: base_value=64:17784, first_product=128:60209, bound_value=119:60571, second_product=238:25376, answer=224:1723)
- Layer 41: ` .`, ` Answer`, ` .↵↵`, `Answer`, ` twenty` (target ranks: base_value=64:10468, first_product=128:36847, bound_value=119:41503, second_product=238:9616, answer=224:753)

### Filler position 50 (absolute token 845, surface ` .↵↵`)

- Layer 0: `aplenty`, `尷`, `�乐`, `EDMF`, `(migrations` (target ranks: base_value=64:122481, first_product=128:115220, bound_value=119:114801, second_product=238:110186, answer=224:113735)
- Layer 10: `EDMF`, ` dével`, `-ulo`, `�乐`, `aplenty` (target ranks: base_value=64:127063, first_product=128:117388, bound_value=119:120563, second_product=238:105601, answer=224:116433)
- Layer 20: `能被`, `ait`, ` Wik`, `忑`, `能吃` (target ranks: base_value=64:14218, first_product=128:41876, bound_value=119:77611, second_product=238:64978, answer=224:49056)
- Layer 30: `答案为`, `答案是`, `答案`, `回答`, `答え` (target ranks: base_value=64:65367, first_product=128:99964, bound_value=119:110178, second_product=238:103402, answer=224:106527)
- Layer 35: `解答`, `答案`, ` answer`, `答案是`, `计算结果` (target ranks: base_value=64:24989, first_product=128:59030, bound_value=119:50057, second_product=238:55162, answer=224:58461)
- Layer 36: `解答`, `答案`, `正确答案`, `计算`, `回答` (target ranks: base_value=64:14991, first_product=128:17998, bound_value=119:25758, second_product=238:29226, answer=224:34962)
- Layer 37: ` dátummal`, `-ulo`, ` Paglin`, `解答`, `polar` (target ranks: base_value=64:76105, first_product=128:69951, bound_value=119:78012, second_product=238:64969, answer=224:67330)
- Layer 38: `-ulo`, `oNames`, `解答`, `romes`, `lut` (target ranks: base_value=64:60468, first_product=128:58104, bound_value=119:53910, second_product=238:51326, answer=224:41475)
- Layer 39: `答案`, ` Answer`, ` Antwort`, ` উত্তর`, `Answer` (target ranks: base_value=64:102747, first_product=128:62309, bound_value=119:89875, second_product=238:25885, answer=224:521)
- Layer 40: `Answer`, ` Answer`, ` answer`, `答案`, `answer` (target ranks: base_value=64:71091, first_product=128:16028, bound_value=119:30928, second_product=238:2315, answer=224:29)
- Layer 41: `Answer`, ` Answer`, ` answer`, `答案`, `答` (target ranks: base_value=64:24495, first_product=128:10022, bound_value=119:14729, second_product=238:7509, answer=224:55)

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

Answer:<｜Assistant｜></think>178<｜end▁of▁sentence｜><｜User｜>niw = 20
kog = 37
suv = 64
woh = twice the number for suv minus 9
voz = twice the number for woh minus 15
Question: What is twice the number for woh minus 14?

Filler: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answer:<｜Assistant｜></think>
```

## Interpretation boundary

A high-ranked token is evidence about a token direction produced by average-Jacobian transport and the model's norm/unembedding. It is not a literal transcript of a private chain of thought. The square released lens also omits an explicit convention for reducing V4's four hyper-connection streams; see `compatibility.md`.
