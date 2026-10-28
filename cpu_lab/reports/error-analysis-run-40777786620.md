# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-28T23:17:20+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 6 | 0 | 20 | 0 |
| business | blend50 | 2 | 490 | 12 | 1 | 12 | 0 |
| business | blend60 | 1 | 490 | 9 | 0 | 13 | 0 |
| business | blend60 | 2 | 490 | 10 | 0 | 8 | 0 |
| business | blend70 | 1 | 490 | 12 | 1 | 11 | 0 |
| business | blend70 | 2 | 490 | 10 | 0 | 7 | 0 |
| business | ft | 1 | 490 | 15 | 4 | 7 | 0 |
| business | ft | 2 | 490 | 12 | 0 | 5 | 0 |
| business2 | blend50 | 1 | 976 | 11 | 1 | 31 | 2 |
| business2 | blend50 | 2 | 976 | 18 | 3 | 22 | 1 |
| business2 | blend60 | 1 | 976 | 14 | 1 | 24 | 1 |
| business2 | blend60 | 2 | 976 | 16 | 2 | 21 | 1 |
| business2 | blend70 | 1 | 976 | 14 | 2 | 20 | 2 |
| business2 | blend70 | 2 | 976 | 16 | 2 | 17 | 1 |
| business2 | ft | 1 | 976 | 16 | 2 | 17 | 2 |
| business2 | ft | 2 | 976 | 19 | 4 | 12 | 1 |
| dev220 | blend50 | 1 | 220 | 8 | 1 | 8 | 0 |
| dev220 | blend50 | 2 | 220 | 7 | 1 | 8 | 0 |
| dev220 | blend60 | 1 | 220 | 7 | 1 | 2 | 0 |
| dev220 | blend60 | 2 | 220 | 6 | 1 | 2 | 0 |
| dev220 | blend70 | 1 | 220 | 7 | 1 | 4 | 0 |
| dev220 | blend70 | 2 | 220 | 6 | 1 | 3 | 0 |
| dev220 | ft | 1 | 220 | 9 | 2 | 2 | 0 |
| dev220 | ft | 2 | 220 | 8 | 2 | 2 | 0 |
| general | blend50 | 1 | 383 | 7 | 0 | 14 | 6 |
| general | blend50 | 2 | 383 | 8 | 1 | 15 | 5 |
| general | blend60 | 1 | 383 | 8 | 0 | 12 | 4 |
| general | blend60 | 2 | 383 | 9 | 1 | 14 | 5 |
| general | blend70 | 1 | 383 | 8 | 0 | 12 | 4 |
| general | blend70 | 2 | 383 | 11 | 3 | 10 | 5 |
| general | ft | 1 | 383 | 7 | 1 | 16 | 5 |
| general | ft | 2 | 383 | 11 | 2 | 11 | 5 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, text→account: 2, product→category: 2, account→category: 2, text→org: 1, quantity→amount: 1, org→category: 1, text→category: 1
- business / blend60: org→account: 8, account→category: 3, text→account: 2, product→category: 2, text→org: 1, category→id: 1, text→category: 1, category→text: 1
- business / blend70: org→account: 8, account→category: 3, text→account: 2, product→category: 2, text→org: 1, account→org: 1, category→id: 1, category→account: 1
- business / ft: org→account: 8, amount→quantity: 4, account→category: 3, text→account: 2, product→category: 2, category→id: 2, category→text: 2, account→org: 1
- business2 / blend50: account→category: 5, category→id: 4, address→category: 4, category→quantity: 3, amount→quantity: 3, quantity→category: 2, org→address: 2, id→address: 2
- business2 / blend60: account→category: 5, category→id: 4, address→category: 4, category→quantity: 3, amount→quantity: 3, id→category: 2, org→address: 2, id→address: 2
- business2 / blend70: account→category: 5, category→id: 4, address→category: 4, category→quantity: 3, amount→quantity: 3, id→category: 2, id→address: 2, category→text: 1
- business2 / ft: category→id: 5, account→category: 4, category→quantity: 4, amount→quantity: 4, address→category: 3, account→org: 2, id→category: 2, quantity→amount: 2
- dev220 / blend50: quantity→category: 4, text→category: 3, org→account: 2, category→text: 2, category→tax_class: 2, id→quantity: 2
- dev220 / blend60: quantity→category: 4, org→account: 2, category→text: 2, category→tax_class: 2, id→quantity: 2, text→category: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, category→text: 2, category→tax_class: 2, id→quantity: 2, text→category: 1
- dev220 / ft: quantity→category: 4, category→text: 3, org→account: 2, text→category: 2, id→quantity: 2, amount→quantity: 2, rate→tax_class: 1, id→tax_class: 1
- general / blend50: org→address: 4, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1, person→org: 1, id→quantity: 1
- general / blend60: category→text: 4, org→address: 4, quantity→category: 2, text→category: 2, id→category: 2, address→org: 1, person→org: 1, id→quantity: 1
- general / blend70: category→text: 4, org→address: 4, quantity→category: 2, text→category: 2, id→quantity: 2, id→address: 1, address→org: 1, person→org: 1
- general / ft: category→text: 5, org→address: 3, quantity→category: 2, id→quantity: 2, id→address: 1, address→org: 1, person→org: 1, quantity→id: 1

