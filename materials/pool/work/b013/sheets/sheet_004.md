# ラベル用シート 004 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：Value of Business Expenditures on Research and Development
- 例1 値：$870,680 | $21,295,043 | $0 | $17,682,991 | $2,741,372
  - 同じ表の列：Region

## g0362（1 列）
- 見出し：PTM EDV - System
- 例1 値：Red Rock Consulting | Deloitte Touche Tohmatsu | Pinnacle Workplace Consultants | The Information Management Group | Blue Crystal Solutions
  - 同じ表の列：ICT Support, $10 585, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0363（1 列）
- 見出し：ICT Support
- 例1 値：Ongoing 3rd party system support | Scanning services | ICT support | Temporary staff | Customer financial system replacement
  - 同じ表の列：PTM EDV - System, $10 585, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0364（1 列）
- 見出し：$10 585
- 例1 値：$49 410 | $15 000 | 4,055,121 | $81 916 | $103 133
  - 同じ表の列：PTM EDV - System, ICT Support, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0365（1 列）
- 見出し：E-Matrix Training
- 例1 値：Adaptive Psychology Pty Ltd | Paxus Australia Pty Ltd | KPMG Australia Technology Solutions Pty… | Symplicit Pty Ltd | Dialog Pty Ltd
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0366（1 列）
- 見出し：Staff Training
- 例1 値：Temporary Staff | Work from home trial review | ICT software security review | Temporary Staff | Strategic Planning Services
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, $14 080, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0367（1 列）
- 見出し：$14 080
- 例1 値：$417 128 | $41 965 | $20 250 | $17 432 | $32 290
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, Staff Training, Peoplebank Australi…, Temporary Staff, $11,453.00

## g0368（1 列）
- 見出し：Peoplebank Australia Ltd
- 例1 値：Rawsons Electrical Pty Ltd | Modis Australia | FDC Construction and Fit-out | Procurement Partners | Deloitte Risk Advisory Pty Ltd
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, Staff Training, $14 080, Temporary Staff, $11,453.00

## g0369（1 列）
- 見出し：Temporary Staff
- 例1 値：Workplace Assessments | Temporary Staff | Customer Relationship Management System… | Procurement Support | Customer Investment Software Updates
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, $11,453.00

## g0370（1 列）
- 見出し：$11,453.00
- 例1 値：2,367,796 | $113,797.00 | $64,317.00 | $593,928.00 | $22,849.00
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff

## g0371（1 列）
- 見出し：KPMG Pty Ltd
- 例1 値：DXC Technology Australia Pty | The Information Management Group | DDLS Australia Pty Ltd | Deloitte Risk Advisory Pty Ltd | Randstad Pty Ltd
  - 同じ表の列：PTM EDV - System, ICT Support, $10 585, E-Matrix Training, Staff Training, $14 080, Peoplebank Australi…, Temporary Staff

## g0372（1 列）
- 見出し：geo_point_2d
- 例1 値：-37.78788013831968, 144.9612333391193 | -37.80281698186015, 144.9555041821315 | -37.82053851243121, 144.963377362942 | -37.78398401734769, 144.9427921184255 | -37.78664887784743, 144.96124036180393
  - 同じ表の列：geo_shape, prop_id, no_smoking, level_1_na, event, training, dog_prohib, dog_off_le

