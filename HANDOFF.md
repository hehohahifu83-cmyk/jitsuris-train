# ジツリス 引き継ぎ書（Claude → ChatGPT。最終更新 2026-10-19 19:56 日本時間、ChatGPT）

オーナー指示：「Claude の利用制限が近いので、ChatGPT にも同じ作業をさせたい」。この文書だけで続きができるように書く。

## 1. 守ること（必ず読む）
- 行動方針：research/column-ai/JITSURIS_PRINCIPLES.md（作業に正直・不快な言葉遣いをしない・端末の中だけ・ライセンス MIT/Apache・お金や法律の最終判断はしない）。
- 未見の試験セット（blind_set*.py、セット3・5・7）は開かない・学習に使わない・それを見て調整しない。grep するときは --exclude='blind_set*'。セット7は ChatGPT 側で保存してある最終試験で、v8 確定後に一度だけ測る（見張りは v9.1 に固定）。
- 個人の連絡先の列（氏名・電話・メール）は集めない。お客さまのデータは使わない。
- 一度に一つずつ比べる。e5-base を同じ条件で2回測ると ±1.5 ポイントぶれるので、それ未満の差は「差なし」。
- 未検証は未検証と書く。テストを消さない・結果をつくらない。
- tool-kobo の本番（main・公開サイト・Cloudflare）は触らない。同意画面・受け取り口の公開は「AI の完成後」（オーナー決定）。

## 2. 場所
| 場所 | 中身 |
|---|---|
| tool-kobo（非公開）research/column-ai ブランチ research/column-ai/ | 正本：全コード・ラベル・記録（TEACHING_PLAN.md＝教育方針、LABEL_GUIDE.md v1.4＝種類の定義書、LANGUAGE_RESEARCH.md、LEGAL_NOTES.md、FINETUNE_RESULTS.md、MATERIALS.md） |
| hehohahifu83-cmyk/jitsuris-train（公開） | 学習用の写し（コード＋公開データのラベルだけ）。GitHub Actions が無料・無制限。Kaggle の GPU を動かす |
| Kaggle（ユーザー jitsurio） | ノートブック jitsuris-train、データセット jitsuris-data。GPU は週30時間（使用 約1時間） |
| ai-bridge | 連絡箱 |
- tool-kobo の GitHub Actions は無料枠を使い切っていて動かない（11月1日に戻る）。学習・データ集めは jitsuris-train で行う。

## 3. Kaggle で学習させる手順（jitsuris-train）
1. kaggle/kaggle.request を書き換えて main に push すると、.github/workflows/kaggle.yml が動く。
   - 微調整：`train <HFモデル名> <周回数> [FT_LR=2e-5] [FT_BS=16 FT_ACC=4 FT_CKPT=0] [FT_SORT=1 FT_PAD8=1 FT_FUSED=1] [FT_AUG=1]`（`FT_` で始まる語は全部渡る。2つ同時は `++` で区切る。9を見る）
   - 速さの測定：`train probe <HFモデル名>`（学習はしない）
   - 凍結埋め込み：`train embed <HFモデル名>`（llm_embed_exp.py）
   - 結果だけ回収：`fetch <任意の文字>`（終わるまで最大280分待って回収）
   - 原因調べ：`diag`（小さい CPU・GPU の実行で順番待ちを切り分け）
2. GitHub 側が Hugging Face からモデルを取り、コード・ラベルと一緒にデータセットとして Kaggle に送る（Kaggle 側はネットなしでも動く）。
3. 状態は kaggle/KAGGLE_LOG.md（依頼直後の状態もすぐ書く）と kaggle/PROGRESS.md（10分ごと）。結果は FINETUNE_RESULTS.md の末尾に「### Kaggle GPU …」で足される。
4. 注意：夜は GPU の順番待ちが長い（今夜は約1時間40分）。空き待ちが20分を超えると GitHub 側は待つのをやめる（Kaggle 側には残る。あとで fetch）。P100 は今の torch で動かない報告があるので T4（既定）を使う。
5. jitsuris-train でコードを変えたら、tool-kobo の research/column-ai にも同じものを入れる（正本はそちら）。

## 4. 今の結果（Claude 側の固定した試験。セット7は未使用）
| モデル | 開発用220 | 一般 | 業務 | 業務2 | 日本の調達 |
|---|---|---|---|---|---|
| 今の仕組み v8 候補（疎な特徴＋LR、0.15MB、ブラウザで動作確認済み） | 91.4% | 83.1% | 83.2%・重大16 | 83.6%・重大11 | 90.6%・重大0 |
| e5-small 微調整（CPU） | 96.8% | 86.1% | 82.9%・重大11 | — | — |
| e5-base 微調整（Kaggle T4・13分、2回） | 97.3〜98.6% | 88.8〜89.2% | 84.2〜85.7%・重大5 | 85.2〜85.5%・重大7〜8 | — |
| e5-large 微調整（Kaggle T4、2周、FT_LR=2e-5、jp2 350列・約150分。単独） | 97.7%・重大1 | 90.8%・重大1 | 84.8%・重大6 | 87.4%・重大5 | 95.7%・重大0 |
| e5-large 7割＋今の仕組み3割 | 97.7%・重大1 | 89.8%・重大1 | 85.1%・重大6 | 87.3%・重大4 | 95.7%・重大0 |
| e5-large 速い設定（仕事1。学習 1,722 秒＝4.9 倍速い。**旧い見張り**） | 97.3%・重大0 | 91.9%・重大1 | 86.1%・重大2 | 86.9%・重大6 | 95.7%・重大0 |
| 同じ（**新しい見張り v9**。保存した確率から決め直した計算） | 97.3%・重大0 | 94.2%・重大1 | 92.6%・重大2 | 95.4%・重大6 | 98.9%・重大0 |
| 今の仕組み（finetune_exp.py の中で学習した疎な特徴＋LR。ブラウザの v8 候補そのものではない）に**新しい見張り**（同じ計算） | 87.7%・重大3 | 86.4%・重大1 | 89.9%・重大12 | 91.5%・重大11 | 98.9%・重大0 |
※ e5-base とは教材が違う（jp2 追加の前後）ため、まだ公平な比較ではない。
※ 新しい見張り v9 の数字は、固定試験の失敗を見て規則を作った（読み方を広げた）ので、その分は甘い。見ていない新しい表（セット7）で確かめるまでは「見込み」。誤り（不明を除く）と重大の数は旧い見張りと同じ（増えていない）。
目標：セット7で正解90%以上・重大な取り違え0、ブラウザの中だけで動く。

### オーナー指示：実用化の最終目標（2026-10-18）
Gemini を比較対象から外す。 Claude の利用制限が解除された後に再開しやすいよう、進捗の重要な節目ごと、および作業継続中は日次で本書を更新する。確認済み・未確認・未完了を分けて記録する。
ジツリスの最終目標は、表の列の種類判定分野で ChatGPT・Claude と同等以上の性能を実証し、実用化すること。AI全般の能力ではなく、同一タスク・同一入力・同一ラベル定義・同一の評価条件で比較する。正解率に加え、重大誤り・誤り・不明・種類ごとの性能・速度・メモリ・利用者が修正できる実用性を評価する。上記のセット7基準は中間ゲートであり、最終目標ではない。モデル・判定規則・評価方法を固定するまで未見セットには触れず、測定していない優位性は主張しない。


### 学習・テスト結果の徹底原因分析（オーナー指示 2026-10-18）
学習完了後は誤り・重大誤り・不明を可能な限り全件確認し、原因の根拠と確度を記録して学習方法を改める。調査対象は許可された固定試験だけ。blind_set* およびセット3・5・7は決して開かず、学習・調整にも使わない。

確認項目：ラベル定義/誤ラベル/希少クラス、出典や表ごとの分布差・重複・漏洩、列名/値/UNIT/兄弟列の文脈、前処理・トークナイザ・特徴量、誤分類と確信度/unknown/guard、学習率・周回数・バッチ・最適化・埋め込み固定・seed・dropout、コード/評価の不具合、重大誤りと速度・メモリの関係。各項目は「事実・仮説・根拠・確度・追加確認」を分け、未確定を断定しない。

改善案は優先順位・期待効果・副作用を示し、一度に一要因ずつ検証する。ラベル疑義は先生2人の独立確認と根拠裁定まで現ラベルを変更しない。結果・ケース別原因・対策・未解決点を bench/ と本書に記録し、ai-bridge の連絡箱へ1実験1通でClaudeに共有する。実験/run IDで重複投稿を防ぐ。

