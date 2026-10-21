# 最新確認 2026-10-21 17:50 JST（Claude。S6-5 採点完了＝E5-base を残す。S6-6 SETS.md 記録。S12 の不具合と S9 のレビューを連絡箱へ）

## S6 独立評価主セット：完了（使い切り）
- **S6-5 完了**：保存済み予測 6 本を非公開ラベル 3 通り（裁定後・Claude 初回・ChatGPT 初回）× Guard v9.1／v10 で手元採点。モデルの再実行なし。結果は `bench/independent_eval_independent-main-20261021-v1.md`（集計だけ）。
- **判定：E5-base を残す。** 未知見出し OK 率 E5-base 77.9%（95% 区間 68.0〜86.7）／mmBERT-small 70.2%、差 −7.7 pt（90% 区間 −11.6〜−4.2）。重大 16.0 対 16.7 件。3 条件はどれも×で、ラベル 3 通りとも同じ結論。
- Guard v9.1 と v10 は、この 6 予測 × 313 列で判定の違いが 0 件（副採点＝主採点）。
- 弱点（学習側で同じ分析をしてから教材にする。主セットの列は教材にしない）：quantity の再現率（66%、quantity を amount と答える取り違え）、正解が unknown の列への言い切り（12 列のうち平均 10 列）、札幌の列での mmBERT の落ち込み。
- **S6-6**：`independent_eval/SETS.md` に使い切りを記録した。集計の道具 `independent_report.py` と試験 `tests/test_independent_report.py`（3 件）を追加。
- S14（先生の初回ラベルとモデルの比較）の条件「S6 が済」が満たされた。

## 要対応：S12 の FT_REAL_FRAC が既定の 1.0 でも import で落ちる（学習が動かない）
- `real_train_rows_with_units` の出力の 5 番目は**単位の例**（`unit`）で、表 ID ではない。`select_real_fraction(real_rows, …)` が空の単位の行で ValueError になる。`finetune_exp.py` は `encoder_exp` を import するので、**今の main では Kaggle の学習も起動直後に落ちる**。既存の試験は `encoder_exp` を import しないため検出できない。
- 直し方（ChatGPT に依頼済み）：水増しの前の元の行（`gtr`・`btr`・`b2tr`・`jtr`、5 番目＝表 ID）に、検証の分割のあとで `select_real_fraction` を当てる。`encoder_exp` を import する試験を足す。
- 見出しの既知／未知の計算（`slice_eval`・`compare_models`）も同じ理由で今の main では動かないため、S6-5 は学習コミット `8d688f5` の作業ツリーで計算した。

---

# 最新確認 2026-10-21 16:13 JST（ChatGPT。S6-4の一回限り予測を完了。S12の実表抽出を実装・試験。新規Kaggle学習は未実施）

## S7 Guard v10 完了
- Claudeの2026-10-21 14:13裁定を反映。D5 `h28.13.1` とD2 `M月D日` はv9.1既受理形として維持し、D5のスキップを解除。
- Pythonとtool-kobo `research/column-ai` のJS parityは259 fixtures・4,309 value fixturesで不一致0。関連単体試験38件成功。
- GitHub Actions replay runs `39558051496`・`39558053746` 成功。E5-base/mmBERT-smallともA=21、B=C=D=0、回復21/5,823＝0.36ポイント。S7は完了。

## S6 独立評価主セット
- 主セットは32表・313列。事前登録はcommit `4634e229a36db9f0c9102ca67ba7580d1526461b` で予測前に固定。ラベル値は読んでいない。
- **S6-4完了**：CPU workflow [39559123410](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39559123410) が成功。事前登録済み6重みのSHA照合、各1回の推論、出力監査がすべて成功。
- 予測6ファイルと台帳6行はcommit `9b6f39e69799a4ad207f4ac4c604747bd364ca55` に保存。場所は `independent_eval/predictions/39502740378_job1.json`〜`job3.json`、`39506074807_job1.json`〜`job3.json`、`ledger.jsonl`。requestは `done independent-main-20261021-v1 (6 predictions)`。
- 6つの予測ファイルは各313行の出力監査に合格。生の列値・正解ラベルは保存されていない。台帳も項目名のみ監査し、値・正解ラベルに当たる項目なし。予測結果や個別の予測ラベルはこの引き継ぎ書に転記していない。
- **次：ClaudeがS6-5を実施**。主v9.1、副v10を保存済み予測から採点し、ラベル提供者別・出典別・言語別の集計を確認する。新規推論は行わない。採点後にS6-6 `SETS.md` を更新する。

## S12 実表量の学習曲線（準備のみ）
- `real_fraction.py` と `encoder_exp.py` に `FT_REAL_FRAC=0.25/0.5/1.0` を実装。SHA-256しきい値で表単位・決定的・入れ子の抽出を行い、合成行と `FT_VAL=1` 検証分割は固定する。選択時に見出し・値・ラベルを使わない。
- `tests/test_real_fraction.py` の5件成功、関連3ファイルの構文検査成功。事前記録は `bench/learning_curve_e5base.md`。主指標は未知見出しmacro-F1、判定規則は `DATA_COLLECTION_PROTOCOL.md` 第8章どおり。
- 6ジョブの見積りは約40〜50分。**学習は開始していない**。既存のオーナー指示「新しいKaggle学習を開始しない」を優先し、`kaggle/kaggle.request` は `done` のまま。S12の数値判定は保留。

## 守る条件
- 封印・盲検セットは開かない。主セットの生値・ラベルJSON値も開かない。
- 予測出力と台帳に生の列値・正解ラベルを保存しない。
- 新しいKaggle学習は開始しない。

---

# 前回確認 2026-10-21 13:38 JST（Guard v10 P1/P2の回帰CI成功、D2/D5裁定待ち）



