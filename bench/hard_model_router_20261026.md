# 苦手克服モデル H と使い分けの手順書 v0（事前記録、2026-10-26 Claude）

- オーナー指示（2026-10-26）：「専門家を減らして今の本体、検査役、ミスや不明となった項目と似た教材のみを重点的に学習させたモデル、それを使い分けるための判断に必要な手順書？とりあえず使い分けられる能力をつける」
- **この記録は結果を見る前に固定する**。封印セット・固定試験は採否に使わない

## H の学習（1 ジョブ）
- 教材の一覧：`research/experts/hard_list.py` → `materials/pool/hard_list.jsonl`（6,003 列：版 31 が間違えた 2,239・不明 1,100、同じ取り違えで迷った 1,388、同じ列名 1,276。b001〜b014 だけ）
- 設定：C2 と同じ（`FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160 FT_KEEP=1`）＋ `FT_POOL_EXCLUDE=b015,b016`（評価に残す）＋ `FT_POOL_HARD_LIST=materials/pool/hard_list.jsonl FT_POOL_HARD_LIST_COPIES=3`（学習で重なる列 5,676）
- 依頼：`train intfloat/multilingual-e5-base 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160 FT_KEEP=1 FT_POOL_EXCLUDE=b015,b016 FT_POOL_HARD_LIST=materials/pool/hard_list.jsonl FT_POOL_HARD_LIST_COPIES=3`
- ERROR／CANCEL なら原因を記録し、原因を直したときだけ同じ設定で依頼し直す

## 測る（手順書 v0：`research/router-procedure.md`）
- 開発用：b015＋b016（本体 C2・H とも見ていない。採点 112 列）。確かめ：b017（アイルランド・カナダ、ラベル後）
- 比べる形：(0) 今の製品の形（C2＋recheck v1＋検査役 v2＋rho 0.7）、(0') (0) から rho をなくした形、(1) 手順書 v0（手順 3・4、rho なし）、(2) 手順書 v0＋rho
- 線 T_H：{0.7, 0.8, 0.9, 0.95, 0.98} から b015・b016 で「重大 ≤ 0.2%（112 列なら 0 列）かつ正解率 ≥ (0)」を満たす一番低い値。満たす値がなければ「手順書 v0 は採らない」
- 確かめ（b017）：選んだ T_H で、正解率が (0) より上、かつ重大 ≤ 0.2%
- 記録だけ：H 単独の製品の形、本体と H の誤りの重なり、H が救った列・壊した列の数

## 結果
（ここに書く。上の規則は変えない）
