# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：全国地方公共団体コード
- 例1 値：313891 | 313891 | 313891 | 313891 | 313891
  - 同じ表の列：地方公共団体名, 名称, 名称_カナ, 名称_英語, 通称, 説明, 連結表記, 都道府県
- 例2 値：313891 | 313891 | 313891 | 313891 | 313891
  - 同じ表の列：地方公共団体名, 名称, 名称_カナ, 名称_英語, 連結表記, 町字, 利用可能曜日, 開始時間

## g0002（2 列）
- 見出し：地方公共団体名
- 例1 値：鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 名称_英語, 通称, 説明, 連結表記, 都道府県
- 例2 値：鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 名称_英語, 連結表記, 町字, 利用可能曜日, 開始時間

## g0003（1 列）
- 見出し：名称
- 例1 値：南部町地域農産物加工施設めぐみの里 | 祐生出会いの館 | 手間要害山 | あいみ富有の里 えんがわ市 | 鎌倉山
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 名称_英語, 通称, 説明, 連結表記, 都道府県

## g0004（1 列）
- 見出し：名称_カナ
- 例1 値：ガノチクチイキコウリュウキョテンシセツエンガワイチ | シミズイ | カマクラサン | シンリンコウエン | キンカザン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_英語, 通称, 説明, 連結表記, 都道府県

## g0005（1 列）
- 見出し：名称_英語
- 例1 値：Ryokusui Lake Auto Camping Ground | rest house BBQhouse | Local produve shop "Nonohana" | Ryokusui Lake Local produce shop | Ryokusuien
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 通称, 説明, 連結表記, 都道府県

## g0006（1 列）
- 見出し：通称
- 例1 値：めぐみの里 | 野の花 | まごころ市 | 板祐生記念館 | 観光協会
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 説明, 連結表記, 都道府県

## g0007（1 列）
- 見出し：説明
- 例1 値：直売所 | 南部町出身の孔版画家・板祐生(いたゆうせい)の作品は素朴な中にも高い芸術性を持… | 斜めにそびえるミステリータワー。 | 神社の周りは木々が生い茂り、小さな森に囲まれています。その中でも苔むした立派な… | 大国主が死から蘇った神話の舞台。再生・復活、昇進の神社として有名。
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 通称, 連結表記, 都道府県

## g0008（1 列）
- 見出し：連結表記
- 例1 値：鳥取県西伯郡南部町下中谷 | 鳥取県西伯郡南部町寺内232番地 | 鳥取県西伯郡南部町下中谷965番地1 | 鳥取県西伯郡南部町法勝寺332番地1 | 鳥取県西伯郡南部町下中谷965番地1
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 通称, 説明, 都道府県

## g0009（1 列）
- 見出し：都道府県
- 例1 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 通称, 説明, 連結表記

## g0010（1 列）
- 見出し：市区町村
- 例1 値：西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町 | 西伯郡南部町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 通称, 説明, 連結表記

## g0011（1 列）
- 見出し：名称
- 例1 値：南部町自然休養村管理センター緑水園 | 緑水湖オートキャンプ場 | 緑水湖ふれあい市 | あいみ富有の里 えんがわ市 | 緑水湖
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 名称_英語, 連結表記, 町字, 利用可能曜日, 開始時間

## g0012（1 列）
- 見出し：名称_カナ
- 例1 値：リョクスイコフレアイイチ | シンリンコウエン | アカイイワジンジャマエバイテン | アカイイワジンジャ | アカイイワ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_英語, 連結表記, 町字, 利用可能曜日, 開始時間

## g0013（1 列）
- 見出し：名称_英語
- 例1 値：Hosshoji Local produce shop | Agricultural Processing Center Epuron"M… | Forest Park | rest house BBQhouse | Ryokusui Lake Auto Camping Ground
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 連結表記, 町字, 利用可能曜日, 開始時間

## g0014（1 列）
- 見出し：連結表記
- 例1 値：鳥取県西伯郡南部町法勝寺332番地1 | 鳥取県西伯郡南部町 | 鳥取県西伯郡南部町下中谷965番地1 | 鳥取県西伯郡南部町下中谷965番地1 | 鳥取県西伯郡南部町法勝寺
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 町字, 利用可能曜日, 開始時間

## g0015（1 列）
- 見出し：町字
- 例1 値：下中谷 | 下中谷 | 法勝寺 | 寺内 | 下中谷
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 連結表記, 利用可能曜日, 開始時間

## g0016（1 列）
- 見出し：利用可能曜日
- 例1 値：月火水木金土日 | 金土日 | 月火水木金土日 | 月水木金土日 | 火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 連結表記, 町字, 開始時間

## g0017（1 列）
- 見出し：開始時間
- 例1 値：8:00 | 9:00 | 10:00 | 8:00 | 8:30
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 連結表記, 町字, 利用可能曜日

## g0018（1 列）
- 見出し：終了時間
- 例1 値：15:00 | 14:30 | 12:30 | 17:00 | 16:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英語, 連結表記, 町字, 利用可能曜日