## Guard v10 S7 の実装・回帰確認
- GitHub Actions run `39544878838`（commit `70a66ce86814b7be4c42418f21250e2fe6294202`）成功。Guard試験、P1/P2全規則の個別再生、E5-base/mmBERT-small再採点、学習側の単調性監査が通過。D5の仕様衝突テストはClaude裁定待ちで1件スキップ。
- 固定回帰診断の再採点：E5-base run `39506074807` と mmBERT-small run `39502740378` は各5,823件。両方とも A（不明→正解）21、B（不明→誤り）0、C（重大誤り）0、D（通過→不明）0。gate C=0・D=0・A≥5×B を通過。詳細は `bench/guard_v10_replay.md`。
- 学習側監査では、v9.1受理列2,814、新規受理列79、日付強値・日付値・数値・列判定の損失0、正規化差0。詳細は `bench/guard_train_side_20261021.md`。この監査に固定試験・主セット・封印セットは使っていない。
- JS parity は tool-kobo `research/column-ai` の commit `c2ea7997a15ec59231d2b8de8d80da75987b0f96` で確認済み。259 fixtures・4,309 value fixturesとも不一致0、PASS。
- D5の `h28.13.1` とD2の `M月D日` は v9.1 が既受理のため単調性と仕様が衝突。Claudeへの照会は連絡箱 `20261021-1259`・`20261021-1320`。今回の確認時点で返答なし。S7は仕様裁定・Claude検収待ちで未完了。`GUARD_VERSION = "v10"` の設定と独立評価manifestへの版欄追加は未実施。v10を独立評価の主経路にしない。

---

# 最新確認 2026-10-21 12:38 JST（Claude。オーナー指示で指示役に回った。改善計画・仕様書 4 本・数える道具 3 本を追加。学習・評価は未実施）

オーナー指示（2026-10-21 11:59）：今後 Claude は ChatGPT に指示する係。連絡箱の内容を分析し、どう改善するか・データをどう集めるかを指示する。**実行は ChatGPT、Claude は指示・検収・ラベルの照合と裁定・手元での採点。**
- 計画の本体：`specs/IMPROVEMENT_PLAN.md`（合格線 G1〜G6、分析、作業パッケージ A〜J、検収表）。細目は `specs/GUARD_V10_SPEC.md`（ガード v10＝STATE.md の S7）、`specs/SEALED_EVAL_PROTOCOL.md`（封印セット・PD-1・S6 の具体手順＝S6・S9・S10・S14）、`specs/DATA_COLLECTION_PROTOCOL.md`（データの集め方＝S8・S11・S12）。読む順番は計画の第 8 章。
- 分析の要点（数字の根拠は計画の第 3 章）：①見張りが正しい答えを不明にする損が約 1.3 ポイント（日付・数の規則は「捨てる正解 52、止める誤り 5」）、②重大な取り違えの 14／16 は金額↔数量で、しきい値では 0 にならない、③本物の学習データは日本語 22.7%・英国／アイルランド系が過半・稀少な種類（人名・商品・税区分・メール・電話）がほぼ合成、④固定試験は稀少な種類を測れない。
- 追加した道具（すべて単体試験つき。再現コマンドは各ファイル冒頭）：`data_inventory.py`（棚卸し→`bench/data_inventory_20261021.md`）、`guard_accounting.py`（見張りの損得表）、`guard_train_side.py`（学習側で見張りに落ちる列→`bench/guard_train_side_20261021.md`）。`evaluate_independent.py` の `score` は、ラベルが unknown の列への言い切り数（`unknown_asserted`）も manifest に出す。全体の試験 238 件が通る（15 件は GPU 等が要る既存のものを飛ばす）。
- 次の一手（実行役）：①自分のラベルを固定して合図（S6）、②ガード v10 の P1 規則を試験先行で（S7）、③`FT_REAL_FRAC` の実装と学習曲線（S12）、④封印セット #2 の公開元割り当てと発見（S9）。順番と条件は STATE.md の S6〜S14。固定試験・主セット・封印セットの行から教材やガードを作らない。LABEL_GUIDE と既存の学習データは S6 の判定まで変えない。
- 状態の四分類：実装＝上記の道具と仕様書。検査＝単体試験（新規 15 件＋既存。全体 238 件）。実接続＝なし。実績＝なし（新しい学習も独立評価もまだ）。

---

# 最新確認 2026-10-21 08:33:06 JST（ChatGPT。独立評価主セットを抽出。S6 は独立ラベル2組待ち）

## 独立評価主セットを固定・抽出
- セット ID: `independent-main-20261021-v1`。GitHub Actions run `39515319651` 成功。
- 結果: `independent_eval/results/main/independent_main.json`（schema v1）、32 表・313 列・30 データセット・4 出典・2 言語。各表は選択列の先頭5データ行のみ。
- SHA-256: セット `4b47c72d70c30982123eaccdcbd1c8f6707d8bf1db8159b3774f1a4078ff3d87`、allowlist `fe5b1216ce7cc6f831cf163f2bc812d839acece948e10e169b8a7a3706b87c5e`。候補 metadata Git blob SHA-1 `8d4689fdb3068dc6830d342ffa380d7cb6437fe1`。訓練コーパス `materials/real_corpus_jp2.jsonl` 350行（blob SHA-1 `907b6b7598a1230d68cfa25efe2fbe976014fbff`）との完全一致 URL は0件。
- 出典・利用条件・版・各リソースの取得SHA-256は `independent_eval/results/main/ATTRIBUTION.md` と `provenance.json` に記録。セットに一括ライセンスは付けない。元CSV全体は保存していない。
- 初回の抽出検査で t16 の金額列の例がプライバシーパターン検査に一致したため、その列を除外して再固定。該当値は保存・ログ出力していない。最終抽出の選択列は全件検査を通過。provenance は `labels_written=false`、`blind_sets_read=false`、`raw_source_files_written=false`。

## 次の作業
Claude と ChatGPT が `LABEL_GUIDE.md` v1.5 に従い、モデル予測を見ずに別々のラベルを作成してから照合する。ラベルは公開リポジトリへ置かず、照合前は相手のラベルを開かない。照合・必要な裁定までは予測を実行しない。固定試験・教材・`LABEL_GUIDE.md` を変更せず、blind set 3/5/7 も開かない。

---

# 最新確認 2026-10-21 07:54 JST（Claude。mmBERT-small と E5-base の最終比較〔seed 1・2・3〕が完了。固定試験の診断では E5-base が上で、mmBERT-small の優位は確認できていない。最終判定は新しい独立評価〔主セット待ち〕）

オーナー決定（ChatGPT 経由で確認済み）：土台モデルを `jhu-clsp/mmBERT-small`（MIT）に切り替えて比べる。Claude が実装と調整。E5-base の道筋・結果・設定は基準として残す。**新しいモデルの利用者への配布はオーナー承認が要る（未実施）。**

## 完了：mmBERT-small の学習率探索（Kaggle run 39435238999、commit 22144f0。4 本とも完了、依頼から約 19 分）
検証モード（学習 50,491 行、検証 889 行＝うち未知の見出し 255 行）、seed 1、2 周。結果は `bench/lr_sweep_mmbert_small.md`、元データは `eval_reports/runs/39435238999/`。

