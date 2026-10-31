# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Code
- 例1 値：134 | 156 | 137 | 138 | 178
  - 同じ表の列：Red, Green, Blue, Label, Étiquette

## g0002（1 列）
- 見出し：Red
- 例1 値：146 | 197 | 182 | 116 | 204
  - 同じ表の列：Code, Green, Blue, Label, Étiquette

## g0003（1 列）
- 見出し：Green
- 例1 値：51 | 102 | 118 | 102 | 51
  - 同じ表の列：Code, Red, Blue, Label, Étiquette

## g0004（1 列）
- 見出し：Blue
- 例1 値：79 | 153 | 80 | 102 | 77
  - 同じ表の列：Code, Red, Green, Label, Étiquette

## g0005（1 列）
- 見出し：Label
- 例1 値：Potatoes | Sod | Blueberry | Vegetables | Chickpeas
  - 同じ表の列：Code, Red, Green, Blue, Étiquette

## g0006（1 列）
- 見出し：Étiquette
- 例1 値：Vergers | Céréales | Chanvre | Terres humides | Tourbière exploitée
  - 同じ表の列：Code, Red, Green, Blue, Label

## g0007（1 列）
- 見出し：Year|Année
- 例1 値：2012 | 2012 | 2012 | 2012 | 2012
  - 同じ表の列：Month|Mois, Client Type|Types d…, Level|Niveau, Net Penalty Amount|…, Contravention Code|…, # of penalties|# d’…, Type|Type

## g0008（1 列）
- 見出し：Month|Mois
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Year|Année, Client Type|Types d…, Level|Niveau, Net Penalty Amount|…, Contravention Code|…, # of penalties|# d’…, Type|Type

## g0009（1 列）
- 見出し：Client Type|Types des clients
- 例1 値：Importer - Importateurs | Carrier - Transporteurs | Importer - Importateurs | Carrier - Transporteurs | Warehouse Operator - Exploitants d'entr…
  - 同じ表の列：Year|Année, Month|Mois, Level|Niveau, Net Penalty Amount|…, Contravention Code|…, # of penalties|# d’…, Type|Type

## g0010（1 列）
- 見出し：Level|Niveau
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Year|Année, Month|Mois, Client Type|Types d…, Net Penalty Amount|…, Contravention Code|…, # of penalties|# d’…, Type|Type

## g0011（1 列）
- 見出し：Net Penalty Amount|Montants net des pénalités
- 例1 値：0 | 0 | 150 | 150 | 0
  - 同じ表の列：Year|Année, Month|Mois, Client Type|Types d…, Level|Niveau, Contravention Code|…, # of penalties|# d’…, Type|Type

## g0012（1 列）
- 見出し：Contravention Code|Code d'infraction
- 例1 値：C207 | C005 | C336 | C244 | C244
  - 同じ表の列：Year|Année, Month|Mois, Client Type|Types d…, Level|Niveau, Net Penalty Amount|…, # of penalties|# d’…, Type|Type

## g0013（1 列）
- 見出し：# of penalties|# d’infractions
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Year|Année, Month|Mois, Client Type|Types d…, Level|Niveau, Net Penalty Amount|…, Contravention Code|…, Type|Type

## g0014（1 列）
- 見出し：Type|Type
- 例1 値：Border - Frontalière | Border - Frontalière | Border - Frontalière | Border - Frontalière | Border - Frontalière
  - 同じ表の列：Year|Année, Month|Mois, Client Type|Types d…, Level|Niveau, Net Penalty Amount|…, Contravention Code|…, # of penalties|# d’…

## g0015（4 列）
- 見出し：Year
- 例1 値：2019 | 2020 | 2015 | 2015 | 2015
  - 同じ表の列：Month, Volume (m3), Volume (m3 per day), Volume (bbl), Volume (bbl per day)
- 例2 値：1996 | 2000 | 1999 | 1996 | 1991
  - 同じ表の列：Flow, Port, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$), Price (CN$/GJ)

## g0016（1 列）
- 見出し：Month
- 例1 値：November | March | January | August | June
  - 同じ表の列：Year, Volume (m3), Volume (m3 per day), Volume (bbl), Volume (bbl per day)

