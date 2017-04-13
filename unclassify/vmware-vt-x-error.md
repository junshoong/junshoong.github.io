Title: 64비트 환경의 Guest OS를 구동시 생기는 문제해결(VT)
Date: 2015-08-18
Modified:
Category:
Tags:
Slug: vmware-vt-x-error
Authors: junshoong
Summary:


context
---
title: "64비트 환경의 Guest OS를 구동시 생기는 문제해결(VT)"
category: post
tags: vmware, bios
---
![vmware error 화면](/images/2015-08-18/01.jpg)

vmware를 통해서 Security Onion을 설치하려는 데 위와 같은 경고 창이 나타났다.


>This virtual machine is configured for 64-bit guest operating systems.  
>However, 64-bit operation is not possible.  
>This host supports Intel VT-x, but Intel VT-x is disabled.  
>...  


그러니까.. 가상머신으로 64비트 게스트OS 돌리려면 호스트가 지원하는 Intel VT-x를 enable 하라는 소리인 것 같은데..

VT, 뭔가 익숙하다. BIOS에서 본 것 같다. HP 노트북 기준으로 부팅 시 `F10`을 눌러 BIOS에 접속한다.

![bios 화면](/images/2015-08-18/02.jpg)

BIOS의 System Configuration에 보니까 Virtualization Technology가 있다. Disabled 되어 있는 부분을 Enable로 수정해준다.

다시 재부팅해서 vmware를 돌려보자.

![security Onion 화면](/images/2015-08-18/03.png)

좋아. 정상적으로 잘 부팅되는 걸 확인할 수 있다.


일부는 여기에서 도움을 얻었다.

[http://vmware.com/info?id=152](http://vmware.com/info?id=152)
