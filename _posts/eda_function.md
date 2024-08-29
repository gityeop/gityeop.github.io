타이타닉 데이터 분석 코드에서 사용된 함수와 메서드에 대해 더 자세히 정리하고, 추가적으로 관련된 유용한 메서드도 포함해 설명드리겠습니다.

### 데이터 불러오기 및 확인

1. **`sns.load_dataset()`**

   - **기능:** seaborn에 내장된 데이터셋을 불러옵니다.
   - **사용법:** `titanic = sns.load_dataset('titanic')`

2. **`head()`**

   - **기능:** 데이터프레임의 처음 몇 줄을 확인합니다.
   - **사용법:** `titanic.head()`는 처음 5개의 행을 출력합니다.

3. **`describe()`**
   - **기능:** 데이터프레임의 통계량(평균, 표준편차, 최소값, 최대값, 사분위수)을 제공합니다.
   - **사용법:** `titanic.describe()`는 타이타닉 데이터의 통계량을 출력합니다.

### 데이터 그룹화 및 집계

4. **`groupby()`**

   - **기능:** 특정 열에 따라 데이터를 그룹화합니다.
   - **사용법:** `titanic.groupby('sex')['alive'].value_counts()`는 성별에 따른 생존 여부를 그룹화합니다.

5. **`value_counts()`**

   - **기능:** 특정 열에서 각 값의 빈도를 계산합니다.
   - **사용법:** `titanic['sex'].value_counts()`는 성별의 빈도를 계산합니다.

6. **`sort_index()`**
   - **기능:** 인덱스를 기준으로 데이터를 정렬합니다.
   - **사용법:** `group.sort_index()`는 그룹화된 데이터를 인덱스 기준으로 정렬합니다.

### 데이터 시각화

7. **`plt.subplots()`**

   - **기능:** 여러 서브플롯을 포함하는 figure를 생성합니다.
   - **사용법:** `fig, axes = plt.subplots(1, 2, figsize=(15, 7))`

8. **`sns.countplot()`**

   - **기능:** 범주형 데이터의 빈도수를 시각화합니다.
   - **사용법:** `sns.countplot(x='survived', data=titanic, hue='sex')`는 생존 여부를 성별에 따라 시각화합니다.

9. **`sns.heatmap()`**

   - **기능:** 상관관계 등을 히트맵으로 시각화합니다.
   - **사용법:** `sns.heatmap(titanic.corr(), annot=True)`는 상관계수를 히트맵으로 시각화합니다.

10. **`sns.boxplot()`**

    - **기능:** 데이터의 분포와 이상치를 시각화하는 박스플롯을 생성합니다.
    - **사용법:** `sns.boxplot(x='age', data=titanic)`는 나이의 분포를 박스플롯으로 표현합니다.

11. **`ax.pie()`**

    - **기능:** 파이 차트를 생성합니다.
    - **사용법:** `ax.pie(group, labels=labels, explode=(0, 0.1, 0, 0), autopct='%1.1f%%', shadow=True, startangle=90)`

12. **`inset_axes()`**

    - **기능:** 메인 그래프 내에 작은 서브플롯을 추가합니다.
    - **사용법:** `ax_inset = inset_axes(ax, width="20%", height="20%", loc='upper right')`는 오른쪽 위에 작은 파이차트를 삽입합니다.

13. **`msno.matrix()`**
    - **기능:** 데이터셋 내의 결측치를 시각화합니다.
    - **사용법:** `msno.matrix(titanic)`는 결측치를 매트릭스 형태로 시각화합니다.

### 데이터 처리

14. **`isnull()`**

    - **기능:** 데이터프레임의 각 셀에 대해 결측값 여부를 확인합니다.
    - **사용법:** `titanic.isnull()`는 타이타닉 데이터프레임에서 결측값을 True/False로 반환합니다.

15. **`notnull()`**

    - **기능:** 결측값이 아닌 데이터를 True로 반환합니다.
    - **사용법:** `titanic.notnull()`는 결측값이 아닌 데이터에 대해 True를 반환합니다.

16. **`sum()`**
    - **기능:** 결측값의 개수를 합산합니다.
    - **사용법:** `titanic.isnull().sum()`는 각 열에 대해 결측값의 수를 계산합니다.

### 데이터 인덱싱 및 필터링

17. **`iloc[]`**

    - **기능:** 데이터프레임에서 행과 열의 위치를 기반으로 데이터를 추출합니다.
    - **사용법:** `titanic.iloc[0:5, 0:3]`는 첫 5개의 행과 첫 3개의 열을 추출합니다.

18. **`loc[]`**

    - **기능:** 라벨을 기반으로 데이터를 추출합니다.
    - **사용법:** `titanic.loc[0:5, 'age':'fare']`는 첫 5개의 행에서 `age`와 `fare` 열을 추출합니다.

19. **`apply()`**

    - **기능:** 함수나 로직을 데이터프레임의 각 요소에 적용합니다.
    - **사용법:** `titanic['age'] = titanic['age'].apply(lambda x: x+1)`는 나이에 1을 더한 값을 새로운 `age` 열로 만듭니다.

20. **`map()`**
    - **기능:** 시리즈의 각 요소에 함수를 적용하여 변환된 결과를 반환합니다.
    - **사용법:** `titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})`는 성별을 0과 1로 변환합니다.

### 고급 시각화

21. **`sns.pairplot()`**

    - **기능:** 데이터프레임의 각 변수 간의 관계를 시각화하는 페어플롯을 생성합니다.
    - **사용법:** `sns.pairplot(titanic, hue='sex')`는 성별에 따른 변수 간 관계를 페어플롯으로 시각화합니다.

22. **`sns.distplot()`**

    - **기능:** 데이터의 분포를 시각화하는 히스토그램을 생성합니다.
    - **사용법:** `sns.distplot(titanic['age'])`는 나이 분포를 히스토그램으로 시각화합니다.

23. **`sns.barplot()`**
    - **기능:** 평균이나 합계와 같은 요약 통계를 시각화하는 막대그래프를 생성합니다.
    - **사용법:** `sns.barplot(x='pclass', y='survived', data=titanic)`는 클래스별 생존율을 막대그래프로 시각화합니다.

### 추가적인 유용한 메서드

24. **`pd.crosstab()`**

    - **기능:** 두 개 이상의 범주형 변수 간의 교차표를 생성합니다.
    - **사용법:** `pd.crosstab(titanic['sex'], titanic['survived'])`는 성별과 생존 여부 간의 관계를 교차표로 만듭니다.

25. **`pd.pivot_table()`**

    - **기능:** 데이터프레임의 피벗 테이블을 생성합니다.
    - **사용법:** `pd.pivot_table(titanic, values='survived', index='sex', columns='pclass', aggfunc='mean')`는 성별과 클래스에 따른 생존율 피벗 테이블을 생성합니다.

26. **`sns.jointplot()`**
    - **기능:** 두 변수 간의 관계를 시각화하고, 그 주변에 히스토그램을 포함한 플롯을 생성합니다.
    - **사용법:** `sns.jointplot(x='age', y='fare', data=titanic)`는 나이와 요금 간의 관계를 시각화합니다.
