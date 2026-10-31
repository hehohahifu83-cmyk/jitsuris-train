# ラベル用シート 001 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Table|Tableau
- 例1 値：Data_Données | Data_Dictionary_Dictionaire_Donnés | Data_Dictionary_Dictionaire_Donnés | Data_Données | Species_Codes_Espèces
  - 同じ表の列：Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0002（1 列）
- 見出し：Field_alias_geospatial|Alias_champ_géospatial
- 例1 値：Start minute|Minute de début | Number|Nombre | n/a | Sex|Sexe | n/a
  - 同じ表の列：Table|Tableau, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0003（4 列）
- 見出し：Data_type_en
- 例1 値：text | text | text | text | short integer
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：text | short integer | text | text | text
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0004（4 列）
- 見出し：Type_de_données_fr
- 例1 値：texte | texte | entier court | texte | texte
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：texte | texte | entier court | texte | entier court
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, NULL_exists|NULL_ex…, Field_length|Longue…, Values_lookup|Reche…

## g0005（4 列）
- 見出し：NULL_exists|NULL_existe
- 例1 値：N|N | N|N | N|N | N|N | Y|O
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…
- 例2 値：Y|O | Y|O | N|N | N|N | N|N
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, Field_length|Longue…, Values_lookup|Reche…

## g0006（4 列）
- 見出し：Field_length|Longueur_du_champ
- 例1 値：110 | 3 | 8 | 3 | 4
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Values_lookup|Reche…
- 例2 値：3 | 19 | 45 | 1 | 2
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Values_lookup|Reche…

## g0007（2 列）
- 見出し：Values_lookup|Recherche_de_valeurs
- 例1 値：AGE | NULL_exists|NULL_existe | SEX | Species_Codes_Espèces.csv | BEHAVIOUR
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…
- 例2 値：Age | Behaviour | Quadrant | Species_Codes_Espèces.csv | NULL_exists|NULL_existe
  - 同じ表の列：Table|Tableau, Field_alias_geospat…, Data_type_en, Type_de_données_fr, NULL_exists|NULL_ex…, Field_length|Longue…

## g0008（1 列）
- 見出し：FEDERAL COURT OF APPEAL (FCA)
- 例1 値：Crown | Total | Scheduled for hearing | Goods and Services Tax | Total
  - 同じ表の列：Cour d’appel fédéra…, 2017–18, 2016–17, 2015–16, 2014–15, 2013–14

## g0009（1 列）
- 見出し：Cour d’appel fédérale (CAF)
- 例1 値：Audiences prévues | Jours d’audience | Jugements ordonnances et directives tra… | Instances à gestion spéciale | Regroupées
  - 同じ表の列：FEDERAL COURT OF AP…, 2017–18, 2016–17, 2015–16, 2014–15, 2013–14

## g0010（1 列）
- 見出し：2017–18
- 例1 値：177431 | 3 | 2463 | 492 | 7440
  - 同じ表の列：FEDERAL COURT OF AP…, Cour d’appel fédéra…, 2016–17, 2015–16, 2014–15, 2013–14

## g0011（1 列）
- 見出し：2016–17
- 例1 値：53 | 3238 | 4 | 137 | 0
  - 同じ表の列：FEDERAL COURT OF AP…, Cour d’appel fédéra…, 2017–18, 2015–16, 2014–15, 2013–14

## g0012（1 列）
- 見出し：2015–16
- 例1 値：33 | 19 | 252 | 132 | 2015–16
  - 同じ表の列：FEDERAL COURT OF AP…, Cour d’appel fédéra…, 2017–18, 2016–17, 2014–15, 2013–14

## g0013（1 列）
- 見出し：2014–15
- 例1 値：5 | 24474 | 55 | 2213 | 179
  - 同じ表の列：FEDERAL COURT OF AP…, Cour d’appel fédéra…, 2017–18, 2016–17, 2015–16, 2013–14

