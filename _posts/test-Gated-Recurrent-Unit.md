---
title: Gated Recurrent Unit (GRU)
date: 2024-07-23
categories: machine-learning
---

[참고 영상](https://www.coursera.org/learn/nlp-sequence-models/lecture/agZiL/gated-recurrent-unit-gru)

장기적인 의존성 포착을 잘하지 못하는(vanishing gradients) 기본 RNN를 더 잘 포착하기 위해 RNN의 숨겨진 레이어를 수정

$$
a^{<t>} = g(W_a[a^{<t-1>}, x^{<t>}] + b_a)
$$

## GRU

> The **cat**, which already ate ..., **was** full

> The **cats**, which already ate ..., **were** full

c = memory cell

- 역할 : 메모리를 제공하는 것
- 단수인지 복수인지 기억을 할 수 있게 함

$ c^{<t>} = a^{<t>} $

$ \sim{c}^{<t>} = \tanh(W_c[c^{<t-1>}, x^{<t>}] + b_c) $
GRU의 중요한 아이디어 **게이트**를 가진다는 것

- update gate : $ \gamma $ 로 표현
- $ \gamma $는 언제나 0과 1사이의 값을 가짐
  - 직관을 위해 0 또는 1이라고 생각 -각
    $ \gamma_u = \sigma ( W_u[c^{<t-1>}, x^{<t>}]+b_u) $

$ \sim{c}^{<t>} $를 사용해서 업데이트하려는 후보를 찾음

c^{<t>}
