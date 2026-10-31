# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Active ingredients - French
- 例1 値：EXTRAIT DE BLATTE GERMANIQUE (N.M.) | PROTHIOCONAZOLE (N.M.) | BROMOXYNIL (N.M.) | BUTOXYDE DE PIPÉRONYLE (N.M.);PYRÉTHRIN… | GLUTARALDÉHYDE (N.M.)
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Purpose, Registration number, Registration status, Category

## g0122（1 列）
- 見出し：Purpose
- 例1 値：Amendment | New | New | New | Amendment
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Active ingredients …, Registration number, Registration status, Category

## g0123（1 列）
- 見出し：Registration number
- 例1 値：25029 | 19176 | 11763 | 28511 | 24834
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration status, Category

## g0124（1 列）
- 見出し：Registration status
- 例1 値：Full Registration | Full Registration | Full Registration | Full Registration | Full Registration
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration number, Category

## g0125（1 列）
- 見出し：Category
- 例1 値：N | A | A | R | C
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration number, Registration status

## g0126（1 列）
- 見出し：Product type
- 例1 値：SLIMICIDE | INSECTICIDE | ANIMAL REPELLENT | HERBICIDE | HERBICIDE
  - 同じ表の列：Application number, Date received, Outcome, Active ingredients …, Active ingredients …, Purpose, Registration number, Registration status

## g0127（1 列）
- 見出し：Naics code Code Scian
- 例1 値：111 | 22133 | 53 | 32611 | 412
  - 同じ表の列：Year Année

## g0128（1 列）
- 見出し：Year Année
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：Naics code Code Sci…

## g0129（1 列）
- 見出し：Jurisdiction
- 例1 値：SK | MB | NS | Canada | Revenues refer to all monies received b…
  - 同じ表の列：Type of Revenue

## g0130（1 列）
- 見出し：Type of Revenue
- 例1 値：4,795,431 | 182,770,135 | 846,262,419 | 25,376,874 | 81,989,096
  - 同じ表の列：Jurisdiction

## g0131（1 列）
- 見出し：Layer
- 例1 値：Projects Referred to MPO | Projects Referred to MPO | Projects Referred to MPO | Projects Referred to MPO | Transformative Strategies
  - 同じ表の列：Vector, Icon, Location, Proponent, Sector, Status, Coordinates, Link

## g0132（1 列）
- 見出し：Vector
- 例1 値：Point | Two points | Polygon | Point | Point
  - 同じ表の列：Layer, Icon, Location, Proponent, Sector, Status, Coordinates, Link

## g0133（1 列）
- 見出し：Icon
- 例1 値：Transport (dark grey with car) | Electricity (blue light bulb) | Highlight BC and YK | Transport (dark grey with car) | Highlight all PTs except PEI
  - 同じ表の列：Layer, Vector, Location, Proponent, Sector, Status, Coordinates, Link

## g0134（1 列）
- 見出し：Location
- 例1 値：Northwestern British Columbia | Bruderheim, Alberta to Southern British… | Manitoba | All of Canada | Wabigoon Lake Ojibway Nation and the To…
  - 同じ表の列：Layer, Vector, Icon, Proponent, Sector, Status, Coordinates, Link

## g0135（1 列）
- 見出し：Proponent
- 例1 値：Nisg̱a’a Nation, Rockies LNG Limited Pa… | Newmont Mining and Imperial Metals | BC Hydro | LNG Canada | Ontario Power Generation
  - 同じ表の列：Layer, Vector, Icon, Location, Sector, Status, Coordinates, Link

## g0136（1 列）
- 見出し：Sector
- 例1 値：Electricity | Transport and Infrastructure | Electricity, Energy | Transport and Infrastructure | Mining
  - 同じ表の列：Layer, Vector, Icon, Location, Proponent, Status, Coordinates, Link

## g0137（1 列）
- 見出し：Status
- 例1 値：Referred to MPO for consideration | Referred to MPO for consideration | Referred to MPO for consideration | This project has been listed under the … | Transformative projects
  - 同じ表の列：Layer, Vector, Icon, Location, Proponent, Sector, Coordinates, Link

## g0138（1 列）
- 見出し：Coordinates
- 例1 値：60.420058, -111.39231 | 45.822674, -73.292881 | N/A | Start point: 62.45369, -114.370665; End… | N/A
  - 同じ表の列：Layer, Vector, Icon, Location, Proponent, Sector, Status, Link

