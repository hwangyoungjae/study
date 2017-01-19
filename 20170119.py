# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os,sys,time
os.chdir(os.path.dirname(__file__))
import BeautifulSoup, requests
from selenium import webdriver

def non_js_execute(url):
    r = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(r.content)
    r.close()
    print soup.find('div', attrs={'class': 'bx-wrapper'})

def js_execute(url):
    client = webdriver.PhantomJS(executable_path=r'C:\Users\youngjae\Desktop\scrapy\crawcraw\crawcraw\spiders\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    client.get(url)
    soup = BeautifulSoup.BeautifulSoup(client.page_source)
    print soup.find('div',attrs={'class':'bx-wrapper'})

if __name__ == '__main__':
    URL = 'http://www.afreecatv.com/'
    # non_js_execute(URL)
    # js_execute(URL)

