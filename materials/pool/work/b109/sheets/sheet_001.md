# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]">
- 例1 値：<tr><th colspan="4"><hr></th></tr> | <tr><td valign="top"><img src="/icons/t… | <tr><td valign="top"><img src="/icons/t… | <tr><td valign="top"><img src="/icons/t… | <tr><td valign="top"><img src="/icons/t…
  - 同じ表の列：</a></td><td align=…

## g0002（1 列）
- 見出し：</a></td><td align="right">2024-01-10 11:24 </td><td align=
- 例1 値：</a></td><td align="right">2024-01-10 1… | </a></td><td align="right">2024-01-10 1… | </a></td><td align="right">2024-01-10 1… | </a></td><td align="right">2024-01-10 1… | </a></td><td align="right">2024-01-10 0…
  - 同じ表の列：<tr><td valign="top…

## g0003（1 列）
- 見出し：FiscalYear_AnneeFinanciere
- 例1 値：2016-2017 | 2017-2018 | 2016-2017 | 2026-2027 | 2023-2024
  - 同じ表の列：ProjectNumber_Numer…, SubmissionStatusEn_…, SubmissionStatusFr_…

## g0004（1 列）
- 見出し：ProjectNumber_NumeroProjet
- 例1 値：AAFC17-040 | AAFC12-021 | AAFC26-014 | AAFC16-058 | AAFC21-010
  - 同じ表の列：FiscalYear_AnneeFin…, SubmissionStatusEn_…, SubmissionStatusFr_…

## g0005（1 列）
- 見出し：SubmissionStatusEn_StatutSoumissionAn
- 例1 値：D.3.2 Review Complete | Submitted to Registrant | D.3.2 Review Complete | D.3.2 Review Complete | D.3.2 Review Complete
  - 同じ表の列：FiscalYear_AnneeFin…, ProjectNumber_Numer…, SubmissionStatusFr_…

## g0006（1 列）
- 見出し：SubmissionStatusFr_StatutSoumissionFr
- 例1 値：Révision du D.3.2 terminée | Révision du D.3.2 terminée | Révision du D.3.2 terminée | Révision du D.3.2 terminée | Révision du D.3.2 terminée
  - 同じ表の列：FiscalYear_AnneeFin…, ProjectNumber_Numer…, SubmissionStatusEn_…

## g0007（1 列）
- 見出し：GRID_ID
- 例1 値：340 | 774 | 749 | 570 | 524
  - 同じ表の列：UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0008（1 列）
- 見出し：UNCCLASS
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：GRID_ID, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0009（1 列）
- 見出し：BOWHEAD_SUMMER_SENST
- 例1 値：3 | 2 | 3 | 3.6 | 2
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0010（1 列）
- 見出し：BOWHEAD_WINTER_SENST
- 例1 値：3 | 3 | 3 | 3.1 | 3
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0011（1 列）
- 見出し：CHAR_SUMMER_SENST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0012（1 列）
- 見出し：CHAR_WINTER_SENST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0013（1 列）
- 見出し：MIGRT_BIRD_SUMMER_SENST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_WINTER_S…, POLAR_BEAR_SUMMER_S…

## g0014（1 列）
- 見出し：MIGRT_BIRD_WINTER_SENST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, POLAR_BEAR_SUMMER_S…

## g0015（1 列）
- 見出し：POLAR_BEAR_SUMMER_SENST
- 例1 値：1 | 4 | 4 | 1 | 1
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…

## g0016（1 列）
- 見出し：POLAR_BEAR_WINTER_SENST
- 例1 値：3 | 3 | 3 | 3 | 4.4
  - 同じ表の列：GRID_ID, UNCCLASS, BOWHEAD_SUMMER_SENST, BOWHEAD_WINTER_SENST, CHAR_SUMMER_SENST, CHAR_WINTER_SENST, MIGRT_BIRD_SUMMER_S…, MIGRT_BIRD_WINTER_S…

## g0017（2 列）
- 見出し：Date
- 例1 値：2020-09-01 | 2018-01-01 | 2018-10-01 | 2011-06-01 | 2025-12-01
  - 同じ表の列：Month, Year, Company, Pipeline, Key Point, Direction Of Flow, Trade Type, Product
