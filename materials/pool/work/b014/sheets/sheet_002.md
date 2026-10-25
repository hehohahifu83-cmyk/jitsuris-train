# ラベル用シート 002 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：特記事項
- 例1 値：一部、小平第十三小も選択できる調整区域あり | 一部、上水中、花小金井南中も選択できる調整区域あり | 一部、学園東小も選択できる調整区域あり | 一部、小平第五小、鈴木小、花小金井小も選択できる調整区域あり | 一部、小平第五小も選択できる調整区域あり
  - 同じ表の列：情報の管理主体_全国地方公共団体コード, 学校ID, 学校名称, 行政サービス拠点種別

## g0122（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都日野市 | 東京都日野市 | 東京都日野市 | 東京都日野市 | 東京都日野市
  - 同じ表の列：全国地方公共団体コード, 組織名称, 局名称, 部名称, 課名称, 係名称, フロア, 建物名等(方書)

## g0123（1 列）
- 見出し：組織名称
- 例1 値：市長部局健康福祉部セーフティネットコールセンター自立支援係 | 教育委員会教育部発達・教育支援課 | 市長部局総務部防災安全課防災係 | 市長部局市民部保険年金課保険税係 | 市長部局総務部職員課人事係
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 局名称, 部名称, 課名称, 係名称, フロア, 建物名等(方書)

## g0124（1 列）
- 見出し：局名称
- 例1 値：市長部局 | 市長部局 | 市長部局 | 市長部局 | 市長部局
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 部名称, 課名称, 係名称, フロア, 建物名等(方書)

## g0125（1 列）
- 見出し：部名称
- 例1 値：市民部 | 健康福祉部 | 環境共生部 | 教育部 | 環境共生部
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 課名称, 係名称, フロア, 建物名等(方書)

## g0126（1 列）
- 見出し：課名称
- 例1 値：保育課 | 健康課 | 市長公室 | 都市農業振興課 | 学務課
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 部名称, 係名称, フロア, 建物名等(方書)

## g0127（1 列）
- 見出し：係名称
- 例1 値：福祉係 | 交通政策係 | 施設係 | 平和と多文化共生係 | 計画工事係
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 部名称, 課名称, フロア, 建物名等(方書)

## g0128（1 列）
- 見出し：フロア
- 例1 値：市役所3階 | 市役所2階 | 市役所3階 | 子ども包括支援センター1階 | 防災情報センター2階
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 部名称, 課名称, 係名称, 建物名等(方書)

## g0129（1 列）
- 見出し：建物名等(方書)
- 例1 値：生活・保健センター | 多摩平の森ふれあい館 | 新選組のふるさと歴史館 | クリーンセンター | 多摩平の森ふれあい館
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 局名称, 部名称, 課名称, 係名称, フロア

## g0130（1 列）
- 見出し：教育機関_学校名
- 例1 値：久留米中学校 | 第三小学校 | 小山小学校 | 東久留米特別支援学校 | 大門中学校
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名カナ表記

## g0131（1 列）
- 見出し：教育機関_学校名カナ表記
- 例1 値：ホンムラショウガッコウ | ダイゴショウガッコウ | ヒガシクルメトクベツシエンガッコウ | クルメチュウガッコウ | ダイサンショウガッコウ
  - 同じ表の列：教育機関_学校コード, 教育機関_学校種, 教育機関_都道府県番号, 教育機関_設置区分, 教育機関_本分校, 教育機関_学校名

## g0132（3 列）
- 見出し：地方公共団体名
- 例1 値：東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市
  - 同じ表の列：全国地方公共団体コード, 名称, 号数, 発行年月, 発行元
- 例2 値：東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 標高, 市区町村コード, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り

## g0133（1 列）
- 見出し：名称
- 例1 値：ぎかいのトビラ第145号 | ぎかいのトビラ第143号 | ぎかいのトビラ第147号 | ぎかいのトビラ第144号 | ぎかいのトビラ第141号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 号数, 発行年月, 発行元

