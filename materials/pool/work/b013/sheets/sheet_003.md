# ラベル用シート 003 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：Jurisdiction
- 例1 値：British Columbia | Quebec | Newfoundland and Labrador | Nova Scotia | Total
  - 同じ表の列：2020, 2021, 2022, 2023, 2024

## g0242（3 列）
- 見出し：2020
- 例1 値：710 | 64950 | 668450 | 107180 | 41470
  - 同じ表の列：Jurisdiction, 2021, 2022, 2023, 2024
- 例2 値：20 | 22 | 23 | 14 | 23
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2017, 2018, 2019, 2021

## g0243（3 列）
- 見出し：2021
- 例1 値：28440 | 740 | 109390 | 1556480 | 3784820
  - 同じ表の列：Jurisdiction, 2020, 2022, 2023, 2024
- 例2 値：20 | 21 | 21 | 22 | 15
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0244（3 列）
- 見出し：2022
- 例1 値：707320 | 2460 | 730 | 572420 | 3848720
  - 同じ表の列：Jurisdiction, 2020, 2021, 2023, 2024
- 例2 値：12 | 22 | 21 | 21 | 15
  - 同じ表の列：Class_Type, 2014, 2015, 2016, 2017, 2018, 2019, 2020

## g0245（3 列）
- 見出し：2023
- 例1 値：4210 | 2420 | 16420 | 1607640 | 715460
  - 同じ表の列：Jurisdiction, 2020, 2021, 2022, 2024
- 例2 値：2025 | 2024 | 2023 | 2025 | 2024
  - 同じ表の列：実数/男女計/令和5年, 382, 679, 922, 338, 1194, 329, 265

## g0246（2 列）
- 見出し：2024
- 例1 値：1550030 | 550980 | 26840 | 15950 | 499210
  - 同じ表の列：Jurisdiction, 2020, 2021, 2022, 2023
- 例2 値：37729 | 2337 | 42653 | 1936
  - 同じ表の列：Number of students, 2016, 2017, 2018, 2019, 2020, 2021, 2022

## g0247（1 列）
- 見出し：Province/Territory
- 例1 値：Northwest Territories | Nunavut | British Columbia | Manitoba | Saskatchewan
  - 同じ表の列：BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0248（1 列）
- 見出し：BADL - Vision
- 例1 値：2220 | 20 | 320 | 950 | 300
  - 同じ表の列：Province/Territory, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0249（1 列）
- 見出し：BADL - Walking
- 例1 値：78400 | 92170 | 22260 | 460 | 1420
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0250（1 列）
- 見出し：BADL - Speaking
- 例1 値：38080 | 130 | 76630 | 6260 | 4840
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0251（1 列）
- 見出し：BADL - Mental Functions
- 例1 値：116250 | 28440 | 296460 | 36960 | 570
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Hearing, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0252（1 列）
- 見出し：BADL - Hearing
- 例1 値：2660 | 8270 | 3610 | 34970 | 2720
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Feeding, BADL - Dressing, BADL - Eliminating

## g0253（1 列）
- 見出し：BADL - Feeding
- 例1 値：149420 | 4490 | 600 | 3800 | 560
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Dressing, BADL - Eliminating

## g0254（1 列）
- 見出し：BADL - Dressing
- 例1 値：12070 | 36550 | 15740 | 36070 | 1490
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Eliminating

## g0255（1 列）
- 見出し：BADL - Eliminating
- 例1 値：7520 | 5670 | 21480 | 6050 | 140
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing

## g0256（1 列）
- 見出し：BADL - Life-Sustaining Therapy
- 例1 値：1330 | 5330 | 18520 | 6910 | 5830
  - 同じ表の列：Province/Territory, BADL - Vision, BADL - Walking, BADL - Speaking, BADL - Mental Funct…, BADL - Hearing, BADL - Feeding, BADL - Dressing

## g0257（1 列）
- 見出し：FY
- 例1 値：*Information unavailable until FY 2023/… | 2022/23 | 2019/20 | 2018/19 | 2021/22
  - 同じ表の列：Quarter, # of Awarded Contra…, % of Indigenous Set…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g0258（1 列）
- 見出し：Quarter
- 例1 値：Q3 | Q1 | Q4 | Q4 | Q1
  - 同じ表の列：FY, # of Awarded Contra…, % of Indigenous Set…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g0259（1 列）
