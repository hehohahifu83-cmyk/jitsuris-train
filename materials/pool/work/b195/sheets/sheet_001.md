# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：全国地方公共団体コード
- 例1 値：313891 | 313891 | 313891 | 313891 | 313891
  - 同じ表の列：ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 連結表記, 都道府県, 市区町村
- 例2 値：313891 | 313891 | 313891 | 313891 | 313891
  - 同じ表の列：ID, 名称, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り, 災害種別_地震, 指定避難所との重複, 対象となる町会・自治会, 備考

## g0002（1 列）
- 見出し：ID
- 例1 値：313891_touhyojo00002 | 313891_touhyojo00009 | 313891_touhyojo00005 | 313891_touhyojo00006 | 313891_touhyojo00012
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 連結表記, 都道府県, 市区町村

## g0003（1 列）
- 見出し：地方公共団体名
- 例1 値：鳥取県南部町 | 鳥取県南部町 | 鳥取県南部町 | 鳥取県南部町 | 鳥取県南部町
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 名称_英字, 連結表記, 都道府県, 市区町村

## g0004（1 列）
- 見出し：名称
- 例1 値：東西町コミュニティセンター | おおくに田園スクエア | ふるさと交流センター | 東長田青年の家 | 南さいはく交流拠点施設 かまくら山荘
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 名称_英字, 連結表記, 都道府県, 市区町村

## g0005（1 列）
- 見出し：名称_カナ
- 例1 値：オオクニデンエンスクエア | ナンブチョウコウミンカンサンカイ フユウマンテンホール | テンマンチョウシャ | ミナミサイハクコウリュウキョテンシセツカマクラサンソウ | オオキヤコウミンカン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_英字, 連結表記, 都道府県, 市区町村

## g0006（1 列）
- 見出し：名称_英字
- 例1 値：Okuni Rural Square | Aimi No. 2 Elementary School | Fuyu Manten Hall, 3rd Floor, Nanbu Town… | Okiya Community Center | Nanbu Town General Welfare Center Ikoi …
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 連結表記, 都道府県, 市区町村

## g0007（1 列）
- 見出し：連結表記
- 例1 値：鳥取県西伯郡南部町大木屋103番地 | 鳥取県西伯郡南部町天萬558番地 | 鳥取県西伯郡南部町法勝寺341番地 | 鳥取県西伯郡南部町福成1452番地1 | 鳥取県西伯郡南部町原868番地4
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 都道府県, 市区町村

## g0008（1 列）
- 見出し：都道府県
- 例1 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 連結表記, 市区町村

## g0009（1 列）
- 見出し：市区町村
- 例1 値：西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 連結表記, 都道府県

## g0010（1 列）
- 見出し：町字
- 例1 値：大木屋 | 天萬 | 池野 | 天萬 | 法勝寺
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 連結表記, 都道府県

## g0012（1 列）
- 見出し：名称
- 例1 値：諸木公民館 | 福頼公民館 | 秋葉山入口 | 原農村公園 | 上長田会館
  - 同じ表の列：全国地方公共団体コード, ID, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り, 災害種別_地震, 指定避難所との重複, 対象となる町会・自治会, 備考

## g0013（1 列）
- 見出し：災害種別_洪水
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 災害種別_崖崩れ、土石流及び地滑り, 災害種別_地震, 指定避難所との重複, 対象となる町会・自治会, 備考

## g0014（1 列）
- 見出し：災害種別_崖崩れ、土石流及び地滑り
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 災害種別_洪水, 災害種別_地震, 指定避難所との重複, 対象となる町会・自治会, 備考

## g0017（1 列）
- 見出し：対象となる町会・自治会
- 例1 値：宮前一区;あいみ手間山;あいみ富有地域 | 倭、大国地域 | 法勝寺 | 福里 | 法勝寺各区;法勝寺地域
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り, 災害種別_地震, 指定避難所との重複, 備考

## g0018（1 列）
- 見出し：備考
- 例1 値：洪水の際2Fのみ | 洪水の際2Fのみ | 洪水の際2Fのみ
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 災害種別_洪水, 災害種別_崖崩れ、土石流及び地滑り, 災害種別_地震, 指定避難所との重複, 対象となる町会・自治会

## g0020（1 列）
- 見出し：学校種
- 例1 値：B1 | B1 | C2 | C1 | C1
  - 同じ表の列：学校コード, 都道府県番号, 設置区分, 本分校, 学校名, 学校名カナ表記, 学校略称, 属性情報設定年月日

## g0022（1 列）
- 見出し：設置区分
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：学校コード, 学校種, 都道府県番号, 本分校, 学校名, 学校名カナ表記, 学校略称, 属性情報設定年月日

## g0024（1 列）
- 見出し：学校名
- 例1 値：南部町立南部中学校 | 南部町立西伯小学校 | 南部町立会見小学校 | 南部町立会見第二小学校 | 南部町立法勝寺中学校
  - 同じ表の列：学校コード, 学校種, 都道府県番号, 設置区分, 本分校, 学校名カナ表記, 学校略称, 属性情報設定年月日

