---
layout: post
title: "[wargame] flee button"
category: post
tags: wargame, html
---

[450p - flee button](http://wargame.kr:8080/flee_button/)

![문제 화면](/images/2016-02-20/01.png)

> click the button!  
> i can't catch

flee는 위험한 상황이나 장소로부터 도망치는 걸 말한다. 버튼을 누르면 된다. 일단 Start

![문제 화면2](/images/2016-02-20/02.png)


검은 화면에 이렇게 적혀있다. 윈도우 + 파폭이나 리눅스 + 크롬에서는 잘 보였는데 왠지 리눅스 + 파이어폭스에선 보이질 않는다. 일단 마우스를 따라다니는 누를 수 없는 버튼이 하나 떠다닌다고 생각하면 될 것 같다. 그럼 코드를 한 번 살펴보자.

![코드 내용 화면](/images/2016-02-20/03.png)


button의 `onclick` 이벤트로 `?key=7c09`로 연결되는 부분이 있다. 특이할 게 없다. 따옴표의 안 쪽 부분을 주소 뒤에 붙여보자.

![결과 화면](/images/2016-02-20/04.png)


key는 ip 등에 따라서 달라지는 것 같다. Flag를 획득했다.