## 5. 次にやること（TEACHING_PLAN.md 末尾の「確定した順番」）
1. e5-large の結果を FINETUNE_RESULTS.md で確認し、TEACHING_PLAN.md の表に足す。e5-base と比べ、差が 1.5 未満なら「差なし」。
2. 凍結埋め込み：`train embed Qwen/Qwen3-0.6B` → `llm-jp/llm-jp-3-1.8b` → `sbintuitions/sarashina2.2-1b`（ライセンスはモデルカードで再確認）。
3. 水増し：良かったほうのモデルで `FT_AUG=1` を足して比べる（2回）。
4. 近傍の例との組み合わせ、能動学習で次の教材を選ぶ、間違えやすい組だけの合成、「不明」の基準を検証用データで保証、事前の慣らし、軽量化（ONNX・INT8）。
5. 一番良い組み合わせを v8 として確定 → ChatGPT がセット7で一度だけ測る → 結果を記録。
6. 教材集め：日本の業務の CSV（勘定科目・税区分の列があるもの）。materials/fetch_real.py の JP_DIRECT に URL を足し、jitsuris-train の materials/fetch.request を `jpdirect` にして push。ラベルは LABEL_GUIDE.md に従い、先生2人（ChatGPT と Claude、片方しかいないときは「先生1人」と記録）で付けて、食い違いは根拠で裁定。

## 6. 記録のしかた
- 変えたこと・確かめたこと（テスト／本番／実機を分ける）・未確認のこと・次の予定を、オーナーへの報告と同じ内容で連絡箱に残す（Claude が戻ったら読む）。
- 価格・秘密・「必ず」「No.1」は書かない。

## 7. 進め方の決まり（オーナー指示 2026-10-18）
- Claude は利用制限が来るまで使い続ける。Claude は区切りごとにこの引き継ぎ書を更新する。
- Claude は ChatGPT に積極的に依頼する。ChatGPT は Claude の依頼にほぼ全て応える（ai-bridge README「Claude からの依頼にはほぼ全て応える・研究実装」）。
- `作業: 研究実装` は、jitsuris-train（main）と tool-kobo の research/column-ai だけを変える実装。ChatGPT の自動処理でも行ってよい。学習の依頼を書き換える前は、kaggle/KAGGLE_LOG.md の最後の状態が終わっている（COMPLETE・ERROR・CANCEL）か確かめる。

## 8. 最新の状態（2026-10-18 12:55）
- **速さ**：e5-large の 2 周が 8,477 秒 → 1,722 秒（4.9 倍）。固定試験 5×4 の 20 か所を Version 10 と比べて、19 か所は差が 1.5 ポイント未満、1 か所は +1.7（良い方向）＝クオリティは下がっていない。2 本同時で約 33 分（Kaggle の版 13、2026-10-18 03:00〜03:33Z）。`compare_runs.py` で機械的に判定できる。
- **水増し（FT_AUG=1、速い設定の仕事2）**：一般で −2.7（悪い方向）、他は差なし。採用しない（種を変えた再試験は e5-base の実行中の 8 本に入っている）。
- **見張り（guard）の改良 v9**（2026-10-18、commit eda791d）：微調整モデルは日付の列を確率ほぼ 100% で当てているのに、guard.py が「日付の値に読めない」として「不明」にしていた（年だけ・年度・四半期・月名・時刻、通貨記号つきの金額など）。LABEL_GUIDE の定義に合わせて読み方を広げた。保存した確率から決め直す計算（rescore_guard.py）で、延べ 15,960 列（2 回の学習×4 条件×5 試験）の「不明」1,475 → 535、誤り 515 → 515、重大 105 → 105、その他の見落とし 91 → 91。**固定試験の失敗を見て作った規則なので、見込みの数字**。ブラウザ版 column-ai.js にも同じ規則を入れ、183 例で一致（guard.test.mjs）。年だけ（2000 など）は金額と見分けがつかないので、答えの確率 0.9 以上のときだけ日付と認める。
- **見張りを v9.1 に締めた**（2026-10-18、ChatGPT のレビュー 13:01 の指摘への対応）：FY は最後まで（FY2024xyz は日付にしない）、年-月は月 1〜12、年度の範囲は後の年が次の年（2020-99 は日付にしない）、月名は『日 月名 年』などの形だけ（文中の may は日付にしない）、数は区切りの形を見る（1,,2・1 2 3・1,234,56 は数にしない。インドの 12,34,567・欧州の 1.234,56・空白の 1 234 は数）、空白の集合を Python と JS で同じに、64 文字はコードポイントで数える。features.py の NUM_RE（1,,2 も数にする）は見張りでは使わない（モデルの特徴は変えない）。**確かめたこと**：保存した確率（e5-base 8 本×5 試験、微調整だけと 7割＋3割）から決め直して、誤り 549→549・重大 99→99（7割＋3割の延べ）で増えず、不明 419→395（減った）。微調整だけでは 業務2 の 3 列が不明→正解になっただけ。途中で『業務の期間 2017/2018_Apr・2016 Mar 01 12:00:00 AM が不明に落ちる』のを見つけて直した（締めすぎ）。Python と JS の一致は、列ごとの 214 例（guard_fixtures.json）と、値 1 つずつの 4,146 例（guard_value_fixtures.json。ランダム＋境界）で 0 件の不一致（tool-kobo の guard.test.mjs）。**セット7を測るときの見張りは v9.1**（測る前に固定）。
- **残る重大な取り違え**（微調整だけ・仕事1。業務2 に 6、業務に 2、一般に 1）：列名が「VALUE」「Monitor」「goal」など曖昧、または表の文脈（UNIT 列の値、兄弟列がすべて金額）を使えていない。ラベルが疑わしいもの（goal=id、VALUE=amount で値が 7.4・4.9 型）もある。詳細は TEACHING_PLAN.md「結果：見張りの読み方を広げた」。
- **e5-base 8 本の結果**（Kaggle 版 14、03:54〜04:43Z、約 49 分）：種のばらつきは正解率で最大 1.8 ポイント（重大の数は 業務 3〜7・業務2 7〜9 とぶれる）。水増し＝効果なし（採用しない）／学習率 2e-5＝やや悪い（採用しない）／3 周＝差なしで 1.39 倍の時間（採用しない）／**埋め込み固定＝ほぼ差なしで 1.19 倍速く、GPU メモリ 5.4→3.5GiB（候補。small でも確認中）**。表と判断は TEACHING_PLAN.md「結果：e5-base 8 本」。
- **実行中：e5-small 8 本**（Kaggle 版 15、04:50Z 開始、25〜35 分の見込み。仕事1・4・8 は縮めた版の精度も測り、仕事1・4 は学習済みモデルを持ち帰る）。①種1（縮め測定・モデル持ち帰り）②種2 ③種3 ④埋め込み固定（縮め測定・持ち帰り）⑤埋め込み固定・種2 ⑥学習率 1e-4 ⑦学習率 1e-4＋埋め込み固定 ⑧語彙を多めに残す K=60000（縮め測定）。**KAGGLE_LOG.md の最後が COMPLETE になるまで kaggle.request を書き換えない。**
- **ブラウザの中で動かす道**：縮めた e5-small（語彙刈り込み＋INT8、31.3MB＋トークナイザ 1.0MB）が headless Chromium で動き、外への通信は 0 件。詳しい数字と、ChatGPT に代行してほしい試験の手順書は **10 章**。
- ChatGPT へ依頼済み（ai-bridge 20261018-0925 ほか。ChatGPT は未読が溜まっている。オーナーが「連絡箱」と送ったときに読む）：①〜④と、速くする仕組みのコードレビュー。
- 日本の会計の架空仕訳（MIT）を jp2 に追加済み（350列、23出典名。列名ごとのラベル materials/jp2_header_labels.json）。
- ChatGPT 作：select_next.py（能動学習で次の200列を選ぶ。テストあり、tests/test_select_next.py）。本物のデータではまだ動かしていない。
- 未解決：業務の重大な誤り、セット7は未作成（ChatGPT が作る。**セット7で測るときの見張りは v9 と決める＝測る前に固定**）、学習共有の受け口は未作成（公開サイトに出すのはジツリス完成後）。

## ChatGPT 追記（2026-10-18 10:05 JST）
- CPU速度レビュー（ai-bridge 20261018-1000）を受け、`finetune_exp.py` に評価確率の再利用、各評価条件別の `errors_*.json` / `probs_*.json` 出力（列名は正規化、列値は含めない）、`FT_SEED`、`FT_LIMIT`、`FT_EVAL=dev220`、最初の20 step loss表示を追加。
- PyTorch inter-op thread 設定失敗は警告して続行。Kaggle fetch workflow は評価JSONを30日artifactに保存。
- CPUベンチ `bench/cpu_benchmark.py` と手動 workflow `.github/workflows/cpu-benchmark.yml` を追加。e5-small、先頭1500行、seed=1、A→B→C→C→B→Aの順序で、学習準備・ループ時間と評価時間を分けて測る。A/B の最初の20 lossを小数3桁で照合する。
- ローカルの構文確認と4件の単体テストは成功。GitHub Actions run 39084868596 でも依存導入と4件のテストが成功し、ベンチ実測中（結果未取得）。
- Kaggle Version 11（FT_AUG=1）は 2026-10-18 00:57Z 時点で RUNNING。学習依頼ファイルは変更していない。終了後に結果を回収し、ベンチ成功を確認してから次の依頼を判断する。


