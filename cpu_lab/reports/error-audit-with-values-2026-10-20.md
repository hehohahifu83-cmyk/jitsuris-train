# 誤り・保留例の値と兄弟列を使った監査（2026-10-20）

## 範囲と扱い

2026-10-20に回収した許可済み固定開発セットの誤りを、元の公開表から列値・兄弟列と照合した。blind set、セット3・5・7は開いていない。固定セットの行は原因調査だけに使い、候補・学習データにはコピーしない。モデル説明は内部状態の説明ではなく、観測された入力・出力からの仮説である。

## 行単位の監査

| 例（正解 → 予測） | 見せた根拠（値・周辺列） | モデルの出力と考えられる手掛かり | 迷う点・追加情報 | 原因の分類 / 判断 |
|---|---|---|---|---|
| `Total Invoices Paid` quantity → amount（sparse 0.995） | 値 `9,309`, `27,687`, `9,561`, `8,817`。兄弟列に `# Invoices Paid Within 5 Days/30 Days` と `% Invoices Paid...`。 | 金額らしい桁区切り数値と `Paid` に引かれ、件数をamountに寄せた可能性。 | 出典表・Fiscal Periodがあれば件数の意味は明瞭。値の単位が個別に付いていないことは入力上の弱点。 | quantityの定義は明確。請求件数の教材不足と数値特徴への過剰依存。合成対照例2件を単独高確信で追加。 |
| `# Invoices Paid Within 5 Days` quantity → amount（sparse 0.963） | 値 `23,147`, `7,373`, `8,151`, `7,623`。兄弟に `Total Invoices Paid`、30日件数、5日・30日割合。 | `#` を識別子や件数として扱えず、数値＋paidをamountとした可能性。 | `#` が列名にあり、表全体も件数・割合を対比する。 | 上と同じ。ラベル疑義なし。 |
| `Department`（値DOF） account（正解） ↔ `Department`（DOH/DFE） org（正解） | いずれも値は政府機関略号。兄弟に `Organisation`, `Check Date`, `Expense type`, `Supplier`, `Invoice number`, `Invoice Amount`。 | 同じような政府支出表の `Department` を account/org に分けている。 | DOFを他の略号と異なるラベルにする根拠が、記録された表情報からは見当たらない。原典の定義・教師の裁定記録が必要。 | **正解ラベル/ラベル境界の不整合候補。保留。** このラベルを教材にもガイド変更にも使わない。 |
| `keyword` category → text（sparse top text 0.847） | 値は `access to education`, `treatment of substance abuse`, `nutrition`, `soil pollution`, `school enrolment`。兄弟列は `goal`, `weight`, `color`。 | フレーズの羅列を自由語句と見てtextにした可能性。 | 値はタグの集合としてcategoryにも読める一方、LABEL_GUIDE v1.5 は「キーワードの羅列」をtextとしている。 | **明示的なガイドと正解の不一致。保留。** 教師の裁定が済むまで学習しない。 |
| `Author` person → org（sparse top org 0.713） | `sgt101`, `hvs`, `dllthomas` 等のユーザー名風値。兄弟列に `ID`, `Type`, `Story`, `Title`, `URL`, `Content`。 | 短い英数字ハンドルを組織コード風に扱った可能性。 | 元サイトでAuthor欄がユーザーアカウントを指すか、出典スキーマがあれば確定する。 | ガイドはユーザー名・ニックネームもpersonと明記。**教材不足/表現分布差**が有力。元行は使わず、ユーザー名例を含む追加教材は別途作る。 |
| `Authors` person → text（sparse top text 0.936） | `H Kakizaki, MO Fraser, WC De...` など複数著者名。兄弟列に `Title`, `Source`, `Publisher`, `DOI`, `ISSN`。 | 長いカンマ区切り文字列を自由記述として扱った可能性。 | 著者一覧として明らかな値だが、著者名の形式・個数は多様。 | personの定義は明確。**複数人表記の教材不足**。試験行は追加しない。 |
| `SurveyName` text → org | `1982 OPRU Jura and Islay sublittoral survey` 等の調査名。兄弟列は `StartDate`, `EndDate`, `LocationName`, `DataType`, `HabitatCode`。 | `Survey`という機関/団体名らしい語をorgとして拾った可能性。 | 調査名が特定組織名と一体化していないかは原典メタデータで確認できるが、値の形式はタイトル。 | textの定義は明確。**教材不足/列名の語彙差**が有力。 |
| `教材費` amount → category（sparse top category 0.514） | 値はすべて`0`。周辺に`受講料（単発/月額/年額）`、`入会金`。 | 全ゼロの値パターンに引かれ、費用を区分値のように扱った可能性。 | 元CSVの通貨単位・データ辞書は今回の行レコードにない。金額列群との並びは強い根拠。 | LABEL_GUIDEは0ばかりでも列名がお金ならamount。**値・単位情報の不足と数値パターンへの過剰依存**。確定した追加ルールはないため試験例を教材化しない。 |
| `FINE` amount → quantity | 値 `70`, `50`, `50`, `70`。兄弟列 `ISSUED`, `LOCATION`, `CONTRAVENTION`。 | 通貨記号なしの整数を数量とした可能性。 | 通貨単位が行データにはないが、駐車違反のfineは徴収額を表す。 | amountの定義は明確。**単位情報の不足/数字への過剰依存**。正解ラベルを変えない。 |
| `Sales-goods-svcs...` / `Miscellaneous...` amount → quantity（blend70はunknown） | 値には`0`, `206`, `349383`; 周辺に`Tax-revenues`, `Return-on-investments`, `Refunds`, `Amt-units`。 | 金額らしい大きな数が、amount単位情報なしでquantityに寄った可能性。blend70でも上位がquantity 0.416 / amount 0.106などで保留。 | 同表の`Amt-units`列の**値**（通貨・千ドルなど）と行レベルの会計単位が必要。兄弟列名だけでは確定不足。 | **モデル入力情報不足が主要候補**。額面・スケールだけで教材を作らない。 |
| `住家全壊` quantity → amount | 値 `0`, `0`, `0`, `0`, `-9999`。兄弟列は発生日、時刻、緯度・経度、発生市町村など災害記録。 | 全ゼロや負の欠損コードを数値金額と誤認した可能性。 | `-9999`の欠損値定義と原表の列説明があれば数量/欠損処理がより明確になる。 | quantityの意味は住宅全壊件数。**欠損コード処理と数値過剰依存**の候補。正解変更なし。 |
| `Pelicula` text → category（sparse top category 0.881） | 値 `Dirty Work`, `Hooper`, `Sinkin' in the Bathtub`, `Dawn of the Dead`, `Bus Stop`; 兄弟列`Id`。 | 外国語の短いタイトルを選択肢カテゴリのように見た可能性。 | 元データの列説明があると題名であることを明示できる。 | ガイドは映画・曲の題名をtextとする。**多言語の列名・題名表現の教材不足**。 |

## 変更した教材と評価経路

- 監査で高確信だった件数/金額の違いだけを、実試験行から独立した新規合成例2件にした。ChatGPT単独監査（監査者1人）として候補・レビュー記録・採用行を保存した。
- 他の事例は例示用学習データに転用していない。とくに `keyword` と `Department` は正解/ガイド間の揺れが解消するまで保留。
- `progress_probe.jsonl` の110件は内部生成のラベル付き診断用データとして既存。学習入力には含めない。CPU labだけで学習直前/直後の同じモデルを採点して、seed別のJSONを成果物に保存する処理を追加した。固定5試験の再利用だけで教材改善を判定しない。
- 実際の追加学習はまだ実行されていない。Kaggleが`QUEUED`の間だけCPU実験を許す既存ゲートがあり、現在はKaggleが完了状態である。したがって改善値は未計測。
