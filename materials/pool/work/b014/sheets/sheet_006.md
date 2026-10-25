# ラベル用シート 006 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（1 列）
- 見出し：AreaID
- 例1 値：12 | 9 | 13 | 1 | 16
  - 同じ表の列：RegionID, Area, Year, Q1, Q2, Q3, Q4

## g0602（1 列）
- 見出し：RegionID
- 例1 値：20 | 19 | 19 | 20 | 20
  - 同じ表の列：AreaID, Area, Year, Q1, Q2, Q3, Q4

## g0603（1 列）
- 見出し：Area
- 例1 値：Dublin City North | Cavan Monaghan | Dublin South East Wicklow | Dublin South Central | Dublin South West Kildare West Wicklow
  - 同じ表の列：AreaID, RegionID, Year, Q1, Q2, Q3, Q4

## g0604（1 列）
- 見出し：Q1
- 例1 値：224 | 260 | 251 | 141 | 101
  - 同じ表の列：AreaID, RegionID, Area, Year, Q2, Q3, Q4

## g0605（1 列）
- 見出し：Q2
- 例1 値：72 | 280 | 226 | 204 | 245
  - 同じ表の列：AreaID, RegionID, Area, Year, Q1, Q3, Q4

## g0606（1 列）
- 見出し：Q3
- 例1 値：240 | 542 | 163 | 240 | 208
  - 同じ表の列：AreaID, RegionID, Area, Year, Q1, Q2, Q4

## g0607（1 列）
- 見出し：Q4
- 例1 値：208 | 300 | 112 | 89 | 245
  - 同じ表の列：AreaID, RegionID, Area, Year, Q1, Q2, Q3

## g0608（1 列）
- 見出し：SHAPE__Area
- 例1 値：4436631.98257446 | 2602067.06204224 | 6770506.59243774 | 10589980.2546997 | 1054265.99145508
  - 同じ表の列：ID, OBJECTID

## g0609（1 列）
- 見出し：Action_Areas
- 例1 値：TIN 4 | AA 3 | AP 4 | SLO 1 | AA 1
  - 同じ表の列：Area_ha, OBJECTID, SHAPE__Length

## g0610（1 列）
- 見出し：Area_ha
- 例1 値：4.31225392402321 | 10.0405447956202 | 4.05753371130849 | 2.75697015065416 | 3.51967813884567
  - 同じ表の列：Action_Areas, OBJECTID, SHAPE__Length

## g0611（1 列）
- 見出し：SHAPE__Length
- 例1 値：239.988596406708 | 3309.97561355975 | 3527.49867507506 | 853.443419856038 | 855.425556309755
  - 同じ表の列：Action_Areas, Area_ha, OBJECTID

## g0612（1 列）
- 見出し：Quarter
- 例1 値：Mar-08 | Mar-08 | Mar-08 | Dec-07 | Mar-08
  - 同じ表の列：Type of personal in…, State, Business or company…, Number of people en…

## g0613（1 列）
- 見出し：Type of personal insolvency administration
- 例1 値：Total personal insolvencies | Personal insolvency agreement | Total bankruptcies | Debtor's petition | Personal insolvency agreement
  - 同じ表の列：Quarter, State, Business or company…, Number of people en…

## g0614（1 列）
- 見出し：State
- 例1 値：Victoria | Queensland | New South Wales | Australian Capital Territory | Total
  - 同じ表の列：Quarter, Type of personal in…, Business or company…, Number of people en…

## g0615（1 列）
- 見出し：Business or company involvement
- 例1 値：Yes | Yes | Yes | Yes | Total
  - 同じ表の列：Quarter, Type of personal in…, State, Number of people en…

## g0616（1 列）
- 見出し：Number of people entering a new personal insolvency
- 例1 値：315 | 2 | 19 | 175 | 75
  - 同じ表の列：Quarter, Type of personal in…, State, Business or company…

## g0617（3 列）
- 見出し：Date-Time
- 例1 値：2010-11-19 12:23:00 | 2010-11-19 15:55:00 | 2010-11-19 10:39:00 | 2010-11-19 16:13:00 | 2010-11-19 06:16:00
  - 同じ表の列：Lat, Lon, UV_Index
