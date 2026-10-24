# ラベル用シート 008 / 019

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_008.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0841（1 列）
- 見出し：普及率(人口)(%)
- 例1 値：100 | 100 | 100 | 100 | 100
  - 同じ表の列：地方公共団体コード, 年度, 日数, 行政区域推計人口(人), 行政区域推計世帯(世帯), 給水戸数(戸), メーター設置個数(個), 受水量(m3)

## g0842（1 列）
- 見出し：メーター設置個数(個)
- 例1 値：111207 | 111334 | 107308 | 109364 | 108423
  - 同じ表の列：地方公共団体コード, 年度, 日数, 行政区域推計人口(人), 行政区域推計世帯(世帯), 給水戸数(戸), 普及率(人口)(%), 受水量(m3)

## g0843（1 列）
- 見出し：受水量(m3)
- 例1 値：38524399 | 37634498 | 36449023 | 36839552 | 37579021
  - 同じ表の列：地方公共団体コード, 年度, 日数, 行政区域推計人口(人), 行政区域推計世帯(世帯), 給水戸数(戸), 普及率(人口)(%), メーター設置個数(個)

## g0844（1 列）
- 見出し：総量_配水量(m3)
- 例1 値：37579021 | 36839552 | 37634498 | 38524399 | 37372357
  - 同じ表の列：地方公共団体コード, 年度, 日数, 行政区域推計人口(人), 行政区域推計世帯(世帯), 給水戸数(戸), 普及率(人口)(%), メーター設置個数(個)

## g0845（7 列）
- 見出し：年
- 例1 値：2021 | 2020 | 2023 | 2024 | 2022
  - 同じ表の列：月, 図書館名, 総数, 0 総記, 1 哲学, 2 歴史, 3 社会, 4 自然
- 例2 値：2022 | 2023 | 2022 | 2022 | 2022
  - 同じ表の列：全国地方公共団体コード, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚, 出生

## g0846（7 列）
- 見出し：月
- 例1 値：11 | 9 | 12 | 3 | 11
  - 同じ表の列：年, 図書館名, 総数, 0 総記, 1 哲学, 2 歴史, 3 社会, 4 自然
- 例2 値：4 | 9 | 6 | 5 | 2
  - 同じ表の列：全国地方公共団体コード, 年, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚, 出生

## g0847（1 列）
- 見出し：図書館名
- 例1 値：中央 | 若狭 | 若狭 | 牧志 | 若狭
  - 同じ表の列：年, 月, 総数, 0 総記, 1 哲学, 2 歴史, 3 社会, 4 自然

## g0848（1 列）
- 見出し：総数
- 例1 値：15920 | 15730 | 6055 | 10809 | 12995
  - 同じ表の列：年, 月, 図書館名, 0 総記, 1 哲学, 2 歴史, 3 社会, 4 自然

## g0849（1 列）
- 見出し：0 総記
- 例1 値：226 | 51 | 54 | 126 | 59
  - 同じ表の列：年, 月, 図書館名, 総数, 1 哲学, 2 歴史, 3 社会, 4 自然

## g0850（1 列）
- 見出し：1 哲学
- 例1 値：489 | 570 | 509 | 490 | 502
  - 同じ表の列：年, 月, 図書館名, 総数, 0 総記, 2 歴史, 3 社会, 4 自然

## g0851（1 列）
- 見出し：2 歴史
- 例1 値：93 | 144 | 149 | 45 | 164
  - 同じ表の列：年, 月, 図書館名, 総数, 0 総記, 1 哲学, 3 社会, 4 自然

## g0852（1 列）
- 見出し：3 社会
- 例1 値：675 | 440 | 736 | 100 | 495
  - 同じ表の列：年, 月, 図書館名, 総数, 0 総記, 1 哲学, 2 歴史, 4 自然

## g0853（1 列）
- 見出し：4 自然
- 例1 値：402 | 635 | 129 | 170 | 428
  - 同じ表の列：年, 月, 図書館名, 総数, 0 総記, 1 哲学, 2 歴史, 3 社会

