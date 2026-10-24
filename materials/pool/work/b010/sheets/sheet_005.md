# ラベル用シート 005 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：GIS_SYSTEM_STATUS
- 例1 値：INST | INST | INST | INST | INST
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0482（1 列）
- 見出し：ROAD_EDGE_TYPE
- 例1 値：GCCC TYPE D | GCCC TYPE J | GCCC TYPE D | GCCC TYPE D | GCCC TYPE D
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0483（1 列）
- 見出し：LENGTH_M
- 例1 値：222.50 | 10.00 | 11.50 | 21.40 | 41.50
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0484（1 列）
- 見出し：GIS_ACQUISITION_METHOD
- 例1 値：UN | CAPEX | CONTR | UN | UN
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_STARTUP_DATE

## g0485（1 列）
- 見出し：GIS_STARTUP_DATE
- 例1 値：1/01/2006 | 1/07/2014 | 1/04/1991 | 27/07/2004 | 1/04/1988
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…

## g0486（1 列）
- 見出し：GIS_ASSET_FUNDING_BASIS
- 例1 値：GCCC | GCCC | UN | UN | UN
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…

## g0487（1 列）
- 見出し：COGG
- 例1 値：N | Y | Y | Y | Y
  - 同じ表の列：long, lat

## g0488（6 列）
- 見出し：long
- 例1 値：144.409775974068 | 144.570301138948 | 144.653065831432 | 144.333464957468 | 144.360634475684
  - 同じ表の列：COGG, lat
- 例2 値：145.242 | 145.7 | 145.1953 | 145.4175 | 145.5519
  - 同じ表の列：lat, type, open_hrs, holiday, id

## g0489（13 列）
- 見出し：lat
- 例1 値：-38.1399536902179 | -38.2083447502281 | -38.0219788308422 | -38.1711275380729 | -38.266798901929
  - 同じ表の列：COGG, long
- 例2 値：-38.23145770138689 | -38.48358482055354 | -37.68464591689836 | -38.61927112427135 | -37.95379409146786
  - 同じ表の列：suburb, assetType, lon, fme_feature_type

## g0490（1 列）
- 見出し：Heritage_Type
- 例1 値：Local Heritage Item | Local Heritage Item | Local Heritage Item | Local Heritage Item | Local Heritage Item
  - 同じ表の列：Ward

## g0491（1 列）
- 見出し：Ward
- 例1 値：01 Wine Coast | 05 Thalassa | 01 Wine Coast | 01 Wine Coast | 01 Wine Coast
  - 同じ表の列：Heritage_Type

## g0492（1 列）
- 見出し：Request Type
- 例1 値：DRFOLA - Dumped Rubbish - Footpaths & L… | DRFOLA - Dumped Rubbish - Footpaths & L… | DRFOLA - Dumped Rubbish - Footpaths & L… | DRFOLA - Dumped Rubbish - Footpaths & L… | DRFOLA - Dumped Rubbish - Footpaths & L…
  - 同じ表の列：Financial Year, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0493（1 列）
- 見出し：Financial Year
- 例1 値：2013/2014 | 2013/2014 | 2012/2013 | 2016/2017 | 2014/2015
  - 同じ表の列：Request Type, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0494（2 列）
- 見出し：Month
- 例1 値：October | July | May | March | July
  - 同じ表の列：Request Type, Financial Year, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…
- 例2 値：November | March | December | December | September
  - 同じ表の列：Year, Births, Deaths, Marriages

## g0495（1 列）
- 見出し：MonthYear
- 例1 値：Dec-2012 | Feb-2013 | Nov-2014 | Sep-2011 | May-2012
  - 同じ表の列：Request Type, Financial Year, Month, CalendarYear, Suburb, NumberOfRequests_Re…

## g0496（1 列）
- 見出し：CalendarYear
- 例1 値：CY 2014 | CY 2012 | CY 2013 | CY 2012 | CY 2016
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, Suburb, NumberOfRequests_Re…

