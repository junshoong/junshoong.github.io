---
layout: post
title: "리눅스 FireFox에서 flash plugin 업데이트"
category: post
tags: firefox, linux, flash, plugin
---

답은 역시 [공식홈페이지](https://support.mozilla.org/ko/kb/install-flash-plugin-view-videos-animations-games)에서 찾을 수 있었다. 아래와 같이 진행하도록 한다.

* [flashplayer 공식홈페이지](https://get.adobe.com/kr/flashplayer/)에서 왼쪽 하단에서 다운로드를 선택해  tar.gz 로 된 압축파일을 받는다.

* 압축파일을 푼다.
{% highlight bash %}
tar -zxvf install_flash_player_###.tar.gz
{% endhighlight %}

* 압축을 풀어낸 폴더 내부에 있는 libflashplayer.so 파일을 firefox의 plugin 디렉터리에 넣는다.  
{% highlight bash %}
sudo cp libflashplayer.so /usr/lib/firefox-addons/plugins/libflashplayer.so
{% endhighlight %}

* 파이어폭스를 껏다가 켜서 해당 문제가 생겼던 곳에가서 정상 작동하는지 확인 한다.


> 참고: Adobe Flash Player 11.2는 Linux를 지원 플랫폼으로 사용하는 마지막 버전이 될 것입니다. Linux용 Flash Player 11.2의 보안 업데이트는 계속 제공됩니다.

2016년 7월 현재 자동 업데이트는 지원되고 있지 않다. apt 명령으로 인스톨도 안 된다.
그러므로 필요할 때마다 직접 수동 설치를 해줘야 한다.
