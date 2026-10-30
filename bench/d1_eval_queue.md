# D1 の比べるための新しい陣：集める順番（2026-10-30 Claude。オーナー「お前の方で確認してくれ」）

最低（採点できる列）：全体 2,500・英語 1,000・日本語 500・ドイツ語とフランス語で 500・1 公開元は全体の 3 割まで（`bench/d1_prereg_20261030.md`）。
`materials/pool/auto.request` が `done …` になったら、下の次の行を Claude が書く。採用が 0 表なら語を変えて次の番号へ。最低に届いた言語の行は飛ばしてよい。

| 番号 | 依頼 | ねらい | 結果 |
|---|---|---|---|
| b066 | `auto b066 --national --only-national data.gov.uk` | 英語 | 246 列（ChatGPT ラベル済み） |
| b067 | `auto b067 --national --only-national opendata.swiss` | 独・仏 | 432 列（独 121・仏 14 の見立て、ラベル済み） |
| b068 | `auto b068 --national --only-national open.canada.ca --query report` | 英・仏 | 70 列 |
| b069 | `auto b069 --national --only-national data.gov.ie --query statistics` | 英語 | |
| b070 | `auto b070 --national --only-national catalog.data.metro.tokyo.lg.jp --query 統計` | 日本語 | |
| b071 | `auto b071 --national --only-national opendata.swiss` | 独・仏（b067 で「1 公開元 3 表まで」で 140 表が残った） | |
| b072 | `auto b072 --national --only-national catalog.data.metro.tokyo.lg.jp --query 施設` | 日本語 | |
| b073 | `auto b073 --national --only-national opendata.swiss` | 独・仏 | |
| b074 | `auto b074 --national --only-national catalog.data.metro.tokyo.lg.jp --query 実績` | 日本語 | |
| b075 | `auto b075 --national --only-national open.canada.ca` | 英・仏 | |
| b076 | `auto b076 --national --only-national data.gov.au --query survey` | 英語 | |
| b077 | `auto b077 --socrata --query budget` | 英語 | |
| b078 | `auto b078 --national --only-national data.gov.uk` | 英語（b066 の残り） | |

言語は `set.json` の language が当てにならない（スイスも en）ので、列名と値の文字で見分けて数える。
