---
title: Inter Rater Metrics
date: 2024-10-29
categories: machine-learning
---

## 주요 Metric: Cohen's Kappa, Fleiss' Kappa, Krippendorff's Alpha

데이터 분석이나 머신러닝 프로젝트에서 레이블링 작업을 진행할 때, 여러 명의 평가자가 동일한 데이터에 대해 일관된 레이블을 붙이는 것이 매우 중요하다. 평가자들 사이의 일치도를 평가하기 위해 다양한 메트릭이 사용되는데, 그중에서도 Cohen's Kappa, Fleiss' Kappa, 그리고 Krippendorff's Alpha는 대표적인 지표들이다.

### 1. Cohen's Kappa

Cohen's Kappa는 두 명의 평가자 간의 일치도를 측정하는 메트릭이다. 이 지표는 단순히 일치한 비율을 계산하는 것에서 더 나아가, 우연에 의해 일치할 가능성을 보정해준다. 예를 들어, 두 명의 영화 리뷰어가 영화의 장르를 분류한다고 가정하자. 각 리뷰어는 영화를 "코미디", "액션", "드라마" 중 하나로 분류한다. 이때 두 평가자의 평가가 얼마나 일관적인지를 확인하기 위해 Cohen's Kappa를 사용할 수 있다. 만약 두 명의 리뷰어가 100개의 영화 중 80개의 영화에 대해 같은 장르를 선택했다면, 이 단순 일치율은 80%다. 하지만 이 중 일부는 우연히 맞았을 가능성도 있다. Cohen's Kappa는 이러한 우연의 영향을 보정하여 실제로 얼마나 일치도가 높은지를 나타낸다.

Cohen's Kappa의 수식은 다음과 같다:

$$
\kappa = \frac{p_0 - p_e}{1 - p_e}
$$

여기서,

- $p_0$ : 관찰된 일치율 (실제로 평가자들이 일치한 비율)
- $p_e$ : 우연에 의해 일치할 것으로 예상되는 비율

### 2. Fleiss' Kappa

Fleiss' Kappa는 Cohen's Kappa와 비슷하지만, 여러 명의 평가자가 있을 때 사용된다. 예를 들어, 5명의 의사들이 50명의 환자에 대해 특정 질병의 진단을 내린다고 가정해보자. 각 환자에 대해 동일한 진단을 내릴 수도 있고, 서로 다른 진단을 내릴 수도 있다. 이때 Fleiss' Kappa를 사용하면 여러 명의 평가자가 특정 환자에 대해 얼마나 일관된 판단을 내렸는지를 평가할 수 있다. Fleiss' Kappa는 평가자가 3명 이상일 때, 즉 다수의 평가자가 관여하는 상황에서 일치도를 측정하는 데 유용하다. 이를 통해 여러 전문가의 의견이 얼마나 합치되는지를 정량적으로 파악할 수 있다.

Fleiss' Kappa의 수식은 다음과 같다:

$$
\kappa = \frac{\bar{P} - \bar{P_e}}{1 - \bar{P_e}}
$$

여기서,

- $ \bar{P} $ : 전체 평가자들의 평균 일치율
- $ \bar{P_e} $ : 우연에 의한 기대 일치율

### 3. Krippendorff's Alpha

Krippendorff's Alpha는 평가자 간 일치도를 측정하는 데 있어 가장 유연한 지표 중 하나다. 이 지표는 데이터의 종류에 관계없이 사용할 수 있다. 즉, 범주형 데이터뿐만 아니라 순서형, 간격형 데이터 등 다양한 데이터 타입에 대해 적용이 가능하다. 예를 들어, 4명의 문학평론가가 10개의 소설에 대해 각각 "매우 좋음", "좋음", "보통", "나쁨", "매우 나쁨"과 같은 등급을 매긴다고 하자. 이때 각 평론가의 평가가 얼마나 일관성 있는지를 측정하기 위해 Krippendorff's Alpha를 사용할 수 있다. Krippendorff's Alpha는 평가자가 일관성 있게 판단했는지뿐만 아니라, 다양한 데이터 타입을 다룰 수 있기 때문에 여러 종류의 데이터 분석에서 유용하게 사용된다.

Krippendorff's Alpha의 수식은 다음과 같다:

$$
\alpha = 1 - \frac{D_o}{D_e}
$$

여기서,

- $ D_o $ : 관찰된 불일치 정도
- $ D_e $ : 우연에 의해 예상되는 불일치 정도

### 어떤 지표를 사용해야 할까?

- **Cohen's Kappa**는 평가자가 두 명인 경우에 적합하다. 예를 들어, 두 명의 교사가 학생들의 시험 답안을 평가할 때 사용하면 좋다.
- **Fleiss' Kappa**는 세 명 이상의 평가자가 있는 상황에 적합하다. 여러 명의 의사나 전문가가 동일한 데이터를 평가할 때 유용하다.
- **Krippendorff's Alpha**는 데이터 타입에 구애받지 않고 일관성을 평가해야 할 때 사용된다. 예를 들어, 텍스트 데이터, 숫자 데이터, 등급 데이터 등 다양한 타입의 데이터를 평가하는 경우에 활용된다.
