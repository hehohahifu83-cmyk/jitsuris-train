# L24 固定5集合の全件監査 — run 41735353926

監査日: 2026-11-05 JST

## 範囲と結論

- 対象: `dev220`、`general`、`business`、`business2`、`japan_procurement`。`blind_set*`、セット3・5・7、sealed2/3、b018は読んでいない。
- L24: e5-base、2 epoch、seed 1/2/3、UNIT文脈、埋め込み未凍結、focal gamma 1.5、LR 3e-5、max length 160、4つのlabel-fix。
- 比較: 同じ固定5集合・同じseedのL（run 41192849082）。各条件の平均差は全て1.5ポイント未満で、固定試験上は**差なし**。F1の一回限り新規公開元試験を終えるまで採用判断はしない。
- 評価artifact `13283840097`（154ファイル）とモデルartifact `13283895077`（約2.64GB、2026-12-04期限）は別成果物として確認済み。

## 学習・再現性

| seed | 学習行 | loop時間 | 最大GPU | train切詰め |
|---:|---:|---:|---:|---:|
| 1 | 142,117 | 1614秒 | 5.5 GiB | 849 (0.60%) |
| 2 | 142,117 | 1647秒 | 5.5 GiB | 849 (0.60%) |
| 3 | 142,117 | 1615秒 | 5.6 GiB | 849 (0.60%) |

- manifestはモデルrevision `d128750597153bb5987e10b1c3493a34e5a4502a`、commit `95d9bb18dbbbc7a7c51201802f53de3062747c85`、16ラベル、3 seedの設定を記録している。
- 未確認: 事前記録の `relabeled 1492` とartifact内の実適用件数の一致。manifestには4ファイル名と学習行hashはあるが件数がない。F1予測前にログまたは再現集計で照合する。

## Lとの比較

Accuracyは `correct + other_ok` / 全行。表の値は5集合のaccuracyを同じ重みで平均し、さらに3 seedを平均したもの。

| 条件 | L24平均 | L平均 | 差 (pp) | 判定 |
|---|---:|---:|---:|---|
| ft | 96.7386% | 96.8000% | -0.0615 | 差なし |
| blend50 | 95.5072% | 95.6754% | -0.1682 | 差なし |
| blend60 | 96.7789% | 96.7667% | +0.0121 | 差なし |
| blend70 | 96.8007% | 96.8235% | -0.0228 | 差なし |
| sparse | 91.4163% | 91.5958% | -0.1794 | 差なし |

### L24のseed・集合・条件別

| seed | 集合 | 条件 | accuracy | 誤り | 重大 | unknown | other見落し |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | dev220 | ft | 97.273% | 5 | 1 | 1 | 0 |
| 1 | dev220 | blend50 | 93.636% | 5 | 1 | 9 | 0 |
| 1 | dev220 | blend60 | 97.727% | 4 | 1 | 1 | 0 |
| 1 | dev220 | blend70 | 97.273% | 4 | 1 | 2 | 0 |
| 1 | dev220 | sparse | 87.273% | 20 | 2 | 8 | 0 |
| 1 | general | ft | 92.689% | 10 | 0 | 11 | 7 |
| 1 | general | blend50 | 91.906% | 10 | 0 | 14 | 7 |
| 1 | general | blend60 | 92.689% | 8 | 0 | 14 | 6 |
| 1 | general | blend70 | 93.473% | 9 | 0 | 10 | 6 |
| 1 | general | sparse | 86.945% | 20 | 2 | 14 | 16 |
| 1 | business | ft | 97.755% | 6 | 0 | 5 | 0 |
| 1 | business | blend50 | 95.918% | 4 | 0 | 16 | 0 |
| 1 | business | blend60 | 96.939% | 5 | 0 | 10 | 0 |
| 1 | business | blend70 | 97.551% | 6 | 0 | 6 | 0 |
| 1 | business | sparse | 91.020% | 29 | 12 | 14 | 1 |
| 1 | business2 | ft | 96.926% | 16 | 3 | 14 | 0 |
| 1 | business2 | blend50 | 95.799% | 12 | 2 | 27 | 2 |
| 1 | business2 | blend60 | 96.516% | 10 | 1 | 24 | 0 |
| 1 | business2 | blend70 | 96.824% | 15 | 3 | 16 | 0 |
| 1 | business2 | sparse | 92.930% | 30 | 11 | 27 | 12 |
| 1 | japan_procurement | ft | 100.000% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend50 | 100.000% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend60 | 100.000% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend70 | 100.000% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | sparse | 98.913% | 1 | 0 | 0 | 0 |
| 2 | dev220 | ft | 97.273% | 5 | 1 | 1 | 0 |
| 2 | dev220 | blend50 | 93.636% | 4 | 1 | 10 | 0 |
| 2 | dev220 | blend60 | 97.727% | 4 | 1 | 1 | 0 |
| 2 | dev220 | blend70 | 97.727% | 4 | 1 | 1 | 0 |
| 2 | dev220 | sparse | 87.273% | 20 | 2 | 8 | 0 |
| 2 | general | ft | 93.211% | 9 | 1 | 10 | 7 |
| 2 | general | blend50 | 92.428% | 8 | 0 | 15 | 6 |
| 2 | general | blend60 | 93.211% | 9 | 0 | 11 | 6 |
| 2 | general | blend70 | 92.950% | 10 | 1 | 10 | 7 |
| 2 | general | sparse | 86.945% | 20 | 2 | 14 | 16 |
| 2 | business | ft | 97.959% | 5 | 0 | 5 | 0 |
| 2 | business | blend50 | 95.510% | 4 | 0 | 18 | 0 |
| 2 | business | blend60 | 97.143% | 4 | 0 | 10 | 0 |
| 2 | business | blend70 | 97.755% | 4 | 0 | 7 | 0 |
| 2 | business | sparse | 91.020% | 29 | 12 | 14 | 1 |
| 2 | business2 | ft | 96.926% | 12 | 3 | 17 | 1 |
| 2 | business2 | blend50 | 95.389% | 14 | 2 | 29 | 2 |
| 2 | business2 | blend60 | 96.414% | 11 | 2 | 23 | 1 |
| 2 | business2 | blend70 | 96.619% | 13 | 3 | 19 | 1 |
| 2 | business2 | sparse | 92.930% | 30 | 11 | 27 | 12 |
| 2 | japan_procurement | ft | 100.000% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend50 | 100.000% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend60 | 100.000% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend70 | 100.000% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | sparse | 98.913% | 1 | 0 | 0 | 0 |
| 3 | dev220 | ft | 96.364% | 8 | 1 | 0 | 0 |
| 3 | dev220 | blend50 | 94.545% | 5 | 1 | 7 | 0 |
| 3 | dev220 | blend60 | 97.727% | 5 | 1 | 0 | 0 |
| 3 | dev220 | blend70 | 96.818% | 6 | 1 | 1 | 0 |
| 3 | dev220 | sparse | 87.273% | 20 | 2 | 8 | 0 |
| 3 | general | ft | 92.167% | 13 | 1 | 10 | 7 |
| 3 | general | blend50 | 92.428% | 10 | 0 | 15 | 4 |
| 3 | general | blend60 | 92.950% | 9 | 0 | 16 | 2 |
| 3 | general | blend70 | 92.689% | 11 | 1 | 14 | 3 |
| 3 | general | sparse | 86.945% | 20 | 2 | 14 | 16 |
| 3 | business | ft | 96.531% | 11 | 3 | 5 | 1 |
| 3 | business | blend50 | 95.714% | 5 | 1 | 16 | 0 |
| 3 | business | blend60 | 96.327% | 6 | 2 | 11 | 1 |
| 3 | business | blend70 | 96.122% | 11 | 4 | 7 | 1 |
| 3 | business | sparse | 91.020% | 29 | 12 | 14 | 1 |
| 3 | business2 | ft | 96.004% | 14 | 2 | 20 | 5 |
| 3 | business2 | blend50 | 95.697% | 12 | 2 | 26 | 4 |
| 3 | business2 | blend60 | 96.311% | 13 | 2 | 19 | 4 |
| 3 | business2 | blend70 | 96.209% | 13 | 3 | 18 | 6 |
| 3 | business2 | sparse | 92.930% | 30 | 11 | 27 | 12 |
| 3 | japan_procurement | ft | 100.000% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend50 | 100.000% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend60 | 100.000% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend70 | 100.000% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | sparse | 98.913% | 1 | 0 | 0 | 0 |

## 問題出力の全体像

- 問題出力 1,626: wrong 701、unknown 741、other見落し 184。重大 135。
- 即時機構: raw誤分類をそのまま出力 701、raw正解をguardがunknown化 397、raw誤分類をguardがunknown化 344、otherの誤受理 184。
- 固有行 231: 全3 seed再発 207、2 seed再発 11、1 seedのみ 13。
- 75個のprobs JSONと対応する75個のerrors JSONを照合し、wrong/unknown/other_ngの行集合が一致することを確認した。

## 原因分析

### 観測事実

- 同じ列が複数seed・複数条件で再発する例が多く、seed固有ノイズだけでは説明できない。
- 741 unknownのうち397はraw top-1が正解だったがguardがunknownへ変え、344はraw top-1も誤りだった。guardとモデルの寄与を分けて扱う必要がある。
- 重大135出力は固定集合中の同じ少数行が条件・seedをまたいで繰り返した分を含む。
- artifactの行には列名・正解・raw/guard後予測・上位確率はあるが、元値、兄弟列、UNIT、出典、分割根拠は含まれない。

### 原因仮説と確度

| 仮説 | 根拠 | 確度 | 追加確認 |
|---|---|---|---|
| 文脈不足または文脈の学習不足 | 短い/汎用の列名で org/address、account/category、amount/quantity 等がseedをまたぎ再発 | 中 | 元値・UNIT・兄弟列・タイトルを許可された固定例だけで再構成し、特徴別反実仮想を取る |
| guard閾値/規則が過剰に見送る | raw正解→unknownが397出力 | 高（即時機構） | raw正解例だけで理由コード・margin・しきい値を層別化。学習変更とguard変更を同時に行わない |
| 教材の量・分布・定義境界が不足 | 再発するラベル対と多言語/業務語が集中 | 中 | 教材庫の見出し×値形×言語×公開元を集計し、対象ケースとの近傍被覆を見る |
| ラベル定義または評価ラベル疑義 | 列名単独では複数解釈が可能な行がある | 低〜中 | 先生2人が独立に元表文脈を確認し、根拠裁定までラベルを変えない |
| 前処理/切詰め | 固定集合にも最大長超過があり、train 849行を切詰め | 低 | 問題行ごとのtoken長、切詰め、正規化差を保存して再評価 |
| 実装/評価コード | probs/errorsは一致し、manifest hashもあるため明白な集計破損は未観測 | 低 | F1前にlabel-fix実適用件数1492を独立再集計 |

### 改善の優先順位

