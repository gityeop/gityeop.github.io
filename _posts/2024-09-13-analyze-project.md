---
title: 자연어 처리(NLP) 필기 노트
date: 2024-09-13
categories: machine-learning
---

## 데이터 수집

## 데이터 정제

1. 오탈자 제거
2. 문법 교정
3. 불용어 제거
4. 노이즈 제거
5. 정규화
6. 토큰화

## 훈련

1. 파라미터
2. 하이퍼파라미터
3. 학습 파라미터 설정

## 예측

1. 모델 평가
2. 모델 분석
3. 모델 활용
4. 추론

## 보완

1. 모델 개선
2. 학습 데이터 정제
3. 학습 데이터 보완
4. 모델 경량화

---

# 자연어 처리(NLP) 필기 노트

## 데이터 수집

자연어 처리의 첫 단계는 양질의 데이터를 수집하는 것이다. 예를 들어, 뉴스 기사, 소셜 미디어 포스트, 블로그 글 등 다양한 출처에서 텍스트 데이터를 모을 수 있다.

- **예시**: 트위터 API를 사용하여 특정 키워드로 트윗을 수집하거나, 웹 스크래핑을 통해 뉴스 기사를 모을 수 있다.

## 데이터 정제

수집한 데이터는 바로 사용하기 어렵기 때문에 정제 과정이 필요하다.

### 1. 오탈자 제거

텍스트에 잘못된 철자가 있으면 모델의 성능에 부정적인 영향을 줄 수 있다. 오탈자를 제거하여 데이터의 정확성을 높인다.

- **예시**: '안녕하세요' 대신 '안년하세요'로 잘못 표기된 부분을 찾아서 수정한다.

### 2. 문법 교정

문법 오류를 수정하면 모델이 더 정확한 언어 패턴을 학습할 수 있다.

- **예시**: '나는 학교 갔다'를 '나는 학교에 갔다'로 수정한다.

- **코드 예시**:

```python
import language_tool_python

tool = language_tool_python.LanguageTool('ko')
text = "Today I went school."
matches = tool.check(text)
corrected_text = language_tool_python.utils.correct(text, matches)
print(corrected_text)
# 출력: 'Today I went to school.'
```

### 3. 불용어 제거

의미 전달에 큰 영향을 주지 않는 단어들을 제거하여 데이터의 품질을 높인다.

- **예시**: 조사나 접속사인 '은', '는', '이', '가' 등을 제거한다.

- **코드 예시**:

```python
from konlpy.tag import Okt

okt = Okt()
text = "오늘은 날씨가 정말 좋다"
stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '도', '으로', '그리고', '하지만']
tokens = okt.morphs(text)
tokens = [word for word in tokens if word not in stopwords]
print(tokens)
# 출력: ['오늘', '날씨', '정말', '좋다']
```

### 4. 노이즈 제거

HTML 태그나 특수 문자, 이모티콘 등 불필요한 정보를 제거한다.

- **예시**: '<div>안녕하세요 :) !!</div>'에서 HTML 태그와 이모티콘, 특수 문자를 제거한다.

- **코드 예시**:

```python
import re

text = "<div>안녕하세요 :) !!</div>"
clean_text = re.sub(r'<[^>]+>', '', text)  # HTML 태그 제거
clean_text = re.sub(r'[^\w\s]', '', clean_text)  # 특수 문자 제거
print(clean_text)
# 출력: '안녕하세요 '
```

### 5. 정규화

비슷한 의미를 가진 단어들을 통일하여 일관성을 높인다.

- **예시**: 'ㅎㅇ', '하이', '안녕'을 모두 '안녕하세요'로 바꿔준다.

- **코드 예시**:

```python
text = "ㅎㅇ, 오늘 기분 어떰?"
normalization_dict = {'ㅎㅇ': '안녕하세요', '하이': '안녕하세요', '안녕': '안녕하세요', '어떰': '어때요'}
tokens = text.split()
normalized_tokens = [normalization_dict.get(token, token) for token in tokens]
normalized_text = ' '.join(normalized_tokens)
print(normalized_text)
# 출력: '안녕하세요, 오늘 기분 어때요?'
```

