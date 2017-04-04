---
title: "atom 에디터의 UI font-size 변경"
category: post
tags:
  - linux
  - atom
  - ui

---

## 문제상황

노트북의 화면 해상도가 너무 높아 실제로 보이는 화면의 글씨가 너무 작아서 보기가 불편하다.


## 환경

- Atom    : 1.15.0
- Electron: 1.4.15
- Chrome  : 53.0.2785.143
- Node    : 6.5.0

## 해결

`~/.atom/styles.less` 파일을 수정해준다.

```css
html, body, .tree-view, .tab-bar .tab {
    font-size: 15px;
}
```

font-size의 값은 적당히 원하는 값으로 넣어주면 된다. 파일을 저장하면 atom 에디터의 font-size가 실시간으로 바뀐다.

## 참고 링크

- [atom issue #2530 - Anyway to change UI/tab/tree view font size? ](https://github.com/atom/atom/issues/2530)
