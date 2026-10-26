# 事前登録 sealed3-20261025-v1（封印セット #3・合格判定）

書いた人：Claude（2026-10-25）。オーナー指示：2026-10-25「重大な間違いをゼロにできるまでは商品化は視野に入れない」「全体の0.2%でいい」「8〜10%を目指そう」、
「今の C1 のまま封印セット #3 の準備に入る」に「そうしてくれ」。
**予測より前にコミットする**。結果を見てから候補を足す・規則を変える・ラベルを付け替えることはしない（`specs/SEALED_EVAL_PROTOCOL.md` 第 6 章）。

- 登録のコミット SHA：このファイルの確定版を入れたコミット（連絡箱に書く）
- セット：`independent_eval/results/sealed3/sealed3.json`、SHA-256：**（凍結のときに書く）**。検査役の入力 `table_rows.json` の SHA-256：**（凍結のときに書く）**（`provenance.json`）
- 作り方：`independent_eval/sealed3.py`（eval3 の公開元だけ、#2 と同じ規則で採用・凍結、値は誰も開いていない。列 1,800 以上）
- ラベルの人とファイル SHA-256：予測の後に、Claude・ChatGPT が別々に付けて連絡箱に書く

## 判定する形（製品に入れる形。ここで固定）
| 段 | 中身 | 版・設定 |
|---|---|---|
| 本体 | C1：教材庫 24,636 列を学習（run 40118170559 の種子 1） | model.safetensors SHA-256 `a7028e711568cfa9b8647b506838db7a353b5b7edf6c1ec8f131f6ac6ec89825` |
| 見張り | 予測ファイルの `guarded_prediction`（主＝v9.1） | `evaluate_independent.py predict` の既定 |
| recheck v1 | 言い切りの検査と不明の再検査 | `recheck.apply_table`、t＝0.95、見張り v11 の列名の日付の規則（`guard.header_date_ok`） |
| 検査役 v2 | 列名を読まず、値と表の中の関係を見る木のモデル | `models/verifier_v2.json`（b001〜b013 で学んだもの）SHA-256 `0392b885c4290ca5a592624dd0e75cdbab533cf20adce97ef3cd717edf9d7fb7`、tau＝0.05、重大検知役は使わない |
| 候補の言い切り戻し | 本体と検査役の 1 位がそろう不明を言い切りに戻す | rho_assert＝0.7（b013 で決め、b014 で確かめた。`bench/verifier_c1_b013.md`・`bench/verifier_c1_b014.md`） |

- 採点の道具：`independent_eval/sealed3_score.py`（b014 を同じ形にして流し、`verifier_c1.py` の数字を再現することを確かめた）
- 参考に並べるもの（判定には使わない）：基準線 E5-base 版 31（run 39506074807 の種子 1、`38c5b3442a5825d3b46e484897e5cce2d5cabbf4dfc051722cfcfafa81187fb7`）に同じ形を重ねたもの、各段ごとの数字、先生（Claude・ChatGPT）の初回ラベルの点（第 9 章）

## 入力と予測
- 入力：`encoder_context.format_encoder_text`（`evaluate_independent.py` が checkpoint の manifest から読む。ctx_unit=true、max_length=128、prefix "query: "）
- 予測：`.github/workflows/sealed3-predict.yml`、CPU、各重み 1 回だけ（台帳 `independent_eval/predictions_sealed3/ledger.jsonl`）。ERROR なら再実行しない

## ラベル
- LABEL_GUIDE **v2.0**（2026-10-26、オーナーの決定で #3 のラベル付けより前に v1.9 から上げた。下書きの段階の変更で、まだ凍結していない）。Claude と ChatGPT が別々に、予測ファイルを開かずに付ける。unknown と S の約束は主セットと同じ。非公開の `ai-bridge/labels/` に保存
- 照合と裁定は Claude（第 4 章）。決め方を足したくなったら LP 番号で記録し、ガイドは評価の後に改訂する
- **裁定はモデルの答えを見ずに行う**（ChatGPT の案、2026-10-25）：Claude は裁定が済むまで予測ファイル・採点の結果を開かない。初回の 2 つのラベル・裁定のラベル・根拠・食い違いの理由を消さずに残す

## 判定の規則（合格の線）
- 数え方：`verifier_eval.score`（＝`llm_baseline.score_real`）。正解が unknown・S・person の列は数えない。**採点した列＝n**、重大＝数字の種類（date・amount・quantity・rate・id）どうしの取り違え
- **合格**：n ≥ 1,500、かつ **重大 ÷ n ≤ 0.2%**、かつ **不明 ÷ n ≤ 10%**（不明と答えた列も n に入る）
- n < 1,500 なら「判定できない」（合格にしない）。どちらかの線を超えたら不合格
- 残った重大は 1 列ずつ見直す。正解のラベルの誤りと分かったものは裁定の記録に LP 番号で残し、**直す前と直した後の両方の数字**を出す。合格の判定は直す前の数字で行い、直した後の数字は参考
- 重大の割合の 90% の上側の限界（Clopper-Pearson）も併記する（判定には使わない）
- 不合格なら #3 は使い切りとし、原因分析のあと #4 を作る

## 先生との比べ方（判定には使わない。ChatGPT の案、2026-10-25）
- 同じ列で、ChatGPT の初回ラベル・Claude の初回ラベル・製品の形のジツリスを、裁定後のラベルに対して並べる：全体の正解率（不明は誤りとして分母に入れる）、言い切った列の正解率と言い切った割合（必ず対で）、重大の割合、macro-F1。種類別・言語別も出す
- 差の区間は、**表ごとにまとめた paired bootstrap**（表を単位に 10,000 回、90% 区間）で出す。「ジツリスが先生を上回った」と言うのは、ChatGPT・Claude の両方に対する差の区間がどちらも 0 を超えたときだけ
- 言い方は「裁定済みの LABEL_GUIDE の基準に対して」とし、「本当の正解率で」とは言わない（人の目での確認はしない：オーナー指示）
- 種類ごとの勝ち負けは、その種類が 100 列未満なら参考にとどめる

## 使い切り
- 採点が済んだら `independent_eval/SETS.md` に、使った日・候補・結果の場所・「以後の変更の判定には使わない」を書く
