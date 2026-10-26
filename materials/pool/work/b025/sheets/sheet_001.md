# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：STATISTIC
- 例1 値：HSBA04C02 | HSBA04C01 | HSBA04C01 | HSBA04C02 | HSBA04C01
  - 同じ表の列：Statistic Label, tlist_a1_, Year, C02076V03371, Age Group, UNIT, VALUE

## g0002（1 列）
- 見出し：Statistic Label
- 例1 値：Percentage of women registered for the … | Women registered for the HSE Home Birth… | Percentage of women registered for the … | Percentage of women registered for the … | Percentage of women registered for the …
  - 同じ表の列：STATISTIC, tlist_a1_, Year, C02076V03371, Age Group, UNIT, VALUE

## g0003（1 列）
- 見出し：tlist_a1_
- 例1 値：2021 | 2015 | 2022 | 2012 | 2022
  - 同じ表の列：STATISTIC, Statistic Label, Year, C02076V03371, Age Group, UNIT, VALUE

## g0004（3 列）
- 見出し：Year
- 例1 値：2017 | 2019 | 2022 | 2022 | 2021
  - 同じ表の列：STATISTIC, Statistic Label, tlist_a1_, C02076V03371, Age Group, UNIT, VALUE
- 例2 値：2021 | 2021 | 2021 | 2024 | 2023
  - 同じ表の列：quarter, revenue_vehicle_cat…, new_used, number_registrations, exempt_registrations, vrt_liability__m

## g0005（1 列）
- 見出し：C02076V03371
- 例1 値：- | 485 | 405 | 410 | 440
  - 同じ表の列：STATISTIC, Statistic Label, tlist_a1_, Year, Age Group, UNIT, VALUE

## g0006（1 列）
- 見出し：Age Group
- 例1 値：25 - 29 years | 40 years and over | 25 - 29 years | 35 - 39 years | All ages
  - 同じ表の列：STATISTIC, Statistic Label, tlist_a1_, Year, C02076V03371, UNIT, VALUE

## g0007（1 列）
- 見出し：UNIT
- 例1 値：% | Number | Number | % | Number
  - 同じ表の列：STATISTIC, Statistic Label, tlist_a1_, Year, C02076V03371, Age Group, VALUE

## g0008（1 列）
- 見出し：VALUE
- 例1 値：34.55 | 36.18 | 387 | 40.05 | 41.7
  - 同じ表の列：STATISTIC, Statistic Label, tlist_a1_, Year, C02076V03371, Age Group, UNIT

## g0009（1 列）
- 見出し：Obs
- 例1 値：153.0 | 166.0 | 464.0 | 390.0 | 419.0
  - 同じ表の列：Data Vintage, Publication Month, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0010（1 列）
- 見出し：Data Vintage
- 例1 値：2021 | 2021 | 2021 | 2020 | 2021
  - 同じ表の列：Obs, Publication Month, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0011（1 列）
- 見出し：Publication Month
- 例1 値：April | April | April | April | April
  - 同じ表の列：Obs, Data Vintage, Publication Year, Sub Sector, Government Departme…, NACE Code

## g0012（1 列）
- 見出し：Publication Year
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：Obs, Data Vintage, Publication Month, Sub Sector, Government Departme…, NACE Code

## g0013（2 列）
- 見出し：Sub Sector
- 例1 値：S1311 | S1311 | S11001 | S1311 | S12001
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Government Departme…, NACE Code
- 例2 値：S11001 | S11001 | S1311 | S1311 | S11001
  - 同じ表の列：Department / Organi…, Type of Funding, Vote Number, Parent Entity, Nace Code

## g0014（1 列）
- 見出し：Government Department/Local Authority
- 例1 値：Department of Environment, Climate and … | Department of Tourism, Culture, Arts, G… | Approved Housing Body | Department of Finance | Department of Health
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Sub Sector, NACE Code

## g0015（2 列）
- 見出し：NACE Code
- 例1 値：P8542 | O8413 | L6820 | K6419 | R9311
  - 同じ表の列：Obs, Data Vintage, Publication Month, Publication Year, Sub Sector, Government Departme…
