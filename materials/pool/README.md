# 教材庫（materials/pool/）

オーナー指示（2026-10-22）：「少しずつ教材を貯めて一気に学習させたい。少しずつチャットGPTに指示を出し教材をお前に送りお前が調整し保管しろ。目標に達したら学習を行う」。

- `batch_<陣>.jsonl`：確定した教材（1 行＝1 列。unknown・S は入れない）。学習（`FT_POOL=1`）はこのファイルを全部読む。**手で書き換えない**（`materials/pipeline.py finalize` だけが作る）。
- `adjudication_<陣>.jsonl`：Claude の裁定と抜き取りの記録（先生・モデル・裁定・理由）。
- `manifest.json`：陣ごとの台帳（列・表・公開元・種類・抜き取りの誤り・各ファイルの SHA-256）。
- `work/<陣>/`：作業の置き場（adopted → corpus・set → pred → labels_chatgpt → review → decisions）。
- 状態：`python materials/pipeline.py status --out bench/pool_status.md`

## 1 陣の流れと担当（2026-10-24 オーナー指示：ChatGPT はラベル付けだけ。ほかは Claude。結果の確認はオーナーが声をかけたとき）
| 段 | 担当 | すること | できるもの |
|---|---|---|---|
| 1 候補 | Claude | train の公開元だけで候補一覧（メタデータだけ。`selected` か `candidates` に publisher_id・resource_url（Socrata は catalog_url）・resource_id・license・datastore_available・safe_headers・title、Socrata は `platform: "socrata"`） | `materials/s11_*_candidates_*.json` |
| 2 採用 | Claude | `pipeline.py adopt --batch <陣> --candidates …`（規則：train・ライセンスの一覧・datastore・使っていない表・1 陣 1 公開元 3 表・教材庫 1 公開元 15 表・同じ見出しの組 3 表） | `work/<陣>/adopted.json` |
| 3 取り出し | Claude が依頼のファイルを書く → Actions | `materials/fetch_rows.request` に `fetch materials/pool/work/<陣>/adopted.json materials/pool/work/<陣>/corpus.jsonl` | `corpus.jsonl`・`set.json` |
| 4 予測 | Claude が依頼のファイルを書く → Actions | `materials/label_assist/predict.request` に `run materials/pool/work/<陣>/set.json materials/pool/work/<陣>/pred_e5base_seed1.json` | `pred_e5base_seed1.json` |
| 5 ラベル | ChatGPT | LABEL_GUIDE だけで全列（予測を見ない）。corpus と同じ順に `{table, header, label, teacher}` | `labels_chatgpt.jsonl` |
| 6 突き合わせ | Claude | `pipeline.py reconcile`：一致は自動で採用、食い違いは優先度の高い順に 500 列まで Claude、残りは捨てる。一致の 5%（最少 10）を抜き取り | `review.jsonl` |
| 7 裁定・確定 | Claude | `decisions.jsonl` を書き、`pipeline.py finalize`（抜き取りの誤りが 5% を超えたら止まる） | `batch_<陣>.jsonl`・台帳 |

1 陣の大きさは 1,000〜2,000 列が目安（Claude の裁定は 1 陣 500 列まで）。陣の ID は `b001`、`b002` … の順。

## CSV のファイルも取り出す・日本の府省と東京都（2026-10-24 Claude）
- これまでは CKAN の datastore（API で行を読める表）だけを使い、BODIK だけで 918 表を「datastore が無い」で落としていた。**datastore が無くても、カタログと同じホストの https の CSV なら候補にする**（`pool_discover.py`、候補に `access: "csv"`）。採用（`pipeline.py adopt`）も CSV の候補を通す
- 取り出し（`fetch_rows.py`）：CSV は先頭 3MB だけ読む（切れた最後の行は捨てる）。文字コードは UTF-8 → CP932。先頭 10 行から見出しの行を探す（表題・注の行を飛ばす）。個人情報の列・値の落とし方は datastore と同じ。別のホストの CSV・http の CSV は使わない（候補集めの `stats` に `csv_other_host` で数を残す）
- 国のポータルに **e-Gov（data.e-gov.go.jp、府省）** と **東京都（catalog.data.metro.tokyo.lg.jp、部局）** を足した（`--national --only-national <ホスト>`）。egov は FIXED_ASSIGNMENTS で train、tokyo は train に登録済みなので、部局も train になる
- 候補集めはホストごとに途中の結果を書き出し、Actions は「集める」が時間切れ（100 分）でも「保存」で途中までの候補と allocation.json を残す

