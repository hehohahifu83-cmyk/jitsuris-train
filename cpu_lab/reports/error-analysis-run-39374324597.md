# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-20T05:48:44+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 13 | 2 | 30 | 0 |
| business | blend50 | 2 | 490 | 16 | 3 | 29 | 0 |
| business | blend60 | 1 | 490 | 19 | 2 | 24 | 0 |
| business | blend60 | 2 | 490 | 26 | 5 | 17 | 0 |
| business | blend70 | 1 | 490 | 22 | 2 | 17 | 0 |
| business | blend70 | 2 | 490 | 29 | 6 | 12 | 0 |
| business | ft | 1 | 490 | 27 | 1 | 13 | 0 |
| business | ft | 2 | 490 | 33 | 7 | 9 | 1 |
| business2 | blend50 | 1 | 976 | 15 | 2 | 35 | 5 |
| business2 | blend50 | 2 | 976 | 16 | 4 | 37 | 4 |
| business2 | blend60 | 1 | 976 | 19 | 3 | 31 | 2 |
| business2 | blend60 | 2 | 976 | 20 | 4 | 33 | 4 |
| business2 | blend70 | 1 | 976 | 19 | 3 | 26 | 3 |
| business2 | blend70 | 2 | 976 | 24 | 5 | 21 | 6 |
| business2 | ft | 1 | 976 | 26 | 3 | 20 | 4 |
| business2 | ft | 2 | 976 | 27 | 4 | 20 | 9 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 4 | 0 |
| dev220 | blend50 | 2 | 220 | 6 | 1 | 3 | 0 |
| dev220 | blend60 | 1 | 220 | 7 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 8 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 8 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 0 | 0 |
| general | blend50 | 1 | 383 | 9 | 0 | 22 | 4 |
| general | blend50 | 2 | 383 | 5 | 0 | 25 | 4 |
| general | blend60 | 1 | 383 | 9 | 0 | 16 | 5 |
| general | blend60 | 2 | 383 | 5 | 0 | 21 | 5 |
| general | blend70 | 1 | 383 | 10 | 0 | 15 | 5 |
| general | blend70 | 2 | 383 | 5 | 0 | 21 | 6 |
| general | ft | 1 | 383 | 11 | 1 | 13 | 5 |
| general | ft | 2 | 383 | 5 | 0 | 20 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 8, category→quantity: 5, quantity→amount: 2, org→address: 2, account→text: 2, text→account: 2, category→account: 2, amount→id: 2
- business / blend60: category→quantity: 17, org→account: 6, category→account: 3, amount→quantity: 3, quantity→amount: 2, org→address: 2, account→text: 2, text→account: 2
- business / blend70: category→quantity: 20, org→account: 6, category→account: 3, amount→quantity: 3, quantity→amount: 2, org→address: 2, org→category: 2, account→text: 2
- business / ft: category→quantity: 23, org→account: 7, category→account: 4, amount→quantity: 4, org→address: 3, quantity→amount: 2, org→category: 2, account→text: 2
- business2 / blend50: account→category: 5, amount→quantity: 4, text→org: 3, category→text: 3, quantity→category: 3, address→category: 3, id→category: 3, quantity→amount: 2
- business2 / blend60: account→category: 5, amount→quantity: 5, id→category: 4, category→id: 4, quantity→category: 3, category→quantity: 3, address→category: 3, quantity→amount: 2
- business2 / blend70: amount→quantity: 6, account→category: 5, id→category: 4, category→id: 4, category→quantity: 4, quantity→category: 3, address→category: 3, quantity→amount: 2
- business2 / ft: category→quantity: 6, account→category: 5, amount→quantity: 5, quantity→category: 5, id→category: 4, category→id: 4, address→category: 3, account→org: 2
- dev220 / blend50: quantity→category: 4, address→id: 3, category→tax_class: 2, id→quantity: 2, category→text: 1
- dev220 / blend60: quantity→category: 4, category→tax_class: 2, id→quantity: 2, text→category: 1, category→text: 1, address→id: 1
- dev220 / blend70: quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→account: 1, text→category: 1, category→text: 1, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, text→category: 1, category→text: 1, address→id: 1, rate→tax_class: 1
- general / blend50: quantity→category: 4, category→text: 3, text→category: 2, id→category: 2, id→address: 1, address→org: 1, org→text: 1
- general / blend60: quantity→category: 4, text→category: 3, category→text: 2, id→address: 2, id→category: 2, address→org: 1
- general / blend70: quantity→category: 4, text→category: 3, category→text: 2, id→address: 2, id→category: 2, org→address: 1, address→org: 1
- general / ft: quantity→category: 4, category→text: 3, text→category: 2, id→address: 2, org→address: 1, text→person: 1, address→org: 1, id→quantity: 1