| 学習率 | 未知見出し macro-F1 | 未知見出し正解率 | 全体 macro-F1 | 全体の正解率 | 重大誤り | 誤断定 | 不明 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5e-5 | 82.6% | 82.4% | 93.3% | 92.9% | 5 | 40 | 23 |
| **1e-4** | **83.2%** | 80.0% | 93.6% | 92.1% | 3 | 48 | 22 |
| 2e-4 | 81.1% | 80.4% | 93.3% | 91.9% | 4 | 45 | 27 |
| 4e-4 | 77.9% | 75.7% | 92.1% | 90.3% | 8 | 51 | 35 |

- **選んだ学習率：1e-4**（事前に固定した規則：未知見出し macro-F1 → 1.5 ポイント以内は同点 → 重大 → 誤断定 → 小さい学習率）。最良は探索の端ではないので再探索は不要。
- 5e-5・1e-4・2e-4 の差は、検証の大きさ（未知見出し 255 行、正解率の標準誤差が約 2 ポイント）と 1 つの種子では区別できない。はっきり悪いのは 4e-4 だけ。**この数字は E5-base との優劣を示さない**（同じ検証セットで E5-base を測るのは下の探索）。
- 実機（GPU・fp16）で初めて通った：4 本とも manifest の status は completed、fp32 への切り替え 0 回、.bin の置き直しは不要（Kaggle は torch 2.11.0+cu128・transformers 5.16.1・tokenizers 0.23.1、Tesla T4 2 枚）。学習ループ 428〜438 秒、GPU メモリ最大 3.31 GiB、検証 889 行の推論 4.1〜4.2 秒（T4・まとめて処理）。

## 完了：E5-base の学習率探索（Kaggle run 39496935773、commit 47c7eac。4 本とも完了、依頼から約 26 分）
同じ検証・同じ規則。結果は `bench/lr_sweep_e5_base.md`（2cc51ca）、元データは `eval_reports/runs/39496935773/`。

| 学習率 | 未知見出し macro-F1 | 未知見出し正解率 | 全体 macro-F1 | 全体の正解率 | 重大誤り | 誤断定 | 不明 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2e-5 | 79.1% | 78.4% | 92.4% | 92.0% | 4 | 49 | 22 |
| **3e-5** | 82.3% | 79.6% | 93.1% | 92.5% | 2 | 48 | 19 |
| 5e-5 | 82.9% | 80.8% | 93.1% | 92.5% | 3 | 49 | 18 |
| 1e-4 | 82.7% | 80.4% | 92.9% | 92.4% | 4 | 48 | 20 |

- **選んだ学習率：3e-5**（最良は 5e-5 の 82.9%。3e-5・5e-5・1e-4 が同点で、重大誤りが最少の 3e-5）。版 31 までの既定は 5e-5。3e-5 と 5e-5 の差は誤差の範囲で、「3e-5 が良い」わけではない。はっきり低いのは 2e-5 だけ。最良は探索の端ではないので再探索は不要。
- 実機：4 本とも completed、学習ループ 546〜551 秒、GPU メモリ最大 5.5 GiB。
- 同じ検証での並べ方（seed 1。優劣を決める値ではない）：mmBERT(1e-4) と E5-base(3e-5) は、未知見出し macro-F1 83.2% 対 82.3%、全体 macro-F1 93.6% 対 93.1%、全体の正解率 92.1% 対 92.5%、重大 3 対 2、誤断定 48 対 48、不明 22 対 19。区別できない（同じ検証で学習率を選んだ偏りは両方に入っている）。
- 未知の見出し 255 行の外れの重なり（`error_overlap.py`、`bench/error_overlap_validation_seed1.md`）：mmBERT 51 行・E5 52 行、**両方が外したのは 39 行**（予測まで同じ 24 行）。中身は、正解 quantity→予測 category が 14 行（見出しが分類名で値が件数に見える「横持ち」の表。診療科名の列など）、正解 other の指標列が 9 行（英国の deprivation 指数の列。mmBERT は category、E5 は rate）、残り約 16 行は散らばり。**仮説（未検証）：土台モデルの差より、学習データ（横持ちの表・other の指標列）とラベル方針の影響が大きい。** 同じ表の列がまとめて外れるので 255 行は独立な件数ではない。`LABEL_GUIDE`・学習データは独立評価の前に変えない（変えるなら、検証を見てから作ったと記録に残す）。

## 完了：最終比較（種子 1・2・3。mmBERT-small=Kaggle run 39502740378〔commit f87278a、依頼から約 20 分〕、E5-base=run 39506074807〔commit 8d688f5、約 23 分〕）
同じ学習行（全 55,213 行・`FT_VAL` なし）・同じ入力文（単位列の文脈つき）・同じ守り（v9.1）・同じ評価。学習率は検証で選んだ値（mmBERT-small 1e-4、E5-base 3e-5）、`FT_KEEP=1`。**固定試験は使い切った回帰診断で、これは最終判定ではない。** 表：`bench/compare_mmbert_vs_e5base.md`（compare_models.py）。計算資源と切り詰め：`bench/resources_mmbert_vs_e5base.md`（resource_table.py）。元データ：`eval_reports/runs/39502740378/`・`39506074807/`。

| 指標（実表 1,941 行。平均 ±標準偏差〔最小〜最大〕） | mmBERT-small | E5-base |
|---|---|---|
| 正解率（見送りの正解を含む） | 92.6% ±0.3（92.2〜92.8） | 93.5% ±0.3（93.1〜93.8） |
| macro-F1 | 94.5% ±0.8（93.6〜95.1） | 94.6% ±0.2（94.4〜94.8） |
| 重大誤り（日付/金額/数量/割合/ID の取り違え） | 13.0 ±3.0（10〜16） | 5.3 ±1.5（4〜7） |
| 誤断定（誤答＋その他の誤受理） | 88.7 ±5.5（85〜95） | 68.7 ±8.1（63〜78） |
| 【未知見出し 635 行】正解率 | 82.4% ±0.7（81.6〜83.0） | 86.2% ±1.1（85.2〜87.4） |
| 【未知見出し】macro-F1 | 83.3% ±2.1（81.5〜85.6） | 86.7% ±1.9（84.9〜88.8） |
| 【未知見出し】重大誤り | 12.7 ±3.5（9〜16） | 5.0 ±1.0（4〜6） |
| 【未知見出し】誤断定 | 73.7 ±4.0（70〜78） | 50.3 ±7.5（43〜58） |
| 学習ループ／GPU メモリ最大（T4） | 464 秒／3.32 GiB | 543 秒／5.47 GiB |
| 推論 1 行あたり（T4・fp32） | 4.4〜4.8 ms | 6.0〜6.7 ms |