## g0497（9 列）
- 見出し：Suburb
- 例1 値：MIDDLE PARK | SOUTH MELBOURNE | MIDDLE PARK | RIPPONLEA | PORT MELBOURNE
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, NumberOfRequests_Re…
- 例2 値：Lismore | Berrybank | Skipton | Port Campbell | Simpson
  - 同じ表の列：assetType, lon, lat, fme_feature_type

## g0498（1 列）
- 見出し：NumberOfRequests_Received
- 例1 値：30 | 26 | 1 | 5 | 3
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, Suburb

## g0499（1 列）
- 見出し：date_captured
- 例1 値：2017-May | 2015-Dec | 2017-Feb | 2019-Apr | 2016-Jun
  - 同じ表の列：section_start, section_end, message

## g0500（1 列）
- 見出し：section_start
- 例1 値：Murphy Street | Garton Street - Wilson Street | Barkly Street | Ramsden Street | Gore Street
  - 同じ表の列：date_captured, section_end, message

## g0501（1 列）
- 見出し：section_end
- 例1 値：Como Street | Palmer Street | St Bernards Road | Stawell Street | Johnston Street
  - 同じ表の列：date_captured, section_start, message

## g0502（1 列）
- 見出し：message
- 例1 値：Standard speed radar message | Speed limit message 40KM | Standard speed radar message | Standard speed radar message | Standard speed radar message
  - 同じ表の列：date_captured, section_start, section_end

## g0503（1 列）
- 見出し：Tree_ID
- 例1 値：7820 | 7365 | 9663 | 8839 | 6592
  - 同じ表の列：Genus_Desc, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0504（1 列）
- 見出し：Genus_Desc
- 例1 値：Agonis | Melaleuca | Lophostermon | Quercus | Quercus
  - 同じ表の列：Tree_ID, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0505（1 列）
- 見出し：Spec_Desc
- 例1 値：flexuosa | viminalis | robur | botriodies | eugeniodes
  - 同じ表の列：Tree_ID, Genus_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0506（1 列）
- 見出し：Location_Type
- 例1 値：Street Trees | Street Trees | Street Trees | Street Trees | Street Trees
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0507（1 列）
- 見出し：Height_m
- 例1 値：10 | 18 | 4 | 15 | 4
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Canopy_width_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0508（1 列）
- 見出し：Canopy_width_m
- 例1 値：1 | 15 | 1 | 1 | 3
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Height_m, Diam_Breast_Height_…, Year_Planted, No_Trunks

## g0509（1 列）
- 見出し：Diam_Breast_Height_mm
- 例1 値：1160 | 400 | 600 | 200 | 300
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Year_Planted, No_Trunks

## g0510（1 列）
- 見出し：Year_Planted
- 例1 値：1980 | 1980 | 1975 | 1970 | 2006
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, No_Trunks

## g0511（1 列）
- 見出し：No_Trunks
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted

## g0512（1 列）
- 見出し：Life_stage_desc
- 例1 値：Semi-Mature | Semi-Mature | Young | Semi-Mature | Semi-Mature
  - 同じ表の列：Tree_ID, Genus_Desc, Spec_Desc, Location_Type, Height_m, Canopy_width_m, Diam_Breast_Height_…, Year_Planted

## g0513（1 列）
- 見出し：Type
- 例1 値：Investigations | Compliance assistance site visits | Businesses engaged through the Better B… | Inspections | Market monitoring activity
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0514（1 列）
- 見出し：2012-13
- 例1 値：573 | 2,702 | N/A | N/A | 4,434
  - 同じ表の列：Type, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0515（2 列）
- 見出し：2013-14
- 例1 値：610 | 51 | 895 | 2,713 | 4,671
  - 同じ表の列：Type, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19
- 例2 値：66,673 | 177 | 176,356 | 9,582
  - 同じ表の列：Road Safety, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20

## g0516（2 列）
- 見出し：2014-15
- 例1 値：3,470 | 161 | 80 | 4,433 | 802
  - 同じ表の列：Type, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19
- 例2 値：12,233 | 182,108 | 75,674 | 2
  - 同じ表の列：Road Safety, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20

## g0517（1 列）
- 見出し：2015-16
- 例1 値：960 | 152 | 68 | N/A | 5,796
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19

