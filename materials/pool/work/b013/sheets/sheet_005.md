# ラベル用シート 005 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：その他[人]
- 例1 値：6062 | 6127 | 6272 | 5955 | 6158
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人]

## g0482（1 列）
- 見出し：計[人]
- 例1 値：17169 | 18170 | 18737 | 18708 | 21658
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人]

## g0483（1 列）
- 見出し：カテゴリ
- 例1 値：財務 | 健康・医療・福祉 | 統計 | 大使館 | 学校
  - 同じ表の列：対象データ, 最終更新日

## g0484（1 列）
- 見出し：対象データ
- 例1 値：第33回港区民世論調査単純集計表・自殺対策について | 施設利用状況一覧:屋内プール開放利用者数 | 港区保健福祉基礎調査(身体障害者)・単純集計表・公衆浴場(銭湯)について | 港区保健福祉基礎調査(身体障害者)・単純集計表・就労状況について | 開発行為等件数
  - 同じ表の列：カテゴリ, 最終更新日

## g0485（1 列）
- 見出し：最終更新日
- 例1 値：2026-04-07T00:00:00 | 2022-06-22T00:00:00 | 2026-06-03T00:00:00 | 2021-01-15T00:00:00 | 2026-03-16T00:00:00
  - 同じ表の列：カテゴリ, 対象データ

## g0486（1 列）
- 見出し：番号
- 例1 値：50 | 28 | 57 | 61 | 21
  - 同じ表の列：店舗名, ジャンル, 店舗PR

## g0487（1 列）
- 見出し：店舗名
- 例1 値：山屋精肉店 | 美食焼肉トラジ 葉菜 SUNAMO店 | ラーメンya | 嵐山 | 餃子の王将門前仲町店
  - 同じ表の列：番号, ジャンル, 店舗PR

## g0488（1 列）
- 見出し：ジャンル
- 例1 値：居酒屋 | ファミリーレストラン | うなぎ | カフェ | ブッフェ
  - 同じ表の列：番号, 店舗名, 店舗PR

## g0489（1 列）
- 見出し：店舗PR
- 例1 値：食べきれない料理のお持ち帰り可(生もの以外)。ランチのご飯小盛り対応可。東陽町… | 普段から量が多めなので、お客様にはひと声おかけして、食べきれる量の調整に応じて… | ランチのご飯の量をご希望で調整できます。食べ放題メニューは、食べ残しのないよう… | 首都高速9号線枝川出口より車で1分。豊洲から車で5分。お台場からも車で15分の… | 大山どりを使った焼き鳥や鶏料理、お洒落な内外装、お子様ドリンク何杯でも無料など…
  - 同じ表の列：番号, 店舗名, ジャンル

## g0490（1 列）
- 見出し：ܓx
- 例1 値：35.657008667848565 | 35.68471962725971 | 35.67690947028408 | 35.684295701331166 | 35.68556272970492
  - 同じ表の列：ox, ǗID, ID, ꖼ, ݒn

## g0491（1 列）
- 見出し：ox
- 例1 値：139.84109938042073 | 139.80901335510254 | 139.83250924051634 | 139.82578737182408 | 139.84019926850604
  - 同じ表の列：ܓx, ǗID, ID, ꖼ, ݒn

## g0492（1 列）
- 見出し：ǗID
- 例1 値：10 | 13 | 4 | 6 | 17
  - 同じ表の列：ܓx, ox, ID, ꖼ, ݒn

## g0493（1 列）
- 見出し：ꖼ
- 例1 値：j[̓ | T̓ | 炩 | xR | ̓
  - 同じ表の列：ܓx, ox, ǗID, ID, ݒn

## g0494（1 列）
- 見出し：ݒn
- 例1 値：s]擌31817 | s]X4918 | s]T64914 | s]擌7151 | s]擌z169
  - 同じ表の列：ܓx, ox, ǗID, ID, ꖼ

## g0495（2 列）
- 見出し：No
- 例1 値：101 | 609 | 203 | 118 | 349
  - 同じ表の列：地区コード, 地区名, 町コード, X座標, Y座標, 備考