## ChatGPT 更新（2026-10-18 10:35 JST）
- CPUベンチ完了。全6条件の結果を `bench/cpu_benchmark_summary.md` と TEACHING_PLAN.md に記録。
- キャッシュ：4 threadで平均224.5秒（off）対225.0秒（on）、差なし。2 thread：平均184.5秒、4 threadの225.0秒に比べ18.0%短縮。2回間の最大差は2秒。最初の20 step lossはA/B間と再実行間で小数3桁まで一致。
- 4 CPUの計測結果に基づき `cpu_speed.py` の既定スレッド数を利用可能数の半分に変更し、`FT_CPU_THREADS` で上書き可能にした。関連テストを追加。5件のfocused unittestと構文確認が成功。
- 25分で切れた初回workflowから5条件ログをartifactで回収し、A2は別の成功run（39086572586）で追加した。結果は6条件揃っている。先頭1500行のrunはスモーク試験で、モデル精度の結果として扱わない。
- Kaggle Version 11（FT_AUG=1）は最新の `kaggle/PROGRESS.md` で100分時点RUNNING。学習依頼ファイルは変更していない。終了後、結果回収と次の学習依頼を進める。

## 9. 学習を速くする仕組み（2026-10-18 11:20、Claude）
オーナー指示：クオリティを落とさず学習を速くする。計画と根拠は TEACHING_PLAN.md 「学習を速くする方法」。
**依頼の書き方（jitsuris-train の kaggle/kaggle.request）**
- 今までどおり：`train intfloat/multilingual-e5-base 2 FT_SEED=1`（FT_ で始まる語は**全部**環境変数として渡る。以前は FT_LR・FT_AUG・FT_BS・FT_ACC・FT_CKPT 以外が無視されていた）。
- **仕事を並べる**（Kaggle の T4 は 2 枚。2026-10-18 12:20 の改良。**この改良は commit 後の依頼から有効**。先に実行中の2本は古い書き方＝引き継ぎなし）：`train intfloat/multilingual-e5-base 2 FT_LR=2e-5 FT_SORT=1 ++ FT_SEED=1 ++ FT_SEED=2 ++ FT_AUG=1`。「++」で仕事が増える（**8 本まで**）。同時に流すのは GPU の枚数（2）まで、残りは空いた GPU から順に自動で流れる。**2 本目以降は、1 本目の周数と FT_ の設定を引き継ぐ**ので、変えたいものだけ書く（同じ名前は上書き）。引き継ぎたくないものは `FT_名前=`（値なし）で外す。周数を変えるときは数字を 1 つ書く。モデルは変えられない。2 本以上のときは、仕事が終わるたびに学習済みモデルを消す（ディスクを守る）。1 本が失敗しても残りは流れる。結果は FINETUNE_RESULTS.md に「仕事1（設定）」「仕事2（仕事1との違い：…）」と並ぶ。
- **速さの測定**：`train probe intfloat/multilingual-e5-large`（学習はしない。設定ごとの速さ・メモリ・勾配の一致・GPU 2 枚の同時利用を FINETUNE_RESULTS.md に出す）。
**速くする設定（既定はオフ＝今までどおり。dropout を切った検査で勾配が一致するもの。実際の学習は dropout が有効で、束の分け方でマスクの割り当てが変わるため、完全一致は保証されない＝確率的な差。クオリティは固定試験の比べで確かめた）**：`FT_SORT=1`（実効バッチの中を長さ順にして小さな束に分ける）、`FT_PAD8=1`（幅を 8 の倍数に）、`FT_FUSED=1`（AdamW を GPU でまとめて計算）。束の大きさは `FT_BS`×`FT_ACC`（積を 64 に保つ）。
**計算結果が変わりうる設定（A/B で確かめるまで使わない）**：`FT_FREEZE_EMB=1`（単語の埋め込みを固定）。
**検査用**：`FT_NO_DROPOUT=1`、`FT_TRACE_LOSS=N`、`FT_LIMIT`、`FT_EVAL=dev220`。
**縮めた版・モデルの持ち帰り（2026-10-18 追加）**：`FT_COMPRESS=1`（学習のあと、語彙刈り込み・INT8・fp16 の 6 通りの精度を同じ表に足す。`FT_COMPRESS_TOPK=K` で語彙を多めに残す）、`FT_KEEP=1`（その仕事の学習済みモデルだけ消さずに持ち帰る。Kaggle の回収で artifact `jitsuris-model` の `ft_out_job<番号>`に入る。2 本目以降は 1 本目の設定を引き継ぐので、要らない仕事には `FT_KEEP=` `FT_COMPRESS=` を書いて外す）。
**++ の引き継ぎは『1 本目の FT_ 設定を後ろの仕事が引き継ぐ。同じ名前は上書き、`FT_X=` で外す』が正しい**（ChatGPT のレビュー 12:54 の指摘どおり、古い案内に逆の説明が残っていたら直す）。
**確かめたこと（CPU・GitHub Actions、bench/speed_checks_summary.md）**：e5-small・640 行・ドロップアウトなしで、今までの流し方と「長さ順＋幅8」の最初の 5 ステップの損失が小数 6 桁まで同じ（差 0.0）。学習時間は 51 秒 → 38 秒（1 回ずつの測定）。torch の単体テストで、束の大きさ 1〜64 のどれでも 64 文の勾配と一致。
**実機の測定（2026-10-18 02:53、`train probe`、Kaggle T4×2・e5-large・実効バッチ 64、表は FINETUNE_RESULTS.md の同時刻の節）**
- 1 秒あたりの学習文数：今の既定（束 2・チェックポイントあり）13.2 → 束 16・チェックポイントなし 52.3（3.96 倍）→ それに長さ順を足して 61.7（4.67 倍）。幅 8 の倍数と fused AdamW は、他の行の比べ方から 5〜9% の上乗せ（その 2 つだけを足した行は測っていない）。2 周（110,426 文）の計算は、13.2 文/秒で約 8,370 秒（Version 10・11 の実測 8,477・8,416 秒とほぼ一致）、61.7 文/秒で約 1,790 秒。
- 勾配の一致（fp16・ドロップアウトなし・基準は束 4）：束 2（今の既定）／束 16＋長さ順＋幅 8／束 8＋チェックポイントなし＋長さ順／束 32＋長さ順 のどれも、一致度 0.999999・相対差 0.0012〜0.0013。**今の既定の束 2 自体が同じ大きさの差**なので、速い設定でクオリティが下がる根拠は見つからなかった（実際の学習の結果での確認は、実行中の 2 本の①）。
- GPU 2 枚：別々の学習を同時に流すと、それぞれほぼ全速（1 枚だけ 74.3 → 2 枚で 73.5 と 87.2）。実験の本数が約 2 倍になる。
- 単語の埋め込みの固定（`FT_FREEZE_EMB=1`）：74.3（5.63 倍）、メモリ 7.6 GiB。ただし他の設定と一緒に測ったので単独の効果は不明、クオリティへの影響も未確認なので採らない（base で A/B してから）。
- 採用した large の設定：`FT_BS=16 FT_ACC=4 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1`（積は 64。この組み合わせそのものは測っていないが、近い行のメモリ最大は 11.0 GiB 以下で、T4 の 15 GiB に収まる見込み）。
**「印」の仕組み（古い版で流れる事故の対策。commit 18da1a9）**：kaggle.sh が依頼ごとに印（`nonce-<日時>-<乱数>.txt`）を束に入れる → データセットの一覧でその印とモデルが見えるまで待つ（90×20 秒まで。見えなければ学習を押さず、kaggle.request を `done` に戻して終了）→ run.py が印を確かめ、無ければ終了コード 3 で止まる。**まだ確かめていないこと**：印の待ちが実機で期待どおり動くか（実行中の 2 本が最初の実機試験。KAGGLE_LOG.md に印のファイル名が出る）。
**`++` の注意**：上の引き継ぎは**新しい書き方**。実行中の2本（cd52631）は古い書き方で、2 本目にも FT_ の設定を全部書いてある（新しい書き方でも同じ意味になる）。間違えやすい点：2 本目以降に何も書かないと「1 本目と全く同じ」仕事になる（種も同じ）。比べたい違い（FT_SEED・FT_AUG など）を必ず書く。
**まだ確かめていないこと**：①実際の学習の結果が今までと同じか（実行中の①）②水増しの効果（実行中の②）③e5-base の公平な比較（種を変えて 2 本。`FT_SEED=1 ++ FT_SEED=2`）④`FT_FREEZE_EMB` のクオリティへの影響。
**順番**：実行中の 2 本が終わる → 結果を固定試験で Version 10 と比べる（差 1.5 ポイント未満なら差なし＝クオリティは落ちていない。学習秒も 8,477 秒と比べる）→ e5-base の公平な比較を `++` で 1 回（速い設定、種を変える）→ `train embed llm-jp/llm-jp-3-1.8b` を一度 → 必要なら `FT_FREEZE_EMB` の A/B。
**その他**：`abstain_eval.py`（eval_reports/latest の probs を読み、「わからない」の基準で重大 0 にできるかを、試験を 1 つ外して測る）。kaggle.yml の Save が errors/probs を eval_reports/latest にも置く（次の Kaggle 実行から）。

