---
license: mit
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: intfloat/multilingual-e5-base
base_model_relation: finetune
tags:
- product-similarity
- product-embeddings
- weak-supervision
---

> This fine-tuning project—including planning, code, data processing, training,
> evaluation, visualization, and documentation—was carried out by **GPT-6.1 Sol**
> under the repository owner's direction.

# Product Similarity E5

A fine-tuned multilingual E5 model for comparing products by function and type
across brands and models. For example, different game consoles should be closer
to each other than to a console sticker.

## Neighborhood visualization

![Recorded rotating product neighborhoods with translucent group spheres](assets/neighborhood-recording.gif)

[Product list](examples/neighborhood-15.json) · [Full example results](reports/neighborhood-15.json)

## Usage

```bash
pip install sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("beno-rohman/product-embedding-e5-base")
products = ["ps5", "wii", "nintendo switch oled", "sticker nintendo switch"]
vectors = model.encode(
    ["query: " + product for product in products],
    normalize_embeddings=True,
)
similarities = vectors @ vectors.T
print(similarities)
```

Use `query: ` for every product. Output vectors have **768 dimensions**;
descriptions are truncated to **96 tokens**, including the prefix.
Private-repository access requires an authorized Hugging Face login or token.

## Training data

Trained on **62,160 automatically generated pairs across 84 product types**,
derived from the [WDC Product Data Corpus v2](https://webdatacommons.org/largescaleproductcorpus/v2/).
Training covers same-function products, related types, different functions, and
confusing shared-name examples. Pairs were generated automatically from the
corpus. The model was fine-tuned from
[`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base).

## Evaluation

On an automatically labeled held-out test with 3,208 queries across 84 types:

| Metric | Original E5 | This model |
|---|---:|---:|
| Same-type nearest neighbor, macro average | 86.49% | 98.75% |
| Main-product versus main-product ranking | 51.34% | 98.93% |

These results measure agreement with automatically generated labels, not
independently reviewed production accuracy. Unseen types and language coverage
need application-specific testing.

This model prioritizes functional similarity. Exact-item retrieval is weaker:
42.1% Recall@1 on the earlier identity test. The earlier identity checkpoint is
retained in repository history. Similarity scores are not match probabilities.

## Details and license

[Training procedure](training/docs/product-function-training.md) ·
[Detailed model notes](training/docs/product-function-model-card.md) ·
[Evaluation reports](reports/functional)

Released under **MIT**. The dataset and third-party product text have separate
rights; see [NOTICE](NOTICE).
