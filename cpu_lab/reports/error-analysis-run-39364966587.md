# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-20T04:05:03+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 13 | 2 | 33 | 0 |
| business | blend50 | 2 | 490 | 14 | 1 | 29 | 0 |
| business | blend60 | 1 | 490 | 19 | 1 | 24 | 0 |
| business | blend60 | 2 | 490 | 23 | 3 | 21 | 0 |
| business | blend70 | 1 | 490 | 20 | 1 | 20 | 0 |
| business | blend70 | 2 | 490 | 25 | 3 | 16 | 0 |
| business | ft | 1 | 490 | 27 | 1 | 12 | 0 |
| business | ft | 2 | 490 | 32 | 5 | 9 | 1 |
| business2 | blend50 | 1 | 976 | 19 | 6 | 33 | 4 |
| business2 | blend50 | 2 | 976 | 17 | 4 | 39 | 3 |
| business2 | blend60 | 1 | 976 | 22 | 5 | 32 | 2 |
| business2 | blend60 | 2 | 976 | 24 | 4 | 28 | 4 |
| business2 | blend70 | 1 | 976 | 23 | 4 | 26 | 3 |
| business2 | blend70 | 2 | 976 | 25 | 4 | 22 | 6 |
| business2 | ft | 1 | 976 | 25 | 4 | 21 | 5 |
| business2 | ft | 2 | 976 | 28 | 4 | 20 | 7 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend60 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 2 | 0 |
| general | blend50 | 1 | 383 | 6 | 0 | 26 | 6 |
| general | blend50 | 2 | 383 | 6 | 0 | 25 | 4 |
| general | blend60 | 1 | 383 | 7 | 1 | 22 | 6 |
| general | blend60 | 2 | 383 | 7 | 0 | 17 | 6 |
| general | blend70 | 1 | 383 | 6 | 1 | 20 | 6 |
| general | blend70 | 2 | 383 | 7 | 0 | 18 | 6 |
| general | ft | 1 | 383 | 7 | 2 | 15 | 6 |
| general | ft | 2 | 383 | 7 | 0 | 17 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 8, category→quantity: 6, quantity→amount: 2, text→category: 2, account→text: 2, text→account: 2, product→text: 1, org→address: 1
- business / blend60: category→quantity: 19, org→account: 7, org→address: 2, text→category: 2, account→text: 2, text→account: 2, category→account: 2, amount→quantity: 2
- business / blend70: category→quantity: 21, org→account: 7, amount→quantity: 3, org→address: 2, text→category: 2, account→text: 2, text→account: 2, category→account: 2
- business / ft: category→quantity: 26, org→account: 8, category→account: 4, amount→quantity: 4, org→address: 2, text→category: 2, account→text: 2, text→account: 2
- business2 / blend50: amount→quantity: 8, account→category: 4, quantity→category: 4, text→org: 3, category→id: 3, category→text: 3, quantity→amount: 2, category→quantity: 2
- business2 / blend60: amount→quantity: 8, quantity→category: 6, account→category: 4, category→id: 4, category→quantity: 3, category→address: 2, id→category: 2, org→address: 2
- business2 / blend70: amount→quantity: 7, quantity→category: 5, category→quantity: 5, account→category: 4, category→id: 4, quantity→address: 4, category→address: 2, id→category: 2
- business2 / ft: category→quantity: 9, amount→quantity: 7, quantity→category: 7, category→id: 4, quantity→address: 4, account→category: 3, category→address: 2, id→category: 2
- dev220 / blend50: quantity→category: 4, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- dev220 / blend60: quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→account: 1, category→text: 1, address→id: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- general / blend50: quantity→category: 4, category→text: 2, text→category: 2, org→address: 1, id→address: 1, address→org: 1, id→category: 1
- general / blend60: text→category: 3, quantity→category: 3, category→text: 2, id→address: 2, org→address: 1, id→quantity: 1, address→org: 1, id→category: 1
- general / blend70: quantity→category: 3, category→text: 2, text→category: 2, id→address: 2, org→address: 1, id→quantity: 1, address→org: 1, id→category: 1
- general / ft: category→text: 3, text→category: 2, id→address: 2, date→id: 1, org→address: 1, address→category: 1, id→quantity: 1, address→org: 1

### seedをまたいで再発した誤り

