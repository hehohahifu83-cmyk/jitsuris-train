# ラベル用シート 013 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_013.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1441（1 列）
- 見出し：registry_group_number
- 例1 値：255 | 288 | 304 | 50 | 311
  - 同じ表の列：year, region EN, Region FR, prov_terr EN, prov_terr FR, district EN, district FR, pop_on_reserve_crow…

## g1442（1 列）
- 見出し：region EN
- 例1 値：Alberta | Manitoba | Saskatchewan | Saskatchewan | Manitoba
  - 同じ表の列：year, registry_group_numb…, Region FR, prov_terr EN, prov_terr FR, district EN, district FR, pop_on_reserve_crow…

## g1443（1 列）
- 見出し：Region FR
- 例1 値：Colombie-Britannique | Ontario | Ontario | Alberta | Colombie-Britannique
  - 同じ表の列：year, registry_group_numb…, region EN, prov_terr EN, prov_terr FR, district EN, district FR, pop_on_reserve_crow…

## g1444（1 列）
- 見出し：prov_terr EN
- 例1 値：Manitoba | Ontario | Ontario | British Columbia | Manitoba
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr FR, district EN, district FR, pop_on_reserve_crow…

## g1445（1 列）
- 見出し：prov_terr FR
- 例1 値：Ontario | Saskatchewan | Ontario | Québec | Manitoba
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr EN, district EN, district FR, pop_on_reserve_crow…

## g1446（1 列）
- 見出し：district EN
- 例1 値：NA | Western District | North Central District | Quebec District | NA
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr EN, prov_terr FR, district FR, pop_on_reserve_crow…

## g1447（1 列）
- 見出し：district FR
- 例1 値：District Western | District Alberta | NA | NA | District South
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr EN, prov_terr FR, district EN, pop_on_reserve_crow…

## g1448（1 列）
- 見出し：pop_on_reserve_crown_land_men
- 例1 値：1075 | 479 | 364 | 601 | 156
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr EN, prov_terr FR, district EN, district FR

## g1449（1 列）
- 見出し：pop_on_reserve_crown_land_women
- 例1 値：3933 | 67 | 297 | 305 | 424
  - 同じ表の列：year, registry_group_numb…, region EN, Region FR, prov_terr EN, prov_terr FR, district EN, district FR

## g1450（1 列）
- 見出し：Annee financiere - Fiscal Year
- 例1 値：2017-18 | 2017-18 | 2017-18 | 2017-18 | 2017-18
  - 同じ表の列：Trimestre - Quarter, Mois - Months, Temps moyen en mois…

## g1451（1 列）
- 見出し：Trimestre - Quarter
- 例1 値：T4 | T4 | T1 | T3 | T2
  - 同じ表の列：Annee financiere - …, Mois - Months, Temps moyen en mois…

## g1452（1 列）
- 見出し：Mois - Months
- 例1 値：Juillet | Aout | Mars | Avril | Fevrier
  - 同じ表の列：Annee financiere - …, Trimestre - Quarter, Temps moyen en mois…

## g1453（1 列）
- 見出し：Temps moyen en mois requis pour completer l'evaluation d'une
- 例1 値：5.5 | 5.3 | 4.7 | 3.2 | 4.2
  - 同じ表の列：Annee financiere - …, Trimestre - Quarter, Mois - Months

## g1454（1 列）
- 見出し：PublicationID
- 例1 値：109331 | 126694 | 295978 | 102813 | pfmq507fg6
  - 同じ表の列：PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1455（1 列）
- 見出し：PublicationTitle_TitrePublication
- 例1 値：Norman Wells Pipeline Monitoring Sites … | Mackenzie valley near surface temperatu… | Shallow ground temperatures | Canada, permafrost | Isotope constraints on the origin of po…
  - 同じ表の列：PublicationID, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1456（1 列）
