# ラベル用シート 011 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_011.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1201（1 列）
- 見出し：planning_permission_reference_no
- 例1 値：3189/23 | 22/1080 | 21590 and ABP 312692-22 | 23/854 | 2460757
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, submission_date, date_permission_was…, classification_of_w…, location_of_the_pro…

## g1202（1 列）
- 見出し：classification_of_works_or_building
- 例1 値：^construction_new_building^ | ^extension_to_a_building^,^material_cha… | ^construction_new_building^ | ^construction_new_building^ | ^material_alterations^,^material_change…
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, submission_date, date_permission_was…, planning_permission…, location_of_the_pro…

## g1203（1 列）
- 見出し：location_of_the_proposed_development
- 例1 値：SR0286688 | SR0297245 | SR0277719 | SR0287864 | SR0286669
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, submission_date, date_permission_was…, planning_permission…, classification_of_w…

## g1204（1 列）
- 見出し：eircode
- 例1 値：D18 C6K1 | V23 CV61 | D02 VX90 | R14 KT50 | F28 EH63
  - 同じ表の列：application_referen…, application_type, local_authority, submission_no, submission_date, date_permission_was…, planning_permission…, classification_of_w…

## g1205（1 列）
- 見出し：Dublin Area Codes
- 例1 値：Dublin 1 | Dublin County | Dublin County | Dublin 4 | Dublin 8
  - 同じ表の列：County, Roll Number, School Type, set_hours_26_27, set_posts__26_27, special_class_teach…, mainstream_sna_allo…, special_class_snas_…

## g1206（1 列）
- 見出し：School Type
- 例1 値：Primary | Primary | Primary | Primary | Primary
  - 同じ表の列：County, Dublin Area Codes, Roll Number, set_hours_26_27, set_posts__26_27, special_class_teach…, mainstream_sna_allo…, special_class_snas_…

## g1207（1 列）
- 見出し：set_hours_26_27
- 例1 値：25.0 | 100.0 | 150.0 | 32.5 | 47.5
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_posts__26_27, special_class_teach…, mainstream_sna_allo…, special_class_snas_…

## g1208（1 列）
- 見出し：set_posts__26_27
- 例1 値：5.0 | 1.5 | 1.0 | 4.3 | 1.3
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_hours_26_27, special_class_teach…, mainstream_sna_allo…, special_class_snas_…

## g1209（1 列）
- 見出し：special_class_teaching_posts__26_27
- 例1 値：1.0 | 2.0 | 1.0 | 1.0 | 2.0
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_hours_26_27, set_posts__26_27, mainstream_sna_allo…, special_class_snas_…

## g1210（1 列）
- 見出し：mainstream_sna_allocation__26_27
- 例1 値：0.5 | 2.0 | 3.0 | 1.83 | 1.75
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_hours_26_27, set_posts__26_27, special_class_teach…, special_class_snas_…

## g1211（1 列）
- 見出し：special_class_snas__26_27
- 例1 値：1.83 | 2.0 | 2.0 | 3.66 | 1.83
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_hours_26_27, set_posts__26_27, special_class_teach…, mainstream_sna_allo…

## g1212（1 列）
- 見出し：total_sna_allocation_26_27
- 例1 値：1.58 | 1.0 | 0.5 | 2.83 | 6.66
  - 同じ表の列：County, Dublin Area Codes, Roll Number, School Type, set_hours_26_27, set_posts__26_27, special_class_teach…, mainstream_sna_allo…

## g1213（1 列）
- 見出し：Operator
- 例1 値：Joe Moroney Coach Hire Ltd | Kearns Transport | Streamline Coaches | Slieve Bloom Coach Tours | Aircoach
  - 同じ表の列：Link

## g1214（1 列）
- 見出し：Link
- 例1 値：https://www.transportforireland.ie/tran… | https://www.transportforireland.ie/tran… | https://www.transportforireland.ie/tran… | https://www.transportforireland.ie/tran… | https://www.transportforireland.ie/tran…
  - 同じ表の列：Operator

