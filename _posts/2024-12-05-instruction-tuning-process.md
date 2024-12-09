---
title: "LLM의 Instruction Tuning 과정 상세 분석"
date: 2024-12-05
categories: machine-learning
tags: ['ai/llm','ai/fine-tuning']
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

Reward Model은 LLM이 생성한 응답의 "좋음"을 점수로 평가한다. $s_i$는 사람이 평가한 기준 점수이며, $R_\phi(x_i, y_i)$는 모델이 예측한 점수다. 이 모델은 사람이 판단한 점수와 최대한 비슷한 점수를 예측하도록 학습한다. 쉽게 말해, 사람이 "이 답변이 좋다"라고 생각한 기준을 모델에 학습시키는 과정이다.

---
### 3. RLHF (Reinforcement Learning from Human Feedback)

RLHF는 LLM이 인간의 피드백을 바탕으로 사용자가 선호하는 답변을 생성하도록 학습시키는 과정이다. 이 과정에서 수식은 다음의 핵심 요소들로 이루어진다.


#### **정책 학습의 목표**
$$
\theta^* = \arg\max_{\theta} \mathbb{E}_{(x, y) \sim \pi_\theta}[R_\phi(x, y)]
$$

##### **수식 요소 설명**

1. $\pi_\theta(y|x)$:
   - 모델이 입력 $x$에 대해 응답 $y$를 생성하는 확률을 나타냄.
   - 예: "주식 투자에 대해 알려주세요."라는 질문에 대한 응답 $y$의 확률을 모델이 계산.

2. $R_\phi(x, y)$:
   - Reward Model이 $x$와 $y$를 평가하여 생성하는 점수(보상).  
   - 높은 점수는 좋은 응답, 낮은 점수는 나쁜 응답을 의미.

3. $\mathbb{E}_{(x, y) \sim \pi_\theta}$:
   - 모델이 생성하는 다양한 응답($y$)의 평균 보상을 계산.  
   - 목표는 평균 보상이 가장 높아지도록 모델을 학습시키는 것.

---

#### **PPO 알고리즘 손실 함수**
$$
\mathcal{L}_{\text{PPO}} = \mathbb{E}_t \left[ \min \left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
$$

##### **수식 요소 설명**

1. $r_t(\theta) = \frac{\pi_\theta(y_t|x_t)}{\pi_{\theta_{\text{old}}}(y_t|x_t)}$:
   - 새 모델 $\pi_\theta$가 $y_t$라는 응답을 생성할 확률을 이전 모델 $\pi_{\theta_{\text{old}}}$와 비교한 비율.
   - **설명**: 새롭게 학습된 모델이 기존 모델과 얼마나 달라졌는지를 나타냄.

2. $\hat{A}_t$:
   - Advantage Estimate로, 특정 응답 $y_t$가 얼마나 좋은지를 나타냄.
   - 계산 방식: $R_\phi(x_t, y_t) - \text{baseline}$ (즉, 보상에서 기준값을 뺀 값).
   - **설명**: "이 응답이 얼마나 더 유용한가?"를 수치로 나타냄.

3. $\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)$:
   - $r_t(\theta)$의 값이 1에 가까워지도록 제한하여 모델의 업데이트가 너무 급격히 변하지 않도록 조정.
   - $\epsilon$은 허용 범위(일반적으로 작은 값, 예: 0.2).
   - **설명**: 새 모델과 기존 모델 간 차이가 너무 크면 학습을 제한해 안정성을 유지.

4. $\min \left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right)$:
   - 학습 손실을 계산할 때, $r_t(\theta)$와 $\text{clip}(r_t(\theta))$ 중 더 작은 값을 선택하여 업데이트.
   - **설명**: 안정성과 성능 향상을 동시에 추구하는 방식.

##### **설명**
PPO는 새 모델이 기존 모델보다 점진적으로 더 좋은 응답을 생성하도록 학습한다. 새 모델의 응답이 기존 응답과 너무 크게 달라지면 이를 제한하여 모델이 안정적으로 학습되도록 조정한다.

---

#### **RLHF 전체 과정 요약**
1. **Reward Model의 점수 계산**:
   - 입력과 모델 응답에 점수를 매겨 "이 응답이 얼마나 좋은가?"를 평가.

2. **정책 학습**:
   - 모델이 높은 점수를 받을 수 있는 응답을 더 자주 생성하도록 학습.

3. **PPO 알고리즘**:
   - 모델이 학습 과정에서 안정적으로 개선되도록 응답 확률을 조정.

### 결론
Instruction Tuning은 **안전성**과 **유용성**을 개선하기 위한 핵심 프로세스다.  
- **SFT**는 지도 학습으로 모델의 초기 성능을 조정.  
- **Reward Model**은 응답 품질을 정량화하여 모델 개선의 기준점 제공.  
- **RLHF**는 사용자의 피드백을 활용해 실제로 유용한 답변을 생성하도록 강화 학습을 적용.