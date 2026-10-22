# S11 第 1 陣（jp3）を学習に足す（事前記録・2026-10-22 12:12 JST Claude）

## 教材
- 3.1（日本の財務・調達）の確定 83 表から、学習の表と URL が同じ 1 表を除く 82 表を採用（`materials/s11_3_1_adopted_20261022.json`）。
- `materials/fetch_rows.py`（Actions `s11-fetch-rows.yml`）で 72 表・504 列を取り出した（`materials/real_corpus_jp3.jsonl`。行をそろえた値 `row_values` つき）。
- ラベル（DATA_COLLECTION_PROTOCOL 第 6 章）：先生 1＝ChatGPT が 504 列（`materials/real_labels_jp3_chatgpt.jsonl`、SHA-256 114a282c…）。今のモデル（E5-base 最終比較の種子 1、Actions `label-assist-predict.yml`）の予測と比べて、**一致 350 列は採用**（10% の 35 列を Claude が抜き取り確認、誤り 0）、**食い違い 154 列は Claude が LABEL_GUIDE v1.5 だけで裁定**（`materials/jp3_adjudication_20261022.jsonl` に理由つき）。
- 学習に使うのは unknown・S を除いた **426 列・67 表**（`materials/real_labels_jp3.jsonl`）。内訳：amount 178・category 57・date 42・id 42・account 36・address 22・quantity 17・rate 13・text 8・other 7・org 4。
- LP の候補（評価の後のガイド改訂で扱う）：会計名称（一般会計・特別会計）が account か category か／地方公共団体名・自治体名が address（市区町村）か org（役所）か（今回は address 行の「市区町村」に従った）／税目は account（費目）として扱った。

## 比べ方（1 要因：`FT_JP3=1`）
- 基準線：W3a・W4 と同じ 3 本（W1 の job3・job6、W3a の回の job4）。W 群：今回の job1〜3（種子 1〜3）。すべて `FT_VAL=1`・`FT_REAL_FRAC=1.0`・基準の設定。
- jp3 は学習側だけに入れる（検証の 889 列は同じ）。学習の行 50,491 → 53,047（＋2,556＝426 列 × 6 倍、表あたり 60 の上限は効かない）。
- 未知見出しは、**基準線の学習で未知だった 255 列に固定**（jp3 を足すと学習側の見出しが増えるため、比べる列を動かさない）。

## 判定の規則（事前に固定。W3a・W4 と同じ形）
- 主：固定の 255 列の OK 率の 3 種子平均で、+jp3 − 基準線 ≥ **+1.0 ポイント**、かつ全 889 列の重大の 3 種子平均が基準線**以下**なら、封印セット #2 に出す候補。
- 副（判定には使わない）：検証（日本の調達）66 列の OK 率、未知見出し macro-F1、全 889 列の OK 率。
- 注意：足すのは学習の行の約 5% で、検証には日本の財務の表が少ない（日本の調達 66 列）。差が出なくても、それは「この検証では見えない」ことがありうる。本当の判定は封印セット #2。

## 依頼と見積り
```text
intfloat/multilingual-e5-base 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_VAL=1 FT_REAL_FRAC=1.0 FT_JP3=1 ++ FT_SEED=2 ++ FT_SEED=3
```
3 本。1 本 約 9〜10 分、2 GPU で 2 波、**約 25〜30 分**（見積り）。

## 依頼のやり直し（2026-10-22 Claude）
- 最初の依頼（c99bcb7、Actions run 39715577031）は、Kaggle に送る束（`kaggle/kaggle.sh` の決め打ちの一覧）に `materials/real_labels_jp3.jsonl` が入っていなかった。`load_real` は無いファイルを黙って飛ばすので、そのままでは jp3 を 0 行足した学習（＝基準線と同じ）になる。Actions を取り消し、依頼を `done` に戻した。束の一覧に足し、`FT_JP3=1` でファイルが無い・0 行なら止めるようにした。
- Kaggle に古い束がすでに送られていた可能性がある。その学習が COMPLETE になってから（動いている学習を置き換えない）、上と同じ依頼の行で出し直す。古い束の学習の結果は使わない。
