# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-30T12:48:06+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 4 | 0 | 16 | 0 |
| business | blend50 | 2 | 490 | 5 | 1 | 13 | 0 |
| business | blend60 | 1 | 490 | 5 | 0 | 11 | 0 |
| business | blend60 | 2 | 490 | 5 | 0 | 9 | 0 |
| business | blend70 | 1 | 490 | 5 | 0 | 9 | 0 |
| business | blend70 | 2 | 490 | 7 | 0 | 6 | 0 |
| business | ft | 1 | 490 | 7 | 0 | 5 | 0 |
| business | ft | 2 | 490 | 7 | 0 | 5 | 0 |
| business2 | blend50 | 1 | 976 | 13 | 2 | 27 | 1 |
| business2 | blend50 | 2 | 976 | 14 | 3 | 28 | 1 |
| business2 | blend60 | 1 | 976 | 15 | 2 | 19 | 0 |
| business2 | blend60 | 2 | 976 | 12 | 2 | 23 | 1 |
| business2 | blend70 | 1 | 976 | 17 | 4 | 14 | 0 |
| business2 | blend70 | 2 | 976 | 12 | 3 | 18 | 1 |
| business2 | ft | 1 | 976 | 19 | 4 | 14 | 0 |
| business2 | ft | 2 | 976 | 17 | 3 | 13 | 1 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 7 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 4 | 1 | 0 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 0 | 0 |
| general | blend50 | 1 | 383 | 8 | 0 | 12 | 6 |
| general | blend50 | 2 | 383 | 8 | 0 | 17 | 6 |
| general | blend60 | 1 | 383 | 6 | 0 | 12 | 4 |
| general | blend60 | 2 | 383 | 7 | 0 | 15 | 7 |
| general | blend70 | 1 | 383 | 6 | 0 | 11 | 6 |
| general | blend70 | 2 | 383 | 9 | 0 | 12 | 7 |
| general | ft | 1 | 383 | 9 | 1 | 9 | 7 |
| general | ft | 2 | 383 | 12 | 1 | 10 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: text→category: 2, text→account: 2, category→text: 2, account→text: 1, quantity→amount: 1, org→account: 1
- business / blend60: text→category: 2, text→account: 2, category→text: 2, account→text: 1, category→id: 1, product→category: 1, org→account: 1
- business / blend70: text→category: 2, text→account: 2, category→text: 2, account→text: 1, category→id: 1, org→category: 1, product→category: 1, org→account: 1
- business / ft: org→category: 2, text→category: 2, text→account: 2, category→text: 2, account→text: 1, account→category: 1, category→id: 1, product→category: 1
- business2 / blend50: account→category: 4, address→category: 4, amount→quantity: 4, id→address: 3, quantity→category: 2, category→quantity: 2, category→text: 2, org→address: 2
- business2 / blend60: account→category: 4, address→category: 4, amount→quantity: 4, id→address: 3, id→category: 2, category→id: 2, quantity→category: 2, category→quantity: 2
- business2 / blend70: amount→quantity: 5, account→category: 4, category→quantity: 3, id→category: 2, category→id: 2, address→category: 2, quantity→amount: 2, org→address: 2
- business2 / ft: amount→quantity: 5, account→category: 4, category→quantity: 4, id→category: 3, address→org: 3, category→id: 2, address→category: 2, quantity→category: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, id→quantity: 2, text→category: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, id→quantity: 2, text→category: 1
- dev220 / ft: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, rate→tax_class: 1, address→id: 1
- general / blend50: org→address: 4, quantity→category: 3, person→org: 2, category→text: 2, text→category: 2, id→category: 2, address→org: 1
- general / blend60: org→address: 4, category→text: 2, quantity→category: 2, id→category: 2, address→org: 1, person→org: 1, category→org: 1
- general / blend70: org→address: 4, category→text: 3, quantity→category: 2, text→account: 2, address→org: 1, person→org: 1, category→org: 1, id→category: 1
- general / ft: category→text: 4, org→address: 4, quantity→category: 2, id→address: 2, text→account: 2, address→org: 1, id→quantity: 1, person→org: 1

### seedをまたいで再発した誤り

- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `title`、category→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `title`、category→text（seed 1, seed 2）
- business / ft: `entitiy`、org→category（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `title`、category→text（seed 1, seed 2）
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
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `health service executive area`、address→org（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `warddesc`、address→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
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
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `cleaned`、text→account（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `cleaned`、text→account（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5192 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4937 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4280 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4882 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6048 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5458 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5423 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.5184 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5824 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4256 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4546 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9819 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4350 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5869 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9475 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9110 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.5389 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.6989 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9249 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.6496 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.6481 | yes |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5325 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4571 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4335 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6049 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5434 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5425 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4900 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5586 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4543 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9806 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3391 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9447 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9122 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7667 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.6658 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9218 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.5042 | no |
| unknown | business | blend60 | 1 | abn | id | unknown | 0.6063 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4284 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.4624 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6804 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.3946 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4834 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9817 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.4662 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5048 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9447 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9202 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6046 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5836 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.7173 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9182 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.7028 | no |
| unknown | business | blend60 | 2 | commodity-title_fr | product | unknown | 0.4501 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4972 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6805 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5779 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9801 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.3512 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5782 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9413 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9216 | no |
| wrong | business | blend60 | 2 | commodity-title_en | product | category | 0.5200 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7988 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.6828 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9144 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.5283 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3946 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.3799 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7560 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3635 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9816 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.4975 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.5661 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9419 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9293 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.6703 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6790 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.7358 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9114 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.7560 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7562 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9797 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.3633 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.5083 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9380 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9309 | no |
| wrong | business | blend70 | 2 | commodity-title_en | product | category | 0.5829 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.5782 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.8308 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.6997 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9070 | no |
| wrong | business | blend70 | 2 | sub_category | category | account | 0.5104 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.5525 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9828 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3589 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9810 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9336 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9567 | no |
| wrong | business | ft | 1 | description | account | text | 0.8674 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.5382 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9652 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.7913 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.8912 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.5913 | no |
| wrong | business | ft | 1 | title | category | text | 0.9155 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9831 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9783 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.4165 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9279 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9590 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.7714 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.8215 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9270 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.7506 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8849 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.6430 | no |
| wrong | business | ft | 2 | title | category | text | 0.6248 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9770 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7771 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5286 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4929 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3045 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4026 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4887 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5465 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5417 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4645 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9877 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4981 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5867 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4600 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4884 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4895 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3824 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4788 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9896 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5718 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4467 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5065 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4136 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4959 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5321 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9920 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5925 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7200 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.8158 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5901 | no |
| wrong | business2 | blend50 | 1 | numéro | id | address | 0.5194 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.6000 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5081 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8981 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5809 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9030 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7077 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9758 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8336 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.6338 | yes |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8022 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.2392 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.4957 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4837 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.2643 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4827 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5443 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5420 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4610 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9867 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6028 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4209 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4940 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4523 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4627 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4874 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4021 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4882 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.4515 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5084 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4968 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5259 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9914 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.5364 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.6721 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5343 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7170 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5970 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5717 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.5750 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5014 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.8103 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.5842 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.8766 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.7581 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9794 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7476 | yes |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.2907 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4792 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5561 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9856 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3855 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3930 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3932 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5091 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5046 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4926 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5846 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4923 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5930 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9916 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6481 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5531 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6707 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7893 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6641 | no |
| wrong | business2 | blend60 | 1 | numéro | id | address | 0.5023 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6721 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5338 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5119 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8903 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.5135 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.8851 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.7259 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9779 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8154 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8033 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.2755 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4923 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.2947 | no |
| unknown | business2 | blend60 | 2 | health service executive area | address | unknown | 0.4717 | no |
| unknown | business2 | blend60 | 2 | loac_group | category | unknown | 0.4849 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5520 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9844 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3875 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4525 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3336 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3957 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9919 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5610 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.4165 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5829 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5941 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6149 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9909 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.5458 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.6433 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6078 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6671 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5266 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6421 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6420 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7850 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.5175 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.8533 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.7863 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.5558 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9817 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7181 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6808 | yes |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.2960 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9836 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.3109 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4147 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4499 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.5897 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5883 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.5710 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9913 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.7036 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6174 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6214 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.7627 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7381 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7441 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.5696 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.5642 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8825 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.5166 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.5386 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8671 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.7441 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9800 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7972 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6787 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8044 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.3124 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3422 | no |
| unknown | business2 | blend70 | 2 | health service executive area | address | unknown | 0.4978 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5158 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9821 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4517 | no |
| unknown | business2 | blend70 | 2 | situtation | address | unknown | 0.4523 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3806 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3667 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9872 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.4996 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.4240 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9905 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.5553 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.5404 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.6146 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6812 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6173 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7124 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7090 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.7597 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.8301 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.8146 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.7857 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9889 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6295 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9693 | yes |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.3117 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.5040 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4518 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9774 | no |
| unknown | business2 | ft | 1 | service | account | unknown | 0.2940 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.6202 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.8318 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9856 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9825 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9800 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9803 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.8072 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9902 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.8702 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8104 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.6830 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9601 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.9601 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.6768 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.7210 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.5435 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8593 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.7323 | no |
| wrong | business2 | ft | 1 | terminal | address | org | 0.5907 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.6765 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8133 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band a | quantity | category | 0.5221 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.7987 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9864 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7426 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9663 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.8077 | no |
| unknown | business2 | ft | 2 | amt-units_mnt-unite | category | unknown | 0.4393 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4849 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.5310 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.3530 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7267 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9754 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9851 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9836 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9822 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9890 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.5836 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.5762 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.7719 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.5282 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9016 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9234 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.9100 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.6445 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6837 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.6404 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.5432 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.5237 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.5127 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.7603 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.8995 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8549 | yes |
| unknown | dev220 | blend50 | 1 | name | person | unknown | 0.4984 | no |
| unknown | dev220 | blend50 | 1 | taxable | category | unknown | 0.4982 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4847 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4880 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4995 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4843 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4376 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9517 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8974 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5016 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7542 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8563 | yes |
| unknown | dev220 | blend50 | 2 | sales tax group | tax_class | unknown | 0.4775 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4876 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4997 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4895 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4942 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4779 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4796 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9791 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9063 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7808 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8736 | yes |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9479 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9124 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7611 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8753 | yes |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9807 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9231 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7931 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8923 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9441 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9274 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7681 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.5090 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8943 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9824 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9399 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8053 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9483 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9326 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9725 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7890 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.5673 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.7088 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9512 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9874 | no |
| wrong | dev220 | ft | 2 | shipping address | address | id | 0.5316 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9903 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8422 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.5523 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6369 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.6628 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.5577 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5079 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.7558 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9294 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4685 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.5177 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6014 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8480 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4737 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.3504 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4294 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4594 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9844 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4016 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9927 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9401 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5169 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5425 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5934 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9229 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9316 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7507 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.8571 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5425 | no |
| other_ng | general | blend50 | 2 | abstract rank | other | category | 0.5395 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.6520 | no |
| other_ng | general | blend50 | 2 | episode | other | id | 0.5301 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.5882 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.7474 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8738 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4869 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4822 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4535 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.6023 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.5621 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8415 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4717 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4142 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4654 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4894 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4352 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.3987 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9857 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4030 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9940 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9444 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3262 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.9429 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.5626 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8666 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9449 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8482 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.6212 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8091 | no |
| wrong | general | blend50 | 2 | 住家一部損壊 | quantity | category | 0.5074 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6940 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.6942 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.7229 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9154 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4722 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.6038 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6792 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.8747 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3200 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5223 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3530 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5076 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9851 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3215 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9913 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9399 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5282 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9216 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9253 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7832 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.8374 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.6108 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.6254 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.7120 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5732 | no |
| other_ng | general | blend60 | 2 | mt2 | other | category | 0.5398 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.6606 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.7127 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.8487 | no |
| unknown | general | blend60 | 2 | cleaned | text | unknown | 0.4845 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.4519 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6803 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.5878 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.8670 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4967 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5685 | no |
| unknown | general | blend60 | 2 | source | category | unknown | 0.4957 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4057 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3461 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9867 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3364 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9928 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9450 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.3907 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.9384 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.8560 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9480 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8252 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5376 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6278 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7797 | no |
| other_ng | general | blend70 | 1 | abstract rank | other | category | 0.5319 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7510 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7256 | no |
| other_ng | general | blend70 | 1 | mood | other | category | 0.5734 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.6899 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9014 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6899 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7570 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4629 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9015 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.3730 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6088 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.4100 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9859 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.3737 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9898 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9396 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.5503 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9202 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.9190 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8157 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.8176 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.6790 | no |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.7112 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7720 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.6657 | no |
| other_ng | general | blend70 | 2 | mt2 | other | category | 0.6288 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.7329 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.6781 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.8235 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.5255 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7583 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8924 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5792 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6626 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.4684 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3674 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9877 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.3921 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9917 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9456 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4552 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.9339 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.5453 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.8454 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9510 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8022 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6266 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.5081 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6345 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7504 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.5021 | yes |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.7126 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9221 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.8196 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.8113 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.6423 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.5912 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.8593 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9484 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9905 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9817 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.8681 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4862 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.4901 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9881 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9855 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9389 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.7847 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9162 | no |
| wrong | general | ft | 1 | place | org | address | 0.9000 | no |
| wrong | general | ft | 1 | property | category | text | 0.5319 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9134 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.7583 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.5330 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.8838 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.7462 | yes |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.9688 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9522 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.9431 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.8960 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9499 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.5743 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.7481 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.5490 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9922 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9687 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8267 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9450 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.6687 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.4313 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9907 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9881 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9474 | no |
| wrong | general | ft | 2 | author | person | org | 0.9203 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.7775 | no |
| wrong | general | ft | 2 | goal | id | category | 0.8135 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.5863 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9602 | no |
| wrong | general | ft | 2 | place | org | address | 0.7332 | no |
| wrong | general | ft | 2 | source | category | org | 0.8937 | no |
| wrong | general | ft | 2 | source | category | text | 0.6650 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.6544 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6622 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.5593 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 41件
- numeric_values_not_parseable: 18件
- other_class: 66件
- probability_below_threshold: 145件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 34件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 148件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 113件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