## g0014（1 列）
- 見出し：2013–14
- 例1 値：10 | 7784 | 177342 | 0 | 2214
  - 同じ表の列：FEDERAL COURT OF AP…, Cour d’appel fédéra…, 2017–18, 2016–17, 2015–16, 2014–15

## g0015（1 列）
- 見出し：EDI Message Number Numéro du message EDI
- 例1 値：118 | A38 | 139 | D13 | 329
  - 同じ表の列：Element ID ID de l’…, Message Number Numé…, Group Groupe, Message Text Messag…, French Message Text…

## g0016（1 列）
- 見出し：Element ID ID de l’élément
- 例1 値：4562 | 4110 | 4357 | 1622 | 1194
  - 同じ表の列：EDI Message Number …, Message Number Numé…, Group Groupe, Message Text Messag…, French Message Text…

## g0017（1 列）
- 見出し：Message Number Numéro du message
- 例1 値：100240 | 100226 | 100226 | 100227 | 100010
  - 同じ表の列：EDI Message Number …, Element ID ID de l’…, Group Groupe, Message Text Messag…, French Message Text…

## g0018（1 列）
- 見出し：Group Groupe
- 例1 値：Validation | Validation | Validation | Validation | Validation
  - 同じ表の列：EDI Message Number …, Element ID ID de l’…, Message Number Numé…, Message Text Messag…, French Message Text…

## g0019（1 列）
- 見出し：Message Text Message Texte
- 例1 値：NUMBER OF OCCURRENCES EXCEEDS MAXIMUM | FIELD IS NOT VALID | NUMBER OF OCCURENCES EXCEEDS MAXIMUM | FIELD IS NOT VALID | FIELD MUST BE NUMERIC
  - 同じ表の列：EDI Message Number …, Element ID ID de l’…, Message Number Numé…, Group Groupe, French Message Text…

## g0020（1 列）
- 見出し：French Message Text Message Texte (français)
- 例1 値：NOMBRE D'EVENEMENTS DEPASSE LE MAXIMUM … | ZONE EST OBLIGATOIRE | FORMAT NUMERIQUE EST INVALIDE | ZONE EST INVALIDE | NOMBRE D'EVENEMENTS DEPASSE LE MAXIMUM …
  - 同じ表の列：EDI Message Number …, Element ID ID de l’…, Message Number Numé…, Group Groupe, Message Text Messag…

## g0021（1 列）
- 見出し：Regions
- 例1 値：Prairies/NT Region | Source: CIC DWS - Enforcement - Removal… | Ontario Region | Atlantic Region | Total Removals Executed
  - 同じ表の列：2009, 2010, 2011, 2012, 2013

## g0022（1 列）
- 見出し：2009
- 例1 値：14,859 | 4,328 | 1,816 | 5 | 734
  - 同じ表の列：Regions, 2010, 2011, 2012, 2013

## g0023（1 列）
- 見出し：2010
- 例1 値：85 | 707 | 8,231 | 15,378 | 2,118
  - 同じ表の列：Regions, 2009, 2011, 2012, 2013

## g0024（1 列）
- 見出し：2011
- 例1 値：3,705 | 2,418 | 10 | 896 | 15,684
  - 同じ表の列：Regions, 2009, 2010, 2012, 2013

## g0025（1 列）
- 見出し：2012
- 例1 値：4,199 | 4 | 18,921 | 1,053 | 10,830
  - 同じ表の列：Regions, 2009, 2010, 2011, 2013

## g0026（1 列）
- 見出し：2013
- 例1 値：967 | 15,232 | 7,902 | 4,140 | 116
  - 同じ表の列：Regions, 2009, 2010, 2011, 2012

## g0027（1 列）
- 見出し：Bureau de l'ASFC
- 例1 値：Aldergrove | Lacolle: Route 221 | Prescott | St. Stephen | Edmundston
  - 同じ表の列：Emplacement, Mis à jour, Débit / Expéditions…, Débit / Expéditions…, Débit / Voyageurs -…, Débit / Voyageurs -…

