# ラベル用シート 003 / 003

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（2 列）
- 見出し：Fiscal Period
- 例1 値：8 | 12 | 8 | 7 | 9
  - 同じ表の列：Fiscal Year, Month, Information Date, Value, Data Source, Comments, Metric Type
- 例2 値：9 | 10 | 6 | 7 | 8
  - 同じ表の列：Fiscal Year, Month, Information Date, Branch, Service, SSC Client, Value, Metric Type

## g0242（2 列）
- 見出し：Month
- 例1 値：November | January | November | November | February
  - 同じ表の列：Fiscal Year, Fiscal Period, Information Date, Value, Data Source, Comments, Metric Type
- 例2 値：November | June | March | June | June
  - 同じ表の列：Fiscal Year, Fiscal Period, Information Date, Branch, Service, SSC Client, Value, Metric Type

## g0243（1 列）
- 見出し：Information Date
- 例1 値：2019-11-30 | 2020-01-31 | 2019-11-30 | 2020-01-31 | 2020-03-31
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Value, Data Source, Comments, Metric Type

## g0244（1 列）
- 見出し：Value
- 例1 値：0 | 0 | 0 | 16,374 | 0
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Data Source, Comments, Metric Type

## g0245（1 列）
- 見出し：Data Source
- 例1 値：Bell/SSC | Bell/SSC | SSC | Bell/SSC | Bell/SSC
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Value, Comments, Metric Type

## g0246（1 列）
- 見出し：Comments
- 例1 値：= or <7 Hourly Failures - Échecs Horair… | High or Critical Incidents - Incidents … | 99.90% | 0 exceptions | 30 FGWD - JOGF
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Value, Data Source, Metric Type

## g0247（1 列）
- 見出し：Metric Type
- 例1 値：Monthly - Mensuel | Monthly - Mensuel | Monthly - Mensuel | Monthly - Mensuel | Monthly - Mensuel
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Value, Data Source, Comments

## g0248（1 列）
- 見出し：Information Date
- 例1 値：1/31/2018 | 8/31/2022 | 2/28/2018 | 2/28/2022 | 10/31/2021
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Branch, Service, SSC Client, Value, Metric Type

## g0249（1 列）
- 見出し：Branch
- 例1 値：Data Centre Services | Data Centre Services | Data Centre Services | Data Centre Services | Data Centre Services
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Service, SSC Client, Value, Metric Type

## g0250（1 列）
- 見出し：Service
- 例1 値：Data Centre Facilities - Enterprise | Data Centre Facilities - Enterprise | Data Centre Facilities - Enterprise | Data Centre Facilities - Enterprise | Data Centre Facilities - Enterprise
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, SSC Client, Value, Metric Type

## g0251（1 列）
- 見出し：SSC Client
- 例1 値：EDC Barrie | EDC Gatineau | EDC Barrie | EDC Borden | EDC Borden
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Value, Metric Type

## g0252（1 列）
- 見出し：Metric Type
- 例1 値：Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value

## g0253（1 列）
- 見出し：reference_number
- 例1 値：IRCC-2019-PR-00002 | IRCC-2019-PR-00001 | NRCan-2019-OEE-00001 | IRCC-2019-CSC-00002 | IRCC-2019-CSC-00003
  - 同じ表の列：titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area, research_design

## g0254（1 列）
- 見出し：titre_du_projet_en
- 例1 値：Increasing Executive Self Identificatio… | test_pbi_01 | Nudging Homeowners Towards a Home Energ… | Post-Incorporation Services Package | Channel shifting: Changing the default …
  - 同じ表の列：reference_number, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area, research_design

## g0255（1 列）
- 見出し：titre_du_projet_fr
- 例1 値：Messages proactifs pour augmenter les m… | Changement de canal : L'impact de la pr… | Changement de canal : Changement du can… | Trousse de services post-incorporation | L'étiquette Énerguide pour les maisons
  - 同じ表の列：reference_number, titre_du_projet_en, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area, research_design

## g0256（1 列）
- 見出し：question_de_recherche_en
- 例1 値：Will the use of nudges and improved vis… | Can we influence the channel through wh… | test_pbi_01 | Can we shift clients to submit an enqui… | Does an e-mail reminder increase the li…
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area, research_design

