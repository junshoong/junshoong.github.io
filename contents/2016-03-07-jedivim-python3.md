---
title: "[vim] (미해결) jedi-vim을 통한 python3 자동완성"
category: post
tags: python, vim, plugin
---

python3를 vim을 사용해서 코딩을 하는데, 자동완성 기능이 있으면 좋을 것 같아 찾아봤더니 [jedi-vim](https://github.com/davidhalter/jedi-vim)을 많이 사용한다.

Pathogen 과 Vundle 사이에서 문제가 조금 생겼지만, 결국 Vundle을 통해서 jedi-vim을 적용하는데 성공했다. 그런데 조금 알아보니 환경변수에 적용된 기본 python을 기준으로 자동완성을 제공한다. 하지만 시스템에 기본 적용된 python의 버전이 2.7이기 때문에 python3로 자동완성하기 위해선 설정을 조금 바꿔줘야 한다.

그 부분은 [설명서](https://github.com/davidhalter/jedi-vim/blob/master/doc/jedi-vim.txt#L479)에 내용이 나와 있었다.

`~/.vimrc` 파일에 아래 내용을 추가해주면 된다.
{% highlight vimrc %}
let g:jedi#force_py_version = 3
{% endhighlight %}

하지만 이 부분에서 또 새로운 문제가 발생했다. 16년 3월 7일 현재 열려있는 [이슈](https://github.com/davidhalter/jedi-vim/issues/488)로, 해당 사항과 동일한 문제가 발생한다. 에러 메세지를 따라가

`.vim/bundle/jedi-vim/initialize.py`

이부분에서 문제가 생기는 것 같아 조금 조사해보니.. vim에서 python3랑 호환이 되지 않는 부분이 좀 있는 것 같다.

특히 python2 와 3를 병행해서 사용하는 경우에 vim에서는 그 중 한가지만 사용할 수 있도록 지원하는 것 같다.

### 참고링크
 - [What's the easiest way to get Vim with Python 3 support?](http://askubuntu.com/questions/585237/atwhats-the-easiest-way-to-get-vim-with-python-3-support)
 - [How to enable python3 in vim?](http://stackoverflow.com/questions/15801243/how-to-enable-python3-in-vim)
 - [jedi-vim issue #526](https://github.com/davidhalter/jedi-vim/issues/526)
 - [Import vim in python gives back errors](http://stackoverflow.com/questions/13477264/import-vim-in-python-gives-back-errors)

vim 쪽에서도 이 문제로 대화가 진행되고 있다.
[Debian Bug report logs - #729924](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=729924)

위에서 참고해 보니 `pi-rho/dev PPA` 를 추가해서 vim을 업데이트 하면 두가지를 같이 사용할 수 있다고 하는 듯 하다. 그런데 그게 안되더라.. 그래서 위에 있는 askubuntu의 내용을 따라하기로 했다. 그런데 deb package를 build하는 도중에 test87 Failed라며 빌드가 안 되는 것이다. 너무 돌아온 것 같아서 처음으로 돌아가보기로했다. 일단 python명령의 환경변수를 수정해서 python3에 연결시켜보기로했다.
{% highlight bash %}
$ alias python=python3
{% endhighlight %}
이것은 단순히 커맨드에서 "python" 이라고 입력하는걸 :python3"로 입력되도록 하는거라 python기본경로인 `/usr/bin/python`의 심볼릭링크 경로를 python3.4로 붙여줬다.

{% highlight bash %}
sudo ln -sf /usr/bin/python3.4 /usr/bin/python
{% endhighlight %}

그랬지만.. vim 에선 여전히 2.7.6 버전으로 돌아가고 있었다.

일단 이 문제는 해결되지 않은 채로 남겨둔다..

시간나면 Pathogen으로 다시 받아봐야겠다.

일단은 이슈 #488 을 Subscribe하고 기다려야겠다.