- **言えること**：この診断では E5-base が、未知の見出しの正解率・重大誤り・誤断定で上（3 つの種子の範囲が重ならない。macro-F1 は範囲が重なる）。全体の macro-F1 は同じ。クラス別（未知見出し）では、mmBERT は id の適合率（90.1% 対 97.7%）・other の再現率（74.6% 対 85.9%）・text の適合率（69.2% 対 97.4%。text は 18 行だけ）が低く、E5-base は text の再現率（70.4% 対 94.4%）・address の適合率（77.6% 対 84.1%）が低い。mmBERT-small は学習が約 15%、GPU メモリが約 40%、推論が約 25% 小さい／速い（T4 での値で、端末での速さではない）。
- **言えないこと**：(1) 固定試験は使い切りで、最終判定は新しい独立評価で行う。(2) 共通の学習設定（焦点損失 γ=1.5・2 周・バッチ・単位列の文脈・守り）は E5 系の実験で整えたもので、mmBERT-small で再調整したのは学習率だけ（検証で 4 点）。E5-base に有利に働いている可能性がある。(3) mmBERT-small の日本語での優位は、この設定では示せなかった（「ない」と言い切る根拠もない）。
- **mmBERT-small が低い理由の仮説（どれも未検証）**：(a) ドロップアウト 0（mmBERT の既定。E5-base は 0.1）、(b) 128 トークンでの切り詰め（学習行は 5.3% 対 5.8% で同程度だが、試験では mmBERT のほうが多い：一般 13.3% 対 7.3%、業務 12.7% 対 9.0%、業務2 5.6% 対 2.7%。切られるのは文の後ろ＝同じ表の列と単位列）、(c) 2 周では足りない（MLM だけの事前学習）、(d) 埋め込みを除いた大きさが E5-base（約 86M）の約半分（約 42M）。確かめる設定は下の「追加の実験」。
- 6 本とも completed。fp16 のまま完走（mmBERT-small で fp32 への切り替え 0 回）。持ち帰った重みは artifact `jitsuris-model`（mmBERT 1.58 GB、E5-base 2.60 GB）。**保存期限：mmBERT は 2026-11-19 22:06 UTC（11/20 07:06 JST）、E5-base は 22:38 UTC（07:38 JST）まで。**
- 定期（schedule）で動いた同じ workflow の run 39506142456 は、最後の Save（コミットと push の段）で失敗。ログが取れない（403）ので原因は未確認。学習と回収は run 39506074807 で成功しており、その結果（manifest は 3 本とも completed）を表に使った。

## 次にやること（STATE.md の常設の依頼 S6。ChatGPT の毎時の確認が進めてよい）
1. **独立評価（最終判定）**：主セットはChatGPTが固定・抽出済み（`independent-main-20261021-v1`、32表・313列、SHA-256 `4b47c72d70c30982123eaccdcbd1c8f6707d8bf1db8159b3774f1a4078ff3d87`）。個別条件・プライバシー検査・訓練URL重複0件を確認し、provenanceとATTRIBUTIONを保存。ChatGPTは連絡箱 `20261021-0833_chatgpt-to-claude_independent-main-labels.md` でClaudeへ独立ラベル付けを依頼済み。ChatGPTも別にラベルを作り、照合が済むまで予測を流さない。ラベルの内容は公開しない。
2. **独立評価の流し方**（6 つの重み。GitHub の CPU で流す。この作業場からは PyPI に届かず〔名前解決の失敗、1 回の試行〕torch を入れられない）：
   - 重みを取る：`gh run download 39502740378 -R hehohahifu83-cmyk/jitsuris-train -n jitsuris-model -D trained/mmbert`（E5-base は 39506074807 → `trained/e5base`。中に `ft_out_job1`〜`ft_out_job3`）。取った重みは `check_trained_model.py` と同じ検査（manifest の SHA-256）を `predict` が自動で通す。
   - 重みごとに `python evaluate_independent.py predict --set <主セット.json> --checkpoint trained/<mmbert|e5base>/ft_out_jobN --out out/<名前>_jobN_preds.json`（台帳 `eval_reports/independent/ledger.jsonl` が、同じ〔主セット, 重み〕の 2 回目を断る。ラベルは読まない。値は出力に書かない）。
   - ラベルを付けた人ごとに `python evaluate_independent.py score --preds out/<名前>_jobN_preds.json --labels <ラベル.json> --out-dir out/<名前>/<ラベルの人> --run jobN --seed N`。
   - 並べる：`python compare_models.py --group mmBERT-small=out/mmbert/<ラベルの人>:job1,job2,job3 --group E5-base=out/e5base/<ラベルの人>:job1,job2,job3 --out bench/independent_eval_<主セット>.md`。判定の前に、ラベルの人ごと・出典ごと・言語ごとにも見る（1 つの出典に偏っていないか）。
   - 公開リポジトリの Actions で流すなら、主セットの値は再配布が許される出典に限る（ChatGPT の審査の前提にしてほしい）。非公開の経路が要るなら別途相談。
   - 保存期限（上）までに主セットが固定されない場合は、同じ依頼を出し直して重みを取り直す（`FT_KEEP=1`。mmBERT 約 20〜25 分、E5-base 約 25〜30 分）。
3. **追加の実験**（任意。未依頼。オーナーまたは ChatGPT が指示したときだけ。いずれも、依頼の前に見積りを連絡箱の【進捗】に書く。選ぶ規則は検証だけで、固定試験は選ぶのに使わない。やるなら、独立評価の候補を固定する前＝主セットに触る前に）：
   - a. mmBERT-small の設定を変えた再挑戦（仮説 a・b）：`FT_MAX_LEN=192 FT_DROPOUT=0.1` で最終比較 1 回（3 つの種子。約 20〜25 分）。E5-base にも同じ回数の別設定（`FT_MAX_LEN=192`。約 25〜30 分）を割り当てる（探索量をそろえる）。診断の結果で選ばず、どちらの設定も独立評価の候補に入れる。見込みは小さい（効果は 1 ポイント前後と見ているが、根拠は薄い）。4 周（仮説 c）にすると時間が約 2 倍（mmBERT 約 35〜40 分、E5-base 約 45 分）。
   - b. 大きさをそろえた比較：E5-small（いまブラウザで動かしている縮めたモデル。重み 21M。学習ループは 1 本約 4 分）を同じ設定で。学習率探索 4 本（約 15 分）→ 最終比較 3 本（約 15 分）。mmBERT-small が E5-small より上なら「小さいモデルとしての価値」が言える。ブラウザに入れる大きさが決め手になるときの比較。
   - c. データ側：検証の未知見出しの外れは 39／51 が両モデル共通（`bench/error_overlap_validation_seed1.md`）。横持ちの表（見出しが分類名で値が件数。正解 quantity→予測 category）と other の指標列の教材。LABEL_GUIDE・教材を変えるなら、検証を見てから作ったと記録に残す。主セットの外れから教材を作らない（主セットは判定専用）。
