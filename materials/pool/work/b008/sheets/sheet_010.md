# ラベル用シート 010 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_010.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1081（1 列）
- 見出し：unsafe_2004
- 例1 値：19 | 6 | 0.3734801131946388 | 492 | 7899
  - 同じ表の列：unsafe_, unsafe_2006, unsafe_2008, unsafe_2010, unsafe_2012, unsafe_2014

## g1082（1 列）
- 見出し：unsafe_2006
- 例1 値：8 | 7353 | 600.5 | 0.4657706404920171 | 22
  - 同じ表の列：unsafe_, unsafe_2004, unsafe_2008, unsafe_2010, unsafe_2012, unsafe_2014

## g1083（1 列）
- 見出し：unsafe_2008
- 例1 値：5 | 749.751 | 11246 | 0.5108101957449186 | 20
  - 同じ表の列：unsafe_, unsafe_2004, unsafe_2006, unsafe_2010, unsafe_2012, unsafe_2014

## g1084（1 列）
- 見出し：unsafe_2010
- 例1 値：708.3251741336063 | 7 | 12140 | 19 | 0.4672135687904447
  - 同じ表の列：unsafe_, unsafe_2004, unsafe_2006, unsafe_2008, unsafe_2012, unsafe_2014

## g1085（1 列）
- 見出し：unsafe_2012
- 例1 値：12117 | 8 | 664.391711227076 | 0.4672135687904447 | 18
  - 同じ表の列：unsafe_, unsafe_2004, unsafe_2006, unsafe_2008, unsafe_2010, unsafe_2014

## g1086（1 列）
- 見出し：unsafe_2014
- 例1 値：0.4467022192266121 | 12835.818456526027 | 6 | 730.1124422149361 | 21
  - 同じ表の列：unsafe_, unsafe_2004, unsafe_2006, unsafe_2008, unsafe_2010, unsafe_2012

## g1087（5 列）
- 見出し：STATISTIC
- 例1 値：G0118C01 | G0118C01 | G0118C01 | G0118C02 | G0118C02
  - 同じ表の列：Statistic, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE
- 例2 値：VCA02C1 | VCA02C1 | VCA02C1 | VCA02C1 | VCA02C1
  - 同じ表の列：Statistic, TLIST(A1), Year, C03749V04498, Product, C03748V04497, Country, UNIT

## g1088（1 列）
- 見出し：Statistic
- 例1 値：Official development assistance (ODA) p… | Official development assistance (ODA) p… | Official development assistance (ODA) p… | Official development assistance (ODA) p… | Official development assistance (ODA) p…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g1089（2 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, State, UNIT, VALUE
- 例2 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, State, UNIT, VALUE

## g1090（2 列）
- 見出し：UNIT
- 例1 値：% | % | % | % | %
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, VALUE
- 例2 値：% | % | % | % | %
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02582V03134, C02496V03023, Factor, C02625V03183

## g1091（3 列）
- 見出し：VALUE
- 例1 値：13 | 13 | 80 | 80
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, UNIT
- 例2 値：30 | 47 | 2358 | 29 | 467
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03012V03633, Independent-Private…, UNIT

## g1092（1 列）
- 見出し：attributes__OBJECTID
- 例1 値：44909 | 67952 | 57283 | 113748 | 91570
  - 同じ表の列：attributes__ENTITY_…, attributes__SMRS, long, lat, geometry__spatialRe…

## g1093（1 列）
- 見出し：attributes__ENTITY_ID
- 例1 値：RO04213 | GA02258 | CO14486 | DG03410 | LF01364
  - 同じ表の列：attributes__OBJECTID, attributes__SMRS, long, lat, geometry__spatialRe…

## g1094（1 列）
- 見出し：attributes__SMRS
- 例1 値：CL033-082001- | KE002-045---- | SL014-209001- | OF039-003007- | DG093-013001-
  - 同じ表の列：attributes__OBJECTID, attributes__ENTITY_…, long, lat, geometry__spatialRe…

## g1095（2 列）
- 見出し：long
- 例1 値：-6.491691121 | -8.259317059 | -7.105393048 | -8.297019768 | -9.620079083
  - 同じ表の列：attributes__OBJECTID, attributes__ENTITY_…, attributes__SMRS, lat, geometry__spatialRe…
