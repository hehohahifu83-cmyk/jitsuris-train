# ラベル用シート 013 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_013.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1441（1 列）
- 見出し：NSW
- 例1 値：- | Yes | Yes | Yes | -
  - 同じ表の列：Community, EPBC Status, ID, ACT, NT, QLD, SA, TAS

## g1442（1 列）
- 見出し：NT
- 例1 値：- | - | - | - | -
  - 同じ表の列：Community, EPBC Status, ID, ACT, NSW, QLD, SA, TAS

## g1443（1 列）
- 見出し：QLD
- 例1 値：Yes | Yes | - | - | Yes
  - 同じ表の列：Community, EPBC Status, ID, ACT, NSW, NT, SA, TAS

## g1444（1 列）
- 見出し：SA
- 例1 値：Yes | - | - | - | -
  - 同じ表の列：Community, EPBC Status, ID, ACT, NSW, NT, QLD, TAS

## g1445（1 列）
- 見出し：TAS
- 例1 値：- | - | - | - | -
  - 同じ表の列：Community, EPBC Status, ID, ACT, NSW, NT, QLD, SA

## g1446（1 列）
- 見出し：VIC
- 例1 値：- | - | - | - | -
  - 同じ表の列：Community, EPBC Status, ID, ACT, NSW, NT, QLD, SA

## g1447（1 列）
- 見出し：School Number
- 例1 値：778 | 455 | 363 | 748 | 1053
  - 同じ表の列：Graduate Qualificat…, Postgraduate Qualif…

## g1448（1 列）
- 見出し：Graduate Qualification
- 例1 値：31 | 225 | 50 | 48 | 10
  - 同じ表の列：School Number, Postgraduate Qualif…

## g1449（1 列）
- 見出し：Postgraduate Qualifications
- 例1 値：8 | 3 | 0 | 6 | 3
  - 同じ表の列：School Number, Graduate Qualificat…

## g1450（1 列）
- 見出し：Public Transport Complaint Response Times
- 例1 値：Jan-Mar 2020 | Jan-Mar 2024 | Oct-Dec 2019 | Oct-Dec 2022 | Jul-Sep 2017
  - 同じ表の列：January 2016 - June…

## g1451（1 列）
- 見出し：January 2016 - June 2026
- 例1 値：888 | 955 | 874 | Volume of Complaints Requiring Responses | 1,078
  - 同じ表の列：Public Transport Co…

## g1452（1 列）
- 見出し：Weight
- 例1 値：1.36368477550431 | .871823431408402 | 1.05898369560252 | 1.16725227372277 | .980074811911262
  - 同じ表の列：ID, StateRegion, State, Region, Region@, S1, S3, S3@

## g1453（1 列）
- 見出し：StateRegion
- 例1 値：VIC Metro | QLD Outer Regional | QLD Outer Regional | QLD Metro | QLD Outer Regional
  - 同じ表の列：ID, Weight, State, Region, Region@, S1, S3, S3@

## g1454（1 列）
- 見出し：Region
- 例1 値：Metro | Inner Regional | Metro | Inner Regional | Outer Regional
  - 同じ表の列：ID, Weight, StateRegion, State, Region@, S1, S3, S3@

## g1455（1 列）
- 見出し：Region@
- 例1 値：Non-metro | Metro | Metro | Non-metro | Non-metro
  - 同じ表の列：ID, Weight, StateRegion, State, Region, S1, S3, S3@

## g1456（1 列）
- 見出し：S1
- 例1 値：Yes, Aboriginal | Yes, Aboriginal | Yes, Aboriginal | Yes, both | Yes, Torres Strait Islander
  - 同じ表の列：ID, Weight, StateRegion, State, Region, Region@, S3, S3@

## g1457（1 列）
- 見出し：S3
- 例1 値：45-54 | 20-24 | 15-19 | 25-34 | 45-54
  - 同じ表の列：ID, Weight, StateRegion, State, Region, Region@, S1, S3@

## g1458（1 列）
- 見出し：S3@
- 例1 値：35-54 | 35-54 | 35-54 | 55+ | 35-54
  - 同じ表の列：ID, Weight, StateRegion, State, Region, Region@, S1, S3

