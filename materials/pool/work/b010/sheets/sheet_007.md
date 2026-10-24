# ラベル用シート 007 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：Dec-08
- 例1 値：326 | 2046 | 127445 | 4206 | 7
  - 同じ表の列：Quarter, Sep-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0722（1 列）
- 見出し：Mar-09
- 例1 値：13 | N/A | 48801 | 13 | 266
  - 同じ表の列：Quarter, Sep-08, Dec-08, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0723（1 列）
- 見出し：Jun-09
- 例1 値：2140 | 4 | N/A | 362 | 2255
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0724（1 列）
- 見出し：Sep-09
- 例1 値：1124 | 132447 | 4363 | 164 | 377
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Dec-09, Mar-10, Jun-10

## g0725（1 列）
- 見出し：Dec-09
- 例1 値：N/A | 315 | N/A | 228 | 659
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Mar-10, Jun-10

## g0726（1 列）
- 見出し：Mar-10
- 例1 値：N/A | 152 | 183 | 148 | 13
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Jun-10

## g0727（1 列）
- 見出し：Jun-10
- 例1 値：14 | 291 | 291 | 376 | N/A
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g0728（1 列）
- 見出し：Sep-10
- 例1 値：8 | N/A | 10 | 130 | 16
  - 同じ表の列：Quarter, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g0729（1 列）
- 見出し：Location
- 例1 値：Statewide | Non-Metropolitan | Metropolitan Adelaide | Statewide | Non-Metropolitan
  - 同じ表の列：Item, 2013-14, 2014-15, 2015-16, 2016-17

## g0730（1 列）
- 見出し：Item
- 例1 値：Major Pipeline Lengths (km) | Major Pipeline Lengths (km) | Water sources (ML) | Used Water (km) | Performance (%)
  - 同じ表の列：Location, 2013-14, 2014-15, 2015-16, 2016-17

## g0731（1 列）
- 見出し：2013-14
- 例1 値：96 | 100 | 213926 | 99 | 72137
  - 同じ表の列：Location, Item, 2014-15, 2015-16, 2016-17

## g0732（1 列）
- 見出し：2014-15
- 例1 値：283 | 1309000 | 259 | 400 | 4079
  - 同じ表の列：Location, Item, 2013-14, 2015-16, 2016-17

## g0733（1 列）
- 見出し：2015-16
- 例1 値：3044 | 7419 | 83.1 | 2984 | 97
  - 同じ表の列：Location, Item, 2013-14, 2014-15, 2016-17

## g0734（1 列）
- 見出し：2016-17
- 例1 値：96 | 100 | 76 | 58.9 | 1139000
  - 同じ表の列：Location, Item, 2013-14, 2014-15, 2015-16

## g0735（1 列）
- 見出し：LCODE
- 例1 値：FLET | COLE | BLH1 | GAMW | ADEL
  - 同じ表の列：STATE, LDATECRTD, JURLINK

## g0736（1 列）
- 見出し：LDATECRTD
- 例1 値：1/01/2007 | 1/01/2007 | 23/09/2010 | 1/01/2007 | 1/01/2007
  - 同じ表の列：LCODE, STATE, JURLINK

## g0737（1 列）
- 見出し：JURLINK
- 例1 値：http://www.ntlis.nt.gov.au/placenames/v… | http://www.ntlis.nt.gov.au/placenames/v… | http://www.ntlis.nt.gov.au/placenames/v… | http://www.ntlis.nt.gov.au/placenames/v… | http://www.ntlis.nt.gov.au/placenames/v…
  - 同じ表の列：LCODE, STATE, LDATECRTD

## g0738（1 列）
- 見出し：Road Safety
- 例1 値：Number of Road Safety Contacts issued p… | Number of SAPOL Road Safety Centre atte… | Number of SAPOL Road Safety Centre atte… | * The 2020-21 financial year, saw the R… | Total number people attending SAPOL roa…
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20