### seedをまたいで再発した誤り

- business / blend50: `commodity-title_en`、product→category（seed 1, seed 2）
- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `commodity-title_en`、product→category（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `commodity-title_en`、product→category（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `commodity-title_en`、product→category（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
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
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `warddesc`、address→category（seed 1, seed 2）
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
- dev220 / blend60: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend60: `terms`、category→text（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `terms`、category→text（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `随意契約理由`、text→category（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
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
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3412 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.3797 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.3464 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.6046 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5586 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4731 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4691 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6392 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5798 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5769 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4575 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5294 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4181 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4859 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9741 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4637 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.3866 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5298 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9473 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8014 | no |
| wrong | business | blend50 | 1 | commodity-title_en | product | category | 0.5326 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9540 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.6260 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9805 | no |
| wrong | business | blend50 | 1 | merchant details | text | org | 0.5225 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8672 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.6600 | yes |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4859 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.4819 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4844 | no |
| unknown | business | blend50 | 2 | defence goods value | amount | unknown | 0.6061 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5599 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6385 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5755 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5701 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4674 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9725 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9246 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7972 | no |
| wrong | business | blend50 | 2 | commodity-title_en | product | category | 0.5309 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9535 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7001 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9774 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.6061 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5163 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5739 | no |
| wrong | business | blend50 | 2 | publisher label | org | category | 0.5060 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.7685 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5457 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.5986 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.3878 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.3801 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.3818 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7079 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4605 | no |
| unknown | business | blend60 | 1 | overseas sourced services | amount | unknown | 0.5045 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4193 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3891 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9764 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4540 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5576 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9463 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8328 | no |
| wrong | business | blend60 | 1 | commodity-title_en | product | category | 0.5929 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9469 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.5983 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9790 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5122 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5605 | no |
| wrong | business | blend60 | 1 | merchant details | text | org | 0.5149 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8573 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5100 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.5337 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.7071 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5545 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4134 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9744 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5927 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9191 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8277 | no |
| wrong | business | blend60 | 2 | commodity-title_en | product | category | 0.5909 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9463 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.6872 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9752 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.6564 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.5370 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6188 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.7390 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6084 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.5823 | no |
| critical | business | blend70 | 1 | overseas sourced goods | amount | quantity | 0.5372 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4524 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.4432 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4173 | no |
| unknown | business | blend70 | 1 | d1 | category | unknown | 0.4796 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7766 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.5821 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4204 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4331 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9786 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9452 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8641 | no |
| wrong | business | blend70 | 1 | account_name | account | org | 0.5108 | no |
| wrong | business | blend70 | 1 | commodity-title_en | product | category | 0.6532 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9398 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.5705 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9774 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5976 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6519 | no |
| wrong | business | blend70 | 1 | merchant details | text | org | 0.5074 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.8475 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.5564 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.5213 | no |
| unknown | business | blend70 | 2 | dispute-status_statut-de-différend-fra | category | unknown | 0.4991 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7756 | no |
| unknown | business | blend70 | 2 | publisher label | org | unknown | 0.3404 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9763 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.5254 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9135 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8582 | no |
| wrong | business | blend70 | 2 | commodity-title_en | product | category | 0.6509 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9391 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.6742 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9731 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7067 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.5578 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.6636 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.7094 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.6712 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.5661 | no |
| critical | business | ft | 1 | australian sourced goods | amount | quantity | 0.6461 | yes |
| critical | business | ft | 1 | australian sourced services | amount | quantity | 0.6327 | yes |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.7673 | yes |
| critical | business | ft | 1 | overseas sourced services | amount | quantity | 0.8150 | yes |
| unknown | business | ft | 1 | department | org | unknown | 0.4926 | no |
| unknown | business | ft | 1 | merchant details | text | unknown | 0.4848 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9826 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.4238 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9853 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9421 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9582 | no |
| wrong | business | ft | 1 | account_name | account | org | 0.6613 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.8342 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.6176 | no |
| wrong | business | ft | 1 | department | org | account | 0.9185 | no |
| wrong | business | ft | 1 | department | org | account | 0.9727 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.8537 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9260 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.8180 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.6955 | no |
| wrong | business | ft | 1 | title | category | account | 0.7234 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.6000 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9813 | no |
| unknown | business | ft | 2 | publisher label | org | unknown | 0.4855 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9820 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.8968 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9497 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.8308 | no |
| wrong | business | ft | 2 | department | org | account | 0.9174 | no |
| wrong | business | ft | 2 | department | org | account | 0.6354 | no |
| wrong | business | ft | 2 | department | org | account | 0.9665 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.6989 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.5337 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.8576 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.6201 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7982 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.6207 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.8595 | no |
| wrong | business | ft | 2 | title | category | text | 0.5173 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9684 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5016 | no |
| other_ng | business2 | blend50 | 1 | energy_consumption | other | quantity | 0.6075 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.3660 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.4332 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4834 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3133 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.4605 | no |
| unknown | business2 | blend50 | 1 | mcc description | category | unknown | 0.4936 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4773 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5813 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5765 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4027 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9852 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5898 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5718 | no |
| unknown | business2 | blend50 | 1 | scheme_description | category | unknown | 0.4805 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3684 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4941 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4827 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4220 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3082 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4237 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5247 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.6164 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5039 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4968 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5191 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9921 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.6416 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9047 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5754 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.6468 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.8441 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7762 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8509 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.8799 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9132 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7029 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9724 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8588 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.6437 | yes |
| other_ng | business2 | blend50 | 2 | energy_consumption | other | quantity | 0.7031 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4047 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5764 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5692 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4584 | no |
| unknown | business2 | blend50 | 2 | numéro | id | unknown | 0.4985 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9855 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5445 | no |
| unknown | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5187 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4458 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4910 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3923 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3380 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4214 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9885 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9839 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9832 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9865 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.6174 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4935 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5196 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9916 | no |
| wrong | business2 | blend50 | 2 | energy_consumption_known | category | quantity | 0.5727 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.5524 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5096 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7355 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5462 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5806 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6815 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.7940 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.7271 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5161 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7984 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6542 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9845 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.5967 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.6929 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9710 | yes |
| other_ng | business2 | blend60 | 1 | energy_consumption | other | quantity | 0.6413 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.4332 | no |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4737 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.4615 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4915 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.3478 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.5272 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.4406 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9826 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5313 | no |
| unknown | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.6143 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3083 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3037 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4376 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9919 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5640 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.6816 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5989 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5943 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6113 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9917 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5824 | no |
| wrong | business2 | blend60 | 1 | mcc description | category | text | 0.5562 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5348 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.5707 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.8995 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6424 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6762 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8642 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8098 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8463 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.8715 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.8984 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.7037 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9757 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8542 | yes |
| other_ng | business2 | blend60 | 2 | energy_consumption | other | quantity | 0.7561 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.4818 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.4858 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.4985 | no |
| unknown | business2 | blend60 | 2 | merchant description | category | unknown | 0.4772 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5193 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5474 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9830 | no |
| unknown | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5035 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3326 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3967 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9860 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9809 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9801 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9853 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5731 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.6827 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5720 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5897 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6118 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9910 | no |
| wrong | business2 | blend60 | 2 | energy_consumption_known | category | quantity | 0.6323 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5735 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6833 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6487 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7178 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.8040 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7510 | no |
| wrong | business2 | blend60 | 2 | service | account | org | 0.5327 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7833 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6007 | no |
| wrong | business2 | blend60 | 2 | terrace | quantity | address | 0.5046 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9840 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.5681 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.6917 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9736 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6939 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | amount | 0.5385 | no |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | quantity | 0.6752 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.5003 | no |
| unknown | business2 | blend70 | 1 | conservation_area_site_id | category | unknown | 0.4420 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.4897 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4995 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4026 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.6120 | no |
| unknown | business2 | blend70 | 1 | name | org | unknown | 0.4998 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9801 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5048 | no |
| unknown | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.6031 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.3187 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3482 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.5036 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.7467 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9912 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6794 | no |
| wrong | business2 | blend70 | 1 | mcc description | category | text | 0.6187 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.5922 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.8943 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7095 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7056 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8842 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8435 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8417 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.8631 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8836 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.7045 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9791 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8495 | yes |
| other_ng | business2 | blend70 | 2 | energy_consumption | other | quantity | 0.8090 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.5590 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.5385 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.4687 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5955 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9806 | no |
| unknown | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5346 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3861 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4623 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9869 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9840 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9779 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9770 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9841 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.5025 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.7481 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5056 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9904 | no |
| wrong | business2 | blend70 | 2 | energy_consumption_known | category | quantity | 0.6920 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6374 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6311 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7168 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7541 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.8141 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7748 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6197 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.7682 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.5471 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5879 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9835 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.5394 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.6905 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9813 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9788 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.7605 | no |
| other_ng | business2 | ft | 1 | energy_consumption | other | quantity | 0.7767 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.7016 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.5670 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8665 | no |
| unknown | business2 | ft | 1 | imd19_income_decile | category | unknown | 0.4963 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9725 | no |
| unknown | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5692 | no |
| unknown | business2 | ft | 1 | service | account | unknown | 0.4549 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.4819 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.7014 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.9422 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.4985 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9899 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.6170 | no |
| wrong | business2 | ft | 1 | cost centre description | account | org | 0.5897 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9703 | no |
| wrong | business2 | ft | 1 | mcc description | category | text | 0.8063 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7646 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8789 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9106 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.7937 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9444 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9444 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8278 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.8378 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8393 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.7070 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9892 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8355 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6276 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.6770 | yes |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.9679 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.7904 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.7614 | no |
| unknown | business2 | ft | 2 | loac_group | category | unknown | 0.4921 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.8239 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9732 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9780 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9690 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9677 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9806 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.9441 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9887 | no |
| wrong | business2 | ft | 2 | energy_consumption_known | category | quantity | 0.8709 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | quantity | 0.5818 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.8291 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9210 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.8630 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8441 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8463 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8805 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.7228 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.5776 | no |
| wrong | business2 | ft | 2 | terminal | address | org | 0.5466 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.6590 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8376 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9820 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.6869 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.9059 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.4231 | no |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4875 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4900 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5813 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4933 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4960 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4949 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4989 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9760 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8799 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.6602 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.6451 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5044 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7473 | no |
| wrong | dev220 | blend50 | 1 | 随意契約理由 | text | category | 0.5171 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8697 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.4843 | no |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4898 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4884 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5805 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4907 | no |
| unknown | dev220 | blend50 | 2 | 商品オプション | text | unknown | 0.4976 | no |
| unknown | dev220 | blend50 | 2 | 商品計 | amount | unknown | 0.5280 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4877 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9820 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8872 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.6882 | no |
| wrong | dev220 | blend50 | 2 | terms | category | text | 0.5511 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5005 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.6984 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.9191 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.4528 | no |
| unknown | dev220 | blend60 | 1 | tax id | id | unknown | 0.4909 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9753 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.8987 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.5980 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.6538 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7759 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5941 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8757 | yes |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.4560 | no |
| unknown | dev220 | blend60 | 2 | 商品計 | amount | unknown | 0.5546 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9825 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9075 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.6317 | no |
| wrong | dev220 | blend60 | 2 | terms | category | text | 0.5409 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7172 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9323 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.4825 | no |
| unknown | dev220 | blend70 | 1 | payment terms | category | unknown | 0.4902 | no |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.5727 | no |
| unknown | dev220 | blend70 | 1 | 支払を受ける者の個人番号 | id | unknown | 0.4697 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9746 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9176 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.5359 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.6624 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8044 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6710 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8816 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.4852 | no |
| unknown | dev220 | blend70 | 2 | tax id | id | unknown | 0.4812 | no |
| unknown | dev220 | blend70 | 2 | 商品計 | amount | unknown | 0.5812 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9830 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9277 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.5752 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.5308 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7360 | no |
| critical | dev220 | ft | 1 | credit limit | amount | quantity | 0.5715 | yes |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9718 | yes |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.8181 | no |
| unknown | dev220 | ft | 1 | 支払を受ける者の個人番号 | id | unknown | 0.6114 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9725 | no |
| wrong | dev220 | ft | 1 | payment terms | category | text | 0.6609 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9741 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.6883 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8901 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.5419 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.9019 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.8994 | yes |
| critical | dev220 | ft | 2 | 商品計 | amount | quantity | 0.6610 | yes |
| unknown | dev220 | ft | 2 | credit limit | amount | unknown | 0.5754 | no |
| unknown | dev220 | ft | 2 | taxable | category | unknown | 0.4855 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9845 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9886 | no |
| wrong | dev220 | ft | 2 | tax id | id | tax_class | 0.5249 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.5003 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.7923 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.5302 | no |
| other_ng | general | blend50 | 1 | characteristicorder | other | category | 0.5099 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.5594 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.7305 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9598 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.6526 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.5670 | no |
| unknown | general | blend50 | 1 | author | person | unknown | 0.4979 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4744 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5537 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8929 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4786 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4183 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4948 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.3939 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4798 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9833 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3855 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9934 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9124 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.4994 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.6869 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5779 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8590 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.7202 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.6820 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.8823 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5305 | no |
| critical | general | blend50 | 2 | 発生県 | id | quantity | 0.5985 | yes |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.5108 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.7161 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.7638 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9602 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9918 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4763 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4754 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5524 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8175 | no |
| unknown | general | blend50 | 2 | mechanism | category | unknown | 0.4650 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4558 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.3788 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.3507 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4738 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4489 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4797 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9832 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9925 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9207 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.2736 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.8952 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.6754 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5679 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8912 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8871 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8278 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.9057 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6340 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.7135 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9576 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.5833 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.4652 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6404 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9092 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.5005 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5696 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4992 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.4378 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3855 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9843 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4623 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9920 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9179 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.6274 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5134 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8587 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.6722 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.6829 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.8728 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5363 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5262 | no |
| critical | general | blend60 | 2 | 発生県 | id | quantity | 0.5749 | yes |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.5756 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.6963 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.7296 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9581 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9904 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5669 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6389 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.8188 | no |
| unknown | general | blend60 | 2 | mechanism | category | unknown | 0.4467 | no |
| unknown | general | blend60 | 2 | pelicula | text | unknown | 0.4563 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4377 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.3449 | no |
| unknown | general | blend60 | 2 | source | category | unknown | 0.4959 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4682 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.5446 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9842 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9910 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9279 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.3261 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.8782 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6136 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5014 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.8974 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8726 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.8579 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.9008 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5480 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7086 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6965 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9553 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.5140 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.5330 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7271 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4490 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9255 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.5826 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6634 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4276 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.4836 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.4482 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9853 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9907 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9234 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.5678 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8584 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6243 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6838 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.8632 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6216 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.5390 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.5530 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | id | 0.6584 | yes |
| critical | general | blend70 | 2 | goal | id | quantity | 0.5157 | yes |
| critical | general | blend70 | 2 | 発生県 | id | quantity | 0.5514 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.6405 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.6765 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.6953 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9559 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9889 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7254 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8200 | no |
| unknown | general | blend70 | 2 | mechanism | category | unknown | 0.4583 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5094 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.3816 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.5461 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9853 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9895 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9351 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.3785 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.8612 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5517 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9035 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8580 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.5779 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8879 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.8959 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6353 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.5182 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9323 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.6456 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.6189 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.6875 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9485 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4834 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.7363 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9874 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9745 | no |
| unknown | general | ft | 1 | organization name | org | unknown | 0.4823 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8292 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9449 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4224 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4930 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.5495 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4981 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.5357 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.6397 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9884 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9867 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9400 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.8574 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.6864 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.8345 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.8777 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.7692 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.6334 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.9329 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.7107 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.8351 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.6170 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.5926 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9493 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9845 | no |
| unknown | general | ft | 2 | cleaned | text | unknown | 0.3757 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9849 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.8238 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.7245 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.4917 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.4966 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.7798 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9883 | no |
| unknown | general | ft | 2 | 発生県 | id | unknown | 0.4807 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9850 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9567 | no |
| wrong | general | ft | 2 | author | person | org | 0.8101 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9219 | no |
| wrong | general | ft | 2 | mechanism | category | id | 0.5583 | no |
| wrong | general | ft | 2 | place | org | address | 0.8144 | no |
| wrong | general | ft | 2 | source | category | org | 0.8239 | no |
| wrong | general | ft | 2 | source | category | text | 0.5761 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9780 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8812 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8971 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 55件
- numeric_values_not_parseable: 21件
- other_class: 76件
- probability_below_threshold: 158件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 41件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 195件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 107件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
