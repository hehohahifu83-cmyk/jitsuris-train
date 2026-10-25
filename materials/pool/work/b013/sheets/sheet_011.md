# ラベル用シート 011 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_011.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1201（1 列）
- 見出し：sub_order
- 例1 値：3 | 15 | 9 | 7 | 3
  - 同じ表の列：profile, census_year, category, sub_category, value

## g1202（1 列）
- 見出し：as_at_date
- 例1 値：2014-07-01 | 2014-07-01 | 2014-07-01 | 2014-07-01 | 2014-07-01
  - 同じ表の列：year, actual_budget_plan, category, sub_category, value_000

## g1203（1 列）
- 見出し：actual_budget_plan
- 例1 値：BUDGET | BUDGET | BUDGET | PLAN | PLAN
  - 同じ表の列：as_at_date, year, category, sub_category, value_000

## g1204（1 列）
- 見出し：sub_category
- 例1 値：Grants and Subsidies | Grants and Subsidies | Grants and Subsidies | Grants and Subsidies | Grants and Subsidies
  - 同じ表の列：as_at_date, year, actual_budget_plan, category, value_000

## g1205（1 列）
- 見出し：value_000
- 例1 値：13217.0 | 10281.0 | 146889.0 | 21483.0 | 4065.0
  - 同じ表の列：as_at_date, year, actual_budget_plan, category, sub_category

## g1206（1 列）
- 見出し：Grass
- 例1 値：Yes | Yes | Yes | Yes | No
  - 同じ表の列：Bin, Bench, Dog Tidy, Drink Fountain, Play Equipment, Toilet, Table, BBQ

## g1207（1 列）
- 見出し：Bin
- 例1 値：1 | 1 | 0 | 1 | 1
  - 同じ表の列：Grass, Bench, Dog Tidy, Drink Fountain, Play Equipment, Toilet, Table, BBQ

## g1208（1 列）
- 見出し：Bench
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Grass, Bin, Dog Tidy, Drink Fountain, Play Equipment, Toilet, Table, BBQ

## g1209（1 列）
- 見出し：Dog Tidy
- 例1 値：1 | 1 | 0 | 1 | 1
  - 同じ表の列：Grass, Bin, Bench, Drink Fountain, Play Equipment, Toilet, Table, BBQ

## g1210（1 列）
- 見出し：Drink Fountain
- 例1 値：No | Yes | No | No | No
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Play Equipment, Toilet, Table, BBQ

## g1211（1 列）
- 見出し：Play Equipment
- 例1 値：No | Yes | Yes | No | No
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Drink Fountain, Toilet, Table, BBQ

## g1212（1 列）
- 見出し：Toilet
- 例1 値：No | No | No | No | No
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Drink Fountain, Play Equipment, Table, BBQ

## g1213（1 列）
- 見出し：Table
- 例1 値：No | Yes | Yes | Yes | No
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Drink Fountain, Play Equipment, Toilet, BBQ

## g1214（1 列）
- 見出し：BBQ
- 例1 値：2 | 1 | 2 | 0 | 0
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Drink Fountain, Play Equipment, Toilet, Table

## g1215（1 列）
- 見出し：Sharps
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Grass, Bin, Bench, Dog Tidy, Drink Fountain, Play Equipment, Toilet, Table

## g1216（1 列）
- 見出し：Rider Levett Bucknall SA Pty Ltd
- 例1 値：The A & G Materne Family Trust and C & … | The A & G Materne Family Trust and C & … | The RG Group Pty Ltd | CyberCX Pty Ltd | System Solutions Engineering Pty Ltd
  - 同じ表の列：Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…, $920.00

## g1217（1 列）
- 見出し：Cost management services
- 例1 値：Concept and architectural services | Architectural services | Architectural services | Total | Engineering services
  - 同じ表の列：Rider Levett Buckna…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…, $920.00

## g1218（1 列）
- 見出し：$3,985.00
- 例1 値：$1,600.00 | $12,500.00 | $864.00 | $5,500.00 | $4,970.00
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…, $920.00