### 6. 토큰화

텍스트를 단어 또는 문장 단위로 분리한다.

- **예시**:

```python
from konlpy.tag import Okt

okt = Okt()
text = "자연어 처리는 재미있다"
tokens = okt.morphs(text)
print(tokens)
# 출력: ['자연어', '처리', '는', '재미있', '다']
```

- **추가 설명**: 토큰화는 모델이 텍스트 데이터를 이해하고 학습할 수 있도록 하는 중요한 단계이다. 단어 토큰화 외에도 문자 토큰화, 문장 토큰화 등이 있으며, 모델과 목적에 따라 적절한 토큰화 방법을 선택한다.

## 훈련

모델을 학습시키는 단계이다.

### 1. 파라미터

모델 내부에서 학습되는 값들로, 데이터에 의해 업데이트된다.

- **예시**: 신경망의 가중치(weight)와 편향(bias).

- **추가 설명**: 파라미터는 모델이 입력 데이터로부터 학습하여 예측을 수행하는 데 핵심적인 역할을 한다. 모델의 복잡도와 성능은 파라미터의 수와 품질에 크게 좌우된다.

### 2. 하이퍼파라미터

학습 과정에서 사람이 설정해야 하는 값들이다.

- **예시**: 학습률(learning rate), 에포크 수(epoch), 배치 크기(batch size), 활성화 함수(activation function) 등.

- **추가 설명**: 하이퍼파라미터는 모델의 학습 속도와 성능에 직접적인 영향을 미치며, 적절한 값을 찾기 위해서는 실험과 검증이 필요하다.

### 3. 학습 파라미터 설정

모델을 최적화하기 위해 하이퍼파라미터를 조절한다.

- **예시**:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 하이퍼파라미터 설정
learning_rate = 0.001
num_epochs = 10
batch_size = 32

# 모델 정의
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.layer = nn.Linear(10, 1)
    def forward(self, x):
        return self.layer(x)

model = MyModel()

# 손실 함수와 옵티마이저 정의
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
```

- **추가 설명**: 학습률이 너무 크면 최적점에 수렴하지 못하고 발산할 수 있으며, 너무 작으면 학습 속도가 느려질 수 있다. 에포크 수와 배치 크기도 모델의 성능과 학습 시간에 영향을 미친다.

## 예측

학습된 모델을 사용하여 결과를 예측하는 단계이다.

### 1. 모델 평가

모델의 성능을 측정한다.

- **예시**: 정확도(accuracy), 정밀도(precision), 재현율(recall), F1 스코어 등을 계산한다.

- **코드 예시**:

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
```

- **추가 설명**: 분류 문제에서는 혼동 행렬(confusion matrix)을 사용하여 모델의 오류 유형을 분석할 수 있다.

### 2. 모델 분석

모델이 어떤 부분에서 잘하고 못하는지 분석한다.

- **예시**: 오분류된 사례들을 검토하여 모델의 약점을 파악한다.

- **추가 설명**: 오류 분석을 통해 데이터의 불균형, 특정 클래스에 대한 낮은 성능 등의 문제를 발견할 수 있으며, 이를 개선하기 위한 전략을 수립할 수 있다.

### 3. 모델 활용

실제 서비스나 애플리케이션에 모델을 적용한다.

- **예시**: 챗봇에 자연어 이해(NLU) 모델을 적용하여 사용자 질문에 적절한 답변을 제공한다.

- **추가 설명**: 모델을 배포할 때는 추론 속도와 정확도, 시스템 자원 등의 요소를 고려해야 한다.

### 4. 추론

새로운 데이터에 대해 예측값을 생성한다.

- **예시**:

