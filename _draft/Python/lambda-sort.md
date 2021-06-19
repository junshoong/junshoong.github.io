Title: [Python] lambda를 통한 sort
Date: 2017-04-12
Category: Python
Slug: lambda-sort
Tags: python
Author: junshoong

`lambda`는 익명 함수이다. python 외에도 여러 언어에서 지원하는 expression으로, 짧은 함수를 잠깐 사용할 때 쓸 수 있다.
가장 기본적으로는 아래와 같이 쓴다.

```python
>>> a = lambda x: (x**2)
>>> a(3)
9
>>> a(15)
225
```

`lambda`뒤에 인자를 받고 return 값을 적어준다.
아래와 같이 사용할 수도 있다.

```python
>>> import sys
>>> read = lambda : sys.stdin.readline()
>>> read()
10
'10\n'
```

`sort` 함수의 key로도 사용한다.
```python
>>> l = [1, 5, 4, 2]
>>> l.sort(key=lambda x: x**2)
>>> l
[1, 2, 4, 5]
>>> l=[[1,2],[1,3],[3,2],[2,2],[3,3]]
>>> l.sort(key=lambda x: (x[0],x[1]))
>>> l
[[1, 2], [1, 3], [2, 2], [3, 2], [3, 3]]
```
