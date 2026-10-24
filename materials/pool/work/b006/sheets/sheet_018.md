# ラベル用シート 018 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_018.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g2041（1 列）
- 見出し：one_way
- 例1 値：f | f | f | f | f
  - 同じ表の列：main_id, dist, start_time, end_time, side, from, to, miles

## g2042（1 列）
- 見出し：week_1
- 例1 値：f | f | t | t | t
  - 同じ表の列：main_id, dist, start_time, end_time, side, from, to, miles

## g2043（1 列）
- 見出し：case_no
- 例1 値：CE944733 | CE945124 | CE945065 | CE945549 | CE945158
  - 同じ表の列：ticket_no, status_dttm, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g2044（1 列）
- 見出し：ticket_no
- 例1 値：CTDS2H03 | GFV1G015 | JGK2M704 | N9FQEC13 | V7V4CF06
  - 同じ表の列：case_no, status_dttm, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g2045（1 列）
- 見出し：status_dttm
- 例1 値：2026-10-19 11:00:00 | 2026-10-20 06:47:00 | 2026-10-22 02:59:00 | 2026-10-20 11:45:00 | 2026-10-21 02:10:00
  - 同じ表の列：case_no, ticket_no, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g2046（1 列）
- 見出し：code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：case_no, ticket_no, status_dttm, status, value, violation_stno, violation_sthigh, violation_suffix

## g2047（1 列）
- 見出し：value
- 例1 値：25 | 25 | 25 | 25 | 25
  - 同じ表の列：case_no, ticket_no, status_dttm, status, code, violation_stno, violation_sthigh, violation_suffix

## g2048（1 列）
- 見出し：violation_stno
- 例1 値：393 | 884 | 15 | 977 | 11
  - 同じ表の列：case_no, ticket_no, status_dttm, status, code, value, violation_sthigh, violation_suffix

## g2049（1 列）
- 見出し：violation_sthigh
- 例1 値：11 | 1740 | 10 | 6 | 248
  - 同じ表の列：case_no, ticket_no, status_dttm, status, code, value, violation_stno, violation_suffix

## g2050（1 列）
- 見出し：violation_suffix
- 例1 値：ST | ST | ST | ST | ST
  - 同じ表の列：case_no, ticket_no, status_dttm, status, code, value, violation_stno, violation_sthigh

## g2051（1 列）
- 見出し：violation_city
- 例1 値：Boston | Mission Hill | Boston | Allston | Brighton
  - 同じ表の列：case_no, ticket_no, status_dttm, status, code, value, violation_stno, violation_sthigh

## g2052（1 列）
- 見出し：Neighborhood
- 例1 値：MISSION HILL/FENWAY | EAST BOSTON | MISSION HILL/FENWAY | SOUTH DORCHESTER/MATTAPAN | NORTH END/BEACON HILL
  - 同じ表の列：Intersection, From, To, Permittee, Contractor, Permit, Project_Category, Construction_Notes

## g2053（1 列）
- 見出し：Intersection
- 例1 値：BOLTON ST | BIGELOW ST | BEACH ST | HOLBORN ST | FRANKLIN ST
  - 同じ表の列：Neighborhood, From, To, Permittee, Contractor, Permit, Project_Category, Construction_Notes

## g2054（1 列）
- 見出し：From
- 例1 値：BAY ST | RIVER ST | WEST SEVENTH ST | LINCOLN ST | Mattakeesett
  - 同じ表の列：Neighborhood, Intersection, To, Permittee, Contractor, Permit, Project_Category, Construction_Notes

## g2055（1 列）
- 見出し：To
- 例1 値：SAVIN HILL AV | END | SHELBY ST | CHELSEA ST | END
  - 同じ表の列：Neighborhood, Intersection, From, Permittee, Contractor, Permit, Project_Category, Construction_Notes