## g0028（1 列）
- 見出し：Emplacement
- 例1 値：Belleville, NB/Houlton, ME | Surrey, BC/Blaine, WA | Aldergrove, BC/Lynden, WA | Windsor, ON/Detroit, MI | Hemmingford, QC/Mooers, NY
  - 同じ表の列：Bureau de l'ASFC, Mis à jour, Débit / Expéditions…, Débit / Expéditions…, Débit / Voyageurs -…, Débit / Voyageurs -…

## g0029（1 列）
- 見出し：Mis à jour
- 例1 値：2026-10-16 10:33 HAA | 2026-10-31 17:30 HAE | 2026-10-31 19:15 HAA | 2026-10-31 18:15 HAE | 2026-10-31 18:15 HAE
  - 同じ表の列：Bureau de l'ASFC, Emplacement, Débit / Expéditions…, Débit / Expéditions…, Débit / Voyageurs -…, Débit / Voyageurs -…

## g0030（1 列）
- 見出し：Débit / Expéditions commerciales - Vers le Canada
- 例1 値：Aucun délai | Aucun délai | Ne s'applique pas | 0 semaine, 0 jour, 0 heure, 20 minutes | Aucun délai
  - 同じ表の列：Bureau de l'ASFC, Emplacement, Mis à jour, Débit / Expéditions…, Débit / Voyageurs -…, Débit / Voyageurs -…

## g0031（1 列）
- 見出し：Débit / Expéditions commerciales - Vers les États-Unis
- 例1 値：-- | -- | -- | -- | --
  - 同じ表の列：Bureau de l'ASFC, Emplacement, Mis à jour, Débit / Expéditions…, Débit / Voyageurs -…, Débit / Voyageurs -…

## g0032（1 列）
- 見出し：Débit / Voyageurs - Vers le Canada
- 例1 値：Aucun délai | 0 semaine, 0 jour, 0 heure, 5 minutes | Aucun délai | Aucun délai | Aucun délai
  - 同じ表の列：Bureau de l'ASFC, Emplacement, Mis à jour, Débit / Expéditions…, Débit / Expéditions…, Débit / Voyageurs -…

## g0033（1 列）
- 見出し：Débit / Voyageurs - Vers les États-Unis
- 例1 値：-- | -- | -- | -- | --
  - 同じ表の列：Bureau de l'ASFC, Emplacement, Mis à jour, Débit / Expéditions…, Débit / Expéditions…, Débit / Voyageurs -…

## g0034（1 列）
- 見出し：400042643
- 例1 値：400045619 | 400045951,Anhydra inc.,Centre-du-Québec… | 400045798 | 400045460 | 400047099
  - 同じ表の列：Compusport inc., Abitibi-Témiscaming…, 2011-06-17, Commercialisation e…, Direct

## g0035（1 列）
- 見出し：Compusport inc.
- 例1 値：Ungava Technologies inc. | Produits innovations BBraver inc. | Noviflow inc. | SiOptiques inc. | Carré Technologies inc.
  - 同じ表の列：400042643, Abitibi-Témiscaming…, 2011-06-17, Commercialisation e…, Direct

## g0036（1 列）
- 見出し：Abitibi-Témiscamingue-Nord-du-Québec
- 例1 値：Bas-Saint-Laurent | Saguenay - Lac-Saint-Jean | Grand Montréal | Québec-Chaudière-Appalaches | Centre-du-Québec
  - 同じ表の列：400042643, Compusport inc., 2011-06-17, Commercialisation e…, Direct

## g0037（1 列）
- 見出し：2011-06-17
- 例1 値：2010-06-10 | 2006-07-12 | 2009-04-30 | 2006-03-10 | 2012-10-30
  - 同じ表の列：400042643, Compusport inc., Abitibi-Témiscaming…, Commercialisation e…, Direct