## g0739（1 列）
- 見出し：2012-13
- 例1 値：170,193 | 0 | 56,868 | 7,337
  - 同じ表の列：Road Safety, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20

## g0740（1 列）
- 見出し：2015-16
- 例1 値：183,007 | 8,187 | 68,697 | 17
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19, 2019-20

## g0741（1 列）
- 見出し：2016-17
- 例1 値：189,559 | 7,989 | 66,647 | 107
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19, 2019-20

## g0742（1 列）
- 見出し：2017-18
- 例1 値：123 | 210,190 | 8,877 | 79,808
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19, 2019-20

## g0743（1 列）
- 見出し：2018-19
- 例1 値：80 | 181,634 | 8,373 | 74,827
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2019-20

## g0744（1 列）
- 見出し：2019-20
- 例1 値：196,671 | 42,641 | 174 | 5,718
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0745（1 列）
- 見出し：*2020-21
- 例1 値：169,492 | 25,925 | 117 | 0
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0746（1 列）
- 見出し：Adelaide
- 例1 値：29.252 | 27.9 | NaN | 41.0816666666667 | 30.1
  - 同じ表の列：Year, Hobart, Darwin, Canberra, NEPM Standard2

## g0747（1 列）
- 見出し：Hobart
- 例1 値：35.5 | 25.5 | 20.6 | 30.3 | 26.8
  - 同じ表の列：Year, Adelaide, Darwin, Canberra, NEPM Standard2

## g0748（1 列）
- 見出し：Darwin
- 例1 値：33 | 26 | 30 | 39 | 28
  - 同じ表の列：Year, Adelaide, Hobart, Canberra, NEPM Standard2

## g0749（1 列）
- 見出し：Canberra
- 例1 値：20.5 | 23 | 63.6 | 33.8 | 20.2
  - 同じ表の列：Year, Adelaide, Hobart, Darwin, NEPM Standard2

## g0750（1 列）
- 見出し：NEPM Standard2
- 例1 値：50 | 50 | 50 | 50 | 50
  - 同じ表の列：Year, Adelaide, Hobart, Darwin, Canberra

## g0751（1 列）
- 見出し：Year end
- 例1 値：2020 | 2018 | 2023 | 2019 | 2025
  - 同じ表の列：Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs, Total gross workers…

## g0752（1 列）
- 見出し：Total new workplace injury claims
- 例1 値：1 | 0 | 1 | 0 | 2
  - 同じ表の列：Year end, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs, Total gross workers…

## g0753（1 列）
- 見出し：Fatalities
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs, Total gross workers…

## g0754（1 列）
- 見出し：Seriously injured workers
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs, Total gross workers…

## g0755（1 列）
- 見出し：Significant injuries
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Number of notifiabl…, Number of provision…, Return to work costs, Total gross workers…

## g0756（1 列）
- 見出し：Number of notifiable incidents
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of provision…, Return to work costs, Total gross workers…

## g0757（1 列）
- 見出し：Number of provisional improvement, improvement, and prohibit
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Return to work costs, Total gross workers…

## g0758（1 列）
- 見出し：Return to work costs
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Total gross workers…

## g0759（1 列）
- 見出し：Total gross workers compensation expenditure
- 例1 値：$558 | $128,165 | $7,524 | $0 | $3,621
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs

## g0760（1 列）
- 見出し：Income support payments - gross
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year end, Total new workplace…, Fatalities, Seriously injured w…, Significant injuries, Number of notifiabl…, Number of provision…, Return to work costs

## g0761（1 列）
- 見出し：Reasons an agency could not provide access
- 例1 値：UNIVERSITIES - Document does not exist/… | LOCAL - Exempt agency | UNIVERSITIES - Exempt agency | STATE - Document does not exist/lost | LOCAL - Document does not exist/lost
  - 同じ表の列：No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0762（1 列）