- 例2 値：45 | 28 | 79 | 91 | 81
  - 同じ表の列：年度, 資料の名称, 担当所管課, 閲覧期間始期, 根拠, 区分名称

## g0496（1 列）
- 見出し：地区コード
- 例1 値：2 | 1 | 2 | 1 | 1
  - 同じ表の列：No, 地区名, 町コード, X座標, Y座標, 備考

## g0497（1 列）
- 見出し：地区名
- 例1 値：大崎・五反田 | 品川 | 品川 | 大崎・五反田 | 品川
  - 同じ表の列：No, 地区コード, 町コード, X座標, Y座標, 備考

## g0498（1 列）
- 見出し：町コード
- 例1 値：21 | 23 | 14 | 12 | 24
  - 同じ表の列：No, 地区コード, 地区名, X座標, Y座標, 備考

## g0499（1 列）
- 見出し：X座標
- 例1 値：-10125.22482 | -10388.83948 | -8351.41831 | -7829.69712 | -8207.27708
  - 同じ表の列：No, 地区コード, 地区名, 町コード, Y座標, 備考

## g0500（1 列）
- 見出し：Y座標
- 例1 値：-42962.81175 | -41649.12055 | -43236.23745 | -41510.08331 | -42935.81934
  - 同じ表の列：No, 地区コード, 地区名, 町コード, X座標, 備考

## g0501（1 列）
- 見出し：備考
- 例1 値：2018-08 街区変更 | R2年度調査にて街区として存在を確認 | 2018-08 街区変更
  - 同じ表の列：No, 地区コード, 地区名, 町コード, X座標, Y座標

## g0502（1 列）
- 見出し：年度
- 例1 値：2025年度 | 2025年度 | 2025年度 | 2025年度 | 2025年度
  - 同じ表の列：No, 資料の名称, 担当所管課, 閲覧期間始期, 根拠, 区分名称

## g0503（1 列）
- 見出し：資料の名称
- 例1 値：令和7年度第2回目黒区廃棄物減量等推進審議会会議録 | 令和7年度第1回地域保健協議会会議録 | 令和8年度目黒区食品衛生監視指導計画(案) | 住まいの情報 | 令和7年度第29回政策執行会議会議録
  - 同じ表の列：年度, No, 担当所管課, 閲覧期間始期, 根拠, 区分名称

## g0504（1 列）
- 見出し：担当所管課
- 例1 値：健康推進課 | 都市計画課 | 子ども若者課 | 財政課 | 国保年金課
  - 同じ表の列：年度, No, 資料の名称, 閲覧期間始期, 根拠, 区分名称

## g0505（1 列）
- 見出し：閲覧期間始期
- 例1 値：2026-02-05T00:00:00 | 2025-09-05T00:00:00 | 2025-09-01T00:00:00 | 2026-02-01T00:00:00 | 2026-02-17T00:00:00
  - 同じ表の列：年度, No, 資料の名称, 担当所管課, 根拠, 区分名称

## g0506（1 列）
- 見出し：根拠
- 例1 値：情報公開条例第22条第1号 | 情報公開条例第22条第3号-1 | 情報公開条例第22条第3号-2 | 情報公開条例第22条第3号-2 | 情報公開条例第22条第3号-1
  - 同じ表の列：年度, No, 資料の名称, 担当所管課, 閲覧期間始期, 区分名称

## g0507（1 列）
- 見出し：区分名称
- 例1 値：その他実施機関が定める事項(付属機関・政策執行会議等の会議録) | その他実施機関が定める事項(付属機関等がまとめた報告書等) | その他実施機関が定める事項(付属機関・政策執行会議等の会議録) | その他実施機関が定める事項(付属機関・政策執行会議等の会議録) | 区の重要な基本計画
  - 同じ表の列：年度, No, 資料の名称, 担当所管課, 閲覧期間始期, 根拠

## g0508（1 列）
- 見出し：種別
- 例1 値：視覚障害者用資料 | 図書資料 | 電子書籍 | 視覚障害者用資料 | 視覚障害者用資料
  - 同じ表の列：区分, 詳細, 集計区分, 単位, 光が丘, 練馬, 石神井, 平和台

