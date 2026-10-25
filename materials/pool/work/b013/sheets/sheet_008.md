# ラベル用シート 008 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：creator
- 例1 値：Australian Gas Light Company | Australian Gas Light Company | Australian Gas Light Company | Australian Gas Light Company | Australian Gas Light Company
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0842（1 列）
- 見出し：dateofwork
- 例1 値：1870 | 1870 | 1870 | 1870 | 1870
  - 同じ表の列：itemid, title, caption, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber

## g0843（1 列）
- 見出し：work_zones
- 例1 値：EE14 | EE6 | WW10 | WW11 | EE5
  - 同じ表の列：id, opwk_zone

## g0844（1 列）
- 見出し：opwk_zone
- 例1 値：W11 | W3 | W5 | E8 | W4
  - 同じ表の列：id, work_zones

## g0845（1 列）
- 見出し：Town
- 例1 値：Euroa | Nagambie | Nagambie | Euroa | Nagambie
  - 同じ表の列：Descrip

## g0846（1 列）
- 見出し：Descrip
- 例1 値：Vacant Tree Site | Vacant Tree Site | Vacant Tree Site | Vacant Tree Site | Vacant Tree Site
  - 同じ表の列：Town

## g0847（1 列）
- 見出し：rub_day
- 例1 値：Monday | Tuesday | Friday | Thursday | Thursday
  - 同じ表の列：rub_weeks, rub_start, rec_day, rec_weeks, rec_start, grn_day, grn_weeks, grn_start

## g0848（1 列）
- 見出し：rub_weeks
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：rub_day, rub_start, rec_day, rec_weeks, rec_start, grn_day, grn_weeks, grn_start

## g0849（1 列）
- 見出し：rub_start
- 例1 値：2017/05/16 | 2017/05/25 | 2017/05/23 | 2017/05/16 | 2017/05/26
  - 同じ表の列：rub_day, rub_weeks, rec_day, rec_weeks, rec_start, grn_day, grn_weeks, grn_start

## g0850（1 列）
- 見出し：rec_day
- 例1 値：Thursday | Tuesday | Monday | Tuesday | Monday
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_weeks, rec_start, grn_day, grn_weeks, grn_start

## g0851（1 列）
- 見出し：rec_weeks
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_start, grn_day, grn_weeks, grn_start

## g0852（1 列）
- 見出し：rec_start
- 例1 値：2017/05/19 | 2017/05/16 | 2017/05/15 | 2017/05/26 | 2017/05/23
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_weeks, grn_day, grn_weeks, grn_start

## g0853（1 列）
- 見出し：grn_day
- 例1 値：Friday | Thursday | Friday | Tuesday | Tuesday
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_weeks, rec_start, grn_weeks, grn_start

## g0854（1 列）
- 見出し：grn_weeks
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_weeks, rec_start, grn_day, grn_start

## g0855（1 列）
- 見出し：grn_start
- 例1 値：2017/05/19 | 2017/05/15 | 2017/05/18 | 2017/05/19 | 2017/05/16
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_weeks, rec_start, grn_day, grn_weeks

## g0856（1 列）
- 見出し：missed_ph
- 例1 値：1800 065 993 | 1800 065 993 | 1800 065 993 | 1800 065 993 | 1800 065 993
  - 同じ表の列：rub_day, rub_weeks, rub_start, rec_day, rec_weeks, rec_start, grn_day, grn_weeks

## g0857（1 列）
- 見出し：Road_Number
- 例1 値：497 | 526 | 595 | 494 | 500
  - 同じ表の列：Locality, Asset_ID, Total_Length__m_, Surfaced_Width__m_, Seal_Type, Vehicles_Per_Day, Commercial_Vehicles

## g0858（1 列）
- 見出し：Asset_ID
- 例1 値：28063 | 26565 | 27131 | 26910 | 27348
  - 同じ表の列：Locality, Road_Number, Total_Length__m_, Surfaced_Width__m_, Seal_Type, Vehicles_Per_Day, Commercial_Vehicles