## g0017（1 列）
- 見出し：Volume (m3)
- 例1 値：653,555 | 525,645 | 1,523,602 | 639,449 | 526,399
  - 同じ表の列：Year, Month, Volume (m3 per day), Volume (bbl), Volume (bbl per day)

## g0018（1 列）
- 見出し：Volume (m3 per day)
- 例1 値：64,163 | 12,563 | 12,514 | 11,799 | 25,313
  - 同じ表の列：Year, Month, Volume (m3), Volume (bbl), Volume (bbl per day)

## g0019（1 列）
- 見出し：Volume (bbl)
- 例1 値：2,579,237 | 2,649,088 | 2,953,378 | 3,718,026 | 1,818,210
  - 同じ表の列：Year, Month, Volume (m3), Volume (m3 per day), Volume (bbl per day)

## g0020（1 列）
- 見出し：Volume (bbl per day)
- 例1 値：151,894 | 89,141 | 155,655 | 120,075 | 124,781
  - 同じ表の列：Year, Month, Volume (m3), Volume (m3 per day), Volume (bbl)

## g0021（1 列）
- 見出し：Flow
- 例1 値：Exports | Exports | Imports | Exports | Exports
  - 同じ表の列：Year, Port, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$), Price (CN$/GJ)

## g0022（1 列）
- 見出し：Port
- 例1 値：North Portal | Huntingdon | Corunna | Reagan Field | Sault Ste Marie
  - 同じ表の列：Year, Flow, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$), Price (CN$/GJ)

## g0023（1 列）
- 見出し：Region
- 例1 値：MidWest | MidWest | West | East | East
  - 同じ表の列：Year, Flow, Port, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$), Price (CN$/GJ)

## g0024（1 列）
- 見出し：Volume (10^3 m3)
- 例1 値：35953.800000 | 101714152.120400 | 408916.900000 | 1360354.600000 | 3843326.400578
  - 同じ表の列：Year, Flow, Port, Region, Volume (MCF), Value (CN$), Value (US$), Price (CN$/GJ)

## g0025（1 列）
- 見出し：Volume (MCF)
- 例1 値：652549802.830537 | 9720794.102198 | 200186213.632949 | 100004.094912 | 348286.350106
  - 同じ表の列：Year, Flow, Port, Region, Volume (10^3 m3), Value (CN$), Value (US$), Price (CN$/GJ)

## g0026（1 列）
- 見出し：Value (CN$)
- 例1 値：20501620.71 | 12928869.00 | 7404.61 | 215993672.80 | 2868548899.82
  - 同じ表の列：Year, Flow, Port, Region, Volume (10^3 m3), Volume (MCF), Value (US$), Price (CN$/GJ)

## g0027（1 列）
- 見出し：Value (US$)
- 例1 値：1036097.05 | 9959482.03 | 1784088312.48 | 116363725.17 | 83184944.32
  - 同じ表の列：Year, Flow, Port, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Price (CN$/GJ)

## g0028（1 列）
- 見出し：Price (CN$/GJ)
- 例1 値：3.23 | 3.16 | 1.99 | 5.34 | 5.40
  - 同じ表の列：Year, Flow, Port, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$)

## g0029（1 列）
- 見出し：Price (US$/MMBTU)
- 例1 値：3.41 | 2.54 | 1.67 | 3.13 | 3.79
  - 同じ表の列：Year, Flow, Port, Region, Volume (10^3 m3), Volume (MCF), Value (CN$), Value (US$)

## g0030（2 列）
- 見出し：province
- 例1 値：Alberta | Alberta | Alberta | Manitoba | Manitoba
  - 同じ表の列：grain_code, variety_stats, acres, year
- 例2 値：Saskatchewan | Saskatchewan | Saskatchewan | Saskatchewan | Alberta
  - 同じ表の列：crop_year, grain, Station, deliveries_kT

## g0031（1 列）
- 見出し：grain_code
- 例1 値：Beans | Canola | Canola | Soybeans | Flaxseed
  - 同じ表の列：province, variety_stats, acres, year

## g0032（1 列）
- 見出し：variety_stats
- 例1 値：FOREMOST | 4414 RR | RUGBY | DKC27-55 | CDC PLATO
  - 同じ表の列：province, grain_code, acres, year

## g0033（2 列）
- 見出し：acres
- 例1 値：80 | 145 | 1148 | 240 | 26064
  - 同じ表の列：province, grain_code, variety_stats, year
