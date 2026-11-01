# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：1.1 Program: Tribunal Specialized and Expert Support Service
- 例1 値：Subtotal | 1.2 Program: Registry Services | 1.3 Program: Payments to Tribunal Chair… | Total | Internal Services
  - 同じ表の列：21,445,348, 21,445,348_2, 22,305,059, 20,419,286, 22,641,024, 21,747,000, 20,397,746, 7,845,015

## g0002（1 列）
- 見出し：21,445,348
- 例1 値：42,075,887 | 12,830,814 | 15,948,649 | 7,799,725 | 58,024,536
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348_2, 22,305,059, 20,419,286, 22,641,024, 21,747,000, 20,397,746, 7,845,015

## g0003（1 列）
- 見出し：21,445,348_2
- 例1 値：15,948,649 | 12,830,814 | 42,075,887 | 58,024,536 | 7,799,725
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 22,305,059, 20,419,286, 22,641,024, 21,747,000, 20,397,746, 7,845,015

## g0004（1 列）
- 見出し：22,305,059
- 例1 値：11,783,427 | 8,263,121 | 42,351,607 | 61,020,149 | 18,668,542
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 20,419,286, 22,641,024, 21,747,000, 20,397,746, 7,845,015

## g0005（1 列）
- 見出し：20,419,286
- 例1 値：18,668,542 | 10,958,479 | 57,469,265 | 38,800,723 | 7,422,958
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 22,305,059, 22,641,024, 21,747,000, 20,397,746, 7,845,015

## g0006（1 列）
- 見出し：22,641,024
- 例1 値：45,943,315 | 9,202,813 | 14,099,478 | 63,383,914 | 17,440,599
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 22,305,059, 20,419,286, 21,747,000, 20,397,746, 7,845,015

## g0007（1 列）
- 見出し：21,747,000
- 例1 値：10,949,929 | 19,626,388 | 60,162,007 | 7,838,690 | 40,535,619
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 22,305,059, 20,419,286, 22,641,024, 20,397,746, 7,845,015

## g0008（1 列）
- 見出し：20,397,746
- 例1 値：17,870,144 | 11,106,695 | 7,477,407 | 56,851,992 | 38,981,848
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 22,305,059, 20,419,286, 22,641,024, 21,747,000, 7,845,015

## g0009（1 列）
- 見出し：7,845,015
- 例1 値：10,217,101 | 16,520,374 | 4,888,986 | 26,737,475 | 3,786,373
  - 同じ表の列：1.1 Program: Tribun…, 21,445,348, 21,445,348_2, 22,305,059, 20,419,286, 22,641,024, 21,747,000, 20,397,746

## g0010（1 列）
- 見出し：sign_year
- 例1 値：2010 | 2001 | 2008 | 2016 | 2016
  - 同じ表の列：permit_type_level1_…, classification_leve…, age_english_desc

## g0011（1 列）
- 見出し：permit_type_level1_eng_desc
- 例1 値：Work permit holder | Work permit holder | Work permit holder | Work permit holder | Work permit holder
  - 同じ表の列：sign_year, classification_leve…, age_english_desc

## g0012（1 列）
- 見出し：classification_level1_eng_desc
- 例1 値：International Mobility Program Particip… | International Mobility Program Particip… | International Mobility Program Particip… | International Mobility Program Particip… | International Mobility Program Particip…
  - 同じ表の列：sign_year, permit_type_level1_…, age_english_desc

## g0013（1 列）
- 見出し：age_english_desc
- 例1 値：0 to 14 years old | 30 to 44 years old | 60 to 74 years old | 30 to 44 years old | 15 to 29 years old
  - 同じ表の列：sign_year, permit_type_level1_…, classification_leve…

## g0014（3 列）
- 見出し：Year | Année
- 例1 値：2023 | 2023 | 2018 | 2019 | 2017
  - 同じ表の列：NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…
- 例2 値：2015 | 2017 | 2019 | 2013 | 2018
  - 同じ表の列：NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0015（3 列）