## g0859（1 列）
- 見出し：Total_Length__m_
- 例1 値：80.0 | 260.0 | 2380.0 | 156.0 | 150.0
  - 同じ表の列：Locality, Road_Number, Asset_ID, Surfaced_Width__m_, Seal_Type, Vehicles_Per_Day, Commercial_Vehicles

## g0860（1 列）
- 見出し：Surfaced_Width__m_
- 例1 値：3.5 | 6.0 | 6.6 | 6.3 | 6.3
  - 同じ表の列：Locality, Road_Number, Asset_ID, Total_Length__m_, Seal_Type, Vehicles_Per_Day, Commercial_Vehicles

## g0861（1 列）
- 見出し：Seal_Type
- 例1 値：Asphalt | Flush Seal | Flush Seal | Flush Seal | Unsealed
  - 同じ表の列：Locality, Road_Number, Asset_ID, Total_Length__m_, Surfaced_Width__m_, Vehicles_Per_Day, Commercial_Vehicles

## g0862（1 列）
- 見出し：Vehicles_Per_Day
- 例1 値：704 | 90 | 218 | 1457 | 2104
  - 同じ表の列：Locality, Road_Number, Asset_ID, Total_Length__m_, Surfaced_Width__m_, Seal_Type, Commercial_Vehicles

## g0863（1 列）
- 見出し：Commercial_Vehicles
- 例1 値：12 | 6 | 201 | 11 | 5
  - 同じ表の列：Locality, Road_Number, Asset_ID, Total_Length__m_, Surfaced_Width__m_, Seal_Type, Vehicles_Per_Day

## g0864（2 列）
- 見出し：Financial Year
- 例1 値：2014/15 | 2015/16 | 2015/16 | 2014/15 | 2015/16
  - 同じ表の列：Type of flow, Country, Sector, Expense $'000
- 例2 値：2015/16 | 2014/15 | 2016/17 | 2015/16 | 2014/15
  - 同じ表の列：Type of flow, Country, Sector, Expense $'000

## g0865（2 列）
- 見出し：Type of flow
- 例1 値：OOF | ODA | ODA | ODA | ODA
  - 同じ表の列：Financial Year, Country, Sector, Expense $'000
- 例2 値：ODA | ODA | OOF | ODA | ODA
  - 同じ表の列：Financial Year, Country, Sector, Expense $'000

## g0866（2 列）
- 見出し：Sector
- 例1 値：12261 | 12263 | 12281 | 12230 | 12261
  - 同じ表の列：Financial Year, Type of flow, Country, Expense $'000
- 例2 値：24081 | 22030 | 21020 | 24081 | 23010
  - 同じ表の列：Financial Year, Type of flow, Country, Expense $'000

## g0867（1 列）
- 見出し：Expense $'000
- 例1 値：496.3 | 10.2 | 21931.9 | 2303.9 | 1344.8
  - 同じ表の列：Financial Year, Type of flow, Country, Sector

## g0868（1 列）
- 見出し：Expense $'000
- 例1 値：2463.6 | 1657.7 | 42.5 | 5 | 5181.7
  - 同じ表の列：Financial Year, Type of flow, Country, Sector

## g0869（3 列）
- 見出し：val_date
- 例1 値：2022-09-17T16:34:26Z | 2022-07-21T13:30:59Z | 2022-10-06T02:19:00Z | 2022-07-29T08:19:18Z | 2022-09-22T19:57:20Z
  - 同じ表の列：dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset
- 例2 値：2023-05-21T16:29:00Z | 2023-05-21T18:19:19Z | 2023-05-21T14:48:43Z | 2023-05-21T10:35:11Z | 2023-05-21T15:43:53Z
  - 同じ表の列：dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0870（1 列）