## g1215（1 列）
- 見出し：location_of_works_services
- 例1 値：Wexford | Multiple locations within Republic of I… | Dublin | Dublin | Wicklow
  - 同じ表の列：Contract Signing Da…, Contract Start Date, Contract End Date, common_procurement_…

## g1216（1 列）
- 見出し：Contract Signing Date
- 例1 値：2023-02-23T00:00:00 | 2023-06-01T00:00:00 | 2023-02-23T00:00:00 | 2023-04-05T00:00:00 | 2023-01-19T00:00:00
  - 同じ表の列：location_of_works_s…, Contract Start Date, Contract End Date, common_procurement_…

## g1217（1 列）
- 見出し：Contract Start Date
- 例1 値：2023-09-01T00:00:00 | 2023-08-04T00:00:00 | 2023-10-17T00:00:00 | 2021-12-16T00:00:00 | 2023-09-01T00:00:00
  - 同じ表の列：location_of_works_s…, Contract Signing Da…, Contract End Date, common_procurement_…

## g1218（1 列）
- 見出し：Contract End Date
- 例1 値：2026-07-31T00:00:00 | 2022-11-04T00:00:00 | 2024-12-31T00:00:00 | 2026-06-26T00:00:00 | 2025-06-30T00:00:00
  - 同じ表の列：location_of_works_s…, Contract Signing Da…, Contract Start Date, common_procurement_…

## g1219（1 列）
- 見出し：common_procurement_vocabulary__cpv__codes
- 例1 値：Codes: 7941000 | Codes: 9091000 | Codes: 7200000 | Codes: 7971000 | Codes: 31000000, 45310000, 45311000, 45…
  - 同じ表の列：location_of_works_s…, Contract Signing Da…, Contract Start Date, Contract End Date

## g1220（1 列）
- 見出し：waterbody
- 例1 値：Barrow | Blackwater [Munster] | Glen | Barrow | Island
  - 同じ表の列：rbd, hydrometric_area, region, catchment_area, bfi_soil, saar, county, easting

## g1221（1 列）
- 見出し：rbd
- 例1 値：South Western RBD | Shannon IRBD | South Eastern RBD | Shannon IRBD | Shannon IRBD
  - 同じ表の列：waterbody, hydrometric_area, region, catchment_area, bfi_soil, saar, county, easting

## g1222（1 列）
- 見出し：hydrometric_area
- 例1 値：Lower Shannon | Newry, Fane, Glyde & Dee | Shannon Estuary South | Galway Bay South East | Erriff-Clew Bay
  - 同じ表の列：waterbody, rbd, region, catchment_area, bfi_soil, saar, county, easting

## g1223（1 列）
- 見出し：region
- 例1 値：Shannon | Shannon | West | Shannon | Shannon
  - 同じ表の列：waterbody, rbd, hydrometric_area, catchment_area, bfi_soil, saar, county, easting

## g1224（1 列）
- 見出し：catchment_area
- 例1 値：75.6 | 1098.78 | 7989 | 202.76 | 279
  - 同じ表の列：waterbody, rbd, hydrometric_area, region, bfi_soil, saar, county, easting

## g1225（1 列）
- 見出し：bfi_soil
- 例1 値：0.7076 | 0.67 | 0.474 | 0.5415 | 0.5185
  - 同じ表の列：waterbody, rbd, hydrometric_area, region, catchment_area, saar, county, easting

## g1226（1 列）
- 見出し：saar
- 例1 値：917.14 | 1023.31 | 879.71 | 783.26 | 868.55
  - 同じ表の列：waterbody, rbd, hydrometric_area, region, catchment_area, bfi_soil, county, easting

## g1227（1 列）
- 見出し：easting
- 例1 値：298397 | 169290 | 234967 | 124321 | 128430
  - 同じ表の列：waterbody, rbd, hydrometric_area, region, catchment_area, bfi_soil, saar, county

## g1228（1 列）
- 見出し：northing
- 例1 値：155258 | 275913 | 212642 | 234609 | 98503
  - 同じ表の列：waterbody, rbd, hydrometric_area, region, catchment_area, bfi_soil, saar, county

