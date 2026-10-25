# ラベル用シート 001 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：分類
- 例1 値：8009001000 | 8005001000 | 8009001000 | 8004001000 | 8009004000
  - 同じ表の列：第1分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 対象, 開催日詳細

## g0002（1 列）
- 見出し：第1分類
- 例1 値：港区イベントカレンダー | 港区イベントカレンダー | 港区イベントカレンダー | 港区イベントカレンダー | 港区イベントカレンダー
  - 同じ表の列：分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 対象, 開催日詳細

## g0003（1 列）
- 見出し：第2分類
- 例1 値：地区指定なし | 芝地区 | 地区指定なし | 地区指定なし | 地区指定なし
  - 同じ表の列：分類, 第1分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 対象, 開催日詳細

## g0004（1 列）
- 見出し：開催日時
- 例1 値：2026年10月17日から2026年10月17日 | 2026年9月26日から2026年9月27日 | 2026年9月1日 | 2026年9月2日から2026年9月2日,2026年9月9日から2026年9月… | 2026年5月9日から2026年5月9日,2026年6月13日から2026年6…
  - 同じ表の列：分類, 第1分類, 第2分類, ページタイトル, 問い合わせ先1, 内容, 対象, 開催日詳細

## g0005（1 列）
- 見出し：ページタイトル
- 例1 値：郷土歴史館・東京海洋大学マリンサイエンスミュージアム連携事業 夏休み学習会-東… | 第3回港区役所ロビーコンサート | あなたの想い・活動をよりよいカタチにする&続けるためのコツ | がん制度大学「60歳以上のがん患者さんに知ってほしいがん制度」 | 芝の語り部と学ぶ!江戸城事件簿
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, 問い合わせ先1, 内容, 対象, 開催日詳細

## g0006（1 列）
- 見出し：問い合わせ先1
- 例1 値：赤坂地区総合支所まちづくり課土木担当 | 教育委員会事務局教育推進部生涯学習スポーツ振興課生涯学習係 | 赤坂地区総合支所まちづくり課土木担当 | みなと保健所健康推進課地域保健係 | 赤坂地区総合支所管理課青山保育園
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, ページタイトル, 内容, 対象, 開催日詳細

## g0007（1 列）
- 見出し：内容
- 例1 値：うた・手遊び・絵本から英語に触れて遊べる楽しい時間です。 親子で一緒に楽しみま… | こころの病気(アルコール依存症を含む)や認知症の早期発見・早期治療・対応の仕方… | 成年後見制度の概要・申し立て、成年後見人等の仕事内容について | 港区子ども家庭支援センターの臨床心理士海老澤先生に、お子さんの発達について相談… | 自死(自殺)で身近な人(家族や友人等)を亡くした人が、ありのままの思いを話し、…
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 対象, 開催日詳細

## g0008（1 列）
- 見出し：対象
- 例1 値：認知症のある人やその家族または認知症の予防等に関心のある人 | 小学生以上の区民 ※小学生は保護者同伴必須 | がん患者およびその家族 | どなたでも | 3歳以上の区民で、7人から20人以下のグループ(小学生以下は保護者同伴必須)
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 開催日詳細

## g0009（1 列）
- 見出し：開催日詳細
- 例1 値：8月2日(日曜)午後4時から | 令和8年7月27日(月曜日)10時から11時 | 令和8年7月16日(木曜日)11時から12時 | 令和8年9月16日(水曜日) 一部 開場時間:午前10時~正午、受付終了:午前… | 7月31日(金曜日) 14時00分~15時00分 ※中止のお知らせは、港区赤坂…
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 対象

## g0010（1 列）
- 見出し：定員
- 例1 値：40人(申込順) | 20人(申込順) | 30人(抽選) | 各回40人(先着) | 20人(抽選)
  - 同じ表の列：分類, 第1分類, 第2分類, 開催日時, ページタイトル, 問い合わせ先1, 内容, 対象

## g0011（2 列）
- 見出し：全国地方公共団体コード
- 例1 値：131091 | 131091 | 131091 | 131091 | 131091
  - 同じ表の列：地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日, 開始時間
- 例2 値：131164 | 131164 | 131164 | 131164 | 131164
  - 同じ表の列：地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0012（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日, 開始時間

## g0013（1 列）
- 見出し：施設名称
- 例1 値：区民活動交流施設 | 大崎第一区民集会所 | 北品川児童センター | 品川第二区民集会所 | 区民活動交流施設
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日, 開始時間

