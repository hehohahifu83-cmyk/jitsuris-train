# Model-derived training material candidates for Jitsuris

Updated: 2026-10-27

This is a source and rights inventory, not a finalized training batch. Do not copy rows into `materials/pool/batch_*.jsonl` until the existing pipeline has deduplicated, mapped labels to `LABEL_GUIDE.md`, and completed independent review. Keep benchmark test splits out of training.

## Current repository baseline

The earlier “80万超” figure was a rough sum of corpus-level counts (GitTables, SOTAB V2, VizNet), not a downloaded or consolidated Jitsuris dataset. The latest repository status available during research reports 27,070 confirmed training columns. Corpus counts overlap and cannot be summed as unique examples without deduplication.

## Candidate sources

| Source / model family | What is available | Jitsuris value | Rights / access status | Handling |
|---|---|---|---|---|
| **GitTables 1M (licensed release)** | Official Zenodo v0.0.6: 1 million tables, about 16.3 GB; 723k+ have at least one DBpedia annotation and 738k+ have a Schema.org annotation. Each table includes column semantic annotations and repository-license metadata. | Highest-priority large candidate. The release is explicitly limited to tables whose repository licenses allow distribution. Its labels were assigned using name matching and FastText semantic similarity, so treat them as weak labels and remap to Jitsuris classes. | GitTables site states CC BY 4.0 and says all Zenodo v0.0.6 tables have distribution-permitting source licenses. The Zenodo API record-level field reports `cc-zero`, while its HTML Rights section has no visible value; preserve per-table source/license metadata and resolve this discrepancy before bulk redistribution. The 1.7M v0.0.4 corpus is different and may include tables without permissive licenses: do not use it. | Priority candidate from the **1M v0.0.6 release only**. The 96-file metadata inventory is saved at `gittables_1m_v0.0.6_inventory_20261027.json`. The first 20-column b046 pilot was placed on rights hold before labeling. Its data and label sheets were removed after review; the staging importer now requires an exact source-URL entry in `rights_approved_sources.json`. The GitTables archive is fetched transiently and never committed. |
| **GitTables benchmark — column type detection** | Official Zenodo benchmark: 1,101 GitTables tables, Schema.org and DBpedia target/ground-truth files, 3.6 MB total; the source page identifies it as a SemTab 2021 CTA benchmark. | Good for studying ontology-to-Jitsuris mapping and evaluation design. | Zenodo record 5706316 has no visible Rights/License value; it is benchmark material and overlaps the broader GitTables family. | Reference only; do not import any benchmark split into training. Keep its test portions sealed and do not mirror until rights are clear. |
| **RWT-RuTaBERT / LoReTA** | LoReTA repo has a pinned MIT-licensed artifact with 1,441,349 columns (1,325,901 train; 115,448 test). The LoReTA data export omits original headers and retains its header-derived weak label. | High-volume candidate once rights clear; reconstruct original headers and values from the RWT source. Discard the source label for independent annotation. | LoReTA MIT layer is verified at a pinned commit. RWT comes from Russian Wikipedia; the upstream RWT repo has no separate dataset LICENSE. Page IDs/table offsets are now verified from LoReTA source code, but per-page license/version/notices and rights for the RWT corpus/selection remain unresolved. | Keep all rows on rights hold. Run metadata-only page-link audit; do not stage any content. If cleared, use train only, preserve per-page attribution and license evidence, and keep test sealed. |
| SOTAB V2 (used by table annotation models including DODUO/ZTab) | Public CTA/CPA train, validation and test splits with JSON tables and ground-truth labels; Zenodo SemTab 2023 package is 4.0 GB. | Strong candidate: column type annotations and realistic web tables. Map Schema.org/DBpedia labels to Jitsuris classes; retain only reviewed mappings. | Official pages expose downloads, but do not make clear the reuse license for the underlying tables. Public download alone is not permission to redistribute. | Candidate only; do not mirror raw archive. Obtain owner/license confirmation before storing source tables. |
| VizNet / Sato | Four corpora (Plotly, ManyEyes, WebTables, Open Data Portal); Sato supplies an annotation/model pipeline and common semantic types. | Potentially broad table examples; labels may be derived from headers or linked entity types, so noisy for Jitsuris. | VizNet README estimates ~657 GB uncompressed. Underlying data comes from multiple sources and rights vary; the Sato script uses legacy HTTP download URLs. | Do not bulk download or redistribute. Prefer legally clear, source-specific subsets after a rights and quality audit. |
| DODUO | Official code and model; its download script points to data and model archives (data archive observed at about 102 MiB). | Useful reference for contextual column-labeling and label hierarchy. | DODUO README says the datasets themselves may not be redistributed by the project; archive bundles third-party data. | Do not mirror the archive. Use the paper/code for method study and fetch source datasets from their original owners under their terms. |
| ZTab (ICDE 2026) | Code and a Google Drive package described as train/validation/test splits, type mappings, prototypes and JSONL fine-tuning data; uses T2D, SOTAB and WikiTable sources. | Useful for domain-aware annotation, prototypes and synthetic/pseudo-labeled training examples. | The code/data package license was not established in the sources reviewed. Pseudo-labels are not gold annotations. | Keep as a pending source. If cleared, store separately as pseudo-labeled; sample-audit and remap before training. |
| TabEmb (ACL 2026) | Code and some T2D setup/sample material; paper uses T2D, WikiTable, WebTables and SOTAB variants; precomputed embeddings are listed separately. | Useful for context/embedding features and comparison; embeddings are not raw labeled examples. | Repository/dataset licensing metadata was incomplete in the reviewed README. | Do not ingest embeddings as labels or distribute until each artifact's terms are verified. |
| TURL / WikiTables | TURL code and derived dataset references; linked original download was unavailable in the current README notice (access revoked while a backup is sought). | Table context and entity/type signals can complement Jitsuris labels. | Currently inaccessible through the official source; original source rights also need review. | Track only; do not use unofficial mirrors as a substitute. |
| ArcheType | Research method for prompting/context sampling/label remapping; not a standalone, new gold-label corpus. | Possible annotation workflow inspiration; does not add independent training rows by itself. | No separate corpus identified. | Use as method reference only. |

