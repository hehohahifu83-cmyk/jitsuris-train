# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-18T23:25:42+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 26 | 2 | 17 | 1 |
| business | blend70 | 2 | 490 | 25 | 6 | 10 | 0 |
| business | ft | 1 | 490 | 30 | 2 | 12 | 1 |
| business | ft | 2 | 490 | 26 | 6 | 8 | 1 |
| business2 | blend70 | 1 | 976 | 23 | 5 | 18 | 4 |
| business2 | blend70 | 2 | 976 | 22 | 4 | 20 | 7 |
| business2 | ft | 1 | 976 | 22 | 4 | 17 | 4 |
| business2 | ft | 2 | 976 | 23 | 4 | 20 | 6 |
| dev220 | blend70 | 1 | 220 | 4 | 1 | 2 | 0 |
| dev220 | blend70 | 2 | 220 | 4 | 1 | 2 | 0 |
| dev220 | ft | 1 | 220 | 7 | 1 | 1 | 0 |
| dev220 | ft | 2 | 220 | 4 | 1 | 2 | 0 |
| general | blend70 | 1 | 383 | 7 | 1 | 22 | 6 |
| general | blend70 | 2 | 383 | 8 | 0 | 16 | 7 |
| general | ft | 1 | 383 | 10 | 2 | 18 | 6 |
| general | ft | 2 | 383 | 11 | 2 | 13 | 7 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 20, org→account: 8, category→account: 3, quantity→amount: 2, text→category: 2, account→text: 2, text→account: 2, org→address: 2
- business / ft: category→quantity: 23, org→account: 8, category→account: 4, quantity→amount: 2, text→category: 2, account→text: 2, text→account: 2, org→address: 2
- business2 / blend70: amount→quantity: 6, category→quantity: 5, category→id: 4, account→category: 3, id→category: 3, quantity→amount: 3, account→org: 3, quantity→address: 2
- business2 / ft: amount→quantity: 6, category→quantity: 5, category→id: 4, id→category: 3, category→account: 3, account→org: 3, account→category: 2, quantity→amount: 2
- dev220 / blend70: quantity→category: 3, id→quantity: 2, org→account: 1, category→text: 1, category→tax_class: 1
- dev220 / ft: quantity→category: 3, id→quantity: 2, rate→tax_class: 1, org→person: 1, org→account: 1, text→category: 1, category→text: 1, category→tax_class: 1
- general / blend70: quantity→category: 5, id→address: 2, text→account: 2, id→category: 2, text→category: 1, quantity→rate: 1, category→text: 1, text→person: 1
- general / ft: quantity→category: 4, quantity→rate: 3, text→category: 2, id→address: 2, text→account: 2, id→category: 2, text→org: 1, quantity→amount: 1

### seedをまたいで再発した誤り

