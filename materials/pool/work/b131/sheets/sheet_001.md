# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Date / dat
- 例1 値：6/1/2007 | 6/1/2002 | 4/1/2002 | 1/1/2008 | 7/1/2009
  - 同じ表の列：Region / région, Natural gas liquid …, Value / valeur, Units / unités

## g0002（1 列）
- 見出し：Region / région
- 例1 値：Western Canada / Ouest Canadien | Western Canada / Ouest Canadien | Western Canada / Ouest Canadien | Western Canada / Ouest Canadien | Western Canada / Ouest Canadien
  - 同じ表の列：Date / dat, Natural gas liquid …, Value / valeur, Units / unités

## g0003（1 列）
- 見出し：Natural gas liquid / liquides de gas naturel
- 例1 値：C4 | C3 | C4 | Spec. propane / propane pur | Total butanes / butanes - total
  - 同じ表の列：Date / dat, Region / région, Value / valeur, Units / unités

## g0004（1 列）
- 見出し：Value / valeur
- 例1 値：126.723907 | 32.607075 | 831.406 | 100.210636 | 526.218189
  - 同じ表の列：Date / dat, Region / région, Natural gas liquid …, Units / unités

## g0005（1 列）
- 見出し：Units / unités
- 例1 値：1 000 cubic metres / 1 000 mètres cubes | 1 000 cubic metres / 1 000 mètres cubes | 1 000 cubic metres / 1 000 mètres cubes | 1 000 cubic metres / 1 000 mètres cubes | 1 000 cubic metres / 1 000 mètres cubes
  - 同じ表の列：Date / dat, Region / région, Natural gas liquid …, Value / valeur

## g0006（1 列）
- 見出し：nom_français
- 例1 値：nbpc | strap_code | longitude_debut | dist_chalute_position | date_debut
  - 同じ表の列：définition_français, english_definition, jeux_de_donnees_dat…

## g0007（1 列）
- 見出し：définition_français
- 例1 値：Numéro de la strate | Hauteur des vagues (m) | Longitude de fin du trait (DD) | Résultat des opérations du trait | Type d'heure. L'heure d'été ou l'heure …
  - 同じ表の列：nom_français, english_definition, jeux_de_donnees_dat…

## g0008（1 列）
- 見出し：english_definition
- 例1 値：Ship number. 31 = Lady Hammond | Size (cm) | Description of the stage of maturity | Beaufort scale code for wind force | Fresh total weight of the specimen (g)
  - 同じ表の列：nom_français, définition_français, jeux_de_donnees_dat…

## g0009（1 列）
- 見出し：jeux_de_donnees_data_set
- 例1 値：lady_hammond_stations | lady_hammond_stations | lady_hammond_carbio | lady_hammond_captures_catches | lady_hammond_stations, lady_hammond_cap…
  - 同じ表の列：nom_français, définition_français, english_definition

## g0010（1 列）
- 見出し：nom_français
- 例1 値：age | vitesse_touage | no_poisson | type_trait | latitude_debut
  - 同じ表の列：définition_français, english_definition, jeux_de_donnees_dat…

## g0011（1 列）
- 見出し：définition_français
- 例1 値：Numéro séquentiel du trait | Vitesse de touage (nœuds) | Type de trait | Poids des gonades congelés (g) | Code de l'échelle Beaufort pour la forc…
  - 同じ表の列：nom_français, english_definition, jeux_de_donnees_dat…

## g0012（1 列）
- 見出し：english_definition
- 例1 値：Description of the sex | Standard length of fresh fish (mm) | Trawl distance (nautical mile) calculat… | Frozen stomacal content weight (g) | Result of the operations of the set
  - 同じ表の列：nom_français, définition_français, jeux_de_donnees_dat…

## g0013（1 列）
- 見出し：jeux_de_donnees_data_set
- 例1 値：needler_stations | needler_carbio | needler_stations | needler_stations | needler_carbio
  - 同じ表の列：nom_français, définition_français, english_definition

