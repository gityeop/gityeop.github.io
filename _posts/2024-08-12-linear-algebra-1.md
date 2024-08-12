## 선형대수-1(Regression & NN Classifier)

Regression이란?
회귀 : 과거의 상태로 돌아가는 것
부모와 자녀의 키 사이에 선형적 관계가 있고, 키가 커지거나 작아지는 것보다는 전체 키 평균(부모의 키 평균)으로 **돌아가려는 경향**이 있다는 가설을 세움

회귀 분석(regression analysis)
: 관찰된 연속형 변수들에 대해 두 변수 사이의 모형을 구한 뒤 적합도를 측정하는 분석 방법

변수: 변하는 수, 값이 변하는 데이터 요소 또는 속성
독립변수(설명변수): 결과의 원인(x)
종속변수(응답변수): 독립변수에 따라 값이 달라짐(y)

Linear Regression
: 선형 회귀는 종속 변수와 하나 이상의 독립 변수간의 관계를 모델링하는 통계적 방법
-> 독립변수의 값을 기반으로 종속 변수의 값을 예측하기 위함
예시
집값과 집 크기 간의 상관관계를 나타낸 산점도

$$
y = mx +b
$$

y: 종속 변수(목표)
m: 직선의 기울기(회귀 계수)
x: 독립 변수(예측 변수)
b: y 절편(상수항)

---

1. 상관 계수 (Correlation Coefficient, r)

상관 계수 $r$ 은 두 변수 $X$ 와 $Y$ 간의 선형 관계의 강도와 방향을 나타냅니다. 상관 계수는 다음과 같이 정의됩니다:

$$
r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

여기서:

    •	$\text{Cov}(X, Y)$는  $X$ 와  $Y$ 의 공분산을 의미하며, 두 변수 간의 공통된 변동성을 나타냅니다.
    •	$\sigma_X$는  $X$ 의 표준 편차, $\sigma_Y$는  $Y$ 의 표준 편차입니다.

공분산 $\text{Cov}(X, Y)$는 다음과 같이 계산됩니다:

$$
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
$$

---

### Linear Regression의 가정

- 선형성: 종속 변수와 독립 변수 간의 관계가 선형적이어야 함
- 독립성: 관측값들은 서로 독립적이어야 함
  - 잔차들이 무작위로 분포되어 있어야 함. 시간의 흐름에 따라 잔차가 특정 패턴을 보이면 독립성 가정이 위배됨(관측값이 시간의 영향을 받지 않아야 함, 이전의 값이 나중의 값에 영향을 주면 안됨)
  - 시간의 흐름에 관측값이 영향을 받는다면 시계열 분석을 고려
- 등분산성: 오류의 분산이 일정해야 함
  - 잔차들이 일정한 분포를 보여야 함. 특정 구간에서 잔차의 분산이 커지거나 작아지면 등분산성 가정이 위배됨
  - 어느 정도로 모델이 예측에서 일관성을 유지하는지, 모델이 특정 영역에 치우치지 않고 전반적으로 안정적이고 일관된 예측을 제공하고 있다는 신호
- 정규성: 오류가 정규 분포를 따름
  - 잔차들이 정규 분포를 따를 경우, 점들이 대각선에 가깝게 위치함
  - 잔차의 대부분이 0에 가까워야 하고, 극단적인 오차(잔차)는 매우 드물어야 합니다.
  - 잔차가 정규 분포를 따를 경우, 회귀 분석의 통계적 테스트(예: t-검정, F-검정)가 올바르게 작동합니다.
    잔차 residual: 오차의 추정치

최소 제곱법(OLS) 방법

$$
Cost(m, b) = \sum(y_i - (mx_i+b_i))^2
$$

실제값과 예측값의 차이의 제곱합을 최소화하는 매개변수 m과 b를 추정하는 방법

다중 선형 회귀
여러 독립 변수를 포함하도록 선형 회귀를 확장한 것

$$
y = b_0+b_1x_1+b_2x_2+...+b_nx_n
$$

예시
집 크기, 침실 수 -> 집값 간의 관계를 나타낸 경우

### 모델 평가 지표

1. 평균 절대 오차(MAE)

   $$
   MAE =  \frac{1}{n}\sum_{i=1}^n|y_i-\hat y_i|
   $$

   예측 값과 실제 값이 얼마나 차이나는지 절대값으로 계산해 평균화한 지표

2. 평균 제곱 오차(MSE)
   $$
   MSE = \frac{1}{n}\sum_{i=1}^n(y_i-\hat y_i)^2
   $$
   큰 오차에 더 큰 패널티를 부여
   큰 오차에 민감하게 반응하므로, 모델의 큰 오차를 줄이는 데 유용

### Nearest Neighbor Classifier

쿼리(테스트) 데이터 포인트에 대해 가장 가까운 (k개의) 학습 데이터 포인트를 (k)개 찾고, 레이블을 사용하여 예측

- 가장 가까운 데이터 포인트의 레이블의 다수결로 테스트 데이터 포인트의 레이블이 결정됨

```python
def train(images, labels):
  # some machine learning
  # 모델 데이터와 라벨을 기억함
  return model

def predict(model, image):
  # use the model
  # 가장 유사한 훈련 예제의 라벨을 출력함
  return predicted_label
```

Nearest Neighbor의 문제점
"유사한 이미지"라는 정의를 어떻게 할 것인가?
두 이미지 간의 유사도(또는 거리) 메트릭이 필요

두 행렬(이미지) 사이의 거리 메트릭을 사용

L1 거리: 절대적 차이
$$L1(A, B) = \sum_{ij} |A_{ij}- B_{ij}|$$

L2 거리: 차이의 크기
$$L2(A,B)= \sqrt{\sum_{ij}(A_{ij}-B_{ij})^2}$$

```python
import numpy as np

class NearestNeighbor:
  def __init__(self):
    pass

  def train(self, images, labels):
    self.images = images
    self.labels = labels

  def predict(self, test_image):
    min_dist = sys.maxint
    for i in range(self.images.shape[0]):
      dist = np.sum(np.abs(self.images[i, :] - test_image))
      if dist < min_dist:
        min_dist = dist
        min_index = i
    return self.labels[min_index]
```

이 알고리즘의 시간 복잡도
훈련시 O(1)
예측시 O(N)
-> 우리는 훈련 시간이 오래 걸려도 예측이 빠른 알고리즘을 원함

**결정 바운더리**

k-Nearest Neighbor Classifier
가장 가까운 하나의 이웃 라벨 대신 가장 가까운 k개 지점에서 과반수 득표

Nearest Neighbor Classifier Issues

- 픽셀 거리에는 k-nearest neighbor가 사용되지 않는다
  - 픽셀의 거리 메트릭은 semantic 정보를 제공하지 않는다
  - 테스트 시 매우 느리다
- Curse of Dimensionality
  - 고차원 데이터의 경우 기하급수적으로 증가하는 예제 수가 필요

Linear Classifier
Softmax Classifier