- 見出し：No. of times reason used 2024-25
- 例1 値：1 | 21 | 27 | 703 | 5
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0763（1 列）
- 見出し：No. of times reason used 2023-24
- 例1 値：0 | 50 | 1 | 614 | 12
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0764（1 列）
- 見出し：No. of times reason used 2022-23
- 例1 値：0 | 661 | 55 | 32 | 1
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0765（1 列）
- 見出し：No. of times reason used 2021-22
- 例1 値：18 | 33 | 0 | 0 | 0
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0766（1 列）
- 見出し：No. of times reason used 2020-21
- 例1 値：0 | 26 | 0 | 0 | 33
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0767（1 列）
- 見出し：No. of times reason used 2019-20
- 例1 値：2 | 42 | 35 | 2 | 0
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0768（1 列）
- 見出し：No. of times reason used 2018-19
- 例1 値：375 | 0 | 0 | 22 | 46
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0769（1 列）
- 見出し：No. of times reason used 2017-18
- 例1 値：385 | 0 | 19 | 2 | 25
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0770（1 列）
- 見出し：No. of times reason used 2016-17
- 例1 値：19 | 4 | 78 | 547 | 1
  - 同じ表の列：Reasons an agency c…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…, No. of times reason…

## g0771（1 列）
- 見出し：itemid
- 例1 値：842900 | 842592 | 843149 | 842803 | 843175
  - 同じ表の列：title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0772（1 列）
- 見出し：title
- 例1 値：Description des plantes rares cultives … | An account of the English colony in New… | An account of the English colony in New… | An account of the English colony in New… | An account of the English colony in New…
  - 同じ表の列：itemid, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0773（1 列）
- 見出し：caption
- 例1 値：Description des plantes rares cultives … | An account of the English colony in New… | Opp. pg. 541 | An account of the English colony in New… | An account of the English colony in New…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0774（1 列）
- 見出し：albumnumber
- 例1 値：846401 | 846401 | 846401 | 846401 | 846401
  - 同じ表の列：itemid, title, caption, creator, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0775（1 列）
- 見出し：dateofwork
- 例1 値：1798-1802 | 1848- | 1798-1802 | 1798-1802 | 1798-1802
  - 同じ表の列：itemid, title, caption, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber

## g0776（1 列）
- 見出し：collectionitemlink
- 例1 値：http://library.sl.nsw.gov.au/record=b16… | http://library.sl.nsw.gov.au/record=b16… | http://library.sl.nsw.gov.au/record=b16… | http://library.sl.nsw.gov.au/record=b16… | http://library.sl.nsw.gov.au/record=b16…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, digitalitemlink, digitalordernumber

## g0777（1 列）
- 見出し：digitalitemlink
- 例1 値：http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalordernumber

## g0778（1 列）
- 見出し：digitalordernumber
- 例1 値：a1341310 | a1341190 | a1341468 | a1341487 | a1341058
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0779（1 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0780（1 列）
- 見出し：Project Area
- 例1 値：White Rock-S22C | Coridale-S16A | Peppercorn Hill-SCP303A | Peppercorn Hill-SCP304 | Gainsborough Lodge-S1
  - 同じ表の列：Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0781（1 列）
- 見出し：Service_Area_Identifier
- 例1 値：WTRK | STPW | PAKE | PMVW | PPCH
  - 同じ表の列：Project Area, Latlong, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0782（1 列）
- 見出し：Latlong
- 例1 値：-38.0603545,145.5366998 | -27.6979222,152.8412351 | -33.6597859,115.3894640 | -27.6982591,152.8402763 | -37.5431750,145.0243414
  - 同じ表の列：Project Area, Service_Area_Identi…, ID, Anticipatory Notice…, Date Completed, Estate Complete

## g0783（1 列）
- 見出し：Anticipatory Notice Reference Date
- 例1 値：2024-10-28 00:00:00 | 2025-03-10 00:00:00 | 2022-12-15 00:00:00 | 2025-04-16 00:00:00 | 2024-10-28 00:00:00
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Date Completed, Estate Complete

## g0784（1 列）
- 見出し：Date Completed
- 例1 値：2026-10-05 00:00:00 | 2026-10-05 00:00:00 | 2026-10-06 00:00:00 | 2026-10-08 00:00:00 | 2026-10-10 00:00:00
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Estate Complete

