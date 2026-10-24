# ラベル用シート 003 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：GEAR
- 例1 値：Trawl | Hooks | Trawl | Hooks | Hooks
  - 同じ表の列：FISHERY, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

## g0242（1 列）
- 見出し：BOATS
- 例1 値：4 | 3 | 46 | 2 | 2
  - 同じ表の列：FISHERY, GEAR, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

## g0243（1 列）
- 見出し：NUMBER_OF_SHOTS
- 例1 値：60 | 28870 | 6592 | 209 | 35
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

## g0244（1 列）
- 見出し：HOURS_TRAWLED
- 例1 値：1527 | 16878 | 23383 | 9 | 69232
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_FISHED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

## g0245（1 列）
- 見出し：HOURS_FISHED
- 例1 値：2234 | 8836 | 40 | 911 | 174
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

## g0246（1 列）
- 見出し：NUMBER_OF_HOOKS
- 例1 値：1 | 223728 | 101781 | 6 | 737711
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, LENGTH_OF_GILLNET

## g0247（1 列）
- 見出し：LENGTH_OF_GILLNET
- 例1 値：44232460 | 7400 | 32483878 | 6000 | 2400
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS

## g0248（1 列）
- 見出し：HOURS_SEARCHED
- 例1 値：187 | 26648 | 29745 | 404 | 2621
  - 同じ表の列：FISHERY, GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS

## g0249（1 列）
- 見出し：Date-Time
- 例1 値：2007-05-23 10:05:00 | 2007-05-23 11:15:00 | 2007-05-23 00:15:00 | 2007-05-23 12:40:00 | 2007-05-23 03:45:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0250（1 列）
- 見出し：UV_Index
- 例1 値：00.00 | 05.47 | 06.73 | 00.00 | 00.57
  - 同じ表の列：Date-Time, Lat, Lon

## g0251（4 列）
- 見出し：number
- 例1 値：101 | 169 | 103 | 102 | 168
  - 同じ表の列：type, area
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year

## g0252（1 列）
- 見出し：area
- 例1 値：1.02 | 0.28 | 2.17 | 10.22 | 0.000885
  - 同じ表の列：type, number

## g0253（1 列）
- 見出し：Question
- 例1 値：5 | 20 | 17 | 3 | 21
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0254（1 列）
- 見出し：Question_Text
- 例1 値：The government should further restrict … | When there is an economic problem gover… | Asylum seekers who arrive by boat shoul… | How much tax should mining companies pa… | The National Broadband Network should d…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0255（1 列）
- 見出し：category1_definition_1
- 例1 値：Much Less | Much Less | Strongly disagree | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0256（1 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0257（1 列）
- 見出し：category1_definition_3
- 例1 値：About the same as now | Neutral | Neutral | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0258（1 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0259（1 列）
- 見出し：category1_definition_5
- 例1 値：Strongly agree | Strongly agree | Much more | Strongly agree | Many more
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0260（1 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0261（1 列）
- 見出し：Taxation statistics 2023-24
- 例1 値：Table 1A | 1 | Notes: | * | *
  - 同じ表の列：None

## g0262（1 列）
- 見出し：None
- 例1 値：Selected items, for income years 1990–9… | Totals may not equal the sum of compone… | Selected counts, totals, means and medi… | The statistics in table 2B were sourced… | To meet privacy regulations, some items…
  - 同じ表の列：Taxation statistics…

## g0263（1 列）
- 見出し：AIRPORT
- 例1 値：ALICE SPRINGS | ADELAIDE | BALLINA | ADELAIDE | ALICE SPRINGS
  - 同じ表の列：Year, Month, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out, Int_Pax_Total

## g0264（1 列）
- 見出し：Month
- 例1 値：7 | 10 | 1 | 5 | 1
  - 同じ表の列：AIRPORT, Year, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out, Int_Pax_Total

## g0265（1 列）
- 見出し：Dom_Pax_In
- 例1 値：284112 | 291320 | 152690 | 2062 | 30596
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out, Int_Pax_Total

