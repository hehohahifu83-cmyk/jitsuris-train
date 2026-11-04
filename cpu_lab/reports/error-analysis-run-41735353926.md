# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-11-04T00:12:46+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 4 | 0 | 16 | 0 |
| business | blend50 | 2 | 490 | 4 | 0 | 18 | 0 |
| business | blend60 | 1 | 490 | 5 | 0 | 10 | 0 |
| business | blend60 | 2 | 490 | 4 | 0 | 10 | 0 |
| business | blend70 | 1 | 490 | 6 | 0 | 6 | 0 |
| business | blend70 | 2 | 490 | 4 | 0 | 7 | 0 |
| business | ft | 1 | 490 | 6 | 0 | 5 | 0 |
| business | ft | 2 | 490 | 5 | 0 | 5 | 0 |
| business2 | blend50 | 1 | 976 | 12 | 2 | 27 | 2 |
| business2 | blend50 | 2 | 976 | 14 | 2 | 29 | 2 |
| business2 | blend60 | 1 | 976 | 10 | 1 | 24 | 0 |
| business2 | blend60 | 2 | 976 | 11 | 2 | 23 | 1 |
| business2 | blend70 | 1 | 976 | 15 | 3 | 16 | 0 |
| business2 | blend70 | 2 | 976 | 13 | 3 | 19 | 1 |
| business2 | ft | 1 | 976 | 16 | 3 | 14 | 0 |
| business2 | ft | 2 | 976 | 12 | 3 | 17 | 1 |
| dev220 | blend50 | 1 | 220 | 5 | 1 | 9 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 1 | 10 | 0 |
| dev220 | blend60 | 1 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 4 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | ft | 2 | 220 | 5 | 1 | 1 | 0 |
| general | blend50 | 1 | 383 | 10 | 0 | 14 | 7 |
| general | blend50 | 2 | 383 | 8 | 0 | 15 | 6 |
| general | blend60 | 1 | 383 | 8 | 0 | 14 | 6 |
| general | blend60 | 2 | 383 | 9 | 0 | 11 | 6 |
| general | blend70 | 1 | 383 | 9 | 0 | 10 | 6 |
| general | blend70 | 2 | 383 | 10 | 1 | 10 | 7 |
| general | ft | 1 | 383 | 10 | 0 | 11 | 7 |
| general | ft | 2 | 383 | 9 | 1 | 10 | 7 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: text→category: 2, text→account: 2, category→text: 2, account→category: 1, account→text: 1
- business / blend60: text→category: 2, text→account: 2, category→text: 2, account→category: 1, category→id: 1, account→text: 1
- business / blend70: text→category: 2, account→text: 2, text→account: 2, category→text: 2, account→category: 1, category→id: 1
- business / ft: text→category: 2, account→text: 2, text→account: 2, category→text: 2, account→category: 1, category→id: 1, org→address: 1
- business2 / blend50: account→category: 4, address→category: 4, amount→quantity: 4, id→address: 3, quantity→category: 2, category→quantity: 2, category→text: 2, org→address: 2
- business2 / blend60: account→category: 4, address→category: 4, amount→quantity: 3, category→quantity: 2, org→address: 2, id→address: 2, quantity→category: 1, address→org: 1
- business2 / blend70: account→category: 4, address→category: 4, account→org: 3, amount→quantity: 3, id→category: 2, category→quantity: 2, quantity→amount: 2, org→address: 2
- business2 / ft: category→quantity: 4, account→org: 3, account→category: 3, address→category: 3, amount→quantity: 3, id→category: 2, quantity→amount: 2, address→text: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, id→quantity: 2, category→tax_class: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, id→quantity: 2
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, rate→tax_class: 1, text→category: 1
- general / blend50: org→address: 6, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1, address→org: 1
- general / blend60: org→address: 5, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1, address→org: 1, person→org: 1
- general / blend70: org→address: 5, category→text: 3, quantity→category: 2, id→category: 2, category→quantity: 1, id→address: 1, address→org: 1, person→org: 1
- general / ft: category→text: 4, org→address: 4, quantity→category: 2, id→category: 2, category→quantity: 1, id→address: 1, address→org: 1, text→account: 1

