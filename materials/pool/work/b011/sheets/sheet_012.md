# ラベル用シート 012 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_012.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1321（1 列）
- 見出し：媒体
- 例1 値：X(旧twitter) | Youtube | Instagram | Facebook | Instagram
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 公式アカウント名, 運用所属名, 説明

## g1322（1 列）
- 見出し：公式アカウント名
- 例1 値：東大和市 | umaee_official | 東大和市(@higashiyamato18) | 東大和市 | 東大和市公式動画チャンネル
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 運用所属名, 説明

## g1323（1 列）
- 見出し：運用所属名
- 例1 値：広報プロモーション課 | 広報プロモーション課 | 広報プロモーション課 | 広報プロモーション課 | 広報プロモーション課
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 公式アカウント名, 説明

## g1324（1 列）
- 見出し：説明
- 例1 値：季節の話題や観光・イベントの情報等を配信しています。 | 季節の話題や観光・イベントの情報等を配信しています。 | 市観光キャラクターの「うまべぇ」のアカウントです。市の情報を発信しています。 | 「北多摩のいい人、いい場所、いい暮らし」を配信しています。 | 映像を通して市の情報を分かりやすく配信しています。
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 公式アカウント名, 運用所属名

## g1325（1 列）
- 見出し：地方公共団体名
- 例1 値：東久留米市 | 東久留米市 | 東久留米市 | 東久留米市 | 東久留米市
  - 同じ表の列：全国地方公共団体コード, ID, 分別区分, ゴミ区分, ゴミ分類区分, 回収区分, 指定ゴミ袋

## g1326（1 列）
- 見出し：分別区分
- 例1 値：有害ごみ | 紙類・布類 | 紙類・布類 | びん・缶 | 紙類・布類
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミ区分, ゴミ分類区分, 回収区分, 指定ゴミ袋

## g1327（1 列）
- 見出し：ゴミ区分
- 例1 値：段ボール | 缶 | 剪定枝木 | 水銀体温計 | 衣類・古布
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ分類区分, 回収区分, 指定ゴミ袋

## g1328（1 列）
- 見出し：ゴミ分類区分
- 例1 値：有害ごみ | 資源ごみ | 資源ごみ | 資源ごみ | 資源ごみ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ区分, 回収区分, 指定ゴミ袋

## g1329（1 列）
- 見出し：指定ゴミ袋
- 例1 値：指定収集袋(黄色) | 指定収集袋(透明) | 指定収集袋(青色)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ区分, ゴミ分類区分, 回収区分

## g1330（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都多摩市 | 東京都多摩市 | 東京都多摩市 | 東京都多摩市 | 東京都多摩市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 号数, 発行年月, 発行元, 町字ID

## g1331（1 列）
- 見出し：名称
- 例1 値：たま市議会だより令和5年2月5日号 | たま市議会だより令和4年8月5日号 | たま市議会だより令和4年5月5日号 | たま市議会だより令和4年11月5日号 | たま市議会だより令和5年8月5日号
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 号数, 発行年月, 発行元, 町字ID

## g1332（1 列）
- 見出し：発行元
- 例1 値：多摩市議会 | 多摩市議会 | 多摩市議会 | 多摩市議会 | 多摩市議会
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 号数, 発行年月, 町字ID

## g1333（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都あきる野市 | 東京都あきる野市 | 東京都あきる野市 | 東京都あきる野市 | 東京都あきる野市
  - 同じ表の列：全国地方公共団体コード, 名称, 都道府県, 市区町村

## g1334（1 列）
- 見出し：名称
- 例1 値：松山町内会 | 草花住宅自治会 | 下引田町内会 | 緑の里自治会 | 前田自治会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 都道府県, 市区町村

## g1335（1 列）
- 見出し：市区町村
- 例1 値：あきる野市 | あきる野市 | あきる野市 | あきる野市 | あきる野市
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 都道府県

