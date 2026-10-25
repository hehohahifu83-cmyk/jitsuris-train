# ラベル用シート 009 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：Type of Traffic
- 例1 値：Tourist cars | Tourist cars | Tourist passengers | Tourist cars | Tourist cars
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, Shipping Corridor, C02638V03194, UNIT

## g0962（1 列）
- 見出し：C02635V03192
- 例1 値：07 | 06 | 07 | 07 | 05
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Shipping Corridor, C02638V03194, Type of Traffic, UNIT

## g0963（1 列）
- 見出し：Type of Traffic
- 例1 値：Driver accompanied freight traffic | Driver accompanied freight traffic | Unaccompanied freight traffic | All freight traffic | All freight traffic
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02635V03192, Shipping Corridor, C02638V03194, UNIT

## g0964（2 列）
- 見出し：RegionID
- 例1 値：21 | 20 | 21 | 18 | 20
  - 同じ表の列：AreaID, Area, Year, Q1, Q2, Q3, Q4
- 例2 値：18 | 21 | 19 | 18 | 21
  - 同じ表の列：AreaID, Area, Year, Jan, Feb, Mar, Apr, May

## g0965（2 列）
- 見出し：AreaID
- 例1 値：12 | 13 | 11 | 15 | 17
  - 同じ表の列：RegionID, Area, Year, Q1, Q2, Q3, Q4
- 例2 値：14 | 9 | 2 | 17 | 5
  - 同じ表の列：RegionID, Area, Year, Jan, Feb, Mar, Apr, May

## g0966（1 列）
- 見出し：Area
- 例1 値：Dublin South Central | Mayo | Dublin South West Kildare West Wicklow | Kerry | Dublin North
  - 同じ表の列：RegionID, AreaID, Year, Q1, Q2, Q3, Q4

## g0967（1 列）
- 見出し：Q1
- 例1 値：22 | 7 | 27 | 27 | 14
  - 同じ表の列：RegionID, AreaID, Area, Year, Q2, Q3, Q4

## g0968（1 列）
- 見出し：Q2
- 例1 値：20 | 28 | 9 | 9 | 5
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q3, Q4

## g0969（1 列）
- 見出し：Q3
- 例1 値：8 | 29 | 81 | 29 | 8
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q2, Q4

## g0970（1 列）
- 見出し：Q4
- 例1 値：10 | 23 | 5 | 8 | 6
  - 同じ表の列：RegionID, AreaID, Area, Year, Q1, Q2, Q3

## g0971（1 列）
- 見出し：Area
- 例1 値：Dublin South Central | The Midlands | Social Work Team for Separated Children… | Louth Meath | Donegal
  - 同じ表の列：RegionID, AreaID, Year, Jan, Feb, Mar, Apr, May

## g0972（1 列）
- 見出し：X
- 例1 値：-6.69642032081438 | -6.07119718000269 | -6.14050505869359 | -6.68343918652262 | -6.61276767050924
  - 同じ表の列：Y, FID, ID, Monument, Caption, Mon_No, Status, OBJECTID

## g0973（1 列）
- 見出し：Y
- 例1 値：53.0432480312687 | 53.085303626198 | 53.1613810278079 | 52.9469771465055 | 52.9439301113423
  - 同じ表の列：X, FID, ID, Monument, Caption, Mon_No, Status, OBJECTID

## g0974（2 列）
- 見出し：FID
- 例1 値：20 | 17 | 23 | 6 | 18
  - 同じ表の列：X, Y, ID, Monument, Caption, Mon_No, Status, OBJECTID
- 例2 値：52 | 60 | 61 | 19 | 22
  - 同じ表の列：County, Area, Perimeter, IGH_Primary, IGH_Second, IGH_Third, Geol_Feature, Site_Code

## g0975（1 列）
- 見出し：Monument
- 例1 値：Threecastles - Oldcourt | Wedge Tomb - Moylisha | St Mark s Cross | Baltinglass Abbey (Cistercian) | Hillfort - Rathgall
  - 同じ表の列：X, Y, FID, ID, Caption, Mon_No, Status, OBJECTID