- 例2 値：89 | 2446 | 28824 | 26 | 673
  - 同じ表の列：province, grain_code, variety, year

## g0034（2 列）
- 見出し：province
- 例1 値：British Columbia | Alberta | Alberta | Alberta | Alberta
  - 同じ表の列：grain_code, variety, acres, year
- 例2 値：British Columbia | Quebec | Alberta | Ontario | Quebec
  - 同じ表の列：Participation Type, City

## g0035（1 列）
- 見出し：grain_code
- 例1 値：Oat | Barley | Amber Durum | Barley | Barley
  - 同じ表の列：province, variety, acres, year

## g0036（1 列）
- 見出し：variety
- 例1 値：CDC FIBAR | TRANSCEND | CONQUER | AC ABBEY | CDN BISON
  - 同じ表の列：province, grain_code, acres, year

## g0037（1 列）
- 見出し：crop_year
- 例1 値：2006-2007 | 2006-2007 | 2006-2007 | 2006-2007 | 2006-2007
  - 同じ表の列：grain, Province, Station, deliveries_kT

## g0038（1 列）
- 見出し：grain
- 例1 値：Flaxseed | Cdn BlyMlt | Barley | Barley | Wheat
  - 同じ表の列：crop_year, Province, Station, deliveries_kT

## g0039（1 列）
- 見出し：Station
- 例1 値：DAVIDSON | DAVIDSON | LANGENBURG | NAICAM | BINSCARTH
  - 同じ表の列：crop_year, grain, Province, deliveries_kT

## g0040（1 列）
- 見出し：deliveries_kT
- 例1 値：0.2 | 23.0 | 1.4 | 6.6 | 62.5
  - 同じ表の列：crop_year, grain, Province, Station

## g0041（3 列）
- 見出し：EN_YEAR
- 例1 値：2016 | 2019 | 2016 | 2019 | 2015
  - 同じ表の列：EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL
- 例2 値：2016 | 2023 | 2025 | 2023 | 2022
  - 同じ表の列：EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER

## g0042（3 列）
- 見出し：EN_MONTH
- 例1 値：Feb | Dec | Oct | Sep | Sep
  - 同じ表の列：EN_YEAR, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL
- 例2 値：Jul | Jan | Jun | Nov | Jun
  - 同じ表の列：EN_YEAR, EN_QUARTER, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER

## g0043（3 列）
- 見出し：FR_ANNEÉ
- 例1 値：2015 | 2018 | 2019 | 2015 | 2016
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL
- 例2 値：2025 | 2017 | 2020 | 2023 | 2020
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER

## g0044（1 列）
- 見出し：FR_MOIS
- 例1 値：nov. | juil. | sept. | juil. | sept.
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL

## g0045（1 列）
- 見出し：EN_PROVINCE_TERRITORY
- 例1 値：Manitoba | Quebec | Ontario | Quebec | Alberta
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_MOIS, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL

## g0046（1 列）
- 見出し：FR_PROVINCE_TERRITOIRE
- 例1 値：Colombie-Britannique | Manitoba | Nouvelle-Écosse | Québec | Nouvelle-Écosse
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…, TOTAL

## g0047（1 列）
- 見出し：EN_CLAIM_OFFICE_TYPE
- 例1 値：Airport | Border | Inland | Airport | Border
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, FR_TYPE_DU_BUREAU_D…, TOTAL

## g0048（1 列）
- 見出し：FR_TYPE_DU_BUREAU_DE_RÉCEPTION_DE_LA_DEMANDE
- 例1 値：Poste frontière | Poste frontière | Aéroport | Bureau intérieur | Bureau intérieur
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, TOTAL

## g0049（1 列）
- 見出し：TOTAL
- 例1 値：125 | 645 | 5 | 10 | --
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_CLAIM_OFFICE_TYPE, FR_TYPE_DU_BUREAU_D…

## g0050（2 列）
- 見出し：EN_QUARTER
- 例1 値：Q2 | Q2 | Q3 | Q4 | Q3
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER
- 例2 値：Q2 | Q2 | Q1 | Q2 | Q2
  - 同じ表の列：EN_YEAR, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_IMMIGRATION_CATE…

