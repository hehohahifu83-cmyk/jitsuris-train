# b084 notes（Claude、2026-10-31）

- オーナー指示「あと200列はお前がやってくれ」により Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。2 人目の目がないので、あとで抜き取りを ChatGPT か Grok に独立に付けてもらう。
- 採用 134 表のうち取り出せたのは 3 表（Cabinet Office の大臣の出張・会合・接待の公開記録、12 列）。残りは datastore 403、許可外ホスト上の XLS/CSV/XML/HTML/PDF などで取れなかった（`corpus_log.json`）。
- 迷った列：
  - Minister（g0001・g0007・g0010）：「Minister of State, The Rt Hon …」のような役職つきの氏名 → person（決まりの表「役職つきでも」）。注記の行が 1 つ混ざるが多い方で決めた。
  - Destination（g0003）：都市・国 → address。
  - 交通手段（g0005、Scheduled など）・接待の種類（g0012）→ category。目的（g0004・g0009）は行ごとに違う文 → text。
  - Total Cost（g0006）：値の頭の「」」は £ の文字化け → amount。
- 公人の公開記録（大臣の公務）なので個人の記録として S にはしない。
