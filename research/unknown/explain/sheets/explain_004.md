# 判断の説明 004 / 006（1 列ずつ、くわしく）

今の仕組みが「不明」と答えたか、種類を取り違えた列です。人がどう考えて種類を決めるかを、決め方の規則（C3 の判断のルール）に移したいので、**考えた順にくわしく**書いてください。

- この枚の列には、**前回の調査でのあなたの答え**を付けてあります（正しいとも誤りとも限りません）。前回なぜそう判断したかを、今の目で説明してください。考え直して変えるなら「前回の答えを変えるか」に書く
- LABEL_GUIDE.md（v2.1）の判定の順番（①列名・単位 → ②表の題名 → ③同じ表の列 → ④値の形）で、それぞれから**何が読めたか・読めなかったか**を書く。読めなければ「なし」
- 「迷った種類」には、候補に上がった別の種類と、それを退けた理由を書く（例：「amount も考えたが、通貨の記号も単位の列もなく、値が整数の小さい数なので quantity」）
- 「規則にするなら」は、ほかの表にも当てはまる言い方で 1〜2 文。当てはまらない例（その規則で誤りそうな列）も書く。規則にできないなら「できない（理由）」
- 決め手は次から 1 つ：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない。使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- **見ないもの**：`research/unknown/columns.jsonl`・`misses.jsonl`・`sheet_index.json`・`explain/index.json`・`compare*`・`candidates*`・`findings.md`（正解と今の仕組みの答えが入っている）、Grok の答え、モデルの予測
- 答え：末尾の雛形を写して埋め、`research/unknown/explain/answers_chatgpt/explain_004.md` に置く。見出し（`## x0001` など）と各行の頭（`- 種類：` など）は変えない

## e0081 — 見出し「Emp_Wkf_POPD_15+yrs_2024」
- 値：1,230,867.76500 | 884,670.85480 | 600,290.44310 | 2,715,829.06290 | 165,808.21300 | 328,091.61860 | 205,357.00860 | 44,707.77680
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Workforce Projections の就業人口推計値。」

## e0082 — 見出し「reporting_period」
- 値：P02 | P01 | P01 | P02 | P01 | P02 | P01 | P02
- 表の題名：Proactive Disclosure - Question Period notes
- 同じ表の列名：year
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「P01・P02 は報告期間の区分コード。」

## e0083 — 見出し「Widmung」
- 値：'In segno di alta stima, e Con…
- 同じ表の列名：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration
- **前回のあなたの答え**：text（決め手：見出しの語）メモ「Widmung は書物に記された自由形式の献辞。」

