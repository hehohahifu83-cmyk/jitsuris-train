# 判断の説明 002 / 006（1 列ずつ、くわしく）

今の仕組みが「不明」と答えたか、種類を取り違えた列です。人がどう考えて種類を決めるかを、決め方の規則（C3 の判断のルール）に移したいので、**考えた順にくわしく**書いてください。

- この枚の列には、**前回の調査でのあなたの答え**を付けてあります（正しいとも誤りとも限りません）。前回なぜそう判断したかを、今の目で説明してください。考え直して変えるなら「前回の答えを変えるか」に書く
- LABEL_GUIDE.md（v2.1）の判定の順番（①列名・単位 → ②表の題名 → ③同じ表の列 → ④値の形）で、それぞれから**何が読めたか・読めなかったか**を書く。読めなければ「なし」
- 「迷った種類」には、候補に上がった別の種類と、それを退けた理由を書く（例：「amount も考えたが、通貨の記号も単位の列もなく、値が整数の小さい数なので quantity」）
- 「規則にするなら」は、ほかの表にも当てはまる言い方で 1〜2 文。当てはまらない例（その規則で誤りそうな列）も書く。規則にできないなら「できない（理由）」
- 決め手は次から 1 つ：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない。使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- **見ないもの**：`research/unknown/columns.jsonl`・`misses.jsonl`・`sheet_index.json`・`explain/index.json`・`compare*`・`candidates*`・`findings.md`（正解と今の仕組みの答えが入っている）、Grok の答え、モデルの予測
- 答え：末尾の雛形を写して埋め、`research/unknown/explain/answers_chatgpt/explain_002.md` に置く。見出し（`## x0001` など）と各行の頭（`- 種類：` など）は変えない

## e0001 — 見出し「Tree」
- 値：2519, 3508 | 842 | 553 | 2664, 174
- 表の題名：Ballarat Historical Naming Index
- 同じ表の列名：Type, Site, Locality, Ward, Authority, See Entry, Not in use, Unknown / uncertain, Beyond Maps
- **前回のあなたの答え**：id（決め手：表の題名）メモ「歴史的名称索引の Tree 欄に並ぶ参照番号。」

## e0002 — 見出し「TIME_PERIOD」
- 値：2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01
- 同じ表の列名：GEO, AGE, SEX, OBS_STATUS, OBS_VALUE
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「TIME_PERIOD は週を示す時間軸。」

## e0003 — 見出し「Rateable Value 2010」
- 値：15000 | 40250 | 46750 | 28000 | 4100 | 6000 | 1075 | 980
- 同じ表の列名：Property Ref, Rate Payer, Start of Liability, Empty, Empty From, Charity, Discretionary relief %, Mandatory Relief %, Small Business Rate Relief
- **前回のあなたの答え**：amount（決め手：見出しの語）メモ「Rateable Value は課税評価額。」

## e0004 — 見出し「monitoring_program」
- 値：BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI
- 同じ表の単位の列：unit: CFU/100ml
- 同じ表の列名：station_number, latidude, date_of_probing, parameter_type, value, lower_LOD, unit
- **前回のあなたの答え**：id（決め手：値の形）メモ「BAQUA_TI はモニタリング事業の識別コード。」

## e0005 — 見出し「EW_Total_Company_SA」
- 値：[x] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA
- **前回のあなたの答え**：category（決め手：値の形）メモ「[x] は季節調整系列の該当フラグ。」

## e0006 — 見出し「Beschluss」
- 値：11300 | 2200 | 66200 | NA | 600 | 6800 | 10400 | 6500
- 同じ表の列名：Kategorie, Sparte, Nachgefragt, Status, Eingangsdatum, Beschlussdatum, ID
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Beschluss と数値だけでは決定額か識別番号か特定できない。」

## e0007 — 見出し「Body」
- 値：http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/…
- 同じ表の列名：Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code, Service Code, Service Label
- **前回のあなたの答え**：id（決め手：値の形）メモ「Body の値は機関を指す統計 URI。」

