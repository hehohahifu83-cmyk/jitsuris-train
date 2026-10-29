# 不明になった列の調査 002 / 003（1 列ずつ）

公開データの表の列です。今の仕組みはこれらの列に種類を付けられず「不明」と答えました。人が見て決められるか、決められるなら何が決め手かを知りたい調査です。

- **1 列ずつ**、LABEL_GUIDE.md（v2.1）のどの種類かを答える。決められなければ `unknown`。
- **決め手**を次から 1 つ（いちばん効いたもの）：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない
- メモは短く（なぜそう決めたか、何があれば決められたか）。日本語で。
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を写し、ChatGPT は `research/unknown/answers_chatgpt/sheet_NNN.tsv`、Grok は `research/unknown/answers_grok/sheet_NNN.tsv` に置く。1 行＝「u0001<TAB>ラベル<TAB>決め手<TAB>メモ」
- **見ないもの**：`research/unknown/columns.jsonl`・`sheet_index.json`（正解と今の仕組みの答えが入っている）、もう一人の先生の答え、モデルの予測

## u0111 — 見出し「organisationuri」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：sitereference, hectares, planningstatus, permissiontype, permissiondate, deliverable, netdwellingsrangefrom, netdwellingsrangeto, firstaddeddate

## u0112 — 見出し「Payroll staff costs」
- 値：Salary | ｣72,902,946 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsor…, Payroll staff, Number of non-payroll st…, Grand Total  (workforce …, Non-Payroll staff (conti…, Grand Total paybill/staf…, Comments and notes

## u0113 — 見出し「quelle_code」
- 値：1 | 1 | 1 | 1 | 1 | 1 | 1 | 2
- 同じ表の列名：jahr, zeithorizonttyp, quelle_gebietart, ziel_gebietart, ziel_code, verkehrsmittel, wert, einheit, gebietsstand

## u0114 — 見出し「Delegated grades」
- 値：Annual Paybill  (delegated gra… | ｣1,155,895,066 | ｣192,481,571 | ｣96,284,000 | ｣37,869,317 | ｣15,428,000
- 同じ表の列名：Main  department, Organisation, SCS on standard contract…, Information for SCS on n…, Comments

## u0115 — 見出し「Cost Centre」
- 値：1002 | 2112 | 1201 | 1101 | 0000 | 0000 | 0000
- 同じ表の列名：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number, Amount in Sterling

## u0116 — 見出し「Payroll staff costs」
- 値：Salary | ｣359,334.04
- 同じ表の列名：Organisation  type, Main, parent or  sponsor…, Payroll staff, Number of non-payroll st…, Grand Total  (workforce …, Non-Payroll staff (conti…, Grand Total paybill/staf…

## u0117 — 見出し「referenztarif」
- 値：683 | 701 | 360 | 698 | 696 | 365 | 587 | 695
- 同じ表の列名：bereich, tarifstruktur, waehrung, gueltig_ab

## u0118 — 見出し「Summe von SG 0」
- 値：0 | 0 | 10 | 598 | 0 | 0 | 15 | 1617
- 同じ表の列名：Titel, Fachgebiet, Versuchszweck, Tierart, Summe von SG 1, Summe von SG 2, Summe von SG 3

## u0119 — 見出し「Delegated grades only」
- 値：Annual Paybill  (delegated gra… | ｣91,579,510 | ｣40,929,943 | ｣60,231,276
- 同じ表の列名：Main department, Organisation, SCS on standard contract…, Information for SCS on n…

## u0120 — 見出し「biomasse_kwh」
- 値：75289240.0 | 75843725.0 | 75705213.0 | 74721273.0 | 84887134.0 | 86258045.0 | 87595049.0 | 81478464.0
- 同じ表の列名：jahr, wind_kwh, abfall_kwh, trinkwasserkraftwerk_kwh, klein_wasserkraftwerk_kw…, photovoltaik_kwh, wasserkraft_kwh

## u0121 — 見出し「Metal ores」
- 値：234140400 | 217336500 | 225465800 | 253387400 | 254395200 | 257881300 | 256568800 | 241431400
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Biomass, Fossil fuels, Non-metallic minerals, Total (All categories)

## u0122 — 見出し「Payscale Minimum (｣)」
- 値：21916 | 25000 | 21916 | 33200 | 21916 | 55431 | 33200 | 33200
- 同じ表の単位の列：Unit: Early Years, Extended Schools and Specia, Safeguarding…
- 同じ表の列名：Parent Department, Organisation, Unit, Reporting Senior Post, Grade, Payscale Maximum (｣), Generic Job Title, Number of Posts in FTE, Professional/Occupationa…

## u0123 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0124 — 見出し「bruttolastgang_kwh」
- 値：11054.566 | 11076.963 | 11679.194 | 10279.515 | 19737.958 | 18026.844 | 21017.563 | 12627.383
- 同じ表の列名：zeitpunkt

## u0125 — 見出し「Arrest/Detention > Assault」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Child…, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immig…, Arrest/Detention > Moder…, Arrest/Detention > Murde…

## u0126 — 見出し「ServiceTypeURI」
- 値：http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5…
- 同じ表の列名：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeLabel, CoordinateReferenceSyste…, GeoX, GeoY, GeoPointLicensingURL, Category

## u0127 — 見出し「wert」
- 値：66 | 0 | 0 | 0 | 0 | 0 | 30 | 0
- 同じ表の列名：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, einheit, gebietsstand

## u0128 — 見出し「principal_dwelling_houses__fixed_rate__over_3_years__rates_o」
- 値：3.94 | 3.83 | 3.37 | 3.36 | 3.34 | 3.24 | 3.23 | 3.22
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0129 — 見出し「Structure」
- 値：Church - Parochial Hall | Lifeboat House -The Comhaltas … | Anchor | The Handball Alley | Grimshaw’s Lodge, | Ruin of The Cholera House, | Signal room and waiting room o… | Saint Nathi’s / Round Mount
- 表の題名：Protected Structures Wicklow Rathnew (CDP 2022 - 2028)
- 同じ表の列名：X, Y, ID, RPS_Number, Location, OBJECTID

## u0130 — 見出し「pubdate」
- 値：1680 | 1680 | 1656 | 1680 | 1656
- 同じ表の列名：catalog_id_swisscovery, page_id_erara, erara_page_view, swisscovery_link, pubdate_from, pubdate_to, creator, publisher, reference

## u0131 — 見出し「temporal」
- 値：2024-M04 | 2026-M03 | 2026-M04 | 2023-M03 | 2024-M02 | 2025-M04 | 2023-M04 | 2024-M11
- 同じ表の列名：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type, value

## u0132 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：WKT, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate

## u0133 — 見出し「Under $5,000 / Moins de 5 000 $」
- 値：8020 | 9560 | 6880 | 5540 | 6040 | 920 | 520 | 1110
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Tot…, Total Income / Revenu to…, $5,000 to $9,999 / 5 000…, $10,000 to $14,999 / 10 …, $15,000 to $19,999 / 15 …, $20,000 to $24,999 / 20 …

## u0134 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, SiteplanURL, GeoY, GeoX, Hectares, Deliverable, PlanningStatus, PermissionType, PermissionDate

## u0135 — 見出し「Number」
- 値：712 | 149 | 11976 | 10655 | 279 | 1042 | 12020 | 9674
- 同じ表の列名：YearWeekIso, LastDayOfWeek, Variable

## u0136 — 見出し「Maturitaetsquote_gymnasial」
- 値：16.38 | 14.01 | 48.81 | 16.1 | 10.14 | 1.61 | 14.63 | 33.08
- 同じ表の列名：Stand, Stand_Gemeindegrenzen, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gymnasia…, Total_19_Jahre_alt

## u0137 — 見出し「beitrag_chf_pro_projekt」
- 値：247.5 | 1200.0 | 4500.0 | 2700.0 | 1000.0 | 1000.0 | 1500.0 | 1000.0
- 同じ表の列名：id, jahr, kategorie, unterstutztes_projekt, begunstigte

## u0138 — 見出し「TLIST(A1)」
- 値：1992 | 1993 | 1993 | 1993 | 1994 | 1995 | 1995 | 1996
- 表の題名：EDA36 - Percentage of persons aged 20-24 years having Comple…
- 同じ表の単位の列：UNIT: %
- 同じ表の列名：STATISTIC, Statistic, Year, C02199V02655, Sex, UNIT, VALUE

## u0139 — 見出し「Emp_Wkf_POPD_15+yrs_2023」
- 値：1,242,188.46500 | 850,937.51060 | 583,815.02590 | 2,676,941.00150 | 156,672.76460 | 318,318.66920 | 212,785.51820 | 44,370.78162
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0140 — 見出し「Arrest/Detention > Immigration」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Child…, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Moder…, Arrest/Detention > Murde…

## u0141 — 見出し「service」
- 値：Find Business Regulation (FBR) | Report a Trade Barrier (RaTB) | Regulated Professions Register… | Business.gov.uk | Trade Remedies Service (TRS) | Business.gov.uk | Digital Market Access Service … | Report a Breach (RaB)
- 同じ表の列名：reporting_month, portfolio, users, sessions, cumulative_users

## u0142 — 見出し「Quarter」
- 値：1979Q1 | 1979Q2 | 1982Q3 | 1991Q2 | 1992Q4 | 2001Q2 | 1981Q2 | 1987Q1
- 表の題名：HSQ08 - House Loans Approved and Paid
- 同じ表の単位の列：UNIT: Number, Euro Million
- 同じ表の列名：STATISTIC, Statistic, TLIST(Q1), C02350V02827, House Type New or Second…, UNIT, VALUE

## u0143 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0144 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory

## u0145 — 見出し「Emp_Wkf_POPD_15+yrs_2025」
- 値：1,227,114.17300 | 894,414.05980 | 609,571.58220 | 2,731,099.81500 | 167,351.77280 | 324,530.32080 | 205,582.51470 | 44,294.62793
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0146 — 見出し「Titel」
- 値：Parkhaus Storchen | Parkhaus Storchen | Parkhaus Elisabethen | Parkhaus Messe | Parkhaus Kunstmuseum | Parkhaus Steinen | Parkhaus Europe | Parkhaus Rebgasse
- 同じ表の列名：Publikationszeit, Anzahl frei, Total Plätze, Anteil belegter Parkplät…, id, id2, link, geo_point_2d, Beschreibung

## u0147 — 見出し「monitoring_program」
- 値：BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI
- 同じ表の単位の列：unit: CFU/100ml
- 同じ表の列名：station_number, latidude, date_of_probing, parameter_type, value, lower_LOD, unit

## u0148 — 見出し「Type of Aid」
- 値：C01 | C01 | C01 | C01 | C01 | D02 | C01 | C01
- 同じ表の列名：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country Code, Input Sector code, Channel of Delivery Code, Type of Flow, Type of Finance

## u0149 — 見出し「EW_Total_Company_SA」
- 値：[x] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA

## u0150 — 見出し「wind_kwh」
- 値：4271000.0 | 4773000.0 | 4400000.0 | 4465000.0 | 4379000.0 | 4541000.0 | 4639000.0 | 4920000.0
- 同じ表の列名：jahr, biomasse_kwh, abfall_kwh, trinkwasserkraftwerk_kwh, klein_wasserkraftwerk_kw…, photovoltaik_kwh, wasserkraft_kwh

## u0151 — 見出し「DiffMedianHourlyPercent」
- 値：4.80 | -16.00 | -7.40 | 9.70 | 14.10 | 15.40 | 6.60 | 19.90
- 同じ表の列名：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent, MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile

## u0152 — 見出し「principal_dwelling_houses__floating_rate__up_to_1_year_fixed」
- 値：3.33 | 3.33 | 3.54 | 3.5 | 3.51 | 3.53 | 3.49 | 3.42
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0153 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：EffectiveDate, ServiceCategoryLabel, ServiceCategoryURI, Licence, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDescripti…, DiscretionaryReliefDescr…

## u0154 — 見出し「EntertainmentTypeURI」
- 値：http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain… | http://id.esd.org.uk/entertain…
- 同じ表の列名：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeLabel, LateNightRefreshment

## u0155 — 見出し「C02350V02827」
- 値：2 | 1 | 1 | 1 | 2 | 2 | 1 | 2
- 表の題名：HSQ08 - House Loans Approved and Paid
- 同じ表の単位の列：UNIT: Number, Euro Million
- 同じ表の列名：STATISTIC, Statistic, TLIST(Q1), Quarter, House Type New or Second…, UNIT, VALUE

## u0156 — 見出し「EW_Total_Company_NSA」
- 値：3597 | 3520 | 2553 | 2567 | 5067 | 5615 | 4700 | 5689
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA

## u0157 — 見出し「EW_Admin_SA」
- 値：[z] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA

## u0158 — 見出し「Total der Gemeinden」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Titel, Datum, Verwaltungsebene, Typ, Status, Ausgezählte Gemeinden, Letzte Änderung, Stimmbeteiligung

## u0159 — 見出し「Price (K)」
- 値：9250 | 8683 | 25497 | 14900 | 14900
- 同じ表の列名：Reference Number (B), Title of Agreement (C ), Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Value (L), Tender Process (N)

## u0160 — 見出し「ServiceCategoryURI」
- 値：http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5… | http://id.esd.org.uk/service/5…
- 同じ表の列名：OrganisationURI, EffectiveDate, ServiceCategoryLabel, Licence, PropertyRef, Occupied, ExemptionDescription, MandatoryReliefDescripti…, DiscretionaryReliefDescr…

## u0161 — 見出し「electorat」
- 値：1'381 | 10'712 | 555 | 4'976 | 4'769 | 6'003 | 5'425 | 2'867
- 同じ表の列名：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc, q1_valables

## u0162 — 見出し「Got none of what I wanted」
- 値：16.5 | 16.6 | 24.6 | 5 | 14 | 33.3 | 19 | 63
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wante…, Got some of what I wante…, Very Satisfied, Satisfied, Neither satisfied nor di…

## u0163 — 見出し「終了日（日）」
- 値：25 | 25 | 25 | 25 | 25 | 25 | 25 | 25
- 表の題名：気象観測_最新の気象データ
- 同じ表の列名：観測所番号, 都道府県, 地点, 国際地点番号, 終了日（年）, 終了日（月）, 前5日間平均気温（℃）, 前5日間平均気温の品質情報, 前5日間平均気温平年差（℃）

## u0164 — 見出し「Arrest/Detention > Modern Slavery / Human Trafficking」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Child…, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immig…, Arrest/Detention > Murde…

## u0165 — 見出し「pop」
- 値：8644780 | 8778099 | 8855062 | 9127125 | NA | NA | NA | NA
- 同じ表の列名：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## u0166 — 見出し「Lim_min」
- 値：151 | 1023 | 879 | 1038 | 885 | 129 | 1101 | 1119
- 同じ表の列名：AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_sup, Exces

## u0167 — 見出し「5」
- 値：ツル目 | チドリ目 | ペリカン目 | スズメ目 | チドリ目 | チドリ目 | スズメ目 | スズメ目
- 表の題名：レッドリスト/レッドデータブック_第５次レッドリスト
- 同じ表の列名：1, 2, 3, 4, 6, 7, 8, 9, 10

## u0168 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus, PermissionType

## u0169 — 見出し「MCC」
- 値：5970 | 7392 | 7392 | 9399 | 7372 | 9399 | 4722
- 同じ表の列名：Post Date, Amount, Reference Number, Code

## u0170 — 見出し「Payscale Maximum (｣)」
- 値：32232 | 40828 | 32232 | 49008 | 32232 | 69187 | 49008 | 49008
- 同じ表の単位の列：Unit: Early Years, Extended Schools and Specia, Safeguarding…
- 同じ表の列名：Parent Department, Organisation, Unit, Reporting Senior Post, Grade, Payscale Minimum (｣), Generic Job Title, Number of Posts in FTE, Professional/Occupationa…

## u0171 — 見出し「@Caption」
- 値：@Creator | @Date | @Language | @@Title | @@Unit | xsd:string | 2003.03 | 2010.03
- 表の題名：情報通信白書_令和2年版(7)
- 同じ表の列名：通信サービス加入契約数の推移

## u0172 — 見出し「gesamtausgaben」
- 値：17656971.06 | 16638854.31 | 14957478.94 | 14369818.41 | 13867888.51 | 13542518.95 | 13048225.23 | 13230171.83
- 同じ表の列名：jahr, raumeinheit, bruttoinlandprodukt, staatsquote_in_prozent

## u0173 — 見出し「abfall_kwh」
- 値：57342000.0 | 54452000.0 | 40137000.0 | 40334000.0 | 40100000.0 | 43000000.0 | 44000000.0 | 48000000.0
- 同じ表の列名：jahr, biomasse_kwh, wind_kwh, trinkwasserkraftwerk_kwh, klein_wasserkraftwerk_kw…, photovoltaik_kwh, wasserkraft_kwh

## u0174 — 見出し「Got everything I wanted」
- 値：31.8 | 20 | 20.1 | 23 | 24 | 26 | 37.15 | 11
- 同じ表の列名：Data status, Department, Organisation, Got most of what I wante…, Got some of what I wante…, Got none of what I wante…, Very Satisfied, Satisfied, Neither satisfied nor di…

## u0175 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, PreviouslyPartOf, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable

## u0176 — 見出し「SMR 2024」
- 値：1.0 | 0.0 | 1.0 | * | * | 0.0 | 2.3 | 2.2
- 同じ表の列名：institution, indicator, taux observe 2019-2023, taux attendu 2019-2023, SMR 2019-2023, nombre de cas 2019-2023, taux observe 2024, taux attendu 2024, nombre de cas 2024

## u0177 — 見出し「Dwellings value」
- 値：nil | nil | 82 | nil | 579 | 99 | 354 | 292
- 同じ表の列名：Valuation Band  Range, Intervening bands, Tenure Status

## u0178 — 見出し「Annual Paybill (delegated grades for financial year 2012/13)」
- 値：｣188,773,159 | ｣1,534,337,826 | ｣510,683,980 | ｣12,418,723 | ｣4,283,902 | ｣888,962 | ｣1,393,088 | ｣22,589,670
- 同じ表の列名：Main department, Organisation, Headcount (delegated gra…, Cost of in-year NCPRP fo…, Number of staff in deleg…, Number of staff in deleg…, Median NCPRP for those r…, Cost of end of year NCPR…, Number of staff in deleg…

## u0179 — 見出し「Surplus Spend」
- 値：893116
- 同じ表の列名：OrganisationURI, IncomeType, IncomeAmount, Expenditure Type, Expenditure Amount

## u0180 — 見出し「date_of_publication_or_production」
- 値：28.07.1780 - 28.12.1780 | 01.01.1781 - 30.12.1781 | 01.01.1782 - 30.12.1782 | 01.01.1783 - 30.12.1783 | 01.01.1784 - 30.12.1784 | 02.01.1785 - 30.12.1785 | 01.01.1787 - 31.12.1787 | 01.01.1788 - 31.12.1788
- 同じ表の列名：library_call_number, digital_reproduction, title, place_of_publication_or_…, date_of_publication_or_p…, series, digital_reproduction_cop…, digital_object_identifie…, digital_platform

## u0181 — 見出し「ServiceTypeURI」
- 値：http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4… | http://id.esd.org.uk/service/4…
- 同じ表の列名：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeLabel, CarParkLocationText, CoordinateReferenceSyste…, GeoX, GeoY, GeoPointLicensingURL

## u0182 — 見出し「Map preview filesize (Megabytes)」
- 値：0.02 | 0.55 | 0.6 | 0.43 | 0.53
- 表の題名：Historical flood map series—Queensland
- 同じ表の列名：Title, Publication Date, Map Scale, Map preview, Download link, Download filesize (Megab…, Download Format, Copyright status, Conditions of Use

## u0183 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0184 — 見出し「Tree」
- 値：2519, 3508 | 842 | 553 | 2664, 174
- 表の題名：Ballarat Historical Naming Index
- 同じ表の列名：Type, Site, Locality, Ward, Authority, See Entry, Not in use, Unknown / uncertain, Beyond Maps

## u0185 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：ogc_fid, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate

## u0186 — 見出し「wert」
- 値：637 | 5 | 12 | 0 | 55 | 5 | 30 | 16
- 同じ表の列名：jahr, fallstruktur, metrik, einheit

## u0187 — 見出し「principal_dwelling_houses__fixed_rate__from_1_to_3_years__ra」
- 値：4.49 | 4.31 | 3.7 | 3.6 | 3.53 | 3.47 | 3.39 | 3.33
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0188 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0189 — 見出し「Time period」
- 値：12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award
- 同じ表の列名：Grant recipient, Registration number, amount allocated, Date of award

## u0190 — 見出し「OrganisationURI」
- 値：http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/…
- 同じ表の列名：OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Purpose, Payment Date, Amount

## u0191 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory

## u0192 — 見出し「STATISTIC」
- 値：STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE | STOCKNURSE
- 表の題名：JQ06 – Stock of nurses by country of first qualification
- 同じ表の単位の列：UNIT: Number
- 同じ表の列名：Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT, VALUE, FLAG

## u0193 — 見出し「$15,000 to $19,999 / 15 000 $ a 19 999 $」
- 値：5830 | 7600 | 4770 | 9080 | 10030 | 1740 | 1150 | 2430
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Tot…, Total Income / Revenu to…, Under $5,000 / Moins de …, $5,000 to $9,999 / 5 000…, $10,000 to $14,999 / 10 …, $20,000 to $24,999 / 20 …

## u0194 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory, Deliverable

## u0195 — 見出し「electorat」
- 値：1'098 | 6'248 | 10'588 | 906 | 4'304 | 1'127 | 4'696 | 6'731
- 同じ表の列名：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc, q1_valables

## u0196 — 見出し「Emp_Wkf_POPD_15+yrs_2028」
- 値：1,264,090.28500 | 946,889.18120 | 641,598.97340 | 2,852,578.43960 | 171,698.56400 | 337,276.71730 | 214,454.49020 | 45,219.51648
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2029

## u0197 — 見出し「SiteReference」
- 値：672100 | 587100 | 646600 | 667700 | 549700 | 663100 | 2045 | 1691
- 同じ表の列名：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0198 — 見出し「Estimated Maximum Annual Value」
- 値：｣170,000 | ｣102,250 | ｣158,000 | ｣17,250 | ｣52,528 | ｣20,000 | ｣10,052 | ｣39,117
- 同じ表の列名：Record UID, Contract Ref No, Directorate/ Service Res…, Start Date, End Date (Includes Ext D…, Review Date

## u0199 — 見出し「Rateable Value 2010」
- 値：15000 | 40250 | 46750 | 28000 | 4100 | 6000 | 1075 | 980
- 同じ表の列名：Property Ref, Rate Payer, Start of Liability, Empty, Empty From, Charity, Discretionary relief %, Mandatory Relief %, Small Business Rate Reli…

## u0200 — 見出し「Cost Centre」
- 値：990 | 1510 | 2110 | 990 | 1302 | 1201 | 990
- 同じ表の列名：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number, Amount in Sterling

## u0201 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：IncomeType, IncomeAmount, Expenditure Type, Expenditure Amount, Surplus Spend

## u0202 — 見出し「04:00」
- 値：113 | 207 | 52 | 137 | 194 | 112 | 103 | 165
- 同じ表の列名：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:00, 03:30

## u0203 — 見出し「6」
- 値：クイナ科 | シギ科 | サギ科 | アトリ科 | シギ科 | ウミスズメ科 | シジュウカラ科 | シジュウカラ科
- 表の題名：レッドリスト/レッドデータブック_第５次レッドリスト
- 同じ表の列名：1, 2, 3, 4, 5, 7, 8, 9, 10

## u0204 — 見出し「Koordinatenherkunft_Code」
- 値：901 | 901 | 901 | 901 | 901 | 901 | 901 | 901
- 同じ表の列名：Eidgenoessischer_Gebaeud…, Kanton, BFS_NR, Eidgenoessischer_Grundst…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenummer, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## u0205 — 見出し「Quarter」
- 値：Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14
- 同じ表の列名：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Version, Year

## u0206 — 見出し「ODA (｣m)」
- 値：11,437 1 | 11,462 | 11,462 | 11,462
- 同じ表の列名：GNI (｣m), ODA:GNI ratios (%)

## u0207 — 見出し「AGE」
- 値：Y40T44 | Y15T19 | Y30T34 | Y10T14 | Y30T34 | Y30T34 | Y55T59 | Y75T79
- 同じ表の列名：TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE

## u0208 — 見出し「Tax gap component」
- 値：PIT: reporting gap (hidden off… | PIT: gross tax gap (lower-boun… | PIT: net tax gap (upper-bound) | CIT: reporting gap (SMEs, lowe… | CIT: reporting gap (SMEs, uppe… | CIT: reporting gap (SMEs, % of… | CIT: reporting gap (large corp… | CIT: reporting gap (large corp…
- 表の題名：Overall federal tax gap report: Estimates and key findings f…
- 同じ表の列名：2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022

## u0209 — 見出し「Age」
- 値：0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64
- 同じ表の列名：Year, Week, Ending, NoDeaths_EP, Expected, LowerB, UpperB, Diff

## u0210 — 見出し「Sexual violence ('000)」
- 値：45.2 | 44.2 | 30.2 | 75.8 | 171.6
- 表の題名：Women aged 18+ years who experienced sexual violence in past…
- 同じ表の列名：All perpetrators, Total women ('000)

## u0211 — 見出し「buy_to_let_properties__fixed_rate__over_3_years__rates_on_ou」
- 値：4.54 | 4.43 | 2.3 | 2.81 | 2.78 | 2.72 | 2.59 | 2.97
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0212 — 見出し「$5,000 to $9,999 / 5 000 $ a  9 999 $」
- 値：4760 | 7370 | 4530 | 5070 | 5630 | 930 | 550 | 1120
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Tot…, Total Income / Revenu to…, Under $5,000 / Moins de …, $10,000 to $14,999 / 10 …, $15,000 to $19,999 / 15 …, $20,000 to $24,999 / 20 …

## u0213 — 見出し「jahr」
- 値：1995 | 2008 | 2007 | 2015 | 2019 | 2018 | 1991 | 2005
- 同じ表の単位の列：unit: percent_gdp
- 同じ表の列名：country_code, indicator, unit, source

## u0214 — 見出し「Value of New Contract (Excluding Options)」
- 値：4500000 | 9000000 | 2000000 | 4000000 | 2000000 | 200000000 | 5000000 | 2500000
- 同じ表の列名：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start Date, Contract Commencement Da…, New Contract End Date, Procurement Sourcing Rou…, Category

## u0215 — 見出し「Beschaffungsgegenstand」
- 値：Informatikdienstleistungen im … | Informatikdienstleistungen im … | Informatikdienstleistungen im … | Informatikdienstleistungen im … | Diverse Dienstleistungen für d… | Expertisen, Rechtsgutachten | Zivile Bauten, Bauleistungen | Fahrzeuge
- 同じ表の列名：Departement, Verwaltungseinheit (Auft…, Lieferant (Auftragnehmer…, Ort, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen inkl. Mw…

## u0216 — 見出し「Emp_Wkf_POPD_15+yrs_2029」
- 値：1,278,131.66100 | 963,977.38350 | 651,945.91510 | 2,894,054.95960 | 173,273.05480 | 341,466.13440 | 217,865.96360 | 45,579.74043
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028

## u0217 — 見出し「Ueberbauungsgrad_Mischzonen」
- 値：88.6 | 90.3 | 91.4 | 97.1 | 81.9 | 91.5 | 91 | 90.3
- 同じ表の列名：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wohnzon…, Ueberbauungsgrad_Arbeits…, Ueberbauungsgrad_Zone_Oe…, Ueberbauungsgrad_Gesamt, Einheit

## u0218 — 見出し「Contract_value」
- 値：1981030 | 419148 | 999596 | 8166850 | 998164 | 699300 | 2170500 | 1143900
- 同じ表の列名：ESF_Co-financing_Plan_re…, UPIN, UKPRN, Contract_end_date

## u0219 — 見出し「Body」
- 値：http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/…
- 同じ表の列名：Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code, Service Code, Service Label

## u0220 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory

## 答えの雛形

```
u0111			
u0112			
u0113			
u0114			
u0115			
u0116			
u0117			
u0118			
u0119			
u0120			
u0121			
u0122			
u0123			
u0124			
u0125			
u0126			
u0127			
u0128			
u0129			
u0130			
u0131			
u0132			
u0133			
u0134			
u0135			
u0136			
u0137			
u0138			
u0139			
u0140			
u0141			
u0142			
u0143			
u0144			
u0145			
u0146			
u0147			
u0148			
u0149			
u0150			
u0151			
u0152			
u0153			
u0154			
u0155			
u0156			
u0157			
u0158			
u0159			
u0160			
u0161			
u0162			
u0163			
u0164			
u0165			
u0166			
u0167			
u0168			
u0169			
u0170			
u0171			
u0172			
u0173			
u0174			
u0175			
u0176			
u0177			
u0178			
u0179			
u0180			
u0181			
u0182			
u0183			
u0184			
u0185			
u0186			
u0187			
u0188			
u0189			
u0190			
u0191			
u0192			
u0193			
u0194			
u0195			
u0196			
u0197			
u0198			
u0199			
u0200			
u0201			
u0202			
u0203			
u0204			
u0205			
u0206			
u0207			
u0208			
u0209			
u0210			
u0211			
u0212			
u0213			
u0214			
u0215			
u0216			
u0217			
u0218			
u0219			
u0220			
```