- 見出し：NPRI ID | ID INRP
- 例1 値：2247 | 3657 | 2247 | 3657 | 3657
  - 同じ表の列：Year | Année, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…
- 例2 値：1445 | 7041 | 7041 | 3161 | 1710
  - 同じ表の列：Year | Année, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0016（1 列）
- 見出し：City | Ville
- 例1 値：Ottawa | Toronto | Port Hope | Blind River | Pembroke
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0017（3 列）
- 見出し：Province | Province
- 例1 値：ON | ON | ON | ON | ON
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…
- 例2 値：ON | ON | ON | ON | ON
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Units | Unités, <1

## g0018（1 列）
- 見出し：Units | Unités
- 例1 値：kg | kg | mSv/a | kg | MBq
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0019（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：0.00E+00 | NRM | NRS | 0.0173 | 0.02 | 0.00E+00
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Direct Discharge | …, Footnotes | Notes d…

## g0020（1 列）
- 見出し：Direct Discharge | Évacuations directes
- 例1 値：NRM | NRS | NRM | NRS | NRM | NRS | 1.4 | NRM | NRS
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Footnotes | Notes d…

## g0021（2 列）
- 見出し：Footnotes | Notes de bas de page
- 例1 値：Estimated public dose is calculated inc… | Estimated public dose is calculated inc… | Estimated public dose is calculated inc… | Estimated public dose is calculated inc… | Estimated public dose is calculated inc…
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …
- 例2 値：Loadings were less than the detection l…
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …

## g0022（1 列）
- 見出し：City | Ville
- 例1 値：Bécancour | Bowmanville | Maces Bay | Bowmanville | Tiverton
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0023（1 列）
- 見出し：CSD | SDR
- 例1 値：Clarington | Kincardine | Pickering | Kincardine | Pickering
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités, <1

## g0024（1 列）
- 見出し：CA or CMA | AR ou RMR
- 例1 値：Toronto | Oshawa | Saint John | Toronto | Saint John
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, Economic Region | R…, Province | Province, Units | Unités, <1

## g0025（1 列）
- 見出し：Economic Region | Région économique
- 例1 値：Saint John--St. Stephen | Stratford--Bruce Peninsula | Saint John--St. Stephen | Toronto | Toronto
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Province | Province, Units | Unités, <1

## g0026（1 列）
- 見出し：Units | Unités
- 例1 値：Bq | Bq | Bq | Bq-MeV | mSv/a
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, <1

## g0027（1 列）
- 見出し：<1
- 例1 値：< | < | < | < | <
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités

## g0028（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：2.50E+14 | 3.50E+06 | 6.17E+09 | 1.60E+08 | 1.70E+13
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, CSD | SDR, CA or CMA | AR ou R…, Economic Region | R…, Province | Province, Units | Unités

## g0029（1 列）
- 見出し：City | Ville
- 例1 値：Saskatoon | Saskatoon | Saskatoon | Saskatoon | Saskatoon
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, Province | Province, Units | Unités, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0030（1 列）
- 見出し：Units | Unités
- 例1 値：MBq | MBq | MBq | MBq | MBq
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Stack Emissions | É…, Direct Discharge | …, Footnotes | Notes d…

## g0031（1 列）
- 見出し：Stack Emissions | Émissions de cheminées
- 例1 値：NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS | NRM | NRS
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Direct Discharge | …, Footnotes | Notes d…

## g0032（1 列）
- 見出し：Direct Discharge | Évacuations directes
- 例1 値：38.8 | 73.0 | 14.7 | 25.2 | 56.1
  - 同じ表の列：Year | Année, NPRI ID | ID INRP, City | Ville, Province | Province, Units | Unités, Stack Emissions | É…, Footnotes | Notes d…

## g0033（1 列）
- 見出し：Requests Received
- 例1 値：Temporary Residents (Visas) | Provinces | Permanent Resident Inside and Outside C… | Requests Received | Statistics - Government Screening Progr…
  - 同じ表の列：2014-2015, 2015-2016, 2016-2017, 2017-2018, 2018-2019, 2019-2020

