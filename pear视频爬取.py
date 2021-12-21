import requests

url = 'https://video.pearvideo.com/mp4/adshort/20211207/cont-1747354-15802637_adpkg-ad_hd.mp4'
resp = requests.get(url)

with open("a.mp4",'wb') as f:
    f.write(resp.content)

resp.close()
print("over.")