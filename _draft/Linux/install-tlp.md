Title: [Linux] ThinkPad 랩탑 배터리관리 패키지 (tlp) 설치
Date: 2016-10-31
Category: Linux
Tags: laptop, linux, tlp
Slug: install-tlp
Authors: junshoong

# tlp 설치

이전에도 사용했던 ThinkPad를 위한 배터리관리 패키지인 `tlp`를 설치했다. 그냥 설치해두고 잊어버려도 되는 편리한 패키지였는데 리눅스를 새로 설치하는 김에 다시 받았다. 실제로 체감은 잘 모르겠어서 당분간 써보고 통계자료를 뽑아볼 수 있으면 다시 추가하도록 하겠다. 배터리 사용 관련 그래프를 나타내주는 패키지로는 `gnome-power-manager` 가 있다.


```bash
$ sudo aura -S tlp
$ sudo tlp start
$ sudo aura -S acpi_call
$ sudo systemctl enable tlp.service
$ sudo systemctl enable tlp-sleep.service
$ sudo systemctl mask systemd-rfkill.service
```

자세한 배터리 정보와 상태를 확인할 수 있다.

```bash
$ sudo tlp stat
```

간결한 상태를 보고 싶으면 아래 명령어도 유용하다.

```bash
$ upower -d
```

배터리 사용 history 그래프는 gnome-power-manager로 볼 수 있다.  

```bash
$ sudo aura -S gnome-power-manager
$ gnome-power-statistics
```

![gnome-power-statistics](/images/2016-10-31/1.png)

# 참고 자료

 - [tlp 공식 문서 - arch install](http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html#arch)
 - [ArchWiki - TLP](https://wiki.archlinux.org/index.php/TLP)
 - [Gnome Help - Gnome Power Manager](https://help.gnome.org/users/gnome-power-manager/stable/statistics.html.en)
 - [Arch Forum - Tool for reporting battery stats?](https://bbs.archlinux.org/viewtopic.php?id=169195)
