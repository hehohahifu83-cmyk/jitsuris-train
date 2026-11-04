# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0002（1 列）
- 見出し：8788_GREEN
- 例1 値：50.28 | -100.00 | 27.24 | 41.68 | 34.88
  - 同じ表の列：SUBURB, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN, 9091_COVER

## g0003（1 列）
- 見出し：8788_COVER
- 例1 値：93.87 | 0.00 | 94.74 | 24.57 | 20.84
  - 同じ表の列：SUBURB, 8788_GREEN, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN, 9091_COVER

## g0004（1 列）
- 見出し：8889_GREEN
- 例1 値：-100.00 | -100.00 | -100.00 | -100.00 | -100.00
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN, 9091_COVER

## g0005（1 列）
- 見出し：8889_COVER
- 例1 値：0.00 | 0.00 | 0.00 | 0.00 | 0.00
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8990_GREEN, 8990_COVER, 9091_GREEN, 9091_COVER

## g0006（1 列）
- 見出し：8990_GREEN
- 例1 値：-100.00 | -100.00 | -100.00 | -100.00 | -100.00
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_COVER, 9091_GREEN, 9091_COVER

## g0007（1 列）
- 見出し：8990_COVER
- 例1 値：0.00 | 0.00 | 0.00 | 0.00 | 0.00
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 9091_GREEN, 9091_COVER

## g0008（1 列）
- 見出し：9091_GREEN
- 例1 値：24.11 | 18.45 | 32.98 | 12.96 | 35.44
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_COVER

## g0009（1 列）
- 見出し：9091_COVER
- 例1 値：97.06 | 63.54 | 92.57 | 83.52 | 53.59
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN

## g0010（1 列）
- 見出し：9192_GREEN
- 例1 値：-100.00 | -100.00 | -100.00 | -100.00 | -100.00
  - 同じ表の列：SUBURB, 8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN

## g0011（1 列）
- 見出し：2002/03
- 例1 値：2003/04 Total | 2010/11 Total | 2009/10 | 2003/04 | 2007/08
  - 同じ表の列：PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 24140, 2002/03_3, 566553, 91980396

## g0012（1 列）
- 見出し：PARRAMATTA RD AUBURN EASTBOUND
- 例1 値：VICTORIA ROAD RYDE (Z) EASTBOUND | HINTERLAND WAY EWINGSDALE NORTHBOUND | CROSS CITY TUNNEL EAST SYDNEY WESTBOUND | PACIFIC HIGHWAY WAHROONGA (Z) NORTHBOUND | EASTERN DISTRIBUTOR DARLINGHURST NORTHB…
  - 同じ表の列：2002/03, 2818701, 2002/03_2, 2010, 24140, 2002/03_3, 566553, 91980396

## g0013（1 列）
- 見出し：2818701
- 例1 値：1935821 | 2222194 | 1577396 | 810882 | 891591
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2002/03_2, 2010, 24140, 2002/03_3, 566553, 91980396

## g0014（1 列）
- 見出し：2002/03_2
- 例1 値：2012/13 | 2004/05 Total | 2014/15 Total | 2003/04 Total | 2013/14 Total
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2010, 24140, 2002/03_3, 566553, 91980396

## g0015（1 列）
- 見出し：2010
- 例1 値：2472 | 2145 | 2076 | 2144 | 2138
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 24140, 2002/03_3, 566553, 91980396

## g0016（1 列）
- 見出し：24140
- 例1 値：10308 | 14987 | 19245 | 11960 | 28687
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 2002/03_3, 566553, 91980396

## g0017（1 列）
- 見出し：2002/03_3
- 例1 値：2013/14 | 2003/04 | 2012/13 | 2004/05 | 2007/08
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 24140, 566553, 91980396

## g0018（1 列）
- 見出し：566553
- 例1 値：8931895 | 661987 | 627281 | 603831 | 694199
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 24140, 2002/03_3, 91980396

## g0019（1 列）
- 見出し：91980396
- 例1 値：87592900 | 123395103 | 117421716 | 137589951 | 147812318
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 24140, 2002/03_3, 566553

## g0020（1 列）
- 見出し：162.35091156520221
- 例1 値：237.31292179908067 | 163.57498189962942 | 234.55773300684152 | 144.88868191705552 | 164.78821060859744
  - 同じ表の列：2002/03, PARRAMATTA RD AUBUR…, 2818701, 2002/03_2, 2010, 24140, 2002/03_3, 566553

