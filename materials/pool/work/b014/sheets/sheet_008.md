# ラベル用シート 008 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：Type of Funding/Service
- 例1 値：Grant | Grant | Grant | Grant | Contribution
  - 同じ表の列：Program/Component, Province, # of host venues, # of visitors, # of public program…, # of public program…

## g0842（1 列）
- 見出し：# of host venues
- 例1 値：1 | 1 | 1 | 1 | 3
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of visitors, # of public program…, # of public program…

## g0843（1 列）
- 見出し：# of visitors
- 例1 値：37,135 | 15,004 | 9,525 | 80,592 | 458
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of host venues, # of public program…, # of public program…

## g0844（1 列）
- 見出し：# of public programming activities
- 例1 値：8 | 5 | 9 | 16 | 2
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of host venues, # of visitors, # of public program…

## g0845（1 列）
- 見出し：# of public programming products
- 例1 値：3 | 2 | 0 | 4 | 4
  - 同じ表の列：Program/Component, Type of Funding/Ser…, Province, # of host venues, # of visitors, # of public program…

## g0846（1 列）
- 見出し：Quarter // trimestre
- 例1 値：2023-2024 - Q1 | 2023-2024 - Q4 | 2023-2024 - Q1 | 2023-2024 - Q1 | 2023-2024 - Q3
  - 同じ表の列：Date of Meeting // …, Nom de l'organisati…, Language of Documen…

## g0847（1 列）
- 見出し：Date of Meeting // Date de la reunion (YYYY-MM-DD)
- 例1 値：2023/05/11 | 2023/11/30 | 2024/02/28 | 2023/06/29 | 2023/04/27
  - 同じ表の列：Quarter // trimestre, Nom de l'organisati…, Language of Documen…

## g0848（1 列）
- 見出し：Nom de l'organisation // Tire d'usage (FR)
- 例1 値：Ministère de la Justice Canada | Conseil de la radiodiffusion et des tél… | Gendarmerie royale du Canada | Secrétariat des conférences intergouver… | Services partagés Canada
  - 同じ表の列：Quarter // trimestre, Date of Meeting // …, Language of Documen…

## g0849（1 列）
- 見出し：Language of Document // Langue du document
- 例1 値：English / Anglais | English / Anglais | English / Anglais | English / Anglais | English / Anglais
  - 同じ表の列：Quarter // trimestre, Date of Meeting // …, Nom de l'organisati…

## g0850（1 列）
- 見出し：fiscal_year
- 例1 値：2015-2016 | 2015-2016 | 2020-2021 | 2023-2024 | 2023-2024
  - 同じ表の列：priority_source_e, priority_source_f, priority_type_e, priority_type_f, n

## g0851（1 列）
- 見出し：priority_source_e
- 例1 値：Regulatory priorities | Regulatory priorities | Regulatory priorities | Statutory priorities | Statutory priorities
  - 同じ表の列：fiscal_year, priority_source_f, priority_type_e, priority_type_f, n

## g0852（1 列）
- 見出し：priority_source_f
- 例1 値：Priorités réglementaires | Priorités réglementaires | Priorités réglementaires | Priorités réglementaires | Priorités réglementaires
  - 同じ表の列：fiscal_year, priority_source_e, priority_type_e, priority_type_f, n

