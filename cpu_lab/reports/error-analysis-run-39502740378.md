# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-20T22:07:18+00:00
使用ファイル数: 40 / 行数: 17288
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | 1 | 490 | 24 | 4 | 26 | 0 |
| business | blend50 | 2 | 490 | 20 | 6 | 30 | 0 |
| business | blend60 | 1 | 490 | 29 | 4 | 21 | 0 |
| business | blend60 | 2 | 490 | 28 | 6 | 21 | 0 |
| business | blend70 | 1 | 490 | 31 | 5 | 22 | 0 |
| business | blend70 | 2 | 490 | 29 | 5 | 20 | 0 |
| business | ft | 1 | 490 | 38 | 6 | 12 | 1 |
| business | ft | 2 | 490 | 32 | 5 | 18 | 0 |
| business2 | blend50 | 1 | 976 | 12 | 5 | 34 | 2 |
| business2 | blend50 | 2 | 976 | 19 | 8 | 36 | 2 |
| business2 | blend60 | 1 | 976 | 11 | 5 | 33 | 4 |
| business2 | blend60 | 2 | 976 | 20 | 8 | 29 | 11 |
| business2 | blend70 | 1 | 976 | 11 | 5 | 30 | 12 |
| business2 | blend70 | 2 | 976 | 21 | 8 | 26 | 13 |
| business2 | ft | 1 | 976 | 14 | 6 | 26 | 14 |
| business2 | ft | 2 | 976 | 27 | 9 | 20 | 14 |
| dev220 | blend50 | 1 | 220 | 6 | 1 | 2 | 0 |
| dev220 | blend50 | 2 | 220 | 4 | 0 | 4 | 0 |
| dev220 | blend60 | 1 | 220 | 5 | 1 | 1 | 0 |
| dev220 | blend60 | 2 | 220 | 4 | 0 | 0 | 0 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 0 | 1 | 0 |
| dev220 | ft | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 5 | 0 | 1 | 0 |
| general | blend50 | 1 | 383 | 6 | 0 | 27 | 5 |
| general | blend50 | 2 | 383 | 7 | 0 | 26 | 5 |
| general | blend60 | 1 | 383 | 10 | 1 | 21 | 5 |
| general | blend60 | 2 | 383 | 7 | 1 | 24 | 6 |
| general | blend70 | 1 | 383 | 11 | 1 | 17 | 5 |
| general | blend70 | 2 | 383 | 9 | 1 | 22 | 6 |
| general | ft | 1 | 383 | 12 | 1 | 16 | 6 |
| general | ft | 2 | 383 | 15 | 2 | 18 | 6 |
| japan_procurement | blend50 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend50 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend60 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 1 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 1 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend50: category→quantity: 11, org→account: 7, category→text: 5, quantity→amount: 4, account→text: 3, amount→quantity: 3, text→category: 2, account→category: 2
- business / blend60: category→quantity: 21, org→account: 7, quantity→amount: 4, category→text: 4, account→text: 3, account→category: 3, amount→quantity: 3, org→address: 2
- business / blend70: category→quantity: 24, org→account: 7, quantity→amount: 4, category→text: 4, account→text: 3, account→category: 3, amount→quantity: 3, org→address: 2
- business / ft: category→quantity: 30, org→account: 7, account→text: 5, quantity→amount: 4, amount→quantity: 4, category→text: 4, account→category: 3, org→address: 2
- business2 / blend50: amount→quantity: 8, account→category: 5, category→text: 5, quantity→amount: 4, quantity→category: 2, id→category: 2, address→org: 1, text→org: 1
- business2 / blend60: amount→quantity: 8, account→category: 5, quantity→amount: 4, category→text: 3, id→category: 2, account→address: 2, text→org: 1, category→quantity: 1
- business2 / blend70: amount→quantity: 8, account→category: 5, quantity→amount: 4, category→text: 3, id→category: 2, account→address: 2, category→id: 2, text→org: 1
- business2 / ft: amount→quantity: 8, category→quantity: 7, quantity→amount: 6, account→category: 5, category→id: 3, id→category: 3, account→address: 2, category→text: 2
- dev220 / blend50: quantity→category: 4, category→text: 2, category→tax_class: 1, category→org: 1, id→quantity: 1, text→category: 1
- dev220 / blend60: quantity→category: 4, category→text: 2, category→org: 1, id→quantity: 1, text→category: 1
- dev220 / blend70: quantity→category: 4, category→text: 3, category→org: 1, id→quantity: 1, text→category: 1
- dev220 / ft: quantity→category: 4, category→text: 3, text→category: 2, category→org: 1, id→quantity: 1
- general / blend50: category→text: 6, quantity→category: 2, address→text: 2, text→category: 2, person→org: 1
- general / blend60: category→text: 6, quantity→category: 2, id→address: 2, address→text: 2, id→quantity: 2, person→org: 1, org→address: 1, category→quantity: 1
- general / blend70: category→text: 8, quantity→category: 2, id→address: 2, category→quantity: 2, address→text: 2, id→quantity: 2, person→org: 1, org→address: 1
- general / ft: category→text: 10, org→address: 2, quantity→category: 2, id→address: 2, category→quantity: 2, address→text: 2, id→quantity: 2, person→org: 1
- japan_procurement / ft: quantity→category: 2

### seedをまたいで再発した誤り

