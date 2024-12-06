---
title: "LLM의 Instruction Tuning 과정 상세 분석"
date: 2024-12-05
categories: machine-learning
tags: 
- LLM
- RLHF
- AI
- Machine Learning
---
LLM을 더 안전하고 유용하게 만들기 위한 Instruction Tuning 프로세스

### 1. Supervised Fine-Tuning (SFT)

#### 수학적 정의
대규모 언어 모델(LLM) $f_\theta$는 파라미터 $\theta$로 정의되며, 지도 데이터셋 $D = \{(x_i, y_i)\}_{i=1}^N$을 사용하여 학습된다. 이 과정에서 모델의 학습 목표는 손실 $\mathcal{L}$을 최소화하는 것이다. 이 수학적 목표는 아래와 같이 표현된다:

$$
\theta^* = \arg\min_{\theta} \frac{1}{N} \sum_{i=1}^N \mathcal{L}(f_\theta(x_i), y_i)
$$

- 여기서 $\mathcal{L}$은 모델의 출력 $f_\theta(x_i)$와 정답 $y_i$ 간의 손실(예: Cross-Entropy Loss)이다.
- $x_i$는 사용자 입력, $y_i$는 그에 따른 적절한 응답이다.

#### 이해하기 쉽게 설명
이 식의 의미는 모델 $f_\theta$가 $x_i$라는 입력에 대해 $y_i$라는 정답을 출력하도록 학습하는 것이다. 수식에서 $N$은 데이터셋의 크기, $\theta$는 모델의 파라미터(가중치)이다. 손실 $\mathcal{L}$을 줄이는 과정은 모델이 더 좋은 응답을 생성하도록 만드는 핵심이다.

---

### 2. Reward Model 구축

#### 수학적 정의
Reward Model $R_\phi(x, y)$는 입력 $x$와 응답 $y$에 대해 점수를 부여한다. 이 점수는 응답의 품질을 나타낸다. Reward Model의 학습 목표는 인간 평가자가 부여한 점수 $s_i$와 모델의 평가 결과가 최대한 일치하도록 하는 것이다. 이 목표는 아래와 같이 표현된다:

$$
\phi^* = \arg\min_{\phi} \frac{1}{N} \sum_{i=1}^N \mathcal{L}_{\text{reward}}(R_\phi(x_i, y_i), s_i)
$$

- $R_\phi(x_i, y_i)$: 모델이 평가한 점수.
- $s_i$: 인간 평가자가 부여한 점수.
- $\mathcal{L}_{\text{reward}}$: 모델의 점수와 인간 평가 점수 간의 차이를 최소화하기 위한 손실 함수.

#### 이해하기 쉽게 설명
Reward Model은 LLM이 생성한 응답의 "좋음"을 점수로 평가한다. $s_i$는 사람이 평가한 기준 점수이며, $R_\phi(x_i, y_i)$는 모델이 예측한 점수다. 이 모델은 사람이 판단한 점수와 최대한 비슷한 점수를 예측하도록 학습한다. 쉽게 말해, 사람이 "이 답변이 좋다"라고 생각한 기준을 모델에 학습시키는 과정이다.

---

### 3. RLHF (Reinforcement Learning from Human Feedback)

#### 수학적 정의
강화 학습을 통해 LLM의 정책 $\pi_\theta$를 최적화한다. 여기서:
- 상태: $x$ (사용자 입력),
- 행동: $y$ (LLM이 생성한 응답),
- 보상: Reward Model $R_\phi(x, y)$.

정책 학습의 목표는 모델이 높은 보상을 받을 수 있는 답변을 생성하는 것이다. 이는 아래와 같은 수식으로 표현된다:

$$
\theta^* = \arg\max_{\theta} \mathbb{E}_{(x, y) \sim \pi_\theta}[R_\phi(x, y)]
$$

Proximal Policy Optimization(PPO) 알고리즘은 안정적인 학습을 위해 아래와 같은 손실 함수를 사용한다:

$$
\mathcal{L}_{\text{PPO}} = \mathbb{E}_t \left[ \min \left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
$$

- $r_t(\theta) = \frac{\pi_\theta(y_t|x_t)}{\pi_{\theta_\text{old}}(y_t|x_t)}$: 새 정책과 이전 정책 간의 비율.
- $\hat{A}_t$: Advantage Estimate (현재 행동이 얼마나 좋은지 나타내는 값).
- $\epsilon$: 정책 업데이트의 안정성을 유지하기 위한 제한.

#### 이해하기 쉽게 설명
이 과정은 LLM이 더 나은 답변을 생성하도록 학습시키는 방법이다. Reward Model이 응답의 품질을 점수로 평가하므로, 모델은 높은 점수를 받는 답변을 더 자주 생성하도록 강화 학습을 진행한다. PPO 알고리즘은 새로운 답변이 이전 학습된 정책과 너무 크게 달라지지 않도록 조정하는 안정화 기법이다.

---

### 구현 시 고려사항

#### 1. 비용
- 대규모 데이터셋 구축 필요: 예를 들어, GPT-3는 13개의 대규모 데이터셋을 활용.
- Reward Model 학습에는 약 33만 3천 개의 평가 데이터가 필요하며, 이를 위해 고성능 GPU 클러스터가 요구됨.

#### 2. 품질 관리
- **안전성**과 **유용성**의 균형을 지속적으로 모니터링.
- 모델 출력의 편향성과 윤리적 문제를 해결하기 위한 반복적인 검증.
- 사용자 피드백 수집 및 응답 품질 평가를 위한 체계적 절차 필요.

---

### 결론
Instruction Tuning은 **안전성**과 **유용성**을 개선하기 위한 핵심 프로세스다.  
- **SFT**는 지도 학습으로 모델의 초기 성능을 조정.  
- **Reward Model**은 응답 품질을 정량화하여 모델 개선의 기준점 제공.  
- **RLHF**는 사용자의 피드백을 활용해 실제로 유용한 답변을 생성하도록 강화 학습을 적용.

이 세 단계는 상호 보완적으로 작용하여 LLM의 성능을 지속적으로 향상시키는 기반이 된다.