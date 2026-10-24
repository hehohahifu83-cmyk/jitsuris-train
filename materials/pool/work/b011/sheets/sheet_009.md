# ラベル用シート 009 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：Title
- 例1 値：Sources of Financing to Buy/Acquire Bus… | Federal Government Procurement | Reasons Given by Credit Provider for Tu… | Intellectual Property | Primary Decision Maker Age, Place of Bi…
  - 同じ表の列：Table, Survey Question, Notes

## g0962（1 列）
- 見出し：Survey Question
- 例1 値：Survey question(s): C.1. In 2014, did y… | Survey question(s): D.2. For your busin… | Survey question(s): C.1. In 2014, did y… | Survey question(s): C.1. In 2014, did y… | Survey question(s): I.1. Over the last …
  - 同じ表の列：Table, Title, Notes

## g0963（1 列）
- 見出し：Notes
- 例1 値：Notes: I.3. is applicable to all respon… | Notes: D.1. is applicable to all respon… | Notes: I.1 is applicable only to those … | Notes: I.5. is applicable to only to th… | Notes: I.4. is applicable to all respon…
  - 同じ表の列：Table, Title, Survey Question

## g0964（1 列）
- 見出し：Organization Acronym - EN
- 例1 値：CSC | PSPC | CIRNAC | IRCC | PHAC
  - 同じ表の列：Fiscal Year, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0965（1 列）
- 見出し：Organization Acroym - FR
- 例1 値：CANAFE | ACC | GRC | FedDev Ontario | DEC
  - 同じ表の列：Fiscal Year, Organization Acrony…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0966（1 列）
- 見出し：Economic Object Code
- 例1 値：1172 | 444 | 813 | 473 | 494
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0967（1 列）
- 見出し：Category - EN
- 例1 値：Services | Services | Services | Services | Services
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - FR, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0968（1 列）
- 見出し：Category - FR
- 例1 値：Biens, terrains, bâtiments et travaux | Services | Services | Biens, terrains, bâtiments et travaux | Services
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Subcategory - EN, Subcategory - FR, Procurement Amount