## g1336（1 列）
- 見出し：市区町村名
- 例1 値：西東京市 | 西東京市 | 西東京市 | 西東京市 | 西東京市
  - 同じ表の列：全国地方公共団体コード, 都道府県, 名称, 名称_カナ, 方書, 運営団体名, 開催頻度, 開催曜日

## g1337（1 列）
- 見出し：名称
- 例1 値：SOMPO流の子ども食堂(そんぽの家S西東京泉町) | 飯もり山 | SOMPO流の子ども食堂(そんぽの家S保谷駅前) | 子ども食堂「ゆいな」 | わいわいクッキング
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称_カナ, 方書, 運営団体名, 開催頻度, 開催曜日

## g1338（1 列）
- 見出し：名称_カナ
- 例1 値：ホウカゴキッチン・ゴロゴロ | ソンポリュウノコドモショクドウソンポノイエエスムサシノ | ソンポリュウノコドモショクドウソンポノイエエスホウヤキタマチ | ワイワイクッキング | ソンポリュウノコドモショクドウソンポノイエヤギサワ
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称, 方書, 運営団体名, 開催頻度, 開催曜日

## g1339（1 列）
- 見出し：方書
- 例1 値：芝久保サロンしゃくなげ | メトロウェストビルディング1階 | 緑町3丁目アパート集会所 | 田無公民館 | 仙人の家
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称, 名称_カナ, 運営団体名, 開催頻度, 開催曜日

## g1340（1 列）
- 見出し：運営団体名
- 例1 値：東京聖新会 | 医療法人社団欅会 看護小規模多機能ゆいなの森 | SOMPOケア株式会社 そんぽの家 | 医療法人徳洲会 武蔵野徳洲会病院 | プネウマ つどいの家
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称, 名称_カナ, 方書, 開催頻度, 開催曜日

## g1341（1 列）
- 見出し：開催曜日
- 例1 値：日 | 土 | 日 | 土 | 土
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称, 名称_カナ, 方書, 運営団体名, 開催頻度

## g1342（1 列）
- 見出し：開催日
- 例1 値：毎月12日 | 第4土曜日 | 第4金曜日 | 第3土曜日 | 第4土曜日
  - 同じ表の列：全国地方公共団体コード, 都道府県, 市区町村名, 名称, 名称_カナ, 方書, 運営団体名, 開催頻度

## g1343（1 列）
- 見出し：ゴミ区分
- 例1 値：金属類 | 紙パック | びん | ペットボトル | 乾電池
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミ分類区分, 回収区分

## g1344（1 列）
- 見出し：ゴミ分類区分
- 例1 値：有害ごみ | 資源ごみ | 不燃ごみ | 資源ごみ | 資源ごみ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミ区分, 回収区分

## g1345（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都利島村 | 東京都利島村 | 東京都利島村 | 東京都利島村 | 東京都利島村
  - 同じ表の列：全国地方公共団体コード, 樹種名称, 指定状態

## g1346（1 列）
- 見出し：樹種名称
- 例1 値：シイ | クロマツ | カエデ | ビャクシン | ハチジョウモクセイ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 指定状態

## g1347（1 列）
- 見出し：指定状態
- 例1 値：指定 | 指定 | 指定 | 指定 | 指定
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 樹種名称

## g1348（1 列）
- 見出し：区市町村名
- 例1 値：調布市 | 葛飾区 | 荒川区 | 足立区 | 八丈町
  - 同じ表の列：担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1349（1 列）
- 見出し：担当部署名
- 例1 値：企画財政課 企画情報係 | 地域協働課 | 地域振興部地域活動課協働推進係 | 政策推進課 振興企画係 | 地域支えあい推進室地域活動推進分野地域活動推進担当
  - 同じ表の列：区市町村名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1350（1 列）
- 見出し：情報提供(1)HPの設置
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1351（1 列）
- 見出し：情報提供(2)情報誌の発行
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1352（1 列）
- 見出し：情報提供(3)その他の媒体での情報提供
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1353（1 列）
- 見出し：制度(4)条例・指針・計画等の策定
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(5)支援センターの設置, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1354（1 列）
- 見出し：制度(5)支援センターの設置
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(6)相談窓口の設置, 制度(7)協働の理解・普及啓発制度

