# 日本の自治体カタログ調査（2026-11-04、Codex）

初回Actions run [41796850950](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/41796850950)、ページ送り修正後の再集計run [41801461167](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/41801461167) はいずれも成功。採用する件数は再集計後だけ。

公的な一覧CSV 3本から5,909 URL参照を抽出。重複をまとめた2,438 API基点を調査、CKAN成功15基点（HTTP/HTTPSの那須1組をまとめると14サイト）。未調査0、一覧取得エラー0。組織一覧は15基点すべて最終の空ページまで確認。

初回のorganization_listはlimit=1000でも25件しか返さないサイトで、offsetを1000進めて過少計上していた。返った件数でoffsetを進めるよう修正し、回帰試験を追加。2回目は既存結果のCKAN15基点だけを8分割で再集計した。

## 到達したサイト（HTTP/HTTPS重複をまとめたもの）

| API基点 | 可視組織 | 組織のpackage_count合計 | 現allowed_hosts |
|---|---:|---:|---|
| https://all-mina-ckan.ayanami-service.jp | 1 | 1 | 未登録 |
| https://catalog-data.city.kanazawa.ishikawa.jp | 7 | 319 | 未登録 |
| https://catalog.data.metro.tokyo.lg.jp | 98 | 9674 | 登録あり |
| https://ckan.hoda.jp | 84 | 461 | 未登録 |
| https://ckan.odp.jig.jp | 49 | 1524 | 未登録 |
| https://data.city.fukuyama.hiroshima.jp | 15 | 58 | 未登録 |
| https://data.city.yokohama.lg.jp | 47 | 648 | 未登録 |
| https://gifu-opendata.pref.gifu.lg.jp | 65 | 1872 | 未登録 |
| https://opdt.city.toyama.lg.jp | 1 | 133 | 未登録 |
| https://opendata-nasu.opendatastack.jp | 71 | 488 | 未登録 |
| https://opendata.city.imizu.toyama.jp | 1 | 169 | 未登録 |
| http://opendata.city.machida.tokyo.jp | 1 | 144 | 未登録 |
| http://opendata.city.niigata.lg.jp | 1 | 489 | 未登録 |
| http://opendata.city.sagamihara.kanagawa.jp | 27 | 114 | 未登録 |

## 出典CSV

- https://data.e-gov.go.jp/data/dataset/ca0bdf50-eb05-481a-ac48-da0c27fc4c0b/resource/d500cb3e-7569-4985-94f8-d7afceedd388/download/20251031_resources_opendata_lg_pref_list_02.csv（SHA-256 `62d9010c6a49459d2a78cc203f3e90932dc2f619b0e4eac90d70ccbaae8287e9`）
- https://data.e-gov.go.jp/data/dataset/ca0bdf50-eb05-481a-ac48-da0c27fc4c0b/resource/e1d71b29-bb97-472c-bcc1-1761b6c2d197/download/20251031_resources_opendata_lg_mani_list_03.csv（SHA-256 `1a0c272c690bdf290d007c692713f29e1b7453bbc0d797cbe7626bd7e168c1c7`）
- https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/2b1128e2-c699-4aa0-9206-37169a6697c8/3d2142af/20260630_resources_opendata_lg_list_02.csv（SHA-256 `928307667dde46f5f7943058c93515865a69e72c14eb4fc804c7acf73bc45887`）

## 解釈の制限

- 表の中身・値は取得していない。カタログ候補へのAPI呼出しはstatus_showとorganization_listだけ。公的な一覧CSVと、その参照を見つける一覧ページ・e-Govのpackage_showは別途取得した。
- 可視組織が所有するpackage_countの合計で、無所属・非公開のデータセットは含まない。サイト間で組織や表が重複しうるので合算を独立な公開元数にしない。
- HTTP/HTTPS以外の別名やリダイレクト先の統合は未実施。14サイトを新しい公開元14件・新規採用14件とは扱わない。
- CKAN以外のサイト、APIを閉じたサイト、一覧に無いカタログ、深いサブパスのAPIはこの調べでは確保できない。失敗結果もJSONに残した。
- allowed_hosts.jsonとallocation.jsonは変更なし。横浜など既存評価の公開元も混ざるので、利用可否・F1/SCRC/trainの割り当てはClaudeが確認する。
- 55 Python試験成功（先例・カタログ・既存の関連試験）。学習・表の収集は起動していない。

出力: `materials/pool/probe/jp_catalogs_20261104.json`、SHA-256 `6f09329192f4f8c227db64bf87fef946ed01ece3fbe8d18ce87b41c220d22ea0`。
