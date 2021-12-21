from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains #ActionChains(事件链)


option = Options()
# 下面这句话是为了保证滑块能划过去  原因：正常chrome里window.navigator.webdriver参数是false（在控制台输入可查看），
# 不加下面的的参数话，控制程序打开会是True
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options = option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(3)
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('zhaoliangliang333')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('7227349ismy')
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(3)
huakuai = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(huakuai,305,0).perform() #绑定事件的执行者web，并perform执行事件 rag_and_drop_by_offset（根据偏移量拖动并停止）