## g1355（1 列）
- 見出し：制度(6)相談窓口の設置
- 例1 値：○ | ○ | △ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(7)協働の理解・普及啓発制度

## g1356（1 列）
- 見出し：制度(7)協働の理解・普及啓発制度
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置

## g1357（1 列）
- 見出し：提案制度団体から行政への協働事業提案制度
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：区市町村名, 担当部署名, 情報提供(1)HPの設置, 情報提供(2)情報誌の発行, 情報提供(3)その他の媒体での情報提供, 制度(4)条例・指針・計画等の策定, 制度(5)支援センターの設置, 制度(6)相談窓口の設置

## g1358（1 列）
- 見出し：Trade
- 例1 値：Indonesia | Malaysia | China | Germany | Malaysia
  - 同じ表の列：unit, 2011–12, 2012–13, 2013–14, 2014–15, 2015–16, 2016–17

## g1359（1 列）
- 見出し：unit
- 例1 値：$m | $m | $m | $m | $m
  - 同じ表の列：Trade, 2011–12, 2012–13, 2013–14, 2014–15, 2015–16, 2016–17

## g1360（1 列）
- 見出し：2011–12
- 例1 値：297.51299999999997680788510479032993316… | 112.10699999999999931787897367030382156… | 534.75199999999995270627550780773162841… | 147.66100000000000136424205265939235687… | 305.04800000000000181898940354585647583…
  - 同じ表の列：Trade, unit, 2012–13, 2013–14, 2014–15, 2015–16, 2016–17

## g1361（1 列）
- 見出し：2012–13
- 例1 値：269.656 | 134.977 | 16.477 | 68.259 | 226.899
  - 同じ表の列：Trade, unit, 2011–12, 2013–14, 2014–15, 2015–16, 2016–17

## g1362（1 列）
- 見出し：2013–14
- 例1 値：10.306 | 291.676 | 220.726 | 1110.137 | 541.896
  - 同じ表の列：Trade, unit, 2011–12, 2012–13, 2014–15, 2015–16, 2016–17

## g1363（1 列）
- 見出し：2014–15
- 例1 値：1320.751 | 269.512 | 360.821 | 297.294 | 646.425
  - 同じ表の列：Trade, unit, 2011–12, 2012–13, 2013–14, 2015–16, 2016–17

## g1364（1 列）
- 見出し：2015–16
- 例1 値：444.255 | 306.048 | 347.332 | 71.087 | 1342.405
  - 同じ表の列：Trade, unit, 2011–12, 2012–13, 2013–14, 2014–15, 2016–17

## g1365（1 列）
- 見出し：2016–17
- 例1 値：145.688 | 88.645 | 117.946 | 1619.633 | 354.784
  - 同じ表の列：Trade, unit, 2011–12, 2012–13, 2013–14, 2014–15, 2015–16

## g1366（1 列）
- 見出し：Destinations
- 例1 値：Ship Stores | New Zealand | Mauritius | Total Middle East | Netherlands
  - 同じ表の列：Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1367（1 列）
- 見出し：Chilled Beef & Veal CS
- 例1 値：1.3085999999999998 | 1.60972 | 16.5436 | 34.33428 | 14.4486
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1368（1 列）
- 見出し：Chilled Beef & Veal B-In
- 例1 値：0.88627 | 0.5411 | 64.57675 | 7.94347 | 64.4773
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1369（1 列）
- 見出し：Chilled Beef & Veal B-Out
- 例1 値：8.47736 | 18339.727546 | 31.298009999999998 | 190.60006 | 2550.579476
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1370（1 列）
- 見出し：Chilled Beef & Veal Total
- 例1 値：15.73397 | 1753.32666 | 1.2589 | 359.46316999999993 | 133.85651
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1371（1 列）
- 見出し：Frozen Beef (exc bull ) CS
- 例1 値：951.01278 | 19.3178 | 931.6949799999999 | 951.01278
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1372（1 列）
- 見出し：Frozen Beef (exc bull ) B-In
- 例1 値：0.34082 | 0.82234 | 21.56098 | 20.805040000000005 | 1.16958
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1373（1 列）
- 見出し：Frozen Beef (exc bull ) B-Out
- 例1 値：130.69894 | 13.57067 | 33.4948 | 166.6554 | 1219.40459
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen BullB-Out

