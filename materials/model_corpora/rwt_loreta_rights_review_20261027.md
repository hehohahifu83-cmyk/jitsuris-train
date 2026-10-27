# RWT-RuTaBERT / LoReTA rights and label-preparation review

Updated: 2026-10-27 19:53 JST
Status: RIGHTS HOLD. Metadata-only source indexing is permitted by this work plan; no table text or values are staged.

## Confirmed artifact and split

- LoReTA repository at pinned commit f12d7f83a70a065c90eb314a14e35bf177bade22 contains the train/test CSV artifacts and a MIT LICENSE (Copyright (c) 2025 YRL-AIDA). Preserve this notice for the LoReTA artifact layer.
- The dataset has 1,441,349 columns: train 1,325,901 and test 115,448. The 21 train CSV shards total 575,626,171 bytes. The separate test CSV is pinned and marked sealed.
- The LoReTA repository describes the dataset as derived from Russian Web Tables, itself extracted from Russian Wikipedia. The RWT repository listing has no separate dataset LICENSE file. A public download and the paper's open-source description do not establish a specific RWT database/selection license.

## Provenance mapping

The page mapping is now verified in the pinned LoReTA code. Its header collector enumerates RWT metadata files under Dataset/data/<page_id>/table_<offset>_meta.json and emits the path without the metadata suffix. Its data collector reads the matching table CSV. The published table_id form dataset/Dataset/data/1000006/table_0 therefore identifies Wikipedia page ID 1000006 and within-page table offset 0.

RWT's paper says it stores a table URL, page title, table title, and surrounding context, and that its surrogate ID consists of page ID plus table offset. The paper reports a 2021-09-13 Wikipedia snapshot. The LoReTA ID mapping allows us to reconstruct a page link as https://ru.wikipedia.org/?curid=<page_id>; it does not identify the exact historical revision by itself.

## Labels and missing headers

The LoReTA labeling notebook explains that it assumes the first noun in the original column header indicates the column's semantic type. It assigns the nearest semantic type using a Russian word-vector similarity calculation, then applies a 0.78 threshold when producing the final subset. These are weak, header-derived labels, not independently verified gold labels.

The flattened CTA export contains table_id, column_id, label_id, label, and column_data. It omits the original header. LoReTA's header-collection code recovers that name from each RWT table metadata file at columns[column_id].name. Independent labeling must reconstruct the original header and column values from the RWT source and hide/discard label and label_id so the target cannot leak.

## Rights status and remaining blockers

The MIT notice on LoReTA is relevant to LoReTA's repository artifact, but it does not override rights in the underlying Wikipedia content or prove the rights to the upstream RWT corpus/selection. RWT's paper and source repository do not state an exact data license for the corpus itself.

The RWT snapshot date predates Wikimedia's 2023 change to the default license for new text contributions. Do not assign one license to every page based only on that date. Wikimedia's current Terms of Use accept a hyperlink/URL to each reused page as attribution, require applicable license and modification notices, and require preserving additional attribution instructions when content was imported from elsewhere. Each source page/history/discussion and any additional notices must be checked.

Until these questions are resolved, the complete 1,441,349 rows stay out of label staging, the training pool, training, and release. The 115,448-column test split remains sealed.

## Efficient next steps after the hold

1. Obtain a clear license/provenance statement for the RWT corpus/selection, or restrict the source set to a rights-cleared subset.
2. Pin the RWT archive/snapshot and derive a page-level index for the 1,325,901 train columns. The metadata-only preflight script verifies the pinned LoReTA train shards and emits source page links and IDs, but never writes cell values or weak labels.
3. Review each unique source page's applicable historical license and imported-content notices; mark unclear pages held and exclude them.
4. Once the source subset is cleared, join original headers from RWT metadata with source values, discard the LoReTA weak target, run privacy and duplicate checks, and create bounded blank-answer batches with page-level source attribution and license notices.
5. Keep approved data, source attribution, and human answers separate from the sealed test split and route any accepted labels through the existing pipeline.

## Primary sources

- LoReTA repository: https://github.com/YRL-AIDA/LoReTA/tree/f12d7f83a70a065c90eb314a14e35bf177bade22
- LoReTA MIT license: https://github.com/YRL-AIDA/LoReTA/blob/f12d7f83a70a065c90eb314a35bf177bade22/LICENSE
- RWT paper: https://arxiv.org/abs/2210.06353
- RWT upstream corpus: https://gitlab.com/unidata-labs/ru-wiki-tables-dataset
- Wikimedia Terms of Use: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
- CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/