## g0021（1 列）
- 見出し：bridge type
- 例1 値：ROAD OVER PERENNIAL WATERCOURSE | ROAD OVER SEASONAL WATERCOURSE | ROAD OVER SEASONAL WATERCOURSE | ROAD OVER IRRIGATION CHANNEL | ROAD OVER IRRIGATION CHANNEL
  - 同じ表の列：STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT, REGION_PHYS

## g0022（1 列）
- 見出し：STRUCTURE_FORM
- 例1 値：BRIDGES | BRIDGES | BRIDGES | BRIDGES | MAJOR CULVERTS
  - 同じ表の列：bridge type, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT, REGION_PHYS

## g0023（1 列）
- 見出し：STRUCTURE_TYPE
- 例1 値：IN-SITU BOX CULVERT | CIRCULAR PIPE | NULL | PRECAST CROWN UNITS | IN-SITU BOX CULVERT
  - 同じ表の列：bridge type, STRUCTURE_FORM, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT, REGION_PHYS

## g0024（1 列）
- 見出し：TRAFFIC_WIDTH
- 例1 値：NULL | NULL | 28.6 | 13.2 | NULL
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT, REGION_PHYS

## g0025（1 列）
- 見出し：YEAR_CONSTRUCTED
- 例1 値：30/06/1982 | 23748 | 30/06/1976 | 30/06/1950 | 30/06/1970
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, CD_DIRECTION, LAT, LONGIT, REGION_PHYS

## g0026（1 列）
- 見出し：CD_DIRECTION
- 例1 値：R | R | B | F | F
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, LAT, LONGIT, REGION_PHYS

## g0027（1 列）
- 見出し：LAT
- 例1 値：-36.91843 | -37.79594 | -37.84912 | -37.8955 | -36.6631
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LONGIT, REGION_PHYS

## g0028（1 列）
- 見出し：LONGIT
- 例1 値：143.108131 | 142.07633 | 144.24753 | 145.37971 | 145.50265
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, REGION_PHYS

## g0029（1 列）
- 見出し：REGION_PHYS
- 例1 値：HUME | GIPPSLAND | LODDON MALLEE | GIPPSLAND | GIPPSLAND
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT

## g0030（1 列）
- 見出し：STRUCTURE_STATUS
- 例1 値：Structure Open | Structure Open | Structure Open | Structure Open | Structure Open
  - 同じ表の列：bridge type, STRUCTURE_FORM, STRUCTURE_TYPE, TRAFFIC_WIDTH, YEAR_CONSTRUCTED, CD_DIRECTION, LAT, LONGIT

## g0031（1 列）
- 見出し：Date
- 例1 値：21/05/2011 | 21/09/2016 | 2/02/2011 | 26/03/2009 | 18/07/2011
  - 同じ表の列：PTP03 Port Pirie We…, PTP05 Port Pirie Fr…

## g0032（1 列）
- 見出し：PTP03 Port Pirie West TSP Lead ug/m3
- 例1 値：0.14 | 0.81 | 0.13 | 1.86 | 0.3
  - 同じ表の列：Date, PTP05 Port Pirie Fr…

## g0033（1 列）
- 見出し：PTP05 Port Pirie Frank Green Park TSP ug/m3
- 例1 値：0.02 | 0.56 | 0.34 | 0.06 | 0.11
  - 同じ表の列：Date, PTP03 Port Pirie We…

