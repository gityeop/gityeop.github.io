---
title: Word Embedding
date: 2024-08-30
categories: machine-learning
---

## One-Hot Encoding의 의미

One-Hot Encoding을 한다는 것은 서로 다른 단어들의 내적 유사도(Dot-product similarity)를 0으로 만들고

단어들 간의 유클리드 거리는 항상 sqrt(2)로 만들겠다는 뜻

-> 단어들을 표백하는 작업

다른 차원은 다 0이기 때문에 메모리 공간 절약을 위해 non-zero값의 위치로 표현하는 것을 Sparse representation이라고 한다

## Sparse Representation

- A=[1 0 0 0]^T -> 1
- B=[0 1 0 0]^T -> 2
- AB = [0 0 1 0]^T -> 3
- O=[0 0 0 1]^T -> 4

좀 더 일반화
[0 0 2.1 0 -4.7 0] -> {(3, 2.1), (5, -4.7)}

## Distributed vector(Dense Vector)

- 단어의 의미를 여러 차원에 0이 아닌 값의 형태로 표현
- 유클리드 거리, 내적, 코사인 유사도는 단어 간 의미론적 유사성을 나타냄

### 예시 설명:

#### 1. **단어의 벡터 표현**:

- 예를 들어 "king"이라는 단어를 벡터로 표현한다고 해봅시다. Distributed Vector는 "king"을 단일 숫자가 아닌 여러 차원으로 된 벡터로 나타냅니다. 예를 들어, 5차원 벡터로 표현한다면:

  $$
  \text{king} = [0.5, 0.2, 0.1, 0.7, 0.9]
  $$

- 같은 방식으로 "queen"이라는 단어는 다음과 같이 표현될 수 있습니다.

  $$
  \text{queen} = [0.6, 0.3, 0.1, 0.8, 0.95]
  $$

#### 2. **단어 간의 유사성 측정**:

- 위와 같은 벡터 표현을 통해 단어 간의 유사성을 측정할 수 있습니다. 유클리드 거리, 내적, 코사인 유사도 등의 수학적 방법을 사용하여 두 벡터 간의 거리를 계산하게 됩니다.

- 예를 들어, 코사인 유사도를 사용하여 "king"과 "queen"의 유사성을 계산한다면, 두 벡터가 이루는 각도의 코사인 값을 통해 유사성을 측정합니다. 두 벡터가 비슷한 방향을 가리킬수록 유사성 값이 1에 가까워지며, 서로 멀어질수록 값이 0에 가까워집니다.

#### 3. **의미론적 유사성**:

- 이러한 벡터 표현 덕분에 "king"과 "queen"은 의미적으로 가까운 단어이기 때문에 유사성 점수가 높게 나옵니다. 반면, "king"과 "apple" 같은 의미적으로 거리가 먼 단어는 벡터 간의 유사성 점수가 낮아집니다.

- 예를 들어, "king"과 "queen"의 코사인 유사도가 0.9라면, 이는 두 단어가 매우 유사함을 의미합니다. 반대로 "king"과 "apple"의 유사도가 0.2라면, 이 두 단어는 의미적으로 멀리 떨어져 있다는 뜻입니다.

## Word2Vec

- 워드들을 Dense vector로 표현
- 주변 단어의 정보들을 이용해 단어 벡터를 표현

### Word2Vec의 핵심 아이디어

- Cat의 앞뒤로 올 확률 $P(w|cat)$이 높은 단어는?
  - "Meow" - 0.57
  - "Potato" - 0.03
  - "Paris" - 0.05
  - "Pet" - 0.34
  - "Baquette" - 0.01
    "Cat"의 의미는 확률 분포 P(w|cat)에 의해서 결정됨

### Skip-gram

Word2Vec의 두 가지 예측 Task

1. Continuous Bag of Words(CBoW)
   - 주변단어를 이용해서 중심단어를 예측
2. Skip-gram
   - 중심단어를 이용해서 주변단어를 예측

### Word Intrusion Detection

- 이질적인 단어를 찾아내는 것
  - **staple** hammer saw drill
  - math **shopping** reading science
  - rain snow sleet **sun**
  - eight six seven five three **owe** nine