- 見出し：# of Awarded Contracts
- 例1 値：112 | 187 | 191 | 107 | 191
  - 同じ表の列：FY, Quarter, % of Indigenous Set…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g0260（1 列）
- 見出し：% of Indigenous Set-Aside*
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g0261（1 列）
- 見出し：# of Amendments Issued
- 例1 値：24 | 24 | 33 | 8 | 25
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Indigenous Set…, % of Sole Sourced F…, % of Competitive Fi…

## g0262（1 列）
- 見出し：% of Sole Sourced Files
- 例1 値：59% | 38% | 41% | 44% | 37%
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Indigenous Set…, # of Amendments Iss…, % of Competitive Fi…

## g0263（1 列）
- 見出し：% of Competitive Files
- 例1 値：52% | 65% | 76% | 65% | 57%
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Indigenous Set…, # of Amendments Iss…, % of Sole Sourced F…

## g0264（3 列）
- 見出し：departmental_identification_number
- 例1 値：OI-538 | OI-586 | OI-1115 | OI-563 | OI-501
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published
- 例2 値：OI-756 | OI-453 | OI-456 | OI-1042 | OI-1043
  - 同じ表の列：title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0265（1 列）
- 見出し：title_translated_en
- 例1 値：Message to industry – Opening of the ap… | Message to industry – Opening of the ap… | WTO: Butter, Dairy Spreads, Fats and Oi… | CUSMA: Other Dairy TRQ – Serial No. 102… | Dairy Report - Global and IREP permits …
  - 同じ表の列：departmental_identi…, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0266（1 列）
- 見出し：title_translated_fr
- 例1 値：Liste des détenteurs de contingent pour… | Sommaire de l’importation sur les conti… | OMC : CT du Beurre, pâtes à tartiner la… | PTPGP : CT des autres produits laitiers… | Liste des détenteurs de contingent pour…
  - 同じ表の列：departmental_identi…, title_translated_en, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0267（1 列）
- 見出し：notes_translated_en
- 例1 値：1.1. The purpose of this Notice is: to … | CUSMA Other Dairy Quota Holders List. | Dairy Export Thresholds | CUSMA Dairy Export Thresholds Below Thr… | WTO: Butter, Dairy Spreads, Fats and Oi…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_fr, organization_title_…, organization_title_…, subject, date_published

## g0268（1 列）
- 見出し：notes_translated_fr
- 例1 値：1.1 Le present Avis a pour objet: a. D'… | Liste des détenteurs des seuils d’expor… | OMC : CT du Beurre, pâtes à tartiner la… | Seuils d’exportation de produits laitie… | Dates clés et quantités d’exportation :…
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, organization_title_…, organization_title_…, subject, date_published

## g0269（3 列）
- 見出し：organization_title_en
- 例1 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada | Global Affairs Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0270（3 列）
- 見出し：organization_title_fr
- 例1 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published
- 例2 値：Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada | Affaires mondiales Canada
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, subject, date_published

## g0271（3 列）
- 見出し：subject
- 例1 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published
- 例2 値：economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry | economics_and_industry
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, date_published

## g0272（3 列）
- 見出し：date_published
- 例1 値：2022-01-18 | 2022-03-02 | 2022-09-07 | 2023-08-02 | 2024-07-12
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：2013-09-30 | 2014-09-30 | 2024-03-12 | 2014-09-10 | 2022-01-06
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0273（3 列）
- 見出し：portal_type
- 例1 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject
- 例2 値：Open Information | Open Information | Open Information | Open Information | Open Information
  - 同じ表の列：departmental_identi…, title_translated_en, title_translated_fr, notes_translated_en, notes_translated_fr, organization_title_…, organization_title_…, subject

## g0274（1 列）
- 見出し：FSA
- 例1 値：M1S | V8G | B4P | V8T | L4E
  - 同じ表の列：Year, Province, Number of CESG Bene…, CESG Amount ($)

## g0275（2 列）
- 見出し：Province
- 例1 値：AB | NL | ON | BC | ON
  - 同じ表の列：Year, FSA, Number of CESG Bene…, CESG Amount ($)
