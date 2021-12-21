from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys #Keys具有点击键盘的功能



web = Chrome()
web.get("http://www.chaojiying.com/user/login/")
# .screenshot_as_png把定位图片元素转为图片二进制数据
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('1336810384', '7227349@ismy', '926835')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('1336810384')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('7227349@ismy')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(6)
# web.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').send_keys(Keys.ENTER)
print('***************************')
time.sleep(100) #这里不睡眠，点击登录后浏览器会自动关闭

