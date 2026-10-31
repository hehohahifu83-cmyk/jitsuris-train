# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（17 列）
- 見出し：Department Family
- 例1 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Entity, Payment Date, Expense Type, Supplier, Sum of Amount
- 例2 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Entity (T), Date, Expense Type (T), Expense Area (T), Supplier (T), Transaction Number, AP Amount

## g0002（6 列）
- 見出し：Entity
- 例1 値：Black Country Partnership NHS Foundatio… | Black Country Partnership NHS Foundatio… | Black Country Partnership NHS Foundatio… | Black Country Partnership NHS Foundatio… | Black Country Partnership NHS Foundatio…
  - 同じ表の列：Department Family, Payment Date, Expense Type, Supplier, Sum of Amount
- 例2 値：Maidstone and Tunbridge Wells NHS Trust | Maidstone and Tunbridge Wells NHS Trust | Maidstone and Tunbridge Wells NHS Trust | Maidstone and Tunbridge Wells NHS Trust | Maidstone and Tunbridge Wells NHS Trust
  - 同じ表の列：Department Family, Cleared Date, Expense Type, Expense Area, Reference, Line Value, Vat Reg No

## g0003（2 列）
- 見出し：Payment Date
- 例1 値：11/11/2020 | 25/11/2020 | 18/11/2020 | 04/11/2020 | 11/11/2020
  - 同じ表の列：Department Family, Entity, Expense Type, Supplier, Sum of Amount
- 例2 値：16/08/2022 | 23/08/2022 | 09/08/2022 | 23/08/2022 | 09/08/2022
  - 同じ表の列：Department Family, Supplier Type, Supplier, Supplier Number, Payment Document, Payment Method, Payment Number, Payment Currency

## g0004（1 列）
- 見出し：Expense Type
- 例1 値：Other Receivables | Drug Costs | Non Clinical Supplies | Premises - Other | Other Receivables
  - 同じ表の列：Department Family, Entity, Payment Date, Supplier, Sum of Amount

## g0005（1 列）
- 見出し：Supplier
- 例1 値：University of York | LIAISON (TEMPRE DISBURSEMENT) | BIST GROUP | Kier Services Maintenance East | MILLS & REEVES SOLICITORS
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Sum of Amount

## g0006（1 列）
- 見出し：Sum of Amount
- 例1 値：40,000.00 | 45,416.68 | -47,490.31 | 490.96 | 40,000.00
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Supplier

## g0007（1 列）
- 見出し：FE Capital Investment Programme
- 例1 値：The first MPA Annual Report in May 2013… | Programme is currently forecasting a ba… | To renew and modernise the FE College e… | Amber/Green | BIS
  - 同じ表の列：The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0008（1 列）
- 見出し：The Francis Crick Institute (formerly UKCMRI)
- 例1 値：753 | 0.00% | 21/12/2017 | 112 | The Total (WLC) cost for the Crick proj…
  - 同じ表の列：FE Capital Investme…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0009（1 列）
- 見出し：Green Investment Bank
- 例1 値：GIB became fully operational in October… | 01/06/2010 | 278 | BIS | 0
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0010（1 列）
- 見出し：HE Reform Programme
- 例1 値：1180 | 31/12/2015 | 4600 | BIS | The Amber/Green status reflects that st…
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0011（1 列）
- 見出し：Royal Mail Sale of Shares
- 例1 値：BIS | Only the non-Government spend is classi… | 380 | To sustain the universal postal service… | The Project start date is given as June…
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, BIS Shared Services, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0012（1 列）
- 見出し：BIS Shared Services
- 例1 値：0 | N/A | 19.27 | 3.785 | The variance in whole life cost is a re…
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, SLC Transformation …, ICR Monetisation, Urenco Future Optio…

## g0013（1 列）
- 見出し：SLC Transformation Programme
- 例1 値：19.86 | BIS | The Amber status reflected the requirem… | No departmental narrative | 19/03/2016
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, ICR Monetisation, Urenco Future Optio…

## g0014（1 列）
- 見出し：ICR Monetisation
- 例1 値：28.61 | Previously an end date reflecting the e… | HM Government is carrying out a program… | 31/12/2018 | 0
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, Urenco Future Optio…