- 例2 値：-6.26668635262603 | -6.13595641515765 | -6.0901021357027 | -6.17618456417894 | -6.37331795423454
  - 同じ表の列：Polling_Station_ID, Location, When_To_Vote_Here, LAT

## g1096（2 列）
- 見出し：lat
- 例1 値：51.79300787 | 52.65040353 | 54.03718746 | 53.10781816 | 51.77218264
  - 同じ表の列：attributes__OBJECTID, attributes__ENTITY_…, attributes__SMRS, long, geometry__spatialRe…
- 例2 値：53.4540654303328 | 53.4222165718242 | 53.4526106987322 | 53.4393892333821 | 53.4489127941346
  - 同じ表の列：Polling_Station_ID, Location, When_To_Vote_Here, LONG

## g1097（1 列）
- 見出し：geometry__spatialReference__wkid
- 例1 値：4326 | 4326 | 4326 | 4326 | 4326
  - 同じ表の列：attributes__OBJECTID, attributes__ENTITY_…, attributes__SMRS, long, lat

## g1098（1 列）
- 見出し：Type
- 例1 値：FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli…
  - 同じ表の列：Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1099（1 列）
- 見出し：Status
- 例1 値：Received | Received | Refused | Refused | Granted
  - 同じ表の列：Type, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1100（1 列）
- 見出し：Nationality
- 例1 値：Åland Islands | Lebanon | Thailand | Cambodia | Guam
  - 同じ表の列：Type, Status, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1101（1 列）
- 見出し：unsafe_2017
- 例1 値：* | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1102（1 列）
- 見出し：unsafe_2018
- 例1 値：7 | * | * | 0 | *
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g1103（1 列）
- 見出し：unsafe_2019
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2020, unsafe_2021, unsafe_2022

## g1104（1 列）
- 見出し：unsafe_2020
- 例1 値：0 | 10 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2021, unsafe_2022

## g1105（1 列）
- 見出し：unsafe_2021
- 例1 値：0 | * | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2022

## g1106（1 列）
- 見出し：unsafe_2022
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g1107（1 列）
- 見出し：unsafe_2023
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g1108（1 列）
- 見出し：Metric
- 例1 値：Resources With Broken Links | High Value Datasets | ga:avgSessionDuration | totalUsers | Active Orgs with Datasets
  - 同じ表の列：4-2018, 5-2018, 6-2018, 7-2018, 8-2018, 9-2018, 10-2018, 11-2018

## g1109（1 列）
- 見出し：4-2018
- 例1 値：4.51 | 105 | No data | 12941 | 6160
  - 同じ表の列：Metric, 5-2018, 6-2018, 7-2018, 8-2018, 9-2018, 10-2018, 11-2018

## g1110（1 列）
- 見出し：5-2018
- 例1 値：17570 | 7920 | 69826 | 1989 | 577
  - 同じ表の列：Metric, 4-2018, 6-2018, 7-2018, 8-2018, 9-2018, 10-2018, 11-2018

## g1111（1 列）
- 見出し：6-2018
- 例1 値：No data | 10518 | 14241 | 61067 | 568
  - 同じ表の列：Metric, 4-2018, 5-2018, 7-2018, 8-2018, 9-2018, 10-2018, 11-2018

## g1112（1 列）
- 見出し：7-2018
- 例1 値：97 | 167 | 54863 | 13938 | 10729
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 8-2018, 9-2018, 10-2018, 11-2018

## g1113（1 列）
- 見出し：8-2018
- 例1 値：14 | No data | 13126 | 8592 | 251
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 7-2018, 9-2018, 10-2018, 11-2018

## g1114（1 列）
- 見出し：9-2018
- 例1 値：70 | 12757 | No data | 3110 | No data
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 7-2018, 8-2018, 10-2018, 11-2018

## g1115（1 列）
- 見出し：10-2018
- 例1 値：36 | 21482 | No data | No data | No data
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 7-2018, 8-2018, 9-2018, 11-2018

## g1116（1 列）
- 見出し：11-2018
- 例1 値：4.93 | No data | No data | 71 | 106768
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 7-2018, 8-2018, 9-2018, 10-2018

