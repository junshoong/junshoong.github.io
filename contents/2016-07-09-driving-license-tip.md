---
title: "[Python] 8퍼센트 투자목록 출력 슬랙 봇"
category: post
tags: 8percent, slack, bot, python
---
생각은 대충하고 있었는데 실제로 만든 건 이틀정도 걸린 것 같다. p2p 대부업체인 8percent에 올라오는 투자목록을 긁어와서 알려준다.

로직은 단순하다. 사용자가 list라고 bot에게 dm을 보내면 beautifulsoup로 투자 목록 페이지의 내용을 정리해서 보여준다.

아직은 단순하지만 몇가지 더 만들어 볼 수 있지 않을까 싶다. 간단한 정렬이라던지, 원하는 내용만 설정해서 보여주는 식으로 말이다.

코드와 설치 방법은 [github](https://github.com/vaporize93/8percent-slack-bot)에 오픈소스로 올려두었다. 크롤링부분은 생략하고 슬랙 봇 부분을 간단히 살펴보자.


{% highlight python linenos %}
token = os.environ.get('SLACK_TOKEN')    // 봇의 토큰을 환경변수에서 받아온다.
client = SlackClient(token)    // 토큰을 사용해서 슬랙클라이언트 객체를 만든다.

if client.rtm_connect():        // 연결을 확인한다.
    while True:                    // 무한루프를 돌면서 확인한다.
        last_read = client.rtm_read()    // 마지막 언급된 메세지를 읽는다.
        if last_read:                          // 언급된 메세지가 있으면
            try:
                parsed = last_read[0]['text']        // text를 긁어오고
                message_channel = last_read[0]['channel']        // 채널정보를 가져와서
                if parsed and 'list' in parsed:            // text안에 list가 있으면
                    deals = investments()        // 투자 정보를 가져온다.
                    investment_list = ""
                    for d in deals:                    // 여기서 이쁘게 프린트할 문장을 만들어준다.
                        d = "{title:>10} {grade:<4} {interest:>8} {duration:>8} {amount:>10} {progress:>5} {status:>5} \n".format(**d)
                        investment_list += d
                    client.rtm_send_message(message_channel, investment_list)        // 해당 채널에 메세지를 뿌려준다.

            except:
                pass
        time.sleep(1)
{% endhighlight %}
