Title: [Python] 프로그램 시간 체크하기
Date: 2017-04-26
Category: Python
Tags: python, time
Slug: time-check
Authors: junshoong

```python
import timeit

s = timeit.default_timer()

some_progress()

e = timeit.default_timer()
print(e-s)
```
위와 같이 특정 처리에 걸린 시간을 확인할 수 있다.
