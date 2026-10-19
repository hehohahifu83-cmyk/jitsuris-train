# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-19T01:51:36+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 30 | 4 | 11 | 1 |
| business | blend70 | 2 | 490 | 27 | 7 | 9 | 0 |
| business | ft | 1 | 490 | 31 | 4 | 10 | 1 |
| business | ft | 2 | 490 | 27 | 7 | 9 | 0 |
| business2 | blend70 | 1 | 976 | 15 | 4 | 19 | 3 |
| business2 | blend70 | 2 | 976 | 18 | 4 | 19 | 3 |
| business2 | ft | 1 | 976 | 14 | 3 | 22 | 3 |
| business2 | ft | 2 | 976 | 20 | 4 | 17 | 3 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 6 | 0 | 3 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 8 | 0 | 2 | 0 |
| general | blend70 | 1 | 383 | 11 | 2 | 13 | 6 |
| general | blend70 | 2 | 383 | 14 | 2 | 10 | 8 |
| general | ft | 1 | 383 | 12 | 3 | 10 | 6 |
| general | ft | 2 | 383 | 16 | 3 | 8 | 8 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 22, org→account: 6, amount→id: 6, category→account: 4, category→text: 4, quantity→amount: 3, account→text: 2, product→text: 2
- business / ft: category→quantity: 22, org→account: 7, amount→id: 6, category→account: 5, category→text: 4, quantity→amount: 3, account→text: 2, amount→quantity: 2
- business2 / blend70: category→quantity: 6, category→text: 4, account→category: 3, amount→quantity: 3, quantity→amount: 3, id→quantity: 2, category→account: 2, id→category: 2
- business2 / ft: category→quantity: 6, category→text: 3, account→category: 3, quantity→amount: 3, quantity→address: 3, id→quantity: 2, amount→quantity: 2, category→account: 2
- dev220 / blend70: org→account: 3, category→tax_class: 2, quantity→category: 2, org→address: 1, id→quantity: 1, address→id: 1, category→text: 1, category→account: 1
- dev220 / ft: org→account: 3, quantity→category: 3, org→address: 2, category→tax_class: 2, id→quantity: 1, address→id: 1, category→text: 1, category→account: 1
- general / blend70: category→text: 7, quantity→category: 3, text→category: 3, org→address: 2, id→address: 2, category→quantity: 2, address→org: 2, id→quantity: 2
- general / ft: category→text: 7, quantity→category: 3, amount→id: 3, text→category: 3, org→address: 2, id→address: 2, category→quantity: 2, address→org: 2

### seedをまたいで再発した誤り

