# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（3 列）
- 見出し：OBJECTID
- 例1 値：86 | 589 | 544 | 269 | 72
  - 同じ表の列：BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：660 | 802 | 72 | 913 | 988
  - 同じ表の列：BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0002（3 列）
- 見出し：BIOMASS_GRID_ID
- 例1 値：6623 | 9841 | 11001 | 12904 | 9869
  - 同じ表の列：OBJECTID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：14025 | 8389 | 12498 | 7631 | 11377
  - 同じ表の列：OBJECTID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0003（2 列）
- 見出し：CROP_BARLEY_AREA
- 例1 値：0 | 0 | 0 | 0.190623781 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：304.5324573 | 0.156606268 | 0 | 0.082065189 | 547.4410606
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0004（2 列）
- 見出し：CROP_CORN_AREA
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0005（1 列）
- 見出し：CROP_FLAX_AREA
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0006（2 列）
- 見出し：CROP_OAT_AREA
- 例1 値：0 | 0 | 83.47585941 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：0 | 0 | 11.79202362 | 0 | 0.617712081
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0007（2 列）
- 見出し：CROP_WHEAT_AREA
- 例1 値：0 | 360.4533369 | 0 | 0 | 91.90396497
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY
- 例2 値：288.1366444 | 0.273803403 | 0 | 345.8191719 | 57.59528439
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0008（2 列）
- 見出し：CROP_BARLEY_QTY
- 例1 値：0 | 0 | 80.11852376 | 446.6153522 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_OAT_QTY
- 例2 値：0 | 0 | 0 | 10.53030349 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_OAT_QTY

## g0009（2 列）
- 見出し：CROP_OAT_QTY
- 例1 値：161.0299888 | 0 | 36.79856229 | 0 | 0.097842762
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY
- 例2 値：0.885295147 | 0 | 0 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY

## g0010（2 列）
- 見出し：CROP_WHEAT_QTY
- 例1 値：0 | 0 | 15.32227633 | 0 | 0
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY
- 例2 値：142.5449911 | 0 | 3475.301395 | 83.15887295 | 1084.148623
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_FLAX_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY

## g0011（1 列）
- 見出し：CROP_FLAX_AREA
- 例1 値：0 | 0 | 0 | 0 | 5.180035672
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, CROP_BARLEY_AREA, CROP_CORN_AREA, CROP_OAT_AREA, CROP_WHEAT_AREA, CROP_BARLEY_QTY, CROP_OAT_QTY

## g0012（1 列）
- 見出し：MNCPL_SOLID_WASTE_TOTAL_VOL
- 例1 値：94.02853019 | 225.370394 | 249.8029895 | 5011.610528 | 1546.198558
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, MNCPL_SOLID_WASTE_O…, MNCPL_SOLID_WASTE_P…

## g0013（1 列）
- 見出し：MNCPL_SOLID_WASTE_ORGANIC_VOL
- 例1 値：15564.0394 | 561.6260958 | 418.6471198 | 3192.439959 | 132.1428689
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, MNCPL_SOLID_WASTE_T…, MNCPL_SOLID_WASTE_P…

## g0014（1 列）
- 見出し：MNCPL_SOLID_WASTE_PAPER_VOL
- 例1 値：6518.213525 | 836.4335812 | 204.0252986 | 83.41316812 | 62.64315887
  - 同じ表の列：OBJECTID, BIOMASS_GRID_ID, MNCPL_SOLID_WASTE_T…, MNCPL_SOLID_WASTE_O…

## g0015（1 列）
- 見出し：Departmental results
- 例1 値：3 – Percentage is based on the average … | Tribunal members receive the specialize… | ‡ – Established timeframes are set for … | † – Results achieved currently reflects… | 1 – Percentage is based on the average …
  - 同じ表の列：Performance indicat…, Target, Date to achieve tar…, 2018–19 Actual resu…, 2019–20 Actual resu…, 2020–21 Actual resu…