## g0034（1 列）
- 見出し：2014-2015
- 例1 値：276,300 | 10,700 | 40,400 | 8,700 | 2014-2015
  - 同じ表の列：Requests Received, 2015-2016, 2016-2017, 2017-2018, 2018-2019, 2019-2020

## g0035（1 列）
- 見出し：2015-2016
- 例1 値：220 | 13,500 | 4,300 | 580 | 2015-2016
  - 同じ表の列：Requests Received, 2014-2015, 2016-2017, 2017-2018, 2018-2019, 2019-2020

## g0036（1 列）
- 見出し：2016-2017
- 例1 値：58,400 | 1,900 | 58,500 | 4,200 | 20,100
  - 同じ表の列：Requests Received, 2014-2015, 2015-2016, 2017-2018, 2018-2019, 2019-2020

## g0037（1 列）
- 見出し：2017-2018
- 例1 値：530 | 306,000 | 63,900 | 58,400 | 140,450
  - 同じ表の列：Requests Received, 2014-2015, 2015-2016, 2016-2017, 2018-2019, 2019-2020

## g0038（1 列）
- 見出し：2018-2019
- 例1 値：41,900 | 3,300 | 46,100 | 12,500 | 2,900
  - 同じ表の列：Requests Received, 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2019-2020

## g0039（1 列）
- 見出し：2019-2020
- 例1 値：43,300 | 5,000 | 2,700 | 18,000 | 75,500
  - 同じ表の列：Requests Received, 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2018-2019

## g0040（1 列）
- 見出し：DeployID
- 例1 値：08A0489 87657 basking | 08A0489 87657 basking | 08A0489 87657 basking | 08A0489 87657 basking | 08A0489 87657 basking
  - 同じ表の列：Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0041（1 列）
- 見出し：Platform_Transmitter_Terminal_Terminal_de_l_émetteur_de_la_p
- 例1 値：87657 | 87657 | 87657 | 87657 | 87657
  - 同じ表の列：DeployID, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0042（1 列）
- 見出し：Date
- 例1 値：27-Jan-2009 08:58:45 | 27-Oct-2008 00:00:00 | 01-Nov-2008 12:00:00 | 22-Nov-2008 00:00:00 | 13-Dec-2008 00:00:00
  - 同じ表の列：DeployID, Platform_Transmitte…, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0043（1 列）
- 見出し：Observation_Type___Type_d_observation
- 例1 値：None | Light - Dusk | None | None | None
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0044（1 列）
- 見出し：Observed_Sea_Surface_Temperature_Température_de_surface_de_l
- 例1 値：24.1 | 21.9 | 24 | 23.5 | 15.5
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0045（1 列）
- 見出し：Satellite_Sea_Surface_Temperature_Température_de_surface_de_
- 例1 値：22.7986940143506 | 21.7178882344564 | 21.6033251705435 | 23.1588198865564 | 21.0566741583524
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0046（1 列）
- 見出し：Observed_Depth_Profondeur_observée
- 例1 値：8 | 6 | 272 | 304 | 400
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Bathymetry_Depth_Ba…, Sunrise_Lever_de_so…

## g0047（1 列）
- 見出し：Bathymetry_Depth_Bathymétrie_Profondeur
- 例1 値：4978 | 4999 | 5030 | 4512 | 5059
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Sunrise_Lever_de_so…

## g0048（1 列）
- 見出し：Sunrise_Lever_de_soleil
- 例1 値：07-Jan-2009 11:39:18 | 09-Jan-2009 11:41:15 | 01-Jan-2009 11:39:15 | 04-Oct-2008 10:12:43 | 30-Nov-2008 11:27:16
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…

## g0049（1 列）
- 見出し：Sunset_Coucher_de_soleil
- 例1 値：13-Oct-2008 21:39:07 | 25-Jan-2009 21:30:56 | 09-Dec-2008 21:19:41 | 28-Oct-2008 21:34:56 | 01-Oct-2008 21:51:22
  - 同じ表の列：DeployID, Platform_Transmitte…, Date, Observation_Type___…, Observed_Sea_Surfac…, Satellite_Sea_Surfa…, Observed_Depth_Prof…, Bathymetry_Depth_Ba…

