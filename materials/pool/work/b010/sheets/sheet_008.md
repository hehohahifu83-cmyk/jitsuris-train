# ラベル用シート 008 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：DEROGATION_COUNTY
- 例1 値：MEATH | DONEGAL | WEXFORD | LAOIS | WEXFORD
  - 同じ表の列：DEROGATION_YEAR, DEROGATION_COUNT, LEA_HERD_COUNT

## g0842（1 列）
- 見出し：DEROGATION_COUNT
- 例1 値：116 | 31 | 263 | 22 | 22
  - 同じ表の列：DEROGATION_YEAR, DEROGATION_COUNTY, LEA_HERD_COUNT

## g0843（1 列）
- 見出し：LEA_HERD_COUNT
- 例1 値：1732 | 1835 | 176 | 429 | 1332
  - 同じ表の列：DEROGATION_YEAR, DEROGATION_COUNTY, DEROGATION_COUNT

## g0844（2 列）
- 見出し：STATISTIC
- 例1 値：EDA51C4 | EDA51C2 | EDA51C1 | EDA51C1 | EDA51C4
  - 同じ表の列：Statistic, TLIST(A1), Year, C02498V03025, Sex Category School, UNIT, VALUE
- 例2 値：MTM01C1 | MTM01C1 | MTM01C1 | MTM01C1 | MTM01C1
  - 同じ表の列：Statistic Label, tlist_m1_, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0845（1 列）
- 見出し：Statistic
- 例1 値：Female Pupils in Ordinary Classes in Or… | Female Pupils in Ordinary Classes in Or… | Female Pupils in Ordinary Classes in Or… | Male Pupils in Ordinary Classes in Ordi… | All Pupils in Ordinary Classes in Ordin…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02498V03025, Sex Category School, UNIT, VALUE

## g0846（3 列）
- 見出し：TLIST(A1)
- 例1 値：2016 | 2013 | 2010 | 2016 | 2002
  - 同じ表の列：STATISTIC, Statistic, Year, C02498V03025, Sex Category School, UNIT, VALUE
- 例2 値：2015 | 2015 | 2015 | 2015 | 2015
  - 同じ表の列：STATISTIC, Statistic, Year, C02779V03348, County, C03552V04288, Vaccine Type, UNIT

## g0847（1 列）
- 見出し：C02498V03025
- 例1 値：- | 031 | 03 | 033 | 02
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex Category School, UNIT, VALUE

## g0848（1 列）
- 見出し：Sex Category School
- 例1 値：All-thru mixed sex schools | Mixed sex schools | Single sex schools | Senior single sex schools | Junior mixed sex schools
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02498V03025, UNIT, VALUE

## g0849（5 列）
- 見出し：STATISTIC
- 例1 値：FIQ02 | FIQ02 | FIQ02 | FIQ02 | FIQ02
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C02568V03113, Item, UNIT, VALUE
- 例2 値：HSM10 | HSM10 | HSM10 | HSM10 | HSM10
  - 同じ表の列：Statistic, TLIST(M1), Month, C02196V02652, State, UNIT, VALUE

## g0850（1 列）
- 見出し：Statistic
- 例1 値：Exchequer Account (Historical Series) | Exchequer Account (Historical Series) | Exchequer Account (Historical Series) | Exchequer Account (Historical Series) | Exchequer Account (Historical Series)
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02568V03113, Item, UNIT, VALUE

## g0851（2 列）
- 見出し：TLIST(Q1)
- 例1 値：19811 | 19953 | 19931 | 19792 | 19913
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02568V03113, Item, UNIT, VALUE
- 例2 値：20094 | 20091 | 20091 | 20092 | 20082
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02638V03194, Type of Traffic, C01855V02284, Irish Ports, UNIT

## g0852（2 列）
- 見出し：Quarter
- 例1 値：1993Q1 | 1990Q4 | 1996Q4 | 1988Q4 | 1978Q2
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02568V03113, Item, UNIT, VALUE
- 例2 値：2010Q2 | 2007Q1 | 2009Q3 | 2007Q2 | 2008Q1
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02638V03194, Type of Traffic, C01855V02284, Irish Ports, UNIT

## g0853（1 列）
- 見出し：C02568V03113
- 例1 値：5 | 6 | 5 | 6 | 6
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Item, UNIT, VALUE