## g0015（1 列）
- 見出し：Urenco Future Options
- 例1 値：18.416 | Whole life costs represent the cumulati… | Data exempt under section 27 and sectio… | BIS | Data exempt under section 27 and sectio…
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation

## g0016（1 列）
- 見出し：Further Education 24+ Learning Loans Programme
- 例1 値：30/11/2010 | To Introduce loans for those aged 24 or… | 84.604 | Amber/Red | No departmental narrative
  - 同じ表の列：FE Capital Investme…, The Francis Crick I…, Green Investment Ba…, HE Reform Programme, Royal Mail Sale of …, BIS Shared Services, SLC Transformation …, ICR Monetisation

## g0017（1 列）
- 見出し：Department
- 例1 値：NHS | NHS | NHS | NHS | NHS
  - 同じ表の列：Entity, Payment Date, Supplier, Transaction No., Line No, Amount

## g0018（1 列）
- 見出し：Entity
- 例1 値：Coventry & Warwickshire Partnership NHS… | Coventry & Warwickshire Partnership NHS… | Coventry & Warwickshire Partnership NHS… | Coventry & Warwickshire Partnership NHS… | Coventry & Warwickshire Partnership NHS…
  - 同じ表の列：Department, Payment Date, Supplier, Transaction No., Line No, Amount

## g0019（1 列）
- 見出し：Payment Date
- 例1 値：20100630 | 20100630 | 20100623 | 20100419 | 20100602
  - 同じ表の列：Department, Entity, Supplier, Transaction No., Line No, Amount

## g0020（1 列）
- 見出し：Supplier
- 例1 値：Lloyds Pharmacy | Lloyds Pharmacy | Hortons' Estate Limited | Lloyds Pharmacy | Lloyds Pharmacy
  - 同じ表の列：Department, Entity, Payment Date, Transaction No., Line No, Amount

## g0021（1 列）
- 見出し：Transaction No.
- 例1 値：92060 | 89541 | 93301 | 93301 | 90915
  - 同じ表の列：Department, Entity, Payment Date, Supplier, Line No, Amount

## g0022（1 列）
- 見出し：Line No
- 例1 値：5 | 9 | 9 | 2 | 12
  - 同じ表の列：Department, Entity, Payment Date, Supplier, Transaction No., Amount

## g0023（3 列）
- 見出し：Amount
- 例1 値：21674.4 | 11827.3 | 28340.97 | 434015.63 | 1928292.5
  - 同じ表の列：Department, Entity, Payment Date, Supplier, Transaction No., Line No
- 例2 値：70286.96 | 52440.00 | 36735.00 | 170738.65 | 100800.00
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier

## g0024（1 列）
- 見出し：Entity (T)
- 例1 値：Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH…
  - 同じ表の列：Department Family, Date, Expense Type (T), Expense Area (T), Supplier (T), Transaction Number, AP Amount

## g0025（14 列）
- 見出し：Date
- 例1 値：27/11/2023 | 30/11/2023 | 23/11/2023 | 30/11/2023 | 06/11/2023
  - 同じ表の列：Department Family, Entity (T), Expense Type (T), Expense Area (T), Supplier (T), Transaction Number, AP Amount
- 例2 値：30/11/2021 | 30/11/2021 | 30/11/2021 | 30/11/2021 | 30/11/2021
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0026（1 列）
- 見出し：Expense Type (T)
- 例1 値：NonNHS Trade Pybls Curr | VAT Cont Out Serv Inp Tax | VAT Cont Out Serv Inp Tax | Continence Products | VAT Cont Out Serv Inp Tax
  - 同じ表の列：Department Family, Entity (T), Date, Expense Area (T), Supplier (T), Transaction Number, AP Amount

## g0027（1 列）
- 見出し：Expense Area (T)
- 例1 値：IM&T | BALANCE SHEET | BALANCE SHEET | IM&T | BALANCE SHEET
  - 同じ表の列：Department Family, Entity (T), Date, Expense Type (T), Supplier (T), Transaction Number, AP Amount

