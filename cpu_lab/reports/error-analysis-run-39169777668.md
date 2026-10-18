# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-18T21:55:16+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 24 | 2 | 14 | 0 |
| business | blend70 | 2 | 490 | 29 | 6 | 11 | 0 |
| business | ft | 1 | 490 | 24 | 2 | 12 | 0 |
| business | ft | 2 | 490 | 29 | 5 | 10 | 0 |
| business2 | blend70 | 1 | 976 | 26 | 4 | 18 | 7 |
| business2 | blend70 | 2 | 976 | 21 | 3 | 21 | 6 |
| business2 | ft | 1 | 976 | 28 | 4 | 15 | 7 |
| business2 | ft | 2 | 976 | 24 | 3 | 17 | 7 |
| dev220 | blend70 | 1 | 220 | 8 | 1 | 1 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 8 | 2 | 1 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 0 | 0 |
| general | blend70 | 1 | 383 | 7 | 1 | 15 | 5 |
| general | blend70 | 2 | 383 | 5 | 1 | 20 | 5 |
| general | ft | 1 | 383 | 8 | 1 | 14 | 4 |
| general | ft | 2 | 383 | 7 | 2 | 18 | 6 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 20, org→account: 6, category→account: 4, amount→quantity: 4, quantity→amount: 2, text→category: 2, account→text: 2, category→text: 2
- business / ft: category→quantity: 20, org→account: 7, amount→quantity: 5, category→account: 4, quantity→amount: 2, text→category: 2, account→text: 2, org→category: 2
- business2 / blend70: amount→quantity: 5, id→category: 4, category→id: 4, quantity→address: 4, category→quantity: 4, account→org: 3, account→category: 3, org→address: 3
- business2 / ft: category→id: 5, amount→quantity: 5, category→quantity: 5, id→category: 4, quantity→address: 4, org→address: 4, account→org: 3, account→category: 3
- dev220 / blend70: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, rate→tax_class: 1, org→address: 1, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, rate→tax_class: 1, org→address: 1, amount→rate: 1, address→id: 1, category→tax_class: 1
- general / blend70: category→text: 2, text→category: 2, id→address: 2, id→quantity: 2, org→address: 1, quantity→category: 1, text→account: 1, text→org: 1
- general / ft: text→category: 3, category→text: 2, id→address: 2, id→quantity: 2, org→address: 1, org→person: 1, quantity→category: 1, text→account: 1

### seedをまたいで再発した誤り