- 見出し：PublicationLanguage_LanguePublication
- 例1 値：English | Anglais | English | Anglais | English | Anglais | English; French | Anglais; Français | English | Anglais
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1457（1 列）
- 見出し：PublicationYear_AnneePublication
- 例1 値：1997 | 2020 | 1993 | 1984 | 2018
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1458（1 列）
- 見出し：DocumentType+No_TypeDocument+No
- 例1 値：Current Research, Part E/Recherches En … | Scientific Presentation 77 | Présentati… | Current Research no. 1995-B | Commissio… | Bulletin 544 | Open File 2315 | Dossier public 2315
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1459（1 列）
- 見出し：Abstract_Resume_FR
- 例1 値：Dans la péninsule Fosheim, le forage de… | L'objectif principal du présent rapport… | On a effectué l'analyse géochimique de … | À l'été 2016, les données sur la tempér… | Le présent guide a pour but de décrire …
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, PublicationProvTerr, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1460（1 列）
- 見出し：PublicationProvTerr
- 例1 値：NA | Canada | Northwest Territories | Territoires du … | Northwest Territories | Territoires du … | Northwest Territories | Territoires du …
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, LatitudeNorth_Latit…, LatitudeSouth_Latit…

## g1461（1 列）
- 見出し：LatitudeNorth_LatitudeNord
- 例1 値：62.75 | 60 | 64 | 70 | 62.55
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeSouth_Latit…

## g1462（1 列）
- 見出し：LatitudeSouth_LatitudeSud
- 例1 値：62.425 | 67 | 62.3833 | 61 | 65
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…

## g1463（1 列）
- 見出し：LongitudeEast_LongitudeEst
- 例1 値：-72 | -70 | -68.5 | -132 | -116
  - 同じ表の列：PublicationID, PublicationTitle_Ti…, PublicationLanguage…, PublicationYear_Ann…, DocumentType+No_Typ…, Abstract_Resume_FR, PublicationProvTerr, LatitudeNorth_Latit…

## g1464（1 列）
- 見出し：STYPE
- 例1 値：1 | 1 | 2 | 2 | 2
  - 同じ表の列：PROV, QF, Q1, Q2, Q3, Q4A, Q4B, Q4C

## g1465（1 列）
- 見出し：QF
- 例1 値：5 | 5 | 5 | 5 | 10
  - 同じ表の列：STYPE, PROV, Q1, Q2, Q3, Q4A, Q4B, Q4C

## g1466（1 列）
- 見出し：Q3
- 例1 値：2 | 5 | 6 | 6 | 7
  - 同じ表の列：STYPE, PROV, QF, Q1, Q2, Q4A, Q4B, Q4C

## g1467（1 列）
- 見出し：Q4A
- 例1 値：1 | 6 | 5 | 2 | 7
  - 同じ表の列：STYPE, PROV, QF, Q1, Q2, Q3, Q4B, Q4C

## g1468（1 列）
- 見出し：Q4B
- 例1 値：5 | 3 | 5 | 5 | 1
  - 同じ表の列：STYPE, PROV, QF, Q1, Q2, Q3, Q4A, Q4C

## g1469（1 列）
- 見出し：Q4C
- 例1 値：5 | 4 | 4 | 4 | 3
  - 同じ表の列：STYPE, PROV, QF, Q1, Q2, Q3, Q4A, Q4B

## g1470（1 列）
- 見出し：Q5
- 例1 値：1 | 1 | 1 | 1 | 2
  - 同じ表の列：STYPE, PROV, QF, Q1, Q2, Q3, Q4A, Q4B

## g1471（1 列）
- 見出し：Total Loan Companies/FIs
- 例1 値：Total Loan Companies | Total Loan Companies | Total Loan Companies | Total Loan Companies | Total Loan Companies
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Societes de p…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1472（1 列）
- 見出し：Total Societes de pret/IFFs
- 例1 値：Total Sociétés de prêt | Total Sociétés de prêt | Total Sociétés de prêt | Total Sociétés de prêt | Total Sociétés de prêt
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1473（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Sociétés de prêt | Sociétés de prêt | Sociétés de prêt | Sociétés de prêt | Sociétés de prêt
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Return/Releve, Return Title

## g1474（1 列）
- 見出し：Park
- 例1 値：YNP | YNP | YNP | YNP | YNP
  - 同じ表の列：Location, PointID, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1475（1 列）
