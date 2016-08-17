---
layout: post
title: "[django]travis에서 test시 생기는 데이터베이스 문제"
category: post
tags: python, travis, djagno
---
로컬에서는 별 말 없이 통과하던 테스트가 travis 위에서는 아래와 같은 오류를 뱉으며 실패한다.


>django.core.exceptions.ImproperlyConfigured: Requested setting DATABASES, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.


읽어보면 `DJANGO_SETTINGS_MODULE` 환경변수나 `settings.configure()`를 호출하라는 것 같은데 어떻게 해야할지 막막하다.


여기저기 찾아보다가 해결했다. github에서 아래 `env:` 영역과 같이 수정해주면 된다.

{% highlight yaml %}
language: python
python:
  - "3.4"
  - "3.5"
env:
  - DJANGO_SETTINGS_MODULE=[my_project_name].settings

install: "pip install -r requirements.txt"
script:

  - python manage.py test
{% endhighlight %}

`[my_project_name]` 부분을 `settings.py` 파일이 있는 폴더와 일치시키면 된다. 보통은 프로젝트 명으로 되어 있다.

수정하고 travis-ci를 확인해보니 초록색이 되었다.
