---
layout: single
title: "Grounded RAG Evaluation Lab"
date: 2026-07-20
categories: machine-learning
tags: [rag, llm, evaluation, python, reliability, ollama]
excerpt: "24개 고정 질문에서 검색, 답변, 인용, 기권, 릴리스 판정을 분리하고 원시 응답까지 24/24 재현한 로컬 RAG 평가 실험"
permalink: /portfolio/grounded-rag-evaluation-lab/
author_profile: true
toc: true
toc_sticky: true
classes: wide
---

## 한 문장 요약

RAG에서 **검색이 맞았다**와 **답변을 사용자에게 공개해도 된다**를 다른 문제로 보고, 고정 24문항의 검색·답변·인용·기권·릴리스 지표와 원시 응답을 두 번 동일하게 재현한 로컬 실험입니다.

## 왜 만들었나

RAG 데모는 관련 문서가 검색되고 자연스러운 답변이 나오면 성공처럼 보이기 쉽습니다. 하지만 실제 제품에서는 다음 질문이 따로 남습니다.

- 정답 문서를 top-k 안에 찾았는가?
- 찾은 문서만으로 답했는가?
- 인용한 문서가 실제 근거인가?
- 문서에 답이 없을 때 기권했는가?
- 모델의 원시 출력이 계약을 어기면 공개를 차단했는가?
- 같은 입력·모델로 다시 실행했을 때 실패까지 재현되는가?

이 질문을 한 점수로 합치지 않고 단계별 계약으로 만들었습니다.

```text
query
  ├─ BM25 lexical ranking
  ├─ nomic-embed-text dense ranking
  └─ RRF hybrid ranking
          ↓ top 4
  qwen2.5-coder:3b JSON answer
          ↓
  schema / exact answer / citation / abstention / grounding checks
          ↓
  release answer · release abstention · reject raw output
```

## 고정한 평가 계약

| 항목 | 계약 |
|---|---|
| 문서 | 직접 작성한 합성 영문 운영 문서 24개 |
| 질문 | 24개: 답변 가능 18개, 의도적 근거 없음 6개 |
| lexical | 외부 의존성 없는 BM25 구현 |
| dense | Ollama `nomic-embed-text:v1.5`, 768차원 |
| hybrid | 전체 BM25·dense 순위의 reciprocal-rank fusion, k=60 |
| 생성 context | generation 전에 고른 hybrid top 4만 사용 |
| 생성 | `qwen2.5-coder:3b`, temperature 0, seed 20260720, JSON schema |
| 재시도 | 0회. 실패 응답을 다시 묻거나 다른 답으로 바꾸지 않음 |
| 저장 | 데이터·모델 digest, 전체 ranking, raw response, parsed output, token, latency, 판정 |

첫 모델 호출 전 corpus와 evaluation 파일의 SHA-256을 고정했습니다.

- corpus:

  ```text
  411464ce37a73534b2c715451b74fcd396e66b96cebcc8357af51088d80c8e43
  ```

- evaluation:

  ```text
  938e2fd5e0778ca29e9b9ab3df1d1d96ac4ef07b9eeffa56065b4d1ef567d9ff
  ```

## 첫 실행을 실패 증거로 보존한 이유

첫 ungated diagnostic에서 JSON schema는 100% 유효했지만, 답이 없는 SLA·DNS 질문에 모델이 답을 만들어 냈습니다. 즉 `구조화 출력 성공`은 `근거 있는 답변 성공`이 아니었습니다.

이 결과를 지우거나 prompt를 바꿔 다시 좋은 결과만 고르지 않았습니다. `diagnostic_v1.json`에 원시 출력을 보존하고, 동일한 고정 데이터와 생성 prompt 위에 deterministic release gate를 추가했습니다.

gate는 다음 조건을 모두 통과할 때만 답변을 공개합니다.

1. JSON schema가 유효하다.
2. 답변 가능 문항은 고정 canonical sentence와 일치한다.
3. 인용 문서가 정답 근거 문서다.
4. 답이 없는 문항은 명시적으로 기권한다.
5. 답변의 핵심 내용이 인용 문서에 존재한다.

하나라도 실패하면 raw response와 정확한 오류를 남기고 공개하지 않습니다. 재시도나 대체 답변은 없습니다.

## 결과

### 검색

| 방식 | Recall@4 | MRR@4 | miss |
|---|---:|---:|---:|
| BM25 | 100.0% | 1.000 | 0 |
| dense | 100.0% | 1.000 | 0 |
| RRF hybrid | 100.0% | 1.000 | 0 |

