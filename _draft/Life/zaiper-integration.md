Title: [Life] Trello와 Wunderlist 연동해서 사용하기
Date: 2015-10-07
Category: Life
Tags: life, tool, trello, wunderlist, tip
Slug: zaiper-integration
Authors: junshoong

요즘 개인 To-do List 관리는 [Wunderlist](https://www.wunderlist.com/)(분더리스트는 아마 독일 쪽에서 시작한 것 같다. 그래서 발음이..)를 활용하고 있는데, 무척 유용하게 잘 쓰고 있다. 그런데 다른 사람들과 업무 공유를 [Trello](https://trello.com/)(트렐로)를 사용하게 되었는데 할일은 계속 쌓여가는데 일일이 확인해서 추가하자니 점점 귀찮아 졌다. 그래서 둘을 연동할 방법을 찾고 있었는데, 처음엔 둘다 Slack을 통해서 Intergration 할 수 있길래 [Slack](https://slack.com/)으로 어떻게 해볼까 했었는데 조금 찾아보니 [Zapier](https://zapier.com/)라는 웹 서비스를 발견했다.


Zapier는 여러 서비스들을 어떤 Trigger를 통해서 Active를 하게 해주는데, 예를 들자면 Trello에서 새로운 Card가 만들어지면 Wunderlist에서 새로운 To-do가 생성된다. 또, Github에서 새로운 Issue가 생길 때 Wunderlist에 새로운 To-do를 만들어 줄 수 있다. 뿐만 아니라 구글, 아마존, 드롭박스, 에버노트 등 수십 가지 연결을 만들어내고 조건에 따른 이벤트를 발생 시킬 수 있다.


일단 이 글의 목적인 Trello - Wunderlist 연결을 살펴보자. 물론 연결할 서비스들과 Zapier에 계정이 있어야 한다. 그리고 Zapier에 들어가서 Dashboard에 들어가 보면 오른쪽에 Make New Zap 버튼이 있다. 그걸 눌러보자.

![zaiper 화면1](/images/2015-10-07/01.png)

위와 같이 설정해주자. 왼쪽에는 어떤 일이 발생할 지를 나타내는 사건이고, 오른쪽에는 어떤 일을 할 지 정하는 것이다.


![zaiper 화면2](/images/2015-10-07/02.png)


2, 3번은 계정 설정인데 해당 사이트의 자기 계정으로 로그인하면 된다.

4번은 Trigger, 즉 방아쇠가 되는 사건의 범위를 정해주는 것이다.

위의 경우에는 Trello를 시작하면 나오는 Welcome Board의 Intermediate 리스트에 Open되는 Card를 말하는 것이다.

아래 +Add a custom filter를 눌러서 카드 이름을 필터 하는 등의 좀 더 자세하게 설정을 해줄 수 있다.


![zaiper 화면3](/images/2015-10-07/03.png)



이 쪽은 이벤트를 발생 시키는 쪽이다. 어떤 리스트에 추가할지, 제목은 무엇으로 할지 Due Date와 Starred 여부, Note의 내용 등을 명시 해줄 수 있다. 자세한 사항은 직접 하나하나 해보면서 느끼면 될 것이다.

![zaiper 화면4](/images/2015-10-07/04.png)



추가적으로 안내하자면, Plan 이다. 한 달 당 Task 횟수, Zap(이벤트) 개수, 동기화 시간 등을 기준으로 가격이 책정되어 있다. 첫 14일은 Trial 버전으로 사용할 수 있는데 그에 따른 포함된 서비스는 위에 적혀있는 Your trial includes에 나와있다. 아마 저 시간이 지나면 Free로 전환되는 것 같다. 업무적으로 쓰거나 많은 프로젝트를 하지 않는 이상 개인 용도로 쓰기에는 무료 버전도 괜찮지 않을까.


기본적으로 많은 어플리케이션들이 서로 Intergration을 지원해주는 편이긴 하지만, 아쉽게도 지원이 안 되는 서비스들이 있다. 이 참에 써보게 되었는데 아직 얼마 써보진 않았지만 그래도 만족하면서 사용 중이다.