## g0050（1 列）
- 見出し：Fiscal years/ Années Fiscales
- 例1 値：Notes: * Une partie de la flotte fera n… | 2017-2018 | Notes: * A portion of the fleet will no… | 2018-2019 | 2016-2017
  - 同じ表の列：Department results/…, Department results …, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0051（1 列）
- 見出し：Department results/ Résultats ministériels
- 例1 値：Military equipment is ready for trainin… | Military equipment is ready for trainin… | Military equipment is ready for trainin… | Military equipment is ready for trainin… | Military equipment is ready for trainin…
  - 同じ表の列：Fiscal years/ Année…, Department results …, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0052（1 列）
- 見出し：Department results indicators/ Indicateurs des résultats min
- 例1 値：% of maritime key fleets that are servi… | % of maritime key fleets that are servi… | % of maritime key fleets that are servi… | % of maritime key fleets that are servi… | % of maritime key fleets that are servi…
  - 同じ表の列：Fiscal years/ Année…, Department results/…, Target/ Cible, Date to achieve tar…, Actual results/ Rés…

## g0053（1 列）
- 見出し：Target/ Cible
- 例1 値：At least 90%* Au moins 90%* | At least 90%* Au moins 90%* | At least 90%* Au moins 90%* | At least 90%* Au moins 90%* | At least 90%* Au moins 90%*
  - 同じ表の列：Fiscal years/ Année…, Department results/…, Department results …, Date to achieve tar…, Actual results/ Rés…

## g0054（1 列）
- 見出し：Date to achieve target/ Date d'atteinte de l'objectif
- 例1 値：2017-03-31 | 2020-03-31 | 2021-03-31 | 2019-03-31 | 2018-03-31
  - 同じ表の列：Fiscal years/ Année…, Department results/…, Department results …, Target/ Cible, Actual results/ Rés…

## g0055（1 列）
- 見出し：Actual results/ Résultats actuels
- 例1 値：98.20% | 89% | 91.40% | 95% | 94.10%
  - 同じ表の列：Fiscal years/ Année…, Department results/…, Department results …, Target/ Cible, Date to achieve tar…

## g0056（1 列）
- 見出し：Document Type Category
- 例1 値：Order | Data | Correspondence | Human Resources Material | Report
  - 同じ表の列：English Document Ty…, English Acronym/Syn…, English Definition, French Document Cla…, French Document Type, French Acronym/Syno…, French Definition

## g0057（1 列）
- 見出し：English Document Type
- 例1 値：1 | Close-out Report | Usage Report | Options Analysis Report | Taxonomy
  - 同じ表の列：Document Type Categ…, English Acronym/Syn…, English Definition, French Document Cla…, French Document Type, French Acronym/Syno…, French Definition

## g0058（1 列）
- 見出し：English Acronym/Synonym
- 例1 値：LFCO | ROE | EA | PXR | VCR
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Definition, French Document Cla…, French Document Type, French Acronym/Syno…, French Definition

## g0059（1 列）
- 見出し：English Definition
- 例1 値：A text representation of the spoken wor… | The act or process to periodically eval… | To be applied when no other specific pl… | Set of theoretical analyses and tests i… | A contract between at least two parties…
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Acronym/Syn…, French Document Cla…, French Document Type, French Acronym/Syno…, French Definition

## g0060（1 列）
- 見出し：French Document Class
- 例1 値：Plan | Rapport | Rapport | Rapport | Matériel décisif
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Acronym/Syn…, English Definition, French Document Type, French Acronym/Syno…, French Definition

## g0061（1 列）
- 見出し：French Document Type
- 例1 値：Rapport de détermination | Formulaire des instructions relatives a… | Rapport d'achèvement du projet | Évaluation envrironnementale | Tableau de bord
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Acronym/Syn…, English Definition, French Document Cla…, French Acronym/Syno…, French Definition

