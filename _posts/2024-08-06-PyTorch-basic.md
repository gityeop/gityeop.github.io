---
title: "PyTorch Basic"
excerpt: "파이토치 기초"
tags: ["pytorch", "deep-learning"]
date: 2024-08-06
categories: machine-learning
---

## PyTorch

1. 간편한 딥러닝 API[^1] 제공
2. 머신러닝 알고리즘을 구현, 실행하기 위한 확장성이 뛰어난 Multi-platform Interface

### PyTorch Architecture

![Image](https://i.imgur.com/2sAM6Yy.png)

- users -> Top-level API (torch, torch.autograd(자동미분), torch.nn(layer, loss), torch.multiprocessing(병렬 처리), torch.utils(데이터로딩, 모델 저장))
- Python API
  - Autograd C++, ATen C++, JIT (Just in Time 동적 컴파일러)
    - 성능 최적화, 연산 효율
  - Low-level Library
    - TH C(텐서 연산), THC CUDA(GPU 텐서 연산), THNN C(신경망 연산), THCUNN CUDA(GPU 신경망 연산)
    - GPU 최적화 컴파일러

---

## What is Tensor?

## 1. 0-D Tensor: Scalar

- 언어적: 하나의 숫자로 표현되는 양
- 대수적: a = a1, a ∈ ℝ
- 코드

a = <span class="blindfold" data-hint="">torch.tensor</span>(365)

## 2.1 1-D Tensor: Vector

- 언어적: 수치가 치열 여러개의 숫자로 이루어진 것
- 대수적: b = [b1, b2, ..., bn], b ∈ ℝ^n
- 코드

```python
b = torch.tensor([175, 60, 81, 0.8, 0.9])
```

## 3. 2-D Tensor: Matrix

- 언어적: 동일한 크기를 가진 1차원 Tensor들이 모여 행과 열로 구성한 구조
- 대수적: c = [[97, 114, 140, 191], [39, ..., ..., 1]], c ∈ ℝ^(m\*n)
- 코드

```python
c = torch.tensor([[97, 114, 140, 191], [39, 45, 78, 1]])
```

## 4. 3-D Tensor

- 언어적: 2-D Tensor들이 쌓여서 형성된 입체적 배열 구조
- 코드

```python
d = torch.tensor([[[255,0,0],[0,255,0]], [[0,0,255],[255,255,0]]])
torch.stack([red, green, blue], dim=2)
```

---

## PyTorch 데이터 타입

### dtype: 데이터 유형

#### 정수형

|        | 8        | 16           | 32                     | 64                                       |
| ------ | -------- | ------------ | ---------------------- | ---------------------------------------- |
| 양수 x | 0~255    | 0~65535      | 0~4294967295           | 0~18446744073709551615                   |
| 음수 0 | -128~127 | -32768~32767 | -2147483648~2147483647 | -9223372036854775808~9223372036854775807 |

### 부호 X, 8비트

1. 연속적 범위: 0~255
2. 강제적: 12 = 0 0 0 0 1 1 0 0
3. 예: dtype = torch.<span class="blindfold" data-hint="">uint8</span>, a = `torch.tensor([1], dtype=torch.uint8)`

### 부호 O, 8비트

1. -128~127, 1비트는 부호에 불림
2. -12 = 1 0 0 0 1 1 0 0
   - 양수: 00000000 (0)부터 01111111 (127)까지 128개의 숫자 표현
   - 음수: 10000000 (-128)부터 11111111 (-1)까지
3. dtype = `torch.int8`

### 부호 O, 16비트

1. -32,768 ~ 32,767
2. dtype = `torch.int16` 또는 torch.<span class="blindfold" data-hint="">short</span>

### 부호 O, 32비트

1. 표준적인 정수 크기
2. dtype = `torch.int32` 또는 `torch.int`

### 부호 O, 64비트

1. dtype = torch.int64 또는 torch.<span class="blindfold" data-hint="">long</span>

> 2의 보수 표현법
>
> 1. 양수는 그대로 표현
> 2. 음수는 절대 값에 대한 2의 보수 형태로 표현
>
> - 예: -5 = 0000 0101(1의 보수) -> 1111 1010 (2의 보수)

> ### 언제 비트를 줄여서 사용하는가?
>
> 1. 16비트: 메모리가 제한적인 환경, 정밀도가 낮아도 되는 경우
> 2. 32비트: 일반적인 경우 (메모리 사용량 <span class="blindfold" data-hint="">4</span>바이트)
> 3. 64비트: 매우 큰 값, 높은 정밀도(메모리 사용량 <span class="blindfold" data-hint="">8</span>바이트)
>    **일종의 해상도**

---

## 고정 소수점

### 16비트 고정 소수점

1. 언어적: 비트를 사용해서 정수부와 소수부로 표현하는 데이터 형식
2. 예: 102.5 -> **0**1100110**00000101**
   - 부호 1비트, 정수부 7비트, 소수부 8비트

Q. 102.005는 어떻게 저장해야 할까?

고정 소수점으로 표현하면 0001 0000 0010 . 0000 0000 0101

- 24비트가 필요함
- 메모리 부족

## 부동 소수점

### 32비트 부동 소수점 수

- 32비트로 숫자를 정규화하여 가수부, 지수부로 나누어 표현하는 방식
- 예: 102.5 = 1.025 x 10^2
- 부호 1bit, 지수부 8bit, 가수부 23bit
- dtype = `torch.float32` 또는 `torch.float`

### 64비트 부동소수점 수

- 1비트 부호, 11비트 지수부, 52비트 가수부
- dtype = torch.float64 또는 torch.<span class="blindfold" data-hint="">double</span>

---

## Typecasting

- 메모리 부하를 줄이기 위해 데이터 타입 변경

```python
i = torch.tensor([2, 3, 4], dtype=torch.int8)
j = i.float()
k = i.double()
```

j: <span class="blindfold" data-hint="">32</span>비트 부동소수점으로 타입 캐스팅

k: <span class="blindfold" data-hint="">64</span>비트 부동소수점으로 타입 캐스팅

## Tensor 기본 함수 및 메서드

1. <span style="color: #FF4500;">min, max, sum, prod, mean, var, std</span>
   - torch.<span style="color: #FF4500;">method</span>(<span style="color: #4169E1;">parameter</span>)
   - <span style="color: #4169E1;">tensorobject</span>.<span style="color: #FF4500;">method()</span>
   - `torch.min(a)`
   - `a.min()`

## Tensor 특성 관련 메서드

1. dim(), size(), shape, numel()
   - <span style="color: #4169E1;">tensorobject</span>.<span style="color: #FF4500;">method()</span>
   - `a.size()`
   - `a.shape`

---

## Manipulation of Tensors

### 1. Tensor의 indexing & slicing

- indexing: Tensor의 특정 <span class="blindfold" data-hint="">위치의 값</span>을 접근하는 것
- slicing: <span class="blindfold" data-hint="">부분집합</span> 선택하여 새로운 Sub Tensor 생성하는 과정
- 예:
  ```python
  a = torch.tensor([10, 20, 30, 40, 50, 60])
  a[0]  # 10
  a[3]  # 40
  ```

### 2-D Tensor의 indexing 예제

```python
b = torch.tensor([[10, 20, 30], [40, 50, 60]])
b[0, 0]  # tensor(10)
b[1, 2], b[1, -1]  # tensor(60)
```

### 2-D Tensor의 slicing 예제

```python
b[0, 1:], b[0, :2]  # tensor([20, 30]), tensor([10, 20])
b[1, ...] 또는 b[1, :] 또는 b[1, :-1]  # tensor([40, 50, 60])
a[:5:2] # tensor([10, 30, 50])
```

### Tensor의 view를 활용한 모양변경

- `view()` 메서드를 활용한 모양변경

  - Tensor의 메모리가 <span class="blindfold" data-hint="">연속으로</span> 할당된 경우에 사용 가능
    - 메모리 주소가 <span class="blindfold" data-hint="">등차수열</span>을 이루는 경우에는 슬라이싱 후에도 view가 가능

  ```python
  c = torch.tensor([[0, 1, 2], [3, 4, 5]])
  d = c[:, :2]
  # tensor([[0, 1],
  #         [3, 4]]) contiguous 속성이 깨짐
  s = c[:, :1]

  #tensor([[1],
  #        [3],
  #        [5]]) # 메모리 연속성이 유지됨(view 가능)
  ```

### contiguous 확인 메서드

```python
d.is_contiguous()
# False
```

d_contiguous = d.<span class="blindfold" data-hint="">contiguous</span>() # 연속적으로 할당 가능

---

### Tensor의 reshaping 예제

- `reshape()` 메서드를 활용한 모양 변경
  - 장점
    - 메모리가 연속적이지 않아도 사용가능
    - 안전하고 유연성이 좋음
  - 단점
    - 성능 저하의 단점
  - 예시:
    ```python
    n = torch.arange(12)
    o = n.reshape((4, 3)) 또는 n.reshape((3, 4))
    ```

### Transpose

- 두 차원의 축을 서로 바꾸는 메서드
  ```python
  m = o.transpose(0, 1) # 0과 1차원의 축을 바꿈
  m = o.transpose(1, 2) # 1과 2차원의 축을 바꿈
  ```

### squeeze()

- dim = 1인 특정 차원은 축소

  ```python
  u = torch.rand(1, 3, 4)
  v = torch.squeeze(u)  # tensor[(3, 4)]
  w = torch.randn(1, 1, 4)
  x = torch.squeeze(w) # tensor(4)
  x = torch.squeeze(w, dim = 0) # tensor[(1, 4)]
  t = torch.randn(1, 2, 3, 1)
  t_squeezed = torch.squeeze(t)
  ```

  > tensor[<span class="blindfold" data-hint="">(2, 3)</span>]

### unsqueeze()

- dim = 1 특정 차원 확장

  ```python
  y = torch.rand(3, 4)
  z = torch.unsqueeze(y, dim=0)  # torch.Size([1, 3, 4])
  z = torch.unsqueeze(y, dim=2)
  ```

  torch.Size(<span class="blindfold" data-hint="">[3, 4, 1]</span>)

### stack()

- Tensor들의 결합

  ```python
  r = torch.tensor([[255, 0], [0, 255]])
  g = torch.tensor([[0, 255], [0, 255]])
  b = torch.tensor([[0, 0], [255, 0]])
  a = torch.stack((r, g, b))
  a = torch.stack((r, g, b), dim = 1)
  a = torch.stack((r, g, b), dim = 2)
  ```

  tensor.size[<span class="blindfold" data-hint="">(3, 2, 2)</span>]

  tensor.size[<span class="blindfold" data-hint="">(2, 3, 2)</span>]

  tensor.size[<span class="blindfold" data-hint="">(2, 2, 3)</span>]

  ![Image](https://i.imgur.com/NBmPhmf.png)

---

[^1] API(Application Programming Interface)

- 응용 프로그램에서 서로 상호작용하는 데 사용하는 명령어, 함수, 프로토콜의 집합