## g1374（1 列）
- 見出し：Frozen BullB-Out
- 例1 値：48.8512 | 18.4144 | 0.9833 | 905.40927 | 571.03483
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…

## g1375（1 列）
- 見出し：Frozen Veal CS
- 例1 値：327.92141 | 0.9321 | 17.2441 | 24.8123 | 75.3969
  - 同じ表の列：Destinations, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Chilled Beef & Veal…, Frozen Beef (exc bu…, Frozen Beef (exc bu…, Frozen Beef (exc bu…

## g1376（1 列）
- 見出し：Establishment ID
- 例1 値：1186S2020 | 210302130 | 1181H2100 | 210102160 | 210201571
  - 同じ表の列：State, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…, 2012-13 Peer Group …

## g1377（1 列）
- 見出し：Medicare Provider No.
- 例1 値：0010940F | 0011370T | 0030530L | 0011740F | 0071100H
  - 同じ表の列：State, Establishment ID, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…, 2012-13 Peer Group …

## g1378（1 列）
- 見出し：Local Hospital Network identifier
- 例1 値：604 | 215 | 202 | 314 | 112
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…, 2012-13 Peer Group …

## g1379（1 列）
- 見出し：Local Hospital Network
- 例1 値：Cairns and Hinterland | Murrumbidgee | Murrumbidgee | Country Health SA | Northern Sydney
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…, 2012-13 Peer Group …

## g1380（1 列）
- 見出し：asgc_ra
- 例1 値：1 | 2 | 2 | 0 | 3
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, Remoteness area, Number of available…, 2012-13 Peer Group …

## g1381（1 列）
- 見出し：Remoteness area
- 例1 値：Outer Regional | Major Cities | Inner Regional | Very remote | Outer Regional
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Number of available…, 2012-13 Peer Group …

## g1382（1 列）
- 見出し：Number of available beds
- 例1 値：285.7 | 0 | 62.3 | 10 | 36
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Remoteness area, 2012-13 Peer Group …

## g1383（1 列）
- 見出し：2012-13 Peer Group code
- 例1 値：Ps | VS | L | S2 | S1
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…

## g1384（1 列）
- 見出し：Provided data for NPHED
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：State, Establishment ID, Medicare Provider N…, Local Hospital Netw…, Local Hospital Netw…, asgc_ra, Remoteness area, Number of available…

## g1385（1 列）
- 見出し：2018-2019
- 例1 値：89.2% | 83.9%
  - 同じ表の列：2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1386（1 列）
- 見出し：2017-2018 (2)
- 例1 値：81.8% | 87.2%
  - 同じ表の列：2018-2019, 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1387（1 列）
- 見出し：2016-2017 (1)
- 例1 値：83.7% | 78.3%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1388（1 列）
- 見出し：2015-2016
- 例1 値：75.2% | 80.5%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2014-2015, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1389（1 列）
- 見出し：2014-2015
- 例1 値：79.9% | 74.3%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2013-2014, 2012-2013, 2011-2012, 2010-2011

## g1390（1 列）
- 見出し：2013-2014
- 例1 値：73.7% | 78.5%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2012-2013, 2011-2012, 2010-2011

## g1391（1 列）
- 見出し：2012-2013
- 例1 値：73.0% | 78.1%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2011-2012, 2010-2011

## g1392（1 列）
- 見出し：2011-2012
- 例1 値：79.8% | 74.8%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2010-2011

## g1393（1 列）
- 見出し：2010-2011
- 例1 値：77.2% | 82.8%
  - 同じ表の列：2018-2019, 2017-2018 (2), 2016-2017 (1), 2015-2016, 2014-2015, 2013-2014, 2012-2013, 2011-2012

## g1394（1 列）
- 見出し：Quarter
- 例1 値：Jun-20 | Jun-18 | Sep-19 | Mar-18 | Dec-19
  - 同じ表の列：Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1395（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): NSW
- 例1 値：1255 | 1064 | 1123 | 517 | 870
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1396（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): ACT
- 例1 値：22 | 37 | 41 | 36 | 39
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1397（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): Vic
- 例1 値：676 | 344 | 649 | 746 | 621
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1398（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): Qld
- 例1 値：1178 | 1165 | 928 | 683 | 1299
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1399（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): SA
- 例1 値：297 | 272 | 245 | 271 | 268
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1400（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): NT
- 例1 値：39 | 37 | 40 | 49 | 14
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1401（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): WA
- 例1 値：473 | 516 | 480 | 300 | 568
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1402（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): Tas
- 例1 値：31 | 106 | 77 | 109 | 95
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1403（1 列）
- 見出し：Number of bankruptcies (Parts IV and XI): Other
- 例1 値：20 | 31 | 34 | 29 | 20
  - 同じ表の列：Quarter, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…, Number of bankruptc…