- 例2 値：2007-05-10 11:39:00 | 2007-05-10 12:26:00 | 2007-05-10 02:37:00 | 2007-05-10 03:02:00 | 2007-05-10 00:27:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0618（3 列）
- 見出し：UV_Index
- 例1 値：02.94 | 02.61 | 01.58 | 04.58 | 01.61
  - 同じ表の列：Date-Time, Lat, Lon
- 例2 値：04.20 | 01.16 | 00.19 | 00.75 | 00.02
  - 同じ表の列：Date-Time, Lat, Lon

## g0619（1 列）
- 見出し：Intended_Destination
- 例1 値：Transfer to Non-Govt Schl | Transfer to SA Govt Schl | unknown | Interstate/Overseas | Other
  - 同じ表の列：2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0620（1 列）
- 見出し：2014
- 例1 値：9022 | 1364 | 633 | 21222 | 2079
  - 同じ表の列：Intended_Destination, 2015, 2016, 2017, 2018, 2019, 2020, 2021

## g0621（1 列）
- 見出し：2015
- 例1 値：21245 | 1643 | 1252 | 4156 | 8843
  - 同じ表の列：Intended_Destination, 2014, 2016, 2017, 2018, 2019, 2020, 2021

## g0622（1 列）
- 見出し：2017
- 例1 値：1503 | 1233 | 21097 | 9306 | 479
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2018, 2019, 2020, 2021

## g0623（1 列）
- 見出し：2018
- 例1 値：4381 | 1752 | 20385 | 1483 | 4157
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2017, 2019, 2020, 2021

## g0624（1 列）
- 見出し：2019
- 例1 値：587 | 1558 | 1670 | 21212 | 4662
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2017, 2018, 2020, 2021

## g0625（1 列）
- 見出し：2020
- 例1 値：8117 | 1386 | 1791 | 530 | 4705
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2017, 2018, 2019, 2021

## g0626（1 列）
- 見出し：2022
- 例1 値：2322 | 1517 | 1517 | 29723 | 4226
  - 同じ表の列：Intended_Destination, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0627（1 列）
- 見出し：School_Number
- 例1 値：0212 | 6684 | 0483 | 1206 | 0906
  - 同じ表の列：Suburb, Post_Code, Type_of_Schooling, Year_Levels

## g0628（1 列）
- 見出し：Type_of_Schooling
- 例1 値：Preschools | Primary/Secondary Combined | Primary Education | Primary Education | Primary Education
  - 同じ表の列：School_Number, Suburb, Post_Code, Year_Levels

## g0629（1 列）
- 見出し：Year_Levels
- 例1 値：Reception to Year 6 | Reception to Year 7 | Reception to Year 12 | Reception to Year 12 | Reception to Year 6
  - 同じ表の列：School_Number, Suburb, Post_Code, Type_of_Schooling

## g0630（1 列）
- 見出し：AGPR ID
- 例1 値：AGPR3736 | AGPR2487 | AGPR661 | AGPR5482 | AGPR5377
  - 同じ表の列：Suburb, State or Territory

## g0631（1 列）
- 見出し：State or Territory
- 例1 値：WA | ACT | WA | NSW | WA
  - 同じ表の列：AGPR ID, Suburb

## g0632（1 列）
- 見出し：ip_right_type
- 例1 値：design | design | design | design | design
  - 同じ表の列：application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0633（1 列）
- 見出し：application_number
- 例1 値：201611038 | 201610573 | 201610590 | 201412778 | 201611257
  - 同じ表の列：ip_right_type, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0634（1 列）
- 見出し：ip_right_sub_type
- 例1 値：design | design | design | design | design
  - 同じ表の列：ip_right_type, application_number, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0635（1 列）
- 見出し：earliest_filed_date
- 例1 値：2014-06-05 | 2014-06-06 | 2016-02-05 | 2016-03-01 | 2016-02-12
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, priority_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0636（1 列）
- 見出し：priority_date
- 例1 値：2013-12-06 | 2014-03-26 | 2014-04-24 | 2015-06-23 | 2014-05-19
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, gained_registration…, gained_enforceable_…, enforceable_from_da…