- 見出し：dev_netid
- 例1 値：70B3D5499161045E | 70B3D5499161045E | 70B3D5499161045E | 70B3D5499161045E | 70B3D5499161045E
  - 同じ表の列：val_date, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0871（3 列）
- 見出し：dev_chid
- 例1 値：1 | 1 | 255 | 2 | 255
  - 同じ表の列：val_date, dev_netid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset
- 例2 値：1 | 3 | 5 | 10 | 5
  - 同じ表の列：val_date, dev_netid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0872（1 列）
- 見出し：val_raw
- 例1 値：37.362 | 38.584 | 46.234 | 3.937 | 3.404
  - 同じ表の列：val_date, dev_netid, dev_chid, val_type, dev_tag, dev_site, val_cal, val_offset

## g0873（2 列）
- 見出し：val_type
- 例1 値：Soil Moisture | Soil Moisture | Battery Voltage | Soil Moisture | Battery Voltage
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, dev_tag, dev_site, val_cal, val_offset
- 例2 値：Gateway Messages | Gateway Messages | Gateway Messages | Gateway Messages | Gateway Messages
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, dev_tag, dev_site, val_cal, val_offset

## g0874（2 列）
- 見出し：dev_tag
- 例1 値：SWH-SMT01 | SWH-SMT01 | SWH-SMT01 | SWH-SMT01 | SWH-SMT01
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_site, val_cal, val_offset
- 例2 値：SWH-WEA01 | SWH-WEA01 | SWH-WEA01 | SWH-WEA01 | SWH-WEA01
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_site, val_cal, val_offset

## g0875（2 列）
- 見出し：dev_site
- 例1 値：Soil Monitoring - SHRCC | Soil Monitoring - SHRCC | Soil Monitoring - SHRCC | Soil Monitoring - SHRCC | Soil Monitoring - SHRCC
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, val_cal, val_offset
- 例2 値：Weather Stations - SHRCC | Weather Stations - SHRCC | Weather Stations - SHRCC | Weather Stations - SHRCC | Weather Stations - SHRCC
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, val_cal, val_offset

## g0876（2 列）
- 見出し：val_cal
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_offset
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_offset

## g0877（3 列）
- 見出し：val_offset
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g0878（2 列）
- 見出し：dev_error
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g0879（1 列）
- 見出し：dev_netid
- 例1 値：70B3D5499A968FD2 | 70B3D5499A968FD2 | 70B3D5499A968FD2 | 70B3D5499A968FD2 | 70B3D5499A968FD2
  - 同じ表の列：val_date, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0880（1 列）
- 見出し：val_raw
- 例1 値：4.9 | 0.8 | 1.26 | 339 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_type, dev_tag, dev_site, val_cal, val_offset

## g0881（1 列）
- 見出し：val_type
- 例1 値：Speed | Speed | Temperature | Humidity (percentage) | Speed
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, dev_tag, dev_site, val_cal, val_offset

## g0882（1 列）
- 見出し：val_cal
- 例1 値：0 | 0 | 0.2 | 0 | 3.6
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_offset

## g0883（1 列）
- 見出し：dev_netid
- 例1 値：622ec530d99a407c7e6fd914 | 622ec530d99a407c7e6fd914 | 622ec530d99a407c7e6fd914 | 622ec530d99a407c7e6fd914 | 622ec530d99a407c7e6fd914
  - 同じ表の列：val_date, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal, val_offset

## g0884（1 列）
- 見出し：val_raw
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：val_date, dev_netid, dev_chid, val_type, dev_tag, dev_site, val_cal, val_offset

## g0885（1 列）
- 見出し：dev_tag
- 例1 値：SWH-GW01-V01 | SWH-GW01-V01 | SWH-GW01-V01 | SWH-GW01-V01 | SWH-GW01-V01
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_site, val_cal, val_offset

## g0886（1 列）
- 見出し：dev_site
- 例1 値：Gateways - SHRCC | Gateways - SHRCC | Gateways - SHRCC | Gateways - SHRCC | Gateways - SHRCC
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, val_cal, val_offset

