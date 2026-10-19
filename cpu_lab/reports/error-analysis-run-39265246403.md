# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-19T14:18:18+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 17 | 1 | 27 | 0 |
| business | blend50 | 2 | 490 | 22 | 2 | 23 | 0 |
| business | blend60 | 1 | 490 | 24 | 2 | 20 | 0 |
| business | blend60 | 2 | 490 | 27 | 5 | 15 | 0 |
| business | blend70 | 1 | 490 | 31 | 3 | 9 | 0 |
| business | blend70 | 2 | 490 | 29 | 6 | 10 | 0 |
| business | ft | 1 | 490 | 32 | 3 | 8 | 0 |
| business | ft | 2 | 490 | 30 | 5 | 9 | 0 |
| business2 | blend50 | 1 | 976 | 17 | 4 | 30 | 3 |
| business2 | blend50 | 2 | 976 | 16 | 4 | 28 | 2 |
| business2 | blend60 | 1 | 976 | 22 | 4 | 23 | 6 |
| business2 | blend60 | 2 | 976 | 18 | 4 | 23 | 5 |
| business2 | blend70 | 1 | 976 | 22 | 4 | 18 | 11 |
| business2 | blend70 | 2 | 976 | 18 | 3 | 18 | 6 |
| business2 | ft | 1 | 976 | 24 | 4 | 16 | 11 |
| business2 | ft | 2 | 976 | 17 | 3 | 19 | 7 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 2 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 1 | 2 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 5 | 1 | 1 | 0 |
| general | blend50 | 1 | 383 | 8 | 1 | 19 | 6 |
| general | blend50 | 2 | 383 | 4 | 0 | 24 | 3 |
| general | blend60 | 1 | 383 | 10 | 1 | 14 | 7 |
| general | blend60 | 2 | 383 | 3 | 0 | 24 | 5 |
| general | blend70 | 1 | 383 | 9 | 1 | 15 | 8 |
| general | blend70 | 2 | 383 | 5 | 1 | 21 | 5 |
| general | ft | 1 | 383 | 9 | 1 | 13 | 8 |
| general | ft | 2 | 383 | 5 | 1 | 17 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 1 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: category→quantity: 17, org→account: 7, category→account: 3, quantity→amount: 2, org→address: 2, text→category: 2, account→text: 2, text→account: 2
- business / blend60: category→quantity: 21, org→account: 6, category→account: 3, amount→quantity: 3, quantity→amount: 2, org→address: 2, text→category: 2, account→text: 2
- business / blend70: category→quantity: 25, org→account: 6, amount→quantity: 5, category→account: 3, quantity→amount: 2, org→address: 2, org→category: 2, text→category: 2
- business / ft: category→quantity: 27, org→account: 6, amount→quantity: 5, category→account: 3, org→address: 2, org→category: 2, text→category: 2, account→text: 2
- business2 / blend50: amount→quantity: 6, id→category: 4, category→id: 4, account→category: 3, category→text: 3, quantity→category: 3, quantity→amount: 2, address→category: 2
- business2 / blend60: amount→quantity: 6, id→category: 4, category→id: 4, quantity→category: 4, account→category: 3, quantity→amount: 2, quantity→address: 2, category→date: 2
- business2 / blend70: amount→quantity: 6, id→category: 4, category→id: 4, quantity→category: 4, account→category: 3, quantity→address: 2, category→date: 2, category→quantity: 2
- business2 / ft: amount→quantity: 6, quantity→category: 5, id→category: 4, category→id: 4, account→category: 3, quantity→address: 2, category→date: 2, category→quantity: 2
- dev220 / blend50: quantity→category: 4, category→tax_class: 2, id→quantity: 2, text→category: 1
- dev220 / blend60: quantity→category: 4, id→quantity: 2, org→account: 1, text→category: 1, rate→tax_class: 1, category→tax_class: 1
- dev220 / blend70: quantity→category: 4, rate→tax_class: 2, id→quantity: 2, org→account: 1, text→category: 1, category→tax_class: 1
- dev220 / ft: quantity→category: 4, rate→tax_class: 2, id→quantity: 2, org→account: 1, text→category: 1, category→tax_class: 1
- general / blend50: category→text: 2, quantity→category: 2, id→address: 2, text→category: 2, org→address: 1, id→quantity: 1, org→text: 1, id→category: 1
- general / blend60: category→text: 2, text→category: 2, quantity→category: 2, id→address: 2, org→address: 1, address→category: 1, id→quantity: 1, org→text: 1
- general / blend70: category→text: 2, quantity→category: 2, id→address: 2, address→category: 2, id→quantity: 2, org→address: 1, text→category: 1, org→text: 1
- general / ft: category→text: 2, quantity→category: 2, id→address: 2, address→category: 2, id→quantity: 2, org→address: 1, text→category: 1, org→text: 1
- japan_procurement / ft: quantity→category: 1