1. **P0** F1前に `relabeled 1492` を独立照合。違えば予測せず原因修正。
2. **P0** 事前登録済みF1でL対L24を一回だけ評価。固定集合は改善選択に再利用しない。
3. **P1** raw正解→unknown 397出力を理由コード/確率margin別に診断し、guardだけを一要因で検証。期待効果はunknown減、副作用は重大誤り増加。
4. **P1** 再発行を教材被覆（見出し、値形、言語、出典、UNIT、兄弟列）へ接続し、不足セルだけを先生2人で追加。期待効果は再発誤分類減、副作用は局所過学習・漏洩。固定試験例自体を教材へ転用しない。
5. **P2** token切詰めと前処理を一要因で測る。max length変更は速度/メモリとの交換条件も記録する。

## 固有231行の全件監査

同じ評価行の複数seed・条件を1行に集約した。即時機構はartifactで確認できる事実。根本原因は上の仮説であり、この表だけから断定しない。

| 集合:index | 列名 | 正解 | 条件 | seed | outcome/予測 | raw top1 | 確率範囲 | 重大 | 即時機構 | 根本原因確度 |
|---|---|---|---|---|---|---|---:|---:|---|---|
| business:41 | total invoices paid | quantity | blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×7; wrong→amount×3 | amount×6; quantity×4 | 0.503–0.998 | 3 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:42 | # invoices paid within 5 days | quantity | sparse | 1,2,3 | wrong→amount×3 | amount×3 | 0.635–0.635 | 3 | raw誤分類を出力 | 中 |
| business:43 | # invoices paid within 30 days | quantity | sparse | 1,2,3 | wrong→amount×3 | amount×3 | 0.648–0.648 | 3 | raw誤分類を出力 | 中 |
| business:46 | quarterno | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.976–0.988 | 0 | raw正解→guard unknown | 中 |
| business:55 | all p-cards payments for february 2022 | org | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.566–0.566 | 0 | raw誤分類を出力 | 中 |
| business:77 | publisher label | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×9; wrong→address×1; wrong→category×3 | address×2; category×7; org×4 | 0.385–0.886 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:81 | la budget allocated to residential care | amount | sparse | 1,2,3 | unknown→unknown×3 | id×3 | 0.445–0.445 | 0 | raw誤り→guard unknown | 中 |
| business:82 | la budget allocated to nursing care | amount | sparse | 1,2,3 | unknown→unknown×3 | id×3 | 0.393–0.393 | 0 | raw誤り→guard unknown | 中 |
| business:84 | department | org | sparse | 1,2,3 | wrong→account×3 | account×3 | 0.536–0.536 | 0 | raw誤分類を出力 | 中 |
| business:92 | department | org | sparse | 1,2,3 | wrong→account×3 | account×3 | 0.519–0.519 | 0 | raw誤分類を出力 | 中 |
| business:101 | entitiy | org | ft,blend60,blend70 | 3 | unknown→unknown×1; wrong→category×2 | category×3 | 0.468–0.771 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 低 |
| business:148 | merchant details | text | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×15 | category×15 | 0.581–0.894 | 0 | raw誤分類を出力 | 中 |
| business:225 | description | account | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×1; wrong→text×10 | text×11 | 0.497–0.894 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business:237 | purposeofexpenditure | text | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→account×15 | account×15 | 0.712–0.956 | 0 | raw誤分類を出力 | 中 |
| business:269 | net current expenditure - min all english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×3 | amount×3; quantity×3 | 0.535–0.878 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:270 | net current expenditure - ave all english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×3 | amount×3; quantity×3 | 0.534–0.859 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:271 | net current expenditure - max english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→quantity×3 | amount×1; quantity×3 | 0.596–0.690 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:275 | provider_name | org | sparse | 1,2,3 | unknown→unknown×3 | text×3 | 0.484–0.484 | 0 | raw誤り→guard unknown | 中 |
| business:278 | 目名 | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | other×15 | 0.804–0.963 | 0 | raw誤り→guard unknown | 中 |
| business:279 | 科名 | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | other×15 | 0.828–0.952 | 0 | raw誤り→guard unknown | 中 |
| business:304 | d2 | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.623–0.623 | 0 | raw誤分類を出力 | 中 |
| business:307 | d5 | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.627–0.627 | 0 | raw誤分類を出力 | 中 |
| business:308 | d6 | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.501–0.501 | 0 | raw誤分類を出力 | 中 |
| business:309 | d7 | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.722–0.722 | 0 | raw誤分類を出力 | 中 |
| business:318 | number-of-disputes_nombre-de-différends | quantity | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.650–0.650 | 0 | raw誤分類を出力 | 中 |
| business:324 | nom_fournisseur | org | sparse | 1,2,3 | unknown→unknown×3 | org×3 | 0.469–0.469 | 0 | raw正解→guard unknown | 中 |
| business:333 | segment-title_en | category | sparse | 1,2,3 | wrong→text×3 | text×3 | 0.583–0.583 | 0 | raw誤分類を出力 | 中 |
| business:335 | family | id | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.429–0.429 | 0 | raw誤り→guard unknown | 中 |
| business:337 | family-title_fr | category | sparse | 1,2,3 | wrong→text×3 | text×3 | 0.692–0.692 | 0 | raw誤分類を出力 | 中 |
| business:342 | commodity-title_en | product | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×6; wrong→text×3 | category×2; product×2; text×5 | 0.350–0.766 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:343 | commodity-title_fr | product | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→text×3 | product×1; text×3 | 0.468–0.627 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:344 | portefeuille_nom_et_code | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×13; wrong→id×1 | account×5; category×3; id×4; org×2 | 0.306–0.612 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:345 | organisme_nom_et_code | org | sparse | 1,2,3 | unknown→unknown×3 | address×3 | 0.330–0.330 | 0 | raw誤り→guard unknown | 中 |
| business:347 | regrp_sommaire | account | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→category×8 | account×2; category×8; quantity×3 | 0.413–0.837 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:348 | regrp_nom | account | sparse | 1,2,3 | wrong→text×3 | text×3 | 0.548–0.548 | 0 | raw誤分類を出力 | 中 |
| business:401 | ligne | category | ft,blend60,blend70 | 1,3 | wrong→id×5 | id×5 | 0.530–0.911 | 0 | raw誤分類を出力 | 中 |
| business:406 | mois calendrier | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×12; wrong→id×3 | date×12; id×3 | 0.614–0.988 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:408 | km budgété | other | ft,blend60,blend70,sparse | 1,2,3 | other_ng→category×3; other_ng→quantity×3 | category×3; quantity×3 | 0.505–0.840 | 0 | other誤受理 | 中 |
| business:421 | abn | id | blend50,blend60,sparse | 1,2,3 | unknown→unknown×4; wrong→amount×3 | amount×3; id×4 | 0.508–0.888 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:445 | regions | address | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.814–0.814 | 0 | raw誤分類を出力 | 中 |
| business:451 | title | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→account×2; wrong→text×8 | account×4; text×11 | 0.416–0.837 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business:457 | defence goods value | amount | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.504–0.504 | 0 | raw正解→guard unknown | 中 |
| business:458 | defence services value | amount | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→id×3 | amount×3; id×3 | 0.563–0.852 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business:459 | australian sourced goods | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→quantity×3 | amount×1; id×3; quantity×4 | 0.455–0.904 | 3 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:460 | australian sourced services | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×4; wrong→id×3; wrong→quantity×2 | amount×2; id×4; quantity×3 | 0.385–0.767 | 5 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:461 | overseas sourced goods | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×6; wrong→id×3; wrong→quantity×2 | amount×3; id×5; quantity×3 | 0.452–0.903 | 5 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business:462 | overseas sourced services | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×6 | amount×2; quantity×7 | 0.544–0.689 | 6 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:11 | merchant description | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→org×7 | org×8 | 0.489–0.842 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:13 | cost centre description | account | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→org×2 | account×3; org×4 | 0.409–0.764 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:45 | type | account | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×15 | category×15 | 0.803–0.985 | 0 | raw誤分類を出力 | 中 |
| business2:58 | numbers of | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×11 | date×3; quantity×8 | 0.442–0.844 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:73 | provider_name | org | sparse | 1,2,3 | wrong→address×3 | address×3 | 0.777–0.777 | 0 | raw誤分類を出力 | 中 |
| business2:75 | monitor | id | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×6; wrong→category×9 | category×12; id×3 | 0.406–0.953 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:90 | total invoices paid | quantity | blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×7; wrong→amount×3 | amount×6; quantity×4 | 0.503–0.998 | 3 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:91 | # invoices paid within 5 days | quantity | sparse | 1,2,3 | wrong→amount×3 | amount×3 | 0.635–0.635 | 3 | raw誤分類を出力 | 中 |
| business2:92 | # invoices paid within 30 days | quantity | sparse | 1,2,3 | wrong→amount×3 | amount×3 | 0.648–0.648 | 3 | raw誤分類を出力 | 中 |
| business2:109 | column2 | address | sparse | 1,2,3 | wrong→text×3 | text×3 | 0.595–0.595 | 0 | raw誤分類を出力 | 中 |
| business2:126 | a1 (retail) floorspace gains sqm | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→quantity×7 | quantity×7 | 0.587–0.656 | 0 | other誤受理 | 中 |
| business2:127 | a1 (retail) floorspace losses sqm | other | ft,blend70,sparse | 1,2,3 | other_ng→amount×3; other_ng→quantity×2 | amount×3; quantity×2 | 0.585–0.802 | 0 | other誤受理 | 中 |
| business2:128 | a1 (retail) floorspace net sqm | other | sparse | 1,2,3 | other_ng→amount×3 | amount×3 | 0.833–0.833 | 0 | other誤受理 | 中 |
| business2:129 | a2 floorspace gains sqm | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→quantity×9 | quantity×9 | 0.503–0.941 | 0 | other誤受理 | 中 |
| business2:130 | a2 floorspace losses sqm | other | ft,blend70 | 3 | other_ng→quantity×2 | quantity×2 | 0.553–0.764 | 0 | other誤受理 | 低 |
| business2:132 | b1a floorspace gains sqm | other | blend50,blend60,blend70,sparse | 1,2,3 | other_ng→quantity×6 | quantity×6 | 0.527–0.781 | 0 | other誤受理 | 中 |
| business2:134 | b1a floorspace net sqm | other | sparse | 1,2,3 | other_ng→amount×3 | amount×3 | 0.851–0.851 | 0 | other誤受理 | 中 |
| business2:135 | d2 floorspace gains sqm | other | blend50,blend60 | 3 | other_ng→quantity×2 | quantity×2 | 0.502–0.513 | 0 | other誤受理 | 低 |
| business2:136 | d2 floorspace losses sqm | other | sparse | 1,2,3 | other_ng→amount×3 | amount×3 | 0.767–0.767 | 0 | other誤受理 | 中 |
| business2:137 | d2 floorspace net sqm | other | sparse | 1,2,3 | other_ng→amount×3 | amount×3 | 0.977–0.977 | 0 | other誤受理 | 中 |
| business2:140 | surveyname | text | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→org×3 | org×3; text×3 | 0.491–0.783 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:149 | projection | category | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→id×3 | category×1; id×3 | 0.496–0.744 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:151 | habitatdescription | text | ft,blend70 | 1,2,3 | unknown→unknown×4 | category×1; other×1; text×2 | 0.455–0.534 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:154 | surveyname | text | blend50,sparse | 1,2,3 | unknown→unknown×4 | address×3; text×1 | 0.414–0.461 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:163 | projection | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.570–0.570 | 0 | raw誤分類を出力 | 中 |
| business2:176 | contravention | category | ft,blend70 | 3 | unknown→unknown×1; wrong→text×1 | category×1; text×1 | 0.485–0.550 | 0 | raw誤分類を出力 / raw正解→guard unknown | 低 |
| business2:177 | fine | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×11; wrong→rate×4 | date×4; other×3; rate×8 | 0.253–0.760 | 4 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:182 | fine | amount | sparse | 1,2,3 | unknown→unknown×3 | date×3 | 0.522–0.522 | 0 | raw誤り→guard unknown | 中 |
| business2:202 | net current expenditure - min all english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×3 | amount×3; quantity×3 | 0.534–0.879 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:203 | net current expenditure - ave all english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×3 | amount×3; quantity×3 | 0.535–0.856 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:204 | net current expenditure - max english county councils | amount | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→quantity×3 | amount×1; quantity×3 | 0.596–0.690 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:229 | post code sector | address | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×7 | address×4; category×3 | 0.441–0.473 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:230 | warddesc | address | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×15 | category×15 | 0.740–0.860 | 0 | raw誤分類を出力 | 中 |
| business2:233 | super output area 2011 name | address | sparse | 1,2,3 | unknown→unknown×3 | org×3 | 0.455–0.455 | 0 | raw誤り→guard unknown | 中 |
| business2:237 | semi-detached | quantity | sparse | 1,2,3 | unknown→unknown×3 | quantity×3 | 0.567–0.567 | 0 | raw正解→guard unknown | 中 |
| business2:238 | terrace | quantity | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×12 | other×9; quantity×3 | 0.346–0.911 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:288 | construction_age_band | category | sparse | 1,2,3 | wrong→id×3 | id×3 | 0.553–0.553 | 0 | raw誤分類を出力 | 中 |
| business2:291 | epc_score_known | category | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×11; wrong→quantity×1 | category×5; quantity×7 | 0.337–0.602 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:295 | potential_epc_score_known | category | ft,blend60,blend70 | 1,3 | unknown→unknown×3; wrong→quantity×1 | category×2; other×1; quantity×1 | 0.417–0.512 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:297 | potential_epc_rating_known | category | ft,blend50,blend60,blend70 | 1,3 | unknown→unknown×7 | category×4; other×3 | 0.391–0.606 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:298 | number_habitable_rooms | quantity | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→category×10 | category×11; quantity×4 | 0.492–0.963 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:299 | number_habitable_rooms_known | category | ft,blend50,blend60,blend70 | 1,2,3 | wrong→quantity×12 | quantity×12 | 0.538–0.956 | 0 | raw誤分類を出力 | 中 |
| business2:301 | total_floor_area_known | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×12; wrong→quantity×3 | category×1; other×8; quantity×6 | 0.348–0.835 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:306 | wall_insulation_known | category | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.497–0.497 | 0 | raw正解→guard unknown | 中 |
| business2:319 | solar_pv_area | other | sparse | 1,2,3 | other_ng→address×3 | address×3 | 0.519–0.519 | 0 | other誤受理 | 中 |
| business2:321 | avg_tilt | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.567–0.567 | 0 | other誤受理 | 中 |
| business2:322 | imd19_national_decile | category | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.296–0.296 | 0 | raw正解→guard unknown | 中 |
| business2:325 | loac_group | category | ft | 3 | wrong→address×1 | address×1 | 0.552–0.552 | 0 | raw誤分類を出力 | 低 |
| business2:326 | fuel_poverty | rate | ft,blend60,blend70 | 2,3 | unknown→unknown×4 | other×2; rate×2 | 0.343–0.642 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:370 | average bids per property | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→amount×2; other_ng→rate×8 | amount×2; rate×8 | 0.531–0.842 | 0 | other誤受理 | 中 |
| business2:379 | terrace | quantity | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×9 | other×8; quantity×1 | 0.404–0.932 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:381 | total_verified_sales | quantity | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×6; wrong→amount×4 | amount×7; quantity×3 | 0.514–0.955 | 4 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:414 | descript | address | ft | 1 | wrong→text×1 | text×1 | 0.521–0.521 | 0 | raw誤分類を出力 | 低 |
| business2:440 | situtation | address | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×2; wrong→category×11; wrong→text×2 | category×12; text×3 | 0.410–0.940 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:443 | tree type | category | ft,blend50,blend60,blend70 | 1,2 | unknown→unknown×8 | category×3; other×5 | 0.401–0.789 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:492 | value () | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | amount×15 | 0.988–0.994 | 0 | raw正解→guard unknown | 中 |
| business2:501 | value | amount | blend50,blend60,sparse | 1,2,3 | unknown→unknown×6; wrong→rate×3 | amount×5; rate×4 | 0.495–0.975 | 3 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:531 | value | quantity | blend50,blend60,sparse | 1,2,3 | unknown→unknown×5; wrong→amount×3 | amount×3; quantity×5 | 0.520–0.908 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:535 | scheme_description | category | blend50,sparse | 1,2,3 | wrong→text×6 | text×6 | 0.502–0.992 | 0 | raw誤分類を出力 | 中 |
| business2:542 | percentage (%) of the total amount paid | rate | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | rate×15 | 0.934–0.997 | 0 | raw正解→guard unknown | 中 |
| business2:548 | health service executive area | address | ft,blend50,blend60,blend70 | 1,3 | wrong→org×8 | org×8 | 0.573–0.822 | 0 | raw誤分類を出力 | 中 |
| business2:562 | name | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→address×13 | address×14 | 0.497–0.979 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:581 | type of expenditure | account | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.651–0.651 | 0 | raw誤分類を出力 | 中 |
| business2:667 | value | amount | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.501–0.501 | 0 | raw正解→guard unknown | 中 |
| business2:812 | value of payments € 000s 2008 | amount | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.443–0.443 | 0 | raw正解→guard unknown | 中 |
| business2:825 | tlist(q1) | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.987–0.996 | 0 | raw正解→guard unknown | 中 |
| business2:838 | value | quantity | sparse | 1,2,3 | unknown→unknown×3 | quantity×3 | 0.525–0.525 | 0 | raw正解→guard unknown | 中 |
| business2:864 | tlist(q1) | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.981–0.999 | 0 | raw正解→guard unknown | 中 |
| business2:874 | tlist(q1) | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.980–0.998 | 0 | raw正解→guard unknown | 中 |
| business2:883 | tlist(q1) | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.978–0.998 | 0 | raw正解→guard unknown | 中 |
| business2:918 | value | amount | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.548–0.548 | 0 | raw正解→guard unknown | 中 |
| business2:926 | tlist(q1) | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.988–0.993 | 0 | raw正解→guard unknown | 中 |
| business2:946 | service_responsable | account | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×14 | category×14 | 0.524–0.957 | 0 | raw誤分類を出力 | 中 |
| business2:948 | numéro_uev | id | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→address×14 | address×15 | 0.491–0.920 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:951 | loc_y | other | sparse | 1,2,3 | other_ng→amount×3 | amount×3 | 0.601–0.601 | 0 | other誤受理 | 中 |
| business2:955 | flow | category | sparse | 1,2,3 | unknown→unknown×3 | other×3 | 0.798–0.798 | 0 | raw誤り→guard unknown | 中 |
| business2:956 | terminal | address | blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×7; wrong→category×3 | address×3; category×7 | 0.378–0.969 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:959 | numéro | id | blend50,sparse | 1,2,3 | wrong→address×4 | address×4 | 0.501–0.717 | 0 | raw誤分類を出力 | 中 |
| business2:962 | service | account | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×5; wrong→category×3; wrong→org×7 | category×5; org×10 | 0.428–0.928 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| business2:970 | return-on-investments_revenus-de-placements | amount | blend50,sparse | 1,2,3 | unknown→unknown×4 | amount×1; quantity×3 | 0.527–0.609 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:971 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | blend50,blend60,sparse | 1,2,3 | unknown→unknown×5; wrong→quantity×3 | amount×5; quantity×3 | 0.507–0.789 | 3 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| business2:972 | sales-goods-svcs_ventes-biens-srvs | amount | blend50,sparse | 1,2,3 | unknown→unknown×4 | amount×1; quantity×3 | 0.508–0.608 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:973 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×3; wrong→quantity×11 | amount×1; quantity×13 | 0.492–0.934 | 11 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| business2:974 | miscellaneous_divers | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→quantity×15 | quantity×15 | 0.948–0.982 | 15 | raw誤分類を出力 | 中 |
| business2:975 | amt-units_mnt-unite | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×10 | category×3; id×4; quantity×3 | 0.243–0.475 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| dev220:5 | 受注名 | person | blend50,sparse | 1,2,3 | unknown→unknown×6 | category×3; person×3 | 0.438–0.497 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| dev220:6 | 受注名カナ | person | sparse | 1,2,3 | unknown→unknown×3 | address×3 | 0.475–0.475 | 0 | raw誤り→guard unknown | 中 |
| dev220:12 | 発送先名 | person | sparse | 1,2,3 | wrong→address×3 | address×3 | 0.796–0.796 | 0 | raw誤分類を出力 | 中 |
| dev220:13 | 発送先カナ | person | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→category×3 | category×3; person×3 | 0.472–0.763 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| dev220:22 | その他費用 | amount | sparse | 1,2,3 | wrong→quantity×3 | quantity×3 | 0.635–0.635 | 3 | raw誤分類を出力 | 中 |
| dev220:27 | 作業者欄 | person | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→address×3 | address×3; person×3 | 0.486–0.879 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| dev220:28 | 備考 | text | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.814–0.814 | 0 | raw誤分類を出力 | 中 |
| dev220:33 | 商品オプション | text | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.919–0.919 | 0 | raw誤分類を出力 | 中 |
| dev220:40 | メッセージ | text | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→category×3 | category×6 | 0.499–0.996 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| dev220:45 | 商品オプション | text | sparse | 1,2,3 | unknown→unknown×3 | text×3 | 0.491–0.491 | 0 | raw正解→guard unknown | 中 |
| dev220:49 | 税率 | rate | ft,blend70 | 1 | unknown→unknown×1; wrong→tax_class×1 | tax_class×2 | 0.490–0.694 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 低 |
| dev220:65 | receive_order_customer_name | person | sparse | 1,2,3 | unknown→unknown×3 | person×3 | 0.333–0.333 | 0 | raw正解→guard unknown | 中 |
| dev220:116 | 履行場所 | address | ft | 3 | wrong→id×1 | id×1 | 0.591–0.591 | 0 | raw誤分類を出力 | 低 |
| dev220:128 | 担当課 | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→account×15 | account×15 | 0.647–0.888 | 0 | raw誤分類を出力 | 中 |
| dev220:130 | 随意契約理由 | text | ft,blend60,blend70 | 2,3 | wrong→category×4 | category×4 | 0.539–0.881 | 0 | raw誤分類を出力 | 中 |
| dev220:131 | 支出負担行為担当官 | person | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→text×3 | person×3; text×3 | 0.468–0.546 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| dev220:140 | customer | org | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.416–0.416 | 0 | raw誤り→guard unknown | 中 |
| dev220:143 | terms | category | blend50,sparse | 1,2,3 | wrong→text×4 | text×4 | 0.503–0.692 | 0 | raw誤分類を出力 | 中 |
| dev220:145 | product/service | product | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.364–0.364 | 0 | raw誤り→guard unknown | 中 |
| dev220:151 | taxable | category | blend50,sparse | 1,2,3 | unknown→unknown×2; wrong→tax_class×4 | tax_class×6 | 0.482–0.942 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| dev220:156 | name | person | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→address×3 | address×3; person×3 | 0.491–0.922 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| dev220:157 | is a company | category | blend50,sparse | 1,2,3 | unknown→unknown×2; wrong→org×3 | category×1; org×4 | 0.496–0.981 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| dev220:168 | website | text | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.508–0.508 | 0 | raw誤分類を出力 | 中 |
| dev220:171 | customer rank | quantity | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×15 | category×15 | 0.950–0.989 | 0 | raw誤分類を出力 | 中 |
| dev220:172 | supplier rank | quantity | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→category×15 | category×15 | 0.899–0.991 | 0 | raw誤分類を出力 | 中 |
| dev220:174 | sales order | id | ft,blend50,blend60,blend70 | 2 | unknown→unknown×4 | date×3; id×1 | 0.456–0.758 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 低 |
| dev220:177 | purchase order by customer | id | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→quantity×15 | quantity×15 | 0.714–0.990 | 15 | raw誤分類を出力 | 中 |
| dev220:183 | material | product | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.489–0.489 | 0 | raw誤り→guard unknown | 中 |
| dev220:189 | payment terms | category | ft,blend70 | 3 | unknown→unknown×1; wrong→text×1 | category×1; text×1 | 0.488–0.584 | 0 | raw誤分類を出力 / raw正解→guard unknown | 低 |
| dev220:195 | sales tax group | tax_class | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→category×3 | category×3; tax_class×1 | 0.499–0.931 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| dev220:196 | credit limit | amount | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×7 | amount×7 | 0.468–0.490 | 0 | raw正解→guard unknown | 中 |
| dev220:197 | primary contact | person | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.807–0.807 | 0 | raw誤分類を出力 | 中 |
| dev220:201 | city | address | ft,blend70 | 3 | wrong→id×2 | id×2 | 0.540–0.761 | 0 | raw誤分類を出力 | 低 |
| dev220:211 | item description | text | blend50,sparse | 1,2,3 | unknown→unknown×1; wrong→category×3 | category×3; text×1 | 0.476–0.680 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| general:1 | author | person | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→org×12 | org×12; person×1 | 0.479–0.974 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| general:27 | keyword | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→text×15 | text×15 | 0.899–0.968 | 0 | raw誤分類を出力 | 中 |
| general:28 | fulltext rank | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.731–0.731 | 0 | other誤受理 | 中 |
| general:32 | 五島 | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→quantity×15 | quantity×15 | 0.839–1.000 | 0 | other誤受理 | 中 |
| general:35 | denominatorunweighted | quantity | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×10; wrong→id×2 | id×4; other×6; quantity×2 | 0.363–0.913 | 2 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:39 | orcinus_orca | category | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.417–0.417 | 0 | raw正解→guard unknown | 中 |
| general:47 | mood | other | ft,blend60,blend70 | 1,2,3 | other_ng→category×5 | category×5 | 0.593–0.979 | 0 | other誤受理 | 中 |
| general:48 | source | category | ft,blend60,blend70 | 2,3 | wrong→org×6 | org×6 | 0.505–0.937 | 0 | raw誤分類を出力 | 中 |
| general:53 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→quantity×8 | quantity×8 | 0.510–0.899 | 0 | raw誤分類を出力 | 中 |
| general:59 | 移動方向1 | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.755–0.755 | 0 | other誤受理 | 中 |
| general:62 | nodes | other | sparse | 1,2,3 | other_ng→text×3 | text×3 | 0.529–0.529 | 0 | other誤受理 | 中 |
| general:70 | lda | text | sparse | 1,2,3 | unknown→unknown×3 | text×3 | 0.448–0.448 | 0 | raw正解→guard unknown | 中 |
| general:71 | property | category | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×12 | category×2; other×10 | 0.390–0.934 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:75 | データセット_キーワード | text | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.699–0.699 | 0 | raw誤分類を出力 | 中 |
| general:83 | place | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→address×15 | address×15 | 0.602–0.934 | 0 | raw誤分類を出力 | 中 |
| general:87 | sens_final | rate | ft,blend60,blend70 | 1,2,3 | unknown→unknown×6 | other×6 | 0.551–0.951 | 0 | raw誤り→guard unknown | 中 |
| general:94 | 名称_カナ | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | wrong→address×15 | address×15 | 0.658–0.820 | 0 | raw誤分類を出力 | 中 |
| general:105 | authors | person | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→org×3 | org×3; person×3 | 0.468–0.762 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| general:112 | 住家全壊 | quantity | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×8; wrong→amount×3 | amount×6; other×1; quantity×4 | 0.358–0.846 | 3 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:121 | dag-stage | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→category×8; other_ng→quantity×3 | category×8; quantity×3 | 0.629–0.922 | 0 | other誤受理 | 中 |
| general:134 | dbpedia_score | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→rate×7 | rate×7 | 0.508–0.547 | 0 | other誤受理 | 中 |
| general:142 | 総観場3 | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.680–0.680 | 0 | other誤受理 | 中 |
| general:148 | mechanism | category | ft,blend60,blend70 | 3 | unknown→unknown×3 | category×2; date×1 | 0.448–0.476 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 低 |
| general:156 | 発生経度確度(±秒) | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.620–0.620 | 0 | other誤受理 | 中 |
| general:175 | bib | id | blend50,sparse | 1,2,3 | unknown→unknown×4 | id×1; other×3 | 0.496–0.865 | 0 | raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:179 | genre | category | sparse | 1,2,3 | wrong→account×3 | account×3 | 0.578–0.578 | 0 | raw誤分類を出力 | 中 |
| general:188 | 被害域幅(m)最小 | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.969–0.969 | 0 | other誤受理 | 中 |
| general:207 | year_step_size | quantity | ft,blend50,blend60,blend70 | 1,2,3 | wrong→category×12 | category×12 | 0.566–0.817 | 0 | raw誤分類を出力 | 中 |
| general:213 | age_q3_nd | quantity | sparse | 1,2,3 | wrong→rate×3 | rate×3 | 0.509–0.509 | 3 | raw誤分類を出力 | 中 |
| general:224 | study | text | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×6; wrong→id×3; wrong→person×2 | id×4; person×4; text×3 | 0.317–0.796 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:227 | 発生日 | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.967–0.989 | 0 | raw正解→guard unknown | 中 |
| general:234 | 発生県 | id | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×9; wrong→address×3; wrong→category×3 | address×5; category×8; id×2 | 0.356–0.885 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:238 | 被害域長さ(100m)最小 | other | blend50,sparse | 1,2,3 | other_ng→quantity×5 | quantity×5 | 0.502–0.974 | 0 | other誤受理 | 中 |
| general:239 | 回転方向 | other | sparse | 1,2,3 | other_ng→quantity×3 | quantity×3 | 0.770–0.770 | 0 | other誤受理 | 中 |
| general:244 | 天候 | category | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.447–0.447 | 0 | raw正解→guard unknown | 中 |
| general:245 | 住家一部損壊 | quantity | sparse | 1,2,3 | wrong→category×3 | category×3 | 0.525–0.525 | 0 | raw誤分類を出力 | 中 |
| general:246 | yearsincurrentrole | quantity | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.428–0.428 | 0 | raw誤り→guard unknown | 中 |
| general:265 | pelicula | text | blend50,sparse | 1,2,3 | unknown→unknown×3; wrong→category×3 | category×4; text×2 | 0.436–0.830 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:269 | female_frequency | rate | sparse | 1,2,3 | unknown→unknown×3 | rate×3 | 0.507–0.507 | 0 | raw正解→guard unknown | 中 |
| general:275 | attrition | category | sparse | 1,2,3 | wrong→quantity×3 | quantity×3 | 0.816–0.816 | 0 | raw誤分類を出力 | 中 |
| general:281 | spotify_url | other | sparse | 1,2,3 | other_ng→category×3 | category×3 | 0.969–0.969 | 0 | other誤受理 | 中 |
| general:282 | 読み方 | address | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×4; wrong→org×4; wrong→text×3 | address×3; org×4; text×4 | 0.335–0.823 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:286 | value | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→rate×15 | rate×15 | 0.734–0.925 | 0 | other誤受理 | 中 |
| general:291 | cleaned | text | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×3; wrong→account×2; wrong→category×10 | account×3; category×12 | 0.447–0.982 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| general:292 | abstract rank | other | ft,blend50,blend60,blend70 | 2,3 | other_ng→category×5 | category×5 | 0.565–0.964 | 0 | other誤受理 | 中 |
| general:296 | image_level_adj_acc | rate | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | other×15 | 0.515–0.981 | 0 | raw誤り→guard unknown | 中 |
| general:302 | episode | other | ft,sparse | 1,2,3 | other_ng→id×3; other_ng→quantity×2 | id×3; quantity×2 | 0.558–0.783 | 0 | other誤受理 | 中 |
| general:308 | ステーション名 | org | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→address×11 | address×12 | 0.485–0.900 | 0 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| general:309 | goal | id | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×1; wrong→category×12; wrong→quantity×2 | category×13; quantity×2 | 0.468–0.880 | 2 | raw誤分類を出力 / raw誤り→guard unknown | 中 |
| general:315 | standardhours | quantity | ft | 1 | unknown→unknown×1 | quantity×1 | 0.420–0.420 | 0 | raw正解→guard unknown | 低 |
| general:338 | denominatorweighted | quantity | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×12 | other×12 | 0.625–0.990 | 0 | raw誤り→guard unknown | 中 |
| general:339 | characteristicorder | other | sparse | 1,2,3 | other_ng→category×3 | category×3 | 0.631–0.631 | 0 | other誤受理 | 中 |
| general:340 | 登録年月日 | date | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | date×15 | 0.985–1.000 | 0 | raw正解→guard unknown | 中 |
| general:341 | 次に掲げるもの | category | sparse | 1,2,3 | unknown→unknown×3 | quantity×3 | 0.458–0.458 | 0 | raw誤り→guard unknown | 中 |
| general:342 | age_q1_nd | quantity | sparse | 1,2,3 | unknown→unknown×3 | other×3 | 0.382–0.382 | 0 | raw誤り→guard unknown | 中 |
| general:343 | mt2 | other | ft,blend50,blend60,blend70,sparse | 1,2,3 | other_ng→category×3; other_ng→quantity×8 | category×3; quantity×8 | 0.516–0.890 | 0 | other誤受理 | 中 |
| general:345 | 受講料(6ヶ月額) | amount | sparse | 1,2,3 | unknown→unknown×3 | amount×3 | 0.373–0.373 | 0 | raw正解→guard unknown | 中 |
| general:351 | operationid | other | ft,blend50,blend60,blend70 | 1,2,3 | other_ng→id×10 | id×10 | 0.534–0.878 | 0 | other誤受理 | 中 |
| general:352 | 法人代表者名及び役職 | person | sparse | 1,2,3 | unknown→unknown×3 | category×3 | 0.469–0.469 | 0 | raw誤り→guard unknown | 中 |
| general:362 | raw | category | blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×6; wrong→text×3 | category×4; text×5 | 0.387–0.719 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:370 | source_value | category | ft,blend50,blend60,blend70 | 1,2,3 | unknown→unknown×8; wrong→text×2 | category×6; other×1; text×3 | 0.307–0.723 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| general:377 | indicator | text | ft,blend70 | 1,3 | unknown→unknown×1; wrong→category×2 | category×2; text×1 | 0.493–0.711 | 0 | raw誤分類を出力 / raw正解→guard unknown | 中 |
| general:380 | 科名 | category | ft,blend50,blend60,blend70,sparse | 1,2,3 | unknown→unknown×15 | other×15 | 0.853–0.945 | 0 | raw誤り→guard unknown | 中 |
| general:382 | source | category | ft,blend50,blend60,blend70 | 2,3 | unknown→unknown×3; wrong→text×5 | category×2; text×6 | 0.459–0.899 | 0 | raw誤分類を出力 / raw正解→guard unknown / raw誤り→guard unknown | 中 |
| japan_procurement:83 | 資産名称 | text | sparse | 1,2,3 | wrong→address×3 | address×3 | 0.657–0.657 | 0 | raw誤分類を出力 | 中 |

