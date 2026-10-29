# 判断の説明 005 / 006（1 列ずつ、くわしく）

今の仕組みが「不明」と答えたか、種類を取り違えた列です。人がどう考えて種類を決めるかを、決め方の規則（C3 の判断のルール）に移したいので、**考えた順にくわしく**書いてください。

- この枚の列には、**前回の調査でのあなたの答え**を付けてあります（正しいとも誤りとも限りません）。前回なぜそう判断したかを、今の目で説明してください。考え直して変えるなら「前回の答えを変えるか」に書く
- LABEL_GUIDE.md（v2.1）の判定の順番（①列名・単位 → ②表の題名 → ③同じ表の列 → ④値の形）で、それぞれから**何が読めたか・読めなかったか**を書く。読めなければ「なし」
- 「迷った種類」には、候補に上がった別の種類と、それを退けた理由を書く（例：「amount も考えたが、通貨の記号も単位の列もなく、値が整数の小さい数なので quantity」）
- 「規則にするなら」は、ほかの表にも当てはまる言い方で 1〜2 文。当てはまらない例（その規則で誤りそうな列）も書く。規則にできないなら「できない（理由）」
- 決め手は次から 1 つ：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない。使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- **見ないもの**：`research/unknown/columns.jsonl`・`misses.jsonl`・`sheet_index.json`・`explain/index.json`・`compare*`・`candidates*`・`findings.md`（正解と今の仕組みの答えが入っている）、Grok の答え、モデルの予測
- 答え：末尾の雛形を写して埋め、`research/unknown/explain/answers_chatgpt/explain_005.md` に置く。見出し（`## x0001` など）と各行の頭（`- 種類：` など）は変えない

## e0121 — 見出し「digital_platform」
- 値：e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch
- 同じ表の列名：library_call_number, digital_reproduction, title, place_of_publication_or_produc…, date_of_publication_or_product…, date_of_publication_or_product…, series, digital_reproduction_copyright, digital_object_identifier
- **前回のあなたの答え**：other（決め手：値の形）メモ「値はデジタルプラットフォームのドメイン名・URL。」

## e0122 — 見出し「Quarter」
- 値：1979Q1 | 1979Q2 | 1982Q3 | 1991Q2 | 1992Q4 | 2001Q2 | 1981Q2 | 1987Q1
- 表の題名：HSQ08 - House Loans Approved and Paid
- 同じ表の単位の列：UNIT: Number, Euro Million
- 同じ表の列名：STATISTIC, Statistic, TLIST(Q1), C02350V02827, House Type New or Second hand, UNIT, VALUE
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「Quarter の YYYYQn 値は暦上の四半期。」

## e0123 — 見出し「Arrest/Detention > Murder / Manslaughter」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「殺人・過失致死による逮捕・拘留件数。」

## e0124 — 見出し「TLIST(A1)」
- 値：1992 | 1993 | 1993 | 1993 | 1994 | 1995 | 1995 | 1996
- 表の題名：EDA36 - Percentage of persons aged 20-24 years having Completed at Lea…
- 同じ表の単位の列：UNIT: %
- 同じ表の列名：STATISTIC, Statistic, Year, C02199V02655, Sex, UNIT, VALUE
- **前回のあなたの答え**：date（決め手：見出しの語）メモ「TLIST(A1) は統計表の暦年軸。」

## e0125 — 見出し「energy」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：issued, administration, agriculture, construction, crime, culture, education, finances, geography
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「0 だけではテーマ別件数か二値指標か判断できない。」

## e0126 — 見出し「aktiver_energieverbrauch」
- 値：2.05199999999999 | 9.57499999999998 | 14.433 | 8.481 | 2.103 | 0 | 0.966000000000001 | 0.001
- 同じ表の列名：id, jahr, stadt, plz, haus_nr, ladeleistung, connector_typ, stop_typ, aktive_ladeleistung
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「aktiver_energieverbrauch はエネルギー消費量。」

## e0127 — 見出し「Ratio」
- 値：4.28:1 | 3.81:1 | 6.14:1 | 3.96:1 | 3.57:1 | 5.39:1 | 4.64:1 | 4.02:1
- 同じ表の列名：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Period, ModelCalculation, OrganisationType, PayPolicyStatementURL
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「Ratio は報酬倍率の比率。」

