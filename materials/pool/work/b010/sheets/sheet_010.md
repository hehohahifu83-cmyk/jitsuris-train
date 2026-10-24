# ラベル用シート 010 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_010.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1081（1 列）
- 見出し：packaged_inventory_units_federal_lh
- 例1 値：20485202 | 381783 | 12,235 | n/a / n/d | n/a / n/d
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## g1082（1 列）
- 見出し：packaged_inventory_units_prov_distributors_retailers
- 例1 値：n/a / n/d | 9660706 | 15759398.5854093 | 9976123.19683452 | 0
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…, unpackaged_producti…

## g1083（1 列）
- 見出し：sales_medical_units
- 例1 値：4 | 238792 | 248406 | 69 | 240406
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_non_medical_u…, unpackaged_producti…

## g1084（1 列）
- 見出し：sales_non_medical_units
- 例1 値：n/a / n/d | n/a / n/d | 168 | 7076329 | n/a / n/d
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, unpackaged_producti…

## g1085（1 列）
- 見出し：unpackaged_production_kg
- 例1 値：n/a / n/d | n/a / n/d | n/a / n/d | n/a / n/d | 153,010
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…

## g1086（1 列）
- 見出し：unpackaged_inventory_kg
- 例1 値：n/a / n/d | n/a / n/d | n/a / n/d | 984600 | n/a / n/d
  - 同じ表の列：year_month, product_type, unpackaged_inventor…, packaged_production…, packaged_inventory_…, packaged_inventory_…, sales_medical_units, sales_non_medical_u…

## g1087（1 列）
- 見出し：Table
- 例1 値：28 | 30 | 9a | 8 | 9
  - 同じ表の列：Title

## g1088（1 列）
- 見出し：Title
- 例1 値：Expenditure on R&D as a percentage of t… | Percentage of revenues derived from exp… | Financial Statements -- TO COME | Credit authorization status for busines… | Credit terms
  - 同じ表の列：Table

## g1089（1 列）
- 見出し：DGUID
- 例1 値：2021A00051001105 | 2021A00051315026 | 2021A00052413055 | 2021A00051009015 | 2021A00051002030
  - 同じ表の列：CSDUID, HICC_HNA, HNA_LINK

## g1090（1 列）
- 見出し：CSDUID
- 例1 値：2412010 | 2407908 | 1305045 | 1001254 | 1304006
  - 同じ表の列：DGUID, HICC_HNA, HNA_LINK

## g1091（1 列）
- 見出し：HICC_HNA
- 例1 値：Not Required | Not Required | Not Required | Not Required | Not Required
  - 同じ表の列：DGUID, CSDUID, HNA_LINK

## g1092（1 列）
- 見出し：HNA_LINK
- 例1 値：Not available | Not available | Not available | Not available | Not available
  - 同じ表の列：DGUID, CSDUID, HICC_HNA

## g1093（1 列）
- 見出し：Province of residence at the time of the refugee claim decis
- 例1 値：Nova Scotia | Ontario | British Columbia | Northwest Territories | British Columbia
  - 同じ表の列：Year, Outcome, Total

## g1094（1 列）
- 見出し：Outcome
- 例1 値：Other | Accepted | Rejected | Accepted | Other
  - 同じ表の列：Province of residen…, Year, Total

## g1095（1 列）
- 見出し：Total
- 例1 値：-- | 323 | -- | 158 | 2,330
  - 同じ表の列：Province of residen…, Year, Outcome

## g1096（1 列）
- 見出し：Region - English
- 例1 値：Ontario | Ontario | Quebec | Manitoba | Manitoba
  - 同じ表の列：Year, Province / Territor…, Region - French, Province / Territor…, Total Registered Po…, Total Registered un…, Total percentage un…

## g1097（1 列）
- 見出し：Province / Territory - English
- 例1 値：Ontario | Quebec | Quebec | Ontario | Ontario
  - 同じ表の列：Year, Region - English, Region - French, Province / Territor…, Total Registered Po…, Total Registered un…, Total percentage un…