```python
# 입력 문장에 대한 예측
input_text = "오늘 날씨 어때?"
input_tokens = tokenize(input_text)
input_tensor = torch.tensor([vocab[token] for token in input_tokens])

model.eval()
with torch.no_grad():
    output = model(input_tensor)
    predicted = torch.argmax(output, dim=1)
print("예측 결과:", predicted.item())
```

- **추가 설명**: 추론 단계에서는 배치 처리(batch processing)를 통해 여러 입력에 대해 동시에 예측을 수행하여 효율성을 높일 수 있다.

## 보완

모델의 성능을 향상시키는 단계이다.

### 1. 모델 개선

더 나은 아키텍처나 기법을 적용하여 모델의 성능을 높인다.

- **예시**: 순환 신경망(RNN)에서 트랜스포머(Transformer) 모델로 변경하거나, 어텐션 메커니즘을 추가한다.

- **추가 설명**: 최신 연구 동향을 반영하여 모델을 개선하면 성능 향상을 기대할 수 있다. 예를 들어, BERT나 GPT와 같은 사전 학습된 언어 모델을 활용할 수 있다.

### 2. 학습 데이터 정제

데이터의 품질을 높여 모델의 성능을 향상시킨다.

- **예시**: 오탈자나 노이즈가 있는 데이터를 제거하거나 수정한다.

- **추가 설명**: 데이터의 품질은 모델의 성능에 직접적인 영향을 미치므로, 데이터 정제에 충분한 시간을 투자하는 것이 중요하다.

### 3. 학습 데이터 보완

더 많은 데이터를 추가하거나 데이터 증강(data augmentation) 기법을 사용한다.

- **예시**: 동의어 치환(Synonym Replacement)을 사용하여 데이터를 늘린다.

- **코드 예시**:

```python
import random

def synonym_replacement(sentence, n):
    words = sentence.split()
    new_words = words.copy()
    random_word_list = list(set([word for word in words if word in synonyms]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for random_word in random_word_list:
        synonyms_list = synonyms.get(random_word)
        if synonyms_list:
            synonym = random.choice(synonyms_list)
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:
            break
    return ' '.join(new_words)

# 동의어 사전
synonyms = {'좋다': ['훌륭하다', '멋지다'], '날씨': ['기상', '하늘']}

sentence = "오늘 날씨가 좋다"
augmented_sentence = synonym_replacement(sentence, n=1)
print(augmented_sentence)
# 출력 예시: "오늘 기상이 좋다"
```

- **추가 설명**: 데이터 증강은 특히 데이터가 부족한 상황에서 모델의 일반화 능력을 향상시키는 데 도움이 된다.

### 4. 모델 경량화

모델의 크기를 줄여 추론 속도를 높이고 자원 사용을 줄인다.

- **예시**: 지식 증류(Knowledge Distillation), 양자화(Quantization), 프루닝(Pruning) 등을 적용한다.

- **코드 예시**: 지식 증류를 통한 경량화

```python
# 교사 모델과 학생 모델 정의
teacher_model = TeacherModel()
student_model = StudentModel()

# 지식 증류 손실 함수
def distillation_loss(y_student, y_teacher, labels, T, alpha):
    loss_ce = nn.CrossEntropyLoss()(y_student, labels)
    loss_kd = nn.KLDivLoss()(F.log_softmax(y_student/T, dim=1), F.softmax(y_teacher/T, dim=1)) * (T * T)
    return loss_ce * (1 - alpha) + loss_kd * alpha

# 학습 루프에서 사용
for data, labels in dataloader:
    optimizer.zero_grad()
    with torch.no_grad():
        teacher_outputs = teacher_model(data)
    student_outputs = student_model(data)
    loss = distillation_loss(student_outputs, teacher_outputs, labels, T=2, alpha=0.5)
    loss.backward()
    optimizer.step()
```

- **추가 설명**: 모델 경량화를 통해 모바일이나 임베디드 시스템에서도 모델을 활용할 수 있다.
