Title: [Linux] 리눅스에서 한글포맷 열기
Date: 2016-08-10
Category: Linux
Tags: linux, editor
Slug: linux-hwp-open
Authors: junshoong

리눅스에서는 한글 포맷(.hwp)을 여는게 여간 힘든게 아니다.

작년 상반기까지만 해도 [한글과컴퓨터](http://www.hancom.com/)(이하 한컴)에서 공식뷰어를 제공해줘서 잘 쓰고 있었는데, 어느순간 조용히 넷피스24로 전환되어 웹에서만 볼 수 있게 되었다. 그래서 개인적으로 만들어서 사용하고 있는 뷰어가 있나 찾아다녔다. 하지만 오늘 이런 기사를 봤다. ["리눅스에서 한글(hwp)파일 연다...한컴 '한컴오피스 뷰어 통합 다운로드' 개시"](http://www.etnews.com/20160810000093) 당혹스럽다. 말도 없이 한글뷰어를 내리더니 새로운 서비스를 내놓는 것 마냥 다시 올려뒀다.

![한컴 오피스 뷰어 설치하기 이미지](/images/2016-08-16/01_hancom.png)

리눅스라는 플랫폼이 국내에서 흔하게 쓰이는 플랫폼은 아니지만 얼마 안 되는 리눅스 사용자를 이용해서 혼란스러운 마케팅을 보여주는건 조금 속상하다.

오해하고 있는 사람이 조금 있는데, 한글은 폐쇄적이진 않다. 실제로 .hwp의 한글 포맷은 한컴 공식홈페이지에서 공개하고 있다. 다만 그걸 굳이 다른 뷰어를 만들지 않는 게 문제인것 같다.

한글 뷰어를 잃었을 때 사용했던 도구는 [pyhwp](https://github.com/mete0r/pyhwp)로, hwp 포맷을 odt나 html 포맷으로 변환 할 수 있는 도구였다.

한글 뷰어는 [한컴홈페이지](http://www.hancom.com/office/viewer_usage_guide.jsp)에서 받을 수 있다.

## 참고링크

[한글파일(hwp)을 텍스트(txt) 혹은 웹문서(html)로 변환하자!](http://storycompiler.tistory.com/197)
[리눅스에서 한글 파일(hwp) 파일 변환해서 읽기](http://mytory.net/archives/12797)
[pyhwp Docs](http://pythonhosted.org/pyhwp/ko/intro.html)
