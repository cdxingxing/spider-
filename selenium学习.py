from selenium.webdriver import Chrome
from selenium.webdriver.chrome import options  #用的什么浏览器驱动  就导入什么浏览器模块
from selenium.webdriver.common.keys import Keys #Keys具有点击键盘的功能
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options



# web = Chrome()
# url = 'https://www.baidu.com'
# web.get(url)
# print(ge.title)


# web = Chrome()  #创建一个浏览器对象
# web.get("http://lagou.com/") #打开网站
# ele = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a') #找到元素"全国"所在HTML位置，复制xpath
# ele.click() #点击
# time.sleep(1)
# ele2  = web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER) #找到搜索框，输入python，并点击enter
# div_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div') #找到所有招聘信息div
# for div in div_list:  #提取div信息的文本内容
#     job_name = div.find_element_by_tag_name("a").text
#     price = div.find_element_by_xpath("./div/div/div[2]/span").text
#     print(price)

# web = Chrome()
# web.get("http://lagou.com/")
# ele = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# ele.click()
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
# web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click() #点击招聘职位，进入下一个窗口
# time.sleep(2)
# web.switch_to.window(web.window_handles[-1]) #将web切换至新窗口
# job_data = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text #提取职位描述内容
# print(job_data)
# web.close() #关闭所在窗口
# web.switch_to.window(web.window_handles[0]) #回到原始窗口
# print(web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text) #在原始窗口提取内容


# # selenium处理iframe（内嵌框架）
# web = Chrome()
# web.get('https://www.bilibili.com/') #随便写的网址
# # 处理iframe必须先切换到iframe里面去才能拿到数据
# iframe = web.find_element_by_xpath('ifram定位')
# web.switch_to.frame(iframe) #切换至iframe
# web.switch_to.default_content() #返回原窗口



# # 构造无头浏览器，就是让原先要打开的浏览器不显示，然后在后台运行
# opt = Options()
# opt.add_argument("--headless") # 无头
# opt.add_argument("--disable-gpu") #gpu(显卡) 不使能显卡
# web = Chrome(options = opt) #把参数设置传入浏览器


# web = Chrome()
# web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]') #定位到年份下拉列表元素
# sel = Select(sel_el) #把元素包装成下拉菜单
# for i in range(len(sel.options)): #获取下拉索引
#     sel.select_by_index(i)
#     time.sleep(2)
#     name = web.find_element_by_xpath('//*[@id="TableList"]/table/tbody/tr[2]/td[2]/a/p')
#     print(name.text)
# web.close()



# # 如何拿到页面进过数据加载以及执行js脚本后的html，也就是f12元素显示的代码，与源代码不一样

# web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# time.sleep(2)
# print(web.page_source)

    