## g0266（1 列）
- 見出し：Dom_Pax_Out
- 例1 値：33329 | 4097 | 22001 | 304558 | 21309
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out, Int_Pax_Total

## g0267（1 列）
- 見出し：Dom_Pax_Total
- 例1 値：42984 | 185858 | 200390 | 58871 | 164174
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Out, Int_Pax_In, Int_Pax_Out, Int_Pax_Total

## g0268（1 列）
- 見出し：Int_Pax_In
- 例1 値：0 | 42945 | 0 | 0 | 0
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_Out, Int_Pax_Total

## g0269（1 列）
- 見出し：Int_Pax_Out
- 例1 値：22938 | 25253 | 11101 | 0 | 22970
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Total

## g0270（1 列）
- 見出し：Int_Pax_Total
- 例1 値：36470 | 0 | 17416 | 70810 | 0
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out

## g0271（1 列）
- 見出し：Pax_In
- 例1 値：317059 | 2259 | 92259 | 28897 | 199298
  - 同じ表の列：AIRPORT, Year, Month, Dom_Pax_In, Dom_Pax_Out, Dom_Pax_Total, Int_Pax_In, Int_Pax_Out

## g0272（1 列）
- 見出し：CouncilID
- 例1 値：8 | 11 | 5 | 9 | 3
  - 同じ表の列：Centre, Lat, Long

## g0273（1 列）
- 見出し：Centre
- 例1 値：Mechanics Institute | Mining Exchange | Eureka Centre | Caro Convention Centre - Ballarat Unive… | Ballarat Fine Art Gallery
  - 同じ表の列：CouncilID, Lat, Long

## g0274（3 列）
- 見出し：Long
- 例1 値：143.841438 | 143.891124 | 143.858528 | 143.870762 | 143.859456
  - 同じ表の列：CouncilID, Centre, Lat
- 例2 値：151.59571 | 152.420375 | 149.2916666 | 148.3916666 | 153.0932585
  - 同じ表の列：id, lat, project_type, location, lga, cwlth_state_funding, project_status, recovery_type

## g0275（1 列）
- 見出し：Feature
- 例1 値：Bike Rack | Bike Rack | Bike Rack | Bike Rack | Bike Rack
  - 同じ表の列：X, Y

## g0276（5 列）
- 見出し：OBJECTID
- 例1 値：203 | 437 | 221 | 273 | 477
  - 同じ表の列：SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM
- 例2 値：14 | 4 | 25 | 20 | 8
  - 同じ表の列：PubliclyOp, universall, dlr, AgeGroup

## g0277（1 列）
- 見出し：SAPOBJECTI
- 例1 値：9000042027 | 9000296183 | 9000105583 | 9000030738 | 9000295176
  - 同じ表の列：OBJECTID, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM

## g0278（1 列）
- 見出し：CLASS
- 例1 値：PIPE_NON_PRESSURE | PIPE_NON_PRESSURE | PIPE_NON_PRESSURE | PIPE_NON_PRESSURE | PIPE_NON_PRESSURE
  - 同じ表の列：OBJECTID, SAPOBJECTI, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM

## g0279（1 列）
- 見出し：PIPE_USE
- 例1 値：RETICULATION | RETICULATION | TRUNK | RETICULATION | RETICULATION
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM

## g0280（1 列）
- 見出し：PIPE_CLASS
- 例1 値：35 | TBA | TBA | SN8 | SN8
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM

## g0281（1 列）
- 見出し：PIPE_MATERIAL
- 例1 値：AC | PVC-U | PVC-U | AC | AC
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_LINING, PIPE_PROTECTION, DIAMETER_MM

## g0282（1 列）
- 見出し：PIPE_LINING
- 例1 値：TBA | TBA | UNLINED | TBA | TBA
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_PROTECTION, DIAMETER_MM

## g0283（1 列）
- 見出し：PIPE_PROTECTION
- 例1 値：TBA | TBA | TBA | UNCOATED | TBA
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, DIAMETER_MM

## g0284（1 列）
- 見出し：DIAMETER_MM
- 例1 値：150.0 | 150.0 | 150.0 | 150.0 | 150.0
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION

## g0285（1 列）
- 見出し：UPSTREAM_INVERT_LEVEL
- 例1 値：3.38 | 0.42 | 14.23 | 3.49 | 10.08
  - 同じ表の列：OBJECTID, SAPOBJECTI, CLASS, PIPE_USE, PIPE_CLASS, PIPE_MATERIAL, PIPE_LINING, PIPE_PROTECTION

## g0286（2 列）
- 見出し：Locality
- 例1 値：SPRINGVALE | DANDENONG NORTH | NOBLE PARK | DANDENONG NORTH | SPRINGVALE
  - 同じ表の列：Animal_Type, GENDER
- 例2 値：Murgheboluc | Grenville | Cape Clear | Meredith | Dereel
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, Home_Clubs, Amenities

## g0287（1 列）
- 見出し：Animal_Type
- 例1 値：Cat | Cat | Cat | Cat | Cat
  - 同じ表の列：Locality, GENDER

## g0288（1 列）
- 見出し：ref
- 例1 値：266662 | 266364 | 266531 | 266624 | 266782
  - 同じ表の列：lat, lon

## g0289（3 列）
- 見出し：Suburb
- 例1 値：SEAFORD RISE | OLD NOARLUNGA | MCLAREN FLAT | PORT NOARLUNGA | HUNTFIELD HEIGHTS
  - 同じ表の列：Zone, Number of Properties
- 例2 値：ANDREWS FARM | ANDREWS FARM | ANGLE VALE | ELIZABETH GROVE | MUNNO PARA
  - 同じ表の列：FROM, TO, AREA (sqm), LENGTH (m), WIDTH (m), RESERVE WIDTH (m)

## g0290（1 列）
- 見出し：Zone
- 例1 値：CSTCON | CU | HF | HF | NCe
  - 同じ表の列：Suburb, Number of Properties

## g0291（1 列）
- 見出し：Number of Properties
- 例1 値：60 | 29 | 17 | 4 | 16
  - 同じ表の列：Suburb, Zone

## g0292（1 列）
- 見出し：FROM
- 例1 値：TALLERACK | PARKVALE | NOLAN | JOHNNY | FATCHEN
  - 同じ表の列：TO, SUBURB, AREA (sqm), LENGTH (m), WIDTH (m), RESERVE WIDTH (m)

## g0293（1 列）
- 見出し：TO
- 例1 値：FAULDING | HOOLE | HENDERSON | MINGARI | BLACKBIRD
  - 同じ表の列：FROM, SUBURB, AREA (sqm), LENGTH (m), WIDTH (m), RESERVE WIDTH (m)

## g0294（1 列）
- 見出し：AREA (sqm)
- 例1 値：962.00000000 | 468.00000000 | 1394.00000000 | 743.00000000 | 526.00000000
  - 同じ表の列：FROM, TO, SUBURB, LENGTH (m), WIDTH (m), RESERVE WIDTH (m)

## g0295（1 列）
- 見出し：LENGTH (m)
- 例1 値：62.00000000 | 67.00000000 | 250.00000000 | 56.00000000 | 182.00000000
  - 同じ表の列：FROM, TO, SUBURB, AREA (sqm), WIDTH (m), RESERVE WIDTH (m)

## g0296（1 列）
- 見出し：WIDTH (m)
- 例1 値：7.00000000 | 10.00000000 | 7.00000000 | 7.00000000 | 8.00000000
  - 同じ表の列：FROM, TO, SUBURB, AREA (sqm), LENGTH (m), RESERVE WIDTH (m)

## g0297（1 列）
- 見出し：RESERVE WIDTH (m)
- 例1 値：23.00000000 | 15.00000000 | 15.00000000 | 25.00000000 | 21.00000000
  - 同じ表の列：FROM, TO, SUBURB, AREA (sqm), LENGTH (m), WIDTH (m)

## g0298（1 列）
- 見出し：Site ID
- 例1 値：5 | 50 | 5 | 5 | 5
  - 同じ表の列：Count Start, Count End, Count Topic, Tally, Max Temperature, Weather, Approach _Azimuth, Exit _Azimuth