- 例2 値：Leinster | Leinster | Leinster | Leinster | Leinster
  - 同じ表の列：LE_ID, ENGLISH, CONTAE, COUNTY, GUID, CENTROID_X, CENTROID_Y, AREA

## g0276（1 列）
- 見出し：Number of CESG Beneficiaries
- 例1 値：2179 | 2100 | 11148 | 5267 | 2296
  - 同じ表の列：Year, FSA, Province, CESG Amount ($)

## g0277（1 列）
- 見出し：CESG Amount ($)
- 例1 値：$2,405,942 | $770,543 | $586,710 | * | $1,240,457
  - 同じ表の列：Year, FSA, Province, Number of CESG Bene…

## g0278（1 列）
- 見出し：Province/Territory
- 例1 値：Newfoundland and Labrador | Nunvavut | Saskatchewan | Nova Scotia | New Brunswick
  - 同じ表の列：1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005

## g0279（1 列）
- 見出し：1998
- 例1 値：$4.98 | $2.76 | $3.56 | $16.88 | $0.57
  - 同じ表の列：Province/Territory, 1999, 2000, 2001, 2002, 2003, 2004, 2005

## g0280（1 列）
- 見出し：1999
- 例1 値：$0.03 | $0.29 | $136.06 | $6.89 | $8.79
  - 同じ表の列：Province/Territory, 1998, 2000, 2001, 2002, 2003, 2004, 2005

## g0281（1 列）
- 見出し：2000
- 例1 値：$9.72 | $0.04 | $317.78 | $1.19 | $7.28
  - 同じ表の列：Province/Territory, 1998, 1999, 2001, 2002, 2003, 2004, 2005

## g0282（1 列）
- 見出し：2001
- 例1 値：$10.36 | $50.96 | $48.45 | $0.05 | $4.42
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2002, 2003, 2004, 2005

## g0283（1 列）
- 見出し：2002
- 例1 値：$177.03 | $4.64 | $0.05 | $43.39 | $0.35
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2001, 2003, 2004, 2005

## g0284（1 列）
- 見出し：2003
- 例1 値：$8.31 | $45.07 | $10.16 | $389.19 | $187.74
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2001, 2002, 2004, 2005

## g0285（1 列）
- 見出し：2004
- 例1 値：$0.36 | $1.35 | $10.98 | $0.39 | $64.22
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2001, 2002, 2003, 2005

## g0286（1 列）
- 見出し：2005
- 例1 値：$9.51 | $5.27 | $0.40 | $469.60 | $70.47
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2001, 2002, 2003, 2004

## g0287（1 列）
- 見出し：2006
- 例1 値：$0.08 | $1.53 | $0.44 | $13.65 | $76.67
  - 同じ表の列：Province/Territory, 1998, 1999, 2000, 2001, 2002, 2003, 2004

## g0288（1 列）
- 見出し：18+ years
- 例1 値：1404139 | 3437267 | 2148917 | 315744 | 1077809
  - 同じ表の列：Year, 0-17 years old

## g0289（1 列）
- 見出し：0-17 years old
- 例1 値：1117834 | 3164709 | 2388324 | 4079026 | 4019727
  - 同じ表の列：Year, 18+ years

