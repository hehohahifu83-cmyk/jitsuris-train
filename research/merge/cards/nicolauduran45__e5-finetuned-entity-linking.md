---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:1260
- loss:MultipleNegativesRankingLoss
base_model: intfloat/multilingual-e5-base
widget:
- source_sentence: 'query: Offshore Supply Vessel. Context: It was built in 2007 as
    an Offshore Supply Vessel (Offshore Supply Vessel) and later converted to a geotechnical
    drilling vessel by performing all necessary modifications and installing machinery
    required for drilling.'
  sentences:
  - 'passage: Light Detection and Ranging sensor [SEP] Sensor that uses light in form
    of a pulsed laser to measure ranges. [SEP] nan [SEP] LiDAR sensor'
  - 'passage: Bioenergy [SEP] Energy derived from organic biological materials including
    wood crops and waste [SEP] biomass power ,  bio-energy ,  biomass energy'
  - 'passage: Offshore Supply Vessel [SEP] A ship designed to transport supplies,
    equipment, and personnel to offshore oil and gas platforms, wind farms, and other
    marine installations. [SEP] PSV ,  platform supply vessel ,  offshore supply ship
    ,  supply ship ,  offshore supply vessel ,  platform supply ship'
- source_sentence: 'query: Implicit Association Test. Context: In addition to the
    construct validity of the Implicit Association Test, there is also uncertainty
    surrounding its predictive validity -that is, the degree to which attitudes measured
    by this task can predict social behavior.'
  sentences:
  - 'passage: Sailing Vessel [SEP] A watercraft propelled primarily by wind acting
    on sails, ranging from traditional tall ships to modern sailing yachts used for
    recreation, training, or specialized transport. [SEP] sailing vessel ,  sailship
    ,  sail ship ,  sailing ships ,  sail ships ,  sailships ,  sailing vessels ,  sail
    vessel ,  sail vessels ,  sail boat ,  sailing boat ,  sailboats ,  sailing boats
    ,  sail boats ,  individual sailboat'
  - 'passage: psychological testing [SEP] ‘Psychological testing’ is a psychometric
    measurement to evaluate a person’s response to a psychological test according
    to carefully prescribed guidelines. [adapted from [wikipedia]()] [SEP] psychological
    test ,  psychological tests ,  psychological measurement ,  psychological scale
    ,  psychometrics'
  - 'passage: Fishing Vessel [SEP] A watercraft used for catching fish and other seafood
    in marine or freshwater environments, equipped with fishing gear such as nets,
    lines, and processing facilities. [SEP] fishing boat ,  fishing ship'
- source_sentence: 'query: cerebellomedullary cistern. Context: CSF was obtained from
    the cerebellomedullary cistern of two dogs with has been demonstrated by the identification
    of hyperphosphorylated tau and axonal loss in a mouse model of experimental autoimmune
    encephalomyelitis (has been demonstrated by the identification of hyperphosphorylated
    tau and axonal loss in a mouse model of experimental autoimmune encephalomyelitis-1
    and has been demonstrated by the identification of hyperphosphorylated tau and
    axonal loss in a mouse model of experimental autoimmune encephalomyelitis-3) using
    a 22-gauge spinal needle (B Braun, Melsungen, Germany).'
  sentences:
  - 'passage: Heavy Load Carrier [SEP] A specialized cargo ship designed to transport
    exceptionally heavy or oversized items such as industrial equipment, offshore
    structures, and other vessels using semi-submersible or heavy-lift techniques.
    [SEP] heavy lift ship'
  - 'passage: Onshore wind energy [SEP] Onshore wind energy is electricity generated
    from the wind by devices located on land. It includes wind energy produced from
    devices installed on piers, platforms, breakwaters or other artificial structures,
    if those structures are connected to the land in any way. It also includes production
    from devices located in rivers and inland water bodies, where these do not fit
    the definition of offshore wind energy. [SEP] onshore wind farm ,  onshore wind
    power plant ,  onshore wind power station ,  onshore wind turbines'
  - 'passage: cerebellomedullary cistern [SEP] The largest of the subarachnoid cisterns
    between the cerebellum and the medulla oblongata; it is divided into a posterior
    cerebellomedullary cistern located between the cerebellum and the posterior surface
    of the medulla (also called cisterna magna), and a lateral cerebellomedullary
    cistern located between the cerebellum and the lateral aspect of the medulla.
    [SEP] nan'
- source_sentence: 'query: autonomous shuttles. Context: Specifically, we are interested
    to figure out the efficiency of the decentralized approach in terms of served
    users, waiting time, travel costs, autonomous shuttles usage, in different settings
    involving diverse number of users and/or autonomous shuttles.'
  sentences:
  - 'passage: Sailing Vessel [SEP] A watercraft propelled primarily by wind acting
    on sails, ranging from traditional tall ships to modern sailing yachts used for
    recreation, training, or specialized transport. [SEP] sailing vessel ,  sailship
    ,  sail ship ,  sailing ships ,  sail ships ,  sailships ,  sailing vessels ,  sail
    vessel ,  sail vessels ,  sail boat ,  sailing boat ,  sailboats ,  sailing boats
    ,  sail boats ,  individual sailboat'
  - 'passage: Natural gas [SEP] Natural gas is a mixture of hydrocarbon gases found
    in underground deposits. Natural gas is a product of the decomposition of organic
    matter trapped underground several thousand years ago. Methane is the largest
    component of natural gas, but natural gas also contains varying amounts of ethane,
    propane and heavier hydrocarbons, as well as smaller amounts of nitrogen, oxygen,
    carbon dioxide, sulphur compounds and water. [SEP] methane gas ,  NG ,  fossil
    gas'
  - 'passage: Automated mobility [SEP] Automated mobility refers to replacing the
    driver in a vehicle for dynamic driving tasks (braking, steering, environment
    monitoring, etc). [SEP] nan [SEP] nan'
