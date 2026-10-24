# ラベル用シート 007 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：2018/19
- 例1 値：2684 | 124 | 28 | 671 | 590
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2014/15, 2015/16, 2016/17, 2017/18

## g0722（1 列）
- 見出し：2019/20
- 例1 値：484 | 2961 | 726 | 896 | 704
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2014/15, 2015/16, 2016/17, 2017/18

## g0723（2 列）
- 見出し：departmental_identification_number
- 例1 値：OI-510 | OI-1032 | OI-1033 | OI-454 | OI-1037
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published
- 例2 値：OI-569 | OI-574 | OI-546 | OI-557 | OI-568
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0724（1 列）
- 見出し：title_translated_en
- 例1 値：Turkey TRQ – Non-ICL Allocation Quota H… | Notice to Importers Turkey and Turkey P… | Notice to Importers Turkey and Turkey P… | CPTPP Turkey Quota Holders List - 2020-… | Turkey TRQ - Allocation to Traditional …
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0725（1 列）
- 見出し：title_translated_fr
- 例1 値：PTPGP : CT du dindon et produits du din… | OMC - Liste des détenteurs de contingen… | Liste des détenteurs de contingent de d… | Avis aux importateurs Dindon et produit… | OMC: CT du dindon et produits de dindon…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0726（1 列）
- 見出し：notes_translated_en
- 例1 値：Accountant’s letter for applicants requ… | Turkey and Turkey Products (Items 105 t… | CPTPP Turkey Quota Holders List | Turkey TRQ – Non-ICL Allocation Quota H… | Imports Permit Issuance for Turkey and …
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0727（1 列）
- 見出し：notes_translated_fr
- 例1 値：Données sur l’utilisation - Dindon et p… | Dindon et produits du dindon (Articles … | Dindon et produits du dindon (Articles … | Délivrance de licences d’importation - … | Délivrance de licences d’importation - …
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0728（2 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0729（2 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0730（2 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published
- 例2 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0731（2 列）
- 見出し：date_published
- 例1 値：2019-04-02 | 2020-03-02 | 2022-01-14 | 2022-01-26 | 2016-09-30
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：2024-05-01 | 2020-08-04 | 2022-01-17 | 2020-05-01 | 2024-07-31
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0732（2 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0733（1 列）
- 見出し：Program Year / Annee du programme
- 例1 値：2025 | 2025 | 2025 | 2025 | 2025
  - 同じ表の列：Region / Region, Activity Constituen…, Circonscription de …, Amount Paid / Monta…, Confirmed Jobs Crea…

## g0734（1 列）
- 見出し：Region / Region
- 例1 値：Alberta | Alberta | Alberta | Alberta | Alberta
  - 同じ表の列：Program Year / Anne…, Activity Constituen…, Circonscription de …, Amount Paid / Monta…, Confirmed Jobs Crea…

## g0735（1 列）
- 見出し：Activity Constituency
- 例1 値：Calgary Centre | Bow River | Calgary Centre | Calgary Centre | Calgary Centre
  - 同じ表の列：Program Year / Anne…, Region / Region, Circonscription de …, Amount Paid / Monta…, Confirmed Jobs Crea…

## g0736（1 列）
- 見出し：Circonscription de l'activite
- 例1 値：Battle River - Crowfoot | Calgary Heritage | Edmonton - Wetaskiwin | Calgary-Centre | Calgary Skyview
  - 同じ表の列：Program Year / Anne…, Region / Region, Activity Constituen…, Amount Paid / Monta…, Confirmed Jobs Crea…

## g0737（1 列）
- 見出し：Amount Paid / Montant paye
- 例1 値：1800 | 8400 | 28018 | 4741 | 35427
  - 同じ表の列：Program Year / Anne…, Region / Region, Activity Constituen…, Circonscription de …, Confirmed Jobs Crea…

## g0738（1 列）
- 見出し：Confirmed Jobs Created / Emplois confirmes crees
- 例1 値：1 | 2 | 2 | 1 | 1
  - 同じ表の列：Program Year / Anne…, Region / Region, Activity Constituen…, Circonscription de …, Amount Paid / Monta…

## g0739（1 列）
- 見出し：Table
- 例1 値：31 | 13 | 30 | 4 | 10
  - 同じ表の列：Title, Survey question, Notes

## g0740（1 列）
- 見出し：Title
- 例1 値：Exports (Percentage of business that ex… | Innovation Activities and Reason for No… | Intended Use of Debt Financing | Provider of External Financing | Business Financial Figures
  - 同じ表の列：Table, Survey question, Notes

## g0741（1 列）
- 見出し：Survey question
- 例1 値：Survey question(s): C.4. What reasons w… | Survey question(s): H.1. What was the v… | Survey question(s): I.1. What is the ag… | Survey question(s): K.8. Does your busi… | Survey question(s): J.3. What was the r…
  - 同じ表の列：Table, Title, Notes

## g0742（1 列）
- 見出し：Notes
- 例1 値：Notes: B.8. is applicable only to those… | Notes: K.3. is applicable only to those… | Notes: K.1. is applicable to all respon… | Notes: H.9. is applicable to all respon… | Notes: H.1. is applicable to all respon…
  - 同じ表の列：Table, Title, Survey question

## g0743（2 列）
- 見出し：annee
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…
- 例2 値：2015 | 2015 | 2013 | 2015 | 2014
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, DATE, Mois, Duree depuis le tra…, DHP (cm)

## g0744（1 列）
- 見出し：numero_groupe_enregistrement
- 例1 値：288 | 16 | 558 | 817 | 387
  - 同じ表の列：annee, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…

## g0745（1 列）
- 見出し：nom_groupe_enregistrement
- 例1 値：Sturgeon Lake Cree Nation | Kwakiutl | Cree Nation of Mistissini | Seine River First Nation | Bridge River
  - 同じ表の列：annee, numero_groupe_enreg…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…

## g0746（1 列）
- 見出し：region
- 例1 値：Saskatchewan | Manitoba | Ontario | Atlantique | Colombie-Britannique
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…

## g0747（1 列）
- 見出し：prov_terr
- 例1 値：Québec | Nouveau-Brunswick | Colombie-Britannique | Colombie-Britannique | Ontario
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, district, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…

## g0748（1 列）
- 見出し：district
- 例1 値：NA | NA | NA | District Alberta | NA
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, pop_reserves_terre_…, pop_reserves_terre_…, pop_reserves_terre_…

## g0749（1 列）
- 見出し：pop_reserves_terre_couronne_hommes
- 例1 値：489 | 445 | X | 84 | X
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…

## g0750（1 列）
- 見出し：pop_reserves_terre_couronne_femmes
- 例1 値：35 | 426 | 848 | 81 | X
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…

## g0751（1 列）
- 見出し：pop_reserves_terre_couronne_total
- 例1 値：1140 | 748 | 965 | 518 | 1083
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…

## g0752（1 列）
- 見出し：pop_hors_reserve_hommes
- 例1 値：111 | 166 | 219 | 259 | 947
  - 同じ表の列：annee, numero_groupe_enreg…, nom_groupe_enregist…, region, prov_terr, district, pop_reserves_terre_…, pop_reserves_terre_…

## g0753（1 列）
- 見出し：Traitement
- 例1 値：Émondé | Témoin | Témoin | Éclairci | Témoin
  - 同じ表の列：Autorite, Endroit, Numero, DATE, Mois, Annee, Duree depuis le tra…, DHP (cm)

## g0754（1 列）
- 見出し：Autorite
- 例1 値：Université Laval | Défense nationale | Défense nationale | Université Laval | Université Laval
  - 同じ表の列：Traitement, Endroit, Numero, DATE, Mois, Annee, Duree depuis le tra…, DHP (cm)

## g0755（1 列）
- 見出し：Endroit
- 例1 値：Saint-Augustin | Saint-Augustin | Saint-Augustin | Saint-Augustin | Saint-Augustin
  - 同じ表の列：Traitement, Autorite, Numero, DATE, Mois, Annee, Duree depuis le tra…, DHP (cm)

## g0756（1 列）
- 見出し：Numero
- 例1 値：UL 08 | MSB 22 | UL 19 | UL 10 | MSB 22
  - 同じ表の列：Traitement, Autorite, Endroit, DATE, Mois, Annee, Duree depuis le tra…, DHP (cm)

## g0757（1 列）
- 見出し：DATE
- 例1 値：2014-08-22 | 2013-08-15 | 2014-08-22 | 2013.08.21 | 2012-07-12
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, Mois, Annee, Duree depuis le tra…, DHP (cm)

## g0758（1 列）
- 見出し：Mois
- 例1 値：08 | 08 | 08 | 07 | 07
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, DATE, Annee, Duree depuis le tra…, DHP (cm)

## g0759（1 列）
- 見出し：Duree depuis le traitement (mois)
- 例1 値：53 | 23 | 17 | 42 | 53
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, DATE, Mois, Annee, DHP (cm)

## g0760（1 列）
- 見出し：DHP (cm)
- 例1 値：53,6 | 45,0 | 36,9 | 34,8 | 38,7
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, DATE, Mois, Annee, Duree depuis le tra…

## g0761（1 列）
- 見出し：Surface terriere (St) (cm2)
- 例1 値：1669,1 | 692,8 | 1152,1 | 1372,3 | 1164,2
  - 同じ表の列：Traitement, Autorite, Endroit, Numero, DATE, Mois, Annee, Duree depuis le tra…

## g0762（2 列）
- 見出し：PROV
- 例1 値：SK | QC | ON | AB | ON
  - 同じ表の列：AREA, LANG, Q1, Q2, Q3M1, Q3M2, Q3M3, Q4M1
- 例2 値：NB | BC | BC | BC | ON
  - 同じ表の列：STYPE, QF, Q1, Q2, Q3, Q4A, Q4B, Q4C

## g0763（1 列）
- 見出し：AREA
- 例1 値：2 | 2 | 7 | 7 | 4
  - 同じ表の列：PROV, LANG, Q1, Q2, Q3M1, Q3M2, Q3M3, Q4M1

## g0764（1 列）
- 見出し：LANG
- 例1 値：FR | EN | FR | EN | EN
  - 同じ表の列：PROV, AREA, Q1, Q2, Q3M1, Q3M2, Q3M3, Q4M1

## g0765（2 列）
- 見出し：Q1
- 例1 値：3 | 1 | 2 | 2 | 3
  - 同じ表の列：PROV, AREA, LANG, Q2, Q3M1, Q3M2, Q3M3, Q4M1
- 例2 値：5 | 4 | 4 | 6 | 2
  - 同じ表の列：STYPE, PROV, QF, Q2, Q3, Q4A, Q4B, Q4C

## g0766（2 列）
- 見出し：Q2
- 例1 値：4 | 99 | 7 | 4 | 6
  - 同じ表の列：PROV, AREA, LANG, Q1, Q3M1, Q3M2, Q3M3, Q4M1
- 例2 値：5 | 2 | 4 | 6 | 4
  - 同じ表の列：STYPE, PROV, QF, Q1, Q3, Q4A, Q4B, Q4C

## g0767（1 列）
- 見出し：Q3M1
- 例1 値：2 | 3 | 2 | 2 | 3
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3M2, Q3M3, Q4M1

## g0768（1 列）
- 見出し：Q3M2
- 例1 値：21 | 20 | 2 | 3 | 2
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3M1, Q3M3, Q4M1

## g0769（1 列）
- 見出し：Q3M3
- 例1 値：3 | 1 | 3 | 3 | 3
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3M1, Q3M2, Q4M1

## g0770（1 列）
- 見出し：Q4M1
- 例1 値：98 | 8 | 1 | 8 | 8
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3M1, Q3M2, Q3M3

## g0771（1 列）
- 見出し：Q4M2
- 例1 値：1 | 8 | 8 | 8 | 5
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3M1, Q3M2, Q3M3

## g0772（2 列）
- 見出し：Calendar Year/Annee civile
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title
- 例2 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0773（2 列）
- 見出し：Calendar Month/Mois civil
- 例1 値：2026-04-30 | 2026-09-30 | 2026-03-31 | 2026-09-30 | 2026-05-31
  - 同じ表の列：Calendar Year/Annee…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title
- 例2 値：2026-06-30 | 2026-06-30 | 2026-06-30 | 2026-06-30 | 2026-05-31
  - 同じ表の列：Calendar Year/Annee…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0774（1 列）
- 見出し：Total FBBs/Total Industry Groups/FIs
- 例1 値：Total All Banks | Total All Banks | Total All Banks | Total All Banks | Total All Banks
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0775（1 列）
- 見出し：Total les SBE/Total des groupe sectoriel/IFFs
- 例1 値：Total toutes les banques | Total toutes les banques | Total toutes les banques | Total toutes les banques | Total toutes les banques
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Industry Group, Groupe Sectoriel, Return/Releve, Return Title

## g0776（2 列）
- 見出し：Industry Group
- 例1 値：All Banks | All Banks | All Banks | All Banks | All Banks
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Groupe Sectoriel, Return/Releve, Return Title
- 例2 値：Loan Companies | Loan Companies | Loan Companies | Loan Companies | Loan Companies
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Groupe Sectoriel, Return/Releve, Return Title

## g0777（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Toutes les banques | Toutes les banques | Toutes les banques | Toutes les banques | Toutes les banques
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Return/Releve, Return Title

## g0778（2 列）
- 見出し：Return/Releve
- 例1 値：M4 | M4 | M4 | M4 | M4
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return Title
- 例2 値：M4 | M4 | M4 | M4 | M4
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Groupe Sectoriel, Return Title

## g0779（2 列）
- 見出し：Return Title
- 例1 値：M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return/Releve
- 例2 値：M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet | M4 - Consolidated Balance Sheet
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Groupe Sectoriel, Return/Releve

## g0780（2 列）
- 見出し：Titre du releve
- 例1 値：M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total FBBs/Total In…, Total les SBE/Total…, Industry Group, Groupe Sectoriel, Return/Releve
- 例2 値：M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé | M4 - Bilan consolidé
  - 同じ表の列：Calendar Year/Annee…, Calendar Month/Mois…, Id, Total Loan Companie…, Total Societes de p…, Industry Group, Groupe Sectoriel, Return/Releve

## g0781（1 列）
- 見出し：Species code
- 例1 値：WETO | LTSA | LTSA | WETO | CSFR
  - 同じ表の列：ID, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2010_Visit3, 2013_Visit1

## g0782（1 列）
- 見出し：2009_Visit1
- 例1 値：. | . | . | . | .
  - 同じ表の列：ID, Species code, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2010_Visit3, 2013_Visit1

## g0783（1 列）
- 見出し：2009_Visit2
- 例1 値：. | . | . | . | .
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2010_Visit3, 2013_Visit1

## g0784（1 列）
- 見出し：2009_Visit3
- 例1 値：. | . | . | . | .
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2010_Visit1, 2010_Visit2, 2010_Visit3, 2013_Visit1

## g0785（1 列）
- 見出し：2010_Visit1
- 例1 値：. | 0 | 0 | 0 | 1
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit2, 2010_Visit3, 2013_Visit1

## g0786（1 列）
- 見出し：2010_Visit2
- 例1 値：0 | 0 | . | 0 | 0
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit3, 2013_Visit1

## g0787（1 列）
- 見出し：2010_Visit3
- 例1 値：. | 0 | . | 0 | .
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2013_Visit1

## g0788（1 列）
- 見出し：2013_Visit1
- 例1 値：0 | 0 | 0 | . | 0
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2010_Visit3

## g0789（1 列）
- 見出し：2013_Visit2
- 例1 値：0 | 0 | . | 0 | .
  - 同じ表の列：ID, Species code, 2009_Visit1, 2009_Visit2, 2009_Visit3, 2010_Visit1, 2010_Visit2, 2010_Visit3

## g0790（4 列）
- 見出し：Fiscal Year
- 例1 値：2017-2018 | 2016-2017 | 2016-2017 | 2016-2017 | 2017-2018
  - 同じ表の列：City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type, Disciplines
- 例2 値：2021-2022 | 2021-2022 | 2020-2021 | 2021-2022 | 2023-2024
  - 同じ表の列：Fiscal Period, Month, Information Date, Metric, Request Fulfillment…, # of Service Reques…

## g0791（1 列）
- 見出し：City
- 例1 値：London | Saint John | Flin Flon | Ottawa | Owen Sound
  - 同じ表の列：Fiscal Year, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type, Disciplines

## g0792（1 列）
- 見出し：Province
- 例1 値：Quebec | Manitoba | Quebec | Ontario | Alberta
  - 同じ表の列：Fiscal Year, City, Region, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type, Disciplines

## g0793（2 列）
- 見出し：Community Type
- 例1 値：Large Urban | Remote | Large Urban | Large Urban | Large Urban
  - 同じ表の列：Fiscal Year, City, Province, Region, Grant Or Contributi…, Amount Approved, Presenter Type, Disciplines
- 例2 値：Large Urban | Large Urban | Remote | Remote | Small Urban
  - 同じ表の列：Fiscal Year, City, Province, Region, Grant Or Contributi…, Amount Approved, Disciplines, Audiences

## g0794（1 列）
- 見出し：Grant Or Contributionution
- 例1 値：Grant | Grant | Grant | Grant | Contribution
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Amount Approved, Presenter Type, Disciplines

## g0795（2 列）
- 見出し：Amount Approved
- 例1 値：10000 | 9000 | 22000 | 7500 | 12000
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Presenter Type, Disciplines
- 例2 値：245000 | 10521 | 442064 | 50000 | 10837
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Disciplines, Audiences

## g0796（1 列）
- 見出し：Presenter Type
- 例1 値：Multidisciplinary | Specialized | Multidisciplinary | Multidisciplinary | Multidisciplinary
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Disciplines

## g0797（1 列）
- 見出し：Disciplines
- 例1 値：Visual Arts, Dance, Music, Theatre | Music | Visual Arts, Dance, Literature, Media A… | Music | Music
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type

## g0798（1 列）
- 見出し：Audiences
- 例1 値：None | None | Official Language Minority | Cultural Diversity, Young Audience | Indigenous Communities
  - 同じ表の列：Fiscal Year, City, Province, Region, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type

## g0799（1 列）
- 見出し：dept_f
- 例1 値：Fonction Publique Fédérale | Fonction Publique Fédérale | Fonction Publique Fédérale | Fonction Publique Fédérale | Fonction Publique Fédérale
  - 同じ表の列：dept_e, question, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0800（1 列）
- 見出し：dept_e
- 例1 値：Federal Public Service | Federal Public Service | Federal Public Service | Federal Public Service | Federal Public Service
  - 同じ表の列：dept_f, question, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0801（1 列）
- 見出し：question
- 例1 値：STA_16B_5 | GDR_11A_4 | MAN_06A_1 | MAN_04A_2 | HMN_05_3
  - 同じ表の列：dept_f, dept_e, question_value_f, question_value_e, shr_w_resp, total_w_resp

## g0802（1 列）
- 見出し：question_value_f
- 例1 値：Oui | Non sélectionné | Pas du tout | Sélectionné | Non sélectionné
  - 同じ表の列：dept_f, dept_e, question, question_value_e, shr_w_resp, total_w_resp

## g0803（1 列）
- 見出し：question_value_e
- 例1 値：Not selected | Not selected | To a great extent | Selected | All respondents
  - 同じ表の列：dept_f, dept_e, question, question_value_f, shr_w_resp, total_w_resp

## g0804（1 列）
- 見出し：shr_w_resp
- 例1 値：0.921 | 0.106 | 0.672 | 0.795 | 1
  - 同じ表の列：dept_f, dept_e, question, question_value_f, question_value_e, total_w_resp

## g0805（1 列）
- 見出し：total_w_resp
- 例1 値：63493 | 7669 | 1158 | 11847 | 6
  - 同じ表の列：dept_f, dept_e, question, question_value_f, question_value_e, shr_w_resp

## g0806（2 列）
- 見出し：Fiscal Period
- 例1 値：3 | 9 | 5 | 8 | 6
  - 同じ表の列：Fiscal Year, Month, Information Date, Metric, Request Fulfillment…, # of Service Reques…
- 例2 値：9 | 7 | 1 | 1 | 3
  - 同じ表の列：Fiscal Year, Month, Information Date, # of service reques…, Turnaround time (in…, # of transactions c…, # of transactions N…, % delivered within …

## g0807（2 列）
- 見出し：Information Date
- 例1 値：5/1/2020 | 5/31/2024 | 10/31/2024 | 10/31/2023 | 10/31/2025
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Metric, Request Fulfillment…, # of Service Reques…
- 例2 値：5/31/2020 | 7/31/2020 | 1/31/2023 | 12/31/2020 | 9/30/2025
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, # of service reques…, Turnaround time (in…, # of transactions c…, # of transactions N…, % delivered within …

## g0808（1 列）
- 見出し：Metric
- 例1 値：Time Sensitive (15 Days) | Time Sensitive (15 Days) | Call Ups NMSO (30 Days) | RVD (60 Days) | Time Sensitive (15 Days)
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Request Fulfillment…, # of Service Reques…

## g0809（1 列）
- 見出し：Request Fulfillment in Days
- 例1 値：12.83 | 16.67 | 62.4 | 13.67 | 7.17
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Metric, # of Service Reques…

## g0810（1 列）
- 見出し：# of Service Requests
- 例1 値：1 | 2 | 6 | 1 | 94
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Metric, Request Fulfillment…

## g0811（1 列）
- 見出し：fiscal_yr
- 例1 値：2024-2025 | 2024-2025 | 2024-2025 | 2023-2024 | 2023-2024
  - 同じ表の列：service_id, service_standard_id, service_standard_en, service_standard_fr, type, channel, channel_comments_en, channel_comments_fr

## g0812（1 列）
- 見出し：service_id
- 例1 値：2150 | 1920 | SRV03291 | 131 | SRV03350
  - 同じ表の列：fiscal_yr, service_standard_id, service_standard_en, service_standard_fr, type, channel, channel_comments_en, channel_comments_fr

## g0813（1 列）
- 見出し：service_standard_id
- 例1 値：2669 | 8727 | 5061 | STAN00005740 | 2614
  - 同じ表の列：fiscal_yr, service_id, service_standard_en, service_standard_fr, type, channel, channel_comments_en, channel_comments_fr

## g0814（1 列）
- 見出し：service_standard_en
- 例1 値：Send you an approval or a rejection not… | Our goal is to issue your notice of ass… | The 12 All-Sky Imagers maintain an aver… | Percentage of processed applications un… | Percentage of draft audit reports will …
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_fr, type, channel, channel_comments_en, channel_comments_fr

## g0815（1 列）
- 見出し：service_standard_fr
- 例1 値：Demeurer accessible pour collaborer et … | Importation de produits biologiques vét… | Pourcentage des rapports préliminaires … | Traiter une demande de nouvel agrément … | Subvention : Une fois que le financemen…
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_en, type, channel, channel_comments_en, channel_comments_fr

## g0816（1 列）
- 見出し：channel
- 例1 値：OTH | ONL | EML | EML | EML
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_en, service_standard_fr, type, channel_comments_en, channel_comments_fr

## g0817（1 列）
- 見出し：channel_comments_en
- 例1 値：All business lines | Target type: A valid statistical sample… | Mail, Telephone, Email | The delivery channel is by the departme… | All inbound enquiries are received by e…
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_en, service_standard_fr, type, channel, channel_comments_fr

## g0818（1 列）
- 見出し：channel_comments_fr
- 例1 値：Appels reçus en ligne et par courrier. … | S.O. | Demandes reçues par téléphone, en perso… | Les paiements sont effectués au moyen d… | Demandes reçues par téléphone, en perso…
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_en, service_standard_fr, type, channel, channel_comments_en

## g0819（1 列）
- 見出し：target
- 例1 値：0.8 | 0.85 | 0.9 | 0.85 | 0.8
  - 同じ表の列：fiscal_yr, service_id, service_standard_id, service_standard_en, service_standard_fr, type, channel, channel_comments_en

## g0820（1 列）
- 見出し：geo_point_2d
- 例1 値：-37.79765952177993, 144.91995554122124 | -37.79793343497252, 144.94618500848327 | -37.79634745110544, 144.91970003228104 | -37.80063041773851, 144.95284387083993 | -37.79647379409297, 144.92048377495283
  - 同じ表の列：geo_shape, data_lin_1, yearplant, park_stree, location, scientific, height_112, data_linea

## g0821（1 列）
- 見出し：geo_shape
- 例1 値：{"coordinates": [[[[144.945862171837, -… | {"coordinates": [[[[144.9616401409028, … | {"coordinates": [[[[144.96897118564453,… | {"coordinates": [[[[144.9653619622429, … | {"coordinates": [[[[144.92381153354518,…
  - 同じ表の列：geo_point_2d, data_lin_1, yearplant, park_stree, location, scientific, height_112, data_linea

## g0822（1 列）
- 見出し：data_lin_1
- 例1 値：Tree Inventory: Existing data (fields f… | Tree Inventory: Existing data (fields f… | Tree Inventory: Existing data (fields f… | Tree Inventory: Existing data (fields f… | Tree Inventory: Existing data (fields f…
  - 同じ表の列：geo_point_2d, geo_shape, yearplant, park_stree, location, scientific, height_112, data_linea

## g0823（1 列）
- 見出し：yearplant
- 例1 値：0 | 2006 | 0 | 0 | 0
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, park_stree, location, scientific, height_112, data_linea

## g0824（1 列）
- 見出し：park_stree
- 例1 値：Street | Street | Street | Street | Street
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, location, scientific, height_112, data_linea

## g0825（1 列）
- 見出し：location
- 例1 値：MacAulay Road between Haines Street and… | J.J. Holland Park | J.J. Holland Park | Haines Street between Curzon Street and… | Grattan Street between Lygon Street and…
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, park_stree, scientific, height_112, data_linea

## g0826（1 列）
- 見出し：scientific
- 例1 値：Ulmus procera | Zelkova serrata | Platanus x acerifolia | Platanus x acerifolia | Angophora costata
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, park_stree, location, height_112, data_linea

## g0827（1 列）
- 見出し：height_112
- 例1 値：12.0 | 5.0 | 8.0 | 3.0 | 1.0
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, park_stree, location, scientific, data_linea

## g0828（1 列）
- 見出し：data_linea
- 例1 値：Tree Canopy: Mapped using LiDAR and 201… | Tree Canopy: Mapped using LiDAR and 201… | Tree Canopy: Mapped using LiDAR and 201… | Tree Canopy: Mapped using LiDAR and 201… | Tree Canopy: Mapped using LiDAR and 201…
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, park_stree, location, scientific, height_112

## g0829（1 列）
- 見出し：ule
- 例1 値：11-20 years | 61+ years | 61+ years | 31-60 years | 61+ years
  - 同じ表の列：geo_point_2d, geo_shape, data_lin_1, yearplant, park_stree, location, scientific, height_112

## g0830（1 列）
- 見出し：Animal Quantity
- 例1 値：1 | 2 | 2 | 1 | 1
  - 同じ表の列：Animal Colour, Animal Date of Birth, Animal Sex, Animal Neutered

## g0831（1 列）
- 見出し：Animal Colour
- 例1 値：Black | Black | Black | Black | Black
  - 同じ表の列：Animal Quantity, Animal Date of Birth, Animal Sex, Animal Neutered

## g0832（1 列）
- 見出し：Animal Date of Birth
- 例1 値：20090322 | 20000403 | 20050310 | 20041208 | 20020519
  - 同じ表の列：Animal Quantity, Animal Colour, Animal Sex, Animal Neutered

## g0833（1 列）
- 見出し：Animal Sex
- 例1 値：F | M | F | M | M
  - 同じ表の列：Animal Quantity, Animal Colour, Animal Date of Birth, Animal Neutered

## g0834（1 列）
- 見出し：Animal Neutered
- 例1 値：Y | N | Y | N | Y
  - 同じ表の列：Animal Quantity, Animal Colour, Animal Date of Birth, Animal Sex

## g0835（1 列）
- 見出し：Total new workplace injury claims
- 例1 値：18 | 12.50% | 16
  - 同じ表の列：Fatalities, Seriously injury wo…, Significant injurie…, Number of notifiabl…, Number of provision…, Total gross workers…, Income support paym…

## g0836（1 列）
- 見出し：Fatalities
- 例1 値：0 | 0 | 0
  - 同じ表の列：Total new workplace…, Seriously injury wo…, Significant injurie…, Number of notifiabl…, Number of provision…, Total gross workers…, Income support paym…

## g0837（1 列）
- 見出し：Seriously injury workers
- 例1 値：0 | 0 | 0
  - 同じ表の列：Total new workplace…, Fatalities, Significant injurie…, Number of notifiabl…, Number of provision…, Total gross workers…, Income support paym…

## g0838（1 列）
- 見出し：Significant injuries (where lost time exceeds a working week
- 例1 値：4.44 | -25.60% | 5.97
  - 同じ表の列：Total new workplace…, Fatalities, Seriously injury wo…, Number of notifiabl…, Number of provision…, Total gross workers…, Income support paym…

## g0839（1 列）
- 見出し：Number of notifiable incidents (WHS Act 2012, Part 3)
- 例1 値：0% | 2 | 2
  - 同じ表の列：Total new workplace…, Fatalities, Seriously injury wo…, Significant injurie…, Number of provision…, Total gross workers…, Income support paym…

## g0840（1 列）
- 見出し：Number of provisional improvement, improvement and prohibiti
- 例1 値：1 | 0% | 1
  - 同じ表の列：Total new workplace…, Fatalities, Seriously injury wo…, Significant injurie…, Number of notifiabl…, Total gross workers…, Income support paym…

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
