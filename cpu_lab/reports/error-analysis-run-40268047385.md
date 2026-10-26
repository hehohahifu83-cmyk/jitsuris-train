# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-26T05:47:00+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 10 | 2 | 18 | 0 |
| business | blend50 | 2 | 490 | 8 | 1 | 13 | 0 |
| business | blend60 | 1 | 490 | 10 | 2 | 16 | 0 |
| business | blend60 | 2 | 490 | 9 | 1 | 10 | 0 |
| business | blend70 | 1 | 490 | 11 | 2 | 13 | 0 |
| business | blend70 | 2 | 490 | 9 | 1 | 8 | 0 |
| business | ft | 1 | 490 | 12 | 1 | 8 | 0 |
| business | ft | 2 | 490 | 13 | 1 | 7 | 0 |
| business2 | blend50 | 1 | 976 | 13 | 3 | 26 | 0 |
| business2 | blend50 | 2 | 976 | 15 | 2 | 26 | 1 |
| business2 | blend60 | 1 | 976 | 15 | 3 | 23 | 0 |
| business2 | blend60 | 2 | 976 | 14 | 2 | 23 | 0 |
| business2 | blend70 | 1 | 976 | 16 | 3 | 18 | 1 |
| business2 | blend70 | 2 | 976 | 16 | 2 | 21 | 0 |
| business2 | ft | 1 | 976 | 18 | 3 | 17 | 1 |
| business2 | ft | 2 | 976 | 18 | 4 | 17 | 3 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 7 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 2 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 6 | 2 | 0 | 0 |
| dev220 | ft | 2 | 220 | 4 | 0 | 1 | 0 |
| general | blend50 | 1 | 383 | 9 | 0 | 17 | 5 |
| general | blend50 | 2 | 383 | 7 | 0 | 18 | 4 |
| general | blend60 | 1 | 383 | 9 | 0 | 17 | 5 |
| general | blend60 | 2 | 383 | 7 | 0 | 18 | 5 |
| general | blend70 | 1 | 383 | 8 | 0 | 18 | 7 |
| general | blend70 | 2 | 383 | 8 | 0 | 16 | 5 |
| general | ft | 1 | 383 | 9 | 1 | 13 | 9 |
| general | ft | 2 | 383 | 9 | 0 | 15 | 5 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 7, quantity→amount: 3, text→category: 2, account→text: 2, text→account: 2, account→category: 2
- business / blend60: org→account: 7, quantity→amount: 3, text→category: 2, account→text: 2, text→account: 2, account→category: 2, category→id: 1
- business / blend70: org→account: 6, quantity→amount: 3, text→category: 2, account→text: 2, text→account: 2, account→category: 2, category→id: 2, org→address: 1
- business / ft: org→account: 7, category→id: 4, quantity→amount: 2, org→address: 2, text→category: 2, account→text: 2, text→account: 2, account→category: 2
- business2 / blend50: account→category: 4, id→address: 4, quantity→amount: 3, address→category: 3, category→quantity: 3, id→category: 2, quantity→category: 2, org→address: 2
- business2 / blend60: account→category: 4, id→address: 4, quantity→amount: 3, address→category: 3, category→quantity: 3, id→category: 2, quantity→category: 2, org→address: 2
- business2 / blend70: account→category: 4, id→address: 4, quantity→amount: 3, category→quantity: 3, id→category: 2, address→category: 2, quantity→category: 2, category→address: 2
- business2 / ft: quantity→amount: 4, id→address: 4, account→category: 3, category→quantity: 3, account→org: 3, id→category: 2, category→date: 2, quantity→category: 2
- dev220 / blend50: quantity→category: 4, id→quantity: 2, org→account: 1, category→text: 1, category→tax_class: 1, text→category: 1
- dev220 / blend60: quantity→category: 4, id→quantity: 2, org→account: 1, category→text: 1, text→category: 1
- dev220 / blend70: quantity→category: 4, id→quantity: 2, org→account: 1, category→text: 1, amount→quantity: 1, text→category: 1
- dev220 / ft: quantity→category: 4, org→account: 2, category→text: 1, id→quantity: 1, amount→quantity: 1, text→category: 1
- general / blend50: org→address: 4, category→text: 3, text→category: 3, person→org: 2, quantity→category: 2, id→category: 2
- general / blend60: category→text: 4, org→address: 4, quantity→category: 2, id→category: 2, text→category: 2, category→id: 1, id→address: 1
- general / blend70: category→text: 4, org→address: 4, quantity→category: 2, id→category: 2, text→category: 2, category→id: 1, id→address: 1
- general / ft: category→text: 5, org→address: 4, category→id: 2, quantity→category: 2, quantity→rate: 1, text→category: 1, org→person: 1, id→address: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `type de matériel`、category→id（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `monitor`、id→category（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service`、account→org（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
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
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
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
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `mechanism`、category→id（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.7094 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9714 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5502 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5718 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.4653 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.4776 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.5387 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5210 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4705 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5459 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4508 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.5759 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4837 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4839 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4845 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9811 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4764 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4650 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.8939 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8827 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9148 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.5602 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9622 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.6215 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.6424 | no |
| wrong | business | blend50 | 1 | procurementclassification:proclasslabel | account | category | 0.5346 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9522 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5448 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.8665 | yes |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4805 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.5133 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4957 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4846 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4899 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.5595 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4756 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4721 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9670 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3492 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4531 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9604 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8691 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9428 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.5796 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9813 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.5788 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7454 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.7403 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9474 | no |
| critical | business | blend60 | 1 | # invoices paid within 30 days | quantity | amount | 0.6804 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9660 | yes |
| unknown | business | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.4953 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.3744 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.3873 | no |
| unknown | business | blend60 | 1 | defence services value | amount | unknown | 0.6140 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.4395 | no |
| unknown | business | blend60 | 1 | ligne | category | unknown | 0.4291 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6507 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.3899 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4425 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4047 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9821 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4835 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.3958 | no |
| unknown | business | blend60 | 1 | type de matériel | category | unknown | 0.4968 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.8780 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8811 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8999 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.5174 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9558 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6879 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.6553 | no |
| wrong | business | blend60 | 1 | procurementclassification:proclasslabel | account | category | 0.5935 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9493 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6254 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.8405 | yes |
| unknown | business | blend60 | 2 | agebann | category | unknown | 0.4659 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.3949 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6443 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5615 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4378 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9713 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.3768 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.4160 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9621 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8876 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9329 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.5251 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9804 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.6376 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5765 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7898 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.7352 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9445 | no |
| critical | business | blend70 | 1 | # invoices paid within 30 days | quantity | amount | 0.6513 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9606 | yes |
| unknown | business | blend70 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5504 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.3884 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.4191 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.4624 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7255 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.4542 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4012 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4662 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9831 | no |
| unknown | business | blend70 | 1 | regrp_nom | account | unknown | 0.4906 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.3812 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.8621 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8794 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8849 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9493 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7544 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.5126 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.6682 | no |
| wrong | business | blend70 | 1 | procurementclassification:proclasslabel | account | category | 0.6524 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9464 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7059 | no |
| wrong | business | blend70 | 1 | type de matériel | category | id | 0.5769 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.8145 | yes |
| unknown | business | blend70 | 2 | agebann | category | unknown | 0.4513 | no |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.3930 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7290 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9756 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4044 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.4490 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9638 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9061 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9231 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9794 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6964 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6704 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.8342 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.7300 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.5038 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9417 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9444 | yes |
| unknown | business | ft | 1 | # invoices paid within 30 days | quantity | unknown | 0.5641 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.5547 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.5733 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9499 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3991 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9863 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.8144 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.8745 | no |
| wrong | business | ft | 1 | department | org | account | 0.8399 | no |
| wrong | business | ft | 1 | department | org | account | 0.9300 | no |
| wrong | business | ft | 1 | description | account | text | 0.9537 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.7321 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.6258 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.7068 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.8291 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.6508 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9378 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9475 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.8170 | no |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.7366 | yes |
| unknown | business | ft | 2 | agebann | category | unknown | 0.4860 | no |
| unknown | business | ft | 2 | capital revenue | category | unknown | 0.4909 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9832 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9886 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.4871 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9689 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9616 | no |
| wrong | business | ft | 2 | department | org | account | 0.8935 | no |
| wrong | business | ft | 2 | department | org | account | 0.9765 | no |
| wrong | business | ft | 2 | description | account | text | 0.8728 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.5103 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.5613 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.9519 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9674 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.7146 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.7018 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9330 | no |
| wrong | business | ft | 2 | title | category | account | 0.5782 | no |
| wrong | business | ft | 2 | type de matériel | category | id | 0.5030 | no |
| critical | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.6793 | yes |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9408 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9643 | yes |
| unknown | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5157 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3841 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.2636 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4016 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4673 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9848 | no |
| unknown | business2 | blend50 | 1 | potential_epc_score_known | category | unknown | 0.4927 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5496 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4981 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4526 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5540 | no |
| unknown | business2 | blend50 | 1 | scheme_description | category | unknown | 0.4906 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4424 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4941 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4110 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3534 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4282 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9884 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.4991 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4965 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5059 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9915 | no |
| wrong | business2 | blend50 | 1 | monitor | id | category | 0.6798 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.7298 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.7693 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5979 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.7003 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.6765 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5821 | no |
| wrong | business2 | blend50 | 1 | total_floor_area_known | category | quantity | 0.5742 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9756 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7455 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9389 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.8593 | yes |
| other_ng | business2 | blend50 | 2 | d2 floorspace net sqm | other | amount | 0.5021 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3485 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.3994 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.3615 | no |
| unknown | business2 | blend50 | 2 | health service executive area | address | unknown | 0.4285 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.4637 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.5037 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9853 | no |
| unknown | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5387 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6013 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3662 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4936 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4883 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.3947 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3608 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4617 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9930 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.3854 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.6186 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.3561 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4920 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5110 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9913 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5825 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.6532 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.7145 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5296 | no |
| wrong | business2 | blend50 | 2 | numéro | id | address | 0.6459 | no |
| wrong | business2 | blend50 | 2 | numéro_de_lot | id | address | 0.5007 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.7536 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.7113 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.6704 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5006 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.6745 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.7215 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9440 | no |
| critical | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | amount | 0.6442 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9492 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9574 | yes |
| unknown | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5376 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.4469 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.3014 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4489 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.4934 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9827 | no |
| unknown | business2 | blend60 | 1 | potential_epc_score_known | category | unknown | 0.4708 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4969 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.4357 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.4035 | no |
| unknown | business2 | blend60 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6164 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4686 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3706 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3735 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9891 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5904 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5879 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6011 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9907 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5712 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.7247 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6800 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7310 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6583 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.6762 | no |
| wrong | business2 | blend60 | 1 | service | account | org | 0.5047 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.6313 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.5193 | no |
| wrong | business2 | blend60 | 1 | total_floor_area_known | category | quantity | 0.5888 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9747 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.7414 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9401 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.8318 | yes |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4000 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.3845 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3061 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.5110 | no |
| unknown | business2 | blend60 | 2 | health service executive area | address | unknown | 0.4329 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.3942 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9831 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4986 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4359 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4556 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4261 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4994 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.3429 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5471 | no |
| unknown | business2 | blend60 | 2 | tree type | category | unknown | 0.3780 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5868 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6050 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9903 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6532 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.5915 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.6718 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6105 | no |
| wrong | business2 | blend60 | 2 | numéro | id | address | 0.6303 | no |
| wrong | business2 | blend60 | 2 | numéro_de_lot | id | address | 0.5492 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7909 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7556 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.7229 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.6657 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6771 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9420 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9577 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9506 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6817 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | amount | 0.6008 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6092 | no |
| unknown | business2 | blend70 | 1 | # invoices paid within 5 days | quantity | unknown | 0.5998 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.3392 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.4962 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.5661 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9806 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.4489 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5637 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.3733 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.3544 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4319 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4197 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9886 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9887 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9867 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9899 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.5097 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6663 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.7696 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6303 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.6926 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7187 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.6520 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.5887 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5860 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.5053 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.6034 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9738 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.7373 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9413 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.8044 | yes |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4515 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4089 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3563 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.5889 | no |
| unknown | business2 | blend70 | 2 | habitatdescription | text | unknown | 0.4514 | no |
| unknown | business2 | blend70 | 2 | health service executive area | address | unknown | 0.4373 | no |
| unknown | business2 | blend70 | 2 | imd19_income_decile | category | unknown | 0.3386 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9808 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4902 | no |
| unknown | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5954 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4914 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.5774 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9910 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.3797 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5124 | no |
| unknown | business2 | blend70 | 2 | tree type | category | unknown | 0.4381 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9892 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.5125 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7239 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.5299 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.6291 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6913 | no |
| wrong | business2 | blend70 | 2 | numéro | id | address | 0.6146 | no |
| wrong | business2 | blend70 | 2 | numéro_de_lot | id | address | 0.5977 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.8283 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7999 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7754 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5056 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6569 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.6327 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9399 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9831 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9300 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9557 | yes |
| other_ng | business2 | ft | 1 | average bids per property | other | amount | 0.8445 | no |
| unknown | business2 | ft | 1 | # invoices paid within 30 days | quantity | unknown | 0.5039 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.4527 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.7840 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9743 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.3832 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.4318 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.4557 | no |
| unknown | business2 | ft | 1 | scheme | id | unknown | 0.4841 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5583 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9849 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9844 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9833 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9843 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9875 | no |
| unknown | business2 | ft | 1 | want to live in this parish & band d | quantity | unknown | 0.4523 | no |
| unknown | business2 | ft | 1 | want to live in this parish only | quantity | unknown | 0.4980 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.6982 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.6159 | no |
| wrong | business2 | ft | 1 | fine | amount | category | 0.6381 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9514 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.9043 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.5775 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9000 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.5796 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.8407 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.7019 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.6161 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.6471 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9711 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.7250 | no |
| wrong | business2 | ft | 1 | état | category | account | 0.6009 | no |
| critical | business2 | ft | 2 | fine | amount | rate | 0.5068 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9449 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.7222 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.7222 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | amount | 0.7209 | no |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.5735 | no |
| other_ng | business2 | ft | 2 | potential_epc_score | other | rate | 0.5380 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.8224 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.6448 | no |
| unknown | business2 | ft | 2 | health service executive area | address | unknown | 0.4504 | no |
| unknown | business2 | ft | 2 | imd19_income_decile | category | unknown | 0.4837 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9741 | no |
| unknown | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5115 | no |
| unknown | business2 | ft | 2 | situtation | address | unknown | 0.4994 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6873 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.8115 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4901 | no |
| unknown | business2 | ft | 2 | tree type | category | unknown | 0.6184 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9862 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.5697 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.5510 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.7321 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9360 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.5009 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9338 | no |
| wrong | business2 | ft | 2 | numéro | id | address | 0.5677 | no |
| wrong | business2 | ft | 2 | numéro_de_lot | id | address | 0.7430 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.9402 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9329 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9329 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.7147 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6305 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9336 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.7752 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.5531 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5916 | no |
| unknown | dev220 | blend50 | 1 | ポイント | amount | unknown | 0.6038 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4956 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4882 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4881 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4815 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8882 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.6010 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5263 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.5175 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.6110 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.6285 | yes |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.5968 | no |
| unknown | dev220 | blend50 | 2 | item description | text | unknown | 0.4812 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4940 | no |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4982 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4996 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4927 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4914 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.8390 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.7906 | no |
| wrong | dev220 | blend50 | 2 | 随意契約理由 | text | category | 0.5136 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8009 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.5788 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8907 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6706 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.5341 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.6737 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.6036 | yes |
| unknown | dev220 | blend60 | 2 | 担当課 | org | unknown | 0.4866 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.8189 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.8097 | no |
| wrong | dev220 | blend60 | 2 | 随意契約理由 | text | category | 0.5875 | no |
| critical | dev220 | blend70 | 1 | credit limit | amount | quantity | 0.6045 | yes |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8266 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8932 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7402 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.5507 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7365 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.5787 | yes |
| unknown | dev220 | blend70 | 2 | 担当課 | org | unknown | 0.4888 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.7988 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.8289 | no |
| wrong | dev220 | blend70 | 2 | 随意契約理由 | text | category | 0.6614 | no |
| critical | dev220 | ft | 1 | credit limit | amount | quantity | 0.6815 | yes |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9036 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9008 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9489 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.6005 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9247 | no |
| unknown | dev220 | ft | 2 | purchase order by customer | id | unknown | 0.5040 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.7385 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.8864 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.6291 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.8831 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.5335 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.6887 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.8168 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9758 | no |
| other_ng | general | blend50 | 1 | 被害域幅(m)最小 | other | quantity | 0.5044 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.5073 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.5607 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.5751 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6412 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.7573 | no |
| unknown | general | blend50 | 1 | mechanism | category | unknown | 0.4842 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4734 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.3065 | no |
| unknown | general | blend50 | 1 | source | category | unknown | 0.4888 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.2920 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4867 | no |
| unknown | general | blend50 | 1 | 東第5 | quantity | unknown | 0.5595 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9661 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4023 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9936 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8451 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3601 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5543 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5472 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.6054 | no |
| wrong | general | blend50 | 1 | indicator | text | category | 0.7353 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.8409 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8712 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.5850 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7224 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.9264 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.8042 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.7073 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8648 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8959 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4975 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.5391 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5795 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9231 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4707 | no |
| unknown | general | blend50 | 2 | mechanism | category | unknown | 0.4874 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4740 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4282 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4151 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4490 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.3131 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4928 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4937 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9852 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4564 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9933 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9156 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3793 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.5630 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.6392 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.6127 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9335 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8967 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8295 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.7918 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6143 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.6610 | no |
| other_ng | general | blend60 | 1 | mt2 | other | category | 0.5395 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.7894 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9710 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.4854 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4716 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4633 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.6563 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.7101 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.7680 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3614 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4403 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4365 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3481 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3978 | no |
| unknown | general | blend60 | 1 | 東第5 | quantity | unknown | 0.4964 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9702 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4026 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9923 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8264 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.3701 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5824 | no |
| wrong | general | blend60 | 1 | indicator | text | category | 0.7178 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.8540 | no |
| wrong | general | blend60 | 1 | mechanism | category | id | 0.5369 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8591 | no |
| wrong | general | blend60 | 1 | raw | category | text | 0.5179 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7285 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.9330 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5458 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.5649 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.7981 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.6552 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8502 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.8753 | no |
| unknown | general | blend60 | 2 | author | person | unknown | 0.4915 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.6223 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6609 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9344 | no |
| unknown | general | blend60 | 2 | lda | text | unknown | 0.4760 | no |
| unknown | general | blend60 | 2 | mechanism | category | unknown | 0.4774 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4103 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.3488 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5677 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.3740 | no |
| unknown | general | blend60 | 2 | standardhours | quantity | unknown | 0.4751 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.3392 | no |
| unknown | general | blend60 | 2 | データセット_キーワード | category | unknown | 0.4979 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3972 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9857 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9919 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9243 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.3996 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.5803 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5809 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9291 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.9036 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.8434 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7654 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5475 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6952 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.6332 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.6266 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.5115 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.7621 | no |
| other_ng | general | blend70 | 1 | ブロモホルム | other | quantity | 0.5792 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9663 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.5505 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.3794 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.7375 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7789 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.7787 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4164 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.4509 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5465 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4186 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.3591 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.4043 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3847 | no |
| unknown | general | blend70 | 1 | 東第5 | quantity | unknown | 0.5791 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9743 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.4694 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9910 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8077 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3835 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.5593 | no |
| wrong | general | blend70 | 1 | indicator | text | category | 0.7003 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.8671 | no |
| wrong | general | blend70 | 1 | mechanism | category | id | 0.5896 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8470 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.7345 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.9396 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6357 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.6489 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.7919 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.6031 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8356 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.8546 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.7054 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7424 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9457 | no |
| unknown | general | blend70 | 2 | lda | text | unknown | 0.4813 | no |
| unknown | general | blend70 | 2 | mechanism | category | unknown | 0.4674 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.4773 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.4006 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6607 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.4187 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.4341 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.3908 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3401 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9862 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9906 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9329 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4525 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5213 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.5492 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9247 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.9106 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8573 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7390 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.5772 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6385 | no |
| critical | general | ft | 1 | age_q3 | quantity | rate | 0.7459 | yes |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.5381 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9376 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.5500 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.6295 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.8877 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.7083 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.6800 | no |
| other_ng | general | ft | 1 | ブロモホルム | other | quantity | 0.8264 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9520 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9811 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9854 | no |
| unknown | general | ft | 1 | goal | id | unknown | 0.4901 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.8106 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.5811 | no |
| unknown | general | ft | 1 | raw | category | unknown | 0.3956 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.7787 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.3566 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.5493 | no |
| unknown | general | ft | 1 | 東第5 | quantity | unknown | 0.8272 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9867 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9872 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.7516 | no |
| wrong | general | ft | 1 | indicator | text | category | 0.6477 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9064 | no |
| wrong | general | ft | 1 | mechanism | category | id | 0.7476 | no |
| wrong | general | ft | 1 | place | org | address | 0.8108 | no |
| wrong | general | ft | 1 | source | category | text | 0.5717 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.7527 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9592 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9053 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9010 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.7733 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.7066 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.7918 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.7925 | no |
| unknown | general | ft | 2 | cleaned | text | unknown | 0.4592 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9549 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9869 | no |
| unknown | general | ft | 2 | goal | id | unknown | 0.4644 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9794 | no |
| unknown | general | ft | 2 | lda | text | unknown | 0.4972 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.6785 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9396 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.5969 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4477 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.4184 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.4856 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9876 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9866 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9590 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9114 | no |
| wrong | general | ft | 2 | mechanism | category | id | 0.5185 | no |
| wrong | general | ft | 2 | organization name | org | person | 0.5806 | no |
| wrong | general | ft | 2 | place | org | address | 0.9316 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.8991 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.6598 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8151 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9118 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.6112 | no |

### unknown の判定理由

- date_value_evidence_low: 74件
- numeric_top2_too_close: 46件
- numeric_values_not_parseable: 16件
- other_class: 68件
- probability_below_threshold: 210件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 43件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 164件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 101件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