## g0134（1 列）
- 見出し：号数
- 例1 値：147 | 142 | 146 | 140 | 145
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 発行年月, 発行元

## g0135（1 列）
- 見出し：発行年月
- 例1 値：2023-05 | 2023-02 | 2023-06 | 2023-08 | 2024-05
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行元

## g0136（1 列）
- 見出し：発行元
- 例1 値：羽村市議会 | 羽村市議会 | 羽村市議会 | 羽村市議会 | 羽村市議会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行年月

## g0137（1 列）
- 見出し：名称
- 例1 値：羽村第二中学校 | 松林小学校 | 羽村第一中学校 | 羽村西小学校 | 羽村第三中学校
  - 同じ表の列：全国地方公共団体コード, ID, 名称_カナ, 標高, 市区町村コード, 地方公共団体名, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り

## g0138（1 列）
- 見出し：名称_カナ
- 例1 値：ハムラダイニチュウガッコウ | ハムラダイイチチュウガッコウ | ハムラヒガシショウガッコウ | サカエショウガッコウ | ショウリンショウガッコウ
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 標高, 市区町村コード, 地方公共団体名, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り

## g0139（1 列）
- 見出し：標高
- 例1 値：148 | 145 | 142 | 145 | 151
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 市区町村コード, 地方公共団体名, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り

## g0140（1 列）
- 見出し：市区町村コード
- 例1 値：132276 | 132276 | 132276 | 132276 | 132276
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 標高, 地方公共団体名, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り

## g0141（1 列）
- 見出し：災害種別_洪水
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 標高, 市区町村コード, 地方公共団体名, 災害種別_崖崩れ、土石流及び地滑り

## g0142（1 列）
- 見出し：災害種別_崖崩れ、土石流及び地滑り
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 標高, 市区町村コード, 地方公共団体名, 災害種別_洪水

## g0143（1 列）
- 見出し：災害種別_地震
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 標高, 市区町村コード, 地方公共団体名, 災害種別_洪水

## g0144（1 列）
- 見出し：名称
- 例1 値：ささのは公園 | 栄会館 | ゆうやけ児童公園 | ひので児童公園 | 水道事務所
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, POIコード

## g0145（1 列）
- 見出し：名称_カナ
- 例1 値：シラウメジドウユウエン | カワサキカイカン | クローバーコウエン | フジミダイラブンシツ | アサヒコウエン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, POIコード

## g0146（2 列）
- 見出し：ID
- 例1 値：132292R6H823 | 132292R6H572 | 132292R6H826 | 132292R6H568 | 132292R6H259
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 管理者番号, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態, 指定年
- 例2 値：132292R6S101 | 132292R06S51 | 132292R06S76 | 132292R06S30 | 132292R06S48
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 部名称, 部名称_カナ

## g0147（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市
  - 同じ表の列：全国地方公共団体コード, ID, 管理者番号, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態, 指定年
- 例2 値：東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市 | 東京都西東京市
  - 同じ表の列：全国地方公共団体コード, ID, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 部名称, 部名称_カナ

## g0148（1 列）
- 見出し：管理者番号
- 例1 値：467 | 490 | 1204 | 467 | 1284
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態, 指定年

## g0149（1 列）
- 見出し：指定番号
- 例1 値：43 | 1296 | 361 | 387 | 1252
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 樹種名称, 樹種名称_カナ, 指定状態, 指定年

## g0150（1 列）
- 見出し：樹種名称
- 例1 値：けやき | こぶし | かし | けやき | ぽぷら
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 指定番号, 樹種名称_カナ, 指定状態, 指定年

## g0151（1 列）
- 見出し：樹種名称_カナ
- 例1 値：ケヤキ | ケヤキ | アカマツ | クヌギ | ムク
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 指定番号, 樹種名称, 指定状態, 指定年

