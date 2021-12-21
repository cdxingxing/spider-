import requests
import csv

# 1 创建类Info_spider()
# 2 数据获取方法get_data()
# 3 数据解析方法parse_data()
# 4 数据保存方法save_data()

class Info_spider():
    def __init__(self):
        self.url = 'http://www.xinfadi.com.cn/getPriceData.html'
        
        self.hesders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
        self.prodName = []
        self.lowPrice = []
        self.avgPrice = []
        self.highPrice = []
        self.specInfo = []
        self.place = []
        self.unitInfo = []
        self.pubDate = []

    def get_data(self):
        n = int(input("请输入要爬取的页数:"))
        for i in range(1,n+1):
            data = {
                    "current": f"{i}",
                    "limit": "20"
                    }
            resp = requests.post(self.url,data = data, headers= self.hesders).json()
            # print(resp.json())
            # return resp.json()
            self.parse_data(resp) # 调用类方法解析并暂存数据


    def parse_data(self,resp_data):
        data_list = resp_data['list']
        for i in data_list:
            self.prodName.append(i.get('prodName'))
            self.lowPrice.append(i.get('lowPrice'))
            self.avgPrice.append(i.get('avgPrice'))
            self.highPrice.append(i.get('highPrice'))
            self.specInfo.append(i.get('specInfo'))
            self.place.append(i.get('place'))
            self.unitInfo.append(i.get('unitInfo'))
            self.pubDate.append(i.get('pubDate'))
            # print(aa)
        # print(self.prodName)


    def save_data(self):
        # 
        row_list = zip(self.prodName,self.lowPrice,self.avgPrice,self.highPrice,self.specInfo,self.place,self.unitInfo,self.pubDate)
        with open("price_m.csv","w",newline= "",encoding= "utf-8") as f:
            csv_witer = csv.writer(f)
            csv_witer.writerow(["品名", "最低价", "平均价", "最高价", "规格", "产地", "单位", "发布日期"])
            for row in row_list:
                csv_witer.writerow(row)

if __name__ == "__main__":
    xinfadi = Info_spider()
    xinfadi.get_data()
    xinfadi.save_data()
    print("over!")