## Lから予測が変わった出力

固定5集合・3 seed・5条件で予測ラベルが変わった全出力。改善/悪化/横ばいを明示する。

| seed | 集合:index | 条件 | 列名 | 正解 | L | L24 | L outcome | L24 outcome | 変化 |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | dev220:49 | ft | 税率 | rate | rate | tax_class | correct | wrong | 悪化 |
| 1 | dev220:130 | ft | 随意契約理由 | text | category | text | wrong | correct | 改善 |
| 1 | dev220:196 | ft | credit limit | amount | amount | unknown | correct | unknown | 悪化 |
| 1 | dev220:201 | ft | city | address | id | address | wrong | correct | 改善 |
| 1 | dev220:33 | blend50 | 商品オプション | text | unknown | text | unknown | correct | 改善 |
| 1 | dev220:40 | blend50 | メッセージ | text | category | unknown | wrong | unknown | 正誤不変 |
| 1 | dev220:156 | blend50 | name | person | person | unknown | correct | unknown | 悪化 |
| 1 | dev220:157 | blend50 | is a company | category | category | unknown | correct | unknown | 悪化 |
| 1 | dev220:168 | blend50 | website | text | unknown | text | unknown | correct | 改善 |
| 1 | dev220:211 | blend50 | item description | text | text | unknown | correct | unknown | 悪化 |
| 1 | dev220:151 | blend60 | taxable | category | tax_class | category | wrong | correct | 改善 |
| 1 | dev220:49 | blend70 | 税率 | rate | rate | unknown | correct | unknown | 悪化 |
| 1 | dev220:5 | sparse | 受注名 | person | category | unknown | wrong | unknown | 正誤不変 |
| 1 | dev220:12 | sparse | 発送先名 | person | org | address | wrong | wrong | 正誤不変 |
| 1 | dev220:27 | sparse | 作業者欄 | person | org | address | wrong | wrong | 正誤不変 |
| 1 | dev220:131 | sparse | 支出負担行為担当官 | person | unknown | text | unknown | wrong | 正誤不変 |
| 1 | dev220:156 | sparse | name | person | org | address | wrong | wrong | 正誤不変 |
| 1 | dev220:168 | sparse | website | text | address | category | wrong | wrong | 正誤不変 |
| 1 | dev220:183 | sparse | material | product | category | unknown | wrong | unknown | 正誤不変 |
| 1 | general:53 | ft | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | category | quantity | correct | wrong | 悪化 |
| 1 | general:94 | ft | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 1 | general:292 | ft | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:308 | ft | ステーション名 | org | address | org | wrong | correct | 改善 |
| 1 | general:315 | ft | standardhours | quantity | quantity | unknown | correct | unknown | 悪化 |
| 1 | general:343 | ft | mt2 | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:370 | ft | source_value | category | unknown | text | unknown | wrong | 正誤不変 |
| 1 | general:377 | ft | indicator | text | text | unknown | correct | unknown | 悪化 |
| 1 | general:382 | ft | source | category | text | category | wrong | correct | 改善 |
| 1 | general:53 | blend50 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | category | quantity | correct | wrong | 悪化 |
| 1 | general:94 | blend50 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 1 | general:175 | blend50 | bib | id | id | unknown | correct | unknown | 悪化 |
| 1 | general:238 | blend50 | 被害域長さ(100m)最小 | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 1 | general:282 | blend50 | 読み方 | address | unknown | org | unknown | wrong | 正誤不変 |
| 1 | general:351 | blend50 | operationid | other | unknown | id | other_ok | other_ng | 悪化 |
| 1 | general:47 | blend60 | mood | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:53 | blend60 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | category | quantity | correct | wrong | 悪化 |
| 1 | general:87 | blend60 | sens_final | rate | unknown | rate | unknown | correct | 改善 |
| 1 | general:94 | blend60 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 1 | general:282 | blend60 | 読み方 | address | unknown | org | unknown | wrong | 正誤不変 |
| 1 | general:291 | blend60 | cleaned | text | unknown | category | unknown | wrong | 正誤不変 |
| 1 | general:292 | blend60 | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:308 | blend60 | ステーション名 | org | address | unknown | wrong | unknown | 正誤不変 |
| 1 | general:343 | blend60 | mt2 | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 1 | general:351 | blend60 | operationid | other | unknown | id | other_ok | other_ng | 悪化 |
| 1 | general:47 | blend70 | mood | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:53 | blend70 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | category | quantity | correct | wrong | 悪化 |
| 1 | general:87 | blend70 | sens_final | rate | unknown | rate | unknown | correct | 改善 |
| 1 | general:94 | blend70 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 1 | general:291 | blend70 | cleaned | text | account | unknown | wrong | unknown | 正誤不変 |
| 1 | general:292 | blend70 | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 1 | general:308 | blend70 | ステーション名 | org | address | org | wrong | correct | 改善 |
| 1 | general:343 | blend70 | mt2 | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 1 | general:370 | blend70 | source_value | category | unknown | text | unknown | wrong | 正誤不変 |
| 1 | general:382 | blend70 | source | category | unknown | category | unknown | correct | 改善 |
| 1 | general:23 | sparse | gadiculus_argenteus | category | quantity | category | wrong | correct | 改善 |
| 1 | general:88 | sparse | yearswithcurrmanager | quantity | unknown | quantity | unknown | correct | 改善 |
| 1 | general:94 | sparse | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 1 | general:170 | sparse | n_occurences | quantity | unknown | quantity | unknown | correct | 改善 |
| 1 | general:207 | sparse | year_step_size | quantity | category | quantity | wrong | correct | 改善 |
| 1 | general:213 | sparse | age_q3_nd | quantity | unknown | rate | unknown | wrong | 正誤不変 |
| 1 | general:295 | sparse | units | category | unknown | category | unknown | correct | 改善 |
| 1 | general:317 | sparse | 日本語教室名 | org | text | org | wrong | correct | 改善 |
| 1 | general:352 | sparse | 法人代表者名及び役職 | person | category | unknown | wrong | unknown | 正誤不変 |
| 1 | business:101 | ft | entitiy | org | account | org | wrong | correct | 改善 |
| 1 | business:303 | ft | d1 | category | quantity | category | wrong | correct | 改善 |
| 1 | business:344 | ft | portefeuille_nom_et_code | org | id | unknown | wrong | unknown | 正誤不変 |
| 1 | business:348 | ft | regrp_nom | account | category | account | wrong | correct | 改善 |
| 1 | business:408 | ft | km budgété | other | quantity | unknown | other_ng | other_ok | 改善 |
| 1 | business:303 | blend50 | d1 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:304 | blend50 | d2 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:308 | blend50 | d6 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:343 | blend50 | commodity-title_fr | product | unknown | product | unknown | correct | 改善 |
| 1 | business:348 | blend50 | regrp_nom | account | unknown | account | unknown | correct | 改善 |
| 1 | business:401 | blend50 | ligne | category | unknown | category | unknown | correct | 改善 |
| 1 | business:459 | blend50 | australian sourced goods | amount | amount | unknown | correct | unknown | 悪化 |
| 1 | business:460 | blend50 | australian sourced services | amount | amount | unknown | correct | unknown | 悪化 |
| 1 | business:77 | blend60 | publisher label | org | org | unknown | correct | unknown | 悪化 |
| 1 | business:303 | blend60 | d1 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:304 | blend60 | d2 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:348 | blend60 | regrp_nom | account | unknown | account | unknown | correct | 改善 |
| 1 | business:77 | blend70 | publisher label | org | org | unknown | correct | unknown | 悪化 |
| 1 | business:303 | blend70 | d1 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:304 | blend70 | d2 | category | unknown | category | unknown | correct | 改善 |
| 1 | business:348 | blend70 | regrp_nom | account | unknown | account | unknown | correct | 改善 |
| 1 | business:55 | sparse | all p-cards payments for february 2022 | org | org | category | correct | wrong | 悪化 |
| 1 | business:92 | sparse | department | org | org | account | correct | wrong | 悪化 |
| 1 | business:275 | sparse | provider_name | org | text | unknown | wrong | unknown | 正誤不変 |
| 1 | business:308 | sparse | d6 | category | unknown | id | unknown | wrong | 正誤不変 |
| 1 | business:344 | sparse | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 1 | business:345 | sparse | organisme_nom_et_code | org | org | unknown | correct | unknown | 悪化 |
| 1 | business:408 | sparse | km budgété | other | amount | category | other_ng | other_ng | 正誤不変 |
| 1 | business2:13 | ft | cost centre description | account | unknown | org | unknown | wrong | 正誤不変 |
| 1 | business2:177 | ft | fine | amount | unknown | rate | unknown | wrong | 正誤不変 |
| 1 | business2:297 | ft | potential_epc_rating_known | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:326 | ft | fuel_poverty | rate | unknown | rate | unknown | correct | 改善 |
| 1 | business2:414 | ft | descript | address | address | text | correct | wrong | 悪化 |
| 1 | business2:440 | ft | situtation | address | text | category | wrong | wrong | 正誤不変 |
| 1 | business2:534 | ft | scheme | id | category | id | wrong | correct | 改善 |
| 1 | business2:946 | ft | service_responsable | account | category | account | wrong | correct | 改善 |
| 1 | business2:956 | ft | terminal | address | org | address | wrong | correct | 改善 |
| 1 | business2:962 | ft | service | account | unknown | org | unknown | wrong | 正誤不変 |
| 1 | business2:973 | ft | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | amount | unknown | correct | 改善 |
| 1 | business2:975 | ft | amt-units_mnt-unite | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:140 | blend50 | surveyname | text | text | unknown | correct | unknown | 悪化 |
| 1 | business2:233 | blend50 | super output area 2011 name | address | unknown | address | unknown | correct | 改善 |
| 1 | business2:295 | blend50 | potential_epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:322 | blend50 | imd19_national_decile | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:548 | blend50 | health service executive area | address | unknown | org | unknown | wrong | 正誤不変 |
| 1 | business2:962 | blend50 | service | account | category | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:975 | blend50 | amt-units_mnt-unite | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:75 | blend60 | monitor | id | category | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:295 | blend60 | potential_epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:297 | blend60 | potential_epc_rating_known | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:322 | blend60 | imd19_national_decile | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:440 | blend60 | situtation | address | text | category | wrong | wrong | 正誤不変 |
| 1 | business2:962 | blend60 | service | account | category | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:971 | blend60 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | amount | unknown | correct | unknown | 悪化 |
| 1 | business2:973 | blend60 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:975 | blend60 | amt-units_mnt-unite | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:13 | blend70 | cost centre description | account | unknown | org | unknown | wrong | 正誤不変 |
| 1 | business2:151 | blend70 | habitatdescription | text | unknown | text | unknown | correct | 改善 |
| 1 | business2:177 | blend70 | fine | amount | unknown | rate | unknown | wrong | 正誤不変 |
| 1 | business2:295 | blend70 | potential_epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:297 | blend70 | potential_epc_rating_known | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:322 | blend70 | imd19_national_decile | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:326 | blend70 | fuel_poverty | rate | unknown | rate | unknown | correct | 改善 |
| 1 | business2:440 | blend70 | situtation | address | text | category | wrong | wrong | 正誤不変 |
| 1 | business2:534 | blend70 | scheme | id | category | id | wrong | correct | 改善 |
| 1 | business2:962 | blend70 | service | account | unknown | org | unknown | wrong | 正誤不変 |
| 1 | business2:973 | blend70 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | quantity | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:975 | blend70 | amt-units_mnt-unite | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:13 | sparse | cost centre description | account | account | unknown | correct | unknown | 悪化 |
| 1 | business2:133 | sparse | b1a floorspace losses sqm | other | amount | unknown | other_ng | other_ok | 改善 |
| 1 | business2:149 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 1 | business2:163 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 1 | business2:179 | sparse | location | address | org | address | wrong | correct | 改善 |
| 1 | business2:229 | sparse | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 1 | business2:233 | sparse | super output area 2011 name | address | org | unknown | wrong | unknown | 正誤不変 |
| 1 | business2:237 | sparse | semi-detached | quantity | quantity | unknown | correct | unknown | 悪化 |
| 1 | business2:291 | sparse | epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 1 | business2:306 | sparse | wall_insulation_known | category | category | unknown | correct | unknown | 悪化 |
| 1 | business2:319 | sparse | solar_pv_area | other | unknown | address | other_ok | other_ng | 悪化 |
| 1 | business2:948 | sparse | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 1 | japan_procurement:83 | sparse | 資産名称 | text | text | address | correct | wrong | 悪化 |
| 2 | dev220:116 | ft | 履行場所 | address | id | address | wrong | correct | 改善 |
| 2 | dev220:130 | ft | 随意契約理由 | text | text | category | correct | wrong | 悪化 |
| 2 | dev220:154 | ft | shipping address | address | unknown | address | unknown | correct | 改善 |
| 2 | dev220:174 | ft | sales order | id | id | unknown | correct | unknown | 悪化 |
| 2 | dev220:201 | ft | city | address | id | address | wrong | correct | 改善 |
| 2 | dev220:156 | blend50 | name | person | person | unknown | correct | unknown | 悪化 |
| 2 | dev220:157 | blend50 | is a company | category | category | unknown | correct | unknown | 悪化 |
| 2 | dev220:174 | blend50 | sales order | id | id | unknown | correct | unknown | 悪化 |
| 2 | dev220:196 | blend50 | credit limit | amount | unknown | amount | unknown | correct | 改善 |
| 2 | dev220:174 | blend60 | sales order | id | id | unknown | correct | unknown | 悪化 |
| 2 | dev220:201 | blend60 | city | address | unknown | address | unknown | correct | 改善 |
| 2 | dev220:174 | blend70 | sales order | id | id | unknown | correct | unknown | 悪化 |
| 2 | dev220:201 | blend70 | city | address | id | address | wrong | correct | 改善 |
| 2 | dev220:5 | sparse | 受注名 | person | category | unknown | wrong | unknown | 正誤不変 |
| 2 | dev220:12 | sparse | 発送先名 | person | org | address | wrong | wrong | 正誤不変 |
| 2 | dev220:27 | sparse | 作業者欄 | person | org | address | wrong | wrong | 正誤不変 |
| 2 | dev220:131 | sparse | 支出負担行為担当官 | person | unknown | text | unknown | wrong | 正誤不変 |
| 2 | dev220:156 | sparse | name | person | org | address | wrong | wrong | 正誤不変 |
| 2 | dev220:168 | sparse | website | text | address | category | wrong | wrong | 正誤不変 |
| 2 | dev220:183 | sparse | material | product | category | unknown | wrong | unknown | 正誤不変 |
| 2 | general:94 | ft | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 2 | general:112 | ft | 住家全壊 | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | general:286 | ft | value | other | unknown | rate | other_ok | other_ng | 悪化 |
| 2 | general:291 | ft | cleaned | text | category | unknown | wrong | unknown | 正誤不変 |
| 2 | general:302 | ft | episode | other | quantity | unknown | other_ng | other_ok | 改善 |
| 2 | general:308 | ft | ステーション名 | org | address | org | wrong | correct | 改善 |
| 2 | general:382 | ft | source | category | category | text | correct | wrong | 悪化 |
| 2 | general:94 | blend50 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 2 | general:175 | blend50 | bib | id | unknown | id | unknown | correct | 改善 |
| 2 | general:245 | blend50 | 住家一部損壊 | quantity | category | quantity | wrong | correct | 改善 |
| 2 | general:370 | blend50 | source_value | category | unknown | category | unknown | correct | 改善 |
| 2 | general:382 | blend50 | source | category | category | unknown | correct | unknown | 悪化 |
| 2 | general:48 | blend60 | source | category | unknown | org | unknown | wrong | 正誤不変 |
| 2 | general:94 | blend60 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 2 | general:175 | blend60 | bib | id | unknown | id | unknown | correct | 改善 |
| 2 | general:224 | blend60 | study | text | unknown | text | unknown | correct | 改善 |
| 2 | general:245 | blend60 | 住家一部損壊 | quantity | category | quantity | wrong | correct | 改善 |
| 2 | general:282 | blend60 | 読み方 | address | unknown | address | unknown | correct | 改善 |
| 2 | general:382 | blend60 | source | category | category | unknown | correct | unknown | 悪化 |
| 2 | general:94 | blend70 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 2 | general:112 | blend70 | 住家全壊 | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | general:245 | blend70 | 住家一部損壊 | quantity | category | quantity | wrong | correct | 改善 |
| 2 | general:282 | blend70 | 読み方 | address | unknown | address | unknown | correct | 改善 |
| 2 | general:382 | blend70 | source | category | category | unknown | correct | unknown | 悪化 |
| 2 | general:23 | sparse | gadiculus_argenteus | category | quantity | category | wrong | correct | 改善 |
| 2 | general:88 | sparse | yearswithcurrmanager | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | general:94 | sparse | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 2 | general:170 | sparse | n_occurences | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | general:207 | sparse | year_step_size | quantity | category | quantity | wrong | correct | 改善 |
| 2 | general:213 | sparse | age_q3_nd | quantity | unknown | rate | unknown | wrong | 正誤不変 |
| 2 | general:295 | sparse | units | category | unknown | category | unknown | correct | 改善 |
| 2 | general:317 | sparse | 日本語教室名 | org | text | org | wrong | correct | 改善 |
| 2 | general:352 | sparse | 法人代表者名及び役職 | person | category | unknown | wrong | unknown | 正誤不変 |
| 2 | business:77 | ft | publisher label | org | org | address | correct | wrong | 悪化 |
| 2 | business:101 | ft | entitiy | org | category | org | wrong | correct | 改善 |
| 2 | business:225 | ft | description | account | account | text | correct | wrong | 悪化 |
| 2 | business:342 | ft | commodity-title_en | product | category | unknown | wrong | unknown | 正誤不変 |
| 2 | business:344 | ft | portefeuille_nom_et_code | org | account | org | wrong | correct | 改善 |
| 2 | business:450 | ft | sub_category | category | account | category | wrong | correct | 改善 |
| 2 | business:451 | ft | title | category | account | text | wrong | wrong | 正誤不変 |
| 2 | business:225 | blend50 | description | account | account | text | correct | wrong | 悪化 |
| 2 | business:271 | blend50 | net current expenditure - max english county councils | amount | amount | unknown | correct | unknown | 悪化 |
| 2 | business:344 | blend50 | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 2 | business:451 | blend50 | title | category | unknown | text | unknown | wrong | 正誤不変 |
| 2 | business:225 | blend60 | description | account | account | text | correct | wrong | 悪化 |
| 2 | business:344 | blend60 | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 2 | business:421 | blend60 | abn | id | unknown | id | unknown | correct | 改善 |
| 2 | business:451 | blend60 | title | category | unknown | text | unknown | wrong | 正誤不変 |
| 2 | business:41 | blend70 | total invoices paid | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | business:101 | blend70 | entitiy | org | category | org | wrong | correct | 改善 |
| 2 | business:225 | blend70 | description | account | account | text | correct | wrong | 悪化 |
| 2 | business:344 | blend70 | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 2 | business:347 | blend70 | regrp_sommaire | account | unknown | account | unknown | correct | 改善 |
| 2 | business:450 | blend70 | sub_category | category | unknown | category | unknown | correct | 改善 |
| 2 | business:451 | blend70 | title | category | unknown | text | unknown | wrong | 正誤不変 |
| 2 | business:55 | sparse | all p-cards payments for february 2022 | org | org | category | correct | wrong | 悪化 |
| 2 | business:92 | sparse | department | org | org | account | correct | wrong | 悪化 |
| 2 | business:275 | sparse | provider_name | org | text | unknown | wrong | unknown | 正誤不変 |
| 2 | business:308 | sparse | d6 | category | unknown | id | unknown | wrong | 正誤不変 |
| 2 | business:344 | sparse | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 2 | business:345 | sparse | organisme_nom_et_code | org | org | unknown | correct | unknown | 悪化 |
| 2 | business:408 | sparse | km budgété | other | amount | category | other_ng | other_ng | 正誤不変 |
| 2 | business2:288 | ft | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:291 | ft | epc_score_known | category | quantity | unknown | wrong | unknown | 正誤不変 |
| 2 | business2:295 | ft | potential_epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:330 | ft | conservation_area_site_id | category | id | category | wrong | correct | 改善 |
| 2 | business2:443 | ft | tree type | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:562 | ft | name | org | org | unknown | correct | unknown | 悪化 |
| 2 | business2:958 | ft | volume (mcf) | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | business2:975 | ft | amt-units_mnt-unite | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:149 | blend50 | projection | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:204 | blend50 | net current expenditure - max english county councils | amount | amount | unknown | correct | unknown | 悪化 |
| 2 | business2:233 | blend50 | super output area 2011 name | address | unknown | address | unknown | correct | 改善 |
| 2 | business2:238 | blend50 | terrace | quantity | quantity | unknown | correct | unknown | 悪化 |
| 2 | business2:288 | blend50 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:443 | blend50 | tree type | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:970 | blend50 | return-on-investments_revenus-de-placements | amount | amount | unknown | correct | unknown | 悪化 |
| 2 | business2:288 | blend60 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:298 | blend60 | number_habitable_rooms | quantity | category | unknown | wrong | unknown | 正誤不変 |
| 2 | business2:326 | blend60 | fuel_poverty | rate | rate | unknown | correct | unknown | 悪化 |
| 2 | business2:440 | blend60 | situtation | address | unknown | category | unknown | wrong | 正誤不変 |
| 2 | business2:443 | blend60 | tree type | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:531 | blend60 | value | quantity | quantity | unknown | correct | unknown | 悪化 |
| 2 | business2:958 | blend60 | volume (mcf) | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | business2:959 | blend60 | numéro | id | unknown | id | unknown | correct | 改善 |
| 2 | business2:972 | blend60 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | amount | unknown | correct | 改善 |
| 2 | business2:58 | blend70 | numbers of | date | date | unknown | correct | unknown | 悪化 |
| 2 | business2:90 | blend70 | total invoices paid | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | business2:288 | blend70 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:291 | blend70 | epc_score_known | category | quantity | unknown | wrong | unknown | 正誤不変 |
| 2 | business2:440 | blend70 | situtation | address | text | category | wrong | wrong | 正誤不変 |
| 2 | business2:443 | blend70 | tree type | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:958 | blend70 | volume (mcf) | quantity | unknown | quantity | unknown | correct | 改善 |
| 2 | business2:962 | blend70 | service | account | unknown | org | unknown | wrong | 正誤不変 |
| 2 | business2:972 | blend70 | sales-goods-svcs_ventes-biens-srvs | amount | unknown | amount | unknown | correct | 改善 |
| 2 | business2:13 | sparse | cost centre description | account | account | unknown | correct | unknown | 悪化 |
| 2 | business2:133 | sparse | b1a floorspace losses sqm | other | amount | unknown | other_ng | other_ok | 改善 |
| 2 | business2:149 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 2 | business2:163 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 2 | business2:179 | sparse | location | address | org | address | wrong | correct | 改善 |
| 2 | business2:229 | sparse | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 2 | business2:233 | sparse | super output area 2011 name | address | org | unknown | wrong | unknown | 正誤不変 |
| 2 | business2:237 | sparse | semi-detached | quantity | quantity | unknown | correct | unknown | 悪化 |
| 2 | business2:291 | sparse | epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 2 | business2:306 | sparse | wall_insulation_known | category | category | unknown | correct | unknown | 悪化 |
| 2 | business2:319 | sparse | solar_pv_area | other | unknown | address | other_ok | other_ng | 悪化 |
| 2 | business2:948 | sparse | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 2 | japan_procurement:83 | sparse | 資産名称 | text | text | address | correct | wrong | 悪化 |
| 3 | dev220:116 | ft | 履行場所 | address | address | id | correct | wrong | 悪化 |
| 3 | dev220:189 | ft | payment terms | category | category | text | correct | wrong | 悪化 |
| 3 | dev220:13 | blend50 | 発送先カナ | person | person | unknown | correct | unknown | 悪化 |
| 3 | dev220:33 | blend50 | 商品オプション | text | unknown | text | unknown | correct | 改善 |
| 3 | dev220:130 | blend50 | 随意契約理由 | text | unknown | text | unknown | correct | 改善 |
| 3 | dev220:143 | blend50 | terms | category | category | text | correct | wrong | 悪化 |
| 3 | dev220:151 | blend50 | taxable | category | tax_class | unknown | wrong | unknown | 正誤不変 |
| 3 | dev220:156 | blend50 | name | person | person | unknown | correct | unknown | 悪化 |
| 3 | dev220:196 | blend50 | credit limit | amount | unknown | amount | unknown | correct | 改善 |
| 3 | dev220:151 | blend60 | taxable | category | tax_class | category | wrong | correct | 改善 |
| 3 | dev220:143 | blend70 | terms | category | text | category | wrong | correct | 改善 |
| 3 | dev220:189 | blend70 | payment terms | category | category | unknown | correct | unknown | 悪化 |
| 3 | dev220:201 | blend70 | city | address | address | id | correct | wrong | 悪化 |
| 3 | dev220:5 | sparse | 受注名 | person | category | unknown | wrong | unknown | 正誤不変 |
| 3 | dev220:12 | sparse | 発送先名 | person | org | address | wrong | wrong | 正誤不変 |
| 3 | dev220:22 | sparse | その他費用 | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | dev220:27 | sparse | 作業者欄 | person | org | address | wrong | wrong | 正誤不変 |
| 3 | dev220:45 | sparse | 商品オプション | text | text | unknown | correct | unknown | 悪化 |
| 3 | dev220:69 | sparse | receive_order_status_id | category | unknown | category | unknown | correct | 改善 |
| 3 | dev220:73 | sparse | 支払を受ける者の住所又は居所 | address | category | address | wrong | correct | 改善 |
| 3 | dev220:131 | sparse | 支出負担行為担当官 | person | unknown | text | unknown | wrong | 正誤不変 |
| 3 | dev220:156 | sparse | name | person | org | address | wrong | wrong | 正誤不変 |
| 3 | dev220:168 | sparse | website | text | address | category | wrong | wrong | 正誤不変 |
| 3 | dev220:174 | sparse | sales order | id | unknown | id | unknown | correct | 改善 |
| 3 | dev220:183 | sparse | material | product | category | unknown | wrong | unknown | 正誤不変 |
| 3 | general:47 | ft | mood | other | unknown | category | other_ok | other_ng | 悪化 |
| 3 | general:53 | ft | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | category | wrong | correct | 改善 |
| 3 | general:65 | ft | app | category | unknown | category | unknown | correct | 改善 |
| 3 | general:94 | ft | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 3 | general:121 | ft | dag-stage | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:282 | ft | 読み方 | address | org | address | wrong | correct | 改善 |
| 3 | general:286 | ft | value | other | unknown | rate | other_ok | other_ng | 悪化 |
| 3 | general:291 | ft | cleaned | text | unknown | account | unknown | wrong | 正誤不変 |
| 3 | general:302 | ft | episode | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | general:343 | ft | mt2 | other | quantity | category | other_ng | other_ng | 正誤不変 |
| 3 | general:377 | ft | indicator | text | text | category | correct | wrong | 悪化 |
| 3 | general:94 | blend50 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 3 | general:105 | blend50 | authors | person | person | unknown | correct | unknown | 悪化 |
| 3 | general:121 | blend50 | dag-stage | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:238 | blend50 | 被害域長さ(100m)最小 | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | general:292 | blend50 | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:302 | blend50 | episode | other | id | unknown | other_ng | other_ok | 改善 |
| 3 | general:370 | blend50 | source_value | category | category | unknown | correct | unknown | 悪化 |
| 3 | general:382 | blend50 | source | category | category | text | correct | wrong | 悪化 |
| 3 | general:48 | blend60 | source | category | category | org | correct | wrong | 悪化 |
| 3 | general:53 | blend60 | 年齢区分(2:乳幼児,3:少年,4:成人,5:高齢者) | category | quantity | category | wrong | correct | 改善 |
| 3 | general:94 | blend60 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 3 | general:112 | blend60 | 住家全壊 | quantity | quantity | unknown | correct | unknown | 悪化 |
| 3 | general:286 | blend60 | value | other | unknown | rate | other_ok | other_ng | 悪化 |
| 3 | general:292 | blend60 | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:343 | blend60 | mt2 | other | quantity | unknown | other_ng | other_ok | 改善 |
| 3 | general:362 | blend60 | raw | category | category | unknown | correct | unknown | 悪化 |
| 3 | general:382 | blend60 | source | category | category | text | correct | wrong | 悪化 |
| 3 | general:48 | blend70 | source | category | category | org | correct | wrong | 悪化 |
| 3 | general:94 | blend70 | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 3 | general:121 | blend70 | dag-stage | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:148 | blend70 | mechanism | category | category | unknown | correct | unknown | 悪化 |
| 3 | general:224 | blend70 | study | text | text | person | correct | wrong | 悪化 |
| 3 | general:292 | blend70 | abstract rank | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:302 | blend70 | episode | other | id | unknown | other_ng | other_ok | 改善 |
| 3 | general:309 | blend70 | goal | id | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | general:343 | blend70 | mt2 | other | category | unknown | other_ng | other_ok | 改善 |
| 3 | general:351 | blend70 | operationid | other | unknown | id | other_ok | other_ng | 悪化 |
| 3 | general:362 | blend70 | raw | category | category | unknown | correct | unknown | 悪化 |
| 3 | general:382 | blend70 | source | category | unknown | text | unknown | wrong | 正誤不変 |
| 3 | general:39 | sparse | orcinus_orca | category | category | unknown | correct | unknown | 悪化 |
| 3 | general:88 | sparse | yearswithcurrmanager | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | general:94 | sparse | 名称_カナ | org | org | address | correct | wrong | 悪化 |
| 3 | general:207 | sparse | year_step_size | quantity | category | quantity | wrong | correct | 改善 |
| 3 | general:213 | sparse | age_q3_nd | quantity | unknown | rate | unknown | wrong | 正誤不変 |
| 3 | general:246 | sparse | yearsincurrentrole | quantity | category | unknown | wrong | unknown | 正誤不変 |
| 3 | general:295 | sparse | units | category | unknown | category | unknown | correct | 改善 |
| 3 | general:317 | sparse | 日本語教室名 | org | text | org | wrong | correct | 改善 |
| 3 | general:352 | sparse | 法人代表者名及び役職 | person | category | unknown | wrong | unknown | 正誤不変 |
| 3 | business:101 | ft | entitiy | org | account | category | wrong | wrong | 正誤不変 |
| 3 | business:237 | ft | purposeofexpenditure | text | text | account | correct | wrong | 悪化 |
| 3 | business:342 | ft | commodity-title_en | product | category | product | wrong | correct | 改善 |
| 3 | business:451 | ft | title | category | text | account | wrong | wrong | 正誤不変 |
| 3 | business:460 | ft | australian sourced services | amount | amount | quantity | correct | wrong | 悪化 |
| 3 | business:461 | ft | overseas sourced goods | amount | amount | quantity | correct | wrong | 悪化 |
| 3 | business:462 | ft | overseas sourced services | amount | amount | unknown | correct | unknown | 悪化 |
| 3 | business:343 | blend50 | commodity-title_fr | product | unknown | product | unknown | correct | 改善 |
| 3 | business:451 | blend50 | title | category | text | unknown | wrong | unknown | 正誤不変 |
| 3 | business:462 | blend50 | overseas sourced services | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business:101 | blend60 | entitiy | org | account | unknown | wrong | unknown | 正誤不変 |
| 3 | business:148 | blend60 | merchant details | text | unknown | category | unknown | wrong | 正誤不変 |
| 3 | business:225 | blend60 | description | account | account | text | correct | wrong | 悪化 |
| 3 | business:342 | blend60 | commodity-title_en | product | unknown | product | unknown | correct | 改善 |
| 3 | business:343 | blend60 | commodity-title_fr | product | unknown | product | unknown | correct | 改善 |
| 3 | business:408 | blend60 | km budgété | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business:421 | blend60 | abn | id | unknown | id | unknown | correct | 改善 |
| 3 | business:451 | blend60 | title | category | text | unknown | wrong | unknown | 正誤不変 |
| 3 | business:459 | blend60 | australian sourced goods | amount | amount | quantity | correct | wrong | 悪化 |
| 3 | business:460 | blend60 | australian sourced services | amount | amount | unknown | correct | unknown | 悪化 |
| 3 | business:462 | blend60 | overseas sourced services | amount | amount | quantity | correct | wrong | 悪化 |
| 3 | business:77 | blend70 | publisher label | org | org | unknown | correct | unknown | 悪化 |
| 3 | business:101 | blend70 | entitiy | org | unknown | category | unknown | wrong | 正誤不変 |
| 3 | business:237 | blend70 | purposeofexpenditure | text | text | account | correct | wrong | 悪化 |
| 3 | business:342 | blend70 | commodity-title_en | product | unknown | product | unknown | correct | 改善 |
| 3 | business:344 | blend70 | portefeuille_nom_et_code | org | id | unknown | wrong | unknown | 正誤不変 |
| 3 | business:408 | blend70 | km budgété | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business:451 | blend70 | title | category | text | account | wrong | wrong | 正誤不変 |
| 3 | business:459 | blend70 | australian sourced goods | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business:460 | blend70 | australian sourced services | amount | amount | quantity | correct | wrong | 悪化 |
| 3 | business:461 | blend70 | overseas sourced goods | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business:462 | blend70 | overseas sourced services | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business:55 | sparse | all p-cards payments for february 2022 | org | org | category | correct | wrong | 悪化 |
| 3 | business:92 | sparse | department | org | org | account | correct | wrong | 悪化 |
| 3 | business:275 | sparse | provider_name | org | text | unknown | wrong | unknown | 正誤不変 |
| 3 | business:304 | sparse | d2 | category | unknown | id | unknown | wrong | 正誤不変 |
| 3 | business:307 | sparse | d5 | category | category | id | correct | wrong | 悪化 |
| 3 | business:308 | sparse | d6 | category | category | id | correct | wrong | 悪化 |
| 3 | business:318 | sparse | number-of-disputes_nombre-de-différends | quantity | unknown | category | unknown | wrong | 正誤不変 |
| 3 | business:344 | sparse | portefeuille_nom_et_code | org | account | unknown | wrong | unknown | 正誤不変 |
| 3 | business:345 | sparse | organisme_nom_et_code | org | org | unknown | correct | unknown | 悪化 |
| 3 | business:408 | sparse | km budgété | other | amount | category | other_ng | other_ng | 正誤不変 |
| 3 | business:457 | sparse | defence goods value | amount | amount | unknown | correct | unknown | 悪化 |
| 3 | business:459 | sparse | australian sourced goods | amount | amount | unknown | correct | unknown | 悪化 |
| 3 | business:460 | sparse | australian sourced services | amount | unknown | id | unknown | wrong | 正誤不変 |
| 3 | business2:58 | ft | numbers of | date | date | unknown | correct | unknown | 悪化 |
| 3 | business2:126 | ft | a1 (retail) floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:127 | ft | a1 (retail) floorspace losses sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:129 | ft | a2 floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:130 | ft | a2 floorspace losses sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:151 | ft | habitatdescription | text | category | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:176 | ft | contravention | category | category | text | correct | wrong | 悪化 |
| 3 | business2:229 | ft | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 3 | business2:291 | ft | epc_score_known | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:295 | ft | potential_epc_score_known | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:297 | ft | potential_epc_rating_known | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:326 | ft | fuel_poverty | rate | rate | unknown | correct | unknown | 悪化 |
| 3 | business2:330 | ft | conservation_area_site_id | category | id | category | wrong | correct | 改善 |
| 3 | business2:381 | ft | total_verified_sales | quantity | amount | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:948 | ft | numéro_uev | id | id | unknown | correct | unknown | 悪化 |
| 3 | business2:11 | blend50 | merchant description | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:126 | blend50 | a1 (retail) floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:132 | blend50 | b1a floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:135 | blend50 | d2 floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:229 | blend50 | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 3 | business2:233 | blend50 | super output area 2011 name | address | unknown | address | unknown | correct | 改善 |
| 3 | business2:288 | blend50 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:379 | blend50 | terrace | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | business2:381 | blend50 | total_verified_sales | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | business2:548 | blend50 | health service executive area | address | unknown | org | unknown | wrong | 正誤不変 |
| 3 | business2:581 | blend50 | type of expenditure | account | category | account | wrong | correct | 改善 |
| 3 | business2:948 | blend50 | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 3 | business2:973 | blend50 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business2:975 | blend50 | amt-units_mnt-unite | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:126 | blend60 | a1 (retail) floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:132 | blend60 | b1a floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:135 | blend60 | d2 floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:154 | blend60 | surveyname | text | unknown | text | unknown | correct | 改善 |
| 3 | business2:229 | blend60 | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 3 | business2:288 | blend60 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:295 | blend60 | potential_epc_score_known | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:301 | blend60 | total_floor_area_known | category | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business2:330 | blend60 | conservation_area_site_id | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:379 | blend60 | terrace | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | business2:381 | blend60 | total_verified_sales | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | business2:531 | blend60 | value | quantity | quantity | unknown | correct | unknown | 悪化 |
| 3 | business2:581 | blend60 | type of expenditure | account | category | account | wrong | correct | 改善 |
| 3 | business2:948 | blend60 | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 3 | business2:971 | blend60 | refunds-prev-yrs-exp_recouv-deps-exs-ant | amount | amount | unknown | correct | unknown | 悪化 |
| 3 | business2:973 | blend60 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business2:58 | blend70 | numbers of | date | date | unknown | correct | unknown | 悪化 |
| 3 | business2:90 | blend70 | total invoices paid | quantity | quantity | unknown | correct | unknown | 悪化 |
| 3 | business2:126 | blend70 | a1 (retail) floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:127 | blend70 | a1 (retail) floorspace losses sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:129 | blend70 | a2 floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:130 | blend70 | a2 floorspace losses sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:132 | blend70 | b1a floorspace gains sqm | other | unknown | quantity | other_ok | other_ng | 悪化 |
| 3 | business2:154 | blend70 | surveyname | text | unknown | text | unknown | correct | 改善 |
| 3 | business2:176 | blend70 | contravention | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:177 | blend70 | fine | amount | unknown | rate | unknown | wrong | 正誤不変 |
| 3 | business2:229 | blend70 | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 3 | business2:288 | blend70 | construction_age_band | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:298 | blend70 | number_habitable_rooms | quantity | category | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:330 | blend70 | conservation_area_site_id | category | id | category | wrong | correct | 改善 |
| 3 | business2:370 | blend70 | average bids per property | other | unknown | amount | other_ok | other_ng | 悪化 |
| 3 | business2:379 | blend70 | terrace | quantity | unknown | quantity | unknown | correct | 改善 |
| 3 | business2:381 | blend70 | total_verified_sales | quantity | amount | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:581 | blend70 | type of expenditure | account | category | account | wrong | correct | 改善 |
| 3 | business2:948 | blend70 | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 3 | business2:973 | blend70 | proceeds-disp-surplus-assets_prods-vente-biens-excdnt | amount | unknown | quantity | unknown | wrong | 正誤不変 |
| 3 | business2:109 | sparse | column2 | address | unknown | text | unknown | wrong | 正誤不変 |
| 3 | business2:133 | sparse | b1a floorspace losses sqm | other | amount | unknown | other_ng | other_ok | 改善 |
| 3 | business2:135 | sparse | d2 floorspace gains sqm | other | quantity | unknown | other_ng | other_ok | 改善 |
| 3 | business2:149 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 3 | business2:163 | sparse | projection | category | category | id | correct | wrong | 悪化 |
| 3 | business2:179 | sparse | location | address | org | address | wrong | correct | 改善 |
| 3 | business2:229 | sparse | post code sector | address | address | unknown | correct | unknown | 悪化 |
| 3 | business2:233 | sparse | super output area 2011 name | address | org | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:290 | sparse | epc_score | other | id | unknown | other_ng | other_ok | 改善 |
| 3 | business2:291 | sparse | epc_score_known | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:299 | sparse | number_habitable_rooms_known | category | unknown | category | unknown | correct | 改善 |
| 3 | business2:306 | sparse | wall_insulation_known | category | category | unknown | correct | unknown | 悪化 |
| 3 | business2:322 | sparse | imd19_national_decile | category | id | unknown | wrong | unknown | 正誤不変 |
| 3 | business2:635 | sparse | expenditure | category | account | category | wrong | correct | 改善 |
| 3 | business2:948 | sparse | numéro_uev | id | id | address | correct | wrong | 悪化 |
| 3 | japan_procurement:83 | sparse | 資産名称 | text | text | address | correct | wrong | 悪化 |

- 変更出力: 472（改善 165、悪化 191、正誤不変 116）。

## 未完了

- label-fix実適用件数1492の独立照合。
- F1の先生2人独立ラベル、根拠裁定、L/L24一回限り予測・採用判定。
- 問題行の元値・兄弟列・UNIT・出典・前処理/token長を含む診断記録。現artifactだけでは根本原因は確定できない。