### seedをまたいで再発した誤り

- business / blend50: `australian sourced services`、amount→id（seed 1, seed 2）
- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `publisher label`、org→address（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `q7`、category→quantity（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `publisher label`、org→address（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `q2a`、category→quantity（seed 1, seed 2）
- business / blend60: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend60: `q5a`、category→quantity（seed 1, seed 2）
- business / blend60: `q6`、category→quantity（seed 1, seed 2）
- business / blend60: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `q8`、category→quantity（seed 1, seed 2）
- business / blend60: `title`、category→account（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `agebann`、category→quantity（seed 1, seed 2）
- business / blend70: `d1`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→category（seed 1, seed 2）
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
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `title`、category→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `surveyname`、text→org（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `surveyname`、text→org（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `account name`、account→org（seed 1, seed 2）
- business2 / ft: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service`、account→address（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→category（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `want to live in this parish only`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `city`、address→id（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | australian sourced services | amount | id | 0.6251 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9809 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5347 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5056 | no |
| unknown | business | blend50 | 1 | agebann | category | unknown | 0.4691 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5185 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3112 | no |
| unknown | business | blend50 | 1 | class-title_en | category | unknown | 0.4588 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4765 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4736 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4178 | no |
| unknown | business | blend50 | 1 | d2 | category | unknown | 0.3646 | no |
| unknown | business | blend50 | 1 | d6 | category | unknown | 0.4354 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5299 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9899 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9313 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.5945 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.4063 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3468 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.4162 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4697 | no |
| unknown | business | blend50 | 1 | q4b_1 | category | unknown | 0.4470 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4959 | no |
| unknown | business | blend50 | 1 | q6 | category | unknown | 0.4837 | no |
| unknown | business | blend50 | 1 | q8 | category | unknown | 0.4868 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9805 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9801 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3756 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.3147 | no |
| unknown | business | blend50 | 1 | segment-title_fr | category | unknown | 0.4459 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9827 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9132 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9827 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.7953 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9894 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.6947 | no |
| wrong | business | blend50 | 1 | entitiy | org | category | 0.5488 | no |
| wrong | business | blend50 | 1 | merchant details | text | org | 0.5453 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5312 | no |
| wrong | business | blend50 | 1 | publisher label | org | address | 0.5139 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8402 | no |
| wrong | business | blend50 | 1 | q7 | category | quantity | 0.5210 | no |
| wrong | business | blend50 | 1 | title | category | account | 0.5002 | no |
| critical | business | blend50 | 2 | australian sourced services | amount | id | 0.5573 | yes |
| critical | business | blend50 | 2 | mois calendrier | date | quantity | 0.7553 | yes |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.9110 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5023 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5100 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4958 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5176 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4278 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4092 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4005 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4438 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.3691 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5374 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4357 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9906 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9264 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.5942 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.3894 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5923 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4524 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.4551 | no |
| unknown | business | blend50 | 2 | q2a | category | unknown | 0.4943 | no |
| unknown | business | blend50 | 2 | q3_1 | category | unknown | 0.4892 | no |
| unknown | business | blend50 | 2 | q3_2 | category | unknown | 0.4746 | no |
| unknown | business | blend50 | 2 | q5b | category | unknown | 0.4972 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9862 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9789 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.2901 | no |
| unknown | business | blend50 | 2 | respnum$ | id | unknown | 0.3944 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4683 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9782 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7261 | no |
| wrong | business | blend50 | 2 | capital revenue | category | account | 0.5789 | no |
| wrong | business | blend50 | 2 | d6 | category | quantity | 0.5563 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9810 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7064 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9835 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7426 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.8766 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5059 | no |
| wrong | business | blend50 | 2 | publisher label | org | address | 0.5152 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.7517 | no |
| wrong | business | blend50 | 2 | q6 | category | quantity | 0.5038 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5279 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5233 | no |
| critical | business | blend60 | 1 | australian sourced services | amount | id | 0.5680 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9780 | yes |
| unknown | business | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5315 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5752 | no |
| unknown | business | blend60 | 1 | agebann | category | unknown | 0.4882 | no |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6116 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.3566 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4159 | no |
| unknown | business | blend60 | 1 | d1 | category | unknown | 0.4834 | no |
| unknown | business | blend60 | 1 | d2 | category | unknown | 0.3954 | no |
| unknown | business | blend60 | 1 | d6 | category | unknown | 0.4881 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9884 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9380 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.3801 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.2804 | no |
| unknown | business | blend60 | 1 | overseas sourced services | amount | unknown | 0.3696 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4427 | no |
| unknown | business | blend60 | 1 | q3_2 | category | unknown | 0.4305 | no |
| unknown | business | blend60 | 1 | q5b | category | unknown | 0.4026 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9779 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9806 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.4168 | no |
| unknown | business | blend60 | 1 | respnum$ | id | unknown | 0.3589 | no |
| unknown | business | blend60 | 1 | segment-title_fr | category | unknown | 0.4780 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9833 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9261 | no |
| wrong | business | blend60 | 1 | commodity-title_en | product | category | 0.5309 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9820 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8290 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9889 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.7290 | no |
| wrong | business | blend60 | 1 | entitiy | org | category | 0.6115 | no |
| wrong | business | blend60 | 1 | merchant details | text | org | 0.6084 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.6040 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8185 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.5655 | no |
| wrong | business | blend60 | 1 | q3_1 | category | quantity | 0.5515 | no |
| wrong | business | blend60 | 1 | q4b_1 | category | id | 0.5321 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.5177 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.5639 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.6085 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.5694 | no |
| wrong | business | blend60 | 1 | title | category | account | 0.5908 | no |
| critical | business | blend60 | 2 | australian sourced goods | amount | quantity | 0.5134 | yes |
| critical | business | blend60 | 2 | mois calendrier | date | quantity | 0.7523 | yes |
| critical | business | blend60 | 2 | overseas sourced goods | amount | quantity | 0.5428 | yes |
| critical | business | blend60 | 2 | overseas sourced services | amount | quantity | 0.5415 | yes |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.8941 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5967 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6046 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6106 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.4866 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3386 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.4549 | no |
| unknown | business | blend60 | 2 | d2 | category | unknown | 0.4095 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4759 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9892 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9321 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.3576 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9848 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9791 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.3481 | no |
| unknown | business | blend60 | 2 | respnum$ | id | unknown | 0.4710 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9779 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.7016 | no |
| wrong | business | blend60 | 2 | account_name | account | org | 0.5366 | no |
| wrong | business | blend60 | 2 | agebann | category | quantity | 0.5780 | no |
| wrong | business | blend60 | 2 | capital revenue | category | account | 0.6417 | no |
| wrong | business | blend60 | 2 | d1 | category | quantity | 0.5301 | no |
| wrong | business | blend60 | 2 | d6 | category | quantity | 0.6332 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9799 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7223 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9819 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.7865 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.8991 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.6056 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.7123 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.5880 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.5740 | no |
| wrong | business | blend60 | 2 | q3_2 | category | quantity | 0.5384 | no |
| wrong | business | blend60 | 2 | q5a | category | quantity | 0.5735 | no |
| wrong | business | blend60 | 2 | q5b | category | quantity | 0.5652 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.5975 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6168 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.6132 | no |
| wrong | business | blend60 | 2 | title | category | account | 0.5525 | no |
| critical | business | blend70 | 1 | australian sourced services | amount | id | 0.5108 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9751 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4159 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4280 | no |
| unknown | business | blend70 | 1 | d2 | category | unknown | 0.4613 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9869 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9448 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.4401 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.2385 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.3539 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3565 | no |
| unknown | business | blend70 | 1 | q3_2 | category | unknown | 0.4992 | no |
| unknown | business | blend70 | 1 | q5b | category | unknown | 0.4032 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9754 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9811 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.4580 | no |
| unknown | business | blend70 | 1 | respnum$ | id | unknown | 0.4030 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9839 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9390 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.5554 | no |
| wrong | business | blend70 | 1 | commodity-title_en | product | category | 0.5852 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.5619 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.5408 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9812 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8627 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9884 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7633 | no |
| wrong | business | blend70 | 1 | entitiy | org | category | 0.6742 | no |
| wrong | business | blend70 | 1 | merchant details | text | org | 0.6714 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6942 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7968 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.6554 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.6401 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | id | 0.6173 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6020 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.6520 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.6960 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.6520 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.6813 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.5990 | yes |
| critical | business | blend70 | 2 | mois calendrier | date | quantity | 0.7492 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6333 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.6279 | yes |
| critical | business | blend70 | 2 | respnum$ | id | amount | 0.5475 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.8773 | yes |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4263 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3522 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4606 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9878 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9379 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.3257 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9833 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9794 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4060 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.4714 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9777 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.6770 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.5982 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.6601 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.7046 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.6164 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7101 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9788 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7382 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9802 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8304 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.5160 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9216 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5228 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6960 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.6730 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6817 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6664 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6250 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6672 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.6562 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6912 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7057 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7031 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.6367 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9665 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.5941 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.3989 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9824 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9650 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.6202 | no |
| unknown | business | ft | 1 | overseas sourced goods | amount | unknown | 0.3407 | no |
| unknown | business | ft | 1 | overseas sourced services | amount | unknown | 0.4249 | no |
| unknown | business | ft | 1 | q5b | category | unknown | 0.5694 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9677 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9826 | no |
| unknown | business | ft | 1 | respnum$ | id | unknown | 0.5355 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9857 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9777 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.7571 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.7481 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.7975 | no |
| wrong | business | ft | 1 | d2 | category | amount | 0.6589 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.6990 | no |
| wrong | business | ft | 1 | department | org | account | 0.9789 | no |
| wrong | business | ft | 1 | department | org | account | 0.9638 | no |
| wrong | business | ft | 1 | department | org | account | 0.5935 | no |
| wrong | business | ft | 1 | department | org | account | 0.9870 | no |
| wrong | business | ft | 1 | description | account | text | 0.8662 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.8624 | no |
| wrong | business | ft | 1 | merchant details | text | org | 0.8607 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | address | 0.5085 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9646 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.7318 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9253 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9060 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.7052 | no |
| wrong | business | ft | 1 | q4b_1 | category | id | 0.8727 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.8551 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9162 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9586 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.8997 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.5817 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.5314 | no |
| wrong | business | ft | 1 | title | category | account | 0.9531 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.8556 | yes |
| critical | business | ft | 2 | australian sourced services | amount | quantity | 0.6090 | yes |
| critical | business | ft | 2 | mois calendrier | date | quantity | 0.7401 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.9046 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.8870 | yes |
| critical | business | ft | 2 | respnum$ | id | amount | 0.7771 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.8267 | yes |
| other_ng | business | ft | 2 | km budgété | other | amount | 0.5490 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4152 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9838 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9552 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.2588 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9790 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9802 | no |
| unknown | business | ft | 2 | tournée | id | unknown | 0.4515 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9768 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.6034 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.7832 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.9067 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.8931 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.8753 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.6140 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9408 | no |
| wrong | business | ft | 2 | department | org | account | 0.9755 | no |
| wrong | business | ft | 2 | department | org | account | 0.7860 | no |
| wrong | business | ft | 2 | department | org | account | 0.9753 | no |
| wrong | business | ft | 2 | description | account | text | 0.9620 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.6363 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9892 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.6917 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9673 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.5548 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9629 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9436 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.8850 | no |
| wrong | business | ft | 2 | q4a | category | quantity | 0.5327 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9482 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9289 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9723 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9724 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9728 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | tax_class | 0.5800 | no |
| wrong | business | ft | 2 | title | category | account | 0.8893 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9710 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9814 | yes |
| other_ng | business2 | blend50 | 1 | a1 (retail) floorspace losses sqm | other | amount | 0.5082 | no |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.7814 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.8773 | no |
| other_ng | business2 | blend50 | 1 | b1a floorspace net sqm | other | amount | 0.5134 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5466 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5340 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5094 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4510 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3794 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 0.9939 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4722 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4477 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.9471 | no |
| unknown | business2 | blend50 | 1 | imd19_income_decile | category | unknown | 0.4844 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.2997 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4785 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4964 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5126 | no |
| unknown | business2 | blend50 | 1 | programme | category | unknown | 0.4885 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5438 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4586 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4771 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4069 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3337 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4296 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4667 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5104 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5065 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9925 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9866 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9912 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4625 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9697 | no |
| wrong | business2 | blend50 | 1 | bike_stands | quantity | category | 0.7343 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.6617 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5082 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7884 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9239 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5869 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5529 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.7844 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5686 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.6370 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.6487 | no |
| wrong | business2 | blend50 | 1 | surveyname | text | org | 0.5577 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9305 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9799 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7475 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7236 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.8686 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.8673 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8724 | no |
| other_ng | business2 | blend50 | 2 | b1a floorspace net sqm | other | amount | 0.5142 | no |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5294 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5024 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5091 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.2680 | no |
| unknown | business2 | blend50 | 2 | bike_stands | quantity | unknown | 0.4998 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.4060 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4297 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4134 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9131 | no |
| unknown | business2 | blend50 | 2 | habitatcode | id | unknown | 0.4679 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.2988 | no |
| unknown | business2 | blend50 | 2 | imd19_national_decile | category | unknown | 0.3408 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5891 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.4763 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4962 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9884 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4828 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4661 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5200 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3000 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3913 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3566 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4032 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.4931 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4951 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4979 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5209 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9949 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9841 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9928 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9724 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5402 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7861 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.6811 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.9199 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5245 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.6359 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.7161 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8249 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.5426 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9323 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.7042 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.5572 | no |
| critical | business2 | blend60 | 1 | fine | amount | quantity | 0.5167 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9701 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9786 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.7747 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.8813 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5322 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5696 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.5303 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.4096 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 0.9927 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4475 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.9496 | no |
| unknown | business2 | blend60 | 1 | health service executive area | address | unknown | 0.4789 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.3170 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5740 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9881 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5985 | no |
| unknown | business2 | blend60 | 1 | programme | category | unknown | 0.4863 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4835 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.4377 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4291 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3036 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4177 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9896 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5687 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.5218 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9910 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9865 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 1 | want to live in this parish only | quantity | unknown | 0.4727 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9698 | no |
| wrong | business2 | blend60 | 1 | bike_stands | quantity | category | 0.7527 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.6314 | no |
| wrong | business2 | blend60 | 1 | imd19_income_decile | category | amount | 0.5812 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5615 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5160 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.8106 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9156 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6635 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6365 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.7517 | no |
| wrong | business2 | blend60 | 1 | service | account | address | 0.5499 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.6255 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.6476 | no |
| wrong | business2 | blend60 | 1 | surveyname | text | org | 0.5209 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.5352 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9381 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9809 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7164 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7668 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.8432 | yes |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.8777 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace losses sqm | other | quantity | 0.6019 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8754 | no |
| other_ng | business2 | blend60 | 2 | avg_tilt | other | rate | 0.5241 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5968 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6035 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.2805 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.4769 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4561 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.4756 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9088 | no |
| unknown | business2 | blend60 | 2 | habitatcode | id | unknown | 0.4644 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.2798 | no |
| unknown | business2 | blend60 | 2 | imd19_national_decile | category | unknown | 0.3812 | no |
| unknown | business2 | blend60 | 2 | merchant description | category | unknown | 0.4745 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9924 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5607 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9865 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6022 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4939 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3291 | no |
| unknown | business2 | blend60 | 2 | surveyname | text | unknown | 0.4961 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4640 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4277 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4838 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9863 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5909 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6124 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9940 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9836 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9730 | no |
| wrong | business2 | blend60 | 2 | account name | account | org | 0.5782 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5526 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5900 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.8078 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.6241 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.5564 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5386 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5323 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.9143 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.6242 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.7285 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8415 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.5670 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9403 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.7273 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.6277 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.5858 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9693 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9758 | yes |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.7679 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.5320 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.8853 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6095 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.4398 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9915 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4487 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9521 | no |
| unknown | business2 | blend70 | 1 | health service executive area | address | unknown | 0.4621 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.3467 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9865 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.3984 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4841 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4923 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4959 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3487 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4059 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend70 | 1 | value | quantity | unknown | 0.5981 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9896 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9864 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 1 | want to live in this parish only | quantity | unknown | 0.4948 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9698 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.7711 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.6011 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6781 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6550 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.5536 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8328 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9072 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.5672 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7401 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7201 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.7190 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6413 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.6141 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.6465 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6038 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9458 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.5378 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9818 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6852 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8101 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.8179 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.5912 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.8881 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.6659 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8784 | no |
| other_ng | business2 | blend70 | 2 | avg_tilt | other | rate | 0.6114 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.6335 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.3250 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9904 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9045 | no |
| unknown | business2 | blend70 | 2 | habitatcode | id | unknown | 0.4609 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.3264 | no |
| unknown | business2 | blend70 | 2 | imd19_national_decile | category | unknown | 0.4217 | no |
| unknown | business2 | blend70 | 2 | merchant description | category | unknown | 0.4877 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9918 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9846 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.3836 | no |
| unknown | business2 | blend70 | 2 | surveyname | text | unknown | 0.4496 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4988 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9846 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9930 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9830 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9905 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9736 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6745 | no |
| wrong | business2 | blend70 | 2 | construction_age_band | category | date | 0.5479 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.5164 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6447 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6399 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8295 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.5672 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6455 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.5944 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.5986 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9087 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6125 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.7409 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8581 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5643 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.6409 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9483 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.7504 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.6981 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.7930 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9667 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9675 | yes |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.7475 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.6668 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.8972 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.5350 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.8472 | no |
| unknown | business2 | ft | 1 | cost centre description | account | unknown | 0.4835 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9597 | no |
| unknown | business2 | ft | 1 | imd19_national_decile | category | unknown | 0.4358 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9863 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9817 | no |
| unknown | business2 | ft | 1 | returns | quantity | unknown | 0.6040 | no |
| unknown | business2 | ft | 1 | surveyname | text | unknown | 0.4487 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.4976 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.4741 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9853 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9863 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9837 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9699 | no |
| wrong | business2 | ft | 1 | account name | account | org | 0.5896 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.8262 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.5103 | no |
| wrong | business2 | ft | 1 | cost centre description | account | text | 0.5043 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.6008 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9687 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9357 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.6661 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.8993 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8820 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.6034 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.8100 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9698 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9709 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.6208 | no |
| wrong | business2 | ft | 1 | scheme_description | category | account | 0.5230 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.9154 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.5797 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.6431 | no |
| wrong | business2 | ft | 1 | surveyname | text | address | 0.6561 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.8095 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9688 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.6994 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.7244 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9845 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9398 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.7419 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.7995 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.6579 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9192 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.8581 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.8874 | no |
| other_ng | business2 | ft | 2 | avg_tilt | other | rate | 0.8732 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.5604 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.8268 | no |
| other_ng | business2 | ft | 2 | total_floor_area | other | quantity | 0.6221 | no |
| unknown | business2 | ft | 2 | amt-units_mnt-unite | category | unknown | 0.4584 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9863 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.8916 | no |
| unknown | business2 | ft | 2 | habitatcode | id | unknown | 0.4712 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.4662 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9898 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.5751 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9790 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5919 | no |
| unknown | business2 | ft | 2 | surveyname | text | unknown | 0.3115 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9846 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9825 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9814 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9796 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9872 | no |
| unknown | business2 | ft | 2 | total membership | quantity | unknown | 0.5246 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9902 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9814 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9870 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9753 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9632 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.7608 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.6974 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9210 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.6479 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.7894 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.8946 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9128 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7617 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7973 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.8918 | no |
| wrong | business2 | ft | 2 | service | account | address | 0.5473 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.5775 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.7779 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9080 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.7120 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8059 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.8624 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9724 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.8197 | no |
| wrong | business2 | ft | 2 | want to live in this parish & band a | quantity | category | 0.6238 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.5597 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.9095 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8480 | yes |
| unknown | dev220 | blend50 | 1 | material | product | unknown | 0.4993 | no |
| unknown | dev220 | blend50 | 1 | receive_order_import_type_id | category | unknown | 0.4963 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4991 | no |
| unknown | dev220 | blend50 | 1 | 履行場所 | address | unknown | 0.4800 | no |
| wrong | dev220 | blend50 | 1 | city | address | id | 0.6382 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8612 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5795 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.7437 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.7690 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8735 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.5097 | no |
| unknown | dev220 | blend50 | 2 | receive_order_import_type_id | category | unknown | 0.4556 | no |
| unknown | dev220 | blend50 | 2 | 履行場所 | address | unknown | 0.4797 | no |
| wrong | dev220 | blend50 | 2 | city | address | id | 0.5286 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.7888 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5704 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.9194 | no |
| wrong | dev220 | blend50 | 2 | 受注郵便番号 | address | id | 0.5026 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8579 | yes |
| unknown | dev220 | blend60 | 1 | 担当課 | org | unknown | 0.4912 | no |
| wrong | dev220 | blend60 | 1 | city | address | id | 0.6299 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8606 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6563 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.6954 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.7721 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5567 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8886 | yes |
| unknown | dev220 | blend60 | 2 | city | address | unknown | 0.4983 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.7738 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6454 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.9062 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8678 | yes |
| wrong | dev220 | blend70 | 1 | city | address | id | 0.6216 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8601 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7331 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.6471 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.7752 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.5560 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6349 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9036 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.7588 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7203 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.8929 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.8976 | yes |
| wrong | dev220 | ft | 1 | city | address | id | 0.5966 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8586 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9634 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.5021 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.7845 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7505 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.8695 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9486 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.7138 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9451 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.8533 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.5919 | no |
| wrong | dev220 | ft | 2 | 税率 | rate | tax_class | 0.5435 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.7288 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.9166 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.7066 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9640 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7625 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.5820 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.7253 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.6037 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4956 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7602 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9119 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.5304 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.9694 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.5931 | no |
| unknown | general | blend50 | 1 | place | org | unknown | 0.4272 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.2749 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4936 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.4728 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.3472 | no |
| unknown | general | blend50 | 1 | term | text | unknown | 0.4954 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4896 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4854 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4550 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9367 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9924 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9523 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.7114 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.6283 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9020 | no |
| wrong | general | blend50 | 1 | standardhours | quantity | category | 0.5836 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.8526 | no |
| wrong | general | blend50 | 1 | 住家一部損壊 | quantity | category | 0.6266 | no |
| wrong | general | blend50 | 1 | 日本語教室名 | org | text | 0.5200 | no |
| wrong | general | blend50 | 1 | 発生県 | id | address | 0.5097 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5075 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.8990 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.9355 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.7307 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9843 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7576 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.4980 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.5901 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.5504 | no |
| unknown | general | blend50 | 2 | author | person | unknown | 0.4780 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4902 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.7507 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9116 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9666 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4931 | no |
| unknown | general | blend50 | 2 | pir_sha | id | unknown | 0.5892 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.4819 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4560 | no |
| unknown | general | blend50 | 2 | sens_final | rate | unknown | 0.5557 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4705 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4813 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.2459 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4879 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.4353 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4945 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.8221 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4898 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9929 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8386 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4453 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.8390 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.7324 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8996 | no |
| wrong | general | blend50 | 2 | raw | category | text | 0.5537 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.6903 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.7071 | no |
| other_ng | general | blend60 | 1 | episode | other | quantity | 0.5126 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.9114 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.6815 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9577 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7850 | no |
| unknown | general | blend60 | 1 | age_q1_nd | quantity | unknown | 0.5482 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.7057 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.5527 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.8057 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9274 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9704 | no |
| unknown | general | blend60 | 1 | place | org | unknown | 0.4814 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.2744 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4954 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3976 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3943 | no |
| unknown | general | blend60 | 1 | 日本語教室名 | org | unknown | 0.4590 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9466 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9909 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9582 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.6612 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5659 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9129 | no |
| wrong | general | blend60 | 1 | standardhours | quantity | category | 0.5885 | no |
| wrong | general | blend60 | 1 | term | text | category | 0.5835 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.8348 | no |
| wrong | general | blend60 | 1 | 住家一部損壊 | quantity | category | 0.6045 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.6036 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5157 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.9113 | no |
| other_ng | general | blend60 | 2 | episode | other | quantity | 0.5598 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.9341 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.7104 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9820 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7791 | no |
| unknown | general | blend60 | 2 | age_q1_nd | quantity | unknown | 0.4474 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.5434 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.4888 | no |
| unknown | general | blend60 | 2 | app | category | unknown | 0.4565 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.7942 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9270 | no |
| unknown | general | blend60 | 2 | funding | amount | unknown | 0.5823 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9670 | no |
| unknown | general | blend60 | 2 | keywords | text | unknown | 0.4310 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5358 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4746 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.6337 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.5605 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4657 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.2720 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4686 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.8090 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9915 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8218 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4411 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.8144 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.6908 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9101 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6400 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5797 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6854 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.5961 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9062 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.6564 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9514 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8075 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.5144 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.6861 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.5017 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.4633 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8512 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9428 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9713 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.2738 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.4480 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.4342 | no |
| unknown | general | blend70 | 1 | 日本語教室名 | org | unknown | 0.4809 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9564 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9893 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9641 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.6110 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.5034 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9238 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.5356 | no |
| wrong | general | blend70 | 1 | standardhours | quantity | category | 0.5934 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6800 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8170 | no |
| wrong | general | blend70 | 1 | 住家一部損壊 | quantity | category | 0.5824 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.6975 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.5239 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9237 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.5329 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6511 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9327 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.6901 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9798 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8006 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.3969 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.4968 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.4272 | no |
| unknown | general | blend70 | 2 | app | category | unknown | 0.5244 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8378 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9424 | no |
| unknown | general | blend70 | 2 | funding | amount | unknown | 0.5251 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9674 | no |
| unknown | general | blend70 | 2 | keywords | text | unknown | 0.3517 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6156 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.4208 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7116 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6540 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.4502 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.2980 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.5456 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.7959 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9901 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8050 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4369 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7897 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.6492 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9206 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.5897 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6696 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.5997 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.6204 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.8464 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.8906 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.6130 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9325 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8750 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.4131 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.6274 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.4143 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.6201 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4603 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9876 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9893 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9743 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.3402 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9859 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9848 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9817 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9567 | no |
| wrong | general | ft | 1 | place | org | address | 0.6981 | no |
| wrong | general | ft | 1 | standardhours | quantity | category | 0.6082 | no |
| wrong | general | ft | 1 | study | text | person | 0.5992 | no |
| wrong | general | ft | 1 | term | text | category | 0.9693 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.7635 | no |
| wrong | general | ft | 1 | 住家一部損壊 | quantity | category | 0.5162 | no |
| wrong | general | ft | 1 | 住家全壊 | quantity | category | 0.6195 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9791 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.5486 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9607 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.6450 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.9250 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9284 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.6291 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9731 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8652 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.4919 | no |
| unknown | general | ft | 2 | age_q3 | quantity | unknown | 0.4931 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.7282 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9684 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9887 | no |
| unknown | general | ft | 2 | funding | amount | unknown | 0.5752 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9687 | no |
| unknown | general | ft | 2 | keywords | text | unknown | 0.4892 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8549 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.6003 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9455 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9342 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4036 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.3761 | no |
| unknown | general | ft | 2 | units | category | unknown | 0.5554 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.7567 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9858 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.7544 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.4242 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.7157 | no |
| wrong | general | ft | 2 | goal | id | category | 0.5243 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9521 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.5438 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9394 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9845 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9876 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9829 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9867 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9814 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9858 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9769 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9832 | no |

### unknown の判定理由

- date_value_evidence_low: 113件
- numeric_top2_too_close: 53件
- numeric_values_not_parseable: 28件
- other_class: 110件
- probability_below_threshold: 240件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 65件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 280件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 191件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
