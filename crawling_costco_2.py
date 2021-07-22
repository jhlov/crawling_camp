# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from slacker import Slacker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# 코스트코
r = requests.get('https://www.costco.co.kr/search/?text=kf')
if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find('ul', {'id': 'list-view-id'})
    for li in list.find_all('li'):
        name = li.select('.product-name-container')[0].select('.notranslate')[0]
        if name.text.find('마스크') >= 0 or name.text.lower().find('kf94') >= 0 or name.text.lower().find('kf80') >= 0:
            pass
            # 슬랙 메시지
            # slacker = Slacker('xoxp-198161310209-344433155092-405373120689-e7e14c5e56d8a2384917ddd2149c6798')
            # slacker.chat.post_message('GVBM6C396', 'https://www.costco.co.kr' + li.select('.thumb')[0].attrs['href'])

# 네이버
r = requests.get('https://smartstore.naver.com/mfbshop/products/4735160554')
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    not_goods = soup.select('.not_goods')
    if not not_goods:
        pass
        # slacker = Slacker('xoxp-198161310209-344433155092-405373120689-e7e14c5e56d8a2384917ddd2149c6798')
        # slacker.chat.post_message('GVBM6C396', 'https://smartstore.naver.com/mfbshop/products/4735160554')

browser = webdriver.Chrome(executable_path='drivers/mac/chromedriver')
# browser = webdriver.PhantomJS(executable_path='drivers/mac/phantomjs')
browser.set_window_size(1120, 550)
browser.get('http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1007205')
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'productDetail')))
try:
    soldout = browser.find_element_by_class_name('soldout')
except NoSuchElementException:
    print('판매중')
    # slacker = Slacker('xoxp-198161310209-344433155092-405373120689-e7e14c5e56d8a2384917ddd2149c6798')
    # slacker.chat.post_message('GVBM6C396', 'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1007205')

browser.quit()