## g0854（1 列）
- 見出し：5 工学
- 例1 値：145 | 395 | 309 | 264 | 830
  - 同じ表の列：年, 月, 図書館名, 総数, 0 総記, 1 哲学, 2 歴史, 3 社会

## g0855（1 列）
- 見出し：都道府県
- 例1 値：沖縄県 | 沖縄県 | 沖縄県 | 沖縄県 | 沖縄県
  - 同じ表の列：地方公共団体コード, 市町村, 年月日, 年度, 項目, 名目, 節, 区分

## g0856（1 列）
- 見出し：市町村
- 例1 値：沖縄市 | 沖縄市 | 沖縄市 | 沖縄市 | 沖縄市
  - 同じ表の列：地方公共団体コード, 都道府県, 年月日, 年度, 項目, 名目, 節, 区分

## g0857（1 列）
- 見出し：年月日
- 例1 値：2023-04-01 | 2023-04-01 | 2023-04-01 | 2023-04-01 | 2023-04-01
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年度, 項目, 名目, 節, 区分

## g0858（1 列）
- 見出し：項目
- 例1 値：消防費 | 消防費 | 消防費 | 消防費 | 消防費
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年月日, 年度, 名目, 節, 区分

## g0859（1 列）
- 見出し：名目
- 例1 値：非常備消防費 | 消防施設費 | 消防施設費 | 消防施設費 | 常備消防費
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年月日, 年度, 項目, 節, 区分

## g0860（1 列）
- 見出し：節
- 例1 値：2 | 15 | 17 | 22 | 26
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年月日, 年度, 項目, 名目, 区分

## g0861（1 列）
- 見出し：区分
- 例1 値：補償、補填及び賠償金 | 公有財産購入費 | 交際費 | 負担金補助及び交付金 | 補償、補填及び賠償金
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年月日, 年度, 項目, 名目, 節

## g0862（1 列）
- 見出し：予算額(千円)
- 例1 値：33655 | 2359 | 699 | 125 | 162316
  - 同じ表の列：地方公共団体コード, 都道府県, 市町村, 年月日, 年度, 項目, 名目, 節

## g0863（1 列）
- 見出し：小地域
- 例1 値：うるま市石川赤崎 | うるま市与那城上原 | うるま市石川赤崎1丁目 | うるま市与那城西原 | うるま市石川公園等
  - 同じ表の列：KEY_CODE, 人口総数, 男, 女, 世帯総数

## g0864（1 列）
- 見出し：市区町村名
- 例1 値：大宜味村 | 大宜味村 | 大宜味村 | 大宜味村 | 大宜味村
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 名称, 名称_カナ, 設置位置, 法人番号, 団体名

## g0865（1 列）
- 見出し：名称
- 例1 値：大宜味小学校中学校 | 平南川ター滝駐車場 | 大宜味村役場 | 大宜味村診療所 | 大宜味村社会福祉協議会
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称_カナ, 設置位置, 法人番号, 団体名

## g0866（1 列）
- 見出し：名称_カナ
- 例1 値：オオギミソンシンリョウショ | オオギミソンシャカイフクシキョウギカイ | ヘナンカワタータキチュウシャジョウ | オオギミショウガッコウチュウガッコウ | オオギミソンヤクバ
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 設置位置, 法人番号, 団体名

## g0867（1 列）
- 見出し：設置位置
- 例1 値：住民福祉課前 | 職員室及び体育館玄関 | 事務所棚 | レジ横 | 診察室棚
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 名称_カナ, 法人番号, 団体名

## g0868（1 列）
- 見出し：団体名
- 例1 値：大宜味村 | (株)ファーマーズフォレスト | 大宜味村社会福祉協議会 | 大宜味村 | 大宜味村
  - 同じ表の列：都道府県コード又は市区町村コード, NO, 都道府県名, 市区町村名, 名称, 名称_カナ, 設置位置, 法人番号