## g0976（1 列）
- 見出し：Caption
- 例1 値：This small granite cross is situated ju… | The ruins of this 13th century castle a… | Tornant Upper | Lemonstown | The site of an Early Christian monaster…
  - 同じ表の列：X, Y, FID, ID, Monument, Mon_No, Status, OBJECTID

## g0977（1 列）
- 見出し：Mon_No
- 例1 値：280 | 662 | 531 | 419 | 328
  - 同じ表の列：X, Y, FID, ID, Monument, Caption, Status, OBJECTID

## g0978（1 列）
- 見出し：ID
- 例1 値：Regional Road Objectives | National Road Objectives | Leinster Outer Orbital Route | National Road Objectives | Leinster Outer Orbital Route
  - 同じ表の列：OBJECTID, SHAPE__Length

## g0979（1 列）
- 見出し：SHAPE__Length
- 例1 値：8222.21617966823 | 22781.1779984 | 354.92124775926 | 40978.8372284118 | 9755.77860412967
  - 同じ表の列：ID, OBJECTID

## g0980（1 列）
- 見出し：Area
- 例1 値：7093489 | 1145554 | 803450 | 202496 | 321562
  - 同じ表の列：FID, County, Perimeter, IGH_Primary, IGH_Second, IGH_Third, Geol_Feature, Site_Code

## g0981（1 列）
- 見出し：Perimeter
- 例1 値：4680 | 3329 | 1155 | 398 | 4902
  - 同じ表の列：FID, County, Area, IGH_Primary, IGH_Second, IGH_Third, Geol_Feature, Site_Code

## g0982（1 列）
- 見出し：IGH_Primary
- 例1 値：IGH2 | IGH4 | IGH7 | IGH11 | IGH4
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Second, IGH_Third, Geol_Feature, Site_Code

## g0983（1 列）
- 見出し：IGH_Second
- 例1 値：IGH7 | IGH14 | IGH14 | IGH14 | IGH6
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Primary, IGH_Third, Geol_Feature, Site_Code

## g0984（1 列）
- 見出し：IGH_Third
- 例1 値：IGH15 | IGH14 | IGH4
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Primary, IGH_Second, Geol_Feature, Site_Code

## g0985（1 列）
- 見出し：Geol_Feature
- 例1 値：The shingle ridge (beach) is a feature … | Hollywood Glen is up to 60m deep and ha… | Glen Ding is up to 50m deep and has a U… | A stunning example of a glaciated U-sha… | The site contains a fault zone with min…
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Primary, IGH_Second, IGH_Third, Site_Code

## g0986（1 列）
- 見出し：Site_Code
- 例1 値：WW047 | WW033 | WW046 | WW035 | WW029
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Primary, IGH_Second, IGH_Third, Geol_Feature

## g0987（1 列）
- 見出し：Report
- 例1 値：attachment | attachment | attachment | attachment | attachment
  - 同じ表の列：FID, County, Area, Perimeter, IGH_Primary, IGH_Second, IGH_Third, Geol_Feature

## g0988（1 列）
- 見出し：AusTender Contract Notice ID
- 例1 値：CN3568359 | CN3581054 | CN3606462 | CN3573876 | CN3581182
  - 同じ表の列：Exchange Date, Supplier Details - …, Management Zone, Contract Value ($), Contract Volume (ML), Town/City, State/Territory

## g0989（1 列）
- 見出し：Exchange Date
- 例1 値：8/11/2018 | 16/01/2019 | 17/01/2019 | 31/01/2019 | 24/04/2019
  - 同じ表の列：AusTender Contract …, Supplier Details - …, Management Zone, Contract Value ($), Contract Volume (ML), Town/City, State/Territory