- 例2 値：2024-01-24 | 2023-01-19 | 2024-04-05 | 2022-09-18 | 2023-07-04
  - 同じ表の列：Location, region, measureid, fractionid, viral_load, seven_day_rolling_a…, pruid

## g0018（1 列）
- 見出し：Month
- 例1 値：2 | 3 | 3 | 2 | 6
  - 同じ表の列：Date, Year, Company, Pipeline, Key Point, Direction Of Flow, Trade Type, Product

## g0019（4 列）
- 見出し：Year
- 例1 値：2016 | 2022 | 2016 | 2016 | 2011
  - 同じ表の列：Date, Month, Company, Pipeline, Key Point, Direction Of Flow, Trade Type, Product
- 例2 値：2014 | 2015 | 2014 | 2014 | 2014
  - 同じ表の列：source, month, grain_code, global_region, ktonnes, grade, sector, destination

## g0020（1 列）
- 見出し：Company
- 例1 値：South Bow GP (Canada) Ltd. | South Bow GP (Canada) Ltd. | South Bow GP (Canada) Ltd. | South Bow GP (Canada) Ltd. | South Bow GP (Canada) Ltd.
  - 同じ表の列：Date, Month, Year, Pipeline, Key Point, Direction Of Flow, Trade Type, Product

## g0021（1 列）
- 見出し：Pipeline
- 例1 値：Keystone pipeline | Keystone pipeline | Keystone pipeline | Keystone pipeline | Keystone pipeline
  - 同じ表の列：Date, Month, Year, Company, Key Point, Direction Of Flow, Trade Type, Product

## g0022（1 列）
- 見出し：Key Point
- 例1 値：International boundary at or near Haske… | International boundary at or near Haske… | International boundary at or near Haske… | International boundary at or near Haske… | International boundary at or near Haske…
  - 同じ表の列：Date, Month, Year, Company, Pipeline, Direction Of Flow, Trade Type, Product

## g0023（1 列）
- 見出し：Direction Of Flow
- 例1 値：south | south | south | south | south
  - 同じ表の列：Date, Month, Year, Company, Pipeline, Key Point, Trade Type, Product

## g0024（1 列）
- 見出し：Trade Type
- 例1 値：export | export | export | export | export
  - 同じ表の列：Date, Month, Year, Company, Pipeline, Key Point, Direction Of Flow, Product

## g0025（1 列）
- 見出し：Product
- 例1 値：total | domestic heavy | domestic light | domestic light | total
  - 同じ表の列：Date, Month, Year, Company, Pipeline, Key Point, Direction Of Flow, Trade Type

## g0026（1 列）
- 見出し：Throughput (1000 m3/d)
- 例1 値：55.40953729032258 | 82.38 | 98.7 | 98.6 | 56.05
  - 同じ表の列：Date, Month, Year, Company, Pipeline, Key Point, Direction Of Flow, Trade Type

## g0027（1 列）
- 見出し：Period
- 例1 値：03/01/1990 | 10/01/1990 | 12/01/1990 | 02/01/1991 | 05/01/1990
  - 同じ表の列：Activity, Source, Destination, Energy (MW.h), Total Value (CAN$), Price (CAN$/MW.h)

## g0028（1 列）
- 見出し：Activity
- 例1 値：Exports | Exports | Imports | Exports | Exports
  - 同じ表の列：Period, Source, Destination, Energy (MW.h), Total Value (CAN$), Price (CAN$/MW.h)

## g0029（1 列）
- 見出し：Source
- 例1 値：New England-ISO | Total | Montana | Ontario | Manitoba
  - 同じ表の列：Period, Activity, Destination, Energy (MW.h), Total Value (CAN$), Price (CAN$/MW.h)

## g0030（1 列）
- 見出し：Destination
- 例1 値：Alberta | Massachusetts | New York | Maine | New York
  - 同じ表の列：Period, Activity, Source, Energy (MW.h), Total Value (CAN$), Price (CAN$/MW.h)

