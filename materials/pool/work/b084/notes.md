# b084 notes（Claude、2026-10-31）

- オーナー指示「あと200列はお前がやってくれ」により Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。2 人目の目がないので、あとで抜き取りを ChatGPT か Grok に独立に付けてもらう。
- 採用 134 表のうち取り出せたのは 3 表（Cabinet Office の大臣の出張・会合・接待の公開記録、12 列）。残りは datastore 403、許可外ホスト上の XLS/CSV/XML/HTML/PDF などで取れなかった（`corpus_log.json`）。
- 迷った列：
  - Minister（g0001・g0007・g0010）：「Minister of State, The Rt Hon …」のような役職つきの氏名 → person（決まりの表「役職つきでも」）。注記の行が 1 つ混ざるが多い方で決めた。
  - Destination（g0003）：都市・国 → address。
  - 交通手段（g0005、Scheduled など）・接待の種類（g0012）→ category。目的（g0004・g0009）は行ごとに違う文 → text。
  - Total Cost（g0006）：値の頭の「」」は £ の文字化け → amount。
- ~~公人の公開記録（大臣の公務）なので個人の記録として S にはしない。~~
- **2026-10-31 訂正**：LABEL_GUIDE 120 行「大臣・常任次官・特別顧問・上級職員の贈答・歓待・出張・面会の記録は表の全列を S」を見落としていた（b085 の ChatGPT の独立ラベルとの食い違いで気づいた）。3 表とも大臣の出張・会合・接待の記録なので、12 列すべて S に付け直した。上の「迷った列」は付け直し前の判断。


## ChatGPT independent table-level exclusions (LABEL_GUIDE v2.3)

- Sheet 001 groups g0001–g0006 belong to **Cabinet Office Ministerial Overseas Travel data**. The table records named ministers' individual trips, dates, destinations, purposes, travel mode, and trip costs. This is a per-person official travel record table; exclude the entire table as S.
- Sheet 001 groups g0007–g0009 belong to **Cabinet Office Ministerial Meetings data**. The table records individual ministers' dates and purposes of meetings, so exclude the entire per-person meeting-record table as S.
- Sheet 001 groups g0010–g0012 belong to **Cabinet Office Ministerial Hospitality data**. The table records individual ministers' hospitality dates and types, so exclude the entire per-person hospitality-record table as S.

All 12 groups are labeled S because LABEL_GUIDE v2.3 excludes personal records at table level; labels were decided from the sheet examples and guide without consulting any model predictions.
