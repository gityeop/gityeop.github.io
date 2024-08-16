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
       이는 <strong>Vanishing Gradient Problem</strong>과 <strong>Exploding Gradient Problem</strong>으로 정의한다. RNN에서는 각 타임 스텝에서의 상태가 이전 타임 스텝의 상태에 의존하기 때문에, 긴 시퀀스의 경우 초기 입력 정보가 시간이 지남에 따라 희미해지거나 소멸될 수 있다. 이로 인해 역전파 과정에서 그라디언트가 점점 작아지거나 커지면서 학습이 잘 이루어지지 않는 문제가 발생한다.
    </div>
</div>

### 퀴즈 2:

LSTM은 RNN의 장기 의존성 문제를 해결하기 위해 도입된 모델이다. LSTM에서 정보를 선택적으로 기억하고 잊을 수 있게 해주는 두 가지 주요 게이트는 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <strong>Forget Gate</strong>와 <strong>Input Gate</strong>이다. Forget Gate는 이전 정보를 잊을지 결정하고, Input Gate는 새로운 정보를 기억할지 결정한다.
    </div>
</div>

### 퀴즈 3:

LSTM은 RNN의 어떤 주요 문제를 개선하기 위해 개발되었는가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       LSTM은 RNN의 장기 의존성 문제(<strong>Vanishing Gradient Problem</strong>)를 해결하여, 긴 시퀀스에서도 중요한 정보를 잃지 않도록 개선하였다.
    </div>
</div>

### 퀴즈 4:

GRU는 LSTM의 변형 모델로, 더 간단한 구조를 가지고 있다. GRU는 LSTM과 달리 몇 개의 게이트를 사용하며, 그 게이트들의 역할은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       GRU는 <strong>두 개의 게이트</strong>(Reset Gate와 Update Gate)를 사용한다. Reset Gate는 이전 정보를 얼마나 반영할지 결정하고, Update Gate는 현재 상태를 얼마나 업데이트할지 결정한다.
    </div>
</div>

### 퀴즈 5:

GRU가 LSTM보다 간단한 구조를 가지는 이유는 무엇인가? GRU의 이러한 구조적 간소화가 제공하는 이점은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       GRU는 LSTM에 비해 구조가 간단한 이유는 <strong>셀 상태 $ C_t $</strong>와 <strong>은닉 상태 \( h_t \)</strong>를 통합하여 하나의 상태 \( h_t \)만을 사용하기 때문이다. 
      •	<strong>LSTM</strong>: 셀 상태와 은닉 상태를 각각 업데이트한다.
        \[
        C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t
        \]
        \[
        h_t = o_t \odot \tanh(C_t)
        \]
      •	<strong>GRU</strong>: 셀 상태 없이 은닉 상태 \( h_t \)만으로 정보를 처리한다.
        \[
        h_t = z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t
        \]

      이로 인해 GRU는 더 적은 파라미터와 계산량으로 더 간단한 구조를 가지며, 학습 속도가 빠르고 메모리 효율이 높다.
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
       Transformer는 <strong>Self-Attention</strong> 메커니즘을 사용하여 입력 시퀀스의 모든 단어를 동시에 처리할 수 있기 때문에, RNN 기반 모델들보다 병렬 처리가 가능하다.
    </div>
</div>

### 퀴즈 9:

Transformer는 RNN이나 LSTM과 달리 시퀀스의 순서 정보를 자연스럽게 학습할 수 없다. 이 문제를 해결하기 위해 Transformer 모델에서 사용되는 기법은 무엇인가?

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
      <strong>답안:</strong>
      <strong>포지셔널 인코딩(Positional Encoding)</strong>이다. 이는 시퀀스 내에서 각 단어의 위치 정보를 벡터로 인코딩하여 Transformer가 위치 정보를 학습할 수 있게 한다.
        •	기존 임베딩 벡터:  \mathbf{E} = [0.5, 0.3, 0.8] 
        •	포지셔널 인코딩 벡터:  \mathbf{PE} = [0.1, 0.2, 0.05]

        이 두 벡터를 더하면, 새로운 벡터  \mathbf{E{\prime}} 는 다음과 같이 된다:

        \mathbf{E{\prime}} = \mathbf{E} + \mathbf{PE} = [0.5 + 0.1, 0.3 + 0.2, 0.8 + 0.05] = [0.6, 0.5, 0.85]

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
       Query, Key, Value 벡터이며, 각각 <strong>W_Q</strong>, <strong>W_K</strong>, <strong>W_V</strong>라는 가중치 행렬을 통해 생성된다.
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
       각 헤드에서 생성된 벡터는 결합(concatenate)되어 차원이 <strong>h × d_v</strong>로 증가한다. 여기서 <strong>h</strong>는 헤드의 수, <strong>d_v</strong>는 각 헤드의 Value 벡터의 차원이다. 모델의 hidden size인 d_model과 동일하다.
    </div>
</div>

### 퀴즈 14:

RNN이 직면했던 장기 의존성 문제는 어떻게 해결되었으며, 이 문제를 해결한 주요 모델들의 발전 순서를 나열하라.

<div class="answer">
    <button class="toggle-answer">답안 보기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       장기 의존성 문제는 <strong>LSTM</strong>과 <strong>GRU</strong> 모델을 통해 해결되었다. LSTM과 GRU는 각각 셀 상태와 게이트를 도입하여, 중요한 정보를 장기간 유지할 수 있게 하였으며, 이전의 상태 정보를 효과적으로 활용하여 그라디언트 소실 문제를 극복했다. 또 한 RNN의 순차 처리로 인한 병렬 처리의 어려움 또한 해결하였다. 이들의 발전 순서는 RNN → LSTM → GRU → Transformer이다.
    </div>
</div>
