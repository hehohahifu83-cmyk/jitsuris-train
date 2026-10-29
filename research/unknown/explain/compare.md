# 重大・不明になった列：ChatGPT の説明と Claude の推論の突き合わせ（`research/unknown/explain_compare.py`）

- シートの列 236。ChatGPT の説明が届いた列 37

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

## 新しい規則の材料：ChatGPT は正しく、Claude の規則では決まらない列（16）

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

## Claude の規則ごとの、ChatGPT の判断

| 規則 | 当たった列 | ChatGPT も同じ種類 | ChatGPT は別の種類（列） |
|---|---:|---:|---|
| D5 | 1 | 1 |  |
| G2 | 1 | 1 |  |
| G5 | 4 | 4 |  |
| G6 | 1 | 1 |  |
| G7 | 2 | 2 |  |
| G8 | 3 | 0 | x0010:id, x0022:id, x0037:id |
| G9 | 5 | 5 |  |

## ChatGPT が誤った列の説明（7。規則にすると誤る考え方）

| 番号 | 見出し | 正解 | ChatGPT | 迷った種類と退けた理由 | ④値の形 | Claude の推論 |
|---|---|---|---|---|---|---|
| x0001 | GEO_CANT | id | address | id は考えたが、行を識別する番号ではなく canton を表すコード。category の単なる選択肢とも違い、地理的区域を指す。 | 1、2 の整数コード。コードの形だけなら ID にも見えるが、列名が示すのは場所。 | 「GEO_CANT」で 1,1,2＝州の番号。GEO_ の列名で値が整数→id だが、GEO_ は地名の列にもなる。規則にしない |
| x0002 | kategorie_sortierung | id | category | id も考えたが、記録を照合するキーではなくカテゴリの順番。quantity の件数とも読めない。 | 1、2、3 の小さい整数で、順序番号のように見える。 | b063-0300 と同じ（正解を見直す） |
| x0005 | sitzung_titel | id | text | date は開始日列が別にあり、id は Sitzung ID が別にあるため退ける。category の固定種別でもない。 | 61. Sitzung などの人が読めるタイトル表現。 | 「sitzung_titel」で「61. Sitzung」＝会の回の名前。正解は id だが、題名（titel）の列で文字の値なので text とも読める（正解を見直す） |
| x0011 | kategorie_sortierung | id | category | id は考えたが gruppe_id・analyt_id が別にある。quantity の件数でもなく、順序・順位として category。 | 1、2、5 などの順序整数。 | 「kategorie_sortierung」で 1,1,2＝並べる順の番号。正解は id だが、順位（Rank）の列は category と付いている（u Rank）。並び順・順位の正解をそろえる必要がある（正解を見直す） |
| x0015 | verteilzone | id | address | id も考えたが、地区・自治体と同じ場所軸。category は任意の分類群で地理区域ではない。 | 261_LZ、220_ZHa の英数字コードで区域を表している。 | 「verteilzone」で 261_LZ＝区域のコード。列名からは区分（category）とも読める。規則にしない |
| x0021 | verantwortlichkeit_abkuerzung | id | org | id も考えたが、隣に組織名と部門名があり、値は責任主体の略称として読める。account は abteilung 側。 | KTTGWH、BAFU の略称が反復し、組織・部門名を指す。 | 「verantwortlichkeit_abkuerzung」で KTTGWH・BAFU＝担当の役所の略号。本体は org。略号は org とも id とも読める。正解は id（正解を見直す） |
| x0029 | GOR CODE | id | address | id も候補だが、GOR が区域そのものを指定する地理分類で、列の役割は地域。 | H のような地域コード。値形のみなら ID に見える。 | 「GOR CODE」で H・H。列名が CODE で終わるのに category。recheck の \bcode$ は大文字小文字を問わないので当たるはず→見張りの段で category と言い切ったため recheck を通らない。言い |

## ChatGPT が決めなかった列（0）で「何があれば決められたか」に出た語

| 足りないもの | 列 |
|---|---:|
