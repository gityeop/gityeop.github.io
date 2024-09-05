---
title: BERT - Self-supervised Pre-training Model
date: 2024-09-06
categories: machine-learning
---

[Self-supervised Pre-training Model - BERT](https://www.boostcourse.org/boostcampaitech7/lecture/1544451?isDesc=false)

1. **Self-Supervised Learning**2. : Image inpainting, Puzzle
   1. Image inpainting
   - Hide parts of data, learn to predict them.
   - Train with raw data, no target labels, just raw data
   1. Solve the puzzle
   - know where each image patch should be located
   - Be able to recognize each object and learn where it should be located
   - Be able to learn knowledge of large objects
1. **Transfer Learning** 1. Pre-training - Self-supervised learning to proactively train 1. Transfer learning - Fine-tuning the pre-trained model for target task
<!-- -->

**BERT: Bidirectional Encoder Representations from Transformers**

- **Model Architecture**- : Transformer encoder
- **Pre-trained Task: **- Masked language modeling(MLM), Next-sentence prediction(NSP)
  - Train with large amounts of unlabeled data

1. **Pre-training: Masked Language Model**

- Randomly masking15% of the input tokens and predicting them
  - Replace 80% of 15% tokens with [MASK] tokens
  - Replace 10% of 15% tokens with other random tokens
    - Replacing input tokens with too many [MASK] tokens cause the model to be unable to understand contexts.
  - 10% of the 15% tokens are still the original token

1. **Pre-training: Next Sentence Prediction**

- Masked language models predict words within sentences, so they are less able to predict context between sentences
- Predict if sentence A is followed by sentence B in real life
<!-- -->

1. Downstream task
   1. **Sentence Classification**
      - 주어진 한 문장에 대해 기준에 맞는 분류를 수행하는 Task
      - 감정 분류, 문법 검사
   1. **Sentence Pair Classification**
      - 주어진 두 문장에 대한 관계를 예측하는 Task
