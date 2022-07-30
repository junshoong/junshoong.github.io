---
layout: single
title: "[Linux] ArchLinux Bluetooth 부팅시 사용"
date: 2022-07-31
categories: linux
tags: archlinux bluetooth
authors: junshoong
---

블루투스 마우스를 연결해서 사용하는데, Reboot후에 바로 연결이 되지 않는 모습이 보인다.

bluethooth 관련 서비스는 잘 동작하고 있는데 컨트롤러가 꺼져있어서 나타나는 이슈 이다.

```
bluetoothctl power on
```
으로 직접 켜줄 수 있고, config를 수정해서 부팅시에 사용가능하도록 해줄 수도 있다.

/etc/bluetooth/main.conf의 Policy 부분에 아래 내용을 추가해준다.

```
AutoEnable=true
```
