from selenium.webdriver.common.by import By

from mySelenium.base_main import BaseMain
from mySelenium.page_contacts import PageContacts


class PageAddMember(BaseMain):
    def add_menber(self,name,memberId,memberEmail,menmPhone):
        # 显示等待
        self.base_driver.implicitly_wait(3)
        self.base_find(By.ID,"username").send_keys(name)
        self.base_find(By.ID,"memberAdd_acctid").send_keys(memberId)
        self.base_find(By.ID,"memberAdd_biz_mail").send_keys(memberEmail)
        self.base_find(By.CSS_SELECTOR,".ww_telInput_mainNumber").send_keys(menmPhone)
        self.base_find(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
        return PageContacts(self.base_driver)