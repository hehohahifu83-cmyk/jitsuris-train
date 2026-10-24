# ラベル用シート 008 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：Information
- 例1 値：<a target=""_blank"" href=https://www.w… | <a target=""_blank"" href=https://www.w… | <a target=""_blank"" href=https://www.w… | <a target=""_blank"" href=https://www.w… | <a target=""_blank"" href=https://www.w…
  - 同じ表の列：OBJECTID, Eff_From, Eff_To, Zoning, Area_Ha, Generic_Zoning, MyPlan_GZT, Designation

## g0842（1 列）
- 見出し：Group Start Date
- 例1 値：2018-07-01 00:00:00 | 2013-07-01 00:00:00 | 2013-07-01 00:00:00 | 2014-07-01 00:00:00 | 2017-09-08 00:00:00
  - 同じ表の列：Group End Date

## g0843（1 列）
- 見出し：Group End Date
- 例1 値：43646 | 43646 | 43646 | 43646 | 43646
  - 同じ表の列：Group Start Date

## g0844（1 列）
- 見出し：FISHERY_ID
- 例1 値：FTR | FTR | FTR | FTR | FTR
  - 同じ表の列：LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME, END_TIME

## g0845（1 列）
- 見出し：LOG_TYPE
- 例1 値：MB06 | MB06 | MB06 | MB06 | MB06
  - 同じ表の列：FISHERY_ID, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME, END_TIME

## g0846（1 列）
- 見出し：BOAT_ID
- 例1 値：1064 | 1064 | 1062 | 1064 | 1064
  - 同じ表の列：FISHERY_ID, LOG_TYPE, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME, END_TIME

## g0847（1 列）
- 見出し：FISHING_DATE
- 例1 値：1983-10-26T00:00:00 | 1981-01-30T00:00:00 | 1981-03-08T00:00:00 | 1980-06-29T00:00:00 | 1980-11-29T00:00:00
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME, END_TIME

## g0848（1 列）
- 見出し：OPERATION_NO
- 例1 値：2 | 4 | 5 | 4 | 3
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, GEAR, POSITION_PRECISION, START_TIME, END_TIME

## g0849（1 列）
- 見出し：GEAR
- 例1 値：PTB | PTB | PTB | PTB | PTB
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, POSITION_PRECISION, START_TIME, END_TIME

## g0850（1 列）
- 見出し：POSITION_PRECISION
- 例1 値：0.008 | 0.008 | 0.008 | 0.008 | 0.008
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, START_TIME, END_TIME

## g0851（1 列）
- 見出し：START_TIME
- 例1 値：1983-11-02T03:30:00 | 1981-03-08T04:20:00 | 1980-06-27T17:35:00 | 1980-10-17T21:30:00 | 1981-03-27T22:00:00
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, END_TIME

## g0852（1 列）
- 見出し：END_TIME
- 例1 値：1980-07-01T06:00:00 | 1980-07-20T02:00:00 | 1983-10-24T21:00:00 | 1980-07-19T23:35:00 | 1980-07-08T00:30:00
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME

## g0853（1 列）
- 見出し：FISHING_TIME
- 例1 値：2.5 | 2.5 | 3.42 | 2.5 | 2.5
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, POSITION_PRECISION, START_TIME

## g0854（2 列）
- 見出し：Date-Time
- 例1 値：2007-12-06 13:38:00 | 2007-12-06 06:46:00 | 2007-12-06 10:07:00 | 2007-12-06 13:12:00 | 2007-12-06 13:42:00
  - 同じ表の列：Lat, Lon, UV_Index
- 例2 値：2007-09-20 18:05:00 | 2007-09-20 03:16:00 | 2007-09-20 14:35:00 | 2007-09-20 01:15:00 | 2007-09-20 07:40:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0855（2 列）
- 見出し：UV_Index
- 例1 値：00.03 | 01.77 | 10.78 | 00.03 | 00.77
  - 同じ表の列：Date-Time, Lat, Lon
- 例2 値：00.02 | 00.36 | 01.24 | 00.27 | 00.01
  - 同じ表の列：Date-Time, Lat, Lon

