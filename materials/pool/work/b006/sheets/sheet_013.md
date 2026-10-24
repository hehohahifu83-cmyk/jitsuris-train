# ラベル用シート 013 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_013.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1441（1 列）
- 見出し：Collision Type
- 例1 値：OTHER | N/A | OPPOSITE DIRECTION SIDESWIPE | OPPOSITE DIRECTION SIDESWIPE | SINGLE VEHICLE
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Weather

## g1442（1 列）
- 見出し：Weather
- 例1 値：CLEAR | CLEAR | CLEAR | CLEAR | CLEAR
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Collision Type

## g1443（1 列）
- 見出し：Surface Condition
- 例1 値：N/A | DRY | WET | DRY | DRY
  - 同じ表の列：Report Number, Local Case Number, ACRS Report Type, Crash Date/Time, Route Type, Municipality, Related Non-Motorist, Collision Type

## g1444（1 列）
- 見出し：Application Number
- 例1 値：2018020283 | 2019070895 | 2018120627 | 2019090991 | 2020051163
  - 同じ表の列：Property City, Zone, Received, Status, Structure

## g1445（1 列）
- 見出し：Property City
- 例1 値：Clarksburg | Silver Spring | Rockville | Boyds | Gaithersburg
  - 同じ表の列：Application Number, Zone, Received, Status, Structure

## g1446（1 列）
- 見出し：Zone
- 例1 値：R-200 | R-10 | NR-0.75 | TS | R-60
  - 同じ表の列：Application Number, Property City, Received, Status, Structure

## g1447（1 列）
- 見出し：Received
- 例1 値：2018-11-08T00:00:00.000 | 2020-07-16T00:00:00.000 | 2018-02-19T00:00:00.000 | 2021-10-29T00:00:00.000 | 2019-03-14T00:00:00.000
  - 同じ表の列：Application Number, Property City, Zone, Status, Structure

## g1448（5 列）
- 見出し：Status
- 例1 値：Withdrawn | Recommended | Recommended | Recommended | Recommended
  - 同じ表の列：Application Number, Property City, Zone, Received, Structure
- 例2 値：Open | Open | Open | Open | Open
  - 同じ表の列：Administrative Unit…, School Branch, Category, County, City, Primary Administrat…, School Year

## g1449（1 列）
- 見出し：Structure
- 例1 値：Tower | Monopole | Monopole | Monopole | Monopole
  - 同じ表の列：Application Number, Property City, Zone, Received, Status

## g1450（1 列）
- 見出し：Bill No
- 例1 値：7-10E | 20-19 | 3-12 | 49-21E | 1-15
  - 同じ表の列：Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date, Effective Date

## g1451（1 列）
- 見出し：Title
- 例1 値：Animal Control - Retail Pet Stores | Contracts and Procurement - Wage Requir… | Special Capital Improvements Project - … | Special Capital Improvements Project - … | Expedited Bill 24-11, Taxes - Excise Ta…
  - 同じ表の列：Bill No, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date, Effective Date

## g1452（1 列）
- 見出し：Sponsor(s)
- 例1 値：[個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除]
  - 同じ表の列：Bill No, Title, Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date, Effective Date

## g1453（1 列）
- 見出し：Co-Sponsor(s)
- 例1 値：[個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除]
  - 同じ表の列：Bill No, Title, Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date, Effective Date

## g1454（1 列）
- 見出し：Introduction Date
- 例1 値：2012-11-27T00:00:00.000 | 2017-06-13T00:00:00.000 | 2014-11-25T00:00:00.000 | 2021-04-20T00:00:00.000 | 2013-12-10T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Expiration Date, Public Hearing Date, Action Date, Effective Date

## g1455（1 列）
- 見出し：Expiration Date
- 例1 値：2011-08-02T00:00:00.000 | 2014-03-11T00:00:00.000 | 2011-11-04T00:00:00.000 | 2011-10-27T00:00:00.000 | 2012-04-26T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Public Hearing Date, Action Date, Effective Date

## g1456（1 列）
- 見出し：Public Hearing Date
- 例1 値：2014-10-14T00:00:00.000 | 2026-07-14T00:00:00.000 | 2021-01-19T00:00:00.000 | 2001-03-23T00:00:00.000 | 2016-01-12T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Action Date, Effective Date

## g1457（1 列）
- 見出し：Action Date
- 例1 値：2023-05-16T00:00:00.000 | 2016-03-15T00:00:00.000 | 2016-06-28T00:00:00.000 | 2015-03-31T00:00:00.000 | 2013-10-22T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Effective Date

