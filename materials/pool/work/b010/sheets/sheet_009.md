# ラベル用シート 009 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：pressure__decibars_
- 例1 値：139.6 | 133.4 | 126.1 | 142.4 | 139.1
  - 同じ表の列：SensorTimestamp, conductivity__s_m_, temperature__degree…

## g0962（2 列）
- 見出し：FID
- 例1 値：23 | 27 | 2 | 18 | 3
  - 同じ表の列：X, Y, FID_1, gid, location, senior_sta, junior_sta, status
- 例2 値：5 | 4 | 2 | 6 | 3
  - 同じ表の列：X, Y, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County, Website

## g0963（1 列）
- 見出し：FID_1
- 例1 値：1 | 19 | 28 | 16 | 27
  - 同じ表の列：X, Y, FID, gid, location, senior_sta, junior_sta, status

## g0964（1 列）
- 見出し：gid
- 例1 値：22 | 8 | 35 | 24 | 13
  - 同じ表の列：X, Y, FID, FID_1, location, senior_sta, junior_sta, status

## g0965（1 列）
- 見出し：location
- 例1 値：Firhouse Weir | Thomas Davis GAA Club | St Thomas JNS Jobstown | Collinstown Park Community College | Lucan Harriers Athletic Club
  - 同じ表の列：X, Y, FID, FID_1, gid, senior_sta, junior_sta, status

## g0966（1 列）
- 見出し：senior_sta
- 例1 値：4 | 2 | 5 | 1 | 4
  - 同じ表の列：X, Y, FID, FID_1, gid, location, junior_sta, status

## g0967（1 列）
- 見出し：junior_sta
- 例1 値：1 | 1 | 2 | 1 | 1
  - 同じ表の列：X, Y, FID, FID_1, gid, location, senior_sta, status

## g0968（2 列）
- 見出し：month
- 例1 値：4 | 7 | 12 | 3 | 1
  - 同じ表の列：year, product, tj_ncv
- 例2 値：3 | 5 | 2 | 2 | 8
  - 同じ表の列：Year, logan_passengers, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, unemp_rate, labor_force_part_ra…

## g0969（1 列）
- 見出し：product
- 例1 値：Total of Five Fuels | Road Diesel | Road Diesel | Heating and Other Gas Oil | Road Diesel
  - 同じ表の列：year, month, tj_ncv

## g0970（1 列）
- 見出し：tj_ncv
- 例1 値：10437 | 23520 | 4621 | 2469 | 3433
  - 同じ表の列：year, month, product

## g0971（1 列）
- 見出し：county
- 例1 値：Galway | Cork | Cork | Cork | Dublin
  - 同じ表の列：region, circuit, district_number, court_house, court_house_eircode, active_status

## g0972（1 列）
- 見出し：circuit
- 例1 値：NA | Midland Circuit | NA | South Eastern Circuit | South Western Circuit
  - 同じ表の列：region, county, district_number, court_house, court_house_eircode, active_status

## g0973（1 列）
- 見出し：district_number
- 例1 値：10 | 6 | 12 | DMD | 6
  - 同じ表の列：region, county, circuit, court_house, court_house_eircode, active_status

## g0974（1 列）
- 見出し：court_house
- 例1 値：An Clochan Liath | Strokestown | Monaghan | Trim | Mullingar
  - 同じ表の列：region, county, circuit, district_number, court_house_eircode, active_status

## g0975（1 列）
- 見出し：court_house_eircode
- 例1 値：F94 PDE7 | F94 X263 | A98 WK84 | P36 A660 | V92 P2FE
  - 同じ表の列：region, county, circuit, district_number, court_house, active_status

## g0976（1 列）
- 見出し：active_status
- 例1 値：active | active | active | active | active
  - 同じ表の列：region, county, circuit, district_number, court_house, court_house_eircode

## g0977（1 列）
- 見出し：Prisons
- 例1 値：Number of persons on PSSSO’s in prison … | Number of persons on PSSSO’s in prison … | Number of persons on PSSSO’s in prison … | Total number of persons dealt with over… | Number of persons on PSSSO’s in prison …
  - 同じ表の列：Year, Number