## g1229（1 列）
- 見出し：Updated -
- 例1 値：Over 75 | 56 to 65 | Blank | 2020 | 2024
  - 同じ表の列：unsafe_01_10_2026, unsafe_, unsafe__2, unsafe__3

## g1230（1 列）
- 見出し：unsafe_01_10_2026
- 例1 値：1.90% | First Time Registration - National Route | 4451 | Pharmacist | Pharmaceutical Assistant
  - 同じ表の列：Updated -, unsafe_, unsafe__2, unsafe__3

## g1231（1 列）
- 見出し：unsafe_
- 例1 値：483 | Male | 423 | 178 | 171
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe__2, unsafe__3

## g1232（1 列）
- 見出し：unsafe__2
- 例1 値：1848 | 1981 | 1728 | 1968 | 1986
  - 同じ表の列：Updated -, unsafe_01_10_2026, unsafe_, unsafe__3

## g1233（1 列）
- 見出し：Local_Authority
- 例1 値：Tipperary | Louth | Fingal | Kildare | Cork County
  - 同じ表の列：County, SICAP_Lot, Female_Total, Male_Total, Other_Gender_Total, Age_15-24, Age_25-35, Age_36-45

## g1234（1 列）
- 見出し：SICAP_Lot
- 例1 値：Wexford County (14-1) | Cork Bandon & Kinsale (18-6) | Cork Charleville & Mitchelstown (18-2) | Laois County (8-1) | Dun Laoghaire/Rathdown (5-1)
  - 同じ表の列：County, Local_Authority, Female_Total, Male_Total, Other_Gender_Total, Age_15-24, Age_25-35, Age_36-45

## g1235（1 列）
- 見出し：Female_Total
- 例1 値：124 | 615 | 240 | 360 | 203
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Male_Total, Other_Gender_Total, Age_15-24, Age_25-35, Age_36-45

## g1236（1 列）
- 見出し：Male_Total
- 例1 値：259 | 210 | 427 | 351 | 206
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Other_Gender_Total, Age_15-24, Age_25-35, Age_36-45

## g1237（1 列）
- 見出し：Other_Gender_Total
- 例1 値：3 | 2 | 1 | 2 | 1
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Male_Total, Age_15-24, Age_25-35, Age_36-45

## g1238（1 列）
- 見出し：Age_15-24
- 例1 値：99 | 77 | 54 | 219 | 69
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Male_Total, Other_Gender_Total, Age_25-35, Age_36-45

## g1239（1 列）
- 見出し：Age_25-35
- 例1 値：91 | 109 | 132 | 138 | 117
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Male_Total, Other_Gender_Total, Age_15-24, Age_36-45

## g1240（1 列）
- 見出し：Age_36-45
- 例1 値：174 | 144 | 54 | 296 | 141
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Male_Total, Other_Gender_Total, Age_15-24, Age_25-35

## g1241（1 列）
- 見出し：Age_46-54
- 例1 値：187 | 71 | 65 | 184 | 27
  - 同じ表の列：County, Local_Authority, SICAP_Lot, Female_Total, Male_Total, Other_Gender_Total, Age_15-24, Age_25-35

## g1242（1 列）
- 見出し：Date of Lease (dd/mm/yyyy)
- 例1 値：2010-07-13T00:00:00 | 2010-01-21T00:00:00 | 2010-02-03T00:00:00 | 2010-02-26T00:00:00 | 2010-05-05T00:00:00
  - 同じ表の列：Type, Average Annual Rent, Length of Lease