## g0025（1 列）
- 見出し：学校名カナ表記
- 例1 値：サイハクショウガッコウ | ホッショウジチュウガッコウ | ナンブチュウガッコウ | アイミショウガッコウ | アイミダイニショウガッコウ
  - 同じ表の列：学校コード, 学校種, 都道府県番号, 設置区分, 本分校, 学校名, 学校略称, 属性情報設定年月日

## g0026（1 列）
- 見出し：学校略称
- 例1 値：西伯小学校 | 会見小学校 | 会見第二小学校 | 南部中学校 | 法勝寺中学校
  - 同じ表の列：学校コード, 学校種, 都道府県番号, 設置区分, 本分校, 学校名, 学校名カナ表記, 属性情報設定年月日

## g0028（1 列）
- 見出し：旧学校調査番号
- 例1 値：310204 | 310207 | 310206 | 313578 | 313577
  - 同じ表の列：学校コード, 学校種, 都道府県番号, 設置区分, 本分校, 学校名, 学校名カナ表記, 学校略称

## g0029（2 列）
- 見出し：localGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：dateOfSurvey, totalPopulation, male, female, male0_4, female0_4, male5_9, female5_9
- 例2 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：identifier, abstract, status, locatedLocalGovernm…, prefecture, city, cityBlock, coordinateReference…

## g0030（1 列）
- 見出し：dateOfSurvey
- 例1 値：2025-12-31 | 2025-12-31 | 2025-12-31 | 2025-12-31 | 2025-12-31
  - 同じ表の列：localGovernmentCode, totalPopulation, male, female, male0_4, female0_4, male5_9, female5_9

## g0031（1 列）
- 見出し：totalPopulation
- 例1 値：257 | 99 | 340 | 104 | 91
  - 同じ表の列：localGovernmentCode, dateOfSurvey, male, female, male0_4, female0_4, male5_9, female5_9

## g0032（1 列）
- 見出し：male
- 例1 値：26 | 55 | 71 | 147 | 36
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, female, male0_4, female0_4, male5_9, female5_9

## g0033（1 列）
- 見出し：female
- 例1 値：226 | 49 | 7 | 429 | 6
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, male0_4, female0_4, male5_9, female5_9

## g0034（1 列）
- 見出し：male0_4
- 例1 値：7 | 4 | 10 | 13 | 4
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, female, female0_4, male5_9, female5_9

## g0035（1 列）
- 見出し：female0_4
- 例1 値：0 | 0 | 25 | 1 | 0
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, female, male0_4, male5_9, female5_9

## g0036（1 列）
- 見出し：male5_9
- 例1 値：79 | 5 | 1 | 11 | 0
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, female, male0_4, female0_4, female5_9

## g0037（1 列）
- 見出し：female5_9
- 例1 値：0 | 58 | 0 | 69 | 7
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, female, male0_4, female0_4, male5_9

## g0038（1 列）
- 見出し：male10_14
- 例1 値：1 | 2 | 0 | 4 | 2
  - 同じ表の列：localGovernmentCode, dateOfSurvey, totalPopulation, male, female, male0_4, female0_4, male5_9

## g0039（1 列）
- 見出し：identifier
- 例1 値：312011_carpark00008 | 312011_carpark00007 | 312011_carpark00005 | 312011_carpark00006 | 312011_carpark00003
  - 同じ表の列：localGovernmentCode, abstract, status, locatedLocalGovernm…, prefecture, city, cityBlock, coordinateReference…

## g0040（1 列）
- 見出し：abstract
- 例1 値：鳥取市の中心市街地にある年中無休の立体駐車場 | 鳥取市の中心市街地にある24時間営業・年中無休の立体駐車場
  - 同じ表の列：localGovernmentCode, identifier, status, locatedLocalGovernm…, prefecture, city, cityBlock, coordinateReference…

## g0041（1 列）
- 見出し：status
- 例1 値：営業中
  - 同じ表の列：localGovernmentCode, identifier, abstract, locatedLocalGovernm…, prefecture, city, cityBlock, coordinateReference…

## g0042（1 列）
- 見出し：locatedLocalGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, prefecture, city, cityBlock, coordinateReference…

## g0043（1 列）
- 見出し：prefecture
- 例1 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, locatedLocalGovernm…, city, cityBlock, coordinateReference…

## g0044（1 列）
- 見出し：city
- 例1 値：鳥取市 | 鳥取市 | 鳥取市 | 鳥取市 | 鳥取市
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, locatedLocalGovernm…, prefecture, cityBlock, coordinateReference…

## g0045（1 列）
- 見出し：cityBlock
- 例1 値：4 | Oct-62 | 922番地3 | 206番地 | 682-64
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, locatedLocalGovernm…, prefecture, city, coordinateReference…

## g0046（1 列）
- 見出し：coordinateReferenceSystem
- 例1 値：世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011)
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, locatedLocalGovernm…, prefecture, city, cityBlock

## g0047（1 列）
- 見出し：coordinateReferenceSystemCode
- 例1 値：6668 | 6668 | 6668 | 6668 | 6668
  - 同じ表の列：localGovernmentCode, identifier, abstract, status, locatedLocalGovernm…, prefecture, city, cityBlock

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
g0012	
g0013	
g0014	
g0017	
g0018	
g0020	
g0022	
g0024	
g0025	
g0026	
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
```