## g0869（1 列）
- 見出し：小地域
- 例1 値：国頭郡大宜味村字津波 | 国頭郡大宜味村字江洲 | 国頭郡大宜味村字宮城 | 国頭郡大宜味村字喜如嘉 | 国頭郡大宜味村字根路銘
  - 同じ表の列：KEY_CODE, 人口総数, 男, 女, 世帯総数

## g0870（2 列）
- 見出し：地方公共団体名
- 例1 値：南風原町 | 南風原町 | 南風原町 | 南風原町 | 南風原町
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 町字ID
- 例2 値：南風原町 | 南風原町 | 南風原町 | 南風原町 | 南風原町
  - 同じ表の列：全国地方公共団体コード, ID, 種別, 町字ID, 建物名等(方書), 口径

## g0871（1 列）
- 見出し：名称
- 例1 値：南風原町立南風原幼稚園 | 南風原町立兼城児童館 | 山川体育センター | 南風原町立本部児童館 | 南風原町立図書館
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_英字, 名称_通称, POIコード, 町字ID

## g0872（1 列）
- 見出し：名称_カナ
- 例1 値：ハエバルチョウリツハエバルショウガッコウ | ハエバルカンコウアンナイジョ | ハエバルチョウリツキタオカジドウカン | ハエバルチョウリツキョウドウフクシシセツ | ハエバルチョウリツカネグスクジドウカン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_英字, 名称_通称, POIコード, 町字ID

## g0873（1 列）
- 見出し：名称_英字
- 例1 値：Haebaru Town Teruya Rural Community Cen… | Haebaru Town Kitaoka Kindergarten | Haebaru Town Kitaoka Kindergarten | Haebaru Town Tsukazan Elementary School | Haebaru City Haebaru Elementary School
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, POIコード, 町字ID

## g0874（1 列）
- 見出し：名称_通称
- 例1 値：本部児童館 | 給食センター | 南星中学校 | 町民広場 | 共同福祉施設
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, POIコード, 町字ID

## g0875（1 列）
- 見出し：小地域
- 例1 値：島尻郡南風原町字兼城 | 島尻郡南風原町字宮平 | 島尻郡南風原町字新川 | 島尻郡南風原町字山川 | 島尻郡南風原町字喜屋武
  - 同じ表の列：KEY_CODE, 人口総数, 男, 女, 世帯総数

## g0876（1 列）
- 見出し：RECORD TYPE
- 例1 値：D | D | D | D | D
  - 同じ表の列：PURCHASE ORDER NUMB…, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER, COST CENTER, INPUT BY, PURCHASING AGENT

## g0877（1 列）
- 見出し：PURCHASE ORDER NUMBER
- 例1 値：PO090853 | PO100024 | PO100049 | PO091982 | PO101002
  - 同じ表の列：RECORD TYPE, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER, COST CENTER, INPUT BY, PURCHASING AGENT

## g0878（1 列）
- 見出し：REQUISITION NUMBER
- 例1 値：RQ025138 | RQ017655 | RQ030048 | RQ025500 | RQ028096
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER, COST CENTER, INPUT BY, PURCHASING AGENT

## g0879（1 列）
- 見出し：INPUT DATE
- 例1 値：2013-08-07T00:00:00.000 | 2010-02-24T00:00:00.000 | 2014-07-02T00:00:00.000 | 2013-08-01T00:00:00.000 | 2013-10-01T00:00:00.000
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, REQUISITION NUMBER, TOTAL AMOUNT, DEPARTMENT NUMBER, COST CENTER, INPUT BY, PURCHASING AGENT

## g0880（1 列）
- 見出し：TOTAL AMOUNT
- 例1 値：32000 | 2105370.43 | 288361.5 | 44600 | 1209160
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, REQUISITION NUMBER, INPUT DATE, DEPARTMENT NUMBER, COST CENTER, INPUT BY, PURCHASING AGENT