## e0128 — 見出し「Property」
- 値：Department | Home Office - IPS | Home Office - IPS | Home Office - NPIA | Home Office - GEO | Home Office - GEO | Home Office - UKBA | Home Office - UKBA
- 同じ表の列名：exceptions for period 01 Novem…
- **前回のあなたの答え**：account（決め手：値の形）メモ「Property 欄の値は Home Office 内の部門名。」

## e0129 — 見出し「Arrest/Detention > Immigration」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「移民関連の逮捕・拘留件数。」

## e0130 — 見出し「03:00」
- 値：97 | 108 | 58 | 94 | 98 | 94 | 95 | 117
- 同じ表の列名：DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:30, 04:00
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「時刻別の数値だが測定対象・単位が示されない。」

## e0131 — 見出し「Biomass」
- 値：131582800 | 123151500 | 143881300 | 154014800 | 160529000 | 179414000 | 183334800 | 173978700
- 表の題名：Material Footprint for Australia
- 同じ表の列名：Product, Fossil fuels, Metal ores, Non-metallic minerals, Total (All categories)
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Material Footprint のバイオマス量。」

## e0132 — 見出し「wert」
- 値：637 | 5 | 12 | 0 | 55 | 5 | 30 | 16
- 同じ表の列名：jahr, fallstruktur, metrik, einheit
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「wert は汎用値で、metric と unit の具体的内容が不足。」

## e0133 — 見出し「EW_Admin_SA」
- 値：[z] | [x] | [x] | [x] | [x] | [x] | [x] | [x]
- 同じ表の列名：Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_CVA_SA, EW_Receiver_SA, EW_Total_Company_NSA
- **前回のあなたの答え**：category（決め手：値の形）メモ「[x] は季節調整系列の該当フラグ。」

## e0134 — 見出し「principal_dwelling_houses__fixed_rate__over_3_years__rates_o」
- 値：3.94 | 3.83 | 3.37 | 3.36 | 3.34 | 3.24 | 3.23 | 3.22
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0135 — 見出し「Arrest/Detention > Modern Slavery / Human Trafficking」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Murder / Ma…
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「人身取引関連の逮捕・拘留件数。」

## e0136 — 見出し「finances」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：issued, administration, agriculture, construction, crime, culture, education, energy, geography
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「0 だけではテーマ別件数か二値の区分列か判断できない。」

## e0137 — 見出し「buy_to_let_properties__floating_rate__tracker_mortgages__rat」
- 値：1.09 | 1.09 | 1.06 | 1.06 | 1.06 | 1.09 | 1.05 | 1.05
- 表の題名：Retail Interest Rates - Mortgage Rates
- 同じ表の列名：Reporting date, buy_to_let_properties__floatin…, buy_to_let_properties__fixed_r…, buy_to_let_properties__fixed_r…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__flo…, principal_dwelling_houses__fix…, principal_dwelling_houses__fix…
- **前回のあなたの答え**：rate（決め手：表の題名）メモ「Retail Interest Rates の住宅ローン金利。」

## e0138 — 見出し「Emp_Wkf_POPD_15+yrs_2025」
- 値：1,227,114.17300 | 894,414.05980 | 609,571.58220 | 2,731,099.81500 | 167,351.77280 | 324,530.32080 | 205,582.51470 | 44,294.62793
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Workforce Projections の就業人口推計値。」

