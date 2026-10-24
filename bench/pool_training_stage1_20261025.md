# 教材庫の学習 第 1 段（検証つき 12 ジョブ）の事前記録（2026-10-25 Claude）

- オーナーの許可：2026-10-25「連絡箱，学習の開始を許可する」（ai-bridge の STATE.md「オーナーの承認が必要」への回答）
- 案の出どころ：`bench/training_env_audit_20261024.md` 4 章。**この記録は結果を見る前に固定する**。結果を見たあとで規則を変えない
- 教材庫：24,636 列・3,564 表・657 公開元（b001〜b012・jp3。jitsuris-train 3ad9aff）
- 固定試験・主セット #1・封印セット #2／#3・blind_set* は使わない（検証モード `FT_VAL=1` だけ）

## 条件（6 条件 × 種子 2 ＝ 12 ジョブ）
基準の設定（全ジョブ共通）：`intfloat/multilingual-e5-base 2 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_VAL=1`

| 記号 | 足す設定 | 見ること |
|---|---|---|
| (a) | `FT_POOL_VALONLY=1`（教材庫を学習しない。検証（教材庫）だけ同じ分け方で測る） | 教材庫なしの基準 |
| (b) | `FT_POOL=1`（1 様式 4 表まで） | 教材庫の効果 |
| (c) | `FT_POOL=1 FT_POOL_FAMILY_CAP=0` | 様式の上限の良し悪し |
| (d) | `FT_POOL=1 FT_POOL_HARD_COPIES=2` | 裁定した難しい列を重く |
| (e) | `FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160` | 表の題名を入力に |
| (f) | `FT_POOL=1 FT_POOL_UNDECIDABLE=2` | 決められない列を other として |

`FT_POOL_VALONLY` は (a) のために今回足した（`encoder_exp.py`。試験 `tests/test_title_undecidable.py`：学習の行は教材庫なしと同じ、検証（教材庫）は `FT_POOL=1` と同じ列）。足す前は (a) で検証（教材庫）が測れなかった。

1 回の依頼は 8 ジョブまでなので 2 回に分ける（同じ Kaggle の仕事なので順番に）：
- 依頼 A（種子 1）：`train intfloat/multilingual-e5-base 2 FT_SEED=1 <基準> FT_POOL_VALONLY=1 ++ FT_POOL_VALONLY= FT_POOL=1 ++ FT_POOL_VALONLY= FT_POOL=1 FT_POOL_FAMILY_CAP=0 ++ FT_POOL_VALONLY= FT_POOL=1 FT_POOL_HARD_COPIES=2 ++ FT_POOL_VALONLY= FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160 ++ FT_POOL_VALONLY= FT_POOL=1 FT_POOL_UNDECIDABLE=2`
- 依頼 B（種子 2）：同じ並びで `FT_SEED=2`。A が COMPLETE して結果を回収してから出す。A が ERROR／CANCEL なら再実行せず、原因を記録してオーナーに知らせる

見込み：1 ジョブ約 18 分（W1 の 543 秒の約 2 倍。見積りで実測ではない）、2 GPU で 3 波 → 1 回約 1 時間、2 回で約 2〜2.5 時間。

## 測るもの
- 主：**検証（教材庫）**の正解率と重大（見張り後、`score_real`。種子 2 つの平均）
- 副：**未知見出しの macro-F1**（検証（一般・業務・業務2・日本の調達）、`slice_eval.macro_f1(min_support=5)`、W1 と同じ定義。未知は各ジョブの学習行の見出しで決める）
- 記録だけ：各検証の正解率・不明・重大、学習の行数、1 ジョブの時間

## 判定の規則（差 1.5 ポイント未満は「差なし」）
1. **教材庫の効果**：(b) − (a) の検証（教材庫）の正解率。+1.5 以上なら「効いた」。未知見出しの macro-F1 が (a) より 1.5 以上下がったら、効いたとしても最終の学習の前にオーナーに相談する
2. **設定の選び方**：(c)〜(f) のうち、(b) より検証（教材庫）の正解率が +1.5 以上、かつ重大が (b) 以下、かつ未知見出しの macro-F1 が (b) − 1.5 以上のものを「良い」とする
3. 最終の学習（第 2 段、`FT_VAL` なし・`FT_KEEP=1`）の設定：「良い」がなければ (b)。1 つなら (b)＋それ。2 つ以上なら、検証（教材庫）の正解率が最も高い 1 つ。ほかの「良い」設定の組み合わせは試していないので、封印セット #2 の候補（最大 4）に回す
4. 封印セット #2 で、最終の候補と基準線（E5-base 版 31）を比べる（`specs/SEALED_EVAL_PROTOCOL.md` の合格の条件：+2.0 ポイント以上・差の 90% 区間の下限 0 超・重大が基準線以下）。ChatGPT・Claude の初回ラベルも同じ #2 の列で採点して並べる（同じ課題での比較。第 9 章）

## 結果
（依頼 A・B の結果をここに書く。上の規則は変えない）
