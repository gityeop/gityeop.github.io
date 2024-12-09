---
title: LangChain 튜토리얼 가이드
date: 2024-11-22
categories: machine-learning
excerpt: "랭체인 튜토리얼"
tags: ["ai/llm", "tools/langchain", "blog/tutorial"]
---
<!-- TOC -->

- [LangChain 소개](#langchain-%EC%86%8C%EA%B0%9C)
- [기본 구성 요소](#%EA%B8%B0%EB%B3%B8-%EA%B5%AC%EC%84%B1-%EC%9A%94%EC%86%8C)
    - [LLM/Chat Models](#llmchat-models)
        - [Groq 사용](#groq-%EC%82%AC%EC%9A%A9)
        - [OpenAI 사용](#openai-%EC%82%AC%EC%9A%A9)
        - [Ollama 사용](#ollama-%EC%82%AC%EC%9A%A9)
    - [프롬프트 템플릿](#%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%ED%85%9C%ED%94%8C%EB%A6%BF)
    - [출력 파서](#%EC%B6%9C%EB%A0%A5-%ED%8C%8C%EC%84%9C)
- [주요 기능 및 사용 예시](#%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EB%B0%8F-%EC%82%AC%EC%9A%A9-%EC%98%88%EC%8B%9C)
    - [체인 구성](#%EC%B2%B4%EC%9D%B8-%EA%B5%AC%EC%84%B1)
    - [비동기 처리](#%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%B2%98%EB%A6%AC)
- [실제 구현 예시](#%EC%8B%A4%EC%A0%9C-%EA%B5%AC%ED%98%84-%EC%98%88%EC%8B%9C)
    - [질문 생성 시스템](#%EC%A7%88%EB%AC%B8-%EC%83%9D%EC%84%B1-%EC%8B%9C%EC%8A%A4%ED%85%9C)
    - [데이터 검증 시스템](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B2%80%EC%A6%9D-%EC%8B%9C%EC%8A%A4%ED%85%9C)

<!-- /TOC -->

## 1. LangChain 소개
LangChain은 언어 모델(LLM)을 활용한 애플리케이션 개발을 위한 프레임워크다. 다양한 LLM을 쉽게 통합하고, 체인과 에이전트를 구성하여 복잡한 작업을 수행할 수 있도록 도와준다.

## 2. 기본 구성 요소

### 2.1 LLM/Chat Models

#### Groq 사용
```python
from langchain_groq import ChatGroq

# Groq LLM 초기화
chat_model = ChatGroq(
    temperature=0.1,
    model_name="model_name",
    api_key="your_api_key"
)
```

#### OpenAI 사용
```python
from langchain_openai import ChatOpenAI

# OpenAI LLM 초기화
chat_model = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4",  # 또는 "gpt-3.5-turbo"
    api_key="your_openai_api_key"
)
```

#### Ollama 사용
```python
from langchain_community.llms import Ollama

# Ollama LLM 초기화
llm = Ollama(
    model="llama2",  # 또는 "mistral", "codellama" 등
    temperature=0.5,
    base_url="http://localhost:11434"  # Ollama 서버 URL
)

# 또는 Ollama Chat 모델 사용
from langchain_community.chat_models import ChatOllama

chat_model = ChatOllama(
    model="llama2",
    temperature=0.5
)
```

### 2.2 프롬프트 템플릿
```python
from langchain.prompts import PromptTemplate

# 프롬프트 템플릿 생성
prompt = PromptTemplate(
    template="Context: {context}\nQuestion: {question}\nChoices: {choices}\nAnswer: {answer}",
    input_variables=["context", "question", "choices", "answer"]
)
```

### 2.3 출력 파서
```python
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Pydantic 모델 정의
class AnswerResponse(BaseModel):
    answer: int = Field(description="답변 번호 (1-5)", ge=1, le=5)

# 파서 초기화
parser = PydanticOutputParser(pydantic_object=AnswerResponse)
```

## 3. 주요 기능 및 사용 예시

### 3.1 체인 구성
LangChain은 여러 컴포넌트를 체인으로 연결하여 복잡한 작업을 수행할 수 있다.

```python
# 프롬프트 템플릿과 출력 파서 연결
prompt = PromptTemplate(
    template=template_text + "\n{format_instructions}",
    input_variables=["context", "question", "choices"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

### 3.2 비동기 처리
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_batch(batch_data, model):
    with ThreadPoolExecutor() as executor:
        futures = []
        for item in batch_data:
            future = executor.submit(process_single_item, item, model)
            futures.append(future)
        
        results = []
        for future in as_completed(futures):
            results.append(future.result())
        return results
```

## 4. 실제 구현 예시

### 4.1 질문 생성 시스템
```python
def generate_answer(context: str, question: str, choices: List[str]):
    """
    주어진 문맥과 질문에 대한 답변을 생성한다.
    
    Args:
        context: 문제의 문맥
        question: 질문 내용
        choices: 선택지 목록
    
    Returns:
        AnswerResponse: 1-5 사이의 답변 번호
    """
    try:
        # 프롬프트 준비
        messages = [
            {"role": "system", "content": "문제를 해결하고 정답 번호를 선택하는 assistant다."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}\nChoices: {choices}"}
        ]
        
        # LLM에 요청
        response = chat_model.invoke(messages)
        
        # 응답 파싱
        return parser.parse(response.content)
        
    except Exception as e:
        print(f"Error generating answer: {e}")
        return None
```

### 4.2 데이터 검증 시스템
```python
class QuestionFormatValidator(BaseModel):
    id: str = Field(description="질문 ID")
    context: str = Field(description="문제 문맥")
    question: str = Field(description="질문 내용")
    choices: List[str] = Field(description="선택지 목록")
    answer: str = Field(description="정답")
    is_error: int = Field(description="오류 여부 (1: 오류, 0: 정상)")
    error_type: str = Field(description="오류 유형 설명")