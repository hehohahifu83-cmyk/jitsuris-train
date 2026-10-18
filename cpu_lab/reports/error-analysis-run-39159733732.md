# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-18T19:41:18+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 29 | 1 | 14 | 0 |
| business | blend70 | 2 | 490 | 23 | 3 | 14 | 1 |
| business | ft | 1 | 490 | 29 | 1 | 12 | 0 |
| business | ft | 2 | 490 | 26 | 3 | 10 | 1 |
| business2 | blend70 | 1 | 976 | 27 | 7 | 16 | 1 |
| business2 | blend70 | 2 | 976 | 23 | 6 | 17 | 3 |
| business2 | ft | 1 | 976 | 28 | 7 | 17 | 1 |
| business2 | ft | 2 | 976 | 25 | 6 | 16 | 3 |
| dev220 | blend70 | 1 | 220 | 7 | 1 | 3 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 0 | 3 | 0 |
| dev220 | ft | 2 | 220 | 7 | 1 | 0 | 0 |
| general | blend70 | 1 | 383 | 6 | 1 | 21 | 5 |
| general | blend70 | 2 | 383 | 6 | 0 | 13 | 8 |
| general | ft | 1 | 383 | 8 | 1 | 19 | 5 |
| general | ft | 2 | 383 | 5 | 0 | 14 | 8 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 23, org→account: 9, category→account: 3, quantity→amount: 2, org→address: 2, text→account: 2, account→category: 2, org→category: 2
- business / ft: category→quantity: 26, org→account: 9, account→text: 3, category→account: 3, quantity→amount: 2, org→address: 2, text→account: 2, account→category: 2
- business2 / blend70: amount→quantity: 7, quantity→address: 5, id→category: 4, quantity→amount: 4, category→id: 4, category→quantity: 4, account→category: 3, quantity→category: 3
- business2 / ft: amount→quantity: 7, category→id: 5, quantity→address: 5, id→category: 4, quantity→amount: 4, category→quantity: 4, account→category: 3, quantity→category: 3
- dev220 / blend70: category→text: 4, quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→account: 1, rate→tax_class: 1
- dev220 / ft: quantity→category: 4, category→text: 3, rate→tax_class: 2, category→tax_class: 2, org→account: 1, id→quantity: 1
- general / blend70: category→text: 2, org→address: 2, quantity→category: 2, id→address: 2, address→category: 1, id→quantity: 1, text→category: 1, id→category: 1
- general / ft: category→text: 3, org→address: 2, text→category: 2, id→address: 2, quantity→category: 1, address→category: 1, id→quantity: 1, id→category: 1

### seedをまたいで再発した誤り