## e0139 — 見出し「Grand Total  (workforce numbers)」
- 値：Headcount | 1,246 | 115 | 43 | 17 | 0 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsoring de…, Payroll staff, Number of non-payroll staff (c…, Payroll staff costs, Non-Payroll staff (contingent …, Grand Total paybill/staffing (…, Notes for Cabinet Office (Not …
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「Grand Total の workforce numbers は職員数。」

## e0140 — 見出し「Total」
- 値：528.00 | 718.80 | 602.00 | 1429.50 | 531.50 | 2712.00 | 626.24 | 1126.80
- 同じ表の列名：Transaction Type, Transaction Date, Transaction Reference, Merchant
- **前回のあなたの答え**：amount（決め手：値の形）メモ「取引表の Total の値がポンド建て。」

## e0141 — 見出し「AGE」
- 値：Y40T44 | Y15T19 | Y30T34 | Y10T14 | Y30T34 | Y30T34 | Y55T59 | Y75T79
- 同じ表の列名：TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE
- **前回のあなたの答え**：category（決め手：見出しの語）メモ「AGE の Y40T44 などは年齢階級コード。」

## e0142 — 見出し「Got none of what I wanted」
- 値：16.5 | 16.6 | 24.6 | 5 | 14 | 33.3 | 19 | 63
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wanted, Got some of what I wanted, Very Satisfied, Satisfied, Neither satisfied nor dissatis…
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「満足度の回答段階ごとの割合。」

## e0143 — 見出し「VALUE」
- 値：. | . | . | . | . | . | . | .
- 表の題名：JQ06 – Stock of nurses by country of first qualification
- 同じ表の単位の列：UNIT: Number
- 同じ表の列名：STATISTIC, Statistic Label, YEAR, Year, TRNGTYPE, Type of training, QUALCOU, UNIT, FLAG
- **前回のあなたの答え**：S（決め手：値の形）メモ「値がすべて欠損記号のため学習対象外。」

## e0144 — 見出し「LowerB」
- 値：147 | 147 | 145 | 139 | 140 | 139 | 143 | 133
- 同じ表の列名：Year, Week, Ending, Age, NoDeaths_EP, Expected, UpperB, Diff
- **前回のあなたの答え**：quantity（決め手：同じ表の列名）メモ「死亡数の予測に対する下限値で、死亡件数の尺度。」

## e0145 — 見出し「C02199V02655」
- 値：- | - | 1 | 2 | 1 | - | 2 | 1
- 表の題名：EDA36 - Percentage of persons aged 20-24 years having Completed at Lea…
- 同じ表の単位の列：UNIT: %
- 同じ表の列名：STATISTIC, Statistic, TLIST(A1), Year, Sex, UNIT, VALUE
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「C02199V02655 は統計分類のコード列。」

## e0146 — 見出し「C02350V02827」
- 値：2 | 1 | 1 | 1 | 2 | 2 | 1 | 2
- 表の題名：HSQ08 - House Loans Approved and Paid
- 同じ表の単位の列：UNIT: Number, Euro Million
- 同じ表の列名：STATISTIC, Statistic, TLIST(Q1), Quarter, House Type New or Second hand, UNIT, VALUE
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「C02350V02827 は統計分類のコード列。」

## e0147 — 見出し「Gcons2005」
- 値：15600 | 23000 | 7000 | 500 | 22000 | 12300 | 12800 | 21500
- 同じ表の列名：HH_ID, REGION, IMD_ENG, IMD_WALES, Gcons2005Valid, Gcons2006, Gcons2006Valid, Gcons2007, Gcons2007Valid
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Gcons2005 は単位や測定対象が示されず金額か数量か不明。」

## e0148 — 見出し「organisati」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：FID, id_0, id, organisa_1, siterefere, site_id_2, siteplanur, geox, geoy
- **前回のあなたの答え**：id（決め手：同じ表の列名）メモ「組織名・組織ID列と対になる組織 URI。」

## e0149 — 見出し「Nachgefragt」
- 値：16100 | 8100 | 902600 | 22500 | 2500 | 20900 | 20000 | 12400
- 同じ表の列名：Kategorie, Sparte, Beschluss, Status, Eingangsdatum, Beschlussdatum, ID
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Nachgefragt と数値だけでは件数か金額か特定できない。」

## e0150 — 見出し「Supplier」
- 値：TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 2 | TPS – Funding Account 1 | TPS – Funding Account 2 | TPS – Funding Account 2
- 同じ表の列名：Departmental Family, Entity, Date, Expense type, Expense area, Transaction Number, Amount
- **前回のあなたの答え**：account（決め手：値の形）メモ「Supplier 欄の値は Funding Account という内部会計口座名。」

## e0151 — 見出し「Prov/Terr」
- 値：12 | 13 | 13 | 24 | 24 | 24 | 24 | 24
- 表の題名：Individual Tax Statistics by Area (ITSA) (2022 Tax Year)
- 同じ表の列名：CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $10,000 to $14,999 / 10 000 $ …, $15,000 to $19,999 / 15 000 $ …, $20,000 to $24,999 / 20 000 $ …
- **前回のあなたの答え**：address（決め手：見出しの語）メモ「Prov/Terr はカナダの州・準州を示す地理項目。」

## e0152 — 見出し「vj_abs_kumsum」
- 値：NA | NA | NA | NA | 74 | 130 | 152 | -23
- 同じ表の列名：jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_rel_kumsum
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「vj_abs_kumsum は件数 n の累積差。」

## e0153 — 見出し「Amount per Container」
- 値：0.50 lbs | 104 mL | 17 mL | 18.9 L | 104 mL | 946 mL | 6 Oz | 91 mL
- 表の題名：Hazardous Waste Inventory Audit
- 同じ表の列名：Date, New/Used, Hazard Class, Quantity
- **前回のあなたの答え**：quantity（決め手：見出しの語）メモ「容器ごとの内容量で、lbs・mL・L などの単位がある。」

## e0154 — 見出し「Got some of what I wanted」
- 値：14.1 | 26.7 | 37.7 | 45 | 26 | 25.9 | 24.85 | 18
- 同じ表の列名：Data status, Department, Organisation, Got everything I wanted, Got most of what I wanted, Got none of what I wanted, Very Satisfied, Satisfied, Neither satisfied nor dissatis…
- **前回のあなたの答え**：rate（決め手：同じ表の列名）メモ「満足度の回答段階ごとの割合。」

## e0155 — 見出し「Total」
- 値：752.6 | 2612.04 | -5030.49 | -1490.8 | 5286.99 | 4316.99 | 512.69 | 1078.53
- 同じ表の列名：Transaction Date, Transaction Reference, Merchant
- **前回のあなたの答え**：amount（決め手：同じ表の列名）メモ「取引表の Total は返金を含む取引金額。」

## e0156 — 見出し「Cost Centre」
- 値：1002 | 2112 | 1201 | 1101 | 0000 | 0000 | 0000
- 同じ表の列名：Department family, Entity, Date of payment, Expense Code, Expense type, Expense area, Supplier, Transaction Number, Amount in Sterling
- **前回のあなたの答え**：id（決め手：値の形）メモ「Cost Centre の数値コードは識別用コード。」

## e0157 — 見出し「Versicherer」
- 値：57 | 62 | 134 | 246 | 343 | 360 | 376 | 455
- 同じ表の列名：Kanton, Geschaftsjahr, Durchschnittsbestand
- **前回のあなたの答え**：unknown（決め手：決められない）メモ「Versicherer と整数値だけでは保険者コードか件数か分からない。」

## e0158 — 見出し「Emp_Wkf_POPD_15+yrs_2023」
- 値：1,242,188.46500 | 850,937.51060 | 583,815.02590 | 2,676,941.00150 | 156,672.76460 | 318,318.66920 | 212,785.51820 | 44,370.78162
- 表の題名：Workforce Projections
- 同じ表の列名：Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029
- **前回のあなたの答え**：quantity（決め手：表の題名）メモ「Workforce Projections の就業人口推計値。」

## e0159 — 見出し「OrganisationCode」
- 値：http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…
- 同じ表の列名：EffectiveDate, FinancialYear, Department, Payee, Language, Amount
- **前回のあなたの答え**：id（決め手：見出しの語）メモ「OrganisationCode の値は組織リソース URI。」

## e0160 — 見出し「Payroll staff costs」
- 値：Salary | ｣72,902,946 | 0 | 0
- 同じ表の列名：Organisation  type, Main, parent or  sponsoring de…, Payroll staff, Number of non-payroll staff (c…, Grand Total  (workforce number…, Non-Payroll staff (contingent …, Grand Total paybill/staffing (…, Comments and notes
- **前回のあなたの答え**：amount（決め手：見出しの語）メモ「Payroll staff costs は給与費用。」

## 答えの雛形

```markdown
## e0121
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

## e0122
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

## e0123
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

## e0124
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

## e0125
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

## e0126
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

## e0127
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

## e0128
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

## e0129
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

## e0130
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

## e0131
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

## e0132
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

## e0133
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

## e0134
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

## e0135
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

## e0136
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

## e0137
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

## e0138
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

## e0139
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

## e0140
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

## e0141
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

## e0142
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

## e0143
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

## e0144
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

## e0145
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

## e0146
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

## e0147
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

## e0148
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

## e0149
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

## e0150
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

## e0151
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

## e0152
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

## e0153
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

## e0154
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

## e0155
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

## e0156
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

## e0157
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

## e0158
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

## e0159
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

## e0160
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
