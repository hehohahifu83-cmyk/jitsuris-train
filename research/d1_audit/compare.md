# D1 の抜き取り：ChatGPT と Claude の比べ（b066〜b083）

| 陣 | 抜き取り | 一致 | 食い違い |
|---|---:|---:|---:|
| b066 | 24 | 5 | 19 |
| b067 | 35 | 33 | 2 |
| b068 | 10 | 6 | 4 |
| b069 | 10 | 10 | 0 |
| b070 | 10 | 9 | 1 |
| b071 | 24 | 20 | 4 |
| b072 | 29 | 26 | 3 |
| b073 | 35 | 30 | 5 |
| b074 | 24 | 20 | 4 |
| b075 | 10 | 10 | 0 |
| b076 | 10 | 9 | 1 |
| b077 | 10 | 10 | 0 |
| b078 | 15 | 14 | 1 |
| b079 | 10 | 10 | 0 |
| b080 | 10 | 10 | 0 |
| b081 | 16 | 14 | 2 |
| 計 | 282 | 236 | 46 |

| 陣 | グループ | ChatGPT | Claude |
|---|---|---|---|
| b066 | g0004 | address | S |
| b066 | g0011 | category | S |
| b066 | g0013 | amount | S |
| b066 | g0038 | category | S |
| b066 | g0043 | S | id |
| b066 | g0052 | S | category |
| b066 | g0068 | address | S |
| b066 | g0083 | amount | S |
| b066 | g0089 | quantity | org |
| b066 | g0094 | amount | quantity |
| b066 | g0109 | category | quantity |
| b066 | g0113 | category | quantity |
| b066 | g0148 | amount | S |
| b066 | g0153 | account | S |
| b066 | g0155 | category | S |
| b066 | g0168 | text | S |
| b066 | g0195 | rate | date |
| b066 | g0200 | id | date |
| b066 | g0203 | other | category |
| b067 | g0033 | org | address |
| b067 | g0083 | category | date |
| b068 | g0044 | S | address |
| b068 | g0055 | S | category |
| b068 | g0056 | S | category |
| b068 | g0060 | S | category |
| b070 | g0060 | quantity | other |
| b071 | g0162 | amount | S |
| b071 | g0168 | amount | S |
| b071 | g0232 | S | unknown |
| b071 | g0237 | S | unknown |
| b072 | g0068 | id | category |
| b072 | g0118 | S | category |
| b072 | g0273 | category | id |
| b073 | g0002 | org | address |
| b073 | g0112 | unknown | address |
| b073 | g0170 | quantity | S |
| b073 | g0174 | rate | S |
| b073 | g0209 | quantity | S |
| b074 | g0087 | S | date |
| b074 | g0088 | S | category |
| b074 | g0134 | id | category |
| b074 | g0209 | id | category |
| b076 | g0020 | amount | unknown |
| b078 | g0117 | category | id |
| b081 | g0028 | text | S |
| b081 | g0092 | org | S |

## Claude の裁定（2026-10-31）
食い違いを LABEL_GUIDE v2.3 で裁定し、ChatGPT の誤りを数えた（ChatGPT が正しいと判断したものは誤りに数えない）。

| 陣 | 抜き取り | ChatGPT の誤り | 率 | 5% を超える → 全部を見直す |
|---|---:|---:|---:|---|
| b066 | 24 | 19 | 79% | **見直す** |
| b067 | 35 | 2 | 5.7% | **見直す** |
| b068 | 10 | 0 | 0% | |
| b069 | 10 | 0 | 0% | |
| b070 | 10 | 1 | 10% | **見直す** |
| b071 | 24 | 2 | 8.3% | **見直す** |
| b072 | 29 | 1 | 3.4% | |
| b073 | 35 | 4 | 11% | **見直す** |
| b074 | 24 | 2 | 8.3% | **見直す** |
| b075〜b077・b079・b080 | 50 | 0 | 0% | |
| b076 | 10 | 0 | 0% | |
| b078 | 15 | 1 | 6.7% | **見直す** |
| b081 | 16 | 2 | 12.5% | **見直す** |

- ChatGPT が正しい：b068 の g0044・g0055・g0056・g0060（調査の個票 → S）、b071 の g0232・g0237（S。どちらも採点しない）、b072 の g0118（議員ごとの記録 → S）・g0273（話題のコード → category）、b073 の g0174（就職率 → rate）、b074 の g0087・g0088（離婚の 1 件ごとの記録 → S）、b076 の g0020（社会保障の支出 → amount）。
- Claude が正しい（ChatGPT の誤り）：
  - b066 の 19（上級職員の記録を S にしていない 6、Main department → quantity など列と合わないラベル）。
  - b067 の g0033（自治体名だけの Schulträger → address）・g0083（週の番号 → date）。
  - b070 の g0060（月平均 → other）。b071 の g0162・g0168（見出しの語が値に混ざる → S）。b072 の g0068（単位のコード → category）。
  - b073 の g0002（避難場所 → address、b090 と同じ）・g0112（観光地の英語名 → address）・g0170・g0209（表が崩れている → S）。
  - b074 の g0134・g0209（種類のコード・0/1 の印 → category）。b078 の g0117（区域の記号 → id）。b081 の g0028・g0092（表が崩れている → S）。
- 事前記録の決まりどおり、5% を超えた 8 陣（b066・b067・b070・b071・b073・b074・b078・b081）は全グループを Claude が見直す。
