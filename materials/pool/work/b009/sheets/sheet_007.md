# ラベル用シート 007 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：AQ_SYS
- 例1 値：Palustrine | Palustrine | Palustrine | Palustrine | Palustrine
  - 同じ表の列：WETLAND_NO, WETLAND_TY, SAL_REGIME, WTRREG, SRC_TIDE, SRC_RVR, SRC_GW, SRC_ART

## g0722（1 列）
- 見出し：SAL_REGIME
- 例1 値：Fresh | Fresh | Fresh | Fresh | Fresh
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, WTRREG, SRC_TIDE, SRC_RVR, SRC_GW, SRC_ART

## g0723（1 列）
- 見出し：WTRREG
- 例1 値：Periodically Inundated - Seasonal Or In… | Periodically Inundated - Episodic | Periodically Inundated - Episodic | Periodically Inundated - Episodic | Periodically Inundated - Episodic
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, SRC_TIDE, SRC_RVR, SRC_GW, SRC_ART

## g0724（1 列）
- 見出し：SRC_TIDE
- 例1 値：Non-tidal | Non-tidal | Non-tidal | Non-tidal | Non-tidal
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, WTRREG, SRC_RVR, SRC_GW, SRC_ART

## g0725（1 列）
- 見出し：SRC_RVR
- 例1 値：Very low | Very low | Low | Low | Low
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, WTRREG, SRC_TIDE, SRC_GW, SRC_ART

## g0726（1 列）
- 見出し：SRC_GW
- 例1 値：Unknown | Unknown | Unknown | Very High | Low
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, WTRREG, SRC_TIDE, SRC_RVR, SRC_ART

## g0727（1 列）
- 見出し：SRC_ART
- 例1 値：Unknown | Not artificial | Not artificial | Not artificial | Not artificial
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, WTRREG, SRC_TIDE, SRC_RVR, SRC_GW

## g0728（1 列）
- 見出し：DOM_VEG
- 例1 値：Forest/woodland | Unknown | Forest/woodland | Forest/woodland | No emergent vegetation
  - 同じ表の列：WETLAND_NO, WETLAND_TY, AQ_SYS, SAL_REGIME, WTRREG, SRC_TIDE, SRC_RVR, SRC_GW

## g0729（1 列）
- 見出し：Silo
- 例1 値：SHEEP HILLS | PATCHEWOLLOCK | RUPANYUP | ROSEBERY | LASCELLES
  - 同じ表の列：Lat, Long, Artist, Photo, Comments

## g0730（1 列）
- 見出し：Artist
- 例1 値：Renowned Melbourne Street Artist Rone h… | Fintan Magee is a Brisbane based street… | Guido Van Helten captured the imaginati… | Adnate is an internationally renowned s… | Russian Artist Julia Volchkova is activ…
  - 同じ表の列：Silo, Lat, Long, Photo, Comments

## g0731（1 列）
- 見出し：Photo
- 例1 値：http://yarriambiack.vic.gov.au/media/up… | http://yarriambiack.vic.gov.au/media/up… | http://yarriambiack.vic.gov.au/media/up… | http://yarriambiack.vic.gov.au/media/up… | http://yarriambiack.vic.gov.au/media/up…
  - 同じ表の列：Silo, Lat, Long, Artist, Comments

## g0732（1 列）
- 見出し：Comments
- 例1 値：Future proposed site | Parking and viewing on the East side of… | Parking area available | Parking on the West side of the Highway… | Parking on the Southern side of Gibson …
  - 同じ表の列：Silo, Lat, Long, Artist, Photo

## g0733（1 列）
- 見出し：fishing_tech
- 例1 値：TBB | TBB | HOK | DRB | FPO
  - 同じ表の列：year, Gear, vessel_length, Vessel Length, Value, unit

## g0734（1 列）
- 見出し：Gear
- 例1 値：Pelagic trawlers | Drift and/or fixed netters | Dredgers | Vessels using hooks | Pelagic trawlers
  - 同じ表の列：year, fishing_tech, vessel_length, Vessel Length, Value, unit