## g0139（1 列）
- 見出し：Link
- 例1 値：https://www.canada.ca/en/privy-council/… | https://www.canada.ca/en/privy-council/… | https://www.canada.ca/en/privy-council/… | https://www.canada.ca/en/privy-council/… | https://www.canada.ca/en/privy-council/…
  - 同じ表の列：Layer, Vector, Icon, Location, Proponent, Sector, Status, Coordinates

## g0140（1 列）
- 見出し：Updated as of
- 例1 値：12/1/2017 | 11/1/2017 | 12/1/2017 | 12/1/2017 | 11/1/2017
  - 同じ表の列：ID, Priority, Commitment, Minister, Status, Results.Statement

## g0141（1 列）
- 見出し：ID
- 例1 値：101_1 | 210 | 169 | 64 | 117
  - 同じ表の列：Updated as of, Priority, Commitment, Minister, Status, Results.Statement

## g0142（1 列）
- 見出し：Priority
- 例1 値：Fair and Open Government | Healthy Canadians | Healthy Canadians | Diverse and Inclusive Canada | Diverse and Inclusive Canada
  - 同じ表の列：Updated as of, ID, Commitment, Minister, Status, Results.Statement

## g0143（1 列）
- 見出し：Commitment
- 例1 値：End Canada's combat mission in Iraq and… | Lead preparations for future internatio… | Provide new funding to preserve and enh… | Maintain current National Defence spend… | Develop a vision for a national space f…
  - 同じ表の列：Updated as of, ID, Priority, Minister, Status, Results.Statement

## g0144（1 列）
- 見出し：Minister
- 例1 値：Minister of Indigenous Services | Minister of Foreign Affairs | Minister of Fisheries, Oceans and the C… | Minister of Health | Minister of Employment, Workforce Devel…
  - 同じ表の列：Updated as of, ID, Priority, Commitment, Status, Results.Statement

## g0145（1 列）
- 見出し：Status
- 例1 値：Underway - on track | Completed - fully met | On-going commitment | Underway - on track | Underway - on track
  - 同じ表の列：Updated as of, ID, Priority, Commitment, Minister, Results.Statement

## g0146（1 列）
- 見出し：Results.Statement
- 例1 値：The recommendations of the Expert Panel… | Indigenous students have greater access… | Canadians have the information, tools a… | Caregivers of critically ill or injured… | Additional commitment
  - 同じ表の列：Updated as of, ID, Priority, Commitment, Minister, Status

## g0147（1 列）
- 見出し：Aggregator
- 例1 値：60 years or more | 40 to 49 years | 2022 | 30 to 39 years | 2025
  - 同じ表の列：Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types, PRUID

## g0148（1 列）
- 見出し：Aggregator_FR
- 例1 値：2022 | 2026 (janv. à mars) | 2024 | 2016 | 2021
  - 同じ表の列：Aggregator, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types, PRUID

## g0149（1 列）
- 見出し：DataTableChart
- 例1 値：2025 | 2023 Q2 | 2019 - Accidental | 2024 - Nova Scotia | 2024 - 60 years or more
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types, PRUID

## g0150（1 列）
- 見出し：DataTableChart_FR
- 例1 値：2023 (janv. à mars) | 20 à 29 ans - Femme | 2017 | 2019 | 2019 T1
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types, PRUID

## g0151（1 列）
- 見出し：Disaggregator
- 例1 値：Female | Male | Male | Methamphetamine | Male
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator_FR, Geography_URI, Graph_Types, PRUID

## g0152（1 列）
- 見出し：Disaggregator_FR
- 例1 値：Homme | Femme | 40 à 49 ans | Homme | 20 à 29 ans
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Geography_URI, Graph_Types, PRUID

## g0153（1 列）
- 見出し：Geography_URI
- 例1 値：https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i…
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Graph_Types, PRUID

## g0154（1 列）
- 見出し：Graph_Types
- 例1 値：GROUPED | GROUPED | GROUPED | BAR | BAR
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, PRUID

## g0155（3 列）
- 見出し：PRUID
- 例1 値：12 | 11 | 61 | 59 | 60
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types
- 例2 値：24 | 12 | 11 | 12 | 59
  - 同じ表の列：week_end, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…

## g0156（1 列）
- 見出し：Period_URI
- 例1 値：https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i… | https://health-infobase.canada.ca/api/i…
  - 同じ表の列：Aggregator, Aggregator_FR, DataTableChart, DataTableChart_FR, Disaggregator, Disaggregator_FR, Geography_URI, Graph_Types

## g0157（2 列）
- 見出し：week_end
- 例1 値：2021-01-09 | 2021-09-25 | 2022-05-08 | 2020-12-19 | 2022-01-15
  - 同じ表の列：pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…