## g0990（1 列）
- 見出し：Supplier Details - AusTender
- 例1 値：Daniel & Chloe Skerman | Global Ag Properties Australia P/L | MK Durack Family No 4 Pty Ltd as trustee | J.R.Armstrong Pty Ltd | Bruce Arnold Passmore
  - 同じ表の列：AusTender Contract …, Exchange Date, Management Zone, Contract Value ($), Contract Volume (ML), Town/City, State/Territory

## g0991（1 列）
- 見出し：Management Zone
- 例1 値：CENTRAL CONDAMINE ALLUVIUM 2 | CENTRAL CONDAMINE ALLUVIUM 2-3 | CENTRAL CONDAMINE ALLUVIUM 1 | CENTRAL CONDAMINE ALLUVIUM 2-3 | CENTRAL CONDAMINE ALLUVIUM 3-3
  - 同じ表の列：AusTender Contract …, Exchange Date, Supplier Details - …, Contract Value ($), Contract Volume (ML), Town/City, State/Territory

## g0992（1 列）
- 見出し：Contract Value ($)
- 例1 値：$246,600.00 | $485,970.00 | $76,000.00 | $11,700.00 | $55,800.00
  - 同じ表の列：AusTender Contract …, Exchange Date, Supplier Details - …, Management Zone, Contract Volume (ML), Town/City, State/Territory

## g0993（1 列）
- 見出し：Contract Volume (ML)
- 例1 値：198.5 | 18.0 | 132.0 | 168.0 | 112.5
  - 同じ表の列：AusTender Contract …, Exchange Date, Supplier Details - …, Management Zone, Contract Value ($), Town/City, State/Territory

## g0994（1 列）
- 見出し：Town/City
- 例1 値：Dalby | Brookstead | Cecil Plains | Clifton | Brookstead
  - 同じ表の列：AusTender Contract …, Exchange Date, Supplier Details - …, Management Zone, Contract Value ($), Contract Volume (ML), State/Territory

## g0995（1 列）
- 見出し：State/Territory
- 例1 値：QLD | QLD | QLD | QLD | QLD
  - 同じ表の列：AusTender Contract …, Exchange Date, Supplier Details - …, Management Zone, Contract Value ($), Contract Volume (ML), Town/City

## g0996（3 列）
- 見出し：Date-Time
- 例1 値：2018-03-23 22:26:00 | 2018-03-24 06:20:00 | 2018-03-24 06:08:00 | 2018-03-23 16:46:00 | 2018-03-23 17:58:00
  - 同じ表の列：Lat, Lon, UV_Index
- 例2 値：2019-08-09 18:22:00 | 2019-08-09 15:45:00 | 2019-08-09 15:35:00 | 2019-08-09 09:53:00 | 2019-08-09 21:15:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0997（3 列）
- 見出し：UV_Index
- 例1 値：0.01 | 0.01 | 0.01 | 5.91 | 0.01
  - 同じ表の列：Date-Time, Lat, Lon
- 例2 値：0.49 | 0.01 | 0.01 | 1.27 | 0.01
  - 同じ表の列：Date-Time, Lat, Lon

## g0998（1 列）
- 見出し：Taxation statistics 2023-24
- 例1 値：Table 6A | Table 6: Individuals | 3 | Table 6B | *
  - 同じ表の列：None

## g0999（1 列）
- 見出し：None
- 例1 値：Selected items, by taxable status, stat… | Refers to the label on the individual r… | State/territory is based on residential… | The statistics for the 2023–24 income y… | Selected items, by state/territory, Sta…
  - 同じ表の列：Taxation statistics…

## g1000（2 列）
- 見出し：ABN
- 例1 値：336317821771 | 18606128090 | 40119031864 | 63620896282 | 58626093150
  - 同じ表の列：Commissioners alloc…
- 例2 値：22001660715 | 48123123124 | 16000011058 | 48123123124 | 22001660715
  - 同じ表の列：ipa_id, year, corp_desg, state, firm_alive, p_max_stock, p_filed, p_certified

