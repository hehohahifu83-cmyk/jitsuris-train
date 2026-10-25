# b013・b014 を入れた学習し直し 第 1 段（検証つき 8 ジョブ）の事前記録（2026-10-25 Claude）

- オーナーの許可：2026-10-25「連絡箱、許可する」（ai-bridge `messages/20261025-2021_claude-to-chatgpt_beat-teachers-plan.md` の「学習のし直しは引き続き許可待ち」、STATE.md「b013・b014追加再学習はオーナー許可待ち」への回答）
- **この記録は結果を見る前に固定する**。結果を見たあとで規則を変えない
- 教材庫：27,070 列（b001〜b014・jp3）。C1（run 40118170559）は b001〜b012・jp3 で学習した
- 固定試験・主セット #1・封印セット #2／#3・blind_set* は使わない（検証モード `FT_VAL=1` だけ）
- 封印セット #3 の凍結構成（C1 種子 1 ＋ recheck v1 ＋ 検査役 v2 ＋ rho_assert 0.7、HANDOFF.md）はこの学習で**変えない**。新しい本体（C2）は recheck・検査役・rho を、C2 が見ていない陣（b015 以降）で決め直すまで封印セットに出さない

## 条件（4 条件 × 種子 2 ＝ 8 ジョブ、1 回の依頼）
基準の設定（全ジョブ共通。第 1 段 `bench/pool_training_stage1_20261025.md` と同じ）：`intfloat/multilingual-e5-base 2 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_VAL=1 FT_POOL=1`

| 記号 | 足す設定 | 見ること |
|---|---|---|
| (a) | `FT_POOL_EXCLUDE=b013,b014` | C1 と同じ教材（b013・b014 を学習しない） |
| (b) | なし | b013・b014 の効果 |
| (c) | `FT_TITLE=1 FT_MAX_LEN=160` | 表の題名を入力に（ChatGPT の案 ②） |
| (d) | `FT_POOL_HARD_COPIES=2` | 裁定した難しい列を重く |

`FT_POOL_EXCLUDE` は (a) のために今回足した（`encoder_exp.py`。試験 `tests/test_title_undecidable.py`：検証（教材庫）は `FT_POOL=1` と同じ列、外した陣の表は学習に残らない）。分け方は様式ごと（`split_val_by_family`、salt `jitsuris-poolval-v2`）なので、検証（教材庫）は 4 条件とも同じ 3,165 列（うち b013・b014 の表 264 列）。教材庫の学習の行は (b) 21,668、(a) はそこから b013・b014 の 2,076 を外したもの（様式の上限の前）。

依頼：`train intfloat/multilingual-e5-base 2 FT_SEED=1 <基準> FT_POOL_EXCLUDE=b013,b014 ++ FT_POOL_EXCLUDE= ++ FT_POOL_EXCLUDE= FT_TITLE=1 FT_MAX_LEN=160 ++ FT_POOL_EXCLUDE= FT_POOL_HARD_COPIES=2 ++ FT_SEED=2 ++ FT_SEED=2 FT_POOL_EXCLUDE= ++ FT_SEED=2 FT_POOL_EXCLUDE= FT_TITLE=1 FT_MAX_LEN=160 ++ FT_SEED=2 FT_POOL_EXCLUDE= FT_POOL_HARD_COPIES=2`（`jobs.split_jobs` で 8 ジョブに分かれることを確かめた）。ERROR／CANCEL なら再実行せず、原因を記録してオーナーに知らせる

見込み：1 ジョブ約 20 分（第 1 段の 1,050〜1,220 秒）、2 GPU で 4 波 → 約 1.5 時間（見積り）

## 測るもの
- 主：**検証（教材庫）**の正解率と重大（見張り後、`score_real`。種子 2 つの平均）
- 副：**未知見出しの macro-F1**（検証（一般・業務・業務2・日本の調達）、`slice_eval.macro_f1(min_support=5)`、第 1 段と同じ定義）
- 参考（判定に使わない。264 列と少ない）：検証（教材庫）のうち b013・b014 の表の列の正解率・重大
- 記録だけ：各検証の不明、学習の行数、1 ジョブの時間

## 判定の規則（差 1.5 ポイント未満は「差なし」）
1. **b013・b014 の効果**：(b) − (a) の検証（教材庫）の正解率。+1.5 以上なら「効いた」、−1.5 以下か重大が (a) の 1.2 倍を超えたら「悪くなった」→ 第 2 段に進まずオーナーに相談する。それ以外（差なし）は、教材を増やして悪くならないので (b) で進む
2. **設定の選び方**：(c)・(d) のうち、次のどちらかを満たすものを「良い」とする（オーナー指示「重大ゼロ」を重く見て、重大の減りも数える）
   - 検証（教材庫）の正解率が (b) より +1.5 以上、かつ重大が (b) 以下、かつ未知見出しの macro-F1 が (b) − 1.5 以上
   - 重大が (b) の 0.8 倍以下、かつ正解率が (b) − 0.5 以上、かつ未知見出しの macro-F1 が (b) − 1.5 以上
3. **第 2 段**（`FT_VAL` なし・`FT_KEEP=1`・種子 1〜3、C2）：「良い」がなければ (b)。1 つなら (b)＋それ。2 つなら重大の少ない方（同じなら正解率の高い方）
4. C2 は封印セット #3 に自動では出さない。C2 が見ていない陣（b015）で C2 の予測を出し、recheck・検査役・rho を b013・b014 と同じ手順で決め直してから、#3 に出すのが C1 か C2 かを #3 の凍結より前に決めてオーナーに伝える

## 結果
（依頼の結果をここに書く。上の規則は変えない）
