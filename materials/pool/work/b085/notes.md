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