## e0008 — 見出し「OrganisationCode」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：Date Approved, Service, Portfolio, Type, Review Date, Current?, Link
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「OrganisationCode の値は組織リソース URI。」

## e0009 — 見出し「Arrest/Detention > Assault」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「逮捕・拘留の暴行関連件数。」

## e0010 — 見出し「SiteReference」
- 値：672100 | 587100 | 646600 | 667700 | 549700 | 663100 | 2045 | 1691
- 同じ表の列名：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReferenceSystem, GeoX, GeoY, Hectares, Deliverable, PlanningStatus
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「SiteReference は地点を参照する識別番号。」

## e0011 — 見出し「value」
- 値：92 | 109 | 91 | 73 | 74 | 73 | 74 | 96
- 同じ表の列名：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「value だけでは単位も測定対象も分からない。」

## e0012 — 見出し「Type of Aid」
- 値：C01 | C01 | C01 | C01 | C01 | D02 | C01 | C01
- 同じ表の列名：Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country Code, Input Sector code, Channel of Delivery Code, Type of Flow, Type of Finance
- **前回のあなたの答え**：id（決め手：値の形）メモ「C01・D02 は援助種別の分類コード。」

## e0013 — 見出し「EW_CVL_SA」
- 値：[x] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA
- **前回のあなたの答え**：category（決め手：値の形）メモ「[x] は季節調整系列の該当フラグ。」

