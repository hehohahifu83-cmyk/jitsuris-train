---
license: mit
library_name: transformers
base_model:
  - intfloat/multilingual-e5-small
  - intfloat/multilingual-e5-base
pipeline_tag: text-classification
tags:
  - entity-resolution
  - record-linkage
  - cross-encoder
  - xlm-roberta
  - multilingual
---

# Business-entity matching encoders

Eight fine-tuned cross-encoders for scoring whether two business records
(name + address) refer to the same organisation. All members live in this
single repository as `state_dict` files (`<tag>/model.pt`).

They are loads for Hugging Face sequence-classification heads built from
[`intfloat/multilingual-e5-small`](https://huggingface.co/intfloat/multilingual-e5-small)
or [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base)
(MIT). Pair text is `"{name} | {address or '-'}"` for each record; the two
sides are the tokenizer pair.

## Members

| Path | Backbone | Notes |
| --- | --- | --- |
| `e5_cont1300k/model.pt` | E5-small | 1.3M training pairs |
| `kA/model.pt` | E5-base | seed 7, 1.9M pairs |
| `kB/model.pt` | E5-base | seed 8, sample disjoint from kA |
| `kC/model.pt` | E5-base | seed 9, 1.9M pairs |
| `kD/model.pt` | E5-base | hard-negative continuation of kA |
| `kE/model.pt` | E5-base | hard-negative continuation of kB |
| `kF/model.pt` | E5-base | mined-error continuation of kA |
| `kG/model.pt` | E5-base | mined-error continuation of kB |
| `deadline_50k/model.cbm` | CatBoost | Frozen comparison gate loaded by CPU fit (76 features) |
| `gate0_100k/enhanced.cbm` | CatBoost | Same bytes as `deadline_50k/model.cbm` |

Downloads must use a **pinned commit**, not `main`. The matching pipeline
stores that snapshot in `BER_HF_REVISION`.

SHA256 checksums are in [`SHA256SUMS`](SHA256SUMS).

## Load a checkpoint

```python
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoModelForSequenceClassification, AutoTokenizer

REPO = "DeeAxe/business-entity-matching-encoders"
tag, backbone = "kA", "intfloat/multilingual-e5-base"  # or e5_cont1300k + e5-small
path = hf_hub_download(REPO, f"{tag}/model.pt", revision="<pinned commit>")
tok = AutoTokenizer.from_pretrained(backbone)
model = AutoModelForSequenceClassification.from_pretrained(backbone, num_labels=1)
model.load_state_dict(torch.load(path, map_location="cpu"))
model.eval()
```

Training recipes that produced these files (data prep, seeds, learning rates,
hard-mix and mined-error continuations) are in the matching pipeline that
consumes this repository; they can be re-run to rebuild every `model.pt`.

## Licence

MIT, matching the E5 base checkpoints.
