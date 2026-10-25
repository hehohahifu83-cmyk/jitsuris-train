# ラベル用シート 005 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：Reclaimed
- 例1 値：61 | 109 | 83 | 81 | 76
  - 同じ表の列：Date, Adopted

## g0482（1 列）
- 見出し：DATE
- 例1 値：2024-03-28T00:00:00 | 2020-06-30T00:00:00 | 2025-09-30T00:00:00 | 2022-12-30T00:00:00 | 2020-09-30T00:00:00
  - 同じ表の列：QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0483（1 列）
- 見出し：QUARTER
- 例1 値：2022 Q3 | 2023 Q2 | 2025 Q4 | 2025 Q3 | 2023 Q4
  - 同じ表の列：DATE, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0484（1 列）
- 見出し：STATISTIC
- 例1 値：Q:IE:S:S129:A50:T:1:W0:S1:_T:EUR | Q:IE:S:S129:A62:T:1:W0:S1:_T:EUR | Q:IE:S:S129:A624:T:1:W0:S1:_T:EUR | Q:IE:S:S129:A625:T:1:W0:S1:_T:EUR | Q:IE:S:S129:A62:T:1:W0:S1:_T:EUR
  - 同じ表の列：DATE, QUARTER, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0485（1 列）
- 見出し：ASSET_LIABILITY
- 例1 値：Asset - Equity | Asset - Equity fund shares/units | Liability - Pension entitlements - defi… | Asset - Mixed fund shares/units | Asset - Bond fund shares/units
  - 同じ表の列：DATE, QUARTER, STATISTIC, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0486（1 列）