## g0735（1 列）
- 見出し：vessel_length
- 例1 値：VL1012 | VL1824 | VL1012 | VL0010 | VL0010
  - 同じ表の列：year, fishing_tech, Gear, Vessel Length, Value, unit

## g0736（1 列）
- 見出し：Vessel Length
- 例1 値：Vessel between 24 meters and 40 meters … | Vessel between 10 meters and 12 meters … | Vessel between 10 meters and 12 meters … | Vessel between 24 meters and 40 meters … | Vessel between 10 meters and 12 meters …
  - 同じ表の列：year, fishing_tech, Gear, vessel_length, Value, unit

## g0737（1 列）
- 見出し：Value
- 例1 値：NA | 11948250.76 | NA | 142839.5904 | -85116.3333
  - 同じ表の列：year, fishing_tech, Gear, vessel_length, Vessel Length, unit

## g0738（5 列）
- 見出し：unit
- 例1 値：euro | euro | euro | euro | euro
  - 同じ表の列：year, fishing_tech, Gear, vessel_length, Vessel Length, Value
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, County, C02669V03229, Nationality of Pupil

## g0739（1 列）
- 見出し：Charities Regulator Registration Stats for 2025
- 例1 値：Number of Trustees information updated | Number of applications refused | Provision of Information through phone,… | Number of applicantions abandoned | Number of applications withdrawn/cancel…
  - 同じ表の列：Jan-25

## g0740（1 列）
- 見出し：Jan-25
- 例1 値：5 | 515 | 74 | 3 | 1118
  - 同じ表の列：Charities Regulator…

## g0741（1 列）
- 見出し：company_num
- 例1 値：111861 | 91945 | 115918 | 670893 | 34805
  - 同じ表の列：submission_num, submission_rec_date, submission_eff_date, submissions_account…

## g0742（1 列）
- 見出し：submission_num
- 例1 値：SR2111615 | SR1677907 | SR1918108 | SR1971688 | SR1542835
  - 同じ表の列：company_num, submission_rec_date, submission_eff_date, submissions_account…

## g0743（1 列）
- 見出し：submission_rec_date
- 例1 値：2023-05-29T00:00:00 | 2023-02-17T00:00:00 | 2022-12-01T00:00:00 | 2023-02-24T00:00:00 | 2023-08-23T00:00:00
  - 同じ表の列：company_num, submission_num, submission_eff_date, submissions_account…

## g0744（1 列）
- 見出し：submission_eff_date
- 例1 値：2023-09-30T00:00:00 | 2023-09-30T00:00:00 | 2023-01-20T00:00:00 | 2023-08-24T00:00:00 | 2022-12-21T00:00:00
  - 同じ表の列：company_num, submission_num, submission_rec_date, submissions_account…

## g0745（1 列）
- 見出し：submissions_accounts_to_date
- 例1 値：2022-09-30T00:00:00 | 2022-12-31T00:00:00 | 2022-01-31T00:00:00 | 2022-04-30T00:00:00 | 2022-12-31T00:00:00
  - 同じ表の列：company_num, submission_num, submission_rec_date, submission_eff_date

## g0746（4 列）
- 見出し：STATISTIC
- 例1 値：SCA25 | SCA25 | SCA25 | SCA25 | SCA25
  - 同じ表の列：Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968
- 例2 値：ED133 | ED133 | ED133 | ED133 | ED133
  - 同じ表の列：Statistic, TLIST(A1), Year, C02451V02968, County, C02669V03229, Nationality of Pupil, UNIT

## g0747（1 列）
- 見出し：Statistic
- 例1 値：Highest Level of Education Attained of … | Highest Level of Education Attained of … | Highest Level of Education Attained of … | Highest Level of Education Attained of … | Highest Level of Education Attained of …
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968

