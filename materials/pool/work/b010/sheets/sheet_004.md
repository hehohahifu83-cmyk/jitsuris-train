# ラベル用シート 004 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都福生市 | 東京都福生市 | 東京都福生市 | 東京都福生市 | 東京都福生市
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚
- 例2 値：東京都福生市 | 東京都福生市 | 東京都福生市 | 東京都福生市 | 東京都福生市
  - 同じ表の列：全国地方公共団体コード, 法人番号, 名称, 名称_カナ

## g0362（1 列）
- 見出し：ゴミの分別方法_全国地方公共団体コード
- 例1 値：132195 | 132195 | 132195 | 132195 | 132195
  - 同じ表の列：ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0363（1 列）
- 見出し：ゴミの分別方法_ID
- 例1 値：132195S00021 | 132195S00055 | 132195S00212 | 132195S00131 | 132195S00198
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0364（1 列）
- 見出し：ゴミの分別方法_地方公共団体名
- 例1 値：狛江市 | 狛江市 | 狛江市 | 狛江市 | 狛江市
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0365（1 列）
- 見出し：ゴミの分別方法_品目
- 例1 値：こたつ | ごみ箱 | ストーブ 石油ストーブ(コンセント未使用 ファンヒーターなし) | ひな壇 | ストーブ パネルヒーター
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0366（1 列）
- 見出し：ゴミの分別方法_分別区分
- 例1 値：粗大ごみ | 粗大ごみ | 粗大ごみ | 粗大ごみ | 粗大ごみ
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_注意点, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0367（1 列）
- 見出し：ゴミの分別方法_注意点
- 例1 値：家庭用 | 大袋(40リットル)に9本まで折らずに入れて出してください。他の不燃ごみと一緒… | 小型電気製品(50cm未満のもの)※小型電気製品やリモコンなどに含まれる乾電池… | パソコンは不可 | 50センチメートル未満のもの
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_料金種別, ゴミの分別方法_料金

## g0368（1 列）
- 見出し：ゴミの分別方法_料金種別
- 例1 値：有料 | 有料 | 有料 | 有料 | 有料
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金

## g0369（1 列）
- 見出し：ゴミの分別方法_料金
- 例1 値：800円 | 500円 | 800円 | 300円 | 500円
  - 同じ表の列：ゴミの分別方法_全国地方公共団体コード, ゴミの分別方法_ID, ゴミの分別方法_地方公共団体名, ゴミの分別方法_品目, ゴミの分別方法_分別区分, ゴミの分別方法_注意点, ゴミの分別方法_料金種別

## g0370（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 名称_通称, 法人番号, 利用可能曜日, 開始時間, 終了時間
- 例2 値：東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g0371（1 列）
- 見出し：名称
- 例1 値：東部運動広場 | 市立テニスコート | 青少年センター | 滝山ゲートボール場 | 野外訓練施設
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 名称_通称, 法人番号, 利用可能曜日, 開始時間, 終了時間

## g0372（1 列）
- 見出し：名称_カナ
- 例1 値：ヤナギクボテニスコート | セイショウネンセンター | トウブウンドウヒロバ | タキヤマテニスコート | シリツテニスコート
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_通称, 法人番号, 利用可能曜日, 開始時間, 終了時間

## g0373（1 列）
- 見出し：名称_通称
- 例1 値：東京ドームスポーツセンター東久留米
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 法人番号, 利用可能曜日, 開始時間, 終了時間

## g0374（5 列）
- 見出し：法人番号
- 例1 値：3000020132225 | 3000020132225 | 3000020132225 | 3000020132225 | 3000020132225
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 利用可能曜日, 開始時間, 終了時間
- 例2 値：8000000000000 | 8000000000000 | 8000000000000 | 8000000000000 | 8000000000000
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 建物名等(方書)

## g0375（2 列）
- 見出し：利用可能曜日
- 例1 値：月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 法人番号, 開始時間, 終了時間
- 例2 値：月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 建物名等(方書)

## g0376（4 列）
- 見出し：開始時間
- 例1 値：07:00 | 08:00 | 07:00 | 07:00 | 10:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 法人番号, 利用可能曜日, 終了時間
- 例2 値：06:00 | 06:00 | 09:00 | 09:00 | 06:00
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 団体名, 利用可能曜日