### seedをまたいで再発した誤り

- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `title`、category→text（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `title`、category→text（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
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
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service`、account→org（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `total_verified_sales`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
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
- general / blend50: `author`、person→org（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `goal`、id→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `place`、org→address（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `ステーション名`、org→address（seed 1, seed 2）
- general / blend50: `名称_カナ`、org→address（seed 1, seed 2）
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `名称_カナ`、org→address（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `名称_カナ`、org→address（seed 1, seed 2）
- general / ft: `goal`、id→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `名称_カナ`、org→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5078 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.4845 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5806 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4452 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5638 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6708 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5343 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5351 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4521 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.5436 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.4137 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4449 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9851 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5030 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9485 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8900 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.5901 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9444 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5504 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.5961 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5407 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5811 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4338 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4681 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5654 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6660 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5354 | no |
| unknown | business | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5961 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5359 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4924 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.5579 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.3806 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4686 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9789 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.4126 | no |
| unknown | business | blend50 | 2 | total invoices paid | quantity | unknown | 0.5232 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.8833 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.8745 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.5277 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.7442 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8343 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.6582 | no |
| unknown | business | blend60 | 1 | abn | id | unknown | 0.5872 | no |
| unknown | business | blend60 | 1 | description | account | unknown | 0.4969 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7343 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4991 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4010 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.4085 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9856 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5918 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9455 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9024 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5507 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.5892 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9420 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5988 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.6194 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3673 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.7284 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5857 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.3686 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.3851 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9782 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4669 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5663 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.8674 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.8838 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.6008 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.7740 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8099 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.6939 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7977 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3883 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4753 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9862 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9426 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9147 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.5528 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6407 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.5883 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9396 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6473 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.6427 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3499 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7909 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4283 | no |
| unknown | business | blend70 | 2 | publisher label | org | unknown | 0.3863 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9776 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.8514 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8931 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6740 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.8039 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.7855 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.7296 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9879 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.3500 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9880 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9339 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9518 | no |
| wrong | business | ft | 1 | description | account | text | 0.7203 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9105 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.5856 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9324 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.7927 | no |
| wrong | business | ft | 1 | title | category | text | 0.7125 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4305 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9782 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9756 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.8036 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9209 | no |
| wrong | business | ft | 2 | description | account | text | 0.8935 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.8936 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.5132 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7123 | no |
| wrong | business | ft | 2 | title | category | text | 0.8367 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9615 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6135 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5029 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.5313 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.3160 | no |
| unknown | business2 | blend50 | 1 | cost centre description | account | unknown | 0.4092 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3777 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3861 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4255 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5351 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5341 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4825 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9658 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5068 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4284 | no |
| unknown | business2 | blend50 | 1 | surveyname | text | unknown | 0.4923 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4877 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4825 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4837 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9925 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9924 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5027 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.7484 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5343 | no |
| unknown | business2 | blend50 | 1 | tree type | category | unknown | 0.4013 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4955 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5344 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9912 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5859 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.6967 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.8270 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5382 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.7350 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5018 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.6470 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.7570 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.8943 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7999 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9751 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8733 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.5042 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8082 | no |
| unknown | business2 | blend50 | 2 | amt-units_mnt-unite | category | unknown | 0.3901 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4532 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.2532 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5361 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5959 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5349 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4424 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9849 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4956 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5800 | no |
| unknown | business2 | blend50 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.6091 | no |
| unknown | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.6077 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4405 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.4907 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4858 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4745 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4763 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9901 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9880 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.5196 | no |
| unknown | business2 | blend50 | 2 | total_floor_area_known | category | unknown | 0.3812 | no |
| unknown | business2 | blend50 | 2 | total_verified_sales | quantity | unknown | 0.5142 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4858 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4978 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5201 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9908 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.7584 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5477 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7381 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.5723 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5774 | no |
| wrong | business2 | blend50 | 2 | numéro | id | address | 0.5013 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.7133 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5065 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.8854 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6931 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9406 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.7800 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9588 | yes |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.3335 | no |
| unknown | business2 | blend60 | 1 | cost centre description | account | unknown | 0.4801 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4225 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.4610 | no |
| unknown | business2 | blend60 | 1 | monitor | id | unknown | 0.4822 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9595 | no |
| unknown | business2 | blend60 | 1 | potential_epc_rating_known | category | unknown | 0.4855 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5494 | no |
| unknown | business2 | blend60 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5730 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4999 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3916 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5682 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.5734 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9906 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5922 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.7657 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5506 | no |
| unknown | business2 | blend60 | 1 | tree type | category | unknown | 0.4788 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5834 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9906 | no |
| wrong | business2 | blend60 | 1 | health service executive area | address | org | 0.6331 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6403 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.7997 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6060 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.7720 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.5857 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.7203 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.8761 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.8120 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9751 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8612 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8014 | no |
| unknown | business2 | blend60 | 2 | amt-units_mnt-unite | category | unknown | 0.4324 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4435 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.2944 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.4266 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.4941 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4596 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9824 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.4688 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3986 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3979 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.4044 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9871 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5709 | no |
| unknown | business2 | blend60 | 2 | total_floor_area_known | category | unknown | 0.3482 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5761 | no |
| unknown | business2 | blend60 | 2 | tree type | category | unknown | 0.4695 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5959 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6077 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9901 | no |
| wrong | business2 | blend60 | 2 | merchant description | category | org | 0.7417 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6288 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.6899 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6530 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7461 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.8717 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.6436 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9316 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.7880 | no |
| critical | business2 | blend70 | 1 | fine | amount | rate | 0.5358 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9560 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6411 | yes |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.3510 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4674 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9532 | no |
| unknown | business2 | blend70 | 1 | potential_epc_rating_known | category | unknown | 0.4618 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4916 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.3776 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6538 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.6631 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9905 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9900 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9902 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.7831 | no |
| unknown | business2 | blend70 | 1 | tree type | category | unknown | 0.5563 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9901 | no |
| wrong | business2 | blend70 | 1 | cost centre description | account | org | 0.5510 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.6803 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.5389 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.5838 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.7725 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6739 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.8091 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.5830 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5243 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.6837 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.8579 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.8240 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9751 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8490 | yes |
| critical | business2 | blend70 | 2 | total_verified_sales | quantity | amount | 0.6708 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.7946 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4747 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4338 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3391 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.3430 | no |
| unknown | business2 | blend70 | 2 | habitatdescription | text | unknown | 0.4647 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.5608 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.5350 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9800 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.4643 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3459 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4659 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9865 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9852 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9838 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9894 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.3657 | no |
| unknown | business2 | blend70 | 2 | tree type | category | unknown | 0.4532 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9895 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.7249 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7100 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.6418 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7287 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7788 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.5468 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.8580 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.5942 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9227 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.7960 | no |
| critical | business2 | ft | 1 | fine | amount | rate | 0.7604 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9478 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9125 | yes |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.4035 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.4986 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9345 | no |
| unknown | business2 | ft | 1 | potential_epc_rating_known | category | unknown | 0.3905 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.9109 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.9322 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9883 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9867 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.8352 | no |
| unknown | business2 | ft | 1 | tree type | category | unknown | 0.7887 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9884 | no |
| wrong | business2 | ft | 1 | cost centre description | account | org | 0.7638 | no |
| wrong | business2 | ft | 1 | descript | address | text | 0.5207 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.6020 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.8220 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7090 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.6908 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8773 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.9203 | no |
| wrong | business2 | ft | 1 | potential_epc_score_known | category | quantity | 0.5120 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.8324 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.5737 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.8033 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.8600 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9751 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8126 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.9550 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.7742 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.4975 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4733 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.4262 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.5338 | no |
| unknown | business2 | ft | 2 | name | org | unknown | 0.4974 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.7962 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9727 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4710 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6505 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9869 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9812 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9796 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9776 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4416 | no |
| unknown | business2 | ft | 2 | tree type | category | unknown | 0.5500 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9876 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.6746 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9534 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9556 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.8770 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.7806 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.8170 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.5263 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.8958 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.8201 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8521 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.4789 | no |
| unknown | dev220 | blend50 | 1 | is a company | category | unknown | 0.4960 | no |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4761 | no |
| unknown | dev220 | blend50 | 1 | name | person | unknown | 0.4917 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4999 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4874 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4974 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4835 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4905 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9663 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.9322 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5249 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7374 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.7800 | yes |
| unknown | dev220 | blend50 | 2 | is a company | category | unknown | 0.4999 | no |
| unknown | dev220 | blend50 | 2 | name | person | unknown | 0.4912 | no |
| unknown | dev220 | blend50 | 2 | sales order | id | unknown | 0.4558 | no |
| unknown | dev220 | blend50 | 2 | sales tax group | tax_class | unknown | 0.4991 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4823 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4992 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4869 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4921 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4678 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4718 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9858 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9449 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7129 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8796 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.4811 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9629 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9388 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7555 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.7931 | yes |
| unknown | dev220 | blend60 | 2 | sales order | id | unknown | 0.4634 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9864 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9540 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7261 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9071 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.4833 | no |
| unknown | dev220 | blend70 | 1 | 税率 | rate | unknown | 0.4895 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9596 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9454 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7736 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.8062 | yes |
| unknown | dev220 | blend70 | 2 | sales order | id | unknown | 0.5370 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9869 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9632 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7393 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9897 | yes |
| unknown | dev220 | ft | 1 | credit limit | amount | unknown | 0.4899 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9495 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9654 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8280 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.6935 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.8456 | yes |
| unknown | dev220 | ft | 2 | sales order | id | unknown | 0.7576 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9886 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9908 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.7790 | no |
| wrong | dev220 | ft | 2 | 随意契約理由 | text | category | 0.6029 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6387 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.5275 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.6835 | no |
| other_ng | general | blend50 | 1 | operationid | other | id | 0.5494 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9241 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9194 | no |
| other_ng | general | blend50 | 1 | 被害域長さ(100m)最小 | other | quantity | 0.5023 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4677 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4960 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4853 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.6257 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.6974 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4648 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4176 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4409 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.3745 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4412 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9784 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4433 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9938 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9325 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5248 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5996 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.8344 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9333 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8327 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.5916 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.5116 | no |
| wrong | general | blend50 | 1 | 名称_カナ | org | address | 0.6947 | no |
| wrong | general | blend50 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.8351 | no |
| wrong | general | blend50 | 1 | 読み方 | address | org | 0.5012 | no |
| other_ng | general | blend50 | 2 | abstract rank | other | category | 0.5647 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.6293 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.5158 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.5693 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8713 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9725 | no |
| unknown | general | blend50 | 2 | authors | person | unknown | 0.4771 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4585 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.6265 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.7050 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4362 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4192 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4277 | no |
| unknown | general | blend50 | 2 | source | category | unknown | 0.4855 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4386 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4316 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9782 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4474 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9926 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9253 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4395 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.9140 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.7033 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8587 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9308 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.7679 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5657 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.5614 | no |
| wrong | general | blend50 | 2 | 名称_カナ | org | address | 0.7121 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6953 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.5313 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.6421 | no |
| other_ng | general | blend60 | 1 | operationid | other | id | 0.6071 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9243 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9033 | no |
| unknown | general | blend60 | 1 | author | person | unknown | 0.4788 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.5599 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6982 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.7339 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4216 | no |
| unknown | general | blend60 | 1 | raw | category | unknown | 0.4355 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4509 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3168 | no |
| unknown | general | blend60 | 1 | ステーション名 | org | unknown | 0.4853 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.3604 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9806 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.4604 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9926 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9350 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.5231 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.8254 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9402 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8125 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.6339 | no |
| wrong | general | blend60 | 1 | 名称_カナ | org | address | 0.7020 | no |
| wrong | general | blend60 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.8224 | no |
| wrong | general | blend60 | 1 | 読み方 | address | org | 0.5654 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.6445 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.6841 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5927 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.6309 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.8609 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9670 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.5493 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6991 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.7431 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.3903 | no |
| unknown | general | blend60 | 2 | source | category | unknown | 0.4645 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4817 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4661 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9804 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3598 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9912 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9263 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.9020 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6475 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.8545 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9372 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.7347 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5714 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.6028 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.5450 | no |
| wrong | general | blend60 | 2 | 名称_カナ | org | address | 0.7229 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7520 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.5351 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.6007 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.6648 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9244 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8873 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4466 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.6345 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7707 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.7705 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4917 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3639 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3577 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9828 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9914 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9375 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.8163 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9470 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7923 | no |
| wrong | general | blend70 | 1 | source_value | category | text | 0.5147 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6761 | no |
| wrong | general | blend70 | 1 | 名称_カナ | org | address | 0.7093 | no |
| wrong | general | blend70 | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.8096 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.5371 | no |
| wrong | general | blend70 | 1 | 読み方 | address | org | 0.6297 | no |
| critical | general | blend70 | 2 | denominatorunweighted | quantity | id | 0.6402 | yes |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.7244 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.7389 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.6894 | no |
| other_ng | general | blend70 | 2 | mt2 | other | category | 0.5763 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6926 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.8505 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9616 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7717 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.7812 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.4551 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.5511 | no |
| unknown | general | blend70 | 2 | source | category | unknown | 0.4592 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.4081 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9825 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.3669 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9897 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9273 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.8901 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.5918 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.8503 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9435 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7016 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6627 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6399 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.5287 | no |
| wrong | general | blend70 | 2 | 名称_カナ | org | address | 0.7337 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9220 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.5466 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.5583 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.6663 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.8378 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9249 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.8392 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.8582 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9881 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.8801 | no |
| unknown | general | ft | 1 | indicator | text | unknown | 0.4926 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.7019 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.5706 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4202 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4541 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9894 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9877 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9449 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.6094 | no |
| wrong | general | ft | 1 | goal | id | category | 0.7891 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9675 | no |
| wrong | general | ft | 1 | place | org | address | 0.7316 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.7232 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8028 | no |
| wrong | general | ft | 1 | 名称_カナ | org | address | 0.7313 | no |
| wrong | general | ft | 1 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.7714 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.7671 | no |
| wrong | general | ft | 1 | 読み方 | address | org | 0.8225 | no |
| critical | general | ft | 2 | denominatorunweighted | quantity | id | 0.9126 | yes |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.9639 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9033 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.9793 | no |
| other_ng | general | ft | 2 | mt2 | other | category | 0.8184 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.8775 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.8193 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9454 | no |
| unknown | general | ft | 2 | cleaned | text | unknown | 0.4970 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9896 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.8954 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.6496 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.7864 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.4044 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9890 | no |
| unknown | general | ft | 2 | 発生県 | id | unknown | 0.5237 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9853 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9303 | no |
| wrong | general | ft | 2 | author | person | org | 0.8542 | no |
| wrong | general | ft | 2 | goal | id | category | 0.8377 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9625 | no |
| wrong | general | ft | 2 | place | org | address | 0.6021 | no |
| wrong | general | ft | 2 | source | category | org | 0.9366 | no |
| wrong | general | ft | 2 | source | category | text | 0.5883 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.7511 | no |
| wrong | general | ft | 2 | 名称_カナ | org | address | 0.7660 | no |

### unknown の判定理由

- date_value_evidence_low: 74件
- numeric_top2_too_close: 46件
- numeric_values_not_parseable: 18件
- other_class: 63件
- probability_below_threshold: 166件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 29件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 137件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 102件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
