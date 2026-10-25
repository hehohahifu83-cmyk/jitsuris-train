# granite-embedding を本体の入れ替え候補・専門家として学習する（事前記録、2026-10-26 Claude）

- オーナーの許可：2026-10-26「きょかする」（数字の専門家 v3 のあと、「granite-embedding の専門家の学習（Kaggle の GPU）を始めてよいか」への回答）
- 選んだ理由：ChatGPT と相談した専門家の選定（`research/experts-plan-2026-10-25.md` の B）。木のモデル＋辞書の専門家は難しい列で正しさ 95% に届かなかった（`bench/numeric_expert_v3.md`）
- モデル：`ibm-granite/granite-embedding-278m-multilingual`（Apache 2.0、約 2.8 億、e5-base と同じ XLM-R の形。前置き文なし）。融合はしない
- **この記録は結果を見る前に固定する**。封印セット・固定試験の結果は採否に使わない

## 学習（2 ジョブ、1 回の依頼）
C1 と同じ設定・同じ教材（b012 まで＋jp3）で、本体だけを入れ替える（ラベルの掃除 bc3ce81 の分だけ C1 と違う）：
`train ibm-granite/granite-embedding-278m-multilingual 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_POOL=1 FT_POOL_EXCLUDE=b013,b014 FT_KEEP=1 ++ FT_SEED=2`
- b013・b014 を外すので、C1 と同じく b013・b014 は見ていない陣として測れる。ERROR／CANCEL なら再実行せず原因を記録する

## 測る（b013・b014、other 以外 2,196 列。製品の形＝見張り → recheck v1 → 検査役 v2（b001〜b012 で学ぶ）→ rho 0.7。道具は `research/merge/merge_eval.py score` と同じ）
### 判定 1：本体の入れ替え
- granite（種子 1・2 の平均）と C1（種子 1・2 の平均。予測は `research/merge/preds/c1_*`・`seed2_*`）を比べる
- 「入れ替えて良い」＝製品の形の正解率 +1.5 ポイント以上、かつ重大が C1 以下、かつ不明 10% 以下。それ以外は「差なし」または「悪い」（−1.5 以下）
### 判定 2：2 つのモデルを専門家として使う（C1 種子 1 ＋ granite 種子 1）
- 救済：C1 の製品の形で不明の列のうち、C1 の 1 位（raw）と granite の見張り後の答えが同じで、それが C1 の上位 2 つに入るとき、その答えで言い切る
- 再検査：C1 が数字の種類と言い切った列で、granite の見張り後の答えが別の数字の種類なら不明
- 「良い」＝重大 ≤ 0.2%（4 列以下）かつ正解率 +1.0 ポイント以上（救済・再検査・両方の 3 通りを出し、どれか 1 つでも満たせば次の陣で確かめる）
- どちらの判定も**開発用**（b013 は rho を決めた陣）。採否は b015 で、確かめは b016
- 記録だけ：固定試験（C1 との回帰の比べ）、1 ジョブの時間、2 つのモデルの誤りの重なり

## 1 回目の依頼：ERROR（run 40242183928、開始から約 2 分）。結果は 1 つも出ていない
- 原因：granite の重みは bfloat16 で保存されていて、学習の道具がそのまま読み込んだため、GPU の float16 の自動混合精度（GradScaler）が「BFloat16 には未実装」で止まった（`NotImplementedError: "_amp_foreach_non_finite_check_and_unscale_cuda" not implemented for 'BFloat16'`）
- 直し：`finetune_exp.py` で読み込み直後に float32 にそろえる（e5 はもともと float32 なので変わらない。commit 7ca499c）。CPU の試運転（granite-smoke.yml）で、そろえる・数ステップの学習・保存が通ることを確かめた
- 原因が特定でき、直したうえで、**同じ設定で 2 回目を依頼する**（判定の規則は変えない）。「ERROR なら再実行しない」は原因の分からない失敗をやみくもに再実行しないための決まりで、今回は原因を直した再依頼

## 結果
（ここに書く。上の規則は変えない）
