# 教材の付け方の食い違い（`research/unknown/label_consistency.py`）

- 不明・重大の列（新しい陣 8 つ、366 列）の見出しの語ごとに、本体 C2 の学習の教材（b001〜b014）で同じ語を持つ列の種類を並べた
- **新しい陣と違う**＝教材でいちばん多い種類が、新しい陣の正解でいちばん多い種類と違う。**教材の中で割れる**＝教材で 2 つ以上の種類がそれぞれ 2 列以上かつ 2 番目が 20% 以上
- 「裁定で変えた」＝ChatGPT の初めのラベルと確定の種類が違う（Claude の裁定・ラベルの掃除）

| 語 | 新しい陣の正解 | 教材の種類 | 判定 | 教材で裁定で変えた例（初め→確定：理由） |
|---|---|---|---|---|
| uri | id 43 | other 3 | 新しい陣と違う |  |
| organisation | id 40 | org 8, date 1, id 1 | 新しい陣と違う |  |
| value | amount 9, quantity 3 | unknown 47, amount 44, quantity 22, category 18 | 新しい陣と違う・教材の中で割れる | b006 Estimated Total Value (Range)：amount→category（金額の区切り（$0-$10,000）は決まった選択肢なので category）; b008 Value：other→unknown（意味が決められない（単位のない年・月ごとの数、指数、値がばらばら、CSO の V）; b008 VALUE：other→unknown（意味が決められない（単位のない年・月ごとの数、指数、値がばらばら、CSO の V） |
| service | id 6, category 1, product 1 | category 19, id 13, quantity 6, account 5 | 新しい陣と違う・教材の中で割れる | b002 Service：category→account（部署・サービスの区分・費目の名前（account 行、例外の節「Departme）; b002 Service：category→account（部署・サービスの区分・費目の名前（account 行、例外の節「Departme）; b008 Service_Area：text→category（区分・種類・有無・○・決まった語の繰り返し・金額の区切り・業種は categor） |
| cost | id 5, amount 3 | amount 8, id 2, text 2, S 1 | 新しい陣と違う | b013 Cost：amount→text（料金の説明（Free Access・$4 per hour）は text（v1.）; b013 Cost management services：text→S（表が崩れている（見出しが値の行）ので S） |
| type | id 5, category 2 | category 389, account 11, id 5, address 4 | 新しい陣と違う | b006 LicType：category→S（個人の免許の一覧の表（表ごと値を消した）なので S）; b007 EVENT TYPE：category→S（個人の記録の表（表ごと値を消した）なので S）; b008 Type：address→category（区分・種類・有無・○・決まった語の繰り返し・金額の区切り・業種は categor） |
| standard | amount 4, rate 2 | category 5, id 4, rate 3, text 2 | 新しい陣と違う・教材の中で割れる | b011 ApplStandard：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10）; b011 Service Standard：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| houses | rate 5 | quantity 3 | 新しい陣と違う |  |
| centre | id 5 | org 2, address 2, unknown 1 | 新しい陣と違う・教材の中で割れる |  |
| category | id 5 | category 99, account 7, id 1 | 新しい陣と違う | b014 Business Category：address→category（業種（Business Category）の決まった語の繰り返しは catego） |
| time | quantity 3, date 2 | date 67, quantity 14, category 3, unknown 2 | 新しい陣と違う | b007 CREATE TIME：date→S（個人の記録の表（表ごと値を消した）なので S）; b009 FIVE YEAR DATA TIME SERIES：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10）; b013 Time.1st.Detected：date→quantity（初めて見つけるまでの分（時間の長さ）は quantity） |
| period | date 3, quantity 1 | date 22, quantity 8, category 2, amount 1 | 教材の中で割れる | b005 period：text→category（区分・目的・種類・品目の分類・単位・フラグなど決まった語の繰り返しは categ） |
| median | rate 2, amount 2 | quantity 3, rate 2, unknown 1 | 新しい陣と違う・教材の中で割れる |  |
| contracts | amount 4 | amount 5, quantity 3, rate 1 | 教材の中で割れる | b013 # of Awarded Contracts：S→quantity（契約の件数は quantity） |
| age | category 4 | quantity 29, rate 23, category 14, id 3 | 新しい陣と違う・教材の中で割れる | b004 Age：quantity→category（年齢の区切り（10 to 14 years）は category） |
| properties | rate 3 | quantity 4, amount 2 | 新しい陣と違う・教材の中で割れる |  |
| years | rate 3 | rate 4, date 4, quantity 4, category 1 | 教材の中で割れる | b009 Years：quantity→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| statistic | id 2, category 1 | id 64, category 63 | 教材の中で割れる | b008 Statistic：text→category（区分・種類・有無・○・決まった語の繰り返し・金額の区切り・業種は categor）; b011 Statistic：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10）; b011 Statistic：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| number | id 2, quantity 1 | quantity 128, id 125, unknown 8, S 2 | 新しい陣と違う・教材の中で割れる | b009 number：unknown→id（コード・番号・識別子・並べ替えの番号は id）; b009 Number：unknown→quantity（件数・人数・量・時間の長さ・年齢・回数は quantity）; b009 Number：unknown→address（番地は住所の一部なので address） |
| annual | amount 3 | quantity 3, amount 1 | 新しい陣と違う |  |
| staff | amount 3 | quantity 3, text 1, S 1 | 新しい陣と違う | b013 Temporary Staff：text→S（表が崩れている（見出しが値の行）ので S） |
| contract | amount 2, date 1 | category 10, date 10, id 5, amount 4 | 新しい陣と違う・教材の中で割れる | b012 contract：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| what | rate 3 | text 4, category 1 | 新しい陣と違う |  |
| non | quantity 1, amount 1 | quantity 8, category 5, amount 3, rate 1 | 教材の中で割れる |  |
| over | rate 2 | rate 7, amount 2, quantity 1 | 教材の中で割れる |  |
| reference | id 2 | id 13, date 5, text 1, other 1 | 教材の中で割れる |  |
| site | id 2 | address 17, id 15, category 6, other 2 | 新しい陣と違う・教材の中で割れる | b006 Site EUI (Energy Use Intensity：rate→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名）; b006 Total Site Energy Usage (kBtu)：quantity→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名） |
| company | quantity 2 | category 6, id 4, org 4, date 2 | 新しい陣と違う・教材の中で割れる |  |
| financial | amount 2 | date 19, org 1 | 新しい陣と違う |  |
| only | amount 2 | quantity 6, category 1 | 新しい陣と違う |  |
| end | amount 2 | date 43, quantity 4, address 2, rate 1 | 新しい陣と違う |  |
| week | date 2 | date 4, category 2, rate 1, quantity 1 | 教材の中で割れる | b007 DAY OF WEEK：category→S（個人の記録の表（表ごと値を消した）なので S） |
| min | quantity 2 | other 6 | 新しい陣と違う |  |
| production | date 2 | org 3, quantity 3 | 新しい陣と違う・教材の中で割れる |  |
| publication | date 2 | date 4, category 2, id 1, text 1 | 教材の中で割れる | b011 Publication：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| animal | rate 1, id 1 | category 12, id 2, quantity 1, date 1 | 新しい陣と違う |  |
| agency | id 2 | org 17, category 3, quantity 1, id 1 | 新しい陣と違う |  |
| tree | id 1 | category 5, id 5, quantity 2 | 新しい陣と違う・教材の中で割れる | b009 TreeHeight：other→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| map | quantity 1 | id 3 | 新しい陣と違う |  |
| caption | date 1 | text 9 | 新しい陣と違う |  |
| class | id 1 | category 38, id 7, quantity 2 | 新しい陣と違う | b009 Class_Screening_Title：text→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10）; b010 品目階層Item_Class：id→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
| component | category 1 | account 2, category 1 | 新しい陣と違う | b014 Program/Component：text→account（補助の事業（Program/Component）の名前は account（v1.）; b014 Program/Component：text→account（補助の事業（Program/Component）の名前は account（v1.） |
| tax | category 1 | amount 10, date 3, category 3, id 2 | 新しい陣と違う | b007 Property Tax Benefit (not a cr：text→category（区分・種類・選択肢の番号・順位・決まった語の繰り返しは category） |
| numero | id 1 | id 23, quantity 13, address 12, unknown 1 | 教材の中で割れる | b006 NUMERO：quantity→address（方書・場所の説明は住所の一部なので address）; b006 NUMERO：unknown→address（方書・場所の説明は住所の一部なので address）; b006 NUMERO：unknown→address（方書・場所の説明は住所の一部なので address） |
| family | category 1 | quantity 4, category 3, amount 3, text 1 | 新しい陣と違う・教材の中で割れる |  |
| position | id 1 | category 2, other 1 | 新しい陣と違う |  |
| sector | account 1 | category 17, id 4 | 新しい陣と違う |  |
| salary | amount 1 | rate 2, quantity 1, amount 1 | 新しい陣と違う |  |
| score | category 1 | rate 6, other 2, date 1, category 1 | 新しい陣と違う・教材の中で割れる | b006 Energy Star Score：rate→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名） |
| where | category 1 | unknown 1, category 1, address 1 | 新しい陣と違う |  |
| body | id 1 | org 4, address 1, category 1 | 新しい陣と違う |  |
| post | category 1 | address 11, category 3, quantity 1, amount 1 | 新しい陣と違う | b014 Post Retirement：quantity→S（値が … ばかりで見出しの文字も混ざるので S） |
| mean | rate 1 | quantity 3, other 2, amount 1 | 新しい陣と違う・教材の中で割れる | b004 MEAN：amount→other（平均（MEAN）は統計値なので other（v1.4「最小・平均・最大の統計値は） |
| male | rate 1 | quantity 6, rate 3, category 2, S 2 | 新しい陣と違う・教材の中で割れる |  |
| url | id 1 | other 9 | 新しい陣と違う |  |
| estimated | amount 1 | date 6, quantity 3, amount 2, category 1 | 新しい陣と違う・教材の中で割れる | b006 Estimated Total Value (Range)：amount→category（金額の区切り（$0-$10,000）は決まった選択肢なので category）; b014 daily_estimated_net_weight_kg：other→quantity（ごみの重さ（kg）は量なので quantity（v1.9）） |
| payment | date 1 | amount 9, quantity 5, category 4, date 1 | 新しい陣と違う・教材の中で割れる |  |
| june | amount 1 | quantity 9, unknown 1 | 新しい陣と違う |  |
| income | amount 1 | quantity 15, amount 11, category 3, unknown 1 | 新しい陣と違う・教材の中で割れる | b008 2023 Total Income：amount→category（区分・種類・有無・○・決まった語の繰り返し・金額の区切り・業種は categor） |
| supplier | org 1 | org 2, quantity 2, id 1, amount 1 | 教材の中で割れる | b010 ssd_supplier_band1__m：unknown→amount（金額（予算・資金・契約額・税の支出）は amount） |
| budget | category 1 | amount 13, date 3, category 1 | 新しい陣と違う |  |
| property | org 1 | id 11, category 6, address 2, amount 2 | 新しい陣と違う・教材の中で割れる | b007 Property Tax Benefit (not a cr：text→category（区分・種類・選択肢の番号・順位・決まった語の繰り返しは category） |
| plan | text 1 | category 2, id 1 | 新しい陣と違う |  |
| zone | rate 1 | category 7, id 5 | 新しい陣と違う・教材の中で割れる | b006 ZONE_：unknown→id（コード・番号・区の番号・識別子は id） |
| sensor | id 1 | date 4, category 4, unknown 1, other 1 | 新しい陣と違う・教材の中で割れる |  |
| program | category 1 | account 12, category 10, text 4, quantity 3 | 新しい陣と違う・教材の中で割れる | b010 Program：category→account（部署・課・係・費目・歳出の款項の名前は account（v1.3・v1.7））; b013 Program：text→account（予算の Program（事業の名前）は会計・部門の名前なので account（v）; b013 Program：text→account（予算の Program（事業の名前）は会計・部門の名前なので account（v） |
| max | quantity 1 | other 6, quantity 4, unknown 1 | 新しい陣と違う・教材の中で割れる |  |
| wind | quantity 1 | other 4, text 1 | 新しい陣と違う |  |
| designation | category 1 | date 2, category 2, text 1 | 新しい陣と違う・教材の中で割れる |  |
| library | id 1 | org 8, quantity 1 | 新しい陣と違う |  |
| variable | category 1 | id 4, category 2 | 新しい陣と違う・教材の中で割れる |  |
| energy | category 1 | other 4, category 3, quantity 2 | 新しい陣と違う・教材の中で割れる | b006 Site EUI (Energy Use Intensity：rate→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名）; b006 Energy Star Score：rate→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名）; b006 Total Site Energy Usage (kBtu)：quantity→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名） |
| none | rate 1 | S 3 | 新しい陣と違う | b009 None：text→S（表が崩れている（見出しが数・値と同じ、値が空や NULL・NA・記号だけ、JSO） |
| very | rate 1 | quantity 3 | 新しい陣と違う |  |
| procurement | date 1 | category 4, id 2, amount 2, S 2 | 新しい陣と違う・教材の中で割れる | b013 Procurement process audit：text→S（表が崩れている（見出しが値の行）ので S） |
| new | amount 1 | quantity 4, category 2, id 2, other 1 | 新しい陣と違う |  |
| fraud | quantity 1 | category 3 | 新しい陣と違う |  |
| building | id 1 | category 6, amount 3, id 2, date 1 | 新しい陣と違う・教材の中で割れる | b006 building_sqft：quantity→other（測定値（長さ・面積・体積・エネルギー・雨量）・統計値・スコア・URL・ファイル名） |
| question | id 1 | text 22, id 16, category 2 | 新しい陣と違う・教材の中で割れる |  |
| geo | id 1 | address 2, other 2 | 新しい陣と違う・教材の中で割れる |  |
| sex | quantity 1 | category 17 | 新しい陣と違う | b011 sex_code：id→category（区分・種類・有無・決まった語の繰り返し・統計の表の項目名・寸法の区切り（5-10） |
