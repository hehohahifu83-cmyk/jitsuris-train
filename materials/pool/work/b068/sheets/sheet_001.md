# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Province/Territory
- 例1 値：Yukon | Nunavut | British Columbia | New Brunswick | Total
  - 同じ表の列：Number of CWB Recip…, Assessed CWB Credit…

## g0002（1 列）
- 見出し：Number of CWB Recipients
- 例1 値：70880 | 14800 | 5210 | 2984130 | 1262720
  - 同じ表の列：Province/Territory, Assessed CWB Credit…

## g0003（1 列）
- 見出し：Assessed CWB Credit (dollars)
- 例1 値：528708000 | 1774847000 | 4290711000 | 3474000 | 136011000
  - 同じ表の列：Province/Territory, Number of CWB Recip…

## g0004（1 列）
- 見出し：Province or Territory
- 例1 値：Manitoba | Ontario | Saskatchewan | Quebec | Prince Edward Island
  - 同じ表の列：Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0005（1 列）
- 見出し：Total, All Recipients, Number
- 例1 値：46940 | 456350 | 16360 | 5780 | 3810140
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0006（1 列）
- 見出し：Total, All Recipients, Thousands of Dollars
- 例1 値：29219249 | 36578 | 641094 | 15844 | 761262
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0007（1 列）
- 見出し：Less than $5,000, Number
- 例1 値：168440 | 250 | 80 | 16710 | 360
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0008（1 列）
- 見出し：Less than $5,000, Thousands of Dollars
- 例1 値：199179 | 212571 | 761533 | 373756 | 5353
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0009（1 列）
- 見出し：$5,000 to $9,999, Number
- 例1 値：1500 | 6060 | 180 | 180 | 30
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0010（1 列）
- 見出し：$5,000 to $9,999, Thousands of Dollars
- 例1 値：2057 | 118762 | 43752 | 589 | 952293
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0011（1 列）
- 見出し：$10,000 to $14,999, Number
- 例1 値：90 | 13350 | 5110 | 160 | 9270
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…

## g0012（1 列）
- 見出し：$10,000 to $14,999, Thousands of Dollars
- 例1 値：1640857 | 53048 | 4609 | 172177 | 67577
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…

## g0013（1 列）
- 見出し：$15,000 to $19,999, Number
- 例1 値：60 | 3130 | 2600 | 19350 | 2550
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…

## g0014（1 列）
- 見出し：Health_Region_ID
- 例1 値：3566 | 3595 | 3561 | 3575 | 3526
  - 同じ表の列：Health_Region_area, cases_apr19, cases_may13, Province, incidence_apr19, incidence_may13, population_2016, percent_65+

## g0015（1 列）
- 見出し：Health_Region_area
- 例1 値：1991151295 | 26204101166 | 41310451756 | 21317859696 | 2985533954
  - 同じ表の列：Health_Region_ID, cases_apr19, cases_may13, Province, incidence_apr19, incidence_may13, population_2016, percent_65+

## g0016（1 列）
- 見出し：cases_apr19
- 例1 値：26 | 17 | 239 | 329 | 226
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_may13, Province, incidence_apr19, incidence_may13, population_2016, percent_65+

## g0017（1 列）
- 見出し：cases_may13
- 例1 値：307 | 42 | 30 | 129 | 173
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, Province, incidence_apr19, incidence_may13, population_2016, percent_65+

## g0018（1 列）
- 見出し：Province
- 例1 値：ON | ON | ON | QC | ON
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, incidence_apr19, incidence_may13, population_2016, percent_65+

## g0019（1 列）
- 見出し：incidence_apr19
- 例1 値：138.4 | 25.2 | 29.2 | 39.6 | 15.2
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, Province, incidence_may13, population_2016, percent_65+

## g0020（1 列）
- 見出し：incidence_may13
- 例1 値：101.2 | 581.1 | 20.4 | 0.0 | 111.1
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, Province, incidence_apr19, population_2016, percent_65+

## g0021（1 列）
- 見出し：population_2016
- 例1 値：639245 | 284461 | 113084 | 455526 | 535154
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, Province, incidence_apr19, incidence_may13, percent_65+

## g0022（1 列）
- 見出し：percent_65+
- 例1 値：14.9 | 19 | 15.7 | 15.1 | 17.9
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, Province, incidence_apr19, incidence_may13, population_2016

## g0023（1 列）
- 見出し：percent_black
- 例1 値：4.38 | 0.21 | 0.92 | 0.62 | 0.69
  - 同じ表の列：Health_Region_ID, Health_Region_area, cases_apr19, cases_may13, Province, incidence_apr19, incidence_may13, population_2016

## g0024（1 列）
- 見出し：Location/Emplacement
- 例1 値：Resolute | Amherstburg | Sidney | Ottawa | Halifax
  - 同じ表の列：Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0025（1 列）