## g1459（1 列）
- 見出し：S3@@
- 例1 値：15-24 | 15-24 | 15-24 | 25-34 | 15-24
  - 同じ表の列：ID, Weight, StateRegion, State, Region, Region@, S1, S3

## g1460（1 列）
- 見出し：TEL_TRIPSTART
- 例1 値：01:54.7 | 29:27.8 | 55:25.0 | 22:27.0 | 43:52.4
  - 同じ表の列：TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1461（1 列）
- 見出し：TEL_STARTODO
- 例1 値：14592 | 10928 | 10752 | 26312 | 2960
  - 同じ表の列：TEL_TRIPSTART, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1462（1 列）
- 見出し：TEL_TRIPEND
- 例1 値：14:39.0 | 45:18.3 | 16:30.5 | 19:52.5 | 40:55.5
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1463（1 列）
- 見出し：TEL_ENDODO
- 例1 値：12458 | 26105 | 1208 | 16774 | 14142
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1464（1 列）
- 見出し：TEL_SOC_START
- 例1 値：99 | 39 | 103 | 79 | 83
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1465（1 列）
- 見出し：TEL_SOC_END
- 例1 値：83 | 86 | 25 | 64 | 86
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_AVG_VELOCITY, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1466（1 列）
- 見出し：TEL_AVG_VELOCITY
- 例1 値：11.35 | 41.54 | 10 | 8.57 | 26.09
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, AC_ON_DURATION, HEADLAMP_ON_DURATION

## g1467（1 列）
- 見出し：AC_ON_DURATION
- 例1 値：6.17 | 13.78 | 8.23 | 43.45 | 6.82
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, HEADLAMP_ON_DURATION

## g1468（1 列）
- 見出し：HEADLAMP_ON_DURATION
- 例1 値：1.23 | 9.67 | 5.97 | 21.55 | 11.62
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION

## g1469（1 列）
- 見出し：TRIPSTART_LOCN
- 例1 値：Other | Other | Other | Home | Other
  - 同じ表の列：TEL_TRIPSTART, TEL_STARTODO, TEL_TRIPEND, TEL_ENDODO, TEL_SOC_START, TEL_SOC_END, TEL_AVG_VELOCITY, AC_ON_DURATION

## g1470（1 列）
- 見出し：Year
- 例1 値：2014/15 | 2013/14 | 2015/16 | 2012/13 | 2016/17
  - 同じ表の列：Number of occasions…

## g1471（1 列）
- 見出し：Number of occasions on which public interest information has
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year

## g1472（1 列）
- 見出し：sa3_5digitcode_2011
- 例1 値：20501 | 11903 | 20703 | 21402 | 12701
  - 同じ表の列：number of Carer All…, Number of Carer Pay…

## g1473（1 列）
- 見出し：number of Carer Allowance recipients under 25 years of age
- 例1 値：5 | 37 | 5 | 61 | 9
  - 同じ表の列：sa3_5digitcode_2011, Number of Carer Pay…

## g1474（1 列）
- 見出し：Number of Carer Payment recipent under 25 years of age
- 例1 値：24 | 30 | 18 | 5 | 5
  - 同じ表の列：sa3_5digitcode_2011, number of Carer All…

## g1475（1 列）
- 見出し：Dataset Title
- 例1 値：Irrigation Divisions | Crime Mapper: Mid Murray (DC) Local Gov… | Housing SA Private Rental Assistance by… | Crime Mapper: Gawler (T) Local Governme… | Public Housing Dwellings 2012-13
  - 同じ表の列：Views, Visits, Resource downloads, Dataset formats

## g1476（1 列）
- 見出し：Resource downloads
- 例1 値：1 | 3 | 0 | 0 | 3
  - 同じ表の列：Dataset Title, Views, Visits, Dataset formats

