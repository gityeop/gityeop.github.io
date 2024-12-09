---
title: "Natural Language Generation with Decoding"
date: 2024-09-06
categories: machine-learning
excerpt: "디코딩을 통한 자연어 생성"
tags: ["nlp", "text-generation", "deep-learning"]
---

[Natural Language Generation with Decoding](https://www.boostcourse.org/boostcampaitech7/lecture/1544453?isDesc=false)

Greedy decoding
Beam search
Hyperparameter: Temperature
Random sampling: Top-k, Top-p sampling

## NLP의 두 가지 주요 테스크

1. Natural Language Understanding
2. Natural Language Generation
<!-- -->

## Natural Language Generation Example

1. 기계 번역
2. 문서 요약
<!-- -->

최적의 문장을 한번에 출력하는 것은 사실상 불가능하기 때문에 다음 단어를 예측하는 Auto-regressive 방법을 사용
→ 그 다음 단어의 확률을 최대화하는 방법은?

$$
\begin{align*}
P_{LM}(\mathbf{y}|\mathbf{x}) &= P_{LM}(y_1, y_2, \ldots, y_t | \mathbf{x}) \\
&= P_{LM}(y_1 | \mathbf{x}) \times P_{LM}(y_2 | y_1, \mathbf{x}) \times P_{LM}(y_3 | y_2, y_1, \mathbf{x}) \times \cdots \times P_{LM}(y_t | y_1, \ldots, y_{t-1}, \mathbf{x}) \\
&= \prod_{i=1}^{t} P_{LM}(y_i | y_1, \ldots, y_{i-1}, \mathbf{x})
\end{align*}
$$

## Greedy Decoding

- 매 Time-step 마다 가장 높은 확률값을 갖는 Token을 다음 Token으로 선택
- 단점 - 근시안적인 접근 방법 - 정답이 아닌 Token을 선택하면, 뒤이어 생성하는 Token에 영향을 끼침
<!-- -->

## Beam Search

- 매 Time-step 마다 - **k개의 후보 단어**- 를 생성함(1개가 아닌)
  - k : Beam size
- Token을 생성할 때마다 Score가 가장 높은 k개를 추적
- 반복 생성에서 한계가 있음 - 인간은 항상 확률이 높은 단어만 선택해서 말하지 않기 때문에
<!-- -->

## Temperature

- 생성 문장의 다양성과 정확성 조절을 위해 타우 도입
- 큰 값의 타우로 확률을 나눌 경우 확률 간의 차이도 나눠지므로 큰 값으로 나누면 차이도 적어져서 출력 확률분포를 평탄하게 만듬
- Uniform 분포 → 생성 문장의 - **다양성**
- 작은 값의 타우로 확률을 나눌 경우 확률 간의 차이도 커지므로 출력 확률분포를 뾰족하게 만듬
- One-hot 분포 - Greedy decoding과 동일
<!-- -->

## Top-k Sampling

- Temperature을 조절할 경우 운이 없으면 확률이 상당히 낮은 단어가 선택될 수도 있음
- 선택 가능한 단어를 - **K개**- 로 제한하여 - **Sampling**
- 이러한 방식은 분포를 고려하지 않음

<!-- -->

## Top-p Sampling(Nucleus sampling)

- Top-k sampling처럼 개수로 선택 가능한 단어를 제한하는 것이 아닌 단어 생성 확률의 합이 p가 될 때까지 후보 단어를 선택하여 Sampling
- 확률 분포가 평평하다면 많은 수의 단어가 후보로 포함
- 확률 분포가 뾰족하다면 적은 수의 단어만이 후보로 포함
<!-- -->