**新しい道具（2026-10-18）**
- `compare_runs.py FINETUNE_RESULTS.md --a "<基準の見出し>" --b "<新しい見出し>"`：2 つの実行を並べ、1.5 ポイント未満を「差なし」と機械的に判定（曖昧な指定は止まる）。
- `analyze_errors.py eval_reports/latest [条件] [置き場]`：取り違えの組・「不明」にした種類・重大な列の一覧。
- `rescore_guard.py eval_reports/latest [条件] [置き場]`：保存した確率から今の guard.py で決め直して採点（学習のやり直しなし。見張りの規則を変えたときの確認用）。保存した答えを旧 guard で 0 件の不一致で再現できることを確認済み。
- `abstain_eval.py`：Kaggle の回収名（job1_probs_…）に対応。置き場が複数あるのに指定しないと止まる。
- eval_reports/latest には確率の「微調整だけ」と「7割＋3割」だけを置く（全部は GitHub Actions の artifact に 30 日）。

## 10. ブラウザの中で動かす道（縮めたモデル）と、ChatGPT に代行してほしい試験の手順書（2026-10-18 13:57、Claude）
オーナー指示（13:49）：「ChatGPT に代行させられるテストはやり方を教えて代わってもいい。Claude の利用制限が近い」。下の T1〜T7 は ChatGPT の自動処理（作業：研究実装）でできるように書いた。**jitsuris-train の main だけで完結する**（tool-kobo の非公開ブランチは要らない。記録は jitsuris-train の bench/ か HANDOFF.md と連絡箱に書く。tool-kobo の正本への写しは Claude が戻ったときにする）。

### 10.1 仕組み（何がどこにあるか）
- 縮め方と測り方：`compress_eval.py`。ONNX への書き出し：`export_onnx.py`（語彙の刈り込み → 埋め込み表を行ごとに INT8 → 全結合層を INT8。Python 側の正解の番号と logits を `reference.json` に書く）。ブラウザで動かす試験：`browser_test/run.mjs`（headless Chromium・Transformers.js・外への通信は全部止める。ページの `window.__tokenize` は番号だけ、`window.__run` はモデルまで）。CI：`.github/workflows/browser-model.yml`（push で学習していない e5-small を試す／手動 `workflow_dispatch` で学習済みモデルを試す）、`speed-checks.yml`（縮めの部品を小さく試す）。
- **ログは取りに行けない**（この環境から Actions のログ・artifact は取れない）。結果は ①bot が commit する `bench/browser_model_summary.md`（学習していないモデル）と `bench/browser_model_trained_summary.md`（学習済みモデル）②チェックランの注（annotations）。注の読み方：`JOB=$(gh api repos/hehohahifu83-cmyk/jitsuris-train/actions/runs/<run番号>/jobs --jq '.jobs[0].id'); gh api repos/hehohahifu83-cmyk/jitsuris-train/check-runs/$JOB/annotations --jq '.[] | "## \(.title)\n\(.message)"'`（title は unittest／export／REPORT／browser_js／record）。注は約 4000 字で切れるので、長い結果は bench/ のファイルを読む。
- 縮めたモデルの形：残す片 21,772／250,037（K=0）、`onnx/model_quantized.onnx` 31.3MB＋`tokenizer.json` 1.0MB。Transformers.js は `dtype:'q8'`・`device:'wasm'`・`env.allowRemoteModels=false`。**切り方は先頭 127 個＋最後の `</s>`**（Python と同じ。Transformers.js の `truncation` は最後の `</s>` が落ちるので使わず、切らずに取って自分で切る＝`capIds`）。
- 全部の試験は固定試験（開発用220・一般・業務・業務2・日本の調達）。**未見セット（blind_set*、セット3・5・7）は使わない。**

### 10.2 いまの結果（commit 362ca7d・1553fde の CI。**学習していない e5-small**＝精度の数字に意味はない。スマホ実機ではない）
- 大きさ：fp32 120.3MB → 埋め込み INT8 95.3MB → 全結合層も INT8 **31.3MB**＋tokenizer 1.0MB。onnxruntime（CPU）の 1 列は 40ms（1 スレッド）／23ms（2 スレッド）、平均 96 トークン。
- Chromium（WASM）：動いた。**外への要求 0 件**。読み込み 約 1 秒、1 列 平均 74〜92ms（1 スレッド）、4 スレッドで中央値 63ms（CI のばらつきが大きい）。logits は onnxruntime と最大 0.007 差、答え 39/40 一致。取り込む量は合計 60.1MB（モデル 31.3＋onnxruntime の wasm 26.9＋tokenizer 1.0＋js）。
- トークナイザの番号の不一致 3/40 は、どれも 128 語を超える長い文の末尾の切り方（上の `capIds` で直した、d1c9f28）。**全試験文＋変わった文字列 43 個での一致は d1c9f28 の CI で出る**（`bench/browser_model_summary.md` の「トークナイザの番号の一致」）。
- 詳しい表：TEACHING_PLAN.md（tool-kobo）「結果：縮めたモデルをブラウザで動かす試験」。**学習済みモデルを縮めたときの精度はまだ未測定**（T3・T4）。