## 組織のドメインの CSV・e-Gov のライセンス（2026-10-24 Claude）
- 10/24 の候補集め（candidates_20261024c）：東京都は datastore の 351 表のほか、**別のホストの CSV が 3,179**（都の各局のサイト）。e-Gov は **12,908 件すべて license_id が空**で落ちた
- `allowed_hosts.json` の `csv_domains`：カタログごとに CSV を取ってよい組織のドメイン（東京都 → `metro.tokyo.lg.jp`、e-Gov → `go.jp`）。カタログのホストか、そのドメインの下のホストの https の CSV だけ（似た名前の別ドメインは通らない）
- `pipeline.license_from_pkg`：license_id が空なら license_title を読む。政府標準利用規約（第2.0版）は CC BY 4.0 と互換と規約に明記されているので cc-by-4.0。CC BY（表示）も読む。NC・SA は通さない

## 個人の記録の表を見つけたら（2026-10-24 Claude。b007 から）
- 取り出しのあとで Claude が、題名・見出し・値を見て、1 人・1 件ごとの記録（生徒・職員の名簿、通報、受験者、違反の記録など）を探す。題名の規則（`pipeline.TITLE_DENY`）で落とせなかったものは規則にも足す
- ラベルを付ける前なら行を取り除く（`work/<陣>/removed.json` の rows）。**ラベルを付けた後は行を残して値だけを「［個人名のため削除］」にし、裁定で S にする**（rows0。行を取り除くとラベルとの対応がずれる）。シートは同じグループ分けのまま `label_sheets.render_sheet` で描き直す
- 1 陣の大きさ：採用できる表が多いときは、公開元を順に 1 表ずつ取って 500 表前後にする（b008 から。`adopted.json` の size_note）

## ラベル用シート（2026-10-24 Claude。b006 から）
ChatGPT が大きな `corpus.jsonl`（1 陣 3〜5MB）を読まずにラベルを付けるための道具。`materials/label_sheets.py`
- Claude：`python materials/label_sheets.py make --batch b00N` → `work/b00N/sheets/` に `sheet_001.md` …（1 枚 120 グループ・約 40KB）と `groups.json`
- **グループ**＝見出し・単位・値の形が同じ列のまとまり（数字・ラテン文字の形だけをそろえ、漢字・かなは文字のまま比べる）。グループの全部の列に同じラベルが付く。b005 で試すと 2,621 列 → 1,772 グループ（約 3 割減）、1 列ずつ付けたラベルとの違いは 7 列（0.3%）
- ChatGPT：シートを読み、末尾の「答えの雛形」を `work/b00N/sheets/answers/sheet_NNN.tsv` に写して、各行「g0001<TAB>ラベル」を埋める。シートごとに commit してよい（途中で止まってもシート単位で続きから）
- Claude：`status --batch b00N`（済んだシート・問題）→ `merge --batch b00N`（全部の行の `labels_chatgpt.jsonl` に戻す。答えの無いグループ・決まりにないラベル・別のシートの番号があれば止まる）→ いつもの `pipeline.py reconcile`
- 番号がはっきりしているので、行のずれ（b003 の 622〜664 行）や抜け（b004 の 1501〜1600 行）は起きない

## 候補を速く集める（2026-10-22 Claude）
- `materials/pool_discover.py`（Actions `pool-discover.yml`、依頼は `materials/pool/discover.request` に `discover materials/pool/candidates_<日付>.json --bodik --socrata`）。BODIK は train の組織ごとに検索 1 回で全データセットを見て datastore のあるリソースを選ぶ。Socrata はカタログ API。年度違いの同じ表は重ねない。
- 1 回目（2026-10-22）：2,201 表・272 公開元。1 陣 1 公開元 3 表までなので、b003 に 716 表、残りは b004 以降へ（同じ候補の一覧を `adopt` にもう一度渡せば、使った表は自動で外れる）。

