# ラベル用シート 001 / 003

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Reporting date
- 例1 値：2015-09-30T00:00:00 | 2017-12-29T00:00:00 | 2016-09-30T00:00:00 | 2016-03-31T00:00:00 | 2019-12-31T00:00:00
  - 同じ表の列：buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0002（1 列）
- 見出し：buy_to_let_properties__floating_rate__standard_or_ltv_variab
- 例1 値：3.93 | 4.23 | 4.39 | 4.03 | 3.9
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0003（1 列）
- 見出し：buy_to_let_properties__floating_rate__tracker_mortgages__rat
- 例1 値：1.05 | 1.05 | 5.46 | 1.06 | 1.06
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0004（1 列）
- 見出し：buy_to_let_properties__fixed_rate__from_1_to_3_years__rates_
- 例1 値：4.84 | 4.27 | 4.35 | 4.34 | 3.36
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0005（1 列）
- 見出し：buy_to_let_properties__fixed_rate__over_3_years__rates_on_ou
- 例1 値：4.43 | 3.75 | 2.78 | 4.25 | 2.4
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0006（1 列）
- 見出し：principal_dwelling_houses__floating_rate__standard_or_ltv_va
- 例1 値：4.11 | 4.26 | 3.5 | 3.5 | 3.94
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0007（1 列）
- 見出し：principal_dwelling_houses__floating_rate__tracker_mortgages_
- 例1 値：1.07 | 5.7 | 1.07 | 3.23 | 1.09
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0008（1 列）
- 見出し：principal_dwelling_houses__floating_rate__up_to_1_year_fixed
- 例1 値：3.51 | 3.49 | 3.41 | 4.05 | 2.92
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0009（1 列）
- 見出し：principal_dwelling_houses__fixed_rate__from_1_to_3_years__ra
- 例1 値：2.91 | 2.72 | 3.04 | 2.66 | 2.92
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0010（1 列）
- 見出し：principal_dwelling_houses__fixed_rate__over_3_years__rates_o
- 例1 値：2.75 | 2.71 | 3.83 | 3.34 | 3.12
  - 同じ表の列：Reporting date, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, buy_to_let_properti…, principal_dwelling_…, principal_dwelling_…, principal_dwelling_…

## g0011（3 列）
- 見出し：COUNTY
- 例1 値：MONAGHAN | CLARE | WATERFORD | CARLOW | WEXFORD
  - 同じ表の列：CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN
- 例2 値：Mayo | Clare | Mayo | Mayo | Leitrim
  - 同じ表の列：Report Date, Area, measurement_unit__h…, Decision, Decision Date, Latest Appeal Date, GPC Category, eis_eia_required

## g0012（1 列）
- 見出し：CENSUS_YEAR
- 例1 値：1970-01-01T00:33:40 | 1970-01-01T00:33:40 | 1970-01-01T00:33:40 | 1970-01-01T00:33:40 | 1970-01-01T00:33:40
  - 同じ表の列：COUNTY, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0013（1 列）
- 見出し：NO_OF_HERD_NUMBERS
- 例1 値：1321 | 2080 | 1185 | 832 | 1309
  - 同じ表の列：COUNTY, CENSUS_YEAR, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0014（1 列）
- 見出し：FLOCKS_WITH_SHEEP_IND
- 例1 値：1804 | 6167 | 256 | 4146 | 2521
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0015（1 列）
- 見出し：FLOCKS_WITH_TOTAL_SHEEP_CALC
- 例1 値：434 | 235 | 971 | 540 | 597
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0016（1 列）
- 見出し：BREEDING_EWES_TOTAL
- 例1 値：18469 | 53977 | 105389 | 30131 | 103456
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0017（1 列）
- 見出し：BREEDING_RAMS_TOTAL
- 例1 値：6332 | 2985 | 2683 | 9356 | 3613
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0018（1 列）
- 見出し：OTHER_SHEEP_TOTAL
- 例1 値：157372 | 21426 | 30878 | 41049 | 14706
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, TOTAL_SHEEP_MOUNTAIN

## g0019（1 列）
- 見出し：TOTAL_SHEEP_MOUNTAIN
- 例1 値：8363 | 2633 | 4496 | 47578 | 31778
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL

