Title: [Blog] html-proofer에 ignore 항목 설정하기
Date: 2016-08-18
Category: Blog
Tags: blog, jekyll, ruby
Slug: jekyll-html-proofer
Authors: junshoong

jekyll에서 plugin으로 `html-proofer`를 통해서 하이퍼링크를 테스트하고 있다. 로컬에서는 터미널에서 간단하게 테스트 해볼 수 있다.

```bash
$ htmlproofer ./_site
```

그런데 travis-ci에서 테스트하는데 [문제가 생겼다.](https://travis-ci.org/vaporize93/blog/builds/153172807) 일부 링크에서 travis-ci 환경에서 접속하는걸 `robots.txt`가 막는 것 같다. 해당 항목을 무시하고 테스트를 하기 위해서 방법을 찾아봤다.

[html-proofer의 Github 페이지](https://github.com/gjtorikian/html-proofer#configuration)에서 확인 할 수 있었다. 이를 확인해보면 `:url_ignore` 옵션을 통해 원하는 항목을 무시할 수 있다.

[gist:id=779b1c3a7e290de7cdf4a0b935afe7bd,file=Rakefile]

위와 같이 설정함으로써 example.com이 포함된 링크는 검사를 하지 않는다.

또한 기존에는 `$ bundle exec htmlproofer ./_site`로 테스트를 했지만, 해당 스크립트 대신에 `$ bundle exec rake test`를 통해 해당 항목을 테스트한다.

## 참고링크

 - [travis failing to run rake with LoadError: cannot load such file — rspec/core/rake_task](http://stackoverflow.com/questions/36204602/travis-failing-to-run-rake-with-loaderror-cannot-load-such-file-rspec-core-r)
 - [LoadError: cannot load such file — rspec/core/rake_task](http://stackoverflow.com/questions/30114733/loaderror-cannot-load-such-file-rspec-core-rake-task)
  - [bundle exec rake test does nothing](http://stackoverflow.com/questions/14362944/bundle-exec-rake-test-does-nothing)
  - [Some Jekyll Tests - Logical Solutions blog](https://spock.rocks/tech/2016/03/21/basic-jekyll-site-tests.html)