## g0856（1 列）
- 見出し：Request Type
- 例1 値：STSYR - Syringe Collection Request - St… | STSYR - Syringe Collection Request - St… | STSYR - Syringe Collection Request - St… | STSYR - Syringe Collection Request - St… | STSYR - Syringe Collection Request - St…
  - 同じ表の列：Financial Year, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0857（1 列）
- 見出し：Financial Year
- 例1 値：2016/2017 | 2011/2012 | 2012/2013 | 2016/2017 | 2017/2018
  - 同じ表の列：Request Type, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0858（4 列）
- 見出し：Month
- 例1 値：October | August | February | October | July
  - 同じ表の列：Request Type, Financial Year, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…
- 例2 値：March | May | February | August | December
  - 同じ表の列：Port of Entry, Fiscal Year, Percentage Met Serv…

## g0859（1 列）
- 見出し：MonthYear
- 例1 値：Jun-2014 | Feb-2020 | Mar-2014 | Sep-2013 | Jun-2017
  - 同じ表の列：Request Type, Financial Year, Month, CalendarYear, Suburb, NumberOfRequests_Re…

## g0860（1 列）
- 見出し：CalendarYear
- 例1 値：CY 2016 | CY 2016 | CY 2016 | CY 2016 | CY 2019
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, Suburb, NumberOfRequests_Re…

## g0861（1 列）
- 見出し：Suburb
- 例1 値：RIPPONLEA | ELWOOD | ST KILDA EAST | SOUTH MELBOURNE | ST KILDA EAST
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, NumberOfRequests_Re…

## g0862（1 列）
- 見出し：NumberOfRequests_Received
- 例1 値：2 | 5 | 1 | 2 | 1
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, Suburb

## g0863（1 列）
- 見出し：DATA_AS_AT
- 例1 値：2018-08-05 | 2018-08-05 | 2018-08-05 | 2018-08-05 | 2018-08-05
  - 同じ表の列：JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0864（1 列）
- 見出し：JOB_PLACEMENT_ID
- 例1 値：712112 | 354414 | 460068 | 350052 | 533890
  - 同じ表の列：DATA_AS_AT, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0865（1 列）
- 見出し：JSKR_LINKAGE_KEY
- 例1 値：198533 | 198625 | 198608 | 199190 | 198925
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0866（1 列）
- 見出し：JOB_PLACEMENT_DATE
- 例1 値：2016-09-28 | 2017-06-15 | 2017-06-19 | 2016-12-01 | 2016-07-11
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0867（1 列）
- 見出し：STREAM_PLACEMENT_DESC
- 例1 値：Stream B | Stream B | Stream C | Stream A | Stream A
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0868（1 列）
- 見出し：STREAM_PHASE_TYPE_DESC
- 例1 値：Self Service and Job Activity | Work for the Dole | Case Management | Work for the Dole | Case Management
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, BROAD_OCCUPATION_DE…, OCCUPATION_DESC

## g0869（1 列）
- 見出し：BROAD_OCCUPATION_DESC
- 例1 値：Professionals | Labourers | Managers | Managers | Labourers
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, OCCUPATION_DESC

## g0870（1 列）
- 見出し：OCCUPATION_DESC
- 例1 値：General-Inquiry Clerks, Call Centre, Re… | Numerical Clerks | Hospitality Workers | Construction and Mining Labourers | Sales, Marketing & Public Relations Pro…
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…

## g0871（1 列）
- 見出し：OCCUPATION_DESC_LEVEL_4
- 例1 値：Telemarketers | Other Cleaners | Other Personal Service Workers | Waiters | Freight and Furniture Handlers
  - 同じ表の列：DATA_AS_AT, JOB_PLACEMENT_ID, JSKR_LINKAGE_KEY, JOB_PLACEMENT_DATE, STATE, STREAM_PLACEMENT_DE…, STREAM_PHASE_TYPE_D…, BROAD_OCCUPATION_DE…

## g0872（1 列）
- 見出し：Program
- 例1 値：Road Construction | Footpaths And Bike Paths | Road Construction | Parks | Footpaths And Bike Paths
  - 同じ表の列：ID, Asset_Type, Works_Type, Funding, Council_Reference, Link, Financial_Year, Expected_Start

