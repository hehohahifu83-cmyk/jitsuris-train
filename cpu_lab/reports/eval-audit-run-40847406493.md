# C3a・C3b・C3u 学習結果と固定5集合の全件監査

対象run: C3a `40777786620`、C3b `40789354990`、C3u `40847406493`。生成: 2026-10-29。

## 結論

- **C3a（金教材追加）は不採用**。新公開元6陣でC2比の正解率・unknown差がどちらも1.5ポイント未満だった。
- **C3b（銀A事前学習→金）は不採用**。新公開元6陣で正解率+0.8ポイント、unknown−1.2ポイントと差なし範囲で、重大誤りが2→7へ増えた。
- **C3u（UNIT見出し拡張後の再学習）は固定5集合ではC3aと明確な差を示していない**。8陣での最終採否はCPU予測run 40857063359の完了待ち。
- 固定5集合のartifactは5集合×5条件×3 seed＝**75ファイル**を全て照合した。自動生成 `ERROR_ANALYSIS.md` は正規表現がjob1/2とft/blend系だけに限定され、40/75ファイルしか集計していないため、本報告でseed3とsparseを補完した。

## 成果物と実装の確認

| 実験 | 評価artifact | モデルartifact | seed | 学習時間（秒） | 最大GPUメモリ |
|---|---:|---:|---:|---:|---:|
| C3a | 12858458125 | 12859342788 | 1 | 1526.3 | 5.46 GiB |
| C3a | 12858458125 | 12859342788 | 2 | 1555.6 | 5.55 GiB |
| C3a | 12858458125 | 12859342788 | 3 | 1553.7 | 5.47 GiB |
| C3b | 12864835318 | 12864187011 | 1 | 1659.4 | 5.66 GiB |
| C3b | 12864835318 | 12864187011 | 2 | 1700.0 | 5.65 GiB |
| C3b | 12864835318 | 12864187011 | 3 | 1655.8 | 5.66 GiB |
| C3u | 12888789308 | 12888908719 | 1 | 1687.2 | 5.46 GiB |
| C3u | 12888789308 | 12888908719 | 2 | 1654.4 | 5.55 GiB |
| C3u | 12888789308 | 12888908719 | 3 | 1661.7 | 5.47 GiB |

C3bの銀段は各seed 26,283行・1周で約150〜156秒。C3uは133,156学習行、token切り詰め807行（0.61%）。評価側の切り詰め率はgeneral 1.31%、business 0%、business2 0.72%、dev220 2.27%、japan_procurement 3.26%。個別の問題行が切り詰め対象だったかはartifactに記録されていない。

## 固定5集合：条件別の3 seed合計

表記は `正解率 / 誤り / other誤受理 / 重大 / unknown`。差はC3u−C3aで、絶対値1.5ポイント未満は差なし。

| 条件 | C3a | C3b | C3u | C3u−C3a 正解率 | C3u−C3a unknown率 | 判定 |
|---|---:|---:|---:|---:|---:|---|
| ft | 95.79% / 149 / 19 / 24 / 105 | 95.80% / 134 / 30 / 17 / 108 | 96.08% / 130 / 22 / 14 / 102 | +0.29pt | -0.05pt | 差なし |
| blend50 | 94.88% / 118 / 20 / 13 / 194 | 94.99% / 103 / 22 / 15 / 200 | 94.82% / 120 / 20 / 10 / 196 | -0.06pt | +0.03pt | 差なし |
| blend60 | 95.63% / 124 / 17 / 11 / 142 | 95.84% / 108 / 24 / 14 / 138 | 95.68% / 117 / 18 / 10 / 145 | +0.05pt | +0.05pt | 差なし |
| blend70 | 95.76% / 133 / 17 / 16 / 125 | 95.90% / 119 / 24 / 16 / 123 | 95.96% / 122 / 20 / 12 / 120 | +0.20pt | -0.08pt | 差なし |
| sparse | 91.53% / 303 / 90 / 90 / 156 | 91.53% / 303 / 90 / 90 / 156 | 91.53% / 303 / 90 / 90 / 156 | +0.00pt | +0.00pt | 差なし |

## C3u：固定5集合・seed別（全75ファイル）

