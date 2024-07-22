---
title: Vanishing gradients with RNNs
date: 2024-07-23
categories: machine-learning
---

참고 영상 : [Vanishing gradients with RNNs](https://www.coursera.org/learn/nlp-sequence-models/lecture/PKMRR/vanishing-gradients-with-rnns)

## 기본적인 RNN 알고리즘의 문제점

1. 기울기 소실(Vanising gradients)

> The **cat**, which already ate ..., **was** full
> The **cats**, which already ate ..., **were** full

위 예시는 언어가 매우 <span class="blindfold">장기적인 의존성</span>을 가질 수 있는 예

- 앞서 쓰여진 단어(cat/ cats)가 문장 후반부에 영향을 미침

하지만 기본 RNN은 <span class="blindfold">의존성</span>을 포착하는데 효과적이지 않음

- 깊은 deep neural network의 <span class="blindfold">기울기 소멸</span> 문제

신경망이 <span class="blindfold">암기</span>가 필요하다는 것을 인식하도록 하는 것이 어려울 수 있음

- 단수형이면 was, 복수형이면 were이라는 사실을 외워야 한다는 사실
- 영어는 삽입되는 관계절이 매우 길 수 있으므로 앞선 정보를 외워야할 수 있음

이 떄문에 기본 RNN은 <span class="blindfold">local</span>의 영향을 많이 받는다.

- $ \hat{y}^{<3>} $ 는 가까운 x^{<1>}, x^{<2>}, x^{<3>}의 영향을 받음
- 오류가 시퀀스의 시작으로 <span class="blindfold">역전파</span>되는 것이 어려움

2. 기울기 폭주(Exploding gradients)

- 기울기가 기하급수적으로 감소하지 않고 <span class="blindfold">통과하는 레이어의 수</span>에 따라 기하급수적으로 증가할 수 있음
- 기울기 폭주는 매개변수가 폭발하기 때문에 <span class="blindfold">발견하기 쉬움</span>
  - <span class="blindfold">NaN</span> : 숫자 오버플로우의 결과
- 솔루션 : <span class="blindfold">Gradient Clipping</span>
- 기울기 벡터를 보고 일부 임계값보다 크다면 벡터의 일부를 다시 조정해서 너무 크지 않게 만드는 것
  - <span class="blindfold">최대값</span>에 따라 클리핑됨
- 기울기 <span class="blindfold">소멸</span>은 기울기 <span class="blindfold">폭주</span>보다 해결하기 힘들다
- RNN은 1,000배 이상의 혹은 10,000배 이상의 데이터 세트를 처리함
- 이는 1,000 or 10,000 신경망 레이어

- 이에 대한 솔루션 : <span class="blindfold">gru(greater recurrent unit)</span>