## g0509（1 列）
- 見出し：区分
- 例1 値：視覚障害者用CD | CD | 視覚障害者用録音雑誌 | 点字雑誌 | 児童書
  - 同じ表の列：種別, 詳細, 集計区分, 単位, 光が丘, 練馬, 石神井, 平和台

## g0510（1 列）
- 見出し：詳細
- 例1 値：布の絵本
  - 同じ表の列：種別, 区分, 集計区分, 単位, 光が丘, 練馬, 石神井, 平和台

## g0511（1 列）
- 見出し：集計区分
- 例1 値：合計 | 合計 | 個別 | 合計 | 合計
  - 同じ表の列：種別, 区分, 詳細, 単位, 光が丘, 練馬, 石神井, 平和台

## g0512（1 列）
- 見出し：単位
- 例1 値：組 | 冊 | 組 | 点 | 冊
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 光が丘, 練馬, 石神井, 平和台

## g0513（1 列）
- 見出し：光が丘
- 例1 値：1240 | 4210 | - | 7 | 200
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 単位, 練馬, 石神井, 平和台

## g0514（1 列）
- 見出し：練馬
- 例1 値：19 | - | - | 16 | 59
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 単位, 光が丘, 石神井, 平和台

## g0515（1 列）
- 見出し：石神井
- 例1 値：53640 | 166 | - | - | 139
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 単位, 光が丘, 練馬, 平和台

## g0516（1 列）
- 見出し：平和台
- 例1 値：- | - | 7810 | 90 | 32
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 単位, 光が丘, 練馬, 石神井

## g0517（1 列）
- 見出し：大泉
- 例1 値：- | - | 28 | - | 187
  - 同じ表の列：種別, 区分, 詳細, 集計区分, 単位, 光が丘, 練馬, 石神井

## g0518（1 列）
- 見出し：名称
- 例1 値：石神井町にこにこ | 大泉第二小にこにこ | 八坂小にこにこ | 開進第一小にこにこ | 光が丘春の風小にこにこ
  - 同じ表の列：実施曜日, 団体利用実施曜日

## g0519（1 列）
- 見出し：実施曜日
- 例1 値：火・水・木・金 | 火・水・木・金 | 火・水・木・金 | 火・水・木・金 | 火・水・木・金
  - 同じ表の列：名称, 団体利用実施曜日

## g0520（1 列）
- 見出し：団体利用実施曜日
- 例1 値：なし | なし | なし | なし | なし
  - 同じ表の列：名称, 実施曜日

## g0521（1 列）
- 見出し：年齢[歳]
- 例1 値：80 | 11 | 79 | 0 | 28
  - 同じ表の列：合 計[人], 男性合計[人], 女性合計[人]

## g0522（1 列）
- 見出し：合 計[人]
- 例1 値：9087 | 3829 | 8586 | 10338 | 6047
  - 同じ表の列：年齢[歳], 男性合計[人], 女性合計[人]

## g0523（1 列）
- 見出し：男性合計[人]
- 例1 値：3661 | 6108 | 5906 | 5413 | 5913
  - 同じ表の列：年齢[歳], 合 計[人], 女性合計[人]

## g0524（1 列）
- 見出し：女性合計[人]
- 例1 値：248 | 5257 | 4531 | 3605 | 2718
  - 同じ表の列：年齢[歳], 合 計[人], 男性合計[人]

## g0525（1 列）
- 見出し：西暦
- 例1 値：2012 | 2017 | 2015 | 2024 | 2020
  - 同じ表の列：和暦, 総数, 市長提出, 議員提出, 選挙等, 報告

## g0526（2 列）
- 見出し：総数
- 例1 値：128 | 156 | 193 | 171 | 167
  - 同じ表の列：和暦, 西暦, 市長提出, 議員提出, 選挙等, 報告
- 例2 値：1 | 1 | 8 | 2 | 2
  - 同じ表の列：会派, 男, 女

## g0527（1 列）
- 見出し：市長提出
- 例1 値：106 | 105 | 101 | 97 | 122
  - 同じ表の列：和暦, 西暦, 総数, 議員提出, 選挙等, 報告