- 見出し：Province/Province
- 例1 値：NT | QC | ON | BC | NU
  - 同じ表の列：Location/Emplacement, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0026（1 列）
- 見出し：Collection Start/Debut du prelevement (UTC)
- 例1 値：2011-04-22 16:49 | 2011-05-17 22:55 | 2011-05-09 15:59 | 2011-05-08 16:33 | 2011-03-23 16:33
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0027（1 列）
- 見出し：Collection Time/Duree d'echantillonnage (s)
- 例1 値：78420 | 604800 | 86395 | 86100 | 675900
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0028（1 列）
- 見出し：AirVolume/Volume d'air (m3)
- 例1 値：17841 | 17626.3 | 12491.7 | 25334.1 | 12566.5
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0029（1 列）
- 見出し：Cs-134 Activity/Cs-134 Activite (Bq/m3)
- 例1 値：1.66E-04 | 1.58E-04 | 4.57E-06 | 4.92E-04 | 1.88E-05
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0030（1 列）
- 見出し：Cs-134 Uncertainty/Cs-134 Incertitude (Bq/m3)
- 例1 値：5.50E-07 | 4.00E-06 | 7.00E-07 | 3.00E-06 | 3.90E-07
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0031（1 列）
- 見出し：Cs-136 Activity/Cs-136 Activite (Bq/m3)
- 例1 値：1.07E-05 | 7.90E-06 | 1.43E-05 | 7.15E-06 | 1.11E-05
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Uncertainty/…

## g0032（1 列）
- 見出し：Cs-136 Uncertainty/Cs-136 Incertitude (Bq/m3)
- 例1 値：6.80E-07 | 6.50E-07 | 1.30E-06 | 4.20E-06 | 4.00E-07
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…

## g0033（1 列）
- 見出し：Cs-137 Activity/Cs-137 Activite (Bq/m3)
- 例1 値：2.49E-04 | 1.22E-04 | 1.26E-04 | 1.04E-04 | 9.79E-06
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, Collection Time/Dur…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…

## g0034（1 列）
- 見出し：Health Canada ID# / Sante Canada ID#
- 例1 値：44056 | 44059 | 44057 | 44036 | 44058
  - 同じ表の列：Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0035（1 列）
- 見出し：Location/Emplacement
- 例1 値：Nass River | Nass River | Nass River | Nass River | Nass River
  - 同じ表の列：Health Canada ID# /…, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0036（1 列）
- 見出し：Weight/Poids (kg)
- 例1 値：157.4 | 120.7 | 116.9 | 159.9 | 113.3
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0037（1 列）
- 見出し：Collection Date / Date de collection
- 例1 値：2018-08-08 | 2018-11-20 | 2018-11-20 | 2019-02-08 | 2018-08-08
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0038（1 列）
- 見出し：Count date / date de mesure
- 例1 値：2018-11-06 | 2018-11-27 | 2018-11-21 | 2018-09-11 | 2018-09-12
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0039（1 列）
- 見出し：Method/Methode
- 例1 値：Gamma Spectroscopy | Gamma Spectroscopy | Gamma Spectroscopy | Gamma Spectroscopy | Gamma Spectroscopy
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0040（1 列）
- 見出し：Counting time/temps de mesure (h)
- 例1 値：6 | 6 | 6 | 6 | 6
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0041（1 列）
- 見出し：Cs-137 Activity/ Cs-137 Activite (Bq/kg)
- 例1 値：ND | ND | ND | ND | ND
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Uncertainty …

## g0042（1 列）
- 見出し：Cs-137 Uncertainty / Cs-137 Incertitude (Bq/kg)
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…

## g0043（1 列）
- 見出し：Cs-137 MDC / Cs-137 CMD (Bq/kg)
- 例1 値：0.99 | 0.15 | 0.64 | 0.85 | 0.91
  - 同じ表の列：Health Canada ID# /…, Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…

## g0044（1 列）
- 見出し：PROV
- 例1 値：QC | NB | MB | QC | ON
  - 同じ表の列：EMPGR, AREA, LANG, Q1, O_Q1, Q2, Q2NET, Q3

## g0045（1 列）
- 見出し：EMPGR
- 例1 値：3 | 2 | 1 | 1 | 1
  - 同じ表の列：PROV, AREA, LANG, Q1, O_Q1, Q2, Q2NET, Q3

## g0046（1 列）
- 見出し：AREA
- 例1 値：2 | 4 | 4 | 2 | 2
  - 同じ表の列：PROV, EMPGR, LANG, Q1, O_Q1, Q2, Q2NET, Q3

## g0047（2 列）
- 見出し：LANG
- 例1 値：EN | EN | FR | EN | EN
  - 同じ表の列：PROV, EMPGR, AREA, Q1, O_Q1, Q2, Q2NET, Q3
