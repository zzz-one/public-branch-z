import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseMain:
    _dr_url=""
    def __init__(self,driver_base=None):
        if driver_base==None:
            __browser_url = r'/Applications/360Chrome.app/Contents/MacOS/360Chrome'  ##360浏览器的地址
            chrome_options = Options()
            # /Applications/360Chrome.app/Contents/MacOS/360Chrome --remote-debugging-port=9222
            chrome_options.debugger_address = "localhost:9222"#指定程序窗口要提前设置启动端口
            chrome_options.binary_location = __browser_url
            self.base_driver = webdriver.Chrome(chrome_options=chrome_options)
            # self.base_driver=webdriver.Chrome()
            self.base_driver.get(self._dr_url)
            self.base_add_cookie()
            self.base_driver.get(self._dr_url)
        else:
            self.base_driver=driver_base


        # 显示等待
        self.base_driver.implicitly_wait(3)
    def base_find(self,by,value):
        return self.base_driver.find_element(by=by,value=value)
    def base_finds(self,by,value):
        return self.base_driver.find_elements(by=by,value=value)
    def base_quit(self):
        return self.base_driver.quit()
    def bese_get_cookie(self):
        return self.base_driver.get_cookies()
    def base_add_cookie(self):
        cookies = json.load(open(os.path.dirname(__file__)+ "/get_cookie/cookie.json"))
        for cookie in cookies:
            # print(cookie)
            if 'expiry' in cookie:
                del cookie['expiry']
            self.base_driver.add_cookie(cookie)