## g0028（1 列）
- 見出し：Supplier (T)
- 例1 値：SH 24 CIC | BOXXE LTD | SUPPLY CHAIN COORDINATION LIMITED - FEE… | COMMUNITY HEALTH PARTNERSHIPS LTD | COMMUNITY HEALTH PARTNERSHIPS LTD
  - 同じ表の列：Department Family, Entity (T), Date, Expense Type (T), Expense Area (T), Transaction Number, AP Amount

## g0029（9 列）
- 見出し：Transaction Number
- 例1 値：500046227 | 500043935 | 500044720 | 500043751 | 500044756
  - 同じ表の列：Department Family, Entity (T), Date, Expense Type (T), Expense Area (T), Supplier (T), AP Amount
- 例2 値：40007010 | 40220109 | 40120829 | 40082570 | 40191663
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, AP Amount, Purchase Invoice Nu…

## g0030（2 列）
- 見出し：AP Amount
- 例1 値：51,353.90 | 48,600.00 | 85,757.03 | 9,720.00 | 39,896.95
  - 同じ表の列：Department Family, Entity (T), Date, Expense Type (T), Expense Area (T), Supplier (T), Transaction Number
- 例2 値：205,278.65 | 32,886.00 | 179,231.29 | 80,491.00 | 28,831.20
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Purchase Invoice Nu…

## g0031（1 列）
- 見出し：Entity
- 例1 値：Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH… | Derbyshire Community Health Services NH…
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0032（1 列）
- 見出し：Expense Type
- 例1 値：Lease Rents | NonNHS Trade Pybls Curr | Service Charge | Phone Instal & Maint | NonNHS Trade Pybls Curr
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0033（1 列）
- 見出し：Expense Area
- 例1 値：Balance Sheet | SEXUAL HEALTH SERVICE DERBYSHIRE COUNTY | SITE SERVICES SWADLINCOTE | Balance Sheet | POE SENIOR MANAGEMENT TEAM (NON JV)
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0034（1 列）
- 見出し：Supplier
- 例1 値：SUPPLY CHAIN COORDINATION LIMITED | VODAFONE LTD | UNIVERSITY HOSPITALS OF DERBY & BURTON … | PRIMARY HEALTH INVESTMENT PROPERTIES LTD | UNIVERSITY HOSPITALS OF DERBY & BURTON …
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0035（1 列）
- 見出し：AP Amount
- 例1 値：8216.6 | 9916.4 | 25021.62 | 40191.89 | 29631.13
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Purchase Invoice Nu…

## g0036（1 列）
- 見出し：Purchase Invoice Number
- 例1 値：60219238 | 99362601 | 9385 | 75A | 800027704
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount

## g0037（1 列）
- 見出し：Transactions over £25,000 Report to Treasury
- 例1 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Payment Date from:, 01/09/2025, To:, 30/09/2025

## g0038（1 列）
- 見出し：Payment Date from:
- 例1 値：Dudley Group NHS FT | Dudley Group NHS FT | Dudley Group NHS FT | Dudley Group NHS FT | Dudley Group NHS FT
  - 同じ表の列：Transactions over £…, 01/09/2025, To:, 30/09/2025

## g0039（1 列）
- 見出し：01/09/2025
- 例1 値：10/09/2025 | 23/09/2025 | 23/09/2025 | 09/09/2025 | 23/09/2025
  - 同じ表の列：Transactions over £…, Payment Date from:, To:, 30/09/2025

## g0040（1 列）
- 見出し：To:
- 例1 値：Service Charge | Services Provided | Capital | Drugs | Services Provided
  - 同じ表の列：Transactions over £…, Payment Date from:, 01/09/2025, 30/09/2025

## g0041（1 列）
- 見出し：30/09/2025
- 例1 値：Estates & Facilities | Renal CAPD Unit | Trust Wide | Dudley Adult Bladder/Bowel Ser | Pathology Administration
  - 同じ表の列：Transactions over £…, Payment Date from:, 01/09/2025, To:

