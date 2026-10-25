---
language:
- multilingual
- en
- ar
- bg
- de
- el
- es
- fr
- hi
- ru
- sw
- th
- tr
- ur
- vi
- zh
license: cc-by-nc-4.0
datasets:
- xnli
- facebook/anli
pipeline_tag: zero-shot-classification
widget:
- text: Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU
  candidate_labels: politics, economy, entertainment, environment
base_model: intfloat/multilingual-e5-base
model-index:
- name: multilingual-e5-base-xnli-anli
  results: []
---

# multilingual-e5-base-xnli-anli

This model is a fine-tuned version of [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) on the XNLI and ANLI dataset.

## Model description

[Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://arxiv.org/pdf/2212.03533.pdf).
Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, Furu Wei, arXiv 2022

## How to use the model

### With the zero-shot classification pipeline

The model can be loaded with the `zero-shot-classification` pipeline like so:

```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="mjwong/multilingual-e5-base-xnli-anli")
```

You can then use this pipeline to classify sequences into any of the class names you specify.

```python
sequence_to_classify = "Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU"
candidate_labels = ["politics", "economy", "entertainment", "environment"]
classifier(sequence_to_classify, candidate_labels)
```

If more than one candidate label can be correct, pass `multi_class=True` to calculate each class independently:

```python
candidate_labels = ["politics", "economy", "entertainment", "environment"]
classifier(sequence_to_classify, candidate_labels, multi_label=True)
```

### With manual PyTorch

The model can also be applied on NLI tasks like so:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# device = "cuda:0" or "cpu"
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "mjwong/multilingual-e5-base-xnli-anli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "But I thought you'd sworn off coffee."
hypothesis = "I thought that you vowed to drink more coffee."

input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["entailment", "neutral", "contradiction"]
prediction = {name: round(float(pred) * 100, 2) for pred, name in zip(prediction, label_names)}
print(prediction)
```

### Eval results
The model was evaluated using the XNLI test sets on 15 languages: English (en), Arabic (ar), Bulgarian (bg), German (de), Greek (el), Spanish (es), French (fr), Hindi (hi), Russian (ru), Swahili (sw), Thai (th), Turkish (tr), Urdu (ur), Vietnam (vi) and Chinese (zh). The metric used is accuracy.

|Datasets|en|ar|bg|de|el|es|fr|hi|ru|sw|th|tr|ur|vi|zh|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|[multilingual-e5-base-xnli](https://huggingface.co/mjwong/multilingual-e5-base-xnli)|0.849|0.768|0.803|0.800|0.792|0.809|0.805|0.738|0.782|0.728|0.756|0.766|0.713|0.787|0.785|
|[multilingual-e5-base-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-base-xnli-anli)|0.811|0.711|0.751|0.759|0.746|0.778|0.765|0.685|0.728|0.662|0.705|0.716|0.683|0.736|0.740|
|[multilingual-e5-large-xnli](https://huggingface.co/mjwong/multilingual-e5-large-xnli)|0.867|0.791|0.832|0.825|0.823|0.837|0.824|0.778|0.806|0.749|0.787|0.793|0.738|0.813|0.808|
|[multilingual-e5-large-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-large-xnli-anli)|0.865|0.765|0.811|0.811|0.795|0.823|0.816|0.743|0.785|0.713|0.765|0.774|0.706|0.788|0.787|
|[multilingual-e5-large-instruct-xnli](https://huggingface.co/mjwong/multilingual-e5-large-instruct-xnli)|0.864|0.793|0.839|0.821|0.824|0.837|0.823|0.770|0.810|0.744|0.784|0.791|0.716|0.807|0.807|
|[multilingual-e5-large-instruct-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-large-instruct-xnli-anli)|0.861|0.780|0.816|0.808|0.806|0.825|0.816|0.758|0.799|0.727|0.775|0.780|0.721|0.787|0.795|

The model was also evaluated using the dev sets for MultiNLI and test sets for ANLI. The metric used is accuracy.

|Datasets|mnli_dev_m|mnli_dev_mm|anli_test_r1|anli_test_r2|anli_test_r3|
| :---: | :---: | :---: | :---: | :---: | :---: |
|[multilingual-e5-base-xnli](https://huggingface.co/mjwong/multilingual-e5-base-xnli)|0.835|0.837|0.287|0.276|0.301|
|[multilingual-e5-base-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-base-xnli-anli)|0.814|0.811|0.588|0.437|0.439|
|[multilingual-e5-large-xnli](https://huggingface.co/mjwong/multilingual-e5-large-xnli)|0.865|0.865|0.312|0.316|0.300|
|[multilingual-e5-large-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-large-xnli-anli)|0.863|0.863|0.623|0.456|0.455|
|[multilingual-e5-large-instruct-xnli](https://huggingface.co/mjwong/multilingual-e5-large-instruct-xnli)|0.867|0.866|0.341|0.330|0.323|
|[multilingual-e5-large-instruct-xnli-anli](https://huggingface.co/mjwong/multilingual-e5-large-instruct-xnli-anli)|0.862|0.862|0.615|0.459|0.462|

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1

### Framework versions
- Transformers 4.28.1
- Pytorch 1.12.1+cu116
- Datasets 2.11.0
- Tokenizers 0.12.1