## g1404（1 列）
- 見出し：BN_STATUS
- 例1 値：Registered | Registered | Registered | Registered | Registered
  - 同じ表の列：BN_REG_DT, BN_CANCEL_DT, BN_STATE_NUM, BN_STATE_OF_REG, BN_ABN

## g1405（1 列）
- 見出し：BN_REG_DT
- 例1 値：02/10/2019 | 04/01/2024 | 21/03/2025 | 01/08/2022 | 25/08/2020
  - 同じ表の列：BN_STATUS, BN_CANCEL_DT, BN_STATE_NUM, BN_STATE_OF_REG, BN_ABN

## g1406（1 列）
- 見出し：BN_CANCEL_DT
- 例1 値：18/12/2025 | 06/08/2026 | 11/03/2026 | 14/01/2026 | 23/07/2026
  - 同じ表の列：BN_STATUS, BN_REG_DT, BN_STATE_NUM, BN_STATE_OF_REG, BN_ABN

## g1407（1 列）
- 見出し：BN_STATE_NUM
- 例1 値：B1613068W | BN98077656 | BN05324610 | BN98583878 | B2162273B
  - 同じ表の列：BN_STATUS, BN_REG_DT, BN_CANCEL_DT, BN_STATE_OF_REG, BN_ABN

## g1408（1 列）
- 見出し：BN_STATE_OF_REG
- 例1 値：NSW | VIC | VIC | VIC | VIC
  - 同じ表の列：BN_STATUS, BN_REG_DT, BN_CANCEL_DT, BN_STATE_NUM, BN_ABN

## g1409（1 列）
- 見出し：BN_ABN
- 例1 値：56325267343 | 42625759444 | 82670937363 | 32136857531 | 42641160395
  - 同じ表の列：BN_STATUS, BN_REG_DT, BN_CANCEL_DT, BN_STATE_NUM, BN_STATE_OF_REG

## g1410（1 列）
- 見出し：lake_id
- 例1 値：LH49 | LH32 | LH16 | LH30 | LH70
  - 同じ表の列：location, altitude, lake_area, catchment_area, maximum_depth, dimensions, distance_from_polar…, geology

## g1411（1 列）
- 見出し：altitude
- 例1 値：85 | 5 | 60 | 20 | 25
  - 同じ表の列：lake_id, location, lake_area, catchment_area, maximum_depth, dimensions, distance_from_polar…, geology

## g1412（1 列）
- 見出し：lake_area
- 例1 値：2 | 0.5 | 3 | 12 | 2.5
  - 同じ表の列：lake_id, location, altitude, catchment_area, maximum_depth, dimensions, distance_from_polar…, geology