## g0042（7 列）
- 見出し：Entity
- 例1 値：East Sussex Healthcare NHS Trust | East Sussex Healthcare NHS Trust | East Sussex Healthcare NHS Trust | East Sussex Healthcare NHS Trust | East Sussex Healthcare NHS Trust
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Amount
- 例2 値：Isle Of Wight NHS Trust | Isle Of Wight NHS Trust | Isle Of Wight NHS Trust | Isle Of Wight NHS Trust | Isle Of Wight NHS Trust
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount

## g0043（1 列）
- 見出し：Expense Type
- 例1 値：FUEL | CAPITAL EXPENDITURE | CONSULTANCY FEES | ENGINEERING MATERIALS | GAS (FIRM)
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Amount

## g0044（3 列）
- 見出し：Expense Area
- 例1 値：Urgent Care | Commercial | Pharmacy Stock | Integrated Care | Integrated Care
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Amount
- 例2 値：CAPITAL EXPENDITURE | CHIEF EXECUTIVE | PATHOLOGY | OPHTHALMOLOGY DEPARTMENT | SURGERY DEPARTMENT
  - 同じ表の列：Department Family, Entity, Cleared Date, Expense Type, Reference, Line Value, Vat Reg No

## g0045（1 列）
- 見出し：Supplier
- 例1 値：CELGENE LTD | JOHNSON & JOHNSON MEDICAL LTD | NHS BLOOD AND TRANSPLANT (NHSBT) | PD HARRIS LTD (ALAN HARRIS) | NHS BLOOD AND TRANSPLANT (NHSBT)
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Amount

## g0046（1 列）
- 見出し：Entity
- 例1 値：Epsom & ST Helier University Hospital | Epsom & ST Helier University Hospital | Epsom & ST Helier University Hospital | Epsom & ST Helier University Hospital | Epsom & ST Helier University Hospital
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0047（4 列）
- 見出し：Expense Type
- 例1 値：Drugs | Lease Rents | Drugs | Electricity | Contractual Clinical Srv
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…
- 例2 値：COMPUTER HARDWARE PURCHASES | POSTAGE | DRUGS DGH | COMPUTER HARDWARE PURCHASES | COMPUTER CONSUMABLES
  - 同じ表の列：Department Family, Entity, Cleared Date, Expense Area, Reference, Line Value, Vat Reg No

## g0048（1 列）
- 見出し：Expense Area
- 例1 値：S UNIT CRAWLEY (STH) | ENERGY (STH) | ENERGY (STH) | NMET | HISTOPATHOLOGY (EPS)
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0049（1 列）
- 見出し：Supplier
- 例1 値：MITIE CLEANING & ENVIRONMENTAL SERVICES… | NOVARTIS PHARMACEUTICALS UK LTD | FRESENIUS MEDICAL CARE RENAL SERVICES L… | ABBOTT LABORATORIES LTD | FRESENIUS MEDICAL CARE RENAL SERVICES L…
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, AP Amount, Purchase Invoice Nu…

## g0050（1 列）
- 見出し：Purchase Invoice Number
- 例1 値：6.50649E+12 | 5278003978 | 8940054468 | 30578914Q | DC0067
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, AP Amount

## g0051（2 列）
- 見出し：Expense Type
- 例1 値：CNST contributions | Equip Maint Contracts | IT Additions | Blood Products | Stocks Raw Materials
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, AP Amount
- 例2 値：SYS Inventory | SYS Inventory | Other Patients Welfare | SYS Inventory | SYS Inventory
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, AP Amount, VAT Registration Nu…

## g0052（2 列）
- 見出し：Expense Area
- 例1 値：Balance Sheet | Balance Sheet | Balance Sheet | Urgent Care Services | PARIS
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, AP Amount
- 例2 値：NON EMERGENCY SERVICES | CLINICAL SERVICES | OPERATIONS | NON EMERGENCY SERVICES | NON EMERGENCY SERVICES
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE TYPE, SUPPLIER, TRANSACTION NUMBER, AMOUNT

## g0053（1 列）
- 見出し：Supplier
- 例1 値：MARITIME & COASTGUARD AGENCY | TRUSTMARQUE SOLUTIONS LTD | BERENDSEN UK LTD | NHS BLOOD & TRANSPLANT | INLAND REVENUE CIS
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, AP Amount

