---
license: apache-2.0
language:
- en
base_model:
- intfloat/multilingual-e5-base
---
## BAM Embeddings (multilingual-e5-base)

Text embeddings specialized for retrieval in the finance domain.

[Greenback Bears and Fiscal Hawks: Finance is a Jungle and Text Embeddings Must Adapt](https://aclanthology.org/2024.emnlp-industry.26.pdf).
Peter Anderson, Mano Vikash Janardhanan, Jason He, Wei Cheng, Charlie Flanagan, EMNLP 2024

This model has 12 layers,  and the embedding size is 768.

## Usage

Below is an example to encode queries and passages for text retrieval.

```python
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


# Each input text should start with "query: " or "passage: ", even for non-English texts.
# For tasks other than retrieval, you can simply use the "query: " prefix.
input_texts = [
    "query: What is a callback provision?",
    "query: EverCommerce revenue headwinds",
    "passage: Beazley PLC/ADR - But they're saying, do you confirm prior to issuing an invoice that this is the correct, or prior to paying an invoice that this is the correct...",
    "passage: EverCommerce Inc\nWe are assuming coverage of EverCommerce, which is among the leading SaaS platforms in the services sector for SMBs..."
]

tokenizer = AutoTokenizer.from_pretrained('BalyasnyAI/multilingual-e5-base')
model = AutoModel.from_pretrained('BalyasnyAI/multilingual-e5-base')

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
```

## Supported Languages

This model is initialized from [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)
and finetuned on English datasets. Other languages may see lower performance.

## Training Details

**Initialization**: [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)

**Finetuning**: contrastive loss with synthetically qenerated queries and hard negatives

| Dataset                                                                                                | Weak supervision                      | # of text pairs |
|--------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------|
| BAM internal dataset                                                                                   | (text passage, synthetic query)       | 14.3M           |

## Support for Sentence Transformers

Below is an example for usage with sentence_transformers.
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('BalyasnyAI/multilingual-e5-base')
input_texts = [
    "query: What is a callback provision?",
    "query: EverCommerce revenue headwinds",
    "passage: Beazley PLC/ADR - But they're saying, do you confirm prior to issuing an invoice that this is the correct, or prior to paying an invoice that this is the correct...",
    "passage: EverCommerce Inc\nWe are assuming coverage of EverCommerce, which is among the leading SaaS platforms in the services sector for SMBs..."
]
embeddings = model.encode(input_texts, normalize_embeddings=True)
```

Package requirements

`pip install sentence_transformers~=2.2.2`

## TIPS FOR BEST PERFORMANCE

**1. Always add the correct text prefix, either "query: " or "passage: " to input texts**

This is how the model is trained, otherwise you will see a performance degradation.

Here are some rules of thumb:
- Use "query: " and "passage: " correspondingly for asymmetric tasks such as passage retrieval.

- Use "query: " prefix for symmetric tasks such as semantic similarity, bitext mining, paraphrase retrieval.

- Use "query: " prefix if you want to use embeddings as features, such as linear probing classification, clustering.

**2. Add Context to Passages**

When a document is split into individual text passages for embedding, frequently these text passages are missing crucial information such as the title of the document, or the name and ticker of the company it relates to. To overcome this problem, BAM embeddings are trained to work well with *one line of document context added to the beginning of each text passage* (followed by a newline). 

It’s up to you what document context you should use. We have had success using combinations of the document title, author name and bio, company name, ticker, event, and date, depending on the application, e.g. “Google GOOG FY23 earnings call\n”. Only one line of document context is needed.

**3. Keep passages <=512 tokens**

Long texts will be truncated to at most 512 tokens.

## Citation

If you find our paper or models helpful, please consider citing as follows:

```
@inproceedings{anderson-etal-2024-greenback,
    title = "Greenback Bears and Fiscal Hawks: Finance is a Jungle and Text Embeddings Must Adapt",
    author = "Anderson, Peter and Janardhanan, Mano Vikash and He, Jason and Cheng, Wei and Flanagan, Charlie",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track",
    year = "2024",
}
```