- 例2 値：2021-04-03 | 2021-05-15 | 2021-01-23 | 2021-04-17 | 2021-05-01
  - 同じ表の列：pruid, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0158（2 列）
- 見出し：numtotal_atleast1dose
- 例1 値：142524 | 149351 | 36494 | 27213 | 32479506
  - 同じ表の列：week_end, pruid, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…
- 例2 値：283586 | 48 | 5 | 18231 | 32673
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0159（2 列）
- 見出し：numtotal_partially
- 例1 値：7298 | 197933 | 5464 | 6241 | 59121
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…
- 例2 値：163293 | 1550423 | 2940 | 3674489 | 2576
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_fully, prop_atleast1dose, prop_partially

## g0160（2 列）
- 見出し：numtotal_fully
- 例1 値：4264133 | 659331 | 603827 | 2565 | 433648
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_onlyfully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…
- 例2 値：1885 | 539 | 34282 | 24 | 10658
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, prop_atleast1dose, prop_partially

## g0161（1 列）
- 見出し：numtotal_onlyfully
- 例1 値：417695 | 423122 | 62429 | 2769975 | 13160626
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_additional, numtotal_1additional, numtotal_2nd_additi…

## g0162（1 列）
- 見出し：numtotal_additional
- 例1 値：7029219 | 430398 | 14474 | 1499675 | 15222
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_1additional, numtotal_2nd_additi…

## g0163（1 列）
- 見出し：numtotal_1additional
- 例1 値：6375311 | 586634 | 16743869 | 6749861 | 380797
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_2nd_additi…

## g0164（1 列）
- 見出し：numtotal_2nd_additional
- 例1 値：3818 | 6669 | 996308 | 1800 | 110266
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional

## g0165（1 列）
- 見出し：proptotal_atleast1dose
- 例1 値：70.7 | 81.9 | 39.2 | 72.5 | 84.5
  - 同じ表の列：week_end, pruid, numtotal_atleast1do…, numtotal_partially, numtotal_fully, numtotal_onlyfully, numtotal_additional, numtotal_1additional

## g0166（1 列）
- 見出し：series_type
- 例1 値：1 | 3 | 1 | 1 | 1
  - 同じ表の列：pruid, week_end, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0167（1 列）
- 見出し：primary_series
- 例1 値：AstraZeneca Vaxzevria/COVISHIELD | Pfizer-BioNTech Comirnaty | Moderna Spikevax | Not reported | AstraZeneca Vaxzevria/COVISHIELD
  - 同じ表の列：pruid, week_end, series_type, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially

## g0168（1 列）
- 見出し：prop_atleast1dose
- 例1 値：<0.1 | 2.5 | 5.5 | <0.1 | 5
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_partially

## g0169（1 列）
- 見出し：prop_partially
- 例1 値：2.2 | 1.1 | 0.8 | 4.4 | 1.8
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose

## g0170（1 列）
- 見出し：prop_fully
- 例1 値：2.5 | 1 | <0.1 | <0.1 | 2.4
  - 同じ表の列：pruid, week_end, series_type, primary_series, numtotal_atleast1do…, numtotal_partially, numtotal_fully, prop_atleast1dose

## g0171（2 列）
- 見出し：referenceNumber-numeroReference
- 例1 値：MX-443506536184 | cb-710-48966764 | cb-277-10754436 | cb-300-93133966 | MX-443534751952
  - 同じ表の列：amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…
- 例2 値：MX-243100733812 | cb-401-80908121 | MX-243100732115 | MX-243100734307 | MX-243100734460
  - 同じ表の列：title-titre-eng, title-titre-fra, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0172（2 列）
- 見出し：amendmentNumber-numeroModification
- 例1 値：001 | 000 | 000 | 000 | 000
  - 同じ表の列：referenceNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…
- 例2 値：000 | 000 | 000 | 000 | 000
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0173（2 列）
- 見出し：publicationDate-datePublication
- 例1 値：2025-09-15 | 2025-09-15 | 2024-09-09 | 2026-04-23 | 2025-11-10
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…
- 例2 値：2026-10-30 | 2026-10-31 | 2026-10-30 | 2026-10-30 | 2026-10-30
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0174（1 列）
- 見出し：contractAwardDate-dateAttributionContrat
- 例1 値：2024-03-04 | 2026-07-31 | 2025-03-14 | 2025-05-05 | 2024-04-24
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0175（1 列）
- 見出し：amendmentDate-dateModification
- 例1 値：2025-10-31 | 2026-03-31 | 2026-03-31 | 2026-06-30 | 2025-03-31
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0176（1 列）
- 見出し：contractStartDate-contratDateDebut
- 例1 値：2023-05-04 | 2025-11-01 | 2025-09-16 | 2025-01-06 | 2025-06-01
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractEndDate-dat…, contractAmount-mont…, totalContractValue-…