## g0873（1 列）
- 見出し：Asset_Type
- 例1 値：Roads | Other infrastructure | Road Bridges - Infra Gap | Road Bridges - Infra Gap | Roads
  - 同じ表の列：ID, Program, Works_Type, Funding, Council_Reference, Link, Financial_Year, Expected_Start

## g0874（1 列）
- 見出し：Works_Type
- 例1 値：Renew | New | Renew | New | Upgrade
  - 同じ表の列：ID, Program, Asset_Type, Funding, Council_Reference, Link, Financial_Year, Expected_Start

## g0875（1 列）
- 見出し：Funding
- 例1 値：12000 | 91000 | 48000 | 172500 | 10000
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Council_Reference, Link, Financial_Year, Expected_Start

## g0876（1 列）
- 見出し：Council_Reference
- 例1 値：6418 | 6394 | 6410 | 6405 | 6363
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Funding, Link, Financial_Year, Expected_Start

## g0877（1 列）
- 見出し：Link
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Funding, Council_Reference, Financial_Year, Expected_Start

## g0878（1 列）
- 見出し：Financial_Year
- 例1 値：2017-18 | 2017-18 | 2017-18 | 2017-18 | 2017-18
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Funding, Council_Reference, Link, Expected_Start

## g0879（1 列）
- 見出し：Expected_Start
- 例1 値：TBA | TBA | Nov-17 | Nov-17 | Feb-18
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Funding, Council_Reference, Link, Financial_Year

## g0880（1 列）
- 見出し：Expected_End
- 例1 値：May-18 | Oct-17 | Nov-17 | Jun-18 | Feb-18
  - 同じ表の列：ID, Program, Asset_Type, Works_Type, Funding, Council_Reference, Link, Financial_Year

## g0881（2 列）
- 見出し：Property_ID
- 例1 値：145332 | 150158 | 140828 | 145341 | 159611
  - 同じ表の列：Property_Type, Attribute_Type, Value_1
- 例2 値：102139 | 100810 | 108049 | 107771 | 105295
  - 同じ表の列：gis_id, polyarea, date_updated, json_geometry, geo_point_2d

## g0882（1 列）
- 見出し：Property_Type
- 例1 値：PRO | DWG | PRO | PRO | PRO
  - 同じ表の列：Property_ID, Attribute_Type, Value_1

## g0883（1 列）
- 見出し：Attribute_Type
- 例1 値：FE02 | FE02 | FE02 | FE02 | FE02
  - 同じ表の列：Property_ID, Property_Type, Value_1

## g0884（1 列）
- 見出し：Value_1
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Property_ID, Property_Type, Attribute_Type

## g0885（1 列）
- 見出し：PROP_PROPNUM
- 例1 値：1077984 | 4009943 | 4010180 | 1061673 | 4011949
  - 同じ表の列：PropertyArea_m2, IntersectedArea_m2, Percentage_Property…, Overlay

## g0886（1 列）
- 見出し：PropertyArea_m2
- 例1 値：3663.16 | 841471.58 | 206169.64 | 40739.17 | 505816.51
  - 同じ表の列：PROP_PROPNUM, IntersectedArea_m2, Percentage_Property…, Overlay

## g0887（1 列）
- 見出し：IntersectedArea_m2
- 例1 値：140301.21 | 13213.63 | 23479.92 | 2799.15 | 14726.12
  - 同じ表の列：PROP_PROPNUM, PropertyArea_m2, Percentage_Property…, Overlay

## g0888（1 列）
- 見出し：Percentage_Property_Area_Affected
- 例1 値：8.12 | 34.11 | 31.10 | 1.01 | 6.77
  - 同じ表の列：PROP_PROPNUM, PropertyArea_m2, IntersectedArea_m2, Overlay

## g0889（1 列）
- 見出し：Overlay
- 例1 値：Land Subject to Inundation Overlay | Land Subject to Inundation Overlay | Land Subject to Inundation Overlay | Land Subject to Inundation Overlay | Land Subject to Inundation Overlay
  - 同じ表の列：PROP_PROPNUM, PropertyArea_m2, IntersectedArea_m2, Percentage_Property…

## g0890（1 列）
- 見出し：manager
- 例1 値：DELWP | BOM | BOM | BOM | BOM
  - 同じ表の列：id, start_date, end_date, active, types, icon, parameters, source

