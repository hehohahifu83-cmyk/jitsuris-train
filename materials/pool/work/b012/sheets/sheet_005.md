# ラベル用シート 005 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：Title
- 例1 値：Bundaberg Housing Service Centre | Hope Vale Tenancy Services, First Natio… | Ravenshoe Queensland Government Agent P… | Emerald Housing Service Centre | Palm Island Housing
  - 同じ表の列：Suburb, Fax, Opening hours

## g0482（1 列）
- 見出し：Fax
- 例1 値：- 07 3245 1717 | - 07 4090 3782 | - 07 4036 5578 | - 07 4324 8626 | - 07 3873 7765
  - 同じ表の列：Title, Suburb, Opening hours

## g0483（1 列）
- 見出し：Opening hours
- 例1 値：- Please contact 07 4036 5555 to make a… | - Please contact 07 4036 5555 to make a… | - Please contact 07 4036 5555 to make a… | - Monday: 8:30am–4:30pm - Tuesday: 8:30… | - Monday: 8:30am–4:30pm - Tuesday: 8:30…
  - 同じ表の列：Title, Suburb, Fax

## g0484（1 列）
- 見出し：CATEGORY
- 例1 値：Car Parking | Car Parking | Sporting (Tennis Court) | Walking | Sporting (Soccer)
  - 同じ表の列：POLENO, HEIGHT, POLE, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1, LAMP_1

## g0485（1 列）
- 見出し：POLENO
- 例1 値：7063243 | 7062935 | 7201 | 7071438 | 9829277
  - 同じ表の列：CATEGORY, HEIGHT, POLE, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1, LAMP_1

## g0486（1 列）
- 見出し：HEIGHT
- 例1 値：5 | 10 | 5 | 6.5 | 0.5
  - 同じ表の列：CATEGORY, POLENO, POLE, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1, LAMP_1

## g0487（1 列）
- 見出し：POLE
- 例1 値：Concrete Pole | Wall Mounted | Concrete Pole | Timber Pole | Steel Pole
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1, LAMP_1

## g0488（1 列）
- 見出し：BRACKET
- 例1 値：Pole Bracket | Pole Mounted | Pole Bracket | Pole Mounted | Pole Bracket
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKETSZ, BRACKETNO, LUMINAIRE1, LAMP_1

## g0489（1 列）
- 見出し：BRACKETSZ
- 例1 値：Small | Medium | Medium | Medium | Medium
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKET, BRACKETNO, LUMINAIRE1, LAMP_1

## g0490（1 列）
- 見出し：BRACKETNO
- 例1 値：Single | Single | Double | Double | Double
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKET, BRACKETSZ, LUMINAIRE1, LAMP_1

## g0491（1 列）
- 見出し：LUMINAIRE1
- 例1 値：Shoebox | Shoebox | Floodlight | LRL NXT-60M | Shoebox
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKET, BRACKETSZ, BRACKETNO, LAMP_1

## g0492（1 列）
- 見出し：LAMP_1
- 例1 値：Unknown | LED 41W | Unknown | Unknown | LED 41W
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1

## g0493（1 列）
- 見出し：LUMINAIRE2
- 例1 値：Shoebox | Floodlight | Shoebox | Shoebox | Sylvania Roadster
  - 同じ表の列：CATEGORY, POLENO, HEIGHT, POLE, BRACKET, BRACKETSZ, BRACKETNO, LUMINAIRE1

## g0494（4 列）
- 見出し：Month
- 例1 値：February | February | February | February | January
  - 同じ表の列：Year, State, ATC_Classification, Scheme, Services, Benefits ($)
- 例2 値：September | September | September | August | October
  - 同じ表の列：Request Type, Financial Year, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0495（1 列）
- 見出し：ATC_Classification
- 例1 値：Sensory Organs | Musculo-Skeletal System | Musculo-Skeletal System | Anti-Neoplastic and Immunomodulating Ag… | Musculo-Skeletal System
  - 同じ表の列：Year, Month, State, Scheme, Services, Benefits ($)

## g0496（1 列）
- 見出し：Scheme
- 例1 値：Normal Arrangements PBS | Special Arrangements RPBS | Special Arrangements PBS | Normal Arrangements PBS | Normal Arrangements PBS
  - 同じ表の列：Year, Month, State, ATC_Classification, Services, Benefits ($)