- 例2 値：EN | EN | FR | FR | EN
  - 同じ表の列：QUEST, STYPE, QF, Q1, Q2, Q3A, Q3B, Q4A

## g0048（2 列）
- 見出し：Q1
- 例1 値：2 | 2 | 3 | 2 | 2
  - 同じ表の列：PROV, EMPGR, AREA, LANG, O_Q1, Q2, Q2NET, Q3
- 例2 値：2 | 2 | 2 | 3 | 3
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q2, Q3A, Q3B, Q4A

## g0049（1 列）
- 見出し：O_Q1
- 例1 値：Sells to military and other | Municipal servce provider for Consumers… | storage | On est specialize en construction de sy… | choses immobilieres
  - 同じ表の列：PROV, EMPGR, AREA, LANG, Q1, Q2, Q2NET, Q3

## g0050（2 列）
- 見出し：Q2
- 例1 値：7 | 5 | 1 | 1 | 5
  - 同じ表の列：PROV, EMPGR, AREA, LANG, Q1, O_Q1, Q2NET, Q3
- 例2 値：7 | 5 | 7 | 7 | 2
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q3A, Q3B, Q4A

## g0051（1 列）
- 見出し：Q2NET
- 例1 値：2 | 1 | 2 | 2 | 3
  - 同じ表の列：PROV, EMPGR, AREA, LANG, Q1, O_Q1, Q2, Q3

## g0052（1 列）
- 見出し：Q3
- 例1 値：2 | 2 | 2 | 1 | 3
  - 同じ表の列：PROV, EMPGR, AREA, LANG, Q1, O_Q1, Q2, Q2NET

## g0053（1 列）
- 見出し：Q4
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PROV, EMPGR, AREA, LANG, Q1, O_Q1, Q2, Q2NET

## g0054（1 列）
- 見出し：QUEST
- 例1 値：79509 | 11616 | 29341 | 57886 | 26876
  - 同じ表の列：STYPE, LANG, QF, Q1, Q2, Q3A, Q3B, Q4A

## g0055（1 列）
- 見出し：STYPE
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：QUEST, LANG, QF, Q1, Q2, Q3A, Q3B, Q4A

## g0056（1 列）
- 見出し：QF
- 例1 値：6 | 6 | 6 | 10 | 5
  - 同じ表の列：QUEST, STYPE, LANG, Q1, Q2, Q3A, Q3B, Q4A

## g0057（1 列）
- 見出し：Q3A
- 例1 値：7 | 6 | 98 | 4 | 6
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q2, Q3B, Q4A

## g0058（1 列）
- 見出し：Q3B
- 例1 値：2 | 3 | 4 | 6 | 2
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q2, Q3A, Q4A

## g0059（1 列）
- 見出し：Q4A
- 例1 値：3 | 4 | 3 | 4 | 5
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q2, Q3A, Q3B

## g0060（1 列）
- 見出し：Q4B
- 例1 値：5 | 7 | 5 | 7 | 7
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q2, Q3A, Q3B

## g0061（1 列）
- 見出し：dept_f
- 例1 値：Bureau du surintendant des institutions… | Agence de la santé publique du Canada | Pétrole et gaz des Indiens du Canada (P… | Normes d'accessibilité Canada | Agriculture et Agroalimentaire Canada
  - 同じ表の列：dept_e, question, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0062（1 列）
- 見出し：dept_e
- 例1 値：Canadian Radio-television and Telecommu… | Canadian Intergovernmental Conference S… | Office of the Correctional Investigator | Transport Canada | Office of the Commissioner for Federal …
  - 同じ表の列：dept_f, question, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0063（1 列）
- 見出し：question
- 例1 値：hmn_15b | hmn_15b | hmn_15b | hmn_15b | hmn_15a
  - 同じ表の列：dept_f, dept_e, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0064（1 列）
- 見出し：question_value_f
- 例1 値：Dans une certaine mesure | Dans une faible mesure | Tous les répondants | Dans une large mesure | Dans une certaine mesure
  - 同じ表の列：dept_f, dept_e, question, question_value_e, shr_w_resp, total_w_resp

## g0065（1 列）
- 見出し：question_value_e
- 例1 値：To a great extent | To a great extent | To a minimal extent | To a great extent | Not at all
  - 同じ表の列：dept_f, dept_e, question, question_value_f, shr_w_resp, total_w_resp

## g0066（1 列）
- 見出し：shr_w_resp
- 例1 値：0.053 | 1 | 0.038 | 1 | 1
  - 同じ表の列：dept_f, dept_e, question, question_value_f, question_value_e, total_w_resp

## g0067（1 列）
- 見出し：total_w_resp
- 例1 値：467 | 70 | 34 | 182 | 3
  - 同じ表の列：dept_f, dept_e, question, question_value_f, question_value_e, shr_w_resp

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
```
