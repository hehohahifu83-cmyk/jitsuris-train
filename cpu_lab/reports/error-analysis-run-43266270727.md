# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-11-12T18:31:06+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 5 | 1 | 20 | 0 |
| business | blend50 | 2 | 490 | 3 | 1 | 22 | 0 |
| business | blend60 | 1 | 490 | 6 | 1 | 10 | 0 |
| business | blend60 | 2 | 490 | 3 | 1 | 15 | 0 |
| business | blend70 | 1 | 490 | 7 | 1 | 8 | 0 |
| business | blend70 | 2 | 490 | 5 | 1 | 10 | 0 |
| business | ft | 1 | 490 | 7 | 1 | 5 | 0 |
| business | ft | 2 | 490 | 8 | 1 | 6 | 0 |
| business2 | blend50 | 1 | 976 | 13 | 2 | 26 | 2 |
| business2 | blend50 | 2 | 976 | 14 | 3 | 27 | 1 |
| business2 | blend60 | 1 | 976 | 13 | 2 | 21 | 1 |
| business2 | blend60 | 2 | 976 | 12 | 3 | 22 | 0 |
| business2 | blend70 | 1 | 976 | 14 | 3 | 18 | 1 |
| business2 | blend70 | 2 | 976 | 15 | 4 | 15 | 0 |
| business2 | ft | 1 | 976 | 14 | 3 | 14 | 0 |
| business2 | ft | 2 | 976 | 16 | 2 | 14 | 1 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 10 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 0 | 13 | 0 |
| dev220 | blend60 | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | blend60 | 2 | 220 | 6 | 0 | 3 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 0 | 3 | 0 |
| dev220 | ft | 1 | 220 | 7 | 1 | 5 | 0 |
| dev220 | ft | 2 | 220 | 9 | 0 | 2 | 0 |
| general | blend50 | 1 | 383 | 9 | 0 | 14 | 5 |
| general | blend50 | 2 | 383 | 9 | 0 | 14 | 6 |
| general | blend60 | 1 | 383 | 8 | 0 | 10 | 5 |
| general | blend60 | 2 | 383 | 9 | 0 | 12 | 6 |
| general | blend70 | 1 | 383 | 5 | 0 | 14 | 9 |
| general | blend70 | 2 | 383 | 12 | 1 | 9 | 5 |
| general | ft | 1 | 383 | 7 | 0 | 14 | 8 |
| general | ft | 2 | 383 | 14 | 1 | 10 | 5 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: quantity→amount: 2, text→account: 2, text→category: 1, product→text: 1, category→account: 1, org→account: 1
- business / blend60: quantity→amount: 2, text→account: 2, text→category: 1, account→category: 1, category→account: 1, category→text: 1, org→address: 1
- business / blend70: quantity→amount: 2, text→account: 2, category→id: 2, category→account: 2, text→category: 1, account→category: 1, category→text: 1, org→address: 1
- business / ft: category→id: 3, category→account: 3, quantity→amount: 2, text→account: 2, text→category: 1, account→category: 1, category→text: 1, org→address: 1
- business2 / blend50: account→category: 5, category→id: 4, category→text: 3, id→address: 3, amount→quantity: 3, quantity→amount: 2, quantity→category: 2, category→quantity: 2
- business2 / blend60: account→category: 5, category→id: 3, id→address: 3, amount→quantity: 3, quantity→amount: 2, category→quantity: 2, address→text: 2, category→text: 2
- business2 / blend70: account→category: 5, quantity→amount: 4, category→id: 3, id→address: 3, amount→quantity: 3, category→quantity: 2, address→text: 2, quantity→address: 2
- business2 / ft: account→category: 4, category→id: 4, quantity→amount: 3, quantity→address: 3, category→quantity: 3, address→text: 2, id→address: 2, amount→quantity: 2
- dev220 / blend50: quantity→category: 4, org→account: 3, id→quantity: 1, category→tax_class: 1, address→id: 1
- dev220 / blend60: quantity→category: 4, org→account: 3, address→id: 2, org→address: 1, id→quantity: 1, category→text: 1
- dev220 / blend70: quantity→category: 4, org→account: 3, address→id: 2, org→address: 1, id→quantity: 1, text→category: 1, category→text: 1
- dev220 / ft: quantity→category: 4, address→id: 3, org→account: 2, text→category: 2, org→address: 2, category→text: 2, id→quantity: 1
- general / blend50: org→address: 6, person→org: 2, category→text: 2, quantity→category: 2, address→text: 2, text→category: 2, id→category: 2
- general / blend60: org→address: 6, category→text: 2, quantity→category: 2, address→text: 2, text→category: 2, id→category: 2, person→org: 1
- general / blend70: category→text: 5, org→address: 4, quantity→category: 2, text→category: 2, person→org: 1, quantity→id: 1, address→text: 1, id→category: 1
- general / ft: category→text: 6, org→address: 4, text→category: 3, quantity→category: 2, id→address: 1, person→org: 1, quantity→id: 1, address→text: 1

