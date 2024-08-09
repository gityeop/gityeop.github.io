---
title: Linear Regression Quiz
date: 2024-08-08
categories: machine-learning
---

### 기본 이해

1.  **다음 용어를 정의하세요:**

    - 선형 회귀
    - 훈련 데이터
    - 특징 변수
    - 목표 변수
    - 손실 함수

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       - <strong>선형 회귀:</strong> 주어진 데이터를 사용하여 특징 변수와 목표 변수 사이의 선형 관계를 분석하고, 이 관계를 기반으로 새로운 데이터의 결과를 예측하는 통계 기법입니다.<br>
       - <strong>훈련 데이터:</strong> 모델을 학습시키기 위해 사용되는 데이터로, 모델이 특징 변수와 목표 변수 간의 관계를 학습하는 데 사용됩니다.<br>
       - <strong>특징 변수:</strong> 입력 데이터로, 예측 모델에 제공되는 독립 변수입니다.<br>
       - <strong>목표 변수:</strong> 출력 데이터로, 모델이 예측하려는 종속 변수입니다.<br>
       - <strong>손실 함수:</strong> 모델의 예측 값과 실제 값 간의 차이를 측정하는 함수로, 모델을 최적화하는 데 사용됩니다.
       </p>
    </div>
    </div>

2.  **Kaggle에서 급여 데이터를 다운로드하고 분석을 위해 준비하는 과정을 설명하세요.**

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       Kaggle API를 사용하여 급여 데이터를 다운로드하고, 압축을 해제한 후 Pandas 라이브러리를 사용하여 CSV 파일을 DataFrame으로 로드합니다. 이 데이터에서 특징 변수와 목표 변수를 분리하여 분석을 준비합니다.
       </p>
    </div>
    </div>

3.  **경험 연수와 해당 급여의 데이터셋이 주어졌을 때, 이 데이터를 Pandas DataFrame에 로드하는 Python 함수를 작성하세요.**
    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
          <div class="language-python highlighter-rouge">
          <div class="highlight">
                <pre class="highlight"><code>
          import pandas as pd

          def load_data(filepath):
          data = pd.read_csv(filepath)
          return data
          </code>

          </pre>
          </div>

       </div>
    </div>
    </div>

4.  **로드된 데이터를 특징 변수(경험 연수)와 목표 변수(급여)로 분할하는 Python 함수를 작성하세요.**
    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
             <div class="language-python highlighter-rouge">
          <div class="highlight">
                <pre class="highlight"><code>
          def split_data(data):
             X = data.iloc[:, 0].values  # 특징 변수 (경험 연수)
             y = data.iloc[:, 1].values  # 목표 변수 (급여)
             return X, y
          </code>
          </pre> 
          </div> 
          </div>
    </div>
    </div>

5.  **경험 연수와 급여 간의 상관 관계를 결정하는 데 있어서 상관 계수의 중요성을 분석하세요. 상관 계수 0.9782는 이 맥락에서 무엇을 의미하나요?**

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       상관 계수는 두 변수 간의 선형 관계의 강도를 나타냅니다. 상관 계수 0.9782는 경험 연수와 급여 간에 매우 강한 양의 선형 관계가 있음을 의미합니다. 이는 경험 연수가 증가할수록 급여도 증가하는 경향이 강하다는 것을 나타냅니다.
       </p>
    </div>
    </div>

6.  **강의 노트에 설명된 PyTorch를 사용하여 선형 회귀 모델을 구축하는 단계를 분석하세요.**

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       PyTorch를 사용하여 선형 회귀 모델을 구축하는 단계는 다음과 같습니다:<br>
       1. `torch.nn` 모듈을 가져와 선형 회귀 모델 클래스를 정의합니다.<br>
       2. 생성자 메서드에서 `nn.Linear`를 사용하여 선형 계층을 정의합니다.<br>
       3. 순전파 메서드에서 입력 데이터를 받아 예측 값을 계산합니다.<br>
       4. 모델을 학습하기 위해 손실 함수를 정의하고 최적화 알고리즘을 설정합니다.<br>
       5. 모델을 훈련 데이터에 맞추어 학습시킵니다.
       </p>
    </div>
    </div>

7.  **선형 회귀 모델의 정확성을 테스트하기 위한 실험을 설계하세요. 수행할 단계와 모델의 성능을 평가할 지표를 설명하세요.**

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       **실험 설계:**<br>
       1. 데이터를 수집하고 전처리합니다.<br>
       2. 데이터를 훈련 세트와 테스트 세트로 분할합니다.<br>
       3. 선형 회귀 모델을 구축하고 훈련 데이터를 사용하여 학습시킵니다.<br>
       4. 테스트 데이터를 사용하여 모델의 예측을 수행합니다.<br>
       5. 예측 값과 실제 값 간의 차이를 계산하여 성능을 평가합니다.<br>
       6. 모델의 성능을 평가하는 지표로 평균 제곱 오차(MSE), 평균 절대 오차(MAE), 결정 계수(R²) 등을 사용합니다.
       </p>
    </div>
    </div>

