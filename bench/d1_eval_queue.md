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
| b080 | `auto b080 --socrata --query budget` | 英語 | 27 列 |
| b081 | `auto b081 --national --only-national data.gov.uk` | 英語（b066 の残り） | 162 列（採点できる 99） |
| b082 | `auto b082 --ckan --only-host data.boston.gov --query report` | 英語 | 0 表（14 表すべて使用済み） |
| b083 | `auto b083 --national --only-national data.gov.ie` | 英語 | 11 列、採点候補 5（ChatGPT ラベル済み）; 1 採用表は取り出し404、HBFI 2表は全列 S |
| b084 | `auto b084 --national --only-national data.gov.uk` | 英語（残りの公開元を検索、採点候補を約200列補う） | 12 列（表 3、大臣の記録なので全列 S に訂正。Claude ラベル）。採用 134 表の大半は許可外ホスト・403 で取り出せず |
| b085 | `auto b085 --national --only-national data.gov.uk --query spend` | 英語（語で別の候補。支出の公開 CSV は gov.uk 上に置かれることが多い） | 125 列（表 18。ChatGPT も独立に付けた → 一致 88/118 グループ。上級職員の出張の表は S で、採点できる 62） |
| b086 | `auto b086 --national --only-national data.gov.uk --query expenses` | 英語（英語がちょうど 1,000 で余裕がない。裁定で減る分を見て、あと約 120 列） | 25 列（表 6、全部上級職員の記録 → 全列 S。TITLE_DENY に足した） |
| b087 | `auto b087 --national --only-national data.gov.uk --query contracts` | 英語（あと 20 列＋余裕） | 15 列（表 4、採点できる 7。Claude ラベル） |
| b088 | `auto b088 --socrata --query inventory` | 英語（data.gov.uk は語を変えても取れる表が少ない。米国の Socrata で別の公開元を探す） | 29 列（表 4、採点できる 28。Claude ラベル） |
| b089 | `auto b089 --socrata --query equipment` | 英語（全体あと 2 列＋裁定で減る分の余裕） | 4 列（表 1、採点できる 4。Socrata は「1 公開元 15 表まで」に当たり始めた） |
| b090 | `auto b090 --bodik --query 施設` | 日本語（全体の最低の余裕。英語の公開元は残りが少ないので、多く取れる BODIK で全体を補う） | |

**2026-10-31 05:00 の数（b066〜b077）**：全体 2,376・英語 約 1,415・日本語 約 618・独仏 約 343。独仏を出せる許可済みの公開元はスイスとカナダだけ（`materials/pool/allowed_hosts.json`）。語つきでも足りなければ、独仏の最低を下げるか、新しい公開元（ライセンスの確認から）をオーナーに相談する。

言語は `set.json` の language が当てにならない（スイスも en）ので、列名と値の文字で見分けて数える。

**2026-10-31 05:50 の数え直し（表ごとの言語、b066〜b078）**：全体 2,558・英語 937・独仏 891・日本語 730。列ごとの数え方では、スイスの表の英字の列名・数だけの列が英語に入っていた。表ごとの数え方を正とする（`count_table` の決まり：表の中に日本語の文字があれば日本語、ドイツ語・フランス語の語が 3 つ以上なら独仏）。独仏と日本語は最低を超えた。英語は S・不明が抜ける分を見て、あと約 200 列集める。

**2026-10-31 09:50 の数（b066〜b081、ChatGPT の初回ラベルで S・unknown を除く、Claude の裁定前）**：採点できる 2,396（英語 913・日本語 593・独仏 890）。足りないのは全体 104・英語 87。1 公開元の最大は 5.4%（swiss:oevch）。数え方は `bench/d1_counts.py`（表ごとの言語）、結果 `bench/d1_counts_20261031.md`。裁定で減る分を見て、英語をあと約 200 列（採点できる列で）集める。b083 を依頼。

**2026-10-31 10:35 の暫定数（b066〜b083、ChatGPT 初回ラベルで S・unknown を除く、Claude 裁定前）**：2,401（英語 918・日本語 593・独仏 890）。b083 は英語 5 列。残りは全体 99・英語 82（裁定後の最低に対する余裕を考え、英語を約200列集める）。最大公開元は既報の swiss:oevch 130 列（全体の約5.4%）。

**2026-10-31 13:10 の暫定数（b066〜b084、b083 まで ChatGPT 初回ラベル・b084 から Claude ラベル、S・unknown を除く、裁定前）**：2,413（英語 930・日本語 593・独仏 890）。残りは全体 87・英語 70。b084 は data.gov.uk の語なしで 12 列だけ（候補の多くが使用済みか許可外ホスト）。b085 は語 spend で別の候補を探す。

**2026-10-31 15:00 の暫定数（b066〜b085、b084 から Claude ラベル、S・unknown を除く、裁定前）**：2,483（英語 1,000・日本語 593・独仏 890）。残りは全体 17・英語 0。ただし英語は余裕がないので、b086 で語 expenses を探す。

**2026-10-31 15:40 の数え直し（b066〜b086）**：2,463（英語 980・日本語 593・独仏 890）。足りないのは全体 37・英語 20。b084・b086 は LABEL_GUIDE 120 行（上級職員の出張・接待・面会の記録は全列 S）を Claude が見落としていたので全列 S に訂正、b085 は ChatGPT の独立ラベルで数える。Claude 一人のラベルの抜き取りを、b085 で ChatGPT と比べた形になった（一致 88/118）。

**2026-10-31 16:20 の数（b066〜b087）**：2,470（英語 987）。足りないのは全体 30・英語 13。b088 は Socrata の語 inventory。

**2026-10-31 17:00 の数（b066〜b088）**：2,498（英語 1,015・日本語 593・独仏 890）。足りないのは全体 2。裁定で減る分の余裕に b089 を依頼。

**2026-10-31 17:20 の数（b066〜b089）**：2,502（英語 1,019・日本語 593・独仏 890）。**4 つの最低すべてに届いた**（裁定前）。余裕は全体 2・英語 19 しかないので、全体の余裕を b090（BODIK）で取る。