- source_sentence: 'query: liquefied petroleum gas carriers. Context: Using fuel consumption
    as a main input, Psaraftis and Kontovas [25] presented an analysis on emissions
    of the world fleet for major ship types, i.e., bulk carriers, crude oil tankers,
    container vessels, product or chemical carriers, liquefied natural gas (liquefied
    natural gas) carriers, liquefied petroleum gas carriers, reefer vessels, Ro-Ro
    vessels, and general cargo ships.'
  sentences:
  - 'passage: Offshore Supply Vessel [SEP] A ship designed to transport supplies,
    equipment, and personnel to offshore oil and gas platforms, wind farms, and other
    marine installations. [SEP] PSV ,  platform supply vessel ,  offshore supply ship
    ,  supply ship ,  offshore supply vessel ,  platform supply ship'
  - 'passage: Gas Carrier [SEP] A tanker equipped with specialized pressurized or
    refrigerated tanks for transporting liquefied natural gas (LNG), liquefied petroleum
    gas (LPG), or other gaseous products. [SEP] gas tanker'
  - 'passage: Non-renewable municipal waste [SEP] Non-renewable municipal waste refers
    to waste materials from households, commerce and public services, often collected
    through municipal waste management processes. [SEP] nan'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on intfloat/multilingual-e5-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) <!-- at revision 835193815a3936a24a0ee7dc9e3d48c1fbb19c55 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False, 'architecture': 'XLMRobertaModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
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
model = SentenceTransformer("nicolauduran45/e5-finetuned-entity-linking")
# Run inference
sentences = [
    'query: liquefied petroleum gas carriers. Context: Using fuel consumption as a main input, Psaraftis and Kontovas [25] presented an analysis on emissions of the world fleet for major ship types, i.e., bulk carriers, crude oil tankers, container vessels, product or chemical carriers, liquefied natural gas (liquefied natural gas) carriers, liquefied petroleum gas carriers, reefer vessels, Ro-Ro vessels, and general cargo ships.',
    'passage: Gas Carrier [SEP] A tanker equipped with specialized pressurized or refrigerated tanks for transporting liquefied natural gas (LNG), liquefied petroleum gas (LPG), or other gaseous products. [SEP] gas tanker',
    'passage: Offshore Supply Vessel [SEP] A ship designed to transport supplies, equipment, and personnel to offshore oil and gas platforms, wind farms, and other marine installations. [SEP] PSV ,  platform supply vessel ,  offshore supply ship ,  supply ship ,  offshore supply vessel ,  platform supply ship',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8028, 0.2250],
#         [0.8028, 1.0000, 0.2569],
#         [0.2250, 0.2569, 1.0000]])
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

* Size: 1,260 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              |
  | details | <ul><li>min: 16 tokens</li><li>mean: 63.57 tokens</li><li>max: 338 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 77.89 tokens</li><li>max: 368 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                            | sentence_1                                                                                                                                                                                                                                                                               |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>query: tugboat. Context: Sharing deployment information: Information sharing between the pilot, tugboat captain and boatmen crew with their planning departments regarding the deployment information such as meeting point with the vessel, or estimated start and completion time of services.</code>                                                                         | <code>passage: Tugboat [SEP] A powerful, maneuverable vessel used to push or tow other ships in harbors, through canals, or at sea, assisting with docking and navigation in confined waters. [SEP] tugboat ,  tug boat ,  tug ,  water tractor</code>                                   |
  | <code>query: fluorescence microscope. Context: staining of the striatum and the mean fluorescence density was performed through a fluorescence microscope, green fluorescence intensity represents the expression level of tyrosine hydroxylase, the results showed that the green fluorescence in the experimental group was slightly lower than that in the Sham group (Fig.</code> | <code>passage: fluorescence microscopy [SEP] Fluorescence microscopy comprises any type of microscopy where the specimen can be made to fluoresce (emit energy as visible light), typically by illuminating it with light of specific wavelengths. [SEP] Microscopy, Fluorescence</code> |
  | <code>query: of liquefied natural gas carriers. Context: Transverse acceleration: Longitudinal acceleration: where: (2) Forced displacement of hull deformation The topic of this study is the piping system installed on the deck of liquefied natural gas carriers.</code>                                                                                                          | <code>passage: Gas Carrier [SEP] A tanker equipped with specialized pressurized or refrigerated tanks for transporting liquefied natural gas (LNG), liquefied petroleum gas (LPG), or other gaseous products. [SEP] gas tanker</code>                                                    |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
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

### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.2.2
- Transformers: 5.0.0
- PyTorch: 2.9.0+cu128
- Accelerate: 1.12.0
- Datasets: 4.0.0
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
    url = "https://arxiv.or