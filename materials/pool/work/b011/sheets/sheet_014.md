# ラベル用シート 014 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_014.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1561（1 列）
- 見出し：zoneid
- 例1 値：32 | 27 | 20 | 29 | 7
  - 同じ表の列：common, genus, species, regulation

## g1562（1 列）
- 見出し：common
- 例1 値：chilean needle grass | chillean needle-grass | chillean needle-grass | chillean needle-grass | chillean needle-grass
  - 同じ表の列：zoneid, genus, species, regulation

## g1563（1 列）
- 見出し：regulation
- 例1 値：high risk weed zone – equipment clean-d… | high risk weed zone – equipment clean-d… | high risk weed zone – equipment clean-d… | high risk weed zone – equipment clean-d… | high risk weed zone – equipment clean-d…
  - 同じ表の列：zoneid, common, genus, species

## g1564（1 列）
- 見出し：X Values
- 例1 値：Oxides of Nitrogen | Sulfur Dioxide | Total VOCs | Particulate Matter <10オm | Carbon Monoxide
  - 同じ表の列：Commercial, Domestic-Commercial, Industrial

## g1565（1 列）
- 見出し：Commercial
- 例1 値：0.042042949 | 0.001523635 | 0.02931011 | 0.007780006 | 0.044263203
  - 同じ表の列：X Values, Domestic-Commercial, Industrial

## g1566（1 列）
- 見出し：Domestic-Commercial
- 例1 値：0.429398517 | 0.012220917 | 0.594671052 | 0.046029638 | 0.55477853
  - 同じ表の列：X Values, Commercial, Industrial

## g1567（1 列）
- 見出し：Industrial
- 例1 値：0.097066839 | 0.125895971 | 0.028379234 | 0.183396879 | 0.301292858
  - 同じ表の列：X Values, Commercial, Domestic-Commercial

## g1568（1 列）
- 見出し：Year ended
- 例1 値：2013 | 2024 | 2021 | 2022 | 2018
  - 同じ表の列：Category, Number of executives

## g1569（1 列）
- 見出し：Number of executives
- 例1 値：3 | 3 | 3 | 2 | 2
  - 同じ表の列：Year ended, Category