## g0020（1 列）
- 見出し：TOTAL_SHEEP_CALC
- 例1 値：23036 | 168678 | 440784 | 84576 | 106963
  - 同じ表の列：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_I…, FLOCKS_WITH_TOTAL_S…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL

## g0021（1 列）
- 見出し：Report Date
- 例1 値：2021-05-05T00:00:00 | 2021-05-28T00:00:00 | 2021-05-05T00:00:00 | 2021-05-04T00:00:00 | 2021-05-14T00:00:00
  - 同じ表の列：County, Area, measurement_unit__h…, Decision, Decision Date, Latest Appeal Date, GPC Category, eis_eia_required

## g0022（1 列）
- 見出し：Area
- 例1 値：5.91 | 5.91 | 12.89 | 10.49 | 10.14
  - 同じ表の列：Report Date, County, measurement_unit__h…, Decision, Decision Date, Latest Appeal Date, GPC Category, eis_eia_required

## g0023（1 列）
- 見出し：measurement_unit__ha_
- 例1 値：Hectare | Hectare | Hectare | Hectare | Hectare
  - 同じ表の列：Report Date, County, Area, Decision, Decision Date, Latest Appeal Date, GPC Category, eis_eia_required

## g0024（1 列）
- 見出し：Decision
- 例1 値：Approved | Refused | Approved | Approved | Approved
  - 同じ表の列：Report Date, County, Area, measurement_unit__h…, Decision Date, Latest Appeal Date, GPC Category, eis_eia_required

## g0025（1 列）
- 見出し：Decision Date
- 例1 値：2021-04-09T00:00:00 | 2021-04-29T00:00:00 | 2021-04-30T00:00:00 | 2021-05-25T00:00:00 | 2021-05-04T00:00:00
  - 同じ表の列：Report Date, County, Area, measurement_unit__h…, Decision, Latest Appeal Date, GPC Category, eis_eia_required

## g0026（1 列）
- 見出し：Latest Appeal Date
- 例1 値：2021-05-19T00:00:00 | 2021-05-19T00:00:00 | 2021-05-14T00:00:00 | 2021-06-18T00:00:00 | 2021-05-17T00:00:00
  - 同じ表の列：Report Date, County, Area, measurement_unit__h…, Decision, Decision Date, GPC Category, eis_eia_required

## g0027（1 列）
- 見出し：GPC Category
- 例1 値：Mixed Conifer/Broadleaf | Mixed Conifer/Broadleaf | Mixed Conifer/Broadleaf | Mixed Conifer/Broadleaf | Mixed Conifer/Broadleaf
  - 同じ表の列：Report Date, County, Area, measurement_unit__h…, Decision, Decision Date, Latest Appeal Date, eis_eia_required

## g0028（1 列）
- 見出し：eis_eia_required
- 例1 値：No | No | No | No | No
  - 同じ表の列：Report Date, County, Area, measurement_unit__h…, Decision, Decision Date, Latest Appeal Date, GPC Category

## g0029（10 列）
- 見出し：YEAR
- 例1 値：2020 | 2015 | 2016 | 2015 | 2016
  - 同じ表の列：LOCATION, TOTAL_SHEEP
- 例2 値：2010 | 2004 | 2007 | 2011 | 2001
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), C02199V02655, Sex, UNIT, VALUE

## g0030（1 列）
- 見出し：LOCATION
- 例1 値：Doonbeg | Vartry | Ilen | Ilen | Ilen
  - 同じ表の列：YEAR, TOTAL_SHEEP

## g0031（1 列）
- 見出し：TOTAL_SHEEP
- 例1 値：26176 | 9269 | 96850 | 113461 | 23412
  - 同じ表の列：YEAR, LOCATION

## g0032（3 列）
- 見出し：STATISTIC
- 例1 値：EDA36 | EDA36 | EDA36 | EDA36 | EDA36
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex, UNIT, VALUE
- 例2 値：EDA96 | EDA96 | EDA96 | EDA96 | EDA96
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex, C02505V03033, Details of Results, UNIT

