---
title: "[elementary OS] eclipse 실행시 시스템이 멈추는 현상"
category: post
tags: linux, elementary, eclipse
---

eclipse 실행시 OS가 굳어버리는 문제가 있다.


GTK 버전 관련 이슈라고 한다.

실행 파일이 있는 디렉터리를 확인해보면 `eclipse.ini` 라는 설정 파일을 볼 수 있다.

그 eclipse.ini 의 내용에 아래 항목을 추가한다.

{% highlight ini %}
-launcher.GTK_version
2
{% endhighlight %}

다만 추가할 때 `--launcher.appendVmargs`의 윗줄에 추가해야 한다.

이후 실행하면 정상적으로 구동되는 걸 볼 수 있다.

참고로 시스템이 멈췄을 때는 `Alt`+`PrtSc`을 누른 상태에서 `REISUB`를 순서대로 눌러주면 재부팅 된다.

## 참고링크

[Ubuntu : 얼어붙은 시스템에 한방 먹여! (REISUB)](http://nemonein.egloos.com/5280987)  
[Eclipse Mars freezes after splash screen](http://elementaryos.stackexchange.com/questions/1276/eclipse-mars-freezes-after-splash-screen)