## g0887（1 列）
- 見出し：dev_type
- 例1 値：virtual | virtual | virtual | virtual | virtual
  - 同じ表の列：val_date, dev_netid, dev_chid, val_raw, val_type, dev_tag, dev_site, val_cal

## g0888（1 列）
- 見出し：measurement_date
- 例1 値：2026-02-27 | 2026-09-24 | 2025-10-29 | 2026-07-04 | 2026-03-01
  - 同じ表の列：dam, catchment_area, capacity, gauge_ref, average_water_level, average_normalised_…, average_volume, maximum_water_level

## g0889（1 列）
- 見出し：dam
- 例1 値：PALUMA | ROSS | PALUMA | ROSS | ROSS
  - 同じ表の列：measurement_date, catchment_area, capacity, gauge_ref, average_water_level, average_normalised_…, average_volume, maximum_water_level

## g0890（1 列）
- 見出し：catchment_area
- 例1 値：9.8 | 9.8 | 9.8 | 750 | 750
  - 同じ表の列：measurement_date, dam, capacity, gauge_ref, average_water_level, average_normalised_…, average_volume, maximum_water_level

## g0891（1 列）
- 見出し：capacity
- 例1 値：233187 | 11400 | 233187 | 11400 | 233187
  - 同じ表の列：measurement_date, dam, catchment_area, gauge_ref, average_water_level, average_normalised_…, average_volume, maximum_water_level

## g0892（1 列）
- 見出し：gauge_ref
- 例1 値：Australian Height Datum | Australian Height Datum | Local Gauge Height | Local Gauge Height | Local Gauge Height
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, average_water_level, average_normalised_…, average_volume, maximum_water_level

## g0893（1 列）
- 見出し：average_water_level
- 例1 値：38.24 | -0.72 | 38.54 | 0.03 | 38.54
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, gauge_ref, average_normalised_…, average_volume, maximum_water_level

## g0894（1 列）
- 見出し：average_normalised_height
- 例1 値：0.9358 | 1.0287 | 1.0086 | 0.9455 | 0.9577
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, gauge_ref, average_water_level, average_volume, maximum_water_level

## g0895（1 列）
- 見出し：average_volume
- 例1 値：8727.02 | 10901.06 | 232033.79 | 12084.22 | 247039
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, gauge_ref, average_water_level, average_normalised_…, maximum_water_level

## g0896（1 列）
- 見出し：maximum_water_level
- 例1 値：37.72 | -0.12 | -0.57 | 0.08 | 38.38
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, gauge_ref, average_water_level, average_normalised_…, average_volume

## g0897（1 列）
- 見出し：maximum_normalised_height
- 例1 値：0.9003 | 0.9898 | 0.9676 | 0.9161 | 1.0036
  - 同じ表の列：measurement_date, dam, catchment_area, capacity, gauge_ref, average_water_level, average_normalised_…, average_volume

## g0898（1 列）
- 見出し：Date
- 例1 値：2024-10-01 00:00:00 | 2026-06-01 00:00:00 | 2023-04-01 00:00:00 | 2024-12-01 00:00:00 | 2022-12-01 00:00:00
  - 同じ表の列：Unit, Activity Type, Activity Code, Number of Work Orde…

## g0899（1 列）
- 見出し：Unit
- 例1 値：Civil Delivery | Parks and Open Spaces | Parks and Open Spaces | Civil Delivery | Civil Delivery
  - 同じ表の列：Date, Activity Type, Activity Code, Number of Work Orde…

## g0900（1 列）
- 見出し：Activity Type
- 例1 値：Reactive | Proactive | Proactive | Reactive | Proactive
  - 同じ表の列：Date, Unit, Activity Code, Number of Work Orde…

## g0901（1 列）
- 見出し：Activity Code
- 例1 値：Reactive Maintenance | Proactive Maintenance | Corrective Maintenance | Proactive Maintenance | Reactive Maintenance
  - 同じ表の列：Date, Unit, Activity Type, Number of Work Orde…