## g0177（1 列）
- 見出し：contractEndDate-dateFinContrat
- 例1 値：2026-04-03 | 2022-04-30 | 2022-09-02 | 2026-09-30 | 2026-10-16
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractAmount-mont…, totalContractValue-…

## g0178（1 列）
- 見出し：contractAmount-montantContrat
- 例1 値：595000.00 | 0.00 | 0.00 | 775000.00 | 0.00
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, totalContractValue-…

## g0179（1 列）
- 見出し：totalContractValue-valeurTotaleContrat
- 例1 値：0.00 | 0.00 | 0.00 | 113250.00 | 0.00
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…

## g0180（1 列）
- 見出し：contractCurrency-contratMonnaie
- 例1 値：CAD | CAD | CAD | CAD | CAD
  - 同じ表の列：referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, contractAwardDate-d…, amendmentDate-dateM…, contractStartDate-c…, contractEndDate-dat…, contractAmount-mont…

## g0181（1 列）
- 見出し：title-titre-eng
- 例1 値：APN-Bottled Water Supply & Delivery Ser… | Leadership Assessment and Coaching Serv… | Request for Abbreviated Proposals for G… | APN-Cultural & Archaeological Assessmen… | Training Facility for Vehicle Technicia…
  - 同じ表の列：title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0182（1 列）
- 見出し：title-titre-fra
- 例1 値：Demande de propositions abrégées pour s… | Services d’évaluation et d’encadrement … | PA-RF Service d’évaluation et de survei… | PA-Services d'approvisionnement et de l… | Centre de formation pour la formation d…
  - 同じ表の列：title-titre-eng, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0183（1 列）
- 見出し：solicitationNumber-numeroSollicitation
- 例1 値：APN_88216 | W3915-27-0110 | KN27SL01 | OR26SO02_88083 | 26-143
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…, expectedContractEnd…

## g0184（1 列）
- 見出し：tenderClosingDate-appelOffresDateCloture
- 例1 値：2026-11-13T14:00:00 | 2026-12-15T14:00:00 | 2026-12-09T14:00:00 | 2026-12-09T14:00:00 | 2026-12-04T13:00:00
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, expectedContractSta…, expectedContractEnd…

## g0185（1 列）
- 見出し：expectedContractStartDate-dateDebutContratPrevue
- 例1 値：2026-12-16 | 2027-05-01 | 2026-12-16
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractEnd…

## g0186（1 列）
- 見出し：expectedContractEndDate-dateFinContratPrevue
- 例1 値：2026-12-16 | 2026-12-16 | 2027-09-30
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…

## g0187（1 列）
- 見出し：tenderStatus-appelOffresStatut-eng
- 例1 値：Open | Open | Open | Open | Open
  - 同じ表の列：title-titre-eng, title-titre-fra, referenceNumber-num…, amendmentNumber-num…, solicitationNumber-…, publicationDate-dat…, tenderClosingDate-a…, expectedContractSta…

## g0188（1 列）
- 見出し：Participation Type
- 例1 値：Account Consignor | Account Consignor | Account Consignor | Account Consignor | Account Consignor
  - 同じ表の列：City, Province

## g0189（1 列）
- 見出し：City
- 例1 値：SMITHERS | Whitehorse | Laval | Calgary | QUEBEC
  - 同じ表の列：Participation Type, Province

## g0190（1 列）
- 見出し：prj_cd
- 例1 値：000009710 | 000010958 | 000012316 | 000015022 | 000010861
  - 同じ表の列：prov_cd, sup_city, lat, lng

## g0191（1 列）
- 見出し：prov_cd
- 例1 値：BC | BC | MB | BC | MB
  - 同じ表の列：prj_cd, sup_city, lat, lng

## g0192（1 列）
- 見出し：sup_city
- 例1 値：Calgary | Grand Forks | Fort McMurray | Moosomin | Tisdale
  - 同じ表の列：prj_cd, prov_cd, lat, lng

## g0193（1 列）
- 見出し：lat
- 例1 値：52.129831 | 49.841864 | 49.097888 | 53.933265 | 49.895623
  - 同じ表の列：prj_cd, prov_cd, sup_city, lng

## g0194（1 列）
- 見出し：lng
- 例1 値：-113.451686 | -119.129046 | -122.752106 | -113.490761 | -97.132795
  - 同じ表の列：prj_cd, prov_cd, sup_city, lat

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
```