## g1001（1 列）
- 見出し：Commissioners allocation $
- 例1 値：1250000 | 500000 | 300000 | 262500 | 356706.75
  - 同じ表の列：ABN

## g1002（1 列）
- 見出し：BEBIOH - Bio Hazards (inc vomit
- 例1 値：BEBIOH - Bio Hazards (inc vomit | BEBIOH - Bio Hazards (inc vomit | BEBIOH - Bio Hazards (inc vomit | BEBIOH - Bio Hazards (inc vomit | BEBIOH - Bio Hazards (inc vomit
  - 同じ表の列：condoms, faeces) - Beach, 2012/2013, March, Mar-2013, CY 2013, ST KILDA EAST, 2

## g1003（1 列）
- 見出し：condoms
- 例1 値：condoms | condoms | condoms | condoms | condoms
  - 同じ表の列：BEBIOH - Bio Hazard…, faeces) - Beach, 2012/2013, March, Mar-2013, CY 2013, ST KILDA EAST, 2

## g1004（1 列）
- 見出し：faeces) - Beach
- 例1 値：faeces) - Beach | faeces) - Beach | faeces) - Beach | faeces) - Beach | faeces) - Beach
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, 2012/2013, March, Mar-2013, CY 2013, ST KILDA EAST, 2

## g1005（1 列）
- 見出し：2012/2013
- 例1 値：2019/2020 | 2019/2020 | 2019/2020 | 2013/2014 | 2018/2019
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, March, Mar-2013, CY 2013, ST KILDA EAST, 2

## g1006（1 列）
- 見出し：March
- 例1 値：December | December | January | January | December
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, 2012/2013, Mar-2013, CY 2013, ST KILDA EAST, 2

## g1007（1 列）
- 見出し：Mar-2013
- 例1 値：Jan-2018 | Aug-2020 | Apr-2018 | Apr-2021 | Feb-2014
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, 2012/2013, March, CY 2013, ST KILDA EAST, 2

## g1008（1 列）
- 見出し：CY 2013
- 例1 値：CY 2018 | CY 2019 | CY 2015 | CY 2018 | CY 2013
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, 2012/2013, March, Mar-2013, ST KILDA EAST, 2

## g1009（1 列）
- 見出し：ST KILDA EAST
- 例1 値：UnAllocated | PORT MELBOURNE | ALBERT PARK | ELWOOD | PORT MELBOURNE
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, 2012/2013, March, Mar-2013, CY 2013, 2

## g1010（1 列）
- 見出し：2
- 例1 値：2 | 1 | 1 | 1 | 2
  - 同じ表の列：BEBIOH - Bio Hazard…, condoms, faeces) - Beach, 2012/2013, March, Mar-2013, CY 2013, ST KILDA EAST

## g1011（1 列）
- 見出し：species
- 例1 値：Platanus X acerifolia | Platanus X acerifolia | Nerium oleander | Lophostemon confertus | Melaleuca linariifolia
  - 同じ表の列：lat, lon, common, dbh, crown, crown_min, crown_max, height

## g1012（1 列）
- 見出し：common
- 例1 値：Brush Box | Brush Box | London Plane | Desert Ash | Desert Ash
  - 同じ表の列：lat, lon, species, dbh, crown, crown_min, crown_max, height

## g1013（1 列）
- 見出し：dbh
- 例1 値：100 | 40 | 50 | 45 | 70
  - 同じ表の列：lat, lon, species, common, crown, crown_min, crown_max, height

## g1014（3 列）
- 見出し：location
- 例1 値：street | street | street | street | street
  - 同じ表の列：lat, lon, species, common, dbh, crown, crown_min, crown_max
- 例2 値：Boundary | Boundary | Boundary | Boundary | Boundary
  - 同じ表の列：Park, PointID, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1015（1 列）
- 見出し：Agencies
- 例1 値：ARENA | ARENA | ARENA | ARENA | ARENA
  - 同じ表の列：ProjID, PrimTech, Lat, Long