- business / blend70: `d2`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `portefeuille_nom_et_code`、org→category（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `title`、category→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d2`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `portefeuille_nom_et_code`、org→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `title`、category→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→text（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `value`、amount→rate（seed 1, seed 2）
- business2 / blend70: `value`、quantity→amount（seed 1, seed 2）
- business2 / ft: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `value`、amount→rate（seed 1, seed 2）
- business2 / ft: `value`、quantity→amount（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `payment terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `payment terms`、category→text（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `税率`、rate→tax_class（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9976 | yes |
| unknown | business | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6211 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.2309 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9985 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9671 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.6755 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.5764 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.4639 | no |
| unknown | business | blend70 | 1 | q1a | category | unknown | 0.4938 | no |
| unknown | business | blend70 | 1 | q3_2 | category | unknown | 0.6699 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9973 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9927 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.7381 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9925 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9529 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.5952 | no |
| wrong | business | blend70 | 1 | class-title_en | category | text | 0.5861 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6955 | no |
| wrong | business | blend70 | 1 | d2 | category | quantity | 0.6803 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7442 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9949 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8842 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.5819 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9965 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6857 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.5365 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | category | 0.5361 | no |
| wrong | business | blend70 | 1 | procurementclassification:proclasslabel | account | category | 0.7245 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.7172 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9800 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7019 | no |
| wrong | business | blend70 | 1 | q2b | category | quantity | 0.6903 | no |
| wrong | business | blend70 | 1 | q2c | category | quantity | 0.5906 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.6933 | no |
| wrong | business | blend70 | 1 | q4a | category | quantity | 0.6903 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | quantity | 0.7877 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.7021 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.7047 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7062 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7205 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.6679 | no |
| wrong | business | blend70 | 1 | regrp_nom | account | text | 0.7393 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.6658 | no |
| critical | business | blend70 | 2 | mois calendrier | date | quantity | 0.9081 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.5414 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9963 | yes |
| other_ng | business | blend70 | 2 | km budgété | other | quantity | 0.6632 | no |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.3811 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4330 | no |
| unknown | business | blend70 | 2 | d1 | category | unknown | 0.4527 | no |
| unknown | business | blend70 | 2 | d6 | category | unknown | 0.4351 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9986 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9677 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.5143 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.4826 | no |
| unknown | business | blend70 | 2 | q5b | category | unknown | 0.4893 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9973 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9924 | no |
| unknown | business | blend70 | 2 | segment-title_fr | category | unknown | 0.4709 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9920 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9517 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.7063 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9949 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8551 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9964 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8530 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.6600 | no |
| wrong | business | blend70 | 2 | merchant details | text | org | 0.7439 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | category | 0.6419 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7149 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9819 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6968 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6898 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6992 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6143 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.7084 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7234 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7195 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.5019 | no |
| wrong | business | blend70 | 2 | sub_category | category | account | 0.6420 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.5911 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9986 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.3299 | no |
| unknown | business | ft | 1 | commodity | id | unknown | 0.3569 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9969 | no |
| unknown | business | ft | 1 | ligne | category | unknown | 0.9492 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.8148 | no |
| unknown | business | ft | 1 | q3_2 | category | unknown | 0.9547 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9990 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9992 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.9887 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9980 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9975 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.8139 | no |
| wrong | business | ft | 1 | class-title_en | category | text | 0.5053 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9883 | no |
| wrong | business | ft | 1 | d2 | category | quantity | 0.9278 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9895 | no |
| wrong | business | ft | 1 | department | org | account | 0.9984 | no |
| wrong | business | ft | 1 | department | org | account | 0.9946 | no |
| wrong | business | ft | 1 | department | org | account | 0.7586 | no |
| wrong | business | ft | 1 | department | org | account | 0.9986 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.9777 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | category | 0.7633 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.9799 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9976 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9935 | no |
| wrong | business | ft | 1 | q1a | category | quantity | 0.7045 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9918 | no |
| wrong | business | ft | 1 | q2b | category | quantity | 0.9774 | no |
| wrong | business | ft | 1 | q2c | category | quantity | 0.8407 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9820 | no |
| wrong | business | ft | 1 | q4a | category | quantity | 0.9847 | no |
| wrong | business | ft | 1 | q4b_1 | category | quantity | 0.9886 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9980 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9983 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9936 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9935 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9225 | no |
| wrong | business | ft | 1 | regrp_nom | account | text | 0.9297 | no |
| wrong | business | ft | 1 | title | category | account | 0.9309 | no |
| critical | business | ft | 2 | mois calendrier | date | quantity | 0.9671 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.7733 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.9968 | yes |
| other_ng | business | ft | 2 | km budgété | other | quantity | 0.9398 | no |
| unknown | business | ft | 2 | australian sourced goods | amount | unknown | 0.3744 | no |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.4059 | no |
| unknown | business | ft | 2 | d6 | category | unknown | 0.5480 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9991 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9977 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.7189 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9990 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9988 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9973 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9959 | no |
| wrong | business | ft | 2 | account_name | account | text | 0.5449 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.5750 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.9650 | no |
| wrong | business | ft | 2 | department | org | account | 0.9984 | no |
| wrong | business | ft | 2 | department | org | account | 0.9529 | no |
| wrong | business | ft | 2 | department | org | account | 0.9984 | no |
| wrong | business | ft | 2 | description | account | text | 0.9943 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.9410 | no |
| wrong | business | ft | 2 | merchant details | text | org | 0.9642 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | category | 0.9144 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9942 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9961 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9845 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9771 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9909 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.8726 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.6370 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9968 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9976 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9962 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.6443 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.7787 | no |
| wrong | business | ft | 2 | title | category | account | 0.8242 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7287 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9916 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9484 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8497 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9976 | yes |
| critical | business2 | blend70 | 1 | value | amount | rate | 0.9949 | yes |
| critical | business2 | blend70 | 1 | value | quantity | amount | 0.9604 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.8356 | no |
| unknown | business2 | blend70 | 1 | apartment | quantity | unknown | 0.4665 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9738 | no |
| unknown | business2 | blend70 | 1 | imd19_income_decile | category | unknown | 0.3995 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9978 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 1 | value | quantity | unknown | 0.5049 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9993 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9949 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9981 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9901 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8357 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.5832 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.9381 | no |
| wrong | business2 | blend70 | 1 | household income decile | category | address | 0.7929 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6990 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.7220 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9863 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6891 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6842 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7599 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7395 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9611 | no |
| wrong | business2 | blend70 | 1 | scheme_description | category | text | 0.7406 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6908 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6765 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6968 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6970 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6156 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9670 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.5589 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.6860 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9918 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8480 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.9961 | yes |
| critical | business2 | blend70 | 2 | value | amount | rate | 0.9952 | yes |
| critical | business2 | blend70 | 2 | value | quantity | amount | 0.9534 | yes |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.6902 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.6093 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.9509 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4566 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4651 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.8293 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.6855 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5301 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9948 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9902 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.5009 | no |
| wrong | business2 | blend70 | 2 | apartment | quantity | address | 0.5944 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | quantity | 0.6605 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6529 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7687 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8942 | no |
| wrong | business2 | blend70 | 2 | name of the building/land or both | address | org | 0.5887 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.6389 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6910 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6904 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7055 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9766 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5910 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.6865 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6865 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6873 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9670 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9971 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9986 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9678 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9964 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9986 | yes |
| critical | business2 | ft | 1 | value | amount | rate | 0.9975 | yes |
| critical | business2 | ft | 1 | value | quantity | amount | 0.9869 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.8262 | no |
| unknown | business2 | ft | 1 | apartment | quantity | unknown | 0.4977 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9907 | no |
| unknown | business2 | ft | 1 | household disposable income quintiles | category | unknown | 0.4266 | no |
| unknown | business2 | ft | 1 | item | category | unknown | 0.4943 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9979 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | value | quantity | unknown | 0.4510 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9983 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9979 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9990 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9185 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.8112 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.9917 | no |
| wrong | business2 | ft | 1 | household income decile | category | address | 0.9082 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.5707 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9985 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.9068 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.9951 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9750 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9771 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9982 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9987 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9667 | no |
| wrong | business2 | ft | 1 | scheme_description | category | text | 0.6320 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.9861 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.9452 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9949 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9955 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.8264 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9991 | no |
| wrong | business2 | ft | 1 | type of expenditure | account | category | 0.5462 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.9360 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9988 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9940 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.9965 | yes |
| critical | business2 | ft | 2 | value | amount | rate | 0.9979 | yes |
| critical | business2 | ft | 2 | value | quantity | amount | 0.9768 | yes |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.6366 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.7771 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9910 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.7842 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.4987 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.9775 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4970 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9982 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9980 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9990 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.7152 | no |
| wrong | business2 | ft | 2 | amt-units_mnt-unite | category | id | 0.5245 | no |
| wrong | business2 | ft | 2 | apartment | quantity | address | 0.8487 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.6425 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | quantity | 0.9164 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9327 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9735 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9870 | no |
| wrong | business2 | ft | 2 | name of the building/land or both | address | org | 0.8355 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9777 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8989 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9501 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9888 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8425 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.9594 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9802 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9816 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9991 | no |
| wrong | business2 | ft | 2 | want to live in this parish & band b | quantity | category | 0.5624 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.6540 | yes |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.6884 | no |
| unknown | dev220 | blend70 | 1 | 支払を受ける者の個人番号 | id | unknown | 0.7016 | no |
| unknown | dev220 | blend70 | 1 | 税率 | rate | unknown | 0.4957 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8133 | no |
| wrong | dev220 | blend70 | 1 | payment terms | category | text | 0.6760 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7277 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.8212 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.5164 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7286 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9359 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8431 | no |
| wrong | dev220 | blend70 | 2 | payment terms | category | text | 0.6585 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7334 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.8250 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.8491 | no |
| wrong | dev220 | blend70 | 2 | 税率 | rate | tax_class | 0.5864 | no |
| unknown | dev220 | ft | 1 | purchase order by customer | id | unknown | 0.5921 | no |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.9814 | no |
| unknown | dev220 | ft | 1 | 支払を受ける者の個人番号 | id | unknown | 0.9939 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.7916 | no |
| wrong | dev220 | ft | 1 | payment terms | category | text | 0.9641 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9556 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.7508 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9970 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.6845 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9948 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8343 | no |
| wrong | dev220 | ft | 2 | payment terms | category | text | 0.9390 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9638 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.7562 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.8901 | no |
| wrong | dev220 | ft | 2 | 税率 | rate | tax_class | 0.8272 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.6210 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.8698 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.5532 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9669 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9189 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9973 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8934 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.4404 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.4317 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.5222 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.6166 | no |
| unknown | general | blend70 | 1 | bib | id | unknown | 0.5453 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.7378 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9494 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9881 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.6214 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6994 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4791 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4974 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.7019 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.6751 | no |
| unknown | general | blend70 | 1 | units | category | unknown | 0.4701 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.6337 | no |
| unknown | general | blend70 | 1 | 東第5 | quantity | unknown | 0.6890 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9656 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9995 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9751 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9313 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7365 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.9684 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7109 | no |
| wrong | general | blend70 | 1 | 読み方 | address | category | 0.6585 | no |
| other_ng | general | blend70 | 2 | _status_ | other | category | 0.6222 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9249 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.7748 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.5992 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9735 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6577 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9436 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9911 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8910 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.6212 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9497 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9881 | no |
| unknown | general | blend70 | 2 | ngram | text | unknown | 0.4033 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.7022 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.3919 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7479 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.5089 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9653 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9742 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.3903 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.9813 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.8684 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9074 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.5340 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6191 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7106 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.8697 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8838 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.7851 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9773 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9560 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9980 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9977 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.4947 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.8600 | no |
| unknown | general | ft | 1 | bib | id | unknown | 0.4496 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.8257 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9986 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9983 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8633 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9279 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.3260 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.7105 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.9572 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.9245 | no |
| unknown | general | ft | 1 | units | category | unknown | 0.6612 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.8955 | no |
| unknown | general | ft | 1 | 東第5 | quantity | unknown | 0.9840 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9990 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9993 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9975 | no |
| wrong | general | ft | 1 | element_char | category | text | 0.5915 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9673 | no |
| wrong | general | ft | 1 | place | org | address | 0.9852 | no |
| wrong | general | ft | 1 | term | text | category | 0.6759 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9799 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9983 | no |
| wrong | general | ft | 1 | 読み方 | address | category | 0.9399 | no |
| other_ng | general | ft | 2 | _status_ | other | category | 0.8876 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9625 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.9905 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8508 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9868 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9333 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9913 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9892 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9943 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.6591 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9990 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9982 | no |
| unknown | general | ft | 2 | ngram | text | unknown | 0.4525 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9786 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.5591 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9973 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.7269 | no |
| unknown | general | ft | 2 | year_step_size | quantity | unknown | 0.4809 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9986 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9992 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9962 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.5560 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.9895 | no |
| wrong | general | ft | 2 | goal | id | category | 0.8375 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9332 | no |
| wrong | general | ft | 2 | place | org | address | 0.6958 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9979 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9968 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9965 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9988 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9984 | no |

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 39件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 153件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 112件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行は学習データへコピーしない。出典独立の公開/合成教材を、ラベル定義と根拠付きで監査してから使う。
2. GPUの基準条件は維持し、次の比較では訓練時の表現拡張（FT_AUG=1）だけを追加する。seed 1/2を両条件で比較する。
3. 固定5セットのaccuracy・errors・critical errors・unknownsに加え、時間・最大GPUメモリを回収する。1.5ポイント未満は差なしとする。
4. 原因が確定したとみなすのは、同じ失敗パターンの再検査と改善の再現が取れた場合だけ。ラベル変更・自動自己ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
