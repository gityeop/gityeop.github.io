---
title: Inverted Index란?
date: 2024-11-11
categories: machine-learning
tags: ["ai/information-retrieval", "ai/search", "science/algorithms"]
---

- [Inverted Index란?](#inverted-index란)
  - [Inverted Index란?](#inverted-index란-1)
  - [왜 "Inverted Index"라고 부를까?](#왜-inverted-index라고-부를까)
  - [정방향 인덱스와 Inverted Index의 차이점](#정방향-인덱스와-inverted-index의-차이점)
    - [정방향 인덱스 (Forward Index)](#정방향-인덱스-forward-index)
    - [Inverted Index](#inverted-index)
  - [Inverted Index의 장점](#inverted-index의-장점)
  - [Inverted Index는 어디에 사용될까?](#inverted-index는-어디에-사용될까)

## Inverted Index란?

검색 엔진의 성능을 높이는 핵심 요소 중 하나가 바로 **Inverted Index**다. 이번 글에서는 Inverted Index가 무엇인지, 왜 이런 이름이 붙었는지, 구체적인 예시를 통해 이 개념을 이해해보자.

---

### Inverted Index란?

**Inverted Index**는 검색 엔진이 특정 키워드와 관련된 문서를 빠르게 찾을 수 있도록 만들어진 데이터 구조다. Inverted Index는 **각 단어(키워드)가 어떤 문서에 포함되어 있는지**를 매핑하여 저장하는 방식이다.

검색 시스템에서 사용자가 특정 단어나 문구를 입력할 때, 이 구조 덕분에 검색 엔진은 해당 단어가 포함된 문서를 신속하게 찾아낼 수 있다.

예를 들어, 사용자가 "blue"라는 단어로 검색했을 때, 이 단어가 포함된 문서들을 곧바로 조회할 수 있는 것이다.

---

### 왜 "Inverted Index"라고 부를까?

"Inverted Index"라는 이름이 붙은 이유는 전통적인 **정방향 인덱스(Forward Index)** 방식과 비교하면 이해하기 쉽다. 정방향 인덱스 방식에서는 각 문서에 어떤 단어들이 포함되어 있는지 하나씩 기록한다. 반면, Inverted Index는 **각 단어에 대해 해당 단어가 포함된 문서 목록을 기록하는 방식**이다. 즉, 문서와 단어 간의 관계를 거꾸로(반대로) 기록하기 때문에 "Inverted Index"라는 이름이 붙었다.

---

### 정방향 인덱스와 Inverted Index의 차이점

세 개의 문서가 있다고 가정해 보자.

1. **문서 1**: "Sky is blue"
2. **문서 2**: "Blue ocean is beautiful"
3. **문서 3**: "Sky and ocean are blue"

이 문서들을 기준으로 정방향 인덱스와 Inverted Index를 각각 만들어보자.

#### 정방향 인덱스 (Forward Index)

정방향 인덱스에서는 각 문서마다 포함된 단어들을 리스트로 저장한다.

- **문서 1**: ["Sky", "is", "blue"]
- **문서 2**: ["Blue", "ocean", "is", "beautiful"]
- **문서 3**: ["Sky", "and", "ocean", "are", "blue"]

이 정방향 인덱스에서는 특정 단어가 포함된 문서를 찾으려면, 모든 문서를 하나씩 확인해야 한다. 예를 들어, "blue"라는 단어가 포함된 문서를 찾기 위해선 모든 문서에 이 단어가 포함되어 있는지 일일이 검색해야 한다.

#### Inverted Index

반면, Inverted Index는 각 단어에 어떤 문서가 포함되어 있는지를 기록한다.

- **"Sky"** : [문서 1, 문서 3]
- **"is"** : [문서 1, 문서 2]
- **"blue"** : [문서 1, 문서 2, 문서 3]
- **"ocean"** : [문서 2, 문서 3]
- **"beautiful"** : [문서 2]
- **"and"** : [문서 3]
- **"are"** : [문서 3]

이 구조에서는 "blue"라는 단어가 포함된 문서를 찾고 싶다면 Inverted Index에서 "blue" 항목만 조회하면 된다. 결과는 [문서 1, 문서 2, 문서 3]으로, 검색 시간을 대폭 줄일 수 있다.

---

### Inverted Index의 장점

Inverted Index의 가장 큰 장점은 **검색 속도와 효율성을 극대화**한다는 점이다. 각 단어가 포함된 문서 목록을 미리 저장해 두기 때문에, 검색할 때마다 모든 문서를 전부 읽어볼 필요가 없다. 이렇게 함으로써 **데이터베이스나 검색 엔진의 성능을 최적화**할 수 있다.

1. **빠른 검색 속도**: 특정 단어에 대해 포함된 문서를 찾으려면 모든 문서를 하나씩 검색하는 대신 Inverted Index에서 해당 단어가 포함된 문서 목록을 즉시 찾아낼 수 있다. 특히 대용량 데이터에서 이 방식은 검색 시간을 획기적으로 단축시킨다.
2. **효율적인 데이터 구조**: 정방향 인덱스와 달리 Inverted Index는 각 단어가 포함된 문서만 기록하므로, 단어별로 필요하지 않은 정보를 최소화하여 더 작은 메모리 공간을 차지한다. 이는 메모리와 저장소를 절약하는 동시에 검색 속도를 높인다.

3. **확장성**: Inverted Index는 시스템이 다루는 데이터의 양이 많아질수록 그 효율성이 더 두드러진다. 새로운 문서를 추가하거나 기존 문서에서 단어를 수정할 때, 해당 단어에 연결된 문서 목록만 업데이트하면 되므로 확장성과 유지보수 측면에서도 유리하다.

이와 같은 장점 덕분에, Inverted Index는 검색 엔진과 데이터베이스 시스템에서 필수적인 구성 요소로 자리 잡았다.

---

### Inverted Index는 어디에 사용될까?

Inverted Index는 검색 엔진뿐 아니라 다양한 정보 검색 시스템에서 사용된다. 대표적인 예로 **Elasticsearch**와 **Apache Lucene** 같은 검색 엔진을 들 수 있다. 이들 검색 엔진은 Inverted Index를 기반으로 **BM25 알고리즘**을 활용하여 검색 결과를 효과적으로 정렬하고 우선순위를 매긴다.

**BM25**는 정보 검색에서 **검색 쿼리와 문서 간의 관련성을 평가하는 알고리즘**이다. Inverted Index는 BM25와 같은 알고리즘에 필요한 문서와 단어 간의 매핑을 미리 저장함으로써, **문서의 관련성을 빠르게 계산할 수 있도록** 한다.

예를 들어, 사용자가 "blue ocean"이라는 검색어를 입력하면 Inverted Index를 통해 "blue"와 "ocean"이 포함된 문서 목록을 빠르게 조회하고, BM25 알고리즘이 각 문서의 관련성을 평가하여 가장 적합한 순서대로 결과를 반환하는 것이다.

BM25는 단순히 키워드 일치만을 기반으로 하지 않고, 문서 길이나 특정 키워드의 빈도 등을 고려하여 관련성을 계산하기 때문에, Inverted Index와 함께 사용할 때 검색 엔진의 성능과 정확도가 크게 향상된다. 이는 검색 엔진이 사용자에게 더욱 정확하고 신속한 검색 결과를 제공할 수 있도록 돕는다.