## g1243（1 列）
- 見出し：Type
- 例1 値：New Commercial / Industrial premises | Site Only | Other | Other | New Commercial / Industrial premises
  - 同じ表の列：Date of Lease (dd/m…, Average Annual Rent, Length of Lease

## g1244（1 列）
- 見出し：Average Annual Rent
- 例1 値：9200 | 11760 | 25000 | 23789 | 7200
  - 同じ表の列：Date of Lease (dd/m…, Type, Length of Lease

## g1245（1 列）
- 見出し：Length of Lease
- 例1 値：4 Years, 9 Months | 9 Years, 9 Months | 3 Years, 0 Months | 4 Years, 9 Months | 25 Years, 0 Months
  - 同じ表の列：Date of Lease (dd/m…, Type, Average Annual Rent

## g1246（1 列）
- 見出し：number_of_taxpayer_units
- 例1 値：413 | 144 | 135 | 472 | 591
  - 同じ表の列：year, tax_cost____m_

## g1247（1 列）
- 見出し：tax_cost____m_
- 例1 値：3.2 | 5.4 | 1 | 0.8 | 3.5
  - 同じ表の列：year, number_of_taxpayer_…

## g1248（1 列）
- 見出し：Statistic
- 例1 値：Waiting at Driver Testing Centres | Waiting at Driver Testing Centres | Waiting at Driver Testing Centres | Waiting at Driver Testing Centres | Waiting at Driver Testing Centres
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C03113V03763, Test Centre, UNIT, VALUE

## g1249（1 列）
- 見出し：C03113V03763
- 例1 値：45 | 30 | 30 | 22 | 15
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Test Centre, UNIT, VALUE

## g1250（1 列）
- 見出し：Test Centre
- 例1 値：Newcastlewest | Birr | Kilrush | Raheny | Birr
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C03113V03763, UNIT, VALUE

## g1251（1 列）
- 見出し：Station_or_Post
- 例1 値：Station | Station | Station | Station | Station
  - 同じ表の列：Year, Fires, Special_Service_Inc…, False_Alarms, Total_, Ambulance_Turnouts, OBJECTID

## g1252（1 列）
- 見出し：Fires
- 例1 値：12 | 53 | 14 | 59 | 21
  - 同じ表の列：Year, Station_or_Post, Special_Service_Inc…, False_Alarms, Total_, Ambulance_Turnouts, OBJECTID

## g1253（1 列）
- 見出し：Special_Service_Incidents
- 例1 値：17 | 13 | 12 | 8 | 32
  - 同じ表の列：Year, Station_or_Post, Fires, False_Alarms, Total_, Ambulance_Turnouts, OBJECTID

## g1254（1 列）
- 見出し：False_Alarms
- 例1 値：3 | 11 | 5 | 8 | 9
  - 同じ表の列：Year, Station_or_Post, Fires, Special_Service_Inc…, Total_, Ambulance_Turnouts, OBJECTID

## g1255（1 列）
- 見出し：Total_
- 例1 値：62 | 90 | 29 | 31 | 109
  - 同じ表の列：Year, Station_or_Post, Fires, Special_Service_Inc…, False_Alarms, Ambulance_Turnouts, OBJECTID

## g1256（1 列）
- 見出し：Ambulance_Turnouts
- 例1 値：1 | 1 | 1 | 1
  - 同じ表の列：Year, Station_or_Post, Fires, Special_Service_Inc…, False_Alarms, Total_, OBJECTID

## g1257（1 列）
- 見出し：OBJECTID
- 例1 値：41 | 17 | 36 | 6 | 25
  - 同じ表の列：Year, Station_or_Post, Fires, Special_Service_Inc…, False_Alarms, Total_, Ambulance_Turnouts

## g1258（1 列）
- 見出し：Project ID
- 例1 値：GOIPG/2025/9022 | COALESCE/2025/7222 | GOIPG/2025/5735 | 25/HERA/4048 | EPSPD/2024/626
  - 同じ表の列：Research Body, Funder ROR ID, Project title, Actual Start Date, Final End Date, Award Amount

## g1259（1 列）
- 見出し：Research Body
- 例1 値：Munster Technological University (MTU) | University of Limerick | University College Dublin | National Institute for Bioprocessing Re… | Munster Technological University
  - 同じ表の列：Project ID, Funder ROR ID, Project title, Actual Start Date, Final End Date, Award Amount

## g1260（1 列）
- 見出し：Funder ROR ID
- 例1 値：https://ror.org/010t7sr36 | https://ror.org/010t7sr36 | https://ror.org/010t7sr36 | https://ror.org/010t7sr36 | https://ror.org/010t7sr36
  - 同じ表の列：Project ID, Research Body, Project title, Actual Start Date, Final End Date, Award Amount

## g1261（1 列）
- 見出し：Project title
- 例1 値：Radicalisation to the right among young… | Adapting ‘Islamic Trauma Healing’ for G… | Between Gael and Gall: Conflict and Con… | Tweet it like you mean it: Social media… | Thinking Gender via Natural History: A …
  - 同じ表の列：Project ID, Research Body, Funder ROR ID, Actual Start Date, Final End Date, Award Amount

## g1262（1 列）
- 見出し：Actual Start Date
- 例1 値：2025-01-10T00:00:00 | 2025-01-09T00:00:00 | 2025-01-13T00:00:00 | 2025-01-09T00:00:00 | 2025-01-09T00:00:00
  - 同じ表の列：Project ID, Research Body, Funder ROR ID, Project title, Final End Date, Award Amount

## g1263（1 列）
- 見出し：Final End Date
- 例1 値：2027-08-31T00:00:00 | 2027-09-30T00:00:00 | 2027-06-30T00:00:00 | 2030-02-28T00:00:00 | 2030-02-28T00:00:00
  - 同じ表の列：Project ID, Research Body, Funder ROR ID, Project title, Actual Start Date, Award Amount

## g1264（1 列）
- 見出し：Award Amount
- 例1 値：€ 120,863.00 | € 124,000.00 | € 614,552.94 | € 175,432.00 | € 5,000.00
  - 同じ表の列：Project ID, Research Body, Funder ROR ID, Project title, Actual Start Date, Final End Date

## g1265（1 列）
- 見出し：SensorTimestamp
- 例1 値：2015-03-12T02:21:00 | 2015-03-11T16:47:00 | 2015-03-10T14:41:00 | 2015-03-10T00:58:00 | 2015-03-08T16:20:00
  - 同じ表の列：no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1266（1 列）
- 見出し：no__zero_crossings__number_
- 例1 値：44 | 52 | 55 | 55 | 40
  - 同じ表の列：SensorTimestamp, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1267（1 列）
- 見出し：havg__av_wave_height___meters_
- 例1 値：0.79 | 0.94 | 0.82 | 0.37 | 0.74
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1268（1 列）
- 見出し：tz___mean_spectral_period___seconds_
- 例1 値：5.7 | 4.6 | 4.7 | 4.1 | 5.7
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1269（1 列）
- 見出し：hmax__max_wave_height___meters_
- 例1 値：0.52 | 0.52 | 1.01 | 2.46 | 1.58
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hsig__significant_w…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1270（1 列）
- 見出し：hsig__significant_wave_height___meters_
- 例1 値：1.37 | 1.66 | 1.75 | 2.25 | 1.43
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, tsig__significant_p…, h10__meters_, t10__seconds_

## g1271（1 列）
- 見出し：tsig__significant_period___seconds_
- 例1 値：7.7 | 6.9 | 7.5 | 6.5 | 6.7
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, h10__meters_, t10__seconds_

## g1272（1 列）
- 見出し：h10__meters_
- 例1 値：2.04 | 2.04 | 1.8 | 2.2 | 0.97
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, t10__seconds_

## g1273（1 列）
- 見出し：t10__seconds_
- 例1 値：8.2 | 9.7 | 6.7 | 4.5 | 6.2
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_

## g1274（1 列）
- 見出し：tavg__mean_wave_period___seconds_
- 例1 値：4.1 | 6.1 | 5.0 | 4.4 | 4.5
  - 同じ表の列：SensorTimestamp, no__zero_crossings_…, havg__av_wave_heigh…, tz___mean_spectral_…, hmax__max_wave_heig…, hsig__significant_w…, tsig__significant_p…, h10__meters_

## g1275（1 列）
- 見出し：ID
- 例1 値：e2263a8 | 180ead7d | 97ee5f0c | a056f36 | f9d0c4e2
  - 同じ表の列：ITMEast, ITMNorth

## g1276（1 列）
- 見出し：ITMEast
- 例1 値：706757.6037 | 711292.484 | 711102.2153 | 707884.9975 | 708749.0737
  - 同じ表の列：ID, ITMNorth

## g1277（1 列）
- 見出し：ITMNorth
- 例1 値：727324.2137 | 727827.1461 | 726191.6916 | 733845.7942 | 727279.9386
  - 同じ表の列：ID, ITMEast

## g1278（1 列）
- 見出し：開催年
- 例1 値：昭和63年度 | 平成3年度 | 昭和61年度 | 昭和58年度 | 平成18年度
  - 同じ表の列：対象者数, 参加者数, 参加率, 回数, TDR

## g1279（1 列）
- 見出し：対象者数
- 例1 値：2,134 | 1,675 | 2,187 | 1,139 | 1,651
  - 同じ表の列：開催年, 参加者数, 参加率, 回数, TDR

## g1280（1 列）
- 見出し：参加者数
- 例1 値：1,463 | 1,631 | 1,004 | 1,301 | 878
  - 同じ表の列：開催年, 対象者数, 参加率, 回数, TDR

## g1281（1 列）
- 見出し：参加率
- 例1 値：78.8% | 50.7% | 77.0% | 71.9% | 82.7%
  - 同じ表の列：開催年, 対象者数, 参加者数, 回数, TDR

## g1282（1 列）
- 見出し：回数
- 例1 値：28 | 50 | 60 | 54 | 63
  - 同じ表の列：開催年, 対象者数, 参加者数, 参加率, TDR

## g1283（1 列）
- 見出し：TDR
- 例1 値：7 | 15 | 6 | 22 | 3
  - 同じ表の列：開催年, 対象者数, 参加者数, 参加率, 回数

## g1284（1 列）
- 見出し：分類コード
- 例1 値：7.2 | 8 | 8.2 | 7 | 4.2
  - 同じ表の列：用途分類, 1月, 2月, 3月, 4月, 5月, 6月, 7月

## g1285（1 列）
- 見出し：用途分類
- 例1 値：その他の消費支出 | 家事雑貨 | (再掲)教育関係費 | 世帯主の年齢(歳) | 被服及び履物
  - 同じ表の列：分類コード, 1月, 2月, 3月, 4月, 5月, 6月, 7月

## g1286（1 列）
- 見出し：1月
- 例1 値：15,225 | 9,829 | 90 | 15,224 | 813
  - 同じ表の列：分類コード, 用途分類, 2月, 3月, 4月, 5月, 6月, 7月

## g1287（1 列）
- 見出し：2月
- 例1 値：89 | 272,477 | 32,159 | 227 | 13,938
  - 同じ表の列：分類コード, 用途分類, 1月, 3月, 4月, 5月, 6月, 7月

## g1288（1 列）
- 見出し：3月
- 例1 値：5,217 | 7,220 | 1,156 | 33,714 | 297,680
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 4月, 5月, 6月, 7月

## g1289（1 列）
- 見出し：4月
- 例1 値：11,593 | 4,533 | 5,341 | 3,346 | 1,433
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 3月, 5月, 6月, 7月

## g1290（1 列）
- 見出し：5月
- 例1 値：11,627 | 356 | 2.89 | 42 | 3,990
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 3月, 4月, 6月, 7月

## g1291（1 列）
- 見出し：6月
- 例1 値：5,830 | 1,075 | 31,424 | 4,498 | 6,754
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 3月, 4月, 5月, 7月

## g1292（1 列）
- 見出し：7月
- 例1 値：1,345 | 5,641 | 14,514 | 2,576 | 22,825
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 3月, 4月, 5月, 6月

## g1293（1 列）
- 見出し：8月
- 例1 値：56,628 | 3,152 | 23,832 | 32,918 | 86
  - 同じ表の列：分類コード, 用途分類, 1月, 2月, 3月, 4月, 5月, 6月

## g1294（1 列）
- 見出し：通し番号
- 例1 値：83 | 123 | 17 | 16 | 38
  - 同じ表の列：水利種別(防火水槽), 水利種別(防火水槽)名, 市町村(水槽)名, 担当区内通番(水槽), 設置場所-1(水槽), 容量・湧水量

## g1295（1 列）
- 見出し：水利種別(防火水槽)
- 例1 値：02 | 02 | 02 | 02 | 02
  - 同じ表の列：通し番号, 水利種別(防火水槽)名, 市町村(水槽)名, 担当区内通番(水槽), 設置場所-1(水槽), 容量・湧水量

## g1296（1 列）
- 見出し：水利種別(防火水槽)名
- 例1 値：防火水槽 | 防火水槽 | 防火水槽 | 防火水槽 | 防火水槽
  - 同じ表の列：通し番号, 水利種別(防火水槽), 市町村(水槽)名, 担当区内通番(水槽), 設置場所-1(水槽), 容量・湧水量

## g1297（1 列）
- 見出し：市町村(水槽)名
- 例1 値：彦根市 | 彦根市 | 彦根市 | 彦根市 | 彦根市
  - 同じ表の列：通し番号, 水利種別(防火水槽), 水利種別(防火水槽)名, 担当区内通番(水槽), 設置場所-1(水槽), 容量・湧水量

## g1298（1 列）
- 見出し：担当区内通番(水槽)
- 例1 値：15-25 | 09-01 | 03-01 | 07-12 | 13-01
  - 同じ表の列：通し番号, 水利種別(防火水槽), 水利種別(防火水槽)名, 市町村(水槽)名, 設置場所-1(水槽), 容量・湧水量

## g1299（1 列）
- 見出し：設置場所-1(水槽)
- 例1 値：彦根市広野町 | 彦根市下西川町 | 彦根市高宮町 | 彦根市犬方町 | 彦根市原町
  - 同じ表の列：通し番号, 水利種別(防火水槽), 水利種別(防火水槽)名, 市町村(水槽)名, 担当区内通番(水槽), 容量・湧水量

## g1300（1 列）
- 見出し：容量・湧水量
- 例1 値：40 | 40 | 40 | 40 | 40
  - 同じ表の列：通し番号, 水利種別(防火水槽), 水利種別(防火水槽)名, 市町村(水槽)名, 担当区内通番(水槽), 設置場所-1(水槽)

## g1301（2 列）
- 見出し：_id
- 例1 値：25 | 131 | 20 | 39 | 76
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ名称, データ概要, データ形式, 分類
- 例2 値：137 | 2 | 12 | 85 | 27
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字

## g1302（4 列）
- 見出し：都道府県コード又は市区町村コード
- 例1 値：252069 | 252069 | 252069 | 252069 | 252069
  - 同じ表の列：_id, NO, 都道府県名, 市区町村名, データ名称, データ概要, データ形式, 分類
- 例2 値：272159 | 272159 | 272159 | 272159 | 272159
  - 同じ表の列：NO, 都道府県名, 市区町村名, 施設名称, 法人営業者名称, 確認年月日, 確認番号

## g1303（1 列）
- 見出し：NO
- 例1 値：252069_00001 | 252069_00039 | 252069_00056 | 252069_00118 | 252069_00102
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, 都道府県名, 市区町村名, データ名称, データ概要, データ形式, 分類

## g1304（1 列）
- 見出し：都道府県名
- 例1 値：滋賀県 | 滋賀県 | 滋賀県 | 滋賀県 | 滋賀県
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 市区町村名, データ名称, データ概要, データ形式, 分類

## g1305（1 列）
- 見出し：市区町村名
- 例1 値：草津市 | 草津市 | 草津市 | 草津市 | 草津市
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, データ名称, データ概要, データ形式, 分類

## g1306（1 列）
- 見出し：データ名称
- 例1 値：統計書(R4) | 第5次総合計画策定に向けての市民意識調査 | くさつの家計簿 | 住所別年齢別人口(R6) | 統計書(R3)
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ概要, データ形式, 分類

## g1307（1 列）
- 見出し：データ概要
- 例1 値：市民意識調査についてです | 市民意識調査についてです | 草津市の学区別地区別年齢別人口です | 令和7年度の草津市の毎月の保護状況です。 | 市内における避難所の位置図
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ名称, データ形式, 分類

## g1308（1 列）
- 見出し：データ形式
- 例1 値：xls、pdf | pdf | xls、xlsx、pdf | doc、docx、xls、xlsx、pdf | xls
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ名称, データ概要, 分類

## g1309（1 列）
- 見出し：分類
- 例1 値：人口・世帯 | 人口・世帯 | 人口・世帯 | その他 | その他
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ名称, データ概要, データ形式

## g1310（1 列）
- 見出し：更新頻度
- 例1 値：1年 | 5年 | 1ヶ月 | 1ヶ月 | 1年
  - 同じ表の列：_id, 都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, データ名称, データ概要, データ形式

## g1311（1 列）
- 見出し：種別
- 例1 値：街区 | 運動 | 地区 | 街区 | 運動
  - 同じ表の列：公園番号, 公園名, 所管, 区, 校区, 床面積・m2, 設置年, 改修年

## g1312（1 列）
- 見出し：公園番号
- 例1 値：400318 | 400601 | 400282 | 400005 | 400347
  - 同じ表の列：種別, 公園名, 所管, 区, 校区, 床面積・m2, 設置年, 改修年

## g1313（1 列）
- 見出し：公園名
- 例1 値：築港新町はまなでしこ公園 | 深井北町公園 | 荒山公園 | 原池公園 | 笠池公園
  - 同じ表の列：種別, 公園番号, 所管, 区, 校区, 床面積・m2, 設置年, 改修年

## g1314（1 列）
- 見出し：所管
- 例1 値：原池 | 大浜 | 大浜 | 泉ヶ丘 | 泉ヶ丘
  - 同じ表の列：種別, 公園番号, 公園名, 区, 校区, 床面積・m2, 設置年, 改修年

## g1315（1 列）
- 見出し：区
- 例1 値：南 | 堺 | 堺 | 堺 | 南
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 校区, 床面積・m2, 設置年, 改修年

## g1316（1 列）
- 見出し：校区
- 例1 値：若松台 | 大仙 | 白鷺 | 晴美台 | 市
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 区, 床面積・m2, 設置年, 改修年

## g1317（1 列）
- 見出し：床面積・m2
- 例1 値：- | 67.0 | - | 15.8 | 18.0
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 区, 校区, 設置年, 改修年

## g1318（1 列）
- 見出し：設置年
- 例1 値：2004 | 1985 | 1987 | 2018 | 1989
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 区, 校区, 床面積・m2, 改修年

## g1319（1 列）
- 見出し：改修年
- 例1 値：2018 | 2022 | 2025 | 2009 | 2007
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 区, 校区, 床面積・m2, 設置年

## g1320（1 列）
- 見出し：形式・構造
- 例1 値：RC | RC | RC | RC | RC
  - 同じ表の列：種別, 公園番号, 公園名, 所管, 区, 校区, 床面積・m2, 設置年

## 答えの雛形

```
g1201	
g1202	
g1203	
g1204	
g1205	
g1206	
g1207	
g1208	
g1209	
g1210	
g1211	
g1212	
g1213	
g1214	
g1215	
g1216	
g1217	
g1218	
g1219	
g1220	
g1221	
g1222	
g1223	
g1224	
g1225	
g1226	
g1227	
g1228	
g1229	
g1230	
g1231	
g1232	
g1233	
g1234	
g1235	
g1236	
g1237	
g1238	
g1239	
g1240	
g1241	
g1242	
g1243	
g1244	
g1245	
g1246	
g1247	
g1248	
g1249	
g1250	
g1251	
g1252	
g1253	
g1254	
g1255	
g1256	
g1257	
g1258	
g1259	
g1260	
g1261	
g1262	
g1263	
g1264	
g1265	
g1266	
g1267	
g1268	
g1269	
g1270	
g1271	
g1272	
g1273	
g1274	
g1275	
g1276	
g1277	
g1278	
g1279	
g1280	
g1281	
g1282	
g1283	
g1284	
g1285	
g1286	
g1287	
g1288	
g1289	
g1290	
g1291	
g1292	
g1293	
g1294	
g1295	
g1296	
g1297	
g1298	
g1299	
g1300	
g1301	
g1302	
g1303	
g1304	
g1305	
g1306	
g1307	
g1308	
g1309	
g1310	
g1311	
g1312	
g1313	
g1314	
g1315	
g1316	
g1317	
g1318	
g1319	
g1320	
```