## g0299（1 列）
- 見出し：Count Start
- 例1 値：26/Oct/2019 18:15 | 26/Oct/2019 16:30 | 26/Oct/2019 10:45 | 26/Oct/2019 14:15 | 02/Nov/2019 10:45
  - 同じ表の列：Site ID, Count End, Count Topic, Tally, Max Temperature, Weather, Approach _Azimuth, Exit _Azimuth

## g0300（1 列）
- 見出し：Count End
- 例1 値：02/Nov/2019 10:00 | 26/Oct/2019 09:45 | 26/Oct/2019 17:30 | 26/Oct/2019 13:15 | 26/Oct/2019 17:30
  - 同じ表の列：Site ID, Count Start, Count Topic, Tally, Max Temperature, Weather, Approach _Azimuth, Exit _Azimuth

## g0301（1 列）
- 見出し：Count Topic
- 例1 値：Bicycle | Bicycle | Bicycle | Bicycle | Bicycle
  - 同じ表の列：Site ID, Count Start, Count End, Tally, Max Temperature, Weather, Approach _Azimuth, Exit _Azimuth

## g0302（1 列）
- 見出し：Tally
- 例1 値：1 | 0 | 0 | 0 | 1
  - 同じ表の列：Site ID, Count Start, Count End, Count Topic, Max Temperature, Weather, Approach _Azimuth, Exit _Azimuth

## g0303（1 列）
- 見出し：Max Temperature
- 例1 値：18.9 | 15.5 | 15.5 | 15.5 | 15.5
  - 同じ表の列：Site ID, Count Start, Count End, Count Topic, Tally, Weather, Approach _Azimuth, Exit _Azimuth

## g0304（1 列）
- 見出し：Weather
- 例1 値：Rainy | Rainy | Rainy | Rainy | Rainy
  - 同じ表の列：Site ID, Count Start, Count End, Count Topic, Tally, Max Temperature, Approach _Azimuth, Exit _Azimuth

## g0305（1 列）
- 見出し：Approach _Azimuth
- 例1 値：77 | 252 | 185 | 77 | 77
  - 同じ表の列：Site ID, Count Start, Count End, Count Topic, Tally, Max Temperature, Weather, Exit _Azimuth

## g0306（1 列）
- 見出し：Exit _Azimuth
- 例1 値：340 | 185 | 340 | 252 | 77
  - 同じ表の列：Site ID, Count Start, Count End, Count Topic, Tally, Max Temperature, Weather, Approach _Azimuth

## g0307（1 列）
- 見出し：date_captured
- 例1 値：2018-Aug | 2017-May | 2013-May | 2018-Aug | 2011-Feb
  - 同じ表の列：section_start, section_end, suburb, direction_1, vehicles_1, direction_2, vehicles_2, volume_per_day

## g0308（1 列）
- 見出し：section_start
- 例1 値：Cremorne Street | Burnley Street | Princes Street | Langridge Street | Burnley Street
  - 同じ表の列：date_captured, section_end, suburb, direction_1, vehicles_1, direction_2, vehicles_2, volume_per_day

## g0309（1 列）
- 見出し：section_end
- 例1 値：Church Street | R.O.W. | freeway overpass | Gold Street | Vaughan Street
  - 同じ表の列：date_captured, section_start, suburb, direction_1, vehicles_1, direction_2, vehicles_2, volume_per_day

## g0310（1 列）
- 見出し：direction_1
- 例1 値：East/North | East/North | East/North | East/North | East/North
  - 同じ表の列：date_captured, section_start, section_end, suburb, vehicles_1, direction_2, vehicles_2, volume_per_day

## g0311（1 列）
- 見出し：vehicles_1
- 例1 値：282 | 21 | 2769 | 1113 | 5
  - 同じ表の列：date_captured, section_start, section_end, suburb, direction_1, direction_2, vehicles_2, volume_per_day

## g0312（1 列）
- 見出し：direction_2
- 例1 値：West/South | West/South | West/South | West/South | West/South
  - 同じ表の列：date_captured, section_start, section_end, suburb, direction_1, vehicles_1, vehicles_2, volume_per_day

