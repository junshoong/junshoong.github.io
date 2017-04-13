Title: archlinux에서 vmware player가 실행되지 않는 문제 해결
Date: 2017-04-04
Modified:
Category:
Tags:
Slug: archlinux-vmware-player-problem
Authors: junshoong
Summary:


context
---
title: "archlinux에서 vmware player가 실행되지 않는 문제 해결"
category: post
tags:
  - archlinux
  - pacman
  - troubleshooting

---



## 문제상황

최근 archlinux의 패키지를 업그레이드하고 나서 vmware player가 실행되지 않는 문제를 겪었다. 실행시에 잠깐 프로세스가 떴다가 사라지고 아무런 로그를 보여주지도 않고 있었다. 관련 문제는 libpng의 업그레이드에 따른 문제로 libpng 1.6.29버전에서 나타나는 문제다.



## 환경

- VMware Player 12.5.2
- Kernel : 4.10.6-1-ARCH



## 해결

 해당 버전을 없애고 업그레이드 하기전으로 돌아가면 해결된다.

```bash
$ sudo pacman -U /var/cache/pacman/pkg/libpng-1.6.28-1-x86_64.pkg.tar.xz
```

경로는 좀 다를 수도 있긴 하지만 최근에 업그레이드했다면 캐시된 이전 버전의 패키지를 얻을 수 있다.

`-U`옵션을 통해서 해당 버전으로 다운그레이드 해준다. 이후 vmware player를 다시 실행해보면 정상적으로 실행된다. 



## 추가정보

혹시 해당 패키지를 업그레이드하고 싶지 않다면 `/etc/pacman.conf`파일을 수정해서 `IgnorePkg`에 `libpng`를 아래와 같이 추가해주면 된다.

```shell
...
# Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup
IgnorePkg   = lib32-libpng libpng
#IgnoreGroup =
...
```



## 참고 링크

- [vmware workstation 12.5.5 not starting [TEMP FIX]](https://bbs.archlinux.org/viewtopic.php?id=224667)
- [[Solved] Vmware - Launch problem (zlib version ?)](https://bbs.archlinux.org/viewtopic.php?id=224680)

