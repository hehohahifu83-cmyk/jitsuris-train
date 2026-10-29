# 重大・不明になった列：ChatGPT の説明と Claude の推論の突き合わせ（`research/unknown/explain_compare.py`）

- シートの列 236。ChatGPT の説明が届いた列 236

## 規則の下書きを新しい陣 8 つの採点列すべてに当てる（決める陣での参考値）

- 採点列 2852：今の答え 正しい 2396・不明 329・重大 1

### 不明の列に当てる

| 規則 | 種類 | 当たった列 | 正しい | 重大 |
|---|---|---:|---:|---:|
| A | amount | 7 | 7 | 0 |
| A2 | amount | 18 | 18 | 0 |
| B | id | 45 | 45 | 0 |
| C | quantity | 12 | 12 | 0 |
| D1 | quantity | 11 | 11 | 0 |
| D2 | rate | 9 | 9 | 0 |
| D3 | amount | 3 | 3 | 0 |
| D4 | date | 7 | 7 | 0 |
| D5 | id | 7 | 7 | 0 |
| E | amount | 7 | 7 | 0 |
| F | rate | 4 | 4 | 0 |
| G2 | date | 7 | 7 | 0 |
| G3 | rate | 6 | 6 | 0 |
| G5 | id | 3 | 3 | 0 |

- 合わせて 146 列が答えになる（正しい 146・重大 0）。不明 329 → 183（6.4%）

### 言い切った列で、規則が別の種類を示すもの（言い切った答えにも規則を当てる段＝G10 を足すかの判断）

| 規則 | 列 | 今の答えが正しい | 規則の種類が正しい | 規則の種類なら重大 |
|---|---:|---:|---:|---:|
| A | 1 | 1 | 0 | 0 |
| D3 | 3 | 0 | 0 | 0 |
| D5 | 4 | 3 | 1 | 0 |
| G2 | 2 | 1 | 1 | 0 |
| G5 | 5 | 1 | 4 | 0 |
| G6 | 1 | 0 | 1 | 0 |
| G7 | 2 | 0 | 2 | 0 |
| G9 | 5 | 0 | 5 | 0 |

- G8（名前の種類なのに値が数字だけ）：当たった 5 列。今の答えが正しかった 1（これを不明・id に下げると損）・下げた先が正しい 1

## ChatGPT と Claude

| 組 | 列 | ChatGPT 正しい | Claude 正しい | 2 人同じ | ChatGPT 重大 | ChatGPT 決めない | 前回から変えた |
|---|---:|---:|---:|---:|---:|---:|---:|
| misses | 37 | 30 | 14 | 18 | 0 | 0 | 0 |
| unknown | 199 | 162 | 16 | 37 | 0 | 21 | 15 |

## 説明の点検：項目ごとの異なる文の数（「…」の中は伏せて数える）

| シート | 列 | ③同じ表の列名 | ④値の形 | 迷った種類 | 何があれば | 規則にするなら |
|---|---:|---:|---:|---:|---:|---:|
| 001 | 37 | 37 | 37 | 37 | 29 | 37 |
| 002〜006 | 199 | 6 | 5 | 12 | 3 | 12 |

## 前回から種類を変えた列（15。変えた理由は列ごとに書かれている）