## g0051（2 列）
- 見出し：FR_TRIMESTRE
- 例1 値：T3 | T3 | T3 | T3 | T1
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER
- 例2 値：T2 | T1 | T2 | T3 | T3
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_IMMIGRATION_CATE…

## g0052（1 列）
- 見出し：FR_MOIS
- 例1 値：fév. | juin | juin | juin | août
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_GENDER

## g0053（2 列）
- 見出し：EN_PROVINCE_TERRITORY
- 例1 値：Nova Scotia | Nova Scotia | Manitoba | New Brunswick | New Brunswick
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, FR_PROVINCE_TERRITO…, EN_GENDER
- 例2 値：Ontario | Manitoba | Manitoba | Ontario | British Columbia
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, FR_PROVINCE_TERRITO…, EN_IMMIGRATION_CATE…

## g0054（1 列）
- 見出し：FR_PROVINCE_TERRITOIRE
- 例1 値：Colombie-Britannique | Manitoba | Nouveau-Brunswick | Nouvelle-Écosse | Alberta
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, EN_GENDER

## g0055（1 列）
- 見出し：EN_GENDER
- 例1 値：Male | Male | Female | Male | Female
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…

## g0056（1 列）
- 見出し：FR_SEXE
- 例1 値：Hommes | Femmes | Hommes | Femmes | Femmes
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…

## g0057（1 列）
- 見出し：FR_MOIS
- 例1 値：mars | août | mars | juin | juin
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…, EN_IMMIGRATION_CATE…

## g0058（1 列）
- 見出し：FR_PROVINCE_TERRITOIRE
- 例1 値：Nouvelle-Écosse | Terre-Neuve-et-Labrador | Québec | Ontario | Ontario
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, EN_IMMIGRATION_CATE…

## g0059（1 列）
- 見出し：EN_IMMIGRATION_CATEGORY-MAIN_CATEGORY
- 例1 値：Sponsored Family | All Other Immigration | Economic | Economic | Resettled Refugee & Protected Person in…
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…

## g0060（1 列）
- 見出し：FR_CATÉGORIE_D'IMMIGRATION-CATÉGORIE_PRINCIPALE
- 例1 値：Famille parrainée | Famille parrainée | Économique | Réfugiés réinstallés et personnes proté… | Économique
  - 同じ表の列：EN_YEAR, EN_QUARTER, EN_MONTH, FR_ANNEÉ, FR_TRIMESTRE, FR_MOIS, EN_PROVINCE_TERRITO…, FR_PROVINCE_TERRITO…

## g0061（1 列）
- 見出し：Year | Année
- 例1 値：2019 | 2014 | 2021 | 2016 | 2023
  - 同じ表の列：City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …

## g0062（1 列）
- 見出し：City | Ville
- 例1 値：Elliot Lake | Elliot Lake | Elliot Lake | Elliot Lake | Elliot Lake
  - 同じ表の列：Year | Année, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …

## g0063（1 列）
- 見出し：Province | Province
- 例1 値：ON | ON | ON | ON | ON
  - 同じ表の列：Year | Année, City | Ville, Units | Unités, Stack Emissions | É…, Direct Discharge | …

## g0064（1 列）
- 見出し：Units | Unités
- 例1 値：MBq | kg | kg | MBq | MBq
  - 同じ表の列：Year | Année, City | Ville, Province | Province, Stack Emissions | É…, Direct Discharge | …

## g0065（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS
  - 同じ表の列：Year | Année, City | Ville, Province | Province, Units | Unités, Direct Discharge | …

## g0066（1 列）
- 見出し：Direct Discharge | Évacuations directes
- 例1 値：41.5 | 81.1 | 9.3 | 383.2 | 14.6
  - 同じ表の列：Year | Année, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…

## g0067（1 列）
- 見出し：SATID
- 例1 値：RCM-3 | RCM-1 | RCM-2 | RCM-1 | RCM-1
  - 同じ表の列：BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_EN, CCD_FR

## g0068（1 列）
- 見出し：BEAMTYPE_EN
- 例1 値：Low Resolution 100m | Medium Resolution 50m | Medium Resolution 50m | Low Resolution 100m | Low Resolution 100m
  - 同じ表の列：SATID, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_EN, CCD_FR

