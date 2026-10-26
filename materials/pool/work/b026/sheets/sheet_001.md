# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：Fiscal Year
- 例1 値：2020-2021 | 2020-2021 | 2020-2021 | 2021-2022 | 2021-2022
  - 同じ表の列：Organization, Core Responsibility, Program, Program Outcome, indicator
- 例2 値：2021-2022 | 2021-2022 | 2021-2022 | 2020-2021 | 2021-2022
  - 同じ表の列：Organization, Core Responsibility, Departmental Results, Indicator, Published on the Op…

## g0002（2 列）
- 見出し：Organization
- 例1 値：Department of National Defence | Department of National Defence | Department of National Defence | Department of National Defence | Department of National Defence
  - 同じ表の列：Fiscal Year, Core Responsibility, Program, Program Outcome, indicator
- 例2 値：Department of National Defence | Department of National Defence | Department of National Defence | Department of National Defence | Department of National Defence
  - 同じ表の列：Fiscal Year, Core Responsibility, Departmental Results, Indicator, Published on the Op…

## g0003（1 列）
- 見出し：Core Responsibility
- 例1 値：Future Force Design | Defence Team | Operations | Procurement of Capabilities | Defence Team
  - 同じ表の列：Fiscal Year, Organization, Program, Program Outcome, indicator

## g0004（1 列）
- 見出し：Program
- 例1 値：Ombudsman | Ready Air and Space Forces | Ready Naval Forces | Defence Materiel Management | Naval Bases
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Program Outcome, indicator

## g0005（1 列）
- 見出し：Program Outcome
- 例1 値：Canadian Armed Forces museums are well … | Canadian Armed Forces has the required … | Land Bases provide services to integral… | Royal Canadian Air Force fleets are ser… | Maritime force elements are deployable …
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Program, indicator

## g0006（1 列）
- 見出し：indicator
- 例1 値：Degree to which Residential Housing was… | Status of Services Provided by Naval Ba… | % of the Chief of the Defence Staff Tas… | % of Canadian Forces Intelligence Comma… | % of Land equipment that is servicable …
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Program, Program Outcome

## g0007（1 列）
- 見出し：Core Responsibility
- 例1 値：Operations | Defence Team | Ready Forces | Defence Team | Operations
  - 同じ表の列：Fiscal Year, Organization, Departmental Results, Indicator, Published on the Op…

## g0008（1 列）
- 見出し：Departmental Results
- 例1 値：The Defence team reflects the values an… | Defence capabilities are designed to me… | Canadian Armed Forces is growing toward… | Supplies are available and well-managed | Defence information technology acquisit…
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Indicator, Published on the Op…

## g0009（1 列）
- 見出し：Indicator
- 例1 値：% of maritime key fleets that are servi… | Number and type of actions taken in res… | Degree to which future security assessm… | % of light-duty vehicle fleet that is h… | % of Canadian Armed Forces families who…
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Departmental Results, Published on the Op…

## g0010（1 列）
- 見出し：Published on the Open government portal
- 例1 値：No | Yes | No | Yes | No
  - 同じ表の列：Fiscal Year, Organization, Core Responsibility, Departmental Results, Indicator

## g0011（1 列）
- 見出し：ColonyID
- 例1 値：WN_14_2015 | NP_16_2015 | NP-56-2015 | WN_29_2009 | NP_15_2015
  - 同じ表の列：Year, Month, Day, Easting, Northing, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0012（1 列）
- 見出し：Year
- 例1 値：2015 | 2015 | 2009 | 2009 | 2009
  - 同じ表の列：ColonyID, Month, Day, Easting, Northing, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0013（1 列）
- 見出し：Month
- 例1 値：11 | 11 | 10 | 10 | 10
  - 同じ表の列：ColonyID, Year, Day, Easting, Northing, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0014（1 列）
- 見出し：Day
- 例1 値：19 | 20 | 20 | 22 | 10
  - 同じ表の列：ColonyID, Year, Month, Easting, Northing, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0015（1 列）
- 見出し：Easting
- 例1 値：438981 | 436450 | 450449 | 434564 | 439006
  - 同じ表の列：ColonyID, Year, Month, Day, Northing, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0016（1 列）
- 見出し：Northing
- 例1 値：5532302 | 5497458 | 5514020 | 5475338 | 5530057
  - 同じ表の列：ColonyID, Year, Month, Day, Easting, Ecoregion, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0017（1 列）
- 見出し：Ecoregion
- 例1 値：NorthernPeninsula | NorthernPeninsula | Écorégion | NorthernPeninsula | NorthernPeninsula
  - 同じ表の列：ColonyID, Year, Month, Day, Easting, Northing, Dam Presence (Y/N), Lodge Presence (Y/N)

## g0018（1 列）
- 見出し：Dam Presence (Y/N)
- 例1 値：Y | Y | N | Y | Y
  - 同じ表の列：ColonyID, Year, Month, Day, Easting, Northing, Ecoregion, Lodge Presence (Y/N)

## g0019（1 列）
- 見出し：Lodge Presence (Y/N)
- 例1 値：Y | N | Y | Y | N
  - 同じ表の列：ColonyID, Year, Month, Day, Easting, Northing, Ecoregion, Dam Presence (Y/N)

## g0020（1 列）
- 見出し：Browse Cache Presence (Y/N)
- 例1 値：N | Y | N | Y | N
  - 同じ表の列：ColonyID, Year, Month, Day, Easting, Northing, Ecoregion, Dam Presence (Y/N)

## g0021（1 列）
- 見出し：fy_ef
- 例1 値：2014-15 | 2013-14 | 2013-14 | 2014-15 | 2014-15
  - 同じ表の列：organization, estimates_document, vote_number, vote_type, authorities