## g0902（1 列）
- 見出し：Number of Work Orders
- 例1 値：447 | 0 | 0 | 1 | 278
  - 同じ表の列：Date, Unit, Activity Type, Activity Code

## g0903（1 列）
- 見出し：Reporting Period
- 例1 値：1991-12 | 1983-03 | 1987-06 | 1998-06 | 1997-03
  - 同じ表の列：Sector, Euro Millions

## g0904（1 列）
- 見出し：Sector
- 例1 値：Other Resident | Non-Resident | Insurance Corporations | Other Resident | Credit Institutions and Central Bank
  - 同じ表の列：Reporting Period, Euro Millions

## g0905（1 列）
- 見出し：Euro Millions
- 例1 値：414 | 310 | 534 | 437 | 630
  - 同じ表の列：Reporting Period, Sector

## g0906（2 列）
- 見出し：STATISTIC
- 例1 値：EDA11C4 | EDA11C7 | EDA11C5 | EDA11C2 | EDA11C5
  - 同じ表の列：Statistic, TLIST(A1), Year, C02351V02955, Type of School, C02447V03042, School Programme, UNIT
- 例2 値：EDA58C9 | EDA58C3 | EDA58C2 | EDA58C7 | EDA58C2
  - 同じ表の列：Statistic, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g0907（1 列）
- 見出し：Statistic
- 例1 値：Single Sex Girls Schools providing Seco… | Single Sex Girls Schools providing Seco… | Mixed Schools providing Second Level Pr… | All Schools providing Second Level Prog… | All Schools providing Second Level Prog…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02351V02955, Type of School, C02447V03042, School Programme, UNIT

## g0908（5 列）
- 見出し：TLIST(A1)
- 例1 値：2003 | 2012 | 2005 | 2006 | 2011
  - 同じ表の列：STATISTIC, Statistic, Year, C02351V02955, Type of School, C02447V03042, School Programme, UNIT
- 例2 値：2012 | 2009 | 2003 | 2008 | 2012
  - 同じ表の列：STATISTIC, Statistic, Year, C02196V02652, State, UNIT, VALUE

## g0909（1 列）
- 見出し：C02351V02955
- 例1 値：21 | 213 | 212 | 21 | 212
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Type of School, C02447V03042, School Programme, UNIT

## g0910（1 列）
- 見出し：Type of School
- 例1 値：Community and Comprehensive schools | Second level education institutions aid… | Vocational schools | Community and Comprehensive schools | Community and Comprehensive schools
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, C02447V03042, School Programme, UNIT

## g0911（1 列）
- 見出し：C02447V03042
- 例1 値：24 | 23 | 24 | 25 | 24
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, Type of School, School Programme, UNIT

## g0912（1 列）
- 見出し：School Programme
- 例1 値：Leaving Certificate Applied Programme | Junior Certificate Programme | Leaving Certificate Applied Programme | Junior Certificate Programme | Leaving Certificate Applied Programme
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02351V02955, Type of School, C02447V03042, UNIT

## g0913（1 列）
- 見出し：Statistic
- 例1 値：Schools outside the Gaeltact in which c… | Pupils in Schools in the Gaeltacht taug… | Pupils in Mixed Medium of Instruction S… | Pupils in Schools in the Gaeltacht taug… | Schools in the Gaeltacht in which class…
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g0914（3 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, State, UNIT, VALUE
- 例2 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, State, UNIT, VALUE

## g0915（3 列）
- 見出し：STATISTIC
- 例1 値：HOSPACT | HOSPACT | HOSPACT | HOSPACT | HOSPACT
  - 同じ表の列：Statistic Label, YEAR, Year, CARETYPE, Type of Care, MEASURE, Measure, UNIT