## g0016（1 列）
- 見出し：Performance indicators
- 例1 値：Percentage of files examined where the … | Level of satisfaction of tribunal membe…
  - 同じ表の列：Departmental results, Target, Date to achieve tar…, 2018–19 Actual resu…, 2019–20 Actual resu…, 2020–21 Actual resu…

## g0017（1 列）
- 見出し：Target
- 例1 値：85% | 85%
  - 同じ表の列：Departmental results, Performance indicat…, Date to achieve tar…, 2018–19 Actual resu…, 2019–20 Actual resu…, 2020–21 Actual resu…

## g0018（1 列）
- 見出し：Date to achieve target
- 例1 値：31-Mar-21 | 31-Mar-21
  - 同じ表の列：Departmental results, Performance indicat…, Target, 2018–19 Actual resu…, 2019–20 Actual resu…, 2020–21 Actual resu…

## g0019（1 列）
- 見出し：2018–19 Actual results
- 例1 値：89.61% | 87.93%1
  - 同じ表の列：Departmental results, Performance indicat…, Target, Date to achieve tar…, 2019–20 Actual resu…, 2020–21 Actual resu…

## g0020（1 列）
- 見出し：2019–20 Actual results
- 例1 値：91.57% | 85.08%2
  - 同じ表の列：Departmental results, Performance indicat…, Target, Date to achieve tar…, 2018–19 Actual resu…, 2020–21 Actual resu…

## g0021（1 列）
- 見出し：2020–21 Actual results
- 例1 値：88.17%3 | 90.81%
  - 同じ表の列：Departmental results, Performance indicat…, Target, Date to achieve tar…, 2018–19 Actual resu…, 2019–20 Actual resu…

## g0022（1 列）
- 見出し：Event ID
- 例1 値：REM2021-042 | REM2021-038 | REM2023-008 | REM2018-028 | REM2025-034
  - 同じ表の列：Company City, Company Province/Te…, Commodity Carried, Facility Type, Province, Applicable Land Use, Population Density, Has Contamination B…

## g0023（1 列）
- 見出し：Company City
- 例1 値：Not Specified | Calgary | Edmonton | Not Specified | Calgary
  - 同じ表の列：Event ID, Company Province/Te…, Commodity Carried, Facility Type, Province, Applicable Land Use, Population Density, Has Contamination B…

## g0024（1 列）
- 見出し：Company Province/Territory
- 例1 値：British Columbia | Ontario | Quebec | Alberta | British Columbia
  - 同じ表の列：Event ID, Company City, Commodity Carried, Facility Type, Province, Applicable Land Use, Population Density, Has Contamination B…

## g0025（1 列）
- 見出し：Commodity Carried
- 例1 値：Crude Oil Sweet Light; Refined Products… | Refined Products-Aviation; Refined Prod… | Crude Oil Sweet Light; Refined Products… | Not Specified | Not Specified
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Facility Type, Province, Applicable Land Use, Population Density, Has Contamination B…

## g0026（1 列）
- 見出し：Facility Type
- 例1 値：Not Specified | Not Specified | Not Specified | Not Specified | Not Specified
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Province, Applicable Land Use, Population Density, Has Contamination B…

## g0027（1 列）
- 見出し：Province
- 例1 値：Alberta | Saskatchewan | Quebec | British Columbia | British Columbia
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Facility Type, Applicable Land Use, Population Density, Has Contamination B…

## g0028（1 列）
- 見出し：Applicable Land Use
- 例1 値：Developed Land - Industrial | Agricultural Land | Non-developed Land | Developed Land - Industrial | Developed Land - Industrial
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Facility Type, Province, Population Density, Has Contamination B…

## g0029（1 列）
- 見出し：Population Density
- 例1 値：10 or fewer dwelling units | 10 or fewer dwelling units | 10 or fewer dwelling units | 10 or fewer dwelling units | 10 or fewer dwelling units
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Facility Type, Province, Applicable Land Use, Has Contamination B…

