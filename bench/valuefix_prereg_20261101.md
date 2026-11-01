# 事前記録：教材の £ の文字化けを直して学び直す（2026-11-01 Claude。学習・予測の前に書く）

## オーナー了承（2026-11-01）
- Claude の問い：「教材の『｣』を『£』に直して、学び直しますか？」（ChatGPT の意見：元のバイトと照合して直し、確かめてから学び直す。事前記録とオーナー承認が要る）
- オーナーの答え：「そうしろ」

## 変えること（1 つ）：V＝教材の値の直し（FT_VALUEFIX）
- 原因：`materials/fetch_rows.py` の `parse_csv` が UTF-8 → CP932 → CP1252 の順に試し、英国の CP1252 のファイルを CP932 で読んだ（`research/confirm_why/findings.md` 不具合 A。取り出しは a2e7e71 で直した）。
- 範囲：教材庫で言語が ja でなく、「｣」を含む表。43 表・263 列（値に £ がある列 58、直る文字列 952）。一覧は `materials/pool/valuefix_cp1252.jsonl`（`research/valuefix/make_list.py`）。
  - 前に書いた「114 列」は、日本語の表と兄弟の列・行の値の中の「｣」まで数えた数。日本語の表の本物のかぎかっこ（｢ナガヨ ミックン｣）は直さない。
- 直し方：文字列を CP932 に戻して元のバイトを得て、CP1252 で読み直す（`encoder_context.cp932_to_cp1252`）。戻せない文字列があれば止める。
  - 学習で `FT_VALUEFIX=materials/pool/valuefix_cp1252.jsonl` のときだけ直す。教材庫のファイルは書き換えない。付け直し（FT_LABELFIX）のあとに当てる。
  - 試験：`tests/test_value_fix.py`。手元では 31,625 行のうち 263 行を直し、英語の表に「｣」が残らないことを確かめた。
- ラベルは変えない。

## 学ぶ前の関門：元のファイルとの照合（`research/valuefix/verify_bytes.py`、手順 `valuefix-verify.yml`）
- 各表を取り直し、直した文字列を CP1252 にしたバイトが元のファイルにあるかを数える。
- 学習に進む決まり：
  - 取れた表で、照合した文字列の 95% 以上が一致する。
  - UTF-8 として読めるファイルが 0（化けの前提に合う）。
- 取れなかった表は、直し方が決まった逆の変換（バイトがそのまま戻る）なので一覧に残す。数を結果に書く。
- 決まりを満たさなければ学ばず、合わない表を調べて報告する。

## 学習（1 回の依頼・3 本。見積り：約 1.5 時間）
- L′：D2 の L と同じ設定に FT_VALUEFIX を足す。種子 1・2・3。
- 依頼：`train intfloat/multilingual-e5-base 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=3e-5 FT_POOL=1 FT_TITLE=1 FT_MAX_LEN=160 FT_KEEP=1 FT_LABELFIX=materials/pool/labelfix_v24.jsonl FT_VALUEFIX=materials/pool/valuefix_cp1252.jsonl ++ FT_SEED=2 FT_LABELFIX=materials/pool/labelfix_v24.jsonl FT_VALUEFIX=materials/pool/valuefix_cp1252.jsonl ++ FT_SEED=3 FT_LABELFIX=materials/pool/labelfix_v24.jsonl FT_VALUEFIX=materials/pool/valuefix_cp1252.jsonl`
- 学習のログに「FT_VALUEFIX=…: fixed 263 pool rows」が出ることを確かめる。

## 測り方（新しい在庫の陣 E1。決める陣・確かめる陣は使い済み）
- 在庫（b091〜）は、2 人のラベル → 裁定 → E1〜E3 に分けて封じたあとで、E1 だけを予測する。E1 の作り方と正解は、予測の前にこの記録に追記する。
- 製品の形は D1〜D3 と同じ（見張り → recheck F4・F8 → 検査役 v2 → rho 0.8 → 通貨の手がかり。手がかりは「｣」も £ とみなす版、a2e7e71）。
- 比べるもの（各 3 本）：
  - 主：**L′＋K2 対 L＋K2**（教材の値の直しの効き目）
  - 分けて：**L＋K2 対 L＋K**（辞書 v2 の効き目。K＝frozen_d3 SHA 08a22701…、K2＝frozen_v2 SHA 0e1c07f5…）
- 採る決まり：D2・D3・確かめる陣と同じ 1〜4。
  1. 正しいが +0.5 ポイント以上
  2. 重大が増えない
  3. ほかの誤りの増えが正しいの増えより少ない
  4. 表で引き直す 90% 区間の下限が 0 より大きい
- 読むだけ：英国の表（publisher が datagov_uk）の金額の列の正しい数。
- 1 回だけ測る。測ったあとに、辞書・正解・製品の形を E1 に合わせて変えない。

## 守ること
- 封印セット・blind_set*・b018 は使わない。在庫の陣は封じる前に予測しない。
- 動いている学習はない（kaggle.request は done）。1 回の依頼で 3 本（8 本まで）。

## 関門の結果（2026-11-01、学習の前。`research/valuefix/verify.md`）
- 43 表すべて取れた。照合した文字列 228 のうち 228 が、CP1252 のバイトのまま元のファイルにあった。UTF-8 として読めるファイルは 0。
- 決まりを満たしたので、上の依頼のとおり学習を依頼した。

## E1 の作り方と正解（2026-11-01、予測の前に追記）
- 在庫は 2 回の収集で 3,191 列しか集まらず、3 陣にできなかった。2 陣（E1・E2）に分けた。割り当ては公開元の単位で、ラベル・予測の前に固定した（`bench/reserve_split_20261101.json`、d179233）。
- E1：
  - 1,559 列（18 陣）。セットは `python bench/reserve_split.py make E1 materials/pool/work/e1`。
  - 採点できる列 1,215（英語 608・日本語 402・独仏 205）。
  - 決まりの最低（全体 2,500・独仏 500）は満たさない。
- 正解：
  - Claude と ChatGPT が独立に全部の列を付けた。Claude の答えは SHA を先に固定した（f3afc2b）。
  - 一致は 86.3%（2,341 / 2,713 グループ）。食い違い 372 を Claude が LABEL_GUIDE v2.3 で裁定した。
    - Claude の答え 314、ChatGPT の答え 41、別の種類 17。
    - 記録は `research/labels/reserve_20261101/adjudicate.py`・`decisions.jsonl`。
  - 各陣の `answers_final` を正解とする。
- 道具：`research/reserve_eval.py E1`（予測の前に push）。
- 予測：label-assist-predict の `d2e`（L 3 本）と `lv`（L′ 3 本）。出力は materials/pool/work/e1。
- E2 は予測しない（次の 1 回のためにとっておく）。