## g0881（1 列）
- 見出し：DEPARTMENT NUMBER
- 例1 値：75 | 75 | 52 | 72 | 72
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, COST CENTER, INPUT BY, PURCHASING AGENT

## g0882（1 列）
- 見出し：COST CENTER
- 例1 値：7578 | 5453 | 5320 | 7577 | 7577
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER, INPUT BY, PURCHASING AGENT

## g0883（1 列）
- 見出し：PO TYPE CODE
- 例1 値：B | B | S | B | B
  - 同じ表の列：RECORD TYPE, PURCHASE ORDER NUMB…, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER, COST CENTER, INPUT BY

## g0884（1 列）
- 見出し：WEBSITE
- 例1 値：data.brla.gov | data.brla.gov | www.brla.gov | www.brla.gov | www.brla.gov
  - 同じ表の列：YEAR, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)

## g0885（5 列）
- 見出し：YEAR
- 例1 値：2025 | 2025 | 2025 | 2025 | 2025
  - 同じ表の列：WEBSITE, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)
- 例2 値：2011 | 2011 | 2011 | 2011 | 2011
  - 同じ表の列：LocationAbbr, LocationDesc, Class, Topic, Question, DataSource, Response, Data_Value_Unit

## g0886（1 列）
- 見出し：PAGE PATH
- 例1 値：/headstatt | /994/privacy | /367/juvenile-services | /government/school/xj7z-n8pj | /816/brbacs-metro-health-education
  - 同じ表の列：WEBSITE, YEAR, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)

## g0887（1 列）
- 見出し：PAGE VIEWS
- 例1 値：4355 | 58 | 2021 | 270 | 88
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)

## g0888（1 列）
- 見出し：UNIQUE VIEWS
- 例1 値：100 | 56 | 939 | 43 | 99291
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, PAGE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)

## g0889（1 列）
- 見出し：AVERAGE TIME ON PAGE (SECONDS)
- 例1 値：21.6725 | 2.7379 | 44.3484 | 0.25 | 13.0716
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, ENTRANCES, BOUNCE RATE (%), EXIT RATE (%)

## g0890（1 列）
- 見出し：ENTRANCES
- 例1 値：0.00000000000000000000 | 0.00000000000000000000 | 0.00000000000000000000 | 329 | 42
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, BOUNCE RATE (%), EXIT RATE (%)

## g0891（1 列）
- 見出し：BOUNCE RATE (%)
- 例1 値：0.1531 | 1 | 0 | 0.3906 | 0.1136
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, EXIT RATE (%)

## g0892（1 列）
- 見出し：EXIT RATE (%)
- 例1 値：0.3322 | 0.4541 | 1 | 0.5832 | 0
  - 同じ表の列：WEBSITE, YEAR, PAGE PATH, PAGE VIEWS, UNIQUE VIEWS, AVERAGE TIME ON PAG…, ENTRANCES, BOUNCE RATE (%)

## g0893（1 列）
- 見出し：LocationAbbr
- 例1 値：PRAMS Total | PRAMS Total | PRAMS Total | PRAMS Total | PRAMS Total
  - 同じ表の列：Year, LocationDesc, Class, Topic, Question, DataSource, Response, Data_Value_Unit

## g0894（1 列）
- 見出し：LocationDesc
- 例1 値：PRAMS Total | PRAMS Total | PRAMS Total | PRAMS Total | PRAMS Total
  - 同じ表の列：Year, LocationAbbr, Class, Topic, Question, DataSource, Response, Data_Value_Unit

## g0895（1 列）
- 見出し：Class
- 例1 値：Insurance/Medicaid/Services | Insurance/Medicaid/Services | Insurance/Medicaid/Services | Insurance/Medicaid/Services | Insurance/Medicaid/Services
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Topic, Question, DataSource, Response, Data_Value_Unit

## g0896（1 列）
- 見出し：Topic
- 例1 値：Prenatal Care - Content | Insurance Coverage | Medicaid | Insurance Coverage | Prenatal Care - Content
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Question, DataSource, Response, Data_Value_Unit

