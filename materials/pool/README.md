# 教材庫（materials/pool/）

オーナー指示（2026-10-22）：「少しずつ教材を貯めて一気に学習させたい。少しずつチャットGPTに指示を出し教材をお前に送りお前が調整し保管しろ。目標に達したら学習を行う」。

- `batch_<陣>.jsonl`：確定した教材（1 行＝1 列。unknown・S は入れない）。学習（`FT_POOL=1`）はこのファイルを全部読む。**手で書き換えない**（`materials/pipeline.py finalize` だけが作る）。
- `adjudication_<陣>.jsonl`：Claude の裁定と抜き取りの記録（先生・モデル・裁定・理由）。
- `manifest.json`：陣ごとの台帳（列・表・公開元・種類・抜き取りの誤り・各ファイルの SHA-256）。
- `work/<陣>/`：作業の置き場（adopted → corpus・set → pred → labels_chatgpt → review → decisions）。
- 状態：`python materials/pipeline.py status --out bench/pool_status.md`

## 1 陣の流れと担当
| 段 | 担当 | すること | できるもの |
|---|---|---|---|
| 1 候補 | ChatGPT | train の公開元だけで候補一覧（メタデータだけ。`selected` か `candidates` に publisher_id・resource_url（Socrata は catalog_url）・resource_id・license・datastore_available・safe_headers・title、Socrata は `platform: "socrata"`） | `materials/s11_*_candidates_*.json` |
| 2 採用 | ChatGPT が道具を実行（規則は Claude が決め、変えてよいのは Claude だけ。2026-10-22 から） | `pipeline.py adopt --batch <陣> --candidates …`（規則：train・ライセンスの一覧・datastore・使っていない表・1 陣 1 公開元 3 表・教材庫 1 公開元 15 表・同じ見出しの組 3 表） | `work/<陣>/adopted.json` |
| 3 取り出し | ChatGPT が依頼のファイルを書く → Actions | `materials/fetch_rows.request` に `fetch materials/pool/work/<陣>/adopted.json materials/pool/work/<陣>/corpus.jsonl` | `corpus.jsonl`・`set.json` |
| 4 予測 | ChatGPT が依頼のファイルを書く → Actions | `materials/label_assist/predict.request` に `run materials/pool/work/<陣>/set.json materials/pool/work/<陣>/pred_e5base_seed1.json` | `pred_e5base_seed1.json` |
| 5 ラベル | ChatGPT | LABEL_GUIDE だけで全列（予測を見ない）。corpus と同じ順に `{table, header, label, teacher}` | `labels_chatgpt.jsonl` |
| 6 突き合わせ | Claude | `pipeline.py reconcile`：一致は自動で採用、食い違いは優先度の高い順に 500 列まで Claude、残りは捨てる。一致の 5%（最少 10）を抜き取り | `review.jsonl` |
| 7 裁定・確定 | Claude | `decisions.jsonl` を書き、`pipeline.py finalize`（抜き取りの誤りが 5% を超えたら止まる） | `batch_<陣>.jsonl`・台帳 |

1 陣の大きさは 1,000〜2,000 列が目安（Claude の裁定は 1 陣 500 列まで）。陣の ID は `b001`、`b002` … の順。

## 候補を速く集める（2026-10-22 Claude）
- `materials/pool_discover.py`（Actions `pool-discover.yml`、依頼は `materials/pool/discover.request` に `discover materials/pool/candidates_<日付>.json --bodik --socrata`）。BODIK は train の組織ごとに検索 1 回で全データセットを見て datastore のあるリソースを選ぶ。Socrata はカタログ API。年度違いの同じ表は重ねない。
- 1 回目（2026-10-22）：2,201 表・272 公開元。1 陣 1 公開元 3 表までなので、b003 に 716 表、残りは b004 以降へ（同じ候補の一覧を `adopt` にもう一度渡せば、使った表は自動で外れる）。

## 取り出せる場（2026-10-22）
- BODIK の datastore（`data.bodik.jp`）
- Socrata（SODA）：公開元の ID が `world_socrata_<ホストの . と - を _ にしたもの>` で、ホストが一致するもの。列の定義から表示名を取り、位置情報・URL・写真の列は落とす。ライセンスは公式の `licenseId` で確かめる（PUBLIC_DOMAIN・CC0_10・CC_30_BY・CC_40_BY・ODC_BY_10）
- ほかの CKAN の datastore：`materials/pool/allowed_hosts.json` の `ckan` に Claude が足したホストだけ
- 採用の道具は、題名が個人の記録になりやすい表（犯罪・逮捕・通報・選挙資金・許可・入学・職員など）を落とす。主セットの NYC（`data.cityofnewyork.us`）は main に固定

## 目標と学習
- **第 1 目標：教材庫の学習に使える列 22,000**（既存の本物 約 11,000 列と合わせて約 3 倍。W1 の伸び方から＋4〜5 ポイントの見込み）。オーナーが変えてよい（`manifest.json` の `target_columns`）。
- 目標に達するまで学習はしない（Kaggle の GPU を使わない）。達したら、Claude が学習の事前記録を書いて依頼する：検証つき（`FT_VAL=1 FT_POOL=1`、教材庫の 1/8 を「検証（教材庫）」に回す）で効果を見て、そのあと検証なしの最終の学習（`FT_POOL=1 FT_KEEP=1`）→ 封印セット #2。
- 学習の量の見込み：22,000 列 × 3 倍 ≒ 66,000 行が増え、学習の行は約 12 万行（今の約 2.2 倍）。1 本 約 20 分、3 本で約 40 分（2 GPU）。倍率は `FT_POOL_COPIES` で変えられる。

## 守ること
- 公開元は train だけ（`independent_eval/allocation.json`）。主セットの 4 出典・eval2・eval3・hold は使わない（採用の道具が止める）。
- 値は公開データだけ。個人情報の列は取り出しで落とす（`fetch_rows.py`）。
- 主セット・封印セット・固定試験の行から教材やガイドを作らない。
