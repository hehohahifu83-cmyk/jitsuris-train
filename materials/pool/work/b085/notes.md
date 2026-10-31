# b085 notes（Claude、2026-10-31）

- オーナー指示により Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。
- 採用 85 表のうち取り出せたのは 18 表、125 列（118 グループ）。
- S（38 列）：
  - 行と列が入れ替わった表（GMPP の大型事業の一覧：見出しが事業名・事業番号で、1 列に日付・金額・状態・説明が混ざる）：g0012–g0020・g0043–g0052・g0070–g0075。
  - 見出しが数の行になっている表（RfR1 / 3,815,040 …）：g0033–g0037。
  - 見出しの説明の行が値に混ざって、値がほとんど残らない列：g0089・g0090・g0100・g0101・g0103・g0104。
- unknown（5 列）：見出しが年度だけ（2008/09 …）で、値の数が金額か件数か表から分からない：g0038–g0042。
- 迷った列：
  - Expense Type・Expense Area → account（決まり 65 行：値が費目・部門）。Departmental Family・Entity・Supplier・Merchant → org。
  - Destination Airport Code（LCY・BFS）→ id（地点を指すコード）。
  - Delegated grades only（g0088）：説明の行が 1 つ混ざるが、残りは金額 → amount。
  - Comments（g0095：Cancelled・Credit note - full refund）：決まった語の繰り返し → category。Comments（g0091・g0118）は行ごとに違う文 → text。
  - Month（October）→ date（年月の一部）。Duration of Stay・Flights・Number of travellers → quantity。
- GPC カードの支払先・出張の記録は会社・役所が相手か、氏名の列がないので、個人の記録として S にはしない。


## ChatGPT independent labels (LABEL_GUIDE v2.3)

- `sheets/answers/sheet_001.tsv` contains independent labels for all 118 groups (125 underlying columns). No model predictions or other label files were consulted.
- Table-level personal-record exclusions: **BIS Senior Officials travel: Quarterly Return** (groups g0026–g0032), **FCO Senior Staff Travel Overseas** (g0061–g0069), and **Home Office senior officials travel report** (g0026–g0028, g0062, g0092–g0095; identical groupings are shared across source tables). These are per-trip official travel records with dates, destinations, and itinerary or cost fields; the whole table is labeled S under LABEL_GUIDE v2.3's senior-official travel record rule. The displayed examples do not include a person-name field, so this exclusion is based on the source table titles and per-trip record structure.
- Table-level structural exclusions (all relevant groups S): **BEIS Government Major Projects Portfolio data** (g0012–g0020), **DFID Annual Report and Accounts 2012-13** (g0033–g0037), **Government major projects portfolio data for DfT** (g0043–g0052), and **Government major projects data for the Foreign and Commonwealth Office** (g0070–g0075). Their sheet headers are project identifiers/names or numeric headings while example values mix dates, money, statuses, organizations, and narrative, so they do not provide stable field columns.
- In **Northern Ireland Office (NIO): Workforce Management Information: October 2021**, g0100–g0101 are S because examples mix measure labels/grade labels with counts. g0103 and the repeated paybill groups g0088–g0090 are unknown where the examples mix monetary values, explanatory text, or counts under the same grouping; g0104 is text.
- First-pass totals: 56 raw columns S, 7 unknown, and 62 scorable columns (before Claude adjudication). These are table-language counts pending adjudication.
