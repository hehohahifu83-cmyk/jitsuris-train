# Shirasagi 独自API（train専用）

候補探しと取り出しは `materials/shirasagi.py`。登録・allocation変更・採用はClaudeが行う。
`allowed_hosts.json` に新しい `shirasagi` 配列を設ける（既定は空）。

```json
{"shirasagi":[{"site":"https://catalog.example.jp/subpath","max_datasets":1000,
 "publishers":[{"field":"user.id","value":"587","municipality_code":"020001",
 "evidence_url":"https://catalog.example.jp/verified-publisher"}]}]}
```

`site` はカタログの実際の基点。既存 `csv_domains` に取得先も明記する。HTTPは既存の完全一致 `http_hosts` だけ。
提供元は確認済みの `author` / `user.id` / `user.name` と自治体コードの対応表で指定する。
`evidence_url` は対応を確認した公開URLを記録する欄であり、自動的な検証済み判定ではない。登録時に人が根拠を確認する。
外部ファイルの提供元は `field: download_host` の完全一致で別途登録する。共用ストレージは自治体の証拠にならないので登録しない。
静岡の `groups=静岡県` は浜松市ファイルにも付き、愛媛も県名のまま市町のファイルを収録する。`areas` は対象範囲であり提供者の証拠には使わない。不明・競合は除外。
自治体コードは6桁検査数字を検証し、既存allocationの別名解決後に明示的なtrain登録を要求する。未登録・hold・eval・mainを除外し、仙台市041009は登録状態によらず除外する。

資料ごとの `license.uid/name` が既存許可一覧にあるCSV/XLS/XLSXだけを候補にする。データセットやサイトの既定ライセンスは継承しない。
資料の識別子は `shirasagi:{host}:{dataset_uuid}:{resource_id}`。resource.id欠落時はURLのSHA256を使う。
数値dataset.idは公開ページ、UUIDはAPIの問い合わせに使う。公開ページのqueryにUUID/資料トークンを保持する。
同じデータセットの別形式・年度違い題名・使用済み資料・自治体15表上限を既存収集と合わせて除外する。
取り出し時にも提供元・train割り当て・ライセンス・数値id・取得先許可を再確認し、既存CSV/Excel解析器を使う。
メタデータは1ホスト2秒間隔以上・直列、一覧はlimit/offsetを明示した100件単位、一覧上限1000件（設定1〜5000）、既存全体時間制限に従う。

```bash
python materials/pool_discover.py --help
# 実行はClaude担当。既存の出力先・pool引数と併用する。
# --shirasagi --only-shirasagi catalog.example.jp
```

実データでの採用・ファイル取得は登録後にClaudeが検証する。実装試験は `python -m unittest discover -s tests -p test_shirasagi.py`。