## g0014（1 列）
- 見出し：Unit Identification Code (UIC) - Code d'identification de l'
- 例1 値：96601 | 127 | 114 | 6428 | 118
  - 同じ表の列：Unit- Unité, Percentage of Rooms…

## g0015（1 列）
- 見出し：Unit- Unité
- 例1 値：3 Canadian Division Support Base Edmont… | 2 Canadian Division Support Base Valcar… | 3 Canadian Division Support Base Edmont… | 2 Canadian Division Support Group Opera… | Canadian Forces Base Shilo
  - 同じ表の列：Unit Identification…, Percentage of Rooms…

## g0016（1 列）
- 見出し：Percentage of Rooms Available- Pourcentage de chambres dispo
- 例1 値：40% | 58% | 41% | 94% | 83%
  - 同じ表の列：Unit Identification…, Unit- Unité

## g0017（1 列）
- 見出し：Table|Tableau
- 例1 値：BOSS_Flight_Lines | Survey_data_Données_relevé.csv | BOSS_Observation_Point | Species_Codes_Espèces.csv | Survey_data_Données_relevé.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, Data_type_GIS, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0018（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | n/a | pilot | n/a | survey_name
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, Data_type_GIS, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0019（1 列）
- 見出し：Data_type_en
- 例1 値：short integer | text | text | short integer | long integer
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, Data_type_GIS, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0020（1 列）
- 見出し：Type_de_données_fr
- 例1 値：entier long | texte | texte | entier long | entier court
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Data_type_GIS, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0021（1 列）
- 見出し：Data_type_GIS
- 例1 値：n/a | n/a | n/a | n/a | n/a
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0022（1 列）
- 見出し：NULL_exists|NULL_existe
- 例1 値：Y|O | N|N | N|N | N|N | N|N
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Data_type_GIS, Field_length|Longue…, Values_lookup|Reche…

## g0023（1 列）
- 見出し：Field_length|Longueur_du_champ
- 例1 値：4 | 10 | 0 | 4 | 6
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Data_type_GIS, NULL_exists|NULL_ex…, Values_lookup|Reche…

## g0024（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：Species_Codes_Espèces.csv | observer_num | data_type | data_type | Species_Codes_Espèces.csv
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Data_type_GIS, NULL_exists|NULL_ex…, Field_length|Longue…

## g0025（1 列）
- 見出し：InstitutionCode
- 例1 値：CWS | CWS | CWS | CWS | CWS
  - 同じ表の列：CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0026（1 列）
- 見出し：CollectionCode
- 例1 値：EWS25 | EWS25 | EWS25 | EWS25 | EWS25
  - 同じ表の列：InstitutionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0027（1 列）
- 見出し：SamplingEventIdentifier
- 例1 値：EWS25_76114_2023 | EWS25_76356_2022 | EWS25_76308_1996 | EWS25_76327_2023 | EWS25_76368_2013
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0028（1 列）
- 見出し：SamplingEventStructure
- 例1 値：SurveyAreaID_Year | SurveyAreaID_Year | SurveyAreaID_Year | SurveyAreaID_Year | SurveyAreaID_Year
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0029（1 列）
- 見出し：SurveyAreaIdentifier
- 例1 値：EWS25_56060 | EWS25_76356 | EWS25_76308 | EWS25_76345 | EWS25_76369
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0030（1 列）
- 見出し：CatalogNumber
- 例1 値：34446 | 34149 | 40238 | 17861 | 6906
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, GlobalUniqueIdentif…, BasisOfRecord, ProtocolType

## g0031（1 列）
- 見出し：GlobalUniqueIdentifier
- 例1 値：URN:catalog:CWS:EWS25:EWS25_76345_1990:… | URN:catalog:CWS:EWS25:EWS25_76369_1991:… | URN:catalog:CWS:EWS25:EWS25_76303_2008:… | URN:catalog:CWS:EWS25:EWS25_76214_2012:… | URN:catalog:CWS:EWS25:EWS25_76420_2014:…
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, BasisOfRecord, ProtocolType

## g0032（1 列）
- 見出し：BasisOfRecord
- 例1 値：observation | observation | observation | observation | observation
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, ProtocolType