## g0033（1 列）
- 見出し：Statistic
- 例1 値：Percentage of persons aged 20-24 years … | Percentage of persons aged 20-24 years … | Percentage of persons aged 20-24 years … | Percentage of persons aged 20-24 years … | Percentage of persons aged 20-24 years …
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, UNIT, VALUE

## g0034（2 列）
- 見出し：TLIST(A1)
- 例1 値：1999 | 2001 | 2002 | 2008 | 2006
  - 同じ表の列：STATISTIC, Statistic, Year, C02199V02655, Sex, UNIT, VALUE
- 例2 値：2008 | 2013 | 2013 | 2002 | 2000
  - 同じ表の列：STATISTIC, Statistic, Year, C02199V02655, Sex, C02505V03033, Details of Results, UNIT

## g0035（2 列）
- 見出し：C02199V02655
- 例1 値：2 | 1 | 1 | 2 | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, UNIT, VALUE
- 例2 値：1 | - | 2 | - | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, C02505V03033, Details of Results, UNIT

## g0036（1 列）
- 見出し：Sex
- 例1 値：Female | Both sexes | Male | Female | Female
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, UNIT, VALUE

## g0037（1 列）
- 見出し：UNIT
- 例1 値：% | % | % | % | %
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, VALUE

## g0038（1 列）
- 見出し：VALUE
- 例1 値：78.4 | 72.9 | 86.2 | 87.3 | 81.5
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, UNIT

## g0039（1 列）
- 見出し：Statistic
- 例1 値：Leaving Certificate Applied Results | Leaving Certificate Applied Results | Leaving Certificate Applied Results | Leaving Certificate Applied Results | Leaving Certificate Applied Results
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, C02505V03033, Details of Results, UNIT

## g0040（1 列）
- 見出し：Sex
- 例1 値：Male | Female | Female | Female | Female
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C02505V03033, Details of Results, UNIT

## g0041（1 列）
- 見出し：C02505V03033
- 例1 値：16 | 15 | 15 | 16 | 15
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, Details of Results, UNIT

## g0042（1 列）
- 見出し：Details of Results
- 例1 値：Candidates who received record of credi… | Candidates who received distinctions | All candidates | Candidates who received distinctions | Candidates who received passes
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02505V03033, UNIT

## g0043（4 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02505V03033, Details of Results
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, VALUE

## g0044（5 列）
- 見出し：VALUE
- 例1 値：216 | 238 | 642 | 243 | 1554
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02505V03033, Details of Results
- 例2 値：82217 | 62639 | 68614 | 41233 | 77090
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, FLAG

## g0045（2 列）
- 見出し：STATISTIC
- 例1 値：STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE
  - 同じ表の列：Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT, VALUE
- 例2 値：NURSES | NURSES | NURSES | NURSES | NURSES
  - 同じ表の列：Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0046（1 列）