### seedをまたいで再発した誤り

- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `ligne`、category→id（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `sub_category`、category→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `sub_category`、category→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `projection`、category→id（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `projection`、category→id（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→text（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→text（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `conservation_area_site_id`、category→id（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `担当課`、org→account（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `location`、org→address（seed 1, seed 2）
- dev220 / ft: `payment terms`、category→text（seed 1, seed 2）
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
- general / blend50: `名称_カナ`、org→address（seed 1, seed 2）
- general / blend50: `読み方`、address→text（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `名称_カナ`、org→address（seed 1, seed 2）
- general / blend60: `読み方`、address→text（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `source_value`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `source`、category→text（seed 1, seed 2）
- general / ft: `source_value`、category→text（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.8635 | yes |
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6090 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5414 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.4805 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5771 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4010 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.6048 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5063 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6207 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5350 | no |
| unknown | business | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5790 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5340 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4771 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3724 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4517 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9607 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4437 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.4952 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4733 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9805 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9397 | no |
| wrong | business | blend50 | 1 | commodity-title_en | product | text | 0.5206 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.5422 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.8896 | no |
| wrong | business | blend50 | 1 | sub_category | category | account | 0.5103 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.8217 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5518 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6228 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5432 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.4960 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5434 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4694 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.6058 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.5093 | no |
| unknown | business | blend50 | 2 | merchant details | text | unknown | 0.4418 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6217 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5321 | no |
| unknown | business | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5719 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5287 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4772 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5707 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4789 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9588 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.4376 | no |
| unknown | business | blend50 | 2 | segment-title_en | category | unknown | 0.4274 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4206 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9670 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9525 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5134 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8009 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.8364 | yes |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4406 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4004 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6918 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5247 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4424 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3888 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9663 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4582 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9803 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9385 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.5500 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8818 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5545 | no |
| wrong | business | blend60 | 1 | sub_category | category | account | 0.5609 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.5062 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.7863 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6136 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4493 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4361 | no |
| unknown | business | blend60 | 2 | ligne | category | unknown | 0.4993 | no |
| unknown | business | blend60 | 2 | merchant details | text | unknown | 0.4295 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6930 | no |
| unknown | business | blend60 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.6186 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.4465 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4732 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9639 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4642 | no |
| unknown | business | blend60 | 2 | segment-title_en | category | unknown | 0.4784 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.4243 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9641 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9538 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5563 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.7754 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.8094 | yes |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4305 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4470 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7628 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4530 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9718 | no |
| unknown | business | blend70 | 1 | regrp_nom | account | unknown | 0.4728 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9801 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9372 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.5045 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.5577 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.8740 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6138 | no |
| wrong | business | blend70 | 1 | sub_category | category | account | 0.6116 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.5392 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.7509 | yes |
| unknown | business | blend70 | 2 | entitiy | org | unknown | 0.3892 | no |
| unknown | business | blend70 | 2 | merchant details | text | unknown | 0.4171 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7643 | no |
| unknown | business | blend70 | 2 | overseas sourced goods | amount | unknown | 0.5187 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4330 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9691 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4908 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.4882 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9612 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9552 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.5204 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.6336 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.7498 | no |
| wrong | business | blend70 | 2 | sub_category | category | account | 0.5216 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.7284 | yes |
| unknown | business | ft | 1 | entitiy | org | unknown | 0.4976 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9760 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9884 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9796 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9335 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.7036 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.5809 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.8506 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.7916 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.7635 | no |
| wrong | business | ft | 1 | title | category | text | 0.6381 | no |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.6448 | yes |
| unknown | business | ft | 2 | merchant details | text | unknown | 0.4597 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9781 | no |
| unknown | business | ft | 2 | portefeuille_nom_et_code | org | unknown | 0.4111 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9845 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9525 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9591 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.5542 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.7263 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.8657 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.6732 | no |
| wrong | business | ft | 2 | q3_2 | category | id | 0.5218 | no |
| wrong | business | ft | 2 | sub_category | category | account | 0.6349 | no |
| wrong | business | ft | 2 | title | category | account | 0.6799 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9561 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.8450 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5209 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.7267 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6099 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.4645 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.2142 | no |
| unknown | business2 | blend50 | 1 | merchant description | category | unknown | 0.4737 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5355 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5790 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5335 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4802 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9887 | no |
| unknown | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5082 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3053 | no |
| unknown | business2 | blend50 | 1 | situtation | address | unknown | 0.4890 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4953 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4854 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4247 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4937 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.3962 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5197 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4980 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5242 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9907 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.5577 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.8485 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5038 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.7360 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.9415 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.9026 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.6067 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.9545 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9168 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.5574 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.8132 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9565 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6973 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.7942 | yes |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.5968 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5411 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6221 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.4534 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.4698 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.3058 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5331 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5716 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5270 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4723 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9747 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3109 | no |
| unknown | business2 | blend50 | 2 | situtation | address | unknown | 0.4730 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4751 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4823 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4098 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4819 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9936 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.6086 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5317 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4982 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5221 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9910 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.4324 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5908 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.8022 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5221 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5325 | no |
| wrong | business2 | blend50 | 2 | numéro | id | address | 0.6438 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.7555 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5769 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5535 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5459 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7523 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9640 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9568 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.8142 | yes |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.6933 | no |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4853 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.5459 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.2396 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.4911 | no |
| unknown | business2 | blend60 | 1 | merchant description | category | unknown | 0.4406 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9866 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5893 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.2511 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3968 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4127 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4029 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.3826 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5714 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5961 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6160 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9910 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.8209 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.5891 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.7628 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.9453 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.9152 | no |
| wrong | business2 | blend60 | 1 | scheme_description | category | text | 0.5289 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.9584 | no |
| wrong | business2 | blend60 | 1 | situtation | address | text | 0.5272 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9023 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.5301 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.8388 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9574 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6682 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.7534 | yes |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6007 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.4925 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.3305 | no |
| unknown | business2 | blend60 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.6166 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5637 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9699 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4962 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3724 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.4034 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4565 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4710 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9929 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9898 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9896 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.6727 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5565 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5965 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6135 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4690 | no |
| wrong | business2 | blend60 | 2 | contravention | category | text | 0.6334 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7672 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6235 | no |
| wrong | business2 | blend60 | 2 | numéro | id | address | 0.6123 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7862 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5078 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7157 | no |
| wrong | business2 | blend60 | 2 | situtation | address | text | 0.5443 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9591 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9576 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.7835 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6661 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.6599 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.6313 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.2787 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.5671 | no |
| unknown | business2 | blend70 | 1 | merchant description | category | unknown | 0.4654 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9846 | no |
| unknown | business2 | blend70 | 1 | potential_epc_score_known | category | unknown | 0.4942 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4511 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.2924 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4622 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4810 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3638 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9889 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.3690 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9913 | no |
| wrong | business2 | blend70 | 1 | conservation_area_site_id | category | id | 0.5657 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.7933 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6743 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7896 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.9491 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.9277 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.9623 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6034 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8879 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.5028 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.8643 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9582 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6390 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.7125 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6487 | yes |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.3551 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6563 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9651 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4968 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4704 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4338 | no |
| unknown | business2 | blend70 | 2 | tenure_known | category | unknown | 0.4959 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4699 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9884 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.7369 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9918 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.6759 | no |
| wrong | business2 | blend70 | 2 | fine | amount | category | 0.5152 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.7322 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7145 | no |
| wrong | business2 | blend70 | 2 | numéro | id | address | 0.5808 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.8169 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6792 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.6234 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5322 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5494 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9541 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9599 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.6914 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9502 | yes |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.8875 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.3960 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.7951 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9785 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.6376 | no |
| unknown | business2 | ft | 1 | service | account | unknown | 0.4173 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5044 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9888 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9825 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9839 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.3287 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9923 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.8067 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.7106 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9300 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.8701 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9605 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9652 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9740 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8320 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.6860 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8446 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.9410 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9607 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9253 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | amount | 0.5837 | no |
| unknown | business2 | ft | 2 | monitor | id | unknown | 0.4422 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9342 | no |
| unknown | business2 | ft | 2 | numéro | id | unknown | 0.4981 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9506 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5515 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9845 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9840 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9836 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | ft | 2 | total invoices paid | quantity | unknown | 0.5900 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.9294 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9930 | no |
| unknown | business2 | ft | 2 | want to live in this parish & band d | quantity | unknown | 0.4556 | no |
| wrong | business2 | ft | 2 | conservation_area_site_id | category | id | 0.6017 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.8035 | no |
| wrong | business2 | ft | 2 | fine | amount | category | 0.5833 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.6042 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.6273 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9874 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.9091 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.6183 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.5695 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.8606 | no |
| wrong | business2 | ft | 2 | tenure_known | category | quantity | 0.6450 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.7591 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.7846 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9391 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8404 | yes |
| unknown | dev220 | blend50 | 1 | active | category | unknown | 0.4874 | no |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.4838 | no |
| unknown | dev220 | blend50 | 1 | primary contact | person | unknown | 0.4999 | no |
| unknown | dev220 | blend50 | 1 | taxable | category | unknown | 0.4856 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.6086 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4970 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4924 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4855 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4827 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4775 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9836 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.9504 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.8468 | no |
| wrong | dev220 | blend50 | 1 | 担当部局 | org | account | 0.5133 | no |
| unknown | dev220 | blend50 | 2 | credit limit | amount | unknown | 0.5349 | no |
| unknown | dev220 | blend50 | 2 | name | person | unknown | 0.4996 | no |
| unknown | dev220 | blend50 | 2 | payment terms | category | unknown | 0.4917 | no |
| unknown | dev220 | blend50 | 2 | primary contact | person | unknown | 0.4986 | no |
| unknown | dev220 | blend50 | 2 | purchase order by customer | id | unknown | 0.5152 | no |
| unknown | dev220 | blend50 | 2 | sales tax group | tax_class | unknown | 0.4836 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.6109 | no |
| unknown | dev220 | blend50 | 2 | ポイント | amount | unknown | 0.4003 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4959 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4920 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4961 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4274 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4886 | no |
| wrong | dev220 | blend50 | 2 | city | address | id | 0.5177 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9816 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9498 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.5231 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.6814 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8557 | yes |
| unknown | dev220 | blend60 | 1 | active | category | unknown | 0.5805 | no |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.4761 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9822 | no |
| wrong | dev220 | blend60 | 1 | location | org | address | 0.5268 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9578 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.8695 | no |
| wrong | dev220 | blend60 | 1 | 担当部局 | org | account | 0.5082 | no |
| unknown | dev220 | blend60 | 2 | credit limit | amount | unknown | 0.5590 | no |
| unknown | dev220 | blend60 | 2 | purchase order by customer | id | unknown | 0.4662 | no |
| unknown | dev220 | blend60 | 2 | ポイント | amount | unknown | 0.3944 | no |
| wrong | dev220 | blend60 | 2 | city | address | id | 0.6111 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9797 | no |
| wrong | dev220 | blend60 | 2 | payment terms | category | text | 0.5625 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9571 | no |
| wrong | dev220 | blend60 | 2 | 履行場所 | address | id | 0.5641 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.6710 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8710 | yes |
| unknown | dev220 | blend70 | 1 | active | category | unknown | 0.6772 | no |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.4798 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9807 | no |
| wrong | dev220 | blend70 | 1 | location | org | address | 0.6073 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9653 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8923 | no |
| wrong | dev220 | blend70 | 1 | 担当部局 | org | account | 0.5030 | no |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.5832 | no |
| unknown | dev220 | blend70 | 2 | purchase order by customer | id | unknown | 0.5149 | no |
| unknown | dev220 | blend70 | 2 | ポイント | amount | unknown | 0.3884 | no |
| wrong | dev220 | blend70 | 2 | city | address | id | 0.7045 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9779 | no |
| wrong | dev220 | blend70 | 2 | payment terms | category | text | 0.6333 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9644 | no |
| wrong | dev220 | blend70 | 2 | 履行場所 | address | id | 0.6551 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.6607 | no |
| wrong | dev220 | blend70 | 2 | 随意契約理由 | text | category | 0.5406 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9168 | yes |
| unknown | dev220 | ft | 1 | active | category | unknown | 0.9673 | no |
| unknown | dev220 | ft | 1 | credit limit | amount | unknown | 0.5080 | no |
| unknown | dev220 | ft | 1 | sales order | id | unknown | 0.5499 | no |
| unknown | dev220 | ft | 1 | 担当部局 | org | unknown | 0.4876 | no |
| unknown | dev220 | ft | 1 | 税率 | rate | unknown | 0.4844 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9763 | no |
| wrong | dev220 | ft | 1 | location | org | address | 0.8487 | no |
| wrong | dev220 | ft | 1 | payment terms | category | text | 0.5456 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9875 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9605 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.6834 | no |
| unknown | dev220 | ft | 2 | active | category | unknown | 0.3407 | no |
| unknown | dev220 | ft | 2 | ポイント | amount | unknown | 0.4602 | no |
| wrong | dev220 | ft | 2 | city | address | id | 0.9847 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9723 | no |
| wrong | dev220 | ft | 2 | location | org | address | 0.5674 | no |
| wrong | dev220 | ft | 2 | payment terms | category | text | 0.8458 | no |
| wrong | dev220 | ft | 2 | shipping address | address | id | 0.6341 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9863 | no |
| wrong | dev220 | ft | 2 | 履行場所 | address | id | 0.9280 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.6297 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.7655 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6009 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.5587 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.6229 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9394 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.7163 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4716 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5700 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.6570 | no |
| unknown | general | blend50 | 1 | lda | text | unknown | 0.4495 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4866 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4382 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4543 | no |
| unknown | general | blend50 | 1 | source | category | unknown | 0.4334 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4462 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.5122 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9881 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3361 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9931 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9681 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5251 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.8625 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.5731 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9633 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8610 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.5060 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.5234 | no |
| wrong | general | blend50 | 1 | 名称_カナ | org | address | 0.5751 | no |
| wrong | general | blend50 | 1 | 読み方 | address | text | 0.6021 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.5378 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.6172 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.5865 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9355 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9731 | no |
| other_ng | general | blend50 | 2 | 被害域長さ(100m)最小 | other | quantity | 0.5004 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4916 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4593 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5660 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.5625 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4632 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4623 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4569 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4391 | no |
| unknown | general | blend50 | 2 | source | category | unknown | 0.4199 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.3578 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9900 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3169 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9942 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9726 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.8702 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.8133 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.7404 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9636 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.9122 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5754 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.7242 | no |
| wrong | general | blend50 | 2 | 名称_カナ | org | address | 0.8532 | no |
| wrong | general | blend50 | 2 | 読み方 | address | text | 0.7722 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6653 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.5316 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.6341 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9452 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.6602 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.3843 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6540 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.6993 | no |
| unknown | general | blend60 | 1 | mechanism | category | unknown | 0.4788 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4152 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4262 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9884 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4032 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9918 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9652 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.8397 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.5037 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9650 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8392 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.5600 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.5072 | no |
| wrong | general | blend60 | 1 | 名称_カナ | org | address | 0.5202 | no |
| wrong | general | blend60 | 1 | 読み方 | address | text | 0.5329 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.5064 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5279 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.5732 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.6619 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9405 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9684 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.4744 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6492 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.5858 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5481 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5221 | no |
| unknown | general | blend60 | 2 | source | category | unknown | 0.4793 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4800 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4288 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9906 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.2537 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9930 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9706 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.8495 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.7807 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.7044 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9654 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.9006 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6433 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.7481 | no |
| wrong | general | blend60 | 2 | 名称_カナ | org | address | 0.8539 | no |
| wrong | general | blend60 | 2 | 読み方 | address | text | 0.7370 | no |
| other_ng | general | blend70 | 1 | _status_ | other | category | 0.5041 | no |
| other_ng | general | blend70 | 1 | abstract rank | other | category | 0.5263 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7297 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.5044 | no |
| other_ng | general | blend70 | 1 | episode | other | id | 0.6453 | no |
| other_ng | general | blend70 | 1 | mood | other | category | 0.5788 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.5627 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9510 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.6041 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.3237 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7380 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4342 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.7415 | no |
| unknown | general | blend70 | 1 | mechanism | category | unknown | 0.4546 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4843 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5062 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4505 | no |
| unknown | general | blend70 | 1 | ステーション名 | org | unknown | 0.4910 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9887 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.4702 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9904 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9623 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.4636 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.8169 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9667 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8174 | no |
| wrong | general | blend70 | 1 | source_value | category | text | 0.5033 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6140 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | id | 0.5528 | yes |
| other_ng | general | blend70 | 2 | mood | other | category | 0.6151 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.5292 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.7374 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9455 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9637 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7325 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.6092 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6393 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6084 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4998 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9913 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.2407 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9919 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9687 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.8289 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7481 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.6685 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9671 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8890 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.5388 | no |
| wrong | general | blend70 | 2 | source_value | category | text | 0.5574 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.7112 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7721 | no |
| wrong | general | blend70 | 2 | 名称_カナ | org | address | 0.8545 | no |
| wrong | general | blend70 | 2 | 読み方 | address | text | 0.7019 | no |
| other_ng | general | ft | 1 | _status_ | other | category | 0.7192 | no |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.7235 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9230 | no |
| other_ng | general | ft | 1 | episode | other | id | 0.6789 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.8250 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.8003 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.5839 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9684 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.6337 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.4346 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9901 | no |
| unknown | general | ft | 1 | goal | id | unknown | 0.3823 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.8682 | no |
| unknown | general | ft | 1 | mechanism | category | unknown | 0.3821 | no |
| unknown | general | ft | 1 | ngram | text | unknown | 0.4288 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.6915 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.7214 | no |
| unknown | general | ft | 1 | source | category | unknown | 0.4873 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9896 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9863 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9537 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.3533 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.7487 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9719 | no |
| wrong | general | ft | 1 | place | org | address | 0.7518 | no |
| wrong | general | ft | 1 | source | category | text | 0.5910 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.7122 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.7762 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.6713 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.7879 | yes |
| other_ng | general | ft | 2 | mood | other | category | 0.8768 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.5693 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9637 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9605 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9495 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9821 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.6792 | no |
| unknown | general | ft | 2 | mechanism | category | unknown | 0.4737 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9130 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.8675 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.7129 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9933 | no |
| unknown | general | ft | 2 | 発生県 | id | unknown | 0.3396 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9884 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9627 | no |
| wrong | general | ft | 2 | author | person | org | 0.7670 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.6504 | no |
| wrong | general | ft | 2 | cluster | category | id | 0.5061 | no |
| wrong | general | ft | 2 | goal | id | category | 0.5606 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9724 | no |
| wrong | general | ft | 2 | place | org | address | 0.8541 | no |
| wrong | general | ft | 2 | source | category | text | 0.7171 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.7895 | no |
| wrong | general | ft | 2 | term | text | category | 0.6506 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9150 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8440 | no |
| wrong | general | ft | 2 | 名称_カナ | org | address | 0.8565 | no |
| wrong | general | ft | 2 | 読み方 | address | text | 0.5963 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 57件
- numeric_values_not_parseable: 19件
- other_class: 65件
- probability_below_threshold: 177件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 36件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 147件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 112件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
