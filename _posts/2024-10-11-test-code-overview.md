---
title: Unit Testing
date: 2024-10-11
categories:
tags: ["programming/testing", "programming/development"]
---

유닛 테스트(Unit Testing)는 소프트웨어 개발에서 개별 코드 단위(함수, 메서드 등)를 독립적으로 테스트하여 예상대로 동작하는지 확인하는 중요한 방법이다. Python에서는 내장된 `unittest` 프레임워크를 주로 사용하며, 이를 통해 코드의 신뢰성과 유지보수성을 크게 향상시킬 수 있다.

이 글에서는 유닛 테스트를 작성하고 해석하는 방법, 발생한 문제를 해결하는 방법, 그리고 좋은 테스트 코드를 작성하기 위한 베스트 프랙티스에 대해 자세히 설명한다.

## **1. `unittest` 프레임워크 이해하기**

### **a. `unittest`란?**

`unittest`는 Python의 표준 라이브러리로 제공되는 테스트 프레임워크이다. Java의 JUnit에서 영감을 받아 만들어졌으며, 다양한 테스트 도구와 기능을 제공하여 코드의 올바름을 검증하는 데 도움을 준다.

### **b. 기본 테스트 케이스 구조**

간단한 예제를 통해 `unittest`의 기본 구조를 이해해보자:

```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

**설명:**

- **`import unittest`**: `unittest` 모듈을 임포트한다.
- **테스트할 함수 정의**: 여기서는 `add` 함수가 두 숫자를 더한다.
- **테스트 케이스 클래스 작성**: `unittest.TestCase`를 상속받는 클래스를 만든다.
- **테스트 메서드 작성**: `test_`로 시작하는 메서드 내에서 다양한 입력과 출력을 검증한다.
- **테스트 실행**: `if __name__ == '__main__':` 블록을 통해 테스트를 실행한다.

### **c. 테스트 실행하기**

테스트 파일이 있는 디렉토리에서 다음 명령어를 실행하여 테스트를 수행할 수 있다:

```bash
python -m unittest test_math_functions.py
```

`test_math_functions.py`는 작성한 테스트 파일의 이름이다.

## **2. 효과적인 유닛 테스트 작성하기**

### **a. 테스트 단위 격리하기**

각 테스트 케이스는 단일 함수나 메서드에 집중하여 독립적으로 동작해야 한다. 이렇게 하면 어떤 테스트가 실패했는지 쉽게 파악할 수 있다.

### **b. 테스트 메서드 이름 명확하게 짓기**

테스트 메서드 이름을 통해 무엇을 테스트하는지 명확히 알 수 있도록 한다. 예를 들어:

```python
def test_add_positive_numbers(self):
    self.assertEqual(add(2, 3), 5)

def test_add_negative_numbers(self):
    self.assertEqual(add(-1, -1), -2)
```

### **c. `setUp`과 `tearDown` 메서드 사용하기**

`setUp` 메서드는 각 테스트가 실행되기 전에 호출되며, `tearDown` 메서드는 테스트가 끝난 후 호출된다. 이를 통해 테스트 전후에 필요한 설정과 정리를 할 수 있다.

```python
class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(add(self.a, self.b), 15)
```

### **d. 외부 의존성 Mocking 하기**

코드가 외부 시스템(API, 데이터베이스 등)과 상호작용할 때는 `unittest.mock`을 사용하여 이러한 의존성을 모킹(mocking)한다. 이렇게 하면 테스트가 빠르고 안정적으로 실행된다.

**예제: `unittest.mock`을 사용한 Mocking**

```python
from unittest.mock import patch, MagicMock

class TestCategorizingQuestions(unittest.TestCase):
    @patch('categorizing_questions_script.client.chat.completions.create')
    def test_categorize_questions(self, mock_create):
        # Mock API 응답 설정
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content='[{"question_number": 1, "category": "HUMAN"}, {"question_number": 2, "category": "OBJECT"}]'))
        ]
        mock_create.return_value = mock_response

        from categorizing_questions_script import categorize_questions
        batch = ["What is AI?", "Describe a car."]
        result = categorize_questions(batch)
        self.assertEqual(result, ["HUMAN", "OBJECT"])
