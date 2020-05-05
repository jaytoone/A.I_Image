## 웹 크롤링을 사용한 인공지능 트렌드 워드 클라우드 만들기

> <span style="color:limegreen">국내 논문을 대상으로 사용된 단어들을 조사해 현재 인공지능의 트렌드를 조사하고 워드 클라우드를 사용해 가시화한다.</span>



## Description

* 논문의 **제목 / 키워드 / 초록별로 명사형 단어만**을 수집했으며 자연어 처리 과정에서 **konlpy, nltk** 를 사용
* **selenium 모듈을 활용해 동적 크롤링**을 진행하였으며 **dbpia 논문 사이트의 모든 페이지를 클릭하여 수집**하였다.
* **exception.txt** 파일을 만들어 A.I Trend.py 파일이 외부에서 참조하게끔 만들어 수집된 명사형 단어 중 무의미한 단어들을 색출해내었다.



## Result

**Keyword Wordcloud**![keyword](https://user-images.githubusercontent.com/50652715/81028407-415f9380-8ebc-11ea-8deb-51a5e3cb7f56.png)



**Abstract Wordcloud**![abstract](https://user-images.githubusercontent.com/50652715/81028408-4290c080-8ebc-11ea-9a0d-7675f15c4501.png)



**Article Wordcloud**![article](https://user-images.githubusercontent.com/50652715/81028410-4290c080-8ebc-11ea-8076-b1516b4529e3.png)

