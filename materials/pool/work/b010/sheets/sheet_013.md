# ラベル用シート 013 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_013.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1441（1 列）
- 見出し：転入
- 例1 値：420 | 472 | 419 | 403 | 580
  - 同じ表の列：地方公共団体名, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 転出

## g1442（1 列）
- 見出し：転出
- 例1 値：540 | 471 | 410 | 1093 | 500
  - 同じ表の列：地方公共団体名, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 転入

## g1443（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都日野市 | 東京都日野市 | 東京都日野市 | 東京都日野市 | 東京都日野市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 方書

## g1444（1 列）
- 見出し：名称
- 例1 値：セレモニー小峰 | 葬援(日野市 葬儀相談センター) | 日野セレモニー | JA東京みなみ(セレモニーセンター) | 三和式典
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 方書

## g1445（1 列）
- 見出し：名称_カナ
- 例1 値：セレモニーコミネ | ジェイエートウキョウミナミヒノシテン | セレモハイネス | ヒノセレモニー | ニシトウキョウソウケン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 方書

## g1446（1 列）
- 見出し：方書
- 例1 値：大沢ビル1階
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ

## g1447（1 列）
- 見出し：教育機関_学校コード
- 例1 値：B113221400035 | B113221400026 | B113221400099 | B113221400017 | B113221400080
  - 同じ表の列：教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1448（1 列）
- 見出し：教育機関_学校種
- 例1 値：B1 | C1 | C1 | B1 | C1
  - 同じ表の列：教育機関_学校コード, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1449（1 列）
- 見出し：教育機関_都道府県番号
- 例1 値：13 | 13 | 13 | 13 | 13
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1450（1 列）
- 見出し：教育機関_設置区分
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_本分校, 教育機関_学校名, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1451（1 列）
- 見出し：教育機関_本分校
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_学校名, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1452（1 列）
- 見出し：教育機関_学校名
- 例1 値：国分寺市立第一小学校 | 国分寺市立第二中学校 | 国分寺市立第五中学校 | 国分寺市立第八小学校 | 国分寺市立第六小学校
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_属性情報設定年月日, 教育機関_旧学校調査番号

## g1453（1 列）
- 見出し：教育機関_属性情報設定年月日
- 例1 値：2020-12-22 | 2020-12-22 | 2020-12-22 | 2020-12-22 | 2020-12-22
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名, 教育機関_旧学校調査番号

## g1454（1 列）
- 見出し：教育機関_旧学校調査番号
- 例1 値：131420 | 131418 | 131417 | 131416 | 131414
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名, 教育機関_属性情報設定年月日

## g1455（1 列）
- 見出し：名称
- 例1 値：JAにしたま葬祭センター | そうしんフレールホール福生 | 愛和セレモニー | 株式会社セレサポート | 有限会社西武葬祭
  - 同じ表の列：全国地方公共団体コード, 法人番号, 地方公共団体名, 名称_カナ

## g1456（1 列）
- 見出し：名称_カナ
- 例1 値：カブシキカイシャセレサポート | アイワセレモニー | ユウゲンガイシャセイブソウサイ | ソウギ・シュウカツソウダンセンターフィーネ | カブシキカイシャタマサイテン
  - 同じ表の列：全国地方公共団体コード, 法人番号, 地方公共団体名, 名称

## g1457（1 列）
- 見出し：地方公共団体名
- 例1 値：狛江市 | 狛江市 | 狛江市 | 狛江市 | 狛江市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ

## g1458（1 列）
- 見出し：名称
- 例1 値：狛江市民総合体育館 | あいとぴあセンター | えきまえ広場デジタルサイネージ | 上和泉地域センター図書室 | 岩戸地域センター図書室
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ

## g1459（1 列）
- 見出し：名称_カナ
- 例1 値：ナンブチイキセンタートショシツ | カミイズミチイキセンター | マエハラコウエンデジタルサイネージ | ノガワチイキセンタートショシツ | アイトピアセンター
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称

