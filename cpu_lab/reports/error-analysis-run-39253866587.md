# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-19T13:53:50+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend70 | 1 | 490 | 27 | 5 | 8 | 1 |
| business | blend70 | 2 | 490 | 26 | 1 | 11 | 0 |
| business | ft | 1 | 490 | 28 | 5 | 8 | 0 |
| business | ft | 2 | 490 | 30 | 2 | 7 | 0 |
| business2 | blend70 | 1 | 976 | 21 | 4 | 16 | 9 |
| business2 | blend70 | 2 | 976 | 24 | 3 | 19 | 9 |
| business2 | ft | 1 | 976 | 21 | 4 | 16 | 12 |
| business2 | ft | 2 | 976 | 26 | 3 | 16 | 10 |
| dev220 | blend70 | 1 | 220 | 6 | 1 | 0 | 0 |
| dev220 | blend70 | 2 | 220 | 7 | 1 | 1 | 0 |
| dev220 | ft | 1 | 220 | 7 | 1 | 0 | 0 |
| dev220 | ft | 2 | 220 | 6 | 1 | 1 | 0 |
| general | blend70 | 1 | 383 | 7 | 0 | 16 | 6 |
| general | blend70 | 2 | 383 | 9 | 1 | 17 | 5 |
| general | ft | 1 | 383 | 9 | 1 | 14 | 5 |
| general | ft | 2 | 383 | 10 | 2 | 14 | 6 |
| japan_procurement | blend70 | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | blend70 | 2 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 1 | 92 | 0 | 0 | 1 | 0 |
| japan_procurement | ft | 2 | 92 | 0 | 0 | 1 | 0 |

### 取り違えの頻度

- business / blend70: category→quantity: 21, org→account: 7, amount→quantity: 4, org→address: 2, text→category: 2, account→text: 2, text→account: 2, account→category: 2
- business / ft: category→quantity: 21, org→account: 8, amount→quantity: 5, category→account: 3, org→address: 2, text→category: 2, account→text: 2, text→account: 2
- business2 / blend70: amount→quantity: 6, quantity→category: 5, account→category: 4, id→category: 4, quantity→address: 4, category→quantity: 3, category→id: 2, category→amount: 2
- business2 / ft: amount→quantity: 6, quantity→category: 5, account→category: 4, id→category: 4, quantity→address: 4, category→quantity: 4, category→id: 2, category→amount: 2
- dev220 / blend70: quantity→category: 4, org→account: 2, category→text: 2, id→quantity: 2, org→person: 1, rate→tax_class: 1, category→tax_class: 1
- dev220 / ft: quantity→category: 4, org→account: 2, id→quantity: 2, org→person: 1, category→text: 1, org→address: 1, rate→tax_class: 1, category→tax_class: 1
- general / blend70: quantity→category: 4, category→text: 2, org→address: 2, id→address: 2, text→account: 2, text→category: 1, org→person: 1, address→org: 1
- general / ft: quantity→category: 5, category→text: 2, org→address: 2, id→address: 2, text→account: 2, id→quantity: 2, text→category: 1, org→person: 1

### seedをまたいで再発した誤り

