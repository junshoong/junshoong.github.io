Title: [Python] selenium 3 + FireFox50 사용시 발생하는 geckodriver관련 에러 해결
Date: 2017-01-09
Category: Python
Tags: python, troubleshooting, selenium, test, firefox
Slug: selenium3-FireFox50-geckodriver-error-solve
Authors: junshoong

## 문제

selenium과 firefox를 사용해서 테스트를 진행하는 도중 아래와 같은 에러가 발생했다.

```python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.python.org")

assert 'Python' in browser.title

browser.quit()
```

```bash
$ python functional_test.py
```

```python
Traceback (most recent call last):
  File "/home/harvey/venvs/dbproject/lib/python3.5/site-packages/selenium/webdriver/common/service.py", line 74, in start
    stdout=self.log_file, stderr=self.log_file)
  File "/usr/lib64/python3.5/subprocess.py", line 947, in __init__
    restore_signals, start_new_session)
  File "/usr/lib64/python3.5/subprocess.py", line 1551, in _execute_child
    raise child_exception_type(errno_num, err_msg)
FileNotFoundError: [Errno 2] No such file or directory: 'geckodriver'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "functional_test.py", line 3, in <module>
    browser = webdriver.Firefox()
  File "/home/harvey/venvs/dbproject/lib/python3.5/site-packages/selenium/webdriver/firefox/webdriver.py", line 140, in __init__
    self.service.start()
  File "/home/harvey/venvs/dbproject/lib/python3.5/site-packages/selenium/webdriver/common/service.py", line 81, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 

Exception ignored in: <bound method Service.__del__ of <selenium.webdriver.firefox.service.Service object at 0x7f117dff9668>>
Traceback (most recent call last):
  File "/home/harvey/venvs/dbproject/lib/python3.5/site-packages/selenium/webdriver/common/service.py", line 173, in __del__
    self.stop()
  File "/home/harvey/venvs/dbproject/lib/python3.5/site-packages/selenium/webdriver/common/service.py", line 145, in stop
    if self.process is None:
AttributeError: 'Service' object has no attribute 'process'
```

로그를 살펴보면 `geckodriver`가 없고, 이것을 `PATH`에 등록해주어야 하는걸로 보인다. 

`geckodriver`는 `selenium`에서 사용하는 `webdriver`와 `firefox`에서 최근에 사용하기 시작한 `marionette` 라는 자동화 드라이버를 연결해준다. 

이를 위해 처음 설정 부분부터 정리해보자.



## selenium 설치

```shell
$ virtualenv venv
$ source venv/bin/activate
$ pip install selenium
```



## geckodriver 설치

github의 geckodriver저장소에서 파일을 받을 수 있다. [#github mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.13.0)

적당한 경로에 압축을 풀어주고 환경변수에 등록해준다. 내 경우에는 홈디렉터리에 builds 디렉터리를 만들고 그 안에 파일을 뒀다. 환경변수는 `zsh`을 사용하고 있기 때문에 `/home/harvey/.zshrc`파일에 경로를 추가해줬다. 참고로 파일의 경로를 직접 지정하는게 아니라 __파일이 들어있는 디렉터리의 경로__를 지정해주어야 한다.

```shell
...
export PATH=$PATH:/home/harvey/builds
...
```

```shell
$ source .zshrc
```

바로 적용하기 위해서 파일을 실행해준다. 이후에는 shell을 키면 바로 적용된다.



## 코드 실행

`selenium_test.py`

```python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.python.org")

assert 'Python' in browser.title

browser.quit()
```

> 코드는 맨위와 같다.

이제 다시 실행하면 문제없이 실행된다. 혹은 시스템 환경변수를 추가하지 않고 코드내에서 명시적으로 경로를 지정할 수도 있다.

```python
from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Firefox(excutable_path='/home/harvey/builds/geckodriver')
browser.get("http://www.python.org")

assert 'Python' in browser.title

browser.quit()
```



## 참고자료

- [Python - Selenium in Ubuntu OSError: (Errno 20) Not a directory - Stack Overflow](http://stackoverflow.com/questions/40073548/python-selenium-in-ubuntu-oserror-errno-20-not-a-directory)
- [WebDriver - Mozilla](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)
