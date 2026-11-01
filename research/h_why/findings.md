# 直し G のあとに残る誤りの調べと、直し H の候補（2026-11-01 Claude。使い済みの陣だけ。採否には使わない）

材料：`analyze.py` → `columns.jsonl`（4 陣 × 3 本の全部の出力）・`summary.md`、`ablate.py` → `ablate.md`。
今の製品（直し G 込み、辞書 frozen_d3、L 3 本）。

## 1. 残りの大きいもの（3 本・4 陣の合計の出力）
| 正解 → 答え | 出力 | 読み |
|---|---:|---|
| category → id | 144 | 種類のコード（gebaeudekategorie_code・hh_typ_nr・NACE Code・中分類コード）。LABEL_GUIDE B3 では category。本体が「code」「_nr」の語尾で id と言う |
| address → org | 140 | 日本の施設の一覧の「名称」（浦安市 b102・b073・b090 など）。公園と学校が混ざる表。決まりの境目（v1.7・v1.4）で、2 人でも割れた所。直すなら決まりから（ChatGPT に相談） |
| id → category | 57 | Table|Tableau（ファイル名）・designation（A・B・R）など。まとまった形がない |
| 不明（日付の正解） | 約 110 | FR_MOIS（nov.・juil.）、FR_TRIMESTRE（T1〜T4）、和暦の年月日、Excel の日付の番号、UNIX 時刻。**本体の段で不明**のため、見張りの見直し（F3・G4）が届かない |

## 2. 直し H の候補（`research/fixes/fixes_h.py`。評価の段だけ、製品のコードは変えない）
- **H1 種類のコード**：列名が「種類の語＋コードの語尾（code・nr・id・cd）」で、最終が id、本体の上位 3 に category があれば category。
  - 種類の語：語の終わりが kategorie・klasse・art・typ・status・form・system・herkunft・sprache・gruppe・sektor・level など。または NACE・NAICS・NOGA・SIC・HS・class などの語。日本語は「分類・種別・種類・区分・業種・用途・構造」＋コード・番号。
  - 個々の物・区域を指す語（bfs・gemeinde・quartier・plz・egid・formular・genehmigung・partner など）がある列は見ない。
  - 「art」だけの語は見ない（仏語の Code-art＝品目のコード。b095 の 4 列で外れた）。
- **H2 日付の形**：最終が不明で、列名に日付の語があり、値の 8 割以上がはっきりした日付の形なら date。
  - 形：仏独英の月の名前（JAN./JAN. も）、四半期 Q1〜Q4・T1〜T4、和暦の年月日・範囲、HHMMSS（列名が時刻）、seit 2010、ISO の日付・期間、Excel の日付の番号・UNIX 時刻（列名が日付のとき）。
  - 1〜2 桁の数だけの列（DAY_SURV・Settimana）は見ない。「日数」などの数の列に当たらないため。

## 3. 確かめ（3 本の合計。`ablate.md`）
| 陣 | P 正しい／重大 | P＋H1 | P＋H2 | P＋H |
|---|---|---|---|---|
| 古い 23 陣（1 本） | 3,740／2 | 3,732／2 | 3,742／2 | 3,734／2 |
| 決める陣 | 3,239／4 | 3,241／4 | 3,248／4 | 3,250／4 |
| 確かめる陣 | 3,228／18 | 3,264／18 | 3,240／18 | 3,276／18 |
| E1 | 3,214／9 | 3,223／9 | 3,225／9 | 3,234／9 |
| E2 | 3,399／1 | 3,410／1 | 3,418／1 | 3,429／1 |

- H2 は 5 陣とも良くなり、悪くした出力は 0。重大は変わらない（date は数の種類ではない）。
- H1 は 4 陣で良くなった。古い 23 陣だけ −8。
  - 悪くした列：NACE Code・Nace Code・Class Code・Economic Category Code・Input Sector code・gruppe_id・Geschäftsart ID・System ID・選択死因分類コード。
  - どれも古い陣のラベルが id。新しい陣（2 人のラベル＋裁定、LABEL_GUIDE v2.3 の B3）では同じ種類の列が category。**古いラベルと B3 の食い違い**で、直しの外れとは言い切れない。
- 合わせた見込み（使い済みの陣の上限の目安）：新しい 4 陣で、正しいが +0.3〜+1.3 ポイント。

## 4. 次
- 新しい陣（b112〜b123、run 41282225631）が揃ったら、2 人のラベル → 裁定 → E3 を固定 → 事前記録 → 1 回だけ測る。
- 事前記録の前にオーナーの了承をもらう（G と同じ）。
- 施設の「名称」の決まりは ChatGPT に相談する（ai-bridge）。決まりを変えるなら教材の付け直しが要る（オーナー承認）。
- 古い陣の B3 のラベル（NACE Code など）を今の決まりで見直すかも、ChatGPT に相談する。