## g0062（1 列）
- 見出し：French Acronym/Synonym
- 例1 値：MC | Plan des RH | CDP | ORFC | Leçon apprise, Leçon observée
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Acronym/Syn…, English Definition, French Document Cla…, French Document Type, French Definition

## g0063（1 列）
- 見出し：French Definition
- 例1 値：Chaque lettre de ce mot représente un m… | Transmission de lettres, de messages et… | Document qui décrit le travail en fonct… | Vérification des antécédents ou enquête… | Évaluation qui consiste â determiner le…
  - 同じ表の列：Document Type Categ…, English Document Ty…, English Acronym/Syn…, English Definition, French Document Cla…, French Document Type, French Acronym/Syno…

## g0064（1 列）
- 見出し：Stategic Outcome
- 例1 値：Defence Operations & Services Improve S… | Defence Remains Continually Prepared to…
  - 同じ表の列：Programs, Sub Programs, Sub-Sub Programs

## g0065（1 列）
- 見出し：Programs
- 例1 値：5.0 Defence Capability Development & Re… | 3.0 Defence Ready Force Element Product… | 1.0 Defence Combat & Support Operations | 4.0 Defence Capability Element Producti… | 6.0 Internal Services
  - 同じ表の列：Stategic Outcome, Sub Programs, Sub-Sub Programs

## g0066（1 列）
- 見出し：Sub Programs
- 例1 値：6.9 Material | 6.4 Human Resources Management | 1.2 International Combat Operations | 4.4 Information Systems Lifecycle | 1.3 Ongoing Centralized Operations & Op…
  - 同じ表の列：Stategic Outcome, Programs, Sub-Sub Programs

## g0067（1 列）
- 見出し：Sub-Sub Programs
- 例1 値：4.3.4 Real Property - Operations, Maint… | 2.2.6 Canadian Safety & Security Program | 4.1.6 Military Personnel - Occupation T… | 3.3.1 Maritime Environment - Force Elem… | 4.1.9 Organization - Security, Protecti…
  - 同じ表の列：Stategic Outcome, Programs, Sub Programs

## g0068（1 列）
- 見出し：Year
- 例1 値：2024 | 2025 | 2016 | 2012 | 2013
  - 同じ表の列：Under 30, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60+

## g0069（1 列）
- 見出し：Under 30
- 例1 値：2,326 | 2,106 | 1,991 | 2,330 | 2,319
  - 同じ表の列：Year, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60+

## g0070（1 列）
- 見出し：30-34
- 例1 値：2,988 | 2,594 | 2,269 | 2,473 | 2,646
  - 同じ表の列：Year, Under 30, 35-39, 40-44, 45-49, 50-54, 55-59, 60+

## g0071（1 列）
- 見出し：35-39
- 例1 値：3,257 | 4,224 | 3,902 | 3,722 | 3,815
  - 同じ表の列：Year, Under 30, 30-34, 40-44, 45-49, 50-54, 55-59, 60+

## g0072（1 列）
- 見出し：40-44
- 例1 値：5,211 | 5,620 | 5,921 | 5,044 | 5,790
  - 同じ表の列：Year, Under 30, 30-34, 35-39, 45-49, 50-54, 55-59, 60+

## g0073（1 列）
- 見出し：45-49
- 例1 値：9,567 | 5,615 | 6,550 | 6,633 | 7,660
  - 同じ表の列：Year, Under 30, 30-34, 35-39, 40-44, 50-54, 55-59, 60+

## g0074（1 列）
- 見出し：50-54
- 例1 値：9,411 | 9,342 | 9,568 | 14,604 | 13,521
  - 同じ表の列：Year, Under 30, 30-34, 35-39, 40-44, 45-49, 55-59, 60+

## g0075（1 列）
- 見出し：55-59
- 例1 値：14,828 | 13,393 | 17,753 | 17,983 | 17,828
  - 同じ表の列：Year, Under 30, 30-34, 35-39, 40-44, 45-49, 50-54, 60+

## g0076（1 列）
- 見出し：60+
- 例1 値：15,085 | 16,057 | 13,680 | 17,218 | 15,869
  - 同じ表の列：Year, Under 30, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59

