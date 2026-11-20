# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-11-20T09:20:14+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 7 | 0 | 19 | 0 |
| business | blend50 | 2 | 490 | 5 | 2 | 21 | 0 |
| business | blend60 | 1 | 490 | 7 | 0 | 12 | 0 |
| business | blend60 | 2 | 490 | 6 | 1 | 12 | 0 |
| business | blend70 | 1 | 490 | 6 | 0 | 10 | 0 |
| business | blend70 | 2 | 490 | 8 | 1 | 9 | 0 |
| business | ft | 1 | 490 | 8 | 0 | 6 | 0 |
| business | ft | 2 | 490 | 10 | 2 | 6 | 0 |
| business2 | blend50 | 1 | 976 | 13 | 2 | 27 | 2 |
| business2 | blend50 | 2 | 976 | 14 | 2 | 24 | 3 |
| business2 | blend60 | 1 | 976 | 11 | 1 | 25 | 1 |
| business2 | blend60 | 2 | 976 | 17 | 2 | 20 | 1 |
| business2 | blend70 | 1 | 976 | 13 | 2 | 20 | 1 |
| business2 | blend70 | 2 | 976 | 15 | 2 | 20 | 1 |
| business2 | ft | 1 | 976 | 15 | 3 | 19 | 0 |
| business2 | ft | 2 | 976 | 18 | 3 | 18 | 1 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 9 | 0 |
| dev220 | blend50 | 2 | 220 | 5 | 1 | 9 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | ft | 2 | 220 | 4 | 1 | 0 | 0 |
| general | blend50 | 1 | 383 | 8 | 0 | 15 | 5 |
| general | blend50 | 2 | 383 | 8 | 0 | 14 | 7 |
| general | blend60 | 1 | 383 | 7 | 0 | 13 | 6 |
| general | blend60 | 2 | 383 | 9 | 0 | 11 | 8 |
| general | blend70 | 1 | 383 | 6 | 0 | 13 | 6 |
| general | blend70 | 2 | 383 | 9 | 0 | 11 | 9 |
| general | ft | 1 | 383 | 8 | 0 | 13 | 7 |
| general | ft | 2 | 383 | 10 | 0 | 9 | 9 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 3, text→category: 2, text→account: 2, account→text: 1, product→text: 1, account→category: 1, quantity→amount: 1, amount→quantity: 1
- business / blend60: org→account: 3, text→category: 2, text→account: 2, org→category: 1, account→text: 1, account→category: 1, category→id: 1, category→account: 1
- business / blend70: text→category: 2, text→account: 2, account→category: 2, org→category: 1, account→text: 1, category→text: 1, org→address: 1, org→account: 1
- business / ft: text→category: 2, text→account: 2, account→category: 2, category→id: 2, org→account: 2, amount→quantity: 2, org→category: 1, account→text: 1
- business2 / blend50: account→category: 5, category→text: 4, address→category: 4, amount→quantity: 4, quantity→category: 2, category→quantity: 2, org→address: 2, id→address: 2
- business2 / blend60: account→category: 5, address→category: 3, category→quantity: 3, amount→quantity: 3, id→category: 2, category→text: 2, quantity→category: 2, org→address: 2
- business2 / blend70: account→category: 5, address→category: 3, category→quantity: 3, amount→quantity: 3, id→category: 2, category→text: 2, org→address: 2, id→address: 2
- business2 / ft: category→quantity: 4, account→category: 4, address→category: 3, amount→quantity: 3, id→category: 2, category→text: 2, quantity→amount: 2, org→address: 2
- dev220 / blend50: quantity→category: 4, org→account: 2, id→quantity: 2, category→text: 1, category→tax_class: 1, person→org: 1
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2, category→text: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, id→quantity: 2, org→address: 1
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, org→address: 1, address→id: 1
- general / blend50: org→address: 6, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2
- general / blend60: org→address: 6, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, person→org: 1, category→org: 1
- general / blend70: org→address: 6, category→text: 2, quantity→category: 2, id→category: 2, person→org: 1, category→org: 1, text→category: 1
- general / ft: org→address: 6, category→text: 4, quantity→category: 2, id→category: 2, id→address: 1, person→org: 1, category→org: 1, text→account: 1

