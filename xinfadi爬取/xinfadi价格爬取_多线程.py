import requests
import csv
from concurrent.futures import ThreadPoolExecutor

#获取数据函数 get_data()
#解析数据函数 parse_data()
#保存数据函数 save_data()



all_list = [] # 全局变量，用于保存解析的每一条数据列表

def get_data(page):
    
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    data = {
            "current": page,
            "limit": "20"
            }
    resp = requests.post(url,data=data,headers=headers).json() # post 提交需要form表单的一些参数
    row_list = []
    data_list = resp['list'] #提取数据列表，列表里的每个字典代表一条蔬菜信息
    for i in data_list:
        row_list.append(i['prodName'])
        row_list.append(i['lowPrice'])
        row_list.append(i['avgPrice'])
        row_list.append(i['highPrice'])
        row_list.append(i['specInfo'])
        row_list.append(i['place'])
        row_list.append(i['unitInfo'])
        row_list.append(i['pubDate'])
        all_list.append(row_list) #每条蔬菜信息存入列表，再将row_list春存入总列表
        row_list = []  # 清空列表，用于暂存下一条蔬菜信息
    with open('prive_duo.csv',"w",newline='',encoding='utf-8') as f: # 创建一个文件对象，newline=''作用是数据写入CSV后不会产生空行
        csv_writer = csv.writer(f) # 用文件对象f构造一个CSV写入对象
        csv_writer.writerow(["品名", "最低价", "平均价", "最高价", "规格", "产地", "单位", "发布日期"]) # writerow写入一行数据
        for row in all_list:
            csv_writer.writerow(row)
    

if __name__ == "__main__":
    with ThreadPoolExecutor(10) as t:
        for i in range(1,30):
            t.submit(get_data,i)
    
    print("over!")