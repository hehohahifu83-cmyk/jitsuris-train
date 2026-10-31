# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：PositiveFluAH1N1pdm09
- 例1 値：483 | 6 | 73 | 14 | 86
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV, TotalParaTests

## g0122（1 列）
- 見出し：PositiveFluAH3
- 例1 値：37 | 66 | 3 | 17 | 51
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV, TotalParaTests

## g0123（1 列）
- 見出し：PositiveFluAunsubtyped
- 例1 値：24 | 4 | 5 | 13 | 351
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV, TotalParaTests

## g0124（1 列）
- 見出し：TotalFluBPositive
- 例1 値：1 | 820 | 164 | 8 | 33
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalRSVTests, TotalPositiveRSV, TotalParaTests

## g0125（1 列）
- 見出し：TotalRSVTests
- 例1 値：9023 | 8416 | 2234 | 3480 | 3134
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalPositiveRSV, TotalParaTests

## g0126（1 列）
- 見出し：TotalPositiveRSV
- 例1 値：352 | 29 | 103 | 6 | 259
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalParaTests

## g0127（1 列）
- 見出し：TotalParaTests
- 例1 値：1294 | 2019 | 1477 | 1225 | 1490
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV

## g0128（1 列）
- 見出し：TotalPositivePara
- 例1 値：71 | 120 | 68 | 97 | 71
  - 同じ表の列：InfluenzaSeasonandE…, TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV

## g0129（1 列）
- 見出し：Location
- 例1 値：Winnipeg West End | Winnipeg West End | Winnipeg West End | Winnipeg West End | Winnipeg West End
  - 同じ表の列：Date, region, measureid, fractionid, viral_load, seven_day_rolling_a…, pruid

## g0130（1 列）
- 見出し：region
- 例1 値：Winnipeg | Winnipeg | Winnipeg | Winnipeg | Winnipeg
  - 同じ表の列：Date, Location, measureid, fractionid, viral_load, seven_day_rolling_a…, pruid

## g0131（1 列）
- 見出し：measureid
- 例1 値：covN2 | covN2 | covN2 | covN2 | covN2
  - 同じ表の列：Date, Location, region, fractionid, viral_load, seven_day_rolling_a…, pruid

## g0132（1 列）
- 見出し：fractionid
- 例1 値：solid | solid | solid | solid | solid
  - 同じ表の列：Date, Location, region, measureid, viral_load, seven_day_rolling_a…, pruid

## g0133（1 列）
- 見出し：viral_load
- 例1 値：7.60740176644338 | 31.6767883565887 | 3.72290121308171 | 20.1196195738661 | 11.2294257268042
  - 同じ表の列：Date, Location, region, measureid, fractionid, seven_day_rolling_a…, pruid

## g0134（1 列）
- 見出し：seven_day_rolling_avg
- 例1 値：37.7028526162439 | 23.3099711585069 | 16.2217300971853 | 111.167388585294 | 62.7466657884242
  - 同じ表の列：Date, Location, region, measureid, fractionid, viral_load, pruid

## g0135（1 列）
- 見出し：pruid
- 例1 値：12 | 46 | 12 | 12 | 46
  - 同じ表の列：Date, Location, region, measureid, fractionid, viral_load, seven_day_rolling_a…

## g0136（1 列）
- 見出し：disease
- 例1 値：Gonorrhea | Chickenpox | Cholera | Hepatitis A | Giardiasis
  - 同じ表の列：year, number-of-reported-…, rate-per-100000-pop…

## g0137（1 列）
- 見出し：number-of-reported-cases
- 例1 値：6 | 9622 | 1 | 3744 | 7
  - 同じ表の列：disease, year, rate-per-100000-pop…

## g0138（1 列）
- 見出し：rate-per-100000-population
- 例1 値：0.02 | 0 | 9.54 | 44.54 | N/A
  - 同じ表の列：disease, year, number-of-reported-…

## g0139（1 列）
- 見出し：Fscl-yr_Ex-fin
- 例1 値：2024/2025 | 2024/2025 | 2024/2025 | 2024/2025 | 2024/2025
  - 同じ表の列：Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0140（1 列）