## g0854（1 列）
- 見出し：Item
- 例1 値：Post Office and TSB deposits | Post Office and TSB deposits | Post Office and TSB deposits | Building Societies deposits and shares | Building Societies deposits and shares
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02568V03113, UNIT, VALUE

## g0855（1 列）
- 見出し：UNIT
- 例1 値：Euro Million | Euro Million | Euro Million | Euro Million | Euro Million
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02568V03113, Item, VALUE

## g0856（3 列）
- 見出し：VALUE
- 例1 値：9152.3 | 9632.9 | 982.9 | 699.1 | 591.1
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02568V03113, Item, UNIT
- 例2 値：153.9 | 12.1 | 92.5 | 65.1 | 86.6
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, C02431V02938, Meteorological Weat…, UNIT

## g0857（1 列）
- 見出し：STATISTIC
- 例1 値：LTCBEDS | LTCBEDS | LTCBEDS | LTCBEDS | LTCBEDS
  - 同じ表の列：Statistic Label, YEAR, Year, BEDTYPE, Bed type, UNIT, VALUE, FLAG

## g0858（1 列）
- 見出し：Statistic Label
- 例1 値：Beds in residential long-term care faci… | Beds in residential long-term care faci… | Beds in residential long-term care faci… | Beds in residential long-term care faci… | Beds in residential long-term care faci…
  - 同じ表の列：STATISTIC, YEAR, Year, BEDTYPE, Bed type, UNIT, VALUE, FLAG

## g0859（1 列）
- 見出し：BEDTYPE
- 例1 値：NURSING | NURSING | NURSING | NURSING | NURSING
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Bed type, UNIT, VALUE, FLAG

## g0860（1 列）
- 見出し：Bed type
- 例1 値：Long-term care nursing bed | Long-term care nursing bed | Long-term care nursing bed | Long-term care nursing bed | Long-term care nursing bed
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, BEDTYPE, UNIT, VALUE, FLAG

## g0861（1 列）
- 見出し：FLAG
- 例1 値：B | B | B
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, BEDTYPE, Bed type, UNIT, VALUE

## g0862（1 列）
- 見出し：Flag
- 例1 値：Break in series | Break in series | Break in series
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, BEDTYPE, Bed type, UNIT, VALUE

## g0863（1 列）
- 見出し：Statistic
- 例1 値：New House Guarantee Registrations | New House Guarantee Registrations | New House Guarantee Registrations | New House Guarantee Registrations | New House Guarantee Registrations
  - 同じ表の列：STATISTIC, TLIST(M1), Month, C02196V02652, State, UNIT, VALUE

## g0864（1 列）
- 見出し：TLIST(M1)
- 例1 値：201610 | 199011 | 201312 | 200605 | 201811
  - 同じ表の列：STATISTIC, Statistic, Month, C02196V02652, State, UNIT, VALUE

## g0865（2 列）
- 見出し：Month
- 例1 値：2019M06 | 2018M05 | 1992M12 | 2013M05 | 1992M11
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), C02196V02652, State, UNIT, VALUE
- 例2 値：1959M11 | 1958M12 | 1959M01 | 1963M03 | 1962M03
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0866（1 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, State, UNIT, VALUE

## g0867（1 列）
- 見出し：Type
- 例1 値：EU5 - Retention | EU1 - Residence Card | EUCC - EU Citizen Child | EUPA - EU Permitted Family Member Asses… | EUPA - EU Permitted Family Member Asses…
  - 同じ表の列：Status, year, Jan, Feb, Mar, Apr, May, Jun

## g0868（4 列）
- 見出し：Status
- 例1 値：Received | Granted | Granted | Granted | Granted
  - 同じ表の列：Type, year, Jan, Feb, Mar, Apr, May, Jun
- 例2 値：Completed | Completed | Completed | Completed | Completed
  - 同じ表の列：X, Y, FID, FID_1, gid, location, senior_sta, junior_sta

## g0869（1 列）
- 見出し：Jan
- 例1 値：* | 32 | * | 25 | *
  - 同じ表の列：Type, Status, year, Feb, Mar, Apr, May, Jun

## g0870（1 列）
- 見出し：Feb
- 例1 値：6 | 27 | 281 | 10 | 295
  - 同じ表の列：Type, Status, year, Jan, Mar, Apr, May, Jun