## g0891（1 列）
- 見出し：start_date
- 例1 値：1973-01-30 | 1886-01-01 | 1988-06-01 | 1898-05-30 | 1995-05-25
  - 同じ表の列：id, manager, end_date, active, types, icon, parameters, source

## g0892（1 列）
- 見出し：end_date
- 例1 値：1948-01-01 | 1973-12-29 | 2001-05-04 | 1987-06-03 | 1972-01-01
  - 同じ表の列：id, manager, start_date, active, types, icon, parameters, source

## g0893（1 列）
- 見出し：active
- 例1 値：False | True | False | False | False
  - 同じ表の列：id, manager, start_date, end_date, types, icon, parameters, source

## g0894（1 列）
- 見出し：types
- 例1 値：Land Surface | Land Surface | Land Surface | Land Surface | Stream
  - 同じ表の列：id, manager, start_date, end_date, active, icon, parameters, source

## g0895（1 列）
- 見出し：icon
- 例1 値：agriculture | water | agriculture | water | water
  - 同じ表の列：id, manager, start_date, end_date, active, types, parameters, source

## g0896（1 列）
- 見出し：parameters
- 例1 値：Rainfall | Watercourse Level, Watercourse Discharge | Rainfall | Rainfall | Rainfall
  - 同じ表の列：id, manager, start_date, end_date, active, types, icon, source

## g0897（1 列）
- 見出し：source
- 例1 値：http://www.bom.gov.au/waterdata/ | http://www.bom.gov.au/jsp/eiexplorer/ | http://www.bom.gov.au/jsp/eiexplorer/ | http://data.water.vic.gov.au/monitoring… | http://data.water.vic.gov.au/monitoring…
  - 同じ表の列：id, manager, start_date, end_date, active, types, icon, parameters

## g0898（1 列）
- 見出し：x
- 例1 値：143.3 | 142.9 | 142.98 | 142.79 | 141.23
  - 同じ表の列：id, manager, start_date, end_date, active, types, icon, parameters

## g0899（3 列）
- 見出し：Date
- 例1 値：2024-11-20 | 2024-11-20 | 2024-11-20 | 2024-11-20 | 2024-11-20
  - 同じ表の列：CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr
- 例2 値：2006-07-27 | 2006-07-09 | 2006-08-07 | 2006-07-28 | 2006-07-04
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, Essence, etat

## g0900（1 列）
- 見出し：CentreEn_CentreAn
- 例1 値：Wholesale-Montreal | Wholesale-Montreal | Wholesale-Toronto | Wholesale-Toronto | Wholesale-Toronto
  - 同じ表の列：Date, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0901（1 列）
- 見出し：CentreFr_CentreFr
- 例1 値：Prix de gros-Montreal | Prix de gros-Toronto | Prix de gros-Toronto | Prix de gros-Montreal | Prix de gros-Montreal
  - 同じ表の列：Date, CentreEn_CentreAn, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0902（1 列）
- 見出し：CmdtyEn_PrdtAn
- 例1 値：Pears | Lettuce | Apples | Asparagus | Leeks
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0903（1 列）
- 見出し：CmdtyEn_PrdtFr
- 例1 値：Pommes | Brocoli | Oignons | Pamplemousse | Collard
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0904（1 列）
- 見出し：VrtyEn_VrteAn
- 例1 値：Organic-Unspecified | Organic-Unspecified | Unspecified | Field-Jalapeno | Yu Choy
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyFr_VrteFr, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0905（1 列）
- 見出し：VrtyFr_VrteFr
- 例1 値：Biologique-inconnue | En botte | Rouge | De champs-Indien | Biologique-inconnue
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, GradeEn_CtgryAn, GradeFr_CtgryFr

## g0906（1 列）
- 見出し：GradeEn_CtgryAn
- 例1 値：Canada Number 1 | Canada Number 1 | N/A | N/A | N/A
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeFr_CtgryFr

## g0907（1 列）
- 見出し：GradeFr_CtgryFr
- 例1 値：États-Unis Numéro 1 | Canada Numéro 1 | États-Unis Numéro 1 | Canada Numéro 1 | Numéro 1
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn

## g0908（1 列）
- 見出し：Cntry_Pays
- 例1 値：CR | US | MX | US | CR
  - 同じ表の列：Date, CentreEn_CentreAn, CentreFr_CentreFr, CmdtyEn_PrdtAn, CmdtyEn_PrdtFr, VrtyEn_VrteAn, VrtyFr_VrteFr, GradeEn_CtgryAn

## g0909（1 列）
- 見出し：Port of Entry
- 例1 値：Prescott | Stanstead | Boundary Bay | St. Stephen 3rd Bridge | Ambassador Bridge
  - 同じ表の列：Month, Fiscal Year, Percentage Met Serv…

## g0910（3 列）
- 見出し：Fiscal Year
- 例1 値：2021-22 | 2021-22 | 2019-20 | 2020-21 | 2020-21
  - 同じ表の列：Port of Entry, Month, Percentage Met Serv…
- 例2 値：2024-25 | 2024-25 | 2025-26 | 2024-25 | 2024-25
  - 同じ表の列：Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0911（1 列）
- 見出し：Percentage Met Service Standard
- 例1 値：100.00% | 69.22% | 100.00% | 81.59% | 100.00%
  - 同じ表の列：Port of Entry, Month, Fiscal Year

## g0912（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：CFP2018-0003 | CFP2018-0001 | CFP2018-0001 | CFP2018-0003 | CFP2018-0003
  - 同じ表の列：Region - Region, Commodity, denree, Function, Fonction, Origin, Origine, Product

## g0913（1 列）
- 見出し：Region - Region
- 例1 値：ONTARIO | ONTARIO | ONTARIO | ONTARIO | ONTARIO
  - 同じ表の列：Sample No. - No. d'…, Commodity, denree, Function, Fonction, Origin, Origine, Product

## g0914（1 列）
- 見出し：Commodity
- 例1 値：IMFD | IMFD | IMFD | IMFD | IMFD
  - 同じ表の列：Sample No. - No. d'…, Region - Region, denree, Function, Fonction, Origin, Origine, Product

## g0915（1 列）
- 見出し：denree
- 例1 値：DAIM | DAIM | DAIM | DAIM | DAIM
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, Function, Fonction, Origin, Origine, Product

## g0916（2 列）
- 見出し：Function
- 例1 値：Import | Import | Import | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Fonction, Origin, Origine, Product
- 例2 値：TOTAL | CURATIVE | LTC | CURATIVE | REHAB
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Type of function, BEDTYPE, Bed type, UNIT

## g0917（1 列）
- 見出し：Fonction
- 例1 値：importé | importé | importé | importé | importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Origin, Origine, Product

## g0918（1 列）
- 見出し：Origin
- 例1 値：IRELAND | UNITED STATES | IRELAND | UNITED STATES | UNITED STATES
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origine, Product

## g0919（1 列）
- 見出し：Origine
- 例1 値：ÉTATS-UNIS | ÉTATS-UNIS | ÉTATS-UNIS | IRLANDE | IRLANDE
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Product

## g0920（1 列）
- 見出し：Product
- 例1 値：Infant Formula - Dairy | Infant Formula - Dairy | Infant Formula - Dairy | Infant Formula - Dairy | Infant Formula - Dairy
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Origine

## g0921（1 列）
- 見出し：Produit
- 例1 値：Préparation pour nourrissons - Laitier | Préparation pour nourrissons - Laitier | Préparation pour nourrissons - Laitier | Préparation pour nourrissons - Laitier | Préparation pour nourrissons - Laitier
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Origine

## g0922（1 列）
- 見出し：Ref Number | Numero ref
- 例1 値：7468512 | 7469108 | 7380223 | 7428863 | 7230954
  - 同じ表の列：Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…

## g0923（1 列）
- 見出し：Title (English)
- 例1 値：Summary of Hours of Work Warning Letter… | CNSC Field Inspection Record, PLRPD-202… | RE_ EXT - HoW CBT Completion Verificati… | Warning Letter – Point Lepreau Nuclear … | NB Power Update to Action Item 221218-2…
  - 同じ表の列：Ref Number | Numero…, Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…