## g0373（1 列）
- 見出し：geo_shape
- 例1 値：{"coordinates": [144.9427921184255, -37… | {"coordinates": [144.94461367085572, -3… | {"coordinates": [144.95521917866634, -3… | {"coordinates": [144.93911928904672, -3… | {"coordinates": [144.9375827252431, -37…
  - 同じ表の列：geo_point_2d, prop_id, no_smoking, level_1_na, event, training, dog_prohib, dog_off_le

## g0374（1 列）
- 見出し：prop_id
- 例1 値：110906 | 103756 | 573368 | 106097 | 106097
  - 同じ表の列：geo_point_2d, geo_shape, no_smoking, level_1_na, event, training, dog_prohib, dog_off_le

## g0375（1 列）
- 見出し：no_smoking
- 例1 値：N | N | N | N | N
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, level_1_na, event, training, dog_prohib, dog_off_le

## g0376（1 列）
- 見出し：level_1_na
- 例1 値：Flagstaff Gardens | Royal Park | Other Park Locations | Other Park Locations | Docklands
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, event, training, dog_prohib, dog_off_le

## g0377（1 列）
- 見出し：event
- 例1 値：N | N | Y | Y | N
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, level_1_na, training, dog_prohib, dog_off_le

## g0378（1 列）
- 見出し：training
- 例1 値：N | N | N | N | Y
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, level_1_na, event, dog_prohib, dog_off_le

## g0379（1 列）
- 見出し：dog_prohib
- 例1 値：N | N | N | N | N
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, level_1_na, event, training, dog_off_le

## g0380（1 列）
- 見出し：dog_off_le
- 例1 値：N | N | N | N | N
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, level_1_na, event, training, dog_prohib

## g0381（1 列）
- 見出し：venue_recn
- 例1 値：268 | 30 | 405 | 435 | 7
  - 同じ表の列：geo_point_2d, geo_shape, prop_id, no_smoking, level_1_na, event, training, dog_prohib

## g0382（1 列）
- 見出し：Contractors with a contract value below $10,000
- 例1 値：Innovate Communicate & Cowork Coplay | Contractors with a contract value above… | Rasu Film & Stills | Veterans SA | AT Kearney Australia
  - 同じ表の列：Purpose, Value

## g0383（1 列）
- 見出し：Purpose
- 例1 値：Total | Client engagement services Submarine Ta… | Delivery of veterans mentoring program | Purpose | Satellite Development
  - 同じ表の列：Contractors with a …, Value

## g0384（1 列）
- 見出し：Value
- 例1 値：$2,034,333 | $41,870 | Value | $1,448,300 | $110,000
  - 同じ表の列：Contractors with a …, Purpose

## g0385（1 列）
- 見出し：Contractor
- 例1 値：RCR O'Donnell Griffin Pty Ltd | Xylem Water Solutions Australia Limited | Tonkin Consulting Pty Ltd | Redbikini Pty Ltd | The Speakers Studio
  - 同じ表の列：Purpose, Value

## g0386（1 列）
- 見出し：Purpose
- 例1 値：Common User Facility Operations and Mai… | Common User Facility Operations and Mai… | Common User Facility Operations and Mai… | Survey Services | Common User Facility Operations and Mai…
  - 同じ表の列：Contractor, Value

## g0387（1 列）
- 見出し：Sampling_point
- 例1 値：Long Point | Noonameena | South Salt Creek | Villa de Yumpa | South Policemans Pt
  - 同じ表の列：Date, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0388（1 列）
- 見出し：Date
- 例1 値：29/05/2008 9:50 | 23/10/2019 9:05 | 19/03/2019 15:45 | 21/07/2014 12:21 | 1/12/1998 15:00
  - 同じ表の列：Sampling_point, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0389（1 列）
- 見出し：Easting
- 例1 値：369342 | 377463 | 320218 | 359175 | 369342
  - 同じ表の列：Sampling_point, Date, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0390（1 列）
- 見出し：Northing
- 例1 値：6010972 | 6010972 | 6000594 | 6005680 | 6041481
  - 同じ表の列：Sampling_point, Date, Easting, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0391（1 列）
- 見出し：Distance_Murray_Mouth
- 例1 値：60.88 | 13.58 | 13.58 | 65.21 | 86.4
  - 同じ表の列：Sampling_point, Date, Easting, Northing, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0392（1 列）
- 見出し：AMPA_ug_L
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：Sampling_point, Date, Easting, Northing, Distance_Murray_Mou…, Acidity_as_Calcium_…, Aldrin_ug_L, Algae_Total_cells_mL

## g0393（1 列）
- 見出し：Acidity_as_Calcium_Carbonate_mg_L
- 例1 値：9.1 | 4.4 | 7.6 | 9 | 4.3
  - 同じ表の列：Sampling_point, Date, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Aldrin_ug_L, Algae_Total_cells_mL

## g0394（1 列）
- 見出し：Aldrin_ug_L
- 例1 値：0.05 | 0.05 | 0.05 | 0.01 | 0.05
  - 同じ表の列：Sampling_point, Date, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Algae_Total_cells_mL

## g0395（1 列）
- 見出し：Algae_Total_cells_mL
- 例1 値：210000 | 3110000 | 967000 | 2450000 | 170
  - 同じ表の列：Sampling_point, Date, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L

## g0396（1 列）
- 見出し：Alkalinity_as_Calcium_Carbonate_mg_L
- 例1 値：196 | 138 | 123 | 204 | 194
  - 同じ表の列：Sampling_point, Date, Easting, Northing, Distance_Murray_Mou…, AMPA_ug_L, Acidity_as_Calcium_…, Aldrin_ug_L

## g0397（2 列）
- 見出し：Fin_year
- 例1 値：FY24-25 | FY24-25 | FY24-25 | FY24-25 | FY24-25
  - 同じ表の列：Stop_ID, Stop_lat, Stop_long, Pax_annual
- 例2 値：FY24-25 | FY24-25 | FY24-25 | FY24-25 | FY24-25
  - 同じ表の列：Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0398（2 列）
- 見出し：Stop_ID
- 例1 値：20291 | 44953 | 47647 | 20302 | 20289
  - 同じ表の列：Fin_year, Stop_lat, Stop_long, Pax_annual
- 例2 値：19943 | 20012 | 20010 | 19869 | 19886
  - 同じ表の列：Fin_year, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0399（2 列）
- 見出し：Stop_lat
- 例1 値：-38.072835 | -38.207239 | -38.203155 | -37.092332 | -38.103103
  - 同じ表の列：Fin_year, Stop_ID, Stop_long, Pax_annual
- 例2 値：-37.8604518 | -37.76889674 | -38.259815 | -37.92514919 | -38.05195538
  - 同じ表の列：Fin_year, Stop_ID, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0400（2 列）
- 見出し：Stop_long
- 例1 値：145.229515 | 144.365323 | 143.888124 | 144.283012 | 145.137733
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Pax_annual
- 例2 値：145.0670324 | 144.9196132 | 144.8944837 | 145.1748917 | 145.1769357
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0401（2 列）
- 見出し：Pax_annual
- 例1 値：260250 | 225300 | 10650 | 1128400 | 333400
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long
- 例2 値：287550 | 1590050 | 412250 | 1624200 | 495750
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0402（1 列）
- 見出し：Pax_weekday
- 例1 値：1350 | 12350 | 1500 | 750 | 550
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_norm_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0403（1 列）
- 見出し：Pax_norm_weekday
- 例1 値：2500 | 900 | 750 | 1100 | 900
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_sch_hol_weekday, Pax_Saturday

## g0404（1 列）
- 見出し：Pax_sch_hol_weekday
- 例1 値：50 | 1800 | 2150 | 1950 | 500
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_Saturday

## g0405（1 列）
- 見出し：Pax_Saturday
- 例1 値：200 | 400 | 400 | 350 | 450
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday

## g0406（1 列）
- 見出し：Pax_Sunday
- 例1 値：150 | 400 | 400 | 650 | 200
  - 同じ表の列：Fin_year, Stop_ID, Stop_lat, Stop_long, Pax_annual, Pax_weekday, Pax_norm_weekday, Pax_sch_hol_weekday

## g0407（1 列）
- 見出し：Number of payments
- 例1 値：18,089 | 13,957 | 38,285 | 31,752 | 34,033
  - 同じ表の列：Year, Value of payments (…

## g0408（1 列）
- 見出し：Value of payments ($ million)
- 例1 値：113.8 | 159.8 | 53.2 | 604.6 | 143.9
  - 同じ表の列：Year, Number of payments

## g0409（3 列）
- 見出し：category
- 例1 値：NSW | Accredited | Accredited | Accredited | Accredited
  - 同じ表の列：city, state, country, fax, hours1, hours2, hours3, lat
- 例2 値：OVSE | OVSE | OVSE | OVSE | OVSE
  - 同じ表の列：CODE_OF_ORIGIN, COUNTRY_OR_STATE, METRO, RURAL, OTHER

## g0410（1 列）
- 見出し：city
- 例1 値：Bingara | Guyra | Glen Innes | Port Macquarie | Blayney
  - 同じ表の列：category, state, country, fax, hours1, hours2, hours3, lat

## g0411（3 列）
- 見出し：country
- 例1 値：Australia | Australia | Australia | Australia | Australia
  - 同じ表の列：category, city, state, fax, hours1, hours2, hours3, lat
- 例2 値：Mongolia | Lesotho | Mexico | Ukraine | Fiji
  - 同じ表の列：Financial Year, Type of flow, Sector, Expense $'000

## g0412（1 列）
- 見出し：fax
- 例1 値：03 5032 4981 | 02 6944 1409 | 02 6920 8109 | 02 6686 8625 | 02 6563 1253
  - 同じ表の列：category, city, state, country, hours1, hours2, hours3, lat

## g0413（1 列）
- 見出し：hours1
- 例1 値：Mon-Fri, 9am-5pm | Mon-Fri, 7am-5pm | Mon-Fri, 11am-1pm, 2pm-4pm, 7.30pm-11.3… | Mon-Fri, 6.45am-5pm | Mon-Fri, 6.30am-12pm
  - 同じ表の列：category, city, state, country, fax, hours2, hours3, lat

## g0414（1 列）
- 見出し：hours2
- 例1 値：Sat, 9am-12pm | Sat & Sun, 1.30am-9.30am, 5.15pm-8.15pm | Sat, 6.15am-9.45pm | Public holidays, Closed | Thu, 9am-6pm
  - 同じ表の列：category, city, state, country, fax, hours1, hours3, lat

## g0415（1 列）
- 見出し：hours3
- 例1 値：Public holidays, 1.30am-9.30am, 12.15pm… | Public holidays, Closed | Sun, 8.30am-4.30pm | Sun, 7am-11.30am | Sun, 6.15am-8.30pm
  - 同じ表の列：category, city, state, country, fax, hours1, hours2, lat

## g0416（22 列）
- 見出し：lat
- 例1 値：-33.88332 | -29.86825 | -34.288006 | -29.473109 | -31.563422
  - 同じ表の列：category, city, state, country, fax, hours1, hours2, hours3
- 例2 値：-37.5834803949659 | -37.5287787449654 | -37.5827789799669 | -37.5829891599667 | -37.555665939962
  - 同じ表の列：Year_Built, Propnum, Long

## g0417（1 列）
- 見出し：lng
- 例1 値：141.466529 | 147.036194 | 147.584167 | 153.046555 | 149.8279
  - 同じ表の列：category, city, state, country, fax, hours1, hours2, hours3

## g0418（1 列）
- 見出し：MonthYear
- 例1 値：2024-10-01 00:00:00.000 | 2024-10-01 00:00:00.000 | 2024-10-01 00:00:00.000 | 2024-11-01 00:00:00.000 | 2024-10-01 00:00:00.000
  - 同じ表の列：Station, Station_Type, Entry_Exit, Trip

## g0419（1 列）
- 見出し：Station
- 例1 値：Minnamurra Station | Auburn Station | Fairy Meadow Station | Scarborough Station | Civic Light Rail
  - 同じ表の列：MonthYear, Station_Type, Entry_Exit, Trip

## g0420（1 列）
- 見出し：Station_Type
- 例1 値：Train | Train | Train | Train | Train
  - 同じ表の列：MonthYear, Station, Entry_Exit, Trip

## g0421（1 列）
- 見出し：Entry_Exit
- 例1 値：Entry | Exit | Exit | Entry | Entry
  - 同じ表の列：MonthYear, Station, Station_Type, Trip

## g0422（1 列）
- 見出し：Trip
- 例1 値：238790 | 4800 | 63210 | 203210 | 65541
  - 同じ表の列：MonthYear, Station, Station_Type, Entry_Exit

## g0423（1 列）
- 見出し：FID
- 例1 値：ESTACIONAMENTO_ROTATIVO_MOTOFRETE_SEGUN… | ESTACIONAMENTO_ROTATIVO_MOTOFRETE_SEGUN… | ESTACIONAMENTO_ROTATIVO_MOTOFRETE_SEGUN… | ESTACIONAMENTO_ROTATIVO_MOTOFRETE_SEGUN… | ESTACIONAMENTO_ROTATIVO_MOTOFRETE_SEGUN…
  - 同じ表の列：ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0424（1 列）
- 見出し：ID_EDESP
- 例1 値：720 | 1587 | 1013 | 1218 | 1023
  - 同じ表の列：FID, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0425（1 列）
- 見出し：DESTINACAO_ESPECIFICA
- 例1 値：MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE
  - 同じ表の列：FID, ID_EDESP, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0426（1 列）
- 見出し：DIA_REGRA_OPERACAO
- 例1 値：SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA | SEGUNDA A SEXTA
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0427（1 列）
- 見出し：PERIODO_VALIDO_REGRA_OPERACAO
- 例1 値：08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0428（1 列）
- 見出し：NUMERO_VAGAS_FISICAS
- 例1 値：12 | 7 | 10 | 7 | 7
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, BAIRRO

## g0429（1 列）
- 見出し：NUMERO_VAGAS_ROTATIVAS
- 例1 値：90 | 80 | 70 | 70 | 70
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, TEMPO_PERMANENCIA, BAIRRO

## g0430（1 列）
- 見出し：TEMPO_PERMANENCIA
- 例1 値：1 HORA(S) | 1 HORA(S) | 1 HORA(S) | 1 HORA(S) | 1 HORA(S)
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, BAIRRO

## g0431（1 列）
- 見出し：BAIRRO
- 例1 値：CENTRO | SERRA | CAIÇARAS | BARRO PRETO | BARREIRO
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA

## g0432（1 列）
- 見出し：GEOMETRIA
- 例1 値：POINT (610494.288828465 7790799.2113980… | POINT (610115.668518849 7796165.2191626… | POINT (612493.403073736 7795375.7948477… | POINT (610444.364364175 7797404.3269458… | POINT (602920.551190189 7791160.9062368…
  - 同じ表の列：FID, ID_EDESP, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA

## g0433（1 列）
- 見出し：ID_QDR
- 例1 値：12846 | 10877 | 18826 | 22041 | 10755
  - 同じ表の列：CODIGO, GEOMETRIA

## g0434（1 列）
- 見出し：CODIGO
- 例1 値：1005087 | 1311641 | 0507678 | 1805467 | 1603920
  - 同じ表の列：ID_QDR, GEOMETRIA

## g0435（1 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((611634.499440179 7805989.3644… | POLYGON ((602890.548427822 7790449.9374… | POLYGON ((607504.848683248 7795692.6603… | POLYGON ((604347.284018681 7794398.4737… | POLYGON ((610106.214658364 7798931.4311…
  - 同じ表の列：ID_QDR, CODIGO

## g0436（1 列）
- 見出し：INDICE_CADASTRAL
- 例1 値：425291 010 0029 | 448037 009 0011 | 107020 001 0050 | 425275 002 001X | 451093 007 0012
  - 同じ表の列：NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0437（1 列）
- 見出し：NULOTCTM
- 例1 値：060422500050 | 050100700060 | 060432600135 | 050071300075 | 050254500095
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0438（1 列）
- 見出し：ZONEAMENTO_PVIPTU
- 例1 値：ZAP | ZAP | ZAP | ZAP | ZAP
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0439（1 列）
- 見出し：FREQUENCIA_COLETA
- 例1 値：COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0440（1 列）
- 見出し：IND_MEIO_FIO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0441（1 列）
- 見出し：IND_PAVIMENTACAO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0442（1 列）
- 見出し：IND_ARBORIZACAO
- 例1 値：SIM | NÃO | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0443（1 列）
- 見出し：IND_GALERIA_PLUVIAL
- 例1 値：SIM | NÃO | SIM | SIM | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_ILUMINACAO_PUBL…

## g0444（1 列）
- 見出し：IND_ILUMINACAO_PUBLICA
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0445（1 列）
- 見出し：IND_REDE_ESGOTO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0446（1 列）
- 見出し：Linha
- 例1 値：S10 | S10 | S10 | S10 | S10
  - 同じ表の列：PC, Veiculo, Data, Saida, Data final operacao, Hora final operacao, Catraca Inicial, Catraca Final

## g0447（1 列）
- 見出し：PC
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Linha, Veiculo, Data, Saida, Data final operacao, Hora final operacao, Catraca Inicial, Catraca Final

## g0448（1 列）
- 見出し：Veiculo
- 例1 値：1050 | 1029 | 1029 | 1058 | 1064
  - 同じ表の列：Linha, PC, Data, Saida, Data final operacao, Hora final operacao, Catraca Inicial, Catraca Final

## g0449（1 列）
- 見出し：Data
- 例1 値：15/02/2023 | 13/02/2023 | 02/02/2023 | 15/02/2023 | 11/02/2023
  - 同じ表の列：Linha, PC, Veiculo, Saida, Data final operacao, Hora final operacao, Catraca Inicial, Catraca Final

## g0450（1 列）
- 見出し：Saida
- 例1 値：16:27:47.0 | 06:05:49.0 | 11:36:55.0 | 09:58:49.0 | 10:16:33.0
  - 同じ表の列：Linha, PC, Veiculo, Data, Data final operacao, Hora final operacao, Catraca Inicial, Catraca Final

## g0451（1 列）
- 見出し：Data final operacao
- 例1 値：07/02/2023 | 03/02/2023 | 01/02/2023 | 04/02/2023 | 04/02/2023
  - 同じ表の列：Linha, PC, Veiculo, Data, Saida, Hora final operacao, Catraca Inicial, Catraca Final

## g0452（1 列）
- 見出し：Hora final operacao
- 例1 値：18:33:55.0 | 07:39:43.0 | 14:42:47.0 | 20:04:47.0 | 06:58:41.0
  - 同じ表の列：Linha, PC, Veiculo, Data, Saida, Data final operacao, Catraca Inicial, Catraca Final

## g0453（1 列）
- 見出し：Catraca Inicial
- 例1 値：215542 | 227312 | 244845 | 176863 | 200193
  - 同じ表の列：Linha, PC, Veiculo, Data, Saida, Data final operacao, Hora final operacao, Catraca Final

## g0454（1 列）
- 見出し：Catraca Final
- 例1 値：223892 | 13479 | 15509 | 216922 | 16314
  - 同じ表の列：Linha, PC, Veiculo, Data, Saida, Data final operacao, Hora final operacao, Catraca Inicial

## g0455（1 列）
- 見出し：Passageiros
- 例1 値：45 | 23 | 23 | 45 | 29
  - 同じ表の列：Linha, PC, Veiculo, Data, Saida, Data final operacao, Hora final operacao, Catraca Inicial

## g0456（1 列）
- 見出し：実数/男女計/令和5年
- 例1 値：対前年・対前年同期増減数/男/令和8年4~6月 | 実数/女/令和6年1~3月 | 実数/男女計/令和6年4~6月 | 対前年・対前年同期増減数/女/令和7年 | 実数/男女計/令和7年
  - 同じ表の列：2023, 382, 679, 922, 338, 1194, 329, 265

## g0457（1 列）
- 見出し：382
- 例1 値：398 | 6 | -5 | 33 | 85
  - 同じ表の列：実数/男女計/令和5年, 2023, 679, 922, 338, 1194, 329, 265

## g0458（1 列）
- 見出し：679
- 例1 値：7 | 4 | 454 | 18 | 209
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 922, 338, 1194, 329, 265

## g0459（1 列）
- 見出し：922
- 例1 値：630 | 24 | 966 | 668 | 701
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 338, 1194, 329, 265

## g0460（1 列）
- 見出し：338
- 例1 値：-7 | 104 | 18 | 92 | 36
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 922, 1194, 329, 265

## g0461（1 列）
- 見出し：1194
- 例1 値：602 | 18 | 129 | 556 | 1233
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 922, 338, 329, 265

## g0462（1 列）
- 見出し：329
- 例1 値：181 | 190 | -2 | -2 | 2
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 922, 338, 1194, 265

## g0463（1 列）
- 見出し：265
- 例1 値：264 | 154 | 108 | 147 | 131
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 922, 338, 1194, 329

## g0464（1 列）
- 見出し：477
- 例1 値：-7 | 495 | 9 | 7 | 244
  - 同じ表の列：実数/男女計/令和5年, 2023, 382, 679, 922, 338, 1194, 329

## g0465（1 列）
- 見出し：年度
- 例1 値：令和3 | 令和6 | 令和6 | Note: 1) The final budget includes the … | 2) The Public enterprise accounts are t…
  - 同じ表の列：Fiscal year, 会計階層, 会計, マーク Mark, 当初予算額 Original budg…, 最終予算額 Final budget …, 決算額 Settlement

## g0466（1 列）
- 見出し：Fiscal year
- 例1 値：2024 | 2024 | 2024 | 2024 | 2024
  - 同じ表の列：年度, 会計階層, 会計, マーク Mark, 当初予算額 Original budg…, 最終予算額 Final budget …, 決算額 Settlement

## g0467（1 列）
- 見出し：会計階層
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：年度, Fiscal year, 会計, マーク Mark, 当初予算額 Original budg…, 最終予算額 Final budget …, 決算額 Settlement

## g0468（1 列）
- 見出し：会計
- 例1 値：国民健康保険事業 | 心身障害者扶養年金 | 総数 | 公債費 | 工業用水道事業清算
  - 同じ表の列：年度, Fiscal year, 会計階層, マーク Mark, 当初予算額 Original budg…, 最終予算額 Final budget …, 決算額 Settlement

## g0469（1 列）
- 見出し：マーク Mark
- 例1 値：2)
  - 同じ表の列：年度, Fiscal year, 会計階層, 会計, 当初予算額 Original budg…, 最終予算額 Final budget …, 決算額 Settlement

## g0470（1 列）
- 見出し：当初予算額 Original budget
- 例1 値：15393857 | 16082069 | 15157870 | 2893 | 15452215
  - 同じ表の列：年度, Fiscal year, 会計階層, 会計, マーク Mark, 最終予算額 Final budget …, 決算額 Settlement

## g0471（1 列）
- 見出し：最終予算額 Final budget 1)
- 例1 値：4432 | 7925 | 48 | 1239809 | 13969
  - 同じ表の列：年度, Fiscal year, 会計階層, 会計, マーク Mark, 当初予算額 Original budg…, 決算額 Settlement

## g0472（1 列）
- 見出し：決算額 Settlement
- 例1 値：6321992 | 140490 | 15775293 | 231370 | 2867
  - 同じ表の列：年度, Fiscal year, 会計階層, 会計, マーク Mark, 当初予算額 Original budg…, 最終予算額 Final budget …

## g0473（1 列）
- 見出し：年月[西暦]
- 例1 値：201404 | 202506 | 202412 | 201704 | 201210
  - 同じ表の列：米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人], その他[人]

## g0474（1 列）
- 見出し：米国[人]
- 例1 値：2708 | 2830 | 3372 | 3312 | 2907
  - 同じ表の列：年月[西暦], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人], その他[人]

## g0475（1 列）
- 見出し：韓国及び朝鮮[人]
- 例1 値：3449 | 3391 | 3472 | 3641 | 3601
  - 同じ表の列：年月[西暦], 米国[人], 中国[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人], その他[人]

## g0476（1 列）
- 見出し：中国[人]
- 例1 値：3933 | 4312 | 7900 | 3477 | 8053
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 英国[人], フィリピン[人], フランス[人], ドイツ[人], その他[人]

## g0477（1 列）
- 見出し：英国[人]
- 例1 値：881 | 844 | 812 | 775 | 848
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], フィリピン[人], フランス[人], ドイツ[人], その他[人]

## g0478（1 列）
- 見出し：フィリピン[人]
- 例1 値：1002 | 1012 | 1061 | 1004 | 902
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フランス[人], ドイツ[人], その他[人]

## g0479（1 列）
- 見出し：フランス[人]
- 例1 値：755 | 757 | 802 | 732 | 682
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], ドイツ[人], その他[人]

## g0480（1 列）
- 見出し：ドイツ[人]
- 例1 値：313 | 276 | 359 | 307 | 366
  - 同じ表の列：年月[西暦], 米国[人], 韓国及び朝鮮[人], 中国[人], 英国[人], フィリピン[人], フランス[人], その他[人]

## 答えの雛形

```
g0361	
g0362	
g0363	
g0364	
g0365	
g0366	
g0367	
g0368	
g0369	
g0370	
g0371	
g0372	
g0373	
g0374	
g0375	
g0376	
g0377	
g0378	
g0379	
g0380	
g0381	
g0382	
g0383	
g0384	
g0385	
g0386	
g0387	
g0388	
g0389	
g0390	
g0391	
g0392	
g0393	
g0394	
g0395	
g0396	
g0397	
g0398	
g0399	
g0400	
g0401	
g0402	
g0403	
g0404	
g0405	
g0406	
g0407	
g0408	
g0409	
g0410	
g0411	
g0412	
g0413	
g0414	
g0415	
g0416	
g0417	
g0418	
g0419	
g0420	
g0421	
g0422	
g0423	
g0424	
g0425	
g0426	
g0427	
g0428	
g0429	
g0430	
g0431	
g0432	
g0433	
g0434	
g0435	
g0436	
g0437	
g0438	
g0439	
g0440	
g0441	
g0442	
g0443	
g0444	
g0445	
g0446	
g0447	
g0448	
g0449	
g0450	
g0451	
g0452	
g0453	
g0454	
g0455	
g0456	
g0457	
g0458	
g0459	
g0460	
g0461	
g0462	
g0463	
g0464	
g0465	
g0466	
g0467	
g0468	
g0469	
g0470	
g0471	
g0472	
g0473	
g0474	
g0475	
g0476	
g0477	
g0478	
g0479	
g0480	
```