- 例2 値：P8532 | R9319 | J6311 | O8411 | L6820
  - 同じ表の列：Department / Organi…, Sub Sector, Type of Funding, Vote Number, Parent Entity

## g0016（1 列）
- 見出し：Department / Organisational Body
- 例1 値：Department of Justice | Department of Finance | Department of Finance | Department of Environment, Climate and … | Department of Health
  - 同じ表の列：Sub Sector, Type of Funding, Vote Number, Parent Entity, Nace Code

## g0017（1 列）
- 見出し：Type of Funding
- 例1 値：Extra-Budgetary Funds | Commercial body under the aegis of Depa… | Commercial body under the aegis of Depa… | Non-commercial body under the aegis of … | Non-commercial body under the aegis of …
  - 同じ表の列：Department / Organi…, Sub Sector, Vote Number, Parent Entity, Nace Code

## g0018（1 列）
- 見出し：Vote Number
- 例1 値：14 | 32 | 27 | 3 | 19
  - 同じ表の列：Department / Organi…, Sub Sector, Type of Funding, Parent Entity, Nace Code

## g0019（1 列）
- 見出し：Parent Entity
- 例1 値：Bord na Móna PLC | Voluntary Health Insurance Board | Shannon Group plc | The Heritage Council | AIB Group PLC
  - 同じ表の列：Department / Organi…, Sub Sector, Type of Funding, Vote Number, Nace Code

## g0020（1 列）
- 見出し：Year
- 例1 値：Q3 14 | Q1 14 | Q4 13 | Q3 11 | Q2 09
  - 同じ表の列：Dublin, National excl. Dubl…

## g0021（1 列）
- 見出し：Dublin
- 例1 値：90.55289916 | 81.89220046 | 115.2269619 | 76.70180754 | 104.2666213
  - 同じ表の列：Year, National excl. Dubl…

## g0022（1 列）
- 見出し：National excl. Dublin
- 例1 値：98.23918828 | 83.47325897 | 79.36509086 | 84.55595189 | 82.51131337
  - 同じ表の列：Year, Dublin

## g0023（1 列）
- 見出し：unsafe_
- 例1 値：Clare | Cork | Cork | Mayo | Donegal
  - 同じ表の列：unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0024（1 列）
- 見出し：unsafe__2
- 例1 値：Bradan Beo Teoranta | Goatsbridge Trout Farm Ltd | Eany Fish Products Ltd. | Bradan Beo Teoranta | Mannin Bay Salmon Co. Ltd
  - 同じ表の列：unsafe_, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0025（1 列）
- 見出し：unsafe_1____________________________________________________
- 例1 値：Parteen Salmon Hatchery, Parteen, Birdh… | Moross 1 & 2, Mulroy Bay, Co. Donegal | Altan Freshwater Smolt Unit, Procklis, … | Innishdoonver, Clew Bay, Co.Mayo by the… | McSwynes Bay, Co. Donegal
  - 同じ表の列：unsafe_, unsafe__2, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0026（1 列）
- 見出し：unsafe_2__registration_number
- 例1 値：110 - FHA | 066 - FHA | 035 - FHA | 597 - FHA | 029 - FHA
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0027（1 列）
- 見出し：unsafe_3__________________________geographical_position___co
- 例1 値：-7.78068 | -9.71101 | -7.75602 | -9.76637 | -8.13331
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe__3, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0028（1 列）
- 見出し：unsafe__3
- 例1 値：53.23966 | 54.50093 | 53.44179 | 53.54283 | 54.63556
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe_4__species_k…, unsafe__4, unsafe__5

## g0029（1 列）
- 見出し：unsafe_4__species_kept
- 例1 値：a | a | a | a | a
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe__4, unsafe__5

## g0030（1 列）
- 見出し：unsafe__4
- 例1 値：a | a | a | a | a
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__5

## g0031（1 列）
- 見出し：unsafe__5
- 例1 値：a | a | a | a | Vector species present
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4