## g0033（1 列）
- 見出し：ProtocolType
- 例1 値：area search | area search | area search | area search | area search
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord

## g0034（1 列）
- 見出し：ProtocolSpeciesTargeted
- 例1 値：waterfowl | waterfowl | waterfowl | waterfowl | waterfowl
  - 同じ表の列：InstitutionCode, CollectionCode, SamplingEventIdenti…, SamplingEventStruct…, SurveyAreaIdentifier, CatalogNumber, GlobalUniqueIdentif…, BasisOfRecord

## g0035（1 列）
- 見出し：CORE_ID
- 例1 値：915 | 515 | 105 | 219 | 647
  - 同じ表の列：SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0036（1 列）
- 見出し：SOURCE_SITEID
- 例1 値：Z-1989-6 | Z-1972-15 | Z-1981-46 | HL03 | Z-1971-11
  - 同じ表の列：CORE_ID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0037（1 列）
- 見出し：SOURCE_SUB
- 例1 値：Site 05 | Site 02 | Z-1981-36 | Z-1971-26-B | 15902 [B1800W+]
  - 同じ表の列：CORE_ID, SOURCE_SITEID, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0038（1 列）
- 見出し：LOC_SOURCE_FORMAT
- 例1 値：DD.2 | DD MM DS.2 | DD.2 | DD.2 | NBS
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0039（1 列）
- 見出し：LOC_ACCURACY_NOTES
- 例1 値：Format in Zoltai et al (2000) is DD.2, … | Format in Zoltai et al (2000) is DD.2, … | Format in Zoltai et al (2000) is DD.2, … | Format in Zoltai et al (2000) is DD.2, … | Format in Zoltai et al (2000) is DD.2, …
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0040（1 列）
- 見出し：PROV_TERR
- 例1 値：SK | AB | ON | NT | MB
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, SAMPLING_YR, SAMPLING_MONTH, SAMPLING_DATE

## g0041（1 列）
- 見出し：SAMPLING_YR
- 例1 値：1972 | 1972 | 1981 | 1981 | 1972
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_MONTH, SAMPLING_DATE

## g0042（1 列）
- 見出し：SAMPLING_MONTH
- 例1 値：7 | 7 | 7 | 6 | 6
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_DATE

## g0043（1 列）
- 見出し：SAMPLING_DATE
- 例1 値：24 | 26 | 18 | 31 | 19
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH

## g0044（1 列）
- 見出し：SAMPLING_ST
- 例1 値：SPDESC | ZMX | ZMX | REG | ZMX
  - 同じ表の列：CORE_ID, SOURCE_SITEID, SOURCE_SUB, LOC_SOURCE_FORMAT, LOC_ACCURACY_NOTES, PROV_TERR, SAMPLING_YR, SAMPLING_MONTH

## g0045（1 列）
- 見出し：OID
- 例1 値：11051 | 13387 | 13742 | 13414 | 13763
  - 同じ表の列：Lat_DD, Long_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mined_Quantity, Mine_Type

## g0046（1 列）
- 見出し：Lat_DD
- 例1 値：62.20250004 | 44.61620958 | 63.89250004 | 45.56480928 | 45.24896213
  - 同じ表の列：OID, Long_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mined_Quantity, Mine_Type

## g0047（1 列）
- 見出し：Long_DD
- 例1 値：-131.601667 | -60.10541202 | -61.21736243 | -130.47 | -105.735941
  - 同じ表の列：OID, Lat_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mined_Quantity, Mine_Type

## g0048（1 列）
- 見出し：Jurisdiction
- 例1 値：YT | SK | YT | SK | NS
  - 同じ表の列：OID, Lat_DD, Long_DD, Juris_ID, Status, Commodity_Code, Mined_Quantity, Mine_Type

## g0049（1 列）
- 見出し：Juris_ID
- 例1 値：392 | 013J/12/U 001 | 99 | 177 | 74
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Status, Commodity_Code, Mined_Quantity, Mine_Type

