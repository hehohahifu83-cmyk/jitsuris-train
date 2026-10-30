# C3s（掃除した銀）固定5集合の全件監査

対象run: `40859140256`。生成: 2026-10-30。対象は許可された dev220・general・business・business2・japan_procurement のみ。

## 結論

- Kaggle学習と3 seed評価はCOMPLETE。評価artifact `12895025977`（154ファイル）とモデルartifact `12894990932`を分けて確認した。
- C3sは新公開元8陣でC3a比が正83.7→83.9%、unknown 12.1→12.0%、重大2→4。正解率・unknownは1.5ポイント未満の差で、重大が増えたため不採用。
- 固定5集合の5条件×3 seed＝75予測ファイルを全て再集計した。下表のC3s−C3aは全条件で1.5ポイント未満であり、固定5集合でも能力向上は実証されない。
- ラベル疑義は変更していない。各固有ケースの仮説は追加確認前の推定である。

## 成果物・学習資源

| seed | 学習行 | 学習時間 | 最大GPUメモリ | 銀教材 |
|---:|---:|---:|---:|---|
| 1 | 133,156 | 1521.3秒 | 5.6 GiB | train_Aclean 16,586列・1周 |
| 2 | 133,156 | 1557.4秒 | 5.7 GiB | train_Aclean 16,586列・1周 |
| 3 | 133,156 | 1521.1秒 | 5.6 GiB | train_Aclean 16,586列・1周 |

Kaggleログで確認したseed 1/2/3の学習ループは1521/1557/1521秒、最大GPUメモリは5.6/5.7/5.6 GiB、学習行はいずれも133,156行。

## 固定5集合：条件別3 seed合計

表記は `正解率 / 誤り / other誤受理 / 重大 / unknown`。

| 条件 | C3a | C3s | 正解率差 | unknown率差 | 判定 |
|---|---:|---:|---:|---:|---|
| ft | 95.79% / 149 / 19 / 24 / 105 | 95.50% / 151 / 24 / 20 / 117 | -0.29pt | +0.19pt | 差なし |
| blend50 | 94.88% / 118 / 20 / 13 / 194 | 94.72% / 111 / 24 / 13 / 207 | -0.15pt | +0.20pt | 差なし |
| blend60 | 95.63% / 124 / 17 / 11 / 142 | 95.54% / 123 / 24 / 12 / 142 | -0.09pt | +0.00pt | 差なし |
| blend70 | 95.76% / 133 / 17 / 16 / 125 | 95.68% / 135 / 26 / 16 / 119 | -0.08pt | -0.09pt | 差なし |
| sparse | 91.53% / 303 / 90 / 90 / 156 | 91.53% / 303 / 90 / 90 / 156 | +0.00pt | +0.00pt | 差なし |

## C3s seed別