## g0257（1 列）
- 見出し：question_de_recherche_fr
- 例1 値：L'utilisation de nudges et d'une concep… | Can we influence the channel through wh… | Les modifications apportées aux message… | Les améliorations apportées à la page d… | Un rappel par courriel augmente-t-il la…
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area, research_design

## g0258（1 列）
- 見出し：project_summary_en
- 例1 値：Natural Resources Canada’s EnerGuide la… | This experiment entailed a live, random… | The Immigration, Refugees, and Citzensh… | The Office of the Chief Human Resources… | This experiment was a quasi Randomized …
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_fr, experimental_area, research_design

## g0259（1 列）
- 見出し：project_summary_fr
- 例1 値：Ressources naturelles Canada délivre de… | Les nouveaux résidents permanents doive… | Le Centre de soutien aux clients (CSC) … | Le Centre de soutien aux clients (CSC) … | L’étiquette ÉnerGuide de Ressources nat…
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, experimental_area, research_design

## g0260（1 列）
- 見出し：experimental_area
- 例1 値：PO | SI | PR | SE | SE
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, research_design

## g0261（1 列）
- 見出し：research_design
- 例1 値：RDM | QEX | STR | RDM | RDM
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area

## g0262（1 列）
- 見出し：design_details_en
- 例1 値：The experiment was a randomized A/B tes… | We examined the impact of sending clien… | The Carrot Rewards mobile application w… | test_pbi_01 | The experiment was a randomized A/B tes…
  - 同じ表の列：reference_number, titre_du_projet_en, titre_du_projet_fr, question_de_recherc…, question_de_recherc…, project_summary_en, project_summary_fr, experimental_area

## g0263（1 列）
- 見出し：reporting_period
- 例1 値：P02 | P01 | P01 | P01 | P02
  - 同じ表の列：year

## g0264（1 列）
- 見出し：tracking_number
- 例1 値：257115 | 25-SAS-312 | 251796 | 257730 | 252886
  - 同じ表の列：title_en, title_fr, originating_sector_…, originating_sector_…, date_received, action_required, additional_informat…, additional_informat…

## g0265（1 列）
- 見出し：title_en
- 例1 値：ATSSC’s 2026–27 Departmental Plan | INFORMATION ON AUSTRALIA WINE DISPUTE N… | SCENARIO NOTE - DM FORBES ATTENDING MEE… | TATC - IT Equipment Request - Internati… | APPROVAL SOUGHT FOR AGRICULTURE AND AGR…
  - 同じ表の列：tracking_number, title_fr, originating_sector_…, originating_sector_…, date_received, action_required, additional_informat…, additional_informat…

## g0266（1 列）
- 見出し：title_fr
- 例1 値：OPTIONS D'AAC POUR MIEUX FAIRE CONNAÎTR… | DEMANDE D'APPROBATION DE L'ENTENTE DE C… | NOTE DE SCÉNARIO - RÉUNION DU SM FORBES… | NOTE DE SCÉNARIO – TABLE RONDE DE LA MI… | DEMANDE D’APPROBATION DE LA DEMANDE DE …
  - 同じ表の列：tracking_number, title_en, originating_sector_…, originating_sector_…, date_received, action_required, additional_informat…, additional_informat…

## g0267（1 列）
- 見出し：originating_sector_en
- 例1 値：IAB | Procurement | SPB | ISB | PB
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, date_received, action_required, additional_informat…, additional_informat…

## g0268（1 列）
- 見出し：originating_sector_fr
- 例1 値：DGSIM | Voyage | DGPS | Finance | DGGI
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, date_received, action_required, additional_informat…, additional_informat…

## g0269（1 列）
- 見出し：date_received
- 例1 値：2024-01-26 | 2020-05-01 | 2022-03-02 | 2021-02-03 | 2021-06-08
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, originating_sector_…, action_required, additional_informat…, additional_informat…

## g0270（1 列）
- 見出し：action_required
- 例1 値：S | I | D | I | I
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, originating_sector_…, date_received, additional_informat…, additional_informat…

## g0271（1 列）
- 見出し：additional_information_en
- 例1 値：BN# requested by Quinn R. | Minister of Diversity, Inclusion and Pe… | PROTECTED B | BN# requested by Chris C. (Nov 14) | BN# requested by Valerie P. (Oct16)
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, originating_sector_…, date_received, action_required, additional_informat…