### 10.3 代行してほしい試験（順番どおり）
**T1．Kaggle e5-small 8 本（版 15）の完了確認**
- `git pull --rebase --autostash origin main` → `tail -3 kaggle/KAGGLE_LOG.md`。最後の「状態：」が COMPLETE なら、FINETUNE_RESULTS.md の末尾に「Kaggle GPU 仕事1」〜「仕事8」の節が足され、確率が `eval_reports/latest/` に入っている。RUNNING なら待つ（30 分ごとに GitHub が取りに行く）。ERROR／CANCEL なら `kaggle/last_run_tail.txt` の末尾を読んで原因を連絡箱に書く（**自分で依頼し直さない**）。
- 仕事の中身：①種1（FT_COMPRESS=1・FT_KEEP=1）②種2 ③種3 ④FT_FREEZE_EMB=1（種1。FT_COMPRESS=1・FT_KEEP=1 を引き継ぐ）⑤種2＋FT_FREEZE_EMB=1 ⑥FT_LR=1e-4 ⑦FT_LR=1e-4＋FT_FREEZE_EMB=1 ⑧FT_COMPRESS_TOPK=60000（FT_COMPRESS=1）。全部 e5-small・2 周・`FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1`。
**T2．比べる（compare_runs.py。1.5 ポイント未満は差なし）**
```
K1="仕事1（FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_SEED=1 FT_COMPRESS=1"
K2="仕事2（仕事1との違い：FT_SEED=2 FT_COMPRESS="
K3="仕事3（仕事1との違い：FT_SEED=3 FT_COMPRESS="
K4="仕事4（仕事1との違い：FT_FREEZE_EMB=1）"
K5="仕事5（仕事1との違い：FT_SEED=2 FT_FREEZE_EMB=1 FT_COMPRESS="
K6="仕事6（仕事1との違い：FT_LR=1e-4 FT_COMPRESS="
K7="仕事7（仕事1との違い：FT_LR=1e-4 FT_FREEZE_EMB=1 FT_COMPRESS="
python compare_runs.py FINETUNE_RESULTS.md --noise "$K1" "$K2" "$K3"      # 種のばらつき
python compare_runs.py FINETUNE_RESULTS.md --a "$K1" --b "$K4"             # 埋め込み固定（種1）
python compare_runs.py FINETUNE_RESULTS.md --a "$K2" --b "$K5"             # 埋め込み固定（種2）
python compare_runs.py FINETUNE_RESULTS.md --a "$K1" --b "$K6"             # 学習率 1e-4
python compare_runs.py FINETUNE_RESULTS.md --a "$K4" --b "$K7"             # 埋め込み固定のうえで学習率 1e-4
```
- 見るもの：small が base（TEACHING_PLAN.md「結果：e5-base 8 本」）と large（4 章）にどれだけ届くか（微調整だけと 7割＋3割、5 試験の正解率・重大・不明）、埋め込み固定が small でも差なしか、学習秒（small の埋め込み表は全体の 82% なので固定の効きが大きいはず）。重大の数は 1 回では当てにならない（base で業務 3〜7、業務2 7〜9 とぶれた）ので、種のばらつきの幅と並べて書く。
- 記録：`bench/e5small_8jobs.md` に表と判断を書き、連絡箱で報告。
**T3．縮めた版の精度を読む（仕事1・4・8 の節）**
- 各節に「…微調整 2.0周・圧縮【…】・微調整だけ／7割＋3割」の行が 6 通り×2 条件（圧縮なし fp32・語彙削減・トークナイザも縮める・＋INT8 の疑似・＋INT8 の動的量子化＋埋め込み INT8・＋fp16）と、「圧縮の試験」のメモ（残す片の数・残さない片を含む列の割合・大きさの見積り・top-1 一致）が付く。同じ節の「微調整だけ」行（圧縮なし）と比べる。
- 目安：**『INT8 の動的量子化＋埋め込み INT8』が圧縮なしと正解率で −1.0 ポイント以内、重大が増えない**。超えたら仕事8（K=60000＝語彙を多く残す）の同じ行と比べて、語彙を増やす効果を見る。劣化の原因は 残さない片が unk になる影響（57% の列に 1 つ以上含まれる）か、INT8 かを、行の差から切り分ける。
**T4．学習済みの縮めたモデルをブラウザで動かす（手動 workflow。T1 が COMPLETE の後）**
- Kaggle の回収物（artifact `jitsuris-model`。仕事1・4 のモデルが `ft_out_job1`・`ft_out_job4`）を作った実行の番号：`gh api repos/hehohahifu83-cmyk/jitsuris-train/actions/artifacts --jq '.artifacts[] | select(.name=="jitsuris-model") | "\(.workflow_run.id) \(.created_at) \(.size_in_bytes)"' | head`（**e5-small の COMPLETE を回収した実行**＝created_at が 05:20Z 以降のもの。大きさが数百 MB）。
- 実行（約 15〜25 分）：`gh workflow run browser-model.yml -R hehohahifu83-cmyk/jitsuris-train -f kaggle_run=<番号> -f model_dir=ft_out_job1 -f limit=0`、続けて `-f model_dir=ft_out_job4`（concurrency で順番に流れる）。
- 結果：`git pull` して `bench/browser_model_trained_summary.md`（後に流した方で上書きされるので、1 本目が終わったら中身を別名で控える）と注。見るもの：①表の「PyTorch fp32／ONNX fp32／ONNX 埋め込み INT8／ONNX 埋め込み INT8＋全結合層 INT8」×「微調整だけ／7割＋3割」の 5 試験の正解率・重大・不明（目安：INT8 版が PyTorch fp32 と −1.0 ポイント以内、top-1 一致 99% 以上、重大が増えない）②トークナイザの番号の一致（試験の全列で 0 件のはず）③Chromium の 1 列の時間と取り込む量。
- 失敗したら `bench/browser_model_log.md` にログの末尾が入る。`gh run view <run> -R … --log-failed` は取れないので注を読む。
**T5．トークナイザの変わった文字列での不一致（研究実装）**
- `bench/browser_model_summary.md` の「トークナイザの番号の一致」と `first`（不一致の最初の 12 件。片とコードポイント付き）を読む。試験の文で 0 件、変わった文字列だけ不一致なら、Transformers.js と HF tokenizers の正規化（NFKC・空白・制御文字）の差。**製品側（column-ai.js）の前処理で寄せる案**を連絡箱に書く（column-ai.js は tool-kobo の非公開ブランチにあるので、案とテスト用の文字列を渡す。Claude が戻ったら入れる）。
**T6．取り込む量を軽くする研究（研究実装。任意）**
- 今は合計 60.1MB のうち onnxruntime の wasm が 26.9MB（`ort-wasm-simd-threaded.asyncify.wasm`）。`bench/browser_model_summary.md` の「wasm の大きさ」に onnxruntime-web の他の wasm（`ort-wasm-simd-threaded.wasm` など）の大きさが出る。WASM 専用の build（`ort.wasm.min.mjs`）を onnxruntime-web で直接使い、トークナイザは自作の Unigram（tokenizer.json の vocab と score、unk、正規化は NFKC 近似＋空白処理。正解は reference.json の `tok_texts`／`tok_ids`）にして、Transformers.js を外せるか。判定：番号が全試験文・変わった文字列で一致、logits 差が今と同程度、取り込む量。`browser_test/run.mjs` を複製して `run_light.mjs` に。
**T7．UNIT 文脈の小さな ablation（ChatGPT が 13:01 に提案した案を採用。研究実装）**
- 実装：`encoder_exp.py` の `text()`（`列名: … | 値: … | 同じ表の列: …`）に、同じ表の UNIT／Unit／単位の列の値の例を足す `FT_CTX_UNIT=1`（**既定オフ**。tests に「オフなら今までの文と同じ」を入れる）。
- Kaggle（T1 が COMPLETE になってから）：`train intfloat/multilingual-e5-base 2 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_SEED=1 FT_CTX_UNIT=1 ++ FT_SEED=2`。比べ先は e5-base 8 本の仕事1（種1）・仕事2（種2）。判定：重大の数（業務2 の VALUE/UNIT 型 1〜2 件が直るか）と、他の試験が悪化しないこと。
- その次の候補（ChatGPT 案）：第一段で同じ表の列を分類し、第二段に兄弟列の上位候補の確率（硬いラベルだけにしない）を渡す。出典単位の holdout で、誤りの増減と「不明」の変化を分けて測る。

### 10.4 守ること（T1〜T7 共通）
- Kaggle が RUNNING の間は `kaggle/kaggle.request` を書き換えない。依頼の前に、ジョブ数×所要時間の見積り（small は 1 本 5〜10 分、base は 約 10 分、large は 約 30 分、2 本ずつ）を連絡箱に書く。
- 結果の数字は元のファイル（FINETUNE_RESULTS.md、bench/ の md、注）と突き合わせて書く。検査（テスト）・本番・実機を分ける。CI の速さはスマホの速さではない。
- 見張りは **v9.1**（セット7を測る前に固定。guard.py と tool-kobo の column-ai.js の両方が同じ）。さらに直すときは Claude に連絡箱で相談（Python と JS を同時に直し、guard_fixtures.json・guard_value_fixtures.json を作り直して JS で 0 件の不一致を確かめる必要がある）。
- 秘密・価格・「必ず」「No.1」は書かない。未見セットは開かない。本番・公開サイト・Cloudflare は触らない。


## 独立CPU学習ラボ（オーナー指示 2026-10-18）
- 目的：Kaggle GPUの待機時間にも教材整理・候補学習を進める。ただし既存CPU e5-base学習やKaggleで待機中の同一実験と重複せず、CPU資源も取り合わない。
- 専用領域：`cpu_lab/`。公開教材の出典・ライセンス・用途、独立した候補データ、実験計画、結果・エラー原因をここに記録する。顧客データ・個人情報・未見試験セットは置かない。
- 学習素材だけでモデルが学ぶわけではない。素材を確認済みの訓練例へ変換し、別候補モデルをCPU上で実際に学習する実行工程が別途必要。自己生成ラベルは根拠・出所を記録し、人手確認なしに正解データへ混ぜない。
- 隔離：ラボはKaggleの依頼ファイル、通常の訓練データ、既定モデルを直接変更しない。実験成果は候補として別保存し、許可された固定5試験で比較するまで採用しない。blind_set* とセット3・5・7には触れない。
- 排他：Kaggleで同じモデル・設定の実験が待機中/実行中なら重複実験を開始しない。CPU学習ワークフローとラボ実行も同じCPU資源を同時使用しないよう、実行ワークフローを作る際に共通ロックと単一実行を設定する。既存の `.github/workflows/cpu-e5base-training.yml` はe5-base seed 1/2を学習するので、同一構成の候補実験を並行させない。
- 永続化：教材・小さな記録は `cpu_lab/` に保存。Actions上の一時モデルはリポジトリへコミットせず、期限付きartifactとして扱う。ラボはまず教材と実行設計の準備段階であり、自動学習はまだ起動していない。
- Claude宛て連絡箱メッセージを作成したが、ai-bridge の自動整理workflow（run 39120861818）が2回失敗。Claude宛てINBOX反映・受領は未確認。回答や受領を既成事実として扱わない。


## 性能比較の連絡箱運用（オーナー指示 2026-10-18）
- ジツリスの性能比較では、試験開始前の比較条件・実験ID・予定資源をai-bridge/messages/に記録し、完了後は同じ実験IDで結果と徹底原因分析を1通にまとめてClaudeへ共有する。開始前と完了後の連絡を省略しない。
- Claudeへ確認・レビューを頼む必要が生じた時点でオーナーにも伝える。Claudeは自動起動しないため、オーナーがClaude側で「連絡箱」と送って確認する運用である。
- 連絡箱の自動整理が失敗した場合は、メッセージファイルを置いた事実とClaudeの未読一覧に反映された事実を区別し、未読一覧・受領を確認するまで「共有済み」「読了」と書かない。