## g0518（1 列）
- 見出し：2016-17
- 例1 値：105 | 5,769 | N/A | 411 | 42
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19

## g0519（1 列）
- 見出し：2017-18
- 例1 値：71 | 5,972 | N/A | 46 | 456
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19

## g0520（1 列）
- 見出し：2018-19
- 例1 値：27 | 4,324 | N/A | N/A | 90
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g0521（2 列）
- 見出し：assetType
- 例1 値：Toilet Block | Toilet Block | Toilet Block | Toilet Block | Toilet Block
  - 同じ表の列：suburb, lon, lat, fme_feature_type
- 例2 値：Transfer Station | Transfer Station | Transfer Station | Transfer Station | Transfer Station
  - 同じ表の列：suburb, lon, lat, fme_feature_type

## g0522（4 列）
- 見出し：lon
- 例1 値：143.34407639999998 | 143.14402152 | 142.91885304000002 | 143.07703092000003 | 142.92732384
  - 同じ表の列：suburb, assetType, lat, fme_feature_type
- 例2 値：143.344824 | 143.532818 | 143.555493 | 143.560907 | 143.532794
  - 同じ表の列：id, lat

## g0523（2 列）
- 見出し：fme_feature_type
- 例1 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat
- 例2 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat

## g0524（1 列）
- 見出し：field_id
- 例1 値：state | primary_anzsic_class_name | public_statement | air_total_emission_kg | transfer_estimation_technique
  - 同じ表の列：type, index

## g0525（5 列）
- 見出し：type
- 例1 値：text | int | text | float | text
  - 同じ表の列：field_id, index
- 例2 値：club | club | club | club | club
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Filter Category, SA2 Band, Subject to Cap, LGA

## g0526（1 列）
- 見出し：index
- 例1 値：Index | Primary Key | Index | Index | Primary Key
  - 同じ表の列：field_id, type

## g0527（1 列）
- 見出し：Reporting_Year
- 例1 値：2018 | 2017 | 2023 | 2013 | 2023
  - 同じ表の列：Year_Level, Suspension_Incidents, Exclusion_Incidents, Expulsion_Incidents

## g0528（1 列）
- 見出し：Year_Level
- 例1 値：Year 2 | Reception | Year 2 | Year 4 | Year 12
  - 同じ表の列：Reporting_Year, Suspension_Incidents, Exclusion_Incidents, Expulsion_Incidents

## g0529（1 列）
- 見出し：Suspension_Incidents
- 例1 値：879 | 1115 | 632 | 149 | 615
  - 同じ表の列：Reporting_Year, Year_Level, Exclusion_Incidents, Expulsion_Incidents

## g0530（1 列）
- 見出し：Exclusion_Incidents
- 例1 値：22 | 7 | 22 | 27 | 9
  - 同じ表の列：Reporting_Year, Year_Level, Suspension_Incidents, Expulsion_Incidents

## g0531（1 列）
- 見出し：Expulsion_Incidents
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Reporting_Year, Year_Level, Suspension_Incidents, Exclusion_Incidents

## g0532（1 列）
- 見出し：IBRA Region Code
- 例1 値：GVD | BHC | CHC | RIV | BHC
  - 同じ表の列：IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0533（1 列）
- 見出し：IBRA Region (hectares)
- 例1 値：7325140.456 | 6095894.865 | 6587005.49 | 30640355.87 | 5608888.692
  - 同じ表の列：IBRA Region Code, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0534（1 列）
- 見出し：IBRA Region in SA (Percent)
- 例1 値：28 | 26 | 28 | 28 | 48
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0535（1 列）
- 見出し：IBRA Region Protected (Percent)
- 例1 値：4.691 | 5.855 | 42.981 | 10.957 | 55.16
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0536（1 列）
- 見出し：IBRA Subregion Code
- 例1 値：BHC04 | NCP04 | RIV05 | MDD01 | FLB03
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0537（1 列）
- 見出し：IBRA Subregion (hectares)
- 例1 値：708021.3436 | 13102605.6 | 957067.0623 | 1168056.89 | 1030410.288
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion in S…, IBRA Subregion Prot…, Geographic CARRS As…