## g1460（1 列）
- 見出し：名称
- 例1 値：合同会社 大南葬祭 | 株式会社 多摩祭典 | 株式会社 セレモア | 株式会社 セレサポート | 有限会社 成華園
  - 同じ表の列：名称_カナ, 方書, FAX番号

## g1461（1 列）
- 見出し：名称_カナ
- 例1 値：カブシキガイシャアサヒセレモニー | カブシキガイシャセレサポート | カブシキガイシャアンシンソウサイ | カブシキガイシャタカショウ カタクリフクシソウサイ | カブシキガイシャセレモノモリ
  - 同じ表の列：名称, 方書, FAX番号

## g1462（1 列）
- 見出し：方書
- 例1 値：大南ロフティー10B
  - 同じ表の列：名称, 名称_カナ, FAX番号

## g1463（1 列）
- 見出し：FAX番号
- 例1 値：(042)-524-0447 | (042)-534-3434 | (042)-566-8727 | (042)-561-3586 | (042)-556-1077
  - 同じ表の列：名称, 名称_カナ, 方書

## g1464（1 列）
- 見出し：名称
- 例1 値：(株)多摩葬儀 | (株)奥野式典 | (株)ゆいまーる | (有)光陽祭典 | (有)まこと式典
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 方書

## g1465（1 列）
- 見出し：方書
- 例1 値：スパークルハイツ105号室 | リバーサイド大丸101 | 1-108 | ファーストヒル101 | メゾンK&M201号
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称

## g1466（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市
  - 同じ表の列：全国地方公共団体コード, ID, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻

## g1467（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g1468（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都奥多摩町 | 東京都奥多摩町 | 東京都奥多摩町 | 東京都奥多摩町 | 東京都奥多摩町
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g1469（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都御蔵島村 | 東京都御蔵島村 | 東京都御蔵島村 | 東京都御蔵島村 | 東京都御蔵島村
  - 同じ表の列：全国地方公共団体コード, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 課名称, 課名称_カナ, 係名称

## g1470（1 列）
- 見出し：組織名称
- 例1 値：総務課企画財政係 | 教育委員会事務局 | 産業課発電係 | 選挙管理委員会事務局 | 総務課民生係
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称_カナ, 局名称, 局名称_カナ, 課名称, 課名称_カナ, 係名称

## g1471（1 列）
- 見出し：組織名称_カナ
- 例1 値：キョウイクイインカイジムキョク | サンギョウカハツデンカカリ | ソウムカキカクザイセイカカリ | カイケイカンリシャカイケイカカリ | サンギョウカサンギョウケンセツカカリ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 局名称_カナ, 課名称, 課名称_カナ, 係名称

## g1472（1 列）
- 見出し：局名称
- 例1 値：農業委員会事務局 | 選挙管理委員会事務局 | 議会事務局 | 教育委員会事務局 | 監査委員会事務局
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称_カナ, 課名称, 課名称_カナ, 係名称

## g1473（1 列）
- 見出し：局名称_カナ
- 例1 値：カンサイインカイジムキョク | キョウイクイインカイジムキョク | ノウギョウイインカイジムキョク | ギカイジムキョク | センキョカンリイインカイジムキョク
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 課名称, 課名称_カナ, 係名称

## g1474（1 列）
- 見出し：課名称
- 例1 値：会計管理者 | 御蔵島診療所 | 産業課 | 総務課 | 総務課
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 課名称_カナ, 係名称

## g1475（1 列）
- 見出し：課名称_カナ
- 例1 値：カイケイカンリシャ | ソウムカ | サンギョウカ | ミクラシマシンリョウジョ | ソウムカ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 課名称, 係名称

## g1476（1 列）
- 見出し：係名称
- 例1 値：企画財政係 | 会計係 | 発電係 | 産業建設係 | 総務係
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 課名称, 課名称_カナ

## g1477（1 列）
- 見出し：係名称_カナ
- 例1 値：カイケイカカリ | ハツデンカカリ | サンギョウケンセツカカリ | ソウムカカリ | ミンセイカカリ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 課名称, 課名称_カナ