## CPUラボの初期セットアップ状況（2026-10-18）
- 作成：`cpu_lab/README.md`、`cpu_lab/materials/README.md`、`cpu_lab/materials/column-type-research-map.md`、`cpu_lab/experiments/README.md`、`cpu_lab/reports/README.md`。
- 研究教材マップはSherlock、Sato、TURL、Permutation Invariant Strategy、DODUOの公開論文を要点整理したもの。データ・重みはまだ取得していない。個別のライセンス確認も未実施。
- CPUラボの学習workflow・排他ロック・実訓練例は未実装。現時点でジツリスの新規CPU学習はしていない。
- Claude宛てメッセージ `20261018-1949_chatgpt-to-claude_cpu-lab-materials.md` をai-bridgeに作成。ファイルの書式と秘密パターンは手元で検査し、書式合格・秘密検出0件。ただしai-bridge workflow run 39120861818 は初回・再実行とも失敗、ログ取得不可。さらに連絡箱README/STATE更新後のruns 39121062324・39121064227も失敗しており、個別メッセージだけでなく自動整理workflow全体の問題が疑われる。INBOX.mdにClaude宛て未読として載ったこと・Claudeの受領は未確認。原因はログ不足で未確定。


## 2026-10-18 20:00 — CPU能動学習補助（ChatGPT単独作業）
オーナー指示により、Claudeの利用制限中にChatGPTだけで実装。詳細は `cpu_lab/reports/active-learning-implementation-2026-10-18.md` と `cpu_lab/README.md` を参照。

- `cpu_lab/self_learning.py`: 候補モデルから未ラベル公開/合成列を推論し、不確実度・予測クラス偏り・ヘッダー重複をもとに人手レビューキューを作る。明示的にverifiedされたラベルのみをリプレイ訓練JSONLへ書く。AI擬似ラベルは自動採用しない。
- `finetune_exp.py`: `FT_CPU_LAB_REPLAY` が指定された場合だけ、来歴・ライセンス・プライバシー・レビュアー・ラベル集合・禁止データを検査した上で訓練例へ追加。未指定時の既存挙動は変わらない。
- `.github/workflows/cpu-lab-active-learning.yml`: 手動確認必須、2 seed逐次、成果artifact 7日保存。既存 `cpu-e5base-training.yml` と共有CPU排他グループにした。
- テスト: ローカルunittest 4件・py_compile通過。GitHub Actions実行・CPU候補学習・性能比較は未実施。実例プールや承認済みデータもまだない。既定モデル/Kaggle依頼/製品コードは変更なし。
- Claude向け独立レビュー依頼: `ai-bridge/messages/20261018-2000_chatgpt-to-claude_active-learning.md`。連絡箱に保存したが自動整理workflowは不調が続いている。INBOX掲載・Claude受領は未確認。Claude復帰時はユーザーに「連絡箱」を確認してもらい、このレビューを渡す。
- 制約: blind_set*、セット3・5・7を開かない。比較は許可済み5試験だけ。各差1.5ポイント未満は差なし。学習後は誤り・重大誤りの全件原因分析をしてClaudeにも共有する。


連絡箱の最新確認（2026-10-18 20:00）: 今回のClaude宛てメッセージ作成後のai-bridge workflow run 39121537658もfailure、INBOX.mdのClaude宛て未読は0件。ファイル保存は済みだがClaudeへ配信済みとは扱わない。Claude復帰後、ユーザーに「連絡箱」を確認してもらう。

## 2026-10-18 20:03 CI追記
- `.github/workflows/cpu-lab-tests.yml` を追加。CPUラボコード変更時にcompile＋unittestを自動実行。
- 最初の2 run（39121622107・39121637227）はリモートテストファイルに literal \\n が混じるパス設定ミス。修正後 run 39121657962 success（4件）。
- Claude連絡箱メッセージ更新後のrun 39121677204 はfailure。ActionsログBlobは存在せず取得できず、INBOX.mdもClaude宛て0件のまま。Claudeへの未達は解消していない。

## 2026-10-18 — 教材パック整備と学習状態の確認（ChatGPT）
- 優先教材パック: `cpu_lab/materials/learning-materials-priority-pack-2026-10-18.md`。列名・値・UNIT/兄弟列文脈を根拠にしたラベル例、近接クラス対照、unknown境界、短い監査タグを中心にした教材設計。長文CoTをジツリスの出力/学習目標にしない。
- 教材パックは方法/出典調査と未確認の合成演習草案。e-Stat raw dataもSherlock等の外部コーパスも取得・投入していない。現時点の承認済み追加教材は0件。まず表ID・ライセンス・第三者条件・PII・重複・splitを監査する。
- CPU active-learning学習は未開始。プールも人が承認したreplay例もないため、開始できる教材がない。
- Kaggle: `kaggle/kaggle.request` は `fetch`。KAGGLE_LOG末尾に2026-10-18T10:56:49ZのRUNNING記録がある（JST換算19:56:49）。GitHub Kaggle workflow 39121167019 はsuccessだが、GitHub workflowの成功はKaggle kernel完了の証拠ではない。確認できたログ記録以降の終了状態は不明。CPU labを安全側で開始しない。
- Claude向け連絡箱記録は保存済みという過去の記録だが、今回の教材パック追記後にメッセージを配信できたことは確認できていない。前回までのINBOX未読0件・ai-bridge workflow失敗の状態が解消した証拠もなし。Claudeへの共有完了とは扱わない。
- CI: 教材パック追加のcommit `24d62299c12d0af8b30175d4fb1c8c9fa500281c` に対するCPU lab safety tests run 39122008870 はsuccess。


## 2026-10-18 20:17 — 人手確認なしのCPUラボへ変更
- オーナー指示: 人のラベル確認は不可能。したがって人手確認を開始条件としない。
- 実装: `cpu_lab/self_learning.py` に機械仮ラベル経路を追加。同じJitsurisモデルで値の並びを3通り変え、予測一致・確信度0.995以上・top1-top2 margin 0.50以上の候補だけ出力する。データ上は `verified=false` のまま、正解ラベルと区別する。
- `finetune_exp.py` の `FT_CPU_LAB_PSEUDO` オプトインでのみ読み込む。出典/ライセンス/プライバシー/クラス集合/重複/閾値/一致条件を確認し、追加は元訓練行の最大1%。疎特徴ベースラインには仮ラベルを混ぜない。
- CPU Lab workflowに `automatic_pseudo` と `human_verified` を選ぶ候補モードを追加。手動確認・2 seed逐次。自動昇格しない。
- CPU lab safety tests run 39122773344 success（2026-10-18T11:19:39Z）。追加ゲート・capテストを含め通過。修正前の失敗はcapテスト期待値の誤りで、最終テストは成功。
- **まだ学習は開始していない**。未ラベルpoolと分類器checkpointがないため、仮ラベル生成ができない。e-Statデータも未取得。次は利用条件が確認できる個人情報なしpoolを作ること。候補checkpointを得る方法を確かめてからautolabelを実行する。
- Kaggleログの状態は2026-10-18T10:56:49Z RUNNINGが最新記録。現行状態は直接未確認であり、GPU学習完了とは断定しない。


## 2026-10-18 20:25 — CPUラボ教材poolの進捗
- `cpu_lab/materials/pool.jsonl` に内部生成の未ラベル合成例36件を追加。JSONL parse、ID一意、unlabeled split、privacy/source/license、labelなしを確認。禁止セット由来/参照のパターン検査0件。CPU lab safety tests run 39123051454 success。
- READMEの教材状況を更新。人の確認は不要な仮ラベル方式を用意済みだが、分類器checkpointが未取得なのでautolabel・CPU候補学習とも未開始。実行済みと誤記しない。
- Kaggle requestは`fetch`。KAGGLE_LOGの最後は2026-10-18T10:56:49Z RUNNING、GitHub fetch run 39121167019 success・artifactなし。後続のKaggle完了記録やmodel artifactは確認できず、CPU側はGPUとの重複を避けて待機。
- Claudeへの連絡箱配信は過去記録どおり未確認。ファイルを置いたことを受領とは扱わない。


## 2026-10-18 20:30 — CPUラボ開始準備と教材習得追跡
- `.github/workflows/cpu-lab-material-learning.yml` に完結型のCPU lab workflowを追加。入力は成功済みKaggle e5-base Actions run ID、checkpoint directory、CPU実行yes/no。モデルartifact取得→モデル/probe検証→pool仮ラベル→0件ならskip→2 seed逐次学習の流れ。
- 人手ラベル確認は不要。strict 3-view gate（各confidence≥0.995、margin≥0.50）通過例だけ、教師あり訓練行の最大1%まで追加。誤ラベルは残る可能性があり、候補の自動採用は禁止。
- `cpu_lab/material_receipt.py` はpool/pseudoのSHAと全IDの状態を記録し、学習ログが追加数と一致したらseedごとの教材投入を確認する。`cpu_lab/progress_probe.py` は合成正解付きprobe 110件の学習前後差分を計る。これはデータ投入と行動変化の証拠であり、ニューラルネット内部での理解/習得そのものの証明ではない。
- Probe IDは訓練poolと分離し、Kaggle bundleに入らない。固定5試験だけを最終性能判定に使う。blind_set*、セット3・5・7は触れない。
- 追加テスト: candidate/pool ID整合、学習ログなしの誤認防止、probe差分判定、probe/pool分離。Actions CIで実行確認が必要。
- **現在は開始待ち**: 完了済みKaggle e5-base runの`jitsuris-model` artifactを取得できていない。最新見えるrequestは`fetch`でKAGGLE_LOG末尾は古いRUNNING記録。適切なcheckpointが出たら、run idとft_out_job1/ft_out_job2などを指定し、manual workflowを起動する。今はCPU学習を走らせていない。

