# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-19T11:06:57+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 21 | 0 | 18 | 0 |
| business | blend70 | 2 | 490 | 27 | 4 | 11 | 1 |
| business | ft | 1 | 490 | 26 | 1 | 11 | 0 |
| business | ft | 2 | 490 | 31 | 4 | 7 | 1 |
| business2 | blend70 | 1 | 976 | 20 | 3 | 17 | 12 |
| business2 | blend70 | 2 | 976 | 23 | 3 | 14 | 8 |
| business2 | ft | 1 | 976 | 22 | 3 | 15 | 14 |
| business2 | ft | 2 | 976 | 23 | 3 | 15 | 9 |
| dev220 | blend70 | 1 | 220 | 7 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 5 | 1 | 0 | 0 |
| dev220 | ft | 1 | 220 | 7 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 5 | 1 | 0 | 0 |
| general | blend70 | 1 | 383 | 9 | 1 | 18 | 6 |
| general | blend70 | 2 | 383 | 4 | 1 | 19 | 7 |
| general | ft | 1 | 383 | 9 | 1 | 17 | 7 |
| general | ft | 2 | 383 | 4 | 1 | 17 | 7 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 13, org→account: 7, category→id: 5, org→address: 3, account→category: 3, amount→quantity: 3, account→text: 2, text→account: 2
- business / ft: category→quantity: 15, org→account: 8, category→id: 6, amount→quantity: 4, org→address: 3, account→category: 3, account→text: 2, text→account: 2
- business2 / blend70: amount→quantity: 6, category→id: 5, account→category: 4, id→category: 4, quantity→address: 3, quantity→category: 3, category→quantity: 3, category→address: 2
- business2 / ft: amount→quantity: 6, category→id: 5, account→category: 4, id→category: 4, category→quantity: 4, quantity→address: 3, quantity→category: 3, category→amount: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- dev220 / ft: quantity→category: 4, org→account: 2, category→tax_class: 2, id→quantity: 2, category→text: 1, address→id: 1
- general / blend70: category→text: 3, id→address: 2, text→account: 2, date→id: 1, org→address: 1, text→category: 1, quantity→category: 1, id→category: 1
- general / ft: category→text: 3, id→address: 2, text→account: 2, date→id: 1, org→address: 1, text→category: 1, quantity→category: 1, id→category: 1

### seedをまたいで再発した誤り

- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `commodity-title_en`、product→category（seed 1, seed 2）
- business / ft: `d2`、category→amount（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `procurementclassification:proclasslabel`、account→category（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `service_responsable`、account→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→text（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service_responsable`、account→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→text（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `total_floor_area_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `taxable`、category→tax_class（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend70: `cleaned`、text→account（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `cleaned`、text→account（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.4169 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.5809 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4937 | no |
| unknown | business | blend70 | 1 | d1 | category | unknown | 0.3577 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.3962 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9986 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9681 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.4513 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.4763 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.4298 | no |
| unknown | business | blend70 | 1 | q5a | category | unknown | 0.4510 | no |
| unknown | business | blend70 | 1 | q5b | category | unknown | 0.4921 | no |
| unknown | business | blend70 | 1 | q7 | category | unknown | 0.4896 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9974 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9927 | no |
| unknown | business | blend70 | 1 | total invoices paid | quantity | unknown | 0.6139 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9920 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9514 | no |
| wrong | business | blend70 | 1 | agebann | category | quantity | 0.6951 | no |
| wrong | business | blend70 | 1 | d2 | category | amount | 0.5982 | no |
| wrong | business | blend70 | 1 | d6 | category | id | 0.6446 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9952 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8871 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9968 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8532 | no |
| wrong | business | blend70 | 1 | merchant details | text | org | 0.7572 | no |
| wrong | business | blend70 | 1 | mois calendrier | date | category | 0.6864 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | account | 0.6960 | no |
| wrong | business | blend70 | 1 | procurementclassification:proclasslabel | account | category | 0.6055 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6616 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9666 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.6802 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.6945 | no |
| wrong | business | blend70 | 1 | q3_2 | category | id | 0.6922 | no |
| wrong | business | blend70 | 1 | q4b_1 | category | id | 0.6372 | no |
| wrong | business | blend70 | 1 | q6 | category | id | 0.5619 | no |
| wrong | business | blend70 | 1 | q8 | category | id | 0.6669 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7203 | no |
| wrong | business | blend70 | 1 | title | category | text | 0.8367 | no |
| critical | business | blend70 | 2 | australian sourced goods | amount | quantity | 0.6781 | yes |
| critical | business | blend70 | 2 | mois calendrier | date | quantity | 0.6843 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6954 | yes |
| critical | business | blend70 | 2 | overseas sourced services | amount | quantity | 0.6363 | yes |
| other_ng | business | blend70 | 2 | km budgété | other | amount | 0.6281 | no |
| unknown | business | blend70 | 2 | agebann | category | unknown | 0.4334 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4381 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.4186 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.4244 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9985 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9669 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9973 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9926 | no |
| unknown | business | blend70 | 2 | regrp_sommaire | account | unknown | 0.4343 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9928 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9512 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.6036 | no |
| wrong | business | blend70 | 2 | capital revenue | category | account | 0.7773 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.5495 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7082 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9950 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8833 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9966 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8546 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.7662 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9284 | no |
| wrong | business | blend70 | 2 | portefeuille_nom_et_code | org | address | 0.6893 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.7235 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7169 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.7994 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.7036 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.7033 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6583 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6929 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.6851 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.6917 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7196 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7159 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.7109 | no |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.6804 | yes |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.5955 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.8297 | no |
| unknown | business | ft | 1 | d1 | category | unknown | 0.4952 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9992 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9984 | no |
| unknown | business | ft | 1 | ligne | category | unknown | 0.4096 | no |
| unknown | business | ft | 1 | q5a | category | unknown | 0.4470 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9973 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9955 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.9567 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.6175 | no |
| wrong | business | ft | 1 | d2 | category | amount | 0.8545 | no |
| wrong | business | ft | 1 | d6 | category | id | 0.8425 | no |
| wrong | business | ft | 1 | department | org | account | 0.9989 | no |
| wrong | business | ft | 1 | department | org | account | 0.9987 | no |
| wrong | business | ft | 1 | department | org | account | 0.9990 | no |
| wrong | business | ft | 1 | description | account | text | 0.9947 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.5100 | no |
| wrong | business | ft | 1 | merchant details | text | org | 0.9831 | no |
| wrong | business | ft | 1 | mois calendrier | date | category | 0.9623 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | account | 0.5770 | no |
| wrong | business | ft | 1 | procurementclassification:proclasslabel | account | category | 0.8099 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9180 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9743 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9608 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9837 | no |
| wrong | business | ft | 1 | q3_2 | category | id | 0.9792 | no |
| wrong | business | ft | 1 | q4b_1 | category | id | 0.9012 | no |
| wrong | business | ft | 1 | q5b | category | id | 0.6964 | no |
| wrong | business | ft | 1 | q6 | category | id | 0.7983 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.6637 | no |
| wrong | business | ft | 1 | q8 | category | id | 0.9485 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9563 | no |
| wrong | business | ft | 1 | title | category | text | 0.8317 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.9687 | yes |
| critical | business | ft | 2 | mois calendrier | date | quantity | 0.6474 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.9933 | yes |
| critical | business | ft | 2 | overseas sourced services | amount | quantity | 0.8991 | yes |
| other_ng | business | ft | 2 | km budgété | other | amount | 0.7839 | no |
| unknown | business | ft | 2 | australian sourced services | amount | unknown | 0.4462 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9990 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9966 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9990 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9990 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9985 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9951 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.8343 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.5827 | no |
| wrong | business | ft | 2 | capital revenue | category | account | 0.9970 | no |
| wrong | business | ft | 2 | commodity-title_en | product | category | 0.5101 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.7797 | no |
| wrong | business | ft | 2 | d2 | category | amount | 0.6062 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9381 | no |
| wrong | business | ft | 2 | department | org | account | 0.9985 | no |
| wrong | business | ft | 2 | department | org | account | 0.9932 | no |
| wrong | business | ft | 2 | department | org | account | 0.9987 | no |
| wrong | business | ft | 2 | description | account | text | 0.9967 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.9938 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9988 | no |
| wrong | business | ft | 2 | portefeuille_nom_et_code | org | address | 0.9838 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.9784 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9970 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.7354 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9941 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9963 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9325 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9849 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9702 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9730 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9923 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9910 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | tax_class | 0.6204 | no |
| wrong | business | ft | 2 | title | category | account | 0.9954 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7283 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9922 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8512 | yes |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.7296 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.7380 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace net sqm | other | quantity | 0.6399 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.9434 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.7646 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace net sqm | other | quantity | 0.6804 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9081 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace gains sqm | other | quantity | 0.7126 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace losses sqm | other | quantity | 0.6942 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.7530 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace losses sqm | other | quantity | 0.7258 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace net sqm | other | quantity | 0.6984 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.7156 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9795 | no |
| unknown | business2 | blend70 | 1 | imd19_income_decile | category | unknown | 0.3594 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 1 | terrace | quantity | unknown | 0.4884 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 1 | total invoices paid | quantity | unknown | 0.5814 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9952 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9898 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8830 | no |
| wrong | business2 | blend70 | 1 | contravention | category | text | 0.9280 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6983 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.7361 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8822 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9881 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6559 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6539 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7599 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7392 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9678 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.6202 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8674 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.6174 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6530 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.7019 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9670 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.7056 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9920 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8509 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.6758 | no |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.5429 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9377 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.7365 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.9463 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace gains sqm | other | quantity | 0.6014 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.7386 | no |
| other_ng | business2 | blend70 | 2 | total_floor_area | other | quantity | 0.7107 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9619 | no |
| unknown | business2 | blend70 | 2 | habitatdescription | text | unknown | 0.4710 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9986 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9981 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9966 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9945 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9901 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6580 | no |
| wrong | business2 | blend70 | 2 | construction_age_band | category | date | 0.5369 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6984 | no |
| wrong | business2 | blend70 | 2 | imd19_national_decile | category | id | 0.6895 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6978 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7308 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.9001 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.5438 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7570 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.7372 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9814 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6936 | no |
| wrong | business2 | blend70 | 2 | service_responsable | account | category | 0.6244 | no |
| wrong | business2 | blend70 | 2 | situtation | address | text | 0.5553 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.9182 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.5775 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6237 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6836 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.6837 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9671 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9965 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9993 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9985 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.9973 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.9989 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace net sqm | other | quantity | 0.8933 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9983 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.9990 | no |
| other_ng | business2 | ft | 1 | a2 floorspace net sqm | other | quantity | 0.9444 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9298 | no |
| other_ng | business2 | ft | 1 | b1a floorspace gains sqm | other | quantity | 0.9747 | no |
| other_ng | business2 | ft | 1 | b1a floorspace losses sqm | other | quantity | 0.9443 | no |
| other_ng | business2 | ft | 1 | b1a floorspace net sqm | other | quantity | 0.7027 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.9977 | no |
| other_ng | business2 | ft | 1 | d2 floorspace losses sqm | other | quantity | 0.9805 | no |
| other_ng | business2 | ft | 1 | d2 floorspace net sqm | other | quantity | 0.9960 | no |
| other_ng | business2 | ft | 1 | potential_epc_score | other | quantity | 0.6573 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9988 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9988 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9982 | no |
| unknown | business2 | ft | 1 | terrace | quantity | unknown | 0.4917 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9988 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9987 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9985 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9861 | no |
| wrong | business2 | ft | 1 | contravention | category | text | 0.9772 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.5134 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9975 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.9269 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.9699 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.9976 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9275 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9339 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9982 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9982 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9762 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.8852 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9416 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.8607 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9323 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.9496 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9990 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.5863 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.9642 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9991 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9982 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.9203 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.7202 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9900 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.9589 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9844 | no |
| other_ng | business2 | ft | 2 | avg_tilt | other | rate | 0.6896 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.8157 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.9770 | no |
| other_ng | business2 | ft | 2 | total_floor_area | other | quantity | 0.9237 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9991 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9737 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9995 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.6316 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 2 | surveyname | text | unknown | 0.4929 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9992 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9990 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9990 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9991 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9978 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9982 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9989 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9397 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.7451 | no |
| wrong | business2 | ft | 2 | habitatdescription | text | category | 0.5267 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.9977 | no |
| wrong | business2 | ft | 2 | imd19_national_decile | category | id | 0.9821 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9968 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9194 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9955 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.6209 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9940 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9953 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9957 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.9891 | no |
| wrong | business2 | ft | 2 | service_responsable | account | category | 0.5945 | no |
| wrong | business2 | ft | 2 | situtation | address | text | 0.7720 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9939 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.8904 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9764 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.9237 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9992 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9386 | yes |
| wrong | dev220 | blend70 | 1 | city | address | id | 0.8895 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9578 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7577 | no |
| wrong | dev220 | blend70 | 1 | taxable | category | tax_class | 0.7462 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.7874 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7130 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9382 | yes |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8386 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7394 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9646 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.7092 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9987 | yes |
| wrong | dev220 | ft | 1 | city | address | id | 0.9793 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9981 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9986 | no |
| wrong | dev220 | ft | 1 | taxable | category | tax_class | 0.6437 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.8019 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9749 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9981 | yes |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8278 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9724 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9557 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.9694 | no |
| critical | general | blend70 | 1 | itemfield14 | date | id | 0.6836 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.9442 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7239 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.5802 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9207 | no |
| other_ng | general | blend70 | 1 | operationid | other | id | 0.5083 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9958 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8940 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.7330 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.6410 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.4103 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8590 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9497 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9884 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.3195 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.7301 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.5914 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.6302 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.6327 | no |
| unknown | general | blend70 | 1 | 住家一部損壊 | quantity | unknown | 0.4862 | no |
| unknown | general | blend70 | 1 | 受入年齢 | category | unknown | 0.6053 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9657 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9751 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.2850 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.6161 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.9146 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9518 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7381 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6607 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.9550 | no |
| wrong | general | blend70 | 1 | データセット_キーワード | category | text | 0.5703 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7108 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.6750 | yes |
| other_ng | general | blend70 | 2 | _status_ | other | category | 0.6274 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9246 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6780 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9675 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6734 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.7391 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9909 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7816 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.5125 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.5760 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.4919 | no |
| unknown | general | blend70 | 2 | author | person | unknown | 0.3872 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.7146 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9496 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9853 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.7146 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.6109 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7470 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6752 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.7227 | no |
| unknown | general | blend70 | 2 | standardhours | quantity | unknown | 0.6005 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3836 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9656 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9735 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.6388 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.6064 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9422 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7097 | no |
| critical | general | ft | 1 | itemfield14 | date | id | 0.7870 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.9900 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.9179 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.8238 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9113 | no |
| other_ng | general | ft | 1 | nodes | other | category | 0.6068 | no |
| other_ng | general | ft | 1 | operationid | other | id | 0.7198 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9960 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9986 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.7254 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.5629 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.4695 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9988 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9991 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9987 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.4319 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9718 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.8449 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.8548 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.8639 | no |
| unknown | general | ft | 1 | 受入年齢 | category | unknown | 0.8613 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9992 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9992 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9975 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.4057 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.8742 | no |
| wrong | general | ft | 1 | goal | id | category | 0.9036 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9966 | no |
| wrong | general | ft | 1 | place | org | address | 0.9874 | no |
| wrong | general | ft | 1 | term | text | category | 0.9419 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9607 | no |
| wrong | general | ft | 1 | データセット_キーワード | category | text | 0.8071 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9982 | no |
| critical | general | ft | 2 | goal | id | quantity | 0.9468 | yes |
| other_ng | general | ft | 2 | _status_ | other | category | 0.8951 | no |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9620 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.9635 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9782 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9556 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.6993 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9889 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8380 | no |
| unknown | general | ft | 2 | age_q3 | quantity | unknown | 0.4955 | no |
| unknown | general | ft | 2 | author | person | unknown | 0.4509 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.7924 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9990 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9942 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9964 | no |
| unknown | general | ft | 2 | raw | category | unknown | 0.8720 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9960 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9645 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.9869 | no |
| unknown | general | ft | 2 | standardhours | quantity | unknown | 0.8181 | no |
| unknown | general | ft | 2 | 住家全壊 | quantity | unknown | 0.5383 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9991 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9992 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9952 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.9111 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.8604 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9830 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9966 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9965 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9963 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9984 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9981 | no |

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 29件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 141件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 109件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