## g1413（1 列）
- 見出し：catchment_area
- 例1 値：43 | 6.4 | 9.1 | 2.2 | 21.2
  - 同じ表の列：lake_id, location, altitude, lake_area, maximum_depth, dimensions, distance_from_polar…, geology

## g1414（1 列）
- 見出し：maximum_depth
- 例1 値：7.7 | 6.3 | 2.5 | 4.0 | 1.5
  - 同じ表の列：lake_id, location, altitude, lake_area, catchment_area, dimensions, distance_from_polar…, geology

## g1415（1 列）
- 見出し：dimensions
- 例1 値：120x60 | 90x45 | 240x165 | 305x76 | 195x90
  - 同じ表の列：lake_id, location, altitude, lake_area, catchment_area, maximum_depth, distance_from_polar…, geology

## g1416（1 列）
- 見出し：distance_from_polar_plateau
- 例1 値：7671 | 2181 | 5063 | 1342 | 1998
  - 同じ表の列：lake_id, location, altitude, lake_area, catchment_area, maximum_depth, dimensions, geology

## g1417（1 列）
- 見出し：geology
- 例1 値：Grey gneiss | Layered gneiss, Blue gneiss | Grey gneiss | Layered gneiss | Um, Opx gneiss
  - 同じ表の列：lake_id, location, altitude, lake_area, catchment_area, maximum_depth, dimensions, distance_from_polar…

## g1418（1 列）
- 見出し：water_temperature
- 例1 値：6.6 | 7.9 | 7.2 | 7.2 | 6.9
  - 同じ表の列：lake_id, location, altitude, lake_area, catchment_area, maximum_depth, dimensions, distance_from_polar…

## g1419（1 列）
- 見出し：Question_Text
- 例1 値：Terminally ill patients should be able … | The government should further restrict … | Asylum seekers who arrive by boat shoul… | The Commonwealth should pass laws requi… | Medicare should offer basic dental care…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g1420（1 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | About the same as now | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g1421（1 列）
- 見出し：AustralianPort
- 例1 値：Sydney | Brisbane | Sydney | Melbourne | Sydney
  - 同じ表の列：Month, ForeignPort, Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g1422（1 列）
- 見出し：ForeignPort
- 例1 値：Singapore | Suva | Tokyo | Port Moresby | Port Moresby
  - 同じ表の列：Month, AustralianPort, Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g1423（1 列）
- 見出し：Country
- 例1 値：USA | Bahrain | Indonesia | Fiji | Indonesia
  - 同じ表の列：Month, AustralianPort, ForeignPort, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g1424（1 列）
- 見出し：Freight_In_(tonnes)
- 例1 値：0 | 49.416 | 0.015 | 2.39 | 25.542
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Passengers_In, Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g1425（1 列）
- 見出し：Mail_Out_(tonnes)
- 例1 値：0.221 | 0 | 0 | 3.152 | 0.359
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out

## g1426（1 列）
- 見出し：Area in Square Metres
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Function/Category, ID, Management Status, Site Code, lat, long

## g1427（1 列）
- 見出し：Function/Category
- 例1 値：Recreation Parkland | Recreation Parkland | Not Applicable | Not Applicable | Conservation Parkland
  - 同じ表の列：Area in Square Metr…, ID, Management Status, Site Code, lat, long

## g1428（1 列）
- 見出し：Management Status
- 例1 値：Not Applicable | Not Applicable | Council / Advisory Comm | Other Managers | Council
  - 同じ表の列：Area in Square Metr…, Function/Category, ID, Site Code, lat, long

## g1429（1 列）
- 見出し：Site Code
- 例1 値：P0338 | P0210 | P0895 | P0040 | P0760
  - 同じ表の列：Area in Square Metr…, Function/Category, ID, Management Status, lat, long

## g1430（1 列）
- 見出し：LOTPLAN
- 例1 値：167SP134014 | 164SP218011 | 166WD4549 | 166SP218011 | 166SP134014
  - 同じ表の列：SUBURB, FACILITY, DAY_OF_SER, SERVICEDAY