## g0152（1 列）
- 見出し：指定状態
- 例1 値：指定 | 指定 | 指定 | 指定 | 指定
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 指定番号, 樹種名称, 樹種名称_カナ, 指定年

## g0153（1 列）
- 見出し：指定年
- 例1 値：1981 | 2011 | 1981 | 1988 | 1981
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態

## g0154（1 列）
- 見出し：指定月
- 例1 値：01 | 04 | 04 | 06 | 05
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 管理者番号, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態

## g0155（1 列）
- 見出し：組織名称
- 例1 値：市長部局都市基盤部下水道課業務係 | 教育委員会教育部公民館保谷駅前公民館 | 市長部局都市基盤部下水道課施設管理係 | 市長部局都市基盤部道路課道路維持係 | 市長部局健康福祉部健康課発達支援係
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称_カナ, 局名称, 局名称_カナ, 部名称, 部名称_カナ

## g0156（1 列）
- 見出し：組織名称_カナ
- 例1 値：シチョウブキョクケンコウフクシブチイキキョウセイカチイキキョウセイガカリ | シチョウブキョクケンコウフクシブセイカツフクシカエンゴダイニガカリ | シチョウブキョクソウムブケンチクエイゼンカケンチクエイゼンガカリ | シチョウブキョクケンコウフクシブコウレイシャシエンカニンテイソウダンガカリ | シチョウブキョクトシキバンブドウロカドウロカンリガカリ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 局名称, 局名称_カナ, 部名称, 部名称_カナ

## g0157（1 列）
- 見出し：局名称
- 例1 値：市長部局 | 市長部局 | 市長部局 | 議会及び行政委員会の事務局など | 市長部局
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称_カナ, 部名称, 部名称_カナ

## g0158（1 列）
- 見出し：局名称_カナ
- 例1 値：シチョウブキョク | シチョウブキョク | シチョウブキョク | シチョウブキョク | シチョウブキョク
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 部名称, 部名称_カナ

## g0159（1 列）
- 見出し：部名称
- 例1 値：総務部 | 企画部 | みどり環境部 | 市民部 | 総務部
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 部名称_カナ

## g0160（1 列）
- 見出し：部名称_カナ
- 例1 値：ケンコウフクシブ | コソダテシエンブ | セイカツブンカスポーツブ | セイカツブンカスポーツブ | ケンコウフクシブ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 部名称

## g0161（1 列）
- 見出し：課名称
- 例1 値：交通課 | 選挙管理委員会事務局 | 公共施設マネジメント課 | 生活福祉課 | 情報推進課
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 局名称, 局名称_カナ, 部名称

## g0162（1 列）
- 見出し：設置者
- 例1 値：東京都オリンピック・パラリンピック準備局 | 東京都オリンピック・パラリンピック準備局 | 東京都オリンピック・パラリンピック準備局 | 東京都オリンピック・パラリンピック準備局 | 東京都オリンピック・パラリンピック準備局
  - 同じ表の列：名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0163（1 列）
- 見出し：名称
- 例1 値：東京都多摩障害者スポーツセンター | 東京体育館 | 東京武道館 | 若洲海浜公園ヨット訓練所 | 東京都障害者総合スポーツセンター
  - 同じ表の列：設置者, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0164（1 列）
- 見出し：アクセス方法
- 例1 値：京王線「飛田給駅」徒歩5分 | りんかい線「国際展示場駅」徒歩5分 | 東急田園都市線「駒沢大学駅」徒歩15分 | 東急田園都市線「駒沢大学駅」徒歩15分 | 都営大江戸線「国立競技場駅」徒歩1分
  - 同じ表の列：設置者, 名称, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0165（1 列）
- 見出し：施設名称
- 例1 値：テニスコート(Aコート) | 第二武道場 | 体育館 | 味の素スタジアム西競技場 | トレーニングルーム
  - 同じ表の列：設置者, 名称, アクセス方法, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0166（1 列）
