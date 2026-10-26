# ラベル用シート 003 / 003

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：road_number
- 例1 値：0006006 | 0000523 | 0000676 | 0000010 | 0000200
  - 同じ表の列：link_length, admin_class, ne_unique

## g0242（1 列）
- 見出し：link_length
- 例1 値：0.044000000000000004 | 12.21 | 0 | 0 | 0.75
  - 同じ表の列：road_number, admin_class, ne_unique

## g0243（1 列）
- 見出し：admin_class
- 例1 値：S | S | S | S | S
  - 同じ表の列：road_number, link_length, ne_unique

## g0244（1 列）
- 見出し：ne_unique
- 例1 値：JF002120 | JF001647 | JF001299 | JF001059 | 0000065,0120,B1
  - 同じ表の列：road_number, link_length, admin_class

## g0245（1 列）
- 見出し：MARITIME_ASSET_ID
- 例1 値：NSP001 | CBW117 | CBW210 | SBB003 | NML426
  - 同じ表の列：PURPOSE, TYPE, POSITION_ACCURACY

## g0246（1 列）
- 見出し：PURPOSE
- 例1 値：Aid to Navigation | Aid to Navigation | Aid to Navigation | Aid to Navigation | Aid to Navigation
  - 同じ表の列：MARITIME_ASSET_ID, TYPE, POSITION_ACCURACY

## g0247（1 列）
- 見出し：TYPE
- 例1 値：475 | 302 | 212 | 501 | 503
  - 同じ表の列：MARITIME_ASSET_ID, PURPOSE, POSITION_ACCURACY

## g0248（1 列）
- 見出し：POSITION_ACCURACY
- 例1 値：Survey DGPS | Non-DGPS (Contractor) | Non-DGPS (Contractor) | Survey DGPS | Unknown
  - 同じ表の列：MARITIME_ASSET_ID, PURPOSE, TYPE

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
```
