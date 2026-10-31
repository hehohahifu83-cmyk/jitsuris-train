# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-31T19:02:23+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 4 | 0 | 18 | 0 |
| business | blend50 | 2 | 490 | 3 | 0 | 17 | 0 |
| business | blend60 | 1 | 490 | 5 | 0 | 11 | 0 |
| business | blend60 | 2 | 490 | 3 | 0 | 12 | 0 |
| business | blend70 | 1 | 490 | 5 | 0 | 7 | 0 |
| business | blend70 | 2 | 490 | 4 | 0 | 6 | 0 |
| business | ft | 1 | 490 | 6 | 0 | 7 | 1 |
| business | ft | 2 | 490 | 6 | 0 | 6 | 0 |
| business2 | blend50 | 1 | 976 | 15 | 2 | 31 | 1 |
| business2 | blend50 | 2 | 976 | 13 | 2 | 27 | 1 |
| business2 | blend60 | 1 | 976 | 14 | 2 | 22 | 0 |
| business2 | blend60 | 2 | 976 | 12 | 2 | 21 | 1 |
| business2 | blend70 | 1 | 976 | 17 | 3 | 18 | 0 |
| business2 | blend70 | 2 | 976 | 12 | 3 | 19 | 1 |
| business2 | ft | 1 | 976 | 20 | 3 | 17 | 3 |
| business2 | ft | 2 | 976 | 17 | 3 | 16 | 1 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 1 | 5 | 0 |
| dev220 | blend60 | 1 | 220 | 4 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 1 | 0 |
| dev220 | ft | 2 | 220 | 5 | 1 | 1 | 0 |
| general | blend50 | 1 | 383 | 9 | 0 | 13 | 6 |
| general | blend50 | 2 | 383 | 7 | 0 | 17 | 7 |
| general | blend60 | 1 | 383 | 5 | 0 | 15 | 6 |
| general | blend60 | 2 | 383 | 8 | 0 | 15 | 6 |
| general | blend70 | 1 | 383 | 7 | 0 | 13 | 7 |
| general | blend70 | 2 | 383 | 10 | 1 | 12 | 7 |
| general | ft | 1 | 383 | 8 | 0 | 11 | 9 |
| general | ft | 2 | 383 | 9 | 1 | 12 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: text→account: 2, account→text: 1, account→category: 1, category→text: 1, text→category: 1, org→account: 1
- business / blend60: text→account: 2, account→text: 1, account→category: 1, category→id: 1, category→text: 1, text→category: 1, org→account: 1
- business / blend70: text→account: 2, account→text: 1, account→category: 1, category→id: 1, category→text: 1, org→address: 1, text→category: 1, org→account: 1
- business / ft: text→account: 2, category→text: 2, org→category: 1, account→text: 1, account→category: 1, category→id: 1, org→address: 1, text→category: 1
- business2 / blend50: account→category: 5, address→category: 4, amount→quantity: 4, category→id: 2, quantity→category: 2, category→quantity: 2, category→text: 2, org→address: 2
- business2 / blend60: account→category: 5, amount→quantity: 4, address→category: 3, id→category: 2, category→id: 2, quantity→category: 2, category→quantity: 2, org→address: 2
- business2 / blend70: account→category: 5, amount→quantity: 4, id→category: 2, category→id: 2, address→category: 2, quantity→category: 2, category→quantity: 2, quantity→amount: 2
- business2 / ft: account→category: 4, amount→quantity: 4, id→category: 3, category→id: 3, category→quantity: 3, address→org: 3, account→org: 2, address→category: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, text→category: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, id→quantity: 2, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, address→id: 2, text→category: 1
- general / blend50: org→address: 4, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1, address→org: 1
- general / blend60: org→address: 4, category→text: 2, quantity→category: 2, address→org: 1, person→org: 1, category→org: 1, text→category: 1, id→category: 1
- general / blend70: org→address: 4, category→text: 3, quantity→category: 2, id→address: 1, address→org: 1, text→account: 1, person→org: 1, quantity→id: 1
- general / ft: org→address: 4, category→text: 3, quantity→category: 2, id→address: 1, text→org: 1, address→org: 1, text→account: 1, person→org: 1

### seedをまたいで再発した誤り

- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `health service executive area`、address→org（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
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
- dev220 / ft: `city`、address→id（seed 1, seed 2）
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
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5250 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4571 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4496 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.6179 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4949 | no |
| unknown | business | blend50 | 1 | merchant details | text | unknown | 0.4907 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6382 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5359 | no |
| unknown | business | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.6031 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5331 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4553 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5693 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3574 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4611 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9808 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5046 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9606 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9120 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.5521 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9441 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.6543 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.6240 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5263 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4872 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4583 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.6192 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6365 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5389 | no |
| unknown | business | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.6037 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5374 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4545 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5169 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4689 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9787 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.4461 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4044 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5394 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9602 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9209 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.6757 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.6287 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.7434 | no |
| unknown | business | blend60 | 1 | abn | id | unknown | 0.6127 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4579 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.4737 | no |
| unknown | business | blend60 | 1 | merchant details | text | unknown | 0.4673 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7080 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5209 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.3393 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9817 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5893 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9597 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9216 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6255 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5918 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9413 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6952 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.6619 | no |
| unknown | business | blend60 | 2 | abn | id | unknown | 0.6143 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4253 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.7060 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.4929 | no |
| unknown | business | blend60 | 2 | overseas sourced services | amount | unknown | 0.5860 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4468 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9793 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4991 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.3984 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5454 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9592 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9322 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.6892 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.6522 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.7005 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4561 | no |
| unknown | business | blend70 | 1 | merchant details | text | unknown | 0.4439 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7778 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3213 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9827 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9589 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9312 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.6989 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6886 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9385 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7362 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.6998 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3634 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7755 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9798 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.4180 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9582 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9435 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7028 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.6757 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.5063 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.6576 | no |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.6054 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.5848 | no |
| unknown | business | ft | 1 | merchant details | text | unknown | 0.4799 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9873 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3144 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9855 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9562 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9599 | no |
| wrong | business | ft | 1 | description | account | text | 0.9191 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.6452 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9791 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9302 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.8590 | no |
| wrong | business | ft | 1 | title | category | text | 0.8136 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.3975 | no |
| unknown | business | ft | 2 | entitiy | org | unknown | 0.3970 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9839 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9815 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9554 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9776 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.5663 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.7434 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.7462 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.6850 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.5289 | no |
| wrong | business | ft | 2 | title | category | account | 0.5163 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9635 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6195 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5493 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4851 | no |
| unknown | business2 | blend50 | 1 | cost centre description | account | unknown | 0.4604 | no |
| unknown | business2 | blend50 | 1 | epc_rating_known | category | unknown | 0.4589 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4310 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4427 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.5704 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4704 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5364 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.6034 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5309 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4857 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9868 | no |
| unknown | business2 | blend50 | 1 | potential_epc_rating_known | category | unknown | 0.3528 | no |
| unknown | business2 | blend50 | 1 | potential_epc_score_known | category | unknown | 0.4872 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5867 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4902 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4875 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4138 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4799 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9919 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5040 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.7247 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5119 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4310 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4921 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5294 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9921 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5824 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7817 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.7920 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5773 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.5787 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.6011 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5358 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5078 | no |
| wrong | business2 | blend50 | 1 | service | account | category | 0.5913 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8986 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5360 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9140 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.8024 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9755 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8908 | yes |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8600 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3893 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4442 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4157 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.5748 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4718 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5399 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.6036 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5370 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4428 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9796 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6091 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4341 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4930 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4679 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4850 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4972 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5402 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.4747 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5088 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4969 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5222 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9926 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.8816 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5275 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7457 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5822 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5574 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.5837 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5003 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.9144 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.5953 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9526 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.8104 | no |
| critical | business2 | blend60 | 1 | fine | amount | quantity | 0.5264 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9632 | yes |
| unknown | business2 | blend60 | 1 | cost centre description | account | unknown | 0.4508 | no |
| unknown | business2 | blend60 | 1 | epc_rating_known | category | unknown | 0.4296 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4730 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9847 | no |
| unknown | business2 | blend60 | 1 | potential_epc_rating_known | category | unknown | 0.4108 | no |
| unknown | business2 | blend60 | 1 | potential_epc_score_known | category | unknown | 0.4159 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5613 | no |
| unknown | business2 | blend60 | 1 | situtation | address | unknown | 0.4862 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3915 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4880 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3861 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5900 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.7442 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5782 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4508 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5879 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9917 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6289 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5355 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.7458 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7543 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6560 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6395 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.6236 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5788 | no |
| wrong | business2 | blend60 | 1 | service | account | category | 0.5465 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8930 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.8984 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.8294 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9775 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8869 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8700 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4639 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4297 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.4688 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.4462 | no |
| unknown | business2 | blend60 | 2 | health service executive area | address | unknown | 0.4669 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5014 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9761 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3656 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4566 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5095 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9874 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5443 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.4441 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5829 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5947 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6125 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9923 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.8890 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6039 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7025 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5026 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6321 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6455 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.9120 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.5346 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9448 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.8389 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.6101 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9628 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6735 | yes |
| unknown | business2 | blend70 | 1 | cost centre description | account | unknown | 0.4412 | no |
| unknown | business2 | blend70 | 1 | epc_rating_known | category | unknown | 0.4004 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.5150 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9826 | no |
| unknown | business2 | blend70 | 1 | potential_epc_rating_known | category | unknown | 0.4788 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.3446 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5031 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4012 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.5622 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4163 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9884 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.7637 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.5227 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9913 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.6754 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6005 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.7098 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.7165 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7348 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7003 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6462 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6219 | no |
| wrong | business2 | blend70 | 1 | service | account | category | 0.5018 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8874 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.5644 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8829 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish & band a | quantity | category | 0.5032 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.8563 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9795 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8830 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6789 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8801 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.5386 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4153 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.3692 | no |
| unknown | business2 | blend70 | 2 | habitatdescription | text | unknown | 0.4420 | no |
| unknown | business2 | blend70 | 2 | health service executive area | address | unknown | 0.4864 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5503 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9725 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4971 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4261 | no |
| unknown | business2 | blend70 | 2 | situtation | address | unknown | 0.4771 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4067 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.5906 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9855 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.4136 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9920 | no |
| wrong | business2 | blend70 | 2 | fine | amount | category | 0.5219 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.8964 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6803 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6594 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7068 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7073 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.9095 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9370 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.8674 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.8612 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9617 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9594 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.5111 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.5273 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.7448 | no |
| unknown | business2 | ft | 1 | epc_rating_known | category | unknown | 0.4131 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.6410 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.5528 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4821 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9762 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.3841 | no |
| unknown | business2 | ft | 1 | service | account | unknown | 0.3675 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.7847 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5847 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9863 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9840 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.8221 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.7384 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9902 | no |
| wrong | business2 | ft | 1 | cost centre description | account | org | 0.5585 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.8149 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7956 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.6020 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.6033 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9709 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.8826 | no |
| wrong | business2 | ft | 1 | potential_epc_rating_known | category | rate | 0.6831 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.7138 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.7510 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.5653 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8705 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.7992 | no |
| wrong | business2 | ft | 1 | terminal | address | org | 0.5715 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8362 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band a | quantity | category | 0.7186 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.9371 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9856 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8712 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9671 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9103 | no |
| unknown | business2 | ft | 2 | amt-units_mnt-unite | category | unknown | 0.7626 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.4835 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.5030 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.4930 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7817 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9618 | no |
| unknown | business2 | ft | 2 | potential_epc_score_known | category | unknown | 0.4542 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.5294 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8337 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9809 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9799 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4795 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9911 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.5118 | no |
| wrong | business2 | ft | 2 | fine | amount | category | 0.6813 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.5449 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.9185 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9097 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.5300 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9310 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.8927 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.5037 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.6076 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.9022 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.6745 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9135 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.9530 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8523 | yes |
| unknown | dev220 | blend50 | 1 | name | person | unknown | 0.4980 | no |
| unknown | dev220 | blend50 | 1 | sales tax group | tax_class | unknown | 0.4821 | no |
| unknown | dev220 | blend50 | 1 | terms | category | unknown | 0.4877 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4868 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4965 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4782 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4647 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9642 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.9517 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5026 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5013 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7970 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8421 | yes |
| unknown | dev220 | blend50 | 2 | sales tax group | tax_class | unknown | 0.4970 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4997 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4900 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4974 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4739 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9826 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9572 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.5048 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7665 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8751 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9611 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9574 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.8230 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8629 | yes |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9832 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9640 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7864 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8979 | yes |
| wrong | dev220 | blend70 | 1 | city | address | id | 0.5320 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9581 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9630 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8490 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8837 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9838 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9708 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8063 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9664 | yes |
| unknown | dev220 | ft | 1 | ポイント | amount | unknown | 0.5339 | no |
| wrong | dev220 | ft | 1 | city | address | id | 0.7565 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9488 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9800 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9270 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.5101 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9461 | yes |
| unknown | dev220 | ft | 2 | 税率 | rate | unknown | 0.4917 | no |
| wrong | dev220 | ft | 2 | city | address | id | 0.5176 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9856 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9911 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8660 | no |
| other_ng | general | blend50 | 1 | abstract rank | other | category | 0.5245 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6325 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.6519 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.8705 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9236 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.5055 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4847 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4933 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6110 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8079 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4757 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.3632 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4666 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4479 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4711 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9822 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4027 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9941 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9445 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5752 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5518 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5687 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9250 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9337 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7324 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.7609 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5007 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5242 | no |
| other_ng | general | blend50 | 2 | abstract rank | other | category | 0.5210 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.6370 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5270 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.6134 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8574 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9748 | no |
| other_ng | general | blend50 | 2 | 被害域長さ(100m)最小 | other | quantity | 0.5018 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4869 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4551 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.6111 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8199 | no |
| unknown | general | blend50 | 2 | mechanism | category | unknown | 0.4503 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4546 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4572 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4037 | no |
| unknown | general | blend50 | 2 | source | category | unknown | 0.4983 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4624 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4475 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.3942 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9823 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3746 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9932 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9528 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3400 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.9571 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.6710 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.7777 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9444 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.7996 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.6455 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8177 | no |
| other_ng | general | blend60 | 1 | abstract rank | other | category | 0.5931 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6950 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.6685 | no |
| other_ng | general | blend60 | 1 | mt2 | other | category | 0.5549 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.8613 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9085 | no |
| unknown | general | blend60 | 1 | app | category | unknown | 0.4815 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4984 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4700 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.5725 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6869 | no |
| unknown | general | blend60 | 1 | goal | id | unknown | 0.4979 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.8357 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3440 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4981 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3610 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5227 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9837 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4829 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9929 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9471 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9232 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9282 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7655 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.7225 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5883 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.5888 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.7004 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5643 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.6820 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8456 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9699 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5291 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6870 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.8501 | no |
| unknown | general | blend60 | 2 | mechanism | category | unknown | 0.4294 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5483 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4702 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5346 | no |
| unknown | general | blend60 | 2 | source | category | unknown | 0.4735 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.5167 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4199 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9839 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.4185 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9919 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9570 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.3400 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.9567 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6114 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7487 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9464 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.7673 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5575 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6611 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7907 | no |
| other_ng | general | blend70 | 1 | abstract rank | other | category | 0.6616 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7576 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6851 | no |
| other_ng | general | blend70 | 1 | mood | other | category | 0.5793 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.6464 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.8521 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8934 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.5372 | no |
| unknown | general | blend70 | 1 | author | person | unknown | 0.4965 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6517 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7628 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4270 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.8636 | no |
| unknown | general | blend70 | 1 | ngram | text | unknown | 0.4974 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4011 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4299 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.4199 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9853 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9918 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9496 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.5480 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9213 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.9226 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.7985 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.6842 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.5630 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.6523 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | id | 0.6157 | yes |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.6567 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7639 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.6548 | no |
| other_ng | general | blend70 | 2 | mt2 | other | category | 0.5778 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.7507 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8338 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9650 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7629 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8803 | no |
| unknown | general | blend70 | 2 | mechanism | category | unknown | 0.4400 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6394 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6232 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6027 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4544 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9854 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.4877 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9905 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9612 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.3960 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.9563 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5519 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.7196 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9485 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7349 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6498 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.5246 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6768 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7637 | no |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.8673 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9452 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.7351 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.5908 | no |
| other_ng | general | ft | 1 | fulltext rank | other | category | 0.5034 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.8184 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.9210 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.8244 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.8480 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.7653 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.8892 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9904 | no |
| unknown | general | ft | 1 | goal | id | unknown | 0.3615 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9471 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.5723 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4428 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3722 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9899 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9882 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9572 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.7818 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9158 | no |
| wrong | general | ft | 1 | ngram | text | org | 0.5481 | no |
| wrong | general | ft | 1 | place | org | address | 0.9060 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8977 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.5690 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.8035 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.8445 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.8756 | yes |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.8602 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9543 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.9262 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.8230 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9566 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.7983 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9503 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.5915 | no |
| unknown | general | ft | 2 | cleaned | text | unknown | 0.4215 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9905 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9710 | no |
| unknown | general | ft | 2 | indicator | text | unknown | 0.4937 | no |
| unknown | general | ft | 2 | mechanism | category | unknown | 0.5309 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9127 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8891 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.8604 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9901 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9865 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9737 | no |
| wrong | general | ft | 2 | author | person | org | 0.9551 | no |
| wrong | general | ft | 2 | goal | id | category | 0.6325 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9546 | no |
| wrong | general | ft | 2 | place | org | address | 0.6379 | no |
| wrong | general | ft | 2 | source | category | org | 0.9266 | no |
| wrong | general | ft | 2 | source | category | text | 0.6779 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7238 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6827 | no |

### unknown の判定理由

- date_value_evidence_low: 73件
- numeric_top2_too_close: 50件
- numeric_values_not_parseable: 20件
- other_class: 73件
- probability_below_threshold: 161件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 30件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 142件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 111件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
