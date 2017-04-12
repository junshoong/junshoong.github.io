---
title: "pacman failed to commit transaction 해결"
category: post
tags:
  - archlinux
  - pacman
  - troubleshooting
---



docker-compose를 설치하다가 종속된 패키지의 일부가 충돌해서 설치가 진행되지 않았다. 아래는 해당 내용을 간단하게 정리했다.



> aura는 aur 패키지들을 받을 수 있는 pacman의 확장 프로그램으로 본 포스트에서는 pacman으로 대체해도 아무런 상관이 없다.



```bash
$ sudo aura -S docker-compose 
resolving dependencies...
looking for conflicting packages...

Packages (11) python-cached-property-1.3.0-2  python-colorama-0.3.7-2
              python-docker-2.0.2-1  python-docker-pycreds-0.2.1-2
              python-dockerpty-0.4.1-2  python-docopt-0.6.2-4
              python-jsonschema-2.5.1-4  python-texttable-0.8.7-2
              python-websocket-client-0.40.0-2  python-yaml-3.12-2
              docker-compose-1.11.1-1

Total Download Size:   0.59 MiB
Total Installed Size:  3.14 MiB

:: Proceed with installation? [Y/n] Y
:: Retrieving packages...
 python-cached-proper...     8.9 KiB  0.00B/s 00:00 [###########################] 100%
 python-colorama-0.3....    21.6 KiB  3.02M/s 00:00 [###########################] 100%
 python-docopt-0.6.2-...    21.2 KiB  6.90M/s 00:00 [###########################] 100%
 python-yaml-3.12-2-x...   137.5 KiB  4.48M/s 00:00 [###########################] 100%
 python-texttable-0.8...    12.7 KiB  0.00B/s 00:00 [###########################] 100%
 python-websocket-cli...    50.2 KiB  4.90M/s 00:00 [###########################] 100%
 python-docker-pycred...     7.0 KiB  2.27M/s 00:00 [###########################] 100%
 python-docker-2.0.2-...   124.4 KiB  7.15M/s 00:00 [###########################] 100%
 python-dockerpty-0.4...    18.6 KiB  4.54M/s 00:00 [###########################] 100%
 python-jsonschema-2....    63.8 KiB  20.8M/s 00:00 [###########################] 100%
 docker-compose-1.11....   139.0 KiB  5.90M/s 00:00 [###########################] 100%
(11/11) checking keys in keyring                    [###########################] 100%
(11/11) checking package integrity                  [###########################] 100%
(11/11) loading package files                       [###########################] 100%
(11/11) checking for file conflicts                 [###########################] 100%
error: failed to commit transaction (conflicting files)
python-jsonschema: /usr/bin/jsonschema exists in filesystem
Errors occurred, no packages were upgraded.
aura >>= Please check your input.
```



archlinux에서 pacman을 사용해서 설치하는 경우 위와 같이 "failed to commit transaction" 에러가 나타나는 경우가 있다. 이 경우 --force 옵션을 추가해서 설치하면 설치가 잘 진행된다.



```bash
$ sudo aura -S --force docker-compose
resolving dependencies...
looking for conflicting packages...

Packages (11) python-cached-property-1.3.0-2  python-colorama-0.3.7-2
              python-docker-2.0.2-1  python-docker-pycreds-0.2.1-2
              python-dockerpty-0.4.1-2  python-docopt-0.6.2-4
              python-jsonschema-2.5.1-4  python-texttable-0.8.7-2
              python-websocket-client-0.40.0-2  python-yaml-3.12-2
              docker-compose-1.11.1-1

Total Installed Size:  3.14 MiB

:: Proceed with installation? [Y/n] Y
(11/11) checking keys in keyring                    [###########################] 100%
(11/11) checking package integrity                  [###########################] 100%
(11/11) loading package files                       [###########################] 100%
(11/11) checking for file conflicts                 [###########################] 100%
(11/11) checking available disk space               [###########################] 100%
:: Processing package changes...
( 1/11) installing python-cached-property           [###########################] 100%
( 2/11) installing python-colorama                  [###########################] 100%
( 3/11) installing python-docopt                    [###########################] 100%
( 4/11) installing python-yaml                      [###########################] 100%
==> Note that even though this package uses libyaml library,
==> slower pure python implementation is used by default.
==> See http://pyyaml.org/wiki/PyYAMLDocumentation
( 5/11) installing python-texttable                 [###########################] 100%
( 6/11) installing python-websocket-client          [###########################] 100%
( 7/11) installing python-docker-pycreds            [###########################] 100%
( 8/11) installing python-docker                    [###########################] 100%
( 9/11) installing python-dockerpty                 [###########################] 100%
(10/11) installing python-jsonschema                [###########################] 100%
(11/11) installing docker-compose                   [###########################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
```