## g2056（1 列）
- 見出し：Permittee
- 例1 値：Comcast | Vicinity Energy Co | Boston Public Works Department ( | National Grid | BWSC - Boston Water And Sewer Co
  - 同じ表の列：Neighborhood, Intersection, From, To, Contractor, Permit, Project_Category, Construction_Notes

## g2057（1 列）
- 見出し：Contractor
- 例1 値：Maverick Construction | National Grid | National Grid | National Grid | Northern Drill Service, In
  - 同じ表の列：Neighborhood, Intersection, From, To, Permittee, Permit, Project_Category, Construction_Notes

## g2058（1 列）
- 見出し：Permit
- 例1 値：EXCA-1839318 | EXCA-1883598 | SINKHOLE | EXCA-1880058 | EXCA-1844093
  - 同じ表の列：Neighborhood, Intersection, From, To, Permittee, Contractor, Project_Category, Construction_Notes

## g2059（1 列）
- 見出し：Project_Category
- 例1 値：CAPITAL | SERVICE | EMERGENCY | POINT REPAIR | SERVICE
  - 同じ表の列：Neighborhood, Intersection, From, To, Permittee, Contractor, Permit, Construction_Notes

## g2060（1 列）
- 見出し：Construction_Notes
- 例1 値：INSTALLATION OF GAS MAIN | GATE BOX REPAIR | Service Repair (Leak on Service) | INSTALLATION OF GAS MAIN AND SERVICES | Emergency - Cable Repair
  - 同じ表の列：Neighborhood, Intersection, From, To, Permittee, Contractor, Permit, Project_Category

## g2061（1 列）
- 見出し：Work_Schedule
- 例1 値：Days & Weekends | Days & Weekends | Days & Weekends | Days & Weekends | Days & Weekends
  - 同じ表の列：Neighborhood, Intersection, From, To, Permittee, Contractor, Permit, Project_Category

## g2062（1 列）
- 見出し：dispatch_ts
- 例1 値：2017-07-30 12:02:41+00 | 2023-04-15 15:31:46+00 | 2018-07-14 15:48:34+00 | 2026-06-20 01:12:56+00 | 2025-12-06 04:21:28+00
  - 同じ表の列：mode_type, location_type, xstreet2, x_cord, y_cord, lat

## g2063（2 列）
- 見出し：mode_type
- 例1 値：ped | mv | mv | mv | bike
  - 同じ表の列：dispatch_ts, location_type, xstreet2, x_cord, y_cord, lat
- 例2 値：bike | mv | ped | ped | mv
  - 同じ表の列：date_time, location_type, xstreet1, xstreet2, x_cord, y_cord, long, lat

## g2064（2 列）
- 見出し：location_type
- 例1 値：Intersection | Intersection | Intersection | Other | Street
  - 同じ表の列：dispatch_ts, mode_type, xstreet2, x_cord, y_cord, lat
- 例2 値：Street | Intersection | Intersection | Intersection | Street
  - 同じ表の列：date_time, mode_type, xstreet1, xstreet2, x_cord, y_cord, long, lat

## g2065（2 列）
- 見出し：xstreet2
- 例1 値：GEORGE ST | MORTON ST | NAVARRE ST | BEALE ST | DEAD END
  - 同じ表の列：dispatch_ts, mode_type, location_type, x_cord, y_cord, lat
- 例2 値：SHAWMUT AVE | RUSKINDALE RD | TRAVELER ST | BLAKEVILLE ST | COLUMBIA RD
  - 同じ表の列：date_time, mode_type, location_type, xstreet1, x_cord, y_cord, long, lat

## g2066（2 列）
- 見出し：x_cord
- 例1 値：747754.04 | 773631.17 | 791130.16 | 762680.03 | 771507.33
  - 同じ表の列：dispatch_ts, mode_type, location_type, xstreet2, y_cord, lat
- 例2 値：771859.870000000000 | 762596.780000000000 | 780117.310000000000 | 748876.550000000000 | 771859.870000000000
  - 同じ表の列：date_time, mode_type, location_type, xstreet1, xstreet2, y_cord, long, lat

## g2067（2 列）
- 見出し：y_cord
- 例1 値：2945044.2 | 2953817.16 | 2952176.67 | 2954221.05 | 2949358.15
  - 同じ表の列：dispatch_ts, mode_type, location_type, xstreet2, x_cord, lat
- 例2 値：2950701.900000000000 | 2953817.160000000000 | 2953067.440000000000 | 2924655.770000000000 | 2923836.370000000000
  - 同じ表の列：date_time, mode_type, location_type, xstreet1, xstreet2, x_cord, long, lat

## g2068（2 列）
- 見出し：lat
- 例1 値：42.26845704820328 | 42.37195523453768 | 42.34681618002979 | 42.32157799977611 | 42.33537016800093
  - 同じ表の列：dispatch_ts, mode_type, location_type, xstreet2, x_cord, y_cord
- 例2 値：42.33651807954778 | 42.34842741593963 | 42.34880940135704 | 42.2775513804847 | 42.38549802767471
  - 同じ表の列：date_time, mode_type, location_type, xstreet1, xstreet2, x_cord, y_cord, long

## g2069（1 列）
- 見出し：date_time
- 例1 値：2023-03-26 21:03:33+00 | 2020-07-25 21:34:28+00 | 2018-02-09 03:31:13+00 | 2021-10-30 05:04:28+00 | 2016-10-25 16:18:52+00
  - 同じ表の列：mode_type, location_type, xstreet1, xstreet2, x_cord, y_cord, long, lat

## g2070（1 列）
- 見出し：xstreet1
- 例1 値：KING ST | MASSACHUSETTS AVE | MARTIN LUTHER KING JR BLVD | PARK ST | AMERICAN LEGION HWY
  - 同じ表の列：date_time, mode_type, location_type, xstreet2, x_cord, y_cord, long, lat

## g2071（1 列）
- 見出し：long
- 例1 値：-71.0894836662669 | -71.06298087466733 | -71.13844401707516 | -71.13447109234244 | -71.12630134202719
  - 同じ表の列：date_time, mode_type, location_type, xstreet1, xstreet2, x_cord, y_cord, lat

## g2072（1 列）
- 見出し：Neighborhoods
- 例1 値：Dorchester | Back Bay/Beacon Hill | South Boston | South End | Allston/Brighton
  - 同じ表の列：PopBto5, Pop0to2, Pop3to5, ParentLabFor, WhitePer, BlackPer, LatinxPer, AsianPer

## g2073（1 列）
- 見出し：PopBto5
- 例1 値：1,944 | 1,260 | 1,856 | 1,764 | 2,749
  - 同じ表の列：Neighborhoods, Pop0to2, Pop3to5, ParentLabFor, WhitePer, BlackPer, LatinxPer, AsianPer

## g2074（1 列）
- 見出し：Pop0to2
- 例1 値：21,020 | 787 | 760 | 1,527 | 1,392
  - 同じ表の列：Neighborhoods, PopBto5, Pop3to5, ParentLabFor, WhitePer, BlackPer, LatinxPer, AsianPer

## g2075（1 列）
- 見出し：Pop3to5
- 例1 値：299 | 1,220 | 19,928 | 1,083 | 918
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, ParentLabFor, WhitePer, BlackPer, LatinxPer, AsianPer

## g2076（1 列）
- 見出し：ParentLabFor
- 例1 値：1,419 | 30,445 | 2,768 | 894 | 308
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, WhitePer, BlackPer, LatinxPer, AsianPer

## g2077（1 列）
- 見出し：WhitePer
- 例1 値：65% | 34% | 63% | 18% | 21%
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, ParentLabFor, BlackPer, LatinxPer, AsianPer

## g2078（1 列）
- 見出し：BlackPer
- 例1 値：87% | 14% | 17% | 0% | 9%
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, ParentLabFor, WhitePer, LatinxPer, AsianPer

## g2079（1 列）
- 見出し：LatinxPer
- 例1 値：28% | 20% | 72% | 27% | 22%
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, ParentLabFor, WhitePer, BlackPer, AsianPer

## g2080（1 列）
- 見出し：AsianPer
- 例1 値：13% | 0% | 2% | 19% | 2%
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, ParentLabFor, WhitePer, BlackPer, LatinxPer

## g2081（1 列）
- 見出し：MarFam
- 例1 値：60% | 76% | 71% | 85% | 85%
  - 同じ表の列：Neighborhoods, PopBto5, Pop0to2, Pop3to5, ParentLabFor, WhitePer, BlackPer, LatinxPer

## 答えの雛形

```
g2041	
g2042	
g2043	
g2044	
g2045	
g2046	
g2047	
g2048	
g2049	
g2050	
g2051	
g2052	
g2053	
g2054	
g2055	
g2056	
g2057	
g2058	
g2059	
g2060	
g2061	
g2062	
g2063	
g2064	
g2065	
g2066	
g2067	
g2068	
g2069	
g2070	
g2071	
g2072	
g2073	
g2074	
g2075	
g2076	
g2077	
g2078	
g2079	
g2080	
g2081	
```