## g0897（1 列）
- 見出し：Question
- 例1 値：Indicator of whether mother received Me… | During any of your prenatal care visits… | Just before you got pregnant were you o… | During any of your prenatal care visits… | Indicator of whether mother was Medicai…
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Topic, DataSource, Response, Data_Value_Unit

## g0898（1 列）
- 見出し：DataSource
- 例1 値：PRAMS | PRAMS | PRAMS | PRAMS | PRAMS
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Topic, Question, Response, Data_Value_Unit

## g0899（1 列）
- 見出し：Response
- 例1 値：Non-WIC | WIC | YES (CHECKED) | Medicaid | YES
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Topic, Question, DataSource, Data_Value_Unit

## g0900（1 列）
- 見出し：Data_Value_Unit
- 例1 値：% | % | % | % | %
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Topic, Question, DataSource, Response

## g0901（1 列）
- 見出し：Data_Value_Type
- 例1 値：Percentage | Percentage | Percentage | Percentage | Percentage
  - 同じ表の列：Year, LocationAbbr, LocationDesc, Class, Topic, Question, DataSource, Response

## g0902（1 列）
- 見出し：EVENTID
- 例1 値：K220527426 | K220528525 | K220493691 | K220539645 | K220553397
  - 同じ表の列：CREATE DATE, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0903（1 列）
- 見出し：CREATE DATE
- 例1 値：2022-07-27T00:00:00.000 | 2022-07-02T00:00:00.000 | 2022-07-09T00:00:00.000 | 2022-07-04T00:00:00.000 | 2022-07-21T00:00:00.000
  - 同じ表の列：EVENTID, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0904（1 列）
- 見出し：CREATE TIME
- 例1 値：18:11:47 PM | 19:04:08 PM | 19:38:15 PM | 20:46:07 PM | 14:55:29 PM
  - 同じ表の列：EVENTID, CREATE DATE, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0905（1 列）
- 見出し：CALL CREATION
- 例1 値：2022-07-16T15:14:00.000 | 2022-07-18T15:11:00.000 | 2022-07-15T18:13:00.000 | 2022-07-15T16:30:00.000 | 2022-07-28T17:53:00.000
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0906（1 列）
- 見出し：HOUR
- 例1 値：14 | 19 | 21 | 18 | 14
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0907（1 列）
- 見出し：DAY OF WEEK
- 例1 値：Fri | Tue | Wed | Mon | Sat
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, HOUR, EVENT TYPE, EVENT SUBTYPE, DIVISION

## g0908（1 列）
- 見出し：EVENT TYPE
- 例1 値：ACCIDENT | ACCIDENT | ACCIDENT | ACCIDENT | ACCIDENT
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT SUBTYPE, DIVISION

## g0909（1 列）
- 見出し：EVENT SUBTYPE
- 例1 値：NON-INJURY | INJURY | NON-INJURY | INJURY | INJURY
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, DIVISION

## g0910（1 列）
- 見出し：DIVISION
- 例1 値：EPD | EPD | MPD | SPD | EPD
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE

## g0911（1 列）
- 見出し：BEAT
- 例1 値：423 | 532 | 131 | 113 | 643
  - 同じ表の列：EVENTID, CREATE DATE, CREATE TIME, CALL CREATION, HOUR, DAY OF WEEK, EVENT TYPE, EVENT SUBTYPE

## g0912（3 列）
- 見出し：Fiscal Year
- 例1 値：2017 | 2003 | 2011 | 2012 | 2008
  - 同じ表の列：Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…, Residential Buildin…
- 例2 値：2026 | 2024 | 2016 | 2022 | 2018
  - 同じ表の列：Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0913（1 列）
- 見出し：Fiscal Year Text Label
- 例1 値：FY2011 | FY2012 | FY2009 | FY2003 | FY2014
  - 同じ表の列：Fiscal Year, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…, Residential Buildin…

