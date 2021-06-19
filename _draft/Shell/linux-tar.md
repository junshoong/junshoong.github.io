Title: [Shell] tar 명령어로 압축하기/압축풀기
Date: 2015-10-20
Category: Shell
Tags: linux, shell
Slug: linux-tar
Authors: junshoong

```bash
$tar -zcvf 압축.tar.gz *
```
이러면 현재 디렉토리에 있는 모든 파일을 압축한다.

```bash
$ tar -zxvf 압축.tar.gz
```

이러면 알아서 풀린다.

여기서 tar 명령어의 옵션을 살펴보자


> -z  gzip gunzip을 사용해서 압축하고 압축을 해제한다.  
> -c 파일을 모은다. create  
> -x 파일을 푼다. extract  
> -v 진행 상황을 본다. verbose  
> -f 입/출력을 파일로 지정해준다.  


-f 명령어가 유의해야 할 점인데, f 명령어가 있기 때문에 파일로 입력, 출력을 할 수 있다.
더불어서 앞에있는 zcxv 는 순서가 별로 상관 없지만 (x랑 c는 같이 쓰면 안 된다.) f는 맨 나중에 있어야 한다.

만약 tar -zcfv  라고 하면 f 뒤에 있는 v 를 파일로 인식하려고 한다.