## CKAN の公開元を足した（2026-10-24 Claude）
- BODIK（254 組織）と Socrata は 2026-10-22 の 1 回で調べ尽くした（もう一度回しても同じ表しか出ない）。新しい候補は、まだ使っていない train の CKAN の公開元から集める：ベロオリゾンテ（dados.pbh.gov.br、19 組織）・レシフェ（dados.recife.pe.gov.br、22）・リオグランデ・ド・スル州（dados.rs.gov.br、7）・ボストン（data.boston.gov、34）。組織の一覧は `independent_eval/allocation_sources_world_20261022.json`
- `pool_discover.py --ckan`（依頼：`discover materials/pool/candidates_<日付>.json --ckan`）。ホストは `allowed_hosts.json` の `ckan` にあるものだけ。ライセンスで落ちたものは `stats` に `license:<id>` で内訳を残す
- 取り出しでは、ポルトガル語の個人情報の列名（nome・cpf・telefone・endereço・logradouro・cep・servidor など）と値（CPF・電話・CEP・通りの住所）も落とす（`fetch_rows.py`）。題名の規則にもポルトガル語（servidor・remuneração・ocorrência・aluno・paciente など）を足した
- ライセンス：ODC-PDDL は公有の宣言なので public-domain と同じ扱いにした。ODbL（継承あり）は使わない

## 国のポータルを足した（2026-10-24 Claude）
- 豪州（data.gov.au）・アイルランド（data.gov.ie）・カナダ（open.canada.ca）。親の公開元（australia・ireland・canada）は `independent_eval/allocation.py` の FIXED_ASSIGNMENTS で train に固定なので、組織を「親:組織」（例 `australia:abs`）で登録すると必ず train になる（評価用の公開元とは重ならない）
- `pool_discover.py --national`：① 組織の一覧（organization_list、名前だけ）を取って `allocation.json` に登録 → ② そのあとで組織ごとに package_search（datastore のあるものだけ、1 組織 1,000 件まで見る）。Actions が `allocation.json` も保存する
- ライセンス：OGL-Canada-2.0 を OGL-UK-3.0 と同じく使ってよいことにした（出典表示だけ）
- レシフェ（10/24 はタイムアウト）は `--ckan --only-host dados.recife.pe.gov.br` で取り直す（待ち時間 120 秒、1 回 200 件）

## 取り出せる場（2026-10-22）
- BODIK の datastore（`data.bodik.jp`）
- Socrata（SODA）：公開元の ID が `world_socrata_<ホストの . と - を _ にしたもの>` で、ホストが一致するもの。列の定義から表示名を取り、位置情報・URL・写真の列は落とす。ライセンスは公式の `licenseId` で確かめる（PUBLIC_DOMAIN・CC0_10・CC_30_BY・CC_40_BY・ODC_BY_10）
- ほかの CKAN の datastore：`materials/pool/allowed_hosts.json` の `ckan` に Claude が足したホストだけ
- 採用の道具は、題名が個人の記録になりやすい表（犯罪・逮捕・通報・選挙資金・許可・入学・職員など）を落とす。主セットの NYC（`data.cityofnewyork.us`）は main に固定

## 目標と学習
- **第 1 目標：教材庫の学習に使える列 22,000**（既存の本物 約 11,000 列と合わせて約 3 倍。W1 の伸び方から＋4〜5 ポイントの見込み）。オーナーが変えてよい（`manifest.json` の `target_columns`）。
- 目標に達するまで学習はしない（Kaggle の GPU を使わない）。**目標に達しても、オーナーの許可が出るまで学習を始めない**（オーナー指示 2026-10-24「目標に達成しても俺の許可が出るまで学習は開始するなよ」。Claude・ChatGPT とも、学習の依頼ファイルの push・Kaggle の実行をしない）。目標に達したらオーナーに報告して許可を求め、許可が出たら Claude が学習の事前記録を書いて依頼する：検証つき（`FT_VAL=1 FT_POOL=1`、教材庫の 1/8 を「検証（教材庫）」に回す）で効果を見て、そのあと検証なしの最終の学習（`FT_POOL=1 FT_KEEP=1`）→ 封印セット #2。
- 学習の量の見込み：22,000 列 × 3 倍 ≒ 66,000 行が増え、学習の行は約 12 万行（今の約 2.2 倍）。1 本 約 20 分、3 本で約 40 分（2 GPU）。倍率は `FT_POOL_COPIES` で変えられる。

## 守ること
- 公開元は train だけ（`independent_eval/allocation.json`）。主セットの 4 出典・eval2・eval3・hold は使わない（採用の道具が止める）。
- 値は公開データだけ。個人情報の列は取り出しで落とす（`fetch_rows.py`）。
- 主セット・封印セット・固定試験の行から教材やガイドを作らない。
