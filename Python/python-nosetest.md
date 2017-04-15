Title: [Python] nosttest 사용하기
Date: 2016-06-26
Category: Python
Tags: python, test
Slug: python-nosetest
Authors: junshoong
Summary:

깐깐하게 배우는 파이썬 ([Learn the Python hard way](http://learnpythonthehardway.org/))을 공부하는 중에 nose를 설치해서 테스트해야 하는 부분이 있었다. (208page) 그런데 현재 사용하는 노트북의 파이썬 환경이 python 3.4 로 맞춰져 있기 때문에 pip 역시 3버전으로 되어 있다.

nose 를 따로 깔아서 사용하기도 싫어서 조금 찾아봤더니 이런 방법이 있다.

```bash
$ nosttest
```

대신

```bash
$ python -m nose
```

을 사용하면 된다. 만약 python 명령이 3 버전으로 연결되어 있다면

```bash
$ python2.7 -m nose
```

으로 사용한다.

### 참고

[Force Nosetests to Use Python 2.7 instead of 3.4](http://stackoverflow.com/questions/26579670/force-nosetests-to-use-python-2-7-instead-of-3-4)
