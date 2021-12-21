
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://umei.cc/bizhitupian/weimeibizhi/225260.htm"
resp = requests.get(url)
resp.encoding = 'utf-8'
page = BeautifulSoup(resp.text,'html.parser')
aa = page.find('div',class_ = 'ImageBody')
bb = aa.find('img')
# cc = bb.find('img')
# jzy_url = cc.get('src')
# jzy_img = requests.get(jzy_url)

# with open("oo.jpg",'wb') as f:
#     f.write(jzy_img.content)
# resp.close()

print(bb.get('src'))
resp.close()