## g0377（4 列）
- 見出し：終了時間
- 例1 値：18:00 | 21:00 | 17:00 | 18:00 | 18:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 法人番号, 利用可能曜日, 開始時間
- 例2 値：21:50 | 22:00 | 21:00 | 22:00 | 18:00
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 団体名, 利用可能曜日

## g0378（1 列）
- 見出し：利用可能時間特記事項
- 例1 値：10月~3月は8時~18時 | 10月~3月は8時~17時 | 10月~3月は8時~18時 | 10月~3月は8時~17時 | 10月~3月は8時~18時
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 法人番号, 利用可能曜日, 開始時間

## g0379（1 列）
- 見出し：市区町村名
- 例1 値：多摩市 | 多摩市 | 多摩市 | 多摩市 | 多摩市
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 名称, 名称_カナ, 運営団体名, 開催頻度, 備考

## g0380（1 列）
- 見出し：名称
- 例1 値：子ども食堂 ココっと | だれでも食堂 | 子ども食堂 ほくの家 | わくわく子ども食堂 | こども食堂 えんそく
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 市区町村名, 名称_カナ, 運営団体名, 開催頻度, 備考

## g0381（1 列）
- 見出し：名称_カナ
- 例1 値：コドモショクドウホクノイエ | アタゴダレデモショクドウ | マンマルパール | コドモショクドウココット | ワクワクコドモショクドウ
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 市区町村名, 名称, 運営団体名, 開催頻度, 備考

## g0382（1 列）
- 見出し：運営団体名
- 例1 値：こども食堂 えんそく | 特定非営利活動法人 福祉亭 | ピンクララタマ | 特定非営利活動法人 どんぐりパン | メルティング・ポット
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 市区町村名, 名称, 名称_カナ, 開催頻度, 備考

## g0383（1 列）
- 見出し：開催頻度
- 例1 値：5 | 5 | 5 | 6 | 5
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 市区町村名, 名称, 名称_カナ, 運営団体名, 備考

## g0384（1 列）
- 見出し：備考
- 例1 値：休止中(2023年12月12日時点)
  - 同じ表の列：全国地方公共団体コード, ID, 都道府県, 市区町村名, 名称, 名称_カナ, 運営団体名, 開催頻度

## g0385（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都稲城市 | 東京都稲城市 | 東京都稲城市 | 東京都稲城市 | 東京都稲城市
  - 同じ表の列：全国地方公共団体コード, ID, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻
- 例2 値：東京都稲城市 | 東京都稲城市 | 東京都稲城市 | 東京都稲城市 | 東京都稲城市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 方書

## g0386（1 列）
- 見出し：地方公共団体名
- 例1 値：羽村市 | 羽村市 | 羽村市 | 羽村市 | 羽村市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 名称_通称, 団体名, 利用可能曜日, 開始時間

## g0387（1 列）
- 見出し：名称
- 例1 値：弓道場 | S&Dスポーツアリーナ羽村(スポーツセンター) | あさひ公園 | 宮の下運動公園 | プリモパークむさしの(武蔵野公園)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_通称, 団体名, 利用可能曜日, 開始時間

## g0388（1 列）
- 見出し：名称_カナ
- 例1 値：アサヒコウエン | エスアンドディースイミングプラザハムラスイミングセンター | ミヤノシタウンドウコウエン | エスアンドディースポーツパークフジミフジミコウエン | プリモパークムサシノムサシノコウエン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_通称, 団体名, 利用可能曜日, 開始時間

## g0389（1 列）
- 見出し：名称_通称
- 例1 値：スポーツセンター | 富士見公園 | 武蔵野公園 | スイミングセンター
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 団体名, 利用可能曜日, 開始時間

## g0390（1 列）
- 見出し：団体名
- 例1 値：羽村市 | 羽村市 | 羽村市 | 羽村市 | 羽村市
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 利用可能曜日, 開始時間

## g0391（1 列）
- 見出し：利用可能曜日
- 例1 値：月火水木金土日 | 火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, 団体名, 開始時間

## g0392（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市
  - 同じ表の列：全国地方公共団体コード, 名称, トレーニング室, 陸上競技, 水泳, サッカー, スキー, テニス
- 例2 値：東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g0393（1 列）
- 見出し：名称
- 例1 値：市民公園グラウンド | 向台運動場 | 総合体育館 | ひばりが丘総合運動場「ひばりアム」 | 芝久保運動場
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, トレーニング室, 陸上競技, 水泳, サッカー, スキー, テニス

