---
title: Extraction, Generation-based MRC
date: 2024-09-30
categories: machine-learning
---

## Extraction-based MRC

- 질문의 답변이 항상 주어진 지문 내에 span으로 존재 -> **텍스트 생성**보다는 텍스트의 위치 파악이 적합

## Pre-processing

### Tokenization

- 텍스트를 작은 단위로 나누는 것
- 본 강에서는 WordPiece Tokenizer 사용

---

## Generation-based MRC

1. Extraction-based MRC: 지문 내 답의 위치를 예측 ⇒ 분류 문제
2. Generation-based MRC: 질의를 보고 답변을 생성 ⇒ 생성 문제

### Metric

1. EM
2. F1 Score

## Pre-processing

Extraction-based MRC와 거의 동일

## Model

### BART

- BART의 인코더는 BERT처럼 bidirectional
- BART의 디코더는 GPT처럼 uni-directional(autoregressive)

### T5(Text-to_Text Transfer Transformer)

- 모든 텍스트 처리 문제를 "test-to-text" 문제로 취급
  - 자연어 문장이 들어가고 자연어 문장이 나온다는 점에서 text-to-text
- Relative position encoding
  - 포지션 인코딩이 절대값이 아니라 토큰 사이의 거리에 따라 정의
- Downstream task에 fine-tuning시, prefix를 사용
  - Input: "**translate English to German**: That is good" → output: "Das ist gut"

## Post-processing

### Decoding

- autoregressive: 이전 스텝에 나온 출력이 다음 스텝의 입력으로 들어감

---

```python
metric = load_metric('squad')


Args:
  - predictions: List of question-answers dictionaries with the following key-values:
        - 'id': id of the question-answer pair as given in the references (see below)
        - 'prediction_text': the text of the answer
  - references: List of question-answers dictionaries with the following key-values:
        - 'id': id of the question-answer pair (see above),
        - 'answers': a Dict in the SQuAD dataset format
            {
                'text': list of possible texts for the answer, as a list of strings
                'answer_start': list of start positions for the answer, as a list of ints
            }
            Note that answer_start values are not taken into account to compute the metric.
Returns:
    'exact_match': Exact match (the normalized answer exactly match the gold answer)
    'f1': The F-score of predicted tokens versus the gold answer
Examples:

    >>> predictions = [{'prediction_text': '1976', 'id': '56e10a3be3433e1400422b22'}]
    >>> references = [{'answers': {'answer_start': [97], 'text': ['1976']}, 'id': '56e10a3be3433e1400422b22'}]
    >>> squad_metric = datasets.load_metric("squad")
    >>> results = squad_metric.compute(predictions=predictions, references=references)
    >>> print(results)
    {'exact_match': 100.0, 'f1': 100.0}
```

```python
model_name = "bert-base-multilingual-cased"
model = AutoModelForQuestionAnswering.from_pretrained(model_name, config=config)
model

BertForQuestionAnswering(
  (bert): BertModel(
    (embeddings): BertEmbeddings(
      (word_embeddings): Embedding(119547, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (token_type_embeddings): Embedding(2, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (encoder): BertEncoder(
      (layer): ModuleList(
        (0-11): 12 x BertLayer(
          (attention): BertAttention(
            (self): BertSelfAttention(
              (query): Linear(in_features=768, out_features=768, bias=True)
              (key): Linear(in_features=768, out_features=768, bias=True)
              (value): Linear(in_features=768, out_features=768, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): BertSelfOutput(
              (dense): Linear(in_features=768, out_features=768, bias=True)
              (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): BertIntermediate(
            (dense): Linear(in_features=768, out_features=3072, bias=True)
            (intermediate_act_fn): GELUActivation()
          )
          (output): BertOutput(
            (dense): Linear(in_features=3072, out_features=768, bias=True)
            (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
      )
    )
  )
  (qa_outputs): Linear(in_features=768, out_features=2, bias=True)
)
```