- 見出し：Location
- 例1 値：Amiskwi | Amiskwi | Amiskwi | Amiskwi | Nom du lieu
  - 同じ表の列：Park, PointID, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1476（1 列）
- 見出し：PointID
- 例1 値：1 | 3 | 6 | 5 | 3
  - 同じ表の列：Park, Location, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1477（1 列）
- 見出し：Month
- 例1 値：6 | 6 | 6 | 6 | 6
  - 同じ表の列：Park, Location, PointID, Year, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1478（1 列）
- 見出し：Day
- 例1 値：11 | 7 | 11 | 13 | 11
  - 同じ表の列：Park, Location, PointID, Year, Month, Species, Time.1st.Detected, #detected_0-3m20s

## g1479（1 列）
- 見出し：Species
- 例1 値：PISI | CAJA | BRCR | CHSP | SWTH
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Time.1st.Detected, #detected_0-3m20s

## g1480（1 列）
- 見出し：Time.1st.Detected
- 例1 値：0.08 | 6.15 | 0 | 3.27 | 2.13
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, #detected_0-3m20s

## g1481（1 列）
- 見出し：#detected_0-3m20s
- 例1 値：0 | 1 | 1 | 0 | 0
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, Time.1st.Detected

## g1482（1 列）
- 見出し：#detected_3m21s-6m40s
- 例1 値：1 | 2 | 1 | 1 | 2
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, Time.1st.Detected

## g1483（1 列）
- 見出し：City
- 例1 値：Port Dover | Shawinigan | Heart's Content | Saguenay | Côte Saint-Luc
  - 同じ表の列：Fiscal Year, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Disciplines, Audiences

## g1484（1 列）
- 見出し：Province
- 例1 値：New Brunswick | British Columbia | Quebec | Alberta | Ontario
  - 同じ表の列：Fiscal Year, City, Region, Community Type, Grant Or Contributi…, Amount Approved, Disciplines, Audiences

## g1485（1 列）
- 見出し：Grant Or Contribution
- 例1 値：Grant | Contribution | Contribution | Grant | Contribution
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Amount Approved, Disciplines, Audiences

## g1486（1 列）
- 見出し：Disciplines
- 例1 値：Art Gallery, Cinema, Multidisciplinary,… | Theatre | Music | Media Art | Visual Arts
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Audiences

## g1487（1 列）
- 見出し：Audiences
- 例1 値：None | None | Young Audience | Indigenous Communities | None
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Disciplines

## g1488（1 列）
- 見出し：Project Type
- 例1 値：Specialized Equipment | Specialized Equipment | Construction/Renovation | Specialized Equipment | Construction/Renovation
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Disciplines

## g1489（1 列）
- 見出し：fiscal_year
- 例1 値：2016-2017 | 2022-2023 | 2013-2014 | 2013-2014 | 2020-2021
  - 同じ表の列：geo_region_e, geo_region_f, recruitment_program…, recruitment_program…, n

## g1490（1 列）
- 見出し：geo_region_e
- 例1 値：Unknown | New Brunswick | Outside Canada | Unknown | Unknown
  - 同じ表の列：fiscal_year, geo_region_f, recruitment_program…, recruitment_program…, n

## g1491（1 列）
- 見出し：geo_region_f
- 例1 値：Nouveau-Brunswick | Nouvelle-Écosse | Terre-Neuve-et-Labrador | Nouvelle-Écosse | Ontario
  - 同じ表の列：fiscal_year, geo_region_e, recruitment_program…, recruitment_program…, n

## g1492（1 列）
- 見出し：recruitment_program_e
- 例1 値：Research Affiliate Program | Research Affiliate Program | Federal Student Work Experience Program | Post-Secondary Recruitment Program | Recruitment of Policy Leaders Initiative
  - 同じ表の列：fiscal_year, geo_region_e, geo_region_f, recruitment_program…, n

## g1493（1 列）
- 見出し：recruitment_program_f
- 例1 値：Recrutement postsecondaire | Recrutement postsecondaire | Programme fédéral d’expérience de trava… | Programme fédéral d’expérience de trava… | Programme des adjoints de recherche
  - 同じ表の列：fiscal_year, geo_region_e, geo_region_f, recruitment_program…, n