세 방식의 1.0은 이 작은 합성 데이터에서만 성립합니다. 실제 문서 노이즈나 다국어·긴 문서·권한 필터 성능으로 일반화하지 않습니다.

### 원시 생성

| 지표 | 결과 |
|---|---:|
| 전체 exact-answer accuracy | 79.2% |
| 답변 가능 문항 exact accuracy | 83.3% |
| 근거 없음 문항 abstention accuracy | 66.7% |
| citation precision / recall | 100.0% / 100.0% |
| grounded rate | 87.5% |
| schema-valid rate | 100.0% |

실패 문항은 `Q-008`, `Q-012`, `Q-017`, `Q-021`, `Q-022`입니다. retrieval miss는 없었기 때문에 이 실험의 실패는 generation·abstention·grounding 단계로 좁힐 수 있었습니다.

### 릴리스 판정

| 결과 | 개수·비율 |
|---|---:|
| 공개 답변 | 15개 |
| 공개 기권 | 4개 |
| 차단 | 5개 |
| 답변 가능 문항 release coverage | 83.3% |
| 공개 답변 exact precision | 100.0% |
| 근거 없는 질문의 답변 공개 | 0건 |

`원시 정확도 79.2%`와 `공개 답변 precision 100%`는 모순이 아닙니다. 전자는 모든 모델 출력을 평가하고, 후자는 strict gate를 통과해 사용자에게 공개한 답변 15개만 평가합니다. 정확도를 높여 보이게 만든 것이 아니라 coverage를 83.3%로 낮추는 대신 잘못된 답변 공개를 막은 trade-off입니다.

## 재현한 범위

같은 데이터 hash와 모델 digest로 canonical run을 두 번 실행했습니다. 두 실행에서 다음 항목이 24/24 일치했습니다.

- lexical·dense·hybrid ranked document IDs
- 모델 raw response
- parsed JSON output
- 문항별 evaluation과 release decision

timestamp와 latency는 stable projection에서 제외했습니다. projection SHA-256은 다음과 같습니다.

```text
e917154a75729fb1987b5f04d7048516d512ea641830b45f7dbe418355d2982c
```

이 replay는 동일 환경의 결정적 재실행을 보여주지만, 다른 하드웨어·Ollama 버전·모델 digest에서도 동일하다는 뜻은 아닙니다.

## 로컬 실행 관측값

- generation 24회
- 순차 실행 wall latency p50 `861.0 ms`, p95 `958.0 ms`
- Ollama 보고 prompt/output token `10,893 / 1,001`
- 단위 테스트 11개

프로세스 상태를 통제하지 않은 단일 로컬 장비의 순차 측정입니다. cold start, concurrency, production SLA, provider 비용, 처리 용량으로 해석하지 않습니다.

## 실행 방법

Python 3.11 이상, 로컬 Ollama와 아래 모델 태그가 필요합니다.

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/run_benchmark.py --run-id run_01 --output-dir artifacts
python3 src/run_benchmark.py --run-id run_02 --output-dir artifacts
python3 src/verify_replay.py \
  --first artifacts/run_01.json \
  --second artifacts/run_02.json \
  --output artifacts/replay.json
python3 verify.py
```

[소스·데이터·테스트·원시 실행 아티팩트 다운로드]({{ '/assets/downloads/grounded-rag-evaluation-lab.zip' | relative_url }})

ZIP SHA-256:

```text
fb412fbbf9e627e3b51e9b8278e62a7b8b61447bff30cce90d97c739e164e6c2
```

압축 파일에는 합성 데이터와 코드·원시 응답만 있으며 개인정보, 고객 데이터, 회사 문서, 모델 가중치와 로컬 절대경로는 없습니다.

## 이 프로젝트가 증명하지 않는 것

- production RAG 운영
- vector database와 ingestion pipeline
- ACL·문서 freshness·multi-tenancy
- prompt injection·adversarial security
- 다국어·긴 문서·복합 추론
- Agent orchestration
- 동시성·부하·SLA·비용 최적화

다음 단계는 이 목록을 경험한 것처럼 이력서에 추가하는 일이 아니라, 문서 revision·사용자 권한·충돌 문서·동시 질의를 평가 계약에 하나씩 넣고 각 실패가 어느 단계에서 발생했는지 계속 분리하는 것입니다.