| 集合 | 条件 | seed | 正解率 | 誤り | other誤受理 | 重大 | unknown |
|---|---|---:|---:|---:|---:|---:|---:|
| dev220 | ft | 1 | 95.91% | 7 | 0 | 2 | 2 |
| dev220 | ft | 2 | 97.27% | 4 | 0 | 1 | 2 |
| dev220 | ft | 3 | 97.27% | 5 | 0 | 1 | 1 |
| dev220 | blend50 | 1 | 93.18% | 7 | 0 | 1 | 8 |
| dev220 | blend50 | 2 | 93.64% | 7 | 0 | 1 | 7 |
| dev220 | blend50 | 3 | 93.64% | 7 | 0 | 1 | 7 |
| dev220 | blend60 | 1 | 96.82% | 5 | 0 | 1 | 2 |
| dev220 | blend60 | 2 | 97.27% | 5 | 0 | 1 | 1 |
| dev220 | blend60 | 3 | 97.73% | 4 | 0 | 1 | 1 |
| dev220 | blend70 | 1 | 96.82% | 5 | 0 | 1 | 2 |
| dev220 | blend70 | 2 | 97.27% | 5 | 0 | 1 | 1 |
| dev220 | blend70 | 3 | 97.27% | 4 | 0 | 1 | 2 |
| dev220 | sparse | 1 | 86.36% | 21 | 0 | 2 | 9 |
| dev220 | sparse | 2 | 86.36% | 21 | 0 | 2 | 9 |
| dev220 | sparse | 3 | 86.36% | 21 | 0 | 2 | 9 |
| general | ft | 1 | 93.47% | 7 | 7 | 1 | 11 |
| general | ft | 2 | 93.47% | 12 | 5 | 3 | 8 |
| general | ft | 3 | 92.69% | 10 | 5 | 0 | 13 |
| general | blend50 | 1 | 92.69% | 8 | 7 | 0 | 13 |
| general | blend50 | 2 | 92.69% | 8 | 5 | 0 | 15 |
| general | blend50 | 3 | 92.69% | 10 | 5 | 0 | 13 |
| general | blend60 | 1 | 93.47% | 7 | 6 | 0 | 12 |
| general | blend60 | 2 | 92.17% | 7 | 5 | 0 | 18 |
| general | blend60 | 3 | 92.69% | 8 | 4 | 0 | 16 |
| general | blend70 | 1 | 93.73% | 6 | 6 | 0 | 12 |
| general | blend70 | 2 | 93.21% | 8 | 5 | 1 | 13 |
| general | blend70 | 3 | 92.69% | 9 | 5 | 0 | 14 |
| general | sparse | 1 | 87.21% | 18 | 15 | 2 | 16 |
| general | sparse | 2 | 87.21% | 18 | 15 | 2 | 16 |
| general | sparse | 3 | 87.21% | 18 | 15 | 2 | 16 |
| business | ft | 1 | 95.71% | 12 | 0 | 0 | 9 |
| business | ft | 2 | 95.92% | 14 | 0 | 0 | 6 |
| business | ft | 3 | 95.51% | 15 | 1 | 0 | 6 |
| business | blend50 | 1 | 94.29% | 8 | 0 | 1 | 20 |
| business | blend50 | 2 | 94.69% | 10 | 0 | 0 | 16 |
| business | blend50 | 3 | 94.69% | 9 | 0 | 1 | 17 |
| business | blend60 | 1 | 95.31% | 10 | 0 | 1 | 13 |
| business | blend60 | 2 | 95.51% | 10 | 0 | 0 | 12 |
| business | blend60 | 3 | 95.71% | 11 | 0 | 1 | 10 |
| business | blend70 | 1 | 95.51% | 11 | 0 | 1 | 11 |
| business | blend70 | 2 | 95.51% | 12 | 0 | 0 | 10 |
| business | blend70 | 3 | 96.12% | 13 | 0 | 1 | 6 |
| business | sparse | 1 | 93.06% | 26 | 1 | 13 | 7 |
| business | sparse | 2 | 93.06% | 26 | 1 | 13 | 7 |
| business | sparse | 3 | 93.06% | 26 | 1 | 13 | 7 |
| business2 | ft | 1 | 96.52% | 15 | 2 | 2 | 17 |
| business2 | ft | 2 | 97.34% | 12 | 1 | 2 | 13 |
| business2 | ft | 3 | 96.72% | 17 | 1 | 2 | 14 |
| business2 | blend50 | 1 | 95.49% | 17 | 1 | 2 | 26 |
| business2 | blend50 | 2 | 95.70% | 14 | 1 | 1 | 27 |
| business2 | blend50 | 3 | 95.70% | 15 | 1 | 2 | 26 |
| business2 | blend60 | 1 | 96.00% | 17 | 1 | 2 | 21 |
| business2 | blend60 | 2 | 96.41% | 15 | 1 | 1 | 19 |
| business2 | blend60 | 3 | 96.11% | 18 | 1 | 2 | 19 |
| business2 | blend70 | 1 | 96.21% | 18 | 2 | 3 | 17 |
| business2 | blend70 | 2 | 96.82% | 13 | 1 | 1 | 17 |
| business2 | blend70 | 3 | 96.52% | 18 | 1 | 2 | 15 |
| business2 | sparse | 1 | 92.93% | 35 | 14 | 13 | 20 |
| business2 | sparse | 2 | 92.93% | 35 | 14 | 13 | 20 |
| business2 | sparse | 3 | 92.93% | 35 | 14 | 13 | 20 |
| japan_procurement | ft | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 1 | 98.91% | 0 | 0 | 0 | 1 |
| japan_procurement | blend50 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 98.91% | 0 | 0 | 0 | 1 |
| japan_procurement | blend60 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | sparse | 1 | 98.91% | 1 | 0 | 0 | 0 |
| japan_procurement | sparse | 2 | 98.91% | 1 | 0 | 0 | 0 |
| japan_procurement | sparse | 3 | 98.91% | 1 | 0 | 0 | 0 |