## g0014（1 列）
- 見出し：施設名称_カナ
- 例1 値：クミンカツドウコウリュウシセツ | エバラブンカセンター | クミンカツドウコウリュウシセツ | オオサキダイニクミンシュウカイジョ | シナガワダイイチクミンシュウカイジョ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日, 開始時間

## g0015（1 列）
- 見出し：施設名称_英字
- 例1 値：gotanda culture center
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, 利用可能曜日, 開始時間

## g0016（1 列）
- 見出し：スペース名称
- 例1 値：第2集会室 | 第4集会室(和室) | 第1集会室 | スポーツ室 | 第3多目的室
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, 利用可能曜日, 開始時間

## g0017（1 列）
- 見出し：スペース名称_カナ
- 例1 値：ワシツイチ | ユウギシツ | ダイヨンカイギシツ | ダイニグループシツ | ダイサンシュウカイシツ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, 利用可能曜日, 開始時間

## g0018（1 列）
- 見出し：利用可能曜日
- 例1 値：月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 開始時間

## g0019（1 列）
- 見出し：開始時間
- 例1 値：09:00 | 09:00 | 09:00 | 09:00 | 09:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日

## g0020（1 列）
- 見出し：終了時間
- 例1 値：21:00 | 21:30 | 21:30 | 21:30 | 21:30
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日

## g0021（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都豊島区 | 東京都豊島区 | 東京都豊島区 | 東京都豊島区 | 東京都豊島区
  - 同じ表の列：全国地方公共団体コード, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0022（1 列）
- 見出し：施設名称
- 例1 値：としま区民センター | 豊島区立舞台芸術交流センター | としま区民センター | 豊島区立芸術文化劇場 | 豊島区立池袋西口公園野外劇場
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0023（1 列）
- 見出し：施設名称_カナ
- 例1 値：トシマクリツゲイジュツブンカゲキジョウ | トシマクミンセンター | トシマクリツイケブクロニシグチコウエンヤガイゲキジョウ | トシマクミンセンター | トシマクリツブタイゲイジュツコウリュウセンター
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0024（1 列）
- 見出し：施設名称_英字
- 例1 値：Toshima Civic Center | Toshima Arts and Culture Theatre | Toshima Civic Center
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0025（1 列）
- 見出し：スペース名称
- 例1 値：劇場 | 小ホール | 舞台棟 | 多目的ホール | 劇場
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0026（1 列）
- 見出し：スペース名称_カナ
- 例1 値：ゲキジョウ | タモクテキホール | ショウホール | ゲキジョウ | ブタイトウ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_英字, 建物名等(方書)

## g0027（1 列）
- 見出し：スペース名称_英字
- 例1 値：Theatre
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 建物名等(方書)