| 集合 | 条件 | seed | 正解率 | 誤り | other誤受理 | 重大 | unknown |
|---|---|---:|---:|---:|---:|---:|---:|
| dev220 | ft | 1 | 97.27% | 6 | 0 | 1 | 0 |
| dev220 | ft | 2 | 95.45% | 10 | 0 | 2 | 0 |
| dev220 | ft | 3 | 97.73% | 5 | 0 | 1 | 0 |
| dev220 | blend50 | 1 | 94.09% | 7 | 0 | 1 | 6 |
| dev220 | blend50 | 2 | 94.09% | 6 | 0 | 1 | 7 |
| dev220 | blend50 | 3 | 95.00% | 6 | 0 | 1 | 5 |
| dev220 | blend60 | 1 | 96.82% | 7 | 0 | 1 | 0 |
| dev220 | blend60 | 2 | 96.36% | 7 | 0 | 1 | 1 |
| dev220 | blend60 | 3 | 98.18% | 4 | 0 | 1 | 0 |
| dev220 | blend70 | 1 | 96.82% | 6 | 0 | 1 | 1 |
| dev220 | blend70 | 2 | 95.91% | 8 | 0 | 1 | 1 |
| dev220 | blend70 | 3 | 97.73% | 5 | 0 | 1 | 0 |
| dev220 | sparse | 1 | 86.36% | 21 | 0 | 2 | 9 |
| dev220 | sparse | 2 | 86.36% | 21 | 0 | 2 | 9 |
| dev220 | sparse | 3 | 86.36% | 21 | 0 | 2 | 9 |
| general | ft | 1 | 91.91% | 10 | 5 | 1 | 16 |
| general | ft | 2 | 91.91% | 11 | 6 | 2 | 14 |
| general | ft | 3 | 91.38% | 13 | 7 | 1 | 13 |
| general | blend50 | 1 | 92.69% | 6 | 5 | 0 | 17 |
| general | blend50 | 2 | 92.17% | 9 | 6 | 0 | 15 |
| general | blend50 | 3 | 92.69% | 10 | 7 | 0 | 11 |
| general | blend60 | 1 | 92.69% | 6 | 6 | 0 | 16 |
| general | blend60 | 2 | 92.69% | 10 | 5 | 0 | 13 |
| general | blend60 | 3 | 92.43% | 11 | 6 | 0 | 12 |
| general | blend70 | 1 | 93.21% | 10 | 6 | 1 | 10 |
| general | blend70 | 2 | 92.43% | 10 | 6 | 0 | 13 |
| general | blend70 | 3 | 92.17% | 11 | 7 | 1 | 12 |
| general | sparse | 1 | 87.21% | 18 | 15 | 2 | 16 |
| general | sparse | 2 | 87.21% | 18 | 15 | 2 | 16 |
| general | sparse | 3 | 87.21% | 18 | 15 | 2 | 16 |
| business | ft | 1 | 96.12% | 11 | 1 | 0 | 7 |
| business | ft | 2 | 96.12% | 12 | 0 | 0 | 7 |
| business | ft | 3 | 96.53% | 11 | 0 | 1 | 6 |
| business | blend50 | 1 | 95.10% | 6 | 0 | 0 | 18 |
| business | blend50 | 2 | 94.69% | 10 | 0 | 1 | 16 |
| business | blend50 | 3 | 94.69% | 10 | 0 | 1 | 16 |
| business | blend60 | 1 | 96.12% | 8 | 0 | 0 | 11 |
| business | blend60 | 2 | 95.92% | 10 | 0 | 0 | 10 |
| business | blend60 | 3 | 95.92% | 10 | 0 | 1 | 10 |
| business | blend70 | 1 | 96.33% | 9 | 0 | 0 | 9 |
| business | blend70 | 2 | 95.92% | 11 | 0 | 0 | 9 |
| business | blend70 | 3 | 96.33% | 11 | 0 | 1 | 7 |
| business | sparse | 1 | 93.06% | 26 | 1 | 13 | 7 |
| business | sparse | 2 | 93.06% | 26 | 1 | 13 | 7 |
| business | sparse | 3 | 93.06% | 26 | 1 | 13 | 7 |
| business2 | ft | 1 | 95.49% | 24 | 1 | 2 | 19 |
| business2 | ft | 2 | 95.70% | 21 | 2 | 5 | 19 |
| business2 | ft | 3 | 96.41% | 17 | 2 | 4 | 16 |
| business2 | blend50 | 1 | 94.88% | 18 | 2 | 3 | 30 |
| business2 | blend50 | 2 | 95.08% | 12 | 3 | 2 | 33 |
| business2 | blend50 | 3 | 95.39% | 11 | 1 | 3 | 33 |
| business2 | blend60 | 1 | 95.49% | 20 | 2 | 2 | 22 |
| business2 | blend60 | 2 | 95.59% | 15 | 3 | 3 | 25 |
| business2 | blend60 | 3 | 96.00% | 15 | 2 | 3 | 22 |
| business2 | blend70 | 1 | 95.70% | 21 | 2 | 2 | 19 |
| business2 | blend70 | 2 | 95.90% | 16 | 3 | 4 | 21 |
| business2 | blend70 | 3 | 96.31% | 17 | 2 | 4 | 17 |
| business2 | sparse | 1 | 92.93% | 35 | 14 | 13 | 20 |
| business2 | sparse | 2 | 92.93% | 35 | 14 | 13 | 20 |
| business2 | sparse | 3 | 92.93% | 35 | 14 | 13 | 20 |
| japan_procurement | ft | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | ft | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend50 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend60 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 1 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 2 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | blend70 | 3 | 100.00% | 0 | 0 | 0 | 0 |
| japan_procurement | sparse | 1 | 98.91% | 1 | 0 | 0 | 0 |
| japan_procurement | sparse | 2 | 98.91% | 1 | 0 | 0 | 0 |
| japan_procurement | sparse | 3 | 98.91% | 1 | 0 | 0 | 0 |

