# b086 notes（Claude、2026-10-31）

- Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。
- 取り出せた 6 表（25 列）はどれも上級職員の経費・接待・出張・面会の記録（Cabinet Office・HMRC・NIO・MOD）。LABEL_GUIDE 120 行により全 25 列 S。採点できる列は 0。
- 語 expenses がちょうどこの種の表を引いた。`materials/pipeline.py` の TITLE_DENY に senior officials・senior staff・special advis・大臣の gifts/hospitality/meetings/travel・hospitality を足して、次から採用の前に落とす。


## ChatGPT independent labels (LABEL_GUIDE v2.3)

- Independently labeled all 25 groups in `sheets/answers/sheet_001.tsv` from the sheet and LABEL_GUIDE v2.3 only. No model prediction or model label file was consulted.
- Table-level personal-record exclusions (all columns S):
  - **Business expenses of Cabinet Office senior officials including hospitality** — g0001–g0005; per-record destination, purpose, travel/hospitality, and total cost.
  - **Cabinet Office Senior Officials Travel Report** — g0006–g0012; per-trip itinerary and cost fields.
  - **HMRC Senior Officials Travel Report** — g0013–g0014; the sheet explicitly shows officials' names with travel destinations.
  - **NIO: Senior Officials' business expenses and the permanent secretary's meetings with external organisations: July to September 2021** — g0015–g0016; individual meeting dates and purposes.
  - **NIO: Senior Officials' hospitality, meetings and travel: April to June 2021** — g0017–g0018; hospitality record fields (examples are nil returns).
  - **MOD: senior officials' domestic and international travel and expenses** — g0019–g0025; per-trip product, date, duration, destination, class, and cost fields.
- These are the senior-official travel, meeting, hospitality, and expense record types that LABEL_GUIDE v2.3 excludes at table level. The displayed values are per-record itinerary/expense details; the HMRC table explicitly includes personal names.
- First-pass result: 25 raw columns S, 0 unknown, 0 scorable columns. This is before Claude adjudication.
