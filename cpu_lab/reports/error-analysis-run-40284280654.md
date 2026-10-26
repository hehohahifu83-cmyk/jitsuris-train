# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-26T08:53:04+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 8 | 1 | 18 | 0 |
| business | blend50 | 2 | 490 | 9 | 1 | 13 | 0 |
| business | blend60 | 1 | 490 | 10 | 1 | 9 | 0 |
| business | blend60 | 2 | 490 | 9 | 1 | 10 | 0 |
| business | blend70 | 1 | 490 | 10 | 1 | 8 | 0 |
| business | blend70 | 2 | 490 | 10 | 1 | 8 | 0 |
| business | ft | 1 | 490 | 10 | 0 | 6 | 1 |
| business | ft | 2 | 490 | 11 | 2 | 7 | 0 |
| business2 | blend50 | 1 | 976 | 16 | 3 | 24 | 2 |
| business2 | blend50 | 2 | 976 | 13 | 3 | 27 | 1 |
| business2 | blend60 | 1 | 976 | 15 | 3 | 19 | 1 |
| business2 | blend60 | 2 | 976 | 14 | 4 | 20 | 0 |
| business2 | blend70 | 1 | 976 | 17 | 2 | 17 | 1 |
| business2 | blend70 | 2 | 976 | 14 | 4 | 17 | 0 |
| business2 | ft | 1 | 976 | 18 | 3 | 15 | 1 |
| business2 | ft | 2 | 976 | 16 | 4 | 15 | 1 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 7 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 6 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 0 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 5 | 1 | 1 | 0 |
| general | blend50 | 1 | 383 | 10 | 0 | 15 | 6 |
| general | blend50 | 2 | 383 | 7 | 0 | 18 | 5 |
| general | blend60 | 1 | 383 | 8 | 0 | 15 | 6 |
| general | blend60 | 2 | 383 | 11 | 0 | 15 | 6 |
| general | blend70 | 1 | 383 | 10 | 0 | 12 | 6 |
| general | blend70 | 2 | 383 | 13 | 0 | 12 | 7 |
| general | ft | 1 | 383 | 10 | 0 | 13 | 8 |
| general | ft | 2 | 383 | 14 | 1 | 11 | 5 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 8, quantity→amount: 2, text→category: 2, text→account: 2, account→category: 2, category→text: 1
- business / blend60: org→account: 7, account→category: 3, quantity→amount: 2, text→category: 2, text→account: 2, category→id: 2, category→text: 1
- business / blend70: org→account: 8, account→category: 3, quantity→amount: 2, text→category: 2, text→account: 2, category→id: 2, category→text: 1
- business / ft: org→account: 7, account→category: 4, category→id: 4, text→category: 2, text→account: 2, quantity→amount: 1, amount→quantity: 1
- business2 / blend50: account→category: 4, category→id: 4, amount→quantity: 4, address→category: 3, id→address: 3, id→category: 2, quantity→amount: 2, quantity→category: 2
- business2 / blend60: amount→quantity: 5, category→id: 4, account→category: 3, address→category: 3, id→address: 3, id→category: 2, quantity→amount: 2, quantity→category: 2
- business2 / blend70: amount→quantity: 5, category→id: 4, account→category: 3, address→category: 3, quantity→category: 3, id→address: 3, id→category: 2, category→quantity: 2
- business2 / ft: category→id: 4, amount→quantity: 4, id→category: 3, address→category: 3, quantity→category: 3, category→quantity: 3, account→category: 2, quantity→amount: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, id→quantity: 2, category→tax_class: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2
- dev220 / ft: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, address→id: 1
- general / blend50: org→address: 4, category→text: 3, text→category: 3, person→org: 2, quantity→category: 2, id→category: 2, address→org: 1
- general / blend60: category→text: 5, org→address: 4, quantity→category: 2, address→org: 2, id→category: 2, text→category: 2, person→org: 1, id→address: 1
- general / blend70: category→text: 7, org→address: 4, quantity→category: 2, address→org: 2, text→account: 2, id→category: 2, text→category: 2, id→text: 1
- general / ft: category→text: 7, org→address: 4, address→org: 2, text→account: 2, text→category: 2, quantity→category: 1, id→category: 1, category→org: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `type de matériel`、category→id（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `monitor`、id→category（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `situtation`、address→category（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `随意契約理由`、text→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `随意契約理由`、text→category（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `随意契約理由`、text→category（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `indicator`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `indicator`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend60: `読み方`、address→org（seed 1, seed 2）
- general / blend70: `cleaned`、text→account（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `indicator`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `source`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `読み方`、address→org（seed 1, seed 2）
- general / ft: `cleaned`、text→account（seed 1, seed 2）
- general / ft: `indicator`、text→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `source`、category→text（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `読み方`、address→org（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.7634 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5980 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5968 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5480 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.4244 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5225 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4899 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.5616 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5299 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4642 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5558 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4812 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6021 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4581 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4771 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9763 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4985 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9756 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9225 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9683 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.8309 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9850 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.7397 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5258 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8766 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.5873 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.8919 | yes |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.6119 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.3311 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5396 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4287 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.6048 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4857 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.5445 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4457 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4422 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9651 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4483 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9321 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7810 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9641 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.5518 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9785 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7037 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5784 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5282 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9656 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5457 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.7164 | yes |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.4357 | no |
| unknown | business | blend60 | 1 | ligne | category | unknown | 0.4437 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6792 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5224 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4886 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3983 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9788 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9765 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9334 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9633 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8368 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9829 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5003 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.7802 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8569 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5851 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.5596 | no |
| wrong | business | blend60 | 1 | type de matériel | category | id | 0.5028 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.8708 | yes |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.3614 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4739 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4319 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6321 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.3572 | no |
| unknown | business | blend60 | 2 | overseas sourced services | amount | unknown | 0.5596 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9698 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.3948 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9285 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.7890 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9580 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9762 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5482 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7535 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.5577 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6024 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9650 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6074 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.6694 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4989 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.4839 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7563 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4513 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4645 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9812 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9775 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9444 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9583 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8427 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9808 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5836 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.8208 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.8372 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6717 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.5319 | no |
| wrong | business | blend70 | 1 | type de matériel | category | id | 0.5822 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.8498 | yes |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.3916 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7196 | no |
| unknown | business | blend70 | 2 | overseas sourced goods | amount | unknown | 0.3496 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.5098 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9745 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.3883 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9248 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.7969 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9518 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9739 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.5039 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6379 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.8034 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.5369 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.6766 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9643 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.6690 | no |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.5110 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9875 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9884 | no |
| unknown | business | ft | 1 | title | category | unknown | 0.4488 | no |
| unknown | business | ft | 1 | total invoices paid | quantity | unknown | 0.5285 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9804 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9771 | no |
| wrong | business | ft | 1 | department | org | account | 0.9432 | no |
| wrong | business | ft | 1 | department | org | account | 0.8605 | no |
| wrong | business | ft | 1 | department | org | account | 0.9744 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.8336 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.6683 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9424 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.5783 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.7780 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9315 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.8205 | no |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.6189 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.7868 | yes |
| unknown | business | ft | 2 | australian sourced goods | amount | unknown | 0.4920 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9823 | no |
| unknown | business | ft | 2 | overseas sourced goods | amount | unknown | 0.4993 | no |
| unknown | business | ft | 2 | portefeuille_nom_et_code | org | unknown | 0.4748 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9885 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9139 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8208 | no |
| wrong | business | ft | 2 | department | org | account | 0.9335 | no |
| wrong | business | ft | 2 | department | org | account | 0.9670 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.7198 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.9071 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9529 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.8992 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9625 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.8540 | no |
| wrong | business | ft | 2 | type de matériel | category | id | 0.5174 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9319 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7584 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.7076 | yes |
| other_ng | business2 | blend50 | 1 | average bids per property | other | quantity | 0.6864 | no |
| other_ng | business2 | blend50 | 1 | d2 floorspace net sqm | other | amount | 0.5080 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5979 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5970 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4645 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4061 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3229 | no |
| unknown | business2 | blend50 | 1 | health service executive area | address | unknown | 0.4694 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4885 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9848 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5943 | no |
| unknown | business2 | blend50 | 1 | scheme_description | category | unknown | 0.4861 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4534 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4048 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3033 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4397 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9924 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.5577 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5417 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4954 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.4953 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9918 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.6824 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7273 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.8889 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5984 | no |
| wrong | business2 | blend50 | 1 | numéro | id | address | 0.6231 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.8358 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.8523 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.8257 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.5457 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.7276 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9642 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.5767 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7638 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9692 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9105 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.8702 | yes |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5135 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3979 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4620 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.3740 | no |
| unknown | business2 | blend50 | 2 | merchant description | category | unknown | 0.5000 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4733 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5144 | no |
| unknown | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5857 | no |
| unknown | business2 | blend50 | 2 | scheme_description | category | unknown | 0.4966 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4124 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4967 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4607 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3256 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4892 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4911 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9933 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9935 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9924 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.3894 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4913 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.5015 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5092 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9917 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.6896 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4085 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5169 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5815 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.8653 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.6090 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5276 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6225 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.6596 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5771 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.9076 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9620 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9432 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7250 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.6495 | yes |
| other_ng | business2 | blend60 | 1 | average bids per property | other | quantity | 0.6908 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4192 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.3810 | no |
| unknown | business2 | blend60 | 1 | health service executive area | address | unknown | 0.4984 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9824 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4276 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4244 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4653 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3555 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3537 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.5960 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5353 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5931 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.5906 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9914 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.7259 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6755 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.8742 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6676 | no |
| wrong | business2 | blend60 | 1 | numéro | id | address | 0.5978 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.8633 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8717 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8506 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.7081 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9633 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.5552 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.7623 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9739 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9247 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6619 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.8449 | yes |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4518 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4368 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3020 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9836 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5197 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4304 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3256 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5825 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5840 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.4220 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5985 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6038 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9912 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.6823 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4558 | no |
| wrong | business2 | blend60 | 2 | contravention | category | text | 0.5813 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6568 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.8413 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5364 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6157 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6454 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.6860 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.6196 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.8973 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9641 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9545 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6916 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | quantity | 0.6952 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4322 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4411 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.4946 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9800 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4910 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.4949 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4077 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3642 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5913 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.6343 | no |
| unknown | business2 | blend70 | 1 | total_verified_sales | quantity | unknown | 0.6194 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9910 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.5274 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.7695 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6237 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.8594 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7368 | no |
| wrong | business2 | blend70 | 1 | numéro | id | address | 0.5725 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.8908 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8910 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8756 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.6887 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9623 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.5337 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish & band a | quantity | category | 0.5251 | no |
| wrong | business2 | blend70 | 1 | want to live in this parish only | quantity | category | 0.5345 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.7608 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9785 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9389 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7380 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.8196 | yes |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4117 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.2872 | no |
| unknown | business2 | blend70 | 2 | habitatcode | id | unknown | 0.4689 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5250 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9814 | no |
| unknown | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5674 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3713 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6757 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6769 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.4546 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9907 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.6750 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.6457 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7320 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8173 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7037 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.6683 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7124 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6620 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5009 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.8870 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9661 | no |
| critical | business2 | ft | 1 | fine | amount | rate | 0.6216 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9885 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.8717 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | quantity | 0.7085 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.4713 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.6737 | no |
| unknown | business2 | ft | 1 | imd19_income_decile | category | unknown | 0.4798 | no |
| unknown | business2 | ft | 1 | numéro | id | unknown | 0.4967 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9729 | no |
| unknown | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5912 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5642 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9853 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9856 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9865 | no |
| unknown | business2 | ft | 1 | total invoices paid | quantity | unknown | 0.5693 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.7491 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9898 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.6143 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.9002 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8151 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9443 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.9732 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9489 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9505 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.7067 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.6303 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5184 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9595 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band a | quantity | category | 0.7500 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.7627 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.7564 | no |
| wrong | business2 | ft | 1 | état | category | account | 0.6252 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9923 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.9816 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9666 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.7436 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | amount | 0.7155 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.3361 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.3813 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7391 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9746 | no |
| unknown | business2 | ft | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.5547 | no |
| unknown | business2 | ft | 2 | scheme | id | unknown | 0.4163 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.9555 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.9557 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9891 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.6531 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.8388 | no |
| wrong | business2 | ft | 2 | habitatcode | id | category | 0.5029 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9577 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.7452 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9678 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.7370 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7916 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.7893 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.7121 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.8559 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.5523 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9721 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.7827 | yes |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5676 | no |
| unknown | dev220 | blend50 | 1 | ポイント | amount | unknown | 0.4785 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4955 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4863 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4912 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4829 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4740 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9382 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.6904 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5239 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.6555 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8619 | yes |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4904 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4962 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4981 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4988 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4878 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4917 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9593 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8647 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.6034 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.7973 | yes |
| unknown | dev220 | blend60 | 1 | ポイント | amount | unknown | 0.4569 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9465 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.7475 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7133 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5179 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8861 | yes |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9631 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.8874 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.6601 | no |
| wrong | dev220 | blend60 | 2 | 随意契約理由 | text | category | 0.5459 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8119 | yes |
| unknown | dev220 | blend70 | 1 | ポイント | amount | unknown | 0.4963 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9548 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.8046 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7711 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.5938 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9103 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9669 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9102 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7168 | no |
| wrong | dev220 | blend70 | 2 | 随意契約理由 | text | category | 0.6135 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.8558 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9796 | no |
| wrong | dev220 | ft | 1 | shipping address | address | id | 0.6809 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9760 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9444 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.8215 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9828 | yes |
| unknown | dev220 | ft | 2 | terms | category | unknown | 0.4955 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9783 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9784 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8868 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.8164 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.6785 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.7426 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5210 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9555 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9704 | no |
| other_ng | general | blend50 | 1 | 被害域幅(m)最小 | other | quantity | 0.5024 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.5386 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6218 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.5712 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8455 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4830 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4163 | no |
| unknown | general | blend50 | 1 | source | category | unknown | 0.4261 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2596 | no |
| unknown | general | blend50 | 1 | データセット_キーワード | category | unknown | 0.4992 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.5013 | no |
| unknown | general | blend50 | 1 | 日本語教室名 | org | unknown | 0.4988 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9721 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4295 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9936 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9510 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5582 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5244 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.6436 | no |
| wrong | general | blend50 | 1 | indicator | text | category | 0.9011 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9072 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8209 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.5028 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.6889 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.8872 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5916 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | quantity | 0.9120 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.6236 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.7227 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9048 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9448 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4599 | no |
| unknown | general | blend50 | 2 | cleaned | text | unknown | 0.4732 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4495 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5546 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.4772 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9435 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4879 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4105 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4493 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4782 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.2727 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4829 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4935 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9863 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4508 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9940 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8685 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4566 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.6240 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5812 | no |
| wrong | general | blend50 | 2 | indicator | text | category | 0.5077 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.8859 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8251 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5666 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8555 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.5711 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.6520 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.7116 | no |
| other_ng | general | blend60 | 1 | mood | other | category | 0.5702 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9556 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9646 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4733 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4773 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.6211 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6953 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.8713 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4931 | no |
| unknown | general | blend60 | 1 | raw | category | unknown | 0.4273 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5646 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4939 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3103 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5855 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9755 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3472 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9923 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9556 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.6500 | no |
| wrong | general | blend60 | 1 | indicator | text | category | 0.9076 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9097 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.7944 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.6891 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.9013 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5947 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.6106 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.5516 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | quantity | 0.9026 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.5904 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.6767 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8995 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9338 | no |
| unknown | general | blend60 | 2 | bib | id | unknown | 0.4798 | no |
| unknown | general | blend60 | 2 | cleaned | text | unknown | 0.4888 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.4609 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6415 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.4743 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9518 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.3313 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4966 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5894 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4384 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.2641 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.5714 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9867 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9928 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8684 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.5591 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5522 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.5067 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.8678 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8043 | no |
| wrong | general | blend60 | 2 | source | category | text | 0.5454 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.5374 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.8370 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5716 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5407 | no |
| wrong | general | blend60 | 2 | 読み方 | address | org | 0.5258 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6448 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6255 | no |
| other_ng | general | blend70 | 1 | episode | other | id | 0.6806 | no |
| other_ng | general | blend70 | 1 | mood | other | category | 0.6610 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9557 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9588 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.7036 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7687 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.8971 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.5699 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.4932 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6575 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4853 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3611 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9788 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.3973 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9910 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9601 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.5547 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.6565 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.9142 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9122 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7678 | no |
| wrong | general | blend70 | 1 | source | category | text | 0.5671 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6893 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.9155 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6926 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.6297 | no |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.6314 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | quantity | 0.8932 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.5572 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.5942 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.6308 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8941 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9228 | no |
| unknown | general | blend70 | 2 | author | person | unknown | 0.4941 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.5255 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7284 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.4715 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9601 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.3275 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6846 | no |
| unknown | general | blend70 | 2 | source | category | unknown | 0.4767 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.3041 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9872 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9916 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8682 | no |
| wrong | general | blend70 | 2 | bib | id | text | 0.5597 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.5630 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.5232 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.5056 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.8498 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7835 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.6205 | no |
| wrong | general | blend70 | 2 | source_value | category | text | 0.5091 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.5081 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.8185 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6634 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6307 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.5951 | no |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.5505 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8659 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.5459 | no |
| other_ng | general | ft | 1 | episode | other | id | 0.5877 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.9334 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.7064 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9559 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9416 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.5985 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9511 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9891 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9745 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8003 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9362 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4467 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3916 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4879 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4816 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9888 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9871 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9738 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.7868 | no |
| wrong | general | ft | 1 | goal | id | category | 0.6758 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.9338 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9198 | no |
| wrong | general | ft | 1 | place | org | address | 0.6882 | no |
| wrong | general | ft | 1 | source | category | text | 0.7868 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.6898 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9579 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9861 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.6868 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.5196 | yes |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.8707 | no |
| other_ng | general | ft | 2 | dag-stage | other | quantity | 0.8650 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8488 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.8782 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.8899 | no |
| unknown | general | ft | 2 | cause_of_invalid_ranking | text | unknown | 0.4763 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.7194 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9890 | no |
| unknown | general | ft | 2 | female_frequency | rate | unknown | 0.4629 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9850 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.4668 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9702 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.4241 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9885 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9880 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.8677 | no |
| wrong | general | ft | 2 | bib | id | text | 0.7994 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.7855 | no |
| wrong | general | ft | 2 | domain | category | id | 0.5648 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.5024 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.7957 | no |
| wrong | general | ft | 2 | place | org | address | 0.7212 | no |
| wrong | general | ft | 2 | source | category | org | 0.5966 | no |
| wrong | general | ft | 2 | source | category | text | 0.8458 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.7213 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.7631 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.9388 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9006 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.8027 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 39件
- numeric_values_not_parseable: 18件
- other_class: 71件
- probability_below_threshold: 160件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 43件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 174件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 110件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
