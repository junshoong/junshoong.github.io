Title: [Linux] elementaryOS 터미널 속성 수정하기
Date: 2016-03-08
Category: Linux
Tags: linux, elementary, terminal
Slug: linux-terminal-configuration
Authors: junshoong

Elementary OS는 Pantheon-terminal 을 사용한다. Pantheon-termainal은 따로 속성을 수정하는 도구를 제공하진 않고 있어서 dconf editor 등으로 속성값은 변경해야 한다. 일단 해당 툴을 받아야 한다. 터미널을 열고 아래를 입력해서 dconf-tools를 설치한다.

```bash
$ sudo apt-get install dconf-tools
```

그리고 슬링샷(`Alt`+`F2`)을 열어서 `dconf editor`를 찾아서 연다.

`org -> pantheon -> terminal -> settings` 로 들어가서 원하는 부분을 수정한다.

![dconf Editor 화면](/images/2016-03-08/01.png)


내 경우에는 opacity(투명도)와 foreground를 조금 수정했다.


색상이 적용되지 않는 경우에는


`~/.bashrc` 파일을 수정하면된다.

```bashrc
  47 # uncomment for a colored prompt, if the terminal has the capability; turned
  48 # off by default to not distract the user: the focus in a terminal window
  49 # should be on the output of commands, not on the prompt
 -50 # force_color_prompt=yes
 +50 force_color_prompt=yes
```

라인 수는 개개인 마다 다를 수 있다. `force_color_prompt=yes`의 주석을 제거 해주면 된다.

이외에도 터미널의 테마를 변경하는건 [Gogh 프로젝트](https://github.com/Mayccoll/Gogh)를 참고할 수 있다.

## 참고링크

[Change colors for the Pantheon terminal emulator](http://unix.stackexchange.com/questions/141066/change-colors-for-the-pantheon-terminal-emulator)
