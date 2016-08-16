---
layout: post
title: "apt 패키지 관리 도구로 파이어폭스 마이너 버전 업그레이드"
tags: firefox, linux, apt
---

#배경

django를 테스트하는데 selenium에서 firefox를 열 때 에러가 발생한다. [(관련이슈)](https://github.com/SeleniumHQ/selenium/issues/2110)

확인해보니 FF47.0에서 공통으로 발생하는 문제이고, 47.0.1에서 fix되었다.

기존에 사용하던 파이어폭스는 기본 ppa저장소에서 제공되는걸 받았었는데, 공식 홈페이지에 가니 tar 확장자로만 제공하고 있다. apt-get 을 사용해서 관리하고 싶은데.. 하며 찾아봤더니 방법을 찾았다.


#업그레이드

[파이어폭스설치 관련페이지 지원페이지](https://support.mozilla.org/en-US/kb/install-firefox-linux) 중간쯤에 보면 Installing Firefox on Ubuntu 라고 적힌 링크가 있다. 해당 링크는 [우분투 헬프 페이지](https://help.ubuntu.com/community/FirefoxNewVersion)
로 이동한다.

이 페이지에서는 Security-testing packages 와 Daily updates를 사용하는 방법에 대해 적혀있다. Daily는 매일 업데이트 된 부분을 적용받는 것이고, Security-testing 패키지의 경우에는 업데이트들의 보안검사를 마친 것을 제공해준다. 이런게 모여서 minor버전, major 버전으로 판 올림되어 배포된다고 생각하면 되겠다.

내 경우에는 Security-testing packages 를 통해 업그레이드 하기로 했다. 방법은 아주 간단하다. 해당 ppa를 추가해주고 업데이트 후 업그레이드를 해주면 된다.
{% highlight bash %}
sudo add-apt-repository ppa:ubuntu-mozilla-security/ppa
sudo apt-get update
sudo apt-get upgrade
{% endhighlight %}

다시 파이어폭스를 열어서 버전확인을 해보면 해당 버전으로 판올림 된걸 확인 할 수 있다.
