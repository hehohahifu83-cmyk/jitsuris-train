# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-19T15:49:28+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 14 | 2 | 29 | 0 |
| business | blend50 | 2 | 490 | 10 | 0 | 32 | 1 |
| business | blend60 | 1 | 490 | 21 | 2 | 22 | 0 |
| business | blend60 | 2 | 490 | 19 | 3 | 24 | 1 |
| business | blend70 | 1 | 490 | 21 | 2 | 19 | 0 |
| business | blend70 | 2 | 490 | 23 | 4 | 16 | 0 |
| business | ft | 1 | 490 | 24 | 2 | 14 | 0 |
| business | ft | 2 | 490 | 29 | 5 | 9 | 0 |
| business2 | blend50 | 1 | 976 | 15 | 3 | 36 | 3 |
| business2 | blend50 | 2 | 976 | 15 | 4 | 39 | 4 |
| business2 | blend60 | 1 | 976 | 19 | 4 | 33 | 2 |
| business2 | blend60 | 2 | 976 | 17 | 3 | 32 | 2 |
| business2 | blend70 | 1 | 976 | 20 | 4 | 27 | 3 |
| business2 | blend70 | 2 | 976 | 20 | 3 | 25 | 4 |
| business2 | ft | 1 | 976 | 23 | 4 | 19 | 3 |
| business2 | ft | 2 | 976 | 20 | 2 | 25 | 8 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 4 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 4 | 0 |
| dev220 | blend60 | 1 | 220 | 7 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 7 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 3 | 0 | 2 | 0 |
| dev220 | ft | 1 | 220 | 7 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 4 | 0 | 2 | 0 |
| general | blend50 | 1 | 383 | 7 | 0 | 25 | 5 |
| general | blend50 | 2 | 383 | 6 | 0 | 26 | 4 |
| general | blend60 | 1 | 383 | 6 | 1 | 20 | 5 |
| general | blend60 | 2 | 383 | 5 | 0 | 23 | 6 |
| general | blend70 | 1 | 383 | 6 | 1 | 15 | 7 |
| general | blend70 | 2 | 383 | 5 | 1 | 22 | 6 |
| general | ft | 1 | 383 | 7 | 1 | 18 | 6 |
| general | ft | 2 | 383 | 6 | 1 | 21 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, category→quantity: 5, account→text: 2, text→account: 2, category→text: 2, quantity→amount: 1, text→category: 1, account→org: 1
- business / blend60: category→quantity: 16, org→account: 6, amount→quantity: 3, org→address: 2, account→text: 2, text→account: 2, category→text: 2, quantity→amount: 1
- business / blend70: category→quantity: 19, org→account: 6, amount→quantity: 5, org→address: 2, account→text: 2, text→account: 2, quantity→amount: 1, text→category: 1
- business / ft: category→quantity: 22, org→account: 7, amount→quantity: 5, org→address: 2, account→text: 2, text→account: 2, category→account: 2, account→category: 2
- business2 / blend50: amount→quantity: 6, account→category: 5, category→text: 4, id→category: 3, quantity→category: 3, category→id: 2, org→address: 2, text→org: 2
- business2 / blend60: amount→quantity: 6, account→category: 4, account→org: 3, id→category: 3, quantity→category: 3, category→id: 2, category→text: 2, category→amount: 2
- business2 / blend70: amount→quantity: 6, account→category: 4, id→category: 4, account→org: 3, quantity→category: 3, category→id: 2, quantity→address: 2, category→amount: 2
- business2 / ft: amount→quantity: 5, account→category: 4, category→quantity: 4, account→org: 3, id→category: 3, quantity→address: 3, quantity→category: 3, category→id: 2
- dev220 / blend50: quantity→category: 4, category→tax_class: 2, id→quantity: 2, category→text: 1
- dev220 / blend60: quantity→category: 4, category→tax_class: 2, id→quantity: 2, org→account: 1, text→category: 1, category→text: 1
- dev220 / blend70: quantity→category: 4, category→tax_class: 2, org→account: 1, text→category: 1, category→text: 1, id→quantity: 1
- dev220 / ft: quantity→category: 4, org→account: 2, category→tax_class: 2, text→category: 1, category→text: 1, id→quantity: 1
- general / blend50: quantity→category: 3, category→text: 2, id→address: 2, text→category: 2, id→category: 2, org→address: 1, address→org: 1
- general / blend60: category→text: 2, id→address: 2, text→category: 2, org→address: 1, id→quantity: 1, quantity→category: 1, address→org: 1, id→category: 1
- general / blend70: category→text: 2, id→address: 2, text→category: 2, id→quantity: 2, org→address: 1, quantity→category: 1, address→org: 1
- general / ft: category→text: 4, id→address: 2, id→quantity: 2, org→address: 1, quantity→category: 1, text→category: 1, address→org: 1, text→account: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `q7`、category→quantity（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend60: `d6`、category→quantity（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `publisher label`、org→address（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `q2a`、category→quantity（seed 1, seed 2）
- business / blend60: `q6`、category→quantity（seed 1, seed 2）
- business / blend60: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `q8`、category→quantity（seed 1, seed 2）
- business / blend60: `title`、category→text（seed 1, seed 2）
- business / blend70: `agebann`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
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
- business2 / blend50: `contravention`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `account name`、account→org（seed 1, seed 2）
- business2 / blend60: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `account name`、account→org（seed 1, seed 2）
- business2 / blend70: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `account name`、account→org（seed 1, seed 2）
- business2 / ft: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total_floor_area_known`、category→quantity（seed 1, seed 2）
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
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `発生県`、id→address（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `goal`、id→quantity（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | australian sourced services | amount | id | 0.5768 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9760 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5438 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5009 | no |
| unknown | business | blend50 | 1 | agebann | category | unknown | 0.4740 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5190 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.2845 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4764 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4677 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4179 | no |
| unknown | business | blend50 | 1 | d2 | category | unknown | 0.4733 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5327 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4178 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9890 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9233 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.5806 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.4082 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3577 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.3830 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4997 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4657 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4997 | no |
| unknown | business | blend50 | 1 | q6 | category | unknown | 0.4899 | no |
| unknown | business | blend50 | 1 | q8 | category | unknown | 0.4730 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9846 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9782 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.3486 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.2692 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.4653 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9792 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9043 | no |
| wrong | business | blend50 | 1 | account_name | account | org | 0.5169 | no |
| wrong | business | blend50 | 1 | d6 | category | quantity | 0.5413 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9827 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.7222 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9873 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.6714 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.7363 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5025 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8339 | no |
| wrong | business | blend50 | 1 | q4b_1 | category | quantity | 0.5014 | no |
| wrong | business | blend50 | 1 | q7 | category | quantity | 0.5024 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.5650 | no |
| other_ng | business | blend50 | 2 | km budgété | other | category | 0.5441 | no |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5014 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5085 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4585 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5192 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4521 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.4738 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4147 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4156 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.3816 | no |
| unknown | business | blend50 | 2 | d6 | category | unknown | 0.4533 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5288 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4161 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9898 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9311 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.5801 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4316 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.4887 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5816 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5946 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4620 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.4798 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.4932 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4542 | no |
| unknown | business | blend50 | 2 | q3_1 | category | unknown | 0.4903 | no |
| unknown | business | blend50 | 2 | q3_2 | category | unknown | 0.4655 | no |
| unknown | business | blend50 | 2 | q6 | category | unknown | 0.4839 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9830 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9797 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3884 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5259 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9727 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8729 | no |
| wrong | business | blend50 | 2 | capital revenue | category | account | 0.6007 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9825 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.6053 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9868 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7391 | no |
| wrong | business | blend50 | 2 | merchant details | text | org | 0.5684 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8637 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5171 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5049 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.7909 | no |
| critical | business | blend60 | 1 | australian sourced services | amount | id | 0.5100 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9722 | yes |
| unknown | business | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5268 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5827 | no |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6122 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.2504 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4192 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4265 | no |
| unknown | business | blend60 | 1 | d1 | category | unknown | 0.3351 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.3978 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9873 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9284 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.3357 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4292 | no |
| unknown | business | blend60 | 1 | overseas sourced services | amount | unknown | 0.3854 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4559 | no |
| unknown | business | blend60 | 1 | q3_1 | category | unknown | 0.4661 | no |
| unknown | business | blend60 | 1 | q3_2 | category | unknown | 0.4149 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9828 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9783 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.3102 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.2799 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9791 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9154 | no |
| wrong | business | blend60 | 1 | account_name | account | org | 0.5869 | no |
| wrong | business | blend60 | 1 | agebann | category | quantity | 0.5518 | no |
| wrong | business | blend60 | 1 | d2 | category | amount | 0.5680 | no |
| wrong | business | blend60 | 1 | d6 | category | quantity | 0.6152 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9819 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.7413 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9864 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.7010 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.7307 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.5871 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8110 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.5315 | no |
| wrong | business | blend60 | 1 | q4b_1 | category | quantity | 0.5379 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.5759 | no |
| wrong | business | blend60 | 1 | q5b | category | quantity | 0.5649 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.5574 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.5862 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.5080 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.5083 | no |
| critical | business | blend60 | 2 | australian sourced goods | amount | quantity | 0.5425 | yes |
| critical | business | blend60 | 2 | overseas sourced goods | amount | quantity | 0.5543 | yes |
| critical | business | blend60 | 2 | overseas sourced services | amount | quantity | 0.5711 | yes |
| other_ng | business | blend60 | 2 | km budgété | other | category | 0.5174 | no |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5957 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6029 | no |
| unknown | business | blend60 | 2 | agebann | category | unknown | 0.4590 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6125 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.5340 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3452 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.3462 | no |
| unknown | business | blend60 | 2 | d1 | category | unknown | 0.4947 | no |
| unknown | business | blend60 | 2 | d2 | category | unknown | 0.4245 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4523 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9883 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9378 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.4083 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.4323 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4047 | no |
| unknown | business | blend60 | 2 | procurementclassification:proclasslabel | account | unknown | 0.4979 | no |
| unknown | business | blend60 | 2 | q5b | category | unknown | 0.4856 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9810 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9801 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4322 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5580 | no |
| unknown | business | blend60 | 2 | tournée | id | unknown | 0.5487 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9713 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8777 | no |
| wrong | business | blend60 | 2 | capital revenue | category | account | 0.6679 | no |
| wrong | business | blend60 | 2 | d6 | category | quantity | 0.5096 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9816 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.6011 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9858 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.7824 | no |
| wrong | business | blend60 | 2 | merchant details | text | org | 0.6361 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5325 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8467 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.5465 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.5658 | no |
| wrong | business | blend60 | 2 | q3_2 | category | quantity | 0.5477 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.5665 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6039 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.5911 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.7794 | no |
| critical | business | blend70 | 1 | overseas sourced goods | amount | quantity | 0.5007 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9683 | yes |
| unknown | business | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6096 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.2921 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.4432 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3620 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4966 | no |
| unknown | business | blend70 | 1 | d1 | category | unknown | 0.3829 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4633 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9857 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9336 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.3882 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.4182 | no |
| unknown | business | blend70 | 1 | q3_2 | category | unknown | 0.4809 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9811 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9784 | no |
| unknown | business | blend70 | 1 | regrp_nom | account | unknown | 0.3421 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.3265 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.4517 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9790 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9266 | no |
| wrong | business | blend70 | 1 | account_name | account | org | 0.6569 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.6296 | no |
| wrong | business | blend70 | 1 | d2 | category | amount | 0.6626 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.6891 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9811 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.7604 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9855 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7307 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.7252 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6744 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7880 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.6158 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.5405 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | quantity | 0.5744 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6700 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6557 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.6444 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.6700 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.5803 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6330 | yes |
| critical | business | blend70 | 2 | australian sourced services | amount | quantity | 0.6229 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6467 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.6624 | yes |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3108 | no |
| unknown | business | blend70 | 2 | commodity-title_fr | product | unknown | 0.3900 | no |
| unknown | business | blend70 | 2 | d1 | category | unknown | 0.4385 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4782 | no |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.4885 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9867 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9445 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.3849 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.4781 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4700 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9789 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9805 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4760 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.4789 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9699 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8826 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.5213 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.7351 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.5659 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9808 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.5968 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9849 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8256 | no |
| wrong | business | blend70 | 2 | merchant details | text | org | 0.7038 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5595 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6107 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8298 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6333 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6569 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6359 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.5632 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6550 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.6906 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.6773 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.7680 | no |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.7152 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9568 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.4171 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.3204 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.3272 | no |
| unknown | business | ft | 1 | d1 | category | unknown | 0.5417 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9806 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9490 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.5460 | no |
| unknown | business | ft | 1 | overseas sourced services | amount | unknown | 0.5167 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9758 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9788 | no |
| unknown | business | ft | 1 | regrp_nom | account | unknown | 0.4885 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.4664 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9787 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9599 | no |
| wrong | business | ft | 1 | account_name | account | org | 0.8670 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.8631 | no |
| wrong | business | ft | 1 | d2 | category | amount | 0.9466 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9109 | no |
| wrong | business | ft | 1 | department | org | account | 0.9788 | no |
| wrong | business | ft | 1 | department | org | account | 0.8177 | no |
| wrong | business | ft | 1 | department | org | account | 0.9829 | no |
| wrong | business | ft | 1 | description | account | text | 0.8196 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.6600 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.7085 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9363 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.7192 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.8687 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.7638 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.6791 | no |
| wrong | business | ft | 1 | q4b_1 | category | quantity | 0.6839 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9522 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9283 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9054 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9214 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.7974 | no |
| wrong | business | ft | 1 | title | category | account | 0.6031 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9042 | yes |
| critical | business | ft | 2 | australian sourced services | amount | quantity | 0.8899 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.9238 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.9363 | yes |
| critical | business | ft | 2 | tournée | id | quantity | 0.5340 | yes |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4010 | no |
| unknown | business | ft | 2 | d1 | category | unknown | 0.4734 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9822 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9645 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.3148 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9727 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9818 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9657 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8971 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.7084 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.9367 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.6391 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.7347 | no |
| wrong | business | ft | 2 | department | org | account | 0.9783 | no |
| wrong | business | ft | 2 | department | org | account | 0.5839 | no |
| wrong | business | ft | 2 | department | org | account | 0.9820 | no |
| wrong | business | ft | 2 | description | account | text | 0.9552 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.5971 | no |
| wrong | business | ft | 2 | merchant details | text | org | 0.9069 | no |
| wrong | business | ft | 2 | mois calendrier | date | category | 0.6647 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7441 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.8453 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7788 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.8937 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9300 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9005 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.5651 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.7961 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9206 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9508 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9358 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.6074 | no |
| wrong | business | ft | 2 | title | category | text | 0.7335 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9759 | yes |
| critical | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6516 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9757 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.6752 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.8154 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5185 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5610 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5053 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4956 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3603 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4980 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.9404 | no |
| unknown | business2 | blend50 | 1 | imd19_income_decile | category | unknown | 0.4294 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.3441 | no |
| unknown | business2 | blend50 | 1 | merchant description | category | unknown | 0.4865 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4963 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9880 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5323 | no |
| unknown | business2 | blend50 | 1 | programme | category | unknown | 0.4879 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5467 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3130 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.4920 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4548 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4274 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4353 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4060 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4553 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4387 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5024 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5189 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9940 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9843 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4166 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9712 | no |
| wrong | business2 | blend50 | 1 | bike_stands | quantity | category | 0.7984 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.8349 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.6352 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5534 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7771 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9532 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5939 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5596 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.6732 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.6243 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.5054 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9385 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9759 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7489 | yes |
| critical | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.6192 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7173 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.8045 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8323 | no |
| other_ng | business2 | blend50 | 2 | b1a floorspace net sqm | other | amount | 0.5016 | no |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5111 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5008 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5084 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3407 | no |
| unknown | business2 | blend50 | 2 | bike_stands | quantity | unknown | 0.4495 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.4819 | no |
| unknown | business2 | blend50 | 2 | contravention | category | unknown | 0.4936 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 0.9936 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4599 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.3181 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9419 | no |
| unknown | business2 | blend50 | 2 | habitatcode | id | unknown | 0.4546 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.4348 | no |
| unknown | business2 | blend50 | 2 | locationname | address | unknown | 0.4960 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4464 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9920 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5810 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5910 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.4774 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4983 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4510 | no |
| unknown | business2 | blend50 | 2 | situtation | address | unknown | 0.3941 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3892 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3875 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3608 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5250 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4991 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5182 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9852 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 2 | want to live in this parish only | quantity | unknown | 0.4448 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4414 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9707 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5058 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.6648 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5344 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.8971 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5569 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.6626 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8415 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.5982 | no |
| wrong | business2 | blend50 | 2 | total_floor_area_known | category | quantity | 0.5264 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9276 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.5485 | no |
| critical | business2 | blend60 | 1 | fine | amount | quantity | 0.5771 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9760 | yes |
| critical | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6805 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9718 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.6471 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.8070 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5046 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5764 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.5837 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.2956 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.9416 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.3851 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5541 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9861 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5235 | no |
| unknown | business2 | blend60 | 1 | programme | category | unknown | 0.4921 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3565 | no |
| unknown | business2 | blend60 | 1 | service_responsable | account | unknown | 0.4692 | no |
| unknown | business2 | blend60 | 1 | situtation | address | unknown | 0.4595 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.4362 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.3579 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4869 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4486 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4918 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4863 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5823 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6099 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9928 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9838 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9879 | no |
| unknown | business2 | blend60 | 1 | warddesc | address | unknown | 0.4015 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9716 | no |
| wrong | business2 | blend60 | 1 | account name | account | org | 0.5690 | no |
| wrong | business2 | blend60 | 1 | bike_stands | quantity | category | 0.8296 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.8393 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6313 | no |
| wrong | business2 | blend60 | 1 | imd19_income_decile | category | amount | 0.5152 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5281 | no |
| wrong | business2 | blend60 | 1 | merchant description | category | org | 0.5288 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.6059 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.7970 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9507 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6719 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6446 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.6182 | no |
| wrong | business2 | blend60 | 1 | scheme_description | category | text | 0.5503 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9477 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9760 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7181 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7593 | yes |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.8024 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8273 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5950 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6027 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4061 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 0.9923 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4328 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.2988 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9434 | no |
| unknown | business2 | blend60 | 2 | habitatcode | id | unknown | 0.4484 | no |
| unknown | business2 | blend60 | 2 | loac_group | category | unknown | 0.4670 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.4774 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9912 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5333 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.3999 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9876 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5677 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4695 | no |
| unknown | business2 | blend60 | 2 | situtation | address | unknown | 0.4141 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4496 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3682 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4329 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5591 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5848 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6091 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9916 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9849 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9710 | no |
| wrong | business2 | blend60 | 2 | account name | account | org | 0.5448 | no |
| wrong | business2 | blend60 | 2 | construction_age_band | category | date | 0.5680 | no |
| wrong | business2 | blend60 | 2 | imd19_income_decile | category | amount | 0.5218 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6623 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.5684 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.8870 | no |
| wrong | business2 | blend60 | 2 | service | account | org | 0.5404 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.6563 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8615 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.5629 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.6069 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9347 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.5405 | no |
| wrong | business2 | blend60 | 2 | want to live in this parish only | quantity | category | 0.5199 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.6562 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9762 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7094 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9679 | yes |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.6191 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.5003 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.7986 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5837 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6719 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.3363 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9428 | no |
| unknown | business2 | blend70 | 1 | habitatdescription | text | unknown | 0.4975 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.4262 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9841 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5969 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4764 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.4157 | no |
| unknown | business2 | blend70 | 1 | situtation | address | unknown | 0.4270 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4883 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.3543 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4419 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.4977 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9917 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9833 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9861 | no |
| unknown | business2 | blend70 | 1 | warddesc | address | unknown | 0.4666 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9719 | no |
| wrong | business2 | blend70 | 1 | account name | account | org | 0.6638 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8609 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.8437 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.6274 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6011 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6161 | no |
| wrong | business2 | blend70 | 1 | merchant description | category | org | 0.5979 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6584 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8169 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9482 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.5740 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7499 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7295 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.5633 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.5678 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9570 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9761 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6872 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8013 | yes |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.8002 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.5321 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8223 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.5685 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4715 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4351 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3312 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9449 | no |
| unknown | business2 | blend70 | 2 | habitatcode | id | unknown | 0.4422 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6175 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4114 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4619 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4654 | no |
| unknown | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5163 | no |
| unknown | business2 | blend70 | 2 | scheme_description | category | unknown | 0.4117 | no |
| unknown | business2 | blend70 | 2 | situtation | address | unknown | 0.4748 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3488 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9846 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9906 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9712 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6355 | no |
| wrong | business2 | blend70 | 2 | construction_age_band | category | date | 0.6542 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6087 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.5448 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.5085 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6597 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6595 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.8768 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6298 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6499 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8814 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.5275 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5050 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.6874 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9418 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.5325 | no |
| wrong | business2 | blend70 | 2 | want to live in this parish only | quantity | category | 0.6037 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.8936 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9765 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7960 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9562 | yes |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.5349 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.6214 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.7734 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9363 | no |
| unknown | business2 | ft | 1 | construction_age_band | category | unknown | 0.4586 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9862 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9463 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.5086 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9888 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms_known | category | unknown | 0.4914 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9783 | no |
| unknown | business2 | ft | 1 | scheme | id | unknown | 0.3983 | no |
| unknown | business2 | ft | 1 | scheme_description | category | unknown | 0.3769 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9871 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9856 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9845 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9883 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9818 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9807 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9729 | no |
| wrong | business2 | ft | 1 | account name | account | org | 0.9479 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9545 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.8568 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.6156 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.8586 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.8800 | no |
| wrong | business2 | ft | 1 | merchant description | category | org | 0.8053 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8159 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.8767 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.9406 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.8198 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9838 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9844 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.5931 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.5853 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.8107 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5011 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.6579 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9848 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9764 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9273 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.6604 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.5244 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.7937 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.6668 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.8072 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.5146 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.7340 | no |
| other_ng | business2 | ft | 2 | total_floor_area | other | quantity | 0.5491 | no |
| unknown | business2 | ft | 2 | basis | category | unknown | 0.4973 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9873 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4293 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9493 | no |
| unknown | business2 | ft | 2 | habitatcode | id | unknown | 0.4444 | no |
| unknown | business2 | ft | 2 | merchant description | category | unknown | 0.4535 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9876 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.8698 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.5859 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9808 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5947 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.3241 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.3258 | no |
| unknown | business2 | ft | 2 | surveyname | text | unknown | 0.4215 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4428 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9872 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9868 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9863 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9862 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9836 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9872 | no |
| unknown | business2 | ft | 2 | want to live in this parish & band d | quantity | unknown | 0.4494 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9719 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9075 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.9126 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.5812 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.8696 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.7783 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.6018 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.6521 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9328 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.8462 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8979 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6309 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.6570 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9414 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.7212 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.9289 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9630 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.5085 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.8550 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8822 | yes |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4988 | no |
| unknown | dev220 | blend50 | 1 | 履行場所 | address | unknown | 0.4954 | no |
| unknown | dev220 | blend50 | 1 | 担当課 | org | unknown | 0.4976 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4977 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9166 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5817 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.9329 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.7392 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.6177 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.4159 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4997 | no |
| unknown | dev220 | blend50 | 2 | 履行場所 | address | unknown | 0.4891 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4991 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.8645 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5797 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.7651 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8990 | yes |
| unknown | dev220 | blend60 | 1 | tax id | id | unknown | 0.4252 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9272 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6589 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.9224 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.7363 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.5766 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5382 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.5816 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.4544 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.8647 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6565 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.7210 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9157 | yes |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.3417 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9378 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7361 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.9118 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.7335 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.6557 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6133 | no |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.4929 | no |
| unknown | dev220 | blend70 | 2 | purchase order by customer | id | unknown | 0.5455 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8648 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7333 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.6770 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9660 | yes |
| unknown | dev220 | ft | 1 | payment terms | category | unknown | 0.4924 | no |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.4856 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9695 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9677 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.8803 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.7249 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8930 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.8387 | no |
| unknown | dev220 | ft | 2 | purchase order by customer | id | unknown | 0.4524 | no |
| unknown | dev220 | ft | 2 | 支払を受ける者の個人番号 | id | unknown | 0.4589 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8653 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9637 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.5448 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.5605 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.8699 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.5422 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.9227 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.6755 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.7512 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7739 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.4281 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.5131 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.4795 | no |
| unknown | general | blend50 | 1 | author | person | unknown | 0.4527 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4932 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4439 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7544 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9121 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.5011 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8130 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.5935 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.3060 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4873 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.4401 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4303 | no |
| unknown | general | blend50 | 1 | 住家一部損壊 | quantity | unknown | 0.4737 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4954 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4172 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4388 | no |
| unknown | general | blend50 | 1 | 日本語教室名 | org | unknown | 0.4643 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9351 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9922 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9488 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.4152 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.7176 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5465 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8775 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.5126 | no |
| wrong | general | blend50 | 1 | standardhours | quantity | category | 0.7181 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.5701 | no |
| wrong | general | blend50 | 1 | 発生県 | id | address | 0.5107 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.7150 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.9365 | no |
| other_ng | general | blend50 | 2 | nodes | other | category | 0.5563 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9472 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7629 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.5716 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.5629 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.5586 | no |
| unknown | general | blend50 | 2 | author | person | unknown | 0.4716 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4820 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.7505 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9119 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.6000 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9701 | no |
| unknown | general | blend50 | 2 | pir_sha | id | unknown | 0.5853 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.3937 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.3683 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4900 | no |
| unknown | general | blend50 | 2 | sens_final | rate | unknown | 0.5592 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.3951 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4176 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.2114 | no |
| unknown | general | blend50 | 2 | 住家一部損壊 | quantity | unknown | 0.4475 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4954 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.4063 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.5372 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4983 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9347 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9935 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8941 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.6429 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5827 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8289 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5514 | no |
| wrong | general | blend50 | 2 | 発生県 | id | address | 0.5025 | no |
| wrong | general | blend50 | 2 | 読み方 | address | org | 0.6524 | no |
| critical | general | blend60 | 1 | goal | id | quantity | 0.5102 | yes |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.8765 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.5963 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.9187 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.6442 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.7023 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.7987 | no |
| unknown | general | blend60 | 1 | age_q1_nd | quantity | unknown | 0.3635 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.4511 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.4037 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4956 | no |
| unknown | general | blend60 | 1 | bib | id | unknown | 0.4890 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.7987 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9276 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.7827 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3549 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4292 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.4932 | no |
| unknown | general | blend60 | 1 | year_step_size | quantity | unknown | 0.4958 | no |
| unknown | general | blend60 | 1 | 住家一部損壊 | quantity | unknown | 0.4850 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.4012 | no |
| unknown | general | blend60 | 1 | 天候 | category | unknown | 0.4931 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9446 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9907 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9540 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.4050 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.6687 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8836 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.5839 | no |
| wrong | general | blend60 | 1 | standardhours | quantity | category | 0.7499 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.6047 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.6905 | no |
| other_ng | general | blend60 | 2 | episode | other | quantity | 0.5033 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.9352 | no |
| other_ng | general | blend60 | 2 | nodes | other | category | 0.6320 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.5365 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9375 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7855 | no |
| unknown | general | blend60 | 2 | age_q1_nd | quantity | unknown | 0.5357 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.5109 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.4986 | no |
| unknown | general | blend60 | 2 | author | person | unknown | 0.4234 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.7940 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9274 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.5408 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9713 | no |
| unknown | general | blend60 | 2 | place | org | unknown | 0.4716 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4305 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.6379 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4645 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4021 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.3893 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.1990 | no |
| unknown | general | blend60 | 2 | year_step_size | quantity | unknown | 0.4733 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4013 | no |
| unknown | general | blend60 | 2 | 天候 | category | unknown | 0.3987 | no |
| unknown | general | blend60 | 2 | 天候 | category | unknown | 0.5775 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9441 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9922 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8884 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.5790 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5112 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.8252 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5949 | no |
| wrong | general | blend60 | 2 | 読み方 | address | org | 0.6897 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.5884 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.8830 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6505 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.5770 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9147 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.5799 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.6129 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.6534 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8235 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.3348 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.3891 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.3521 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8430 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9432 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.7524 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4037 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.4182 | no |
| unknown | general | blend70 | 1 | year_step_size | quantity | unknown | 0.4215 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3070 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9542 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9892 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9591 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3948 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.6198 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8896 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6552 | no |
| wrong | general | blend70 | 1 | standardhours | quantity | category | 0.7818 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.6988 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.5072 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.6660 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.5851 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9340 | no |
| other_ng | general | blend70 | 2 | nodes | other | category | 0.7076 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6235 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9279 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8081 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.4998 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.4588 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.4441 | no |
| unknown | general | blend70 | 2 | author | person | unknown | 0.3751 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8375 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9429 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.4817 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9724 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.4927 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7165 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.5151 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.4091 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.3610 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.1969 | no |
| unknown | general | blend70 | 2 | データセット_キーワード | category | unknown | 0.4946 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3071 | no |
| unknown | general | blend70 | 2 | 天候 | category | unknown | 0.4313 | no |
| unknown | general | blend70 | 2 | 天候 | category | unknown | 0.6178 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9536 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9909 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8826 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5151 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.8216 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6874 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.7269 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.8230 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9026 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.8129 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.8192 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9027 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.8221 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.5068 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8979 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.4370 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.4937 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.5008 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4729 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9759 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9897 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.6616 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3491 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.3854 | no |
| unknown | general | ft | 1 | year_step_size | quantity | unknown | 0.4296 | no |
| unknown | general | ft | 1 | データセット_キーワード | category | unknown | 0.4983 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.3917 | no |
| unknown | general | ft | 1 | 東第5 | quantity | unknown | 0.4393 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9827 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9845 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9747 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.3641 | no |
| wrong | general | ft | 1 | de | text | category | 0.5115 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9078 | no |
| wrong | general | ft | 1 | place | org | address | 0.8689 | no |
| wrong | general | ft | 1 | property | category | text | 0.5502 | no |
| wrong | general | ft | 1 | standardhours | quantity | category | 0.8772 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9810 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.7070 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.5926 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8308 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9303 | no |
| other_ng | general | ft | 2 | nodes | other | category | 0.9345 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.8843 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.8989 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8759 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.4814 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.5347 | no |
| unknown | general | ft | 2 | author | person | unknown | 0.3649 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9680 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9894 | no |
| unknown | general | ft | 2 | doi | id | unknown | 0.5778 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9758 | no |
| unknown | general | ft | 2 | ngram | text | unknown | 0.4814 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.6794 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9524 | no |
| unknown | general | ft | 2 | source | category | unknown | 0.4465 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.7358 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.5034 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4028 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.2317 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.3643 | no |
| unknown | general | ft | 2 | 天候 | category | unknown | 0.7388 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9818 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9871 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.8654 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.5575 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.8106 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.6990 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9647 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.8385 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9847 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9878 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9833 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9869 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9818 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9861 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9774 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9836 | no |

### unknown の判定理由

- date_value_evidence_low: 113件
- numeric_top2_too_close: 57件
- numeric_values_not_parseable: 31件
- other_class: 104件
- probability_below_threshold: 291件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 58件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 228件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 192件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