- 見出し：出入口まで平坦、あっても2cm未満の段差※点字ブロック、タイル目地などの微妙な凹凸除く
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0167（1 列）
- 見出し：出入口までに階段があるが、手すりがある
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0168（1 列）
- 見出し：出入口までに階段があるが、リフトがある
- 例1 値：○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までにスロ-プがある, 施設内が平坦、あっても2cm未満の段差

## g0169（1 列）
- 見出し：出入口までにスロ-プがある
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 施設内が平坦、あっても2cm未満の段差

## g0170（1 列）
- 見出し：施設内が平坦、あっても2cm未満の段差
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある

## g0171（1 列）
- 見出し：施設内に階段があるが、手すりがある
- 例1 値：○ | ○ | ○ | ○ | ○
  - 同じ表の列：設置者, 名称, アクセス方法, 施設名称, 出入口まで平坦、あっても2cm未満の段…, 出入口までに階段があるが、手すりがある, 出入口までに階段があるが、リフトがある, 出入口までにスロ-プがある

## g0172（1 列）
- 見出し：番号
- 例1 値：20 | 62 | 42 | 64 | 48
  - 同じ表の列：区市町村名, 申請団体名, 事業名

## g0173（1 列）
- 見出し：区市町村名
- 例1 値：足立区 | 日野市 | 港区 | 立川市 | 杉並区
  - 同じ表の列：番号, 申請団体名, 事業名

## g0174（1 列）
- 見出し：申請団体名
- 例1 値：三田町会 | 豊島連合町会 | ときわ松町会 | 瀬戸岡町内会 | 豊島一丁目町会
  - 同じ表の列：番号, 区市町村名, 事業名

