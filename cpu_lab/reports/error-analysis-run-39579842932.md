# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-21T09:53:53+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 10 | 2 | 33 | 1 |
| business | blend50 | 2 | 490 | 15 | 3 | 27 | 1 |
| business | blend60 | 1 | 490 | 19 | 2 | 24 | 1 |
| business | blend60 | 2 | 490 | 22 | 2 | 19 | 1 |
| business | blend70 | 1 | 490 | 19 | 1 | 22 | 1 |
| business | blend70 | 2 | 490 | 24 | 1 | 13 | 1 |
| business | ft | 1 | 490 | 19 | 1 | 18 | 1 |
| business | ft | 2 | 490 | 24 | 2 | 12 | 1 |
| business2 | blend50 | 1 | 976 | 16 | 3 | 37 | 5 |
| business2 | blend50 | 2 | 976 | 14 | 3 | 37 | 4 |
| business2 | blend60 | 1 | 976 | 18 | 3 | 34 | 2 |
| business2 | blend60 | 2 | 976 | 15 | 2 | 33 | 3 |
| business2 | blend70 | 1 | 976 | 23 | 3 | 25 | 3 |
| business2 | blend70 | 2 | 976 | 17 | 2 | 24 | 3 |
| business2 | ft | 1 | 976 | 24 | 3 | 20 | 5 |
| business2 | ft | 2 | 976 | 18 | 2 | 24 | 3 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 6 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 1 | 6 | 0 |
| dev220 | blend60 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 7 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 8 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 4 | 1 | 2 | 0 |
| general | blend50 | 1 | 383 | 7 | 0 | 27 | 4 |
| general | blend50 | 2 | 383 | 5 | 0 | 32 | 4 |
| general | blend60 | 1 | 383 | 9 | 0 | 21 | 5 |
| general | blend60 | 2 | 383 | 5 | 0 | 24 | 5 |
| general | blend70 | 1 | 383 | 8 | 1 | 22 | 5 |
| general | blend70 | 2 | 383 | 7 | 0 | 23 | 6 |
| general | ft | 1 | 383 | 10 | 1 | 20 | 6 |
| general | ft | 2 | 383 | 10 | 0 | 20 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 8, category→quantity: 5, quantity→amount: 2, account→text: 2, text→account: 2, amount→id: 2, text→category: 1, text→org: 1
- business / blend60: category→quantity: 18, org→account: 7, account→text: 2, text→account: 2, category→account: 2, amount→id: 2, quantity→amount: 1, text→category: 1
- business / blend70: category→quantity: 21, org→account: 7, account→text: 2, text→account: 2, category→account: 2, quantity→amount: 1, text→category: 1, account→category: 1
- business / ft: category→quantity: 21, org→account: 7, account→text: 2, text→account: 2, category→account: 2, amount→quantity: 2, quantity→amount: 1, text→category: 1
- business2 / blend50: category→text: 4, amount→quantity: 4, account→category: 3, text→org: 3, quantity→category: 3, id→category: 3, quantity→amount: 2, category→id: 2
- business2 / blend60: amount→quantity: 4, account→category: 3, text→org: 3, quantity→category: 3, category→quantity: 3, id→category: 3, org→address: 3, category→id: 2
- business2 / blend70: category→quantity: 6, quantity→category: 4, amount→quantity: 4, account→category: 3, id→category: 3, org→address: 3, account→org: 3, category→id: 2
- business2 / ft: category→quantity: 7, org→address: 4, amount→quantity: 4, account→category: 3, quantity→category: 3, id→category: 3, account→org: 3, category→id: 2
- dev220 / blend50: quantity→category: 4, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- dev220 / blend60: quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→account: 1, category→text: 1
- dev220 / blend70: quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→person: 1, org→account: 1, category→text: 1
- dev220 / ft: quantity→category: 4, category→tax_class: 2, id→quantity: 2, rate→tax_class: 1, org→person: 1, org→account: 1, category→text: 1
- general / blend50: quantity→category: 4, category→text: 3, text→category: 2, id→category: 2, address→org: 1
- general / blend60: quantity→category: 4, text→category: 3, category→text: 2, id→category: 2, org→address: 1, id→address: 1, address→org: 1
- general / blend70: quantity→category: 4, category→text: 2, text→category: 2, id→address: 2, org→address: 1, address→org: 1, id→quantity: 1, text→org: 1
- general / ft: quantity→category: 4, category→text: 3, text→category: 3, id→address: 2, org→address: 1, address→org: 1, text→account: 1, id→quantity: 1

