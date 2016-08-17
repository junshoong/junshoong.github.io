---
layout: post
title: "[github] 원격지에 새 branch를 만들며 push하기"
category: post
tags: git, github
---

>local : master, test  
>origin: master

의 상태에서 master는 서로 같은 시점에 있다. 여기서 local에 test를 만들어 작업하다가 원격지에도 test와 일치하는 새 branch를 만들어 관리하고 싶다.
이런 경우 아래와 같이 처리한다.
로컬저장소의 위치에서
{% highlight bash %}
$ git push origin test
{% endhighlight %}

를 입력한다. origin은 원격 저장소이름이고, test는 원하는 branch 이름이다. 성공하고나면 하단에

>  \* [new branch]   test -> test

라고 적힌 글자를 볼 수 있고, 해당 저장소에 가면 compare & pull request 라고 적힌 버튼이 생긴걸 볼 수 있다. 해당 버튼을 눌러 세부사항을 확인할 수 있고, create 하면 새 branch가 생긴다.

이 일련의 과정이 pull request의 과정이라고 볼 수 있다. 다만 여기서는 branch를 새로 만들었을 뿐이다.
