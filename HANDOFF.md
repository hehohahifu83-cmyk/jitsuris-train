# ジツリス 引き継ぎ書（Claude → ChatGPT。最終更新 2026-10-18 00:05）

オーナー指示：「Claude の利用制限が近いので、ChatGPT にも同じ作業をさせたい」。この文書だけで続きができるように書く。

## 1. 守ること（必ず読む）
- 行動方針：research/column-ai/JITSURIS_PRINCIPLES.md（作業に正直・不快な言葉遣いをしない・端末の中だけ・ライセンス MIT/Apache・お金や法律の最終判断はしない）。
- 未見の試験セット（blind_set*.py、セット3・5・7）は開かない・学習に使わない・それを見て調整しない。grep するときは --exclude='blind_set*'。セット7は ChatGPT 側で保存してある最終試験で、v8 確定後に一度だけ測る。
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
※ e5-base とは教材が違う（jp2 追加の前後）ため、まだ公平な比較ではない。
目標：セット7で正解90%以上・重大な取り違え0、ブラウザの中だけで動く。

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

## 8. 最新の状態（2026-10-18 12:00）
- e5-large（2周、FT_AUG なし）：完了（2026-10-17 23:34Z）。上の表のとおり。e5-base と比べて「大きいほど良い」とは言い切れない（教材が違う）。重大な誤りは業務で 6、業務2 で 4〜5 が残る。結果は TEACHING_PLAN.md 「結果：e5-large 微調整」。
- **Version 11（`FT_AUG=1` の依頼）は無効**：Kaggle が前回（Version 10）の版のデータで流し、全数字が Version 10 と同じで「水増し」の表示もなかった（学習 8,416 秒）。水増しの結果として使わない。対策は 9 の「印」。
- 実行中：速い設定の2本（commit cd52631、02:58Z 依頼。Kaggle の版番号は kaggle/KAGGLE_LOG.md）。①`FT_LR=2e-5 FT_BS=16 FT_ACC=4 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1`（Version 10 と同じ条件で、クオリティが下がっていないかの確認）②同じ設定＋`FT_AUG=1`。見込み完了 03:35〜03:45Z（日本時間 12:35〜12:45）。進み具合は kaggle/PROGRESS.md。これが終わるまで kaggle.request を書き換えない。
- ChatGPT へ依頼済み（ai-bridge 20261018-0925）：①間違えた列の一覧（errors_*.json）②全試験列の確率の保存（probs_*.json、保留の測定用）③e5-base を今の教材で種を変えて2回（公平な比較）④`train embed llm-jp/llm-jp-3-1.8b` を一度だけ。
- Claude の次：abstain_eval.py（しきい値を下げたとき重大0にできるか・答える割合）。まずは今の仕組み（疎なLR）の確率で作って動かし、微調整の probs が届いたら当てる。
- 日本の会計の架空仕訳（MIT）を jp2 に追加済み（350列、23出典名。列名ごとのラベル materials/jp2_header_labels.json）。
- ChatGPT 作：select_next.py（能動学習で次の200列を選ぶ。テストあり、tests/test_select_next.py）。本物のデータではまだ動かしていない。
- 未解決：業務の重大な誤り、セット7は未作成（ChatGPT が作る）、学習共有の受け口は未作成（公開サイトに出すのはジツリス完成後）。


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
**速くする設定（既定はオフ＝今までどおり。計算結果は変わらないもの）**：`FT_SORT=1`（実効バッチの中を長さ順にして小さな束に分ける）、`FT_PAD8=1`（幅を 8 の倍数に）、`FT_FUSED=1`（AdamW を GPU でまとめて計算）。束の大きさは `FT_BS`×`FT_ACC`（積を 64 に保つ）。
**計算結果が変わりうる設定（A/B で確かめるまで使わない）**：`FT_FREEZE_EMB=1`（単語の埋め込みを固定）。
**検査用**：`FT_NO_DROPOUT=1`、`FT_TRACE_LOSS=N`、`FT_LIMIT`、`FT_EVAL=dev220`。
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
