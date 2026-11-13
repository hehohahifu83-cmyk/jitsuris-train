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

## 2026-11-13 追記（学習のあと、G3 の予測の前。予測・採点はまだ見ていない）
- L24S の学習は終わった：Kaggle 完了 2026-11-12T18:28Z、成果物は run **43266270727** の `jitsuris-model`（ft_out_job1〜3）。3 本とも FT_SILVER=`materials/model_corpora/silver/train_A.jsonl.gz`・FT_SILVER_EPOCHS=1・FT_LABELFIX＝L24 と同じ 4 ファイル・FT_TITLE=1・種子 1〜3、学習の commit 66bbb87（銀のファイルの SHA-256 `0a06e0ffb7a287280a3423536822aaf16f60938fe9da8d921c6e0209847b5f2d`、事前記録の先頭と一致）。学習 1 本 1,735〜1,773 秒。
  - 重みの SHA-256：job1 `4bd5489ce4d8cdbb…`、job2 `85e9e9c2a7e534c2…`、job3 `dfac0920936fa319…`。
- 採点：`research/g3/g3_eval.py`（SHA-256 `4bf552aafdb22232e0be2f7b1c6eac85e0aa916c5477ee7b34580a3c0726ce53`）。形は L+G・L24+G・L24+G+M・L24S+G・L24+G+R・L24S+G+R（R＝rho の金額の守り）。主 1＝M（表で引き直す、`bench/fixm_prereg_20261112.md`）、主 2＝銀（L24S+G 対 L24+G、公開元で引き直す）。Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0 でないと止まる。
- 予測：`.github/workflows/g3-predict.yml`（SHA-256 `7bb2089924e0ec5537064f5b6e46e04005bcbe260511e7dfe862f48d8ac1ccba`。L・L24・L24S 各 3 本、重み・設定・学習の commit の付け直し 4 ファイルと銀のファイルの SHA を照合）。題名：`independent_eval/results/g3/titles.json`（126 表、adopted の題名を corpus の resource_page で表につないだもの。SHA-256 `281e038bc3c5994b5e368416fedeb2023cb4a079300abc8c67f0d4b15aa5773c`）。
- 正解：ai-bridge `labels/g3/final.jsonl`（SHA-256 `1162b62032d580e59345f0ca44ed588d1e8d05a707fb0453d54adb380994bbeb`）。**Codex の裁定の見直しが返ってから**予測を 1 回だけ依頼する。見直しで正解が直れば、SHA を書き直したうえで予測の前にここへ追記する。

## 2026-11-13 追記 2（Codex の予測前の点検を受けた直し。予測・採点はまだ見ていない）
- Codex の点検：ai-bridge `messages/20261113-0753_codex-to-claude_g3-preflight-review.md`、再現 `research/g3/codex_review/`。G3 の裁定 118 列は支持（正解は変えない、SHA `1162b620…bbeb` のまま）。必須の直し 2 点を Claude も再現して直した。
  1. **直し M が採点の中で消えていた**：`RC.cue_types` に足しても、`eval_fixes.run` の `FX.use` が `make_cue_types(fixes)` で置き換えていた。→ M の形だけ `FX.make_cue_types` が作る関数の結果に `FM.extra_cues` を足す形に直した（finally で必ず戻す）。合成の確かめ：Funding→amount、Students・abfall_kwh→quantity が再確認まで届く。M なしの形には漏れない。例外のあとも元の関数に戻る。
  2. **予測の由来を照合していなかった**：`check_predictions` を足した。9 本それぞれのセットの SHA・set_id、重みの SHA（モデル×本、L・L24 は G2 の照合済みの記録、L24S は学習の manifest）、種子、題名の SHA、790 列の id の集合（重複・欠け・余り）を照合し、違えば止まる。偽の重み・種子 999・偽のセット・偽の題名・欠け・重複の 6 通りで止まることを確かめた。
- workflow の補強：gate で titles.json の SHA も照合。実行の commit と道具・セット・題名の SHA を `predictions_g3/run_record.txt` に残す。途中で失敗したら予測・台帳・記録を artifact `g3-predictions-partial` に残す。**再実行は、その artifact を回収し、理由を事前記録に書いてから**にする（1 回だけの予測を守る）。
- 新しい SHA-256：`research/g3/g3_eval.py` **`b8b37850f5bce4285c57916e20fb6d8635eecc31bc9546edb54f910018d092c1`**、`.github/workflows/g3-predict.yml` **`be37690399f6292d210322568f7663e627ede9b368f6ad6b6c39e2704af8ab7b`**（前の追記の SHA に代わる）。題名・正解・セットは変えていない。
- 判定の決まり・形・引き直しの単位は変えていない。G3 で M の語に当たる列は 790 列のうち 31（列名・単位だけで数えた。値・正解・予測は見ていない）。

## 2026-11-13 結果（G3 の 1 回だけの予測 run 43354388430・commit 4989d4d、採点 `research/g3/g3_eval.md`）
- 採点 555 列。L24+G 74.17%（重大 4）、L24+G+M 74.59%（4）、L24S+G 74.83%（13）、L+G 74.17%（5）。
- **主 1（M）：確かめられなかった**。正しい +0.42（決まり 1 の +0.5 に届かない）、重大 ±0、ほかの誤り −0.18、90% 区間 +0.06〜+0.90。M が変えた列は 4 種（Patients・Approved Funding・Provincial Library Operating Grant が不明→正しい、Funding Status (Effective Date) が date→不明）。決まりは変えない。M は仮にも採らない。
- **主 2（銀）：確かめられなかった**。正しい +0.66、重大 +9（決まり 2 ×）、90% 区間 −0.54〜+1.69（決まり 4 ×）。銀は使わないまま（製品は L24）。
- 読むだけ：増えた重大は「FIR/SIR/FS Rec'd（受け取った日）→ id」「Range→date」「WMU→quantity」で、rho の金額の戻しの道筋ではない（rho の守り R の有無で重大は同じ 13）。前回 C3b の原因（rho が amount に戻す）とは別の道筋で、銀は日付・識別子の境目を崩した（因果は仮説として残す）。銀は不明を減らす（18.02% 対 19.40%）が、重大の増えが上回る。
- G3 は G1・G2 より低い（金額の列 90 のうち不明 153/270＝本体が金額を言い切らない列が多い）。海外の金額の列の弱さは残る。
- 2026-11-13 18:18 JST：Codex が同じ版（Python 3.12.14・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0、main 1743cb4）で `--dry` を回し、6 形×3 本の数・判定・重大の列がすべて一致（ai-bridge `messages/20261113-1818_codex-to-claude_g3-dry-recheck.md`）。読み方に異論なし。M・銀の G3 の測りはこれで閉じる。