## g0924（1 列）
- 見出し：Titre (Francais)
- 例1 値：Centrale nucléaire de Point Lepreau : R… | Procès-verbal | RE_EXT - Vérification de l'achèvement d… | Résumé des heures de travail - Suivi de… | Lettre d'avertissement – Centrale nuclé…
  - 同じ表の列：Ref Number | Numero…, Title (English), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…

## g0925（1 列）
- 見出し：Author | Auteur
- 例1 値：CNSC | CNSC | CNSC | CNSC | NB Power
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), # pages, Language | Langue, Date, Availability | Disp…

## g0926（1 列）
- 見出し：# pages
- 例1 値：1 | 2 | 16 | 36 | 1
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, Language | Langue, Date, Availability | Disp…

## g0927（1 列）
- 見出し：Language | Langue
- 例1 値：English | English | English | English | English
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Date, Availability | Disp…

## g0928（1 列）
- 見出し：Date
- 例1 値：9/19/2023 | 1/7/2025 | 2/11/2025 | 3/20/2025 | 2023-02-29
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Availability | Disp…

## g0929（1 列）
- 見出し：Availability | Disponibilite
- 例1 値：Available | Available | Available | Not Available | Available
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Date

## g0930（1 列）
- 見出し：BN
- 例1 値：133652214RR0001 | 129795340RR0001 | 888177649RR0001 | 805182805RR0001 | 831832340RR0001
  - 同じ表の列：FPE, Form ID, #, Position, At Arm's Length, Start Date, End Date

## g0931（1 列）
- 見出し：FPE
- 例1 値：2019-01-31 | 2019-01-31 | 2019-03-31 | 2019-03-31 | 2019-01-01
  - 同じ表の列：BN, Form ID, #, Position, At Arm's Length, Start Date, End Date

## g0932（1 列）
- 見出し：Form ID
- 例1 値：23 | 23 | 23 | 23 | 23
  - 同じ表の列：BN, FPE, #, Position, At Arm's Length, Start Date, End Date

## g0933（1 列）
- 見出し：#
- 例1 値：000000003 | 000000003 | 000000005 | 000000007 | 000000002
  - 同じ表の列：BN, FPE, Form ID, Position, At Arm's Length, Start Date, End Date

## g0934（1 列）
- 見出し：Position
- 例1 値：Member-at-Large | Director | Decorating/Director | Vice Chair | DIRECTOR
  - 同じ表の列：BN, FPE, Form ID, #, At Arm's Length, Start Date, End Date

## g0935（1 列）
- 見出し：At Arm's Length
- 例1 値：Y | Y | N | Y | Y
  - 同じ表の列：BN, FPE, Form ID, #, Position, Start Date, End Date

## g0936（1 列）
- 見出し：Start Date
- 例1 値：1992-05-11 | 2018-03-01 | 2012-09-26 | 2017-05-01 | 2013-04-15
  - 同じ表の列：BN, FPE, Form ID, #, Position, At Arm's Length, End Date

## g0937（1 列）
- 見出し：End Date
- 例1 値：2019-06-12 | 2020-01-31 | 2020-03-01 | 2020-03-31 | 2020-03-01
  - 同じ表の列：BN, FPE, Form ID, #, Position, At Arm's Length, Start Date

