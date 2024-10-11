---
title: fzf로 명령어 history 쉽게 보기
date: 2024-10-10
categories: productivity
---

1. fzf 설치

   `sudo apt install fzf`

2. `history | tac | fzf --height 50% --layout=reverse --border`

   그럼 이렇게 뜬다

   ![Image](https://i.imgur.com/3LKD7qp.png)

3. alias 설정
   나는 `h`로 했다.

   `alias h='history | tac | fzf --height 50% --layout=reverse --border'`