## g1478（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都八丈町 | 東京都八丈町 | 東京都八丈町 | 東京都八丈町 | 東京都八丈町
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g1479（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村
  - 同じ表の列：全国地方公共団体コード, ID, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻

## g1480（1 列）
- 見出し：VALUE *
- 例1 値：103 | 613 | 526 | 110 | 685
  - 同じ表の列：Rowid, COUNT, FOR_CATEGORY, FOR_TYPE, FOR_CODE, COVER_CODE, HT_CODE, FOREST

## g1481（1 列）
- 見出し：FOR_CATEGORY
- 例1 値：Native forest | Native forest | Native forest | Native forest | Native forest
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_TYPE, FOR_CODE, COVER_CODE, HT_CODE, FOREST

## g1482（1 列）
- 見出し：FOR_TYPE
- 例1 値：Rainforest | Mangrove | Callitris | Acacia | Mangrove
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_CATEGORY, FOR_CODE, COVER_CODE, HT_CODE, FOREST

## g1483（1 列）
- 見出し：FOR_CODE
- 例1 値：18 | 0 | 73 | 68 | 25
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_CATEGORY, FOR_TYPE, COVER_CODE, HT_CODE, FOREST

## g1484（1 列）
- 見出し：COVER_CODE
- 例1 値：2 | 5 | 3 | 1 | 1
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_CATEGORY, FOR_TYPE, FOR_CODE, HT_CODE, FOREST

## g1485（1 列）
- 見出し：HT_CODE
- 例1 値：3 | 2 | 2 | 2 | 1
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_CATEGORY, FOR_TYPE, FOR_CODE, COVER_CODE, FOREST

## g1486（1 列）
- 見出し：FOREST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Rowid, VALUE *, COUNT, FOR_CATEGORY, FOR_TYPE, FOR_CODE, COVER_CODE, HT_CODE

## g1487（1 列）
- 見出し：Pilot
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：DURINT, DATE, STOPDATE, RESULT, QD1, QD4, QPOST, QSTATE

## g1488（1 列）
- 見出し：DURINT
- 例1 値：638 | 727 | 1934 | 626 | 1089
  - 同じ表の列：Pilot, DATE, STOPDATE, RESULT, QD1, QD4, QPOST, QSTATE

## g1489（1 列）
- 見出し：STOPDATE
- 例1 値：4/25/2013 | 4/24/2013 | 4/25/2013 | 4/25/2013 | 4/25/2013
  - 同じ表の列：Pilot, DURINT, DATE, RESULT, QD1, QD4, QPOST, QSTATE

## g1490（1 列）
- 見出し：RESULT
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, QD1, QD4, QPOST, QSTATE

## g1491（1 列）
- 見出し：QD1
- 例1 値：5 | 5 | 7 | 5 | 3
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, RESULT, QD4, QPOST, QSTATE

## g1492（1 列）
- 見出し：QD4
- 例1 値：3220 | 4505 | 6061 | 3173 | 5012
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, RESULT, QD1, QPOST, QSTATE

## g1493（1 列）
- 見出し：QPOST
- 例1 値：1 | 1 | 1 | 1 | 3
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, RESULT, QD1, QD4, QSTATE

## g1494（1 列）
- 見出し：QSTATE
- 例1 値：4 | 2 | 2 | 1 | 2
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, RESULT, QD1, QD4, QPOST

## g1495（1 列）
- 見出し：QD3
- 例1 値：1 | 2 | 2 | 2 | 1
  - 同じ表の列：Pilot, DURINT, DATE, STOPDATE, RESULT, QD1, QD4, QPOST

## g1496（1 列）
- 見出し：Sex
- 例1 値：Persons | Male | Male | Male | Persons
  - 同じ表の列：Year, Type, Cancer_Type, Age_0_to_4, Age_5_to_9, Age_10_to_14, Age_15_to_19, Age_20_to_24

## g1497（1 列）
- 見出し：Cancer_Type
- 例1 値：Acute lymphoblastic leukaemia | Acute myeloid leukaemia | Acute myeloid leukaemia | Bladder cancer | Acute lymphoblastic leukaemia
  - 同じ表の列：Year, Sex, Type, Age_0_to_4, Age_5_to_9, Age_10_to_14, Age_15_to_19, Age_20_to_24