- 見出し：MATURITY
- 例1 値：All original maturities | All original maturities | All original maturities | All original maturities | All original maturities
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0487（1 列）
- 見出し：COUNTERPART_AREA
- 例1 値：World (all entities, including referenc… | World (all entities, including referenc… | World (all entities, including referenc… | Other Euro area member states (all coun… | World (all entities, including referenc…
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…, OBSERVATION

## g0488（1 列）
- 見出し：COUNTERPART_SECTOR
- 例1 値：Total economy | Total economy | Total economy | Total economy | Total economy
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, ASSET_LIABILITY_CUR…, OBSERVATION

## g0489（1 列）
- 見出し：ASSET_LIABILITY_CURRENCY
- 例1 値：All currencies | All currencies | All currencies | All currencies | All currencies
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, OBSERVATION

## g0490（1 列）
- 見出し：OBSERVATION
- 例1 値：12950.59 | 36856.69 | 129124.5 | 43396.93 | 1667.64
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…

## g0491（1 列）
- 見出し：OBSERVATION_CURRENCY
- 例1 値：Euro | Euro | Euro | Euro | Euro
  - 同じ表の列：DATE, QUARTER, STATISTIC, ASSET_LIABILITY, MATURITY, COUNTERPART_AREA, COUNTERPART_SECTOR, ASSET_LIABILITY_CUR…

## g0492（1 列）
- 見出し：PUBLISHED DATE
- 例1 値：2021-05-24T00:00:00 | 2021-05-05T00:00:00 | 2021-05-10T00:00:00 | 2021-05-26T00:00:00 | 2021-05-17T00:00:00
  - 同じ表の列：submission_observat…, SCHEME, ded_s_, DIGITISED AREA, measurement_unit__h…, county_s_, CATEGORY

## g0493（1 列）
- 見出し：submission_observation_date
- 例1 値：2021-06-27T00:00:00 | 2021-06-18T00:00:00 | 2021-06-25T00:00:00 | 2021-06-23T00:00:00 | 2021-06-11T00:00:00
  - 同じ表の列：PUBLISHED DATE, SCHEME, ded_s_, DIGITISED AREA, measurement_unit__h…, county_s_, CATEGORY

## g0494（1 列）
- 見出し：SCHEME
- 例1 値：Afforestation | Afforestation | Afforestation | Afforestation | Afforestation
  - 同じ表の列：PUBLISHED DATE, submission_observat…, ded_s_, DIGITISED AREA, measurement_unit__h…, county_s_, CATEGORY

## g0495（1 列）
- 見出し：ded_s_
- 例1 値：ARDBRACCAN | KILMACTRANNY | MOTHELL | RODANSTOWN | KILKELLY
  - 同じ表の列：PUBLISHED DATE, submission_observat…, SCHEME, DIGITISED AREA, measurement_unit__h…, county_s_, CATEGORY

## g0496（1 列）
- 見出し：DIGITISED AREA
- 例1 値：4.44 | 0.38 | 8.98 | 2.38 | 10.02
  - 同じ表の列：PUBLISHED DATE, submission_observat…, SCHEME, ded_s_, measurement_unit__h…, county_s_, CATEGORY

## g0497（1 列）
- 見出し：measurement_unit__ha_
- 例1 値：Hectare | Hectare | Hectare | Hectare | Hectare
  - 同じ表の列：PUBLISHED DATE, submission_observat…, SCHEME, ded_s_, DIGITISED AREA, county_s_, CATEGORY

## g0498（1 列）
- 見出し：county_s_
- 例1 値：Monaghan | Sligo | Tipperary | Meath | Leitrim
  - 同じ表の列：PUBLISHED DATE, submission_observat…, SCHEME, ded_s_, DIGITISED AREA, measurement_unit__h…, CATEGORY

## g0499（1 列）
- 見出し：CATEGORY
- 例1 値：Agroforestry | Broadleaf | Broadleaf | Mixed Conifer/Broadleaf | Mixed Conifer/Broadleaf
  - 同じ表の列：PUBLISHED DATE, submission_observat…, SCHEME, ded_s_, DIGITISED AREA, measurement_unit__h…, county_s_

## g0500（1 列）
- 見出し：BIRTH_YEAR
- 例1 値：2016 | 2016 | 2016 | 2016 | 2016
  - 同じ表の列：COUNTY_ORIGIN, BIRTH_MONTH, CALF_BREED_TYPE, TOTAL_BIRTH

## g0501（1 列）
- 見出し：COUNTY_ORIGIN
- 例1 値：GALWAY | DUBLIN | KERRY | DUBLIN | LEITRIM
  - 同じ表の列：BIRTH_YEAR, BIRTH_MONTH, CALF_BREED_TYPE, TOTAL_BIRTH

## g0502（1 列）
- 見出し：BIRTH_MONTH
- 例1 値：APR | NOV | JUN | OCT | JUN
  - 同じ表の列：BIRTH_YEAR, COUNTY_ORIGIN, CALF_BREED_TYPE, TOTAL_BIRTH

## g0503（1 列）
- 見出し：CALF_BREED_TYPE
- 例1 値：BEEF | DAIRY | DAIRY | BEEF | DAIRY
  - 同じ表の列：BIRTH_YEAR, COUNTY_ORIGIN, BIRTH_MONTH, TOTAL_BIRTH

## g0504（1 列）
- 見出し：TOTAL_BIRTH
- 例1 値：226 | 851 | 127 | 11887 | 217
  - 同じ表の列：BIRTH_YEAR, COUNTY_ORIGIN, BIRTH_MONTH, CALF_BREED_TYPE

## g0505（3 列）
- 見出し：STATISTIC
- 例1 値：EDA54 | EDA54 | EDA54 | EDA54 | EDA54
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex, C02462V02980, Leavers, UNIT
- 例2 値：HSQ11 | HSQ11 | HSQ11 | HSQ11 | HSQ11
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C01947V02657, Local Authority, C02341V02815, Housing Sector, UNIT

## g0506（1 列）
- 見出し：Statistic
- 例1 値：Leavers from Mainstream Classes in Nati… | Leavers from Mainstream Classes in Nati… | Leavers from Mainstream Classes in Nati… | Leavers from Mainstream Classes in Nati… | Leavers from Mainstream Classes in Nati…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, C02462V02980, Leavers, UNIT

## g0507（5 列）
- 見出し：TLIST(A1)
- 例1 値：2018 | 2015 | 2012 | 2018 | 2013
  - 同じ表の列：STATISTIC, Statistic, Year, C02199V02655, Sex, C02462V02980, Leavers, UNIT
- 例2 値：2004 | 2006 | 2002 | 2007 | 2016
  - 同じ表の列：STATISTIC, Statistic, Year, C02348V02824, Teacher Size of Sch…, UNIT, VALUE

## g0508（1 列）
- 見出し：C02199V02655
- 例1 値：1 | 1 | 1 | 2 | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, C02462V02980, Leavers, UNIT

## g0509（1 列）
- 見出し：Sex
- 例1 値：Both sexes | Male | Female | Male | Male
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C02462V02980, Leavers, UNIT

## g0510（1 列）
- 見出し：C02462V02980
- 例1 値：1 | 8 | 2 | 2 | 6
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, Leavers, UNIT

## g0511（1 列）
- 見出し：Leavers
- 例1 値：All leavers | Leavers (excluding emigrants) who did n… | All leavers | Leavers (excluding emigrants) who did n… | Leavers who went to a secondary, vocati…
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02462V02980, UNIT

## g0512（9 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02462V02980, Leavers
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02348V02824, Teacher Size of Sch…, VALUE

## g0513（10 列）
- 見出し：VALUE
- 例1 値：213 | 41452 | 19619 | 280 | 2223
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02462V02980, Leavers
- 例2 値：3124 | 62 | 22833 | 32290 | 12553
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02348V02824, Teacher Size of Sch…, UNIT

## g0514（3 列）
- 見出し：STATISTIC
- 例1 値：EDA49C1 | EDA49C1 | EDA49C2 | EDA49C1 | EDA49C1
  - 同じ表の列：Statistic, TLIST(A1), Year, C02348V02824, Teacher Size of Sch…, UNIT, VALUE
- 例2 値：ED114C01 | ED114C01 | ED114C01 | ED114C01 | ED114C01
  - 同じ表の列：Statistic, TLIST(A1), Year, C02445V02957, Class Size, C02446V02958, Grade Structure, UNIT

## g0515（1 列）
- 見出し：Statistic
- 例1 値：National Schools | Pupils in National Schools | National Schools | National Schools | Pupils in National Schools
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02348V02824, Teacher Size of Sch…, UNIT, VALUE

## g0516（1 列）
- 見出し：C02348V02824
- 例1 値：04 | 10 | 08 | 02 | 101
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Teacher Size of Sch…, UNIT, VALUE

## g0517（1 列）
- 見出し：Teacher Size of School
- 例1 値：19 teachers | 19 teachers | 16 teachers | 16 teachers | 14.5 teachers
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02348V02824, UNIT, VALUE

## g0518（3 列）
- 見出し：Statistic
- 例1 値：Mainstream Classes | Mainstream Classes | Mainstream Classes | Mainstream Classes | Mainstream Classes
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02445V02957, Class Size, C02446V02958, Grade Structure, UNIT
- 例2 値：ESB Connections | ESB Connections | ESB Connections | ESB Connections | ESB Connections
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C01947V02657, Local Authority, C02341V02815, Housing Sector, UNIT

## g0519（1 列）
- 見出し：C02445V02957
- 例1 値：- | 6 | 1 | - | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Class Size, C02446V02958, Grade Structure, UNIT

## g0520（1 列）
- 見出し：Class Size
- 例1 値：All pupils | 40 pupils and over | 40 pupils and over | All pupils | All pupils
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02445V02957, C02446V02958, Grade Structure, UNIT

## g0521（1 列）
- 見出し：C02446V02958
- 例1 値：27 | 3 | 3 | 18 | 3
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02445V02957, Class Size, Grade Structure, UNIT

## g0522（1 列）
- 見出し：Grade Structure
- 例1 値：1st class | 2nd-3rd class | 4th class | Multi-grade classes containing infants | Multi-grade classes containing infants
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02445V02957, Class Size, C02446V02958, UNIT

## g0523（3 列）
- 見出し：STATISTIC
- 例1 値：PHARMACISTS | PHARMACISTS | PHARMACISTS | PHARMACISTS | PHARMACISTS
  - 同じ表の列：Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG
- 例2 値：DENTISTS | DENTISTS | DENTISTS | DENTISTS | DENTISTS
  - 同じ表の列：Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0524（2 列）
- 見出し：Statistic Label
- 例1 値：Pharmacists | Pharmacists | Pharmacists | Pharmacists | Pharmacists
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG
- 例2 値：Dentists | Dentists | Dentists | Dentists | Dentists
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0525（3 列）
- 見出し：MEASURE
- 例1 値：LICENSEPHARM | LICENSEPHARM | LICENSEPHARM | LICENSEPHARM | LICENSEPHARM
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Measure, UNIT, VALUE, FLAG
- 例2 値：LICENSEDEN | PRACDEN | LICENSEDEN | LICENSEDEN | LICENSEDEN
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Measure, UNIT, VALUE, FLAG

## g0526（3 列）
- 見出し：Measure
- 例1 値：Pharmacists licensed to practice | Pharmacists licensed to practice | Pharmacists licensed to practice | Pharmacists licensed to practice | Pharmacists licensed to practice
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, UNIT, VALUE, FLAG
- 例2 値：Dentists licensed to practice | Dentists licensed to practice | Dentists licensed to practice | Dentists licensed to practice | Dentists licensed to practice
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, UNIT, VALUE, FLAG

## g0527（4 列）
- 見出し：FLAG
- 例1 値：BE | E | M
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE
- 例2 値：E | E | E | E | E
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0528（1 列）
- 見出し：Flag
- 例1 値：Estimate | Missing | Break in series, Estimate
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0529（1 列）
- 見出し：Statistic Label
- 例1 値：Caring Personnel | Caring Personnel | Caring Personnel | Caring Personnel | Caring Personnel
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0530（1 列）
- 見出し：Flag
- 例1 値：Break in series
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0531（1 列）
- 見出し：Statistic
- 例1 値：New House Prices | Second Hand House Prices | Second Hand House Prices | Second Hand House Prices | New House Prices
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02343V02817, Area, UNIT, VALUE

## g0532（1 列）
- 見出し：C02343V02817
- 例1 値：06 | - | 05 | - | 03
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Area, UNIT, VALUE

## g0533（1 列）
- 見出し：Area
- 例1 値：Cork | National | Galway | Waterford | Cork
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02343V02817, UNIT, VALUE

## g0534（1 列）
- 見出し：TLIST(Q1)
- 例1 値：19952 | 19961 | 19954 | 19943 | 19951
  - 同じ表の列：STATISTIC, Statistic, Quarter, C01947V02657, Local Authority, C02341V02815, Housing Sector, UNIT

## g0535（1 列）
- 見出し：Quarter
- 例1 値：1995Q3 | 1994Q1 | 1995Q3 | 1995Q2 | 1995Q4
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C01947V02657, Local Authority, C02341V02815, Housing Sector, UNIT

## g0536（1 列）
- 見出し：C01947V02657
- 例1 値：02 | 24 | 23 | 12 | 17
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Local Authority, C02341V02815, Housing Sector, UNIT

## g0537（1 列）
- 見出し：Local Authority
- 例1 値：Dublin (City Council) | Sligo (County Council) | Dublin (City Council) | Kilkenny (County Council) | Westmeath (County Council)
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C01947V02657, C02341V02815, Housing Sector, UNIT

## g0538（2 列）
- 見出し：C02341V02815
- 例1 値：04 | - | 03 | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C01947V02657, Local Authority, Housing Sector, UNIT
- 例2 値：01 | 01 | - | 03 | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Housing Sector, UNIT, VALUE

## g0539（1 列）
- 見出し：Housing Sector
- 例1 値：All housing sectors | All housing sectors | Private | Private | Private
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C01947V02657, Local Authority, C02341V02815, UNIT

## g0540（1 列）
- 見出し：Housing Sector
- 例1 値：Private | All housing sectors | Voluntary and co-operative | Voluntary and co-operative | All housing sectors
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02341V02815, UNIT, VALUE

## g0541（1 列）
- 見出し：HarvestTime
- 例1 値：2020-09-23T17:30:03 | 2020-09-23T19:30:03 | 2020-09-23T18:30:03 | 2020-09-23T22:00:03 | 2020-09-23T22:30:02
  - 同じ表の列：BikeID, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsMotor, IsSmartLock

## g0542（1 列）
- 見出し：BikeID
- 例1 値：30 | 54 | 41 | 57 | 20
  - 同じ表の列：HarvestTime, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsMotor, IsSmartLock

## g0543（1 列）
- 見出し：Battery
- 例1 値：87 | 45 | 90 | 78 | 87
  - 同じ表の列：HarvestTime, BikeID, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsMotor, IsSmartLock

## g0544（1 列）
- 見出し：BikeIdentifier
- 例1 値：69 | 44 | 35 | 60 | 117
  - 同じ表の列：HarvestTime, BikeID, Battery, EBikeProfileID, EBikeStateID, IsEBike, IsMotor, IsSmartLock

## g0545（1 列）
- 見出し：EBikeProfileID
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeStateID, IsEBike, IsMotor, IsSmartLock

## g0546（1 列）
- 見出し：EBikeStateID
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeProfileID, IsEBike, IsMotor, IsSmartLock

## g0547（1 列）
- 見出し：IsEBike
- 例1 値：True | True | True | True | True
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsMotor, IsSmartLock

## g0548（1 列）
- 見出し：IsMotor
- 例1 値：False | False | False | False | False
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsSmartLock

## g0549（1 列）
- 見出し：IsSmartLock
- 例1 値：False | False | False | False | False
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsMotor

## g0550（1 列）
- 見出し：LastGPSTime
- 例1 値：2020-09-23T14:30:08 | 2020-09-23T23:58:58 | 2020-09-23T20:29:57 | 2020-09-23T20:31:42 | 2020-09-23T20:19:21
  - 同じ表の列：HarvestTime, BikeID, Battery, BikeIdentifier, EBikeProfileID, EBikeStateID, IsEBike, IsMotor

## g0551（1 列）
- 見出し：WEEK
- 例1 値：12 | 45 | 11 | 38 | 45
  - 同じ表の列：YEAR, Waste Type, Location, Weight (Kg)

## g0552（1 列）
- 見出し：Waste Type
- 例1 値：Green Waste | Green Waste | Green Waste | Green Waste | Green Waste
  - 同じ表の列：YEAR, WEEK, Location, Weight (Kg)

## g0553（1 列）
- 見出し：Location
- 例1 値：Coolock | Coolock | rathmines | rathmines | Coolock
  - 同じ表の列：YEAR, WEEK, Waste Type, Weight (Kg)

## g0554（1 列）
- 見出し：Weight (Kg)
- 例1 値：6740 | 9140 | 5920 | 7400 | 1680
  - 同じ表の列：YEAR, WEEK, Waste Type, Location

## g0555（1 列）
- 見出し：Meter_Number_Serving_Space
- 例1 値：161 | 406 | 276 | 810 | 140
  - 同じ表の列：IDENTIFIER, Location, Area_Ref, Hours_of_operation, Days_of_operation, Hourly_Tarrif, Restrictions

## g0556（1 列）
- 見出し：IDENTIFIER
- 例1 値：MNKSIGN0048 | DUNSIGN0273 | BLKSIGN0204 | CHWSIGN0009 | BLKSIGN0111
  - 同じ表の列：Meter_Number_Servin…, Location, Area_Ref, Hours_of_operation, Days_of_operation, Hourly_Tarrif, Restrictions

## g0557（1 列）
- 見出し：Location
- 例1 値：Glasthule | Mellifont | Blackrock Park Car Park | Cowshed Ca | Avoca Place
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Area_Ref, Hours_of_operation, Days_of_operation, Hourly_Tarrif, Restrictions

## g0558（1 列）
- 見出し：Area_Ref
- 例1 値：EFCH | Dundrum | Monkstown | Dún Laoghai | Dún Laoghai
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Location, Hours_of_operation, Days_of_operation, Hourly_Tarrif, Restrictions

## g0559（1 列）
- 見出し：Hours_of_operation
- 例1 値：0800 - 1900 | 0800 - 1900 | 0800 - 1900 | 0800 - 1900 | 0800 - 1900
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Location, Area_Ref, Days_of_operation, Hourly_Tarrif, Restrictions

## g0560（1 列）
- 見出し：Days_of_operation
- 例1 値：Monday to Saturda | Monday to Saturday | Monday to Saturda | Monday to Friday | Monday to Saturda
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Location, Area_Ref, Hours_of_operation, Hourly_Tarrif, Restrictions

## g0561（1 列）
- 見出し：Hourly_Tarrif
- 例1 値：1.5 | 1 | 1.5 | 1 | 1.5
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Location, Area_Ref, Hours_of_operation, Days_of_operation, Restrictions

## g0562（1 列）
- 見出し：Restrictions
- 例1 値：Max Charge €5 | Max Charge €6 | Max stay 3 Hours | Max Charge €3.60 | Max stay 3 Hours
  - 同じ表の列：Meter_Number_Servin…, IDENTIFIER, Location, Area_Ref, Hours_of_operation, Days_of_operation, Hourly_Tarrif

## g0563（1 列）
- 見出し：OID_
- 例1 値：17 | 25 | 24 | 7 | 44
  - 同じ表の列：Location, Unique_Ide, X_IG, Y_IG, SampleType, x_itm, y_itm

## g0564（1 列）
- 見出し：Location
- 例1 値：Little Dargle Nutgrove Avenue | Brewery Stream, Carysfort Pond Inlet | Bridesglen Stream Kilternan Bridge | Monkstown Stream, Drayton Close. | Priory Stream, Priory Avenue.
  - 同じ表の列：OID_, Unique_Ide, X_IG, Y_IG, SampleType, x_itm, y_itm

## g0565（1 列）
- 見出し：Unique_Ide
- 例1 値：44025 | 104010 | 40572 | 44095 | 43980
  - 同じ表の列：OID_, Location, X_IG, Y_IG, SampleType, x_itm, y_itm

## g0566（1 列）
- 見出し：X_IG
- 例1 値：314946 | 324735 | 319222 | 315914 | 326406
  - 同じ表の列：OID_, Location, Unique_Ide, Y_IG, SampleType, x_itm, y_itm

## g0567（1 列）
- 見出し：Y_IG
- 例1 値：228131 | 219343 | 227306 | 230056 | 230573
  - 同じ表の列：OID_, Location, Unique_Ide, X_IG, SampleType, x_itm, y_itm

## g0568（1 列）
- 見出し：SampleType
- 例1 値：River | Bathing Water | River | Bathing Water | River
  - 同じ表の列：OID_, Location, Unique_Ide, X_IG, Y_IG, x_itm, y_itm

## g0569（1 列）
- 見出し：x_itm
- 例1 値：715718.579361 | 720039.687269 | 721234.421568 | 720704.4608 | 721909.223613
  - 同じ表の列：OID_, Location, Unique_Ide, X_IG, Y_IG, SampleType, y_itm

## g0570（1 列）
- 見出し：y_itm
- 例1 値：728110.518973 | 725525.095673 | 729113.321742 | 722987.635307 | 727237.77458
  - 同じ表の列：OID_, Location, Unique_Ide, X_IG, Y_IG, SampleType, x_itm

## g0571（1 列）
- 見出し：Time
- 例1 値：00:00 | 12:00 | 18:00 | 17:00 | 14:00
  - 同じ表の列：Report, Temperature oC, wind_speed_km_h, wind_gust_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0572（1 列）
- 見出し：Report
- 例1 値："Moderate Drizzle " | "Cloudy" | "Rain shower" | "Moderate rain " | "Recent Drizzle "
  - 同じ表の列：Time, Temperature oC, wind_speed_km_h, wind_gust_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0573（1 列）
- 見出し：Temperature oC
- 例1 値：11 | 8 | 8 | 8 | 8
  - 同じ表の列：Time, Report, wind_speed_km_h, wind_gust_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0574（1 列）
- 見出し：wind_speed_km_h
- 例1 値：6 | 17 | 19 | 13 | 9
  - 同じ表の列：Time, Report, Temperature oC, wind_gust_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0575（1 列）
- 見出し：wind_gust_km_h
- 例1 値：39
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, Wind Direction o, rainfall_mm_h, Pressure hPa

## g0576（1 列）
- 見出し：Wind Direction o
- 例1 値：90 | 180 | 180 | 45 | 135
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, wind_gust_km_h, rainfall_mm_h, Pressure hPa

## g0577（1 列）
- 見出し：rainfall_mm_h
- 例1 値：0.4 | 0.1 | 0.3 | 0.01 | 1.0
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, wind_gust_km_h, Wind Direction o, Pressure hPa

## g0578（1 列）
- 見出し：Pressure hPa
- 例1 値：999 | 997 | 998 | 998 | 996
  - 同じ表の列：Time, Report, Temperature oC, wind_speed_km_h, wind_gust_km_h, Wind Direction o, rainfall_mm_h

## g0579（2 列）
- 見出し：County
- 例1 値：Donegal | Cork | Cork | Cork | Cork
  - 同じ表の列：SRN, School Year, School Type, Class ID, Class Type, New or Existing Cla…
- 例2 値：Waterford | Limerick | Dublin | Donegal | Leitrim
  - 同じ表の列：year, duty_paid_from, duty_paid_up_to, number_of_taxpayers

## g0580（1 列）
- 見出し：SRN
- 例1 値：17152R | 14839P | 13647B | 20603S | 18217B
  - 同じ表の列：County, School Year, School Type, Class ID, Class Type, New or Existing Cla…

## g0581（1 列）
- 見出し：School Year
- 例1 値：26/27 | 26/27 | 26/27 | 26/27 | 26/27
  - 同じ表の列：County, SRN, School Type, Class ID, Class Type, New or Existing Cla…

## g0582（1 列）
- 見出し：School Type
- 例1 値：Post Primary | Primary | Primary | Post Primary | Post Primary
  - 同じ表の列：County, SRN, School Year, Class ID, Class Type, New or Existing Cla…

## g0583（1 列）
- 見出し：Class ID
- 例1 値：15342.0 | 12740.0 | 44946.0 | 36039.0 | 12109.0
  - 同じ表の列：County, SRN, School Year, School Type, Class Type, New or Existing Cla…

## g0584（1 列）
- 見出し：Class Type
- 例1 値：Autism/Autistic Spectrum Disorders | Autism/Autistic Spectrum Disorders | Mild General Learning Disability | Hearing Impairment | Autism/Autistic Spectrum Disorders
  - 同じ表の列：County, SRN, School Year, School Type, Class ID, New or Existing Cla…

## g0585（1 列）
- 見出し：New or Existing Class
- 例1 値：Existing | Existing | Existing | Existing | Existing
  - 同じ表の列：County, SRN, School Year, School Type, Class ID, Class Type

## g0586（1 列）
- 見出し：category
- 例1 値：category_a_-_book_or_other_writing | category_a_-_book_or_other_writing | category_a_-_book_or_other_writing | category_c_-_a_musical_composition | category_a_-_book_or_other_writing
  - 同じ表の列：type_or_title

## g0587（1 列）
- 見出し：type_or_title
- 例1 値：Painting | Musical Composition | Something New/The Wrong Date Deal/Try H… | Pabhsaeir Inis Meáin | Alive
  - 同じ表の列：category

## g0588（1 列）
- 見出し：payments_to__mscon_
- 例1 値：LITHUANIA | CROATIA | ROMANIA | CZECH REPUBLIC | BELGIUM
  - 同じ表の列：quarter_year, payments_from__msid_, Country Code, Import, Non-Union, union__of__which_go…, union___of__which_t…, Total Union

## g0589（1 列）
- 見出し：quarter_year
- 例1 値：Q1 2025 | Q1 2022 | Q1 2025 | Q1 2024 | Q3 2021
  - 同じ表の列：payments_to__mscon_, payments_from__msid_, Country Code, Import, Non-Union, union__of__which_go…, union___of__which_t…, Total Union

## g0590（1 列）
- 見出し：payments_from__msid_
- 例1 値：IRELAND | IRELAND | IRELAND | AUSTRIA | PORTUGAL
  - 同じ表の列：payments_to__mscon_, quarter_year, Country Code, Import, Non-Union, union__of__which_go…, union___of__which_t…, Total Union

## g0591（1 列）
- 見出し：Country Code
- 例1 値：IT | LU | ES | PL | SK
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Import, Non-Union, union__of__which_go…, union___of__which_t…, Total Union

## g0592（1 列）
- 見出し：Import
- 例1 値：19.1 | 1497591.57 | 180411840.9 | 6216457.83 | 138850795.1
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Non-Union, union__of__which_go…, union___of__which_t…, Total Union

## g0593（1 列）
- 見出し：Non-Union
- 例1 値：2176583.58 | 519 | 13695.37 | 15695.06 | 1086.5
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Import, union__of__which_go…, union___of__which_t…, Total Union

## g0594（1 列）
- 見出し：union__of__which_goods
- 例1 値：1243461.09 | 1396387.55 | 33851224.2 | 301001.87 | 350313.35
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Import, Non-Union, union___of__which_t…, Total Union

## g0595（1 列）
- 見出し：union___of__which_tbe_services
- 例1 値：4026452.14 | 268413048.5 | 5236987.03 | 10787252.62 | 16139.82
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Import, Non-Union, union__of__which_go…, Total Union

## g0596（1 列）
- 見出し：Total Union
- 例1 値：16072849.16 | 109141.55 | 8534995.5 | 1454477.44 | 1056307.31
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Import, Non-Union, union__of__which_go…, union___of__which_t…

## g0597（1 列）
- 見出し：Total IOSS
- 例1 値：31126150.62 | 252146 | 243564.87 | 55859779.93 | 8725076.52
  - 同じ表の列：payments_to__mscon_, quarter_year, payments_from__msid_, Country Code, Import, Non-Union, union__of__which_go…, union___of__which_t…

## g0598（1 列）
- 見出し：duty_paid_from
- 例1 値：4000 | 3000 | 2000 | 3000 | 3000
  - 同じ表の列：year, county, duty_paid_up_to, number_of_taxpayers

## g0599（1 列）
- 見出し：duty_paid_up_to
- 例1 値：999 | 1999 | 3999 | 3999 | 3999
  - 同じ表の列：year, county, duty_paid_from, number_of_taxpayers

## g0600（1 列）
- 見出し：number_of_taxpayers
- 例1 値：399 | 149 | 407 | 15 | 371
  - 同じ表の列：year, county, duty_paid_from, duty_paid_up_to

## 答えの雛形

```
g0481	
g0482	
g0483	
g0484	
g0485	
g0486	
g0487	
g0488	
g0489	
g0490	
g0491	
g0492	
g0493	
g0494	
g0495	
g0496	
g0497	
g0498	
g0499	
g0500	
g0501	
g0502	
g0503	
g0504	
g0505	
g0506	
g0507	
g0508	
g0509	
g0510	
g0511	
g0512	
g0513	
g0514	
g0515	
g0516	
g0517	
g0518	
g0519	
g0520	
g0521	
g0522	
g0523	
g0524	
g0525	
g0526	
g0527	
g0528	
g0529	
g0530	
g0531	
g0532	
g0533	
g0534	
g0535	
g0536	
g0537	
g0538	
g0539	
g0540	
g0541	
g0542	
g0543	
g0544	
g0545	
g0546	
g0547	
g0548	
g0549	
g0550	
g0551	
g0552	
g0553	
g0554	
g0555	
g0556	
g0557	
g0558	
g0559	
g0560	
g0561	
g0562	
g0563	
g0564	
g0565	
g0566	
g0567	
g0568	
g0569	
g0570	
g0571	
g0572	
g0573	
g0574	
g0575	
g0576	
g0577	
g0578	
g0579	
g0580	
g0581	
g0582	
g0583	
g0584	
g0585	
g0586	
g0587	
g0588	
g0589	
g0590	
g0591	
g0592	
g0593	
g0594	
g0595	
g0596	
g0597	
g0598	
g0599	
g0600	
```