## g1219（1 列）
- 見出し：PKF Adelaide
- 例1 値：Rider Levett Bucknall SA Pty Ltd | NEC Australia Pty Ltd | ISDefence Pty Ltd | Consultants with a contract value above… | The A & G Materne Family Trust and C & …
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…, $920.00

## g1220（1 列）
- 見出し：Procurement process audit
- 例1 値：Cost management services | Records management audit | Protective security maturity assessment | Total | ICT corporate infrastructure network re…
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, $6,000.00, ISDefence Pty Ltd, Protective security…, $920.00

## g1221（1 列）
- 見出し：$6,000.00
- 例1 値：$54,898.97 | $2,475.00 | $1,476.00 | $500.00 | $23,000.00
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, ISDefence Pty Ltd, Protective security…, $920.00

## g1222（1 列）
- 見出し：ISDefence Pty Ltd
- 例1 値：Consultants with a contract value above… | Wendy Fewsdale | The A & G Materne Family Trust and C & … | NEC IT Services Australia Pty Ltd | Consultancies
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, Protective security…, $920.00

## g1223（1 列）
- 見出し：Protective security maturity assessment
- 例1 値：Information technology upgrade | Purpose | Total | Security compliance audit report | Architectural design
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, $920.00

## g1224（1 列）
- 見出し：$920.00
- 例1 値：$50,665.36 | $7,502.28 | $12,800.00 | $2,800.00 | $5,850.00
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…

## g1225（1 列）
- 見出し：Flight Safety
- 例1 値：Visual Analysis | Materne Pennino Hoare | Consultants with a contract value above… | 2017-2018 | Info-Osmosis
  - 同じ表の列：Rider Levett Buckna…, Cost management ser…, $3,985.00, PKF Adelaide, Procurement process…, $6,000.00, ISDefence Pty Ltd, Protective security…

## g1226（2 列）
- 見出し：Time
- 例1 値：2021-05-07T04:49:14+10:00 | 2021-05-06T20:52:50+10:00 | 2021-05-07T07:51:37+10:00 | 2021-05-06T22:51:23+10:00 | 2021-05-06T17:28:04+10:00
  - 同じ表の列：Device ID, Humidity (%), Temperature (°C), Sensor Type, Location, TTN metadata
- 例2 値：2021-05-06T10:44:05+10:00 | 2021-05-04T17:14:14+10:00 | 2021-05-04T14:24:08+10:00 | 2021-05-04T21:04:09+10:00 | 2021-05-01T09:54:14+10:00
  - 同じ表の列：Device ID, Location, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1227（1 列）
- 見出し：Device ID
- 例1 値：00137a100000a7d0 | 00137a100000a7c8 | 00137a100000a7cb | 00137a100000a7ca | 00137a100000a7c6
  - 同じ表の列：Time, Humidity (%), Temperature (°C), Sensor Type, Location, TTN metadata

## g1228（1 列）
- 見出し：Humidity (%)
- 例1 値：98.17 | 92.18 | 90.38 | 96.42 | 99.61
  - 同じ表の列：Time, Device ID, Temperature (°C), Sensor Type, Location, TTN metadata

## g1229（2 列）
- 見出し：Temperature (°C)
- 例1 値：18.97 | 19.05 | 18.39 | 18.53 | 20.87
  - 同じ表の列：Time, Device ID, Humidity (%), Sensor Type, Location, TTN metadata
- 例2 値：19.4 | 14.2 | 21.1 | 18.3 | 19.7
  - 同じ表の列：Time, Device ID, Location, TTN metadata, TTN payload fields, Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1230（1 列）
- 見出し：Sensor Type
- 例1 値：NVX | NVX | NVX | NVX | NVX
  - 同じ表の列：Time, Device ID, Humidity (%), Temperature (°C), Location, TTN metadata

## g1231（2 列）
- 見出し：Location
- 例1 値：-32.962254,151.68561 | -32.958576,151.69977 | -32.96574,151.70169 | -32.96574,151.70169 | -32.97024,151.68633
  - 同じ表の列：Time, Device ID, Humidity (%), Temperature (°C), Sensor Type, TTN metadata
