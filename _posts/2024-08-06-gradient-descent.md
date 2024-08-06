---
title: 경사하강법 순한 맛 Gradient Descent(Mild)
date: 2024-08-06
categories: math-for-ml
---

## 미분(differentiation)

$$
f'(x) = \lim_{{h \to 0}} \frac{f(x+h) - f(x)}{h}
$$

변수의 움직임에 따른 함수값의 변화를 측정하기 위한 도구

미분은 함수 f의 주어진 점 (x, f(x))에서의 <span class="blindfold" data-hint="">접선의 기울기</span>

한 점에서의 접선의 기울기를 알면 어느 방향으로 점을 움직여야 함수값이 **증가**하는지 / **감소**하는지 알 수 있다.

경사하강법(gradient descent): 미분값을 빼서 함수의 <span class="blindfold" data-hint="">극소값</span>의 위치를 구할 때 사용한다.

경사상승법(gradient ascent): 미분값을 더해서 함수의 <span class="blindfold" data-hint="">극대값</span>의 위치를 구할 때 사용한다.

- 경사상승법/경사하강법은 극값에 도달하면 움직임을 멈춘다.

### 경사하강법 알고리즘

경사하강법은 함수의 최소값을 찾기 위해 반복적으로 미분값을 이용해 함수값을 줄이는 방법이다.

1. 초기값 설정: $ \( x_0 \) $
2. 학습률 설정: $ \( \alpha \) $
3. 경사 계산: $ \( \nabla f(x_t) \) $
4. 업데이트: $ \( x\_{t+1} = x_t - \alpha \nabla f(x_t) \) $
5. 종료 조건 만족 시 알고리즘 종료

```python
import sympy as sym
from sympy.abc import x
sym.diff(sym.poly(x**2 +2*x +3), x)
```

컴퓨터로 계산할 때 미분이 정확히 0이 되는 것은 불가능하므로 eps보다 작을 때 종료하는 조건이 필요

```python
while(abs(grad) > eps):
```

## 변수가 벡터일 경우

벡터가 입력인 다변수 함수인 경우 <span class="blindfold" data-hint="">편미분(partial differentiation)</span>을 사용

각 변수 별로 편미분을 계산한 그래디언트(gradient) 벡터를 이용하여 경사하강/ 경사상승법에 사용할 수 있다