## g0748（7 列）
- 見出し：TLIST(A1)
- 例1 値：2011 | 2011 | 2011 | 2011 | 2011
  - 同じ表の列：STATISTIC, Statistic, Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968
- 例2 値：2000 | 2001 | 2000 | 2001 | 2000
  - 同じ表の列：STATISTIC, Statistic, Year, C02451V02968, County, C02669V03229, Nationality of Pupil, UNIT

## g0749（1 列）
- 見出し：C02076V02508
- 例1 値：205 | 205 | 205 | 205 | 205
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Age Group, C02199V02655, Sex, C02451V02968

## g0750（1 列）
- 見出し：Age Group
- 例1 値：0 - 4 years | 0 - 4 years | 0 - 4 years | 0 - 4 years | 0 - 4 years
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, C02199V02655, Sex, C02451V02968

## g0751（1 列）
- 見出し：C02199V02655
- 例1 値：- | 1 | 1 | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, Sex, C02451V02968

## g0752（1 列）
- 見出し：Sex
- 例1 値：Both sexes | Both sexes | Male | Both sexes | Both sexes
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, C02451V02968

## g0753（2 列）
- 見出し：C02451V02968
- 例1 値：12 | 05 | 01 | 05 | 024
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex
- 例2 値：172 | 15 | 10 | 171 | 05
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, County, UNIT, VALUE

## g0754（1 列）
- 見出し：Administrative County
- 例1 値：All Counties | Fingal | Laois | Fingal | Cork County
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex

## g0755（1 列）
- 見出し：Statistic
- 例1 値：Pupils enrolled in Second-Level Schools | Pupils enrolled in Second-Level Schools | Pupils enrolled in Second-Level Schools | Pupils enrolled in Second-Level Schools | Pupils enrolled in Second-Level Schools
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02451V02968, County, C02669V03229, Nationality of Pupil, UNIT

## g0756（1 列）
- 見出し：C02451V02968
- 例1 値：12 | 141 | 024 | - | 24
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, County, C02669V03229, Nationality of Pupil, UNIT

## g0757（1 列）
- 見出し：County
- 例1 値：Dún Laoghaire-Rathdown | Kildare | Cork County | Offaly | Wicklow
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, C02669V03229, Nationality of Pupil, UNIT

## g0758（1 列）
- 見出し：C02669V03229
- 例1 値：ZZABI | ZZEUAB13 | IE | USCA | ZZAA10
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, County, Nationality of Pupil, UNIT

## g0759（1 列）
- 見出し：Nationality of Pupil
- 例1 値：Other countries | All countries | United Kingdom (1) | Other Europe(32) | Ireland
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, County, C02669V03229, UNIT

## g0760（4 列）
- 見出し：STATISTIC
- 例1 値：G0113C02 | G0113C01 | G0113C02 | G0113C01 | G0113C02
  - 同じ表の列：Statistic, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE
- 例2 値：HR009C01 | HR009C03 | HR009C04 | HR009C04 | HR009C02
  - 同じ表の列：Statistic, TLIST(A1), Year, C02842V03416, HSE Regions, UNIT, VALUE

## g0761（1 列）
- 見出し：Statistic
- 例1 値：SICAP Funding | RAPID Funding | RAPID Funding | SICAP Funding | SICAP Funding
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g0762（1 列）
- 見出し：C02196V02652
- 例1 値：- | - | - | - | -
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, State, UNIT, VALUE

## g0763（2 列）
- 見出し：UNIT
- 例1 値：Euro Million | Euro Million | Euro Million | Euro Million | Euro Million
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, VALUE
- 例2 値：Degrees C | Degrees C | Degrees C | Degrees C | Degrees C
  - 同じ表の列：STATISTIC, Statistic Label, tlist_m1_, Month, C02431V02938, Meteorological Weat…, VALUE

## g0764（3 列）
- 見出し：VALUE
- 例1 値：6 | 38 | 37.5 | 37.5
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, State, UNIT
- 例2 値：697 | 30 | 0.3 | 8 | 25478
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02842V03416, HSE Regions, UNIT