## g0914（1 列）
- 見出し：Time Stamp
- 例1 値：2006-04-30T00:00:00.000 | 2005-04-30T00:00:00.000 | 2015-12-01T00:00:00.000 | 2017-11-01T00:00:00.000 | 2007-04-30T00:00:00.000
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…, Residential Buildin…

## g0915（1 列）
- 見出し：Population (used for per capita calculations)
- 例1 値：450666 | 457963 | 464472 | 459787 | 467253
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…, Residential Buildin…

## g0916（1 列）
- 見出し：Price Index (For Inflation Calculation)
- 例1 値：90.3411540673 | 99.531115263 | 87.3450524576 | 81.1565823513 | 98.1343417649
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Commercial Properti…, Residential Propert…, Commercial Building…, Residential Buildin…

## g0917（1 列）
- 見出し：Commercial Properties Taxable Real Property Market Value Per
- 例1 値：11148.78 | 9154.41 | 7995.86 | 11062.56 | 11120.41
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Residential Propert…, Commercial Building…, Residential Buildin…

## g0918（1 列）
- 見出し：Residential Properties Taxable Real Property Market Value Pe
- 例1 値：32963.44 | 38961.48 | 38671.71 | 30985.66 | 25941.85
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Commercial Building…, Residential Buildin…

## g0919（1 列）
- 見出し：Commercial Building Permit Valuation - Real Dollars
- 例1 値：232996625.31 | 628801954.76 | 306924937.18 | 370093889.56 | 395400542
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Residential Buildin…

## g0920（1 列）
- 見出し：Residential Building Permit Valuation - Real Dollars
- 例1 値：98689394.71 | 318278470.91 | 181685129.38 | 285575446.90 | 195073222.27
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…