## g0528（1 列）
- 見出し：議員提出
- 例1 値：51 | 31 | 56 | 23 | 28
  - 同じ表の列：和暦, 西暦, 総数, 市長提出, 選挙等, 報告

## g0529（1 列）
- 見出し：選挙等
- 例1 値：4 | 15 | 4 | 4 | 15
  - 同じ表の列：和暦, 西暦, 総数, 市長提出, 議員提出, 報告

## g0530（1 列）
- 見出し：報告
- 例1 値：13 | 17 | 14 | 13 | 16
  - 同じ表の列：和暦, 西暦, 総数, 市長提出, 議員提出, 選挙等

## g0531（1 列）
- 見出し：会派
- 例1 値：日本維新の会 | 注 条例定数は,28人である。 | 総数 | チャレンジ調布 | 資料 議会事務局
  - 同じ表の列：総数, 男, 女

## g0532（1 列）
- 見出し：男
- 例1 値：17 | 5 | 1 | 2 | 5
  - 同じ表の列：会派, 総数, 女

## g0533（1 列）
- 見出し：女
- 例1 値：1 | 3 | 2 | 3 | 11
  - 同じ表の列：会派, 総数, 男

## g0534（1 列）
- 見出し：反則行為の種類(略号)
- 例1 値：安全地帯徐行違反 | 牽引自動車本線車道通行帯違反 | 積載物重量制限超過普通等10割以上 | 定員外乗車違反 | 歩行者等側方安全通過義務違反
  - 同じ表の列：車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0535（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 大型車
- 例1 値：* | 9 | 30 | 7 | 7
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0536（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 普通車
- 例1 値：6 | 9 | 6 | 6 | 9
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0537（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 二輪車
- 例1 値：6 | 20 | 6 | 6 | 7
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0538（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 小型特殊車
- 例1 値：5 | 25 | 6 | * | 5
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0539（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 原付車
- 例1 値：* | 3 | 20 | * | *
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0540（1 列）
- 見出し：車両等の種類及び反則金額(単位:千円) 軽車両
- 例1 値：* | 5 | 6 | 5 | 5
  - 同じ表の列：反則行為の種類(略号), 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…, 車両等の種類及び反則金額(単位:千円)…

## g0541（1 列）
- 見出し：違反行為の種別
- 例1 値：歩行者用道路徐行違反 | 無免許運転 | 信号無視赤色等 | 原付等牽引違反 | 優先道路通行車妨害等
  - 同じ表の列：点数, 酒気帯び点数0.25未満, 酒気帯び点数0.25以上

## g0542（1 列）
- 見出し：点数
- 例1 値：1 | 1 | 1 | 1 | 2
  - 同じ表の列：違反行為の種別, 酒気帯び点数0.25未満, 酒気帯び点数0.25以上

## g0543（1 列）
- 見出し：酒気帯び点数0.25未満
- 例1 値：14 | 16 | 14 | 19 | 14
  - 同じ表の列：違反行為の種別, 点数, 酒気帯び点数0.25以上

## g0544（1 列）
- 見出し：酒気帯び点数0.25以上
- 例1 値：25 | 25 | 25 | 25 | 25
  - 同じ表の列：違反行為の種別, 点数, 酒気帯び点数0.25未満

## g0545（1 列）
- 見出し：Main business related cause of personal insolvency
- 例1 値：Total | Gambling or speculation | Note: We have revised data in this publ… | Personal reasons, including ill health … | Excessive interest payments on loan mon…
  - 同じ表の列：Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0546（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2007-08
- 例1 値：36 | 52 | 4 | 19 | 4
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0547（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2008-09
- 例1 値：3 | 3 | 6 | 6 | 52
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0548（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2009-10
- 例1 値：1 | 9 | 85 | 12 | 38
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0549（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2010-11
- 例1 値：8 | 8 | 69 | 7 | 3
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0550（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2011-12
- 例1 値：8 | 2 | 4 | 4 | 3
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0551（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2012-13
- 例1 値：3 | 26 | 5 | 2 | 74
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0552（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2013-14
- 例1 値：1 | 1 | 4 | 4 | 2
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0553（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2014-15
- 例1 値：20 | 4 | 1 | 34 | 6
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0554（1 列）
- 見出し：Number of personal insolvency agreement debtors: 2015-16
- 例1 値：31 | 24 | 4 | 1 | 3
  - 同じ表の列：Main business relat…, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …, Number of personal …

