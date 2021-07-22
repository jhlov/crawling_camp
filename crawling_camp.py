# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from slacker import Slacker


r = requests.get('https://camping.gtdc.or.kr/DZ_reservation/reserCamping.php?xch=reservation&xid=camping_reservation&searchDate=202006')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
table = soup.select('.caleTitTbl')
h25_list = table[0].select('.h25')
for h25 in h25_list:
    span = h25.find('span')
    if span.text in ['10', ]:
        ul = h25.parent.find('ul')
        for span in ul.find_all('span')[:2]:
            i = int(span.text.replace('(', '').replace(')', ''))
            print(i)
            if i > 0:
                # 슬랙 메시지
                slacker = Slacker('xoxp-198161310209-344433155092-405373120689-e7e14c5e56d8a2384917ddd2149c6798')
                slacker.chat.post_message('DA4CR4P8C', i)

                break


