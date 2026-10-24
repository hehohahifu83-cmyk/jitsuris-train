# ラベル用シート 010 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_010.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1081（1 列）
- 見出し：Environmental_Assessment_Type
- 例1 値：Screening | Screening using a class screening report | Screening using a class screening report | Screening | Screening using a class screening report
  - 同じ表の列：Project_ID, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

## g1082（1 列）
- 見出し：Class_Screening_ID
- 例1 値：11 | 11 | 5 | 5 | 5
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

## g1083（1 列）
- 見出し：Class_Screening_Title
- 例1 値：Routine Projects in National Park Commu… | Routine Projects within the Town of Ban… | Routine Projects within the Town of Ban… | Routine Projects in National Park Commu… | Routine Projects in National Park Commu…
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

## g1084（1 列）
- 見出し：Subclass
- 例1 値：Buildings | Buildings | Buildings | Buildings | Buildings
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

## g1085（1 列）
- 見出し：Nature_of_Project_1
- 例1 値：Building and Property Development | Ports and Harbours | Building and Property Development | Dams, Weirs and Reservoirs | Ports and Harbours
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_2, Nature_of_Project_3, Nature_of_Project_4

## g1086（1 列）
- 見出し：Nature_of_Project_2
- 例1 値：Building and Property Development | Highways and Roads | Dredging, Filling, Salvaging Dredge Spo… | Ports and Harbours | Dams, Weirs and Reservoirs
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_3, Nature_of_Project_4

## g1087（1 列）
- 見出し：Nature_of_Project_3
- 例1 値：Recreation and Tourism | Solid Waste
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_4

## g1088（1 列）
- 見出し：Nature_of_Project_4
- 例1 値：Water Management
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3

## g1089（1 列）
- 見出し：Responsible_or_Regulated_Authorities
- 例1 値：Aboriginal Affairs and Northern Develop… | Fisheries and Oceans Canada | Aboriginal Affairs and Northern Develop… | Environment Canada Fisheries and Oceans… | Aboriginal Affairs and Northern Develop…
  - 同じ表の列：Project_ID, Environmental_Asses…, Class_Screening_ID, Class_Screening_Tit…, Subclass, Nature_of_Project_1, Nature_of_Project_2, Nature_of_Project_3

## g1090（1 列）
- 見出し：DEFINITION
- 例1 値：Share | Average Amount Authorized | Financing Type | Intended Use | Region
  - 同じ表の列：VALUES, NOTES

## g1091（1 列）
- 見出し：VALUES
- 例1 値：Land and Buildings, Vehicles/Rolling St… | Percentage | Atlantic, Quebec, Ontario, ... | Exporter, Non-Exporter | Percentage
  - 同じ表の列：DEFINITION, NOTES

## g1092（1 列）
- 見出し：NOTES
- 例1 値：Interest rates and collateral requireme… | Approved amounts were calculated using … | Other includes: financing from governme… | A request that received either full app… | Fixed Assets includes: Land, Vehicles, …
  - 同じ表の列：DEFINITION, VALUES

## g1093（1 列）
- 見出し：Shelter Type
- 例1 値：Transitional | Emergency | Transitional | Transitional | Emergency
  - 同じ表の列：Province Code, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province, Clientele cible

## g1094（1 列）
- 見出し：Province Code
- 例1 値：ON | QC | SK | QC | SK
  - 同じ表の列：Shelter Type, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province, Clientele cible

## g1095（1 列）
- 見出し：City/Ville
- 例1 値：Vancouver | Campbell River | Toronto | Ottawa | Montreal
  - 同じ表の列：Shelter Type, Province Code, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province, Clientele cible

## g1096（1 列）
- 見出し：Target Clientele
- 例1 値：General | Youth | Youth | Youth | General
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province, Clientele cible

## g1097（1 列）
- 見出し：Gender(s) Served
- 例1 値：Both | Both | Male | Male | Female
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Number of Beds/Nomb…, Type de refuge, Code de la province, Clientele cible

## g1098（1 列）
- 見出し：Number of Beds/Nombre de lits
- 例1 値：10 | 37 | 975 | 9 | 144
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Gender(s) Served, Type de refuge, Code de la province, Clientele cible