## g0022（1 列）
- 見出し：organization
- 例1 値：Department of Housing, Infrastructure a… | Copyright Board | Canadian Centre for Occupational Health… | Royal Canadian Mounted Police External … | International Joint Commission (Canadia…
  - 同じ表の列：fy_ef, estimates_document, vote_number, vote_type, authorities

## g0023（1 列）
- 見出し：estimates_document
- 例1 値：Main Estimates | Other voted adjustments | Main Estimates | Other voted adjustments | Main Estimates
  - 同じ表の列：fy_ef, organization, vote_number, vote_type, authorities

## g0024（1 列）
- 見出し：vote_number
- 例1 値：30 | 16 | 1 | 1 | 30
  - 同じ表の列：fy_ef, organization, estimates_document, vote_type, authorities

## g0025（1 列）
- 見出し：vote_type
- 例1 値：Operating/Program | Operating/Program | Operating/Program | Operating/Program | Payments to Crown Corps
  - 同じ表の列：fy_ef, organization, estimates_document, vote_number, authorities

## g0026（1 列）
- 見出し：authorities
- 例1 値：13457.00 | 37870228.00 | 1310000.00 | 3090000.00 | 17815785.00
  - 同じ表の列：fy_ef, organization, estimates_document, vote_number, vote_type

## g0027（1 列）
- 見出し：ai_register_id
- 例1 値：2526-AAFC-AAC-012 | 2526-DFO-MPO-016 | 2526-CSPS-EFPC-005 | 2526-HICC-LICC-002 | 2526-LAC-BAC-006
  - 同じ表の列：government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en, ai_system_status_fr

## g0028（1 列）
- 見出し：government_organization
- 例1 値：Employment and Social Development Canad… | Department of Justice Canada / Ministèr… | Indigenous Services Canada / Services a… | Environment and Climate Change Canada /… | Canadian Heritage / Patrimoine canadien
  - 同じ表の列：ai_register_id, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en, ai_system_status_fr

## g0029（1 列）
- 見出し：ai_system_primary_users_en
- 例1 値：GC employees | GC employees | GC employees | GC employees | GC employees
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en, ai_system_status_fr

## g0030（1 列）
- 見出し：ai_system_primary_users_fr
- 例1 値：Employés du GC | Employés du GC | Employés du GC | Employés du GC | Employés du GC
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en, ai_system_status_fr

## g0031（1 列）
- 見出し：developed_by_en
- 例1 値：Vendor | Government of Canada | Government of Canada | Government of Canada | Open source
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_fr, vendor_information, ai_system_status_en, ai_system_status_fr

## g0032（1 列）
- 見出し：developed_by_fr
- 例1 値：Gouvernement du Canada | Gouvernement du Canada | Gouvernement du Canada | Fournisseur | Gouvernement du Canada
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, vendor_information, ai_system_status_en, ai_system_status_fr

## g0033（1 列）
- 見出し：vendor_information
- 例1 値：MDA Inc, Subs | Transitional Forms | Microsoft | Microsoft | CGI Group Inc.
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, ai_system_status_en, ai_system_status_fr

## g0034（1 列）
- 見出し：ai_system_status_en
- 例1 値：In production | In production | In development | In development | In production
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_fr

## g0035（1 列）
- 見出し：ai_system_status_fr
- 例1 値：En production | En production | En cours de développement | Mis hors service | En production
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en

## g0036（1 列）
- 見出し：status_date
- 例1 値：2025 | 2024 | 2025 | 2019 | 2026
  - 同じ表の列：ai_register_id, government_organiza…, ai_system_primary_u…, ai_system_primary_u…, developed_by_en, developed_by_fr, vendor_information, ai_system_status_en

## g0037（1 列）
- 見出し：Federal organization
- 例1 値：Natural Resources Canada | Agriculture and Agri-Food Canada | Parks Canada | Canada Border Services Agency | Employment and Social Development Canada
  - 同じ表の列：Fiscal year, GHG source, GHG scope, Energy category, Energy use (GJ), Emissions (kt)

## g0038（1 列）
- 見出し：Fiscal year
- 例1 値：FY2015-16 | FY2017-18 | FY2005-06 | FY2014-15 | FY2012-13
  - 同じ表の列：Federal organization, GHG source, GHG scope, Energy category, Energy use (GJ), Emissions (kt)

## g0039（1 列）
- 見出し：GHG source
- 例1 値：fleet | fleet | fleet | fleet | fleet
  - 同じ表の列：Federal organization, Fiscal year, GHG scope, Energy category, Energy use (GJ), Emissions (kt)

## g0040（1 列）
- 見出し：GHG scope
- 例1 値：1 | 2 | 1 | 1 | 1
  - 同じ表の列：Federal organization, Fiscal year, GHG source, Energy category, Energy use (GJ), Emissions (kt)

## g0041（1 列）
- 見出し：Energy category
- 例1 値：natural gas | gasoline | district cooling | aviation fuel | Gasoline
  - 同じ表の列：Federal organization, Fiscal year, GHG source, GHG scope, Energy use (GJ), Emissions (kt)

## g0042（1 列）
- 見出し：Energy use (GJ)
- 例1 値：45312.71353 | 0.040 | 126115.6032 | 2918.92726 | 50899.99939
  - 同じ表の列：Federal organization, Fiscal year, GHG source, GHG scope, Energy category, Emissions (kt)

## g0043（1 列）
- 見出し：Emissions (kt)
- 例1 値：0.0553314 | 0.000 | 12.0480611 | 40.3049962 | 1.4013619
  - 同じ表の列：Federal organization, Fiscal year, GHG source, GHG scope, Energy category, Energy use (GJ)

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
```
