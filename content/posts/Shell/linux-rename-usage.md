Title: [Shell] rename을 사용하여 여러 파일의 이름을 한번에 변경하는 방법
Date: 2016-09-05
Category: Shell
Tags: linux, shell
Slug: linux-rename-usage
Authors: junshoong

리눅스에서는 일반적으로 `mv`를 사용해서 파일명을 변경한다. 하지만 여러 파일의 이름을 변경하기 위해서 `rename`을 사용하기도 하는데, 이를 좀 살펴보자.

```bash
$ man rename
```

이렇게 쳐보면 매뉴얼이 나오고 상단을 보면`Perl Programmers Reference Guide`라는 글자가 있다. rename은 perl의 표현식으로 파일명을 변경해준다.

```bash
$ rename 's/[변경 전 문자]/[변경 후 문자]/' [변경할 파일]
```

위와 같은 형식으로 간단하게 파일명을 변경할 수 있다.  
만약 아래와 같은 텍스트 파일을 가지고 있다면,

```
00.test
01.test  
02.test  
03.test  
04.test  
05.test
06.test  
07.test  
08.test  
09.test  
10.test
```

아래와 같은 명령으로 한 번에 확장자 부분을 `.txt`로 변환이 가능하다.

```bash
$ rename 's/.test/.txt/' *.test
```

이렇게 여러 파일명을 쉽게 바꿀 수 있다.