## g0050（1 列）
- 見出し：Status
- 例1 値：NULL | NULL | NULL | NULL | Abandoned Non-Uranium Sites
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Juris_ID, Commodity_Code, Mined_Quantity, Mine_Type

## g0051（1 列）
- 見出し：Commodity_Code
- 例1 値：CL | CL | CL | CL | CL
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Juris_ID, Status, Mined_Quantity, Mine_Type

## g0052（1 列）
- 見出し：Mined_Quantity
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mine_Type

## g0053（1 列）
- 見出し：Mine_Type
- 例1 値：Underground | Underground | Unknown | Unknown | Unknown
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mined_Quantity

## g0054（1 列）
- 見出し：Permit
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：OID, Lat_DD, Long_DD, Jurisdiction, Juris_ID, Status, Commodity_Code, Mined_Quantity

## g0055（1 列）
- 見出し：Droits de la personne
- 例1 値：Examen périodique universel | Déclaration d’ouverture du Canada, Conv… | À propos du Canada et le système des dr… | Guide sur la Charte canadienne des droi… | Droits par communauté ou groupe
  - 同じ表の列：https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 11465, 8617

## g0056（1 列）
- 見出し：https://www.canada.ca/en/services/culture/canadian-identity-
- 例1 値：https://www.canada.ca/en/canadian-herit… | https://www.canada.ca/en/canadian-herit… | https://www.canada.ca/en/canadian-herit… | https://www.canada.ca/en/canadian-herit… | https://www.canada.ca/en/canadian-herit…
  - 同じ表の列：Droits de la person…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 11465, 8617

## g0057（1 列）
- 見出し：https://www.canada.ca/fr/services/culture/identite-canadienn
- 例1 値：https://www.canada.ca/fr/patrimoine-can… | https://www.canada.ca/fr/patrimoine-can… | https://www.canada.ca/fr/patrimoine-can… | https://www.canada.ca/fr/patrimoine-can… | https://www.canada.ca/fr/patrimoine-can…
  - 同じ表の列：Droits de la person…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 11465, 8617

## g0058（1 列）
- 見出し：42986
- 例1 値：43031 | 43031 | 43031 | 43031 | 43032
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986_2, 43804, 43804_2, 11465, 8617

## g0059（1 列）
- 見出し：42986_2
- 例1 値：43031 | 42986 | 43031 | 43031 | 43031
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 43804, 43804_2, 11465, 8617

## g0060（1 列）
- 見出し：43804
- 例1 値：43804 | 43353 | 43033 | 43032 | 43811
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804_2, 11465, 8617

## g0061（1 列）
- 見出し：43804_2
- 例1 値：43255 | 43053 | 43350 | 43353 | 43053
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804, 11465, 8617

## g0062（1 列）
- 見出し：11465
- 例1 値：6021 | 90398 | 63 | 1423 | 13453
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 8617

## g0063（1 列）
- 見出し：8617
- 例1 値：23252 | 10939 | 5848 | 471 | 1152
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 11465

## g0064（1 列）
- 見出し：2099
- 例1 値：400 | 628 | 528 | Page did not exist | 94
  - 同じ表の列：Droits de la person…, https://www.canada.…, https://www.canada.…, 42986, 42986_2, 43804, 43804_2, 11465

## g0065（1 列）
- 見出し：Fscl-yr_Ex-fin
- 例1 値：2023-2024 | 2022-2023 | 2020-2021 | 2024-2025 | 2021-2022
  - 同じ表の列：Space-modernized_Es…, Total-office-space_…

## g0066（1 列）
- 見出し：Space-modernized_Espace-modernise
- 例1 値：167635.43 | 121237.23 | 98520.00 | 113730.16 | 150947.10
  - 同じ表の列：Fscl-yr_Ex-fin, Total-office-space_…

## g0067（1 列）
- 見出し：Total-office-space_Espace-de-bureau-total
- 例1 値：4550269.68 | 4548716.65 | 4787847.65 | 4866524.83 | 4749279.42
  - 同じ表の列：Fscl-yr_Ex-fin, Space-modernized_Es…

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
```
