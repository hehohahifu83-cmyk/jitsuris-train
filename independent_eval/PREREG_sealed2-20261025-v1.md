# 事前登録 sealed2-20261025-v1（封印セット #2）

書いた人：Claude（2026-10-25）。オーナーの許可：2026-10-25「学習の開始を許可する。Claude やチャット GPT と比べてどの程度の能力かも比べて欲しい」
**予測より前にコミットする**。結果を見てから候補を足す・規則を変える・ラベルを付け替えることはしない（`specs/SEALED_EVAL_PROTOCOL.md` 第 6 章）。

- 登録のコミット SHA：このファイルを入れたコミット（連絡箱に書く）
- セット：`independent_eval/results/sealed2/sealed2.json`、SHA-256：`7ebecac4372898280d07bdd81f8ad3a123642a21a1ed89af0aeffa634c86355e`（1,030 列・300 表・68 公開元・日本語 68%・学習にある見出し 20%・最大の公開元 5.5%。凍結 2026-10-24 23:05 UTC）（`provenance.json`）
- 作り方：`independent_eval/sealed2.py`（eval2 の公開元だけ、規則で採用・凍結、値は誰も開いていない）
- ラベルの人とファイル SHA-256：Claude `9a635238f14d5c9115ff60c6c50aebeeabf2c6b4989220966562e8bce4beee13`（2026-10-25、予測を開かずに付けた・非公開） ／ ChatGPT `82c9777548892eb531bec8b3f9c90db51ac91e766eb463e313dbeb81c1e2e6c2` ／ 裁定後 `9aeeb6a1f450ea0ac082b6c93b88a124afa483eee1e6b96eeef7b10acdf4adc9`

## 候補と基準線
| 名前 | run | 種子 | 重みの SHA-256（model.safetensors） |
|---|---|---|---|
| 候補 C1：教材庫 24,636 列を学習（`FT_POOL=1`、`bench/pool_training_stage1_20261025.md` 第 2 段） | 40118170559 | 1 | a7028e711568cfa9b8647b506838db7a353b5b7edf6c1ec8f131f6ac6ec89825 |
| | | 2 | 282a6e7f5edf13e414daff80df261161e97e2f01fea7dba5bc3007b26515bd73 |
| | | 3 | bf967eb40cec826cf11e784d99a7e5284c1651fefc52e04a05515d604a2f1873 |
| 基準線：E5-base 版 31 | 39506074807 | 1 | 38c5b3442a5825d3b46e484897e5cce2d5cabbf4dfc051722cfcfafa81187fb7 |
| | | 2 | 80c11790ccbae558d6b01e40975da739a000696b2693537bb75b5766cfd04b71 |
| | | 3 | 739dbc55dfe3c89acf5f91ec3d1ca8f83203148d77a0dea2c0c2012910b4fe70 |

候補は C1 の 1 つだけ。

## 入力と見張り
- 入力：`encoder_context.format_encoder_text`（`evaluate_independent.py` が checkpoint の manifest から読む。ctx_unit=true、max_length=128、prefix "query: "）
- 見張り：主＝v9.1、副＝v10（予測ファイルに両方を残す。モデルの再実行なし）
- 予測：`.github/workflows/sealed2-predict.yml`、CPU、各重み 1 回だけ（台帳 `independent_eval/predictions_sealed2/ledger.jsonl`）。ERROR なら再実行しない

## ラベル
- LABEL_GUIDE **v1.9**。Claude と ChatGPT が別々に、予測ファイルを開かずに付ける。unknown と S の約束は主セットと同じ。非公開の `ai-bridge/labels/` に保存
- 照合と裁定は Claude（第 4 章）。決め方を足したくなったら LP 番号で記録し、ガイドは評価の後に改訂する

## 指標（第 5 章）
- 主指標：**未知の見出しの列の OK 率**（見張り後。OK＝正解、または正解が other で不明）。未知＝各モデルの学習行（版 31：教材庫なし、C1：教材庫あり）に見出しがない列。3 種子の平均
- 副指標：全体の OK 率、macro-F1（正解側 5 列以上）、重大、誤断定、不明の率、種類別、unknown の列への言い切り率
- 区間：表単位のブートストラップ 10,000 回（差は対応のある差）。90% 区間で判定、95% 区間も載せる

## 判定規則（第 6 章を写す）
- **C1 を採用候補にするのは**、裁定後のラベルで (1) 主指標の差（C1 − 基準線、3 種子平均）が **+2.0 ポイント以上**、(2) 差の **90% 区間の下限が 0 超**、(3) **重大の平均が基準線以下**、をすべて満たすとき。そうでなければ基準線を残す
- Claude のラベルだけ・ChatGPT のラベルだけでも同じ計算をし、結論が割れたら採用しない

## 先生との比較（第 9 章。オーナーの依頼「ChatGPT・Claude と比べてどの程度か」）
- Claude・ChatGPT の**初回ラベル**を裁定後のラベルで採点し、C1・基準線と同じ列・同じ採点（OK 率・重大・種類別）で並べる
- 先生の点は裁定の循環で甘く出る（食い違い率の半分ほど）ことを必ず併記する。先生が一致した列だけのモデルの OK 率も出す
- 判定（上の採用の規則）には使わない。報告だけ
