Title: [Docker] Arch linux에서 Docker로 Oracle Database 사용하기
Date: 2016-11-22
Category: Docker
Tags: linux, docker, oracle, db
Slug: arch-docker-oracle
Authors: junshoong

# 개요

학교 수업으로 오라클 11g를 사용하고 있는데, 아치리눅스에 설치가 쉽지 않아보여서 미루고 있었다. Windows를 가지고 있지 않아 그간 프로젝트실에 있는 Windows 10으로 실습을 진행하고 있었다. 하지만 주말마다 실습을 위해 학교에 와서 하는게 여간 번거로운게 아니었다. 이러던 참에 최근 스터디하고 있는 Docker를 사용하면 되겠다 싶어서 얼른 찾아봤더니 아니나 다를까 Docker로 Oracle을 띄울 수 있는 것이다. 그래서 이렇게 진행하게 되었다.

# Docker 설치

```bash
# pacman -S docker
# systemctl start docker.service
```

`aura` 를 사용한다면 `aura -S docker`로도 받을 수 있다. 설치가 완료되면 서비스를 실행해준다.

# Oracle Express Edition 11g 이미지 받기

```bash
$ docker pull wnameless/oracle-xe-11g
$ docker images | grep oracle
```

![pulling oracle docker image](/images/2016-11-22/01.png)

![oracle docker image](/images/2016-11-22/02.png)

이미지의 총 크기는 2.2G로 이미지를 받아오는데 10분이 안 걸렸다.

# 컨테이너 실행

```bash
$ docker run -d --name oracle -p 49160:22 -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true wnameless/oracle-xe-11g
```


[DockerHub 저장소](https://hub.docker.com/r/wnameless/oracle-xe-11g/
)에 가면 설치와 기본적으로 설정된 내용들을 확인할 수 있다. 위에 보이는 `-p` 옵션은 `<host_port>:<container_port>`로 포트를 연결해준다.

# Oracle Client 설치 및 접속

Host 시스템에서 Docker로 띄운 Oracle Server로 접속하기 위해서 클라이언트를 사용한다. 클라이언트는 `oracle-instantclient-sqlplus`를 사용하는데, AUR 패키지를 받는 경우에는 홈페이지에서 따로 zip 파일을 받아줘야 하는 번거로움이 있다.  
`/etc/pacman.conf` 파일을 열어서 아래 내용을 하단에 추가해준다.

```conf
[oracle]
SigLevel = Optional TrustAll
Server = http://linux.shikadi.net/arch/$repo/$arch/
```

oracle서버의 사용 약관을 동의한다면 위 내용을 추가해주는 걸로 pacman을 통해 패키지을 제공받을 수 있다. 아래는 AUR 에서 패키지를 받아서 실행하면 나타나는 메세지이다.

```
==> Warning: This software cannot be downloaded automatically.
    You will need to sign up for an Oracle account and download the software from
    Oracle directly.  Place the downloaded file in the same directory as the
    PKGBUILD and re-run makepkg.

    The source .zip files can be downloaded from:

    i686   - http://www.oracle.com/technetwork/topics/linuxsoft-082809.html
    x86_64 - http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

    Alternatively, unofficial prebuilt Arch packages are available by adding the
    following lines to /etc/pacman.conf, if you agree to the Oracle licence[1]:

      [oracle]
      SigLevel = Optional TrustAll
      Server = http://linux.shikadi.net/arch/$repo/$arch/

    Then run 'pacman -Sys oracle' to see available packages.

    [1]: http://www.oracle.com/technetwork/licenses/instant-client-lic-152016.html
```

위 내용을 인지했으면 `pacman`을 이용해서 다시 패키지를 받아보자.

```bash
# pacman -Sys oracle
# pacman -S oracle-instantclient-sqlplus
```

이제 sqlplus로 DB server에 접근할 수 있다.

```bash
$ sqlplus system@localhost:49161
```
![sqlplus connection](/images/2016-11-22/03.png)

# Oracle SQL Developer 설치 및 접속

sqlplus는 여러모로 사용하기가 불편하다. 이를 보완하기 위해서 사용하는 gqlplus 등이 있지만 이 역시 CLI를 기반으로 하기 때문에 스크립트를 짜긴 불편하다. 그런데 위에서 pacman에 오라클 저장소를 추가하면서 생긴 sqldeveloper가 보인다. 이는 Windows에서도 사용할 수 있는 프론트엔드 툴로 GUI 환경에서 사용할 수 있다.

```bash
# pacman -S oracle-sqldeveloper
```

네트워크에 따라 다르지만 한국기준으로 한시간 가량 소요되기 때문에 충분한 시간을 가지고 진행하도록하자.  
설치가 완료되면 JDK PATH를 설정해줘야 한다. 이 프로그램은 JDK7 지원하지만 8에서도 큰 무리없이 작동하는걸로 보인다.  
`~/.sqldeveloper/4.0.0/product.conf` 파일을 열어서 아래 내용을 추가해준다.

```conf
SetJavaHome /usr/lib/jvm/default
```

Arch linux의 기본 JAVA PATH는 저 경로이나 혹시 다른 jdk 버전을 사용한다면 해당 경로를 등록해준다. 다시 sqldeveloper를 실행하면 프로그램이 잘 실행되는걸 볼 수 있다.

![oracle sqldeveloper](/images/2016-11-22/04.png)

> 만약 중간에 setting을 받아올지에 대한 창이 뜨면 No 를 선택하고 지나가면 된다.

프로그램이 실행되면 왼쪽 `connections` 탭에서 새로 연결을 추가해준다. 우리가 실행하고 있는 oracle container에 접속하자. 접속에 대한 계정 정보는 [여기서](https://hub.docker.com/r/wnameless/oracle-xe-11g/
)얻을 수 있다.

![oracle sqldeveloper setting](/images/2016-11-22/05.png)

이제 접속해서 Oracle 11g를 사용할 수 있다.

# 참고자료
 - [http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter20/28](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter20/28)
 - [https://wiki.archlinux.org/index.php/Oracle_client](https://wiki.archlinux.org/index.php/Oracle_client)
 - [https://wiki.archlinux.org/index.php/java](https://wiki.archlinux.org/index.php/java)
 - [https://hub.docker.com/r/wnameless/oracle-xe-11g](https://hub.docker.com/r/wnameless/oracle-xe-11g)
