Title: jekyll에 django template 입력시 생기는 liquid 문제
Date: 2016-09-09
Modified:
Category:
Tags:
Slug: jekyll-liquid-django-template
Authors: junshoong
Summary:


context
---
title: "jekyll에 django template 입력시 생기는 liquid 문제"
category: post
tags: jekyll, liquid
---
jekyll에서 code highlight 등을 하는데 도움을 주는 {% raw %}`{% syntax %}`{% endraw %} 형식의 태그는 마크다운파일에 그대로 입력하면

> Liquid Exception: Liquid syntax error (line n): Unknown tag 'xxx' in /home/harvey/blog/text.md  
> jekyll 3.1.6 | Error:  Liquid syntax error (line n): Unknown tag 'xxx'  

와 같은 오류를 내면서 해석을 해주지 못한다.
같은 이유로 django의 template에서는 위와 같은 태그를 사용하는데 불편이 생긴다.

이는 이런 식의 템플릿 태그로 해결이 가능하다.
{% raw %}
`{% (end)raw %}`
{% endraw %}
highlight와 같이 사용하게 된다면 이런식으로 적는다.
{% raw %}
`{% (end)highlight language %}  
{% (end)raw %}`
{% endraw %}

## 참고자료
- [Liquid Templates and Django Templates](http://schinckel.net/2014/08/17/liquid-templates-and-django-templates/)
