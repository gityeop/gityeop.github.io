---
title: Feel the Non-Zero Centered Problem
date: 2024-08-22
categories: machine-learning
---

<iframe frameborder="0" src="https://itch.io/embed-upload/11279872?color=333333" allowfullscreen="" width="800" height="620"><a href="https://gityeop517.itch.io/feel-the-non-zero-centered-problem">Play feel the non-zero centered problem on itch.io</a></iframe>

신경망 학습에서 non-zero centered 활성화 함수(예: Sigmoid, ReLU)가 가진 문제점은 기울기(gradient)의 부호가 항상 양수나 음수로 일정하다는 점입니다.

두 개의 매개변수 𝑤1과 𝑤2의 차원에서 기울기가 항상 같은 부호를 가진다면, 학습은 매개변수 공간에서 특정 방향(++, --)으로만 이루어지게 됩니다.

예를 들어, 각각 0.5로 초기화된 𝑤1과 𝑤2의 최적값이 0.3, 0.8이라고 한다면, 𝑤1의 학습 방향은 -, 𝑤2의 학습 방향은 +로 되어야 가장 빠른 학습이 가능하겠지만, non-zero centered 활성화 함수이기 때문에 -+로 학습이 안되고 ++, --로만 학습이 가능합니다.

이러한 학습 방식은 경사 하강법이 비효율적으로 작동하도록 하여, 목표 지점까지 지그재그 형태로 진행되며 이 때문에 학습 속도가 저하될 수 있습니다.

이 간단한 게임은 non-zero centered 활성화 함수가 어떻게 신경망 학습에 영향을 미치는지 직관적인 이해를 돕고자 만들어졌습니다.