## g0030（1 列）
- 見出し：Has Contamination Been Reported To Other Regulator
- 例1 値：No | No | No | No | No
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Facility Type, Province, Applicable Land Use, Population Density

## g0031（1 列）
- 見出し：Other Regulator Notifed
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：Event ID, Company City, Company Province/Te…, Commodity Carried, Facility Type, Province, Applicable Land Use, Population Density

## g0032（1 列）
- 見出し：Date
- 例1 値：04/26/2012 | 05/02/2001 | 06/06/2002 | 05/25/2012 | 06/30/2011
  - 同じ表の列：Theme, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…, Due Date

## g0033（1 列）
- 見出し：Theme
- 例1 値：Integrity Management | Safety Management | Safety Management | Damage Prevention | Management System
  - 同じ表の列：Date, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…, Due Date

## g0034（1 列）
- 見出し：Categories
- 例1 値：Checking and Corrective Actions | Workplace Exposures and Protections | Implementation | Implementation | Implementation
  - 同じ表の列：Date, Theme, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…, Due Date

## g0035（1 列）
- 見出し：Sub-Categories
- 例1 値：Safeguarding | Preliminary Review | Safeguarding | Operational Control - Upset or Abnormal… | Consultations
  - 同じ表の列：Date, Theme, Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…, Due Date

## g0036（1 列）
- 見出し：Selected Facilities
- 例1 値：EDSON M/L LOOP #3 (ROBB SECTION) - NPS … | PELICAN MAINLINE BACKUP LOOP - NPS 16 | TRANS MOUNTAIN EXPANSION PROJECT | EDSON M/L LOOP #3 (ROBB SECTION) - NPS … | TRANS MOUNTAIN EXPANSION PROJECT
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Compliance Tool Used, Is This A Repeated …, Source of Requireme…, Due Date

## g0037（1 列）
- 見出し：Compliance Tool Used
- 例1 値：Recommendation | Assurance of Voluntary Compliance (AVC) | Assurance of Voluntary Compliance (AVC) | Assurance of Voluntary Compliance (AVC) | Assurance of Voluntary Compliance (AVC)
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Selected Facilities, Is This A Repeated …, Source of Requireme…, Due Date

## g0038（1 列）
- 見出し：Is This A Repeated Non-Compliance?
- 例1 値：No | No | No | No | No
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Source of Requireme…, Due Date

## g0039（1 列）
- 見出し：Source of Requirement
- 例1 値：Onshore Pipeline Regulations (OPR) | Onshore Pipeline Regulations (OPR) | Onshore Pipeline Regulations (OPR) | Onshore Pipeline Regulations (OPR) | Onshore Pipeline Regulations (OPR)
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Due Date

## g0040（1 列）
- 見出し：Due Date
- 例1 値：12/28/2017 | 01/23/2013 | 01/23/2013 | 10/17/2003 | 09/13/2012
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…

## g0041（1 列）
- 見出し：Number of Extensions Granted
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Date, Theme, Categories, Sub-Categories, Selected Facilities, Compliance Tool Used, Is This A Repeated …, Source of Requireme…

## g0042（1 列）
- 見出し：Company
- 例1 値：Enbridge Pipelines (NW) Inc. | Trans-Northern Pipelines Inc. | TransCanada PipeLines Limited | Cochin Pipe Lines Ltd. | Trans Mountain Pipe Line Company Limited
  - 同じ表の列：Activity Type, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, End Date, Life Cycle Phases

## g0043（1 列）
- 見出し：Activity Type
- 例1 値：Field Inspection | Field Inspection | Field Inspection | Field Inspection | Field Inspection
  - 同じ表の列：Company, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, End Date, Life Cycle Phases

## g0044（1 列）
- 見出し：Disciplines
- 例1 値：Environmental Protection | Environmental Protection | Emergency Management | Environmental Protection | Safety Management
  - 同じ表の列：Company, Activity Type, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, End Date, Life Cycle Phases