## g0853（1 列）
- 見出し：priority_type_e
- 例1 値：Disabled employee (sec. 7) | Reinstatement to higher level (sec. 10) | Medically released CAF (attributable to… | RCMP medically discharged (sec. 7.1) | Surviving Spouse or Common law Partner …
  - 同じ表の列：fiscal_year, priority_source_e, priority_source_f, priority_type_f, n

## g0854（1 列）
- 見出し：priority_type_f
- 例1 値：Membres des FAC libérés pour raisons mé… | Fonctionnaires excédentaires (art.5)(b) | Mises en disponibilité (art.41.4) | Mises en disponibilité (art.41.4) | Congés autorisés (art.41.1)
  - 同じ表の列：fiscal_year, priority_source_e, priority_source_f, priority_type_e, n

## g0855（1 列）
- 見出し：n
- 例1 値：127 | 0 | 134 | 0 | 99
  - 同じ表の列：fiscal_year, priority_source_e, priority_source_f, priority_type_e, priority_type_f

## g0856（3 列）
- 見出し：Fiscal Year
- 例1 値：2017-2018 | 2023-2024 | 2017-2018 | 2021-2022 | 2023-2024
  - 同じ表の列：Fiscal Period, Month, Information Date, Branch, Service, Value, Comments, Metric Type
- 例2 値：2020-2021 | 2018-2019 | 2020-2021 | 2020-2021 | 2019-2020
  - 同じ表の列：Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value, Comments

## g0857（3 列）
- 見出し：Fiscal Period
- 例1 値：6 | 6 | 8 | 1 | 2
  - 同じ表の列：Fiscal Year, Month, Information Date, Branch, Service, Value, Comments, Metric Type
- 例2 値：3 | 6 | 3 | 6 | 3
  - 同じ表の列：Fiscal Year, Month, Information Date, Branch, Service, SSC Client, Value, Comments

## g0858（2 列）
- 見出し：Information Date
- 例1 値：8/31/2022 | 2/28/2023 | 12/31/2022 | 10/31/2018 | 3/31/2021
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Branch, Service, Value, Comments, Metric Type
- 例2 値：12/31/2019 | 9/30/2020 | 6/30/2020 | 9/30/2017 | 12/31/2018
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Branch, Service, SSC Client, Value, Comments

## g0859（2 列）
- 見出し：Branch
- 例1 値：Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Service, Value, Comments, Metric Type
- 例2 値：Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services | Networks Security and Digital Services
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Date, Service, Value, Metric Type

## g0860（2 列）
- 見出し：Service
- 例1 値：Infrastructure Security | Infrastructure Security | Infrastructure Security | Infrastructure Security | Infrastructure Security
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Value, Comments, Metric Type
- 例2 値：Fixed Telephony | Fixed Telephony | Fixed Telephony | Fixed Telephony | Fixed Telephony
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, SSC Client, Value, Comments

## g0861（2 列）
- 見出し：Value
- 例1 値：100 | 100 | 100 | 99.966 | 99.997
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Comments, Metric Type
- 例2 値：100 | 100 | 99.98 | 100 | 100
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Date, Branch, Service, Metric Type

## g0862（1 列）
- 見出し：Comments
- 例1 値：The number is based on the aggregate av… | Availability is based on the aggregate … | The number is based on the aggregate av…
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Value, Metric Type

## g0863（2 列）
- 見出し：Metric Type
- 例1 値：Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Value, Comments
- 例2 値：Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative | Non Cumulative
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Date, Branch, Service, Value

## g0864（1 列）
- 見出し：Branch
- 例1 値：NSDS | NSDS | NSDS | NSDS | NSDS
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Service, SSC Client, Value, Comments

## g0865（1 列）
- 見出し：SSC Client
- 例1 値：Infrastructure Canada | Fisheries and Oceans Canada | National Research Council Canada | Canadian Nuclear Safety Commission | Privy Council Office
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, Value, Comments

## g0866（1 列）
- 見出し：Comments
- 例1 値：accumulated total to date | accumulated total to date | Quarterly only | accumulated total to date | accumulated total to date
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value

## g0867（1 列）
- 見出し：Metric Type
- 例1 値：As at | Cumulative | As at | As at | As at
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Information Date, Branch, Service, SSC Client, Value

## g0868（1 列）
- 見出し：Service
- 例1 値：External Credential Management | External Credential Management | External Credential Management | External Credential Management | External Credential Management
  - 同じ表の列：Fiscal Year, Fiscal Period, Month, Date, Branch, Value, Metric Type

## g0869（1 列）
- 見出し：ref_number
- 例1 値：NIL | FW-2017-00004 | FW-2012-00001 | FW-2018-Q1-01 | 2012-2013-001
  - 同じ表の列：file_id_number, file_id_date, findings_conclusions, recommendations_cor…, recommendations_cor…

## g0870（1 列）
- 見出し：file_id_number
- 例1 値：WD00004 | SIID-2014/15-001 (PSDPA) | WD00007 | ECCC-2022-001 | SIID-2017/18-325 (PSDPA)
  - 同じ表の列：ref_number, file_id_date, findings_conclusions, recommendations_cor…, recommendations_cor…

## g0871（1 列）
- 見出し：file_id_date
- 例1 値：2022-05-06 | 2018-03-31 | 2021-12-23 | 2022-10-12 | 2016-10-19
  - 同じ表の列：ref_number, file_id_number, findings_conclusions, recommendations_cor…, recommendations_cor…

## g0872（1 列）
- 見出し：findings_conclusions
- 例1 値：a,e,f | c | e | a,b,e | e
  - 同じ表の列：ref_number, file_id_number, file_id_date, recommendations_cor…, recommendations_cor…

## g0873（1 列）
- 見出し：recommendations_corrective_measures_en
- 例1 値：The Senior Officer for Internal Disclos… | The subsequent investigation, conducted… | Administrative measures were taken agai… | Following an investigation, the public … | The Senior Officer for Internal Disclos…
  - 同じ表の列：ref_number, file_id_number, file_id_date, findings_conclusions, recommendations_cor…

## g0874（1 列）
- 見出し：recommendations_corrective_measures_fr
- 例1 値：Le rapport d’enquête contenait les reco… | L’enquête qui a suivi a permis de concl… | Des mesures correctives ont été prises. | Des mesures ont été appliquées pour acc… | L’agent supérieur pour la divulgation i…
  - 同じ表の列：ref_number, file_id_number, file_id_date, findings_conclusions, recommendations_cor…

## g0875（1 列）
- 見出し：reporting_period
- 例1 値：2026-06 | 2025-12 | 2025-12 | 2025-12 | 2025-12
  - 同じ表の列：commitments, milestones, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0876（1 列）
- 見出し：commitments
- 例1 値：C04 | C01 | C01 | C04 | C04
  - 同じ表の列：reporting_period, milestones, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0877（1 列）
- 見出し：milestones
- 例1 値：C02.1 | C04.4 | C03.4 | C04.3 | C02.3
  - 同じ表の列：reporting_period, commitments, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0878（1 列）
- 見出し：indicators
- 例1 値：C04.3.3 | C02.1.3 | C02.1.2 | C04.5.3 | C04.3.4
  - 同じ表の列：reporting_period, commitments, milestones, indicator_en, indicator_fr, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0879（1 列）
- 見出し：indicator_en
- 例1 値：Invite branches to think about their ow… | Development of a data-sensitivity frame… | Contribute to the government-wide imple… | Create an ethics and personal data tool… | Set up the multi-collaborator forum (th…
  - 同じ表の列：reporting_period, commitments, milestones, indicators, indicator_fr, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0880（1 列）
- 見出し：indicator_fr
- 例1 値：Analyser les commentaires reçus durant … | Élaborer une proposition détaillant la … | Faire la promotion du cadre et du guide… | Publier le visualiseur de données inter… | Préparer une ébauche d'un document qui …
  - 同じ表の列：reporting_period, commitments, milestones, indicators, indicator_en, indicator_deadline_…, indicator_deadline_…, indicator_lead_dept

## g0881（1 列）
- 見出し：indicator_deadline_en
- 例1 値：Biannually until 2029 | Biannually until 2029 | Feedback will be compiled in March 2027… | By summer 2025 | Biannually until 2029
  - 同じ表の列：reporting_period, commitments, milestones, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_lead_dept

## g0882（1 列）
- 見出し：indicator_deadline_fr
- 例1 値：Effectuer une mise à jour à l'interne c… | Permanent, chaque année | Les exemples seront compilés en mars 20… | D'ici la fin de 2028 | Deux fois par année jusqu'en 2029
  - 同じ表の列：reporting_period, commitments, milestones, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_lead_dept

## g0883（1 列）
- 見出し：indicator_lead_dept
- 例1 値：pch | tbs-sct | rcmp-grc | jus | isc-sac
  - 同じ表の列：reporting_period, commitments, milestones, indicators, indicator_en, indicator_fr, indicator_deadline_…, indicator_deadline_…

## g0884（1 列）
- 見出し：Audit Area
- 例1 値：General Waste Bins | General Waste Bins | General Waste Bins | Recycling Stations | Recycling Stations
  - 同じ表の列：Date, Point of Inspection, Compliance Yes/No (…, Comments on Non-Com…

## g0885（1 列）
- 見出し：Point of Inspection
- 例1 値：Avionics | Fleet Appearance | 2nd Floor (Central Registry) | Stores | Engine Repair
  - 同じ表の列：Date, Audit Area, Compliance Yes/No (…, Comments on Non-Com…

## g0886（2 列）
- 見出し：Compliance Yes/No (1/0)
- 例1 値：1 | 1 | 0 | 1 | 1
  - 同じ表の列：Date, Audit Area, Point of Inspection, Comments on Non-Com…
- 例2 値：1 | 1 | 1 | 1 | 0
  - 同じ表の列：Date, Audit Area, Point of Inspection, Comments

## g0887（1 列）
- 見出し：Comments on Non-Compliance
- 例1 値：Two pairs of gloves in garbage | Recyclables, two pairs gloves in garbage | Three absorbants in garbage | Plastic in garbage | Coffee cups found in plastic
  - 同じ表の列：Date, Audit Area, Point of Inspection, Compliance Yes/No (…

## g0888（1 列）
- 見出し：Audit Area
- 例1 値：Cleaning Room | Cleaning Room | Cleaning Room | Cleaning Room | Cleaning Room
  - 同じ表の列：Date, Point of Inspection, Compliance Yes/No (…, Comments

## g0889（1 列）
- 見出し：Point of Inspection
- 例1 値：2 pairs nitrile gloves | Floor and walls clean | Drum patch compound | Drum patch compound | Floor and walls clean
  - 同じ表の列：Date, Audit Area, Compliance Yes/No (…, Comments

## g0890（1 列）
- 見出し：Comments
- 例1 値：Pair of ear muffs missing | No spare face shield visor | No issues | One Release Agent MS143H. Label was mis… | One Royco 950. The labels are torn and …
  - 同じ表の列：Date, Audit Area, Point of Inspection, Compliance Yes/No (…

## g0891（1 列）
- 見出し：Region
- 例1 値：Western Canada | Alberta | British Columbia | Saskatchewan | Manitoba
  - 同じ表の列：Number of high grow…

## g0892（1 列）
- 見出し：Number of high growth firms
- 例1 値：3,440 | 260 | 2,120 | 160 | 900
  - 同じ表の列：Region

## g0893（1 列）
- 見出し：station_id
- 例1 値：36 | 16 | 30 | 17 | 48
  - 同じ表の列：rental_method, capacity, lat, lon, location

## g0894（1 列）
- 見出し：rental_method
- 例1 値：CREDITCARD,KEY | CREDITCARD,KEY | CREDITCARD,KEY | CREDITCARD,KEY | CREDITCARD,KEY
  - 同じ表の列：station_id, capacity, lat, lon, location

## g0895（2 列）
- 見出し：location
- 例1 値：-37.841954, 144.935296 | -37.847795, 144.948351 | -37.828887, 144.970822 | -37.807021, 144.941854 | -37.807699, 144.963095
  - 同じ表の列：station_id, rental_method, capacity, lat, lon
- 例2 値：-37.81567009, 144.970513161 | -37.81193715, 144.972055105 | -37.81581152, 144.960636662 | -37.81434461, 144.971348894 | -37.81280958, 144.971442013
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, number_of_patrons

## g0896（1 列）
- 見出し：census_year
- 例1 値：2004 | 2010 | 2009 | 2008 | 2015
  - 同じ表の列：property_id, base_property_id, clue_small_area, number_of_patrons, location

## g0897（1 列）
- 見出し：property_id
- 例1 値：108532 | 103985 | 105964 | 585863 | 111175
  - 同じ表の列：census_year, base_property_id, clue_small_area, number_of_patrons, location

## g0898（1 列）
- 見出し：base_property_id
- 例1 値：104103 | 110666 | 109706 | 103951 | 110862
  - 同じ表の列：census_year, property_id, clue_small_area, number_of_patrons, location

## g0899（1 列）
- 見出し：clue_small_area
- 例1 値：Melbourne (CBD) | Southbank | Melbourne (CBD) | Southbank | Melbourne (CBD)
  - 同じ表の列：census_year, property_id, base_property_id, number_of_patrons, location

## g0900（1 列）
- 見出し：number_of_patrons
- 例1 値：10 | 840 | 200 | 50 | 70
  - 同じ表の列：census_year, property_id, base_property_id, clue_small_area, location

## g0901（1 列）
- 見出し：day
- 例1 値：Friday | Monday | Sunday | Monday | Friday
  - 同じ表の列：date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0902（1 列）
- 見出し：number_of_1100_litre_bins_filled
- 例1 値：3 | 3 | 3 | 2 | 3
  - 同じ表の列：day, date, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0903（1 列）
- 見出し：time_bin_1_spot_check_weight_recorded
- 例1 値：6:00 | 6:00 | 6:00 | 9:00 | 8:30
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0904（1 列）
- 見出し：time_bin_2_spot_check_weight_recorded
- 例1 値：18:00 | 16:45 | 13:00 | 11:00 | 14:55
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0905（1 列）
- 見出し：time_bin_3_spot_check_weight_recorded
- 例1 値：18:00 | 17:30 | 17:40 | 18:25 | 18:00
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0906（1 列）
- 見出し：time_bin_4_spot_check_weight_recorded
- 例1 値：5:00:00 PM | 17:50 | 17:30 | 18:30 | 18:20
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_5_spot_che…, daily_estimated_net…

## g0907（1 列）
- 見出し：time_bin_5_spot_check_weight_recorded
- 例1 値：18:20
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, daily_estimated_net…

## g0908（1 列）
- 見出し：daily_estimated_net_weight_kg
- 例1 値：180.939 | 241.252 | 180.939 | 180.939 | 180.939
  - 同じ表の列：day, date, number_of_1100_litr…, time_bin_1_spot_che…, time_bin_2_spot_che…, time_bin_3_spot_che…, time_bin_4_spot_che…, time_bin_5_spot_che…

## g0909（1 列）
- 見出し：station
- 例1 値：100009 | 100008 | 90912 | 90907 | 90908
  - 同じ表の列：objectid, region, geolocation, location, notes, y_2018_oct, y_2018_nov, y_2018_dec

## g0910（1 列）
- 見出し：region
- 例1 値：Metro Sydney Inner North | Metro Sydney North West | Sydney City | Metro Sydney Inner North | Metro Sydney North West
  - 同じ表の列：objectid, station, geolocation, location, notes, y_2018_oct, y_2018_nov, y_2018_dec

## g0911（1 列）
- 見出し：geolocation
- 例1 値：-33.768099 150.84619 | -33.829159 151.215186 | -33.818056 151.202340 | -33.75367 150.966419 | -33.817990 151.089939
  - 同じ表の列：objectid, station, region, location, notes, y_2018_oct, y_2018_nov, y_2018_dec

## g0912（1 列）
- 見出し：location
- 例1 値：Lane Cove River Walk, near Browns Water… | Sydney Olympic Park to Parramatta cycle… | Western Sydney Parklands cycleway, near… | Iron Cove Bridge cycleway, near King Ge… | Como Bridge cycleway, near Oatley Parad…
  - 同じ表の列：objectid, station, region, geolocation, notes, y_2018_oct, y_2018_nov, y_2018_dec

## g0913（1 列）
- 見出し：notes
- 例1 値：First data collected 20 Sept 2012. | Counter inoperable December 2013 to Jun… | Counter inoperable June 2015 to Nov 201… | First data collected 7 Oct 2011. | Counter inoperable Mar 2014 to June 201…
  - 同じ表の列：objectid, station, region, geolocation, location, y_2018_oct, y_2018_nov, y_2018_dec

## g0914（1 列）
- 見出し：y_2018_oct
- 例1 値：1249 | 0 | 0 | 20 | 129
  - 同じ表の列：objectid, station, region, geolocation, location, notes, y_2018_nov, y_2018_dec

## g0915（1 列）
- 見出し：y_2018_nov
- 例1 値：91 | 1 | 0 | 158 | 0
  - 同じ表の列：objectid, station, region, geolocation, location, notes, y_2018_oct, y_2018_dec

## g0916（1 列）
- 見出し：y_2018_dec
- 例1 値：167 | 1 | 180 | 75 | 70
  - 同じ表の列：objectid, station, region, geolocation, location, notes, y_2018_oct, y_2018_nov

## g0917（1 列）
- 見出し：y_2019_jan
- 例1 値：72 | 1299 | 0 | 0 | 0
  - 同じ表の列：objectid, station, region, geolocation, location, notes, y_2018_oct, y_2018_nov

## g0918（1 列）
- 見出し：Interchange_Type
- 例1 値：Train | Train | Train | Ferry | Train
  - 同じ表の列：Suburb, Location, Type, Total_Lockers_at_Lo…, Total_Spaces_at_Shed, Bike_Rack_Spaces, Vertical_Hanging_Sp…, multi_tier_bike_par…

## g0919（1 列）
- 見出し：Location
- 例1 値：Meadowbank Station (Bank St) | Glenbrook Station (Burfitt Pde) | Seven Hills Station (Boomerang Pl) | Maitland Station, Station St | Wyong Station (Howarth St) 1
  - 同じ表の列：Suburb, Interchange_Type, Type, Total_Lockers_at_Lo…, Total_Spaces_at_Shed, Bike_Rack_Spaces, Vertical_Hanging_Sp…, multi_tier_bike_par…

## g0920（1 列）
- 見出し：Total_Lockers_at_Location
- 例1 値：12 | 4 | 2 | 4 | 4
  - 同じ表の列：Suburb, Interchange_Type, Location, Type, Total_Spaces_at_Shed, Bike_Rack_Spaces, Vertical_Hanging_Sp…, multi_tier_bike_par…

## g0921（1 列）
- 見出し：Total_Spaces_at_Shed
- 例1 値：32 | 26 | 24 | 82 | 32
  - 同じ表の列：Suburb, Interchange_Type, Location, Type, Total_Lockers_at_Lo…, Bike_Rack_Spaces, Vertical_Hanging_Sp…, multi_tier_bike_par…

## g0922（1 列）
- 見出し：Bike_Rack_Spaces
- 例1 値：16 | 8 | 28 | 82 | 32
  - 同じ表の列：Suburb, Interchange_Type, Location, Type, Total_Lockers_at_Lo…, Total_Spaces_at_Shed, Vertical_Hanging_Sp…, multi_tier_bike_par…

## g0923（1 列）
- 見出し：Vertical_Hanging_Spaces
- 例1 値：25 | 16 | 12 | 20 | 30
  - 同じ表の列：Suburb, Interchange_Type, Location, Type, Total_Lockers_at_Lo…, Total_Spaces_at_Shed, Bike_Rack_Spaces, multi_tier_bike_par…

## g0924（1 列）
- 見出し：multi_tier_bike_parking_spaces
- 例1 値：36 | 16 | 36 | 36 | 30
  - 同じ表の列：Suburb, Interchange_Type, Location, Type, Total_Lockers_at_Lo…, Total_Spaces_at_Shed, Bike_Rack_Spaces, Vertical_Hanging_Sp…

## 答えの雛形

```
g0841	
g0842	
g0843	
g0844	
g0845	
g0846	
g0847	
g0848	
g0849	
g0850	
g0851	
g0852	
g0853	
g0854	
g0855	
g0856	
g0857	
g0858	
g0859	
g0860	
g0861	
g0862	
g0863	
g0864	
g0865	
g0866	
g0867	
g0868	
g0869	
g0870	
g0871	
g0872	
g0873	
g0874	
g0875	
g0876	
g0877	
g0878	
g0879	
g0880	
g0881	
g0882	
g0883	
g0884	
g0885	
g0886	
g0887	
g0888	
g0889	
g0890	
g0891	
g0892	
g0893	
g0894	
g0895	
g0896	
g0897	
g0898	
g0899	
g0900	
g0901	
g0902	
g0903	
g0904	
g0905	
g0906	
g0907	
g0908	
g0909	
g0910	
g0911	
g0912	
g0913	
g0914	
g0915	
g0916	
g0917	
g0918	
g0919	
g0920	
g0921	
g0922	
g0923	
g0924	
```