## g0978（1 列）
- 見出し：Administrative_Authority_ID
- 例1 値：23 | 23 | 23 | 23 | 23
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Town, County, Website

## g0979（1 列）
- 見出し：Administrative_Authority
- 例1 値：Wexford County Council | Wexford County Council | Wexford County Council | Wexford County Council | Wexford County Council
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Town, County, Website

## g0980（1 列）
- 見出し：Town
- 例1 値：Bunclody | Enniscorthy | New Ross | Wexford | Wexford
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, County, Website

## g0981（1 列）
- 見出し：County
- 例1 値：County Wexford | County Wexford | County Wexford | County Wexford | County Wexford
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, Website

## g0982（1 列）
- 見出し：Website
- 例1 値：http://www.wexford.ie/wex/Departments/L… | http://www.wexford.ie/wex/Departments/L… | http://www.wexford.ie/wex/Departments/L… | http://www.wexford.ie/wex/Departments/L… | http://www.wexford.ie/wex/Departments/L…
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County

## g0983（1 列）
- 見出し：Opening_Hours_Monday
- 例1 値：09.30 - 13.00 and 14.00 - 17.30 | 10.30am - 5.30pm Closed for lunch 1.00p… | 10.30 - 5.30 Closed for lunch between 1… | 10.30 am - 5.30 pm Closed for lunch 1.0… | 10.30 - 5.30
  - 同じ表の列：X, Y, FID, OBJECTID, Administrative_Auth…, Administrative_Auth…, Town, County

## g0984（1 列）
- 見出し：Settlement_Level
- 例1 値：Level 9 | Level 9 | Level 8 | Level 9 | Level 9
  - 同じ表の列：Area_ha, OBJECTID

## g0985（1 列）
- 見出し：Area_ha
- 例1 値：9.88806882299014 | 5.49756958762557 | 5.23690402167419 | 194.246992995889 | 4.81112681495893
  - 同じ表の列：Settlement_Level, OBJECTID

## g0986（1 列）
- 見出し：Date-Time
- 例1 値：2007-03-27 14:05:00 | 2007-03-27 16:24:00 | 2007-03-27 07:06:00 | 2007-03-27 02:05:00 | 2007-03-27 12:20:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0987（1 列）
- 見出し：UV_Index
- 例1 値：00.04 | 00.03 | 00.34 | 01.27 | 03.70
  - 同じ表の列：Date-Time, Lat, Lon

## g0988（1 列）
- 見出し：location_id
- 例1 値：15650 | 36910 | 36580 | 33220 | 10550
  - 同じ表の列：location_type, metric_id, category, attribute, value

## g0989（1 列）
- 見出し：location_type
- 例1 値：LGA | LGA | LGA | LGA | LGA
  - 同じ表の列：location_id, metric_id, category, attribute, value

## g0990（1 列）
- 見出し：metric_id
- 例1 値：2_101 | 2_108 | 2_108 | 2_107 | 2_103
  - 同じ表の列：location_id, location_type, category, attribute, value

## g0991（1 列）
- 見出し：attribute
- 例1 値：Applications approved ($) | Support received | Disaster Recovery Allowance Eligible | Houses damaged | destroyed | Disaster Recovery Allowance Eligible
  - 同じ表の列：location_id, location_type, metric_id, category, value

## g0992（1 列）
- 見出し：value
- 例1 値：7 | 95 | 0 | 1 | Not active | 10 | 10
  - 同じ表の列：location_id, location_type, metric_id, category, attribute

## g0993（1 列）
- 見出し：weight
- 例1 値：2.1191761 | 2.576493384 | 2.023500793 | 0.923940677 | 2.576493384
  - 同じ表の列：id, SCR1, SCR3, HQGender, hqareatypex, Age Bracket, HQHouseIncome, Q2_A

## g0994（1 列）
- 見出し：SCR1
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：id, weight, SCR3, HQGender, hqareatypex, Age Bracket, HQHouseIncome, Q2_A