## g0019（2 列）
- 見出し：localGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：prefecture, city, coordinateReference…, coordinateReference…
- 例2 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：locatedLocalGovernm…, prefecture, city, coordinateReference…, coordinateReference…, serviceDay, startTime, endTime

## g0020（2 列）
- 見出し：prefecture
- 例1 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：localGovernmentCode, city, coordinateReference…, coordinateReference…
- 例2 値：鳥取県 | 鳥取県 | 鳥取県 | 鳥取県 | 鳥取県
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, city, coordinateReference…, coordinateReference…, serviceDay, startTime, endTime

## g0021（3 列）
- 見出し：city
- 例1 値：鳥取市 | 鳥取市 | 鳥取市 | 鳥取市 | 鳥取市
  - 同じ表の列：localGovernmentCode, prefecture, coordinateReference…, coordinateReference…
- 例2 値：鳥取市 | 鳥取市 | 鳥取市 | 鳥取市 | 鳥取市
  - 同じ表の列：schoolCode, schoolType, establishmentType, establishingOrganiz…, mainOrBranchSchool, mainSchoolCode, cityBlock

## g0022（2 列）
- 見出し：coordinateReferenceSystem
- 例1 値：世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011)
  - 同じ表の列：localGovernmentCode, prefecture, city, coordinateReference…
- 例2 値：世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011) | 世界測地系(JGD2011)
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, serviceDay, startTime, endTime

## g0023（2 列）
- 見出し：coordinateReferenceSystemCode
- 例1 値：6668 | 6668 | 6668 | 6668 | 6668
  - 同じ表の列：localGovernmentCode, prefecture, city, coordinateReference…
- 例2 値：6668 | 6668 | 6668 | 6668 | 6668
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, serviceDay, startTime, endTime

## g0024（1 列）
- 見出し：schoolCode
- 例1 値：B131210000174 | B131210000762 | C131210000047 | C231210000019 | B131210000192
  - 同じ表の列：schoolType, establishmentType, establishingOrganiz…, mainOrBranchSchool, mainSchoolCode, city, cityBlock

## g0025（1 列）
- 見出し：schoolType
- 例1 値：B1 | B1 | B1 | B1 | B1
  - 同じ表の列：schoolCode, establishmentType, establishingOrganiz…, mainOrBranchSchool, mainSchoolCode, city, cityBlock

## g0026（1 列）
- 見出し：establishmentType
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：schoolCode, schoolType, establishingOrganiz…, mainOrBranchSchool, mainSchoolCode, city, cityBlock

## g0027（1 列）
- 見出し：establishingOrganization
- 例1 値：鳥取市役所 | 鳥取市役所 | 鳥取市役所 | 鳥取市役所 | 鳥取市役所
  - 同じ表の列：schoolCode, schoolType, establishmentType, mainOrBranchSchool, mainSchoolCode, city, cityBlock

## g0028（1 列）
- 見出し：mainOrBranchSchool
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：schoolCode, schoolType, establishmentType, establishingOrganiz…, mainSchoolCode, city, cityBlock

## g0029（1 列）
- 見出し：mainSchoolCode
- 例1 値：C131210000010
  - 同じ表の列：schoolCode, schoolType, establishmentType, establishingOrganiz…, mainOrBranchSchool, city, cityBlock

## g0030（1 列）
- 見出し：cityBlock
- 例1 値：42 | 75-1 | 2888 | 907 | 65
  - 同じ表の列：schoolCode, schoolType, establishmentType, establishingOrganiz…, mainOrBranchSchool, mainSchoolCode, city

## g0031（1 列）
- 見出し：locatedLocalGovernmentCode
- 例1 値：312011 | 312011 | 312011 | 312011 | 312011
  - 同じ表の列：localGovernmentCode, prefecture, city, coordinateReference…, coordinateReference…, serviceDay, startTime, endTime

## g0032（1 列）
- 見出し：serviceDay
- 例1 値：月火水木金土日 | 月火水木金土日 | 月水木金土日 | 月火木金土日 | 月火水木金土日
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, coordinateReference…, startTime, endTime

## g0033（1 列）
- 見出し：startTime
- 例1 値：9時 | 10時 | 10時 | 9時 | 9時
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, coordinateReference…, serviceDay, endTime

## g0034（1 列）
- 見出し：endTime
- 例1 値：18時 | 22時 | 17時 | 17時 | 19時
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, coordinateReference…, serviceDay, startTime

## g0035（1 列）
- 見出し：dateTimeRemarks
- 例1 値：情報コーナー、トイレは年中無休 | 12月~2月の第2水曜日が休館日 | 情報コーナー、トイレは年中無休 | 12月~2月の第2水曜日が休館日 | 情報コーナー、トイレは年中無休
  - 同じ表の列：localGovernmentCode, locatedLocalGovernm…, prefecture, city, coordinateReference…, coordinateReference…, serviceDay, startTime

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
```
