# 教材集めの自動化：ChatGPT 向けの使い方（2026-10-26 Claude）

オーナー指示（2026-10-26）：Claude の利用制限が解けるまでの約 1 日、ChatGPT が教材を集める。

## 1. 道具：1 行書くだけでラベル用シートまでできる
`materials/pool/auto.request` の 1 行目を次の形で書き換えて main に push する（Actions `pool-auto.yml` が動く）：

```
auto <陣> <探し方>
```

自動でやること：試験 → 候補を集める（メタデータだけ）→ 採用（規則は `pipeline.py adopt` のまま。train の公開元・許可ライセンス・使っていない表・1 公開元の上限）→ 値の取り出し → `set.json` → ラベル用シート。終わると `auto.request` が `done …` になり、`materials/pool/work/<陣>/auto_log.md` に「採用した表・取り出した列・シートの枚数」が書かれる。

守ること：
- **1 回に 1 つ**。`auto.request` が `done …` になってから次を書く（1 回 30 分〜2 時間）
- 陣の番号は **1 回ごとに新しい番号**（b018、b019 …）。採用が 0 表でも、その番号は使えなくなる（次の番号で探し方を変える）
- `--query` の語は **1 つだけ**（空白を入れない）
- 採用の規則・`allowed_hosts.json`・`allocation.json`・`pipeline.py` は変えない（評価の独立のため。変えたいときは Claude への提案に書く）

## 2. 集めるもののリスト（上から順に）
今の苦手（交差検証で間違えた・不明だった列の種類）：quantity 952、date 656、address 653、category 611、org 506、text 293、id 265。この種類が多そうな表を語で探す。

| 順 | 依頼の 1 行 | ねらい |
|---|---|---|
| 1 | `auto b018 --national --only-national data.e-gov.go.jp` | e-Gov の残り（約 40 表）。**b018 は最終確認の陣**（学習に入れない。Claude が使う） |
| 2 | `auto b019 --national --only-national catalog.data.metro.tokyo.lg.jp --query 所在地` | address |
| 3 | `auto b020 --national --only-national catalog.data.metro.tokyo.lg.jp --query 件数` | quantity |
| 4 | `auto b021 --national --only-national data.e-gov.go.jp --query 年月日` | date |
| 5 | `auto b022 --national --only-national data.gov.au --query address` | address（英語） |
| 6 | `auto b023 --national --only-national data.gov.au --query count` | quantity（英語） |
| 7 | `auto b024 --socrata --query permit` | date・address・id・category（米国の train の公開元だけ） |
| 8 | `auto b025 --national --only-national data.gov.ie --query register` | org・category |
| 9 | `auto b026 --national --only-national open.canada.ca --query inventory` | category・quantity |
| 10 | `auto b027 --ckan --only-host data.boston.gov --query inspection` | date・address |

採用が 0 表のときは、語を変える（日本語：住所・施設・一覧・事業者・区分・種別・実績・統計・人数・届出、英語：facility・location・inspection・license・grant・contract・schedule・survey）。同じ語で 2 回やらない。

### 2026-10-28 追加（Claude）：次の順
これまでの取れ高：data.gov.au が一番多い（語なし b036 276 列、address 141・count 130・population 87）。次に data.gov.ie（53）・open.canada.ca（45）・東京都（103）。data.gov.uk は b049 で採用 396 表すべて resource_show が HTTP 403 だった → **2026-10-28 Claude が直した**（resource_show だけが止められていたので package_show から読む。opendata.swiss は名乗り方で止められていたので直した。調査 `materials/pool/probe/hosts_20261028.json`）。data.boston.gov は候補がすべて使用済み（b027〜b034）。