## g1117（1 列）
- 見出し：12-2018
- 例1 値：3110 | No data | 10944 | 56430 | 8698
  - 同じ表の列：Metric, 4-2018, 5-2018, 6-2018, 7-2018, 8-2018, 9-2018, 10-2018

## g1118（1 列）
- 見出し：Time
- 例1 値：Jan 15, 2021 7:00 PM | Jan 2, 2021 5:00 AM | Jan 25, 2021 11:00 PM | Feb 1, 2021 2:00 PM | Jan 21, 2021 10:00 PM
  - 同じ表の列：Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1119（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Pedestrian
- 例1 値：280 | 37 | 23 | 427 | 137
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1120（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Peds IN
- 例1 値：70 | 94 | 66 | 114 | 29
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1121（1 列）
- 見出し：Dun Laoghaire @ Peoples Park Peds OUT
- 例1 値：18 | 123 | 17 | 137 | 83
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1122（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Pedestrian
- 例1 値：73 | 15 | 77 | 3 | 1
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1123（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Peds IN
- 例1 値：14 | 32 | 2 | 25 | 16
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1124（1 列）
- 見出し：Dun Laoghaire @ Seapoint Beach Peds OUT
- 例1 値：25 | 16 | 13 | 29 | 37
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…, Dun Laoghaire @ Yor…

## g1125（1 列）
- 見出し：Dun Laoghaire @ York Road Pedestrian
- 例1 値：43 | 22 | 63 | 28 | 3
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…

## g1126（1 列）
- 見出し：Dun Laoghaire @ York Road Peds IN
- 例1 値：11 | 19 | 60 | 68 | 30
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…

## g1127（1 列）
- 見出し：Dun Laoghaire @ York Road Peds OUT
- 例1 値：21 | 36 | 8 | 12 | 4
  - 同じ表の列：Time, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Peo…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Sea…, Dun Laoghaire @ Yor…

## g1128（1 列）
- 見出し：Territory
- 例1 値：RoI | NI | RoI | NI | RoI
  - 同じ表の列：County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CCS kWs, CHAdeMO kWs

## g1129（1 列）
- 見出し：nr__chargers
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Territory, County, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CCS kWs, CHAdeMO kWs

## g1130（1 列）
- 見出し：max__sim__ccs
- 例1 値：2 | 1 | 1 | 1 | 2
  - 同じ表の列：Territory, County, nr__chargers, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CCS kWs, CHAdeMO kWs

## g1131（1 列）
- 見出し：max__sim__chademo
- 例1 値：1 | 1 | 1 | 2 | 2
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__fast_ac, max__sim__ac_socket, CCS kWs, CHAdeMO kWs

## g1132（1 列）
- 見出し：max__sim__fast_ac
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__ac_socket, CCS kWs, CHAdeMO kWs

## g1133（1 列）
- 見出し：max__sim__ac_socket
- 例1 値：1 | 1 | 2 | 2 | 2
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, CCS kWs, CHAdeMO kWs

## g1134（1 列）
- 見出し：CCS kWs
- 例1 値：50 | 150, 50 | 200(8) | 50 | 50
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CHAdeMO kWs

## g1135（1 列）
- 見出し：CHAdeMO kWs
- 例1 値：50 | 50 | 50 | 50 | 50
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CCS kWs

## g1136（1 列）
- 見出し：AC Fast kWs
- 例1 値：43 | 43 | 43 | 43 | 43
  - 同じ表の列：Territory, County, nr__chargers, max__sim__ccs, max__sim__chademo, max__sim__fast_ac, max__sim__ac_socket, CCS kWs

## g1137（1 列）
- 見出し：Statistic
- 例1 値：Agricultural Output | Agricultural Output | Agricultural Output | Agricultural Output | Agricultural Output
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C03749V04498, Product, C03748V04497, Country, UNIT

## g1138（1 列）
- 見出し：C03749V04498
- 例1 値：1.3 | 1.2 | 1.4 | 1.6 | 1.6
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Product, C03748V04497, Country, UNIT