- business / blend70: `capital revenue`、category→account（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `capital revenue`、category→account（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `mois calendrier`、date→category（seed 1, seed 2）
- business / ft: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `account name`、account→org（seed 1, seed 2）
- business2 / blend70: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `account name`、account→org（seed 1, seed 2）
- business2 / ft: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend70: `goal`、id→quantity（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend70 | 1 | australian sourced services | amount | id | 0.5065 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9979 | yes |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4913 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.3217 | no |
| unknown | business | blend70 | 1 | d2 | category | unknown | 0.4027 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.4279 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9678 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.2433 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.3907 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.4839 | no |
| unknown | business | blend70 | 1 | publisher label | org | unknown | 0.3913 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9974 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9928 | no |
| unknown | business | blend70 | 1 | segment-title_fr | category | unknown | 0.4384 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9928 | no |
| wrong | business | blend70 | 1 | capital revenue | category | account | 0.7487 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.7008 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7451 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9948 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8795 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9967 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8540 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.9285 | no |
| wrong | business | blend70 | 1 | mois calendrier | date | category | 0.5245 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | category | 0.5336 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7067 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.7018 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.7038 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.7019 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6963 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7094 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7241 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7201 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7365 | no |
| wrong | business | blend70 | 1 | segment-title_en | category | text | 0.5260 | no |
| wrong | business | blend70 | 1 | sub_category | category | account | 0.5219 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.6761 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6984 | yes |
| critical | business | blend70 | 2 | australian sourced services | amount | quantity | 0.6817 | yes |
| critical | business | blend70 | 2 | mois calendrier | date | quantity | 0.5136 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6988 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.7057 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9971 | yes |
| unknown | business | blend70 | 2 | # invoices paid within 30 days | quantity | unknown | 0.6010 | no |
| unknown | business | blend70 | 2 | d1 | category | unknown | 0.4257 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.3481 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9670 | no |
| unknown | business | blend70 | 2 | ligne | category | unknown | 0.2619 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9975 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9917 | no |
| unknown | business | blend70 | 2 | tournée | id | unknown | 0.5736 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9872 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9405 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.7010 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.7751 | no |
| wrong | business | blend70 | 2 | commodity-title_en | product | category | 0.7316 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7195 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9951 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8866 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9966 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8546 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.7685 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9286 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | address | 0.6983 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7164 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9779 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.7059 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.7043 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.7035 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6706 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.6982 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.7057 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7169 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7197 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | tax_class | 0.6099 | no |
| wrong | business | blend70 | 2 | title | category | text | 0.9448 | no |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.5581 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9990 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.7017 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.3409 | no |
| unknown | business | ft | 1 | commodity-title_en | product | unknown | 0.4055 | no |
| unknown | business | ft | 1 | d2 | category | unknown | 0.5752 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9992 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9979 | no |
| unknown | business | ft | 1 | ligne | category | unknown | 0.3099 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9993 | no |
| unknown | business | ft | 1 | segment-title_en | category | unknown | 0.4400 | no |
| unknown | business | ft | 1 | segment-title_fr | category | unknown | 0.3893 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9984 | no |
| wrong | business | ft | 1 | capital revenue | category | account | 0.9561 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9959 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9907 | no |
| wrong | business | ft | 1 | department | org | account | 0.9983 | no |
| wrong | business | ft | 1 | department | org | account | 0.9879 | no |
| wrong | business | ft | 1 | department | org | account | 0.9989 | no |
| wrong | business | ft | 1 | description | account | text | 0.9958 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.6094 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9990 | no |
| wrong | business | ft | 1 | mois calendrier | date | category | 0.7310 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | category | 0.7597 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9986 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9942 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.9975 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9978 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9862 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9983 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9987 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9971 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9795 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.6071 | no |
| wrong | business | ft | 1 | title | category | account | 0.9457 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9977 | yes |
| critical | business | ft | 2 | australian sourced services | amount | quantity | 0.9738 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.9982 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.9981 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.9978 | yes |
| unknown | business | ft | 2 | d1 | category | unknown | 0.5435 | no |
| unknown | business | ft | 2 | d2 | category | unknown | 0.4532 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9992 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9967 | no |
| unknown | business | ft | 2 | ligne | category | unknown | 0.3679 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9992 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9978 | no |
| unknown | business | ft | 2 | tournée | id | unknown | 0.5617 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9905 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9798 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.9650 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.9938 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.9572 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9542 | no |
| wrong | business | ft | 2 | department | org | account | 0.9987 | no |
| wrong | business | ft | 2 | department | org | account | 0.9979 | no |
| wrong | business | ft | 2 | department | org | account | 0.9987 | no |
| wrong | business | ft | 2 | description | account | text | 0.9966 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.9971 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9992 | no |
| wrong | business | ft | 2 | mois calendrier | date | category | 0.5788 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | address | 0.9967 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9963 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9904 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9974 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9977 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9970 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9531 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9890 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9929 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9883 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9965 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | tax_class | 0.8713 | no |
| wrong | business | ft | 2 | title | category | text | 0.9861 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7293 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8511 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9979 | yes |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.6115 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.6028 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.9359 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.7417 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9161 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.7385 | no |
| other_ng | business2 | blend70 | 1 | total_floor_area | other | quantity | 0.6681 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6142 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9709 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.6338 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 1 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5283 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4301 | no |
| unknown | business2 | blend70 | 1 | surveyname | text | unknown | 0.4658 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9952 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9898 | no |
| wrong | business2 | blend70 | 1 | account name | account | org | 0.5344 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8894 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.6916 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.8548 | no |
| wrong | business2 | blend70 | 1 | epc_score_known | category | quantity | 0.7239 | no |
| wrong | business2 | blend70 | 1 | health service executive area | address | org | 0.7645 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6978 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6920 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6896 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.9002 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6276 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6781 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7606 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7398 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9791 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.6191 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.9061 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6133 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6719 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6799 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.7262 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9669 | no |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9920 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8515 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.9966 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.6307 | no |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.6429 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9392 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.7549 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.9527 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.6677 | no |
| unknown | business2 | blend70 | 2 | # invoices paid within 30 days | quantity | unknown | 0.5628 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4477 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.2894 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9631 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6983 | no |
| unknown | business2 | blend70 | 2 | numbers of | date | unknown | 0.3663 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 2 | scheme_description | category | unknown | 0.4891 | no |
| unknown | business2 | blend70 | 2 | service | account | unknown | 0.4585 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 2 | total_floor_area_known | category | unknown | 0.3964 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9951 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9904 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6608 | no |
| wrong | business2 | blend70 | 2 | body name | org | address | 0.6633 | no |
| wrong | business2 | blend70 | 2 | fine | amount | category | 0.7773 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6925 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6913 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.6852 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7754 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8991 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.5778 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7597 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7391 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9756 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.8024 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8971 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8267 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5161 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.5938 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9671 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9980 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9993 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9984 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9991 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.8286 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.8057 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9875 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.9663 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9412 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.9769 | no |
| other_ng | business2 | ft | 1 | total_floor_area | other | quantity | 0.8629 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.8540 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9865 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.8932 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9987 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9988 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9985 | no |
| wrong | business2 | ft | 1 | account name | account | org | 0.7631 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9953 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.9661 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.8726 | no |
| wrong | business2 | ft | 1 | epc_score_known | category | quantity | 0.9938 | no |
| wrong | business2 | ft | 1 | health service executive area | address | org | 0.8116 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9969 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9885 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.8604 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.9957 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.8872 | no |
| wrong | business2 | ft | 1 | potential_epc_score_known | category | quantity | 0.6297 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9684 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9991 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9992 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9924 | no |
| wrong | business2 | ft | 1 | scheme_description | category | account | 0.6130 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.8827 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9969 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8549 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9593 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9710 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.9843 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9990 | no |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9992 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9990 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.9972 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.8560 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.8631 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9922 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.9851 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9935 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.6398 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.8758 | no |
| unknown | business2 | ft | 2 | construction_age_band | category | unknown | 0.3915 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9753 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9854 | no |
| unknown | business2 | ft | 2 | numbers of | date | unknown | 0.5214 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.5380 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9986 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9986 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9993 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9437 | no |
| wrong | business2 | ft | 2 | amt-units_mnt-unite | category | id | 0.5119 | no |
| wrong | business2 | ft | 2 | body name | org | address | 0.5240 | no |
| wrong | business2 | ft | 2 | body name | org | address | 0.8708 | no |
| wrong | business2 | ft | 2 | fine | amount | category | 0.9327 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.9893 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9875 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.9299 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9830 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9940 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.8161 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9979 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9981 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9874 | no |
| wrong | business2 | ft | 2 | service | account | address | 0.6543 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.8658 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9637 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.8489 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.7367 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8481 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9992 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9384 | yes |
| unknown | dev220 | blend70 | 1 | rate | amount | unknown | 0.5074 | no |
| wrong | dev220 | blend70 | 1 | city | address | id | 0.9026 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9356 | no |
| wrong | dev220 | blend70 | 1 | location | org | address | 0.6054 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7553 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.6341 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7120 | no |
| wrong | dev220 | blend70 | 1 | 税率 | rate | tax_class | 0.5546 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9379 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8970 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7539 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.7673 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.5829 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9985 | yes |
| critical | dev220 | ft | 1 | rate | amount | rate | 0.6932 | yes |
| unknown | dev220 | ft | 1 | taxable | category | unknown | 0.4970 | no |
| wrong | dev220 | ft | 1 | city | address | id | 0.9981 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9664 | no |
| wrong | dev220 | ft | 1 | location | org | address | 0.8647 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9950 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9733 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.7818 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9977 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.9112 | no |
| wrong | dev220 | ft | 2 | division | category | account | 0.6678 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9931 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.6739 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.7890 | no |
| critical | general | blend70 | 1 | goal | id | quantity | 0.7109 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.7272 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.7007 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.6104 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.8927 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9964 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8940 | no |
| unknown | general | blend70 | 1 | app | category | unknown | 0.6763 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8590 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9497 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9870 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.6460 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.4365 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.7392 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.3686 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3481 | no |
| unknown | general | blend70 | 1 | 受入年齢 | category | unknown | 0.5009 | no |
| unknown | general | blend70 | 1 | 東第5 | quantity | unknown | 0.5369 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9655 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9995 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.4643 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.5075 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9501 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7415 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6992 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.8620 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7104 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.6784 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9479 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6219 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9620 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.7015 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9954 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8869 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.5096 | no |
| unknown | general | blend70 | 2 | app | category | unknown | 0.6136 | no |
| unknown | general | blend70 | 2 | author | person | unknown | 0.5235 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8562 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9495 | no |
| unknown | general | blend70 | 2 | doi | id | unknown | 0.7050 | no |
| unknown | general | blend70 | 2 | female_frequency | rate | unknown | 0.9051 | no |
| unknown | general | blend70 | 2 | funding | amount | unknown | 0.5304 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9886 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.7127 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7482 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6384 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.7056 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.5362 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3264 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9652 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9995 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9592 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.4222 | no |
| wrong | general | blend70 | 2 | cleaned | text | category | 0.7953 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9473 | no |
| wrong | general | blend70 | 2 | study | text | org | 0.5528 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7095 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.9981 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.6800 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.9959 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9186 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9968 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9986 | no |
| unknown | general | ft | 1 | app | category | unknown | 0.9451 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9987 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9990 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9966 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.8983 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9849 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.4420 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4945 | no |
| unknown | general | ft | 1 | 受入年齢 | category | unknown | 0.7121 | no |
| unknown | general | ft | 1 | 東第5 | quantity | unknown | 0.7668 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9990 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9993 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.6617 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.7190 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9942 | no |
| wrong | general | ft | 1 | organization name | org | person | 0.6023 | no |
| wrong | general | ft | 1 | place | org | address | 0.9923 | no |
| wrong | general | ft | 1 | term | text | category | 0.9967 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.8278 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9976 | no |
| critical | general | ft | 2 | funding | amount | id | 0.7440 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.9516 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9953 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8833 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9703 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9959 | no |
| other_ng | general | ft | 2 | value | other | amount | 0.6019 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9954 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9884 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.8556 | no |
| unknown | general | ft | 2 | author | person | unknown | 0.7428 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9948 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9988 | no |
| unknown | general | ft | 2 | doi | id | unknown | 0.9980 | no |
| unknown | general | ft | 2 | female_frequency | rate | unknown | 0.9090 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9989 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9936 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9977 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9120 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.9624 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.7262 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.4656 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9984 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9993 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9747 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.6016 | no |
| wrong | general | ft | 2 | cause_of_invalid_ranking | text | category | 0.6495 | no |
| wrong | general | ft | 2 | cleaned | text | category | 0.7237 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9902 | no |
| wrong | general | ft | 2 | study | text | org | 0.7861 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9963 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9967 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9967 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9987 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9987 | no |

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 39件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 144件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 110件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行は学習データへコピーしない。出典独立の公開/合成教材を、ラベル定義と根拠付きで監査してから使う。
2. GPUの基準条件は維持し、次の比較では訓練時の表現拡張（FT_AUG=1）だけを追加する。seed 1/2を両条件で比較する。
3. 固定5セットのaccuracy・errors・critical errors・unknownsに加え、時間・最大GPUメモリを回収する。1.5ポイント未満は差なしとする。
4. 原因が確定したとみなすのは、同じ失敗パターンの再検査と改善の再現が取れた場合だけ。ラベル変更・自動自己ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
