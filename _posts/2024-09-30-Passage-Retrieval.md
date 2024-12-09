---
title: Passage Retrieval
date: 2024-10-11
categories: machine-learning
excerpt: "문서 검색"
tags: ["information-retrieval", "nlp", "search"]
---

- [Passage Embedding and Sparse Embedding](#passage-embedding-and-sparse-embedding)
  - [Passage Embedding Space](#passage-embedding-space)
  - [Sparse Embedding](#sparse-embedding)
  - [Sparse Embedding의 특징](#sparse-embedding의-특징)
- [TF-IDF(Term Frequency - Inverse Document Frequency)](#tf-idfterm-frequency---inverse-document-frequency)
  - [Term Frequency의 측정 방법](#term-frequency의-측정-방법)
  - [Inverse Document Frequency의 측정 방법](#inverse-document-frequency의-측정-방법)
- [BM25](#bm25)
  - [수식 설명](#수식-설명)
  - [BM25의 의미](#bm25의-의미)

### Passage Retrieval

- 질문에 맞는 문서를 찾는 과정으로, 정보 검색(Information Retrieval, IR)에서 핵심적인 역할을 담당함.
- 주어진 질문(Query)에 적합한 답을 포함한 문서나 텍스트 부분을 찾아내는 작업임. 이때 효율적으로 관련 정보를 찾기 위해 다양한 방법이 사용됨.
- **Passage Retrieval**은 Open-domain Question Answering의 첫 번째 단계로 사용됨.

### Open-domain Question Answering

- Open-domain QA는 방대한 양의 문서에서 질문에 대한 정확한 답을 찾아내는 과정.
- 일반적으로 두 단계로 이루어짐: **Passage Retrieval**과 **Machine Reading Comprehension(MRC)**.
  - 첫 번째 단계에서는 질문에 적합한 문서를 검색하는 Passage Retrieval.
  - 두 번째 단계에서는 해당 문서를 바탕으로 구체적인 답을 추출하는 MRC.
- **Query와 Passage를 임베딩**하고, 임베딩된 벡터 공간에서 유사도를 기반으로 랭킹을 매겨 가장 적합한 Passage를 선택함.

## Passage Embedding and Sparse Embedding

### Passage Embedding Space

- **임베딩(Embedding)**이란 텍스트 데이터를 수치 벡터로 변환하여 계산하는 것.
- **Passage Embedding**은 문장이나 문서를 벡터로 변환한 후, 벡터 스페이스에서 질문과 유사한 Passage를 찾는 방식.
- 이 벡터 공간에서의 유사도는 주로 벡터 간의 거리(distance)나 내적(inner product)으로 계산함.
  - 유사도는 벡터가 얼마나 가까운지에 따라 결정되며, 문장의 의미적 유사성을 반영할 수 있음.

### Sparse Embedding

- **Sparse Embedding**은 텍스트에서 특정 단어가 존재하는지 여부를 이진 벡터로 표현하는 방법.
- 각 단어를 0 또는 1로 표현하며, 단어가 등장하면 1, 그렇지 않으면 0으로 표시됨.
- 이 방식은 **Bag-of-Words(BoW)**로도 불리며, 문서 내 단어의 빈도만을 고려함.
  1. **BoW 구성 방법**: BoW는 주로 **n-gram**을 통해 구성됨. 단순히 단어 하나만이 아닌 연속된 n개의 단어를 묶어 표현할 수 있음.
  2. **Term의 값 결정 방법**:
     - **Binary**: 단어가 등장하면 1, 그렇지 않으면 0.
     - **Term Frequency**: 특정 단어가 문서에 몇 번 등장했는지 빈도수로 표현.

### Sparse Embedding의 특징

- 임베딩 벡터의 차원은 **전체 단어 수**에 따라 결정됨.
  - 문서에 등장하는 단어가 많을수록 차원이 증가.
  - **n-gram**의 n이 커질수록 차원이 증가.
  - 단어의 **Term overlap**을 잘 잡아내어, 특정 문서 간의 유사도를 명확히 구별할 수 있음.
  - 그러나 의미적으로 비슷하지만 다른 단어는 구별하기 어렵다는 단점이 있음.

## TF-IDF(Term Frequency - Inverse Document Frequency)

- **TF-IDF**는 단순한 단어 빈도 기반의 임베딩 방식인 Sparse Embedding을 개선한 방법.
- **Term Frequency(TF)**: 단어의 등장 빈도를 기반으로 해당 단어의 중요성을 측정함.
- **Inverse Document Frequency(IDF)**: 전체 문서에서 얼마나 자주 등장하는지에 따라 특정 단어의 정보를 측정함.
  - 흔히 등장하는 단어는 정보량이 적고, 드물게 등장하는 단어는 더 많은 정보를 제공함.

### Term Frequency의 측정 방법

1. **Raw count**: 해당 단어가 문서에 몇 번 등장했는지.
2. **Adjusted for doc length**: 문서의 길이에 따라 조정한 빈도수.
3. **Log normalization**: 빈도수의 로그를 취하여 과도한 값의 영향력을 줄임.

### Inverse Document Frequency의 측정 방법

- IDF 공식은 다음과 같음:

$$ IDF(t) = \log \frac{N}{DF(t)} $$

- 여기서 **N**은 전체 문서 수, **DF(t)**는 단어 t가 등장한 문서 수.

## BM25

**BM25**는 TF-IDF의 개념을 바탕으로 문서의 길이까지 고려하여 점수를 매기는 방식이다. 문서가 길어지면 단어의 빈도가 자연스럽게 증가할 수 있기 때문에, BM25는 이를 보정하는 역할을 한다.

BM25의 기본 수식은 다음과 같다:

$$
\text{BM25}(q, D) = \sum_{i=1}^{n} IDF(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}
$$

여기서:

- $q_i$: 쿼리에서 $i$번째 단어.
- $f(q_i, D)$: 문서 $D$에서 쿼리 단어 $q_i$의 빈도(Term Frequency).
- $|D|$: 문서 $D$의 길이 (총 단어 수).
- $\text{avgdl}$: 코퍼스 내의 문서들의 평균 길이.
- $k_1$: 문서에서 단어의 빈도가 점수에 미치는 영향을 조절하는 매개변수 (일반적으로 1.2~2.0 사이).
- $b$: 문서의 길이가 점수에 미치는 영향을 조절하는 매개변수 (보통 0.75로 설정).
- $IDF(q_i)$: Inverse Document Frequency로, 단어 $q_i$의 정보량을 의미함. 자주 등장하지 않는 단어일수록 값이 커짐.

### 수식 설명

1. **$IDF(q_i)$**: 단어의 정보량을 나타내는 부분이다. 특정 단어가 전체 문서에서 얼마나 드물게 등장하는지를 기반으로 그 단어가 얼마나 중요한지를 결정한다. 등장 빈도가 낮은 단어일수록 $IDF$ 값이 커진다.
2. **$f(q_i, D)$**: 문서 내에서 단어 $q_i$가 몇 번 등장했는지를 나타낸다. 해당 단어가 많이 등장할수록 그 문서가 쿼리에 더 적합할 가능성이 높다고 본다.

3. $k_1 + 1$과 $k_1$: 단어의 빈도가 점수에 미치는 영향을 조절하는 부분이다. $k_1$은 단어의 빈도에 얼마나 큰 가중치를 줄지를 결정한다. 이 값이 클수록 빈도가 많이 나오는 단어들이 더 중요하게 평가된다.

4. **$1 - b + b \cdot \frac{|D|}{\text{avgdl}}$**: 문서의 길이를 보정하는 부분이다. $b$는 문서 길이에 따른 조정값으로, 문서가 평균보다 길면 점수가 감소하고, 짧으면 점수가 증가하는 식으로 작동한다. 이를 통해 문서의 길이에 따른 편향을 줄일 수 있다.

### BM25의 의미

BM25는 단순히 빈도가 높은 문서를 우선하는 것이 아니라, 문서의 길이, 단어의 중요성 등을 종합적으로 고려하여 보다 정교하게 문서를 평가한다. 특히 긴 문서들이 무조건적으로 높은 점수를 받는 것을 방지할 수 있기 때문에, 검색 엔진이나 질문 답변 시스템에서 자주 사용되는 기법이다.
