import requests
from lxml import etree

url = 'https://chengdu.zbj.com/search/f/?kw=saas'
resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for div in divs:
    price = div.xpath('./div/div/a[2]/div[2]/div/span[1]/text()')[0].strip("¥")
    print(price)