- 例2 値：HEALTHGRAD | HEALTHGRAD | HEALTHGRAD | HEALTHGRAD | HEALTHGRAD
  - 同じ表の列：Statistic Label, YEAR, Year, FIELDSTUDY, Field of Study, UNIT, VALUE, FLAG

## g0916（1 列）
- 見出し：Statistic Label
- 例1 値：Hospital activities | Hospital activities | Hospital activities | Hospital activities | Hospital activities
  - 同じ表の列：STATISTIC, YEAR, Year, CARETYPE, Type of Care, MEASURE, Measure, UNIT

## g0917（1 列）
- 見出し：CARETYPE
- 例1 値：INPATIENT | INPATIENT | CURATIVE | CURATIVE | CURATIVE
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Type of Care, MEASURE, Measure, UNIT

## g0918（1 列）
- 見出し：Type of Care
- 例1 値：Curative (acute) Care | Curative (acute) Care | Curative (acute) Care | Curative (acute) Care | Curative (acute) Care
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, CARETYPE, MEASURE, Measure, UNIT

## g0919（2 列）
- 見出し：MEASURE
- 例1 値：DISCHSOM | BEDDAYSOM | ALOSSOM | OCCRTPSY | DISCHTOT
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, CARETYPE, Type of Care, Measure, UNIT
- 例2 値：PRACPHYSIO | PRACPHYSIO | PRACPHYSIO | PRACPHYSIO | PRACPHYSIO
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Measure, UNIT, VALUE, FLAG

## g0920（1 列）
- 見出し：Measure
- 例1 値：Average length of stay | Occupancy rate for total care | Bed days for Somatic care | Occupancy rate for Somatic care | Bed days for Somatic care
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, CARETYPE, Type of Care, MEASURE, UNIT

## g0921（3 列）
- 見出し：VALUE
- 例1 値：4460798 | 87.63 | 5.78 | 19286 | 5.8
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, CARETYPE, Type of Care, MEASURE, Measure
- 例2 値：189.4 | 184.8 | 170 | 194.5 | 70.3
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C02196V02652, State, UNIT

## g0922（1 列）
- 見出し：Statistic Label
- 例1 値：Graduates in Health related roles | Graduates in Health related roles | Graduates in Health related roles | Graduates in Health related roles | Graduates in Health related roles
  - 同じ表の列：STATISTIC, YEAR, Year, FIELDSTUDY, Field of Study, UNIT, VALUE, FLAG

## g0923（1 列）
- 見出し：FIELDSTUDY
- 例1 値：PHARMA | PHARMA | NURSING | PHARMA | PHARMA
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Field of Study, UNIT, VALUE, FLAG

## g0924（1 列）
- 見出し：Field of Study
- 例1 値：Pharmacy graduates | Pharmacy graduates | Nursing graduates | Medical graduates | Dentistry graduates
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FIELDSTUDY, UNIT, VALUE, FLAG

## g0925（2 列）
- 見出し：FLAG
- 例1 値：B | B | B | B | M
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FIELDSTUDY, Field of Study, UNIT, VALUE
- 例2 値：B | B
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0926（2 列）
- 見出し：Flag
- 例1 値：Break in series | Break in series | Break in series | Break in series | Break in series
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, FIELDSTUDY, Field of Study, UNIT, VALUE
- 例2 値：Break in series | Break in series
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, Measure, UNIT, VALUE

## g0927（1 列）
- 見出し：Statistic Label
- 例1 値：Physiotherapists | Physiotherapists | Physiotherapists | Physiotherapists | Physiotherapists
  - 同じ表の列：STATISTIC, YEAR, Year, MEASURE, Measure, UNIT, VALUE, FLAG

## g0928（1 列）
- 見出し：Measure
- 例1 値：Practising physiotherapists | Practising physiotherapists | Practising physiotherapists | Practising physiotherapists | Practising physiotherapists
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, MEASURE, UNIT, VALUE, FLAG