### seedをまたいで再発した誤り

- business / blend50: `australian sourced services`、amount→id（seed 1, seed 2）
- business / blend50: `d6`、category→quantity（seed 1, seed 2）
- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `australian sourced services`、amount→id（seed 1, seed 2）
- business / blend60: `d1`、category→quantity（seed 1, seed 2）
- business / blend60: `d6`、category→quantity（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `q2a`、category→quantity（seed 1, seed 2）
- business / blend60: `q6`、category→quantity（seed 1, seed 2）
- business / blend60: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `d1`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business2 / blend50: `contravention`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `surveyname`、text→org（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `surveyname`、text→org（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `service`、account→org（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
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
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `standardhours`、quantity→category（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `standardhours`、quantity→category（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `standardhours`、quantity→category（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `standardhours`、quantity→category（seed 1, seed 2）
- general / ft: `term`、text→category（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | australian sourced services | amount | id | 0.6157 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9754 | yes |
| other_ng | business | blend50 | 1 | km budgété | other | category | 0.5980 | no |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5930 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5394 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5158 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3731 | no |
| unknown | business | blend50 | 1 | class-title_en | category | unknown | 0.4995 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4671 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4546 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4524 | no |
| unknown | business | blend50 | 1 | d2 | category | unknown | 0.3677 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5157 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4348 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9840 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9146 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.5217 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.3118 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.4485 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3445 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5293 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4497 | no |
| unknown | business | blend50 | 1 | q2a | category | unknown | 0.4946 | no |
| unknown | business | blend50 | 1 | q3_1 | category | unknown | 0.4984 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4643 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4917 | no |
| unknown | business | blend50 | 1 | q6 | category | unknown | 0.4823 | no |
| unknown | business | blend50 | 1 | q7 | category | unknown | 0.4906 | no |
| unknown | business | blend50 | 1 | q8 | category | unknown | 0.4665 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9743 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9760 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4754 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.3766 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4739 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9759 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8838 | no |
| wrong | business | blend50 | 1 | d6 | category | quantity | 0.5345 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9797 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.7975 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9862 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.7017 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.6397 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5206 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8034 | no |
| critical | business | blend50 | 2 | australian sourced services | amount | id | 0.5822 | yes |
| critical | business | blend50 | 2 | mois calendrier | date | quantity | 0.5643 | yes |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.6299 | yes |
| other_ng | business | blend50 | 2 | km budgété | other | amount | 0.5461 | no |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.4942 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5071 | no |
| unknown | business | blend50 | 2 | account_name | account | unknown | 0.4903 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4700 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5175 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.2825 | no |
| unknown | business | blend50 | 2 | capital revenue | category | unknown | 0.4961 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4055 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4196 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4533 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.4715 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5345 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4502 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9893 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9235 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.5697 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.3108 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.6015 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.3791 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.3331 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4865 | no |
| unknown | business | blend50 | 2 | q3_2 | category | unknown | 0.4768 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9870 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9775 | no |
| unknown | business | blend50 | 2 | respnum$ | id | unknown | 0.4610 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9654 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8298 | no |
| wrong | business | blend50 | 2 | d6 | category | quantity | 0.5468 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9762 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7111 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9792 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7139 | no |
| wrong | business | blend50 | 2 | merchant details | text | org | 0.5563 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5612 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.7512 | no |
| wrong | business | blend50 | 2 | q6 | category | quantity | 0.5037 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5280 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5205 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.6283 | no |
| critical | business | blend60 | 1 | australian sourced services | amount | id | 0.5566 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9714 | yes |
| other_ng | business | blend60 | 1 | km budgété | other | category | 0.5821 | no |
| unknown | business | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5177 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5253 | no |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6084 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.4476 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4081 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4087 | no |
| unknown | business | blend60 | 1 | d2 | category | unknown | 0.2956 | no |
| unknown | business | blend60 | 1 | defence services value | amount | unknown | 0.6015 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9813 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9180 | no |
| unknown | business | blend60 | 1 | grant in dollars | amount | unknown | 0.4799 | no |
| unknown | business | blend60 | 1 | ligne | category | unknown | 0.2645 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.3842 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.2861 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4300 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4342 | no |
| unknown | business | blend60 | 1 | q3_1 | category | unknown | 0.4955 | no |
| unknown | business | blend60 | 1 | q3_2 | category | unknown | 0.4706 | no |
| unknown | business | blend60 | 1 | q4b_1 | category | unknown | 0.4991 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9705 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9757 | no |
| unknown | business | blend60 | 1 | respnum$ | id | unknown | 0.4332 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9751 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8908 | no |
| wrong | business | blend60 | 1 | d1 | category | quantity | 0.5404 | no |
| wrong | business | blend60 | 1 | d6 | category | quantity | 0.6070 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9783 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8317 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9851 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.7374 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5209 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.6148 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.7743 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.5103 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.5289 | no |
| wrong | business | blend60 | 1 | q5b | category | quantity | 0.5520 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.5428 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.5720 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.5363 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5366 | no |
| wrong | business | blend60 | 1 | title | category | account | 0.5154 | no |
| critical | business | blend60 | 2 | australian sourced services | amount | id | 0.5165 | yes |
| critical | business | blend60 | 2 | mois calendrier | date | quantity | 0.5230 | yes |
| other_ng | business | blend60 | 2 | km budgété | other | amount | 0.6024 | no |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5870 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6012 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6105 | no |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.3190 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3342 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4932 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9877 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9287 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.2872 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.4549 | no |
| unknown | business | blend60 | 2 | overseas sourced services | amount | unknown | 0.3302 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4788 | no |
| unknown | business | blend60 | 2 | q5a | category | unknown | 0.4945 | no |
| unknown | business | blend60 | 2 | q5b | category | unknown | 0.4944 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9857 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9775 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5569 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9626 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8260 | no |
| wrong | business | blend60 | 2 | account_name | account | org | 0.5551 | no |
| wrong | business | blend60 | 2 | agebann | category | quantity | 0.5470 | no |
| wrong | business | blend60 | 2 | capital revenue | category | account | 0.5423 | no |
| wrong | business | blend60 | 2 | d1 | category | quantity | 0.5415 | no |
| wrong | business | blend60 | 2 | d2 | category | quantity | 0.5452 | no |
| wrong | business | blend60 | 2 | d6 | category | quantity | 0.6218 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9742 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7280 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9767 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.7521 | no |
| wrong | business | blend60 | 2 | merchant details | text | org | 0.6216 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5711 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.7117 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.5429 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.5172 | no |
| wrong | business | blend60 | 2 | q3_2 | category | quantity | 0.5684 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.5974 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6169 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.6098 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.5843 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9675 | yes |
| other_ng | business | blend70 | 1 | km budgété | other | category | 0.5662 | no |
| unknown | business | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5207 | no |
| unknown | business | blend70 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6067 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.5222 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.4976 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3617 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4759 | no |
| unknown | business | blend70 | 1 | d2 | category | unknown | 0.3261 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9787 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9214 | no |
| unknown | business | blend70 | 1 | grant in dollars | amount | unknown | 0.4701 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.2693 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.3198 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.3337 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4062 | no |
| unknown | business | blend70 | 1 | q2c | category | unknown | 0.4843 | no |
| unknown | business | blend70 | 1 | q3_2 | category | unknown | 0.5481 | no |
| unknown | business | blend70 | 1 | q4b_1 | category | unknown | 0.4848 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9667 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9753 | no |
| unknown | business | blend70 | 1 | respnum$ | id | unknown | 0.4897 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9744 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8978 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6284 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.6796 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9769 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8659 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9840 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7731 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6070 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.5899 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7453 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.5911 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.5748 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6152 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6408 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.6273 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.6535 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.6134 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.5978 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.5935 | no |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.5307 | yes |
| other_ng | business | blend70 | 2 | km budgété | other | amount | 0.6587 | no |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.3721 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4508 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.2629 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9861 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9338 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.3326 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.4818 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.3539 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9844 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9775 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.4972 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9598 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8222 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.6198 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.6240 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.5886 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.6297 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.6190 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.6968 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9721 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7449 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9742 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.7902 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.5363 | no |
| wrong | business | blend70 | 2 | merchant details | text | org | 0.6869 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6558 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.6722 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6291 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6001 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6601 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.5571 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.5735 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6911 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7058 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.6991 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.5403 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9556 | yes |
| other_ng | business | ft | 1 | km budgété | other | category | 0.5184 | no |
| unknown | business | ft | 1 | agebann | category | unknown | 0.4684 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.7459 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.3342 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4288 | no |
| unknown | business | ft | 1 | d2 | category | unknown | 0.4513 | no |
| unknown | business | ft | 1 | department | org | unknown | 0.4756 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9706 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9316 | no |
| unknown | business | ft | 1 | ligne | category | unknown | 0.3471 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.4321 | no |
| unknown | business | ft | 1 | overseas sourced goods | amount | unknown | 0.4766 | no |
| unknown | business | ft | 1 | q2c | category | unknown | 0.3164 | no |
| unknown | business | ft | 1 | q3_2 | category | unknown | 0.7808 | no |
| unknown | business | ft | 1 | q4b_1 | category | unknown | 0.4420 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9553 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9744 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9721 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9188 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.8925 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.8972 | no |
| wrong | business | ft | 1 | department | org | account | 0.9728 | no |
| wrong | business | ft | 1 | department | org | account | 0.9683 | no |
| wrong | business | ft | 1 | department | org | account | 0.9808 | no |
| wrong | business | ft | 1 | description | account | text | 0.8803 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.8652 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.5153 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.6581 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.8334 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.8127 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.8739 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9069 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.8810 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.8978 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.8446 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.7813 | no |
| wrong | business | ft | 1 | title | category | account | 0.8275 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.5316 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.7580 | yes |
| other_ng | business | ft | 2 | km budgété | other | amount | 0.8276 | no |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.2536 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.3669 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9813 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9493 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.4689 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.3684 | no |
| unknown | business | ft | 2 | overseas sourced services | amount | unknown | 0.4737 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9806 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9774 | no |
| unknown | business | ft | 2 | title | category | unknown | 0.4861 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9513 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8109 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.8140 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.8551 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.7274 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.8943 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.8403 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9218 | no |
| wrong | business | ft | 2 | department | org | account | 0.9659 | no |
| wrong | business | ft | 2 | department | org | account | 0.7955 | no |
| wrong | business | ft | 2 | department | org | account | 0.9666 | no |
| wrong | business | ft | 2 | description | account | text | 0.9047 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.6653 | no |
| wrong | business | ft | 2 | merchant details | text | org | 0.8827 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9098 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.5537 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.8878 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.8488 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9350 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.7909 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.8109 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9721 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9726 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9670 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9711 | yes |
| critical | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6304 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9746 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.7397 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.8824 | no |
| other_ng | business2 | blend50 | 1 | b1a floorspace losses sqm | other | amount | 0.5426 | no |
| other_ng | business2 | blend50 | 1 | b1a floorspace net sqm | other | amount | 0.5108 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5197 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5843 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5367 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.5102 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.4135 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 0.9901 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3895 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3080 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.8970 | no |
| unknown | business2 | blend50 | 1 | imd19_income_decile | category | unknown | 0.4829 | no |
| unknown | business2 | blend50 | 1 | loac_group | category | unknown | 0.5000 | no |
| unknown | business2 | blend50 | 1 | locationname | address | unknown | 0.4976 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4168 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9882 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4966 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9828 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4913 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5379 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4256 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.3516 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4310 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4690 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3380 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3673 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9867 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9853 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4592 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4388 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5180 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5003 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9903 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9757 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9814 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4868 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9644 | no |
| wrong | business2 | blend50 | 1 | bike_stands | quantity | category | 0.6651 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.5927 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5013 | no |
| wrong | business2 | blend50 | 1 | imd19_national_decile | category | quantity | 0.5290 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7838 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.7696 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5378 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5148 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.9281 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5330 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8109 | no |
| wrong | business2 | blend50 | 1 | surveyname | text | org | 0.5645 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9273 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9764 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7090 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.6382 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.7401 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.7597 | no |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5070 | no |
| other_ng | business2 | blend50 | 2 | loc_y | other | address | 0.5452 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.4943 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5063 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3180 | no |
| unknown | business2 | blend50 | 2 | bike_stands | quantity | unknown | 0.4925 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.3621 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 0.9919 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4459 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4404 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9342 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.2999 | no |
| unknown | business2 | blend50 | 2 | locationname | address | unknown | 0.4963 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.6037 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4986 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9840 | no |
| unknown | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5230 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4433 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4667 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5160 | no |
| unknown | business2 | blend50 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.6138 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3656 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4278 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4883 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3592 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9842 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9868 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4399 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4967 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5150 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9917 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9738 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9832 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4870 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9744 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5451 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.5081 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5272 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7749 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.6569 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.9059 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5164 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6592 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8502 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.6546 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9219 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9703 | yes |
| critical | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6550 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9704 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.7246 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.8874 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5072 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5295 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.6013 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.4860 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 0.9881 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4486 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.2867 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.8895 | no |
| unknown | business2 | blend60 | 1 | health service executive area | address | unknown | 0.4706 | no |
| unknown | business2 | blend60 | 1 | monitor | id | unknown | 0.4090 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9865 | no |
| unknown | business2 | blend60 | 1 | number_habitable_rooms_known | category | unknown | 0.4903 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5603 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9798 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5729 | no |
| unknown | business2 | blend60 | 1 | programme | category | unknown | 0.4702 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4408 | no |
| unknown | business2 | blend60 | 1 | situtation | address | unknown | 0.3345 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.3623 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4054 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4407 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9866 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9846 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9855 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4529 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5547 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.5877 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9885 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9735 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9779 | no |
| unknown | business2 | blend60 | 1 | want to live in this parish only | quantity | unknown | 0.4559 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9634 | no |
| wrong | business2 | blend60 | 1 | bike_stands | quantity | category | 0.6697 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.5487 | no |
| wrong | business2 | blend60 | 1 | imd19_income_decile | category | amount | 0.5795 | no |
| wrong | business2 | blend60 | 1 | imd19_national_decile | category | quantity | 0.5792 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5706 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.8051 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7304 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6045 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5908 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.9241 | no |
| wrong | business2 | blend60 | 1 | service | account | org | 0.5099 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8342 | no |
| wrong | business2 | blend60 | 1 | surveyname | text | org | 0.5291 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.5004 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9343 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9766 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7494 | yes |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.7251 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.7401 | no |
| other_ng | business2 | blend60 | 2 | loc_y | other | address | 0.5602 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5838 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6002 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.3220 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.2921 | no |
| unknown | business2 | blend60 | 2 | contravention | category | unknown | 0.4915 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.4456 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9342 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.2873 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9893 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms_known | category | unknown | 0.4856 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4920 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9812 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5299 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4384 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4493 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5975 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4379 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4890 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3332 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9853 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9841 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9818 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9860 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5668 | no |
| unknown | business2 | blend60 | 2 | tree type | category | unknown | 0.4741 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5902 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6053 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9902 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9711 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9802 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9754 | no |
| wrong | business2 | blend60 | 2 | account name | account | org | 0.5654 | no |
| wrong | business2 | blend60 | 2 | body name | org | address | 0.5323 | no |
| wrong | business2 | blend60 | 2 | epc_score_known | category | quantity | 0.5162 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5756 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.5869 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5744 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7944 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5951 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.8975 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6602 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8719 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.6305 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9279 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9694 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6796 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9663 | yes |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.7095 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.5785 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.8924 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5344 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6116 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6924 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9861 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.2654 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.8820 | no |
| unknown | business2 | blend70 | 1 | health service executive area | address | unknown | 0.4693 | no |
| unknown | business2 | blend70 | 1 | monitor | id | unknown | 0.4057 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9848 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9768 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4838 | no |
| unknown | business2 | blend70 | 1 | situtation | address | unknown | 0.3494 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4937 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.3937 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4727 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9850 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9839 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9825 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9832 | no |
| unknown | business2 | blend70 | 1 | total_verified_sales | quantity | unknown | 0.5932 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9866 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9713 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9745 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9624 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.6743 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.5584 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.5046 | no |
| wrong | business2 | blend70 | 1 | epc_score_known | category | quantity | 0.5076 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6761 | no |
| wrong | business2 | blend70 | 1 | imd19_national_decile | category | quantity | 0.6295 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6657 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8263 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.6911 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.5683 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.5485 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6713 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6668 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9201 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.5941 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8576 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.5141 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.5632 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9413 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish only | quantity | category | 0.5028 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9768 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7897 | yes |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.7100 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.7206 | no |
| other_ng | business2 | blend70 | 2 | loc_y | other | address | 0.5751 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.3260 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.3061 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.4508 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9341 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.3351 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9785 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6043 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5115 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5242 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4898 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3482 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9824 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9833 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9819 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9794 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.4954 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.4720 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9886 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9685 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9771 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9764 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6595 | no |
| wrong | business2 | blend70 | 2 | body name | org | address | 0.5912 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.5866 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6715 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.6657 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6216 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8139 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.5333 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.5628 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.8890 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5102 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.6612 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8937 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.6064 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9338 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9669 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7535 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9539 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.5288 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.6641 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.7331 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9074 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.5762 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9656 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9802 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.2790 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8594 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4786 | no |
| unknown | business2 | ft | 1 | monitor | id | unknown | 0.4549 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9799 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9679 | no |
| unknown | business2 | ft | 1 | situtation | address | unknown | 0.4779 | no |
| unknown | business2 | ft | 1 | surveyname | text | unknown | 0.3874 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9805 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9782 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9762 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9783 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9799 | no |
| unknown | business2 | ft | 1 | total_verified_sales | quantity | unknown | 0.4959 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9810 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9646 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9642 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9593 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.6879 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.7759 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.6849 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9658 | no |
| wrong | business2 | ft | 1 | imd19_national_decile | category | quantity | 0.7802 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9509 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.8901 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.5733 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8025 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.7833 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.8716 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.8948 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9081 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.8470 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9275 | no |
| wrong | business2 | ft | 1 | surveyname | text | address | 0.5152 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.6747 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.7342 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.7515 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9623 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.7108 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9774 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9107 | yes |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.6649 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.6619 | no |
| other_ng | business2 | ft | 2 | loc_y | other | address | 0.6200 | no |
| unknown | business2 | ft | 2 | amt-units_mnt-unite | category | unknown | 0.3945 | no |
| unknown | business2 | ft | 2 | construction_age_band | category | unknown | 0.4154 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9838 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4662 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9339 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.4787 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9846 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.5894 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9702 | no |
| unknown | business2 | ft | 2 | potential_epc_rating_known | category | unknown | 0.4854 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7307 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7489 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4921 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4971 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9766 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9772 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9753 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9721 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9829 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.3587 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9838 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9607 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9679 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9793 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9418 | no |
| wrong | business2 | ft | 2 | body name | org | address | 0.5966 | no |
| wrong | business2 | ft | 2 | body name | org | address | 0.7678 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.7977 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9592 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.9021 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.7634 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.8723 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.7947 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.5424 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.8637 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.7270 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.6641 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9588 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.5342 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9517 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8682 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.5473 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4911 | no |
| unknown | dev220 | blend50 | 1 | 受注郵便番号 | address | unknown | 0.4993 | no |
| unknown | dev220 | blend50 | 1 | 履行場所 | address | unknown | 0.4912 | no |
| unknown | dev220 | blend50 | 1 | 担当課 | org | unknown | 0.4890 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4902 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8337 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5639 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.7842 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.7274 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8200 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.3998 | no |
| unknown | dev220 | blend50 | 2 | receive_order_import_type_id | category | unknown | 0.4678 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4955 | no |
| unknown | dev220 | blend50 | 2 | 履行場所 | address | unknown | 0.4907 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4990 | no |
| unknown | dev220 | blend50 | 2 | 発送郵便番号 | address | unknown | 0.4999 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.7473 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5525 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.9610 | no |
| wrong | dev220 | blend50 | 2 | 受注郵便番号 | address | id | 0.5074 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8821 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8277 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6376 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.7440 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.7222 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.5097 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8243 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.3716 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.7241 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6239 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.9561 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8961 | yes |
| unknown | dev220 | blend70 | 1 | 税率 | rate | unknown | 0.4853 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8217 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7112 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.7037 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.7170 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.5777 | no |
| wrong | dev220 | blend70 | 1 | 支払者の氏名又は名称 | org | person | 0.5110 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8286 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.3489 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.7008 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.6952 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9513 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9380 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8037 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9321 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.5830 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.7014 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7815 | no |
| wrong | dev220 | ft | 1 | 支払者の氏名又は名称 | org | person | 0.7214 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.6408 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.8416 | yes |
| unknown | dev220 | ft | 2 | credit limit | amount | unknown | 0.4027 | no |
| unknown | dev220 | ft | 2 | 商品オプション | text | unknown | 0.4630 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.6309 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9093 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9366 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6989 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.8194 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.8463 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.8055 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7552 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.4618 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.5211 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.4821 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4754 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4865 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7537 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9089 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.9704 | no |
| unknown | general | blend50 | 1 | indicator | text | unknown | 0.4975 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.5871 | no |
| unknown | general | blend50 | 1 | place | org | unknown | 0.4765 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.2260 | no |
| unknown | general | blend50 | 1 | sens_final | rate | unknown | 0.5051 | no |
| unknown | general | blend50 | 1 | source_value | category | unknown | 0.4932 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.4267 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2073 | no |
| unknown | general | blend50 | 1 | term | text | unknown | 0.4951 | no |
| unknown | general | blend50 | 1 | 住家一部損壊 | quantity | unknown | 0.3963 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4977 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4950 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4756 | no |
| unknown | general | blend50 | 1 | 日本語教室名 | org | unknown | 0.4893 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9277 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4977 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9898 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9305 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5925 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5761 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.7511 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.5263 | no |
| wrong | general | blend50 | 1 | standardhours | quantity | category | 0.6357 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.8709 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5363 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.8513 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.9324 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8196 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9218 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7950 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.5129 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.5593 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.5178 | no |
| unknown | general | blend50 | 2 | author | person | unknown | 0.4710 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4818 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4268 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.6797 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9094 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.5660 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9724 | no |
| unknown | general | blend50 | 2 | ngram | text | unknown | 0.4360 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4690 | no |
| unknown | general | blend50 | 2 | pir_sha | id | unknown | 0.5895 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.4549 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.3610 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4817 | no |
| unknown | general | blend50 | 2 | sens_final | rate | unknown | 0.5122 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4833 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.3811 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.3618 | no |
| unknown | general | blend50 | 2 | 住家一部損壊 | quantity | unknown | 0.4472 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4890 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.4631 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.3456 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4963 | no |
| unknown | general | blend50 | 2 | 次に掲げるもの | category | unknown | 0.4842 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9307 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3814 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9913 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9184 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4601 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.7056 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8072 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8715 | no |
| wrong | general | blend50 | 2 | standardhours | quantity | category | 0.5863 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8227 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6713 | no |
| other_ng | general | blend60 | 1 | episode | other | quantity | 0.5198 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.7947 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.8491 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.7675 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7762 | no |
| unknown | general | blend60 | 1 | age_q1_nd | quantity | unknown | 0.4040 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.4607 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.4211 | no |
| unknown | general | blend60 | 1 | bib | id | unknown | 0.4300 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.7979 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9237 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9715 | no |
| unknown | general | blend60 | 1 | indicator | text | unknown | 0.4901 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.2518 | no |
| unknown | general | blend60 | 1 | raw | category | unknown | 0.4416 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5729 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.5178 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4401 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.2256 | no |
| unknown | general | blend60 | 1 | 住家一部損壊 | quantity | unknown | 0.3569 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.4040 | no |
| unknown | general | blend60 | 1 | 東第5 | quantity | unknown | 0.5090 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9358 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9877 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9320 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.5186 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5032 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.7319 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.5405 | no |
| wrong | general | blend60 | 1 | standardhours | quantity | category | 0.6510 | no |
| wrong | general | blend60 | 1 | term | text | category | 0.5826 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.8567 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.5892 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5503 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.8541 | no |
| other_ng | general | blend60 | 2 | episode | other | quantity | 0.5178 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.9303 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8170 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9071 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8240 | no |
| unknown | general | blend60 | 2 | age_q1_nd | quantity | unknown | 0.4653 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.5065 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.4496 | no |
| unknown | general | blend60 | 2 | bib | id | unknown | 0.3809 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.7090 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9244 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.5000 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9740 | no |
| unknown | general | blend60 | 2 | ngram | text | unknown | 0.4378 | no |
| unknown | general | blend60 | 2 | pelicula | text | unknown | 0.3870 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4218 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.3881 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5815 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4794 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4361 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.4151 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3935 | no |
| unknown | general | blend60 | 2 | 天候 | category | unknown | 0.4117 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9394 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.4496 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9895 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9176 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4589 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6543 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7806 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.8763 | no |
| wrong | general | blend60 | 2 | standardhours | quantity | category | 0.5918 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.7989 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.5195 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6436 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.6045 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.7701 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.8519 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.7295 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7973 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.3989 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.4324 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.4905 | no |
| unknown | general | blend70 | 1 | bib | id | unknown | 0.3735 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4446 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8420 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9386 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9727 | no |
| unknown | general | blend70 | 1 | indicator | text | unknown | 0.4827 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.2843 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.3633 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6408 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.6041 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.4534 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.2439 | no |
| unknown | general | blend70 | 1 | 住家一部損壊 | quantity | unknown | 0.3950 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3103 | no |
| unknown | general | blend70 | 1 | 東第5 | quantity | unknown | 0.4280 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9438 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9857 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9336 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.7126 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6046 | no |
| wrong | general | blend70 | 1 | standardhours | quantity | category | 0.6663 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6789 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8425 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.6807 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.5643 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.8569 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6021 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9282 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.5627 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8145 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.8924 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8530 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.4177 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.4537 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.3814 | no |
| unknown | general | blend70 | 2 | bib | id | unknown | 0.4080 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.7384 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9393 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.4437 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9755 | no |
| unknown | general | blend70 | 2 | pelicula | text | unknown | 0.4389 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.4826 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.4056 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6507 | no |
| unknown | general | blend70 | 2 | source | category | unknown | 0.4286 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.5593 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.4911 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.4684 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4351 | no |
| unknown | general | blend70 | 2 | 天候 | category | unknown | 0.4777 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9480 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9878 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9167 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4576 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.6029 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.7539 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.8811 | no |
| wrong | general | blend70 | 2 | ngram | text | org | 0.5074 | no |
| wrong | general | blend70 | 2 | standardhours | quantity | category | 0.5972 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.7751 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.5178 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.7247 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.5606 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.5630 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.8584 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.6961 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.8604 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.6154 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8604 | no |
| unknown | general | ft | 1 | bib | id | unknown | 0.4810 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9745 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9832 | no |
| unknown | general | ft | 1 | domain | category | unknown | 0.3977 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9762 | no |
| unknown | general | ft | 1 | indicator | text | unknown | 0.4604 | no |
| unknown | general | ft | 1 | keywords | text | unknown | 0.4567 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.3816 | no |
| unknown | general | ft | 1 | raw | category | unknown | 0.5182 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.8442 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4052 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.8630 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4933 | no |
| unknown | general | ft | 1 | study | text | unknown | 0.2987 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4189 | no |
| unknown | general | ft | 1 | 東第5 | quantity | unknown | 0.5936 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9679 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9796 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9382 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.5774 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.6550 | no |
| wrong | general | ft | 1 | ngram | text | category | 0.5089 | no |
| wrong | general | ft | 1 | place | org | address | 0.7967 | no |
| wrong | general | ft | 1 | standardhours | quantity | category | 0.7123 | no |
| wrong | general | ft | 1 | term | text | category | 0.9678 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8001 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9551 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.6062 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.8653 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.5779 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8550 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9221 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.7976 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.8069 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.8482 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9400 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.4959 | no |
| unknown | general | ft | 2 | bib | id | unknown | 0.4894 | no |
| unknown | general | ft | 2 | cause_of_invalid_ranking | text | unknown | 0.4944 | no |
| unknown | general | ft | 2 | cleaned | text | unknown | 0.4877 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.8265 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9843 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9803 | no |
| unknown | general | ft | 2 | keywords | text | unknown | 0.4918 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.6649 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.5787 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8585 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.7989 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.6560 | no |
| unknown | general | ft | 2 | units | category | unknown | 0.5719 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.6118 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9739 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9826 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9141 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.4539 | no |
| wrong | general | ft | 2 | goal | id | category | 0.6740 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.8957 | no |
| wrong | general | ft | 2 | ngram | text | org | 0.7162 | no |
| wrong | general | ft | 2 | source | category | org | 0.5643 | no |
| wrong | general | ft | 2 | standardhours | quantity | category | 0.6136 | no |
| wrong | general | ft | 2 | study | text | person | 0.6284 | no |
| wrong | general | ft | 2 | term | text | category | 0.5273 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7037 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.5643 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.7224 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9814 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9865 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9792 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9854 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9771 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9843 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9707 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9809 | no |

### unknown の判定理由

- date_value_evidence_low: 116件
- numeric_top2_too_close: 52件
- numeric_values_not_parseable: 29件
- other_class: 112件
- probability_below_threshold: 307件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 45件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 243件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 192件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
