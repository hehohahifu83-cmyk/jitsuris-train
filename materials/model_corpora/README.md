# Model-derived training material candidates for Jitsuris

Updated: 2026-10-27

This is a source and rights inventory, not a finalized training batch. Do not copy rows into `materials/pool/batch_*.jsonl` until the existing pipeline has deduplicated, mapped labels to `LABEL_GUIDE.md`, and completed independent review. Keep benchmark test splits out of training.

## Current repository baseline

The earlier “80万超” figure was a rough sum of corpus-level counts (GitTables, SOTAB V2, VizNet), not a downloaded or consolidated Jitsuris dataset. The latest repository status available during research reports 27,070 confirmed training columns. Corpus counts overlap and cannot be summed as unique examples without deduplication.

## Candidate sources

| Source / model family | What is available | Jitsuris value | Rights / access status | Handling |
|---|---|---|---|---|
| **GitTables 1M (licensed release)** | Official Zenodo v0.0.6: 1 million tables, about 16.3 GB; 723k+ have at least one DBpedia annotation and 738k+ have a Schema.org annotation. Each table includes column semantic annotations and repository-license metadata. | Highest-priority large candidate. The release is explicitly limited to tables whose repository licenses allow distribution. Its labels were assigned using name matching and FastText semantic similarity, so treat them as weak labels and remap to Jitsuris classes. | GitTables site says the corpus is CC BY 4.0 and all tables in Zenodo v0.0.6 have distribution-permitting licenses; preserve attribution and per-table license/source metadata. The 1.7M v0.0.4 corpus is different and may include tables without permissive licenses: do not use it. | Safe candidate for staging from the **1M v0.0.6 release only**. Download was not completed in this pass because Zenodo downloads timed out from this environment. Do not claim this corpus is locally stored yet. |
| SOTAB V2 (used by table annotation models including DODUO/ZTab) | Public CTA/CPA train, validation and test splits with JSON tables and ground-truth labels; Zenodo SemTab 2023 package is 4.0 GB. | Strong candidate: column type annotations and realistic web tables. Map Schema.org/DBpedia labels to Jitsuris classes; retain only reviewed mappings. | Official pages expose downloads, but do not make clear the reuse license for the underlying tables. Public download alone is not permission to redistribute. | Candidate only; do not mirror raw archive. Obtain owner/license confirmation before storing source tables. |
| VizNet / Sato | Four corpora (Plotly, ManyEyes, WebTables, Open Data Portal); Sato supplies an annotation/model pipeline and common semantic types. | Potentially broad table examples; labels may be derived from headers or linked entity types, so noisy for Jitsuris. | VizNet README estimates ~657 GB uncompressed. Underlying data comes from multiple sources and rights vary; the Sato script uses legacy HTTP download URLs. | Do not bulk download or redistribute. Prefer legally clear, source-specific subsets after a rights and quality audit. |
| DODUO | Official code and model; its download script points to data and model archives (data archive observed at about 102 MiB). | Useful reference for contextual column-labeling and label hierarchy. | DODUO README says the datasets themselves may not be redistributed by the project; archive bundles third-party data. | Do not mirror the archive. Use the paper/code for method study and fetch source datasets from their original owners under their terms. |
| ZTab (ICDE 2026) | Code and a Google Drive package described as train/validation/test splits, type mappings, prototypes and JSONL fine-tuning data; uses T2D, SOTAB and WikiTable sources. | Useful for domain-aware annotation, prototypes and synthetic/pseudo-labeled training examples. | The code/data package license was not established in the sources reviewed. Pseudo-labels are not gold annotations. | Keep as a pending source. If cleared, store separately as pseudo-labeled; sample-audit and remap before training. |
| TabEmb (ACL 2026) | Code and some T2D setup/sample material; paper uses T2D, WikiTable, WebTables and SOTAB variants; precomputed embeddings are listed separately. | Useful for context/embedding features and comparison; embeddings are not raw labeled examples. | Repository/dataset licensing metadata was incomplete in the reviewed README. | Do not ingest embeddings as labels or distribute until each artifact's terms are verified. |
| TURL / WikiTables | TURL code and derived dataset references; linked original download was unavailable in the current README notice (access revoked while a backup is sought). | Table context and entity/type signals can complement Jitsuris labels. | Currently inaccessible through the official source; original source rights also need review. | Track only; do not use unofficial mirrors as a substitute. |
| ArcheType | Research method for prompting/context sampling/label remapping; not a standalone, new gold-label corpus. | Possible annotation workflow inspiration; does not add independent training rows by itself. | No separate corpus identified. | Use as method reference only. |

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

GitTables 1M v0.0.6 is the first suitable bulk corpus to stage, subject to preserving its CC BY attribution and per-table source/license metadata. Its official Zenodo record identifies 1 million tables and the Schema.org/DBpedia label counts; the official site documents the label-generation methods and distinguishes this licensed release from earlier variants. We have not downloaded the archive: a direct transfer timed out in this environment. Therefore, no new source rows have yet been added to the local candidate store or confirmed training pool. Next, acquire this release from the official Zenodo page in an environment with working access, retain only train-eligible splits, map weak labels to Jitsuris, deduplicate, and use the established review/finalize pipeline.
