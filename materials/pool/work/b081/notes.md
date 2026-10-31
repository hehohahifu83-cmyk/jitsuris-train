# b081 notes

- LABEL_GUIDE v2.3 independent labeling; no model predictions were read.
- Person-level record exclusions (all columns in each table set to S):
  - co-spads-hospitality-oct2010_1.csv: special adviser hospitality entries (groups g0001–g0003).
  - Board_expenses_and_hospitality_Oct_-_dec_2011.csv: board hospitality/expense entries (g0004–g0009).
  - ministerial_quarterly_returns_july_to_september_2011.csv: ministerial gifts and recipient entries (g0010–g0013).
  - DExEU-senior-officials-travel-july-september-2016.csv: individual official travel records (g0014–g0021).
  - april-june2013.csv: individual travel records (g0022–g0027).
  - HMRC_senior_officials_outside_employment_April_2022_to_March_2023.csv: named senior official outside-employment records (g0080–g0081).
  - senior_staff_meetings_with_external_orgs_3rdqrt.csv: named senior official meeting records (g0111–g0113).
- Structural exclusions (all columns set to S because project names are columns while the rows mix dates, narrative, status, department, and financial values):
  - gmpp-data-DWP-q2-2012-13-csv.csv (g0050–g0059).
  - gmpp-data-HMRC-q2-2012-13.csv (g0082–g0090).
  - HO_Major_projects.csv (g0095–g0104).
- No other table-level personal-record exclusions.
