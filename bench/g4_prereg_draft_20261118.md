# G4 の事前記録（下書き。Codex の点検のあとで凍結する。収集・学習・予測はまだしない）2026-11-18 Claude

元：`bench/table_reading_plan_20261116.md`（方法 T1、改訂・診断 v2）、`bench/g4_design_draft_20261115.md`（公開元・N の扱い）。

## 1. 何を決めるか
- **主：T1-256 対 L24-control-256**（同じ設定、入力の長さ 256、違いは FT_ROWCTX=1 だけ）。決まり 1〜4（表で引き直す、下の 6）。
- 読むだけ：L24（今の研究の基準、長さ 160、run 41735353926）、公開元で引き直した差、直し N（`research/fix_n/fix_n.py` SHA-256 672dd705…）を control・T1 に足した形。N は主の判定に混ぜない。
- G4 は同じカタログ（Alberta・GovData.de）の中の未使用の公開元での確かめ。新しいカタログ一般への広がりとは分けて書く。

## 2. 学習（Kaggle の無料の GPU、費用なし、1 回の依頼・6 本）
- 共通：L24 の依頼と同じ（`FT_SEED FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_POOL=1 FT_TITLE=1 FT_KEEP=1 FT_LABELFIX=<L24 の 4 ファイル>`）＋**FT_MAX_LEN=256**。
- control-256：上の共通だけ。種子 1〜3。T1-256：共通＋**FT_ROWCTX=1**（rowctx-v1、`encoder_context.py` の ROWCTX_*：2 行・9 列・値 24 文字・列名 20 文字）。種子 1〜3。
- 学習の commit の `encoder_context.py`・`encoder_exp.py`・`finetune_exp.py` の SHA と、manifest の `extra.row_context`・`max_length=256` を予測の前に照合する。学習は G4 を見ない（教材庫だけ）。

## 3. 公開元と表の集め方（値・ラベル・予測を見る前に固定）
- カタログ：Alberta（open.alberta.ca）・GovData.de（ckan.govdata.de）。hold で登録済み。
- 公開元：両カタログの組織のうち、**G1・G2・G3 で表を採った公開元（provenance の publisher、92）を除く全部**。公開元の id は `allocation.normalize_publisher_id`（「カタログ:組織名」、小文字）。別名の表は作らない（同じ組織の名前の違いは今の正規化だけに任せる）。
- 除く表：教材庫・sealed2・sealed3・F1・G1・G1x・G2・G2x・G3・G3x の資源の URL と resource_id（`S2.known_resources` と各 adopted.json）。同じデータセットの別の資源も除く（dataset の id が同じもの）。
- 候補：`materials/pool_discover.py --national --pool hold --only-national <2 ホスト>`、**語では絞らない**。1 回だけ。
- 採用：塩 `jitsuris-g4-v1` のハッシュの順。**1 公開元 3 表まで、全体 300 表まで**、1 表 10 列まで、同じ列名の組の表は 2 つまで（G3 と同じ select）。
- 取り出し：1 回。取れなかった表は、採用の段で決めた同じ公開元の次の候補（ハッシュの順）で 1 回だけ置き換える（値を見る前の adopt の段で控えを決めておく）。**結果を見て集め足さない**。目標：採点の列 400 以上。届かなければ、届かないまま測り、「確かめに要る例が足りなかった」と書く。
- 個人・連絡先の除外：今の取り出しの決まり（pipeline の除外）のまま。落とした列は文脈にも戻さない。

## 4. セットの形（凍結）
- `independent_eval/results/g4/g4.json`：G3 と同じ列の形（id・table・source・language・header・values・siblings・unit）＋
  - **`row_context`**：表 → `encoder_context.table_row_context(表の URL, セットのその表の列（セットの順）の corpus の行)` が返した文脈（headers・rows）。
  - **`row_context_none`**：文脈を作れなかった表 → 理由（`table_row_context` の理由の文字列だけ：「同じ列名が 2 つ以上」「row_index が空の列がある」「列ごとに row_index が違う」「同じ行番号の重複」「row_values と row_index の長さが違う」「列が無い」）。
  - 文脈の headers はセットのその表の列と同じ並び（`evaluate_independent.with_row_contexts` が照合する）。
- `provenance.json`：corpus（g4・g4x）の SHA、元の行番号（row_index）の SHA、row_context の SHA、表ごとの文脈の有無と理由の数、上の決まり。
- 題名：`titles.json`（G3 と同じ作り方、corpus の resource_page で adopted の題名につなぐ）。

## 5. 正解
- 先生 2 人（Claude・Codex）の独立のラベル（SHA だけを連絡）→ 突き合わせ → 裁定 → Codex の見直し。LABEL_GUIDE v2.4（営業時間は B8）。予測を見たあとで正解を変えない。

## 6. 予測と採点（1 回だけ）
- 予測：GitHub の CPU、control-256・T1-256・L24 の各 3 本（9 本）。予測の由来（セット・題名の SHA、重み・種子、row_context の版と付いた列の数）を照合（G3 と同じ照合＋row_context）。
- 採点：G3 と同じ製品の形（guard＋recheck＋verifier v2＋rho＋辞書 K＋末尾の通貨確認）。Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0。正解が unknown・S・other・person の列は数えない。
- 決まり（D2・F1 と同じ）：1. 正しいが種子 3 本の平均で +0.5 ポイント以上 2. 重大の合計が増えない 3. ほかの誤りの増えが正しいの増えより少ない 4. 90% 区間の下限が 0 より大きい（表で引き直す、1 万回、種 0）。満たせば「T1 を採る候補」、満たさなければ「確かめられなかった」。
- 必ず書くもの：変えた列の全部、重大の列、**採点の外の列への新しい言い切り（id×本）**、T1 の切り詰め（同じ行の 1・2 行目・単位列の値・列名の一覧が 256 に残る率、G4 の上で数えるだけで決まりは変えない）、種類ごとの正しい・不明。

## 7. 決めていないこと（Codex に聞く）
- 表の上限 300・1 公開元 3 表・目標 400 列の数でよいか。GovData の表は取り出せないことが多かった（G2）ので、Alberta に偏りうる。
- 学習をラベル付けの前に依頼してよいか（学習は G4 を見ないので、独立は保てる見込み）。
