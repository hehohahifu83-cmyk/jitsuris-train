# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-25T15:38:31+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 8 | 1 | 15 | 0 |
| business | blend50 | 2 | 490 | 9 | 1 | 14 | 0 |
| business | blend60 | 1 | 490 | 6 | 0 | 13 | 0 |
| business | blend60 | 2 | 490 | 10 | 1 | 10 | 0 |
| business | blend70 | 1 | 490 | 8 | 0 | 10 | 0 |
| business | blend70 | 2 | 490 | 13 | 1 | 6 | 0 |
| business | ft | 1 | 490 | 11 | 0 | 6 | 0 |
| business | ft | 2 | 490 | 15 | 1 | 6 | 1 |
| business2 | blend50 | 1 | 976 | 12 | 2 | 27 | 2 |
| business2 | blend50 | 2 | 976 | 12 | 3 | 28 | 1 |
| business2 | blend60 | 1 | 976 | 13 | 2 | 23 | 1 |
| business2 | blend60 | 2 | 976 | 16 | 3 | 21 | 1 |
| business2 | blend70 | 1 | 976 | 15 | 3 | 20 | 1 |
| business2 | blend70 | 2 | 976 | 17 | 4 | 16 | 1 |
| business2 | ft | 1 | 976 | 19 | 4 | 13 | 2 |
| business2 | ft | 2 | 976 | 17 | 3 | 16 | 2 |
| dev220 | blend50 | 1 | 220 | 4 | 1 | 8 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 2 | 8 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 2 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 2 | 1 | 0 |
| dev220 | ft | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 6 | 3 | 2 | 0 |
| general | blend50 | 1 | 383 | 8 | 0 | 14 | 6 |
| general | blend50 | 2 | 383 | 8 | 0 | 17 | 6 |
| general | blend60 | 1 | 383 | 7 | 0 | 13 | 4 |
| general | blend60 | 2 | 383 | 11 | 0 | 14 | 6 |
| general | blend70 | 1 | 383 | 10 | 1 | 10 | 4 |
| general | blend70 | 2 | 383 | 11 | 0 | 13 | 5 |
| general | ft | 1 | 383 | 10 | 1 | 9 | 4 |
| general | ft | 2 | 383 | 14 | 1 | 9 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, quantity→amount: 2, text→category: 2, text→account: 2, category→text: 2, category→id: 1, account→category: 1
- business / blend60: org→account: 7, text→category: 2, text→account: 2, category→id: 1, quantity→amount: 1, account→text: 1, account→category: 1, category→text: 1
- business / blend70: org→account: 8, text→category: 2, text→account: 2, account→category: 2, category→id: 2, category→text: 2, account→org: 1, quantity→amount: 1
- business / ft: org→account: 8, text→category: 2, text→account: 2, account→category: 2, category→id: 2, category→text: 2, org→address: 1, org→category: 1
- business2 / blend50: account→category: 4, amount→quantity: 4, category→id: 3, id→address: 3, id→category: 2, address→category: 2, category→quantity: 2, org→address: 2
- business2 / blend60: category→id: 4, amount→quantity: 4, account→category: 3, id→address: 3, id→category: 2, category→quantity: 2, category→address: 2, address→text: 2
- business2 / blend70: category→id: 4, account→category: 3, quantity→amount: 3, amount→quantity: 3, id→category: 2, category→quantity: 2, category→address: 2, address→text: 2
- business2 / ft: category→id: 4, account→category: 3, quantity→category: 3, account→org: 3, amount→quantity: 3, id→category: 2, amount→rate: 2, category→date: 2
- dev220 / blend50: quantity→category: 4, id→quantity: 2, org→account: 1, text→category: 1, amount→quantity: 1
- dev220 / blend60: quantity→category: 4, id→quantity: 2, org→account: 1, text→category: 1, amount→quantity: 1
- dev220 / blend70: quantity→category: 4, id→quantity: 2, org→account: 1, text→category: 1, rate→tax_class: 1, amount→quantity: 1
- dev220 / ft: quantity→category: 4, id→quantity: 2, amount→quantity: 2, org→account: 1, text→category: 1, rate→tax_class: 1
- general / blend50: org→address: 4, text→category: 4, person→org: 2, category→text: 2, quantity→category: 2, address→org: 1, id→category: 1
- general / blend60: category→text: 5, org→address: 4, text→category: 3, quantity→category: 2, address→org: 1, person→org: 1, category→org: 1, id→category: 1
- general / blend70: category→text: 6, org→address: 4, text→category: 3, quantity→category: 2, address→org: 1, text→account: 1, id→quantity: 1, person→org: 1
- general / ft: category→text: 6, org→address: 4, text→category: 3, quantity→category: 2, address→org: 1, text→account: 1, id→quantity: 1, person→org: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `ligne`、category→id（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `monitor`、id→category（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `situtation`、address→text（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `situtation`、address→text（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / ft: `fine`、amount→rate（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `indicator`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `indicator`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `indicator`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `source`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `indicator`、text→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `source`、category→text（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.6363 | yes |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.5648 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.6105 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4563 | no |
| unknown | business | blend50 | 1 | d6 | category | unknown | 0.4859 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.6111 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4654 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6368 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5780 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4989 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4613 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4725 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9690 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3983 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9434 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8593 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9835 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.8209 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9865 | no |
| wrong | business | blend50 | 1 | ligne | category | id | 0.5132 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.6577 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9610 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.5020 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.8291 | yes |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.5232 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5770 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.3204 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.6114 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4741 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4886 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6386 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5728 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4528 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4719 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9682 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3554 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9612 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8586 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9311 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.6632 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9782 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.6624 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.6914 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.6161 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9120 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.6242 | no |
| unknown | business | blend60 | 1 | d1 | category | unknown | 0.4627 | no |
| unknown | business | blend60 | 1 | d6 | category | unknown | 0.4956 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.3753 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7056 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5910 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4290 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3850 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9718 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.4557 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4666 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5642 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9404 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8765 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9820 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8214 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9858 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.6074 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.7198 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9646 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.7955 | yes |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3484 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4639 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.4947 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.7077 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5116 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4696 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9708 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.3234 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9617 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8757 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9190 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.6321 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9759 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.5310 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7254 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.7051 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.6764 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9058 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.6132 | no |
| unknown | business | blend70 | 1 | d1 | category | unknown | 0.4897 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4218 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7744 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3966 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4436 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9745 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.4311 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.4973 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9373 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8938 | no |
| wrong | business | blend70 | 1 | account_name | account | org | 0.5071 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9804 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8219 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9851 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.7017 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.7818 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9682 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.5131 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.7620 | yes |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3764 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7769 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9734 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.3450 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9622 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8928 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9069 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.6011 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9736 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.5991 | no |
| wrong | business | blend70 | 2 | dispute-status_statut-de-différend-fra | category | text | 0.5705 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.5412 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.5702 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.7884 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.7187 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.7367 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8995 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.6022 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9807 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9827 | no |
| unknown | business | ft | 1 | title | category | unknown | 0.3258 | no |
| unknown | business | ft | 1 | type de matériel | category | unknown | 0.4526 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9282 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9454 | no |
| wrong | business | ft | 1 | account_name | account | org | 0.6752 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.6947 | no |
| wrong | business | ft | 1 | department | org | account | 0.9757 | no |
| wrong | business | ft | 1 | department | org | account | 0.8235 | no |
| wrong | business | ft | 1 | department | org | account | 0.9831 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.5668 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9845 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9681 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.6191 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9790 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.6853 | no |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.6613 | yes |
| other_ng | business | ft | 2 | km budgété | other | quantity | 0.5092 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4603 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9843 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9812 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.4183 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9638 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9441 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.5046 | no |
| wrong | business | ft | 2 | department | org | account | 0.8707 | no |
| wrong | business | ft | 2 | department | org | account | 0.5079 | no |
| wrong | business | ft | 2 | department | org | account | 0.9666 | no |
| wrong | business | ft | 2 | description | account | text | 0.8034 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.8150 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.7730 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.7965 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9774 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.7597 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.9176 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8809 | no |
| wrong | business | ft | 2 | title | category | text | 0.5692 | no |
| wrong | business | ft | 2 | tournée | id | category | 0.5272 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9677 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8300 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5203 | no |
| other_ng | business2 | blend50 | 1 | energy_consumption | other | quantity | 0.5113 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.4040 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3405 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3897 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5770 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4784 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4879 | no |
| unknown | business2 | blend50 | 1 | scheme_description | category | unknown | 0.4678 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4557 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4858 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4845 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4621 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.3927 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4877 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4927 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.6123 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4729 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5208 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4933 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5135 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.5827 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5236 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7129 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.9088 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5418 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.7099 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.5780 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.5299 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5342 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9785 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.6614 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9663 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6607 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.8035 | yes |
| other_ng | business2 | blend50 | 2 | energy_consumption | other | quantity | 0.5082 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.4319 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.3692 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4360 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.4900 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5722 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms | quantity | unknown | 0.4986 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4727 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9879 | no |
| unknown | business2 | blend50 | 2 | scheme_description | category | unknown | 0.4716 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4533 | no |
| unknown | business2 | blend50 | 2 | situtation | address | unknown | 0.4920 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4941 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4832 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4585 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3907 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.2548 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4224 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9868 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.4768 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5097 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4963 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5063 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9897 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.6381 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5884 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7336 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5891 | no |
| wrong | business2 | blend50 | 2 | numéro | id | address | 0.5493 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6673 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.7173 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5969 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7332 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9763 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9726 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8318 | yes |
| other_ng | business2 | blend60 | 1 | energy_consumption | other | quantity | 0.5736 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.4705 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4001 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.3850 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.5288 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9834 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4828 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3910 | no |
| unknown | business2 | blend60 | 1 | service_responsable | account | unknown | 0.4857 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4041 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5761 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5768 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5354 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.5126 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5609 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5895 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6076 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.5481 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5546 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5785 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6563 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.9046 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6058 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.7398 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5973 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.5374 | no |
| wrong | business2 | blend60 | 1 | situtation | address | text | 0.5184 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9773 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.6426 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9709 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6286 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.7648 | yes |
| other_ng | business2 | blend60 | 2 | energy_consumption | other | quantity | 0.5699 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4967 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.4287 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.5210 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5871 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.6090 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4435 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4150 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.2883 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3480 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.5174 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5739 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5876 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.5990 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.6147 | no |
| wrong | business2 | blend60 | 2 | fuel_poverty | rate | category | 0.5004 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5685 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6562 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6812 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6626 | no |
| wrong | business2 | blend60 | 2 | numéro | id | address | 0.5064 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6887 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7645 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.6681 | no |
| wrong | business2 | blend60 | 2 | service | account | org | 0.5273 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7125 | no |
| wrong | business2 | blend60 | 2 | situtation | address | text | 0.5598 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9748 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9775 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8335 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6488 | yes |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | quantity | 0.6360 | no |
| unknown | business2 | blend70 | 1 | bike_stands | quantity | unknown | 0.4597 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4598 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4474 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.6142 | no |
| unknown | business2 | blend70 | 1 | health service executive area | address | unknown | 0.4943 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9809 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.4550 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4678 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6645 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6609 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9869 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5315 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.5523 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9894 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.5136 | no |
| unknown | business2 | blend70 | 1 | want to live in this parish only | quantity | unknown | 0.4955 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.5369 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6467 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6333 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.5997 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9003 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6698 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7696 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.6166 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.5869 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6014 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9762 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.6237 | no |
| critical | business2 | blend70 | 2 | fine | amount | rate | 0.6060 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9755 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.7262 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6639 | yes |
| other_ng | business2 | blend70 | 2 | energy_consumption | other | quantity | 0.6317 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4882 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6755 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9838 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5965 | no |
| unknown | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5863 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4805 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3287 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3939 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9860 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9819 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.5579 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9894 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.5912 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.5324 | no |
| wrong | business2 | blend70 | 2 | fuel_poverty | rate | category | 0.5834 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6628 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7241 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6288 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7361 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7101 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.8117 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7394 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6141 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6917 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.6496 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9732 | no |
| critical | business2 | ft | 1 | fine | amount | rate | 0.6345 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8388 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9125 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.6660 | no |
| other_ng | business2 | ft | 1 | energy_consumption | other | quantity | 0.8230 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.6386 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8704 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9735 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.4467 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.9298 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.9132 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9833 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9831 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9832 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.6716 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9889 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.6554 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.7363 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.5365 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9229 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7979 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.8875 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8618 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.8592 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.6747 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.7354 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.6473 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8503 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9728 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.6904 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.5672 | no |
| critical | business2 | ft | 2 | fine | amount | rate | 0.8611 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9892 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9340 | yes |
| other_ng | business2 | ft | 2 | avg_tilt | other | rate | 0.5463 | no |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.8169 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.5625 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9408 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9777 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5001 | no |
| unknown | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5182 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4500 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.5318 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9866 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9806 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9804 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9747 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9854 | no |
| unknown | business2 | ft | 2 | total invoices paid | quantity | unknown | 0.6102 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.6795 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9889 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.5209 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.6667 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.6747 | no |
| wrong | business2 | ft | 2 | cost centre description | account | org | 0.5128 | no |
| wrong | business2 | ft | 2 | fuel_poverty | rate | category | 0.8321 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9460 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9275 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9564 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.7741 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9533 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9532 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8745 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6295 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.9193 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9685 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8913 | yes |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4813 | no |
| unknown | dev220 | blend50 | 1 | material | product | unknown | 0.4976 | no |
| unknown | dev220 | blend50 | 1 | taxable | category | unknown | 0.4883 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4948 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.5000 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4903 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4845 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4889 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9690 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8709 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.5315 | no |
| critical | dev220 | blend50 | 2 | credit limit | amount | quantity | 0.5746 | yes |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8787 | yes |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4654 | no |
| unknown | dev220 | blend50 | 2 | material | product | unknown | 0.4938 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4993 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4884 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4894 | no |
| unknown | dev220 | blend50 | 2 | 商品計 | amount | unknown | 0.4936 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4862 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4964 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9596 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8714 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5008 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.9076 | yes |
| unknown | dev220 | blend60 | 1 | tax id | id | unknown | 0.4876 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9661 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.8921 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.5674 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.5037 | no |
| critical | dev220 | blend60 | 2 | credit limit | amount | quantity | 0.6168 | yes |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8924 | yes |
| unknown | dev220 | blend60 | 2 | 商品計 | amount | unknown | 0.4650 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9547 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.8926 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9238 | yes |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.5077 | no |
| unknown | dev220 | blend70 | 1 | 支払を受ける者の個人番号 | id | unknown | 0.4615 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9631 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9133 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.6033 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.5665 | no |
| critical | dev220 | blend70 | 2 | credit limit | amount | quantity | 0.6590 | yes |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9062 | yes |
| unknown | dev220 | blend70 | 2 | 商品計 | amount | unknown | 0.5142 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9499 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9139 | no |
| wrong | dev220 | blend70 | 2 | 税率 | rate | tax_class | 0.5062 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9726 | yes |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.7253 | no |
| unknown | dev220 | ft | 1 | 支払を受ける者の個人番号 | id | unknown | 0.6077 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9543 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9769 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.7111 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.7548 | no |
| critical | dev220 | ft | 2 | credit limit | amount | quantity | 0.7856 | yes |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9474 | yes |
| critical | dev220 | ft | 2 | 商品計 | amount | quantity | 0.6616 | yes |
| unknown | dev220 | ft | 2 | 履行場所 | address | unknown | 0.4986 | no |
| unknown | dev220 | ft | 2 | 支払を受ける者の個人番号 | id | unknown | 0.4778 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9354 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9778 | no |
| wrong | dev220 | ft | 2 | 税率 | rate | tax_class | 0.7169 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.9025 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.6959 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9252 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.8665 | no |
| other_ng | general | blend50 | 1 | 被害域幅(m)最小 | other | quantity | 0.5015 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.5584 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4790 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5326 | no |
| unknown | general | blend50 | 1 | goal | id | unknown | 0.4537 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.9270 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4651 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4168 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4749 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4693 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4927 | no |
| unknown | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | unknown | 0.4986 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9691 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4592 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9910 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9256 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5095 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5117 | no |
| wrong | general | blend50 | 1 | indicator | text | category | 0.6030 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8372 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8949 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7943 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.7497 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5173 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | quantity | 0.6360 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.9014 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5798 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9297 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9864 | no |
| other_ng | general | blend50 | 2 | 被害域幅(m)最小 | other | quantity | 0.5157 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4368 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4959 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5328 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9213 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4399 | no |
| unknown | general | blend50 | 2 | mechanism | category | unknown | 0.4444 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4694 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4525 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4792 | no |
| unknown | general | blend50 | 2 | source | category | unknown | 0.4983 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4629 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.5428 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9720 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4423 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9934 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9212 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3806 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.9212 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.6619 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.7272 | no |
| wrong | general | blend50 | 2 | indicator | text | category | 0.7567 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9067 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8830 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.7634 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.8783 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.8993 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.6523 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9322 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.8399 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4980 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.5443 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6237 | no |
| unknown | general | blend60 | 1 | goal | id | unknown | 0.4886 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9365 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3661 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5784 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4845 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5560 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9720 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3867 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9893 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9296 | no |
| wrong | general | blend60 | 1 | indicator | text | category | 0.6059 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8299 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8781 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7988 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.7188 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5766 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5305 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | quantity | 0.5989 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.8979 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5239 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.5131 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9377 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9838 | no |
| unknown | general | blend60 | 2 | bib | id | unknown | 0.4530 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.4518 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6240 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9297 | no |
| unknown | general | blend60 | 2 | lda | text | unknown | 0.4493 | no |
| unknown | general | blend60 | 2 | mechanism | category | unknown | 0.4530 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5410 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.4957 | no |
| unknown | general | blend60 | 2 | 城南第2 | quantity | unknown | 0.5741 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9754 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3742 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9921 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9243 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4086 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.9119 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6015 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7158 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.7903 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9133 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8638 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5055 | no |
| wrong | general | blend60 | 2 | source | category | text | 0.5518 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.7617 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.8732 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5841 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.5418 | yes |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.8960 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.6088 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9393 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8133 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6295 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7148 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9461 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4254 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6738 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.4435 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9748 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.3508 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9875 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9335 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.5803 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.6089 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8226 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8613 | no |
| wrong | general | blend70 | 1 | source | category | text | 0.5569 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8032 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.6880 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6698 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.5437 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | quantity | 0.5618 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.8945 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.5974 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9457 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9812 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.5239 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7151 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9381 | no |
| unknown | general | blend70 | 2 | lda | text | unknown | 0.4710 | no |
| unknown | general | blend70 | 2 | mechanism | category | unknown | 0.4926 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6295 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.5716 | no |
| unknown | general | blend70 | 2 | 城南第2 | quantity | unknown | 0.5033 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9788 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.4365 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9908 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9274 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4760 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.9026 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5412 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.7044 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.8240 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9199 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8446 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.5894 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.6355 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.7600 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.8682 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6786 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.7012 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.5099 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.8863 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9606 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.7336 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.8852 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9882 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9747 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.6036 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9603 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.4329 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9833 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9821 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9454 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.8272 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.6176 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.8007 | no |
| wrong | general | ft | 1 | place | org | address | 0.8109 | no |
| wrong | general | ft | 1 | source | category | text | 0.7745 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8165 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.5956 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9494 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.5833 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.7403 | yes |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.8841 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.6571 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.8182 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.6570 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9697 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9734 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9885 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9634 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8952 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8142 | no |
| unknown | general | ft | 2 | 城南第2 | quantity | unknown | 0.6337 | no |
| unknown | general | ft | 2 | 東第5 | quantity | unknown | 0.4931 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9890 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9868 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9366 | no |
| wrong | general | ft | 2 | author | person | org | 0.8747 | no |
| wrong | general | ft | 2 | goal | id | category | 0.6702 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.9250 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9397 | no |
| wrong | general | ft | 2 | lda | text | category | 0.5362 | no |
| wrong | general | ft | 2 | mechanism | category | id | 0.6115 | no |
| wrong | general | ft | 2 | place | org | address | 0.7870 | no |
| wrong | general | ft | 2 | source | category | org | 0.8410 | no |
| wrong | general | ft | 2 | source | category | text | 0.8868 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7547 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8529 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.9620 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.6233 | no |

### unknown の判定理由

- date_value_evidence_low: 73件
- numeric_top2_too_close: 39件
- numeric_values_not_parseable: 19件
- other_class: 80件
- probability_below_threshold: 157件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 45件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 168件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 114件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
