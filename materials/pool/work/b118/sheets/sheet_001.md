# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ID
- 例1 値：ep2 | ep21 | ep22 | ep3 | ep26
  - 同じ表の列：DE, FR, IT, EN

## g0002（1 列）
- 見出し：DE
- 例1 値：ETO und Salmonellen | Mikrobiologie (STEC) | Mykotoxine, Mikrobiologie, Farbstoffe, … | verbotene Arzneistoffe und Kennzeichnung | Sudanfarbstoffe
  - 同じ表の列：ID, FR, IT, EN

## g0003（1 列）
- 見出し：FR
- 例1 値：Microbiologie (salmonelles et listérias) | Mycotoxines et salmonelles | Critères microbiologiques et chimiques … | Aflatoxines | Substances parfumantes allergisantes
  - 同じ表の列：ID, DE, IT, EN

## g0004（1 列）
- 見出し：IT
- 例1 値：Micotossine e salmonelle | Fragranze allergizzanti | Contaminazione con gli idrocarburi poli… | Salmonelle | Microbiologia
  - 同じ表の列：ID, DE, FR, EN

## g0005（1 列）
- 見出し：EN
- 例1 値：Unauthorised medicinal substances and l… | Norovirus | Sulphur dioxide and sulphites | Microbiology | Salmonella, irradiation, falsification,…
  - 同じ表の列：ID, DE, FR, IT

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
```