## g0765（1 列）
- 見出し：STATISTIC
- 例1 値：MEDICTECH | MEDICTECH | MEDICTECH | MEDICTECH | MEDICTECH
  - 同じ表の列：Statistic Label, YEAR, Year, TECHTYPE, Medical technology, SETTING, Type of setting, UNIT

## g0766（1 列）
- 見出し：Statistic Label
- 例1 値：Medical technology by type of setting | Medical technology by type of setting | Medical technology by type of setting | Medical technology by type of setting | Medical technology by type of setting
  - 同じ表の列：STATISTIC, YEAR, Year, TECHTYPE, Medical technology, SETTING, Type of setting, UNIT

## g0767（1 列）
- 見出し：TECHTYPE
- 例1 値：GAMCAM | GAMCAM | GAMCAM | RTEQUIP | GAMCAM
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, Medical technology, SETTING, Type of setting, UNIT

## g0768（1 列）
- 見出し：Medical technology
- 例1 値：Gamma camera | Gamma camera | Gamma camera | PET scanner | MRI unit
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TECHTYPE, SETTING, Type of setting, UNIT

## g0769（1 列）
- 見出し：SETTING
- 例1 値：HP4 | HP1HP17 | HP4 | HP1HP15 | HP1HP17
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TECHTYPE, Medical technology, Type of setting, UNIT

## g0770（1 列）
- 見出し：Type of setting
- 例1 値：Total (HP.1+HP.3) | Total (HP.1+HP.3) | Ambulatory (HP.3) | Total (HP.1+HP.3) | Hospital (HP.1)
  - 同じ表の列：STATISTIC, Statistic Label, YEAR, Year, TECHTYPE, Medical technology, SETTING, UNIT

## g0771（2 列）
- 見出し：County
- 例1 値：Cavan | Wicklow | Kildare | Limerick | Kerry
  - 同じ表の列：Number of Licences, numbers_of_deer_sho…, numbers_of_deer_sho…, numbers_of_deer_sho…
- 例2 値：Wexford | Wexford | Wexford | Wexford | Wexford
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town

## g0772（1 列）
- 見出し：Number of Licences
- 例1 値：68 | 0 | 21 | 27 | 11
  - 同じ表の列：County, numbers_of_deer_sho…, numbers_of_deer_sho…, numbers_of_deer_sho…

## g0773（1 列）
- 見出し：numbers_of_deer_shot__male_
- 例1 値：118 | 4,764 | 322 | 0 | 20
  - 同じ表の列：County, Number of Licences, numbers_of_deer_sho…, numbers_of_deer_sho…

## g0774（1 列）
- 見出し：numbers_of_deer_shot__female_
- 例1 値：22 | 15 | 2 | 0 | 71
  - 同じ表の列：County, Number of Licences, numbers_of_deer_sho…, numbers_of_deer_sho…

## g0775（1 列）
- 見出し：numbers_of_deer_shot__total_
- 例1 値：690 | 129 | 32 | 9,508 | 7
  - 同じ表の列：County, Number of Licences, numbers_of_deer_sho…, numbers_of_deer_sho…

## g0776（1 列）
- 見出し：Type
- 例1 値：FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli… | FRU - International Protection by Appli…
  - 同じ表の列：Status, year, Jan, Feb, Mar, Apr, May, Jun

## g0777（2 列）
- 見出し：Jan
- 例1 値：143 | 26 | 254 | 31 | 21
  - 同じ表の列：Type, Status, year, Feb, Mar, Apr, May, Jun
- 例2 値：223 | 289 | 8 | 144 | 153
  - 同じ表の列：RegionID, AreaID, Area, Year, Feb, Mar, Apr, May

## g0778（2 列）
- 見出し：Feb
- 例1 値：166 | 44 | 32 | 60 | 63
  - 同じ表の列：Type, Status, year, Jan, Mar, Apr, May, Jun
