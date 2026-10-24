# ラベル用シート 009 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：Port of Entry
- 例1 値：Pearson T3 | Pearson T3 | Quebec City | Winnipeg | Pearson T3
  - 同じ表の列：Month, Fiscal Year, Count of Delays, Percentage Met Serv…

## g0962（1 列）
- 見出し：Fiscal Year
- 例1 値：2020-21 | 2023-24 | 2024-25 | 2022-23 | 2020-21
  - 同じ表の列：Port of Entry, Month, Count of Delays, Percentage Met Serv…

## g0963（1 列）
- 見出し：Count of Delays
- 例1 値：38 | 0 | 0 | 0 | 13
  - 同じ表の列：Port of Entry, Month, Fiscal Year, Percentage Met Serv…

## g0964（1 列）
- 見出し：Percentage Met Service Standard
- 例1 値：92.50% | 83.47% | 100.00% | 100.00% | 100.00%
  - 同じ表の列：Port of Entry, Month, Fiscal Year, Count of Delays

## g0965（1 列）
- 見出し：Technology
- 例1 値：Natural Gas Simple Cycle | Natural Gas Simple Cycle | Natural Gas Simple Cycle | Natural Gas Simple Cycle | Natural Gas Simple Cycle
  - 同じ表の列：Scenario, Province/Territory, Year, Dollar Year, Field, Value, Unit

## g0966（1 列）
- 見出し：Scenario
- 例1 値：Higher | Higher | Higher | CNZ | Lower
  - 同じ表の列：Technology, Province/Territory, Year, Dollar Year, Field, Value, Unit

## g0967（1 列）
- 見出し：Province/Territory
- 例1 値：NT | NS | NS | MB | ON
  - 同じ表の列：Technology, Scenario, Year, Dollar Year, Field, Value, Unit

## g0968（1 列）
- 見出し：Dollar Year
- 例1 値：2025 | 2025 | 2025 | 2025 | 2025
  - 同じ表の列：Technology, Scenario, Province/Territory, Year, Field, Value, Unit

## g0969（1 列）
- 見出し：Field
- 例1 値：Overnight Capital Cost | Overnight Capital Cost | Overnight Capital Cost | Overnight Capital Cost | Overnight Capital Cost
  - 同じ表の列：Technology, Scenario, Province/Territory, Year, Dollar Year, Value, Unit

## g0970（1 列）
- 見出し：Unit
- 例1 値：CAD/kW | CAD/kW | CAD/kW | CAD/kW | CAD/kW
  - 同じ表の列：Technology, Scenario, Province/Territory, Year, Dollar Year, Field, Value

## g0971（1 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：F11-10-AL-0008 | F11-10-AL-0019 | F11-10-AL-0041 | F11-10-AL-0029 | F11-10-AL-0028
  - 同じ表の列：Region - Region, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0972（1 列）
- 見出し：Region - Region
- 例1 値：ONTARIO | ONTARIO | ONTARIO | ONTARIO | ONTARIO
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0973（1 列）
- 見出し：Function
- 例1 値：Import | Domestic | Import | Import | Domestic
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0974（1 列）
- 見出し：Fonction
- 例1 値：Domestique | Domestique | Domestique | Importé | Importé
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0975（1 列）
- 見出し：Origin
- 例1 値：POLAND | EGYPT | Ukraine | UNKNOWN | Trinidad And Tobago
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origine, Product, Produit, Date Sampled - Date…

## g0976（1 列）
- 見出し：Origine
- 例1 値：Roumanie | POLOGNE | CANADA | CANADA | LIBAN
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Product, Produit, Date Sampled - Date…

## g0977（1 列）
- 見出し：Product
- 例1 値：Fruit Spread | Marmalade | Preserve - Jam/Jelly | Preserve - Jam/Jelly | Preserve - Jam/Jelly
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Produit, Date Sampled - Date…

## g0978（1 列）
- 見出し：Produit
- 例1 値：Conserve de fruits | Conserve - Autre | Tartinade de fruits | Tartinade de fruits | Tartinade de fruits
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Date Sampled - Date…

## g0979（1 列）
- 見出し：Date Sampled - Date d'echantillonage
- 例1 値：2010-12-11 | 2010-11-10 | 2010-12-11 | 2010-12-11 | 2010-12-11
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g0980（1 列）
- 見出し：Type of test
- 例1 値：SULPHITES | SULPHITES | SULPHITES | SULPHITES | SULPHITES
  - 同じ表の列：Sample No. - No. d'…, Region - Region, Function, Fonction, Origin, Origine, Product, Produit