## 全問題出力の監査

- 問題出力 **1752件**、固有ケース **245件**、重大出力 **151件**。
- 機構別: raw誤りを言い切り 823、raw正解→guardでunknown 408、raw誤り→guardでunknown 333、other誤受理 188。
- 判定理由: `記録なし` 1011、`probability_below_threshold` 330、`date_value_evidence_low` 136、`other_class` 130、`numeric_top2_too_close` 99、`numeric_values_not_parseable` 46。

### 固有ケース全件

| 集合/index | 列名 | 正解 | 観測（条件×seed） | 重大 | 原因仮説 | 確度 | 追加確認 |
|---|---|---|---|---:|---|---|---|
| dev220/5 | 受注名 | person | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/6 | 受注名カナ | person | wrong:account(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/12 | 発送先名 | person | wrong:org(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/13 | 発送先カナ | person | unknown:unknown(probability_below_threshold)×1; wrong:org(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/17 | 商品計 | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/21 | ポイント | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/22 | その他費用 | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/27 | 作業者欄 | person | unknown:unknown(probability_below_threshold)×6 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/33 | 商品オプション | text | wrong:category(none)×3; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/40 | メッセージ | text | wrong:category(none)×6 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/45 | 商品オプション | text | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/60 | receive_order_import_type_id | category | wrong:id(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/65 | receive_order_customer_name | person | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/69 | receive_order_status_id | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/71 | receive_order_delivery_method_id | category | wrong:id(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/116 | 履行場所 | address | wrong:id(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/128 | 担当課 | org | wrong:account(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/130 | 随意契約理由 | text | wrong:category(none)×6 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/131 | 支出負担行為担当官 | person | unknown:unknown(probability_below_threshold)×6 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/143 | terms | category | wrong:text(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/146 | description | text | wrong:category(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/151 | taxable | category | wrong:tax_class(none)×10; unknown:unknown(probability_below_threshold)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/156 | name | person | wrong:org(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/157 | is a company | category | wrong:org(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| dev220/168 | website | text | unknown:unknown(probability_below_threshold)×3; wrong:category(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/171 | customer rank | quantity | wrong:category(none)×15 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| dev220/172 | supplier rank | quantity | wrong:category(none)×15 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| dev220/174 | sales order | id | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/177 | purchase order by customer | id | wrong:quantity(none)×15 | 15 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| dev220/183 | material | product | wrong:category(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/195 | sales tax group | tax_class | wrong:category(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/196 | credit limit | amount | unknown:unknown(numeric_top2_too_close)×2; unknown:unknown(probability_below_threshold)×1; wrong:quantity(none)×1 | 1 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| dev220/197 | primary contact | person | wrong:category(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/201 | city | address | wrong:id(none)×8 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| dev220/211 | item description | text | wrong:category(none)×3; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/1 | author | person | unknown:unknown(probability_below_threshold)×2; wrong:org(none)×9 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/2 | artist | person | unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/27 | keyword | category | wrong:text(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/32 | 五島 | other | other_ng:quantity(none)×14 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/35 | denominatorunweighted | quantity | unknown:unknown(other_class)×5; unknown:unknown(probability_below_threshold)×5; wrong:id(none)×2 | 2 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/47 | mood | other | other_ng:category(none)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/48 | source | category | unknown:unknown(probability_below_threshold)×2; wrong:org(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/53 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | wrong:quantity(none)×4 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/62 | nodes | other | other_ng:text(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/63 | ブロモホルム | other | other_ng:quantity(none)×2 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/65 | app | category | unknown:unknown(other_class)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/70 | lda | text | unknown:unknown(probability_below_threshold)×8 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/71 | property | category | unknown:unknown(other_class)×8; unknown:unknown(probability_below_threshold)×4 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/75 | データセット_キーワード | category | wrong:text(none)×9 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/83 | place | org | wrong:address(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/87 | sens_final | rate | unknown:unknown(other_class)×7 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/105 | authors | person | wrong:org(none)×3; unknown:unknown(probability_below_threshold)×1 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| general/112 | 住家全壊 | quantity | unknown:unknown(probability_below_threshold)×7; wrong:amount(none)×3; unknown:unknown(numeric_top2_too_close)×1 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/121 | dag-stage | other | other_ng:category(none)×8; other_ng:quantity(none)×7 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/131 | 学名 | other | other_ng:address(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/134 | dbpedia_score | other | other_ng:rate(none)×12 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/142 | 総観場3 | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/152 | 東第5 | quantity | unknown:unknown(numeric_top2_too_close)×1; unknown:unknown(date_value_evidence_low)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/156 | 発生経度確度(±秒) | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/174 | domain | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/175 | bib | id | unknown:unknown(other_class)×4; unknown:unknown(probability_below_threshold)×2; unknown:unknown(date_value_evidence_low)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/188 | 被害域幅(m)最小 | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/190 | organization name | org | wrong:person(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/197 | age_q3 | quantity | wrong:rate(none)×1; unknown:unknown(numeric_top2_too_close)×2; unknown:unknown(probability_below_threshold)×2 | 1 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/207 | year_step_size | quantity | wrong:category(none)×15 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/213 | age_q3_nd | quantity | unknown:unknown(numeric_top2_too_close)×1; unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/224 | study | text | unknown:unknown(probability_below_threshold)×3; wrong:id(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/227 | 発生日 | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/233 | 天候 | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/234 | 発生県 | id | unknown:unknown(probability_below_threshold)×9; wrong:quantity(none)×3; wrong:address(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/237 | ngram | text | wrong:category(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/238 | 被害域長さ(100m)最小 | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/241 | 教材費 | amount | wrong:category(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/244 | 天候 | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/246 | yearsincurrentrole | quantity | wrong:category(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/265 | pelicula | text | wrong:category(none)×4; unknown:unknown(probability_below_threshold)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/269 | female_frequency | rate | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/275 | attrition | category | wrong:quantity(none)×4; unknown:unknown(probability_below_threshold)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/281 | spotify_url | other | other_ng:category(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/282 | 読み方 | address | wrong:org(none)×4; unknown:unknown(probability_below_threshold)×10 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| general/286 | value | other | other_ng:rate(none)×15 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/291 | cleaned | text | wrong:category(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/295 | units | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/296 | image_level_adj_acc | rate | unknown:unknown(other_class)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/302 | episode | other | other_ng:id(none)×13 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/306 | 和名 | other | other_ng:address(none)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/308 | ステーション名 | org | wrong:address(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/309 | goal | id | wrong:quantity(none)×3; wrong:category(none)×9; unknown:unknown(probability_below_threshold)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/310 | 駐車場 | category | unknown:unknown(numeric_values_not_parseable)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/315 | standardhours | quantity | unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/317 | 日本語教室名 | org | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/338 | denominatorweighted | quantity | unknown:unknown(other_class)×12 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/339 | characteristicorder | other | other_ng:category(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/340 | 登録年月日 | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/341 | 次に掲げるもの | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/342 | age_q1_nd | quantity | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/343 | mt2 | other | other_ng:category(none)×5; other_ng:quantity(none)×8 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/351 | operationid | other | other_ng:category(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/352 | 法人代表者名及び役職 | person | wrong:category(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| general/353 | 入会金 | amount | wrong:category(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| general/362 | raw | category | wrong:text(none)×3; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/370 | source_value | category | unknown:unknown(probability_below_threshold)×4; wrong:text(none)×2 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/377 | indicator | text | wrong:category(none)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| general/380 | 科名 | category | unknown:unknown(other_class)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| general/382 | source | category | wrong:text(none)×6; unknown:unknown(probability_below_threshold)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/41 | total invoices paid | quantity | wrong:amount(none)×8; unknown:unknown(numeric_top2_too_close)×5 | 8 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/42 | # invoices paid within 5 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/43 | # invoices paid within 30 days | quantity | wrong:amount(none)×3; unknown:unknown(numeric_top2_too_close)×2 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/46 | quarterno | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/77 | publisher label | org | wrong:address(none)×6; wrong:category(none)×3; unknown:unknown(probability_below_threshold)×5 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/82 | la budget allocated to nursing care | amount | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/84 | department | org | wrong:account(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/92 | department | org | wrong:account(none)×14 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/101 | entitiy | org | wrong:account(none)×7; unknown:unknown(probability_below_threshold)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/136 | capital revenue | category | wrong:account(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/148 | merchant details | text | wrong:category(none)×8; wrong:org(none)×7 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/199 | department | org | wrong:account(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/225 | description | account | wrong:text(none)×12 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/237 | purposeofexpenditure | text | wrong:account(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/238 | procurementclassification:proclasslabel | account | wrong:category(none)×8 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/269 | net current expenditure - min all english county councils | amount | wrong:quantity(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/270 | net current expenditure - ave all english county councils | amount | wrong:quantity(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/271 | net current expenditure - max english county councils | amount | wrong:quantity(none)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/278 | 目名 | category | unknown:unknown(other_class)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/279 | 科名 | category | unknown:unknown(other_class)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/303 | d1 | category | wrong:quantity(none)×1 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/304 | d2 | category | unknown:unknown(probability_below_threshold)×2 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/308 | d6 | category | unknown:unknown(probability_below_threshold)×2 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/318 | number-of-disputes_nombre-de-différends | quantity | wrong:category(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/320 | dispute-status_statut-de-différend-fra | category | wrong:text(none)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/334 | segment-title_fr | category | wrong:account(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/335 | family | id | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/342 | commodity-title_en | product | wrong:category(none)×1; wrong:text(none)×3; unknown:unknown(probability_below_threshold)×10 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business/343 | commodity-title_fr | product | unknown:unknown(probability_below_threshold)×5 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/344 | portefeuille_nom_et_code | org | unknown:unknown(probability_below_threshold)×11; wrong:category(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/347 | regrp_sommaire | account | wrong:category(none)×8; unknown:unknown(numeric_values_not_parseable)×3; unknown:unknown(probability_below_threshold)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/348 | regrp_nom | account | wrong:text(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/401 | ligne | category | wrong:id(none)×3; unknown:unknown(probability_below_threshold)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/406 | mois calendrier | date | unknown:unknown(date_value_evidence_low)×12; wrong:id(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business/408 | km budgété | other | other_ng:amount(none)×3; other_ng:quantity(none)×1 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/421 | abn | id | wrong:amount(none)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/445 | regions | address | wrong:category(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business/451 | title | category | wrong:text(none)×8; unknown:unknown(probability_below_threshold)×6 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business/457 | defence goods value | amount | wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/458 | defence services value | amount | wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/459 | australian sourced goods | amount | wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/460 | australian sourced services | amount | wrong:id(none)×3; unknown:unknown(probability_below_threshold)×1; unknown:unknown(numeric_top2_too_close)×2 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/461 | overseas sourced goods | amount | wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×3; unknown:unknown(probability_below_threshold)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business/468 | project name | text | wrong:org(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/5 | account name | account | wrong:org(none)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/11 | merchant description | category | wrong:org(none)×10; unknown:unknown(probability_below_threshold)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/45 | type | account | wrong:category(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/58 | numbers of | date | unknown:unknown(probability_below_threshold)×6; wrong:id(none)×3; unknown:unknown(numeric_top2_too_close)×2 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/75 | monitor | id | wrong:category(none)×9; unknown:unknown(probability_below_threshold)×6 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/90 | total invoices paid | quantity | unknown:unknown(numeric_top2_too_close)×6; wrong:amount(none)×7 | 7 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/91 | # invoices paid within 5 days | quantity | wrong:amount(none)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/92 | # invoices paid within 30 days | quantity | wrong:amount(none)×3; unknown:unknown(numeric_top2_too_close)×2 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/113 | column6 | text | wrong:address(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/127 | a1 (retail) floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/128 | a1 (retail) floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/129 | a2 floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/130 | a2 floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/131 | a2 floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/132 | b1a floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/133 | b1a floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/134 | b1a floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/135 | d2 floorspace gains sqm | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/136 | d2 floorspace losses sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/137 | d2 floorspace net sqm | other | other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/140 | surveyname | text | unknown:unknown(probability_below_threshold)×3; wrong:org(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/149 | projection | category | wrong:id(none)×11; unknown:unknown(other_class)×2; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/151 | habitatdescription | text | unknown:unknown(probability_below_threshold)×2 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/154 | surveyname | text | unknown:unknown(probability_below_threshold)×5 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/159 | locationname | address | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/163 | projection | category | wrong:id(none)×11; unknown:unknown(other_class)×2; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/176 | contravention | category | wrong:text(none)×3; unknown:unknown(probability_below_threshold)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/177 | fine | amount | unknown:unknown(other_class)×3; unknown:unknown(probability_below_threshold)×8; wrong:id(none)×3; wrong:rate(none)×1 | 4 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/179 | location | address | wrong:org(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business2/180 | contravention | category | unknown:unknown(probability_below_threshold)×4 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/202 | net current expenditure - min all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/203 | net current expenditure - ave all english county councils | amount | unknown:unknown(numeric_top2_too_close)×3; wrong:quantity(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/204 | net current expenditure - max english county councils | amount | wrong:quantity(none)×3 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/230 | warddesc | address | wrong:category(none)×7; unknown:unknown(probability_below_threshold)×4 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business2/233 | super output area 2011 name | address | unknown:unknown(probability_below_threshold)×3; wrong:org(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/238 | terrace | quantity | unknown:unknown(probability_below_threshold)×6; unknown:unknown(other_class)×5; wrong:address(none)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/288 | construction_age_band | category | wrong:id(none)×3; unknown:unknown(probability_below_threshold)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/290 | epc_score | other | other_ng:rate(none)×4 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/291 | epc_score_known | category | unknown:unknown(probability_below_threshold)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/295 | potential_epc_score_known | category | unknown:unknown(probability_below_threshold)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/298 | number_habitable_rooms | quantity | unknown:unknown(numeric_values_not_parseable)×8; wrong:category(none)×6; unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/299 | number_habitable_rooms_known | category | wrong:quantity(none)×12; unknown:unknown(probability_below_threshold)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/301 | total_floor_area_known | category | wrong:quantity(none)×7; unknown:unknown(other_class)×4; unknown:unknown(probability_below_threshold)×4 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/317 | energy_consumption | other | other_ng:quantity(none)×12 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/318 | energy_consumption_known | category | unknown:unknown(probability_below_threshold)×1; wrong:quantity(none)×4 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/319 | solar_pv_area | other | other_ng:id(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/321 | avg_tilt | other | other_ng:quantity(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/322 | imd19_national_decile | category | unknown:unknown(probability_below_threshold)×6; wrong:quantity(none)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/323 | imd19_income_decile | category | wrong:quantity(none)×4 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/325 | loac_group | category | wrong:address(none)×9 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/326 | fuel_poverty | rate | unknown:unknown(other_class)×4; unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/330 | conservation_area_site_id | category | wrong:id(none)×6; unknown:unknown(probability_below_threshold)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/356 | want to live in this parish only | quantity | wrong:category(none)×1 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/364 | want to live in this parish & band a | quantity | wrong:category(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/365 | want to live in this parish & band b | quantity | unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/367 | want to live in this parish & band d | quantity | wrong:category(none)×1 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/370 | average bids per property | other | other_ng:rate(none)×9; other_ng:amount(none)×3 | 0 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/379 | terrace | quantity | unknown:unknown(probability_below_threshold)×6; unknown:unknown(other_class)×5; wrong:address(none)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/381 | total_verified_sales | quantity | unknown:unknown(numeric_top2_too_close)×7; wrong:amount(none)×5 | 5 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/440 | situtation | address | wrong:text(none)×9; unknown:unknown(probability_below_threshold)×2; wrong:category(none)×4 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business2/443 | tree type | category | unknown:unknown(probability_below_threshold)×3; unknown:unknown(other_class)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/492 | value () | amount | unknown:unknown(numeric_values_not_parseable)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/499 | county | address | wrong:org(none)×3 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business2/501 | value | amount | unknown:unknown(probability_below_threshold)×3; wrong:rate(none)×3; unknown:unknown(numeric_top2_too_close)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/531 | value | quantity | unknown:unknown(numeric_top2_too_close)×6; wrong:amount(none)×3 | 3 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/535 | scheme_description | category | wrong:text(none)×4; unknown:unknown(probability_below_threshold)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/542 | percentage (%) of the total amount paid | rate | unknown:unknown(numeric_values_not_parseable)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/548 | health service executive area | address | wrong:org(none)×10; unknown:unknown(probability_below_threshold)×2 | 0 | 見出しの多義性、出典固有語、近い教材、周辺文脈不足のいずれか | 中 | 値、題名、兄弟列、出典定義と近傍教材を確認 |
| business2/562 | name | org | wrong:address(none)×14 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/581 | type of expenditure | account | wrong:category(none)×7 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/625 | household income decile | category | wrong:address(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/633 | household disposable income quintiles | category | unknown:unknown(probability_below_threshold)×1 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/667 | value | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/825 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/838 | value | quantity | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/864 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/874 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/883 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/918 | value | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/926 | tlist(q1) | date | unknown:unknown(date_value_evidence_low)×15 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/945 | état | category | wrong:account(none)×1 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/946 | service_responsable | account | wrong:category(none)×15 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/948 | numéro_uev | id | wrong:address(none)×12; unknown:unknown(probability_below_threshold)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/955 | flow | category | unknown:unknown(other_class)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/956 | terminal | address | unknown:unknown(probability_below_threshold)×3; wrong:category(none)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/958 | volume (mcf) | quantity | unknown:unknown(other_class)×4 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/959 | numéro | id | wrong:address(none)×4 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/962 | service | account | wrong:address(none)×3; unknown:unknown(probability_below_threshold)×7; wrong:category(none)×3; wrong:org(none)×2 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |
| business2/963 | numéro entente-cadre | id | unknown:unknown(numeric_values_not_parseable)×2; unknown:unknown(probability_below_threshold)×2 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/970 | return-on-investments_revenus-de-placements | amount | unknown:unknown(numeric_top2_too_close)×3 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/971 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | unknown:unknown(numeric_top2_too_close)×7; wrong:quantity(none)×4 | 4 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| business2/972 | sales-goods-svcs_ventes-biens-srvs | amount | wrong:quantity(none)×3; unknown:unknown(numeric_top2_too_close)×1 | 3 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | wrong:quantity(none)×14; unknown:unknown(numeric_top2_too_close)×1 | 14 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/974 | miscellaneous_divers | amount | wrong:quantity(none)×15 | 15 | 数値意味・単位・題名・兄弟列の不足、またはラベル境界 | 中 | 値形式、UNIT、題名、兄弟列、token切り詰めを照合 |
| business2/975 | amt-units_mnt-unite | category | unknown:unknown(probability_below_threshold)×4 | 0 | 後段guardが出力をunknownへ変えた機構は確認済み。根本の証拠不足は未確定 | 高 | 値形式、UNIT、題名、兄弟列、出典定義、token切り詰めを照合 |
| japan_procurement/83 | 資産名称 | text | wrong:org(none)×3 | 0 | ラベル境界、近い教材の偏り、出典固有語、周辺文脈不足のいずれか | 中 | LABEL_GUIDE根拠と近傍教材を先生2人で独立確認 |

## 確認できた原因と未確定事項

- **観測事実**: cleaned silver 16,586列を追加しても固定5集合・新公開元8陣の双方で1.5ポイント以上の改善がなく、新公開元の重大は2→4へ増えた。C3bで重大化した数字列2件がC3sでも再発した。
- **高確度の機構原因**: `probability_below_threshold`、数値guard、date evidence等がraw出力をunknownに変える事例がある。一方、重大の中心はguardが退避しなかったraw誤分類である。
- **中確度仮説**: 銀を掃除しても、銀がC2とChatGPTの一致を起点に選ばれた選択バイアス、近い教材の誤った境界、UNIT・題名・兄弟列・値選択の不足が残る。個々の因果はこのartifactだけでは確定できない。
- **未確認**: 問題行ごとの元値、実際に使われたUNIT・題名・兄弟列、行別token切り詰め、近傍教材の寄与。学習データと固定集合の行単位重複も本artifactだけでは再確認できない。

## 次の一要因改善

1. まず学習入力と予測入力を一致させる（FT_TITLE、値の選び方、UNIT、兄弟列）。C3sの再実行はしない。
2. 評価行にraw/guard、入力に採用した題名・UNIT・兄弟列ID、token長・切り詰め、近傍教材IDを保存し、重大の直接原因を追跡できるようにする。
3. LABEL_GUIDEと近い教材の境界を先生2人が独立確認し、根拠裁定後だけ再ラベルする。
4. 次の学習は新しい未見陣を事前登録し、入力一致、合成教材、決め方の変更を一度に一要因だけ試す。
