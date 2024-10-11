## Introduction to Passage Retrieval

### Passage Retrieval

- 질문에 맞는 문서를 찾는 것

### Open-domain Question Answering

- 대규모 문서 중에서 질문에 대한 답 찾기
- Passage Retrieval과 MRC를 이어서 2-Stage로 만들 수 있음
- Querydhk Passage를 임베딩한 뒤 유사도로 랭킹을 매기고, 유사도가 가장 높은 Passage를 선택함

## Passage Embedding and Sparse Embedding

### Passage Embedding Space

- 벡터 스페이스 상의 거리 또는 내적으로 유사도를 계산함

### Sparse Embedding

- 단어가 존재하는지(1) 안하는지(0)를 1과 0으로 표현함
- Bag-of-Words(BoW)라고 함

1. BoW를 구성하는 방법 → n-gram
2. Term value를 결정하는 방법
   - Term이 문서에 등장하는지(binary)
   - Term이 몇번 등장하는지(term frequency)

특징

- Dimension of embedding vector = number of terms
  - 등장하는 단어가 많아질수록 증가
  - N-gram의 n이 커질수록 증가
  - Term overlap을 정확하게 잡아 내야 할 때 유용
  - 의미가 비슷하지만 다른 단어인 경우 비교 불가

## TF-IDF(Term Frequency - Inverse Document Frequency)

- Term Frequency: 단어의 등장빈도
- Inverse Document Frequency: 단어가 제공하는 정보의 양
  다른 문서에 자주 등장하지만

### Term Frequency

- 측정 방법
  1. Raw count
  2. Adjusted for doc length: raw count/ num words(TF)
  3. Other variants, log normalization

### Inverse Document Frequency

- 측정 방법

$$ IDF(t) = \log \frac{N}{DF(t)} $$

## BM25

TF-IDF의 개념을 바탕으로, 문서의 길이까지 고려하여 점수를 매기는 방식