- 例2 値：373 | 177 | 1 | 117 | 112
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Mar, Apr, May

## g0779（2 列）
- 見出し：Mar
- 例1 値：244 | 67 | 27 | 56 | 50
  - 同じ表の列：Type, Status, year, Jan, Feb, Apr, May, Jun
- 例2 値：161 | 11 | 1 | 128 | 97
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Apr, May

## g0780（2 列）
- 見出し：Apr
- 例1 値：54 | 22 | 8 | 65 | 0
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, May, Jun
- 例2 値：226 | 12 | 15 | 22 | 1
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, May

## g0781（2 列）
- 見出し：May
- 例1 値：0 | 0 | 16 | 391 | 72
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, Jun
- 例2 値：16 | 152 | 21 | 99 | 50
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0782（2 列）
- 見出し：Jun
- 例1 値：252 | 80 | 20 | 0 | 107
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May
- 例2 値：59 | 24 | 196 | 25 | 192
  - 同じ表の列：RegionID, AreaID, Area, Year, Jan, Feb, Mar, Apr

## g0783（1 列）
- 見出し：Jul
- 例1 値：30 | 6 | 33 | 9 | *
  - 同じ表の列：Type, Status, year, Jan, Feb, Mar, Apr, May

## g0784（1 列）
- 見出し：Level_1
- 例1 値：V33 - Tourism, Culture, Arts, Gaeltacht… | V7 - Department Of Finance (net) | V38 - Health (net) | V32 - Business, Enterprise & Innovation… | V33 - Tourism, Culture, Arts, Gaeltacht…
  - 同じ表の列：Year, Level_2, Level_3, Level_4, Level_5, Level_6, Dept_Level_1, Dept_Level_2

## g0785（1 列）
- 見出し：Level_2
- 例1 値：V31 - Transport (gross) | V27 - International Co-operation (gross) | V2 - Department Of The Taoiseach (gross) | V2 - Department Of The Taoiseach (gross) | V19 - Office Of The Ombudsman (gross)
  - 同じ表の列：Year, Level_1, Level_3, Level_4, Level_5, Level_6, Dept_Level_1, Dept_Level_2

