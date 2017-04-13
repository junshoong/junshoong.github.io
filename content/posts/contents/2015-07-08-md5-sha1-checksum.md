---
title: "MD5, SHA1 체크섬 확인하기"
category: post
tags: encrypt, linux
---
카테고리 구분은 linux에 넣으려고 했지만 아무래도 리눅스보다는 보안 관련인 것 같아서 새로 카테고리를 만들었다.

트리구조는 분류하긴 좋지만 분류할때마다 고민하게 되는 것 같다.


오늘은 리눅스민트에서 md5와 sha1의 checksum을 확인하는 방법을 알아보자.

그 일례로 vmware player를 들어보자. [vmware 사이트의 다운로드 페이지](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/7_0)를 확인해보면 아래와 같은 모습을 볼 수 있다.

![vmware 다운로드 페이지 화면](/images/2015-07-08/01.png)

하단에 보면 `CHECKSUMS` 라고 적혀있고 `MD5SUM`, `SHA1SUM`이라고 적혀있다. 이건 이 파일의 내용을 해당 알고리즘을 통해서 변조한 해쉬값을 나타낸다.

MD5나 SHA1 알고리즘에 대한 정보는 국내 위키에도 잘 나와있다.


간단하게 말하면 웹상에 올라온 파일과 내가 받은 파일이 일치하는지 확인하는게 목적인 값이라고 생각하면 된다.

만약 중간에 파일에 악성코드등의 추가로 인해 파일이 변조가 된다면 저 해시값이 변하게 된다. 그래서 리눅스 터미널에서 간단하게 확인을 해보도록 하자.


다운로드받은 위치에서 마우스 오른쪽 버튼을 눌러 "이 위치로 터미널 열기"를 통해 터미널을 열어주고 아래 키워드를 입력한다.

{% highlight shell %}
$ openssl dgst -md5 VMware-Player-7.1.2-2780323.x86_64.bundle
{% endhighlight %}

openssl dgst 는 자료에 있는 정보를 코드로 변환시켜준다고 생각하면 될 것 같다.

openssl 명령과 관련된 자세한 내용은 [여기](https://www.openssl.org/docs/apps/openssl.html)서 확인 가능하다.



위 메세지를 실행하면 아래와 같이 나온다.



MD5값도, SHA1값도 웹사이트에 올라온 값과 동일하다는 것을 알 수 있다. 이 파일엔 변조가 없을 것으로 추정할 수 있다.

물론 파일이 다르고 해시값이 같은 경우가 있을 수 있고, 그걸 해시 충돌이라고 한다. 그래서 보안을 목적으로는 MD5나 SHA1을 권장하지 않는다고 한다.

하지만 이런 간단한 파일 변조를 확인하는데는 큰 무리가 없어서 널리 사용하는것 같다.


+

_2015.08.18 추가_


간단한 명령어가 있었다.

{% highlight shell %}
$ md5sum [file]
{% endhighlight %}

마찬가지로

{% highlight shell %}
$ sha1sum [file]
{% endhighlight %}

자세한 사항은 해당 명렁어의 도움말을 참고!