## g0497（1 列）
- 見出し：Services
- 例1 値：9 | 35 | 51823 | 4 | 12360
  - 同じ表の列：Year, Month, State, ATC_Classification, Scheme, Benefits ($)

## g0498（1 列）
- 見出し：Benefits ($)
- 例1 値：581773 | 2201080 | 300244 | 6848 | 43470
  - 同じ表の列：Year, Month, State, ATC_Classification, Scheme, Services

## g0499（1 列）
- 見出し：2016/2017
- 例1 値：University of Newcastle | Relationships Australia | Vuca | VUCA | Total Consultancies Above $10,000 each
  - 同じ表の列：Purpose, Value

## g0500（1 列）
- 見出し：Purpose
- 例1 値：Provide a written report about mental h… | Develop a proposal to build capacity fo… | $100,931 | Provide lived experience and advice reg… | Provide lived experience and advice reg…
  - 同じ表の列：2016/2017, Value

## g0501（1 列）
- 見出し：Value
- 例1 値：$11,576 | $10,830 | Value | $15,887 | $30,000
  - 同じ表の列：2016/2017, Purpose

## g0502（1 列）
- 見出し：Year
- 例1 値：1 July 2016 - 30 June 2017 | ^ Actual number who attended was not re… | 1 July 2019 - 30 June 2020 | 1 July 2021 - 30 June 2022 | 1 July 2022 - 30 June 2023
  - 同じ表の列：Presentations, No Attended ^, No Booked

## g0503（1 列）
- 見出し：Presentations
- 例1 値：178 | 212 | 168 | 211 | 128
  - 同じ表の列：Year, No Attended ^, No Booked

## g0504（1 列）
- 見出し：No Attended ^
- 例1 値：N/A ^ | N/A ^ | N/A ^ | N/A ^ | N/A ^
  - 同じ表の列：Year, Presentations, No Booked

## g0505（1 列）
- 見出し：No Booked
- 例1 値：11 198 | 14 958 | 19 557 | 18 436 | 15 712
  - 同じ表の列：Year, Presentations, No Attended ^

## g0506（1 列）
- 見出し：X Values
- 例1 値：Lead and\\compounds | Total VOCs | SO_2 | PM_{2.5} | CO
  - 同じ表の列：Series1, %series1

## g0507（1 列）
- 見出し：Series1
- 例1 値：-0.146964984983979 | -0.023263441450675 | -0.251129202264524 | -0.08359967023579 | -0.059212011643561
  - 同じ表の列：X Values, %series1

## g0508（1 列）
- 見出し：%series1
- 例1 値：-2.32634414506751 | -25.1129202264525 | -42.2206875140308 | -14.6964984983979 | -5.92120116435608
  - 同じ表の列：X Values, Series1

## g0509（1 列）
- 見出し：Year end
- 例1 値：2024 | 2023 | 2021 | 2014 | 2016
  - 同じ表の列：Category, No, Amount

## g0510（1 列）
- 見出し：Category
- 例1 値：Total | Total | Total | Total | Total
  - 同じ表の列：Year end, No, Amount

## g0511（1 列）
- 見出し：Amount
- 例1 値：$0 | $0 | $0 | $0 | $111,000
  - 同じ表の列：Year end, Category, No

## g0512（3 列）
- 見出し：Year
- 例1 値：2024-25 | 2019-20 | 2020-21 | 2012-13 | 2023-24
  - 同じ表の列：Number of Investiga…
- 例2 値：2005-06 | 2005-06 | 2005-06 | 2005-06 | 2005-06
  - 同じ表の列：Trade type, SITC 3 digit, Country, Geographic level 1, Geographic level 2, Geographic level 3, APEC, ASEAN

## g0513（1 列）
- 見出し：Number of Investigations completed
- 例1 値：3,700 | 11,365 | 4,003 | 8,877 | 6,828
  - 同じ表の列：Year

## g0514（1 列）
- 見出し：Service_Area_Identifier
- 例1 値：CHLT | NANG | BNYP | RPDM | HAES
  - 同じ表の列：Latlong, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0515（1 列）
