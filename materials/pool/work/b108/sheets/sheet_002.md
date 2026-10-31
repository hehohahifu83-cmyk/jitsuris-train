# ラベル用シート 002 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Persons with disabilities Personnes handicapées
- 例1 値：1.90% | 1.80% | 0.80% | 3.50% | 2.00%
  - 同じ表の列：Year Année (as of M…, Visible Minorities …, Aboriginal Peoples …, Women Femmes

## g0122（1 列）
- 見出し：Women Femmes
- 例1 値：48.30% | 45.60% | 49.60% | 46.20% | 44.00%
  - 同じ表の列：Year Année (as of M…, Visible Minorities …, Aboriginal Peoples …, Persons with disabi…

## g0123（2 列）
- 見出し：SP_QUAL
- 例1 値：LAKE TYPE SOCKEYE SALMON | CHINOOK SALMON | EVEN YEAR PINK SALMON | COHO SALMON | LAKE TYPE SOCKEYE SALMON
  - 同じ表の列：CENSUS_SITE, POP_ID
- 例2 値：CHUM SALMON | CHINOOK SALMON | LAKE TYPE SOCKEYE SALMON | LAKE TYPE SOCKEYE SALMON | CHUM SALMON
  - 同じ表の列：CENSUS_SITE, POP_ID

## g0124（1 列）
- 見出し：CENSUS_SITE
- 例1 値：NASPARTI RIVER | SOOKE RIVER | COMO CREEK | SETON RIVER | COLONIAL CREEK
  - 同じ表の列：SP_QUAL, POP_ID

## g0125（2 列）
- 見出し：POP_ID
- 例1 値：3448 | 3432 | 208 | 40732 | 39756
  - 同じ表の列：SP_QUAL, CENSUS_SITE
- 例2 値：3056 | 208 | 39897 | 39910 | 3090
  - 同じ表の列：SP_QUAL, CENSUS_SITE

## g0126（1 列）
- 見出し：CENSUS_SITE
- 例1 値：EAST CREEK | CRUICKSHANK POINT WEST | MONKEY CREEK | SKIMLETS CREEK | FOUR MILE CREEK
  - 同じ表の列：SP_QUAL, POP_ID

## g0127（1 列）
- 見出し：Fiscal years/ Années fiscales
- 例1 値：2019-2020 | Notes: * - As the Quality of Life Surve… | Notes : * - Comme l'Enquête sur la qual… | 2018-2019 | ** - Compte tenu des périodes d'enquête…
  - 同じ表の列：Department result/ …, Department results …, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0128（1 列）
- 見出し：Department result/ Résultats départementaux
- 例1 値：3.4 Military families are supported and…
  - 同じ表の列：Fiscal years/ Année…, Department results …, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0129（1 列）
- 見出し：Department results indicators/ Indicateurs de résultats dépa
- 例1 値：3.4.2 % of Canadian Armed Forces member…
  - 同じ表の列：Fiscal years/ Année…, Department result/ …, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0130（1 列）
- 見出し：Target/ Cible
- 例1 値：85%
  - 同じ表の列：Fiscal years/ Année…, Department result/ …, Department results …, Date to achieve tar…, Actual results/ Rés…

## g0131（1 列）
- 見出し：Date to achieve target/ Date d'atteinte de l'objectif
- 例1 値：2021-03-31 | 2021-03-31 | 2021-03-31
  - 同じ表の列：Fiscal years/ Année…, Department result/ …, Department results …, Target/ Cible, Actual results/ Rés…

## g0132（1 列）
- 見出し：Actual results/ Résultats actuels
- 例1 値：71.0% | 67.4%* | 67.4%*
  - 同じ表の列：Fiscal years/ Année…, Department result/ …, Department results …, Target/ Cible, Date to achieve tar…

## g0133（1 列）
- 見出し：Experience
- 例1 値：Senior | Senior | Junior | Junior | Senior
  - 同じ表の列：Difficulty, Importance, Timeframe_5levels, Timeframe_binary, Outcome, Forecast, Brier_score

## g0134（1 列）
- 見出し：Difficulty
- 例1 値：Harder | Easier | Easier | Easier | Easier
  - 同じ表の列：Experience, Importance, Timeframe_5levels, Timeframe_binary, Outcome, Forecast, Brier_score

## g0135（1 列）
- 見出し：Importance
- 例1 値：Lower | Lower | Higher | Higher | Higher
  - 同じ表の列：Experience, Difficulty, Timeframe_5levels, Timeframe_binary, Outcome, Forecast, Brier_score

## g0136（1 列）
- 見出し：Timeframe_5levels
- 例1 値：6 MONTHS TO 1 YEAR | UP TO 1 MONTH | UP TO 1 MONTH | 3-6 MONTH | 3-6 MONTH
  - 同じ表の列：Experience, Difficulty, Importance, Timeframe_binary, Outcome, Forecast, Brier_score

## g0137（1 列）
- 見出し：Timeframe_binary
- 例1 値：Up to 6 months | Up to 6 months | More than 6 months | More than 6 months | More than 6 months
  - 同じ表の列：Experience, Difficulty, Importance, Timeframe_5levels, Outcome, Forecast, Brier_score

## g0138（1 列）
- 見出し：Outcome
- 例1 値：Did not occur | Did occur | Did occur | Did occur | Did occur
  - 同じ表の列：Experience, Difficulty, Importance, Timeframe_5levels, Timeframe_binary, Forecast, Brier_score

## g0139（1 列）
- 見出し：Forecast
- 例1 値：0.75 | 0.75 | 0.75 | 0.1 | 1
  - 同じ表の列：Experience, Difficulty, Importance, Timeframe_5levels, Timeframe_binary, Outcome, Brier_score

## g0140（1 列）
- 見出し：Brier_score
- 例1 値：0.0625 | 0 | 0.01 | 0.0625 | 0.0625
  - 同じ表の列：Experience, Difficulty, Importance, Timeframe_5levels, Timeframe_binary, Outcome, Forecast

## g0141（1 列）
- 見出し：NDA Section
- 例1 値：90 | 130 (430 CC) | 108 | 127 | 95
  - 同じ表の列：2019-2020, 2020-2021

## g0142（1 列）
- 見出し：2019-2020
- 例1 値：0 | # | 50 | 128 | 9
  - 同じ表の列：NDA Section, 2020-2021

## g0143（1 列）
- 見出し：2020-2021
- 例1 値：23 | 21 | 1 | 1 | #
  - 同じ表の列：NDA Section, 2019-2020

## g0144（1 列）
- 見出し：Table|Tableau
- 例1 値：Species_Codes_Espèces.csv | Other_Codes_Autres.csv | Data_Dictionary_Dictionaire_Donnés.csv | Point_Count_Data_Données_Point d’écoute… | Stations_Points_d’écoute.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0145（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | Longitude|Longitude | Station|Station | n/a | Latitude|Latitude
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0146（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：QUADRANT | DISTANCE | DISTANCE | NULL_exists|NULL_existe | BEHAVIOUR
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0147（1 列）
- 見出し：Table|Tableau
- 例1 値：Point_count_data_Données_point_d’écoute… | Point_Count_Data_Données_Point d’écoute… | Point_count_data_Données_point_d’écoute… | Point_count_data_Données_point_d’écoute… | Species_Codes_Espèces.csv
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0148（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：n/a | Observer ID|ID de l’observateur | Minute|Minute | Quadrant in 2nd interval|Quadrant dans … | Distance in 2nd interval|Distance dans …
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0149（1 列）
- 見出し：Table|Tableau
- 例1 値：Point_count_data_Données_point_d’écoute… | Point_count_data_Données_point_d’écoute… | Data_Dictionary_Dictionaire_Donnés.csv | Point_count_data_Données_point_d’écoute… | Point_count_data_Données_point_d’écoute…
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0150（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：Station|Point d’écoute | Distance 1|Distance 1 | Comments-point count|Commentaires sur l… | Number|Nombre | Site|Site
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0151（1 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：Det_Type | NULL_exists|NULL_existe | Det_Type | Species_Codes_Espèces.csv | Distance
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0152（1 列）
- 見出し：Geocode|Géocode
- 例1 値：3543064 | 3532038 | 3534024 | 3530004 | 3512005
  - 同じ表の列：Geography|Géographie, 2016, 2017

## g0153（1 列）
- 見出し：Geography|Géographie
- 例1 値：Hiawatha First Nation, Ontario | Collingwood, Ontario | Shelburne, Ontario | Asphodel-Norwood, Ontario | Madoc, Ontario
  - 同じ表の列：Geocode|Géocode, 2016, 2017

## g0154（1 列）
- 見出し：2016
- 例1 値：77 | 95 | 153 | 172 | 11183
  - 同じ表の列：Geocode|Géocode, Geography|Géographie, 2017

## g0155（1 列）
- 見出し：2017
- 例1 値：141 | 97 | 642 | 185 | 177
  - 同じ表の列：Geocode|Géocode, Geography|Géographie, 2016

## g0156（1 列）
- 見出し：Incorporation Status Statue d'incorporation
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0157（1 列）
- 見出し：Naics_code Code_SCIAN
- 例1 値：55 | 419 | 113 | 55 | 412
  - 同じ表の列：Incorporation Statu…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0158（1 列）
- 見出し：Province Canada
- 例1 値：61 | 47 | 35 | 59 | 11
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0159（1 列）
- 見出し：Whole Industry (Reliability) Industrie entière (fiabilité)
- 例1 値：57315 | 363 | 28 | 999999 | 41
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0160（1 列）
- 見出し：Whole industry low revenue range Intervalles de revenu minim
- 例1 値：9999 | 30 | 30 | 30 | 9999
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0161（1 列）
- 見出し：Whole industry High revenue range Intervalles de revenue max
- 例1 値：5000 | 9999 | 5000 | 5000 | 5000
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Bottom quartile Low…, Bottom quartile Hig…, Top quartile Low re…

## g0162（1 列）
- 見出し：Bottom quartile Low revenue range Quart inférieur Intervalle
- 例1 値：9999 | 30 | 30 | 30 | 9999
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Hig…, Top quartile Low re…

## g0163（1 列）
- 見出し：Bottom quartile High revenue range 2e quart Intervalles de r
- 例1 値：41 | 45 | 44 | 9999 | 9999
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Top quartile Low re…

## g0164（1 列）
- 見出し：Top quartile Low revenue range Quart supérieur invertalle de
- 例1 値：140 | 9999 | 138 | 158 | 77
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…

## g0165（1 列）
- 見出し：Top quartile High revenue range Quart supérieur invertalle d
- 例1 値：9999 | 9999 | 9999 | 5000 | 5000
  - 同じ表の列：Incorporation Statu…, Naics_code Code_SCI…, Province Canada, Whole Industry (Rel…, Whole industry low …, Whole industry High…, Bottom quartile Low…, Bottom quartile Hig…

## g0166（1 列）
- 見出し：HS6-SH6
- 例1 値：30193 | 20629 | 30369 | 30289 | 20130
  - 同じ表の列：COMPANY-ENTREPRISE, CITY-VILLE, PROVINCE_ENG, PROVINCE_FRA, DATA_YEAR-ANNÉE_DES…

## g0167（1 列）
- 見出し：COMPANY-ENTREPRISE
- 例1 値：CAVEL CANADA EXPORT, INC | HAI YANG INTERNATIONAL INC | LA COMPAGNIE DE POISSONS DE MONTREAL LT… | CANADIAN FISHING COMPANY GROUP B | BLUNDELL SEAFOODS LTD.
  - 同じ表の列：HS6-SH6, CITY-VILLE, PROVINCE_ENG, PROVINCE_FRA, DATA_YEAR-ANNÉE_DES…

## g0168（1 列）
- 見出し：CITY-VILLE
- 例1 値：Mississauga | Kirkland | Langley | Montréal | Lachine
  - 同じ表の列：HS6-SH6, COMPANY-ENTREPRISE, PROVINCE_ENG, PROVINCE_FRA, DATA_YEAR-ANNÉE_DES…

## g0169（1 列）
- 見出し：PROVINCE_ENG
- 例1 値：Quebec | British Columbia | Quebec | Nova Scotia | Saskatchewan
  - 同じ表の列：HS6-SH6, COMPANY-ENTREPRISE, CITY-VILLE, PROVINCE_FRA, DATA_YEAR-ANNÉE_DES…

## g0170（1 列）
- 見出し：PROVINCE_FRA
- 例1 値：Colombie-Britannique | Saskatchewan | Saskatchewan | Colombie-Britannique | Alberta
  - 同じ表の列：HS6-SH6, COMPANY-ENTREPRISE, CITY-VILLE, PROVINCE_ENG, DATA_YEAR-ANNÉE_DES…

## g0171（1 列）
- 見出し：DATA_YEAR-ANNÉE_DES_DONNÉES
- 例1 値：2012 | 2012 | 2012 | 2012 | 2012
  - 同じ表の列：HS6-SH6, COMPANY-ENTREPRISE, CITY-VILLE, PROVINCE_ENG, PROVINCE_FRA

## g0172（1 列）
- 見出し：PNuid_NLidu
- 例1 値：819 | 186 | 169 | 759 | 306
  - 同じ表の列：Nom_fr, Province

## g0173（1 列）
- 見出し：Nom_fr
- 例1 値：Charleston | Sheet Harbour Passage | Ecum Secum Bridge | Florence | Knutsford
  - 同じ表の列：PNuid_NLidu, Province

## g0174（1 列）
- 見出し：NOM DE LA COLONNE
- 例1 値：Date de la photographie | Province ou territoire | ProductName | SLevelPS | HighPS
  - 同じ表の列：TYPE DE DONNÉE

## g0175（1 列）
- 見出し：TYPE DE DONNÉE
- 例1 値：Nombre | Nombre | Nombre | Texte | Texte
  - 同じ表の列：NOM DE LA COLONNE

## g0176（1 列）
- 見出し：Numéro de suivi / Tracking number
- 例1 値：OCS2236 | HB109 | MIN-BR32 | FC8845 | FC8634
  - 同じ表の列：Titre - Anglais / T…, Titre - Français / …, Secteur d'origine -…, Secteur d'origine -…, Date de réception /…, Mesure requise / Ac…

## g0177（1 列）
- 見出し：Titre - Anglais / Title- English
- 例1 値：Nomination of Director to the First Nat… | Nomination of Chairperson to the First … | Daylu Dena Council administration build… | 10-Year Grant - New Recommendations for… | Indigenous Homes Innovation Initiatives…
  - 同じ表の列：Numéro de suivi / T…, Titre - Français / …, Secteur d'origine -…, Secteur d'origine -…, Date de réception /…, Mesure requise / Ac…

## g0178（1 列）
- 見出し：Titre - Français / Title - French
- 例1 値：Rencontre de Bilan - 4 mars 2019 | Mise à jour sur le financement du bien-… | Table à Grassy Narrows | *caviardé* | Outil de suivi des sujets chauds de la …
  - 同じ表の列：Numéro de suivi / T…, Titre - Anglais / T…, Secteur d'origine -…, Secteur d'origine -…, Date de réception /…, Mesure requise / Ac…

## g0179（1 列）
- 見出し：Secteur d'origine - Anglais / Originating sector - English
- 例1 値：Lands and Economic Development Sector | Chief Finances, Results and Delivery Of… | Ontario Region | First Nations and Inuit Health Branch | Chief Finances, Results and Delivery Of…
  - 同じ表の列：Numéro de suivi / T…, Titre - Anglais / T…, Titre - Français / …, Secteur d'origine -…, Date de réception /…, Mesure requise / Ac…

## g0180（1 列）
- 見出し：Secteur d'origine - Français / Originating sector - French
- 例1 値：Secteur des Opérations régionales | Secteur des Terres et développement éco… | Secteur des Terres et développement éco… | Région de l'Ontario | Secteur de la Réforme des services à l'…
  - 同じ表の列：Numéro de suivi / T…, Titre - Anglais / T…, Titre - Français / …, Secteur d'origine -…, Date de réception /…, Mesure requise / Ac…

## g0181（1 列）
- 見出し：Date de réception / Date received
- 例1 値：04/29/2019 | 04/02/2019 | 04/15/2019 | 04/15/2019 | 04/01/2019
  - 同じ表の列：Numéro de suivi / T…, Titre - Anglais / T…, Titre - Français / …, Secteur d'origine -…, Secteur d'origine -…, Mesure requise / Ac…

## g0182（1 列）
- 見出し：Mesure requise / Action required
- 例1 値：Information | Decision | Information | Decision | Information
  - 同じ表の列：Numéro de suivi / T…, Titre - Anglais / T…, Titre - Français / …, Secteur d'origine -…, Secteur d'origine -…, Date de réception /…

## g0183（1 列）
- 見出し：Annee financiere - Fiscal year
- 例1 値：2017-18 | 2017-18 | 2017-18 | 2017-18 | 2017-18
  - 同じ表の列：Trimestre - Quarter, Mois - Months, Nombre de telecharg…

## g0184（1 列）
- 見出し：Trimestre - Quarter
- 例1 値：T2 | T2 | T4 | T1 | T3
  - 同じ表の列：Annee financiere - …, Mois - Months, Nombre de telecharg…

## g0185（1 列）
- 見出し：Mois - Months
- 例1 値：Fevrier | Novembre | Decembre | Juin | Avril
  - 同じ表の列：Annee financiere - …, Trimestre - Quarter, Nombre de telecharg…

## g0186（1 列）
- 見出し：Nombre de telechargements d’items sur le site Web de BAC (ne
- 例1 値：976045 | 867057 | 925843 | 624919 | 883318
  - 同じ表の列：Annee financiere - …, Trimestre - Quarter, Mois - Months

## g0187（1 列）
- 見出し：TITLE / TITRE
- 例1 値：Optimizing the electrical conductivity … | Long-term performance of a microbial el… | Real-time large-scale fusion of high re… | Another unprecedented Wieland mechanism… | Advances in the uncertainty evaluation …
  - 同じ表の列：AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0188（1 列）
- 見出し：AUTHOR_DISPLAY / AFFICHE_AUTEUR
- 例1 値：Hill, Alex S.|Mac Low, Mordecai-Mark|Ga… | Littell, Patrick|Kazantseva, Anna|Kuhn,… | Knox, Paul | Osman, A.|Soler-Penades, J.|Sanchez-Pos… | Kratzer, Jan|Musil, Stanislav|Marschner…
  - 同じ表の列：TITLE / TITRE, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0189（1 列）
- 見出し：JOURNAL_TITLE / TITRE_REVUE
- 例1 値：Water Resources Management | Current Metabolomics | Scientific Reports | ACS Omega | IEEE Journal of Radio Frequency Identif…
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0190（1 列）
- 見出し：VOLUME / VOLUME
- 例1 値：32 | 164 | 8 | 65 | 78
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0191（1 列）
- 見出し：ISSUE / NUMÉRO
- 例1 値：1 | 8 | 11 | 24 | 6
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0192（1 列）
- 見出し：START_PAGE / PAGE_DÉBUT
- 例1 値：2669 | 1 | 5288 | 238 | 267
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0193（1 列）
- 見出し：END_PAGE / PAGE_FIN
- 例1 値：827 | 3666 | 86 | 1651 | 424
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, ARTICLE NUMBER / NU…, YEAR / ANNÉE

## g0194（1 列）
- 見出し：ARTICLE NUMBER / NUMÉRO_ARTICLE
- 例1 値：138454 | 2018-01-1213 | 9.54E+13 | e0190681 | e0208978
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, YEAR / ANNÉE

## g0195（1 列）
- 見出し：YEAR / ANNÉE
- 例1 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…

## g0196（1 列）
- 見出し：DATE_PUBLISHED / DATE_PUBLICATION
- 例1 値：2018-10-12 | 2018-10-01 | 2018-01-01 | 2018-06-20 | 2018-11-05
  - 同じ表の列：TITLE / TITRE, AUTHOR_DISPLAY / AF…, JOURNAL_TITLE / TIT…, VOLUME / VOLUME, ISSUE / NUMÉRO, START_PAGE / PAGE_D…, END_PAGE / PAGE_FIN, ARTICLE NUMBER / NU…

## g0197（1 列）
- 見出し：REGION
- 例1 値：28 | 14 | 1 | 10 | 12
  - 同じ表の列：REGION_NOM, 11, 12, 13, 14, 15, 16, 17

## g0198（1 列）
- 見出し：REGION_NOM
- 例1 値：Arctique oriental - Zone extracotiere | Sud du Labrador | Sud des Grands bancs | Ouest du plateau Scotian | Détroit Hecate
  - 同じ表の列：REGION, 11, 12, 13, 14, 15, 16, 17

## g0199（1 列）
- 見出し：11
- 例1 値：0.0533 | 0 | 0 | 0.0183 | 0.0662
  - 同じ表の列：REGION, REGION_NOM, 12, 13, 14, 15, 16, 17

## g0200（1 列）
- 見出し：12
- 例1 値：0 | 0.0507 | 0.0507 | 0 | 0
  - 同じ表の列：REGION, REGION_NOM, 11, 13, 14, 15, 16, 17

## g0201（1 列）
- 見出し：13
- 例1 値：0 | 0.0789 | 0.0849 | 0 | 0
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 14, 15, 16, 17

## g0202（1 列）
- 見出し：14
- 例1 値：0.0579 | 0.0823 | 0.0579 | 0 | 0.0579
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 13, 15, 16, 17

## g0203（1 列）
- 見出し：15
- 例1 値：0.1468 | 0 | 0.0931 | 0 | 0
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 13, 14, 16, 17

## g0204（1 列）
- 見出し：16
- 例1 値：0 | 0 | 0.107 | 0 | 0.1109
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 13, 14, 15, 17

## g0205（1 列）
- 見出し：17
- 例1 値：0 | 0 | 0.0154 | 0.0662 | 0.06
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 13, 14, 15, 16

## g0206（1 列）
- 見出し：18
- 例1 値：0.0707 | 0.0816 | 0.0712 | 0 | 0.2626
  - 同じ表の列：REGION, REGION_NOM, 11, 12, 13, 14, 15, 16

## g0207（1 列）
- 見出し：id
- 例1 値：5 | 19 | 6 | 14 | 9
  - 同じ表の列：Nom, Période, Matériel supplément…, Descripteur des don…, Étendue, Type de données, Données manquantes

## g0208（1 列）
- 見出し：Nom
- 例1 値：CanLaBS_NBR1000_post_v0.tif | CanLaBS_dNBR1000_v0.tif | CanLaBS_B4_post_v0.tif | CanLaBS_B4_pre_v0.tif | CanLaBS_B5_pre_v0.tif
  - 同じ表の列：id, Période, Matériel supplément…, Descripteur des don…, Étendue, Type de données, Données manquantes

## g0209（1 列）
- 見出し：Période
- 例1 値：après feu | avant feu | après feu | année du feu | avant feu
  - 同じ表の列：id, Nom, Matériel supplément…, Descripteur des don…, Étendue, Type de données, Données manquantes

## g0210（1 列）
- 見出し：Matériel supplémentaire
- 例1 値：cjfr-2020-0353supplc | cjfr-2020-0353supplb | cjfr-2020-0353supplc | cjfr-2020-0353supplb | cjfr-2020-0353supplb
  - 同じ表の列：id, Nom, Période, Descripteur des don…, Étendue, Type de données, Données manquantes

## g0211（1 列）
- 見出し：Descripteur des données
- 例1 値：Landsat | Année | Landsat | Prediction random forest | Landsat
  - 同じ表の列：id, Nom, Période, Matériel supplément…, Étendue, Type de données, Données manquantes

## g0212（1 列）
- 見出し：Étendue
- 例1 値：0-94 | 0-90 | 0-99 | 1985-2015 | 0-94
  - 同じ表の列：id, Nom, Période, Matériel supplément…, Descripteur des don…, Type de données, Données manquantes

## g0213（1 列）
- 見出し：Type de données
- 例1 値：Int16 | Int16 | Int16 | Byte | Int16
  - 同じ表の列：id, Nom, Période, Matériel supplément…, Descripteur des don…, Étendue, Données manquantes

## g0214（1 列）
- 見出し：Données manquantes
- 例1 値：255 | 255 | -32768 | -32768 | -32768
  - 同じ表の列：id, Nom, Période, Matériel supplément…, Descripteur des don…, Étendue, Type de données

## g0215（1 列）
- 見出し：Number of participants in National Indigenous Peoples Day co
- 例1 値：Number of participants in Saint-Jean-Ba… | Number of participants for Winterlude | Number of participants in Canadian Mult… | Number of volunteers that contribute to… | Number of participants for the Sound an…
  - 同じ表の列：320073

## g0216（1 列）
- 見出し：320073
- 例1 値：163300 | 206700 | 5445428 | 1537 | 350000
  - 同じ表の列：Number of participa…

## g0217（2 列）
- 見出し：pruid
- 例1 値：1 | 35 | 59 | 62 | 59
  - 同じ表の列：week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially
- 例2 値：99 | 10 | 35 | 62 | 59
  - 同じ表の列：date, reporting_week, reporting_year, update, totalcases, ratecases_total, numdeaths, ratedeaths

## g0218（1 列）
- 見出し：week_end
- 例1 値：2021-05-22 | 2021-05-08 | 2021-01-16 | 2021-05-22 | 2021-05-08
  - 同じ表の列：pruid, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0219（1 列）
- 見出し：series_type
- 例1 値：3 | 1 | 3 | 1 | 2
  - 同じ表の列：pruid, week_end, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0220（1 列）
- 見出し：primary_series
- 例1 値：Moderna Spikevax | AstraZeneca Vaxzevria/COVISHIELD | Unknown | Not reported | Moderna Spikevax
  - 同じ表の列：pruid, week_end, series_type, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0221（1 列）
- 見出し：numtotal_atleast1dose
- 例1 値：54645 | 55702 | 14664 | 54503 | 175085
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0222（1 列）
- 見出し：numtotal_partially
- 例1 値：na | 253504 | 2177 | 3540 | 3431630
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_fully, prop_atleast1dose, prop_partially

## g0223（1 列）
- 見出し：numtotal_fully
- 例1 値：26 | 14469 | 0 | 0 | 25
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, prop_atleast1dose, prop_partially

## g0224（1 列）
- 見出し：prop_atleast1dose
- 例1 値：1.4 | 0.1 | 6 | 16.7 | 13.9
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_partially

## g0225（1 列）
- 見出し：prop_partially
- 例1 値：7.3 | 8.6 | 10.6 | 1.7 | 1.7
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose

## g0226（1 列）
- 見出し：prop_fully
- 例1 値：0.5 | 0.8 | 0.8 | <0.1 | 2.7
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose

## g0227（2 列）
- 見出し：Date
- 例1 値：2020-10-06 | 2020-05-21 | 2020-04-23 | 2022-11-19 | 2020-11-09
  - 同じ表の列：BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER, COVID_OTHER
- 例2 値：2021-02-20 | 2020-02-08 | 2021-04-10 | 2020-02-29 | 2020-11-14
  - 同じ表の列：pruid, reporting_week, reporting_year, update, totalcases, ratecases_total, numdeaths, ratedeaths

## g0228（1 列）
- 見出し：BEDCAP_ICU
- 例1 値：5183 | 5352 | 6488 | 5187 | 6488
  - 同じ表の列：Date, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER, COVID_OTHER

## g0229（1 列）
- 見出し：VENTCAP_ICU
- 例1 値：3320 | 3200 | 3813 | 3963 | 3528
  - 同じ表の列：Date, BEDCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER, COVID_OTHER

## g0230（1 列）
- 見出し：BEDCAP_OTHER
- 例1 値：58254 | 58587 | 61728 | 58304 | 58826
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER, COVID_OTHER

## g0231（1 列）
- 見出し：VENTCAP_OTHER
- 例1 値：991 | 849 | 975 | 1108 | 866
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER, COVID_OTHER

## g0232（1 列）
- 見出し：COVID_NEWICU
- 例1 値：25 | 4 | 3 | 13 | 20
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_ICU, COVID_NEWOTHER, COVID_OTHER

## g0233（1 列）
- 見出し：COVID_ICU
- 例1 値：532 | 270 | 237 | 355 | 181
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_NEWOTHER, COVID_OTHER

## g0234（1 列）
- 見出し：COVID_NEWOTHER
- 例1 値：26 | 586 | 13 | 276 | 211
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_OTHER

## g0235（1 列）
- 見出し：COVID_OTHER
- 例1 値：3250 | 261 | 5530 | 4858 | 1807
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER

## g0236（1 列）
- 見出し：COVID_VENT
- 例1 値：111 | 110 | 172 | 117 | 203
  - 同じ表の列：Date, BEDCAP_ICU, VENTCAP_ICU, BEDCAP_OTHER, VENTCAP_OTHER, COVID_NEWICU, COVID_ICU, COVID_NEWOTHER

## g0237（1 列）
- 見出し：reporting_week
- 例1 値：6 | 43 | 34 | 14 | 31
  - 同じ表の列：pruid, date, reporting_year, update, totalcases, ratecases_total, numdeaths, ratedeaths

## g0238（1 列）
- 見出し：reporting_year
- 例1 値：2021 | 2021 | 2020 | 2021 | 2021
  - 同じ表の列：pruid, date, reporting_week, update, totalcases, ratecases_total, numdeaths, ratedeaths

## g0239（1 列）
- 見出し：update
- 例1 値：1.0 | 1.0 | 1.0 | 1.0 | 1.0
  - 同じ表の列：pruid, date, reporting_week, reporting_year, totalcases, ratecases_total, numdeaths, ratedeaths

## g0240（1 列）
- 見出し：totalcases
- 例1 値：124639 | 218835 | 70841 | 20750 | 152176
  - 同じ表の列：pruid, date, reporting_week, reporting_year, update, ratecases_total, numdeaths, ratedeaths

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
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
