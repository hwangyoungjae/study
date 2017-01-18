# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os,sys,time
os.chdir(os.path.dirname(__file__))
import requests, BeautifulSoup, datetime

sdate = datetime.date.today() - datetime.timedelta(days = 7) #검색할 날짜 범위, 시작날짜(오늘로부터 7일 전)
edate = datetime.date.today() #검색할 날짜 범위, 끝날짜(오늘)
query = '광화문' #검색할 키워드

url = 'http://search.chosun.com/search/news.search'
params = {
    'query':query, #검색할 키워드
    'pageno':0, #페이지 번호
    'orderby':'docdatetime', #정렬 순서(최신순)
    'sdate':sdate.strftime('%Y.%m.%d'), #시작날짜
    'edate':edate.strftime('%Y.%m.%d'), #끝날짜
}
r = requests.get(url, params)
soup = BeautifulSoup.BeautifulSoup(r.content)
r.close()

soup2 = soup.find('section',attrs={'class':'result news'}) #<section class="result news"> 가져오기
# for article in soup2.findAll('dd',attrs={'class':'thumb'}):
for article in soup2.findAll('dl'):
    print article.dt.a['href'] #기사 URL
    print article.dt.a.text.encode('utf8') #기사 제목
    print