## g1494（1 列）
- 見出し：n
- 例1 値：17128 | 38 | 88 | 367 | 3079
  - 同じ表の列：fiscal_year, geo_region_e, geo_region_f, recruitment_program…, recruitment_program…

## g1495（1 列）
- 見出し：# of service request:
- 例1 値：168 | 15 | 48 | 247 | 208
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Turnaround time (in…, # of transactions c…, # of transactions N…, % delivered within …

## g1496（1 列）
- 見出し：Turnaround time (in days):
- 例1 値：7.25 | 0.588 | 2.23 | 5.3 | 0
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, # of service reques…, # of transactions c…, # of transactions N…, % delivered within …

## g1497（1 列）
- 見出し：# of transactions completed within the SLS:
- 例1 値：83 | 145 | 14 | 22 | 86
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, # of service reques…, Turnaround time (in…, # of transactions N…, % delivered within …

## g1498（1 列）
- 見出し：# of transactions NOT completed within the SLS:
- 例1 値：0 | 6 | 0 | 2 | 0
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, # of service reques…, Turnaround time (in…, # of transactions c…, % delivered within …

## g1499（1 列）
- 見出し：% delivered within the standard:
- 例1 値：99.04% | 100.00% | 100% | 89.66% | 85.57%
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, # of service reques…, Turnaround time (in…, # of transactions c…, # of transactions N…

## g1500（1 列）
- 見出し：ref_number
- 例1 値：ATS-2020-Q3-058 | PR-2024-Q4-00023 | ATS-2021-Q1-069 | PR-2022-Q1-00047 | PR-2022-Q1-00061
  - 同じ表の列：pos_number, date, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code, new_class_level

## g1501（1 列）
- 見出し：pos_number
- 例1 値：00126097 | 30316438 | 21313 | 00017621 | 00019852
  - 同じ表の列：ref_number, date, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code, new_class_level

## g1502（1 列）
- 見出し：pos_title_en
- 例1 値：Manager, Regional Programs | HUMAN RESOURCES ADVISOR | Manager, Regional Trade Operations | Administrative Officer | SIMA Compliance Officer
  - 同じ表の列：ref_number, pos_number, date, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code, new_class_level

## g1503（1 列）
- 見出し：pos_title_fr
- 例1 値：Chercheur Scientifique | Gestionnaire des programmes régionaux | Chercheur Scientifique | Dir gén région Atlantique | DIRECTEUR (TRICE) DU SERVICE À LA CLIEN…
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, old_class_group_code, old_class_level, new_class_group_code, new_class_level

## g1504（1 列）
- 見出し：old_class_group_code
- 例1 値：FB | PG | SE-RES | FI | CR
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, pos_title_fr, old_class_level, new_class_group_code, new_class_level

## g1505（1 列）
- 見出し：old_class_level
- 例1 値：07 | 04 | 02 | 03 | 06
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, pos_title_fr, old_class_group_code, new_class_group_code, new_class_level

## g1506（1 列）
- 見出し：new_class_group_code
- 例1 値：PE | PM | AS | BI | FB
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_level

## g1507（1 列）
- 見出し：new_class_level
- 例1 値：05 | 03 | 03 | 05 | 02
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code

## g1508（1 列）
- 見出し：old_differential
- 例1 値：X | X | n/a | X | X
  - 同じ表の列：ref_number, pos_number, date, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code

## g1509（1 列）
- 見出し：MAKE
- 例1 値：HYUNDAI | JEEP | ASTON MARTIN | FORD | SUBARU
  - 同じ表の列：MODEL, MYR, OL, OW, OH, WB, CW, A

## g1510（1 列）
- 見出し：MODEL
- 例1 値：CARNIVAL MINIVAN | ARTURA 2DR COUPE | SANTA CRUZ 4DR PICKUP | ATLAS 4DR SUV FWD | BRONCO 4DR 2.7L SUV
  - 同じ表の列：MAKE, MYR, OL, OW, OH, WB, CW, A

## g1511（1 列）
- 見出し：MYR
- 例1 値：22 | 22 | 22 | 22 | 22
  - 同じ表の列：MAKE, MODEL, OL, OW, OH, WB, CW, A

## g1512（1 列）
- 見出し：OL
- 例1 値：469 | 491 | 471 | 495 | 525
  - 同じ表の列：MAKE, MODEL, MYR, OW, OH, WB, CW, A

## g1513（1 列）
- 見出し：OW
- 例1 値：197 | 189 | 199 | 186 | 198
  - 同じ表の列：MAKE, MODEL, MYR, OL, OH, WB, CW, A

## g1514（1 列）
- 見出し：OH
- 例1 値：150 | 163 | 189 | 161 | 175
  - 同じ表の列：MAKE, MODEL, MYR, OL, OW, WB, CW, A

## g1515（1 列）
- 見出し：WB
- 例1 値：270 | 265 | 300 | 308 | 320
  - 同じ表の列：MAKE, MODEL, MYR, OL, OW, OH, CW, A

## g1516（1 列）
- 見出し：CW
- 例1 値：2095 | 2091 | 1899 | 1669 | 2210
  - 同じ表の列：MAKE, MODEL, MYR, OL, OW, OH, WB, A

## g1517（1 列）
- 見出し：A
- 例1 値：129 | N/A | 137 | 119 | 119
  - 同じ表の列：MAKE, MODEL, MYR, OL, OW, OH, WB, CW

## g1518（1 列）
- 見出し：B
- 例1 値：142 | 203 | 49 | 49 | 157
  - 同じ表の列：MAKE, MODEL, MYR, OL, OW, OH, WB, CW

## g1519（1 列）
- 見出し：Region
- 例1 値：Saskatchewan | British Columbia | Alberta | Western Canada | Manitoba
  - 同じ表の列：Value of exports

## g1520（1 列）
- 見出し：Value of exports
- 例1 値：18,641 | 207,768 | 50,125 | 19,317 | 119,685
  - 同じ表の列：Region

## g1521（1 列）
- 見出し：2018-2019
- 例1 値：15.6%
  - 同じ表の列：2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1522（1 列）
- 見出し：2017-2018 (2)
- 例1 値：14.9%
  - 同じ表の列：2018-2019, 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1523（1 列）
- 見出し：2016-2017 (1)
- 例1 値：15.3%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1524（1 列）
- 見出し：2015-2016
- 例1 値：9.2%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1525（1 列）
- 見出し：2014-2015
- 例1 値：7.6%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1526（1 列）
- 見出し：2013-2014
- 例1 値：7.8%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2012-2013, 2011-2012, 2010-2011

## g1527（1 列）
- 見出し：2012-2013
- 例1 値：9.5%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2011-2012, 2010-2011

## g1528（1 列）
- 見出し：2011-2012
- 例1 値：9.3%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2010-2011

## g1529（1 列）
- 見出し：2010-2011
- 例1 値：8.3%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012

## g1530（1 列）
- 見出し：assetid
- 例1 値：1541519 | 1543184 | 1544232 | 1543180 | 1542268
  - 同じ表の列：class, type, company, contract, assetmanager, primaryservicemanag…, conditionrating, evaluationdate

## g1531（1 列）
- 見出し：type
- 例1 値：Feature Lighting | Feature Lighting | Feature Lighting | Feature Lighting | Feature Lighting
  - 同じ表の列：assetid, class, company, contract, assetmanager, primaryservicemanag…, conditionrating, evaluationdate

## g1532（1 列）
- 見出し：company
- 例1 値：City of Melbourne | City of Melbourne | City of Melbourne | City of Melbourne | City of Melbourne
  - 同じ表の列：assetid, class, type, contract, assetmanager, primaryservicemanag…, conditionrating, evaluationdate

## g1533（1 列）
- 見出し：contract
- 例1 値：Public Lighting Maintenance Services | Public Lighting Maintenance Services | Public Lighting Maintenance Services | Public Lighting Maintenance Services | Public Lighting Maintenance Services
  - 同じ表の列：assetid, class, type, company, assetmanager, primaryservicemanag…, conditionrating, evaluationdate

## g1534（1 列）
- 見出し：assetmanager
- 例1 値：City Infrastructure | City Infrastructure | City Infrastructure | City Infrastructure | City Infrastructure
  - 同じ表の列：assetid, class, type, company, contract, primaryservicemanag…, conditionrating, evaluationdate

## g1535（1 列）
- 見出し：primaryservicemanager
- 例1 値：City Infrastructure | City Infrastructure | City Infrastructure | City Infrastructure | City Infrastructure
  - 同じ表の列：assetid, class, type, company, contract, assetmanager, conditionrating, evaluationdate

## g1536（1 列）
- 見出し：conditionrating
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：assetid, class, type, company, contract, assetmanager, primaryservicemanag…, evaluationdate

## g1537（1 列）
- 見出し：evaluationdate
- 例1 値：2024-06-28 | 2024-06-28 | 2024-06-28 | 2024-06-28 | 2024-06-28
  - 同じ表の列：assetid, class, type, company, contract, assetmanager, primaryservicemanag…, conditionrating

## g1538（1 列）
- 見出し：roadsegmentdescription
- 例1 値：Intersection of Lonsdale Street and Rus… | Collins Landing between Australian Whar… | Collins Landing between Australian Whar… | Yarra River | Webb Bridge between North Wharf Road an…
  - 同じ表の列：assetid, class, type, company, contract, assetmanager, primaryservicemanag…, conditionrating

## g1539（1 列）
- 見出し：2020-21
- 例1 値：11 | - | - | 2 | 1
  - 同じ表の列：2019-20, 2018-19, 2017-18, 2016-17, 2015-16 8, 2014-15 8, 2013-14 9

## g1540（1 列）
- 見出し：2019-20
- 例1 値：3 4 | 0 5 | - | Number of executives as at 30 June 2020 | 1 3
  - 同じ表の列：2020-21, 2018-19, 2017-18, 2016-17, 2015-16 8, 2014-15 8, 2013-14 9

## g1541（1 列）
- 見出し：2018-19
- 例1 値：1 | 0 | 12 | 1 | -
  - 同じ表の列：2020-21, 2019-20, 2017-18, 2016-17, 2015-16 8, 2014-15 8, 2013-14 9

## g1542（1 列）
- 見出し：2017-18
- 例1 値：11 | - | 0 | - | 3
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2016-17, 2015-16 8, 2014-15 8, 2013-14 9

## g1543（1 列）
- 見出し：2016-17
- 例1 値：- | 1 | 1 | - | 1
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2017-18, 2015-16 8, 2014-15 8, 2013-14 9

## g1544（1 列）
- 見出し：2015-16 8
- 例1 値：- | 1 | - | 1 | -
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2017-18, 2016-17, 2014-15 8, 2013-14 9

## g1545（1 列）
- 見出し：2014-15 8
- 例1 値：- | - | 1 | 1 | 3
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2017-18, 2016-17, 2015-16 8, 2013-14 9

## g1546（1 列）
- 見出し：2013-14 9
- 例1 値：- | - | 5 | - | -
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2017-18, 2016-17, 2015-16 8, 2014-15 8

## g1547（1 列）
- 見出し：Device ID
- 例1 値：0004a30b001c42b7 | 0004a30b001c42b7 | 0004a30b001c5fbb | 0004a30b00269004 | 0004a30b001b15cf
  - 同じ表の列：Time, Temperature (°C), Humidity (%), Average Sound (dBA), Peak Sound (dBA), PM10 Particulate Ma…, PM2.5 Particulate M…, PM1 Particulate Mat…

## g1548（1 列）
- 見出し：Average Sound (dBA)
- 例1 値：61.0 | 64.0 | 63.0 | 60.0 | 65.0
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Peak Sound (dBA), PM10 Particulate Ma…, PM2.5 Particulate M…, PM1 Particulate Mat…

## g1549（1 列）
- 見出し：Peak Sound (dBA)
- 例1 値：78.0 | 70.0 | 81.0 | 84.0 | 85.0
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Average Sound (dBA), PM10 Particulate Ma…, PM2.5 Particulate M…, PM1 Particulate Mat…

## g1550（1 列）
- 見出し：PM10 Particulate Matter (μg/m3)
- 例1 値：7.0 | 0.0 | 0.0 | 3.0 | 5.0
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Average Sound (dBA), Peak Sound (dBA), PM2.5 Particulate M…, PM1 Particulate Mat…

## g1551（1 列）
- 見出し：PM2.5 Particulate Matter (μg/m3)
- 例1 値：3.0 | 4.0 | 1.0 | 6.0 | 0.0
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Average Sound (dBA), Peak Sound (dBA), PM10 Particulate Ma…, PM1 Particulate Mat…

## g1552（1 列）
- 見出し：PM1 Particulate Matter (μg/m3)
- 例1 値：2.0 | 1.0 | 13.0 | 5.0 | 0.0
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Average Sound (dBA), Peak Sound (dBA), PM10 Particulate Ma…, PM2.5 Particulate M…

## g1553（1 列）
- 見出し：Carbon Monoxide CO (ppm)
- 例1 値：-2.872 | -2.44 | -2.359 | -5.349 | -2.884
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Average Sound (dBA), Peak Sound (dBA), PM10 Particulate Ma…, PM2.5 Particulate M…

## g1554（1 列）
- 見出し：site_id
- 例1 値：164-02 | 112-01 | 212-03 | 198-02 | 194-01
  - 同じ表の列：timetable_id, lat, lon

## g1555（1 列）
- 見出し：timetable_id
- 例1 値：799 | 799 | 799 | 799 | 798
  - 同じ表の列：site_id, lat, lon

## g1556（1 列）
- 見出し：FID
- 例1 値：ESTACIONAMENTO_ROTATIVO_IDOSO_SEGUNDA_S… | ESTACIONAMENTO_ROTATIVO_IDOSO_SEGUNDA_S… | ESTACIONAMENTO_ROTATIVO_IDOSO_SEGUNDA_S… | ESTACIONAMENTO_ROTATIVO_IDOSO_SEGUNDA_S… | ESTACIONAMENTO_ROTATIVO_IDOSO_SEGUNDA_S…
  - 同じ表の列：ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g1557（1 列）
- 見出し：ID_EDESP
- 例1 値：1633 | 1250 | 514 | 719 | 1249
  - 同じ表の列：FID, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g1558（1 列）
- 見出し：DESTINACAO_ESPECIFICA
- 例1 値：PESSOA IDOSA | PESSOA IDOSA | PESSOA IDOSA | PESSOA IDOSA | PESSOA IDOSA
  - 同じ表の列：FID, ID_EDESP, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g1559（1 列）
- 見出し：DIA_REGRA_OPERACAO
- 例1 値：SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g1560（1 列）
- 見出し：PERIODO_VALIDO_REGRA_OPERACAO
- 例1 値：08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## 答えの雛形

```
g1441	
g1442	
g1443	
g1444	
g1445	
g1446	
g1447	
g1448	
g1449	
g1450	
g1451	
g1452	
g1453	
g1454	
g1455	
g1456	
g1457	
g1458	
g1459	
g1460	
g1461	
g1462	
g1463	
g1464	
g1465	
g1466	
g1467	
g1468	
g1469	
g1470	
g1471	
g1472	
g1473	
g1474	
g1475	
g1476	
g1477	
g1478	
g1479	
g1480	
g1481	
g1482	
g1483	
g1484	
g1485	
g1486	
g1487	
g1488	
g1489	
g1490	
g1491	
g1492	
g1493	
g1494	
g1495	
g1496	
g1497	
g1498	
g1499	
g1500	
g1501	
g1502	
g1503	
g1504	
g1505	
g1506	
g1507	
g1508	
g1509	
g1510	
g1511	
g1512	
g1513	
g1514	
g1515	
g1516	
g1517	
g1518	
g1519	
g1520	
g1521	
g1522	
g1523	
g1524	
g1525	
g1526	
g1527	
g1528	
g1529	
g1530	
g1531	
g1532	
g1533	
g1534	
g1535	
g1536	
g1537	
g1538	
g1539	
g1540	
g1541	
g1542	
g1543	
g1544	
g1545	
g1546	
g1547	
g1548	
g1549	
g1550	
g1551	
g1552	
g1553	
g1554	
g1555	
g1556	
g1557	
g1558	
g1559	
g1560	
```
