Title: [Regex] 특정문자로 시작하지 않는 중국어가 포함된 문자열
Date: 2017-04-09 15:40
Category: Regex
Slug: chinese-string-without-special-character-starting
Tags: regex, python, slackbot
Author: junshoong

[ssslackbot](https://github.com/skhu-sss/ssslackbot/blob/master/plugins/filter.py)을 개발 중에 regex가 필요하게 되었다. 전각 느낌표(`！`)로 시작하지 않는 중국어가 포함된 문자열을 확인해서 걸러내야하는 작업이다.

> 중국어 자판에서는 전각느낌표를 사용한다. `！` != `!`

먼저 중국어 문자열의 범위를 살펴보자. 영어에서는 `[a-z]`나 `[A-Z]`등을 사용해서 간단히 거를 수 있다. 한글도 마찬가지로 `[ㄱ-힇]` 정도로 거른다. 하지만 중국어는 유니코드로 걸러내야한다. `[\u4e00-\u9fff]`로 표현 된다.

그럼 이제 전각 느낌표로 시작하지 않는 문자열을 걸러보자. 편의를 위해서 일반적으로 사용하는 반각느낌표(`!`)를 사용하겠다.

`^(?!!)(.*)`

하나씩 풀어보자.

- `^` 는 문자열의 시작부분을 의미한다.
- `(?!x)`는 `x`로 시작하지 않는 문자를 검색한다.
- `.`는 모든 문자를 의미한다.
- `*`는 0~n개의 문자를 의미한다.

`^(?!!)(.*)` 그럼 이것은 `!`로 시작하지 않는 모든 문자를 의미한다.

그럼 두 가지를 합쳐보자.

`^(?!!)(.*[\u4e00-\u9fff]+.*)` !로 시작하지 않는 모든 문자열속의 중국어가 1개 이상포함된 문자열을 의미한다.

- [regex101](https://regex101.com/r/ZMBaBB/1)
- [stackoverflow - chinese character](http://stackoverflow.com/a/40122744/4466697)
- [stackoverflow - chinese unicode](http://stackoverflow.com/a/1366113/4466697)