## e0014 — 見出し「Grand Total  (workforce numbers)」
- 値：Headcount | 400 | 127 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsoring de…, Payroll staff, Number of non-payroll staff (c…, Payroll staff costs, Non-Payroll staff (contingent …, Grand Total paybill/staffing (…, Notes for Cabinet Office (Not …
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「Grand Total の workforce numbers は職員数。」

## e0015 — 見出し「Lim_min」
- 値：151 | 1023 | 879 | 1038 | 885 | 129 | 1101 | 1119
- 同じ表の列名：AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_sup, Exces
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「死亡数の予測に対する下限値で、死亡件数の尺度。」

## e0016 — 見出し「SMR 2024」
- 値：1.0 | 0.0 | 1.0 | * | * | 0.0 | 2.3 | 2.2
- 同じ表の列名：institution, indicator, taux observe 2019-2023, taux attendu 2019-2023, SMR 2019-2023, nombre de cas 2019-2023, taux observe 2024, taux attendu 2024, nombre de cas 2024
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「SMR は観測死亡数と期待死亡数の比率。」

## e0017 — 見出し「PaymentDate」
- 値：14/08/2014 | 19/08/2014 | 08/09/2014 | 18/09/2014 | 02/10/2014 | 02/10/2014 | 08/10/2014 | 15/10/2014
- 同じ表の列名：OrganisationURI, EffectiveDate, Directorate/ServiceWhereExpend…, ServiceCategoryLabel, ServiceCategoryURI, Supplier, NetAmount, IrrecoverableVAT, ProcurementClassification:Proc…
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「PaymentDate は支払日。」

## e0018 — 見出し「Cost Centre」
- 値：2553 | 2540 | 3805 | 7500 | 1322 | 2554 | 3304 | 7500
- 同じ表の列名：Organisation, Service Area, Expense Type, Payment Date, Transaction No., Amount, Capital Revenue, Supplier ID
- **前回のあなたの答え**：id（決め手：値の形）メモ「Cost Centre の数値コードはコストセンター識別子。」

## e0019 — 見出し「UK Treaty Actions November 2015 - February 2016」
- 値：Algeria – Double Taxation Conv… | South Africa – Exchange of Not… | Canada – Exchange of Notes con… | Uruguay – Double Taxation Conv… | China – Treaty on Mutual Legal… | Kazakhstan – Treaty on Mutual … | Belgium - Exchange of Letters … | Bulgaria – Double Taxation Con…
- 同じ表の列名：Region
- **前回のあなたの答え**：text（決め手：値の形）メモ「各値は条約・協定の個別の長い名称。」

## e0020 — 見出し「max_time_generation」
- 値：0 | 0.801 | 0 | 0 | 1.652 | 0 | 0 | 0.548
- 同じ表の列名：label, nb_visits, nb_hits, nb_hits_with_time_generation, min_time_generation, sum_time_spent, bounce_count, exit_nb_visits, sum_daily_nb_uniq_visitors
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「max_time_generation は処理時間の長さ。」

## e0021 — 見出し「$15,000 to $19,999 / 15 000 $ a 19 999 $」
- 値：5830 | 7600 | 4770 | 9080 | 10030 | 1740 | 1150 | 2430
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $10,000 to $14,999 / 10 000 $ …, $20,000 to $24,999 / 20 000 $ …
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Individual Tax Statistics の所得階級別申告件数。」

## e0022 — 見出し「Procurement Start Date」
- 値：45714 | 46023 | 45361 | 45166 | 44959 | 44943 | 45016 | 45019
- 同じ表の列名：Reference Number, Business Area, Contract Title, Commercial Strategy, Contract Commencement Date, New Contract End Date, Value of New Contract (Excludi…, Procurement Sourcing Route, Category
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「Procurement Start Date は契約開始日。」

## e0023 — 見出し「Rank」
- 値：109 | 143 | 168 | 291 | 315 | 338 | 352 | 372
- 表の題名：Grade Crossings Inventory 
- 同じ表の列名：TC Number, Railway Company, Region, Province, Access, Jurisdiction, Mile, Subdivision, Spur Mile Point
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「Rank は踏切インベントリの順位。」

## e0024 — 見出し「Quarter」
- 値：Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14 | Qtr1 - 13-14
- 同じ表の列名：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Version, Year
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「Quarter は会計年度の四半期。」

## e0025 — 見出し「$5,000 to $9,999 / 5 000 $ a  9 999 $」
- 値：4760 | 7370 | 4530 | 5070 | 5630 | 930 | 550 | 1120
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $10,000 to $14,999 / 10 000 $ …, $15,000 to $19,999 / 15 000 $ …, $20,000 to $24,999 / 20 000 $ …
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Individual Tax Statistics の所得階級別申告件数。」

## e0026 — 見出し「service」
- 値：Find Business Regulation (FBR) | Report a Trade Barrier (RaTB) | Regulated Professions Register… | Business.gov.uk | Trade Remedies Service (TRS) | Business.gov.uk | Digital Market Access Service … | Report a Breach (RaB)
- 同じ表の列名：reporting_month, portfolio, users, sessions, cumulative_users
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「service は定義済みサービス名の区分。」

## e0027 — 見出し「RANK OF IMD SCORE (where 1 is most deprived)」
- 値：9045 | 11857 | 6148 | 16321 | 11576 | 22842 | 19057 | 9485
- 同じ表の列名：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, GOR CODE, IMD SCORE, INCOME SCORE, RANK OF INCOME SCORE (where 1 …, EMPLOYMENT SCORE, RANK OF EMPLOYMENT SCORE (wher…
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「RANK は deprivation score の順位区分。」

## e0028 — 見出し「date_of_publication_or_production_standardised」
- 値：1780 | 1781 | 1782 | 1783 | 1784 | 1785 | 1787 | 1788
- 同じ表の列名：library_call_number, digital_reproduction, title, place_of_publication_or_produc…, date_of_publication_or_product…, series, digital_reproduction_copyright, digital_object_identifier, digital_platform
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「date_of_publication_or_production は刊行・制作年。」

## e0029 — 見出し「value」
- 値：12958860367.92 | 3311818203.61 | 3674632983.64 | 16149934595.31 | 6410324420.9 | 5630602017.71 | 3901317329.87 | 7231329921.51
- 同じ表の単位の列：unit: CHF
- 同じ表の列名：arten, jahr, dim, hh, unit, model
- **前回のあなたの答え**：amount（決め手：単位の列）メモ「CHF と示された統計値は通貨金額。」

## e0030 — 見出し「TIME_PERIOD」
- 値：2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01
- 同じ表の列名：GEO, AGE, SEX, OBS_STATUS, OBS_VALUE
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「TIME_PERIOD は週を示す時間軸。」

## e0031 — 見出し「Class ID」
- 値：44,445.00 | 44,950.00 | 44,699.00 | 44,871.00 | 46,011.00 | 45,062.00 | 45,080.00 | 46,189.00
- 表の題名：New Established Special Classes Opening for 2026-2027 School Year
- 同じ表の列名：County, SRN, School Year, School Type, Class Type
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「Class ID は特別学級レコードの識別番号。」

## e0032 — 見出し「TOTAL_SHEEP_MOUNTAIN」
- 値：13028 | 10984 | 1316 | 59191 | 196521 | 6312 | 105879 | 183200
- 表の題名：DAFM National Sheep Census 2020
- 同じ表の列名：COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_IND, FLOCKS_WITH_TOTAL_SHEEP_CALC, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_CALC
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「National Sheep Census の羊・群れの頭数。」

## e0033 — 見出し「$10,000 to $14,999 / 10 000 $ a 14 999 $」
- 値：6880 | 7380 | 4820 | 7200 | 7510 | 1370 | 870 | 1710
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $15,000 to $19,999 / 15 000 $ …, $20,000 to $24,999 / 20 000 $ …
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Individual Tax Statistics の所得階級別申告件数。」

## e0034 — 見出し「$20,000 to $24,999 / 20 000 $ a 24 999 $」
- 値：9200 | 10560 | 6130 | 12280 | 14290 | 2530 | 1670 | 3010
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：Prov/Terr, CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $10,000 to $14,999 / 10 000 $ …, $15,000 to $19,999 / 15 000 $ …
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Individual Tax Statistics の所得階級別申告件数。」

## e0035 — 見出し「Version」
- 値：RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG | RETURN4_AUG
- 同じ表の列名：Organisation Code, Organisation, Control Budget Code, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Year, Quarter
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「Version は予算データの版を表す区分値。」

## e0036 — 見出し「Got everything I wanted」
- 値：31.8 | 20 | 20.1 | 23 | 24 | 26 | 37.15 | 11
- 同じ表の列名：Data status, Department, Organisation, Got most of what I wanted, Got some of what I wanted, Got none of what I wanted, Very Satisfied, Satisfied, Neither satisfied nor dissatis…
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「満足度の回答段階ごとの割合。」

## e0037 — 見出し「EW_Receiver_SA」
- 値：[z] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Total_Company_NSA
- **前回のあなたの答え**：category（決め手：値の形）メモ「[x]・[z] は系列の該当・状態フラグ。」

## e0038 — 見出し「Fossil fuels」
- 値：155975600 | 153398500 | 150781700 | 152557700 | 161329100 | 175027300 | 166924500 | 163439700
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Biomass, Metal ores, Non-metallic minerals, Total (All categories)
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Material Footprint の化石燃料量。」

## e0039 — 見出し「temporal」
- 値：2019-M11 | 2021-M01 | 2022-M02 | 2026-M03 | 2017-M09 | 2024-M11 | 2017-M07 | 2023-M07
- 同じ表の列名：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value, pop
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「temporal は年月を表す時点。」

## e0040 — 見出し「Emp_Wkf_POPD_15+yrs_2026」
- 値：1,235,608.02200 | 908,883.28090 | 617,945.99980 | 2,762,437.30270 | 168,306.25900 | 328,030.50980 | 207,870.90790 | 44,528.80621
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Workforce Projections の就業人口推計値。」

## 答えの雛形

```markdown
## e0001
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0002
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0003
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0004
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0005
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0006
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0007
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0008
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0009
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0010
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0011
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0012
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0013
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0014
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0015
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0016
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0017
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0018
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0019
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0020
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0021
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0022
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0023
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0024
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0025
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0026
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0027
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0028
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0029
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0030
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0031
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0032
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0033
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0034
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0035
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0036
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0037
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0038
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0039
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## e0040
- 前回の答えを変えるか：変えない／変える（新しい種類）
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

```