## g0921（1 列）
- 見出し：Revenue - Structural Balance - General, Special Revenue, and
- 例1 値：962048000 | 970749000 | 956803000 | 989292000 | 1017958000
  - 同じ表の列：Fiscal Year, Fiscal Year Text La…, Time Stamp, Population (used fo…, Price Index (For In…, Commercial Properti…, Residential Propert…, Commercial Building…

## g0922（1 列）
- 見出し：Year
- 例1 値：FY 05-06 | FY 13-14 | FY 04-05 | FY 11-12 | FY08-09
  - 同じ表の列：Total Trash Collect…, Total Recycling Col…, Total Recycling Plu…, Row ID, Cumulative Reductio…, Date

## g0923（1 列）
- 見出し：Total Trash Collected (Tons)
- 例1 値：119864 | 95169 | 88590 | 152406 | 95003
  - 同じ表の列：Year, Total Recycling Col…, Total Recycling Plu…, Row ID, Cumulative Reductio…, Date

## g0924（1 列）
- 見出し：Total Recycling Collected (Tons)
- 例1 値：20361 | 21552 | 21632 | 19405 | 12186
  - 同じ表の列：Year, Total Trash Collect…, Total Recycling Plu…, Row ID, Cumulative Reductio…, Date

## g0925（1 列）
- 見出し：Total Recycling Plus Leaf and Brush Collected (Tons)
- 例1 値：12186 | 51313 | 39138 | 34818 | 39281
  - 同じ表の列：Year, Total Trash Collect…, Total Recycling Col…, Row ID, Cumulative Reductio…, Date

## g0926（1 列）
- 見出し：Row ID
- 例1 値：2006 | 2012 | 2004 | 2011 | 2009
  - 同じ表の列：Year, Total Trash Collect…, Total Recycling Col…, Total Recycling Plu…, Cumulative Reductio…, Date

## g0927（1 列）
- 見出し：Cumulative Reduction in Trash Tonnage Since FY03-04
- 例1 値：41.87 | 37.66 | 39.6 | 43.42 | 17.79
  - 同じ表の列：Year, Total Trash Collect…, Total Recycling Col…, Total Recycling Plu…, Row ID, Date

## g0928（1 列）
- 見出し：Date
- 例1 値：2012-04-30T00:00:00.000 | 2007-04-30T00:00:00.000 | 2009-04-30T00:00:00.000 | 2010-04-30T00:00:00.000 | 2015-04-30T00:00:00.000
  - 同じ表の列：Year, Total Trash Collect…, Total Recycling Col…, Total Recycling Plu…, Row ID, Cumulative Reductio…

## g0929（1 列）
- 見出し：Precinct
- 例1 値：SHL 32-0606 | SHL 32-0875 | M-V 05-3368 | LFP 46-0652 | M-V 05-3366
  - 同じ表の列：Race, LEG, CC, CG, CounterGroup, Party, CounterType, SumOfCount

## g0930（1 列）
- 見出し：Race
- 例1 値：Shoreline School District No. 412 Propo… | Shoreline School District No. 412 Propo… | Shoreline School District No. 412 Propo… | Shoreline School District No. 412 Propo… | Shoreline School District No. 412 Propo…
  - 同じ表の列：Precinct, LEG, CC, CG, CounterGroup, Party, CounterType, SumOfCount

## g0931（1 列）
- 見出し：LEG
- 例1 値：32 | 32 | 32 | 32 | 32
  - 同じ表の列：Precinct, Race, CC, CG, CounterGroup, Party, CounterType, SumOfCount

## g0932（1 列）
- 見出し：CC
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Precinct, Race, LEG, CG, CounterGroup, Party, CounterType, SumOfCount

## g0933（1 列）
- 見出し：CG
- 例1 値：7 | 8 | 7 | 8 | 8
  - 同じ表の列：Precinct, Race, LEG, CC, CounterGroup, Party, CounterType, SumOfCount

## g0934（1 列）
- 見出し：CounterGroup
- 例1 値：Total | Total | Total | Total | Total
  - 同じ表の列：Precinct, Race, LEG, CC, CG, Party, CounterType, SumOfCount

## g0935（1 列）
- 見出し：Party
- 例1 値：NP | NP | NP | NP | NP
  - 同じ表の列：Precinct, Race, LEG, CC, CG, CounterGroup, CounterType, SumOfCount

## g0936（1 列）
- 見出し：CounterType
- 例1 値：Registered Voters | Times Counted | Times Blank Voted | Times Over Voted | Registered Voters
  - 同じ表の列：Precinct, Race, LEG, CC, CG, CounterGroup, Party, SumOfCount

## g0937（1 列）
- 見出し：SumOfCount
- 例1 値：97 | 53 | 99 | 0 | 232
  - 同じ表の列：Precinct, Race, LEG, CC, CG, CounterGroup, Party, CounterType

## g0938（1 列）
- 見出し：School Year
- 例1 値：2016-17 | 2016-17 | 2016-17 | 2016-17 | 2016-17
  - 同じ表の列：Within District Bou…, Reported, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption, Personal Exemption

## g0939（1 列）
- 見出し：Within District Boundary
- 例1 値：AUBURN SCHOOL DISTRICT | SEATTLE PUBLIC SCHOOLS | SEATTLE PUBLIC SCHOOLS | RENTON SCHOOL DISTRICT | FEDERAL WAY SCHOOL DISTRICT
  - 同じ表の列：School Year, Reported, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption, Personal Exemption

## g0940（1 列）
- 見出し：Reported
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：School Year, Within District Bou…, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption, Personal Exemption

## g0941（1 列）
- 見出し：Grade Levels
- 例1 値：K-5 | 9-12 | PK-K | 6-8 | P-12
  - 同じ表の列：School Year, Within District Bou…, Reported, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption, Personal Exemption

## g0942（1 列）
- 見出し：Total Enrollment
- 例1 値：260 | 24 | 38 | 179 | 547
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, COMPLETE, EXEMPT, Medical Exemption, Personal Exemption

## g0943（1 列）
- 見出し：COMPLETE
- 例1 値：56.1 | 95.9 | 93.6 | 97.1 | 90.4
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, Total Enrollment, EXEMPT, Medical Exemption, Personal Exemption

## g0944（1 列）
- 見出し：EXEMPT
- 例1 値：6.0 | 11.7 | 8.6 | 0.8 | 7.5
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, Total Enrollment, COMPLETE, Medical Exemption, Personal Exemption

## g0945（1 列）
- 見出し：Medical Exemption
- 例1 値：0.6 | 1.8 | 1.2 | 0.4 | 3.5
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Personal Exemption

## g0946（1 列）
- 見出し：Personal Exemption
- 例1 値：7.1 | 5.1 | 12.8 | 4.2 | 5.3
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption

## g0947（1 列）
- 見出し：Religious Exemption
- 例1 値：0.0 | 0.0 | 0.2 | 0.4 | 0.0
  - 同じ表の列：School Year, Within District Bou…, Reported, Grade Levels, Total Enrollment, COMPLETE, EXEMPT, Medical Exemption

## g0948（1 列）
- 見出し：WBID
- 例1 値：100307.0 | 100306.0 | 100305.0 | 100309.0 | 100310.0
  - 同じ表の列：WATER_BODY

## g0949（1 列）
- 見出し：WATER_BODY
- 例1 値：Creve Coeur Creek | Dardenne Creek | Fee Fee Creek | Indian Creek | Grand Glaize Creek
  - 同じ表の列：WBID

## g0950（1 列）
- 見出し：PARK_ID
- 例1 値：67 | 13 | 41 | 75 | 75
  - 同じ表の列：DATE_DES

## g0951（1 列）
- 見出し：DATE_DES
- 例1 値：19780524 | 19810128 | 19780706 | 19780708 | 19790329
  - 同じ表の列：PARK_ID

## g0952（1 列）
- 見出し：WBID
- 例1 値：2288 | 2034 | 2080 | 3184 | 2080
  - 同じ表の列：YR, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ, UNIT

## g0953（1 列）
- 見出し：YR
- 例1 値：2014 | 2010 | 2006 | 2002 | 2008
  - 同じ表の列：WBID, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ, UNIT

## g0954（1 列）
- 見出し：BUSINESSID
- 例1 値：51548 | 60031 | 55224 | 60270 | 55224
  - 同じ表の列：WBID, YR, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ, UNIT

## g0955（1 列）
- 見出し：WATER_BODY
- 例1 値：Big R. | Big R. | Big R. | Big R. | Baynham Br.
  - 同じ表の列：WBID, YR, BUSINESSID, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ, UNIT

## g0956（1 列）
- 見出し：WB_CLS
- 例1 値：P | P | P | P | P
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, MDNR_IMPSZ, SIZE_, EPA_APPRSZ, UNIT

## g0957（1 列）
- 見出し：MDNR_IMPSZ
- 例1 値：136.7 | 47.1 | 47.1 | 136.7 | 39
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, WB_CLS, SIZE_, EPA_APPRSZ, UNIT

## g0958（1 列）
- 見出し：SIZE_
- 例1 値：81.3 | 81.3 | 81.3 | 34.1 | 4.7
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, EPA_APPRSZ, UNIT

## g0959（1 列）
- 見出し：EPA_APPRSZ
- 例1 値：136.7 | 7.7 | 34.1 | 81.3 | 136.7
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, UNIT

## g0960（1 列）
- 見出し：UNIT
- 例1 値：Mi. | Mi. | Mi. | Mi. | Mi.
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ

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
g0925	
g0926	
g0927	
g0928	
g0929	
g0930	
g0931	
g0932	
g0933	
g0934	
g0935	
g0936	
g0937	
g0938	
g0939	
g0940	
g0941	
g0942	
g0943	
g0944	
g0945	
g0946	
g0947	
g0948	
g0949	
g0950	
g0951	
g0952	
g0953	
g0954	
g0955	
g0956	
g0957	
g0958	
g0959	
g0960	
```