## g0785（1 列）
- 見出し：Estate Complete
- 例1 値：N | N | N | N | N
  - 同じ表の列：Project Area, Service_Area_Identi…, Latlong, ID, Anticipatory Notice…, Date Completed

## g0786（2 列）
- 見出し：type
- 例1 値：transfer station | transfer station | transfer station | transfer station | transfer station
  - 同じ表の列：lat, long, open_hrs, holiday, id
- 例2 値：First Application | First Application | First Application | First Application | First Application
  - 同じ表の列：Date, Program, Claim, Processing Time (we…

## g0787（1 列）
- 見出し：open_hrs
- 例1 値：Wednesday (10:00am - 2:00pm); Sunday (1… | Wednesday (1:00pm - 5:00pm); Sunday (1:… | Monday (8.30am - 12:00pm); Thursday (8:… | Tuesday (8:00am - 11:00am); Thursday (8… | Monday (8:30am - 12:00pm); Thursday (8:…
  - 同じ表の列：lat, long, type, holiday, id

## g0788（1 列）
- 見出し：holiday
- 例1 値：ANZAC Day; Good Friday; Christmas Day; … | ANZAC Day; Good Friday; Christmas Day; … | ANZAC Day; Good Friday; Christmas Day; … | ANZAC Day; Good Friday; Christmas Day; … | ANZAC Day; Good Friday; Christmas Day; …
  - 同じ表の列：lat, long, type, open_hrs, id

## g0789（1 列）
- 見出し：Web
- 例1 値：http://www.surfcoast.vic.gov.au/My_Comm… | goodstart.org.au | http://www.surfcoast.vic.gov.au/My_Comm… | http://www.surfcoast.vic.gov.au/My_Comm… | www.lornekindergarten.com.au
  - 同じ表の列：Long, Lat

## g0790（1 列）
- 見出し：Drop-off point
- 例1 値：Anglesea Transfer Station | Darebin Resource Recovery Centre | Drysdale Resource Recovery Centre | Officeworks Ballarat | Officeworks Dandenong
  - 同じ表の列：Suburb

## g0791（1 列）
- 見出し：Scholarship Key Sector
- 例1 値：Unknown | Governance | Other | Environment | Education
  - 同じ表の列：Male, Female, Unknown, Total

## g0792（1 列）
- 見出し：Male
- 例1 値：146 | 1981 | 380 | 99 | 4
  - 同じ表の列：Scholarship Key Sec…, Female, Unknown, Total

## g0793（1 列）
- 見出し：Unknown
- 例1 値：1 | 1
  - 同じ表の列：Scholarship Key Sec…, Male, Female, Total

## g0794（1 列）
- 見出し：Value
- 例1 値：Sub-Total | Value $10,000 and below | Total | Note - figures exclude GST | Value $10,000 and above
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0795（1 列）
- 見出し：2024-25
- 例1 値：Sequencing for SATAC | Site inspection and preparing feasibili… | Develop cyber security strategy | Contract tender advice | Financial systems advice
  - 同じ表の列：Value, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0796（1 列）
- 見出し：2023-24
- 例1 値：Software Asset Management health check … | 1,330,438 | Strategy and Operating Model for the TA… | Fast Track – Vocational Education & Tra… | Valuation Report for TAFE SA Property H…
  - 同じ表の列：Value, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0797（1 列）
- 見出し：2022-23
- 例1 値：Delivery of a strategic risk workshop f… | Review strategic documents, roadmap and… | School Cohort Process mapping and impro… | 973,445 | Informed Decision Making Web and Enrolm…
  - 同じ表の列：Value, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0798（1 列）
- 見出し：2021-22
- 例1 値：550,760 | Student experience - SATAC commercial a… | 9,360 | Bolder Future Project - Professional se… | 541,400
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g0799（1 列）
- 見出し：2020-21
- 例1 値：WHSIM Performance team Services 2020-21… | 13,762 | Education Partnership Process mapping-p… | TAFE SA-Financial Modelling Secondment | Adaptive Insights Review
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g0800（1 列）
- 見出し：2019-20
- 例1 値：257,907 | Formative consultancy advice on the TAF… | Event Management, external communicatio… | Advisory services with respect to TAFE … | Investigate and advise on fees & charge…
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g0801（1 列）
- 見出し：2018-19
- 例1 値：Consulting on review of executive class… | Validation Support in developing fundin… | 7,792 | 184,685 | Event management, external communicatio…
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g0802（1 列）
- 見出し：2017-18
- 例1 値：Professional services and advice relati… | 259,852 | External classification and reclassific… | Fees for professional services rendered… | 0
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0803（1 列）
- 見出し：2016-17
- 例1 値：882,543 | External classifiation and reclassifica… | 9,791 | Materials Handling Project at Tonsley | Classification and Remuneration Advice
  - 同じ表の列：Value, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0804（1 列）
- 見出し：Month
- 例1 値：2024-04-01 00:00:00 | 2024-08-01 00:00:00 | 2025-12-01 00:00:00 | 2019-07-01 00:00:00 | 2021-05-01 00:00:00
  - 同じ表の列：Hervey Range, Magnetic Island - T…, Townsville City Cou…, Waste Received (Ton…

## g0805（1 列）
- 見出し：Hervey Range
- 例1 値：9.1 | 13.34 | 18.22 | 7.5 | 7.4
  - 同じ表の列：Month, Magnetic Island - T…, Townsville City Cou…, Waste Received (Ton…

## g0806（1 列）
- 見出し：Magnetic Island - TCC
- 例1 値：27.799999999999997 | 17.1 | 19.34 | 20.119999999999997 | 23.440000000000005
  - 同じ表の列：Month, Hervey Range, Townsville City Cou…, Waste Received (Ton…

## g0807（1 列）
- 見出し：Townsville City Council
- 例1 値：872.4399999999999 | 731.2399999999996 | 892.4800000000001 | 787.61 | 726.2999999999997
  - 同じ表の列：Month, Hervey Range, Magnetic Island - T…, Waste Received (Ton…

## g0808（1 列）
- 見出し：Waste Received (Tonnes)
- 例1 値：920.2800000000002 | 791.9899999999994 | 699.5599999999998 | 870.6199999999995 | 876.7399999999993
  - 同じ表の列：Month, Hervey Range, Magnetic Island - T…, Townsville City Cou…

## g0809（1 列）
- 見出し：cma_no
- 例1 値：5 | 4 | 3 | 6 | 7
  - 同じ表の列：abbreviation, fax, facebook, twitter, instagram, flickr, picasa, youtube

## g0810（1 列）
- 見出し：abbreviation
- 例1 値：NECMA | NCCMA | PPWCMA | WCMA | CCMA
  - 同じ表の列：cma_no, fax, facebook, twitter, instagram, flickr, picasa, youtube

## g0811（1 列）
- 見出し：fax
- 例1 値：(03) 9781 0199 | (03) 5051 4379 | (03) 5831 6254 | (03) 5232 2759 | (03) 5175 7899
  - 同じ表の列：cma_no, abbreviation, facebook, twitter, instagram, flickr, picasa, youtube

## g0812（1 列）
- 見出し：facebook
- 例1 値：http://www.facebook.com/WimmeraCMA | http://www.facebook.com/pages/North-Cen… | https://www.facebook.com/ppwcma | http://www.facebook.com/pages/Glenelg-H… | http://facebook.com/gbcma
  - 同じ表の列：cma_no, abbreviation, fax, twitter, instagram, flickr, picasa, youtube

## g0813（1 列）
- 見出し：twitter
- 例1 値：https://www.twitter.com/ppwcma | https://twitter.com/northcentralcma | https://twitter.com/eastgippscma | http://twitter.com/gbcma | https://twitter.com/NorthEastCMA
  - 同じ表の列：cma_no, abbreviation, fax, facebook, instagram, flickr, picasa, youtube

## g0814（1 列）
- 見出し：instagram
- 例1 値：https://www.instagram.com/wimmeracma/
  - 同じ表の列：cma_no, abbreviation, fax, facebook, twitter, flickr, picasa, youtube

## g0815（1 列）
- 見出し：flickr
- 例1 値：https://www.flickr.com/photos/122189135… | http://flickr.com/photos/gbcma
  - 同じ表の列：cma_no, abbreviation, fax, facebook, twitter, instagram, picasa, youtube

## g0816（1 列）
- 見出し：picasa
- 例1 値：https://plus.google.com/101573383479854…
  - 同じ表の列：cma_no, abbreviation, fax, facebook, twitter, instagram, flickr, youtube

## g0817（1 列）
- 見出し：youtube
- 例1 値：http://www.youtube.com/user/corangamite… | http://youtube.com/gbcma | https://www.youtube.com/user/ppwcma | https://www.youtube.com/channel/UCJ1iQf… | https://www.youtube.com/channel/UCtZxup…
  - 同じ表の列：cma_no, abbreviation, fax, facebook, twitter, instagram, flickr, picasa

## g0818（1 列）
- 見出し：vimeo
- 例1 値：https://vimeo.com/wgcma
  - 同じ表の列：cma_no, abbreviation, fax, facebook, twitter, instagram, flickr, picasa

## g0819（1 列）
- 見出し：All consultancies below $10,000
- 例1 値：No consultancy spend in the period | No consultancy spend in the period | All consultancies below $10,000 | All consultancies below $10,000 each | Total of all consultancies below $10,000
  - 同じ表の列：Purpose, Value ('000s)

## g0820（1 列）
- 見出し：Purpose
- 例1 値：Windmill Pictures Pty Ltd Governance Fr… | Purpose | N/A | N/A | N/A
  - 同じ表の列：All consultancies b…, Value ('000s)

## g0821（1 列）
- 見出し：Value ('000s)
- 例1 値：Value ('000s) | 0 | 16625 | 0 | 0
  - 同じ表の列：All consultancies b…, Purpose

## g0822（1 列）
- 見出し：Dog
- 例1 値：Dog | Dog | Dog | Dog | Cat
  - 同じ表の列：Staffordshire Bull …, TRI, WERRIBEE

## g0823（1 列）
- 見出し：Staffordshire Bull Terrier
- 例1 値：Rag Doll | Jack Russell Terrier Cross | Bichon Frise Cross | Domestic Medium Hair | Pointer
  - 同じ表の列：Dog, TRI, WERRIBEE

## g0824（1 列）
- 見出し：TRI
- 例1 値：BLK/WHT | WHT/TAN | BLACK | NULL | WHT/BLK
  - 同じ表の列：Dog, Staffordshire Bull …, WERRIBEE

## g0825（1 列）
- 見出し：WERRIBEE
- 例1 値：WERRIBEE | WERRIBEE | WERRIBEE | WERRIBEE | WERRIBEE
  - 同じ表の列：Dog, Staffordshire Bull …, TRI

## g0826（1 列）
- 見出し：PLAY_GROUND
- 例1 値：Jung Recreation Reserve | Minyip Wetlands | Apex Park | Hopetoun Caravan Park &Tennis Court Pla… | Rupanyup Recreation Reserve
  - 同じ表の列：Lat, Long, RUN_BY

## g0827（1 列）
- 見出し：RUN_BY
- 例1 値：Progress Association | Tennis Club/Council | Recreation Reserve Trustees | Beulah Lions Club | Committee/Group/Club
  - 同じ表の列：Lat, Long, PLAY_GROUND

## g0828（1 列）
- 見出し：JH
- 例1 値：BT | PRC | COL1 | VT | RTV0
  - 同じ表の列：table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0829（1 列）
- 見出し：table_1_1_amarach_research___online_s22163
- 例1 値：Employed by a charity or carrying/carri… | TOTAL (UNWTD.) | Charity Public | 6 | Q5a. What, if anything, influences you …
  - 同じ表の列：JH, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0830（1 列）
- 見出し：unsafe_
- 例1 値：36% | 22% | 100% | 38% | 11
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0831（1 列）
- 見出し：unsafe__2
- 例1 値：1% | 14% | 100% | 20 | 1
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__3, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0832（1 列）
- 見出し：unsafe__3
- 例1 値：2 | 885 | 250 | 2% | Female
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__4, unsafe__5, unsafe__6, unsafe__7

## g0833（1 列）
- 見出し：unsafe__4
- 例1 値：15 | 13% | 9% | 31% | 474
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__5, unsafe__6, unsafe__7

## g0834（1 列）
- 見出し：unsafe__5
- 例1 値：51% | 7% | 2 | 86 | 15
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__6, unsafe__7

## g0835（1 列）
- 見出し：unsafe__6
- 例1 値：4 | 55+ | 13% | 1% | 188
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__7

## g0836（1 列）
- 見出し：unsafe__7
- 例1 値：44% | 25 | 117 | 46% | 24
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g0837（1 列）
- 見出し：unsafe__8
- 例1 値：247 | 9% | 1% | 5 | 5%
  - 同じ表の列：JH, table_1_1_amarach_r…, unsafe_, unsafe__2, unsafe__3, unsafe__4, unsafe__5, unsafe__6

## g0838（4 列）
- 見出し：OBJECTID
- 例1 値：16 | 22 | 15 | 11 | 7
  - 同じ表の列：Details, Type
- 例2 値：278 | 207 | 159 | 330 | 394
  - 同じ表の列：X, Y, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, AREA, CATEGORY

## g0839（1 列）
- 見出し：Details
- 例1 値：CHAdeMO DC 45kW (1 space), AC (Type-2) … | Type-2 AC Socket 22kW (x2, ALL Occupied… | 1 charge point with facility to charge … | Type-2 AC Socket 3.7kW Slow Charger (x2… | Type-2 AC Socket 22kW (x2, ALL Availabl…
  - 同じ表の列：OBJECTID, Type

## g0840（1 列）
- 見出し：DEROGATION_YEAR
- 例1 値：2015 | 2020 | 2019 | 2016 | 2016
  - 同じ表の列：DEROGATION_COUNTY, DEROGATION_COUNT, LEA_HERD_COUNT

## 答えの雛形

```
g0721	
g0722	
g0723	
g0724	
g0725	
g0726	
g0727	
g0728	
g0729	
g0730	
g0731	
g0732	
g0733	
g0734	
g0735	
g0736	
g0737	
g0738	
g0739	
g0740	
g0741	
g0742	
g0743	
g0744	
g0745	
g0746	
g0747	
g0748	
g0749	
g0750	
g0751	
g0752	
g0753	
g0754	
g0755	
g0756	
g0757	
g0758	
g0759	
g0760	
g0761	
g0762	
g0763	
g0764	
g0765	
g0766	
g0767	
g0768	
g0769	
g0770	
g0771	
g0772	
g0773	
g0774	
g0775	
g0776	
g0777	
g0778	
g0779	
g0780	
g0781	
g0782	
g0783	
g0784	
g0785	
g0786	
g0787	
g0788	
g0789	
g0790	
g0791	
g0792	
g0793	
g0794	
g0795	
g0796	
g0797	
g0798	
g0799	
g0800	
g0801	
g0802	
g0803	
g0804	
g0805	
g0806	
g0807	
g0808	
g0809	
g0810	
g0811	
g0812	
g0813	
g0814	
g0815	
g0816	
g0817	
g0818	
g0819	
g0820	
g0821	
g0822	
g0823	
g0824	
g0825	
g0826	
g0827	
g0828	
g0829	
g0830	
g0831	
g0832	
g0833	
g0834	
g0835	
g0836	
g0837	
g0838	
g0839	
g0840	
```
