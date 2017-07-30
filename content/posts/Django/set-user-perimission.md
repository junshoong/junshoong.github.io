Title: [Django] User에게 권한 부여하기
Date: 2017-04-21
Category: Django
Tags: django, 
Slug: set-user-permission
Authors: junshoong


코드 몇줄로 간단하게 권한을 부여할 수 있다.

```python
user = User.objects.get(username='testuser')
perm = Permission.objects.get(codename='model.add_model')
user.user_permissions.add(perm)
```

여기서 주의할 점은 적용되긴하지만 `has_perm`등으로 확인하면 해당 권한이 없다고 나온다는 점이다. 이는 캐싱되어 있는 정보때문에 그렇다. 캐시를 지우거나 인스턴스를 새로 불러오면 올바르게 적용된걸 확인할 수 있다.
아래와 같이 해결할 수 있다.

```python
del user._perm_cache
del user._user_perm_cache
# OR
user = User.objects.get(id=10)
```

아래 링크를 참고할 수 있다.
- [stackoverflow - Pytest-django: set user permissions](http://stackoverflow.com/questions/42220272/pytest-django-set-user-permissions)