## g1098（1 列）
- 見出し：Region - French
- 例1 値：Atlantique | Manitoba | Saskatchewan | Manitoba | Saskatchewan
  - 同じ表の列：Year, Region - English, Province / Territor…, Province / Territor…, Total Registered Po…, Total Registered un…, Total percentage un…

## g1099（1 列）
- 見出し：Province / Territory - French
- 例1 値：Saskatchewan | Saskatchewan | Saskatchewan | Manitoba | Ontario
  - 同じ表の列：Year, Region - English, Province / Territor…, Region - French, Total Registered Po…, Total Registered un…, Total percentage un…

## g1100（1 列）
- 見出し：Total Registered Population
- 例1 値：1968 | 886 | 559 | 481 | 2291
  - 同じ表の列：Year, Region - English, Province / Territor…, Region - French, Province / Territor…, Total Registered un…, Total percentage un…

## g1101（1 列）
- 見出し：Total Registered under Section 6(2)
- 例1 値：166 | 1723 | 1105 | 401 | 980
  - 同じ表の列：Year, Region - English, Province / Territor…, Region - French, Province / Territor…, Total Registered Po…, Total percentage un…

## g1102（1 列）
- 見出し：Total percentage under Section 6(2)
- 例1 値：0.359614699 | 0.399441341 | 0.301687764 | 0.31865285 | 0.245117188
  - 同じ表の列：Year, Region - English, Province / Territor…, Region - French, Province / Territor…, Total Registered Po…, Total Registered un…

## g1103（1 列）
- 見出し：Datasheet-Feuille_donnees
- 例1 値：seedlings | seedlings | seedlings | seedlings | seedlings
  - 同じ表の列：Units, Unites, Source_EN, Source_FR

## g1104（1 列）
- 見出し：Units
- 例1 値：% | mm | mm | cm2 | %
  - 同じ表の列：Datasheet-Feuille_d…, Unites, Source_EN, Source_FR

## g1105（1 列）
- 見出し：Unites
- 例1 値：g | m | g/g | mm3 | cm
  - 同じ表の列：Datasheet-Feuille_d…, Units, Source_EN, Source_FR

## g1106（1 列）
- 見出し：Source_EN
- 例1 値：Data processing | Field work | Field work | Lab measurement at UQAM) | Data processing
  - 同じ表の列：Datasheet-Feuille_d…, Units, Unites, Source_FR

## g1107（1 列）
- 見出し：Source_FR
- 例1 値：Traitement des données | Donnée terrain | Donnée terrain | Traitement des données | Donnée terrain
  - 同じ表の列：Datasheet-Feuille_d…, Units, Unites, Source_EN

## g1108（1 列）
- 見出し：ResLanguage
- 例1 値：en | en | en | en | en
  - 同じ表の列：SC1, SC1_A, SC2, SC3, SC3_2, SC4, SC5, SC6_A1

## g1109（1 列）
- 見出し：SC1
- 例1 値：1.00 | 2.00 | 2.00 | 2.00 | 2.00
  - 同じ表の列：ResLanguage, SC1_A, SC2, SC3, SC3_2, SC4, SC5, SC6_A1

## g1110（1 列）
- 見出し：SC1_A
- 例1 値：1.00 | 1.00 | 1.00 | 1.00 | 1.00
  - 同じ表の列：ResLanguage, SC1, SC2, SC3, SC3_2, SC4, SC5, SC6_A1

## g1111（1 列）
- 見出し：SC2
- 例1 値：5.00 | 5.00 | 4.00 | 4.00 | 5.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC3, SC3_2, SC4, SC5, SC6_A1

## g1112（1 列）
- 見出し：SC3
- 例1 値：11.00 | 9.00 | 5.00 | 10.00 | 11.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3_2, SC4, SC5, SC6_A1

## g1113（1 列）
- 見出し：SC3_2
- 例1 値：9.00 | 11.00 | 1.00 | 1.00 | 9.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3, SC4, SC5, SC6_A1