## g0045（1 列）
- 見出し：Number Of Hours In The Field
- 例1 値：72.00 | 36.00
  - 同じ表の列：Company, Activity Type, Disciplines, Related Events, Related CV Activiti…, Start Date, End Date, Life Cycle Phases

## g0046（1 列）
- 見出し：Related Events
- 例1 値：REM-0309
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related CV Activiti…, Start Date, End Date, Life Cycle Phases

## g0047（1 列）
- 見出し：Related CV Activities
- 例1 値：CV1617-253 | CV2425-108; CV2425-345; CV2425-368; CV2…
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related Events, Start Date, End Date, Life Cycle Phases

## g0048（1 列）
- 見出し：Start Date
- 例1 値：1/14/2004 12:00:00 AM | 11/25/2004 12:00:00 AM | 9/2/2003 12:00:00 AM | 10/2/2002 12:00:00 AM | 9/27/2001 12:00:00 AM
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, End Date, Life Cycle Phases

## g0049（1 列）
- 見出し：End Date
- 例1 値：8/28/2001 12:00:00 AM | 6/2/2006 12:00:00 AM | 3/3/2005 12:00:00 AM | 2/16/2005 12:00:00 AM | 9/21/2010 12:00:00 AM
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, Life Cycle Phases

## g0050（1 列）
- 見出し：Life Cycle Phases
- 例1 値：Operations | Construction | Construction | Operations | Post-Construction (Reclamation)
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, End Date

## g0051（1 列）
- 見出し：Status
- 例1 値：Closed | Closed | Closed | Final | Closed
  - 同じ表の列：Company, Activity Type, Disciplines, Number Of Hours In …, Related Events, Related CV Activiti…, Start Date, End Date

## g0052（1 列）
- 見出し：sea_water_pressure_pression_eau_de_mer
- 例1 値：1650 | 1100 | 15 | 1350 | 30
  - 同じ表の列：station, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0053（1 列）
- 見出し：station
- 例1 値：8 | 25.5 | 18 | 15 | 19
  - 同じ表の列：sea_water_pressure_…, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0054（1 列）
- 見出し：sea_water_temperature_temperature_eau_de_mer
- 例1 値：3.38278213 | 3.290781995 | 3.303846612 | 2.812950753 | 3.421095969
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0055（1 列）
- 見出し：sea_water_temperature_standard_deviation_ecart_type_temperat
- 例1 値：0.238698681 | 0.154302848 | 0.86012406 | 0.137811098 | 0.092887173
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0056（1 列）
- 見出し：sea_water_practical_salinity_salinite_pratique_eau_de_mer
- 例1 値：34.91537911 | 34.85441781 | 34.83105165 | 34.91654773 | 34.9011043
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0057（1 列）
- 見出し：sea_water_practical_salinity_standard_deviation_ecart_type_s
- 例1 値：0.068372224 | 0.016797349 | 0.011575029 | 0.023327702 | 0.027096779
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_sigma_the…, sea_water_sigma_the…

## g0058（1 列）
- 見出し：sea_water_sigma_theta_sigma_theta_eau_de_mer
- 例1 値：27.73758642 | 27.69474037 | 27.77760155 | 27.79560482 | 27.76877915
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…

## g0059（1 列）
- 見出し：sea_water_sigma_theta_standard_deviation_ecart_type_sigma_th
- 例1 値：0.009905825 | 0.016400867 | 0.005403694 | 0.224185774 | 0.18396238
  - 同じ表の列：sea_water_pressure_…, station, sea_water_temperatu…, sea_water_temperatu…, sea_water_practical…, sea_water_practical…, sea_water_sigma_the…

## g0060（1 列）
- 見出し：Director of Defence Counsel Services Casefiles 01 April 2019
- 例1 値：75 | 7 | 87 | 152 | 77
  - 同じ表の列：Director of Defence…

## g0061（1 列）
- 見出し：Director of Defence Counsel Services Casefiles 01 April 2020
- 例1 値：121 | 69 | 12 | 50 | 67
  - 同じ表の列：Director of Defence…

