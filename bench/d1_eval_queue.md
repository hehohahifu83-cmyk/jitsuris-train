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
| b073 | `auto b073 --bodik --query 一覧` | 日本語 | 412 列（日本語 378 の見立て） |
| b074 | `auto b074 --national --only-national opendata.swiss` | 独・仏 | 320 列（独 90・仏 3 の見立て） |

**2026-10-31 02:40 の数（b066〜b073、ラベル前の列）**：全体 1,896・英語 約 1,050・日本語 約 620・独仏 約 230。英語と日本語は最低を超えた。

| b075 | `auto b075 --national --only-national open.canada.ca` | 英・仏（日本語は b073 で最低に届いたので、BODIK の行をやめて独仏を増やす。2026-10-31 02:40） | 19 列（カナダはほぼ使い切った → b077 のカナダはやめてスイスに） |
| b076 | `auto b076 --national --only-national opendata.swiss` | 独・仏 | 105 列（独 10） |
| b077 | `auto b077 --national --only-national opendata.swiss` | 独・仏（カナダの代わり） | 36 列（独 8）。スイスは語なしでは毎回同じ 433 表の候補で、使い切りに近い |
| b078 | `auto b078 --national --only-national opendata.swiss --query statistik` | 独（語で別の候補を探す。2026-10-31 05:00） | 182 列 |
| b079 | `auto b079 --national --only-national data.gov.au --query survey` | 英語（表ごとに数え直すと英語が足りない。2026-10-31 05:50） | 30 列 |
| b080 | `auto b080 --socrata --query budget` | 英語 | |
| b081 | `auto b081 --national --only-national data.gov.uk` | 英語（b066 の残り） | |
| b082 | `auto b082 --ckan --only-host data.boston.gov --query report` | 英語 | |
| b083 | `auto b083 --national --only-national data.gov.ie` | 英語 | |

**2026-10-31 05:00 の数（b066〜b077）**：全体 2,376・英語 約 1,415・日本語 約 618・独仏 約 343。独仏を出せる許可済みの公開元はスイスとカナダだけ（`materials/pool/allowed_hosts.json`）。語つきでも足りなければ、独仏の最低を下げるか、新しい公開元（ライセンスの確認から）をオーナーに相談する。

言語は `set.json` の language が当てにならない（スイスも en）ので、列名と値の文字で見分けて数える。

**2026-10-31 05:50 の数え直し（表ごとの言語、b066〜b078）**：全体 2,558・英語 937・独仏 891・日本語 730。列ごとの数え方では、スイスの表の英字の列名・数だけの列が英語に入っていた。表ごとの数え方を正とする（`count_table` の決まり：表の中に日本語の文字があれば日本語、ドイツ語・フランス語の語が 3 つ以上なら独仏）。独仏と日本語は最低を超えた。英語は S・不明が抜ける分を見て、あと約 200 列集める。