## g0077（3 列）
- 見出し：Location/Emplacement
- 例1 値：Britannia | Britannia | Britannia | Lemieux | Britannia
  - 同じ表の列：Start Date/Date de …, Type/Type, Tritium Activity/Ac…, Tritium Error/Erreu…, MDC / CMD (Bq/L), Volume/Volume (mL), Notes
- 例2 値：Britannia | Britannia | Britannia | Britannia | Britannia
  - 同じ表の列：Start Date/Date de …, Type/Type, Alpha Activity/Acti…, Alpha Error/Erreur …, Beta Activity/Activ…, Beta Error/Erreur b…

## g0078（2 列）
- 見出し：Start Date/Date de début
- 例1 値：2017-08-13 | 2012-01-08 | 2013-12-22 | 2011-06-19 | 2015-09-20
  - 同じ表の列：Location/Emplacement, Type/Type, Tritium Activity/Ac…, Tritium Error/Erreu…, MDC / CMD (Bq/L), Volume/Volume (mL), Notes
- 例2 値：2010-06-27 | 2010-05-30 | 2007-11-13 | 2019-01-14 | 2003-01-06
  - 同じ表の列：Location/Emplacement, Type/Type, Alpha Activity/Acti…, Alpha Error/Erreur …, Beta Activity/Activ…, Beta Error/Erreur b…

## g0079（1 列）
- 見出し：Type/Type
- 例1 値：Treated/Traitée | Treated/Traitée | Treated/Traitée | Treated/Traitée | Treated/Traitée
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Tritium Activity/Ac…, Tritium Error/Erreu…, MDC / CMD (Bq/L), Volume/Volume (mL), Notes

## g0080（1 列）
- 見出し：Tritium Activity/Activité du tritium (Bq/L)
- 例1 値：Below MDC | 6.7 | 5.3 | 4.5 | 8.9
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Tritium Error/Erreu…, MDC / CMD (Bq/L), Volume/Volume (mL), Notes

## g0081（1 列）
- 見出し：Tritium Error/Erreur de tritium (Bq/L)
- 例1 値：2.0 | NA | NA | N/A | 2.0
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Tritium Activity/Ac…, MDC / CMD (Bq/L), Volume/Volume (mL), Notes

## g0082（1 列）
- 見出し：MDC / CMD (Bq/L)
- 例1 値：4.0 | 5.1 | 4.0 | 5.1 | 4.6
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Tritium Activity/Ac…, Tritium Error/Erreu…, Volume/Volume (mL), Notes

## g0083（1 列）
- 見出し：Volume/Volume (mL)
- 例1 値：8.0 | 8.0 | 8.0 | 8.0 | 8.0
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Tritium Activity/Ac…, Tritium Error/Erreu…, MDC / CMD (Bq/L), Notes

## g0084（1 列）
- 見出し：Notes
- 例1 値：*New blanks and standards were created … | New instrument used to measure the samp… | *Due to changes in Due to changes in in… | * Starting in July 2017, the samples ar…
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Tritium Activity/Ac…, Tritium Error/Erreu…, MDC / CMD (Bq/L), Volume/Volume (mL)

## g0085（1 列）
- 見出し：resultNumber
- 例1 値：10 | 5 | 9 | 11 | 46
  - 同じ表の列：pre-mitigationRadon, long-termPost-mitig…, reductionAchieved

## g0086（1 列）
- 見出し：pre-mitigationRadon
- 例1 値：3000 | 1110 | 3494 | 1758 | 20634
  - 同じ表の列：resultNumber, long-termPost-mitig…, reductionAchieved

## g0087（1 列）
- 見出し：long-termPost-mitigationRadon
- 例1 値：75 | 17 | 23 | 57 | 20
  - 同じ表の列：resultNumber, pre-mitigationRadon, reductionAchieved

## g0088（1 列）
- 見出し：reductionAchieved
- 例1 値：95.1 | 97.2 | 84.3 | 96.2 | 96.1
  - 同じ表の列：resultNumber, pre-mitigationRadon, long-termPost-mitig…