```

**설명:**

- **`@patch` 데코레이터**: 특정 경로의 함수를 Mock 객체로 대체한다.
- **`mock_create`**: Mock된 함수이다.
- **Mock 응답 설정**: API 호출 시 반환될 응답을 정의한다.
- **함수 호출 및 결과 검증**: 실제 함수를 호출하고 예상 결과와 비교한다.

## **3. 테스트 결과 읽고 해석하기**

테스트를 실행하면 다음과 같은 출력이 나타날 수 있다:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

이 출력은 모든 테스트가 성공적으로 통과했음을 의미한다. 하지만 실패나 에러가 발생하면 더 자세한 정보가 제공된다:

```
.F.E.
======================================================================
FAIL: test_categorize_questions (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 46, in test_categorize_questions
    self.assertEqual(result, ["HUMAN", "OBJECT"])
AssertionError: <MagicMock name='categorize_questions()' id='139625319978832'> != ['HUMAN', 'OBJECT']

======================================================================
ERROR: test_save_categorized_data (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 72, in test_save_categorized_data
    df['answers'] = df['answers'].apply(ast.literal_eval)
ValueError: malformed node or string: {'text': ['Answer1'], 'answer_start': [0]}

----------------------------------------------------------------------
Ran 5 tests in 1.996s

FAILED (failures=1, errors=1)
```

**해석:**

- **`.`**: 테스트가 성공했음을 의미한다.
- **`F`**: 실패한 테스트가 있음을 나타낸다.
- **`E`**: 에러가 발생한 테스트가 있음을 나타낸다.
- **Traceback**: 어디에서 어떤 오류가 발생했는지 자세한 정보를 제공한다.

### **Common Issues and Resolutions**

#### **a. Assertion Failures**

- **Cause**: 실제 결과가 예상 결과와 다를 때 발생한다.
- **Resolution**: 함수 로직을 검토하고, Mock 설정이 올바른지 확인한다.

**Example Issue:**

```python
self.assertEqual(result, ["HUMAN", "OBJECT"])
```

- **Problem**: `result`가 `MagicMock` 객체일 경우.
- **Solution**: 테스트에서 함수 자체를 Mock하지 말고, 외부 의존성(API 호출 등)만 Mock하도록 한다.

#### **b. Errors Due to Incorrect Mocking**

- **Cause**: 테스트가 예상치 못한 데이터 타입이나 unmocked 외부 상호작용을 시도할 때 발생한다.
- **Resolution**: Mock이 올바른 데이터 타입을 반환하는지, 모든 외부 의존성이 제대로 Mock되었는지 확인한다.

**Specific to Your Case:**

1. **Error in `test_save_categorized_data`:**

   ```
   ValueError: malformed node or string: {'text': ['Answer1'], 'answer_start': [0]}
   ```

   - **Cause**: `save_categorized_data` 함수가 `'answers'` 컬럼을 `ast.literal_eval`로 파싱하려고 할 때, 딕셔너리가 문자열이 아닌 실제 딕셔너리로 제공되어 오류가 발생했다.
   - **Solution**: 테스트 데이터에서 `'answers'` 컬럼을 JSON 문자열 형식으로 제공하여 `ast.literal_eval`이 올바르게 파싱할 수 있도록 한다.

   **Corrected Test Data:**

   ```python
   df = pd.DataFrame({
       "id": ["1", "2"],
       "title": ["AI", "Telephone"],
       "context": ["Context1", "Context2"],
       "question": ["What is AI?", "Who invented the telephone?"],
       "answers": [
           '{"text": ["Answer1"], "answer_start": [0]}',
           '{"text": ["Answer2"], "answer_start": [10]}'
       ],
       "category": ["HUMAN", "OBJECT"]
   })
   ```

2. **Failure in `test_categorize_questions`:**

   ```
   AssertionError: <MagicMock name='categorize_questions()' id='139625319978832'> != ['HUMAN', 'OBJECT']
   ```

   - **Cause**: `test_categorize_questions` 테스트에서 `categorize_questions` 함수를 Mock하고 있어, 실제 함수가 호출되지 않고 `MagicMock` 객체를 반환하게 되었다.
   - **Solution**: `categorize_questions` 함수를 Mock하지 않고, 내부에서 호출되는 OpenAI API 클라이언트(`client.chat.completions.create`)만 Mock하여 함수의 실제 로직을 테스트하도록 한다.

   **Correct Approach:**

   - **Mock Only External Calls**: `categorize_questions` 함수 내부에서 호출되는 `client.chat.completions.create` 메서드만 Mock한다.
   - **Allow `categorize_questions` to Execute Normally**: 함수가 Mock된 API 응답을 처리하여 예상 결과를 반환하게 한다.

   **Example:**

   ```python
   @patch("categorizing_questions_script.client.chat.completions.create")
   def test_categorize_questions(self, mock_create):
       # Mock API 응답 설정
       mock_response = MagicMock()
       mock_response.choices = [
           MagicMock(message=MagicMock(content='[{"question_number": 1, "category": "HUMAN"}, {"question_number": 2, "category": "OBJECT"}]'))
       ]
       mock_create.return_value = mock_response

       from categorizing_questions_script import categorize_questions
       batch = ["What is AI?", "Describe a car."]
       result = categorize_questions(batch)
       self.assertEqual(result, ["HUMAN", "OBJECT"])
   ```

## **4. 유닛 테스트 작성 및 읽는 방법 요약**

### **a. 테스트 작성 방법**

1. **테스트할 함수 또는 메서드 결정**: 각 테스트는 특정 함수나 메서드의 동작을 검증해야 한다.
2. **테스트 케이스 클래스 생성**: `unittest.TestCase`를 상속받는 클래스를 만든다.
3. **테스트 메서드 작성**: `test_`로 시작하는 메서드를 작성하여 다양한 입력과 예상 출력을 검증한다.
4. **Mocking 적용**: 외부 의존성이 있는 경우, `unittest.mock`을 사용하여 Mock 객체를 생성하고 필요한 응답을 설정한다.
5. **Assertions 사용**: `self.assertEqual`, `self.assertTrue` 등 다양한 어서션 메서드를 사용하여 실제 결과와 예상 결과를 비교한다.

### **b. 테스트 읽는 방법**

- **성공**: `.` 표시가 나오며, 최종적으로 `OK` 메시지가 나타난다.
- **실패/에러**: 특정 테스트가 실패하거나 에러가 발생하면, 해당 테스트의 상세한 정보와 함께 실패 원인이 표시된다.

**예시:**

```
.F.E.
======================================================================
FAIL: test_categorize_questions (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 46, in test_categorize_questions
    self.assertEqual(result, ["HUMAN", "OBJECT"])
AssertionError: <MagicMock name='categorize_questions()' id='139625319978832'> != ['HUMAN', 'OBJECT']

======================================================================
ERROR: test_save_categorized_data (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 72, in test_save_categorized_data
    df['answers'] = df['answers'].apply(ast.literal_eval)
ValueError: malformed node or string: {'text': ['Answer1'], 'answer_start': [0]}

----------------------------------------------------------------------
Ran 5 tests in 1.996s

FAILED (failures=1, errors=1)
```

**해석:**

- **`.`**: 성공한 테스트.
- **`F`**: 실패한 테스트 (`test_categorize_questions`).
- **`E`**: 에러가 발생한 테스트 (`test_save_categorized_data`).
- **Traceback**: 문제의 원인과 발생 위치를 상세히 알려준다.

### **c. 자주 발생하는 문제와 해결 방법**

#### **1. 어서션 실패 (`AssertionError`)**

- **원인**: 실제 결과가 예상 결과와 다를 때 발생한다.
- **해결 방법**: 함수 로직을 검토하고, Mock 설정이 올바른지 확인한다.

**예시 문제:**

```python
self.assertEqual(result, ["HUMAN", "OBJECT"])
```

- **문제**: `result`가 `MagicMock` 객체일 경우.
- **해결**: 테스트에서 함수 자체를 Mock하지 말고, 외부 의존성(API 호출 등)만 Mock하도록 한다.

#### **2. Mocking 관련 에러 (`ValueError`, `TypeError` 등)**

- **원인**: Mock된 데이터의 형식이 함수가 기대하는 형식과 다를 때 발생한다.
- **해결 방법**: Mock 데이터의 형식을 함수가 처리할 수 있는 형식으로 맞춘다.

**예시 문제:**

```
ValueError: malformed node or string: {'text': ['Answer1'], 'answer_start': [0]}
```

- **해결**: `'answers'` 컬럼의 값을 문자열(JSON 형식)으로 변경하여 `ast.literal_eval`이 올바르게 파싱할 수 있도록 한다.

## **5. 좋은 유닛 테스트 작성하기 위한 베스트 프랙티스**

### **a. 테스트의 독립성 유지**

각 테스트는 다른 테스트에 의존하지 않고 독립적으로 실행되어야 한다. 이를 통해 특정 테스트의 실패가 다른 테스트에 영향을 미치지 않도록 한다.

### **b. 의미 있는 어서션 사용**

단순히 최종 결과만 검증하는 것보다, 중간 단계의 상태도 검증하여 문제가 발생한 위치를 더 쉽게 파악할 수 있도록 한다.

### **c. 다양한 케이스 테스트**

정상적인 입력뿐만 아니라, 엣지 케이스(예외 상황, 비정상적인 입력 등)도 테스트하여 함수의 견고성을 확인한다.

### **d. 명확하고 설명적인 테스트 이름 사용**

테스트 이름을 통해 무엇을 테스트하는지 명확히 알 수 있도록 한다.

```python
def test_save_categorized_data_with_valid_input(self):
    # 테스트 코드
```

### **e. 외부 의존성 적절히 Mocking**

- **Only Mock What’s Necessary**: Mock 객체는 외부 시스템과의 상호작용만 대체한다.
- **Return Realistic Data**: Mock이 반환하는 데이터는 함수가 기대하는 형식과 일치해야 한다.

### **f. `setUp`과 `tearDown` 활용**

여러 테스트에서 공통으로 사용하는 설정이나 데이터를 `setUp` 메서드에 작성하여 코드 중복을 줄인다.

```python
class TestCategorizingQuestions(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame({
            "id": ["1", "2"],
            "title": ["AI", "Telephone"],
            "context": ["Context1", "Context2"],
            "question": ["What is AI?", "Who invented the telephone?"],
            "answers": [
                '{"text": ["Answer1"], "answer_start": [0]}',
                '{"text": ["Answer2"], "answer_start": [10]}'
            ],
            "category": ["HUMAN", "OBJECT"]
        })
```

### **g. 테스트 커버리지 유지**

코드의 다양한 부분을 테스트하여 잠재적인 버그를 조기에 발견한다.

## **6. 테스트 스위트 실행 및 해석**

### **a. 테스트 실행하기**

작성한 테스트 스크립트를 실행하려면 다음 명령어를 사용한다:

```bash
python -m unittest test_categorizing_questions.py
```

### **b. 테스트 결과 해석하기**

- **성공**: 모든 테스트가 통과했을 때는 `OK` 메시지가 표시된다.
- **실패/에러**: 특정 테스트가 실패하거나 에러가 발생하면, 해당 테스트의 상세한 정보와 함께 실패 원인이 표시된다.

**성공 예시:**

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

**실패 예시:**

```
.F.E.
======================================================================
FAIL: test_categorize_questions (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 46, in test_categorize_questions
    self.assertEqual(result, ["HUMAN", "OBJECT"])
AssertionError: <MagicMock name='categorize_questions()' id='139625319978832'> != ['HUMAN', 'OBJECT']

======================================================================
ERROR: test_save_categorized_data (test_categorizing_questions.TestCategorizingQuestions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_categorizing_questions.py", line 72, in test_save_categorized_data
    df['answers'] = df['answers'].apply(ast.literal_eval)
ValueError: malformed node or string: {'text': ['Answer1'], 'answer_start': [0]}

----------------------------------------------------------------------
Ran 5 tests in 1.996s

FAILED (failures=1, errors=1)
```

**해석:**

- **`.`**: 성공한 테스트.
- **`F`**: 실패한 테스트 (`test_categorize_questions`).
- **`E`**: 에러가 발생한 테스트 (`test_save_categorized_data`).
- **Traceback**: 문제의 원인과 발생 위치를 상세히 알려준다.

## **7. 추가 팁**

### **a. Fixtures 사용하기**

여러 테스트에서 공통으로 사용하는 설정이나 데이터를 `setUp` 메서드에 작성하여 재사용한다.

```python
class TestCategorizingQuestions(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "id": ["1", "2"],
            "title": ["AI", "Telephone"],
            "context": ["Context1", "Context2"],
            "question": ["What is AI?", "Who invented the telephone?"],
            "answers": [
                '{"text": ["Answer1"], "answer_start": [0]}',
                '{"text": ["Answer2"], "answer_start": [10]}'
            ],
            "category": ["HUMAN", "OBJECT"]
        })
```

### **b. 예외 상황 테스트하기**

함수가 특정 조건에서 예외를 발생시키는지 테스트한다.

```python
def test_load_dataset_with_invalid_path(self):
    from categorizing_questions_script import load_dataset
    with self.assertRaises(FileNotFoundError):
        load_dataset("invalid_path.arrow")
```

### **c. 테스트 발견 및 관리**

테스트 파일과 메서드를 적절히 명명하여 `unittest`가 자동으로 테스트를 발견하고 실행할 수 있도록 한다. 일반적으로 테스트 파일은 `test_*.py` 형식을 따른다.

### **d. 파라미터화된 테스트**

여러 입력 케이스를 간편하게 테스트하기 위해 파라미터화된 테스트를 사용한다. `parameterized` 라이브러리나 `pytest`를 사용하는 것이 일반적이다.

**`parameterized` 예제:**

```python
from parameterized import parameterized

class TestMathFunctions(unittest.TestCase):

    @parameterized.expand([
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(self, a, b, expected):
        self.assertEqual(add(a, b), expected)
```

### **e. 테스트 커버리지 측정**

테스트 커버리지를 측정하여 코드의 어떤 부분이 테스트되지 않았는지 파악할 수 있다. `coverage` 라이브러리를 사용하면 편리하다.

**설치 및 사용:**

```bash
pip install coverage
coverage run -m unittest test_categorizing_questions.py
coverage report