## g0034（1 列）
- 見出し：Date/Time (AEST)
- 例1 値：2026-01-18T20:00 | 2026-01-21T08:00 | 2026-01-04T00:00 | 2026-01-12T02:30 | 2026-01-07T03:00
  - 同じ表の列：Hs (m), Hmax (m), Tz (s), Tp (s), Peak Direction (deg…, SST (degrees C)

## g0035（1 列）
- 見出し：Hs (m)
- 例1 値：0.76 | 1.146 | 2.899 | 1.52 | 1.481
  - 同じ表の列：Date/Time (AEST), Hmax (m), Tz (s), Tp (s), Peak Direction (deg…, SST (degrees C)

## g0036（1 列）
- 見出し：Hmax (m)
- 例1 値：2.593 | 2.351 | 2.559 | 2.68 | 1.248
  - 同じ表の列：Date/Time (AEST), Hs (m), Tz (s), Tp (s), Peak Direction (deg…, SST (degrees C)

## g0037（1 列）
- 見出し：Tz (s)
- 例1 値：6.18 | 6.479 | 7.448 | 5.176 | 6.649
  - 同じ表の列：Date/Time (AEST), Hs (m), Hmax (m), Tp (s), Peak Direction (deg…, SST (degrees C)

## g0038（1 列）
- 見出し：Tp (s)
- 例1 値：7.143 | 8 | 9.091 | 5.405 | 8.333
  - 同じ表の列：Date/Time (AEST), Hs (m), Hmax (m), Tz (s), Peak Direction (deg…, SST (degrees C)

## g0039（1 列）
- 見出し：Peak Direction (degrees)
- 例1 値：65.03 | 75.14 | 110.72 | 134.86 | 70.31
  - 同じ表の列：Date/Time (AEST), Hs (m), Hmax (m), Tz (s), Tp (s), SST (degrees C)

## g0040（1 列）
- 見出し：SST (degrees C)
- 例1 値：26.13 | 26.74 | 26.03 | 26.74 | 26.89
  - 同じ表の列：Date/Time (AEST), Hs (m), Hmax (m), Tz (s), Tp (s), Peak Direction (deg…

## g0042（1 列）
- 見出し：site_code
- 例1 値：R010161 | R904232 | R808500 | R902038 | R904452
  - 同じ表の列：ref, program, asset_type, works_type, location, from_, extent, year

## g0043（1 列）
- 見出し：program
- 例1 値：Footpath Program | Kerb Program | Sealing Program | Sealing Program | Kerb Program
  - 同じ表の列：ref, site_code, asset_type, works_type, location, from_, extent, year

## g0044（1 列）
- 見出し：asset_type
- 例1 値：Kerb and Channel | Roads | Roads | Kerb and Channel | Kerb and Channel
  - 同じ表の列：ref, site_code, program, works_type, location, from_, extent, year

## g0045（1 列）
- 見出し：works_type
- 例1 値：Replace | Spray Seal Overlay | Replace | Replace | Replace
  - 同じ表の列：ref, site_code, program, asset_type, location, from_, extent, year

## g0046（1 列）
- 見出し：location
- 例1 値：Francis Street (Tatura) | Stevenson Street (Murchison) | Coomboona Road | Albert Street (Tatura) | Corio Street (Shepparton)
  - 同じ表の列：ref, site_code, program, asset_type, works_type, from_, extent, year

## g0047（1 列）
- 見出し：from_
- 例1 値：ECHUCA/MOOROOPNA | JOHN STREET | HOGAN STREET | ALBERT | WILMOT ROAD
  - 同じ表の列：ref, site_code, program, asset_type, works_type, location, extent, year

## g0048（1 列）
- 見出し：extent
- 例1 値：Minimum extent of works | Minimum extent of works | Minimum extent of works | Minimum extent of works | Minimum extent of works
  - 同じ表の列：ref, site_code, program, asset_type, works_type, location, from_, year

## g0049（1 列）
- 見出し：year
- 例1 値：2018/19 | 2020/21 | 2018/19 | 2020/21 | 2018/19
  - 同じ表の列：ref, site_code, program, asset_type, works_type, location, from_, extent

## g0050（1 列）
- 見出し：status
- 例1 値：Programmed | Programmed | Programmed | Programmed | Programmed
  - 同じ表の列：ref, site_code, program, asset_type, works_type, location, from_, extent

## g0052（1 列）
- 見出し：num_of
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：ref, material, accessible

## g0054（1 列）
- 見出し：accessible
- 例1 値：Yes | No | Not Applicable | Yes | Yes
  - 同じ表の列：ref, num_of, material

## g0055（1 列）
- 見出し：Location
- 例1 値：Newport Lakes | Hatt Reserve | Donald McLean Reserve | Charles Bates Reserve | Altona Meadows Community Park
  - 同じ表の列：Suburb

## g0056（1 列）
- 見出し：Location
- 例1 値：The Spit Reserve | Altona Coastal Park | Donald McLean Reserve | Williamstown Cricket & Football Ground | Gloucester Reserve
  - 同じ表の列：Suburb, Seat_Type, SeatMaterial

## g0057（1 列）
- 見出し：Suburb
- 例1 値：NEWPORT | NEWPORT | WILLIAMSTOWN | ALTONA | WILLIAMSTOWN
  - 同じ表の列：Location, Seat_Type, SeatMaterial

## g0058（1 列）
- 見出し：Seat_Type
- 例1 値：Bench | Bench | Seat | Bench | Seat
  - 同じ表の列：Location, Suburb, SeatMaterial

## g0059（1 列）
- 見出し：SeatMaterial
- 例1 値：Timber/Steel | Timber/Steel | Timber/Steel | Timber/Steel | Timber/Steel
  - 同じ表の列：Location, Suburb, Seat_Type

## g0060（1 列）
- 見出し：Location
- 例1 値：Carlsson, C.W. Reserve | Bruce Comben Reserve | Apex Park | Carinza Reserve | Altona Green Park
  - 同じ表の列：Suburb, Feature_Type, Heightm, Lengthm, FenceMaterial

## g0061（1 列）
- 見出し：Feature_Type
- 例1 値：Chain Link Fence | Post & Rail Fence | Post & Wire Fence | Pipe Rail Fence | Post & Rail Fence
  - 同じ表の列：Location, Suburb, Heightm, Lengthm, FenceMaterial

## g0062（1 列）
- 見出し：Heightm
- 例1 値：0.60 | 1.20 | 1.00 | 0.40 | 0.50
  - 同じ表の列：Location, Suburb, Feature_Type, Lengthm, FenceMaterial

## g0063（1 列）
- 見出し：Lengthm
- 例1 値：1.40 | 2.70 | 2.00 | 3.10 | 2.30
  - 同じ表の列：Location, Suburb, Feature_Type, Heightm, FenceMaterial

## g0064（1 列）
- 見出し：FenceMaterial
- 例1 値：Steel Chain/Steel | Wire Mesh/T-Pine | Timber | Timber | Steel
  - 同じ表の列：Location, Suburb, Feature_Type, Heightm, Lengthm

## g0065（1 列）
- 見出し：Metropolitan or Regional
- 例1 値：Metropolitan | Regional
  - 同じ表の列：City or Town, Legal Aid Office, CLC, Indigenous Legal Ai…, ICC's

## g0066（1 列）
- 見出し：City or Town
- 例1 値：Launceston | Devonport | Hobart | Burnie
  - 同じ表の列：Metropolitan or Reg…, Legal Aid Office, CLC, Indigenous Legal Ai…, ICC's

## g0067（1 列）
- 見出し：Legal Aid Office
- 例1 値：Head Office | Regional branch | Regional branch
  - 同じ表の列：Metropolitan or Reg…, City or Town, CLC, Indigenous Legal Ai…, ICC's

## g0068（1 列）
- 見出し：CLC
- 例1 値：Women's Legal Service (Tas) Inc | Environmental Defenders Office (Tas) Inc | Tenants' Union of Tasmania Inc | North West Community Legal Centre | Launceston Community Legal Centre
  - 同じ表の列：Metropolitan or Reg…, City or Town, Legal Aid Office, Indigenous Legal Ai…, ICC's

## g0069（1 列）
- 見出し：Indigenous Legal Aid Providers
- 例1 値：Tasmanian Aboriginal Centre Incorporated
  - 同じ表の列：Metropolitan or Reg…, City or Town, Legal Aid Office, CLC, ICC's

## g0070（1 列）
- 見出し：ICC's
- 例1 値：ICC
  - 同じ表の列：Metropolitan or Reg…, City or Town, Legal Aid Office, CLC, Indigenous Legal Ai…

## g0071（1 列）
- 見出し：Town
- 例1 値：Nagambie | Nagambie | Nagambie | Euroa | Nagambie
  - 同じ表の列：Number, Descript

## g0072（1 列）
- 見出し：Number
- 例1 値：1 | 10 | 15 | 9 | 6
  - 同じ表の列：Town, Descript

## g0073（1 列）
- 見出し：Descript
- 例1 値：Passive Irrigation Opportunities | Passive Irrigation Opportunities | Passive Irrigation Opportunities | Passive Irrigation Opportunities | Passive Irrigation Opportunities
  - 同じ表の列：Town, Number

## 答えの雛形

```
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
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0052	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
```