- 見出し：Latlong
- 例1 値：-27.9894253,153.3473969 | -37.8107398,144.7055969 | -33.817140, 151.090610 | -32.2295160,115.9854154 | -35.343279, 149.083854
  - 同じ表の列：Service_Area_Identi…, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0516（1 列）
- 見出し：Anticipatory Notice Reference Date
- 例1 値：2025-08-04 00:00:00 | 2026-07-23 00:00:00 | 2024-09-02 00:00:00 | 2024-12-27 00:00:00 | 2024-07-29 00:00:00
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Date Completed, Estate Complete

## g0517（1 列）
- 見出し：Date Completed
- 例1 値：2026-09-23 00:00:00 | 2026-09-23 00:00:00 | 2026-09-23 00:00:00 | 2026-09-23 00:00:00 | 2026-09-23 00:00:00
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Estate Complete

## g0518（1 列）
- 見出し：Estate Complete
- 例1 値：N | Y | N | N | Y
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed

## g0519（1 列）
- 見出し：Council_Managed
- 例1 値：true | true | true | true | true
  - 同じ表の列：Long, Lat

## g0520（1 列）
- 見出し：Year:
- 例1 値：2016 | 2020 | 2018 | 2019 | 2017
  - 同じ表の列：Notification rate o…

## g0521（1 列）
- 見出し：Notification rate of Tuberculosis per 100,000 population
- 例1 値：6 | 6.2 | 5.8 | 5.8 | 5.2
  - 同じ表の列：Year:

## g0522（2 列）
- 見出し：wheelchair
- 例1 値：yes | yes | yes | yes | yes
  - 同じ表の列：id, lat, lon, needle_bin
- 例2 値：no | yes | no | yes | yes
  - 同じ表の列：lat, lon, needle_bin, operator, ref

## g0523（2 列）
- 見出し：needle_bin
- 例1 値：yes | no | no | yes | yes
  - 同じ表の列：id, lat, lon, wheelchair
- 例2 値：no | no | no | no | no
  - 同じ表の列：lat, lon, wheelchair, operator, ref

## g0524（1 列）
- 見出し：Nature of Fraud
- 例1 値：Use of TAFE SA Premise and duty time fo… | Theft of monies | Total | Theft of computer equipment | Discrepancy in cash balance
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0525（1 列）
- 見出し：2024-25
- 例1 値：0
  - 同じ表の列：Nature of Fraud, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0526（1 列）
- 見出し：2023-24
- 例1 値：0
  - 同じ表の列：Nature of Fraud, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0527（1 列）
- 見出し：2022-23
- 例1 値：0
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0528（1 列）
- 見出し：2021-22
- 例1 値：1 | 1
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g0529（1 列）
- 見出し：2020-21
- 例1 値：2 | 2
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g0530（1 列）
- 見出し：2019-20
- 例1 値：1 | 1 | 2
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g0531（1 列）
- 見出し：2018-19
- 例1 値：0
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g0532（1 列）
- 見出し：2017-18
- 例1 値：1 | 1
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0533（1 列）
- 見出し：2016-17
- 例1 値：1 | 1 | 2
  - 同じ表の列：Nature of Fraud, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0534（2 列）
