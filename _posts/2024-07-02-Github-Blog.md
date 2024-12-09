---
title: Github Blog 만들기(2024)
date: 2024-07-02
categories: github-blog
excerpt: "깃허브 블로그 만들기"
tags: ["blog", "jekyll"]
---


참고 영상
	[테디노트 깃헙(GitHub) 블로그 10분안에 완성하기](https://www.youtube.com/watch?v=ACzFIAOsfpM)
### 1. 블로그 만들기
1. 간단하게 만들기 위해서 유명한 테마를 **fork**한다
	1. [minimal-mistakes 테마](https://github.com/mmistakes/minimal-mistakes) 접속
	![image](https://i.imgur.com/drg0ivT.png)
	2. 복사된 리포지토리로 들어가서 **Settings** → **General** → **Repository name**을 **“내 ID.github.io”** 이 형식으로 수정해서 입력한다.
	   ![image](https://i.imgur.com/FkPnUhl.png)
	3. **\_config.yml"** 파일로 들어가서 **Site Setting**의 **url** 부분을 수정한 **Repository name**으로 수정하고 **Commit Changes..**를 누른다.
	   ![image](https://i.imgur.com/3ooQTrR.png)
	   ![image](https://i.imgur.com/mEKOdHd.png)
	4. “**내 ID.github.io**”로 설정한 해당 주소로 들어가보면 블로그가 개설되었다.
	   ![image](https://i.imgur.com/ytmDcdk.png)

### 2. 글 게시하기
1. **Create new file** 로 새로운 파일을 만들고 파일 이름의 형식을 “**YYYY-MM-DD-제목.md**”로 설정하고 **Front matter**를 설정하고 그 아래에 내용을 작성한다.
- Front matter

\---

title: "The second post"

date: 2024-06-29

\---

![image](https://i.imgur.com/QhJUuoS.png)
	
   ![image](https://i.imgur.com/5jpqUV0.png)
> 발생할 수 있는 오류 
> 1. future : true
> 
> 현재 날짜를 제목과 date에 입력하고 글을 작성했을 때 블로그에 글이 게시되지 않는 상황이 발생할 수 있다. 이럴 때는 **-config.yml**에 **future: true**라는 값을 추가해준다. GitHub 블로그는 Jekyll이라는 정적 사이트 생성기를 사용하는데 Jekyll은 블로그 게시물의 날짜를 기준으로 게시 여부를 결정한다. Jekyll의 기본 설정은 future: false로 되어 있어, 미래 날짜의 게시물이 기본적으로 게시되지 않는다.
> ![image](https://i.imgur.com/bxBvWaC.png)

> 2. 포스트 클릭해서 보면 레이아웃이 깨짐
>
> 참고한 영상에서는 layout: post를 front matter에 넣었지만 현재 front matter에 layout: post를 입력하면 글을 클릭했을 때 사이트 레이아웃이 깨진다. 나같은 경우는 아래처럼 깨졌다.
> ![image](https://i.imgur.com/bcFuRmv.png)
> 글을 클릭해서 들어갈 경우(아래 그림)
> ![image](https://i.imgur.com/klLa9I9.png)
> 해결 방법 : front matter에서 layout: post를 지운다



   