## g1458（1 列）
- 見出し：Effective Date
- 例1 値：2011-06-09T00:00:00.000 | 2021-05-25T00:00:00.000 | 2014-10-22T00:00:00.000 | 2019-01-15T00:00:00.000 | 2012-05-15T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date

## g1459（1 列）
- 見出し：Effective Date (2)
- 例1 値：2021-03-22T00:00:00.000 | 2022-07-01T00:00:00.000 | 2023-09-15T00:00:00.000 | 2020-08-01T00:00:00.000 | 2017-01-01T00:00:00.000
  - 同じ表の列：Bill No, Title, Sponsor(s), Co-Sponsor(s), Introduction Date, Expiration Date, Public Hearing Date, Action Date

## g1460（2 列）
- 見出し：Award Year
- 例1 値：FY2023 | FY2026 | FY2018 | FY2026 | FY2023
  - 同じ表の列：Recipient, $ Amount, Purpose
- 例2 値：FY2024 | FY2024 | FY2026 | FY2022 | FY2025
  - 同じ表の列：Organization Receiv…, Award Type, Amount

## g1461（1 列）
- 見出し：Recipient
- 例1 値：e-MSion, Inc. | Continuous Solutions LLC | Oregon Cascades West Council of Governm… | Center Mom, Inc. | Neuramedica
  - 同じ表の列：Award Year, $ Amount, Purpose

## g1462（1 列）
- 見出し：$ Amount
- 例1 値：5000 | 145000 | 50000 | 46228 | 25000
  - 同じ表の列：Award Year, Recipient, Purpose

## g1463（1 列）
- 見出し：Purpose
- 例1 値：Enzymes for Accelerated Plastic Recycli… | Chargeway Oregon Pilot Project with Par… | Software and Training for Decision-Maki… | Automated Window Opener Technology Deve… | Lithium Extraction Technology
  - 同じ表の列：Award Year, Recipient, $ Amount

## g1464（1 列）
- 見出し：LicNbr
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：Profession, LicType, DBA, Addr3, Addr4, City, State, Zipcode

## g1465（1 列）
- 見出し：Profession
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, LicType, DBA, Addr3, Addr4, City, State, Zipcode

## g1466（1 列）
- 見出し：LicType
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, DBA, Addr3, Addr4, City, State, Zipcode

## g1467（1 列）
- 見出し：DBA
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, Addr3, Addr4, City, State, Zipcode