## g0938（1 列）
- 見出し：departmental_identification_number
- 例1 値：OI-755 | OI-528 | OI-1118 | OI-1118 | OI-960
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0939（1 列）
- 見出し：title_translated_en
- 例1 値：Notice to Importers Beef and Veal (Item… | Year To Date Beef and Veal Tariff Rate … | Notice to Importers Beef and Veal (Item… | Year To Date Beef and Veal Tariff Rate … | Year-to-Date Beef and Veal Tariff Rate …
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0940（1 列）
- 見出し：title_translated_fr
- 例1 値：Liste des détenteurs de contingent de b… | Avis aux importateurs : Boeuf et Veau (… | Avis aux importateurs : Boeuf et Veau (… | Résumé annuel du contingent tarifaire d… | Résumé Annuel du Contingent Tarifaire D…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0941（1 列）
- 見出し：notes_translated_en
- 例1 値：Beef and veal TRQ: Returns and Re-alloc… | Beef and Veal (Items 114 to 116 on the … | Beef and Veal Quota Holders List | Beef Global Import Prices. | Import quota reports for beef and veal.
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0942（1 列）
- 見出し：notes_translated_fr
- 例1 値：RÉSUMÉ ANNUEL DU CONTINGENT TARIFAIRE D… | Boeuf et Veau (Articles 114 à 116 de la… | Liste des détenteurs de contingent de b… | Liste des détenteurs de contingent de b… | RÉSUMÉ ANNUEL DU CONTINGENT TARIFAIRE D…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0943（1 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0944（1 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0945（1 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0946（1 列）
- 見出し：date_published
- 例1 値：2023-01-02 | 2012-10-29 | 2012-04-23 | 2014-06-09 | 2018-01-10
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0947（1 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0948（1 列）
- 見出し：t1benefityear
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：t1benefitquarter, t1incomeyear, t1income_from, t1income_to, t1gistotal, t1gistotalwithoas65, t1gistotalwithoas75

## g0949（1 列）
- 見出し：t1benefitquarter
- 例1 値：4 | 4 | 4 | 4 | 4
  - 同じ表の列：t1benefityear, t1incomeyear, t1income_from, t1income_to, t1gistotal, t1gistotalwithoas65, t1gistotalwithoas75

## g0950（1 列）
- 見出し：t1incomeyear
- 例1 値：2025 | 2025 | 2025 | 2025 | 2025
  - 同じ表の列：t1benefityear, t1benefitquarter, t1income_from, t1income_to, t1gistotal, t1gistotalwithoas65, t1gistotalwithoas75

## g0951（1 列）
- 見出し：t1income_from
- 例1 値：3360 | 18456 | 7568 | 1824 | 18168
  - 同じ表の列：t1benefityear, t1benefitquarter, t1incomeyear, t1income_to, t1gistotal, t1gistotalwithoas65, t1gistotalwithoas75

## g0952（1 列）
- 見出し：t1income_to
- 例1 値：3839.99 | 19679.99 | 12287.99 | 13295.99 | 16823.99
  - 同じ表の列：t1benefityear, t1benefitquarter, t1incomeyear, t1income_from, t1gistotal, t1gistotalwithoas65, t1gistotalwithoas75

## g0953（1 列）
- 見出し：t1gistotal
- 例1 値：972.9 | 228.49 | 372.49 | 762.9 | 694.9
  - 同じ表の列：t1benefityear, t1benefitquarter, t1incomeyear, t1income_from, t1income_to, t1gistotalwithoas65, t1gistotalwithoas75

## g0954（1 列）
- 見出し：t1gistotalwithoas65
- 例1 値：1038.99 | 983.99 | 1286.99 | 1125.99 | 1504.4
  - 同じ表の列：t1benefityear, t1benefitquarter, t1incomeyear, t1income_from, t1income_to, t1gistotal, t1gistotalwithoas75

## g0955（1 列）
- 見出し：t1gistotalwithoas75
- 例1 値：980.24 | 1728.65 | 1527.65 | 1613.65 | 1953.65
  - 同じ表の列：t1benefityear, t1benefitquarter, t1incomeyear, t1income_from, t1income_to, t1gistotal, t1gistotalwithoas65

## g0956（1 列）
- 見出し：Food_Code
- 例1 値：1462 | 1235 | 1647 | 918 | 712
  - 同じ表の列：Food_Source_Code, USDA_NDB_Code, CNF_Food_Group_Code

## g0957（1 列）
- 見出し：Food_Source_Code
- 例1 値：37 | 0 | 0 | 37 | 0
  - 同じ表の列：Food_Code, USDA_NDB_Code, CNF_Food_Group_Code

## g0958（1 列）
- 見出し：USDA_NDB_Code
- 例1 値：01105 | 07952 | 05122 | 06046 | 06486
  - 同じ表の列：Food_Code, Food_Source_Code, CNF_Food_Group_Code

## g0959（1 列）
- 見出し：CNF_Food_Group_Code
- 例1 値：9 | 5 | 8 | 9 | 8
  - 同じ表の列：Food_Code, Food_Source_Code, USDA_NDB_Code

## g0960（1 列）
- 見出し：Table
- 例1 値：1 | 10 | 24 | 7 | 11
  - 同じ表の列：Title, Survey Question, Notes

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