## g0062（1 列）
- 見出し：Year of publication
- 例1 値：Dec-12 | 2010 Reports | 2012 Reports | Sep-13 | Jun-14
  - 同じ表の列：Report Title, Link to report

## g0063（1 列）
- 見出し：Report Title
- 例1 値：Internal Audit: Subcontract Visibility … | Evaluation of Defence Policy and Diplom… | Audit of Civilian Leave Administration … | Audit of the Canadian Surface Combatant… | Audit of Departmental Budget Management
  - 同じ表の列：Year of publication, Link to report

## g0064（1 列）
- 見出し：Link to report
- 例1 値：https://www.canada.ca/content/dam/dnd-m… | https://www.canada.ca/content/dam/dnd-m… | https://www.canada.ca/content/dam/dnd-m… | https://www.canada.ca/en/department-nat… | https://www.canada.ca/en/department-nat…
  - 同じ表の列：Year of publication, Report Title

## g0065（1 列）
- 見出し：Request_Type
- 例1 値：Access | Access | Access | Access | Access
  - 同じ表の列：Request_Number, Activity_Date, Date_Due, Activity_Status

## g0066（1 列）
- 見出し：Request_Number
- 例1 値：A-2020-01544 | A-2020-01490 | A-2020-01286 | A-2020-01635 | A-2020-00903
  - 同じ表の列：Request_Type, Activity_Date, Date_Due, Activity_Status

## g0067（1 列）
- 見出し：Activity_Date
- 例1 値：2020-12-15 | 2020-12-29 | 2021-01-18 | 2021-01-25 | 2021-01-06
  - 同じ表の列：Request_Type, Request_Number, Date_Due, Activity_Status

## g0068（1 列）
- 見出し：Date_Due
- 例1 値：2021-01-28 | 2020-11-23 | 2021-02-08 | 2021-07-14 | 2021-02-17
  - 同じ表の列：Request_Type, Request_Number, Activity_Date, Activity_Status

## g0069（1 列）
- 見出し：Activity_Status
- 例1 値：RECEIVED | RECEIVED | RECEIVED | CLOSED | CLOSED
  - 同じ表の列：Request_Type, Request_Number, Activity_Date, Date_Due

## g0070（1 列）
- 見出し：Identification de l'installation/ Facility Identification
- 例1 値：62212 | 23241 | 30582 | 24986 | 25077
  - 同じ表の列：Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0071（1 列）
- 見出し：Ville/ City
- 例1 値：St. Claude | New Bothwell | Clarke's Beach | Stephenville Crossing | Riverside-Albert
  - 同じ表の列：Identification de l…, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0072（1 列）
- 見出し：Province (Anglais)/ Province (English)
- 例1 値：Newfoundland and Labrador | Alberta | Manitoba | Newfoundland and Labrador | Newfoundland and Labrador
  - 同じ表の列：Identification de l…, Ville/ City, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0073（1 列）