## g1114（1 列）
- 見出し：SC4
- 例1 値：2.00 | 2.00 | 1.00 | 1.00 | 2.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3, SC3_2, SC5, SC6_A1

## g1115（1 列）
- 見出し：SC5
- 例1 値：1.00 | 2.00 | 2.00 | 2.00 | 3.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3, SC3_2, SC4, SC6_A1

## g1116（1 列）
- 見出し：SC6_A1
- 例1 値：14.00 | 16.00 | 13.00 | 10.00 | 17.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3, SC3_2, SC4, SC5

## g1117（1 列）
- 見出し：SC6_A2
- 例1 値：13.00 | 11.00 | 17.00 | 9.00 | 6.00
  - 同じ表の列：ResLanguage, SC1, SC1_A, SC2, SC3, SC3_2, SC4, SC5

## g1118（1 列）
- 見出し：Calendar Year/Annee civile
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1119（1 列）
- 見出し：Calendar Month/Mois civil
- 例1 値：2026-06-30 | 2026-06-30 | 2026-05-31 | 2026-08-31 | 2026-07-31
  - 同じ表の列：Calendar Year/Annee…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1120（1 列）
- 見出し：Total All Banks/Total Industry Groups/FIs
- 例1 値：Total All Banks | Total All Banks | Total All Banks | Total All Banks | Total All Banks
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1121（1 列）
- 見出し：Total Banques/Total des groupe sectoriel/IFFs
- 例1 値：Total toutes les banques | Total toutes les banques | Total toutes les banques | Total toutes les banques | Total toutes les banques
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1122（1 列）
- 見出し：Industry Group
- 例1 値：All Banks | All Banks | All Banks | All Banks | All Banks
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Groupe Sectoriel, Return/Releve, Return Title

## g1123（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Toutes les banques | Toutes les banques | Toutes les banques | Toutes les banques | Toutes les banques
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Return/Releve, Return Title

## g1124（1 列）
- 見出し：Return/Releve
- 例1 値：M4 | M4 | M4 | M4 | M4
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return Title

## g1125（1 列）
- 見出し：Return Title
- 例1 値：M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return/Releve

## g1126（1 列）
- 見出し：Titre du releve
- 例1 値：M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total All Banks/Tot…, Total Banques/Total…, Industry Group, Groupe Sectoriel, Return/Releve

## g1127（1 列）
- 見出し：Stream
- 例1 値：BHB | GRC | BHB | GRC | SCC
  - 同じ表の列：Station, Year, Abundance, Subsample, Phylum, Subphylum, Class, Subclass

## g1128（1 列）
- 見出し：Station
- 例1 値：1 | 2 | 3 | 2 | 3
  - 同じ表の列：Stream, Year, Abundance, Subsample, Phylum, Subphylum, Class, Subclass

## g1129（2 列）
- 見出し：Abundance
- 例1 値：19 | 8 | 5 | 5 | 7
  - 同じ表の列：Stream, Station, Year, Subsample, Phylum, Subphylum, Class, Subclass
- 例2 値：3 | 2 | 1 | 7 | 3
  - 同じ表の列：SiteID, ProgramID, dateSamplingCommenc…, MethodCode, operationCode, TaxaCode, inTimeStamp, isBiomassCalculated

## g1130（1 列）
- 見出し：Subsample
- 例1 値：12 | 16 | 3 | 11 | 25
  - 同じ表の列：Stream, Station, Year, Abundance, Phylum, Subphylum, Class, Subclass

## g1131（1 列）
- 見出し：Phylum
- 例1 値：Arthropoda | Arthropoda | Arthropoda | Annelida | Arthropoda
  - 同じ表の列：Stream, Station, Year, Abundance, Subsample, Subphylum, Class, Subclass

## g1132（1 列）
- 見出し：Subphylum
- 例1 値：Hexapoda | Hexapoda | Hexapoda | Hexapoda
  - 同じ表の列：Stream, Station, Year, Abundance, Subsample, Phylum, Class, Subclass