## g1498（1 列）
- 見出し：Age_0_to_4
- 例1 値：5 | 0 | 31 | 0 | 1
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_5_to_9, Age_10_to_14, Age_15_to_19, Age_20_to_24

## g1499（1 列）
- 見出し：Age_5_to_9
- 例1 値：0 | 12 | 12 | 4 | 0
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_0_to_4, Age_10_to_14, Age_15_to_19, Age_20_to_24

## g1500（1 列）
- 見出し：Age_10_to_14
- 例1 値：8 | 3 | 0 | 16 | 0
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_0_to_4, Age_5_to_9, Age_15_to_19, Age_20_to_24

## g1501（1 列）
- 見出し：Age_15_to_19
- 例1 値：4 | 0 | 7 | 1 | 1
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_0_to_4, Age_5_to_9, Age_10_to_14, Age_20_to_24

## g1502（1 列）
- 見出し：Age_20_to_24
- 例1 値：0 | 8 | 0 | 2 | 10
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_0_to_4, Age_5_to_9, Age_10_to_14, Age_15_to_19

## g1503（1 列）
- 見出し：Age_25_to_29
- 例1 値：2 | 0 | 5 | 1 | 0
  - 同じ表の列：Year, Sex, Type, Cancer_Type, Age_0_to_4, Age_5_to_9, Age_10_to_14, Age_15_to_19

## g1504（1 列）
- 見出し：Organisation
- 例1 値：Public Records Office of Victoria | Ballarat Fine Art Gallery | Geelong Gallery | The Ian Potter Centre: NGV Australia | Bendigo Art Gallery
  - 同じ表の列：Suburb/Town, Website

## g1505（1 列）
- 見出し：Suburb/Town
- 例1 値：Melbourne | Melbourne | Bendigo | Melbourne | Ballarat
  - 同じ表の列：Organisation, Website

## g1506（1 列）
- 見出し：Website
- 例1 値：http://www.bendigoartgallery.com.au/ | http://www.geelonggallery.org.au/ | http://www.acmi.net.au/ | http://www.ngv.vic.gov.au/ | http://www.ngv.vic.gov.au/
  - 同じ表の列：Organisation, Suburb/Town

## g1507（1 列）
- 見出し：Calendar_year
- 例1 値：2012 | 2012 | 2012 | 2012 | 2012
  - 同じ表の列：Calendar_quarter, Industry_division, Industry_subdivision, Organisation_ID, Financial_year_of_A…, Number_of_PPSR_regi…

## g1508（1 列）
- 見出し：Calendar_quarter
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Calendar_year, Industry_division, Industry_subdivision, Organisation_ID, Financial_year_of_A…, Number_of_PPSR_regi…

## g1509（1 列）
- 見出し：Industry_division
- 例1 値：Financial and Insurance Services | Financial and Insurance Services | Financial and Insurance Services | Information Media and Telecommunications | Financial and Insurance Services
  - 同じ表の列：Calendar_year, Calendar_quarter, Industry_subdivision, Organisation_ID, Financial_year_of_A…, Number_of_PPSR_regi…

## g1510（1 列）
- 見出し：Industry_subdivision
- 例1 値：Building Construction | Auxiliary Finance and Insurance Services | Construction Services | Finance | Finance
  - 同じ表の列：Calendar_year, Calendar_quarter, Industry_division, Organisation_ID, Financial_year_of_A…, Number_of_PPSR_regi…

## g1511（1 列）
- 見出し：Organisation_ID
- 例1 値：1652433 | 174094 | 1021312 | 789283 | 2156725
  - 同じ表の列：Calendar_year, Calendar_quarter, Industry_division, Industry_subdivision, Financial_year_of_A…, Number_of_PPSR_regi…