## g1099（1 列）
- 見出し：Type de refuge
- 例1 値：Logement de transition | Refuge d'urgence | Refuge d'urgence | Logement de transition | Refuge d'urgence
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Code de la province, Clientele cible

## g1100（1 列）
- 見出し：Code de la province
- 例1 値：ON | QC | ON | SK | SK
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Clientele cible

## g1101（1 列）
- 見出し：Clientele cible
- 例1 値：Jeunes | Jeunes | Jeunes | Familles | Général
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province

## g1102（1 列）
- 見出し：Sexe desservi
- 例1 値：Hommes | Mixtes | Mixtes | Mixtes | Hommes
  - 同じ表の列：Shelter Type, Province Code, City/Ville, Target Clientele, Gender(s) Served, Number of Beds/Nomb…, Type de refuge, Code de la province

## g1103（1 列）
- 見出し：Pays de persecution
- 例1 値：Bahamas | Brésil | Angola | Afghanistan | Bulgarie
  - 同じ表の列：Annee, Resultats, Total

## g1104（1 列）
- 見出し：Annee
- 例1 値：2021 | 2021 | 2016 | 2021 | 2015
  - 同じ表の列：Pays de persecution, Resultats, Total

## g1105（1 列）
- 見出し：Resultats
- 例1 値：Positive | Autre | Positive | Négative | Autre
  - 同じ表の列：Pays de persecution, Annee, Total

## g1106（1 列）
- 見出し：Total
- 例1 値：-- | 33 | -- | 87 | --
  - 同じ表の列：Pays de persecution, Annee, Resultats

## g1107（1 列）
- 見出し：Organization Acronym
- 例1 値：HICC | PrairiesCan | CFIA | ACOA | OCI
  - 同じ表の列：Organization Acrony…, Phase, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1108（1 列）
- 見出し：Organization Acronym - FR
- 例1 値：APECA | SPPC | SATJ | SPC | ASC
  - 同じ表の列：Organization Acronym, Phase, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1109（1 列）
- 見出し：Phase
- 例1 値：3 | 3 | 2 | 3 | 1
  - 同じ表の列：Organization Acronym, Organization Acrony…, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1110（1 列）
- 見出し：Report Received
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1111（1 列）
- 見出し：Report Received - FR
- 例1 値：Oui | Oui | Oui | Oui | Oui
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, A - All Contracts t…, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1112（1 列）
- 見出し：A - All Contracts to Indigenous Business
- 例1 値：607074.64 | 8587803.72 | 37064 | 245715.65 | 809893
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, Report Received - FR, B - All Contracts A…, C - Value of total …, % of all contracts …

## g1113（1 列）
- 見出し：B - All Contracts Awarded to All Business
- 例1 値：102270418.2 | 228898161.3 | 1484003.79 | 6754237.51 | 69646973.97
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, Report Received - FR, A - All Contracts t…, C - Value of total …, % of all contracts …

## g1114（1 列）
- 見出し：C - Value of total contracts Deputy Head approved exceptions
- 例1 値：204945449 | 36614352 | 62134649 | 157585344 | 16177693
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, % of all contracts …

