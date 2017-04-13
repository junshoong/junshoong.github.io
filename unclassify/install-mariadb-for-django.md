Title: MariaDB를 사용해서 Django개발 환경 만들기
Date: 2016-11-03
Modified:
Category:
Tags:
Slug: install-mariadb-for-django
Authors: junshoong
Summary:


context
---
title: "MariaDB를 사용해서 Django개발 환경 만들기"
category: post
tags:
    - mariadb
    - django
---

# 개요

django는 기본적으로 sqlite3를 지원한다.  
project/settings.py 를 확인해보면 아래와 같은 부분을 확인할 수 있다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

`sqlite3` 대신 `mariadb`를 사용하는 방법을 알아보도록하자.

# MariaDB 설치

먼저 `mariadb`를 받는다.

```bash
$ # arch linux command (aura 대신 pacman을 사용할 수 있다.)
$ sudo aura -S mariadb
```

`mariadb`는 `mysql`이 oracle에 인수되고 나서 fork되어 나온 DBMS로 이름만 다를 뿐 기존의 mysql과 호환된다. 때문에 명령어나 다른 라이브러리들을 사용할때도 mysql이라고 적힌 부분을 많이 볼 수 있다.

```
$ sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

위 명령어로 데이터베이스를 설치해줄 수 있다. 이후 바로 데이터베이스를 사용하려는 경우 아래와 같은 에러가 출력된다.

```
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/run/mysqld/mysqld.sock' (2 "No such file or directory")
```

이런 경우엔 `mysql` 서버가 시작되지 않아서 생기는 문제로

```bash
$ sudo systemctl start mariadb.service
```

이런식으로 서비스를 시작해주면 된다.

```bash
$ sudo mysql_secure_installation
```

명령으로 간단히 보안 설정을 해줄 수 있다. remote에서 root 접근 금지나 익명 사용자 사용 여부들을 interactive하게 설정해준다.

# MariaDB 설정

```bash
$ mysql -u root -p
```

위 명령으로 mariaDB에 접근할 수 있다. 위에서 언급했듯이 명령어는 mysql로 접속하지만 mariaDB라고 적힌 화면을 볼 수 있다.
![접속화면](/images/2016-11-03/01.png)

```mysql
MariaDB [(none)]>
```

이런 화면이 나오면 maridDB에 정상적으로 접근한 것이다. 이제 원하는 SQL문을 입력해서 데이터베이스를 사용할 수 있다.

```sql
> CREATE DATABASE djangomaria CHARACTER SET UTF8;
> CREATE USER dmuser@localhost IDENTIFIED BY 'dmpassword';
> GRANT ALL PRIVILEGES ON djangomaria.* TO dmuser@localhost;
> FLUSH PRIVILEGES;
```
![생성화면1](/images/2016-11-03/02.png)
![생성화면2](/images/2016-11-03/03.png)

순서대로 데이터베이스 생성, 유저 생성, 권한부여를 해준다. 그럼 데이터베이스에서 설정은 마무리되었다.  

# Django 설치 및 설정

이제 django쪽을 보자. 먼저 virtualenv로 격리된 환경을 구성하고 django를 설치한다. 이 포스트에서는 virtualenv에 대한 자세한 내용은 생략하도록 하겠다.

```bash
$ pip install virtualenv
$ mkdir ~/djangomaria
$ cd ~/djangomaria
$ virtualenv venv
$ source venv/bin/activate
$ # (venv) username@hostname ~/djangomaria$ 와 같은 모습을 보인다.
$ pip install django mysqlclient
$ django-admin.py startproject djangomaria
$ vim djangomaria/djangomaria/settings.py
```

vim이나 nano와 같은 편집기를 이용해서 settings.py를 수정해준다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

이 항목을 아래와 같이 수정한다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangomaria',
        'USER': 'dmuser',
        'PASSWORD': 'dmpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

```bash
$ cd djangomaria/
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

브라우저를 열어서 `localhost:8000/admin`에 접속하면 로그인 화면이 나온다. 여기에 createsuperuser에서 입력했던 id, pw를 치고 들어가면 admin페이지를 확인할 수 있다.

# 연동 확인

이제 연결이 완료되었으니 정말로 데이터베이스에 저장되었는지 확인해보자.

```bash
$ mysql -u dmuser -p
Enter password:
```

```sql
connect djangomaria;
select * from auth_user;
```
![결과화면](/images/2016-11-03/04.png)

우리가 createsuperuser에서 등록했던 계정 정보가 나오는걸 볼 수 있다. 성공적으로 연결되었다.

# 참고자료
- [ArchWiki - MySQL](https://wiki.archlinux.org/index.php/MySQL)
- [ArchWiki Forums - How to start MySQL](https://bbs.archlinux.org/viewtopic.php?id=158393)
- [DigitalOcean Community - How To Use MySQL or MariaDB with your Django Application on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)
- [MariaDB - CREATE USER](https://mariadb.com/kb/en/mariadb/create-user/)
- [블로그 몽개구리 - Django 에 MySQL 혹은 MariaDB 연동하기](http://zafertop.tistory.com/2)
- [블로그 권남 - MySQL 기본 명령어 정리](http://kwon37xi.egloos.com/1634694)
- [블로그 너머 - DB TABLE 목록 조회](http://darkhorizon.tistory.com/313)
