# b083 notes

- LABEL_GUIDE v2.3 independent labeling; no model predictions were read.
- Adopted tables and extraction:
  - Quarterly Financial Accounts (Central Bank of Ireland): extraction failed (HTTP 404); no sheet columns to label.
  - Authorised Credit Intermediaries (Competition and Consumer Protection Commission): 5 columns labeled; all 5 are scorable.
  - HBFI Payments Q4 2021 and Home Building Finance Ireland Payments Q1 2020: 6 extracted columns, all S.
- Table-level personal-record exclusions (all extracted columns set to S):
  - HBFI Payments Q4 2021 (g0006–g0008): supplier-payment records include a named natural-person supplier among business suppliers; the extracted columns also have unsafe_ headers with a mixture of field names, amounts, and explanatory text.
  - Home Building Finance Ireland Payments Q1 2020 (g0007–g0009): same type of supplier-payment record and malformed unsafe_ headers; all extracted columns set to S.
- Structural exclusions:
  - The two HBFI payment tables have no usable column headers in the extracted representation; values mix actual field labels, payment values, supplier names, and notes. This independently supports S for all extracted columns.
- Candidate excluded before adoption by the title-based personal-record filter (per auto_log): Register of gaming licences, Revenue Commissioners (resource f9923f40-1243-405c-a158-5b0d331ade3d); no columns extracted or labeled.