## g0038（1 列）
- 見出し：Commercialisation et exportation
- 例1 値：Commercialisation et exportation | Commercialisation et exportation | Démarrage et création d'entreprises - a… | Commercialisation et exportation | Commercialisation et exportation
  - 同じ表の列：400042643, Compusport inc., Abitibi-Témiscaming…, 2011-06-17, Direct

## g0039（1 列）
- 見出し：Direct
- 例1 値：Direct | Direct | Direct | Direct | Direct
  - 同じ表の列：400042643, Compusport inc., Abitibi-Témiscaming…, 2011-06-17, Commercialisation e…

## g0040（1 列）
- 見出し：Promotor/ Promoteur
- 例1 値：Québec International | Bureau du cinéma et de la télévision de… | Montréal International | Bureau du Cinéma et de la Télévision du… | Total
  - 同じ表の列：Source

## g0041（1 列）
- 見出し：Source
- 例1 値：http://www.bctq.ca/uploads/files/PDF/bc… | http://www.quebecinternational.ca/media… | http://www.montrealinternational.com/wp… | -
  - 同じ表の列：Promotor/ Promoteur

## g0042（1 列）
- 見出し：Year
- 例1 値：1990 | 1990 | 1990 | 1990 | 1990
  - 同じ表の列：Product, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$), Value (US$)

## g0043（1 列）
- 見出し：Product
- 例1 値：Propane | Propane | Propane | Butane | Butane
  - 同じ表の列：Year, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$), Value (US$)

## g0044（1 列）
- 見出し：Origin
- 例1 値：Total | Alberta | Manitoba | Ontario | Total
  - 同じ表の列：Year, Product, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$), Value (US$)

## g0045（1 列）
- 見出し：Destination / PADD
- 例1 値：PADD V | PADD IV | PADD II | Total | PADD IV
  - 同じ表の列：Year, Product, Origin, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$), Value (US$)

## g0046（1 列）
- 見出し：Mode of Transportation
- 例1 値：Truck | Total | Total | Truck | Total
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Volume (m3), Volume (bbl), Value (CN$), Value (US$)

## g0047（1 列）
- 見出し：Volume (m3)
- 例1 値：478.000000 | 701.000000 | 17716.800000 | 35761.400000 | 4075.000000
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Mode of Transportat…, Volume (bbl), Value (CN$), Value (US$)

## g0048（1 列）
- 見出し：Volume (bbl)
- 例1 値：255457.711080 | 65725.265100 | 123264.355500 | 5572.762800 | 2196.398160
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Value (CN$), Value (US$)

## g0049（1 列）
- 見出し：Value (CN$)
- 例1 値：118299.000000 | 117008.000000 | 1052423.870000 | 19708598.900000 | 2826021.290000
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (US$)

## g0050（1 列）
- 見出し：Value (US$)
- 例1 値：6022457.763880 | 13900368.320440 | 868276.766960 | 856137.277000 | 33371.141290
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$)

## g0051（1 列）
- 見出し：Price (CN cents/L)
- 例1 値：8.880000 | 14.492996 | 11.305854 | 11.874629 | 17.213759
  - 同じ表の列：Year, Product, Origin, Destination / PADD, Mode of Transportat…, Volume (m3), Volume (bbl), Value (CN$)

## g0052（1 列）
- 見出し：Company
- 例1 値：2193914 Canada Limited | Alliance Pipeline Ltd. | 2193914 Canada Limited | 1057533 Alberta Ltd. | 1057533 Alberta Ltd.
  - 同じ表の列：Project Status, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Instrument Status, Location, Condition Number

## g0053（1 列）
- 見出し：Project Status
- 例1 値：Completed | Completed | Completed | In Progress | Completed
  - 同じ表の列：Company, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Instrument Status, Location, Condition Number

## g0054（1 列）
- 見出し：Instrument Activity
- 例1 値：Kaiser Exploration Ltd. | Portal Municipal Gas Company Canada Inc. | Terra Energy Corp. | Talisman Energy Inc. | Terra Energy Corp.
  - 同じ表の列：Company, Project Status, Effective Date, Issuance Date, Sunset Date, Instrument Status, Location, Condition Number

