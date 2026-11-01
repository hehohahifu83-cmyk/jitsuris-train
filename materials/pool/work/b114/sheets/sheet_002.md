# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Source Language
- 例1 値：English | English | English | English | English
  - 同じ表の列：Session, Format, Format_2, Langue d’origine, Priority, Priorité, Region of Session (…, Région de la séance…

## g0122（1 列）
- 見出し：Langue d’origine
- 例1 値：Anglais | Anglais | Anglais | Anglais | Anglais
  - 同じ表の列：Session, Format, Format_2, Source Language, Priority, Priorité, Region of Session (…, Région de la séance…

## g0123（1 列）
- 見出し：Priority
- 例1 値：Employment | Employment | Health and Wellness | Health and Wellness | Employment
  - 同じ表の列：Session, Format, Format_2, Source Language, Langue d’origine, Priorité, Region of Session (…, Région de la séance…

## g0124（1 列）
- 見出し：Priorité
- 例1 値：Emploi | Emploi | Emploi | Emploi | Santé et bien-être
  - 同じ表の列：Session, Format, Format_2, Source Language, Langue d’origine, Priority, Region of Session (…, Région de la séance…

## g0125（1 列）
- 見出し：Region of Session (if available)
- 例1 値：Ontario | National | n.a. | Ontario | National
  - 同じ表の列：Session, Format, Format_2, Source Language, Langue d’origine, Priority, Priorité, Région de la séance…

## g0126（1 列）
- 見出し：Région de la séance (si disponible)
- 例1 値：Ontario | National | Nouveau-Brunswick | s.o. | National
  - 同じ表の列：Session, Format, Format_2, Source Language, Langue d’origine, Priority, Priorité, Region of Session (…

## g0127（1 列）
- 見出し：Population Centre (if available)
- 例1 値：Urban | n.a. | Urban | Urban | n.a.
  - 同じ表の列：Session, Format, Format_2, Source Language, Langue d’origine, Priority, Priorité, Region of Session (…

## g0128（1 列）
- 見出し：Year Data Reported Publicly*
- 例1 値：(Year of DPR) | 2017-2018 | 2018-2019 | *Results reported are from previous fis… | 2016-2017
  - 同じ表の列：Youth enhance their…

## g0129（1 列）
- 見出し：Youth enhance their appreciation of the diversity and shared
- 例1 値：87 | 87 | Percentage of participants in the Excha… | 85
  - 同じ表の列：Year Data Reported …

## g0130（1 列）
- 見出し：Year Data Reported Publicly*
- 例1 値：(Year of DPR) | This indicator was developed and came i… | 2016-2017 | 2018-2019 | * Results reported are from previous fi…
  - 同じ表の列：Number of performer…

## g0131（1 列）
- 見出し：Number of performers and volunteers
- 例1 値：190,855 | (Number of performers and volunteers in… | N/A | N/A
  - 同じ表の列：Year Data Reported …

## g0132（1 列）
- 見出し：unique_id
- 例1 値：724 | 926 | 985 | 55 | 410
  - 同じ表の列：mode, prov, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1C, QKNOW1D

## g0133（1 列）
- 見出し：mode
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：unique_id, prov, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1C, QKNOW1D

## g0134（1 列）
- 見出し：prov
- 例1 値：6 | 3 | 3 | 6 | 6
  - 同じ表の列：unique_id, mode, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1C, QKNOW1D

## g0135（1 列）
- 見出し：QGENDR
- 例1 値：2 | 2 | 2 | 1 | 2
  - 同じ表の列：unique_id, mode, prov, age, QKNOW1A, QKNOW1B, QKNOW1C, QKNOW1D

## g0136（1 列）
- 見出し：age
- 例1 値：6 | 4 | 4 | 4 | 5
  - 同じ表の列：unique_id, mode, prov, QGENDR, QKNOW1A, QKNOW1B, QKNOW1C, QKNOW1D

## g0137（1 列）
- 見出し：QKNOW1A
- 例1 値：5 | 2 | 5 | 5 | 3
  - 同じ表の列：unique_id, mode, prov, QGENDR, age, QKNOW1B, QKNOW1C, QKNOW1D

## g0138（1 列）
- 見出し：QKNOW1B
- 例1 値：3 | 3 | 2 | 3 | 5
  - 同じ表の列：unique_id, mode, prov, QGENDR, age, QKNOW1A, QKNOW1C, QKNOW1D

## g0139（1 列）
- 見出し：QKNOW1C
- 例1 値：3 | 4 | 5 | 5 | 1
  - 同じ表の列：unique_id, mode, prov, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1D

## g0140（1 列）
- 見出し：QKNOW1D
- 例1 値：4 | 4 | 3 | 3 | 3
  - 同じ表の列：unique_id, mode, prov, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1C

## g0141（1 列）
- 見出し：HRISKA
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：unique_id, mode, prov, QGENDR, age, QKNOW1A, QKNOW1B, QKNOW1C

## g0142（1 列）
- 見出し：disease
- 例1 値：Amoebiasis | Amoebiasis | Amoebiasis | Amoebiasis | Amoebiasis
  - 同じ表の列：age-group, sex, year, number-of-reported-…, rate-per-100000

## g0143（1 列）
- 見出し：age-group
- 例1 値：All | 14-Oct | 30-39 | All | 15-19
  - 同じ表の列：disease, sex, year, number-of-reported-…, rate-per-100000

## g0144（1 列）
- 見出し：sex
- 例1 値：Female | Female | Male | Male | Unknown
  - 同じ表の列：disease, age-group, year, number-of-reported-…, rate-per-100000

## g0145（1 列）
- 見出し：year
- 例1 値：2005 | 1995 | 1997 | 2006 | 1991
  - 同じ表の列：disease, age-group, sex, number-of-reported-…, rate-per-100000

## g0146（1 列）
- 見出し：number-of-reported-cases
- 例1 値：453 | N/A | 31 | N/A | N/A
  - 同じ表の列：disease, age-group, sex, year, rate-per-100000

## g0147（1 列）
- 見出し：rate-per-100000
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：disease, age-group, sex, year, number-of-reported-…

## g0148（1 列）
- 見出し：Characteristic
- 例1 値：Total diagnoses | Year of diagnosis, 2006 | Ethnicity, Other/Mixed Ethnicity | Sex, Male | Region, Québec
  - 同じ表の列：Number of Diagnoses, Percent (%)

## g0149（1 列）
- 見出し：Number of Diagnoses
- 例1 値：530 | 820 | 60 | 1845 | 1420
  - 同じ表の列：Characteristic, Percent (%)

## g0150（1 列）
- 見出し：Percent (%)
- 例1 値：7 | 1.9 | 17.3 | 45.2 | 2.8
  - 同じ表の列：Characteristic, Number of Diagnoses

## g0151（1 列）
- 見出し：Lvl1-code-FRA_Code-CRF-niv1
- 例1 値：1 | 1 | 2 | 5 | 4
  - 同じ表の列：Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0152（1 列）
- 見出し：Lvl2-code-FRA_Code-CRF-niv2
- 例1 値：16 | 11 | 52 | 51 | 13
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0153（1 列）
- 見出し：Lvl3-code-FRA_Code-CRF-niv3
- 例1 値：112 | 233 | 166 | 312 | 226
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0154（1 列）
- 見出し：Lvl3-desc-FRA_Desc-CRF-niv3_eng
- 例1 値：Accounting requirements for capitalized… | Other Employee Future Benefits are earn… | Accounting requirements for capitalized… | Accounting requirements for capitalized… | Other Employee Future Benefits are earn…
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0155（1 列）
- 見出し：Lvl3-desc-FRA_Desc-CRF-niv3_fra
- 例1 値：Les besoins comptables liés à l'intérêt… | Les besoins comptables liés à l'intérêt… | Les autres avantages sociaux futurs son… | Les autres avantages sociaux futurs son… | Les besoins comptables liés à l'intérêt…
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0156（1 列）
- 見出し：Lvl4-code-FRA_Code-CRF-niv4
- 例1 値：2335 | 2331 | 4213 | 1312 | 1211
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0157（1 列）
- 見出し：Lvl4-desc-FRA_Desc-CRF-niv4_eng
- 例1 値：Post-employment benefits are expected t… | The accounts in this category would inc… | The accounts in this category would inc… | The accounts in this category would inc… | Other Retirement Benefits are benefits,…
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0158（1 列）
- 見出し：Lvl4-desc-FRA_Desc-CRF-niv4_fra
- 例1 値：Les avantages postérieurs à l'emploi co… | Les avantages postérieurs à l'emploi co… | Les autres avantages de retraite sont l… | Les comptes de cette catégorie inclurai… | Les comptes de cette catégorie inclurai…
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl5-code-FRA_Code-…

## g0159（1 列）
- 見出し：Lvl5-code-FRA_Code-CRF-niv5
- 例1 値：42535 | 41134 | 24311 | 21221 | 21152
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…

## g0160（1 列）
- 見出し：Notes_eng
- 例1 値：Accounting requirements to be done by d… | Assets under construction will be recor… | Last digit in the account numbers ident… | Last digit in the account numbers ident… | The breakdown for accumulated amortizat…
  - 同じ表の列：Lvl1-code-FRA_Code-…, Lvl2-code-FRA_Code-…, Lvl3-code-FRA_Code-…, Lvl3-desc-FRA_Desc-…, Lvl3-desc-FRA_Desc-…, Lvl4-code-FRA_Code-…, Lvl4-desc-FRA_Desc-…, Lvl4-desc-FRA_Desc-…

## g0161（1 列）
- 見出し：Quarter_Trimestre_eng
- 例1 値：Q1 | Q1 | Q1 | Q1 | Q1
  - 同じ表の列：Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0162（1 列）
- 見出し：Quarter_Trimestre_fra
- 例1 値：T1 | T1 | T1 | T1 | T1
  - 同じ表の列：Quarter_Trimestre_e…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0163（1 列）
- 見出し：Contracting-vehicle_Instrument-de-contrat_eng
- 例1 値：Supply arrangement | Supply arrangement | Supply arrangement | Supply arrangement | Supply arrangement
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0164（1 列）
- 見出し：Contracting-vehicle_Instrument-de-contrat_fra
- 例1 値：Arrangement en matière d'approvisionnem… | Arrangement en matière d'approvisionnem… | Arrangement en matière d'approvisionnem… | Arrangement en matière d'approvisionnem… | Arrangement en matière d'approvisionnem…
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0165（1 列）
- 見出し：Type-of-contracting-vehicle_Type-de-vehicule_eng
- 例1 値：Task | Task | Task | Task | Task
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0166（1 列）
- 見出し：Type-of-contracting-vehicle_Type-de-vehicule_fra
- 例1 値：Tâches | Tâches | Tâches | Tâches | Tâches
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…, Method-of-supply_Me…

## g0167（1 列）
- 見出し：Reporting-period_Periode-de-rapporte_eng
- 例1 値：April 1 to June 30, 2026 | April 1 to June 30, 2026 | April 1 to June 30, 2026 | April 1 to June 30, 2026 | April 1 to June 30, 2026
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Method-of-supply_Me…

## g0168（1 列）
- 見出し：Reporting-period_Periode-de-rapporte_fra
- 例1 値：1 avril au 30 juin 2026 | 1 avril au 30 juin 2026 | 1 avril au 30 juin 2026 | 1 avril au 30 juin 2026 | 1 avril au 30 juin 2026
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Method-of-supply_Me…

## g0169（1 列）
- 見出し：Method-of-supply_Methode-approvisionnement_eng
- 例1 値：Task and Solutions Professional Service… | Temporary Help Services for the Nationa… | ProServices | Task and Solutions Professional Service… | Temporary Help Services for the Nationa…
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…

## g0170（1 列）
- 見出し：Method-of-supply_Methode-approvisionnement_fra
- 例1 値：Services professionnels en informatique… | ProServices | Services professionnels centrés sur les… | Les services d'aide temporaire pour la … | ProServices
  - 同じ表の列：Quarter_Trimestre_e…, Quarter_Trimestre_f…, Contracting-vehicle…, Contracting-vehicle…, Type-of-contracting…, Type-of-contracting…, Reporting-period_Pe…, Reporting-period_Pe…

## g0171（1 列）
- 見出し：Structure Id
- 例1 値：736 | 2739 | 4038 | 33 | 1128
  - 同じ表の列：DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type, Structure Type_2

## g0172（1 列）
- 見出し：DFRP Structure Number
- 例1 値：113925 | 112101 | 112780 | 112187 | 113896
  - 同じ表の列：Structure Id, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type, Structure Type_2

## g0173（1 列）
- 見出し：TC Identifier
- 例1 値：107 | LK4-11 | LK5-8 | LK6-16 | 95
  - 同じ表の列：Structure Id, DFRP Structure Numb…, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type, Structure Type_2

## g0174（1 列）
- 見出し：DFRP Reportable
- 例1 値：1 | 0 | 1 | 1 | 0
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, Structure Status, Structure Status_2, Structure Status (f…, Structure Type, Structure Type_2

## g0175（1 列）
- 見出し：Structure Status
- 例1 値：ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status_2, Structure Status (f…, Structure Type, Structure Type_2

## g0176（1 列）
- 見出し：Structure Status_2
- 例1 値：Active | Active | Active | Active | Active
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status (f…, Structure Type, Structure Type_2

## g0177（1 列）
- 見出し：Structure Status (fr)
- 例1 値：Actif | Actif | Actif | Actif | Actif
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Type, Structure Type_2

## g0178（1 列）
- 見出し：Structure Type
- 例1 値：BLDG | BLDG | BRKWTR | BLDG | WARF
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type_2

## g0179（1 列）
- 見出し：Structure Type_2
- 例1 値：Building | Building | Parking Lot | Bridge | Building
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type

## g0180（1 列）
- 見出し：Structure Type (fr)
- 例1 値：Bâtiments | Bâtiments | Pont | Bâtiments | Bâtiments
  - 同じ表の列：Structure Id, DFRP Structure Numb…, TC Identifier, DFRP Reportable, Structure Status, Structure Status_2, Structure Status (f…, Structure Type

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
```