## g0871（1 列）
- 見出し：Mar
- 例1 値：* | 160 | 18 | 208 | 15
  - 同じ表の列：Type, Status, year, Jan, Feb, Apr, May, Jun

## g0872（1 列）
- 見出し：Apr
- 例1 値：13 | 0 | 29 | 11 | 37
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, May, Jun

## g0873（1 列）
- 見出し：May
- 例1 値：12 | 6 | 24 | * | 13
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, Jun

## g0874（1 列）
- 見出し：Jun
- 例1 値：0 | 10 | 0 | 6 | 42
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May

## g0875（1 列）
- 見出し：Jul
- 例1 値：0 | * | 11 | 70 | *
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May

## g0876（1 列）
- 見出し：Quarter
- 例1 値：Qtr 1 | Qtr 2 | Qtr 1 | Qtr 4 | Qtr 1
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, FTE

## g0877（1 列）
- 見出し：Level_1
- 例1 値：Agriculture Group | Agriculture Group | Tourism, Culture, Arts, Gaeltacht, Spor… | Housing, Local Government & Heritage Gr… | Health Group
  - 同じ表の列：Year, Quarter, Level_2, Level_3, Level_4, Level_5, Level_6, FTE

## g0878（1 列）
- 見出し：Level_2
- 例1 値：Local Authorities | Defence | Housing, Local Government & Heritage | Education & Skillls | Education & Skillls
  - 同じ表の列：Year, Quarter, Level_1, Level_3, Level_4, Level_5, Level_6, FTE

## g0879（1 列）
- 見出し：Level_3
- 例1 値：NCSA | Civil Service | NCSA | Civil Service | Local Authorities
  - 同じ表の列：Year, Quarter, Level_1, Level_2, Level_4, Level_5, Level_6, FTE

## g0880（1 列）
- 見出し：Level_4
- 例1 値：Civil Service | Commission for Regulation of Utilities … | Non Commercial State Agencies | Defence Sector | Health Sector
  - 同じ表の列：Year, Quarter, Level_1, Level_2, Level_3, Level_5, Level_6, FTE

## g0881（1 列）
- 見出し：Level_5
- 例1 値：NCSA - Active | NCSA - Active | Health Service Executive | NCSA - Active | International Protection Tribunal
  - 同じ表の列：Year, Quarter, Level_1, Level_2, Level_3, Level_4, Level_6, FTE

## g0882（1 列）
- 見出し：Level_6
- 例1 値：Educational Research Centres | Arts Council | National Library of Ireland | Waterways Ireland | Institutes Of Technology - Core Posts
  - 同じ表の列：Year, Quarter, Level_1, Level_2, Level_3, Level_4, Level_5, FTE

## g0883（1 列）
- 見出し：FTE
- 例1 値：34 | 161.68 | 35.3 | 1,237.60 | 98.6
  - 同じ表の列：Year, Quarter, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6

## g0884（1 列）
- 見出し：period
- 例1 値：2015Q1 | 2015Q1 | 2014Q1 | 2015Q1 | 2015Q2
  - 同じ表の列：programme, scheme, basis, age_code, age_band, recipients

## g0885（1 列）
- 見出し：programme
- 例1 値：Pensions | Illness,Disability and Caring | Working Age Income Supports | Pensions | Illness,Disability and Caring
  - 同じ表の列：period, scheme, basis, age_code, age_band, recipients

## g0886（1 列）
- 見出し：scheme
- 例1 値：CARB | WCP | UA | UA | INVP
  - 同じ表の列：period, programme, basis, age_code, age_band, recipients

## g0887（1 列）
- 見出し：basis
- 例1 値：Social Insurance | Social Insurance | Social Assistance | Social Assistance | Social Assistance
  - 同じ表の列：period, programme, scheme, age_code, age_band, recipients

## g0888（1 列）
- 見出し：age_code
- 例1 値：576 | 515 | 355 | 515 | 530
  - 同じ表の列：period, programme, scheme, basis, age_band, recipients

## g0889（1 列）
- 見出し：age_band
- 例1 値：55 - 59 years | 25 - 29 years | 66 - 74 years | Under 20 years | 66 years and over
  - 同じ表の列：period, programme, scheme, basis, age_code, recipients

## g0890（1 列）
- 見出し：recipients
- 例1 値：13.0 | 42.0 | 199253.0 | 34.0 | 2368.0
  - 同じ表の列：period, programme, scheme, basis, age_code, age_band