## g0175（1 列）
- 見出し：事業名
- 例1 値：第33回清水ファミリーデー | 高輪共和会第9回防災フェスタ | 子供まつりを通じた地域交流「コヤヨンまつり」 | ときわ松町会&渋谷二丁目町会 七夕パレードと合同防災企画(障がい者と健常者が共… | スタンドパイプを活用した防災訓練
  - 同じ表の列：番号, 区市町村名, 申請団体名

## g0176（1 列）
- 見出し：都道府県コード又は市区町村コード
- 例1 値：131164 | 131067 | 131059 | 131164 | 131083
  - 同じ表の列：都道府県名, 市区町村名, イベント名, イベント名_カナ, 開始日, 終了日, 開始時間, 終了時間

## g0177（1 列）
- 見出し：都道府県名
- 例1 値：東京都 | 東京都 | 東京都 | 東京都 | 東京都
  - 同じ表の列：都道府県コード又は市区町村コード, 市区町村名, イベント名, イベント名_カナ, 開始日, 終了日, 開始時間, 終了時間

## g0178（1 列）
- 見出し：市区町村名
- 例1 値：墨田区 | 台東区 | 台東区 | 渋谷区 | 台東区
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, イベント名, イベント名_カナ, 開始日, 終了日, 開始時間, 終了時間

## g0179（1 列）
- 見出し：イベント名
- 例1 値：特別展 江戸東京博物館コレクション展 | コレクション展 | 特別展 日本のタイル100年 | MOTアニュアル2022 | 夏のこどもワークショップ
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 市区町村名, イベント名_カナ, 開始日, 終了日, 開始時間, 終了時間

## g0180（1 列）
- 見出し：イベント名_カナ
- 例1 値：コレクションテン | カイガイオーケストラシリーズ ロンドンコウキョウガクダン エンソウカイ | セイジンノヒハタテモノエンヘ | ヨミウリニホンコウキョウガクダン エンソウカイ | キカクテン フィン・ユールトデンマークノイス
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 市区町村名, イベント名, 開始日, 終了日, 開始時間, 終了時間

## g0181（1 列）
- 見出し：開始日
- 例1 値：2022-11-19 | 2023-02-04 | 2022-07-23 | 2023-01-03 | 2022-10-08
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 市区町村名, イベント名, イベント名_カナ, 終了日, 開始時間, 終了時間

## g0182（1 列）
- 見出し：終了日
- 例1 値：2023-02-05 | 2022-10-16 | 2023-02-19 | 2023-01-06 | 2022-10-02
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 市区町村名, イベント名, イベント名_カナ, 開始日, 開始時間, 終了時間

## g0183（1 列）
- 見出し：開始日時特記事項
- 例1 値：10月~会期末までは16:30まで | 通年(計10日間程度) | 全130回以上開催(開催日未定) | (*3F展示室以外は2月3日~2月19日 ) | 第2次予選 2022年8月20日、21日、22日 本選 2022年8月26日、…
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 市区町村名, イベント名, イベント名_カナ, 開始日, 終了日, 開始時間

## g0184（1 列）
- 見出し：Preliminary Briefs Received
- 例1 値：15 | 11 | 20 | 134 | 121
  - 同じ表の列：Number of Accused

## g0185（1 列）
- 見出し：Number of Accused
- 例1 値：6 | 11% | 146 | 13 | 7
  - 同じ表の列：Preliminary Briefs …

## g0186（1 列）
- 見出し：YearMonth
- 例1 値：2012-11 | 2012-10 | 2012-10 | 2012-10 | 2012-11
  - 同じ表の列：IdentifierType, Colour, ComplianceDate, Encumbered

## g0187（1 列）
- 見出し：IdentifierType
- 例1 値：VIN | VIN | VIN | VIN | VIN
  - 同じ表の列：YearMonth, Colour, ComplianceDate, Encumbered

## g0188（1 列）
- 見出し：Colour
- 例1 値：WHITE | WHITE | GREY | GREY | WHITE
  - 同じ表の列：YearMonth, IdentifierType, ComplianceDate, Encumbered

## g0189（1 列）
- 見出し：ComplianceDate
- 例1 値：2012-03 | 2007-07 | 1999-10 | 2001-06 | 2010-10
  - 同じ表の列：YearMonth, IdentifierType, Colour, Encumbered

## g0190（1 列）
- 見出し：Encumbered
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：YearMonth, IdentifierType, Colour, ComplianceDate

## g0191（3 列）
- 見出し：Question
- 例1 値：14 | 11 | 20 | 8 | 27
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：8 | 23 | 12 | 10 | 14
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0192（2 列）
- 見出し：Question_Text
- 例1 値：There should be fewer restrictions on c… | How much should the federal government … | How many new immigrants should Australi… | Trade unions have too much power in the… | The national budget deficit should be r…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：How accessible should abortion services… | The National Broadband Network should d… | When there is an economic problem gover… | How many new immigrants should Australi… | The national budget deficit should be r…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0193（3 列）
- 見出し：category1_definition_1
- 例1 値：Much Less | Much Less | Much Less | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly disagree | Strongly disagree | Much Less | Strongly disagree | Much Less
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0194（3 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat disagree | Somewhat disagree | Somewhat Less | Somewhat Less | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0195（3 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | Neutral | About the same as now | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Neutral | Neutral | Neutral | About the same as now | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0196（3 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat agree | Somewhat more | Somewhat more | Somewhat more | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat more | Somewhat more | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0197（3 列）
- 見出し：category1_definition_5
- 例1 値：Strongly agree | Strongly agree | Much more | Strongly agree | Strongly agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly agree | Strongly agree | Strongly agree | Strongly agree | Much more
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0198（3 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0199（1 列）
- 見出し：Question_Text
- 例1 値：Medicare should offer basic dental care… | There should be more restrictions on 45… | Workplace protections have gone too far. | The National Broadband Network should d… | Asylum seekers who arrive by boat shoul…
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0200（1 列）
- 見出し：Type
- 例1 値：Distance per Flight | Distance Flown | Load Factor (RPKs/ASKs) | Seats per Flight | Distance per Flight
  - 同じ表の列：Fin Year, Major Cities, Regional, Remote, Regional Total, Domestic

## g0201（1 列）
- 見出し：Fin Year
- 例1 値：1996-97 | 1992-93 | 2002-03 | 1996-97 | 2007-08
  - 同じ表の列：Type, Major Cities, Regional, Remote, Regional Total, Domestic

## g0202（1 列）
- 見出し：Major Cities
- 例1 値：21 | 33828175 | 1109.326039 | 1095.881349 | 106.542323
  - 同じ表の列：Type, Fin Year, Regional, Remote, Regional Total, Domestic

## g0203（1 列）
- 見出し：Regional
- 例1 値：125 | 20609.34213 | 5231169 | 78.29108184 | 333.8813607
  - 同じ表の列：Type, Fin Year, Major Cities, Remote, Regional Total, Domestic

## g0204（1 列）
- 見出し：Remote
- 例1 値：36 | 87066734 | 67.45461453 | 88788 | 2587511
  - 同じ表の列：Type, Fin Year, Major Cities, Regional, Regional Total, Domestic

## g0205（1 列）
- 見出し：Regional Total
- 例1 値：16942388 | 20563352 | 217653750 | 408 | 15117.90809
  - 同じ表の列：Type, Fin Year, Major Cities, Regional, Remote, Domestic

## g0206（1 列）
- 見出し：Domestic
- 例1 値：65488692 | 67178.49587 | 53859256 | 23862.33269 | 845.0205383
  - 同じ表の列：Type, Fin Year, Major Cities, Regional, Remote, Regional Total

## g0207（2 列）
- 見出し：Area
- 例1 値：Mount Helen | Eureka | Wendouree | Brown Hill | Black Hill
  - 同じ表の列：ID, Constructed, PlayType, Maintain, Site, Ward, long, lat
- 例2 値：Newington | Ballarat North | Bakery Hill | Buninyong | Alfredton
  - 同じ表の列：Class, Number, Ward, lat

## g0208（1 列）
- 見出し：Constructed
- 例1 値：2013-06-01 | 2021-10-29 | 2007-01-01 | 2015-07-01 | 2002-01-01
  - 同じ表の列：Area, ID, PlayType, Maintain, Site, Ward, long, lat

## g0209（1 列）
- 見出し：PlayType
- 例1 値：PG-Playground | PG-Playground | PG-Playground | PG-Child Minding Playground | PG-Exercise Equipment
  - 同じ表の列：Area, ID, Constructed, Maintain, Site, Ward, long, lat

## g0210（1 列）
- 見出し：Maintain
- 例1 値：City of Ballarat | Tenant | City of Ballarat | Tenant | City of Ballarat
  - 同じ表の列：Area, ID, Constructed, PlayType, Site, Ward, long, lat

## g0211（2 列）
- 見出し：Site
- 例1 値：Wendouree Childrens Centre | Lake Wendouree Reserve | Lake Learmonth | Pleasant Street Reserve | Bridge Mall
  - 同じ表の列：Area, ID, Constructed, PlayType, Maintain, Ward, long, lat
- 例2 値：Truganina Park | Newport Lakes | Cherry Lake Reserve | Cheetham Wetlands | Macaulay Street
  - 同じ表の列：location, type, maint_auth, area_sqm, length_m, width_m, clearance, span

## g0212（2 列）
- 見出し：Ward
- 例1 値：South | South | South | South | South
  - 同じ表の列：Area, ID, Constructed, PlayType, Maintain, Site, long, lat
- 例2 値：South | South | North | South | North
  - 同じ表の列：Area, Class, Number, lat

## g0213（6 列）
- 見出し：long
- 例1 値：143.84016032084995 | 143.87390575628814 | 143.8065301576705 | 143.8383820069361 | 143.82427033575874
  - 同じ表の列：Area, ID, Constructed, PlayType, Maintain, Site, Ward, lat
- 例2 値：144.361460784282 | 144.34660951025 | 144.381600653434 | 144.32905127719 | 144.393454068454
  - 同じ表の列：type, lat

## g0214（19 列）
- 見出し：lat
- 例1 値：-37.58810401448544 | -37.598854254431515 | -37.53947900855628 | -37.555450959506366 | -37.56442298239575
  - 同じ表の列：Area, ID, Constructed, PlayType, Maintain, Site, Ward, long
- 例2 値：-37.5570573825237 | -37.565176168567824 | -37.55809907267304 | -37.42288154864535 | -37.593178972522445
  - 同じ表の列：Area, Class, Number, Ward

## g0215（1 列）
- 見出し：Class
- 例1 値：No Code Allocated | No Code Allocated | No Code Allocated | PG-District | No Code Allocated
  - 同じ表の列：Area, Number, Ward, lat

## g0216（3 列）
- 見出し：Number
- 例1 値：1 | 2 | 1 | 2 | 2
  - 同じ表の列：Area, Class, Ward, lat
- 例2 値：0 | 1461 | 0 | 0 | 0
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Locality, Post_Code, LAT, LONG

## g0217（11 列）
- 見出し：lon
- 例1 値：143.832215385035 | 143.820710320035 | 143.867164010038 | 143.838545075036 | 143.859820450037
  - 同じ表の列：ID, lat
- 例2 値：144.98018664075371 | 144.9921581400325 | 144.9892932009193 | 144.97777274496417 | 145.02602717980056
  - 同じ表の列：lat, elevation, status, ref, suburb

## g0218（1 列）
- 見出し：CLASS
- 例1 値：FISH_CLEAN_STATION | FISH_CLEAN_STATION | FISH_CLEAN_STATION | FISH_CLEAN_STATION | FISH_CLEAN_STATION
  - 同じ表の列：FISH_CLEAN, FISH_CLE_1, FINISH, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_X, POINT_Y

## g0219（1 列）
- 見出し：FISH_CLEAN
- 例1 値：ALUMINIUM | ALUMINIUM | ALUMINIUM | ALUMINIUM | ALUMINIUM
  - 同じ表の列：CLASS, FISH_CLE_1, FINISH, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_X, POINT_Y

## g0220（1 列）
- 見出し：FISH_CLE_1
- 例1 値：SINK | SINK WITH SHADE | SINK WITH SHADE | SINK WITH SHADE | SINK WITH SHADE
  - 同じ表の列：CLASS, FISH_CLEAN, FINISH, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_X, POINT_Y

## g0221（1 列）
- 見出し：FINISH
- 例1 値：PLAIN | PLAIN | PLAIN | PLAIN | PLAIN
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_X, POINT_Y

## g0222（2 列）
- 見出し：ASSET_POSI
- 例1 値：GPS | GPS | GPS | GPS | GPS
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, FINISH, FUNCTIONAL, CREATED_DA, POINT_X, POINT_Y
- 例2 値：GPS | GPS | AIR | AIR | GPS
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM

## g0223（1 列）
- 見出し：FUNCTIONAL
- 例1 値：Y-RIVER-LODERSC | Y-RIVER-CURRU03 | Y-RIVER-LODERSC | Y-RIVER-CURRU03 | Y-RIVER-THEBR03
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, FINISH, ASSET_POSI, CREATED_DA, POINT_X, POINT_Y

## g0224（1 列）
- 見出し：CREATED_DA
- 例1 値：23/05/2014 | 23/05/2014 | 23/05/2014 | 23/05/2014 | 23/05/2014
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, FINISH, ASSET_POSI, FUNCTIONAL, POINT_X, POINT_Y

## g0225（1 列）
- 見出し：POINT_X
- 例1 値：541896.2773 | 540944.6079 | 540289.187 | 541490.2684 | 546786.2691
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, FINISH, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_Y

## g0226（1 列）
- 見出し：POINT_Y
- 例1 値：6907634.402 | 6909520.098 | 6906804.851 | 6907682.862 | 6887531.104
  - 同じ表の列：CLASS, FISH_CLEAN, FISH_CLE_1, FINISH, ASSET_POSI, FUNCTIONAL, CREATED_DA, POINT_X

## g0227（1 列）
- 見出し：CLASS
- 例1 値：BUILDING | BUILDING | BUILDING | BUILDING | BUILDING
  - 同じ表の列：BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0228（1 列）
- 見出し：BUILDING_U
- 例1 値：CABIN | SHED | EQUIPMENT HOUSING BUILDING | CLUBHOUSE | EQUIPMENT HOUSING BUILDING
  - 同じ表の列：CLASS, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0229（1 列）
- 見出し：NO_OF_STOR
- 例1 値：1 | 1 | 1 | 2 | 1
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0230（1 列）
- 見出し：NO_OF_LIFT
- 例1 値：1 | 2 | 1 | 1
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0231（1 列）
- 見出し：NO_OF_BASE
- 例1 値：1 | 1
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, BLD_ENERGY, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0232（1 列）
- 見出し：BLD_ENERGY
- 例1 値：ELECTRICITY (GRID) | TBA | TBA | ELECTRICITY (GRID) | ELECTRICITY (GRID)
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, EQUITABLE_, AREA_SQM, ASSET_POSI

## g0233（1 列）
- 見出し：EQUITABLE_
- 例1 値：N | Y | N | N | Y
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, AREA_SQM, ASSET_POSI

## g0234（2 列）
- 見出し：AREA_SQM
- 例1 値：248 | 52.08 | 12 | 29.07 | 217.51
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, ASSET_POSI
- 例2 値：72 | 21 | 21 | 42.85 | 25
  - 同じ表の列：suburb, maint_auth, melway_ref

## g0235（1 列）
- 見出し：FUNCTIONAL
- 例1 値：F-OTTIPP | F-ACMIAM | K-PIMP01 | S-EL-SPUMP-B30 | K-ROYNEA
  - 同じ表の列：CLASS, BUILDING_U, NO_OF_STOR, NO_OF_LIFT, NO_OF_BASE, BLD_ENERGY, EQUITABLE_, AREA_SQM

## g0236（4 列）
- 見出し：OBJECTID
- 例1 値：32 | 83 | 80 | 116 | 115
  - 同じ表の列：TYPE_, ASSET_NUMB, CONDUIT_SI, COMMENTS, CREATE_DAT, UPDATE_DAT, POSITIONAL, SHAPE_LEN
- 例2 値：8 | 12 | 5 | 6 | 2
  - 同じ表の列：ID, SHAPE__Area

## g0237（1 列）
- 見出し：TYPE_
- 例1 値：ITS Fibre | ITS Fibre | ITS Fibre | ITS Fibre | ITS Fibre
  - 同じ表の列：OBJECTID, ASSET_NUMB, CONDUIT_SI, COMMENTS, CREATE_DAT, UPDATE_DAT, POSITIONAL, SHAPE_LEN

## g0238（1 列）
- 見出し：ASSET_NUMB
- 例1 値：U_GC460 | U_GC411 | U_GC1076 | U_GC464 | U_GC429
  - 同じ表の列：OBJECTID, TYPE_, CONDUIT_SI, COMMENTS, CREATE_DAT, UPDATE_DAT, POSITIONAL, SHAPE_LEN

## g0239（1 列）
- 見出し：CONDUIT_SI
- 例1 値：100 | 100 | 100 | 100 | 100
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, COMMENTS, CREATE_DAT, UPDATE_DAT, POSITIONAL, SHAPE_LEN

## g0240（1 列）
- 見出し：COMMENTS
- 例1 値：100mm White PVC Communications Conduit | 100mm White PVC Communications Conduit | 100mm White PVC Communications Conduit | 100mm White PVC Communications Conduit | 100mm White PVC Communications Conduit
  - 同じ表の列：OBJECTID, TYPE_, ASSET_NUMB, CONDUIT_SI, CREATE_DAT, UPDATE_DAT, POSITIONAL, SHAPE_LEN

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