## g1133（1 列）
- 見出し：Class
- 例1 値：Insecta | Insecta | Insecta | Insecta | Insecta
  - 同じ表の列：Stream, Station, Year, Abundance, Subsample, Phylum, Subphylum, Subclass

## g1134（1 列）
- 見出し：Subclass
- 例1 値：Acari | Acari | Acari | Acari | Acari
  - 同じ表の列：Stream, Station, Year, Abundance, Subsample, Phylum, Subphylum, Class

## g1135（1 列）
- 見出し：Superorder
- 例1 値：Acariformes | Acariformes | Acariformes | Acariformes | Acariformes
  - 同じ表の列：Stream, Station, Year, Abundance, Subsample, Phylum, Subphylum, Class

## g1136（2 列）
- 見出し：ID
- 例1 値：MUSE0840 | MUSE0470 | MUSE0798 | MUSE0138 | MUSE0558
  - 同じ表の列：Timestamp, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season Start, Season End, By Appointment Only?
- 例2 値：J00000000017 | J00000000016 | J00000000007 | K00000000002 | J00000000012
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 建設年度, 管理戸数

## g1137（1 列）
- 見出し：Timestamp
- 例1 値：2023-09-06 | 2022-06-27 | 2022-06-22 | 2023-05-29 | 2023-08-15
  - 同じ表の列：ID, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season Start, Season End, By Appointment Only?

## g1138（1 列）
- 見出し：Province/ Territory
- 例1 値：ON | NL | QC | PE | MB
  - 同じ表の列：ID, Timestamp, Budget, Budget Year, Seasonal Institution, Season Start, Season End, By Appointment Only?

## g1139（1 列）
- 見出し：Budget
- 例1 値：110747 | 61647 | 81611 | 25968 | 5528
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget Year, Seasonal Institution, Season Start, Season End, By Appointment Only?

## g1140（1 列）
- 見出し：Budget Year
- 例1 値：2022 | 2022 | 2022 | 2021 | 2022
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Seasonal Institution, Season Start, Season End, By Appointment Only?

## g1141（1 列）
- 見出し：Seasonal Institution
- 例1 値：FALSE | TRUE | TRUE | FALSE | FALSE
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Budget Year, Season Start, Season End, By Appointment Only?

## g1142（1 列）
- 見出し：Season Start
- 例1 値：5 | 5 | ? | 6 | 5
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season End, By Appointment Only?

## g1143（1 列）
- 見出し：Season End
- 例1 値：9 | 8 | 9 | 9 | 8
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season Start, By Appointment Only?

## g1144（1 列）
- 見出し：By Appointment Only?
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season Start, Season End

## g1145（1 列）
- 見出し：Volunteer Management
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：ID, Timestamp, Province/ Territory, Budget, Budget Year, Seasonal Institution, Season Start, Season End

## g1146（1 列）
- 見出し：Values_G1_1
- 例1 値：2 | 2 | 4 | 1 | 5
  - 同じ表の列：Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2, Values_G5_1

## g1147（1 列）
- 見出し：Values_G1_2
- 例1 値：5 | 4 | 4 | 5 | 3
  - 同じ表の列：Values_G1_1, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2, Values_G5_1

## g1148（1 列）
- 見出し：Values_G2_1
- 例1 値：5 | 2 | 3 | 4 | 4
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2, Values_G5_1

## g1149（1 列）
- 見出し：Values_G2_2
- 例1 値：5 | 4 | 5 | 3 | 3
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2, Values_G5_1

## g1150（1 列）
- 見出し：Values_G3_1
- 例1 値：3 | 2 | 1 | 3 | 1
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_2, Values_G4_1, Values_G4_2, Values_G5_1

## g1151（1 列）
- 見出し：Values_G3_2
- 例1 値：5 | 4 | 1 | 4 | 5
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G4_1, Values_G4_2, Values_G5_1

## g1152（1 列）
- 見出し：Values_G4_1
- 例1 値：5 | 5 | 5 | 5 | 4
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_2, Values_G5_1

## g1153（1 列）
- 見出し：Values_G4_2
- 例1 値：2 | 4 | 1 | 2 | 1
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G5_1