- business / blend50: `department`、org→account（seed 1, seed 2）
- business / blend50: `description`、account→text（seed 1, seed 2）
- business / blend50: `merchant details`、text→category（seed 1, seed 2）
- business / blend50: `mois calendrier`、date→quantity（seed 1, seed 2）
- business / blend50: `portefeuille_nom_et_code`、org→account（seed 1, seed 2）
- business / blend50: `q2a`、category→quantity（seed 1, seed 2）
- business / blend50: `q7`、category→quantity（seed 1, seed 2）
- business / blend50: `q8`、category→quantity（seed 1, seed 2）
- business / blend50: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend50: `title`、category→text（seed 1, seed 2）
- business / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend60: `department`、org→account（seed 1, seed 2）
- business / blend60: `description`、account→text（seed 1, seed 2）
- business / blend60: `entitiy`、org→account（seed 1, seed 2）
- business / blend60: `merchant details`、text→category（seed 1, seed 2）
- business / blend60: `mois calendrier`、date→quantity（seed 1, seed 2）
- business / blend60: `publisher label`、org→address（seed 1, seed 2）
- business / blend60: `q2a`、category→quantity（seed 1, seed 2）
- business / blend60: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend60: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend60: `q5a`、category→quantity（seed 1, seed 2）
- business / blend60: `q6`、category→quantity（seed 1, seed 2）
- business / blend60: `q7`、category→quantity（seed 1, seed 2）
- business / blend60: `q8`、category→quantity（seed 1, seed 2）
- business / blend60: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend60: `title`、category→text（seed 1, seed 2）
- business / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q4b_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `title`、category→text（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `net current expenditure - max english county councils`、amount→quantity（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q4a`、category→quantity（seed 1, seed 2）
- business / ft: `q4b_1`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `regions`、address→category（seed 1, seed 2）
- business / ft: `regrp_nom`、account→text（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `title`、category→text（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `contravention`、category→text（seed 1, seed 2）
- business2 / blend50: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend50: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend50: `scheme`、id→category（seed 1, seed 2）
- business2 / blend50: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend50: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend50: `type`、account→category（seed 1, seed 2）
- business2 / blend50: `type of expenditure`、account→category（seed 1, seed 2）
- business2 / blend60: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend60: `scheme`、id→category（seed 1, seed 2）
- business2 / blend60: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend60: `service`、account→address（seed 1, seed 2）
- business2 / blend60: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend60: `type`、account→category（seed 1, seed 2）
- business2 / blend60: `type of expenditure`、account→category（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `scheme_description`、category→text（seed 1, seed 2）
- business2 / blend70: `service`、account→address（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / blend70: `type of expenditure`、account→category（seed 1, seed 2）
- business2 / ft: `imd19_national_decile`、category→id（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `proceeds-disp-surplus-assets_prods-vente-biens-excdnt`、amount→quantity（seed 1, seed 2）
- business2 / ft: `returns`、quantity→amount（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service`、account→address（seed 1, seed 2）
- business2 / ft: `tenure_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- business2 / ft: `type of expenditure`、account→category（seed 1, seed 2）
- dev220 / blend50: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend50: `terms`、category→text（seed 1, seed 2）
- dev220 / blend60: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend60: `terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `terms`、category→text（seed 1, seed 2）
- general / blend50: `cleaned`、text→category（seed 1, seed 2）
- general / blend50: `keyword`、category→text（seed 1, seed 2）
- general / blend50: `raw`、category→text（seed 1, seed 2）
- general / blend50: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend50: `読み方`、address→text（seed 1, seed 2）
- general / blend60: `goal`、id→quantity（seed 1, seed 2）
- general / blend60: `keyword`、category→text（seed 1, seed 2）
- general / blend60: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend60: `発生県`、id→address（seed 1, seed 2）
- general / blend60: `読み方`、address→text（seed 1, seed 2）
- general / blend70: `attrition`、category→quantity（seed 1, seed 2）
- general / blend70: `goal`、id→quantity（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / blend70: `読み方`、address→text（seed 1, seed 2）
- general / ft: `attrition`、category→quantity（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `データセット_キーワード`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）
- general / ft: `読み方`、address→text（seed 1, seed 2）
- japan_procurement / ft: `50,000,000円以上150,000,000円未満件数`、quantity→category（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.9753 | yes |
| critical | business | blend50 | 1 | # invoices paid within 5 days | quantity | amount | 0.9617 | yes |
| critical | business | blend50 | 1 | mois calendrier | date | quantity | 0.8743 | yes |
| critical | business | blend50 | 1 | total invoices paid | quantity | amount | 0.9976 | yes |
| unknown | business | blend50 | 1 | agebann | category | unknown | 0.4403 | no |
| unknown | business | blend50 | 1 | année civile/mois | date | unknown | 0.5264 | no |
| unknown | business | blend50 | 1 | australian sourced goods | amount | unknown | 0.3217 | no |
| unknown | business | blend50 | 1 | australian sourced services | amount | unknown | 0.4821 | no |
| unknown | business | blend50 | 1 | commodity-title_en | product | unknown | 0.4468 | no |
| unknown | business | blend50 | 1 | commodity-title_fr | product | unknown | 0.4250 | no |
| unknown | business | blend50 | 1 | d1 | category | unknown | 0.4560 | no |
| unknown | business | blend50 | 1 | defence services value | amount | unknown | 0.5433 | no |
| unknown | business | blend50 | 1 | entitiy | org | unknown | 0.4943 | no |
| unknown | business | blend50 | 1 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend50 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9488 | no |
| unknown | business | blend50 | 1 | grant in dollars | amount | unknown | 0.6040 | no |
| unknown | business | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5146 | no |
| unknown | business | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5082 | no |
| unknown | business | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.4961 | no |
| unknown | business | blend50 | 1 | overseas sourced goods | amount | unknown | 0.3509 | no |
| unknown | business | blend50 | 1 | overseas sourced services | amount | unknown | 0.4927 | no |
| unknown | business | blend50 | 1 | q3_2 | category | unknown | 0.4999 | no |
| unknown | business | blend50 | 1 | q5b | category | unknown | 0.4885 | no |
| unknown | business | blend50 | 1 | quarter | date | unknown | 0.9935 | no |
| unknown | business | blend50 | 1 | quarterno | date | unknown | 0.9875 | no |
| unknown | business | blend50 | 1 | regrp_nom | account | unknown | 0.4407 | no |
| unknown | business | blend50 | 1 | respnum$ | id | unknown | 0.4244 | no |
| unknown | business | blend50 | 1 | tournée | id | unknown | 0.4854 | no |
| unknown | business | blend50 | 1 | 目名 | category | unknown | 0.9815 | no |
| unknown | business | blend50 | 1 | 科名 | category | unknown | 0.8973 | no |
| wrong | business | blend50 | 1 | class-title_en | category | text | 0.8219 | no |
| wrong | business | blend50 | 1 | class-title_fr | category | text | 0.8798 | no |
| wrong | business | blend50 | 1 | d2 | category | quantity | 0.5126 | no |
| wrong | business | blend50 | 1 | d6 | category | quantity | 0.5765 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.8535 | no |
| wrong | business | blend50 | 1 | department | org | account | 0.9864 | no |
| wrong | business | blend50 | 1 | description | account | text | 0.7599 | no |
| wrong | business | blend50 | 1 | family-title_fr | category | text | 0.5168 | no |
| wrong | business | blend50 | 1 | merchant details | text | category | 0.8466 | no |
| wrong | business | blend50 | 1 | portefeuille_nom_et_code | org | account | 0.5449 | no |
| wrong | business | blend50 | 1 | publisher label | org | address | 0.5227 | no |
| wrong | business | blend50 | 1 | q2a | category | quantity | 0.5101 | no |
| wrong | business | blend50 | 1 | q3_1 | category | quantity | 0.5059 | no |
| wrong | business | blend50 | 1 | q4b_1 | category | quantity | 0.6431 | no |
| wrong | business | blend50 | 1 | q6 | category | quantity | 0.5166 | no |
| wrong | business | blend50 | 1 | q7 | category | quantity | 0.5389 | no |
| wrong | business | blend50 | 1 | q8 | category | quantity | 0.5339 | no |
| wrong | business | blend50 | 1 | regions | address | category | 0.6109 | no |
| wrong | business | blend50 | 1 | regrp_sommaire | account | category | 0.5300 | no |
| wrong | business | blend50 | 1 | title | category | text | 0.9033 | no |
| critical | business | blend50 | 2 | mois calendrier | date | quantity | 0.5726 | yes |
| critical | business | blend50 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6792 | yes |
| critical | business | blend50 | 2 | net current expenditure - max english county councils | amount | quantity | 0.6577 | yes |
| critical | business | blend50 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7136 | yes |
| critical | business | blend50 | 2 | respnum$ | id | quantity | 0.7205 | yes |
| critical | business | blend50 | 2 | total invoices paid | quantity | amount | 0.9817 | yes |
| unknown | business | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6009 | no |
| unknown | business | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5644 | no |
| unknown | business | blend50 | 2 | agebann | category | unknown | 0.4366 | no |
| unknown | business | blend50 | 2 | année civile/mois | date | unknown | 0.5264 | no |
| unknown | business | blend50 | 2 | australian sourced goods | amount | unknown | 0.2951 | no |
| unknown | business | blend50 | 2 | australian sourced services | amount | unknown | 0.4628 | no |
| unknown | business | blend50 | 2 | class-title_en | category | unknown | 0.4715 | no |
| unknown | business | blend50 | 2 | class-title_fr | category | unknown | 0.4494 | no |
| unknown | business | blend50 | 2 | commodity-title_fr | product | unknown | 0.4710 | no |
| unknown | business | blend50 | 2 | d1 | category | unknown | 0.4267 | no |
| unknown | business | blend50 | 2 | d2 | category | unknown | 0.3708 | no |
| unknown | business | blend50 | 2 | d6 | category | unknown | 0.4268 | no |
| unknown | business | blend50 | 2 | defence services value | amount | unknown | 0.5426 | no |
| unknown | business | blend50 | 2 | entitiy | org | unknown | 0.4878 | no |
| unknown | business | blend50 | 2 | family | id | unknown | 0.3620 | no |
| unknown | business | blend50 | 2 | financial year 2017/18 | date | unknown | 0.9986 | no |
| unknown | business | blend50 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9488 | no |
| unknown | business | blend50 | 2 | grant in dollars | amount | unknown | 0.6017 | no |
| unknown | business | blend50 | 2 | number-of-disputes_nombre-de-différends | quantity | unknown | 0.4911 | no |
| unknown | business | blend50 | 2 | overseas sourced goods | amount | unknown | 0.3514 | no |
| unknown | business | blend50 | 2 | overseas sourced services | amount | unknown | 0.4670 | no |
| unknown | business | blend50 | 2 | q3_1 | category | unknown | 0.4929 | no |
| unknown | business | blend50 | 2 | q3_2 | category | unknown | 0.4865 | no |
| unknown | business | blend50 | 2 | q4b_1 | category | unknown | 0.4701 | no |
| unknown | business | blend50 | 2 | q6 | category | unknown | 0.4991 | no |
| unknown | business | blend50 | 2 | quarter | date | unknown | 0.9953 | no |
| unknown | business | blend50 | 2 | quarterno | date | unknown | 0.9799 | no |
| unknown | business | blend50 | 2 | segment-title_en | category | unknown | 0.4649 | no |
| unknown | business | blend50 | 2 | 目名 | category | unknown | 0.9897 | no |
| unknown | business | blend50 | 2 | 科名 | category | unknown | 0.9166 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7987 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.7069 | no |
| wrong | business | blend50 | 2 | department | org | account | 0.9810 | no |
| wrong | business | blend50 | 2 | description | account | text | 0.7195 | no |
| wrong | business | blend50 | 2 | merchant details | text | category | 0.8794 | no |
| wrong | business | blend50 | 2 | portefeuille_nom_et_code | org | account | 0.5064 | no |
| wrong | business | blend50 | 2 | publisher label | org | category | 0.5335 | no |
| wrong | business | blend50 | 2 | purposeofexpenditure | text | account | 0.6731 | no |
| wrong | business | blend50 | 2 | q2a | category | quantity | 0.5004 | no |
| wrong | business | blend50 | 2 | q7 | category | quantity | 0.5337 | no |
| wrong | business | blend50 | 2 | q8 | category | quantity | 0.5314 | no |
| wrong | business | blend50 | 2 | regrp_nom | account | text | 0.6037 | no |
| wrong | business | blend50 | 2 | regrp_sommaire | account | category | 0.5627 | no |
| wrong | business | blend50 | 2 | title | category | text | 0.7622 | no |
| critical | business | blend60 | 1 | # invoices paid within 30 days | quantity | amount | 0.9765 | yes |
| critical | business | blend60 | 1 | # invoices paid within 5 days | quantity | amount | 0.9614 | yes |
| critical | business | blend60 | 1 | mois calendrier | date | quantity | 0.8951 | yes |
| critical | business | blend60 | 1 | total invoices paid | quantity | amount | 0.9980 | yes |
| unknown | business | blend60 | 1 | année civile/mois | date | unknown | 0.6211 | no |
| unknown | business | blend60 | 1 | australian sourced goods | amount | unknown | 0.2736 | no |
| unknown | business | blend60 | 1 | australian sourced services | amount | unknown | 0.3964 | no |
| unknown | business | blend60 | 1 | commodity-title_en | product | unknown | 0.4053 | no |
| unknown | business | blend60 | 1 | commodity-title_fr | product | unknown | 0.3891 | no |
| unknown | business | blend60 | 1 | family-title_fr | category | unknown | 0.4849 | no |
| unknown | business | blend60 | 1 | financial year 2017/18 | date | unknown | 0.9989 | no |
| unknown | business | blend60 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9590 | no |
| unknown | business | blend60 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5621 | no |
| unknown | business | blend60 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5314 | no |
| unknown | business | blend60 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5331 | no |
| unknown | business | blend60 | 1 | overseas sourced goods | amount | unknown | 0.2873 | no |
| unknown | business | blend60 | 1 | portefeuille_nom_et_code | org | unknown | 0.4592 | no |
| unknown | business | blend60 | 1 | q2c | category | unknown | 0.4885 | no |
| unknown | business | blend60 | 1 | quarter | date | unknown | 0.9935 | no |
| unknown | business | blend60 | 1 | quarterno | date | unknown | 0.9895 | no |
| unknown | business | blend60 | 1 | regrp_nom | account | unknown | 0.4689 | no |
| unknown | business | blend60 | 1 | respnum$ | id | unknown | 0.4516 | no |
| unknown | business | blend60 | 1 | tournée | id | unknown | 0.5494 | no |
| unknown | business | blend60 | 1 | 目名 | category | unknown | 0.9819 | no |
| unknown | business | blend60 | 1 | 科名 | category | unknown | 0.9070 | no |
| wrong | business | blend60 | 1 | agebann | category | quantity | 0.5114 | no |
| wrong | business | blend60 | 1 | class-title_en | category | text | 0.8313 | no |
| wrong | business | blend60 | 1 | class-title_fr | category | text | 0.9014 | no |
| wrong | business | blend60 | 1 | d1 | category | quantity | 0.5447 | no |
| wrong | business | blend60 | 1 | d2 | category | quantity | 0.5946 | no |
| wrong | business | blend60 | 1 | d6 | category | quantity | 0.6574 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.8269 | no |
| wrong | business | blend60 | 1 | department | org | account | 0.9854 | no |
| wrong | business | blend60 | 1 | description | account | text | 0.8072 | no |
| wrong | business | blend60 | 1 | entitiy | org | account | 0.5923 | no |
| wrong | business | blend60 | 1 | merchant details | text | category | 0.8632 | no |
| wrong | business | blend60 | 1 | publisher label | org | address | 0.6146 | no |
| wrong | business | blend60 | 1 | q2a | category | quantity | 0.6070 | no |
| wrong | business | blend60 | 1 | q3_1 | category | quantity | 0.6032 | no |
| wrong | business | blend60 | 1 | q3_2 | category | quantity | 0.5962 | no |
| wrong | business | blend60 | 1 | q4a | category | quantity | 0.5365 | no |
| wrong | business | blend60 | 1 | q4b_1 | category | quantity | 0.7080 | no |
| wrong | business | blend60 | 1 | q5a | category | quantity | 0.5783 | no |
| wrong | business | blend60 | 1 | q5b | category | quantity | 0.5822 | no |
| wrong | business | blend60 | 1 | q6 | category | quantity | 0.6128 | no |
| wrong | business | blend60 | 1 | q7 | category | quantity | 0.6299 | no |
| wrong | business | blend60 | 1 | q8 | category | quantity | 0.6259 | no |
| wrong | business | blend60 | 1 | regions | address | category | 0.6791 | no |
| wrong | business | blend60 | 1 | regrp_sommaire | account | category | 0.6021 | no |
| wrong | business | blend60 | 1 | title | category | text | 0.9143 | no |
| critical | business | blend60 | 2 | mois calendrier | date | quantity | 0.5330 | yes |
| critical | business | blend60 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6751 | yes |
| critical | business | blend60 | 2 | net current expenditure - max english county councils | amount | quantity | 0.7109 | yes |
| critical | business | blend60 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7216 | yes |
| critical | business | blend60 | 2 | respnum$ | id | quantity | 0.7562 | yes |
| critical | business | blend60 | 2 | total invoices paid | quantity | amount | 0.9790 | yes |
| unknown | business | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5271 | no |
| unknown | business | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5142 | no |
| unknown | business | blend60 | 2 | année civile/mois | date | unknown | 0.6211 | no |
| unknown | business | blend60 | 2 | australian sourced goods | amount | unknown | 0.2417 | no |
| unknown | business | blend60 | 2 | australian sourced services | amount | unknown | 0.3732 | no |
| unknown | business | blend60 | 2 | class-title_fr | category | unknown | 0.4899 | no |
| unknown | business | blend60 | 2 | d1 | category | unknown | 0.4035 | no |
| unknown | business | blend60 | 2 | d2 | category | unknown | 0.3707 | no |
| unknown | business | blend60 | 2 | d6 | category | unknown | 0.4778 | no |
| unknown | business | blend60 | 2 | department | org | unknown | 0.4619 | no |
| unknown | business | blend60 | 2 | family | id | unknown | 0.3446 | no |
| unknown | business | blend60 | 2 | financial year 2017/18 | date | unknown | 0.9989 | no |
| unknown | business | blend60 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9590 | no |
| unknown | business | blend60 | 2 | overseas sourced goods | amount | unknown | 0.2859 | no |
| unknown | business | blend60 | 2 | q4b_1 | category | unknown | 0.4858 | no |
| unknown | business | blend60 | 2 | quarter | date | unknown | 0.9957 | no |
| unknown | business | blend60 | 2 | quarterno | date | unknown | 0.9803 | no |
| unknown | business | blend60 | 2 | regions | address | unknown | 0.4681 | no |
| unknown | business | blend60 | 2 | tournée | id | unknown | 0.4849 | no |
| unknown | business | blend60 | 2 | 目名 | category | unknown | 0.9917 | no |
| unknown | business | blend60 | 2 | 科名 | category | unknown | 0.9302 | no |
| wrong | business | blend60 | 2 | agebann | category | id | 0.5003 | no |
| wrong | business | blend60 | 2 | class-title_en | category | product | 0.5657 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7611 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.7229 | no |
| wrong | business | blend60 | 2 | department | org | account | 0.9788 | no |
| wrong | business | blend60 | 2 | description | account | text | 0.7587 | no |
| wrong | business | blend60 | 2 | entitiy | org | account | 0.5845 | no |
| wrong | business | blend60 | 2 | merchant details | text | category | 0.9025 | no |
| wrong | business | blend60 | 2 | portefeuille_nom_et_code | org | category | 0.5264 | no |
| wrong | business | blend60 | 2 | procurementclassification:proclasslabel | account | category | 0.5053 | no |
| wrong | business | blend60 | 2 | publisher label | org | address | 0.5187 | no |
| wrong | business | blend60 | 2 | purposeofexpenditure | text | account | 0.6180 | no |
| wrong | business | blend60 | 2 | q2a | category | quantity | 0.5953 | no |
| wrong | business | blend60 | 2 | q3_1 | category | quantity | 0.5875 | no |
| wrong | business | blend60 | 2 | q3_2 | category | quantity | 0.5801 | no |
| wrong | business | blend60 | 2 | q5a | category | quantity | 0.5705 | no |
| wrong | business | blend60 | 2 | q6 | category | quantity | 0.5918 | no |
| wrong | business | blend60 | 2 | q7 | category | quantity | 0.6238 | no |
| wrong | business | blend60 | 2 | q8 | category | quantity | 0.6229 | no |
| wrong | business | blend60 | 2 | regrp_nom | account | text | 0.6654 | no |
| wrong | business | blend60 | 2 | regrp_sommaire | account | category | 0.6413 | no |
| wrong | business | blend60 | 2 | title | category | text | 0.7450 | no |
| critical | business | blend70 | 1 | # invoices paid within 30 days | quantity | amount | 0.9776 | yes |
| critical | business | blend70 | 1 | # invoices paid within 5 days | quantity | amount | 0.9611 | yes |
| critical | business | blend70 | 1 | mois calendrier | date | quantity | 0.9159 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9985 | yes |
| critical | business | blend70 | 1 | tournée | id | quantity | 0.6404 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.2256 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.4577 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4716 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4530 | no |
| unknown | business | blend70 | 1 | d5 | category | unknown | 0.4586 | no |
| unknown | business | blend70 | 1 | d7 | category | unknown | 0.4652 | no |
| unknown | business | blend70 | 1 | family-title_en | category | unknown | 0.4959 | no |
| unknown | business | blend70 | 1 | family-title_fr | category | unknown | 0.4529 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9992 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9693 | no |
| unknown | business | blend70 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.6096 | no |
| unknown | business | blend70 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5547 | no |
| unknown | business | blend70 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5700 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.3341 | no |
| unknown | business | blend70 | 1 | portefeuille_nom_et_code | org | unknown | 0.3735 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9935 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9915 | no |
| unknown | business | blend70 | 1 | regrp_nom | account | unknown | 0.4978 | no |
| unknown | business | blend70 | 1 | respnum$ | id | unknown | 0.5112 | no |
| unknown | business | blend70 | 1 | service | account | unknown | 0.4951 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9822 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9167 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.5825 | no |
| wrong | business | blend70 | 1 | class-title_en | category | text | 0.8407 | no |
| wrong | business | blend70 | 1 | class-title_fr | category | text | 0.9230 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6335 | no |
| wrong | business | blend70 | 1 | d2 | category | quantity | 0.6766 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7383 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8003 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9843 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8546 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6903 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.8797 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.7066 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7038 | no |
| wrong | business | blend70 | 1 | q2c | category | quantity | 0.5615 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.7004 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.6924 | no |
| wrong | business | blend70 | 1 | q4a | category | quantity | 0.6254 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | quantity | 0.7728 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6727 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6760 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7090 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7210 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7179 | no |
| wrong | business | blend70 | 1 | regions | address | category | 0.7472 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.6742 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.9254 | no |
| critical | business | blend70 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6709 | yes |
| critical | business | blend70 | 2 | net current expenditure - max english county councils | amount | quantity | 0.7641 | yes |
| critical | business | blend70 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7296 | yes |
| critical | business | blend70 | 2 | respnum$ | id | quantity | 0.7918 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9762 | yes |
| unknown | business | blend70 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5444 | no |
| unknown | business | blend70 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5938 | no |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.1883 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.2836 | no |
| unknown | business | blend70 | 2 | d1 | category | unknown | 0.4457 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4154 | no |
| unknown | business | blend70 | 2 | department | org | unknown | 0.4075 | no |
| unknown | business | blend70 | 2 | family | id | unknown | 0.3583 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9992 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9692 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.4934 | no |
| unknown | business | blend70 | 2 | overseas sourced goods | amount | unknown | 0.2244 | no |
| unknown | business | blend70 | 2 | purpose | account | unknown | 0.4761 | no |
| unknown | business | blend70 | 2 | q5b | category | unknown | 0.4991 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9961 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9808 | no |
| unknown | business | blend70 | 2 | regions | address | unknown | 0.4800 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.4045 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9937 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9437 | no |
| wrong | business | blend70 | 2 | agebann | category | id | 0.5639 | no |
| wrong | business | blend70 | 2 | class-title_en | category | product | 0.6599 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.5288 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7235 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7390 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9767 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.7980 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.6812 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9256 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | category | 0.6132 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.5680 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.5946 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.5629 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.6902 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.6822 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6737 | no |
| wrong | business | blend70 | 2 | q4b_1 | category | quantity | 0.5136 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6637 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6845 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7139 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7144 | no |
| wrong | business | blend70 | 2 | regrp_nom | account | text | 0.7271 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.7200 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.7278 | no |
| critical | business | ft | 1 | # invoices paid within 30 days | quantity | amount | 0.9809 | yes |
| critical | business | ft | 1 | # invoices paid within 5 days | quantity | amount | 0.9602 | yes |
| critical | business | ft | 1 | mois calendrier | date | quantity | 0.9782 | yes |
| critical | business | ft | 1 | net current expenditure - max english county councils | amount | quantity | 0.6246 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9999 | yes |
| critical | business | ft | 1 | tournée | id | quantity | 0.9132 | yes |
| other_ng | business | ft | 1 | 学名 | other | text | 0.6700 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.2561 | no |
| unknown | business | ft | 1 | family-title_en | category | unknown | 0.3764 | no |
| unknown | business | ft | 1 | family-title_fr | category | unknown | 0.4915 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 1.0000 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 1.0000 | no |
| unknown | business | ft | 1 | overseas sourced goods | amount | unknown | 0.4746 | no |
| unknown | business | ft | 1 | portefeuille_nom_et_code | org | unknown | 0.4839 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9935 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9975 | no |
| unknown | business | ft | 1 | service | account | unknown | 0.4518 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9834 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9459 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.7957 | no |
| wrong | business | ft | 1 | australian sourced services | amount | org | 0.6539 | no |
| wrong | business | ft | 1 | class-title_en | category | text | 0.8691 | no |
| wrong | business | ft | 1 | class-title_fr | category | text | 0.9879 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.8997 | no |
| wrong | business | ft | 1 | d2 | category | quantity | 0.9225 | no |
| wrong | business | ft | 1 | d5 | category | quantity | 0.6331 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9812 | no |
| wrong | business | ft | 1 | d7 | category | quantity | 0.6468 | no |
| wrong | business | ft | 1 | department | org | account | 0.7205 | no |
| wrong | business | ft | 1 | department | org | account | 0.9812 | no |
| wrong | business | ft | 1 | description | account | text | 0.9966 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.9842 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9293 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9823 | no |
| wrong | business | ft | 1 | q1a | category | quantity | 0.5619 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9945 | no |
| wrong | business | ft | 1 | q2b | category | quantity | 0.6125 | no |
| wrong | business | ft | 1 | q2c | category | quantity | 0.7991 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9922 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.9813 | no |
| wrong | business | ft | 1 | q4a | category | quantity | 0.8920 | no |
| wrong | business | ft | 1 | q4b_1 | category | quantity | 0.9674 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9561 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9572 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9977 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9943 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9940 | no |
| wrong | business | ft | 1 | regions | address | category | 0.9517 | no |
| wrong | business | ft | 1 | regrp_nom | account | text | 0.5847 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.8905 | no |
| wrong | business | ft | 1 | title | category | text | 0.9584 | no |
| critical | business | ft | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6586 | yes |
| critical | business | ft | 2 | net current expenditure - max english county councils | amount | quantity | 0.9237 | yes |
| critical | business | ft | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7537 | yes |
| critical | business | ft | 2 | respnum$ | id | quantity | 0.8986 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.9681 | yes |
| unknown | business | ft | 2 | account_name | account | unknown | 0.3968 | no |
| unknown | business | ft | 2 | australian sourced goods | amount | unknown | 0.2664 | no |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.3729 | no |
| unknown | business | ft | 2 | d1 | category | unknown | 0.5721 | no |
| unknown | business | ft | 2 | d2 | category | unknown | 0.5495 | no |
| unknown | business | ft | 2 | d5 | category | unknown | 0.4746 | no |
| unknown | business | ft | 2 | department | org | unknown | 0.4894 | no |
| unknown | business | ft | 2 | family | id | unknown | 0.4021 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9999 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9999 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.3747 | no |
| unknown | business | ft | 2 | overseas sourced goods | amount | unknown | 0.3177 | no |
| unknown | business | ft | 2 | q2c | category | unknown | 0.4960 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9973 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9821 | no |
| unknown | business | ft | 2 | tournée | id | unknown | 0.4373 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9998 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9845 | no |
| wrong | business | ft | 2 | agebann | category | id | 0.7548 | no |
| wrong | business | ft | 2 | class-title_en | category | product | 0.9424 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.6818 | no |
| wrong | business | ft | 2 | department | org | account | 0.6107 | no |
| wrong | business | ft | 2 | department | org | account | 0.7870 | no |
| wrong | business | ft | 2 | department | org | account | 0.9702 | no |
| wrong | business | ft | 2 | description | account | text | 0.9158 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.9713 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9948 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | category | 0.8734 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.7563 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.8224 | no |
| wrong | business | ft | 2 | purpose | account | text | 0.6794 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9751 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9661 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9545 | no |
| wrong | business | ft | 2 | q4a | category | quantity | 0.6599 | no |
| wrong | business | ft | 2 | q4b_1 | category | quantity | 0.5971 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9432 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.6249 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9627 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9841 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9888 | no |
| wrong | business | ft | 2 | regions | address | category | 0.5700 | no |
| wrong | business | ft | 2 | regrp_nom | account | text | 0.9122 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.9559 | no |
| wrong | business | ft | 2 | title | category | text | 0.6761 | no |
| critical | business2 | blend50 | 1 | # invoices paid within 30 days | quantity | amount | 0.9759 | yes |
| critical | business2 | blend50 | 1 | # invoices paid within 5 days | quantity | amount | 0.9677 | yes |
| critical | business2 | blend50 | 1 | miscellaneous_divers | amount | quantity | 0.9785 | yes |
| critical | business2 | blend50 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7960 | yes |
| critical | business2 | blend50 | 1 | total invoices paid | quantity | amount | 0.9976 | yes |
| other_ng | business2 | blend50 | 1 | a2 floorspace gains sqm | other | quantity | 0.8867 | no |
| other_ng | business2 | blend50 | 1 | average bids per property | other | rate | 0.9191 | no |
| unknown | business2 | blend50 | 1 | amt-units_mnt-unite | category | unknown | 0.6250 | no |
| unknown | business2 | blend50 | 1 | bike_stands | quantity | unknown | 0.4792 | no |
| unknown | business2 | blend50 | 1 | construction_age_band | category | unknown | 0.3577 | no |
| unknown | business2 | blend50 | 1 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend50 | 1 | fine | amount | unknown | 0.4409 | no |
| unknown | business2 | blend50 | 1 | fuel_poverty | rate | unknown | 0.9023 | no |
| unknown | business2 | blend50 | 1 | imd19_national_decile | category | unknown | 0.3238 | no |
| unknown | business2 | blend50 | 1 | monitor | id | unknown | 0.4155 | no |
| unknown | business2 | blend50 | 1 | montant | amount | unknown | 0.9982 | no |
| unknown | business2 | blend50 | 1 | name | org | unknown | 0.4694 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5199 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5605 | no |
| unknown | business2 | blend50 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5360 | no |
| unknown | business2 | blend50 | 1 | numbers of | date | unknown | 0.4962 | no |
| unknown | business2 | blend50 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9786 | no |
| unknown | business2 | blend50 | 1 | projection | category | unknown | 0.4486 | no |
| unknown | business2 | blend50 | 1 | recipients | quantity | unknown | 0.3877 | no |
| unknown | business2 | blend50 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5839 | no |
| unknown | business2 | blend50 | 1 | returns | quantity | unknown | 0.6067 | no |
| unknown | business2 | blend50 | 1 | service | account | unknown | 0.4787 | no |
| unknown | business2 | blend50 | 1 | terminal | address | unknown | 0.4879 | no |
| unknown | business2 | blend50 | 1 | terrace | quantity | unknown | 0.4673 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9978 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend50 | 1 | tlist(q1) | date | unknown | 0.9954 | no |
| unknown | business2 | blend50 | 1 | value | amount | unknown | 0.5015 | no |
| unknown | business2 | blend50 | 1 | value | quantity | unknown | 0.5168 | no |
| unknown | business2 | blend50 | 1 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend50 | 1 | volume (10^3 m3) | quantity | unknown | 0.9918 | no |
| unknown | business2 | blend50 | 1 | volume (mcf) | quantity | unknown | 0.9969 | no |
| unknown | business2 | blend50 | 1 | warddesc | address | unknown | 0.4861 | no |
| unknown | business2 | blend50 | 1 | 販売 | date | unknown | 0.9847 | no |
| wrong | business2 | blend50 | 1 | contravention | category | text | 0.6606 | no |
| wrong | business2 | blend50 | 1 | health service executive area | address | org | 0.5146 | no |
| wrong | business2 | blend50 | 1 | number_habitable_rooms | quantity | category | 0.5005 | no |
| wrong | business2 | blend50 | 1 | scheme | id | category | 0.9594 | no |
| wrong | business2 | blend50 | 1 | scheme_description | category | text | 0.6456 | no |
| wrong | business2 | blend50 | 1 | type | account | category | 0.9427 | no |
| wrong | business2 | blend50 | 1 | type of expenditure | account | category | 0.7808 | no |
| critical | business2 | blend50 | 2 | miscellaneous_divers | amount | quantity | 0.8519 | yes |
| critical | business2 | blend50 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6755 | yes |
| critical | business2 | blend50 | 2 | net current expenditure - max english county councils | amount | quantity | 0.6357 | yes |
| critical | business2 | blend50 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7019 | yes |
| critical | business2 | blend50 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8204 | yes |
| critical | business2 | blend50 | 2 | recipients | quantity | id | 0.5387 | yes |
| critical | business2 | blend50 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.6938 | yes |
| critical | business2 | blend50 | 2 | total invoices paid | quantity | amount | 0.9810 | yes |
| other_ng | business2 | blend50 | 2 | a2 floorspace gains sqm | other | quantity | 0.9042 | no |
| other_ng | business2 | blend50 | 2 | average bids per property | other | rate | 0.6915 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5934 | no |
| unknown | business2 | blend50 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5580 | no |
| unknown | business2 | blend50 | 2 | bike_stands | quantity | unknown | 0.4065 | no |
| unknown | business2 | blend50 | 2 | construction_age_band | category | unknown | 0.3745 | no |
| unknown | business2 | blend50 | 2 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend50 | 2 | epc_score_known | category | unknown | 0.4847 | no |
| unknown | business2 | blend50 | 2 | fuel_poverty | rate | unknown | 0.9552 | no |
| unknown | business2 | blend50 | 2 | habitatcode | id | unknown | 0.3169 | no |
| unknown | business2 | blend50 | 2 | imd19_national_decile | category | unknown | 0.3848 | no |
| unknown | business2 | blend50 | 2 | monitor | id | unknown | 0.4271 | no |
| unknown | business2 | blend50 | 2 | montant | amount | unknown | 0.9982 | no |
| unknown | business2 | blend50 | 2 | numbers of | date | unknown | 0.5015 | no |
| unknown | business2 | blend50 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9983 | no |
| unknown | business2 | blend50 | 2 | programme | category | unknown | 0.4755 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4209 | no |
| unknown | business2 | blend50 | 2 | projection | category | unknown | 0.4590 | no |
| unknown | business2 | blend50 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5283 | no |
| unknown | business2 | blend50 | 2 | returns | quantity | unknown | 0.5719 | no |
| unknown | business2 | blend50 | 2 | service | account | unknown | 0.4719 | no |
| unknown | business2 | blend50 | 2 | situtation | address | unknown | 0.4309 | no |
| unknown | business2 | blend50 | 2 | super output area 2011 name | address | unknown | 0.4798 | no |
| unknown | business2 | blend50 | 2 | surveyname | text | unknown | 0.5000 | no |
| unknown | business2 | blend50 | 2 | terminal | address | unknown | 0.4966 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9978 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend50 | 2 | tlist(q1) | date | unknown | 0.9954 | no |
| unknown | business2 | blend50 | 2 | tree type | category | unknown | 0.4381 | no |
| unknown | business2 | blend50 | 2 | value | amount | unknown | 0.5008 | no |
| unknown | business2 | blend50 | 2 | value | quantity | unknown | 0.5199 | no |
| unknown | business2 | blend50 | 2 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend50 | 2 | volume (10^3 m3) | quantity | unknown | 0.9934 | no |
| unknown | business2 | blend50 | 2 | volume (mcf) | quantity | unknown | 0.9993 | no |
| unknown | business2 | blend50 | 2 | warddesc | address | unknown | 0.3883 | no |
| unknown | business2 | blend50 | 2 | 販売 | date | unknown | 0.9842 | no |
| wrong | business2 | blend50 | 2 | amt-units_mnt-unite | category | id | 0.6490 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5333 | no |
| wrong | business2 | blend50 | 2 | contravention | category | text | 0.5306 | no |
| wrong | business2 | blend50 | 2 | name | org | address | 0.5608 | no |
| wrong | business2 | blend50 | 2 | number_habitable_rooms | quantity | category | 0.6723 | no |
| wrong | business2 | blend50 | 2 | scheme | id | category | 0.7629 | no |
| wrong | business2 | blend50 | 2 | scheme_description | category | text | 0.8382 | no |
| wrong | business2 | blend50 | 2 | service_responsable | account | category | 0.7724 | no |
| wrong | business2 | blend50 | 2 | surveyname | text | org | 0.6642 | no |
| wrong | business2 | blend50 | 2 | type | account | category | 0.9446 | no |
| wrong | business2 | blend50 | 2 | type of expenditure | account | category | 0.6329 | no |
| critical | business2 | blend60 | 1 | # invoices paid within 30 days | quantity | amount | 0.9771 | yes |
| critical | business2 | blend60 | 1 | # invoices paid within 5 days | quantity | amount | 0.9686 | yes |
| critical | business2 | blend60 | 1 | miscellaneous_divers | amount | quantity | 0.9791 | yes |
| critical | business2 | blend60 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7746 | yes |
| critical | business2 | blend60 | 1 | total invoices paid | quantity | amount | 0.9980 | yes |
| other_ng | business2 | blend60 | 1 | a2 floorspace gains sqm | other | quantity | 0.9009 | no |
| other_ng | business2 | blend60 | 1 | a2 floorspace losses sqm | other | quantity | 0.5521 | no |
| other_ng | business2 | blend60 | 1 | average bids per property | other | rate | 0.9314 | no |
| other_ng | business2 | blend60 | 1 | potential_epc_score | other | quantity | 0.5406 | no |
| unknown | business2 | blend60 | 1 | amt-units_mnt-unite | category | unknown | 0.6441 | no |
| unknown | business2 | blend60 | 1 | bike_stands | quantity | unknown | 0.4466 | no |
| unknown | business2 | blend60 | 1 | construction_age_band | category | unknown | 0.3657 | no |
| unknown | business2 | blend60 | 1 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend60 | 1 | fuel_poverty | rate | unknown | 0.8958 | no |
| unknown | business2 | blend60 | 1 | health service executive area | address | unknown | 0.4866 | no |
| unknown | business2 | blend60 | 1 | imd19_national_decile | category | unknown | 0.3872 | no |
| unknown | business2 | blend60 | 1 | monitor | id | unknown | 0.4235 | no |
| unknown | business2 | blend60 | 1 | montant | amount | unknown | 0.9986 | no |
| unknown | business2 | blend60 | 1 | net current expenditure - ave all english county councils | amount | unknown | 0.5672 | no |
| unknown | business2 | blend60 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5588 | no |
| unknown | business2 | blend60 | 1 | net current expenditure - min all english county councils | amount | unknown | 0.5814 | no |
| unknown | business2 | blend60 | 1 | number_habitable_rooms | quantity | unknown | 0.5205 | no |
| unknown | business2 | blend60 | 1 | numbers of | date | unknown | 0.5270 | no |
| unknown | business2 | blend60 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9748 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.4930 | no |
| unknown | business2 | blend60 | 1 | projection | category | unknown | 0.4696 | no |
| unknown | business2 | blend60 | 1 | publication_assuj | id | unknown | 0.4527 | no |
| unknown | business2 | blend60 | 1 | recipients | quantity | unknown | 0.4360 | no |
| unknown | business2 | blend60 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5254 | no |
| unknown | business2 | blend60 | 1 | returns | quantity | unknown | 0.5312 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9990 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend60 | 1 | tlist(q1) | date | unknown | 0.9963 | no |
| unknown | business2 | blend60 | 1 | total_verified_sales | quantity | unknown | 0.5924 | no |
| unknown | business2 | blend60 | 1 | value | amount | unknown | 0.6007 | no |
| unknown | business2 | blend60 | 1 | value | quantity | unknown | 0.6075 | no |
| unknown | business2 | blend60 | 1 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend60 | 1 | volume (10^3 m3) | quantity | unknown | 0.9928 | no |
| unknown | business2 | blend60 | 1 | volume (mcf) | quantity | unknown | 0.9966 | no |
| unknown | business2 | blend60 | 1 | 販売 | date | unknown | 0.9877 | no |
| wrong | business2 | blend60 | 1 | contravention | category | text | 0.6027 | no |
| wrong | business2 | blend60 | 1 | scheme | id | category | 0.9617 | no |
| wrong | business2 | blend60 | 1 | scheme_description | category | text | 0.5760 | no |
| wrong | business2 | blend60 | 1 | service | account | address | 0.5741 | no |
| wrong | business2 | blend60 | 1 | type | account | category | 0.9528 | no |
| wrong | business2 | blend60 | 1 | type of expenditure | account | category | 0.8193 | no |
| critical | business2 | blend60 | 2 | miscellaneous_divers | amount | quantity | 0.8273 | yes |
| critical | business2 | blend60 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6719 | yes |
| critical | business2 | blend60 | 2 | net current expenditure - max english county councils | amount | quantity | 0.6845 | yes |
| critical | business2 | blend60 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7071 | yes |
| critical | business2 | blend60 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.8039 | yes |
| critical | business2 | blend60 | 2 | recipients | quantity | id | 0.6195 | yes |
| critical | business2 | blend60 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7311 | yes |
| critical | business2 | blend60 | 2 | total invoices paid | quantity | amount | 0.9781 | yes |
| other_ng | business2 | blend60 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.6391 | no |
| other_ng | business2 | blend60 | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.6348 | no |
| other_ng | business2 | blend60 | 2 | a1 (retail) floorspace net sqm | other | quantity | 0.6137 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace gains sqm | other | quantity | 0.9220 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace losses sqm | other | quantity | 0.6463 | no |
| other_ng | business2 | blend60 | 2 | a2 floorspace net sqm | other | quantity | 0.6151 | no |
| other_ng | business2 | blend60 | 2 | average bids per property | other | rate | 0.6583 | no |
| other_ng | business2 | blend60 | 2 | b1a floorspace gains sqm | other | quantity | 0.6374 | no |
| other_ng | business2 | blend60 | 2 | b1a floorspace losses sqm | other | quantity | 0.6184 | no |
| other_ng | business2 | blend60 | 2 | d2 floorspace gains sqm | other | quantity | 0.6693 | no |
| other_ng | business2 | blend60 | 2 | d2 floorspace losses sqm | other | quantity | 0.6274 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5181 | no |
| unknown | business2 | blend60 | 2 | # invoices paid within 5 days | quantity | unknown | 0.5219 | no |
| unknown | business2 | blend60 | 2 | bike_stands | quantity | unknown | 0.4687 | no |
| unknown | business2 | blend60 | 2 | construction_age_band | category | unknown | 0.4037 | no |
| unknown | business2 | blend60 | 2 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend60 | 2 | fuel_poverty | rate | unknown | 0.9593 | no |
| unknown | business2 | blend60 | 2 | habitatcode | id | unknown | 0.3691 | no |
| unknown | business2 | blend60 | 2 | imd19_national_decile | category | unknown | 0.4604 | no |
| unknown | business2 | blend60 | 2 | monitor | id | unknown | 0.4543 | no |
| unknown | business2 | blend60 | 2 | montant | amount | unknown | 0.9986 | no |
| unknown | business2 | blend60 | 2 | numbers of | date | unknown | 0.4038 | no |
| unknown | business2 | blend60 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9984 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.3819 | no |
| unknown | business2 | blend60 | 2 | projection | category | unknown | 0.3784 | no |
| unknown | business2 | blend60 | 2 | publication_assuj | id | unknown | 0.4983 | no |
| unknown | business2 | blend60 | 2 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.6122 | no |
| unknown | business2 | blend60 | 2 | returns | quantity | unknown | 0.5083 | no |
| unknown | business2 | blend60 | 2 | situtation | address | unknown | 0.4600 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend60 | 2 | tlist(q1) | date | unknown | 0.9963 | no |
| unknown | business2 | blend60 | 2 | value | amount | unknown | 0.5936 | no |
| unknown | business2 | blend60 | 2 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend60 | 2 | volume (10^3 m3) | quantity | unknown | 0.9947 | no |
| unknown | business2 | blend60 | 2 | volume (mcf) | quantity | unknown | 0.9994 | no |
| unknown | business2 | blend60 | 2 | warddesc | address | unknown | 0.4039 | no |
| unknown | business2 | blend60 | 2 | 販売 | date | unknown | 0.9871 | no |
| wrong | business2 | blend60 | 2 | amt-units_mnt-unite | category | id | 0.7192 | no |
| wrong | business2 | blend60 | 2 | epc_score_known | category | quantity | 0.5628 | no |
| wrong | business2 | blend60 | 2 | name | org | address | 0.5375 | no |
| wrong | business2 | blend60 | 2 | number_habitable_rooms | quantity | category | 0.6135 | no |
| wrong | business2 | blend60 | 2 | programme | category | account | 0.5138 | no |
| wrong | business2 | blend60 | 2 | scheme | id | category | 0.7258 | no |
| wrong | business2 | blend60 | 2 | scheme_description | category | text | 0.8071 | no |
| wrong | business2 | blend60 | 2 | service | account | address | 0.5659 | no |
| wrong | business2 | blend60 | 2 | service_responsable | account | category | 0.7881 | no |
| wrong | business2 | blend60 | 2 | surveyname | text | org | 0.6487 | no |
| wrong | business2 | blend60 | 2 | type | account | category | 0.9551 | no |
| wrong | business2 | blend60 | 2 | type of expenditure | account | category | 0.6417 | no |
| critical | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | amount | 0.9783 | yes |
| critical | business2 | blend70 | 1 | # invoices paid within 5 days | quantity | amount | 0.9695 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9798 | yes |
| critical | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7532 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9985 | yes |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.6752 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.6320 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace net sqm | other | quantity | 0.6012 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.9152 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.6078 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace net sqm | other | quantity | 0.6483 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9438 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace gains sqm | other | quantity | 0.6778 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace losses sqm | other | quantity | 0.5874 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.6461 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace losses sqm | other | quantity | 0.5900 | no |
| other_ng | business2 | blend70 | 1 | potential_epc_score | other | quantity | 0.6214 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6632 | no |
| unknown | business2 | blend70 | 1 | bike_stands | quantity | unknown | 0.4139 | no |
| unknown | business2 | blend70 | 1 | conservation_area_site_id | category | unknown | 0.4910 | no |
| unknown | business2 | blend70 | 1 | construction_age_band | category | unknown | 0.3886 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.8894 | no |
| unknown | business2 | blend70 | 1 | health service executive area | address | unknown | 0.4943 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.4506 | no |
| unknown | business2 | blend70 | 1 | monitor | id | unknown | 0.4574 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 1 | net current expenditure - max english county councils | amount | unknown | 0.5570 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.6025 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms_known | category | unknown | 0.4761 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9710 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.5752 | no |
| unknown | business2 | blend70 | 1 | projection | category | unknown | 0.5478 | no |
| unknown | business2 | blend70 | 1 | publication_assuj | id | unknown | 0.4635 | no |
| unknown | business2 | blend70 | 1 | recipients | quantity | unknown | 0.4842 | no |
| unknown | business2 | blend70 | 1 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown | 0.5281 | no |
| unknown | business2 | blend70 | 1 | returns | quantity | unknown | 0.5435 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9972 | no |
| unknown | business2 | blend70 | 1 | total_verified_sales | quantity | unknown | 0.5545 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9998 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9937 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9962 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9908 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.5449 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9639 | no |
| wrong | business2 | blend70 | 1 | scheme_description | category | text | 0.5063 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6695 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9629 | no |
| wrong | business2 | blend70 | 1 | type of expenditure | account | category | 0.8577 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.8026 | yes |
| critical | business2 | blend70 | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6684 | yes |
| critical | business2 | blend70 | 2 | net current expenditure - max english county councils | amount | quantity | 0.7333 | yes |
| critical | business2 | blend70 | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7124 | yes |
| critical | business2 | blend70 | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7873 | yes |
| critical | business2 | blend70 | 2 | recipients | quantity | id | 0.7003 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7684 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.9753 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.7281 | no |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.7191 | no |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace net sqm | other | quantity | 0.7079 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9397 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.7178 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace net sqm | other | quantity | 0.7069 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.6252 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace gains sqm | other | quantity | 0.7267 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace losses sqm | other | quantity | 0.7029 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace net sqm | other | quantity | 0.6980 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.7505 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace losses sqm | other | quantity | 0.7100 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace net sqm | other | quantity | 0.6952 | no |
| unknown | business2 | blend70 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5546 | no |
| unknown | business2 | blend70 | 2 | # invoices paid within 5 days | quantity | unknown | 0.6027 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4330 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 1.0000 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9635 | no |
| unknown | business2 | blend70 | 2 | habitatcode | id | unknown | 0.4261 | no |
| unknown | business2 | blend70 | 2 | item | category | unknown | 0.4731 | no |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.4816 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9989 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.4350 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4456 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.4117 | no |
| unknown | business2 | blend70 | 2 | publication_assuj | id | unknown | 0.5813 | no |
| unknown | business2 | blend70 | 2 | returns | quantity | unknown | 0.5907 | no |
| unknown | business2 | blend70 | 2 | situtation | address | unknown | 0.4891 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9972 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9999 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9960 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9996 | no |
| unknown | business2 | blend70 | 2 | warddesc | address | unknown | 0.4370 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9900 | no |
| wrong | business2 | blend70 | 2 | amt-units_mnt-unite | category | id | 0.7893 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.6410 | no |
| wrong | business2 | blend70 | 2 | imd19_national_decile | category | id | 0.5360 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.5141 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.5548 | no |
| wrong | business2 | blend70 | 2 | programme | category | account | 0.5994 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.6888 | no |
| wrong | business2 | blend70 | 2 | scheme_description | category | text | 0.7759 | no |
| wrong | business2 | blend70 | 2 | service | account | address | 0.6600 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.8037 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.6332 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9656 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.6506 | no |
| critical | business2 | ft | 1 | # invoices paid within 30 days | quantity | amount | 0.9819 | yes |
| critical | business2 | ft | 1 | # invoices paid within 5 days | quantity | amount | 0.9722 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9816 | yes |
| critical | business2 | ft | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.6889 | yes |
| critical | business2 | ft | 1 | returns | quantity | amount | 0.7704 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9999 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.9195 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.8474 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace net sqm | other | quantity | 0.8380 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9580 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.7750 | no |
| other_ng | business2 | ft | 1 | a2 floorspace net sqm | other | quantity | 0.8985 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9808 | no |
| other_ng | business2 | ft | 1 | b1a floorspace gains sqm | other | quantity | 0.9249 | no |
| other_ng | business2 | ft | 1 | b1a floorspace losses sqm | other | quantity | 0.7916 | no |
| other_ng | business2 | ft | 1 | b1a floorspace net sqm | other | quantity | 0.8495 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.8449 | no |
| other_ng | business2 | ft | 1 | d2 floorspace losses sqm | other | quantity | 0.7865 | no |
| other_ng | business2 | ft | 1 | d2 floorspace net sqm | other | quantity | 0.6901 | no |
| other_ng | business2 | ft | 1 | potential_epc_score | other | quantity | 0.8638 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.7204 | no |
| unknown | business2 | ft | 1 | bike_stands | quantity | unknown | 0.4302 | no |
| unknown | business2 | ft | 1 | conservation_area_site_id | category | unknown | 0.4778 | no |
| unknown | business2 | ft | 1 | daily and seven day rolling totals | category | unknown | 0.6241 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8701 | no |
| unknown | business2 | ft | 1 | monitor | id | unknown | 0.5591 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | net current expenditure - max english county councils | amount | unknown | 0.5517 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.8485 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9595 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.8217 | no |
| unknown | business2 | ft | 1 | projection | category | unknown | 0.7826 | no |
| unknown | business2 | ft | 1 | publication_assuj | id | unknown | 0.6619 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 1 | total membership | quantity | unknown | 0.5259 | no |
| unknown | business2 | ft | 1 | total_verified_sales | quantity | unknown | 0.5587 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9999 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9967 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9952 | no |
| unknown | business2 | ft | 1 | want to live in this parish only | quantity | unknown | 0.4999 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9998 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.5225 | no |
| wrong | business2 | ft | 1 | imd19_national_decile | category | id | 0.6408 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.6708 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9707 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.9557 | no |
| wrong | business2 | ft | 1 | tenure_known | category | quantity | 0.5531 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9931 | no |
| wrong | business2 | ft | 1 | type of expenditure | account | category | 0.9731 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.7285 | yes |
| critical | business2 | ft | 2 | net current expenditure - ave all english county councils | amount | quantity | 0.6577 | yes |
| critical | business2 | ft | 2 | net current expenditure - max english county councils | amount | quantity | 0.8797 | yes |
| critical | business2 | ft | 2 | net current expenditure - min all english county councils | amount | quantity | 0.7282 | yes |
| critical | business2 | ft | 2 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | 0.7377 | yes |
| critical | business2 | ft | 2 | recipients | quantity | id | 0.9428 | yes |
| critical | business2 | ft | 2 | returns | quantity | amount | 0.8379 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8803 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.9667 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.9951 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.9719 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace net sqm | other | quantity | 0.9904 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9930 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.9321 | no |
| other_ng | business2 | ft | 2 | a2 floorspace net sqm | other | quantity | 0.9823 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.5256 | no |
| other_ng | business2 | ft | 2 | avg_tilt | other | amount | 0.6790 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.9948 | no |
| other_ng | business2 | ft | 2 | b1a floorspace losses sqm | other | quantity | 0.9567 | no |
| other_ng | business2 | ft | 2 | b1a floorspace net sqm | other | quantity | 0.9901 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.9940 | no |
| other_ng | business2 | ft | 2 | d2 floorspace losses sqm | other | quantity | 0.9580 | no |
| other_ng | business2 | ft | 2 | d2 floorspace net sqm | other | quantity | 0.9914 | no |
| unknown | business2 | ft | 2 | conservation_area_site_id | category | unknown | 0.4893 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9758 | no |
| unknown | business2 | ft | 2 | habitatcode | id | unknown | 0.5968 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.5761 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.6195 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9988 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.6366 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.5882 | no |
| unknown | business2 | ft | 2 | publication_assuj | id | unknown | 0.8303 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9999 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9999 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9999 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9999 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 1.0000 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9988 | no |
| wrong | business2 | ft | 2 | amt-units_mnt-unite | category | id | 0.9999 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.8754 | no |
| wrong | business2 | ft | 2 | imd19_national_decile | category | id | 0.7628 | no |
| wrong | business2 | ft | 2 | item | category | text | 0.6575 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.5633 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.5182 | no |
| wrong | business2 | ft | 2 | potential_epc_rating_known | category | quantity | 0.5369 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.5489 | no |
| wrong | business2 | ft | 2 | programme | category | account | 0.8560 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.5777 | no |
| wrong | business2 | ft | 2 | scheme_description | category | text | 0.6824 | no |
| wrong | business2 | ft | 2 | service | account | address | 0.9421 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.8506 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.5867 | no |
| wrong | business2 | ft | 2 | tenure_known | category | quantity | 0.5814 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9971 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.6771 | no |
| wrong | business2 | ft | 2 | warddesc | address | category | 0.5365 | no |
| critical | dev220 | blend50 | 1 | purchase order by customer | id | quantity | 0.8539 | yes |
| unknown | dev220 | blend50 | 1 | receive_order_import_type_id | category | unknown | 0.4936 | no |
| unknown | dev220 | blend50 | 1 | 履行場所 | address | unknown | 0.4692 | no |
| wrong | dev220 | blend50 | 1 | customer rank | quantity | category | 0.8612 | no |
| wrong | dev220 | blend50 | 1 | is a company | category | org | 0.6306 | no |
| wrong | dev220 | blend50 | 1 | supplier rank | quantity | category | 0.5689 | no |
| wrong | dev220 | blend50 | 1 | taxable | category | tax_class | 0.5654 | no |
| wrong | dev220 | blend50 | 1 | terms | category | text | 0.8739 | no |
| unknown | dev220 | blend50 | 2 | purchase order by customer | id | unknown | 0.5171 | no |
| unknown | dev220 | blend50 | 2 | receive_order_import_type_id | category | unknown | 0.4829 | no |
| unknown | dev220 | blend50 | 2 | taxable | category | unknown | 0.4955 | no |
| unknown | dev220 | blend50 | 2 | 履行場所 | address | unknown | 0.4876 | no |
| wrong | dev220 | blend50 | 2 | customer rank | quantity | category | 0.9023 | no |
| wrong | dev220 | blend50 | 2 | supplier rank | quantity | category | 0.5937 | no |
| wrong | dev220 | blend50 | 2 | terms | category | text | 0.8529 | no |
| wrong | dev220 | blend50 | 2 | 商品オプション | text | category | 0.5635 | no |
| critical | dev220 | blend60 | 1 | purchase order by customer | id | quantity | 0.8650 | yes |
| unknown | dev220 | blend60 | 1 | payment terms | category | unknown | 0.4524 | no |
| wrong | dev220 | blend60 | 1 | customer rank | quantity | category | 0.8607 | no |
| wrong | dev220 | blend60 | 1 | is a company | category | org | 0.6134 | no |
| wrong | dev220 | blend60 | 1 | supplier rank | quantity | category | 0.6435 | no |
| wrong | dev220 | blend60 | 1 | terms | category | text | 0.8980 | no |
| wrong | dev220 | blend60 | 2 | customer rank | quantity | category | 0.9100 | no |
| wrong | dev220 | blend60 | 2 | supplier rank | quantity | category | 0.6733 | no |
| wrong | dev220 | blend60 | 2 | terms | category | text | 0.8728 | no |
| wrong | dev220 | blend60 | 2 | 商品オプション | text | category | 0.5905 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.8761 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8602 | no |
| wrong | dev220 | blend70 | 1 | is a company | category | org | 0.5962 | no |
| wrong | dev220 | blend70 | 1 | payment terms | category | text | 0.5268 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7182 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.9221 | no |
| unknown | dev220 | blend70 | 2 | 商品オプション | text | unknown | 0.4976 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.9177 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7529 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.8927 | no |
| wrong | dev220 | blend70 | 2 | 商品オプション | text | category | 0.6174 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9093 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8586 | no |
| wrong | dev220 | ft | 1 | is a company | category | org | 0.5446 | no |
| wrong | dev220 | ft | 1 | payment terms | category | text | 0.7508 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9421 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.9943 | no |
| unknown | dev220 | ft | 2 | 年末調整未済 | category | unknown | 0.3930 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9408 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9918 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.9523 | no |
| wrong | dev220 | ft | 2 | 商品オプション | text | category | 0.6984 | no |
| wrong | dev220 | ft | 2 | 商品オプション | text | category | 0.6638 | no |
| other_ng | general | blend50 | 1 | dag-stage | other | category | 0.8477 | no |
| other_ng | general | blend50 | 1 | mt2 | other | quantity | 0.8265 | no |
| other_ng | general | blend50 | 1 | nodes | other | text | 0.5512 | no |
| other_ng | general | blend50 | 1 | value | other | rate | 0.6233 | no |
| other_ng | general | blend50 | 1 | 五島 | other | quantity | 0.9939 | no |
| unknown | general | blend50 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.5092 | no |
| unknown | general | blend50 | 1 | age_q1_nd | quantity | unknown | 0.7821 | no |
| unknown | general | blend50 | 1 | age_q3 | quantity | unknown | 0.6905 | no |
| unknown | general | blend50 | 1 | age_q3_nd | quantity | unknown | 0.8624 | no |
| unknown | general | blend50 | 1 | app | category | unknown | 0.4610 | no |
| unknown | general | blend50 | 1 | authors | person | unknown | 0.4689 | no |
| unknown | general | blend50 | 1 | denominatorunweighted | quantity | unknown | 0.7657 | no |
| unknown | general | blend50 | 1 | denominatorweighted | quantity | unknown | 0.9167 | no |
| unknown | general | blend50 | 1 | element_char | category | unknown | 0.4652 | no |
| unknown | general | blend50 | 1 | female_frequency | rate | unknown | 0.7472 | no |
| unknown | general | blend50 | 1 | goal | id | unknown | 0.4951 | no |
| unknown | general | blend50 | 1 | image_level_adj_acc | rate | unknown | 0.5177 | no |
| unknown | general | blend50 | 1 | itemfield14 | date | unknown | 0.4585 | no |
| unknown | general | blend50 | 1 | keywords | text | unknown | 0.4879 | no |
| unknown | general | blend50 | 1 | n_occurences | quantity | unknown | 0.4645 | no |
| unknown | general | blend50 | 1 | pir_sha | id | unknown | 0.4854 | no |
| unknown | general | blend50 | 1 | place | org | unknown | 0.4838 | no |
| unknown | general | blend50 | 1 | property | category | unknown | 0.4583 | no |
| unknown | general | blend50 | 1 | source_value | category | unknown | 0.4669 | no |
| unknown | general | blend50 | 1 | 住家一部損壊 | quantity | unknown | 0.4975 | no |
| unknown | general | blend50 | 1 | 住家全壊 | quantity | unknown | 0.4932 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4296 | no |
| unknown | general | blend50 | 1 | 天候 | category | unknown | 0.4487 | no |
| unknown | general | blend50 | 1 | 発生日 | date | unknown | 0.9437 | no |
| unknown | general | blend50 | 1 | 発生県 | id | unknown | 0.4690 | no |
| unknown | general | blend50 | 1 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend50 | 1 | 科名 | category | unknown | 0.8874 | no |
| wrong | general | blend50 | 1 | author | person | org | 0.6868 | no |
| wrong | general | blend50 | 1 | cleaned | text | category | 0.5149 | no |
| wrong | general | blend50 | 1 | keyword | category | text | 0.9219 | no |
| wrong | general | blend50 | 1 | raw | category | text | 0.8782 | no |
| wrong | general | blend50 | 1 | year_step_size | quantity | category | 0.7557 | no |
| wrong | general | blend50 | 1 | 読み方 | address | text | 0.5939 | no |
| other_ng | general | blend50 | 2 | dag-stage | other | category | 0.8379 | no |
| other_ng | general | blend50 | 2 | mt2 | other | quantity | 0.8831 | no |
| other_ng | general | blend50 | 2 | nodes | other | category | 0.5837 | no |
| other_ng | general | blend50 | 2 | value | other | rate | 0.8943 | no |
| other_ng | general | blend50 | 2 | 五島 | other | quantity | 0.7532 | no |
| unknown | general | blend50 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8246 | no |
| unknown | general | blend50 | 2 | age_q1_nd | quantity | unknown | 0.7502 | no |
| unknown | general | blend50 | 2 | age_q3 | quantity | unknown | 0.4638 | no |
| unknown | general | blend50 | 2 | age_q3_nd | quantity | unknown | 0.9196 | no |
| unknown | general | blend50 | 2 | app | category | unknown | 0.4836 | no |
| unknown | general | blend50 | 2 | bib | id | unknown | 0.4391 | no |
| unknown | general | blend50 | 2 | denominatorunweighted | quantity | unknown | 0.7662 | no |
| unknown | general | blend50 | 2 | denominatorweighted | quantity | unknown | 0.9171 | no |
| unknown | general | blend50 | 2 | female_frequency | rate | unknown | 0.9474 | no |
| unknown | general | blend50 | 2 | goal | id | unknown | 0.4893 | no |
| unknown | general | blend50 | 2 | image_level_adj_acc | rate | unknown | 0.9014 | no |
| unknown | general | blend50 | 2 | itemfield14 | date | unknown | 0.4798 | no |
| unknown | general | blend50 | 2 | pir_sha | id | unknown | 0.5138 | no |
| unknown | general | blend50 | 2 | place | org | unknown | 0.3939 | no |
| unknown | general | blend50 | 2 | property | category | unknown | 0.4204 | no |
| unknown | general | blend50 | 2 | sens_final | rate | unknown | 0.5600 | no |
| unknown | general | blend50 | 2 | source_value | category | unknown | 0.4975 | no |
| unknown | general | blend50 | 2 | study | text | unknown | 0.3210 | no |
| unknown | general | blend50 | 2 | 住家全壊 | quantity | unknown | 0.4853 | no |
| unknown | general | blend50 | 2 | 日本語教室名 | org | unknown | 0.4937 | no |
| unknown | general | blend50 | 2 | 東第5 | quantity | unknown | 0.5258 | no |
| unknown | general | blend50 | 2 | 次に掲げるもの | category | unknown | 0.3463 | no |
| unknown | general | blend50 | 2 | 発生日 | date | unknown | 0.9420 | no |
| unknown | general | blend50 | 2 | 発生県 | id | unknown | 0.4921 | no |
| unknown | general | blend50 | 2 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend50 | 2 | 科名 | category | unknown | 0.9470 | no |
| wrong | general | blend50 | 2 | cleaned | text | category | 0.5022 | no |
| wrong | general | blend50 | 2 | keyword | category | text | 0.9219 | no |
| wrong | general | blend50 | 2 | raw | category | text | 0.5732 | no |
| wrong | general | blend50 | 2 | year_step_size | quantity | category | 0.8854 | no |
| wrong | general | blend50 | 2 | 天候 | category | text | 0.5007 | no |
| wrong | general | blend50 | 2 | 天候 | category | text | 0.5497 | no |
| wrong | general | blend50 | 2 | 読み方 | address | text | 0.7363 | no |
| critical | general | blend60 | 1 | goal | id | quantity | 0.5860 | yes |
| other_ng | general | blend60 | 1 | dag-stage | other | category | 0.8498 | no |
| other_ng | general | blend60 | 1 | episode | other | quantity | 0.5520 | no |
| other_ng | general | blend60 | 1 | mt2 | other | quantity | 0.8033 | no |
| other_ng | general | blend60 | 1 | nodes | other | text | 0.5032 | no |
| other_ng | general | blend60 | 1 | 五島 | other | quantity | 0.9936 | no |
| unknown | general | blend60 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.4811 | no |
| unknown | general | blend60 | 1 | age_q1_nd | quantity | unknown | 0.7883 | no |
| unknown | general | blend60 | 1 | age_q3 | quantity | unknown | 0.6640 | no |
| unknown | general | blend60 | 1 | age_q3_nd | quantity | unknown | 0.8632 | no |
| unknown | general | blend60 | 1 | app | category | unknown | 0.5434 | no |
| unknown | general | blend60 | 1 | authors | person | unknown | 0.4694 | no |
| unknown | general | blend60 | 1 | cleaned | text | unknown | 0.4254 | no |
| unknown | general | blend60 | 1 | denominatorunweighted | quantity | unknown | 0.8122 | no |
| unknown | general | blend60 | 1 | denominatorweighted | quantity | unknown | 0.9331 | no |
| unknown | general | blend60 | 1 | element_char | category | unknown | 0.4185 | no |
| unknown | general | blend60 | 1 | female_frequency | rate | unknown | 0.7174 | no |
| unknown | general | blend60 | 1 | itemfield14 | date | unknown | 0.4425 | no |
| unknown | general | blend60 | 1 | keywords | text | unknown | 0.4041 | no |
| unknown | general | blend60 | 1 | n_occurences | quantity | unknown | 0.4924 | no |
| unknown | general | blend60 | 1 | pir_sha | id | unknown | 0.5745 | no |
| unknown | general | blend60 | 1 | property | category | unknown | 0.4945 | no |
| unknown | general | blend60 | 1 | source_value | category | unknown | 0.4423 | no |
| unknown | general | blend60 | 1 | 住家全壊 | quantity | unknown | 0.4866 | no |
| unknown | general | blend60 | 1 | 発生日 | date | unknown | 0.9549 | no |
| unknown | general | blend60 | 1 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend60 | 1 | 科名 | category | unknown | 0.8803 | no |
| wrong | general | blend60 | 1 | attrition | category | quantity | 0.5785 | no |
| wrong | general | blend60 | 1 | author | person | org | 0.6816 | no |
| wrong | general | blend60 | 1 | keyword | category | text | 0.9368 | no |
| wrong | general | blend60 | 1 | place | org | address | 0.5493 | no |
| wrong | general | blend60 | 1 | raw | category | text | 0.8639 | no |
| wrong | general | blend60 | 1 | year_step_size | quantity | category | 0.7185 | no |
| wrong | general | blend60 | 1 | データセット_キーワード | category | text | 0.5342 | no |
| wrong | general | blend60 | 1 | 発生県 | id | address | 0.5547 | no |
| wrong | general | blend60 | 1 | 読み方 | address | text | 0.6122 | no |
| critical | general | blend60 | 2 | goal | id | quantity | 0.5773 | yes |
| other_ng | general | blend60 | 2 | dag-stage | other | category | 0.8380 | no |
| other_ng | general | blend60 | 2 | mt2 | other | quantity | 0.8711 | no |
| other_ng | general | blend60 | 2 | nodes | other | category | 0.6648 | no |
| other_ng | general | blend60 | 2 | operationid | other | id | 0.5860 | no |
| other_ng | general | blend60 | 2 | value | other | rate | 0.9067 | no |
| other_ng | general | blend60 | 2 | 五島 | other | quantity | 0.7048 | no |
| unknown | general | blend60 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8595 | no |
| unknown | general | blend60 | 2 | age_q1_nd | quantity | unknown | 0.7501 | no |
| unknown | general | blend60 | 2 | age_q3 | quantity | unknown | 0.3919 | no |
| unknown | general | blend60 | 2 | age_q3_nd | quantity | unknown | 0.9318 | no |
| unknown | general | blend60 | 2 | app | category | unknown | 0.4241 | no |
| unknown | general | blend60 | 2 | bib | id | unknown | 0.4833 | no |
| unknown | general | blend60 | 2 | denominatorunweighted | quantity | unknown | 0.8129 | no |
| unknown | general | blend60 | 2 | denominatorweighted | quantity | unknown | 0.9336 | no |
| unknown | general | blend60 | 2 | female_frequency | rate | unknown | 0.9577 | no |
| unknown | general | blend60 | 2 | image_level_adj_acc | rate | unknown | 0.8887 | no |
| unknown | general | blend60 | 2 | itemfield14 | date | unknown | 0.4873 | no |
| unknown | general | blend60 | 2 | pir_sha | id | unknown | 0.6086 | no |
| unknown | general | blend60 | 2 | place | org | unknown | 0.4414 | no |
| unknown | general | blend60 | 2 | property | category | unknown | 0.4921 | no |
| unknown | general | blend60 | 2 | raw | category | unknown | 0.4979 | no |
| unknown | general | blend60 | 2 | sens_final | rate | unknown | 0.6388 | no |
| unknown | general | blend60 | 2 | source_value | category | unknown | 0.5970 | no |
| unknown | general | blend60 | 2 | study | text | unknown | 0.3658 | no |
| unknown | general | blend60 | 2 | 住家全壊 | quantity | unknown | 0.4219 | no |
| unknown | general | blend60 | 2 | 東第5 | quantity | unknown | 0.5656 | no |
| unknown | general | blend60 | 2 | 次に掲げるもの | category | unknown | 0.3869 | no |
| unknown | general | blend60 | 2 | 発生日 | date | unknown | 0.9529 | no |
| unknown | general | blend60 | 2 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend60 | 2 | 科名 | category | unknown | 0.9518 | no |
| wrong | general | blend60 | 2 | keyword | category | text | 0.9368 | no |
| wrong | general | blend60 | 2 | year_step_size | quantity | category | 0.8741 | no |
| wrong | general | blend60 | 2 | 天候 | category | text | 0.5121 | no |
| wrong | general | blend60 | 2 | 天候 | category | text | 0.5787 | no |
| wrong | general | blend60 | 2 | 発生県 | id | address | 0.5825 | no |
| wrong | general | blend60 | 2 | 読み方 | address | text | 0.7831 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.6768 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.8519 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.6420 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.7801 | no |
| other_ng | general | blend70 | 1 | nodes | other | category | 0.5325 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9933 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.4530 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.7946 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.6375 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.8640 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.6259 | no |
| unknown | general | blend70 | 1 | cleaned | text | unknown | 0.4512 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8588 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9496 | no |
| unknown | general | blend70 | 1 | element_char | category | unknown | 0.4833 | no |
| unknown | general | blend70 | 1 | female_frequency | rate | unknown | 0.6877 | no |
| unknown | general | blend70 | 1 | itemfield14 | date | unknown | 0.4380 | no |
| unknown | general | blend70 | 1 | keywords | text | unknown | 0.3203 | no |
| unknown | general | blend70 | 1 | n_occurences | quantity | unknown | 0.5203 | no |
| unknown | general | blend70 | 1 | pir_sha | id | unknown | 0.6636 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9662 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.8732 | no |
| wrong | general | blend70 | 1 | attrition | category | quantity | 0.6736 | no |
| wrong | general | blend70 | 1 | author | person | org | 0.6764 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9517 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.6148 | no |
| wrong | general | blend70 | 1 | raw | category | text | 0.8496 | no |
| wrong | general | blend70 | 1 | source_value | category | text | 0.5146 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.6813 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.6203 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.6405 | no |
| wrong | general | blend70 | 1 | 読み方 | address | text | 0.6304 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.6667 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.8381 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.8592 | no |
| other_ng | general | blend70 | 2 | nodes | other | category | 0.7459 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6813 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9192 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.6563 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8944 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.7499 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.3200 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.9440 | no |
| unknown | general | blend70 | 2 | app | category | unknown | 0.4175 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8595 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9501 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.9680 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.8761 | no |
| unknown | general | blend70 | 2 | itemfield14 | date | unknown | 0.4947 | no |
| unknown | general | blend70 | 2 | mechanism | category | unknown | 0.4880 | no |
| unknown | general | blend70 | 2 | pir_sha | id | unknown | 0.7034 | no |
| unknown | general | blend70 | 2 | place | org | unknown | 0.4890 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7176 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6965 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.4105 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.4911 | no |
| unknown | general | blend70 | 2 | 東第5 | quantity | unknown | 0.6597 | no |
| unknown | general | blend70 | 2 | 次に掲げるもの | category | unknown | 0.4275 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9638 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9566 | no |
| wrong | general | blend70 | 2 | attrition | category | quantity | 0.5573 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9518 | no |
| wrong | general | blend70 | 2 | property | category | text | 0.5638 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.8629 | no |
| wrong | general | blend70 | 2 | 天候 | category | text | 0.5234 | no |
| wrong | general | blend70 | 2 | 天候 | category | text | 0.6078 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.6729 | no |
| wrong | general | blend70 | 2 | 読み方 | address | text | 0.8298 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.9494 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8582 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.9120 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.7104 | no |
| other_ng | general | ft | 1 | nodes | other | category | 0.6843 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.6174 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9923 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.4554 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.8134 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.5579 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.8662 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.8731 | no |
| unknown | general | ft | 1 | cluster | category | unknown | 0.4559 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9985 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9989 | no |
| unknown | general | ft | 1 | female_frequency | rate | unknown | 0.5985 | no |
| unknown | general | ft | 1 | itemfield14 | date | unknown | 0.4360 | no |
| unknown | general | ft | 1 | keywords | text | unknown | 0.4431 | no |
| unknown | general | ft | 1 | n_occurences | quantity | unknown | 0.6041 | no |
| unknown | general | ft | 1 | pir_sha | id | unknown | 0.9309 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9998 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.8519 | no |
| wrong | general | ft | 1 | attrition | category | quantity | 0.9589 | no |
| wrong | general | ft | 1 | author | person | org | 0.6608 | no |
| wrong | general | ft | 1 | element_char | category | address | 0.6777 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9965 | no |
| wrong | general | ft | 1 | place | org | address | 0.8113 | no |
| wrong | general | ft | 1 | raw | category | text | 0.8068 | no |
| wrong | general | ft | 1 | source_value | category | text | 0.7316 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.5697 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.8785 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.8977 | no |
| wrong | general | ft | 1 | 読み方 | address | text | 0.6852 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.9349 | yes |
| critical | general | ft | 2 | itemfield14 | date | id | 0.5170 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.8385 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.8234 | no |
| other_ng | general | ft | 2 | nodes | other | category | 0.9892 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9669 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9564 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.5110 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9992 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.7496 | no |
| unknown | general | ft | 2 | age_q3 | quantity | unknown | 0.4156 | no |
| unknown | general | ft | 2 | age_q3_nd | quantity | unknown | 0.9806 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.5755 | no |
| unknown | general | ft | 2 | count | quantity | unknown | 0.5910 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9995 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9997 | no |
| unknown | general | ft | 2 | female_frequency | rate | unknown | 0.9990 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.8382 | no |
| unknown | general | ft | 2 | keywords | text | unknown | 0.4319 | no |
| unknown | general | ft | 2 | pir_sha | id | unknown | 0.9878 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9539 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9949 | no |
| unknown | general | ft | 2 | 東第5 | quantity | unknown | 0.9423 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9964 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 1.0000 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9711 | no |
| wrong | general | ft | 2 | attrition | category | quantity | 0.7928 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9966 | no |
| wrong | general | ft | 2 | mechanism | category | id | 0.6229 | no |
| wrong | general | ft | 2 | place | org | address | 0.6315 | no |
| wrong | general | ft | 2 | property | category | text | 0.7790 | no |
| wrong | general | ft | 2 | study | text | id | 0.5448 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.8291 | no |
| wrong | general | ft | 2 | データセット_キーワード | category | text | 0.6180 | no |
| wrong | general | ft | 2 | 天候 | category | text | 0.5575 | no |
| wrong | general | ft | 2 | 天候 | category | text | 0.6951 | no |
| wrong | general | ft | 2 | 次に掲げるもの | category | text | 0.5494 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9440 | no |
| wrong | general | ft | 2 | 読み方 | address | text | 0.9700 | no |
| unknown | japan_procurement | blend50 | 1 | 入札時期 (予定) | date | unknown | 0.9960 | no |
| unknown | japan_procurement | blend50 | 2 | 入札時期 (予定) | date | unknown | 0.9960 | no |
| unknown | japan_procurement | blend60 | 1 | 入札時期 (予定) | date | unknown | 0.9968 | no |
| unknown | japan_procurement | blend60 | 2 | 入札時期 (予定) | date | unknown | 0.9968 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9976 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9976 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 1.0000 | no |
| wrong | japan_procurement | ft | 1 | 50,000,000円以上150,000,000円未満件数 | quantity | category | 0.5358 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 1.0000 | no |
| wrong | japan_procurement | ft | 2 | 50,000,000円以上150,000,000円未満件数 | quantity | category | 0.7009 | no |

### unknown の判定理由

- date_value_evidence_low: 115件
- numeric_top2_too_close: 68件
- numeric_values_not_parseable: 34件
- other_class: 132件
- probability_below_threshold: 243件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 106件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 289件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 201件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