| 番号 | 見出し | 前回 | 今回 | 正解 | 理由 |
|---|---|---|---|---|---|
| e0005 | EW_Total_Company_SA | category | quantity | quantity | 前回category→quantity。先頭8値の[x]だけでフラグと見たが、更新シートの実値3884等は件数の数値。時系列の同系列列なのでカウント値と判断。 |
| e0006 | Beschluss | unknown | amount | amount | 前回unknown→amount。Nachgefragt（申請額）、別ID、status・日付列と並び、Beschlussは決定額と推定。 |
| e0013 | EW_CVL_SA | category | quantity | quantity | 前回category→quantity。先頭の[x]表示ではなく、更新された表後半の2382等の実値を確認し、系列の件数と判断。 |
| e0037 | EW_Receiver_SA | category | quantity | quantity | 前回category→quantity。[x]/[z]だけで分類フラグとしたが、追加された実値249等は受給側系列の数値実績。 |
| e0052 | perPikaHabitat | rate | unknown | rate | 前回rate→unknown。perPikaHabitatという名と整数値だけでは分子・分母・単位が分からず、割合と断定できない。定義または単位が必要。 |
| e0056 | List Number_ numero de liste | id | category | id | 前回id→category。4A/4B/3等は各行の一意キーではなく、製剤のリスト分類値と読める。CAS Numberや製品名は別列。 |
| e0076 | @Caption | S | unknown | date | 前回の答え「unknown（決め手：決められない）」を維持。現在の列名・表題・兄弟列・値を使って再確認した。 |
| e0113 | NO_COMPLEMENTAIRE | S | unknown | id | 前回の答え「unknown（決め手：決められない）」を維持。現在の列名・表題・兄弟列・値を使って再確認した。 |
| e0133 | EW_Admin_SA | category | quantity | quantity | 前回category→quantity。更新シートで[x]以外の系列値が提示されたため、EW_Admin_SAの季節調整済み実績数と判断。 |
| e0143 | VALUE | S | unknown | quantity | 前回の答え「unknown（決め手：決められない）」を維持。現在の列名・表題・兄弟列・値を使って再確認した。 |
| e0149 | Nachgefragt | unknown | amount | amount | 前回unknown→amount。Nachgefragt（申請された額）がBeschluss（決定）・Status・日付・独立したIDと並び、申請額の数値列と読むのが整合。 |
| e0157 | Versicherer | unknown | id | id | 前回unknown→id。Versichererは保険者を指し、Kanton・Geschäftsjahr・Durchschnittsbestandと並ぶ数値は保険者コードとして読むのが妥当。ただしコード表未確認のため確信 |
| e0171 | EW_CVA_SA | category | quantity | quantity | 前回category→quantity。[x]/[z]の先頭値のみではなく更新された実値を考慮し、EW_CVA_SA系列の数値実績と判断。 |
| e0175 | MCC | id | category | id | 前回id→category。MCCは取引行を一意にするIDではなく加盟店の業種分類コード。固定された分類コードはcategory。 |
| e0178 | EW_Compulsory_SA | category | quantity | quantity | 前回category→quantity。更新シートの系列値と同じEW区分の実績値であることから件数系の量と判断。 |

## 新しい規則の材料：ChatGPT は正しく、Claude の規則では決まらない列（162）

