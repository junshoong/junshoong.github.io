Title: blinking 과 flashing의 차이
Date: 2016-01-26
Modified:
Category:
Tags:
Slug: blinking-flashing-diff
Authors: junshoong
Summary:


context
---
title: "blinking 과 flashing의 차이"
category: post
tags: accessbility, english
---
KWCAG를 공부하는 중 원칙 2인 운용의 용이성 중 지침 2.3의 광과민성 발작 예방 관련한 검사 항목 2.3.1 부분 이슈이다.

> 2.3.1 (깜빡임과 번쩍임 사용 제한) 초당 3~50회 주기로 깜빡이거나 번쩍이는 콘텐츠를 제공하지 않아야 한다.

혼란이 오는 부분은 깜빡임과 번쩍임이라는 단어를 같이 사용한다는 점이다. KWCAG는 기본적으로 영문으로된 WCAG를 가져오면서 작성된 점을 미루어 [W3C의 원문](https://www.w3.org/TR/WCAG20)을 찾아나섰다. 문서 안에는 flash와 blink의 의미가 명시되어 있다.

KWCAG에서 보듯이 번쩍임은 Flash를 의미하고, 깜빡임은 Blinking을 의미한다.


>    flash  
>  
>    a pair of opposing changes in relative luminance that can cause seizures in some people if it is large enough and in the right frequency range  
>  
>    Note 1: See general flash and red flash thresholds for information about types of flash that are not allowed.  
>  
>    Note 2: See also blinking.  

번쩍임

상대 밝기가 서로 변화하는 한 쌍이 충분히 크고, 적절한 주파수 범위 내에 있다면, 어떤 사람들에겐 발작을 유발할 수 있다.

Note 1: 허용되지 않는 번쩍임의 유형에 대한 정보를 위해 일반적인 번쩍임와 빨간 번쩍임의 임계 값을 보시오.

Note 2: 깜빡임도 확인하시오.

>    blinking  
>    switch back and forth between two visual states in a way that is meant to draw attention  
>    Note: See also flash. It is possible for something to be large enough and blink brightly enough at the right frequency to be also classified as a flash.  

깜박임

주의를 끌기 위한 의미 있는 방법으로, 두 시각적 상태가 앞뒤로 교차한다.

Note: 번쩍임도 확인하시오. 충분히 크고 적절한 주파수에서 충분히 밝게 깜빡이면 또한 번쩍임으로 분류될 수 있다.



문서를 보면 추측할 수 있듯이,

깜빡임(Blinking)은 단순히 두 가지의 상태가 전환되는 모습을 나타내고, 충분히 크고 밝게 빛나면 번쩍임이라고 볼 수 있겠다. 번쩍임(Flash)에 대한 정보는 자세하게 나와있는데, 상대 밝기부터 번쩍임에 대한 임계 값도 안내 되어있다. 결국, Flash와 Blinking은 그 정도의 차이라고 볼 수 있겠다.



## 참고자료

KWCAG 2.0

http://www.w3.org/TR/2008/REC-WCAG20-20081211/#blinksdef

http://www.w3.org/TR/2008/REC-WCAG20-20081211/#flash-def
