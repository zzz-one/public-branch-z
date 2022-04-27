import json
import time

from mySelenium.page_main import PageMain
main=PageMain()
time.sleep(20)
cookies=main.bese_get_cookie()
print(cookies)
with open("cookie.json", "w") as f:
    json.dump(cookies,f)
main.base_quit()