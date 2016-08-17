---
layout: post
title: "[elementary os] ppa repository 삭제하기"
category: post
tags: linux, apt
---
여러 프로그램을 받다보면 자연스레 ppa 가 쌓인다. 이러다보면 한번 정리해주고 싶을때가 온다. 일단 설치된 리스트를 확인해보자.

{% highlight bash %}
ls -al /etc/apt/sources.list.d/
{% endhighlight %}

해당 경로아래 리스트를 확인할 수 있다.
그럼 지워보자.

{% highlight bash %}
sudo add-apt-repository --remove ppa:team/name
{% endhighlight %}

저 뒤에 ppa: 뒷부분은 해당 repository의 이름을 넣어주면 된다.
혹은 GUI 환경에서도 삭제할 수 있다. `Applications > Software & Updates > Other Software`에서 삭제를 진행하면 된다.

![Software & Updates 창](/images/2016-04-02/01.png)

## 참고링크

[How can I get a list of all repositories and PPAs from the command line into an install script?](http://askubuntu.com/questions/148932/how-can-i-get-a-list-of-all-repositories-and-ppas-from-the-command-line-into-an)
[How can PPAs be removed?](http://askubuntu.com/questions/307/how-can-ppas-be-removed)