## g1139（1 列）
- 見出し：Product
- 例1 値：Agricultural and animal husbandry servi… | Agricultural and animal husbandry servi… | Non-perennial crops | Live animals and animal products | Non-perennial crops
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03749V04498, C03748V04497, Country, UNIT

## g1140（1 列）
- 見出し：C03748V04497
- 例1 値：CY | GR | HR | SI | LU
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03749V04498, Product, Country, UNIT

## g1141（1 列）
- 見出し：Country
- 例1 値：United Kingdom | Sweden | Estonia | France | Lithuania
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03749V04498, Product, C03748V04497, UNIT

## g1142（1 列）
- 見出し：UNIT
- 例1 値：€million | €million | €million | €million | €million
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03749V04498, Product, C03748V04497, Country

## g1143（1 列）
- 見出し：Is Free To Visit
- 例1 値：Yes | No | No | No | No
  - 同じ表の列：Event Type, County, Price, Start Date, End Date, Start Time, End Time, Recurring Dates

## g1144（1 列）
- 見出し：Price
- 例1 値：28.50 | 20 | 5.5 | 80 | 20
  - 同じ表の列：Event Type, County, Is Free To Visit, Start Date, End Date, Start Time, End Time, Recurring Dates

## g1145（1 列）
- 見出し：Start Time
- 例1 値：11:30 | 12:00 | 19:30 | 19:30 | 20:00
  - 同じ表の列：Event Type, County, Is Free To Visit, Price, Start Date, End Date, End Time, Recurring Dates

## g1146（1 列）
- 見出し：End Time
- 例1 値：06:30 | 20:00 | 20:00 | 20:00 | 13:50
  - 同じ表の列：Event Type, County, Is Free To Visit, Price, Start Date, End Date, Start Time, Recurring Dates

## g1147（1 列）
- 見出し：Recurring Dates
- 例1 値：Yes | No | No | Yes | Yes
  - 同じ表の列：Event Type, County, Is Free To Visit, Price, Start Date, End Date, Start Time, End Time

## g1148（1 列）
- 見出し：Polling_Station_ID
- 例1 値：14 | 21 | 33 | 27 | 2
  - 同じ表の列：Location, When_To_Vote_Here, LAT, LONG

## g1149（1 列）
- 見出し：Location
- 例1 値：Kinsealy | Lusk | Skerries | Bayside | Santry Parish Centre
  - 同じ表の列：Polling_Station_ID, When_To_Vote_Here, LAT, LONG

## g1150（1 列）
- 見出し：When_To_Vote_Here
- 例1 値：Local, Dáil, Referenda, Presidential | Local, Dáil, Referenda, Presidential | Local, Dáil, Referenda, Presidential | Local, Dáil, Referenda, Presidential | Local, Dáil, Referenda, Presidential
  - 同じ表の列：Polling_Station_ID, Location, LAT, LONG

## g1151（1 列）
- 見出し：Date
- 例1 値：2018-12-28T00:00:00 | 2020-02-21T00:00:00 | 2020-09-19T00:00:00 | 2018-11-25T00:00:00 | 2018-10-30T00:00:00
  - 同じ表の列：Inch Entry, Corrib, Moffat ROI, Total ROI supplies

## g1152（1 列）
- 見出し：Inch Entry
- 例1 値：12.495639 | 4.62225 | 8.740972 | 6.512028 | 6.587889
  - 同じ表の列：Date, Corrib, Moffat ROI, Total ROI supplies

## g1153（1 列）
- 見出し：Corrib
- 例1 値：78.255367 | 75.00496 | 57.063898 | 89.042764 | 100.334303
  - 同じ表の列：Date, Inch Entry, Moffat ROI, Total ROI supplies

## g1154（1 列）
- 見出し：Moffat ROI
- 例1 値：56.34305499999999 | 125.83861 | 94.889444 | 47.523611 | 119.063334
  - 同じ表の列：Date, Inch Entry, Corrib, Total ROI supplies

## g1155（1 列）
- 見出し：Total ROI supplies
- 例1 値：147.765403 | 173.609757 | 127.39119099999999 | 199.152582 | 109.180298
  - 同じ表の列：Date, Inch Entry, Corrib, Moffat ROI