- 見出し：Min-code
- 例1 値：02 | 09 | 09 | 06 | 09
  - 同じ表の列：Fscl-yr_Ex-fin, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0141（1 列）
- 見出し：Min-portfolio_Portefeuille-min_eng
- 例1 値：Global Affairs | Agriculture and Agri-Food | Global Affairs | Global Affairs | Finance
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0142（1 列）
- 見出し：Min-portfolio_Portefeuille-min_fra
- 例1 値：Finances | Affaires mondiales | Conseil privé | Environnement et Changement climatique | Agriculture et Agroalimentaire
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0143（1 列）
- 見出し：Dept-nbr_No-min
- 例1 値：008 | 007 | 005 | 007 | 006
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0144（1 列）
- 見出し：Rpt-obj_Art-rppt
- 例1 値：048 | 042 | 048 | 082 | 040
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0145（1 列）
- 見出し：Rpt-obj_Art-rppt_eng
- 例1 値：Business Services | Other Services | Business Services | Special Fees and Services | Business Services
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_fra, Xpnd-current-yr_Dep…

## g0146（1 列）
- 見出し：Rpt-obj_Art-rppt_fra
- 例1 値：Services informatiques | Services commerciaux | Services informatiques | Services commerciaux | Services informatiques
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Xpnd-current-yr_Dep…

## g0147（1 列）
- 見出し：Xpnd-current-yr_Dep-ex-courant
- 例1 値：1734672 | 0 | 32850522 | 0 | 0
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra

## g0148（1 列）
- 見出し：Aggregate-payments_Versements-totalisant
- 例1 値：250000 | 245287 | 201356 | 498563 | 205250
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Rpt-obj_Art-rppt, Rpt-obj_Art-rppt_eng, Rpt-obj_Art-rppt_fra

## g0149（1 列）
- 見出し：Dashboard-date_Date-du-tableau-de-bord
- 例1 値：2022-01-31 | 2023-05-24 | 2022-05-25 | 2024-09-25 | 2021-02-15
  - 同じ表の列：Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0150（1 列）
- 見出し：Transactions-ready_Mouvements-prets
- 例1 値：354000 | 296000 | 475000 | 320000 | 489000
  - 同じ表の列：Dashboard-date_Date…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0151（1 列）
- 見出し：Total-financial-transactions-pending_Mouvements-financiers-e
- 例1 値：183000 | 340000 | 174000 | 288000 | 302000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0152（1 列）
- 見出し：Financial-transactions-pay-centre_Mouvements-financiers-cent
- 例1 値：251000 | 243000 | 261000 | 221000 | 214000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0153（1 列）
- 見出し：Financial-transactions-home-dept_Mouvements-financiers-min-o
- 例1 値：32000 | 32000 | 28000 | 28000 | 29000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0154（1 列）
- 見出し：Transactions-with-no-impact_Mouvements-sans-repercussion
- 例1 値：47500 | 97000 | 58000 | 60000 | 59000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-waitin…, Collective-agreemen…, Transactions-within…

## g0155（1 列）
- 見出し：Transactions-waiting-closed_Mouvements-devant-etre-fermes
- 例1 値：33000 | 58000 | 38000 | 33000 | 49000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Collective-agreemen…, Transactions-within…

## g0156（1 列）
- 見出し：Collective-agreements-transactions_Mouvements-conventions-co
- 例1 値：8500 | 5000 | 5000 | 18000 | 5000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Transactions-within…

## g0157（1 列）
- 見出し：Transactions-within-service-standards_Mouvements-conformants
- 例1 値：94000 | 87000 | 81000 | 78000 | 83000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…

## g0158（1 列）
- 見出し：Transactions-outside-service-standards-less-1yr_Mouvements-h
- 例1 値：37000 | 117000 | 124000 | 152000 | 120000
  - 同じ表の列：Dashboard-date_Date…, Transactions-ready_…, Total-financial-tra…, Financial-transacti…, Financial-transacti…, Transactions-with-n…, Transactions-waitin…, Collective-agreemen…

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
```
