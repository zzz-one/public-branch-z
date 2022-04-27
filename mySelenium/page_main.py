from selenium.webdriver.common.by import By

from mySelenium.base_main import BaseMain
from mySelenium.page_addMember import PageAddMember


class PageMain(BaseMain):
    _dr_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        self.base_find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return PageAddMember(self.base_driver)
    def goto_member_list(self):
        self.base_driver(By.ID,"menu_contacts")
        return