## g0995（1 列）
- 見出し：SCR3
- 例1 値：2 | 3 | 2 | 4 | 2
  - 同じ表の列：id, weight, SCR1, HQGender, hqareatypex, Age Bracket, HQHouseIncome, Q2_A

## g0996（1 列）
- 見出し：HQGender
- 例1 値：2 | 1 | 2 | 1 | 1
  - 同じ表の列：id, weight, SCR1, SCR3, hqareatypex, Age Bracket, HQHouseIncome, Q2_A

## g0997（1 列）
- 見出し：hqareatypex
- 例1 値：1 | 1 | 1 | 2 | 1
  - 同じ表の列：id, weight, SCR1, SCR3, HQGender, Age Bracket, HQHouseIncome, Q2_A

## g0998（1 列）
- 見出し：Age Bracket
- 例1 値：7 | 6 | 3 | 4 | 6
  - 同じ表の列：id, weight, SCR1, SCR3, HQGender, hqareatypex, HQHouseIncome, Q2_A

## g0999（1 列）
- 見出し：HQHouseIncome
- 例1 値：8 | 3 | 99 | 3 | 7
  - 同じ表の列：id, weight, SCR1, SCR3, HQGender, hqareatypex, Age Bracket, Q2_A

## g1000（1 列）
- 見出し：Q2_A
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：id, weight, SCR1, SCR3, HQGender, hqareatypex, Age Bracket, HQHouseIncome

## g1001（1 列）
- 見出し：Q2_B
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：id, weight, SCR1, SCR3, HQGender, hqareatypex, Age Bracket, HQHouseIncome

## g1002（2 列）
- 見出し：Date
- 例1 値：2018-01-03 | 2018-01-06 | 2018-01-02 | 2018-01-03 | 2018-01-04
  - 同じ表の列：Region, Mode, Sum of Volume
- 例2 値：2018-10-01 | 2018-10-01 | 2018-10-01 | 2018-10-01 | 2018-10-01
  - 同じ表の列：Acronym_EN, Services, Results, Scores

## g1003（1 列）
- 見出し：Region
- 例1 値：Québec Region | Atlantic Region | Northern Ontario Region | Prairie Region | Atlantic Region
  - 同じ表の列：Date, Mode, Sum of Volume

## g1004（1 列）
- 見出し：Mode
- 例1 値：Land | Land | Land | Land | Land
  - 同じ表の列：Date, Region, Sum of Volume

## g1005（1 列）
- 見出し：Sum of Volume
- 例1 値：272 | 61 | 1033 | 529 | 800
  - 同じ表の列：Date, Region, Mode

## g1006（1 列）
- 見出し：Colonne
- 例1 値：Scénario | Année | Type | Variable | Valeur
  - 同じ表の列：Valeur des donnees …

## g1007（1 列）
- 見出し：Valeur des donnees ou titre de colonne
- 例1 値：Utilisation finale | Néant | Total | Titre de la colonne | Métallurgique
  - 同じ表の列：Colonne

## g1008（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：CFP2017-0001 | CFP2017-0001 | CFP2017-0001 | CFP2017-0001 | CFP2017-0001
  - 同じ表の列：Region - Region, Commodity, denree, Function, Fonction, Origin, Origine, Product

## g1009（1 列）
- 見出し：Region - Region
- 例1 値：ONTARIO | ONTARIO | ONTARIO | ONTARIO | ONTARIO
  - 同じ表の列：Sample No. - No. d'…, Commodity, denree, Function, Fonction, Origin, Origine, Product

## g1010（1 列）
- 見出し：Commodity
- 例1 値：IMFD | IMFD | IMFD | IMFD | IMFD
  - 同じ表の列：Sample No. - No. d'…, Region - Region, denree, Function, Fonction, Origin, Origine, Product

## g1011（1 列）
- 見出し：denree
- 例1 値：DAIM | DAIM | DAIM | DAIM | DAIM
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, Function, Fonction, Origin, Origine, Product

