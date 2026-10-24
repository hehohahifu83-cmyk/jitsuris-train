# ラベル用シート 010 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_010.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1081（1 列）
- 見出し：調査年月日
- 例1 値：2024-01-01 | 2024-01-01 | 2024-01-01 | 2024-01-01 | 2024-01-01
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 地域名, 総人口, 男性, 女性, 0-4歳の男性, 0-4歳の女性

## g1082（1 列）
- 見出し：地域名
- 例1 値：新町 | 東恋ヶ窪 | 東戸倉 | 富士本 | 東元町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 総人口, 男性, 女性, 0-4歳の男性, 0-4歳の女性

## g1083（1 列）
- 見出し：0-4歳の男性
- 例1 値：128 | 178 | 154 | 52 | 92
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 男性, 女性, 0-4歳の女性

## g1084（1 列）
- 見出し：0-4歳の女性
- 例1 値：205 | 121 | 94 | 165 | 115
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 男性, 女性, 0-4歳の男性

## g1085（1 列）
- 見出し：5-9歳の男性
- 例1 値：194 | 116 | 229 | 103 | 124
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 男性, 女性, 0-4歳の男性

## g1086（1 列）
- 見出し：名称
- 例1 値：狛江市市民活動支援センター(こまえくぼ1234) | 狛江市立中学校給食センター | 西河原公園 | 南部地域センター | ビン・缶リサイクルセンター
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_英語, 設置位置, 高度の種別, 高度の値

## g1087（1 列）
- 見出し：名称_カナ
- 例1 値：カミイズミチイキセンター | モトイズミシミンテニスコート | コマエシリツチュウガッコウキュウショクセンター | ニチガワラコウエン | コマエシシミンカツドウシミンセンター
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_英語, 設置位置, 高度の種別, 高度の値