## g0055（1 列）
- 見出し：Effective Date
- 例1 値：06/04/2014 | 06/04/2014 | 04/24/2020 | 05/05/2014 | 05/05/2014
  - 同じ表の列：Company, Project Status, Instrument Activity, Issuance Date, Sunset Date, Instrument Status, Location, Condition Number

## g0056（1 列）
- 見出し：Issuance Date
- 例1 値：05/05/2014 | 06/04/2014 | 05/05/2014 | 06/04/2014 | 06/04/2014
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Sunset Date, Instrument Status, Location, Condition Number

## g0057（1 列）
- 見出し：Sunset Date
- 例1 値：09/09/2015 | 07/14/2015 | 12/31/2024 | 09/30/2017 | 10/26/2012
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Issuance Date, Instrument Status, Location, Condition Number

## g0058（1 列）
- 見出し：Instrument Status
- 例1 値：All Conditions/Requirements Met | All Conditions/Requirements Met | All Conditions/Requirements Met | All Conditions/Requirements Met | All Conditions/Requirements Met
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Location, Condition Number

## g0059（1 列）
- 見出し：Location
- 例1 値：Camrose--Drumheller/Alberta | Athabasca--Grande Prairie--Peace River/… | Regina--Moose Mountain/Saskatchewan | Regina--Moose Mountain/Saskatchewan | Athabasca--Grande Prairie--Peace River/…
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Instrument Status, Condition Number

## g0060（1 列）
- 見出し：Condition Number
- 例1 値：1 | 2 | 3 | 1 | 1
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Instrument Status, Location

## g0061（1 列）
- 見出し：Condition Status
- 例1 値：Closed | Closed | Closed | Closed | Closed
  - 同じ表の列：Company, Project Status, Instrument Activity, Effective Date, Issuance Date, Sunset Date, Instrument Status, Location

## g0062（1 列）
- 見出し：Event Number
- 例1 値：DPR2026-081 | DPR2023-074 | DPR2025-259 | UX2009-065 | UX2018-228
  - 同じ表の列：Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0063（1 列）
- 見出し：Event Type
- 例1 値：Ground Disturbance | Vehicle Crossing | Ground Disturbance; Vehicle Crossing | Ground Disturbance | Vehicle Crossing
  - 同じ表の列：Event Number, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0064（1 列）
- 見出し：Applicable Regulations
- 例1 値：National Energy Board Pipeline Damage P… | National Energy Board Pipeline Damage P… | National Energy Board Pipeline Crossing… | Canadian Energy Regulator Pipeline Dama… | National Energy Board Pipeline Damage P…
  - 同じ表の列：Event Number, Event Type, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0065（1 列）
- 見出し：Damage Prevention Program Changed
- 例1 値：No | No | Not Specified | Yes | N/A
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0066（1 列）
- 見出し：Further Action Required
- 例1 値：N/A | No | No | Not Specified | Not Specified
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Equipment Type, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0067（1 列）
- 見出し：Equipment Type
- 例1 値：N/A | Directional Drill | N/A | N/A | N/A
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Was Pipe Damaged, Was There Damage To…, Was There Damage To…

## g0068（1 列）
- 見出し：Was Pipe Damaged
- 例1 値：N/A | N/A | N/A | Not Specified | Not Specified
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was There Damage To…, Was There Damage To…

## g0069（1 列）
- 見出し：Was There Damage To Pipe Coating
- 例1 値：N/A | Not Specified | Not Specified | Not Specified | N/A
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…

## g0070（1 列）
- 見出し：Was There Damage To Pipe Body
- 例1 値：N/A | N/A | Not Specified | N/A | N/A
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…

## g0071（1 列）
- 見出し：Will An Engineering Assessment Be Required
- 例1 値：Not Specified | Not Specified | Not Specified | Not Specified | Not Specified
  - 同じ表の列：Event Number, Event Type, Applicable Regulati…, Damage Prevention P…, Further Action Requ…, Equipment Type, Was Pipe Damaged, Was There Damage To…

