---
title: Pandas의 reset_index의 inplace, drop에 대한 설명
date: 2024-07-29
categories: python-basic
tags: ["pandas", "data-analysis"]
---

`inplace`[^1]와 `drop`을 조합하여 `reset_index`를 적용하는 4가지 경우에 대해 예시를 통한 설명.
각 경우는 아래와 같다:

1. `inplace=True`와 `drop=True`
2. `inplace=True`와 `drop=False`
3. `inplace=False`와 `drop=True`
4. `inplace=False`와 `drop=False`

### 예시 데이터프레임 생성 및 인덱스 설정

```python
import pandas as pd

# 예시 데이터프레임 생성
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
df.index = ['a', 'b', 'c']

# 기존 데이터프레임 출력
print("Original DataFrame with custom index:")
print(df)
```

```plaintext
Original DataFrame with custom index:
   A  B
a  1  4
b  2  5
c  3  6
```

### 1. `inplace=True`와 `drop=True`

```python
# 원본 데이터프레임을 직접 수정하고 기존 인덱스를 삭제
df.reset_index(inplace=True, drop=True)

# 수정된 데이터프레임 출력
print("\nDataFrame after reset_index with inplace=True and drop=True:")
print(df)
```

```plaintext
DataFrame after reset_index with inplace=True and drop=True:
   A  B
0  1  4
1  2  5
2  3  6
```

- **설명**: 원본 데이터프레임이 **직접 수정**되며 기존 인덱스는 **삭제**.

### 2. `inplace=True`와 `drop=False`

```python
# 예시 데이터프레임 재생성 및 인덱스 설정
df = pd.DataFrame(data)
df.index = ['a', 'b', 'c']

# 원본 데이터프레임을 직접 수정하고 기존 인덱스를 열로 추가
df.reset_index(inplace=True, drop=False)

# 수정된 데이터프레임 출력
print("\nDataFrame after reset_index with inplace=True and drop=False:")
print(df)
```

```plaintext
DataFrame after reset_index with inplace=True and drop=False:
  index  A  B
0     a  1  4
1     b  2  5
2     c  3  6
```

- **설명**: 원본 데이터프레임이 **직접 수정**되며 기존 인덱스가 **새로운 열로 추가**.

### 3. `inplace=False`와 `drop=True`

```python
# 예시 데이터프레임 재생성 및 인덱스 설정
df = pd.DataFrame(data)
df.index = ['a', 'b', 'c']

# 인덱스를 재설정하고 기존 인덱스를 삭제, 새로운 데이터프레임에 저장
df_reset = df.reset_index(drop=True)

# 원본 데이터프레임 출력 (수정되지 않음)
print("\nOriginal DataFrame after reset_index with inplace=False and drop=True:")
print(df)

# 새로운 데이터프레임 출력 (수정됨)
print("\nNew DataFrame after reset_index with inplace=False and drop=True:")
print(df_reset)
```

```plaintext
Original DataFrame after reset_index with inplace=False and drop=True:
   A  B
a  1  4
b  2  5
c  3  6

New DataFrame after reset_index with inplace=False and drop=True:
   A  B
0  1  4
1  2  5
2  3  6
```

- **설명**: 원본 데이터프레임은 **그대로 유지**되며, 기존 인덱스가 삭제된 **새로운 데이터프레임이 생성**.

### 4. `inplace=False`와 `drop=False`

```python
# 예시 데이터프레임 재생성 및 인덱스 설정
df = pd.DataFrame(data)
df.index = ['a', 'b', 'c']

# 인덱스를 재설정하고 기존 인덱스를 열로 추가, 새로운 데이터프레임에 저장
df_reset = df.reset_index(drop=False)

# 원본 데이터프레임 출력 (수정되지 않음)
print("\nOriginal DataFrame after reset_index with inplace=False and drop=False:")
print(df)

# 새로운 데이터프레임 출력 (수정됨)
print("\nNew DataFrame after reset_index with inplace=False and drop=False:")
print(df_reset)
```

```plaintext
Original DataFrame after reset_index with inplace=False and drop=False:
   A  B
a  1  4
b  2  5
c  3  6

New DataFrame after reset_index with inplace=False and drop=False:
  index  A  B
0     a  1  4
1     b  2  5
2     c  3  6
```

- **설명**: 원본 데이터프레임은 **그대로 유지**되며, 기존 인덱스가 새로운 열로 추가된 **새로운 데이터프레임이 생성**.

### 요약

- `inplace=True`, `drop=True`: 원본 데이터프레임이 직접 수정되고, 기존 인덱스는 삭제.
- `inplace=True`, `drop=False`: 원본 데이터프레임이 직접 수정되고, 기존 인덱스가 새로운 열로 추가.
- `inplace=False`, `drop=True`: 원본 데이터프레임은 수정되지 않고, 기존 인덱스가 삭제된 새로운 데이터프레임이 생성.
- `inplace=False`, `drop=False`: 원본 데이터프레임은 수정되지 않고, 기존 인덱스가 새로운 열로 추가된 새로운 데이터프레임이 생성.

---

[^1] inplace의 원래 영어 의미는 “원래 위치에”, “제자리에서” 또는 “기존 위치에서”를 의미한다. 이 용어는 어떤 동작이나 변경이 새로운 위치나 다른 객체를 생성하는 대신, 현재 위치나 원래 객체에서 직접 수행되는 것을 의미한다다

예를 들어, 프로그램 코드에서 inplace 파라미터를 사용한다는 것은 함수나 메서드가 현재 객체를 변경하고, 그 결과를 새로운 객체로 반환하지 않고 원래 객체에 그대로 반영한다는 의미이다.

Pandas에서 inplace=True를 사용하는 경우, 데이터프레임이나 시리즈 객체가 새로운 객체로 반환되지 않고 원래 객체가 직접 수정된다. inplace=False일 경우에는 변경이 적용된 새로운 객체가 반환되고, 원래 객체는 변경되지 않는다.