## g1154（1 列）
- 見出し：Values_G5_1
- 例1 値：4 | 1 | 3 | 4 | 5
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2

## g1155（1 列）
- 見出し：Values_G5_2
- 例1 値：1 | 5 | 5 | 5 | 4
  - 同じ表の列：Values_G1_1, Values_G1_2, Values_G2_1, Values_G2_2, Values_G3_1, Values_G3_2, Values_G4_1, Values_G4_2

## g1156（1 列）
- 見出し：Indicator
- 例1 値：DEATHS BY SUICIDE | CANCER CASES | LOW BIRTHWEIGHT | DIABETES CASES | CANCER DEATHS
  - 同じ表の列：Unit, OCED_Country, Value, Year, Comparison_to_OECD_…

## g1157（1 列）
- 見出し：Unit
- 例1 値：Percent of live births below 2500 grams | Rate per 100 000 | Years | Incidence per 100 000 population | Rate per 1000 population
  - 同じ表の列：Indicator, OCED_Country, Value, Year, Comparison_to_OECD_…

## g1158（1 列）
- 見出し：OCED_Country
- 例1 値：Iceland | Türkiye | Denmark | Spain | Denmark
  - 同じ表の列：Indicator, Unit, Value, Year, Comparison_to_OECD_…

## g1159（1 列）
- 見出し：Comparison_to_OECD_average
- 例1 値：Similar | Worse | Similar | Similar | Similar
  - 同じ表の列：Indicator, Unit, OCED_Country, Value, Year

## g1160（1 列）
- 見出し：academic_level_area_of_study_e
- 例1 値：Bachelor's degreeApplied Arts | Bachelor's degree | Bachelor's degree | Bachelor's degreeArts | Bachelor's degreeApplied Sciences
  - 同じ表の列：academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f, program_type_e

