Title: [Linux] 파일 인코딩 검사 및 인코딩 변환하기
Date: 2016-09-15
Category: Linux
Tags: linux, encoding
Slug: file-encoding-detect-and-convert
Authors: junshoong

윈도우의 메모장 등에서 작성한 파일은 리눅스에서 볼때 깨져서 보인다. 이런 경우 뿐만아니라 웹상에서 파일을 구한 경우에도 인코딩이 깨진 경우가 종종 있다. 이럴때 해당 파일의 인코딩을 검사하고 인코딩을 변환하는 방법을 알아보자.

## 인코딩 검사

인코딩 검사는 `chardet`라는 좋은 파이썬 패키지가 있다. `pip`을 통해 간단하게 설치할 수 있다.
```bash
$ chardet [file]
```

결과도 간단하게 나온다.  

![old.spl: EUC-KR (confidence: 0.99)](/images/2016-09-15/01.png)

## 인코딩 변환

인코딩 변환은 `iconv`를 통해서 변환한다. 기본적으로 리눅스에 설치되어 있을 것이다.
```bash
$ iconv -f EUC-KR -t UTF-8 [input_file] -o [output_file]
```

쉘 상에서 따로 메세지가 없으면 성공적으로 변환된 것이다.

## 참고자료
- [How to auto detect text file encoding?](http://superuser.com/questions/301552/how-to-auto-detect-text-file-encoding)
- [\[우분투14.04\]윈도우에서 작성한 텍스트 파일의 한글이 깨져서 나올때 팁](http://forum.falinux.com/zbxe/index.php?document_srl=807803)