## g0981（1 列）
- 見出し：Business Term
- 例1 値：Citizenship Effective Date | Judicial Stay | Standard Ceremony | Oath of Citizenship | Inadmissible on Grounds of Violating Hu…
  - 同じ表の列：Number, Terme operationnel, Definition Anglaise, Definition Francaise, Synonyme Anglais, Synonyme Francais

## g0982（1 列）
- 見出し：Terme operationnel
- 例1 値：Date de la cérémonie de citoyenneté | Mineurs présentant une demande en tant … | Date de débarquement | Evaluation | Décision d'autorisation
  - 同じ表の列：Number, Business Term, Definition Anglaise, Definition Francaise, Synonyme Anglais, Synonyme Francais

## g0983（1 列）
- 見出し：Definition Anglaise
- 例1 値：Many criminal charges brought against i… | To be a citizen of a country means that… | A request made to the Federal Court of … | Individuals who are members in good sta… | A judgment by the court that the accuse…
  - 同じ表の列：Number, Business Term, Terme operationnel, Definition Francaise, Synonyme Anglais, Synonyme Francais

## g0984（1 列）
- 見出し：Definition Francaise
- 例1 値：Abréviation : DDN La date à laquelle un… | Action de désistement avec le consentem… | Utilisé dans la production de rapports … | Personne qui offre une aide ou des cons… | Abréviation : IUC L’identificateur uniq…
  - 同じ表の列：Number, Business Term, Terme operationnel, Definition Anglaise, Synonyme Anglais, Synonyme Francais

## g0985（1 列）
- 見出し：Synonyme Anglais
- 例1 値：Non-Permanent Resident Time Credit | Decision Date | Finalization Effective Date
  - 同じ表の列：Number, Business Term, Terme operationnel, Definition Anglaise, Definition Francaise, Synonyme Francais

## g0986（1 列）
- 見出し：Synonyme Francais
- 例1 値：Date de l'étape finale en vigueur | Crédit de temps pour résidents non perm… | Date de la décision
  - 同じ表の列：Number, Business Term, Terme operationnel, Definition Anglaise, Definition Francaise, Synonyme Anglais

## g0987（1 列）
- 見出し：Event Number and ID
- 例1 値：CNSC-2677-07 | CNSC-1668-03 | CNSC-1196-02 | CNSC-6347-02 | CNSC-3371-01
  - 同じ表の列：Location, INES Level, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Sealed Source Categ…, Event Date

## g0988（1 列）
- 見出し：Location
- 例1 値：Ottawa, ON | Ottawa, ON | Baie-Comeau, QC | Edmonton, AB | Pickering, ON
  - 同じ表の列：Event Number and ID, INES Level, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Sealed Source Categ…, Event Date

## g0989（1 列）
- 見出し：INES Level
- 例1 値：0 | N/A | N/A | 0 | N/A
  - 同じ表の列：Event Number and ID, Location, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Sealed Source Categ…, Event Date

## g0990（1 列）
- 見出し：Radiation Device Make/ Model and Serial Number
- 例1 値：Beckman LS3801 S/N 204663 | Troxler, 3411B | Troxler 3440 S/N 17226 | Humboldt, 5001B | Ronan, SASR-C10
  - 同じ表の列：Event Number and ID, Location, INES Level, Nuclear Substance, Activity, Unit, Sealed Source Categ…, Event Date

## g0991（1 列）
- 見出し：Nuclear Substance
- 例1 値：Cs-137 | Cs-137 | Cs-137 | Cs-137 | Ra-226
  - 同じ表の列：Event Number and ID, Location, INES Level, Radiation Device Ma…, Activity, Unit, Sealed Source Categ…, Event Date

## g0992（1 列）
- 見出し：Activity
- 例1 値：16.8 | 241 | 10.6 | 1.48 | 300
  - 同じ表の列：Event Number and ID, Location, INES Level, Radiation Device Ma…, Nuclear Substance, Unit, Sealed Source Categ…, Event Date

## g0993（1 列）
- 見出し：Sealed Source Category
- 例1 値：4 | 4 | 5 | 4 | 5
  - 同じ表の列：Event Number and ID, Location, INES Level, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Event Date

