Title: [Django] timezone 설정
Date: 2017-04-19
Category: Django
Tags: django, timezone
Slug: timezone-setting
Authors: junshoong

Django에서 기본적인 DateTimeField를 현재 timezone으로 맞추고 싶다.

settings.py
```python
TIME_ZONE = 'Asia/Seoul'
# USE_TZ = True
```

여기서 `TIME_ZONE`만 수정해주니까 저장되는 값이 달랐다. `USE_TZ`도 comment 해주니 정상적으로 입력되었다.
참고로 Django에서는 [`ISO 8601`](https://www.w3.org/TR/NOTE-datetime) 을 따른다.

