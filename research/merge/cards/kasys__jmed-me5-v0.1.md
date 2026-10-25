---
language:
- ja
base_model:
- intfloat/multilingual-e5-base
license: 
- llama3.1
- gemma
---


# Japanese Medical Document Retrieval Model (jmed-me5-v0.1)

This model is built on top of the [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) checkpoint 
and has been fine-tuned to specialize in Japanese medical document retrieval. 
It leverages crawled Japanese medical web documents and LLM-based query generation and distilation of a strong re-ranker to achieve domain specialization.

---

## Usage

See the Usage section of [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base).

## Model Overview

This model is designed for Japanese medical document search. It was fine-tuned using 750,000 Japanese medical web documents. 

The overall algorithm is based on the work presented in the paper (NOTE: The authors of this model are different from those of this paper):
  
* Tamber et al. "Teaching Dense Retrieval Models to Specialize with Listwise Distillation and LLM Data Augmentation." arXiv preprint arXiv:2502.19712 (2025).
  * GitHub: [manveertamber/enhancing_domain_adaptation](https://github.com/manveertamber/enhancing_domain_adaptation)
 

The pipeline includes:

- **LLM-Based Query Generation:**  
  A large language model is used to generate queries from a set of 50,000 source documents.  
  - Similar documents in the source set are removed to ensure diversity.  
  - Query generation is performed using [tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1) with three examples provided for few-shot learning.  
  - Generated queries are further filtered by using the LLM to check for the inclusion of relevant medical or health-related knowledge; queries failing this check are removed.

- **Candidate Query Validation & Re-ranking:**  
  - The generated queries are used to search the Japanese medical documents using [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base).
    Only queries in which the original source document appears within the top 100 results are retained.
  - A re-ranking step is performed using the [cl-nagoya/ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) model.
  - Only queries where the original document is ranked at the top are kept.  
  - The top result is treated as a positive example.
  - For candidates ranked between 1 and 100, a min-max scaling is applied. Documents scoring above a threshold (defined as Top 1 score * α) are removed, as they might already be relevant.
  - The top 20 of the remaining documents are then used as negative examples.

- **Training Loss:**  
  The model is trained using a combination of:
  - **InfoNCE Loss (DPR-style):** Encouraging embeddings of queries and positive documents to be similar, and those and negative documents to be dissimilar.
  - **KL Divergence Loss:** Minimizing the difference between the re-ranking scores and the model’s predicted scores.

## Dependencies

- Base model:
  - [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)
- Query generation:
  - [tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1)
    - Built with Meta Llama 3
    - Built with Gemma
    - [META LLAMA 3.1 COMMUNITY LICENSE](https://www.llama.com/llama3_1/license/) and [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- Reranking:
  - [cl-nagoya/ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large)

## Benchmark Results

**Japanese TREC-COVID (Japanese translation of TREC-COVID)**

|  | nDCG@10 | Recall@100 |
| -------- | -------- | -------- |
| BM25 | 0.5721 | 0.1115 | 
| ruri-base | 0.4435 | 0.0793 | 
| ruri-base-v2 | 0.6548 | 0.1163 | 
| ruri-large-v2 | 0.6648 | 0.1215 | 
| mE5-base | 0.676 | 0.1258 | 
| jmed-me5-v0.1 (mE5-base + domain adaptation) | 0.7236 | 0.1292 | 
| aken12/splade-japanese-v3 | 0.6193 | 0.1141 | 
| hotchpotch/japanese-splade-v2 | 0.7021 | 0.1274 | 

**Japanese NF-Corpus (Japanese translation of NF-Corpus)**

|  | nDCG@10 | Recall@100 |
| -------- | -------- | -------- |
| BM25| 0.3258| 0.2443| 
| ruri-base| 0.2713| 0.2544| 
| ruri-base-v2| 0.2939| 0.2651| 
| ruri-large-v2| 0.3109| 0.2797| 
| jmed-me5-v0.1| 0.2865| 0.268| 
| aken12/splade-japanese-v3| 0.3196| 0.2775| 
| hotchpotch/japanese-splade-v2| 0.3365| 0.286| 


## Contributors

- [Kenya Abe (aken12)](https://huggingface.co/aken12) (Main contributor)
- [Makoto P. Kato (mpkato)](https://huggingface.co/mpkato) (Dataset translation)