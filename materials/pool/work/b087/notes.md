# b087 notes（Claude、2026-10-31）

- Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。
- 取り出せた 4 表・15 列。採点できるのは 7 列。
- S（8 列）：
  - 調達の進み具合の表（g0001・g0002）：見出しが表の題名の行で、値に部署名・説明・見出しの語が混ざる。
  - Cabinet Office の支出の承認（g0005–g0010）：列がずれている（Moratorium に部署名、Basis for Exception に月名、Date of Update に職階）。表が崩れているので全列 S。
- 迷った列：SPEND BY BUDGET TYPE（g0003）は小見出しの行が 1 つ混ざるが、残りは支出の区分（Running the estate・Procurement costs）→ account。TOTAL（g0004）は「£millions*」の行が 1 つ混ざるが金額 → amount。
- 上級職員の記録の表はない（b086 で足した TITLE_DENY が効いている）。

## Claude の裁定（2026-10-31、ChatGPT の答えと比べて）
- 一致 13/15 グループ。ChatGPT は Claude の notes の抜粋を先に見たと申告している（ai-bridge 20261031-1655）ので、厳密な独立ではない。
- g0003・g0004（年次報告の支出の表）：小見出しの行と「£millions*」が混ざる白書型の表 → **S**（ChatGPT。決まり 59 行）。