## g0891（1 列）
- 見出し：Time
- 例1 値：2026-01-18T12:00:00 | 2026-01-26T13:00:00 | 2026-01-28T19:00:00 | 2026-02-04T01:00:00 | 2026-01-13T02:00:00
  - 同じ表の列：aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0892（1 列）
- 見出し：aston_quay_fitzgeralds
- 例1 値：12 | 3 | 24 | 37 | 29
  - 同じ表の列：Time, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0893（3 列）
- 見出し：bachelors_walk_bachelors_way__counter_nonrepsonsive___remove
- 例1 値：9 | 1 | 6 | 1 | 1
  - 同じ表の列：Time, aston_quay_fitzgera…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…
- 例2 値：3 | 1 | 2 | 2 | 2
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0894（1 列）
- 見出し：aston_quay_fitzgeralds_in
- 例1 値：5 | 25 | 20 | 4 | 7
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0895（1 列）
- 見出し：aston_quay_fitzgeralds_out
- 例1 値：1 | 11 | 14 | 3 | 17
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…, baggot_st_upper_mes…

## g0896（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank
- 例1 値：5132 | 6576 | 7515 | 3692 | 5252
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0897（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank_pedestrians_in
- 例1 値：3300 | 3091 | 2406 | 6817 | 3142
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0898（1 列）
- 見出し：baggot_st_upper_mespil_rd_bank_pedestrians_out
- 例1 値：305 | 4599 | 4361 | 5139 | 3956
  - 同じ表の列：Time, aston_quay_fitzgera…, bachelors_walk_bach…, aston_quay_fitzgera…, aston_quay_fitzgera…, bachelors_walk_bach…, bachelors_walk_bach…, baggot_st_upper_mes…

## g0899（3 列）
- 見出し：X
- 例1 値：-679245.041008136 | -684957.732410276 | -679698.443067748 | -677996.5906925 | -679634.656999523
  - 同じ表の列：Y, Local_Authority, Location_Town, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type, Parking_Fee
- 例2 値：-6.45090379217623 | -6.32795331229551 | -6.34749113860511 | -6.32558223623118 | -6.41640427143994
  - 同じ表の列：Y, FID, FID_1, gid, location, senior_sta, junior_sta, status

## g0900（4 列）
- 見出し：Y
- 例1 値：7067093.08445489 | 7066702.58303626 | 7066692.86280554 | 7066899.60720105 | 7096665.4533854
  - 同じ表の列：X, Local_Authority, Location_Town, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type, Parking_Fee
- 例2 値：732621.6682 | 735349.1928 | 736640.2183 | 726489.0781 | 739144.5466
  - 同じ表の列：X, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, AREA, CATEGORY

## g0901（1 列）
- 見出し：Local_Authority
- 例1 値：Fingal County Council | Fingal County Council | Fingal County Council | Fingal County Council | Fingal County Council
  - 同じ表の列：X, Y, Location_Town, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type, Parking_Fee

## g0902（1 列）
- 見出し：Location_Town
- 例1 値：Rush | Malahide | Malahide | Malahide | Skerries
  - 同じ表の列：X, Y, Local_Authority, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type, Parking_Fee

## g0903（1 列）
- 見出し：Section_ID
- 例1 値：1 | 4 | 6 | 4 | 2
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Meter_ID, Parking_Type, Tariff___Area_Type, Parking_Fee

## g0904（1 列）
- 見出し：Meter_ID
- 例1 値：18 | 23 | 21 | 21 | 11
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Section_ID, Parking_Type, Tariff___Area_Type, Parking_Fee

## g0905（1 列）
- 見出し：Parking_Type
- 例1 値：Pay & Display Meter | Pay & Display Meter | Pay & Display Meter | Pay & Display Meter | Pay & Display Meter
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Section_ID, Meter_ID, Tariff___Area_Type, Parking_Fee

## g0906（1 列）
- 見出し：Tariff___Area_Type
- 例1 値：FF | FC | FD | FAM | FC
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Section_ID, Meter_ID, Parking_Type, Parking_Fee

## g0907（1 列）
- 見出し：Parking_Fee
- 例1 値：€1.70/hr | €5.00 per day or part thereof | €5.00 per day or part thereof | €1.70/hr | 1st 2 hrs free, then €1.00 per hr there…
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type

