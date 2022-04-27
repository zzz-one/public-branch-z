import os

from mySelenium.page_main import PageMain
import time

class TestMain:
    def setup(self):
        self.main=PageMain()
    def test_addMember(self):
        self.main.goto_add_member().add_menber(name="2",memberId='2',memberEmail="2",menmPhone="13388881000")
        # assert "xx" in self.main.goto_add_member().getMemberList()
    def teardown(self):
        time.sleep(5)
        # self.main.base_quit()
def test_ospath():
    f=open("get_cookie/cookie.json")
    print(os.getcwd())#不好用，自己调用返回自己路径，被别人调用返回别人路径
    print("dddddda+++++++++++")
    print(f.readlines())
    print(os.path.abspath(__file__))
    #文件完整路径
    print(__file__)
    #文件完整路径
    print(os.path.dirname(__file__))
    #文件夹完整路径
    print(os.path.dirname(os.path.abspath(__file__)))
    #文件夹完整路径
    print(os.path.dirname(os.path.dirname(__file__)))
    #文件夹的上级文件夹完整路径
def test_osstr():
    Path1 = 'home'
    Path2 = 'develop'
    Path3 = 'code'
    Path10 = Path1 + Path2 + Path3
    Path20 = os.path.join(Path1, Path2, Path3)
    print("\n")
    print(Path10)
    print(Path20)