## g0555（1 列）
- 見出し：NSW
- 例1 値：455.0 | 1847.0 | 770.0 | 744.0 | 3418.0
  - 同じ表の列：ACT, Vic, Qld, SA, NT, WA, Tas, Other

## g0556（1 列）
- 見出し：ACT
- 例1 値：16 | 21 | 17 | 95 | 23
  - 同じ表の列：NSW, Vic, Qld, SA, NT, WA, Tas, Other

## g0557（1 列）
- 見出し：Vic
- 例1 値：1042 | 482 | 423 | 468 | 1714
  - 同じ表の列：NSW, ACT, Qld, SA, NT, WA, Tas, Other

## g0558（1 列）
- 見出し：Qld
- 例1 値：619 | 720 | 648 | 529 | 734
  - 同じ表の列：NSW, ACT, Vic, SA, NT, WA, Tas, Other

## g0559（1 列）
- 見出し：SA
- 例1 値：137 | 100 | 114 | 114 | 452
  - 同じ表の列：NSW, ACT, Vic, Qld, NT, WA, Tas, Other

## g0560（1 列）
- 見出し：NT
- 例1 値：13 | 14 | 15 | 12 | 11
  - 同じ表の列：NSW, ACT, Vic, Qld, SA, WA, Tas, Other

## g0561（1 列）
- 見出し：WA
- 例1 値：178 | 170 | 169 | 218 | 263
  - 同じ表の列：NSW, ACT, Vic, Qld, SA, NT, Tas, Other

## g0562（1 列）
- 見出し：Tas
- 例1 値：61 | 132 | 27 | 185 | 61
  - 同じ表の列：NSW, ACT, Vic, Qld, SA, NT, WA, Other

## g0563（2 列）
- 見出し：Other
- 例1 値：12 | 17 | 17 | 58 | 14
  - 同じ表の列：NSW, ACT, Vic, Qld, SA, NT, WA, Tas
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：CODE_OF_ORIGIN, COUNTRY_OR_STATE, CATEGORY, METRO, RURAL

## g0564（3 列）
- 見出し：Total
- 例1 値：2230 | 2705 | 2055 | 1837 | 2888
  - 同じ表の列：NSW, ACT, Vic, Qld, SA, NT, WA, Tas
- 例2 値：1 | 1 | 2 | 2 | 1
  - 同じ表の列：location.id, location, park, trailtype, datestart, dateimage, timeimage, species

## g0565（1 列）
- 見出し：ASIC Register Do
- 例1 値：Previous State of | State Registration | Date of Registration | ABN | Registration
  - 同じ表の列：wnload - Help File, Contributor: Asher …

## g0566（1 列）
- 見出し：wnload - Help File
- 例1 値：Flag indicating whether a dataset recor… | shown is the current company name | State in which the company was original… | been updated since the last report | registered
  - 同じ表の列：ASIC Register Do, Contributor: Asher …

## g0567（1 列）
- 見出し：Contributor: Asher Brooks
- 例1 値：are further variations used in connecti… | DISS - Dissolved by Special Act of Parl… | the meaning of any of these please cont… | THEN show ABN | ABN field has the following logic appli…
  - 同じ表の列：ASIC Register Do, wnload - Help File