## g1088（1 列）
- 見出し：名称_英語
- 例1 値：Komae city Junior High School Lunch Cen… | Itopia Center | Civic Activity Support Center(Komaekubo… | Iwado Community Center | Komae North entrance Underground Parking
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 設置位置, 高度の種別, 高度の値

## g1089（1 列）
- 見出し：設置位置
- 例1 値：岩戸地域センター敷地内 | 上和泉地域センター敷地内 | 西泉体育施設敷地内 | 公園南側 | 南部地域センター敷地内
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 高度の種別, 高度の値

## g1090（1 列）
- 見出し：高度の種別
- 例1 値：階数 | 階数;階数;階数 | 階数;階数 | 階数;階数;階数;階数;階数 | 階数;階数;階数;階数;階数
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 設置位置, 高度の値

## g1091（1 列）
- 見出し：高度の値
- 例1 値：1;2;-1 | 1 | -2 | 1;2;3;4;5 | 4;3;2;1;-1
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 設置位置, 高度の種別

## g1092（1 列）
- 見出し：男性トイレ総数
- 例1 値：4 | 5 | 4 | 1 | 15
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 設置位置, 高度の種別

## g1093（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市 | 東京都東久留米市
  - 同じ表の列：全国地方公共団体コード, 名称, 都道府県, 市区町村, 備考

## g1094（1 列）
- 見出し：名称
- 例1 値：前沢5丁目けやき会 | こぶしヶ丘自治会 | 柳窪自治会 | 野火止二丁目アパート自治会 | 前沢宿自治会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 都道府県, 市区町村, 備考

## g1095（1 列）
- 見出し：市区町村
- 例1 値：東久留米市 | 東久留米市 | 東久留米市 | 東久留米市 | 東久留米市
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 都道府県, 備考

## g1096（1 列）
- 見出し：備考
- 例1 値：令和6年4月1日時点 | 令和6年4月1日時点 | 令和6年4月1日時点 | 令和6年4月1日時点 | 令和6年4月1日時点
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 都道府県, 市区町村

## g1097（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都武蔵村山市 | 東京都武蔵村山市 | 東京都武蔵村山市 | 東京都武蔵村山市 | 東京都武蔵村山市
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 都道府県, 市区町村

## g1098（1 列）
- 見出し：名称
- 例1 値：第2ブロック自治会 | 中村第二自治会 | 緑が丘第一自治会 | 萩ノ尾自治会 | 村山団地第11ブロック自治会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 都道府県, 市区町村

## g1099（1 列）
- 見出し：名称_カナ
- 例1 値：シュクジチカイ | ジュウニブロックジチカイ | ムラヤマミチシタジチカイ | オオミナミゴチョウメジチカイ | ヘイワダイダイニジチカイ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 都道府県, 市区町村

## g1100（1 列）
- 見出し：市区町村
- 例1 値：武蔵村山市 | 武蔵村山市 | 武蔵村山市 | 武蔵村山市 | 武蔵村山市
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 都道府県

## g1101（1 列）
- 見出し：媒体
- 例1 値：X(旧twitter) | Instagram | インスタグラム | Facebook | X(旧twitter)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 公式アカウント名, 運用所属名, 説明

## g1102（1 列）
- 見出し：公式アカウント名
- 例1 値：稲城公式動画channel | 稲城市(観光):@inagi_kanko | あそびの広場向陽台(稲城市)【公式】 | 稲城市消防団(公式) | 稲城市の学校給食【公式】
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 運用所属名, 説明

## g1103（1 列）
- 見出し：運用所属名
- 例1 値：防災課 | おやこ包括支援センター課 | 防災課 | 防災課 | 秘書広報課
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 公式アカウント名, 説明

## g1104（1 列）
- 見出し：説明
- 例1 値：学校給食の献立、調理風景等を配信しています。 | イベント情報や中止のお知らせの配信 | 毎月秘書広報課で制作してる動画のほか、各課より掲載依頼があった動画を投稿してい… | 各課より依頼のあった記事を投稿している。 | 稲城市女性防火クラブの活動情報などを配信。
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 媒体, 公式アカウント名, 運用所属名

## g1105（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市 | 東京都羽村市
  - 同じ表の列：全国地方公共団体コード, 名称

## g1106（1 列）
- 見出し：名称
- 例1 値：美原町内会 | 奈賀二町内会 | 緑ヶ丘第二町内会 | 栄町第二町内会 | 五ノ神東町内会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名

## g1107（1 列）
- 見出し：樹種名称
- 例1 値：ひとつばたご | いとひば | そめいよしの(2本組) | いちょう | さいかち
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 指定状態, 指定年, 指定月, 指定日

## g1108（4 列）
- 見出し：指定状態
- 例1 値：指定 | 指定 | 指定 | 指定 | 指定
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 樹種名称, 指定年, 指定月, 指定日
- 例2 値：指定 | 指定 | 指定 | 指定 | 指定
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 樹種名称, 指定年, 指定月, 指定日

## g1109（2 列）
- 見出し：地区名
- 例1 値：全域 | 全域 | 全域 | 全域 | 全域
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミの品目, ゴミの品目_カナ, ゴミの品目_英字, 分別区分
- 例2 値：全域 | 全域 | 全域 | 全域 | 全域
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, ゴミの品目, 分別区分, 備考, 粗大ごみ回収料金

## g1110（1 列）
- 見出し：ゴミの品目
- 例1 値：蚊帳(かや) | 霧吹き | テレビ | ストロー | おもちゃ(電気・電池で動くもの)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 地区名, ゴミの品目_カナ, ゴミの品目_英字, 分別区分

## g1111（1 列）
- 見出し：ゴミの品目_カナ
- 例1 値：セーター | ハサミルイ | オモチャ | ギンガミ | クダモノノホゴザイ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 地区名, ゴミの品目, ゴミの品目_英字, 分別区分

## g1112（1 列）
- 見出し：ゴミの品目_英字
- 例1 値：Shopping bags (e.g., plastic bags from … | Futon cover (plastic) | Drafting (draughting, drawing) board | Bat (flat plate) metal | Glue bags (for eating and drinking)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 地区名, ゴミの品目, ゴミの品目_カナ, 分別区分

## g1113（1 列）
- 見出し：分別区分
- 例1 値：不燃ごみ | びん・スプレー缶・ライター | 小型家電 | 市で収集できない物 | 粗大ごみ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 地区名, ゴミの品目, ゴミの品目_カナ, ゴミの品目_英字

## g1114（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町 | 東京都日の出町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 都道府県, 市区町村

## g1115（1 列）
- 見出し：名称
- 例1 値：第6自治会 | 第21自治会 | 第8自治会 | 第13自治会 | 第1自治会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 都道府県, 市区町村

## g1116（1 列）
- 見出し：名称_カナ
- 例1 値：ダイサンジチカイ | ダイジュウニジチカイ | ダイハチジチカイ | ダイニジュウニジチカイ | ダイニジュウナナジチカイ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 都道府県, 市区町村

## g1117（1 列）
- 見出し：市区町村
- 例1 値：日の出町 | 日の出町 | 日の出町 | 日の出町 | 日の出町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 都道府県

## g1118（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村 | 東京都小笠原村
  - 同じ表の列：全国地方公共団体コード, ID, 組織名称, 組織名称_カナ, 課名称, 課名称_カナ, 係名称, 係名称_カナ

## g1119（1 列）
- 見出し：組織名称
- 例1 値：医療課診療所係 | 環境課生活環境係 | 母島支所施設係 | 建設水道課建設係 | 環境課自然環境係
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称_カナ, 課名称, 課名称_カナ, 係名称, 係名称_カナ

## g1120（1 列）
- 見出し：組織名称_カナ
- 例1 値：ギカイジムキョク | カンキョウカセイカツカンキョウカカリ | ソウムカジョウホウツウシンカカリ | ソウムカキカクセイサクシツ | ケンセツスイドウカケンセツカカリ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 課名称, 課名称_カナ, 係名称, 係名称_カナ

## g1121（1 列）
- 見出し：課名称
- 例1 値：財政課 | 教育課 | 村民課 | 産業観光課 | 会計室
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 課名称_カナ, 係名称, 係名称_カナ

## g1122（1 列）
- 見出し：課名称_カナ
- 例1 値：ギカイジムキョク | ソウムカ | キョウイクカ | カンキョウカ | ザイセイカ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 課名称, 係名称, 係名称_カナ

## g1123（1 列）
- 見出し：係名称
- 例1 値：産業観光係 | 企画政策室 | 自然環境係 | 福祉係 | 庶務係
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 課名称, 課名称_カナ, 係名称_カナ

## g1124（1 列）
- 見出し：係名称_カナ
- 例1 値：ケンセツカカリ | キョウイクカカリ | ジョウゲスイドウカカリ | シセツカカリ | ジュウミンカカリ
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 課名称, 課名称_カナ, 係名称

## g1125（1 列）
- 見出し：フロア
- 例1 値：本庁舎1階 | 第二庁舎2階 | 本庁舎2階 | 本庁舎1階 | 第二庁舎2階
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 組織名称, 組織名称_カナ, 課名称, 課名称_カナ, 係名称

## g1126（1 列）
- 見出し：Unique identifier
- 例1 値：6JPFDTH8 | BJMF73DB | QTH4ZJQW | TSYSV6F4 | W2SWYZFG
  - 同じ表の列：Australian Business…, Trading Zone, Suburb, State, Water Authority

## g1127（1 列）
- 見出し：Australian Business Number
- 例1 値：67567292487 | 17808929427 | 33602791724 | 81479526232 | 56904272558
  - 同じ表の列：Unique identifier, Trading Zone, Suburb, State, Water Authority

## g1128（1 列）
- 見出し：Trading Zone
- 例1 値：1A | 10B | 13 | 1A | 1A
  - 同じ表の列：Unique identifier, Australian Business…, Suburb, State, Water Authority

## g1129（1 列）
- 見出し：Suburb
- 例1 値：Tatura | Wanganella | Whitton | Cobram | Finley
  - 同じ表の列：Unique identifier, Australian Business…, Trading Zone, State, Water Authority

## g1130（1 列）
- 見出し：Water Authority
- 例1 値：Murray Irrigation Ltd | Goulburn Murray Water | Goulburn Murray Water | West Corurgan Private Irrigation Stock … | Murray Irrigation Ltd
  - 同じ表の列：Unique identifier, Australian Business…, Trading Zone, Suburb, State

## g1131（1 列）
- 見出し：Opinions open
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Pre committal stage, Post committal (pre…, Trial stage, Summary matter, Appeal, Other, Finalised in month, Total open

## g1132（1 列）
- 見出し：Pre committal stage
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Opinions open, Post committal (pre…, Trial stage, Summary matter, Appeal, Other, Finalised in month, Total open

## g1133（1 列）
- 見出し：Post committal (pre-trial) stage
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Opinions open, Pre committal stage, Trial stage, Summary matter, Appeal, Other, Finalised in month, Total open

## g1134（1 列）
- 見出し：Trial stage
- 例1 値：4 | 3 | 3 | 3 | 2
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Summary matter, Appeal, Other, Finalised in month, Total open

## g1135（1 列）
- 見出し：Summary matter
- 例1 値：4 | 5 | 5 | 5 | 5
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Trial stage, Appeal, Other, Finalised in month, Total open

## g1136（1 列）
- 見出し：Appeal
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Trial stage, Summary matter, Other, Finalised in month, Total open

## g1137（1 列）
- 見出し：Other
- 例1 値：0 | 1 | 0 | 0 | 1
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Trial stage, Summary matter, Appeal, Finalised in month, Total open

## g1138（1 列）
- 見出し：Finalised in month
- 例1 値：0 | 1 | 0 | 0 | 0
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Trial stage, Summary matter, Appeal, Other, Total open

## g1139（1 列）
- 見出し：Total open
- 例1 値：6 | 10 | 9 | 6 | 10
  - 同じ表の列：Opinions open, Pre committal stage, Post committal (pre…, Trial stage, Summary matter, Appeal, Other, Finalised in month

## g1140（1 列）
- 見出し：Age(years)
- 例1 値：50  54 | 40  44 | 65  69 | Age unknown | 35  39
  - 同じ表の列：Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1141（1 列）
- 見出し：Totalnumberofdebtors:2008
- 例1 値：798 | 5,019 | 4,242 | 1,629 | 3,438
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1142（1 列）
- 見出し：Totalnumberofdebtors:2009
- 例1 値：273 | 4,662 | 1,960 | 1,869 | 1,314
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1143（1 列）
- 見出し：Totalnumberofdebtors:2010
- 例1 値：4,419 | 5,136 | 344 | 1,128 | 3,505
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1144（1 列）
- 見出し：Totalnumberofdebtors:2011
- 例1 値：3,456 | 285 | 1,850 | 1,796 | 2,350
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1145（1 列）
- 見出し：Totalnumberofdebtors:2012
- 例1 値：1,805 | 32,801 | 3,716 | 270 | 4,678
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1146（1 列）
- 見出し：Totalnumberofdebtors:2013
- 例1 値：30,576 | 4,529 | 906 | 1,810 | 3,693
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1147（1 列）
- 見出し：Totalnumberofdebtors:2014
- 例1 値：3,492 | 29,601 | 927 | 806 | 451
  - 同じ表の列：Age(years), Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…, Totalnumberofdebtor…

## g1148（1 列）
- 見出し：BD_ORG_ACN
- 例1 値：118554046 | 011021640 | 052177009 | 008876033 | 009380205
  - 同じ表の列：BD_ORG_TYPE, BD_ORG_START_DT, BD_ORG_END_DT

## g1149（1 列）
- 見出し：BD_ORG_TYPE
- 例1 値：Credit banning by a State or Territory | Section 920A banning | Credit banning by a State or Territory | Australian Financial Services banning | Credit banning by a State or Territory
  - 同じ表の列：BD_ORG_ACN, BD_ORG_START_DT, BD_ORG_END_DT

## g1150（1 列）
- 見出し：BD_ORG_START_DT
- 例1 値：10/04/2001 | 04/03/2002 | 03/12/2013 | 31/07/2003 | 05/12/2004
  - 同じ表の列：BD_ORG_ACN, BD_ORG_TYPE, BD_ORG_END_DT

## g1151（1 列）
- 見出し：BD_ORG_END_DT
- 例1 値：16/12/2018 | Permanent banning | 24/06/2017 | 07/11/2008 | 08/02/2015
  - 同じ表の列：BD_ORG_ACN, BD_ORG_TYPE, BD_ORG_START_DT

## g1152（1 列）
- 見出し：site_id
- 例1 値：GD14 | GC24 | GF05 | GC22 | GF06
  - 同じ表の列：speed, azimuth

## g1153（1 列）
- 見出し：speed
- 例1 値：192.2 | 123.4 | 30.9 | 19.8 | 13.1
  - 同じ表の列：site_id, azimuth

## g1154（1 列）
- 見出し：azimuth
- 例1 値：14 | 39 | 40 | 20 | 334
  - 同じ表の列：site_id, speed

## g1155（1 列）
- 見出し：Asset
- 例1 値：157556 | 137259 | 137284 | 208924 | 36598
  - 同じ表の列：Defect, Date, Offensive, Site, Size, Long, Lat

## g1156（1 列）
- 見出し：Defect
- 例1 値：B-Graffiti | B-Graffiti | B-Graffiti | B-Graffiti | B-Graffiti
  - 同じ表の列：Asset, Date, Offensive, Site, Size, Long, Lat

## g1157（2 列）
- 見出し：Date
- 例1 値：2015-02-18 | 2015-02-25 | 2014-10-08 | 2013-09-23 | 2014-09-02
  - 同じ表の列：Asset, Defect, Offensive, Site, Size, Long, Lat
- 例2 値：2023-07-04 | 2007-02-21 | 2025-04-01 | 2007-08-01 | 2022-05-30
  - 同じ表の列：ref_number, pos_number, pos_title_en, pos_title_fr, old_class_group_code, old_class_level, new_class_group_code, new_class_level

## g1158（1 列）
- 見出し：Offensive
- 例1 値：No | No | No | No | Yes
  - 同じ表の列：Asset, Defect, Date, Site, Size, Long, Lat

## g1159（1 列）
- 見出し：Site
- 例1 値：Ballarat-Skipton Rail Trail | Little Bridge Street Toilets | Little Bridge Street Toilets | Cuthberts Road Reserve | Chisholm Street Reserve
  - 同じ表の列：Asset, Defect, Date, Offensive, Size, Long, Lat

## g1160（1 列）
- 見出し：Size
- 例1 値：Major | No | Minor | Minor | Minor
  - 同じ表の列：Asset, Defect, Date, Offensive, Site, Long, Lat

## g1161（1 列）
- 見出し：Length
- 例1 値：89m | 13m | 17m | 10m | 13m
  - 同じ表の列：SITENO, CLASS, TYPE, long, lat

## g1162（1 列）
- 見出し：SITENO
- 例1 値：49 | 9 | 191a | 98 | 73
  - 同じ表の列：Length, CLASS, TYPE, long, lat

## g1163（2 列）
- 見出し：CLASS
- 例1 値：V | V | V | V | V
  - 同じ表の列：Length, SITENO, TYPE, long, lat
- 例2 値：Lighting | Lighting | Lighting | Lighting | Lighting
  - 同じ表の列：assetid, type, company, contract, assetmanager, primaryservicemanag…, conditionrating, evaluationdate

## g1164（1 列）
- 見出し：Ward
- 例1 値：03 Knox | 05 Thalassa | 02 Mid South Coast | 02 Mid South Coast | 01 Wine Coast
  - 同じ表の列：Suburb, No_of_Parcels, Land_Use

## g1165（1 列）
- 見出し：No_of_Parcels
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Suburb, Ward, Land_Use

## g1166（1 列）
- 見出し：Land_Use
- 例1 値：4520 | 4510 | 4520 | 4100 | 4510
  - 同じ表の列：Suburb, Ward, No_of_Parcels

## g1167（1 列）
- 見出し：managed_by
- 例1 値：Council | Council | Council | Council | Council
  - 同じ表の列：lat, lon

## g1168（1 列）
- 見出し：Type of residential tenancies service provided
- 例1 値：Bonds transferred | Bonds held | Residential Tenancy Goods left behind | Calls answered Residential Tenancies Bo… | Residential Tenancy Rental reports comp…
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1169（1 列）
- 見出し：2012-13
- 例1 値：216,400 | 190,100 | 4,193 | 93,127 | 1,223
  - 同じ表の列：Type of residential…, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1170（1 列）
- 見出し：2013-14
- 例1 値：542,209 | 1,106 | 97,309 | 6,178 | 4,130
  - 同じ表の列：Type of residential…, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18, 2018-19

## g1171（1 列）
- 見出し：2014-15
- 例1 値：203,614 | 1,115 | 228,955 | 936 | 6,267
  - 同じ表の列：Type of residential…, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18, 2018-19

## g1172（1 列）
- 見出し：2015-16
- 例1 値：3,861 | 90,224 | 210,963 | 916 | 69,365
  - 同じ表の列：Type of residential…, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18, 2018-19

## g1173（1 列）
- 見出し：2016-17
- 例1 値：3,531 | 241,489 | 212,749 | 77,847 | 89,375
  - 同じ表の列：Type of residential…, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18, 2018-19

## g1174（1 列）
- 見出し：2017-18
- 例1 値：1,050 | 67,813 | 6,893 | 87,848 | 71,378
  - 同じ表の列：Type of residential…, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2018-19

## g1175（1 列）
- 見出し：2018-19
- 例1 値：244,756 | 73,446 | 8,129 | 1,518 | 219,297
  - 同じ表の列：Type of residential…, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g1176（1 列）
- 見出し：CO2e emissions (tonnes per capita)
- 例1 値：15.73557384 | 24.34667699 | 63.02459369 | 40.51752401 | 3.382856512
  - 同じ表の列：Year, State

## g1177（1 列）
- 見出し：Employment Category
- 例1 値：Public Sector Act | Education & Children's Services Act | Public Sector Act | Education & Children's Services Act | Education & Children's Services Act
  - 同じ表の列：Role, fin_year, Headcount

## g1178（1 列）
- 見出し：Role
- 例1 値：Early childhood workers supporting pres… | Corporate employees in the Department f… | Bus drivers | Bus drivers | Corporate employees in the Department f…
  - 同じ表の列：Employment Category, fin_year, Headcount

## g1179（1 列）
- 見出し：fin_year
- 例1 値：2014 | 2016 | 2023 | 2020 | 2020
  - 同じ表の列：Employment Category, Role, Headcount

## g1180（1 列）
- 見出し：Headcount
- 例1 値：13 | 7 | 100 | 8 | 11
  - 同じ表の列：Employment Category, Role, fin_year

## g1181（1 列）
- 見出し：Location
- 例1 値：ELDER SMITH ROAD / MAIN NORTH ROAD / MA… | BOTANIC ROAD / DEQUETTEVILLE TERRACE / … | PHILLIPS STREET / PORT ROAD / PARKLANDS… | FULLARTON ROAD / GREENHILL ROAD | PORT ROAD / SOUTH RD (PORT RD TO MANTON…
  - 同じ表の列：Rank, Vehicle Exposure

## g1182（1 列）
- 見出し：Vehicle Exposure
- 例1 値：76,800 | 70,800 | 78,600 | 81,500 | 75,000
  - 同じ表の列：Rank, Location

## g1183（1 列）
- 見出し：ABS
- 例1 値：NAA | AusAID | AIC | GBRMPA | Ombudsman
  - 同じ表の列：Australian Bureau o…

## g1184（1 列）
- 見出し：Australian Bureau of Statistics
- 例1 値：Australian Commission for Law Enforceme… | Family Court of Australia | Climate Change Authority | Australian Office of Financial Manageme… | Australian Radiation Protection and Nuc…
  - 同じ表の列：ABS

## g1185（1 列）
- 見出し：Contribution ID
- 例1 値：184468 | 180391 | 184460 | 182887 | 180490
  - 同じ表の列：Date Submitted, What is your level …, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1186（1 列）
- 見出し：Date Submitted
- 例1 値：Dec 04, 2019, 11:15 PM | Jan 22, 2020, 12:20 PM | Dec 04, 2019, 09:39 PM | Jan 31, 2020, 03:48 PM | Dec 06, 2019, 01:20 AM
  - 同じ表の列：Contribution ID, What is your level …, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1187（1 列）
- 見出し：What is your level of experience with open data?
- 例1 値：Moderate | High | Low | Very High | Very High
  - 同じ表の列：Contribution ID, Date Submitted, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1188（1 列）
- 見出し：What is your primary interest in the Open Data Policy?
- 例1 値：Technical | Driving data driven enterprise leadersh… | Technical | Advocacy with Local Govt | how it enables innovation
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1189（1 列）
- 見出し：Where do you work?
- 例1 値：Research and higher education sector | Public sector | Currently not working | Private sector | Research and higher education sector
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you live?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1190（1 列）
- 見出し：Where do you live?
- 例1 値：Outside Australia | Victoria, Metro | Victoria, Metro | Victoria, Metro | Victoria, Rural or Regional
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you work?, Do you face any iss…, If yes, please spec…, What kinds of data …

## g1191（1 列）
- 見出し：Do you face any issues in accessing or using open government
- 例1 値：Yes | No | No | Yes | No
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you work?, Where do you live?, If yes, please spec…, What kinds of data …

## g1192（1 列）
- 見出し：If yes, please specify
- 例1 値：Could not find finance and planning dat… | Available data is very limited in some … | Access to digital ID services, open dat… | The currency and completeness of datase… | See written submission
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, What kinds of data …

## g1193（1 列）
- 見出し：What kinds of data would you like the Victorian government t
- 例1 値：Other states have made elevation (LiDAR… | An API into historical Sold prices on R… | All publicly funded programs and activi… | Need more discussion / opportunites aro… | Fire severity data, fire extent data, R…
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…

## g1194（1 列）
- 見出し：The priority for the Victorian government open data policy s
- 例1 値：Building transparency and trust between… | Building transparency and trust between… | Building transparency and trust between… | Building transparency and trust between… | Building transparency and trust between…
  - 同じ表の列：Contribution ID, Date Submitted, What is your level …, What is your primar…, Where do you work?, Where do you live?, Do you face any iss…, If yes, please spec…

## g1195（1 列）
- 見出し：SA4_Code_2011
- 例1 値：309 | 702 | 305 | 126 | 311
  - 同じ表の列：Service Area, Number of organisat…, More Information: D…, DSS Emergency Relie…

## g1196（1 列）
- 見出し：Service Area
- 例1 値：Far West and Orana | Sydney - City and Inner South | Melbourne - Outer East | Brisbane Inner City | Riverina
  - 同じ表の列：SA4_Code_2011, Number of organisat…, More Information: D…, DSS Emergency Relie…

## g1197（1 列）
- 見出し：Number of organisations
- 例1 値：6 | 14 | 10 | 5 | 4
  - 同じ表の列：SA4_Code_2011, Service Area, More Information: D…, DSS Emergency Relie…

## g1198（1 列）
- 見出し：More Information: DSS Grants Service Directory
- 例1 値：<a href='http://serviceproviders.dss.go… | <a href='http://serviceproviders.dss.go… | <a href='http://serviceproviders.dss.go… | <a href='http://serviceproviders.dss.go… | <a href='http://serviceproviders.dss.go…
  - 同じ表の列：SA4_Code_2011, Service Area, Number of organisat…, DSS Emergency Relie…

## g1199（1 列）
- 見出し：DSS Emergency Relief Website
- 例1 値：<a href='http://www.dss.gov.au/our-resp… | <a href='http://www.dss.gov.au/our-resp… | <a href='http://www.dss.gov.au/our-resp… | <a href='http://www.dss.gov.au/our-resp… | <a href='http://www.dss.gov.au/our-resp…
  - 同じ表の列：SA4_Code_2011, Service Area, Number of organisat…, More Information: D…

## g1200（1 列）
- 見出し：Publisher Title
- 例1 値：Department of Planning, Transport and I… | Office for Recreation and Sport | Renewal SA | Zero Waste SA - Inactive | Department for Environment and Water
  - 同じ表の列：Views, Visits

## 答えの雛形

```
g1081	
g1082	
g1083	
g1084	
g1085	
g1086	
g1087	
g1088	
g1089	
g1090	
g1091	
g1092	
g1093	
g1094	
g1095	
g1096	
g1097	
g1098	
g1099	
g1100	
g1101	
g1102	
g1103	
g1104	
g1105	
g1106	
g1107	
g1108	
g1109	
g1110	
g1111	
g1112	
g1113	
g1114	
g1115	
g1116	
g1117	
g1118	
g1119	
g1120	
g1121	
g1122	
g1123	
g1124	
g1125	
g1126	
g1127	
g1128	
g1129	
g1130	
g1131	
g1132	
g1133	
g1134	
g1135	
g1136	
g1137	
g1138	
g1139	
g1140	
g1141	
g1142	
g1143	
g1144	
g1145	
g1146	
g1147	
g1148	
g1149	
g1150	
g1151	
g1152	
g1153	
g1154	
g1155	
g1156	
g1157	
g1158	
g1159	
g1160	
g1161	
g1162	
g1163	
g1164	
g1165	
g1166	
g1167	
g1168	
g1169	
g1170	
g1171	
g1172	
g1173	
g1174	
g1175	
g1176	
g1177	
g1178	
g1179	
g1180	
g1181	
g1182	
g1183	
g1184	
g1185	
g1186	
g1187	
g1188	
g1189	
g1190	
g1191	
g1192	
g1193	
g1194	
g1195	
g1196	
g1197	
g1198	
g1199	
g1200	
```
