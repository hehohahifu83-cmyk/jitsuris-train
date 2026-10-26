# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：State
- 例1 値：VIC | VIC | VIC | VIC | VIC
  - 同じ表の列：electorate, site_id, Legs, layout_1, layout_1_enter, layout_2, layout_2_enter, layout_3

## g0002（1 列）
- 見出し：electorate
- 例1 値：Ballarat | Ballarat | Ballarat | Ballarat | Ballarat
  - 同じ表の列：State, site_id, Legs, layout_1, layout_1_enter, layout_2, layout_2_enter, layout_3

## g0003（1 列）
- 見出し：site_id
- 例1 値：4933 | 4944 | 4938 | 4928 | 4929
  - 同じ表の列：State, electorate, Legs, layout_1, layout_1_enter, layout_2, layout_2_enter, layout_3

## g0004（1 列）
- 見出し：Legs
- 例1 値：3 | 4 | 4 | 4 | 4
  - 同じ表の列：State, electorate, site_id, layout_1, layout_1_enter, layout_2, layout_2_enter, layout_3

## g0005（1 列）
- 見出し：layout_1
- 例1 値：42 | 21 | 25 | 72 | 91
  - 同じ表の列：State, electorate, site_id, Legs, layout_1_enter, layout_2, layout_2_enter, layout_3

## g0006（1 列）
- 見出し：layout_1_enter
- 例1 値：188 | 214 | 271 | 188 | 188
  - 同じ表の列：State, electorate, site_id, Legs, layout_1, layout_2, layout_2_enter, layout_3

## g0007（1 列）
- 見出し：layout_2
- 例1 値：98 | 71 | 99 | 77 | 98
  - 同じ表の列：State, electorate, site_id, Legs, layout_1, layout_1_enter, layout_2_enter, layout_3

## g0008（1 列）
- 見出し：layout_2_enter
- 例1 値：257 | 11 | 352 | 6 | 317
  - 同じ表の列：State, electorate, site_id, Legs, layout_1, layout_1_enter, layout_2, layout_3

## g0009（1 列）
- 見出し：layout_3
- 例1 値：123 | 277 | 169 | 146 | 234
  - 同じ表の列：State, electorate, site_id, Legs, layout_1, layout_1_enter, layout_2, layout_2_enter

## g0010（1 列）
- 見出し：layout_3_enter
- 例1 値：8 | 39 | 9 | 95 | 84
  - 同じ表の列：State, electorate, site_id, Legs, layout_1, layout_1_enter, layout_2, layout_2_enter

## g0011（1 列）
- 見出し：device_id
- 例1 値：014da4 | 014daf | 014da4 | 014daf | 014da1
  - 同じ表の列：new_devices, current_devices, total_devices, left_devices, left_average_minute…, time

## g0012（1 列）
- 見出し：new_devices
- 例1 値：3 | 15 | 0 | 4 | 34
  - 同じ表の列：device_id, current_devices, total_devices, left_devices, left_average_minute…, time

## g0013（1 列）
- 見出し：current_devices
- 例1 値：1 | 1 | 6 | 4 | 13
  - 同じ表の列：device_id, new_devices, total_devices, left_devices, left_average_minute…, time

## g0014（1 列）
- 見出し：total_devices
- 例1 値：1 | 5 | 4 | 2 | 11
  - 同じ表の列：device_id, new_devices, current_devices, left_devices, left_average_minute…, time

## g0015（1 列）
- 見出し：left_devices
- 例1 値：6 | 1 | 2 | 19 | 2
  - 同じ表の列：device_id, new_devices, current_devices, total_devices, left_average_minute…, time

## g0016（1 列）
- 見出し：left_average_minutes_devices
- 例1 値：5 | 0 | 10 | 10 | 0
  - 同じ表の列：device_id, new_devices, current_devices, total_devices, left_devices, time