## g0908（1 列）
- 見出し：Short_Stay___Long_Stay
- 例1 値：Long Stay | Long Stay | Short Stay | Long Stay | Short Stay
  - 同じ表の列：X, Y, Local_Authority, Location_Town, Section_ID, Meter_ID, Parking_Type, Tariff___Area_Type

## g0909（1 列）
- 見出し：Statistic
- 例1 値：Immunisation uptake at 12 months of age | Immunisation uptake at 12 months of age | Immunisation uptake at 12 months of age | Immunisation uptake at 12 months of age | Immunisation uptake at 12 months of age
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02779V03348, County, C03552V04288, Vaccine Type, UNIT

## g0910（1 列）
- 見出し：C02779V03348
- 例1 値：171 | 162 | 09 | 06 | 15
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, County, C03552V04288, Vaccine Type, UNIT

## g0911（1 列）
- 見出し：County
- 例1 値：Limerick County | South Tipperary | Kildare | Donegal | Kilkenny
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02779V03348, C03552V04288, Vaccine Type, UNIT

## g0912（1 列）
- 見出し：C03552V04288
- 例1 値：80 | 10 | 80 | 30 | 10
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02779V03348, County, Vaccine Type, UNIT

## g0913（1 列）
- 見出し：Vaccine Type
- 例1 値：Bacille Calmette Guerin vaccine | Pneumococcal Conjugare vaccine | Meningococcal group C vaccine | Pneumococcal Conjugare vaccine | Pneumococcal Conjugare vaccine
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02779V03348, County, C03552V04288, UNIT

## g0914（1 列）
- 見出し：UNIT
- 例1 値：% | % | % | % | %
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02779V03348, County, C03552V04288, Vaccine Type

## g0915（1 列）
- 見出し：Statistic
- 例1 値：Bulk Traffic | Bulk Traffic | Bulk Traffic | Bulk Traffic | Bulk Traffic
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02638V03194, Type of Traffic, C01855V02284, Irish Ports, UNIT

## g0916（1 列）
- 見出し：C02638V03194
- 例1 値：12 | 13 | 12 | 12 | 12
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Type of Traffic, C01855V02284, Irish Ports, UNIT

## g0917（1 列）
- 見出し：Type of Traffic
- 例1 値：All bulk traffic | Break bulk traffic | All bulk traffic | Dry bulk traffic | Dry bulk traffic
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02638V03194, C01855V02284, Irish Ports, UNIT

## g0918（1 列）
- 見出し：C01855V02284
- 例1 値：- | IEGRN | XI | XI | IEKLN
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02638V03194, Type of Traffic, Irish Ports, UNIT

## g0919（1 列）
- 見出し：Irish Ports
- 例1 値：Dublin | All Irish ports | Wicklow | Bantry Bay | Larne
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02638V03194, Type of Traffic, C01855V02284, UNIT

## g0920（1 列）
- 見出し：UNIT
- 例1 値：000 Tonnes | 000 Tonnes | 000 Tonnes | 000 Tonnes | 000 Tonnes
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02638V03194, Type of Traffic, C01855V02284, Irish Ports

## g0921（1 列）
- 見出し：Statistic Label
- 例1 値：Total Rainfall | Total Rainfall | Total Rainfall | Total Rainfall | Total Rainfall
  - 同じ表の列：STATISTIC, tlist_m1_, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0922（1 列）
- 見出し：tlist_m1_
- 例1 値：196004 | 196304 | 196007 | 195911 | 196112
  - 同じ表の列：STATISTIC, Statistic Label, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g0923（1 列）
- 見出し：C02431V02938
- 例1 値：010 | 009 | 013 | 012 | 010
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, Meteorological Weat…, UNIT, VALUE

## g0924（1 列）
- 見出し：Meteorological Weather Station
- 例1 値：Cork airport | Galway | Malin head | Shannon airport | Shannon airport
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, C02431V02938, UNIT, VALUE

## g0925（1 列）
- 見出し：DESCRIPTIO
- 例1 値：Under Construction | New | New | Preliminary Design | New
  - 同じ表の列：X, Y, OBJECTID, TESSELLATE, VISIBILITY, METRES, AREA, CATEGORY

## g0926（1 列）
- 見出し：TESSELLATE
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, VISIBILITY, METRES, AREA, CATEGORY

