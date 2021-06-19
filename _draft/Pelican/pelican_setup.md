Title: [Pelican] 설치
Date: 2017-04-09	04:25
Category: Pelican
Slug: pelican-setup
Tags: pelican
Author: junshoong

pelican 3.7.1을 설치했다.
```
pip install pelican markdown
pelican-quickstart
```
로 설치를 진행한다.

[simple-bootstrap](https://github.com/getpelican/pelican-themes/tree/master/simple-bootstrap) 테마를 적용했다.

원하는 경로에 테마를 받은 후에 `pelicanconf.py` 파일에 아래와 같이 적어준다.

```python
THEME = "<your_themes_path>/simple-bootstrap"
```



make publish 로 배포를 준비할 경우, 이전에 유지되던 디렉터리가 사라져서 난감했다. 이런 경우에는 `publishconf.py` 파일에 아래와 같이 추가해주자.

```python
DELETE_OUTPUT_DIRECTORY = False
```