4. **変えないこと**：新しいモデルの利用者への配布・公開サイトへの載せ替えはオーナー承認が要る（未実施）。ERROR／CANCEL は自分で依頼し直さない。`kaggle/kaggle.request` は現在 `done`（実行中の学習はない）。

## 道具（どれも未見セットは読まない）
`provenance.py`（学習の記録）、`val_split.py`（検証＝学習側の表の 1/8）、`slice_eval.py`（既知ペア／既知見出し・別ラベル／未知見出し）、`compare_models.py`（モデルの並べ方）、`resource_table.py`（manifest から学習時間・GPU メモリ・推論時間・切り詰め率の表）、`sweep_pick.py`（学習率の選び方）、`error_overlap.py`（2 つの仕事の外れの重なり）、`evaluate_independent.py`（保存した重みを学習の束の外の主セットに当てる。予測とラベルの採点を分け、各（主セット, 重み）の組は 1 回だけ）、`check_trained_model.py`（取ったモデルの重みの SHA-256 の照合）、`model_setup.py`（ModernBERT の読み込み・.bin の置き直し・fp16→fp32 の切り替え判断・ドロップアウトの指定）、`kaggle/hf_fetch.py`、`tests/mmbert_smoke.py`・`mmbert-smoke.yml`（CPU の試運転）。
`finetune_exp.py` の任意の設定（未指定なら今までどおり）：`FT_MAX_LEN`（最大トークン数。既定 128。manifest の `extra.max_length` と `evaluate_independent.py` が同じ値を使う）、`FT_DROPOUT`（0〜0.5。ModernBERT は attention／mlp／embedding／classifier、XLM-R は hidden／attention。`FT_NO_DROPOUT` とは併用できない）、`FT_NO_DROPOUT`。

## 確認の程度（テスト／実機／実績を分ける）
- テスト：単体試験（手元・GitHub）が成功（`resource_table.py` 5 件を含む 101 件、手元）。mmBERT-small の CPU 試運転は commit 0de5652 でも成功（run 39510163285。必須項目の NG 0 件。`FT_MAX_LEN=192`・`FT_DROPOUT=0.1` が効くこと〔設定に dropout 0.1、切り詰め 0.00%〕を CPU で確認）。強制した .bin→safetensors の置き直しは読み込み結果が元と完全一致。
- 独立評価の経路（`evaluate_independent.py`）：単体試験 9 件。本物の torch（CPU）で、学習が書いた重みを通し、学習時の評価と最上位ラベル 24/24・判断 24/24・見出し 24/24・確率の最大差 0 で一致（run 39503519924、max_length=192 の重みでも run 39510163285）。**主セットでの実際の評価は未実施**（主セットは固定済みだが、独立ラベル2組の作成・照合待ち）。6 つの重みを GitHub の CPU で流す workflow は未作成（主セットの置き場所が決まってから）。
- 実機：GPU（Tesla T4・fp16）での学習・評価は、mmBERT-small 7 本（探索 4＋最終 3）と E5-base 7 本（探索 4＋最終 3）で確認。すべて completed、mmBERT で fp32 への切り替え 0 回。`FT_MAX_LEN`・`FT_DROPOUT` の GPU 実行は未経験（CPU のみ）。ONNX／ブラウザの経路は mmBERT では未確認（CPU で ONNX 書き出しの一致のみ確認：最大差 1.6e-5。競争力が出てから）。
- 実績：固定試験の診断（上の表）では E5-base が上で、mmBERT-small の優位は示せていない。**独立評価はまだ 1 件もない**ので、最終判定はしていない。目標（未知見出しの正解率 90% 以上・重大誤り 0）は、どちらのモデルでも未達（E5-base で 86%・重大 5 件／635 行）。E5-base（版 31）の見出し別の基準は `bench/slice_eval_e5base_v31.md`：全体の 93〜94% は見出しの重なりで高く出ている。
- 版 31 の仕事 3・4（リプレイ）は、固定試験と見出し・ラベルが重なる 9 行を含む 39 行で学習していた（ChatGPT が 0c95af2 で除去・訂正済み）。その結果は比較に使わない。

## 守ること
未見セット（`blind_set*`、セット 3・5・7）は開かない・学習に使わない。固定試験の内容を教材に入れない。個人の連絡先の列は集めない。依頼は 1 回 1 モデル・8 本まで、動いている学習を置き換えない。ERROR／CANCEL は自分で依頼し直さない。未検証は未検証と書く。

## 未完了
- 新しい独立評価：主セット（32表・313列、4出典・2言語、URL重複0件）を固定・抽出済み。Claude と ChatGPT の別ラベル作成・照合、および6つの重みを流す workflow の追加が未完了。第1号の HDB 8列は予備セットのまま。
- tool-kobo `research/column-ai` への写し（51 コミット遅れ。こちらが先に進んでいる。HANDOFF.md は分かれているので、README・llm_baseline・exp15・LABEL_GUIDE を上書きしないよう注意して統合する）。
- 追加の実験（上の 3 の a〜c）は、オーナーまたは ChatGPT の指示待ち。

---

# 最新確認 2026-10-20 UTC

- Kaggle run [39374324597](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39374324597) は成功し、COMPLETE。request=done、現時点で学習workflowは進行中でない。
- Replay条件は精度向上を実証せず（5セットの平均差はすべて±1.5pp未満）。wrong 143→122、critical 18→14、unknown 97→114。詳細監査 [eval-audit-run-39374324597.md](cpu_lab/reports/eval-audit-run-39374324597.md)。
- evaluation artifactは回収済み。model artifactはbaseline job1のみでreplay checkpointは未保存。ケース別の根因は値/UNIT/token/source情報不足で未確定。次の学習は保留、依頼ファイルは触らない。
- Geminiは比較対象外。ChatGPT/Claudeとの同一課題・同一条件比較は今回行っていない。blind_set*、セット3・5・7は未閲覧・未使用。

---

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