## g0089（1 列）
- 見出し：RecallPosted_RapellPoste
- 例1 値：2019-08-27 | 2019-10-10 | 2019-09-04 | 2019-05-15 | 2019-06-27
  - 同じ表の列：Decision_Decision, Level_Niveau, WebIdentifier_Ident…, Measure_Mesur

## g0090（1 列）
- 見出し：Decision_Decision
- 例1 値：2019-07-05 | 2019-05-21 | 2019-07-25 | 2019-06-10 | 2019-08-19
  - 同じ表の列：RecallPosted_Rapell…, Level_Niveau, WebIdentifier_Ident…, Measure_Mesur

## g0091（1 列）
- 見出し：Level_Niveau
- 例1 値：3 | 2 | 3 | 3 | 2
  - 同じ表の列：RecallPosted_Rapell…, Decision_Decision, WebIdentifier_Ident…, Measure_Mesur

## g0092（1 列）
- 見出し：WebIdentifier_IdentifiantWeb
- 例1 値：RA-70183 | RA-71213 | RA-70043 | RA-71007 | RA-70997
  - 同じ表の列：RecallPosted_Rapell…, Decision_Decision, Level_Niveau, Measure_Mesur

## g0093（1 列）
- 見出し：Measure_Mesur
- 例1 値：10 | 31 | 71 | 10 | 22
  - 同じ表の列：RecallPosted_Rapell…, Decision_Decision, Level_Niveau, WebIdentifier_Ident…

## g0094（1 列）
- 見出し：Type/Type
- 例1 値：Treated/Traitée | Raw/Brute | Treated/Traitée | Raw/Brute | Treated/Traitée
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Alpha Activity/Acti…, Alpha Error/Erreur …, Beta Activity/Activ…, Beta Error/Erreur b…

## g0095（1 列）
- 見出し：Alpha Activity/Activité alpha (Bq/L)
- 例1 値：0.01 | 0.01 | 0.03 | 0.00 | N/A
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Alpha Error/Erreur …, Beta Activity/Activ…, Beta Error/Erreur b…

## g0096（1 列）
- 見出し：Alpha Error/Erreur alpha (Bq/L)
- 例1 値：0.01 | 0.00 | 0.00 | 0.00 | 0.00
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Alpha Activity/Acti…, Beta Activity/Activ…, Beta Error/Erreur b…

## g0097（1 列）
- 見出し：Beta Activity/Activité bêta (Bq/L)
- 例1 値：0.02 | 0.04 | 0.05 | 0.03 | 0.04
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Alpha Activity/Acti…, Alpha Error/Erreur …, Beta Error/Erreur b…

## g0098（1 列）
- 見出し：Beta Error/Erreur bêta (Bq/L)
- 例1 値：0.02 | 0.33 | 0.02 | 0.01 | 0.02
  - 同じ表の列：Location/Emplacement, Start Date/Date de …, Type/Type, Alpha Activity/Acti…, Alpha Error/Erreur …, Beta Activity/Activ…

## g0099（1 列）
- 見出し：Province/ Province
- 例1 値：ON | ON | NU | ON | NU
  - 同じ表の列：Location/Emplacement, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0100（1 列）
