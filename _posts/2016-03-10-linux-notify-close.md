---
layout: post
title: "[elementary OS] critical notify-send 알림 없애기"
category: post
tags: linux, elementary, terminal
---
터미널에서
{% highlight bash %}
$ notify-send -u critical "Test Notification"
{% endhighlight %}
과 같이 입력하면 알림 창이 자동으로 사라지지 않는다.


이때 알림창 위에 마우스 포인터를 올려주면 X 버튼이 나타나서 알림을 끌 수 있다.

하지만 어떤 프로그램의 창 위에서는 알림창 위에 마우스 포인터를 올려도 x 버튼이 나타나지 않는다. 이때는 바탕화면으로 가서 마우스를 올리면 x 버튼이 나타난다.



Type in Terminal,

{% highlight bash %}
notify-send -u critical "Test Notification"
{% endhighlight %}

In this case, notification don't automatically disappear.


This situation, place mouse pointer on notification, then appear close button.


But, if norification is on any program( firefox, terminal, .. etc.), don't appear close button.

This situation, view the desktop, you can see close button.  
