Title: 파이어폭스 언어팩 적용하기
Date: 2015-01-28
Modified:
Category:
Tags:
Slug: firefox-language-pack-config
Authors: junshoong
Summary:


context
---
title: "파이어폭스 언어팩 적용하기"
category: post
tags: firefox, language
---
*deprecate*
> 이글은 윈도우 기준으로 작성되었습니다.  
> 현재(16.08.24) 언어팩은 제공되고 있지 않습니다.  

파이어폭스는 처음 받을 때 언어를 선택해서 받아야 하므로 새로운 언어로 변경하기 위해서는 파이어폭스를 다시 설치해야한다.

그런데 재설치를 하지 않고서 파이어폭스 언어팩을 받으려면 xpi 파일을 받아와야한다. 현재 최신버전에 따른 언어팩은 따로 지원해주지 않는다.
[여기서](http://download.cdn.mozilla.net/pub/mozilla.org/firefox/releases/) 원하는 버전에 접속한 후 해당 OS - xpi 로 들어간다.

![xpi 파일 리스트](/images/2015-01-28/01.jpg)

여기서 원하는 언어를 클릭하면

![적용 경고창](/images/2015-01-28/02.jpg)


위와 같은 창이 나온다. 그럼 적용버튼을 눌러주자.

![소프트웨어 설치창](/images/2015-01-28/03.jpg)

보통은 3~5초정도 대기시간이 있다. 시간이 지나면 마찬가지로 설치버튼을 눌러준다.

주소창에 `about:config` 를 치고 고급설정으로 들어간다.

![고급설정 경고화면](/images/2015-01-28/04.jpg)


경고창이 나오는데, 고급설정을 수정할경우 치명적일 수 있다는 얘기다.

수정할 것만 수정하고 모르는건 건들지 말자.

![고급설정 변경 화면](/images/2015-01-28/05.jpg)

위와 같이 `general.useragent.locale` 를 검색해서 해당 값을 아까 .xpi 파일의 이름으로 바꿔 준다 .

예를 들면 `en-US` / `en-GB` / `ko` 이런 식으로.

껏다가 키면 적용 완료 !
