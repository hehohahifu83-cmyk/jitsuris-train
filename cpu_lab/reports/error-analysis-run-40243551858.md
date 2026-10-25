# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-25T23:43:48+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 8 | 1 | 22 | 1 |
| business | blend50 | 2 | 490 | 10 | 1 | 21 | 1 |
| business | blend60 | 1 | 490 | 10 | 1 | 14 | 1 |
| business | blend60 | 2 | 490 | 12 | 1 | 15 | 1 |
| business | blend70 | 1 | 490 | 11 | 1 | 13 | 0 |
| business | blend70 | 2 | 490 | 13 | 1 | 12 | 1 |
| business | ft | 1 | 490 | 15 | 2 | 7 | 0 |
| business | ft | 2 | 490 | 16 | 1 | 8 | 1 |
| business2 | blend50 | 1 | 976 | 12 | 5 | 36 | 2 |
| business2 | blend50 | 2 | 976 | 13 | 4 | 33 | 3 |
| business2 | blend60 | 1 | 976 | 14 | 5 | 31 | 0 |
| business2 | blend60 | 2 | 976 | 12 | 4 | 32 | 1 |
| business2 | blend70 | 1 | 976 | 15 | 6 | 27 | 0 |
| business2 | blend70 | 2 | 976 | 12 | 3 | 29 | 1 |
| business2 | ft | 1 | 976 | 16 | 5 | 23 | 1 |
| business2 | ft | 2 | 976 | 16 | 4 | 20 | 0 |
| dev220 | blend50 | 1 | 220 | 8 | 1 | 11 | 0 |
| dev220 | blend50 | 2 | 220 | 7 | 2 | 12 | 0 |
| dev220 | blend60 | 1 | 220 | 7 | 1 | 6 | 0 |
| dev220 | blend60 | 2 | 220 | 8 | 2 | 4 | 0 |
| dev220 | blend70 | 1 | 220 | 8 | 1 | 5 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 2 | 4 | 0 |
| dev220 | ft | 1 | 220 | 9 | 1 | 3 | 0 |
| dev220 | ft | 2 | 220 | 8 | 2 | 2 | 0 |
| general | blend50 | 1 | 383 | 12 | 0 | 17 | 6 |
| general | blend50 | 2 | 383 | 12 | 0 | 15 | 8 |
| general | blend60 | 1 | 383 | 14 | 0 | 15 | 5 |
| general | blend60 | 2 | 383 | 13 | 0 | 13 | 6 |
| general | blend70 | 1 | 383 | 16 | 1 | 11 | 6 |
| general | blend70 | 2 | 383 | 15 | 0 | 14 | 6 |
| general | ft | 1 | 383 | 14 | 1 | 14 | 6 |
| general | ft | 2 | 383 | 13 | 0 | 14 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 2 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 2 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 4 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 2 | 2 | 2 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 6, account→text: 3, account→category: 3, quantity→amount: 2, text→account: 2, category→id: 1, text→category: 1
- business / blend60: org→account: 8, account→category: 3, quantity→amount: 2, account→text: 2, text→account: 2, product→category: 1, category→id: 1, org→address: 1
- business / blend70: org→account: 6, account→category: 5, quantity→amount: 2, account→text: 2, category→account: 2, category→id: 2, text→org: 1, product→category: 1
- business / ft: category→account: 6, account→category: 5, org→account: 4, quantity→amount: 2, account→text: 2, id→category: 2, org→address: 2, category→id: 2
- business2 / blend50: account→category: 5, amount→quantity: 5, quantity→amount: 2, amount→id: 2, address→org: 2, quantity→category: 2, org→address: 2, id→address: 2
- business2 / blend60: account→category: 5, amount→quantity: 5, quantity→amount: 2, amount→id: 2, quantity→category: 2, address→org: 2, org→address: 2, category→quantity: 1
- business2 / blend70: amount→quantity: 6, account→category: 5, quantity→amount: 2, quantity→category: 2, org→address: 2, account→org: 1, amount→id: 1, category→quantity: 1
- business2 / ft: amount→quantity: 6, account→category: 3, quantity→amount: 3, category→id: 3, account→org: 2, quantity→category: 2, category→quantity: 2, rate→category: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, category→text: 2, category→tax_class: 2, id→quantity: 2, person→org: 1, text→category: 1, amount→quantity: 1
- dev220 / blend60: category→text: 4, quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, amount→quantity: 1
- dev220 / blend70: category→text: 5, quantity→category: 4, org→account: 2, id→quantity: 2, category→tax_class: 1, amount→quantity: 1
- dev220 / ft: category→text: 6, quantity→category: 4, org→account: 2, id→quantity: 2, category→tax_class: 1, text→category: 1, amount→quantity: 1
- general / blend50: text→category: 8, org→address: 4, category→text: 3, person→org: 2, category→quantity: 2, quantity→category: 2, id→category: 2, address→org: 1
- general / blend60: text→category: 9, category→text: 4, org→address: 4, person→org: 2, category→quantity: 2, quantity→category: 2, id→category: 2, id→address: 1
- general / blend70: text→category: 9, category→text: 5, org→address: 4, person→org: 2, category→quantity: 2, quantity→category: 2, id→address: 2, id→category: 2
- general / ft: text→category: 7, category→text: 5, org→address: 4, quantity→category: 2, id→address: 2, id→category: 2, category→quantity: 1, quantity→amount: 1
- japan_procurement / ft: amount→quantity: 2

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `entitiy`、org→account（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `regrp_nom`、account→category（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `regrp_nom`、account→category（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `segment`、id→category（seed 1, seed 2）
- business / ft: `segment-title_fr`、category→account（seed 1, seed 2）
- business / ft: `sub_category`、category→account（seed 1, seed 2）
- business / ft: `title`、category→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `fine`、amount→id（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `super output area 2011 name`、address→org（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `fine`、amount→id（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / ft: `fuel_poverty`、rate→category（seed 1, seed 2）
- business2 / ft: `health service executive area`、address→org（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend50: `terms`、category→text（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend60: `terms`、category→text（seed 1, seed 2）
- dev220 / blend60: `年末調整未済`、category→text（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `年末調整未済`、category→text（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `terms`、category→text（seed 1, seed 2）
- dev220 / ft: `年末調整未済`、category→text（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `indicator`、text→category（seed 1, seed 2）
- general / blend50: `itemfield1`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `lda`、text→category（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend50: `年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者)`、category→quantity（seed 1, seed 2）
- general / blend60: `author`、person→org（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `indicator`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `lda`、text→category（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `term`、text→category（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者)`、category→quantity（seed 1, seed 2）
- general / blend70: `author`、person→org（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `indicator`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `lda`、text→category（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `term`、text→category（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者)`、category→quantity（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `goal`、id→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `lda`、text→category（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `term`、text→category（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.8570 | yes |
| other_ng | business | blend50 | 1 | km budgété | other | amount | 0.5942 | no |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5466 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5292 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5935 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.4951 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5816 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4610 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5867 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4893 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5265 | no |
| unknown | business | blend50 | 1 | merchant details | text | unknown | 0.4282 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.5225 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4229 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3637 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4823 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9662 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4711 | no |
| unknown | business | blend50 | 1 | segment-title_en | category | unknown | 0.4748 | no |
| unknown | business | blend50 | 1 | segment-title_fr | category | unknown | 0.4034 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.3918 | no |
| unknown | business | blend50 | 1 | tournée | id | unknown | 0.4746 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.8898 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8394 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.6733 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.5938 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9555 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.6107 | no |
| wrong | business | blend50 | 1 | ligne | category | id | 0.5199 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.6134 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5494 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.8678 | yes |
| other_ng | business | blend50 | 2 | km budgété | other | amount | 0.8621 | no |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.4758 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5338 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5587 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4387 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4472 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5797 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.3277 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5834 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.5141 | no |
| unknown | business | blend50 | 2 | family-title_fr | category | unknown | 0.4785 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.5131 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.3899 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.4283 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4812 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9630 | no |
| unknown | business | blend50 | 2 | segment-title_en | category | unknown | 0.4706 | no |
| unknown | business | blend50 | 2 | segment-title_fr | category | unknown | 0.3529 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.3770 | no |
| unknown | business | blend50 | 2 | tournée | id | unknown | 0.4799 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9204 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8589 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.6992 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.5646 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9364 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.6012 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.5559 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5792 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8431 | no |
| wrong | business | blend50 | 2 | regrp_nom | account | text | 0.5084 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5523 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.8287 | yes |
| other_ng | business | blend60 | 1 | km budgété | other | amount | 0.5307 | no |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.6008 | no |
| unknown | business | blend60 | 1 | description | text | unknown | 0.4806 | no |
| unknown | business | blend60 | 1 | merchant details | text | unknown | 0.4421 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6083 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5030 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4180 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3877 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9677 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4871 | no |
| unknown | business | blend60 | 1 | segment-title_fr | category | unknown | 0.4719 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4419 | no |
| unknown | business | blend60 | 1 | tournée | id | unknown | 0.3930 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.8728 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8369 | no |
| wrong | business | blend60 | 1 | commodity-title_en | product | category | 0.5303 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.6091 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.5442 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9483 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6796 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5556 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.6011 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.5447 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6324 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.8417 | yes |
| other_ng | business | blend60 | 2 | km budgété | other | amount | 0.8521 | no |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5377 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.4748 | no |
| unknown | business | blend60 | 2 | agebann | category | unknown | 0.4978 | no |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.5087 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3398 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.5970 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.3128 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4550 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9638 | no |
| unknown | business | blend60 | 2 | regrp_nom | account | unknown | 0.4510 | no |
| unknown | business | blend60 | 2 | segment-title_fr | category | unknown | 0.4112 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.4241 | no |
| unknown | business | blend60 | 2 | tournée | id | unknown | 0.3994 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9095 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8603 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.6402 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.5091 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9254 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.6682 | no |
| wrong | business | blend60 | 2 | entitiy | org | account | 0.5019 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.5953 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6132 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5232 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8203 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6358 | no |
| wrong | business | blend60 | 2 | sub_category | category | account | 0.5083 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.8004 | yes |
| unknown | business | blend70 | 1 | department | org | unknown | 0.4945 | no |
| unknown | business | blend70 | 1 | merchant details | text | unknown | 0.4561 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.6941 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4865 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.3817 | no |
| unknown | business | blend70 | 1 | purposeofexpenditure | text | unknown | 0.4825 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9691 | no |
| unknown | business | blend70 | 1 | segment | id | unknown | 0.4939 | no |
| unknown | business | blend70 | 1 | sub_category | category | unknown | 0.4885 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.4920 | no |
| unknown | business | blend70 | 1 | tournée | id | unknown | 0.4028 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.8558 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8345 | no |
| wrong | business | blend70 | 1 | commodity-title_en | product | category | 0.5995 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.5450 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9410 | no |
| wrong | business | blend70 | 1 | description | text | org | 0.5515 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7485 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6482 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6823 | no |
| wrong | business | blend70 | 1 | regrp_nom | account | category | 0.5655 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7154 | no |
| wrong | business | blend70 | 1 | segment-title_fr | category | account | 0.5403 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.8157 | yes |
| other_ng | business | blend70 | 2 | km budgété | other | amount | 0.8421 | no |
| unknown | business | blend70 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5096 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3773 | no |
| unknown | business | blend70 | 2 | description_entente | text | unknown | 0.4302 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.6810 | no |
| unknown | business | blend70 | 2 | overseas sourced goods | amount | unknown | 0.3531 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9646 | no |
| unknown | business | blend70 | 2 | segment | id | unknown | 0.4737 | no |
| unknown | business | blend70 | 2 | segment-title_fr | category | unknown | 0.4696 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.4712 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.3259 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.8986 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8618 | no |
| wrong | business | blend70 | 2 | agebann | category | id | 0.5626 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.5813 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9144 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.7352 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.5855 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.6348 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.6472 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6061 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.7975 | no |
| wrong | business | blend70 | 2 | regrp_nom | account | category | 0.5010 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.7194 | no |
| wrong | business | blend70 | 2 | sub_category | category | account | 0.5638 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.7156 | yes |
| critical | business | ft | 1 | tournée | id | quantity | 0.5753 | yes |
| unknown | business | ft | 1 | description_entente | text | unknown | 0.4947 | no |
| unknown | business | ft | 1 | merchant details | text | unknown | 0.4978 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9514 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9734 | no |
| unknown | business | ft | 1 | type de matériel | category | unknown | 0.4793 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.8049 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.8271 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.8074 | no |
| wrong | business | ft | 1 | department | org | account | 0.9194 | no |
| wrong | business | ft | 1 | description | text | org | 0.7878 | no |
| wrong | business | ft | 1 | description | account | text | 0.9552 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.9259 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9258 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | address | 0.6920 | no |
| wrong | business | ft | 1 | regrp_nom | account | category | 0.8008 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9645 | no |
| wrong | business | ft | 1 | segment | id | category | 0.6405 | no |
| wrong | business | ft | 1 | segment-title_fr | category | account | 0.7456 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.6228 | no |
| wrong | business | ft | 1 | title | category | account | 0.6422 | no |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.7374 | yes |
| other_ng | business | ft | 2 | km budgété | other | amount | 0.8122 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4899 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9327 | no |
| unknown | business | ft | 2 | overseas sourced goods | amount | unknown | 0.5041 | no |
| unknown | business | ft | 2 | prev_des_reslt_2023-2024 | amount | unknown | 0.5091 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9670 | no |
| unknown | business | ft | 2 | tournée | id | unknown | 0.4654 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.8660 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8661 | no |
| wrong | business | ft | 2 | agebann | category | id | 0.7569 | no |
| wrong | business | ft | 2 | department | org | account | 0.8813 | no |
| wrong | business | ft | 2 | description | account | text | 0.9362 | no |
| wrong | business | ft | 2 | description_entente | text | account | 0.5920 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.8364 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.7531 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7493 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.8549 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7291 | no |
| wrong | business | ft | 2 | regrp_nom | account | category | 0.7086 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.9702 | no |
| wrong | business | ft | 2 | segment | id | category | 0.6767 | no |
| wrong | business | ft | 2 | segment-title_fr | category | account | 0.6446 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.7304 | no |
| wrong | business | ft | 2 | title | category | account | 0.6125 | no |
| critical | business2 | blend50 | 1 | fine | amount | id | 0.6251 | yes |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9728 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9001 | yes |
| critical | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6252 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.8558 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5019 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5059 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5484 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5023 | no |
| unknown | business2 | blend50 | 1 | cost centre description | account | unknown | 0.4335 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4098 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.4684 | no |
| unknown | business2 | blend50 | 1 | health service executive area | address | unknown | 0.4880 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.4044 | no |
| unknown | business2 | blend50 | 1 | merchant description | category | unknown | 0.4488 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.3608 | no |
| unknown | business2 | blend50 | 1 | number_habitable_rooms_known | category | unknown | 0.5506 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4217 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9639 | no |
| unknown | business2 | blend50 | 1 | potential_epc_rating_known | category | unknown | 0.3876 | no |
| unknown | business2 | blend50 | 1 | potential_epc_score_known | category | unknown | 0.3611 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.3978 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4376 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5586 | no |
| unknown | business2 | blend50 | 1 | return-on-investments_revenus-de-placements | amount | unknown | 0.5478 | no |
| unknown | business2 | blend50 | 1 | scheme_description | category | unknown | 0.4869 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3105 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.4941 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4976 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4617 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3283 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4714 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9828 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9835 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9846 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9858 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9806 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.3782 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5105 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.4937 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9853 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.7618 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4182 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.8648 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.8051 | no |
| wrong | business2 | blend50 | 1 | numéro | id | address | 0.5044 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.5303 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.6127 | no |
| wrong | business2 | blend50 | 1 | super output area 2011 name | address | org | 0.5268 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9816 | no |
| critical | business2 | blend50 | 2 | fine | amount | id | 0.5626 | yes |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9638 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8577 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.8389 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.5274 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | quantity | 0.6267 | no |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5022 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.4792 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5787 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3756 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4761 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.4713 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4949 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.3209 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.4158 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4627 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9700 | no |
| unknown | business2 | blend50 | 2 | post code sector | address | unknown | 0.4290 | no |
| unknown | business2 | blend50 | 2 | potential_epc_rating_known | category | unknown | 0.3863 | no |
| unknown | business2 | blend50 | 2 | potential_epc_score_known | category | unknown | 0.4739 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4487 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5659 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3119 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4849 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.3913 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4203 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4050 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4665 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9822 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9809 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9826 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9783 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.5143 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5373 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.5157 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.4989 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9883 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.7481 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4112 | no |
| wrong | business2 | blend50 | 2 | imd19_national_decile | category | id | 0.6007 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.8847 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.9273 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5232 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.6174 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6537 | no |
| wrong | business2 | blend50 | 2 | super output area 2011 name | address | org | 0.5714 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9809 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.5917 | no |
| critical | business2 | blend60 | 1 | fine | amount | id | 0.6000 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9751 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9151 | yes |
| critical | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6906 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.8273 | yes |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5685 | no |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4649 | no |
| unknown | business2 | blend60 | 1 | cost centre description | account | unknown | 0.4735 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4839 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.4098 | no |
| unknown | business2 | blend60 | 1 | merchant description | category | unknown | 0.4801 | no |
| unknown | business2 | blend60 | 1 | monitor | id | unknown | 0.3925 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.4303 | no |
| unknown | business2 | blend60 | 1 | numéro | id | unknown | 0.4891 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9572 | no |
| unknown | business2 | blend60 | 1 | potential_epc_rating_known | category | unknown | 0.3980 | no |
| unknown | business2 | blend60 | 1 | potential_epc_score_known | category | unknown | 0.3757 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.4774 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.5251 | no |
| unknown | business2 | blend60 | 1 | return-on-investments_revenus-de-placements | amount | unknown | 0.5888 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4342 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3362 | no |
| unknown | business2 | blend60 | 1 | super output area 2011 name | address | unknown | 0.4664 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3013 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3978 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9809 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9807 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9818 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9832 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9787 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4167 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5660 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.5834 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9829 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.7598 | no |
| unknown | business2 | blend60 | 1 | warddesc | address | unknown | 0.3412 | no |
| wrong | business2 | blend60 | 1 | fuel_poverty | rate | category | 0.5036 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.5321 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.8394 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7831 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6184 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.5084 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.5590 | no |
| wrong | business2 | blend60 | 1 | situtation | address | text | 0.5457 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9795 | no |
| critical | business2 | blend60 | 2 | fine | amount | id | 0.5250 | yes |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9644 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8642 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.8070 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | quantity | 0.5865 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5419 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5287 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4366 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.5634 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.3825 | no |
| unknown | business2 | blend60 | 2 | health service executive area | address | unknown | 0.4802 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.3351 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms_known | category | unknown | 0.4567 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4796 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9645 | no |
| unknown | business2 | blend60 | 2 | post code sector | address | unknown | 0.4974 | no |
| unknown | business2 | blend60 | 2 | potential_epc_rating_known | category | unknown | 0.3964 | no |
| unknown | business2 | blend60 | 2 | potential_epc_score_known | category | unknown | 0.5589 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4861 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4778 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.2902 | no |
| unknown | business2 | blend60 | 2 | surveyname | text | unknown | 0.3804 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4936 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4856 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3919 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9802 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9776 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9794 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9825 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9760 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.5800 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5307 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5610 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.5937 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9864 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.7433 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.3440 | no |
| wrong | business2 | blend60 | 2 | imd19_national_decile | category | id | 0.6453 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.8633 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.9297 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.5647 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6015 | no |
| wrong | business2 | blend60 | 2 | super output area 2011 name | address | org | 0.5199 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9787 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.5839 | no |
| critical | business2 | blend70 | 1 | fine | amount | id | 0.5749 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9775 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9301 | yes |
| critical | business2 | blend70 | 1 | return-on-investments_revenus-de-placements | amount | quantity | 0.6299 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7559 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.7988 | yes |
| unknown | business2 | blend70 | 1 | conservation_area_site_id | category | unknown | 0.4487 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.5580 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.4151 | no |
| unknown | business2 | blend70 | 1 | monitor | id | unknown | 0.4241 | no |
| unknown | business2 | blend70 | 1 | numbers of | date | unknown | 0.4390 | no |
| unknown | business2 | blend70 | 1 | numéro | id | unknown | 0.4933 | no |
| unknown | business2 | blend70 | 1 | numéro_uev | id | unknown | 0.4872 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9504 | no |
| unknown | business2 | blend70 | 1 | potential_epc_rating_known | category | unknown | 0.4084 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.4302 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.5570 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.6126 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4812 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.3895 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.2999 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4482 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9790 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9779 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9790 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9807 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9768 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.4552 | no |
| unknown | business2 | blend70 | 1 | uprn | id | unknown | 0.5730 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9804 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.4978 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.7577 | no |
| unknown | business2 | blend70 | 1 | warddesc | address | unknown | 0.3280 | no |
| wrong | business2 | blend70 | 1 | cost centre description | account | org | 0.5507 | no |
| wrong | business2 | blend70 | 1 | fuel_poverty | rate | category | 0.5867 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.5763 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8140 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.7610 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6863 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5054 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6328 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9774 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9650 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8707 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.7751 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | quantity | 0.5462 | no |
| unknown | business2 | blend70 | 2 | # invoices paid within 5 days | quantity | unknown | 0.4787 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4976 | no |
| unknown | business2 | blend70 | 2 | conservation_area_site_id | category | unknown | 0.4697 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.6507 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.4874 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.4454 | no |
| unknown | business2 | blend70 | 2 | health service executive area | address | unknown | 0.4655 | no |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.3493 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms_known | category | unknown | 0.4976 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4965 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9590 | no |
| unknown | business2 | blend70 | 2 | potential_epc_rating_known | category | unknown | 0.4066 | no |
| unknown | business2 | blend70 | 2 | potential_epc_score_known | category | unknown | 0.6439 | no |
| unknown | business2 | blend70 | 2 | scheme_description | category | unknown | 0.4414 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.3358 | no |
| unknown | business2 | blend70 | 2 | super output area 2011 name | address | unknown | 0.4739 | no |
| unknown | business2 | blend70 | 2 | surveyname | text | unknown | 0.4363 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3368 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9781 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9743 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9762 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9799 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9737 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.6457 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.6112 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9845 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.5146 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.7384 | no |
| unknown | business2 | blend70 | 2 | warddesc | address | unknown | 0.3993 | no |
| wrong | business2 | blend70 | 2 | imd19_national_decile | category | id | 0.6899 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8418 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.9321 | no |
| wrong | business2 | blend70 | 2 | post code sector | address | id | 0.5658 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.5120 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.5494 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5661 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9765 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.5762 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9846 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9751 | yes |
| critical | business2 | ft | 1 | return-on-investments_revenus-de-placements | amount | quantity | 0.7529 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9520 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.7132 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.6887 | no |
| unknown | business2 | ft | 1 | cost centre description | account | unknown | 0.4149 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.7802 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.4995 | no |
| unknown | business2 | ft | 1 | imd19_national_decile | category | unknown | 0.4485 | no |
| unknown | business2 | ft | 1 | numbers of | date | unknown | 0.4821 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9301 | no |
| unknown | business2 | ft | 1 | potential_epc_rating_known | category | unknown | 0.4397 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.5935 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.7956 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.8751 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.3488 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5996 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9732 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9695 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9706 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9730 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9712 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.5707 | no |
| unknown | business2 | ft | 1 | uprn | id | unknown | 0.5412 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9730 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.5659 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.7516 | no |
| unknown | business2 | ft | 1 | warddesc | address | unknown | 0.4633 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.6380 | no |
| wrong | business2 | ft | 1 | cost centre description | account | org | 0.7823 | no |
| wrong | business2 | ft | 1 | fuel_poverty | rate | category | 0.8360 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.7088 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.5190 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.7377 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.6949 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8899 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.5493 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8942 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9712 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9668 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8902 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.6794 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.8525 | yes |
| unknown | business2 | ft | 2 | # invoices paid within 5 days | quantity | unknown | 0.5386 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.9127 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.3746 | no |
| unknown | business2 | ft | 2 | monitor | id | unknown | 0.3918 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.5472 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9424 | no |
| unknown | business2 | ft | 2 | potential_epc_rating_known | category | unknown | 0.4882 | no |
| unknown | business2 | ft | 2 | potential_epc_score_known | category | unknown | 0.8988 | no |
| unknown | business2 | ft | 2 | service | account | unknown | 0.4726 | no |
| unknown | business2 | ft | 2 | supplier type | category | unknown | 0.4586 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4404 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9720 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9643 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9667 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9719 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9667 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.8429 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9788 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.6679 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.7240 | no |
| wrong | business2 | ft | 2 | conservation_area_site_id | category | id | 0.5879 | no |
| wrong | business2 | ft | 2 | fuel_poverty | rate | category | 0.6341 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.5470 | no |
| wrong | business2 | ft | 2 | imd19_national_decile | category | id | 0.8237 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.7775 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.9394 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.6203 | no |
| wrong | business2 | ft | 2 | post code sector | address | id | 0.7710 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.5843 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8076 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9698 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.5529 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.7889 | yes |
| unknown | dev220 | blend50 | 1 | is a company | category | unknown | 0.4688 | no |
| unknown | dev220 | blend50 | 1 | material | product | unknown | 0.4900 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4979 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5629 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4692 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4733 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4844 | no |
| unknown | dev220 | blend50 | 1 | 商品計 | amount | unknown | 0.5632 | no |
| unknown | dev220 | blend50 | 1 | 年末調整未済 | category | unknown | 0.4873 | no |
| unknown | dev220 | blend50 | 1 | 役職名 | category | unknown | 0.4397 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.2913 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8717 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.6964 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.7619 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.6529 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5005 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.6260 | no |
| wrong | dev220 | blend50 | 1 | 発送先カナ | person | org | 0.5095 | no |
| critical | dev220 | blend50 | 2 | credit limit | amount | quantity | 0.5250 | yes |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8531 | yes |
| unknown | dev220 | blend50 | 2 | is a company | category | unknown | 0.4972 | no |
| unknown | dev220 | blend50 | 2 | material | product | unknown | 0.4908 | no |
| unknown | dev220 | blend50 | 2 | name | person | unknown | 0.4996 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4949 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5629 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4974 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4681 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4992 | no |
| unknown | dev220 | blend50 | 2 | 商品オプション | text | unknown | 0.4324 | no |
| unknown | dev220 | blend50 | 2 | 商品計 | amount | unknown | 0.4347 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.2726 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4890 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.8019 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.6889 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.6254 | no |
| wrong | dev220 | blend50 | 2 | terms | category | text | 0.5727 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7025 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.7862 | yes |
| unknown | dev220 | blend60 | 1 | is a company | category | unknown | 0.3801 | no |
| unknown | dev220 | blend60 | 1 | 商品オプション | text | unknown | 0.4241 | no |
| unknown | dev220 | blend60 | 1 | 役職名 | category | unknown | 0.3657 | no |
| unknown | dev220 | blend60 | 1 | 支出負担行為担当官 | person | unknown | 0.3433 | no |
| unknown | dev220 | blend60 | 1 | 時間帯指定 | category | unknown | 0.4780 | no |
| unknown | dev220 | blend60 | 1 | 発送先カナ | person | unknown | 0.4510 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8541 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.7480 | no |
| wrong | dev220 | blend60 | 1 | taxable | category | tax_class | 0.7211 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.7138 | no |
| wrong | dev220 | blend60 | 1 | 年末調整未済 | category | text | 0.5587 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.6541 | no |
| critical | dev220 | blend60 | 2 | credit limit | amount | quantity | 0.5293 | yes |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8633 | yes |
| unknown | dev220 | blend60 | 2 | 商品オプション | text | unknown | 0.4110 | no |
| unknown | dev220 | blend60 | 2 | 商品計 | amount | unknown | 0.4170 | no |
| unknown | dev220 | blend60 | 2 | 支出負担行為担当官 | person | unknown | 0.3114 | no |
| unknown | dev220 | blend60 | 2 | 発送先カナ | person | unknown | 0.4744 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.7704 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.7391 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.5572 | no |
| wrong | dev220 | blend60 | 2 | terms | category | text | 0.6176 | no |
| wrong | dev220 | blend60 | 2 | 年末調整未済 | category | text | 0.5146 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7458 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.7835 | yes |
| unknown | dev220 | blend70 | 1 | is a company | category | unknown | 0.4025 | no |
| unknown | dev220 | blend70 | 1 | 商品オプション | text | unknown | 0.3639 | no |
| unknown | dev220 | blend70 | 1 | 役職名 | category | unknown | 0.3430 | no |
| unknown | dev220 | blend70 | 1 | 支出負担行為担当官 | person | unknown | 0.3954 | no |
| unknown | dev220 | blend70 | 1 | 発送先カナ | person | unknown | 0.4974 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8366 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7996 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.6802 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.7748 | no |
| wrong | dev220 | blend70 | 1 | 年末調整未済 | category | text | 0.6517 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.6821 | no |
| wrong | dev220 | blend70 | 1 | 時間帯指定 | category | text | 0.5575 | no |
| critical | dev220 | blend70 | 2 | credit limit | amount | quantity | 0.5337 | yes |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8734 | yes |
| unknown | dev220 | blend70 | 2 | taxable | category | unknown | 0.4891 | no |
| unknown | dev220 | blend70 | 2 | 商品オプション | text | unknown | 0.4520 | no |
| unknown | dev220 | blend70 | 2 | 商品計 | amount | unknown | 0.3994 | no |
| unknown | dev220 | blend70 | 2 | 支出負担行為担当官 | person | unknown | 0.3503 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.7390 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7893 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.6625 | no |
| wrong | dev220 | blend70 | 2 | 年末調整未済 | category | text | 0.6003 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7892 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.7754 | yes |
| unknown | dev220 | ft | 1 | 商品オプション | text | unknown | 0.4744 | no |
| unknown | dev220 | ft | 1 | 役職名 | category | unknown | 0.4897 | no |
| unknown | dev220 | ft | 1 | 普通徴収 | category | unknown | 0.4780 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.7841 | no |
| wrong | dev220 | ft | 1 | is a company | category | text | 0.5750 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9545 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.5576 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.9576 | no |
| wrong | dev220 | ft | 1 | 年末調整未済 | category | text | 0.9306 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7662 | no |
| wrong | dev220 | ft | 1 | 時間帯指定 | category | text | 0.7963 | no |
| critical | dev220 | ft | 2 | credit limit | amount | quantity | 0.5466 | yes |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9039 | yes |
| unknown | dev220 | ft | 2 | 商品計 | amount | unknown | 0.3962 | no |
| unknown | dev220 | ft | 2 | 支出負担行為担当官 | person | unknown | 0.4667 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.6446 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9397 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.7972 | no |
| wrong | dev220 | ft | 2 | 商品オプション | text | category | 0.5748 | no |
| wrong | dev220 | ft | 2 | 年末調整未済 | category | text | 0.8572 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.9191 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | quantity | 0.6178 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.8355 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.5664 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.8884 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9611 | no |
| other_ng | general | blend50 | 1 | 被害域幅(m)最小 | other | quantity | 0.5045 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4721 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4867 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5715 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.4593 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.5718 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4929 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.4874 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.4194 | no |
| unknown | general | blend50 | 1 | standardhours | quantity | unknown | 0.3845 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2784 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.5894 | no |
| unknown | general | blend50 | 1 | 城南第2 | quantity | unknown | 0.5277 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9564 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4591 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9891 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8727 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3559 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.6431 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.9383 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.8496 | no |
| wrong | general | blend50 | 1 | indicator | text | category | 0.6808 | no |
| wrong | general | blend50 | 1 | itemfield1 | text | category | 0.5660 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.6818 | no |
| wrong | general | blend50 | 1 | lda | text | category | 0.6965 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9124 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.5472 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7427 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.7947 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.7852 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | quantity | 0.5413 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.8113 | no |
| other_ng | general | blend50 | 2 | episode | other | id | 0.8262 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5864 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.5108 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8610 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9721 | no |
| other_ng | general | blend50 | 2 | 被害域幅(m)最小 | other | quantity | 0.5033 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.4857 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.3750 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5338 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.4995 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.7822 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4929 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4910 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4742 | no |
| unknown | general | blend50 | 2 | standardhours | quantity | unknown | 0.4060 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4424 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4579 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9556 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4437 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9878 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9371 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.8105 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.9568 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8265 | no |
| wrong | general | blend50 | 2 | indicator | text | category | 0.5991 | no |
| wrong | general | blend50 | 2 | itemfield1 | text | category | 0.5153 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.7160 | no |
| wrong | general | blend50 | 2 | lda | text | category | 0.6723 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.9333 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.6642 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.7387 | no |
| wrong | general | blend50 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.6981 | no |
| wrong | general | blend50 | 2 | 読み方 | address | org | 0.5566 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | quantity | 0.5634 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.8195 | no |
| other_ng | general | blend60 | 1 | operationid | other | id | 0.5290 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9005 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9535 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6369 | no |
| unknown | general | blend60 | 1 | female_frequency | rate | unknown | 0.4488 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.5085 | no |
| unknown | general | blend60 | 1 | pir_sha | id | unknown | 0.5794 | no |
| unknown | general | blend60 | 1 | raw | category | unknown | 0.4662 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5027 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4210 | no |
| unknown | general | blend60 | 1 | standardhours | quantity | unknown | 0.4352 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3278 | no |
| unknown | general | blend60 | 1 | 城南第2 | quantity | unknown | 0.5503 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9605 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4390 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9869 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8582 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.4262 | no |
| wrong | general | blend60 | 1 | author | person | org | 0.5786 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.9288 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.8523 | no |
| wrong | general | blend60 | 1 | indicator | text | category | 0.6593 | no |
| wrong | general | blend60 | 1 | itemfield1 | text | category | 0.5432 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.6651 | no |
| wrong | general | blend60 | 1 | lda | text | category | 0.7362 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9043 | no |
| wrong | general | blend60 | 1 | source_value | category | text | 0.5000 | no |
| wrong | general | blend60 | 1 | term | text | category | 0.5858 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7283 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.7970 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5067 | no |
| wrong | general | blend60 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.7592 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.7904 | no |
| other_ng | general | blend60 | 2 | episode | other | id | 0.8023 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.5335 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.5975 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8677 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9667 | no |
| unknown | general | blend60 | 2 | authors | person | unknown | 0.4262 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.5917 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.4850 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.7611 | no |
| unknown | general | blend60 | 2 | itemfield1 | text | unknown | 0.4823 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5726 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4246 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.3475 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.5009 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4857 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9595 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9854 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9354 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.7796 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.9509 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.8247 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.5614 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.7063 | no |
| wrong | general | blend60 | 2 | lda | text | category | 0.7071 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.9293 | no |
| wrong | general | blend60 | 2 | term | text | category | 0.5582 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6341 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7298 | no |
| wrong | general | blend60 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.6547 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5033 | no |
| wrong | general | blend60 | 2 | 読み方 | address | org | 0.6021 | no |
| critical | general | blend70 | 1 | 城南第2 | quantity | amount | 0.6419 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | quantity | 0.5090 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.8034 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.5319 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.6043 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9126 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9459 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7023 | no |
| unknown | general | blend70 | 1 | female_frequency | rate | unknown | 0.4749 | no |
| unknown | general | blend70 | 1 | pir_sha | id | unknown | 0.6714 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5847 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.4802 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.4932 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3772 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9646 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9847 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8436 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.4966 | no |
| wrong | general | blend70 | 1 | author | person | org | 0.5141 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.9192 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.8551 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.6379 | no |
| wrong | general | blend70 | 1 | itemfield1 | text | category | 0.5203 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.6485 | no |
| wrong | general | blend70 | 1 | lda | text | category | 0.7758 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8961 | no |
| wrong | general | blend70 | 1 | source_value | category | text | 0.5821 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6832 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.7138 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.7994 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.5873 | no |
| wrong | general | blend70 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.7332 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.5120 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.7696 | no |
| other_ng | general | blend70 | 2 | episode | other | id | 0.7785 | no |
| other_ng | general | blend70 | 2 | nodes | other | category | 0.5100 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6842 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8743 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9613 | no |
| unknown | general | blend70 | 2 | authors | person | unknown | 0.4774 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.6496 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.4706 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.7399 | no |
| unknown | general | blend70 | 2 | itemfield1 | text | unknown | 0.4982 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6663 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.4327 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.3971 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.3258 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.5594 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.5304 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9635 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9829 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9337 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.7486 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.9450 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.8228 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.5236 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.6965 | no |
| wrong | general | blend70 | 2 | lda | text | category | 0.7419 | no |
| wrong | general | blend70 | 2 | organization name | org | person | 0.5105 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.9253 | no |
| wrong | general | blend70 | 2 | term | text | category | 0.6511 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6039 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7209 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.5171 | no |
| wrong | general | blend70 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.6114 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.5870 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.6475 | no |
| critical | general | ft | 1 | 城南第2 | quantity | amount | 0.9169 | yes |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.7554 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.7527 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.8302 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9491 | no |
| other_ng | general | ft | 1 | ブロモホルム | other | category | 0.7140 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9230 | no |
| unknown | general | ft | 1 | author | person | unknown | 0.4911 | no |
| unknown | general | ft | 1 | cluster | category | unknown | 0.4562 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.4775 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.8986 | no |
| unknown | general | ft | 1 | female_frequency | rate | unknown | 0.5534 | no |
| unknown | general | ft | 1 | funding | amount | unknown | 0.5761 | no |
| unknown | general | ft | 1 | pir_sha | id | unknown | 0.9474 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.8310 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4624 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.6577 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.6671 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9768 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9782 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.7999 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.8905 | no |
| wrong | general | ft | 1 | goal | id | category | 0.8633 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.5737 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.5986 | no |
| wrong | general | ft | 1 | lda | text | category | 0.8948 | no |
| wrong | general | ft | 1 | place | org | address | 0.8715 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.8285 | no |
| wrong | general | ft | 1 | term | text | category | 0.9755 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.6705 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.8064 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.8294 | no |
| wrong | general | ft | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.6553 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.7310 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.7070 | no |
| other_ng | general | ft | 2 | episode | other | id | 0.7069 | no |
| other_ng | general | ft | 2 | genre_pop | other | rate | 0.5680 | no |
| other_ng | general | ft | 2 | nodes | other | category | 0.6329 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9443 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.8943 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9450 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.8233 | no |
| unknown | general | ft | 2 | female_frequency | rate | unknown | 0.4273 | no |
| unknown | general | ft | 2 | funding | amount | unknown | 0.5852 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.6763 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9475 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.4573 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.5199 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4235 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.7350 | no |
| unknown | general | ft | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | unknown | 0.4812 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9752 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9756 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9287 | no |
| unknown | general | ft | 2 | 駐車場 | category | unknown | 0.6473 | no |
| wrong | general | ft | 2 | author | person | org | 0.6556 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.9273 | no |
| wrong | general | ft | 2 | goal | id | category | 0.8172 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.6671 | no |
| wrong | general | ft | 2 | lda | text | category | 0.8464 | no |
| wrong | general | ft | 2 | organization name | org | person | 0.7290 | no |
| wrong | general | ft | 2 | place | org | address | 0.9133 | no |
| wrong | general | ft | 2 | term | text | category | 0.9296 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.5135 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6943 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.7291 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.8380 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.7840 | no |
| unknown | japan_procurement | blend50 | 1 | 20,000,000円以上50,000,000円未満金額(円) | amount | unknown | 0.5618 | no |
| unknown | japan_procurement | blend50 | 1 | 50,000,000円以上150,000,000円未満金額(円) | amount | unknown | 0.5714 | no |
| unknown | japan_procurement | blend60 | 1 | 20,000,000円以上50,000,000円未満金額(円) | amount | unknown | 0.4744 | no |
| unknown | japan_procurement | blend60 | 1 | 50,000,000円以上150,000,000円未満金額(円) | amount | unknown | 0.4858 | no |
| unknown | japan_procurement | blend70 | 1 | 2,000,000円以上5,000,000円未満金額(円) | amount | unknown | 0.6120 | no |
| unknown | japan_procurement | blend70 | 1 | 20,000,000円以上50,000,000円未満金額(円) | amount | unknown | 0.5479 | no |
| unknown | japan_procurement | blend70 | 1 | 5,000,000円以上20,000,000円未満金額(円) | amount | unknown | 0.5622 | no |
| unknown | japan_procurement | blend70 | 1 | 50,000,000円以上150,000,000円未満金額(円) | amount | unknown | 0.5639 | no |
| critical | japan_procurement | ft | 1 | 20,000,000円以上50,000,000円未満金額(円) | amount | quantity | 0.7823 | yes |
| critical | japan_procurement | ft | 1 | 50,000,000円以上150,000,000円未満金額(円) | amount | quantity | 0.8052 | yes |
| unknown | japan_procurement | ft | 1 | 2,000,000円以上5,000,000円未満金額(円) | amount | unknown | 0.5196 | no |
| unknown | japan_procurement | ft | 1 | 5,000,000円以上20,000,000円未満金額(円) | amount | unknown | 0.5935 | no |

### unknown の判定理由

- date_value_evidence_low: 75件
- numeric_top2_too_close: 58件
- numeric_values_not_parseable: 18件
- other_class: 82件
- probability_below_threshold: 280件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 61件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 199件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 91件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