## 11. mmBERT-small への切替の比較の記録（2026-10-21、Claude）
**決定**（オーナー確認済み・ChatGPT 経由）：土台モデルを `jhu-clsp/mmBERT-small`（MIT）に切り替えて比べる。Claude が実装と調整。最初の実験はモデルだけを変える。うまく合わない設定があれば、検証だけで等しい探索量を使い、変えた点を書く。固定試験は回帰診断に使うだけ。最終判定は学習・調整に使わない新しい独立評価だけ。3 つ以上の種子。macro-F1・クラス別の適合率と再現率・重大誤り・不明／誤断定・推論時間・GPU メモリを残す。全体の正解率だけで決めない。mmBERT の日本語での優位は未証明で、前提にしない。新しいモデルの配布はオーナー承認が要る（未実施）。

| 段 | commit／Kaggle run | 内容 | 結果の置き場 |
|---|---|---|---|
| CPU 試運転 | f7917c9／GitHub run 39433968539 | ModernBERT の読み込み・トークナイザ・学習 3 ステップ・保存→読み込みの一致 | `bench/mmbert_smoke.md` |
| mmBERT 学習率探索 | 22144f0／39435238999 | `FT_VAL=1`・seed 1・2 周・4 点（5e-5〜4e-4）→ **1e-4** | `bench/lr_sweep_mmbert_small.md` |
| E5-base 学習率探索 | 47c7eac／39496935773 | 同じ条件・4 点（2e-5〜1e-4）→ **3e-5** | `bench/lr_sweep_e5_base.md` |
| mmBERT 最終比較 | f87278a／39502740378 | 全 55,213 行・種子 1〜3・`FT_KEEP=1` | `bench/compare_mmbert_vs_e5base.md` |
| E5-base 最終比較 | 8d688f5／39506074807 | 同上 | 同上、`bench/resources_mmbert_vs_e5base.md` |

選び方は事前に固定（`sweep_pick.py`）：未知見出し macro-F1 が最大 → 1.5 ポイント以内は同点 → 重大誤りが少ない → 誤断定が少ない → 学習率が小さい。端なら範囲を広げる（どちらも端ではなかった）。
依頼文（再現用。`kaggle/kaggle.request` の書き方）：
- 最終比較 mmBERT：`train jhu-clsp/mmBERT-small 2 FT_SEED=1 FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1 FT_CTX_UNIT=1 FT_FREEZE_EMB=0 FT_FOCAL_GAMMA=1.5 FT_LR=1e-4 FT_KEEP=1 ++ FT_SEED=2 ++ FT_SEED=3`
- 最終比較 E5-base：`train intfloat/multilingual-e5-base 2 …（同じ）… FT_LR=3e-5 FT_KEEP=1 ++ FT_SEED=2 ++ FT_SEED=3`
- 探索はそれぞれ `FT_VAL=1 FT_SEED=1 …（同じ）… FT_LR=<値> ++ FT_LR=<値> ++ …`（4 本）。

**結果（要点）**：最終比較の固定試験の診断では E5-base が上（未知見出し正解率 86.2% 対 82.4%、重大誤り 5.3 対 13.0、誤断定 69 対 89。macro-F1 は同じ）。mmBERT-small は学習が約 15%、GPU メモリが約 40%、推論が約 25% 小さい／速い。検証（seed 1）では区別できなかった。未知見出しの外れの 39／51 は両モデル共通で、土台モデルよりデータ（横持ちの表・other の指標列）とラベル方針の影響が大きいという仮説（未検証）。E5-base の未知見出しの正解率（診断）86% 前後・重大 5 件は、目標の 90% 以上・重大 0 に届いていない。
**この章で確認していないこと**：独立評価での優劣、mmBERT の設定を変えたときの精度（`FT_MAX_LEN`・`FT_DROPOUT`・周回数）、大きさをそろえた E5-small との比較、mmBERT の ONNX／INT8／ブラウザの経路、日本語での優位。次の手順は先頭の「次にやること」。

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


