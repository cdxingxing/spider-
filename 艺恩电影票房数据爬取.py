
import requests
import json
import jsonpath
import execjs

"""js逆向--百度翻译分析"""

"""
# 0.尝试构建URL访问---可行
url = "https://fanyi.baidu.com/?aldtype=16047#en/zh/hello%20spider"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}
r = requests.get(url, headers=headers)
html = r.text
print(html)
"""

# js逆向撸,注意要带上cookie

# 1.初步构建表单
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Cookie": "BAIDUID=C3A44BD2BCAA852D78454F118D907CA2:FG=1; BIDUPSID=C3A44BD2BCAA852D78454F118D907CA2; PSTM=1558237711; delPer=0; H_PS_PSSID=1455_21097_29064_28519_28769_28723_28963_28838_28585_29071; PSINO=7; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1558237732; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1558237732; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; CHINA_PINYIN_SWITCH=0; DOUBLE_LANG_SWITCH=0"
}
data = {
    "from": "en",
    "to": "zh",
    "query": "",  # query 即我们要翻译的的内容
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "",  # sign 是变化的需要我们执行js代码得到
    "token": "26b850184b8b9031bd6089b7e263a887"  # token没有变化
}

# 2.尝试执行js逆向得出sign值
# 设置一下我们要翻译的内容
query = "hello spider"
data["query"] = query
# 执行js代码得到我们苦求的sign值
# 读取js文件
with open("fanyi.js", "r", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())
sign = ctx.call("e", query)
# print(sign)
# sign成功获取，写入date
data["sign"] = sign

# 3.请求翻译结果
response = requests.post(url, headers=headers, data=data)
# print(response.text)
# json_date = json.loads(response.text)
json_date = response.json() 
result = jsonpath.jsonpath(json_date, '$..data.0.dst')
print(result[0])