## g1115（1 列）
- 見出し：% of all contracts awarded to Indigenous business A / (B - C
- 例1 値：0.4 | 0.19 | 0.05 | 0.32 | 0.06
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …

## g1116（1 列）
- 見出し：Meet 5% Target
- 例1 値：No | Yes | Yes | Yes | No
  - 同じ表の列：Organization Acronym, Organization Acrony…, Phase, Report Received, Report Received - FR, A - All Contracts t…, B - All Contracts A…, C - Value of total …

## g1117（1 列）
- 見出し：Fiscal Year - Annee financiere
- 例1 値：2017-18 | 2017-18 | 2017-18 | 2017-18 | 2017-18
  - 同じ表の列：Quarter - Trimestre, Months - Mois, Total of published …, Total number of tit…

## g1118（1 列）
- 見出し：Quarter - Trimestre
- 例1 値：Q4 | Q2 | Q3 | Q3 | Q4
  - 同じ表の列：Fiscal Year - Annee…, Months - Mois, Total of published …, Total number of tit…

## g1119（1 列）
- 見出し：Months - Mois
- 例1 値：January | December | March | February | April
  - 同じ表の列：Fiscal Year - Annee…, Quarter - Trimestre, Total of published …, Total number of tit…

## g1120（1 列）
- 見出し：Total of published documents - Total de documents publies
- 例1 値：2696 | 2662 | 2267 | 2059 | 1706
  - 同じ表の列：Fiscal Year - Annee…, Quarter - Trimestre, Months - Mois, Total number of tit…

## g1121（1 列）
- 見出し：Total number of titles aqcuired - Nombre total de titres acq
- 例1 値：1653 | 1659 | 1765 | 2336 | 3002
  - 同じ表の列：Fiscal Year - Annee…, Quarter - Trimestre, Months - Mois, Total of published …

## g1122（1 列）
- 見出し：Data Source/Source des donnees
- 例1 値：Scopus/SciVal (Elsevier) | Scopus/SciVal (Elsevier) | Scopus/SciVal (Elsevier) | Scopus/SciVal (Elsevier) | Scopus/SciVal (Elsevier)
  - 同じ表の列：Publication Year/An…, Journal, Title/Titre, FWCI/IIPD, Number of citations…, DOI

## g1123（1 列）
- 見出し：Publication Year/Annee de publication
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：Data Source/Source …, Journal, Title/Titre, FWCI/IIPD, Number of citations…, DOI

## g1124（1 列）
- 見出し：Journal
- 例1 値：Surface and Coatings Technology | Optics InfoBase Conference Papers | International Journal of Ventilation | ACS Omega | Planetary Science Journal
  - 同じ表の列：Data Source/Source …, Publication Year/An…, Title/Titre, FWCI/IIPD, Number of citations…, DOI

## g1125（1 列）
- 見出し：Title/Titre
- 例1 値：Maximally accreting supermassive stars:… | Incorporation of Ammonium Fluoride and … | Characterization of extracellular vesic… | Thousands of cpgs show dna methylation … | Microphysical processes producing high …
  - 同じ表の列：Data Source/Source …, Publication Year/An…, Journal, FWCI/IIPD, Number of citations…, DOI

## g1126（1 列）
- 見出し：FWCI/IIPD
- 例1 値：0.93 | 0.53 | 2.96 | 0.56 | 0.89
  - 同じ表の列：Data Source/Source …, Publication Year/An…, Journal, Title/Titre, Number of citations…, DOI

## g1127（1 列）
- 見出し：Number of citations/Nombre de citations
- 例1 値：6 | 4 | 1 | 3 | 3
  - 同じ表の列：Data Source/Source …, Publication Year/An…, Journal, Title/Titre, FWCI/IIPD, DOI

## g1128（1 列）
- 見出し：DOI
- 例1 値：10.1103/PhysRevB.103.235310 | 10.1149/10301.1653ecst | 10.1093/mnras/stab1549 | 10.3850/978-981-14-8593-0_4043-cd | 10.1038/s41467-021-24234-1
  - 同じ表の列：Data Source/Source …, Publication Year/An…, Journal, Title/Titre, FWCI/IIPD, Number of citations…

## g1129（1 列）
- 見出し：Model year
- 例1 値：2024 | 2026 | 2025 | 2024 | 2022
  - 同じ表の列：Make, Model, Vehicle class, Motor (kW), Transmission, Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1130（1 列）
- 見出し：Make
- 例1 値：Ford | Volkswagen | BMW | Genesis | MINI
  - 同じ表の列：Model year, Model, Vehicle class, Motor (kW), Transmission, Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1131（1 列）
- 見出し：Model
- 例1 値：i7 xDrive60 Sedan (21" Wheels) | LEAF S PLUS | R1T Performance Dual Large (22" Wheels) | Model X 60D | i7 xDrive60 Sedan (19" Wheels)
  - 同じ表の列：Model year, Make, Vehicle class, Motor (kW), Transmission, Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1132（1 列）
- 見出し：Vehicle class
- 例1 値：Mid-size | Mid-size | Sport utility vehicle: Standard | Full-size | Sport utility vehicle: Standard
  - 同じ表の列：Model year, Make, Model, Motor (kW), Transmission, Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1133（1 列）
- 見出し：Motor (kW)
- 例1 値：360 | 250 | 160 | 634 | 160
  - 同じ表の列：Model year, Make, Model, Vehicle class, Transmission, Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1134（1 列）
- 見出し：Transmission
- 例1 値：A1 | A1 | A1 | A1 | A1
  - 同じ表の列：Model year, Make, Model, Vehicle class, Motor (kW), Fuel type, City (kWh/100 km), Highway (kWh/100 km)

## g1135（1 列）
- 見出し：Fuel type
- 例1 値：B | B | B | B | B
  - 同じ表の列：Model year, Make, Model, Vehicle class, Motor (kW), Transmission, City (kWh/100 km), Highway (kWh/100 km)

## g1136（1 列）
- 見出し：City (kWh/100 km)
- 例1 値：16.0 | 25.4 | 19.3 | 25.6 | 24.5
  - 同じ表の列：Model year, Make, Model, Vehicle class, Motor (kW), Transmission, Fuel type, Highway (kWh/100 km)

## g1137（1 列）
- 見出し：Highway (kWh/100 km)
- 例1 値：21.3 | 27.9 | 20.6 | 20.6 | 18.8
  - 同じ表の列：Model year, Make, Model, Vehicle class, Motor (kW), Transmission, Fuel type, City (kWh/100 km)

## g1138（1 列）
- 見出し：Combined (kWh/100 km)
- 例1 値：23.2 | 31.0 | 19.5 | 17.3 | 22.6
  - 同じ表の列：Model year, Make, Model, Vehicle class, Motor (kW), Transmission, Fuel type, City (kWh/100 km)

## g1139（1 列）
- 見出し：PROV
- 例1 値：ON | ON | BC | SK | BC
  - 同じ表の列：AREA, EMPGR, LANG, Q1, Q2, Q3, EMPSIZE, Q4M1

## g1140（1 列）
- 見出し：AREA
- 例1 値：2 | 2 | 4 | 1 | 4
  - 同じ表の列：PROV, EMPGR, LANG, Q1, Q2, Q3, EMPSIZE, Q4M1

## g1141（1 列）
- 見出し：EMPGR
- 例1 値：1 | 1 | 2 | 3 | 1
  - 同じ表の列：PROV, AREA, LANG, Q1, Q2, Q3, EMPSIZE, Q4M1

## g1142（1 列）
- 見出し：LANG
- 例1 値：EN | EN | EN | FR | FR
  - 同じ表の列：PROV, AREA, EMPGR, Q1, Q2, Q3, EMPSIZE, Q4M1

## g1143（1 列）
- 見出し：Q1
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q2, Q3, EMPSIZE, Q4M1

## g1144（1 列）
- 見出し：Q2
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q1, Q3, EMPSIZE, Q4M1

## g1145（1 列）
- 見出し：Q3
- 例1 値：9 | 2 | 17 | 2 | 4
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q1, Q2, EMPSIZE, Q4M1

## g1146（1 列）
- 見出し：EMPSIZE
- 例1 値：1 | 2 | 1 | 2 | 1
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q1, Q2, Q3, Q4M1

## g1147（1 列）
- 見出し：Q4M1
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q1, Q2, Q3, EMPSIZE

## g1148（1 列）
- 見出し：Q4M2
- 例1 値：3 | 4 | 3 | 3 | 4
  - 同じ表の列：PROV, AREA, EMPGR, LANG, Q1, Q2, Q3, EMPSIZE

## g1149（1 列）
- 見出し：Fiscal Year/Annee fiscale
- 例1 値：2026 | 2025 | 2024 | 2024 | 2025
  - 同じ表の列：Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve

## g1150（1 列）
- 見出し：Fiscal Quarter
- 例1 値：Q2 - 2025 | Q1 - 2025 | Q2 - 2021 | Q1 - 2023 | Q1 - 2022
  - 同じ表の列：Fiscal Year/Annee f…, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve

## g1151（1 列）
- 見出し：Trimestre fiscal
- 例1 値：T3 - 2022 | T2 - 2022 | T3 - 2024 | T1 - 2023 | T2 - 2023
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve

## g1152（1 列）
- 見出し：Total P&C Companies/FIs
- 例1 値：Total Canadian Mortgage Insurers | Total Canadian Mortgage Insurers | Total Canadian Mortgage Insurers | Total Canadian Mortgage Insurers | Total Canadian Mortgage Insurers
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total Societes d'as…, Industry Group, Groupe Sectoriel, Return/Releve

## g1153（1 列）
- 見出し：Total Societes d'assurance multirisque/IFFs
- 例1 値：Total assureurs hypothécaires canadien | Total assureurs hypothécaires canadien | Total assureurs hypothécaires canadien | Total assureurs hypothécaires canadien | Total assureurs hypothécaires canadien
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Industry Group, Groupe Sectoriel, Return/Releve

## g1154（1 列）
- 見出し：Industry Group
- 例1 値：Canadian Mortgage Insurers | Canadian Mortgage Insurers | Canadian Mortgage Insurers | Canadian Mortgage Insurers | Canadian Mortgage Insurers
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Groupe Sectoriel, Return/Releve

## g1155（1 列）
- 見出し：Groupe Sectoriel
- 例1 値：Assureurs hypothécaires canadien | Assureurs hypothécaires canadien | Assureurs hypothécaires canadien | Assureurs hypothécaires canadien | Assureurs hypothécaires canadien
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Return/Releve

## g1156（1 列）
- 見出し：Return/Releve
- 例1 値：MI | MI | MI | MI | MI
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Groupe Sectoriel

## g1157（1 列）
- 見出し：Return Title
- 例1 値：MI -Mortgage Insurance Capital Adequacy… | MI -Mortgage Insurance Capital Adequacy… | MI -Mortgage Insurance Capital Adequacy… | MI -Mortgage Insurance Capital Adequacy… | MI -Mortgage Insurance Capital Adequacy…
  - 同じ表の列：Fiscal Year/Annee f…, Fiscal Quarter, Trimestre fiscal, Id, Total P&C Companies…, Total Societes d'as…, Industry Group, Groupe Sectoriel

## g1158（1 列）
- 見出し：Place
- 例1 値：Saint-Ours Canal National Historic Site | Monument Lefebvre National Historic Site | S.S. Klondike National Historic Site | Fort Chambly National Historic Site | Kouchibouguac National Park
  - 同じ表の列：2025-26 FY Attendan…

## g1159（1 列）
- 見出し：2025-26 FY Attendance
- 例1 値：13,813 | 2,332 | 95,893 | 4,558,171 | 34,515
  - 同じ表の列：Place

## g1160（1 列）
- 見出し：Production Company / Societe de production
- 例1 値：2nd Chance Productions Ltd. | Out There Productions Inc | Abroad II 2022 Inc | WRC Productions Inc. | Reel One Films 3 Inc.
  - 同じ表の列：Production Company …, Production Company …

## g1161（1 列）
- 見出し：Production Company (2) / Societe de production (2)
- 例1 値：Christmas Fury 2017 Inc. | Frantic Films Live Action Producition I… | Eerie Productions Ontario Inc. | Capital Productions 4 (SV) Inc. | Elemental Obsession ONT Productions Inc.
  - 同じ表の列：Production Company …, Production Company …

## g1162（1 列）
- 見出し：Production Company (3) / Societe de production (3)
- 例1 値：Turtlebox Productions Inc. | Aboriginal Day Live 2017 QC Inc. | Frantic Films Ontario Inc.
  - 同じ表の列：Production Company …, Production Company …

## g1163（1 列）
- 見出し：registration_number
- 例1 値：cta-otc-2024-2 | A-001831 | C-0000003 | A-002491 | C202301
  - 同じ表の列：partner_departments, subjects, title_en, title_fr, start_date, end_date, status, profile_page_en

## g1164（1 列）
- 見出し：partner_departments
- 例1 値：D235,D64 | D115,D119,D173 | D94 | D115 | D16
  - 同じ表の列：registration_number, subjects, title_en, title_fr, start_date, end_date, status, profile_page_en

## g1165（1 列）
- 見出し：subjects
- 例1 値：EN | CM | AG,AM,AN,IN,RE | NR,RE | EC,ED,FI,SE,ST
  - 同じ表の列：registration_number, partner_departments, title_en, title_fr, start_date, end_date, status, profile_page_en

## g1166（1 列）
- 見出し：title_en
- 例1 値：Modernizing Crop Variety Registration i… | Recovery Strategy for the Maritime Ring… | Engagement Sessions on Bill C-27, First… | Digital Services Tax Consultation | CN Jansen Spur Consultation
  - 同じ表の列：registration_number, partner_departments, subjects, title_fr, start_date, end_date, status, profile_page_en

## g1167（1 列）
- 見出し：title_fr
- 例1 値：Placements des régimes de pension au Ca… | Conduite de l'exploitation : Gestion de… | Provisoire – Guide sur le processus de … | Conventions des Nations Unis relative a… | Les lignes directrices proposées concer…
  - 同じ表の列：registration_number, partner_departments, subjects, title_en, start_date, end_date, status, profile_page_en

## g1168（1 列）
- 見出し：start_date
- 例1 値：2021-07-16 | 2010-01-01 | 2011-07-07 | 2017-01-11 | 2010-10-30
  - 同じ表の列：registration_number, partner_departments, subjects, title_en, title_fr, end_date, status, profile_page_en

## g1169（1 列）
- 見出し：end_date
- 例1 値：2020-08-13 | 2020-12-03 | 2021-07-06 | 2022-11-07 | 2022-11-30
  - 同じ表の列：registration_number, partner_departments, subjects, title_en, title_fr, start_date, status, profile_page_en

## g1170（1 列）
- 見出し：profile_page_en
- 例1 値：https://crtc.gc.ca/eng/consultation/nor… | http://www.statcan.gc.ca/consult/2012/e… | http://www.fin.gc.ca/vcap-pacr/index-en… | http://www.fin.gc.ca/activty/consult/pc… | https://www.cbsa-asfc.gc.ca/agency-agen…
  - 同じ表の列：registration_number, partner_departments, subjects, title_en, title_fr, start_date, end_date, status

## g1171（1 列）
- 見出し：profile_page_fr
- 例1 値：http://otc-cta.gc.ca/fra/consultation/c… | https://www.cmhc-schl.gc.ca/fr/salle-de… | http://www.cer-rec.gc.ca/bts/ctrg/gnnb/… | https://www.otc-cta.gc.ca/fra/consultat… | http://inspection.gc.ca/vegetaux/export…
  - 同じ表の列：registration_number, partner_departments, subjects, title_en, title_fr, start_date, end_date, status

## g1172（1 列）
- 見出し：resp_id
- 例1 値：658 | 791 | 563 | 210 | 218
  - 同じ表の列：prov, weight, gender, A, A_R, QC, D_1, D_2

## g1173（1 列）
- 見出し：prov
- 例1 値：Sask. | New Brunswick | Alberta | Quebec | Sask.
  - 同じ表の列：resp_id, weight, gender, A, A_R, QC, D_1, D_2

## g1174（1 列）
- 見出し：weight
- 例1 値：1 | 1 | 2 | 1 | 1
  - 同じ表の列：resp_id, prov, gender, A, A_R, QC, D_1, D_2

## g1175（1 列）
- 見出し：A
- 例1 値：First Nations | First Nations | First Nations | First Nations | First Nations
  - 同じ表の列：resp_id, prov, weight, gender, A_R, QC, D_1, D_2

## g1176（1 列）
- 見出し：A_R
- 例1 値：#NULL! | #NULL! | #NULL! | #NULL! | #NULL!
  - 同じ表の列：resp_id, prov, weight, gender, A, QC, D_1, D_2

## g1177（1 列）
- 見出し：QC
- 例1 値：2 | 1 | 1 | 2 | 2
  - 同じ表の列：resp_id, prov, weight, gender, A, A_R, D_1, D_2

## g1178（1 列）
- 見出し：D_1
- 例1 値：25 | 60 | 20 | 36 | 25
  - 同じ表の列：resp_id, prov, weight, gender, A, A_R, QC, D_2

## g1179（1 列）
- 見出し：D_2
- 例1 値：25 | 48 | #NULL! | #NULL! | 36
  - 同じ表の列：resp_id, prov, weight, gender, A, A_R, QC, D_1

## g1180（1 列）
- 見出し：D_3
- 例1 値：#NULL! | #NULL! | #NULL! | #NULL! | #NULL!
  - 同じ表の列：resp_id, prov, weight, gender, A, A_R, QC, D_1

## g1181（1 列）
- 見出し：FISCAL_YEAR
- 例1 値：2023-2024 | 2023-2024 | 2023-2024 | 2023-2024 | 2023-2024
  - 同じ表の列：CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1182（1 列）
- 見出し：CAR_CHC_ID
- 例1 値：1867994 | 1 | 1891244 | 1882493 | 1937736
  - 同じ表の列：FISCAL_YEAR, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1183（1 列）
- 見出し：REFERENCE_NUMBER
- 例1 値：SVC22J-044795-000063 | RCM22J-020967-000086 | DFO22J-015935-000550 | CEO23J-112795-000014 | RCM21J-021207-000510
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1184（1 列）
- 見出し：SELECTION_PROCESS_NUMBER
- 例1 値：22-DIS-ATL-IA-435308 | 23-CSW-EA-BA-PROG-200 | 23-RCM-IA-N-N-NCR-FP-116132 | 2022-PEN-EA-ATL-176577 | 22/23-SIF-EA-9345
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1185（1 列）
- 見出し：CREATION_DATE
- 例1 値：2023-03-14 | 2022-08-18 | 2023-03-23 | 2023-03-07 | 2023-01-17
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1186（1 列）
- 見出し：OPEN_DATE
- 例1 値：2023-02-10 | 2023-03-23 | 2022-09-23 | 2023-03-31 | 2023-05-02
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, CLOSE_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1187（1 列）
- 見出し：CLOSE_DATE
- 例1 値：2023-06-01 | 2023-12-14 | 2024-06-19 | 2023-04-28 | 2023-04-04
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, DAYS_TO_OPEN, NUMBER_DAYS_OPEN

## g1188（1 列）
- 見出し：DAYS_TO_OPEN
- 例1 値：58 | 27 | 217 | 18 | 19
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, NUMBER_DAYS_OPEN

## g1189（1 列）
- 見出し：NUMBER_DAYS_OPEN
- 例1 値：3 | 353 | 436 | 9 | 729
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN

## g1190（1 列）
- 見出し：INTERNAL_INDICATOR
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：FISCAL_YEAR, CAR_CHC_ID, REFERENCE_NUMBER, SELECTION_PROCESS_N…, CREATION_DATE, OPEN_DATE, CLOSE_DATE, DAYS_TO_OPEN

## g1191（1 列）
- 見出し：Partner Acronym
- 例1 値：ISED | FINTRAC | VAC | CSC | PCO
  - 同じ表の列：Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1192（1 列）
- 見出し：Timeliness 1
- 例1 値：1 | 2 | 1 | 3 | 3
  - 同じ表の列：Partner Acronym, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1193（1 列）
- 見出し：Timeliness 2
- 例1 値：4 | 4 | 3 | 3 | 3
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1194（1 列）
- 見出し：Timeliness 3
- 例1 値：4 | 4 | 4 | 4 | 4
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1195（1 列）
- 見出し：Ease of Access 1
- 例1 値：4 | 2 | 3 | 1 | 3
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 2, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1196（1 列）
- 見出し：Ease of Access 2
- 例1 値：4 | 4 | 2 | 4 | 5
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 3, Positive Outcome 1, Positive Outcome 2

## g1197（1 列）
- 見出し：Ease of Access 3
- 例1 値：4 | 4 | 4 | 5 | 1
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Positive Outcome 1, Positive Outcome 2

## g1198（1 列）
- 見出し：Positive Outcome 1
- 例1 値：2 | 4 | 4 | 3 | 4
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 2

## g1199（1 列）
- 見出し：Positive Outcome 2
- 例1 値：3 | 4 | 4 | 4 | 3
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1

## g1200（1 列）
- 見出し：Process Aspect 1
- 例1 値：3 | 3 | 4 | 4 | 4
  - 同じ表の列：Partner Acronym, Timeliness 1, Timeliness 2, Timeliness 3, Ease of Access 1, Ease of Access 2, Ease of Access 3, Positive Outcome 1

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
