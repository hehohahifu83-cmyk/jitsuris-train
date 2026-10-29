# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-29T11:49:06+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 6 | 0 | 18 | 0 |
| business | blend50 | 2 | 490 | 10 | 1 | 16 | 0 |
| business | blend60 | 1 | 490 | 8 | 0 | 11 | 0 |
| business | blend60 | 2 | 490 | 10 | 0 | 10 | 0 |
| business | blend70 | 1 | 490 | 9 | 0 | 9 | 0 |
| business | blend70 | 2 | 490 | 11 | 0 | 9 | 0 |
| business | ft | 1 | 490 | 11 | 0 | 7 | 1 |
| business | ft | 2 | 490 | 12 | 0 | 7 | 0 |
| business2 | blend50 | 1 | 976 | 18 | 3 | 30 | 2 |
| business2 | blend50 | 2 | 976 | 12 | 2 | 33 | 3 |
| business2 | blend60 | 1 | 976 | 20 | 2 | 22 | 2 |
| business2 | blend60 | 2 | 976 | 15 | 3 | 25 | 3 |
| business2 | blend70 | 1 | 976 | 21 | 2 | 19 | 2 |
| business2 | blend70 | 2 | 976 | 16 | 4 | 21 | 3 |
| business2 | ft | 1 | 976 | 24 | 2 | 19 | 1 |
| business2 | ft | 2 | 976 | 21 | 5 | 19 | 2 |
| dev220 | blend50 | 1 | 220 | 7 | 1 | 6 | 0 |
| dev220 | blend50 | 2 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 7 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 7 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 8 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 10 | 2 | 0 | 0 |
| general | blend50 | 1 | 383 | 6 | 0 | 17 | 5 |
| general | blend50 | 2 | 383 | 9 | 0 | 15 | 6 |
| general | blend60 | 1 | 383 | 6 | 0 | 16 | 6 |
| general | blend60 | 2 | 383 | 10 | 0 | 13 | 5 |
| general | blend70 | 1 | 383 | 10 | 1 | 10 | 6 |
| general | blend70 | 2 | 383 | 10 | 0 | 13 | 6 |
| general | ft | 1 | 383 | 10 | 1 | 16 | 5 |
| general | ft | 2 | 383 | 11 | 2 | 14 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 6, account→text: 2, text→account: 2, account→category: 2, text→org: 1, quantity→amount: 1, text→category: 1, category→text: 1
- business / blend60: org→account: 7, account→text: 2, text→account: 2, account→category: 2, org→address: 1, text→org: 1, category→id: 1, text→category: 1
- business / blend70: org→account: 8, account→text: 2, text→account: 2, account→category: 2, category→text: 2, org→address: 1, text→org: 1, category→id: 1
- business / ft: org→account: 8, category→account: 2, account→text: 2, text→account: 2, account→category: 2, category→text: 2, org→address: 1, text→org: 1
- business2 / blend50: amount→quantity: 5, account→category: 4, category→quantity: 4, id→address: 3, category→org: 2, id→category: 2, category→id: 2, address→category: 2
- business2 / blend60: amount→quantity: 5, account→category: 4, category→id: 4, category→quantity: 4, category→org: 2, id→category: 2, quantity→category: 2, category→address: 2
- business2 / blend70: amount→quantity: 5, account→category: 4, category→id: 4, category→quantity: 4, category→org: 2, id→category: 2, category→address: 2, address→text: 2
- business2 / ft: category→quantity: 6, account→category: 4, category→id: 4, amount→quantity: 4, quantity→category: 3, id→category: 2, quantity→address: 2, category→address: 2
- dev220 / blend50: quantity→category: 4, text→category: 3, org→account: 2, category→tax_class: 2, id→quantity: 2
- dev220 / blend60: quantity→category: 4, address→id: 3, org→account: 2, category→tax_class: 2, id→quantity: 2, text→category: 1
- dev220 / blend70: quantity→category: 4, address→id: 3, org→account: 2, text→category: 2, id→quantity: 2, category→tax_class: 1
- dev220 / ft: quantity→category: 4, text→category: 3, address→id: 3, org→account: 2, id→quantity: 2, category→tax_class: 1, amount→quantity: 1
- general / blend50: org→address: 4, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, category→quantity: 2, id→category: 1
- general / blend60: category→text: 4, org→address: 4, text→category: 3, quantity→category: 2, person→org: 1, category→quantity: 1, id→category: 1
- general / blend70: category→text: 6, org→address: 4, text→category: 3, quantity→category: 2, id→address: 1, id→quantity: 1, person→org: 1, category→quantity: 1
- general / ft: category→text: 6, org→address: 4, text→category: 4, quantity→category: 2, id→quantity: 2, id→address: 1, quantity→rate: 1, category→quantity: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business2 / blend50: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `monitor`、id→category（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / blend60: `health service executive area`、address→org（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→text（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / blend70: `health service executive area`、address→org（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→text（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / ft: `health service executive area`、address→org（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service`、account→address（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend50: `メッセージ`、text→category（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `city`、address→id（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `city`、address→id（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `随意契約理由`、text→category（seed 1, seed 2）
- dev220 / ft: `city`、address→id（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `随意契約理由`、text→category（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.5226 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5000 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4055 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.6058 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5593 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4608 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6084 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5807 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5762 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4743 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4406 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4904 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9765 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3268 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4908 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5949 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9185 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.7850 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9362 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.6554 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9699 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.5613 | no |
| wrong | business | blend50 | 1 | merchant details | text | org | 0.7048 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.7367 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.6483 | yes |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.5471 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5847 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.3547 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4422 | no |
| unknown | business | blend50 | 2 | defence goods value | amount | unknown | 0.6067 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5601 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4982 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6289 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5806 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5762 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4660 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.3415 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4861 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9736 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9509 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7841 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9582 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7206 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9806 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.5213 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.5374 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5100 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8774 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5298 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.6355 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4474 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.4963 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6709 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5628 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4198 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9792 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.2663 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4530 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5146 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9118 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8131 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9255 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.6336 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9663 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6362 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5505 | no |
| wrong | business | blend60 | 1 | merchant details | text | org | 0.7337 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.5294 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.7008 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3794 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.4968 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6956 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5530 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4046 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.3894 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9757 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5786 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9506 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8120 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9520 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7117 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9790 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.5882 | no |
| wrong | business | blend60 | 2 | entitiy | org | account | 0.5514 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.5740 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.5421 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8696 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.5894 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.6267 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4893 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7334 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3990 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9819 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.2706 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.4152 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.5540 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9050 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8411 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9149 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.6117 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9626 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7111 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5266 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6402 | no |
| wrong | business | blend70 | 1 | merchant details | text | org | 0.7626 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6146 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.6648 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.4042 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4695 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7622 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4677 | no |
| unknown | business | blend70 | 2 | publisher label | org | unknown | 0.4337 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9778 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.5089 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9503 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8399 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9458 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7029 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9774 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6550 | no |
| wrong | business | blend70 | 2 | dispute-status_statut-de-différend-fra | category | text | 0.5190 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.6433 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.6105 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5742 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8618 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.6490 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.6178 | no |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.6140 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9209 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3366 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9900 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.3294 | no |
| unknown | business | ft | 1 | title | category | unknown | 0.3894 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.8847 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9253 | no |
| wrong | business | ft | 1 | capital revenue | category | account | 0.5134 | no |
| wrong | business | ft | 1 | department | org | account | 0.8829 | no |
| wrong | business | ft | 1 | department | org | account | 0.5461 | no |
| wrong | business | ft | 1 | department | org | account | 0.9515 | no |
| wrong | business | ft | 1 | description | account | text | 0.9357 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.7522 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9093 | no |
| wrong | business | ft | 1 | merchant details | text | org | 0.8494 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.8701 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.5570 | no |
| wrong | business | ft | 1 | segment-title_fr | category | account | 0.5157 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4784 | no |
| unknown | business | ft | 2 | d2 | category | unknown | 0.4909 | no |
| unknown | business | ft | 2 | d6 | category | unknown | 0.4691 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9621 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9842 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9494 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9236 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.5194 | no |
| wrong | business | ft | 2 | department | org | account | 0.9270 | no |
| wrong | business | ft | 2 | department | org | account | 0.6763 | no |
| wrong | business | ft | 2 | department | org | account | 0.9728 | no |
| wrong | business | ft | 2 | description | account | text | 0.8556 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.7414 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.9190 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.7202 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.6704 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8385 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.8278 | no |
| wrong | business | ft | 2 | title | category | text | 0.5912 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9642 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7024 | yes |
| critical | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | quantity | 0.6437 | yes |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.5760 | no |
| other_ng | business2 | blend50 | 1 | energy_consumption | other | quantity | 0.6689 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4672 | no |
| unknown | business2 | blend50 | 1 | conservation_area_site_id | category | unknown | 0.4602 | no |
| unknown | business2 | blend50 | 1 | contravention | category | unknown | 0.4989 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3687 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3762 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5824 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5759 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4019 | no |
| unknown | business2 | blend50 | 1 | numéro entente-cadre | id | unknown | 0.4901 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9857 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4055 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.4930 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4908 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4958 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4856 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4310 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3175 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4292 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9937 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5922 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5602 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4452 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4973 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5242 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.5261 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5724 | no |
| wrong | business2 | blend50 | 1 | merchant description | category | org | 0.6815 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5023 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7484 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.5807 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.6091 | no |
| wrong | business2 | blend50 | 1 | numéro | id | address | 0.5306 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.6240 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.8574 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7885 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5209 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8407 | no |
| wrong | business2 | blend50 | 1 | total_floor_area_known | category | quantity | 0.6173 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9361 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.6617 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9737 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8190 | yes |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.5849 | no |
| other_ng | business2 | blend50 | 2 | energy_consumption | other | quantity | 0.6687 | no |
| other_ng | business2 | blend50 | 2 | epc_score | other | rate | 0.5005 | no |
| unknown | business2 | blend50 | 2 | conservation_area_site_id | category | unknown | 0.4806 | no |
| unknown | business2 | blend50 | 2 | contravention | category | unknown | 0.4688 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.3268 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.2994 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4883 | no |
| unknown | business2 | blend50 | 2 | imd19_national_decile | category | unknown | 0.3416 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5819 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5754 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4753 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9868 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4570 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.3972 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5132 | no |
| unknown | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5882 | no |
| unknown | business2 | blend50 | 2 | scheme_description | category | unknown | 0.4849 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3523 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4928 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4930 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4329 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4102 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4541 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.6212 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.4643 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5098 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4986 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5229 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9925 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4652 | no |
| wrong | business2 | blend50 | 2 | imd19_income_decile | category | quantity | 0.5591 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.8993 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5235 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7609 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5198 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.6004 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.7153 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7630 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.5347 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9420 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9659 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6665 | yes |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.5566 | no |
| other_ng | business2 | blend60 | 1 | energy_consumption | other | quantity | 0.7150 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.3538 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4477 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.4719 | no |
| unknown | business2 | blend60 | 1 | numéro entente-cadre | id | unknown | 0.4731 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9832 | no |
| unknown | business2 | blend60 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6063 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4770 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4864 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3130 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3483 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5113 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5140 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4164 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5950 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6174 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9919 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.5411 | no |
| wrong | business2 | blend60 | 1 | conservation_area_site_id | category | id | 0.5501 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.5361 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6423 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5868 | no |
| wrong | business2 | blend60 | 1 | merchant description | category | org | 0.6321 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5648 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6988 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.5107 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6829 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6488 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8801 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8246 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8340 | no |
| wrong | business2 | blend60 | 1 | situtation | address | text | 0.5247 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.6372 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9259 | no |
| wrong | business2 | blend60 | 1 | want to live in this parish & band a | quantity | category | 0.5620 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.6543 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9773 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8063 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6424 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.5673 | no |
| other_ng | business2 | blend60 | 2 | energy_consumption | other | quantity | 0.7147 | no |
| other_ng | business2 | blend60 | 2 | epc_score | other | rate | 0.5176 | no |
| unknown | business2 | blend60 | 2 | contravention | category | unknown | 0.4346 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.3459 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3404 | no |
| unknown | business2 | blend60 | 2 | imd19_national_decile | category | unknown | 0.3725 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5521 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5677 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9845 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4711 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4766 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5407 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4226 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4850 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5365 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9865 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5461 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.4990 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5767 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5965 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6159 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4376 | no |
| wrong | business2 | blend60 | 2 | conservation_area_site_id | category | id | 0.5746 | no |
| wrong | business2 | blend60 | 2 | health service executive area | address | org | 0.5413 | no |
| wrong | business2 | blend60 | 2 | imd19_income_decile | category | quantity | 0.6300 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5672 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.8934 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5902 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7139 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6724 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7584 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7408 | no |
| wrong | business2 | blend60 | 2 | situtation | address | text | 0.5098 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9330 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9676 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6305 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.5372 | no |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | quantity | 0.7611 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.3701 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.5191 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.5472 | no |
| unknown | business2 | blend70 | 1 | numéro entente-cadre | id | unknown | 0.5200 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9808 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.4585 | no |
| unknown | business2 | blend70 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5688 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3646 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3957 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5574 | no |
| unknown | business2 | blend70 | 1 | total_verified_sales | quantity | unknown | 0.5948 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.4845 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9915 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.5561 | no |
| wrong | business2 | blend70 | 1 | account name | account | org | 0.5214 | no |
| wrong | business2 | blend70 | 1 | conservation_area_site_id | category | id | 0.6399 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.5732 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.7122 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6846 | no |
| wrong | business2 | blend70 | 1 | merchant description | category | org | 0.5827 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6272 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6492 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7567 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.6736 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.9028 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8607 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.5673 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8274 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6089 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6571 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9157 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish & band a | quantity | category | 0.6556 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.6468 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9810 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7937 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6966 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6680 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.5497 | no |
| other_ng | business2 | blend70 | 2 | energy_consumption | other | quantity | 0.7608 | no |
| other_ng | business2 | blend70 | 2 | epc_score | other | rate | 0.5346 | no |
| unknown | business2 | blend70 | 2 | contravention | category | unknown | 0.4004 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.3650 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3953 | no |
| unknown | business2 | blend70 | 2 | imd19_national_decile | category | unknown | 0.4101 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6337 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9823 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5496 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5561 | no |
| unknown | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6036 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4929 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.5598 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6189 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9855 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.5197 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.5337 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9918 | no |
| unknown | business2 | blend70 | 2 | warddesc | address | unknown | 0.4944 | no |
| wrong | business2 | blend70 | 2 | conservation_area_site_id | category | id | 0.6685 | no |
| wrong | business2 | blend70 | 2 | health service executive area | address | org | 0.5944 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | quantity | 0.7008 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6616 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.8876 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6569 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6668 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7445 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.8015 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.7186 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.5915 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9240 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9728 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.8373 | yes |
| other_ng | business2 | ft | 1 | energy_consumption | other | quantity | 0.8994 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.4295 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.7334 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.5997 | no |
| unknown | business2 | ft | 1 | merchant description | category | unknown | 0.4345 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.7549 | no |
| unknown | business2 | ft | 1 | numéro entente-cadre | id | unknown | 0.6609 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9735 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.3847 | no |
| unknown | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5226 | no |
| unknown | business2 | ft | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5258 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9865 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.6889 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9903 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.6011 | no |
| unknown | business2 | ft | 1 | want to live in this parish & band b | quantity | unknown | 0.4689 | no |
| wrong | business2 | ft | 1 | account name | account | org | 0.7439 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.9095 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.6847 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.9219 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9777 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8146 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.5004 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9780 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.7480 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9708 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9690 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.8100 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8074 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8613 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5195 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5630 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.7167 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8852 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band a | quantity | category | 0.9365 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band d | quantity | category | 0.5352 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.6246 | no |
| wrong | business2 | ft | 1 | état | category | account | 0.6657 | no |
| critical | business2 | ft | 2 | fine | amount | rate | 0.5602 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9919 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7557 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8591 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9418 | yes |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.8990 | no |
| other_ng | business2 | ft | 2 | epc_score | other | rate | 0.5859 | no |
| unknown | business2 | ft | 2 | contravention | category | unknown | 0.3684 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.4222 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.5029 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.3894 | no |
| unknown | business2 | ft | 2 | household disposable income quintiles | category | unknown | 0.4827 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.8786 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9757 | no |
| unknown | business2 | ft | 2 | potential_epc_score_known | category | unknown | 0.4219 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7852 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7944 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.7842 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8661 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9850 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9841 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9826 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.6378 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9907 | no |
| wrong | business2 | ft | 2 | conservation_area_site_id | category | id | 0.9504 | no |
| wrong | business2 | ft | 2 | energy_consumption_known | category | quantity | 0.5230 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.7536 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | quantity | 0.9135 | no |
| wrong | business2 | ft | 2 | imd19_national_decile | category | quantity | 0.5231 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9449 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.8700 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.8570 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.5256 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9606 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.9307 | no |
| wrong | business2 | ft | 2 | service | account | address | 0.7037 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6520 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.8365 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.8969 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.5537 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8812 | yes |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4909 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4932 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5812 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4933 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4938 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4869 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9640 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8805 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.6023 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5008 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7687 | no |
| wrong | dev220 | blend50 | 1 | 随意契約理由 | text | category | 0.5016 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8715 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.4682 | no |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4944 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4930 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5812 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4948 | no |
| unknown | dev220 | blend50 | 2 | 商品オプション | text | unknown | 0.5000 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4758 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9735 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8827 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.7485 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5016 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7891 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8894 | yes |
| wrong | dev220 | blend60 | 1 | city | address | id | 0.5626 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9609 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.8994 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.5286 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.8015 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5754 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8778 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.5069 | no |
| wrong | dev220 | blend60 | 2 | city | address | id | 0.5520 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9723 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9021 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.7040 | no |
| wrong | dev220 | blend60 | 2 | 履行場所 | address | id | 0.5219 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.8260 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8976 | yes |
| unknown | dev220 | blend70 | 1 | taxable | category | unknown | 0.4914 | no |
| wrong | dev220 | blend70 | 1 | city | address | id | 0.6551 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9578 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9184 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8343 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6492 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8841 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.5456 | no |
| wrong | dev220 | blend70 | 2 | city | address | id | 0.6428 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9711 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9215 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.6595 | no |
| wrong | dev220 | blend70 | 2 | 履行場所 | address | id | 0.6054 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8629 | no |
| wrong | dev220 | blend70 | 2 | 随意契約理由 | text | category | 0.5187 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9223 | yes |
| wrong | dev220 | ft | 1 | city | address | id | 0.9328 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9485 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9752 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9328 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.8707 | no |
| critical | dev220 | ft | 2 | credit limit | amount | quantity | 0.6616 | yes |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9029 | yes |
| wrong | dev220 | ft | 2 | city | address | id | 0.9152 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9675 | no |
| wrong | dev220 | ft | 2 | description | text | category | 0.6169 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9796 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.5261 | no |
| wrong | dev220 | ft | 2 | 履行場所 | address | id | 0.8557 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.9736 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.6843 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | quantity | 0.6678 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.7651 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.5665 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9689 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.7326 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4991 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4653 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4655 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5533 | no |
| unknown | general | blend50 | 1 | goal | id | unknown | 0.4592 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.6705 | no |
| unknown | general | blend50 | 1 | lda | text | unknown | 0.4727 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4856 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4182 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4898 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4577 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4822 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9842 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3734 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9950 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8795 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3536 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5457 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.8885 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9005 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9157 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7715 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.9352 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.5588 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.8256 | no |
| other_ng | general | blend50 | 2 | episode | other | id | 0.7786 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5442 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9385 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9420 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4878 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4799 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5548 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8239 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4635 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4741 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4206 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4754 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4943 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4817 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9838 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4562 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9947 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8849 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3496 | no |
| wrong | general | blend50 | 2 | attrition | category | quantity | 0.6512 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.7312 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.8264 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.6304 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9169 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8343 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8073 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.9147 | no |
| wrong | general | blend50 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5141 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | quantity | 0.6400 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.7551 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.5033 | no |
| other_ng | general | blend60 | 1 | mt2 | other | category | 0.5347 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9685 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.6793 | no |
| unknown | general | blend60 | 1 | bib | id | unknown | 0.5052 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.4673 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6400 | no |
| unknown | general | blend60 | 1 | goal | id | unknown | 0.4384 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.6424 | no |
| unknown | general | blend60 | 1 | lda | text | unknown | 0.4919 | no |
| unknown | general | blend60 | 1 | pelicula | text | unknown | 0.4782 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.5004 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4872 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4638 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3884 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9854 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4477 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9940 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8785 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.3513 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.8692 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9085 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9069 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7903 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.9362 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5738 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.6333 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.8276 | no |
| other_ng | general | blend60 | 2 | episode | other | id | 0.7579 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9320 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9305 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.5511 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5642 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6417 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.8264 | no |
| unknown | general | blend60 | 2 | lda | text | unknown | 0.4810 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4587 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5799 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.5541 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9850 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.4042 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9937 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8849 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4172 | no |
| wrong | general | blend60 | 2 | attrition | category | quantity | 0.6900 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.6814 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.7947 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5764 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.5147 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9281 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8092 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.8333 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.9116 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5300 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.5014 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | quantity | 0.6122 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7450 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.6229 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9680 | no |
| other_ng | general | blend70 | 1 | ブロモホルム | other | quantity | 0.5062 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.6260 | no |
| unknown | general | blend70 | 1 | bib | id | unknown | 0.5893 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.5354 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7267 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.6143 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.5826 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3422 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9866 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9930 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8774 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3489 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.8499 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9165 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8981 | no |
| wrong | general | blend70 | 1 | source | category | text | 0.5529 | no |
| wrong | general | blend70 | 1 | source_value | category | text | 0.5298 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8091 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.9373 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6654 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.5221 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7078 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.8297 | no |
| other_ng | general | blend70 | 2 | episode | other | id | 0.7372 | no |
| other_ng | general | blend70 | 2 | mt2 | other | category | 0.5705 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9255 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9191 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.4859 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.6485 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7287 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8290 | no |
| unknown | general | blend70 | 2 | lda | text | unknown | 0.4984 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5339 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6754 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9861 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.3522 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9926 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8849 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4849 | no |
| unknown | general | blend70 | 2 | 駐車場 | category | unknown | 0.5015 | no |
| wrong | general | blend70 | 2 | attrition | category | quantity | 0.7287 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.6316 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7630 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.5225 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.5885 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9394 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7841 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8592 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.9085 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6143 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.6903 | yes |
| other_ng | general | ft | 1 | dag-stage | other | quantity | 0.5287 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.7149 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.8874 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9667 | no |
| other_ng | general | ft | 1 | ブロモホルム | other | quantity | 0.7226 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.5460 | no |
| unknown | general | ft | 1 | bib | id | unknown | 0.8416 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.7398 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9867 | no |
| unknown | general | ft | 1 | domain | category | unknown | 0.4098 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.5298 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8290 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.6496 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4128 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4956 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4865 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9902 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9900 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.8742 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.4040 | no |
| unknown | general | ft | 1 | 駐車場 | category | unknown | 0.5620 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.7921 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9405 | no |
| wrong | general | ft | 1 | place | org | address | 0.8716 | no |
| wrong | general | ft | 1 | source | category | text | 0.7498 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.7532 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8654 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9403 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9401 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.7450 | no |
| critical | general | ft | 2 | age_q3 | quantity | rate | 0.5998 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.5054 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9312 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.8358 | no |
| other_ng | general | ft | 2 | episode | other | id | 0.6750 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.8125 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9059 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.8848 | no |
| unknown | general | ft | 2 | age_q3_nd | quantity | unknown | 0.5872 | no |
| unknown | general | ft | 2 | author | person | unknown | 0.4821 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9013 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9896 | no |
| unknown | general | ft | 2 | domain | category | unknown | 0.4931 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.8366 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.7595 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9619 | no |
| unknown | general | ft | 2 | source | category | unknown | 0.4575 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9896 | no |
| unknown | general | ft | 2 | 発生県 | id | unknown | 0.3689 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9895 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.8849 | no |
| unknown | general | ft | 2 | 駐車場 | category | unknown | 0.7163 | no |
| wrong | general | ft | 2 | attrition | category | quantity | 0.8450 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.6680 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.8097 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9732 | no |
| wrong | general | ft | 2 | ngram | text | category | 0.5308 | no |
| wrong | general | ft | 2 | place | org | address | 0.7088 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9370 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8992 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8672 | no |

### unknown の判定理由

- date_value_evidence_low: 75件
- numeric_top2_too_close: 55件
- numeric_values_not_parseable: 26件
- other_class: 75件
- probability_below_threshold: 174件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 37件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 188件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 95件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
