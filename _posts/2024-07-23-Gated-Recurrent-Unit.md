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

