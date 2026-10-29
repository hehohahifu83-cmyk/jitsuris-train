# 不明になった列の調査 001 / 003（1 列ずつ）

公開データの表の列です。今の仕組みはこれらの列に種類を付けられず「不明」と答えました。人が見て決められるか、決められるなら何が決め手かを知りたい調査です。

- **1 列ずつ**、LABEL_GUIDE.md（v2.1）のどの種類かを答える。決められなければ `unknown`。
- **決め手**を次から 1 つ（いちばん効いたもの）：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない
- メモは短く（なぜそう決めたか、何があれば決められたか）。日本語で。
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を写し、ChatGPT は `research/unknown/answers_chatgpt/sheet_NNN.tsv`、Grok は `research/unknown/answers_grok/sheet_NNN.tsv` に置く。1 行＝「u0001<TAB>ラベル<TAB>決め手<TAB>メモ」
- **見ないもの**：`research/unknown/columns.jsonl`・`sheet_index.json`（正解と今の仕組みの答えが入っている）、もう一人の先生の答え、モデルの予測

## u0001 — 見出し「Datierung_von」
- 値：1812 | 1829 | 1746 | 1746 | 1684 | 1684 | 1684 | 1740
- 同じ表の列名：ID, Signatur, KünstlerIn, Titel, Inhalt_Kurzbeschreibung, Titelvariante, Datierung_bis, Serientitel, Farbe

## u0002 — 見出し「Stimmbeteiligung」
- 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0
- 同じ表の列名：Titel, Datum, Verwaltungsebene, Typ, Status, Total der Gemeinden, Ausgezählte Gemeinden, Letzte Änderung

## u0003 — 見出し「value」
- 値：92 | 109 | 91 | 73 | 74 | 73 | 74 | 96
- 同じ表の列名：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type

## u0004 — 見出し「SCS on standard contracts」
- 値：Annual SCS Paybill for those S… | ｣18,099,035 | ｣16,469,061
- 同じ表の列名：Main  department, Organisation, Delegated grades, Information for SCS on n…, Comments

## u0005 — 見出し「Satisfied」
- 値：35.3 | 33.3 | 33.6 | 46 | 43 | 28.6 | 30.28 | 10
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wante…, Got some of what I wante…, Got none of what I wante…, Very Satisfied, Neither satisfied nor di…

## u0006 — 見出し「crime」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：issued, administration, agriculture, construction, culture, education, energy, finances, geography

## u0007 — 見出し「buy_to_let_properties__floating_rate__tracker_mortgages__rat」
- 値：1.09 | 1.09 | 1.06 | 1.06 | 1.06 | 1.09 | 1.05 | 1.05
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0008 — 見出し「Gcons2006」
- 値：14300 | 22500 | 3000 | 500 | 16000 | 8400 | 14700 | 21000
- 同じ表の列名：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006Valid, Gcons2007, Gcons2007Valid

## u0009 — 見出し「Emp_Wkf_POPD_15+yrs_2027」
- 値：1,249,173.48000 | 927,782.30500 | 629,413.12760 | 2,806,368.91260 | 169,894.80070 | 332,610.99360 | 210,939.51460 | 44,870.87752
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0010 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, PreviouslyPartOf, SitePlanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable

## u0011 — 見出し「SCS on standard contracts」
- 値：Annual SCS Paybill for those S… | ｣18,322,781
- 同じ表の列名：Main  department, Organisation, Delegated grades, Information for SCS on n…, Comments

## u0012 — 見出し「reporting_period」
- 値：P02 | P01 | P01 | P02 | P01 | P02 | P01 | P02
- 表の題名：Proactive Disclosure - Question Period notes
- 同じ表の列名：year

## u0013 — 見出し「anzahl」
- 値：137713 | 138727 | 146186 | 138062 | 138545 | 144157 | 145044 | 150742
- 同じ表の列名：jahr, szenario

