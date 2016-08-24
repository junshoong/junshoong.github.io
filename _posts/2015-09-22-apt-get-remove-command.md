---
layout: post
title: "apt-get 제거 명령어 정리"
category: post
tags: linux, shell
---

`apt-get`으로 신나게 많은 프로그램을 설치했었다.

그런데 필요 없어진 패키지는 어떻게 삭제할까?

아래와 같이 세가지 방법이 있다.

{% highlight shell %}
$ sudo apt-get remove <package>
{% endhighlight %}

<package>에 해당 패키지를 입력하면 삭제할 수 있다.

다만 설정 파일은 남겨둔다.

{% highlight shell %}
$ sudo apt-get autoremove <package>
{% endhighlight %}

remove와 같은데, 설치하면서 같이 설치된 다른 package들 중 사용하지 않는 package들도 같이 삭제해준다.

{% highlight shell %}
$ sudo apt-get purge <package>
{% endhighlight %}

설정 파일도 삭제해준다.