- 見出し：Province (Français) / Province (French)
- 例1 値：Alberta | Nouveau-Brunswick | Manitoba | Colombie-Britannique | Colombie-Britannique
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0074（1 列）
- 見出し：Type d'exploitant (Anglais)/ Operator Type (English)
- 例1 値：Municipal or another local authority | Municipal or another local authority | Municipal or another local authority | Municipal or another local authority | Municipal or another local authority
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0075（1 列）
- 見出し：Type d'exploitant (Français) / Operator Type (French)
- 例1 値：Municipalité ou une autre autorité loca… | Municipalité ou une autre autorité loca… | Municipalité ou une autre autorité loca… | Municipalité ou une autre autorité loca… | Municipalité ou une autre autorité loca…
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…, Méthode de calcul (…

## g0076（1 列）
- 見出し：Volume journalier moyen de l'effluent (m3) / Average Daily E
- 例1 値：409 | 147 | 600 | 0 | 3600
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Méthode de calcul (…, Méthode de calcul (…

## g0077（1 列）
- 見出し：Méthode de calcul (Anglais) / Method of Calculation (English
- 例1 値：Continuous measure of effluent volume d… | Continuous measure of effluent volume d… | Other method of calculation based on me… | Other method of calculation based on me… | Estimate based on generally accepted en…
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…

## g0078（1 列）
- 見出し：Méthode de calcul (Français)/ Method of Calculation (French
- 例1 値：Estimations fondée sur la mesure du déb… | Estimations fondée sur les pratiques d'… | Mesure en continu du volume d'effluent … | Autre méthode de calcul fondée sur les … | Mesure en continu du volume d'effluent …
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…

## g0079（1 列）
- 見出し：Indicateur - Utilisation de chlore (Anglais)/ Chlorine Use I
- 例1 値：No | No | No | No | No
  - 同じ表の列：Identification de l…, Ville/ City, Province (Anglais)/…, Province (Français)…, Type d'exploitant (…, Type d'exploitant (…, Volume journalier m…, Méthode de calcul (…

## g0080（1 列）
- 見出し：Province
- 例1 値：ON | AB | BC | BC | AB
  - 同じ表の列：FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0081（1 列）
- 見出し：FSA
- 例1 値：V4G | T4N | K2R | V8X | L0B
  - 同じ表の列：Province, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0082（1 列）
- 見出し：Number of CLB Beneficiaries as of Dec 31, 2006
- 例1 値：* | * | * | * | *
  - 同じ表の列：Province, FSA, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0083（1 列）
- 見出し：Number of Eligible Children as of Dec 31, 2006
- 例1 値：49 | 391 | 162 | 37 | 270
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0084（1 列）
- 見出し：Cumulative CLB Participation Rate (percent) as of Dec 31, 20
- 例1 値：* | * | * | * | *
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0085（1 列）
- 見出し：Number of CLB Beneficiaries as of Mar 31, 2007
- 例1 値：* | * | * | * | 36
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…

## g0086（1 列）
- 見出し：Number of Eligible Children as of Mar 31, 2007
- 例1 値：290 | * | 115 | 239 | *
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Cumulative CLB Part…, Number of CLB Benef…

## g0087（1 列）
- 見出し：Cumulative CLB Participation Rate (percent) as of Mar 31, 20
- 例1 値：* | 18.0% | * | * | *
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Number of CLB Benef…

## g0088（1 列）
- 見出し：Number of CLB Beneficiaries as of Jun 30, 2007
- 例1 値：* | * | * | * | *
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…

## g0089（1 列）
- 見出し：Number of Eligible Children as of Jun 30, 2007
- 例1 値：114 | 721 | 314 | 118 | 249
  - 同じ表の列：Province, FSA, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…, Number of CLB Benef…, Number of Eligible …, Cumulative CLB Part…

## g0090（1 列）
- 見出し：Sensor_Capteur
- 例1 値：7000_14 | 9000_5 | 7000_12 | 6000_5 | 2000_3
  - 同じ表の列：DoseRateType_TypeDe…, StartTime_HeureDebu…, EndTime_HeureFin (U…, Value_Valeur (nSv/h…

## g0091（1 列）
- 見出し：DoseRateType_TypeDebitDose
- 例1 値：Terrestrial Gamma/Gamma terrestre | Terrestrial Gamma/Gamma terrestre | Terrestrial Gamma/Gamma terrestre | Terrestrial Gamma/Gamma terrestre | Terrestrial Gamma/Gamma terrestre
  - 同じ表の列：Sensor_Capteur, StartTime_HeureDebu…, EndTime_HeureFin (U…, Value_Valeur (nSv/h…

## g0092（1 列）
- 見出し：StartTime_HeureDebut (UTC)
- 例1 値：20250101014500 | 20250101004500 | 20250101020000 | 20250101020000 | 20250101023000
  - 同じ表の列：Sensor_Capteur, DoseRateType_TypeDe…, EndTime_HeureFin (U…, Value_Valeur (nSv/h…

## g0093（1 列）
- 見出し：EndTime_HeureFin (UTC)
- 例1 値：20250101013000 | 20250101023000 | 20250101013000 | 20250101011500 | 20250101021500
  - 同じ表の列：Sensor_Capteur, DoseRateType_TypeDe…, StartTime_HeureDebu…, Value_Valeur (nSv/h…

## g0094（1 列）
- 見出し：Value_Valeur (nSv/hr)
- 例1 値：30 | 29 | 35 | 31 | 50
  - 同じ表の列：Sensor_Capteur, DoseRateType_TypeDe…, StartTime_HeureDebu…, EndTime_HeureFin (U…

## g0095（2 列）
- 見出し：index #
- 例1 値：150 | 154 | 164 | 32 | 191
  - 同じ表の列：VOC Species, CAS #, MDL, season, Exposure Category, Count, Min, Max
- 例2 値：66 | 128 | 33 | 101 | 29
  - 同じ表の列：VOC Species, CAS #, MDL, Season, Exposure Category, Count, Min, Max

## g0096（1 列）
- 見出し：VOC Species
- 例1 値：1-Butyne | Methylcyclopentane | 2,3-Dimethylpentane | Acetaldehyde | c-1,3-Dichloropropene
  - 同じ表の列：index #, CAS #, MDL, season, Exposure Category, Count, Min, Max

## g0097（2 列）
- 見出し：CAS #
- 例1 値：565-75-3 | 589-53-7 | 526-73-8 | 75-07-0 | 100-41-4
  - 同じ表の列：index #, VOC Species, MDL, season, Exposure Category, Count, Min, Max
- 例2 値：123-72-8 | 74-86-2 | 109-67-1 | 1077-16-3 | 76-13-1
  - 同じ表の列：Index #, VOC Species, MDL, Season, Exposure Category, Count, Min, Max

## g0098（2 列）
- 見出し：MDL
- 例1 値：0.026440359 | 0.049407608 | 0.035490055 | 0.053913857 | 0.016
  - 同じ表の列：index #, VOC Species, CAS #, season, Exposure Category, Count, Min, Max
- 例2 値：0.06 | 0.015 | 0.027 | 0.017 | 0.042
  - 同じ表の列：Index #, VOC Species, CAS #, Season, Exposure Category, Count, Min, Max

## g0099（2 列）
- 見出し：season
- 例1 値：Winter | Summer | Winter | Summer | Winter
  - 同じ表の列：index #, VOC Species, CAS #, MDL, Exposure Category, Count, Min, Max
- 例2 値：winter | summer | winter | summer | summer
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Exposure Category, Count, Min, Max

## g0100（2 列）
- 見出し：Exposure Category
- 例1 値：Outdoor | Indoor | Indoor | Outdoor | Indoor
  - 同じ表の列：index #, VOC Species, CAS #, MDL, season, Count, Min, Max
- 例2 値：indoor | outdoor | indoor | indoor | indoor
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Season, Count, Min, Max

## g0101（2 列）
- 見出し：Count
- 例1 値：328 | 324 | 324 | 337 | 328
  - 同じ表の列：index #, VOC Species, CAS #, MDL, season, Exposure Category, Min, Max
- 例2 値：287 | 331 | 324 | 324 | 287
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Season, Exposure Category, Min, Max

## g0102（1 列）
- 見出し：Min
- 例1 値：<MDL | <MDL | <MDL | <MDL | <MDL
  - 同じ表の列：index #, VOC Species, CAS #, MDL, season, Exposure Category, Count, Max

## g0103（2 列）
- 見出し：Max
- 例1 値：3.616 | 11.647 | 0.223 | 11.035 | 0.187
  - 同じ表の列：index #, VOC Species, CAS #, MDL, season, Exposure Category, Count, Min
- 例2 値：21.55 | 700.8 | 0.058 | 70.27 | 0.32
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Season, Exposure Category, Count, Min

## g0104（1 列）
- 見出し：% Samples > MDL
- 例1 値：5.1 | 99.1 | 0.3 | 55.2 | 33.8
  - 同じ表の列：index #, VOC Species, CAS #, MDL, season, Exposure Category, Count, Min

## g0105（1 列）
- 見出し：VOC Species
- 例1 値：Ethylene | Bromotrichloromethane | 2,5-Dimethylhexane | Acrylonitrile (2-Propennitrile) | Isobutylacetate
  - 同じ表の列：Index #, CAS #, MDL, Season, Exposure Category, Count, Min, Max

## g0106（1 列）
- 見出し：Min
- 例1 値：0.14 | 0.08 | <MDL | 0.168 | <MDL
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Season, Exposure Category, Count, Max

## g0107（1 列）
- 見出し：% Samples > MDL
- 例1 値：55.45 | 4.53 | 100 | 98.72 | 7.72
  - 同じ表の列：Index #, VOC Species, CAS #, MDL, Season, Exposure Category, Count, Min

## g0108（1 列）
- 見出し：Sample Type / Type d'échantillon
- 例1 値：Vapour/Vapeur | Vapour/Vapeur | Vapour/Vapeur | Vapour/Vapeur | Vapour/Vapeur
  - 同じ表の列：Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0109（1 列）
- 見出し：Month/Mois
- 例1 値：7 | 11 | 5 | 4 | 1
  - 同じ表の列：Sample Type / Type …, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0110（1 列）
- 見出し：Year/Année
- 例1 値：2003 | 2005 | 2001 | 2003 | 2003
  - 同じ表の列：Sample Type / Type …, Month/Mois, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0111（1 列）
- 見出し：Location/Emplacement
- 例1 値：LE3 | LE7 | LE4 | GE4 | GE9
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0112（1 列）
- 見出し：Volume Collected/Volume prélevé (L)
- 例1 値：0.02 | 0.02 | 0.02 | 0.02 | 0.02
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0113（1 列）
- 見出し：Activity/Activité (Bq/L)
- 例1 値：5.5 | -2.5 | 11.3 | 59.5 | 40.7
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Error/Erreur (Bq/L), Activity/Activité (…, Error/Erreur (Bq/m^…

## g0114（1 列）
- 見出し：Error/Erreur (Bq/L)
- 例1 値：2.7 | 3.3 | 3.1 | 3 | 3.5
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Activity/Activité (…, Error/Erreur (Bq/m^…

## g0115（1 列）
- 見出し：Activity/Activité (Bq/m^3)
- 例1 値：0.034 | 1.42 | 0.027 | 0.051 | 0.001
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Error/Erreur (Bq/m^…

## g0116（1 列）
- 見出し：Error/Erreur (Bq/m^3)
- 例1 値：0.012 | 0.015 | 0.035 | 0.015 | 0.019
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…

## g0117（1 列）
- 見出し：Comments/Commentaires
- 例1 値：Saturated/Saturée | Saturated/Saturée | Saturated/Saturée | Saturated/Saturée
  - 同じ表の列：Sample Type / Type …, Month/Mois, Year/Année, Location/Emplacement, Volume Collected/Vo…, Activity/Activité (…, Error/Erreur (Bq/L), Activity/Activité (…

## g0118（1 列）
- 見出し：Session
- 例1 値：29 | 15 | 34 | 34 | 12
  - 同じ表の列：Format, Format_2, Source Language, Langue d’origine, Priority, Priorité, Region of Session (…, Région de la séance…

## g0119（1 列）
- 見出し：Format
- 例1 値：Engagement Session | Engagement Session | Engagement Session | Engagement Session | Engagement Session
  - 同じ表の列：Session, Format_2, Source Language, Langue d’origine, Priority, Priorité, Region of Session (…, Région de la séance…

## g0120（1 列）
- 見出し：Format_2
- 例1 値：Séances de mobilisation | Séances de mobilisation | Séances de mobilisation | Formulaire de réponse individuel | Séances de mobilisation
  - 同じ表の列：Session, Format, Source Language, Langue d’origine, Priority, Priorité, Region of Session (…, Région de la séance…

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