## g1431（1 列）
- 見出し：FACILITY
- 例1 値：REC | REC | REC | REC | REC
  - 同じ表の列：LOTPLAN, SUBURB, DAY_OF_SER, SERVICEDAY

## g1432（1 列）
- 見出し：DAY_OF_SER
- 例1 値：4 | 5 | 12 | 10 | 8
  - 同じ表の列：LOTPLAN, SUBURB, FACILITY, SERVICEDAY

## g1433（1 列）
- 見出し：SERVICEDAY
- 例1 値：,F | F, | ,T | F, | ,F
  - 同じ表の列：LOTPLAN, SUBURB, FACILITY, DAY_OF_SER

## g1434（1 列）
- 見出し：type
- 例1 値：SPL2 | SPL2 | SPL2 | MEDV | SPL1
  - 同じ表の列：ref, desc, long

## g1435（1 列）
- 見出し：desc
- 例1 値：ON STREET CARPARK INDENTATION | BRICK SPLITTER ISLAND | CONC SPLITTER ISLAND | CONC SPLITTER ISLAND | NULL
  - 同じ表の列：type, ref, long

## g1436（1 列）
- 見出し：type
- 例1 値：Primary | Primary | Primary | Pri/Sec | Primary
  - 同じ表の列：lat, lon, sector, suburb, ref

## g1437（1 列）
- 見出し：sector
- 例1 値：Government | Catholic | Government | Government | Government
  - 同じ表の列：lat, lon, type, suburb, ref

## g1438（1 列）
- 見出し：Community
- 例1 値：Eastern Stirling Range Montane Heath an… | Natural Grasslands of the Murray Valley… | Tasmanian Forests and Woodlands dominat… | Gippsland Red Gum (Eucalyptus tereticor… | Turpentine-Ironbark Forest of the Sydne…
  - 同じ表の列：EPBC Status, ID, ACT, NSW, NT, QLD, SA, TAS

## g1439（1 列）
- 見出し：EPBC Status
- 例1 値：Endangered | Endangered | Endangered | Critically Endangered | Endangered
  - 同じ表の列：Community, ID, ACT, NSW, NT, QLD, SA, TAS

## g1440（1 列）
- 見出し：ACT
- 例1 値：- | - | Yes | - | -
  - 同じ表の列：Community, EPBC Status, ID, NSW, NT, QLD, SA, TAS

## 答えの雛形

```
g1321	
g1322	
g1323	
g1324	
g1325	
g1326	
g1327	
g1328	
g1329	
g1330	
g1331	
g1332	
g1333	
g1334	
g1335	
g1336	
g1337	
g1338	
g1339	
g1340	
g1341	
g1342	
g1343	
g1344	
g1345	
g1346	
g1347	
g1348	
g1349	
g1350	
g1351	
g1352	
g1353	
g1354	
g1355	
g1356	
g1357	
g1358	
g1359	
g1360	
g1361	
g1362	
g1363	
g1364	
g1365	
g1366	
g1367	
g1368	
g1369	
g1370	
g1371	
g1372	
g1373	
g1374	
g1375	
g1376	
g1377	
g1378	
g1379	
g1380	
g1381	
g1382	
g1383	
g1384	
g1385	
g1386	
g1387	
g1388	
g1389	
g1390	
g1391	
g1392	
g1393	
g1394	
g1395	
g1396	
g1397	
g1398	
g1399	
g1400	
g1401	
g1402	
g1403	
g1404	
g1405	
g1406	
g1407	
g1408	
g1409	
g1410	
g1411	
g1412	
g1413	
g1414	
g1415	
g1416	
g1417	
g1418	
g1419	
g1420	
g1421	
g1422	
g1423	
g1424	
g1425	
g1426	
g1427	
g1428	
g1429	
g1430	
g1431	
g1432	
g1433	
g1434	
g1435	
g1436	
g1437	
g1438	
g1439	
g1440	
```