## g1012（2 列）
- 見出し：Function
- 例1 値：Import | Import | Import | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Fonction, Origin, Origine, Product
- 例2 値：Create | Create | Create | Create | Create
  - 同じ表の列：SSTS Confirmation N…, Serial No., Transaction Source, Category on Report …, Date Entered into S…, Transaction Date

## g1013（1 列）
- 見出し：Fonction
- 例1 値：importé | importé | importé | importé | importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Origin, Origine, Product

## g1014（1 列）
- 見出し：Origin
- 例1 値：POLAND | POLAND | POLAND | POLAND | POLAND
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origine, Product

## g1015（1 列）
- 見出し：Origine
- 例1 値：POLOGNE | POLOGNE | POLOGNE | POLOGNE | POLOGNE
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Product

## g1016（1 列）
- 見出し：Product
- 例1 値：Infant Food - Cereal | Infant Food - Cereal | Infant Food - Cereal | Infant Food - Cereal | Infant Food - Cereal
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Origine

## g1017（1 列）
- 見出し：Produit
- 例1 値：Céréales - Nourrissons | Céréales - Nourrissons | Céréales - Nourrissons | Céréales - Nourrissons | Céréales - Nourrissons
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Commodity, denree, Function, Fonction, Origin, Origine

## g1018（1 列）
- 見出し：SSTS Confirmation No.
- 例1 値：1020000493706 | 1020000353301 | 1020000437578 | 1020000456921 | 1020000405821
  - 同じ表の列：Serial No., Transaction Source, Function, Category on Report …, Date Entered into S…, Transaction Date

## g1019（1 列）
- 見出し：Serial No.
- 例1 値：NFA143 | CC388 | BW692 | NFC119 | BV781
  - 同じ表の列：SSTS Confirmation N…, Transaction Source, Function, Category on Report …, Date Entered into S…, Transaction Date

## g1020（1 列）
- 見出し：Transaction Source
- 例1 値：Online | Online | Online | Online | Online
  - 同じ表の列：SSTS Confirmation N…, Serial No., Function, Category on Report …, Date Entered into S…, Transaction Date

## g1021（1 列）
- 見出し：Category on Report Date
- 例1 値：1 | 2 | 2 | 2 | 2
  - 同じ表の列：SSTS Confirmation N…, Serial No., Transaction Source, Function, Date Entered into S…, Transaction Date

## g1022（1 列）
- 見出し：Date Entered into System
- 例1 値：1/31/2017 | 5/12/2017 | 10/26/2017 | 3/30/2017 | 10/26/2017
  - 同じ表の列：SSTS Confirmation N…, Serial No., Transaction Source, Function, Category on Report …, Transaction Date

## g1023（1 列）
- 見出し：Transaction Date
- 例1 値：10/25/2017 | 3/23/2017 | 2/23/2017 | 5/12/2017 | 6/1/2017
  - 同じ表の列：SSTS Confirmation N…, Serial No., Transaction Source, Function, Category on Report …, Date Entered into S…

## g1024（1 列）
- 見出し：Jurisdiction
- 例1 値：Manitoba | Multi-Jurisdiction | Quebec | Northwest Territories | Nunavut
  - 同じ表の列：2019, 2020, 2021, 2022, 2023, 2024

## g1025（2 列）
- 見出し：2019
- 例1 値：383250 | 44780 | 366110 | 2551880 | 1005120
  - 同じ表の列：Jurisdiction, 2020, 2021, 2022, 2023, 2024
- 例2 値：203 | 529 | 1272 | 852 | 35
  - 同じ表の列：Age_Group, Gender, 2012, 2013, 2014, 2015, 2016, 2017

## g1026（1 列）
- 見出し：2020
- 例1 値：45710 | 515390 | 650 | 65580 | 34170
  - 同じ表の列：Jurisdiction, 2019, 2021, 2022, 2023, 2024

## g1027（1 列）
- 見出し：2021
- 例1 値：68280 | 47220 | 2728060 | 9180 | 19390
  - 同じ表の列：Jurisdiction, 2019, 2020, 2022, 2023, 2024

