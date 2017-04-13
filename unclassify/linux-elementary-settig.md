Title: [elementary OS] 초기 설치 셋팅
Date: 2016-03-07
Modified:
Category:
Tags:
Slug: linux-elementary-settig
Authors: junshoong
Summary:


context
---
title: "[elementary OS] 초기 설치 셋팅"
category: post
tags: linux, elementary, setting
---
{% highlight bash %}
$ sudo apt-get update
$ sudo apt-get install language-selector-gnome uim uim-byeoru vim tmux libreoffice git
$ sudo add-apt-repository ppa:linrunner/tlp && sudo apt-get update && sudo apt-get install tlp tlp-rdw
# (아래는 Thinkpad의 경우)
$ sudo apt-get install tp-smapi-dkms acpi-call-tools
$ sudo tlp start
{% endhighlight %}

한글 설정은 [박정규님 블로그](http://bagjunggyu.blogspot.kr/2015/04/elementary-os-freya-stable-release.html)를 참고하면 좋겠다. 내 경우는 환경은 영어로 할거라 gnome-language-selector 에서 입력기만 바꿨다.

![Language Support 화면](/images/2016-03-07/01.png)

vim에서 사용하는 vundle 플러그인을 설치해준다.

{% highlight bash %}
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
{% endhighlight %}


이외에 jdk는 오라클 홈페이지에서 받고,  docker는 [공식홈페이지](https://docs.docker.com/engine/installation/linux/ubuntulinux/)를 참고한다.


이클립스는 [che버전](https://www.eclipse.org/che/getting-started/)을 한 번 사용해보고..

docker위에 돌아가는 것 같은데 조금 무리가 가길래 그냥 eclipse-mars를 설치했다.

그런데 eclipse 실행시 운영체제가 뻗어버리는 문제가 생겼다. 이 부분은 다음에 포스팅.
