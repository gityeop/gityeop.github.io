---
title: 텐서 연산, 비교 개념 정리
date: 2024-08-07
categories: machine-learning
---

### 텐서 연산 및 비교 개념 정리

#### 텐서 연결 (Tensor Concatenation)

1. **텐서 연결**:

   - `torch.cat` 함수를 사용하여 텐서를 지정된 차원(axis) 방향으로 연결합니다.
   - 예시:
     ```python
     a = torch.tensor([[1, 2], [3, 4]])
     b = torch.tensor([[5, 6], [7, 8]])
     result = torch.cat((a, b), dim=0)
     # 출력:
     # tensor([[1, 2],
     #         [3, 4],
     #         [5, 6],
     #         [7, 8]])
     ```

2. **오류와 해결 방법**:
   - 동일한 두 텐서를 서로 다른 차원으로 연결하려고 할 때, 차원이 일치하지 않으면 오류가 발생합니다.
   - 예시:
     ```python
     a = torch.tensor([[1, 2], [3, 4]])
     b = torch.tensor([[5, 6]])
     # 오류 발생: RuntimeError: Sizes of tensors must match except in dimension 1. Got 2 and 1 in dimension 0
     b = torch.tensor([[5], [6]])
     result = torch.cat((a, b), dim=1)
     # 출력:
     # tensor([[1, 2, 5],
     #         [3, 4, 6]])
     ```

#### 텐서 확장 (Tensor Expansion)

1. **텐서 확장**:

   - `torch.expand` 메소드를 사용하여 텐서를 지정된 크기로 확장합니다. 주의할 점은 확장된 텐서는 원본 데이터를 공유합니다.
   - 예시:
     ```python
     f = torch.tensor([[1, 2, 3]])
     f_expanded = f.expand(4, 3)
     # 출력:
     # tensor([[1, 2, 3],
     #         [1, 2, 3],
     #         [1, 2, 3],
     #         [1, 2, 3]])
     ```

2. **반복**:
   - `torch.repeat` 메소드를 사용하여 텐서를 지정된 횟수만큼 반복합니다.
   - 예시:
     ```python
     h = torch.tensor([[1, 2], [3, 4]])
     h_repeated = h.repeat(2, 3)
     # 출력:
     # tensor([[1, 2, 1, 2, 1, 2],
     #         [3, 4, 3, 4, 3, 4],
     #         [1, 2, 1, 2, 1, 2],
     #         [3, 4, 3, 4, 3, 4]])
     ```

#### 텐서 산술 연산 (Tensor Arithmetic Operations)

1. **요소별 연산**:

   - `torch.add`, `torch.sub`, `torch.mul`, `torch.div` 등의 함수를 사용하여 요소별 연산을 수행할 수 있습니다.
   - 예시:
     ```python
     A = torch.tensor([[1, 2], [3, 4]])
     B = torch.tensor([[5, 6], [7, 8]])
     result = torch.add(A, B)
     # 출력:
     # tensor([[ 6,  8],
     #         [10, 12]])
     ```

2. **인플레이스 연산**:

   - 인플레이스 계산은 기존 텐서의 메모리를 재사용하여 계산 결과를 직접 저장하는 방법입니다.
   - `A.add_(B)`와 같은 인플레이스 연산을 사용하면 텐서 `A`의 값이 변경되며, `A`와 `B`의 요소별 덧셈 결과가 `A`에 저장됩니다.

   - 예시:
     ```python
     A = torch.tensor([[1, 2], [3, 4]])
     B = torch.tensor([[5, 6], [7, 8]])
     A.add_(B)
     print(A)
     # 출력:
     # tensor([[ 6,  8],
     #         [10, 12]])
     ```

3. **브로드캐스팅**:
   - 크기가 다른 텐서들 간의 연산 시 자동으로 작은 텐서를 큰 텐서의 크기로 확장하여 연산합니다.
   - 예시:
     ```python
     C = torch.tensor([[1, 2], [3, 4]])
     D = torch.tensor([5, 6])
     result = C + D
     # 출력:
     # tensor([[ 6,  8],
     #         [ 8, 10]])
     # 설명: 1차원 텐서 D가 자동으로 확장되어 2차원 텐서 C와 연산됩니다.
     ```

#### 텐서 비교 연산 (Tensor Comparison Operations)

1. **요소 비교**:

   - PyTorch에서 제공하는 비교 연산 함수들은 두 텐서의 요소들을 비교하고, 그 결과를 동일한 크기의 텐서로 반환합니다. 각 함수는 다음과 같은 역할을 합니다:

- `torch.eq` (==): 두 텐서의 요소들이 같은지 비교합니다.

  ```python
  result = torch.eq(v, w)
  # v와 w가 같은 위치에 있는 요소들이 같으면 True, 다르면 False를 반환
  ```

- `torch.ne` (!=): 두 텐서의 요소들이 다른지 비교합니다.

  ```python
  result = torch.ne(v, w)
  # v와 w가 같은 위치에 있는 요소들이 다르면 True, 같으면 False를 반환
  ```

- `torch.gt` (>): 첫 번째 텐서의 요소가 두 번째 텐서의 요소보다 큰지 비교합니다.

  ```python
  result = torch.gt(v, w)
  # v의 요소가 w의 요소보다 크면 True, 그렇지 않으면 False를 반환
  ```

- `torch.lt` (<): 첫 번째 텐서의 요소가 두 번째 텐서의 요소보다 작은지 비교합니다.

  ```python
  result = torch.lt(v, w)
  # v의 요소가 w의 요소보다 작으면 True, 그렇지 않으면 False를 반환
  ```

