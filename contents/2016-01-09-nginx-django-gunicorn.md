---
title: "[Nginx] Django+gunicorn 사용환경에서 외부에서 접속하기"
category: post
tags: nginx, django, gunicorn, network
---
이걸로 몇 일 동안 고생을 한지 모르겠다. 집 네트워크의 80번 포트가 공유기 설정으로 열려있어서 웹서버로 사용할 수 있지 않을까 했는데, 집에 있는 서버와 연결이 안된다. DMZ설정도, 포트포워딩으로도... 그래서 결국 8080번 포트를 사용해서 운용을 하려고 하니까, 외부 포트 8080번  - 서버 포트 80번으로 해두니까 테스팅 환경이 외부와 내부가 다르니 또 머리가 아프다.

결국 외부 8080 - 내부 8080으로 맞추기로 했는데, 잘 안되더라. gunicorn의 port 설정도 확인해보고, Django도 확인해봤는데, 두 가지를 설정하는 게 아니라 nignx면 충분했다. gunicorn은 소켓으로 연결되어 있기 때문에 port 설정은 따로 해주지 않아도 되는 것 같다.

SITENAME은 각자 알아서.


`/etc/init/gunicorn-SITENAME.conf`
{% highlight conf %}
description "Gunicorn server for SITENAME"

start on net-device-up
stop on shutdown

respawn

setuid USER
chdir /home/USER/sites/SITENAME/source

exec ../virtualenv/bin/gunicorn \
    --bind unix:/tmp/SITENAME.socket \
    superlists.wsgi:application
{% endhighlight %}

`/etc/nginx/sites-enable/SITENAME`  // 이 파일은 `../sites-available` 쪽 경로의 파일에 링크 되어 있다.

{% highlight nginx %}
server {
    listen 8080;
    server_name SITENAME;

    location /static {
        alias /home/USER/sites/SITENAME/static;
    }  

    location / {
        proxy_set_header Host $host:$server_port;
        proxy_pass http://unix:/tmp/SITENAME.socket;
    }
}
{% endhighlight %}

위에 보면 `proxy_set_header Host` 부분이 보인다. 여기서 `$host` 만 적어주게 되면 첫 화면은 접속이 잘 되지만, 페이지를 이동하거나 하면 지정해준 포트 부분이 날아간다.

예를 들면 이렇다.  `www.harveyk.me:8080` 에서 다음 버튼을 눌러 `~/next`로 가게 되면 `www.harveyk.me/next`로 이동하여 페이지를 찾을 수 없게 된다. 이 부분을 위해 저 라인 뒷 부분에 `:$server_port`를 추가해준다. 이러면 포트 부분이 날아가지 않아 정상적으로 작동한다. 외부8080 - 내부8080을 맞췄기 때문에 외부에서 테스트 작업을 하게 되더라도 환경이 달라지지 않는다.


참고로 네트워크 내부에서는 내부 ip로만 접속이 가능하도록 되어 있는 경우가 있다. 예를 들면 내부는 `192.168.150.150:8080` 이고 외부는 `www.harveyk.me:8080`인 경우인데, 이 경우엔 `/etc/hosts` 파일을 수정해주면 된다.

{% highlight hosts %}
192.168.150.150    www.harveyk.me    harveyk
{% endhighlight %}

이런 식으로 추가해주면 내부에서도 접근이 가능하다. 일부 공유기에서는 라우팅 환경을 조정해서 해주는 경우가 있는데, NIC 성능 이슈가 있다고 한다.

## 참고링크

 - [http://stackoverflow.com/questions/10168155/nginx-proxy-https-to-http-on-non-standard-port](http://stackoverflow.com/questions/10168155/nginx-proxy-https-to-http-on-non-standard-port)

- [Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/index.html)
