# 割れている組の見直し 006（LABEL_GUIDE v2.2）

同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。
`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。
今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。

## G151　b011「2020-21」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $18 508 / 2020-21 /  /  /  /  /  / （同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2016-17・2017-18・2018-19・2019-20・2021-22）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 690 / 180 / 22 / 18 / 3 / 4 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2021-22・2019-20・2018-19・2017-18 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

## G152　b011「2021-22」（2 列：amount 1・quantity 1）

多いほうの amount の例：

- $18 000 / 2021-22 /  /  /  /  /  / （同じ表：Consultants - Consultancies with a contr・2014-15・2015-16・2016-17・2017-18・2018-19・2019-20・2020-21）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | quantity | 601 / 77 / 13 / 14 / 1 / 0 | Formal extension reasons, by sector・2024-25・2023-24・2022-23・2020-21・2019-20・2018-19・2017-18 | a-foi-number-of-s14-1-extensions-given-by-sector-by-year.csv |

## G153　b012「名称」（47 列：org 36・address 8・text 2・other 1）

多いほうの org の例：

- Ocean Shinagawa / LUMIERE南品川B棟 03 / LUMIERE南品川B棟 02 / 宿処龍馬 青物横丁Ⅰ / HOSTEL・LUND / KIKA STAY / ゲストハウス大崎 / 東急ステイ五反田（同じ表：全国地方公共団体コード・地方公共団体名・許可番号・営業形態・許可年月日・備考）
- アークテリクス 東京丸の内ブランドストア / メトグリーン３号館薬局内ホワイト急便 / ㈱オオニシ外務省売店 / 東宝舞台（株）クリーニング取次店 / 参議院議員会館小松屋クリーニング / ポニークリーニング半蔵門店 / ウブカタ・クリーニング有限会社 / ホーマット三番町（同じ表：営業形態・確認年月日）
- 下町こども食堂みらい / 下町こども食堂さくら / ユニバーサルスペースさくら / よみせ通りいこいの家 / Kids Café / まなび部子供食堂 / もぐもぐ子供食堂（同じ表：全国地方公共団体コード・ID・都道府県・市区町村名・名称_カナ・設置目的・実施支援の主な区分・方書）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 大倉山公園 / 春日公園 / 大森南第一公園 / 東糀谷第一公園 / 東糀谷防災公園 / 本羽田一丁目公園 / 久が原公園 / 洗足池公園 | 全国地方公共団体コード・ID・地方公共団体名 | data.metro.tokyo.lg.jp/ota/131113_otaku_toshitoritukouen.csv |
| 3 | text | としま区議会だより令和5年第1回定例会号 / としま区議会だより令和5年第1回臨時会号 / としま区議会だより令和5年第2回定例会号 / としま区議会だより令和5年第3回定例会号 / としま区議会だより令和6年新年号 / としま区議会だより令和5年第4回定例会・令和6年第1回臨時会号 / としま区議会だより令和6年第1回定例会・第2回臨時会号 / としま区議会だより令和6年第3回臨時会号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | a.metro.tokyo.lg.jp/toshima/131164_toshimaku_gikaidayori.csv |
| 4 | address | 谷保第一公園 / 谷保第二公園 / 谷保第三公園 / 谷保第四公園 / 谷保第五公園 / 谷保第六公園 / 矢川上公園 / 西児童公園 | 全国地方公共団体コード・ID・地方公共団体名・面積(㎡) | kyo.lg.jp/kunitachi/132152_kunitachishi_toshitoritukouen.csv |
| 18 | other | 茶の花 / つつじ / まつ / もくせい / ひばり | 全国地方公共団体コード・ID・地方公共団体名・種類 | ndata.metro.tokyo.lg.jp/mizuho/133035_mizuhomachi_symbol.csv |
| 19 | address | 五反田南公園 / 西の森公園 / 北浜公園 / 旗の台北公園 / 旗の台なか公園 / 旗の台広場公園 / 天王洲アイル第九公園 / 庚申公園 | 全国地方公共団体コード・地方公共団体名・面積(㎡) | okyo.lg.jp/shinagawa/131091_shinagawaku_toshitoritukouen.csv |
| 20 | address | 蒲田二丁目アパート / 南六郷一丁目第３アパート ３号棟 / 中馬込一丁目アパート １号棟 / 仲六郷一丁目第３アパート / プラムハイツ西馬込 / プラムハイツ東矢口 / プラムハイツ千鳥 / 中央八丁目アパート １号棟 | 全国地方公共団体コード・ID・地方公共団体名・面積・間取り・建設年度・管理戸数・一般 | .opendata.metro.tokyo.lg.jp/ota/131113_otaku_koueijutaku.csv |
| 23 | address | 江戸東京たてもの園 / 東京都写真美術館 / 東京都現代美術館 / 東京文化会館 / トーキョーアーツアンドスペース本郷 / 大泉中央公園 / 砧公園 / 木場公園 | 都道府県コード又は市区町村コード・都道府県名・名称_カナ・POIコード・方書・利用可能曜日・開始時間・終了時間 | .metro.tokyo.lg.jp/suisyoudataset/130001_public_facility.csv |
| 28 | address | 篠崎緑地 / 小松川境川親水公園 / 総合レクリエーション公園 / 総合レクリエーション公園 / 総合レクリエーション公園 / 総合レクリエーション公園 / 総合レクリエーション公園 / 総合レクリエーション公園 | 全国地方公共団体コード・ID・地方公共団体名・建物名等(方書)・設置位置・高度の種別・高度の値・バリアフリートイレ数 | .opendata.metro.tokyo.lg.jp/edogawa/131237_public_toilet.csv |
| 37 | address | 南大井六丁目区営住宅 / 西大井六丁目区営住宅 / 南大井一丁目区営住宅 / 南大井五丁目区営住宅 / 西大井六丁目第二区営住宅 / 西大井六丁目第二区営住宅 / 東大井三丁目区営住宅 / 東大井三丁目区営住宅 | 全国地方公共団体コード・地方公共団体名・間取り・管理戸数・主な線・主な駅 | tro.tokyo.lg.jp/shinagawa/131091_shinagawaku_koueijutaku.csv |
| 38 | address | 宮本公園 / 芳林公園 / 東郷元帥記念公園 / 練成公園 / 淡路公園 / 西神田公園 / 神田児童公園 / 神田橋公園 | 地方公共団体名・面積(㎡) | ro.tokyo.lg.jp/chiyoda/131016_chiyodaku_toshitoritukouen.csv |
| 46 | text | 町田市議会だより / 町田市議会だより / 町田市議会だより / 町田市議会だより / 町田市議会だより / 町田市議会だより / 町田市議会だより | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | .metro.tokyo.lg.jp/machida/132098_machidashi_gikaidayori.csv |

## G154　b012「備考」（11 列：text 8・category 2・date 1）

多いほうの text の例：

-  /  /  /  /  /  /  / （同じ表：床面積の合計・金額（円））
-  /  /  /  /  /  /  / （同じ表：名称・卸売業者・仲卸業者・関連事業者流通保管業務・関連事業者物販・飲食業務・関連事業者加工・サービス業務・関連事業者合計・売買参加者）
-  /  /  /  / 回答数103人（同じ表：回答・割合(％)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | category |  /  /  /  /  /  /  /  | 全国地方公共団体コード・地方公共団体名・許可番号・営業形態・名称・許可年月日 | metro.tokyo.lg.jp/shinagawa/131091_shinagawaku_syukuhaku.csv |
| 5 | category | 宿泊 /  /  /  /  /  / 登録 /  | 区市町村名・施設区分・施設名 | ps://www.opendata.metro.tokyo.lg.jp/kyouiku/R3/skseti_47.csv |
| 7 | date | 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 / 令和６年４月１日時点 | 全国地方公共団体コード・地方公共団体名・名称・都道府県・市区町村 | tokyo.lg.jp/higashikurume/132225_higashikurumeshi_chokai.csv |

## G155　b012「発行元」（2 列：account 1・org 1）

多いほうの account の例：

- 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局 / 豊島区議会事務局（同じ表：全国地方公共団体コード・地方公共団体名・名称・号数・発行年月）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | 町田市議会 / 町田市議会 / 町田市議会 / 町田市議会 / 町田市議会 / 町田市議会 / 町田市議会 | 全国地方公共団体コード・地方公共団体名・名称・号数・発行年月 | .metro.tokyo.lg.jp/machida/132098_machidashi_gikaidayori.csv |

## G156　b012「区分」（4 列：category 3・account 1）

多いほうの category の例：

- 総数 / 法律相談 / 人権身の上相談 / 交通事故相談 / 家庭相談 / 税務相談 / 市政・行政相談 / 登記相談（同じ表：2012年度・2013年度・2014年度・2015年度・2016年度・2017年度・2018年度・2019年度）
- 牛総数 / 和牛総数 / 和牛生体枝肉 / 和牛搬入枝肉 / 交雑牛総数 / 交雑牛生体枝肉 / 交雑牛搬入枝肉 / 乳牛総数（同じ表：取扱頭数(頭)・取扱頭数構成比(％)・取扱重量(kg)・取扱重量構成比(％)・枝肉・部分肉取扱金額(円)・枝肉・部分肉取扱金額構成比(％)・副生物等取扱金額合計(円)・副生物等内臓取扱金額(円)）
- 補助金等交付団体 / 補助金等交付団体うち交付額2,000万円以上 / 出資団体 / 公の施設の指定管理者 / 合計（同じ表：監査対象団体数・監査実施団体数・実施率）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | account | 全会計 / 一般会計 / 特別会計母子父子福祉 / 特別会計中小企業 / 特別会計と場 / 特別会計都営住宅 / 特別会計用地 / 特別会計臨海基盤 | 平成26年度末現在高（円）・平成27年度起債額（円）・平成27年度元金償還額（円）・平成27年度末現在高（円）・平成28年度支払予定額元金上期（円）・平成28年度支払予定額元金下期（円）・平成28年度支払予定額利子上期（円）・平成28年度支払予定額利子下期（円） | pendata.metro.tokyo.lg.jp/zaimu/R3/genzaidakasirabe_5_27.csv |

## G157　b012「名称_カナ」（22 列：org 21・address 1）

多いほうの org の例：

- シタマチコドモショクドウミライ / シタマチコドモショクドウサクラ / ユニバーサルスペースサクラ / ヨミセドオリイコイノイエ / キッズカフェ / マナビブコドモショクドウ / モグモグコドモショクドウ（同じ表：全国地方公共団体コード・ID・都道府県・市区町村名・名称・設置目的・実施支援の主な区分・方書）
- エビスジモトコドモショクドウ / カゲオカノイエコドモショクドウ / パールコドモテーブルカツドウ / ミートザオヤツ / ハセコセイカツガッコウコドモショク / リフレッシュヒカワコドモショクドウ / コドモリョウリキョウシツ / シブヤセンターガイコドモショクドウ（同じ表：全国地方公共団体コード・都道府県・市区町村名・名称・設置目的・開催日・開催開始時間・開催終了時間）
- アラカワクリツミナミセンジュトショカン / アラカワクリツオグトショカン / アラカワクリツマチヤトショカン / アラカワクリツニッポリトショカン / アラカワクリツミナミセンジュトショカンシオイリトショサービスステーション / アラカワクリツニッポリトショカンカンムリシンドウトショサービスステーション / アラカワクリツユイノモリアラカワ（同じ表：全国地方公共団体コード・地方公共団体名・名称・名称_英字・名称_通称・POIコード・建物名等(方書)・高度の種別）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 9 | address | エドトウキョウタテモノエン / トウキョウトシャシンビジュツカン / トウキョウトゲンダイビジュツカン / トウキョウブンカカイカン / トーキョーアーツアンドスペースホンゴウ / オオイズミチュウオウコウエン / キヌタコウエン / キバコウエン | 都道府県コード又は市区町村コード・都道府県名・名称・POIコード・方書・利用可能曜日・開始時間・終了時間 | .metro.tokyo.lg.jp/suisyoudataset/130001_public_facility.csv |

## G158　b012「実施支援の主な区分」（2 列：category 1・text 1）

多いほうの category の例：

- 学習支援;フードパントリー / 学習支援;フードパントリー / 学習支援 / 学習支援;フードパントリー / フードパントリー / 学習支援 / 該当なし（同じ表：全国地方公共団体コード・ID・都道府県・市区町村名・名称・名称_カナ・設置目的・方書）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text |  /  /  / 食事提供、エンタメコンテンツ提供 /  /  /  / 生活相談・学習支援 | 全国地方公共団体コード・都道府県・市区町村名・名称・名称_カナ・設置目的・方書・法人番号 | tokyo.lg.jp/katsushika/131229_katsushikaku_kodomosyokudo.csv |

## G159　b012「名称_英語」（2 列：address 1・org 1）

多いほうの address の例：

- cocobunji Plaza / transportation square of Kokubunji station North Exit / square of Kokubunji station South Exit / Keyaki park / Kubo-Higashi park / Kitamachi park / cocobunji Plaza / Musashi Kokubunji Temple Remains Museum（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・建物名等(方書)・設置者・内線番号）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Izumitamagawa public toiret / Nishigawara Park / Nishigawara Nature Park / Maehara Park / Komae City Office / Komae Central Civic Hall / Nishigawara Civic Hall / Itopia Center | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・設置位置・高度の種別・高度の値 | ww.opendata.metro.tokyo.lg.jp/komae/132195_public_toilet.csv |

## G160　b012「Title」（2 列：org 1・text 1）

多いほうの org の例：

- Cairns Housing Service Centre, Queensland Government Service / Thursday Island Hub Tenancy Services, First Nations Housing / Mackay Housing Service Centre / Bundaberg Housing Service Centre / Maryborough Housing Service Centre / Ipswich Housing Service Centre / Fortitude Valley Housing Service Centre / Buranda Housing Service Centre（同じ表：Suburb・Fax・Opening hours）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | Overall External Financing Request Rate and Reason for Not S / Provider of External Financing / Debt Financing / Debt Financing by Instrument type / Amount of Debt Financing Requested and Authorized / Debt Financing Terms and Conditions / Reasons Given by Credit Provider for Turning Down Debt Finan / Intended Use of Lease Financing | Table・Survey question・Notes | 91b0-7bc33e24f138/download/2011_sfgsme-efcpme_tables_eng.csv |

## G161　b012「VALUE」（8 列：quantity 7・amount 1）

多いほうの quantity の例：

- 8 / 20 / 19 / 11 / 81 / 18 / 31 / 15（同じ表：STATISTIC・Statistic・TLIST(A1)・Year・C02451V02968・Administrative County・UNIT）
- 86 / 85 / 85 / 85 / 56 / 56 / 56 / 56（同じ表：STATISTIC・Statistic Label・YEAR・Year・HOSPSECTOR・Sector・HOSPTYPE・Type of hospital）
- 90 / 87 / 238 / 90 / 218 / 110 / 82 / 75（同じ表：STATISTIC・Statistic・TLIST(A1)・Year・C01947V02657・Local Authority・UNIT）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 7 | amount | 14725 / 17149 / 30076 / 37796 / 48414 / 45361 / 45699 / 41702 | STATISTIC・Statistic・TLIST(Q1)・Quarter・C02343V02817・Area・UNIT | pi.restful/PxStat.Data.Cube_API.ReadDataset/HSQ06/CSV/1.0/en |

## G162　b012「AREA」（2 列：id 1・address 1）

多いほうの id の例：

- 3 / 6 / 7 / 4 / 2 / 1 / 4 / 4（同じ表：PROV・LANG・Q1・Q2・Q3M1・Q3M2・Q3M3・Q4M1）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | Fremantle; Beaconsfield; South Fremantle; White Gum Valley; / Harvey; Eaton; Australind; Brunswick; Waroona / Fremantle / Coogee; Fremantle; Yangebup; Bibra Lake; Beaconsfield; Coolb / Kalgoorlie / Dowerin; Northam; Goomalling; Wongan Hills / Helena Valley; Gooseberry Hill; Lesmurdie; Kalamunda; Maida / Melville | TITLE・DATES・FORMERTITLE・LATERTITLE | 0daf9-193e-4748-9aee-29bc50c909c4/download/newspapers-wa.csv |

## G163　b013「Route」（2 列：id 1・category 1）

多いほうの id の例：

- DUD-OOL / AKL-MEL / AKL-SYD / TBU-AKL-SYD / ADL-MEL-HKG / BNE-SIN-ROM / OOL-DUD / PER-HKT-BKK（同じ表：Month・In_Out・Australian_City・International_City・Airline・Port_Country・Port_Region・Service_Country）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Ayers Rock - Cairns / Hamilton Island - Sydney / Karratha - Perth / Adelaide - Perth / Launceston - Sydney / Melbourne - Sydney / Adelaide - Perth / Cairns - Sydney | Year・Month・YearMonth・Port1・Port2・$Value・$Real | 84-4416-b3d6-6a669fc4e423/download/faresforbi_excel_0926.csv |

## G164　b013「ID」（8 列：id 7・category 1）

多いほうの id の例：

- 00142341 / 00142463 / 00232166 / 00259897 / 00142464 / 00259709 / 00229227 / 00229285（同じ表：site・area・built・diam_mm・length_m・mat_desc・plot）
- 663 / 664 / 666 / 668 / 669 / 670 / 671 / 672（同じ表：No.・Anticipatory Notice Date Reference・Previous_Project_Area・Varied-Project_Area・Previous_Service_Area_ Identifier・Varied_Service_ Area_Identifier・Estimated_ Completion_Date・Previous_Latlong）
- 1 / 2 / 19 / 3 / 4 / 16 / 18 / 14（同じ表：ܓx・ox・ǗID・ꖼ・ݒn）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 7 | category | Leinster Outer Orbital Route / Leinster Outer Orbital Route / Leinster Outer Orbital Route / Leinster Outer Orbital Route / National Road Objectives / Leinster Outer Orbital Route / National Road Objectives / Local Aligment & Width Improvements | OBJECTID・SHAPE__Length | 5f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1 |

## G165　b013「LGA」（5 列：address 4・category 1）

多いほうの address の例：

- Bayside (C) / Manningham / Stonnington (C); Glen Eira (C) / Boroondara (C) / Melbourne (C) / Kingston (C) / Maroondah (C) / Manningham (C)（同じ表：Suburb・State・Business Category・Region）
- Canterbury-Bankstown Council / Northern Beaches Council / Council of the City of Sydney / Sutherland Shire Council / Bayside Council / Lane Cove Municipal Council / Fairfield City Council / Albury City Council（同じ表：Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・SA2 Band・Subject to Cap）
- Delatite / Campaspe / Strathbogie / Frankston / Port Phillip / Alpine (S) / Yarra (C) / Wellington（同じ表：Suburb・State・Business Category・Region）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | No / No / No / No / No / No / No / No | Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・SA2 Band・Subject to Cap | -a603-c2aa4914bc62/download/find-my-lia-band-6-june-2021.csv |

## G166　b013「Region」（9 列：address 8・category 1）

多いほうの address の例：

- Southern Metropolitan Region / Eastern Metro / Southern Metropolitan Region / Eastern Metropolitan Region / North and West Metropolitan Region / Southern Metropolitan Region / Eastern Metropolitan Region / Eastern Metropolitan Region（同じ表：Suburb・State・Business Category・LGA）
- British Columbia / Alberta / Saskatchewan / Manitoba / Western Canada（同じ表：Value of Business Expenditures on Resear）
- Coffs Harbour City Council / Northern Beaches Council / Sutherland Shire Council / Sutherland Shire Council / North Sydney Council / Woollahra Municipal Council / Northern Beaches Council / Armidale Regional Council（同じ表：Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・SA2 Band・Subject to Cap）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Country | Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・SA2 Band・Subject to Cap | -8a8e-d3b9b145194b/download/find-my-lia-band-10-may-2021.csv |

## G167　b013「Location」（3 列：address 2・category 1）

多いほうの address の例：

- Hazardous Waste Sheds / Stores / Workshops / Bead Blast Shop / Composite Shop / Training Center / Pump House / Helicopter Shop（同じ表：Year・Number of Spills・Volume (L)）
- Bladin Street Reserve Laverton / Cyril Curtain Reserve, Williamstown / Pipeline Reserve / A. B. Shaw Reserve Altona Meadows / P.A. Burns Reserve Altona / S.J. Clement Reserve / Edwards Reserve, South Kingsville / Donald McClean Reserve, Spotswood（同じ表：Id・Dog_Restrictions）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | Boundary / Boundary / Boundary / Boundary / Boundary / Boundary / Boundary / Boundary | Park・PointID・Year・Month・Day・Species・Time.1st.Detected・#detected_0-3m20s | wnload/kootenay_np_forest_and_tundra_birds_knp_2007-2025.csv |

## G168　b013「SA2 Band」（2 列：category 1・address 1）

多いほうの category の例：

- 2 / 1 / 2 / 1 / 2 / 1 / 3 / 2（同じ表：Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・Subject to Cap・LGA）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | Coffs Harbour - North / Balgowlah - Clontarf - Seaforth / Cronulla - Kurnell - Bundeena / Cronulla - Kurnell - Bundeena / North Sydney - Lavender Bay / Rose Bay - Vaucluse - Watsons Bay / Manly Vale - Allambie Heights / Armidale | Data as of・Licence No・Start Date・Trading Status・Type・Filter Category・Subject to Cap・LGA | -a603-c2aa4914bc62/download/find-my-lia-band-6-june-2021.csv |

## G169　b013「species」（4 列：other 2・category 2）

多いほうの other の例：

- Excelsior 'Aurea' / Raywood / Not Specified / Sp. / Pennsylvanica 'Cimmzam' / Ussuriensis / Sp. / Raywood（同じ表：lat・lon・genus・dbh・dbh_min・dbh_max・crown・crown_min）
- Eucalyptus maculata / Eucalyptus maculata / Melaleuca stypheloides / Cedrus deodara / Eucalyptus citriodora / Acacia floribunda / Allocasuarina littoralis / Eucalyptus citriodora（同じ表：date1・house・str_type・suburb・pcode・alphatree・height・dbh）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | horse rider / horse rider / horse rider / coyote / unknown / grizzly bear / hiker / grizzly bear | location.id・location・park・trailtype・datestart・dateimage・timeimage・total | load/yoho_np_multispecies_mammal_occupancy_ynp_2010-2025.csv |
| 4 | category | grizzly bear / coyote / bald eagle / common raven / coyote / white-tailed deer / white-tailed deer / white-tailed deer | location.id・location・park・trailtype・datestart・dateimage・timeimage・total | /kootenay_np_multispecies_mammal_occupancy_knp_2010-2025.csv |

## G170　b013「dbh」（2 列：other 1・category 1）

多いほうの other の例：

- 15.5 / 25.5 / 15.5 / 5 / 5 / 15.5 / 5 / 15.5（同じ表：lat・lon・genus・species・dbh_min・dbh_max・crown・crown_min）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | 500 - 1000mm / 100 - 250mm / 100 - 250mm / 1000mm+ / 100 - 250mm / 250 - 500mm / 100 - 250mm / 100 - 250mm | date1・house・str_type・suburb・pcode・alphatree・species・height | -4ed7-9d84-ea318302b881/download/manningham_street_trees.csv |

## G171　b013「location」（2 列：address 1・category 1）

多いほうの address の例：

- charles street / smith street / david street / stewart street / stewart street / high street / milton street / milton street（同じ表：ref・species・common・height・crown・maturity・locality・lat）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | street / street / street / street / street / street / street / street | lat・lon・species・common・dbh・crown・crown_min・crown_max | 9b-af5c-9b31a6848455/download/city-of-port-phillip-trees.csv |

## G172　b013「Sector」（3 列：id 2・category 1）

多いほうの id の例：

- 12263 / 12281 / 12281 / 12230 / 12261 / 12263 / 12240 / 12182（同じ表：Financial Year・Type of flow・Country・Expense $'000）
- 23340 / 25010 / 24040 / 24040 / 24040 / 23182 / 23182 / 25010（同じ表：Financial Year・Type of flow・Country・Expense $'000）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | Credit Institutions and Central Bank / Credit Institutions and Central Bank / General Government / General Government / General Government / General Government / Insurance Corporations / Insurance Corporations | Reporting Period・Euro Millions | 575-a2a7-bcdece7f3433/download/irish-gov-bonds-1969-2001.csv |

## G173　b014「名称」（7 列：org 4・address 2・text 1）

多いほうの org の例：

- 西多摩保健所 / 南多摩保健所 / 多摩立川保健所 / 多摩府中保健所 / 多摩小平保健所（同じ表：担当地域）
- 天王洲公園 / 八潮北公園 / 品川南ふ頭公園 / しながわ区民公園 / 子供の森公園 / 鮫洲運動公園 / 東品川公園 / しながわ中央公園（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_英字・POIコード・利用可能曜日・開始時間）
- 羽村東小学校 / 羽村西小学校 / 富士見小学校 / 栄小学校 / 松林小学校 / 小作台小学校 / 武蔵野小学校 / 羽村第一中学校（同じ表：全国地方公共団体コード・ID・名称_カナ・標高・市区町村コード・地方公共団体名・災害種別_洪水・災害種別_崖崩れ、土石流及び地滑り）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | address | 千早四丁目アパート(1･2号棟) / 千川二丁目アパート / 要町三丁目アパート / 高松三丁目アパート / 上池袋二丁目アパート / 高松三丁目第2アパート(1・2号棟) / 高松三丁目第3アパート / 長崎六丁目アパート(3・10号棟) | 全国地方公共団体コード・面積・間取り・建設年度・管理戸数・一般・主な線・主な駅 | a.metro.tokyo.lg.jp/toshima/131164_toshimaku_koueijutaku.csv |
| 4 | text | ぎかいのトビラ第147号 / ぎかいのトビラ第146号 / ぎかいのトビラ第145号 / ぎかいのトビラ第144号 / ぎかいのトビラ第143号 / ぎかいのトビラ第142号 / ぎかいのトビラ第141号 / ぎかいのトビラ第140号 | 全国地方公共団体コード・地方公共団体名・号数・発行年月・発行元 | ta.metro.tokyo.lg.jp/hamura/132276_hamurashi_gikaidayori.csv |
| 6 | address | 三矢会館 / 小作本町会館 / 富士見平会館 / 緑ヶ丘会館 / 小作台西会館 / 消費生活センター / 福祉事務所 / 羽村市福祉センター | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・POIコード | opendata.metro.tokyo.lg.jp/hamura/132276_public_facility.csv |

## G174　b014「名称_カナ」（3 列：org 2・address 1）

多いほうの org の例：

- テンノウズコウエン / ヤシオキタコウエン / シナガワミナミフトウコウエン / シナガワクミンコウエン / コドモノモリコウエン / サメズウンドウコウエン / ヒガシシナガワコウエン / シナガワチュウオウコウエン（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_英字・POIコード・利用可能曜日・開始時間）
- ハムラヒガシショウガッコウ / ハムラニシショウガッコウ / フジミショウガッコウ / サカエショウガッコウ / ショウリンショウガッコウ / オザクダイショウガッコウ / ムサシノショウガッコウ / ハムラダイイチチュウガッコウ（同じ表：全国地方公共団体コード・ID・名称・標高・市区町村コード・地方公共団体名・災害種別_洪水・災害種別_崖崩れ、土石流及び地滑り）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | address | ミツヤカイカン / オザクホンマチカイカン / フジミダイラカイカン / ミドリガオカカイカン / オザクダイニシカイカン / ショウヒセイカツセンター / フクシジムショ / ハムラシフクシセンター | 全国地方公共団体コード・ID・地方公共団体名・名称・POIコード | opendata.metro.tokyo.lg.jp/hamura/132276_public_facility.csv |

## G175　b014「operator」（2 列：org 1・category 1）

多いほうの org の例：

- Board of Directors / Yarra City Council / Private / Parent committee / Presbyterian Church / Yarra City Council / Brotherhood of St Laurence / Committee Uniting Church N.W.C.S（同じ表：licence_capacity・ref）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | southern grampians shire council / southern grampians shire council / southern grampians shire council / southern grampians shire council / southern grampians shire council / southern grampians shire council / private / southern grampians shire council | lat・lon・wheelchair | -89eaeae7f611/download/southern-grampians-public-toilets.csv |

## G176　b014「LGA」（5 列：address 4・org 1）

多いほうの address の例：

- Colac-Otway (S) / Wyndham (C); Moorabool (S); Melton (S) / Wangaratta (RC) / Macedon Ranges (S) / Kingston (C) / Moira (S) / Yarra Ranges (S) / Greater Geelong (C)（同じ表：Suburb・State・Business Category・Region）
- Whitehorse (C) / Greater Bendigo (C) / Macedon Ranges (S) / Whitehorse (C) / Ballarat (C) / Darebin (C) / Whitehorse (C) / Boroondara (C)（同じ表：Suburb・State・Business Category・Region）
- Surf Coast (S) / East Gippsland (S) / Indigo (S) / Greater Geelong (C) / Moreland (C) / Bayside (C) / Whitehorse (C) / Cardinia（同じ表：Suburb・State・Business Category・Region）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 5 | org | Wyndham City Council / Wyndham City Council / Wyndham City Council / Wyndham City Council / Wyndham City Council | _id・Library・Long・Lat・PublicAccessFloorSpace・OpeningHours(perweek) | 7e260a36-50f0-4e0b-99e9-18734759785c/download/branchinfo.csv |

## G177　b014「location」（6 列：address 4・other 2）

多いほうの address の例：

- Village Green Reserve (Kialla) / John Pick Reserve (Shepparton) / Waverley Avenue (Merrigum) / Wyndham Street (Shepparton) / Wyndham Street (Shepparton) / Knight Street (Shepparton) / Poplar (Urban) Avenue (Shepparton) / Welsford Street (Shepparton)（同じ表：ref・material・type・number_of・capacity）
- Behind Grant Ave / Golf course walkways / Altona Golf Course / Newport Lakes Walk / Newport Lakes Walk / Cherry lake walk / McCormack Park / Bay West Trail（同じ表：site・type・maint_auth・area_sqm・length_m・width_m・clearance・span）
- Highfield Rd, Doncaster East / George St, Doncaster East / Council St, Doncaster / Springvale Rd, Donvale / Fullwood Parade, Doncaster East / Park Road, Park Orchards / Serpells Rd, Templestowe / King St, Templestowe（同じ表：between_・school・mapref・hours・lat）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 4 | other | -37.841954, 144.935296 / -37.824088, 144.970085 / -37.809216, 144.955223 / -37.820715594013, 144.969164729118 / -37.802129, 144.96677 / -37.809072, 144.972762 / -37.820836, 144.962266 / -37.836323, 144.975162 | station_id・rental_method・capacity・lat・lon | pi/v2/catalog/datasets/bike-share-dock-locations/exports/csv |
| 5 | other | -37.79303373, 144.973391203 / -37.8153389, 144.954698371 / -37.82166549, 144.964566826 / -37.81403196, 144.96103479 / -37.81472467, 144.96581017 / -37.8091536, 144.968590037 / -37.82020482, 144.955152428 / -37.8091842, 144.970732474 | census_year・property_id・base_property_id・clue_small_area・number_of_patrons | alog/datasets/bars-and-pubs-with-patron-capacity/exports/csv |

## G178　b014「Value」（3 列：rate 2・amount 1）

多いほうの rate の例：

- 99.91 / 99.98 / 99.939 / 99.949 / 99.966 / 99.881 / 99.825 / 100（同じ表：Fiscal Year・Fiscal Period・Month・Information Date・Branch・Service・Comments・Metric Type）
- 100 / 100 / 100 / 100 / 100 / 100 / 100 / 100（同じ表：Fiscal Year・Fiscal Period・Month・Date・Branch・Service・Metric Type）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | amount | 250.00 / 225.00 / 325.00 / 668.50 / 118.00 / 718.00 / 200.00 / 150.00 | Date Received・Reasons for accepting gift (what is the | fts-year-to-date-as-at-30-june-2026.csv?v=639220172201645992 |

## G179　b014「Title」（2 列：text 1・category 1）

多いほうの text の例：

- Daily Herald (Adelaide, SA : 1910 - 1924) / The Advertiser (Adelaide, SA : 1889 - 1931) / The Register (Adelaide, SA : 1901 - 1929) / Observer (Adelaide, SA : 1905 - 1931) / The Advertiser (Adelaide, SA : 1889 - 1931) / The Register (Adelaide, SA : 1901 - 1929) / Daily Herald (Adelaide, SA : 1910 - 1924) / The Advertiser (Adelaide, SA : 1889 - 1931)（同じ表：Heading・Category・Page・Date・TrovePageUrl・Illustrated・WordCount・Relevance）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Chief Agent / President & Chief Regional Executive (and CEO for corporate / Chief Agent / Chief Agent / Chief Agent / President & CEO / Chief Agent / Chief Agent | City・Province State・Authorized Insurance Classes | 0-47d4-aad2-144d69467824/download/who_we_regulate_fi_eng.csv |

## G180　b014「Comments」（3 列：text 2・category 1）

多いほうの text の例：

-  /  /  /  /  /  /  / （同じ表：Fiscal Year・Fiscal Period・Month・Information Date・Branch・Service・Value・Metric Type）
- No issues / One Isopropyl Alcohol. The labels are torn and worn out and / One Royco 950. The labels are torn and worn out and illegib / No issues / No issues / One Release Agent MS143H. Label was missing. /  / No spare face shield visor（同じ表：Date・Audit Area・Point of Inspection・Compliance Yes/No (1/0)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category |  /  /  /  /  /  /  /  | Fiscal Year・Fiscal Period・Month・Information Date・Branch・Service・SSC Client・Value | -a46d-79fe0c81e925/download/fixed-telephony-june-2025-en.csv |

