# ラベル用シート 009 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：Buses (billion passenger kilometres)
- 例1 値：19.24 | 17.84 | 17.35 | 19.93 | 20.41
  - 同じ表の列：Financial year, Passenger cars (bil…, Rail (billion passe…, Air (billion passen…, Other (billion pass…, Total (billion pass…

## g0962（1 列）
- 見出し：Rail (billion passenger kilometres)
- 例1 値：11.86 | 14.77 | 16.15 | 12.97 | 11.98
  - 同じ表の列：Financial year, Passenger cars (bil…, Buses (billion pass…, Air (billion passen…, Other (billion pass…, Total (billion pass…

## g0963（1 列）
- 見出し：Air (billion passenger kilometres)
- 例1 値：70.86 | 71.44 | 53.01 | 69.67 | 35.68
  - 同じ表の列：Financial year, Passenger cars (bil…, Buses (billion pass…, Rail (billion passe…, Other (billion pass…, Total (billion pass…

## g0964（1 列）
- 見出し：Other (billion passenger kilometres)
- 例1 値：43.67 | 28.9 | 27.89 | 38.27 | 27.6
  - 同じ表の列：Financial year, Passenger cars (bil…, Buses (billion pass…, Rail (billion passe…, Air (billion passen…, Total (billion pass…

## g0965（1 列）
- 見出し：Total (billion passenger kilometres)
- 例1 値：425.8 | 395.01 | 368.15 | 389.36 | 334.26
  - 同じ表の列：Financial year, Passenger cars (bil…, Buses (billion pass…, Rail (billion passe…, Air (billion passen…, Other (billion pass…

## g0966（1 列）
- 見出し：UID
- 例1 値：23 | 39 | 37 | 10 | 48
  - 同じ表の列：TYPE, DESC, Location, Road, IMAGE, LAT, LON

## g0967（1 列）
- 見出し：TYPE
- 例1 値：Green Metal Cylinder | Green Metal Cylinder | Green Metal Cylinder | Green Metal Cylinder | Green Metal Cylinder
  - 同じ表の列：UID, DESC, Location, Road, IMAGE, LAT, LON

## g0968（1 列）
- 見出し：DESC
- 例1 値：Ken Harrison Reserve Entrance Fence | East Lake Drive | Steggall Park Footpath | Off-Leash Dog Park - East | Coles Entrance/Exit
  - 同じ表の列：UID, TYPE, Location, Road, IMAGE, LAT, LON

## g0969（1 列）
- 見出し：Road
- 例1 値：Parkside Avenue | Ken Harrison Reserve Access | East Lake Drive | Campbell Street | Naretha Street
  - 同じ表の列：UID, TYPE, DESC, Location, IMAGE, LAT, LON

## g0970（1 列）
- 見出し：IMAGE
- 例1 値：https://qgis-swanhillvicgovau.msappprox… | https://qgis-swanhillvicgovau.msappprox… | https://qgis-swanhillvicgovau.msappprox… | https://qgis-swanhillvicgovau.msappprox… | https://qgis-swanhillvicgovau.msappprox…
  - 同じ表の列：UID, TYPE, DESC, Location, Road, LAT, LON

## g0971（1 列）
- 見出し：Grant Program
- 例1 値：Community Grants | Economic Activation Partnership | Social Grants and Partnerships | Economic Grants and Partnerships | Social Grants and Partnerships
  - 同じ表の列：Decision, Decision Date, Project Title, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…, Economic Priority

## g0972（1 列）
- 見出し：Decision
- 例1 値：Approved | Approved | Approved | Approved | Approved
  - 同じ表の列：Grant Program, Decision Date, Project Title, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…, Economic Priority

## g0973（1 列）
- 見出し：Decision Date
- 例1 値：30/01/2024 | 2024-05-10 00:00:00 | 09/08/2023 | 2024-06-06 00:00:00 | 22/06/2022
  - 同じ表の列：Grant Program, Decision, Project Title, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…, Economic Priority

## g0974（1 列）
- 見出し：Project Title
- 例1 値：2025 Townsville NAIDOC Week Events | Townsville Dragon Boat Club Inc. Regatt… | Townsville Regatta | Pre Loved Gifts Community Event | TheatreiNQ Operational
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…, Economic Priority

## g0975（1 列）
- 見出し：Project Start Date
- 例1 値：2026-04-17 00:00:00 | 10/12/2023 | 2026-08-15 00:00:00 | 19/09/2020 | 26/10/2019
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Location Su…, Social Priority, Environmental Prior…, Economic Priority

## g0976（1 列）
- 見出し：Project Location Suburb
- 例1 値：North Ward | Annandale | Townsville City | South Townsville | Idalia
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Start Date, Social Priority, Environmental Prior…, Economic Priority

## g0977（1 列）
- 見出し：Social Priority
- 例1 値：Support multicultural diversity and com… | Support multicultural diversity and com… | Develop healthy and active lifestyles | Grow the capacity of Townsville through… | Support multicultural diversity and com…
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Start Date, Project Location Su…, Environmental Prior…, Economic Priority

## g0978（1 列）
- 見出し：Environmental Priority
- 例1 値：Building capacity in local sustainabili… | Ecological landscape restoration | Building capacity in local sustainabili… | Building capacity in local sustainabili… | Building capacity in local sustainabili…
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Start Date, Project Location Su…, Social Priority, Economic Priority

## g0979（1 列）
- 見出し：Economic Priority
- 例1 値：Placemaking - enliven the CBD through a… | Tourism and events - establish new tour… | Tourism and events - establish new tour… | Tourism and events - establish new tour… | Tourism and events - establish new tour…
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…

## g0980（1 列）
- 見出し：Total Allocated
- 例1 値：2113 | 16394.4 | 846.81 | 4900 | 8131.94
  - 同じ表の列：Grant Program, Decision, Decision Date, Project Title, Project Start Date, Project Location Su…, Social Priority, Environmental Prior…

## g0981（1 列）
- 見出し：NSW
- 例1 値：6.94746445983 | 6.95109695962 | 9.52402913754 | 4.91812074048 | 6.39743089915
  - 同じ表の列：Vic, Qld, SA, WA, Tas, NT, ACT, Total

## g0982（1 列）
- 見出し：Vic
- 例1 値：2.5406504065040649287254836963256821036… | 8.2406828341787683456232116441242396831… | 12.720685716468734582917932129930704832… | 1.8197137099576123908661884343018755316… | 6.9201236884163712659301381791010499000…
  - 同じ表の列：NSW, Qld, SA, WA, Tas, NT, ACT, Total

## g0983（1 列）
- 見出し：Qld
- 例1 値：7.13474241409546 | 7.212091616942713 | 7.456978006409691 | 3.341650389318492 | 8.808711572070944
  - 同じ表の列：NSW, Vic, SA, WA, Tas, NT, ACT, Total

## g0984（1 列）
- 見出し：SA
- 例1 値：5.472456087867003 | 4.813239882046242 | 4.543486642588557 | 5.382708662763366 | 7.422464203691363
  - 同じ表の列：NSW, Vic, Qld, WA, Tas, NT, ACT, Total

## g0985（1 列）
- 見出し：WA
- 例1 値：11.67732935161845 | 5.642419532020026 | 4.332006130893713 | 5.322657719032923 | 3.5152773013646885
  - 同じ表の列：NSW, Vic, Qld, SA, Tas, NT, ACT, Total

## g0986（1 列）
- 見出し：Tas
- 例1 値：7.644875283435677 | 15.61386670442863 | 14.784281156648863 | 9.285714285714286 | 5.585652477700399
  - 同じ表の列：NSW, Vic, Qld, SA, WA, NT, ACT, Total

## g0987（1 列）
- 見出し：NT
- 例1 値：3.601857278095839 | 2.731795603891787 | 2.6642023170896634 | 4.6270089552915 | 3.22318892845873
  - 同じ表の列：NSW, Vic, Qld, SA, WA, Tas, ACT, Total

## g0988（1 列）
- 見出し：ACT
- 例1 値：6.835790864948436 | 4.960926830661981 | 7.082654781291963 | 0.0914259592583069 | 10.311601807697782
  - 同じ表の列：NSW, Vic, Qld, SA, WA, Tas, NT, Total

## g0989（1 列）
- 見出し：Total
- 例1 値：12.900404685913758 | 2.605842354517851 | 4.883031346330139 | 6.142631957471199 | 7.279389956195588
  - 同じ表の列：NSW, Vic, Qld, SA, WA, Tas, NT, ACT

## g0990（1 列）
- 見出し：Road_Section_Id
- 例1 値：1000 | 1000 | 1000 | 1000 | 1000
  - 同じ表の列：Carriageway_Code, Tdist_Start, AADT, AADT_Intervention_C…

## g0991（1 列）
- 見出し：Carriageway_Code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Road_Section_Id, Tdist_Start, AADT, AADT_Intervention_C…

## g0992（1 列）
- 見出し：Tdist_Start
- 例1 値：6.730 | 1.740 | 6.950 | 3.680 | 8.130
  - 同じ表の列：Road_Section_Id, Carriageway_Code, AADT, AADT_Intervention_C…

## g0993（1 列）
- 見出し：AADT
- 例1 値：2130 | 2130 | 2130 | 2130 | 2130
  - 同じ表の列：Road_Section_Id, Carriageway_Code, Tdist_Start, AADT_Intervention_C…

## g0994（1 列）
- 見出し：AADT_Intervention_Category
- 例1 値：Cat C | Cat C | Cat C | Cat C | Cat C
  - 同じ表の列：Road_Section_Id, Carriageway_Code, Tdist_Start, AADT

## g0995（1 列）
- 見出し：siteid
- 例1 値：21 | 21 | 7 | 5 | 10
  - 同じ表の列：site, Date, EC, DO (%), Turbidity (NTU), Temperature (degC), pH, Water Condition

## g0996（1 列）
- 見出し：site
- 例1 値：Mackenzie River @ Mt Victory Rd | Glenlofty Creek @ U/S Glenlofty gauge | Mackenzie River @ Mt Victory Rd | Concongella Creek @ Donald Rd | Heiffer Station Creek @ Landsborough We…
  - 同じ表の列：siteid, Date, EC, DO (%), Turbidity (NTU), Temperature (degC), pH, Water Condition

## g0997（1 列）
- 見出し：Date
- 例1 値：2013-02-19 00:00:00 | 2020-12-16 00:00:00 | 2019-07-29 00:00:00 | 2017-05-09 00:00:00 | 2011-08-30 00:00:00
  - 同じ表の列：siteid, site, EC, DO (%), Turbidity (NTU), Temperature (degC), pH, Water Condition

## g0998（1 列）
- 見出し：EC
- 例1 値：90 | 93 | 135.5 | 153 | 5340
  - 同じ表の列：siteid, site, Date, DO (%), Turbidity (NTU), Temperature (degC), pH, Water Condition

## g0999（1 列）
- 見出し：DO (%)
- 例1 値：99 | 42.9 | 27.2 | 85.6 | 20.4
  - 同じ表の列：siteid, site, Date, EC, Turbidity (NTU), Temperature (degC), pH, Water Condition

## g1000（1 列）
- 見出し：Turbidity (NTU)
- 例1 値：2 | 151 | 500 | 99.8 | 6.1
  - 同じ表の列：siteid, site, Date, EC, DO (%), Temperature (degC), pH, Water Condition

## g1001（1 列）
- 見出し：Temperature (degC)
- 例1 値：18.71 | 9.65 | 16.4 | 13.68 | 9.01
  - 同じ表の列：siteid, site, Date, EC, DO (%), Turbidity (NTU), pH, Water Condition

## g1002（1 列）
- 見出し：pH
- 例1 値：5.13 | 5.99 | 5.14 | 7.58 | 6.5
  - 同じ表の列：siteid, site, Date, EC, DO (%), Turbidity (NTU), Temperature (degC), Water Condition

## g1003（1 列）
- 見出し：Water Condition
- 例1 値：Medium Flow | Medium Flow | Medium Flow | Low Flow | Medium Flow
  - 同じ表の列：siteid, site, Date, EC, DO (%), Turbidity (NTU), Temperature (degC), pH

## g1004（1 列）
- 見出し：None
- 例1 値：DO issues | Trouble with DO calibration
  - 同じ表の列：siteid, site, Date, EC, DO (%), Turbidity (NTU), Temperature (degC), pH

## g1005（1 列）
- 見出し：Category
- 例1 値：Indigenous | Relationships | Health and Wellbeing | Health and Wellbeing | Legal
  - 同じ表の列：Keywords, Suburb, State, Fax, Hours 1, Hours 2

## g1006（1 列）
- 見出し：Keywords
- 例1 値：community centre, social activities, re… | breastfeeding, parenting | community centre, accommodation, legal … | family counselling, children, child abu… | family counselling, family support, gro…
  - 同じ表の列：Category, Suburb, State, Fax, Hours 1, Hours 2

## g1007（1 列）
- 見出し：Fax
- 例1 値：07 3857 1953 | 02 9577 3355 | 07 4157 3937 | 07 4984 8188 | 07 3839 2000
  - 同じ表の列：Category, Keywords, Suburb, State, Hours 1, Hours 2

## g1008（1 列）
- 見出し：Hours 1
- 例1 値：Mon-Fri 9am-3pm | Mon-Fri 8.30am-5pm | Mon-Thurs 9am-5pm | Mon-Fri 8am-5 pm | Mon -Thur 8am-5pm
  - 同じ表の列：Category, Keywords, Suburb, State, Fax, Hours 2

## g1009（1 列）
- 見出し：Hours 2
- 例1 値：Tues-Wed 9am-7pm | Thurs 8am-2.30pm | Wed 1pm-5pm | Wed 11am-4pm | Fri 8:30am-4:00pm
  - 同じ表の列：Category, Keywords, Suburb, State, Fax, Hours 1

## g1010（1 列）
- 見出し：reporting_year
- 例1 値：2024-25 | 2024-25 | 2024-25 | 2024-25 | 2024-25
  - 同じ表の列：employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group, anzsic_class

## g1011（1 列）
- 見出し：employer_abn
- 例1 値：95003777259 | 24450502757 | 16293921492 | 49671903923 | 23665834935
  - 同じ表の列：reporting_year, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group, anzsic_class

## g1012（1 列）
- 見出し：is_relevant_employer
- 例1 値：TRUE | TRUE | TRUE | TRUE | TRUE
  - 同じ表の列：reporting_year, employer_abn, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group, anzsic_class

## g1013（1 列）
- 見出し：employer_size
- 例1 値：<250 | <250 | 500- 999 | 500- 999 | 250- 499
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group, anzsic_class

## g1014（1 列）
- 見出し：anzsic_code
- 例1 値：6419 | 3734 | 0809 | 8601 | 7212
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_division, anzsic_subdivision, anzsic_group, anzsic_class

## g1015（1 列）
- 見出し：anzsic_division
- 例1 値：Other Services | Education and Training | Construction | Manufacturing | Health Care and Social Assistance
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_subdivision, anzsic_group, anzsic_class

## g1016（1 列）
- 見出し：anzsic_subdivision
- 例1 値：Basic Material Wholesaling | Forestry and Logging | Preschool and School Education | Machinery and Equipment Wholesaling | Machinery and Equipment Wholesaling
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_group, anzsic_class

## g1017（1 列）
- 見出し：anzsic_group
- 例1 値：Grocery, Liquor and Tobacco Product Who… | Other Mining Support Services | Specialised Machinery and Equipment Man… | Computer System Design and Related Serv… | Building Cleaning, Pest Control and Gar…
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_class

## g1018（1 列）
- 見出し：anzsic_class
- 例1 値：Paint and Coatings Manufacturing | Computer System Design and Related Serv… | Freight Forwarding Services | Furniture and Floor Covering Wholesaling | Other Information Services
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group

## g1019（1 列）
- 見出し：section
- 例1 値：Action on gender equality | Action on gender equality | Action on gender equality | Action on gender equality | Action on gender equality
  - 同じ表の列：reporting_year, employer_abn, is_relevant_employer, employer_size, anzsic_code, anzsic_division, anzsic_subdivision, anzsic_group

## g1020（1 列）
- 見出し：unsafe_
- 例1 値：Q4 2022 | Q3 2022 | Longitutde | Q1 2022 | Q2 2022
  - 同じ表の列：Achill, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan, Kenmare Bay

## g1021（1 列）
- 見出し：Achill
- 例1 値：-10.11586497 | 53.99309071 | 0.4
  - 同じ表の列：unsafe_, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan, Kenmare Bay

## g1022（1 列）
- 見出し：Bannow
- 例1 値：-6.780104772 | 1.9 | 1.9 | 52.20443825
  - 同じ表の列：unsafe_, Achill, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan, Kenmare Bay

## g1023（1 列）
- 見出し：Bantry Bay
- 例1 値：51.65463193 | -9.711088042
  - 同じ表の列：unsafe_, Achill, Bannow, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan, Kenmare Bay

## g1024（1 列）
- 見出し：Carlingford
- 例1 値：0.05 | -6.174466915 | 0.03 | 0.4 | 54.04455017
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Castlemaine Harbour, Clew Bay, Dungarvan, Kenmare Bay

## g1025（1 列）
- 見出し：Castlemaine Harbour
- 例1 値：52.1268566 | 5 | -9.931539485
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Carlingford, Clew Bay, Dungarvan, Kenmare Bay

## g1026（1 列）
- 見出し：Clew Bay
- 例1 値：-9.798798405 | 53.83333201 | 0.22 | 1.8 | 0.1
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Dungarvan, Kenmare Bay

## g1027（1 列）
- 見出し：Dungarvan
- 例1 値：52.08518503 | 1.8 | 1.89 | 1.68 | 0.4
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Kenmare Bay

## g1028（1 列）
- 見出し：Kenmare Bay
- 例1 値：-9.720997067 | 51.8486 | 5 | 0.8
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan

## g1029（1 列）
- 見出し：Killary
- 例1 値：6 | 53.63269065 | -9.892399683
  - 同じ表の列：unsafe_, Achill, Bannow, Bantry Bay, Carlingford, Castlemaine Harbour, Clew Bay, Dungarvan

## g1030（1 列）
- 見出し：obs__status
- 例1 値：A | A | A | A | A
  - 同じ表の列：Date, Value, obs__conf_, Series key, Title complement, Decimals, Units, Issuance Type

## g1031（1 列）
- 見出し：obs__conf_
- 例1 値：F | F | F | F | F
  - 同じ表の列：Date, Value, obs__status, Series key, Title complement, Decimals, Units, Issuance Type

## g1032（1 列）
- 見出し：Series key
- 例1 値：CSEC.M.N.IE.W0.S122.S1.N.L.LE.F3C.L._Z.… | CSEC.M.N.IE.W0.S127.S1.N.L.LE.F3C.L._Z.… | CSEC.M.N.IE.W0.S12Q.S1.N.L.F.F3VR.L._Z.… | CSEC.M.N.IE.W0.S126.S1.N.L.LE.F3.S._Z.E… | CSEC.M.N.IE.W0.S127.S1.N.L.LE.F511._Z._…
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Title complement, Decimals, Units, Issuance Type

## g1033（1 列）
- 見出し：Title complement
- 例1 値：Insurance corporations and Pension Fund… | Non financial corporations issuing sect… | Insurance corporations and Pension Fund… | Deposit taking corporations, except the… | Insurance corporations and Pension Fund…
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Series key, Decimals, Units, Issuance Type

## g1034（1 列）
- 見出し：Decimals
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Series key, Title complement, Units, Issuance Type

## g1035（1 列）
- 見出し：Units
- 例1 値：Millions of Euro | Millions of Euro | Millions of Euro | Millions of Euro | Millions of Euro
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Series key, Title complement, Decimals, Issuance Type

## g1036（1 列）
- 見出し：Issuance Type
- 例1 値：Gross issuance | Net Issuance | Net Issuance | Gross issuance | Gross issuance
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Series key, Title complement, Decimals, Units

## g1037（1 列）
- 見出し：Currency
- 例1 値：Euro | Non-Euro | Euro | Euro | Non-Euro
  - 同じ表の列：Date, Value, obs__status, obs__conf_, Series key, Title complement, Decimals, Units

## g1038（1 列）
- 見出し：Charities Regulator Concerns received 2025
- 例1 値：Number of Concerns closed to date 2024 | Concerns received to date 2024 | Number of active concerns | Number of Concerns received for this pe… | Number of Concerns closed for this peri…
  - 同じ表の列：Jan-25

## g1039（1 列）
- 見出し：Jan-25
- 例1 値：38 | 35 | 305 | 38 | 35
  - 同じ表の列：Charities Regulator…

## g1040（1 列）
- 見出し：company_num
- 例1 値：295733 | 587440 | 585054 | 588758 | 591729
  - 同じ表の列：company_status_code, company_status, company_type_code, company_type, company_reg_date, comp_dissolved_date, nard, company_status_date

## g1041（1 列）
- 見出し：company_status_code
- 例1 値：1158 | 1158 | 1156 | 1158 | 1158
  - 同じ表の列：company_num, company_status, company_type_code, company_type, company_reg_date, comp_dissolved_date, nard, company_status_date

## g1042（1 列）
- 見出し：company_status
- 例1 値：Normal | Dissolved | Strike Off Listed | Dissolved | Dissolved
  - 同じ表の列：company_num, company_status_code, company_type_code, company_type, company_reg_date, comp_dissolved_date, nard, company_status_date

## g1043（1 列）
- 見出し：company_type_code
- 例1 値：1150 | 1153 | 1119 | 1119 | 1119
  - 同じ表の列：company_num, company_status_code, company_status, company_type, company_reg_date, comp_dissolved_date, nard, company_status_date

## g1044（1 列）
- 見出し：company_type
- 例1 値：Private limited by shares | LTD - Private Company Limited by Shares | LTD - Private Company Limited by Shares | LTD - Private Company Limited by Shares | CLG - Company Limited by Guarantee
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_reg_date, comp_dissolved_date, nard, company_status_date

## g1045（1 列）
- 見出し：company_reg_date
- 例1 値：1998-02-09T00:00:00 | 2016-05-30T00:00:00 | 1998-11-23T00:00:00 | 2017-01-04T00:00:00 | 1998-09-10T00:00:00
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_type, comp_dissolved_date, nard, company_status_date

## g1046（1 列）
- 見出し：comp_dissolved_date
- 例1 値：2001-07-27T00:00:00 | 2000-08-04T00:00:00 | 2001-07-27T00:00:00 | 2024-01-24T00:00:00 | 2008-02-22T00:00:00
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_type, company_reg_date, nard, company_status_date

## g1047（1 列）
- 見出し：nard
- 例1 値：2025-02-28T00:00:00 | 2025-09-30T00:00:00 | 2024-09-30T00:00:00 | 2020-07-18T00:00:00 | 2002-12-15T00:00:00
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_type, company_reg_date, comp_dissolved_date, company_status_date

## g1048（1 列）
- 見出し：company_status_date
- 例1 値：2005-05-27T00:00:00 | 2000-08-04T00:00:00 | 2017-05-31T00:00:00 | 2018-10-03T00:00:00 | 2003-12-19T00:00:00
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_type, company_reg_date, comp_dissolved_date, nard

## g1049（1 列）
- 見出し：nace_v2_code
- 例1 値：7022 | 6810 | 4334 | 4321 | 5629
  - 同じ表の列：company_num, company_status_code, company_status, company_type_code, company_type, company_reg_date, comp_dissolved_date, nard

## g1050（1 列）
- 見出し：Authorisation Number
- 例1 値：A003758/26 | A003598/26 | A004836/26 | A001812/26 | A003515/26
  - 同じ表の列：Expiry Date, County, Post Code, Financial Instituti…

## g1051（1 列）
- 見出し：Expiry Date
- 例1 値：20270119 | 20261031 | 20270128 | 20270417 | 20271018
  - 同じ表の列：Authorisation Number, County, Post Code, Financial Instituti…

## g1052（1 列）
- 見出し：County
- 例1 値：Laois | Cork | Donegal | Co.Galway | Louth
  - 同じ表の列：Authorisation Number, Expiry Date, Post Code, Financial Instituti…

## g1053（1 列）
- 見出し：Post Code
- 例1 値：F23Kd60 | - | R32X8H7 | 5 | R95Rk11
  - 同じ表の列：Authorisation Number, Expiry Date, County, Financial Instituti…

## g1054（1 列）
- 見出し：Financial Institutions
- 例1 値：Allied Irish Banks plc & AIB Leasing Lt… | Finance For You Ltd T/A Finance For You… | Premium Credit Limited | Finance For You Ltd T/A Finance For You… | Bank of Ireland Finance,Finance Ireland…
  - 同じ表の列：Authorisation Number, Expiry Date, County, Post Code

## g1055（7 列）
- 見出し：County
- 例1 値：Waterford | Donegal | Kerry | Offaly | Roscommon
  - 同じ表の列：no__of_flocks, Avg Flock Size, Breeding Ewes over …, Rams, Other Sheep, Total Sheep
- 例2 値：Dublin | Dublin | Dublin | Dublin | Dublin
  - 同じ表の列：Roll Number, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…

## g1056（1 列）
- 見出し：no__of_flocks
- 例1 値：521 | 754 | 1,155 | 619 | 1,080
  - 同じ表の列：County, Avg Flock Size, Breeding Ewes over …, Rams, Other Sheep, Total Sheep

## g1057（1 列）
- 見出し：Avg Flock Size
- 例1 値：87 | 140 | 134 | 90 | 115
  - 同じ表の列：County, no__of_flocks, Breeding Ewes over …, Rams, Other Sheep, Total Sheep

## g1058（1 列）
- 見出し：Breeding Ewes over 12 Months Old
- 例1 値：127,579 | 47,942 | 35,199 | 80,579 | 59,036
  - 同じ表の列：County, no__of_flocks, Avg Flock Size, Rams, Other Sheep, Total Sheep

## g1059（1 列）
- 見出し：Rams
- 例1 値：8,484 | 1,320 | 2,506 | 2,397 | 1,196
  - 同じ表の列：County, no__of_flocks, Avg Flock Size, Breeding Ewes over …, Other Sheep, Total Sheep

## g1060（1 列）
- 見出し：Other Sheep
- 例1 値：36,680 | 83,510 | 24,549 | 54,814 | 59,760
  - 同じ表の列：County, no__of_flocks, Avg Flock Size, Breeding Ewes over …, Rams, Total Sheep

## g1061（1 列）
- 見出し：Total Sheep
- 例1 値：57,548 | 108,588 | 321,372 | 131,720 | 58,304
  - 同じ表の列：County, no__of_flocks, Avg Flock Size, Breeding Ewes over …, Rams, Other Sheep

## g1062（4 列）
- 見出し：STATISTIC
- 例1 値：SCA27 | SCA27 | SCA27 | SCA27 | SCA27
  - 同じ表の列：Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968
- 例2 値：G0207 | G0207 | G0207 | G0207 | G0207
  - 同じ表の列：Statistic, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g1063（3 列）
- 見出し：Statistic
- 例1 値：Children with a Disability | Children with a Disability | Children with a Disability | Children with a Disability | Children with a Disability
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968
- 例2 値：Area under organic farming | Area under organic farming | Area under organic farming | Area under organic farming | Area under organic farming
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02196V02652, State, UNIT, VALUE

## g1064（8 列）
- 見出し：TLIST(A1)
- 例1 値：2016 | 2011 | 2011 | 2016 | 2016
  - 同じ表の列：STATISTIC, Statistic, Year, C02076V02508, Age Group, C02199V02655, Sex, C02451V02968
- 例2 値：2017 | 2016 | 2017 | 2016 | 2018
  - 同じ表の列：STATISTIC, Statistic, Year, C02196V02652, State, UNIT, VALUE

## g1065（1 列）
- 見出し：C02076V02508
- 例1 値：221 | 265 | 265 | 245 | 245
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Age Group, C02199V02655, Sex, C02451V02968

## g1066（1 列）
- 見出し：Age Group
- 例1 値：0 - 17 years | 15 - 17 years | 0 - 17 years | 0 - 4 years | 5 - 9 years
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, C02199V02655, Sex, C02451V02968

## g1067（1 列）
- 見出し：C02199V02655
- 例1 値：1 | 1 | 1 | - | 2
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, Sex, C02451V02968

## g1068（1 列）
- 見出し：Sex
- 例1 値：Both sexes | Female | Both sexes | Female | Both sexes
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, C02451V02968

## g1069（1 列）
- 見出し：C02451V02968
- 例1 値：20 | 142 | 03 | 021 | 16
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex

## g1070（1 列）
- 見出し：Administrative County
- 例1 値：Waterford | Cork County | Monaghan | Galway County | Leitrim
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02076V02508, Age Group, C02199V02655, Sex

## g1071（2 列）
- 見出し：Roll Number
- 例1 値：68161H | 60320H | 68082L | 70180A | 76130P
  - 同じ表の列：County, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…
- 例2 値：16443A | 13447Q | 15301V | 13607M | 15963V
  - 同じ表の列：County, Dublin Area Codes, School Type, set_hours_26_27, set_posts__26_27, special_class_teach…, mainstream_sna_allo…, special_class_snas_…

## g1072（1 列）
- 見出し：Local Authority
- 例1 値：Dun Laoghaire Rathdown | South Dublin County Council | South Dublin County Council | Dublin City Council | Fingal County Council
  - 同じ表の列：Roll Number, County, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…

## g1073（1 列）
- 見出し：Eircode
- 例1 値：D24XA46 | K67KW30 | D15H1FC | A94TP97 | D04E9X5
  - 同じ表の列：Roll Number, County, Local Authority, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…

## g1074（1 列）
- 見出し：DEIS (Y/N)
- 例1 値：Y | N | Y | N | N
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…

## g1075（1 列）
- 見出し：Gaeltacht Area Location (Y/N)
- 例1 値：N | N | N | N | N
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, DEIS (Y/N), Island Location (Y/…, Fee Paying School (…, Pupil Attendance Ty…

## g1076（1 列）
- 見出し：Island Location (Y/N)
- 例1 値：N | N | N | N | N
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Fee Paying School (…, Pupil Attendance Ty…

## g1077（1 列）
- 見出し：Fee Paying School (Y/N)
- 例1 値：N | N | N | N | Y
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Pupil Attendance Ty…

## g1078（1 列）
- 見出し：Pupil Attendance Type
- 例1 値：Day | Day | Day | Day | Day
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…

## g1079（1 列）
- 見出し：School Gender - Post Primary
- 例1 値：Girls | Boys | Mixed | Girls | Girls
  - 同じ表の列：Roll Number, County, Local Authority, Eircode, DEIS (Y/N), Gaeltacht Area Loca…, Island Location (Y/…, Fee Paying School (…

## g1080（1 列）
- 見出し：unsafe_
- 例1 値：Higher education expenditure on R&D (HE… | Total researchers in HE sector (FTE) | HERD as a % of GNP | Researchers (HC) per 1000 labour force … | Ireland's rank out of 42 countries
  - 同じ表の列：unsafe_2004, unsafe_2006, unsafe_2008, unsafe_2010, unsafe_2012, unsafe_2014

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
