# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from slacker import Slacker

slacker = Slacker('xoxp-198161310209-344433155092-405373120689-e7e14c5e56d8a2384917ddd2149c6798')

# 코스트코
print('costco')
# r = requests.get('https://www.costco.co.kr/search/?text=kf')
# html = r.text
# soup = BeautifulSoup(html, 'html.parser')
# list = soup.find('ul', {'id': 'list-view-id'})
# for li in list.find_all('li'):
#     name = li.select('.product-name-container')[0].select('.notranslate')[0]
#     if name.text.find('마스크') >= 0 or name.text.lower().find('kf94') >= 0 or name.text.lower().find('kf80') >= 0:
#         # 슬랙 메시지
#         slacker.chat.post_message('GVBM6C396', 'https://www.costco.co.kr' + li.select('.thumb')[0].attrs['href'])


print('drpuri')
url_list = [
    'https://smartstore.naver.com/mfbshop/products/4735160554',
    # 'https://smartstore.naver.com/cucofarm/products/4818644134',
    # 'https://smartstore.naver.com/cucofarm/products/4818677202',
    'https://smartstore.naver.com/gonggami/products/4705579501',
]

for url in url_list:
    r = requests.get(url)
    print(url, r.status_code)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        not_goods = soup.select('.not_goods')
        if not not_goods:
            slacker.chat.post_message('GVBM6C396', url)

# 닥터퓨리
# r = requests.get('https://smartstore.naver.com/mfbshop/products/4735160554')
# soup = BeautifulSoup(r.text, 'html.parser')
# not_goods = soup.select('.not_goods')
# if not not_goods:
#     slacker.chat.post_message('GVBM6C396', 'https://smartstore.naver.com/mfbshop/products/4735160554')
#
# print('maskpam')
# r = requests.get('https://smartstore.naver.com/cucofarm/products/4818644134')
# soup = BeautifulSoup(r.text, 'html.parser')
# not_goods = soup.select('.not_goods')
# if not not_goods:
#     slacker.chat.post_message('GVBM6C396', 'https://smartstore.naver.com/cucofarm/products/4818644134')

# 웰킵스
# print('welkeeps')
# # browser = webdriver.Chrome(executable_path='drivers/mac/chromedriver')
# browser = webdriver.PhantomJS(executable_path='drivers/mac/phantomjs')
# browser.set_window_size(1120, 550)
# browser.get('http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1007205')
# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'productDetail')))
# try:
#     soldout = browser.find_element_by_class_name('soldout')
# except NoSuchElementException:
#     slacker.chat.post_message('GVBM6C396', 'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1007205')
#
# browser.quit()