## g1477（1 列）
- 見出し：Dataset formats
- 例1 値：[u'HTML', u'zip (shp)', u'KML', u'GeoJS… | [u'SHP', u'KMZ', u'GeoJSON', u'Metadata… | [u'.csv', u'DOCX', u'PDF'] | [u'KML'] | [u'XLS']
  - 同じ表の列：Dataset Title, Views, Visits, Resource downloads

## g1478（1 列）
- 見出し：Metropolitan train
- 例1 値：12833409 | 20011823 | 15480989 | 11890697 | 20806123
  - 同じ表の列：Year, Month, Metropolitan tram, Metropolitan bus, V/Line train, V/Line coach, Regional bus

## g1479（1 列）
- 見出し：Metropolitan tram
- 例1 値：16980925 | 11792860 | 17169239 | 11614262 | 14656787
  - 同じ表の列：Year, Month, Metropolitan train, Metropolitan bus, V/Line train, V/Line coach, Regional bus

## g1480（1 列）
- 見出し：Metropolitan bus
- 例1 値：4805284 | 3769166 | 11775566 | 7624940 | 12082141
  - 同じ表の列：Year, Month, Metropolitan train, Metropolitan tram, V/Line train, V/Line coach, Regional bus

## g1481（1 列）
- 見出し：V/Line train
- 例1 値：1775964 | 1466256 | 1927292 | 1469224 | 245905
  - 同じ表の列：Year, Month, Metropolitan train, Metropolitan tram, Metropolitan bus, V/Line coach, Regional bus

## g1482（1 列）
- 見出し：V/Line coach
- 例1 値：122422 | 110348 | 121267 | 95859 | 116481
  - 同じ表の列：Year, Month, Metropolitan train, Metropolitan tram, Metropolitan bus, V/Line train, Regional bus

## g1483（1 列）
- 見出し：Regional bus
- 例1 値：985731 | 1224816 | 763812 | 1098964 | 693393
  - 同じ表の列：Year, Month, Metropolitan train, Metropolitan tram, Metropolitan bus, V/Line train, V/Line coach

## g1484（1 列）
- 見出し：TRIEC 4 digit
- 例1 値：1112 Seafood fresh chilled dried smoked… | 1129 Unprocessed minerals nes | 1216 Animal & vegetables oils fats & wa… | 1129 Unprocessed minerals nes | 1149 Crude materials nes
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, Partner Country, Geographic level 1, Geographic level 2

## g1485（1 列）
- 見出し：Partner Country
- 例1 値：China | United Arab Emirates | Malaysia | Unknown | South Africa
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Geographic level 1, Geographic level 2

## g1486（1 列）
- 見出し：Geographic level 1
- 例1 値：Asia | Europe | Americas | Americas | Americas
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 2

## g1487（1 列）
- 見出し：Geographic level 2
- 例1 値：Latin America | North America | Northern & Western Europe | East Asia | Northern & Western Europe
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g1488（1 列）
- 見出し：Geographic level 3
- 例1 値：South-Eastern Europe | Western Europe | Other Middle East | Caribbean | Northern Europe
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g1489（1 列）
- 見出し：LGA
- 例1 値：Greater Dandenong (C) | Port Phillip (C) | Maribyrnong (C) | Boroondara (C) | Melbourne (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g1490（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | Eastern Metropolitan Region | Southern Metropolitan Region; North and… | North and West Metropolitan Region | Southern Metro
  - 同じ表の列：Suburb, State, Business Category, LGA

## g1491（1 列）
- 見出し：seat
- 例1 値：Park Furniture | Park Furniture | Park Furniture | Park Furniture | Park Furniture
  - 同じ表の列：ref, num_of, material, type

## g1492（1 列）
- 見出し：material
- 例1 値：Not Applicable | Timber bench seat | Timber Steel | Timber seat with back | Timber
  - 同じ表の列：ref, seat, num_of, type

## g1493（1 列）
- 見出し：type
- 例1 値：Metro Seat | Metro Seat | Other | Metro Seat | Other
  - 同じ表の列：ref, seat, num_of, material

## g1494（1 列）
- 見出し：Kindergarten
- 例1 値：South Kingsville Pre-School | Laverton Community Children's Centre | Altona Gate Kindergarten | Altona Meadows Kindergarten | Somers Parade Kindergarten
  - 同じ表の列：ID

## g1495（1 列）
- 見出し：APPL_NUMBER
- 例1 値：1992/129 | 1991/052 | 1993/060 | 1990/109 | 1990/072
  - 同じ表の列：COUNTRY_CODE

## g1496（1 列）
- 見出し：COUNTRY_CODE
- 例1 値：US | AU | AU | AU | GB
  - 同じ表の列：APPL_NUMBER

## g1497（1 列）
- 見出し：Date
- 例1 値：May-26 | Apr-26 | Mar-26 | Feb-26 | Jan-26
  - 同じ表の列：Burial, Cremation, Other, Total

## g1498（1 列）
- 見出し：Burial
- 例1 値：611 | 699 | 534 | 641 | 607
  - 同じ表の列：Date, Cremation, Other, Total

## g1499（1 列）
- 見出し：Cremation
- 例1 値：2518 | 2506 | 2196 | 2911 | 2366
  - 同じ表の列：Date, Burial, Other, Total

## g1500（1 列）
- 見出し：Other
- 例1 値：100 | 102 | 105 | 121 | 100
  - 同じ表の列：Date, Burial, Cremation, Total

## g1501（2 列）
- 見出し：Total
- 例1 値：3215 | 3731 | 3077 | 3264 | 2830
  - 同じ表の列：Date, Burial, Cremation, Other
- 例2 値：106 | 302 | 19 | 0 | 38
  - 同じ表の列：Tenure type, Very low income <$6…, Low income $603-$96…, Moderate income $96…

## g1502（1 列）
- 見出し：All Counsultancies below $10,000
- 例1 値：0 | Consultancies above $10,000 | Consultancies above $10,000 | 0 | 0
  - 同じ表の列：Purpose, Value ('000s)

## g1503（1 列）
- 見出し：Purpose
- 例1 値：0 | Purpose | Purpose | Purpose | Purpose
  - 同じ表の列：All Counsultancies …, Value ('000s)

## g1504（1 列）
- 見出し：Value ('000s)
- 例1 値：4 | Value ('000s) | Value ('000s) | 0 | Value ('000s)
  - 同じ表の列：All Counsultancies …, Purpose

## g1505（1 列）
- 見出し：class
- 例1 値：Minor Structures | Bridges and Major Culverts | Bridges and Major Culverts | Minor Structures | Minor Structures
  - 同じ表の列：assetid, subtype, mapref, lat, long

## g1506（1 列）
- 見出し：subtype
- 例1 値：Boardwalk | Culvert | Culvert | Vehicular Bridge | Culvert
  - 同じ表の列：assetid, class, mapref, lat, long

## g1507（1 列）
- 見出し：mapref
- 例1 値：34 H9 | 35 H8 | 33 E5 | 48 K5 | 49 B3
  - 同じ表の列：assetid, class, subtype, lat, long

## g1508（1 列）
- 見出し：SurveyProgram
- 例1 値：Eastern Australian Survey | Eastern Australian Survey | Eastern Australian Survey | Eastern Australian Survey | Eastern Australian Survey
  - 同じ表の列：SurvYear, Date, Band, Number, SubNumber, Combo, Fx_Group, SppCode

## g1509（1 列）
- 見出し：SurvYear
- 例1 値：1983 | 1983 | 1983 | 1983 | 1983
  - 同じ表の列：SurveyProgram, Date, Band, Number, SubNumber, Combo, Fx_Group, SppCode

## g1510（1 列）
- 見出し：Band
- 例1 値：3 | 2 | 5 | 4 | 4
  - 同じ表の列：SurveyProgram, SurvYear, Date, Number, SubNumber, Combo, Fx_Group, SppCode

## g1511（1 列）
- 見出し：SubNumber
- 例1 値：B | A | - | - | A
  - 同じ表の列：SurveyProgram, SurvYear, Date, Band, Number, Combo, Fx_Group, SppCode

## g1512（1 列）
- 見出し：Combo
- 例1 値：4-53B | 7-116- | 4-67- | 4-74D | 3-20-
  - 同じ表の列：SurveyProgram, SurvYear, Date, Band, Number, SubNumber, Fx_Group, SppCode

## g1513（1 列）
- 見出し：Fx_Group
- 例1 値：La | He | He | Du | La
  - 同じ表の列：SurveyProgram, SurvYear, Date, Band, Number, SubNumber, Combo, SppCode

## g1514（1 列）
- 見出し：SppCode
- 例1 値：WNH | BSW | FDU | MNU | WNH
  - 同じ表の列：SurveyProgram, SurvYear, Date, Band, Number, SubNumber, Combo, Fx_Group

## g1515（1 列）
- 見出し：SumOfCount
- 例1 値：121 | 10 | 260 | 491 | 9
  - 同じ表の列：SurveyProgram, SurvYear, Date, Band, Number, SubNumber, Combo, Fx_Group

## g1516（1 列）
- 見出し：School Code
- 例1 値：2725 | 2356 | 2273 | 1609 | 2730
  - 同じ表の列：Original RAM Fundin…

## g1517（1 列）
- 見出し：Original RAM Funding $
- 例1 値：$1,069,916 | $265,155 | $266,182 | $857,273 | $70,312
  - 同じ表の列：School Code

## g1518（1 列）
- 見出し：MALE
- 例1 値：46,806 | 48,451 | 55,808 | 48,310 | 48,554
  - 同じ表の列：Year, FEMALE

## g1519（1 列）
- 見出し：FEMALE
- 例1 値：46,846 | 46,255 | 42,674 | 48,104 | 43,799
  - 同じ表の列：Year, MALE

## g1520（1 列）
- 見出し：Workplace Injury Claims
- 例1 値：Total new workplace injury claims | Total gross workers compensation expend… | Significant Injuries (where lost time e… | ** before third party recovery | Return to work costs**
  - 同じ表の列：2020-2021, 2019-2020, % Change (+/-)

## g1521（1 列）
- 見出し：2020-2021
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Workplace Injury Cl…, 2019-2020, % Change (+/-)

## g1522（1 列）
- 見出し：Quarter
- 例1 値：Swan River Trust | Western Australian Electoral Commission | Hairdressers Registration Board of West… | Department of Commerce | Kimberley Development Commission
  - 同じ表の列：Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g1523（1 列）
- 見出し：Sep-08
- 例1 値：N/A | 413 | 13 | 14 | 39
  - 同じ表の列：Quarter, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g1524（1 列）
- 見出し：Dec-08
- 例1 値：9 | 156 | 3191 | 561 | 107
  - 同じ表の列：Quarter, Sep-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g1525（1 列）
- 見出し：Mar-09
- 例1 値：119 | N/A | 1274 | 145 | 31096
  - 同じ表の列：Quarter, Sep-08, Dec-08, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g1526（1 列）
- 見出し：Jun-09
- 例1 値：3681 | 1834 | 4 | 26 | 667
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Sep-09, Dec-09, Mar-10, Jun-10

## g1527（1 列）
- 見出し：Sep-09
- 例1 値：1569 | 10 | 1042 | 9 | 158
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Dec-09, Mar-10, Jun-10

## g1528（1 列）
- 見出し：Dec-09
- 例1 値：1552 | 1638 | 6 | 31 | 57
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Mar-10, Jun-10

## g1529（1 列）
- 見出し：Mar-10
- 例1 値：33 | 15 | 128 | 27 | 7
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Jun-10

## g1530（1 列）
- 見出し：Jun-10
- 例1 値：182 | 112 | 731 | 52 | 52
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g1531（1 列）
- 見出し：Sep-10
- 例1 値：111 | N/A | 2 | 72 | 2
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g1532（1 列）
- 見出し：Executive Classification
- 例1 値：EXEC0C | EXEC0B | EXEC0A | TOTAL | EXEC0D
  - 同じ表の列：Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1533（1 列）
- 見出し：Number of executives 2017-18
- 例1 値：6 | 2 | 0 | 1 | 0
  - 同じ表の列：Executive Classific…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1534（1 列）
- 見出し：Number of Executives 2018-19
- 例1 値：6 | 1 | 1 | 1 | 0
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1535（1 列）
- 見出し：Number of Executives 2019-20
- 例1 値：1 | 1 | 5 | 1 | 0
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1536（1 列）
- 見出し：Number of Executives 2020-21
- 例1 値：1 | 5 | 0 | 2 | 1
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1537（1 列）
- 見出し：Number of Executives 2021-22
- 例1 値：1 | 5 | 0 | 1 | 3
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1538（1 列）
- 見出し：Number of Executives 2022-23
- 例1 値：1 | 2 | 1 | 0 | 5
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1539（1 列）
- 見出し：Number of Executives 2023-24
- 例1 値：1 | 0 | 0 | 1 | 3
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1540（1 列）
- 見出し：Number of Executives 2024-25
- 例1 値：1 | 1 | 3 | 0 | 0
  - 同じ表の列：Executive Classific…, Number of executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…, Number of Executive…

## g1541（1 列）
- 見出し：Item_number
- 例1 値：1081X | 1109J | 1088G | 1037N | 1104D
  - 同じ表の列：Year, State, Scheme, Month, Services, Benefits ($)

## g1542（2 列）
- 見出し：Scheme
- 例1 値：PBS | PBS | PBS | PBS | PBS
  - 同じ表の列：Year, Item_number, State, Month, Services, Benefits ($)
- 例2 値：CAR | HHB | OFP | DPMA | INVP
  - 同じ表の列：period, programme, basis, county, county_code, recipients

## g1543（1 列）
- 見出し：Services
- 例1 値：2 | 48 | 11 | 871 | 2
  - 同じ表の列：Year, Item_number, State, Scheme, Month, Benefits ($)

## g1544（1 列）
- 見出し：Benefits ($)
- 例1 値：48 | 375 | 5356 | 74 | 385
  - 同じ表の列：Year, Item_number, State, Scheme, Month, Services

## g1545（1 列）
- 見出し：Business Category
- 例1 値：Life Saving Club | Life Saving Club | Life Saving Club | Life Saving Club | Life Saving Club
  - 同じ表の列：Suburb, State, LGA, Region

## g1546（1 列）
- 見出し：LGA
- 例1 値：Surf Coast (S) | Greater Geelong (C) | Bayside (C) | Port Phillip (C); Melbourne (C) | Bass Coast (S)
  - 同じ表の列：Suburb, State, Business Category, Region

## g1547（1 列）
- 見出し：Region
- 例1 値：Gippsland Region | Gippsland Region | Southern Metropolitan Region | Barwon South Western Region | Southern Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g1548（1 列）
- 見出し：Tenure type
- 例1 値：Rented: Other landlord | Being purchased (incl rent/buy) | Rented: Private and not stated | Rented: TOTAL | Rented: Other landlord
  - 同じ表の列：Very low income <$6…, Low income $603-$96…, Moderate income $96…, Total

## g1549（1 列）
- 見出し：Very low income <$603 per wk
- 例1 値：198 | 65 | 10 | 7 | 246
  - 同じ表の列：Tenure type, Low income $603-$96…, Moderate income $96…, Total

## g1550（1 列）
- 見出し：Low income $603-$964 per wk
- 例1 値：227 | 0 | 0 | 5 | 0
  - 同じ表の列：Tenure type, Very low income <$6…, Moderate income $96…, Total

## g1551（1 列）
- 見出し：Moderate income $965-$1446 per wk
- 例1 値：0 | 5 | 11 | 0 | 3
  - 同じ表の列：Tenure type, Very low income <$6…, Low income $603-$96…, Total

## g1552（1 列）
- 見出し：Consultants - Consultancies with a contract value below $10,
- 例1 値：Zen Yap (Developing health surveillance… | Safe Select (Psychological testing and … | GHD Pty Ltd (PFAS testing) | Chandler Macleod (Bushfire Review) | University of Adelaide (Investigate occ…
  - 同じ表の列：2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1553（1 列）
- 見出し：2014-15
- 例1 値：2014-15 | $18 896 | $42 096 | $23 200
  - 同じ表の列：Consultants - Consu…, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1554（1 列）
- 見出し：2015-16
- 例1 値：$18 279 | $24 888 | $43 167 | 2015-16
  - 同じ表の列：Consultants - Consu…, 2014-15, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1555（1 列）
- 見出し：2016-17
- 例1 値：$12 700 | $60 621 | $0 | $47 921 | 2016-17
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g1556（1 列）
- 見出し：2017-18
- 例1 値：$26 664 | $17 579 | $9 085 | 2017-18
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2016-17, 2018-19, 2019-20, 2020-21, 2021-22

## g1557（1 列）
- 見出し：2018-19
- 例1 値：$309 545 | $9 790 | $730 256 | 2018-19 | $420 711
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22

## g1558（1 列）
- 見出し：2019-20
- 例1 値：$57 550 | $753 626 | $43 192 | $18 154 | $11 350
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2020-21, 2021-22

## g1559（1 列）
- 見出し：2020-21
- 例1 値：2020-21 | $131 243 | $195 206 | $18 508 | $63 963
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2021-22

## g1560（1 列）
- 見出し：2021-22
- 例1 値：$18 000 | $136 750 | $223 648 | $21 068 | $34 161
  - 同じ表の列：Consultants - Consu…, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21

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