## g0969（1 列）
- 見出し：Subcategory - EN
- 例1 値：Acquisition of machinery and equipment,… | Professional and special services | Materials and supplies (standard object… | Acquisition of machinery and equipment,… | Acquisition of machinery and equipment,…
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - FR, Procurement Amount

## g0970（1 列）
- 見出し：Subcategory - FR
- 例1 値：Information | Services professionnels et spéciaux | Acquisition de machinerie et matériel, … | Services professionnels et spéciaux | Réparation et entretien
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Procurement Amount

## g0971（1 列）
- 見出し：Procurement Amount
- 例1 値：$300 | $432,000 | $170,000 | $101,640 | $2,500
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR

## g0972（1 列）
- 見出し：Delivery Location of Goods and Services - EN
- 例1 値：Ontario | Canada | National Capital Region | National Capital Region and Regional Of… | National Capital Region
  - 同じ表の列：Fiscal Year, Organization Acrony…, Organization Acroym…, Economic Object Code, Category - EN, Category - FR, Subcategory - EN, Subcategory - FR

## g0973（1 列）
- 見出し：No unique
- 例1 値：248 | 674 | 185 | 753 | 819
  - 同じ表の列：Autorite, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, Essence, etat

## g0974（1 列）
- 見出し：Autorite
- 例1 値：Parcs Canada | Premieres Nations | Parcs Canada | Commission de la Capitale Nationale | Parcs Canada
  - 同じ表の列：No unique, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, Essence, etat

## g0975（1 列）
- 見出し：Endroit
- 例1 値：Forges St-Maurice | Parc de la Mauricie | Parc de la Gatineau | Parc de la Gatineau | Parc de la Gatineau
  - 同じ表の列：No unique, Autorite, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, Essence, etat

## g0976（1 列）
- 見出し：Place d'etude
- 例1 値：NIC-03 | MBR-01 | NIC-01 | PMA-02 | ODA-01
  - 同じ表の列：No unique, Autorite, Endroit, Arbre No, Arbre isole? 1=oui …, DATE, Essence, etat

## g0977（1 列）
- 見出し：Arbre No
- 例1 値：49 | 26 | 32 | 19 | 1
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre isole? 1=oui …, DATE, Essence, etat

## g0978（1 列）
- 見出し：Arbre isole? 1=oui 0=noyer en peuplement
- 例1 値：0 | 0 | 1 | 1 | 0
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre No, DATE, Essence, etat

## g0979（1 列）
- 見出し：Essence
- 例1 値：86 | 276 | 276 | 276 | 276
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, etat

## g0980（1 列）
- 見出し：etat
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, Essence

## g0981（1 列）
- 見出し：Localisation X (m)
- 例1 値：29,5 | 13 | 7 | 13,8 | 13
  - 同じ表の列：No unique, Autorite, Endroit, Place d'etude, Arbre No, Arbre isole? 1=oui …, DATE, Essence

## g0982（1 列）
- 見出し：QUEST
- 例1 値：27805 | 102564 | 55685 | 46082 | 3629
  - 同じ表の列：STYPE, CPO_STATUS, QF, Q1, Q2, Q3, Q4A, Q4B

## g0983（1 列）
- 見出し：STYPE
- 例1 値：1 | 2 | 2 | 2 | 1
  - 同じ表の列：QUEST, CPO_STATUS, QF, Q1, Q2, Q3, Q4A, Q4B

## g0984（1 列）
- 見出し：CPO_STATUS
- 例1 値：2 | 2 | 2 | 3 | 2
  - 同じ表の列：QUEST, STYPE, QF, Q1, Q2, Q3, Q4A, Q4B

## g0985（1 列）
- 見出し：QF
- 例1 値：9 | 7 | 6 | 9 | 6
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, Q1, Q2, Q3, Q4A, Q4B

## g0986（1 列）
- 見出し：Q4A
- 例1 値：6 | 2 | 3 | 4 | 6
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q1, Q2, Q3, Q4B

## g0987（1 列）
- 見出し：Q4B
- 例1 値：1 | 1 | 5 | 4 | 6
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q1, Q2, Q3, Q4A

## g0988（1 列）
- 見出し：Q4C
- 例1 値：5 | 2 | 7 | 6 | 4
  - 同じ表の列：QUEST, STYPE, CPO_STATUS, QF, Q1, Q2, Q3, Q4A

## g0989（1 列）
- 見出し：Calendar Year/Annee civile
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0990（1 列）
- 見出し：Calendar Month/Mois civil
- 例1 値：2026-02-28 | 2026-03-31 | 2026-03-31 | 2026-04-30 | 2026-05-31
  - 同じ表の列：Calendar Year/Annee…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0991（1 列）
- 見出し：Total Trust Companies/FIs
- 例1 値：Total Trust Companies | Total Trust Companies | Total Trust Companies | Total Trust Companies | Total Trust Companies
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Societes de f…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0992（1 列）
- 見出し：Total Societes de fiducie/IFFs
- 例1 値：Total Sociétés de fiducie | Total Sociétés de fiducie | Total Sociétés de fiducie | Total Sociétés de fiducie | Total Sociétés de fiducie
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0993（1 列）
- 見出し：Industry Group
- 例1 値：Trust Companies | Trust Companies | Trust Companies | Trust Companies | Trust Companies
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Groupe Sectoriel, Return/Releve, Return Title

## g0994（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Sociétés de fiducie | Sociétés de fiducie | Sociétés de fiducie | Sociétés de fiducie | Sociétés de fiducie
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Return/Releve, Return Title

## g0995（1 列）
- 見出し：Return/Releve
- 例1 値：M4 | M4 | M4 | M4 | M4
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Groupe Sectoriel, Return Title

## g0996（1 列）
- 見出し：Return Title
- 例1 値：M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Groupe Sectoriel, Return/Releve

## g0997（1 列）
- 見出し：Titre du releve
- 例1 値：M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Trust Compani…, Total Societes de f…, Industry Group, Groupe Sectoriel, Return/Releve

## g0998（2 列）
- 見出し：Type
- 例1 値：Place | Place | Place | Place | Place
  - 同じ表の列：Designation Date, Location, Province / Territory
- 例2 値：MUGA | Park | MUGA | Park | Walk
  - 同じ表の列：OBJECTID, Website, MUGA

## g0999（1 列）
- 見出し：Designation Date
- 例1 値：6/11/1973 | 11/6/1992 | 5/30/1960 | 3/10/1993 | 11/16/1990
  - 同じ表の列：Type, Location, Province / Territory

## g1000（1 列）
- 見出し：Location
- 例1 値：Fredericton | Abernethy | Chimney Island | Dawson | Toronto
  - 同じ表の列：Type, Designation Date, Province / Territory

## g1001（1 列）
- 見出し：Province / Territory
- 例1 値：Manitoba | British Columbia | Quebec | British Columbia | Quebec
  - 同じ表の列：Type, Designation Date, Location

## g1002（1 列）
- 見出し：Codes PCH_er
- 例1 値：er3590 | er1030 | er6110 | er3560 | er2470
  - 同じ表の列：Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1003（1 列）
- 見出し：Codes PCH_pr
- 例1 値：pr59 | pr35 | pr61 | pr13 | pr48
  - 同じ表の列：Codes PCH_er, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1004（1 列）
- 見出し：Dimension_f
- 例1 値：Institutionnelle | Démographique | Démolinguistique | Institutionnelle | Géographique
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1005（1 列）
- 見出し：Dimension_e
- 例1 値：Institutional | Demolinguistic | Socioeconomic | Demolinguistic | Demographic
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1006（1 列）
- 見出し：Indicateur_er
- 例1 値：3.509921843 | 1.232005177 | 1.168735214 | 2.424597634 | 1.248004797
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Rang_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1007（1 列）
- 見出し：Rang_er
- 例1 値：66 | 29 | 75 | 19 | 33
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Quintile_er, Niveau de vitalite_…, Vitality level_er

## g1008（1 列）
- 見出し：Quintile_er
- 例1 値：1 | 5 | 3 | 2 | 5
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Niveau de vitalite_…, Vitality level_er

## g1009（1 列）
- 見出し：Niveau de vitalite_er
- 例1 値：Faible | Élevé | Moyen | Élevé | Élevé
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Vitality level_er

## g1010（1 列）
- 見出し：Vitality level_er
- 例1 値：High | Low | Moderate | Very high | Very low
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…

## g1011（1 列）
- 見出し：Indicateur_pr
- 例1 値：1.375584206 | 0.903807901 | 0.846295113 | 1.217359973 | 1.217359973
  - 同じ表の列：Codes PCH_er, Codes PCH_pr, Dimension_f, Dimension_e, Indicateur_er, Rang_er, Quintile_er, Niveau de vitalite_…

## g1012（1 列）
- 見出し：Unique_id
- 例1 値：481 | 621 | 867 | 446 | 342
  - 同じ表の列：month_dv, PT, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C4, Q1_C5

## g1013（1 列）
- 見出し：month_dv
- 例1 値：11 | 3 | 11 | 12 | 2
  - 同じ表の列：Unique_id, PT, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C4, Q1_C5

## g1014（1 列）
- 見出し：PT
- 例1 値：2 | 5 | 5 | 6 | 7
  - 同じ表の列：Unique_id, month_dv, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C4, Q1_C5

## g1015（1 列）
- 見出し：DEMO8
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：Unique_id, month_dv, PT, Q1_C1, Q1_C2, Q1_C3, Q1_C4, Q1_C5

## g1016（1 列）
- 見出し：Q1_C1
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C2, Q1_C3, Q1_C4, Q1_C5

## g1017（1 列）
- 見出し：Q1_C2
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C1, Q1_C3, Q1_C4, Q1_C5

## g1018（1 列）
- 見出し：Q1_C3
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C1, Q1_C2, Q1_C4, Q1_C5

## g1019（1 列）
- 見出し：Q1_C4
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C5

## g1020（1 列）
- 見出し：Q1_C5
- 例1 値：1 | 1 | 1 | 0 | 1
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C4

## g1021（1 列）
- 見出し：Q1_C6
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Unique_id, month_dv, PT, DEMO8, Q1_C1, Q1_C2, Q1_C3, Q1_C4

## g1022（1 列）
- 見出し：fiscal_year
- 例1 値：2020-2021 | 2016-2017 | 2021-2022 | 2019-2020 | 2025-2026
  - 同じ表の列：provision_type_e, provision_type_f, application_type_e, application_type_f, applications_count, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1023（1 列）
- 見出し：provision_type_e
- 例1 値：Mobility | Preference | Mobility | Mobility | Mobility
  - 同じ表の列：fiscal_year, provision_type_f, application_type_e, application_type_f, applications_count, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1024（1 列）
- 見出し：provision_type_f
- 例1 値：Mobilité | Mobilité | Préférence | Mobilité | Mobilité
  - 同じ表の列：fiscal_year, provision_type_e, application_type_e, application_type_f, applications_count, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1025（1 列）
- 見出し：application_type_e
- 例1 値：CAF applications to internal advertisem… | CAF applications to internal advertisem… | Veteran applications to internal advert… | Veteran applications to external advert… | Veteran applications to external advert…
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_f, applications_count, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1026（1 列）
- 見出し：application_type_f
- 例1 値：Demandes d'emploi des anciens combattan… | Demandes d'emploi des membres FAC sur l… | Demandes d'emploi des anciens combattan… | Demandes d'emploi des anciens combattan… | Demandes d'emploi des anciens combattan…
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_e, applications_count, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1027（1 列）
- 見出し：applications_count
- 例1 値：976 | 356 | 618 | 683 | 1858
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_e, application_type_f, total_internal_adv_…, total_external_adv_…, processing_date_tra…

## g1028（1 列）
- 見出し：total_internal_adv_count
- 例1 値：1821 | 1957 | 297 | 1957 | 1381
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_e, application_type_f, applications_count, total_external_adv_…, processing_date_tra…

## g1029（1 列）
- 見出し：total_external_adv_count
- 例1 値：957 | 758 | 645 | 820 | 596
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_e, application_type_f, applications_count, total_internal_adv_…, processing_date_tra…

## g1030（1 列）
- 見出し：processing_date_traitement
- 例1 値：2026-09-03 | 2026-09-03 | 2026-09-03 | 2026-09-03 | 2026-09-03
  - 同じ表の列：fiscal_year, provision_type_e, provision_type_f, application_type_e, application_type_f, applications_count, total_internal_adv_…, total_external_adv_…

## g1031（1 列）
- 見出し：Fiscal Period
- 例1 値：5 | 8 | 1 | 7 | 7
  - 同じ表の列：Fiscal Year, Month, Total SLA Met, Total SLA Not met

## g1032（1 列）
- 見出し：Total SLA Met
- 例1 値：9 | 4 | 71 | 98 | 16
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Total SLA Not met

## g1033（1 列）
- 見出し：Total SLA Not met
- 例1 値：0 | 3 | 1 | 0 | 0
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Total SLA Met

## g1034（1 列）
- 見出し：Incentive Request Date
- 例1 値：2019-05-16 | 2019-05-16 | 2019-05-17 | 2019-05-16 | 2019-05-16
  - 同じ表の列：Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1035（1 列）
- 見出し：Month and Year
- 例1 値：May 2019 | May 2019 | May 2019 | May 2019 | May 2019
  - 同じ表の列：Incentive Request D…, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1036（1 列）
- 見出し：Government of Canada Fiscal Year (FY)
- 例1 値：2019-20 | 2019-20 | 2019-20 | 2019-20 | 2019-20
  - 同じ表の列：Incentive Request D…, Month and Year, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1037（1 列）
- 見出し：Calendar Year
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1038（1 列）
- 見出し：Dealership Province/Territory
- 例1 値：Quebec | British Columbia | British Columbia | Quebec | British Columbia
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Purchase or Lease, Vehicle Year, Vehicle Make, Vehicle Model

## g1039（1 列）
- 見出し：Purchase or Lease
- 例1 値：Purchase | Purchase | Purchase | Purchase | Purchase
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Vehicle Year, Vehicle Make, Vehicle Model

## g1040（1 列）
- 見出し：Vehicle Year
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Make, Vehicle Model

## g1041（1 列）
- 見出し：Vehicle Make
- 例1 値：Hyundai | Chevrolet | Hyundai | Hyundai | Chevrolet
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Model

## g1042（1 列）
- 見出し：Vehicle Model
- 例1 値：Bolt | Bolt | Ioniq electric | e-Golf | e-Golf
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make

## g1043（1 列）
- 見出し：Vehicle Make and Model
- 例1 値：Chevrolet Bolt | Nissan Leaf | Kia Soul EV | Hyundai Kona Electric | Chevrolet Bolt
  - 同じ表の列：Incentive Request D…, Month and Year, Government of Canad…, Calendar Year, Dealership Province…, Purchase or Lease, Vehicle Year, Vehicle Make

## g1044（1 列）
- 見出し：Population
- 例1 値：Saskatchewan | Manitoba | Western Canada | Alberta | British Columbia
  - 同じ表の列：Number of communiti…

## g1045（1 列）
- 見出し：Number of communities benefitting from Community Economic Gr
- 例1 値：216 | 257 | 541 | 1,431 | 417
  - 同じ表の列：Population

## g1046（1 列）
- 見出し：gis_id
- 例1 値：80 | 1551 | 2392 | 1882 | 1929
  - 同じ表の列：polyarea, property_id, date_updated, json_geometry, geo_point_2d

## g1047（1 列）
- 見出し：polyarea
- 例1 値：817 | 1015 | 139 | 6810 | 262
  - 同じ表の列：gis_id, property_id, date_updated, json_geometry, geo_point_2d

## g1048（1 列）
- 見出し：date_updated
- 例1 値：2026-09-28 | 2026-09-28 | 2026-09-28 | 2026-09-28 | 2026-09-28
  - 同じ表の列：gis_id, polyarea, property_id, json_geometry, geo_point_2d

## g1049（1 列）
- 見出し：json_geometry
- 例1 値：{"coordinates": [[[144.9273871927, -37.… | {"coordinates": [[[144.9700854838, -37.… | {"coordinates": [[[144.9427320532, -37.… | {"coordinates": [[[144.968573783, -37.8… | {"coordinates": [[[144.9554840578, -37.…
  - 同じ表の列：gis_id, polyarea, property_id, date_updated, geo_point_2d

## g1050（1 列）
- 見出し：geo_point_2d
- 例1 値：-37.816220415327294, 144.96297609909797 | -37.7973426804462, 144.93067068589693 | -37.798821886975816, 144.92814138082932 | -37.79042185014278, 144.9228526974754 | -37.83111064612636, 144.90141502540723
  - 同じ表の列：gis_id, polyarea, property_id, date_updated, json_geometry

## g1051（1 列）
- 見出し：Tree Species
- 例1 値：Casuarina stricta | Callistemon 'harkness' | Washingtonia filifera | Callistemon 'harkness' | Platanus x acerifolia
  - 同じ表の列：Tree Age, Trunk Circumference, Tree Health, Tree Structure, Tree Height

## g1052（1 列）
- 見出し：Tree Age
- 例1 値：Mature (50% Life Expectancy) | Mature (50% Life Expectancy) | Mature (50% Life Expectancy) | Mature (50% Life Expectancy) | Veteran (15% Life Expectancy)
  - 同じ表の列：Tree Species, Trunk Circumference, Tree Health, Tree Structure, Tree Height

## g1053（1 列）
- 見出し：Trunk Circumference
- 例1 値：Less than 2m | Less than 2m | Less than 2m | Less than 2m | Less than 2m
  - 同じ表の列：Tree Species, Tree Age, Tree Health, Tree Structure, Tree Height

## g1054（1 列）
- 見出し：Tree Health
- 例1 値：Good | Fair | Fair | Good | Good
  - 同じ表の列：Tree Species, Tree Age, Trunk Circumference, Tree Structure, Tree Height

## g1055（1 列）
- 見出し：Tree Structure
- 例1 値：Fair | Good | Fair | Fair | Fair
  - 同じ表の列：Tree Species, Tree Age, Trunk Circumference, Tree Health, Tree Height

## g1056（1 列）
- 見出し：Tree Height
- 例1 値：5-10m | 5-10m | less than 5m | 10-20m | 5-10m
  - 同じ表の列：Tree Species, Tree Age, Trunk Circumference, Tree Health, Tree Structure

## g1057（1 列）
- 見出し：David Mark Reimers
- 例1 値：Randstad Pty Limited | Dunn Transcripts Pty Ltd | Contractors with a contract value above… | 2020-21 | Paxus Australia Pty Limited
  - 同じ表の列：Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, Information technol…, $9,405.00

## g1058（1 列）
- 見出し：Procurement support
- 例1 値：Maladministration investigation | Temporary HR and Recruitment Officer | Total | Temporary Senior Governance Officer | Procurement support
  - 同じ表の列：David Mark Reimers, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, Information technol…, $9,405.00

## g1059（1 列）
- 見出し：$840.00
- 例1 値：$18,305.62 | $23,210.82 | $21,827.85 | $5,565.00 | $24,435.20
  - 同じ表の列：David Mark Reimers, Procurement support, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, Information technol…, $9,405.00

## g1060（1 列）
- 見出し：Dunn Transcripts Pty Ltd
- 例1 値：Dunn Transcripts Pty Ltd | Dunn Transcripts Pty Ltd | Randstad Pty Ltd | Contractors with a contract value above… | Contractors
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Maladministration i…, $9,331.75, David Reimers, Information technol…, $9,405.00

## g1061（1 列）
- 見出し：Maladministration investigation
- 例1 値：Total | Procurement support | Information technology support | Protective security maturity support | Corruption investigation
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, $9,331.75, David Reimers, Information technol…, $9,405.00

## g1062（1 列）
- 見出し：$9,331.75
- 例1 値：$41,184.91 | $3,095.29 | $16,057.48 | $16,076.04 | $5,810.67
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, David Reimers, Information technol…, $9,405.00

## g1063（1 列）
- 見出し：David Reimers
- 例1 値：Randstad Pty Ltd | 2018-19 | Randstad Pty Ltd | Contractors | Dunn Transcripts Pty Ltd
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, Information technol…, $9,405.00

## g1064（1 列）
- 見出し：Information technology support
- 例1 値：Maladministration investigation | Purpose | Total | Corruption investigation | Temporary Administration Officer
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, $9,405.00

## g1065（1 列）
- 見出し：$9,405.00
- 例1 値：$ Actual payment | $7,412.93 | $11,025.00 | $7,104.00 | $11,025.00
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, Information technol…

## g1066（1 列）
- 見出し：Docs in the Box
- 例1 値：Contract staff | Dunn Transcripts | Randstad | Dunn Transcripts | Contractors with a contract value above…
  - 同じ表の列：David Mark Reimers, Procurement support, $840.00, Dunn Transcripts Pt…, Maladministration i…, $9,331.75, David Reimers, Information technol…

## g1067（1 列）
- 見出し：Time
- 例1 値：2021-05-06T23:41:20+10:00 | 2021-05-07T07:22:13+10:00 | 2021-05-07T10:18:51+10:00 | 2021-05-07T08:08:59+10:00 | 2021-05-07T02:12:09+10:00
  - 同じ表の列：Device ID, Temperature (°C), Humidity (%), Sensor Type, Location, TTN metadata, TTN payload fields

## g1068（1 列）
- 見出し：Device ID
- 例1 値：70b3d57ba0000b5e | 70b3d57ba0000b5d | 70b3d57ba0000b65 | 70b3d57ba0000b66 | 70b3d57ba0000b5d
  - 同じ表の列：Time, Temperature (°C), Humidity (%), Sensor Type, Location, TTN metadata, TTN payload fields

## g1069（1 列）
- 見出し：Temperature (°C)
- 例1 値：18.572518501564048 | 18.44167238879988 | 18.193331807431143 | 18.682001983672848 | 19.42969405661097
  - 同じ表の列：Time, Device ID, Humidity (%), Sensor Type, Location, TTN metadata, TTN payload fields

## g1070（1 列）
- 見出し：Humidity (%)
- 例1 値：95.14763103685054 | 97.63179980163271 | 93.45845731288624 | 95.4207675288014 | 91.08720531013962
  - 同じ表の列：Time, Device ID, Temperature (°C), Sensor Type, Location, TTN metadata, TTN payload fields

## g1071（1 列）
- 見出し：Sensor Type
- 例1 値：DLB | DLB | DLB | DLB | DLB
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Location, TTN metadata, TTN payload fields

## g1072（1 列）
- 見出し：Location
- 例1 値：-32.9725,151.7017 | -32.96178,151.61884 | -32.9643,151.697 | -32.96359,151.6971 | -32.9679,151.6948
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Sensor Type, TTN metadata, TTN payload fields

## g1073（1 列）
- 見出し：TTN metadata
- 例1 値：{"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r…
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Sensor Type, Location, TTN payload fields

## g1074（1 列）
- 見出し：TTN payload fields
- 例1 値：{"battery": 3.017, "type": "DLB", "temp… | {"battery": 2.973, "type": "DLB", "temp… | {"battery": 3.017, "type": "DLB", "temp… | {"battery": 3.017, "type": "DLB", "temp… | {"battery": 2.895, "type": "DLB", "temp…
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%), Sensor Type, Location, TTN metadata

## g1075（1 列）
- 見出し：ID_DECLIV_TRECHO_UFMG_2007
- 例1 値：944 | 556 | 537 | 868 | 225
  - 同じ表の列：ID_TRECHO, LARGURA, COTA_MINIMA, COTA_MEDIA, COTA_MAXIMA, GEOMETRIA

## g1076（1 列）
- 見出し：ID_TRECHO
- 例1 値：49180 | 49753 | 49333 | 49914 | 67
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, LARGURA, COTA_MINIMA, COTA_MEDIA, COTA_MAXIMA, GEOMETRIA

## g1077（1 列）
- 見出し：LARGURA
- 例1 値：1.0 | 11.95 | 3.46 | 8.03 | 10.62
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, ID_TRECHO, COTA_MINIMA, COTA_MEDIA, COTA_MAXIMA, GEOMETRIA

## g1078（1 列）
- 見出し：COTA_MINIMA
- 例1 値：816.453336166 | 813.254042711 | 967.35826414 | 840.40353214 | 699.534004732
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, ID_TRECHO, LARGURA, COTA_MEDIA, COTA_MAXIMA, GEOMETRIA

## g1079（1 列）
- 見出し：COTA_MEDIA
- 例1 値：1154.50352948 | 1016.29031197 | 993.076056609 | 1154.83759531 | 876.126098908
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, ID_TRECHO, LARGURA, COTA_MINIMA, COTA_MAXIMA, GEOMETRIA

## g1080（1 列）
- 見出し：COTA_MAXIMA
- 例1 値：750.0 | 921.983488839 | 723.770021016 | 767.408056726 | 876.999622601
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, ID_TRECHO, LARGURA, COTA_MINIMA, COTA_MEDIA, GEOMETRIA

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
