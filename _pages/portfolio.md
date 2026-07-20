---
layout: single
title: "AI Engineer Portfolio"
permalink: /portfolio/
author_profile: true
toc: true
toc_sticky: true
classes: wide
---

## 임상엽

제품·평가·재현 가능한 추론을 연결하는 AI Engineer입니다. Python·PyTorch 기반 LLM/RAG·Vision 실험을 React·Swift 사용자 제품으로 연결하고, 성공 사례뿐 아니라 실패 응답·검증 조건·적용 범위를 함께 남깁니다.

현재 집중하는 직무는 `AI Engineer`, `LLM/Agent Engineer`, `Applied AI Engineer`, `Forward Deployed Engineer`입니다.

## 먼저 볼 프로젝트

### Grounded RAG Evaluation Lab

검색 점수 하나로 RAG 품질을 설명하지 않고 `retrieval → answer → citation → abstention → release`를 분리해 측정한 로컬 재현 실험입니다.

- 합성 영문 문서 24개, 고정 질문 24개: 답변 가능 18개·의도적 근거 없음 6개
- BM25·dense·RRF hybrid 각각 Recall@4·MRR@4 `1.0`
- Qwen2.5-Coder 3B 원시 exact accuracy `79.2%`, 근거 없음 기권 `66.7%`
- 계약 위반 5건을 재시도·대체 답변 없이 차단
- 공개 답변 15건 exact precision `100%`, 근거 없는 질문의 답변 공개 `0건`
- 두 실행의 검색 순위·원시 응답·판정 `24/24` 일치, 단위 테스트 11개

[설계·실패·결과 상세 보기](/portfolio/grounded-rag-evaluation-lab/) · [재현 묶음 다운로드](/assets/downloads/grounded-rag-evaluation-lab.zip)

> 작은 합성 영문·단일 로컬 장비의 오프라인 실험입니다. production RAG, ACL, freshness, multi-tenancy, 동시성, SLA를 증명하지 않습니다.

### OnText

선택한 텍스트와 이미지·PDF·문서를 앱 전환 없이 OpenAI·Claude·Gemini·Ollama로 처리하는 macOS 제품입니다. 제공자별 인증·요청·streaming·첨부 제약을 공통 제품 계약으로 분리하고, 코드 서명·공증·Sparkle 업데이트를 포함한 공개 릴리스를 운영합니다.

[제품](/OnText/) · [공개 릴리스](https://github.com/gityeop/OnText-Updates/releases)

### CodexMate

여러 AI 개발 작업의 진행·대기·완료 상태를 표시하는 독립 비공식 macOS companion입니다. JSON-RPC·SQLite·JSONL을 조정하고 지연 이벤트·재시작·비동기 경합에서 상태가 역행하지 않도록 복구 규칙을 만들었습니다. 36개 파일의 388개 XCTest 메서드를 CI에서 검증합니다.

[Repository](https://github.com/gityeop/CodexMate)

### ShotTracker MVP

iPhone 영상에서 농구공과 슛 이벤트를 추적하는 온디바이스 MVP입니다. 실제 촬영 실패를 작은 공 누락과 배경 오인으로 분리하고 데이터·후처리를 조정했습니다.

- 공 검출 검증셋 mAP50 `0.747 → 0.828`
- recall `0.616 → 0.726`
- 배경 102장 중 오검출 포함 이미지 `29장 → 11장`

이 수치는 슛 성공률이 아니라 공 검출 성능입니다. 저장소·원본 데이터·실험 아티팩트는 비공개이며 면접에서 구조와 검증 범위를 설명할 수 있습니다.

### 아라부기·LLM Agent/ODQA

느린 학습자를 위한 어휘·문해력 학습 서비스에서 React·TypeScript UI와 REST API를 연결하고 HyperCLOVA X 퀴즈 생성·PEFT 요청·Gemini 평가 코드를 구현했습니다. 동일 100개 입력·8개 기준·40점 형식의 내부 반복 평가에서 평균 `22.40 → 27.95/40` 변화를 확인했고, 팀은 네이버클라우드 기업 해커톤 1위를 수상했습니다.

별도 팀 프로젝트에서는 명세 생성·문제 풀이·검증의 세 개 `Swarm client.run` 호출을 수동 순차 연결하고 LangChain 검색형 QA·RAG·fine-tuning 비교 실험에 참여했습니다. 자동 handoff나 production Agent로 부르지 않습니다.

[Agent 구현 시점 커밋](https://github.com/boostcampaitech7/level2-nlp-generationfornlp-nlp-04-lv3/commit/06cff52)

## 추가 제품

- [FlowOrFlop](https://github.com/gityeop/FlowOrFlop): Python Vision sidecar와 Rust/Tauri·React UI를 연결한 로컬 집중 상태 제품
- [Voice Diary](https://github.com/gityeop/voice_diary): Google Streaming STT → Gemini 대화 → OpenAI TTS를 연결한 음성 대화 프로토타입
- [GitHub 전체 보기](https://github.com/gityeop)

## 일하는 기준

1. 입력 데이터·평가셋·모델 버전을 고정합니다.
2. 검색·생성·제품 릴리스 판단을 한 숫자로 합치지 않습니다.
3. 원시 실패를 숨기거나 성공 응답으로 대체하지 않습니다.
4. 팀 공용 스택과 개인 구현 범위를 구분합니다.
5. 측정하지 않은 사용자 수·트래픽·SLA·비용 절감은 주장하지 않습니다.

## 기술

`Python` · `PyTorch` · `LLM/RAG Evaluation` · `LangChain` · `FastAPI` · `React/TypeScript` · `Swift/AppKit` · `Vision/Core ML` · `Automated Testing` · `GitHub Actions` · `Signed macOS Release`