- 見出し：Collection Start/Début du prélèvement (UTC)
- 例1 値：2010-03-01 | 2011-02-21 | 2011-04-18 | 2011-04-13 | 2019-03-18
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0101（1 列）
- 見出し：Collection Time/Durée d'échantillonnage (s)
- 例1 値：595320 | 605280 | 588960 | 604140 | 595200
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0102（1 列）
- 見出し：AirVolume/Volume d'air (m3)
- 例1 値：2055 | 1988.800049 | 2096 | 17801 | 1818
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0103（1 列）
- 見出し：7Be Activity/7Be Activité (mBq/m3)
- 例1 値：2.57455241 | 3.180351849 | 1.277471289 | 1.751313081 | 2.728480025
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0104（1 列）
- 見出し：7Be Uncertainty/7Be Incertitude (mBq/m3)
- 例1 値：0.043953126 | 0.147884425 | 0.17496467 | 0.100702611 | 0.116677935
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be MDC/7Be CMD (mB…, 210Pb Activity/210P…

## g0105（1 列）
- 見出し：7Be MDC/7Be CMD (mBq/m3)
- 例1 値：0.019273626 | 0.019568577 | 0.137790273 | 0.181298412 | 0.330518943
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 210Pb Activity/210P…

## g0106（1 列）
- 見出し：210Pb Activity/210Pb Activité (mBq/m3)
- 例1 値：0.575763462 | 0.703802292 | 0.664702331 | 0.140792892 | 0.126485989
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…

## g0107（1 列）
- 見出し：210Pb Uncertainty/210Pb Incertitude (mBq/m3)
- 例1 値：0.018871113 | 0.008884756 | 0.015668676 | 0.024201794 | 0.0311
  - 同じ表の列：Location/Emplacement, Province/ Province, Collection Start/Dé…, Collection Time/Dur…, AirVolume/Volume d'…, 7Be Activity/7Be Ac…, 7Be Uncertainty/7Be…, 7Be MDC/7Be CMD (mB…

## g0108（1 列）
- 見出し：CANADIAN CHARTER OF RIGHTS AND FREEDOMS
- 例1 値：35,660 | 2509 | 3442 | 5927 | 3464
  - 同じ表の列：CANADIAN BILL OF RI…, CHARTER AND BILL OF…

## g0109（1 列）
- 見出し：CANADIAN BILL OF RIGHTS
- 例1 値：803 | 757 | 2795 | 3031 | Certificate
  - 同じ表の列：CANADIAN CHARTER OF…, CHARTER AND BILL OF…

## g0110（1 列）
- 見出し：CHARTER AND BILL OF RIGHTS
- 例1 値：5013 | 12666 | Total | 12426 | 7276
  - 同じ表の列：CANADIAN CHARTER OF…, CANADIAN BILL OF RI…

## g0111（1 列）
- 見出し：Program/Component
- 例1 値：Scientific Service at CCI - Object Anal… | Museums Assistance Program / Collection… | Scientific Service at client site | Equipment Loan | Conservation Treatment at CCI
  - 同じ表の列：Type of Funding/Ser…, Province, # of objects, # of Collections

## g0112（1 列）
- 見出し：Type of Funding/Service
- 例1 値：Service | Service | Service | Service | Service
  - 同じ表の列：Program/Component, Province, # of objects, # of Collections

## g0113（1 列）
- 見出し：Province
- 例1 値：QC | NT | BC | NL | QC
  - 同じ表の列：Program/Component, Type of Funding/Ser…, # of objects, # of Collections

## g0114（1 列）
- 見出し：# of objects
- 例1 値：3,233 | 1 | 1 | 1 | 1
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of Collections

## g0115（1 列）
- 見出し：# of Collections
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of objects

## g0116（1 列）
- 見出し：Min-portfolio_Portefeuille-min_eng
- 例1 値：Environment and Climate Change | Environment and Climate Change | Privy Council | Indigenous Services | Agriculture and Agri-Food
  - 同じ表の列：Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0117（1 列）
- 見出し：Min-portfolio_Portefeuille-min_fra
- 例1 値：Affaires mondiales | Santé | Sécurité publique | Pêches et Océans | Santé
  - 同じ表の列：Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0118（1 列）
- 見出し：Entity_Entite_eng
- 例1 値：Canadian Food Inspection Agency | Canadian Heritage (Department of) | Senate | National Defence (Department of) | Canada Border Services Agency
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0119（1 列）
- 見出し：Entity_Entite_fra
- 例1 値：Agriculture et de l'Agroalimentaire (Mi… | Relations Couronne-Autochtones et des A… | Conseil national de recherches du Canada | Téléfilm Canada | Sécurité publique et de la Protection c…
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0120（1 列）
- 見出し：Prog-core-resp-code_Code-prog-resp-essent
- 例1 値：ISS00 | BUN00 | ISS00 | BNT00 | ISS00
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

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