## g0394（1 列）
- 見出し：トレーニング室
- 例1 値：有 | 有
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 陸上競技, 水泳, サッカー, スキー, テニス

## g0395（1 列）
- 見出し：陸上競技
- 例1 値：無 | 無 | 無 | 無 | 無
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 水泳, サッカー, スキー, テニス

## g0396（1 列）
- 見出し：水泳
- 例1 値：無 | 無 | 無 | 無 | 無
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 陸上競技, サッカー, スキー, テニス

## g0397（1 列）
- 見出し：サッカー
- 例1 値：有 | 有 | 無 | 無 | 有
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 陸上競技, 水泳, スキー, テニス

## g0398（1 列）
- 見出し：スキー
- 例1 値：無 | 無 | 無 | 無 | 無
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 陸上競技, 水泳, サッカー, テニス

## g0399（1 列）
- 見出し：テニス
- 例1 値：無 | 無 | 無 | 無 | 無
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 陸上競技, 水泳, サッカー, スキー

## g0400（1 列）
- 見出し：ボート
- 例1 値：無 | 無 | 無 | 無 | 無
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, トレーニング室, 陸上競技, 水泳, サッカー, スキー

## g0401（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 町字ID
- 例2 値：東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町 | 東京都瑞穂町
  - 同じ表の列：全国地方公共団体コード, ID, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻

## g0402（1 列）
- 見出し：名称
- 例1 値：武蔵野コミュニティセンター図書室 | 殿ケ谷図書室 | 元狭山ふるさと思い出館図書室 | 瑞穂町図書館 | 長岡コミュニティセンター図書室
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_英字, 名称_通称, POIコード, 町字ID

## g0403（1 列）
- 見出し：名称_カナ
- 例1 値：ムサシノコミュニティセンタートショシツ | ナガオカコミュニティセンタートショシツ | モトサヤマフルサトオモイデカントショシツ | トノガヤトショシツ | ミズホマチトショカン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_英字, 名称_通称, POIコード, 町字ID

## g0404（1 列）
- 見出し：名称_英字
- 例1 値：Mizuho town library
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_通称, POIコード, 町字ID

## g0405（1 列）
- 見出し：名称_通称
- 例1 値：長岡コミュニティセンター図書室 | 殿ケ谷図書室 | 元狭山ふるさと思い出館図書室 | 武蔵野コミュニティセンター図書室 | 瑞穂町図書館
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, POIコード, 町字ID

## g0406（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都利島村 | 東京都利島村 | 東京都利島村 | 東京都利島村 | 東京都利島村
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g0407（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都新島村 | 東京都新島村 | 東京都新島村 | 東京都新島村 | 東京都新島村
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0408（1 列）
- 見出し：名称
- 例1 値：若郷体育館 | いきいき広場 | 新島スポーツ広場 | 村民プール | 式根島スポーツ広場
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0409（1 列）
- 見出し：名称_カナ
- 例1 値：シキネジマスポーツヒロバ | ソンミンプール | ワカゴウタイイクカン | イキイキヒロバ | ニイジマスポーツヒロバ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 利用可能曜日, 開始時間, 終了時間, 利用可能時間特記事項

## g0410（1 列）
- 見出し：利用可能曜日
- 例1 値：土日 | 月火水金土日 | 月火水金土日 | 月火水金土日
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 開始時間, 終了時間, 利用可能時間特記事項

## g0411（1 列）
- 見出し：利用可能時間特記事項
- 例1 値：10:00—12:00/13:00—17:00 (木曜日定休) | 土日祝のみ(GW・7/22〜8/31は毎日) 8:30〜17:00
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 利用可能曜日, 開始時間, 終了時間

## g0412（1 列）
- 見出し：説明
- 例1 値：テニスコート1面
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 利用可能曜日, 開始時間, 終了時間

## g0413（3 列）
- 見出し：ID
- 例1 値：133817GMKB000002 | 133817GMKB000004 | 133817GMKB000013 | 133817GMKB000012 | 133817GMKB000006
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 分別区分, ゴミ区分, ゴミ分類区分, 回収区分
- 例2 値：20L00015 | 2L00055 | 14L00000 | 35L00005 | 43L00065
  - 同じ表の列：lat, long, type, open_hrs, holiday

