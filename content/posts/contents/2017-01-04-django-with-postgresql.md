---
title: "ArchLinux에서 Django + PostgreSQL 설정하기"
category: post
tags:
    - arch
    - linux
    - django
    - postgresql
---



# Django + PostgreSQL

django 프로젝트에서 사용하는 DBMS로 [PostgreSQL](https://www.postgresql.org/)을 사용하도록 한다. 이 가이드에서는 Arch Linux 기준으로 작성되었다. 일부분은 같은 부분이 있겠지만, 설치나 설정에서 다른 경우는 최 하단에 있는 링크나 구글링을 통해서 찾아보길 바란다.



## 설치

```bash
$ sudo aura -Sa postgresql
```

`aura`나 `pacman`으로 `postgresql` 패키지를 설치한다. 



## 설정

```shell
$ sudo -i -u postgres
```

user를 `postgres`로 바꾼다. 

> 만약 sudo를 사용하지 않는 환경이라면 `$ su` `# su - postgres` 를 통해 user을 바꾼다.

```shell
[postgres]$ initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
```

앞에 username이 `postgres`로 바뀐걸 확인할 수 있다.  위 명령어는 DBMS를 초기화 시킨다. 옵션은 아래와 같은 의미를 지닌다.

-  `/etc/locale.conf`에 명시되어 있는 설정으로 적용
-  encoding으로 `UTF8`을 사용
-  data 저장위치로 `/var/lib/postgres/data` 위치를 사용

```shell
$ sudo systemctl start postgresql.service
```

service를 실행한다. 만약 부팅시에 자동으로 실행하기 위에서는 `systemctl enable postgresql.service`를 실행한다.

```shell
[postgres]$ createuser --interactive
```

사용자를 새로 만든다. `--interactive`옵션을 줘서 사용자명과 `superuser role` 사용 여부를 확인한다.

```shell
[postgres]$ createdb -U <db-username> <dbname>
```

데이터베이스를 만든다. `<db-username>`에는 위에서 `createuser` 명령을 통해 입력받은 이름을 넣는다. `<dbname>`에는 원하는 데이터베이스 이름을 입력한다. 

```shell
$ psql -d <dbname>
```

일반 사용자로 데이터베이스에 접근한다.



## Django 설정

프로젝트를 새로 작성하는 경우 프로젝트의 `settings.py`파일의 DB부분을 아래와 같이 수정해준다.

`myproject/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<dbname>',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

`USER`에 개인적으로 만든 사용자인 `<db-username>`를 넣어도 되지만 여기서는 기본 계정인 `postgres`를 넣어두었다. 암호를 따로 지정해주었다면 해당 암호를 넣어준다.

```shell
$ pip install psycopg2
```

`postgresql_psycopg2`를 사용하기 위해서 `psycopg2`패키지를 받아야한다. 프로젝트의 `requirements.txt`에 해당 패키지를 추가해 두었다면 `$ pip install -r requirements.txt` 를 통해서 다른 패키지들과 함께 설치할 수 있다. 

```shell
$ python manage.py migrate
$ python manage.py runserver
```

모든 설정을 마쳤으면 `migrate`하고 테스트 서버를 구동해본다.



## 참고
- [우분투 16.04에서 django에 postgresql 설정하기 (영문)](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04)
- [PostgreSQL 설치 - Django Girls (영문)](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/)
- [PostgreSQL 설치 - Django Girls (한글)](https://jinpark-dg.gitbooks.io/django-girls-extended-tutorial-korean/content/optional_postgresql_installation/index.html)
- [PostgreSQL - ArchWiki (영문)](https://wiki.archlinux.org/index.php/PostgreSQL)


