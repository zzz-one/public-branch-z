from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

# __browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址
# __browser_url = r'/Applications/360Chrome.app'  ##360浏览器的地址
__browser_url = r'/Applications/360Chrome.app/Contents/MacOS/360Chrome'  ##360浏览器的地址
chrome_options = Options()
chrome_options.binary_location = __browser_url

dr = webdriver.Chrome(chrome_options=chrome_options)
# dr=webdriver.Chrome()
dr.get("https://www.baidu.com/")
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id('su').click()
dr.find_element_by_id()
#这个方法已经弃用，改用find_element
dr.find_element()
time.sleep(6)
dr.quit()
#关闭浏览器
# dr.quit()