## g1156（1 列）
- 見出し：Economic Sector
- 例1 値：L-Real Estate Activities | H-Transportation and Storage | M-Professional, Scientific and Technica… | P-Education | F-Construction
  - 同じ表の列：unsafe_2026_fatalit…

## g1157（1 列）
- 見出し：unsafe_2026_fatalities
- 例1 値：1 | 1 | 24 | 1 | 2
  - 同じ表の列：Economic Sector

## g1158（1 列）
- 見出し：Statistic
- 例1 値：Hepatitis B incidence | Notifications of Hepatitis B | Hepatitis B incidence | Notifications of Hepatitis B | Hepatitis B incidence
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, UNIT, VALUE

## g1159（1 列）
- 見出し：C02196V02652
- 例1 値：IE12 | IE22 | IE25 | IE25 | IE21
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, NUTS 3 Regions, UNIT, VALUE

## g1160（1 列）
- 見出し：NUTS 3 Regions
- 例1 値：South-West | Mid-West | South-East | Midland | State
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, UNIT, VALUE

## g1161（1 列）
- 見出し：UNIT
- 例1 値：Number | Rate per 100,000 Pop. | Number | Rate per 100,000 Pop. | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, VALUE

## g1162（1 列）
- 見出し：VALUE
- 例1 値：20 | 12.8 | 25 | 10.3 | 31
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, UNIT

## g1163（1 列）
- 見出し：C03012V03633
- 例1 値：02 | 031 | 09 | 031 | 08
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Independent-Private…, UNIT, VALUE

## g1164（1 列）
- 見出し：Independent-Private and Private-Charitable Centre
- 例1 値：Kylemore Clinic, Dublin | Highfield Hospital, Dublin (2) | Total independent/private and private c… | Hampstead and Highfield Hospital, Dublin | Hampstead Hospital, Dublin
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03012V03633, UNIT, VALUE

## g1165（1 列）
- 見出し：Statistic
- 例1 値：Important Factors to Enterprises Hamper… | Important Factors to Enterprises Hamper… | Important Factors to Enterprises Hamper… | Important Factors to Enterprises Hamper… | Important Factors to Enterprises Hamper…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02582V03134, C02496V03023, Factor, C02625V03183, Ranking

## g1166（1 列）
- 見出し：C02582V03134
- 例1 値：- | 02 | - | 01 | 01
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02496V03023, Factor, C02625V03183, Ranking

## g1167（1 列）
- 見出し：C02496V03023
- 例1 値：14 | 14 | 13 | 13 | 13
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02582V03134, Factor, C02625V03183, Ranking

## g1168（1 列）
- 見出し：Factor
- 例1 値：Lack of relevant industry experience on… | Company research and development activi… | Lack of relevant industry experience on… | Company research and development activi… | Company research and development activi…
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02582V03134, C02496V03023, C02625V03183, Ranking

## g1169（1 列）
- 見出し：C02625V03183
- 例1 値：1 | 2 | 1 | 1 | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02582V03134, C02496V03023, Factor, Ranking

## g1170（1 列）
- 見出し：Ranking
- 例1 値：Low/not relevant | Low/not relevant | Low/not relevant | Medium | Medium
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02582V03134, C02496V03023, Factor, C02625V03183

## g1171（1 列）
- 見出し：Sessions
- 例1 値：143700 | 294431 | 128553 | 373369 | 254223
  - 同じ表の列：Year, Users, pageviews

## g1172（1 列）
- 見出し：Users
- 例1 値：72453 | 133856 | 88586 | 195692 | 162439
  - 同じ表の列：Year, Sessions, pageviews

## g1173（1 列）
- 見出し：pageviews
- 例1 値：670214 | 1334687 | 1439530 | 859752 | 468438
  - 同じ表の列：Year, Sessions, Users

## g1174（1 列）
- 見出し：Channels of Engagement
- 例1 値：Connacht/Ulster | Over Phone | National | Public Meeting | In Person5
  - 同じ表の列：unsafe_2021, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g1175（1 列）
- 見出し：unsafe_2021
- 例1 値：N= | 41 | 28 | 76 | 26
  - 同じ表の列：Channels of Engagem…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g1176（1 列）
