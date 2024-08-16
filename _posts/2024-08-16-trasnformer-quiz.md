---
title: Transformer Quiz
date: 2024-08-16
categories: machine-learning
---

### 퀴즈 1:

RNN은 시퀀스 데이터를 순차적으로 처리하는 과정에서 학습의 어려움이 발생한다. 이 어려움 중 하나로, 타임 스텝(time step)이 늘어날수록 초기 입력 정보가 뒤로 갈수록 점점 약해지는 이유는 무엇이며, 이 문제는 어떻게 정의할 수 있는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       이는 **Vanishing Gradient Problem**과 **Exploding Gradient Problem**으로 정의한다. RNN에서는 각 타임 스텝에서의 상태가 이전 타임 스텝의 상태에 의존하기 때문에, 긴 시퀀스의 경우 초기 입력 정보가 시간이 지남에 따라 희미해지거나 소멸될 수 있다. 이로 인해 역전파 과정에서 그라디언트가 점점 작아지거나 커지면서 학습이 잘 이루어지지 않는 문제가 발생한다.
    </div>
</div>

### 퀴즈 2:

LSTM은 RNN의 장기 의존성 문제를 해결하기 위해 도입된 모델이다. LSTM에서 정보를 선택적으로 기억하고 잊을 수 있게 해주는 두 가지 주요 게이트는 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       **Forget Gate**와 **Input Gate**이다. Forget Gate는 이전 정보를 잊을지 결정하고, Input Gate는 새로운 정보를 기억할지 결정한다.
    </div>
</div>

### 퀴즈 3:

LSTM은 RNN의 어떤 주요 문제를 개선하기 위해 개발되었는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       LSTM은 RNN의 장기 의존성 문제(**Vanishing Gradient Problem**)를 해결하여, 긴 시퀀스에서도 중요한 정보를 잃지 않도록 개선하였다.
    </div>
</div>

### 퀴즈 4:

GRU는 LSTM의 변형 모델로, 더 간단한 구조를 가지고 있다. GRU는 LSTM과 달리 몇 개의 게이트를 사용하며, 그 게이트들의 역할은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       GRU는 **두 개의 게이트**(Reset Gate와 Update Gate)를 사용한다. Reset Gate는 이전 정보를 얼마나 반영할지 결정하고, Update Gate는 현재 상태를 얼마나 업데이트할지 결정한다.
    </div>
</div>

### 퀴즈 5:

GRU가 LSTM보다 간단한 구조를 가지는 이유는 무엇인가? GRU의 이러한 구조적 간소화가 제공하는 이점은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       GRU는 LSTM보다 적은 수의 게이트(두 개)와 셀 상태를 사용하여 계산량이 적고, 구조가 단순해졌기 때문이다. 이로 인해 훈련 속도가 빠르고, 더 적은 데이터로도 학습할 수 있는 이점이 있다.
    </div>
</div>

### 퀴즈 6:

Attention 메커니즘이 도입된 주요 이유는 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Attention은 입력 시퀀스 내에서 중요한 부분에 가중치를 더 많이 부여함으로써, 특정 요소들에 더 집중할 수 있도록 설계되었다. 이는 특히 긴 시퀀스에서 중요한 정보를 강조할 수 있게 한다.
    </div>
</div>

### 퀴즈 7:

Attention 메커니즘이 RNN 기반 모델과 결합되었을 때, 어떤 이점을 제공하는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Attention 메커니즘은 RNN의 장기 의존성 문제를 완화시키고, 모델이 시퀀스 내에서 중요한 단어들을 선택적으로 집중하게 만들어 번역, 문장 생성 등의 작업에서 성능을 크게 향상시킨다.
    </div>
</div>

### 퀴즈 8:

