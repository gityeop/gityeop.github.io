---
title: 경사하강법 매운 맛 Gradient Descent(Spicy)
date: 2024-08-06
categories: math-for-ml
---

### 1. 경사하강법의 기본 개념

경사하강법은 주어진 목적함수를 최소화하는 최적화 알고리즘이다. 선형 회귀 분석에서는 데이터의 변수와 모델을 나타내는 선형 모델을 찾기 위해 경사하강법을 사용한다. 다음은 경사하강법의 기본 수식이다.

```python
def gradient_descent(X, y, learning_rate, num_iterations):
    beta = np.zeros(X.shape[1])
    for i in range(num_iterations):
        gradient = -2 * X.T.dot(y - X.dot(beta)) / len(y)
        beta -= learning_rate * gradient
    return beta
```

### 2. 무어-펜로즈 역행렬과 경사하강법의 차이

무어-펜로즈 역행렬을 사용하여 선형 모델을 찾을 수 있다. 그러나 경사하강법은 더 일반적인 기계학습 모형에서 최적화를 가능하게 하며 비선형 모델에서도 적용가능하다.

### 3. 목적식의 최소화

선형 회귀에서의 목적식은 다음과 같이 표현된다:

$$
L(\beta) = \frac{1}{n} \sum_{i=1}^n (y_i - \mathbf{x}_i^T \beta)^2
$$

$$
\nabla L(\beta) = -\frac{2}{n} \sum_{i=1}^n \mathbf{x}_i (y_i - \mathbf{x}_i^T \beta)
$$

이 목적식을 최소화하기 위해 경사하강법을 사용한다. 주어진 목적식에 대해 편미분을 수행하여 그래디언트 벡터를 계산하고, 이를 통해 $\beta$를 업데이트한다.

```python
def compute_gradient(X, y, beta):
    return -2 * X.T.dot(y - X.dot(beta)) / len(y)
```

### 4. 학습률과 학습 횟수의 중요성

학습률(learning rate)과 학습 횟수(num_iterations)는 경사하강법의 수렴 속도와 정확성에 큰 영향을 미친다. 학습률이 너무 크면 발산할 수 있고, 너무 작으면 수렴 속도가 느려진다. 적절한 학습 횟수를 선택해야 경사하강법이 최적의 해를 찾을 수 있다.

### 5. 확률적 경사하강법 (SGD)

확률적 경사하강법은 모든 데이터를 사용하지 않고, 일부 데이터를 샘플링하여 그래디언트를 계산한다. 이를 통해 연산량을 줄이고, 더 빠르게 수렴할 수 있다. 미니배치(mini-batch) SGD는 데이터 일부를 사용하여 그래디언트를 계산하고 업데이트하는 방식이다.