## g0929（2 列）
- 見出し：Statistic
- 例1 値：House Construction Cost Index | House Construction Cost Index | House Construction Cost Index | House Construction Cost Index | House Construction Cost Index
  - 同じ表の列：STATISTIC, TLIST(M1), Month, C02196V02652, State, UNIT, VALUE
- 例2 値：House Construction Cost Index | House Construction Cost Index | House Construction Cost Index | House Construction Cost Index | House Construction Cost Index
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g0930（1 列）
- 見出し：TLIST(M1)
- 例1 値：1996M12 | 2005M08 | 2003M12 | 1991M01 | 2006M11
  - 同じ表の列：STATISTIC, Statistic, Month, C02196V02652, State, UNIT, VALUE

## g0931（2 列）
- 見出し：UNIT
- 例1 値：Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100
  - 同じ表の列：STATISTIC, Statistic, TLIST(M1), Month, C02196V02652, State, VALUE
- 例2 値：Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100 | Base Jan 1991=100
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, VALUE

## g0932（1 列）
- 見出し：Type
- 例1 値：Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic… | Domestic Residence & Permissions applic…
  - 同じ表の列：Status, year, Jan, Feb, Mar, Apr, May, Jun

## g0933（2 列）
- 見出し：Status
- 例1 値：Granted | Refused | Received | Received | Received
  - 同じ表の列：Type, year, Jan, Feb, Mar, Apr, May, Jun
- 例2 値：O | O | O | O | G
  - 同じ表の列：X, Y, FID, ID, Monument, Caption, Mon_No, OBJECTID

## g0934（2 列）
- 見出し：Jan
- 例1 値：894 | 550 | 538 | 208 | 592
  - 同じ表の列：Type, Status, year, Feb, Mar, Apr, May, Jun
- 例2 値：49 | 40 | 43 | 4 | 17
  - 同じ表の列：RegionID, AreaID, Area, Year, Feb, Mar, Apr, May

## g0935（2 列）
- 見出し：Feb
- 例1 値：1870 | 823 | 2125 | 729 | 310
  - 同じ表の列：Type, Status, year, Jan, Mar, Apr, May, Jun
- 例2 値：8 | 3 | 1 | 9 | 15
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Mar, Apr, May

## g0936（2 列）
- 見出し：Mar
- 例1 値：1022 | 413 | 854 | 1958 | 2290
  - 同じ表の列：Type, Status, year, Jan, Feb, Apr, May, Jun
- 例2 値：11 | 16 | 23 | 47 | 48
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Apr, May

## g0937（2 列）
- 見出し：Apr
- 例1 値：2331 | 213 | 1344 | 72 | 1921
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, May, Jun
- 例2 値：25 | 4 | 18 | 41 | 26
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, May

## g0938（2 列）
- 見出し：May
- 例1 値：153 | 1310 | 2730 | 659 | 2749
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, Jun
- 例2 値：50 | 43 | 48 | 1 | 14
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0939（2 列）
- 見出し：Jun
- 例1 値：752 | 144 | 450 | 357 | 640
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May
- 例2 値：27 | 25 | 1 | 49 | 48
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0940（1 列）
- 見出し：Jul
- 例1 値：1550 | 110 | 180 | 617 | 808
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May

## g0941（1 列）
- 見出し：Values
- 例1 値：96 | 96 | 96 | 96 | 96
  - 同じ表の列：Date, 00:00, 00:15, 00:30, 00:45, 01:00, 01:15, 01:30

## g0942（1 列）
- 見出し：00:00
- 例1 値：432 | 440 | 408 | 424 | 416
  - 同じ表の列：Date, Values, 00:15, 00:30, 00:45, 01:00, 01:15, 01:30

## g0943（1 列）
- 見出し：00:15
- 例1 値：424 | 504 | 424 | 408 | 432
  - 同じ表の列：Date, Values, 00:00, 00:30, 00:45, 01:00, 01:15, 01:30

## g0944（1 列）
- 見出し：00:30
- 例1 値：448 | 432 | 496 | 432 | 408
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:45, 01:00, 01:15, 01:30

