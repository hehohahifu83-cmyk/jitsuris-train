# 独立評価セット候補の発見

## S9 の公開元割当（データを読む前に実施）

- `specs/SEALED_EVAL_PROTOCOL.md` §2 に従い、公開元 ID を確認したら、データセット情報や表の値を見る前に割り当てます。
- `independent_eval/allocation.json` は既存の学習公開元と主セット公開元の固定レジストリです。割当済み ID は付け替えません。
- 新しい CKAN 公開元は、`organization_list` を `all_fields=false` で呼び、ポータル URL と `organization.name` の組だけを保存します。ID は `<portal_id>:<organization.name>` として `allocation.py` で記録します。曖昧な公開元は `--ambiguous` で `hold` に入れ、学習・評価の両方から外します。
- 割当レジストリを commit するまでは `package_search` を呼びません。割当後に eval2・eval3 の公開元だけを対象として、題名・ライセンス・リソース形式・URL のメタデータを取得します。リソースのダウンロード、データセット本文・行・列値の取得は行いません。
- 割当を済ませた公開元についても、この手順だけではデータセットを取得・閲覧しません。セットの選定・凍結は別途手順と承認が整ってから行います。

S9 #2/#3 の候補発見では、公開カタログのメタデータだけを記録します。個別データセットのライセンス・公開元・URL を確認し、学習側との URL 完全一致を検査します。メタデータだけでプライバシーを判断できない候補は保留し、行・列値を見る段階には進みません。

公開元の取得時点の一覧は `independent_eval/allocation_sources_20261021.json`、eval2・eval3 の候補メタデータは `independent_eval/results/discovery/` に記録します。割当や候補発見だけでは、実データを使う独立評価セットは固定されません。

## 主セットを抽出するとき

- `independent_eval/allowlist.json` に、候補ごとの個別利用条件・プライバシー・学習データとの重複を確認して固定します。
- 公開 runner を使う場合、再配布が許可された公開データだけを採用します。個人情報・住所・連絡先・第三者制限・学習重複・有償表示がある候補は除外します。
- 必要最小限の列と先頭5行だけを `independent_eval/results/main/independent_main.json` に抽出します。出典・バージョン・変更内容・各リソースと入力セットの SHA-256 は同じ場所の `provenance.json` と `ATTRIBUTION.md` に記録します。
- 候補発見時のサンプル値、元CSV全体、ラベル、未見セットの内容は、この公開リポジトリや Actions 成果物へ保存しません。ラベルはセット固定後に別ファイルで付け、学習用データ束から分離します。
- 評価入力は `evaluate_independent.py` の schema_version 1 に合わせます。候補の発見やセット抽出だけでは、モデル評価を実行しません。
