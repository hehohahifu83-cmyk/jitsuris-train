# ラベル用シート 006 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（4 列）
- 見出し：Suburb
- 例1 値：GISBORNE | TYERS | LILYDALE | KAWARREN | CLARKEFIELD
  - 同じ表の列：Region, P/C, Business Ph, Category
- 例2 値：Sunshine | Camperdown | Westmeadows | Ashburton | Strathmore
  - 同じ表の列：State, Business Category, LGA, Region

## g0602（1 列）
- 見出し：P/C
- 例1 値：3770 | 3197 | 3373 | 3756 | 3352
  - 同じ表の列：Region, Suburb, Business Ph, Category

## g0603（1 列）
- 見出し：Business Ph
- 例1 値：Refer to R20 HQ | 03 54 291204 | Refer to R15 HQ | 03 5626 1563 | 5345 6216
  - 同じ表の列：Region, Suburb, P/C, Category

## g0604（2 列）
- 見出し：Category
- 例1 値：Fire Station | Fire Station | Fire Station | Fire Station | Fire Station
  - 同じ表の列：Region, Suburb, P/C, Business Ph
- 例2 値：Economic Recovery | Bushfire Impact | Economic Recovery | Bushfire Impact | Economic Recovery
  - 同じ表の列：location_id, location_type, metric_id, attribute, value

## g0605（1 列）
- 見出し：Business Category
- 例1 値：Recreation Group,Walking Club/Group | Walking Club/Group | Walking Club/Group | Walking Club/Group | Walking Club/Group
  - 同じ表の列：Suburb, State, LGA, Region