- business / blend70: `d1`、category→quantity（seed 1, seed 2）
- business / blend70: `d6`、category→quantity（seed 1, seed 2）
- business / blend70: `department`、org→account（seed 1, seed 2）
- business / blend70: `description`、account→text（seed 1, seed 2）
- business / blend70: `merchant details`、text→category（seed 1, seed 2）
- business / blend70: `mois calendrier`、date→category（seed 1, seed 2）
- business / blend70: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
- business / blend70: `publisher label`、org→address（seed 1, seed 2）
- business / blend70: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / blend70: `q2a`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_1`、category→quantity（seed 1, seed 2）
- business / blend70: `q3_2`、category→quantity（seed 1, seed 2）
- business / blend70: `q5a`、category→quantity（seed 1, seed 2）
- business / blend70: `q5b`、category→quantity（seed 1, seed 2）
- business / blend70: `q6`、category→quantity（seed 1, seed 2）
- business / blend70: `q7`、category→quantity（seed 1, seed 2）
- business / blend70: `q8`、category→quantity（seed 1, seed 2）
- business / blend70: `title`、category→account（seed 1, seed 2）
- business / ft: `australian sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `d1`、category→quantity（seed 1, seed 2）
- business / ft: `d6`、category→quantity（seed 1, seed 2）
- business / ft: `department`、org→account（seed 1, seed 2）
- business / ft: `description`、account→text（seed 1, seed 2）
- business / ft: `merchant details`、text→category（seed 1, seed 2）
- business / ft: `mois calendrier`、date→category（seed 1, seed 2）
- business / ft: `overseas sourced goods`、amount→quantity（seed 1, seed 2）
- business / ft: `publisher label`、org→address（seed 1, seed 2）
- business / ft: `purposeofexpenditure`、text→account（seed 1, seed 2）
- business / ft: `q2a`、category→quantity（seed 1, seed 2）
- business / ft: `q3_1`、category→quantity（seed 1, seed 2）
- business / ft: `q3_2`、category→quantity（seed 1, seed 2）
- business / ft: `q5a`、category→quantity（seed 1, seed 2）
- business / ft: `q5b`、category→quantity（seed 1, seed 2）
- business / ft: `q6`、category→quantity（seed 1, seed 2）
- business / ft: `q7`、category→quantity（seed 1, seed 2）
- business / ft: `q8`、category→quantity（seed 1, seed 2）
- business / ft: `title`、category→account（seed 1, seed 2）
- business2 / blend70: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / blend70: `fine`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / blend70: `loac_group`、category→address（seed 1, seed 2）
- business2 / blend70: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `monitor`、id→category（seed 1, seed 2）
- business2 / blend70: `name`、org→address（seed 1, seed 2）
- business2 / blend70: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / blend70: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / blend70: `scheme`、id→category（seed 1, seed 2）
- business2 / blend70: `situtation`、address→category（seed 1, seed 2）
- business2 / blend70: `terrace`、quantity→address（seed 1, seed 2）
- business2 / blend70: `type`、account→category（seed 1, seed 2）
- business2 / ft: `bike_stands`、quantity→category（seed 1, seed 2）
- business2 / ft: `fine`、amount→quantity（seed 1, seed 2）
- business2 / ft: `imd19_income_decile`、category→amount（seed 1, seed 2）
- business2 / ft: `loac_group`、category→address（seed 1, seed 2）
- business2 / ft: `miscellaneous_divers`、amount→quantity（seed 1, seed 2）
- business2 / ft: `monitor`、id→category（seed 1, seed 2）
- business2 / ft: `name`、org→address（seed 1, seed 2）
- business2 / ft: `number_habitable_rooms`、quantity→category（seed 1, seed 2）
- business2 / ft: `sales-goods-svcs_ventes-biens-srvs`、amount→quantity（seed 1, seed 2）
- business2 / ft: `scheme`、id→category（seed 1, seed 2）
- business2 / ft: `situtation`、address→category（seed 1, seed 2）
- business2 / ft: `terrace`、quantity→address（seed 1, seed 2）
- business2 / ft: `type`、account→category（seed 1, seed 2）
- dev220 / blend70: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / blend70: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / blend70: `terms`、category→text（seed 1, seed 2）
- dev220 / blend70: `担当課`、org→account（seed 1, seed 2）
- dev220 / ft: `customer rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `purchase order by customer`、id→quantity（seed 1, seed 2）
- dev220 / ft: `supplier rank`、quantity→category（seed 1, seed 2）
- dev220 / ft: `担当課`、org→account（seed 1, seed 2）
- general / blend70: `cleaned`、text→account（seed 1, seed 2）
- general / blend70: `keyword`、category→text（seed 1, seed 2）
- general / blend70: `place`、org→address（seed 1, seed 2）
- general / blend70: `year_step_size`、quantity→category（seed 1, seed 2）
- general / blend70: `発生県`、id→address（seed 1, seed 2）
- general / ft: `cleaned`、text→account（seed 1, seed 2）
- general / ft: `goal`、id→quantity（seed 1, seed 2）
- general / ft: `keyword`、category→text（seed 1, seed 2）
- general / ft: `place`、org→address（seed 1, seed 2）
- general / ft: `year_step_size`、quantity→category（seed 1, seed 2）
- general / ft: `住家全壊`、quantity→category（seed 1, seed 2）
- general / ft: `発生県`、id→address（seed 1, seed 2）

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend70 | 1 | australian sourced goods | amount | quantity | 0.6930 | yes |
| critical | business | blend70 | 1 | overseas sourced goods | amount | quantity | 0.6931 | yes |
| critical | business | blend70 | 1 | overseas sourced services | amount | quantity | 0.5127 | yes |
| critical | business | blend70 | 1 | respnum$ | id | amount | 0.6787 | yes |
| critical | business | blend70 | 1 | total invoices paid | quantity | amount | 0.9978 | yes |
| other_ng | business | blend70 | 1 | km budgété | other | category | 0.5182 | no |
| unknown | business | blend70 | 1 | entitiy | org | unknown | 0.3810 | no |
| unknown | business | blend70 | 1 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend70 | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9683 | no |
| unknown | business | blend70 | 1 | quarter | date | unknown | 0.9974 | no |
| unknown | business | blend70 | 1 | quarterno | date | unknown | 0.9928 | no |
| unknown | business | blend70 | 1 | segment-title_en | category | unknown | 0.3735 | no |
| unknown | business | blend70 | 1 | 目名 | category | unknown | 0.9929 | no |
| unknown | business | blend70 | 1 | 科名 | category | unknown | 0.9495 | no |
| wrong | business | blend70 | 1 | d1 | category | quantity | 0.6998 | no |
| wrong | business | blend70 | 1 | d2 | category | amount | 0.6811 | no |
| wrong | business | blend70 | 1 | d6 | category | quantity | 0.7243 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9952 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.5603 | no |
| wrong | business | blend70 | 1 | department | org | account | 0.9968 | no |
| wrong | business | blend70 | 1 | description | account | text | 0.8515 | no |
| wrong | business | blend70 | 1 | merchant details | text | category | 0.9150 | no |
| wrong | business | blend70 | 1 | mois calendrier | date | category | 0.6632 | no |
| wrong | business | blend70 | 1 | portefeuille_nom_et_code | org | account | 0.9674 | no |
| wrong | business | blend70 | 1 | publisher label | org | address | 0.6649 | no |
| wrong | business | blend70 | 1 | purposeofexpenditure | text | account | 0.7109 | no |
| wrong | business | blend70 | 1 | q2a | category | quantity | 0.7035 | no |
| wrong | business | blend70 | 1 | q3_1 | category | quantity | 0.7024 | no |
| wrong | business | blend70 | 1 | q3_2 | category | quantity | 0.7005 | no |
| wrong | business | blend70 | 1 | q5a | category | quantity | 0.6963 | no |
| wrong | business | blend70 | 1 | q5b | category | quantity | 0.6738 | no |
| wrong | business | blend70 | 1 | q6 | category | quantity | 0.7062 | no |
| wrong | business | blend70 | 1 | q7 | category | quantity | 0.7229 | no |
| wrong | business | blend70 | 1 | q8 | category | quantity | 0.7160 | no |
| wrong | business | blend70 | 1 | regrp_sommaire | account | category | 0.7333 | no |
| wrong | business | blend70 | 1 | title | category | account | 0.7074 | no |
| critical | business | blend70 | 2 | overseas sourced goods | amount | quantity | 0.6179 | yes |
| unknown | business | blend70 | 2 | australian sourced goods | amount | unknown | 0.4980 | no |
| unknown | business | blend70 | 2 | australian sourced services | amount | unknown | 0.4770 | no |
| unknown | business | blend70 | 2 | commodity-title_en | product | unknown | 0.3373 | no |
| unknown | business | blend70 | 2 | financial year 2017/18 | date | unknown | 0.9987 | no |
| unknown | business | blend70 | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9684 | no |
| unknown | business | blend70 | 2 | overseas sourced services | amount | unknown | 0.4590 | no |
| unknown | business | blend70 | 2 | quarter | date | unknown | 0.9975 | no |
| unknown | business | blend70 | 2 | quarterno | date | unknown | 0.9926 | no |
| unknown | business | blend70 | 2 | segment-title_fr | category | unknown | 0.4882 | no |
| unknown | business | blend70 | 2 | 目名 | category | unknown | 0.9927 | no |
| unknown | business | blend70 | 2 | 科名 | category | unknown | 0.9528 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.7083 | no |
| wrong | business | blend70 | 2 | account_name | account | org | 0.7412 | no |
| wrong | business | blend70 | 2 | d1 | category | quantity | 0.6895 | no |
| wrong | business | blend70 | 2 | d2 | category | quantity | 0.6630 | no |
| wrong | business | blend70 | 2 | d6 | category | quantity | 0.7447 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9947 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.7238 | no |
| wrong | business | blend70 | 2 | department | org | account | 0.9963 | no |
| wrong | business | blend70 | 2 | description | account | text | 0.8539 | no |
| wrong | business | blend70 | 2 | entitiy | org | category | 0.5368 | no |
| wrong | business | blend70 | 2 | merchant details | text | category | 0.9287 | no |
| wrong | business | blend70 | 2 | mois calendrier | date | category | 0.5247 | no |
| wrong | business | blend70 | 2 | procurementclassification:proclasslabel | account | category | 0.6366 | no |
| wrong | business | blend70 | 2 | publisher label | org | address | 0.7176 | no |
| wrong | business | blend70 | 2 | purposeofexpenditure | text | account | 0.6598 | no |
| wrong | business | blend70 | 2 | q2a | category | quantity | 0.7060 | no |
| wrong | business | blend70 | 2 | q3_1 | category | quantity | 0.7030 | no |
| wrong | business | blend70 | 2 | q3_2 | category | quantity | 0.7028 | no |
| wrong | business | blend70 | 2 | q5a | category | quantity | 0.6978 | no |
| wrong | business | blend70 | 2 | q5b | category | quantity | 0.7038 | no |
| wrong | business | blend70 | 2 | q6 | category | quantity | 0.7096 | no |
| wrong | business | blend70 | 2 | q7 | category | quantity | 0.7241 | no |
| wrong | business | blend70 | 2 | q8 | category | quantity | 0.7212 | no |
| wrong | business | blend70 | 2 | regrp_sommaire | account | tax_class | 0.6391 | no |
| wrong | business | blend70 | 2 | title | category | account | 0.5476 | no |
| critical | business | ft | 1 | australian sourced goods | amount | quantity | 0.9900 | yes |
| critical | business | ft | 1 | overseas sourced goods | amount | quantity | 0.9901 | yes |
| critical | business | ft | 1 | overseas sourced services | amount | quantity | 0.7225 | yes |
| critical | business | ft | 1 | respnum$ | id | amount | 0.9645 | yes |
| critical | business | ft | 1 | total invoices paid | quantity | amount | 0.9988 | yes |
| unknown | business | ft | 1 | agebann | category | unknown | 0.3831 | no |
| unknown | business | ft | 1 | financial year 2017/18 | date | unknown | 0.9993 | no |
| unknown | business | ft | 1 | financial year 2021 to 2022 - voa | date | unknown | 0.9986 | no |
| unknown | business | ft | 1 | quarter | date | unknown | 0.9991 | no |
| unknown | business | ft | 1 | quarterno | date | unknown | 0.9993 | no |
| unknown | business | ft | 1 | segment-title_en | category | unknown | 0.4821 | no |
| unknown | business | ft | 1 | 目名 | category | unknown | 0.9986 | no |
| unknown | business | ft | 1 | 科名 | category | unknown | 0.9926 | no |
| wrong | business | ft | 1 | d1 | category | quantity | 0.9945 | no |
| wrong | business | ft | 1 | d2 | category | amount | 0.9730 | no |
| wrong | business | ft | 1 | d6 | category | quantity | 0.9611 | no |
| wrong | business | ft | 1 | department | org | account | 0.9989 | no |
| wrong | business | ft | 1 | department | org | account | 0.5318 | no |
| wrong | business | ft | 1 | department | org | account | 0.9990 | no |
| wrong | business | ft | 1 | description | account | text | 0.9922 | no |
| wrong | business | ft | 1 | entitiy | org | account | 0.5198 | no |
| wrong | business | ft | 1 | merchant details | text | category | 0.9798 | no |
| wrong | business | ft | 1 | mois calendrier | date | category | 0.9292 | no |
| wrong | business | ft | 1 | portefeuille_nom_et_code | org | account | 0.9647 | no |
| wrong | business | ft | 1 | publisher label | org | address | 0.9229 | no |
| wrong | business | ft | 1 | purposeofexpenditure | text | account | 0.6090 | no |
| wrong | business | ft | 1 | q2a | category | quantity | 0.9940 | no |
| wrong | business | ft | 1 | q3_1 | category | quantity | 0.9950 | no |
| wrong | business | ft | 1 | q3_2 | category | quantity | 0.9927 | no |
| wrong | business | ft | 1 | q5a | category | quantity | 0.9898 | no |
| wrong | business | ft | 1 | q5b | category | quantity | 0.9541 | no |
| wrong | business | ft | 1 | q6 | category | quantity | 0.9936 | no |
| wrong | business | ft | 1 | q7 | category | quantity | 0.9969 | no |
| wrong | business | ft | 1 | q8 | category | quantity | 0.9912 | no |
| wrong | business | ft | 1 | regrp_sommaire | account | category | 0.9750 | no |
| wrong | business | ft | 1 | title | category | account | 0.9903 | no |
| critical | business | ft | 2 | australian sourced goods | amount | quantity | 0.7114 | yes |
| critical | business | ft | 2 | overseas sourced goods | amount | quantity | 0.8827 | yes |
| unknown | business | ft | 2 | commodity-title_en | product | unknown | 0.4785 | no |
| unknown | business | ft | 2 | financial year 2017/18 | date | unknown | 0.9993 | no |
| unknown | business | ft | 2 | financial year 2021 to 2022 - voa | date | unknown | 0.9987 | no |
| unknown | business | ft | 2 | quarter | date | unknown | 0.9992 | no |
| unknown | business | ft | 2 | quarterno | date | unknown | 0.9990 | no |
| unknown | business | ft | 2 | 目名 | category | unknown | 0.9984 | no |
| unknown | business | ft | 2 | 科名 | category | unknown | 0.9974 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.9838 | no |
| wrong | business | ft | 2 | account_name | account | org | 0.9874 | no |
| wrong | business | ft | 2 | australian sourced services | amount | address | 0.6653 | no |
| wrong | business | ft | 2 | d1 | category | quantity | 0.9797 | no |
| wrong | business | ft | 2 | d2 | category | quantity | 0.9031 | no |
| wrong | business | ft | 2 | d6 | category | quantity | 0.9902 | no |
| wrong | business | ft | 2 | department | org | account | 0.9982 | no |
| wrong | business | ft | 2 | department | org | account | 0.7654 | no |
| wrong | business | ft | 2 | department | org | account | 0.9983 | no |
| wrong | business | ft | 2 | description | account | text | 0.9957 | no |
| wrong | business | ft | 2 | entitiy | org | category | 0.6661 | no |
| wrong | business | ft | 2 | merchant details | text | category | 0.9993 | no |
| wrong | business | ft | 2 | mois calendrier | date | category | 0.7314 | no |
| wrong | business | ft | 2 | overseas sourced services | amount | address | 0.5270 | no |
| wrong | business | ft | 2 | procurementclassification:proclasslabel | account | category | 0.8543 | no |
| wrong | business | ft | 2 | publisher label | org | address | 0.9981 | no |
| wrong | business | ft | 2 | purposeofexpenditure | text | account | 0.5360 | no |
| wrong | business | ft | 2 | q2a | category | quantity | 0.9976 | no |
| wrong | business | ft | 2 | q3_1 | category | quantity | 0.9959 | no |
| wrong | business | ft | 2 | q3_2 | category | quantity | 0.9961 | no |
| wrong | business | ft | 2 | q5a | category | quantity | 0.9920 | no |
| wrong | business | ft | 2 | q5b | category | quantity | 0.9969 | no |
| wrong | business | ft | 2 | q6 | category | quantity | 0.9985 | no |
| wrong | business | ft | 2 | q7 | category | quantity | 0.9986 | no |
| wrong | business | ft | 2 | q8 | category | quantity | 0.9986 | no |
| wrong | business | ft | 2 | regrp_sommaire | account | tax_class | 0.9129 | no |
| wrong | business | ft | 2 | segment-title_fr | category | account | 0.6331 | no |
| wrong | business | ft | 2 | title | category | account | 0.7621 | no |
| critical | business2 | blend70 | 1 | fine | amount | quantity | 0.7301 | yes |
| critical | business2 | blend70 | 1 | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | blend70 | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8503 | yes |
| critical | business2 | blend70 | 1 | total invoices paid | quantity | amount | 0.9978 | yes |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.6602 | no |
| other_ng | business2 | blend70 | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.7073 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace gains sqm | other | quantity | 0.9404 | no |
| other_ng | business2 | blend70 | 1 | a2 floorspace losses sqm | other | quantity | 0.7615 | no |
| other_ng | business2 | blend70 | 1 | average bids per property | other | rate | 0.9540 | no |
| other_ng | business2 | blend70 | 1 | b1a floorspace gains sqm | other | quantity | 0.6002 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace gains sqm | other | quantity | 0.7378 | no |
| other_ng | business2 | blend70 | 1 | d2 floorspace net sqm | other | quantity | 0.6636 | no |
| other_ng | business2 | blend70 | 1 | energy_consumption | other | amount | 0.6987 | no |
| unknown | business2 | blend70 | 1 | amt-units_mnt-unite | category | unknown | 0.6244 | no |
| unknown | business2 | blend70 | 1 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend70 | 1 | fuel_poverty | rate | unknown | 0.9748 | no |
| unknown | business2 | blend70 | 1 | habitatdescription | text | unknown | 0.5281 | no |
| unknown | business2 | blend70 | 1 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 1 | scheme_description | category | unknown | 0.4602 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9983 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 1 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 1 | value () | amount | unknown | 0.9994 | no |
| unknown | business2 | blend70 | 1 | volume (10^3 m3) | quantity | unknown | 0.9945 | no |
| unknown | business2 | blend70 | 1 | volume (mcf) | quantity | unknown | 0.9977 | no |
| unknown | business2 | blend70 | 1 | 販売 | date | unknown | 0.9902 | no |
| wrong | business2 | blend70 | 1 | bike_stands | quantity | category | 0.8911 | no |
| wrong | business2 | blend70 | 1 | construction_age_band | category | date | 0.6099 | no |
| wrong | business2 | blend70 | 1 | imd19_income_decile | category | amount | 0.6983 | no |
| wrong | business2 | blend70 | 1 | loac_group | category | address | 0.6974 | no |
| wrong | business2 | blend70 | 1 | monitor | id | category | 0.6164 | no |
| wrong | business2 | blend70 | 1 | name | org | address | 0.6659 | no |
| wrong | business2 | blend70 | 1 | number_habitable_rooms | quantity | category | 0.9855 | no |
| wrong | business2 | blend70 | 1 | programme | category | account | 0.6852 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7601 | no |
| wrong | business2 | blend70 | 1 | projection | category | id | 0.7395 | no |
| wrong | business2 | blend70 | 1 | scheme | id | category | 0.8840 | no |
| wrong | business2 | blend70 | 1 | service | account | address | 0.5911 | no |
| wrong | business2 | blend70 | 1 | service_responsable | account | category | 0.8751 | no |
| wrong | business2 | blend70 | 1 | situtation | address | category | 0.8408 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6884 | no |
| wrong | business2 | blend70 | 1 | terrace | quantity | address | 0.6679 | no |
| wrong | business2 | blend70 | 1 | type | account | category | 0.9672 | no |
| critical | business2 | blend70 | 2 | fine | amount | quantity | 0.6922 | yes |
| critical | business2 | blend70 | 2 | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | blend70 | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.8471 | yes |
| other_ng | business2 | blend70 | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.6983 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace gains sqm | other | quantity | 0.9422 | no |
| other_ng | business2 | blend70 | 2 | a2 floorspace losses sqm | other | quantity | 0.7609 | no |
| other_ng | business2 | blend70 | 2 | average bids per property | other | rate | 0.8964 | no |
| other_ng | business2 | blend70 | 2 | b1a floorspace gains sqm | other | quantity | 0.6194 | no |
| other_ng | business2 | blend70 | 2 | d2 floorspace gains sqm | other | quantity | 0.7486 | no |
| other_ng | business2 | blend70 | 2 | epc_score | other | quantity | 0.5184 | no |
| other_ng | business2 | blend70 | 2 | loc_y | other | address | 0.8169 | no |
| other_ng | business2 | blend70 | 2 | potential_epc_score | other | quantity | 0.5808 | no |
| unknown | business2 | blend70 | 2 | amt-units_mnt-unite | category | unknown | 0.4515 | no |
| unknown | business2 | blend70 | 2 | construction_age_band | category | unknown | 0.4873 | no |
| unknown | business2 | blend70 | 2 | date | date | unknown | 0.9996 | no |
| unknown | business2 | blend70 | 2 | fuel_poverty | rate | unknown | 0.9744 | no |
| unknown | business2 | blend70 | 2 | montant | amount | unknown | 0.9985 | no |
| unknown | business2 | blend70 | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9980 | no |
| unknown | business2 | blend70 | 2 | potential_epc_rating_known | category | unknown | 0.4766 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.6798 | no |
| unknown | business2 | blend70 | 2 | projection | category | unknown | 0.6718 | no |
| unknown | business2 | blend70 | 2 | terminal | address | unknown | 0.3521 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9982 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9987 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9984 | no |
| unknown | business2 | blend70 | 2 | tlist(q1) | date | unknown | 0.9968 | no |
| unknown | business2 | blend70 | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | blend70 | 2 | volume (10^3 m3) | quantity | unknown | 0.9952 | no |
| unknown | business2 | blend70 | 2 | volume (mcf) | quantity | unknown | 0.9988 | no |
| unknown | business2 | blend70 | 2 | 販売 | date | unknown | 0.9902 | no |
| wrong | business2 | blend70 | 2 | account name | account | org | 0.6875 | no |
| wrong | business2 | blend70 | 2 | bike_stands | quantity | category | 0.8467 | no |
| wrong | business2 | blend70 | 2 | epc_score_known | category | quantity | 0.5536 | no |
| wrong | business2 | blend70 | 2 | imd19_income_decile | category | amount | 0.6898 | no |
| wrong | business2 | blend70 | 2 | loac_group | category | address | 0.6836 | no |
| wrong | business2 | blend70 | 2 | merchant description | category | org | 0.6911 | no |
| wrong | business2 | blend70 | 2 | monitor | id | category | 0.7528 | no |
| wrong | business2 | blend70 | 2 | name | org | address | 0.8981 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms | quantity | category | 0.9549 | no |
| wrong | business2 | blend70 | 2 | number_habitable_rooms_known | category | quantity | 0.6915 | no |
| wrong | business2 | blend70 | 2 | scheme | id | category | 0.9726 | no |
| wrong | business2 | blend70 | 2 | service | account | org | 0.6839 | no |
| wrong | business2 | blend70 | 2 | situtation | address | category | 0.6893 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.9208 | no |
| wrong | business2 | blend70 | 2 | surveyname | text | org | 0.8648 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6835 | no |
| wrong | business2 | blend70 | 2 | terrace | quantity | address | 0.6917 | no |
| wrong | business2 | blend70 | 2 | total_floor_area_known | category | quantity | 0.6703 | no |
| wrong | business2 | blend70 | 2 | type | account | category | 0.9671 | no |
| wrong | business2 | blend70 | 2 | type of expenditure | account | category | 0.7358 | no |
| wrong | business2 | blend70 | 2 | want to live in this parish only | quantity | category | 0.6363 | no |
| critical | business2 | ft | 1 | fine | amount | quantity | 0.9991 | yes |
| critical | business2 | ft | 1 | miscellaneous_divers | amount | quantity | 0.9992 | yes |
| critical | business2 | ft | 1 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9972 | yes |
| critical | business2 | ft | 1 | total invoices paid | quantity | amount | 0.9989 | yes |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace gains sqm | other | quantity | 0.8981 | no |
| other_ng | business2 | ft | 1 | a1 (retail) floorspace losses sqm | other | quantity | 0.9550 | no |
| other_ng | business2 | ft | 1 | a2 floorspace gains sqm | other | quantity | 0.9940 | no |
| other_ng | business2 | ft | 1 | a2 floorspace losses sqm | other | quantity | 0.9946 | no |
| other_ng | business2 | ft | 1 | a2 floorspace net sqm | other | quantity | 0.5994 | no |
| other_ng | business2 | ft | 1 | average bids per property | other | rate | 0.9954 | no |
| other_ng | business2 | ft | 1 | b1a floorspace gains sqm | other | quantity | 0.8140 | no |
| other_ng | business2 | ft | 1 | b1a floorspace losses sqm | other | quantity | 0.5047 | no |
| other_ng | business2 | ft | 1 | d2 floorspace gains sqm | other | quantity | 0.9759 | no |
| other_ng | business2 | ft | 1 | d2 floorspace losses sqm | other | quantity | 0.5605 | no |
| other_ng | business2 | ft | 1 | d2 floorspace net sqm | other | quantity | 0.9463 | no |
| other_ng | business2 | ft | 1 | energy_consumption | other | amount | 0.9945 | no |
| unknown | business2 | ft | 1 | amt-units_mnt-unite | category | unknown | 0.8685 | no |
| unknown | business2 | ft | 1 | date | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | fuel_poverty | rate | unknown | 0.9921 | no |
| unknown | business2 | ft | 1 | habitatdescription | text | unknown | 0.7544 | no |
| unknown | business2 | ft | 1 | montant | amount | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 1 | scheme_description | category | unknown | 0.4519 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 1 | value () | amount | unknown | 0.9993 | no |
| unknown | business2 | ft | 1 | volume (10^3 m3) | quantity | unknown | 0.9978 | no |
| unknown | business2 | ft | 1 | volume (mcf) | quantity | unknown | 0.9973 | no |
| unknown | business2 | ft | 1 | 販売 | date | unknown | 0.9990 | no |
| wrong | business2 | ft | 1 | bike_stands | quantity | category | 0.9977 | no |
| wrong | business2 | ft | 1 | construction_age_band | category | date | 0.8494 | no |
| wrong | business2 | ft | 1 | imd19_income_decile | category | amount | 0.9976 | no |
| wrong | business2 | ft | 1 | loac_group | category | address | 0.9962 | no |
| wrong | business2 | ft | 1 | monitor | id | category | 0.7558 | no |
| wrong | business2 | ft | 1 | name | org | address | 0.6609 | no |
| wrong | business2 | ft | 1 | number_habitable_rooms | quantity | category | 0.9939 | no |
| wrong | business2 | ft | 1 | programme | category | account | 0.9786 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9985 | no |
| wrong | business2 | ft | 1 | projection | category | id | 0.9986 | no |
| wrong | business2 | ft | 1 | scheme | id | category | 0.8565 | no |
| wrong | business2 | ft | 1 | service | account | address | 0.8437 | no |
| wrong | business2 | ft | 1 | service_responsable | account | category | 0.9526 | no |
| wrong | business2 | ft | 1 | situtation | address | category | 0.9207 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9829 | no |
| wrong | business2 | ft | 1 | terrace | quantity | address | 0.9539 | no |
| wrong | business2 | ft | 1 | type | account | category | 0.9994 | no |
| critical | business2 | ft | 2 | fine | amount | quantity | 0.9450 | yes |
| critical | business2 | ft | 2 | miscellaneous_divers | amount | quantity | 0.9992 | yes |
| critical | business2 | ft | 2 | sales-goods-svcs_ventes-biens-srvs | amount | quantity | 0.9928 | yes |
| other_ng | business2 | ft | 2 | a1 (retail) floorspace gains sqm | other | quantity | 0.9526 | no |
| other_ng | business2 | ft | 2 | a2 floorspace gains sqm | other | quantity | 0.9965 | no |
| other_ng | business2 | ft | 2 | a2 floorspace losses sqm | other | quantity | 0.9937 | no |
| other_ng | business2 | ft | 2 | average bids per property | other | rate | 0.9130 | no |
| other_ng | business2 | ft | 2 | b1a floorspace gains sqm | other | quantity | 0.8415 | no |
| other_ng | business2 | ft | 2 | d2 floorspace gains sqm | other | quantity | 0.9913 | no |
| other_ng | business2 | ft | 2 | energy_consumption | other | amount | 0.5872 | no |
| other_ng | business2 | ft | 2 | epc_score | other | quantity | 0.7077 | no |
| other_ng | business2 | ft | 2 | loc_y | other | address | 0.9654 | no |
| other_ng | business2 | ft | 2 | potential_epc_score | other | quantity | 0.8057 | no |
| unknown | business2 | ft | 2 | date | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | fuel_poverty | rate | unknown | 0.9914 | no |
| unknown | business2 | ft | 2 | montant | amount | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | percentage (%) of the total amount paid | rate | unknown | 0.9981 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.9712 | no |
| unknown | business2 | ft | 2 | projection | category | unknown | 0.9597 | no |
| unknown | business2 | ft | 2 | terminal | address | unknown | 0.4911 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9993 | no |
| unknown | business2 | ft | 2 | tlist(q1) | date | unknown | 0.9994 | no |
| unknown | business2 | ft | 2 | value () | amount | unknown | 0.9995 | no |
| unknown | business2 | ft | 2 | volume (10^3 m3) | quantity | unknown | 0.9987 | no |
| unknown | business2 | ft | 2 | volume (mcf) | quantity | unknown | 0.9989 | no |
| unknown | business2 | ft | 2 | 販売 | date | unknown | 0.9990 | no |
| wrong | business2 | ft | 2 | account name | account | org | 0.9819 | no |
| wrong | business2 | ft | 2 | amt-units_mnt-unite | category | tax_class | 0.6451 | no |
| wrong | business2 | ft | 2 | bike_stands | quantity | category | 0.9343 | no |
| wrong | business2 | ft | 2 | epc_score_known | category | quantity | 0.7506 | no |
| wrong | business2 | ft | 2 | imd19_income_decile | category | amount | 0.9853 | no |
| wrong | business2 | ft | 2 | loac_group | category | address | 0.9766 | no |
| wrong | business2 | ft | 2 | merchant description | category | org | 0.9384 | no |
| wrong | business2 | ft | 2 | monitor | id | category | 0.9507 | no |
| wrong | business2 | ft | 2 | name | org | address | 0.9926 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms | quantity | category | 0.9503 | no |
| wrong | business2 | ft | 2 | number_habitable_rooms_known | category | quantity | 0.9785 | no |
| wrong | business2 | ft | 2 | potential_epc_rating_known | category | quantity | 0.5573 | no |
| wrong | business2 | ft | 2 | scheme | id | category | 0.9831 | no |
| wrong | business2 | ft | 2 | service | account | org | 0.9753 | no |
| wrong | business2 | ft | 2 | situtation | address | category | 0.7042 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9976 | no |
| wrong | business2 | ft | 2 | surveyname | text | org | 0.9034 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9759 | no |
| wrong | business2 | ft | 2 | terrace | quantity | address | 0.9879 | no |
| wrong | business2 | ft | 2 | total_floor_area_known | category | quantity | 0.9046 | no |
| wrong | business2 | ft | 2 | type | account | category | 0.9992 | no |
| wrong | business2 | ft | 2 | type of expenditure | account | category | 0.7989 | no |
| wrong | business2 | ft | 2 | want to live in this parish only | quantity | category | 0.9015 | no |
| critical | dev220 | blend70 | 1 | purchase order by customer | id | quantity | 0.9386 | yes |
| wrong | dev220 | blend70 | 1 | customer rank | quantity | category | 0.9538 | no |
| wrong | dev220 | blend70 | 1 | supplier rank | quantity | category | 0.7574 | no |
| wrong | dev220 | blend70 | 1 | terms | category | text | 0.8958 | no |
| wrong | dev220 | blend70 | 1 | 担当課 | org | account | 0.7179 | no |
| wrong | dev220 | blend70 | 1 | 支払者の氏名又は名称 | org | person | 0.5515 | no |
| critical | dev220 | blend70 | 2 | purchase order by customer | id | quantity | 0.9337 | yes |
| unknown | dev220 | blend70 | 2 | 支払を受ける者の個人番号 | id | unknown | 0.5093 | no |
| wrong | dev220 | blend70 | 2 | customer rank | quantity | category | 0.8419 | no |
| wrong | dev220 | blend70 | 2 | supplier rank | quantity | category | 0.7494 | no |
| wrong | dev220 | blend70 | 2 | taxable | category | tax_class | 0.9904 | no |
| wrong | dev220 | blend70 | 2 | terms | category | text | 0.5373 | no |
| wrong | dev220 | blend70 | 2 | 担当課 | org | account | 0.5800 | no |
| wrong | dev220 | blend70 | 2 | 税率 | rate | tax_class | 0.5291 | no |
| critical | dev220 | ft | 1 | purchase order by customer | id | quantity | 0.9987 | yes |
| wrong | dev220 | ft | 1 | customer rank | quantity | category | 0.9923 | no |
| wrong | dev220 | ft | 1 | location | org | address | 0.6852 | no |
| wrong | dev220 | ft | 1 | supplier rank | quantity | category | 0.9982 | no |
| wrong | dev220 | ft | 1 | terms | category | text | 0.9568 | no |
| wrong | dev220 | ft | 1 | 担当課 | org | account | 0.9819 | no |
| wrong | dev220 | ft | 1 | 支払者の氏名又は名称 | org | person | 0.7793 | no |
| critical | dev220 | ft | 2 | purchase order by customer | id | quantity | 0.9916 | yes |
| unknown | dev220 | ft | 2 | 支払を受ける者の個人番号 | id | unknown | 0.7191 | no |
| wrong | dev220 | ft | 2 | customer rank | quantity | category | 0.8326 | no |
| wrong | dev220 | ft | 2 | supplier rank | quantity | category | 0.9867 | no |
| wrong | dev220 | ft | 2 | taxable | category | tax_class | 0.9925 | no |
| wrong | dev220 | ft | 2 | 担当課 | org | account | 0.7847 | no |
| wrong | dev220 | ft | 2 | 税率 | rate | tax_class | 0.7454 | no |
| other_ng | general | blend70 | 1 | dag-stage | other | quantity | 0.6351 | no |
| other_ng | general | blend70 | 1 | dbpedia_score | other | rate | 0.7718 | no |
| other_ng | general | blend70 | 1 | episode | other | quantity | 0.6990 | no |
| other_ng | general | blend70 | 1 | mt2 | other | quantity | 0.9591 | no |
| other_ng | general | blend70 | 1 | value | other | rate | 0.6300 | no |
| other_ng | general | blend70 | 1 | 五島 | other | quantity | 0.9962 | no |
| unknown | general | blend70 | 1 | 1日最大給水量(m3) | quantity | unknown | 0.8913 | no |
| unknown | general | blend70 | 1 | age_q1_nd | quantity | unknown | 0.4130 | no |
| unknown | general | blend70 | 1 | age_q3 | quantity | unknown | 0.4761 | no |
| unknown | general | blend70 | 1 | age_q3_nd | quantity | unknown | 0.3883 | no |
| unknown | general | blend70 | 1 | denominatorunweighted | quantity | unknown | 0.8589 | no |
| unknown | general | blend70 | 1 | denominatorweighted | quantity | unknown | 0.9496 | no |
| unknown | general | blend70 | 1 | goal | id | unknown | 0.4995 | no |
| unknown | general | blend70 | 1 | image_level_adj_acc | rate | unknown | 0.9882 | no |
| unknown | general | blend70 | 1 | property | category | unknown | 0.6995 | no |
| unknown | general | blend70 | 1 | sens_final | rate | unknown | 0.5997 | no |
| unknown | general | blend70 | 1 | source_value | category | unknown | 0.6288 | no |
| unknown | general | blend70 | 1 | 住家全壊 | quantity | unknown | 0.4521 | no |
| unknown | general | blend70 | 1 | 発生日 | date | unknown | 0.9657 | no |
| unknown | general | blend70 | 1 | 登録年月日 | date | unknown | 0.9995 | no |
| unknown | general | blend70 | 1 | 科名 | category | unknown | 0.9711 | no |
| unknown | general | blend70 | 1 | 読み方 | address | unknown | 0.3090 | no |
| wrong | general | blend70 | 1 | cleaned | text | account | 0.6632 | no |
| wrong | general | blend70 | 1 | keyword | category | text | 0.9491 | no |
| wrong | general | blend70 | 1 | organization name | org | person | 0.5036 | no |
| wrong | general | blend70 | 1 | place | org | address | 0.7441 | no |
| wrong | general | blend70 | 1 | term | text | category | 0.5588 | no |
| wrong | general | blend70 | 1 | year_step_size | quantity | category | 0.9594 | no |
| wrong | general | blend70 | 1 | 発生県 | id | address | 0.7109 | no |
| critical | general | blend70 | 2 | goal | id | quantity | 0.7060 | yes |
| other_ng | general | blend70 | 2 | dag-stage | other | category | 0.9436 | no |
| other_ng | general | blend70 | 2 | episode | other | quantity | 0.6014 | no |
| other_ng | general | blend70 | 2 | mt2 | other | quantity | 0.9727 | no |
| other_ng | general | blend70 | 2 | operationid | other | id | 0.6677 | no |
| other_ng | general | blend70 | 2 | 五島 | other | quantity | 0.9971 | no |
| unknown | general | blend70 | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7060 | no |
| unknown | general | blend70 | 2 | app | category | unknown | 0.6106 | no |
| unknown | general | blend70 | 2 | denominatorunweighted | quantity | unknown | 0.8482 | no |
| unknown | general | blend70 | 2 | denominatorweighted | quantity | unknown | 0.9497 | no |
| unknown | general | blend70 | 2 | doi | id | unknown | 0.5431 | no |
| unknown | general | blend70 | 2 | funding | amount | unknown | 0.5806 | no |
| unknown | general | blend70 | 2 | image_level_adj_acc | rate | unknown | 0.9880 | no |
| unknown | general | blend70 | 2 | property | category | unknown | 0.7147 | no |
| unknown | general | blend70 | 2 | raw | category | unknown | 0.3733 | no |
| unknown | general | blend70 | 2 | sens_final | rate | unknown | 0.7309 | no |
| unknown | general | blend70 | 2 | source_value | category | unknown | 0.6075 | no |
| unknown | general | blend70 | 2 | study | text | unknown | 0.4827 | no |
| unknown | general | blend70 | 2 | units | category | unknown | 0.6835 | no |
| unknown | general | blend70 | 2 | 住家全壊 | quantity | unknown | 0.3679 | no |
| unknown | general | blend70 | 2 | 発生日 | date | unknown | 0.9658 | no |
| unknown | general | blend70 | 2 | 登録年月日 | date | unknown | 0.9996 | no |
| unknown | general | blend70 | 2 | 科名 | category | unknown | 0.9754 | no |
| wrong | general | blend70 | 2 | cleaned | text | account | 0.6310 | no |
| wrong | general | blend70 | 2 | keyword | category | text | 0.9498 | no |
| wrong | general | blend70 | 2 | place | org | address | 0.7165 | no |
| wrong | general | blend70 | 2 | standardhours | quantity | category | 0.8644 | no |
| wrong | general | blend70 | 2 | year_step_size | quantity | category | 0.9615 | no |
| wrong | general | blend70 | 2 | 住家一部損壊 | quantity | category | 0.5397 | no |
| wrong | general | blend70 | 2 | 発生県 | id | address | 0.7098 | no |
| wrong | general | blend70 | 2 | 読み方 | address | org | 0.6581 | no |
| critical | general | ft | 1 | goal | id | quantity | 0.6961 | yes |
| other_ng | general | ft | 1 | dag-stage | other | quantity | 0.8481 | no |
| other_ng | general | ft | 1 | dbpedia_score | other | rate | 0.9862 | no |
| other_ng | general | ft | 1 | episode | other | quantity | 0.9934 | no |
| other_ng | general | ft | 1 | mt2 | other | quantity | 0.9661 | no |
| other_ng | general | ft | 1 | 五島 | other | quantity | 0.9966 | no |
| unknown | general | ft | 1 | 1日最大給水量(m3) | quantity | unknown | 0.9947 | no |
| unknown | general | ft | 1 | age_q1_nd | quantity | unknown | 0.4096 | no |
| unknown | general | ft | 1 | age_q3 | quantity | unknown | 0.4722 | no |
| unknown | general | ft | 1 | age_q3_nd | quantity | unknown | 0.5058 | no |
| unknown | general | ft | 1 | denominatorunweighted | quantity | unknown | 0.9986 | no |
| unknown | general | ft | 1 | denominatorweighted | quantity | unknown | 0.9989 | no |
| unknown | general | ft | 1 | image_level_adj_acc | rate | unknown | 0.9984 | no |
| unknown | general | ft | 1 | property | category | unknown | 0.9747 | no |
| unknown | general | ft | 1 | sens_final | rate | unknown | 0.7856 | no |
| unknown | general | ft | 1 | source_value | category | unknown | 0.8982 | no |
| unknown | general | ft | 1 | 発生日 | date | unknown | 0.9992 | no |
| unknown | general | ft | 1 | 登録年月日 | date | unknown | 0.9993 | no |
| unknown | general | ft | 1 | 科名 | category | unknown | 0.9918 | no |
| unknown | general | ft | 1 | 読み方 | address | unknown | 0.4399 | no |
| wrong | general | ft | 1 | cleaned | text | account | 0.9414 | no |
| wrong | general | ft | 1 | keyword | category | text | 0.9927 | no |
| wrong | general | ft | 1 | organization name | org | person | 0.7163 | no |
| wrong | general | ft | 1 | place | org | address | 0.9959 | no |
| wrong | general | ft | 1 | term | text | category | 0.7962 | no |
| wrong | general | ft | 1 | year_step_size | quantity | category | 0.9669 | no |
| wrong | general | ft | 1 | 住家全壊 | quantity | category | 0.6451 | no |
| wrong | general | ft | 1 | 発生県 | id | address | 0.9983 | no |
| critical | general | ft | 2 | funding | amount | id | 0.8157 | yes |
| critical | general | ft | 2 | goal | id | quantity | 0.9911 | yes |
| other_ng | general | ft | 2 | dag-stage | other | category | 0.9892 | no |
| other_ng | general | ft | 2 | episode | other | quantity | 0.8540 | no |
| other_ng | general | ft | 2 | mt2 | other | quantity | 0.9856 | no |
| other_ng | general | ft | 2 | operationid | other | id | 0.9476 | no |
| other_ng | general | ft | 2 | value | other | amount | 0.7402 | no |
| other_ng | general | ft | 2 | 五島 | other | quantity | 0.9977 | no |
| unknown | general | ft | 2 | 1日最大給水量(m3) | quantity | unknown | 0.7300 | no |
| unknown | general | ft | 2 | app | category | unknown | 0.8512 | no |
| unknown | general | ft | 2 | denominatorunweighted | quantity | unknown | 0.9833 | no |
| unknown | general | ft | 2 | denominatorweighted | quantity | unknown | 0.9991 | no |
| unknown | general | ft | 2 | doi | id | unknown | 0.7667 | no |
| unknown | general | ft | 2 | image_level_adj_acc | rate | unknown | 0.9980 | no |
| unknown | general | ft | 2 | property | category | unknown | 0.9965 | no |
| unknown | general | ft | 2 | sens_final | rate | unknown | 0.9730 | no |
| unknown | general | ft | 2 | source_value | category | unknown | 0.8677 | no |
| unknown | general | ft | 2 | study | text | unknown | 0.5723 | no |
| unknown | general | ft | 2 | units | category | unknown | 0.9756 | no |
| unknown | general | ft | 2 | 発生日 | date | unknown | 0.9993 | no |
| unknown | general | ft | 2 | 登録年月日 | date | unknown | 0.9994 | no |
| unknown | general | ft | 2 | 科名 | category | unknown | 0.9979 | no |
| wrong | general | ft | 2 | cleaned | text | account | 0.8956 | no |
| wrong | general | ft | 2 | keyword | category | text | 0.9937 | no |
| wrong | general | ft | 2 | place | org | address | 0.9566 | no |
| wrong | general | ft | 2 | standardhours | quantity | category | 0.9952 | no |
| wrong | general | ft | 2 | year_step_size | quantity | category | 0.9700 | no |
| wrong | general | ft | 2 | 住家全壊 | quantity | category | 0.5248 | no |
| wrong | general | ft | 2 | 発生県 | id | address | 0.9967 | no |
| wrong | general | ft | 2 | 読み方 | address | org | 0.7403 | no |
| unknown | japan_procurement | blend70 | 1 | 入札時期 (予定) | date | unknown | 0.9970 | no |
| unknown | japan_procurement | blend70 | 2 | 入札時期 (予定) | date | unknown | 0.9972 | no |
| unknown | japan_procurement | ft | 1 | 入札時期 (予定) | date | unknown | 0.9992 | no |
| unknown | japan_procurement | ft | 2 | 入札時期 (予定) | date | unknown | 0.9994 | no |

### unknown の判定理由

- date_value_evidence_low: 56件
- numeric_top2_too_close: 2件
- numeric_values_not_parseable: 14件
- other_class: 67件
- probability_below_threshold: 29件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 35件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 147件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 109件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