## g0069（1 列）
- 見出し：BEAMTYPE_FR
- 例1 値：Résolution moyenne 50m | Faible résolution 100m | Résolution moyenne 50m | Résolution moyenne 50m | Faible résolution 100m
  - 同じ表の列：SATID, BEAMTYPE_EN, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_EN, CCD_FR

## g0070（1 列）
- 見出し：POLTYPE_EN
- 例1 値：Dual Co/Cross Polarization | Dual HH-VV Polarization | Dual HH-VV Polarization | Dual Co/Cross Polarization | Dual HH-VV Polarization
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_FR, TXPOL, RXPOL, CCD_EN, CCD_FR

## g0071（1 列）
- 見出し：POLTYPE_FR
- 例1 値：Polarisation double HH-VV | Polarisation double HH-VV | Polarisation double HH-VV | Polarisation double HH-VV | Polarisation double HH-VV
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, TXPOL, RXPOL, CCD_EN, CCD_FR

## g0072（1 列）
- 見出し：TXPOL
- 例1 値：H | H+V | H+V | H+V | H
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, RXPOL, CCD_EN, CCD_FR

## g0073（1 列）
- 見出し：RXPOL
- 例1 値：H+V | H+V | H+V | H+V | H+V
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, CCD_EN, CCD_FR

## g0074（1 列）
- 見出し：CCD_EN
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_FR

## g0075（1 列）
- 見出し：CCD_FR
- 例1 値：FAUX | FAUX | FAUX | FAUX | FAUX
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_EN

## g0076（1 列）
- 見出し：EXACTCCD_EN
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：SATID, BEAMTYPE_EN, BEAMTYPE_FR, POLTYPE_EN, POLTYPE_FR, TXPOL, RXPOL, CCD_EN

## g0077（1 列）
- 見出し：Facility Reference Number
- 例1 値：Licence Holder | Licence Type | Site Specific Conditions | SEP Community Facilities | Licensed Species
  - 同じ表の列：The unique identifi…

## g0078（1 列）
- 見出し：The unique identification number assigned to the facility.
- 例1 値：The name of the company or person that … | A licence issued to an aquaculture faci… | Conditions of Licence specific to the f… | For SEP Community Facilities, the group… | The latitude position in decimal degree…
  - 同じ表の列：Facility Reference …

## g0079（1 列）
- 見出し：Transect_ID
- 例1 値：CON030 | CON034 | CON033 | CON030 | CON033
  - 同じ表の列：Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, Altitude_m, FOV_m2

## g0080（1 列）
- 見出し：Date_YYYYMMDD
- 例1 値：20230924 | 20230924 | 20230923 | 20230923 | 20230923
  - 同じ表の列：Transect_ID, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, Altitude_m, FOV_m2

## g0081（1 列）
- 見出し：Time_UTC_HHMMSS_Heure_UTC_HHMMSS
- 例1 値：143611 | 123005 | 173005 | 140019 | 145402
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Distance_to_next_im…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, Altitude_m, FOV_m2

## g0082（1 列）
- 見出し：Distance_to_next_image_m_Distance_entre_deux_images_m
- 例1 値：3.47509643 | 4.72636186 | 6.515804977 | 9.85 | 8.609891172
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, Altitude_m, FOV_m2

## g0083（1 列）
- 見出し：Time_lapse_to_next_image_s_Intervalle_entre_deux_images_s
- 例1 値：12 | 5 | 30 | 23 | 24
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Bathymetry_m_Bathym…, Altitude_m, FOV_m2

## g0084（1 列）
- 見出し：Bathymetry_m_Bathymétrie_m
- 例1 値：-41.57974 | -75.21526 | 50.09476471 | 117.3079224 | 36.85971832
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Time_lapse_to_next_…, Altitude_m, FOV_m2

## g0085（1 列）
- 見出し：Altitude_m
- 例1 値：1 | 1 | 0.8 | 1 | 0.8
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, FOV_m2

## g0086（1 列）
- 見出し：FOV_m2
- 例1 値：1.350534131 | 0.965 | 0.875 | 1.562658541 | 1.19565651
  - 同じ表の列：Transect_ID, Date_YYYYMMDD, Time_UTC_HHMMSS_Heu…, Distance_to_next_im…, Time_lapse_to_next_…, Bathymetry_m_Bathym…, Altitude_m