## e0084 — 見出し「Non-Payroll staff (contingent labour/consultancy - CCL) cost」
- 値：Total cost of contingent labou… | ｣1,363,024 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsoring de…, Payroll staff, Number of non-payroll staff (c…, Grand Total  (workforce number…, Payroll staff costs, Grand Total paybill/staffing (…, Comments and notes
- **前回のあなたの答え**：amount（決め手：見出しの語）メモ「Non-Payroll staff cost は人件費。」

## e0085 — 見出し「buy_to_let_properties__floating_rate__standard_or_ltv_variab」
- 値：4.53 | 4.52 | 4.24 | 4.2 | 4.2 | 4.38 | 4.15 | 4.03
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0086 — 見出し「Arrest/Detention > Fraud」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「詐欺による逮捕・拘留の件数列。」

## e0087 — 見出し「Total」
- 値：1,062.00 | 964.93 | 919.62 | 800.40 | 793.08 | 774.57 | 755.32 | 751.34
- 同じ表の列名：Transaction Date
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Total と日付列だけでは金額・数量などを区別できない。」

## e0088 — 見出し「principal_dwelling_houses__floating_rate__up_to_1_year_fixed」
- 値：3.33 | 3.33 | 3.54 | 3.5 | 3.51 | 3.53 | 3.49 | 3.42
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0089 — 見出し「principal_dwelling_houses__floating_rate__standard_or_ltv_va」
- 値：4.19 | 4.26 | 3.82 | 3.77 | 3.76 | 3.78 | 3.75 | 3.66
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0090 — 見出し「Mandatory Relief %」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Property Ref, Rate Payer, Start of Liability, Rateable Value 2010, Empty, Empty From, Charity, Discretionary relief %, Small Business Rate Relief
- **前回のあなたの答え**：rate（決め手：見出しの語）メモ「Mandatory Relief % は軽減率。」

## e0091 — 見出し「Dwellings value」
- 値：nil | nil | 82 | nil | 579 | 99 | 354 | 292
- 同じ表の列名：Valuation Band  Range, Intervening bands, Tenure Status
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「Dwellings value の表における dwelling の戸数。」

## e0092 — 見出し「EW_Total_Company_NSA」
- 値：3597 | 3520 | 2553 | 2567 | 5067 | 5615 | 4700 | 5689
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「EW_Total_Company の非季節調整済み企業数。」

## e0093 — 見出し「Titel」
- 値：Parkhaus Storchen | Parkhaus Storchen | Parkhaus Elisabethen | Parkhaus Messe | Parkhaus Kunstmuseum | Parkhaus Steinen | Parkhaus Europe | Parkhaus Rebgasse
- 同じ表の列名：Publikationszeit, Anzahl frei, Total Plätze, Anteil belegter Parkplätze, id, id2, link, geo_point_2d, Beschreibung
- **前回のあなたの答え**：address（決め手：値の形）メモ「Titel は建物である駐車場の名称。」

## e0094 — 見出し「wert」
- 値：12931 | 44 | 31 | 7 | 17 | 7 | 14578 | 32
- 同じ表の列名：jahr, bildungsabschluss, metrik, einheit
- **前回のあなたの答え**：unknown（決め手：同じ表の列名）メモ「wert は汎用値で、metric と unit の具体的内容が不足。」

## e0095 — 見出し「vj_rel_kumsum」
- 値：NA | NA | NA | NA | 0.0369630369630369 | 0.0329865516366405 | 0.0265224219158959 | -0.0110789980732178
- 同じ表の列名：jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum
- **前回のあなたの答え**：rate（決め手：見出しの語）メモ「vj_rel_kumsum は前年比の相対累積変化率。」

## e0096 — 見出し「Gcons2006」
- 値：14300 | 22500 | 3000 | 500 | 16000 | 8400 | 14700 | 21000
- 同じ表の列名：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005, Gcons2005Valid, Gcons2006Valid, Gcons2007, Gcons2007Valid
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Gcons の意味・単位がなく、値だけで金額か数量か決められない。」

## e0097 — 見出し「Cost Centre」
- 値：E7036 | L3951 | S6131 | B8450 | S6141 | S6141 | S6141 | S6141
- 同じ表の列名：Transaction Number, Paid Date, Paid Amount, Department, Irrecoverable VAT
- **前回のあなたの答え**：id（決め手：値の形）メモ「Cost Centre の英数字コードはコストセンター識別子。」

## e0098 — 見出し「Neither satisfied nor dissatisfied」
- 値：10.6 | 16.7 | 21.3 | 32 | 15 | 14.3 | 14.68 | 6
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wanted, Got some of what I wanted, Got none of what I wanted, Very Satisfied, Satisfied
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「満足度の段階別割合を示す調査指標。」

## e0099 — 見出し「Family_Famille」
- 値：Sapindaceae | betulaceae | Rosaceae | Asteraceae | Asteraceae | asteraceae | Asteraceae | cyperaceae
- 表の題名：TOPIC Open - Literature Review Module
- 同じ表の列名：ID, SpeciesCode_CodeEspece, Synonym_Synonyme, TraitCode, TraitValue_ValeurTrait, TraitValueDescription_Descript…, TraitValueComments_Commentaire…, ReferenceID, ReferenceType
- **前回のあなたの答え**：other（決め手：見出しの語）メモ「Family は植物の科学的な分類群名。」

## e0100 — 見出し「Arrest/Detention > Drugs」
- 値：<5 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「逮捕・拘留の薬物関連件数で、<5 は秘匿件数。」

## e0101 — 見出し「MaleLowerQuartile」
- 値：60.30 | 59.00 | 78.90 | 10.00 | 70.30 | 94.20 | 37.00 | 77.70
- 同じ表の列名：EmployerId, CompanyNumber, SicCodes, DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent, MaleBonusPercent, FemaleBonusPercent
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「MaleLowerQuartile は賃金四分位の構成割合。」

## e0102 — 見出し「Time period」
- 値：12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award | 12 months from award
- 同じ表の列名：Grant recipient, Registration number, amount allocated, Date of award
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「Time period は受賞後12か月の期間の長さ。」

## e0103 — 見出し「Control Budget Code」
- 値：DEL | DEL | AME | DEL | AME | DEL | DEL | DEL
- 同じ表の列名：Organisation Code, Organisation, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Version, Year, Quarter
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「Control Budget Code は予算区分コード。」

## e0104 — 見出し「Tax gap component」
- 値：PIT: reporting gap (hidden off… | PIT: gross tax gap (lower-boun… | PIT: net tax gap (upper-bound) | CIT: reporting gap (SMEs, lowe… | CIT: reporting gap (SMEs, uppe… | CIT: reporting gap (SMEs, % of… | CIT: reporting gap (large corp… | CIT: reporting gap (large corp…
- 表の題名：Overall federal tax gap report: Estimates and key findings for non-com…
- 同じ表の列名：2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
- **前回のあなたの答え**：category（決め手：表の題名）メモ「Tax gap component は税ギャップ内訳の定義済み区分。」

## e0105 — 見出し「Legislatur」
- 値：01.01.2013 - 31.12.2016 | 01.01.2013 - 31.12.2016 | 01.01.2017 - 31.12.2020 | 01.01.2021 - 31.12.2024 | 01.01.2021 - 31.12.2024 | 01.01.2021 - 31.12.2024 | 01.01.2021 - 31.12.2024 | 01.01.2021 - 31.12.2024
- 同じ表の列名：Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Zeit, Bemerkungen, Geschaeftstyp
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「Legislatur は開始日・終了日のある議会期。」

## e0106 — 見出し「Cost Centre」
- 値：990 | 1510 | 2110 | 990 | 1302 | 1201 | 990
- 同じ表の列名：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number, Amount in Sterling
- **前回のあなたの答え**：id（決め手：値の形）メモ「Cost Centre の数値コードはコストセンター識別子。」

## e0107 — 見出し「plan」
- 値：Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado…
- 同じ表の列名：FID, id, code, location
- **前回のあなたの答え**：text（決め手：値の形）メモ「plan に入る個別の計画書名・文書名。」

## e0108 — 見出し「principal_dwelling_houses__floating_rate__tracker_mortgages_」
- 値：1.03 | 1.05 | 1.03 | 1.03 | 1.03 | 1.04 | 1.04 | 1.04
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0109 — 見出し「SMR 2019-2023」
- 値：1.1 | 0.7 | 1.0 | * | * | 0.6 | 1.6 | 5.2
- 同じ表の列名：institution, indicator, taux observe 2019-2023, taux attendu 2019-2023, nombre de cas 2019-2023, taux observe 2024, taux attendu 2024, SMR 2024, nombre de cas 2024
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「SMR は観測死亡数と期待死亡数の比率。」

## e0110 — 見出し「Value」
- 値：333.20 | 1,489.75 | 14,400.00 | 448,000.00 | 25,000.00 | 7,020.00 | 13,617.20 | 42,500.00
- 同じ表の列名：Reference Number, Purchase Order Date, Local Authority Department
- **前回のあなたの答え**：amount（決め手：同じ表の列名）メモ「Purchase Order の Value は発注金額。」

## e0111 — 見出し「YearWeekIso」
- 値：202441 | 202441 | 202442 | 202442 | 202442 | 202442 | 202443 | 202444
- 同じ表の列名：LastDayOfWeek, Variable, Number
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「YearWeekIso は暦上の年・週。」

## e0112 — 見出し「Wert」
- 値：44445966754.09931 | 45213068201.47224 | 48691273509.50475 | 53154938765.891846 | 52104361215.42215 | 53136735491.91763 | 51749555387.060326 | 54899558375.98117
- 同じ表の列名：Stichtag, Kennzahl
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Wert と Kennzahl だけでは測定対象・単位が特定できない。」

## e0113 — 見出し「NO_COMPLEMENTAIRE」
- 値：1 | 1 | 1 | 1 | 1 | 1 | 1 | 1
- 同じ表の列名：PK     L"]]­„³²MóMó   …, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, STATUT, OPERATION, ORIGINE
- **前回のあなたの答え**：S（決め手：同じ表の列名）メモ「同じ表の見出しに ZIP バイナリ由来の文字列が混ざり崩れている。」

## e0114 — 見出し「SiteReference」
- 値：292 | 351 | 1411 | 2024 | 2343 | 3053 | 4608a | 8069
- 同じ表の列名：OrganisationURI, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「SiteReference は地点を参照する識別番号。」

## e0115 — 見出し「Arrest/Detention > Child Pornography」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「逮捕・拘留の児童ポルノ関連件数。」

## e0116 — 見出し「Contract Commencement Date」
- 値：45804 | 46202 | 45541 | 45346 | 45139 | 45230 | 45264 | 45383
- 同じ表の列名：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start Date, New Contract End Date, Value of New Contract (Excludi…, Procurement Sourcing Route, Category
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「Contract Commencement Date は契約開始日。」

## e0117 — 見出し「Q3 (October - December 2014)」
- 値：548.66 | 347 | 0 | 5.55 | 7.1 | 860.35 | 2416.06 | 543.96
- 同じ表の列名：Expense type, Q1 (April - June 2014), Q2 (July - September 2014), Q4 (January - March 2015)
- **前回のあなたの答え**：amount（決め手：同じ表の列名）メモ「Q1〜Q4 は費目ごとの四半期支出額。」

## e0118 — 見出し「Datierung_Bemerkung」
- 値：Poststempel | Entzifferung unsicher | Orig.: 8 Octobre nouveau style… | 9. Juni (?) | Dat. Karte (Br. undat.) | Entzifferung unsicher | Entzifferung unsicher | Orig.: 29. Brumaire an IV
- 同じ表の列名：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Illustration, Widmung
- **前回のあなたの答え**：text（決め手：見出しの語）メモ「Datierung_Bemerkung は日付に関する自由記述の注記。」

## e0119 — 見出し「AnzStand」
- 値：1 | 16 | 1 | 15 | 3 | 1 | 1 | 13
- 同じ表の列名：KT, Inst, Adr, Ort, KT_Standort, Ort_Standort, LA
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「AnzStand は施設・拠点数を示す。」

## e0120 — 見出し「Age」
- 値：0-64 | 65+ | 65+ | 65+ | 65+ | 0-64 | 65+ | 65+
- 同じ表の列名：AC, Semaine, Fin, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「Age の 0-64・65+ は年齢階級。」

## 答えの雛形

```markdown
## e0081
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

## e0082
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

## e0083
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

## e0084
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

## e0085
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

## e0086
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

## e0087
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

## e0088
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

## e0089
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

## e0090
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

## e0091
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

## e0092
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

## e0093
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

## e0094
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

## e0095
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

## e0096
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

## e0097
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

## e0098
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

## e0099
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

## e0100
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

## e0101
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

## e0102
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

## e0103
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

## e0104
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

## e0105
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

## e0106
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

## e0107
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

## e0108
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

## e0109
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

## e0110
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

## e0111
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

## e0112
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

## e0113
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

## e0114
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

## e0115
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

## e0116
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

## e0117
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

## e0118
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

## e0119
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

## e0120
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