- business / blend70: `abn`、id→amount（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `entitiy`、org→account（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / blend70: `title`、category→account（seed 1, seed 2）
- business / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business / ft: `abn`、id→amount（seed 1, seed 2）
- business / ft: `agebann`、category→quantity（seed 1, seed 2）
- business / ft: `d2`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `entitiy`、org→account（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `regrp_sommaire`、account→category（seed 1, seed 2）
- business / ft: `title`、category→account（seed 1, seed 2）
- business / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / blend70: `projection`、category→id（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `service`、account→org（seed 1, seed 2）
- business2 / blend70: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `construction_age_band`、category→date（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms_known`、category→quantity（seed 1, seed 2）
- business2 / ft: `programme`、category→account（seed 1, seed 2）
- business2 / ft: `projection`、category→id（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `service`、account→org（seed 1, seed 2）
- business2 / ft: `total invoices paid`、quantity→amount（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- general / blend70: `cleaned`、text→account（seed 1, seed 2）
- general / blend70: `goal`、id→category（seed 1, seed 2）
- general / blend70: `standardhours`、quantity→category（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `cleaned`、text→account（seed 1, seed 2）
- general / ft: `goal`、id→category（seed 1, seed 2）
- general / ft: `standardhours`、quantity→category（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend70 | 1 | abn | id | amount | 0.6809 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9953 | yes |
| other_ng | business | blend70 | 1 | km budgété | other | category | 0.5709 | no |
| unknown | business | blend70 | 1 | # invoices paid within 30 days | quantity | unknown | 0.6051 | no |
| unknown | business | blend70 | 1 | agebann | category | unknown | 0.4911 | no |
| unknown | business | blend70 | 1 | australian sourced goods | amount | unknown | 0.6807 | no |
| unknown | business | blend70 | 1 | australian sourced services | amount | unknown | 0.6532 | no |
| unknown | business | blend70 | 1 | capital revenue | category | unknown | 0.4926 | no |
| unknown | business | blend70 | 1 | commodity-title_en | product | unknown | 0.4472 | no |
| unknown | business | blend70 | 1 | commodity-title_fr | product | unknown | 0.4426 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9969 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9654 | no |
| unknown | business | blend70 | 1 | ligne | category | unknown | 0.2874 | no |
| unknown | business | blend70 | 1 | overseas sourced goods | amount | unknown | 0.6671 | no |
| unknown | business | blend70 | 1 | overseas sourced services | amount | unknown | 0.4735 | no |
| unknown | business | blend70 | 1 | q2c | category | unknown | 0.4986 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9949 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9909 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9826 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9353 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6964 | no |
| wrong | business | blend70 | 1 | d2 | category | quantity | 0.7067 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7320 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9914 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.8767 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9941 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8436 | no |
| wrong | business | blend70 | 1 | entitiy | org | account | 0.6964 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.8406 | no |
| wrong | business | blend70 | 1 | mois calendrier | date | category | 0.5298 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | address | 0.5406 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.9789 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7033 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.6912 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.6780 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6929 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6971 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7062 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7214 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7179 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7314 | no |
| wrong | business | blend70 | 1 | sub_category | category | account | 0.7382 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.6953 | no |
| wrong | business | blend70 | 1 | type de matériel | category | id | 0.5178 | no |
| critical | business | blend70 | 2 | abn | id | amount | 0.7970 | yes |
| critical | business | blend70 | 2 | australian sourced goods | amount | id | 0.7524 | yes |
| critical | business | blend70 | 2 | australian sourced services | amount | id | 0.8574 | yes |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.5319 | yes |
| critical | business | blend70 | 2 | respnum$ | id | quantity | 0.7452 | yes |
| critical | business | blend70 | 2 | total invoices paid | quantity | amount | 0.9081 | yes |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3879 | no |
| unknown | business | blend70 | 2 | d2 | category | unknown | 0.3893 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9972 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9623 | no |
| unknown | business | blend70 | 2 | mois calendrier | date | unknown | 0.3122 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.4910 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9957 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9906 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9825 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.8606 | no |
| wrong | business | blend70 | 2 | agebann | category | quantity | 0.7024 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7061 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9908 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.8388 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9933 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8507 | no |
| wrong | business | blend70 | 2 | entitiy | org | account | 0.5753 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9219 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7038 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.9599 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.7001 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.6656 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6976 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.6986 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.7040 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7191 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7109 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | category | 0.7218 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.7068 | no |
| critical | business | ft | 1 | abn | id | amount | 0.8056 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9953 | yes |
| other_ng | business | ft | 1 | km budgété | other | category | 0.5252 | no |
| unknown | business | ft | 1 | # invoices paid within 30 days | quantity | unknown | 0.5291 | no |
| unknown | business | ft | 1 | australian sourced goods | amount | unknown | 0.9724 | no |
| unknown | business | ft | 1 | australian sourced services | amount | unknown | 0.9331 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9968 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9945 | no |
| unknown | business | ft | 1 | ligne | category | unknown | 0.3729 | no |
| unknown | business | ft | 1 | overseas sourced goods | amount | unknown | 0.9529 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9955 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9966 | no |
| unknown | business | ft | 1 | reslt_probl_2022-2023 | amount | unknown | 0.5496 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9839 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9724 | no |
| wrong | business | ft | 1 | agebann | category | quantity | 0.6651 | no |
| wrong | business | ft | 1 | capital revenue | category | account | 0.5902 | no |
| wrong | business | ft | 1 | commodity-title_en | product | category | 0.5511 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9896 | no |
| wrong | business | ft | 1 | d2 | category | quantity | 0.9656 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9721 | no |
| wrong | business | ft | 1 | department | org | account | 0.9935 | no |
| wrong | business | ft | 1 | department | org | account | 0.9838 | no |
| wrong | business | ft | 1 | department | org | account | 0.9952 | no |
| wrong | business | ft | 1 | description | account | text | 0.9810 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.9930 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.8735 | no |
| wrong | business | ft | 1 | mois calendrier | date | category | 0.7387 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | address | 0.7714 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.9919 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9938 | no |
| wrong | business | ft | 1 | q2c | category | quantity | 0.7093 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9791 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.9606 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9849 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9873 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9937 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9949 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9940 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9721 | no |
| wrong | business | ft | 1 | sub_category | category | account | 0.9161 | no |
| wrong | business | ft | 1 | title | category | account | 0.9731 | no |
| wrong | business | ft | 1 | type de matériel | category | id | 0.7390 | no |
| critical | business | ft | 2 | abn | id | amount | 0.9714 | yes |
| critical | business | ft | 2 | australian sourced goods | amount | id | 0.9049 | yes |
| critical | business | ft | 2 | australian sourced services | amount | id | 0.8345 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.7598 | yes |
| critical | business | ft | 2 | respnum$ | id | quantity | 0.8321 | yes |
| critical | business | ft | 2 | total invoices paid | quantity | amount | 0.8707 | yes |
| other_ng | business | ft | 2 | km budgété | other | quantity | 0.5593 | no |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4662 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9971 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9899 | no |
| unknown | business | ft | 2 | mois calendrier | date | unknown | 0.4059 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9966 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9961 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9837 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.8657 | no |
| wrong | business | ft | 2 | agebann | category | quantity | 0.9670 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.5121 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9351 | no |
| wrong | business | ft | 2 | department | org | account | 0.9927 | no |
| wrong | business | ft | 2 | department | org | account | 0.9297 | no |
| wrong | business | ft | 2 | department | org | account | 0.9940 | no |
| wrong | business | ft | 2 | description | account | text | 0.9911 | no |
| wrong | business | ft | 2 | entitiy | org | account | 0.8200 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9896 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9784 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.9647 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9892 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9429 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9917 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9896 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9906 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9916 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9840 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | category | 0.9584 | no |
| wrong | business | ft | 2 | title | category | account | 0.9895 | no |
| critical | business2 | blend70 | 1 | # invoices paid within 30 days | quantity | amount | 0.6574 | yes |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.5370 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9900 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.7627 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9953 | yes |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.8893 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.5580 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9147 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.5657 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6998 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.8492 | no |
| unknown | business2 | blend70 | 1 | imd19_national_decile | category | unknown | 0.3153 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9969 | no |
| unknown | business2 | blend70 | 1 | number_habitable_rooms | quantity | unknown | 0.5772 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9937 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9972 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9970 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9953 | no |
| unknown | business2 | blend70 | 1 | value | amount | unknown | 0.5827 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9976 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9841 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9918 | no |
| unknown | business2 | blend70 | 1 | want to live in this parish only | quantity | unknown | 0.4851 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9883 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.6997 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.6656 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6944 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6953 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6228 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.8896 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms_known | category | quantity | 0.6829 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6260 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7586 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7380 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.9789 | no |
| wrong | business2 | blend70 | 1 | service | account | org | 0.6614 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.5306 | no |
| wrong | business2 | blend70 | 1 | situtation | address | text | 0.7001 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6654 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6537 | no |
| wrong | business2 | blend70 | 1 | total_floor_area_known | category | quantity | 0.5290 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9653 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.5177 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9899 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8320 | yes |
| critical | business2 | blend70 | 2 | total invoices paid | quantity | amount | 0.8388 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.7066 | no |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.6712 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9362 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.7403 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.6011 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace gains sqm | other | quantity | 0.6455 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.7149 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | epc_score_known | category | unknown | 0.4158 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9709 | no |
| unknown | business2 | blend70 | 2 | monitor | id | unknown | 0.4200 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9972 | no |
| unknown | business2 | blend70 | 2 | number_habitable_rooms | quantity | unknown | 0.6990 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9928 | no |
| unknown | business2 | blend70 | 2 | programme | category | unknown | 0.4767 | no |
| unknown | business2 | blend70 | 2 | service_responsable | account | unknown | 0.4865 | no |
| unknown | business2 | blend70 | 2 | surveyname | text | unknown | 0.3675 | no |
| unknown | business2 | blend70 | 2 | terrace | quantity | unknown | 0.4128 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9969 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9964 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9954 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9345 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9751 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9886 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6175 | no |
| wrong | business2 | blend70 | 2 | basis | category | account | 0.6533 | no |
| wrong | business2 | blend70 | 2 | code | address | id | 0.6064 | no |
| wrong | business2 | blend70 | 2 | construction_age_band | category | date | 0.6907 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6549 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6945 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.7222 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8969 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6318 | no |
| wrong | business2 | blend70 | 2 | potential_epc_rating_known | category | quantity | 0.6152 | no |
| wrong | business2 | blend70 | 2 | potential_epc_score_known | category | quantity | 0.5054 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6418 | no |
| wrong | business2 | blend70 | 2 | projection | category | id | 0.6749 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9809 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6226 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.8343 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8757 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.8503 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.7232 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9963 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8722 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9954 | yes |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9210 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.7039 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9393 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.7300 | no |
| unknown | business2 | ft | 1 | # invoices paid within 30 days | quantity | unknown | 0.5236 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.9762 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9972 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.8127 | no |
| unknown | business2 | ft | 1 | imd19_national_decile | category | unknown | 0.3713 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9972 | no |
| unknown | business2 | ft | 1 | number_habitable_rooms | quantity | unknown | 0.8123 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9919 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9971 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9971 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9969 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9969 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9972 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9967 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9829 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9889 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9963 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.7243 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.9290 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9920 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9933 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7650 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.9805 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms_known | category | quantity | 0.9661 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.8939 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9964 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9965 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.9921 | no |
| wrong | business2 | ft | 1 | service | account | org | 0.9430 | no |
| wrong | business2 | ft | 1 | situtation | address | text | 0.9789 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9501 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9336 | no |
| wrong | business2 | ft | 1 | total_floor_area_known | category | quantity | 0.7027 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9966 | no |
| wrong | business2 | ft | 1 | want to live in this parish only | quantity | category | 0.6182 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.6957 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9962 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9712 | yes |
| critical | business2 | ft | 2 | total invoices paid | quantity | amount | 0.7717 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.9644 | no |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace losses sqm | other | quantity | 0.9034 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9880 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.9643 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.8787 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.9432 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9974 | no |
| unknown | business2 | ft | 2 | epc_rating_known | category | unknown | 0.4950 | no |
| unknown | business2 | ft | 2 | epc_score_known | category | unknown | 0.5537 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9865 | no |
| unknown | business2 | ft | 2 | monitor | id | unknown | 0.4753 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9975 | no |
| unknown | business2 | ft | 2 | number_habitable_rooms | quantity | unknown | 0.9863 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9907 | no |
| unknown | business2 | ft | 2 | surveyname | text | unknown | 0.4766 | no |
| unknown | business2 | ft | 2 | terrace | quantity | unknown | 0.3802 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9971 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9967 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9965 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9964 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9974 | no |
| unknown | business2 | ft | 2 | total_floor_area_known | category | unknown | 0.4694 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9976 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9121 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9650 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9968 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.8818 | no |
| wrong | business2 | ft | 2 | basis | category | account | 0.9328 | no |
| wrong | business2 | ft | 2 | code | address | id | 0.8333 | no |
| wrong | business2 | ft | 2 | construction_age_band | category | date | 0.9648 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.9355 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9921 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.9828 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9910 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.8932 | no |
| wrong | business2 | ft | 2 | potential_epc_rating_known | category | quantity | 0.8664 | no |
| wrong | business2 | ft | 2 | potential_epc_score_known | category | quantity | 0.7082 | no |
| wrong | business2 | ft | 2 | programme | category | account | 0.6807 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.8295 | no |
| wrong | business2 | ft | 2 | projection | category | id | 0.9064 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9950 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.8877 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.9115 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9331 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.8324 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9105 | yes |
| unknown | dev220 | blend70 | 1 | credit limit | amount | unknown | 0.3964 | no |
| unknown | dev220 | blend70 | 1 | 税率 | rate | unknown | 0.4785 | no |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.8827 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7492 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.6867 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.7223 | yes |
| unknown | dev220 | blend70 | 2 | credit limit | amount | unknown | 0.4257 | no |
| unknown | dev220 | blend70 | 2 | customer rank | quantity | unknown | 0.5207 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.6761 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9559 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.8026 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9585 | yes |
| unknown | dev220 | ft | 1 | credit limit | amount | unknown | 0.4705 | no |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.8908 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9864 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9373 | no |
| wrong | dev220 | ft | 1 | 支払者の氏名又は名称 | org | person | 0.5888 | no |
| wrong | dev220 | ft | 1 | 税率 | rate | tax_class | 0.6723 | no |
| wrong | dev220 | ft | 1 | 随意契約理由 | text | category | 0.5076 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.6896 | yes |
| unknown | dev220 | ft | 2 | credit limit | amount | unknown | 0.5124 | no |
| unknown | dev220 | ft | 2 | customer rank | quantity | unknown | 0.7140 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.8820 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9432 | no |
| wrong | dev220 | ft | 2 | terms | category | text | 0.8237 | no |
| critical | general | blend70 | 1 | n_occurences | quantity | rate | 0.7046 | yes |
| other_ng | general | blend70 | 1 | dag-stage | other | category | 0.8273 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.5313 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.6327 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.8882 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.9297 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9634 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8857 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.4240 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.5572 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.4391 | no |
| unknown | general | blend70 | 1 | bib | id | unknown | 0.4369 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8559 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9469 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9861 | no |
| unknown | general | blend70 | 1 | ngram | text | unknown | 0.4931 | no |
| unknown | general | blend70 | 1 | place | org | unknown | 0.3915 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.2976 | no |
| unknown | general | blend70 | 1 | raw | category | unknown | 0.3816 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.7379 | no |
| unknown | general | blend70 | 1 | source | category | unknown | 0.4923 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.6834 | no |
| unknown | general | blend70 | 1 | standardhours | quantity | unknown | 0.3760 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.3137 | no |
| unknown | general | blend70 | 1 | 城南第2 | quantity | unknown | 0.4943 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9619 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9980 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9582 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.2927 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.6867 | no |
| wrong | general | blend70 | 1 | goal | id | category | 0.9714 | no |
| wrong | general | blend70 | 1 | standardhours | quantity | category | 0.7764 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.6991 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.9646 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7069 | no |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.5351 | no |
| other_ng | general | blend70 | 2 | dbpedia_score | other | rate | 0.7699 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6227 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9476 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6250 | no |
| other_ng | general | blend70 | 2 | value | other | rate | 0.9314 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9914 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.8668 | no |
| unknown | general | blend70 | 2 | age_q1_nd | quantity | unknown | 0.4912 | no |
| unknown | general | blend70 | 2 | age_q3 | quantity | unknown | 0.4616 | no |
| unknown | general | blend70 | 2 | age_q3_nd | quantity | unknown | 0.4531 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8557 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9473 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9865 | no |
| unknown | general | blend70 | 2 | pelicula | text | unknown | 0.4817 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.6423 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7455 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6648 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3788 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9635 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9981 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9507 | no |
| unknown | general | blend70 | 2 | 読み方 | address | unknown | 0.3460 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.6778 | no |
| wrong | general | blend70 | 2 | goal | id | category | 0.9072 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9486 | no |
| wrong | general | blend70 | 2 | standardhours | quantity | category | 0.7219 | no |
| wrong | general | blend70 | 2 | study | text | person | 0.6653 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.9745 | no |
| wrong | general | blend70 | 2 | 住家一部損壊 | quantity | category | 0.5609 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.5104 | no |
| critical | general | ft | 1 | n_occurences | quantity | rate | 0.9180 | yes |
| critical | general | ft | 1 | 城南第2 | quantity | amount | 0.7061 | yes |
| other_ng | general | ft | 1 | dag-stage | other | category | 0.8230 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.6427 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.8988 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.8648 | no |
| other_ng | general | ft | 1 | value | other | rate | 0.9715 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9497 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9868 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.4712 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.4432 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.4455 | no |
| unknown | general | ft | 1 | bib | id | unknown | 0.4903 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9943 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9951 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9953 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.4006 | no |
| unknown | general | ft | 1 | raw | category | unknown | 0.5443 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.9830 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.9762 | no |
| unknown | general | ft | 1 | standardhours | quantity | unknown | 0.4917 | no |
| unknown | general | ft | 1 | 住家全壊 | quantity | unknown | 0.4474 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9938 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9972 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9734 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.3536 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.9751 | no |
| wrong | general | ft | 1 | goal | id | category | 0.9847 | no |
| wrong | general | ft | 1 | ngram | text | org | 0.6958 | no |
| wrong | general | ft | 1 | source | category | org | 0.7032 | no |
| wrong | general | ft | 1 | standardhours | quantity | category | 0.8696 | no |
| wrong | general | ft | 1 | term | text | category | 0.9967 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9745 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9925 | no |
| critical | general | ft | 2 | age_q3 | quantity | rate | 0.6063 | yes |
| critical | general | ft | 2 | age_q3_nd | quantity | rate | 0.5542 | yes |
| other_ng | general | ft | 2 | _status_ | other | category | 0.5694 | no |
| other_ng | general | ft | 2 | dbpedia_score | other | rate | 0.9835 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8844 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9497 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.8865 | no |
| other_ng | general | ft | 2 | value | other | rate | 0.9740 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9896 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.9598 | no |
| unknown | general | ft | 2 | age_q1_nd | quantity | unknown | 0.3799 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9941 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9956 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9960 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.8931 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9939 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.9497 | no |
| unknown | general | ft | 2 | 住家一部損壊 | quantity | unknown | 0.4855 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9960 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9973 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9626 | no |
| unknown | general | ft | 2 | 読み方 | address | unknown | 0.4824 | no |
| wrong | general | ft | 2 | cause_of_invalid_ranking | text | category | 0.6471 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.9623 | no |
| wrong | general | ft | 2 | goal | id | category | 0.8929 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9920 | no |
| wrong | general | ft | 2 | mechanism | category | id | 0.5057 | no |
| wrong | general | ft | 2 | standardhours | quantity | category | 0.7917 | no |
| wrong | general | ft | 2 | study | text | person | 0.9096 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9886 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.7118 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9949 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9954 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9961 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9969 | no |

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 42件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 147件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 109件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
