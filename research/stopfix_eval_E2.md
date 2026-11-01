# 止める段の直しの E2 での 1 回だけの測り（`research/stopfix_eval.py`）

- 事前記録 `bench/stopfix_prereg_20261101.md`。採点 1253 列。正解は 2 人のラベルの裁定（answers_final）。fixes.py SHA-256 d25c3dae6286e57c77d08fd08d7ef47f3a250f8fc8cc803dcfa7239d24f4daa3。

| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |
|---|---:|---:|---:|---:|---|
| P | 89.84% | 6.07% | 2 | 4.04% | 1124・1129・1124 |
| P+G | 90.42% | 5.40% | 1 | 4.15% | 1131・1136・1132 |

## 決まり 1〜4

- 1. 正しい +0.59 ○
- 2. 重大 -1 ○
- 3. ほかの誤り +0.11 ○
- 4. 90% 区間 +0.16〜+1.12 ○
- **判定：確かめられた（採る）**

## 直しが変えた列（3 本）

| 本 | id | 列名 | 正解 | P | P+G |
|---|---|---|---|---|---|
| 1 | b100-0140 | hh_typ_nr | category | unknown | id |
| 1 | b100-0142 | einheit_nr | category | unknown | id |
| 1 | b103-0465 | 指定日 | date | unknown | date |
| 1 | b106-0007 | AUDIT_YEAR | date | unknown | date |
| 1 | b108-0125 | Persons with disabilities
Personnes | rate | unknown | rate |
| 1 | b110-0057 | PCT_COMPOSITE_CLASS_STUDENTS_14 | rate | unknown | rate |
| 1 | b110-0060 | PCT_COMPOSITE_CLASSES_15 | rate | unknown | rate |
| 1 | b110-0061 | PCT_COMPOSITE_CLASS_STUDENTS_15 | rate | unknown | rate |
| 1 | b110-0066 | end_month | date | unknown | date |
| 2 | b100-0142 | einheit_nr | category | unknown | id |
| 2 | b103-0465 | 指定日 | date | unknown | date |
| 2 | b106-0007 | AUDIT_YEAR | date | unknown | date |
| 2 | b108-0125 | Persons with disabilities
Personnes | rate | unknown | rate |
| 2 | b110-0057 | PCT_COMPOSITE_CLASS_STUDENTS_14 | rate | unknown | rate |
| 2 | b110-0060 | PCT_COMPOSITE_CLASSES_15 | rate | unknown | rate |
| 2 | b110-0061 | PCT_COMPOSITE_CLASS_STUDENTS_15 | rate | unknown | rate |
| 2 | b110-0066 | end_month | date | unknown | date |
| 3 | b100-0142 | einheit_nr | category | unknown | id |
| 3 | b103-0465 | 指定日 | date | unknown | date |
| 3 | b106-0007 | AUDIT_YEAR | date | unknown | date |
| 3 | b108-0125 | Persons with disabilities
Personnes | rate | unknown | rate |
| 3 | b110-0056 | PCT_COMPOSITE_CLASSES_14 | rate | quantity | unknown |
| 3 | b110-0057 | PCT_COMPOSITE_CLASS_STUDENTS_14 | rate | unknown | rate |
| 3 | b110-0058 | COMPOSITE_CLASS_COUNT_15 | quantity | unknown | quantity |
| 3 | b110-0060 | PCT_COMPOSITE_CLASSES_15 | rate | unknown | rate |
| 3 | b110-0061 | PCT_COMPOSITE_CLASS_STUDENTS_15 | rate | unknown | rate |
| 3 | b110-0066 | end_month | date | unknown | date |
