# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-29T10:21:35+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 8 | 1 | 20 | 0 |
| business | blend50 | 2 | 490 | 10 | 0 | 16 | 0 |
| business | blend60 | 1 | 490 | 10 | 1 | 13 | 0 |
| business | blend60 | 2 | 490 | 10 | 0 | 12 | 0 |
| business | blend70 | 1 | 490 | 11 | 1 | 11 | 0 |
| business | blend70 | 2 | 490 | 12 | 0 | 10 | 0 |
| business | ft | 1 | 490 | 12 | 0 | 9 | 0 |
| business | ft | 2 | 490 | 14 | 0 | 6 | 0 |
| business2 | blend50 | 1 | 976 | 17 | 2 | 26 | 1 |
| business2 | blend50 | 2 | 976 | 14 | 1 | 27 | 1 |
| business2 | blend60 | 1 | 976 | 17 | 2 | 21 | 1 |
| business2 | blend60 | 2 | 976 | 15 | 1 | 19 | 1 |
| business2 | blend70 | 1 | 976 | 18 | 3 | 17 | 2 |
| business2 | blend70 | 2 | 976 | 13 | 1 | 17 | 1 |
| business2 | ft | 1 | 976 | 15 | 2 | 17 | 2 |
| business2 | ft | 2 | 976 | 12 | 2 | 13 | 1 |
| dev220 | blend50 | 1 | 220 | 7 | 1 | 8 | 0 |
| dev220 | blend50 | 2 | 220 | 7 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 7 | 2 | 2 | 0 |
| dev220 | ft | 2 | 220 | 4 | 1 | 2 | 0 |
| general | blend50 | 1 | 383 | 8 | 0 | 13 | 7 |
| general | blend50 | 2 | 383 | 8 | 0 | 15 | 5 |
| general | blend60 | 1 | 383 | 7 | 0 | 12 | 6 |
| general | blend60 | 2 | 383 | 7 | 0 | 18 | 5 |
| general | blend70 | 1 | 383 | 6 | 0 | 12 | 6 |
| general | blend70 | 2 | 383 | 8 | 1 | 13 | 5 |
| general | ft | 1 | 383 | 7 | 1 | 11 | 7 |
| general | ft | 2 | 383 | 12 | 3 | 8 | 5 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, account→category: 3, text→category: 2, text→account: 2, quantity→amount: 1, account→text: 1, org→category: 1, category→text: 1
- business / blend60: org→account: 8, account→category: 3, text→category: 2, account→text: 2, text→account: 2, quantity→amount: 1, category→id: 1, category→text: 1
- business / blend70: org→account: 8, account→category: 3, text→category: 2, account→text: 2, text→account: 2, quantity→amount: 1, category→id: 1, category→account: 1
- business / ft: org→account: 9, account→category: 3, category→id: 3, text→category: 2, account→text: 2, text→account: 2, org→address: 1, category→account: 1
- business2 / blend50: account→category: 6, category→id: 4, address→category: 4, category→quantity: 3, id→address: 3, category→org: 2, quantity→category: 2, org→address: 2
- business2 / blend60: account→category: 6, category→id: 4, address→category: 4, category→quantity: 3, id→address: 3, category→org: 2, id→category: 2, quantity→category: 2
- business2 / blend70: account→category: 5, category→id: 4, address→category: 4, category→quantity: 3, id→address: 3, id→category: 2, quantity→amount: 2, quantity→category: 2
- business2 / ft: category→id: 4, account→category: 3, category→quantity: 3, id→category: 2, quantity→category: 2, quantity→amount: 2, id→address: 2, account→org: 2
- dev220 / blend50: quantity→category: 4, text→category: 2, org→account: 2, category→text: 2, category→tax_class: 2, id→quantity: 2
- dev220 / blend60: quantity→category: 4, org→account: 2, category→text: 2, id→quantity: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, category→text: 2, id→quantity: 2
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, text→category: 1, category→text: 1, amount→quantity: 1
- general / blend50: org→address: 4, person→org: 2, category→text: 2, category→quantity: 2, quantity→category: 2, text→category: 2, id→category: 2
- general / blend60: category→text: 4, org→address: 4, quantity→category: 2, text→category: 1, id→category: 1, person→org: 1, category→org: 1
- general / blend70: category→text: 4, org→address: 4, quantity→category: 2, text→category: 1, person→org: 1, quantity→id: 1, category→org: 1
- general / ft: category→text: 6, org→address: 4, quantity→category: 2, id→quantity: 2, person→org: 1, quantity→id: 1, category→org: 1, quantity→rate: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business2 / blend50: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `type of expenditure`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `type of expenditure`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend50: `terms`、category→text（seed 1, seed 2）
- dev220 / blend50: `メッセージ`、text→category（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `terms`、category→text（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend50: `年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者)`、category→quantity（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.7658 | yes |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3453 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5626 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.3358 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4313 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.6043 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5589 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4765 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4782 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6391 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5811 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5775 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4570 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3495 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4941 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9750 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4661 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3326 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4150 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.8861 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.7570 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9680 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.7361 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9866 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.5007 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.5000 | no |
| wrong | business | blend50 | 1 | procurementclassification:proclasslabel | account | category | 0.5968 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9230 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4669 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5213 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4031 | no |
| unknown | business | blend50 | 2 | defence goods value | amount | unknown | 0.6064 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5602 | no |
| unknown | business | blend50 | 2 | description | account | unknown | 0.4904 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4844 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6371 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5747 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5736 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4567 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9712 | no |
| unknown | business | blend50 | 2 | regrp_nom | account | unknown | 0.4247 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5536 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9532 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7904 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9613 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7808 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9782 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.6583 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5274 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5597 | no |
| wrong | business | blend50 | 2 | publisher label | org | category | 0.5089 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8572 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5662 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.7900 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.7196 | yes |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.3706 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.3567 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4837 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7078 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4407 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.3369 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4273 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9774 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4893 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.2733 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4881 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.8728 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.7794 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9637 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.7304 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9862 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.5635 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5562 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5714 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.5291 | no |
| wrong | business | blend60 | 1 | procurementclassification:proclasslabel | account | category | 0.6462 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9243 | no |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.5164 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4446 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4087 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.7053 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5316 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4168 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9729 | no |
| unknown | business | blend60 | 2 | regrp_nom | account | unknown | 0.4396 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5277 | no |
| unknown | business | blend60 | 2 | tournée | id | unknown | 0.4592 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9533 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8195 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9556 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7840 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9762 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.5511 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7190 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.5503 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6017 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8453 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6330 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.8120 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.6734 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.3959 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3777 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7764 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.5089 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3243 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4955 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9798 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.2519 | no |
| unknown | business | blend70 | 1 | type de matériel | category | unknown | 0.4903 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.8596 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8018 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9594 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.7247 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9859 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.6262 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6488 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6646 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.5582 | no |
| wrong | business | blend70 | 1 | procurementclassification:proclasslabel | account | category | 0.6956 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9256 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.5611 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.4860 | no |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.4768 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7736 | no |
| unknown | business | blend70 | 2 | publisher label | org | unknown | 0.4826 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9745 | no |
| unknown | business | blend70 | 2 | regrp_nom | account | unknown | 0.4545 | no |
| unknown | business | blend70 | 2 | respnum$ | id | unknown | 0.5015 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.6151 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9535 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8486 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.5155 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9500 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7873 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9742 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6118 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7797 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.5733 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.6437 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8335 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.6999 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.8340 | no |
| wrong | business | blend70 | 2 | tournée | id | category | 0.5108 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.5034 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4405 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9824 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3304 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9870 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.3598 | no |
| unknown | business | ft | 1 | total invoices paid | quantity | unknown | 0.5349 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.8198 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.8692 | no |
| wrong | business | ft | 1 | department | org | account | 0.9465 | no |
| wrong | business | ft | 1 | department | org | account | 0.7075 | no |
| wrong | business | ft | 1 | department | org | account | 0.9848 | no |
| wrong | business | ft | 1 | description | account | text | 0.8145 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.9269 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9441 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.6455 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.8439 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.6999 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9296 | no |
| wrong | business | ft | 1 | title | category | account | 0.7803 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.6996 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9784 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9795 | no |
| unknown | business | ft | 2 | regrp_nom | account | unknown | 0.4993 | no |
| unknown | business | ft | 2 | respnum$ | id | unknown | 0.4772 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9539 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9360 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.6680 | no |
| wrong | business | ft | 2 | department | org | account | 0.9331 | no |
| wrong | business | ft | 2 | department | org | account | 0.7969 | no |
| wrong | business | ft | 2 | department | org | account | 0.9681 | no |
| wrong | business | ft | 2 | description | account | text | 0.7938 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.6811 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.5973 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9619 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.6423 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7698 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7979 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.9005 | no |
| wrong | business | ft | 2 | title | category | text | 0.9001 | no |
| wrong | business | ft | 2 | tournée | id | category | 0.6802 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9400 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.7631 | yes |
| other_ng | business2 | blend50 | 1 | energy_consumption | other | quantity | 0.7024 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4476 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4303 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3344 | no |
| unknown | business2 | blend50 | 1 | health service executive area | address | unknown | 0.4939 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5825 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5771 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4621 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9874 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5033 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5736 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3580 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4918 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4943 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.3922 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3749 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4234 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.5994 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5105 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4963 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5163 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9921 | no |
| wrong | business2 | blend50 | 1 | merchant description | category | org | 0.5856 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5282 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7694 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9108 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5200 | no |
| wrong | business2 | blend50 | 1 | numéro | id | address | 0.6367 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.6399 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7286 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.6512 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5195 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.6473 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.6524 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.8930 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.5824 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.8266 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9456 | yes |
| other_ng | business2 | blend50 | 2 | energy_consumption | other | quantity | 0.6405 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.2999 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4960 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5760 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5727 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4023 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9839 | no |
| unknown | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5352 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5733 | no |
| unknown | business2 | blend50 | 2 | scheme_description | category | unknown | 0.4857 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3939 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4912 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4967 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4755 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3929 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3352 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4290 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9866 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5492 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.5440 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.6147 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4979 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5184 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9914 | no |
| wrong | business2 | blend50 | 2 | energy_consumption_known | category | quantity | 0.5035 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.8245 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.6836 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5934 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5931 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6193 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.7556 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.6888 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7743 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.7024 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9698 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.5410 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.5584 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9369 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.7164 | yes |
| other_ng | business2 | blend60 | 1 | energy_consumption | other | quantity | 0.7553 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4277 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.3975 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.4925 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5518 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9853 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5880 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4873 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4274 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3800 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4426 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4997 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.6612 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5754 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5938 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6080 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9917 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.5482 | no |
| wrong | business2 | blend60 | 1 | merchant description | category | org | 0.5170 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5959 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.7240 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9068 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.5759 | no |
| wrong | business2 | blend60 | 1 | numéro | id | address | 0.6048 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6679 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.7255 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6598 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.6019 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.5985 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.8742 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.5509 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.8522 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9436 | yes |
| other_ng | business2 | blend60 | 2 | energy_consumption | other | quantity | 0.6809 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3183 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.3941 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9811 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5085 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3874 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3591 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3950 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3958 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9842 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9831 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5332 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.5947 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5435 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5957 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6104 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9909 | no |
| wrong | business2 | blend60 | 2 | energy_consumption_known | category | quantity | 0.5493 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.8037 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5572 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6211 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5260 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6637 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6432 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7579 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7050 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7543 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6585 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9663 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.5012 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.5303 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9338 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.6698 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6665 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | amount | 0.5932 | no |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | quantity | 0.8081 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4250 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4605 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.5715 | no |
| unknown | business2 | blend70 | 1 | merchant description | category | unknown | 0.4484 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9832 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.4968 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4392 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.5103 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.5760 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.7229 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.4942 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9912 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.6024 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6635 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6787 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9029 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6319 | no |
| wrong | business2 | blend70 | 1 | numéro | id | address | 0.5729 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.6959 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7224 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6685 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5566 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.5446 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8554 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.5193 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish only | quantity | category | 0.5287 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.8777 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9416 | yes |
| other_ng | business2 | blend70 | 2 | energy_consumption | other | quantity | 0.7214 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3464 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5249 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4576 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9784 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5800 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4502 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4149 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4548 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4548 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9818 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9805 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.6453 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5166 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9903 | no |
| wrong | business2 | blend70 | 2 | energy_consumption_known | category | quantity | 0.5951 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.7829 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6183 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.5585 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7343 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.6671 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7603 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7212 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.7344 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.6145 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9629 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.5023 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9245 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9397 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.8387 | no |
| other_ng | business2 | ft | 1 | energy_consumption | other | quantity | 0.9666 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.4172 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.6498 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8086 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4418 | no |
| unknown | business2 | ft | 1 | numéro | id | unknown | 0.4991 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9770 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.7135 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.8048 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9871 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9871 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | ft | 1 | total invoices paid | quantity | unknown | 0.5297 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.9082 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.5170 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9899 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.7650 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8664 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.5425 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8911 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.7998 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.7799 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.7132 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.6944 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.7051 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.5845 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.7989 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.7548 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.9544 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9356 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.7256 | yes |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.8427 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4308 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7231 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9700 | no |
| unknown | business2 | ft | 2 | situtation | address | unknown | 0.4833 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6341 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6317 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9854 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9797 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9744 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9727 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9854 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.7973 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9885 | no |
| wrong | business2 | ft | 2 | energy_consumption_known | category | quantity | 0.7326 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.7204 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.8019 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9461 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.7387 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7673 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7697 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.6384 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6745 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9525 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.9044 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.4285 | no |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4921 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4904 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5808 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4892 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4990 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4901 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4994 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9753 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8835 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5086 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.6370 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5030 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7076 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8839 | yes |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4962 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4921 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5806 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4919 | no |
| unknown | dev220 | blend50 | 2 | 商品オプション | text | unknown | 0.4982 | no |
| unknown | dev220 | blend50 | 2 | 商品計 | amount | unknown | 0.5434 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4861 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9762 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8813 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.5447 | no |
| wrong | dev220 | blend50 | 2 | terms | category | text | 0.5301 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5008 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7431 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.9173 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.4592 | no |
| unknown | dev220 | blend60 | 1 | tax id | id | unknown | 0.4920 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9744 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9031 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.6440 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7282 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8926 | yes |
| unknown | dev220 | blend60 | 2 | 商品計 | amount | unknown | 0.5461 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9756 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9004 | no |
| wrong | dev220 | blend60 | 2 | terms | category | text | 0.5157 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7708 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9302 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.4900 | no |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.4074 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9736 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9226 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.6510 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7488 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9014 | yes |
| unknown | dev220 | blend70 | 2 | 商品計 | amount | unknown | 0.5489 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9749 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9195 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.5013 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7985 | no |
| critical | dev220 | ft | 1 | credit limit | amount | quantity | 0.5823 | yes |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9688 | yes |
| unknown | dev220 | ft | 1 | city | address | unknown | 0.4888 | no |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.3106 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9710 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9813 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.6720 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8105 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.5622 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9277 | yes |
| unknown | dev220 | ft | 2 | 商品計 | amount | unknown | 0.5572 | no |
| unknown | dev220 | ft | 2 | 支払を受ける者の個人番号 | id | unknown | 0.4374 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9729 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9769 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8816 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.5604 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.7203 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.6581 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5544 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9418 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9829 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.8354 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4989 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5527 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8966 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4597 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4101 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4849 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4009 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4808 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9830 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3937 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9937 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8647 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3576 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5242 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.7251 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5713 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8639 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8376 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7867 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.9273 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5045 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.5613 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.6278 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.8096 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9670 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9663 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.4173 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4898 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5534 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8893 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4756 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4547 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4260 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4210 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.3882 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4781 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9833 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4006 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9927 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9227 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4320 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.8037 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.5782 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5524 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9151 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.9042 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8063 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8878 | no |
| wrong | general | blend50 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5369 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6352 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.7012 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.6133 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9360 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9796 | no |
| other_ng | general | blend60 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.8132 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.5869 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6393 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9137 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4907 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5076 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.4783 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.4927 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9840 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4722 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9924 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8607 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.3380 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.6732 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5055 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8646 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8132 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.8085 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.9268 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5523 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.6363 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.5903 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.7845 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9662 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9597 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.4606 | no |
| unknown | general | blend60 | 2 | cleaned | text | unknown | 0.4968 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5842 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6401 | no |
| unknown | general | blend60 | 2 | goal | id | unknown | 0.4828 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9049 | no |
| unknown | general | blend60 | 2 | lda | text | unknown | 0.4955 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5097 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4803 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5338 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4147 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.3764 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4985 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9843 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3436 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9912 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9303 | no |
| unknown | general | blend60 | 2 | 駐車場 | category | unknown | 0.4936 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.7684 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9260 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8931 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5353 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.8320 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.8794 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5247 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7100 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6822 | no |
| other_ng | general | blend70 | 1 | episode | other | id | 0.5685 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9301 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9763 | no |
| other_ng | general | blend70 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.7910 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6750 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7259 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4994 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9307 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.5712 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5910 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4897 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4330 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9850 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9912 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8567 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3184 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.6212 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8652 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7888 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8304 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.9262 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6403 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | id | 0.6786 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7112 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.5528 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.7594 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9654 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9531 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.5038 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7268 | no |
| unknown | general | blend70 | 2 | goal | id | unknown | 0.4857 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9205 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5934 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6216 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.3814 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.4369 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9853 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.4005 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9898 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9379 | no |
| unknown | general | blend70 | 2 | 駐車場 | category | unknown | 0.5759 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.7330 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9369 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8820 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6238 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8578 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.8709 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6081 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.6874 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9343 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.6252 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.5198 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.6971 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9125 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9666 | no |
| other_ng | general | ft | 1 | 被害域長さ(100m)最小 | other | quantity | 0.7245 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4654 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9392 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9855 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9819 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8128 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.8414 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3354 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9880 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9874 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.8446 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.2931 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.8673 | no |
| wrong | general | ft | 1 | place | org | address | 0.7155 | no |
| wrong | general | ft | 1 | source | category | text | 0.6595 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8958 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9245 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9044 | no |
| critical | general | ft | 2 | age_q3_nd | quantity | rate | 0.6336 | yes |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.9618 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.6678 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9361 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.6845 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.6842 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9629 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9334 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9869 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9673 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8445 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8851 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9884 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9854 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9607 | no |
| unknown | general | ft | 2 | 駐車場 | category | unknown | 0.8226 | no |
| wrong | general | ft | 2 | author | person | org | 0.6270 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9696 | no |
| wrong | general | ft | 2 | place | org | address | 0.8486 | no |
| wrong | general | ft | 2 | source | category | org | 0.8895 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.5412 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9349 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8455 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8584 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.5714 | no |
| unknown | japan_procurement | blend50 | 1 | 資産名称 | text | unknown | 0.4652 | no |
| unknown | japan_procurement | blend60 | 1 | 資産名称 | text | unknown | 0.4984 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 53件
- numeric_values_not_parseable: 20件
- other_class: 72件
- probability_below_threshold: 166件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 31件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 181件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 101件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
