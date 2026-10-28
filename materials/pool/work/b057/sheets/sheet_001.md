# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Commodity // Produit
- 例1 値：Dairy products // Produits laitiers | Dairy products // Produits laitiers | Dairy products // Produits laitiers | Dairy products // Produits laitiers | Dairy products // Produits laitiers
  - 同じ表の列：Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0002（1 列）
- 見出し：Sample Plan Number // Numero du plan d'echantillonnage
- 例1 値：2024_D210 | 2024_D210 | 2024_D221 | 2024_D207 | 2024_D210
  - 同じ表の列：Commodity // Produit, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0003（1 列）
- 見出し：Sample Plan Program // Programme du plan d'echantillonnage
- 例1 値：D207 | D221 | D210 | D210 | D221
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0004（1 列）
- 見出し：Domestic and/or Import // Canadien et/ou Importe
- 例1 値：Domestic // Canadien | Domestic // Canadien | Domestic // Canadien | Domestic // Canadien | Domestic // Canadien
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0005（1 列）
- 見出し：Product vs. Environmental // Produit ou Environnemental
- 例1 値：Product // Produit | Product // Produit | Product // Produit | Product // Produit | Product // Produit
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0006（1 列）
- 見出し：Job Laboratory Number // Tache - numero de laboratoire
- 例1 値：STH-FD-2024-MI-1651 | BUR-FI-2024-MI-00960 | STH-FD-2024-MI-1196 | STH-FD-2024-MI-1332 | STH-FD-2024-MI-1394
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Date Sampled YYYY/M…, Country of Origin /…, Production Practice…

## g0007（1 列）
- 見出し：Date Sampled YYYY/MM/DD // Date d'echantillonnage AAAA/MM/JJ
- 例1 値：2024-07-22 | 2024-05-23 | 2024-07-15 | 2024-05-21 | 2024-06-18
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Country of Origin /…, Production Practice…

## g0008（1 列）
- 見出し：Country of Origin // Pays d'Origine
- 例1 値：Canada | Canada | Canada | Germany // Allemagne | Canada
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Production Practice…

## g0009（1 列）
- 見出し：Production Practice // Methode de production
- 例1 値：Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle | Conventional // Conventionnelle
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…

## g0010（1 列）
- 見出し：Product Type // Type de produit
- 例1 値：Pasteurized Milk Cheese // Fromage de l… | Raw Milk Cheese // Fromage de lait cru | Pasteurized Milk Cheese // Fromage de l… | Raw Milk Cheese // Fromage de lait cru | Pasteurized Milk Cheese // Fromage de l…
  - 同じ表の列：Commodity // Produit, Sample Plan Number …, Sample Plan Program…, Domestic and/or Imp…, Product vs. Environ…, Job Laboratory Numb…, Date Sampled YYYY/M…, Country of Origin /…

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
```
