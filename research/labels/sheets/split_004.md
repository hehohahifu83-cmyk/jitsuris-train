# 割れている組の見直し 004（LABEL_GUIDE v2.2）

同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。
`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。
今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。

## G091　b007「ゴミの分別方法_分別区分」（2 列：category 1・product 1）

多いほうの category の例：

- 金属類 / 金属類 / もやせるごみ / もやせるごみ / もやせないごみ / もやせるごみ / もやせるごみ / 金属類（同じ表：ゴミの分別方法_全国地方公共団体コード・ゴミの分別方法_ID・ゴミの分別方法_品目・ゴミの分別方法_料金種別・ゴミの分別方法_料金備考）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | product | 空き箱（紙製) / 油の付着したびん / 折込チラシ / カーペット / カタログ類 / 紙くず / ガムテープ / 救急ばんそうこう | ゴミの分別方法_全国地方公共団体コード・ゴミの分別方法_ID・ゴミの分別方法_品目・ゴミの分別方法_料金種別 | .tokyo.lg.jp/setagaya/131121_setagayaku_garbage_separate.csv |

## G092　b007「値」（2 列：quantity 1・category 1）

多いほうの quantity の例：

- 10015 / 12162 / 910 / 10439 / 14074 / 3978 / 5766 / 6623（同じ表：市町村コード・市などの別・都道府県・市町村・年・年齢別・性別）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | NO / 非常に満足 / 非常に満足 / 知りたい情報を見つけたが、情報が雑多で整理されておらずわかりにくかった / 知りたい情報を見つけたが、難しい表現や専門用語で書かれていてわかりにくかった / その他 / どちらかといえば満足 / どちらかといえば満足 | 項目名・データ形態・カテゴリー数・質問文・属性 | pendata.metro.tokyo.lg.jp/digitalservice/shintosei2025_1.csv |

## G093　b007「公式アカウント名」（3 列：org 2・account 1）

多いほうの org の例：

- 世田谷区広報 / 世田谷区危機管理部 / 世田谷区子ども・若者 / 世田谷保健所 / 世田谷区教育委員会事務局 / 世田谷区世田谷総合支所 / 世田谷区北沢総合支所 / 世田谷区玉川総合支所（同じ表：全国地方公共団体コード・地方公共団体名・媒体・運用所属名・説明）
- 東京都府中市 / ふちゅこま / 府中市公共施設マネジメント担当 / 府中市協働共創推進課 / リサちゃん＠府中市 / スポーツタウン府中／SPORTS TOWN FUCHU【公式】 / 府中市美術館 Fuchu Art Museum / 給食５レンジャー＆らんちーず（同じ表：全国地方公共団体コード・地方公共団体名・媒体・運用所属名・説明）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | account | 東京都 / Tokyo Gov / 東京ベイeSGプロジェクト / 東京都公文書館 / 東京都公文書館 / 東京都八丈支庁 / hachijoshicho / 東京都三宅支庁 | 全国地方公共団体コード・地方公共団体名・媒体・運用所属名・説明 | ndata.metro.tokyo.lg.jp/seisakukikaku/130001_tokyoto_sns.csv |

## G094　b007「車椅子」（4 列：quantity 3・category 1）

多いほうの quantity の例：

-  /  /  /  /  / 2 /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・間取り・建設年度・管理戸数・主な線・主な駅）
-  /  /  /  /  /  /  / （同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・面積・間取り・建設年度・管理戸数）
- 2 /  /  /  /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・面積・間取り・建設年度・管理戸数・一般）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 4 | category | なし / なし / 一部 / なし / なし / なし / なし / なし | 全国地方公共団体コード・地方公共団体名・名称・面積・建設年度・管理戸数・主な線・主な駅 | data.metro.tokyo.lg.jp/fussa/132187_fussashi_koueijutaku.csv |

## G095　b008「区分２」（2 列：account 1・category 1）

多いほうの account の例：

- 交通安全対策特別交付金 / 委託金 / 市町村からのもの / 地方債 / 授業料 / 財産売払収入 / 石油ガス譲与税 / 石油ガス譲与税（同じ表：年度・歳入区分・区分３・区分順序１・区分順序２・区分順序３・決算額（千円）・決算額（億円））

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category |  /  / 三次 / 二次 / 二次 / 二次 / 特殊 / 特殊 | 区分１・区分３・広尾病院・大塚病院・駒込病院・墨東病院・多摩総合医療センター・神経病院 | w.opendata.metro.tokyo.lg.jp/byouin/kaikaku-suishin-plan.csv |

## G096　b008「区分３」（2 列：account 1・category 1）

多いほうの account の例：

- 交通安全対策特別交付金 / 普通建設事業 / 市町村からのもの / 地方債 / その他 / その他 / 石油ガス譲与税 / 石油ガス譲与税（同じ表：年度・歳入区分・区分２・区分順序１・区分順序２・区分順序３・決算額（千円）・決算額（億円））

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | 東京都災害拠点病院（★基幹災害拠点病院、☆地域災害拠点中核病院、○地域災害拠点病院、◇災害医療支援病院） / 東京ＤＭＡＴ指定病院 / 東京都救命救急センター / 東京都救急告示医療機関 / 東京都指定二次救急医療機関（休日・全夜間診療事業実施医療機関） / 東京都地域救急医療センター（東京ルール） / 東京都熱傷救急連絡協議会加盟施設 / 精神科緊急医療機関（緊急措置入院等） | 区分１・区分２・広尾病院・大塚病院・駒込病院・墨東病院・多摩総合医療センター・神経病院 | w.opendata.metro.tokyo.lg.jp/byouin/kaikaku-suishin-plan.csv |

## G097　b008「区分」（5 列：category 4・account 1）

多いほうの category の例：

- 公共用地／教育文化施設 / 公共用地／厚生医療施設 / 公共用地／供給処理施設 / 商業用地／住商併用施設 / 商業用地／スポーツ・興行施設 / 住宅用地／独立住宅 / 工業用地／専用工場 / 工業用地／住居併用工場（同じ表：用途）
- 調査産業計 / 製造業／繊維工業・衣服製造業 / 製造業／印刷・同関連業 / 製造業／プラスチック製品製造業 / 製造業／ゴム製品・革製品・毛皮製造業 / 製造業／電子部品・電機機器・情報通信機器製造業 / 製造業／その他の製造業 / 情報通信業／計（同じ表：抽出企業数／総計・抽出企業数／10～29人・抽出企業数／30～49人・抽出企業数／50～99人・抽出企業数／100～299人・集計企業数／総計）
- 訪都外国人旅行者数／旅行者数（千人） / 訪都外国人旅行者数／対前年比(%) / 訪都国内旅行者数／旅行者数（千人） / 訪都国内旅行者数／対前年比(%) / 訪日外国人旅行者数／旅行者数（千人） / 訪日外国人旅行者数／対前年比(%) / ※2021年は新型コロナウイルス感染症への対応等の観点から調査の一部および推計を中止 / ※2022年の増減率については新型コロナウイルス感染症拡大前の2019年と比較した増減率である（同じ表：2004・2005・2006・2007・2008・2009・2010・2011）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | account | 都税総額 / 法人二税 / 固定・都市計 / 個人都民税 / 繰入地方消費税 / その他 | ２８年度決算額Ａ（億円）・２８年度補正後予算額Ｂ（億円）・２７年度決算額Ｃ（億円）・比較増減対２８年度補正後Ａ－Ｂ（億円）・比較増減対２８年度増減率（％）・比較増減対２７年度決算額Ａ－Ｃ（億円）・比較増減対２７年度増減率（％） | tps://www.tax.metro.tokyo.lg.jp/documents/d/tax/kessan_h28_1 |

## G098　b008「施設名」（4 列：org 3・address 1）

多いほうの org の例：

- 東京都江戸東京博物館 / 江戸東京たてもの園 / 江戸東京たてもの園 / 江戸東京たてもの園 / 東京都写真美術館 / 東京都写真美術館 / 東京都美術館 / 東京都美術館（同じ表：施設通し番号・施設内エレベーター通し番号・エレベーター名・左のうち車椅子に対応しているエレベーター・定員（名）・積載量（kg）・停止階・乗降ロビーに到着するかごの昇降方向を表示する装置を設けている）
- 東京体育館 / 駒沢オリンピック公園総合運動場 / 東京武道館 / 東京辰巳国際水泳場 / 有明テニスの森公園テニス施設 / 若洲海浜公園ヨット訓練所 / 東京都障害者総合スポーツセンター / 東京都多摩障害者スポーツセンター（同じ表：指定期間・総合評価・評価内容）
- 恩賜上野動物園 / 多摩動物公園 / 葛西臨海水族園 / 井の頭自然文化園 / しながわ水族館（同じ表：優待等）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | address | 淀橋給水所 / 区立両国公園 / 都立八潮高等学校 / 東海給水所 / 区立西六郷三丁目公園 / 砧浄水場 / 区立みずのとう公園 / 区立日暮里南公園 | 番号・種別・確保水量（立方メートル）・詳細画像・情報更新日・備考 | www.opendata.metro.tokyo.lg.jp/suidou/R7/kyoten_20251211.csv |

## G099　b008「名称」（46 列：address 30・org 15・text 1）

多いほうの address の例：

- 昭島つつじが丘立体 / 芝山立体 / 玉川上水立体 / 立川立体 / 松原立体 / 立川共同溝 / 美住歩行者トンネル / 美住陸橋下地下歩道（同じ表：路線名・設置個所・延長（m）・備考）
- 東京体育館 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場 / 駒沢オリンピック公園総合運動場（同じ表：設置者・アクセス方法・施設名称・施設分類・面数・面積（m2）・観覧席数・夜間照明有無）
- 総合スポーツセンター / 月島スポーツプラザ / 浜町運動場 / 月島運動場 / 豊海テニス場（同じ表：全国地方公共団体コード・地方公共団体名・団体名・陸上競技・水泳・サッカー・スキー・テニス）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | 都議会だより令和6年第1回定例会 / 都議会だより令和5年第4回定例会 / 都議会だより令和4年新年特別号 / 都議会だより令和3年第3回定例会 / 都議会だより令和2年第3回定例会 / 都議会だより平成30年第3回定例会 / 都議会だより平成30年第2回定例会 / 都議会だより平成30年新年特別号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元・町字ID | ndata.metro.tokyo.lg.jp/gikai/130001_tokyoto_gikaidayori.csv |
| 7 | org | 台東区生涯学習センタートレーニングルーム / 台東リバーサイドスポーツセンター / 東京都立浅草高等学校温水プール / たなかスポーツプラザ / 江戸川河川敷野球場 / 荒川河川敷運動公園運動場 / 清島温水プール / 柳北スポーツプラザ | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・建物名等(方書)・団体名・利用可能曜日・開始時間 | .metro.tokyo.lg.jp/taito/131067_taitoku_sportsfacilities.csv |
| 9 | org | 深川南部保健相談所 / 深川スポーツセンター / 小松橋出張所 / 亀戸文化センター / 第二亀戸中学校 / 第二亀戸幼稚園 / 亀戸図書館 / 北砂ホーム | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・高度の種別・高度の値・設置位置・法人番号 | tps://www.opendata.metro.tokyo.lg.jp/koto/131083_008_aed.csv |
| 11 | org | スポーツセンター / 代々木西原公園庭球場 / 代々木大山公園運動場 / 二子玉川区民運動施設 / 代官山スポーツプラザ / ひがし健康プラザ / 猿楽トレーニングジム / 中幡小学校温水プール | 全国地方公共団体コード・ID・地方公共団体名・開始時間・終了時間・説明・備考・トレーニング室 | ro.tokyo.lg.jp/shibuya/131130_shibuyaku_sportsfacilities.csv |
| 12 | org | 鷺宮スポーツ・コミュニティプラザ / 中部スポーツ・コミュニティプラザ / 南部スポーツ・コミュニティプラザ / 上高田運動施設（野球場、庭球場） / 哲学堂運動施設（野球場、庭球場、弓道場） / 妙正寺川公園運動広場 / 中野区立総合体育館 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_英字・POIコード・団体名・利用可能曜日 | etro.tokyo.lg.jp/nakano/131148_nakanoku_sportsfacilities.csv |
| 13 | org | 杉並区大宮前体育館 / 杉並区馬橋公園運動広場 / 杉並区上井草体育館 / 杉並区上井草運動場 / 杉並区上井草温水プール / 杉並区妙正寺体育館 / 杉並区荻窪体育館 / 杉並区高円寺体育館 | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・名称_通称・POIコード・内線番号・団体名 | .tokyo.lg.jp/suginami/131156_suginamiku_sportsfacilities.csv |
| 19 | org | 江戸川区立中央図書館 / 江戸川区立小岩図書館 / 江戸川区立松江図書館 / 江戸川区立小松川図書館 / 江戸川区立篠崎図書館 / 江戸川区立葛西図書館 / 江戸川区立西葛西図書館 / 江戸川区立東葛西図書館 | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・建物名等(方書)・高度の種別・高度の値・団体名 | ndata.metro.tokyo.lg.jp/edogawa/131237_edogawaku_library.csv |
| 21 | org | 中央図書館 / 柴崎図書館 / 上砂図書館 / 幸図書館 / 西砂図書館 / 多摩川図書館 / 高松図書館 / 錦図書館 | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・POIコード・町字ID・建物名等(方書)・利用可能曜日 | .metro.tokyo.lg.jp/tachikawa/132021_tachikawashi_library.csv |
| 26 | org | 中央図書館 / さるびあ図書館 / 鶴川図書館 / 鶴川駅前図書館 / 金森図書館 / 忠生図書館 / 木曽山崎図書館 / 堺図書館 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_英字・POIコード・建物名等(方書)・法人番号 | data.metro.tokyo.lg.jp/machida/132098_machidashi_library.csv |
| 28 | org | 中央図書館 / 高幡図書館 / 多摩平図書館 / 日野図書館 / 百草図書館 / 平山図書館 / 市政図書室 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ | w.opendata.metro.tokyo.lg.jp/hino/132128_hinoshi_library.csv |
| 29 | org | 東村山市民スポーツセンター / 東村山市運動公園野球場 / 東村山市運動公園トラック競技場 / 東村山市運動公園庭球場 / 東村山市前川公園テニスコート / 東村山市前川公園グラウンド / 東村山市健康広場 / 東村山市秋津ゲートボール場 | 全国地方公共団体コード・地方公共団体名・名称_カナ・利用可能曜日・開始時間・終了時間・利用可能時間特記事項・陸上競技 | gashimurayama/132136_higashimurayamashi_sportsfacilities.csv |
| 38 | org | 秋川体育館 / 五日市ファインプラザ / あきる野市民プール（屋内） / あきる野市民プール（屋外）（令和8年まで閉場） / いきいきセンター / 油平クラブハウス / 総合グラウンド / 玉見ヶ崎レクリエーション広場 | 全国地方公共団体コード・地方公共団体名・名称_カナ・内線番号・利用可能曜日・開始時間・終了時間・利用可能時間特記事項 | o.tokyo.lg.jp/akiruno/132284_akirunoshi_sportsfacilities.csv |
| 39 | org | 西東京市中央図書館 / 西東京市保谷駅前図書館 / 西東京市芝久保図書館 / 西東京市谷戸図書館 / 西東京市柳沢図書館 / 西東京市ひばりが丘図書館 | 全国地方公共団体コード・地方公共団体名・名称_カナ・町字ID・建物名等(方書)・団体名・利用可能曜日・開始時間 | etro.tokyo.lg.jp/nishitokyo/132292_nishitokyoshi_library.csv |
| 42 | org | つばき小学校体育館 / つばき小学校グランド / さくら小学校体育館 / さくら小学校グランド / つつじ小学校体育館 / つつじ小学校グランド / 第一中学校体育館 / 第一中学校グランド | 地方公共団体名・名称_カナ・建物名等(方書)・連絡先FormURL・団体名・利用可能曜日・開始時間・終了時間 | o.tokyo.lg.jp/oshima/133612_oshimamachi_sportsfacilities.csv |
| 44 | org | 如是保育所 / 北昭和台保育所 / 春日保育所 / 芝生保育所 / 愛光認定こども園 / 和光認定こども園 / まかみこども園(分園含む) / 日輪保育園 | 市町村コード・都道府県名・市区町村名・ID・名称カナ・種別・定員・保育開始年齢～保育終了年齢 | -bf5b-4583-8578-a5ebc82b3786/download/ninkahoikushisetsu.csv |
| 45 | org | こどもセンター / 三角子育て支援センター / 宇城市子育て支援センター「かもめ」 / 宇城市子育てひろば / 宇城市松橋子育て支援センター豊川 / 豊福保育園子育て総合支援センター / 豊野保育園子育て支援センター / 小川町子育て支援センター | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・種別・建物名等(方書)・高度の種別・高度の値 | 12-fd3b-40fb-beb6-4ad90713a47c/download/432130_preschool.csv |

## G100　b008「備考」（4 列：text 2・category 1・address 1）

多いほうの text の例：

- フィンスイミングは団体利用のみ /  /  /  /  /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・陸上競技・水泳・サッカー・スキー・テニス）
-  /  /  /  /  /  /  / （同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・開始時間・終了時間・説明・トレーニング室）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | category | 排水場、警報装置 / 排水場、警報装置 / 排水場、警報装置 / 排水場、警報装置 / 排水場、警報装置 / 排水場、警報装置 /  /  | 名称・路線名・設置個所・延長（m） | //www.opendata.metro.tokyo.lg.jp/kensetsu/R3/dourosisetu.csv |
| 2 | address | ［住所］西新宿2-10-1 / ［住所］両国4-25-3 / ［住所］東品川3-27-22 / ［住所］東海1-3-12 / ［住所］西六郷3-16-16 / ［住所］喜多見2-9-1 / ［住所］江古田1-3 / ［住所］東日暮里5-19-1 | 番号・施設名・種別・確保水量（立方メートル）・詳細画像・情報更新日 | www.opendata.metro.tokyo.lg.jp/suidou/R7/kyoten_20251211.csv |

## G101　b008「施設名称」（3 列：org 2・address 1）

多いほうの org の例：

- 美容室ステイ / Ｓｋｙｗａｒｄ（スカイワード） / ルーニア麻布十番シャルム店 / ｒｉｃａｒｉ（リカリ） / Ｌａｚ ＴＯＫＹＯ ａｚａｂｕ / Ａｒｉｅｓ 麻布十番店 / ジュエル美容室 / ｅｎｏｒｕｈａ（同じ表：施設方書・確認日・確認番号）
- かず理容所 / ヘアーサロンヤマモト / ヘアースタジアム ホームラン / ヘアースポットＫＡＪＩ / 理容サワイ / ヘアーサロン ヒカリ / ヘアースタジオ スター / 理容 みなみ（同じ表：都道府県コード又は市区町村コード・NO・都道府県名・市区町村名・法人営業者名称・確認年月日・確認番号）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | address | 陸上競技場 / 陸上競技場 / 体育館 / 第一球技場 / 第二球技場 / 補助競技場 / 軟式野球場 / 硬式野球場 | 設置者・名称・アクセス方法・施設分類・面数・面積（m2）・観覧席数・夜間照明有無 | pendata.metro.tokyo.lg.jp/sports/130001sports_facilities.csv |

## G102　b008「団体名」（18 列：address 11・org 7）

多いほうの address の例：

- 中野区 / 中野区 / 中野区 / 中野区 / 中野区 / 中野区 / 中野区（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・利用可能曜日）
- 荒川区 / 荒川区 / 荒川区 / 荒川区 / 荒川区 / 荒川区 / 荒川区 / 荒川区（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・POIコード・高度の種別・高度の値・利用可能曜日）
- 町田市 / 町田市 / 町田市 / 町田市 / 町田市 / 町田市 / 町田市 / 町田市（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・建物名等(方書)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | org | 中央区スポーツ未来創造パートナーズ / 中央区スポーツ未来創造パートナーズ / 中央区スポーツ未来創造パートナーズ / タフカ株式会社 / タフカ株式会社 | 全国地方公共団体コード・地方公共団体名・名称・陸上競技・水泳・サッカー・スキー・テニス | ta.metro.tokyo.lg.jp/chuo/131024_chuoku_sportsfacilities.csv |
| 2 | org | 台東区 / 公益財団法人台東区芸術文化財団 / 台東区 / 台東区 / 台東区 / 台東区 / ＪＮ共同事業体 / 台東区 | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・建物名等(方書)・利用可能曜日・開始時間 | .metro.tokyo.lg.jp/taito/131067_taitoku_sportsfacilities.csv |
| 4 | org | コナミスポーツ・杉並建物総合管理事業協同組合共同事業体 / 杉並区 / ＴＡＣ・ＦＣ東京・ＭＥＬＴＥＣ共同事業体 / ＴＡＣ・ＦＣ東京・ＭＥＬＴＥＣ共同事業体 / ＴＡＣ・ＦＣ東京・ＭＥＬＴＥＣ共同事業体 / ＴＡＣ・ＦＣ東京・ＭＥＬＴＥＣ共同事業体 / コナミスポーツ・杉並建物総合管理事業協同組合共同事業体 / コナミスポーツ・杉並建物総合管理事業協同組合共同事業体 | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・名称_通称・POIコード・内線番号 | .tokyo.lg.jp/suginami/131156_suginamiku_sportsfacilities.csv |
| 6 | org | 株式会社図書館流通センター / 株式会社ヴィアックス / 株式会社ヴィアックス / 株式会社ヴィアックス / 株式会社図書館流通センター / 株式会社図書館流通センター / 株式会社図書館流通センター / 株式会社図書館流通センター | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・建物名等(方書)・高度の種別・高度の値 | ndata.metro.tokyo.lg.jp/edogawa/131237_edogawaku_library.csv |
| 7 | org | 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 / 武蔵野文化生涯学習事業団 | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・開始時間・終了時間・利用可能時間特記事項 | kyo.lg.jp/musashino/132039_musashinoshi_sportsfacilities.csv |
| 8 | org | 公益財団法人三鷹市スポーツと文化財団 / 公益財団法人三鷹市スポーツと文化財団 / 三鷹市 / 三鷹市 / 公益財団法人三鷹市スポーツと文化財団 / 公益財団法人三鷹市スポーツと文化財団 / 三鷹市 / 公益財団法人三鷹市スポーツと文化財団 | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・名称_通称・POIコード | tro.tokyo.lg.jp/mitaka/132047_mitakashi_sportsfacilities.csv |
| 14 | org | 公益財団法人いなぎグリーンウェルネス財団 / 公益財団法人いなぎグリーンウェルネス財団 / 東京ヴェルディグループ / 株式会社オーエンス / 公益財団法人いなぎグリーンウェルネス財団 / 公益財団法人いなぎグリーンウェルネス財団 / 公益財団法人いなぎグリーンウェルネス財団 / 公益財団法人いなぎグリーンウェルネス財団 | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・名称_通称・POIコード | metro.tokyo.lg.jp/inagi/132250_inagishi_sportsfacilities.csv |

## G103　b008「名称_カナ」（37 列：address 23・org 14）

多いほうの address の例：

- シンジュククリツコズミックスポーツセンター / シンジュククリツシンジュクスポーツセンター / シンジュククリツオオクボスポーツプラザ / シンジュククリツヨツヤスポーツスクエア / シンジュククリツニシトヤマコウエンヤキュウジョウ / シンジュククリツオチアイチュウオウコウエンヤキュウジョウ / シンジュククリツニシオチアイコウエンショウネンヤキュウジョウ / シンジュククリツカンセンエンコウエンテイキュウジョウ（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・名称_通称・POIコード・高度の種別）
- ブンキョウソウゴウタイイクカン / ブンキョウスポーツセンター / ブンキョウエドガワバシタイイクカン / リクギコウエンウンドウジョウ / コイシカワウンドウジョウ / コウラクコウエンショウネンヤキュウジョウ / タケハヤテニスコート（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・利用可能曜日・開始時間・終了時間）
- リョウゴクオクナイプール / スミダスポーツケンコウセンター / キュウドウジョウ / タチバナタイイクカン / オクガイスポーツシセツ / ヤヒロヤキュウジョウ / スミダヤキュウジョウ / アラカワヨツギバシリョクチヤキュウジョウ（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・名称_通称・POIコード・町字ID）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | org | タイトウクショウガイガクシュウセンタートレーニングルーム / タイトウリバーサイドスポーツセンター / トウキョウトリツアサクサコウトウガッコウオンスイプール / タナカスポーツプラザ / エドガワカセンジキヤキュウジョウ / アラカワカセンジキウンドウコウエンウンドウジョウ / キヨシマオンスイプール / リュウホクスポーツプラザ | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・建物名等(方書)・団体名・利用可能曜日・開始時間 | .metro.tokyo.lg.jp/taito/131067_taitoku_sportsfacilities.csv |
| 5 | org | フカガワナンブホケンソウダンジョ / フカガワスポーツセンター / コマツバシシュッチョウジョ / カメイドブンカセンター / ダイニカメイドチュウガッコウ / ダイニカメイドヨウチエン / カメイドトショカン / キタスナホーム | 全国地方公共団体コード・ID・地方公共団体名・名称・高度の種別・高度の値・設置位置・法人番号 | tps://www.opendata.metro.tokyo.lg.jp/koto/131083_008_aed.csv |
| 6 | org | サギノミヤスポーツ・コミュニティプラザ / チュウブスポーツ・コミュニティプラザ / ナンブスポーツ・コミュニティプラザ / カミタカダウンドウシセツ / テツガクドウウンドウシセツ / ミョウショウジガワコウエンウンドウヒロバ / ナカノクリツソウゴウタイイクカン | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・POIコード・団体名・利用可能曜日 | etro.tokyo.lg.jp/nakano/131148_nakanoku_sportsfacilities.csv |
| 7 | org | スギナミクオオミヤマエタイイクカン / スギナミクマバシコウエンウンドウヒロバ / スギナミクスギナミクカミイグサタイイクカン / スギナミクカミイグサウンドウジョウ / スギナミクカミイグサオンスイプール / スギナミクミョウショウジタイイクカン / スギナミクオギクボタイイクカン / スギナミクコウエンジタイイクカン | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・名称_通称・POIコード・内線番号・団体名 | .tokyo.lg.jp/suginami/131156_suginamiku_sportsfacilities.csv |
| 11 | org | エドガワクリツチュウオウトショカン / エドガワクリツコイワトショカン / エドガワクリツマツエトショカン / エドガワクリツコマツガワトショカン / エドガワクリツシノザキトショカン / エドガワクリツカサイトショカン / エドガワクリツニシカサイトショカン / エドガワクリツヒガシカサイトショカン | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・建物名等(方書)・高度の種別・高度の値・団体名 | ndata.metro.tokyo.lg.jp/edogawa/131237_edogawaku_library.csv |
| 12 | org |  /  /  /  /  /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・名称_通称・POIコード・建物名等(方書)・高度の種別 | okyo.lg.jp/hachioji/132012_hachioujishi_sportsfacilities.csv |
| 13 | org | チュウオウトショカン / シバサキトショカン / カミスナトショカン / サイワイトショカン / ニシスナトショカン / タマガワトショカン / タカマツトショカン / ニシキトショカン | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・POIコード・町字ID・建物名等(方書)・利用可能曜日 | .metro.tokyo.lg.jp/tachikawa/132021_tachikawashi_library.csv |
| 18 | org | チュウオウトショカン / サルビアトショカン / ツルカワトショカン / ツルカワエキマエトショカン / カナモリトショカン / タダオトショカン / キソヤマザキトショカン / サカイトショカン | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・POIコード・建物名等(方書)・法人番号 | data.metro.tokyo.lg.jp/machida/132098_machidashi_library.csv |
| 20 | org | チュウオウトショカン / タカハタトショカン / タマダイラトショカン / ヒノトショカン / モグサトショカン / ヒラヤマトショカン / シセイトショシツ | 全国地方公共団体コード・ID・地方公共団体名・名称 | w.opendata.metro.tokyo.lg.jp/hino/132128_hinoshi_library.csv |
| 21 | org | ヒガシムラヤマシミンスポーツセンター / ヒガシムラヤマシウンドウコウエンヤキュウジョウ / ヒガシムラヤマシウンドウコウエントラックキョウギジョウ / ヒガシムラヤマシウンドウコウエンテイキュウジョウ / ヒガシムラヤマシマエカワコウエンテニスコート / ヒガシムラヤマシマエカワコウエングラウンド / ヒガシムラヤマシケンコウヒロバ / ヒガシムラヤマシアキツゲートボールジョウ | 全国地方公共団体コード・地方公共団体名・名称・利用可能曜日・開始時間・終了時間・利用可能時間特記事項・陸上競技 | gashimurayama/132136_higashimurayamashi_sportsfacilities.csv |
| 30 | org | アキガワタイイクカン / イツカイチファインプラザ / アキルノシミンプールオクナイ / アキルノシミンプールオクガイ / イキイキセンター / アブラダイクラブハウス / ソウゴウグラウンド / タマミガサキレクリエーションヒロバ | 全国地方公共団体コード・地方公共団体名・名称・内線番号・利用可能曜日・開始時間・終了時間・利用可能時間特記事項 | o.tokyo.lg.jp/akiruno/132284_akirunoshi_sportsfacilities.csv |
| 31 | org | ニシトウキョウシチュウオウトショカン / ニシトウキョウシホウヤエキマエトショカン / ニシトウキョウシシバクボトショカン / ニシトウキョウシヤトトショカン / ニシトウキョウシヤギサワトショカン / ニシトウキョウシヒバリガオカトショカン | 全国地方公共団体コード・地方公共団体名・名称・町字ID・建物名等(方書)・団体名・利用可能曜日・開始時間 | etro.tokyo.lg.jp/nishitokyo/132292_nishitokyoshi_library.csv |
| 34 | org | ツバキショウガッコウタイイクカン / ツバキショウガッコウグランド / サクラショウガッコウタイイクカン / サクラショウガッコウグランド / ツツジショウガッコウタイイクカン / ツツジショウガッコウグランド / ダイイチチュウガッコウタイイクカン / ダイイチチュウガッコウグランド | 地方公共団体名・名称・建物名等(方書)・連絡先FormURL・団体名・利用可能曜日・開始時間・終了時間 | o.tokyo.lg.jp/oshima/133612_oshimamachi_sportsfacilities.csv |
| 36 | org | コドモセンター / ミスミコソダテシエンセンター / ウキシコソダテシエンセンター「カモメ」 / ウキシコソダテヒロバ / ウキシマツバセコソダテシエンセンタートヨカワ / トヨフクホイクエンコソダテソウゴウシエンセンター / トヨノホイクエンコソダテシエンセンター / オガワマチコソダテシエンセンター | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・種別・建物名等(方書)・高度の種別・高度の値 | 12-fd3b-40fb-beb6-4ad90713a47c/download/432130_preschool.csv |

## G104　b008「名称_英字」（21 列：address 12・org 9）

多いほうの address の例：

- Shinjuku Cosmic Sports Center / Shinjuku Sports Center / Okubo Sports Plaza / Yotsuya Sports Square / Nishi-Toyama Park Baseball Field / Ochiai Chuo Park Baseball Field / Nishi-Ochiai Park Youth Baseball Field / Kansen-en Park Tennis Courts（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・高度の種別）
- General Gymnasium / Sports Center / Edogawabashi Gymnasium / Rikugi Park Sports Ground / Koishikawa Sports Ground / Koraku Park Junior Baseball Ground / Takehaya Tennis Courts（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・利用可能曜日・開始時間・終了時間）
- Ryogoku Indoor Pool / Sumida Sports Health Center / Kyudo Hall / Tachibana Gymnasium / Kinshi Park Baseball Ground / Yahiro Baseball Ground / Sumida Baseball Ground / Arakawa Yotsugibashi Ryokuchi Baseball Ground（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・町字ID）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | org |  / Taito riverside sports center /  /  /  /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・建物名等(方書)・団体名・利用可能曜日・開始時間 | .metro.tokyo.lg.jp/taito/131067_taitoku_sportsfacilities.csv |
| 5 | org | Saginomiya Sports and Community Plaza / Central Sports and Community Plaza / Southern Sports and Community Plaza / Kamitakada Sports Facility / Tetsugakudo Park Sports Facility / Myoshojigawa Park Athletic Field / Nakano City General Gymnasium | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・POIコード・団体名・利用可能曜日 | etro.tokyo.lg.jp/nakano/131148_nakanoku_sportsfacilities.csv |
| 6 | org | Omiyamae gymnasium / Mabashi park movement square / Kamiigusa, Suginamiku sports center / Kamiigusa, Suginamiku sports center / Kamiigusa, Suginamiku sports center / suginami city myoushoji gymnasium / Ogikubo gymnasium / Koenji gymnasium | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・内線番号・団体名 | .tokyo.lg.jp/suginami/131156_suginamiku_sportsfacilities.csv |
| 9 | org |  /  /  /  /  /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・建物名等(方書)・高度の種別 | okyo.lg.jp/hachioji/132012_hachioujishi_sportsfacilities.csv |
| 10 | org | Chuo Library / Shibasaki Library / Kamisuna Library / Saiwai Library / Nishisuna Library / Tamagawa Library / Takamatsu Library / Nishiki Library | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・POIコード・町字ID・建物名等(方書)・利用可能曜日 | .metro.tokyo.lg.jp/tachikawa/132021_tachikawashi_library.csv |
| 13 | org | Machida city library / Machida city library / Machida city library / Machida city library / Machida city library / Machida city library / Machida city library / Machida city library | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・POIコード・建物名等(方書)・法人番号 | data.metro.tokyo.lg.jp/machida/132098_machidashi_library.csv |
| 14 | org | Chuo Park Tennis Court / Tenjin Tennis Court / Jyosui Park Tennis Court / Kodaira Municipal Onuma Ground / Kodaira Municipal Tenjin Ground / Kodaira Municipal Ogawa Nishi Ground / Kodaira Municipal Hagiyama Park Ground / Kodaira Municipal Chuo Park Ground | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・POIコード・町字ID・法人番号 | tro.tokyo.lg.jp/kodaira/132110_kodairashi_sportsfacility.csv |
| 20 | org |  /  /  /  /  /  /  /  | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・内線番号・利用可能曜日・開始時間 | o.tokyo.lg.jp/mizuho/133035_mizuhomachi_sportsfacilities.csv |
| 21 | org |  / misumi child rearinng support center / uki city child rearing support center kamome / uki city child rearing support center hiroba / uki city matubase child rearing support center toyokawa / toyofuku nursery school child rearing comprehensive support / toyono nursery school child rearing support center / ogawa town child rearing support center | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・種別・建物名等(方書)・高度の種別・高度の値 | 12-fd3b-40fb-beb6-4ad90713a47c/download/432130_preschool.csv |

## G105　b008「名称_通称」（12 列：address 10・org 2）

多いほうの address の例：

- 新宿コズミックスポーツセンター / 新宿スポーツセンター / 大久保スポーツプラザ / 四谷スポーツスクエア / 西戸山公園野球場 / 落合中央公園野球場 / 西落合公園少年野球場 / 甘泉園公園庭球場（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・高度の種別）
- 両国屋内プール / すみだスポーツ健康センター / 弓道場 / 立花体育館 / 錦糸公園野球場 / 八広野球場 / 墨田野球場 / 荒川四ツ木橋緑地野球場（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・町字ID）
- 小豆沢体育館 / 赤塚体育館 / 上板橋体育館 / 植村記念加賀スポーツセンター / 高島平温水プール / 和弓場 / 洋弓場 / 浮間舟渡フットサルパーク（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・利用可能曜日・開始時間）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | org | 大宮前体育館 / 馬橋公園運動広場 / TAC杉並区上井草スポーツセンター / TAC杉並区上井草スポーツセンター / TAC杉並区上井草スポーツセンター / TAC杉並区妙正寺体育館 / 荻窪体育館 / 高円寺みんなの体育館 | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・内線番号・団体名 | .tokyo.lg.jp/suginami/131156_suginamiku_sportsfacilities.csv |
| 5 | org |  /  /  /  /  /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・建物名等(方書)・高度の種別 | okyo.lg.jp/hachioji/132012_hachioujishi_sportsfacilities.csv |

## G106　b008「建物名等(方書)」（9 列：address 8・org 1）

多いほうの address の例：

- 生涯学習センター内 /  / 都立浅草高等学校体育館棟地下１階 /  / 江戸川河川敷 / 荒川河川敷 / 社会教育センター地下1階 / （同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・団体名・利用可能曜日・開始時間）
- 富士森公園内 / 大塚公園内 / 富士森公園内 / 大塚公園内 / 松木公園内 / 内裏谷戸公園内 / 上柚木公園内 / 殿入中央公園内（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・名称_通称・POIコード・高度の種別）
- ファーレ立川センタースクエア内 /  / 都営上砂町1丁目アパート内 /  /  / 都営立川富士見町6丁目アパート内 /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・町字ID・利用可能曜日）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org |  /  /  /  / しのざき文化プラザ /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・高度の種別・高度の値・団体名 | ndata.metro.tokyo.lg.jp/edogawa/131237_edogawaku_library.csv |

## G107　b008「Time」（2 列：quantity 1・date 1）

多いほうの quantity の例：

- about 4 mins / about 6 min / about 9 min / about 24 min / about 15 min / about 7 min / about 1 min / about 1hr 20min（同じ表：Distance）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | date | Jan 1, 2021 12:00 PM / Jan 2, 2021 8:00 AM / Jan 2, 2021 1:00 PM / Jan 5, 2021 6:00 AM / Jan 9, 2021 11:00 AM / Jan 9, 2021 8:00 PM / Jan 10, 2021 7:00 AM / Jan 11, 2021 6:00 PM | Dun Laoghaire @ Peoples Park Pedestrian・Dun Laoghaire @ Peoples Park Peds IN・Dun Laoghaire @ Peoples Park Peds OUT・Dun Laoghaire @ Seapoint Beach Pedestria・Dun Laoghaire @ Seapoint Beach Peds IN・Dun Laoghaire @ Seapoint Beach Peds OUT・Dun Laoghaire @ York Road Pedestrian・Dun Laoghaire @ York Road Peds IN | e-4b97-afd8-86180ef24a9b/download/dlr_footfall_count2021.csv |

## G108　b008「Title」（5 列：text 3・org 1・address 1）

多いほうの text の例：

- Noorat Show / Kangaroobie Base Camp / Kangaroobie Klassic / Camperdown Show / Timboon parkrun / Terang RSL Morning Melodies / 2022 Noorat Show / Inner Varnika（同じ表：Start Date・End Date・Id・CreateDate・ActivateDate・DeactivateDate・Cost・Website）
- Title : "Establishing the High Court" / Title : "White Australia Policy" / Title : "Mildenhall collection" / Title : "Testing passages" / Title : "POW history sheet" / Title : "Faces of Australia" / Title : "Faces of Australia" / Title : "Faces of Australia"（同じ表：Theme・Subtheme・Tags・More Info・Year・Series・Control Symbol・Barcode）
- Premises of Balfour Wauchope / Alberga. Cattle Train / Aldgate. Wayzgoose Party / Aldinga Tennis Club / Camels, Alice Springs / Alice Springs / Jubilee Celebrations / Telegraph Station（同じ表：ID・Catalogue・XML・Publication・Topical・Image）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Bethania Transport and Main Roads Customer Service Centre / Bollon Police Station / Bundaberg Transport and Main Roads Customer Service Centre / Caboolture Transport and Main Roads Customer Service Centre / Cairns Queensland Government Service Centre / Charters Towers Transport and Main Roads Customer Service Ce / Darra Motor Vehicle Inspection Centre / Emerald Transport and Main Roads Customer Service Centre | Suburb・Mon am・Mon pm・Tues am・Tues pm・Wed am・Wed pm・Thurs am | e/81d78d4f-0cad-4145-9fe6-43526036cabf/download/30092026.csv |
| 3 | address | Bridgewater / Campbell Town / Currie / Deloraine / George Town / Glenorchy / Huonville / Launceston | Hours・Googlemap | e/b8e618b5-2ec4-46b7-a1ce-e1fafedce05f/download/stoshops.csv |

## G109　b008「State」（7 列：address 5・category 2）

多いほうの address の例：

- QLD / QLD / NSW / QLD / QLD / SA / WA / WA（同じ表：FacilityID・FacilityType・Town・Parking・ParkingAccessible・ParkingNote・KeyRequired・MLAK24）
- NSW / Victoria / Queensland / Queensland / SA / SA / SA / Tasmania（同じ表：Year・Trade type・TRIEC 1 digit・TRIEC 2 digit・TRIEC 3 digit・TRIEC 4 digit・Partner Country・Geographic level 1）
- VIC / VIC / VIC / VIC / VIC / VIC / VIC / VIC（同じ表：Suburb・Business Category・LGA・Region）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 6 | category | State / State / State / State / State / State | STATISTIC・Statistic・TLIST(A1)・Year・C02196V02652・UNIT・VALUE | pi.restful/PxStat.Data.Cube_API.ReadDataset/G0118/CSV/1.0/en |
| 7 | category | State / State / State / State / State / State / State / State | STATISTIC・Statistic・TLIST(A1)・Year・C02196V02652・UNIT・VALUE | pi.restful/PxStat.Data.Cube_API.ReadDataset/G0207/CSV/1.0/en |

## G110　b008「Contract」（2 列：text 1・category 1）

多いほうの text の例：

- LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro / LBNCo Pty Ltd has entered into a real estate development pro（同じ表：Service_Area・Service_Area_Identifier・Network_Infrastructure・Estimated_Completion_Date・Contract_Entered_Date）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Completed / Completed / Completed / Completed / Completed / Completed / Completed / Completed | id・Service_Area・Network_Infrastructure・Estimated_Completion_Date | b673-f023-4a97-86c5-f962e934d10c/download/wkt_12.01.2021.csv |

## G111　b009「Reference」（3 列：id 2・text 1）

多いほうの id の例：

- 110892 / 110978 / 111220 / 112336 / 114141 / 114427 / 114489 / 117941（同じ表：Gender・Suburb）
- 78/3198G / 78/3198J / 78/2165 / 78/3198K / 78/3198O / 78/3285 / 78/3198L / 78/3290（同じ表：ID・Location・OBJECTID・SHAPE__Length）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | Felton, 2013, p.119; NSW Office of Environment & Heritage 20 / Felton, 2013, p.124; Kabaila, PR 2011, Survival legacies: st / Felton, 2013, p.365 / Felton, 2013, pp. 146-147, 365; NSW Office of Environment & / Felton, 2013, p.365; NSW Office of Environment and Heritage / Felton, 2013, p.138; Kabaila, PR 2011, Survival legacies: st / Felton, 2013, p.156 / Felton, 2013, p.163 | AR_number・Lat・Lon・Year_gazetted_est_closure・Years_of_operation_as_mission・Parish_Maps・Type | 096cbe-e2a7-48ec-9761-c5564ece85bd/download/nsw-missions.csv |

## G112　b009「Region」（4 列：address 3・category 1）

多いほうの address の例：

- Metropolitan Sydney / North Coast / North Coast / Metropolitan Sydney / North Coast / Riverina-Murray / Metropolitan Sydney / Metropolitan Sydney（同じ表：AgencyCategory・ProjectType・Type・Location・LGA・StartYear・CompletionYear・ETC）
- Grampians / Loddon-Mallee / North and West Metropolitan Region / Eastern Metro / Hume / North and West Metropolitan Region / North and West Metropolitan Region / North and West Metropolitan Region（同じ表：Suburb・State・Business Category・LGA）
- Grampians Region / Southern Metropolitan Region / Hume Region / Loddon-Mallee Region / North and West Metropolitan Region / Loddon-Mallee Region / North and West Metropolitan Region / Barwon South Western Region（同じ表：Suburb・State・Business Category・LGA）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | category | Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Country | Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・SA2 Band・Subject to Cap | 4-862a-30e555896d1b/download/find-my-lia-band-1-sep-2021.csv |

## G113　b009「Years」（3 列：date 2・category 1）

多いほうの date の例：

- 2009-12-31 / 2010-12-31 / 2011-12-31 / 2012-12-31 / 2013-12-31 / 2014-12-31 / 2015-12-31 / 2016-12-31（同じ表：Number of attendees）
- 2014-06-30 / 2015-06-30 / 2016-06-30 / 2017-06-30 / 2018-06-30 / 2019-06-30 / 2020-06-30 / 2021-06-30（同じ表：NSW visitor expenditure in $ million）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | 7 years - maximum allowable period / 7 years - maximum allowable period / 7 years - maximum allowable period / 7 years - maximum allowable period and extended for a furthe / 7 years - maximum allowable period and extended for a furthe / 7 years - maximum allowable period / 7 years - maximum allowable period / 7 years - maximum allowable period and extended for a furthe | ProviderID・ABN・Category・Website・RegistrationStatus・RegistrationDescription・RegistrationRenewalDate・SelfAccreditation | 780b-4a70-8c87-b6796d5ab237/download/providers_16102026a.csv |

## G114　b009「Location」（6 列：address 4・other 1・category 1）

多いほうの address の例：

- Various / Ewingsdale / Coraki / Ryde / Tweed Heads / Deniliquin / Wentworth Point / Cherrybrook（同じ表：AgencyCategory・ProjectType・Type・LGA・Region・StartYear・CompletionYear・ETC）
- Brisbane - South / Brisbane - South / Ipswich / Brisbane City / Caboolture / North Queensland / Sunshine Coast / Sunshine Coast（同じ表：Title・Services・Office type・Counter type・Suburb・Fax・Mon am・Mon pm）
- Coolattin Estate, Shillelagh, County Wicklow. / Coolattin Estate, Shillelagh, County Wicklow. / Quarry Road Killincarrig, Greystones. / Coolattin Estate, Shillelagh, County Wicklow. / Coolattin Estate, Shillelagh, County Wicklow. / Coolattin Estate, Shillelagh, County Wicklow. / Coolattin Estate, Shillelagh, County Wicklow. / Coolattin Estate, Shillelagh, County Wicklow.（同じ表：ID・Reference・OBJECTID・SHAPE__Length）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | other | -32.963547,151.695653 / -32.963547,151.695653 / -32.964057,151.695091 / -32.964564,151.690618 / -32.963547,151.695653 / -32.973856,151.715786 / -32.963547,151.695653 / -32.964209,151.68868 | Time・Device ID・Temperature (°C)・Humidity (%) | bf9ed/download/council-netvox-historical-to-31-july-2020.csv |
| 4 | category | Not within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone / Within a Fire Restriction Zone | UID・Township・Requiremen・Criterion_・Criterio00・Criterio01・Document_L | 6-995b-db0fc2ae4f35/download/shrcctownfirezonesoffseason.csv |

## G115　b009「Mon pm」（2 列：text 1・date 1）

多いほうの text の例：

- 12:00-15:30 / 12:00-15:45 / 12:00-13:00 / 12:00-16:30 / 12:00-16:00 / 13:30-15:00 / 12:00-16:00 / 12:00-16:45（同じ表：Title・Location・Services・Office type・Counter type・Suburb・Fax・Mon am）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | date | 13:30-16:00 / 16:30 / 16:30 / 14:00-16:00 / 14:00-16:30 / 15:30 / 13:00 - 15:30 / 13:45-16:00 | Column・Title・Wheelchair access・Suburb・State・Fax・Notes・Mon am | 8e0f-f538-44df-bb3f-a6cccba0381f/download/website-update.csv |

## G116　b009「State」（10 列：address 8・id 1・category 1）

多いほうの address の例：

- VIC / WA / QLD / WA / VIC / NSW / VIC / VIC（同じ表：ABN・Town_City・Country・Charity_Website・Registration_Date・Date_Organisation_Established・Charity_Size・Number_of_Responsible_Persons）
- New South Wales / New South Wales / New South Wales / New South Wales / New South Wales / New South Wales / New South Wales / New South Wales（同じ表：Month・Type of personal insolvency administrati・In a business or company・Industry of Employment・Number of people entering a new personal）
- QLD / QLD / QLD / QLD / QLD / QLD / QLD / QLD（同じ表：Column・Title・Wheelchair access・Suburb・Fax・Notes・Mon am・Mon pm）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 4 | id | 1 / 1 / 1 / 1 / 1 / 1 / 1 / 1 | SA1_MAIN16・SA1_7DIG16・MMM2019 | f3b211-60a0-4515-96ba-2e72b4cd7119/download/mmm-2019-csv.zip |
| 10 | category | State / State / State / State / State / State | STATISTIC・Statistic・TLIST(A1)・Year・C02196V02652・UNIT・VALUE | pi.restful/PxStat.Data.Cube_API.ReadDataset/G0113/CSV/1.0/en |

## G117　b009「2015-16」（2 列：quantity 1・amount 1）

多いほうの quantity の例：

- 73,952 / 90,224 / 30,408 / 69,365 / 25,960 / 24,815 / 10,765 / 11,244（同じ表：Type of call・2012-13・2013-14・2014-15・2016-17・2017-18・2018-19）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 902108652 / 654082398 / 653263304 / 749422251 / 1012021088 / 155819937 / 589283816 / 356530753 | State/Territory・Month・2016-17・2017-18・2018-19・2019-20・2020-21・2021-22 | al_2024_june_funding-and-payments-for-each-state-trend-1.csv |

## G118　b009「2016-17」（3 列：quantity 2・amount 1）

多いほうの quantity の例：

- 62,025 / 77,847 / 23,300 / 69,472 / 26,243 / 29,125 / 13,879 / 10,809（同じ表：Type of call・2012-13・2013-14・2014-15・2015-16・2017-18・2018-19）
- 2 / 50 / 16 / 3 / 1 / 22 / 47 / 2（同じ表：Agency・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2018-19）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 960212237 / 864315120 / 782498432 / 770994686 / 848993785 / 460420399 / 548257972 / 457752587 | State/Territory・Month・2015-16・2017-18・2018-19・2019-20・2020-21・2021-22 | al_2024_june_funding-and-payments-for-each-state-trend-1.csv |

## G119　b009「2017-18」（3 列：quantity 2・amount 1）

多いほうの quantity の例：

- 55,197 / 71,378 / 19,695 / 67,813 / 26,030 / 27,378 / 14,700 / 9,705（同じ表：Type of call・2012-13・2013-14・2014-15・2015-16・2016-17・2018-19）
- 0 / 57 / 14 / 2 / 0 / 19 / 44 / 5（同じ表：Agency・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2018-19）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 1069543268 / 883629297 / 844796851 / 909542456 / 879126915 / 153659476 / 497996528 / 522368568 | State/Territory・Month・2015-16・2016-17・2018-19・2019-20・2020-21・2021-22 | al_2024_june_funding-and-payments-for-each-state-trend-1.csv |

## G120　b009「2018-19」（4 列：quantity 2・amount 2）

多いほうの quantity の例：

- 58,710 / 73,446 / 19,725 / 64,118 / 22,163 / 25,536 / 13,006 / 9,263（同じ表：Type of call・2012-13・2013-14・2014-15・2015-16・2016-17・2017-18）
- 1 / 31 / 12 / 4 / 5 / 25 / 43 / 1（同じ表：Agency・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2017-18）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 1059195300 / 857800041 / 1095793013 / 1059331708 / 957317763 / 192322221 / 471934937 / 500482818 | State/Territory・Month・2015-16・2016-17・2017-18・2019-20・2020-21・2021-22 | al_2024_june_funding-and-payments-for-each-state-trend-1.csv |
| 3 | amount | $48 534 / 2018-19 / $553 425 /  /  / $83 821 /  /  | Contractors - Contractors with a contrac・2014-15・2015-16・2016-17・2017-18・2019-20・2020-21・2021-22 | d/2022-08-09-mfs-annual-report-data-contractors-a1846530.csv |

