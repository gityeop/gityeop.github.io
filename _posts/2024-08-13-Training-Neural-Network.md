## Activation Functions, Weight Initialization, Learning Rate Scheduling

### Activation Functions

1. Sigmoid Function

- 특징
  출력 값의 범위: (0, 1)
- 단점
  - Vanishing Gradient: input의 크기가 크거나 작을 때 기울기가 0에 가까워짐
    - Upstream Gradient가 0이면 Downstream Gradient도 0임
    - 트레이닝이 안됨
  - 출력 값들이 zero-centered하지 않음
  - exp()의 연산이 비쌈
    Derivative of Sigmoid function
    $$
    \frac{\partial \sigma(x)}{\partial x} = \sigma(x) \left(1 - \sigma(x)\right)
    $$
  - $\sigma(x)$ 값이 1이거나 0이면(크거나 작으면) gradient가 0이 됨
- Non Zero-centered Output
  $$
  \frac{\partial \sigma}{\partial w_i} = \sigma(\mathbf{w}^{\top} \mathbf{x} + b) \left(1 - \sigma(\mathbf{w}^{\top} \mathbf{x} + b)\right) x_i
  $$
  - 입력 x가 모두 다 양수라고 가정한다면, 출력 값의 범위가 항상 [0.5, 1]
  - 중심이 0이 아닌 0.5
  - 모든 w에 대한 upstream gradient의 부호가 변하지 않는다.
  - 모든 gradient들은 모두 양수이거나 모두 음수이다
  - gradient가 특정 방향으로만 업데이트 된다
  - 우상향, 좌하향 방향키로 우하향, 좌상향으로 이동해보기
