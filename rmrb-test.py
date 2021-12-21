# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import datetime
import time
base_url = 'http://paper.people.com.cn/rmrb/html/2021-12/01/'
url = 'http://paper.people.com.cn/rmrb/html/2021-12/01/nbs.D110000renmrb_01.htm'
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
resp = requests.get(url,headers=headers)
resp.encoding = resp.apparent_encoding
html = resp.text
div_bf= BeautifulSoup(html)
title_list = div_bf.find_all('div',class_ = 'swiper-slide')
a_bf = BeautifulSoup(str(title_list))
a= a_bf.find_all('a')
bb = {}
for each in a:
    bb[each.string] = base_url + each.get('href')
    # print(each.string, base_url + each.get('href'))


with open('./rmrb.txt', 'w', encoding='utf-8') as f:
    for i in bb:
        f.write(i + '\n')
        f.write(bb[i] + '\n')
# print(bb)