- business / blend50: `d6`、category→quantity（seed 1, seed 2）
- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `agebann`、category→quantity（seed 1, seed 2）
- business / blend60: `d1`、category→quantity（seed 1, seed 2）
- business / blend60: `d6`、category→quantity（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `publisher label`、org→address（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `q2a`、category→quantity（seed 1, seed 2）
- business / blend60: `q5a`、category→quantity（seed 1, seed 2）
- business / blend60: `q5b`、category→quantity（seed 1, seed 2）
- business / blend60: `q6`、category→quantity（seed 1, seed 2）
- business / blend60: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `agebann`、category→quantity（seed 1, seed 2）
- business / blend70: `d1`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `sub_category`、category→account（seed 1, seed 2）
- business2 / blend50: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `surveyname`、text→org（seed 1, seed 2）
- business2 / blend50: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `want to live in this parish only`、quantity→category（seed 1, seed 2）
- business2 / blend70: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `want to live in this parish only`、quantity→category（seed 1, seed 2）
- business2 / ft: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / ft: `epc_score_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `want to live in this parish only`、quantity→category（seed 1, seed 2）
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
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.6451 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9882 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5250 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5194 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.2857 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5143 | no |
| unknown | business | blend50 | 1 | class-title_en | category | unknown | 0.3980 | no |
| unknown | business | blend50 | 1 | class-title_fr | category | unknown | 0.4438 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4301 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4799 | no |
| unknown | business | blend50 | 1 | d2 | category | unknown | 0.3667 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5360 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4053 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9881 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9362 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.5783 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.4114 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3519 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5582 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4787 | no |
| unknown | business | blend50 | 1 | q2a | category | unknown | 0.4902 | no |
| unknown | business | blend50 | 1 | q3_1 | category | unknown | 0.4828 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4653 | no |
| unknown | business | blend50 | 1 | q4b_1 | category | unknown | 0.4443 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4969 | no |
| unknown | business | blend50 | 1 | q6 | category | unknown | 0.4965 | no |
| unknown | business | blend50 | 1 | q8 | category | unknown | 0.4876 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9808 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9804 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3864 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.5272 | no |
| unknown | business | blend50 | 1 | segment-title_fr | category | unknown | 0.4153 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4613 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9823 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9040 | no |
| wrong | business | blend50 | 1 | agebann | category | quantity | 0.5157 | no |
| wrong | business | blend50 | 1 | commodity-title_fr | product | text | 0.5136 | no |
| wrong | business | blend50 | 1 | d6 | category | quantity | 0.5612 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9847 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.7661 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9886 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.6670 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.8692 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.8282 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8226 | no |
| wrong | business | blend50 | 1 | q7 | category | quantity | 0.5246 | no |
| critical | business | blend50 | 2 | mois calendrier | date | quantity | 0.5617 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5039 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5102 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4740 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5186 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4513 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5012 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4054 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4004 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4913 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.4152 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5326 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.3840 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9902 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9336 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.5880 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5675 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4118 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.4506 | no |
| unknown | business | blend50 | 2 | q2a | category | unknown | 0.4953 | no |
| unknown | business | blend50 | 2 | q3_1 | category | unknown | 0.4948 | no |
| unknown | business | blend50 | 2 | q3_2 | category | unknown | 0.4759 | no |
| unknown | business | blend50 | 2 | q5b | category | unknown | 0.4949 | no |
| unknown | business | blend50 | 2 | q6 | category | unknown | 0.4901 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9878 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9784 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3507 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5576 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9457 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7901 | no |
| wrong | business | blend50 | 2 | capital revenue | category | account | 0.5589 | no |
| wrong | business | blend50 | 2 | d6 | category | quantity | 0.5715 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9760 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7601 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9807 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7201 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7613 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5270 | no |
| wrong | business | blend50 | 2 | publisher label | org | address | 0.5096 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8484 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5140 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5238 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.8020 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9868 | yes |
| unknown | business | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5802 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5523 | no |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6126 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.2545 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.4481 | no |
| unknown | business | blend60 | 1 | class-title_en | category | unknown | 0.3730 | no |
| unknown | business | blend60 | 1 | class-title_fr | category | unknown | 0.4989 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.3637 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4638 | no |
| unknown | business | blend60 | 1 | d2 | category | unknown | 0.3102 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.3355 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9863 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9439 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.4896 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4209 | no |
| unknown | business | blend60 | 1 | q3_1 | category | unknown | 0.4779 | no |
| unknown | business | blend60 | 1 | q3_2 | category | unknown | 0.3737 | no |
| unknown | business | blend60 | 1 | q4b_1 | category | unknown | 0.4693 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9782 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9809 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.4298 | no |
| unknown | business | blend60 | 1 | segment-title_fr | category | unknown | 0.4413 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9828 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9150 | no |
| wrong | business | blend60 | 1 | agebann | category | quantity | 0.6019 | no |
| wrong | business | blend60 | 1 | d1 | category | quantity | 0.5734 | no |
| wrong | business | blend60 | 1 | d6 | category | quantity | 0.6390 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9843 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.7939 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9880 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6958 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.8902 | no |
| wrong | business | blend60 | 1 | portefeuille_nom_et_code | org | account | 0.7991 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.5618 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.7974 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.5714 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.5563 | no |
| wrong | business | blend60 | 1 | q5b | category | quantity | 0.5924 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.5888 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.6128 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.5704 | no |
| wrong | business | blend60 | 1 | title | category | account | 0.5403 | no |
| critical | business | blend60 | 2 | australian sourced goods | amount | quantity | 0.5416 | yes |
| critical | business | blend60 | 2 | mois calendrier | date | quantity | 0.5199 | yes |
| critical | business | blend60 | 2 | overseas sourced services | amount | quantity | 0.5360 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5986 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6049 | no |
| unknown | business | blend60 | 2 | account_name | account | unknown | 0.4998 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6117 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.4434 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4455 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.3280 | no |
| unknown | business | blend60 | 2 | d2 | category | unknown | 0.4777 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.3868 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9888 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9408 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.4942 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4672 | no |
| unknown | business | blend60 | 2 | q3_2 | category | unknown | 0.4091 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9866 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9786 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4208 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5182 | no |
| unknown | business | blend60 | 2 | tournée | id | unknown | 0.5145 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9389 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.7784 | no |
| wrong | business | blend60 | 2 | agebann | category | quantity | 0.5518 | no |
| wrong | business | blend60 | 2 | capital revenue | category | account | 0.6178 | no |
| wrong | business | blend60 | 2 | d1 | category | quantity | 0.5871 | no |
| wrong | business | blend60 | 2 | d6 | category | quantity | 0.6514 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9739 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7868 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9785 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.7595 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7608 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.5181 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5989 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8284 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.5893 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.5899 | no |
| wrong | business | blend60 | 2 | q5a | category | quantity | 0.5692 | no |
| wrong | business | blend60 | 2 | q5b | category | quantity | 0.5772 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.5810 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6001 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.6138 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.7927 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9854 | yes |
| unknown | business | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5153 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.2906 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.5162 | no |
| unknown | business | blend70 | 1 | class-title_en | category | unknown | 0.4068 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3626 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4141 | no |
| unknown | business | blend70 | 1 | d2 | category | unknown | 0.3448 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.3570 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9844 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9517 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.5679 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.4900 | no |
| unknown | business | blend70 | 1 | q3_2 | category | unknown | 0.4270 | no |
| unknown | business | blend70 | 1 | q4b_1 | category | unknown | 0.4944 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9757 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9815 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.4732 | no |
| unknown | business | blend70 | 1 | segment-title_fr | category | unknown | 0.4673 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9833 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9261 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.6881 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6670 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7169 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9839 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8218 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9874 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7245 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.9112 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | account | 0.7700 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6449 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7722 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.6623 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.5542 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6471 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6878 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.6810 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7010 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.6531 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.6225 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6319 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.5765 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.6215 | yes |
| unknown | business | blend70 | 2 | account_name | account | unknown | 0.4813 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.5173 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.4856 | no |
| unknown | business | blend70 | 2 | commodity-title_fr | product | unknown | 0.2556 | no |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.4121 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9874 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9480 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.4782 | no |
| unknown | business | blend70 | 2 | q3_2 | category | unknown | 0.4741 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9855 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9788 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4909 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.6038 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.4434 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9322 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.7667 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.5553 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.6296 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.6766 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.6829 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.5403 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7313 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9718 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8135 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9763 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.7989 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7602 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5830 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6882 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8084 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6832 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6849 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6622 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.6700 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6720 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.6863 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7038 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.7835 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9812 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.3987 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4302 | no |
| unknown | business | ft | 1 | commodity-title_fr | product | unknown | 0.4632 | no |
| unknown | business | ft | 1 | d2 | category | unknown | 0.4712 | no |
| unknown | business | ft | 1 | department | org | unknown | 0.4888 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9789 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9748 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.8027 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9681 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9831 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9849 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9592 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.9466 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9476 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9505 | no |
| wrong | business | ft | 1 | department | org | account | 0.9827 | no |
| wrong | business | ft | 1 | department | org | account | 0.9054 | no |
| wrong | business | ft | 1 | department | org | account | 0.9856 | no |
| wrong | business | ft | 1 | description | account | text | 0.8109 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.5081 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9743 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | account | 0.6828 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.8943 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.6966 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9352 | no |
| wrong | business | ft | 1 | q2b | category | quantity | 0.5532 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.7834 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.6020 | no |
| wrong | business | ft | 1 | q4a | category | quantity | 0.5200 | no |
| wrong | business | ft | 1 | q4b_1 | category | quantity | 0.5696 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9195 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9741 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9577 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9657 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9014 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.6033 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.5108 | no |
| wrong | business | ft | 1 | title | category | account | 0.8691 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9027 | yes |
| critical | business | ft | 2 | australian sourced services | amount | quantity | 0.7390 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.8235 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.8779 | yes |
| critical | business | ft | 2 | tournée | id | quantity | 0.6318 | yes |
| other_ng | business | ft | 2 | km budgété | other | quantity | 0.5009 | no |
| unknown | business | ft | 2 | commodity-title_fr | product | unknown | 0.3309 | no |
| unknown | business | ft | 2 | entitiy | org | unknown | 0.4879 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9831 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9696 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.3583 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9822 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9793 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9118 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.7315 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.6407 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.7219 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.8631 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.8531 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.6059 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.9703 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.7278 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9711 | no |
| wrong | business | ft | 2 | department | org | account | 0.9654 | no |
| wrong | business | ft | 2 | department | org | account | 0.8935 | no |
| wrong | business | ft | 2 | department | org | account | 0.9697 | no |
| wrong | business | ft | 2 | description | account | text | 0.9171 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.7586 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7777 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9561 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7482 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9650 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9700 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.6694 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9411 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9487 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9448 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9447 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9738 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | tax_class | 0.7011 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.5088 | no |
| wrong | business | ft | 2 | title | category | text | 0.7557 | no |
| critical | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.6486 | yes |
| critical | business2 | blend50 | 1 | fine | amount | quantity | 0.5439 | yes |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9814 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6807 | yes |
| critical | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7194 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9885 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.7241 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.7802 | no |
| other_ng | business2 | blend50 | 1 | b1a floorspace net sqm | other | amount | 0.5035 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5151 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5388 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.5079 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3589 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 0.9940 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.8869 | no |
| unknown | business2 | blend50 | 1 | imd19_income_decile | category | unknown | 0.4408 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.3605 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.3772 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4962 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9879 | no |
| unknown | business2 | blend50 | 1 | programme | category | unknown | 0.4520 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5424 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3174 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.4629 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4081 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4140 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4119 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3818 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4388 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5015 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5086 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9925 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9835 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9895 | no |
| unknown | business2 | blend50 | 1 | want to live in this parish only | quantity | unknown | 0.4470 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4264 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9643 | no |
| wrong | business2 | blend50 | 1 | bike_stands | quantity | category | 0.8094 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.7940 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.6908 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7566 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9205 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5792 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5480 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.8720 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5632 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.5889 | no |
| wrong | business2 | blend50 | 1 | surveyname | text | org | 0.5032 | no |
| wrong | business2 | blend50 | 1 | total_floor_area_known | category | quantity | 0.5061 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9345 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9803 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8860 | yes |
| critical | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.8550 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7138 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.8469 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8749 | no |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5160 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5021 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5105 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.4281 | no |
| unknown | business2 | blend50 | 2 | apartment | quantity | unknown | 0.3793 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.3659 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 0.9938 | no |
| unknown | business2 | blend50 | 2 | epc_rating_known | category | unknown | 0.4604 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4052 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9200 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.3094 | no |
| unknown | business2 | blend50 | 2 | locationname | address | unknown | 0.4982 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.3437 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5516 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.6081 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.4981 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4973 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9869 | no |
| unknown | business2 | blend50 | 2 | potential_epc_rating_known | category | unknown | 0.4319 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4997 | no |
| unknown | business2 | blend50 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.5945 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4292 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4057 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4512 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4581 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9858 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5357 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4963 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5203 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9940 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9846 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | want to live in this parish only | quantity | unknown | 0.4725 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.3874 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9761 | no |
| wrong | business2 | blend50 | 2 | bike_stands | quantity | category | 0.7981 | no |
| wrong | business2 | blend50 | 2 | fine | amount | category | 0.5465 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7195 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.6285 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5198 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.9311 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5163 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.5505 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8430 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8250 | no |
| wrong | business2 | blend50 | 2 | total_floor_area_known | category | quantity | 0.5160 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9242 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.6646 | no |
| critical | business2 | blend60 | 1 | fine | amount | quantity | 0.6322 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9826 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6363 | yes |
| critical | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7618 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9872 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.7059 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.7648 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5843 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5345 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.5985 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.3755 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 0.9929 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4922 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.8773 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.3771 | no |
| unknown | business2 | blend60 | 1 | monitor | id | unknown | 0.3944 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9899 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5596 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4770 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3805 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.4554 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.4479 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4912 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4940 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4580 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4103 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5837 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.5976 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9911 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9828 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9877 | no |
| unknown | business2 | blend60 | 1 | warddesc | address | unknown | 0.3626 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9632 | no |
| wrong | business2 | blend60 | 1 | bike_stands | quantity | category | 0.8428 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.7902 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6980 | no |
| wrong | business2 | blend60 | 1 | imd19_income_decile | category | amount | 0.5290 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5650 | no |
| wrong | business2 | blend60 | 1 | merchant description | category | org | 0.5211 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.7724 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9115 | no |
| wrong | business2 | blend60 | 1 | programme | category | account | 0.5423 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6542 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6306 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.8567 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.5678 | no |
| wrong | business2 | blend60 | 1 | situtation | address | text | 0.5456 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.5826 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9429 | no |
| wrong | business2 | blend60 | 1 | want to live in this parish only | quantity | category | 0.5194 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9813 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8826 | yes |
| critical | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.8507 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7550 | yes |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.8532 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace losses sqm | other | quantity | 0.5935 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8784 | no |
| other_ng | business2 | blend60 | 2 | d2 floorspace gains sqm | other | quantity | 0.6040 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5964 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6052 | no |
| unknown | business2 | blend60 | 2 | apartment | quantity | unknown | 0.3763 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.3935 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 0.9926 | no |
| unknown | business2 | blend60 | 2 | epc_rating_known | category | unknown | 0.4504 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4675 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9170 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.3015 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.3542 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9915 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.3987 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9848 | no |
| unknown | business2 | blend60 | 2 | potential_epc_rating_known | category | unknown | 0.4191 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3571 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5450 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5918 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6117 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9929 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9842 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9899 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4456 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9774 | no |
| wrong | business2 | blend60 | 2 | account name | account | org | 0.5633 | no |
| wrong | business2 | blend60 | 2 | bike_stands | quantity | category | 0.8293 | no |
| wrong | business2 | blend60 | 2 | fine | amount | category | 0.5729 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5288 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7279 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5610 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.5294 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5830 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5727 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.9277 | no |
| wrong | business2 | blend60 | 2 | service | account | org | 0.5142 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.5297 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8633 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8351 | no |
| wrong | business2 | blend60 | 2 | terrace | quantity | address | 0.5412 | no |
| wrong | business2 | blend60 | 2 | terrace | quantity | address | 0.5496 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.5945 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9307 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.6798 | no |
| wrong | business2 | blend60 | 2 | want to live in this parish only | quantity | category | 0.5635 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7205 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9838 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8042 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9858 | yes |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.6876 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.5264 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.7494 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5201 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6174 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6891 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.4000 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9917 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4749 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.8678 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.3937 | no |
| unknown | business2 | blend70 | 1 | monitor | id | unknown | 0.4117 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9889 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9839 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5918 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.3909 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.4436 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4077 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9891 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.4672 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9896 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9821 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9858 | no |
| unknown | business2 | blend70 | 1 | warddesc | address | unknown | 0.4212 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9621 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8762 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.7864 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.7052 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6171 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6591 | no |
| wrong | business2 | blend70 | 1 | merchant description | category | org | 0.5890 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.7882 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9024 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6325 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7292 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7133 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.8415 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5467 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6282 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.5761 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.5342 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6591 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9514 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish only | quantity | category | 0.6031 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9823 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8792 | yes |
| critical | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.8465 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7963 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.5773 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.8596 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.6561 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8819 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace gains sqm | other | quantity | 0.5744 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.6743 | no |
| unknown | business2 | blend70 | 2 | apartment | quantity | unknown | 0.3734 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4210 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9913 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9141 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.3517 | no |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.3648 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9906 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.4935 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4063 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9826 | no |
| unknown | business2 | blend70 | 2 | potential_epc_rating_known | category | unknown | 0.4841 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4119 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9816 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9917 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9838 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9884 | no |
| unknown | business2 | blend70 | 2 | want to live in this parish & band d | quantity | unknown | 0.4928 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9787 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6570 | no |
| wrong | business2 | blend70 | 2 | bike_stands | quantity | category | 0.8604 | no |
| wrong | business2 | blend70 | 2 | epc_rating_known | category | quantity | 0.5201 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.5297 | no |
| wrong | business2 | blend70 | 2 | fine | amount | category | 0.5992 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6169 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.7363 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6140 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6462 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6457 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9243 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5992 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.5090 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8836 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8451 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6311 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6412 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.6729 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9371 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.6950 | no |
| wrong | business2 | blend70 | 2 | want to live in this parish only | quantity | category | 0.6545 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9855 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9874 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9314 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9818 | yes |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.6329 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.6587 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.7030 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.6117 | no |
| other_ng | business2 | ft | 1 | potential_epc_score | other | quantity | 0.5309 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9609 | no |
| unknown | business2 | ft | 1 | construction_age_band | category | unknown | 0.4736 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9882 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8392 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4629 | no |
| unknown | business2 | ft | 1 | monitor | id | unknown | 0.4634 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9856 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9780 | no |
| unknown | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5096 | no |
| unknown | business2 | ft | 1 | scheme_description | category | unknown | 0.4682 | no |
| unknown | business2 | ft | 1 | service_responsable | account | unknown | 0.4870 | no |
| unknown | business2 | ft | 1 | surveyname | text | unknown | 0.4841 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9863 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9835 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9853 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9801 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9803 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9589 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9764 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.7750 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.5153 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.7268 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.8816 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9416 | no |
| wrong | business2 | ft | 1 | merchant description | category | org | 0.7925 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.8356 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8752 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.5404 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9033 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9543 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9612 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.7958 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.6330 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8762 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.8225 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.7630 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.8884 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9768 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.8541 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9853 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8689 | yes |
| critical | business2 | ft | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.8336 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9202 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.7797 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.5674 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.8785 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.8440 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.8924 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.7772 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.8852 | no |
| unknown | business2 | ft | 2 | apartment | quantity | unknown | 0.4563 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9877 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9054 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.4700 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.5024 | no |
| unknown | business2 | ft | 2 | monitor | id | unknown | 0.3965 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9881 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.6780 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.5789 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9762 | no |
| unknown | business2 | ft | 2 | situtation | address | unknown | 0.4877 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9851 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9835 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9753 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9883 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9824 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9841 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9826 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9383 | no |
| wrong | business2 | ft | 2 | bike_stands | quantity | category | 0.9539 | no |
| wrong | business2 | ft | 2 | epc_rating_known | category | quantity | 0.7292 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.7164 | no |
| wrong | business2 | ft | 2 | fine | amount | category | 0.6784 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.8812 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.7616 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.8678 | no |
| wrong | business2 | ft | 2 | potential_epc_rating_known | category | quantity | 0.6791 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.5170 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8357 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8646 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9140 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8542 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9444 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.8752 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9011 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9157 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.9082 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9563 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.7405 | no |
| wrong | business2 | ft | 2 | want to live in this parish & band d | quantity | category | 0.6989 | no |
| wrong | business2 | ft | 2 | want to live in this parish and all others | quantity | category | 0.5579 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.9276 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8271 | yes |
| unknown | dev220 | blend50 | 1 | 履行場所 | address | unknown | 0.4832 | no |
| unknown | dev220 | blend50 | 1 | 担当課 | org | unknown | 0.4939 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8693 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5742 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.8027 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.6274 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8579 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.4749 | no |
| unknown | dev220 | blend50 | 2 | 履行場所 | address | unknown | 0.4701 | no |
| wrong | dev220 | blend50 | 2 | city | address | id | 0.7080 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.8797 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5839 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.9533 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8328 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8704 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6499 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.7661 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.6022 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.5192 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8698 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.5252 | no |
| unknown | dev220 | blend60 | 2 | 担当課 | org | unknown | 0.4900 | no |
| wrong | dev220 | blend60 | 2 | city | address | id | 0.7137 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.8829 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6615 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.9469 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8385 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8715 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7256 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.7296 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.5770 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.5887 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8817 | yes |
| wrong | dev220 | blend70 | 2 | city | address | id | 0.7193 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8861 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7392 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9405 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.5546 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.8557 | yes |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.4710 | no |
| unknown | dev220 | ft | 1 | 日付指定 | date | unknown | 0.4042 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8748 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9527 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.6199 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.5013 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7973 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9174 | yes |
| unknown | dev220 | ft | 2 | tax id | id | unknown | 0.4729 | no |
| unknown | dev220 | ft | 2 | 税率 | rate | unknown | 0.4793 | no |
| wrong | dev220 | ft | 2 | city | address | id | 0.7363 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8956 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9721 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9212 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.7486 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6944 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.5330 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5929 | no |
| other_ng | general | blend50 | 1 | operationid | other | category | 0.5452 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.7310 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.8784 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8034 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.4444 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.5102 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.4987 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4985 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4432 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7556 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9122 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.5572 | no |
| unknown | general | blend50 | 1 | goal | id | unknown | 0.4911 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.9119 | no |
| unknown | general | blend50 | 1 | itemfield14 | date | unknown | 0.5198 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.5921 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.2438 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4929 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.4097 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.3641 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2692 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4880 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4966 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4543 | no |
| unknown | general | blend50 | 1 | 日本語教室名 | org | unknown | 0.4743 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9369 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9929 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9442 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3712 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5877 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8825 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.5324 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.6275 | no |
| wrong | general | blend50 | 1 | 住家一部損壊 | quantity | category | 0.5058 | no |
| wrong | general | blend50 | 1 | 発生県 | id | address | 0.5104 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.9070 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.8718 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.6967 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8244 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7713 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.4480 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.4492 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.4687 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4969 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.7511 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9114 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.5057 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9693 | no |
| unknown | general | blend50 | 2 | pir_sha | id | unknown | 0.5837 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.2609 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4890 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4849 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4762 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4896 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.1967 | no |
| unknown | general | blend50 | 2 | 住家一部損壊 | quantity | unknown | 0.4023 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4926 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.4963 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.3761 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4967 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9351 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4896 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9927 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8843 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.8134 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8157 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8550 | no |
| wrong | general | blend50 | 2 | standardhours | quantity | category | 0.5333 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.6399 | no |
| wrong | general | blend50 | 2 | 読み方 | address | org | 0.5885 | no |
| critical | general | blend60 | 1 | goal | id | quantity | 0.5600 | yes |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6658 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.5854 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.5230 | no |
| other_ng | general | blend60 | 1 | operationid | other | category | 0.5435 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.7108 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.8549 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8340 | no |
| unknown | general | blend60 | 1 | age_q1_nd | quantity | unknown | 0.3832 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.4476 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.4267 | no |
| unknown | general | blend60 | 1 | bib | id | unknown | 0.3781 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.8002 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9277 | no |
| unknown | general | blend60 | 1 | female_frequency | rate | unknown | 0.4895 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9014 | no |
| unknown | general | blend60 | 1 | itemfield14 | date | unknown | 0.5352 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.2801 | no |
| unknown | general | blend60 | 1 | raw | category | unknown | 0.4868 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4704 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.3763 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3040 | no |
| unknown | general | blend60 | 1 | 住家一部損壊 | quantity | unknown | 0.4696 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3924 | no |
| unknown | general | blend60 | 1 | 日本語教室名 | org | unknown | 0.4597 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9467 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9915 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9485 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.3449 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.5128 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8896 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.6076 | no |
| wrong | general | blend60 | 1 | term | text | category | 0.5642 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.5646 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.6044 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.9209 | no |
| other_ng | general | blend60 | 2 | episode | other | quantity | 0.5300 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.8576 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.5626 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.6696 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.7902 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7956 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.4982 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.7947 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9268 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9703 | no |
| unknown | general | blend60 | 2 | place | org | unknown | 0.3107 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5754 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4359 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.5495 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.5663 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.1813 | no |
| unknown | general | blend60 | 2 | 住家一部損壊 | quantity | unknown | 0.4572 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3979 | no |
| unknown | general | blend60 | 2 | 天候 | category | unknown | 0.4482 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9446 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9912 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8766 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.7837 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7907 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.8565 | no |
| wrong | general | blend60 | 2 | standardhours | quantity | category | 0.5281 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.5795 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5794 | no |
| wrong | general | blend60 | 2 | 読み方 | address | org | 0.6129 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.6465 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6372 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6377 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.5413 | no |
| other_ng | general | blend70 | 1 | operationid | other | category | 0.5419 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.6906 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8315 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8647 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.3851 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.4469 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.4680 | no |
| unknown | general | blend70 | 1 | bib | id | unknown | 0.3129 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4379 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8447 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9433 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.8908 | no |
| unknown | general | blend70 | 1 | itemfield14 | date | unknown | 0.5507 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.3165 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4950 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.5311 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.3885 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3388 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3432 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9566 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9901 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9528 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3798 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8966 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6829 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6574 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.5018 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.6984 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9349 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6163 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.8435 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6539 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.6425 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.7560 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8198 | no |
| unknown | general | blend70 | 2 | app | category | unknown | 0.4778 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8384 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9422 | no |
| unknown | general | blend70 | 2 | funding | amount | unknown | 0.5855 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9713 | no |
| unknown | general | blend70 | 2 | ngram | text | unknown | 0.4461 | no |
| unknown | general | blend70 | 2 | place | org | unknown | 0.3618 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6618 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.5083 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.5115 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6411 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.6429 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.1873 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3059 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9542 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9897 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8689 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7539 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.7658 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.8581 | no |
| wrong | general | blend70 | 2 | standardhours | quantity | category | 0.5229 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.5192 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6693 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.6373 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.9061 | yes |
| critical | general | ft | 1 | itemfield14 | date | id | 0.5970 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.5515 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.7947 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.7681 | no |
| other_ng | general | ft | 1 | operationid | other | category | 0.5368 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.6299 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.7613 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9567 | no |
| unknown | general | ft | 1 | bib | id | unknown | 0.3567 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.3818 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9784 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9899 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.8593 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.4257 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3078 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.7132 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4251 | no |
| unknown | general | ft | 1 | study | text | unknown | 0.4432 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4805 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9862 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9859 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9656 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9178 | no |
| wrong | general | ft | 1 | place | org | address | 0.9085 | no |
| wrong | general | ft | 1 | term | text | category | 0.9371 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9805 | no |
| wrong | general | ft | 1 | 読み方 | address | category | 0.5418 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9767 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8753 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.8010 | no |
| other_ng | general | ft | 2 | nodes | other | category | 0.6012 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9279 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.5612 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.6534 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8926 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.5941 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9693 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9883 | no |
| unknown | general | ft | 2 | funding | amount | unknown | 0.4739 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9742 | no |
| unknown | general | ft | 2 | ngram | text | unknown | 0.4770 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9209 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.7253 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.6595 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9158 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.8730 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.2600 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.4342 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9827 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9854 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.8458 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.6645 | no |
| wrong | general | ft | 2 | goal | id | category | 0.6909 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.8627 | no |
| wrong | general | ft | 2 | standardhours | quantity | category | 0.5075 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.6173 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9388 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.7105 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9855 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9850 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9842 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9836 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9829 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9822 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9790 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9780 | no |

### unknown の判定理由

- date_value_evidence_low: 114件
- numeric_top2_too_close: 61件
- numeric_values_not_parseable: 29件
- other_class: 99件
- probability_below_threshold: 260件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 64件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 267件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 192件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
