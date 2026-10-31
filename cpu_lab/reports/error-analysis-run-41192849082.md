# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-31T11:51:57+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 5 | 0 | 13 | 0 |
| business | blend50 | 2 | 490 | 4 | 0 | 20 | 0 |
| business | blend60 | 1 | 490 | 4 | 0 | 12 | 0 |
| business | blend60 | 2 | 490 | 5 | 0 | 12 | 0 |
| business | blend70 | 1 | 490 | 5 | 0 | 8 | 0 |
| business | blend70 | 2 | 490 | 6 | 0 | 8 | 0 |
| business | ft | 1 | 490 | 7 | 0 | 7 | 1 |
| business | ft | 2 | 490 | 10 | 0 | 4 | 1 |
| business2 | blend50 | 1 | 976 | 10 | 1 | 31 | 1 |
| business2 | blend50 | 2 | 976 | 12 | 2 | 28 | 2 |
| business2 | blend60 | 1 | 976 | 11 | 1 | 22 | 1 |
| business2 | blend60 | 2 | 976 | 13 | 2 | 20 | 0 |
| business2 | blend70 | 1 | 976 | 14 | 2 | 17 | 0 |
| business2 | blend70 | 2 | 976 | 14 | 3 | 20 | 0 |
| business2 | ft | 1 | 976 | 16 | 3 | 14 | 1 |
| business2 | ft | 2 | 976 | 15 | 2 | 17 | 0 |
| dev220 | blend50 | 1 | 220 | 7 | 1 | 5 | 0 |
| dev220 | blend50 | 2 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 0 | 0 |
| general | blend50 | 1 | 383 | 8 | 0 | 13 | 6 |
| general | blend50 | 2 | 383 | 7 | 0 | 14 | 5 |
| general | blend60 | 1 | 383 | 5 | 0 | 13 | 5 |
| general | blend60 | 2 | 383 | 5 | 0 | 16 | 6 |
| general | blend70 | 1 | 383 | 6 | 0 | 14 | 6 |
| general | blend70 | 2 | 383 | 8 | 0 | 12 | 7 |
| general | ft | 1 | 383 | 9 | 1 | 11 | 7 |
| general | ft | 2 | 383 | 9 | 0 | 10 | 9 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: text→category: 2, text→account: 2, account→category: 2, category→text: 2, product→text: 1
- business / blend60: text→account: 2, account→category: 2, category→text: 2, org→account: 1, text→category: 1, category→id: 1
- business / blend70: text→account: 2, account→category: 2, category→id: 2, category→text: 2, org→account: 1, text→category: 1, account→text: 1
- business / ft: account→category: 3, org→account: 2, account→text: 2, text→account: 2, category→id: 2, category→text: 2, category→account: 1, text→category: 1
- business2 / blend50: account→category: 6, address→category: 4, amount→quantity: 3, quantity→category: 2, category→quantity: 2, category→text: 2, org→address: 2, id→address: 1
- business2 / blend60: account→category: 6, amount→quantity: 3, id→category: 2, address→category: 2, quantity→category: 2, category→quantity: 2, address→org: 2, org→address: 2
- business2 / blend70: account→category: 5, id→category: 3, category→quantity: 3, amount→quantity: 3, address→category: 2, quantity→category: 2, quantity→amount: 2, address→org: 2
- business2 / ft: account→category: 5, category→quantity: 5, id→category: 3, address→org: 3, address→category: 2, quantity→category: 2, quantity→amount: 2, address→text: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, text→category: 2, category→tax_class: 2, id→quantity: 2, category→text: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2, text→category: 1, category→text: 1, category→tax_class: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, id→quantity: 2, text→category: 1, category→text: 1
- dev220 / ft: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, address→id: 1
- general / blend50: org→address: 4, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1
- general / blend60: org→address: 4, category→text: 2, quantity→category: 2, person→org: 1, id→category: 1
- general / blend70: org→address: 4, category→text: 2, quantity→category: 2, person→org: 1, text→category: 1, id→address: 1, address→org: 1, text→account: 1
- general / ft: category→text: 4, org→address: 4, quantity→category: 2, id→address: 2, person→org: 1, id→quantity: 1, text→category: 1, address→org: 1

### seedをまたいで再発した誤り

- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend60: `title`、category→text（seed 1, seed 2）
- business / blend70: `ligne`、category→id（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `title`、category→text（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `title`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `health service executive area`、address→org（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `health service executive area`、address→org（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `health service executive area`、address→org（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `warddesc`、address→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `随意契約理由`、text→category（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `source`、category→text（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5219 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4715 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.5983 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5448 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5425 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4230 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5465 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3822 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4532 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9850 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5485 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9661 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9119 | no |
| wrong | business | blend50 | 1 | commodity-title_en | product | text | 0.5017 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.5001 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8220 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5679 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.5615 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5025 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4367 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4988 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4602 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.4078 | no |
| unknown | business | blend50 | 2 | d6 | category | unknown | 0.4890 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5608 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4897 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.5989 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5387 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5364 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4903 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5560 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.3210 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4666 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9797 | no |
| unknown | business | blend50 | 2 | regrp_nom | account | unknown | 0.3842 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5250 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9701 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9143 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7164 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9211 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.6382 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.6789 | no |
| unknown | business | blend60 | 1 | abn | id | unknown | 0.6096 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4379 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4600 | no |
| unknown | business | blend60 | 1 | merchant details | text | unknown | 0.4788 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6726 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4436 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.3867 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4425 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9854 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5287 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9670 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9212 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5011 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.7947 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6258 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.5970 | no |
| unknown | business | blend60 | 2 | abn | id | unknown | 0.5884 | no |
| unknown | business | blend60 | 2 | d1 | category | unknown | 0.4491 | no |
| unknown | business | blend60 | 2 | d2 | category | unknown | 0.4305 | no |
| unknown | business | blend60 | 2 | description | account | unknown | 0.4992 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6756 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5837 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.3852 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9807 | no |
| unknown | business | blend60 | 2 | regrp_nom | account | unknown | 0.4318 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5614 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9707 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9264 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5688 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7341 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9155 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6794 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.7218 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3793 | no |
| unknown | business | blend70 | 1 | merchant details | text | unknown | 0.4575 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7470 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3911 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9859 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.6164 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9679 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9305 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5846 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.5494 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7673 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6836 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.6326 | no |
| unknown | business | blend70 | 2 | d1 | category | unknown | 0.4380 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4533 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7523 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4494 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9817 | no |
| unknown | business | blend70 | 2 | regrp_nom | account | unknown | 0.4793 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9714 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9384 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.5115 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6617 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7518 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9099 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.7206 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.7648 | no |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.5663 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.6056 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4807 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9699 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.4044 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9872 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9707 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9584 | no |
| wrong | business | ft | 1 | description | account | text | 0.5068 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.8351 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.7800 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.6854 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.8572 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.5623 | no |
| wrong | business | ft | 1 | title | category | text | 0.7392 | no |
| other_ng | business | ft | 2 | km budgété | other | quantity | 0.6094 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9823 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9846 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9733 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9746 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.5458 | no |
| wrong | business | ft | 2 | description | account | text | 0.6469 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.5372 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.9405 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.8048 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | id | 0.6420 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8932 | no |
| wrong | business | ft | 2 | regrp_nom | account | category | 0.6221 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.8442 | no |
| wrong | business | ft | 2 | title | category | text | 0.8937 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9595 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5979 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4945 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3483 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4028 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3580 | no |
| unknown | business2 | blend50 | 1 | health service executive area | address | unknown | 0.4869 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4983 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5461 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5424 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4521 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9894 | no |
| unknown | business2 | blend50 | 1 | potential_epc_rating_known | category | unknown | 0.4777 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5261 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5957 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4681 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4915 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4897 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4631 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4876 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4836 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4993 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5413 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4515 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5455 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4991 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5315 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9920 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7206 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.7527 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5456 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5113 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.9176 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5106 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9815 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.6631 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7842 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9566 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7674 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.5101 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.5297 | no |
| unknown | business2 | blend50 | 2 | cost centre description | account | unknown | 0.4948 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.3329 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.2587 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4895 | no |
| unknown | business2 | blend50 | 2 | imd19_national_decile | category | unknown | 0.4138 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4626 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5397 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5353 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4823 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9836 | no |
| unknown | business2 | blend50 | 2 | potential_epc_score_known | category | unknown | 0.4782 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5645 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4862 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4861 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4499 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4736 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5233 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.7743 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5148 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4261 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4944 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5399 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9917 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.6517 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.8657 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5721 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6273 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5031 | no |
| wrong | business2 | blend50 | 2 | service | account | category | 0.5931 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.8696 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.5310 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.8872 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.7525 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9584 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.5278 | no |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4624 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.3825 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4315 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4277 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5354 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9876 | no |
| unknown | business2 | blend60 | 1 | potential_epc_rating_known | category | unknown | 0.4617 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5231 | no |
| unknown | business2 | blend60 | 1 | situtation | address | unknown | 0.4292 | no |
| unknown | business2 | blend60 | 1 | surveyname | text | unknown | 0.4680 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5698 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5341 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5371 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4985 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5363 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5969 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9916 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.5213 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5646 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6715 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7135 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6107 | no |
| wrong | business2 | blend60 | 1 | service | account | org | 0.5613 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.9138 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9793 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.6626 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.8178 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9542 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7350 | yes |
| unknown | business2 | blend60 | 2 | cost centre description | account | unknown | 0.4914 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.3684 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.2221 | no |
| unknown | business2 | blend60 | 2 | imd19_national_decile | category | unknown | 0.4108 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9808 | no |
| unknown | business2 | blend60 | 2 | potential_epc_score_known | category | unknown | 0.4154 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3897 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5302 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4986 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9853 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9834 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5635 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.7969 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5752 | no |
| unknown | business2 | blend60 | 2 | tree type | category | unknown | 0.5079 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5914 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9911 | no |
| wrong | business2 | blend60 | 2 | health service executive area | address | org | 0.5232 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5289 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.5897 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.8441 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6463 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6821 | no |
| wrong | business2 | blend60 | 2 | service | account | category | 0.5390 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.8576 | no |
| wrong | business2 | blend60 | 2 | situtation | address | text | 0.5007 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.8662 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.7686 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9573 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6244 | yes |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.4167 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4603 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4974 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend70 | 1 | potential_epc_rating_known | category | unknown | 0.4456 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.4834 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6034 | no |
| unknown | business2 | blend70 | 1 | situtation | address | unknown | 0.4747 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4728 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6560 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6190 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9874 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9912 | no |
| wrong | business2 | blend70 | 1 | conservation_area_site_id | category | id | 0.5237 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.5557 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6308 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6223 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.6743 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6758 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.6545 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.9099 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.5454 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9770 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.6620 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.8513 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9519 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7027 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6700 | yes |
| unknown | business2 | blend70 | 2 | cost centre description | account | unknown | 0.4880 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4039 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.2539 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.5189 | no |
| unknown | business2 | blend70 | 2 | habitatdescription | text | unknown | 0.4670 | no |
| unknown | business2 | blend70 | 2 | imd19_national_decile | category | unknown | 0.4550 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9780 | no |
| unknown | business2 | blend70 | 2 | potential_epc_score_known | category | unknown | 0.4747 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4849 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4260 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6105 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.5768 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9849 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9832 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9808 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.8194 | no |
| unknown | business2 | blend70 | 2 | tree type | category | unknown | 0.5897 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9906 | no |
| wrong | business2 | blend70 | 2 | health service executive area | address | org | 0.5570 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.5953 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.5277 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.8224 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7205 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7369 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.5167 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.8456 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.5812 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.8452 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.7848 | no |
| critical | business2 | ft | 1 | fine | amount | rate | 0.7065 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9539 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.8887 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.6097 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.5464 | no |
| unknown | business2 | ft | 1 | numéro_uev | id | unknown | 0.4008 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9808 | no |
| unknown | business2 | ft | 1 | potential_epc_rating_known | category | unknown | 0.4998 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.4711 | no |
| unknown | business2 | ft | 1 | surveyname | text | unknown | 0.4874 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.9146 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.8736 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9863 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9842 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9824 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9901 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.7336 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.5193 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.6589 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8296 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.5566 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8710 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.9342 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8984 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.6725 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.6863 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9703 | no |
| wrong | business2 | ft | 1 | type of expenditure | account | category | 0.6603 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.9518 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9448 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9544 | yes |
| unknown | business2 | ft | 2 | cost centre description | account | unknown | 0.4971 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.3496 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.7059 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.6671 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9696 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6056 | no |
| unknown | business2 | ft | 2 | service | account | unknown | 0.3227 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8514 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8116 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9803 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9800 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9767 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9733 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.8870 | no |
| unknown | business2 | ft | 2 | tree type | category | unknown | 0.8350 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9890 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.5105 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.6581 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.7944 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.7575 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9432 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.9013 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.6526 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.7157 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.8095 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.8229 | no |
| wrong | business2 | ft | 2 | terminal | address | org | 0.6067 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.7823 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.8333 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8022 | yes |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.5000 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4880 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4995 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4750 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4992 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9725 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.9010 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5070 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.5600 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7377 | no |
| wrong | dev220 | blend50 | 1 | 随意契約理由 | text | category | 0.5014 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8451 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.5497 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4994 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4881 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4992 | no |
| unknown | dev220 | blend50 | 2 | 商品オプション | text | unknown | 0.4952 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4780 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4901 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.8929 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9421 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.5753 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5019 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.8131 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8104 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9729 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9167 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.5378 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7413 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5931 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8735 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.5702 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.8744 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9482 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.5021 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.8266 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8185 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9732 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9324 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.5156 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7450 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6848 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9019 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.5907 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8559 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9543 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8400 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.8429 | yes |
| unknown | dev220 | ft | 1 | city | address | unknown | 0.4892 | no |
| unknown | dev220 | ft | 1 | description | text | unknown | 0.4955 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9743 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9796 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7560 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.9599 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9871 | yes |
| wrong | dev220 | ft | 2 | city | address | id | 0.6658 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8005 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9725 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8802 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.5988 | no |
| other_ng | general | blend50 | 1 | abstract rank | other | category | 0.5229 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.5462 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.7605 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5153 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.8171 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9816 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.5191 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5998 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8424 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4819 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4297 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4375 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4282 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.5452 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9852 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4029 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9943 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9451 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3464 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.7800 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5260 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5559 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9360 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9334 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7377 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.8521 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5064 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.6022 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.5520 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5228 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9199 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8630 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4644 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.5016 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.6174 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.7572 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4756 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.3721 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4100 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4483 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4130 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9742 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3814 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9940 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9493 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4273 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.5433 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.5263 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.7530 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9337 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.9576 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.7259 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8093 | no |
| other_ng | general | blend60 | 1 | abstract rank | other | category | 0.6054 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.5850 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.7398 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.7964 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9781 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4406 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.6055 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6773 | no |
| unknown | general | blend60 | 1 | goal | id | unknown | 0.4831 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.8680 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.5153 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5500 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.4489 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9861 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3803 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9931 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9458 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.3347 | no |
| wrong | general | blend60 | 1 | author | person | org | 0.7429 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9373 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9274 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7676 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.8314 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.5041 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.6702 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.5569 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5012 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9230 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.8358 | no |
| unknown | general | blend60 | 2 | author | person | unknown | 0.4726 | no |
| unknown | general | blend60 | 2 | cleaned | text | unknown | 0.4976 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5817 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6922 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.7966 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4462 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4792 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5269 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4641 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.3592 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3704 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9771 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.4572 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9928 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9539 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4744 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7202 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9345 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.9545 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.7643 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7807 | no |
| other_ng | general | blend70 | 1 | abstract rank | other | category | 0.6879 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6239 | no |
| other_ng | general | blend70 | 1 | episode | other | id | 0.7190 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.5533 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.7757 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9745 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.3551 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6919 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7548 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4805 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.8937 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.6009 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6410 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4795 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4449 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9871 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.4433 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9920 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9466 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3898 | no |
| wrong | general | blend70 | 1 | author | person | org | 0.7058 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.5135 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9386 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.9215 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.7976 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.8106 | no |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.5554 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7382 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.5618 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.5818 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.5331 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9260 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.8085 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.6619 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7671 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8360 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5202 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6144 | no |
| unknown | general | blend70 | 2 | source | category | unknown | 0.4989 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.3889 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.3823 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4026 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9800 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9916 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9585 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.5802 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.6875 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9353 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.9514 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8027 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7520 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.5330 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.5215 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.6716 | yes |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.9354 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.7406 | no |
| other_ng | general | ft | 1 | episode | other | id | 0.6568 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.6338 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.7880 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.7137 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9638 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.5221 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4390 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9512 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9873 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9705 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8577 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9142 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3820 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9898 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9886 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9488 | no |
| wrong | general | ft | 1 | author | person | org | 0.5945 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.6809 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9424 | no |
| wrong | general | ft | 1 | place | org | address | 0.9036 | no |
| wrong | general | ft | 1 | source | category | text | 0.6241 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8874 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.7483 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.6324 | no |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.7092 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9422 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.5764 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.7253 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.8236 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.5813 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.6534 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9352 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.7267 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9025 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9917 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9541 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.7423 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8768 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.4363 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.4993 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9886 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9880 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9722 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.8279 | no |
| wrong | general | ft | 2 | goal | id | category | 0.5892 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9376 | no |
| wrong | general | ft | 2 | place | org | address | 0.9422 | no |
| wrong | general | ft | 2 | source | category | text | 0.5602 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9179 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6661 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.7606 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.6627 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 45件
- numeric_values_not_parseable: 16件
- other_class: 82件
- probability_below_threshold: 157件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 25件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 150件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 114件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