## g1468（1 列）
- 見出し：Addr3
- 例1 値：[個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr4, City, State, Zipcode

## g1469（1 列）
- 見出し：Addr4
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr3, City, State, Zipcode

## g1470（1 列）
- 見出し：City
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr3, Addr4, State, Zipcode

## g1471（3 列）
- 見出し：State
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr3, Addr4, City, Zipcode
- 例2 値：MA | MA | MA | MA | MA
  - 同じ表の列：fc_num, supervisor, city, duration, circumstance, basis, vehicle_year, vehicle_state

## g1472（2 列）
- 見出し：Zipcode
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr3, Addr4, City, State
- 例2 値：01701 | 02125 | 02119 | 22182 | 02121
  - 同じ表の列：services_provided, mbe_wbe_cert, small_local_cert, veteran_cert, sdo_certified, city_registered, city, state

## g1473（1 列）
- 見出し：County
- 例1 値：[個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除] | [個人の記録のため削除]
  - 同じ表の列：LicNbr, Profession, LicType, DBA, Addr3, Addr4, City, State

## g1474（1 列）
- 見出し：Organization Receiving Award
- 例1 値：City of Beaverton | Tillamook County | Warm Springs Community Action Team | Wild Rivers Land Trust | City of John Day
  - 同じ表の列：Award Year, Award Type, Amount

## g1475（1 列）
- 見出し：Award Type
- 例1 値：Loan | Grant | Grant | Grant | Grant
  - 同じ表の列：Award Year, Organization Receiv…, Amount

## g1476（1 列）
- 見出し：Amount
- 例1 値：60000 | 125000 | 1950000 | 125000 | 150000
  - 同じ表の列：Award Year, Organization Receiv…, Award Type

## g1477（1 列）
- 見出し：Administrative Unit Number
- 例1 値：413362704 | 408116206 | 412679704 | 410146139 | 426510059
  - 同じ表の列：School Branch, Category, Status, County, City, Primary Administrat…, School Year

## g1478（1 列）
- 見出し：School Branch
- 例1 値：0000 | 0000 | 0000 | 0000 | 0000
  - 同じ表の列：Administrative Unit…, Category, Status, County, City, Primary Administrat…, School Year

## g1479（1 列）
- 見出し：Category
- 例1 値：Specialized Associate Degree | Private College and University | Private Licensed School | Private Licensed School | State University
  - 同じ表の列：Administrative Unit…, School Branch, Status, County, City, Primary Administrat…, School Year

## g1480（1 列）
- 見出し：County
- 例1 値：Philadelphia | Philadelphia | Out-of-State | Delaware | Lancaster
  - 同じ表の列：Administrative Unit…, School Branch, Category, Status, City, Primary Administrat…, School Year

## g1481（3 列）
- 見出し：City
- 例1 値：Washington | Bethlehem | Philadelphia | York | Monaca
  - 同じ表の列：Administrative Unit…, School Branch, Category, Status, County, Primary Administrat…, School Year
- 例2 値：DORCHESTER | BOSTON | BOSTON | ROXBURY | DORCHESTER
  - 同じ表の列：fc_num, supervisor, state, duration, circumstance, basis, vehicle_year, vehicle_state

## g1482（1 列）
- 見出し：Primary Administrator
- 例1 値：[個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除] | [個人名のため削除]
  - 同じ表の列：Administrative Unit…, School Branch, Category, Status, County, City, School Year

## g1483（1 列）
- 見出し：School Year
- 例1 値：SY2122 | SY2021 | SY2122 | SY2122 | SY2021
  - 同じ表の列：Administrative Unit…, School Branch, Category, Status, County, City, Primary Administrat…

## g1484（1 列）
- 見出し：Institution
- 例1 値：Benner Township (BEN) | Pittsburgh (PIT) | Community Corrections Center - Central | Pine Grove (PNG) | Quehanna Boot Camp (QUE)
  - 同じ表の列：Institution Type, County, Fiscal Year, Date, Corrections Populat…

## g1485（1 列）
- 見出し：Institution Type
- 例1 値：State Correctional Institution | State Correctional Institution | State Correctional Institution | State Correctional Institution | State Correctional Institution
  - 同じ表の列：Institution, County, Fiscal Year, Date, Corrections Populat…

## g1486（1 列）
- 見出し：County
- 例1 値：N/A | Lycoming | N/A | Huntingdon | N/A
  - 同じ表の列：Institution, Institution Type, Fiscal Year, Date, Corrections Populat…

## g1487（1 列）
- 見出し：Fiscal Year
- 例1 値：FY 2018-2019 | FY 2017-2018 | FY 2017-2018 | FY 2016-2017 | FY 2018-2019
  - 同じ表の列：Institution, Institution Type, County, Date, Corrections Populat…

## g1488（1 列）
- 見出し：Date
- 例1 値：2015-09-30T00:00:00.000 | 2018-03-31T00:00:00.000 | 2017-02-28T00:00:00.000 | 2017-01-31T00:00:00.000 | 2016-04-30T00:00:00.000
  - 同じ表の列：Institution, Institution Type, County, Fiscal Year, Corrections Populat…

## g1489（1 列）
- 見出し：Corrections Population
- 例1 値：2311 | 1151 | 483 | 1365 | 2298
  - 同じ表の列：Institution, Institution Type, County, Fiscal Year, Date

## g1490（1 列）
- 見出し：State Fiscal Year
- 例1 値：2021-2022 | 2017-2018 | 2013-2014 | 2012-2013 | 2013-2014
  - 同じ表の列：Ticket Sales, Prizes Paid, Retailer Commissions, FIPS County Code

## g1491（1 列）
- 見出し：Ticket Sales
- 例1 値：126729608 | 1401705 | 7443737 | 42078957 | 53575476
  - 同じ表の列：State Fiscal Year, Prizes Paid, Retailer Commissions, FIPS County Code

## g1492（1 列）
- 見出し：Prizes Paid
- 例1 値：18273268 | 13207486 | 247618081 | 64204366 | 7475708
  - 同じ表の列：State Fiscal Year, Ticket Sales, Retailer Commissions, FIPS County Code

## g1493（1 列）
- 見出し：Retailer Commissions
- 例1 値：3058641 | 1830098 | 5889272 | 401410 | 1616780
  - 同じ表の列：State Fiscal Year, Ticket Sales, Prizes Paid, FIPS County Code

## g1494（1 列）
- 見出し：FIPS County Code
- 例1 値：42041 | 42107 | 42081 | 42097 | 42069
  - 同じ表の列：State Fiscal Year, Ticket Sales, Prizes Paid, Retailer Commissions

## g1495（1 列）
- 見出し：ReportDate
- 例1 値：2021-02-28T10:00:00.000 | 2022-04-02T10:00:00.000 | 2020-07-22T10:00:00.000 | 2021-11-24T10:00:00.000 | 2022-09-06T10:00:00.000
  - 同じ表の列：TotalCases, CaseDelta, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests, NegDelta

## g1496（1 列）
- 見出し：TotalCases
- 例1 値：968540 | 145281 | 61701 | 1173854 | 878679
  - 同じ表の列：ReportDate, CaseDelta, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests, NegDelta

## g1497（1 列）
- 見出し：CaseDelta
- 例1 値：1077 | 401 | 471 | 624 | 2201
  - 同じ表の列：ReportDate, TotalCases, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests, NegDelta

## g1498（1 列）
- 見出し：TotalTests
- 例1 値：10306108.0 | 22702208.0 | 14781411.0 | 272931.0 | 64106.0
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests, NegDelta

## g1499（1 列）
- 見出し：TestsDelta
- 例1 値：24996.0 | 11008.0 | 48348.0 | 50720.0 | 19325.0
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, PosTestPercent, PosPercentDiff, NegativeTests, NegDelta

## g1500（1 列）
- 見出し：PosTestPercent
- 例1 値：5.72 | 3.07 | 13.78 | 10.93 | 3.74
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, TestsDelta, PosPercentDiff, NegativeTests, NegDelta

## g1501（1 列）
- 見出し：PosPercentDiff
- 例1 値：-0.01 | 0.05 | -0.04 | -0.02 | 0.09
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, TestsDelta, PosTestPercent, NegativeTests, NegDelta

## g1502（1 列）
- 見出し：NegativeTests
- 例1 値：4593887.0 | 4082547.0 | 313099.0 | 3065701.0 | 64363.0
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegDelta

## g1503（1 列）
- 見出し：NegDelta
- 例1 値：8729 | 7430 | 8376 | 0 | 5303
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests

## g1504（1 列）
- 見出し：bedsTotal
- 例1 値：1812.0 | 507.0 | 168.0 | 1496.0 | 632.0
  - 同じ表の列：ReportDate, TotalCases, CaseDelta, TotalTests, TestsDelta, PosTestPercent, PosPercentDiff, NegativeTests

## g1505（1 列）
- 見出し：Field Order
- 例1 値：175 | 161 | 96 | 118 | 228
  - 同じ表の列：Data Type, SDAT Field Number

## g1506（1 列）
- 見出し：Data Type
- 例1 値：money | text | text | text | text
  - 同じ表の列：Field Order, SDAT Field Number

## g1507（1 列）
- 見出し：SDAT Field Number
- 例1 値：256 | 30 | 167 | 141 | 157
  - 同じ表の列：Field Order, Data Type

## g1508（1 列）
- 見出し：uid
- 例1 値：Somerset2026-10-03T10:00:55 | Prince_George's2026-10-03T01:45:59 | Somerset2026-10-03T06:00:58 | Frederick2026-10-03T02:31:01 | Garrett2026-10-03T08:16:01
  - 同じ表の列：area, outages, customers, percent_out, dt_stamp

## g1509（1 列）
- 見出し：area
- 例1 値：Caroline | Somerset | Kent | Garrett | Baltimore
  - 同じ表の列：uid, outages, customers, percent_out, dt_stamp

## g1510（1 列）
- 見出し：outages
- 例1 値：0 | 0 | 0 | 0 | 4
  - 同じ表の列：uid, area, customers, percent_out, dt_stamp

## g1511（1 列）
- 見出し：customers
- 例1 値：377956 | 76616 | 55584 | 359950 | 24136
  - 同じ表の列：uid, area, outages, percent_out, dt_stamp

## g1512（1 列）
- 見出し：percent_out
- 例1 値：0.008201158003510097 | 0.0035827526288447413 | 0.004901258492372888 | 0.0 | 0.1503894701663282
  - 同じ表の列：uid, area, outages, customers, dt_stamp

## g1513（1 列）
- 見出し：dt_stamp
- 例1 値：2026-10-03T07:15:58.000 | 2026-10-03T06:30:58.000 | 2026-10-03T09:30:58.000 | 2026-10-03T06:16:03.000 | 2026-10-03T02:00:57.000
  - 同じ表の列：uid, area, outages, customers, percent_out

## g1514（1 列）
- 見出し：ID_ATRATIVO_TURISTICO
- 例1 値：185 | 188 | 81 | 62 | 46
  - 同じ表の列：CATEGORIA, NUMERO, REF_LOCALIZACAO, GEOMETRIA

## g1515（1 列）
- 見出し：CATEGORIA
- 例1 値：CULTURAL | NATURAL | CULTURAL | NATURAL | ENTRETENIMENTO E LAZER
  - 同じ表の列：ID_ATRATIVO_TURISTI…, NUMERO, REF_LOCALIZACAO, GEOMETRIA

## g1516（1 列）
- 見出し：NUMERO
- 例1 値：580 | 8000 | 452 | 904 | -
  - 同じ表の列：ID_ATRATIVO_TURISTI…, CATEGORIA, REF_LOCALIZACAO, GEOMETRIA

## g1517（1 列）
- 見出し：REF_LOCALIZACAO
- 例1 値：- | - | - | - | -
  - 同じ表の列：ID_ATRATIVO_TURISTI…, CATEGORIA, NUMERO, GEOMETRIA

## g1518（9 列）
- 見出し：GEOMETRIA
- 例1 値：POINT (606796.977091737 7802055.9935506… | POINT (613015.861342525 7800362.0580761… | POINT (610147.715992706 7795119.5969960… | POINT (611523.396197928 7797214.9920302… | POINT (609715.098793442 7806358.2101827…
  - 同じ表の列：ID_ATRATIVO_TURISTI…, CATEGORIA, NUMERO, REF_LOCALIZACAO
- 例2 値：POINT (611798.264178478 7801003.7630972) | POINT (607667.33690123 7807111.56407965) | POINT (607631.868984122 7807284.2083377… | POINT (604782.141231819 7807782.3578446… | POINT (604986.05447495 7807823.89046938)
  - 同じ表の列：ID_NTCV

## g1519（1 列）
- 見出し：respondent_id
- 例1 値：11184844521 | 11185212086 | 11185196714 | 11186165371 | 11183432073
  - 同じ表の列：FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, RegionalTouE, BairroUtrabalha

## g1520（1 列）
- 見出し：FaixaIdade
- 例1 値：De 35 a 44 anos | De 35 a 44 anos | De 45 a 59 anos | De 25 a 34 anos | De 35 a 44 anos
  - 同じ表の列：respondent_id, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, RegionalTouE, BairroUtrabalha

## g1521（1 列）
- 見出し：Escolaridade
- 例1 値：Ensino Medio completo_tecnico | Ensino Fundamental completo | Ensino Superior completo | Ensino Superior completo | Outro _especifique_
  - 同じ表の列：respondent_id, FaixaIdade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, RegionalTouE, BairroUtrabalha

## g1522（1 列）
- 見出し：EscolaridadeOutro
- 例1 値：Ensino Superior Incompleto | Ensino superior cursando | Fundamental incompleto | Superior incompleto | Fundamental Incompleto
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, Renda familiar, RegionalMora, BairroUMora, RegionalTouE, BairroUtrabalha

## g1523（1 列）
- 見出し：Renda familiar
- 例1 値：Entre 1 SM e 3 SM _ RS 998,01 a RS 2994… | NS | Entre 1 SM e 3 SM _ RS 998,01 a RS 2994… | Entre 1 SM e 3 SM _ RS 998,01 a RS 2994… | Nao possui renda
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, RegionalMora, BairroUMora, RegionalTouE, BairroUtrabalha

## g1524（1 列）
- 見出し：RegionalMora
- 例1 値：Noroeste | Noroeste | Nordeste | Centro Sul | Nordeste
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, BairroUMora, RegionalTouE, BairroUtrabalha

## g1525（1 列）
- 見出し：BairroUMora
- 例1 値：Floresta | Jardim dos Comerciarios | Santa Monica | Leticia | Prado
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, RegionalTouE, BairroUtrabalha

## g1526（1 列）
- 見出し：RegionalTouE
- 例1 値：Nao estuda_Nao trabalho_Trabalho itiner… | Nao estuda_Nao trabalho_Trabalho itiner… | Nao estuda_Nao trabalho_Trabalho itiner… | Nao estuda_Nao trabalho_Trabalho itiner… | Nao estuda_Nao trabalho_Trabalho itiner…
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, BairroUtrabalha

## g1527（1 列）
- 見出し：BairroUtrabalha
- 例1 値：Sao Paulo | Sion | Floresta | Sao Marcos | Floresta
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, RegionalTouE

## g1528（1 列）
- 見出し：visitouComplexoCMP
- 例1 値：Nao | Sim | Sim | Sim | Sim
  - 同じ表の列：respondent_id, FaixaIdade, Escolaridade, EscolaridadeOutro, Renda familiar, RegionalMora, BairroUMora, RegionalTouE

## g1529（1 列）
- 見出し：ID_NTCV
- 例1 値：94689 | 94665 | 90291 | 86217 | 88117
  - 同じ表の列：GEOMETRIA

## g1530（1 列）
- 見出し：ID_SINALIZACAO_SEMAFORICA
- 例1 値：26 | 765 | 718 | 915 | 594
  - 同じ表の列：COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1531（1 列）
- 見出し：COD_SINALIZACAO_SEMAFORICA
- 例1 値：S4076 | S7293 | S1034 | S3027 | S2027
  - 同じ表の列：ID_SINALIZACAO_SEMA…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1532（1 列）
- 見出し：TP_TRAVESSIA_PEDESTRE
- 例1 値：Travessia sem Foco de Pedestre | Travessia Incompleta | Travessia Total | Somente Pedestre | Travessia Total
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, BOTOEIRA, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1533（1 列）
- 見出し：BOTOEIRA
- 例1 値：Não | Não | Não | Não | Não
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1534（1 列）
- 見出し：BOTOEIRA_SONORA
- 例1 値：Não | Não | Não | Não | Não
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1535（1 列）
- 見出し：LACO_DETECTOR_VEICULAR
- 例1 値：Não | Não | Não | Não | Não
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, BOTOEIRA_SONORA, QTD_TR_C_FOCO, QTD_TR_S_FOCO, GEOMETRIA

## g1536（1 列）
- 見出し：QTD_TR_C_FOCO
- 例1 値：1 | 3 | 2 | 8 | 2
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_S_FOCO, GEOMETRIA

## g1537（1 列）
- 見出し：QTD_TR_S_FOCO
- 例1 値：0 | 2 | 2 | 0 | 0
  - 同じ表の列：ID_SINALIZACAO_SEMA…, COD_SINALIZACAO_SEM…, TP_TRAVESSIA_PEDEST…, BOTOEIRA, BOTOEIRA_SONORA, LACO_DETECTOR_VEICU…, QTD_TR_C_FOCO, GEOMETRIA

## g1538（1 列）
- 見出し：ID_REDUTOR_VELOCIDADE
- 例1 値：4373 | 6824 | 4181 | 4250 | 7215
  - 同じ表の列：NUM_PROJETO_OPERACI…, BAIRRO, REFERENCIA_LOCALIZA…, DATA_IMPLANTACAO, DATA_ULTIMA_MANUTEN…, GEOMETRIA

## g1539（1 列）
- 見出し：NUM_PROJETO_OPERACIONAL
- 例1 値：17-VHF-0021899-2011 | 26-VHF-0000080-2008 | 22-VHF-067095T-2018 | 15-VHF-0036717-2011 | 18-VHF-152623T-2019
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, BAIRRO, REFERENCIA_LOCALIZA…, DATA_IMPLANTACAO, DATA_ULTIMA_MANUTEN…, GEOMETRIA

## g1540（1 列）
- 見出し：BAIRRO
- 例1 値：CACHOEIRINHA | NOVO AARÃO REIS | MARIA HELENA | RIO BRANCO | CAMPO ALEGRE
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, NUM_PROJETO_OPERACI…, REFERENCIA_LOCALIZA…, DATA_IMPLANTACAO, DATA_ULTIMA_MANUTEN…, GEOMETRIA

## g1541（1 列）
- 見出し：REFERENCIA_LOCALIZACAO
- 例1 値：ENTRE RUA WALTER DE SOUZA RIBEIRO E RUA… | ENTRE PCA DOUTOR JESUS BENIGNO E RUA IT… | ENTRE RUA SAO PEDRO DA ALDEIA E | ENTRE RUA MARECHAL BITENCOURT E RUA MAR… | ENTRE RUA SAO BERNARDO DO CAMPO E RUA T…
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, NUM_PROJETO_OPERACI…, BAIRRO, DATA_IMPLANTACAO, DATA_ULTIMA_MANUTEN…, GEOMETRIA

## g1542（1 列）
- 見出し：DATA_IMPLANTACAO
- 例1 値：2018-11-27 | 2016-02-25 | 2012-10-16 | 2009-11-12 | 2016-05-30
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, NUM_PROJETO_OPERACI…, BAIRRO, REFERENCIA_LOCALIZA…, DATA_ULTIMA_MANUTEN…, GEOMETRIA

## g1543（1 列）
- 見出し：DATA_ULTIMA_MANUTENCAO
- 例1 値：2012-01-18 | 2014-11-12 | 2014-08-11 | 2019-04-15 | 2019-06-25
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, NUM_PROJETO_OPERACI…, BAIRRO, REFERENCIA_LOCALIZA…, DATA_IMPLANTACAO, GEOMETRIA

## g1544（4 列）
- 見出し：GEOMETRIA
- 例1 値：LINESTRING (601928.08 7788157.08, 60192… | LINESTRING (605742.36 7792182.65, 60574… | LINESTRING (603376.20 7796945.58, 60337… | LINESTRING (610056.70 7798789.96, 61005… | LINESTRING (614734.66 7799987.08, 61473…
  - 同じ表の列：ID_REDUTOR_VELOCIDA…, NUM_PROJETO_OPERACI…, BAIRRO, REFERENCIA_LOCALIZA…, DATA_IMPLANTACAO, DATA_ULTIMA_MANUTEN…
- 例2 値：LINESTRING (604100.73 7795211.34, 60409… | LINESTRING (613800.80 7805345.67, 61380… | LINESTRING (616535.16 7796266.01, 61652… | LINESTRING (615847.48 7797943.20, 61584… | LINESTRING (613282.75 7795353.92, 61328…
  - 同じ表の列：ID_BASE_TRECHO, ID_RDESG, LADO_RDESG, IND_RDESG, DATA

## g1545（1 列）
- 見出し：DATA_MOVIMENTO
- 例1 値：2026-01-15 00:00:00 | 2026-01-28 00:00:00 | 2026-01-28 00:00:00 | 2026-01-12 00:00:00 | 2026-01-28 00:00:00
  - 同じ表の列：DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1546（1 列）
- 見出し：DATA_LIQUIDACAO
- 例1 値：2026-01-14 00:00:00 | 2026-01-16 00:00:00 | 2026-01-28 00:00:00 | 2026-01-28 00:00:00 | 2026-01-28 00:00:00
  - 同じ表の列：DATA_MOVIMENTO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1547（1 列）
- 見出し：NUMERO_LIQUIDACAO
- 例1 値：7 | 12 | 3 | 105 | 1
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1548（1 列）
- 見出し：DATA_PAGAMENTO
- 例1 値：2026-01-15 00:00:00 | 2026-01-15 00:00:00 | 2026-01-15 00:00:00 | 2026-01-22 00:00:00 | 2026-01-19 00:00:00
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1549（1 列）
- 見出し：NUMERO_BORDERO_PAGAMENTO
- 例1 値：Não se aplica | Não se aplica | Não se aplica | 3772 | Não se aplica
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1550（1 列）
- 見出し：GRUPO_FONTE
- 例1 値：1 - RECURSOS DO EXERCÍCIO CORRENTE | 1 - RECURSOS DO EXERCÍCIO CORRENTE | 1 - RECURSOS DO EXERCÍCIO CORRENTE | 1 - RECURSOS DO EXERCÍCIO CORRENTE | 1 - RECURSOS DO EXERCÍCIO CORRENTE
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, FONTE_DESTINACAO, DETALHAMENTO_FONTE, CO

## g1551（1 列）
- 見出し：FONTE_DESTINACAO
- 例1 値：500 - RECURSOS NÃO VINCULADOS DE IMPOST… | 500 - RECURSOS NÃO VINCULADOS DE IMPOST… | 500 - RECURSOS NÃO VINCULADOS DE IMPOST… | 500 - RECURSOS NÃO VINCULADOS DE IMPOST… | 500 - RECURSOS NÃO VINCULADOS DE IMPOST…
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, DETALHAMENTO_FONTE, CO

## g1552（1 列）
- 見出し：DETALHAMENTO_FONTE
- 例1 値：0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, CO

## g1553（1 列）
- 見出し：CO
- 例1 値：0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA | 0 - NÃO SE APLICA
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE

## g1554（2 列）
- 見出し：UNIDADE_ORCAMENTARIA
- 例1 値：0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL
  - 同じ表の列：DATA_MOVIMENTO, DATA_LIQUIDACAO, NUMERO_LIQUIDACAO, DATA_PAGAMENTO, NUMERO_BORDERO_PAGA…, GRUPO_FONTE, FONTE_DESTINACAO, DETALHAMENTO_FONTE
- 例2 値：0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL | 0101 - CÂMARA MUNICIPAL
  - 同じ表の列：DT_MOVIMENTO, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1555（1 列）
- 見出し：DT_MOVIMENTO
- 例1 値：2026-01-07 00:00:00 | 2026-01-14 00:00:00 | 2026-01-22 00:00:00 | 2026-01-26 00:00:00 | 2026-01-22 00:00:00
  - 同じ表の列：UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1556（3 列）
- 見出し：NUMERO_EMPENHO
- 例1 値：139 | 126 | 138 | 11 | 158
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO
- 例2 値：4031 | 13628 | 324 | 21853 | 21949
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1557（2 列）
- 見出し：CLASSIFICACAO_ORCAMENTARIA
- 例1 値：0101.1000.01.031.001.2.001.339040 | 0101.1000.01.031.001.2.001.339046 | 0101.1000.01.031.001.2.001.339039 | 0101.1000.01.031.001.2.001.339039 | 0101.1000.01.031.001.2.001.319011
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO
- 例2 値：4001.5703.28.846.089.3.137.339091 | 3801.1100.12.306.132.2.761.339030 | 0201.6001.04.122.096.2.004.449052 | 3701.1100.08.244.019.2.405.339048 | 0614.1100.09.122.026.2.871.339039
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1558（1 列）
- 見出し：FUNCAO
- 例1 値：09 - PREVIDÊNCIA SOCIAL | 01 - LEGISLATIVA | 09 - PREVIDÊNCIA SOCIAL | 01 - LEGISLATIVA | 01 - LEGISLATIVA
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1559（1 列）
- 見出し：SUBFUNCAO
- 例1 値：031 - AÇÃO LEGISLATIVA | 031 - AÇÃO LEGISLATIVA | 272 - PREVIDÊNCIA DO REGIME ESTATUTÁRIO | 031 - AÇÃO LEGISLATIVA | 031 - AÇÃO LEGISLATIVA
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, PROGRAMA, ACAO, SUBACAO

## g1560（1 列）
- 見出し：PROGRAMA
- 例1 値：001 - ATUAÇÃO LEGISLATIVA DA CÂMARA MUN… | 001 - ATUAÇÃO LEGISLATIVA DA CÂMARA MUN… | 001 - ATUAÇÃO LEGISLATIVA DA CÂMARA MUN… | 001 - ATUAÇÃO LEGISLATIVA DA CÂMARA MUN… | 001 - ATUAÇÃO LEGISLATIVA DA CÂMARA MUN…
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, ACAO, SUBACAO

## 答えの雛形

```
g1441	
g1442	
g1443	
g1444	
g1445	
g1446	
g1447	
g1448	
g1449	
g1450	
g1451	
g1452	
g1453	
g1454	
g1455	
g1456	
g1457	
g1458	
g1459	
g1460	
g1461	
g1462	
g1463	
g1464	
g1465	
g1466	
g1467	
g1468	
g1469	
g1470	
g1471	
g1472	
g1473	
g1474	
g1475	
g1476	
g1477	
g1478	
g1479	
g1480	
g1481	
g1482	
g1483	
g1484	
g1485	
g1486	
g1487	
g1488	
g1489	
g1490	
g1491	
g1492	
g1493	
g1494	
g1495	
g1496	
g1497	
g1498	
g1499	
g1500	
g1501	
g1502	
g1503	
g1504	
g1505	
g1506	
g1507	
g1508	
g1509	
g1510	
g1511	
g1512	
g1513	
g1514	
g1515	
g1516	
g1517	
g1518	
g1519	
g1520	
g1521	
g1522	
g1523	
g1524	
g1525	
g1526	
g1527	
g1528	
g1529	
g1530	
g1531	
g1532	
g1533	
g1534	
g1535	
g1536	
g1537	
g1538	
g1539	
g1540	
g1541	
g1542	
g1543	
g1544	
g1545	
g1546	
g1547	
g1548	
g1549	
g1550	
g1551	
g1552	
g1553	
g1554	
g1555	
g1556	
g1557	
g1558	
g1559	
g1560	
```
