# import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
import numpy as np
import nltk
from collections import Counter
from konlpy.tag import Twitter
# from nltk.corpus import stopwords
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plot

dbpia = "http://www.dbpia.co.kr/search/topSearch?startCount=0&collection=ALL&range=A&searchField=ALL&sort=RANK&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&srchOption=*#none"
# resp = requests.get(dbpia).content
# source = BeautifulSoup(resp, 'html.parser')
# print(source)
#
#
# linklist = source.find_all('div', {'class': 'titWrap'})
# print(linklist)

driver = webdriver.Chrome(executable_path='chromedriver.exe')

page_number = 1
article_sentence, key_sentence, abstract_sentence = '', '', ''
article_words, key_words, abstract_words = [], [], []
with open("exception.txt", 'r', encoding='utf-8') as f:
    exception = f.read().split()
    f.close()

twitter = Twitter()
# stop_words = stopwords.words("english")
# stop_words.append(',')
# stop_words.append('.')

while True:
    # try:
    # ------ 페이지 열기 ------#
    paper_search = "http://www.papersearch.net/search/sch-result.asp?page={}&sel_searchfield=ALL&query=인공지능".format(
        page_number)
    driver.get(paper_search)
    driver.implicitly_wait(3)

    # ------ 해당 페이지 크롤 ------#
    article_list = driver.find_elements_by_tag_name('h3')
    keyword_list = driver.find_elements_by_class_name('btn-key')
    abstract_list = driver.find_elements_by_class_name('btn-cho')

    #  정보창 다 열어놓기
    for keyword in keyword_list:
        keyword.send_keys(Keys.RETURN)
    for abstract in abstract_list:
        abstract.send_keys(Keys.RETURN)

    # 데이터 없으면 종료
    if len(article_list) == 0:
        print("크롤링 완료!")
        driver.close()
        driver.quit()
        break

    # 데이터 가져오기 위한 웨이팅
    driver.implicitly_wait(3)

    # ------ 논문 제목 ------#
    for article in article_list:
        article_sentence += (" " + article.text)
        # print(article_sentence)
    # article_tokens = nltk.word_tokenize(article_sentence)
    # article_tag = nltk.pos_tag(article_tokens)
    article_tag = twitter.pos(article_sentence, norm=True, stem=True)

    # ------ 논문 키워드 ------#
    keywords_bundle = driver.find_elements_by_class_name('words')
    for bundle in keywords_bundle:
        keywords = bundle.find_elements_by_tag_name('a')
        # print(driver.page_source)
        for words in keywords:
            key_sentence += (" " + words.text)
    key_tokens = nltk.word_tokenize(key_sentence)
    key_tag = nltk.pos_tag(key_tokens)

    # ------ 논문 초록 ------#
    abstract_bundle = driver.find_elements_by_class_name('fs-small1')
    for bundle in abstract_bundle:
        abstract_sentence += (" " + bundle.text)
        # print(abstract_sentence)
    abstract_tokens = nltk.word_tokenize(abstract_sentence)
    abstract_tag = nltk.pos_tag(abstract_tokens)

    # except Exception as e:
    #     print("%s 페이지 크롤링 중 에러 발생" % page_number)
    #     print(e)

    for word, tag in article_tag:
        if tag in ['Noun']:
            article_words.append(word.lower())
    article_count = dict(sorted(dict(Counter(article_words)).items(), key=lambda x: x[1], reverse=True))
    # word_count_most = word_count.most_common(10)

    for word in exception:
        try:
            article_count.pop(word)
        except Exception as e:
            pass
    print(article_count)
    print()

    for word, tag in key_tag:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
            key_words.append(word.lower())
    key_count = dict(sorted(dict(Counter(key_words)).items(), key=lambda x: x[1], reverse=True))
    # word_count_most = word_count.most_common(10)

    for word in exception:
        try:
            key_count.pop(word)
        except Exception as e:
            pass
    print(key_count)
    print()

    for word, tag in abstract_tag:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
            abstract_words.append(word.lower())
    abstract_count = dict(sorted(dict(Counter(abstract_words)).items(), key=lambda x: x[1], reverse=True))
    # word_count_most = word_count.most_common(10)

    for word in exception:
        try:
            abstract_count.pop(word)
        except Exception as e:
            pass
    print(abstract_count)
    print()

    print("------------ {} page ------------".format(page_number))

    # ------------------ 페이지 넘기기 ------------------#
    page_number += 1
    print()
    break


# ------------------ WORD CLOUD ------------------------#
word_cloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", width=1000, height=500, background_color='white')
word_cloud.generate_from_frequencies(article_count)
plot.figure(figsize=(15, 15))
plot.imshow(word_cloud)
plot.axis('off')
plot.tight_layout(pad=0)
# plot.show()
plot.savefig("article1.png")
plot.close()

word_cloud.generate_from_frequencies(key_count)
word_cloud.generate_from_frequencies(key_count)
plot.figure(figsize=(15, 15))
plot.imshow(word_cloud)
plot.axis('off')
plot.tight_layout(pad=0)
# plot.show()
plot.savefig("keyword1.png")
plot.close()

word_cloud.generate_from_frequencies(abstract_count)
word_cloud.generate_from_frequencies(abstract_count)
plot.figure(figsize=(15, 15))
plot.imshow(word_cloud)
plot.axis('off')
plot.tight_layout(pad=0)
# plot.show()
plot.savefig("abstract1.png")
plot.close()







# ------------------ 페이지 넘기기 ------------------------#
# ---- 페이지 리스트 ----#
# page_list_bundle = driver.find_elements_by_class_name('paging')
# page_list = page_list_bundle[0].find_elements_by_tag_name('a')

# for page in page_list:
#     print(page.text)




