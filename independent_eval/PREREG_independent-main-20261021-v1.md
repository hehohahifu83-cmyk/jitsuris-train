# 事前登録 independent-main-20261021-v1

登録コミット SHA：本ファイルの作成コミット SHA を連絡箱の【進捗】に記録する（ファイルには自己参照しない）

セット ID：`independent-main-20261021-v1`  
セット SHA-256：`4b47c72d70c30982123eaccdcbd1c8f6707d8bf1db8159b3774f1a4078ff3d87`  
対象：32 表・313 列。ここに記録するのは主セットのみ。blind set、セット3・5・7は使わない。

## ラベルの固定

| 用途 | ファイル（ai-bridge の非公開 labels/） | SHA-256 |
|---|---|---|
| 主採点（裁定後） | `adjudicated-independent-main-20261021-v1.json` | `b73e8b75ae35f2642d35ff046e832e8ed20de6700478ea401bdd5dda8a11159f` |
| 副採点（Claude 初回） | `claude-independent-main-20261021-v1.json` | `e2d5181a2ce0739793b7f04cb3c34f917676a4fcc722ebdbb98b3f0605f219a8` |
| 副採点（ChatGPT 初回） | `chatgpt-independent-main-20261021-v1.json` | `2b7fcb1e86c3043345894d430e521f455d80a4d9e5e75c2b1e5a860f304a5fc5` |

初回ラベルの一致は 306/313（97.8%、κ=0.973）。一致した列 306、食い違った列 7（すべて NYC）。裁定後に採点する列は299（unknown 12、S 2を除外）。主セット内の5つの重大種類の正解列は211。ラベル値・列別ラベル・根拠はこの登録および公開リポジトリに含めない。

## 候補と基準線

基準線は E5-base の3 seed、候補は mmBERT-small の3 seed。仕事番号は seed と対応する（job1=seed 1、job2=seed 2、job3=seed 3）。いずれも微調整だけの重みを使い、seedを対応させて比較する。

| 役割 | モデル | run / job | seed | HF revision | 保存重み SHA-256 |
|---|---|---|---:|---|---|
| 候補 | mmBERT-small (`jhu-clsp/mmBERT-small`) | 39502740378 / job1 | 1 | `abc32620dd4f6ab06f5fbe905dc25f310618e09f` | `ed9a902d43b5f7a7fe0cbfca87660feefe04494805c8f47356f2705d30ce567c` |
| 候補 | mmBERT-small (`jhu-clsp/mmBERT-small`) | 39502740378 / job2 | 2 | `abc32620dd4f6ab06f5fbe905dc25f310618e09f` | `9201d775982decc971af65308de5782390ac47700e530595f1051d834a3b8eea` |
| 候補 | mmBERT-small (`jhu-clsp/mmBERT-small`) | 39502740378 / job3 | 3 | `abc32620dd4f6ab06f5fbe905dc25f310618e09f` | `284423e13cd745f300dc5b9b6849bbb55ff9d821e32513950eb158ae24890540` |
| 基準線 | E5-base (`intfloat/multilingual-e5-base`) | 39506074807 / job1 | 1 | `d128750597153bb5987e10b1c3493a34e5a4502a` | `38c5b3442a5825d3b46e484897e5cce2d5cabbf4dfc051722cfcfafa81187fb7` |
| 基準線 | E5-base (`intfloat/multilingual-e5-base`) | 39506074807 / job2 | 2 | `d128750597153bb5987e10b1c3493a34e5a4502a` | `80c11790ccbae558d6b01e40975da739a000696b2693537bb75b5766cfd04b71` |
| 基準線 | E5-base (`intfloat/multilingual-e5-base`) | 39506074807 / job3 | 3 | `d128750597153bb5987e10b1c3493a34e5a4502a` | `739dbc55dfe3c89acf5f91ec3d1ca8f83203148d77a0dea2c0c2012910b4fe70` |

## 入力と推論設定

- 入力形式：`encoder_context.format_encoder_text`。単位列の文脈 `FT_CTX_UNIT=1`、最大長 `max_length=128`。
- mmBERT-small の prefix は空、E5-base は `query: `。モデル revision と tokenizer は各 checkpoint manifest の固定値を使う。
- 学習 manifest の tokenizer/runtime：Python 3.13.15、transformers 5.16.1、tokenizers 0.23.1、safetensors 0.8.0、torch 2.11.0+cu128。予測は CPU で実行する。評価 runner の CPU torch 版は実行環境記録に残す。
- モデル重みは各1回だけ推論する。予測後は保存した確率と同じ推論の guard 判定を使い、guard の版を変える目的でモデルを再実行しない。

## 見張り・採点

- 主：Guard v9.1。副：Guard v10（S7完了後のみ）。予測 manifest は主版を `guard_version=v9.1` と記録し、同じ予測に v9.1 と v10 の判定を保存する。副採点は保存済み予測から行い、重みを再実行しない。
- 確率下限 0.5、数値系 top-2 差 0.25。
- LABEL_GUIDE v1.5。裁定後ラベルを主採点、Claude 初回・ChatGPT 初回の各ラベルを副採点に使う。unknown と S は採点から除外し、unknown の列への言い切り数・率を別記する。
- 層別：見出し既知／未知、出典、言語、種類、先生の一致306列／食い違い7列。5種類の重大ラベルは5×5混同行列も出す。
- 主指標：未知見出し列のガード後 OK 率（正解、または正解が other で「不明」）。副指標・出表は `specs/SEALED_EVAL_PROTOCOL.md` 第5章のとおり。報告区間は表単位の復元抽出10,000回による95%区間、モデル差は対応のある差の区間。重大0件なら95%上限 `3/n` を併記する。
- 主セット #1 の判定：mmBERT-small を採るのは、未知見出し OK 率の平均が E5-base より2.0ポイント以上高く、重大の平均が E5-base 以下で、差の90%区間下限が0を超える場合だけ。それ以外は E5-base を残す。
- Claude 初回ラベルと ChatGPT 初回ラベルで判定が分かれたら採用しない。裁定後ラベルでも同じ結論の場合だけ候補を採る。
- 予測後の候補追加、規則変更、ラベル付け替えは禁止。主セットの結果から学習教材・モデル設定を作らない。

