# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0002（2 列）
- 見出し：地方公共団体名
- 例1 値：鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, 調査年月日, 地域名, 総人口, 男, 女, 0-4歳の男性, 0-4歳の女性
- 例2 値：鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 名称_英字, 種別, 建物名等(方書), 団体名, 収容定員

## g0004（1 列）
- 見出し：地域名
- 例1 値：倭二区 | 法勝寺五区 | 朝金(1) | 浅井 | 田住
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 総人口, 男, 女, 0-4歳の男性, 0-4歳の女性

## g0005（1 列）
- 見出し：総人口
- 例1 値：162 | 30 | 30 | 43 | 380
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 男, 女, 0-4歳の男性, 0-4歳の女性

## g0006（1 列）
- 見出し：男
- 例1 値：26 | 41 | 121 | 10 | 89
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 女, 0-4歳の男性, 0-4歳の女性

## g0008（1 列）
- 見出し：0-4歳の男性
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 男, 女, 0-4歳の女性

## g0009（1 列）
- 見出し：0-4歳の女性
- 例1 値：0 | 0 | 3 | 1 | 0
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 調査年月日, 地域名, 総人口, 男, 女, 0-4歳の男性

## g0011（1 列）
- 見出し：名称
- 例1 値：宮前児童館 | ひまわり保育園 | 小規模保育園南部町ベアーズ | 法勝寺児童館 | 子どもの広場(いこい荘)
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 名称_英字, 種別, 建物名等(方書), 団体名, 収容定員

## g0012（1 列）
- 見出し：名称_カナ
- 例1 値：コドモノヒロバ | ヒマワリホイクエン | サクラキッズ | ホッショウジジドウカン | ヒマワリガッキュウ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_英字, 種別, 建物名等(方書), 団体名, 収容定員

## g0013（1 列）
- 見出し：名称_英字
- 例1 値：Child-Rearing Exchange Room “Ai-Ai” | Himawari Nursery School | Glico Children's Playground Park Nanbu | Nanbu Town Bears (Small-Scale Nursery S… | Tsukushi Nursery School
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 種別, 建物名等(方書), 団体名, 収容定員

## g0014（1 列）
- 見出し：種別
- 例1 値：放課後児童クラブ | 認可公立保育所 | 認可公立保育所 | その他 | 児童館
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 建物名等(方書), 団体名, 収容定員

## g0015（1 列）
- 見出し：建物名等(方書)
- 例1 値：会見農村環境改善センター内 | 法勝寺児童館内 | プラザ西伯内
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 種別, 団体名, 収容定員

## g0016（1 列）
- 見出し：団体名
- 例1 値：南部町 | 南部町国民健康保険西伯病院 | 南部町 | 南部町 | 南部町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 種別, 建物名等(方書), 収容定員

## g0020（1 列）
- 見出し：学校ID
- 例1 値：B131210000851 | B131210000842 | C131210000396 | B131210000833 | C131210000387
  - 同じ表の列：情報の管理主体_全国地方公共団体コード, 学校コード, 学校名称, 学校名称_カナ

## g0022（1 列）
- 見出し：学校名称
- 例1 値：南部町立法勝寺中学校 | 南部町立西伯小学校 | 南部町立会見小学校 | 南部町立南部中学校 | 南部町立会見第二小学校
  - 同じ表の列：情報の管理主体_全国地方公共団体コード, 学校ID, 学校コード, 学校名称_カナ

## g0023（1 列）
- 見出し：学校名称_カナ
- 例1 値：サイハクショウガッコウ | アイミダイニショウガッコウ | ナンブチュウガッコウ | ホッショウジチュウガッコウ | アイミショウガッコウ
  - 同じ表の列：情報の管理主体_全国地方公共団体コード, 学校ID, 学校コード, 学校名称

## g0024（3 列）
- 見出し：localGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：identifier, locatedLocalGovernm…, prefecture, city, serviceDay, startTime, endTime, dateTimeRemarks
- 例2 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：identifier, category, locatedLocalGovernm…, prefecture, city, cityBlock, permitNumber, permitDate