## g1161（1 列）
- 見出し：academic_level_area_of_study_f
- 例1 値：BaccalauréatSciences appliquées | Attestation d'études collégiales (au Qu… | Baccalauréat | BaccalauréatArts & Sciences | Attestation d'études collégiales (au Qu…
  - 同じ表の列：academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f, program_type_e

## g1162（1 列）
- 見出し：program_of_study_e
- 例1 値：Economics | Computer Science | Software Development: Secure Desktop, M… | Machining | Drama
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f, program_type_e

## g1163（1 列）
- 見出し：program_of_study_f
- 例1 値：Baccalauréat en cinéma et télévision | Geographie | Études de genre | Communications - Journalisme | Analyse des politiques publiques
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f, program_type_e

## g1164（1 列）
- 見出し：program_length_e
- 例1 値：4Year(s) | 4Year(s) | 10Month(s) | 5Year(s) | 4Year(s)
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_f, duration_of_term_e, duration_of_term_f, program_type_e

## g1165（1 列）
- 見出し：program_length_f
- 例1 値：5Année(s) | 4Année(s) | 5Année(s) | 4Année(s) | 4Année(s)
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, duration_of_term_e, duration_of_term_f, program_type_e

## g1166（1 列）
- 見出し：duration_of_term_e
- 例1 値：12Week(s) | 5Week(s) | 12Week(s) | 12-18Week(s) | 210Hour(s)
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_f, program_type_e

## g1167（1 列）
- 見出し：duration_of_term_f
- 例1 値：350Heure(s) | 90Heure(s) | 16Semaine(s) | 4Semaine(s) | 12-17Semaine(s)
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, program_type_e

## g1168（1 列）
- 見出し：program_type_e
- 例1 値：Internship | Internship | CO-OP | CO-OP | CO-OP
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f

## g1169（1 列）
- 見出し：program_type_f
- 例1 値：Coopératif | Coopératif | Stages | Coopératif | Stages
  - 同じ表の列：academic_level_area…, academic_level_area…, program_of_study_e, program_of_study_f, program_length_e, program_length_f, duration_of_term_e, duration_of_term_f

## g1170（1 列）
- 見出し：Acronym_EN
- 例1 値：GAC | DND | INAC | DFO | LAC
  - 同じ表の列：Services, Results, Scores, Date

## g1171（1 列）
- 見出し：Services
- 例1 値：Email | Cabling | Secure Remote Access | Midrange | Overall
  - 同じ表の列：Acronym_EN, Results, Scores, Date

## g1172（1 列）
- 見出し：Results
- 例1 値：Agree | Agree | Agree | Agree | Strongly Agree
  - 同じ表の列：Acronym_EN, Services, Scores, Date

## g1173（1 列）
- 見出し：Scores
- 例1 値：5 | 4 | 3 | 5 | 5
  - 同じ表の列：Acronym_EN, Services, Results, Date

## g1174（1 列）
- 見出し：year_annee
- 例1 値：2024 | 2013 | 2016 | 2017 | 2015
  - 同じ表の列：month_mois, visits_visites, downloads_telecharg…

## g1175（1 列）
- 見出し：month_mois
- 例1 値：10 | 11 | 3 | 6 | 6
  - 同じ表の列：year_annee, visits_visites, downloads_telecharg…

## g1176（1 列）
- 見出し：visits_visites
- 例1 値：38368 | 205791 | 1058246 | 65516 | 860212
  - 同じ表の列：year_annee, month_mois, downloads_telecharg…

## g1177（1 列）
- 見出し：downloads_telechargements
- 例1 値：112939 | 61998 | 7684 | 15860 | 4791
  - 同じ表の列：year_annee, month_mois, visits_visites

## g1178（1 列）
- 見出し：Incentive Request Date
- 例1 値：2023-03-22 | 2022-11-07 | 2023-02-09 | 2022-12-05 | 2022-12-02
  - 同じ表の列：Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1179（1 列）
- 見出し：Month and Year
- 例1 値：December 2022 | December 2022 | December 2022 | October 2022 | February 2023
  - 同じ表の列：Incentive Request D…, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1180（1 列）
- 見出し：Government of Canada Fiscal Year
- 例1 値：2022-23 | 2022-23 | 2022-23 | 2022-23 | 2022-23
  - 同じ表の列：Incentive Request D…, Month and Year, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1181（1 列）
- 見出し：Calendar Year
- 例1 値：2022 | 2022 | 2022 | 2022 | 2023
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1182（1 列）
- 見出し：Dealership Province/Territory
- 例1 値：Quebec | Quebec | Quebec | Quebec | Quebec
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1183（1 列）
- 見出し：Purchase or Lease
- 例1 値：Lease | Lease | Lease | Lease | Purchase
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Vehicle Year, Vehicle Make, Vehicle Model

## g1184（1 列）
- 見出し：Vehicle Year
- 例1 値：2022 | 2022 | 2023 | 2022 | 2023
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Make, Vehicle Model

## g1185（1 列）
- 見出し：Vehicle Make
- 例1 値：Lion | Ford | Peterbilt | Ford | Lion
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Model

## g1186（1 列）
- 見出し：Vehicle Model
- 例1 値：Lion6 | E-Transit | E-Transit | E-Transit | E-Transit
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make

## g1187（1 列）
- 見出し：Vehicle Make and Model
- 例1 値：Ford E-Transit | Ford E-Transit | Ford E-Transit | Ford E-Transit | Ford E-Transit
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make

## g1188（1 列）
- 見出し：Program
- 例1 値：Disability | Disability | Disability | Critical Injury Benefit | Disability
  - 同じ表の列：Date, Type, Claim, Processing Time (we…

## g1189（1 列）
- 見出し：Claim
- 例1 値：PTSD (Single Condition) | PTSD (Single Condition) | PTSD (Single Condition) | Hearing Loss (Single Condition) | Other (Single Condition)
  - 同じ表の列：Date, Program, Type, Processing Time (we…

## g1190（1 列）
- 見出し：Processing Time (weeks)
- 例1 値：2.53 | 47.22 | 17.54 | 6.12 | 8.96
  - 同じ表の列：Date, Program, Type, Claim

## g1191（2 列）
- 見出し：Region
- 例1 値：Saskatchewan | Manitoba | Alberta | British Columbia | Western Canada
  - 同じ表の列：% of professional j…
- 例2 値：South | North | West | Greater Sydney | West
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, site_status, lga, distance_from, road_number

## g1192（1 列）
- 見出し：% of professional jobs
- 例1 値：33.5% | 29.5% | 28.2% | 33.1% | 32.4%
  - 同じ表の列：Region

## g1193（1 列）
- 見出し：Jun-24
- 例1 値：636 | 12 | Board Directors | All Employees | 472
  - 同じ表の列：Jun-23

## g1194（1 列）
- 見出し：Jun-23
- 例1 値：10 | 168 | 650 | Secondment | 136
  - 同じ表の列：Jun-24

## g1195（1 列）
- 見出し：DOG_BREED
- 例1 値：Old English Sheepdog | Maltese Cross | Cavalier King Charles Spaniel | Maltese Cross | Labrador Retriever Cross
  - 同じ表の列：YEAR, DOG_SEX, DOG_SUBURB

## g1196（1 列）
- 見出し：DOG_SEX
- 例1 値：Desexed Male | Desexed Female | Female | Desexed Female | Desexed Male
  - 同じ表の列：DOG_BREED, YEAR, DOG_SUBURB

## g1197（1 列）
- 見出し：DOG_SUBURB
- 例1 値：ERINDALE | KENSINGTON PARK | KENSINGTON GARDENS | TUSMORE | ERINDALE
  - 同じ表の列：DOG_BREED, YEAR, DOG_SEX

## g1198（1 列）
- 見出し：Time
- 例1 値：2020-07-31T21:43:10+10:00 | 2020-07-31T06:56:49+10:00 | 2020-07-31T12:21:17+10:00 | 2020-07-31T13:22:23+10:00 | 2020-07-31T20:45:41+10:00
  - 同じ表の列：Device ID, Location

## g1199（1 列）
- 見出し：Device ID
- 例1 値：70b3d57ba0000b65 | 70b3d57ba0000b5e | 70b3d57ba0000b63 | 70b3d57ba0000b62 | 70b3d57ba0000b61
  - 同じ表の列：Time, Location

## g1200（1 列）
- 見出し：Location
- 例1 値：-32.96116,151.69792 | -32.9661,151.6987 | -32.97838,151.70843 | -32.9661,151.6987 | -32.96618,151.695461
  - 同じ表の列：Time, Device ID

## 答えの雛形

```
g1081	
g1082	
g1083	
g1084	
g1085	
g1086	
g1087	
g1088	
g1089	
g1090	
g1091	
g1092	
g1093	
g1094	
g1095	
g1096	
g1097	
g1098	
g1099	
g1100	
g1101	
g1102	
g1103	
g1104	
g1105	
g1106	
g1107	
g1108	
g1109	
g1110	
g1111	
g1112	
g1113	
g1114	
g1115	
g1116	
g1117	
g1118	
g1119	
g1120	
g1121	
g1122	
g1123	
g1124	
g1125	
g1126	
g1127	
g1128	
g1129	
g1130	
g1131	
g1132	
g1133	
g1134	
g1135	
g1136	
g1137	
g1138	
g1139	
g1140	
g1141	
g1142	
g1143	
g1144	
g1145	
g1146	
g1147	
g1148	
g1149	
g1150	
g1151	
g1152	
g1153	
g1154	
g1155	
g1156	
g1157	
g1158	
g1159	
g1160	
g1161	
g1162	
g1163	
g1164	
g1165	
g1166	
g1167	
g1168	
g1169	
g1170	
g1171	
g1172	
g1173	
g1174	
g1175	
g1176	
g1177	
g1178	
g1179	
g1180	
g1181	
g1182	
g1183	
g1184	
g1185	
g1186	
g1187	
g1188	
g1189	
g1190	
g1191	
g1192	
g1193	
g1194	
g1195	
g1196	
g1197	
g1198	
g1199	
g1200	
```