## g1016（1 列）
- 見出し：ProjID
- 例1 値：2015/ARP012 | 2017/ARP012 | 2018/ARP016 | 2010/ASI004 | 2018/ARP132
  - 同じ表の列：Agencies, PrimTech, Lat, Long

## g1017（1 列）
- 見出し：PrimTech
- 例1 値：Hydrogen | Pumped Hydro Energy Storage (PHES) | Solar Thermal | Enabling | Solar PV
  - 同じ表の列：Agencies, ProjID, Lat, Long

## g1018（1 列）
- 見出し：Seq
- 例1 値：53 | 67 | 31 | 23 | 36
  - 同じ表の列：Y, X

## g1019（2 列）
- 見出し：Y
- 例1 値：-36.718269532650 | -36.715222926494 | -36.713682775257 | -36.713200921925 | -36.712560480261
  - 同じ表の列：Seq, X
- 例2 値：-36.11186784 | -36.10354802 | -36.32977812 | -36.23522752 | -36.12621394
  - 同じ表の列：X, Code, Year, Type, Area (Ha), Number of Plants, Town, Project Hindmarsh W…

## g1020（2 列）
- 見出し：X
- 例1 値：142.200730672002 | 142.195656381155 | 142.201590309498 | 142.198282093638 | 142.205413830617
  - 同じ表の列：Seq, Y
- 例2 値：141.721861 | 141.8037545 | 141.3492571 | 141.5168568 | 141.4871603
  - 同じ表の列：Y, Code, Year, Type, Area (Ha), Number of Plants, Town, Project Hindmarsh W…

## g1021（1 列）
- 見出し：LatLong
- 例1 値：-36.68002895044, 142.297630906105 | -36.7087659, 142.1905518 | -36.7089885, 142.2113719 | -36.845825, 142.2302272 | -36.7112365, 142.1880749
  - 同じ表の列：DefectNumber, PhysicalDescription, PrimaryLocation, RaisedBy, CreatedOn

## g1022（1 列）
- 見出し：DefectNumber
- 例1 値：DN00260 | DN00080 | DN00148 | DN00592 | DN00270
  - 同じ表の列：LatLong, PhysicalDescription, PrimaryLocation, RaisedBy, CreatedOn

