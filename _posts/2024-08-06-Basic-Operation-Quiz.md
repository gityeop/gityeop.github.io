---
title: Basic Operation Quiz
date: 2024-08-06
categories: machine-learning
---

### 문제집: 텐서 연산 및 비교

#### 기본 개념 확인 문제

**문제 1: 텐서 연결**

1. 두 텐서 `a`와 `b`를 디멘전 제로 방향으로 연결하는 코드를 작성하세요.

<span class="blindfold" data-hint="">a = torch.tensor([[1,2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
result = torch.cat((a, b), dim = 0)
</span>

2. 동일한 두 텐서를 디멘전 원 방향으로 연결하려고 할 때 발생하는 오류의 원인을 설명하고, 이 오류를 해결하는 코드를 작성하세요.

**문제 2: 텐서 확장**

1. 1행 3열의 텐서 `f`를 4행 3열로 확장하는 코드를 작성하세요.
2. `repeat` 메소드를 사용하여 2행 2열의 텐서 `h`를 디멘전 0방향으로 2번, 디멘전 1방향으로 3번 반복하는 코드를 작성하세요.

#### 중급 응용 문제

**문제 3: 텐서 산술 연산**

1. 2행 2열의 텐서 `A`와 `B`를 생성하고, 두 텐서의 요소별 더하기 연산을 수행하는 코드를 작성하세요.
2. 동일한 텐서 `A`와 `B`에 대해 인플레이스 방식으로 더하기 연산을 수행하는 코드를 작성하세요.
3. 크기가 다른 두 텐서 `C`(2행 2열)와 `D`(1행 2열)를 더하는 코드를 작성하세요. 이때 자동 확장이 어떻게 이루어지는지 설명하세요.

**문제 4: 텐서 비교 연산**

1. 두 텐서 `v`(1, 3, 5, 7)와 `w`(2, 3, 5, 7)를 생성하고, 두 텐서의 요소들이 같은지를 비교하는 코드를 작성하세요.
2. 동일한 텐서 `v`와 `w`에 대해 각 요소들이 다른지를 비교하는 코드를 작성하세요.
3. 텐서 `v`의 요소들이 텐서 `w`의 요소들보다 큰지를 비교하는 코드를 작성하세요.

**문제 5: 텐서 논리 연산**

1. 두 텐서 `x`(1, 0, 1, 0)와 `y`(1, 1, 0, 0)를 생성하고, 논리곱 연산을 수행하는 코드를 작성하세요.
2. 동일한 텐서 `x`와 `y`에 대해 논리합 연산을 수행하는 코드를 작성하세요.
3. 베타적 논리합 연산을 수행하는 코드를 작성하세요.

#### 고급 응용 문제

**문제 6: 텐서의 복합 연산**

1. 2행 2열의 텐서 `E`와 `F`를 생성하고, 두 텐서의 요소별 더하기, 빼기, 곱하기, 나누기 연산을 순서대로 수행하는 코드를 작성하세요.
2. 텐서 `G`와 `H`를 생성하고, 두 텐서의 요소별 제곱과 제곱근을 구하는 코드를 작성하세요.

**문제 7: 텐서의 실제 문제 적용**

1. 3차원 텐서 `M`과 `N`을 생성하고, 두 텐서를 디멘전 1 방향으로 연결하는 코드를 작성하세요. 이때 두 텐서의 크기를 미리 조정해야 한다면 어떻게 조정해야 하는지 설명하세요.
2. 텐서 `P`와 `Q`를 사용하여 주어진 크기 제약 조건 내에서 최대한 메모리를 절약하는 방식으로 인플레이스 연산을 사용하는 코드를 작성하세요.

---

### 정답 및 풀이

#### 기본 개념 확인 문제

**문제 1: 텐서 연결**

1.

```python
import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

result = torch.cat((a, b), dim=0)
print(result)
# 출력:
# tensor([[1, 2],
#         [3, 4],
#         [5, 6],
#         [7, 8]])
```

2.

```python
# 오류 설명: 두 텐서의 크기가 다를 때 발생
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6]])

try:
    result = torch.cat((a, b), dim=1)
except RuntimeError as e:
    print(e)
# 출력:
# RuntimeError: Sizes of tensors must match except in dimension 1. Got 2 and 1 in dimension 0

# 오류 해결 방법: 텐서 b의 크기를 조정
b = torch.tensor([[5], [6]])
result = torch.cat((a, b), dim=1)
print(result)
# 출력:
# tensor([[1, 2, 5],
#         [3, 4, 6]])
```

**문제 2: 텐서 확장**

1.

```python
f = torch.tensor([[1, 2, 3]])
f_expanded = f.expand(4, 3)
print(f_expanded)
# 출력:
# tensor([[1, 2, 3],
#         [1, 2, 3],
#         [1, 2, 3],
#         [1, 2, 3]])
```

2.

```python
h = torch.tensor([[1, 2], [3, 4]])
h_repeated = h.repeat(2, 3)
print(h_repeated)
# 출력:
# tensor([[1, 2, 1, 2, 1, 2],
#         [3, 4, 3, 4, 3, 4],
#         [1, 2, 1, 2, 1, 2],
#         [3, 4, 3, 4, 3, 4]])
```

#### 중급 응용 문제

**문제 3: 텐서 산술 연산**

1.

```python
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])

result = torch.add(A, B)
print(result)
# 출력:
# tensor([[ 6,  8],
#         [10, 12]])
```

2.

```python
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])

A.add_(B)
print(A)
# 출력:
# tensor([[ 6,  8],
#         [10, 12]])
```

3.

```python
C = torch.tensor([[1, 2], [3, 4]])
D = torch.tensor([5, 6])

result = C + D
print(result)
# 출력:
# tensor([[ 6,  8],
#         [ 8, 10]])
# 설명: 1차원 텐서 D가 자동으로 확장되어 2차원 텐서 C와 연산됩니다.
```

**문제 4: 텐서 비교 연산**

1.

```python
v = torch.tensor([1, 3, 5, 7])
w = torch.tensor([2, 3, 5, 7])

result = torch.eq(v, w)
print(result)
# 출력:
# tensor([False,  True,  True,  True])
```

2.

```python
result = torch.ne(v, w)
print(result)
# 출력:
# tensor([ True, False, False, False])
```

3.

```python
result = torch.gt(v, w)
print(result)
# 출력:
# tensor([False, False, False, False])
```

**문제 5: 텐서 논리 연산**

1.

```python
x = torch.tensor([1, 0, 1, 0], dtype=torch.bool)
y = torch.tensor([1, 1, 0, 0], dtype=torch.bool)

result = torch.logical_and(x, y)
print(result)
# 출력:
# tensor([ True, False, False, False])
```

2.

```python
result = torch.logical_or(x, y)
print(result)
# 출력:
# tensor([ True,  True,  True, False])
```

3.

```python
result = torch.logical_xor(x, y)
print(result)
# 출력:
# tensor([False,  True,  True, False])
```

#### 고급 응용 문제

**문제 6: 텐서의 복합 연산**

1.

```python
E = torch.tensor([[1, 2], [3, 4]])
F = torch.tensor([[5, 6], [7, 8]])

add_result = E + F
sub_result = E - F
mul_result = E * F
div_result = E / F

print("Add:", add_result)
# 출력:
# Add: tensor([[ 6,  8],
#              [10, 12]])

print("Sub:", sub_result)
# 출력:
# Sub: tensor([[-4, -4],
#              [-4, -4]])

print("Mul:", mul_result)
# 출력:
# Mul

: tensor([[ 5, 12],
#              [21, 32]])

print("Div:", div_result)
# 출력:
# Div: tensor([[0.2000, 0.3333],
#              [0.4286, 0.5000]])
```

2.

```python
G = torch.tensor([[1, 2], [3, 4]])
H = torch.tensor([[2, 2], [2, 2]])

pow_result = torch.pow(G, H)
sqrt_result = torch.sqrt(G.float())  # sqrt requires float tensor

print("Power:", pow_result)
# 출력:
# Power: tensor([[ 1,  4],
#                [ 9, 16]])

print("Sqrt:", sqrt_result)
# 출력:
# Sqrt: tensor([[1.0000, 1.4142],
#               [1.7321, 2.0000]])
```

**문제 7: 텐서의 실제 문제 적용**

1.

```python
M = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
N = torch.tensor([[[9, 10]], [[11, 12]]])

# M의 크기와 맞추기 위해 N의 크기 조정
N = N.expand(2, 2, 2)

result = torch.cat((M, N), dim=1)
print(result)
# 출력:
# tensor([[[ 1,  2],
#          [ 3,  4],
#          [ 9, 10]],
#
#         [[ 5,  6],
#          [ 7,  8],
#          [11, 12]]])
```

2.

```python
P = torch.tensor([[1, 2], [3, 4]])
Q = torch.tensor([[5, 6], [7, 8]])

P.add_(Q)
print(P)
# 출력:
# tensor([[ 6,  8],
#         [10, 12]])
```