| 順 | 依頼の 1 行 | ねらい |
|---|---|---|
| 11 | `auto b050 --national --only-national data.gov.au --query register` | org・category・date（Claude が出した。data.gov.au は語なしでも 2,227 候補のうち 2,038 表がもう使った表で、残りは少ない） |
| 12 | `auto b051 --national --only-national opendata.swiss` | **まだ一度も集めていない公開元**（2026-10-27 に train に固定・許可済み）。ドイツ語・フランス語。1 陣 600 表までなので、採用が多ければ同じ形で b052 も |
| 13 | `auto b052 --national --only-national opendata.swiss` | b051 の残り（b051 の auto_log で「残りは次の陣へ」があるときだけ。無ければ飛ばす） |
| 14 | `auto b053 --national --only-national open.canada.ca` | 語なし（英語・仏語） |
| 15 | `auto b054 --national --only-national data.gov.ie` | 語なし |
| 16 | `auto b055 --national --only-national catalog.data.metro.tokyo.lg.jp --query 一覧` | 日本語の category・address |
| 17 | `auto b056 --national --only-national data.gov.au --query grants` | org・amount・date |
| 18 | `auto b057 --national --only-national open.canada.ca --query licence` | date・id・org |
| 19 | `auto b058 --national --only-national data.gov.uk` | 英国（直したあと。Claude が出した） |
| 20 | `auto b059 --national --only-national opendata.swiss` | スイス（直したあと） |
| 21 | `auto b060 --national --only-national data.gov.uk` | **英国をもう一度**（2026-10-28 Claude が出した。b058 は 162 表すべて「redirected outside the allowed hosts」＝API が ckan.publishing.service.gov.uk へ転送していた → 許可した。b049 の 395 表も「使った表」から外した） |
| 22 | `auto b061 --national --only-national opendata.swiss` | **スイスをもう一度**（b059 は候補 0：利用条件が URL（…/terms-of-use#terms_by）で来て読めなかった → 直した。terms_open・terms_by だけ使い、terms_ask・terms_by_ask は使わない） |
| 23 | `auto b062 --national --only-national data.gov.uk` | 英国の残り（b060 の auto_log に「残りは次の陣へ」があるか、採用が多いとき） |
| 24 | `auto b063 --national --only-national opendata.swiss` | **スイスをもう一度**（b061 は 149 表すべて転送の誤り＝API が ckan.opendata.swiss へ転送 → 許可した。2026-10-28 Claude） |
| 25 | `auto b064 --national --only-national opendata.swiss` | **スイスの残り**（b063 は 433 候補のうち 283 表が「1 陣 1 公開元 3 表まで」で次の陣へ回った。使った表は自動で外れる。2026-10-28 Claude） |

**列が減った理由（2026-10-28 Claude）**：b003〜b014 は 1 陣 1,100〜4,500 列だったが、b015 から 15〜320 列。①大きい公開元（東京都・豪州・世界の CKAN）の表をもう使った（b012 で候補 13,748 のうち 10,221、b036 で 2,227 のうち 2,038）②`--query` の 1 語で候補が 30〜230 に絞られる ③採用しても取り出しで落ちる（b036：採用 133 表のうち取り出せたのは 47。見出しの行が見つからない 42、datastore が 302 で 16）。増やすには**新しい公開元**が要る

## 3. ラベル付け（今までと同じ）
- `materials/pool/work/<陣>/sheets/sheet_NNN.md` を LABEL_GUIDE v2.0 だけで答え、`materials/pool/work/<陣>/sheets/answers/sheet_NNN.tsv` に保存する（予測は見ない。予測ファイルはまだ無い）
- 1 人・1 件ごとの記録（名簿・通報・受験者・違反者など）に見える表は、その表の列を全部 `S` にし、`work/<陣>/sheets/answers/notes.md` に表の名前と理由を書く
- 突き合わせ・裁定・確定（`merge`・`reconcile`・`finalize`）は Claude が戻ってからやる

## 4. 新しい公開元（調べるだけ。取り込みは Claude）
`materials/pool/new_sources_20261026.md` の候補の扱い（Claude が割り当てを確かめた結果）：
- **横浜市・神戸市：使わない**（主セットの公開元。`allocation.py` の FIXED_ASSIGNMENTS で main）
- **神奈川県（140007）：使わない**（eval2 に当たる）
- 仙台市（041009）・山口県（350001）：train に当たる。取り込むには組織ごとの公開元の決め方が要る（山口のカタログは県内の市町が混ざる。市町は自分の団体コードで割り当てる必要がある）→ **組織の一覧と、各組織がどの団体（団体コード）かの対応表**を `materials/pool/new_sources_orgmap_20261026.md` に作ってほしい（メタデータだけ）
- ニュージーランド・リオ州・英国：組織の一覧とライセンスの内訳（メタデータだけ）を同じファイルに