## g0637（1 列）
- 見出し：gained_registration_status_date
- 例1 値：2016-03-01 | 2016-03-22 | 2016-02-11 | 2016-03-18 | 2016-04-15
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_enforceable_…, enforceable_from_da…

## g0638（1 列）
- 見出し：gained_enforceable_status_date
- 例1 値：2014-10-29 | 2015-01-14 | 2016-04-19 | 2015-01-14 | 2016-05-17
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, enforceable_from_da…

## g0639（1 列）
- 見出し：enforceable_from_date
- 例1 値：2016-05-27 | 2014-09-12 | 2016-04-22 | 2016-10-31 | 2016-05-16
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…

## g0640（1 列）
- 見出し：deemed_retired_date
- 例1 値：2016-04-19 | 2019-03-12 | 2016-04-08 | 2014-08-19 | 2019-05-30
  - 同じ表の列：ip_right_type, application_number, ip_right_sub_type, status, earliest_filed_date, priority_date, gained_registration…, gained_enforceable_…

## g0641（1 列）
- 見出し：LAND_DATE
- 例1 値：1879 | 1876 | 1872 | 1861 | 1871
  - 同じ表の列：LOCATION, LAND_AREA, YEAR, DESC_SR

## g0642（1 列）
- 見出し：LOCATION
- 例1 値：Somerset | Woodside, Westmorland | Westmorland | Kermode | Chichester, Somerset
  - 同じ表の列：LAND_DATE, LAND_AREA, YEAR, DESC_SR

## g0643（1 列）
- 見出し：LAND_AREA
- 例1 値：14 acres, 2 roods, 39 perches | 2460 acres | 40 acres | 124 acres | 1000 acres
  - 同じ表の列：LAND_DATE, LOCATION, YEAR, DESC_SR

## g0644（1 列）
- 見出し：DESC_SR
- 例1 値：All Nations Tin Mining Company
  - 同じ表の列：LAND_DATE, LOCATION, LAND_AREA, YEAR

## g0645（1 列）
- 見出し：Scenario D — 65 GL
- 例1 値：21.099999999999997868371792719699442386… | 0 | 65.400000000000005684341886080801486968… | 0 | 15.099999999999999644728632119949907064…
  - 同じ表の列：Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0646（1 列）
- 見出し：Scenario E — 90 GL
- 例1 値：89.899999999999991473487170878797769546… | 15.299999999999998934185896359849721193… | 4 | 15 | 15
  - 同じ表の列：Scenario D — 65 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0647（1 列）
- 見出し：Scenario C — 100 GL
- 例1 値：2.6000000000000000888178419700125232338… | 100.5 | 0 | 19.699999999999999289457264239899814128… | 11.899999999999998578914528479799628257…
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0648（1 列）
- 見出し：Scenario G — 115 GL
- 例1 値：19 | 19 | 3 | 23 | 27
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0649（1 列）
- 見出し：Scenario B — 142 GL
- 例1 値：142.5 | 44.5 | 25.1 | 4.2 | 25.4
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0650（1 列）
- 見出し：Scenario A — 151 GL
- 例1 値：4.2 | 47.8 | 151 | 13 | 10.2
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario I - 345 GL, Scenario J -321 GL, Scenario K -320 GL

## g0651（1 列）
- 見出し：Scenario I - 345 GL
- 例1 値：10 | 15 | 4 | 10 | 100
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario J -321 GL, Scenario K -320 GL

## g0652（1 列）
- 見出し：Scenario J -321 GL
- 例1 値：4.1 | 2.1 | 10 | 20.8 | 28
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario K -320 GL

## g0653（1 列）
- 見出し：Scenario K -320 GL
- 例1 値：15 | 4.1 | 22 | 5 | 10
  - 同じ表の列：Scenario D — 65 GL, Scenario E — 90 GL, Scenario C — 100 GL, Scenario G — 115 GL, Scenario B — 142 GL, Scenario A — 151 GL, Scenario I - 345 GL, Scenario J -321 GL

## g0654（1 列）
- 見出し：K
- 例1 値：19.3 | 19.8 | 24.2 | 19.3 | 18.4
  - 同じ表の列：Year, Year 1, Year 2, Year 3, Year 4, Year 5, Year 6, K-6