## g1028（1 列）
- 見出し：2022
- 例1 値：377500 | 12320 | 74960 | 19220 | 557720
  - 同じ表の列：Jurisdiction, 2019, 2020, 2021, 2023, 2024

## g1029（1 列）
- 見出し：2023
- 例1 値：2550 | 382440 | 36490 | 1169700 | 75610
  - 同じ表の列：Jurisdiction, 2019, 2020, 2021, 2022, 2024

## g1030（1 列）
- 見出し：2024
- 例1 値：36160 | 18120 | 75000 | 379870 | 428300
  - 同じ表の列：Jurisdiction, 2019, 2020, 2021, 2022, 2023

## g1031（1 列）
- 見出し：City
- 例1 値：Wemindji | Pinawa | Chetwynd | Back | Athabasca
  - 同じ表の列：Province/Territory …, University, Project, Instrument

## g1032（1 列）
- 見出し：Province/Territory code
- 例1 値：NU | SK | NU | AB | NU
  - 同じ表の列：City, University, Project, Instrument

## g1033（1 列）
- 見出し：University
- 例1 値：Universit‚ de l'Alberta | Universit‚ du Nouveau-Brunswick | Universit‚ de l'Alberta | Universit‚ de l'Alberta | Universit‚ de l'Alberta
  - 同じ表の列：City, Province/Territory …, Project, Instrument

## g1034（1 列）
- 見出し：Project
- 例1 値：CARISMA | CARISMA | ABOVE | RIO | AIM
  - 同じ表の列：City, Province/Territory …, University, Instrument

## g1035（1 列）
- 見出し：Instrument
- 例1 値：Imageur tout-ciel | Ionosonde digitale | Imageur tout-ciel | FESOÿ | Interf‚romŠtre Fabry-Perot
  - 同じ表の列：City, Province/Territory …, University, Project

## g1036（1 列）
- 見出し：Employment Equity (EE) groups / Official Languages
- 例1 値：Équité en matière d’emploi / Langues of… | Persons from Racialized or Ethnic group… | First Official Language UNKNOWN / Premi… | Indigenous peoples / Populations autoch… | -Please note that employees can identif…
  - 同じ表の列：% of Identifying Em…

