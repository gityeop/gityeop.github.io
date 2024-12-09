---
title: 맥북 정각마다 차임벨 설정하기
date: 2024-07-24
categories: productivity
tags: ["macos", "settings"]
excerpt: "맥북 정각마다 차임벨 설정하기"
---

단계는 3단계로 나뉜다.

1. 플레이 할 **차임벨 구하기**
2. 차임벨을 울리게 하는 **스크립트** 설정
3. 시간마다 정해진 작업을 수행하기 위한 **crontab** 설정

---

1.차임벨 구하기

인터넷에서 다운받을 수 있는 마음에 드는 차임벨 mp3 파일을 다운 받는다. 개인 용도로 사용할 것이기 때문에 저작권의 위험은 괜찮을 것 같다. 하지만 그래도 찝찝하다면 아래의 사이트에서 무료 차임벨을 다운 받는 것을 추천한다.

[무료 차임벨](https://mixkit.co/free-sound-effects/bell/)

2.스크립트 작성하기

이제 이 차임벨을 울리게 할 스크립트를 작성할 차례이다. 재생은 간단히 **afplay**라는 명령어로 한다. afplay 명령어는 macOS의 기본 제공 유틸리티 중 하나로, 별도로 다운로드하거나 설치할 필요가 없다.

.sh 확장명으로 파일을 만들어준다. 나는 "play_chime.sh"으로 만들었다.

![화면 기록 2024-07-25 00 13 50](https://github.com/user-attachments/assets/ce87d77e-f163-436d-9a5f-72e27eccbc7b)

다운 받은 파일을 오른쪽 클릭하고 옵션 키를 눌러서 **경로 이름**을 복사해두고, play_chime.sh 파일을 열고 아래의 스크립트를 작성해서 afplay 옆에 붙여넣기 해준다.

```bash
#!/bin/bash
afplay /path/to/your/wavfile.wav
```

3.예정된 시간에 스크립트 실행하기

예정된 시간에 스크립트를 실행하기 위해서는 macos의 crontab을 사용해야한다.
사용법이 그리 어렵지 않다.

1. 터미널을 실행한다.
2. "crontab -e"을 붙여 넣어서 contab 파일을 터미널에서 연다.
3. 참고로 vim으로 수정할 수 있어서 익숙하지 않는 사람은 설명대로 한다.
   > vim에 익숙하지 않다면 순서대로 진행한다.
   >
   > 1. crontab -e 엔터
   >    <img width="592" alt="스크린샷 2024-07-25 00 47 03" src="https://github.com/user-attachments/assets/7ef6d520-9c88-4e82-ac39-0381e427e33a">
   > 2. i 눌러서 INSERT 모드 진입
   >   <img width="592" alt="스크린샷 2024-07-25 00 47 16" src="https://github.com/user-attachments/assets/4f72707a-77d2-4b72-9295-98c2db1c4077">
   > 3. 아래의 "0 9-23 ..." 스크립트 cmd+v로 붙여넣기
```
0 9-23 * * * /path/to/your/script.sh
```
   > 4. esc(INSERT 모드 나오기)
   > 5. :wq 입력 후 엔터

위 crontab 스크립트의 형식은 아래와 같다.

- 0 : 분을 나타냄(0-59 가능)
- 9-23 : 시간(0-23 가능)
- \* : 모든 일(1-31)
- \* : 모든 월(1-12)
- \* : 모든 요일(0-7)
- 마지막 : 실행할 스크립트의 인수

---

참고로 crontab을 활용하면 불필요한 데이터를 지우는 작업도 자동화할 수 있어서 cleanmymac의 작업을 부분적으로 대체 가능하다.
