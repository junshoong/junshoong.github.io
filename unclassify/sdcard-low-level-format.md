Title: SD카드 로우레벨 포맷 및 OS 부팅 디스크 만들기
Date: 2015-08-18
Modified:
Category:
Tags:
Slug: sdcard-low-level-format
Authors: junshoong
Summary:


context
---
title: "SD카드 로우레벨 포맷 및 OS 부팅 디스크 만들기"
category: post
tags: linux, shell, sdcard
---

라즈베리 파이에 사용하던 microSD를 포맷하고 새롭게 OS를 설치하려고 한다.

{% highlight shell %}
$ sudo fdisk -l
{% endhighlight %}

위 명령어로 현재 시스템에서 인식하고 있는 디스크를 확인할 수 있다.

일반적으로 sda 는 사용하고 있는 하드일 것이고, sdb 나 usb, mmcblk0 등을 확인할 수 있다.

필자의 경우에는 `/dev/mmcblk0`였고, 파티션이 분리되어 있어서 `/dev/mmcblk0p1`,`mmcblk0p2`로 나뉘어져 있었다.

{% highlight shell %}
$ sudo umount /dev/mmcblk0*
{% endhighlight %}

(\*은 모든 항목을 말한다, mmcblk0*은 mmcblk0로 시작하는 모든 항목이다.)

('u' mount 다 'un' mount 가 아니다.)

언마운트 해주는 게 맞는지 잘 모르겠다. 필자의 경우엔 언마운트 후에 작업하려고 하니까 읽기 오류가 나타났다.

{% highlight shell %}
$ sudo dd if=/dev/zero of=/dev/mmcblk0
{% endhighlight %}

깨끗하게 포맷이 되었으면 iso파일을 집어넣어 보자

{% highlight shell %}
$ sudo dd if=./so.iso of=/dev/mmcblk0
{% endhighlight %}

위 명령어는 현재 디렉토리의 `so.iso` 파일을 포맷이 완료된 sd카드에 복사하는 것이다.

위에 `dd` 명령어 대신에 `dcfldd`라는 명령어를 대신 사용할 수 있는데, 이는 현재 진행상황을 간단하게 볼 수 있는 이점이 있다.

작업이 완료되었다. 다시 마운트를 해보면 완료된걸 확인할 수 있다.

다만 나는 이렇게 했는데 라즈베리 파이에서 부팅이 안된다. 라즈비안 OS는 잘 올라가는걸로 보아 내가 원하는 os는 라즈베리파이와 잘 맞지 않나 보다.

## 참고자료

- [Linux Mint(리눅스 민트)와 Ubuntu(우분투)의 터미널에서 usb 시동 디스크 만들기,usb 로우포맷,파티션 나누기(partition),포맷하기(format)](http://blog.daum.net/bagjunggyu/91)
