---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:300000
- loss:MultipleNegativesRankingLoss
base_model: intfloat/multilingual-e5-base
widget:
- source_sentence: 'query: business: SU Enterprises Pvt Ltd | address: Office Number
    Hd-157 At Sy-11, Wework, Krishe Emerald, Kondapur Main Road, Laxmi Cyber City,
    Whitefields, Serilingampally Mandal, Hyderabad, Rangareddy, Telangana'
  sentences:
  - 'passage: business: ୱାନ୍ ପ୍ରୋଡ୍ୟୁସର୍ | address: DOLAMUNDEIHARIPUR ROAD, CUTTACK,
    Odisha'
  - 'passage: business: Kelokelo | address: C-760 B, Sangam Vihar, New Delhi, South
    Delhi, Delhi'
  - 'passage: business: SU Erreprses Pvt  Ltd | address: OFFICE NUMBER HD-157 AT SY-11,
    WEWORK, KRISHE EMERALD, KONDAPUR MAIN ROAD, LAXMI CYBER CITY, WHITEFIELDS, SERILINGAMPALLY
    MANDAL, HYDERABAD, Telangana'
- source_sentence: 'query: business: Street Media (India) LLP | address: Whitefield
    Road, Mahadevapura Post, Whitefield Road, Karnataka, Bangalore'
  sentences:
  - 'passage: business: OP | address: 560 Stafford Hill Road, Cheshire, MA'
  - 'passage: business: Neera (índia) | address: H.NO ##492 VIII/20A, ERGO HEIGHTS,
    MANGAYIL LAWNS VIKRAM SARABHAI ROAD, MARADU P.O., Kerala'
  - 'passage: business: Street Media LLP Partners | address: Whitefield Road, Mahadevapura
    Post, Bangalore, KA'
- source_sentence: 'query: business: Kayle''s Unified Cleaning Service | address:
    14 Tilton Circle, Yarmouth, MA'
  sentences:
  - 'passage: business: Brixlum née Kayle''s Unified Cleaning Service | address: 14
    Tilton Circle, Yarmouth, MA'
  - 'passage: business: Fluxzetaio trading as Lorrie Johnson Block LLC | address:
    NY, 320 Lena Avenue, Freeport'
  - 'passage: business: Strategic-Pntintoing Group | address: 527-D North Line Drive,
    Hampstead, North Carolina'
- source_sentence: 'query: business: Metro Family Practice | address: W7027 B, Town
    Of Byron, WI'
  sentences:
  - 'passage: business: JONES AND  HODGES | address: TX, 004200 Sunken Ct, PORT ARTHUR'
  - 'passage: business: Herrera, Táylor & Stephens | address: 0826 Clay St, Fraanklin,
    Virginia'
  - 'passage: business: Metro Practice Partners (ID: 35149) | address: W7027  B, OAKIELD,
    WI'
- source_sentence: 'query: business: Soriano and Piedra, Inc | address: Houston, TX,
    1014 Christine Street'
  sentences:
  - 'passage: business: Kanav Technologies Private | address: Plot No.-77, 780, Ward
    No.-12, Vijay Nagar Colony, Mustafapur, Danapur, Patna, Dinapur-cum-khagaul, BR'
  - 'passage: business: TZ Electricity LLC | address: 0015005 Jansmore Court, Bowie,
    Maryland'
  - 'passage: business: Soriano & Piedra, Inc Center | address: 1014- Christine St,
    Houston, Texas'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on intfloat/multilingual-e5-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) <!-- at revision d128750597153bb5987e10b1c3493a34e5a4502a -->
- **Maximum Sequence Length:** 64 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'XLMRobertaModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'query: business: Soriano and Piedra, Inc | address: Houston, TX, 1014 Christine Street',
    'passage: business: Soriano & Piedra, Inc Center | address: 1014- Christine St, Houston, Texas',
    'passage: business: TZ Electricity LLC | address: 0015005 Jansmore Court, Bowie, Maryland',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.8361, -0.1334],
#         [ 0.8361,  1.0000,  0.0365],
#         [-0.1334,  0.0365,  1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 300,000 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                        |
  |:--------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                            |
  | details | <ul><li>min: 21 tokens</li><li>mean: 33.14 tokens</li><li>max: 64 tokens</li></ul> | <ul><li>min: 12 tokens</li><li>mean: 33.8 tokens</li><li>max: 64 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                  | sentence_1                                                                                                      |
  |:----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
  | <code>query: business: Ambika Ideal Public Limited \| address: Tilakmarg, Tilak Marg, Delhi</code>                          | <code>passage: business: Smt Ambika  Ideal Public Limited \| address: TILAKMARG, TILAK MARG, Delhi</code>       |
  | <code>query: business: Lee Fresh Office Group \| address: 135 Hollow Haven Street, Fairhope, AL</code>                      | <code>passage: business: LEE FRESH OFFICE #58116 \| address: Hollow Haven St, BALDWIN COUNTY, AL</code>         |
  | <code>query: business: Showtime Real (India) Limited \| address: 23/4, Iii Floor, East Patel Nagar, New Delhi, Delhi</code> | <code>passage: business: Limited Showtime Real (India) \| address: 23/4, DL, New Delhi, East Patel Nagar</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `num_train_epochs`: 1
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_ratio`: None
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `enable_jit_checkpoint`: False
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `use_cpu`: False
- `seed`: 42
- `data_seed`: None
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: -1
- `ddp_backend`: None
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `auto_find_batch_size`: False
- `full_determinism`: False
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `use_cache`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.2133 | 500  | 0.2652        |
| 0.4266 | 1000 | 0.0015        |
| 0.6399 | 1500 | 0.0010        |
| 0.8532 | 2000 | 0.0009        |


### Training Time
- **Training**: 1.2 hours

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 5.4.1
- Transformers: 5.0.0
- PyTorch: 2.10.0+cu128
- Accelerate: 1.13.0
- Datasets: 5.0.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->