## g0290（1 列）
- 見出し：index
- 例1 値：90 | 176 | 3 | 65 | 62
  - 同じ表の列：VOC Species [all co…, CAS #, Sampling environment, Count, max MDL, # samples > MDL, % samples > MDL, min

## g0291（1 列）
- 見出し：VOC Species [all concentrations in ug/m3]
- 例1 値：2_2_5_Trimethylhexane | Butylacetate | Isoprene (2_Methyl_1_3_Butadiene) | Heptane | iso_Propylbenzene
  - 同じ表の列：index, CAS #, Sampling environment, Count, max MDL, # samples > MDL, % samples > MDL, min

## g0292（1 列）
- 見出し：CAS #
- 例1 値：100-41-4 | 110-62-3 | 67-56-1 | 106-97-8 | 10/6/7642
  - 同じ表の列：index, VOC Species [all co…, Sampling environment, Count, max MDL, # samples > MDL, % samples > MDL, min

## g0293（1 列）
- 見出し：Sampling environment
- 例1 値：indoor | outdoor | outdoor | outdoor | outdoor
  - 同じ表の列：index, VOC Species [all co…, CAS #, Count, max MDL, # samples > MDL, % samples > MDL, min

## g0294（1 列）
- 見出し：Count
- 例1 値：48 | 48 | 48 | 48 | 48
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, max MDL, # samples > MDL, % samples > MDL, min

## g0295（1 列）
- 見出し：max MDL
- 例1 値：0.02 | 0 | 0.02 | 0.04 | 0
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, Count, # samples > MDL, % samples > MDL, min

## g0296（1 列）
- 見出し：# samples > MDL
- 例1 値：48 | 48 | 35 | 3 | 48
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, Count, max MDL, % samples > MDL, min

## g0297（1 列）
- 見出し：% samples > MDL
- 例1 値：77.08333333 | 100 | 100 | 100 | 100
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, Count, max MDL, # samples > MDL, min

## g0298（1 列）
- 見出し：min
- 例1 値：0.078 | 0.078 | 0.108 | 0.122 | 0.042
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, Count, max MDL, # samples > MDL, % samples > MDL

## g0299（1 列）
- 見出し：max
- 例1 値：0.676 | 0.52 | 0.304 | 3.276 | 1.3
  - 同じ表の列：index, VOC Species [all co…, CAS #, Sampling environment, Count, max MDL, # samples > MDL, % samples > MDL

## g0300（1 列）
- 見出し：Location/Emplacement
- 例1 値：Kuujjuarapik | Toronto | Point Lepreau | Montreal | Charlottetown
  - 同じ表の列：Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0301（1 列）
- 見出し：Province/Province
- 例1 値：ON | PEI | NS | MB | QC
  - 同じ表の列：Location/Emplacement, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0302（1 列）
- 見出し：Year/Annee
- 例1 値：2008 | 2008 | 2008 | 2013 | 2012
  - 同じ表の列：Location/Emplacement, Province/Province, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0303（1 列）
- 見出し：Quarter/Trimestre
- 例1 値：1 | 1 | 2 | 3 | 4
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0304（1 列）
- 見出し：TLD Monitor/Controle (uGy)
- 例1 値：268.347 | 184.26 | 215.179 | 323.822 | 214.508
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0305（1 列）
- 見出し：TLD Transit Out/Transport dehors (uGy)
- 例1 値：83.307 | 129.895 | 184.937 | 105.251 | 93.965
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Back/Tr…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0306（1 列）
- 見出し：TLD Transit Back/Transport de retour (uGy)
- 例1 値：106.271 | 116.545 | 113.31 | 87.172 | 94.751
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, OSL Monitor/Control…, OSL Transit Out/Tra…

## g0307（1 列）
- 見出し：OSL Monitor/Controle (uGy)
- 例1 値：280.456 | 297.984 | 201.578 | 184.049 | 219.106
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Transit Out/Tra…

## g0308（1 列）
- 見出し：OSL Transit Out/Transport dehors (uGy)
- 例1 値：113.935 | 113.935 | 131.464 | 113.935 | 113.935
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…

## g0309（1 列）
- 見出し：OSL Transit Back/Transport de retour (uGy)
- 例1 値：96.407 | 105.171 | 105.171 | 61.35 | 113.935
  - 同じ表の列：Location/Emplacement, Province/Province, Year/Annee, Quarter/Trimestre, TLD Monitor/Control…, TLD Transit Out/Tra…, TLD Transit Back/Tr…, OSL Monitor/Control…

## g0310（1 列）
- 見出し：Health Canada ID Number/Numero d'ID de Sante Canada
- 例1 値：40017 | 40003 | 40006 | 39990 | 40009
  - 同じ表の列：Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0311（1 列）
- 見出し：Collection Date/Date de prelevement
- 例1 値：2017-10-22 | 2017-10-22 | 2017-08-27 | 2017-08-02 | 2017-10-22
  - 同じ表の列：Health Canada ID Nu…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0312（1 列）
- 見出し：Wet Weight/Poids humide (g)
- 例1 値：76.11771667 | 63.81771667 | 124.4177167 | 269.2177167 | 77.21771667
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0313（1 列）
- 見出し：Dry Weight/Poids sec (g)
- 例1 値：13.7739 | 39.952 | 34.1573 | 38.0689 | 26.4689
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0314（1 列）
- 見出し：Count Date/Date de comptage
- 例1 値：12/12/2017 | 12/6/2017 | 12/9/2017 | 12/9/2017 | 12/15/2017
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0315（1 列）
- 見出し：Wet Cs-137 Activity/Humide Cs-137 Activite (Bq/Kg)
- 例1 値：43.34339158 | 1.560800827 | 1.287443486 | 0.873835872 | 3.72270733
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0316（1 列）
- 見出し：Wet Cs-137 Uncertainty/Humide Cs-137 Incertitude (Bq/Kg)
- 例1 値：0.268034928 | 0.183505533 | 0.12658058 | 0.269498031 | 2.427229929
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 MDC/Humi…, Wet Cs-134 Activity…

## g0317（1 列）
- 見出し：Wet Cs-137 MDC/Humide Cs-137 CMD (Bq/Kg)
- 例1 値：0.413366357 | 0.389735808 | 1.205987388 | 0.391722146 | 1.121504283
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-134 Activity…

## g0318（1 列）
- 見出し：Wet Cs-134 Activity/Humide Cs-134 Activite (Bq/Kg)
- 例1 値：ND | ND | ND | ND | ND
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…

## g0319（1 列）
- 見出し：Wet Cs-134 Uncertainty/Humide Cs-134 Incertitude (Bq/Kg)
- 例1 値：­ | ­ | ­ | ­ | ­
  - 同じ表の列：Health Canada ID Nu…, Collection Date/Dat…, Wet Weight/Poids hu…, Dry Weight/Poids se…, Count Date/Date de …, Wet Cs-137 Activity…, Wet Cs-137 Uncertai…, Wet Cs-137 MDC/Humi…

## g0320（1 列）
- 見出し：Fiscal Year
- 例1 値：2017-18 | 2021-22 | 2016-17 | 2019-20 | 2022-23
  - 同じ表の列：Date Published, Cost of procurement…, Target

## g0321（1 列）
- 見出し：Date Published
- 例1 値：20-Jul | N/A | N/A | N/A | N/A
  - 同じ表の列：Fiscal Year, Cost of procurement…, Target

## g0322（1 列）
- 見出し：Cost of procurement per each $100 of contracts awarded
- 例1 値：$1.04 | $1.14 | $1.02 | $0.93 | $0.85
  - 同じ表の列：Fiscal Year, Date Published, Target

## g0323（1 列）
- 見出し：Target
- 例1 値：$1.75 | $1.75 | $1.75 | $1.75 | $1.75
  - 同じ表の列：Fiscal Year, Date Published, Cost of procurement…

## g0324（1 列）
- 見出し：reference_number
- 例1 値：C-2022-P1-00004 | C-2022-P12-00004 | C-2022-P12-00006 | C-2022-P1-00006 | C-2021-P8-00003
  - 同じ表の列：minister, purpose_en, purpose_fr, start_date, end_date, locations_en, locations_fr, hours

## g0325（1 列）
- 見出し：minister
- 例1 値：PM | PM | MND | PM | GG
  - 同じ表の列：reference_number, purpose_en, purpose_fr, start_date, end_date, locations_en, locations_fr, hours

## g0326（1 列）
- 見出し：purpose_en
- 例1 値：Official Government Travel | Personal Travel | Official Government Travel | Official Government Travel | NATO Visit
  - 同じ表の列：reference_number, minister, purpose_fr, start_date, end_date, locations_en, locations_fr, hours

## g0327（1 列）
- 見出し：purpose_fr
- 例1 値：Service Funéraires pour l'Honorable Pre… | Voyage gouvernmental officiel | Tâche officielle du gouvernement | Voyage pour une annonce governementale | Voyage gouvernmental officiel
  - 同じ表の列：reference_number, minister, purpose_en, start_date, end_date, locations_en, locations_fr, hours

## g0328（2 列）
- 見出し：start_date
- 例1 値：2021-11-15 | 2022-04-19 | 2022-04-13 | 2021-11-04 | 2022-03-17
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, end_date, locations_en, locations_fr, hours
- 例2 値：2013-07-26 | 2016-12-13 | 2023-04-27 | 2013-04-29 | 2018-01-30
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, end_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g0329（2 列）
- 見出し：end_date
- 例1 値：2022-02-04 | 2022-03-09 | 2022-04-20 | 2022-04-01 | 2022-02-20
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, start_date, locations_en, locations_fr, hours
- 例2 値：2019-12-10 | 2016-03-22 | 2025-08-20 | 2026-08-11 | 2016-02-29
  - 同じ表の列：ref_number, disclosure_group, title_en, title_fr, start_date, vendor_2_en, vendor_2_fr, vendor_other_en

## g0330（1 列）
- 見出し：locations_en
- 例1 値：Ottawa, Canada; Vancouver, Canada; Vict… | Ottawa, Canada; Charlo, Canada | Ottawa, Canada; Brussels , Belgium; Par… | Toronto, Canada | Ottawa, Canada; Toronto, Canada
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, start_date, end_date, locations_fr, hours

## g0331（1 列）
- 見出し：locations_fr
- 例1 値：Ottawa, Canada; Toronto, Canada | Ottawa, Canada; Hamilton, Canada | Ottawa, Canada; Vancouver, Canada; Vict… | Ottawa, Canada; Toronto, Canada | Ottawa, Canada; Toronto, Canada; Vancou…
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, start_date, end_date, locations_en, hours

## g0332（1 列）
- 見出し：hours
- 例1 値：10.9 | 3.2 | 9.2 | 8.4 | 2
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, start_date, end_date, locations_en, locations_fr

## g0333（1 列）
- 見出し：passengers
- 例1 値：Adrienne Vaupshas, John Broadhead, Adam… | Ben Sparkes, Annabelle Archambault, Hel… | Helena Kojo, Nathalie Gahimbare, Annabe… | William Harvey-Blouin, Philip Proulx, A… | Ben Chin, Cecely Roy, Alex Tetrault, Ta…
  - 同じ表の列：reference_number, minister, purpose_en, purpose_fr, start_date, end_date, locations_en, locations_fr

## g0334（1 列）
- 見出し：operational_activities_kdollars
- 例1 値：63 | . | 538 | . | 53
  - 同じ表の列：year, training_kdollars, other_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, hospitality_kdollars, conference_fees_kdo…

## g0335（1 列）
- 見出し：training_kdollars
- 例1 値：1 | 549 | . | . | 6871
  - 同じ表の列：year, operational_activit…, other_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, hospitality_kdollars, conference_fees_kdo…

## g0336（1 列）
- 見出し：other_kdollars
- 例1 値：0 | 446 | . | 21 | 15
  - 同じ表の列：year, operational_activit…, training_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, hospitality_kdollars, conference_fees_kdo…

## g0337（1 列）
- 見出し：internal_governance_kdollars
- 例1 値：0 | 785.37249 | 0 | . | 308
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, non_public_servants…, public_servants_kdo…, hospitality_kdollars, conference_fees_kdo…

## g0338（1 列）
- 見出し：non_public_servants_kdollars
- 例1 値：51 | 436 | 1 | 1643 | 15930
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, internal_governance…, public_servants_kdo…, hospitality_kdollars, conference_fees_kdo…

## g0339（1 列）
- 見出し：public_servants_kdollars
- 例1 値：4198 | 1536 | 2663 | 27360 | 51926
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, internal_governance…, non_public_servants…, hospitality_kdollars, conference_fees_kdo…

## g0340（1 列）
- 見出し：hospitality_kdollars
- 例1 値：0 | 278 | 103 | 10 | 0
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, conference_fees_kdo…

## g0341（1 列）
- 見出し：conference_fees_kdollars
- 例1 値：8 | 100 | 1723.6 | 25 | 3
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, hospitality_kdollars

## g0342（1 列）
- 見出し：minister_kdollars
- 例1 値：0 | 70 | 0 | 1080.5 | 0
  - 同じ表の列：year, operational_activit…, training_kdollars, other_kdollars, internal_governance…, non_public_servants…, public_servants_kdo…, hospitality_kdollars

## g0343（1 列）
- 見出し：AIRCRAFT
- 例1 値：CGCQK | CIR | FGXO | 617 | FDOC
  - 同じ表の列：DATE, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0344（1 列）
- 見出し：DATE
- 例1 値：2019-10-14 | 2019-10-22 | 2019-10-20 | 2019-10-01 | 2019-10-08
  - 同じ表の列：AIRCRAFT, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0345（1 列）
- 見出し：REGION/OPERATING GROUP
- 例1 値：NEWFOUNDLAND | QUEBEC CITY, QC | WINNIPEG, MB | MONCTON, NB (GREEN PLAN) | OTTAWA, ON
  - 同じ表の列：AIRCRAFT, DATE, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0346（1 列）
- 見出し：CITY OF PURCHASE
- 例1 値：OTTAWA | CHARLEVOIX | OTTAWA | OTTAWA | MASSET
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0347（1 列）
- 見出し：FUEL CO.
- 例1 値：SHELL | IRVING OIL | DAUGHIN REGIONAL AIRPORT | SHELL | SHELL
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, CITY OF PURCHASE, METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0348（1 列）
- 見出し：METHOD OF PAYMENT
- 例1 値：STRAIGHT PAYMENT | PERSONAL CREDIT CARD, GAC BLOCKED BY FR… | CONTRACT | CONTRACT | STANDARD OFFER
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., TOTAL LITRES, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0349（1 列）
- 見出し：TOTAL LITRES
- 例1 値：1835.4 | 150 | 18612.6 | 647 | 315
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, PRICE/LITRE INCLUDI…, EXTENDED COST (CAD …

## g0350（1 列）
- 見出し：PRICE/LITRE INCLUDING PROVINCIAL & FEDERAL FUEL TAXES (CAD $
- 例1 値：0.952262889 | 1.223307573 | 0.934898949 | 1.55 | 0.980813559
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, EXTENDED COST (CAD …

## g0351（1 列）
- 見出し：EXTENDED COST (CAD $)
- 例1 値：464.94 | 794.42 | 5580.72 | 519.1 | 264.7
  - 同じ表の列：AIRCRAFT, DATE, REGION/OPERATING GR…, CITY OF PURCHASE, FUEL CO., METHOD OF PAYMENT, TOTAL LITRES, PRICE/LITRE INCLUDI…

## g0352（1 列）
- 見出し：Location
- 例1 値：Workshops | Air Fleet Appearance | Hazardous Waste Sheds | Air Fleet Appearance | Training Center
  - 同じ表の列：Year, Number of Spills, Volume (L)

## g0353（1 列）
- 見出し：Number of Spills
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, Location, Volume (L)

## g0354（1 列）
- 見出し：Volume (L)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, Location, Number of Spills

## g0355（1 列）
- 見出し：Aircraft
- 例1 値：Bell 206B | Bell 206B | Dash 8 | Citation 550 | King Air C90A
  - 同じ表の列：Past Labour Rate/Ho…, Year, Aircraft Flying Hou…, Direct Labour Worke…, Labour Rate/Hour

## g0356（1 列）
- 見出し：Past Labour Rate/Hour
- 例1 値：1.877 | 4.777 | 8.395 | 4.195 | 4.777
  - 同じ表の列：Aircraft, Year, Aircraft Flying Hou…, Direct Labour Worke…, Labour Rate/Hour

## g0357（1 列）
- 見出し：Aircraft Flying Hours
- 例1 値：389 | 902 | 1514 | 924 | 1298
  - 同じ表の列：Aircraft, Past Labour Rate/Ho…, Year, Direct Labour Worke…, Labour Rate/Hour

## g0358（1 列）
- 見出し：Direct Labour Worked (hours)
- 例1 値：7344.652 | 8137.84 | 3155.71 | 2027.7 | 45250.414
  - 同じ表の列：Aircraft, Past Labour Rate/Ho…, Year, Aircraft Flying Hou…, Labour Rate/Hour

## g0359（1 列）
- 見出し：Labour Rate/Hour
- 例1 値：9.869789357 | 4.547895105 | 6.088905983 | 9.829541912 | 9.44
  - 同じ表の列：Aircraft, Past Labour Rate/Ho…, Year, Aircraft Flying Hou…, Direct Labour Worke…

## g0360（3 列）
- 見出し：Region
- 例1 値：British Columbia | Saskatchewan | Western Canada | Manitoba | Alberta
  - 同じ表の列：Value of Business E…
- 例2 値：Alberta | Western Canada | British Columbia | Manitoba | Saskatchewan
  - 同じ表の列：Number of communiti…

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
```