## g0538（1 列）
- 見出し：IBRA Subregion in SA (percent)
- 例1 値：100 | 25 | 0 | 100 | 0
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion Prot…, Geographic CARRS As…

## g0539（1 列）
- 見出し：IBRA Subregion Protected (percent)
- 例1 値：2.341 | 0.993 | 3.301 | 6.919 | 5.46
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, Geographic CARRS As…

## g0540（1 列）
- 見出し：Geographic CARRS Assessment
- 例1 値：High Priority | Not a Priority | Not a Priority | Not a Priority | Priority
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…

## g0541（1 列）
- 見出し：Outcome CARRS Assessment
- 例1 値：Not Assessed | Not Assessed | Not Assessed | Priority | Not Assessed
  - 同じ表の列：IBRA Region Code, IBRA Region (hectar…, IBRA Region in SA (…, IBRA Region Protect…, IBRA Subregion Code, IBRA Subregion (hec…, IBRA Subregion in S…, IBRA Subregion Prot…

## g0542（1 列）
- 見出し：suburb_num
- 例1 値：522304 | 521401 | 531108 | 533001 | 517102
  - 同じ表の列：suburb, legalstart, shape_Leng, shape_Area

## g0543（1 列）
- 見出し：legalstart
- 例1 値：23/07/1992 | 5/08/1999 | 11/10/1990 | 31/08/2000 | 12/08/1993
  - 同じ表の列：suburb, suburb_num, shape_Leng, shape_Area

## g0544（1 列）
- 見出し：shape_Leng
- 例1 値：0.108580336821482 | 0.077222947379124 | 0.814403809358922 | 0.308301015651142 | 0.059684960774905
  - 同じ表の列：suburb, suburb_num, legalstart, shape_Area

## g0545（1 列）
- 見出し：shape_Area
- 例1 値：0.007496458907831 | 0.008978542839186 | 0.000413295706300 | 0.002726790021266 | 0.002885729995838
  - 同じ表の列：suburb, suburb_num, legalstart, shape_Leng

## g0546（1 列）
- 見出し：Age
- 例1 値：22 | 22 | 57 | 75 | 58
  - 同じ表の列：Sex, Total

## g0547（2 列）
- 見出し：Sex
- 例1 値：Male | Female | Male | Female | Not listed
  - 同じ表の列：Age, Total
- 例2 値：Male | Both sexes | Female | Male | Male
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C03111V03761, Type of Driving Lic…, C03110V03760

## g0548（1 列）
- 見出し：city
- 例1 値：Brisbane | Sydney | North Sydney | Brisbane | Canberra
  - 同じ表の列：state, poa, country, year_founded, company_type, company_category, revenue_source, business_model

## g0549（1 列）
- 見出し：poa
- 例1 値：2000 | 7001 | 4110 | 3000 | 2000
  - 同じ表の列：city, state, country, year_founded, company_type, company_category, revenue_source, business_model

## g0550（1 列）
- 見出し：year_founded
- 例1 値：1945 | 2002 | 2007 | 2009 | 2009
  - 同じ表の列：city, state, poa, country, company_type, company_category, revenue_source, business_model

## g0551（1 列）
- 見出し：company_type
- 例1 値：Private | Private | Public | Private | Public
  - 同じ表の列：city, state, poa, country, year_founded, company_category, revenue_source, business_model

## g0552（1 列）
- 見出し：company_category
- 例1 値：Data/Technology | Research & Consulting | Mining/Manufacturing | Construction | Data/Technology
  - 同じ表の列：city, state, poa, country, year_founded, company_type, revenue_source, business_model

## g0553（1 列）
- 見出し：revenue_source
- 例1 値：Consulting, Government contract, Manage… | Database licensing, Subscriptions | Government contract, Manufacture of ele… | Consulting, Data analysis for clients, … | Contributions/Donations, Government con…
  - 同じ表の列：city, state, poa, country, year_founded, company_type, company_category, business_model

## g0554（1 列）
- 見出し：business_model
- 例1 値：Business to Business | Organisation to community | Business to Business, Business to Consu… | Business to Business, Business to Gover… | Business to Business, Business to Gover…
  - 同じ表の列：city, state, poa, country, year_founded, company_type, company_category, revenue_source

## g0555（1 列）
- 見出し：social_impact
- 例1 値：Citizen engagement and participation, E… | Citizen engagement and participation, C… | Citizen engagement and participation | Public safety | Citizen engagement and participation, C…
  - 同じ表の列：city, state, poa, country, year_founded, company_type, company_category, revenue_source

## g0556（1 列）
- 見出し：Data as of
- 例1 値：11-Apr-21 | 11-Apr-21 | 11-Apr-21 | 11-Apr-21 | 11-Apr-21
  - 同じ表の列：Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0557（1 列）
- 見出し：Licence No
- 例1 値：LIQC300239527 | LIQC300236145 | LIQC300236447 | LIQC300242056 | LIQC300235971
  - 同じ表の列：Data as of, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0558（1 列）
- 見出し：Start Date
- 例1 値：12/06/1957 | 13/02/1959 | 7/07/1947 | 6/07/1955 | 8/03/1972
  - 同じ表の列：Data as of, Licence No, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0559（1 列）
- 見出し：Trading Status
- 例1 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Data as of, Licence No, Start Date, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0560（1 列）
- 見出し：Filter Category
- 例1 値：Club - non gaming | Club - medium | Club - medium | Club - non gaming | Club - small
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, SA2 Band, Subject to Cap, LGA

## g0561（1 列）
- 見出し：SA2 Band
- 例1 値：1 | 2 | 3 | 1 | 2
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Subject to Cap, LGA

## g0562（1 列）
- 見出し：Subject to Cap
- 例1 値：No | Yes | No | Yes | No
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, LGA

## g0563（1 列）
- 見出し：LGA
- 例1 値：Glen Innes Severn Council | The Council of the Shire of Hornsby | Queanbeyan-Palerang Regional Council | Central Coast Council | Northern Beaches Council
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0564（2 列）
- 見出し：Region
- 例1 値：Metropolitan | Country | Country | Metropolitan | Metropolitan
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap
- 例2 値：Dublin | Southern | Southern | Dublin | Eastern
  - 同じ表の列：county, circuit, district_number, court_house, court_house_eircode, active_status

## g0565（1 列）
- 見出し：Portfolio
- 例1 値：Infra, Transport, Regional Developt, Co… | Industry, Science and Resources | Home Affairs | Defence | Social Services
  - 同じ表の列：Outcome, Program, Expense_type, Appropriation_type, 2024-25, 2025-26, 2026-27, 2027-28

## g0566（1 列）
- 見出し：Outcome
- 例1 値：Outcome 1: Provide high quality policy … | Outcome 4: Good governance and service … | Outcome 1: More sustainable, productive… | Outcome 2: Support an efficient and hig… | Outcome 2: Promote growth in economic p…
  - 同じ表の列：Portfolio, Program, Expense_type, Appropriation_type, 2024-25, 2025-26, 2026-27, 2027-28

## g0567（1 列）
- 見出し：Program
- 例1 値：Program 1.1: Employment Services | Program 1.1: Federal Court of Australia | Program 1.2: Australian Government Disa… | Program 1.11: Drought Programs | Program 1.1: National Health Funding Po…
  - 同じ表の列：Portfolio, Outcome, Expense_type, Appropriation_type, 2024-25, 2025-26, 2026-27, 2027-28

## g0568（1 列）
- 見出し：Expense_type
- 例1 値：Administered Expenses | Departmental Expenses | Departmental Expenses | Administered Expenses | Departmental Expenses
  - 同じ表の列：Portfolio, Outcome, Program, Appropriation_type, 2024-25, 2025-26, 2026-27, 2027-28

## g0569（1 列）
- 見出し：Appropriation_type
- 例1 値：Revenues from other independent sources | Refundable Accommodation Deposit Conces… | Revenues from other sources | Departmental appropriation | s74 External Revenue
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, 2024-25, 2025-26, 2026-27, 2027-28

## g0570（1 列）
- 見出し：2024-25
- 例1 値：47983 | -439 | 66268 | 2455 | 21292
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, Appropriation_type, 2025-26, 2026-27, 2027-28

## g0571（1 列）
- 見出し：2025-26
- 例1 値：216860 | 252481 | 14674 | 2452 | 700787
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, Appropriation_type, 2024-25, 2026-27, 2027-28

## g0572（1 列）
- 見出し：2026-27
- 例1 値：20617 | 266760 | 18986 | 0 | 19
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, Appropriation_type, 2024-25, 2025-26, 2027-28

## g0573（1 列）
- 見出し：2027-28
- 例1 値：7717 | 773054 | 16529 | 0 | 406418
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, Appropriation_type, 2024-25, 2025-26, 2026-27

## g0574（1 列）
- 見出し：2028-29
- 例1 値：37669 | 0 | 1800 | 0 | 229088
  - 同じ表の列：Portfolio, Outcome, Program, Expense_type, Appropriation_type, 2024-25, 2025-26, 2026-27

## g0575（1 列）
- 見出し：Q8
- 例1 値：8 | 20 | 1 | 6 | 7
  - 同じ表の列：Year, Q17aiv, Q20, Q20dii, Q22, Q28, Q24, Q26a

## g0576（1 列）
- 見出し：Q17aiv
- 例1 値：6 | 0 | 1 | 0 | 1
  - 同じ表の列：Year, Q8, Q20, Q20dii, Q22, Q28, Q24, Q26a

## g0577（1 列）
- 見出し：Q20
- 例1 値：0 | 12 | 279 | 1 | 0
  - 同じ表の列：Year, Q8, Q17aiv, Q20dii, Q22, Q28, Q24, Q26a

## g0578（1 列）
- 見出し：Q20dii
- 例1 値：$4,469,659.00 | $6,035,745.00 | $634,684.00 | $129,918.00 | $504,390.00
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q22, Q28, Q24, Q26a

## g0579（1 列）
- 見出し：Q22
- 例1 値：$138,472.00 | $28,762.00 | $0.00 | $0.00 | $0.00
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q20dii, Q28, Q24, Q26a

## g0580（1 列）
- 見出し：Q28
- 例1 値：1 | 0 | 0 | 2 | 4
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q20dii, Q22, Q24, Q26a

## g0581（1 列）
- 見出し：Q24
- 例1 値：$20,000.00 | $0.00 | $3,039,156.00 | $1,341,000.00 | $420,000.00
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q20dii, Q22, Q28, Q26a

## g0582（1 列）
- 見出し：Q26a
- 例1 値：1 | 0 | 1 | 0 | 3
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q20dii, Q22, Q28, Q24

## g0583（1 列）
- 見出し：Q26b
- 例1 値：5 | 5 | 4 | 8 | 0
  - 同じ表の列：Year, Q8, Q17aiv, Q20, Q20dii, Q22, Q28, Q24

## g0584（2 列）
- 見出し：Year
- 例1 値：2016/17 | 2012/13 | 2012/13 | 2012/13 | 2015/16
  - 同じ表の列：Purpose, $'000
- 例2 値：2014/15 | 2012/13 | 2014/15 | 2012/13 | 2013/14
  - 同じ表の列：Executive Classific…, Number of Executives

## g0585（1 列）
- 見出し：Purpose
- 例1 値：Review of South Australian Research and… | Consultancy services for the review of … | Advisory Group Services for SARDI Review | Strategic Advice | Review of the Gulf of St Vincent Prawn …
  - 同じ表の列：Year, $'000

## g0586（1 列）
- 見出し：$'000
- 例1 値：14 | 1 | 37 | 4 | 17
  - 同じ表の列：Year, Purpose

## g0587（1 列）
- 見出し：CD_MAKE_VEH
- 例1 値：G M C | GAC | B Y D | G WALL | AUDI
  - 同じ表の列：CD_MODEL_VEH, CD_CLR_BDY_VEH_P, NB_YEAR_MFC_VEH, TOTAL

## g0588（1 列）
- 見出し：CD_MODEL_VEH
- 例1 値：X3 M50 | SILVER | Q2 | C5 URB | 700MT
  - 同じ表の列：CD_MAKE_VEH, CD_CLR_BDY_VEH_P, NB_YEAR_MFC_VEH, TOTAL

## g0589（2 列）
- 見出し：CD_CLR_BDY_VEH_P
- 例1 値：GRY | WHI | SIL | WHI | BLU
  - 同じ表の列：CD_MAKE_VEH, CD_MODEL_VEH, NB_YEAR_MFC_VEH, TOTAL
- 例2 値：BLU | GRY | SIL | WHI | WHI
  - 同じ表の列：CD_MAKE_VEH1, CD_MODEL_VEH, NB_YEAR_MFC_VEH, TOTAL1

## g0590（2 列）
- 見出し：NB_YEAR_MFC_VEH
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：CD_MAKE_VEH, CD_MODEL_VEH, CD_CLR_BDY_VEH_P, TOTAL
- 例2 値：2002 | 2013 | 2017 | 2023 | 2018
  - 同じ表の列：CD_MAKE_VEH1, CD_MODEL_VEH, CD_CLR_BDY_VEH_P, TOTAL1

## g0591（4 列）
- 見出し：Year
- 例1 値：2006-07 | 2006-07 | 2006-07 | 2006-07 | 2006-07
  - 同じ表の列：Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3, APEC
- 例2 値：2024-25 | 2017-18 | 2017-18 | 2018-19 | 2017-18
  - 同じ表の列：Contractor, Purpose, Value

## g0592（2 列）
- 見出し：Trade type
- 例1 値：Total Exports | Total Exports | Total Exports | Total Exports | Total Exports
  - 同じ表の列：Year, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3, APEC
- 例2 値：Total Exports | Total Exports | Total Exports | Total Exports | Total Exports
  - 同じ表の列：Year, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3, APEC

## g0593（1 列）
- 見出し：Sitc 3 digit
- 例1 値：047 Other cereal flours | 046 Wheat flour | 056 Vegetables, prepared or preserved | 024 Cheese & curd | 061 Sugars, molasses & honey
  - 同じ表の列：Year, Trade type, State, Partner country, Geographic level 1, Geographic level 2, Geographic level 3, APEC

## g0594（2 列）
- 見出し：Partner country
- 例1 値：China | United Kingdom | Jordan | India | United Kingdom
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Geographic level 1, Geographic level 2, Geographic level 3, APEC
- 例2 値：Japan | Norway | New Zealand | Spain | Thailand
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Geographic level 1, Geographic level 2, Geographic level 3, APEC

## g0595（1 列）
- 見出し：Geographic level 1
- 例1 値：Africa | Asia | Oceania & Antarctica | Oceania & Antarctica | Oceania & Antarctica
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 2, Geographic level 3, APEC

## g0596（2 列）
- 見出し：Geographic level 2
- 例1 値：Pacific Islands | Pacific Islands | Northern & Western Europe | Pacific Islands | Pacific Islands
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 3, APEC
- 例2 値：Middle East | Eastern & Southern Europe | East Asia | East Asia | East Asia
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 3, APEC

## g0597（1 列）
- 見出し：Geographic level 3
- 例1 値：South East Asia | South East Asia | Eastern Europe | Pacific Island Forum Countries | Eastern Europe
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, APEC

## g0598（2 列）
- 見出し：APEC
- 例1 値：Non-APEC | Non-APEC | Non-APEC | APEC | APEC
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3
- 例2 値：Non-APEC | Non-APEC | Non-APEC | Non-APEC | APEC
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3

## g0599（2 列）
- 見出し：ASEAN
- 例1 値：Non-ASEAN | Non-ASEAN | Non-ASEAN | ASEAN | Non-ASEAN
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3
- 例2 値：Non-ASEAN | Non-ASEAN | Non-ASEAN | ASEAN | Non-ASEAN
  - 同じ表の列：Year, Trade type, State, Sitc 3 digit, Partner country, Geographic level 1, Geographic level 2, Geographic level 3

## g0600（1 列）
- 見出し：Region
- 例1 値：6 | 10 | 8 | 6 | 12
  - 同じ表の列：Suburb, P/C, Business Ph, Category

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