- 見出し：Statistic Label
- 例1 値：Nurses by type of training (first quali… | Nurses by type of training (first quali… | Nurses by type of training (first quali… | Nurses by type of training (first quali… | Nurses by type of training (first quali…
  - 同じ表の列：STATISTIC, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT, VALUE

## g0047（1 列）
- 見出し：TRNGTYPE
- 例1 値：FOREIGN | FOREIGN | FOREIGN | FOREIGN | FOREIGN
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Type of training, QUALCOU, UNIT, VALUE

## g0048（1 列）
- 見出し：Type of training
- 例1 値：Foreign trained | Foreign trained | Foreign trained | Foreign trained | Foreign trained
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, QUALCOU, UNIT, VALUE

## g0049（1 列）
- 見出し：QUALCOU
- 例1 値：COM | RWA | BFA | TUV | KNA
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, UNIT, VALUE

## g0050（1 列）
- 見出し：VALUE
- 例1 値：. | . | . | 0 | 0
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT

## g0051（2 列）
- 見出し：FLAG
- 例1 値：S | S | S | S | S
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT
- 例2 値：D | D | D | D | D
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0052（1 列）
- 見出し：Statistic Label
- 例1 値：Nurses | Nurses | Nurses | Nurses | Nurses
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0053（1 列）
- 見出し：MEASURE
- 例1 値：LICENSENURSE | LICENSENURSE | LICENSENURSE | LICENSENURSE | PRACNURSE
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Measure, UNIT, VALUE, FLAG

## g0054（1 列）
- 見出し：Measure
- 例1 値：Nurses licensed to practice | Nurses licensed to practice | Nurses licensed to practice | Nurses licensed to practice | Nurses licensed to practice
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, UNIT, VALUE, FLAG

## g0055（1 列）
- 見出し：Flag
- 例1 値：Deviation from definition | Deviation from definition | Deviation from definition | Deviation from definition | Deviation from definition
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0056（1 列）
- 見出し：STATISTIC
- 例1 値：HSQ08C3 | HSQ08C3 | HSQ08C3 | HSQ08C3 | HSQ08C1
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C02350V02827, House Type New or S…, UNIT, VALUE

## g0057（1 列）
- 見出し：Statistic
- 例1 値：Value of House Loans Approved | Number of House Loans Paid | Value of House Loans Approved | Number of House Loans Paid | Number of House Loans Paid
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02350V02827, House Type New or S…, UNIT, VALUE

## g0058（1 列）
- 見出し：TLIST(Q1)
- 例1 値：20132 | 20114 | 20014 | 19924 | 20022
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02350V02827, House Type New or S…, UNIT, VALUE

## g0059（1 列）
- 見出し：Quarter
- 例1 値：1995Q2 | 1986Q4 | 2002Q2 | 1995Q4 | 2005Q3
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02350V02827, House Type New or S…, UNIT, VALUE

## g0060（1 列）
- 見出し：C02350V02827
- 例1 値：2 | 1 | 1 | 1 | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, House Type New or S…, UNIT, VALUE

## g0061（1 列）
- 見出し：House Type New or Second hand
- 例1 値：Second-hand houses | Second-hand houses | Second-hand houses | Second-hand houses | New houses
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02350V02827, UNIT, VALUE

## g0062（1 列）
- 見出し：UNIT
- 例1 値：Number | Euro Million | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02350V02827, House Type New or S…, VALUE

## g0063（1 列）
- 見出し：VALUE
- 例1 値：11074 | 187.8 | 1395 | 8210 | 168.8
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02350V02827, House Type New or S…, UNIT

## g0064（1 列）
- 見出し：Statistic
- 例1 値：ESB Connections | ESB Connections | ESB Connections | ESB Connections | ESB Connections
  - 同じ表の列：STATISTIC, TLIST(M1), Month, C02196V02652, State, UNIT, VALUE

## g0065（1 列）
- 見出し：TLIST(M1)
- 例1 値：198610 | 199810 | 200707 | 199005 | 201107
  - 同じ表の列：STATISTIC, Statistic, Month, C02196V02652, State, UNIT, VALUE

## g0066（1 列）
- 見出し：Month
- 例1 値：1981M09 | 2015M08 | 2005M03 | 2006M08 | 1976M11
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), C02196V02652, State, UNIT, VALUE

## g0067（1 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, State, UNIT, VALUE

## g0068（1 列）
- 見出し：State
- 例1 値：State | State | State | State | State
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C02196V02652, UNIT, VALUE

## g0069（3 列）
- 見出し：Time
- 例1 値：13:00 | 06:00 | 04:00 | 02:00 | 11:00
  - 同じ表の列：Temperature oC, wind_speed_km_h, rainfall_mm_h, Pressure hPa
- 例2 値：21:00 | 8:00 | 15:00 | 1:00 | 19:00
  - 同じ表の列：Site, Date, TempC

## g0070（1 列）
- 見出し：Temperature oC
- 例1 値：7 | 7 | 8 | 9 | 9
  - 同じ表の列：Time, wind_speed_km_h, rainfall_mm_h, Pressure hPa

## g0071（1 列）
- 見出し：wind_speed_km_h
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Time, Temperature oC, rainfall_mm_h, Pressure hPa

## g0072（1 列）
- 見出し：rainfall_mm_h
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, Pressure hPa

## g0073（1 列）
- 見出し：Pressure hPa
- 例1 値：998 | 997 | 998 | 998 | 998
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, rainfall_mm_h

## g0074（1 列）
- 見出し：Station
- 例1 値：Dunsany | Claremorris | Markree Castle | Gurteen | Ballyhaise
  - 同じ表の列：temperature____c_, Weather, wind_speed__kts_, Wind Direction, humidity____, rainfall__mm_, pressure__hpa_

## g0075（1 列）
- 見出し：temperature____c_
- 例1 値：9 | 10 | 12 | 10 | 11
  - 同じ表の列：Station, Weather, wind_speed__kts_, Wind Direction, humidity____, rainfall__mm_, pressure__hpa_

## g0076（1 列）
- 見出し：Weather
- 例1 値：- | - | - | - | Rain/Drizzle
  - 同じ表の列：Station, temperature____c_, wind_speed__kts_, Wind Direction, humidity____, rainfall__mm_, pressure__hpa_

## g0077（1 列）
- 見出し：wind_speed__kts_
- 例1 値：12 | 10 | 10 | 06 | 22
  - 同じ表の列：Station, temperature____c_, Weather, Wind Direction, humidity____, rainfall__mm_, pressure__hpa_

## g0078（1 列）
- 見出し：Wind Direction
- 例1 値：- | SW | E | SE | S
  - 同じ表の列：Station, temperature____c_, Weather, wind_speed__kts_, humidity____, rainfall__mm_, pressure__hpa_

## g0079（1 列）
- 見出し：humidity____
- 例1 値：76 | 97 | 79 | 87 | 82
  - 同じ表の列：Station, temperature____c_, Weather, wind_speed__kts_, Wind Direction, rainfall__mm_, pressure__hpa_

## g0080（1 列）
- 見出し：rainfall__mm_
- 例1 値：0.01 | 3.0 | 2.1 | 0.1 | 0.5
  - 同じ表の列：Station, temperature____c_, Weather, wind_speed__kts_, Wind Direction, humidity____, pressure__hpa_

## g0081（1 列）
- 見出し：pressure__hpa_
- 例1 値：995 | 998 | 995 | 995 | 996
  - 同じ表の列：Station, temperature____c_, Weather, wind_speed__kts_, Wind Direction, humidity____, rainfall__mm_

## g0082（1 列）
- 見出し：SRN
- 例1 値：14900P | 19794V | 20384J | 18911R | 01840C
  - 同じ表の列：County, School Year, School Type, Class ID, Class Type

## g0083（1 列）
- 見出し：School Year
- 例1 値：26/27 | 26/27 | 26/27 | 26/27 | 26/27
  - 同じ表の列：County, SRN, School Type, Class ID, Class Type

## g0084（1 列）
- 見出し：School Type
- 例1 値：Primary | Primary | Primary | Post Primary | Primary
  - 同じ表の列：County, SRN, School Year, Class ID, Class Type

## g0085（1 列）
- 見出し：Class ID
- 例1 値：44,415.00 | 44,400.00 | 45,062.00 | 45,002.00 | 44,780.00
  - 同じ表の列：County, SRN, School Year, School Type, Class Type

## g0086（1 列）
- 見出し：Class Type
- 例1 値：Autism/Autistic Spectrum Disorders | Autism/Autistic Spectrum Disorders | Autism/Autistic Spectrum Disorders | Autism Inclusion Class | Autism/Autistic Spectrum Disorders
  - 同じ表の列：County, SRN, School Year, School Type, Class ID

## g0087（1 列）
- 見出し：RegionID
- 例1 値：18 | 22 | 19 | 21 | 20
  - 同じ表の列：AreaID, Area, Year, Jan, Feb, Mar, Apr, May

## g0088（1 列）
- 見出し：AreaID
- 例1 値：12 | 7 | 2 | 17 | 14
  - 同じ表の列：RegionID, Area, Year, Jan, Feb, Mar, Apr, May

## g0089（1 列）
- 見出し：Area
- 例1 値：Cavan Monaghan | Cork | Carlow Kilkenny South Tipperary | Sligo Leitrim West Cavan | Dublin South West Kildare West Wicklow
  - 同じ表の列：RegionID, AreaID, Year, Jan, Feb, Mar, Apr, May

## g0090（1 列）
- 見出し：Jan
- 例1 値：24 | 1 | 6 | 2 | 12
  - 同じ表の列：RegionID, AreaID, Area, Year, Feb, Mar, Apr, May

## g0091（1 列）
- 見出し：Feb
- 例1 値：2 | 24 | 11 | 3 | 4
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Mar, Apr, May

## g0092（1 列）
- 見出し：Mar
- 例1 値：8 | 2 | 15 | 1 | 7
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Apr, May

## g0093（1 列）
- 見出し：Apr
- 例1 値：4 | 1 | 3 | 1 | 26
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, May

## g0094（1 列）
- 見出し：May
- 例1 値：6 | 27 | 15 | 10 | 6
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0095（1 列）
- 見出し：Jun
- 例1 値：4 | 5 | 1 | 1 | 7
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0096（2 列）
- 見出し：X
- 例1 値：-6.35679546876853 | -6.26115526161955 | -6.09347011040539 | -6.2007658046913 | -6.52802865997777
  - 同じ表の列：Y, ID, RPS_Number, Structure, Townland, Image, ImageFile, OBJECTID
- 例2 値：-6.03481103418796 | -6.03976627830593 | -6.03971026880467 | -6.03965488004302 | -6.04942870284893
  - 同じ表の列：Y, ID, RPS_Number, Location, Structure, OBJECTID

## g0097（2 列）
- 見出し：Y
- 例1 値：52.9669693294653 | 52.9427215747741 | 53.1943810560585 | 53.0027185440083 | 53.1200965111648
  - 同じ表の列：X, ID, RPS_Number, Structure, Townland, Image, ImageFile, OBJECTID
- 例2 値：52.9809453585292 | 52.9811088112459 | 52.9773584529007 | 52.9777885357153 | 52.9776031837196
  - 同じ表の列：X, ID, RPS_Number, Location, Structure, OBJECTID

## g0098（4 列）
- 見出し：ID
- 例1 値：192 | 518 | 145 | 286 | 125
  - 同じ表の列：X, Y, RPS_Number, Structure, Townland, Image, ImageFile, OBJECTID
- 例2 値：100 | 73 | 61 | 109 | 3
  - 同じ表の列：RPS_Number, Location, OBJECTID, SHAPE__Area, SHAPE__Length

## g0099（1 列）
- 見出し：RPS_Number
- 例1 値：21-09 | 09-03 | 15-13 | 08-15 | 31-01
  - 同じ表の列：X, Y, ID, Structure, Townland, Image, ImageFile, OBJECTID

## g0100（1 列）
- 見出し：Structure
- 例1 値：Gate-lodge | Pair of semi-detached houses | House | Old Mining Office | House
  - 同じ表の列：X, Y, ID, RPS_Number, Townland, Image, ImageFile, OBJECTID

## g0101（1 列）
- 見出し：Townland
- 例1 値：Manger Td | Coolattin Td | Bellevue Demesne | Castlekevin Td | Whitefield Td
  - 同じ表の列：X, Y, ID, RPS_Number, Structure, Image, ImageFile, OBJECTID

## g0102（1 列）
- 見出し：Image
- 例1 値：Images\277.jpg | Images\474.jpg | Images\370.jpg | Images\193.jpg | Images\429.jpg
  - 同じ表の列：X, Y, ID, RPS_Number, Structure, Townland, ImageFile, OBJECTID

## g0103（1 列）
- 見出し：ImageFile
- 例1 値：416.jpg | 460.jpg | 306.jpg | 103.jpg | 107.jpg
  - 同じ表の列：X, Y, ID, RPS_Number, Structure, Townland, Image, OBJECTID

## g0104（3 列）
- 見出し：OBJECTID
- 例1 値：145 | 184 | 224 | 168 | 563
  - 同じ表の列：X, Y, ID, RPS_Number, Structure, Townland, Image, ImageFile
- 例2 値：122 | 113 | 72 | 84 | 141
  - 同じ表の列：ID, RPS_Number, Location, SHAPE__Area, SHAPE__Length

## g0105（1 列）
- 見出し：RPS_Number
- 例1 値：B01 | B41 | B41 | B101 | B54
  - 同じ表の列：ID, Location, OBJECTID, SHAPE__Area, SHAPE__Length

## g0106（1 列）
- 見出し：Location
- 例1 値：Vevay Road | Florence Road | Dublin Road | Kilbride | Quinsborough Road
  - 同じ表の列：ID, RPS_Number, OBJECTID, SHAPE__Area, SHAPE__Length

## g0107（1 列）
- 見出し：SHAPE__Area
- 例1 値：228.192321777344 | 0.33953857421875 | 129.962860107422 | 114.5380859375 | 137.843963623047
  - 同じ表の列：ID, RPS_Number, Location, OBJECTID, SHAPE__Length

## g0108（1 列）
- 見出し：SHAPE__Length
- 例1 値：55.8498364889542 | 134.658667128441 | 94.7187627713687 | 59.3995046627256 | 63.4758266917925
  - 同じ表の列：ID, RPS_Number, Location, OBJECTID, SHAPE__Area

## g0109（1 列）
- 見出し：RPS_Number
- 例1 値：WTC - RPS 4 | WTC - RPS 19 | WTC - RPS 22 | WTC - RPS 28 | WTC - RPS 21
  - 同じ表の列：X, Y, ID, Location, Structure, OBJECTID

## g0110（1 列）
- 見出し：Location
- 例1 値：Saint Dominic's Wing, Dominican Convent… | Saint Nathi’s / Round Mount, Brickfield… | Wicklow Parish Church of rieland, Churc… | Brickfield Lane, Wicklow Town | Wicklow Parish COI Graveyard, Church Hi…
  - 同じ表の列：X, Y, ID, RPS_Number, Structure, OBJECTID

## g0111（1 列）
- 見出し：Structure
- 例1 値：Piers and gate | Abbey ruin | Convent | Convent Chapel | The Capstan
  - 同じ表の列：X, Y, ID, RPS_Number, Location, OBJECTID

## g0112（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：F8-10-AL-00066 | F8-10-AL-00011 | F8-10-AL-00007 | F8-10-AL-00068 | F8-10-AL-00032
  - 同じ表の列：Region - Region, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0113（1 列）
- 見出し：Region - Region
- 例1 値：ONTARIO | ONTARIO | ONTARIO | ONTARIO | ONTARIO
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0114（3 列）
- 見出し：Function
- 例1 値：Import | Import | Import | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：Domestic | Import | Unknown | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test

## g0115（3 列）
- 見出し：Fonction
- 例1 値：Domestique | Domestique | Importé | Importé | Importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Origin, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：Importé | Importé | Domestique | Inconnu | Importé
  - 同じ表の列：Sample No. - No. d'…, Function, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test

## g0116（3 列）
- 見出し：Origin
- 例1 値：UNKNOWN | PAKISTAN | PAKISTAN | JAPAN | UNITED STATES
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：CANADA | CANADA | CANADA | UNITED STATES | UNITED STATES
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…, Type of Test

## g0117（2 列）
- 見出し：Origine
- 例1 値：ÉTATS-UNIS | JAPON | ÉTATS-UNIS | PAKISTAN | SINGAPOUR
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…
- 例2 値：CANADA | CANADA | CANADA | ÉTATS-UNIS | ÉTATS-UNIS
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…, Type of Test

## g0118（1 列）
- 見出し：Product
- 例1 値：Flavour Packet - Dried | Flavour Packet - Dried | Flavour Packet - Dried | Flavour Packet - Dried | Flavour Packet - Dried
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…

## g0119（1 列）
- 見出し：Produit
- 例1 値：Paquet de saveurs - séchés | Paquet de saveurs - séchés | Paquet de saveurs - séchés | Paquet de saveurs - séchés | Paquet de saveurs - séchés
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…

## g0120（3 列）
- 見出し：Date Sampled - Date d'echantillonage
- 例1 値：2011-01-11 | 2011-01-11 | 2011-01-11 | 2011-01-11 | 2011-01-11
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit
- 例2 値：2011-08-08 | 2011-07-10 | 2011-07-17 | 2012-01-18 | 2012-01-27
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Type of Test

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
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