## g0031（1 列）
- 見出し：Energy (MW.h)
- 例1 値：278136.5680 | 2094.2000 | 116944.3000 | 86672.0000 | 35535.0000
  - 同じ表の列：Period, Activity, Source, Destination, Total Value (CAN$), Price (CAN$/MW.h)

## g0032（1 列）
- 見出し：Total Value (CAN$)
- 例1 値：43281.5900 | 6144363.0400 | 9547.1400 | 8561113.4300 | 504.5600
  - 同じ表の列：Period, Activity, Source, Destination, Energy (MW.h), Price (CAN$/MW.h)

## g0033（1 列）
- 見出し：Price (CAN$/MW.h)
- 例1 値：51.85 | 52.11 | 43.88 | 61.03 | 24.27
  - 同じ表の列：Period, Activity, Source, Destination, Energy (MW.h), Total Value (CAN$)

## g0034（1 列）
- 見出し：Week End
- 例1 値：07/28/1992 | 05/24/1994 | 05/03/1994 | 01/29/1991 | 05/30/1995
  - 同じ表の列：Region, Crude Volumes For T…, Percent Of Capacity, 4 Week Average, YTD Average, Unit

## g0035（1 列）
- 見出し：Region
- 例1 値：Quebec & Eastern Canada | Quebec & Eastern Canada | Western Canada | Ontario | Western Canada
  - 同じ表の列：Week End, Crude Volumes For T…, Percent Of Capacity, 4 Week Average, YTD Average, Unit

## g0036（1 列）
- 見出し：Crude Volumes For The Week
- 例1 値：85.200 | 69.920 | 51.700 | 65.650 | 64.950
  - 同じ表の列：Week End, Region, Percent Of Capacity, 4 Week Average, YTD Average, Unit

## g0037（1 列）
- 見出し：Percent Of Capacity
- 例1 値：84.340 | 86.310 | 71.690 | 80.290 | 89.760
  - 同じ表の列：Week End, Region, Crude Volumes For T…, 4 Week Average, YTD Average, Unit

## g0038（1 列）
- 見出し：4 Week Average
- 例1 値：80.780 | 110.180 | 101.100 | 65.890 | 104.190
  - 同じ表の列：Week End, Region, Crude Volumes For T…, Percent Of Capacity, YTD Average, Unit

## g0039（1 列）
- 見出し：YTD Average
- 例1 値：74.620 | 71.220 | 77.870 | 87.940 | 70.160
  - 同じ表の列：Week End, Region, Crude Volumes For T…, Percent Of Capacity, 4 Week Average, Unit

## g0040（1 列）
- 見出し：Unit
- 例1 値：thousand cubic metres per day | thousand cubic metres per day | thousand cubic metres per day | thousand cubic metres per day | thousand cubic metres per day
  - 同じ表の列：Week End, Region, Crude Volumes For T…, Percent Of Capacity, 4 Week Average, YTD Average

## g0041（1 列）
- 見出し：source
- 例1 値：Canadian Grain Commission | Canadian Grain Commission | Canadian Grain Commission | Canadian Grain Commission | Canadian Grain Commission
  - 同じ表の列：year, month, grain_code, global_region, ktonnes, grade, sector, destination

## g0042（1 列）
- 見出し：month
- 例1 値：Sep | Dec | Sep | Nov | Dec
  - 同じ表の列：source, year, grain_code, global_region, ktonnes, grade, sector, destination

## g0043（1 列）
- 見出し：grain_code
- 例1 値：Soybeans | Wheat | Amber Durum | Wheat | Amber Durum
  - 同じ表の列：source, year, month, global_region, ktonnes, grade, sector, destination

## g0044（1 列）
- 見出し：global_region
- 例1 値：Western Hemisphere | Asia | Western Hemisphere | Western Hemisphere | Asia
  - 同じ表の列：source, year, month, grain_code, ktonnes, grade, sector, destination

## g0045（1 列）
- 見出し：ktonnes
- 例1 値：3.145 | 0.824 | 126 | 27.5 | 3.3
  - 同じ表の列：source, year, month, grain_code, global_region, grade, sector, destination

## g0046（1 列）
- 見出し：grade
- 例1 値：No.2 CE | No.1 CANADA | No.2 CW RS | No.2 CW RS | No.1 CW AD
  - 同じ表の列：source, year, month, grain_code, global_region, ktonnes, sector, destination

