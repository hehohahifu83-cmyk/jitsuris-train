# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Minister
- 例1 値：Parliamentary Secretary (Minister for C… | Minister of State, The Rt Hon Oliver Le… | Minister for the Cabinet Office, Paymas… | Parliamentary Secretary (Minister for P… | Minister without Portfolio, The Rt Hon …
  - 同じ表の列：Date of Trip, Destination, Purpose, No.32 (The Royal Sq…, Total Cost includin…

## g0002（1 列）
- 見出し：Date of Trip
- 例1 値：16-20 July 2010 | nil return | nil return | nil return | 10-11 July 2010
  - 同じ表の列：Minister, Destination, Purpose, No.32 (The Royal Sq…, Total Cost includin…

## g0003（1 列）
- 見出し：Destination
- 例1 値：Islamabad,Pakistan | Srebenica, Bosnia
  - 同じ表の列：Minister, Date of Trip, Purpose, No.32 (The Royal Sq…, Total Cost includin…

## g0004（1 列）
- 見出し：Purpose
- 例1 値：15th Anniversary of Srebenica massacre | Met senior members of the Pakistani Gov…
  - 同じ表の列：Minister, Date of Trip, Destination, No.32 (The Royal Sq…, Total Cost includin…

## g0005（1 列）
- 見出し：No.32 (The Royal Squadron)' or 'other RAF' or 'Charter' or
- 例1 値：Scheduled | Scheduled
  - 同じ表の列：Minister, Date of Trip, Destination, Purpose, Total Cost includin…

## g0006（1 列）
- 見出し：Total Cost including travel and accommodation of Minister on
- 例1 値：」1,296 | 」415
  - 同じ表の列：Minister, Date of Trip, Destination, Purpose, No.32 (The Royal Sq…

## g0007（1 列）
- 見出し：Minister
- 例1 値：Minister of State, The Rt Hon Oliver Le… | Minister without Portfolio, The Rt Hon … | Minister for the Cabinet Office, Paymas… | Parliamentary Secretary (Minister for P… | Does not normally include meetings with…
  - 同じ表の列：Date, Purpose of meeting

## g0008（1 列）
- 見出し：Date
- 例1 値：June, 2010 | July, 2010 | July, 2010 | July, 2010 | July, 2010
  - 同じ表の列：Minister, Purpose of meeting

## g0009（1 列）
- 見出し：Purpose of meeting
- 例1 値：Environmental regulation | Meeting on Gift Aid | Roundtable to discuss employee led mutu… | Procurement issues | Contract Renegotiation
  - 同じ表の列：Minister, Date

## g0010（1 列）
- 見出し：Minister
- 例1 値：Minister for the Cabinet Office and Pay… | Does not normally include attendance at… | Parliamentary Secretary (Minister for C… | Minister without Portfolio, The Rt Hon … | Parliamentary Secretary (Minister for P…
  - 同じ表の列：Date of Hospitality, Type of hospitality…

## g0011（1 列）
- 見出し：Date of Hospitality
- 例1 値：30-Jun-2010 | 06-Jul-2010 | nil return | nil return | 17-Jun-2010
  - 同じ表の列：Minister, Type of hospitality…

## g0012（1 列）
- 見出し：Type of hospitality received
- 例1 値：Dinner | Lunch | Lunch | Dinner | Dinner
  - 同じ表の列：Minister, Date of Hospitality

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
```
