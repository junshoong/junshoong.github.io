Title: [Python] http 요청을 비동기로하기
Date: 2017-04-26
Category: Python
Tags: python, asyncronous
Slug: asyncronous-http-request
Authors: junshoong

http 요청으로 간단한 스크래핑 작업을 하는데 요청 갯수가 일곱개 정도 되니 시간이 오래걸린다.

`asyncio`와 `aiohttp`를 사용해서 속도를 높여보자.

[gist:id=6c7db753f49f4720473b34147abc3b6c,file=requests_test.py]


위 코드는 `http://example.com`에 http get을 20회 실행하는 코드다.
timeit을 이용해서 시간을 확인해보니 6~7초정도 걸렸다.

[gist:id=6c7db753f49f4720473b34147abc3b6c,file=aiohttp_test.py]


같은 동작을 하는 코드지만 비동기처리를 한다.
시간을 확인해보니 1초 전후로 수행된다.

입출력이나 대기하는시간이 긴 작업일수록 비동기처리가 효율이 좋을 수 있다.