## g0272（1 列）
- 見出し：additional_information_fr
- 例1 値：Ministre de l'Emploi, du Développement … | Ministre de la Diversité, de l'Inclusio… | Signed version received | Ministre de l'Emploi, du Développement … | Signed version received
  - 同じ表の列：tracking_number, title_en, title_fr, originating_sector_…, originating_sector_…, date_received, action_required, additional_informat…

## g0273（1 列）
- 見出し：Audit Area
- 例1 値：Hazardous Waste Stations | Hazardous Waste Stations | Hazardous Waste Stations | Hazardous Waste Stations | Hazardous Waste Stations
  - 同じ表の列：Date, Point of Inspection, Compliance Yes/No (…, Comments

## g0274（1 列）
- 見出し：Point of Inspection
- 例1 値：Workshop | Workshop | Hangar (by AFA) | Hangar (by Engine Repair) | Hangar (by Engine Repair)
  - 同じ表の列：Date, Audit Area, Compliance Yes/No (…, Comments

## g0275（1 列）
- 見出し：Compliance Yes/No (1/0)
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Date, Audit Area, Point of Inspection, Comments

## g0276（1 列）
- 見出し：Comments
- 例1 値：Two metal oil cans in plastic oil can d… | Paper in absorbants disposal | Gloves in in absorbants disposal
  - 同じ表の列：Date, Audit Area, Point of Inspection, Compliance Yes/No (…

## g0277（1 列）
- 見出し：New/Used
- 例1 値：Used | New | Used | Used | New
  - 同じ表の列：Date, Hazard Class, Quantity, Amount per Container

## g0278（1 列）
- 見出し：Hazard Class
- 例1 値：Flammable | Toxic | Flammable | Flammable | Flammable
  - 同じ表の列：Date, New/Used, Quantity, Amount per Container

## g0279（1 列）
- 見出し：Quantity
- 例1 値：1 | 3 | 1 | 1 | 2
  - 同じ表の列：Date, New/Used, Hazard Class, Amount per Container

## g0280（1 列）
- 見出し：Amount per Container
- 例1 値：946 mL | 0.79 mL | 50 mL | 52 mL remaining | Unknown
  - 同じ表の列：Date, New/Used, Hazard Class, Quantity

## g0281（1 列）
- 見出し：Rank
- 例1 値：663 | 554 | 659 | 679 | 339
  - 同じ表の列：TC Number, Railway Company, Region, Province, Access, Jurisdiction, Mile, Subdivision

## g0282（1 列）
- 見出し：TC Number
- 例1 値：10200 | 4857 | 405157 | 7963 | 17162
  - 同じ表の列：Rank, Railway Company, Region, Province, Access, Jurisdiction, Mile, Subdivision

## g0283（1 列）
- 見出し：Railway Company
- 例1 値：Canadian National Railway | GO Transit | Canadian Pacific Railway | Canadian Pacific Railway | Canadian Pacific Railway
  - 同じ表の列：Rank, TC Number, Region, Province, Access, Jurisdiction, Mile, Subdivision

## g0284（1 列）
- 見出し：Region
- 例1 値：PAC | PNR | ONT | ONT | ONT
  - 同じ表の列：Rank, TC Number, Railway Company, Province, Access, Jurisdiction, Mile, Subdivision

## g0285（1 列）
- 見出し：Access
- 例1 値：Public | Public | Public | Public | Public
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Province, Jurisdiction, Mile, Subdivision

## g0286（1 列）
- 見出し：Jurisdiction
- 例1 値：F | F | F | F | F
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Province, Access, Mile, Subdivision

## g0287（1 列）
- 見出し：Mile
- 例1 値：103.05 | 22.73 | 57.13 | 196.66 | 12.2
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Province, Access, Jurisdiction, Subdivision

## g0288（1 列）
- 見出し：Subdivision
- 例1 値：Belleville | Blackfoot | Cascade | Victoria - SRY | Slave Lake
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Province, Access, Jurisdiction, Mile

## g0289（1 列）
- 見出し：Spur Mile Point
- 例1 値：- | - | 0.42 | - | -
  - 同じ表の列：Rank, TC Number, Railway Company, Region, Province, Access, Jurisdiction, Mile

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
```
