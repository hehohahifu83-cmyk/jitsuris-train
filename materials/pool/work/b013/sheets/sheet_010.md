# ラベル用シート 010 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_010.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1081（1 列）
- 見出し：Comments
- 例1 値：Confidential | Confidential | Confidential | Confidential
  - 同じ表の列：Ref Number | Numero…, Title (English), Titre (Francais), Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…

## g1082（1 列）
- 見出し：Province or territory
- 例1 値：Quebec | Alberta | Manitoba | Nova Scotia | Canada
  - 同じ表の列：Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g1083（1 列）
- 見出し：Grand total (#)
- 例1 値：3852070 | 135080 | 4140 | 5800 | 3400
  - 同じ表の列：Province or territo…, Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g1084（1 列）
- 見出し：Grand total ($)
- 例1 値：672513 | 36734 | 131425 | 26698 | 4311643
  - 同じ表の列：Province or territo…, Grand total (#), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g1085（1 列）
- 見出し：Family income less than $5,000 (#)
- 例1 値：173880 | 390 | 100 | 17090 | 16320
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g1086（1 列）
- 見出し：Family income less than $5,000 ($)
- 例1 値：37768 | 2091 | 405921 | 4541 | 316852
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…, Family income betwe…

## g1087（1 列）
- 見出し：Family income $5,000 - $9,999 (no. of recipients)
- 例1 値：1180 | 34420 | 180 | 3290 | 2910
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income betwe…, Family income betwe…

## g1088（1 列）
- 見出し：Family income $5,000 - $9,999 ($)
- 例1 値：1578 | 23596 | 14541 | 119551 | 2482
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income betwe…, Family income betwe…

## g1089（1 列）
- 見出し：Family income between $10,000 - $14,999 (#)
- 例1 値：180 | 390 | 50 | 123840 | 9080
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g1090（1 列）
- 見出し：Family income between $10,000 - $14,999 ($)
- 例1 値：1649100 | 51663 | 607 | 827861 | 74803
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g1091（1 列）
- 見出し：Family income between $15,000 - $19,999 (#)
- 例1 値：4270 | 50890 | 14310 | 5650 | 15020
  - 同じ表の列：Province or territo…, Grand total (#), Grand total ($), Family income less …, Family income less …, Family income $5,00…, Family income $5,00…, Family income betwe…

## g1092（1 列）
- 見出し：Employment Equity (EE) groups / Official Languages
- 例1 値：*Please note that employees can identif… | Persons with disabilities | Women | First Official Language ENGLISH | 2SLGBTIQ+*
  - 同じ表の列：% of Identifying Em…

## g1093（1 列）
- 見出し：% of Identifying Employees
- 例1 値：74.20% | 22.60% | 13.80% | 28.80% | 3.20%
  - 同じ表の列：Employment Equity (…

## g1094（1 列）
- 見出し：title_translated_en
- 例1 値：First-Come, First-Served Tariff Rate Qu… | Tariff Rate Quotas for Wheat, Barley, W… | Message To Industry Subject: Barley Pro… | Notice to Importers Items 162 to 181 - … | Message to Industry Subject : Barley Pr…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1095（1 列）
- 見出し：title_translated_fr
- 例1 値：Avis aux importateurs Articles 162 à 18… | Avis aux importateurs Articles 183 à 19… | Message à l’intention de l’industrie : … | Message aux parties de l'industrie : Le… | Message aux parties de l’industrie : Le…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1096（1 列）
- 見出し：notes_translated_en
- 例1 値：Notice to Importers Items 183 to 191 - … | This message pertains to imports of bar… | This message pertains to imports of whe… | First-Come, First-Served Tariff Rate Qu… | This message pertains to imports of whe…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1097（1 列）
- 見出し：notes_translated_fr
- 例1 値：Contingents tarifaires, premier arrivé,… | Ce message concerne les importations de… | Ce message concerne les importations de… | Contingents tarifaires, premier arrivé,… | Le présent avis remplace l’Avis aux imp…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g1098（1 列）
- 見出し：title_translated_en
- 例1 値：Notice to Exporters NAFTA Wool Apparel … | Notice to Exporters NAFTA Fabric Export… | Notices Administration of the North Ame… | Notice to Exporters Administration of t… | Notice - Textiles and clothing tariff p…
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1099（1 列）
- 見出し：title_translated_fr
- 例1 値：Glossaire des avis aux exportateurs N° … | Avis aux exportateurs Vêtements destiné… | Avis aux exportateurs Exportations de t… | Niveau de préférence tarifaire pour l’e… | Avis aux exportateurs Textiles et vêtem…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1100（1 列）
- 見出し：notes_translated_en
- 例1 値：The purpose of this Notice is to outlin… | This notice is to inform Tariff Prefere… | This Notice sets out the policies and p… | This Notice sets out the policies and p… | This Notice sets out the policies and p…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g1101（1 列）
- 見出し：notes_translated_fr
- 例1 値：Le présent avis énonce les politiques e… | Cet avis aux exportateurs explique les … | Le présent avis énonce les politiques e… | En vertu de l’Accord économique et comm… | Le présent Avis a pour objet d'exposer …
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g1102（1 列）
- 見出し：treatment_code
- 例1 値：S | C | SH | C | C
  - 同じ表の列：female_id, emergence_date, dissection_date, death_period, status_at_dissection, age_in_days, oocyte_count, parasitized_hosts_c…

## g1103（1 列）
- 見出し：female_id
- 例1 値：L2-32 | S4-63 | L2-51 | S4-223 | S1-96
  - 同じ表の列：treatment_code, emergence_date, dissection_date, death_period, status_at_dissection, age_in_days, oocyte_count, parasitized_hosts_c…

## g1104（1 列）
- 見出し：emergence_date
- 例1 値：2004-02-11 | 2004-01-21 | 2004-04-05 | 2004-02-09 | 2004-03-30
  - 同じ表の列：treatment_code, female_id, dissection_date, death_period, status_at_dissection, age_in_days, oocyte_count, parasitized_hosts_c…

## g1105（1 列）
- 見出し：dissection_date
- 例1 値：2004-01-12 | 2004-04-09 | 2004-02-07 | 2003-10-16 | 2004-01-22
  - 同じ表の列：treatment_code, female_id, emergence_date, death_period, status_at_dissection, age_in_days, oocyte_count, parasitized_hosts_c…

## g1106（1 列）
- 見出し：death_period
- 例1 値：am | am | am | am | am
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, status_at_dissection, age_in_days, oocyte_count, parasitized_hosts_c…

## g1107（1 列）
- 見出し：status_at_dissection
- 例1 値：alive | alive | dead | alive | alive
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, death_period, age_in_days, oocyte_count, parasitized_hosts_c…

## g1108（1 列）
- 見出し：age_in_days
- 例1 値：4.0 | 2.0 | 2.0 | 4.0 | 0.5
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, death_period, status_at_dissection, oocyte_count, parasitized_hosts_c…

## g1109（1 列）
- 見出し：oocyte_count
- 例1 値：2 | 3 | 0 | 2 | 7
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, death_period, status_at_dissection, age_in_days, parasitized_hosts_c…

## g1110（1 列）
- 見出し：parasitized_hosts_count
- 例1 値：33.0 | 71.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, death_period, status_at_dissection, age_in_days, oocyte_count

## g1111（1 列）
- 見出し：total_reproductive_output_count
- 例1 値：7.0 | 89.0 | 41.0 | 97.0 | 5.0
  - 同じ表の列：treatment_code, female_id, emergence_date, dissection_date, death_period, status_at_dissection, age_in_days, oocyte_count

## g1112（2 列）
- 見出し：EMDatasetID_EMJeuID
- 例1 値：EM138 | EM140 | EM139 | EM138 | EM139
  - 同じ表の列：id, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, SampleType_TypeEcha…
- 例2 値：EM144 | EM144 | EM144 | EM144 | EM144
  - 同じ表の列：ID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1113（2 列）
- 見出し：DatasetID_IDJeu
- 例1 値：48 | 388 | 193 | 633 | 60
  - 同じ表の列：id, EMDatasetID_EMJeuID, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, SampleType_TypeEcha…
- 例2 値：866 | 600 | 178 | 488 | 717
  - 同じ表の列：ID, EMDatasetID_EMJeuID, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1114（1 列）
- 見出し：SampleID_IDEchantillon
- 例1 値：SAMRAC-R-01-3 | 1697p002 | 1697p041 | TRIBOR-R-01-1 | MELALB-BS-01-1
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, SampleType_TypeEcha…

## g1115（2 列）
- 見出し：TOPICSpeciesCode_CodeEspTOPIC
- 例1 値：BETPAP | STRAMP | RUBIDA | SAMRAC | MAICAN
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs, SampleType_TypeEcha…
- 例2 値：CORCAN | VACANG | KALANG | TRIBOR | KALANG
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, StudyPlotID_EtudeID…, Population, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1116（1 列）
- 見出し：TraitCode
- 例1 値：SLA | LDMC | Leaf_N | LA | CA
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, ObsTraitValue_Valeu…, ObsUnit_UniteObs, SampleType_TypeEcha…

## g1117（1 列）
- 見出し：ObsTraitValue_ValeurTraitObs
- 例1 値：45.72273254 | 182.86875 | 19644775.3 | 22879.31 | 7084.394396
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsUnit_UniteObs, SampleType_TypeEcha…

## g1118（1 列）
- 見出し：ObsUnit_UniteObs
- 例1 値：mm2 | mm2 | mm2 | % | mm2
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, SampleType_TypeEcha…

## g1119（1 列）
- 見出し：SampleType_TypeEchantillon
- 例1 値：Trees and shrubs | Understory | Understory | Understory | Understory
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1120（1 列）
- 見出し：ObsHabitatDescription_DescriptionHabitatObs
- 例1 値：Meadow by trail side - full sun | Low birch oak canopy - part shade to fu… | NA | Low birch oak canopy - part shade | Conifer cover - Full shade to part shade
  - 同じ表の列：id, EMDatasetID_EMJeuID, DatasetID_IDJeu, SampleID_IDEchantil…, TOPICSpeciesCode_Co…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1121（1 列）
- 見出し：StudyPlotID_EtudeIDParcelle
- 例1 値：MACPES-2 | IGNACE2-2 | LONGLAC-2 | IGNACE2-3 | LAN-1
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, Population, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1122（1 列）
- 見出し：Population
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, TraitCode, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1123（1 列）
- 見出し：TraitCode
- 例1 値：Root_Ca | Root_Mg | Root_P | Root_Mg | Root_P
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, ObsTraitValue_Valeu…, ObsUnit_UniteObs

## g1124（1 列）
- 見出し：ObsTraitValue_ValeurTraitObs
- 例1 値：10615 | 8171 | 0.795 | 4425 | 2852
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, TraitCode, ObsUnit_UniteObs

## g1125（1 列）
- 見出し：ObsUnit_UniteObs
- 例1 値：mg/g | mg/g | mg/g | mg/g | mg/g
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, TraitCode, ObsTraitValue_Valeu…

## g1126（1 列）
- 見出し：YearSampled_AnneeObs
- 例1 値：2014 | 2014 | 2014 | 2014 | 2014
  - 同じ表の列：ID, EMDatasetID_EMJeuID, DatasetID_IDJeu, TOPICSpeciesCode_Co…, StudyPlotID_EtudeID…, Population, TraitCode, ObsTraitValue_Valeu…

## g1127（1 列）
- 見出し：Calendar Year/Annee civile
- 例1 値：2016 | 2015 | 2016 | 2016 | 2015
  - 同じ表の列：Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title, Titre du releve

## g1128（1 列）
- 見出し：Calendar Month/Mois civil
- 例1 値：2015-07-31 | 2015-08-31 | 2015-08-31 | 2015-10-31 | 2015-09-30
  - 同じ表の列：Calendar Year/Annee…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title, Titre du releve

## g1129（1 列）
- 見出し：Total Cooperative Retail Associations/FIs
- 例1 値：Total Cooperative Retail Associations | Total Cooperative Retail Associations | Total Cooperative Retail Associations | Total Cooperative Retail Associations | Total Cooperative Retail Associations
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Industry Group, Groupe Sectoriel, Return/Releve, Return Title, Titre du releve

## g1130（2 列）
- 見出し：Industry Group
- 例1 値：Cooperative Retail Associations | Cooperative Retail Associations | Cooperative Retail Associations | Cooperative Retail Associations | Cooperative Retail Associations
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Groupe Sectoriel, Return/Releve, Return Title, Titre du releve
- 例2 値：Canadian Life Companies | Canadian Life Companies | Canadian Life Companies | Canadian Life Companies | Canadian Life Companies
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Groupe Sectoriel, Return/Releve

## g1131（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Associations coopérative et de détail | Associations coopérative et de détail | Associations coopérative et de détail | Associations coopérative et de détail | Associations coopérative et de détail
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Return/Releve, Return Title, Titre du releve

## g1132（1 列）
- 見出し：Return/Releve
- 例1 値：M4 | M4 | M4 | M4 | M4
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return Title, Titre du releve

## g1133（1 列）
- 見出し：Return Title
- 例1 値：M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return/Releve, Titre du releve

## g1134（1 列）
- 見出し：Titre du releve
- 例1 値：M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1135（1 列）
- 見出し：Libelle de l'adresse du point de donnees
- 例1 値：Bilan mensuel consolidé : actif, autres… | Bilan mensuel consolidé : passif, avoir… | Bilan mensuel consolidé : passif, total… | Bilan mensuel consolidé : actif, espèce… | Bilan mensuel consolidé : passif, autre…
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Cooperative R…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g1136（2 列）
- 見出し：Fiscal Year/Annee fiscale
- 例1 値：2023 | 2024 | 2024 | 2024 | 2023
  - 同じ表の列：Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve
- 例2 値：2025 | 2023 | 2023 | 2024 | 2023
  - 同じ表の列：Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Groupe Sectoriel, Return/Releve

## g1137（2 列）
- 見出し：Fiscal Quarter
- 例1 値：Q4 - 2023 | Q4 - 2024 | Q4 - 2025 | Q4 - 2024 | Q4 - 2024
  - 同じ表の列：Fiscal Year/Annee f…, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve
- 例2 値：Q4 - 2024 | Q4 - 2024 | Q4 - 2023 | Q4 - 2025 | Q4 - 2025
  - 同じ表の列：Fiscal Year/Annee f…, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Groupe Sectoriel, Return/Releve

## g1138（2 列）
- 見出し：Trimestre fiscal
- 例1 値：T4 - 2023 | T4 - 2023 | T4 - 2024 | T4 - 2025 | T4 - 2024
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve
- 例2 値：T4 - 2023 | T4 - 2025 | T4 - 2025 | T4 - 2025 | T4 - 2023
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Groupe Sectoriel, Return/Releve

## g1139（1 列）
- 見出し：Total Life Insurance Companies/FIs
- 例1 値：Sun Life Financial Inc. | RBC Life Insurance Company | BMO Life Assurance Company | The Manufacturers Life Insurance Company | BMO Life Insurance Company
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve

## g1140（1 列）
- 見出し：Total Societes d'assurance-vie/IFFs
- 例1 値：Total sociétés d’assurance-vie canadien… | Compagnie d’assurance Manuvie du Canada | La Compagnie d'Assurance-Vie Manufactur… | Compagnie de rentes Blumont | TD, Compagnie d'assurance-vie
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Industry Group, Groupe Sectoriel, Return/Releve

## g1141（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Sociétés d’assurance-vie canadiennes | Sociétés d’assurance-vie canadiennes | Sociétés d’assurance-vie canadiennes | Sociétés d’assurance-vie canadiennes | Sociétés d’assurance-vie canadiennes
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Return/Releve

## g1142（2 列）
- 見出し：Return/Releve
- 例1 値：LCA | LCA | LCA | LCA | LCA
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Groupe Sectoriel
- 例2 値：LCA | LCA | LCA | LCA | LCA
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Groupe Sectoriel

## g1143（2 列）
- 見出し：Return Title
- 例1 値：LCA - LICAT | LCA - LICAT | LCA - LICAT | LCA - LICAT | LCA - LICAT
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Life Insuranc…, Total Societes d'as…, Industry Group, Groupe Sectoriel
- 例2 値：LCA - LICAT | LCA - LICAT | LCA - LICAT | LCA - LICAT | LCA - LICAT
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Groupe Sectoriel

## g1144（1 列）
- 見出し：Total Fraternal Benefit Societies/FIs
- 例1 値：Serenia Life Financial | The Grand Orange Lodge of British Ameri… | The Grand Orange Lodge of British Ameri… | The Independent Order of Foresters | The Grand Orange Lodge of British Ameri…
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total les societes …, Industry Group, Groupe Sectoriel, Return/Releve

## g1145（1 列）
- 見出し：Total les societes de secours mutuels/IFFs
- 例1 値：Total sociétés de secours mutuels canad… | Total sociétés de secours mutuels canad… | Toronto Police Widows and Orphans Fund | Total sociétés de secours mutuels canad… | La société d'assurance-vie des enseigna…
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Industry Group, Groupe Sectoriel, Return/Releve

## g1146（1 列）
- 見出し：Industry Group
- 例1 値：Canadian Fraternals | Canadian Fraternals | Canadian Fraternals | Canadian Fraternals | Canadian Fraternals
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Groupe Sectoriel, Return/Releve

## g1147（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Sociétés de secours mutuels canadiennes | Sociétés de secours mutuels canadiennes | Sociétés de secours mutuels canadiennes | Sociétés de secours mutuels canadiennes | Sociétés de secours mutuels canadiennes
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Fraternal Ben…, Total les societes …, Industry Group, Return/Releve

## g1148（3 列）
- 見出し：Park
- 例1 値：KNP | KNP | KNP | KNP | KNP
  - 同じ表の列：Location, PointID, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s
- 例2 値：YNP | YNP | YNP | YNP | YNP
  - 同じ表の列：location.id, location, trailtype, datestart, dateimage, timeimage, species, total

## g1149（1 列）
- 見出し：PointID
- 例1 値：5 | 2 | 1 | 5 | 4
  - 同じ表の列：Park, Location, Year, Month, Day, Species, Time.1st.Detected, #detected_0-3m20s

## g1150（1 列）
- 見出し：Day
- 例1 値：3 | 11 | 15 | 14 | 15
  - 同じ表の列：Park, Location, PointID, Year, Month, Species, Time.1st.Detected, #detected_0-3m20s

## g1151（1 列）
- 見出し：Species
- 例1 値：OCWA | GCKI | CHSP | PISI | AMRO
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Time.1st.Detected, #detected_0-3m20s

## g1152（1 列）
- 見出し：Time.1st.Detected
- 例1 値：5.43 | 8 | 0.08 | 0.02 | 0
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, #detected_0-3m20s

## g1153（1 列）
- 見出し：#detected_0-3m20s
- 例1 値：1 | 0 | 1 | 2 | 0
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, Time.1st.Detected

## g1154（1 列）
- 見出し：#detected_3m21s-6m40s
- 例1 値：1 | 0 | 1 | 0 | 0
  - 同じ表の列：Park, Location, PointID, Year, Month, Day, Species, Time.1st.Detected

## g1155（2 列）
- 見出し：location.id
- 例1 値：26 | 26 | 26 | 26 | 26
  - 同じ表の列：location, park, trailtype, datestart, dateimage, timeimage, species, total
- 例2 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：location, park, trailtype, datestart, dateimage, timeimage, species, total

## g1156（2 列）
- 見出し：trailtype
- 例1 値：human trail | human trail | human trail | human trail | human trail
  - 同じ表の列：location.id, location, park, datestart, dateimage, timeimage, species, total
- 例2 値：road bed | road bed | road bed | road bed | road bed
  - 同じ表の列：location.id, location, park, datestart, dateimage, timeimage, species, total

## g1157（2 列）
- 見出し：datestart
- 例1 値：2018-09-06 | 2014-09-27 | 2018-09-06 | 2018-09-06 | 2019-07-11
  - 同じ表の列：location.id, location, park, trailtype, dateimage, timeimage, species, total
- 例2 値：2012-08-09 | 2013-12-01 | 2013-12-01 | 2014-06-18 | 2013-12-01
  - 同じ表の列：location.id, location, park, trailtype, dateimage, timeimage, species, total

## g1158（2 列）
- 見出し：dateimage
- 例1 値：2019-06-19 | 2019-07-29 | 2019-02-13 | 2020-08-12 | 2019-06-12
  - 同じ表の列：location.id, location, park, trailtype, datestart, timeimage, species, total
- 例2 値：2013-06-21 | 2014-06-13 | 2011-11-24 | 2011-06-14 | 2013-09-06
  - 同じ表の列：location.id, location, park, trailtype, datestart, timeimage, species, total

## g1159（2 列）
- 見出し：timeimage
- 例1 値：12:00:00 | 18:10:05 | 12:00:00 | 15:10:54 | 16:25:54
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, species, total
- 例2 値：13:19:00 | 11:41:17 | 21:57:00 | 12:16:42 | 05:42:46
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, species, total

## g1160（1 列）
- 見出し：species
- 例1 値：hiker | empty | empty | grizzly bear | empty
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, timeimage, total

## g1161（1 列）
- 見出し：horses
- 例1 値：2 | 2
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, timeimage, species

## g1162（1 列）
- 見出し：location
- 例1 値：4 mile pit | 4 mile pit | 4 mile pit | 4 mile pit | 4 mile pit
  - 同じ表の列：location.id, park, trailtype, datestart, dateimage, timeimage, species, total

## g1163（1 列）
- 見出し：species
- 例1 値：coyote | white-tailed deer | coyote | white-tailed deer | white-tailed deer
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, timeimage, total

## g1164（1 列）
- 見出し：dogsoffleash
- 例1 値：1
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, timeimage, species

## g1165（2 列）
- 見出し：fiscal_year
- 例1 値：2017-2018 | 2015-2016 | 2016-2017 | 2024-2025 | 2022-2023
  - 同じ表の列：tenure_e, tenure_f, n
- 例2 値：2023-2024 | 2022-2023 | 2020-2021 | 2019-2020 | 2019-2020
  - 同じ表の列：quarter, n, median

## g1166（2 列）
- 見出し：tenure_e
- 例1 値：Casual | Student | Student | Student | Student
  - 同じ表の列：fiscal_year, tenure_f, n
- 例2 値：Casual | Term | Casual | Indeterminate | Casual
  - 同じ表の列：month_end_date, tenure_f, n

## g1167（2 列）
- 見出し：tenure_f
- 例1 値：Emploi étudiant | Durée déterminée | Emploi occasionnel | Durée déterminée | Emploi étudiant
  - 同じ表の列：fiscal_year, tenure_e, n
- 例2 値：Emploi étudiant | Emploi occasionnel | Période indéterminée | Période indéterminée | Emploi occasionnel
  - 同じ表の列：month_end_date, tenure_e, n

## g1168（3 列）
- 見出し：n
- 例1 値：6227 | 7762 | 8244 | 20070 | 7364
  - 同じ表の列：fiscal_year, tenure_e, tenure_f
- 例2 値：7988 | 13462 | 9643 | 173083 | 15074
  - 同じ表の列：month_end_date, tenure_e, tenure_f

## g1169（1 列）
- 見出し：month_end_date
- 例1 値：2015-03-31 | 2024-03-31 | 2014-03-31 | 2009-03-31 | 2020-03-31
  - 同じ表の列：tenure_e, tenure_f, n

## g1170（1 列）
- 見出し：quarter
- 例1 値：YTD Q4 | YTD Q2 | Q1 | Q1 | YTD Q3
  - 同じ表の列：fiscal_year, n, median

## g1171（1 列）
- 見出し：median
- 例1 値：205 | 194 | 227 | 220 | 207.5
  - 同じ表の列：fiscal_year, quarter, n

## g1172（1 列）
- 見出し：Fiscal Year
- 例1 値：2018-2019 | 2016-2017 | 2020-2021 | 2021/2022 | 2017-2018
  - 同じ表の列：Employment Equity G…, Representation, Workforce Availabil…

## g1173（1 列）
- 見出し：Employment Equity Group
- 例1 値：Visible Minorities | Women | Persons wih Disabilities | Persons wih Disabilities | Persons wih Disabilities
  - 同じ表の列：Fiscal Year, Representation, Workforce Availabil…

## g1174（1 列）
- 見出し：Representation
- 例1 値：15.60% | 5.48% | 17.60% | 5.50% | 7.38%
  - 同じ表の列：Fiscal Year, Employment Equity G…, Workforce Availabil…

## g1175（1 列）
- 見出し：Workforce Availability
- 例1 値：4.00% | 9.70% | 37.86% | 9.75% | 17.48%
  - 同じ表の列：Fiscal Year, Employment Equity G…, Representation

## g1176（1 列）
- 見出し：exercice fiscal
- 例1 値：2022-2023 | 2024-2025 | 2020-2021 | 2019-2020 | 2022-2023
  - 同じ表の列：mois, indicateur de resul…, cible, resultats reels, Fournisseur, remarques

## g1177（1 列）
- 見出し：mois
- 例1 値：juin | mars | août | juin | juin
  - 同じ表の列：exercice fiscal, indicateur de resul…, cible, resultats reels, Fournisseur, remarques

## g1178（1 列）
- 見出し：indicateur de resultats ministeriels
- 例1 値：Pourcentage du temps où le réseau cellu… | Pourcentage du temps où le réseau cellu… | Pourcentage du temps où le réseau cellu… | Pourcentage du temps où le réseau cellu… | Pourcentage du temps où le réseau cellu…
  - 同じ表の列：exercice fiscal, mois, cible, resultats reels, Fournisseur, remarques

## g1179（1 列）
- 見出し：cible
- 例1 値：99.5 | 99.5 | 99.5 | 99.8 | 99.9
  - 同じ表の列：exercice fiscal, mois, indicateur de resul…, resultats reels, Fournisseur, remarques

## g1180（1 列）
- 見出し：resultats reels
- 例1 値：Cible atteinte | Cible atteinte | Cible atteinte | Cible atteinte | Cible atteinte
  - 同じ表の列：exercice fiscal, mois, indicateur de resul…, cible, Fournisseur, remarques

## g1181（1 列）
- 見出し：Fournisseur
- 例1 値：Fournisseur 1 | Fournisseur 1 | Fournisseur 2 | Fournisseur 2 | Fournisseur 1
  - 同じ表の列：exercice fiscal, mois, indicateur de resul…, cible, resultats reels, remarques

## g1182（1 列）
- 見出し：remarques
- 例1 値：Depuis le Plan ministériel 2019-2020, l… | Depuis le Plan ministériel 2019-2020, l… | Depuis le Plan ministériel 2019-2020, l… | Depuis le Plan ministériel 2019-2020, l… | Depuis le Plan ministériel 2019-2020, l…
  - 同じ表の列：exercice fiscal, mois, indicateur de resul…, cible, resultats reels, Fournisseur

## g1183（1 列）
- 見出し：ref_number
- 例1 値：H-2016-Q2-00003 | H-2018-Q3-00005 | H-2018-Q2-012 | H-2016-Q4-009 | H-2026-P05-8138
  - 同じ表の列：disclosure_group, title_en, title_fr, start_date, end_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g1184（1 列）
- 見出し：disclosure_group
- 例1 値：SLE | SLE | SLE | SLE | SLE
  - 同じ表の列：ref_number, title_en, title_fr, start_date, end_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g1185（1 列）
- 見出し：title_en
- 例1 値：President | Acting Chief Transition Officer and Vic… | President | Vice-President, Prince Edward Island | Vice-President, Prince Edward Island
  - 同じ表の列：ref_number, disclosure_group, title_fr, start_date, end_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g1186（1 列）
- 見出し：title_fr
- 例1 値：Vice-president, Communications et affai… | Directeur exécutif et avocat général | Directeur exécutive et greffière par in… | Vice-président, programme d'immobilisat… | Sous-ministre ajointe, Direction généra…
  - 同じ表の列：ref_number, disclosure_group, title_en, start_date, end_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g1187（1 列）
- 見出し：vendor_2_en
- 例1 値：Evermoore Brewing Co. | Manhattan's Coffee Co. | Fairmont Queen Elizabeth | Ignite Pizzeria | Fairmont Queen Elizabeth
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, start_date, end_date, vendor_2_fr, vendor_other_en

## g1188（1 列）
- 見出し：vendor_2_fr
- 例1 値：Fairmont Queen Elizabeth | Gabriel Pizza | Ignite Pizzeria | Carmelito Café Preston | Brown's Plus+ Inc.
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, start_date, end_date, vendor_2_en, vendor_other_en

## g1189（1 列）
- 見出し：vendor_other_en
- 例1 値：67.85 | SuzyQ Doughnuts & Starbucks | 62.42 | Purple Potties | Ottawa Bagelshop & Deli & Real Canadian…
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, start_date, end_date, vendor_2_en, vendor_2_fr

## g1190（1 列）
- 見出し：vendor_other_fr
- 例1 値：Uber | Purple Potties | Ottawa Bagelshop & Deli & Real Canadian… | Brown's Plus+ Inc. | Evermoore Brewing Co.
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, start_date, end_date, vendor_2_en, vendor_2_fr

## g1191（1 列）
- 見出し：Number of communities benefitting from federal public infras
- 例1 値：217 | 167 | 671 | 115 | 172
  - 同じ表の列：Region

## g1192（1 列）
- 見出し：Value of international business activity facilitated by WD
- 例1 値：85,390,054 | 421,181,501 | 938,919,668 | 206,691,000 | 225,657,113
  - 同じ表の列：Region

## g1193（1 列）
- 見出し：Final Dispatch Code
- 例1 値：Code 2 | Code 2 | Code 1 | Code 1 | Code 1
  - 同じ表の列：%<=15mins, AVG RT - Seconds, Total Number

## g1194（1 列）
- 見出し：%<=15mins
- 例1 値：89.30% | 92.41% | 84.17% | 89.71% | 71.43%
  - 同じ表の列：Final Dispatch Code, AVG RT - Seconds, Total Number

## g1195（1 列）
- 見出し：AVG RT - Seconds
- 例1 値：1402 | 1327 | 667 | 570 | 646
  - 同じ表の列：Final Dispatch Code, %<=15mins, Total Number

## g1196（1 列）
- 見出し：Total Number
- 例1 値：654 | 353 | 535 | 441 | 1480
  - 同じ表の列：Final Dispatch Code, %<=15mins, AVG RT - Seconds

## g1197（1 列）
- 見出し：profile
- 例1 値：Families with children 0-12 years | Families with children 9-12 years | Families with children 0-5 years | Families with children 9-12 years | Families with children 0-5 years
  - 同じ表の列：census_year, category, sub_category, sub_order, value

## g1198（1 列）
- 見出し：census_year
- 例1 値：2016 | 2016 | 2016 | 2016 | 2016
  - 同じ表の列：profile, category, sub_category, sub_order, value

## g1199（1 列）
- 見出し：category
- 例1 値：Occupation | Language spoken at home - detailed | Personal weekly income - detailed | Language spoken at home - detailed | Dependent students in family
  - 同じ表の列：profile, census_year, sub_category, sub_order, value

## g1200（1 列）
- 見出し：sub_category
- 例1 値：Cared for other child/children | Count of families | $300 - $399 | Somali | Ethiopia
  - 同じ表の列：profile, census_year, category, sub_order, value

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