## g0047（1 列）
- 見出し：sector
- 例1 値：Pacific | Thunder Bay | Pacific | Pacific | Prairie Elevators
  - 同じ表の列：source, year, month, grain_code, global_region, ktonnes, grade, destination

## g0048（1 列）
- 見出し：destination
- 例1 値：Peru | Venezuela | Turkey | Senegal | Norway
  - 同じ表の列：source, year, month, grain_code, global_region, ktonnes, grade, sector

## g0049（1 列）
- 見出し：NDA Section
- 例1 値：97 | 130 (5(1) CDSA*) | 130 (320.13(1) CC) | 116 | 130 (5(2) CDSA)
  - 同じ表の列：2019-2020, 2020-2021

## g0050（1 列）
- 見出し：2019-2020
- 例1 値：0 | 6 | 0 | 5 | 2
  - 同じ表の列：NDA Section, 2020-2021

## g0051（1 列）
- 見出し：2020-2021
- 例1 値：1 | 0 | # | 1 | 0
  - 同じ表の列：NDA Section, 2019-2020

## g0052（1 列）
- 見出し：Canadian Armes Forces Employment Equity Goals
- 例1 値：Reg F + PRes Officer | Total Reg F + PRes | Total Navy | Army Officer | Reg Forces Non-Commisioned Members
  - 同じ表の列：Women, Aboriginal Peoples, Visible Minorities, Persons with Disabi…

## g0053（1 列）
- 見出し：Women
- 例1 値：16.40% | 19.10% | 20.00% | 19.50% | 16.00%
  - 同じ表の列：Canadian Armes Forc…, Aboriginal Peoples, Visible Minorities, Persons with Disabi…

## g0054（1 列）
- 見出し：Aboriginal Peoples
- 例1 値：2.10% | 2.80% | 3.30% | 1.90% | 1.80%
  - 同じ表の列：Canadian Armes Forc…, Women, Visible Minorities, Persons with Disabi…

## g0055（1 列）
- 見出し：Visible Minorities
- 例1 値：9.90% | 11.70% | 11.30% | 12.50% | 11.60%
  - 同じ表の列：Canadian Armes Forc…, Women, Aboriginal Peoples, Persons with Disabi…

## g0056（1 列）
- 見出し：Persons with Disabilities
- 例1 値：0.80% | 1.00% | 1.40% | 0.70% | 1.40%
  - 同じ表の列：Canadian Armes Forc…, Women, Aboriginal Peoples, Visible Minorities

## g0057（1 列）
- 見出し：Neutral Citation
- 例1 値：Standing court martial | Cour Martiale permanente | Dossier | Cour Martiale | Cour Martiale générale
  - 同じ表の列：Unique reference nu…

## g0058（1 列）
- 見出し：Unique reference number given to a particular case to identi
- 例1 値：Procédure judiciaire qui a lieu avant l… | The General Court Martial is comprised … | The official record of all of the proce… | Formal military courts presided over by… | Court proceeding that takes place befor…
  - 同じ表の列：Neutral Citation

## g0059（1 列）
- 見出し：Table|Tableau
- 例1 値：Other_Codes_Autres.csv | Data_Dictionary_Dictionaire_Donnés.csv | Point_count_data_Données_point_d’écoute… | Point_count_data_Données_point_d’écoute… | Data_Dictionary_Dictionaire_Donnés.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0060（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：Longitude|Longitude | Behaviour first interval|Comportement l… | Point count comment|Commentaire sur le … | Creek noise|Bruit du ruisseau | n/a
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0061（3 列）
- 見出し：Data_type_en
- 例1 値：text | short integer | text | text | text
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：short integer | text | text | text | short integer
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0062（1 列）
- 見出し：Type_de_données_fr
- 例1 値：texte | texte | texte | texte | texte
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0063（3 列）
- 見出し：NULL_exists|NULL_existe
- 例1 値：N|N | Y|O | Y|O | N|N | Y|O
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：Y|O | N|N | N|N | N|N | N|N
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…

