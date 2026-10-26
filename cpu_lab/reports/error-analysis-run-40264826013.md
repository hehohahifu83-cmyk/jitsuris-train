# ジツリス失敗分析（観測と仮説を分離）

生成日時 (UTC): 2026-10-26T04:12:47+00:00
使用ファイル数: 20 / 行数: 8644
対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。

## 観測結果

| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |
|---|---|---:|---:|---:|---:|---:|---:|
| business | blend50 | t | 490 | 8 | 1 | 14 | 0 |
| business | blend60 | t | 490 | 10 | 1 | 10 | 0 |
| business | blend70 | t | 490 | 10 | 1 | 7 | 0 |
| business | ft | t | 490 | 9 | 0 | 7 | 0 |
| business2 | blend50 | t | 976 | 12 | 2 | 27 | 2 |
| business2 | blend60 | t | 976 | 14 | 2 | 19 | 1 |
| business2 | blend70 | t | 976 | 14 | 3 | 16 | 0 |
| business2 | ft | t | 976 | 16 | 2 | 17 | 0 |
| dev220 | blend50 | t | 220 | 6 | 2 | 11 | 0 |
| dev220 | blend60 | t | 220 | 6 | 2 | 0 | 0 |
| dev220 | blend70 | t | 220 | 6 | 2 | 0 | 0 |
| dev220 | ft | t | 220 | 6 | 2 | 1 | 0 |
| general | blend50 | t | 383 | 9 | 1 | 10 | 6 |
| general | blend60 | t | 383 | 9 | 1 | 12 | 6 |
| general | blend70 | t | 383 | 10 | 1 | 13 | 6 |
| general | ft | t | 383 | 11 | 1 | 13 | 7 |
| japan_procurement | blend50 | t | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | t | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | t | 92 | 0 | 0 | 0 | 0 |
| japan_procurement | ft | t | 92 | 0 | 0 | 0 | 0 |

### 取り違えの頻度

- business / blend50: org→account: 4, quantity→amount: 1, text→category: 1, text→account: 1, category→text: 1
- business / blend60: org→account: 5, quantity→amount: 1, text→category: 1, text→account: 1, category→id: 1, category→text: 1
- business / blend70: org→account: 5, quantity→amount: 1, text→category: 1, text→account: 1, category→id: 1, category→text: 1
- business / ft: org→account: 5, text→category: 1, account→text: 1, text→account: 1, category→id: 1
- business2 / blend50: account→category: 2, address→category: 2, id→category: 1, quantity→amount: 1, category→date: 1, quantity→category: 1, category→quantity: 1, org→address: 1
- business2 / blend60: account→category: 2, address→category: 2, id→category: 1, quantity→amount: 1, amount→category: 1, category→date: 1, quantity→category: 1, category→quantity: 1
- business2 / blend70: account→category: 2, quantity→amount: 2, address→category: 2, id→category: 1, amount→category: 1, category→date: 1, quantity→category: 1, category→quantity: 1
- business2 / ft: account→org: 2, account→category: 2, address→category: 2, id→category: 1, amount→category: 1, category→date: 1, quantity→category: 1, category→quantity: 1
- dev220 / blend50: quantity→category: 2, text→category: 1, org→account: 1, id→quantity: 1, amount→quantity: 1
- dev220 / blend60: quantity→category: 2, org→account: 1, text→category: 1, id→quantity: 1, amount→quantity: 1
- dev220 / blend70: quantity→category: 2, org→account: 1, text→category: 1, id→quantity: 1, amount→quantity: 1
- dev220 / ft: quantity→category: 2, org→account: 1, text→category: 1, id→quantity: 1, amount→quantity: 1
- general / blend50: org→address: 2, text→category: 2, person→org: 1, category→text: 1, quantity→category: 1, id→quantity: 1, id→category: 1
- general / blend60: category→text: 2, org→address: 2, person→org: 1, quantity→category: 1, id→quantity: 1, id→category: 1, text→category: 1
- general / blend70: category→text: 3, org→address: 2, person→org: 1, quantity→category: 1, id→quantity: 1, id→category: 1, text→category: 1
- general / ft: category→text: 3, org→address: 2, person→org: 1, quantity→category: 1, id→quantity: 1, text→account: 1, id→category: 1, text→category: 1

### seedをまたいで再発した誤り

同じ列名・正解・予測の誤りは複数seedで確認されませんでした。

### 全ての誤り・unknown（評価例。学習に転用しない）

| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |
|---|---|---|---:|---|---|---|---:|---:|
| critical | business | blend50 | t | total invoices paid | quantity | amount | 0.7848 | yes |
| unknown | business | blend50 | t | abn | id | unknown | 0.5431 | no |
| unknown | business | blend50 | t | australian sourced goods | amount | unknown | 0.4360 | no |
| unknown | business | blend50 | t | commodity-title_en | product | unknown | 0.3683 | no |
| unknown | business | blend50 | t | defence services value | amount | unknown | 0.5881 | no |
| unknown | business | blend50 | t | entitiy | org | unknown | 0.4656 | no |
| unknown | business | blend50 | t | ligne | category | unknown | 0.4925 | no |
| unknown | business | blend50 | t | mois calendrier | date | unknown | 0.6768 | no |
| unknown | business | blend50 | t | overseas sourced goods | amount | unknown | 0.4404 | no |
| unknown | business | blend50 | t | publisher label | org | unknown | 0.4862 | no |
| unknown | business | blend50 | t | quarterno | date | unknown | 0.9692 | no |
| unknown | business | blend50 | t | regrp_nom | account | unknown | 0.4886 | no |
| unknown | business | blend50 | t | regrp_sommaire | account | unknown | 0.6046 | no |
| unknown | business | blend50 | t | 目名 | category | unknown | 0.9690 | no |
| unknown | business | blend50 | t | 科名 | category | unknown | 0.8978 | no |
| wrong | business | blend50 | t | department | org | account | 0.9892 | no |
| wrong | business | blend50 | t | department | org | account | 0.7958 | no |
| wrong | business | blend50 | t | department | org | account | 0.9902 | no |
| wrong | business | blend50 | t | merchant details | text | category | 0.5926 | no |
| wrong | business | blend50 | t | portefeuille_nom_et_code | org | account | 0.6408 | no |
| wrong | business | blend50 | t | purposeofexpenditure | text | account | 0.9634 | no |
| wrong | business | blend50 | t | title | category | text | 0.5975 | no |
| critical | business | blend60 | t | total invoices paid | quantity | amount | 0.7421 | yes |
| unknown | business | blend60 | t | australian sourced goods | amount | unknown | 0.4930 | no |
| unknown | business | blend60 | t | commodity-title_en | product | unknown | 0.4079 | no |
| unknown | business | blend60 | t | mois calendrier | date | unknown | 0.7394 | no |
| unknown | business | blend60 | t | overseas sourced goods | amount | unknown | 0.5081 | no |
| unknown | business | blend60 | t | publisher label | org | unknown | 0.4518 | no |
| unknown | business | blend60 | t | quarterno | date | unknown | 0.9728 | no |
| unknown | business | blend60 | t | regrp_nom | account | unknown | 0.4710 | no |
| unknown | business | blend60 | t | regrp_sommaire | account | unknown | 0.5928 | no |
| unknown | business | blend60 | t | 目名 | category | unknown | 0.9666 | no |
| unknown | business | blend60 | t | 科名 | category | unknown | 0.9075 | no |
| wrong | business | blend60 | t | department | org | account | 0.9883 | no |
| wrong | business | blend60 | t | department | org | account | 0.7869 | no |
| wrong | business | blend60 | t | department | org | account | 0.9899 | no |
| wrong | business | blend60 | t | entitiy | org | account | 0.5103 | no |
| wrong | business | blend60 | t | ligne | category | id | 0.5388 | no |
| wrong | business | blend60 | t | merchant details | text | category | 0.6655 | no |
| wrong | business | blend60 | t | portefeuille_nom_et_code | org | account | 0.6517 | no |
| wrong | business | blend60 | t | purposeofexpenditure | text | account | 0.9652 | no |
| wrong | business | blend60 | t | title | category | text | 0.5778 | no |
| critical | business | blend70 | t | total invoices paid | quantity | amount | 0.6995 | yes |
| unknown | business | blend70 | t | commodity-title_en | product | unknown | 0.4475 | no |
| unknown | business | blend70 | t | description | account | unknown | 0.4854 | no |
| unknown | business | blend70 | t | mois calendrier | date | unknown | 0.8021 | no |
| unknown | business | blend70 | t | quarterno | date | unknown | 0.9764 | no |
| unknown | business | blend70 | t | regrp_sommaire | account | unknown | 0.5810 | no |
| unknown | business | blend70 | t | 目名 | category | unknown | 0.9642 | no |
| unknown | business | blend70 | t | 科名 | category | unknown | 0.9173 | no |
| wrong | business | blend70 | t | department | org | account | 0.9875 | no |
| wrong | business | blend70 | t | department | org | account | 0.7780 | no |
| wrong | business | blend70 | t | department | org | account | 0.9895 | no |
| wrong | business | blend70 | t | entitiy | org | account | 0.5954 | no |
| wrong | business | blend70 | t | ligne | category | id | 0.6242 | no |
| wrong | business | blend70 | t | merchant details | text | category | 0.7384 | no |
| wrong | business | blend70 | t | portefeuille_nom_et_code | org | account | 0.6626 | no |
| wrong | business | blend70 | t | purposeofexpenditure | text | account | 0.9670 | no |
| wrong | business | blend70 | t | title | category | text | 0.5582 | no |
| unknown | business | ft | t | mois calendrier | date | unknown | 0.9901 | no |
| unknown | business | ft | t | quarterno | date | unknown | 0.9873 | no |
| unknown | business | ft | t | regrp_sommaire | account | unknown | 0.5455 | no |
| unknown | business | ft | t | title | category | unknown | 0.4992 | no |
| unknown | business | ft | t | total invoices paid | quantity | unknown | 0.5714 | no |
| unknown | business | ft | t | 目名 | category | unknown | 0.9569 | no |
| unknown | business | ft | t | 科名 | category | unknown | 0.9466 | no |
| wrong | business | ft | t | department | org | account | 0.9851 | no |
| wrong | business | ft | t | department | org | account | 0.7513 | no |
| wrong | business | ft | t | department | org | account | 0.9885 | no |
| wrong | business | ft | t | description | account | text | 0.6643 | no |
| wrong | business | ft | t | entitiy | org | account | 0.8505 | no |
| wrong | business | ft | t | ligne | category | id | 0.8806 | no |
| wrong | business | ft | t | merchant details | text | category | 0.9572 | no |
| wrong | business | ft | t | portefeuille_nom_et_code | org | account | 0.6954 | no |
| wrong | business | ft | t | purposeofexpenditure | text | account | 0.9723 | no |
| critical | business2 | blend50 | t | miscellaneous_divers | amount | quantity | 0.9716 | yes |
| critical | business2 | blend50 | t | total invoices paid | quantity | amount | 0.7811 | yes |
| other_ng | business2 | blend50 | t | a2 floorspace gains sqm | other | quantity | 0.5679 | no |
| other_ng | business2 | blend50 | t | d2 floorspace net sqm | other | amount | 0.5030 | no |
| unknown | business2 | blend50 | t | amt-units_mnt-unite | category | unknown | 0.4630 | no |
| unknown | business2 | blend50 | t | epc_score_known | category | unknown | 0.4647 | no |
| unknown | business2 | blend50 | t | fine | amount | unknown | 0.4348 | no |
| unknown | business2 | blend50 | t | numbers of | date | unknown | 0.4882 | no |
| unknown | business2 | blend50 | t | numéro entente-cadre | id | unknown | 0.5352 | no |
| unknown | business2 | blend50 | t | percentage (%) of the total amount paid | rate | unknown | 0.9822 | no |
| unknown | business2 | blend50 | t | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5507 | no |
| unknown | business2 | blend50 | t | projection | category | unknown | 0.3732 | no |
| unknown | business2 | blend50 | t | projection | category | unknown | 0.4137 | no |
| unknown | business2 | blend50 | t | service | account | unknown | 0.4652 | no |
| unknown | business2 | blend50 | t | super output area 2011 name | address | unknown | 0.4949 | no |
| unknown | business2 | blend50 | t | surveyname | text | unknown | 0.4870 | no |
| unknown | business2 | blend50 | t | surveyname | text | unknown | 0.4652 | no |
| unknown | business2 | blend50 | t | terminal | address | unknown | 0.3961 | no |
| unknown | business2 | blend50 | t | terrace | quantity | unknown | 0.4006 | no |
| unknown | business2 | blend50 | t | terrace | quantity | unknown | 0.4513 | no |
| unknown | business2 | blend50 | t | tlist(q1) | date | unknown | 0.9921 | no |
| unknown | business2 | blend50 | t | tlist(q1) | date | unknown | 0.9928 | no |
| unknown | business2 | blend50 | t | tlist(q1) | date | unknown | 0.9930 | no |
| unknown | business2 | blend50 | t | tlist(q1) | date | unknown | 0.9932 | no |
| unknown | business2 | blend50 | t | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend50 | t | total_floor_area_known | category | unknown | 0.4819 | no |
| unknown | business2 | blend50 | t | total_verified_sales | quantity | unknown | 0.5074 | no |
| unknown | business2 | blend50 | t | value | amount | unknown | 0.5381 | no |
| unknown | business2 | blend50 | t | value | quantity | unknown | 0.5075 | no |
| unknown | business2 | blend50 | t | value () | amount | unknown | 0.9852 | no |
| unknown | business2 | blend50 | t | volume (mcf) | quantity | unknown | 0.5177 | no |
| wrong | business2 | blend50 | t | construction_age_band | category | date | 0.5044 | no |
| wrong | business2 | blend50 | t | monitor | id | category | 0.5858 | no |
| wrong | business2 | blend50 | t | name | org | address | 0.6380 | no |
| wrong | business2 | blend50 | t | number_habitable_rooms | quantity | category | 0.7611 | no |
| wrong | business2 | blend50 | t | number_habitable_rooms_known | category | quantity | 0.5728 | no |
| wrong | business2 | blend50 | t | numéro_uev | id | address | 0.7066 | no |
| wrong | business2 | blend50 | t | service_responsable | account | category | 0.7358 | no |
| wrong | business2 | blend50 | t | situtation | address | category | 0.7882 | no |
| wrong | business2 | blend50 | t | type | account | category | 0.9835 | no |
| wrong | business2 | blend50 | t | warddesc | address | category | 0.8212 | no |
| critical | business2 | blend60 | t | miscellaneous_divers | amount | quantity | 0.9757 | yes |
| critical | business2 | blend60 | t | total invoices paid | quantity | amount | 0.7377 | yes |
| other_ng | business2 | blend60 | t | a2 floorspace gains sqm | other | quantity | 0.5001 | no |
| unknown | business2 | blend60 | t | epc_score_known | category | unknown | 0.4745 | no |
| unknown | business2 | blend60 | t | numéro entente-cadre | id | unknown | 0.5160 | no |
| unknown | business2 | blend60 | t | percentage (%) of the total amount paid | rate | unknown | 0.9789 | no |
| unknown | business2 | blend60 | t | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.4940 | no |
| unknown | business2 | blend60 | t | projection | category | unknown | 0.4391 | no |
| unknown | business2 | blend60 | t | projection | category | unknown | 0.4459 | no |
| unknown | business2 | blend60 | t | terminal | address | unknown | 0.3576 | no |
| unknown | business2 | blend60 | t | terrace | quantity | unknown | 0.4746 | no |
| unknown | business2 | blend60 | t | terrace | quantity | unknown | 0.5236 | no |
| unknown | business2 | blend60 | t | tlist(q1) | date | unknown | 0.9912 | no |
| unknown | business2 | blend60 | t | tlist(q1) | date | unknown | 0.9916 | no |
| unknown | business2 | blend60 | t | tlist(q1) | date | unknown | 0.9917 | no |
| unknown | business2 | blend60 | t | tlist(q1) | date | unknown | 0.9920 | no |
| unknown | business2 | blend60 | t | tlist(q1) | date | unknown | 0.9892 | no |
| unknown | business2 | blend60 | t | total_floor_area_known | category | unknown | 0.4720 | no |
| unknown | business2 | blend60 | t | total_verified_sales | quantity | unknown | 0.6016 | no |
| unknown | business2 | blend60 | t | value | amount | unknown | 0.5263 | no |
| unknown | business2 | blend60 | t | value | quantity | unknown | 0.6039 | no |
| unknown | business2 | blend60 | t | value () | amount | unknown | 0.9860 | no |
| wrong | business2 | blend60 | t | construction_age_band | category | date | 0.5980 | no |
| wrong | business2 | blend60 | t | fine | amount | category | 0.5167 | no |
| wrong | business2 | blend60 | t | monitor | id | category | 0.6583 | no |
| wrong | business2 | blend60 | t | name | org | address | 0.5660 | no |
| wrong | business2 | blend60 | t | number_habitable_rooms | quantity | category | 0.7209 | no |
| wrong | business2 | blend60 | t | number_habitable_rooms_known | category | quantity | 0.6456 | no |
| wrong | business2 | blend60 | t | numéro_uev | id | address | 0.7323 | no |
| wrong | business2 | blend60 | t | service | account | org | 0.5114 | no |
| wrong | business2 | blend60 | t | service_responsable | account | category | 0.7082 | no |
| wrong | business2 | blend60 | t | situtation | address | category | 0.7542 | no |
| wrong | business2 | blend60 | t | type | account | category | 0.9833 | no |
| wrong | business2 | blend60 | t | warddesc | address | category | 0.8485 | no |
| critical | business2 | blend70 | t | miscellaneous_divers | amount | quantity | 0.9798 | yes |
| critical | business2 | blend70 | t | total invoices paid | quantity | amount | 0.6943 | yes |
| critical | business2 | blend70 | t | total_verified_sales | quantity | amount | 0.6958 | yes |
| unknown | business2 | blend70 | t | epc_score_known | category | unknown | 0.4843 | no |
| unknown | business2 | blend70 | t | numéro entente-cadre | id | unknown | 0.4967 | no |
| unknown | business2 | blend70 | t | percentage (%) of the total amount paid | rate | unknown | 0.9756 | no |
| unknown | business2 | blend70 | t | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | 0.5302 | no |
| unknown | business2 | blend70 | t | projection | category | unknown | 0.5122 | no |
| unknown | business2 | blend70 | t | projection | category | unknown | 0.5202 | no |
| unknown | business2 | blend70 | t | terminal | address | unknown | 0.4163 | no |
| unknown | business2 | blend70 | t | terrace | quantity | unknown | 0.5486 | no |
| unknown | business2 | blend70 | t | terrace | quantity | unknown | 0.5958 | no |
| unknown | business2 | blend70 | t | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend70 | t | tlist(q1) | date | unknown | 0.9903 | no |
| unknown | business2 | blend70 | t | tlist(q1) | date | unknown | 0.9904 | no |
| unknown | business2 | blend70 | t | tlist(q1) | date | unknown | 0.9907 | no |
| unknown | business2 | blend70 | t | tlist(q1) | date | unknown | 0.9881 | no |
| unknown | business2 | blend70 | t | total_floor_area_known | category | unknown | 0.4620 | no |
| unknown | business2 | blend70 | t | value () | amount | unknown | 0.9868 | no |
| wrong | business2 | blend70 | t | construction_age_band | category | date | 0.6917 | no |
| wrong | business2 | blend70 | t | fine | amount | category | 0.5986 | no |
| wrong | business2 | blend70 | t | monitor | id | category | 0.7308 | no |
| wrong | business2 | blend70 | t | number_habitable_rooms | quantity | category | 0.6808 | no |
| wrong | business2 | blend70 | t | number_habitable_rooms_known | category | quantity | 0.7184 | no |
| wrong | business2 | blend70 | t | numéro_uev | id | address | 0.7581 | no |
| wrong | business2 | blend70 | t | service | account | org | 0.5955 | no |
| wrong | business2 | blend70 | t | service_responsable | account | category | 0.6806 | no |
| wrong | business2 | blend70 | t | situtation | address | category | 0.7202 | no |
| wrong | business2 | blend70 | t | type | account | category | 0.9830 | no |
| wrong | business2 | blend70 | t | warddesc | address | category | 0.8758 | no |
| critical | business2 | ft | t | miscellaneous_divers | amount | quantity | 0.9921 | yes |
| critical | business2 | ft | t | total_verified_sales | quantity | amount | 0.9783 | yes |
| unknown | business2 | ft | t | fuel_poverty | rate | unknown | 0.6297 | no |
| unknown | business2 | ft | t | habitatdescription | text | unknown | 0.4723 | no |
| unknown | business2 | ft | t | numéro entente-cadre | id | unknown | 0.5341 | no |
| unknown | business2 | ft | t | percentage (%) of the total amount paid | rate | unknown | 0.9656 | no |
| unknown | business2 | ft | t | projection | category | unknown | 0.7318 | no |
| unknown | business2 | ft | t | projection | category | unknown | 0.7431 | no |
| unknown | business2 | ft | t | terrace | quantity | unknown | 0.7707 | no |
| unknown | business2 | ft | t | terrace | quantity | unknown | 0.8127 | no |
| unknown | business2 | ft | t | tlist(q1) | date | unknown | 0.9878 | no |
| unknown | business2 | ft | t | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | t | tlist(q1) | date | unknown | 0.9864 | no |
| unknown | business2 | ft | t | tlist(q1) | date | unknown | 0.9870 | no |
| unknown | business2 | ft | t | tlist(q1) | date | unknown | 0.9847 | no |
| unknown | business2 | ft | t | total invoices paid | quantity | unknown | 0.5640 | no |
| unknown | business2 | ft | t | total_floor_area_known | category | unknown | 0.4587 | no |
| unknown | business2 | ft | t | tree type | category | unknown | 0.4978 | no |
| unknown | business2 | ft | t | value () | amount | unknown | 0.9893 | no |
| wrong | business2 | ft | t | account name | account | org | 0.6033 | no |
| wrong | business2 | ft | t | conservation_area_site_id | category | id | 0.5052 | no |
| wrong | business2 | ft | t | construction_age_band | category | date | 0.9726 | no |
| wrong | business2 | ft | t | fine | amount | category | 0.8441 | no |
| wrong | business2 | ft | t | monitor | id | category | 0.9483 | no |
| wrong | business2 | ft | t | number_habitable_rooms | quantity | category | 0.5604 | no |
| wrong | business2 | ft | t | number_habitable_rooms_known | category | quantity | 0.9369 | no |
| wrong | business2 | ft | t | numéro_uev | id | address | 0.8354 | no |
| wrong | business2 | ft | t | service | account | org | 0.8477 | no |
| wrong | business2 | ft | t | service_responsable | account | category | 0.5977 | no |
| wrong | business2 | ft | t | situtation | address | category | 0.6183 | no |
| wrong | business2 | ft | t | terminal | address | org | 0.5925 | no |
| wrong | business2 | ft | t | type | account | category | 0.9822 | no |
| wrong | business2 | ft | t | warddesc | address | category | 0.9576 | no |
| critical | dev220 | blend50 | t | credit limit | amount | quantity | 0.6175 | yes |
| critical | dev220 | blend50 | t | purchase order by customer | id | quantity | 0.8835 | yes |
| unknown | dev220 | blend50 | t | item description | text | unknown | 0.4734 | no |
| unknown | dev220 | blend50 | t | material | product | unknown | 0.4964 | no |
| unknown | dev220 | blend50 | t | taxable | category | unknown | 0.4933 | no |
| unknown | dev220 | blend50 | t | website | text | unknown | 0.4956 | no |
| unknown | dev220 | blend50 | t | その他費用 | amount | unknown | 0.5902 | no |
| unknown | dev220 | blend50 | t | ポイント | amount | unknown | 0.5660 | no |
| unknown | dev220 | blend50 | t | 作業者欄 | person | unknown | 0.4899 | no |
| unknown | dev220 | blend50 | t | 受注名 | person | unknown | 0.4963 | no |
| unknown | dev220 | blend50 | t | 支出負担行為担当官 | person | unknown | 0.4826 | no |
| unknown | dev220 | blend50 | t | 発送先カナ | person | unknown | 0.4615 | no |
| unknown | dev220 | blend50 | t | 随意契約理由 | text | unknown | 0.4922 | no |
| wrong | dev220 | blend50 | t | customer rank | quantity | category | 0.9750 | no |
| wrong | dev220 | blend50 | t | supplier rank | quantity | category | 0.9061 | no |
| wrong | dev220 | blend50 | t | メッセージ | text | category | 0.5022 | no |
| wrong | dev220 | blend50 | t | 担当課 | org | account | 0.7898 | no |
| critical | dev220 | blend60 | t | credit limit | amount | quantity | 0.6746 | yes |
| critical | dev220 | blend60 | t | purchase order by customer | id | quantity | 0.9026 | yes |
| wrong | dev220 | blend60 | t | customer rank | quantity | category | 0.9726 | no |
| wrong | dev220 | blend60 | t | supplier rank | quantity | category | 0.9207 | no |
| wrong | dev220 | blend60 | t | 担当課 | org | account | 0.8231 | no |
| wrong | dev220 | blend60 | t | 随意契約理由 | text | category | 0.5779 | no |
| critical | dev220 | blend70 | t | credit limit | amount | quantity | 0.7316 | yes |
| critical | dev220 | blend70 | t | purchase order by customer | id | quantity | 0.9216 | yes |
| wrong | dev220 | blend70 | t | customer rank | quantity | category | 0.9703 | no |
| wrong | dev220 | blend70 | t | supplier rank | quantity | category | 0.9352 | no |
| wrong | dev220 | blend70 | t | 担当課 | org | account | 0.8564 | no |
| wrong | dev220 | blend70 | t | 随意契約理由 | text | category | 0.6636 | no |
| critical | dev220 | ft | t | credit limit | amount | quantity | 0.9028 | yes |
| critical | dev220 | ft | t | purchase order by customer | id | quantity | 0.9787 | yes |
| unknown | dev220 | ft | t | 税率 | rate | unknown | 0.4859 | no |
| wrong | dev220 | ft | t | customer rank | quantity | category | 0.9633 | no |
| wrong | dev220 | ft | t | supplier rank | quantity | category | 0.9788 | no |
| wrong | dev220 | ft | t | 担当課 | org | account | 0.9565 | no |
| wrong | dev220 | ft | t | 随意契約理由 | text | category | 0.9206 | no |
| critical | general | blend50 | t | 発生県 | id | quantity | 0.8882 | yes |
| other_ng | general | blend50 | t | dag-stage | other | quantity | 0.7005 | no |
| other_ng | general | blend50 | t | dbpedia_score | other | rate | 0.9249 | no |
| other_ng | general | blend50 | t | value | other | rate | 0.9300 | no |
| other_ng | general | blend50 | t | 五島 | other | quantity | 0.9889 | no |
| other_ng | general | blend50 | t | 被害域幅(m)最小 | other | quantity | 0.5154 | no |
| other_ng | general | blend50 | t | 被害域長さ(100m)最小 | other | quantity | 0.7722 | no |
| unknown | general | blend50 | t | denominatorunweighted | quantity | unknown | 0.4866 | no |
| unknown | general | blend50 | t | denominatorweighted | quantity | unknown | 0.5252 | no |
| unknown | general | blend50 | t | image_level_adj_acc | rate | unknown | 0.9416 | no |
| unknown | general | blend50 | t | pelicula | text | unknown | 0.4772 | no |
| unknown | general | blend50 | t | property | category | unknown | 0.4032 | no |
| unknown | general | blend50 | t | study | text | unknown | 0.4534 | no |
| unknown | general | blend50 | t | 発生日 | date | unknown | 0.9802 | no |
| unknown | general | blend50 | t | 登録年月日 | date | unknown | 0.9921 | no |
| unknown | general | blend50 | t | 科名 | category | unknown | 0.9337 | no |
| unknown | general | blend50 | t | 読み方 | address | unknown | 0.4973 | no |
| wrong | general | blend50 | t | author | person | org | 0.7411 | no |
| wrong | general | blend50 | t | cleaned | text | category | 0.5192 | no |
| wrong | general | blend50 | t | goal | id | category | 0.6895 | no |
| wrong | general | blend50 | t | indicator | text | category | 0.5788 | no |
| wrong | general | blend50 | t | keyword | category | text | 0.8911 | no |
| wrong | general | blend50 | t | place | org | address | 0.9145 | no |
| wrong | general | blend50 | t | year_step_size | quantity | category | 0.7939 | no |
| wrong | general | blend50 | t | ステーション名 | org | address | 0.9086 | no |
| critical | general | blend60 | t | 発生県 | id | quantity | 0.8877 | yes |
| other_ng | general | blend60 | t | dag-stage | other | quantity | 0.6682 | no |
| other_ng | general | blend60 | t | dbpedia_score | other | rate | 0.9265 | no |
| other_ng | general | blend60 | t | mt2 | other | category | 0.5776 | no |
| other_ng | general | blend60 | t | value | other | rate | 0.9368 | no |
| other_ng | general | blend60 | t | 五島 | other | quantity | 0.9868 | no |
| other_ng | general | blend60 | t | 被害域長さ(100m)最小 | other | quantity | 0.7289 | no |
| unknown | general | blend60 | t | cleaned | text | unknown | 0.4291 | no |
| unknown | general | blend60 | t | denominatorunweighted | quantity | unknown | 0.5665 | no |
| unknown | general | blend60 | t | denominatorweighted | quantity | unknown | 0.6185 | no |
| unknown | general | blend60 | t | image_level_adj_acc | rate | unknown | 0.9495 | no |
| unknown | general | blend60 | t | property | category | unknown | 0.4327 | no |
| unknown | general | blend60 | t | sens_final | rate | unknown | 0.5919 | no |
| unknown | general | blend60 | t | source_value | category | unknown | 0.4720 | no |
| unknown | general | blend60 | t | study | text | unknown | 0.3634 | no |
| unknown | general | blend60 | t | 発生日 | date | unknown | 0.9819 | no |
| unknown | general | blend60 | t | 登録年月日 | date | unknown | 0.9905 | no |
| unknown | general | blend60 | t | 科名 | category | unknown | 0.9360 | no |
| unknown | general | blend60 | t | 読み方 | address | unknown | 0.4971 | no |
| wrong | general | blend60 | t | author | person | org | 0.6932 | no |
| wrong | general | blend60 | t | goal | id | category | 0.6721 | no |
| wrong | general | blend60 | t | indicator | text | category | 0.6032 | no |
| wrong | general | blend60 | t | keyword | category | text | 0.8812 | no |
| wrong | general | blend60 | t | place | org | address | 0.9008 | no |
| wrong | general | blend60 | t | year_step_size | quantity | category | 0.7975 | no |
| wrong | general | blend60 | t | ステーション名 | org | address | 0.9031 | no |
| wrong | general | blend60 | t | データセット_キーワード | category | text | 0.5576 | no |
| critical | general | blend70 | t | 発生県 | id | quantity | 0.8872 | yes |
| other_ng | general | blend70 | t | dag-stage | other | quantity | 0.6360 | no |
| other_ng | general | blend70 | t | dbpedia_score | other | rate | 0.9282 | no |
| other_ng | general | blend70 | t | mt2 | other | category | 0.6729 | no |
| other_ng | general | blend70 | t | value | other | rate | 0.9436 | no |
| other_ng | general | blend70 | t | 五島 | other | quantity | 0.9848 | no |
| other_ng | general | blend70 | t | 被害域長さ(100m)最小 | other | quantity | 0.6856 | no |
| unknown | general | blend70 | t | cleaned | text | unknown | 0.4538 | no |
| unknown | general | blend70 | t | denominatorunweighted | quantity | unknown | 0.6578 | no |
| unknown | general | blend70 | t | denominatorweighted | quantity | unknown | 0.7117 | no |
| unknown | general | blend70 | t | image_level_adj_acc | rate | unknown | 0.9573 | no |
| unknown | general | blend70 | t | property | category | unknown | 0.5035 | no |
| unknown | general | blend70 | t | sens_final | rate | unknown | 0.6895 | no |
| unknown | general | blend70 | t | source | category | unknown | 0.4256 | no |
| unknown | general | blend70 | t | source_value | category | unknown | 0.4907 | no |
| unknown | general | blend70 | t | study | text | unknown | 0.3096 | no |
| unknown | general | blend70 | t | 発生日 | date | unknown | 0.9836 | no |
| unknown | general | blend70 | t | 登録年月日 | date | unknown | 0.9890 | no |
| unknown | general | blend70 | t | 科名 | category | unknown | 0.9383 | no |
| unknown | general | blend70 | t | 読み方 | address | unknown | 0.4968 | no |
| wrong | general | blend70 | t | author | person | org | 0.6453 | no |
| wrong | general | blend70 | t | goal | id | category | 0.6547 | no |
| wrong | general | blend70 | t | indicator | text | category | 0.6276 | no |
| wrong | general | blend70 | t | keyword | category | text | 0.8713 | no |
| wrong | general | blend70 | t | place | org | address | 0.8871 | no |
| wrong | general | blend70 | t | source | category | text | 0.5216 | no |
| wrong | general | blend70 | t | year_step_size | quantity | category | 0.8011 | no |
| wrong | general | blend70 | t | ステーション名 | org | address | 0.8976 | no |
| wrong | general | blend70 | t | データセット_キーワード | category | text | 0.6485 | no |
| critical | general | ft | t | 発生県 | id | quantity | 0.8857 | yes |
| other_ng | general | ft | t | dag-stage | other | quantity | 0.5393 | no |
| other_ng | general | ft | t | dbpedia_score | other | rate | 0.9330 | no |
| other_ng | general | ft | t | episode | other | quantity | 0.6704 | no |
| other_ng | general | ft | t | mt2 | other | category | 0.9587 | no |
| other_ng | general | ft | t | value | other | rate | 0.9642 | no |
| other_ng | general | ft | t | 五島 | other | quantity | 0.9786 | no |
| other_ng | general | ft | t | 被害域長さ(100m)最小 | other | quantity | 0.5557 | no |
| unknown | general | ft | t | denominatorunweighted | quantity | unknown | 0.9314 | no |
| unknown | general | ft | t | denominatorweighted | quantity | unknown | 0.9913 | no |
| unknown | general | ft | t | image_level_adj_acc | rate | unknown | 0.9808 | no |
| unknown | general | ft | t | lda | text | unknown | 0.4971 | no |
| unknown | general | ft | t | property | category | unknown | 0.7159 | no |
| unknown | general | ft | t | sens_final | rate | unknown | 0.9825 | no |
| unknown | general | ft | t | source | category | unknown | 0.4825 | no |
| unknown | general | ft | t | source_value | category | unknown | 0.7006 | no |
| unknown | general | ft | t | study | text | unknown | 0.4404 | no |
| unknown | general | ft | t | 発生日 | date | unknown | 0.9887 | no |
| unknown | general | ft | t | 登録年月日 | date | unknown | 0.9842 | no |
| unknown | general | ft | t | 科名 | category | unknown | 0.9452 | no |
| unknown | general | ft | t | 読み方 | address | unknown | 0.4962 | no |
| wrong | general | ft | t | author | person | org | 0.5015 | no |
| wrong | general | ft | t | cleaned | text | account | 0.6469 | no |
| wrong | general | ft | t | goal | id | category | 0.6025 | no |
| wrong | general | ft | t | indicator | text | category | 0.7008 | no |
| wrong | general | ft | t | keyword | category | text | 0.8415 | no |
| wrong | general | ft | t | place | org | address | 0.8461 | no |
| wrong | general | ft | t | source | category | text | 0.7012 | no |
| wrong | general | ft | t | year_step_size | quantity | category | 0.8120 | no |
| wrong | general | ft | t | ステーション名 | org | address | 0.8813 | no |
| wrong | general | ft | t | データセット_キーワード | category | text | 0.9211 | no |

### unknown の判定理由

- date_value_evidence_low: 36件
- numeric_top2_too_close: 17件
- numeric_values_not_parseable: 13件
- other_class: 40件
- probability_below_threshold: 71件

## 原因仮説（断定ではない）

- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: 24件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。
- categoryを含む取り違え: 80件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。
- 高い上位確率（90%以上）なのに最終予測がunknown: 59件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。

## 次の検証案

1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。
2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。
3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。
4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。

## 制約

これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。
