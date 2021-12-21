import requests


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
    "params": "kjJNtSnFSmHpcjVeaqKoj7os9ztQpiCedVCLW6SXjUN9ojUD97owvLIA6wKBKWH6QsPaNpaZhQRjTET3ZAU9ettptbnGFgAItKT45VkJD+yxHHkSNruSCuvkJB5ScNO6Ggswz2YFx+Db3ibQDIWpZusHlXfi55D3wT3v3a99sY7+2G1VO4xr3uax+JKmYiT0p1Ew3sdgDV4AX7Kvgk0b7CdwNCOL8FPVBSiMuNGJ+0QMtSE9OH36MlpQjRHxuQ6jC7Cq4OVPlaISSePn8aN9S92/aSjMLYQRMfs9ter1BHM=",
    "encSecKey": "bcd0865cac366af03778b980ed8bf249ce908af5990281b8340bc2f8f50b8c1c577f981b3cda8ef9b6d1aad9f511735613c34e77f0a91a04d428b12c1c6a4f072015ba52741afc271d52a1205b8e80ffb4fe0cb1cbc4f321595926a547b90b11ac970f7dea6ffc8582a11f5f2fff5d39f5adf36a3193fadb1d4ea79b1020cf45"
}

resp = requests.post(url,data)
# print(resp.json()['data']['hotComments'][0]['content'])
data_list = resp.json()['data']['hotComments']
i = 0
for data_content in data_list:
    print(i, data_content['content'])
    i +=1