## g1037（1 列）
- 見出し：% of Identifying Employees
- 例1 値：76.10% | % d'Identification des employés | 2.40% | 32.10% | 0.10%
  - 同じ表の列：Employment Equity (…

## g1038（1 列）
- 見出し：GC_HIST_ID
- 例1 値：1005710 | 1010010 | 1001409 | 1007510 | 1027510
  - 同じ表の列：GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1039（1 列）
- 見出し：GC_ID
- 例1 値：10185 | 10166 | 10085 | 10265 | 10200
  - 同じ表の列：GC_HIST_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1040（1 列）
- 見出し：GC_NM_OFF_EN
- 例1 値：the Republic of the Congo | the Republic of Korea | Democratic Republic of Congo | the Territory of Wallis and Futuna Isla… | the Grand Duchy of Luxembourg
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1041（1 列）
- 見出し：GC_NM_OFF_FR
- 例1 値：Îles Midway | la République de Guinée-Bissau | la République du Chili | la République du Pérou | la République du Nicaragua
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1042（1 列）
- 見出し：GC_NM_AB_EN
- 例1 値：Jordan | San Marino | Cabo Verde | Djibouti | Cameroon
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1043（1 列）
- 見出し：GC_NM_AB_FR
- 例1 値：Hong Kong | Saint-Martin | Antigua | Salvador | Irlande
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, STAT_CD, STAT_DESC_EN, STAT_DESC_FR

## g1044（1 列）
- 見出し：STAT_CD
- 例1 値：1 | 2 | 1 | 1 | 2
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_DESC_EN, STAT_DESC_FR

## g1045（1 列）
- 見出し：STAT_DESC_EN
- 例1 値：INACTIVE | ACTIVE | ACTIVE | ACTIVE | INACTIVE
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_FR

## g1046（1 列）
- 見出し：STAT_DESC_FR
- 例1 値：ACTIF | ACTIF | INACTIF | ACTIF | ACTIF
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN

## g1047（1 列）
- 見出し：TYPE_CD
- 例1 値：5 | 1 | 6 | 1 | 1
  - 同じ表の列：GC_HIST_ID, GC_ID, GC_NM_OFF_EN, GC_NM_OFF_FR, GC_NM_AB_EN, GC_NM_AB_FR, STAT_CD, STAT_DESC_EN

## g1048（1 列）
- 見出し：ACCENTESTAR
- 例1 値：ESTAR | ESTAR | ESTAR | ESTAR | ESTAR
  - 同じ表の列：ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1049（1 列）
- 見出し：ACMODELNUMBER
- 例1 値：MXZ-2C20NAHZ4,MSZ-GS12NA | MLAO12S4S-1P / MWMAO12S4 | 25HPB624A300 | D5CSHAH12AAK, D5FSHAH12XAK | 38GP036330
  - 同じ表の列：ACCENTESTAR, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1050（1 列）
- 見出し：ACWINDESTAR
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1051（1 列）
- 見出し：ACWINDNUM
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, AHRI, AIR50P, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1052（1 列）
- 見出し：AHRI
- 例1 値：210448841 | 8849330 | 215864380 | 0 | 0
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AIR50P, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1053（1 列）
- 見出し：AIR50P
- 例1 値：2.9703 | 2.9392 | 4.3442 | 2.8321 | 4.2439
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIRCONDTYPE, AIRCOP, ASHPHSPF

## g1054（1 列）
- 見出し：AIRCONDTYPE
- 例1 値：Not installed | Mini-split ductless | Central split system | Ductless Mini- or Multi-split system | Mini-split ductless
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCOP, ASHPHSPF

## g1055（1 列）
- 見出し：AIRCOP
- 例1 値：0.0 | 0.0 | 2.578 | 2.578 | 2.76
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, ASHPHSPF

## g1056（1 列）
- 見出し：ASHPHSPF
- 例1 値：0.0 | 0.0 | 0.0 | 5.0 | 0.0
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, AIRCOP

## g1057（1 列）
- 見出し：ASHPHSPF2
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：ACCENTESTAR, ACMODELNUMBER, ACWINDESTAR, ACWINDNUM, AHRI, AIR50P, AIRCONDTYPE, AIRCOP

## g1058（1 列）
- 見出し：ythWIC Job Location Snapshot ID
- 例1 値：15835329 | 15774648 | 15767359 | 15765648 | 15783550
  - 同じ表の列：Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Official Language, Education LOS

## g1059（1 列）
- 見出し：Job Title
- 例1 値：administrative assistant | home support worker | alarm system technician | sprinkler system installer apprentice | nursing services aide
  - 同じ表の列：ythWIC Job Location…, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Official Language, Education LOS

## g1060（1 列）
- 見出し：Original Job Title
- 例1 値：NA | JOURNEYMEN Electrician | Part Time Cleaner | NA | NA
  - 同じ表の列：ythWIC Job Location…, Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Official Language, Education LOS

## g1061（1 列）
- 見出し：NOC 2016 Code
- 例1 値：6733 | 6711 | 6211 | 7321 | 7322
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC21 Code, External Indicator, Vacancy Count, Official Language, Education LOS

## g1062（1 列）
- 見出し：NOC21 Code
- 例1 値：62024 | 60031 | 43100 | 13111 | 33102
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, External Indicator, Vacancy Count, Official Language, Education LOS

## g1063（1 列）
- 見出し：External Indicator
- 例1 値：1 | 1 | 0 | 1 | 0
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, Vacancy Count, Official Language, Education LOS

## g1064（1 列）
- 見出し：Vacancy Count
- 例1 値：1 | 1 | 1 | 1 | 8
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Official Language, Education LOS

## g1065（1 列）
- 見出し：Official Language
- 例1 値：English or French | English | English | English | French
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Education LOS

## g1066（1 列）
- 見出し：Education LOS
- 例1 値：College/CEGEP | NA | NA | No degree, certificate or diploma | Secondary (high) school graduation cert…
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Official Language

## g1067（1 列）
- 見出し：Experience Level
- 例1 値：No experience | NA | NA | NA | No experience
  - 同じ表の列：ythWIC Job Location…, Job Title, Original Job Title, NOC 2016 Code, NOC21 Code, External Indicator, Vacancy Count, Official Language

## g1068（1 列）
- 見出し：NL (millions of dollars)
- 例1 値：65 | 76 | 0 | 0 | 102
  - 同じ表の列：Year, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1069（1 列）
- 見出し：PE (millions of dollars)
- 例1 値：38 | 18 | 0 | 0 | 0
  - 同じ表の列：Year, NL (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1070（1 列）
- 見出し：NS (millions of dollars)
- 例1 値：0 | 244 | 0 | 0 | 267
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1071（1 列）
- 見出し：NB (millions of dollars)
- 例1 値：0 | 137 | 161 | 80 | 204
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1072（1 列）
- 見出し：QC (millions of dollars)
- 例1 値：0 | 1,374 | 0 | 0 | 1,740
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, ON (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1073（1 列）
- 見出し：ON (millions of dollars)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, MB (millions of dol…, SK (millions of dol…

## g1074（1 列）
- 見出し：MB (millions of dollars)
- 例1 値：263 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, SK (millions of dol…

## g1075（1 列）
- 見出し：SK (millions of dollars)
- 例1 値：0 | 0 | 0 | 0 | 157
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…

## g1076（1 列）
- 見出し：AL (millions of dollars)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, NL (millions of dol…, PE (millions of dol…, NS (millions of dol…, NB (millions of dol…, QC (millions of dol…, ON (millions of dol…, MB (millions of dol…

## g1077（1 列）
- 見出し：year_month
- 例1 値：2021-10 | 2026-01 | 2024-04 | 2025-12 | 2022-05
  - 同じ表の列：product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## g1078（1 列）
- 見出し：product_type
- 例1 値：edible cannabis / cannabis comestible | edible cannabis / cannabis comestible | edible cannabis / cannabis comestible | cannabis extracts / extraits de cannabis | edible cannabis / cannabis comestible
  - 同じ表の列：year_month, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## g1079（1 列）
- 見出し：unpackaged_inventory_units
- 例1 値：2813991 | n/a / n/d | 2,486,045 | n/a / n/d | n/a / n/d
  - 同じ表の列：year_month, product_type, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## g1080（1 列）
- 見出し：packaged_production_units
- 例1 値：571 | 4219227 | 4,183,514 | 35794 | 14353
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## 答えの雛形

```
g0961	
g0962	
g0963	
g0964	
g0965	
g0966	
g0967	
g0968	
g0969	
g0970	
g0971	
g0972	
g0973	
g0974	
g0975	
g0976	
g0977	
g0978	
g0979	
g0980	
g0981	
g0982	
g0983	
g0984	
g0985	
g0986	
g0987	
g0988	
g0989	
g0990	
g0991	
g0992	
g0993	
g0994	
g0995	
g0996	
g0997	
g0998	
g0999	
g1000	
g1001	
g1002	
g1003	
g1004	
g1005	
g1006	
g1007	
g1008	
g1009	
g1010	
g1011	
g1012	
g1013	
g1014	
g1015	
g1016	
g1017	
g1018	
g1019	
g1020	
g1021	
g1022	
g1023	
g1024	
g1025	
g1026	
g1027	
g1028	
g1029	
g1030	
g1031	
g1032	
g1033	
g1034	
g1035	
g1036	
g1037	
g1038	
g1039	
g1040	
g1041	
g1042	
g1043	
g1044	
g1045	
g1046	
g1047	
g1048	
g1049	
g1050	
g1051	
g1052	
g1053	
g1054	
g1055	
g1056	
g1057	
g1058	
g1059	
g1060	
g1061	
g1062	
g1063	
g1064	
g1065	
g1066	
g1067	
g1068	
g1069	
g1070	
g1071	
g1072	
g1073	
g1074	
g1075	
g1076	
g1077	
g1078	
g1079	
g1080	
```