### 2026-10-19 11:39 UTC — ai-bridge反映状態の再確認
- Kaggle: `kaggle.request=done`。KAGGLE_LOG.md の最新対象 run 39212587761 は 2026-10-19 11:05:35Z COMPLETE。最新Actions一覧に進行中のKaggle training workflowはない。run 39244116615（speed-check）はin_progress、39245751418（speed-check）はpendingで、いずれも学習runではない。
- e5-base監査を伝えるClaude宛メッセージは [ai-bridge message](https://github.com/hehohahifu83-cmyk/ai-bridge/blob/main/messages/20261019-2029_chatgpt-to-claude_e5base-unfreeze-result.md) に存在する。ただしai-bridge整理run 39244999273と39245654101はfailure。INBOX.mdはClaude宛未読0のままで、Claudeへの受領・閲覧は未確認。二重投稿はしない。
- failure理由は未確定。GitHubジョブstepsは空、ログ取得はBlobNotFoundになり、失敗箇所を確認できなかった。原因を推測で断定せず、INBOX.mdも手で編集していない。


### 2026-10-19 12:01 UTC — 圧縮評価経路の再検証
- 確定: speed-check run [39247602096](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39247602096) は success。前回Eでの失敗は `finetune_exp.py` が `compress_eval.run(..., decide, ...)` に未定義名を渡したこと。mainへ `train3.decide` のimportを追加して解消。
- 再検証: 部品試験、通しA/Bと損失一致、C/D、検査E、speed_probe が全て通過。Eでは圧縮６方式×２条件の表行が記録され、60列の縮小評価が完了。これはCPU/e5-small/短縮標本の実装確認で、GPU性能・本番精度・実用性の改善証拠ではない。
- Kaggle: `kaggle.request=done`。最新対象ログは 2026-10-19 11:05:35Z COMPLETE。現在の進行runはCPU speed-checkのみで、Kaggle trainingは起動していない。次の学習依頼も未提出。
- summary: [bench/speed_checks_summary.md](https://github.com/hehohahifu83-cmyk/jitsuris-train/blob/main/bench/speed_checks_summary.md)。

### 2026-10-19 UTC — 保存済みseed 1 checkpointの推論監査
- checkpoint-evaluation workflow run [39251294219](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/39251294219) はsuccess。run 39241962638のjob1 / seed 1モデルをCPU上で推論のみ再実行し、ft・blend70×固定試験5種の行ごと比較10/10通過。トップ1・判定・truth・正規化列名は一致し、確率最大差は0.001293（許容0.005）。一件だけ下位rankの僅差でtop3順が入れ替わったため、トップ1は厳密一致を維持し、下位rankの並びだけ確率許容差内で扱うよう比較を修正した。初回run 39250095640のfailure原因と修正内容はこの記録に含めた。
- 固定5試験の各条件2,161行、合計4,322行をschema v3で再出力し、判定理由も記録。確率・正解・正規化列名のみで、列値は保存していない。結果表のnはtruth=otherを除く採点対象件数。詳細: eval_reports/checkpoint-39241962638/CHECKPOINT_EVALUATION.md、eval_reports/checkpoint-39241962638/comparison.json。
- ft合計: wrong 64、unknown 44、重大な数値種類誤り6。blend70合計: wrong 57、unknown 54、重大5。blend70はこの固定試験ではwrongと重大が各7件・1件減る一方、unknownが10件増えたため採用判断は保留。unknown理由はother_class、日付根拠不足、閾値未達など。高確信度の誤りもあり、確信度だけでは重大誤りを防げていない。
- blend70の重大誤り5件はdev220のpurchase order by customer（id→quantity）、generalのitemfield14（date→id）、business2のfine・sales-goods-svcs_ventes-biens-srvs・miscellaneous_divers（amount→quantity）。行別artifactに値・兄弟列・出典がないため、原因やラベル誤りは未確定。次の一手はLABEL_GUIDEと公開元文脈で5件を監査し、疑義があれば2人の独立確認を得る。ラベルはまだ変更しない。
- Kaggle学習依頼は追加していない。blind setおよびセット3・5・7は閲覧・評価していない。監査一覧: eval_reports/checkpoint-39241962638/ERROR_REASON_AUDIT.md。


## ChatGPT 更新（2026-10-19、重大誤り監査とKaggle状態確認）
- 保存済みseed 1の推論評価に出た重大誤りを、出典・表文脈・ラベル定義と照合し、列値を記録せず `cpu_lab/reports/error-analysis-run-39241962638.md` に追記した。
- `purchase order by customer` はSAP公開スキーマ上のidで、評価値生成もID形式。quantityへのラベル変更は根拠なし。英国の `fine` は駐車違反金でamountが妥当。カナダの2例は金額列で、同表に金額の単位・倍率列があるが、既存のUNIT列抽出は完全一致見出し限定のため `Amt-units_Mnt-unite` を拾わないことを確認した。これが誤分類の原因かは未検証。
- `itemfield14` はGittablesの `classmark.parquet`、ラベルdateだが、列名・兄弟見出しが汎用名で、確認した5値は一般的な日付・年月・年形式でない。誤ラベルとは断定せず、独立した先生2人の確認待ち。
- 次の一要因実験に向け、`encoder_context.py` のUNIT見出し判定に `Amt-units_Mnt-unite` 型の複合見出しを追加し、合成fixtureテストを1件足した。GitHub main更新コミットはコード `37c2706`、テスト `158713c`。正規表現の4 assertionはローカルで成功。Pythonのfocused unittest全件はまだ未実行。今回のコード変更を含むKaggle学習は未実行。
- Kaggle Version 23（2026-10-19 06:56:06Z、e5-base 2周、seed 1/2、`FT_CTX_UNIT=1`）はKAGGLE_LOG.md上で11:05:35ZにCOMPLETE。仕事1/2の学習ループ566/576秒、GPU最大5.5GiB。結果はFINETUNE_RESULTS.mdに追記済み。Progressに残っていた07:16Z QUEUEDは古い状態だったため、kaggle/PROGRESS.mdを11:05Z完了へ更新した。
- 最新のseed 1/2「微調整だけ」結果：開発用220 96.8/97.7%、一般 91.2/92.9%、業務 92.2/92.0%、業務2 95.9/95.8%、日本の調達 98.9/98.9%。重大誤りは開発1/1、一般1/1、業務1/4、業務2 3/3、調達0/0（seed1/2）。数値差はseed変動と並べて解釈し、順位を断定しない。
- 次の順序：まずencoder_contextの既存Pythonテストを全件実行し、Kaggle現行ログ・requestの状態を再確認。完了済み基準に今回の見出し抽出修正だけを加えた同条件seed 1/2比較を計画する。学習依頼はまだ変更していない。blind set・セット3/5/7は未使用。

### 2026-10-19 12:42 UTC追記 — 実験投入と監視の誤判定を修正
- 先の学習投入run 39253741625はHugging Faceの準備で失敗。依頼にKaggle保存先 `hfmodel/intfloat__multilingual-e5-base` をHFモデルIDとして渡していたのが原因。Kaggle側への新規pushはなく、今回の学習は始まっていない。
- 原因を直し、正しい公開ID `intfloat/multilingual-e5-base` で同じe5-base・2周・seed 1/2・他設定固定の依頼を再投入。run 39253866587が開始し、Kaggle依存導入と監視テストは成功。12:42 UTC時点でKaggle準備／実行stepが進行中。開始・完了の確認はまだ取れておらず、結果未確定。
- 先の失敗時、直近依頼がKaggleへpushされていないのに、旧jobの `COMPLETE` を現在依頼の状態として表示する監視上の欠陥を確認。次回以降の依頼では、Kaggleログの新規push記録がない場合に以前の状態を引き継がずUNKNOWNとする修正を `kaggle.yml` と `kaggle_monitor.py` に追加し、回帰テストを追加した。main commit: `d6e3642` / `1885221` / `27310cb`。この監視修正を含むActions runはまだ実行されていない。
- `encoder_context.py` の複合金額単位見出し修正と既存監視テストを合わせ、ローカルで10件のfocused unittestが成功。YAMLのCI実行確認は未取得。


### 2026-10-19 13:33 UTC追記 — Version 24進行中
- Kaggle/PROGRESS.mdの50分観測は `KernelWorkerStatus.RUNNING`。Version 24の依頼は12:42:29ZにRUNNING、12:42:29Zに学習依頼記録。13:33Z時点でActions run 39253866587とKaggle stepは継続中。今回のFINETUNE_RESULTSは未追記で、完了・精度は未確認。
- 監視修正を含めたローカルのencoder-context＋Kaggle-monitor focused unittestは13件成功。現在走っているrunは監視修正前のworkflow revisionだが、新しいKaggle push記録がすでにあるため、今回の学習cycleは旧Version 23と区別できる。
- 次はKaggleの終端状態、2仕事分の実行ログ、FINETUNE_RESULTS追加、artifactを照合してからこの実験を判定する。

## 9. 最新状況（2026-10-19 14:04:04 UTC）
- Kaggle Version 24 は 2026-10-19 13:52:29Z に COMPLETE。GitHub Actions run 39253866587 は success、model/evaluation artifact 回収済み。
- Safari webarchive にあった学習566/576秒と集計127/85/164はVersion 23の古いNotebook出力だった。Version 24の実績と誤認しない。Version 24の実学習はseed1=582秒、seed2=563秒。KAGGLE_LOGと正式なprobability artifactで照合する。
- Version 24 artifactから再集計（2seed×固定5試験、同じ評価行をseed間で反復）: FT単独=誤り137/重大19/不明78/other見落とし33、blend50=97/13/153/17、blend70=127/16/90/30。重大誤りは誤りの内数。
- FT→blend50のペア比較: FTの誤り34件（重大7件）が不明へ、正解48件が不明へ、誤り10件が正解へ、正解3件が誤りへ移った。seed間で同一評価行を重複して数える。
- cpu_lab/error_analysis.py のフィルターがft/blend70だけでblend50を落としていたためblend50/blend60にも対応。abstain_eval.py と rescore_guard.py のblend60表示/既定条件も更新。finetune_exp.py に60:40評価条件を追加。修正後、Version 24 artifactで30 probability files/12,966行が再集計され、py_compile成功。
- kaggle/kaggle.request は同一モデル・教材・seed・学習設定のまま60:40を追加評価する依頼に更新済み。Kaggle Kernel Version 25 successfully pushed 2026-10-19T14:03:29Z、依頼直後にQUEUEDを確認 14:03:59Z。GPU割当待ちで、RUNNING/学習開始は未確認。requestはtrainのまま。二重依頼を出さない。
- 次: Version 25のQUEUEDからRUNNINGへの遷移を確認して開始時刻を記録し、Kaggle COMPLETE後に60:40結果とcase artifactを回収。固定5試験・複数seedで誤り/重大/不明/other見落としと自動適用/要確認のtradeoffを比較する。blind_set*・セット3/5/7は触らない。

### 2026-10-20 UTC — run 39374324597 paired replay evaluation and case audit

#### Confirmed
- GitHub Actions run 39374324597 succeeded; Kaggle returned COMPLETE at 2026-10-20T05:48:45Z. The latest state capture 39404684583 verified COMPLETE at 09:59:37Z. `kaggle/kaggle.request=done`; current Actions list has no queued or in-progress run. Run 39404712403 (“CPU lab audited replay”) succeeded as a workflow but its preparation/training steps were skipped; it is not another training.
- The actual training run has a separate evaluation artifact (12243449321) and model artifact (12244070400). The later capture run 39404684583 has no artifacts. Only baseline job1 used `FT_KEEP=1`, so the available model artifact is not the replay checkpoint; its weights were not downloaded or inspected.
- Four jobs were paired: baseline jobs 1/2 and replay jobs 3/4, seeds 1/2; same e5-base, 2 epochs, UNIT, FT_FOCAL_GAMMA=1.5 and other settings. Replay adds 39 rows (55,213→55,252); 9 are new ChatGPT examples, each with a single reviewer. This is a fresh E5 fine-tune with a newly initialized classifier head, not cumulative continuation of the previous Jitsuris classifier.
- Reconciled all 100 evaluation metric cells (4 jobs × 5 allowed sets × 5 conditions) using official `score_real`; all matched FINETUNE_RESULTS. Error indices matched issue rows. No blind_set*/set 3/5/7 members were read or used.
- FT two-seed means: dev220 96.82→97.05 (+0.23pp), general 91.69→91.02 (-0.67), business 91.37→91.58 (+0.21), business2 94.91→95.24 (+0.33), japan_procurement 98.91→98.37 (-0.54). Every accuracy difference is under 1.5pp. Wrong 143→122 and critical 18→14, while unknown 97→114. business2 `other_ng` increases 13→25 and `other_ok` falls 113→101. No demonstrated overall capability gain.
- FT runtime was 570/611s baseline vs 583/617s replay (mean +1.6%); all four peak GPU readings were 5.5 GiB.
- The audit enumerates 1,105 replay issue instances across FT/blend50/blend60/blend70, 2 seeds, and five allowed sets. These are repeated row-condition observations, not 1,105 unique columns. Common wrong transitions: category→quantity 92, quantity→category 37, org→account 32, category→text 31, amount→quantity 25. For FT, 38/122 wrongs had raw top-1 p≥0.90; 51 unknowns had raw top-1 equal to truth but a guard abstained. The recorded FT unknown reasons: probability_below_threshold 37, other_class 33, date_value_evidence_low 30, numeric_values_not_parseable 11, numeric_top2_too_close 3.
- On the 1,050 non-dev issue instances, joining the allowed fixed-test source rows by index and gold label matched all labels. Artifact headers are normalized; raw cell values, exact UNIT-map flags, tokenizer lengths/truncation, and stable source-row IDs are missing from saved output, so individual causes remain unconfirmed. Same-row FT issues recur in both seeds for 111 dataset/index pairs; only 4 are critical in both. This is descriptive on reused test rows, not independent generalization.
- Label conflict: a reviewed synthetic replay item labels bare `税率` as `tax_class`, while generator/rules/guideline associate bare `税率` with `rate` and `tax_class` with tax category. No label changed; two independent teachers and evidence adjudication are required.

#### Cause assessment and actions
- **Observed:** repeated category/quantity and org/account errors, many guard-driven abstentions, and high-confidence wrong predictions. **Hypotheses, not established causes:** class-boundary overlap; missing/weak UNIT and sibling context; value-shape or truncation loss; source shift; synthetic replay's low dosage. The case artifact cannot confirm which caused each individual row.
- **P0:** retain per-job artifacts with run/job/seed/data digest; the replay checkpoint was not preserved. Keep the official scorer and artifact assertions. Add stable row/source IDs, guard reason, confidence/margin, safe value-shape and UNIT-match indicators, sibling count, token length/truncation, and label/preprocess version without exporting cell values.
- **P1:** resolve the `税率` conflict only through independent review by two teachers; do not copy evaluation cases into training. Use ≥5 matched seeds and a locked new table/source test before claiming a learning gain. Do not queue a training until checkpoint/evaluation provenance is repaired.
- Gemini remains excluded. Final benchmark goal remains same-task table-column classification at parity with or better than ChatGPT and Claude; this run is not that comparison.
- Full case table, metrics, root-cause dimensions, confidence, and next checks: [eval-audit-run-39374324597.md](cpu_lab/reports/eval-audit-run-39374324597.md). Claude's existing experiment message was updated in place; no duplicate message was created.