## g0786（1 列）
- 見出し：Level_3
- 例1 値：C - Regulation | - Retired Expenditure | - An Equal And Inclusive Society (Civil… | - Retired Expenditure | B - Appropriations In Aid
  - 同じ表の列：Year, Level_1, Level_2, Level_4, Level_5, Level_6, Dept_Level_1, Dept_Level_2

## g0787（1 列）
- 見出し：Level_4
- 例1 値：V38 - Other Services | A.1 - Salaries, Wages And Allowances | V9 - Administration (1994 - 2009) | - admin & Other Service Receipts | V36 - Administration (1994 - 2010)
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_5, Level_6, Dept_Level_1, Dept_Level_2

## g0788（1 列）
- 見出し：Level_5
- 例1 値：A.4 - Postal And Telecommunications Ser… | - Grants-in-aid | - Grants To Health Boards - Gms Payments | - Childcare | - Drug Recoupment Schemes
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_6, Dept_Level_1, Dept_Level_2

## g0789（1 列）
- 見出し：Level_6
- 例1 値：- An Post Licence Fees | A.6 - Office Premises Expenses | - Institute Of Public Administration (g… | A.7 - Consultancy Services | - Educational And Visitor Services
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_5, Dept_Level_1, Dept_Level_2

## g0790（1 列）
- 見出し：Dept_Level_1
- 例1 値：Environment, Climate and Communications… | Taoiseach's Group | Tourism, Culture, Arts, Gaeltacht, Spor… | Environment, Climate and Communications… | Finance Group
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, Dept_Level_2

## g0791（1 列）
- 見出し：Dept_Level_2
- 例1 値：International Co-operation | Defence | Education and Skills | - President's Establishment (Moved to T… | Housing, Local Government & Heritage
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, Dept_Level_1

## g0792（1 列）
- 見出し：Exp_Level_1
- 例1 値：Current | Current | Current | Current | Current
  - 同じ表の列：Year, Level_1, Level_2, Level_3, Level_4, Level_5, Level_6, Dept_Level_1

## g0793（1 列）
- 見出し：period
- 例1 値：2014Q3 | 2014Q1 | 2014Q4 | 2014Q2 | 2014Q4
  - 同じ表の列：programme, scheme, basis, age_code, age_band, recipients

## g0794（1 列）
- 見出し：programme
- 例1 値：Children | Illness,Disability and Caring | Illness,Disability and Caring | Supplementary Payments and Miscellaneou… | Working Age Income Supports
  - 同じ表の列：period, scheme, basis, age_code, age_band, recipients

## g0795（1 列）
- 見出し：scheme
- 例1 値：INVP | BASI | RCG | OFP | UA
  - 同じ表の列：period, programme, basis, age_code, age_band, recipients

## g0796（1 列）
- 見出し：basis
- 例1 値：Social Assistance | Social Assistance | Social Assistance | Social Assistance | Social Assistance
  - 同じ表の列：period, programme, scheme, age_code, age_band, recipients

## g0797（1 列）
- 見出し：age_code
- 例1 値：410 | 515 | 365 | 530 | 495
  - 同じ表の列：period, programme, scheme, basis, age_band, recipients

## g0798（1 列）
- 見出し：age_band
- 例1 値：60 - 65 years | 30 - 34 years | 55 - 59 years | 66 years and over | Under 20 years
  - 同じ表の列：period, programme, scheme, basis, age_code, recipients

## g0799（1 列）
- 見出し：recipients
- 例1 値：230 | 39254 | 1129 | 28699 | 1358
  - 同じ表の列：period, programme, scheme, basis, age_code, age_band

## g0800（1 列）
- 見出し：PubliclyOp
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OBJECTID, universall, dlr, AgeGroup

## g0801（1 列）
- 見出し：universall
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OBJECTID, PubliclyOp, dlr, AgeGroup

## g0802（1 列）
- 見出し：dlr
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OBJECTID, PubliclyOp, universall, AgeGroup

## g0803（1 列）
- 見出し：AgeGroup
- 例1 値：toddler, junior | toddler | toddler, junior | junior | toddler, junior
  - 同じ表の列：OBJECTID, PubliclyOp, universall, dlr

## g0804（1 列）
- 見出し：Tree_ID
- 例1 値：8040 | 3412 | 3408 | 2828 | 4244
  - 同じ表の列：Town, Tree_Species, Species_Desc, Age_Desc, Height, Spread, Trunk, Actual_Trunk

## g0805（1 列）
- 見出し：Town
- 例1 値：Swords North | Swords North | Donabate Portra | Donabate Portra | Swords North
  - 同じ表の列：Tree_ID, Tree_Species, Species_Desc, Age_Desc, Height, Spread, Trunk, Actual_Trunk

## g0806（1 列）
- 見出し：Tree_Species
- 例1 値：ACPS | TICO | SOAU | PRCEN | ACPL
  - 同じ表の列：Tree_ID, Town, Species_Desc, Age_Desc, Height, Spread, Trunk, Actual_Trunk

## g0807（1 列）
- 見出し：Species_Desc
- 例1 値：Sorbus aucuparia | Fraxinus excelsior | Tilia cordata 'Greenspire' | Tilia cordata | Sorbus aucuparia
  - 同じ表の列：Tree_ID, Town, Tree_Species, Age_Desc, Height, Spread, Trunk, Actual_Trunk

## g0808（1 列）
- 見出し：Age_Desc
- 例1 値：Young | Semi-Mature | Young | Newly Planted | Young
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Height, Spread, Trunk, Actual_Trunk

## g0809（1 列）
- 見出し：Height
- 例1 値：Up to 5 metres | 5.1-10 metres | Up to 5 metres | 5.1-10 metres | Up to 5 metres
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Age_Desc, Spread, Trunk, Actual_Trunk

## g0810（1 列）
- 見出し：Spread
- 例1 値：Up to 3 metres | 3 to 6 metres | 3 to 6 metres | 3 to 6 metres | Up to 3 metres
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Age_Desc, Height, Trunk, Actual_Trunk

## g0811（1 列）
- 見出し：Trunk
- 例1 値：1cm - 10cm | 1cm - 10cm | 11cm to 20cm | 1cm - 10cm | 11cm to 20cm
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Age_Desc, Height, Spread, Actual_Trunk

## g0812（1 列）
- 見出し：Actual_Trunk
- 例1 値：7cm | 4cm | 13cm | 31cm | 13cm
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Age_Desc, Height, Spread, Trunk

## g0813（1 列）
- 見出し：Condition
- 例1 値：Fair to Good | Good | Good | Good | Good
  - 同じ表の列：Tree_ID, Town, Tree_Species, Species_Desc, Age_Desc, Height, Spread, Trunk

## g0814（2 列）
- 見出し：X
- 例1 値：-9.9385 | -9.98769 | -6.28174 | -7.55491666699993 | -10.0481
  - 同じ表の列：Y, FID, LABEL, ANALYSIS, SAMPLER, DATE_, DESCRIPT, SORTING
- 例2 値：-6.46869438199997 | -6.50668018099998 | -6.56928014199997 | -6.55994417699998 | -6.48859148499997
  - 同じ表の列：Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County

## g0815（2 列）
- 見出し：Y
- 例1 値：54.1505 | 52.3432 | 52.65783 | 51.488316 | 51.8817
  - 同じ表の列：X, FID, LABEL, ANALYSIS, SAMPLER, DATE_, DESCRIPT, SORTING
- 例2 値：52.3419795120001 | 52.501878622 | 52.5204351410001 | 52.395535866 | 52.328807426
  - 同じ表の列：X, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County

## g0816（2 列）
- 見出し：FID
- 例1 値：597 | 551 | 132 | 137 | 949
  - 同じ表の列：X, Y, LABEL, ANALYSIS, SAMPLER, DATE_, DESCRIPT, SORTING
- 例2 値：6 | 7 | 5 | 8 | 4
  - 同じ表の列：X, Y, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County

## g0817（1 列）
- 見出し：LABEL
- 例1 値：IE000455_G1 | IE000268_G38 | IE002262_G4 | IE000697_G3 | IE000472_G42
  - 同じ表の列：X, Y, FID, ANALYSIS, SAMPLER, DATE_, DESCRIPT, SORTING

## g0818（1 列）
- 見出し：ANALYSIS
- 例1 値：PSA | PSA | PSA | PSA | PSA
  - 同じ表の列：X, Y, FID, LABEL, SAMPLER, DATE_, DESCRIPT, SORTING

## g0819（1 列）
- 見出し：SAMPLER
- 例1 値：Day Grab | Day Grab | Day | Day Grab | Day Grab
  - 同じ表の列：X, Y, FID, LABEL, ANALYSIS, DATE_, DESCRIPT, SORTING

## g0820（1 列）
- 見出し：DATE_
- 例1 値：2011-10-11T00:00:00 | 2009-08-14T00:00:00 | 2010-09-16T00:00:00 | 2010-09-02T00:00:00 | 2010-11-19T00:00:00
  - 同じ表の列：X, Y, FID, LABEL, ANALYSIS, SAMPLER, DESCRIPT, SORTING

## g0821（1 列）
- 見出し：DESCRIPT
- 例1 値：Muddy Sand | Muddy Sand | Slightly Fine Gravelly Very Coarse Silt… | Slightly Very Fine Gravelly Fine Sand | Very Fine Gravelly Medium Sand
  - 同じ表の列：X, Y, FID, LABEL, ANALYSIS, SAMPLER, DATE_, SORTING

## g0822（1 列）
- 見出し：SORTING
- 例1 値：Very Poorly Sorted | Moderately Well Sorted | Poorly Sorted | Very Poorly Sorted | Poorly Sorted
  - 同じ表の列：X, Y, FID, LABEL, ANALYSIS, SAMPLER, DATE_, DESCRIPT

## g0823（1 列）
- 見出し：LONG_
- 例1 値：-8.518183 | -9.07345 | -8.3734 | -10.09805 | -7.86747
  - 同じ表の列：X, Y, FID, LABEL, ANALYSIS, SAMPLER, DATE_, DESCRIPT

## g0824（1 列）
- 見出し：Economic sector
- 例1 値：P-Education | B-Mining and quarrying | N-Administrative and support service ac… | S-Other service activities | R-Arts, entertainment and recreation
  - 同じ表の列：unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0825（1 列）
- 見出し：unsafe_
- 例1 値：Crop and animal production, hunting and… | Fishing and aquaculture | Forestry and logging
  - 同じ表の列：Economic sector, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0826（1 列）
- 見出し：unsafe_2015
- 例1 値：1 | 5 | 3 | 1 | 56
  - 同じ表の列：Economic sector, unsafe_, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0827（1 列）
- 見出し：unsafe_2016
- 例1 値：48 | 2 | 1 | 1 | 1
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0828（1 列）
- 見出し：unsafe_2017
- 例1 値：3 | 6 | 25 | 1 | 5
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2018, unsafe_2019, unsafe_2020, unsafe_2021

## g0829（1 列）
- 見出し：unsafe_2018
- 例1 値：2 | 2 | 8 | 39 | 15
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2019, unsafe_2020, unsafe_2021

## g0830（1 列）
- 見出し：unsafe_2019
- 例1 値：2 | 2 | 1 | 3 | 2
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2020, unsafe_2021

## g0831（1 列）
- 見出し：unsafe_2020
- 例1 値：3 | 1 | 4 | 2 | 1
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2021

## g0832（1 列）
- 見出し：unsafe_2021
- 例1 値：2 | 6 | 1 | 10 | 2
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020

## g0833（1 列）
- 見出し：unsafe_2022
- 例1 値：1 | 2 | 14 | 1 | 38
  - 同じ表の列：Economic sector, unsafe_, unsafe_2015, unsafe_2016, unsafe_2017, unsafe_2018, unsafe_2019, unsafe_2020

## g0834（1 列）
- 見出し：Statistic
- 例1 値：Number of new HIV infections | Number of new HIV infections | Number of new HIV infections | Number of new HIV infections | Number of new HIV infections
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, UNIT, VALUE

## g0835（1 列）
- 見出し：C02196V02652
- 例1 値：IE22 | IE11 | IE21 | IE25 | IE23
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, NUTS 3 Regions, UNIT, VALUE

## g0836（1 列）
- 見出し：NUTS 3 Regions
- 例1 値：Midland | South-East | Mid-East | West | Border
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, UNIT, VALUE

## g0837（1 列）
- 見出し：UNIT
- 例1 値：Rate per 1,000 Pop. | Rate per 1,000 Pop. | Rate per 1,000 Pop. | Rate per 1,000 Pop. | Rate per 1,000 Pop.
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, VALUE

## g0838（2 列）
- 見出し：VALUE
- 例1 値：0.05 | 0.05 | 0.12 | 0.03 | 0.05
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02196V02652, NUTS 3 Regions, UNIT
- 例2 値：1453.74 | 1563.06 | 1618.45 | 1525.7 | 1269.14
  - 同じ表の列：Technology, Scenario, Province/Territory, Year, Dollar Year, Field, Unit

## g0839（1 列）
- 見出し：Statistic
- 例1 値：Median number of days | Percentages of In- patients in each reg… | Average number of days | Average number of days | Average number of days
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02842V03416, HSE Regions, UNIT, VALUE

## g0840（1 列）
- 見出し：C02842V03416
- 例1 値：X23 | X06 | X04 | X04 | X04
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, HSE Regions, UNIT, VALUE

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
