## Data Preprocessing

데이터 전처리의 다양한 기법
? 왜 Zero-centering을 해줘야 하는가?

1. Zero-centering & Normalization
   - 모든 입력값이 양수 일 때, sigmoid function과 비슷한 상황이 존재
   - 데이터의 평균을 빼는 것은 zero-centering에 도움이 됨
   - normalize하기 위해 표준편차로 나눠준다.
2. Why Zero-cnetering
   - weight의 작은 변화에 덜 민감해짐
   - optimize하기 쉬움
3. PCA(Principle Component Anlaysis) & Whitening
   - PCA: 데이터를 정규화하여 zero-center을 만들고 축을 정렬
   - Whitening: covariance 행렬을 만듬. 각각의 축을 같은 중요도를 가지게 만든다.(정규분포를 따르도록)
4. Data Augmentation
   - 실제 데이터셋의 양이 적기 때문에 데이터의 의미에 영향을 주지 않고 각각의 데이터들을 수정하는 방법
     - 큰 데이터 셋은 돈이 많이 들기 때문
   - classifier는 불변해야 함

## Data Augmentation

1. Horizontal Flips
   - 수평으로 뒤집어도 고양이를 인식할 수 있음
   - 수직으로 뒤집으면 의미가 왜곡될 수 있음
2. Random Crops
   - classifier가 부분만 보더라도 고양이라고 인식하기를 바람
   - Translation invariance: 몇 개의 픽셀만 이동하더라도 비슷하다고 인식하는 것
   - 다른 유형의 데이터에도 비슷하게 적용됨: audio, video, text, sequence...
3. Scaling
   - 스케일의 크기를 키워도 물체를 인식할 수 있어야함
   - Scaling + Random Crops 사용 가능
4. Random Crops and Scaling
   - for training:
     - [256, 480] -> 짧은 길이 256
     - 짧은 길이보다 조금 더 작은 조정된 이미지에서 224\*224 패치를 무작위로 샘플링
   - for test:
     - 이미지 크기를 다음 5개 사이즈로 조정. [224, 256, 384, 480, 640]
     - 224\*224 사이즈 이미지 10개를 크롭하여 분류를 진행
     - 이 이미지들의 평균 혹은 최대값을 최종 분류에 사용
5. Color Jitter
   - 빛이나 다른 요인들에 의해 색깔이 다르게 보일 수 있으니 조절한다.
6. Data Augmentation in Practice
   - 문제와 데이터의 영영에 따라 사용하는 방법이 다름
   - Translation, Rotation, stretching, Shearing, Random blocking, Add noise, Mix two images, Apply a filter