## g1512（1 列）
- 見出し：Financial_year_of_ABN_date_of_effect
- 例1 値：1999-00 | 2004-05 | 2002-03 | 1999-00 | 1999-00
  - 同じ表の列：Calendar_year, Calendar_quarter, Industry_division, Industry_subdivision, Organisation_ID, Number_of_PPSR_regi…

## g1513（1 列）
- 見出し：Number_of_PPSR_registrations_created
- 例1 値：1 | 4 | 1 | 1 | 1
  - 同じ表の列：Calendar_year, Calendar_quarter, Industry_division, Industry_subdivision, Organisation_ID, Financial_year_of_A…

## g1514（1 列）
- 見出し：FISHERY_ID
- 例1 値：FSQ | FSQ | FSQ | FSQ | FSQ
  - 同じ表の列：LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1515（1 列）
- 見出し：LOG_TYPE
- 例1 値：SQ03 | SQ03 | SQ03 | SQ03 | SQ03
  - 同じ表の列：FISHERY_ID, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1516（1 列）
- 見出し：BOAT_ID
- 例1 値：1331 | 1175 | 1134 | 1331 | 1091
  - 同じ表の列：FISHERY_ID, LOG_TYPE, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1517（1 列）
- 見出し：FISHING_DATE
- 例1 値：1979-11-12 00:00:00 | 1984-03-06 00:00:00 | 1984-01-12 00:00:00 | 1984-01-29 00:00:00 | 1984-02-12 00:00:00
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1518（1 列）
- 見出し：OPERATION_NO
- 例1 値：1 | 1 | 2 | 1 | 1
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, GEAR, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1519（1 列）
- 見出し：GEAR
- 例1 値：LSM | LSM | LSM | LSM | LSM
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, FISHING_START_TIME, FISHING_TIME, BOTTOM_DEPTH

## g1520（1 列）
- 見出し：FISHING_START_TIME
- 例1 値：1984-03-16 08:50:00 | 1984-03-16 09:00:00 | 1984-02-09 19:10:00 | 1984-01-24 09:00:00 | 1984-03-07 12:15:00
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_TIME, BOTTOM_DEPTH

## g1521（1 列）
- 見出し：FISHING_TIME
- 例1 値：9.75 | 11 | 6.83 | 0.02 | 9
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, BOTTOM_DEPTH

## g1522（1 列）
- 見出し：BOTTOM_DEPTH
- 例1 値：76 | 73 | 72 | 78 | 72
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME

## g1523（1 列）
- 見出し：FISHING_DEPTH
- 例1 値：70 | 70 | 70 | 70 | 80
  - 同じ表の列：FISHERY_ID, LOG_TYPE, BOAT_ID, FISHING_DATE, OPERATION_NO, GEAR, FISHING_START_TIME, FISHING_TIME

## g1524（1 列）
- 見出し：location
- 例1 値：Scholes Lagoon | Scarlet Hill | Tryworks Beach | Atlas Cove | Skua Beach
  - 同じ表の列：species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g1525（1 列）
- 見出し：species
- 例1 値：Gentoo Penguin | Antarctic Tern | ANARE | Kelp Gull | Subantarctic Skua
  - 同じ表の列：location, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g1526（1 列）
- 見出し：feature
- 例1 値：Colony | Wood in tussocks | Colony | Colony | Iron and wood
  - 同じ表の列：location, species, id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g1527（1 列）
- 見出し：comments
- 例1 値：Goldsworthy PV 3 | North Spit Colony, photographs taken fo… | Unofficial place name used by expeditio… | Stove door? Photographed | Burrows in Azorella
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day

## g1528（1 列）
- 見出し：City1
- 例1 値：MELBOURNE | ADELAIDE | BRISBANE | GOLD COAST | BRISBANE
  - 同じ表の列：City2, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs, ASKs

## g1529（1 列）
- 見出し：City2
- 例1 値：ALICE SPRINGS | PERTH | SYDNEY | MELBOURNE | SYDNEY
  - 同じ表の列：City1, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs, ASKs

## g1530（1 列）
- 見出し：Month
- 例1 値：Dec-84 | Dec-84 | May-85 | Mar-84 | Jul-84
  - 同じ表の列：City1, City2, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs, ASKs