## g0072（1 列）
- 見出し：CropYr
- 例1 値：2018-2019 | 2018-2019 | 2018-2019 | 2018-2019 | 2018-2019
  - 同じ表の列：ShipWeek, Week_ending_date, WorkSheet, Province, Grain, Destination, Country, Cars_Allocated

## g0073（1 列）
- 見出し：ShipWeek
- 例1 値：52 | 45 | 46 | 51 | 53
  - 同じ表の列：CropYr, Week_ending_date, WorkSheet, Province, Grain, Destination, Country, Cars_Allocated

## g0074（1 列）
- 見出し：Week_ending_date
- 例1 値：2019-05-04 | 2019-06-29 | 2019-06-29 | 2019-06-15 | 2019-08-03
  - 同じ表の列：CropYr, ShipWeek, WorkSheet, Province, Grain, Destination, Country, Cars_Allocated

## g0075（1 列）
- 見出し：WorkSheet
- 例1 値：Destination | Destination | Province | Destination | Province
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, Province, Grain, Destination, Country, Cars_Allocated

## g0076（2 列）
- 見出し：Province
- 例1 値：Saskatchewan | Manitoba | Saskatchewan | Manitoba | Saskatchewan
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, WorkSheet, Grain, Destination, Country, Cars_Allocated
- 例2 値：PE | NS | NS | NS | NS
  - 同じ表の列：PNuid_NLidu, Nom_fr

## g0077（1 列）
- 見出し：Grain
- 例1 値：Flaxseed | Wheat | Buckwheat | Oat | Oat
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, WorkSheet, Province, Destination, Country, Cars_Allocated

## g0078（1 列）
- 見出し：Destination
- 例1 値：Pacific | Bay & Lakes | Pacific | Export | St. Lawrence
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, WorkSheet, Province, Grain, Country, Cars_Allocated

## g0079（1 列）
- 見出し：Country
- 例1 値：Canada Unlicensed | Canada Unlicensed | United States | Canada Licensed | United States
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, WorkSheet, Province, Grain, Destination, Cars_Allocated

## g0080（1 列）
- 見出し：Cars_Allocated
- 例1 値：3 | 3 | 10 | 68 | 17
  - 同じ表の列：CropYr, ShipWeek, Week_ending_date, WorkSheet, Province, Grain, Destination, Country

## g0081（1 列）
- 見出し：Year/année
- 例1 値：2017 | 2010 | 2015 | 2008 | 2013
  - 同じ表の列：Gender, Sexe, Category, Catégorie, Number/Nombre

## g0082（1 列）
- 見出し：Gender
- 例1 値：Females | Males | Males | Females | Males
  - 同じ表の列：Year/année, Sexe, Category, Catégorie, Number/Nombre

## g0083（1 列）
- 見出し：Sexe
- 例1 値：Hommes | Femmes | Femmes | Femmes | Hommes
  - 同じ表の列：Year/année, Gender, Category, Catégorie, Number/Nombre

## g0084（1 列）
- 見出し：Category
- 例1 値：All Other Immigration | Resettled Refugee & Protected Person in… | Resettled Refugee & Protected Person in… | All Other Immigration | All Other Immigration
  - 同じ表の列：Year/année, Gender, Sexe, Catégorie, Number/Nombre

## g0085（1 列）
- 見出し：Catégorie
- 例1 値：Économique | Réfugiés réinstallés et personnes proté… | Famille parrainée | Famille parrainée | Toutes les autres catégories d'immigrat…
  - 同じ表の列：Year/année, Gender, Sexe, Category, Number/Nombre

## g0086（1 列）
- 見出し：Number/Nombre
- 例1 値：13967 | 11552 | 28690 | 83623 | 1985
  - 同じ表の列：Year/année, Gender, Sexe, Category, Catégorie