### seedをまたいで再発した誤り

- business / blend50: `agebann`、category→quantity（seed 1, seed 2）
- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `publisher label`、org→address（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `q2a`、category→quantity（seed 1, seed 2）
- business / blend50: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend50: `q6`、category→quantity（seed 1, seed 2）
- business / blend50: `q7`、category→quantity（seed 1, seed 2）
- business / blend50: `q8`、category→quantity（seed 1, seed 2）
- business / blend50: `title`、category→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `agebann`、category→quantity（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
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
- business / blend70: `australian sourced goods`、amount→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→category（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `title`、category→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `australian sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `commodity-title_en`、product→category（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→category（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
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
- business2 / blend50: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `monitor`、id→category（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / blend60: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→category（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `want to live in this parish only`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `税率`、rate→tax_class（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `税率`、rate→tax_class（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `発生県`、id→address（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `goal`、id→quantity（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `読み方`、address→category（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）
- general / ft: `読み方`、address→category（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9973 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5050 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5159 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5261 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3838 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5163 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4463 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4466 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4164 | no |
| unknown | business | blend50 | 1 | d2 | category | unknown | 0.4943 | no |
| unknown | business | blend50 | 1 | d6 | category | unknown | 0.4380 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5430 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4792 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9982 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9482 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.5560 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.3882 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3413 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4624 | no |
| unknown | business | blend50 | 1 | q4a | category | unknown | 0.4992 | no |
| unknown | business | blend50 | 1 | q4b_1 | category | unknown | 0.4977 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4830 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9961 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9884 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4632 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.5026 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9892 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9225 | no |
| wrong | business | blend50 | 1 | agebann | category | quantity | 0.5374 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9925 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.8108 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9953 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.7521 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.8638 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.7637 | no |
| wrong | business | blend50 | 1 | publisher label | org | address | 0.5272 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.7248 | no |
| wrong | business | blend50 | 1 | q2a | category | quantity | 0.5080 | no |
| wrong | business | blend50 | 1 | q3_1 | category | quantity | 0.5082 | no |
| wrong | business | blend50 | 1 | q5a | category | quantity | 0.5030 | no |
| wrong | business | blend50 | 1 | q6 | category | quantity | 0.5167 | no |
| wrong | business | blend50 | 1 | q7 | category | quantity | 0.5406 | no |
| wrong | business | blend50 | 1 | q8 | category | quantity | 0.5333 | no |
| wrong | business | blend50 | 1 | title | category | account | 0.5207 | no |
| critical | business | blend50 | 2 | mois calendrier | date | quantity | 0.6858 | yes |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.7598 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5142 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5179 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5261 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4973 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.4870 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.3894 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.3888 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4504 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5431 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4550 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.5512 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9983 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9482 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.6042 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.3917 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4992 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5095 | no |
| unknown | business | blend50 | 2 | q5a | category | unknown | 0.4993 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9963 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9884 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.2457 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9868 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8687 | no |
| wrong | business | blend50 | 2 | agebann | category | quantity | 0.5390 | no |
| wrong | business | blend50 | 2 | capital revenue | category | account | 0.6307 | no |
| wrong | business | blend50 | 2 | d2 | category | quantity | 0.5125 | no |
| wrong | business | blend50 | 2 | d6 | category | quantity | 0.5806 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9921 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9950 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7596 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.8817 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5319 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5635 | no |
| wrong | business | blend50 | 2 | publisher label | org | address | 0.5297 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9143 | no |
| wrong | business | blend50 | 2 | q2a | category | quantity | 0.5119 | no |
| wrong | business | blend50 | 2 | q3_1 | category | quantity | 0.5070 | no |
| wrong | business | blend50 | 2 | q3_2 | category | quantity | 0.5082 | no |
| wrong | business | blend50 | 2 | q5b | category | quantity | 0.5079 | no |
| wrong | business | blend50 | 2 | q6 | category | quantity | 0.5140 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5400 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5358 | no |
| wrong | business | blend50 | 2 | title | category | account | 0.5211 | no |
| critical | business | blend60 | 1 | respnum$ | id | amount | 0.6008 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9977 | yes |
| unknown | business | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5862 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6118 | no |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6207 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.4605 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.6115 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4670 | no |
| unknown | business | blend60 | 1 | d1 | category | unknown | 0.3730 | no |
| unknown | business | blend60 | 1 | d6 | category | unknown | 0.4913 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9984 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9583 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.3759 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.2738 | no |
| unknown | business | blend60 | 1 | q2b | category | unknown | 0.4961 | no |
| unknown | business | blend60 | 1 | q2c | category | unknown | 0.4575 | no |
| unknown | business | blend60 | 1 | q3_2 | category | unknown | 0.4584 | no |
| unknown | business | blend60 | 1 | q5b | category | unknown | 0.4679 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9967 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9906 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9911 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9373 | no |
| wrong | business | blend60 | 1 | agebann | category | quantity | 0.6279 | no |
| wrong | business | blend60 | 1 | d2 | category | amount | 0.5932 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9937 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8476 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9960 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.7979 | no |
| wrong | business | blend60 | 1 | entitiy | org | category | 0.5281 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.8837 | no |
| wrong | business | blend60 | 1 | portefeuille_nom_et_code | org | account | 0.7218 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.6200 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.6800 | no |
| wrong | business | blend60 | 1 | q1a | category | quantity | 0.5345 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.6045 | no |
| wrong | business | blend60 | 1 | q3_1 | category | quantity | 0.6059 | no |
| wrong | business | blend60 | 1 | q4a | category | quantity | 0.5844 | no |
| wrong | business | blend60 | 1 | q4b_1 | category | id | 0.5930 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.6013 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.6129 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.6321 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.6252 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5219 | no |
| wrong | business | blend60 | 1 | title | category | account | 0.6154 | no |
| critical | business | blend60 | 2 | australian sourced goods | amount | quantity | 0.5968 | yes |
| critical | business | blend60 | 2 | mois calendrier | date | quantity | 0.6689 | yes |
| critical | business | blend60 | 2 | overseas sourced goods | amount | quantity | 0.5990 | yes |
| critical | business | blend60 | 2 | overseas sourced services | amount | quantity | 0.6068 | yes |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.7127 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6110 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6141 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6208 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.5844 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3935 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.4120 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4990 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9985 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9583 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.4627 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9969 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9906 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.2796 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9882 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8727 | no |
| wrong | business | blend60 | 2 | account_name | account | org | 0.5354 | no |
| wrong | business | blend60 | 2 | agebann | category | quantity | 0.6298 | no |
| wrong | business | blend60 | 2 | capital revenue | category | account | 0.7039 | no |
| wrong | business | blend60 | 2 | d1 | category | quantity | 0.5380 | no |
| wrong | business | blend60 | 2 | d2 | category | quantity | 0.5944 | no |
| wrong | business | blend60 | 2 | d6 | category | quantity | 0.6623 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9932 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9956 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.8069 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.9052 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6505 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.6230 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9074 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.6092 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.6045 | no |
| wrong | business | blend60 | 2 | q3_2 | category | quantity | 0.6062 | no |
| wrong | business | blend60 | 2 | q5a | category | quantity | 0.5968 | no |
| wrong | business | blend60 | 2 | q5b | category | quantity | 0.6055 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.6097 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6313 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.6282 | no |
| wrong | business | blend60 | 2 | title | category | account | 0.6158 | no |
| critical | business | blend70 | 1 | australian sourced goods | amount | quantity | 0.5373 | yes |
| critical | business | blend70 | 1 | respnum$ | id | amount | 0.6990 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9981 | yes |
| unknown | business | blend70 | 1 | d1 | category | unknown | 0.4332 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9986 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9684 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.4352 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.2701 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9972 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9928 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9930 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9520 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.7184 | no |
| wrong | business | blend70 | 1 | commodity-title_en | product | category | 0.5106 | no |
| wrong | business | blend70 | 1 | d2 | category | amount | 0.6921 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.5445 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9948 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8844 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9967 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8437 | no |
| wrong | business | blend70 | 1 | entitiy | org | category | 0.5769 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.9037 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | account | 0.6798 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.7129 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.6352 | no |
| wrong | business | blend70 | 1 | q1a | category | quantity | 0.6232 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7009 | no |
| wrong | business | blend70 | 1 | q2b | category | quantity | 0.5754 | no |
| wrong | business | blend70 | 1 | q2c | category | quantity | 0.5325 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.7036 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.5317 | no |
| wrong | business | blend70 | 1 | q4a | category | quantity | 0.6813 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | id | 0.6883 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6996 | no |
| wrong | business | blend70 | 1 | q5b | category | id | 0.5433 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7092 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7235 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7171 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.5806 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.7100 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6962 | yes |
| critical | business | blend70 | 2 | australian sourced services | amount | quantity | 0.6818 | yes |
| critical | business | blend70 | 2 | mois calendrier | date | quantity | 0.6519 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6988 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.7040 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.6656 | yes |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.4249 | no |
| unknown | business | blend70 | 2 | commodity-title_fr | product | unknown | 0.4797 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9684 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.5336 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9974 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9927 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.3261 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9896 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8767 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.6137 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.7206 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.7771 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.6256 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.6764 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7441 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9943 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9963 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8542 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.5429 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9287 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.7375 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7164 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9006 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.7064 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.7020 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.7041 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6944 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.7031 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.7054 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7226 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7205 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.7106 | no |
| critical | business | ft | 1 | australian sourced goods | amount | quantity | 0.7675 | yes |
| critical | business | ft | 1 | respnum$ | id | amount | 0.9935 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9992 | yes |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9987 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.6132 | no |
| unknown | business | ft | 1 | overseas sourced goods | amount | unknown | 0.3858 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9989 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9993 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9987 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9963 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.9899 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.6416 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.6135 | no |
| wrong | business | ft | 1 | d2 | category | amount | 0.9886 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.7042 | no |
| wrong | business | ft | 1 | department | org | account | 0.9984 | no |
| wrong | business | ft | 1 | department | org | account | 0.9948 | no |
| wrong | business | ft | 1 | department | org | account | 0.9989 | no |
| wrong | business | ft | 1 | description | account | text | 0.9811 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.7233 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9636 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | account | 0.5539 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9913 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.5008 | no |
| wrong | business | ft | 1 | q1a | category | quantity | 0.8892 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9903 | no |
| wrong | business | ft | 1 | q2b | category | quantity | 0.8132 | no |
| wrong | business | ft | 1 | q2c | category | quantity | 0.7578 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9968 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.7516 | no |
| wrong | business | ft | 1 | q4a | category | quantity | 0.9718 | no |
| wrong | business | ft | 1 | q4b_1 | category | id | 0.9742 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9945 | no |
| wrong | business | ft | 1 | q5b | category | id | 0.7696 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9980 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9979 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9927 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.7568 | no |
| wrong | business | ft | 1 | title | category | account | 0.9941 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9946 | yes |
| critical | business | ft | 2 | australian sourced services | amount | quantity | 0.9740 | yes |
| critical | business | ft | 2 | mois calendrier | date | quantity | 0.6011 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.9982 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.9958 | yes |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9993 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9987 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.7465 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9992 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9992 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.4659 | no |
| unknown | business | ft | 2 | total invoices paid | quantity | unknown | 0.5243 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9940 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8888 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.8487 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.9930 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.9967 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.5191 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.8885 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.9223 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9894 | no |
| wrong | business | ft | 2 | department | org | account | 0.9976 | no |
| wrong | business | ft | 2 | department | org | account | 0.9983 | no |
| wrong | business | ft | 2 | description | account | text | 0.9961 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.6748 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9993 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.9984 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9963 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8800 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9981 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9944 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9979 | no |
| wrong | business | ft | 2 | q4b_1 | category | quantity | 0.5111 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9870 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9960 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9926 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9965 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9977 | no |
| wrong | business | ft | 2 | title | category | account | 0.9949 | no |
| critical | business2 | blend50 | 1 | fine | amount | quantity | 0.5505 | yes |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9872 | yes |
| critical | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7524 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9972 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.9069 | no |
| other_ng | business2 | blend50 | 1 | a2 floorspace losses sqm | other | quantity | 0.6077 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.8794 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5132 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5162 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.5050 | no |
| unknown | business2 | blend50 | 1 | bike_stands | quantity | unknown | 0.4640 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.5223 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 0.9997 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.9567 | no |
| unknown | business2 | blend50 | 1 | imd19_income_decile | category | unknown | 0.4936 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9979 | no |
| unknown | business2 | blend50 | 1 | number_habitable_rooms_known | category | unknown | 0.4850 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.5002 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9979 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6069 | no |
| unknown | business2 | blend50 | 1 | programme | category | unknown | 0.4967 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5540 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4969 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4320 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4517 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4199 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9975 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9978 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9951 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5016 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5313 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9843 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.5494 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5181 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5751 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.8171 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9690 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.6015 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5670 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.8884 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5802 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8455 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.7748 | no |
| wrong | business2 | blend50 | 1 | total_floor_area_known | category | quantity | 0.5219 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9456 | no |
| critical | business2 | blend50 | 2 | fine | amount | quantity | 0.5484 | yes |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9873 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7531 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.7135 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.8951 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.9256 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5136 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5179 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.5061 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 0.9997 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9547 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.2956 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9979 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.5005 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5307 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5529 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3678 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4812 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.5404 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.6955 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9975 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9978 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9951 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.5024 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5312 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9996 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9924 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9970 | no |
| unknown | business2 | blend50 | 2 | want to live in this parish only | quantity | unknown | 0.4666 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4838 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9844 | no |
| wrong | business2 | blend50 | 2 | bike_stands | quantity | category | 0.6736 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.6432 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.5591 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.9625 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5671 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5531 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.9632 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5023 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.7669 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8698 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.8777 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9457 | no |
| critical | business2 | blend60 | 1 | fine | amount | quantity | 0.6401 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9895 | yes |
| critical | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8014 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9976 | yes |
| other_ng | business2 | blend60 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.6395 | no |
| other_ng | business2 | blend60 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.6483 | no |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.9252 | no |
| other_ng | business2 | blend60 | 1 | a2 floorspace losses sqm | other | quantity | 0.6857 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.8837 | no |
| other_ng | business2 | blend60 | 1 | d2 floorspace gains sqm | other | quantity | 0.6711 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5760 | no |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6121 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.5950 | no |
| unknown | business2 | blend60 | 1 | bike_stands | quantity | unknown | 0.4384 | no |
| unknown | business2 | blend60 | 1 | contravention | category | unknown | 0.4967 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.9611 | no |
| unknown | business2 | blend60 | 1 | health service executive area | address | unknown | 0.4908 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9982 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5995 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9979 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5477 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4974 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9979 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9959 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.6009 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9941 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9873 | no |
| wrong | business2 | blend60 | 1 | construction_age_band | category | date | 0.6166 | no |
| wrong | business2 | blend60 | 1 | imd19_income_decile | category | amount | 0.5924 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5880 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.6319 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.8451 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9697 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.5777 | no |
| wrong | business2 | blend60 | 1 | programme | category | account | 0.5960 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6811 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6534 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.8765 | no |
| wrong | business2 | blend60 | 1 | service | account | address | 0.5960 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8757 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.7989 | no |
| wrong | business2 | blend60 | 1 | terrace | quantity | address | 0.5418 | no |
| wrong | business2 | blend60 | 1 | terrace | quantity | address | 0.5037 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.6015 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9563 | no |
| critical | business2 | blend60 | 2 | fine | amount | quantity | 0.6376 | yes |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9897 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8022 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.6571 | yes |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.9111 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace losses sqm | other | quantity | 0.6111 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.9393 | no |
| other_ng | business2 | blend60 | 2 | avg_tilt | other | rate | 0.5128 | no |
| other_ng | business2 | blend60 | 2 | d2 floorspace gains sqm | other | quantity | 0.6125 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6103 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6141 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9588 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.2965 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9982 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5999 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6202 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4406 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4227 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5989 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.7368 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9979 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9960 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.6018 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9935 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9967 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9873 | no |
| wrong | business2 | blend60 | 2 | account name | account | org | 0.5000 | no |
| wrong | business2 | blend60 | 2 | bike_stands | quantity | category | 0.6798 | no |
| wrong | business2 | blend60 | 2 | construction_age_band | category | date | 0.5971 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.7137 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.5354 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.9618 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.6397 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.6367 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.9663 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.7894 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8954 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.8982 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9565 | no |
| wrong | business2 | blend60 | 2 | want to live in this parish only | quantity | category | 0.5045 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7297 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9919 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8505 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9980 | yes |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.7286 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.7348 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.9435 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.7637 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace net sqm | other | quantity | 0.6305 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.8881 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace gains sqm | other | quantity | 0.6758 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace net sqm | other | quantity | 0.5773 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.7526 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace losses sqm | other | quantity | 0.6341 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace net sqm | other | quantity | 0.6958 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6850 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9655 | no |
| unknown | business2 | blend70 | 1 | health service executive area | address | unknown | 0.4635 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9979 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5041 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4768 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9953 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | want to live in this parish only | quantity | unknown | 0.4656 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9902 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.7108 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6911 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6860 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6887 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8730 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9703 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6703 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6952 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7606 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7399 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.8645 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6950 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.9059 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.8230 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6319 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.5876 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6811 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9670 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.7268 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8514 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.5895 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9270 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.6767 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.9529 | no |
| other_ng | business2 | blend70 | 2 | avg_tilt | other | rate | 0.5981 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.6842 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9628 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.3459 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3641 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6574 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.7782 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.6008 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9946 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9964 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9903 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.5832 | no |
| wrong | business2 | blend70 | 2 | bike_stands | quantity | category | 0.6861 | no |
| wrong | business2 | blend70 | 2 | construction_age_band | category | date | 0.6881 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7842 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.5117 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.9611 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7123 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7204 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9693 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5133 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.8120 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.9210 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.9188 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9672 | no |
| wrong | business2 | blend70 | 2 | want to live in this parish only | quantity | category | 0.5857 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9986 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9990 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9975 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9992 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.9958 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.9942 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9984 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.9977 | no |
| other_ng | business2 | ft | 1 | a2 floorspace net sqm | other | quantity | 0.8731 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9012 | no |
| other_ng | business2 | ft | 1 | b1a floorspace gains sqm | other | quantity | 0.9220 | no |
| other_ng | business2 | ft | 1 | b1a floorspace net sqm | other | quantity | 0.8177 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.9970 | no |
| other_ng | business2 | ft | 1 | d2 floorspace losses sqm | other | quantity | 0.8495 | no |
| other_ng | business2 | ft | 1 | d2 floorspace net sqm | other | quantity | 0.9923 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9551 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9788 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.5136 | no |
| unknown | business2 | ft | 1 | health service executive area | address | unknown | 0.4449 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9989 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9988 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9991 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.9936 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9872 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9800 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8592 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.9568 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.9722 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9482 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9928 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9991 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9992 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.8287 | no |
| wrong | business2 | ft | 1 | scheme_description | category | account | 0.6797 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.9922 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9967 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.8953 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9022 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.8392 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.9199 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9991 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.6577 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.9944 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9992 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9988 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.7971 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9748 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.8734 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9938 | no |
| other_ng | business2 | ft | 2 | avg_tilt | other | rate | 0.8543 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.6907 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.8993 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9995 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9749 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.4940 | no |
| unknown | business2 | ft | 2 | merchant description | category | unknown | 0.4930 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9982 | no |
| unknown | business2 | ft | 2 | terminal | address | unknown | 0.3009 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8328 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.9021 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | total invoices paid | quantity | unknown | 0.5614 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9979 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9955 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9992 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.8328 | no |
| wrong | business2 | ft | 2 | bike_stands | quantity | category | 0.7048 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.9611 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9955 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.9591 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9302 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9714 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9784 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.7315 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.8795 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9979 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9805 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9993 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.8292 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8984 | yes |
| unknown | dev220 | blend50 | 1 | 担当課 | org | unknown | 0.4876 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9304 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5967 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5180 | no |
| wrong | dev220 | blend50 | 1 | 随意契約理由 | text | category | 0.5307 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8973 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.4033 | no |
| unknown | dev220 | blend50 | 2 | 支払を受ける者の個人番号 | id | unknown | 0.4994 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9288 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5962 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.9592 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.9184 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9437 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6769 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.5416 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.6194 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.9171 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.4392 | no |
| unknown | dev220 | blend60 | 2 | 支払を受ける者の個人番号 | id | unknown | 0.5954 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9418 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6763 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.9539 | no |
| wrong | dev220 | blend60 | 2 | 税率 | rate | tax_class | 0.5070 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9384 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9571 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7571 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.6148 | no |
| wrong | dev220 | blend70 | 1 | 税率 | rate | tax_class | 0.5438 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.7080 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9368 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.4752 | no |
| unknown | dev220 | blend70 | 2 | 支払を受ける者の個人番号 | id | unknown | 0.6913 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9548 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7564 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9487 | no |
| wrong | dev220 | blend70 | 2 | 税率 | rate | tax_class | 0.5874 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9984 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9971 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9976 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8346 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.7664 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.9740 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9961 | yes |
| unknown | dev220 | ft | 2 | 支払を受ける者の個人番号 | id | unknown | 0.9792 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9938 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9967 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9329 | no |
| wrong | dev220 | ft | 2 | 税率 | rate | tax_class | 0.8286 | no |
| critical | general | blend50 | 1 | goal | id | quantity | 0.5024 | yes |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.9107 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.6203 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.9608 | no |
| other_ng | general | blend50 | 1 | nodes | other | category | 0.5097 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9018 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9962 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8240 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.4646 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.4781 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.4582 | no |
| unknown | general | blend50 | 1 | author | person | unknown | 0.4248 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7658 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9168 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.9815 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.2796 | no |
| unknown | general | blend50 | 1 | sens_final | rate | unknown | 0.5672 | no |
| unknown | general | blend50 | 1 | source_value | category | unknown | 0.4835 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2129 | no |
| unknown | general | blend50 | 1 | term | text | unknown | 0.4965 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4870 | no |
| unknown | general | blend50 | 1 | 受入年齢 | category | unknown | 0.4937 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9433 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9997 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9605 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.4292 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.6189 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9221 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.5400 | no |
| wrong | general | blend50 | 1 | standardhours | quantity | category | 0.7729 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.8965 | no |
| wrong | general | blend50 | 1 | 日本語教室名 | org | text | 0.7599 | no |
| wrong | general | blend50 | 1 | 発生県 | id | address | 0.5188 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.9163 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.9694 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8296 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8199 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.5948 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.7818 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.6178 | no |
| unknown | general | blend50 | 2 | author | person | unknown | 0.3913 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.7383 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9167 | no |
| unknown | general | blend50 | 2 | doi | id | unknown | 0.5097 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.6643 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9792 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.3354 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.5259 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4873 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4926 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4688 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.2282 | no |
| unknown | general | blend50 | 2 | year_step_size | quantity | unknown | 0.4965 | no |
| unknown | general | blend50 | 2 | 住家一部損壊 | quantity | unknown | 0.4877 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4848 | no |
| unknown | general | blend50 | 2 | 天候 | category | unknown | 0.4506 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9435 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9997 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9384 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4073 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.5457 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5682 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9196 | no |
| wrong | general | blend50 | 2 | 発生県 | id | address | 0.5176 | no |
| critical | general | blend60 | 1 | goal | id | quantity | 0.5947 | yes |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.9254 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.6901 | no |
| other_ng | general | blend60 | 1 | episode | other | quantity | 0.5940 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.9644 | no |
| other_ng | general | blend60 | 1 | nodes | other | category | 0.5760 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9157 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9964 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8588 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4621 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.8124 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9332 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9850 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3241 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.6475 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.5802 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.2365 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3911 | no |
| unknown | general | blend60 | 1 | 受入年齢 | category | unknown | 0.5908 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9544 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9996 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9680 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.5502 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9371 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.6167 | no |
| wrong | general | blend60 | 1 | standardhours | quantity | category | 0.8157 | no |
| wrong | general | blend60 | 1 | term | text | category | 0.5949 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.8874 | no |
| wrong | general | blend60 | 1 | 日本語教室名 | org | text | 0.7469 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.6145 | no |
| wrong | general | blend60 | 1 | 読み方 | address | category | 0.5147 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.9321 | no |
| other_ng | general | blend60 | 2 | episode | other | quantity | 0.5875 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.9747 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.5657 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.7964 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8539 | no |
| unknown | general | blend60 | 2 | age_q1_nd | quantity | unknown | 0.5636 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.7735 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.5696 | no |
| unknown | general | blend60 | 2 | author | person | unknown | 0.4219 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.7794 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9332 | no |
| unknown | general | blend60 | 2 | doi | id | unknown | 0.6074 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.6180 | no |
| unknown | general | blend60 | 2 | goal | id | unknown | 0.4937 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9822 | no |
| unknown | general | blend60 | 2 | place | org | unknown | 0.4016 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.6196 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.5844 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.5911 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4508 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.2477 | no |
| unknown | general | blend60 | 2 | 住家一部損壊 | quantity | unknown | 0.4717 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4436 | no |
| unknown | general | blend60 | 2 | 天候 | category | unknown | 0.4736 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9547 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9996 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9415 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4884 | no |
| wrong | general | blend60 | 2 | cleaned | text | account | 0.5204 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9341 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.6130 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.6870 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.9400 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7599 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.6910 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9680 | no |
| other_ng | general | blend70 | 1 | nodes | other | category | 0.6423 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.5490 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9297 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9966 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8936 | no |
| unknown | general | blend70 | 1 | author | person | unknown | 0.4994 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4815 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8589 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9496 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9884 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.3686 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.7277 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.6769 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.2600 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3356 | no |
| unknown | general | blend70 | 1 | 受入年齢 | category | unknown | 0.6879 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9656 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9995 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9755 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9521 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6934 | no |
| wrong | general | blend70 | 1 | standardhours | quantity | category | 0.8584 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6932 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8784 | no |
| wrong | general | blend70 | 1 | 日本語教室名 | org | text | 0.7339 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7102 | no |
| wrong | general | blend70 | 1 | 読み方 | address | category | 0.6002 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.5690 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9479 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6835 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9801 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6575 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.7632 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8879 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.5324 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.7653 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.5215 | no |
| unknown | general | blend70 | 2 | author | person | unknown | 0.4525 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8205 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9496 | no |
| unknown | general | blend70 | 2 | doi | id | unknown | 0.7051 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.5717 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9851 | no |
| unknown | general | blend70 | 2 | place | org | unknown | 0.4678 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.7134 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.6816 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6896 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.4327 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.2860 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.5138 | no |
| unknown | general | blend70 | 2 | 天候 | category | unknown | 0.4966 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9658 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9996 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9446 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.6048 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9486 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7085 | no |
| wrong | general | blend70 | 2 | 読み方 | address | category | 0.5694 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.9639 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9841 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.9693 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.9820 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9789 | no |
| other_ng | general | ft | 1 | nodes | other | category | 0.8412 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.7780 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9714 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9970 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9980 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9987 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9990 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9986 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.5020 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9684 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.9669 | no |
| unknown | general | ft | 1 | study | text | unknown | 0.3307 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4697 | no |
| unknown | general | ft | 1 | 受入年齢 | category | unknown | 0.9792 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9990 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9981 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9970 | no |
| wrong | general | ft | 1 | place | org | address | 0.9236 | no |
| wrong | general | ft | 1 | standardhours | quantity | category | 0.9867 | no |
| wrong | general | ft | 1 | term | text | category | 0.9882 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8513 | no |
| wrong | general | ft | 1 | 日本語教室名 | org | text | 0.6949 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9973 | no |
| wrong | general | ft | 1 | 読み方 | address | category | 0.8567 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.7954 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9953 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.9712 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9961 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9329 | no |
| other_ng | general | ft | 2 | value | other | amount | 0.5854 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.6637 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9899 | no |
| unknown | general | ft | 2 | age_q3 | quantity | unknown | 0.7404 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9437 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9990 | no |
| unknown | general | ft | 2 | doi | id | unknown | 0.9981 | no |
| unknown | general | ft | 2 | female_frequency | rate | unknown | 0.4966 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9940 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9946 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.9729 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9851 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4241 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.4011 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.7242 | no |
| unknown | general | ft | 2 | 天候 | category | unknown | 0.5657 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9994 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9539 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.8581 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9920 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9948 | no |
| wrong | general | ft | 2 | 読み方 | address | category | 0.8127 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9955 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9955 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9962 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9962 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9969 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9969 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9990 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9990 | no |
| wrong | japan_procurement | ft | 2 | 50,000,000円以上150,000,000円未満件数 | quantity | category | 0.6242 | no |

### unknown の判定理由

- date_value_evidence_low: 113件
- numeric_top2_too_close: 52件
- numeric_values_not_parseable: 31件
- other_class: 132件
- probability_below_threshold: 131件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 71件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 281件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 210件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
