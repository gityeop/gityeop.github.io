---
title: Mac Window Management 맥북의 윈도우를 설정하는 앱들
date: 2024-08-17
categories: productivity
---

## Rectangle | Magnet...

## yabai + skhd

### Aerospace로 갈아탄 이유

yabai의 모든 기능을 사용하려면 **System Integrity Protection(시스템 무결성 보호)을 비활성화**해야한다.

나 같은 경우는 space를 만들어서 **여러개의 space**를 활용하려고 했기 때문에 **SIP 비활성화**가 필요했다.

그래서 [yabai documetation](https://github.com/koekeishiya/yabai/wiki/Disabling-System-Integrity-Protection)을 따라 SIP를 비활성화하고 설정을 해보았지만 여전히 적용되지 않았고, 이러한 설정의 오류를 고치기 위해 방법을 찾다가 시간이 너무 많이 소비되어 결국 yabai를 사용하지 않게 되었다.

그리고 초기 학습 비용이 비교적 낮은 Aerospace로 넘어갔다.

## Aerospace + Rectangle

[Aerospace](https://github.com/nikitabobko/AeroSpace)는 yabai에 비해 비교적 적은 초기 학습 비용을 가지고 여러개의 space를 생성하여 활용할 수 있는 Window Management app이다

yabai를 버리고나서 그냥 맥의 기본 space 관리 기능을 사용하려고 했으나 기존 **desktop 전환 애니메이션이 불편**해서 기본 space 관리 기능을 사용하지 않게 되었다.
![Image](https://i.imgur.com/qt7xJzz.png)

Reduce motion을 활성화하면 전환 애니메이션이 줄어드나, 그래도 역시 딜레이가 있다.
![Image](https://i.imgur.com/AgfgwZA.png)

## Aerospace 사용법

자세한 Aerospace 사용법은 [AeroSpace Guide](https://nikitabobko.github.io/AeroSpace/guide#exec-env-vars)를 보기를 추천한다.

그리고 최근에 Mac app에 대해 업로드하는 해외 유튜버인 Josean Martinez에서 Aerospace 영상을 업로드했기 때문에 [이 영상](https://www.youtube.com/watch?v=-FoWClVHG5g&t=1066s)을 참고 바란다.

자주쓰는 기능만 소개하자면

1. Tiles Mode

윈도우가 가진 화면을 최대한 다 사용가능한 모드이다.

mac의 window는 기본적으로 **floating 모드**로 되어있어서 창을 띄워서 사용하는 방식이다.

반면에 Aerospace는 Tile Mode를 지원하기 때문에 새로운 프로그램이나 창을 띄우면 기존에 사용하고 있는 공간의 절반을 차지해서 나란히 볼 수 있게 되어있다.

![Image](https://i.imgur.com/rmgTyDN.png)

간단한 단축키 설정으로 창이 차지하는 비율을 조절할 수 있다.

2. Floating mode

Tile mode로 사용하다가 floating mode가 필요한 앱들이 있다. System Setting이라던지 간단히 팝업처럼 띄워서 사용할 앱들이 이런 경우이다.

나 같은 경우는 **Hyperkey + T**를 눌러서 Tile/ Floating을 Toggle 할 수 있도록 하였다.

그리고 항상 Floating mode로 켤 앱은 아래의 설정을 config에서 추가하여 설정할 수 있다.

```
[[on-window-detected]]
if.app-id = 'com.apple.calculator'
run = 'layout floating'  # 계산기

[[on-window-detected]]
if.app-id = 'org.pqrs.Karabiner-Elements.Settings'
run = 'layout floating'  # Karabiner-Elements

[[on-window-detected]]
if.app-id = 'com.apple.systempreferences'
run = 'layout floating'  # 시스템 설정

```