## g0032（1 列）
- 見出し：unsafe__6
- 例1 値：a | a | a | 4.1.2 Infectious haematopoietic necrosi… | a
  - 同じ表の列：unsafe_, unsafe__2, unsafe_1___________…, unsafe_2__registrat…, unsafe_3___________…, unsafe__3, unsafe_4__species_k…, unsafe__4

## g0033（1 列）
- 見出し：quarter
- 例1 値：3 | 2 | 1 | 2 | 3
  - 同じ表の列：year, revenue_vehicle_cat…, new_used, number_registrations, exempt_registrations, vrt_liability__m

## g0034（1 列）
- 見出し：revenue_vehicle_category
- 例1 値：C | M | A | M | C
  - 同じ表の列：year, quarter, new_used, number_registrations, exempt_registrations, vrt_liability__m

## g0035（1 列）
- 見出し：new_used
- 例1 値：New | Used | New | Used | Used
  - 同じ表の列：year, quarter, revenue_vehicle_cat…, number_registrations, exempt_registrations, vrt_liability__m

## g0036（1 列）
- 見出し：number_registrations
- 例1 値：13771 | 1654 | 3392 | 3044 | 15895
  - 同じ表の列：year, quarter, revenue_vehicle_cat…, new_used, exempt_registrations, vrt_liability__m

## g0037（1 列）
- 見出し：exempt_registrations
- 例1 値：798 | 18 | 26 | 40 | 43
  - 同じ表の列：year, quarter, revenue_vehicle_cat…, new_used, number_registrations, vrt_liability__m

## g0038（1 列）
- 見出し：vrt_liability__m
- 例1 値：3.21 | 36.34 | 0.22 | 2.2 | 0.81
  - 同じ表の列：year, quarter, revenue_vehicle_cat…, new_used, number_registrations, exempt_registrations

## g0039（1 列）
- 見出し：Licence Ref
- 例1 値：DG0476 | CN0931 | ENP0097 | 1020522 | CAP0078
  - 同じ表の列：County

## g0040（1 列）
- 見出し：County
- 例1 値：CO. CAVAN | CO. CLARE | CO. CORK | CO. CLARE | CO. CLARE
  - 同じ表の列：Licence Ref

## g0041（1 列）
- 見出し：JURISDICTION
- 例1 値：High Court | Circuit Court | Special Criminal Court | High Court | Circuit Court
  - 同じ表の列：AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0042（1 列）
- 見出し：AREA_OF_LAW
- 例1 値：Civil | Civil | Civil | Family | Civil
  - 同じ表の列：JURISDICTION, YEAR, CATEGORY, ODP_CATEGORY, INCOMING, RESOLVED

## g0043（1 列）
- 見出し：CATEGORY
- 例1 値：Other | Other | Appeals (Current) | Service Of Documents | Mental Health Applications
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, ODP_CATEGORY, INCOMING, RESOLVED

## g0044（1 列）
- 見出し：ODP_CATEGORY
- 例1 値：Guardianship Custody And Access | Other | Satisfaction Piece | Maintenance (Foreign) | Judgments Marked In The Office
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, INCOMING, RESOLVED

## g0045（1 列）
- 見出し：INCOMING
- 例1 値：229 | 1624 | 151 | 17 | 96
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, RESOLVED

## g0046（1 列）
- 見出し：RESOLVED
- 例1 値：77 | 16 | 1 | 58 | 1270
  - 同じ表の列：JURISDICTION, AREA_OF_LAW, YEAR, CATEGORY, ODP_CATEGORY, INCOMING

## g0047（1 列）
- 見出し：OBJECTID
- 例1 値：5207 | 4017 | 5606 | 4413 | 4013
  - 同じ表の列：Ref_No, Shape__Length

## g0048（1 列）
- 見出し：Ref_No
- 例1 値：VS/NTMK/12 | VS/B/09 | VS/RD/05 | VS/GD/03 | VS/W/05
  - 同じ表の列：OBJECTID, Shape__Length

## g0049（1 列）
- 見出し：Shape__Length
- 例1 値：120.12183305814 | 292.563051183167 | 682.755050098366 | 227.565288753508 | 537.417285283276
  - 同じ表の列：OBJECTID, Ref_No

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
```