### seedをまたいで再発した誤り

- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business2 / blend50: `contravention`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `contravention`、category→text（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `contravention`、category→text（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `contravention`、category→text（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `numéro_uev`、id→address（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `total_verified_sales`、quantity→amount（seed 1, seed 2）
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
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `名称_カナ`、org→address（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `名称_カナ`、org→address（seed 1, seed 2）
- general / ft: `goal`、id→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `名称_カナ`、org→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6159 | no |
| unknown | business | blend50 | 1 | abn | id | unknown | 0.5048 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5885 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4135 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.6047 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4999 | no |
| unknown | business | blend50 | 1 | family | id | unknown | 0.5081 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6231 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5353 | no |
| unknown | business | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5790 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5337 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.4768 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4511 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9606 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4216 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.4621 | no |
| unknown | business | blend50 | 1 | total invoices paid | quantity | unknown | 0.5031 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9435 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.9508 | no |
| wrong | business | blend50 | 1 | commodity-title_en | product | text | 0.5233 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.5875 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.5503 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.6950 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5469 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9041 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5145 | no |
| critical | business | blend50 | 2 | overseas sourced services | amount | quantity | 0.5800 | yes |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.6282 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6035 | no |
| unknown | business | blend50 | 2 | abn | id | unknown | 0.5086 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.3553 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.3889 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4706 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4728 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.6006 | no |
| unknown | business | blend50 | 2 | department | org | unknown | 0.4955 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.5050 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4867 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6246 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5337 | no |
| unknown | business | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5764 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5327 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.4767 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4476 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9561 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.4455 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4540 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9745 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9617 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.5778 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.6558 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.8764 | no |
| unknown | business | blend60 | 1 | abn | id | unknown | 0.5861 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4438 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.4071 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.6947 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.4972 | no |
| unknown | business | blend60 | 1 | publisher label | org | unknown | 0.3823 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9661 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4318 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.4928 | no |
| unknown | business | blend60 | 1 | total invoices paid | quantity | unknown | 0.5926 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9359 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9518 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.5267 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.6311 | no |
| wrong | business | blend60 | 1 | entitiy | org | category | 0.5010 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.7333 | no |
| wrong | business | blend60 | 1 | portefeuille_nom_et_code | org | account | 0.5135 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.8992 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.5776 | no |
| critical | business | blend60 | 2 | overseas sourced services | amount | quantity | 0.5877 | yes |
| unknown | business | blend60 | 2 | abn | id | unknown | 0.5907 | no |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.4258 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.3784 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.3805 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6965 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.3816 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4470 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9607 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.4949 | no |
| unknown | business | blend60 | 2 | total invoices paid | quantity | unknown | 0.5541 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9731 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9649 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5760 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.5927 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | account | 0.6441 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.8660 | no |
| wrong | business | blend60 | 2 | title | category | account | 0.5367 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4744 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4006 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.4834 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7662 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.4801 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.4455 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9716 | no |
| unknown | business | blend70 | 1 | regrp_nom | account | unknown | 0.4420 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9284 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9528 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.7120 | no |
| wrong | business | blend70 | 1 | entitiy | org | category | 0.5839 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.7716 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.8943 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6408 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.5235 | no |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.5955 | yes |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.4963 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4072 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3867 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7684 | no |
| unknown | business | blend70 | 2 | overseas sourced goods | amount | unknown | 0.3962 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9653 | no |
| unknown | business | blend70 | 2 | total invoices paid | quantity | unknown | 0.5113 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9717 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9680 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6653 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.6076 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | account | 0.6324 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.5061 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.8555 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.5442 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.6193 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9808 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.4094 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9881 | no |
| unknown | business | ft | 1 | regrp_nom | account | unknown | 0.4725 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9056 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9557 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.6605 | no |
| wrong | business | ft | 1 | description | account | text | 0.9545 | no |
| wrong | business | ft | 1 | entitiy | org | category | 0.8324 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.6340 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.8865 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.8796 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.8302 | no |
| wrong | business | ft | 1 | title | category | text | 0.6157 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.7077 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.6187 | yes |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.4939 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9839 | no |
| unknown | business | ft | 2 | overseas sourced goods | amount | unknown | 0.5651 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9791 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9675 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9775 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.6196 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.9333 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.6522 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | account | 0.5974 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.6835 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.8242 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.6923 | no |
| wrong | business | ft | 2 | title | category | account | 0.8673 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9712 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6250 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.5333 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.6171 | no |
| unknown | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6156 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.4032 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.2585 | no |
| unknown | business2 | blend50 | 1 | household income decile | category | unknown | 0.4908 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4534 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5363 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5789 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5334 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4807 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9863 | no |
| unknown | business2 | blend50 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5674 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.2944 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4860 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4829 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4210 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4790 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9899 | no |
| unknown | business2 | blend50 | 1 | total invoices paid | quantity | unknown | 0.5027 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.3936 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5101 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4951 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5253 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9890 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.5502 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.8805 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.6341 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.5136 | no |
| wrong | business2 | blend50 | 1 | numéro_uev | id | address | 0.7382 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5545 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.7311 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.5068 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.7314 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.7470 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.6053 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9541 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8136 | yes |
| other_ng | business2 | blend50 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.5404 | no |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.5568 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.8273 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6027 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.3808 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4957 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5344 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - max english county councils | amount | unknown | 0.5757 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5319 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms_known | category | unknown | 0.4524 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4661 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9885 | no |
| unknown | business2 | blend50 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.4991 | no |
| unknown | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5434 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4503 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4817 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4066 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4950 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend50 | 2 | total invoices paid | quantity | unknown | 0.6064 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4970 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5228 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9890 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5768 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.8538 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.7838 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.7362 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5904 | no |
| wrong | business2 | blend50 | 2 | projection | category | id | 0.5687 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.5010 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7745 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.8109 | no |
| wrong | business2 | blend50 | 2 | total_floor_area_known | category | quantity | 0.5867 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.8576 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.7839 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9750 | yes |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.5618 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.3368 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.4927 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.3092 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.5336 | no |
| unknown | business2 | blend60 | 1 | household income decile | category | unknown | 0.4983 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9838 | no |
| unknown | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5814 | no |
| unknown | business2 | blend60 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5688 | no |
| unknown | business2 | blend60 | 1 | scheme_description | category | unknown | 0.4663 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.3080 | no |
| unknown | business2 | blend60 | 1 | situtation | address | unknown | 0.4995 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.4220 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.4081 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3853 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend60 | 1 | total invoices paid | quantity | unknown | 0.5931 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.4148 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5817 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5927 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6173 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9890 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.5846 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5183 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.8612 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.5637 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6008 | no |
| wrong | business2 | blend60 | 1 | numéro_uev | id | address | 0.7654 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.6903 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.6799 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.7577 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.5893 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9545 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8076 | yes |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.8140 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3857 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4683 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9864 | no |
| unknown | business2 | blend60 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.4948 | no |
| unknown | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5400 | no |
| unknown | business2 | blend60 | 2 | scheme_description | category | unknown | 0.4983 | no |
| unknown | business2 | blend60 | 2 | terminal | address | unknown | 0.3856 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3301 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.5869 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9875 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9884 | no |
| unknown | business2 | blend60 | 2 | total invoices paid | quantity | unknown | 0.5280 | no |
| unknown | business2 | blend60 | 2 | total_verified_sales | quantity | unknown | 0.5564 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5950 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6143 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9889 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.5182 | no |
| wrong | business2 | blend60 | 2 | contravention | category | text | 0.6165 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.5691 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.8291 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.7433 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.5274 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.7631 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5240 | no |
| wrong | business2 | blend60 | 2 | projection | category | id | 0.5144 | no |
| wrong | business2 | blend60 | 2 | service | account | org | 0.5397 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7423 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.8086 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.6560 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.8314 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.8035 | no |
| wrong | business2 | blend60 | 2 | état | category | account | 0.5562 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9788 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6781 | yes |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.5065 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.3665 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4302 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.3599 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.6167 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.4932 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9813 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5378 | no |
| unknown | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5703 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.3781 | no |
| unknown | business2 | blend70 | 1 | service | account | unknown | 0.3588 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4916 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4546 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4432 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9895 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9891 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9890 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.4360 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9890 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.6190 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.5578 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.5832 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8418 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6880 | no |
| wrong | business2 | blend70 | 1 | numéro_uev | id | address | 0.7927 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.6495 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.5711 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.6284 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.7683 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.5733 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9548 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8017 | yes |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8007 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4555 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.3906 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4706 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9843 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4943 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4790 | no |
| unknown | business2 | blend70 | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.4974 | no |
| unknown | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5367 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3821 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3386 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.6787 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9908 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9859 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9877 | no |
| unknown | business2 | blend70 | 2 | total invoices paid | quantity | unknown | 0.5422 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5072 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9889 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.5587 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.6563 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6424 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8044 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.7027 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6023 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7900 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6291 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.7102 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.8064 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.7253 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.8051 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.8232 | no |
| wrong | business2 | blend70 | 2 | état | category | account | 0.6483 | no |
| critical | business2 | ft | 1 | fine | amount | rate | 0.5120 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9902 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.9673 | yes |
| unknown | business2 | ft | 1 | construction_age_band | category | unknown | 0.4556 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.5898 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8659 | no |
| unknown | business2 | ft | 1 | household disposable income quintiles | category | unknown | 0.4395 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.7003 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9738 | no |
| unknown | business2 | ft | 1 | potential_epc_score_known | category | unknown | 0.4780 | no |
| unknown | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5656 | no |
| unknown | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5745 | no |
| unknown | business2 | ft | 1 | scheme_description | category | unknown | 0.4957 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.5940 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9873 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9856 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9850 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9837 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9876 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.4995 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9889 | no |
| unknown | business2 | ft | 1 | want to live in this parish only | quantity | unknown | 0.4940 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.7223 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.7968 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7779 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.7839 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9495 | no |
| wrong | business2 | ft | 1 | numéro_uev | id | address | 0.8745 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.5110 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.5271 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.7858 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.6328 | no |
| wrong | business2 | ft | 1 | type of expenditure | account | category | 0.8003 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.5251 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9559 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7840 | yes |
| critical | business2 | ft | 2 | total_verified_sales | quantity | amount | 0.7231 | yes |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.7609 | no |
| unknown | business2 | ft | 2 | fine | amount | unknown | 0.4052 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.4869 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.4774 | no |
| unknown | business2 | ft | 2 | numéro entente-cadre | id | unknown | 0.5448 | no |
| unknown | business2 | ft | 2 | numéro_de_lot | id | unknown | 0.4906 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9781 | no |
| unknown | business2 | ft | 2 | return-on-investments_revenus-de-placements | amount | unknown | 0.5061 | no |
| unknown | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | 0.5265 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.4825 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.9543 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9828 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9801 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9805 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9858 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9888 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.5095 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.6802 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.7754 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.5518 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.8625 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.7304 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.5812 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.8271 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.8706 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8972 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.6138 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.7995 | no |
| wrong | business2 | ft | 2 | terminal | address | org | 0.5420 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.9333 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.7263 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.8822 | no |
| wrong | business2 | ft | 2 | état | category | account | 0.9245 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.7093 | yes |
| unknown | dev220 | blend50 | 1 | name | person | unknown | 0.4999 | no |
| unknown | dev220 | blend50 | 1 | primary contact | person | unknown | 0.4990 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.6109 | no |
| unknown | dev220 | blend50 | 1 | ポイント | amount | unknown | 0.3619 | no |
| unknown | dev220 | blend50 | 1 | メッセージ | text | unknown | 0.4938 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4891 | no |
| unknown | dev220 | blend50 | 1 | 受注名 | person | unknown | 0.4960 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4734 | no |
| unknown | dev220 | blend50 | 1 | 発送先カナ | person | unknown | 0.4902 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.9863 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.9439 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5177 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.5310 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.8305 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8612 | yes |
| unknown | dev220 | blend50 | 2 | name | person | unknown | 0.4970 | no |
| unknown | dev220 | blend50 | 2 | primary contact | person | unknown | 0.4966 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4809 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.6084 | no |
| unknown | dev220 | blend50 | 2 | メッセージ | text | unknown | 0.4948 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4875 | no |
| unknown | dev220 | blend50 | 2 | 受注名 | person | unknown | 0.4830 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4521 | no |
| unknown | dev220 | blend50 | 2 | 発送先名 | person | unknown | 0.4915 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9909 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.9524 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.8142 | no |
| wrong | dev220 | blend50 | 2 | 発送先カナ | person | org | 0.5026 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.6983 | yes |
| unknown | dev220 | blend60 | 1 | taxable | category | unknown | 0.4925 | no |
| unknown | dev220 | blend60 | 1 | ポイント | amount | unknown | 0.3890 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.9854 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.9500 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.5009 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.8500 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.8806 | yes |
| unknown | dev220 | blend60 | 2 | 発送先カナ | person | unknown | 0.4819 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9909 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9603 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.8305 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.6874 | yes |
| unknown | dev220 | blend70 | 1 | city | address | unknown | 0.4980 | no |
| unknown | dev220 | blend70 | 1 | ポイント | amount | unknown | 0.4503 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9845 | no |
| wrong | dev220 | blend70 | 1 | location | org | address | 0.5540 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.9561 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.8695 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9000 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9909 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9681 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.8467 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.6546 | yes |
| unknown | dev220 | ft | 1 | payment terms | category | unknown | 0.4989 | no |
| unknown | dev220 | ft | 1 | ポイント | amount | unknown | 0.6340 | no |
| wrong | dev220 | ft | 1 | city | address | id | 0.6896 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9817 | no |
| wrong | dev220 | ft | 1 | location | org | address | 0.7726 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9744 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9280 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9584 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9908 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9915 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8954 | no |
| other_ng | general | blend50 | 1 | abstract rank | other | category | 0.5211 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.6282 | no |
| other_ng | general | blend50 | 1 | fulltext rank | other | category | 0.5195 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.7764 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.7998 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4661 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5685 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.6794 | no |
| unknown | general | blend50 | 1 | lda | text | unknown | 0.4816 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4807 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4528 | no |
| unknown | general | blend50 | 1 | raw | category | unknown | 0.4844 | no |
| unknown | general | blend50 | 1 | source | category | unknown | 0.4351 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.3676 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.5355 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9877 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3180 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9924 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.9444 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.4909 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5301 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.6318 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.8688 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9540 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8918 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.5609 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.7290 | no |
| wrong | general | blend50 | 1 | 名称_カナ | org | address | 0.8131 | no |
| other_ng | general | blend50 | 2 | abstract rank | other | category | 0.5247 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | quantity | 0.6089 | no |
| other_ng | general | blend50 | 2 | fulltext rank | other | category | 0.5658 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.8381 | no |
| other_ng | general | blend50 | 2 | operationid | other | id | 0.5607 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9060 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.8251 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4880 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4599 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5701 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.6933 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4569 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4496 | no |
| unknown | general | blend50 | 2 | source | category | unknown | 0.4816 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4960 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4909 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9873 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3645 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9926 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9803 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.4765 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.9342 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.7081 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.8233 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9565 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8900 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5295 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.6758 | no |
| wrong | general | blend50 | 2 | 名称_カナ | org | address | 0.8308 | no |
| other_ng | general | blend60 | 1 | abstract rank | other | category | 0.6121 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6981 | no |
| other_ng | general | blend60 | 1 | fulltext rank | other | category | 0.5895 | no |
| other_ng | general | blend60 | 1 | mt2 | other | category | 0.5308 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.7496 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.7604 | no |
| unknown | general | blend60 | 1 | app | category | unknown | 0.5004 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.4114 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6523 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.7261 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3759 | no |
| unknown | general | blend60 | 1 | sens_final | rate | unknown | 0.5723 | no |
| unknown | general | blend60 | 1 | source | category | unknown | 0.4283 | no |
| unknown | general | blend60 | 1 | study | text | unknown | 0.3199 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9879 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3053 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9908 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.9368 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.4947 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.5629 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.8585 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9538 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8761 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.6259 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.7539 | no |
| wrong | general | blend60 | 1 | 名称_カナ | org | address | 0.8058 | no |
| other_ng | general | blend60 | 2 | abstract rank | other | category | 0.6164 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | quantity | 0.5886 | no |
| other_ng | general | blend60 | 2 | fulltext rank | other | category | 0.6450 | no |
| other_ng | general | blend60 | 2 | mood | other | category | 0.5697 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.8383 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.6310 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9051 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.7908 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.4505 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6541 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.7428 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.5001 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5819 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.4308 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9875 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3737 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9912 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9798 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.3822 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.9264 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.6545 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.8039 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9569 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8739 | no |
| wrong | general | blend60 | 2 | source | category | org | 0.5600 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.5882 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.6901 | no |
| wrong | general | blend60 | 2 | 名称_カナ | org | address | 0.8270 | no |
| other_ng | general | blend70 | 1 | abstract rank | other | category | 0.7030 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7679 | no |
| other_ng | general | blend70 | 1 | fulltext rank | other | category | 0.6595 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.6179 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.7228 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.7210 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.5830 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4941 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.4660 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7360 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.7728 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4220 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.6670 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4442 | no |
| unknown | general | blend70 | 1 | study | text | unknown | 0.3629 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9881 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.3560 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9893 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9292 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.8482 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9536 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8604 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6909 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.7789 | no |
| wrong | general | blend70 | 1 | 名称_カナ | org | address | 0.7984 | no |
| other_ng | general | blend70 | 2 | abstract rank | other | category | 0.7080 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | quantity | 0.5683 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.5331 | no |
| other_ng | general | blend70 | 2 | fulltext rank | other | category | 0.7242 | no |
| other_ng | general | blend70 | 2 | mood | other | category | 0.6639 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.8385 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.7013 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9042 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.7565 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.5117 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7382 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.7923 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.5833 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6782 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.5000 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9876 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.3829 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9897 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9794 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4162 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.9186 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.6008 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.7845 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9572 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.8579 | no |
| wrong | general | blend70 | 2 | source | category | org | 0.6451 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.6470 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.7044 | no |
| wrong | general | blend70 | 2 | 名称_カナ | org | address | 0.8232 | no |
| other_ng | general | ft | 1 | abstract rank | other | category | 0.9759 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9776 | no |
| other_ng | general | ft | 1 | fulltext rank | other | category | 0.8694 | no |
| other_ng | general | ft | 1 | mood | other | category | 0.6660 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.8792 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.6424 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.6029 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.8310 | no |
| unknown | general | ft | 1 | cleaned | text | unknown | 0.4846 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.6298 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9872 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9130 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.6026 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9512 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.4348 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4866 | no |
| unknown | general | ft | 1 | study | text | unknown | 0.4919 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9888 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9847 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9063 | no |
| wrong | general | ft | 1 | goal | id | category | 0.8174 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9531 | no |
| wrong | general | ft | 1 | place | org | address | 0.8134 | no |
| wrong | general | ft | 1 | source | category | text | 0.5819 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8860 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.8537 | no |
| wrong | general | ft | 1 | 名称_カナ | org | address | 0.7764 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.5082 | no |
| other_ng | general | ft | 2 | abstract rank | other | category | 0.9831 | no |
| other_ng | general | ft | 2 | dag-stage | other | quantity | 0.5075 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.7614 | no |
| other_ng | general | ft | 2 | fulltext rank | other | category | 0.9619 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.9465 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.8390 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9123 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9015 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.6536 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.6951 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9903 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9408 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8329 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9671 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9880 | no |
| unknown | general | ft | 2 | 発生県 | id | unknown | 0.4105 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9853 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9780 | no |
| wrong | general | ft | 2 | author | person | org | 0.8951 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.5017 | no |
| wrong | general | ft | 2 | goal | id | category | 0.7264 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9582 | no |
| wrong | general | ft | 2 | place | org | address | 0.8097 | no |
| wrong | general | ft | 2 | source | category | org | 0.9006 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.7075 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.8232 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.7472 | no |
| wrong | general | ft | 2 | 名称_カナ | org | address | 0.8117 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 61件
- numeric_values_not_parseable: 17件
- other_class: 69件
- probability_below_threshold: 173件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 31件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 155件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 113件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
