# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Minister
- 例1 値：Secretary of State: The Rt Hon Ed Milib… | Minister of State: Lord Davies of Abers… | Secretary of State: The Rt Hon Shaun Wo… | Parliamentary Under Secretary of State:… | Minister for the Olympics and Paymaster…
  - 同じ表の列：Date of Trip, Destination, Purpose, No.32 (The Royal Sq…, Number of officials…, Total Cost includin…

## g0002（1 列）
- 見出し：Date of Trip
- 例1 値：27-28 April 2009 | 14-15 October 2009 | 27-28 May 2009 | 7-8 September 2009 | 7-8 May 2009
  - 同じ表の列：Minister, Destination, Purpose, No.32 (The Royal Sq…, Number of officials…, Total Cost includin…

## g0003（1 列）
- 見出し：Destination
- 例1 値：Brussels | Abu Dhabi, Dubai and Qatar | Tripoli, Libya | Washington DC, USA | Copenhagen, Denmark
  - 同じ表の列：Minister, Date of Trip, Purpose, No.32 (The Royal Sq…, Number of officials…, Total Cost includin…

## g0004（1 列）
- 見出し：Purpose
- 例1 値：World Gas Conference | D-Day Celebrations | G8 Foreign Ministers' Meeting | Ministerial Visit on Preventing Extremi… | ASEAN Conference
  - 同じ表の列：Minister, Date of Trip, Destination, No.32 (The Royal Sq…, Number of officials…, Total Cost includin…

## g0005（1 列）
- 見出し：No.32 (The Royal Squadron)' or 'other RAF' or 'Charter' or
- 例1 値：Charter | Scheduled | Charter | Scheduled | Eurostar
  - 同じ表の列：Minister, Date of Trip, Destination, Purpose, Number of officials…, Total Cost includin…

## g0006（1 列）
- 見出し：Number of officials accompanying Ministers (where non-schedu
- 例1 値：18 | 2 | 18 | 4 | 31
  - 同じ表の列：Minister, Date of Trip, Destination, Purpose, No.32 (The Royal Sq…, Total Cost includin…

## g0007（1 列）
- 見出し：Total Cost including travel and accommodation of Minister on
- 例1 値：£5,422 | £872 | £623 | £8,626 | £695
  - 同じ表の列：Minister, Date of Trip, Destination, Purpose, No.32 (The Royal Sq…, Number of officials…

## g0008（1 列）
- 見出し：Domestic Energy Consumption in Plymouth - 2011 updated 201
- 例1 値：Consumption of Ordinary Domestic Electr… | Number of Domestic Gas meters | Average Consumption of Ordinary Domesti… | Average Consumption of Domestic Gas | Number of Economy 7 Domestic Electricit…
  - 同じ表の列：Method of Counting, Type of Measurement, Plymouth Unitary Au…, South West Region, England

## g0009（1 列）
- 見出し：Method of Counting
- 例1 値：Count | Count | Count | Count | Count
  - 同じ表の列：Domestic Energy Con…, Type of Measurement, Plymouth Unitary Au…, South West Region, England

## g0010（1 列）
- 見出し：Type of Measurement
- 例1 値：Meter Points | Meter Points | Megawatt Hours | Megawatt Hours | Meter Points
  - 同じ表の列：Domestic Energy Con…, Method of Counting, Plymouth Unitary Au…, South West Region, England

## g0011（1 列）
- 見出し：Plymouth Unitary Authority
- 例1 値：1045559 | 1473507 | 3540 | 102624 | 12982
  - 同じ表の列：Domestic Energy Con…, Method of Counting, Type of Measurement, South West Region, England

## g0012（1 列）
- 見出し：South West Region
- 例1 値：12425 | 6668 | 2713654 | 406988 | 7758029
  - 同じ表の列：Domestic Energy Con…, Method of Counting, Type of Measurement, Plymouth Unitary Au…, England

## g0013（1 列）
- 見出し：England
- 例1 値：371756954 | 019586188 | 070428614 | 000003777 | 000005478
  - 同じ表の列：Domestic Energy Con…, Method of Counting, Type of Measurement, Plymouth Unitary Au…, South West Region

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
g0013	
```