- business / blend70: `agebann`、category→quantity（seed 1, seed 2）
- business / blend70: `australian sourced goods`、amount→id（seed 1, seed 2）
- business / blend70: `australian sourced services`、amount→id（seed 1, seed 2）
- business / blend70: `commodity-title_en`、product→text（seed 1, seed 2）
- business / blend70: `d1`、category→quantity（seed 1, seed 2）
- business / blend70: `d2`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `sub_category`、category→account（seed 1, seed 2）
- business / blend70: `title`、category→text（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `australian sourced goods`、amount→id（seed 1, seed 2）
- business / ft: `australian sourced services`、amount→id（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d2`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `segment-title_fr`、category→account（seed 1, seed 2）
- business / ft: `sub_category`、category→account（seed 1, seed 2）
- business / ft: `title`、category→text（seed 1, seed 2）
- business2 / blend70: `contravention`、category→text（seed 1, seed 2）
- business2 / blend70: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `programme`、category→account（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `contravention`、category→text（seed 1, seed 2）
- business2 / ft: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→quantity（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `programme`、category→account（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service`、account→address（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `location`、org→address（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend70: `attrition`、category→quantity（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `goal`、id→quantity（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `読み方`、address→org（seed 1, seed 2）
- general / ft: `attrition`、category→quantity（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `介護費`、amount→id（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）
- general / ft: `読み方`、address→org（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend70 | 1 | australian sourced goods | amount | id | 0.7962 | yes |
| critical | business | blend70 | 1 | australian sourced services | amount | id | 0.9477 | yes |
| critical | business | blend70 | 1 | overseas sourced goods | amount | quantity | 0.5130 | yes |
| critical | business | blend70 | 1 | overseas sourced services | amount | quantity | 0.6497 | yes |
| other_ng | business | blend70 | 1 | km budgété | other | quantity | 0.6080 | no |
| unknown | business | blend70 | 1 | all p-cards payments for february 2022 | org | unknown | 0.4257 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4716 | no |
| unknown | business | blend70 | 1 | family-title_fr | category | unknown | 0.4875 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9982 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9678 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7053 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9954 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9928 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.6991 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9934 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9540 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.7179 | no |
| wrong | business | blend70 | 1 | capital revenue | category | account | 0.7780 | no |
| wrong | business | blend70 | 1 | class-title_en | category | text | 0.8963 | no |
| wrong | business | blend70 | 1 | class-title_fr | category | text | 0.9196 | no |
| wrong | business | blend70 | 1 | commodity-title_en | product | text | 0.7136 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.7002 | no |
| wrong | business | blend70 | 1 | d2 | category | quantity | 0.6726 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7502 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9953 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8576 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9971 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8539 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6399 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.7001 | no |
| wrong | business | blend70 | 1 | procurementclassification:proclasslabel | account | category | 0.7383 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7053 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.6845 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.6496 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6886 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6772 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7093 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7240 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7210 | no |
| wrong | business | blend70 | 1 | segment-title_fr | category | account | 0.6963 | no |
| wrong | business | blend70 | 1 | sub_category | category | account | 0.7902 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.8951 | no |
| critical | business | blend70 | 2 | # invoices paid within 30 days | quantity | amount | 0.9900 | yes |
| critical | business | blend70 | 2 | # invoices paid within 5 days | quantity | amount | 0.9876 | yes |
| critical | business | blend70 | 2 | australian sourced goods | amount | id | 0.8174 | yes |
| critical | business | blend70 | 2 | australian sourced services | amount | id | 0.9699 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | id | 0.7483 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | id | 0.8216 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9984 | yes |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9990 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9691 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7058 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9975 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9931 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4264 | no |
| unknown | business | blend70 | 2 | segment-title_fr | category | unknown | 0.4683 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9934 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9539 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.7218 | no |
| wrong | business | blend70 | 2 | commodity-title_en | product | text | 0.5716 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.7010 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.6206 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7483 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9951 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9972 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6878 | no |
| wrong | business | blend70 | 2 | merchant details | text | product | 0.5940 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.9873 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7083 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9841 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.5762 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6604 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.5278 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.5751 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7228 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7025 | no |
| wrong | business | blend70 | 2 | sub_category | category | account | 0.7843 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.9474 | no |
| critical | business | ft | 1 | australian sourced goods | amount | id | 0.9674 | yes |
| critical | business | ft | 1 | australian sourced services | amount | id | 0.9634 | yes |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.7328 | yes |
| critical | business | ft | 1 | overseas sourced services | amount | quantity | 0.9181 | yes |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.8610 | no |
| unknown | business | ft | 1 | all p-cards payments for february 2022 | org | unknown | 0.4149 | no |
| unknown | business | ft | 1 | family-title_fr | category | unknown | 0.4066 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9985 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9979 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9990 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9963 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9992 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.9987 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9993 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9991 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.9892 | no |
| wrong | business | ft | 1 | capital revenue | category | account | 0.9979 | no |
| wrong | business | ft | 1 | class-title_en | category | text | 0.9484 | no |
| wrong | business | ft | 1 | class-title_fr | category | text | 0.9830 | no |
| wrong | business | ft | 1 | commodity-title_en | product | text | 0.6929 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9950 | no |
| wrong | business | ft | 1 | d2 | category | quantity | 0.9168 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9981 | no |
| wrong | business | ft | 1 | department | org | account | 0.9991 | no |
| wrong | business | ft | 1 | department | org | account | 0.9565 | no |
| wrong | business | ft | 1 | department | org | account | 0.9994 | no |
| wrong | business | ft | 1 | description | account | text | 0.9956 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.6718 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9079 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.6727 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.9995 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9965 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9694 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.9201 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9788 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9590 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9981 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9986 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9984 | no |
| wrong | business | ft | 1 | segment-title_fr | category | account | 0.9305 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.9904 | no |
| wrong | business | ft | 1 | title | category | text | 0.9152 | no |
| critical | business | ft | 2 | # invoices paid within 30 days | quantity | amount | 0.9987 | yes |
| critical | business | ft | 2 | # invoices paid within 5 days | quantity | amount | 0.9981 | yes |
| critical | business | ft | 2 | australian sourced goods | amount | id | 0.9978 | yes |
| critical | business | ft | 2 | australian sourced services | amount | id | 0.9952 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | id | 0.9358 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | id | 0.8955 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.9998 | yes |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4899 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9997 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9997 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9997 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9993 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9998 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.6091 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9993 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9990 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.9948 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.9961 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.8426 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9953 | no |
| wrong | business | ft | 2 | department | org | account | 0.9988 | no |
| wrong | business | ft | 2 | department | org | account | 0.9996 | no |
| wrong | business | ft | 2 | description | account | text | 0.7583 | no |
| wrong | business | ft | 2 | merchant details | text | product | 0.8485 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.9931 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9848 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9992 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.8122 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9350 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.7460 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.8064 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9968 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9719 | no |
| wrong | business | ft | 2 | segment-title_fr | category | account | 0.6047 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.9819 | no |
| wrong | business | ft | 2 | title | category | text | 0.9899 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7298 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.6649 | yes |
| critical | business2 | blend70 | 1 | monitor | id | quantity | 0.8313 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9696 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9407 | no |
| other_ng | business2 | blend70 | 1 | epc_score | other | quantity | 0.7130 | no |
| other_ng | business2 | blend70 | 1 | potential_epc_score | other | quantity | 0.7045 | no |
| unknown | business2 | blend70 | 1 | contravention | category | unknown | 0.6619 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9998 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9799 | no |
| unknown | business2 | blend70 | 1 | household disposable income quintiles | category | unknown | 0.6980 | no |
| unknown | business2 | blend70 | 1 | household income decile | category | unknown | 0.4384 | no |
| unknown | business2 | blend70 | 1 | imd19_income_decile | category | unknown | 0.3829 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.7059 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9990 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9970 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.7010 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9958 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9993 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9906 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.9371 | no |
| wrong | business2 | blend70 | 1 | epc_score_known | category | quantity | 0.7151 | no |
| wrong | business2 | blend70 | 1 | imd19_national_decile | category | quantity | 0.6976 | no |
| wrong | business2 | blend70 | 1 | merchant description | category | text | 0.6881 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.9026 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7061 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6837 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9832 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6917 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9652 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.7819 | no |
| critical | business2 | blend70 | 2 | # invoices paid within 30 days | quantity | amount | 0.9898 | yes |
| critical | business2 | blend70 | 2 | # invoices paid within 5 days | quantity | amount | 0.9880 | yes |
| critical | business2 | blend70 | 2 | monitor | id | quantity | 0.8269 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.9984 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.9535 | no |
| other_ng | business2 | blend70 | 2 | epc_score | other | quantity | 0.7206 | no |
| other_ng | business2 | blend70 | 2 | potential_epc_score | other | quantity | 0.7162 | no |
| unknown | business2 | blend70 | 2 | apartment | quantity | unknown | 0.4072 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9998 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9801 | no |
| unknown | business2 | blend70 | 2 | imd19_national_decile | category | unknown | 0.8034 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.7080 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9991 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4848 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4455 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9990 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9970 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.7184 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9997 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9959 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9907 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.8457 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.7244 | no |
| wrong | business2 | blend70 | 2 | fine | amount | category | 0.8195 | no |
| wrong | business2 | blend70 | 2 | health service executive area | address | org | 0.8942 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6988 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8935 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7063 | no |
| wrong | business2 | blend70 | 2 | potential_epc_score_known | category | quantity | 0.6922 | no |
| wrong | business2 | blend70 | 2 | programme | category | account | 0.6792 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9811 | no |
| wrong | business2 | blend70 | 2 | scheme_description | category | text | 0.6386 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6063 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.8449 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | account | 0.9299 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9986 | yes |
| critical | business2 | ft | 1 | monitor | id | quantity | 0.9921 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9980 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9764 | no |
| other_ng | business2 | ft | 1 | epc_score | other | quantity | 0.9856 | no |
| other_ng | business2 | ft | 1 | potential_epc_score | other | quantity | 0.9826 | no |
| unknown | business2 | ft | 1 | contravention | category | unknown | 0.9456 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9998 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | household disposable income quintiles | category | unknown | 0.9969 | no |
| unknown | business2 | ft | 1 | household income decile | category | unknown | 0.4885 | no |
| unknown | business2 | ft | 1 | imd19_income_decile | category | unknown | 0.5198 | no |
| unknown | business2 | ft | 1 | miscellaneous_divers | amount | unknown | 0.5318 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9999 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.9962 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.4571 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.4951 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.9955 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9999 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9997 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9997 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9996 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.9902 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.9813 | no |
| wrong | business2 | ft | 1 | imd19_national_decile | category | quantity | 0.8775 | no |
| wrong | business2 | ft | 1 | merchant description | category | text | 0.9803 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.9991 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9993 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9764 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9982 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.9874 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9965 | no |
| wrong | business2 | ft | 1 | type of expenditure | account | category | 0.8648 | no |
| critical | business2 | ft | 2 | # invoices paid within 30 days | quantity | amount | 0.9984 | yes |
| critical | business2 | ft | 2 | # invoices paid within 5 days | quantity | amount | 0.9987 | yes |
| critical | business2 | ft | 2 | monitor | id | quantity | 0.9858 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.9998 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9946 | no |
| other_ng | business2 | ft | 2 | epc_score | other | quantity | 0.9965 | no |
| other_ng | business2 | ft | 2 | potential_epc_score | other | quantity | 0.9993 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9998 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9996 | no |
| unknown | business2 | ft | 2 | imd19_national_decile | category | unknown | 0.9014 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9998 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9996 | no |
| unknown | business2 | ft | 2 | scheme_description | category | unknown | 0.4862 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9997 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9996 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9997 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9997 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9997 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.9980 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9998 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9997 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9997 | no |
| wrong | business2 | ft | 2 | apartment | quantity | address | 0.5812 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.8597 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.9945 | no |
| wrong | business2 | ft | 2 | fine | amount | category | 0.9931 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.9969 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.9983 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9861 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9996 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.9750 | no |
| wrong | business2 | ft | 2 | programme | category | account | 0.9700 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9953 | no |
| wrong | business2 | ft | 2 | service | account | address | 0.6918 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.6359 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8660 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.8247 | no |
| wrong | business2 | ft | 2 | warddesc | address | account | 0.9986 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9390 | yes |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.6923 | no |
| unknown | dev220 | blend70 | 1 | 支払を受ける者の個人番号 | id | unknown | 0.7040 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8730 | no |
| wrong | dev220 | blend70 | 1 | location | org | address | 0.5531 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7444 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.9874 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7180 | no |
| unknown | dev220 | blend70 | 2 | customer rank | quantity | unknown | 0.5688 | no |
| unknown | dev220 | blend70 | 2 | purchase order by customer | id | unknown | 0.3712 | no |
| unknown | dev220 | blend70 | 2 | supplier rank | quantity | unknown | 0.4564 | no |
| wrong | dev220 | blend70 | 2 | division | category | account | 0.7019 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9949 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.7861 | no |
| wrong | dev220 | blend70 | 2 | 履行場所 | address | id | 0.6768 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7299 | no |
| wrong | dev220 | blend70 | 2 | 担当部局 | org | account | 0.6622 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9993 | yes |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.9869 | no |
| unknown | dev220 | ft | 1 | 支払を受ける者の個人番号 | id | unknown | 0.9973 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8769 | no |
| wrong | dev220 | ft | 1 | location | org | address | 0.7900 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9796 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.9882 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9820 | no |
| unknown | dev220 | ft | 2 | customer rank | quantity | unknown | 0.7827 | no |
| unknown | dev220 | ft | 2 | purchase order by customer | id | unknown | 0.4544 | no |
| wrong | dev220 | ft | 2 | division | category | account | 0.9946 | no |
| wrong | dev220 | ft | 2 | location | org | address | 0.5545 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.5682 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9990 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.8001 | no |
| wrong | dev220 | ft | 2 | 履行場所 | address | id | 0.5976 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.9989 | no |
| wrong | dev220 | ft | 2 | 担当部局 | org | account | 0.9430 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.7115 | yes |
| critical | general | blend70 | 1 | 介護費 | amount | id | 0.7614 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.8950 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7365 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.7033 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9813 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9493 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9980 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8947 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.5292 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.5498 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8590 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9501 | no |
| unknown | general | blend70 | 1 | funding | amount | unknown | 0.5540 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9851 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.4589 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3603 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.6894 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9661 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9998 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9761 | no |
| wrong | general | blend70 | 1 | attrition | category | quantity | 0.5098 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.8688 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9532 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7450 | no |
| wrong | general | blend70 | 1 | property | category | text | 0.6156 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.9589 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.5644 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7109 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.8269 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | amount | 0.5360 | yes |
| critical | general | blend70 | 2 | goal | id | quantity | 0.7056 | yes |
| other_ng | general | blend70 | 2 | _status_ | other | category | 0.6688 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9467 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6997 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.8625 | no |
| other_ng | general | blend70 | 2 | nodes | other | category | 0.7530 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.5243 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9411 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9985 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8944 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.9014 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.9465 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.9554 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9500 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.4433 | no |
| unknown | general | blend70 | 2 | 介護費 | amount | unknown | 0.5049 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9661 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9998 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9762 | no |
| wrong | general | blend70 | 2 | attrition | category | quantity | 0.7009 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.9854 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.8704 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7328 | no |
| wrong | general | blend70 | 2 | raw | category | text | 0.8600 | no |
| wrong | general | blend70 | 2 | source_value | category | text | 0.5372 | no |
| wrong | general | blend70 | 2 | term | text | category | 0.7013 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8295 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.5561 | no |
| wrong | general | blend70 | 2 | 住家全壊 | quantity | category | 0.6256 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7112 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.8296 | no |
| critical | general | ft | 1 | funding | amount | id | 0.7777 | yes |
| critical | general | ft | 1 | goal | id | quantity | 0.9989 | yes |
| critical | general | ft | 1 | 介護費 | amount | id | 0.9991 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9198 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.9358 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.9996 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9979 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9994 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9990 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9996 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.7644 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9987 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9997 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9939 | no |
| unknown | general | ft | 1 | study | text | unknown | 0.4095 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.9751 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9997 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9997 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9990 | no |
| wrong | general | ft | 1 | attrition | category | quantity | 0.7248 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.8287 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9987 | no |
| wrong | general | ft | 1 | place | org | address | 0.9973 | no |
| wrong | general | ft | 1 | property | category | text | 0.8528 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9663 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.7987 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9983 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.9814 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | amount | 0.7649 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.9904 | yes |
| critical | general | ft | 2 | 介護費 | amount | id | 0.6326 | yes |
| other_ng | general | ft | 2 | _status_ | other | category | 0.9542 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9936 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.9944 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.8281 | no |
| other_ng | general | ft | 2 | nodes | other | category | 0.9993 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.7427 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9877 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9998 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9992 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.9659 | no |
| unknown | general | ft | 2 | age_q3 | quantity | unknown | 0.9994 | no |
| unknown | general | ft | 2 | age_q3_nd | quantity | unknown | 0.9969 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9995 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9997 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9998 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9991 | no |
| wrong | general | ft | 2 | attrition | category | quantity | 0.9979 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.9952 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.8803 | no |
| wrong | general | ft | 2 | place | org | address | 0.9799 | no |
| wrong | general | ft | 2 | raw | category | text | 0.8217 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.7638 | no |
| wrong | general | ft | 2 | study | text | id | 0.5917 | no |
| wrong | general | ft | 2 | term | text | category | 0.9998 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7814 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.7869 | no |
| wrong | general | ft | 2 | 住家全壊 | quantity | category | 0.8929 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9987 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.9852 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9971 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9970 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9993 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9991 | no |

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 49件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 147件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 120件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