## g0655（1 列）
- 見出し：Year 1
- 例1 値：21.3 | 24.5 | 20.6 | 21.1 | 21.3
  - 同じ表の列：Year, K, Year 2, Year 3, Year 4, Year 5, Year 6, K-6

## g0656（1 列）
- 見出し：Year 2
- 例1 値：25.4 | 22.5 | 22.3 | 21.6 | 22.6
  - 同じ表の列：Year, K, Year 1, Year 3, Year 4, Year 5, Year 6, K-6

## g0657（1 列）
- 見出し：Year 3
- 例1 値：25.5 | 25.9 | 26.7 | 25.9 | 25.7
  - 同じ表の列：Year, K, Year 1, Year 2, Year 4, Year 5, Year 6, K-6

## g0658（1 列）
- 見出し：Year 4
- 例1 値：26.6 | 25.9 | 26.1 | 26.1 | 26.1
  - 同じ表の列：Year, K, Year 1, Year 2, Year 3, Year 5, Year 6, K-6

## g0659（1 列）
- 見出し：Year 5
- 例1 値：26.4 | 26.5 | 27.0 | 26.9 | 26.3
  - 同じ表の列：Year, K, Year 1, Year 2, Year 3, Year 4, Year 6, K-6

## g0660（1 列）
- 見出し：Year 6
- 例1 値：26.3 | 26.8 | 27.0 | 26.9 | 26.5
  - 同じ表の列：Year, K, Year 1, Year 2, Year 3, Year 4, Year 5, K-6

## g0661（1 列）
- 見出し：K-6
- 例1 値：24.2 | 26.2 | 24.0 | 23.8 | 26.5
  - 同じ表の列：Year, K, Year 1, Year 2, Year 3, Year 4, Year 5, Year 6

## g0662（1 列）
- 見出し：Selective Status
- 例1 値：Secondary education schools by selectiv… | Fully selective | Total selective | Non-selective | Total non-selective
  - 同じ表の列：Coeducational, Boys, Girls, Total

## g0663（1 列）
- 見出し：Coeducational
- 例1 値：7 | 3 | 332 | 1 | 17
  - 同じ表の列：Selective Status, Boys, Girls, Total

## g0664（1 列）
- 見出し：Boys
- 例1 値：2 | 13 | 1 | 20 | 7
  - 同じ表の列：Selective Status, Coeducational, Girls, Total

## g0665（1 列）
- 見出し：Girls
- 例1 値：1 | 17 | 6 | 23 | 2
  - 同じ表の列：Selective Status, Coeducational, Boys, Total

## g0666（2 列）
- 見出し：Total
- 例1 値：1 | 10 | 1 | 1 | 1
  - 同じ表の列：Selective Status, Coeducational, Boys, Girls
- 例2 値：8342930 | 5685240 | 17127690 | 10979910 | 4863490
  - 同じ表の列：Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0667（1 列）
- 見出し：primary_and_infants_schools
- 例1 値：1633 | 1649 | 1648 | 1652 | 1642
  - 同じ表の列：year, central_and_communi…, secondary_schools, schools_for_specifi…, environmental_educa…, total_schools

## g0668（1 列）
- 見出し：central_and_community_schools
- 例1 値：68 | 66 | 67 | 67 | 67
  - 同じ表の列：year, primary_and_infants…, secondary_schools, schools_for_specifi…, environmental_educa…, total_schools

## g0669（1 列）
- 見出し：secondary_schools
- 例1 値：394 | 397 | 404 | 398 | 402
  - 同じ表の列：year, primary_and_infants…, central_and_communi…, schools_for_specifi…, environmental_educa…, total_schools

## g0670（1 列）
- 見出し：schools_for_specific_purposes
- 例1 値：95 | 117 | 113 | 113 | 114
  - 同じ表の列：year, primary_and_infants…, central_and_communi…, secondary_schools, environmental_educa…, total_schools

## g0671（1 列）
- 見出し：environmental_education_centres
- 例1 値：23 | 23 | 23 | 23 | 23
  - 同じ表の列：year, primary_and_infants…, central_and_communi…, secondary_schools, schools_for_specifi…, total_schools