## g0054（2 列）
- 見出し：AP Amount
- 例1 値：34080 | 51066.6 | 44764 | 35358.35 | 25312.56
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number
- 例2 値：4918.8 | 2500 | 1154.4 | 63.48 | 99.24
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, VAT Registration Nu…

## g0055（2 列）
- 見出し：Entity
- 例1 値：Leicestershire Partnership NHS Trust | Leicestershire Partnership NHS Trust | Leicestershire Partnership NHS Trust | Leicestershire Partnership NHS Trust | Leicestershire Partnership NHS Trust
  - 同じ表の列：Department family, Date, Expense type, Expense area, Supplier, Amount
- 例2 値：NHS Business Services Authority | NHS Business Services Authority | NHS Business Services Authority | NHS Business Services Authority | NHS Business Services Authority
  - 同じ表の列：Department family, Date, Expense type, Expense area, Supplier, Amount

## g0056（1 列）
- 見出し：Expense type
- 例1 値：NURSE - BAND 2 - AGENCY | Water & Sewerage Charges | Healthcare Services / Recharges from No… | NURSE - BAND 2 - AGENCY | Water & Sewerage Charges
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Amount

## g0057（1 列）
- 見出し：Expense area
- 例1 値：Welford Ward | Chief Executives Office | Mill Lodge | Swithland House - London Road 352 (P44,… | City ICS
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Amount

## g0058（1 列）
- 見出し：Supplier
- 例1 値：HCL NURSING | HCL NURSING | SOFT TOUCH ARTS LTD | HCL NURSING | SUPPLY CHAIN CO LTD
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Amount

## g0059（3 列）
- 見出し：GEOGRAPHY_CODE
- 例1 値：E10000019 | E07000136 | E10000019 | E07000138 | E07000137
  - 同じ表の列：OBS_VALUE
- 例2 値：E01026030 | E01026015 | E01034680 | E01026007 | E01026021
  - 同じ表の列：GEOGRAPHY_TYPE, OBS_VALUE

## g0060（1 列）
- 見出し：OBS_VALUE
- 例1 値：409 | 542 | 734 | 251 | 4424
  - 同じ表の列：GEOGRAPHY_CODE

## g0061（1 列）
- 見出し：GEOGRAPHY_TYPE
- 例1 値：2021 super output areas - lower layer | 2021 super output areas - lower layer | 2021 super output areas - lower layer | 2021 super output areas - lower layer | 2021 super output areas - lower layer
  - 同じ表の列：GEOGRAPHY_CODE, OBS_VALUE

## g0062（1 列）
- 見出し：OBS_VALUE
- 例1 値：0.2 | 0.0 | 0 | 0 | 5
  - 同じ表の列：GEOGRAPHY_CODE, GEOGRAPHY_TYPE

## g0063（1 列）
- 見出し：Department Family
- 例1 値：DOH | DOH | DOH | DOH | DOH
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0064（1 列）
- 見出し：Expense Type
- 例1 値：BT Phone Bills | CAC Tools Maintenance | Gas | Electricity | Gas
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Amount

## g0065（3 列）
- 見出し：Expense Area
- 例1 値：Hanwell Estates | Fleet Support Services | Deputy Director of Operations | Kenton Estates | Edmonton Estates
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Amount
- 例2 値：Prescription Pricing Division | Corporate Services | Corporate Services | Supply Chain Management Division | Corporate Services
  - 同じ表の列：Department family, Entity, Date, Expense type, Supplier, Amount

## g0066（1 列）
- 見出し：Supplier
- 例1 値：BRITISH GAS | LONDON ELECTRICITY | BRITISH GAS | LONDON ELECTRICITY | BRITISH GAS
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Amount

## g0067（1 列）
- 見出し：Amount
- 例1 値：197.71 | 27767.53 | 25496.30 | 1,960.35 | 30039.51
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier

## g0068（1 列）
- 見出し：Cleared Date
- 例1 値：27/04/2020 | 27/04/2020 | 20/04/2020 | 20/04/2020 | 27/04/2020
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Reference, Line Value, Vat Reg No

## g0069（1 列）
- 見出し：Reference
- 例1 値：1116317 | 1112418 | 1115692 | 1109353 | 1059185
  - 同じ表の列：Department Family, Entity, Cleared Date, Expense Type, Expense Area, Line Value, Vat Reg No

## g0070（1 列）
- 見出し：Line Value
- 例1 値：51150 | 48396 | 12154.02 | 20190.34 | 28684.8
  - 同じ表の列：Department Family, Entity, Cleared Date, Expense Type, Expense Area, Reference, Vat Reg No

## g0071（1 列）
- 見出し：Vat Reg No
- 例1 値：Omitted | Omitted | Omitted | Omitted | Omitted
  - 同じ表の列：Department Family, Entity, Cleared Date, Expense Type, Expense Area, Reference, Line Value

## g0072（1 列）
- 見出し：Expense Type
- 例1 値：Equipment | Eq Disp - Glass/Plast | Msse Equip'T (<#5k) | Serv Recvd - Saxon | Works
  - 同じ表の列：Department family, Entity, Date, Expense Area, Supplier, Transaction number, Amount

## g0073（1 列）
- 見出し：Expense Area
- 例1 値：Endoscopy | Endoscopy | Endoscopy | Endoscopy | M.R.I. Unit
  - 同じ表の列：Department family, Entity, Date, Expense Type, Supplier, Transaction number, Amount

## g0074（1 列）
- 見出し：Supplier
- 例1 値：Inhealth Ltd | Ge Capital Funding Services Ltd | Ir-P362pp00007781 | Nhs Litigation Authority | Total Gas & Power
  - 同じ表の列：Department family, Entity, Date, Expense Type, Expense Area, Transaction number, Amount

## g0075（1 列）
- 見出し：Transaction number
- 例1 値：PL2-638220 | PL2-643691 | PL2-640766 | PL2-638526 | PL2-644317
  - 同じ表の列：Department family, Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0076（3 列）
- 見出し：Amount
- 例1 値：4752 | 3040 | 4680.87 | 2869 | 968449.03
  - 同じ表の列：Department family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction number
- 例2 値：680.63 | 53115.5 | 25865.05 | 380095 | 24843.11
  - 同じ表の列：DEPARTMENT FAMILY, ENTITY, DATE, EXPENSE TYPE, EXPENSE AREA, SUPPLIER, TRANSACTION NUMBER

## g0077（1 列）
- 見出し：Oct-10
- 例1 値：1747 | 38 | 20 | 579 | 39
  - 同じ表の列：Nov-10, Dec-10, Jan-11, Feb-11, Mar-11

## g0078（1 列）
- 見出し：Nov-10
- 例1 値：796 | 61 | 36 | 92 | 1630
  - 同じ表の列：Oct-10, Dec-10, Jan-11, Feb-11, Mar-11

## g0079（1 列）
- 見出し：Dec-10
- 例1 値：403 | 1150 | 134 | 42 | 17
  - 同じ表の列：Oct-10, Nov-10, Jan-11, Feb-11, Mar-11

## g0080（1 列）
- 見出し：Jan-11
- 例1 値：1551 | 642 | 45 | 52 | 247
  - 同じ表の列：Oct-10, Nov-10, Dec-10, Feb-11, Mar-11

## g0081（1 列）
- 見出し：Feb-11
- 例1 値：230 | 607 | 47 | 12 | 450
  - 同じ表の列：Oct-10, Nov-10, Dec-10, Jan-11, Mar-11

## g0082（1 列）
- 見出し：Mar-11
- 例1 値：908 | 1880 | 9 | 296 | 465
  - 同じ表の列：Oct-10, Nov-10, Dec-10, Jan-11, Feb-11

## g0083（1 列）
- 見出し：Q1:In general do you believe that at the moment things in Ir
- 例1 値：0 | Count | Count | % within D12 City | 14
  - 同じ表の列：Total

## g0084（1 列）
- 見出し：Total
- 例1 値：100 | 3 | 0 | 100 | 2
  - 同じ表の列：Q1:In general do yo…

## g0085（1 列）
- 見出し：Expense type
- 例1 値：Minor Works | Temporary Staff | Query | Bank Charges | Rates Charges
  - 同じ表の列：Department family, Entity, Date, Expense area, Supplier, Amount

## g0086（1 列）
- 見出し：Supplier
- 例1 値：CLAYBROOK COMPUTING LTD | CAPITA BUSINESS SERVICES LTD | CAPITA BUSINESS SERVICES LTD | FLEXIFORM | ROYAL MAIL
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Amount

## g0087（2 列）
- 見出し：Amount
- 例1 値：29,969.90 | 39,370.72 | 53,640.98 | 1,644,113.37 | 24,147.20
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier
- 例2 値：37,968.00 | 1,191,844.17 | 127,145.79 | 227,110.00 | 214,276.80
  - 同じ表の列：Department Of Health, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Month

## g0088（1 列）
- 見出し：<script>(function(w,d,s,l,i){w[l]=w[l]||[]
- 例1 値：<span class="share--link-span share--li… | </li> | </li> | optionalCookies: [ | <div id="block-pagetitle" class="conten…
  - 同じ表の列：w[l].push({'gtm.sta…

## g0089（1 列）
- 見出し：w[l].push({'gtm.start':
- 例1 値：f.parentNode.insertBefore(j,f) | j.async=true | visibility:hidden"></iframe></noscript> | if(b){var d=b.createElement('script') | i < ca.length
  - 同じ表の列：<script>(function(w…

## g0090（1 列）
- 見出し：Audit Year
- 例1 値：2015-18 | 2015-18 | 2015-18 | 2015-18 | 2015-18
  - 同じ表の列：Organisation Type, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0091（1 列）
- 見出し：Organisation Type
- 例1 値：Service | Service | CCG | Service | CCG
  - 同じ表の列：Audit Year, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0092（1 列）
- 見出し：Organisation Code
- 例1 値：RVV | RK9 | RXK | RNQ51A | 01J
  - 同じ表の列：Audit Year, Organisation Type, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0093（1 列）
- 見出し：Parent Code
- 例1 値：RXF | E20 | RH8 | RBD | E26
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0094（1 列）
- 見出し：Nationality
- 例1 値：England | England | England | England | England
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0095（1 列）
- 見出し：NDFA cases (n)
- 例1 値：40 | 140 | 1045 | 495 | 75
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, Nationality, NDFA patients (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0096（1 列）
- 見出し：NDFA patients (n)
- 例1 値：260 | 465 | 55 | 150 | 190
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA cases 2015-16 …, NDFA patients 2015-…

## g0097（1 列）
- 見出し：NDFA cases 2015-16 (n)
- 例1 値：5 | 0 | 0 | 65 | 80
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA patients 2015-…

## g0098（1 列）
- 見出し：NDFA patients 2015-16 (n)
- 例1 値：45 | 85 | 25 | 5 | 0
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …

## g0099（1 列）
- 見出し：NDFA cases 2016-17 (n)
- 例1 値：180 | 10 | 10 | 55 | 75
  - 同じ表の列：Audit Year, Organisation Type, Organisation Code, Parent Code, Nationality, NDFA cases (n), NDFA patients (n), NDFA cases 2015-16 …

## g0100（1 列）
- 見出し：Section
- 例1 値：Reference Tables | National Standard | National Standard | National Standard Summary | National Standard
  - 同じ表の列：Output_Reference, Period, WhenOccurred, Organisation_Code, Identifier, DataType, Value, Standard_Target

## g0101（1 列）
- 見出し：Output_Reference
- 例1 値：Table R 1 | Table NSS 2 | Table NS 5 | Table NS 14 | Table NS 13
  - 同じ表の列：Section, Period, WhenOccurred, Organisation_Code, Identifier, DataType, Value, Standard_Target

## g0102（1 列）
- 見出し：Period
- 例1 値：2020-21 | 2019-20 | 2019-20 | 2021-22 | 2021-22
  - 同じ表の列：Section, Output_Reference, WhenOccurred, Organisation_Code, Identifier, DataType, Value, Standard_Target

## g0103（1 列）
- 見出し：WhenOccurred
- 例1 値：Audit Year | Audit Year | Audit Year offset -30 days | Audit Year | Audit Year
  - 同じ表の列：Section, Output_Reference, Period, Organisation_Code, Identifier, DataType, Value, Standard_Target

## g0104（1 列）
- 見出し：Organisation_Code
- 例1 値：RP4 | Total | RAL | RAL | RGM
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Identifier, DataType, Value, Standard_Target

## g0105（1 列）
- 見出し：Identifier
- 例1 値：% having WHO functional class/exercise … | % having QoL recorded | % having catheterisation | Standard 8 | % first line usage of PDE5
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Organisation_Code, DataType, Value, Standard_Target

## g0106（1 列）
- 見出し：DataType
- 例1 値：% | % | % | % | %
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Organisation_Code, Identifier, Value, Standard_Target

## g0107（1 列）
- 見出し：Value
- 例1 値：75 | 100 | 97 | 8 | 71
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Organisation_Code, Identifier, DataType, Standard_Target

## g0108（1 列）
- 見出し：Standard_Target
- 例1 値：Yes | 50 | 95 | 95 | 90
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Organisation_Code, Identifier, DataType, Value

## g0109（1 列）
- 見出し：Standard_Met
- 例1 値：N/A | Yes | Yes | Yes | Yes
  - 同じ表の列：Section, Output_Reference, Period, WhenOccurred, Organisation_Code, Identifier, DataType, Value

## g0110（1 列）
- 見出し：Accounting Date
- 例1 値：27/04/2026 | 27/04/2026 | 27/04/2026 | 27/04/2026 | 27/04/2026
  - 同じ表の列：Department Family, Expense Type, Expense Area, Supplier, Transaction Number, Invoice Distributio…

## g0111（1 列）
- 見出し：Expense Type
- 例1 値：GMS; LES Ethnicity | PCN; DES New To General Practice Nurse | NCD; Trainee Nursing Associate | GMS; LES Anti-Coagulation | GMS; LES Diabetes-Insulin (GTT)
  - 同じ表の列：Department Family, Accounting Date, Expense Area, Supplier, Transaction Number, Invoice Distributio…

## g0112（1 列）
- 見出し：Expense Area
- 例1 値：T6Y - Acute - Contract - Independent | T6Y - PCSE Interface; Delegated GP | T6Y - PCSE Interface; Central Drugs | T6Y - PCSE Interface; Delegated GP | T6Y - ADHD RtC - CYP
  - 同じ表の列：Department Family, Accounting Date, Expense Type, Supplier, Transaction Number, Invoice Distributio…

## g0113（1 列）
- 見出し：Supplier
- 例1 値：CENTRAL NORWICH PCN | BDO LLP | COUNTY CARE HOMES LTD | CASTLE PARTNERSHIP (D82011) | BUNGAY MEDICAL PRACTICE (D83034)
  - 同じ表の列：Department Family, Accounting Date, Expense Type, Expense Area, Transaction Number, Invoice Distributio…

## g0114（1 列）
- 見出し：Invoice Distribution Amount
- 例1 値：57,840.29 | -65.59 | 4,797.20 | 140,828.15 | -11,103.55
  - 同じ表の列：Department Family, Accounting Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0115（1 列）
- 見出し：DATE
- 例1 値：2002 | 2002 | 2002 | 2002 | 2003
  - 同じ表の列：DATE_CODE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

## g0116（1 列）
- 見出し：DATE_CODE
- 例1 値：2002 | 2002 | 2002 | 2002 | 2002
  - 同じ表の列：DATE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

## g0117（1 列）
- 見出し：DATE_TYPE
- 例1 値：date | date | date | date | date
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

## g0118（1 列）
- 見出し：DATE_TYPECODE
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_SORTORDER, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

## g0119（1 列）
- 見出し：DATE_SORTORDER
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_TYPECODE, GEOGRAPHY, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

## g0120（1 列）
- 見出し：GEOGRAPHY
- 例1 値：1946157117 | 1946157113 | 1946157113 | 1946157115 | 1946157118
  - 同じ表の列：DATE, DATE_CODE, DATE_TYPE, DATE_TYPECODE, DATE_SORTORDER, GEOGRAPHY_CODE, GEOGRAPHY_TYPE, GEOGRAPHY_TYPECODE

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
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
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
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
