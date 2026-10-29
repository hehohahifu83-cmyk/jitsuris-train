# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-29T00:56:55+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 5 | 1 | 19 | 0 |
| business | blend50 | 2 | 490 | 6 | 1 | 21 | 0 |
| business | blend60 | 1 | 490 | 7 | 1 | 11 | 0 |
| business | blend60 | 2 | 490 | 7 | 1 | 14 | 0 |
| business | blend70 | 1 | 490 | 8 | 1 | 10 | 0 |
| business | blend70 | 2 | 490 | 11 | 1 | 9 | 0 |
| business | ft | 1 | 490 | 9 | 1 | 7 | 1 |
| business | ft | 2 | 490 | 10 | 1 | 7 | 0 |
| business2 | blend50 | 1 | 976 | 14 | 3 | 26 | 1 |
| business2 | blend50 | 2 | 976 | 16 | 3 | 27 | 3 |
| business2 | blend60 | 1 | 976 | 16 | 3 | 19 | 1 |
| business2 | blend60 | 2 | 976 | 13 | 2 | 26 | 3 |
| business2 | blend70 | 1 | 976 | 16 | 4 | 18 | 1 |
| business2 | blend70 | 2 | 976 | 14 | 2 | 22 | 3 |
| business2 | ft | 1 | 976 | 19 | 2 | 16 | 1 |
| business2 | ft | 2 | 976 | 17 | 3 | 19 | 3 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 7 | 0 |
| dev220 | blend50 | 2 | 220 | 6 | 1 | 5 | 0 |
| dev220 | blend60 | 1 | 220 | 4 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 5 | 1 | 0 | 0 |
| dev220 | blend70 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 7 | 2 | 0 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 1 | 0 |
| general | blend50 | 1 | 383 | 7 | 0 | 15 | 6 |
| general | blend50 | 2 | 383 | 8 | 0 | 14 | 4 |
| general | blend60 | 1 | 383 | 8 | 0 | 11 | 6 |
| general | blend60 | 2 | 383 | 9 | 0 | 12 | 6 |
| general | blend70 | 1 | 383 | 8 | 0 | 11 | 7 |
| general | blend70 | 2 | 383 | 9 | 0 | 13 | 6 |
| general | ft | 1 | 383 | 8 | 0 | 12 | 8 |
| general | ft | 2 | 383 | 11 | 1 | 9 | 9 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 6, quantity→amount: 2, text→account: 2, account→text: 1
- business / blend60: org→account: 6, quantity→amount: 2, text→account: 2, category→id: 2, org→address: 1, account→text: 1
- business / blend70: org→account: 7, quantity→amount: 2, text→account: 2, category→id: 2, org→address: 1, category→account: 1, account→text: 1, account→category: 1
- business / ft: org→account: 6, quantity→amount: 2, category→account: 2, text→account: 2, category→id: 2, org→address: 1, account→text: 1, account→category: 1
- business2 / blend50: account→category: 4, address→category: 4, amount→quantity: 4, category→quantity: 3, category→text: 3, category→org: 2, quantity→amount: 2, category→id: 2
- business2 / blend60: account→category: 4, address→category: 4, category→quantity: 3, category→text: 3, amount→quantity: 3, id→category: 2, quantity→amount: 2, category→id: 2
- business2 / blend70: account→category: 3, quantity→amount: 3, address→category: 3, category→quantity: 3, amount→quantity: 3, id→category: 2, category→id: 2, category→address: 2
- business2 / ft: category→id: 4, account→category: 3, category→quantity: 3, id→category: 2, address→category: 2, quantity→address: 2, category→address: 2, quantity→category: 2
- dev220 / blend50: quantity→category: 4, text→category: 2, org→account: 2, category→tax_class: 2, id→quantity: 2
- dev220 / blend60: quantity→category: 4, org→account: 2, id→quantity: 2, category→tax_class: 1
- dev220 / blend70: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, category→tax_class: 1, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, text→category: 2, id→quantity: 2, address→id: 2, amount→quantity: 1
- general / blend50: org→address: 4, person→org: 2, category→text: 2, quantity→category: 2, text→category: 2, id→category: 2, category→quantity: 1
- general / blend60: category→text: 4, org→address: 4, text→category: 3, quantity→category: 2, id→category: 2, category→org: 1, person→org: 1
- general / blend70: category→text: 5, org→address: 4, text→category: 3, quantity→category: 2, category→org: 1, id→category: 1, person→org: 1
- general / ft: category→text: 8, org→address: 4, text→category: 3, category→org: 1, person→org: 1, id→address: 1, id→quantity: 1

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `ligne`、category→id（seed 1, seed 2）
- business / blend60: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `ligne`、category→id（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `ligne`、category→id（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `merchant description`、category→org（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `name`、org→address（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend50: `situtation`、address→category（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `monitor`、id→category（seed 1, seed 2）
- business2 / blend60: `name`、org→address（seed 1, seed 2）
- business2 / blend60: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend60: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend60: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend60: `situtation`、address→category（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `warddesc`、address→category（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `warddesc`、address→category（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend50: `メッセージ`、text→category（seed 1, seed 2）
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
- general / blend60: `cleaned`、text→category（seed 1, seed 2）
- general / blend60: `goal`、id→category（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `place`、org→address（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `ステーション名`、org→address（seed 1, seed 2）
- general / blend60: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / blend70: `cleaned`、text→category（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `ステーション名`、org→address（seed 1, seed 2）
- general / blend70: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `cleaned`、text→category（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `source`、category→text（seed 1, seed 2）
- general / ft: `source_value`、category→text（seed 1, seed 2）
- general / ft: `ステーション名`、org→address（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.8075 | yes |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.5870 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.5955 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.3442 | no |
| unknown | business | blend50 | 1 | defence goods value | amount | unknown | 0.6039 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5588 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4835 | no |
| unknown | business | blend50 | 1 | ligne | category | unknown | 0.4921 | no |
| unknown | business | blend50 | 1 | merchant details | text | unknown | 0.4244 | no |
| unknown | business | blend50 | 1 | mois calendrier | date | unknown | 0.6426 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5799 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5777 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.5013 | no |
| unknown | business | blend50 | 1 | portefeuille_nom_et_code | org | unknown | 0.3268 | no |
| unknown | business | blend50 | 1 | publisher label | org | unknown | 0.4897 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9777 | no |
| unknown | business | blend50 | 1 | regrp_sommaire | account | unknown | 0.3484 | no |
| unknown | business | blend50 | 1 | title | category | unknown | 0.3717 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9254 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.7755 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9641 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.5906 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9754 | no |
| wrong | business | blend50 | 1 | purposeofexpenditure | text | account | 0.9244 | no |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.9768 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5722 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.5800 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.5987 | no |
| unknown | business | blend50 | 2 | commodity-title_en | product | unknown | 0.4380 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4708 | no |
| unknown | business | blend50 | 2 | defence goods value | amount | unknown | 0.6081 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5619 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4941 | no |
| unknown | business | blend50 | 2 | ligne | category | unknown | 0.4540 | no |
| unknown | business | blend50 | 2 | merchant details | text | unknown | 0.3800 | no |
| unknown | business | blend50 | 2 | mois calendrier | date | unknown | 0.6238 | no |
| unknown | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5825 | no |
| unknown | business | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5791 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.5013 | no |
| unknown | business | blend50 | 2 | portefeuille_nom_et_code | org | unknown | 0.4478 | no |
| unknown | business | blend50 | 2 | publisher label | org | unknown | 0.4878 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9743 | no |
| unknown | business | blend50 | 2 | regrp_sommaire | account | unknown | 0.3465 | no |
| unknown | business | blend50 | 2 | title | category | unknown | 0.4835 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9054 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.7689 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9518 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.5792 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9671 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.5524 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.9139 | no |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.7696 | yes |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.3668 | no |
| unknown | business | blend60 | 1 | entitiy | org | unknown | 0.3935 | no |
| unknown | business | blend60 | 1 | merchant details | text | unknown | 0.4383 | no |
| unknown | business | blend60 | 1 | mois calendrier | date | unknown | 0.7120 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.5953 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.3300 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9806 | no |
| unknown | business | blend60 | 1 | regrp_sommaire | account | unknown | 0.3718 | no |
| unknown | business | blend60 | 1 | title | category | unknown | 0.3496 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9200 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.8016 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9590 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.5558 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9728 | no |
| wrong | business | blend60 | 1 | ligne | category | id | 0.5881 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.5237 | no |
| wrong | business | blend60 | 1 | purposeofexpenditure | text | account | 0.9261 | no |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.9729 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6201 | no |
| unknown | business | blend60 | 2 | commodity-title_en | product | unknown | 0.4794 | no |
| unknown | business | blend60 | 2 | entitiy | org | unknown | 0.4920 | no |
| unknown | business | blend60 | 2 | merchant details | text | unknown | 0.3850 | no |
| unknown | business | blend60 | 2 | mois calendrier | date | unknown | 0.6894 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.5953 | no |
| unknown | business | blend60 | 2 | portefeuille_nom_et_code | org | unknown | 0.4285 | no |
| unknown | business | blend60 | 2 | procurementclassification:proclasslabel | account | unknown | 0.4994 | no |
| unknown | business | blend60 | 2 | publisher label | org | unknown | 0.4059 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9766 | no |
| unknown | business | blend60 | 2 | regrp_sommaire | account | unknown | 0.3694 | no |
| unknown | business | blend60 | 2 | title | category | unknown | 0.4442 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.8960 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.7937 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9442 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.5421 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9628 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.6254 | no |
| wrong | business | blend60 | 2 | ligne | category | id | 0.5424 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.9134 | no |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.7318 | yes |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3894 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4452 | no |
| unknown | business | blend70 | 1 | merchant details | text | unknown | 0.4523 | no |
| unknown | business | blend70 | 1 | mois calendrier | date | unknown | 0.7814 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3807 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9835 | no |
| unknown | business | blend70 | 1 | regrp_sommaire | account | unknown | 0.3951 | no |
| unknown | business | blend70 | 1 | title | category | unknown | 0.3996 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9146 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.8278 | no |
| wrong | business | blend70 | 1 | capital revenue | category | account | 0.5274 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9540 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.5210 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9701 | no |
| wrong | business | blend70 | 1 | ligne | category | id | 0.6841 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6079 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9277 | no |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9689 | yes |
| unknown | business | blend70 | 2 | merchant details | text | unknown | 0.3901 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.7550 | no |
| unknown | business | blend70 | 2 | portefeuille_nom_et_code | org | unknown | 0.4092 | no |
| unknown | business | blend70 | 2 | publisher label | org | unknown | 0.4733 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9789 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.3923 | no |
| unknown | business | blend70 | 2 | title | category | unknown | 0.4050 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.8866 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8186 | no |
| wrong | business | blend70 | 2 | commodity-title_en | product | category | 0.5207 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9367 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.5049 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9585 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.6985 | no |
| wrong | business | blend70 | 2 | dispute-status_statut-de-différend-fra | category | text | 0.5354 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.5740 | no |
| wrong | business | blend70 | 2 | ligne | category | id | 0.6308 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5108 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9129 | no |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.6183 | yes |
| other_ng | business | ft | 1 | km budgété | other | quantity | 0.6669 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4593 | no |
| unknown | business | ft | 1 | merchant details | text | unknown | 0.4942 | no |
| unknown | business | ft | 1 | mois calendrier | date | unknown | 0.9895 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9924 | no |
| unknown | business | ft | 1 | regrp_sommaire | account | unknown | 0.4650 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.8983 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9062 | no |
| wrong | business | ft | 1 | capital revenue | category | account | 0.6752 | no |
| wrong | business | ft | 1 | department | org | account | 0.9387 | no |
| wrong | business | ft | 1 | department | org | account | 0.9623 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.6360 | no |
| wrong | business | ft | 1 | ligne | category | id | 0.9720 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.8605 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9325 | no |
| wrong | business | ft | 1 | title | category | account | 0.5495 | no |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.9571 | yes |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.9518 | no |
| unknown | business | ft | 2 | portefeuille_nom_et_code | org | unknown | 0.3512 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9857 | no |
| unknown | business | ft | 2 | regrp_sommaire | account | unknown | 0.4611 | no |
| unknown | business | ft | 2 | title | category | unknown | 0.4802 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.8583 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8931 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.6449 | no |
| wrong | business | ft | 2 | department | org | account | 0.9141 | no |
| wrong | business | ft | 2 | department | org | account | 0.9457 | no |
| wrong | business | ft | 2 | description | account | text | 0.9177 | no |
| wrong | business | ft | 2 | dispute-status_statut-de-différend-fra | category | text | 0.7649 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.8200 | no |
| wrong | business | ft | 2 | ligne | category | id | 0.8958 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.5799 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9114 | no |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9738 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7460 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.7846 | yes |
| other_ng | business2 | blend50 | 1 | energy_consumption | other | quantity | 0.6341 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.4861 | no |
| unknown | business2 | blend50 | 1 | conservation_area_site_id | category | unknown | 0.4866 | no |
| unknown | business2 | blend50 | 1 | epc_score_known | category | unknown | 0.3527 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.3022 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4816 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5808 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5772 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4532 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9775 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5691 | no |
| unknown | business2 | blend50 | 1 | return-on-investments_revenus-de-placements | amount | unknown | 0.5994 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.3947 | no |
| unknown | business2 | blend50 | 1 | super output area 2011 name | address | unknown | 0.4903 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.3946 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.3403 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4517 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9931 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9934 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9942 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9924 | no |
| unknown | business2 | blend50 | 1 | total_floor_area_known | category | unknown | 0.5818 | no |
| unknown | business2 | blend50 | 1 | total_verified_sales | quantity | unknown | 0.5359 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.4990 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5234 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9931 | no |
| wrong | business2 | blend50 | 1 | merchant description | category | org | 0.7761 | no |
| wrong | business2 | blend50 | 1 | name | org | address | 0.6869 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.6421 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms_known | category | quantity | 0.6069 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7939 | no |
| wrong | business2 | blend50 | 1 | projection | category | id | 0.7317 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.5680 | no |
| wrong | business2 | blend50 | 1 | service_responsable | account | category | 0.5922 | no |
| wrong | business2 | blend50 | 1 | situtation | address | category | 0.7567 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9814 | no |
| wrong | business2 | blend50 | 1 | warddesc | address | category | 0.7101 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.9535 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6307 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.9694 | yes |
| other_ng | business2 | blend50 | 2 | energy_consumption | other | quantity | 0.6792 | no |
| other_ng | business2 | blend50 | 2 | epc_score | other | rate | 0.6168 | no |
| other_ng | business2 | blend50 | 2 | potential_epc_score | other | rate | 0.6465 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5358 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.4177 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4700 | no |
| unknown | business2 | blend50 | 2 | fine | amount | unknown | 0.3143 | no |
| unknown | business2 | blend50 | 2 | imd19_income_decile | category | unknown | 0.3737 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | unknown | 0.5840 | no |
| unknown | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | unknown | 0.5784 | no |
| unknown | business2 | blend50 | 2 | number_habitable_rooms | quantity | unknown | 0.4969 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.4752 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9730 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4068 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.3790 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5739 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.3363 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4944 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4251 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.3586 | no |
| unknown | business2 | blend50 | 2 | terrace | quantity | unknown | 0.4405 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9937 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9933 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.4952 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5216 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9937 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.6268 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5964 | no |
| wrong | business2 | blend50 | 2 | merchant description | category | org | 0.5483 | no |
| wrong | business2 | blend50 | 2 | monitor | id | category | 0.5322 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.7960 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms_known | category | quantity | 0.5970 | no |
| wrong | business2 | blend50 | 2 | numéro | id | address | 0.5309 | no |
| wrong | business2 | blend50 | 2 | numéro_uev | id | address | 0.6664 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.7419 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.9228 | no |
| wrong | business2 | blend50 | 2 | situtation | address | category | 0.6194 | no |
| wrong | business2 | blend50 | 2 | total_floor_area_known | category | quantity | 0.5038 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9865 | no |
| wrong | business2 | blend50 | 2 | warddesc | address | category | 0.5975 | no |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9774 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7187 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.7422 | yes |
| other_ng | business2 | blend60 | 1 | energy_consumption | other | quantity | 0.6732 | no |
| unknown | business2 | blend60 | 1 | conservation_area_site_id | category | unknown | 0.4512 | no |
| unknown | business2 | blend60 | 1 | epc_score_known | category | unknown | 0.3984 | no |
| unknown | business2 | blend60 | 1 | fine | amount | unknown | 0.2753 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5411 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9734 | no |
| unknown | business2 | blend60 | 1 | service | account | unknown | 0.4715 | no |
| unknown | business2 | blend60 | 1 | terminal | address | unknown | 0.3822 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3296 | no |
| unknown | business2 | blend60 | 1 | terrace | quantity | unknown | 0.3754 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9923 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9933 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9925 | no |
| unknown | business2 | blend60 | 1 | total_floor_area_known | category | unknown | 0.6400 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5454 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.5971 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6165 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9929 | no |
| wrong | business2 | blend60 | 1 | loac_group | category | address | 0.5800 | no |
| wrong | business2 | blend60 | 1 | merchant description | category | org | 0.7456 | no |
| wrong | business2 | blend60 | 1 | monitor | id | category | 0.5399 | no |
| wrong | business2 | blend60 | 1 | name | org | address | 0.6250 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms | quantity | category | 0.5844 | no |
| wrong | business2 | blend60 | 1 | number_habitable_rooms_known | category | quantity | 0.6802 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.8039 | no |
| wrong | business2 | blend60 | 1 | projection | category | id | 0.7565 | no |
| wrong | business2 | blend60 | 1 | scheme_description | category | text | 0.5016 | no |
| wrong | business2 | blend60 | 1 | service_responsable | account | category | 0.5358 | no |
| wrong | business2 | blend60 | 1 | situtation | address | category | 0.7236 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9803 | no |
| wrong | business2 | blend60 | 1 | warddesc | address | category | 0.7123 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.9531 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.9639 | yes |
| other_ng | business2 | blend60 | 2 | energy_consumption | other | quantity | 0.7273 | no |
| other_ng | business2 | blend60 | 2 | epc_score | other | rate | 0.6571 | no |
| other_ng | business2 | blend60 | 2 | potential_epc_score | other | rate | 0.6876 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5765 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.4428 | no |
| unknown | business2 | blend60 | 2 | energy_consumption_known | category | unknown | 0.4833 | no |
| unknown | business2 | blend60 | 2 | epc_score_known | category | unknown | 0.4753 | no |
| unknown | business2 | blend60 | 2 | fine | amount | unknown | 0.3751 | no |
| unknown | business2 | blend60 | 2 | imd19_income_decile | category | unknown | 0.4297 | no |
| unknown | business2 | blend60 | 2 | loac_group | category | unknown | 0.4975 | no |
| unknown | business2 | blend60 | 2 | merchant description | category | unknown | 0.4970 | no |
| unknown | business2 | blend60 | 2 | number_habitable_rooms | quantity | unknown | 0.5819 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.5676 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9681 | no |
| unknown | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5804 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4311 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.4548 | no |
| unknown | business2 | blend60 | 2 | service | account | unknown | 0.3085 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3862 | no |
| unknown | business2 | blend60 | 2 | terrace | quantity | unknown | 0.3619 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9915 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9928 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9922 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9918 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5925 | no |
| unknown | business2 | blend60 | 2 | value | quantity | unknown | 0.6142 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9936 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.6620 | no |
| wrong | business2 | blend60 | 2 | contravention | category | text | 0.6531 | no |
| wrong | business2 | blend60 | 2 | monitor | id | category | 0.6006 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.7559 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms_known | category | quantity | 0.6684 | no |
| wrong | business2 | blend60 | 2 | numéro_uev | id | address | 0.6998 | no |
| wrong | business2 | blend60 | 2 | scheme_description | category | text | 0.7103 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.9325 | no |
| wrong | business2 | blend60 | 2 | situtation | address | category | 0.5589 | no |
| wrong | business2 | blend60 | 2 | total_floor_area_known | category | quantity | 0.5010 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9863 | no |
| wrong | business2 | blend60 | 2 | warddesc | address | category | 0.5772 | no |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9811 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6915 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.6998 | yes |
| critical | business2 | blend70 | 1 | total_verified_sales | quantity | amount | 0.6314 | yes |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | quantity | 0.7123 | no |
| unknown | business2 | blend70 | 1 | conservation_area_site_id | category | unknown | 0.4767 | no |
| unknown | business2 | blend70 | 1 | energy_consumption_known | category | unknown | 0.4985 | no |
| unknown | business2 | blend70 | 1 | epc_score_known | category | unknown | 0.4527 | no |
| unknown | business2 | blend70 | 1 | fine | amount | unknown | 0.3180 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9693 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4706 | no |
| unknown | business2 | blend70 | 1 | service_responsable | account | unknown | 0.4884 | no |
| unknown | business2 | blend70 | 1 | terminal | address | unknown | 0.4417 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.3840 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4096 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9924 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9925 | no |
| unknown | business2 | blend70 | 1 | total_floor_area_known | category | unknown | 0.6982 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9927 | no |
| unknown | business2 | blend70 | 1 | want to live in this parish & band d | quantity | unknown | 0.4891 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6765 | no |
| wrong | business2 | blend70 | 1 | merchant description | category | org | 0.7151 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.5981 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.5631 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.5268 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.7536 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.8139 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7813 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.5482 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.6906 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9792 | no |
| wrong | business2 | blend70 | 1 | warddesc | address | category | 0.7146 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9527 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.9585 | yes |
| other_ng | business2 | blend70 | 2 | energy_consumption | other | quantity | 0.7755 | no |
| other_ng | business2 | blend70 | 2 | epc_score | other | rate | 0.6975 | no |
| other_ng | business2 | blend70 | 2 | potential_epc_score | other | rate | 0.7287 | no |
| unknown | business2 | blend70 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6172 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4680 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4806 | no |
| unknown | business2 | blend70 | 2 | fine | amount | unknown | 0.4358 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6685 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9631 | no |
| unknown | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5301 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5030 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.5306 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.3581 | no |
| unknown | business2 | blend70 | 2 | situtation | address | unknown | 0.4984 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4446 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.3854 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9913 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9919 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9911 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9896 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.4982 | no |
| unknown | business2 | blend70 | 2 | total_verified_sales | quantity | unknown | 0.5824 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9935 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.6971 | no |
| wrong | business2 | blend70 | 2 | contravention | category | text | 0.7097 | no |
| wrong | business2 | blend70 | 2 | energy_consumption_known | category | quantity | 0.5138 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.5013 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.5804 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.6691 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.7158 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.7398 | no |
| wrong | business2 | blend70 | 2 | numéro_uev | id | address | 0.7331 | no |
| wrong | business2 | blend70 | 2 | scheme_description | category | text | 0.6787 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.9422 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9862 | no |
| wrong | business2 | blend70 | 2 | warddesc | address | category | 0.5569 | no |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9920 | yes |
| critical | business2 | ft | 1 | total_verified_sales | quantity | amount | 0.8896 | yes |
| other_ng | business2 | ft | 1 | energy_consumption | other | quantity | 0.8298 | no |
| unknown | business2 | ft | 1 | energy_consumption_known | category | unknown | 0.4344 | no |
| unknown | business2 | ft | 1 | epc_score_known | category | unknown | 0.6156 | no |
| unknown | business2 | ft | 1 | fine | amount | unknown | 0.4462 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.5822 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.6348 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9571 | no |
| unknown | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6098 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9882 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9879 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9897 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9926 | no |
| unknown | business2 | ft | 1 | total invoices paid | quantity | unknown | 0.5726 | no |
| unknown | business2 | ft | 1 | total_floor_area_known | category | unknown | 0.8728 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9919 | no |
| unknown | business2 | ft | 1 | want to live in this parish only | quantity | unknown | 0.4984 | no |
| wrong | business2 | ft | 1 | conservation_area_site_id | category | id | 0.6763 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.5175 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9662 | no |
| wrong | business2 | ft | 1 | lsoa11nm | address | id | 0.5533 | no |
| wrong | business2 | ft | 1 | merchant description | category | org | 0.6236 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7730 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9736 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.8438 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.8555 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.7785 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.5914 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5471 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.5829 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9758 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band a | quantity | category | 0.6133 | no |
| wrong | business2 | ft | 1 | want to live in this parish & band d | quantity | category | 0.6985 | no |
| wrong | business2 | ft | 1 | warddesc | address | category | 0.7214 | no |
| critical | business2 | ft | 2 | fine | amount | rate | 0.6181 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9514 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.9422 | yes |
| other_ng | business2 | ft | 2 | energy_consumption | other | quantity | 0.9200 | no |
| other_ng | business2 | ft | 2 | epc_score | other | rate | 0.8185 | no |
| other_ng | business2 | ft | 2 | potential_epc_score | other | rate | 0.8521 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.4966 | no |
| unknown | business2 | ft | 2 | habitatdescription | text | unknown | 0.4903 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9282 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9482 | no |
| unknown | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.6071 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7186 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.7580 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.6195 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.5326 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9909 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9893 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9857 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9914 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4897 | no |
| unknown | business2 | ft | 2 | total_verified_sales | quantity | unknown | 0.5741 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9931 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.8026 | no |
| unknown | business2 | ft | 2 | warddesc | address | unknown | 0.4961 | no |
| wrong | business2 | ft | 2 | contravention | category | text | 0.8797 | no |
| wrong | business2 | ft | 2 | energy_consumption_known | category | quantity | 0.6164 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.7161 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.8289 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.8744 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.5957 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9540 | no |
| wrong | business2 | ft | 2 | numéro_uev | id | address | 0.8330 | no |
| wrong | business2 | ft | 2 | propertytype | category | id | 0.5406 | no |
| wrong | business2 | ft | 2 | scheme_description | category | text | 0.5839 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.5069 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.9715 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.6413 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9859 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8948 | yes |
| unknown | dev220 | blend50 | 1 | credit limit | amount | unknown | 0.4674 | no |
| unknown | dev220 | blend50 | 1 | item description | text | unknown | 0.4799 | no |
| unknown | dev220 | blend50 | 1 | website | text | unknown | 0.4918 | no |
| unknown | dev220 | blend50 | 1 | その他費用 | amount | unknown | 0.5807 | no |
| unknown | dev220 | blend50 | 1 | 作業者欄 | person | unknown | 0.4939 | no |
| unknown | dev220 | blend50 | 1 | 商品オプション | text | unknown | 0.4999 | no |
| unknown | dev220 | blend50 | 1 | 支出負担行為担当官 | person | unknown | 0.4560 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.7583 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.8627 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5076 | no |
| wrong | dev220 | blend50 | 1 | メッセージ | text | category | 0.5001 | no |
| wrong | dev220 | blend50 | 1 | 担当課 | org | account | 0.7387 | no |
| critical | dev220 | blend50 | 2 | purchase order by customer | id | quantity | 0.8937 | yes |
| unknown | dev220 | blend50 | 2 | website | text | unknown | 0.4951 | no |
| unknown | dev220 | blend50 | 2 | その他費用 | amount | unknown | 0.5824 | no |
| unknown | dev220 | blend50 | 2 | 作業者欄 | person | unknown | 0.4957 | no |
| unknown | dev220 | blend50 | 2 | 支出負担行為担当官 | person | unknown | 0.4564 | no |
| unknown | dev220 | blend50 | 2 | 発送先カナ | person | unknown | 0.4805 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9785 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.8816 | no |
| wrong | dev220 | blend50 | 2 | taxable | category | tax_class | 0.7257 | no |
| wrong | dev220 | blend50 | 2 | メッセージ | text | category | 0.5002 | no |
| wrong | dev220 | blend50 | 2 | 担当課 | org | account | 0.7290 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.9058 | yes |
| unknown | dev220 | blend60 | 1 | credit limit | amount | unknown | 0.5059 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.7140 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.8781 | no |
| wrong | dev220 | blend60 | 1 | 担当課 | org | account | 0.7655 | no |
| critical | dev220 | blend60 | 2 | purchase order by customer | id | quantity | 0.9044 | yes |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9783 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.9008 | no |
| wrong | dev220 | blend60 | 2 | taxable | category | tax_class | 0.6766 | no |
| wrong | dev220 | blend60 | 2 | 担当課 | org | account | 0.7539 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9167 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.5445 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.6698 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.8934 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7923 | no |
| wrong | dev220 | blend70 | 1 | 随意契約理由 | text | category | 0.5218 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9151 | yes |
| wrong | dev220 | blend70 | 2 | city | address | id | 0.5475 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9781 | no |
| wrong | dev220 | blend70 | 2 | description | text | category | 0.5222 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.9200 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.6276 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7788 | no |
| critical | dev220 | ft | 1 | credit limit | amount | quantity | 0.6601 | yes |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9496 | yes |
| wrong | dev220 | ft | 1 | city | address | id | 0.6688 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.5371 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9396 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.8728 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.6887 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9473 | yes |
| unknown | dev220 | ft | 2 | taxable | category | unknown | 0.4804 | no |
| wrong | dev220 | ft | 2 | city | address | id | 0.7791 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9774 | no |
| wrong | dev220 | ft | 2 | description | text | category | 0.7367 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9775 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.8535 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.5330 | no |
| other_ng | general | blend50 | 1 | dbpedia_score | other | rate | 0.8289 | no |
| other_ng | general | blend50 | 1 | episode | other | id | 0.7555 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.5136 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.9621 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9080 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.4404 | no |
| unknown | general | blend50 | 1 | bib | id | unknown | 0.4630 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.4636 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.5537 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.8678 | no |
| unknown | general | blend50 | 1 | pelicula | text | unknown | 0.4659 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.3764 | no |
| unknown | general | blend50 | 1 | source | category | unknown | 0.4989 | no |
| unknown | general | blend50 | 1 | study | text | unknown | 0.4855 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4798 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9846 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.3703 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 0.9961 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8797 | no |
| unknown | general | blend50 | 1 | 読み方 | address | unknown | 0.3859 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.5375 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.8272 | no |
| wrong | general | blend50 | 1 | goal | id | category | 0.6883 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9124 | no |
| wrong | general | blend50 | 1 | place | org | address | 0.8968 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.5878 | no |
| wrong | general | blend50 | 1 | ステーション名 | org | address | 0.9351 | no |
| other_ng | general | blend50 | 2 | dbpedia_score | other | rate | 0.8565 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.7492 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.9748 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.9496 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.4821 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.5437 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.8863 | no |
| unknown | general | blend50 | 2 | lda | text | unknown | 0.4748 | no |
| unknown | general | blend50 | 2 | pelicula | text | unknown | 0.4866 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.3979 | no |
| unknown | general | blend50 | 2 | raw | category | unknown | 0.4558 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.4651 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4777 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9846 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.3732 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 0.9940 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.8709 | no |
| unknown | general | blend50 | 2 | 読み方 | address | unknown | 0.3912 | no |
| wrong | general | blend50 | 2 | author | person | org | 0.7473 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.8093 | no |
| wrong | general | blend50 | 2 | goal | id | category | 0.5986 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9131 | no |
| wrong | general | blend50 | 2 | place | org | address | 0.8380 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.5520 | no |
| wrong | general | blend50 | 2 | ステーション名 | org | address | 0.9092 | no |
| wrong | general | blend50 | 2 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | 0.5332 | no |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.6023 | no |
| other_ng | general | blend60 | 1 | dbpedia_score | other | rate | 0.8316 | no |
| other_ng | general | blend60 | 1 | episode | other | id | 0.7302 | no |
| other_ng | general | blend60 | 1 | mt2 | other | category | 0.5078 | no |
| other_ng | general | blend60 | 1 | value | other | rate | 0.9603 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.8897 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.4302 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.4167 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.6405 | no |
| unknown | general | blend60 | 1 | image_level_adj_acc | rate | unknown | 0.8790 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.3914 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.5136 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9860 | no |
| unknown | general | blend60 | 1 | 発生県 | id | unknown | 0.3944 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 0.9953 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8786 | no |
| unknown | general | blend60 | 1 | 読み方 | address | unknown | 0.4608 | no |
| wrong | general | blend60 | 1 | cleaned | text | category | 0.7957 | no |
| wrong | general | blend60 | 1 | goal | id | category | 0.6459 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9228 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.8842 | no |
| wrong | general | blend60 | 1 | source | category | org | 0.5778 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.5698 | no |
| wrong | general | blend60 | 1 | ステーション名 | org | address | 0.9361 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5894 | no |
| other_ng | general | blend60 | 2 | _status_ | other | category | 0.5004 | no |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.5551 | no |
| other_ng | general | blend60 | 2 | dbpedia_score | other | rate | 0.8647 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.7120 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9755 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.9397 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.3942 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.6284 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.9013 | no |
| unknown | general | blend60 | 2 | lda | text | unknown | 0.4945 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.3803 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.5575 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.3946 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9859 | no |
| unknown | general | blend60 | 2 | 発生県 | id | unknown | 0.3543 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 0.9928 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.8682 | no |
| unknown | general | blend60 | 2 | 読み方 | address | unknown | 0.4672 | no |
| wrong | general | blend60 | 2 | author | person | org | 0.7007 | no |
| wrong | general | blend60 | 2 | cleaned | text | category | 0.7743 | no |
| wrong | general | blend60 | 2 | goal | id | category | 0.5383 | no |
| wrong | general | blend60 | 2 | indicator | text | category | 0.5005 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9237 | no |
| wrong | general | blend60 | 2 | place | org | address | 0.8137 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.5269 | no |
| wrong | general | blend60 | 2 | ステーション名 | org | address | 0.9050 | no |
| wrong | general | blend60 | 2 | データセット_キーワード | category | text | 0.5395 | no |
| other_ng | general | blend70 | 1 | _status_ | other | category | 0.5491 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.6715 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.8343 | no |
| other_ng | general | blend70 | 1 | episode | other | id | 0.7049 | no |
| other_ng | general | blend70 | 1 | mt2 | other | category | 0.5915 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9585 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.8715 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.4200 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.4965 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.4764 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.7273 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.8903 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.4553 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5152 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9873 | no |
| unknown | general | blend70 | 1 | 発生県 | id | unknown | 0.4599 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9945 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8776 | no |
| wrong | general | blend70 | 1 | cleaned | text | category | 0.7642 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.6036 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9331 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.8716 | no |
| wrong | general | blend70 | 1 | source | category | org | 0.6735 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.5518 | no |
| wrong | general | blend70 | 1 | ステーション名 | org | address | 0.9371 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6836 | no |
| other_ng | general | blend70 | 2 | _status_ | other | category | 0.5837 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.6166 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.8729 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.6749 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9763 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9297 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.3063 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.7132 | no |
| unknown | general | blend70 | 2 | goal | id | unknown | 0.4780 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9163 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.4424 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.6493 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.4808 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4527 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9872 | no |
| unknown | general | blend70 | 2 | 発生県 | id | unknown | 0.4131 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9916 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.8654 | no |
| unknown | general | blend70 | 2 | 駐車場 | category | unknown | 0.5146 | no |
| wrong | general | blend70 | 2 | author | person | org | 0.6540 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7392 | no |
| wrong | general | blend70 | 2 | indicator | text | category | 0.5719 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9342 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7893 | no |
| wrong | general | blend70 | 2 | source | category | text | 0.5368 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.5018 | no |
| wrong | general | blend70 | 2 | ステーション名 | org | address | 0.9008 | no |
| wrong | general | blend70 | 2 | データセット_キーワード | category | text | 0.6254 | no |
| other_ng | general | ft | 1 | _status_ | other | category | 0.7841 | no |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8794 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.8425 | no |
| other_ng | general | ft | 1 | episode | other | id | 0.6290 | no |
| other_ng | general | ft | 1 | mt2 | other | category | 0.8425 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.5165 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9531 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.8168 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.4730 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.6567 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.6554 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9875 | no |
| unknown | general | ft | 1 | goal | id | unknown | 0.4765 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9242 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.6473 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.7331 | no |
| unknown | general | ft | 1 | year_step_size | quantity | unknown | 0.4978 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9912 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9921 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.8745 | no |
| wrong | general | ft | 1 | cleaned | text | category | 0.6696 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9643 | no |
| wrong | general | ft | 1 | place | org | address | 0.8338 | no |
| wrong | general | ft | 1 | source | category | org | 0.9604 | no |
| wrong | general | ft | 1 | source | category | text | 0.5530 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.5037 | no |
| wrong | general | ft | 1 | ステーション名 | org | address | 0.9401 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.9662 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.6558 | yes |
| other_ng | general | ft | 2 | _status_ | other | category | 0.8334 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.8009 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.8976 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.5372 | no |
| other_ng | general | ft | 2 | mood | other | category | 0.5485 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.5634 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.6918 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9785 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9000 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.2503 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9674 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9614 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.6289 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9246 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9910 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9881 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.8571 | no |
| unknown | general | ft | 2 | 駐車場 | category | unknown | 0.7351 | no |
| wrong | general | ft | 2 | author | person | org | 0.5142 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.6339 | no |
| wrong | general | ft | 2 | indicator | text | category | 0.7860 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9657 | no |
| wrong | general | ft | 2 | place | org | address | 0.7163 | no |
| wrong | general | ft | 2 | source | category | text | 0.7268 | no |
| wrong | general | ft | 2 | source_value | category | text | 0.6832 | no |
| wrong | general | ft | 2 | ステーション名 | org | address | 0.8883 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.8830 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.5893 | no |

### unknown の判定理由

- date_value_evidence_low: 72件
- numeric_top2_too_close: 50件
- numeric_values_not_parseable: 22件
- other_class: 65件
- probability_below_threshold: 174件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 40件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 169件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 95件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
