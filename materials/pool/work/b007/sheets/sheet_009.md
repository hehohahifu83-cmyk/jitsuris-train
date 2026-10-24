# ラベル用シート 009 / 019

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_009.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0961（1 列）
- 見出し：POLLUTANT
- 例1 値：Cadmium (S) | Mercury in Fish Tissue (T) | Mercury in Fish Tissue (T) | Zinc (S) | Lead (T)
  - 同じ表の列：WBID, YR, BUSINESSID, WATER_BODY, WB_CLS, MDNR_IMPSZ, SIZE_, EPA_APPRSZ

## g0962（1 列）
- 見出し：Award Year
- 例1 値：FY2021 | FY2025 | FY2025 | FY2021 | FY2023
  - 同じ表の列：Organization Receiv…, Award Type, Amount

## g0963（1 列）
- 見出し：Organization Receiving Award
- 例1 値：Lane Community College | Chiloquin Fire and Rescue (CF&R) | Powers School District | Gaston Rural Fire District | Monroe School District 1J
  - 同じ表の列：Award Year, Award Type, Amount

## g0964（1 列）
- 見出し：Award Type
- 例1 値：Grant | Grant | Grant | Grant | Grant
  - 同じ表の列：Award Year, Organization Receiv…, Amount

## g0965（1 列）
- 見出し：Amount
- 例1 値：2497895 | 2496835 | 1765780 | 2368445 | 2498895
  - 同じ表の列：Award Year, Organization Receiv…, Award Type