8.  **선형 회귀 모델의 주요 목적은 무엇인가요?**

    - A. 데이터를 다른 카테고리로 분류하는 것
    - B. 데이터 포인트에 가장 적합한 곡선을 찾는 것
    - C. 데이터 포인트에 가장 적합한 직선을 찾는 것
    - D. 데이터 포인트를 유사성에 따라 클러스터링하는 것

    <div class="answer">
    <button class="toggle-answer">답안 보기/숨기기</button>
    <div class="answer-content" style="display: none;">
       <strong>답안:</strong>
       <p>
       - **정답:** C. 데이터 포인트에 가장 적합한 직선을 찾는 것<br>
       - **정답 이유:** 선형 회귀 모델은 주어진 데이터에서 독립 변수와 종속 변수 사이의 관계를 설명하는 최적의 직선을 찾는 것을 목적으로 합니다.
       </p>
    </div>
    </div>

9.  **다음 중 평균 제곱 오차(MSE) 손실 함수의 특성이 아닌 것은?**

- A. 오차의 제곱의 평균을 측정한다.
- B. 선형 회귀 모델을 최적화하는 데 사용될 수 있다.
- C. 예측 값과 실제 값 간의 절대 차이를 계산한다.
- D. 예측 오차를 최소화하는 직선을 찾는 데 도움을 준다.

   <div class="answer">
   <button class="toggle-answer">답안 보기/숨기기</button>
   <div class="answer-content" style="display: none;">
    <strong>답안:</strong>
    <p>
    - **정답:** C. 예측 값과 실제 값 간의 절대 차이를 계산한다.<br>
    - **정답 이유:** 평균 제곱 오차(MSE)는 예측 값과 실제 값 간의 차이의 제곱의 평균을 측정하는 손실 함수로, 절대 차이를 계산하지 않습니다.
    </p>
   </div>
   </div>

11. **다음 코드는 무엇을 하나요? `pd.read_csv('salary_dataset.csv', sep=',', header=0)`**

    - A. 첫 번째 행을 데이터로 사용하여 CSV 파일을 DataFrame으로 읽어들인다.
    - B. 첫 번째 행을 열 이름으로 사용하여 CSV 파일을 DataFrame으로 읽어들인다.
    - C. DataFrame의 데이터를 CSV 파일로 작성한다.
    - D. 열 이름을 CSV 파일로 작성한다.

   <div class="answer">
   <button class="toggle-answer">답안 보기/숨기기</button>
   <div class="answer-content" style="display: none;">
      <strong>답안:</strong>
      <p>
      - **정답:** B. 첫 번째 행을 열 이름으로 사용하여 CSV 파일을 DataFrame으로 읽어들인다.<br>
      - **정답 이유:** `pd.read_csv` 함수의 `header=0` 인자는 첫 번째 행을 열 이름으로 사용하여 데이터를 DataFrame으로 읽어들이는 것을 의미합니다.
      </p>
   </div>
   </div>

12. **특징 변수와 목표 변수 간의 상관 관계를 시각화하는 데 있어서 산점도를 사용하는 이점은 무엇인가요?**

   <div class="answer">
   <button class="toggle-answer">답안 보기/숨기기</button>
   <div class="answer-content" style="display: none;">
      <strong>답안:</strong>
      <p>
      산점도는 두 변수 간의 관계를 직관적으로 시각화할 수 있으며, 선형 관계의 강도와 방향을 쉽게 파악할 수 있게 해줍니다. 또한 <strong>이상치</strong>를 식별하는 데도 유용합니다.
      </p>
   </div>
   </div>

13. **선형 회귀 모델을 학습할 때 손실 함수를 최소화하는 과정의 의미와 중요성을 설명하세요. 이 과정이 모델의 예측 정확도와 신뢰성에 어떻게 기여하는지 논의하세요.**

   <div class="answer">
   <button class="toggle-answer">답안 보기/숨기기</button>
   <div class="answer-content" style="display: none;">
      <strong>답안:</strong>
      <p>
      손실 함수를 최소화하는 과정은 모델이 목표 변수와 예측 변수 간의 차이를 줄이기 위한 것입니다. 손실 함수가 최소화되면 모델의 예측 값이 실제 값에 더 가까워지며, 이는 모델의 예측 정확도를 높이고 신뢰성을 향상시킵니다. 이 과정에서 모델의 가중치와 바이어스를 조정하여 최적의 직선을 찾게 되며, 이를 통해 새로운 데이터에 대해서도 높은 예측 성능을 보일 수 있습니다.
      </p>
   </div>
   </div>
