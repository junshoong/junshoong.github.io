Title: [vim] 새 파일 작성시 자동으로 템플릿(구조) 불러오기
Date: 2015-11-23
Modified:
Category:
Tags:
Slug: vim-auto-template
Authors: junshoong
Summary:


context
---
title: "[vim] 새 파일 작성시 자동으로 템플릿(구조) 불러오기"
category: post
tags: vim
---
vim으로 html 파일을 만들 때마다 구조를 새로 적어주려니 손목에 통증이 생겼다. 새 파일을 만들 때마다 자동으로 템플릿을 작성해주면 좋겠다 싶어서 한참을 검색했었는데, 검색 키워드를 vim new file format으로 하니 나오 질 않았다. 조금 더 찾다가 vim new file template으로 검색해서 결과를 얻어냈다.


홈 디렉터리에 있는 `.vimrc`를 열어서 수정하자.

{% highlight vim %}
au BufNewFile *.html 0r ~/.vim/html.skel
au BufNewFile *.sh 0r ~/.vim/sh.skel
{% endhighlight %}

그리고 해당 경로에 원하는 형식의 Template를 작성해둔다.


html.skel
{% highlight html %}
 <!DOCTYPE html>
 <html>
     <head>
         <title> </title>
         <meta charset='utf-8' />
     </head>
     <body>
     </body>
 </html>
{% endhighlight %}

sh.skel
{% highlight shell %}
#!/bin/bash
{% endhighlight %}


앞으로 파일을 만들 때 `.html`이나 `.sh` 확장자를 가지는 파일은 위와 같은 템플릿을 가지는 걸 확인할 수 있다.



## 참고자료

[Stackoverflow - How can I automatically add some skeleton code when creating a new file with vim](http://stackoverflow.com/questions/162617/how-can-i-automatically-add-some-skeleton-code-when-creating-a-new-file-with-vim)