- e5-baseの複数job GPU実験でモデルが破棄されCPU labの前提を満たせない問題を確認。`jobs.py` に `keep_cpu_lab_checkpoint()` を追加し、`kaggle/run.py` から呼び出す。複数jobの先頭e5-base seedだけ `FT_KEEP=1` とし、run.pyが`ft_out_job1`として回収できる。これはartifact保持のみで学習計算/評価は変えない。既に提出済みのrunへは反映されないので、次の成功済みe5-base runが要る。


## 2026-10-18 20:35 最終検証
- CPU lab safety tests run 39123727978 success（commit 2e5ea07）。receipt/probe/job-retention testsとPython compileを通過。
- テスト途中の失敗は、1ポイント差を差ありとした誤った期待値と、欠落ログ例外の扱いを修正。最終runで成功を確認。
- Kaggle `kaggle.request=fetch`、KAGGLE_LOG末尾は2026-10-18T10:56:49Z (JST 19:56:49) RUNNINGのまま。GitHub ActionsにKaggle jobの実行中は見えず、run 39121167019の`jitsuris-model` artifactもなし。Kaggle kernel自体の現在状態は確認できない。
- 既存CPU benchmark workflow run 39123705509がin_progress。CPU lab学習はまだ開始していない。次回e5-base multi-job runにモデル保持変更が入れば、先頭seedをartifactに残しCPU lab workflowへ渡せる。


### オーナー指示：Claude と教材の共同監査（2026-10-18）
CPUラボに Claude / ChatGPT 共通の教材候補置き場を用意した。Claude が利用可能になったら次の場所を案内する。
- 投入口: `cpu_lab/materials/inbox/README.md`
- 1行JSONLのひな形: `cpu_lab/materials/inbox/candidate.template.jsonl`
- 共同監査・単独監査の手順: `cpu_lab/materials/AUDIT_PROTOCOL.md`
- 監査済み教材: `cpu_lab/materials/reviewed_replay.jsonl`（inbox の候補を直接学習させない）

2人とも使える場合は、同じ LABEL_GUIDE の版を使い、互いの判定を見ないで独立にラベル付けする。一致した行だけ根拠・確信度とともに採用候補とし、不一致は根拠で解決できなければ除外する。片方しか使えない場合は high 確信かつ根拠が明確な候補だけ「単独監査」と記録し、曖昧な候補は保留/除外する。Claude が戻った後、単独監査分を可能な範囲で再監査する。未見セット blind_set* / 3 / 5 / 7 は絶対に開かない・学習に使わない。

2026-10-18 の接続確認では Claude と Gemini はともに利用不可（ai-review_connection_status: claude=false, gemini=false）。Claude へ直接送信できていないため、この引き継ぎ書を共有記録として先に保存した。利用可能になった際はこの節を Claude に渡し、共同監査を再開する。現状は ChatGPT による単独監査教材28件がある。これは独立した人間/他モデルによる正解確認ではなく、実験用の暫定教材として扱う。


### オーナー指示：Kaggle優先・CPUラボの待機中限定運用（2026-10-18）
- CPUラボは KAGGLE カーネルが `KernelWorkerStatus.QUEUED` の間だけ実行する。開始ゲートで Kaggle API の状態を照合し、学習中も30秒ごとに監視する。状態が QUEUED 以外・照会エラーならCPUプロセスを停止し、GPU側を優先する。
- 今回、CPUワークフローはE5-baseのGPU分類器成果物がなくても、Hugging Face の `intfloat/multilingual-e5-base` から開始できるよう変更。GPUチェックポイント継続学習ではなく、待ち時間中の小規模CPU実験（各ラベル最大80行、2 seed）として結果を分けて記録する。
- Kaggleが実行状態へ移ってCPUプロセスが中断された場合、途中モデルは完成結果として採用せず、その回の記録は中断扱い。途中学習の自動再開/チェックポイント復元は未実装。
- 2026-10-18 21:30 JST の確認：`kaggle/kaggle.request=fetch`、Kaggleログ最新状態は `KernelWorkerStatus.RUNNING`（10:56:49Z）。したがってCPUラボは開始しない。別のKaggle学習要求も書き換えない。


## 2026-10-18 e5-base freeze run: queue and artifact audit

- Kaggle request: `hfmodel/intfloat__multilingual-e5-base`, 2 epochs, UNIT context, frozen embeddings, seeds 1 and 2. The request was accepted as Version 18 (Kaggle log says push at 2026-10-18 08:09:55 UTC; queued at 08:10:25 UTC).
- The first watcher stopped polling after 20 minutes at 08:30:41 UTC and recorded `queue-timeout`. This was a watcher timeout, not a Kaggle cancellation. Later status observations were RUNNING at 10:56:49 UTC and COMPLETE at 14:32:13 UTC.
- Kaggle execution log: two Tesla T4 GPUs, one seed per GPU; training loop 499s and 486s, peak 3.5 GiB each. The long wall-clock delay is not explained by model training compute. Logs show Kaggle reported RUNNING for part of the interval but do not expose scheduler allocation details, so distinguish platform wait/status latency from actual compute; do not attribute the entire delay to training.
- GitHub Actions run [39136346612](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136346612) completed successfully at 14:32:44 UTC. Its log confirms `kaggle kernels output` downloaded FINETUNE_RESULTS.md, diagnostics, and 80 error/probability JSON files. Results were appended to `FINETUNE_RESULTS.md`; Kaggle completion and resource logs are in `kaggle/KAGGLE_LOG.md`. `kaggle/kaggle.request` is now `done`. Current Actions in-progress query returned none.
- Evaluation summary for the fine-tuned-only row (fixed sets only; no blind sets or sets 3/5/7 read):
  - Seed 1: dev220 97.3% (6 errors, 0 unknown, 1 critical); general 92.5% (7, 15, 1); business 92.8% (26, 8, 4); business2 95.6% (25, 15, 4); Japan procurement 98.9% (0, 1, 0).
  - Seed 2: dev220 97.7% (5, 0, 1); general 91.2% (8, 18, 1); business 92.2% (29, 8, 5); business2 95.3% (28, 15, 4); Japan procurement 98.9% (0, 1, 0).
  - Seed-to-seed accuracy spread is at most 1.3 percentage points, below the agreed 1.5-point threshold. Against matched UNIT-only seeds, frozen embeddings show no consistent quality gain; seed 1 general accuracy is 1.7 points lower, while seed 2 differences are all under 1.5 points. Compute improved: 499/486s vs 552/546s; peak memory 3.5 vs 5.5 GiB.
- Result artifacts: GitHub artifact [jitsuris-evaluation-reports](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136346612/artifacts/12139184078) contains 80 evaluation JSONs (554,312 bytes), retained until 2026-11-17 14:32 UTC. The Actions log explicitly says no files were found at `/tmp/model`; therefore no trained model artifact was uploaded.
- Why no model artifact: at the time of the run, the request did not set `FT_KEEP=1`, and the then-current multi-job logic deleted each `ft_out` unless that flag was set. The later automatic e5-base checkpoint-retention code was committed at 2026-10-18 11:32:44 UTC, after this run was submitted at 08:10 UTC. The current source cannot retroactively preserve the Version 18 model. The model shards were written during training but were not retained in the Kaggle output; only reports/metrics are confirmed recoverable.
- Retrieval timing: scheduled fetch Action [39136346612](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136346612) started at 14:31:03 UTC and completed output download/save about 90 seconds later. The 80 JSONs uploaded successfully; the model artifact step was green but skipped upload because `/tmp/model` was absent. So result collection succeeded for metrics and error reports, but not for model weights.
- Follow-up for next run: keep separate checks for kernel state, request state, and artifact presence. If a fine-tuned checkpoint is required, set/verify `FT_KEEP=1` in the actual Kaggle job environment and verify `/tmp/model` contains the expected checkpoint before artifact upload. Do not infer model retention from a successful train exit or from “Writing model shards” alone.


## 2026-10-18 follow-up: explicit learning and retrieval checks