## g0672（1 列）
- 見出し：total_schools
- 例1 値：2109 | 2239 | 2210 | 2210 | 2230
  - 同じ表の列：year, primary_and_infants…, central_and_communi…, secondary_schools, schools_for_specifi…, environmental_educa…

## g0673（1 列）
- 見出し：_id
- 例1 値：5 | 1 | 2 | 4 | 3
  - 同じ表の列：Library, LGA, Long, Lat, PublicAccessFloorSp…, OpeningHours(perwee…

## g0674（1 列）
- 見出し：Library
- 例1 値：Wyndham Vale | Werribee | Point Cook | Julia Gillard Library Tarneit | Plaza
  - 同じ表の列：_id, LGA, Long, Lat, PublicAccessFloorSp…, OpeningHours(perwee…

## g0675（1 列）
- 見出し：LGA
- 例1 値：Wyndham City Council | Wyndham City Council | Wyndham City Council | Wyndham City Council | Wyndham City Council
  - 同じ表の列：_id, Library, Long, Lat, PublicAccessFloorSp…, OpeningHours(perwee…

## g0676（1 列）
- 見出し：PublicAccessFloorSpace
- 例1 値：1321 | 833 | 483 | 760 | 1225
  - 同じ表の列：_id, Library, LGA, Long, Lat, OpeningHours(perwee…

## g0677（1 列）
- 見出し：OpeningHours(perweek)
- 例1 値：48 | 48 | 62.5 | 57.5 | 57.5
  - 同じ表の列：_id, Library, LGA, Long, Lat, PublicAccessFloorSp…

## g0678（1 列）
- 見出し：P_TOT
- 例1 値：1.1818 | 0.3141 | 0.9779 | 1.5138 | 0.3473
  - 同じ表の列：YEAR, P_CROP, P_LVST, P_MISC, W_TOT, W_KAP, W_LAB, W_LAND

## g0679（1 列）
- 見出し：P_CROP
- 例1 値：1.0635 | 0.7711 | 1.0000 | 1.1413 | 0.8471
  - 同じ表の列：YEAR, P_TOT, P_LVST, P_MISC, W_TOT, W_KAP, W_LAB, W_LAND

## g0680（1 列）
- 見出し：P_LVST
- 例1 値：1.3593 | 1.1565 | 0.7164 | 1.1396 | 0.6571
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_MISC, W_TOT, W_KAP, W_LAB, W_LAND

## g0681（1 列）
- 見出し：P_MISC
- 例1 値：1.9318 | 1.3563 | 0.8324 | 0.7313 | 2.1098
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, W_TOT, W_KAP, W_LAB, W_LAND

## g0682（1 列）
- 見出し：W_TOT
- 例1 値：1.1704 | 1.7654 | 1.0758 | 0.6815 | 1.6416
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, P_MISC, W_KAP, W_LAB, W_LAND

## g0683（1 列）
- 見出し：W_KAP
- 例1 値：1.7469 | 1.0000 | 0.3675 | 0.6941 | 0.6442
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, P_MISC, W_TOT, W_LAB, W_LAND

## g0684（1 列）
- 見出し：W_LAB
- 例1 値：1.1805 | 0.1788 | 0.3256 | 1.1652 | 1.6038
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, P_MISC, W_TOT, W_KAP, W_LAND

## g0685（1 列）
- 見出し：W_LAND
- 例1 値：1.3686 | 0.9325 | 1.0047 | 1.5910 | 1.1028
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, P_MISC, W_TOT, W_KAP, W_LAB

## g0686（1 列）
- 見出し：W_INTMD
- 例1 値：1.6802 | 1.2513 | 0.8451 | 1.6419 | 1.0857
  - 同じ表の列：YEAR, P_TOT, P_CROP, P_LVST, P_MISC, W_TOT, W_KAP, W_LAB

## g0687（1 列）
- 見出し：Province or territory
- 例1 値：Quebec | Non-resident | British Columbia | Yukon | Quebec
  - 同じ表の列：Tax year, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0688（1 列）
- 見出し：Tax year
- 例1 値：2024 | 2024 | 2024 | 2024 | 2024
  - 同じ表の列：Province or territo…, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0689（1 列）
- 見出し：Number of returns
- 例1 値：443923 | 7297 | 7106958 | 2571814 | 12244678
  - 同じ表の列：Province or territo…, Tax year, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0690（1 列）
- 見出し：Total income assessed (Thousands of $)
- 例1 値：561234 | 24746204 | 431297827 | 805997663 | 55221378
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0691（1 列）
- 見出し：Total deductions (Thousands of $)
- 例1 値：43163796 | 4062488 | 27368407 | 1135489 | 4418404
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0692（1 列）
- 見出し：Taxable income assessed (Thousands of $)
- 例1 値：29120877 | 215900990 | 52317 | 6683211 | 87283082
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Total deductions (T…, Total non-refundabl…, Net federal tax (Th…, Net provincial tax …

## g0693（1 列）
- 見出し：Total non-refundable tax credits (Thousands of $)
- 例1 値：83133 | 91890 | 387248 | 3164361 | 25198
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Net federal tax (Th…, Net provincial tax …

## g0694（1 列）
- 見出し：Net federal tax (Thousands of $)
- 例1 値：163467 | 5602152 | 0 | 163467 | 0
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net provincial tax …

## g0695（1 列）
- 見出し：Net provincial tax (Thousands of $)
- 例1 値：119018 | 0 | 14412908 | 0 | 52003
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…

## g0696（1 列）
- 見出し：Total tax payable (Thousands of $)
- 例1 値：1294697 | 10125440 | 0 | 0 | 10125440
  - 同じ表の列：Province or territo…, Tax year, Number of returns, Total income assess…, Total deductions (T…, Taxable income asse…, Total non-refundabl…, Net federal tax (Th…

## g0697（1 列）
- 見出し：Females and males under 20
- 例1 値：36060 | 10 | 172770 | 1.4 | 37780
  - 同じ表の列：Total, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0698（1 列）
- 見出し：Females and males 20 to 24
- 例1 値：160080 | 633530 | 799610 | 67430 | 301930
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0699（1 列）
- 見出し：Females and males 25 to 29
- 例1 値：1464720 | 2797740 | 1600020 | 550 | 567810
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0700（1 列）
- 見出し：Females and males 30 to 34
- 例1 値：540360 | 281950 | 71210 | 1.8 | 3369760
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0701（1 列）
- 見出し：Females and males 35 to 39
- 例1 値：985630 | 1.8 | 780620 | 459550 | 590220
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 4…, Females and males 4…, Females and males 5…

## g0702（1 列）
- 見出し：Females and males 40 to 44
- 例1 値：1570 | 1.7 | 76930 | 724920 | 1614100
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 5…

## g0703（1 列）
- 見出し：Females and males 45 to 49
- 例1 値：453320 | 2421970 | 341270 | 1690 | 1429870
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 5…

## g0704（1 列）
- 見出し：Females and males 50 to 54
- 例1 値：594500 | 414340 | 2310840 | 1.7 | 1378160
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…

## g0705（1 列）
- 見出し：Females and males 55 to 59
- 例1 値：1432000 | 826240 | 605750 | 1262360 | 2366760
  - 同じ表の列：Total, Females and males u…, Females and males 2…, Females and males 2…, Females and males 3…, Females and males 3…, Females and males 4…, Females and males 4…

## g0706（1 列）
- 見出し：Sectors (English) | Secteurs (anglais)
- 例1 値：Information and communications technolo… | Other | Safety | Federal institutions | Food
  - 同じ表の列：Sectors (French) | …, Online Requests | D…, Requests by other c…, Total number of req…

## g0707（1 列）
- 見出し：Sectors (French) | Secteurs (francais)
- 例1 値：Institutions fédérales | Manufacturier | Petites et moyennes entreprises (PME) | Autres paliers de gouvernement | Innovation
  - 同じ表の列：Sectors (English) |…, Online Requests | D…, Requests by other c…, Total number of req…

## g0708（1 列）
- 見出し：Online Requests | Demandes en ligne
- 例1 値：0 | 523 | 2 | 0 | 0
  - 同じ表の列：Sectors (English) |…, Sectors (French) | …, Requests by other c…, Total number of req…

## g0709（1 列）
- 見出し：Requests by other channels | Demandes par autres voies
- 例1 値：5 | 145 | 6 | 4 | 1
  - 同じ表の列：Sectors (English) |…, Sectors (French) | …, Online Requests | D…, Total number of req…

## g0710（1 列）
- 見出し：Total number of requests received Nombre total de demandes r
- 例1 値：4 | 6 | 1971 | 189 | 1038
  - 同じ表の列：Sectors (English) |…, Sectors (French) | …, Online Requests | D…, Requests by other c…

## g0711（3 列）
- 見出し：departmental_identification_number
- 例1 値：OI-1014 | OI-1153 | OI-1084 | OI-1153 | OI-1014
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published
- 例2 値：OI-461 | OI-1138 | OI-1104 | OI-1104 | OI-462
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0712（1 列）
- 見出し：title_translated_en
- 例1 値：Yogurt Quota Holders List - 2018 | Accountant’s letter - CPTPP: Yogurt and… | CPTPP: Yogurt and Buttermilk TRQ - Seri… | CUSMA Yogurt and Buttermilk Quota Holde… | Yogurt Quota Holders List - 2017
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0713（1 列）
- 見出し：title_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Liste des Détenteurs de Contingent de y… | Liste des détenteurs de contingent du y… | Liste des détenteurs de contingent du y… | Liste des détenteurs de contingent pour…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0714（1 列）
- 見出し：notes_translated_en
- 例1 値：CPTPP: Yogurt and Buttermilk TRQ | Skim Milk Powder and Milk Protein Conce… | CPTPP: Yogurt and Buttermilk TRQ | Notice to Importers Yogurt (Item 158 on… | WTO Yogurt Quota Holders List.
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0715（1 列）
- 見出し：notes_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Avis aux importateurs Yoghourt (Article… | OMC : CT du Yogourt | Liste des détenteurs de contingent pour… | PTPGP : CT du yogourt et du babeurre
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0716（3 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0717（3 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0718（2 列）
- 見出し：subject
- 例1 値：Economics and Industry | Economics and Industry | Economics and Industry | Economics and Industry | Economics and Industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published
- 例2 値：Economics and Industry | Economics and Industry | Economics and Industry | Economics and Industry | Economics and Industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0719（3 列）
- 見出し：date_published
- 例1 値：2019-10-01 | 2023-10-18 | 2012-11-20 | 2016-10-21 | 2013-06-24
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：2022-01-06 | 2022-01-04 | 2019-02-05 | 2018-02-28 | 2014-10-31
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0720（3 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## 答えの雛形

```
g0601	
g0602	
g0603	
g0604	
g0605	
g0606	
g0607	
g0608	
g0609	
g0610	
g0611	
g0612	
g0613	
g0614	
g0615	
g0616	
g0617	
g0618	
g0619	
g0620	
g0621	
g0622	
g0623	
g0624	
g0625	
g0626	
g0627	
g0628	
g0629	
g0630	
g0631	
g0632	
g0633	
g0634	
g0635	
g0636	
g0637	
g0638	
g0639	
g0640	
g0641	
g0642	
g0643	
g0644	
g0645	
g0646	
g0647	
g0648	
g0649	
g0650	
g0651	
g0652	
g0653	
g0654	
g0655	
g0656	
g0657	
g0658	
g0659	
g0660	
g0661	
g0662	
g0663	
g0664	
g0665	
g0666	
g0667	
g0668	
g0669	
g0670	
g0671	
g0672	
g0673	
g0674	
g0675	
g0676	
g0677	
g0678	
g0679	
g0680	
g0681	
g0682	
g0683	
g0684	
g0685	
g0686	
g0687	
g0688	
g0689	
g0690	
g0691	
g0692	
g0693	
g0694	
g0695	
g0696	
g0697	
g0698	
g0699	
g0700	
g0701	
g0702	
g0703	
g0704	
g0705	
g0706	
g0707	
g0708	
g0709	
g0710	
g0711	
g0712	
g0713	
g0714	
g0715	
g0716	
g0717	
g0718	
g0719	
g0720	
```