## g1531（1 列）
- 見出し：Passenger_Trips
- 例1 値：2272 | 32201 | 1442 | 391 | 30210
  - 同じ表の列：City1, City2, Month, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs, ASKs

## g1532（1 列）
- 見出し：Aircraft_Trips
- 例1 値：4 | 310 | 206 | 1593 | 517
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs, ASKs

## g1533（1 列）
- 見出し：Passenger_Load_Factor
- 例1 値：64.3 | 81 | 69.5 | 77.3 | 40.7
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Aircraft_Trips, Distance_GC_(km), RPKs, ASKs

## g1534（1 列）
- 見出し：Distance_GC_(km)
- 例1 値：1677 | 2022 | 1622 | 895 | 476
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, RPKs, ASKs

## g1535（1 列）
- 見出し：RPKs
- 例1 値：5085452 | 66911262 | 13338948 | 10297388 | 6517196
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), ASKs

## g1536（1 列）
- 見出し：ASKs
- 例1 値：112099445 | 59167880 | 811988 | 6407281 | 3316257
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs

## g1537（1 列）
- 見出し：Seats
- 例1 値：49555 | 8863 | 1980 | 10250 | 49377
  - 同じ表の列：City1, City2, Month, Passenger_Trips, Aircraft_Trips, Passenger_Load_Fact…, Distance_GC_(km), RPKs

## g1538（1 列）
- 見出し：CouncilID
- 例1 値：12 | 21 | 19 | 13 | 11
  - 同じ表の列：Facility, Long, Lat

## g1539（1 列）
- 見出し：Facility
- 例1 値：Buninyong Community Facility | The Space | Ascot Hall | Eureka Public Hall | Kohinoor Community Centre
  - 同じ表の列：CouncilID, Long, Lat

## g1540（1 列）
- 見出し：LHR_ID
- 例1 値：LHR0053 | LHR0051 | LHR0015 | LHR0038 | LHR0001
  - 同じ表の列：LotPlan, Register_Status, Qld_Heritage_Regist…

## g1541（1 列）
- 見出し：LotPlan
- 例1 値：50WD3686 | 901SP260794 - current 901SP211911 - pre… | 226AP15896 | 0BUP106977 | 10SP156264
  - 同じ表の列：LHR_ID, Register_Status, Qld_Heritage_Regist…

## g1542（1 列）
- 見出し：Register_Status
- 例1 値：Registered | Registered | Registered | Registered | Registered
  - 同じ表の列：LHR_ID, LotPlan, Qld_Heritage_Regist…

## g1543（1 列）
- 見出し：Qld_Heritage_Register
- 例1 値：YES | NO | NO | NO | YES
  - 同じ表の列：LHR_ID, LotPlan, Register_Status

## g1544（1 列）
- 見出し：Lots
- 例1 値：Lot 558 Sec 3166 DP 38816 Hd of Munno P… | Lot 291 Sec 3167 DP 38206 Hd of Munno P… | Lot 27 Sec 311S DP 37176 Hd of Para Wir… | Lot 181 Sec 3888 DP 40643 Hd of Munno P… | Lot 163 Sec 3888 DP 37185 Hd of Munno P…
  - 同じ表の列：Suburb

## g1545（1 列）
- 見出し：object_ID
- 例1 値：5665333 | 5663020 | 5684281 | 5665172 | 5660632
  - 同じ表の列：road_type, feature_type, speed_limit, limit_type

## g1546（1 列）
- 見出し：road_type
- 例1 値：Street | Street | Street | Street | Street
  - 同じ表の列：object_ID, feature_type, speed_limit, limit_type

## g1547（1 列）
- 見出し：feature_type
- 例1 値：road | road | road | road | road
  - 同じ表の列：object_ID, road_type, speed_limit, limit_type

## g1548（1 列）
- 見出し：speed_limit
- 例1 値：40 | 40 | 40 | 40 | 40
  - 同じ表の列：object_ID, road_type, feature_type, limit_type