## g0945（1 列）
- 見出し：00:45
- 例1 値：424 | 448 | 448 | 432 | 408
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:30, 01:00, 01:15, 01:30

## g0946（1 列）
- 見出し：01:00
- 例1 値：408 | 432 | 432 | 440 | 416
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:30, 00:45, 01:15, 01:30

## g0947（1 列）
- 見出し：01:15
- 例1 値：408 | 440 | 424 | 400 | 416
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:30, 00:45, 01:00, 01:30

## g0948（1 列）
- 見出し：01:30
- 例1 値：440 | 424 | 416 | 424 | 408
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:30, 00:45, 01:00, 01:15

## g0949（1 列）
- 見出し：01:45
- 例1 値：416 | 416 | 432 | 408 | 416
  - 同じ表の列：Date, Values, 00:00, 00:15, 00:30, 00:45, 01:00, 01:15

## g0950（1 列）
- 見出し：LE_ID
- 例1 値：13260409 | 13260410 | 13260405 | 13260406 | 13260407
  - 同じ表の列：ENGLISH, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_X, CENTROID_Y, AREA

## g0951（1 列）
- 見出し：ENGLISH
- 例1 値：BLACKROCK LEA-6 | DUNDRUM LEA-7 | GLENCULLEN-SANDYFORD LEA-7 | DÚN LAOGHAIRE LEA-7 | STILLORGAN LEA-6
  - 同じ表の列：LE_ID, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_X, CENTROID_Y, AREA

## g0952（1 列）
- 見出し：CONTAE
- 例1 値：Baile Átha Cliath | Baile Átha Cliath | Baile Átha Cliath | Baile Átha Cliath | Baile Átha Cliath
  - 同じ表の列：LE_ID, ENGLISH, COUNTY, PROVINCE, GUID, CENTROID_X, CENTROID_Y, AREA

## g0953（1 列）
- 見出し：GUID
- 例1 値：2ae19629-3f4f-13a3-e055-000000000001 | 2ae19629-3efd-13a3-e055-000000000001 | 2ae19629-3f3f-13a3-e055-000000000001 | 2ae19629-3efc-13a3-e055-000000000001 | 2ae19629-3f4e-13a3-e055-000000000001
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, PROVINCE, CENTROID_X, CENTROID_Y, AREA

## g0954（1 列）
- 見出し：CENTROID_X
- 例1 値：724659.47 | 720853.94 | 717720.19 | 720118.68 | 716791.52
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_Y, AREA

## g0955（1 列）
- 見出し：CENTROID_Y
- 例1 値：727546.07 | 722697.93 | 728116.54 | 728307.05 | 727463.43
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_X, AREA

## g0956（1 列）
- 見出し：AREA
- 例1 値：11494745.72 | 10166489.35 | 11453851.74 | 52646523.44 | 8937906.87
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, PROVINCE, GUID, CENTROID_X, CENTROID_Y

## g0957（2 列）
- 見出し：Statistic
- 例1 値：Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off) | Passenger Traffic (Roll On/Roll Off)
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT
- 例2 値：Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off) | Freight Traffic (Roll On/Roll Off)
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02635V03192, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0958（1 列）
- 見出し：C02635V03192
- 例1 値：05 | 05 | 04 | - | 05
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0959（2 列）
- 見出し：Shipping Corridor
- 例1 値：Southern | All shipping corridors | Northern | Northern | All shipping corridors
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, C02638V03194, Type of Traffic, UNIT
- 例2 値：All shipping corridors | Central | Continental | Continental | Northern
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, C02638V03194, Type of Traffic, UNIT

## g0960（2 列）
- 見出し：C02638V03194
- 例1 値：9 | 8 | 9 | 9 | 8
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, Shipping Corridor, Type of Traffic, UNIT
- 例2 値：7 | 7 | 4 | 4 | 4
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, Shipping Corridor, Type of Traffic, UNIT

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