## Rights gate for labeling

- `stage_gittables_sample.py` now admits only exact source URLs listed as `cleared_for_label_staging` in `rights_approved_sources.json`. A repository-level SPDX label by itself is insufficient.
- The approved register currently contains one exact file: StraboSpot's controlled-vocabulary CSV at a pinned commit. Its MIT license file, copyright notice and source-file blob were verified and are copied into the b047 staging batch (1 table, 3 columns, 3 blank answer rows).
- GitTables' project page says CC BY 4.0; its Zenodo API metadata also reports CC0. Staged GitTables-derived material keeps the stricter CC BY attribution plus the original per-table license notice.
- This is clearance for independent label staging only. It is not final approval for training-pool inclusion, public redistribution or model release.
- RWT-RuTaBERT/LoReTA remains on rights hold. Its MIT license and page-ID mapping are now pinned/verified, but the upstream RWT corpus license and per-page revision/exception audit are still unresolved. The metadata-only preflight tool records reconstructed page links without exporting column text or weak labels.

## Label conversion rules for any future import

1. Preserve the source's original label and source table/column identifier in a staging file.
2. Map to Jitsuris classes only where the meaning is equivalent under `LABEL_GUIDE.md`; otherwise leave unmapped/unknown.
3. Do not infer a Jitsuris label from a column header alone when values/context conflict.
4. Deduplicate by normalized table content and column values against the existing pool; record source and split provenance.
5. Keep train, validation and test provenance. Never train on benchmark test rows.
6. Mark model-generated or weak labels as pseudo-labels and require human adjudication before they enter confirmed batches.
7. Finalize confirmed examples only through `materials/pipeline.py`; do not hand-edit batch files.

## Primary source links

- GitTables 1M (licensed, Zenodo v0.0.6, 16.3 GB): https://zenodo.org/records/6517052
- GitTables site and license notes: https://gittables.github.io/
- GitTables 1.7M (avoid; possible non-permissive underlying tables): https://zenodo.org/records/4943312
- SOTAB V2 downloads: https://webdatacommons.org/structureddata/sotab/v2/
- SOTAB V2 for SemTab 2023 (Zenodo, 4.0 GB): https://zenodo.org/records/8422037
- VizNet repository: https://github.com/viznetauthors/viznet
- Sato repository: https://github.com/megagonlabs/sato
- DODUO repository: https://github.com/megagonlabs/doduo
- ZTab repository: https://github.com/hoseinzadeehsan/ZTab
- TabEmb paper: https://aclanthology.org/2026.acl-long.126/
- TURL repository: https://github.com/sunlab-osu/TURL
- ArcheType paper: https://arxiv.org/abs/2405.10555

## Acquisition decision

- GitTables 1M v0.0.6 remains a high-priority **candidate**, not confirmed training data. The official GitTables site reports 1M tables, 723K+ DBpedia-annotated tables and 738K+ Schema.org-annotated tables, and says every table in v0.0.6 has a source license that permits distribution. The Zenodo API record metadata says `cc-zero`, while the GitTables project page says CC BY 4.0 and the HTML Rights section is blank. For staged samples, apply the stricter CC BY 4.0 attribution and retain the per-table source license; bulk eligibility still requires a source-register entry for each selected source.
- RWT-RuTaBERT/LoReTA's 1,441,349 columns remain rights-held and are excluded from labeling. LoReTA is pinned to commit f12d7f83a70a065c90eb314a14e35bf177bade22 (MIT); its path mapping to Wikipedia page ID + table offset is verified. The upstream RWT corpus/data rights, exact per-page license/revision, and imported-content notices remain unresolved. See rwt_loreta_rights_review_20261027.md and rwt_rutabert_candidate_20261027.json.
- The separate 1,101-table GitTables benchmark is reference-only. Its Zenodo record shows no visible rights/license value, and its benchmark splits must not be moved into training.
- b046 is rights-held and its data/sheets have been removed. b047 is label-ready for independent labeling only: 3 groups with blank answers. No rows have been imported into the final pool or used for training. The Zenodo/API license discrepancy is handled conservatively by retaining CC BY 4.0 attribution together with the per-table source license; broader staging still requires each source to pass the exact-URL register.
