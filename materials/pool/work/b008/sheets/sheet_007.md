# ラベル用シート 007 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：Exitedwithintwelvemonths
- 例1 値：16688.0 | 3399.0 | 287537.0 | 66877.0 | 53494.0
  - 同じ表の列：Paymenttype, Totalentries (Betwe…, Percentexitedwithin…

## g0722（1 列）
- 見出し：Percentexitedwithintwelvemonths
- 例1 値：89.3 | 63.0 | 52.9 | 43.6 | 66.7
  - 同じ表の列：Paymenttype, Totalentries (Betwe…, Exitedwithintwelvem…

## g0723（1 列）
- 見出し：SA3_code_2011
- 例1 値：10202 | 11701 | 11602 | 11904 | 11903
  - 同じ表の列：FY, Servicetype, child_age, child_count, service_count, fee_hr_mean, fee_hr_std

## g0724（1 列）
- 見出し：FY
- 例1 値：FY201516 | FY201516 | FY201314 | FY201314 | FY201415
  - 同じ表の列：SA3_code_2011, Servicetype, child_age, child_count, service_count, fee_hr_mean, fee_hr_std

## g0725（2 列）
- 見出し：Servicetype
- 例1 値：LDC | LDC | BSC | LDC | BSC
  - 同じ表の列：SA3_code_2011, FY, child_age, child_count, service_count, fee_hr_mean, fee_hr_std
- 例2 値：Optional | Compulsory | Compulsory | Compulsory | Optional
  - 同じ表の列：collectionday, propnum, nextwaste, nextrecycle, nextgreen, Calendar_Link

## g0726（1 列）
- 見出し：child_age
- 例1 値：3: 10+ | 1: 0-4 | 3: 10+ | 2: 5-9 | 2: 5-9
  - 同じ表の列：SA3_code_2011, FY, Servicetype, child_count, service_count, fee_hr_mean, fee_hr_std

## g0727（1 列）
- 見出し：child_count
- 例1 値：1,130 | 50 | 310 | 1,160 | 2,200
  - 同じ表の列：SA3_code_2011, FY, Servicetype, child_age, service_count, fee_hr_mean, fee_hr_std

## g0728（1 列）
- 見出し：service_count
- 例1 値：16 | 16 | 57 | 26 | 12
  - 同じ表の列：SA3_code_2011, FY, Servicetype, child_age, child_count, fee_hr_mean, fee_hr_std

## g0729（1 列）
- 見出し：fee_hr_mean
- 例1 値：$7.80 | $8.60 | $7.60 | $6.85 | $7.15
  - 同じ表の列：SA3_code_2011, FY, Servicetype, child_age, child_count, service_count, fee_hr_std

## g0730（1 列）
- 見出し：fee_hr_std
- 例1 値：$0.70 | $0.80 | $1.60 | $0.70 | $2.40
  - 同じ表の列：SA3_code_2011, FY, Servicetype, child_age, child_count, service_count, fee_hr_mean

## g0731（3 列）
- 見出し：Year
- 例1 値：1989-90 | 1989-90 | 1989-90 | 1989-90 | 1989-90
  - 同じ表の列：Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1
- 例2 値：2023-24 | 2016-17 | 2020-21 | 2019-20 | 2018-19
  - 同じ表の列：Number of occasions…

## g0732（1 列）
- 見出し：Trade type
- 例1 値：Total Exports | Total Exports | Total Exports | Total Exports | Total Exports
  - 同じ表の列：Year, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0733（1 列）
- 見出し：TRIEC 1 digit
- 例1 値：3 Other goods | 3 Other goods | 3 Other goods | 3 Other goods | 3 Other goods
  - 同じ表の列：Year, Trade type, State, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0734（1 列）
- 見出し：TRIEC 2 digit
- 例1 値：30 Other goods | 30 Other goods | 30 Other goods | 30 Other goods | 30 Other goods
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0735（1 列）
- 見出し：TRIEC 3 digit
- 例1 値：302 Other goods - Non-monetary gold | 301 Other goods - Miscellaneous trade | 301 Other goods - Miscellaneous trade | 302 Other goods - Non-monetary gold | 304 Other goods - Confidential trade
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0736（1 列）
- 見出し：TRIEC 4 digit
- 例1 値：3019 Miscellaneous merchandise trade nes | 3041 Confidential trade | 3031 Unclassified trade & invalid items | 3031 Unclassified trade & invalid items | 3041 Confidential trade
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, Partner Country, Geographic level 1

## g0737（1 列）
- 見出し：Partner Country
- 例1 値：Saudi Arabia | Tonga | Cyprus | No Country Details | Kuwait
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Geographic level 1

## g0738（1 列）
- 見出し：Geographic level 1
- 例1 値：Asia | Asia | Asia | Asia | Asia
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country

## g0739（1 列）
- 見出し：Geographic level 2
- 例1 値：Pacific Islands | Sub-Saharan Africa | Sub-Saharan Africa | Northern & Western Europe | North America
  - 同じ表の列：Year, Trade type, State, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country

## g0740（1 列）
- 見出し：Type
- 例1 値：Thoroughbred | Thoroughbred | Thoroughbred | Thoroughbred | Thoroughbred
  - 同じ表の列：Town

## g0741（1 列）
- 見出し：Business Category
- 例1 値：Yoga | Yoga | Yoga | Yoga | Tai Chi
  - 同じ表の列：Suburb, State, LGA, Region

## g0742（1 列）
- 見出し：LGA
- 例1 値：Yarra | Ballarat | Brimbank | Whitehorse (C) | Kingston
  - 同じ表の列：Suburb, State, Business Category, Region

## g0743（1 列）
- 見出し：Region
- 例1 値：Southern Metro | Eastern Metropolitan Region | North and West Metropolitan Region | Southern Metro | Southern Metro
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0744（1 列）
- 見出し：Number of occasions on which public interest information has
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year

## g0745（1 列）
- 見出し：MARKER_ID
- 例1 値：FCC204 | MTH002 | LER510 | ELT057 | KOO500
  - 同じ表の列：MARKER_STATUS, LAT, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY

## g0746（1 列）
- 見出し：MARKER_STATUS
- 例1 値：IN CAD | IN CAD | IN CAD | IN CAD | IN CAD
  - 同じ表の列：MARKER_ID, LAT, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY

## g0747（5 列）
- 見出し：LON
- 例1 値：146.457108 | 146.59999 | 145.343517 | 144.652392 | 145.193816
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY
- 例2 値：145.10399852300 | 145.17030180000 | 145.12432455100 | 145.10729970900 | 145.21403136800
  - 同じ表の列：assetid, strno, suburb, classif, park_id, lat

## g0748（1 列）
- 見出し：A_ROAD_TYPE
- 例1 値：RD | ST | ST | RD | PL
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, LON, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY

## g0749（1 列）
- 見出し：A_ROAD_SUFFIX
- 例1 値：W | OF | OF | OF
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, LON, A_ROAD_TYPE, B_ROAD_TYPE, B_ROAD_SUFFIX, LOCALITY

## g0750（1 列）
- 見出し：B_ROAD_TYPE
- 例1 値：RD | BLVD | RD | RD | RD
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_SUFFIX, LOCALITY

## g0751（1 列）
- 見出し：B_ROAD_SUFFIX
- 例1 値：OF | OF | ON | OF | OF
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, LOCALITY

## g0752（1 列）
- 見出し：LOCALITY
- 例1 値：FLEMINGTON | WANTIRNA SOUTH | TARRAWINGEE | PORT MELBOURNE | HOTHAM HEIGHTS
  - 同じ表の列：MARKER_ID, MARKER_STATUS, LAT, LON, A_ROAD_TYPE, A_ROAD_SUFFIX, B_ROAD_TYPE, B_ROAD_SUFFIX

## g0753（1 列）
- 見出し：Date/Time
- 例1 値：08/12/2025 19:00 | 25/12/2025 03:00 | 11/12/2025 10:00 | 27/12/2025 00:00 | 02/12/2025 12:00
  - 同じ表の列：PMTSP TEOM ug/m3, PM10 TEOM ug/m3, Temperature Deg C, Barometric Pressure…

## g0754（1 列）
- 見出し：PMTSP TEOM ug/m3
- 例1 値：24.7 | 28.4 | 32.1 | 55.9 | 24.6
  - 同じ表の列：Date/Time, PM10 TEOM ug/m3, Temperature Deg C, Barometric Pressure…

## g0755（1 列）
- 見出し：PM10 TEOM ug/m3
- 例1 値：44.7 | 44.4 | 54.6 | 24.2 | 22.5
  - 同じ表の列：Date/Time, PMTSP TEOM ug/m3, Temperature Deg C, Barometric Pressure…

## g0756（1 列）
- 見出し：Temperature Deg C
- 例1 値：31.5 | 30.8 | 26.2 | 15.1 | 16.3
  - 同じ表の列：Date/Time, PMTSP TEOM ug/m3, PM10 TEOM ug/m3, Barometric Pressure…

## g0757（1 列）
- 見出し：Barometric Pressure atm
- 例1 値：1.009 | 1.005 | 0.998 | 1.000 | 0.994
  - 同じ表の列：Date/Time, PMTSP TEOM ug/m3, PM10 TEOM ug/m3, Temperature Deg C

## g0758（1 列）
- 見出し：executives
- 例1 値：7 | 23 | 39 | 44 | 27
  - 同じ表の列：year

## g0759（1 列）
- 見出し：id
- 例1 値：a05f7892-c71f-7506-e044-00144fdd4fa6 | a05f7892-c8e9-7506-e044-00144fdd4fa6 | a05f7892-c62b-7506-e044-00144fdd4fa6 | a05f7892-ce34-7506-e044-00144fdd4fa6 | a05f7892-da8a-7506-e044-00144fdd4fa6
  - 同じ表の列：title, metadataURL, dataURL, licence

## g0760（1 列）
- 見出し：title
- 例1 値：Cloncurry | Bloods Range | Scott | Mount Marumba | AUSGeoid98 v.1.0 data files: Wollongong…
  - 同じ表の列：id, metadataURL, dataURL, licence

## g0761（1 列）
- 見出し：metadataURL
- 例1 値：http://www.ga.gov.au/metadata-gateway/m… | http://www.ga.gov.au/metadata-gateway/m… | http://www.ga.gov.au/metadata-gateway/m… | http://www.ga.gov.au/metadata-gateway/m… | http://www.ga.gov.au/metadata-gateway/m…
  - 同じ表の列：id, title, dataURL, licence

## g0762（1 列）
- 見出し：dataURL
- 例1 値：http://www.ga.gov.au/corporate_data/619… | http://www.ga.gov.au/geodesy/ausgeoid/f… | http://www.ga.gov.au/corporate_data/645… | http://www.ga.gov.au/corporate_data/643… | http://www.ga.gov.au/geodesy/ausgeoid/f…
  - 同じ表の列：id, title, metadataURL, licence

## g0763（1 列）
- 見出し：licence
- 例1 値：Public Access;Creative Commons Attribut… | Public Access;Creative Commons Attribut… | Public Access;Creative Commons Attribut… | Public Access;Creative Commons Attribut… | Public Access;Creative Commons Attribut…
  - 同じ表の列：id, title, metadataURL, dataURL

## g0764（1 列）
- 見出し：Complex_Type
- 例1 値：Recreation Reserve | Recreation Reserve | Public Open Space | Skate Park | Public Open Space
  - 同じ表の列：Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0765（1 列）
- 見出し：Facility_Type
- 例1 値：Skate Park | Skate Park | Skate Park | Skate Park | Skate Park
  - 同じ表の列：Complex_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0766（1 列）
- 見出し：Bookable_Item
- 例1 値：Meredith Skate Park | Inverleigh Skate Park | Dereel Skate Park | Rokewood Skate Park | Enfield Skate Park
  - 同じ表の列：Complex_Type, Facility_Type, Assessment_No, Number, Locality, Post_Code, LAT, LONG

## g0767（1 列）
- 見出し：Assessment_No
- 例1 値：41400030 | 44400005 | 25400115 | 66117403 | 66300008
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Number, Locality, Post_Code, LAT, LONG

## g0768（1 列）
- 見出し：Number
- 例1 値：55 | 14 | 3 | 24 | 30
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, LAT, LONG

## g0769（1 列）
- 見出し：Locality
- 例1 値：Rokewood | Enfield | Dereel | Teesdale | Haddon
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Post_Code, LAT, LONG

## g0770（1 列）
- 見出し：Post_Code
- 例1 値：3351 | 3331 | 3351 | 3328 | 3333
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, LAT, LONG

## g0771（1 列）
- 見出し：ref
- 例1 値：SB00695 | SB00095 | SB00433 | SB02248 | SB00568
  - 同じ表の列：type, number_of, size, style, collection

## g0772（1 列）
- 見出し：type
- 例1 値：Waste Bin | Waste Bin | Waste Bin | Waste Bin | Waste Bin
  - 同じ表の列：ref, number_of, size, style, collection

## g0773（1 列）
- 見出し：number_of
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：ref, type, size, style, collection

## g0774（1 列）
- 見出し：size
- 例1 値：120L | 80L | 80L | 240L | 80L
  - 同じ表の列：ref, type, number_of, style, collection

## g0775（1 列）
- 見出し：style
- 例1 値：Stand and Bin | Stand and Bin | Stand and Bin | Stand and Bin | Blue Old Style
  - 同じ表の列：ref, type, number_of, size, collection

## g0776（1 列）
- 見出し：collection
- 例1 値：Monday-Thursday | Monday | Monday-Thursday | Monday-Thursday | Not Applicable
  - 同じ表の列：ref, type, number_of, size, style

## g0777（1 列）
- 見出し：Location
- 例1 値：Altona Sports Club Reserve | Hatt Reserve | Newport Lakes | Riverside Park | Williamstown Beach
  - 同じ表の列：Suburb, Material

## g0778（1 列）
- 見出し：Material
- 例1 値：Stainless | Stainless/Steel | Stainless | Stainless/Conc Filled Steel | Stainless/Steel
  - 同じ表の列：Location, Suburb

## g0779（1 列）
- 見出し：Seq
- 例1 値：1 | 4 | 5 | 3 | 2
  - 同じ表の列：Facility, Opening Hours

## g0780（1 列）
- 見出し：Facility
- 例1 値：Quantong Transfer Station | Dooen Landfill | Toolondo Transfer Station | Mt Zero Transfer Station | Horsham Transfer Station
  - 同じ表の列：Seq, Opening Hours

## g0781（1 列）
- 見出し：Opening Hours
- 例1 値：Thursday (1:00pm - 4:00pm) | Weekdays (8:00am - 3:30pm); Open All Pu… | Everyday (10:00am - 5:00pm); Boxing Day… | Wednesday (1:00pm - 4:00pm); Saturday (… | Saturday (9:00am - 12:00pm)
  - 同じ表の列：Seq, Facility

## g0782（1 列）
- 見出し：Infrastructure SA - Public Interest Disclosure Act 2018
- 例1 値：2024 - 25 | 2023 - 24 | 2021 - 22 | 2020 - 21 | 2022 - 23
  - 同じ表の列：None

## g0783（1 列）
- 見出し：None
- 例1 値：0 | 0 | Number | 0 | 0
  - 同じ表の列：Infrastructure SA -…

## g0784（1 列）
- 見出し：lord_party_id
- 例1 値：17.0 | 361.0 | 120.0 | 280.0 | 225.0
  - 同じ表の列：lord_party_id_type, country_code, state_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count, d_granted_count

## g0785（1 列）
- 見出し：lord_party_id_type
- 例1 値：party_id | party_id | party_id | party_id | party_id
  - 同じ表の列：lord_party_id, country_code, state_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count, d_granted_count

## g0786（1 列）
- 見出し：country_code
- 例1 値：us | be | jp | us | au
  - 同じ表の列：lord_party_id, lord_party_id_type, state_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count, d_granted_count

## g0787（1 列）
- 見出し：state_code
- 例1 値：new jersey | new jersey | nsw | nsw | nsw
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count, d_granted_count

## g0788（1 列）
- 見出し：financial_year
- 例1 値：1985 | 1944 | 1975 | 1952 | 1986
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, d_filed_count, pbr_filed_count, tm_filed_count, d_granted_count

## g0789（1 列）
- 見出し：d_filed_count
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, financial_year, pbr_filed_count, tm_filed_count, d_granted_count

## g0790（1 列）
- 見出し：pbr_filed_count
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, financial_year, d_filed_count, tm_filed_count, d_granted_count

## g0791（1 列）
- 見出し：tm_filed_count
- 例1 値：0 | 0 | 0 | 2 | 0
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, financial_year, d_filed_count, pbr_filed_count, d_granted_count

## g0792（1 列）
- 見出し：d_granted_count
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count

## g0793（1 列）
- 見出し：pbr_granted_count
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：lord_party_id, lord_party_id_type, country_code, state_code, financial_year, d_filed_count, pbr_filed_count, tm_filed_count

## g0794（1 列）
- 見出し：assetid
- 例1 値：PL9 | PL63 | PL75 | Unknown01 | PL128
  - 同じ表の列：strno, suburb, classif, park_id, lat, lon

## g0795（1 列）
- 見出し：strno
- 例1 値：23 | 12-14 | 10 | 3-5 | 23
  - 同じ表の列：assetid, suburb, classif, park_id, lat, lon

## g0796（1 列）
- 見出し：classif
- 例1 値：Small Playground | Small Playground | District Playground | Small Playground | Small Playground
  - 同じ表の列：assetid, strno, suburb, park_id, lat, lon

## g0797（1 列）
- 見出し：park_id
- 例1 値：FLPK31 | FLPK104 | FLPK163 | FLPK269 | FLPK62
  - 同じ表の列：assetid, strno, suburb, classif, lat, lon

## g0798（1 列）
- 見出し：Zone
- 例1 値：Central Zone | Central Zone | Northern Zone | Western Zone | Northern Zone
  - 同じ表の列：Station No., Fire Appliances

## g0799（2 列）
- 見出し：Station No.
- 例1 値：35 | 6 | 27 | 19 | 16
  - 同じ表の列：Zone, Fire Appliances
- 例2 値：425007 | 425007 | 425007 | 425007 | 425007
  - 同じ表の列：Class, Current Sampling Fr…, Parameter, Date & Time, Value, Unit

## g0800（1 列）
- 見出し：Fire Appliances
- 例1 値：Pumper Tanker | Pumper Tanker | Pumper Tanker | Mk4 Pumper, Hydraulic Platform | Mk3 Pumper, Water Tanker
  - 同じ表の列：Zone, Station No.

## g0801（1 列）
- 見出し：Timestamp (UTC)
- 例1 値：2023-03-10T18:03:20Z | 2023-02-20T02:59:09Z | 2023-02-28T18:01:18Z | 2023-03-06T04:01:44Z | 2023-03-28T21:05:37Z
  - 同じ表の列：Device Tag, Raw Value, Calibration, Offset, Calibrated Value, Unit, Location Lat, Location Long

## g0802（1 列）
- 見出し：Device Tag
- 例1 値：mil-bin01 | mil-bin01 | mil-bin01 | mil-bin01 | mil-bin01
  - 同じ表の列：Timestamp (UTC), Raw Value, Calibration, Offset, Calibrated Value, Unit, Location Lat, Location Long

## g0803（1 列）
- 見出し：Raw Value
- 例1 値：1050 | 1320 | 1330 | 975 | 975
  - 同じ表の列：Timestamp (UTC), Device Tag, Calibration, Offset, Calibrated Value, Unit, Location Lat, Location Long

## g0804（1 列）
- 見出し：Calibration
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Offset, Calibrated Value, Unit, Location Lat, Location Long

## g0805（1 列）
- 見出し：Offset
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Calibration, Calibrated Value, Unit, Location Lat, Location Long

## g0806（1 列）
- 見出し：Calibrated Value
- 例1 値：1102 | 1315 | 1212 | 1032 | 1288
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Calibration, Offset, Unit, Location Lat, Location Long

## g0807（5 列）
- 見出し：Unit
- 例1 値：mm | mm | mm | mm | mm
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Calibration, Offset, Calibrated Value, Location Lat, Location Long
- 例2 値：AAU | AAU | AAU | AAU | AAU
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, VALUE

## g0808（1 列）
- 見出し：Location Lat
- 例1 値：-34.187008 | -34.187008 | -34.187008 | -34.187008 | -34.187008
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Calibration, Offset, Calibrated Value, Unit, Location Long

## g0809（1 列）
- 見出し：Location Long
- 例1 値：142.165156 | 142.165156 | 142.165156 | 142.165156 | 142.165156
  - 同じ表の列：Timestamp (UTC), Device Tag, Raw Value, Calibration, Offset, Calibrated Value, Unit, Location Lat

## g0810（1 列）
- 見出し：Class
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Station No., Current Sampling Fr…, Parameter, Date & Time, Value, Unit

## g0811（1 列）
- 見出し：Current Sampling Freq.
- 例1 値：Monthly | Monthly | Monthly | Not Reported | Monthly
  - 同じ表の列：Station No., Class, Parameter, Date & Time, Value, Unit

## g0812（1 列）
- 見出し：Parameter
- 例1 値：Alkalinity Bicarbonate as CaCO3 | BGA Algalscan | Alkalinity Bicarbonate as CaCO3 | Alkalinity Bicarbonate as CaCO3 | Alkalinity Bicarbonate as CaCO3
  - 同じ表の列：Station No., Class, Current Sampling Fr…, Date & Time, Value, Unit

## g0813（1 列）
- 見出し：Date & Time
- 例1 値：1983-12-13T09:00:00.000+10:00 | 2023-03-06T09:00:00.000+10:00 | 1983-09-20T09:00:00.000+10:00 | 1988-03-24T09:00:00.000+10:00 | 2002-03-26T09:00:00.000+10:00
  - 同じ表の列：Station No., Class, Current Sampling Fr…, Parameter, Value, Unit

## g0814（5 列）
- 見出し：Value
- 例1 値：10.4 | 160.0 | 0.01 | 245.5 | 320.0
  - 同じ表の列：Station No., Class, Current Sampling Fr…, Parameter, Date & Time, Unit
- 例2 値：761.6208042 | 748.738515 | 261088.5463 | 47088.65655 | 30264.82992
  - 同じ表の列：Date, obs__status, obs__conf_, Series key, Title complement, Decimals, Units, Issuance Type

## g0815（1 列）
- 見出し：Unit
- 例1 値：mg/l | mg/l | mg/l | mg/l | mg/l
  - 同じ表の列：Station No., Class, Current Sampling Fr…, Parameter, Date & Time, Value

## g0816（1 列）
- 見出し：State/Territory
- 例1 値：NSW | NT | WA | VIC | TAS
  - 同じ表の列：Month, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0817（1 列）
- 見出し：2015-16
- 例1 値：76960327 | 653263304 | 278014718 | 83357464 | 353537998
  - 同じ表の列：State/Territory, Month, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0818（1 列）
- 見出し：2016-17
- 例1 値：782498432 | 1268231892 | 109291802 | 460420399 | 701686881
  - 同じ表の列：State/Territory, Month, 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0819（1 列）
- 見出し：2017-18
- 例1 値：95360786 | 88666388 | 87953494 | 1109243165 | 88666388
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2018-19, 2019-20, 2020-21, 2021-22

## g0820（1 列）
- 見出し：2018-19
- 例1 値：99315305 | 93635112 | 1323682889 | 214741793 | 941778969
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22

## g0821（1 列）
- 見出し：2019-20
- 例1 値：1006303135 | 119072599 | 291428414 | 80688679 | 911887680
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2018-19, 2020-21, 2021-22

## g0822（1 列）
- 見出し：2020-21
- 例1 値：112975087 | 119976461 | 314619484 | 108504647 | 1069433780
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2021-22

## g0823（1 列）
- 見出し：2021-22
- 例1 値：204123770 | 1097178692 | 1064076040 | 103228166 | 104722831
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21

## g0824（1 列）
- 見出し：2022-23
- 例1 値：1384105741 | 99736382 | 1667912065 | 1534927175 | 1367361039
  - 同じ表の列：State/Territory, Month, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21

## g0825（1 列）
- 見出し：Theme
- 例1 値：{"Theme" : "A collection like no other" | {"Theme" : "A collection like no other" | {"Theme" : "Everyday lives" | {"Theme" : "Federation Gallery" | {"Theme" : "A collection like no other"
  - 同じ表の列：Subtheme, Title, Tags, More Info, Year, Series, Control Symbol, Barcode

## g0826（1 列）
- 見出し：Subtheme
- 例1 値：Subtheme : "Of enduring value" | Subtheme : null | Subtheme : null | Subtheme : "New Year surprises" | Subtheme : "Eavesdropping on the past"
  - 同じ表の列：Theme, Title, Tags, More Info, Year, Series, Control Symbol, Barcode

## g0827（1 列）
- 見出し：Title
- 例1 値：Title : "Breeding like rabbits" | Title : "War bride documents" | Title : "Mildenhall collection" | Title : "Faces of Australia" | Title : "Faces of Australia"
  - 同じ表の列：Theme, Subtheme, Tags, More Info, Year, Series, Control Symbol, Barcode

## g0828（1 列）
- 見出し：Tags
- 例1 値：Tags : "Sydney, New South Wales" | Tags : "White Australia Policy, Immigra… | Tags : "Navy" | Tags : "White Australia Policy, Immigra… | Tags : "Sydney, New South Wales"
  - 同じ表の列：Theme, Subtheme, Title, More Info, Year, Series, Control Symbol, Barcode

## g0829（1 列）
- 見出し：More Info
- 例1 値：MoreInfo : "Until the enactment of the … | MoreInfo : null | MoreInfo : "-" | MoreInfo : "-" | MoreInfo : "-"
  - 同じ表の列：Theme, Subtheme, Title, Tags, Year, Series, Control Symbol, Barcode

## g0830（1 列）
- 見出し：Year
- 例1 値：Year : 1954 | Year : 1911 | Year : 1945 | Year : 1931 | Year : 1926
  - 同じ表の列：Theme, Subtheme, Title, Tags, More Info, Series, Control Symbol, Barcode

## g0831（1 列）
- 見出し：Series
- 例1 値：Series : "A1500" | Series : "A1378" | Series : "A1500" | Series : "A1861" | Series : "B2455"
  - 同じ表の列：Theme, Subtheme, Title, Tags, More Info, Year, Control Symbol, Barcode

## g0832（1 列）
- 見出し：Control Symbol
- 例1 値：ControlSymbol : "K17370" | ControlSymbol : "K30/4/93/72" | ControlSymbol : "L54095" | ControlSymbol : "1973/141 Part 7" | ControlSymbol : "7084"
  - 同じ表の列：Theme, Subtheme, Title, Tags, More Info, Year, Series, Barcode

## g0833（1 列）
- 見出し：Barcode
- 例1 値：Barcode : "7480002" | Barcode : "7522920" | Barcode : "807586" | Barcode : "11854896" | Barcode : "5450875"
  - 同じ表の列：Theme, Subtheme, Title, Tags, More Info, Year, Series, Control Symbol

## g0834（1 列）
- 見出し：Collection
- 例1 値：Collection : "Australian News and Infor… | Collection : "William James Mildenhall … | Collection : "Australian News and Infor… | Collection : "Australian News and Infor… | Collection : "Australian News and Infor…
  - 同じ表の列：Theme, Subtheme, Title, Tags, More Info, Year, Series, Control Symbol

## g0835（1 列）
- 見出し：AssetNo
- 例1 値：656 | 596 | 623 | 607 | 599
  - 同じ表の列：AssetNo_old, AssetType, BeachAccessNo, AccessType, Suburb, Beach, DogInfo, AlternativeAccess

## g0836（1 列）
- 見出し：AssetNo_old
- 例1 値：33443 | 33380 | 33385 | 33402 | 33171
  - 同じ表の列：AssetNo, AssetType, BeachAccessNo, AccessType, Suburb, Beach, DogInfo, AlternativeAccess

## g0837（1 列）
- 見出し：AssetType
- 例1 値：Beach Access Sign | Beach Access Sign | Beach Access Sign | Beach Access Sign | Beach Access Sign
  - 同じ表の列：AssetNo, AssetNo_old, BeachAccessNo, AccessType, Suburb, Beach, DogInfo, AlternativeAccess

## g0838（1 列）
- 見出し：BeachAccessNo
- 例1 値：27 | 29 | 44 | 57 | 9
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, AccessType, Suburb, Beach, DogInfo, AlternativeAccess

## g0839（1 列）
- 見出し：AccessType
- 例1 値：Vehicle Access | Pedestrian Access | Pedestrian Access | Pedestrian Access | Pedestrian Access
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, Suburb, Beach, DogInfo, AlternativeAccess

## g0840（1 列）
- 見出し：Suburb
- 例1 値：Marcus Beach | Castaways Beach | Peregian Beach | Peregian Beach | Noosa North Shore
  - 同じ表の列：AssetNo, AssetNo_old, AssetType, BeachAccessNo, AccessType, Beach, DogInfo, AlternativeAccess

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
