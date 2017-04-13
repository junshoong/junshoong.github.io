Title: [wargame] login filtering
Date: 2016-02-21
Modified:
Category:
Tags:
Slug: wargame-login-filtering
Authors: junshoong
Summary:


context
---
title: "[wargame] login filtering"
category: post
tags: wargame, php, mqsql
---

[450p - login filtering](http://wargame.kr:8080/login_filtering/)

![문제 화면](/images/2016-02-21/01.png)

> I have accounts. but, it's blocked.  
> can you login bypass filtering?

내가 계정이 있는데 블록 당했습니다.
당신은 필터링을 우회해서 로그인할 수 있나요?

Start를 눌러 들어가면 소스를 볼 수 있는 링크가 제공되어 있다. 들어 가보면 php코드와 html코드가 있고 하단에 블록된 계정명이 적혀있다.

![소스 주석부분 화면](/images/2016-02-21/02.png)

계정을 두 개 가지고 있는데, guest / guest 계정을 일단 사용해보자.

![로그인 실패 화면](/images/2016-02-21/03.png)

음.. 역시 계정이 블록되어 있다고 나타난다. 코드를 한 번 살펴보자.

{% highlight php %}
<?php

if (isset($_GET['view-source'])) {
    show_source(__FILE__);
    exit();
}
/*
create table user(
 idx int auto_increment primary key,
 id char(32),
 ps char(32)
);
*/
if(isset($_POST['id']) && isset($_POST['ps'])){
  include("../lib.php"); # include for auth_code function.

  mysql_connect("localhost","login_filtering","login_filtering_pz");
  mysql_select_db ("login_filtering");
  mysql_query("set names utf8");

  $key = auth_code("login filtering");

  $id = mysql_real_escape_string(trim($_POST['id']));
  $ps = mysql_real_escape_string(trim($_POST['ps']));

  $row=mysql_fetch_array(mysql_query("select * from user where id='$id' and ps=md5('$ps')"));

  if(isset($row['id'])){
   if($id=='guest' || $id=='blueh4g'){
    echo "your account is blocked";
   }else{
    echo "login ok"."<br />";
    echo "Password : ".$key;
   }
  }else{
   echo "wrong..";
  }
 }
?>
{% endhighlight %}

id, ps를 입력하면 시작한다. db 쿼리는 MySQL를 사용한다. `mysql_real_escape_string` 함수는 기본적인 SQL인젝션에 대항해서 검증을 거치는 함수다.`' or ''='` 같은 항목을 걸러준다. trim은 앞 뒤 공백을 제거한다. `mysql_fetch_array` 함수는 추출된 데이터를 배열로 변환해서 저장한다.


`$row['id']`가 set 되어있고 id가 guest나 blueh4g가 아니면 key를 획득할 수 있다.

그런데 여기서 중요한 건 입력 받은 `$id` 값이 guest나 blueh4g만 아니면 된다는 점이다. mysql에서는 컬럼명과 값에 대소문자나 앞 뒤 공백을 신경 쓰지 않는다.

그럼 아래 쿼리문 실행 결과를 보자.

{% highlight sql %}
select * from user where id='guest';
{% endhighlight %}
![쿼리문 실행결과](/images/2016-02-21/04.png)

{% highlight sql %}
SELECT * FROM user WHERE ID='GUSET';
{% endhighlight %}
![쿼리문 실행결과](/images/2016-02-21/05.png)

{% highlight sql %}
SELECT * FROM USER WHERE ID='GUSET';
{% endhighlight %}
![쿼리문 실행결과](/images/2016-02-21/06.png)

쓸 일은 없겠지만 이런 식으로 대소문자를 섞어서 사용해도 잘 실행된다.

{% highlight sql %}
sElEcT * FrOm user wHeRe iD='GuEsT ';
{% endhighlight %}
![쿼리문 실행결과](/images/2016-02-21/07.png)

위에 스크린샷을 보면 알 수 있듯이 테이블 이름 외에는 대소문자를 구분하지 않고 결과가 나온다.

이건 자료형이 `CHAR` 형이나 `VARCHAR` 형일 경우 그렇고, `BINARY`, `VARBINARY` 의 경우는 해당 바이트 값으로 구분하기 때문에 대소문자 구분이 된다.


아무튼 php에서 id를 검증하는 부분으로 돌아가 보자.
{% highlight sql %}
$id = mysql_real_escape_string(trim($_POST['id']));
$ps = mysql_real_escape_string(trim($_POST['ps']));
{% endhighlight %}

일단 이 부분에서 띄어쓰기나 불순한 의도를 가진 명령들이 걸러진다.
{% highlight sql %}
if($id=='guest' || $id=='blueh4g'){
{% endhighlight %}
그럼 이 부분은 어떨까? 소문자로 이루어진 id 값만 걸러낸다.


그럼 하나만 대문자로 바꿔보자.

![로그인 창](/images/2016-02-21/08.png)

![로그인 성공화면](/images/2016-02-21/09.png)
성공했다.
