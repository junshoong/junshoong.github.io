Title: [Linux] apt-get 제거 명령어 정리
Date: 2015-09-22
Category: Linux
Tags: linux, shell, apt
Slug: apt-get-remove-command
Authors: junshoong

`apt-get`으로 신나게 많은 프로그램을 설치했었다.

그런데 필요 없어진 패키지는 어떻게 삭제할까?

아래와 같이 세가지 방법이 있다.

```bash
$ sudo apt-get remove <package>
```

<package>에 해당 패키지를 입력하면 삭제할 수 있다.

다만 설정 파일은 남겨둔다.

```bash
$ sudo apt-get autoremove <package>
```

remove와 같은데, 설치하면서 같이 설치된 다른 package들 중 사용하지 않는 package들도 같이 삭제해준다.

```bash
$ sudo apt-get purge <package>
```

설정 파일도 삭제해준다.
