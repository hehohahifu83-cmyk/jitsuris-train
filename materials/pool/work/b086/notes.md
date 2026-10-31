# b086 notes（Claude、2026-10-31）

- Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。
- 取り出せた 6 表（25 列）はどれも上級職員の経費・接待・出張・面会の記録（Cabinet Office・HMRC・NIO・MOD）。LABEL_GUIDE 120 行により全 25 列 S。採点できる列は 0。
- 語 expenses がちょうどこの種の表を引いた。`materials/pipeline.py` の TITLE_DENY に senior officials・senior staff・special advis・大臣の gifts/hospitality/meetings/travel・hospitality を足して、次から採用の前に落とす。