## u0014 — 見出し「Procurement Start Date」
- 値：45714 | 46023 | 45361 | 45166 | 44959 | 44943 | 45016 | 45019
- 同じ表の列名：Reference Number, Business Area, Contract Title, Commercial Strategy, Contract Commencement Da…, New Contract End Date, Value of New Contract (E…, Procurement Sourcing Rou…, Category

## u0015 — 見出し「digital_platform」
- 値：e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch
- 同じ表の列名：library_call_number, digital_reproduction, title, place_of_publication_or_…, date_of_publication_or_p…, date_of_publication_or_p…, series, digital_reproduction_cop…, digital_object_identifie…

## u0016 — 見出し「Beschluss」
- 値：11300 | 2200 | 66200 | NA | 600 | 6800 | 10400 | 6500
- 同じ表の列名：Kategorie, Sparte, Nachgefragt, Status, Eingangsdatum, Beschlussdatum, ID

## u0017 — 見出し「VALUE」
- 値：. | . | . | . | . | . | . | .
- 表の題名：JQ06 – Stock of nurses by country of first qualification
- 同じ表の単位の列：UNIT: Number
- 同じ表の列名：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT, FLAG

## u0018 — 見出し「organisati」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：FID, id_0, id, organisa_1, siterefere, site_id_2, siteplanur, geox, geoy

## u0019 — 見出し「Total」
- 値：｣531.36 | ｣531.36 | ｣717.70 | ｣527.68 | ｣531.36 | ｣999.00 | ｣594.00 | ｣1,476.00
- 同じ表の列名：Transaction Reference, Transaction Date, Merchant

## u0020 — 見出し「Delegated grades」
- 値：Annual Paybill  (delegated gra… | ｣1,053,041,472 | ｣208,453,917 | ｣89,399,301 | ｣38,302,816 | ｣15,558,951 | ｣468,236,981
- 同じ表の列名：Main  department, Organisation, SCS on standard contract…, Information for SCS on n…, Comments

## u0021 — 見出し「bathPosition」
- 値：4 | 9 | NA | 16 | 18 | NA | NA | NA
- 表の題名：Reducing pest risk in birch wood products - The effective he…
- 同じ表の列名：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, vialPosition, replicate

## u0022 — 見出し「Anzahl von fact_kurs_hist_sid」
- 値：5 | 144 | 256 | 4 | 77 | 7 | 68 | 68
- 同じ表の列名：Jahr

## u0023 — 見出し「Annual Paybill (delegated grades for financial year 2012/13)」
- 値：｣148,884,966 | ｣152,259,751 | ｣83,720,000 | ｣65,040,000 | ｣46,946,741 | ｣69,299,856 | ｣29,670,856 | ｣38,292,164
- 同じ表の列名：Main Department, Organisation, Headcount (delegated gra…, Cost of in-year NCPRP fo…, Number of staff in deleg…, In-Year - Number of staf…, In-Year - Median NCPRP f…, End of Year - Cost of en…, End of Year - Number of …

## u0024 — 見出し「wasserkraft_kwh」
- 値：7273783000.0 | 10185136000.0 | 7575000000.0 | 5062431000.0 | 7829000000.0 | 8204000000.0 | 8039000000.0 | 7402000000.0
- 同じ表の列名：jahr, biomasse_kwh, wind_kwh, abfall_kwh, trinkwasserkraftwerk_kwh, klein_wasserkraftwerk_kw…, photovoltaik_kwh

## u0025 — 見出し「FISCAL_YEAR」
- 値：2012_2013 | 2012_2013 | 2012_2013 | 2013_2014 | 2013_2014 | 2013_2014 | 2014_2015 | 2014_2015
- 表の題名：Employment Equity Designated Groups under the Public Service…
- 同じ表の列名：emp_equity_designated_gr…, emp_equity_designated_gr…

## u0026 — 見出し「modell_lauf」
- 値：2026_03 | 2026_03 | 2026_03 | 2026_03 | 2026_03 | 2026_03 | 2026_03 | 2026_03
- 同じ表の列名：indikator, einheit, region, branche, jahr, wert

## u0027 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0028 — 見出し「Arrest/Detention > Drugs」
- 値：<5 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Child…, Arrest/Detention > Fraud, Arrest/Detention > Immig…, Arrest/Detention > Moder…, Arrest/Detention > Murde…

## u0029 — 見出し「lastgang_kwh」
- 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.093 | 0.0
- 同じ表の列名：zeitpunkt

## u0030 — 見出し「Cost of in-year NCPRP for delegated grades (｣s)」
- 値：｣373,947 | ｣570,048 | ｣652,611 | ｣38,650 | ｣11,300 | ｣2,250 | ｣2,140 | ｣0
- 同じ表の列名：Main department, Organisation, Annual Paybill (delegate…, Headcount (delegated gra…, Number of staff in deleg…, Number of staff in deleg…, Median NCPRP for those r…, Cost of end of year NCPR…, Number of staff in deleg…

## u0031 — 見出し「Mandatory Relief %」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relief %, Small Business Rate Reli…

## u0032 — 見出し「pop」
- 値：8275032 | 8522244 | 8582905 | 8855062 | NA | NA | NA | NA
- 同じ表の列名：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## u0033 — 見出し「pubdate_from」
- 値：1645 | 1645 | 1645 | 1645 | 1645 | 1645 | 1645 | 1645
- 同じ表の列名：catalog_id_swisscovery, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_to, creator, publisher, reference

## u0034 — 見出し「plz」
- 値：8910 | 8910 | 8910 | 8451 | 8460 | 8192 | 8152 | 8152
- 同じ表の列名：jahr, bezirk_nr, bezirk, id, ort, leistungsauftrag, leistungsauftrag_gmde, indikator, wert

## u0035 — 見出し「Paid_fare」
- 値：273.5 | 276.63 | 231.6 | 263.2 | 190.6 | 332.43 | 107.35 | 3074.37
- 同じ表の列名：Agency, Trip type, Routing_type, Ticket class, Departure Date, Origin, Destination, Destination Country, Carrier

## u0036 — 見出し「Arrest/Detention > Fraud」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Child…, Arrest/Detention > Drugs, Arrest/Detention > Immig…, Arrest/Detention > Moder…, Arrest/Detention > Murde…

## u0037 — 見出し「LowerB」
- 値：147 | 147 | 145 | 139 | 140 | 139 | 143 | 133
- 同じ表の列名：Year, Week, Ending, Age, NoDeaths_EP, Expected, UpperB, Diff

## u0038 — 見出し「Discretionary relief %」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Mandatory Relief %, Small Business Rate Reli…

## u0039 — 見出し「Biomass」
- 値：131582800 | 123151500 | 143881300 | 154014800 | 160529000 | 179414000 | 183334800 | 173978700
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Fossil fuels, Metal ores, Non-metallic minerals, Total (All categories)

## u0040 — 見出し「Salary Cost of Reports (｣)」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の単位の列：Unit: GO London, GO North West, GO Yorkshire and Humber
- 同じ表の列名：Post Unique Reference, Grade, Job Title, Job/Team Function, Parent Department, Organisation, Unit, Reports to Senior Post, FTE

## u0041 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：ExtractDate, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, MonthPaid, ExpenseType, Amount

## u0042 — 見出し「sensor」
- 値：531 | 531 | 531 | 531 | 531 | 531 | 531 | 531
- 同じ表の列名：starttime, site, masl, magl, x, y, temperature, humidity

## u0043 — 見出し「Versicherer」
- 値：57 | 62 | 134 | 246 | 343 | 360 | 376 | 455
- 同じ表の列名：Kanton, Geschaftsjahr, Durchschnittsbestand

## u0044 — 見出し「electorat」
- 値：720 | 616 | 948 | 1'085 | 709 | 888 | 1'033 | 4'393
- 同じ表の列名：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc, q1_valables

## u0045 — 見出し「replicate」
- 値：13 | 20 | 5 | 16 | 23 | 1 | 13 | 16
- 表の題名：Reducing pest risk in birch wood products - The effective he…
- 同じ表の列名：treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition

## u0046 — 見出し「funk」
- 値：29 | 35 | 5 | 68 | 92
- 同じ表の列名：arten, d, f, i, e, model

## u0047 — 見出し「Grand Total  (workforce numbers)」
- 値：Headcount | 400 | 127 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsor…, Payroll staff, Number of non-payroll st…, Payroll staff costs, Non-Payroll staff (conti…, Grand Total paybill/staf…, Notes for Cabinet Office…

## u0048 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：ExtractDate, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeURI, EntertainmentTypeLabel, LateNightRefreshment

## u0049 — 見出し「Type of Post」
- 値：British Embassy | British Embassy | British Embassy | British Trade Office | UK Government Office (DIT) | British High Commission | British High Commission | British Embassy
- 同じ表の列名：Region, Country/Territory, Location (City), y, x

## u0050 — 見出し「trinkwasserkraftwerk_kwh」
- 値：34722365.0 | 38647313.0 | 33282153.0 | 30345196.0 | 34971069.0 | 37410192.0 | 31614931.0 | 23889811.0
- 同じ表の列名：jahr, biomasse_kwh, wind_kwh, abfall_kwh, klein_wasserkraftwerk_kw…, photovoltaik_kwh, wasserkraft_kwh

## u0051 — 見出し「Service_FR」
- 値：Téléphonie - Fixe et Mobile | Accès à distance protégé | Téléphonie - Fixe et Mobile | Téléphonie - Fixe et Mobile | Téléphonie - Fixe et Mobile | Gestion des justificatifs inte… | Téléphonie - Fixe et Mobile | Conférence
- 表の題名：Enterprise Service Model Consumption Actuals
- 同じ表の列名：Department_EN, Department_FR, Service_EN, Value, Date_Captured

## u0052 — 見出し「Durchschnittsbestand」
- 値：207.58 | 5.25 | 23.56 | 967.14 | 3141.476491 | 10.23 | 17072.27778 | 389.0200001
- 同じ表の列名：Versicherer, Kanton, Geschaftsjahr

## u0053 — 見出し「principal_dwelling_houses__floating_rate__tracker_mortgages_」
- 値：1.03 | 1.05 | 1.03 | 1.03 | 1.03 | 1.04 | 1.04 | 1.04
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0054 — 見出し「transect_code」
- 値：B1 | A4 | C0 | B2 | B3 | A1 | A3 | A2
- 同じ表の列名：site, x_lv95, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, wd_max_ufp, datetime_installed

## u0055 — 見出し「Neither satisfied nor dissatisfied」
- 値：10.6 | 16.7 | 21.3 | 32 | 15 | 14.3 | 14.68 | 6
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wante…, Got some of what I wante…, Got none of what I wante…, Very Satisfied, Satisfied

## u0056 — 見出し「lastgang_kwh」
- 値：3.171 | 690.0 | 1043.088 | 157.353 | 0.0 | 0.0 | 0.0 | 155.904
- 同じ表の列名：zeitpunkt, energietraeger

## u0057 — 見出し「buy_to_let_properties__floating_rate__standard_or_ltv_variab」
- 値：4.53 | 4.52 | 4.24 | 4.2 | 4.2 | 4.38 | 4.15 | 4.03
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0058 — 見出し「OrganisationURL」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory

## u0059 — 見出し「Variable」
- 値：farms_examined_count | farms_examined_positive_count | farms_total_count | farms_to_examine_count | farms_examined_positive_count | farms_examined_negative_count | farms_total_count | farms_to_examine_count
- 同じ表の列名：YearWeekIso, LastDayOfWeek, Number

## u0060 — 見出し「Class ID」
- 値：44,445.00 | 44,950.00 | 44,699.00 | 44,871.00 | 46,011.00 | 45,062.00 | 45,080.00 | 46,189.00
- 表の題名：New Established Special Classes Opening for 2026-2027 School…
- 同じ表の列名：County, SRN, School Year, School Type, Class Type

## u0061 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：EffectiveDate, PaymentDate, Directorate/ServiceWhere…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount, IrrecoverableVAT, ProcurementClassificatio…

## u0062 — 見出し「UK Treaty Actions November 2015 - February 2016」
- 値：Algeria – Double Taxation Conv… | South Africa – Exchange of Not… | Canada – Exchange of Notes con… | Uruguay – Double Taxation Conv… | China – Treaty on Mutual Legal… | Kazakhstan – Treaty on Mutual … | Belgium - Exchange of Letters … | Bulgaria – Double Taxation Con…
- 同じ表の列名：Region

## u0063 — 見出し「C02199V02655」
- 値：- | - | 1 | 2 | 1 | - | 2 | 1
- 表の題名：EDA36 - Percentage of persons aged 20-24 years having Comple…
- 同じ表の単位の列：UNIT: %
- 同じ表の列名：STATISTIC, Statistic, TLIST(A1), Year, Sex, UNIT, VALUE

## u0064 — 見出し「Invoiced」
- 値：｣2,113.05 | ｣3,000.00 | ｣3,901.51 | ｣725.00 | ｣810.00 | ｣845.00 | ｣7,969.50 | ｣1,336.50
- 同じ表の列名：Invoice Date, Proclass Category, Service Area

## u0065 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：SiteReference, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory

## u0066 — 見出し「Datierung_Bemerkung」
- 値：Poststempel | Entzifferung unsicher | Orig.: 8 Octobre nouveau style… | 9. Juni (?) | Dat. Karte (Br. undat.) | Entzifferung unsicher | Entzifferung unsicher | Orig.: 29. Brumaire an IV
- 同じ表の列名：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Illustration, Widmung

## u0067 — 見出し「Grand Total  (workforce numbers)」
- 値：Headcount | 1,246 | 115 | 43 | 17 | 0 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsor…, Payroll staff, Number of non-payroll st…, Payroll staff costs, Non-Payroll staff (conti…, Grand Total paybill/staf…, Notes for Cabinet Office…

## u0068 — 見出し「01:30」
- 値：97 | 96 | 52 | 92 | 93 | 95 | 96 | 97
- 同じ表の列名：DATE, 00:00, 00:30, 01:00, 02:00, 02:30, 03:00, 03:30, 04:00

## u0069 — 見出し「wert」
- 値：12931 | 44 | 31 | 7 | 17 | 7 | 14578 | 32
- 同じ表の列名：jahr, bildungsabschluss, metrik, einheit

## u0070 — 見出し「Total」
- 値：1,062.00 | 964.93 | 919.62 | 800.40 | 793.08 | 774.57 | 755.32 | 751.34
- 同じ表の列名：Transaction Date

## u0071 — 見出し「Version」
- 値：RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG
- 同じ表の列名：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Year, Quarter

## u0072 — 見出し「Ueberbauungsgrad_Arbeitszonen」
- 値：100 | 96.2 | 95.3 | 96.4 | 90 | 95.4 | 61.5 | 74.8
- 同じ表の列名：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wohnzon…, Ueberbauungsgrad_Mischzo…, Ueberbauungsgrad_Zone_Oe…, Ueberbauungsgrad_Gesamt, Einheit

## u0073 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, UPRN, AssetCode, PostTown, GEOX, GEOY, TenureType, TenureDetail, HoldingType

## u0074 — 見出し「spur_code」
- 値：1 | 1 | 1 | 1 | 1 | 1 | 1 | 1
- 同じ表の列名：code, gemeinde, richtung, reg_bus, datum, zeit_von, zeit_bis, jahr, monat

## u0075 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, EffectiveDate, ExpenditureType, ExpenditureAmount, SurplusAmount, ParkingSpacesNumber, FreeParkingSpacesNumber, Charged-forParkingSpaces…

## u0076 — 見出し「Cost Centre」
- 値：E7036 | L3951 | S6131 | B8450 | S6141 | S6141 | S6141 | S6141
- 同じ表の列名：Transaction Number, Paid Date, Paid Amount, Department, Irrecoverable VAT

## u0077 — 見出し「Cost Centre」
- 値：2553 | 2540 | 3805 | 7500 | 1322 | 2554 | 3304 | 7500
- 同じ表の列名：Organisation, Service Area, Expense Type, Payment Date, Transaction No., Amount, Capital Revenue, Supplier ID

## u0078 — 見出し「TIME_PERIOD」
- 値：2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01
- 同じ表の列名：GEO, AGE, SEX, OBS_STATUS, OBS_VALUE

## u0079 — 見出し「Total (All categories)」
- 値：688618500 | 648585000 | 693829900 | 718423000 | 739419600 | 785531700 | 787917600 | 759645500
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Biomass, Fossil fuels, Metal ores, Non-metallic minerals

## u0080 — 見出し「AGE」
- 値：Y75T79 | _T | Y85T89 | Y5T9 | Y45T49 | Y20T24 | Y45T49 | _T
- 同じ表の列名：TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE

## u0081 — 見出し「energy」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：issued, administration, agriculture, construction, crime, culture, education, finances, geography

## u0082 — 見出し「TOTAL_SHEEP_MOUNTAIN」
- 値：13028 | 10984 | 1316 | 59191 | 196521 | 6312 | 105879 | 183200
- 表の題名：DAFM National Sheep Census 2020
- 同じ表の列名：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_IND, FLOCKS_WITH_TOTAL_SHEEP_…, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_CALC

## u0083 — 見出し「Emp_Wkf_POPD_15+yrs_2024」
- 値：1,230,867.76500 | 884,670.85480 | 600,290.44310 | 2,715,829.06290 | 165,808.21300 | 328,091.61860 | 205,357.00860 | 44,707.77680
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0084 — 見出し「Cost Centre」
- 値：A7000 | L4974 | E9061 | L3950 | E5630 | T4020 | E9061 | L2430
- 同じ表の列名：Transaction Number, Paid Date, Paid Amount, Department, Irrecoverable VAT, Merchant Category

## u0085 — 見出し「ServiceTypeURI」
- 値：http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8… | http://id.esd.org.uk/service/8…
- 同じ表の列名：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeLabel, EntertainmentTypeURI, EntertainmentTypeLabel, LateNightRefreshment

## u0086 — 見出し「OrganisationURI」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：OrganisationLabel, SiteReference, SiteplanURL, CoordinateReferenceSyste…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus

## u0087 — 見出し「Arrest/Detention > Child Pornography」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assau…, Arrest/Detention > Assau…, Arrest/Detention > Child…, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immig…, Arrest/Detention > Moder…, Arrest/Detention > Murde…

## u0088 — 見出し「Value (L)」
- 値：9250 | 8683 | 25497 | 14900 | 14900
- 同じ表の列名：Reference Number (B), Title of Agreement (C ), Dept (D), Service Label (E ), Start Date (H), End Date (I), Quantity (J), Price (K), Tender Process (N)

## u0089 — 見出し「laufnummer」
- 値：2026/5602 | 2026/5510 | 2026/5117 | 2026/5036 | 2026/4653 | 2026/3371 | 2026/3364 | 2025/529
- 同じ表の列名：titel, status, komission, federfuehrende_direktion, beginn, ende, stand_lr, ueberweisungsdatum, geschaeftstyp

## u0090 — 見出し「RANK OF IMD SCORE (where 1 is most deprived)」
- 値：9045 | 11857 | 6148 | 16321 | 11576 | 22842 | 19057 | 9485
- 同じ表の列名：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, INCOME SCORE, RANK OF INCOME SCORE (wh…, EMPLOYMENT SCORE, RANK OF EMPLOYMENT SCORE…

## u0091 — 見出し「Emp_Wkf_POPD_15+yrs_2026」
- 値：1,235,608.02200 | 908,883.28090 | 617,945.99980 | 2,762,437.30270 | 168,306.25900 | 328,030.50980 | 207,870.90790 | 44,528.80621
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0092 — 見出し「BFS_NR」
- 値：115 | 96 | 112 | 102 | 112 | 112 | 96 | 111
- 同じ表の列名：Eidgenoessischer_Gebaeud…, Kanton, Eidgenoessischer_Grundst…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenummer, E-Gebaeudekoordinate, N-Gebaeudekoordinate, Koordinatenherkunft_Code

## u0093 — 見出し「Auftragsvolumen inkl. MwSt in CHF」
- 値：427440.64 | 85000 | 53311.5 | 51696 | 510850.7 | 101969.28 | 96073.36 | 93100
- 同じ表の列名：Departement, Verwaltungseinheit (Auft…, Lieferant (Auftragnehmer…, Ort, Beschaffungsgegenstand, Vergabeverfahren, Vertragsbeginn, Vertragsende

## u0094 — 見出し「OrganisationCode」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：EffectiveDate, FinancialYear, Department, Payee, Language, Amount

## u0095 — 見出し「principal_dwelling_houses__floating_rate__standard_or_ltv_va」
- 値：4.19 | 4.26 | 3.82 | 3.77 | 3.76 | 3.78 | 3.75 | 3.66
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, buy_to_let_properties__f…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…, principal_dwelling_house…

## u0096 — 見出し「Total_Value」
- 値：｣6,316.50 | ｣9,750.00 | ｣6,399.01 | ｣313,889.44 | ｣6,380.00 | ｣23,250.00 | ｣5,595.00 | ｣6,975.00
- 同じ表の列名：Purchase Order Number, Order date, Service

## u0097 — 見出し「Fossil fuels」
- 値：155975600 | 153398500 | 150781700 | 152557700 | 161329100 | 175027300 | 166924500 | 163439700
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Biomass, Metal ores, Non-metallic minerals, Total (All categories)

## u0098 — 見出し「monat」
- 値：10 | 10 | 10 | 10 | 10 | 10 | 10 | 10
- 同じ表の列名：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## u0099 — 見出し「$20,000 to $24,999 / 20 000 $ a 24 999 $」
- 値：9200 | 10560 | 6130 | 12280 | 14290 | 2530 | 1670 | 3010
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Tot…, Total Income / Revenu to…, Under $5,000 / Moins de …, $5,000 to $9,999 / 5 000…, $10,000 to $14,999 / 10 …, $15,000 to $19,999 / 15 …

## u0100 — 見出し「9」
- 値：③ | D | D | B2ab | A2 | C2b | B2ab | B2ab
- 表の題名：レッドリスト/レッドデータブック_第５次レッドリスト
- 同じ表の列名：1, 2, 3, 4, 5, 6, 7, 8, 10

## u0101 — 見出し「designation」
- 値：Bissone (lago) | Informationsschalter | Stazione Lugano FLP | Guichet d'information | Capolago SNL | Billettschalter | Guichet des billets | Billettschalter
- 同じ表の列名：sloid, parentSloidServicePoint, parentNumberServicePoint, type, inductionLoop, wheelchairAccess, validFrom, validTo, creationDate

## u0102 — 見出し「Surplus Amount」
- 値：103268
- 同じ表の列名：Organisation Code, Expenditure Type, Expenditure Amount

## u0103 — 見出し「EW_Compulsory_SA」
- 値：[x] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA

## u0104 — 見出し「plan」
- 値：Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado…
- 同じ表の列名：FID, id, code, location

## u0105 — 見出し「date_of_publication_or_production_standardised」
- 値：1780 | 1781 | 1782 | 1783 | 1784 | 1785 | 1787 | 1788
- 同じ表の列名：library_call_number, digital_reproduction, title, place_of_publication_or_…, date_of_publication_or_p…, series, digital_reproduction_cop…, digital_object_identifie…, digital_platform

## u0106 — 見出し「Got some of what I wanted」
- 値：14.1 | 26.7 | 37.7 | 45 | 26 | 25.9 | 24.85 | 18
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wante…, Got none of what I wante…, Very Satisfied, Satisfied, Neither satisfied nor di…

## u0107 — 見出し「DiffMedianBonusPercent」
- 値：0.00 | 34.00 | 0.00 | 0.00 | 31.80 | 12.50 | -5.70 | 20.40
- 同じ表の列名：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile

## u0108 — 見出し「Emp_Wkf_POPD_15+yrs_2022」
- 値：1,181,105.90700 | 776,608.72070 | 542,331.13300 | 2,500,045.76070 | 154,303.68380 | 300,092.53510 | 197,583.65530 | 42,883.56708
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029

## u0109 — 見出し「kumsum」
- 値：2002 | 3941 | 3941 | 5731 | 2076 | 4071 | 5883 | 2053
- 同じ表の列名：jahr, quartal, branchen, n, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## u0110 — 見出し「GNI (｣m)」
- 値：1,593,448 | 28,718 | 1,622,166 | 45,595 | 1,667,761 | 32,409 | 1,700,170
- 同じ表の列名：ODA (｣m), ODA:GNI ratios (%)

## 答えの雛形

```
u0001			
u0002			
u0003			
u0004			
u0005			
u0006			
u0007			
u0008			
u0009			
u0010			
u0011			
u0012			
u0013			
u0014			
u0015			
u0016			
u0017			
u0018			
u0019			
u0020			
u0021			
u0022			
u0023			
u0024			
u0025			
u0026			
u0027			
u0028			
u0029			
u0030			
u0031			
u0032			
u0033			
u0034			
u0035			
u0036			
u0037			
u0038			
u0039			
u0040			
u0041			
u0042			
u0043			
u0044			
u0045			
u0046			
u0047			
u0048			
u0049			
u0050			
u0051			
u0052			
u0053			
u0054			
u0055			
u0056			
u0057			
u0058			
u0059			
u0060			
u0061			
u0062			
u0063			
u0064			
u0065			
u0066			
u0067			
u0068			
u0069			
u0070			
u0071			
u0072			
u0073			
u0074			
u0075			
u0076			
u0077			
u0078			
u0079			
u0080			
u0081			
u0082			
u0083			
u0084			
u0085			
u0086			
u0087			
u0088			
u0089			
u0090			
u0091			
u0092			
u0093			
u0094			
u0095			
u0096			
u0097			
u0098			
u0099			
u0100			
u0101			
u0102			
u0103			
u0104			
u0105			
u0106			
u0107			
u0108			
u0109			
u0110			
```
