# 事前記録：銀教材で下地を作った L24（L24S）と今の L24 を分けて比べる（2026-11-13 Claude。学習・予測の前に書く）

## オーナーの指示
- 2026-11-12「銀教材を全て学習させたジツリスと今のジツリスを分けて比較できるか？」→ Claude の説明（前回 C3b・C3s の結果）→「それ（なら）銀教材をもう一度 Codex と共にチェックし、前回重大が増えた原因を特定したのちに学習を開始しろ」。
- 学習は Kaggle の無料の GPU 枠（費用なし）。「銀教材は使わない」（2026-11-05）の例外は**この比べる実験だけ**。製品は L24 のまま。

## 原因の特定（学習の前に済ませた）
- Claude：`research/silver_crit_why.md`。Codex の再現と点検：`research/silver_review_codex/`（ai-bridge `messages/20261113-0154_codex-to-claude_silver-replay-review.md`）。
- **C3b（銀 train_A を全部、26,283 列）**：scikit-learn 1.8.0 で数えると重大 6（銀なし C3a は 2）。増えた 4 列は全部「正解 quantity（kWh のエネルギー量など）→ amount」で、本体 amount → 検査役が不明 → **rho が本体の amount に戻す**、の道筋（Claude と Codex で一致）。
- **C3s（数の種類を外した銀）**：当時のコードのまま scikit-learn 1.8.0 で数えると、C3a・C3s とも採点 2,851 列・重大 4（同じ列）で、銀による増えは無い。当時の記録（2,852 列・重大 2 → 4）は版を記録していない当時の実行環境でしか出ない数（Claude が当時の commit 608e011 で確かめた）。
- 銀ラベルの抜き取り点検（Codex、75 列）：一致 68/75（90.7%）。不一致 7 列は Codex の答えを採る（数だけで金額・数量を決められない列は unknown、日付の形でも識別子は id、ジニ係数の指数は unknown、国旗の文字は address でない、など）。
- 「銀の金額ラベルが本体を『小数＝金額』に寄せた」は**因果の仮説**として残す（Codex の指摘）。

## 学習（1 回の依頼・3 本）
- **L24S**＝L24 と同じ設定 ＋ `FT_SILVER=materials/model_corpora/silver/train_A.jsonl.gz FT_SILVER_EPOCHS=1`（銀を全部、26,283 列。SHA-256 先頭 `0a06e0ffb7a28728`）。L24 との違いは「先に銀で 1 周学ぶ」だけ。種子 1〜3。
- 依頼の文：`train intfloat/multilingual-e5-base 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160 FT_KEEP=1 FT_LABELFIX=materials/pool/labelfix_v24.jsonl,materials/pool/labelfix_g24_b3.jsonl,materials/pool/labelfix_g24_sheet.jsonl,materials/pool/labelfix_g24_pool.jsonl FT_SILVER=materials/model_corpora/silver/train_A.jsonl.gz FT_SILVER_EPOCHS=1 ++ FT_SEED=2（同じ FT_LABELFIX・FT_SILVER） ++ FT_SEED=3（同じ）`（L24 の依頼と同じく、種子ごとに FT_LABELFIX・FT_SILVER を書く。実際の文は kaggle/kaggle.request）。見積り 1 本 35〜45 分 × 3。

## 比べ方（予測は 1 回。測る陣は **G3**＝まだ予測していない海外の陣。正解が確定してから）
- Codex の提案どおり、原因が混ざらないよう **銀あり／なし × rho の金額の守りあり／なし** の 4 つを並べる。rho の金額の守り：`research/silver/rho_amount_guard.py`（SHA-256 `68610f8e7fce92e26b3862c421efc93ed2b82eb414c20473090821329d4e956c`。rho が amount に戻すのは列名に金額の強い手がかりがあるときだけ）。
- **主（採否）**：L24S＋G 対 L24＋G（今の製品の形のまま）。決まり（D2・F1 と同じ 1〜4、公開元で引き直す）：1. 正しいが種子 3 本の平均で +0.5 ポイント以上 2. 重大の合計が増えない 3. ほかの誤りの増えが正しいの増えより少ない 4. 90% 区間の下限が 0 より大きい。満たさなければ「確かめられなかった」、銀は使わない（今の方針のまま）。
- 読むだけ：rho の守りあり の L24S と L24 の差、守りの有無ごとの重大の列、種類ごとの不明（数の列）。守りを製品に入れるかは別の事前記録で決める。
- 採点の環境：Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（違えば止まる）。検査役は採点のたびに同じ版で学び直す。

## 守ること
- 封印セット・blind_set*・b018・セット 3・5・7 は使わない。G3 の正解は、予測の前に確定する（2 人の独立ラベル → 裁定 → Codex の見直し）。予測を見たあとで正解・決まりを変えない。
- GitTables 1M は今回は使わない（表ごとの権利の確認が終わっていない）。
