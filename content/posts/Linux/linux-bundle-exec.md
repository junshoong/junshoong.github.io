Title: [Linux] elementaryOS GUI환경에서 *.bundle 파일 실행이 안 될 때
Date: 2016-03-07
Category: Linux
Tags: linux, elementary
Slug: linux-bundle-exec
Authors: junshoong

mint에서는 잘 되었던 것 같은데 elementary OS에서는 bundle파일이 클릭으로 실행이 안 된다.  
그냥 터미널을 열고 실행권한을 준다음 실행하면 된다.

```bash
$ chmod 755 *.bundle
$ sudo ./*.bundle
```

\* 은 파일 이름이다.