## g0966（1 列）
- 見出し：Agency Issuing Tax Expenditure
- 例1 値：Umatilla County Assessor (Oregon Depart… | Lincoln County Assessor (Oregon Departm… | Morrow County Assessor (Oregon Departme… | Umatilla County Assessor (Oregon Depart… | Lake County Assessor (Oregon Department…
  - 同じ表の列：Fiscal Year, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0967（1 列）
- 見出し：Report Period End Date
- 例1 値：2024-06-30T00:00:00.000 | 2024-06-30T00:00:00.000 | 2017-06-30T00:00:00.000 | 2024-06-30T00:00:00.000 | 2018-07-30T00:00:00.000
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0968（1 列）
- 見出し：Estimated Total Investment
- 例1 値：$1,420,000,000 | $600,000,000 | $116,000,000 | NA | $152,000,000
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0969（1 列）
- 見出し：Property Tax Benefit (not a credit)
- 例1 値：Unrealized (Taxes forgone over 15 years… | Unrealized (Taxes forgone over 15 years… | Unrealized (Taxes forgone over 15 years… | Unrealized (Taxes forgone over 15 years… | Unrealized (Taxes forgone over 15 years…
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0970（1 列）
- 見出し：Specific Outcomes of the Program and Taxpayer Requirements
- 例1 値：Project benefits traded-sector industry… | Project benefits traded-sector industry… | Project benefits traded-sector industry… | Project benefits traded-sector industry… | Project benefits traded-sector industry…
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Statistics and Meth…, Agency's Certificat…, Date Approved

## g0971（1 列）
- 見出し：Statistics and Methodology Employed
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Agency's Certificat…, Date Approved

## g0972（1 列）
- 見出し：Agency's Certification Decision
- 例1 値：Oregon Business Development Commission … | Oregon Business Development Commission … | Oregon Business Development Commission … | Oregon Business Development Commission … | Oregon Business Development Commission …
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Date Approved

## g0973（1 列）
- 見出し：Date Approved
- 例1 値：2023-09-22T00:00:00.000 | 2023-06-09T00:00:00.000 | 2020-05-22T00:00:00.000 | 2020-09-18T00:00:00.000 | 2019-09-20T00:00:00.000
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…

## g0974（1 列）
- 見出し：Facility Location County Code
- 例1 値：07 | 35 | NA | 11, 19 | 49
  - 同じ表の列：Fiscal Year, Agency Issuing Tax …, Report Period End D…, Estimated Total Inv…, Property Tax Benefi…, Specific Outcomes o…, Statistics and Meth…, Agency's Certificat…

## g0975（1 列）
- 見出し：Year
- 例1 値：1994-01-01T00:00:00.000 | 1975-01-01T00:00:00.000 | 1999-01-01T00:00:00.000 | 1971-01-01T00:00:00.000 | 2000-01-01T00:00:00.000
  - 同じ表の列：Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…, Fatality claims

## g0976（1 列）
- 見出し：Subject employers
- 例1 値：94800 | 76026 | 67602 | 67410 | 134200
  - 同じ表の列：Year, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…, Fatality claims

## g0977（1 列）
- 見出し：Subject employees
- 例1 値：1105200 | 1943000 | 1547800 | 1987300 | 1280500
  - 同じ表の列：Year, Subject employers, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…, Fatality claims

## g0978（1 列）
- 見出し：Accepted disabling claims
- 例1 値：22994 | 44930 | 36802 | 43660 | 35372
  - 同じ表の列：Year, Subject employers, Subject employees, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…, Fatality claims

## g0979（1 列）
- 見出し：Est. accepted nondisabling claims
- 例1 値：98100 | 46000 | 102200 | 46800 | 89700
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. total accepted…, Denied claims, Disabling claim den…, Fatality claims

## g0980（1 列）
- 見出し：Est. total accepted claims
- 例1 値：110700 | 67800 | 64600 | 61100 | 62400
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Denied claims, Disabling claim den…, Fatality claims

## g0981（1 列）
- 見出し：Denied claims
- 例1 値：2647 | 20915 | 10204 | 12726 | 2699
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Disabling claim den…, Fatality claims

## g0982（1 列）
- 見出し：Disabling claim denial rate
- 例1 値：0.167 | 0.175 | 0.169 | 0.148 | 0.104
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Fatality claims

## g0983（1 列）
- 見出し：Fatality claims
- 例1 値：29 | 35 | 45 | 35 | 89
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…

## g0984（1 列）
- 見出し：Net PTD claims
- 例1 値：285 | 10 | 9 | 124 | 122
  - 同じ表の列：Year, Subject employers, Subject employees, Accepted disabling …, Est. accepted nondi…, Est. total accepted…, Denied claims, Disabling claim den…

## g0985（1 列）
- 見出し：PennDOT County Code
- 例1 値：52 | 58 | 18 | 49 | 13
  - 同じ表の列：ID, County Code, FIPS County Code, Provider City, Provider State

## g0986（2 列）
- 見出し：County Code
- 例1 値：35 | 07 | 12 | 50 | 13
  - 同じ表の列：ID, PennDOT County Code, FIPS County Code, Provider City, Provider State
- 例2 値：06 | 67 | 15 | 39 | 51
  - 同じ表の列：Type of Facility, County, State FIPS code, County FIPS code, County Number

## g0987（1 列）
- 見出し：FIPS County Code
- 例1 値：105 | 085 | 025 | 033 | 041
  - 同じ表の列：ID, PennDOT County Code, County Code, Provider City, Provider State

## g0988（1 列）
- 見出し：Provider City
- 例1 値：Marienville | Pittsburgh | Indiana | York | Washington
  - 同じ表の列：ID, PennDOT County Code, County Code, FIPS County Code, Provider State

## g0989（1 列）
- 見出し：Provider State
- 例1 値：Pennsylvania | Pennsylvania | Pennsylvania | Pennsylvania | Pennsylvania
  - 同じ表の列：ID, PennDOT County Code, County Code, FIPS County Code, Provider City

## g0990（1 列）
- 見出し：Type of Facility
- 例1 値：DDAP-Licensed Treatment Facility | DDAP-Licensed Treatment Facility | DDAP-Licensed Treatment Facility | DDAP-Licensed Treatment Facility | DDAP-Licensed Treatment Facility
  - 同じ表の列：County, State FIPS code, County FIPS code, County Number, County Code

## g0991（2 列）
- 見出し：County
- 例1 値：Allegheny | Philadelphia | Susquehanna | Dauphin | Erie
  - 同じ表の列：Type of Facility, State FIPS code, County FIPS code, County Number, County Code
- 例2 値：Caroline | Allegany | Allegany | Washington | Worcester
  - 同じ表の列：Fiscal Year, Awardee, Award, City

## g0992（1 列）
- 見出し：State FIPS code
- 例1 値：42 | 42 | 42 | 42 | 42
  - 同じ表の列：Type of Facility, County, County FIPS code, County Number, County Code

## g0993（1 列）
- 見出し：County FIPS code
- 例1 値：091 | 017 | 101 | 003 | 127
  - 同じ表の列：Type of Facility, County, State FIPS code, County Number, County Code

## g0994（1 列）
- 見出し：County Number
- 例1 値：51 | 36 | 26 | 9 | 6
  - 同じ表の列：Type of Facility, County, State FIPS code, County FIPS code, County Code

## g0995（1 列）
- 見出し：Year of Release
- 例1 値：2002 | 2017 | 2005 | 2000 | 2016
  - 同じ表の列：Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g0996（1 列）
- 見出し：Inmates Released
- 例1 値：12550 | 18578 | 19222 | 10125 | 20031
  - 同じ表の列：Year of Release, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g0997（1 列）
- 見出し：Rearrest Rates 6 months
- 例1 値：13.2 | 12.3 | 10.4 | 13.7 | 14.2
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g0998（1 列）
- 見出し：Rearrest Rates 1 year
- 例1 値：23.3 | 25.7 | 25.2 | 23.6 | 24.2
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g0999（1 列）
- 見出し：Rearrest Rates 3 years
- 例1 値：48.4 | 50.7 | 47.6 | 49.2 | 49.4
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g1000（1 列）
- 見出し：Reincarceration Rates 6 months
- 例1 値：12 | 13.9 | 10.7 | 13.6 | 15.4
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g1001（1 列）
- 見出し：Reincarceration Rates 1 year
- 例1 値：26.1 | 26.3 | 22 | 24.9 | 22.3
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g1002（1 列）
- 見出し：Reincarceration Rates 3 years
- 例1 値：47.8 | 43.9 | 40.6 | 47.1 | 47.1
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Overall Recidivism …

## g1003（1 列）
- 見出し：Overall Recidivism Rates 6 months
- 例1 値：26 | 19.9 | 24.1 | 22.6 | 21.7
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…

## g1004（1 列）
- 見出し：Overall Recidivism Rates 1 year
- 例1 値：35.8 | 37 | 35.5 | 36.7 | 35
  - 同じ表の列：Year of Release, Inmates Released, Rearrest Rates 6 mo…, Rearrest Rates 1 ye…, Rearrest Rates 3 ye…, Reincarceration Rat…, Reincarceration Rat…, Reincarceration Rat…

## g1005（1 列）
- 見出し：OBJECTID
- 例1 値：868 | 904 | 557 | 1014 | 735
  - 同じ表の列：total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1006（1 列）
- 見出し：total01_01_2022
- 例1 値：836.0 | 318.0 | 1627.0 | 612.0 | 330.0
  - 同じ表の列：OBJECTID, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1007（1 列）
- 見出し：total01_02_2022
- 例1 値：86.0 | 4083.0 | 267.0 | 633.0 | 2167.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1008（1 列）
- 見出し：total01_03_2022
- 例1 値：2245.0 | 1832.0 | 638.0 | 321.0 | 3541.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1009（1 列）
- 見出し：total01_04_2022
- 例1 値：305.0 | 1854.0 | 311.0 | 243.0 | 348.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_05_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1010（1 列）
- 見出し：total01_05_2022
- 例1 値：2306.0 | 94.0 | 15.0 | 1264.0 | 676.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_06_2022, total01_07_2022, total01_08_2022

## g1011（1 列）
- 見出し：total01_06_2022
- 例1 値：626.0 | 3110.0 | 90.0 | 1910.0 | 120.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_07_2022, total01_08_2022

## g1012（1 列）
- 見出し：total01_07_2022
- 例1 値：307.0 | 3768.0 | 303.0 | 89.0 | 2234.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_08_2022

## g1013（1 列）
- 見出し：total01_08_2022
- 例1 値：295.0 | 1882.0 | 2652.0 | 9236.0 | 365.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022

## g1014（1 列）
- 見出し：total01_09_2022
- 例1 値：66.0 | 285.0 | 10846.0 | 1143.0 | 5303.0
  - 同じ表の列：OBJECTID, total01_01_2022, total01_02_2022, total01_03_2022, total01_04_2022, total01_05_2022, total01_06_2022, total01_07_2022

## g1015（1 列）
- 見出し：Awardee
- 例1 値：Town of Loch Lynn Heights | Board of County Commissioners of Kent C… | Worcester County | Town of Princess Anne | Town of New Windsor
  - 同じ表の列：Fiscal Year, Award, City, County

## g1016（1 列）
- 見出し：Award
- 例1 値：51455.00 | 673300.00 | 40000.00 | 335000.00 | 82400.00
  - 同じ表の列：Fiscal Year, Awardee, City, County

## g1017（2 列）
- 見出し：City
- 例1 値：Funkstown | Westminster | Cambridge | Crisfield | Willards
  - 同じ表の列：Fiscal Year, Awardee, Award, County
- 例2 値：Boston | Boston | Boston | Boston | Boston
  - 同じ表の列：Division/Sitegroup, Site, State, Country, Type, Category, UOM, Feb 14

## g1018（1 列）
- 見出し：Tipo
- 例1 値：text | text | text | text | text
  - 同じ表の列：Tamanho, valores_possiveis

## g1019（1 列）
- 見出し：Tamanho
- 例1 値：2 | 2 | 2 | 20 | 3
  - 同じ表の列：Tipo, valores_possiveis

## g1020（1 列）
- 見出し：valores_possiveis
- 例1 値：1 a 10 | Compras, Congressos e Convencoes, Estud… | 1 a 10 | Sim, Nao | 1 a 10
  - 同じ表の列：Tipo, Tamanho

## g1021（1 列）
- 見出し：dia_semana
- 例1 値：domingo | segunda | sexta | sabado | domingo
  - 同じ表の列：mes, temporada, Cidade, UF, regiao, pais, motivo, selazer_atrativo

## g1022（1 列）
- 見出し：mes
- 例1 値：dezembro | maio | dezembro | dezembro | maio
  - 同じ表の列：dia_semana, temporada, Cidade, UF, regiao, pais, motivo, selazer_atrativo

## g1023（1 列）
- 見出し：temporada
- 例1 値：alta | alta | alta | alta | baixa
  - 同じ表の列：dia_semana, mes, Cidade, UF, regiao, pais, motivo, selazer_atrativo

## g1024（2 列）
- 見出し：Cidade
- 例1 値：Caruaru | Curitiba | Curitiba | Sao Paulo | Conselheiro Lafaiete
  - 同じ表の列：dia_semana, mes, temporada, UF, regiao, pais, motivo, selazer_atrativo
- 例2 値：CONTAGEM | CONTAGEM | TRES CORACOES | BELO HORIZONTE | BELO HORIZONTE
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, bairro, sem_carnaval, pernoitar, quantas_pernoites

## g1025（1 列）
- 見出し：UF
- 例1 値：SP | SP | MG | RS | MG
  - 同じ表の列：dia_semana, mes, temporada, Cidade, regiao, pais, motivo, selazer_atrativo

## g1026（1 列）
- 見出し：regiao
- 例1 値：Sudeste | Nordeste | Nordeste | Sudeste | Nordeste
  - 同じ表の列：dia_semana, mes, temporada, Cidade, UF, pais, motivo, selazer_atrativo

## g1027（1 列）
- 見出し：pais
- 例1 値：Estados Unidos | Brasil | Brasil | Brasil | Brasil
  - 同じ表の列：dia_semana, mes, temporada, Cidade, UF, regiao, motivo, selazer_atrativo

## g1028（1 列）
- 見出し：motivo
- 例1 値：Negocios | Lazer _Passeio | Saude_ tratamento_ consulta medica | Visita a amigos e parentes | Estudos ou cursos
  - 同じ表の列：dia_semana, mes, temporada, Cidade, UF, regiao, pais, selazer_atrativo

## g1029（1 列）
- 見出し：selazer_atrativo
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：dia_semana, mes, temporada, Cidade, UF, regiao, pais, motivo

## g1030（1 列）
- 見出し：senegocios_motivo
- 例1 値：NA | NA | NA | NA | Atividade comercial ou industrial _vend…
  - 同じ表の列：dia_semana, mes, temporada, Cidade, UF, regiao, pais, motivo

## g1031（1 列）
- 見出し：local
- 例1 値：BAIANAS OZADAS | QUANDO COME SE LAMBUZA | BAIANAS OZADAS | BEICO DO WANDO | BAIANAS OZADAS
  - 同じ表の列：morador, BH_RMBH, uf_pais, cidade, bairro, sem_carnaval, pernoitar, quantas_pernoites

## g1032（1 列）
- 見出し：morador
- 例1 値：Morador | Morador | Morador | Visitante | Visitante
  - 同じ表の列：local, BH_RMBH, uf_pais, cidade, bairro, sem_carnaval, pernoitar, quantas_pernoites

## g1033（1 列）
- 見出し：BH_RMBH
- 例1 値：Belo Horizonte | Interior de Minas | Belo Horizonte | RMBH | Belo Horizonte
  - 同じ表の列：local, morador, uf_pais, cidade, bairro, sem_carnaval, pernoitar, quantas_pernoites

## g1034（1 列）
- 見出し：uf_pais
- 例1 値：Minas Gerais | Minas Gerais | Minas Gerais | Minas Gerais | Minas Gerais
  - 同じ表の列：local, morador, BH_RMBH, cidade, bairro, sem_carnaval, pernoitar, quantas_pernoites

## g1035（1 列）
- 見出し：bairro
- 例1 値：Cidade Nova | Cachoeirinha | Gutierrez | Santa Terezinha | Savassi
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, cidade, sem_carnaval, pernoitar, quantas_pernoites

## g1036（1 列）
- 見出し：sem_carnaval
- 例1 値：Nao | Sim | Sim | Sim | Sim
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, cidade, bairro, pernoitar, quantas_pernoites

## g1037（1 列）
- 見出し：pernoitar
- 例1 値：Sim | Sim | Sim | Sim | Sim
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, cidade, bairro, sem_carnaval, quantas_pernoites

## g1038（1 列）
- 見出し：quantas_pernoites
- 例1 値：5 | 5 | 10 | 3 | 4
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, cidade, bairro, sem_carnaval, pernoitar

## g1039（1 列）
- 見出し：meio_de_hospedagem
- 例1 値：Casa de Amigos/Parentes | Casa de Amigos/Parentes | Hoteis/Pousadas | Casa de Amigos/Parentes | Casa de Amigos/Parentes
  - 同じ表の列：local, morador, BH_RMBH, uf_pais, cidade, bairro, sem_carnaval, pernoitar

## g1040（1 列）
- 見出し：ID_REDE_PRIORIZACAO_ONIBUS
- 例1 値：1835 | 756 | 1843 | 165 | 2083
  - 同じ表の列：SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA

## g1041（2 列）
- 見出し：SITUACAO
- 例1 値：IMPLANTADA | IMPLANTADA | IMPLANTADA | IMPLANTADA | IMPLANTADA
  - 同じ表の列：ID_REDE_PRIORIZACAO…, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA
- 例2 値：Real | Real | Real | Real | Real
  - 同じ表の列：DESC_SIGLA_TIPO_LOG…, COMPRIMENTO, LARGURA, GEOMETRIA

## g1042（1 列）
- 見出し：INFRAESTRUTURA_PREDOMINANTE
- 例1 値：FAIXA PREFERENCIAL | FAIXA EXCLUSIVA | FAIXA PREFERENCIAL | FAIXA EXCLUSIVA | FAIXA PREFERENCIAL
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA

## g1043（1 列）
- 見出し：ANO_IMPLANT_INFRA_ATUAL
- 例1 値：2014 | 2014 | 1985 | 2018 | 2009
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA

## g1044（1 列）
- 見出し：SISTEMA_BRT
- 例1 値：NÃO | SIM | NÃO | NÃO | SIM
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA

## g1045（1 列）
- 見出し：EXTENSAO_TRECHO
- 例1 値：139.82 | 36.804 | 30.631 | 91.88 | 83.0
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, LOGRAD_INICIAL, LOGRAD_FINAL, GEOMETRIA

## g1046（1 列）
- 見出し：LOGRAD_INICIAL
- 例1 値：RUA BRASILIA | PCA RUI BARBOSA | RUA MALACACHETA | AVE SILVA LOBO | RUA DA BAHIA
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_FINAL, GEOMETRIA

## g1047（1 列）
- 見出し：LOGRAD_FINAL
- 例1 値：AVE AFONSO PENA | RUA QUATRO MIL OITOCENTOS E NOVENTA E O… | AVE SANTOS DUMONT | RUA CORONEL COSTA DIAS | ALA DAS PALMEIRAS
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, GEOMETRIA

## g1048（2 列）
- 見出し：GEOMETRIA
- 例1 値：LINESTRING (606381.05 7795838.07, 60631… | LINESTRING (606624.11 7797958.64, 60660… | LINESTRING (610707.58 7796782.98, 61080… | LINESTRING (607348.08 7797732.96, 60723… | LINESTRING (609538.93 7797291.67, 60958…
  - 同じ表の列：ID_REDE_PRIORIZACAO…, SITUACAO, INFRAESTRUTURA_PRED…, ANO_IMPLANT_INFRA_A…, SISTEMA_BRT, EXTENSAO_TRECHO, LOGRAD_INICIAL, LOGRAD_FINAL
- 例2 値：LINESTRING (612861.95 7804957.42, 61286… | LINESTRING (609411.56 7796258.30, 60927… | LINESTRING (609790.14 7808963.71, 60979… | LINESTRING (613445.18 7803194.83, 61348… | LINESTRING (604224.12 7787673.81, 60421…
  - 同じ表の列：DESC_SIGLA_TIPO_LOG…, COMPRIMENTO, LARGURA, SITUACAO

## g1049（1 列）
- 見出し：ID_POSTO_VENDA_ROTATIVO
- 例1 値：348143 | 348395 | 348464 | 348116 | 348272
  - 同じ表の列：GEOMETRIA

## g1050（5 列）
- 見出し：GEOMETRIA
- 例1 値：POINT (610271.236856672 7796332.3755177… | POINT (609653.868441401 7796900.9117506… | POINT (612103.789277546 7794606.3595493… | POINT (611473.197609301 7797276.4122324… | POINT (611409.167536081 7794934.7538147…
  - 同じ表の列：ID_POSTO_VENDA_ROTA…
- 例2 値：POINT (611091.432949963 7796529.1110803… | POINT (611293.412741149 7796773.5854895… | POINT (603877.325617307 7794040.1777495… | POINT (610580.494391233 7798438.4546868… | POINT (611208.701692459 7796918.6985564…
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, COD_SECUNDARIA

## g1051（1 列）
- 見出し：ID_FISCALIZACAO_ELETRONICA
- 例1 値：565 | 566 | 646 | 642 | 353
  - 同じ表の列：DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, COD_SECUNDARIA, GEOMETRIA

## g1052（1 列）
- 見出し：DESC_TIPO_CONTROLADOR_TRANSITO
- 例1 値：Detector de Parada sobre Faixa de Pedes… | Detector de Avanço de Semáforo | Detector de Avanço de Semáforo | Detector de Avanço de Semáforo | Detector de Avanço de Semáforo
  - 同じ表の列：ID_FISCALIZACAO_ELE…, VELOCIDADE_REGULAME…, SENTIDO, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, COD_SECUNDARIA, GEOMETRIA

## g1053（1 列）
- 見出し：VELOCIDADE_REGULAMENTAR
- 例1 値：30 | 60 | 60 | 60 | 60
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, SENTIDO, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, COD_SECUNDARIA, GEOMETRIA

## g1054（1 列）
- 見出し：SENTIDO
- 例1 値：Barro Preto/Viaduto Oeste | Bairro/Centro | Bairro/Centro | Bairro/Centro e Centro/Bairro | Bairro/Centro
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, COD_SECUNDARIA, GEOMETRIA

## g1055（1 列）
- 見出し：SENTIDO_FISCALIZADO
- 例1 値：Único | Único | Único | Único | Único
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO, NUM_SERIE_ATUAL, COD_SECUNDARIA, GEOMETRIA

## g1056（1 列）
- 見出し：NUM_SERIE_ATUAL
- 例1 値：3272 | 9701 | 1026 | 295 | 3269
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO, SENTIDO_FISCALIZADO, COD_SECUNDARIA, GEOMETRIA

## g1057（1 列）
- 見出し：COD_SECUNDARIA
- 例1 値：GCT032 | 9698 | 3003 | GCT002 | 393205021
  - 同じ表の列：ID_FISCALIZACAO_ELE…, DESC_TIPO_CONTROLAD…, VELOCIDADE_REGULAME…, SENTIDO, SENTIDO_FISCALIZADO, NUM_SERIE_ATUAL, GEOMETRIA

## g1058（1 列）
- 見出し：ID_QUADRA_CEMITERIO
- 例1 値：303 | 17 | 35 | 54 | 10
  - 同じ表の列：NUM_QUADRA_CEMITERIO, GEOMETRIA

## g1059（1 列）
- 見出し：NUM_QUADRA_CEMITERIO
- 例1 値：41 | 29 | 29 | 32 | 2
  - 同じ表の列：ID_QUADRA_CEMITERIO, GEOMETRIA

## g1060（5 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((609534.00 7797955.75, 609520.… | POLYGON ((609600.04 7798130.25, 609598.… | POLYGON ((608561.98 7799702.90, 608560.… | POLYGON ((608386.93 7799451.86, 608369.… | POLYGON ((608284.57 7799343.09, 608275.…
  - 同じ表の列：ID_QUADRA_CEMITERIO, NUM_QUADRA_CEMITERIO
- 例2 値：POLYGON ((612889.15 7803494.57, 612874.… | POLYGON ((614709.39 7807719.89, 614708.… | POLYGON ((602381.86 7790090.82, 602393.… | POLYGON ((609226.94 7810448.41, 609247.… | POLYGON ((617126.12 7806542.66, 617099.…
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO

## g1061（1 列）
- 見出し：Ano
- 例1 値：2020 | 2020 | 2018 | 2019 | 2017
  - 同じ表の列：Modalidade, Codigo unidade, Regional, Valor

## g1062（1 列）
- 見出し：Modalidade
- 例1 値：Reposicao ambiental por supressao arbor… | Reposicao ambiental por supressao arbor… | Reposicao ambiental por supressao arbor… | Reposicao ambiental por supressao arbor… | Reposicao ambiental por supressao arbor…
  - 同じ表の列：Ano, Codigo unidade, Regional, Valor

## g1063（2 列）
- 見出し：Codigo unidade
- 例1 値：3001 | 3065 | 3002 | 3013 | 3001
  - 同じ表の列：Ano, Modalidade, Regional, Valor
- 例2 値：3056 | 3010 | 3014 | 3048 | 3063
  - 同じ表の列：Area, Perimetro, Aberto, Legislacao, Cercamento, Ano criacao, Ano abertura, Bairro popular

## g1064（1 列）
- 見出し：Regional
- 例1 値：Pampulha | Centro-Sul | Venda Nova | Pampulha | Nao se aplica
  - 同じ表の列：Ano, Modalidade, Codigo unidade, Valor

## g1065（1 列）
- 見出し：Valor
- 例1 値：23230,43 | 24328,72 | 10000 | 6136,34 | 2008,4
  - 同じ表の列：Ano, Modalidade, Codigo unidade, Regional

## g1066（1 列）
- 見出し：Area
- 例1 値：27953,92 | 83835,56 | 180497,81 | 53170,69 | 30942,87
  - 同じ表の列：Codigo unidade, Perimetro, Aberto, Legislacao, Cercamento, Ano criacao, Ano abertura, Bairro popular

## g1067（1 列）
- 見出し：Perimetro
- 例1 値：2138,21 | 1452,51 | 544,09 | 511,82 | 436,77
  - 同じ表の列：Codigo unidade, Area, Aberto, Legislacao, Cercamento, Ano criacao, Ano abertura, Bairro popular

## g1068（1 列）
- 見出し：Aberto
- 例1 値：Sim | Sim | Nao | Sim | Sim
  - 同じ表の列：Codigo unidade, Area, Perimetro, Legislacao, Cercamento, Ano criacao, Ano abertura, Bairro popular

## g1069（1 列）
- 見出し：Legislacao
- 例1 値：Lei Municipal no. 7.550/1998 | Lei Municipal n°. 9.095/2005 e Decreto … | Lei Municipal n°. 7.432/1998 | Decreto Municipal n°. 12.279/2006 | Decreto Municipal n°. 2.065/1971, Decre…
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Cercamento, Ano criacao, Ano abertura, Bairro popular

## g1070（1 列）
- 見出し：Cercamento
- 例1 値：Sim | Nao | Parcial | Nao | Sim
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Legislacao, Ano criacao, Ano abertura, Bairro popular

## g1071（1 列）
- 見出し：Ano criacao
- 例1 値：1990 | 2012 | 1999 | 1990 | 1942
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Legislacao, Cercamento, Ano abertura, Bairro popular

## g1072（1 列）
- 見出し：Ano abertura
- 例1 値：2002 | 2018 | 1996 | 2008 | 1995
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Legislacao, Cercamento, Ano criacao, Bairro popular

## g1073（1 列）
- 見出し：Bairro popular
- 例1 値：Lagoa | Sao Francisco | Santo Antonio | Luxemburgo | Planalto
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Legislacao, Cercamento, Ano criacao, Ano abertura

## g1074（1 列）
- 見出し：TGC
- 例1 値：NE5 | CS2 | O3 | CS2 | NE2
  - 同じ表の列：Codigo unidade, Area, Perimetro, Aberto, Legislacao, Cercamento, Ano criacao, Ano abertura

## g1075（1 列）
- 見出し：CODIGO CONTA
- 例1 値：4.1.0.10.10001 | 3.1.0.10.50013 | 1.1.0.20.90006 | 2.1.0.60.20001 | 1.1.0.10.40008
  - 同じ表の列：GRUPO, CLASSIFICACAO 1, CLASSIFICACAO 2, CONTA SINTETICA, CONTA ANALITICA, SALDO ANTERIOR, DEBITO, CREDITO

## g1076（1 列）
- 見出し：GRUPO
- 例1 値：CUSTOS E DESPESAS | PASSIVO | CUSTOS E DESPESAS | PASSIVO | PASSIVO
  - 同じ表の列：CODIGO CONTA, CLASSIFICACAO 1, CLASSIFICACAO 2, CONTA SINTETICA, CONTA ANALITICA, SALDO ANTERIOR, DEBITO, CREDITO

## g1077（1 列）
- 見出し：CLASSIFICACAO 1
- 例1 値：RECEITAS OPERACIONAIS | CUSTOS E DESPESAS OPERACIONAIS | PASSIVO CIRCULANTE | RECEITAS OPERACIONAIS | PATRIMONIO LIQUIDO
  - 同じ表の列：CODIGO CONTA, GRUPO, CLASSIFICACAO 2, CONTA SINTETICA, CONTA ANALITICA, SALDO ANTERIOR, DEBITO, CREDITO

## g1078（1 列）
- 見出し：CLASSIFICACAO 2
- 例1 値：CAIXA E EQUIVALENTES DE CAIXA | CUSTOS E DESPESAS OPERACIONAIS | REALIZAVEL A LONGO PRAZO | DEBENTURES NAO CONVERSIVEIS EM ACOES - … | CUSTOS E DESPESAS OPERACIONAIS
  - 同じ表の列：CODIGO CONTA, GRUPO, CLASSIFICACAO 1, CONTA SINTETICA, CONTA ANALITICA, SALDO ANTERIOR, DEBITO, CREDITO

## g1079（1 列）
- 見出し：CONTA SINTETICA
- 例1 値：OUTRAS VARIACOES DE CREDITO | BANCOS CONTA MOVIMENTO | PROVISAO IRPJ E CSLL DIFERIDOS - CREDIT… | OUTRAS VARIACOES DE CREDITO | SALDO NEGATIVO DO CSLL
  - 同じ表の列：CODIGO CONTA, GRUPO, CLASSIFICACAO 1, CLASSIFICACAO 2, CONTA ANALITICA, SALDO ANTERIOR, DEBITO, CREDITO

## g1080（1 列）
- 見出し：CONTA ANALITICA
- 例1 値：DIREITOS CREDITORIOS A RECEBER | CARTORIOS E CERTIDOES | VARIACAO MONETARIA | IRPJ A RECOLHER | CEF 3792-5 REC COPASA FIC TOP
  - 同じ表の列：CODIGO CONTA, GRUPO, CLASSIFICACAO 1, CLASSIFICACAO 2, CONTA SINTETICA, SALDO ANTERIOR, DEBITO, CREDITO

## 答えの雛形

```
g0961	
g0962	
g0963	
g0964	
g0965	
g0966	
g0967	
g0968	
g0969	
g0970	
g0971	
g0972	
g0973	
g0974	
g0975	
g0976	
g0977	
g0978	
g0979	
g0980	
g0981	
g0982	
g0983	
g0984	
g0985	
g0986	
g0987	
g0988	
g0989	
g0990	
g0991	
g0992	
g0993	
g0994	
g0995	
g0996	
g0997	
g0998	
g0999	
g1000	
g1001	
g1002	
g1003	
g1004	
g1005	
g1006	
g1007	
g1008	
g1009	
g1010	
g1011	
g1012	
g1013	
g1014	
g1015	
g1016	
g1017	
g1018	
g1019	
g1020	
g1021	
g1022	
g1023	
g1024	
g1025	
g1026	
g1027	
g1028	
g1029	
g1030	
g1031	
g1032	
g1033	
g1034	
g1035	
g1036	
g1037	
g1038	
g1039	
g1040	
g1041	
g1042	
g1043	
g1044	
g1045	
g1046	
g1047	
g1048	
g1049	
g1050	
g1051	
g1052	
g1053	
g1054	
g1055	
g1056	
g1057	
g1058	
g1059	
g1060	
g1061	
g1062	
g1063	
g1064	
g1065	
g1066	
g1067	
g1068	
g1069	
g1070	
g1071	
g1072	
g1073	
g1074	
g1075	
g1076	
g1077	
g1078	
g1079	
g1080	
```
