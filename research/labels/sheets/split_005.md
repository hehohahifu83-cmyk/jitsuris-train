# 割れている組の見直し 005（LABEL_GUIDE v2.2）

同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。
`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。
今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。

## G121　b009「Number」（3 列：quantity 1・address 1・id 1）

多いほうの quantity の例：

- 0 / 0 / 0 / 0 / 0 / （同じ表：Year）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 1444 /  / 22 /  / 58 / 4715 / 1462 / 23 | Complex_Type・Facility_Type・Bookable_Item・Assessment_No・Locality・Post_Code・Home_Clubs・Amenities | b7e3aeba/download/golden-plains-community-facilitieshall.csv |
| 3 | id | 3 / 14 / 19 / 36 / 38 / 42 / 63 / 69 | Business Term・Terme operationnel・Definition Anglaise・Definition Francaise・Synonyme Anglais・Synonyme Francais | 6/download/ircc-glossaire-du-programme-de-citoyennete-fr.csv |

## G122　b009「2021-22」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $26 000 / 2021-22 / $639 692 /  /  /  /  / $155 772（同じ表：Contractors - Contractors with a contrac・2014-15・2015-16・2016-17・2017-18・2018-19・2019-20・2020-21）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 0 / 26 / 15 / 4 / 0 / 27 / 6 / 1 | Agency・2024-25・2023-24・2022-23・2020-21・2019-20・2018-19・2017-18 | mber-of-applications-received-by-agency-local-government.csv |

## G123　b009「title_en」（2 列：text 1・org 1）

多いほうの text の例：

- Consulting Canadians on a possible Canada-Pacific Alliance F / Consulting Canadians on trade with Asia-Pacific nations / Consultation on the Agri-Food and Aquaculture Sector Regulat / Prescribed Conditions - National Security Inadmissibility Ca / Proposed Amendments to Stay of Removal/Public Policy Conside / Revised Event Reporting Guidelines / Consultation on regulatory classification of products contai / Consultation on personal use exemption maximum quantity limi（同じ表：registration_number・partner_departments・subjects・title_fr・start_date・end_date・status・profile_page_en）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Canada Development Investment Corporation / Canada Energy Regulator / Canadian Air Transport Security Authority / Canadian Human Rights Commission / Canadian Race Relations Foundation / Copyright Board Canada / Corporation for the Mitigation of Mackenzie Gas Project Impa / Crown-Indigenous Relations and Northern Affairs Canada | title_fr・short_form_en・short_form_fr・department_number・umd_number・open_canada_id | ource/04cbec5c-5a3d-4d34-927d-e41c9e6e3736/download/orgs.csv |

## G124　b009「title_fr」（2 列：text 1・org 1）

多いほうの text の例：

- Consultation des Canadiens au sujet d’un accord de libre-éch / Consultation auprès des Canadiens au sujet du commerce avec / Consultation sur l’examen réglementaire du secteur de l’agro / Conditions réglementaires - Cas d'interdiction de territoire / Modifications proposées au sursis au renvoi/Considérations d / Lignes directrices révisées sur les rapports d’événements / Consultation sur la classification réglementaire des produit / Consultation sur les quantités maximales pour l'exemption po（同じ表：registration_number・partner_departments・subjects・title_en・start_date・end_date・status・profile_page_en）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Corporation de développement des investissements du Canada / La Régie de l’énergie du Canada / Administration canadienne de la sûreté du transport aérien / Commission canadienne des droits de la personne / La Fondation Canadienne des relations raciales / Commission du droit d'auteur du Canada / Société d'atténuation des répercussions du projet gazier Mac / Relations Couronne-Autochtones et Affaires du Nord Canada | title_en・short_form_en・short_form_fr・department_number・umd_number・open_canada_id | ource/04cbec5c-5a3d-4d34-927d-e41c9e6e3736/download/orgs.csv |

## G125　b009「名称」（20 列：org 16・address 4）

多いほうの org の例：

- チェルシー / フランススタイルのグリーンモダンアレンジサークル / 心理学コミュニティ / 外濠漢文講読会 / naranja / 腹式呼吸クラブ / 楊名時八段錦太極拳流水会 / 春虹会（同じ表：全国地方公共団体コード・地方公共団体名・名称_カナ・活動内容・主な活動場所）
- 後楽ガーデンホテル / 講道館合宿所 / D旅館 / ＳＭＩＬＥ ＨＯＭＥ 白山 / otsuka family hotel in tokyo / New民家ゲストハウス / the b 水道橋 / 文部科学省共済組合福利厚生施設（東京宿泊所）（同じ表：全国地方公共団体コード・地方公共団体名・営業形態・建物名等(方書)・許可年月日）
- ちくま旅館 / 結のや / 公認民宿 台東館 / ｺｽﾓﾌﾟﾗｻﾞ浅草橋 / 宿家･Rendez-vous / MONday Apart Premium 上野御徒町 / MONday Apart Premium 上野 / こんや（同じ表：全国地方公共団体コード・許可番号・営業形態・許可年月日）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 5 | address | ヴェルミドール恵比寿３０２ / ＥＢＩＳＵ２１０１４０２ / ＲＥＪルフレ恵比寿３０６ / ＲＡＰＩＤＯ ＳａｋｕｒａｇａｏｋａＨｏｕｓｅ ３ Ｆ / 翠楼 / Ｓｈｉｂｕｙａ ＰａｒｋＲｅｓｉｄｅｎｃｅ / Ｆｏｒｅｓｔ Ｓｉｄｅ ＹｏｙｏｇｉＰａｒｋ ３０１ / ドエル・アーバン７Ｂ | 全国地方公共団体コード・ID・地方公共団体名・許可番号・営業形態・建物名等(方書)・許可年月日 | ata.metro.tokyo.lg.jp/shibuya/131130_shibuyaku_syukuhaku.csv |
| 12 | address | 総合体育館 / スポーツランド / スポーツセンター / 陸上競技場 / 江戸川区球場 / 臨海球技場 / 水辺のスポーツガーデン / 新左近川親水公園カヌー場 | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_英字・名称_通称・POIコード・高度の種別・高度の値 | ro.tokyo.lg.jp/edogawa/131237_edogawaku_sportsfacilities.csv |
| 15 | address | 小野路球場 / 小野路グラウンド / 鶴川球場 / 鶴川中央公園テニスコート / 鶴川第二テニスコート / 木曽山崎グラウンド / 町田市立陸上競技場 / 上の原グラウンド | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_英字・名称_通称・建物名等(方書)・法人番号 | o.tokyo.lg.jp/machida/132098_machidashi_sportsfacilities.csv |
| 17 | address | 南平体育館 / 日野市民プール / 東部会館温水プール / 実践女子学園グラウンド / 万願寺中央公園グラウンド / 北川原公園グラウンド / 旭が丘中央公園グラウンド / 旭が丘中央公園テニスコート | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・トレーニング室・陸上競技・水泳・サッカー | a.metro.tokyo.lg.jp/hino/132128_hinoshi_sportsfacilities.csv |

## G126　b009「名称_カナ」（13 列：org 10・address 3）

多いほうの org の例：

- チェルシー / フランススタイルノグリーンモダンアレンジサークル / シンリガクコミュニティ / ソトボリカンブンコウドクカイ / ナランハ / フクシキコキュウクラブ / ヨウメイジハチダンニシキタイキョクケンリュウスイカイ / シュンコウカイ（同じ表：全国地方公共団体コード・地方公共団体名・名称・活動内容・主な活動場所）
- チュウオウトショカン / エイフクトショカン / カキノキトショカン / コウエンジトショカン / ミヤマエトショカン / ナリタトショカン / ニシオギトショカン / アサガヤトショカン（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_英字・団体名・利用可能曜日・開始時間・終了時間）
- スガモゴチョウメダイシンチョウカイ / ニシスガモヨンチョウメシンコウチョウカイ / ニシイケブクロミナミチョウカイ / イケブクロニチョウメハラチョウカイ / イケブクロミタケチョウカイ / イケブクロサンギョウチョウカイ / タカダチュウオウチョウカイ / メジロヒガシチョウカイ（同じ表：全国地方公共団体コード・地方公共団体名・名称・都道府県・市区町村）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 5 | address | ソウゴウタイイクカン / スポーツランド / スポーツセンター / リクジョウキョウギジョウ / エドガワクキュウジョウ / リンカイキュウギジョウ / ミズベノスポーツガーデン / シンサコンガワシンスイコウエンカヌージョウ | 全国地方公共団体コード・地方公共団体名・名称・名称_英字・名称_通称・POIコード・高度の種別・高度の値 | ro.tokyo.lg.jp/edogawa/131237_edogawaku_sportsfacilities.csv |
| 8 | address | オノジキュウジョウ / オノジグラウンド / ツルカワキュウジョウ / ツルカワチュウオウコウエンテニスコート / ツルカワダイニテニスコート / キソヤマザキグラウンド / マチダシリクジョウキョウギジョウ / ウエノハラグラウンド | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・名称_通称・建物名等(方書)・法人番号 | o.tokyo.lg.jp/machida/132098_machidashi_sportsfacilities.csv |
| 10 | address | ミナミダイラタイイクカン / ヒノシミンプール / トウブカイカンオンスイプール / ジッセンジョシガクエングラウンド / マンガンジチュウオウコウエングラウンド / キタガワラコウエングラウンド / アサヒガオカチュウオウコウエングラウンド / アサヒガオカチュウオウコウエンテニスコート | 全国地方公共団体コード・ID・地方公共団体名・名称・トレーニング室・陸上競技・水泳・サッカー | a.metro.tokyo.lg.jp/hino/132128_hinoshi_sportsfacilities.csv |

## G127　b009「名称_英字」（6 列：org 4・address 2）

多いほうの org の例：

- Central library / Eifuku library / Kakinoki library / Kouenji library / Miyamae library / Narita library / Nishiogi library / Asagaya library（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・団体名・利用可能曜日・開始時間・終了時間）
- Central Library / Lifelong Learning Center Library / Minamiosawa Library / Kawaguchi Library / Yugi Chuo Community Center Library / Ongata Community Center Library / Yui Community Center Minamino Library / Kitano Community Center Library（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・町字ID・建物名等(方書)）
- Central Library / Nakamachi Library / Hanakoganei Library / Ogawa Nishimachi Library / Kihei Library / Kamijuku Library / Tsuda Library / Onuma Library（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・建物名等(方書)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | sougoutaiikukann / sportsland / sportscenter / rikujoukyougijou / edogawacity baseball stadium / rinnkaikyuugijou / mizubenosportsgarden / shinnsakonngawashinnsuikouenncanoejou | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_通称・POIコード・高度の種別・高度の値 | ro.tokyo.lg.jp/edogawa/131237_edogawaku_sportsfacilities.csv |
| 4 | address | Onoji Baseball Field / Onoji Ground / Tsurukawa Baseball Field / Tsurukawa Chuo Park Tennis Coat / Tsurukawa Daini Tennis Coat / Kiso Yamazaki Ground / Municipal Athletic Field / Uenohara Ground | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_通称・建物名等(方書)・法人番号 | o.tokyo.lg.jp/machida/132098_machidashi_sportsfacilities.csv |

## G128　b009「名称_通称」（6 列：org 4・address 2）

多いほうの org の例：

- 中央図書館 / 生涯学習センター図書館 / 南大沢図書館 / 川口図書館 / 由木中央市民センター図書館 / 恩方市民センター図書館 / 由井市民センターみなみ野図書館 / 北野市民センター図書館（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・町字ID・建物名等(方書)）
- 中央図書館 / 青梅図書館 / 長淵図書館 / 大門図書館 / 梅郷図書館 / 沢井図書館 / 小曾木図書館 / 成木図書館（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・POIコード・町字ID・建物名等(方書)）
- 中央図書館 / 仲町図書館 / 花小金井図書館 / 小川西町図書館 / 喜平図書館 / 上宿図書館 / 津田図書館 / 大沼図書館（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・建物名等(方書)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | address |  /  /  / スピアーズえどりくフィールド /  /  /  /  | 全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・高度の種別・高度の値 | ro.tokyo.lg.jp/edogawa/131237_edogawaku_sportsfacilities.csv |
| 4 | address | 小野路GIONベースボールパーク / 小野路GIONグラウンド /  /  /  /  / 町田GIONスタジアム /  | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英字・建物名等(方書)・法人番号 | o.tokyo.lg.jp/machida/132098_machidashi_sportsfacilities.csv |

## G129　b010「名称」（48 列：org 28・address 16・text 4）

多いほうの org の例：

- 菩提寺北小学校 / 菩提寺小学校 / 日枝中学校 / 石部防災センター / 石部保育園 / 石部文化ホール / 京進のようちえんHOPPA石部南 / 石部南小学校（同じ表：TEL・FAX）
- 御殿山小学校 / 山中小学校 / 上神明小学校 / 西の台公園 / 平塚公園 / 荏原中央公園 / 南品川二丁目児童遊園 / 老人保健施設「ケアセンター南大井」（同じ表：カテゴリ）
- ビュティサロン・カトレア / Hair&Beauty Muse / ａｎｔ / 写真スタジオ暦-KOYOMI- / 美容室 小春日和 / ヘアーサロン ＩＷＡＳＡＫＩ / ATELIER 想 SOU / ブルースタイル 久が原（同じ表：全国地方公共団体コード・ID・地方公共団体名）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 駒込公園 / 教育の森公園 / 関口三丁目公園 / はつね広場 / 団子坂上広場 / 氷川下児童遊園 / 千駄木児童遊園 / 大塚五丁目児童遊園 | 全国地方公共団体コード・地方公共団体名・面積(㎡) | etro.tokyo.lg.jp/bunkyo/131059_bunkyoku_toshitoritukouen.csv |
| 3 | address | 日本堤公園 / 西町公園 / 山伏公園 / 松葉公園 / 金竜公園 / 鶯谷公園 / 待乳山聖天公園 / 上根岸公園 | 全国地方公共団体コード・面積(㎡) | .metro.tokyo.lg.jp/taito/131067_taitoku_toshitoritukouen.csv |
| 6 | address | 恵比寿四丁目児童遊園地 / 猿楽古代住居跡公園 / 鶯谷緑地 / うぐいす公園 / 恵比寿南一公園 / 氷川の杜公園 / 百軒店児童遊園地 / 円山児童遊園地 | 全国地方公共団体コード・ID・地方公共団体名・備考 | ro.tokyo.lg.jp/shibuya/131130_shibuyaku_toshitoritukouen.csv |
| 7 | address | 荒川自然公園 / 宮前公園 / 荒川三丁目公園 / 町屋五丁目北公園 / 尾久八幡公園 / 日暮里公園 / 真土公園 / 西日暮里六丁目公園 | 全国地方公共団体コード・ID・地方公共団体名 | o.tokyo.lg.jp/arakawa/131181_arakawaku_toshitoritsukouen.csv |
| 8 | address | 青戸平和公園 / 奥戸しらさぎ公園 / 奥戸ｽﾎﾟｰﾂｾﾝﾀｰ公園 / 飾にいじゅくみらい公園 / 協栄公園 / 小菅東スポーツ公園 / 白鳥南公園 / 諏訪野公園 | 全国地方公共団体コード・地方公共団体名・面積(㎡) | yo.lg.jp/katsushika/131229_katsushikaku_toshitoritukouen.csv |
| 9 | text | ふちゅう市議会だより令和7年第3回市会定例会号 / ふちゅう市議会だより令和7年第2回市会定例会号 / ふちゅう市議会だより令和7年臨時会号 / ふちゅう市議会だより令和7年第1回市会定例会号 / ふちゅう市議会だより令和6年第4回市会定例会号 / ふちゅう市議会だより令和6年第3回市会定例会号 / ふちゅう市議会だより令和6年第2回市会定例会号 / ふちゅう市議会だより令和6年臨時会号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | data.metro.tokyo.lg.jp/fuchu/132063_fuchushi_gikaidayori.csv |
| 12 | address | 公衆電話（港区元麻布1-2-2） / 公衆電話（港区芝大門2-9-11） / 公衆電話（渋谷区代々木3丁目23） / 公衆電話（台東区寿2-7-11） / 公衆電話（台東区浅草1-1-3） / 公衆電話（台東区蔵前2-6-7） / 公衆電話（台東区雷門2-18-3） / 公衆電話（中央区銀座1-19-13） | 都道府県コード又は市区町村コード・NO・都道府県名・設置者・SSID・最終確認日 | lg.jp/suisyoudataset/130001_public_wireless_lan_20240901.csv |
| 16 | address | 青少年センター / 滝山球場 / 白山球場 / 上の原グラウンド / 東部運動広場 / 西部運動広場 / 南町運動広場 / 市立テニスコート | 全国地方公共団体コード・地方公共団体名・名称_カナ・名称_通称・法人番号・利用可能曜日・開始時間・終了時間 | g.jp/higashikurume/132225_higashikurume_sportsfacilities.csv |
| 18 | address | S＆Dスポーツアリーナ羽村（スポーツセンター） / S＆Dスイミングプラザ羽村（スイミングセンター） / 弓道場 / プリモパークむさしの（武蔵野公園） / あさひ公園 / S&Dスポーツパーク富士見（富士見公園） / 宮の下運動公園 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_通称・団体名・利用可能曜日・開始時間 | tro.tokyo.lg.jp/hamura/132276_hamurashi_sportsfacilities.csv |
| 19 | address | スポーツセンター / 南町スポーツ・文化交流センター「きらっと」 / 総合体育館 / 武道場 / 芝久保運動場 / 健康広場 / ひばりが丘総合運動場「ひばりアム」 / 市民公園グラウンド | 全国地方公共団体コード・地方公共団体名・トレーニング室・陸上競技・水泳・サッカー・スキー・テニス | o.lg.jp/nishitokyo/132292_nishitokyoshi_sportsfacilities.csv |
| 21 | address | 新島スポーツ広場 / 式根島スポーツ広場 / いきいき広場 / 若郷体育館 / 村民プール | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・利用可能曜日・開始時間・終了時間・利用可能時間特記事項 | .tokyo.lg.jp/niijima/133639_niijimamura_sportsfacilities.csv |
| 23 | text | ちゅうおう区議会だより平成22年第2回定例会号 / ちゅうおう区議会だより平成22年第3回定例会号 / ちゅうおう区議会だより平成23年第2回定例会号 / ちゅうおう区議会だより平成24年第1回定例会号 / ちゅうおう区議会だより平成25年第1回臨時会号 / ちゅうおう区議会だより平成25年第2回定例会号 / ちゅうおう区議会だより平成26年第1回定例会号 / ちゅうおう区議会だより平成26年第1回臨時会号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | pendata.metro.tokyo.lg.jp/chuo/131024_chuoku_gikaidayori.csv |
| 24 | text | 平成18年第4回定例会･平成19年新年号 / 議会改革特集号 / 平成19年第4回定例会･新年合併号 / 平成20年第2回定例会号 / 平成20年第4回定例会･新年合併号 / 平成21年第1回定例会号 / 区議会アンケート特集号 / 平成23年第1回定例会号 | 全国地方公共団体コード・ID・地方公共団体名・号数・発行年月・発行元 | tro.tokyo.lg.jp/shinjyuku/131041_shinjyukuku_gikaidayori.csv |
| 25 | address | 文京区営本駒込二丁目アパート / 文京区営白山四丁目アパート / 文京区営白山四丁目アパート / 文京区営白山四丁目アパート / 文京区営関口二丁目アパート / シルバーピアおおつか / シルバーピア千石 / シルバーピア向丘 | 全国地方公共団体コード・地方公共団体名・建物名等(方書)・面積・間取り・建設年度・管理戸数・一般 | ata.metro.tokyo.lg.jp/bunkyo/131059_bunkyoku_koueijutaku.csv |
| 26 | address | シルバーピアきよかわ / シルバーピア今戸 / シルバーピア千束 / シルバーピア寿 / シルバーピア入谷 / シルバーピア日本堤 / シルバーピア西町 / シルバーピア三筋 | 全国地方公共団体コード・管理戸数・シルバーピア | ndata.metro.tokyo.lg.jp/taito/131067_taitoku_koueijutaku.csv |
| 30 | text | せたがや区議会だより令和6年第3回区議会定例会号 / せたがや区議会だより令和6年第4回区議会定例会号 / せたがや区議会だより令和7年第1回区議会臨時会・第1回定例会号 / せたがや区議会だより令和7年第2回区議会臨時会号 / せたがや区議会だより令和7年第2回区議会定例会号 / せたがや区議会だより令和7年第3回区議会定例会号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元・町字ID | metro.tokyo.lg.jp/setagaya/131121_setagayaku_gikaidayori.csv |
| 31 | address | 代々木三丁目住宅 / ハイツ橡尾 / 代官山アドレス / 幡ヶ谷原町住宅 / 幡ヶ谷二丁目住宅 / 幡ヶ谷二丁目住宅 / 幡ヶ谷二丁目住宅 / メゾン幡ヶ谷 | 全国地方公共団体コード・ID・地方公共団体名・面積・間取り・建設年度・管理戸数・備考1_種別1 | a.metro.tokyo.lg.jp/shibuya/131130_shibuyaku_koueijutaku.csv |
| 33 | address | さくらハイツ南千住（南千住二丁目住宅） / さくらハイツ町屋（町屋七丁目住宅） / さくらハイツ小台（西尾久三丁目住宅） / さくらハイツ西尾久（西尾久七丁目住宅） / 町屋五丁目住宅 | 全国地方公共団体コード・地方公共団体名 | a.metro.tokyo.lg.jp/arakawa/131181_arakawaku_koueijutaku.csv |
| 34 | address | 青戸八丁目第2アパート / 白鳥三丁目第4アパート / 柴又二丁目アパート1号棟 / 柴又二丁目アパート2号棟 / 柴又二丁目アパート3号棟 / 柴又六丁目アパート2号棟 / 宝町一丁目アパート2号棟 / 西亀有二丁目第9アパート10号棟 | 全国地方公共団体コード・ID・地方公共団体名・建物名等(方書)・面積・間取り・建設年度・管理戸数 | o.tokyo.lg.jp/katsushika/131229_katsushikaku_koueijutaku.csv |
| 35 | address | 府中市営第一武蔵台住宅 / 府中市営第二矢崎町住宅北 / 府中市営第三本町住宅 / 府中市営第四栄町住宅 / 府中市営第五是政住宅 / 府中市営第六若松町住宅 / 府中市営第七西府町住宅 / 府中市営第八新町住宅 | 全国地方公共団体コード・ID・地方公共団体名・建物名等(方書)・面積・間取り・建設年度・管理戸数 | data.metro.tokyo.lg.jp/fuchu/132063_fuchushi_koueijutaku.csv |

## G130　b010「市区町村」（2 列：id 1・address 1）

多いほうの id の例：

- 452017 / 452017 / 452017 / 452017 / 452017 / 452017 / 452017 / 452017（同じ表：_id・NO・情報掲載月・ジャンル・タイトル）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 国立市 / 国立市 / 国立市 / 国立市 / 国立市 / 国立市 / 国立市 / 国立市 | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・都道府県 | a.metro.tokyo.lg.jp/kunitachi/132152_kunitachishi_chokai.csv |

## G131　b010「名称_カナ」（18 列：org 15・address 3）

多いほうの org の例：

- アキシマシヤクショ / イーストテラス・サブスリー / マツバラチョウコミュニティセンター / キンロウショウコウシミンセンター / アサヒチョウコウレイシャフクシセンター / マツバラチョウコウレイシャフクシセンター / ハイジマチョウコウレイシャフクシセンター / ジドウセンター「パレット」（同じ表：都道府県コード 又は市区町村コード・NO・都道府県名・市区町村名・名称・名称_英語・設置者・SSID）
- クニタチカイヒガシノカイ / ヒガシイチ・ニチョウメチョウカイ / アーデルグランクニタチジチカイ / クニタチシサンワカイ / アオバカイ / トエイクニタチニシイッチョウメアパートジチカイ / トエイクニタチキタサンダイニアパートダイイチジチカイ / イチョウナミキクニタチジチカイ（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・都道府県・市区町村）
- チュウオウトショカン / アカツカトショカン / シミズトショカン / ハスネトショカン / ヒカワトショカン / タカシマダイラトショカン / ヒガシイタバシトショカン / コモネトショカン（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_英字・名称_通称・POIコード・建物名等(方書)・高度の種別）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 5 | address | セイショウネンセンター / タキヤマキュウジョウ / ハクサンキュウジョウ / ウエノハラグラウンド / トウブウンドウヒロバ / セイブウンドウヒロバ / ミナミチョウウンドウヒロバ / シリツテニスコート | 全国地方公共団体コード・地方公共団体名・名称・名称_通称・法人番号・利用可能曜日・開始時間・終了時間 | g.jp/higashikurume/132225_higashikurume_sportsfacilities.csv |
| 7 | address | エスアンドディースポーツアリーナハムラスポーツセンター / エスアンドディースイミングプラザハムラスイミングセンター / キュウドウジョウ / プリモパークムサシノムサシノコウエン / アサヒコウエン / エスアンドディースポーツパークフジミフジミコウエン / ミヤノシタウンドウコウエン | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_通称・団体名・利用可能曜日・開始時間 | tro.tokyo.lg.jp/hamura/132276_hamurashi_sportsfacilities.csv |
| 9 | address | ニイジマスポーツヒロバ / シキネジマスポーツヒロバ / イキイキヒロバ / ワカゴウタイイクカン / ソンミンプール | 全国地方公共団体コード・ID・地方公共団体名・名称・利用可能曜日・開始時間・終了時間・利用可能時間特記事項 | .tokyo.lg.jp/niijima/133639_niijimamura_sportsfacilities.csv |

## G132　b010「名称_通称」（6 列：org 5・address 1）

多いほうの org の例：

-  /  /  /  /  /  /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・建物名等(方書)・高度の種別）
- 小金井市立図書館 / 小金井市立図書館東分室 / 小金井市立図書館緑分室 / 小金井市立図書館貫井北分室 / 小金井市立図書館西之台会館図書室（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・名称_英字・POIコード・外部識別子・外部識別子の値）
-  /  /  /  /  /  /  / （同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_カナ・法人番号・利用可能曜日・開始時間・終了時間）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 4 | address | スポーツセンター / スイミングセンター /  / 武蔵野公園 /  / 富士見公園 /  | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・団体名・利用可能曜日・開始時間 | tro.tokyo.lg.jp/hamura/132276_hamurashi_sportsfacilities.csv |

## G133　b010「Outcome」（2 列：text 1・category 1）

多いほうの text の例：

- Outcome 1: More sustainable, productive, internationally com / Outcome 1: Provide correct or preferable decisions through a / Outcome 1: A just and secure society through the maintenance / Outcome 1: To contribute to Defence outcomes by providing to / Outcome 2: Protect and advance Australia’s strategic interes / Outcome 2: Protect and advance Australia’s strategic interes / Outcome 1: Foster a productive and competitive labour market / Outcome 3: Support for parliamentarians and others as requir（同じ表：Portfolio・Program・Expense_type・Appropriation_type・2024-25・2025-26・2026-27・2027-28）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Other / Accepted / Accepted / Accepted / Other / Other / Accepted / Accepted | Province of residence at the time of the・Year・Total | sions-from-1997-2021-by-outcome-and-province-of-claimant.csv |

## G134　b010「Program」（2 列：account 1・category 1）

多いほうの account の例：

- Program 1.13: International Market Access / Program 1.1: Administrative Review Tribunal / Program 1.4: Justice Services / Program 1.1 Other Departmental - DHA / Program 2.6 Army Capabilities / Program 2.11 Defence Digital / Outcome 1 / Program 3.1: Ministerial and Parliamentary Services（同じ表：Portfolio・Outcome・Expense_type・Appropriation_type・2024-25・2025-26・2026-27・2027-28）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Disability / Disability / Disability / Disability / Disability / Disability / Disability / Disability | Date・Type・Claim・Processing Time (weeks) | -386aa1321350/download/wtt-odta-2020-04-01-2020-06-30_en.csv |

## G135　b010「Region」（5 列：address 4・id 1）

多いほうの address の例：

- Gippsland / Loddon-Mallee Region; Loddon-Mallee Region / Eastern Metro / Barwon South Western Region / North and West Metropolitan Region / North and West Metropolitan Region / Loddon-Mallee Region / North and West Metropolitan Region（同じ表：Suburb・State・Business Category・LGA）
- Prairie Region / Prairie Region / Prairie Region / Pacific Region / Pacific Region / Atlantic Region / Atlantic Region / Québec Region（同じ表：Date・Mode・Sum of Volume）
- British Columbia / Alberta / Saskatchewan / Manitoba / Western Canada（同じ表：% of professional jobs）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | id | 2 / 2 / 2 / 4 / 5 / 5 / 6 / 8 | Suburb・P/C・Business Ph・Category | ov.au/storage/f/2013-05-12T180721/tmp07rzt1CFA-locations.csv |

## G136　b010「VALUE」（7 列：quantity 4・amount 1・rate 1・other 1）

多いほうの quantity の例：

- 66 / 20 / 227 / 72 / 219299 / 35817 / 138145 / 7418（同じ表：STATISTIC・Statistic・TLIST(A1)・Year・C02498V03025・Sex Category School・UNIT）
- 9450 / 11600 / 12000 / 14040 / 14591 / 15190 / 16078 / 18809（同じ表：STATISTIC・Statistic Label・YEAR・Year・BEDTYPE・Bed type・UNIT・FLAG）
- 929 / 815 / 1007 / 1240 / 600 / 1177 / 2788 / 2833（同じ表：STATISTIC・Statistic・TLIST(M1)・Month・C02196V02652・State・UNIT）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 393.7 / 423.3 / 409.7 / 488.6 / 594 / 1190.4 / 665 / 1542.7 | STATISTIC・Statistic・TLIST(Q1)・Quarter・C02568V03113・Item・UNIT | pi.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en |
| 5 | rate | 90 / 94 / 95 / 91 / 91 / 95 / 94 / 95 | STATISTIC・Statistic・TLIST(A1)・Year・C02779V03348・County・C03552V04288・Vaccine Type | pi.restful/PxStat.Data.Cube_API.ReadDataset/G0328/CSV/1.0/en |
| 7 | other | 102.5 / 133.8 / 85 / 115.5 / 127 / 64 / 168.9 / 37.2 | STATISTIC・Statistic Label・tlist_m1_・Month・C02431V02938・Meteorological Weather Station・UNIT | pi.restful/PxStat.Data.Cube_API.ReadDataset/MTM01/CSV/1.0/en |

## G137　b010「REGIONAL」（2 列：address 1・category 1）

多いほうの address の例：

- BARREIRO / CENTRO-SUL / CENTRO-SUL / ENDEREÇO NÃO GEORREFERENCIADO / LESTE / LESTE / NORDESTE / NORDESTE（同じ表：CRAS・QTDE_FAMILIAS・MES_ANO_REFERENCIA）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | DIRE-VN / DIRE-N / DIRE-O / DIRE-O / DIRE-NO / DIRE-CS / DIRE-CS / DIRE-O | INEP・ESCOLA・BAIRRO・OFERTA REFEICAO | 4b04e9eda08/download/20241230_instituicoes_rede_parceira.csv |

## G138　b011「名称」（43 列：org 29・address 9・text 4・other 1）

多いほうの org の例：

- ヘアーサロンよしもと / ヘアーズタタラ / 理髪 関根 / barber Suma / 介護老人保健施設ケアセンター南大井 / BARBER SPACE I－Dy / ヘアーサロンイバヤシ / BARBER SHOP BABO（同じ表：全国地方公共団体コード・地方公共団体名・確認番号・確認年月日）
- 田中クリーニング / 三浦クリーニング商会 / ㈱東ﾗﾝ / 松原クリーニング / 株式会社白洋舎 ユニフォームレンタル東部事業所東京工場 / クリーニング ぴゅあ 梅屋敷店 / エニタイムクリーニング大森町駅前店 / ホワイト急便山王店（同じ表：全国地方公共団体コード・ID・地方公共団体名・営業形態）
- Ｊｅｔ Ｓｅｔ 東京ミッドタウン日比谷 / ＭＡＫＥ－ＵＰ＆ＰＨＯＴＯ ＳＴＵＤＩＯ ＯＰＳＩＳ / ヴォートル イストワール シュウ ウエムラ ウェディング / ｅｎ 銀座店 / ＱＢハウス麹町店 / 美容室ブロス / ＭＡＴＩＬＤＡ ｈａｉｒ ｍａｋｅ ＆ ｎａｉｌ / Ｅｙｅｌａｓｈｅｓ＆Ｎａｉｌ Ｓａｌｏｎ ＳＰＡＣＥ（同じ表：確認年月日）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | address | 坂本町公園 / 鉄砲洲児童公園 / 数寄屋橋公園 / 月島第一児童公園 / 月島第二児童公園 / 楓川久安橋公園 / 楓川新富橋公園 / 築地川采女橋公園 | 全国地方公共団体コード・地方公共団体名・湊1・面積(㎡) | ta.metro.tokyo.lg.jp/chuo/131024_chuoku_toshitoritukouen.csv |
| 2 | address | 大久保公園 / 西戸山公園 / 柏木公園 / 大東橋公園 / 北柏木公園 / 新小川公園 / まつ川公園 / 中町公園 | 全国地方公共団体コード・地方公共団体名・面積(㎡) | tokyo.lg.jp/shinjyuku/131041_shinjukuku_toshitoritukouen.csv |
| 3 | address | 江東区立平野四丁目公園 / 江東区立牡丹町公園 / 江東区立中の島公園 / 江東区立しおかぜ橋塩浜公園 / 江東区立塩浜二丁目公園 / 江東区立暁橋公園 / 江東区立豊洲公園 / 江東区立豊洲四丁目第二公園 | 全国地方公共団体コード・地方公共団体名・面積(㎡) | ta.metro.tokyo.lg.jp/koto/131083_kotoku_toshitoritukouen.csv |
| 6 | address | 桜丘やまもも公園 / 桜丘五丁目公園 / 鶴ヶ久保公園 / 三宿えのき公園 / 若林なつつばき公園 / 豪徳寺一丁目たまにゃん公園 / どんぐりひろば公園 / 上用賀五丁目公園 | 全国地方公共団体コード・地方公共団体名 | .tokyo.lg.jp/setagaya/131121_setagayaku_toshitoritukouen.csv |
| 7 | address | 日比谷地下自動車道 / 新橋地下自動車道 / 仙台坂トンネル / 平和隧道 / 東海隧道 / 橋詰トンネル / 中山トンネル / 大麦代トンネル | 番号・所管事務所・路線名・工法・建設年度・延長(m) | opendata.metro.tokyo.lg.jp/kensetsu/R3/jigyokeikakukouka.csv |
| 21 | text | 新島村議会だより / 新島村議会だより / 新島村議会だより / 新島村議会だより / 新島村議会だより / 新島村議会だより / 新島村議会だより / 新島村議会だより | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元・町字ID | metro.tokyo.lg.jp/niijima/133639_niijimamura_gikaidayori.csv |
| 22 | text | 御蔵島村議会だより第12号 / 御蔵島村議会だより第16号 / 御蔵島村議会だより第19号 / 御蔵島村議会だより第26号 / 御蔵島村議会だより第30号 / 御蔵島村議会だより第31号 / 御蔵島村議会だより第32号 / 御蔵島村議会だより第33号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | tokyo.lg.jp/mikurajima/133825_mikurajimamura_gikaidayori.csv |
| 23 | address | 新小川町第2区営住宅 / 新小川町第1区営住宅 / 早稲田南町コーポラス / 河田町第2アパート / 市谷台町第1区営住宅 / 西早稲田三丁目第1区営住宅 / 富久町第1区営住宅 / 若松町第1区営住宅 | 全国地方公共団体コード・ID・地方公共団体名・建物名等(方書) | etro.tokyo.lg.jp/shinjyuku/131041_shinjukuku_koueijutaku.csv |
| 25 | address | 大島住宅 / 猿江住宅 / ピアおおじま / ピアこうとう / 塩浜一丁目住宅12号棟 / 塩浜一丁目住宅14号棟 / 塩浜住宅1号棟 / 塩浜住宅2号棟 | 全国地方公共団体コード・地方公共団体名 | pendata.metro.tokyo.lg.jp/koto/131083_kotoku_koueijutaku.csv |
| 28 | address | ユアーズ若林 / 世田谷二丁目アパート / 弦巻四丁目第三アパート / 大原一丁目アパート / グリーンヒル大原 / 桜上水三丁目アパート / 上用賀五丁目アパート / 玉川四丁目アパート | 全国地方公共団体コード・地方公共団体名・間取り・建設年度・管理戸数 | metro.tokyo.lg.jp/setagaya/131121_setagayaku_koueijutaku.csv |
| 32 | text | くにたち市議会だより令和６年第2回定例会号 / くにたち市議会だより令和６年第1回臨時会・定例会号 / くにたち市議会だより令和５年第4回定例会号 / くにたち市議会だより令和５年第3回定例会号 / くにたち市議会だより令和５年第2回定例会号 / くにたち市議会だより令和５年第1回臨時会号 / くにたち市議会だより令和５年第1回定例会号 / くにたち市議会だより令和４年第4回定例会号 | 全国地方公共団体コード・ID・地方公共団体名・号数・発行年月・発行元・町字ID | ro.tokyo.lg.jp/kunitachi/132152_kunitachishi_gikaidayori.csv |
| 37 | other | ハギ / ムラサキ / ムラサキハナナ / ツツジ / ジンチョウゲ / スイセン / フヨウ / アサガオ | 全国地方公共団体コード・ID・地方公共団体名・種類・種類についての補足・制定年・制定月・制定日 | a.metro.tokyo.lg.jp/musashino/132039_musashinoshi_symbol.csv |
| 40 | address | 黒鐘公園 / 姿見の池緑地 / 窪東公園 / 内藤さつき公園 / 並木町公園 / 北町公園 / けやき公園 / 泉町多喜窪公園 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・設置位置・男性トイレ総数・男性トイレ数（小便器）・男性トイレ数（和式） | pendata.metro.tokyo.lg.jp/kokubunji/132144_public_toilet.csv |
| 41 | text | たま市議会だより令和4年2月5日号 / たま市議会だより令和4年5月5日号 / たま市議会だより令和4年8月5日号 / たま市議会だより令和4年11月5日号 / たま市議会だより令和5年2月5日号 / たま市議会だより令和5年5月5日号 / たま市議会だより令和5年6月5日号 / たま市議会だより令和5年8月5日号 | 全国地方公共団体コード・ID・地方公共団体名・号数・発行年月・発行元・町字ID | endata.metro.tokyo.lg.jp/tama/132241_tamashi_gikaidayori.csv |

## G139　b011「名称_カナ」（16 列：org 15・address 1）

多いほうの org の例：

- イグサ・ユウユウミマモリタイフレアイショクドウ / コドモショクドウホープ / ニシオギ・テラコヤショクドウ / ワイワイショクドウコーナーチュウコウセイタイムスペシャル / コウサテンパントリー / ニシオギクリキンディノヒトシズク / ニシオギクリキンディノヒトシズク / モモイ・ミンナデショクドウ(ミンショク)（同じ表：全国地方公共団体コード・都道府県・市区町村名・名称・方書・開催頻度・開催曜日・開催開始時間）
- アイコウアケボノホイクエン / アイコウダイゴホイクエンサンクレール / アイコウホイクエン / アイコウミドリホイクエン / アオバダイニホイクエン / カシワホイクエン / キラメキノモリホイクエン / ジョウナンルミナホイクエンタチカワ（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・種別・認可等年月日・入園案内ホームページ）
- ミカヅキコドモショクドウ / ユトリエモッタイナイショクドウ / ワイワイライス / ミューショクドウ / ファイブグループコドモショクドウ（同じ表：全国地方公共団体コード・ID・都道府県・市区町村名・名称・方書・運営団体名・開催頻度）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 15 | address | クロガネコウエン / スガタミノイケリョクチ / クボヒガシコウエン / ナイトウサツキコウエン / ナミキチョウコウエン / キタマチコウエン / ケヤキコウエン / イズミチョウタキクボコウエン | 全国地方公共団体コード・ID・地方公共団体名・名称・設置位置・男性トイレ総数・男性トイレ数（小便器）・男性トイレ数（和式） | pendata.metro.tokyo.lg.jp/kokubunji/132144_public_toilet.csv |

## G140　b011「location」（4 列：address 3・category 1）

多いほうの address の例：

- Saddle Point / Azorella Peninsula / West Bay / Nullarbor Plain / Erratic Point / South West Bay / Laurens Peninsula / Laurens Peninsula（同じ表：species・id・feature・observation_date・observation_date_year・observation_date_month・observation_date_day・comments）
- Congupna Recreation Reserve (Congupna) / Congupna Recreation Reserve (Congupna) / Karramomus Recreation Reserve Land / Tatura Showground and Recreation Reserve / John McEwen Reserve (Shepparton) / Merrigum Swimming Pool / Aquamoves (Shepparton) / Kidstown (Mooroopna)（同じ表：ref・num_of・num_burner・type）
- N Stornes / W Stornes / Central Stornes / SE Stornes / E Stornes / Grovness / Sigdoy Island / Sigdoy Island（同じ表：lake_id・altitude・lake_area・catchment_area・maximum_depth・dimensions・distance_from_polar_plateau・geology）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | park / park / park / other / other / residential / park / other | lat, lon・genus・species・dbh・height・common・ref・maturity | -4d5d-94f4-03314ba6b252/download/yarra-significant-trees.csv |

## G141　b011「Designation」（2 列：category 1・text 1）

多いほうの category の例：

- Cooled appliance / Cooled appliance / Cooled appliance / Cooled appliance / Cooled appliance（同じ表：ApplStandard・Brand・Labelled energy consumption (kWh/year)・CompartGrVol・CompartType・Configuration・Country・Depth）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | These lands are already zoned for residential development. I / These lands are already zoned for residential development. I / Primary Development Area: These lands are already zoned for / These lands are already zoned for residential development. I / These lands are already zoned for open space / park uses. Th / These lands are already zoned for residential development. I / These lands are already zoned for residential development. I / These lands are already zoned for residential development. I | OBJECTID・Eff_From・Eff_To・Zoning・Area_Ha・Generic_Zoning・MyPlan_GZT・Information | scache/Wicklow_Zoning_CDP_2022_2028_-1261874313604190018.csv |

## G142　b011「Table」（2 列：text 1・id 1）

多いほうの text の例：

- Table 5: Age Pension customers by state/territory and sex, J / Table 5: Age Pension customers by state/territory and sex, J / Table 7: Disability Support Pension customers, characteristi / Table 6: Disability Support Pension customers by sex, June 1 / Table 9: Sickness Allowance customers by sex, June 1990 to J / Table 10: Sickness Allowance customers, characteristics by s / Table 12: Mobility Allowance customers by sex, June 1990 to / Table 12: Mobility Allowance customers by sex, June 1990 to（同じ表：Publication・Extract・Payment・Payment_Type・Source・Theme_1・Measure_1・Theme_2）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | id | 2 / 4 / 5 / 6 / 7 / 8 / 9 / 11 | Title・Survey Question・Notes | b1f9-46e7cfcd92d7/download/2014_sfgsme-efcpme_tables_eng.csv |

## G143　b011「title」（2 列：org 1・text 1）

多いほうの org の例：

- Bella Vista Clinical Labs Pathology Walk-In Clinic / Belmore Respiratory Clinic / Bondi Junction GP Respiratory Clinic / Condobolin Multi-Purpose Health Service Clinic / Cowra Respiratory Clinic / Dee Why Respiratory Clinic / Dubbo Respiratory Clinic / Lakemba Respiratory Clinic（同じ表：uniqueID・suburb・state・locationInstructions・driveThroughTesting・wheelchairAccessible・walkInAllowed・bookingRequired）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in / Sydney - photographs of streets, public buildings, views in | itemid・albumnumber・dateofwork・collectionitemlink・digitalitemlink・digitalordernumber・thumbnaillink・highreslink | .au/storage/f/2013-05-12T210543/tmpCYp8JMsydney-pictures.csv |

## G144　b011「scheme」（2 列：id 1・category 1）

多いほうの id の例：

- CAR / CAR / UA / MAT / WNCP / OFP / DB / UA（同じ表：period・programme・basis・sex_code・sex・recipients）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | FIS / DPMA / CAR / SPNC / SPNC / WCP / SPNC / UA | period・programme・basis・county・county_code・recipients | ssets.gov.ie/311530/978139ff-2a25-43a0-878e-42b046ae0aa1.csv |

## G145　b011「Q1」（2 列：quantity 1・category 1）

多いほうの quantity の例：

- 5 / 2 / 10 / 4 / 20 / 23 / 27 / 16（同じ表：RegionID・AreaID・Area・Year・Q2・Q3・Q4）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | 5 / 4 / 6 / 4 / 5 / 5 / 5 / 5 | QUEST・STYPE・CPO_STATUS・QF・Q2・Q3・Q4A・Q4B | 21-survey-of-canadians-on-privacy-related-issues-dataset.csv |

## G146　b011「desc」（2 列：category 1・account 1）

多いほうの category の例：

- CONC SPLITTER ISLAND / VIC ROADS MEDIAN STRIP / BRICK SPLITTER ISLAND / NULL / CONC SPLITTER ISLAND / CONC & LANDSCAPED SLOW POINT / BRICK SPLITTER ISLAND / BLUESTONE SPLITTER ISLAND（同じ表：type・ref・long）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | account | Housing & Building / Road Transport & Safety / Water Services / Development Management / Environmental Services / Recreation & Amenity / Agriculture, Food & the Marine / Miscellaneous Services | Doc・Heading・Ref・Inc・PY・OBJECTID | m/datasets/RosCoCo::annual-budget-2018-table-e-roscommon.csv |

## G147　b011「2016-17」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $0 / 2016-17 /  /  /  /  /  / （同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2017-18・2018-19・2019-20・2020-21・2021-22）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 283 / 155 / 8 / 10 / 2 / 1 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2018-19 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

## G148　b011「2017-18」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $9 085 / 2017-18 / $17 579 /  /  /  /  / （同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2016-17・2018-19・2019-20・2020-21・2021-22）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 332 / 134 / 9 / 11 / 2 / 3 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2018-19 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

## G149　b011「2018-19」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $9 790 / 2018-19 /  /  /  /  /  / （同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2016-17・2017-18・2019-20・2020-21・2021-22）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 282 / 243 / 9 / 19 / 6 / 4 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2021-22・2020-21・2019-20・2017-18 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

## G150　b011「2019-20」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $57 715 / 2019-20 /  / $30 870 /  / $30 134 / $18 154 / $12 860（同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2016-17・2017-18・2018-19・2020-21・2021-22）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 306 / 380 / 5 / 14 / 10 / 2 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2021-22・2020-21・2018-19・2017-18 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