## g0994（1 列）
- 見出し：Event Date
- 例1 値：10/30/2013 | 6/8/2011 | 5/9/2021 | 10/21/2014 | 6/9/2018
  - 同じ表の列：Event Number and ID, Location, INES Level, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Sealed Source Categ…

## g0995（1 列）
- 見出し：Recovery Date
- 例1 値：1/19/2022 | Not recovered | Not recovered | Not recovered | Not recovered
  - 同じ表の列：Event Number and ID, Location, INES Level, Radiation Device Ma…, Nuclear Substance, Activity, Unit, Sealed Source Categ…

## g0996（1 列）
- 見出し：Province or Territory
- 例1 値：Nova Scotia | Saskatchewan | Total | Newfoundland and Labrador | Outside Canada
  - 同じ表の列：Number of Accounts …, Fair Market Value (…, Total Contributions…, Total Withdrawals (…

## g0997（1 列）
- 見出し：Number of Accounts (#)
- 例1 値：123930 | 2030 | 220720 | 337030 | 13720
  - 同じ表の列：Province or Territo…, Fair Market Value (…, Total Contributions…, Total Withdrawals (…

## g0998（1 列）
- 見出し：Fair Market Value (FMV) ($)
- 例1 値：41553000 | 2814970000 | 967000 | 20953000 | 2184000
  - 同じ表の列：Province or Territo…, Number of Accounts …, Total Contributions…, Total Withdrawals (…

## g0999（1 列）
- 見出し：Total Contributions ($)
- 例1 値：965617000 | 23829000 | 1175184000 | 943000 | 3050574000
  - 同じ表の列：Province or Territo…, Number of Accounts …, Fair Market Value (…, Total Withdrawals (…

## g1000（1 列）
- 見出し：Total Withdrawals ($)
- 例1 値：0 | 4524000 | 1161000 | 32523000 | 5030000
  - 同じ表の列：Province or Territo…, Number of Accounts …, Fair Market Value (…, Total Contributions…

## g1001（1 列）
- 見出し：Numero
- 例1 値：118 | 133 | 586 | 163 | 436
  - 同じ表の列：MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1002（1 列）
- 見出し：MotFrancais
- 例1 値：station terrienne | caméra dans le proche infrarouge | revue critique de définition | géosynchrone | temps universel
  - 同じ表の列：Numero, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1003（1 列）
- 見出し：MotAnglais
- 例1 値：geosynchronous | Vehicle Assembly Building | radiation | camera, light & pan/tilt unit ORU | ORU temporary platform
  - 同じ表の列：Numero, MotFrancais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1004（1 列）
- 見出し：DefinitionFrancaise
- 例1 値：système de caméras de pointe qui orbite… | système américain de localisation et de… | Installation terrestre destinée à la po… | Appareil permettant de fragmenter les g… | Ensemble des sciences et techniques spa…
  - 同じ表の列：Numero, MotFrancais, MotAnglais, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1005（1 列）
- 見出し：SigleFrancais
- 例1 値：PDTS | HAE | AIAC | OT | CCM
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, DefinitionAnglaise, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1006（1 列）
- 見出し：DefinitionAnglaise
- 例1 値：A form of energy whose nature is unknow… | Component of the Special Purpose Dexter… | The act of interrogating aircrew or ast… | Component of the canadian Mobile Base S… | Component of the Special Purpose Dexter…
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, SigleAnglais, SynonymeFrancais, SynonymeAnglais

## g1007（1 列）
- 見出し：SigleAnglais
- 例1 値：CART | CSEW | PCIOG | EO | ERA
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SynonymeFrancais, SynonymeAnglais

## g1008（1 列）
- 見出し：SynonymeFrancais
- 例1 値：Base MIM | image-satellite | météore | année de lumière | équipement embarqué
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeAnglais

## g1009（1 列）
- 見出し：SynonymeAnglais
- 例1 値：MIM Base Unit | docking | to orbit, gravitate around | Mobile Base System | vernier motor
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais

## g1010（1 列）
- 見出し：AutreDefFrancais
- 例1 値：Projectile qui assure lui-même sa propu… | Ensemble cohérent de dispositions écono… | Méthode de localisation qui consiste à … | Appareil ou groupement d'appareils mett… | Existence, dans un signal, de plus d'él…
  - 同じ表の列：Numero, MotFrancais, MotAnglais, DefinitionFrancaise, SigleFrancais, DefinitionAnglaise, SigleAnglais, SynonymeFrancais

## g1011（1 列）
- 見出し：FY
- 例1 値：2025/26 | 2022/23 | 2021/22 | 2020/21 | 2024/25
  - 同じ表の列：Quarter, # of Awarded Contra…, % of Files with Ind…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g1012（1 列）
- 見出し：Quarter
- 例1 値：Q1 | Q2 | Q1 | Q3 | Q3
  - 同じ表の列：FY, # of Awarded Contra…, % of Files with Ind…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g1013（1 列）
- 見出し：# of Awarded Contracts
- 例1 値：164 | 120 | 303 | 112 | 135
  - 同じ表の列：FY, Quarter, % of Files with Ind…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g1014（1 列）
- 見出し：% of Files with Indigenous Business
- 例1 値：Data unavailable | Data unavailable | Data unavailable | Data unavailable | Data unavailable
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, # of Amendments Iss…, % of Sole Sourced F…, % of Competitive Fi…

## g1015（1 列）
- 見出し：# of Amendments Issued
- 例1 値：35 | 14 | 27 | 14 | 16
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Files with Ind…, % of Sole Sourced F…, % of Competitive Fi…

## g1016（1 列）
- 見出し：% of Sole Sourced Files
- 例1 値：48% | 62% | 51% | 44% | 35%
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Files with Ind…, # of Amendments Iss…, % of Competitive Fi…

## g1017（1 列）
- 見出し：% of Competitive Files
- 例1 値：59% | 32% | 30% | 35% | 40%
  - 同じ表の列：FY, Quarter, # of Awarded Contra…, % of Files with Ind…, # of Amendments Iss…, % of Sole Sourced F…

## g1018（1 列）
- 見出し：QID51
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：QID8, QID10, QID11, QID12, QID12_91_TEXT, QID13, QID14, QID15

## g1019（1 列）
- 見出し：QID8
- 例1 値：55+ | 45-54 | 35-44 | 18-24 | 45-54
  - 同じ表の列：QID51, QID10, QID11, QID12, QID12_91_TEXT, QID13, QID14, QID15

## g1020（1 列）
- 見出し：QID10
- 例1 値：female/woman | male/man | male/man | male/man | female/woman
  - 同じ表の列：QID51, QID8, QID11, QID12, QID12_91_TEXT, QID13, QID14, QID15

## g1021（1 列）
- 見出し：QID11
- 例1 値：11-15 years | 11-15 years | 16-20 years | 6-10 years | 11-15 years
  - 同じ表の列：QID51, QID8, QID10, QID12, QID12_91_TEXT, QID13, QID14, QID15

## g1022（1 列）
- 見出し：QID12
- 例1 値：CRA - Canada Revenue Agency | ESDC - Employment and Social Developmen… | HC - Health Canada | SSC - Shared Services Canada | ESDC - Employment and Social Developmen…
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12_91_TEXT, QID13, QID14, QID15

## g1023（1 列）
- 見出し：QID12_91_TEXT
- 例1 値：CGC | ACOA | IRCC | CFIA | ECCC
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12, QID13, QID14, QID15

## g1024（1 列）
- 見出し：QID13
- 例1 値：Newfoundland and Labrador | National Capital Region | National Capital Region | National Capital Region | National Capital Region
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12, QID12_91_TEXT, QID14, QID15

## g1025（1 列）
- 見出し：QID14
- 例1 値：data specialist | executive | policy analyst | communication advisor | manager
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12, QID12_91_TEXT, QID13, QID15

## g1026（1 列）
- 見出し：QID15
- 例1 値：Service delivery | Regulation | Service delivery | Information Management,Information Tech… | Human Resources
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12, QID12_91_TEXT, QID13, QID14

## g1027（1 列）
- 見出し：QID18
- 例1 値：I’ve heard of them, but I’m not too sur… | I’ve never heard of them | I know what they are, and can explain t… | I’ve heard of them, but I’m not too sur… | I know what they are, and can explain t…
  - 同じ表の列：QID51, QID8, QID10, QID11, QID12, QID12_91_TEXT, QID13, QID14

## g1028（1 列）
- 見出し：Contingent
- 例1 値：0 | 0 | 255 | 0 | 0
  - 同じ表の列：Maritimes, Golfe, Quebec, T.-N., TOTAL, %, Quantite restante

## g1029（1 列）
- 見出し：Maritimes
- 例1 値：0 | 0 | 0 | 0 | 32
  - 同じ表の列：Contingent, Golfe, Quebec, T.-N., TOTAL, %, Quantite restante

## g1030（1 列）
- 見出し：Golfe
- 例1 値：98 | 0 | 0 | 0 | 0
  - 同じ表の列：Contingent, Maritimes, Quebec, T.-N., TOTAL, %, Quantite restante

## g1031（1 列）
- 見出し：Quebec
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Contingent, Maritimes, Golfe, T.-N., TOTAL, %, Quantite restante

## g1032（1 列）
- 見出し：T.-N.
- 例1 値：0 | 13 | 52 | 0 | 12 422
  - 同じ表の列：Contingent, Maritimes, Golfe, Quebec, TOTAL, %, Quantite restante

## g1033（1 列）
- 見出し：TOTAL
- 例1 値：0 | 1 217 | 0 | 204 | 119
  - 同じ表の列：Contingent, Maritimes, Golfe, Quebec, T.-N., %, Quantite restante

## g1034（1 列）
- 見出し：%
- 例1 値：49% | 100% | 23% | - | -
  - 同じ表の列：Contingent, Maritimes, Golfe, Quebec, T.-N., TOTAL, Quantite restante

## g1035（1 列）
- 見出し：Quantite restante
- 例1 値：- | - | 25 | 244 | 1 288
  - 同じ表の列：Contingent, Maritimes, Golfe, Quebec, T.-N., TOTAL, %

## g1036（1 列）
- 見出し：Ref.
- 例1 値：2.8.12 | 2.1.1 | 8.7.7 | 2.5.2 | 2.5
  - 同じ表の列：Nom du service, Niveau de service c…

## g1037（1 列）
- 見出し：Nom du service
- 例1 値：Signalement d'un incident - Collaborati… | Installations de TI | Aide et information relatives au transf… | Service de maintenance de la Force aéri… | Référer un client
  - 同じ表の列：Ref., Niveau de service c…

## g1038（1 列）
- 見出し：Niveau de service cible*
- 例1 値：20 | 40 | 15 | 20 | 10
  - 同じ表の列：Ref., Nom du service

## g1039（1 列）
- 見出し：Organization
- 例1 値：Environment and Climate Change Canada | Employment and Social Development Canada | Library and Archives Canada | Canada Revenue Agency | Office of the Chief Electoral Officer
  - 同じ表の列：FSDS Goal, FSDS Target, Implementation stra…, Departmental action

## g1040（1 列）
- 見出し：FSDS Goal
- 例1 値：GOAL 14: CONSERVE AND PROTECT CANADA’S … | GOAL 13: TAKE ACTION ON CLIMATE CHANGE … | GOAL 13: TAKE ACTION ON CLIMATE CHANGE … | GOAL 4: PROMOTE KNOWLEDGE AND SKILLS FO… | GOAL 17: STRENGTHEN PARTNERSHIPS TO PRO…
  - 同じ表の列：Organization, FSDS Target, Implementation stra…, Departmental action

## g1041（1 列）
- 見出し：FSDS Target
- 例1 値：Reduce the amount of waste Canadians se… | The Government of Canada’s procurement … | The Government of Canada’s procurement … | Between 2023 and 2026, and every year o… | By 2026, increase the percentage of spe…
  - 同じ表の列：Organization, FSDS Goal, Implementation stra…, Departmental action

## g1042（1 列）
- 見出し：Implementation strategy
- 例1 値：Implement the United Nations Declaratio… | Implement the Greening Government Strat… | Reduce risks posed by climate change im… | Implement the Greening Government Strat… | Implement the Greening Government Strat…
  - 同じ表の列：Organization, FSDS Goal, FSDS Target, Departmental action

## g1043（1 列）
- 見出し：Departmental action
- 例1 値：Ensure timely processing of digital and… | Ensure that all CRCC employees involved… | Requiring proponents in all Tailored Im… | Contribute to the development of indica… | ESDC will fund projects that support Ca…
  - 同じ表の列：Organization, FSDS Goal, FSDS Target, Implementation stra…

## g1044（1 列）
- 見出し：ELECTION_E
- 例1 値：GE 41, 2011 | GE 40, 2008 | GE 40, 2008 | GE 40, 2008 | GE 38, 2004
  - 同じ表の列：YEAR, ELECTION_F, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_E, GENDER_F, AGE_GROUP_ID

## g1045（1 列）
- 見出し：ELECTION_F
- 例1 値：ÉG 41, 2011 | ÉG 40, 2008 | ÉG 40, 2008 | ÉG 41, 2011 | ÉG 39, 2006
  - 同じ表の列：YEAR, ELECTION_E, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_E, GENDER_F, AGE_GROUP_ID

## g1046（1 列）
- 見出し：PROVINCE_ID
- 例1 値：35 | 13 | 99 | 35 | 24
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_E, PROVINCE_F, GENDER_E, GENDER_F, AGE_GROUP_ID

## g1047（1 列）
- 見出し：PROVINCE_E
- 例1 値：New Brunswick | Northwest Territories | Prince Edward Island | Yukon | Manitoba
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_F, GENDER_E, GENDER_F, AGE_GROUP_ID

## g1048（1 列）
- 見出し：PROVINCE_F
- 例1 値：Alberta | Nouveau-Brunswick | Québec | Île-du-Prince-Édouard | Québec
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_E, GENDER_E, GENDER_F, AGE_GROUP_ID

## g1049（1 列）
- 見出し：GENDER_E
- 例1 値：Female | Female | All genders | All genders | Female
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_F, AGE_GROUP_ID

## g1050（1 列）
- 見出し：GENDER_F
- 例1 値：Femme | Tous les genres | Homme | Tous les genres | Tous les genres
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_E, AGE_GROUP_ID

## g1051（1 列）
- 見出し：AGE_GROUP_ID
- 例1 値：9 | 2 | 7 | 2 | 1
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_E, GENDER_F

## g1052（1 列）
- 見出し：AGE_GROUP_E
- 例1 値：75 years and over | 35 to 44 years | 75 years and over | 55 to 64 years | Not first time
  - 同じ表の列：YEAR, ELECTION_E, ELECTION_F, PROVINCE_ID, PROVINCE_E, PROVINCE_F, GENDER_E, GENDER_F

## g1053（1 列）
- 見出し：Mois
- 例1 値：2025-07-01 | 2025-10-01 | 2025-06-01 | 2025-09-01 | 2025-10-01
  - 同じ表の列：Province/Territoire, Taux base sur l'age, Genre, SV #, SRG #, SV $, SRG $

## g1054（1 列）
- 見出し：Province/Territoire
- 例1 値：Nouveau-Brunswick | Terre-Neuve-et-Labrador | Alberta | Manitoba | Nunavut
  - 同じ表の列：Mois, Taux base sur l'age, Genre, SV #, SRG #, SV $, SRG $

## g1055（1 列）
- 見出し：Taux base sur l'age
- 例1 値：65 - 74 | Inconnu | 65 - 74 | 65 - 74 | Inconnu
  - 同じ表の列：Mois, Province/Territoire, Genre, SV #, SRG #, SV $, SRG $

## g1056（1 列）
- 見出し：Genre
- 例1 値：Femme | Homme | Femme | Homme | Homme
  - 同じ表の列：Mois, Province/Territoire, Taux base sur l'age, SV #, SRG #, SV $, SRG $

## g1057（1 列）
- 見出し：SV #
- 例1 値：0 | 0 | 0 | 7060 | 0
  - 同じ表の列：Mois, Province/Territoire, Taux base sur l'age, Genre, SRG #, SV $, SRG $

## g1058（1 列）
- 見出し：SRG #
- 例1 値：4040 | 0 | 0 | 10 | 274400
  - 同じ表の列：Mois, Province/Territoire, Taux base sur l'age, Genre, SV #, SV $, SRG $

## g1059（1 列）
- 見出し：SV $
- 例1 値：925000 | 40270000 | 0 | 3977000 | 0
  - 同じ表の列：Mois, Province/Territoire, Taux base sur l'age, Genre, SV #, SRG #, SRG $

## g1060（1 列）
- 見出し：SRG $
- 例1 値：0 | 24000 | 232000 | 8237000 | 6629000
  - 同じ表の列：Mois, Province/Territoire, Taux base sur l'age, Genre, SV #, SRG #, SV $

## g1061（1 列）
- 見出し：MEASURE
- 例1 値：Small Businesses Air Quality Improvemen… | Capital loss carry-overs | Deferral of income from destruction of … | Non-capital loss carry-overs | Rebate for qualifying non-profit organi…
  - 同じ表の列：GROUP, SUBJECT, CATEGORY, TAX, DETAILS, 2020, 2021, 2022

## g1062（1 列）
- 見出し：GROUP
- 例1 値：Refundable tax credit classified as tra… | Tax expenditure | Tax expenditure | Tax expenditure | Tax expenditure
  - 同じ表の列：MEASURE, SUBJECT, CATEGORY, TAX, DETAILS, 2020, 2021, 2022

## g1063（1 列）
- 見出し：SUBJECT
- 例1 値：Donations, gifts, charities, and non-pr… | Business - natural resources | Donations, gifts, charities, and non-pr… | Business - natural resources | Health
  - 同じ表の列：MEASURE, GROUP, CATEGORY, TAX, DETAILS, 2020, 2021, 2022

## g1064（1 列）
- 見出し：CATEGORY
- 例1 値：Non-structural | Non-structural | Non-structural | Non-structural | Non-structural
  - 同じ表の列：MEASURE, GROUP, SUBJECT, TAX, DETAILS, 2020, 2021, 2022

## g1065（1 列）
- 見出し：TAX
- 例1 値：CIT | PIT | PIT | PIT/TRU | GST
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, DETAILS, 2020, 2021, 2022

## g1066（1 列）
- 見出し：DETAILS
- 例1 値：Cultural property | Corporate income tax | Credit for employee-paid premiums | Personal income tax | Goods and Services Tax
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, TAX, 2020, 2021, 2022

## g1067（1 列）
- 見出し：2021
- 例1 値：13,860 | 29,155 | 3 | 15 | -2
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, TAX, DETAILS, 2020, 2022

## g1068（1 列）
- 見出し：2022
- 例1 値：6,290 | – | 34,545 | n.a. | 10
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, TAX, DETAILS, 2020, 2021

## g1069（1 列）
- 見出し：2023
- 例1 値：S | 1,220 | 925 | 2,480 | 30
  - 同じ表の列：MEASURE, GROUP, SUBJECT, CATEGORY, TAX, DETAILS, 2020, 2021

## g1070（1 列）
- 見出し：Year_month
- 例1 値：20-Aug | 20-Oct | 22-Nov | 24-Aug | 23-Jun
  - 同じ表の列：CAN_Total_active_ r…, AB, BC, MB, NB, NL, NT, NS

## g1071（1 列）
- 見出し：CAN_Total_active_ registrations_with_LH
- 例1 値：161650 | 232213 | 163039 | 193519 | 156427
  - 同じ表の列：Year_month, AB, BC, MB, NB, NL, NT, NS

## g1072（1 列）
- 見出し：AB
- 例1 値：21223 | 73555 | 26165 | 66676 | 25685
  - 同じ表の列：Year_month, CAN_Total_active_ r…, BC, MB, NB, NL, NT, NS

## g1073（1 列）
- 見出し：BC
- 例1 値：17905 | 15639 | 9333 | 12480 | 11715
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, MB, NB, NL, NT, NS

## g1074（1 列）
- 見出し：MB
- 例1 値：15855 | 5462 | 5391 | 4917 | 15746
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, NB, NL, NT, NS

## g1075（1 列）
- 見出し：NB
- 例1 値：7575 | 7213 | 8662 | 7635 | 7414
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, MB, NL, NT, NS

## g1076（1 列）
- 見出し：NL
- 例1 値：4477 | 4704 | 5697 | 4443 | 4450
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, MB, NB, NT, NS

## g1077（1 列）
- 見出し：NT
- 例1 値：81 | 75 | 185 | 95 | 86
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, MB, NB, NL, NS

## g1078（1 列）
- 見出し：NS
- 例1 値：15069 | 11483 | 11081 | 13993 | 11881
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, MB, NB, NL, NT

## g1079（1 列）
- 見出し：NU
- 例1 値：62 | 101 | 73 | 27 | 89
  - 同じ表の列：Year_month, CAN_Total_active_ r…, AB, BC, MB, NB, NL, NT

## g1080（1 列）
- 見出し：Project_ID
- 例1 値：40588 | 44264 | 47376 | 47 | 9575
  - 同じ表の列：Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

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