## g0568（3 列）
- 見出し：Question
- 例1 値：21 | 13 | 9 | 2 | 6
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：16 | 21 | 22 | 26 | 2
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0569（2 列）
- 見出し：Question_Text
- 例1 値：Australia should end the monarchy and b… | How much should the government spend on… | The National Broadband Network should d… | How much tax should mining companies pa… | How much should the federal government …
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：How much federal government funding sho… | Asylum seekers who arrive by boat shoul… | Terminally ill patients should be able … | Boats carrying asylum seekers should be… | How much financial support should the C…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0570（3 列）
- 見出し：category1_definition_1
- 例1 値：Strongly disagree | Strongly disagree | Strongly disagree | Much Less | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly disagree | Much Less | Strongly disagree | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0571（3 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat disagree | Somewhat Less | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat disagree | Somewhat Less | Somewhat Less | Somewhat disagree | Somewhat Less
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0572（2 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | About the same as now | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：About the same as now | Neutral | About the same as now | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0573（3 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat agree | Somewhat agree | Somewhat more | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0574（3 列）
- 見出し：category1_definition_5
- 例1 値：Much more | Strongly agree | Strongly agree | Strongly agree | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly agree | Strongly agree | Much more | Strongly agree | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0575（3 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0576（1 列）
- 見出し：Question_Text
- 例1 値：Live animal exports should be banned. | How much should the federal government … | The Australian constitution should reco… | The government should further restrict … | The government's parental leave pay sho…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0577（1 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | Neutral | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0578（1 列）
- 見出し：Year_Built
- 例1 値：1997 | 1997 | 1978 | 1997 | 1997
  - 同じ表の列：Propnum, Long, Lat

## g0579（1 列）
- 見出し：Propnum
- 例1 値：2012103 | 2017583 | 2000933 | 2010433 | 2014701
  - 同じ表の列：Year_Built, Long, Lat

## g0580（10 列）
- 見出し：Long
- 例1 値：143.834020325035 | 143.798430840033 | 143.852405630037 | 143.824543785035 | 143.871372340038
  - 同じ表の列：Year_Built, Propnum, Lat
- 例2 値：143.818275812435 | 143.823469360527 | 143.847145749292 | 143.860071895658 | 143.801740190071
  - 同じ表の列：CouncilID, Service, Lat

## g0581（1 列）
- 見出し：CouncilID
- 例1 値：27 | 9 | 37 | 16 | 38
  - 同じ表の列：Service, Lat, Long

## g0582（1 列）
- 見出し：Service
- 例1 値：Government Secondary | Government Secondary | Government Primary | Government Primary | Government Primary
  - 同じ表の列：CouncilID, Lat, Long

## g0583（1 列）
- 見出し：ADDR1
- 例1 値：264 | 385 | 7 | 1 | 12A
  - 同じ表の列：ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS, SHAPE_AREA

## g0584（1 列）
- 見出し：ADDR2
- 例1 値：BURKE CRESCENT | CURRUMBURRA ROAD | WOOLMERE STREET | CAMPBELL STREET | ACRON STREET
  - 同じ表の列：ADDR1, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS, SHAPE_AREA

## g0585（1 列）
- 見出し：ADDR3
- 例1 値：ORMEAU | NERANG | MUDGEERABA | BROADBEACH WATERS | BENOWA
  - 同じ表の列：ADDR1, ADDR2, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS, SHAPE_AREA

## g0586（1 列）
- 見出し：AREA_SQ_M
- 例1 値：2522 | 10537 | 1960 | 1091 | 20257
  - 同じ表の列：ADDR1, ADDR2, ADDR3, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS, SHAPE_AREA

## g0587（1 列）
- 見出し：RFOS_CATEG
- 例1 値：UTILITY RESERVES | GOLD COAST CONSERVATION ESTATE | SPORTS PARKS | OPEN SPACE PARKS | OPEN SPACE PARKS
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_SUB_C, MAINTAINED, COMMENTS, SHAPE_AREA

## g0588（1 列）
- 見出し：RFOS_SUB_C
- 例1 値：BUSHLAND RESERVE | UTILITY RESERVE | BUSHLAND RESERVE | LOCAL RECREATION PARK | AMENITY SPACE
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, MAINTAINED, COMMENTS, SHAPE_AREA

## g0589（1 列）
- 見出し：MAINTAINED
- 例1 値：GCCC | GCCC | GCCC | GCCC | GCCC
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, COMMENTS, SHAPE_AREA

## g0590（1 列）
- 見出し：COMMENTS
- 例1 値：Lot 133WD948 OSPL ACQUISITION | Recreation acquisition | OPSL Aquisition. Also Nature Refuge und… | Recreation acquisition | MUDGEERABA ARTS AND CRAFT HISTORICAL VI…
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, SHAPE_AREA