## C3uの全問題出力監査

- 問題出力 **1681件**、固有ケース **222件**（同じ列を条件・seedで繰り返した出力を統合）。重大出力 **136件**。
- raw正解→guardでunknown: 400、raw誤り→guardでunknown: 319、raw誤りを言い切り: 792、raw正解→後段で誤り: 0、後段が別の誤りへ変更: 0、other誤受理: 170。

### 判定理由（問題出力）

- `記録なし`: 962件
- `probability_below_threshold`: 329件
- `date_value_evidence_low`: 132件
- `other_class`: 124件
- `numeric_top2_too_close`: 97件
- `numeric_values_not_parseable`: 37件

### 固有ケース全件

各行の「観測」はartifactにある事実。「仮説」は追加確認前の推定で、ラベルは変更しない。

| 集合/index | 列名 | 正解 | 観測（条件×seed） | 重大 | 原因仮説・確度 | 追加確認 |
|---|---|---|---|---:|---|---|
| dev220/5 | 受注名 | person | unknown:unknown(probability_below_threshold)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/6 | 受注名カナ | person | wrong:account(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/12 | 発送先名 | person | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/13 | 発送先カナ | person | wrong:org(none)×3; unknown:unknown(probability_below_threshold)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/17 | 商品計 | amount | unknown:unknown(numeric_top2_too_close)×7 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/21 | ポイント | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/22 | その他費用 | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/27 | 作業者欄 | person | unknown:unknown(probability_below_threshold)×6 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/33 | 商品オプション | text | wrong:category(none)×4; unknown:unknown(probability_below_threshold)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/40 | メッセージ | text | wrong:category(none)×6 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/45 | 商品オプション | text | unknown:unknown(probability_below_threshold)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/60 | receive_order_import_type_id | category | wrong:id(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/65 | receive_order_customer_name | person | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/69 | receive_order_status_id | category | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/71 | receive_order_delivery_method_id | category | wrong:id(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/75 | 支払を受ける者の個人番号 | id | unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/128 | 担当課 | org | wrong:account(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/130 | 随意契約理由 | text | wrong:category(none)×2; unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/131 | 支出負担行為担当官 | person | unknown:unknown(probability_below_threshold)×6 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/143 | terms | category | wrong:text(none)×10 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/151 | taxable | category | wrong:tax_class(none)×6 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/156 | name | person | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| dev220/157 | is a company | category | wrong:org(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/168 | website | text | unknown:unknown(probability_below_threshold)×3; wrong:category(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/170 | tax id | id | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/171 | customer rank | quantity | wrong:category(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/172 | supplier rank | quantity | wrong:category(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/174 | sales order | id | unknown:unknown(numeric_top2_too_close)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/177 | purchase order by customer | id | wrong:quantity(none)×15 | 15 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| dev220/183 | material | product | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/195 | sales tax group | tax_class | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/196 | credit limit | amount | unknown:unknown(probability_below_threshold)×4; unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×1 | 1 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/197 | primary contact | person | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| dev220/201 | city | address | unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| dev220/211 | item description | text | unknown:unknown(probability_below_threshold)×3; wrong:category(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/1 | author | person | wrong:org(none)×11; unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/27 | keyword | category | wrong:text(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/32 | 五島 | other | other_ng:quantity(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/35 | denominatorunweighted | quantity | unknown:unknown(probability_below_threshold)×5; unknown:unknown(other_class)×4; wrong:id(none)×2; unknown:unknown(numeric_top2_too_close)×1 | 2 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/47 | mood | other | other_ng:category(none)×2 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/48 | source | category | wrong:org(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/53 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | wrong:quantity(none)×5 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/62 | nodes | other | other_ng:text(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/70 | lda | text | unknown:unknown(probability_below_threshold)×5 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/71 | property | category | unknown:unknown(other_class)×7; unknown:unknown(probability_below_threshold)×5 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/75 | データセット_キーワード | category | wrong:text(none)×7 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/83 | place | org | wrong:address(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/87 | sens_final | rate | unknown:unknown(other_class)×9 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/104 | term | text | wrong:category(none)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/105 | authors | person | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/112 | 住家全壊 | quantity | unknown:unknown(probability_below_threshold)×7; wrong:amount(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/121 | dag-stage | other | other_ng:category(none)×8; other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/131 | 学名 | other | other_ng:address(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/134 | dbpedia_score | other | other_ng:rate(none)×14 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/142 | 総観場3 | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/148 | mechanism | category | wrong:id(none)×4 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/156 | 発生経度確度(±秒) | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/175 | bib | id | unknown:unknown(other_class)×3; unknown:unknown(probability_below_threshold)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/188 | 被害域幅(m)最小 | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/207 | year_step_size | quantity | wrong:category(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/213 | age_q3_nd | quantity | unknown:unknown(probability_below_threshold)×5; wrong:rate(none)×1; unknown:unknown(numeric_top2_too_close)×1 | 1 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/224 | study | text | unknown:unknown(probability_below_threshold)×8; wrong:id(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/227 | 発生日 | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/233 | 天候 | category | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/234 | 発生県 | id | unknown:unknown(probability_below_threshold)×8; wrong:quantity(none)×3; wrong:address(none)×1 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/238 | 被害域長さ(100m)最小 | other | other_ng:quantity(none)×7 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/241 | 教材費 | amount | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/244 | 天候 | category | unknown:unknown(probability_below_threshold)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/246 | yearsincurrentrole | quantity | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/265 | pelicula | text | wrong:category(none)×4; unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/269 | female_frequency | rate | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/275 | attrition | category | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/281 | spotify_url | other | other_ng:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/282 | 読み方 | address | unknown:unknown(probability_below_threshold)×8; wrong:org(none)×4 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/286 | value | other | other_ng:rate(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/291 | cleaned | text | wrong:category(none)×10; unknown:unknown(probability_below_threshold)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/295 | units | category | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/296 | image_level_adj_acc | rate | unknown:unknown(other_class)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/302 | episode | other | other_ng:id(none)×9; other_ng:quantity(none)×1 | 0 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/308 | ステーション名 | org | wrong:address(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/309 | goal | id | wrong:category(none)×7; unknown:unknown(probability_below_threshold)×6; wrong:quantity(none)×2 | 2 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/310 | 駐車場 | category | unknown:unknown(numeric_values_not_parseable)×2; unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/317 | 日本語教室名 | org | unknown:unknown(probability_below_threshold)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/338 | denominatorweighted | quantity | unknown:unknown(other_class)×12 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| general/339 | characteristicorder | other | other_ng:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/340 | 登録年月日 | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/341 | 次に掲げるもの | category | unknown:unknown(probability_below_threshold)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/342 | age_q1_nd | quantity | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/343 | mt2 | other | other_ng:quantity(none)×9; other_ng:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/351 | operationid | other | other_ng:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/352 | 法人代表者名及び役職 | person | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/353 | 入会金 | amount | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/357 | de | text | wrong:category(none)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/362 | raw | category | unknown:unknown(probability_below_threshold)×7; wrong:text(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/370 | source_value | category | unknown:unknown(probability_below_threshold)×8; wrong:text(none)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| general/380 | 科名 | category | unknown:unknown(other_class)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| general/382 | source | category | wrong:text(none)×3; unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/41 | total invoices paid | quantity | wrong:amount(none)×9; unknown:unknown(numeric_top2_too_close)×4; unknown:unknown(probability_below_threshold)×1 | 9 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/42 | # invoices paid within 5 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/43 | # invoices paid within 30 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/46 | quarterno | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/77 | publisher label | org | unknown:unknown(probability_below_threshold)×8; wrong:category(none)×4; wrong:address(none)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/82 | la budget allocated to nursing care | amount | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/84 | department | org | wrong:account(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/92 | department | org | wrong:account(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/101 | entitiy | org | wrong:account(none)×7; unknown:unknown(probability_below_threshold)×5 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/148 | merchant details | text | wrong:category(none)×12; wrong:org(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/199 | department | org | wrong:account(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/215 | account_name | account | wrong:org(none)×2; unknown:unknown(probability_below_threshold)×1 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/225 | description | account | wrong:text(none)×11; unknown:unknown(probability_below_threshold)×1 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/237 | purposeofexpenditure | text | wrong:account(none)×15 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/238 | procurementclassification:proclasslabel | account | wrong:category(none)×8 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/269 | net current expenditure - min all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/270 | net current expenditure - ave all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/271 | net current expenditure - max english county councils | amount | wrong:quantity(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/278 | 目名 | category | unknown:unknown(other_class)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/279 | 科名 | category | unknown:unknown(other_class)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/288 | respnum$ | id | unknown:unknown(probability_below_threshold)×1; unknown:unknown(numeric_top2_too_close)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/318 | number-of-disputes_nombre-de-différends | quantity | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/332 | segment | id | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/335 | family | id | unknown:unknown(probability_below_threshold)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business/342 | commodity-title_en | product | unknown:unknown(probability_below_threshold)×7; wrong:category(none)×4; wrong:text(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/343 | commodity-title_fr | product | unknown:unknown(probability_below_threshold)×7 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/344 | portefeuille_nom_et_code | org | unknown:unknown(probability_below_threshold)×7; wrong:account(none)×4; wrong:category(none)×3; wrong:id(none)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/347 | regrp_sommaire | account | wrong:category(none)×8; unknown:unknown(probability_below_threshold)×4; unknown:unknown(numeric_values_not_parseable)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/348 | regrp_nom | account | unknown:unknown(probability_below_threshold)×6; wrong:text(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/401 | ligne | category | wrong:id(none)×6; unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/403 | tournée | id | wrong:category(none)×2; unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/404 | type de matériel | category | wrong:id(none)×2; unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/406 | mois calendrier | date | unknown:unknown(date_value_evidence_low)×12; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/408 | km budgété | other | other_ng:amount(none)×3; other_ng:quantity(none)×1 | 0 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/421 | abn | id | wrong:amount(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/445 | regions | address | wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/451 | title | category | wrong:text(none)×7; wrong:account(none)×4; unknown:unknown(probability_below_threshold)×4 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business/457 | defence goods value | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/458 | defence services value | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/459 | australian sourced goods | amount | unknown:unknown(probability_below_threshold)×4; unknown:unknown(numeric_top2_too_close)×3; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/460 | australian sourced services | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/461 | overseas sourced goods | amount | unknown:unknown(probability_below_threshold)×4; unknown:unknown(numeric_top2_too_close)×3; wrong:id(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business/468 | project name | text | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/11 | merchant description | category | wrong:org(none)×9; unknown:unknown(probability_below_threshold)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/45 | type | account | wrong:category(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/58 | numbers of | date | unknown:unknown(probability_below_threshold)×5; wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×2 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/75 | monitor | id | wrong:category(none)×11; unknown:unknown(probability_below_threshold)×4 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/90 | total invoices paid | quantity | wrong:amount(none)×8; unknown:unknown(numeric_top2_too_close)×5 | 8 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/91 | # invoices paid within 5 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/92 | # invoices paid within 30 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/113 | column6 | text | wrong:address(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/127 | a1 (retail) floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/128 | a1 (retail) floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/129 | a2 floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/130 | a2 floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/131 | a2 floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/132 | b1a floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/133 | b1a floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/134 | b1a floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/135 | d2 floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/136 | d2 floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/137 | d2 floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/140 | surveyname | text | unknown:unknown(probability_below_threshold)×3; wrong:org(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/149 | projection | category | wrong:id(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/151 | habitatdescription | text | unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/154 | surveyname | text | unknown:unknown(probability_below_threshold)×4 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/159 | locationname | address | unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/163 | projection | category | wrong:id(none)×15 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/176 | contravention | category | unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/177 | fine | amount | unknown:unknown(probability_below_threshold)×9; unknown:unknown(other_class)×3; wrong:id(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/179 | location | address | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/202 | net current expenditure - min all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/203 | net current expenditure - ave all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/204 | net current expenditure - max english county councils | amount | wrong:quantity(none)×3 | 3 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/230 | warddesc | address | wrong:category(none)×14 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/233 | super output area 2011 name | address | unknown:unknown(probability_below_threshold)×3; wrong:org(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/238 | terrace | quantity | unknown:unknown(other_class)×6; unknown:unknown(probability_below_threshold)×6 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/288 | construction_age_band | category | unknown:unknown(probability_below_threshold)×4; wrong:id(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/291 | epc_score_known | category | unknown:unknown(probability_below_threshold)×7 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/298 | number_habitable_rooms | quantity | wrong:category(none)×13; unknown:unknown(numeric_values_not_parseable)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/299 | number_habitable_rooms_known | category | wrong:quantity(none)×12; unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/301 | total_floor_area_known | category | unknown:unknown(other_class)×8; unknown:unknown(probability_below_threshold)×4; wrong:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/317 | energy_consumption | other | other_ng:quantity(none)×12 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/318 | energy_consumption_known | category | wrong:quantity(none)×4 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/319 | solar_pv_area | other | other_ng:id(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/321 | avg_tilt | other | other_ng:quantity(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/322 | imd19_national_decile | category | unknown:unknown(probability_below_threshold)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/325 | loac_group | category | wrong:address(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/326 | fuel_poverty | rate | unknown:unknown(other_class)×2; unknown:unknown(probability_below_threshold)×2; wrong:category(none)×2 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/356 | want to live in this parish only | quantity | wrong:category(none)×2 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/370 | average bids per property | other | other_ng:rate(none)×3; other_ng:amount(none)×2 | 0 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/379 | terrace | quantity | unknown:unknown(other_class)×6; unknown:unknown(probability_below_threshold)×6 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/381 | total_verified_sales | quantity | unknown:unknown(numeric_top2_too_close)×7; wrong:amount(none)×5 | 5 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/440 | situtation | address | wrong:category(none)×12; wrong:text(none)×2; unknown:unknown(probability_below_threshold)×1 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/443 | tree type | category | unknown:unknown(other_class)×1; unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/492 | value () | amount | unknown:unknown(numeric_values_not_parseable)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/499 | county | address | wrong:org(none)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/501 | value | amount | unknown:unknown(probability_below_threshold)×3; unknown:unknown(numeric_top2_too_close)×3; wrong:rate(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/531 | value | quantity | unknown:unknown(numeric_top2_too_close)×6; wrong:amount(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/535 | scheme_description | category | wrong:text(none)×6; unknown:unknown(probability_below_threshold)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/542 | percentage (%) of the total amount paid | rate | unknown:unknown(numeric_values_not_parseable)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/548 | health service executive area | address | wrong:org(none)×6; unknown:unknown(probability_below_threshold)×2 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/562 | name | org | wrong:address(none)×14 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/581 | type of expenditure | account | wrong:category(none)×11 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/625 | household income decile | category | wrong:address(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/667 | value | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/825 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/838 | value | quantity | unknown:unknown(numeric_top2_too_close)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/864 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/874 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/883 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/918 | value | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/926 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/946 | service_responsable | account | wrong:category(none)×14 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/948 | numéro_uev | id | wrong:address(none)×12; unknown:unknown(probability_below_threshold)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/955 | flow | category | unknown:unknown(other_class)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/956 | terminal | address | unknown:unknown(probability_below_threshold)×9; wrong:category(none)×3 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/959 | numéro | id | wrong:address(none)×6; unknown:unknown(probability_below_threshold)×1 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/962 | service | account | unknown:unknown(probability_below_threshold)×7; wrong:org(none)×5; wrong:category(none)×3 | 0 | 有限分類語と自由文/ID/業務科目の境界、またはラベル定義差（中） | 出典表とLABEL_GUIDE根拠を先生2人で独立確認 |
| business2/970 | return-on-investments_revenus-de-placements | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 見出しの多義性・出典固有語・周辺文脈不足（中） | 値、題名、兄弟列、出典定義を確認 |
| business2/971 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown:unknown(numeric_top2_too_close)×6; wrong:quantity(none)×3; unknown:unknown(probability_below_threshold)×1 | 3 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| business2/974 | miscellaneous_divers | amount | wrong:quantity(none)×15 | 15 | 数値意味・単位文脈の不足またはラベル境界（中） | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/975 | amt-units_mnt-unite | category | unknown:unknown(probability_below_threshold)×4 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |
| japan_procurement/83 | 資産名称 | text | wrong:org(none)×3; unknown:unknown(probability_below_threshold)×2 | 0 | guard/evidence規則が厳しすぎる機構は確認済み（高）。根本の入力証拠不足は未確定 | guard理由と値形式、UNIT・題名・兄弟列を照合 |

## 再発性と原因のまとめ

- 15通り（5条件×3 seed）のうち10回以上問題になった固有ケースは **81件**。seed依存だけでは説明できない系統的な失敗。
- 重大誤りはquantity↔amountなどの数値意味、generalのラベル境界、business2のID/住所/分類境界に集中する。個々の根本原因は値・UNIT・兄弟列をartifactが保持していないため未確定。
- guardは一部のraw誤りをunknownへ退避させる一方、raw正解もunknownへ変えている。安全性とunknown率の交換条件が確認できる。
- C3uの変更はUNIT見出し拡張と、学習に新しく届く単位例93列（約0.3%）。固定5集合で差なしなのは変更量が小さい仮説と整合するが、因果は8陣評価完了前には断定しない。
- C3bは銀AがC2予測との一致で作られており、C2の癖を強める選択バイアスがある。新公開元6陣で重大2→7になった事実はあるが、どの銀行が各誤りを生んだかは影響関数等を測っておらず未確定。

## ラベル・重複・データ漏洩・実装の監査

- 固定5集合のordered/unordered SHAは3実験・3 seedで一致し、同じ評価対象を比較している。
- 学習除外はC3aがb015/b016/b017/b060/b062/b063、C3uはさらにb064/b065を除外。開発陣の直接学習混入は設定上防いでいる。固定5集合と教材庫の行単位重複はartifactだけでは再検査できず、未確認。
- ラベル疑義は本監査では変更していない。曖昧ケースはChatGPT・Claudeの独立確認と根拠裁定が必要。
- tokenizerは3実験とも同じE5-base revision。C3uの評価切り詰め率は集合別0〜3.26%だが、問題行との対応がないため切り詰め原因は未確認。
- `ERROR_ANALYSIS.md`の40/75ファイル集計は、`cpu_lab/error_analysis.py`の正規表現が`job[12]`かつsparse除外であることが原因。評価artifact自体は75ファイル揃っており、本監査は全件を読み直した。

## 改善案（優先順、一度に一要因）

1. **高**：進行中のC3u 8陣評価を完了し、事前規則で採否を確定する。期待効果はUNIT見出し変更の実測。副作用はなし。
2. **高**：自動監査をjob1〜3・sparse対応へ直し、raw/guard/UNIT/token長を行別に保存する。期待効果は原因切り分け。副作用はartifact増加。
3. **高**：所得帯の申告件数などamount/quantityの対照教材を、評価行を流用せず別出典から集める。期待効果は重大誤り低減。副作用はunknown増加またはamount再現率低下。
4. **中**：銀Aをクラス上限・出典上限付きで再構成し、金のみ→銀A→金の一要因再試験をする。期待効果はid偏重とC2同意バイアスの低減。副作用は教材量減少。
5. **中**：rho/amount veto/guardを開発陣で一要因ずつ再検証し、重大≤0.2%とunknown≤10%の交換条件を記録する。副作用は正解率低下。

## 未確認・制約

- 固定5集合の問題行は列名・正解・予測・確率・guard理由まで確認した。元の値、抽出UNIT、題名、兄弟列、出典URL、行別token長はartifactにないため、ラベル・文脈・前処理の根本原因は未確定。
- ChatGPT・Claudeとの同一課題比較は今回実施していない。比較目標は維持し、Geminiは除外する。
- blind_set*、セット3・5・7、b018の中身は読んでいない。固定5集合の問題行は教材へ転用しない。
