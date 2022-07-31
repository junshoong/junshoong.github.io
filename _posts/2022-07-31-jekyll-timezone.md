---
layout: single
title: "github jekyll timezone 설정"
date: "2022-07-31"
categories: "blog"
tags: jekyll github
authors: junshoong
---

github를 통해서 퍼블리싱하고 있는 이 블로그에 timezone 설정이 빠져 있어서 그런지 포스트 등록이 skip되었다.

skip되는 부분은 github action에 build쪽에서 볼 수 있었다.
```
Skipping: _posts/2022-07-31-archlinux-bluetoothctl-on-boot.md has a future date
```

로컬에서는 문제없이 보이던게 github쪽에 가면 보이지 않는 현상이라 \_config.yml에 timezone설정을 해줘봤다.

```
timezone: Asia/Seoul
```

다시 push 했을때는 시간이 이미 지나간 뒤라 잘된건지는 다음에 보면 될것 같다.