- 見出し：unsafe_
- 例1 値：67 | 18-24 | 43 | 62 | 70
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g1177（1 列）
- 見出し：unsafe__2
- 例1 値：180 | 75 | 5 The In Person figure for 2021 = In Pe… | 106 | 90
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe_, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g1178（2 列）
- 見出し：unsafe__3
- 例1 値：72 | 37 | 71 | 9 | 54
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe_, unsafe__2, unsafe__4, unsafe__5, unsafe__6
- 例2 値：2 | 0 | 0 | 2 | 0
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__2

## g1179（1 列）
- 見出し：unsafe__4
- 例1 値：54 | 11 | 23 | 85 | 40
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe_, unsafe__2, unsafe__3, unsafe__5, unsafe__6

## g1180（1 列）
- 見出し：unsafe__5
- 例1 値：79 | 33 | 73 | 149 | 55-64
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__6

## g1181（1 列）
- 見出し：unsafe__6
- 例1 値：331 | 104 | 84 | 94 | 65+
  - 同じ表の列：Channels of Engagem…, unsafe_2021, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5

## g1182（1 列）
- 見出し：time
- 例1 値：2024-04-07T07:00:00Z | 2024-04-03T18:00:00Z | 2024-04-02T21:00:00Z | 2024-04-06T18:30:00Z | 2024-04-04T00:30:00Z
  - 同じ表の列：stationID, significant_wave_he…, mean_wave_period, mean_wave_direction, wave_power_per_unit…, peak_period, energy_period

## g1183（1 列）
- 見出し：stationID
- 例1 値：Belmullet_Inner | Belmullet_Outer | Ballybunnion | Belmullet_Inner | Belmullet_Inner
  - 同じ表の列：time, significant_wave_he…, mean_wave_period, mean_wave_direction, wave_power_per_unit…, peak_period, energy_period

## g1184（1 列）
- 見出し：significant_wave_height
- 例1 値：3.56307 | 2.90843 | 2.63359 | 2.56774 | 1.53927
  - 同じ表の列：time, stationID, mean_wave_period, mean_wave_direction, wave_power_per_unit…, peak_period, energy_period

## g1185（1 列）
- 見出し：mean_wave_period
- 例1 値：2.6942 | 5.5597 | 6.4692 | 3.1059 | 3.1726
  - 同じ表の列：time, stationID, significant_wave_he…, mean_wave_direction, wave_power_per_unit…, peak_period, energy_period

## g1186（1 列）
- 見出し：mean_wave_direction
- 例1 値：273.055 | 306.973 | 56.071 | 23.719 | 319.699
  - 同じ表の列：time, stationID, significant_wave_he…, mean_wave_period, wave_power_per_unit…, peak_period, energy_period

## g1187（1 列）
- 見出し：wave_power_per_unit_crest_length
- 例1 値：18.278311290443852 | 110.015907279361 | 14.693924172346954 | 246.65062574987132 | 9.032090008733757
  - 同じ表の列：time, stationID, significant_wave_he…, mean_wave_period, mean_wave_direction, peak_period, energy_period

## g1188（1 列）
- 見出し：peak_period
- 例1 値：10.852 | 11.5648 | 12.6103 | 11.5656 | 9.3855
  - 同じ表の列：time, stationID, significant_wave_he…, mean_wave_period, mean_wave_direction, wave_power_per_unit…, energy_period

## g1189（1 列）
- 見出し：energy_period
- 例1 値：8.8819 | 11.347 | 9.0379 | 7.4409 | 5.0694
  - 同じ表の列：time, stationID, significant_wave_he…, mean_wave_period, mean_wave_direction, wave_power_per_unit…, peak_period

## g1190（1 列）
- 見出し：Statistic Label
- 例1 値：Total Sunshine Hours | Total Sunshine Hours | Total Sunshine Hours | Total Sunshine Hours | Total Sunshine Hours
  - 同じ表の列：STATISTIC, tlist_m1_, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g1191（1 列）
- 見出し：tlist_m1_
- 例1 値：195905 | 195807 | 196205 | 196004 | 196101
  - 同じ表の列：STATISTIC, Statistic Label, Month, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g1192（1 列）