## g0927（1 列）
- 見出し：VISIBILITY
- 例1 値：-1 | -1 | -1 | -1 | -1
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, TESSELLATE, METRES, AREA, CATEGORY

## g0928（1 列）
- 見出し：METRES
- 例1 値：270 | 5930 | 502 | 902 | 53
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, AREA, CATEGORY

## g0929（1 列）
- 見出し：AREA
- 例1 値：GDA | DLRCC | GDA | GDA | GDA
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, CATEGORY

## g0930（1 列）
- 見出し：CATEGORY
- 例1 値：Greenway | Greenway | Greenway | Greenway | Greenway
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, AREA

## g0931（1 列）
- 見出し：SCHEMES
- 例1 値：GDA SW2 SW6 SW5, 2A, SW1 | 11F | 11C | GDA S06 | GDA 13D, 13G, 13
  - 同じ表の列：X, Y, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, AREA

## g0932（1 列）
- 見出し：STN_NU
- 例1 値：35002 | 14057 | 25006 | 35012 | 26021
  - 同じ表の列：LOCATION, WATERBODY, Catchment, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_, msl__km_

## g0933（1 列）
- 見出し：LOCATION
- 例1 値：KEALE BRIDGE | BALLYNACARROW | MOYLES MILL | NEW BR. | CASTLETOWNROCHE
  - 同じ表の列：STN_NU, WATERBODY, Catchment, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_, msl__km_

## g0934（1 列）
- 見出し：WATERBODY
- 例1 値：OWENGARVE | DUNKELLIN | KINGS | OWENMORE | FALLAN
  - 同じ表の列：STN_NU, LOCATION, Catchment, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_, msl__km_

## g0935（1 列）
- 見出し：Catchment
- 例1 値：Glyde & Dee | Corrib | Feale | Maigue | Owenea
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_, msl__km_

## g0936（1 列）
- 見出し：ORG
- 例1 値：OPW | EPA | OPW | OPW | OPW
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, gauge_x__m_, gauge_y__m_, poly_area__km_2_, msl__km_

## g0937（1 列）
- 見出し：gauge_x__m_
- 例1 値：298397 | 170982 | 295342 | 180581 | 131830
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, ORG, gauge_y__m_, poly_area__km_2_, msl__km_

## g0938（1 列）
- 見出し：gauge_y__m_
- 例1 値：270996 | 289236 | 222975 | 118457 | 268539
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, ORG, gauge_x__m_, poly_area__km_2_, msl__km_

## g0939（1 列）
- 見出し：poly_area__km_2_
- 例1 値：143.2 | 647.55 | 1098.78 | 2143.67 | 237.9
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, ORG, gauge_x__m_, gauge_y__m_, msl__km_

## g0940（1 列）
- 見出し：msl__km_
- 例1 値：36.358 | 12.698 | 34.984 | 42.343 | 16.214
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_

## g0941（1 列）
- 見出し：netlen__km_
- 例1 値：137.697 | 202.389 | 1746.456 | 816.976 | 166.017
  - 同じ表の列：STN_NU, LOCATION, WATERBODY, Catchment, ORG, gauge_x__m_, gauge_y__m_, poly_area__km_2_

## g0942（1 列）
- 見出し：accounting_year
- 例1 値：2020 | 2022 | 2021 | 2018 | 2024
  - 同じ表の列：pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0943（1 列）
- 見出し：pd_start_dt
- 例1 値：20210501 | 20250101 | 20240701 | 20180901 | 20190101
  - 同じ表の列：accounting_year, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0944（1 列）
- 見出し：pd_end_dt
- 例1 値：20190630 | 20231231 | 20190831 | 20181231 | 20250228
  - 同じ表の列：accounting_year, pd_start_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0945（1 列）
- 見出し：am_rateband1
- 例1 値：16.26 | 16.26 | 16.26 | 16.26 | 16.26
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0946（1 列）
- 見出し：am_rateband2
- 例1 値：24.39 | 24.39 | 24.39 | 24.39 | 24.39
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0947（1 列）
- 見出し：ssd_supplier_band1__m
- 例1 値：0.138 | 0.386 | 0.133 | 0.079 | 0.483
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band2_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0948（1 列）
- 見出し：ssd_supplier_band2__m
- 例1 値：4.822 | 5.158 | 4.892 | 5.374 | 5.345
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_exporter_band1_…, ssd_exporter_band2_…

