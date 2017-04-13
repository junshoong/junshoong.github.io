---
title: "[elementary OS] lenovo e450 FreeDos에 Install"
category: post
tags: linux, elementary, lenovo
---
기존에 사용하던 HP430을 떠나보내면서 민트에서 elementary로 갈아타보기로 했다. [공식 홈페이지](https://elementary.io/)에서 파일을 받을 수 있다. 금액이 적혀있는데, 구매하고 싶으면 금액을 선택해서 하고, 아니면 custom에 0을 입력하고 받으면 된다.

한글 입력기 관련 이슈를 설명해둔 [박정규님 블로그](http://bagjunggyu.blogspot.kr/2015/12/2015.html)다. 항상 새로운 리눅스를 도전하시는 것 같은데 참고하면 큰 도움이 된다. 아직 해당 사항은 적용해보지 않았다. [elementary os 포럼](https://elementaryforums.com)도 존재한다. 여타 리눅스 버전보다 작은 규모다. 현재 상황을 볼 수 있는 [런치패드](https://translations.launchpad.net/elementary)도 존재한다. 번역, 버그, 이슈 등등의 트래킹서비스를 제공한다.

어디서 새로 얻어온 노랑 미니언즈 usb 4gb에 담아서 설치하기로 했다. `usb-creator-gtk`, `mintstick`, `dd` 모두 실패 했다.

아무래도 잘 안 되서 공식 홈페이지에 가보니 [설치관련 정보](https://elementary.io/docs/installation#creating-an-installation-medium)가 있다. 따라서 UNetbootin 이라는 프로그램을 사용했지만 역시 실패했다. 무슨 문제지.. 싶어서 다른 USB랑 동시에 시도하기로 했다. 다른 USB에서 mintstick으로 레코딩 했더니 잘 됬다. USB의 부트 영역이 망가진 것 같다. 아마 이전에 민트를 설치했던 문제와 비슷한 게 아닐까..

[2015/07/05 - [linuxmint] 17.2 Cinnamon 설치]http://harveyk.me/130

BIOS로 진입하거나 Booting 메뉴를 고르기 위해선 처음에 `Enter`를 누르면 된다. `F1`은 BIOS, `F12`는 Booting Menu로 연결 된다. 참고로 `Enter` 누를 때 비프음이 상당히 컷다. 영어 환경 / 위치 서울 / 한글 자판으로 설치를 진행했다.

> 8gb swap    -> sda1  
> 나머지 /       -> sda2  
> 부트로더는 sda에 설치를

![인스톨관련 문제 화면](/images/2016-03-06/01.jpg)

... 하는데 문제가 생겼다.

>Unable to install GRUB in /dev/sda2
>
>Executing 'grub-install /dev/sda2' failed.  
>This is a fatal error.

부트로더를 sda2로 바꿔서 다시 설치했지만 똑같은 오류로 fail.. 오류창에 있는 키워드로 구글링을 좀 해보니 askubuntu에 관련 글을 볼 수 있었다.

## 참고링크
 - [I receive the error 'grub-install /dev/sda failed' while attempting to install Ubuntu as the computer's only OS.](http://askubuntu.com/questions/143678/i-receive-the-error-grub-install-dev-sda-failed-while-attempting-to-install-u)
 - [“Unable to install GRUB in /dev/sda” when installing GRUB](http://askubuntu.com/questions/459620/unable-to-install-grub-in-dev-sda-when-installing-grub)
 - [Ubuntu installation failure - Unable to install GRUB](http://askubuntu.com/questions/532540/ubuntu-installation-failure-unable-to-install-grub)

내 경우는 BIOS에서 `QUICK boot` 모드를 disable 시키고, livebooting해서 install 하니까 정상적으로 설치 되었다.

![elementary os 바탕화면](/images/2016-03-06/02.png)