## g1549（1 列）
- 見出し：limit_type
- 例1 値：Maximum speed limit | Maximum speed limit | Maximum speed limit | Maximum speed limit | Maximum speed limit
  - 同じ表の列：object_ID, road_type, feature_type, speed_limit

## g1550（1 列）
- 見出し：Type
- 例1 値：Twitter followers | Disputes finalised | Letters, email and online contacts | MoneyHelp website visits | Website visits
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1551（1 列）
- 見出し：2012-13
- 例1 値：31,042 | 15,676 | 1,654,784 | 3,300 | 222,485
  - 同じ表の列：Type, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1552（1 列）
- 見出し：2013-14
- 例1 値：13,358 | 4,984 | 58,041 | 17,418 | 2,372,794
  - 同じ表の列：Type, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1553（1 列）
- 見出し：2014-15
- 例1 値：59,432 | 23,628 | 411,456 | 2,942,816 | 878,029
  - 同じ表の列：Type, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19

## g1554（1 列）
- 見出し：2015-16
- 例1 値：62,669 | 52,526 | 28,548 | 8,120 | 640,020
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19

## g1555（1 列）
- 見出し：2016-17
- 例1 値：3956932 > 3425370 | 36,555 | 72,488 | 59,525 | 565,214
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19

## g1556（1 列）
- 見出し：2017-18
- 例1 値：3,603,610 | 6,827 | 10,175 | 42,600 | 65,378
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19

## g1557（1 列）
- 見出し：2018-19
- 例1 値：10,240 | 3,675,683 | 94,206 | N/A | 6,752
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g1558（1 列）
- 見出し：Project Lead
- 例1 値：Commonwealth Scientific and Industrial … | Commonwealth Scientific and Industrial … | Commonwealth Scientific and Industrial … | Commonwealth Scientific and Industrial … | Commonwealth Scientific and Industrial …
  - 同じ表の列：Date Sampled, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## g1559（1 列）
- 見出し：Date Sampled
- 例1 値：2024-06-24 00:00:00 | 2024-10-08 00:04:00 | 2024-06-24 00:00:00 | 2024-06-24 00:00:00 | 2024-06-24 00:00:00
  - 同じ表の列：Project Lead, SiteType, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## g1560（1 列）
- 見出し：SiteType
- 例1 値：Single | Single | Multiple | Single | Single
  - 同じ表の列：Project Lead, Date Sampled, Layer, Sample Prep = fine …, Sample Location ID, Datum/ EPSG, Method of collectin…, State (eg NSW, QLD)

## 答えの雛形

```
g1441	
g1442	
g1443	
g1444	
g1445	
g1446	
g1447	
g1448	
g1449	
g1450	
g1451	
g1452	
g1453	
g1454	
g1455	
g1456	
g1457	
g1458	
g1459	
g1460	
g1461	
g1462	
g1463	
g1464	
g1465	
g1466	
g1467	
g1468	
g1469	
g1470	
g1471	
g1472	
g1473	
g1474	
g1475	
g1476	
g1477	
g1478	
g1479	
g1480	
g1481	
g1482	
g1483	
g1484	
g1485	
g1486	
g1487	
g1488	
g1489	
g1490	
g1491	
g1492	
g1493	
g1494	
g1495	
g1496	
g1497	
g1498	
g1499	
g1500	
g1501	
g1502	
g1503	
g1504	
g1505	
g1506	
g1507	
g1508	
g1509	
g1510	
g1511	
g1512	
g1513	
g1514	
g1515	
g1516	
g1517	
g1518	
g1519	
g1520	
g1521	
g1522	
g1523	
g1524	
g1525	
g1526	
g1527	
g1528	
g1529	
g1530	
g1531	
g1532	
g1533	
g1534	
g1535	
g1536	
g1537	
g1538	
g1539	
g1540	
g1541	
g1542	
g1543	
g1544	
g1545	
g1546	
g1547	
g1548	
g1549	
g1550	
g1551	
g1552	
g1553	
g1554	
g1555	
g1556	
g1557	
g1558	
g1559	
g1560	
```