## g0064（3 列）
- 見出し：Field_length|Longueur_du_champ
- 例1 値：4 | 43 | 95 | 2 | 2
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Values_lookup|Reche…
- 例2 値：96 | 2 | 25 | 23 | 5
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Values_lookup|Reche…

## g0065（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：Month | Behaviour | Wind | Distance | Quadrant
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0066（1 列）
- 見出し：Table|Tableau
- 例1 値：Data_Dictionary_Dictionaire_Donnés.csv | Data_Dictionary_Dictionaire_Donnés.csv | Point_count_data_Données_point_d’écoute… | Visits_Visites.csv | Visits_Visites.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0067（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | n/a | n/a | Species code|Code de l'espèce | n/a
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0068（1 列）
- 見出し：Type_de_données_fr
- 例1 値：entier court | décimal | texte | entier court | entier court
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0069（2 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：NULL_exists|NULL_existe | Wind | Wind | Sex | Behaviour
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…
- 例2 値：Age | NULL_exists|NULL_existe | Behaviour | Wind | Quadrant
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0070（1 列）
- 見出し：Table|Tableau
- 例1 値：Data_Dictionary_Dictionaire_Donnés.csv | Point_count_data_Données_point_d’écoute… | Point_count_data_Données_point_d’écoute… | Data_Dictionary_Dictionaire_Donnés.csv | Data_Dictionary_Dictionaire_Donnés.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0071（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | n/a | Day|Jour | n/a | Minute|Minute
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0072（1 列）
- 見出し：Type_de_données_fr
- 例1 値：texte | entier court | entier court | texte | texte
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0073（1 列）
- 見出し：Period
- 例1 値：JAN./JAN. | OCT./OCT. | OCT./OCT. | OCT./OCT. | OCT./OCT.
  - 同じ表の列：Year, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …, GIS Married Maximum…

## g0074（1 列）
- 見出し：OAS (age 65 and over)
- 例1 値：132.90 | 505.83 | 516.96 | 135.43 | 613.53
  - 同じ表の列：Year, Period, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …, GIS Married Maximum…

## g0075（1 列）
- 見出し：OAS (age 65 to 74)
- 例1 値：... | ... | ... | ... | ...
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …, GIS Married Maximum…

## g0076（1 列）
- 見出し：OAS (age 75 and over)
- 例1 値：... | ... | ... | ... | ...
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …, GIS Married Maximum…

## g0077（1 列）
- 見出し：GIS Single Top-Up Amount
- 例1 値：... | 143.07 | 52.81 | 165.04 | ...
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Maximum …, GIS Married Top-Up …, GIS Married Maximum…

## g0078（1 列）
- 見出し：GIS Single Maximum Amount
- 例1 値：1,065.47 | 773.60 | 560.69 | 916.38 | 652.51
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Married Top-Up …, GIS Married Maximum…

## g0079（1 列）
- 見出し：GIS Married Top-Up Amount
- 例1 値：... | 37.94 | ... | ... | 49.30
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Maximum…

## g0080（1 列）
- 見出し：GIS Married Maximum Amount
- 例1 値：... | 95.56 | 342.67 | 628.09 | 335.59
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …

## g0081（1 列）
- 見出し：ALW Married Top-Up Amount
- 例1 値：39.12 | ... | ... | ... | ...
  - 同じ表の列：Year, Period, OAS (age 65 and ove…, OAS (age 65 to 74), OAS (age 75 and ove…, GIS Single Top-Up A…, GIS Single Maximum …, GIS Married Top-Up …

## g0082（1 列）
- 見出し：Group(e)
- 例1 値：Nicola | Okanagan | Supplementary | Supplementary | Supplementary
  - 同じ表の列：Site, Elevation, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, n2, sd_n2

## g0083（1 列）
- 見出し：Site
- 例1 値：112 | 113 | 17 | 111 | 1
  - 同じ表の列：Group(e), Elevation, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, n2, sd_n2

## g0084（1 列）
- 見出し：Elevation
- 例1 値：600 | 750 | 850 | 850 | 1050
  - 同じ表の列：Group(e), Site, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, n2, sd_n2

## g0085（1 列）
- 見出し：Foliage/Feuillage(tons/ha)
- 例1 値：7.064 | * | * | 7.064 | 13.37
  - 同じ表の列：Group(e), Site, Elevation, Year/Année, n1, sd_n1, n2, sd_n2

## g0086（1 列）
- 見出し：Year/Année
- 例1 値：2008 | 2011 | 2007 | 2005 | 2004
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, n1, sd_n1, n2, sd_n2

## g0087（1 列）
- 見出し：n1
- 例1 値：11.01446388 | 73.29260434 | 154.9882226 | 29.5803474 | *
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, Year/Année, sd_n1, n2, sd_n2

## g0088（1 列）
- 見出し：sd_n1
- 例1 値：76.94948564 | 38.15742612 | 53.984204 | * | 69.88790713
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, Year/Année, n1, n2, sd_n2

## g0089（1 列）
- 見出し：n2
- 例1 値：* | 72.40873634 | 51.32113251 | 24.44812594 | 269.3594858
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, sd_n2

## g0090（1 列）
- 見出し：sd_n2
- 例1 値：* | 81.08164029 | * | 92.58064449 | 35.22617419
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, n2

## g0091（1 列）
- 見出し：N_n2
- 例1 値：10 | * | 10 | * | 10
  - 同じ表の列：Group(e), Site, Elevation, Foliage/Feuillage(t…, Year/Année, n1, sd_n1, n2

## g0092（1 列）
- 見出し：Immigrant status and period of immigration
- 例1 値：Non-immigrants | Before 1996 | 1996 to 2005 | Total - Immigrant status and period of … | Immigrants
  - 同じ表の列：Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario, Manitoba

## g0093（1 列）
- 見出し：Canada
- 例1 値：3837770 | 1620885 | 940195 | 6398855 | 20543700
  - 同じ表の列：Immigrant status an…, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario, Manitoba

## g0094（1 列）
- 見出し：Newfoundland and Labrador
- 例1 値：421170 | 5415 | 431045 | 8315 | 1215
  - 同じ表の列：Immigrant status an…, Canada, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario, Manitoba

## g0095（1 列）
- 見出し：Prince Edward Island
- 例1 値：107085 | 114195 | 6415 | 920 | 3455
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario, Manitoba

## g0096（1 列）
- 見出し：Nova Scotia / Nouvelle-Écosse
- 例1 値：7485 | 28690 | 8485 | 768060 | 717140
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, New Brunswick / Nou…, Quebec, Ontario, Manitoba

## g0097（1 列）
- 見出し：New Brunswick / Nouveau-Brunswick
- 例1 値：25890 | 593840 | 622440 | 5395 | 16530
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, Quebec, Ontario, Manitoba

## g0098（1 列）
- 見出し：Quebec
- 例1 値：227160 | 179040 | 496790 | 6474590 | 902990
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Ontario, Manitoba

## g0099（1 列）
- 見出し：Ontario
- 例1 値：2148600 | 410270 | 6912395 | 3442895 | 884025
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Manitoba

## g0100（1 列）
- 見出し：Manitoba
- 例1 値：43205 | 90000 | 774365 | 165005 | 31800
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario

## g0101（1 列）
- 見出し：Saskatchewan
- 例1 値：60500 | 29120 | 744685 | 11165 | 20215
  - 同じ表の列：Immigrant status an…, Canada, Newfoundland and La…, Prince Edward Island, Nova Scotia / Nouve…, New Brunswick / Nou…, Quebec, Ontario

## g0102（1 列）
- 見出し：Canada
- 例1 値：Ottawa - Gatineau (Quebec part) CMA | Halifax CMA | Yukon | Nunavut | London CMA
  - 同じ表の列：32852325, 25066475, 5794635, 1525135, 1268325, 837050, 588100, 381280

## g0103（1 列）
- 見出し：32852325
- 例1 値：1199125 | 31695 | 904905 | 714640 | 1215735
  - 同じ表の列：Canada, 25066475, 5794635, 1525135, 1268325, 837050, 588100, 381280

## g0104（1 列）
- 見出し：25066475
- 例1 値：3830 | 269860 | 787705 | 4988945 | 6693900
  - 同じ表の列：Canada, 32852325, 5794635, 1525135, 1268325, 837050, 588100, 381280

## g0105（1 列）
- 見出し：5794635
- 例1 値：25230 | 3795 | 599595 | 38210 | 1087115
  - 同じ表の列：Canada, 32852325, 25066475, 1525135, 1268325, 837050, 588100, 381280

## g0106（1 列）
- 見出し：1525135
- 例1 値：7905 | 944970 | 151710 | 59290 | 5725
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1268325, 837050, 588100, 381280

## g0107（1 列）
- 見出し：1268325
- 例1 値：70760 | 4730 | 10095 | 34435 | 79255
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1525135, 837050, 588100, 381280

## g0108（1 列）
- 見出し：837050
- 例1 値：2105 | 414655 | 29075 | 199355 | 6520
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1525135, 1268325, 588100, 381280

## g0109（1 列）
- 見出し：588100
- 例1 値：242140 | 370 | 9825 | 9455 | 55160
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1525135, 1268325, 837050, 381280

## g0110（1 列）
- 見出し：381280
- 例1 値：30 | 20590 | 1025 | 116380 | 10360
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1525135, 1268325, 837050, 588100

## g0111（1 列）
- 見出し：380620
- 例1 値：395 | 74990 | 3235 | 5525 | 0
  - 同じ表の列：Canada, 32852325, 25066475, 5794635, 1525135, 1268325, 837050, 588100

## g0112（1 列）
- 見出し：Geography
- 例1 値：London CMA | Yukon | Manitoba | Vancouver CMA | Newfoundland and Labrador
  - 同じ表の列：Total - Presence of…, Below low income cu…, Persons under 15 ye…, Without income, At or above low inc…, LICO concept not ap…

## g0113（1 列）
- 見出し：Total - Presence of total income and low income status befor
- 例1 値：33320 | 5521235 | 746685 | 1174345 | 1215735
  - 同じ表の列：Geography, Below low income cu…, Persons under 15 ye…, Without income, At or above low inc…, LICO concept not ap…

## g0114（1 列）
- 見出し：Below low income cut-offs (LICO) before tax (The "With incom
- 例1 値：158195 | 0 | 0 | 90900 | 69490
  - 同じ表の列：Geography, Total - Presence of…, Persons under 15 ye…, Without income, At or above low inc…, LICO concept not ap…

## g0115（1 列）
- 見出し：Persons under 15 years old
- 例1 値：29835 | 29270 | 20875 | 6830 | 31665
  - 同じ表の列：Geography, Total - Presence of…, Below low income cu…, Without income, At or above low inc…, LICO concept not ap…

## g0116（1 列）
- 見出し：Without income
- 例1 値：164400 | 2505 | 0 | 119195 | 10045
  - 同じ表の列：Geography, Total - Presence of…, Below low income cu…, Persons under 15 ye…, At or above low inc…, LICO concept not ap…

## g0117（1 列）
- 見出し：At or above low income cut-offs (LICO) before tax
- 例1 値：268920 | 782980 | 3527050 | 636965 | 444225
  - 同じ表の列：Geography, Total - Presence of…, Below low income cu…, Persons under 15 ye…, Without income, LICO concept not ap…

## g0118（1 列）
- 見出し：LICO concept not applicable (Includes economic families and
- 例1 値：210 | 48585 | 466155 | 56625 | 33320
  - 同じ表の列：Geography, Total - Presence of…, Below low income cu…, Persons under 15 ye…, Without income, At or above low inc…

## g0119（1 列）
- 見出し：InfluenzaSeasonandEpidemiologicalWeek
- 例1 値：201630 | Source: Influenza and Respiratory Infec… | 201604 | 201623 | 201549
  - 同じ表の列：TotalFluTests, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV, TotalParaTests

## g0120（1 列）
- 見出し：TotalFluTests
- 例1 値：1561 | 3836 | 12232 | 5330 | 3521
  - 同じ表の列：InfluenzaSeasonandE…, PositiveFluAH1N1pdm…, PositiveFluAH3, PositiveFluAunsubty…, TotalFluBPositive, TotalRSVTests, TotalPositiveRSV, TotalParaTests

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
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