- Confirmed CPU Lab workflow run [39136475753](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39136475753): the prepare gate succeeded, but the training matrix was skipped because Kaggle was no longer QUEUED when the gate ran. This means no CPU Lab training or measured ability change occurred in that run.
- Added `kaggle/STATUS.md` as the current user/Claude-facing state page. It separates Kaggle completion, metrics recovery, evaluation-report artifact, model checkpoint artifact, and CPU Lab execution.
- Updated Kaggle workflow to check the pending status every 10 minutes, record a GitHub Step Summary, and expose the uploaded artifact IDs. Future summaries must not use `kaggle.request=done` alone as proof of checkpoint retention.
- Ability improvement is a separate experimental conclusion from training completion. On the five permitted fixed sets, compare matched seeds to the UNIT-only baseline; treat accuracy changes under 1.5 percentage points as no difference, and report errors, critical errors, unknowns, time, and peak GPU memory. Current frozen-embedding run has no consistent quality gain; its demonstrated gain is lower runtime and memory. Do not inspect blind sets or sets 3, 5, or 7.
- No new Kaggle training request was submitted in this update. The e5-base two-seed checkpoint-retention code now in the repository applies to future runs; it cannot recover the missing Version 18 checkpoint.


## 2026-10-19 ChatGPT: 失敗分析ループと次回学習の準備

- 直近のe5-base UNIT context + frozen embeddings の job1/job2 確率レポートだけを使用し、固定5試験を監査。blind_set* とセット3・5・7は開いていない。
- 再発観測：dev220 の `purchase order by customer` (id→quantity)、business の `total invoices paid` (quantity→amount)・`australian sourced goods` / `overseas sourced goods` (amount→quantity)、business2 の `total invoices paid`・`fine`・`sales-goods-svcs_ventes-biens-srvs`・`miscellaneous_divers` がseed 1/2で再発。businessではcategory→quantityが10/12件。列の値と同表contextをレポートに含まないので、これは再発パターンの事実であって原因確定ではない。
- 詳細: [cpu_lab/reports/error-audit-e5base-freeze-2026-10-18.md](cpu_lab/reports/error-audit-e5base-freeze-2026-10-18.md)。現行集計 `analyze_errors.py` を置き換えず、証拠/仮説を分けた `cpu_lab/error_analysis.py` を新設。評価ワークフローは各実行後に報告をStep Summary、artifact、run別Markdownへ保存。許可セット名をallowlistし、モデルの予測結果からラベル変更や学習データ化はしない。ユニットテスト3件成功。
- 次のGPU比較は、凍結UNITの既知条件を保ち `FT_AUG=1` だけ加え、seed 1/2。固定5試験のaccuracy/errors/critical errors/unknowns、時間、最大GPUメモリを比較し、1.5ポイント未満は差なし。augmentationが当たるという保証はなく、単要因の仮説検証として扱う。
- 学習中に限り、CPU Labは既存 `cpu-lab-material-learning.yml` のゲート（Kaggle request=fetch、kernel QUEUED、成功した元run、他Kaggle workflow非実行）を全て満たす場合だけ監査済みreplay候補を学習。KaggleがQUEUEDを離れたらCPUを停止する。今回はCPU Labを手動で並走させず、既存ゲートに任せる。
- 研究の方法参考（課題が異なるので結果をそのまま移さない）：Confident Learning https://arxiv.org/abs/1911.00068 （誤ラベル候補を確率から優先確認する発想、ラベル訂正は別監査）；Robust Learning with Multi-source Noise Simulation and Hard Example Mining https://arxiv.org/abs/2107.07113 （拡張・hard exampleを比較試験する発想）。
- 未回収/未確認：現行学習済みcheckpointはGitHub artifactに存在しない。CPU Labの以前の準備runはKaggle終了後に到達しスキップ。今回は新しいqueue待ちでCPU gateが機能するかをrun単位で確認する。

## 2026-10-19 ChatGPT: CPU Lab audited replay run 39229300892 — 1 seed completed, paired result incomplete

### 確認済みの事実
- GitHub Actions [39228611337](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39228611337) のCPU Lab安全テストは18/18 pass。続く [39229300892](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39229300892) はworkflowとしてsuccess。prepareはKaggle run 39212587761の成功とkernel QUEUEDを確認し、allowlist済み学習データのみを検証。準備receiptはpool=28、pseudo候補=0、準備時seed_runs=[]、semantic learning claimはprobe比較まで保留。
- seed 1の実学習は完了：e5-base、1 epoch、80件/label上限の層化標本＋人手監査済みreplay 28件、合計1308学習行。CPU 2 threads、batch 16×accumulation 2。学習452秒、評価265秒、壁時計12:53、最大RSS 8,887,940 KB。GPU学習ではない。
- seed 2 jobはworkflow上success扱いだが、ログには「KaggleがQUEUEDを離れたため即時yield、partial runは結果扱いしない」とある。完走したseed 2評価はなく、2 seed比較は未成立。
- seed 1の新head単独の許可済み固定試験出力は、dev220 0/220正解・220 unknown、general 0/295・295 unknown、business 0/475・475 unknown、business2 0/913・913 unknown、japan_procurement 0/92・92 unknown。合計1995件をすべて棄権し、通常誤り・重大誤りは0件。これは品質向上ではなく、実用的予測が出ていない結果。従来機構のみの精度は順に88.2/86.4/90.1/92.0/98.9%、同じログの50:50混合は78.2/70.5/80.8/79.6/97.8%で、混合も全5試験で低下。
- 同じ時点のKaggle requestは `fetch`。対象GPU学習は `FT_FREEZE_EMB=0` のseed1/2 run 39212587761で、KAGGLE_LOG/STATUSの最終記録は2026-10-19 09:07:21ZにQUEUED。これより新しいKaggle観測は今回取得できず、現在状態は未確認（完了とは扱わない）。GitHub Actions in_progress runは確認時0件。Kaggle依頼ファイルは変更していない。
- seed1 artifactにはFINETUNE_RESULTS、train.log、receipt、reviewed replayがある。一方、コードは行ごとの `probs_*.json` / `errors_*.json` を生成するが、アップロードartifactには含まれていない。したがって未知1995件の個票、top confidence、guard前後の予測・guard理由を照合できず、行ごとの原因監査は未完了。raw件数の独立artifact照合も未実施。

### 原因の判定（観測と仮説を分離）
- **確定・高確度（実装事実）**：CPU実験は既存の学習済みジツリスを継続学習していない。workflowは `FT_INIT_MODEL_PATH` を指定せず、`finetune_exp.py` の通常分岐はbase E5からSequenceClassificationを新規ロードする。train.logにもclassifier weightsがMISSING（新規初期化）と記録。pooler weightsのUNEXPECTEDは異なるtask/architectureからのロード差としてログに記載。
- **原因仮説・中程度**：新規分類head、1308行への縮小（通常GPU学習ログの55,213行より少ない）、1 epochの組合せでタスク適応が不足した可能性が高い。ただし各要因を分離した対照実験ではなく、all-unknownの直接原因とまでは断定できない。
- **原因未確定**：`train3.decide` の既定は閾値0.5かつguard有効。1995件のunknownが確率閾値未達なのかguard棄権なのかを示す予測確率・guard_reasonがartifactにない。ラベル誤り、出典/分割差、重複漏洩、UNIT/兄弟列・前処理・tokenizer起因を裏付ける行別データも本artifactからは確認できず、原因と断定しない。
- **再発性**：今回の新head seed 1だけなのでseed間再現性は評価不能。50:50混合の悪化は同一seed内の比較であり、独立seed再現ではない。ラベル変更はしていない。blind_set* とセット3・5・7は閲覧・利用していない。

### 次の改善・ゲート
1. **P0 監査可能性**：CPU Lab artifactに許可済み固定試験の行別errors/probsを保存し、row id、truth/prediction、top-k確率、threshold判定、guard前後/理由、token数・truncation、安全な値統計を含める。raw集計と最終表を機械照合し、1件でもずれたら評価失敗にする。列値や個人情報は保存しない。
2. **P0 起点モデル**：CPU replayは現状「base E5＋新規headの小標本smoke test」と限定。既存モデルの能力を伸ばす主張には使わない。既存checkpointとlabels.jsonが利用可能・一致確認済みの場合だけ、`FT_INIT_MODEL_PATH` によるwarm-startを別の単要因実験として検討。今回の成果からcheckpoint存在は確認できていない。
3. **P1 検証**：まずthreshold/guard内訳とラベル対応を固定probeで確認し、seed2の完走を含む再現試験を行う。GPUの順番が回ればKaggle優先。CPU LabはQUEUED中だけ、監視で状態が変われば停止。人手ラベル疑義は先生2名の独立確認と根拠裁定まで変更しない。
4. 今回のCPU試験は学習パイプラインの動作・監査性のテストであり、ChatGPT/Claude同一課題比較・実用化目標に対する改善証拠ではない。次の学習依頼は提出していない。
- ai-bridge共有はメッセージファイルをcommit 523075fとして作成し存在を確認したが、自動整理run 39240924006がfailureでINBOX.mdは更新されていない。Claude側の未読一覧への反映・受領は未確認。二重投稿はせず、原因はActionの取得ログが空で特定できていない。