## g0414（1 列）
- 見出し：地方公共団体名
- 例1 値：三宅村 | 三宅村 | 三宅村 | 三宅村 | 三宅村
  - 同じ表の列：全国地方公共団体コード, ID, 分別区分, ゴミ区分, ゴミ分類区分, 回収区分

## g0415（1 列）
- 見出し：分別区分
- 例1 値：回収・引取はしません | 燃えるゴミ | 有害ゴミ | ペットボトル | ペットボトル
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミ区分, ゴミ分類区分, 回収区分

## g0416（1 列）
- 見出し：ゴミ区分
- 例1 値：パソコン | 乾電池 | 乾電池 | エアコン・テレビ(液晶・プラズマ含む)・冷蔵庫(H16.4.1から冷凍庫も含む… | びん
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ分類区分, 回収区分

## g0417（1 列）
- 見出し：ゴミ分類区分
- 例1 値：家電リサイクル対象 | 有害ごみ | 資源ごみ | 可燃ごみ | 家電リサイクル対象
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ区分, 回収区分

## g0418（1 列）
- 見出し：回収区分
- 例1 値：分別回収 | 分別回収 | 拠点回収 | 分別回収 | 拠点回収
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 分別区分, ゴミ区分, ゴミ分類区分

## g0419（2 列）
- 見出し：Rowid
- 例1 値：380 | 557 | 932 | 572 | 859
  - 同じ表の列：VALUE, COUNT, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_OSR, IND_EST
- 例2 値：145 | 32 | 353 | 62 | 568
  - 同じ表の列：VALUE *, COUNT, FOR_CATEGORY, FOR_TYPE, FOR_CODE, COVER_CODE, HT_CODE, FOREST

## g0420（6 列）
- 見出し：VALUE
- 例1 値：22 | 596 | 496 | 440 | 807
  - 同じ表の列：Rowid, COUNT, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_OSR, IND_EST
- 例2 値：30595 | 25 | 24415 | 3622 | 95
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02498V03025, Sex Category School, UNIT

## g0421（2 列）
- 見出し：COUNT
- 例1 値：14838 | 2417 | 1664 | 527811 | 51224
  - 同じ表の列：Rowid, VALUE, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_OSR, IND_EST
- 例2 値：82969 | 5237 | 1 | 202606 | 31891
  - 同じ表の列：Rowid, VALUE *, FOR_CATEGORY, FOR_TYPE, FOR_CODE, COVER_CODE, HT_CODE, FOREST

## g0422（12 列）
- 見出し：STATE
- 例1 値：NSW | NT | VIC | QLD | NT
  - 同じ表の列：Rowid, VALUE, COUNT, IND_OWN, IND_MNG, IND_COMNG, IND_OSR, IND_EST
- 例2 値：QLD | NSW | NSW | NSW | WA
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, Country, Charity_Size, BRC

## g0423（1 列）
- 見出し：IND_OWN
- 例1 値：0 | 1 | 0 | 1 | 1
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_MNG, IND_COMNG, IND_OSR, IND_EST

## g0424（1 列）
- 見出し：IND_MNG
- 例1 値：0 | 0 | 0 | 1 | 0
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_OWN, IND_COMNG, IND_OSR, IND_EST

## g0425（1 列）
- 見出し：IND_COMNG
- 例1 値：1 | 0 | 1 | 1 | 0
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_OWN, IND_MNG, IND_OSR, IND_EST

## g0426（1 列）
- 見出し：IND_OSR
- 例1 値：1 | 0 | 1 | 0 | 0
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_EST

## g0427（1 列）
- 見出し：IND_EST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_OSR

## g0428（1 列）
- 見出し：OVERLAP
- 例1 値：1 | 0 | 1 | 1 | 1
  - 同じ表の列：Rowid, VALUE, COUNT, STATE, IND_OWN, IND_MNG, IND_COMNG, IND_OSR

## g0429（1 列）
- 見出し：ABN
- 例1 値：12007297994 | 12165302125 | 12095876323 | 11857749742 | 11805438327
  - 同じ表の列：AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, State, Country, Charity_Size, BRC

## g0430（1 列）
- 見出し：AIS_Due_Date
- 例1 値：31/01/2016 | 30/06/2016 | 31/01/2016 | 31/01/2016 | 31/01/2016
  - 同じ表の列：ABN, Date_AIS_Received, Registration_Status, Town_City, State, Country, Charity_Size, BRC

## g0431（1 列）
- 見出し：Date_AIS_Received
- 例1 値：01/02/2016 | 30/06/2016 | 28/01/2016 | 27/03/2017 | 28/09/2016
  - 同じ表の列：ABN, AIS_Due_Date, Registration_Status, Town_City, State, Country, Charity_Size, BRC

## g0432（1 列）
- 見出し：Registration_Status
- 例1 値：Registered | Voluntarily Revoked No Longer Operating | Registered | Registered | Registered
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Town_City, State, Country, Charity_Size, BRC

## g0433（1 列）
- 見出し：Town_City
- 例1 値：HOLLAND PARK WEST | Glen Iris | Osborne Park | Melbourne | Bourke
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, State, Country, Charity_Size, BRC

## g0434（2 列）
- 見出し：Country
- 例1 値：AUSTRALIA | AUSTRALIA | AUSTRALIA | AUSTRALIA | AUSTRALIA
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, State, Charity_Size, BRC
- 例2 値：au | au | au | au | au
  - 同じ表の列：city, state, poa, year_founded, company_type, company_category, revenue_source, business_model

## g0435（1 列）
- 見出し：Charity_Size
- 例1 値：Small | Small | Medium | Small | Medium
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, State, Country, BRC

## g0436（1 列）
- 見出し：BRC
- 例1 値：n | n | n | n | y
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, State, Country, Charity_Size

## g0437（1 列）
- 見出し：CONDUCTED_ACTIVITIES
- 例1 値：y | y | y | y | y
  - 同じ表の列：ABN, AIS_Due_Date, Date_AIS_Received, Registration_Status, Town_City, State, Country, Charity_Size

## g0438（1 列）
- 見出し：Year
- 例1 値：201415 | 201314 | 201415 | 201011 | 200809
  - 同じ表の列：Country_of_origin, Time_frames, Total

## g0439（1 列）
- 見出し：Country_of_origin
- 例1 値：Philippines | Philippines | South Korea | All countries | India
  - 同じ表の列：Year, Time_frames, Total

## g0440（1 列）
- 見出し：Time_frames
- 例1 値：Time to file sent | Time to approval | Time to approval | Time to placement | Time to file sent
  - 同じ表の列：Year, Country_of_origin, Total

## g0441（6 列）
- 見出し：Total
- 例1 値：32 | 3 | 17 | 34 | 2
  - 同じ表の列：Year, Country_of_origin, Time_frames
- 例2 値：1 | 43 | 80 | 53 | 2
  - 同じ表の列：Age, Sex

## g0442（1 列）
- 見出し：Suburb/Town
- 例1 値：Ballarat | North Melbourne | Bendigo | Fitzroy | Melbourne
  - 同じ表の列：Website

## g0443（1 列）
- 見出し：Website
- 例1 値：http://www.offthekerb.com.au/ | http://www.looponline.com.au/ | http://www.geelongotway.org/ | http://platformartistsgroup.blogspot.co… | http://www.hellgallery.blogspot.com/
  - 同じ表の列：Suburb/Town

## g0444（1 列）
- 見出し：Quarter end date
- 例1 値：31-Mar-08 | 31-Dec-07 | 30-Jun-09 | 30-Sep-08 | 31-Dec-09
  - 同じ表の列：ASGS code, Number of people no…, Number of people in…, Total number of peo…

## g0445（1 列）
- 見出し：ASGS code
- 例1 値：10104 | 11903 | 10502 | 10502 | 10802
  - 同じ表の列：Quarter end date, Number of people no…, Number of people in…, Total number of peo…

## g0446（1 列）
- 見出し：Number of people not in business or not stated
- 例1 値：11 | 37 | 41 | 54 | 18
  - 同じ表の列：Quarter end date, ASGS code, Number of people in…, Total number of peo…

## g0447（1 列）
- 見出し：Number of people in business
- 例1 値：9 | 24 | 7 | 9 | 7
  - 同じ表の列：Quarter end date, ASGS code, Number of people no…, Total number of peo…

## g0448（1 列）
- 見出し：Total number of people
- 例1 値：82 | 18 | 151 | 108 | 37
  - 同じ表の列：Quarter end date, ASGS code, Number of people no…, Number of people in…

## g0449（1 列）
- 見出し：FISHERY
- 例1 値：CSF | CSF | CSF | CSF | CSF
  - 同じ表の列：GEAR, YEAR, CAAB, RETAINED_CATCH_KG, DATA_SOURCE

## g0450（1 列）
- 見出し：GEAR
- 例1 値：Trawl | Pots and traps | Hooks | Hooks | Hooks
  - 同じ表の列：FISHERY, YEAR, CAAB, RETAINED_CATCH_KG, DATA_SOURCE

## g0451（22 列）
- 見出し：YEAR
- 例1 値：2014 | 2009 | 2012 | 2005 | 2012
  - 同じ表の列：FISHERY, GEAR, CAAB, RETAINED_CATCH_KG, DATA_SOURCE
- 例2 値：2013 | 2011 | 2000 | 2001 | 2004
  - 同じ表の列：Q8, Q17aiv, Q20, Q20dii, Q22, Q28, Q24, Q26a

## g0452（1 列）
- 見出し：CAAB
- 例1 値：37346032 | 37337025 | 37346029 | 37346001 | 37017008
  - 同じ表の列：FISHERY, GEAR, YEAR, RETAINED_CATCH_KG, DATA_SOURCE

## g0453（1 列）
- 見出し：RETAINED_CATCH_KG
- 例1 値：454 | 57 | 60 | 32 | 129
  - 同じ表の列：FISHERY, GEAR, YEAR, CAAB, DATA_SOURCE

## g0454（1 列）
- 見出し：DATA_SOURCE
- 例1 値：Logbook | Logbook | Logbook | Logbook | Logbook
  - 同じ表の列：FISHERY, GEAR, YEAR, CAAB, RETAINED_CATCH_KG

## g0455（1 列）
- 見出し：location
- 例1 値：Dovers Moraine | Scarlet Hill | Paddick Valley | Capsize Beach | Stephenson Lagoon moraine
  - 同じ表の列：species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0456（1 列）
- 見出し：species
- 例1 値：South Georgian Diving Petrel | Antarctic Prion | South Georgian Diving Petrel | Rockhopper Penguin | South Georgian Diving Petrel
  - 同じ表の列：location, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0457（2 列）
- 見出し：id
- 例1 値：point_178 | polygon_8 | point_69 | polygon_16 | point_340
  - 同じ表の列：location, species, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments
- 例2 値：point_240 | polygon_8 | point_345 | point_424 | line_1
  - 同じ表の列：location, species, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0458（1 列）
- 見出し：feature
- 例1 値：Nest | Timber with iron | Spit Bay camp bounds | Nests | Nests
  - 同じ表の列：location, species, id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0459（2 列）
- 見出し：observation_date
- 例1 値：2004-01-06 | 2004-01-06 | 2004-01-06 | 2004-01-04 | 2004-01-07
  - 同じ表の列：location, species, id, feature, observation_date_ye…, observation_date_mo…, observation_date_day, comments
- 例2 値：2003-12-26 | 2004-01-13 | 2004-02-09 | 2003-12-29 | 2003-12-29
  - 同じ表の列：location, species, id, feature, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0460（2 列）
- 見出し：observation_date_year
- 例1 値：2003 | 2004 | 2004 | 2004 | 2004
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_mo…, observation_date_day, comments
- 例2 値：2003 | 2004 | 2004 | 2004 | 2004
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_mo…, observation_date_day, comments

## g0461（2 列）
- 見出し：observation_date_month
- 例1 値：12 | 12 | 1 | 12 | 1
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_day, comments
- 例2 値：12 | 1 | 1 | 2 | 2
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_day, comments

## g0462（2 列）
- 見出し：observation_date_day
- 例1 値：22 | 22 | 9 | 4 | 6
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, comments
- 例2 値：6 | 6 | 29 | 1 | 29
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, comments

## g0463（1 列）
- 見出し：comments
- 例1 値：Colony 4E | M&L 31;iron and associated debris. Phot… | Goldsworthy Skua 2 | Goldsworthy PV 3 | Goldsworthy N Spit 4
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day

## g0464（2 列）
- 見出し：data_type
- 例1 値：point | polygon | point | point | point
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day
- 例2 値：point | point | point | polygon | point
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day

## g0465（2 列）
- 見出し：Question
- 例1 値：12 | 15 | 24 | 6 | 2
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：20 | 4 | 29 | 1 | 28
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0466（2 列）
- 見出し：Question_Text
- 例1 値：Medicare should offer basic dental care… | There should be more restrictions on 45… | The national budget deficit should be r… | Private health insurance rebates should… | How much should the federal government …
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：How accessible should abortion services… | Boats carrying asylum seekers should be… | How much financial support should the C… | How much government regulation should t… | How much should the federal government …
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0467（2 列）
- 見出し：category1_definition_1
- 例1 値：Strongly disagree | Strongly disagree | Many fewer | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly disagree | Strongly disagree | Strongly disagree | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0468（2 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0469（2 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | Neutral | Neutral | About the same as now
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：About the same as now | Neutral | Neutral | Neutral | About the same as now
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0470（2 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat agree | Somewhat agree | Somewhat agree | Somewhat more | Somewhat more
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat agree | Somewhat more | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0471（2 列）
- 見出し：category1_definition_5
- 例1 値：Strongly agree | Strongly agree | Much more | Many more | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Much more | Much more | Much more | Strongly agree | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0472（2 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0473（1 列）
- 見出し：vehicle_type
- 例1 値：Passenger vehicles | Passenger vehicles | Passenger vehicles | Passenger vehicles | Passenger vehicles
  - 同じ表の列：state_abb, year_of_manufacture, no_vehicles

## g0474（1 列）
- 見出し：state_abb
- 例1 値：WA | Qld | Qld | WA | SA
  - 同じ表の列：vehicle_type, year_of_manufacture, no_vehicles

## g0475（1 列）
- 見出し：year_of_manufacture
- 例1 値：1989 | 2003 | 1996 | 1977 | 1982
  - 同じ表の列：vehicle_type, state_abb, no_vehicles

## g0476（1 列）
- 見出し：no_vehicles
- 例1 値：151 | 0 | 139 | 93 | 917
  - 同じ表の列：vehicle_type, state_abb, year_of_manufacture

## g0477（1 列）
- 見出し：SAPOBJECTID
- 例1 値：000000008000128600 | 000000008000131372 | 000000008000131195 | 000000008000017221 | 000000008000128300
  - 同じ表の列：CLASS, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0478（1 列）
- 見出し：CLASS
- 例1 値：KERB_CHANNEL | KERB_CHANNEL | KERB_CHANNEL | KERB_CHANNEL | KERB_CHANNEL
  - 同じ表の列：SAPOBJECTID, GIS_USER_STATUS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0479（1 列）
- 見出し：GIS_USER_STATUS
- 例1 値：INSV | INSV | INSV | INSV | INSV
  - 同じ表の列：SAPOBJECTID, CLASS, OBJECT_TYPE, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## g0480（1 列）
- 見出し：OBJECT_TYPE
- 例1 値：KRBC | KRBC | KRBC | KRBC | KRBC
  - 同じ表の列：SAPOBJECTID, CLASS, GIS_USER_STATUS, GIS_SYSTEM_STATUS, ROAD_EDGE_TYPE, LENGTH_M, GIS_ACQUISITION_MET…, GIS_STARTUP_DATE

## 答えの雛形

```
g0361	
g0362	
g0363	
g0364	
g0365	
g0366	
g0367	
g0368	
g0369	
g0370	
g0371	
g0372	
g0373	
g0374	
g0375	
g0376	
g0377	
g0378	
g0379	
g0380	
g0381	
g0382	
g0383	
g0384	
g0385	
g0386	
g0387	
g0388	
g0389	
g0390	
g0391	
g0392	
g0393	
g0394	
g0395	
g0396	
g0397	
g0398	
g0399	
g0400	
g0401	
g0402	
g0403	
g0404	
g0405	
g0406	
g0407	
g0408	
g0409	
g0410	
g0411	
g0412	
g0413	
g0414	
g0415	
g0416	
g0417	
g0418	
g0419	
g0420	
g0421	
g0422	
g0423	
g0424	
g0425	
g0426	
g0427	
g0428	
g0429	
g0430	
g0431	
g0432	
g0433	
g0434	
g0435	
g0436	
g0437	
g0438	
g0439	
g0440	
g0441	
g0442	
g0443	
g0444	
g0445	
g0446	
g0447	
g0448	
g0449	
g0450	
g0451	
g0452	
g0453	
g0454	
g0455	
g0456	
g0457	
g0458	
g0459	
g0460	
g0461	
g0462	
g0463	
g0464	
g0465	
g0466	
g0467	
g0468	
g0469	
g0470	
g0471	
g0472	
g0473	
g0474	
g0475	
g0476	
g0477	
g0478	
g0479	
g0480	
```