Transformer 모델은 RNN, LSTM과는 다르게 시퀀스를 병렬로 처리할 수 있다. 이 모델이 병렬 처리가 가능한 이유는 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Transformer는 **Self-Attention** 메커니즘을 사용하여 입력 시퀀스의 모든 단어를 동시에 처리할 수 있기 때문에, RNN 기반 모델들보다 병렬 처리가 가능하다.
    </div>
</div>

### 퀴즈 9:

Transformer는 RNN이나 LSTM과 달리 시퀀스의 순서 정보를 자연스럽게 학습할 수 없다. 이 문제를 해결하기 위해 Transformer 모델에서 사용되는 기법은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       **포지셔널 인코딩(Positional Encoding)**이다. 이는 시퀀스 내에서 각 단어의 위치 정보를 벡터로 인코딩하여 Transformer가 위치 정보를 학습할 수 있게 한다.
    </div>
</div>

### 퀴즈 10:

Transformer 모델의 주요 혁신 중 하나인 Multi-Head Attention은 기존의 Attention 메커니즘에 비해 어떤 장점을 제공하는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Multi-Head Attention은 여러 개의 Attention을 병렬로 수행함으로써, 입력 시퀀스의 다양한 측면을 동시에 학습할 수 있는 능력을 제공한다. 이로 인해 모델이 더 풍부한 문맥 정보를 포착할 수 있다.
    </div>
</div>

### 퀴즈 11:

Self-Attention 메커니즘에서 입력 시퀀스의 각 단어가 변환되는 세 가지 벡터는 무엇이며, 이 벡터들은 어떤 학습 가능한 가중치 행렬을 통해 만들어지는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Query, Key, Value 벡터이며, 각각 \( W_Q \), \( W_K \), \( W_V \)라는 가중치 행렬을 통해 생성된다.
    </div>
</div>

### 퀴즈 12:

Multi-Head Attention에서 각 헤드는 서로 다른 정보를 학습할 수 있다. 이는 어떤 학습 과정 덕분에 가능한가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       각 헤드는 독립적인 가중치 행렬을 가지며, 동일한 손실 함수를 최소화하기 위해 서로 다른 정보를 학습하게 된다. 이로 인해 경쟁적 학습이 발생한다.
    </div>
</div>

### 퀴즈 13:

Multi-Head Attention에서 각 헤드의 출력이 결합될 때, 결합된 벡터의 차원은 어떻게 계산되는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       각 헤드에서 생성된 벡터는 결합(concatenate)되어 차원이 \( h \times d_v \)로 증가한다. 여기서 \( h \)는 헤드의 수, \( d_v \)는 각 헤드의 Value 벡터의 차원이다.
    </div>
</div>

### 퀴즈 14:

Multi-Head Attention에서 "헤드(head)"라는 용어는 어떤 의미를 가지고 있는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       "Head"는 독립적으로 동작하는 Self-Attention 모듈을 의미하며, 여러 헤드가 병렬로 존재하여 각각 서로 다른 정보를 학습할 수 있다.
    </

div>

</div>

### 퀴즈 15:

RNN이 직면했던 장기 의존성 문제는 어떻게 해결되었으며, 이 문제를 해결한 주요 모델들의 발전 순서를 나열하라.

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       장기 의존성 문제는 **LSTM**과 **GRU** 모델을 통해 해결되었다. LSTM과 GRU는 각각 셀 상태와 게이트를 도입하여, 중요한 정보를 장기간 유지할 수 있게 하였으며, 이전의 상태 정보를 효과적으로 활용하여 그라디언트 소실 문제를 극복했다. 이들의 발전 순서는 RNN → LSTM → GRU → Transformer이다.
    </div>
</div>

### 퀴즈 16:

Transformer 모델이 등장함으로써, 기존의 RNN 기반 모델들이 갖고 있던 어떤 주요 문제들이 해결되었는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       Transformer는 RNN의 **순차 처리로 인한 병렬 처리의 어려움**과 **장기 의존성 문제**를 해결하였다. 이를 통해 모델의 학습 효율과 성능이 크게 개선되었다.
    </div>
</div>
