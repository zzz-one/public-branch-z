import json
import time

from mySelenium.page_main import PageMain


def test_cookielogin():
    main=PageMain()
    # cookies = json.load(open("cookie.json"))
    # for cookie in cookies:
    #     print(cookie)
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
    #     main.base_driver.add_cookie(cookie)
    # main.base_driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(10)
    main.base_quit()