| 番号 | 見出し | 正解 | ChatGPT の決め手 | ChatGPT の「規則にするなら」 | 何があれば決められたか |
|---|---|---|---|---|---|
| x0006 | abkuerzung | id | 見出しの語 | 用語集で略語が各定義を引く一意の見出しコードとして使われるなら id。ただし略称が組織そのものを指すと確認できる列は org。 | 略語の展開一覧があれば、製品名・組織名・一般用語の構成比を確かめられる。 |
| x0009 | Degree of severity 2 | quantity | 同じ表の列名 | 複数の Degree of severity 列に整数が並び、実験・個体分類を行軸に持つなら各値は区分別件数＝quantity。ただし値が severity label 自体なら category。 | 列に表示されない場合はテーブル説明か単位定義で「動物数」の集計を確認できる。 |
| x0010 | Extending Agency | id | 見出しの語 | 機関を指す項目でも値が数値・英数字の参照コードで、名称でなければ id。実際の機関名が入る列は org。 | Agency code の対応表があれば、コードが実施機関 ID か分類値か確定できる。 |
| x0013 | nfr | id | 値の形 | 階層分類表で英数字コードを格納し、別列が説明を持つ場合は id。コードでなく表示名を格納する列は category。 | コード表があればコードと説明ラベルの役割を確かめられる。 |
| x0014 | Question | id | 見出しの語 | Question 列に Q1/Q10 のような安定した項目番号がある場合は id。回答選択肢の値や質問文はそれぞれ category/text。 | 質問票の本文があれば各 Q 番号の質問内容を確認できる。 |
| x0016 | Arrest/Detention > Assault with Weapon | quantity | 見出しの語 | 犯罪・出来事の種別を列見出しに展開し、セルに数値を置く表ではセルは件数＝quantity。ただしセルが有無フラグ 0/1 と定義される場合は category。 | 集計説明があれば 0 が「件数ゼロ」か「未報告」か区別できる。 |
| x0017 | Degree of severity 1 | quantity | 同じ表の列名 | 複数の severity 列を横持ちした集計で各セルが個体数なら quantity。フラグ列と明記される場合のみ category。 | データ辞書で各値が個体数であることを確認できる。 |
| x0020 | No. | id | 同じ表の列名 | No. が個票・調査行の順番を付け、件数列が別にあるなら id。No. ill のように物の数を数える場合は quantity。 | 表の原資料で No. が調査IDか行番号か確認できる。 |
| x0022 | listed_building | id | 見出しの語 | listed building の数値キーが建物レコードを識別するなら id。住所・建物名が入る場合は address。 | schema の定義で listed_building がレコードIDか登録状態かを確認できる。 |
| x0024 | Arrest/Detention > Child Sex | quantity | 見出しの語 | 種別別の Arrest/Detention 件数を横持ちした列は quantity。ただしデータ辞書で二値フラグと明記されるなら category。 | 集計の仕様があれば 0 が欠測・秘匿でないことを確認できる。 |
| x0025 | Neither satisfied or dissatisfied | quantity | 同じ表の列名 | 満足度段階ごとに整数の回答数を持つなら quantity。総回答数に対する割合や%が示される場合は rate。 | 各週の回答総数か単位があれば、件数か率か確定できる。 |
| x0026 | Degree of severity 3 | quantity | 同じ表の列名 | severity 区分ごとの個体数を示す横持ち集計は quantity。区分コード自体は category/id。 | データ辞書があればセルが動物件数かどうか確認できる。 |
| x0028 | Degree of severity 0 | quantity | 同じ表の列名 | severity の各区分に該当する個体数をセルで示すなら quantity。分類コード列とは区別する。 | データ辞書でセルが動物件数か確認できる。 |
| x0031 | id2 | id | 見出しの語 | id2 や slug 列に安定したレコード参照文字列が入るなら id。自由記述の場所名なら address/text。 | スラッグと駐車場レコードの一対一対応を確認できる仕様があれば確証が得られる。 |
| x0033 | batch | id | 見出しの語 | 実験サンプル表で batch の値が各行を群に割り当てる番号なら id。実際に製造数・バッチ数を集計する列は quantity。 | プロトコルに batch が件数でなくグループIDとあるか確認できる。 |
| x0037 | Extending Agency | id | 値の形 | 援助・行政表で agency が数値参照コードなら id。機関名称が入る場合だけ org。 | Agency code の辞書があればコード対象を検証できる。 |
| e0001 | Tree | id | 表の題名 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0003 | Rateable Value 2010 | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0005 | EW_Total_Company_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0006 | Beschluss | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0007 | Body | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0008 | OrganisationCode | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0009 | Arrest/Detention > Assault | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0013 | EW_CVL_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0014 | Grand Total 
(workforce numbers) | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0015 | Lim_min | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0016 | SMR 2024 | rate | 同じ表の列名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0017 | PaymentDate | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0018 | Cost Centre | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0019 | UK Treaty Actions November 2015 - Februa | text | 値の形 | 自由な説明・題名・注記はtextにする。固定選択肢の短いラベルはcategory。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0020 | max_time_generation | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0021 | $15,000 to $19,999 / 15 000 $ a 19 999 $ | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0022 | Procurement Start Date | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0023 | Rank | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0025 | $5,000 to $9,999 / 5 000 $ a  9 999 $ | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0027 | RANK OF IMD SCORE (where 1 is most depri | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0028 | date_of_publication_or_production_standa | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0029 | value | amount | 単位の列 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0032 | TOTAL_SHEEP_MOUNTAIN | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0033 | $10,000 to $14,999 / 10 000 $ a 14 999 $ | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0034 | $20,000 to $24,999 / 20 000 $ a 24 999 $ | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0035 | Version | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0036 | Got everything I wanted | rate | 同じ表の列名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0037 | EW_Receiver_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0038 | Fossil fuels | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0040 | Emp_Wkf_POPD_15+yrs_2026 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0041 | Number | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0042 | Under $5,000 / Moins de 5 000 $ | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0043 | 5 | category | 表の題名 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0045 | 6 | category | 表の題名 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0046 | STATISTIC | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0047 | Price (K) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0048 | Q2 (July - September 2014) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0049 | buy_to_let_properties__fixed_rate__over_ | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0051 | Emp_Wkf_POPD_15+yrs_2022 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0054 | FISCAL_YEAR | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0057 | id2 | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0059 | Surplus Spend | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0061 | Emp_Wkf_POPD_15+yrs_2021 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0062 | principal_dwelling_houses__fixed_rate__f | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0063 | Service_FR | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0065 | Type of Post | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0066 | Irrecoverable VAT | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0067 | Metal ores | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0068 | Non-metallic minerals | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0069 | modell_lauf | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0070 | UpperB | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0072 | pop | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0073 | Emp_Wkf_POPD_15+yrs_2028 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0074 | OrganisationCode | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0075 | pop | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0077 | Total - All Returns /Total - Toutes les  | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0078 | Q4 (January - March 2015) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0079 | Emp_Wkf_POPD_15+yrs_2027 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0080 | 前5日間平均気温の品質情報 | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0081 | Emp_Wkf_POPD_15+yrs_2024 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0083 | Widmung | text | 見出しの語 | 自由な説明・題名・注記はtextにする。固定選択肢の短いラベルはcategory。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0084 | Non-Payroll staff (contingent labour/con | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0085 | buy_to_let_properties__floating_rate__st | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0086 | Arrest/Detention > Fraud | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0088 | principal_dwelling_houses__floating_rate | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0089 | principal_dwelling_houses__floating_rate | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0090 | Mandatory Relief % | rate | 見出しの語 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0091 | Dwellings value | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0092 | EW_Total_Company_NSA | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0095 | vj_rel_kumsum | rate | 見出しの語 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0097 | Cost Centre | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0100 | Arrest/Detention > Drugs | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0101 | MaleLowerQuartile | rate | 同じ表の列名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0102 | Time period | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0104 | Tax gap component | category | 表の題名 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0105 | Legislatur | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0106 | Cost Centre | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0107 | plan | text | 値の形 | 自由な説明・題名・注記はtextにする。固定選択肢の短いラベルはcategory。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0108 | principal_dwelling_houses__floating_rate | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0109 | SMR 2019-2023 | rate | 同じ表の列名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0110 | Value | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0111 | YearWeekIso | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0115 | Arrest/Detention > Child Pornography | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0116 | Contract Commencement Date | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0117 | Q3 (October - December 2014) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0118 | Datierung_Bemerkung | text | 見出しの語 | 自由な説明・題名・注記はtextにする。固定選択肢の短いラベルはcategory。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0119 | AnzStand | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0120 | Age | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0123 | Arrest/Detention > Murder / Manslaughter | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0124 | TLIST(A1) | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0126 | aktiver_energieverbrauch | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0127 | Ratio | rate | 同じ表の列名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0129 | Arrest/Detention > Immigration | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0131 | Biomass | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0133 | EW_Admin_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0134 | principal_dwelling_houses__fixed_rate__o | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0135 | Arrest/Detention > Modern Slavery / Huma | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0137 | buy_to_let_properties__floating_rate__tr | rate | 表の題名 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0138 | Emp_Wkf_POPD_15+yrs_2025 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0139 | Grand Total 
(workforce numbers) | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0140 | Total | amount | 値の形 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0141 | AGE | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0144 | LowerB | quantity | 同じ表の列名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0145 | C02199V02655 | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0146 | C02350V02827 | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0148 | organisati | id | 同じ表の列名 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0149 | Nachgefragt | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0151 | Prov/Terr | address | 見出しの語 | 住所・場所名・郵便番号・国や地域名はaddressにする。地域の統計用コード・参照番号だけを記録する場合はid。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0152 | vj_abs_kumsum | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0153 | Amount per Container | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0155 | Total | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0156 | Cost Centre | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0157 | Versicherer | id | 同じ表の列名 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0158 | Emp_Wkf_POPD_15+yrs_2023 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0159 | OrganisationCode | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0160 | Payroll staff costs | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0161 | Q1 (April - June 2014) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0163 | Value (L) | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0165 | EAP amount ($) | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0166 | 終了日（日） | date | 同じ表の列名 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0167 | date_of_publication_or_production | date | 見出しの語 | 暦上の時点・年月・年度・期間コードはdateにする。経過時間の長さはquantity。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0168 | vj_rel_n | rate | 見出しの語 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0169 | sensor | id | 同じ表の列名 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0170 | 9 | category | 表の題名 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0171 | EW_CVA_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0172 | bathPosition | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0174 | Beschaffungsgegenstand | category | 値の形 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0176 | Emp_Wkf_POPD_15+yrs_2029 | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0177 | min_time_generation | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0178 | EW_Compulsory_SA | quantity | 値の形 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0179 | Sexual violence ('000) | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0180 | replicate | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0181 | Discretionary relief % | rate | 見出しの語 | 百分率・割合・比率・利率はrateにする。実人数や金額など分子そのものを記録した値はquantityまたはamount。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0183 | RemunerationValue | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0184 | Variable | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0185 | Cost Centre | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0186 | STATISTIC | id | 値の形 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0187 | Age | category | 同じ表の列名 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0188 | kumsum | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0189 | IrrecoverableVAT | amount | 同じ表の列名 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0190 | Total (All categories) | quantity | 表の題名 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | なし。列名と文脈が一致しており、提示情報で判定できる。 |
| e0191 | plz | address | 見出しの語 | 住所・場所名・郵便番号・国や地域名はaddressにする。地域の統計用コード・参照番号だけを記録する場合はid。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0194 | AGE | category | 見出しの語 | 固定された種別・状態・段階・順位の選択肢はcategoryにする。対象を識別するコードはid、自由文はtext。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0195 | vj_abs_n | quantity | 見出しの語 | 個数・件数・人数・時間長や、質量・エネルギー・面積・容量・データサイズなど加算可能な量はquantityにする。温度・濃度・座標・得点はother、割合はrate。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0197 | library_call_number | id | 見出しの語 | 一意の対象を参照する番号・コード・URIはidにする。郵便番号・国コードなどガイドがaddressと定める値や、分類の意味そのものを表すコードは例外。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |
| e0198 | bruttoinlandprodukt | amount | 見出しの語 | 通貨額・費用・収入・価格を表す値はamountにする。件数はquantity、割合はrate、単なる測定値はother。 | 確信は中程度。単位・データ辞書・コード表があれば値の意味をさらに確認できる。 |

## Claude の規則ごとの、ChatGPT の判断

| 規則 | 当たった列 | ChatGPT も同じ種類 | ChatGPT は別の種類（列） |
|---|---:|---:|---|
| D5 | 1 | 1 |  |
| G2 | 8 | 8 |  |
| G3 | 6 | 6 |  |
| G5 | 7 | 7 |  |
| G6 | 1 | 1 |  |
| G7 | 2 | 2 |  |
| G8 | 3 | 0 | x0010:id, x0022:id, x0037:id |
| G9 | 5 | 5 |  |

## ChatGPT が誤った列の説明（23。規則にすると誤る考え方）

| 番号 | 見出し | 正解 | ChatGPT | 迷った種類と退けた理由 | ④値の形 | Claude の推論 |
|---|---|---|---|---|---|---|
| x0001 | GEO_CANT | id | address | id は考えたが、行を識別する番号ではなく canton を表すコード。category の単なる選択肢とも違い、地理的区域を指す。 | 1、2 の整数コード。コードの形だけなら ID にも見えるが、列名が示すのは場所。 | 「GEO_CANT」で 1,1,2＝州の番号。GEO_ の列名で値が整数→id だが、GEO_ は地名の列にもなる。規則にしない |
| x0002 | kategorie_sortierung | id | category | id も考えたが、記録を照合するキーではなくカテゴリの順番。quantity の件数とも読めない。 | 1、2、3 の小さい整数で、順序番号のように見える。 | b063-0300 と同じ（正解を見直す） |
| x0005 | sitzung_titel | id | text | date は開始日列が別にあり、id は Sitzung ID が別にあるため退ける。category の固定種別でもない。 | 61. Sitzung などの人が読めるタイトル表現。 | 「sitzung_titel」で「61. Sitzung」＝会の回の名前。正解は id だが、題名（titel）の列で文字の値なので text とも読める（正解を見直す） |
| x0011 | kategorie_sortierung | id | category | id は考えたが gruppe_id・analyt_id が別にある。quantity の件数でもなく、順序・順位として category。 | 1、2、5 などの順序整数。 | 「kategorie_sortierung」で 1,1,2＝並べる順の番号。正解は id だが、順位（Rank）の列は category と付いている（u Rank）。並び順・順位の正解をそろえる必要がある（正解を見直す） |
| x0015 | verteilzone | id | address | id も考えたが、地区・自治体と同じ場所軸。category は任意の分類群で地理区域ではない。 | 261_LZ、220_ZHa の英数字コードで区域を表している。 | 「verteilzone」で 261_LZ＝区域のコード。列名からは区分（category）とも読める。規則にしない |
| x0021 | verantwortlichkeit_abkuerzung | id | org | id も考えたが、隣に組織名と部門名があり、値は責任主体の略称として読める。account は abteilung 側。 | KTTGWH、BAFU の略称が反復し、組織・部門名を指す。 | 「verantwortlichkeit_abkuerzung」で KTTGWH・BAFU＝担当の役所の略号。本体は org。略号は org とも id とも読める。正解は id（正解を見直す） |
| x0029 | GOR CODE | id | address | id も候補だが、GOR が区域そのものを指定する地理分類で、列の役割は地域。 | H のような地域コード。値形のみなら ID に見える。 | 「GOR CODE」で H・H。列名が CODE で終わるのに category。recheck の \bcode$ は大文字小文字を問わないので当たるはず→見張りの段で category と言い切ったため recheck を通らない。言い |
| e0004 | monitoring_program | category | id | category・quantityも考えたが、固有の行や対象を参照する番号／コードであり、測定量や分類そのものではない。 | 値の例「BAQUA_TI / BAQUA_TI / BAQUA_TI / BAQUA_TI / BAQUA_TI / BAQUA_TI / BAQUA_TI / BAQUA_TI」。値の形式は、列名・ | 「monitoring_program」で BAQUA_TI。正解 category、ChatGPT id。値が 1 種類のコード。境目 |
| e0012 | Type of Aid | category | id | category・quantityも考えたが、固有の行や対象を参照する番号／コードであり、測定量や分類そのものではない。 | 値の例「C01 / C01 / C01 / C01 / C01 / D02 / C01 / C01」。値の形式は、列名・表題・兄弟列の解釈を補助するが、数字だけでIDや量と決めない。 | 「Type of Aid」で C01。正解 category、ChatGPT id。列名が Type of…（種類）なら値がコードでも category。規則にできる：列名が type・kind・art・typ・category で始まるな |
| e0026 | service | product | category | id・text・quantityも考えたが、値は固定された種別・状態・段階の選択肢で、自由文や固有レコード識別子ではない。 | 値の例「Find Business Regulation (FBR) / Report a Trade Barrier (RaTB) / Regulated Professions Register… | 「service」でサービスの名前。正解 product、ChatGPT category。境目 |
| e0044 | designation | category | address | id・orgも考えたが、値が場所・区域・郵便／国情報を表す。地点を引くコードだけならidとなる点には注意。 | 値の例「Bissone (lago) / Informationsschalter / Stazione Lugano FLP / Guichet d'information / Capolago S | 「designation」で停留所・窓口の名前。正解 category、ChatGPT address。地点の名前は address か category か境目 |
| e0055 | Structure | category | address | id・orgも考えたが、値が場所・区域・郵便／国情報を表す。地点を引くコードだけならidとなる点には注意。 | 値の例「Church - Parochial Hall / Lifeboat House -The Comhaltas … / Anchor / The Handball Alley / Grimsh | 「Structure」で建物の名前。正解 category、ChatGPT address。境目 |
| e0056 | List Number_ numero de liste | id | category | id・text・quantityも考えたが、値は固定された種別・状態・段階の選択肢で、自由文や固有レコード識別子ではない。 | 値の例「4B / 4A / 4B / 3 / 4B / 4B / 2 / 4B」。値の形式は、列名・表題・兄弟列の解釈を補助するが、数字だけでIDや量と決めない。 |  |
| e0082 | reporting_period | date | category | id・text・quantityも考えたが、値は固定された種別・状態・段階の選択肢で、自由文や固有レコード識別子ではない。 | 値の例「P02 / P01 / P01 / P02 / P01 / P02 / P01 / P02」。値の形式は、列名・表題・兄弟列の解釈を補助するが、数字だけでIDや量と決めない。 | 「reporting_period」で P01・P02＝会計の期間。正解 date、ChatGPT category。会計の期の番号は date か category か LABEL_GUIDE で決まっていない（正解を見直す） |
| e0093 | Titel | org | address | id・orgも考えたが、値が場所・区域・郵便／国情報を表す。地点を引くコードだけならidとなる点には注意。 | 値の例「Parkhaus Storchen / Parkhaus Storchen / Parkhaus Elisabethen / Parkhaus Messe / Parkhaus Kunstmu | 「Titel」で Parkhaus Storchen。正解 org、ChatGPT address。境目 |
| e0099 | Family_Famille | category | other | quantity・categoryも考えたが、値が測定属性・科学名・URL等で、分類体系上の数量や選択肢ではない。 | 値の例「Sapindaceae / betulaceae / Rosaceae / Asteraceae / Asteraceae / asteraceae / Asteraceae / cypera | 「Family_Famille」で植物の科。正解 category、ChatGPT other。分類群は区分 |
| e0103 | Control Budget Code | category | id | category・quantityも考えたが、固有の行や対象を参照する番号／コードであり、測定量や分類そのものではない。 | 値の例「DEL / DEL / AME / DEL / AME / DEL / DEL / DEL」。値の形式は、列名・表題・兄弟列の解釈を補助するが、数字だけでIDや量と決めない。 | 「Control Budget Code」で DEL・AME＝予算の区分。正解 category、ChatGPT id。列名が Code でも値が少ない種類の略号なら区分。境目 |
| e0121 | digital_platform | category | other | quantity・categoryも考えたが、値が測定属性・科学名・URL等で、分類体系上の数量や選択肢ではない。 | 値の例「e-manuscripta.ch / e-manuscripta.ch / e-manuscripta.ch / e-manuscripta.ch / e-manuscripta.ch / e | 「digital_platform」で e-manuscripta.ch。正解 category、ChatGPT other。サイトの名前の区分。境目 |
| e0128 | Property | org | account | org・categoryも考えたが、値が内部の部門・費目・口座等で、法人名や一般分類ではない。 | 値の例「Department / Home Office - IPS / Home Office - IPS / Home Office - NPIA / Home Office - GEO / Ho | 「Property」で Home Office - IPS。正解 org、ChatGPT account。組織名なので org |
| e0150 | Supplier | org | account | org・categoryも考えたが、値が内部の部門・費目・口座等で、法人名や一般分類ではない。 | 値の例「TPS – Funding Account 1 / TPS – Funding Account 1 / TPS – Funding Account 1 / TPS – Funding Acco | 「Supplier」で TPS – Funding Account 1。正解 org、ChatGPT account。値は口座名なので境目 |
| e0162 | STATISTIC | category | id | category・quantityも考えたが、固有の行や対象を参照する番号／コードであり、測定量や分類そのものではない。 | 値の例「STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCK | 「STATISTIC」で STOCKNURSE。正解 category、ChatGPT id。統計の系列のコード（正解を見直す） |
| e0175 | MCC | id | category | id・text・quantityも考えたが、値は固定された種別・状態・段階の選択肢で、自由文や固有レコード識別子ではない。 | 値の例「5970 / 7392 / 7392 / 9399 / 7372 / 9399 / 4722」。値の形式は、列名・表題・兄弟列の解釈を補助するが、数字だけでIDや量と決めない。 |  |
| e0199 | originating_sector_fr | account | org | id・accountも考えたが、値が会社・組織名であり、部署や識別コードそのものではない。 | 値の例「Normes d'accessibilité Canada / Organisation canadienne d'élab… / Organisation canadienne d'élab | 「originating_sector_fr」で役所の名前。正解 account、ChatGPT org。値は組織名なので org が自然（正解を見直す） |

## ChatGPT が決めなかった列（21）で「何があれば決められたか」に出た語

| 足りないもの | 列 |
|---|---:|
| 単位の列の値 | 21 |
| 表の題名 | 0 |
| 同じ表のほかの列の値 | 0 |
| 通貨 | 0 |
| 略語の意味 | 0 |
