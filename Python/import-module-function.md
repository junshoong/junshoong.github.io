Title: [Python]import_module을 사용해서 import 하기
Date: 2017-05-01
Category: Python
Tags: python, package
Slug: import-module-function
Authors: junshoong

python에서 숫자 등으로 시작하는 패키지를 import 할때는 주의해야한다.

```python
import 1234
from 1234 import abc
```

위와 같이 숫자로 된 파일은 에러를 뱉을 뿐 import 되지 않는다.
그럴 땐 아래와 같이 한다.

```python
import importlib

importlib.import_module('1234')
p = importlib.import_module('1234')
p.abc()
```

위와 같은 작업으로 import를 진행할 수 있다.

참고링크
- [python docs](https://docs.python.org/3/library/importlib.html#importlib.import_module)
- [stackoverflow - In python, how to import filename starts with a number](http://stackoverflow.com/questions/9090079/in-python-how-to-import-filename-starts-with-a-number)