## g0591（1 列）
- 見出し：SHAPE_AREA
- 例1 値：23328.05279 | 3913.673413 | 157255.9418 | 1267.484433 | 20636.44724
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS

## g0592（1 列）
- 見出し：SHAPE_LEN
- 例1 値：9618.999939 | 177.4664079 | 3836.106306 | 684.2018056 | 527.5024668
  - 同じ表の列：ADDR1, ADDR2, ADDR3, AREA_SQ_M, RFOS_CATEG, RFOS_SUB_C, MAINTAINED, COMMENTS

## g0593（1 列）
- 見出し：CLASS
- 例1 値：BOATING_FACILITY | BOATING_FACILITY | BOATING_FACILITY | BOATING_FACILITY | BOATING_FACILITY
  - 同じ表の列：BOATING_FA, BOATING__1, BOATING__2, FINISH, GRADE, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0594（1 列）
- 見出し：BOATING_FA
- 例1 値：PONTOON | RAMP | RAMP | PONTOON | JETTY
  - 同じ表の列：CLASS, BOATING__1, BOATING__2, FINISH, GRADE, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0595（1 列）
- 見出し：BOATING__1
- 例1 値：CONCRETE | CONCRETE | CONCRETE/ALUMINIUM | CONCRETE | CONCRETE
  - 同じ表の列：CLASS, BOATING_FA, BOATING__2, FINISH, GRADE, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0596（1 列）
- 見出し：BOATING__2
- 例1 値：PUBLIC | PUBLIC | PUBLIC | PUBLIC | PUBLIC
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, FINISH, GRADE, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0597（1 列）
- 見出し：FINISH
- 例1 値：PLAIN | PLAIN | PLAIN | PLAIN | PLAIN
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, GRADE, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0598（1 列）
- 見出し：GRADE
- 例1 値：17 | 10 | 12.5 | 12.5 | 10
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, FINISH, POWER_SUPP, WATER_SUPP, AREA_SQM

## g0599（1 列）
- 見出し：POWER_SUPP
- 例1 値：N | N | N | N | N
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, FINISH, GRADE, WATER_SUPP, AREA_SQM

## g0600（1 列）
- 見出し：WATER_SUPP
- 例1 値：Y | Y | Y | N | Y
  - 同じ表の列：CLASS, BOATING_FA, BOATING__1, BOATING__2, FINISH, GRADE, POWER_SUPP, AREA_SQM

## 答えの雛形

```
g0481	
g0482	
g0483	
g0484	
g0485	
g0486	
g0487	
g0488	
g0489	
g0490	
g0491	
g0492	
g0493	
g0494	
g0495	
g0496	
g0497	
g0498	
g0499	
g0500	
g0501	
g0502	
g0503	
g0504	
g0505	
g0506	
g0507	
g0508	
g0509	
g0510	
g0511	
g0512	
g0513	
g0514	
g0515	
g0516	
g0517	
g0518	
g0519	
g0520	
g0521	
g0522	
g0523	
g0524	
g0525	
g0526	
g0527	
g0528	
g0529	
g0530	
g0531	
g0532	
g0533	
g0534	
g0535	
g0536	
g0537	
g0538	
g0539	
g0540	
g0541	
g0542	
g0543	
g0544	
g0545	
g0546	
g0547	
g0548	
g0549	
g0550	
g0551	
g0552	
g0553	
g0554	
g0555	
g0556	
g0557	
g0558	
g0559	
g0560	
g0561	
g0562	
g0563	
g0564	
g0565	
g0566	
g0567	
g0568	
g0569	
g0570	
g0571	
g0572	
g0573	
g0574	
g0575	
g0576	
g0577	
g0578	
g0579	
g0580	
g0581	
g0582	
g0583	
g0584	
g0585	
g0586	
g0587	
g0588	
g0589	
g0590	
g0591	
g0592	
g0593	
g0594	
g0595	
g0596	
g0597	
g0598	
g0599	
g0600	
```