## g0606（1 列）
- 見出し：LGA
- 例1 値：Boroondara (C) | Melton (S) | Central Goldfields (S) | Hobsons Bay (C) | Melbourne (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0607（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | Eastern Metropolitan Region | North and West Metropolitan Region | North and West Metropolitan Region | Loddon-Mallee Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0608（1 列）
- 見出し：Location
- 例1 値：Mitchell River | Point Cook RAAF Jetty | Surf fishing beaches | Dromana Pier | Cape Nelson
  - 同じ表の列：Fish, Fishing allowed/not…, Nearest alternative…

## g0609（1 列）
- 見出し：Fish
- 例1 値：whiting, flathead, snapper. | flathead, whiting, mullet, silver treva… | flathead, snapper, whiting, garfish | Australian salmon, gummy shark, snapper | bream, whiting
  - 同じ表の列：Location, Fishing allowed/not…, Nearest alternative…

## g0610（1 列）
- 見出し：Fishing allowed/not allowed
- 例1 値：Tick: Fishing is allowed | Tick: Fishing is allowed | Tick: Fishing is allowed | Tick: Fishing is allowed | Tick: Fishing is allowed
  - 同じ表の列：Location, Fish, Nearest alternative…

## g0611（1 列）
- 見出し：Nearest alternative fishing spot
- 例1 値：. | . | Moggs Creek, less than 5 km away for sa… | . | .
  - 同じ表の列：Location, Fish, Fishing allowed/not…

## g0612（1 列）
- 見出し：Portfolio
- 例1 値：Treasury | Health, Disability and Ageing | Agriculture, Fisheries and Forestry | Home Affairs | Treasury
  - 同じ表の列：Agency, Tier, DCA 2026, DCA 2025, DCA 2024, Delivery status, Total budget (milli…, Digital budget (mil…

## g0613（1 列）
- 見出し：Agency
- 例1 値：Department of Health, Disability and Ag… | Inspector-General of Water Compliance | Australian Taxation Office | Australian Securities and Investments C… | Questacon
  - 同じ表の列：Portfolio, Tier, DCA 2026, DCA 2025, DCA 2024, Delivery status, Total budget (milli…, Digital budget (mil…

## g0614（1 列）
- 見出し：Tier
- 例1 値：Tier 3 | Tier 3 | Tier 3 | Tier 3 | Tier 2
  - 同じ表の列：Portfolio, Agency, DCA 2026, DCA 2025, DCA 2024, Delivery status, Total budget (milli…, Digital budget (mil…

## g0615（1 列）
- 見出し：DCA 2026
- 例1 値：Medium | Medium-High | Medium-High | Medium | Medium-High
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2025, DCA 2024, Delivery status, Total budget (milli…, Digital budget (mil…

## g0616（1 列）
- 見出し：DCA 2025
- 例1 値：Medium | Medium | Medium-High | Medium-High | Medium
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2024, Delivery status, Total budget (milli…, Digital budget (mil…

## g0617（1 列）
- 見出し：DCA 2024
- 例1 値：Not reported | Medium-High | Not reported | Medium | Medium-High
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2025, Delivery status, Total budget (milli…, Digital budget (mil…

## g0618（1 列）
- 見出し：Delivery status
- 例1 値：Active | Closed | Active | Closed | Active
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2025, DCA 2024, Total budget (milli…, Digital budget (mil…

## g0619（1 列）
- 見出し：Total budget (millions)
- 例1 値：3.2 | 275.2 | 287.9 | 15.5 | 9.5
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2025, DCA 2024, Delivery status, Digital budget (mil…

## g0620（1 列）
- 見出し：Digital budget (millions)
- 例1 値：68.4 | 9.5 | 14.5 | 15.1 | 7.7
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2025, DCA 2024, Delivery status, Total budget (milli…

## g0621（1 列）
- 見出し：Project start date
- 例1 値：Jan-19 | Jul-23 | Jul-24 | Feb-23 | Nov-23
  - 同じ表の列：Portfolio, Agency, Tier, DCA 2026, DCA 2025, DCA 2024, Delivery status, Total budget (milli…

## g0622（1 列）
- 見出し：Contractor
- 例1 値：Hays Recruiting Experts Worldwide | Hays Recruiting Experts Worldwide | Contractors with a contract value below… | 2018-19 | Aktis Performance Management
  - 同じ表の列：Purpose, $ Actual payment

## g0623（1 列）
- 見出し：Purpose
- 例1 値：External audit | Corporate ID project | Financial analysis | Office Design | Purpose
  - 同じ表の列：Contractor, $ Actual payment

## g0624（1 列）
- 見出し：$ Actual payment
- 例1 値：$ Actual payment | $19,960 | $ Actual payment | $183,945 | $317,135
  - 同じ表の列：Contractor, Purpose

## g0625（1 列）
- 見出し：Site
- 例1 値：abellpoint | abellpoint | abellpoint | abellpoint | abellpoint
  - 同じ表の列：Seconds, DateTime, Water Level, Prediction, Residual

## g0626（1 列）
- 見出し：Seconds
- 例1 値：1792219200 | 1792348200 | 1792257000 | 1792362000 | 1792201200
  - 同じ表の列：Site, DateTime, Water Level, Prediction, Residual

## g0627（1 列）
- 見出し：DateTime
- 例1 値：2026-10-21T09:00 | 2026-10-22T22:30 | 2026-10-23T12:20 | 2026-10-21T08:00 | 2026-10-17T13:20
  - 同じ表の列：Site, Seconds, Water Level, Prediction, Residual

## g0628（1 列）
- 見出し：Water Level
- 例1 値：1.860 | 0.618 | 0.686 | 1.395 | 2.067
  - 同じ表の列：Site, Seconds, DateTime, Prediction, Residual

## g0629（1 列）
- 見出し：Prediction
- 例1 値：2.420 | 2.474 | 1.266 | 1.125 | 2.410
  - 同じ表の列：Site, Seconds, DateTime, Water Level, Residual

## g0630（1 列）
- 見出し：Residual
- 例1 値：0.194 | 0.152 | 0.263 | 0.175 | 0.203
  - 同じ表の列：Site, Seconds, DateTime, Water Level, Prediction

## g0631（1 列）
- 見出し：Contractor
- 例1 値：BDO Advisory (SA) P/L | Dr Pat Walsh | Chillogy Pty Ltd | KPMG | Gus Commercial Consulting (SA) Pty Ltd
  - 同じ表の列：Year, Purpose, Value

## g0632（1 列）
- 見出し：Purpose
- 例1 値：Assurance work on SA Water Regulatory D… | Conciliation advice | Review of SAWRD20 processes | Nil | Temporary staffing
  - 同じ表の列：Year, Contractor, Value

## g0633（1 列）
- 見出し：Value
- 例1 値：Nil | $14,824 | $27,750 | $15,435 | $84,066
  - 同じ表の列：Year, Contractor, Purpose

## g0634（1 列）
- 見出し：Complex_Type
- 例1 値：Equestrian Centre | Recreation Reserve | Recreation Reserve | Stadium | Hall Reserve
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Capacity

## g0635（1 列）
- 見出し：Facility_Type
- 例1 値：Meeting Room | Meeting Room | Meeting Room | Meeting Room | Meeting Room
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Capacity

## g0636（1 列）
- 見出し：Bookable_Item
- 例1 値：Woady Yaloak Equestrian Centre Nissan H… | Bannockburn Victoria Park Recreation Ov… | Haddon Recreation Reserve Pavilion | Bannockburn Tennis Pavilion | Lethbridge Recreation Reserve Tennis Pa…
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, Home_Clubs, Capacity

## g0637（1 列）
- 見出し：Assessment_No
- 例1 値：43600430 | 41400011 | 66116405 | 41400035 | 41400035
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, Home_Clubs, Capacity

## g0638（2 列）
- 見出し：Number
- 例1 値：5 | 1164 | 19 | 27 | 396
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, Home_Clubs, Capacity
- 例2 値：329 | 567 | 2518 | 664 | 340
  - 同じ表の列：Prisons, Year

## g0639（1 列）
- 見出し：Locality
- 例1 値：Bannockburn | Bannockburn | Meredith | Smythesdale | Bannockburn
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, Home_Clubs, Capacity

## g0640（1 列）
- 見出し：Post_Code
- 例1 値：3328 | 3331 | 3331 | 3351 | 3321
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Home_Clubs, Capacity

## g0641（1 列）
- 見出し：Home_Clubs
- 例1 値：Haddon Community Learning Centre; Haddo… | Sutherlands Creek Tennis Club | Haddon Community Learning Centre; Haddo… | Gheringhap Tennis Club | Haddon Community Learning Centre; Haddo…
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Capacity

## g0642（1 列）
- 見出し：Capacity
- 例1 値：12 people | 15 people | 16 people conference, 25 people theatre… | 8 people | 12 people
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs

## g0643（1 列）
- 見出し：Day
- 例1 値：Friday | Wednesday | Tuesday | Monday | Tuesday
  - 同じ表の列：Descr, Cycle, Land_Sch, Recyc_Sch, Green_Sch

## g0644（1 列）
- 見出し：Descr
- 例1 値：Thursday Area 2 | Friday Area 2 | Wednesday Area 1 | Wednesday Area 2 | Tuesday Area 2
  - 同じ表の列：Day, Cycle, Land_Sch, Recyc_Sch, Green_Sch

## g0645（1 列）
- 見出し：Cycle
- 例1 値：22T | 21H | 22M | 21F | 21T
  - 同じ表の列：Day, Descr, Land_Sch, Recyc_Sch, Green_Sch

## g0646（1 列）
- 見出し：Land_Sch
- 例1 値：R/2015-01-08/PW | R/2015-01-07/PW | R/2015-01-06/PW | R/2015-01-02/PW | R/2015-01-06/PW
  - 同じ表の列：Day, Descr, Cycle, Recyc_Sch, Green_Sch

## g0647（1 列）
- 見出し：Recyc_Sch
- 例1 値：R/2015-01-02/P2W | R/2015-01-09/P2W | R/2015-01-12/P2W | R/2015-01-13/P2W | R/2015-01-15/P2W
  - 同じ表の列：Day, Descr, Cycle, Land_Sch, Green_Sch

## g0648（1 列）
- 見出し：Green_Sch
- 例1 値：R/2015-01-06/P2W | R/2015-01-07/P2W | R/2015-01-09/P2W | R/2015-01-02/P2W | R/2015-01-08/P2W
  - 同じ表の列：Day, Descr, Cycle, Land_Sch, Recyc_Sch

## g0649（3 列）
- 見出し：X
- 例1 値：142.3174856 | 142.2418538 | 142.5085313 | 142.4581346 | 142.4828401
  - 同じ表の列：Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel
- 例2 値：720482.1265 | 716419.5954 | 720907.2748 | 709541.933 | 714068.3476
  - 同じ表の列：Y, OBJECTID, DESCRIPTIO, TESSELLATE, VISIBILITY, METRES, AREA, CATEGORY

## g0650（2 列）
- 見出し：Y
- 例1 値：-36.7005268 | -36.6883409 | -36.6913494 | -36.7453952 | -36.8117543
  - 同じ表の列：X, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel
- 例2 値：-36.721278 | -36.7113226 | -36.7301552 | -36.7211965 | -36.7241837
  - 同じ表の列：Id, Status, Regulation, X

## g0651（1 列）
- 見出し：Manual_Gauge_Location
- 例1 値：WimmeraRiverTownGauge | WimmeraRiverFauxsBridge | MtWilliamCreekWalWalRd | WimmeraRiverRiverside | YarriambiackCreekLongerenongRd
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel

## g0652（1 列）
- 見出し：Manual_Gauge_Location_Display_Value
- 例1 値：Yarriambiack Creek - Longerenong Rd | Wimmera River - Southbank Horsham | Mt William Creek - Wal Wal Rd | Wimmera River - Riverside Bridge | MacKenzie River - Tatlocks Bridge
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel

## g0653（1 列）
- 見出し：2011_Peak_Flood_level_in_100year
- 例1 値：3.05M | Flood study still underway | 2.82M | 3.55M | 2.40M
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel

## g0654（1 列）
- 見出し：50_year_Design_Floodlevel
- 例1 値：2.77M | 0.17M | 1.57M | 3.45M | Flood study still underway
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 20_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel

## g0655（1 列）
- 見出し：20_year_Design_Floodlevel
- 例1 値：1.56M | 0.51M | Flood study still underway | 2.75M | 3.25M
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 1996_Peak_Floodlevel, 1983_Peak_Floodlevel

## g0656（1 列）
- 見出し：1996_Peak_Floodlevel
- 例1 値：1.92M | No flow | 1.95M | 3.00M | No data available
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1983_Peak_Floodlevel

## g0657（1 列）
- 見出し：1983_Peak_Floodlevel
- 例1 値：2.33M | 0.66M | 1.75M | 2.32M | No flow
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel

## g0658（1 列）
- 見出し：photo1
- 例1 値：https://i.imgur.com/2gdMChz.jpg | https://i.imgur.com/OSlSMXz.jpg | https://i.imgur.com/0saT1oJ.jpg | https://i.imgur.com/3HgtA2a.jpg | https://i.imgur.com/WDPS0lp.jpg
  - 同じ表の列：X, Y, Manual_Gauge_Locati…, Manual_Gauge_Locati…, 2011_Peak_Flood_lev…, 50_year_Design_Floo…, 20_year_Design_Floo…, 1996_Peak_Floodlevel

## g0659（1 列）
- 見出し：Agency
- 例1 値：QIMR Berghofer | Qld Health | Dept of Transport and Main Roads | Qld Corrective Services | Qld Health
  - 同じ表の列：Business Unit, Category Group, Category, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status, Region SA4

## g0660（1 列）
- 見出し：Business Unit
- 例1 値：Capital Delivery | Social Housing Delivery Office | Social Housing Delivery Office | REGIONAL | Infrastructure & Precincts
  - 同じ表の列：Agency, Category Group, Category, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status, Region SA4

## g0661（1 列）
- 見出し：Category Group
- 例1 値：Social Services | Building construction and maintenance | General goods and services | Social Services | Information and communication technology
  - 同じ表の列：Agency, Business Unit, Category, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status, Region SA4

## g0662（1 列）
- 見出し：Category
- 例1 値：Utilities | Construction | Building Contractors | Construction | Physical Works
  - 同じ表の列：Agency, Business Unit, Category Group, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status, Region SA4

## g0663（1 列）
- 見出し：Estimated Timing for Release to Market
- 例1 値：Apr - Jun 26 | Apr - Jun 26 | Apr - Jun 26 | Jul - Sep 26 | Jul - Sep 26
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Procurement Method, Spend Range, Funding Status, Region SA4

## g0664（1 列）
- 見出し：Procurement Method
- 例1 値：Open offer method | Limited offer method | Closed or restricted tender | Limited offer method | Closed or restricted tender
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Estimated Timing fo…, Spend Range, Funding Status, Region SA4

## g0665（1 列）
- 見出し：Spend Range
- 例1 値：<10m | N/A | <10m | Less than $1M | <10m
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Estimated Timing fo…, Procurement Method, Funding Status, Region SA4

## g0666（1 列）
- 見出し：Funding Status
- 例1 値：Funded | Funded | Funded | Funded | Funded
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Estimated Timing fo…, Procurement Method, Spend Range, Region SA4

## g0667（1 列）
- 見出し：Region SA4
- 例1 値：South East Queensland | Moreton Bay - North | South East Queensland | Toowoomba | South East Queensland
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status

## g0668（1 列）
- 見出し：Link
- 例1 値：https://www.families.qld.gov.au/our-wor… | https://www.families.qld.gov.au/our-wor… | https://www.families.qld.gov.au/our-wor… | https://www.families.qld.gov.au/our-wor… | https://www.families.qld.gov.au/our-wor…
  - 同じ表の列：Agency, Business Unit, Category Group, Category, Estimated Timing fo…, Procurement Method, Spend Range, Funding Status

## g0669（1 列）
- 見出し：2020-21 2
- 例1 値：2020-21 | 37% | 39.40% | 66.7 | 71
  - 同じ表の列：2019-20 2, 2018-19 2, 2017-18 3, 2016-17, 2015-16, 2014-15, 2013-14

## g0670（1 列）
- 見出し：2019-20 2
- 例1 値：70.3 | 75 | 2019-20 | 24.4% | 21.3%
  - 同じ表の列：2020-21 2, 2018-19 2, 2017-18 3, 2016-17, 2015-16, 2014-15, 2013-14

## g0671（1 列）
- 見出し：2018-19 2
- 例1 値：27 | 1.4 | 23 | 2020-21 | 25.0%
  - 同じ表の列：2020-21 2, 2019-20 2, 2017-18 3, 2016-17, 2015-16, 2014-15, 2013-14

## g0672（1 列）
- 見出し：2017-18 3
- 例1 値：2017-18 2 | 63 | 0.87% of total salary expenditure was c… | 16 | 70% of fully inducted employees complet…
  - 同じ表の列：2020-21 2, 2019-20 2, 2018-19 2, 2016-17, 2015-16, 2014-15, 2013-14

## g0673（1 列）
- 見出し：2016-17
- 例1 値：15 | 55 | 2018-19 | 0.5 | 2016-17 2
  - 同じ表の列：2020-21 2, 2019-20 2, 2018-19 2, 2017-18 3, 2015-16, 2014-15, 2013-14

## g0674（1 列）
- 見出し：2015-16
- 例1 値：2017-18 | 2017-18 | 2015-16 2 | 28.3% | 51
  - 同じ表の列：2020-21 2, 2019-20 2, 2018-19 2, 2017-18 3, 2016-17, 2014-15, 2013-14

## g0675（1 列）
- 見出し：2014-15
- 例1 値：12 employees (17% of full-time equivale… | 22.8% | 0.61% of total salary expenditure was c… | 41 | 18
  - 同じ表の列：2020-21 2, 2019-20 2, 2018-19 2, 2017-18 3, 2016-17, 2015-16, 2013-14

## g0676（1 列）
- 見出し：2013-14
- 例1 値：19 | 37.6 | 0.5 | 13 | 3.5
  - 同じ表の列：2020-21 2, 2019-20 2, 2018-19 2, 2017-18 3, 2016-17, 2015-16, 2014-15

## g0677（1 列）
- 見出し：Variable type
- 例1 値：VARCHAR2(1) | VARCHAR2(3) | NUMBER | NUMBER | VARCHAR2(3)
  - 同じ表の列：Nullable

## g0678（1 列）
- 見出し：Nullable
- 例1 値：Y | Y | Y
  - 同じ表の列：Variable type

## g0679（1 列）
- 見出し：electorate
- 例1 値：Lake Macquarie | Lake Macquarie | Lake Macquarie | Lake Macquarie | Lake Macquarie
  - 同じ表の列：state, site_id, no_legs, leg1, leg2, leg3, leg4, leg5

## g0680（1 列）
- 見出し：site_id
- 例1 値：5856 | 5865 | 5863 | 6047 | 5861
  - 同じ表の列：state, electorate, no_legs, leg1, leg2, leg3, leg4, leg5

## g0681（1 列）
- 見出し：no_legs
- 例1 値：4 | 4 | 4 | 5 | 3
  - 同じ表の列：state, electorate, site_id, leg1, leg2, leg3, leg4, leg5

## g0682（1 列）
- 見出し：leg1
- 例1 値：TC Frith Ave [N] | Warners Bay Rd [N] | Charlestown Rd [SE] | Harrison St [N] | Fairfax Rd [N]
  - 同じ表の列：state, electorate, site_id, no_legs, leg2, leg3, leg4, leg5

## g0683（1 列）
- 見出し：leg2
- 例1 値：Winding Creek Bike Path [SE] | Red Bluff Shared Path [E] | Main Rd [S] | Hillsborough Rd [W] | Hudson St [SE]
  - 同じ表の列：state, electorate, site_id, no_legs, leg1, leg3, leg4, leg5

## g0684（1 列）
- 見出し：leg3
- 例1 値：King St/shared path [S] | Grenache Way/shared path [S] | Pendlebury Rd [S] | Pacific Hwy [SW] | Ranclaud St [SE]
  - 同じ表の列：state, electorate, site_id, no_legs, leg1, leg2, leg4, leg5

## g0685（1 列）
- 見出し：leg4
- 例1 値：Greenway Track [NW] | Ferris St [NW] | Kopa St [NW] | Station St [NW] | Fishery Point Rd/shared path [SW]
  - 同じ表の列：state, electorate, site_id, no_legs, leg1, leg2, leg3, leg5

## g0686（1 列）
- 見出し：leg5
- 例1 値：Bypass entrance ramp [N] | Path to train station [NW]
  - 同じ表の列：state, electorate, site_id, no_legs, leg1, leg2, leg3, leg4

## g0687（2 列）
- 見出し：female
- 例1 値：0 | 1 | 21 | 0 | 31
  - 同じ表の列：state, electorate, site_id, no_legs, leg1, leg2, leg3, leg4
- 例2 値：726 | 2355 | 110 | 109 | 58
  - 同じ表の列：Scholarship Key Sec…, Male, Unknown, Total

## g0688（3 列）
- 見出し：ref
- 例1 値：BU231 | BU226 | BU228 | BU227 | BU224
  - 同じ表の列：lat
- 例2 値：PLE000319 | PLE000418 | PLE000355 | PLE000333 | PLE000341
  - 同じ表の列：class, subclass, type, location, locality, gid, material, additional

## g0689（3 列）
- 見出し：Date
- 例1 値：5/05/2010 | 10/04/2008 | 24/02/2009 | 23/02/2010 | 21/02/2012
  - 同じ表の列：TaxaCode, Caught, Observed
- 例2 値：2020/04/22 | 2020/05/13 | 2020/04/01 | 2020/06/24 | 2020/05/06
  - 同じ表の列：Program, Type, Claim, Processing Time (we…

## g0690（2 列）
- 見出し：TaxaCode
- 例1 値：PHIGRA | MACPEE | CARAUR | MACAMB | BIDBID
  - 同じ表の列：Date, Caught, Observed
- 例2 値：NEMERE | HYPSPP | HYPSPP | MACPEE | HYPSPP
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, operationCode, Abundance, inTimeStamp, isBiomassCalculated

## g0691（1 列）
- 見出し：Caught
- 例1 値：42 | 1 | 19 | 28 | 78
  - 同じ表の列：Date, TaxaCode, Observed

## g0692（1 列）
- 見出し：Observed
- 例1 値：5 | 126 | 1 | 2 | 310
  - 同じ表の列：Date, TaxaCode, Caught

## g0693（2 列）
- 見出し：Rank
- 例1 値：2 | 1 | 7 | 5 | 17
  - 同じ表の列：Application, Usage, Unit, % Usage
- 例2 値：8 | 10 | 7 | 7 | 5
  - 同じ表の列：Year, Count

## g0694（1 列）
- 見出し：Application
- 例1 値：CDNs | Miscellaneous web | Miscellaneous audio | Software updates | Miscellaneous secure web
  - 同じ表の列：Rank, Usage, Unit, % Usage

## g0695（1 列）
- 見出し：Usage
- 例1 値：87.71 | 48.47 | 24.1 | 266.93 | 23.7
  - 同じ表の列：Rank, Application, Unit, % Usage

## g0696（5 列）
- 見出し：Unit
- 例1 値：GB | GB | GB | GB | GB
  - 同じ表の列：Rank, Application, Usage, % Usage
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02498V03025, Sex Category School, VALUE

## g0697（1 列）
- 見出し：% Usage
- 例1 値：0.70% | 2.10% | 0.70% | 5.00% | 1.40%
  - 同じ表の列：Rank, Application, Usage, Unit

## g0698（1 列）
- 見出し：class
- 例1 値：Play Equipment | Play Equipment | Play Equipment | Play Equipment | Play Equipment
  - 同じ表の列：ref, subclass, type, location, locality, gid, material, additional

## g0699（1 列）
- 見出し：subclass
- 例1 値：Park | Pre-school | Park | Park | Park
  - 同じ表の列：ref, class, type, location, locality, gid, material, additional

## g0700（2 列）
- 見出し：type
- 例1 値：Activity Frame | Swing | Shadesail | Spring Rider | Combination Unit
  - 同じ表の列：ref, class, subclass, location, locality, gid, material, additional
- 例2 値：Standard | Fast Charge | Standard | Fast Charge | Fast Charge
  - 同じ表の列：OBJECTID, Details

## g0701（1 列）
- 見出し：location
- 例1 値：Taylors Gully Childcare Centre | Market Square Park | Taylors Gully Park | St Arnaud Early Learning Centre | Bi-Centennial Park
  - 同じ表の列：ref, class, subclass, type, locality, gid, material, additional

## g0702（2 列）
- 見出し：locality
- 例1 値：Stawell | Stawell | St Arnaud | Stawell | St Arnaud
  - 同じ表の列：ref, class, subclass, type, location, gid, material, additional
- 例2 値：Coral Sea | Leafdale | Tummaville | Tully Heads | Tummaville
  - 同じ表の列：Local Government, Closing Date for Ob…, Case Number, Road, Item Type, Path

## g0703（1 列）
- 見出し：gid
- 例1 値：PG-020 | B0066 | B0080 | PG-012 | PG-003
  - 同じ表の列：ref, class, subclass, type, location, locality, material, additional

## g0704（1 列）
- 見出し：material
- 例1 値：Steel/Plywood | Pine Mulch | Plastic | Steel | Timber
  - 同じ表の列：ref, class, subclass, type, location, locality, gid, additional

## g0705（1 列）
- 見出し：additional
- 例1 値：200 mm | Canopy | Single | Quarterpipe | Ultraplay
  - 同じ表の列：ref, class, subclass, type, location, locality, gid, material

## g0706（1 列）
- 見出し：SA4_Groupings
- 例1 値：North East NSW | Sydney-South West | Regional total | NSW Government schools by type and SA4 … | North West NSW
  - 同じ表の列：Primary, Central_Community, Secondary, SSPs, EECs, Total

## g0707（1 列）
- 見出し：Primary
- 例1 値：198 | 659 | 214 | 112 | 944
  - 同じ表の列：SA4_Groupings, Central_Community, Secondary, SSPs, EECs, Total

## g0708（1 列）
- 見出し：Central_Community
- 例1 値：3 | 28 | 1 | 66 | 8
  - 同じ表の列：SA4_Groupings, Primary, Secondary, SSPs, EECs, Total

## g0709（1 列）
- 見出し：Secondary
- 例1 値：38 | 405 | 39 | 38 | 29
  - 同じ表の列：SA4_Groupings, Primary, Central_Community, SSPs, EECs, Total

## g0710（1 列）
- 見出し：SSPs
- 例1 値：17 | 13 | 10 | 8 | 12
  - 同じ表の列：SA4_Groupings, Primary, Central_Community, Secondary, EECs, Total

## g0711（1 列）
- 見出し：EECs
- 例1 値：2 | 2 | 11 | 22 | 2
  - 同じ表の列：SA4_Groupings, Primary, Central_Community, Secondary, SSPs, Total

## g0712（1 列）
- 見出し：Births
- 例1 値：8,251 | 9,205 | 7,187 | 8,363 | 6,729
  - 同じ表の列：Year, Month, Deaths, Marriages

## g0713（1 列）
- 見出し：Deaths
- 例1 値：5,522 | 3,805 | 4,914 | 4,187 | 4,129
  - 同じ表の列：Year, Month, Births, Marriages

## g0714（1 列）
- 見出し：Marriages
- 例1 値：3,454 | 2,773 | 4,905 | 2,871 | 3,655
  - 同じ表の列：Year, Month, Births, Deaths

## g0715（1 列）
- 見出し：Workplace Injury Claims
- 例1 値：Income support payments - gross ($) | Total gross workers compensation expend… | Total new workplace injury claims | Return to Work Costs** | Significant injuries (where lost time e…
  - 同じ表の列：2019-20, 2018-19, % Change (+/-)

## g0716（1 列）
- 見出し：2019-20
- 例1 値：$0 | 0 | 0 | 0 | $0
  - 同じ表の列：Workplace Injury Cl…, 2018-19, % Change (+/-)

## g0717（1 列）
- 見出し：2018-19
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Workplace Injury Cl…, 2019-20, % Change (+/-)

## g0718（1 列）
- 見出し：% Change (+/-)
- 例1 値：0.00% | 0.00% | 0.00% | 0.00% | 0.00%
  - 同じ表の列：Workplace Injury Cl…, 2019-20, 2018-19

## g0719（1 列）
- 見出し：Quarter
- 例1 値：Commissioner of Main Roads | Builders Registration Board of Western … | State Supply Commission | Department of Regional Development and … | Great Southern Institute of Technology
  - 同じ表の列：Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0720（1 列）
- 見出し：Sep-08
- 例1 値：1686 | 18 | 14 | 60 | 294
  - 同じ表の列：Quarter, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

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
