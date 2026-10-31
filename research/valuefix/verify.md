# 直した値と元のファイルのバイトの照合（`research/valuefix/verify_bytes.py`）

- 表 43：取れた 43、取れなかった 0。
- 取れた表で、照合した文字列 228、CP1252 のバイトが元のファイルにあった 228。
- 取れた表のうち UTF-8 として読めるファイル（化けの前提に合わない）：0。

| 陣 | 表 | 取れた | 照合 | 一致 | UTF-8 | 合わない例・誤り |
|---|---|---|---:|---:|---|---|
| b065 | ds/system/uploads/attachment_data/file/1008184/Sept-2020.csv | ○ | 3 | 3 | False |  |
| b065 | /file/808459/NCPRP_dept_template_for_publication_2017_18.csv | ○ | 5 | 5 | False |  |
| b060 | nt_data/file/930114/NCPRP_18-19_template_for_publication.csv | ○ | 6 | 6 | False |  |
| b060 | .uk/media/65b8d3b24ec51d000dc9f13a/desnz-gpc-august-2023.csv | ○ | 5 | 5 | False |  |
| b060 | v.uk/media/65bb56d83e26be000de47e00/dsit-gpc-august-2023.csv | ○ | 5 | 5 | False |  |
| b060 | gov.uk/media/5259/social-housing-asset-valuation-2014-15.csv | ○ | 2 | 2 | False |  |
| b062 | ttps://data.rochdale.gov.uk/files/2013-01-spend-over-500.csv | ○ | 5 | 5 | False |  |
| b065 | 2014_Oct_Dec_Rochdale_Borough_Council_Purchase_Orders_V1.csv | ○ | 6 | 6 | False |  |
| b060 | /data.rochdale.gov.uk/files/2015_01_Contract_Register-v1.csv | ○ | 5 | 5 | False |  |
| b062 | ta.rushmoor.gov.uk/Datasets/Open/Rushmoor%20Fraud%20data.csv | ○ | 5 | 5 | False |  |
| b060 | sets/Open/Rushmoor%20Organisation%20Structure%2020232024.csv | ○ | 6 | 6 | False |  |
| b060 | ww.blaby.gov.uk/media/1409/translation-costs-august-2018.csv | ○ | 5 | 5 | False |  |
| b065 | ocial_housing_asset_value_sept_2015_published_01_10_2015.csv | ○ | 7 | 7 | False |  |
| b060 | ploads/system/uploads/attachment_data/file/11578/1920409.csv | ○ | 1 | 1 | False |  |
| b062 | system/uploads/attachment_data/file/184439/wmi_april2011.csv | ○ | 7 | 7 | False |  |
| b065 | uploads/attachment_data/file/186398/dwp-payments-april10.csv | ○ | 5 | 5 | False |  |
| b060 | m/uploads/attachment_data/file/186424/dwp-gpc-spend-0811.csv | ○ | 4 | 4 | False |  |
| b060 | le/188122/dfe_20senior_20staff_20data_20september_202010.csv | ○ | 2 | 2 | False |  |
| b065 | ent_data/file/190249/quarterly-data-summary-q1-2012-2013.csv | ○ | 6 | 6 | False |  |
| b060 | t_data/file/190925/senior-staff-posts-dataset-march-2012.csv | ○ | 5 | 5 | False |  |
| b062 | uploads/attachment_data/file/194672/dft-gpc-spend-201302.csv | ○ | 5 | 5 | False |  |
| b062 | 8323/gpc_20spend_20over_20500_20april_20to_20june_202011.csv | ○ | 5 | 5 | False |  |
| b065 | tem/uploads/attachment_data/file/203884/Baseline-2010-11.csv | ○ | 4 | 4 | False |  |
| b060 | loads/attachment_data/file/207009/april-june-2011-travel.csv | ○ | 1 | 1 | False |  |
| b060 | loads/attachment_data/file/219998/moj-aramis-data-may-10.csv | ○ | 5 | 5 | False |  |
| b060 | attachment_data/file/220038/probation-trusts-data-may-10.csv | ○ | 0 | 0 | False |  |
| b060 | ._June_2013_DfE_family_monthly_workforce_management_info.csv | ○ | 13 | 13 | False |  |
| b062 | chment_data/file/230198/DCMS_April_2013_Workforce_Return.csv | ○ | 5 | 5 | False |  |
| b060 | file/246647/DCMS-GPC-Transactions-over-500-November-2011.csv | ○ | 5 | 5 | False |  |
| b060 | file/263614/Q2_exceptions_reporting_-_Recruitment_return.csv | ○ | 3 | 3 | False |  |
| b065 | /uploads/attachment_data/file/284904/NCPRP_2013_exercise.csv | ○ | 6 | 6 | False |  |
| b062 | ds/system/uploads/attachment_data/file/285086/ncprp-2013.csv | ○ | 21 | 21 | False |  |
| b062 | is-non-consolidated-performance-related-pay-2012-to-2013.csv | ○ | 15 | 15 | False |  |
| b060 | achment_data/file/306035/gpc-500-payments-april11-mar-12.csv | ○ | 1 | 1 | False |  |
| b060 | ttachment_data/file/349841/_500_GPC_April_to_August_2011.csv | ○ | 5 | 5 | False |  |
| b060 | kforce-management-information-bis-2012-2013-october-2012.csv | ○ | 1 | 1 | False |  |
| b062 | s/system/uploads/attachment_data/file/370041/table-1-GNI.csv | ○ | 2 | 2 | False |  |
| b060 | a/file/394556/Ofsted_spending_over__25_000_November_2014.csv | ○ | 5 | 5 | False |  |
| b062 | /attachment_data/file/51038/Spend_20over_2025k_202009-10.csv | ○ | 8 | 8 | False |  |
| b060 | a/file/51086/CO-workforce-management-information-July-12.csv | ○ | 3 | 3 | False |  |
| b062 | oads/system/uploads/attachment_data/file/516303/NCPRP_15.csv | ○ | 6 | 6 | False |  |
| b062 | uploads/system/uploads/attachment_data/file/5839/1727867.csv | ○ | 1 | 1 | False |  |
| b062 | ads/attachment_data/file/685613/beis-workforce-june-2017.csv | ○ | 13 | 13 | False |  |