- 見出し：Month
- 例1 値：1962M06 | 1960M08 | 1961M04 | 1962M11 | 1962M04
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, C02431V02938, Meteorological Weat…, UNIT, VALUE

## g1193（1 列）
- 見出し：C02431V02938
- 例1 値：007 | 004 | 002 | 008 | 004
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, Meteorological Weat…, UNIT, VALUE

## g1194（1 列）
- 見出し：Meteorological Weather Station
- 例1 値：Birr | Valentia Observatory | Dublin airport | Shannon airport | Shannon airport
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, C02431V02938, UNIT, VALUE

## g1195（1 列）
- 見出し：application_reference_no
- 例1 値：DAC2303804LL | DAC2512036CY | DAC2306093KK | DAC2512719WH | DAC2303681WW
  - 同じ表の列：application_type, local_authority, submission_no, submission_date, date_permission_was…, planning_permission…, classification_of_w…, location_of_the_pro…

## g1196（1 列）
- 見出し：application_type
- 例1 値：disability_access_certificate_applicati… | disability_access_certificate_applicati… | disability_access_certificate_applicati… | disability_access_certificate_applicati… | disability_access_certificate_applicati…
  - 同じ表の列：application_referen…, local_authority, submission_no, submission_date, date_permission_was…, planning_permission…, classification_of_w…, location_of_the_pro…

## g1197（1 列）
- 見出し：local_authority
- 例1 値：Limerick City and County Council | Dún-Laoghaire Rathdown County Council | Cork County Council | Fingal County Council | Dublin City Council
  - 同じ表の列：application_referen…, application_type, submission_no, submission_date, date_permission_was…, planning_permission…, classification_of_w…, location_of_the_pro…

## g1198（1 列）
- 見出し：submission_no
- 例1 値：4017348 | 4007768 | 4017772 | 4008498 | 4009347
  - 同じ表の列：application_referen…, application_type, local_authority, submission_date, date_permission_was…, planning_permission…, classification_of_w…, location_of_the_pro…

## g1199（1 列）
- 見出し：submission_date
- 例1 値：2022-11-14T00:00:00 | 2025-05-01T00:00:00 | 2025-03-31T00:00:00 | 2025-05-02T00:00:00 | 2025-03-19T00:00:00
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, date_permission_was…, planning_permission…, classification_of_w…, location_of_the_pro…

## g1200（1 列）
- 見出し：date_permission_was_granted
- 例1 値：2021-12-10T00:00:00 | 2022-10-11T00:00:00 | 2023-07-13T00:00:00 | 2022-11-03T00:00:00 | 2021-09-23T00:00:00
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, submission_date, planning_permission…, classification_of_w…, location_of_the_pro…

## 答えの雛形

```
g1081	
g1082	
g1083	
g1084	
g1085	
g1086	
g1087	
g1088	
g1089	
g1090	
g1091	
g1092	
g1093	
g1094	
g1095	
g1096	
g1097	
g1098	
g1099	
g1100	
g1101	
g1102	
g1103	
g1104	
g1105	
g1106	
g1107	
g1108	
g1109	
g1110	
g1111	
g1112	
g1113	
g1114	
g1115	
g1116	
g1117	
g1118	
g1119	
g1120	
g1121	
g1122	
g1123	
g1124	
g1125	
g1126	
g1127	
g1128	
g1129	
g1130	
g1131	
g1132	
g1133	
g1134	
g1135	
g1136	
g1137	
g1138	
g1139	
g1140	
g1141	
g1142	
g1143	
g1144	
g1145	
g1146	
g1147	
g1148	
g1149	
g1150	
g1151	
g1152	
g1153	
g1154	
g1155	
g1156	
g1157	
g1158	
g1159	
g1160	
g1161	
g1162	
g1163	
g1164	
g1165	
g1166	
g1167	
g1168	
g1169	
g1170	
g1171	
g1172	
g1173	
g1174	
g1175	
g1176	
g1177	
g1178	
g1179	
g1180	
g1181	
g1182	
g1183	
g1184	
g1185	
g1186	
g1187	
g1188	
g1189	
g1190	
g1191	
g1192	
g1193	
g1194	
g1195	
g1196	
g1197	
g1198	
g1199	
g1200	
```