## g0949（1 列）
- 見出し：ssd_exporter_band1__m
- 例1 値：-0.001 | -0.006 | -0.005 | -0.009 | -0.004
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band2_…

## g0950（1 列）
- 見出し：ssd_exporter_band2__m
- 例1 値：-0.195 | -0.166 | -0.11 | -0.059 | -0.138
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…

## g0951（1 列）
- 見出し：ssd_supplier_hectolitres_band1
- 例1 値：5592.2 | 30649.8 | 3987.5 | 29991 | 33013.5
  - 同じ表の列：accounting_year, pd_start_dt, pd_end_dt, am_rateband1, am_rateband2, ssd_supplier_band1_…, ssd_supplier_band2_…, ssd_exporter_band1_…

## g0952（1 列）
- 見出し：Statistic
- 例1 値：Current Driving Licences | Current Driving Licences | Current Driving Licences | Current Driving Licences | Current Driving Licences
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex, C03111V03761, Type of Driving Lic…, C03110V03760

## g0953（1 列）
- 見出し：C02199V02655
- 例1 値：1 | - | 2 | 1 | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex, C03111V03761, Type of Driving Lic…, C03110V03760

## g0954（1 列）
- 見出し：C03111V03761
- 例1 値：1 | 5 | 5 | 1 | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, Type of Driving Lic…, C03110V03760

## g0955（1 列）
- 見出し：Type of Driving Licence
- 例1 値：Learner permit | Learner permit | Learner permit | Learner permit | Full
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C03111V03761, C03110V03760

## g0956（1 列）
- 見出し：C03110V03760
- 例1 値：15 | 14 | 13 | 17 | 26
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C03111V03761, Type of Driving Lic…

## g0957（1 列）
- 見出し：Licensing Authority
- 例1 値：Roscommon county council | Tipperary North county council | Monaghan county council | Kildare county council | Westmeath county council
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C03111V03761, Type of Driving Lic…

## g0958（1 列）
- 見出し：SensorTimestamp
- 例1 値：2013-07-06T00:00:29 | 2013-07-11T13:10:29 | 2013-07-11T13:00:29 | 2013-07-10T17:40:29 | 2013-07-11T22:15:39
  - 同じ表の列：conductivity__s_m_, temperature__degree…, pressure__decibars_

## g0959（1 列）
- 見出し：conductivity__s_m_
- 例1 値：3.92386 | 4.50774 | 4.46335 | 3.94227 | 4.48867
  - 同じ表の列：SensorTimestamp, temperature__degree…, pressure__decibars_

## g0960（1 列）
- 見出し：temperature__degrees_c_
- 例1 値：17.4741 | 10.903 | 17.0567 | 11.9951 | 11.9717
  - 同じ表の列：SensorTimestamp, conductivity__s_m_, pressure__decibars_

## 答えの雛形

```
g0841	
g0842	
g0843	
g0844	
g0845	
g0846	
g0847	
g0848	
g0849	
g0850	
g0851	
g0852	
g0853	
g0854	
g0855	
g0856	
g0857	
g0858	
g0859	
g0860	
g0861	
g0862	
g0863	
g0864	
g0865	
g0866	
g0867	
g0868	
g0869	
g0870	
g0871	
g0872	
g0873	
g0874	
g0875	
g0876	
g0877	
g0878	
g0879	
g0880	
g0881	
g0882	
g0883	
g0884	
g0885	
g0886	
g0887	
g0888	
g0889	
g0890	
g0891	
g0892	
g0893	
g0894	
g0895	
g0896	
g0897	
g0898	
g0899	
g0900	
g0901	
g0902	
g0903	
g0904	
g0905	
g0906	
g0907	
g0908	
g0909	
g0910	
g0911	
g0912	
g0913	
g0914	
g0915	
g0916	
g0917	
g0918	
g0919	
g0920	
g0921	
g0922	
g0923	
g0924	
g0925	
g0926	
g0927	
g0928	
g0929	
g0930	
g0931	
g0932	
g0933	
g0934	
g0935	
g0936	
g0937	
g0938	
g0939	
g0940	
g0941	
g0942	
g0943	
g0944	
g0945	
g0946	
g0947	
g0948	
g0949	
g0950	
g0951	
g0952	
g0953	
g0954	
g0955	
g0956	
g0957	
g0958	
g0959	
g0960	
```
