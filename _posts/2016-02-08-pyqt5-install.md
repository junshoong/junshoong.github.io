---
layout: post
title: "[PyQt5] PyQt5 설치"
category: post
tags: python, linux
---
GUI를 해볼까 하면서 Python GUI를 찾아봤다. 리눅스 환경에도 적절하고, 크로스플랫폼 지원도 한다고 하니, 이게 좋겠다 싶어 받기로 했다. 일단 PyQt는 Qt라는 GUI 개발용 프레임워크를 파이썬으로 사용할 수 있게 해주는 거라고 보면 될 것 같다.

[Qt (프레임 워크) - 위키백과](https://ko.wikipedia.org/wiki/Qt_%28%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC%29)

PyQt는 널리 사용하는 v4와 최신인 v5가 있다. 나는 최신 버전이 좋다. PyQt5를 설치하기로 했다.

[PyQt5 설치 가이드(공식)](http://pyqt.sourceforge.net/Docs/PyQt5/installation.html)

가이드에 보면 나와있듯이 SIP라는 게 필요하다. SIP는 아마 Scripting language Python이 아닐까 싶다.

[SIP (software) - 위키백과(영문)](https://en.wikipedia.org/wiki/SIP_%28software%29)


일단 그럼 , SIP랑 Qt를 받아보자. SIP는 여기서 받을 수 있다. [SIP download](https://riverbankcomputing.com/software/sip/download)

mercurial를 통해서 소스를 받을 수 있는 것 같은데 이쪽은 잘 모르니까, `tar.gz`으로 받았다. shell을 열고, 압축을 풀어주도록 하자. 글 작성 당시 최신 버전은 4.17이다.

{% highlight shell %}
$ tar -xvf sip-4.17.tar.gz
{% endhighlight %}

뭐, 직관적이니까 아래처럼 따라 해보자. 만약 Python3가 아닌 2를 기반으로 한다면 3을 빼주면 된다.


{% highlight shell %}
$ cd sip-4.17
$ python3 configure.py
$ make
$ make install
{% endhighlight %}

Qt5가 필요하다 설치해주자. qt5를 설치하는 건 여러 방법이 있는데, 이게 제일 간단해 보여서 이렇게 설치했다. 사용하다가 필요하면 새로 설치해주면 될 것 같다.


{% highlight shell %}
$ apt-get install qt5-default
{% endhighlight %}

기본적으로 필요한 건 모두 설치되었다. 그럼 이제 다시 PyQt로 돌아가자. SIP와 같게 설치를 진행하면 된다. [PyQt download](https://riverbankcomputing.com/software/pyqt/download5)

기본적으로 GPL 라이센스를 따르기 때문에 이름이 이런가 보다


{% highlight shell %}
$ tar -xvf PyQt-gpl-5.5.1
{% endhighlight %}

마찬가지로 아래처럼 따라 해보자.


{% highlight shell %}
$ cd PyQt-gpl-5.5.1
$ python3 configure.py
$ make
$ make install
{% endhighlight %}

이제 설치는 완료 되었다. tutorial 할만한 걸 찾아보니까, 공식 reference 문서에는 따로 없는 듯 하고, zetcode라는 사이트에서 괜찮은 tutorial을 발견했다. 아무래도 기본적인 건 한번 따라 해보는 게 익숙해지기 좋을 것 같다.


[zetcode.com PyQt5 tutorial](http://zetcode.com/gui/pyqt5)