## g0087（1 列）
- 見出し：descriptionEN
- 例1 値：Department (French) | Type of exercise (French) | Type of exercise (English) | Name of firing practice and exercise ar… | Air space used in firing practice and e…
  - 同じ表の列：descriptionFR

## g0088（1 列）
- 見出し：descriptionFR
- 例1 値：département (anglais) | type d'exercice (français) | espace aérien utilisé dans la zone de p… | nom de la zone de pratique de tir et d'… | département (français)
  - 同じ表の列：descriptionEN

## g0089（1 列）
- 見出し：Field|Champ
- 例1 値：FrenchName | RecordID | individual_order | task_comments | vocalization
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0090（1 列）
- 見出し：Table|Tableau
- 例1 値：YT_HighElevationMonitoringProgram_ARU_D… | YT_HighElevationMonitoringProgram_ARU_D… | YT_HighElevationMonitoringProgram_ARU_D… | YT_HighElevationMonitoringProgram_ARU_D… | YT_HighElevationMonitoringProgram_ARU_D…
  - 同じ表の列：Field|Champ, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0091（2 列）
- 見出し：Data_type_en
- 例1 値：text | long integer | decimal | short integer | short integer
  - 同じ表の列：Field|Champ, Table|Tableau, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：text | short integer | text | short integer | text
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0092（1 列）
- 見出し：Type_de_données_fr
- 例1 値：décimal | entier court | décimal | texte | entier court
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, NULL_permitted|auto…, Field_length|Longue…, Values_lookup|Reche…

## g0093（1 列）
- 見出し：NULL_permitted|autorisé
- 例1 値：Y|O | N|N | N|N | N|N | N|N
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…

## g0094（2 列）
- 見出し：Field_length|Longueur_du_champ
- 例1 値：18 | 170 | 12 | 73 | 10
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Values_lookup|Reche…
- 例2 値：2 | 47 | 4 | 1 | 4
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Values_lookup|Reche…

## g0095（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：abundance | species_class | vocalization | see|voir DetectionCodes|CodesDétection
  - 同じ表の列：Field|Champ, Table|Tableau, Data_type_en, Type_de_données_fr, NULL_permitted|auto…, Field_length|Longue…

## g0096（1 列）
- 見出し：Table|Tableau
- 例1 値：Species_Codes_Espèces.csv | Data_Dictionary_Dictionaire_Donnés.csv | Other_Codes_Autres.csv | Other_Codes_Autres.csv | Data_Dictionary_Dictionaire_Donnés.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0097（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | n/a | Month|Mois | n/a | Station ID|ID de la station
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0098（1 列）
- 見出し：Type_de_données_fr
- 例1 値：entier court | entier court | décimal | entier court | entier court
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0099（1 列）
- 見出し：NULL_exists|NULL_existe
- 例1 値：N|N | N|N | N|N | N|N | N|N
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…

## g0100（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：Period | See Species_Codes_Espèces.csv | Distance | Behaviour | StandNumber
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0101（1 列）
- 見出し：SITE
- 例1 値：Pickhandle | Rock Island Lake | Pickhandle | Rock Island Lake | Kloo Lake
  - 同じ表の列：STN, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, HR_START, MIN_START, OBS_ID

## g0102（1 列）
- 見出し：STN
- 例1 値：B9 | B3 | P4 | K7 | R8
  - 同じ表の列：SITE, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, HR_START, MIN_START, OBS_ID

## g0103（1 列）
- 見出し：LOCATION_WT
- 例1 値：SYWRPC:K5 | IABTBL:BL:5 | SYWRPC:R1 | SYWRPC:R3 | SYWRPC:K19
  - 同じ表の列：SITE, STN, YR_SURV, MON_SURV, DAY_SURV, HR_START, MIN_START, OBS_ID

## g0104（1 列）
- 見出し：YR_SURV
- 例1 値：2003 | 2003 | 2003 | 2003 | 2003
  - 同じ表の列：SITE, STN, LOCATION_WT, MON_SURV, DAY_SURV, HR_START, MIN_START, OBS_ID

## g0105（1 列）
- 見出し：MON_SURV
- 例1 値：6 | 6 | 6 | 6 | 6
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, DAY_SURV, HR_START, MIN_START, OBS_ID