## g0313（1 列）
- 見出し：vehicles_2
- 例1 値：5 | 177 | 4094 | 95 | 73
  - 同じ表の列：date_captured, section_start, section_end, suburb, direction_1, vehicles_1, direction_2, volume_per_day

## g0314（1 列）
- 見出し：volume_per_day
- 例1 値：749 | 243 | 1413 | 468 | 3980
  - 同じ表の列：date_captured, section_start, section_end, suburb, direction_1, vehicles_1, direction_2, vehicles_2

## g0315（1 列）
- 見出し：85th_percentile_speed
- 例1 値：46.1 | 39.6 | 26.6 | 33.8 | 52.9
  - 同じ表の列：date_captured, section_start, section_end, suburb, direction_1, vehicles_1, direction_2, vehicles_2

## g0316（1 列）
- 見出し：Type of call
- 例1 値：Building | Calls to regional offices | General consumer | Residential Tenancies Bond Authority (R… | Registrations
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0317（1 列）
- 見出し：2012-13
- 例1 値：409,936 | N/A | N/A | N/A | N/A
  - 同じ表の列：Type of call, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0318（1 列）
- 見出し：2013-14
- 例1 値：21,342 | 3,909 | 7,458 | 4,398 | 4,822
  - 同じ表の列：Type of call, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0319（1 列）
- 見出し：2014-15
- 例1 値：99,325 | 299 | 24,331 | 78,028 | 22,993
  - 同じ表の列：Type of call, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19

## g0320（1 列）
- 見出し：2015-16
- 例1 値：90,224 | 69,365 | 30,408 | 10,765 | 2,457
  - 同じ表の列：Type of call, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19

## g0321（1 列）
- 見出し：2016-17
- 例1 値：13,879 | 1,653 | 77,847 | 23,300 | N/A
  - 同じ表の列：Type of call, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19

## g0322（1 列）
- 見出し：2017-18
- 例1 値：67,813 | 304,048 | 71,378 | 27,378 | 1,489
  - 同じ表の列：Type of call, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19

## g0323（1 列）
- 見出し：2018-19
- 例1 値：64,118 | 8,942 | 9,263 | 295,955 | 22,163
  - 同じ表の列：Type of call, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g0324（2 列）
- 見出し：genus
- 例1 値：Salix | Fraxinus | Ulmus | Fraxinus | Fraxinus
  - 同じ表の列：lat, lon, species, dbh, crown, height, common, ref
- 例2 値：Melaleuca | Melaleuca | Eucalyptus | Eucalyptus | Corymbia
  - 同じ表の列：type, suburb, easting, northing, melway_ref, Species

## g0325（1 列）
- 見出し：species
- 例1 値：Eucalyptus nicholii | Ulmus procera | Ulmus procera | Fraxinus angustifolia subsp. Oxycarpa | Corymbia maculata
  - 同じ表の列：lat, lon, genus, dbh, crown, height, common, ref

## g0326（1 列）
- 見出し：dbh
- 例1 値：56 | 75 | 18 | 19 | 87
  - 同じ表の列：lat, lon, genus, species, crown, height, common, ref

## g0327（1 列）
- 見出し：crown
- 例1 値：4 | 2 | 1.5 | 6 | 1
  - 同じ表の列：lat, lon, genus, species, dbh, height, common, ref

## g0328（1 列）
- 見出し：height
- 例1 値：11 | 15 | 10 | 16 | 14
  - 同じ表の列：lat, lon, genus, species, dbh, crown, common, ref

## g0329（1 列）
- 見出し：common
- 例1 値：Sugar Gum | Manna Gum | River Red Gum | Prickly Paperbark | Dwarf Sugar Gum
  - 同じ表の列：lat, lon, genus, species, dbh, crown, height, ref

## g0330（2 列）
- 見出し：ref
- 例1 値：TR00091 | TR00732 | TR00184 | TR00384 | TR00583
  - 同じ表の列：lat, lon, genus, species, dbh, crown, height, common
- 例2 値：PE029 | PE044 | PE003 | PE006 | PE053
  - 同じ表の列：operation, size_diam

## g0331（1 列）
- 見出し：maturity
- 例1 値：Semi mature | Mature | Mature | Semi mature | Removed
  - 同じ表の列：lat, lon, genus, species, dbh, crown, height, common

## g0332（1 列）
- 見出し：Jurisdiction
- 例1 値：Higher Courts - Custodial | Magistrates Court | Higher Courts - Witness | Total | Youth Court
  - 同じ表の列：2020-21, 2021-22, 2022-23, 2023-24, 2024-25

## g0333（1 列）
- 見出し：Column
- 例1 値：TRAN | TRAN | HER | NBCS | JAG
  - 同じ表の列：Title, Wheelchair access, Suburb, State, Fax, Notes, Mon am, Mon pm

## g0334（1 列）
- 見出し：Title
- 例1 値：Barcaldine QGAP | Maroochydore QGSC | Crows Nest QGAP | Babinda QGAP | Nanango QGAP
  - 同じ表の列：Column, Wheelchair access, Suburb, State, Fax, Notes, Mon am, Mon pm

## g0335（1 列）
- 見出し：Wheelchair access
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Column, Title, Suburb, State, Fax, Notes, Mon am, Mon pm

## g0336（3 列）
- 見出し：Suburb
- 例1 値：Kandanga | Quilpie | Boonah | Stanthorpe | Mossman
  - 同じ表の列：Column, Title, Wheelchair access, State, Fax, Notes, Mon am, Mon pm
- 例2 値：ULLADULLA | CHATSWOOD | TURRAMURRA | SUTHERLAND | ROBERTSON
  - 同じ表の列：Licence number, Licence type, Status, Start date, Trading Status, LGA, Precinct, Extended trading

## g0337（1 列）
- 見出し：Fax
- 例1 値：4625 8433 | 4654 5009 | 4748 2164 | 4746 3338 | 13 QGOV (13 74 68)
  - 同じ表の列：Column, Title, Wheelchair access, Suburb, State, Notes, Mon am, Mon pm

## g0338（1 列）
- 見出し：Notes
- 例1 値：New vehicle registrations before 4pm. | New vehicle registrations before 14:30. | New vehicle registrations before 3.30pm. | Services not offered at this location: … | New vehicle registrations or drivers' l…
  - 同じ表の列：Column, Title, Wheelchair access, Suburb, State, Fax, Mon am, Mon pm

## g0339（1 列）
- 見出し：Mon am
- 例1 値：9:30 | 9:00 | 9:00-13:00 | 9:00 - 12:30 | 9:00-12:30
  - 同じ表の列：Column, Title, Wheelchair access, Suburb, State, Fax, Notes, Mon pm

## g0340（1 列）
- 見出し：Mon pm
- 例1 値：14:00-16:30 | 13:30-16:30 | 13:00-16:00 | 16:00 | 13:30-16:00
  - 同じ表の列：Column, Title, Wheelchair access, Suburb, State, Fax, Notes, Mon am

## g0341（1 列）
- 見出し：Tues am
- 例1 値：9:00 | 9:00-13:00 | 10:00-12:00 | 9:00-12:00 | 9:00
  - 同じ表の列：Column, Title, Wheelchair access, Suburb, State, Fax, Notes, Mon am

## g0342（1 列）
- 見出し：The Parents
- 例1 値：Gaia "The Earth" | Uranus
  - 同じ表の列：The Titans, The Cyclopes, The Hecatoncheires, The Erinyes (blood), The Gigantes (blood)

## g0343（1 列）
- 見出し：The Titans
- 例1 値：Oceanus | Phoebe | Crius | Hyperion | Theia
  - 同じ表の列：The Parents, The Cyclopes, The Hecatoncheires, The Erinyes (blood), The Gigantes (blood)

## g0344（1 列）
- 見出し：The Cyclopes
- 例1 値：Arges | Brontes | Steropes
  - 同じ表の列：The Parents, The Titans, The Hecatoncheires, The Erinyes (blood), The Gigantes (blood)

## g0345（1 列）
- 見出し：The Hecatoncheires
- 例1 値：Gyges | Cottus | Briareus
  - 同じ表の列：The Parents, The Titans, The Cyclopes, The Erinyes (blood), The Gigantes (blood)

## g0346（1 列）
- 見出し：The Erinyes (blood)
- 例1 値：Megaera | Tisiphone | Alecto
  - 同じ表の列：The Parents, The Titans, The Cyclopes, The Hecatoncheires, The Gigantes (blood)

## g0347（1 列）
- 見出し：The Gigantes (blood)
- 例1 値：Alcyoneus | Eurytus | Pallas | Thoas | Mimas
  - 同じ表の列：The Parents, The Titans, The Cyclopes, The Hecatoncheires, The Erinyes (blood)

## g0348（1 列）
- 見出し：ApplStandard
- 例1 値：[SEER Non Multi-Split <=65kW] GEMS (Air… | [SEER Multi-Split <=65kW] GEMS (Air Con… | [SEER Non Multi-Split <=65kW] GEMS (Air… | [SEER Multi-Split >65kW] GEMS (Air Cond… | [SEER Non Multi-Split <=65kW] GEMS (Air…
  - 同じ表の列：MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0349（1 列）
- 見出し：MEPSComp
- 例1 値：MEPS 2019 | MEPS 2019 | MEPS 2020 | MEPS 2019 | MEPS 2019
  - 同じ表の列：ApplStandard, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0350（1 列）
- 見出し：N-Standard
- 例1 値：AS/NZS 3823.1.1:2012 | AS/NZS 3823.1.2:2012 | AS/NZS 3823.1.2:2012 | AS/NZS 3823.1.1:2012 | AS/NZS 3823.1.1:2012
  - 同じ表の列：ApplStandard, MEPSComp, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0351（1 列）
- 見出し：Model_No
- 例1 値：FDMA71AV1A / RZAV71CV1 | RAC-XJ35FHAE/RAF-XJ35RHAE | DPRC35ECO | RAS-13U2AVSG-NZ / RAS-13U2FVG-NZ | MCHX450D326B
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0352（1 列）
- 見出し：avg_pwr_standby_mode
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, Brand, C-Dehumid_Rated, Configuration1, Configuration2

## g0353（1 列）
- 見出し：Brand
- 例1 値：DAIKIN | MITSUBISHI ELECTRIC | Olimpia Splendid | Arlec | AIRSTAGE
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, C-Dehumid_Rated, Configuration1, Configuration2

## g0354（1 列）
- 見出し：C-Dehumid_Rated
- 例1 値：N/A | N/A | N/A | 0.93 | 1.25
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, Configuration1, Configuration2

## g0355（1 列）
- 見出し：Configuration1
- 例1 値：Ducted | Ducted | Ducted | Non Ducted | Non Ducted
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration2

## g0356（1 列）
- 見出し：Configuration2
- 例1 値：Packaged | vrf | Single Split System | Single Split System | Single Split System
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1

## g0357（1 列）
- 見出し：Configuration2-unitmount
- 例1 値：Wall Hung | - | Wall Hung | Under ceiling | N/A
  - 同じ表の列：ApplStandard, MEPSComp, N-Standard, Model_No, avg_pwr_standby_mode, Brand, C-Dehumid_Rated, Configuration1

## g0358（1 列）
- 見出し：Type
- 例1 値：2 - Suspension incidents | 3 - Students excluded | 5 - Students expelled | 1 - Students suspended | 6 - Expulsion incidents
  - 同じ表の列：2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019

## g0359（1 列）
- 見出し：2012
- 例1 値：222 | 0 | 5011 | 0 | 222
  - 同じ表の列：Type, 2013, 2014, 2015, 2016, 2017, 2018, 2019

## g0360（1 列）
- 見出し：2013
- 例1 値：263 | 0 | 3842 | 261 | 5073
  - 同じ表の列：Type, 2012, 2014, 2015, 2016, 2017, 2018, 2019

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
```
