---
title: "Arch linux 설치"
category: post
tags:
  - linux
---


![my-arch-linux](/images/2016-10-30/1.png)

# 개요
27일 저녁부터 [Arch linux](https://www.archlinux.org/) 설치를 진행했다. 이전에는 [Elementary OS](http://elementary.io/)를 사용했었는데 어느 정도 리눅스에 익숙해지기도 했고 사용하던 HDD를 SSD로 바꾸려고 계속 계획을 해 왔기에 이참에 Arch 를 설치해봤다. 이 기회를 빌어 결심부터 설치까지 여러 도움을 준 [@youngbin](https://youngbin.xyz/) 에게 감사한다.

# Arch linux Download & Write

먼저 [Arch linux Downloads 페이지](https://archlinux.org/download/)에서 파일을 받는다. torrent나 kaist mirror등을 통해서 직접 받는다. 그리고 적당한 usb에 write 해준다. [USB flach installation media](https://wiki.archlinux.org/index.php/USB_flash_installation_media)를 참고해보면 usb에 굽는 여러 방법을 보여준다. 내 경우에는 이미 linux를 사용하고 있기 때문에 별다른 유틸리티 없이 구울 수 있었다. 처음엔 `gnome-disk-utility`를 통해서 구웠는데 부팅시 문제가 발생해서 `dd`명령을 통해서 다시 구워줬다.  

```bash
$ sudo fdisk -l
$ sudo dd bs=4M if=/path/to/archlinux.iso of=/dev/sdb && sync
```

먼저 `fdisk`를 통해서 구울 usb의 이름을 확인하고 진행한다. 내 경우에는 `sdb` 였지만 다른 경우가 있을 수 있으므로 확실히 확인 후 진행한다. 이후 usb를 다시 꼽고 재부팅을 진행한다. 부팅시 usb로 부팅을 진행하도록한다.  

# Live Booting

처음에는 그래픽화면이 나오면서 메뉴를 확인할 수 있다. 상단에 있는 `Boot Arch Linux`를 클릭해서 부팅을 진행한다. CLI 환경으로 shell이 뜨는 걸 확인할 수 있다.  

```bash
root@archiso ~ #
```

## 인터넷 연결

내 경우에는 인터넷 연결이 되지 않아서 난감했었는데 LAN선을 직접 연결해서 잡아주면 된다.

```bash
# ip addr
# systemctl start dhcpcd@<interface name>
```

인터넷이 연결 확인은 `ping` 명령을 통해서 확인하는게 좋다. wireless LAN을 사용해서 진행하고 싶기 때문에 `wifi-menu`를 통해서 무선 랜을 잡아줬다. 해당 명령을 입력하는 경우 의존성 패키지가 필요한 경우가 있기 때문에 유선 연결 상태에서 `dialog`, `wpa_supplicant`를 설치해준 뒤에 다시 명령을 실행한다.

## 파티션 설정

그럼 이제 설치를 진행할 디스크의 파티션을 편집해주자. `fdisk`를 통해서 파티션을 확인한다. 내 `/dev/sda` 등으로 잡혀있는걸 확인 할 수 있다. 연결된 경우에는 `umount`로 마운트를 해제해주고 `cfdisk` 툴을 사용해서 파티션을 편집해주었다.

```bash
# fdisk -l
# umount /dev/sda*
# cfdisk /dev/sda
```

검은 화면에 흰 글씨지만 직관적인 화면을 볼 수 있다. 기존에 있는 파티션을 Delete해서 Free Space로 만들고 원하는 대로 파티션을 나눠준다.

| Device | Boot | Size | Type |
|--------|------|------|------|
|/dev/sda1|*|230.8G|Linux|
|/dev/sda2||7.7G|Extended|
|/dev/sda5||7.7G|Linux swap / Solaris|

형태로 파티션을 맞춰주고 Write한 후 종료한다.

```bash
# mkfs.ext4 /dev/sda1
# mkswap /dev/sda5
# swapon /dev/sda5
```

이렇게 위와 같이 명령하면 포맷을 진행한다.

```bash
# mount /dev/sda1 /mnt
# mkdir /mnt/boot
```

위 작업을 통해 마운트해준다.  

## mirror 설정

이제 기본적인 작업은 다 되었다. `mirrorlist`를 수정해서 내 네트워크 환경을 맞춰 줘야한다.

```bash
# vi /etc/pacman.d/mirrorlist
```

필요없는 부분을 다 지우고 Korea에 해당하는 mirror만 남겨주면 된다.

## 패키지 설치

```bash
# pacstrap /mnt base
# genfstab -U /mnt >> /mnt/etc/fstab
```

base 패키지를 설치해주고 부팅시 해당 디스크를 읽을 수 있게 작업해준다.

```bash
# arch-chroot \mnt
```
루트를 바꿔주고 작업한다.

## 기타 설정

```bash
# ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
# hwclock --systohc
# locale-gen
```

기타 Localization을 진행해준다.

```bash
# passwd
# vi /etc/hostname
# vi /etc/hosts
```
root 계정 password와 hostname을 지정해준다.
해당 내용은 [Wiki의 Hostname부분](https://wiki.archlinux.org/index.php/Installation_guide#Hostname)을 참고한다.

```bash
# mkinitcpio -p linux
```
램파일시스템에 대한 설정을 해준다. 정확히 무슨 역할을 하는지는 잘 모르겠다.

## 부트로더 설치

```bash
# pacman -S grub-bios
# grub-install --target=i386-pc /dev/sda
# grub-mkconfig -o /boot/grub/grub.cfg
```
부트로더를 설치해준다. `grub`을 사용하는 경우 이렇게 설치해주면 된다.

## 재부팅

```bash
# exit
# umount -R /mnt
# reboot
```

부트로더까지 설치가 완료되었으면 접속을 종료하고 재부팅한다. 재부팅시에는 usb를 뽑고 진행하면 된다.


# 환경 구축하기

재부팅이 되었으면 먼저 __root__로 로그인해준다.

## 유저생성하기

```bash
# useradd -m -G wheel -s /bin/bash harvey
# passwd harvey
# visudo
```

계정을 생성하고 `visudo`를 통해서 sudo권한을 부여해준다.

## GUI 환경 설치

```bash
# pacman -S dialog wpa_supplicant networkmanager
# pacman -S xf86-video-intel xorg-server gdm gnome gnome-shell
# pacman -S xterm
# systemctl enable gdm.service
# systemctl enable NetworkManager
```

첫번째 명령은 와이파이 연결을 위해서 설치해줬던 패키지와 네트워크매니저 패키지를 설치해준다. 두번째는 video card를 잡아주고, Display Server와 Display Manager, Desktop 환경을 설치해준다. 세번째는 xterm이라는 터미널을 설치해준다. 내 경우에는 처음에 gnome-terminal이 켜지지 않아서 난감했었다. 마지막 두 라인은 시작시 자동으로 실행되도록 등록해준다.  
재부팅하면 gnome 환경으로 로그인 할 수 있다.

## 터치패드 설정

```bash
# sudo pacman -S xf86-input-libinput
```
만약 작동하지 않는다면 `-R` 명령으로 지우고 `xf86-input-synaptics`를 설치해준다.

## 기타 설치

이외에 필요한 패키지들을 아래와 같이 설치했다. pacman을 통해서는 기본적인 패키지만 설치할 수 있고, AUR에 있는 패키지를 설치하는 경우에는 Helper인 [yaourt](https://archlinux.fr/yaourt-en)나 [aura](https://github.com/aurapm/aura)를 사용할 수 있다. 나는 aura을 사용해서 아래 패키지들을 받았다.
`slack-desktop`, `gnome-tweak-tool`, `ibus`, `ibus-hangul`, `openssh`, `ttf-d2coding`, `ttf-monaco`, `jdk8-openjdk`, `pycharm-professional`, `atom`, `ntfs-3g`, `eclipse-jee`, `insync`, `pushbullet`, `cups`, `hplip`, `ttf-nanumgothic_coding`
git을 통해서 설치 `powerline/fonts`, `vaporize93/dotfiles`, `VundleVim/Vundle.vim`, `aura-bin(AUR)`, `terminix(AUR)`

# References
__ArchWiki__  

 - [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)
 - [Network configuration](https://wiki.archlinux.org/index.php/Network_configuration)
 - [Wireless Network configuration](https://wiki.archlinux.org/index.php/Wireless_network_configuration)
 - [GRUB](https://wiki.archlinux.org/index.php/GRUB)
 - [General recommendations](https://wiki.archlinux.org/index.php/General_recommendations)
 - [Users and groups](https://wiki.archlinux.org/index.php/Users_and_groups)
 - [AUR helpers](https://wiki.archlinux.org/index.php/AUR_helpers)
 - [Pacman (한국어)](https://wiki.archlinux.org/index.php/Pacman_(%ED%95%9C%EA%B5%AD%EC%96%B4))
 - [CUPS](https://wiki.archlinux.org/index.php/CUPS)

__Etc__  

 - [박정규님의 블로그 - Arch Linux 설치과정 정리 - Part I](http://bagjunggyu.blogspot.kr/2014/07/arch-linux-part-i.html)
 - [박정규님의 블로그 - Arch Linux 설치과정 정리 - Part II](http://bagjunggyu.blogspot.kr/2014/07/arch-linux-part-ii.html)
