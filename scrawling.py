import requests
from bs4 import BeautifulSoup

# 기사의 링크들이 담기는 리스트입니다.
rsss = []

# rss와 기사에서 특정 부분을 크롤링하는 함수입니다.
def crawler(url, parser, css_selector):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, parser)
    datas = soup.select(css_selector)
    if parser == "lxml":
        print(datas[0].text)
    else:
        for data in datas:
            rsss.append(data.text)

#실행코드
print("크롤링을 시작합니다.")
crawler('http://rss.joins.com/joins_news_list.xml', 'xml', 'item link')
print("rss 추출이 완료되었습니다.")

for link in rsss:
    try:
        crawler(link, 'lxml', '#article_body')
        print("="*20)
    except Exception as e:
        print(e)
        print('Continuing ...')
        continue

print("크롤링을 종료합니다.")
