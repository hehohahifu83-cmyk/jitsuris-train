# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-24T18:46:48+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 6 | 1 | 20 | 0 |
| business | blend50 | 2 | 490 | 8 | 0 | 23 | 0 |
| business | blend60 | 1 | 490 | 6 | 0 | 14 | 0 |
| business | blend60 | 2 | 490 | 10 | 1 | 12 | 0 |
| business | blend70 | 1 | 490 | 9 | 0 | 10 | 0 |
| business | blend70 | 2 | 490 | 11 | 2 | 10 | 0 |
| business | ft | 1 | 490 | 12 | 1 | 7 | 1 |
| business | ft | 2 | 490 | 14 | 3 | 7 | 0 |
| business2 | blend50 | 1 | 976 | 15 | 3 | 31 | 1 |
| business2 | blend50 | 2 | 976 | 11 | 2 | 32 | 1 |
| business2 | blend60 | 1 | 976 | 16 | 2 | 24 | 0 |
| business2 | blend60 | 2 | 976 | 11 | 1 | 32 | 0 |
| business2 | blend70 | 1 | 976 | 15 | 2 | 20 | 0 |
| business2 | blend70 | 2 | 976 | 13 | 2 | 25 | 0 |
| business2 | ft | 1 | 976 | 17 | 4 | 17 | 1 |
| business2 | ft | 2 | 976 | 16 | 3 | 16 | 1 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 10 | 0 |
| dev220 | blend50 | 2 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 6 | 1 | 3 | 0 |
| dev220 | blend60 | 2 | 220 | 6 | 2 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 3 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 2 | 1 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 3 | 0 |
| dev220 | ft | 2 | 220 | 9 | 2 | 1 | 0 |
| general | blend50 | 1 | 383 | 10 | 0 | 14 | 6 |
| general | blend50 | 2 | 383 | 13 | 1 | 10 | 6 |
| general | blend60 | 1 | 383 | 11 | 1 | 11 | 4 |
| general | blend60 | 2 | 383 | 13 | 1 | 13 | 5 |
| general | blend70 | 1 | 383 | 9 | 1 | 11 | 4 |
| general | blend70 | 2 | 383 | 12 | 1 | 13 | 5 |
| general | ft | 1 | 383 | 11 | 1 | 11 | 7 |
| general | ft | 2 | 383 | 15 | 2 | 11 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, text→account: 2, account→category: 2, quantity→amount: 1, text→org: 1, account→text: 1
- business / blend60: org→account: 7, account→category: 3, category→id: 2, text→account: 1, org→address: 1, account→text: 1, amount→quantity: 1
- business / blend70: org→account: 8, account→category: 3, category→id: 3, amount→quantity: 2, text→account: 1, org→category: 1, org→address: 1, account→text: 1
- business / ft: org→account: 8, account→category: 4, amount→quantity: 4, category→id: 3, org→address: 2, org→category: 2, text→account: 1, category→account: 1
- business2 / blend50: account→category: 5, amount→quantity: 4, category→id: 3, address→category: 3, category→text: 2, quantity→category: 2, org→address: 2, id→address: 2
- business2 / blend60: account→category: 4, category→id: 3, address→category: 3, category→quantity: 3, amount→quantity: 3, category→text: 2, quantity→category: 2, category→address: 2
- business2 / blend70: category→id: 4, amount→quantity: 4, account→category: 3, category→quantity: 3, category→text: 2, category→address: 2, address→category: 2, org→address: 2
- business2 / ft: amount→quantity: 6, category→id: 5, category→quantity: 4, account→category: 3, id→category: 2, category→text: 2, category→address: 2, address→text: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, category→tax_class: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, category→text: 1, amount→quantity: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, category→text: 1, address→id: 1, amount→quantity: 1
- dev220 / ft: quantity→category: 4, address→id: 3, org→account: 2, text→category: 2, id→quantity: 2, category→text: 1, amount→quantity: 1
- general / blend50: text→category: 7, category→text: 4, org→address: 4, person→org: 2, quantity→category: 2, address→org: 2, id→quantity: 1, id→category: 1
- general / blend60: text→category: 6, category→text: 4, org→address: 4, person→org: 2, quantity→category: 2, address→org: 2, id→quantity: 2, category→org: 1
- general / blend70: text→category: 5, category→text: 4, org→address: 4, quantity→category: 2, address→org: 2, id→quantity: 2, person→org: 1, category→org: 1
- general / ft: category→text: 5, text→category: 5, org→address: 4, id→quantity: 3, quantity→category: 2, address→org: 2, id→address: 1, person→org: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `ligne`、category→id（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `ligne`、category→id（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `australian sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business2 / blend50: `contravention`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `contravention`、category→text（seed 1, seed 2）
- business2 / blend60: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `contravention`、category→text（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service`、account→org（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / ft: `contravention`、category→text（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend50: `随意契約理由`、text→category（seed 1, seed 2）
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
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `indicator`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `lda`、text→category（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `raw`、category→text（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend50: `読み方`、address→org（seed 1, seed 2）
- general / blend60: `author`、person→org（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `indicator`、text→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `lda`、text→category（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend60: `読み方`、address→org（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `indicator`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `読み方`、address→org（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `indicator`、text→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `読み方`、address→org（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.6559 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5385 | no |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5447 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5794 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3384 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.4441 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4544 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5418 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5560 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4599 | no |
| unknown | business | blend50 | 1 | merchant details | text | unknown | 0.3570 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.5436 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3481 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4737 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4690 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9688 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4681 | no |
| unknown | business | blend50 | 1 | segment-title_en | category | unknown | 0.4716 | no |
| unknown | business | blend50 | 1 | segment-title_fr | category | unknown | 0.4010 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9540 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9145 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9801 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.8407 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9837 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9401 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5446 | no |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5268 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5472 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5624 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4590 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.4094 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4470 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5424 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4888 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.5557 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4928 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.5390 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.3825 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.4367 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4797 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9585 | no |
| unknown | business | blend50 | 2 | regrp_nom | account | unknown | 0.4581 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.4597 | no |
| unknown | business | blend50 | 2 | segment-title_en | category | unknown | 0.4903 | no |
| unknown | business | blend50 | 2 | segment-title_fr | category | unknown | 0.4745 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.3429 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5739 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9650 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9139 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9770 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.8650 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9802 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.5606 | no |
| wrong | business | blend50 | 2 | merchant details | text | org | 0.5014 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.7354 | no |
| wrong | business | blend50 | 2 | procurementclassification:proclasslabel | account | category | 0.5125 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.5368 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.4060 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.5040 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.4725 | no |
| unknown | business | blend60 | 1 | merchant details | text | unknown | 0.2956 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6309 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4010 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4997 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4328 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9727 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4528 | no |
| unknown | business | blend60 | 1 | segment-title_fr | category | unknown | 0.3600 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5873 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9494 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9228 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9776 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8337 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9818 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5396 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9352 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6287 | no |
| critical | business | blend60 | 2 | australian sourced goods | amount | quantity | 0.5507 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6062 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.3607 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.3948 | no |
| unknown | business | blend60 | 2 | merchant details | text | unknown | 0.4688 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6254 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.4589 | no |
| unknown | business | blend60 | 2 | overseas sourced services | amount | unknown | 0.4204 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9603 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.3228 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.4965 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9626 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9221 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9739 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.8629 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9777 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.6332 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5791 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.7586 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.5433 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5670 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.5269 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4736 | no |
| unknown | business | blend70 | 1 | merchant details | text | unknown | 0.2957 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7183 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.4639 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4977 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9766 | no |
| unknown | business | blend70 | 1 | segment-title_fr | category | unknown | 0.3871 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.5188 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9448 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9311 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9751 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8267 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9800 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5513 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6192 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | category | 0.5257 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9303 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7129 | no |
| wrong | business | blend70 | 1 | type de matériel | category | id | 0.5351 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6425 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.5353 | yes |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.3968 | no |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.4510 | no |
| unknown | business | blend70 | 2 | merchant details | text | unknown | 0.4362 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7118 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.4643 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9622 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.3596 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.5790 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9603 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9303 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9708 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8608 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9751 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.7057 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6653 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.7818 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5741 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6543 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.5941 | no |
| critical | business | ft | 1 | australian sourced goods | amount | quantity | 0.6765 | yes |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.6151 | no |
| unknown | business | ft | 1 | merchant details | text | unknown | 0.4220 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9803 | no |
| unknown | business | ft | 1 | overseas sourced services | amount | unknown | 0.6075 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9883 | no |
| unknown | business | ft | 1 | segment-title_fr | category | unknown | 0.4819 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9310 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9559 | no |
| wrong | business | ft | 1 | department | org | account | 0.9676 | no |
| wrong | business | ft | 1 | department | org | account | 0.8058 | no |
| wrong | business | ft | 1 | department | org | account | 0.9744 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.7875 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.8582 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | category | 0.6037 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.5034 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.6924 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9157 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9653 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.7533 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9177 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.7644 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.6290 | yes |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.5050 | no |
| unknown | business | ft | 2 | merchant details | text | unknown | 0.3384 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9712 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9677 | no |
| unknown | business | ft | 2 | title | category | unknown | 0.4698 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9531 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9549 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.6130 | no |
| wrong | business | ft | 2 | department | org | account | 0.9615 | no |
| wrong | business | ft | 2 | department | org | account | 0.8546 | no |
| wrong | business | ft | 2 | department | org | account | 0.9674 | no |
| wrong | business | ft | 2 | description | account | text | 0.9233 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.6268 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.9241 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.8514 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.6665 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9161 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.7956 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9581 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8272 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.6737 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5170 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.5389 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5459 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4828 | no |
| unknown | business2 | blend50 | 1 | column6 | text | unknown | 0.4937 | no |
| unknown | business2 | blend50 | 1 | conservation_area_site_id | category | unknown | 0.4541 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3797 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.2820 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4139 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.4480 | no |
| unknown | business2 | blend50 | 1 | number_habitable_rooms_known | category | unknown | 0.5630 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4021 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9875 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5439 | no |
| unknown | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5503 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3951 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4901 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4781 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4695 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.3238 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4577 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4176 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9927 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9925 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9919 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.4253 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4960 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5079 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9930 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.5981 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.5361 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.5592 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.8206 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.5864 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.6174 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.8417 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7022 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.8858 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.6779 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9844 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.5528 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.5385 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9574 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6174 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.5275 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5254 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5465 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.2576 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.3888 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4257 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4370 | no |
| unknown | business2 | blend50 | 2 | merchant description | category | unknown | 0.4796 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4036 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.5129 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.3739 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9879 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4600 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4704 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5814 | no |
| unknown | business2 | blend50 | 2 | scheme_description | category | unknown | 0.4185 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4176 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4909 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4199 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.2783 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3405 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.5079 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9872 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9862 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5691 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4959 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5031 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.5864 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4777 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5303 | no |
| wrong | business2 | blend50 | 2 | imd19_national_decile | category | id | 0.5712 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7350 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5953 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.5896 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.5411 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6715 | no |
| wrong | business2 | blend50 | 2 | total_floor_area_known | category | quantity | 0.5568 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9664 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9641 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8363 | yes |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4553 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.3612 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.3172 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4148 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.4359 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.4803 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9854 | no |
| unknown | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.4955 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4685 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3801 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5332 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4120 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.6087 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4719 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5835 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5833 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6027 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9925 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.5342 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.5611 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5137 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.6231 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.7871 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.5178 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6385 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6430 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8659 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.7547 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.8863 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.6317 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9837 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.5159 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.5113 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9633 | yes |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6045 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.2895 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4222 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.5044 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.4929 | no |
| unknown | business2 | blend60 | 2 | health service executive area | address | unknown | 0.4760 | no |
| unknown | business2 | blend60 | 2 | merchant description | category | unknown | 0.4051 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.4365 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4465 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9859 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5845 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4190 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4526 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5202 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4794 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4955 | no |
| unknown | business2 | blend60 | 2 | surveyname | text | unknown | 0.4965 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3255 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3926 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5784 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9861 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9850 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9839 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9816 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9869 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5033 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5663 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5939 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.5969 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9905 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.5202 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4384 | no |
| wrong | business2 | blend60 | 2 | contravention | category | text | 0.5541 | no |
| wrong | business2 | blend60 | 2 | imd19_national_decile | category | id | 0.5651 | no |
| wrong | business2 | blend60 | 2 | loac_group | category | address | 0.5640 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6843 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.5285 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.5784 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6096 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6240 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.5672 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9621 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9702 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8454 | yes |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.3462 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.3666 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4786 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.4800 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.5359 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9833 | no |
| unknown | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5489 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4365 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6087 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4548 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5437 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.5184 | no |
| unknown | business2 | blend70 | 1 | total_verified_sales | quantity | unknown | 0.5296 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9920 | no |
| unknown | business2 | blend70 | 1 | warddesc | address | unknown | 0.4842 | no |
| wrong | business2 | blend70 | 1 | conservation_area_site_id | category | id | 0.5281 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.5861 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.5993 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6871 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.7535 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7140 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.6686 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8901 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8072 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.5419 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8869 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.5854 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9831 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.5831 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9692 | yes |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.3214 | no |
| unknown | business2 | blend70 | 2 | conservation_area_site_id | category | unknown | 0.4787 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4557 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.4950 | no |
| unknown | business2 | blend70 | 2 | merchant description | category | unknown | 0.3710 | no |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.4693 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5194 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.5191 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9839 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5517 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4428 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4349 | no |
| unknown | business2 | blend70 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5269 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3728 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4446 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6489 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9827 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9815 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9789 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9860 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.5869 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5095 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9896 | no |
| unknown | business2 | blend70 | 2 | warddesc | address | unknown | 0.3991 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.5779 | no |
| wrong | business2 | blend70 | 2 | health service executive area | address | org | 0.5197 | no |
| wrong | business2 | blend70 | 2 | imd19_national_decile | category | id | 0.5591 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6580 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6337 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6439 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.6296 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5735 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.5765 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.5776 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9579 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.6699 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9883 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8728 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7092 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.6584 | no |
| unknown | business2 | ft | 1 | construction_age_band | category | unknown | 0.4638 | no |
| unknown | business2 | ft | 1 | energy_consumption_known | category | unknown | 0.4724 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.5148 | no |
| unknown | business2 | ft | 1 | health service executive area | address | unknown | 0.4993 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.7401 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9771 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.8351 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5833 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9871 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9891 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.6579 | no |
| unknown | business2 | ft | 1 | total_verified_sales | quantity | unknown | 0.6149 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9906 | no |
| unknown | business2 | ft | 1 | warddesc | address | unknown | 0.4458 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.7465 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.6610 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.8561 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8789 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.6529 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9405 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.7453 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9626 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9647 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.7622 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.8885 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.5158 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9812 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.8191 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9869 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.6455 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | amount | 0.7496 | no |
| unknown | business2 | ft | 2 | amt-units_mnt-unite | category | unknown | 0.4172 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.6930 | no |
| unknown | business2 | ft | 2 | merchant description | category | unknown | 0.4702 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7165 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9778 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5201 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.3817 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6008 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8605 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9804 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9761 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9745 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9708 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9834 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9871 | no |
| unknown | business2 | ft | 2 | warddesc | address | unknown | 0.4121 | no |
| wrong | business2 | ft | 2 | conservation_area_site_id | category | id | 0.5859 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.6494 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.5560 | no |
| wrong | business2 | ft | 2 | health service executive area | address | org | 0.6507 | no |
| wrong | business2 | ft | 2 | imd19_national_decile | category | id | 0.5409 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9400 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.5678 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.8404 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.6896 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8072 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.5196 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.6089 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9452 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8574 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.5420 | no |
| unknown | dev220 | blend50 | 1 | taxable | category | unknown | 0.4916 | no |
| unknown | dev220 | blend50 | 1 | terms | category | unknown | 0.4924 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4990 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5445 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4934 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4876 | no |
| unknown | dev220 | blend50 | 1 | 商品計 | amount | unknown | 0.4812 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4940 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4986 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9000 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8184 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7743 | no |
| wrong | dev220 | blend50 | 1 | 随意契約理由 | text | category | 0.5495 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8554 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.5591 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4967 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5422 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4930 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4907 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4231 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4940 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9365 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8203 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.5626 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7677 | no |
| wrong | dev220 | blend50 | 2 | 随意契約理由 | text | category | 0.5421 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8773 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.5468 | no |
| unknown | dev220 | blend60 | 1 | tax id | id | unknown | 0.4942 | no |
| unknown | dev220 | blend60 | 1 | 商品計 | amount | unknown | 0.5014 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8851 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.8483 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.5199 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.8031 | no |
| wrong | dev220 | blend60 | 1 | 随意契約理由 | text | category | 0.6208 | no |
| critical | dev220 | blend60 | 2 | credit limit | amount | quantity | 0.5912 | yes |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8750 | yes |
| unknown | dev220 | blend60 | 2 | taxable | category | unknown | 0.4833 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9290 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.8505 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7951 | no |
| wrong | dev220 | blend60 | 2 | 随意契約理由 | text | category | 0.6119 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8973 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.5517 | no |
| unknown | dev220 | blend70 | 1 | tax id | id | unknown | 0.5766 | no |
| unknown | dev220 | blend70 | 1 | 商品計 | amount | unknown | 0.5415 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8703 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.8782 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.5474 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8318 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.6921 | no |
| critical | dev220 | blend70 | 2 | credit limit | amount | quantity | 0.6233 | yes |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8945 | yes |
| unknown | dev220 | blend70 | 2 | 商品オプション | text | unknown | 0.4932 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9214 | no |
| wrong | dev220 | blend70 | 2 | shipping address | address | id | 0.5691 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.8808 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8226 | no |
| wrong | dev220 | blend70 | 2 | 随意契約理由 | text | category | 0.6817 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9571 | yes |
| unknown | dev220 | ft | 1 | credit limit | amount | unknown | 0.5663 | no |
| unknown | dev220 | ft | 1 | tax id | id | unknown | 0.8237 | no |
| unknown | dev220 | ft | 1 | 支払を受ける者の個人番号 | id | unknown | 0.4558 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8258 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9678 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.6300 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9181 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.9061 | no |
| critical | dev220 | ft | 2 | credit limit | amount | quantity | 0.7197 | yes |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9531 | yes |
| unknown | dev220 | ft | 2 | 商品オプション | text | unknown | 0.4167 | no |
| wrong | dev220 | ft | 2 | city | address | id | 0.6107 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8988 | no |
| wrong | dev220 | ft | 2 | shipping address | address | id | 0.8128 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9715 | no |
| wrong | dev220 | ft | 2 | 履行場所 | address | id | 0.5319 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.9049 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.8912 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.8817 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.5524 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9096 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.8700 | no |
| other_ng | general | blend50 | 1 | 被害域幅(m)最小 | other | quantity | 0.5162 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.5137 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4968 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.5208 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6083 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.5488 | no |
| unknown | general | blend50 | 1 | goal | id | unknown | 0.4716 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8986 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4857 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4914 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4005 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4454 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9608 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4245 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9935 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9435 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5909 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.8073 | no |
| wrong | general | blend50 | 1 | indicator | text | category | 0.7706 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8356 | no |
| wrong | general | blend50 | 1 | lda | text | category | 0.5210 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.9204 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.5229 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.8596 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.8397 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5458 | no |
| critical | general | blend50 | 2 | 発生県 | id | quantity | 0.7747 | yes |
| other_ng | general | blend50 | 2 | dag-stage | other | quantity | 0.7052 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.7867 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.7257 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9278 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9900 | no |
| other_ng | general | blend50 | 2 | 被害域幅(m)最小 | other | quantity | 0.5078 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4793 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.5330 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.6088 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.5236 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9050 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.2856 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.5087 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9575 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9897 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9448 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.8064 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.9662 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5559 | no |
| wrong | general | blend50 | 2 | indicator | text | category | 0.6913 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.7518 | no |
| wrong | general | blend50 | 2 | lda | text | category | 0.7250 | no |
| wrong | general | blend50 | 2 | pelicula | text | category | 0.5467 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.9251 | no |
| wrong | general | blend50 | 2 | raw | category | text | 0.5150 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.7586 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.7174 | no |
| wrong | general | blend50 | 2 | 読み方 | address | org | 0.5196 | no |
| critical | general | blend60 | 1 | goal | id | quantity | 0.5441 | yes |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.5577 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.8737 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9129 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.8443 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.5972 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6840 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.9073 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4306 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5109 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.4735 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5019 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9661 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3463 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9922 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9415 | no |
| wrong | general | blend60 | 1 | author | person | org | 0.5151 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.7702 | no |
| wrong | general | blend60 | 1 | indicator | text | category | 0.7785 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8492 | no |
| wrong | general | blend60 | 1 | lda | text | category | 0.5014 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.9105 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.8721 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.8537 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5502 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5630 | no |
| critical | general | blend60 | 2 | 発生県 | id | quantity | 0.7666 | yes |
| other_ng | general | blend60 | 2 | dag-stage | other | quantity | 0.6731 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.7596 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.7024 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9347 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9884 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.6119 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6845 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9150 | no |
| unknown | general | blend60 | 2 | ngram | text | unknown | 0.5583 | no |
| unknown | general | blend60 | 2 | pelicula | text | unknown | 0.4661 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4815 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5719 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4748 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.3383 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4772 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9622 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9877 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9431 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.7736 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.9608 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5004 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.6832 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.7487 | no |
| wrong | general | blend60 | 2 | lda | text | category | 0.7462 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.9162 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5230 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.7509 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7070 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5261 | no |
| wrong | general | blend60 | 2 | 読み方 | address | org | 0.5316 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.6171 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6290 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.8656 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9161 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8187 | no |
| unknown | general | blend70 | 1 | author | person | unknown | 0.4392 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6737 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7597 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9160 | no |
| unknown | general | blend70 | 1 | lda | text | unknown | 0.4819 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.3697 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5948 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9713 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.3614 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9909 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9396 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.7330 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.7863 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8629 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.9006 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8846 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.8678 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6398 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.5802 | no |
| critical | general | blend70 | 2 | 発生県 | id | quantity | 0.7585 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | quantity | 0.6409 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.7326 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.6792 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9416 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9868 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.6908 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7603 | no |
| unknown | general | blend70 | 2 | goal | id | unknown | 0.4780 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9250 | no |
| unknown | general | blend70 | 2 | ngram | text | unknown | 0.6510 | no |
| unknown | general | blend70 | 2 | pelicula | text | unknown | 0.4394 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6660 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.3915 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.3910 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.5342 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9668 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9856 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9414 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.7409 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.9554 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.6752 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.7456 | no |
| wrong | general | blend70 | 2 | lda | text | category | 0.7674 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.9073 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6097 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.7432 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.6966 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6117 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.5435 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.8363 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8428 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.8415 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.5397 | no |
| other_ng | general | ft | 1 | nodes | other | category | 0.5858 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9258 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.7418 | no |
| other_ng | general | ft | 1 | 和名 | other | address | 0.5695 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9032 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9867 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9421 | no |
| unknown | general | ft | 1 | lda | text | unknown | 0.4893 | no |
| unknown | general | ft | 1 | mechanism | category | unknown | 0.4760 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.4360 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.8466 | no |
| unknown | general | ft | 1 | term | text | unknown | 0.4913 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9872 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9870 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9338 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.6215 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.8097 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9038 | no |
| wrong | general | ft | 1 | place | org | address | 0.8710 | no |
| wrong | general | ft | 1 | source | category | text | 0.5072 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9222 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9099 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9085 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.5160 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.6318 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.6376 | yes |
| critical | general | ft | 2 | 発生県 | id | quantity | 0.7341 | yes |
| other_ng | general | ft | 2 | dag-stage | other | quantity | 0.5443 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.6515 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.6975 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.6095 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9622 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9820 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9276 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9876 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9549 | no |
| unknown | general | ft | 2 | mechanism | category | unknown | 0.4453 | no |
| unknown | general | ft | 2 | ngram | text | unknown | 0.9293 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.4339 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9483 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.4131 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9807 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9795 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9364 | no |
| wrong | general | ft | 2 | author | person | org | 0.6426 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.9392 | no |
| wrong | general | ft | 2 | domain | category | id | 0.5041 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.6510 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.7363 | no |
| wrong | general | ft | 2 | lda | text | category | 0.8311 | no |
| wrong | general | ft | 2 | place | org | address | 0.8805 | no |
| wrong | general | ft | 2 | source | category | org | 0.8699 | no |
| wrong | general | ft | 2 | study | text | person | 0.5492 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7203 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6653 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8684 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.5794 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 66件
- numeric_values_not_parseable: 20件
- other_class: 76件
- probability_below_threshold: 189件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 46件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 178件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 119件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