## g0106（1 列）
- 見出し：DAY_SURV
- 例1 値：4 | 27 | 9 | 9 | 5
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, MON_SURV, HR_START, MIN_START, OBS_ID

## g0107（1 列）
- 見出し：HR_START
- 例1 値：5 | 7 | 7 | 8 | 7
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, MIN_START, OBS_ID

## g0108（1 列）
- 見出し：MIN_START
- 例1 値：13 | 57 | 16 | 26 | 36
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, HR_START, OBS_ID

## g0109（1 列）
- 見出し：OBS_ID
- 例1 値：181 | 55 | 55 | 55 | 55
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, HR_START, MIN_START

## g0110（1 列）
- 見出し：TEMP
- 例1 値：6 | 6 | 6 | 8 | 12
  - 同じ表の列：SITE, STN, LOCATION_WT, YR_SURV, MON_SURV, DAY_SURV, HR_START, MIN_START

## g0111（1 列）
- 見出し：ActivitySector_SecteurD'activité
- 例1 値：Banks_Banque | Banks_Banque | Banks_Banque | Banks_Banque | Banks_Banque
  - 同じ表の列：PostalCode_CodePost…, ReportType_TypeDeDé…, YearMonthReportRece…, NumberOfReports_Nom…, FiscalYear_Exercice…

## g0112（1 列）
- 見出し：PostalCode_CodePostal
- 例1 値：_National | _National | _National | A | A
  - 同じ表の列：ActivitySector_Sect…, ReportType_TypeDeDé…, YearMonthReportRece…, NumberOfReports_Nom…, FiscalYear_Exercice…

## g0113（1 列）
- 見出し：ReportType_TypeDeDéclaration
- 例1 値：STR_DOD | STR_DOD | EFT_télévirements | EFT_télévirements | LCTR_DOIE
  - 同じ表の列：ActivitySector_Sect…, PostalCode_CodePost…, YearMonthReportRece…, NumberOfReports_Nom…, FiscalYear_Exercice…

## g0114（1 列）
- 見出し：YearMonthReportReceived_AnnéeMoisDéclarationReçue
- 例1 値：201510 | 201903 | 201106 | 201305 | 202003
  - 同じ表の列：ActivitySector_Sect…, PostalCode_CodePost…, ReportType_TypeDeDé…, NumberOfReports_Nom…, FiscalYear_Exercice…

## g0115（1 列）
- 見出し：NumberOfReports_NombreDeDéclarations
- 例1 値：1 | 12306 | 11 | 31 | 10016
  - 同じ表の列：ActivitySector_Sect…, PostalCode_CodePost…, ReportType_TypeDeDé…, YearMonthReportRece…, FiscalYear_Exercice…

## g0116（1 列）
- 見出し：FiscalYear_ExerciceFinancier
- 例1 値：2016-2017 | 2023-2024 | 2021-2022 | 2020-2021 | 2015-2016
  - 同じ表の列：ActivitySector_Sect…, PostalCode_CodePost…, ReportType_TypeDeDé…, YearMonthReportRece…, NumberOfReports_Nom…

## g0117（1 列）
- 見出し：Application number
- 例1 値：2004-1616 | 2004-0171 | 2005-2273 | 2004-0166 | 2002-2842
  - 同じ表の列：Date received, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration number, Registration status, Category

## g0118（1 列）
- 見出し：Date received
- 例1 値：2005-12-07 | 2005-12-30 | 2005-12-28 | 2005-12-07 | 2005-12-15
  - 同じ表の列：Application number, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration number, Registration status, Category

## g0119（1 列）
- 見出し：Outcome
- 例1 値：COMPLETED | COMPLETED | REGISTERED | REGISTERED | REGISTERED
  - 同じ表の列：Application number, Date received, Active ingredients …, Active ingredients …, Purpose, Registration number, Registration status, Category

## g0120（1 列）
- 見出し：Active ingredients - English
- 例1 値：DEVICE, NO GUARANTEE REQUIRED | SIMAZINE PLUS RELATED ACTIVE TRIAZINES | IMAZAMETHABENZ-METHYL | N-ALKYL (50% C12, 30% C14, 17% C16, 3% … | PIPERONYL BUTOXIDE;PYRETHRINS
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Purpose, Registration number, Registration status, Category

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
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