## g0087（1 列）
- 見出し：Immigration Overview
- 例1 値：Resettled Refugee & Protected Person in… | Resettled Refugee & Protected Person in… | Females | Economic | Economic
  - 同じ表の列：Aperçu de l’immigra…

## g0088（1 列）
- 見出し：Aperçu de l’immigration
- 例1 値：Toutes les autres catégories d'immigrat… | Réfugiés réinstallés et personnes proté… | Réfugiés réinstallés et personnes proté… | Famille parrainée | Famille parrainée
  - 同じ表の列：Immigration Overview

## g0089（1 列）
- 見出し：Ref Number | Numéro réf
- 例1 値：7086167 | 7236939 | 7162990 | 7092850 | 7086162
  - 同じ表の列：Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…, Comments

## g0090（1 列）
- 見出し：Author | Auteur
- 例1 値：NB | NB | NB | NB | NB
  - 同じ表の列：Ref Number | Numéro…, # pages, Language | Langue, Date, Availability | Disp…, Comments

## g0091（1 列）
- 見出し：# pages
- 例1 値：259 | 2 | 10 | 12 | 144
  - 同じ表の列：Ref Number | Numéro…, Author | Auteur, Language | Langue, Date, Availability | Disp…, Comments

## g0092（1 列）
- 見出し：Language | Langue
- 例1 値：English | English | English | English | English
  - 同じ表の列：Ref Number | Numéro…, Author | Auteur, # pages, Date, Availability | Disp…, Comments

## g0093（1 列）
- 見出し：Date
- 例1 値：13-Jul-23 | 13-Jul-23 | 30-Jun-23 | 30-Jun-23 | 13-Jul-23
  - 同じ表の列：Ref Number | Numéro…, Author | Auteur, # pages, Language | Langue, Availability | Disp…, Comments

## g0094（1 列）
- 見出し：Availability | Disponibilité
- 例1 値：Available | Available | Available | partially available | Available
  - 同じ表の列：Ref Number | Numéro…, Author | Auteur, # pages, Language | Langue, Date, Comments

## g0095（1 列）
- 見出し：Comments
- 例1 値：7247178 | 7247178 | ARC Proprietary | ARC Proprietary | 7247178
  - 同じ表の列：Ref Number | Numéro…, Author | Auteur, # pages, Language | Langue, Date, Availability | Disp…

## g0096（2 列）
- 見出し：Year | Année
- 例1 値：2016 | 2013 | 2016 | 2021 | 2019
  - 同じ表の列：NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1
- 例2 値：2013 | 2018 | 2013 | 2015 | 2020
  - 同じ表の列：NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0097（2 列）
- 見出し：NPRI ID | ID INRP
- 例1 値：3161 | 7041 | 3161 | 1710 | 3163
  - 同じ表の列：Year | Année, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1
- 例2 値：2247 | 2247 | 3657 | 3657 | 2247
  - 同じ表の列：Year | Année, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0098（1 列）
- 見出し：City | Ville
- 例1 値：Tiverton | Pickering | Bowmanville | Bowmanville | Pickering
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0099（1 列）
- 見出し：CSD | SDR
- 例1 値：Musquash | Pickering | Pickering | Pickering | Kincardine
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0100（1 列）
- 見出し：CA or CMA | AR ou RMR
- 例1 値：Toronto | Oshawa | Oshawa | Toronto | Toronto
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, Economic Region | R…, Province | Province, Units | Unités, <1

## g0101（1 列）
- 見出し：Economic Region | Région économique
- 例1 値：Saint John--St. Stephen | Toronto | Toronto | Toronto | Stratford--Bruce Peninsula
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Province | Province, Units | Unités, <1

## g0102（2 列）
- 見出し：Province | Province
- 例1 値：ON | ON | ON | NB | NB
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Units | Unités, <1
- 例2 値：ON | ON | ON | ON | ON
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0103（2 列）
- 見出し：Units | Unités
- 例1 値：Bq | Bq | Bq | mSv/a | Bq
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, <1
- 例2 値：kg | MBq | GBq | mSv/a | kg
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0104（1 列）
- 見出し：<1
- 例1 値：< | < | < | < | <
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités

