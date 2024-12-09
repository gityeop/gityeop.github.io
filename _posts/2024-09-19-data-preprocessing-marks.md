---
title: 데이터 전처리 고민흔적 data preprocessing marks
excerpt: "데이터 전처리 체크리스트"
tags: ["ai/data-preprocessing", "ai/data-analysis", "blog/study-notes"]
date: 2024-09-19
categories:
---

train과 dev의 평균과 중간값의 차이
![Image](https://i.imgur.com/OGMnawU.png)

- train의 label 데이터의 평균과 중간값이 모두 dev보다 낮다
  - label 0이 많은 train
  - 골고루 분포되어있는 dev

train 데이터 label의 분포
![Image](https://i.imgur.com/R5ACi17.png)

dev 데이터 label의 분포
![Image](https://i.imgur.com/3T7wniQ.png)

train과 dev 데이터셋의 분포를 맞춰주기 위해 data augmentation이 필요할 것 같다는 생각(data swap)

0을 제외한 나머지에 data augmentation을 하고 난 후의 label 분포
![Image](https://i.imgur.com/mLPwQFd.png)

label 5 데이터의 특징 띄어쓰기, 동의어 사용
-> label 0 데이터 500개를 가져와서 4.8, 5.0의 데이터로 증강하면 어떨까