## g0028（1 列）
- 見出し：建物名等(方書)
- 例1 値：ライズアリーナビル2階
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0029（1 列）
- 見出し：高度の種別
- 例1 値：階数 | 階数 | 階数
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0030（2 列）
- 見出し：和暦
- 例1 値：R6 | H29 | H22 | R6 | R6
  - 同じ表の列：西暦, 生物化学的酸素要求量(BOD)(mg/…, 溶存酸素量(DO)(mg/l), 浮遊物質(SS)(mg/l), 水素イオン濃度(pH)(ph)
- 例2 値：H27 | H28 | R5 | H29 | H30
  - 同じ表の列：西暦, 総数, 市長提出, 議員提出, 選挙等, 報告

## g0031（1 列）
- 見出し：西暦
- 例1 値：12月 | 10月 | 11月 | 2012.0 | 2月
  - 同じ表の列：和暦, 生物化学的酸素要求量(BOD)(mg/…, 溶存酸素量(DO)(mg/l), 浮遊物質(SS)(mg/l), 水素イオン濃度(pH)(ph)

## g0032（1 列）
- 見出し：生物化学的酸素要求量(BOD)(mg/l)
- 例1 値：1.6 | 1.6 | 1.7 | 1.7 | 1.5
  - 同じ表の列：和暦, 西暦, 溶存酸素量(DO)(mg/l), 浮遊物質(SS)(mg/l), 水素イオン濃度(pH)(ph)

## g0033（1 列）
- 見出し：溶存酸素量(DO)(mg/l)
- 例1 値：7.7 | 8.8 | 9 | 9.4 | 10
  - 同じ表の列：和暦, 西暦, 生物化学的酸素要求量(BOD)(mg/…, 浮遊物質(SS)(mg/l), 水素イオン濃度(pH)(ph)

## g0034（1 列）
- 見出し：浮遊物質(SS)(mg/l)
- 例1 値：3 | 2 | 2 | 2 | 2
  - 同じ表の列：和暦, 西暦, 生物化学的酸素要求量(BOD)(mg/…, 溶存酸素量(DO)(mg/l), 水素イオン濃度(pH)(ph)

## g0035（1 列）
- 見出し：水素イオン濃度(pH)(ph)
- 例1 値：7.4 | 7.5 | 7.4 | 7.4 | 8.1
  - 同じ表の列：和暦, 西暦, 生物化学的酸素要求量(BOD)(mg/…, 溶存酸素量(DO)(mg/l), 浮遊物質(SS)(mg/l)

## g0036（1 列）
- 見出し：site_id
- 例1 値：GD15 | GD05 | GD01 | B029 | GC41
  - 同じ表の列：observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, depth_of_observation, drill_type, date_drilled

## g0037（1 列）
- 見出し：observation_date
- 例1 値：1984-12-03 | 1984-11-06 | 1978-10-19 | 1986-12-10 | 1984-11-28
  - 同じ表の列：site_id, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, depth_of_observation, drill_type, date_drilled

## g0038（1 列）
- 見出し：observation_date_year
- 例1 値：1985 | 1983 | 1984 | 1985 | 1986
  - 同じ表の列：site_id, observation_date, observation_date_mo…, observation_date_day, temperature, depth_of_observation, drill_type, date_drilled

## g0039（1 列）
- 見出し：observation_date_month
- 例1 値：11 | 11 | 10 | 11 | 11
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_day, temperature, depth_of_observation, drill_type, date_drilled

## g0040（1 列）
- 見出し：observation_date_day
- 例1 値：2 | 14 | 2 | 10 | 6
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, temperature, depth_of_observation, drill_type, date_drilled

## g0041（1 列）
- 見出し：temperature
- 例1 値：-32.64 | -34.22 | -44.68 | -23.73 | -31.4
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, depth_of_observation, drill_type, date_drilled

## g0042（1 列）
- 見出し：depth_of_observation
- 例1 値：20 | 20 | 15 | 20 | 18.8
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, drill_type, date_drilled

## g0043（1 列）
- 見出し：drill_type
- 例1 値：STEAM | PICO | STEAM | PICO | STEAM
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, depth_of_observation, date_drilled

## g0044（1 列）
- 見出し：date_drilled
- 例1 値：1983-10-24 | 1983-10-14 | 1983-11-04 | 1983-10-16 | 1983-04-13
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, depth_of_observation, drill_type

## g0045（1 列）
- 見出し：days_between_drilling_and_measurement
- 例1 値：0.67 | 82.29 | 1.79 | 1.88 | 23
  - 同じ表の列：site_id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, temperature, depth_of_observation, drill_type

## g0046（2 列）
- 見出し：Month
- 例1 値：Sep-03 | Dec-03 | Sep-03 | Sep-03 | Sep-03
  - 同じ表の列：In_Out, Australian_City, International_City, Airline, Route, Port_Country, Port_Region, Service_Country
- 例2 値：Jul-91 | Sep-91 | Feb-91 | Jan-92 | Apr-91
  - 同じ表の列：Airline, Service_Country, Flights_In, Passengers_In, Seats_In, Flights_Out, Passengers_Out, Seats_Out

## g0047（1 列）
- 見出し：In_Out
- 例1 値：I | I | O | I | I
  - 同じ表の列：Month, Australian_City, International_City, Airline, Route, Port_Country, Port_Region, Service_Country

## g0048（1 列）
- 見出し：Australian_City
- 例1 値：Brisbane | Gold Coast | Brisbane | Cairns | Sydney
  - 同じ表の列：Month, In_Out, International_City, Airline, Route, Port_Country, Port_Region, Service_Country

## g0049（1 列）
- 見出し：International_City
- 例1 値：Auckland | Singapore | Auckland | Osaka | Dubai
  - 同じ表の列：Month, In_Out, Australian_City, Airline, Route, Port_Country, Port_Region, Service_Country

## g0050（1 列）
- 見出し：Airline
- 例1 値：Qantas Airways | Qantas Airways | Qantas Airways | Qantas Airways | Garuda Indonesia
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Route, Port_Country, Port_Region, Service_Country

## g0051（1 列）
- 見出し：Route
- 例1 値：BNE-VLI | HKG-SYD | SYD-SIN-LON | MEL-SYD-HKG | TBU-AKL-SYD
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Airline, Port_Country, Port_Region, Service_Country

## g0052（1 列）
- 見出し：Port_Country
- 例1 値：Indonesia | USA | Singapore | Thailand | Hong Kong (SAR)
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Airline, Route, Port_Region, Service_Country

## g0053（1 列）
- 見出し：Port_Region
- 例1 値：Islands | New Zealand | New Zealand | SE Asia | NE Asia
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Airline, Route, Port_Country, Service_Country

## g0054（2 列）
- 見出し：Service_Country
- 例1 値：China | Japan | USA | China | Singapore
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Airline, Route, Port_Country, Port_Region
- 例2 値：Brunei | Canada | Fiji | China | Fiji
  - 同じ表の列：Month, Airline, Flights_In, Passengers_In, Seats_In, Flights_Out, Passengers_Out, Seats_Out

## g0055（1 列）
- 見出し：Service_Region
- 例1 値：Africa | NE Asia | SE Asia | New Zealand | NE Asia
  - 同じ表の列：Month, In_Out, Australian_City, International_City, Airline, Route, Port_Country, Port_Region

## g0056（1 列）
- 見出し：Airline
- 例1 値：Northwest Airlines | Continental Airlines | Qantas Airways | Korean Air | Thai Airways International
  - 同じ表の列：Month, Service_Country, Flights_In, Passengers_In, Seats_In, Flights_Out, Passengers_Out, Seats_Out

## g0057（1 列）
- 見出し：Flights_In
- 例1 値：22 | 4 | 174 | 13 | 26
  - 同じ表の列：Month, Airline, Service_Country, Passengers_In, Seats_In, Flights_Out, Passengers_Out, Seats_Out

## g0058（1 列）
- 見出し：Passengers_In
- 例1 値：8 | 3777 | 3699 | 14741 | 8143
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Seats_In, Flights_Out, Passengers_Out, Seats_Out

## g0059（1 列）
- 見出し：Seats_In
- 例1 値：424 | 3744 | 24890 | 288 | 19719
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Passengers_In, Flights_Out, Passengers_Out, Seats_Out

## g0060（1 列）
- 見出し：Flights_Out
- 例1 値：0 | 4 | 48 | 84 | 0
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Passengers_In, Seats_In, Passengers_Out, Seats_Out

## g0061（1 列）
- 見出し：Passengers_Out
- 例1 値：2922 | 759 | 1687 | 2378 | 2688
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Passengers_In, Seats_In, Flights_Out, Seats_Out

## g0062（1 列）
- 見出し：Seats_Out
- 例1 値：0 | 350 | 7451 | 2216 | 18384
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Passengers_In, Seats_In, Flights_Out, Passengers_Out

## g0063（29 列）
- 見出し：Year
- 例1 値：1991 | 1991 | 1991 | 1991 | 1992
  - 同じ表の列：Month, Airline, Service_Country, Flights_In, Passengers_In, Seats_In, Flights_Out, Passengers_Out
- 例2 値：2020 | 2025 | 2016 | 2021 | 2020
  - 同じ表の列：tax_type_or_activit…, gross_receipts__m, net_receipts__m, properties_returned…, number_of_contracts, value_of_contracts_…, number_of_payments, value_of_payments__b

## g0064（13 列）
- 見出し：ID
- 例1 値：00270426 | 00099499 | 00142273 | 00141743 | 00102377
  - 同じ表の列：site, area, built, diam_mm, length_m, mat_desc, plot
- 例2 値：666 | 669 | 670 | 664 | 672
  - 同じ表の列：No., Anticipatory Notice…, Previous_Project_Ar…, Varied-Project_Area, Previous_Service_Ar…, Varied_Service_ Are…, Estimated_ Completi…, Previous_Latlong

## g0065（1 列）
- 見出し：site
- 例1 値：Chase Boulevard | Echo Place | Peel Street North | Marshall Road | Aberdeen Street
  - 同じ表の列：ID, area, built, diam_mm, length_m, mat_desc, plot

## g0066（1 列）
- 見出し：area
- 例1 値：No Code Allocated | No Code Allocated | Miners Rest | Lucas | Alfredton
  - 同じ表の列：ID, site, built, diam_mm, length_m, mat_desc, plot

## g0067（1 列）
- 見出し：built
- 例1 値：2013/09/ | 1971/07/ | 2005/05/ | 1980/07/ | 2012/08/
  - 同じ表の列：ID, site, area, diam_mm, length_m, mat_desc, plot

## g0068（1 列）
- 見出し：diam_mm
- 例1 値：300 | 300 | 450 | 900 | 750
  - 同じ表の列：ID, site, area, built, length_m, mat_desc, plot

## g0069（1 列）
- 見出し：length_m
- 例1 値：84.00 | 11.00 | 12.39 | 40.00 | 84.53
  - 同じ表の列：ID, site, area, built, diam_mm, mat_desc, plot

## g0070（1 列）
- 見出し：mat_desc
- 例1 値：Earthenware | Earthenware | Black Max | Black Max | Earthenware
  - 同じ表の列：ID, site, area, built, diam_mm, length_m, plot

## g0071（1 列）
- 見出し：plot
- 例1 値：520008 | 520008 | 520019 | 520006 | 520015
  - 同じ表の列：ID, site, area, built, diam_mm, length_m, mat_desc

## g0072（1 列）
- 見出し：carrying
- 例1 値：Stormwater | Stormwater | Stormwater | Stormwater | Stormwater
  - 同じ表の列：material, form, length_mm, width_mm, built, ref

## g0073（2 列）
- 見出し：material
- 例1 値：Unknown | Unknown | Unknown | Unknown | Unknown
  - 同じ表の列：carrying, form, length_mm, width_mm, built, ref
- 例2 値：Timber | Timber | Timber | Timber | Timber
  - 同じ表の列：ref, num_of, accessible

## g0074（1 列）
- 見出し：form
- 例1 値：Circular pipe | Circular pipe | Circular pipe | Circular pipe | Circular pipe
  - 同じ表の列：carrying, material, length_mm, width_mm, built, ref

## g0075（1 列）
- 見出し：length_mm
- 例1 値：19000 | 3000 | 9000 | 6000 | 37000
  - 同じ表の列：carrying, material, form, width_mm, built, ref

## g0076（1 列）
- 見出し：width_mm
- 例1 値：225 | 300 | 225 | 375 | 225
  - 同じ表の列：carrying, material, form, length_mm, built, ref

## g0077（1 列）
- 見出し：built
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：carrying, material, form, length_mm, width_mm, ref

## g0078（4 列）
- 見出し：ref
- 例1 値：290 | 943 | 189 | 945 | 166
  - 同じ表の列：carrying, material, form, length_mm, width_mm, built
- 例2 値：1 | 2 | 7 | 3 | 5
  - 同じ表の列：Doc, Heading, Desc, CY_Exp, PY_Exp, OBJECTID

## g0079（1 列）
- 見出し：Quantity
- 例1 値：Information and advice provided through… | Information and advice provided through… | Transactions undertaken: registration a… | Inspections, compliance monitoring and … | Transactions undertaken: Residential Te…
  - 同じ表の列：2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0080（1 列）
- 見出し：2012-13 Actual
- 例1 値：9,749 | 406,535 | 61,378 | 84,659 | 409,936
  - 同じ表の列：Quantity, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0081（1 列）
- 見出し：2013-14 Actual
- 例1 値：67,520 | 133,729 | 390,349 | 10,588 | 419,135
  - 同じ表の列：Quantity, 2012-13 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0082（1 列）
- 見出し：2014-15 Target
- 例1 値：12,000 | 140,000 | 69,500 | 375,000 | 448,000
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0083（1 列）
- 見出し：2014-15 Actual
- 例1 値：432,569 | 11,344 | 70,679 | 129,430 | 352,369
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0084（1 列）
- 見出し：2015-16 Actual
- 例1 値：88,221 | 447,934 | 349,985 | 123,309 | 9,774
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2016-17 Actual, 2017-18 Actual, 2018-19 Actual

## g0085（1 列）
- 見出し：2016-17 Actual
- 例1 値：114,176 | 84,154 | 454,238 | 325,773 | 9,075
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2017-18 Actual, 2018-19 Actual

## g0086（1 列）
- 見出し：2017-18 Actual
- 例1 値：118,309 | 93,186 | 461,137 | 304,048 | N/A
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2018-19 Actual

## g0087（1 列）
- 見出し：2018-19 Actual
- 例1 値：94,826 | 467,431 | 295,955 | 115,479 | N/A
  - 同じ表の列：Quantity, 2012-13 Actual, 2013-14 Actual, 2014-15 Target, 2014-15 Actual, 2015-16 Actual, 2016-17 Actual, 2017-18 Actual

## g0088（1 列）
- 見出し：Type
- 例1 値：Motor car traders New applications lodg… | Sex work brothel managers New applicati… | Patriotic funds Total on register | Limited partnerships New applications l… | Owners corporation managers New applica…
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0089（1 列）
- 見出し：2012-13
- 例1 値：38,751 | 173 | 2,243 | 345 | 491
  - 同じ表の列：Type, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0090（1 列）
- 見出し：2013-14
- 例1 値：1,219 | 771 | 712 | 21 | 4,385
  - 同じ表の列：Type, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g0091（1 列）
- 見出し：2014-15
- 例1 値：426 | 25 | 657 | 39,665 | 621
  - 同じ表の列：Type, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19

## g0092（1 列）
- 見出し：2015-16
- 例1 値：439 | 481 | 6 | 40,577 | 14
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19

## g0093（3 列）
- 見出し：2016-17
- 例1 値：169 | 877 | 563 | 167 | 348
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19
- 例2 値：3 | 3 | 4032 | 150 | 44
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0094（3 列）
- 見出し：2017-18
- 例1 値：14 | 453 | 192 | 577 | 80
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19
- 例2 値：35 | 59 | 172 | 1 | 1038
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2016-17

## g0095（1 列）
- 見出し：2018-19
- 例1 値：15,039 | 189 | 456 | 1,850 | 121
  - 同じ表の列：Type, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g0096（1 列）
- 見出し：Contractor
- 例1 値：Peter Fuller and Associates | University of South Australia | Grieve Gillett Anderson | Birdon Pty Ltd | Australian Industry Group
  - 同じ表の列：Purpose, Value

## g0097（1 列）
- 見出し：Purpose
- 例1 値：Dredging services final payment | Supply Chain Study | Naval shipbuilding industry workforce r… | Defence and Space Landing Pad concierge… | Local defence supply chain resilience s…
  - 同じ表の列：Contractor, Value

## g0098（1 列）
- 見出し：Value
- 例1 値：$50,000 | $59,800 | $18,115 | $22,500 | $65,000
  - 同じ表の列：Contractor, Purpose

## g0099（1 列）
- 見出し：Portfolio
- 例1 値：Home Affairs | Health | Infrastructure, Transport, Regional Dev… | Home Affairs | Infrastructure, Transport, Regional Dev…
  - 同じ表の列：Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0100（1 列）
- 見出し：Department/Agency
- 例1 値：Department of Home Affairs | Department of Health | Department of Agriculture, Water and th… | Federal Court of Australia | Department of Infrastructure, Transport…
  - 同じ表の列：Portfolio, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0101（1 列）
- 見出し：Outcome
- 例1 値：Outcome 2: Facilitate jobs growth throu… | Outcome 3: Improved wellbeing for senio… | Outcome 1: A just and secure society th… | Outcome 2: An efficient, sustainable, c… | Outcome 1: Conserve, protect and sustai…
  - 同じ表の列：Portfolio, Department/Agency, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0102（1 列）
- 見出し：Program
- 例1 値：Program 1.1: Quality Aged Care Services | Program 1.2: Management of the Investme… | Program 3.3: Aged Care Quality | Program 3.2: Aged Care Services | Program 3.3: Cities
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0103（2 列）
- 見出し：Expense type
- 例1 値：Administered Expenses | Departmental Expenses | Departmental Expenses | Program Component | Administered Expenses
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Appropriation type, 2021-22, 2022-23, 2023-24
- 例2 値：Administered Expenses | Administered Expenses | Departmental Expenses | Administered Expenses | Administered Expenses
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Appropriation type, 2021-22, 2022-23, 2023-24

## g0104（1 列）
- 見出し：Appropriation type
- 例1 値：Farm Household Support Act 2014, s. 105… | Implement an Australian farm biodiversi… | Departmental appropriation | Ordinary annual services (Appropriation… | Regionalisation Fund
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, 2021-22, 2022-23, 2023-24

## g0105（4 列）
- 見出し：2021-22
- 例1 値：27222 | 140065 | 480266 | 39466 | 26092
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2022-23, 2023-24
- 例2 値：17500 | 313 | 8276 | 145879 | 4709
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2022-23, 2023-24

## g0106（4 列）
- 見出し：2022-23
- 例1 値：301052 | 1027 | 3652 | 2333 | 3680
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2023-24
- 例2 値：14151 | 4077 | 1469 | 166669 | 4
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2023-24

## g0107（4 列）
- 見出し：2023-24
- 例1 値：854310 | 1773 | 223147 | 265 | 14550
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23
- 例2 値：0 | 17692 | 0 | 29911 | 0
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23

## g0108（3 列）
- 見出し：2024-25
- 例1 値：7870 | 1500 | 158326 | 2174 | 7058
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23
- 例2 値：98 | 443 | 7457 | 5836 | 4
  - 同じ表の列：2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18, 2016-17

## g0109（1 列）
- 見出し：Portfolio
- 例1 値：Health and Aged Care | Foreign Affairs and Trade | Agriculture, Fisheries and Forestry | Defence | Attorney-General's
  - 同じ表の列：Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0110（1 列）
- 見出し：Department/Agency
- 例1 値：Department of Health and Aged Care | Attorney-General's Department | Department of Education | Department of Agriculture, Water and th… | Department of Agriculture, Fisheries an…
  - 同じ表の列：Portfolio, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0111（1 列）
- 見出し：Outcome
- 例1 値：Outcome 1: Growth in the long-term pros… | Outcome 2: Apply and uphold the rule of… | Outcome 1: Support economic growth, pro… | Outcome 1: More sustainable, productive… | Outcome 1: Enhance the quality of teach…
  - 同じ表の列：Portfolio, Department/Agency, Program, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0112（1 列）
- 見出し：Program
- 例1 値：Program 1.1: Sustainable Management of … | Program 1.9: Meat and Livestock Industry | Program 1.1 - Foreign Signals Intellige… | Program 1.9: Meat and Livestock Industry | 1.2.1 - Component 2: Official Developme…
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Expense type, Appropriation type, 2021-22, 2022-23, 2023-24

## g0113（1 列）
- 見出し：Appropriation type
- 例1 値：Departmental appropriation | Less special account | Delivering Cyber Security Skills for a … | Expenses not requiring appropriation in… | Expenses not requiring appropriation in…
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, 2021-22, 2022-23, 2023-24

## g0114（1 列）
- 見出し：2024-25
- 例1 値：0 | -23649 | 9402 | 1767 | 0
  - 同じ表の列：Portfolio, Department/Agency, Outcome, Program, Expense type, Appropriation type, 2021-22, 2022-23

## g0115（9 列）
- 見出し：Suburb
- 例1 値：Beaumaris | Brighton East | Hawthorn | Wheelers Hill | Mordialloc
  - 同じ表の列：State, Business Category, LGA, Region
- 例2 値：Fitzroy North | Fitzroy | Fitzroy | Alphington | Carlton North
  - 同じ表の列：lat, lon, industry_code, industry_desc

## g0116（8 列）
- 見出し：State
- 例1 値：VIC | VIC | VIC | VIC | VIC
  - 同じ表の列：Suburb, Business Category, LGA, Region
- 例2 値：NSW | NSW | NSW | NSW | NSW
  - 同じ表の列：category, city, country, fax, hours1, hours2, hours3, lat

## g0117（2 列）
- 見出し：Business Category
- 例1 値：Personal training | Personal training | Personal training | Personal training | Personal training
  - 同じ表の列：Suburb, State, LGA, Region
- 例2 値：Fishing Club | Fishing Club | Fishing Club | Fishing Club | Fishing Club
  - 同じ表の列：Suburb, State, LGA, Region

## g0118（1 列）
- 見出し：LGA
- 例1 値：Wodonga (RC) | Manningham (C) | Moonee Valley (C) | Manningham (C) | Kingston (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0119（1 列）
- 見出し：Region
- 例1 値：Eastern Metropolitan Region | North and West Metropolitan Region | North and West Metropolitan Region | Southern Metropolitan Region | Southern Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0120（2 列）
- 見出し：ref
- 例1 値：NRF027 | NRF022 | NRF005 | NRF006 | NRF019
  - 同じ表の列：type
- 例2 値：PF03284 | PF03055 | PF03197 | PF03052 | PF03200
  - 同じ表の列：num_of, material, accessible

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