## g0025（2 列）
- 見出し：identifier
- 例1 値：00040 | 00043 | 00003 | 00028 | 00015
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, serviceDay, startTime, endTime, dateTimeRemarks
- 例2 値：00195 | 00064 | 00083 | 00005 | 00107
  - 同じ表の列：localGovernmentCode, category, locatedLocalGovernm…, prefecture, city, cityBlock, permitNumber, permitDate

## g0026（2 列）
- 見出し：locatedLocalGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：localGovernmentCode, identifier, prefecture, city, serviceDay, startTime, endTime, dateTimeRemarks
- 例2 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：localGovernmentCode, identifier, category, prefecture, city, cityBlock, permitNumber, permitDate

## g0027（2 列）
- 見出し：prefecture
- 例1 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, city, serviceDay, startTime, endTime, dateTimeRemarks
- 例2 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, city, cityBlock, permitNumber, permitDate

## g0028（1 列）
- 見出し：city
- 例1 値：鳥取市 | 鳥取市 | 鳥取市 | 鳥取市 | 鳥取市
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, serviceDay, startTime, endTime, dateTimeRemarks

## g0029（1 列）
- 見出し：serviceDay
- 例1 値：月水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火木金土日 | 火水木金土日
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, startTime, endTime, dateTimeRemarks

## g0030（1 列）
- 見出し：startTime
- 例1 値：0.375 | 0.375 | 0.375 | 0.375 | 0.416666667
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, serviceDay, endTime, dateTimeRemarks

## g0031（1 列）
- 見出し：endTime
- 例1 値：0.916666667 | 0.708333333 | 0.75 | 0.708333333 | 0.75
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, serviceDay, startTime, dateTimeRemarks

## g0032（1 列）
- 見出し：dateTimeRemarks
- 例1 値：展示期間中は無休 | 第一木曜日は利用不可
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, serviceDay, startTime, endTime

## g0033（1 列）
- 見出し：fee
- 例1 値：300 | 300 | 800
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, serviceDay, startTime, endTime

## g0034（1 列）
- 見出し：category
- 例1 値：そうざい製造業 | 菓子製造業 | 飲食店営業 | 飲食店営業 | 飲食店営業
  - 同じ表の列：localGovernmentCode, identifier, locatedLocalGovernm…, prefecture, city, cityBlock, permitNumber, permitDate

## g0035（1 列）
- 見出し：city
- 例1 値：鳥取市 | 智頭町 | 鳥取市 | 鳥取市 | 鳥取市
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, prefecture, cityBlock, permitNumber, permitDate

## g0036（1 列）
- 見出し：cityBlock
- 例1 値：4124-6 | 242-1 | 2168-657 | 124 | 4-2
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, prefecture, city, permitNumber, permitDate

## g0037（1 列）
- 見出し：permitNumber
- 例1 値：第20250149号 | 第20250263号 | 第20250431号 | 第20250277号 | 第20250366号
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, prefecture, city, cityBlock, permitDate

## g0038（1 列）
- 見出し：permitDate
- 例1 値：2025-08-19 | 2025-05-26 | 2025-10-08 | 2025-11-18 | 2025-09-24
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, prefecture, city, cityBlock, permitNumber

## g0039（1 列）
- 見出し：permitEndDate
- 例1 値：2031-05-31 | 2031-11-30 | 2030-11-30 | 2031-08-31 | 2032-02-29
  - 同じ表の列：localGovernmentCode, identifier, category, locatedLocalGovernm…, prefecture, city, cityBlock, permitNumber

## g0040（1 列）
- 見出し：sortingType
- 例1 値：大型 | プラスチック | 小型破砕 | 大型 | 持出禁止
  - 同じ表の列：localGovernmentCode

## 答えの雛形

```
g0002	
g0004	
g0005	
g0006	
g0008	
g0009	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0020	
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
```
