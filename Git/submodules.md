Title: [Git] Submodule 사용하기
Date: 2017-04-13
Category: Git
Tags: git
Slug: use-submodule
Authors: junshoong
Summary: git에서 Submodule을 사용해봤다.

단순하게 git repo안에서 `git clone`을 하는 경우 연동이 잘 되지 않는것 같다. `git checkout`등을 하면서 git repo안에 clone 했던 git repo가 날아가버리는 상황도 발생했다. 이럴땐 아래와 같이 하자.
```bash
git submodule add git@github.com:<user>/<repo>.git
```
`.gitmodules`라는 파일이 생성되고 submodule로 등록되었다. push하면 웹상에서도 연결되어 있음을 확인할 수 있다.

더 자세한 도움은 아래 링크에서 받을 수 있다.
- [git-scm docs](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88)
- [꿀벌개발일지 - 서브모듈 이해하기](http://ohgyun.com/711)