- 例2 値：-32.96599,151.69513 | -32.96599,151.69513 | -32.96599,151.69513 | -32.96599,151.69513 | -32.96599,151.69513
  - 同じ表の列：Time, Device ID, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1232（2 列）
- 見出し：TTN metadata
- 例1 値：{"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r…
  - 同じ表の列：Time, Device ID, Humidity (%), Temperature (°C), Sensor Type, Location
- 例2 値：{"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r… | {"location_source": "registry", "data_r…
  - 同じ表の列：Time, Device ID, Location, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1233（1 列）
- 見出し：Device ID
- 例1 値：dlb_atm41_5282 | dlb_atm41_5282 | dlb_atm41_5282 | dlb_atm41_5282 | dlb_atm41_5282
  - 同じ表の列：Time, Location, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1234（1 列）
- 見出し：TTN payload fields
- 例1 値：{"sensor_temperature_internal": {"displ… | {"sensor_temperature_internal": {"displ… | {"sensor_temperature_internal": {"displ… | {"sensor_temperature_internal": {"displ… | {"sensor_temperature_internal": {"displ…
  - 同じ表の列：Time, Device ID, Location, TTN metadata, Temperature (°C), Atmospheric Pressur…, Lightning Average D…, Lightning Strike Co…

## g1235（1 列）
- 見出し：Atmospheric Pressure (kPa)
- 例1 値：100.29 | 101.59 | 100.45 | 100.47 | 99.8
  - 同じ表の列：Time, Device ID, Location, TTN metadata, TTN payload fields, Temperature (°C), Lightning Average D…, Lightning Strike Co…

## g1236（1 列）
- 見出し：Lightning Average Distance (km)
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：Time, Device ID, Location, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Strike Co…

## g1237（1 列）
- 見出し：Lightning Strike Count
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：Time, Device ID, Location, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…

## g1238（1 列）
- 見出し：Maximum Wind Speed (m/s)
- 例1 値：4.31 | 1.38 | 1.52 | 5.6 | 3.84
  - 同じ表の列：Time, Device ID, Location, TTN metadata, TTN payload fields, Temperature (°C), Atmospheric Pressur…, Lightning Average D…

## g1239（1 列）
- 見出し：Operator
- 例1 値：Chargefox | JOLT | Chargefox | Everty | Tesla
  - 同じ表の列：OBJECTID, Number_of_plugs, Charger_Type, Charger_rating, PCODE, Source

## g1240（1 列）
- 見出し：Number_of_plugs
- 例1 値：4 | 4 | 2 | 2 | 6
  - 同じ表の列：OBJECTID, Operator, Charger_Type, Charger_rating, PCODE, Source

## g1241（1 列）
- 見出し：Charger_Type
- 例1 値：AC | AC | AC | DC | AC
  - 同じ表の列：OBJECTID, Operator, Number_of_plugs, Charger_rating, PCODE, Source

## g1242（1 列）
- 見出し：Charger_rating
- 例1 値：22 kW | 22 kW | 75 kW | 50 kW | 22 kW
  - 同じ表の列：OBJECTID, Operator, Number_of_plugs, Charger_Type, PCODE, Source

## g1243（1 列）
- 見出し：Source
- 例1 値：Existing Destination Chargers | ARENA - Driving the Nation | Existing Destination Chargers | Existing Destination Chargers | Existing Fast Chargers
  - 同じ表の列：OBJECTID, Operator, Number_of_plugs, Charger_Type, Charger_rating, PCODE

## 答えの雛形

```
g1201	
g1202	
g1203	
g1204	
g1205	
g1206	
g1207	
g1208	
g1209	
g1210	
g1211	
g1212	
g1213	
g1214	
g1215	
g1216	
g1217	
g1218	
g1219	
g1220	
g1221	
g1222	
g1223	
g1224	
g1225	
g1226	
g1227	
g1228	
g1229	
g1230	
g1231	
g1232	
g1233	
g1234	
g1235	
g1236	
g1237	
g1238	
g1239	
g1240	
g1241	
g1242	
g1243	
```