## g0105（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：1.20E+05 | 5.20E+05 | 1.00E+07 | 1.40E+14 | 7.09E+06
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités

## g0106（1 列）
- 見出し：City | Ville
- 例1 値：Port Hope | Peterborough | Ottawa | Port Hope | Ottawa
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0107（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：0.0214 | 0.00E+00 | 0.0038 | 8.79E+03 | 0.241
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Direct Discharge | …, Footnotes | Notes d…

## g0108（1 列）
- 見出し：Direct Discharge | Évacuations directes
- 例1 値：NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Footnotes | Notes d…

## g0109（1 列）
- 見出し：Footnotes | Notes de bas de page
- 例1 値：Site 2, Estimated public dose is calcul… | Estimated public dose is calculated inc… | Site 2, Estimated public dose is calcul… | Estimated public dose is calculated inc… | Estimated public dose is calculated inc…
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …

## g0110（1 列）
- 見出し：Number of Publications/ Nombre de publications
- 例1 値：41 | 1 | 194 | 63 | 13
  - 同じ表の列：Average of Relative…

## g0111（1 列）
- 見出し：Average of Relative Citations (ARC)/ Impact des citations
- 例1 値：n.s. | n.s. | n.s. | n.s. | 0.90359999999999996
  - 同じ表の列：Number of Publicati…

## g0112（1 列）
- 見出し：Employment Equity (EE) groups / Official Languages Équité en
- 例1 値：*2SLGBTIQ+ is not an official EE group … | 2SLGBTIQ+* / Personne de la communauté … | First Official Language FRENCH / Premiè… | Persons with disabilities / Personnes e… | Indigenous peoples / Populations autoch…
  - 同じ表の列：% of Identifying Em…

## g0113（1 列）
- 見出し：% of Identifying Employees / % d'Identification des employés
- 例1 値：11.80% | 1.70% | 15.00% | 28.80% | 8.00%
  - 同じ表の列：Employment Equity (…

## g0114（1 列）
- 見出し：Women
- 例1 値：37.0% | 37.7% | 37.7% | 37.7% | 36.9%
  - 同じ表の列：Aboriginals, Persons with Disabi…, Visible Minorities

## g0115（1 列）
- 見出し：Aboriginals
- 例1 値：2.1% | 2.0% | 1.9% | 2.1% | 2.0%
  - 同じ表の列：Women, Persons with Disabi…, Visible Minorities

## g0116（1 列）
- 見出し：Persons with Disabilities
- 例1 値：4.5% | 5.3% | 5.5% | 5.4% | 4.7%
  - 同じ表の列：Women, Aboriginals, Visible Minorities

## g0117（1 列）
- 見出し：Visible Minorities
- 例1 値：9.6% | 10.7% | 11.4% | 10.7% | 11.0%
  - 同じ表の列：Women, Aboriginals, Persons with Disabi…

## g0118（1 列）
- 見出し：Year Année (as of March 31 / au 31 mars)
- 例1 値：1999/2000 | 2017/2018 | 1992/1993 | 2014/2015 | 2016/2017
  - 同じ表の列：Visible Minorities …, Aboriginal Peoples …, Persons with disabi…, Women Femmes

## g0119（1 列）
- 見出し：Visible Minorities Minorités visibles
- 例1 値：15.50% | 1.60% | 4.40% | 11.70% | 9.20%
  - 同じ表の列：Year Année (as of M…, Aboriginal Peoples …, Persons with disabi…, Women Femmes

## g0120（1 列）
- 見出し：Aboriginal Peoples Autochtones
- 例1 値：1.80% | 1.30% | 1.50% | 1.30% | 0.70%
  - 同じ表の列：Year Année (as of M…, Visible Minorities …, Persons with disabi…, Women Femmes

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