- 見出し：Date
- 例1 値：2011-11-17T00:00:00 | 2009-09-13T00:00:00 | 2011-02-26T00:00:00 | 2012-02-02T00:00:00 | 2011-06-03T00:00:00
  - 同じ表の列：Douglas WTP (ML), Northern WTP (ML), Daily Production (M…
- 例2 値：2018-08-02T21:01:43 | 2018-07-06T21:12:05 | 2018-08-11T23:26:56 | 2018-07-11T05:28:15 | 2018-07-31T04:32:26
  - 同じ表の列：id, region, todaywww, tonightwww, tomorrowwww

## g0535（1 列）
- 見出し：Douglas WTP (ML)
- 例1 値：68.94 | 58.98 | 91.63 | 128.041 | 55.75
  - 同じ表の列：Date, Northern WTP (ML), Daily Production (M…

## g0536（1 列）
- 見出し：Northern WTP (ML)
- 例1 値：14.55 | 16.34618594 | 28.24 | 16.57 | 19.84
  - 同じ表の列：Date, Douglas WTP (ML), Daily Production (M…

## g0537（1 列）
- 見出し：Daily Production (ML)
- 例1 値：115.47 | 120.67999999999999 | 118.63 | 182.702 | 108
  - 同じ表の列：Date, Douglas WTP (ML), Northern WTP (ML)

## g0538（1 列）
- 見出し：Funding agency
- 例1 値：DWATSIPM | DWATSIPM | DWATSIPM | DWATSIPM | DWATSIPM
  - 同じ表の列：Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0539（1 列）
- 見出し：Program title
- 例1 値：Celebrating Reconciliation Grants | Social Reinvestment | Local Thriving Communities | Strengthening Communities Multicultural… | Empowering Queensland Women grant progr…
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0540（1 列）
- 見出し：Sub-program title
- 例1 値：NAIDOC Week Events
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0541（1 列）
- 見出し：Purpose
- 例1 値：The Celebrating Reconciliation Grants P… | To support events and festivals that in… | To fund multicultural community-led inf… | To create opportunities to encourage th… | One-off funding is available to support…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0542（1 列）
- 見出し：Category1
- 例1 値：Aboriginal and Torres Strait Islander p… | Community support | Aboriginal and Torres Strait Islander p… | Aboriginal and Torres Strait Islander p… | Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Category3, Client group1, Client group2

## g0543（1 列）
- 見出し：Category2
- 例1 値：Health and wellbeing | Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0544（1 列）
- 見出し：Category3
- 例1 値：Parents and families
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0545（1 列）
- 見出し：Client group1
- 例1 値：Aboriginal and Torres Strait Islanders | Aboriginal and Torres Strait Islanders | Aboriginal and Torres Strait Islanders | Women | Women
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0546（1 列）
- 見出し：Client group2
- 例1 値：All Queenslanders | All Queenslanders | All Queenslanders | All Queenslanders | All Queenslanders
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0547（1 列）
- 見出し：Client group3
- 例1 値：All Queenslanders | Community groups | Young people 16-25 years | Community groups | All Queenslanders
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0548（2 列）
- 見出し：_id
- 例1 値：2 | 1 | 4 | 3 | 5
  - 同じ表の列：Library, General Comp Hours, Adaptive Comp Hours, iMAC Comp Hours, Gene Comp Hours, Patron PC Sessions
- 例2 値：2 | 3 | 1 | 4 | 5
  - 同じ表の列：Library, CKOs Only, Total Loans, RFID CKOs only, RFID loans

## g0549（2 列）
- 見出し：Library
- 例1 値：Wyndham Vale | Julia Gillard Library Tarneit | Point Cook | Plaza | Werribee
  - 同じ表の列：_id, General Comp Hours, Adaptive Comp Hours, iMAC Comp Hours, Gene Comp Hours, Patron PC Sessions
- 例2 値：Werribee | Plaza | Julia Gillard Library Tarneit | Point Cook | Wyndham Vale
  - 同じ表の列：_id, CKOs Only, Total Loans, RFID CKOs only, RFID loans

## g0550（1 列）
- 見出し：General Comp Hours
- 例1 値：9577.47 | 7415.84 | 13937.39 | 10933.42 | 26969.51
  - 同じ表の列：_id, Library, Adaptive Comp Hours, iMAC Comp Hours, Gene Comp Hours, Patron PC Sessions

## g0551（1 列）
- 見出し：Adaptive Comp Hours
- 例1 値：1564.03 | 1170.71 | 2188.27 | 497.75 | 1151.12
  - 同じ表の列：_id, Library, General Comp Hours, iMAC Comp Hours, Gene Comp Hours, Patron PC Sessions

## g0552（1 列）
- 見出し：iMAC Comp Hours
- 例1 値：0 | 956.45 | 0 | 0 | 316.6
  - 同じ表の列：_id, Library, General Comp Hours, Adaptive Comp Hours, Gene Comp Hours, Patron PC Sessions

## g0553（1 列）
- 見出し：Gene Comp Hours
- 例1 値：0 | 0 | 0 | 0 | 2485.38
  - 同じ表の列：_id, Library, General Comp Hours, Adaptive Comp Hours, iMAC Comp Hours, Patron PC Sessions

## g0554（1 列）
- 見出し：Patron PC Sessions
- 例1 値：18425 | 16534 | 41115 | 13761 | 28141.5
  - 同じ表の列：_id, Library, General Comp Hours, Adaptive Comp Hours, iMAC Comp Hours, Gene Comp Hours

## g0555（3 列）
- 見出し：STATISTIC
- 例1 値：EDA15C02 | EDA15C01 | EDA15C01 | EDA15C01 | EDA15C02
  - 同じ表の列：Statistic, TLIST(A1), Year, C02451V02968, Administrative Coun…, UNIT, VALUE
- 例2 値：HSA07C01 | HSA07C02 | HSA07C01 | HSA07C02 | HSA07C03
  - 同じ表の列：Statistic, TLIST(A1), Year, C01947V02657, Local Authority, UNIT, VALUE

## g0556（1 列）
- 見出し：Statistic
- 例1 値：Schools | Entrants to First Year of Junior Cycle | Schools | Schools | Entrants to First Year of Junior Cycle
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02451V02968, Administrative Coun…, UNIT, VALUE

## g0557（4 列）
- 見出し：TLIST(A1)
- 例1 値：1999 | 1997 | 1997 | 1998 | 1996
  - 同じ表の列：STATISTIC, Statistic, Year, C02451V02968, Administrative Coun…, UNIT, VALUE
- 例2 値：2003 | 2001 | 2007 | 2002 | 1997
  - 同じ表の列：STATISTIC, Statistic, Year, C01947V02657, Local Authority, UNIT, VALUE

## g0558（1 列）
- 見出し：C02451V02968
- 例1 値：162 | 050 | 060 | - | 010
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Administrative Coun…, UNIT, VALUE

## g0559（1 列）
- 見出し：Administrative County
- 例1 値：Longford | Cork County | Roscommon | All Counties | Sligo
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, UNIT, VALUE

## g0560（7 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, Administrative Coun…, VALUE
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, Sector, HOSPTYPE, Type of hospital

## g0561（8 列）
- 見出し：VALUE
- 例1 値：655 | 1153 | 3354 | 26 | 1810
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, Administrative Coun…, UNIT
- 例2 値：56 | 86 | 67 | 86 | 67
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, Sector, HOSPTYPE, Type of hospital

## g0562（2 列）
- 見出し：STATISTIC
- 例1 値：NUMBHOSP | NUMBHOSP | NUMBHOSP | NUMBHOSP | NUMBHOSP
  - 同じ表の列：Statistic Label, YEAR, Year, HOSPSECTOR, Sector, HOSPTYPE, Type of hospital, UNIT
- 例2 値：SURGPROC | SURGPROC | SURGPROC | SURGPROC | SURGPROC
  - 同じ表の列：Statistic Label, YEAR, Year, PROCTYPE, Type of surigcal pr…, CASETYPE, Case type, UNIT

## g0563（1 列）
- 見出し：Statistic Label
- 例1 値：Hospitals by sector | Hospitals by sector | Hospitals by sector | Hospitals by sector | Hospitals by sector
  - 同じ表の列：STATISTIC, YEAR, Year, HOSPSECTOR, Sector, HOSPTYPE, Type of hospital, UNIT

## g0564（1 列）
- 見出し：HOSPSECTOR
- 例1 値：TOT | TOT | PRIV | TOT | TOT
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Sector, HOSPTYPE, Type of hospital, UNIT

## g0565（1 列）
- 見出し：Sector
- 例1 値：Total hospitals | Total hospitals | Total hospitals | Privately owned hospitals | Privately owned hospitals
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, HOSPTYPE, Type of hospital, UNIT

## g0566（1 列）
- 見出し：HOSPTYPE
- 例1 値：ALLHOSP | ALLHOSP | ALLHOSP | GENHOSP | ALLHOSP
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, Sector, Type of hospital, UNIT

## g0567（1 列）
- 見出し：Type of hospital
- 例1 値：All types of hospitals | All types of hospitals | All types of hospitals | All types of hospitals | All types of hospitals
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, HOSPSECTOR, Sector, HOSPTYPE, UNIT

## g0568（1 列）
- 見出し：Statistic
- 例1 値：Authorised Starts for Local Authority H… | Authorised Starts for Local Authority H… | Authorised Starts for Local Authority H… | Actual Starts for Local Authority Housi… | Actual Starts for Local Authority Housi…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C01947V02657, Local Authority, UNIT, VALUE

## g0569（1 列）
- 見出し：C01947V02657
- 例1 値：03 | 32 | 17 | 06 | 32
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Local Authority, UNIT, VALUE

## g0570（1 列）
- 見出し：Local Authority
- 例1 値：Cork (City Council) | Offaly (County Council) | Wicklow (County Council) | Limerick (City Council) | Tipperary S.R. (County Council)
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C01947V02657, UNIT, VALUE

## g0571（1 列）
- 見出し：Type
- 例1 値：short term visa applications | long term visa applications | long term visa applications | long term visa applications | long term visa applications
  - 同じ表の列：Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0572（4 列）
- 見出し：Status
- 例1 値：Granted | Received | Received | Received | Granted
  - 同じ表の列：Type, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022
- 例2 値：Open | Closed | Open | Open | Closed
  - 同じ表の列：School Code, SA4, Year

## g0573（1 列）
- 見出し：Nationality
- 例1 値：Marshall Islands (the) | Papua New Guinea | Kenya | Nepal | Western Sahara
  - 同じ表の列：Type, Status, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0574（2 列）
- 見出し：unsafe_2017
- 例1 値：0 | 46 | 104 | 37 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022
- 例2 値：0 | 5 | 14 | 25 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0575（2 列）
- 見出し：unsafe_2018
- 例1 値：173 | 8 | * | 127 | 55
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022
- 例2 値：* | 0 | 0 | 9 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2019, unsafe_2020, unsafe_2021, unsafe_2022

## g0576（1 列）
- 見出し：unsafe_2019
- 例1 値：6 | 557 | 39 | 30 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2020, unsafe_2021, unsafe_2022

## g0577（2 列）
- 見出し：unsafe_2020
- 例1 値：* | 0 | 0 | 222 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2021, unsafe_2022
- 例2 値：* | 0 | * | 580 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2021, unsafe_2022

## g0578（1 列）
- 見出し：unsafe_2021
- 例1 値：0 | 36 | 0 | 0 | 6
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2022

## g0579（1 列）
- 見出し：unsafe_2022
- 例1 値：0 | 0 | 0 | 238 | 664
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0580（2 列）
- 見出し：unsafe_2023
- 例1 値：0 | 10 | 21 | 40 | 0
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021
- 例2 値：0 | 22 | 5 | 0 | 27
  - 同じ表の列：Type, Status, Nationality, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0581（2 列）
- 見出し：period
- 例1 値：2015Q2 | 2014Q4 | 2015Q1 | 2016Q1 | 2014Q3
  - 同じ表の列：programme, scheme, basis, nationality_code, nationality, recipients
- 例2 値：2015Q4 | 2021Q2 | 2021Q1 | 2023Q4 | 2020Q1
  - 同じ表の列：programme, scheme, basis, recipients

## g0582（1 列）
- 見出し：programme
- 例1 値：Working Age Income Supports | Illness,Disability and Caring | Pensions | Pensions | Illness,Disability and Caring
  - 同じ表の列：period, scheme, basis, nationality_code, nationality, recipients

## g0583（2 列）
- 見出し：scheme
- 例1 値：UA | RENT | DPMA | WNCP | FIS
  - 同じ表の列：period, programme, basis, nationality_code, nationality, recipients
- 例2 値：CB | FIS | CB | CAR | CB
  - 同じ表の列：period, programme, basis, recipients

## g0584（2 列）
- 見出し：basis
- 例1 値：Social Assistance | Social Assistance | Social Insurance | Social Insurance | Social Insurance
  - 同じ表の列：period, programme, scheme, nationality_code, nationality, recipients
- 例2 値：Social Insurance | Social Insurance | Social Insurance | Social Insurance | Social Insurance
  - 同じ表の列：period, programme, scheme, recipients

## g0585（1 列）
- 見出し：nationality_code
- 例1 値：0 | 5 | 0 | 1 | 4
  - 同じ表の列：period, programme, scheme, basis, nationality, recipients

## g0586（1 列）
- 見出し：nationality
- 例1 値：Irish nationals | EU14 exl Irl(countries in the EU pre 20… | United Kingdom | EU15 to EU27(accession countries joined… | All
  - 同じ表の列：period, programme, scheme, basis, nationality_code, recipients

## g0587（2 列）
- 見出し：recipients
- 例1 値：58302.0 | 396.0 | 3281.0 | 73413.0 | 153.0
  - 同じ表の列：period, programme, scheme, basis, nationality_code, nationality
- 例2 値：686152.0 | 157837.0 | 643159.0 | 166809.0 | 7198.0
  - 同じ表の列：period, programme, scheme, basis

## g0588（1 列）
- 見出し：FID
- 例1 値：5 | 8 | 6 | 3 | 7
  - 同じ表の列：Lat, Long, ITM_X, ITM_Y

## g0589（1 列）
- 見出し：Lat
- 例1 値：53.260259 | 53.293897 | 53.2779072 | 53.3082488 | 53.294541
  - 同じ表の列：FID, Long, ITM_X, ITM_Y

## g0590（1 列）
- 見出し：Long
- 例1 値：-6.1055397 | -6.13367 | -6.2430904 | -6.154886 | -6.16127
  - 同じ表の列：FID, Lat, ITM_X, ITM_Y

## g0591（1 列）
- 見出し：ITM_X
- 例1 値：723002.968128 | 717675.828741 | 722509.166444 | 724540.395006 | 718186.34489
  - 同じ表の列：FID, Lat, Long, ITM_Y

## g0592（2 列）
- 見出し：ITM_Y
- 例1 値：724900.87712 | 728690.984534 | 727896.887913 | 727855.440319 | 728725.897983
  - 同じ表の列：FID, Lat, Long, ITM_X
- 例2 値：727755.6687000003 | 726949.2740000002 | 721838.8602000009 | 726270.0581 | 722963.5820000004
  - 同じ表の列：OBJECTID

## g0593（3 列）
- 見出し：STATISTIC
- 例1 値：IMQ02 | IMQ02 | IMQ02 | IMQ02 | IMQ02
  - 同じ表の列：Statistic, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT
- 例2 値：EDA81 | EDA81 | EDA81 | EDA81 | EDA81
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex, C02460V02978, Type of Second Chan…, UNIT

## g0594（1 列）
- 見出し：Statistic
- 例1 値：Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off)
  - 同じ表の列：STATISTIC, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0595（2 列）
- 見出し：TLIST(Q1)
- 例1 値：20084 | 20081 | 20074 | 20072 | 20053
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT
- 例2 値：20032 | 19941 | 20034 | 19971 | 20102
  - 同じ表の列：STATISTIC, Statistic, Quarter, C02343V02817, Area, UNIT, VALUE

## g0596（2 列）
- 見出し：Quarter
- 例1 値：2006Q1 | 2007Q2 | 2006Q2 | 2010Q3 | 2006Q2
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT
- 例2 値：1981Q2 | 2010Q3 | 2008Q1 | 1990Q4 | 1981Q4
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), C02343V02817, Area, UNIT, VALUE

## g0597（1 列）
- 見出し：C02635V03192
- 例1 値：04 | 05 | 06 | 04 | 06
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0598（1 列）
- 見出し：Shipping Corridor
- 例1 値：All shipping corridors | Continental | Northern | Northern | Northern
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, C02638V03194, Type of Traffic, UNIT

## g0599（2 列）
- 見出し：C02638V03194
- 例1 値：7 | 5 | 5 | 7 | 4
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, Type of Traffic, UNIT
- 例2 値：12 | 12 | 11 | 13 | 12
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Type of Traffic, C01855V02284, Port, UNIT

## g0600（1 列）
- 見出し：Type of Traffic
- 例1 値：Unaccompanied freight traffic | All freight traffic | Driver accompanied freight traffic | Unaccompanied freight traffic | Trade vehicles
  - 同じ表の列：STATISTIC, Statistic, TLIST(Q1), Quarter, C02635V03192, Shipping Corridor, C02638V03194, UNIT

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