## g0017（1 列）
- 見出し：time
- 例1 値：2019-11-19T15:12:00+11:00 | 2019-11-19T14:44:01+11:00 | 2019-11-18T23:21:03+11:00 | 2019-11-19T06:51:31+11:00 | 2019-11-20T23:13:53+11:00
  - 同じ表の列：device_id, new_devices, current_devices, total_devices, left_devices, left_average_minute…

## g0018（1 列）
- 見出し：GRP Expenditure Method $M
- 例1 値：minus Overseas Imports | Per Worker GRP ($'000) | minus Domestic Imports | Government Consumption | Public Gross Fixed Capital Expenditure
  - 同じ表の列：Greater Geelong (C)…, Victoria (State) (A…, G21 Region (Apr 201…

## g0019（1 列）
- 見出し：Greater Geelong (C) (Mar 2015)
- 例1 値：$8,625.43 | 210,873 | $9,815.21 | -$4,321.80 | $138.05
  - 同じ表の列：GRP Expenditure Met…, Victoria (State) (A…, G21 Region (Apr 201…

## g0020（1 列）
- 見出し：Victoria (State) (Apr 2015)
- 例1 値：$108,208.49 | $350,343.00 | $24,489.21 | $144.65 | -$72,240.38
  - 同じ表の列：GRP Expenditure Met…, Greater Geelong (C)…, G21 Region (Apr 201…

## g0021（1 列）
- 見出し：G21 Region (Apr 2015)
- 例1 値：$3,828.57 | $11,406.25 | $19,682.10 | -$4,576.62 | $48.22
  - 同じ表の列：GRP Expenditure Met…, Greater Geelong (C)…, Victoria (State) (A…

## g0022（3 列）
- 見出し：census_year
- 例1 値：2024 | 2020 | 2022 | 2024 | 2024
  - 同じ表の列：clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…, electricity_gas_wat…
- 例2 値：2023 | 2020 | 2024 | 2020 | 2020
  - 同じ表の列：clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, construction, education_and_train…

## g0023（1 列）
- 見出し：clue_small_area
- 例1 値：West Melbourne (Residential) | Port Melbourne | Kensington | North Melbourne | Kensington
  - 同じ表の列：census_year, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…, electricity_gas_wat…

## g0024（1 列）
- 見出し：accommodation_and_food_services
- 例1 値：0 | 1 | 4 | 11 | 4
  - 同じ表の列：census_year, clue_small_area, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…, electricity_gas_wat…

## g0025（1 列）
- 見出し：administrative_and_support_services
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…, electricity_gas_wat…

## g0026（1 列）
- 見出し：agriculture_forestry_and_fishing
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, arts_and_recreation…, construction, education_and_train…, electricity_gas_wat…

## g0027（2 列）
- 見出し：arts_and_recreation_services
- 例1 値：0 | 0 | 1 | 3 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, construction, education_and_train…, electricity_gas_wat…
- 例2 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, business_services, construction, education_and_train…

## g0028（2 列）
- 見出し：construction
- 例1 値：0 | 4 | 1 | 0 | 1
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, education_and_train…, electricity_gas_wat…
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, education_and_train…

## g0029（2 列）
- 見出し：education_and_training
- 例1 値：0 | 0 | 0 | 1 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, electricity_gas_wat…
- 例2 値：2 | 0 | 0 | 0 | 2
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, construction

## g0030（2 列）
- 見出し：electricity_gas_water_and_waste_services
- 例1 値：0 | 0 | 0 | 0 | 3
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…
- 例2 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, construction

## g0031（1 列）
- 見出し：financial_and_insurance_services
- 例1 値：0 | 1 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation_and_f…, administrative_and_…, agriculture_forestr…, arts_and_recreation…, construction, education_and_train…

## g0032（1 列）
- 見出し：clue_small_area
- 例1 値：Melbourne (CBD) | Docklands | Kensington | Melbourne (CBD) | Parkville
  - 同じ表の列：census_year, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, construction, education_and_train…

## g0033（1 列）
- 見出し：accommodation
- 例1 値：0 | 4 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, business_services, construction, education_and_train…

## g0034（1 列）
- 見出し：admin_and_support_services
- 例1 値：0 | 2 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation, agriculture_and_min…, arts_and_recreation…, business_services, construction, education_and_train…

## g0035（1 列）
- 見出し：agriculture_and_mining
- 例1 値：0 | 2 | 0 | 0 | 0
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, arts_and_recreation…, business_services, construction, education_and_train…

## g0036（1 列）
- 見出し：business_services
- 例1 値：0 | 0 | 0 | 0 | 8
  - 同じ表の列：census_year, clue_small_area, accommodation, admin_and_support_s…, agriculture_and_min…, arts_and_recreation…, construction, education_and_train…

## g0037（2 列）
- 見出し：date
- 例1 値：2015-02-09 | 2015-12-14 | 2015-04-09 | 2015-03-06 | 2015-08-31
  - 同じ表の列：suburb, speed_limit, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_3, vehicle_class_4
- 例2 値：2007-12-03 | 2009-03-10 | 2008-01-10 | 2009-10-20 | 2009-08-11
  - 同じ表の列：cartodb_id, record_id, station_key, traffic_direction_s…, cardinal_direction_…, classification_seq, year, month

## g0038（4 列）
- 見出し：suburb
- 例1 値：Carlton | Kensington | East Melbourne | West Melbourne | Kensington
  - 同じ表の列：date, speed_limit, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_3, vehicle_class_4
- 例2 値：Keyneton | Unley | Strathalbyn | Port Lincoln | Golden Grove
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Reception, Year_1, Year_2, Year_3

## g0039（1 列）
- 見出し：speed_limit
- 例1 値：40 | 50 | 50 | 50 | 50
  - 同じ表の列：date, suburb, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_3, vehicle_class_4

## g0040（1 列）
- 見出し：direction
- 例1 値：E | W | S | S | N
  - 同じ表の列：date, suburb, speed_limit, time, vehicle_class_1, vehicle_class_2, vehicle_class_3, vehicle_class_4

## g0041（1 列）
- 見出し：time
- 例1 値：17:00 | 13:00 | 6:00 | 4:00 | 7:00
  - 同じ表の列：date, suburb, speed_limit, direction, vehicle_class_1, vehicle_class_2, vehicle_class_3, vehicle_class_4

## g0042（1 列）
- 見出し：vehicle_class_1
- 例1 値：1 | 20 | 2 | 49 | 6
  - 同じ表の列：date, suburb, speed_limit, direction, time, vehicle_class_2, vehicle_class_3, vehicle_class_4

## g0043（1 列）
- 見出し：vehicle_class_2
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：date, suburb, speed_limit, direction, time, vehicle_class_1, vehicle_class_3, vehicle_class_4

## g0044（1 列）
- 見出し：vehicle_class_3
- 例1 値：0 | 3 | 20 | 6 | 5
  - 同じ表の列：date, suburb, speed_limit, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_4

## g0045（1 列）
- 見出し：vehicle_class_4
- 例1 値：2 | 0 | 0 | 0 | 0
  - 同じ表の列：date, suburb, speed_limit, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_3

## g0046（1 列）
- 見出し：vehicle_class_5
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：date, suburb, speed_limit, direction, time, vehicle_class_1, vehicle_class_2, vehicle_class_3

## g0047（1 列）
- 見出し：ID
- 例1 値：5 | 21 | 448 | 134 | 274
  - 同じ表の列：Census_Year, School_Number, Type_of_School, Suburb, Reception, Year_1, Year_2, Year_3

## g0048（2 列）
- 見出し：School_Number
- 例1 値：1792 | 1375 | 1142 | 0971 | 0714
  - 同じ表の列：ID, Census_Year, Type_of_School, Suburb, Reception, Year_1, Year_2, Year_3
- 例2 値：0209 | 0952 | 0999 | 0783 | 0570
  - 同じ表の列：Type_of_School, Suburb, 2014, 2015, 2016, 2017, 2018, 2019

## g0049（2 列）
- 見出し：Type_of_School
- 例1 値：Primary Education | Primary Education | Primary Education | Primary Education | Primary/Secondary Combined
  - 同じ表の列：ID, Census_Year, School_Number, Suburb, Reception, Year_1, Year_2, Year_3
- 例2 値：Secondary Education | Primary/Secondary Combined | Primary Education | Primary Education | Primary Education
  - 同じ表の列：School_Number, Suburb, 2014, 2015, 2016, 2017, 2018, 2019

## g0050（1 列）
- 見出し：Reception
- 例1 値：85.9 | 80.8 | 88.9 | 83.7 | 89
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Suburb, Year_1, Year_2, Year_3

## g0051（1 列）
- 見出し：Year_1
- 例1 値：79.9 | 91.6 | 75.3 | 85 | 90.9
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Suburb, Reception, Year_2, Year_3

## g0052（1 列）
- 見出し：Year_2
- 例1 値：87 | 86.2 | 85 | 78.7 | 89.2
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Suburb, Reception, Year_1, Year_3

## g0053（1 列）
- 見出し：Year_3
- 例1 値：87.2 | 84.7 | 89.2 | 81.6 | 83.6
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Suburb, Reception, Year_1, Year_2

## g0054（1 列）
- 見出し：Year_4
- 例1 値：91.1 | 91 | 90.3 | 89.6 | 88.9
  - 同じ表の列：ID, Census_Year, School_Number, Type_of_School, Suburb, Reception, Year_1, Year_2

## g0055（1 列）
- 見出し：2014
- 例1 値：94.6 | 89.0 | 92.4 | 88.0 | 85.7
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2015, 2016, 2017, 2018, 2019

## g0056（1 列）
- 見出し：2015
- 例1 値：93.8 | 93.1 | 91.3 | 93.0 | 52.1
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2016, 2017, 2018, 2019

## g0057（1 列）
- 見出し：2016
- 例1 値：91.5 | 90.7 | 92.1 | 95.2 | 94.5
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2015, 2017, 2018, 2019

## g0058（1 列）
- 見出し：2017
- 例1 値：88.8 | 86.1 | 93.8 | 89.4 | 90.5
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2015, 2016, 2018, 2019

## g0059（1 列）
- 見出し：2018
- 例1 値：94.8 | 62.5 | 81.0 | 90.1 | 77.9
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2015, 2016, 2017, 2019

## g0060（1 列）
- 見出し：2019
- 例1 値：84.9 | 86.6 | 94.9 | 91.6 | 70.7
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2015, 2016, 2017, 2018

## g0061（1 列）
- 見出し：2020
- 例1 値：86.3 | 88.7 | 86.7 | 88.5 | 64.5
  - 同じ表の列：School_Number, Type_of_School, Suburb, 2014, 2015, 2016, 2017, 2018

## g0062（1 列）
- 見出し：Tariff
- 例1 値：DPTI owned CLER | SAPN owned LED PLC | DPTI owned Energy Only | DPTI owned Metered | SAPN owned SLUoS
  - 同じ表の列：Number of Luminaires

## g0063（1 列）
- 見出し：Number of Luminaires
- 例1 値：345 | 15963 | 12753 | 3545 | 1343
  - 同じ表の列：Tariff

## g0064（1 列）
- 見出し：LOC_LEG
- 例1 値：59471 | 64627 | 70011 | 59455 | 64620
  - 同じ表の列：SITE_XN_ROUTE, GPS_LAT, GPS_LONG, SURFACE_TYPE, BEARING_DESC, REGION, STATUS, PURPOSE

## g0065（1 列）
- 見出し：SITE_XN_ROUTE
- 例1 値：34216 | 6415 | 6600 | 6596 | 34314
  - 同じ表の列：LOC_LEG, GPS_LAT, GPS_LONG, SURFACE_TYPE, BEARING_DESC, REGION, STATUS, PURPOSE

## g0066（1 列）
- 見出し：GPS_LAT
- 例1 値：-37.799708 | -37.783563 | -37.8017268 | -37.758216 | -37.778002
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LONG, SURFACE_TYPE, BEARING_DESC, REGION, STATUS, PURPOSE

## g0067（1 列）
- 見出し：GPS_LONG
- 例1 値：144.999312 | 144.98773 | 144.97733 | 145.023728 | 145.105324
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, SURFACE_TYPE, BEARING_DESC, REGION, STATUS, PURPOSE

## g0068（1 列）
- 見出し：SURFACE_TYPE
- 例1 値：BIKE PATH | BIKE PATH | BIKE PATH | BIKE LANE | BIKE LANE
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, GPS_LONG, BEARING_DESC, REGION, STATUS, PURPOSE

## g0069（1 列）
- 見出し：BEARING_DESC
- 例1 値：NORTH BOUND | NORTH BOUND | WEST BOUND | NORTH WEST BOUND | SOUTH BOUND
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, GPS_LONG, SURFACE_TYPE, REGION, STATUS, PURPOSE

## g0070（1 列）
- 見出し：REGION
- 例1 値：METRO NORTH WEST | SOUTHERN | METRO SOUTH EAST | METRO NORTH WEST | EASTERN
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, GPS_LONG, SURFACE_TYPE, BEARING_DESC, STATUS, PURPOSE

## g0071（1 列）
- 見出し：STATUS
- 例1 値：COMBINED BIDIRECTIONAL SITE | COMBINED BIDIRECTIONAL SITE | COMBINED BIDIRECTIONAL SITE | COMBINED BIDIRECTIONAL SITE | Bayside City Council Site
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, GPS_LONG, SURFACE_TYPE, BEARING_DESC, REGION, PURPOSE

## g0072（1 列）
- 見出し：PURPOSE
- 例1 値：Commuter | Commuter | Commuter | Recreational | Recreational
  - 同じ表の列：LOC_LEG, SITE_XN_ROUTE, GPS_LAT, GPS_LONG, SURFACE_TYPE, BEARING_DESC, REGION, STATUS

## g0073（1 列）
- 見出し：Leaver type
- 例1 値：All Leavers | Year 12 Completers | All Leavers | Early School Leavers | Year 12 Completers
  - 同じ表の列：Main destination, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0074（1 列）
- 見出し：Main destination
- 例1 値：Part-time work(%) | VET cert IV+(%) | NILFET(%) | Looking for work(%) | Part-time work(%)
  - 同じ表の列：Leaver type, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0075（1 列）
- 見出し：2014
- 例1 値：3.4 | 2.9 | 6.6 | 7.0 | 6.9
  - 同じ表の列：Leaver type, Main destination, 2015, 2016, 2017, 2018, 2019, 2020

## g0076（1 列）
- 見出し：2015
- 例1 値：9.8 | 9.1 | 2.1 | 8.9 | 9.6
  - 同じ表の列：Leaver type, Main destination, 2014, 2016, 2017, 2018, 2019, 2020

## g0077（1 列）
- 見出し：2016
- 例1 値：2.8 | 64,392 | 27.8 | 8.6 | 3.8
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2017, 2018, 2019, 2020

## g0078（1 列）
- 見出し：2017
- 例1 値：6.0 | 5.8 | 50.1 | 1.7 | 37.7
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2016, 2018, 2019, 2020

## g0079（1 列）
- 見出し：2018
- 例1 値：5.2 | 87,252 | 13.8 | 2.7 | 12.7
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2016, 2017, 2019, 2020

## g0080（1 列）
- 見出し：2019
- 例1 値：11.2 | 5.1 | 87,429 | 5.7 | 3.2
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2016, 2017, 2018, 2020

## g0081（1 列）
- 見出し：2020
- 例1 値：3.7 | 5.2 | 8.0 | 5.4 | 4.0
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2016, 2017, 2018, 2019

## g0082（1 列）
- 見出し：2021
- 例1 値：13.4 | 3.2 | 2.9 | 1.2 | 4.7
  - 同じ表の列：Leaver type, Main destination, 2014, 2015, 2016, 2017, 2018, 2019

## g0083（1 列）
- 見出し：(000) Generalities
- 例1 値：(800) Literature & rhetoric | (600) Technology (Applied sciences) | (100) Philosophy & psychology | (200) Religion | (900) Geography & history
  - 同じ表の列：(00X) Generalities, 18,029

## g0084（1 列）
- 見出し：(00X) Generalities
- 例1 値：(51X) Mathematics | (18X) Ancient, medieval, Oriental philo… | (32X) Political science | (63X) Agriculture | (14X) Specific philosophical schools
  - 同じ表の列：(000) Generalities, 18,029

## g0085（1 列）
- 見出し：18,029
- 例1 値：5,525 | 1,542 | 2,267 | 6,504 | 2,235
  - 同じ表の列：(000) Generalities, (00X) Generalities

## g0086（5 列）
- 見出し：Year
- 例1 値：2013 | 2002 | 1995 | 2010 | 1985
  - 同じ表の列：Breed index
- 例2 値：1975 | 2011 | 2002 | 1997 | 1995
  - 同じ表の列：Curlew sandpiper nu…

## g0087（1 列）
- 見出し：Breed index
- 例1 値：469 | 61254 | 2193 | 180 | 9474
  - 同じ表の列：Year

## g0088（1 列）
- 見出し：Curlew sandpiper numbers
- 例1 値：19 | 965 | 285 | 0 | 101
  - 同じ表の列：Year

## g0089（1 列）
- 見出し：Number of elephant seals
- 例1 値：18908 | 19185 | 19543 | 19580 | 20614
  - 同じ表の列：Year, Number of seals ('0…

## g0090（1 列）
- 見出し：Number of seals ('000)
- 例1 値：21.218 | 23.467 | 22.337 | 19.779 | 18.67
  - 同じ表の列：Year, Number of elephant …

## g0091（1 列）
- 見出し：Year:
- 例1 値：2014 | 2018 | 2012 | 2017 | 2011
  - 同じ表の列：Neonatal Mortality …

## g0092（1 列）
- 見出し：Neonatal Mortality Ratio per 1,000 births
- 例1 値：2.4 | 2.5 | 2.4 | 2.8 | 2.2
  - 同じ表の列：Year:

## g0093（1 列）
- 見出し：Date
- 例1 値：2026-01-01 00:00:00 | 2023-07-01 00:00:00 | 2026-03-01 00:00:00 | 2022-05-01 00:00:00 | 2026-07-01 00:00:00
  - 同じ表の列：Location, Counts, Life Guard Service

## g0094（1 列）
- 見出し：Location
- 例1 値：The Strand Net 2 | The Strand Rock Pool | Pallarenda | The Strand Rock Pool | The Strand Water Park
  - 同じ表の列：Date, Counts, Life Guard Service

## g0095（1 列）
- 見出し：Counts
- 例1 値：18927 | 0 | 0 | 9898 | 5568
  - 同じ表の列：Date, Location, Life Guard Service

## g0096（1 列）
- 見出し：Life Guard Service
- 例1 値：There is one lifeguard and no stinger n… | There is one lifeguard. Winter months a… | There is one lifeguard and no stinger n… | There are 1-2 lifeguards present 6 days… | There is one lifeguard. Winter months a…
  - 同じ表の列：Date, Location, Counts

## g0097（1 列）
- 見出し：Bird Count
- 例1 値：1 | 2 | 4 | 2 | 2
  - 同じ表の列：Year, Suburb, Bird Profile

## g0098（1 列）
- 見出し：Bird Profile
- 例1 値：https://birdlife.org.au/bird-profile/li… | https://birdlife.org.au/bird-profile/ea… | https://birdlife.org.au/bird-profile/su… | https://birdlife.org.au/bird-profile/su… | https://birdlife.org.au/bird-profile/li…
  - 同じ表の列：Year, Suburb, Bird Count

## g0099（2 列）
- 見出し：Year_Month
- 例1 値：Sep-16 | Sep-16 | Sep-16 | Aug-16 | Aug-16
  - 同じ表の列：Card_type, Line, Trip
- 例2 値：Aug-2017 | Apr-2017 | Nov-2016 | Jun-2018 | Apr-2017
  - 同じ表の列：Card_type, Travel_Mode, Trip

## g0100（1 列）
- 見出し：Card_type
- 例1 値：Sgl Trip LR Child/Youth | Concession | School Student | Sgl Trip LR Child/Youth | Adult
  - 同じ表の列：Year_Month, Line, Trip

## g0101（1 列）
- 見出し：Line
- 例1 値：Dulwich Hill Line | Dulwich Hill Line | Dulwich Hill Line | Dulwich Hill Line | Dulwich Hill Line
  - 同じ表の列：Year_Month, Card_type, Trip

## g0102（1 列）
- 見出し：Trip
- 例1 値：1037 | 10 | 1591 | 58 | 33
  - 同じ表の列：Year_Month, Card_type, Line

## g0103（1 列）
- 見出し：cartodb_id
- 例1 値：38538 | 227094 | 227053 | 227040 | 20146
  - 同じ表の列：record_id, station_key, traffic_direction_s…, cardinal_direction_…, classification_seq, date, year, month

## g0104（1 列）
- 見出し：record_id
- 例1 値：17439 | 40273 | 4391 | 20594 | 45183
  - 同じ表の列：cartodb_id, station_key, traffic_direction_s…, cardinal_direction_…, classification_seq, date, year, month

## g0105（1 列）
- 見出し：station_key
- 例1 値：58595 | 58235 | 57797 | 58081 | 55569
  - 同じ表の列：cartodb_id, record_id, traffic_direction_s…, cardinal_direction_…, classification_seq, date, year, month

## g0106（1 列）
- 見出し：traffic_direction_seq
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：cartodb_id, record_id, station_key, cardinal_direction_…, classification_seq, date, year, month

## g0107（1 列）
- 見出し：cardinal_direction_seq
- 例1 値：5 | 1 | 7 | 7 | 1
  - 同じ表の列：cartodb_id, record_id, station_key, traffic_direction_s…, classification_seq, date, year, month

## g0108（1 列）
- 見出し：classification_seq
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：cartodb_id, record_id, station_key, traffic_direction_s…, cardinal_direction_…, date, year, month

## g0109（1 列）
- 見出し：month
- 例1 値：6 | 6 | 2 | 4 | 5
  - 同じ表の列：cartodb_id, record_id, station_key, traffic_direction_s…, cardinal_direction_…, classification_seq, date, year

## g0110（1 列）
- 見出し：day_of_week
- 例1 値：1 | 5 | 2 | 6 | 2
  - 同じ表の列：cartodb_id, record_id, station_key, traffic_direction_s…, cardinal_direction_…, classification_seq, date, year

## g0111（1 列）
- 見出し：Card_type
- 例1 値：Senior/Pensioner | Employee | School Student | Senior/Pensioner | Employee
  - 同じ表の列：Year_Month, Travel_Mode, Trip

## g0112（1 列）
- 見出し：Travel_Mode
- 例1 値：Ferry | Train | Ferry | Bus | Ferry
  - 同じ表の列：Year_Month, Card_type, Trip

## g0113（1 列）
- 見出し：Trip
- 例1 値：64989.0 | 41549.0 | 4474.0 | 21532401.0 | 220589.0
  - 同じ表の列：Year_Month, Card_type, Travel_Mode

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
```