- `torch.ge` (>=): 첫 번째 텐서의 요소가 두 번째 텐서의 요소보다 크거나 같은지 비교합니다.

  ```python
  result = torch.ge(v, w)
  # v의 요소가 w의 요소보다 크거나 같으면 True, 그렇지 않으면 False를 반환
  ```

- `torch.le` (<=): 첫 번째 텐서의 요소가 두 번째 텐서의 요소보다 작거나 같은지 비교합니다.
  ```python
  result = torch.le(v, w)
  # v의 요소가 w의 요소보다 작거나 같으면 True, 그렇지 않으면 False를 반환
  ```

#### 텐서 논리 연산 (Tensor Logical Operations)

1. **논리 연산**:

### 3. 논리 연산

- PyTorch에서는 논리 연산을 수행하는 함수도 제공됩니다. 주요 논리 연산 함수는 다음과 같습니다:

- `torch.logical_and`: 두 텐서의 요소별 논리곱 (AND) 연산을 수행합니다.

  ```python
  x = torch.tensor([True, False, True, False])
  y = torch.tensor([True, True, False, False])
  result = torch.logical_and(x, y)
  # 출력: tensor([True, False, False, False])
  ```

- `torch.logical_or`: 두 텐서의 요소별 논리합 (OR) 연산을 수행합니다.

  ```python
  result = torch.logical_or(x, y)
  # 출력: tensor([True, True, True, False])
  ```

- `torch.logical_xor`: 두 텐서의 요소별 베타적 논리합 (XOR) 연산을 수행합니다.
  ```python
  result = torch.logical_xor(x, y)
  # 출력: tensor([False, True, True, False])
  ```

이 외에도 PyTorch에서는 다음과 같은 논리 연산을 제공합니다:

- `torch.logical_not`: 텐서의 각 요소에 대해 논리 부정 (NOT) 연산을 수행합니다.
  ```python
  result = torch.logical_not(x)
  # 출력: tensor([False, True, False, True])
  ```

#### 텐서의 복합 연산 (Complex Tensor Operations)

1. **요소별 연산**:

   - 두 텐서의 요소별로 여러 연산을 순차적으로 수행합니다.
   - 예시:
     ```python
     E = torch.tensor([[1, 2], [3, 4]])
     F = torch.tensor([[5, 6], [7, 8]])
     add_result = E + F
     sub_result = E - F
     mul_result = E * F
     div_result = E / F
     # 출력:
     # add_result: tensor([[ 6,  8],
     #                     [10, 12]])
     # sub_result: tensor([[-4, -4],
     #                     [-4, -4]])
     # mul_result: tensor([[ 5, 12],
     #                     [21, 32]])
     # div_result: tensor([[0.2000, 0.3333],
     #                     [0.4286, 0.5000]])
     ```

2. **제곱과 제곱근**:
   - `torch.pow`, `torch.sqrt` 등의 함수를 사용하여 제곱 및 제곱근 연산을 수행합니다.
   - 예시:
     ```python
     G = torch.tensor([[1, 2], [3, 4]])
     H = torch.tensor([[2, 2], [2, 2]])
     pow_result = torch.pow(G, H)
     sqrt_result = torch.sqrt(G.float())
     # 출력:
     # pow_result: tensor([[ 1,  4],
     #                     [ 9, 16]])
     # sqrt_result: tensor([[1.0000, 1.4142],
     #                      [1.7321, 2.0000]])
     ```

> 참고) 행렬 생성
> `torch.twos_like` 명령어는 존재하지 않지만, `torch.full_like`를 사용하여 동일한 크기의 텐서를 원하는 값으로 채울 수 있습니다.
> 예시:

```python
H = torch.tensor([[2, 2], [2, 2]])
# 동일한 크기의 행렬을 2로 채우기
H_like = torch.full_like(H, 2)
print(H_like)
# 출력:
# tensor([[2, 2],
#         [2, 2]])
```

#### 텐서의 실제 문제 적용 (Real-world Tensor Applications)

1. **3차원 텐서 연결**:

   - 3차원 텐서를 연결할 때 크기를 맞추어야 합니다.
   - 예시:
     ```python
     M = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
     N = torch.tensor([[[9, 10]], [[11, 12]]])
     N = N.expand(2, 2, 2)
     result = torch.cat((M, N), dim=1)
     # 출력:
     # tensor([[[ 1,  2],
     #          [ 3,  4],
     #          [ 9, 10]],
     #
     #         [[ 5,  6],
     #          [ 7,  8],
     #          [11, 12]]])
     ```

2. **인플레이스 연산**:
   - 메모리를 절약하기 위해 인플레이스 연산을 사용

합니다.

- 예시:
  ```python
  P = torch.tensor([[1, 2], [3, 4]])
  Q = torch.tensor([[5, 6], [7, 8]])
  P.add_(Q)
  # 출력:
  # tensor([[ 6,  8],
  #         [10, 12]])
  ```

---

### 추가 제안

**Suggestion 1**: 인플레이스 연산의 메모리 관리 이점과 사용 시 주의사항을 연구해 보세요.

**Suggestion 2**: 텐서 연산의 효율성을 높이기 위한 다양한 최적화 기법들을 실험해 보세요.

**Suggestion 3**: 다양한 논리 연산을 활용한 복잡한 조건문을 텐서 연산으로 구현해 보세요.
