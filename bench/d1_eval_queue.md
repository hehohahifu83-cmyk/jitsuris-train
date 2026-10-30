# D1 の比べるための新しい陣：集める順番（2026-10-30 Claude。オーナー「お前の方で確認してくれ」）

最低（採点できる列）：全体 2,500・英語 1,000・日本語 500・ドイツ語とフランス語で 500・1 公開元は全体の 3 割まで（`bench/d1_prereg_20261030.md`）。
`materials/pool/auto.request` が `done …` になったら、下の次の行を書く（Claude でも ChatGPT でもよいが、**この表の番号と依頼を使う**。2026-10-31 00:55 に b071 から入れ替えた）。採用が 0 表なら語を変えて次の番号へ。最低に届いた言語の行は飛ばしてよい。

| 番号 | 依頼 | ねらい | 結果 |
|---|---|---|---|
| b066 | `auto b066 --national --only-national data.gov.uk` | 英語 | 246 列（ChatGPT ラベル済み） |
| b067 | `auto b067 --national --only-national opendata.swiss` | 独・仏 | 432 列（独 121・仏 14 の見立て、ラベル済み） |
| b068 | `auto b068 --national --only-national open.canada.ca --query report` | 英・仏 | 70 列（ラベル済み） |
| b069 | `auto b069 --national --only-national data.gov.ie --query statistics` | 英語 | 52 列（ラベル済み） |
| b070 | `auto b070 --national --only-national catalog.data.metro.tokyo.lg.jp --query 統計` | 日本語 | 64 列（東京都は「教材庫で 1 公開元 15 表まで」で 27 表落ちる → 日本語は BODIK に切り替え） |
| b071 | `auto b071 --bodik --query 統計` | 日本語（全国の自治体。公開元が多く、上限に当たりにくい） | 259 列（日本語） |
| b072 | `auto b072 --national --only-national opendata.swiss` | 独・仏（b067 で「1 公開元 3 表まで」で 140 表が残った） | 361 列（ChatGPT ラベル済み） |
| b073 | `auto b073 --bodik --query 一覧` | 日本語 | 済（列数は下の数え直し） |
| b074 | `auto b074 --national --only-national opendata.swiss` | 独・仏 | |
| b075 | `auto b075 --bodik --query 実績` | 日本語 | |
| b076 | `auto b076 --national --only-national open.canada.ca` | 英・仏 | |
| b077 | `auto b077 --national --only-national data.gov.au --query survey` | 英語 | |
| b078 | `auto b078 --socrata --query budget` | 英語 | |
| b079 | `auto b079 --national --only-national data.gov.uk` | 英語（b066 の残り） | |

言語は `set.json` の language が当てにならない（スイスも en）ので、列名と値の文字で見分けて数える。