## g1570（1 列）
- 見出し：Formal extension reasons, by sector
- 例1 値：UNIVERSITIES - Extension under s14(1)(b… | UNIVERSITIES - Extension under s14(1)(a… | STATE - Extension under s14(1)(b) - con… | LOCAL - Extension under s14(1)(b) - con… | STATE - Extension under s14(1)(a) - sea…
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g1571（1 列）
- 見出し：2024-25
- 例1 値：15 | 31 | 0 | 195 | 43
  - 同じ表の列：Formal extension re…, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g1572（1 列）
- 見出し：2023-24
- 例1 値：395 | 43 | 12 | 185 | 30
  - 同じ表の列：Formal extension re…, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g1573（1 列）
- 見出し：2022-23
- 例1 値：3 | 2 | 36 | 28 | 117
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g1574（1 列）
- 見出し：2021-22
- 例1 値：14 | 13 | 1 | 77 | 601
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g1575（1 列）
- 見出し：2020-21
- 例1 値：180 | 22 | 690 | 4 | 18
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g1576（1 列）
- 見出し：2019-20
- 例1 値：5 | 306 | 10 | 14 | 380
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g1577（1 列）
- 見出し：2018-19
- 例1 値：19 | 4 | 9 | 282 | 6
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g1578（1 列）
- 見出し：2017-18
- 例1 値：332 | 2 | 134 | 3 | 9
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g1579（1 列）
- 見出し：2016-17
- 例1 値：283 | 155 | 10 | 8 | 2
  - 同じ表の列：Formal extension re…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g1580（1 列）
- 見出し：Threshold amount ($)
- 例1 値：1,029,000.00 | 1,052,000.00 | 1,093,000.00 | 1,133,000.00 | 1,076,000.00
  - 同じ表の列：Financial year

## g1581（1 列）
- 見出し：Contractors
- 例1 値：No. of Contractors below $10,000 each | Value of Contractors above $10,000 each | Value of Contractors below $10,000 each | Contractors | No. of Contractors above $10,000 each
  - 同じ表の列：_id, 2015-16*, 2016-17*, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1582（1 列）
- 見出し：2015-16*
- 例1 値：0 | 2015-16* | 0 | 0 | 0
  - 同じ表の列：_id, Contractors, 2016-17*, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1583（1 列）
- 見出し：2016-17*
- 例1 値：2016-17* | 0 | 0 | 0 | 0
  - 同じ表の列：_id, Contractors, 2015-16*, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1584（1 列）
- 見出し：2017-18
- 例1 値：51 | 152,553 | 8 | 199,654 | 2017-18
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2018-19, 2019-20, 2020-21, 2021-22

## g1585（1 列）
- 見出し：2018-19
- 例1 値：42 | 642,861 | 2018-19 | 12 | 86,111
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2017-18, 2019-20, 2020-21, 2021-22

## g1586（1 列）
- 見出し：2019-20
- 例1 値：54 | 2019-20 | 384,360 | 91,777 | 11
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2017-18, 2018-19, 2020-21, 2021-22

## g1587（1 列）
- 見出し：2020-21
- 例1 値：12 | 2020-21 | 80 | 422,538 | 93,819
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2017-18, 2018-19, 2019-20, 2021-22

## g1588（1 列）
- 見出し：2021-22
- 例1 値：183,952 | 80 | 8 | 120,234 | 2021-22
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2017-18, 2018-19, 2019-20, 2020-21

## g1589（1 列）
- 見出し：2022-23
- 例1 値：9 | 2022-23 | 151,466 | 81 | 154,175
  - 同じ表の列：_id, Contractors, 2015-16*, 2016-17*, 2017-18, 2018-19, 2019-20, 2020-21

## g1590（1 列）
- 見出し：caption
- 例1 値：150th Anniversary celebrations: process… | 10,000 metres cross country at Parramat… | 1st Light Horse Machine Gun Regiment in… | 2UW Deanna Durbin competition at Bon Ma… | 2CH Old Time Dance at Trocadero
  - 同じ表の列：itemid, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g1591（1 列）
- 見出し：collectiontitle
- 例1 値：Hood Collection part I : Sydney streets… | Hood Collection part I : Sydney streets… | Hood Collection part I : Sydney streets… | Hood Collection part I : Sydney streets… | Hood Collection part I : Sydney streets…
  - 同じ表の列：itemid, caption, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g1592（1 列）
- 見出し：dateofwork
- 例1 値：20/9/1938 | 6/10/1937 | 15/8/1944 | 9/1937 | October 1940
  - 同じ表の列：itemid, caption, collectiontitle, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g1593（1 列）
- 見出し：digitalordernumber
- 例1 値：hood_21851 | hood_16724 | hood_15103 | hood_21481 | hood_21439
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, collectionitemlink, digitalitemlink, thumbnaillink, highreslink

## g1594（1 列）
- 見出し：topicstring
- 例1 値：<a href="http://acms.sl.nsw.gov.au/sear… | <a href="http://acms.sl.nsw.gov.au/sear… | <a href="http://acms.sl.nsw.gov.au/sear… | <a href="http://acms.sl.nsw.gov.au/sear… | <a href="http://acms.sl.nsw.gov.au/sear…
  - 同じ表の列：itemid, caption, collectiontitle, dateofwork, digitalordernumber, collectionitemlink, digitalitemlink, thumbnaillink

## g1595（1 列）
- 見出し：Captionformaponrecord
- 例1 値：45/10/C1 (1900) Historic map series C, … | 45/9/L137 1893 Historic map series L We… | 45_14_M19_1893_Historic_map_series_M_We… | 45 11 C48 Historic map series C Western… | 45_16_S45_1896_Historic_map_series_S_We…
  - 同じ表の列：BibliographicRecord…, URLformap

## g1596（1 列）
- 見出し：URLformap
- 例1 値：http://purl.slwa.wa.gov.au/slwa_b277537… | http://purl.slwa.wa.gov.au/slwa_map_b27… | http://purl.slwa.wa.gov.au/slwa_b277564… | http://purl.slwa.wa.gov.au/slwa_b277537… | http://purl.slwa.wa.gov.au/slwa_b277564…
  - 同じ表の列：BibliographicRecord…, Captionformaponreco…

## g1597（1 列）
- 見出し：Project Area
- 例1 値：Ridgeview-S13 | Figtree Hill-S1F | Figtree Hill-S2A | Aarya Estate-S3 | Melbourne Square T1 & T6-T1
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed, Comments, Estate Complete

## g1598（1 列）
- 見出し：Service_Area_Identifier
- 例1 値：WTPL | MTGD | STPW | STNB | OSKS
  - 同じ表の列：Project Area, Latlong, ID, Anticipatory Notice…, Date Completed, Comments, Estate Complete

## g1599（1 列）
- 見出し：Latlong
- 例1 値：-27.186721, 152.924614 | -37.7054436,144.7020288 | -32.1285399,115.9078465 | -33.7616987,150.7558402 | -37.8256453,144.9642661
  - 同じ表の列：Project Area, Service_Area_Identi…, ID, Anticipatory Notice…, Date Completed, Comments, Estate Complete

## g1600（1 列）
- 見出し：Anticipatory Notice Reference Date
- 例1 値：2025-04-16 00:00:00 | 2024-11-25 00:00:00 | 2025-05-07 00:00:00 | 2025-01-22 00:00:00 | 2025-11-05 00:00:00
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Date Completed, Comments, Estate Complete

## g1601（1 列）
- 見出し：Date Completed
- 例1 値：2026-09-24 00:00:00 | 2026-09-28 00:00:00 | 2026-10-02 00:00:00 | 2026-10-01 00:00:00 | 2026-09-29 00:00:00
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Comments, Estate Complete

## g1602（1 列）
- 見出し：Comments
- 例1 値：Project area incorrectly declared on 31… | Project area incorrectly declared on 18… | Project area incorrectly declared on 18… | Project area incorrectly declared on 31… | Original estate Ridgeview (STNB) is a d…
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g1603（1 列）
- 見出し：Estate Complete
- 例1 値：N | Y | N | N | N
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed, Comments

## g1604（1 列）
- 見出し：BudgetYear
- 例1 値：2025-2026 | 2025-2026 | 2025-2026 | 2025-2026 | 2025-2026
  - 同じ表の列：AssetID, SiteCode, Locality, ExtID, Desc, Comments

## g1605（1 列）
- 見出し：AssetID
- 例1 値：R08060/030/FO | R01740/085/RS | R09550/035/RS | R09090/015/FO | R04880/020/RS
  - 同じ表の列：BudgetYear, SiteCode, Locality, ExtID, Desc, Comments

## g1606（1 列）
- 見出し：SiteCode
- 例1 値：37R04880 | 11R09190 | 11R01120 | 5R00420 | 31R10160
  - 同じ表の列：BudgetYear, AssetID, Locality, ExtID, Desc, Comments

## g1607（1 列）
- 見出し：Locality
- 例1 値：Gooram | Nagambie | Wahring | Nagambie | Violet Town
  - 同じ表の列：BudgetYear, AssetID, SiteCode, ExtID, Desc, Comments

## g1608（1 列）
- 見出し：ExtID
- 例1 値：1556 | 1117 | 123 | 10167 | 1525
  - 同じ表の列：BudgetYear, AssetID, SiteCode, Locality, Desc, Comments

## g1609（1 列）
- 見出し：Desc
- 例1 値：Reseal Road | Reseal Road | Reseal Road | Reseal Road | Major Projects: Rehabilitation
  - 同じ表の列：BudgetYear, AssetID, SiteCode, Locality, ExtID, Comments

## g1610（1 列）
- 見出し：Comments
- 例1 値：Please note: This map does not show all… | Please note: This map does not show all… | Please note: This map does not show all… | Please note: This map does not show all… | Please note: This map does not show all…
  - 同じ表の列：BudgetYear, AssetID, SiteCode, Locality, ExtID, Desc

## g1611（1 列）
- 見出し：Breed
- 例1 値：KELPIE | FOX TERRIER | LABRADOR CROSS | BORDER COLLIE | BURMESE
  - 同じ表の列：Suburb, Colour, Registered

## g1612（1 列）
- 見出し：Colour
- 例1 値：BLUE MERLE | BROWN | TAN & WHITE | BRINDLE | BLACK & WHITE
  - 同じ表の列：Suburb, Breed, Registered

## g1613（1 列）
- 見出し：Registered
- 例1 値：N | Y | Y | Y | Y
  - 同じ表の列：Suburb, Breed, Colour

## g1614（1 列）
- 見出し：RFx No
- 例1 値：TCW00595 | TCW00474 | TOW00273 | TCW00459 | TOWNSV-935039
  - 同じ表の列：Tender Type, Notice Type, Status, Release Date, Closed Date/Time

## g1615（1 列）
- 見出し：Tender Type
- 例1 値：Public | Public | Tender | Public | Pre-Identified
  - 同じ表の列：RFx No, Notice Type, Status, Release Date, Closed Date/Time

## g1616（1 列）
- 見出し：Notice Type
- 例1 値：Request for Quotation | Request for Tender | Request for Tender | Request for Tender | Request for Tender
  - 同じ表の列：RFx No, Tender Type, Status, Release Date, Closed Date/Time

## g1617（1 列）
- 見出し：Release Date
- 例1 値：2020-11-03 00:00:00 | 2023-07-08 00:01:00 | 2021-10-23 00:01:00 | 2021-12-11 00:01:00 | 2022-10-29 00:01:00
  - 同じ表の列：RFx No, Tender Type, Notice Type, Status, Closed Date/Time

## g1618（1 列）
- 見出し：Closed Date/Time
- 例1 値：2022-09-07 10:00:00 | 2023-05-31 16:00:00 | 2024-05-24 10:00:00 | 09/10/2020 - 4:00 p.m. | 2026-08-04 10:00:00
  - 同じ表の列：RFx No, Tender Type, Notice Type, Status, Release Date

## g1619（1 列）
- 見出し：Door Counter
- 例1 値：267677 | 144350 | 276066 | 229104 | 117934
  - 同じ表の列：_id, Library

## g1620（1 列）
- 見出し：MUGA
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OBJECTID, Website, Type

## g1621（1 列）
- 見出し：Statistic
- 例1 値：Persons in Receipt of Full-time Educati… | Persons in Receipt of Full-time Educati… | Persons in Receipt of Full-time Educati… | Persons in Receipt of Full-time Educati… | Persons in Receipt of Full-time Educati…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02076V02508, Age, C02199V02655, Sex, C02351V02955

## g1622（1 列）
- 見出し：C02076V02508
- 例1 値：14 | 14 | 10 | 5 | 10
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Age, C02199V02655, Sex, C02351V02955

## g1623（1 列）
- 見出し：Age
- 例1 値：13 years | 9 years | 15 years | 6 years | 14 years
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, C02199V02655, Sex, C02351V02955

## g1624（1 列）
- 見出し：C02199V02655
- 例1 値：1 | - | - | 2 | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age, Sex, C02351V02955

## g1625（1 列）
- 見出し：Type of Institution
- 例1 値：All education institutions | Second level education institutions aid… | Second level education institutions aid… | All first level education institutions | All second level education institutions
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age, C02199V02655, Sex

## g1626（1 列）
- 見出し：Statistic Label
- 例1 値：Hospital beds by function and type | Hospital beds by function and type | Hospital beds by function and type | Hospital beds by function and type | Hospital beds by function and type
  - 同じ表の列：STATISTIC, YEAR, Year, FUNCTION, Type of function, BEDTYPE, Bed type, UNIT

## g1627（1 列）
- 見出し：Type of function
- 例1 値：All types of bed functions | Beds for other care function | Beds for rehabilitative care function | Beds for rehabilitative care function | Beds for other care function
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FUNCTION, BEDTYPE, Bed type, UNIT

## g1628（1 列）
- 見出し：BEDTYPE
- 例1 値：SOM | TOT | TOT | PSYCH | PSYCH
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FUNCTION, Type of function, Bed type, UNIT

## g1629（1 列）
- 見出し：Bed type
- 例1 値：Psychiatric care type beds | Psychiatric care type beds | Somatic care type beds | Psychiatric care type beds | All types of beds
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FUNCTION, Type of function, BEDTYPE, UNIT

## g1630（1 列）
- 見出し：Statistic
- 例1 値：Number of House Loans Paid | Number of House Loans Approved | Value of House Loans Approved | Value of House Loans Paid | Number of House Loans Approved
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02350V02827, House Type New or S…, UNIT, VALUE

## g1631（1 列）
- 見出し：C02350V02827
- 例1 値：1 | 1 | 1 | 2 | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, House Type New or S…, UNIT, VALUE

## g1632（1 列）
- 見出し：House Type New or Second hand
- 例1 値：New houses | New houses | Second-hand houses | Second-hand houses | New houses
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02350V02827, UNIT, VALUE

## g1633（1 列）
- 見出し：UNIT
- 例1 値：Number | Euro Million | Number | Euro Million | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02350V02827, House Type New or S…, VALUE

## g1634（1 列）
- 見出し：Type
- 例1 値：long term visa applications | long term visa applications | long term visa applications | long term visa applications | long term visa applications
  - 同じ表の列：Status, year, Jan, Feb, Mar, Apr, May, Jun

## g1635（2 列）
- 見出し：Jan
- 例1 値：1103 | 6973 | 7079 | 1406 | 602
  - 同じ表の列：Type, Status, year, Feb, Mar, Apr, May, Jun
- 例2 値：15 | 8 | 33 | 18 | 26
  - 同じ表の列：AreaID, RegionID, Area, Year, Feb, Mar, Apr, May

## g1636（2 列）
- 見出し：Feb
- 例1 値：1723 | 1725 | 8528 | 3185 | 5114
  - 同じ表の列：Type, Status, year, Jan, Mar, Apr, May, Jun
- 例2 値：33 | 29 | 29 | 19 | 1
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Mar, Apr, May

## g1637（2 列）
- 見出し：Mar
- 例1 値：123 | 7491 | 2386 | 7398 | 800
  - 同じ表の列：Type, Status, year, Jan, Feb, Apr, May, Jun
- 例2 値：4 | 16 | 10 | 28 | 25
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Apr, May

## g1638（2 列）
- 見出し：Apr
- 例1 値：895 | 1060 | 7474 | 15949 | 528
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, May, Jun
- 例2 値：41 | 32 | 7 | 9 | 15
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, May

## g1639（2 列）
- 見出し：May
- 例1 値：219 | 18 | 139 | 1622 | 2089
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, Jun
- 例2 値：29 | 32 | 34 | 25 | 15
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, Apr

## g1640（2 列）
- 見出し：Jun
- 例1 値：630 | 11206 | 6934 | 174 | 2369
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May
- 例2 値：32 | 9 | 17 | 36 | 26
  - 同じ表の列：AreaID, RegionID, Area, Year, Jan, Feb, Mar, Apr

## g1641（1 列）
- 見出し：Jul
- 例1 値：12426 | 2944 | 1164 | 1259 | 322
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May

## g1642（1 列）
- 見出し：programme
- 例1 値：Illness,Disability and Caring | Supplementary Payments and Miscellaneou… | Children | Working Age Income Supports | Illness,Disability and Caring
  - 同じ表の列：period, scheme, basis, county, county_code, recipients

## g1643（1 列）
- 見出し：county_code
- 例1 値：LS | LD | KY | WH | LD
  - 同じ表の列：period, programme, scheme, basis, county, recipients

## g1644（1 列）
- 見出し：unit_no
- 例1 値：12.0 | 6.0 | 2.0 | 13.0 | 16.0
  - 同じ表の列：ID, unit_type

## g1645（1 列）
- 見出し：unit_type
- 例1 値：PL: Column | PL: ESB Pole | PL: Column | PL: Column | PL: LUAS Pole/Line
  - 同じ表の列：ID, unit_no

## g1646（1 列）
- 見出し：TLIST(Q1)
- 例1 値：2010Q1 | 2006Q2 | 2008Q1 | 2006Q4 | 2005Q1
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g1647（1 列）
- 見出し：C02635V03192
- 例1 値：- | - | - | 05 | 04
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g1648（1 列）
- 見出し：Shipping Corridor
- 例1 値：Continental | Southern | Continental | Continental | Southern
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, C02638V03194, Type of Traffic, UNIT

## g1649（1 列）
- 見出し：Type of Traffic
- 例1 値：Tourist passengers | Tourist cars | Tourist cars | Tourist passengers | Tourist passengers
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, C02638V03194, UNIT

## g1650（1 列）
- 見出し：Belmullet 1981-2010 averages
- 例1 値：greatest daily duration | greatest daily total | thunder | WEATHER (mean no. of days with..) | mean daily duration
  - 同じ表の列：unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7, unsafe__8

## g1651（1 列）
- 見出し：unsafe_
- 例1 値：10.7 | 23 | 0.4 | 5.8 | 13.9
  - 同じ表の列：Belmullet 1981-2010…, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7, unsafe__8

## g1652（1 列）
- 見出し：unsafe__2
- 例1 値：15.1 | 9.1 | 0.2 | 20 | 6
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7, unsafe__8

## g1653（1 列）
- 見出し：unsafe__3
- 例1 値：5.9 | 3.1 | 3.1 | 19.5 | 0.6
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__4, unsafe__5, unsafe__6, unsafe__7, unsafe__8

## g1654（1 列）
- 見出し：unsafe__4
- 例1 値：43 | 1.4 | 2.7 | 13 | 1.4
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__5, unsafe__6, unsafe__7, unsafe__8

## g1655（1 列）
- 見出し：unsafe__5
- 例1 値：0 | 66 | 13 | 14.6 | 70.4
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__6, unsafe__7, unsafe__8

## g1656（1 列）
- 見出し：unsafe__6
- 例1 値：0.2 | 13.3 | 10.4 | 14.9 | 1.7
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__7, unsafe__8

## g1657（1 列）
- 見出し：unsafe__7
- 例1 値：16.8 | 12.2 | 0 | 0 | Jul
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__8

## g1658（1 列）
- 見出し：unsafe__8
- 例1 値：79.2 | 27.7 | 0 | 40 | 16.1
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g1659（1 列）
- 見出し：unsafe__9
- 例1 値：3.7 | 12.1 | 10.7 | 0 | 77.9
  - 同じ表の列：Belmullet 1981-2010…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g1660（1 列）
- 見出し：age__end_of_academic_year_
- 例1 値：20 | 8 | Unkown | 11 | 14
  - 同じ表の列：No of Pupils

## g1661（1 列）
- 見出し：No of Pupils
- 例1 値：488 | 989 | 1120 | 989 | 675
  - 同じ表の列：age__end_of_academi…

## g1662（1 列）
- 見出し：OID_
- 例1 値：585 | 495 | 705 | 10 | 371
  - 同じ表の列：cdo, twoway, bollardpro

## g1663（1 列）
- 見出し：accounting_year
- 例1 値：2023 | 2025 | 2025 | 2024 | 2023
  - 同じ表の列：accounting_quarter, accounting_period, product_level_1, product_level_2, unit, rate, volume home, volume import

## g1664（1 列）
- 見出し：accounting_quarter
- 例1 値：2 | 1 | 4 | 1 | 2
  - 同じ表の列：accounting_year, accounting_period, product_level_1, product_level_2, unit, rate, volume home, volume import

## g1665（1 列）
- 見出し：accounting_period
- 例1 値：202410 | 202308 | 202412 | 202302 | 202301
  - 同じ表の列：accounting_year, accounting_quarter, product_level_1, product_level_2, unit, rate, volume home, volume import

## g1666（1 列）
- 見出し：product_level_1
- 例1 値：Cider & Perry | Spirits | Spirits | Spirits | Wine
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_2, unit, rate, volume home, volume import

## g1667（1 列）
- 見出し：product_level_2
- 例1 値：Still & sparkling, exceeding 2.8% vol b… | Sparkling, exceeding 5.5% vol | Sparkling, exceeding 5.5% vol | Spirits not exceeding 5.5% vol | Beer exceeding 2.8% vol
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, unit, rate, volume home, volume import

## g1668（1 列）
- 見出し：unit
- 例1 値：litre of alcohol | Hectolitre of Product | Hectolitre of Product | litre of alcohol | Hectolitre of Product
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, product_level_2, rate, volume home, volume import

## g1669（1 列）
- 見出し：rate
- 例1 値：616.45 | 424.84 | 42.57 | 218.44 | 42.57
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, product_level_2, unit, volume home, volume import

## g1670（1 列）
- 見出し：volume home
- 例1 値：32.42 | 0.9 | 1922.38 | 48652.96 | 1243.84
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, product_level_2, unit, rate, volume import

## g1671（1 列）
- 見出し：volume import
- 例1 値：155477.05 | 6.32 | 4580.48 | 33.27 | 63499.08
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, product_level_2, unit, rate, volume home

## g1672（1 列）
- 見出し：liability_home__
- 例1 値：67.97 | 75.09 | 3349233.2 | 1205376.61 | 4218.74
  - 同じ表の列：accounting_year, accounting_quarter, accounting_period, product_level_1, product_level_2, unit, rate, volume home

## g1673（1 列）
- 見出し：desc
- 例1 値：Recreation & Amenity | Library Council | Defence | DTO | Other Grants & Subsidies
  - 同じ表の列：Doc, Heading, Ref, Inc, PY, OBJECTID

## g1674（1 列）
- 見出し：Inc
- 例1 値：-720000 | -373000 | -2194700 | -206500 | -12621300
  - 同じ表の列：Doc, Heading, Ref, desc, PY, OBJECTID

## g1675（1 列）
- 見出し：PY
- 例1 値：-12220700 | -40000 | -625000 | -25000 | -95400
  - 同じ表の列：Doc, Heading, Ref, desc, Inc, OBJECTID

## g1676（1 列）
- 見出し：air_temperature__degrees_c_
- 例1 値：16.8 | 9.7 | 14.3 | 11.3 | 13.5
  - 同じ表の列：SensorTimestamp, barometric_pressure…, wind_direction__deg…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…, barometric_pressure…

## g1677（1 列）
- 見出し：barometric_pressure__inches_
- 例1 値：29.9936 | 29.9611 | 29.905 | 29.8578 | 29.8666
  - 同じ表の列：SensorTimestamp, air_temperature__de…, wind_direction__deg…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…, barometric_pressure…

## g1678（1 列）
- 見出し：wind_direction__degrees_magnetic_
- 例1 値：226.3 | 147.1 | 146.7 | 148.2 | 279.7
  - 同じ表の列：SensorTimestamp, air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…, barometric_pressure…

## g1679（1 列）
- 見出し：wind_direction__degrees_true_
- 例1 値：234.0 | 188.5 | 260.4 | 258.2 | 188.5
  - 同じ表の列：SensorTimestamp, air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_speed__knot_, wind_speed__meters_…, barometric_pressure…

## g1680（1 列）
- 見出し：wind_speed__knot_
- 例1 値：3.6 | 11.8 | 18.9 | 18.4 | 5.5
  - 同じ表の列：SensorTimestamp, air_temperature__de…, barometric_pressure…, wind_direction__deg…, wind_direction__deg…, wind_speed__meters_…, barometric_pressure…

## 答えの雛形

```
g1561	
g1562	
g1563	
g1564	
g1565	
g1566	
g1567	
g1568	
g1569	
g1570	
g1571	
g1572	
g1573	
g1574	
g1575	
g1576	
g1577	
g1578	
g1579	
g1580	
g1581	
g1582	
g1583	
g1584	
g1585	
g1586	
g1587	
g1588	
g1589	
g1590	
g1591	
g1592	
g1593	
g1594	
g1595	
g1596	
g1597	
g1598	
g1599	
g1600	
g1601	
g1602	
g1603	
g1604	
g1605	
g1606	
g1607	
g1608	
g1609	
g1610	
g1611	
g1612	
g1613	
g1614	
g1615	
g1616	
g1617	
g1618	
g1619	
g1620	
g1621	
g1622	
g1623	
g1624	
g1625	
g1626	
g1627	
g1628	
g1629	
g1630	
g1631	
g1632	
g1633	
g1634	
g1635	
g1636	
g1637	
g1638	
g1639	
g1640	
g1641	
g1642	
g1643	
g1644	
g1645	
g1646	
g1647	
g1648	
g1649	
g1650	
g1651	
g1652	
g1653	
g1654	
g1655	
g1656	
g1657	
g1658	
g1659	
g1660	
g1661	
g1662	
g1663	
g1664	
g1665	
g1666	
g1667	
g1668	
g1669	
g1670	
g1671	
g1672	
g1673	
g1674	
g1675	
g1676	
g1677	
g1678	
g1679	
g1680	
```