## g1023（1 列）
- 見出し：PhysicalDescription
- 例1 値：Defective with a step or edge drop grea… | Pavement failure (less than 50m［個人名のため削除］ | Potholes in traffic lane of road paveme… | Defective with a step or edge drop grea… | Surface cracking bigger than 20 mm on f…
  - 同じ表の列：LatLong, DefectNumber, PrimaryLocation, RaisedBy, CreatedOn

## g1024（1 列）
- 見出し：PrimaryLocation
- 例1 値：James St | Baillie St | Rasmussen Rd (Horsham) | Darlot St (East CW) | Longerenong Rd
  - 同じ表の列：LatLong, DefectNumber, PhysicalDescription, RaisedBy, CreatedOn

## g1025（1 列）
- 見出し：RaisedBy
- 例1 値：［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］
  - 同じ表の列：LatLong, DefectNumber, PhysicalDescription, PrimaryLocation, CreatedOn

## g1026（1 列）
- 見出し：CreatedOn
- 例1 値：2017-08-14T08:42:00 | 2018-01-15T08:10:17 | 2017-10-06T14:18:00 | 2017-09-20T09:13:00 | 2017-08-09T08:54:00
  - 同じ表の列：LatLong, DefectNumber, PhysicalDescription, PrimaryLocation, RaisedBy

## g1027（1 列）
- 見出し：ipa_id
- 例1 値：366674 | 25807 | 61440 | 243761 | 136445
  - 同じ表の列：abn, year, corp_desg, state, firm_alive, p_max_stock, p_filed, p_certified

## g1028（1 列）
- 見出し：corp_desg
- 例1 値：CORP | INC | INC | BV | CO
  - 同じ表の列：abn, ipa_id, year, state, firm_alive, p_max_stock, p_filed, p_certified

## g1029（1 列）
- 見出し：state
- 例1 値：US | ACT AU | DE | JP | GB
  - 同じ表の列：abn, ipa_id, year, corp_desg, firm_alive, p_max_stock, p_filed, p_certified

## g1030（1 列）
- 見出し：firm_alive
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：abn, ipa_id, year, corp_desg, state, p_max_stock, p_filed, p_certified

## g1031（1 列）
- 見出し：p_max_stock
- 例1 値：597 | 1732 | 1238 | 1728 | 138
  - 同じ表の列：abn, ipa_id, year, corp_desg, state, firm_alive, p_filed, p_certified

## g1032（1 列）
- 見出し：p_filed
- 例1 値：60 | 126 | 1 | 56 | 115
  - 同じ表の列：abn, ipa_id, year, corp_desg, state, firm_alive, p_max_stock, p_certified

## g1033（1 列）
- 見出し：p_certified
- 例1 値：33 | 46 | 1 | 76 | 79
  - 同じ表の列：abn, ipa_id, year, corp_desg, state, firm_alive, p_max_stock, p_filed

## g1034（1 列）
- 見出し：p_retired
- 例1 値：86 | 113 | 21 | 72 | 104
  - 同じ表の列：abn, ipa_id, year, corp_desg, state, firm_alive, p_max_stock, p_filed

## g1035（1 列）
- 見出し：Code
- 例1 値：PH029 | PH037 | PH063 | PH002 | PH028
  - 同じ表の列：X, Y, Year, Type, Area (Ha), Number of Plants, Town, Project Hindmarsh W…

## g1036（1 列）
- 見出し：Area (Ha)
- 例1 値：5.65 | 7.25 | 30 | 12.9 | 7.15
  - 同じ表の列：X, Y, Code, Year, Type, Number of Plants, Town, Project Hindmarsh W…

## g1037（1 列）
- 見出し：Number of Plants
- 例1 値：3600 | 24,000 | 15000 | 780 | 2500
  - 同じ表の列：X, Y, Code, Year, Type, Area (Ha), Town, Project Hindmarsh W…

## g1038（1 列）
- 見出し：Town
- 例1 値：Dimboola | Nhill | Yanac | Gerang Gerung | Jeparit
  - 同じ表の列：X, Y, Code, Year, Type, Area (Ha), Number of Plants, Project Hindmarsh W…

## g1039（1 列）
- 見出し：Project Hindmarsh Weekend
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：X, Y, Code, Year, Type, Area (Ha), Number of Plants, Town

## g1040（3 列）
- 見出し：_id
- 例1 値：2 | 5 | 1 | 3 | 4
  - 同じ表の列：Library, CKI
- 例2 値：1 | 4 | 5 | 3 | 2
  - 同じ表の列：Library, Number of members

## g1041（3 列）
- 見出し：Library
- 例1 値：Werribee | Plaza | Julia Gillard Library Tarneit | Wyndham Vale | Point Cook
  - 同じ表の列：_id, CKI
- 例2 値：Julia Gillard Library Tarneit | Wyndham Vale | Point Cook | Plaza | Werribee
  - 同じ表の列：_id, Number of members

## g1042（1 列）
- 見出し：CKI
- 例1 値：215798 | 205293 | 554822 | 188861 | 461184
  - 同じ表の列：_id, Library

## g1043（1 列）
- 見出し：Number of members
- 例1 値：51627 | 5664 | 3950 | 14890 | 20429
  - 同じ表の列：_id, Library

## g1044（1 列）
- 見出し：Attendance - Total
- 例1 値：17501 | 12762 | 10481 | 8717 | 25828
  - 同じ表の列：_id, Library, EY:0-5, J:5-12, Y:13-19, Adult, Elderly, Number of Programs

## g1045（1 列）
- 見出し：EY:0-5
- 例1 値：7103 | 6450 | 20440 | 11646 | 8116
  - 同じ表の列：_id, Library, Attendance - Total, J:5-12, Y:13-19, Adult, Elderly, Number of Programs

## g1046（1 列）
- 見出し：J:5-12
- 例1 値：3153 | 3216 | 4506 | 1628 | 2626
  - 同じ表の列：_id, Library, Attendance - Total, EY:0-5, Y:13-19, Adult, Elderly, Number of Programs

## g1047（1 列）
- 見出し：Y:13-19
- 例1 値：177 | 690 | 242 | 526 | 56
  - 同じ表の列：_id, Library, Attendance - Total, EY:0-5, J:5-12, Adult, Elderly, Number of Programs

## g1048（1 列）
- 見出し：Adult
- 例1 値：2071 | 653 | 692 | 422 | 579
  - 同じ表の列：_id, Library, Attendance - Total, EY:0-5, J:5-12, Y:13-19, Elderly, Number of Programs

## g1049（1 列）
- 見出し：Elderly
- 例1 値：4 | 111 | 88 | 52 | 42
  - 同じ表の列：_id, Library, Attendance - Total, EY:0-5, J:5-12, Y:13-19, Adult, Number of Programs

## g1050（1 列）
- 見出し：Number of Programs
- 例1 値：742 | 407 | 580 | 609 | 410
  - 同じ表の列：_id, Library, Attendance - Total, EY:0-5, J:5-12, Y:13-19, Adult, Elderly

## g1051（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：2010MYC0183 | 2010MYC0488 | 2010MYC0345 | 2010MYC0231 | 2010MYC0376
  - 同じ表の列：Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test

## g1052（3 列）
- 見出し：Function
- 例1 値：Import | Import | Import | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test
- 例2 値：Import | Import | Import | Import | Import
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1053（2 列）
- 見出し：Fonction
- 例1 値：Domestique | Importé | Domestique | Importé | Importé
  - 同じ表の列：Sample No. - No. d'…, Function, Origin, Origine, Product, Produit, Date Sampled - Date…, Type of Test
- 例2 値：Domestique | Domestique | Importé | Domestique | Importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1054（2 列）
- 見出し：Origin
- 例1 値：UNITED STATES | CANADA | CANADA | CANADA | SWITZERLAND
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…, Type of Test
- 例2 値：UNITED STATES | CHILE | UNITED STATES | UNITED STATES | UNITED STATES
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…

## g1055（1 列）
- 見出し：Origine
- 例1 値：AUSTRALIE | ÉTATS-UNIS | CANADA | INCONNU | COLOMBIE
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…, Type of Test

## g1056（1 列）
- 見出し：Product
- 例1 値：Infant Formula - Dairy | Cereal - Adult | Cereal - Adult | Infant Food - Cereal | Raisin
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…, Type of Test

## g1057（1 列）
- 見出し：Produit
- 例1 値：Céréales - Enfants | Préparation pour nourrissons - Laitier | Figue | Figue | Céréales - Nourrissons
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…, Type of Test

## g1058（3 列）
- 見出し：Date Sampled - Date d'echantillonage
- 例1 値：2010-12-14 | 2011-03-01 | 2010-12-17 | 2010-12-08 | 2010-12-08
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Type of Test
- 例2 値：2010-11-20 | 2010-11-14 | 2010-10-25 | 2010-11-02 | 2010-12-02
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g1059（2 列）
- 見出し：Type of Test
- 例1 値：VOMITOXIN | VOMITOXIN | VOMITOXIN | VOMITOXIN | OCHRATOXIN
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…
- 例2 値：SULPHITES | SULPHITES | SULPHITES | SULPHITES | SULPHITES
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g1060（1 列）
- 見出し：Type d'analyse
- 例1 値：VOMITOXINE | OCHRATOXINE | VOMITOXINE | OCHRATOXINE | OCHRATOXINE
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1061（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：2010SUL0019 | 2010SUL0072 | 2010SUL0103-2 | 2010SUL0248 | 2010SUL0086
  - 同じ表の列：Region - Region, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1062（1 列）
- 見出し：Region - Region
- 例1 値：ATLANTIC - ATLANTIQUE | QUEBEC - QUÉBEC | WEST - OUEST | WEST - OUEST | QUEBEC - QUÉBEC
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1063（1 列）
- 見出し：Fonction
- 例1 値：Importé | Importé | Importé | Importé | Importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1064（1 列）
- 見出し：Origine
- 例1 値：ÉTATS-UNIS | ÉTATS-UNIS | PÉROU | ÉTATS-UNIS | INCONNU
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…

## g1065（2 列）
- 見出し：Product
- 例1 値：Grape | Grape | Grape | Grape | Grape
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…
- 例2 値：BEER | BEER | BEER | BEER | BEER
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…

## g1066（1 列）
- 見出し：Produit
- 例1 値：Raisin | Raisin | Raisin | Raisin | Raisin
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…

## g1067（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：B9-10-AL-00101 | B9-10-AL-00070 | B9-10-AL-00154 | B9-10-AL-00029 | B9-10-AL-00176
  - 同じ表の列：Region - Region, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1068（1 列）
- 見出し：Region - Region
- 例1 値：QUEBEC - QUÉBEC | QUEBEC - QUÉBEC | QUEBEC - QUÉBEC | QUEBEC - QUÉBEC | QUEBEC - QUÉBEC
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g1069（1 列）
- 見出し：Origin
- 例1 値：CANADA | CANADA | CANADA | CANADA | CANADA
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…

## g1070（1 列）
- 見出し：Origine
- 例1 値：DANEMARK | CANADA | CANADA | FRANCE | CANADA
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…

## g1071（1 列）
- 見出し：Produit
- 例1 値：BIÈRE | BIÈRE | BIÈRE | BIÈRE | BIÈRE
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…

## g1072（1 列）
- 見出し：Type of test
- 例1 値：UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen | UNDECLARED Multi Allergen
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g1073（1 列）
- 見出し：Ref Number | Numero ref
- 例1 値：5470841 | 6726780 | 7109206 | 7108831 | 7209144
  - 同じ表の列：Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…, Comments

## g1074（1 列）
- 見出し：Title (English)
- 例1 値：［個人名のため削除］ staff review of ［個人名のため削除］ Status Update … | Pickering NGS – ［個人名のため削除］ staff Review of Pe… | CD# NK30-CORR-00531-08580 - Pickering N… | Pickering NGS – ［個人名のため削除］ staff Review of As… | Pickering NGS – Revised 2022 Predictive…
  - 同じ表の列：Ref Number | Numero…, Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…, Comments

## g1075（1 列）
- 見出し：Titre (Francais)
- 例1 値：CD# NK30-CORR-00531-08580 – Centrale nu… | Modification de l’autorisation 16-HCAA-… | CD# P-CORR-00531-23299 – Centrale nuclé… | Centrale nucléaire de Pickering : Atten… | Centrale nucléaire de Pickering, tranch…
  - 同じ表の列：Ref Number | Numero…, Title (English), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…, Comments

## g1076（1 列）
- 見出し：Author | Auteur
- 例1 値：［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), # pages, Language | Langue, Date, Availability | Disp…, Comments

## g1077（1 列）
- 見出し：# pages
- 例1 値：133 | 3 | 4 | 2 | 122
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, Language | Langue, Date, Availability | Disp…, Comments

## g1078（1 列）
- 見出し：Language | Langue
- 例1 値：English | English | English | English | English
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Date, Availability | Disp…, Comments

## g1079（1 列）
- 見出し：Date
- 例1 値：8-Sep-23 | 23-Oct-23 | 2-Nov-23 | 11-Jul-23 | 2-May-23
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Availability | Disp…, Comments

## g1080（1 列）
- 見出し：Availability | Disponibilite
- 例1 値：Available | Available | Available | Available | Not available
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Comments

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
