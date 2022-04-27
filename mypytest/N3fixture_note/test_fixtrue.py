import pytest


@pytest.fixture
def login1():
    print("这是登录")
    return "登录返回值"
# @pytest.fixture(autouse=True)#默认scope=function，全部函数、方法(不用形参)
# @pytest.fixture(scope="session")#这个是目录级的，所有文件才会1次前后（要加形参）
# @pytest.fixture(scope="module")#脚本级，前后1次（要加形参）
# @pytest.fixture(scope="function")#脚本级，每个每次（要加形参）
# @pytest.fixture(scope="class")#类级，类前后1次（要加形参）
@pytest.fixture(autouse=True)#默认scope=function，全部函数、方法(不用形参)
def loginA():
    print("这是autouse登录")
    return "autouse返回值"
@pytest.fixture(scope="module")#脚本级，前后1次
def login2():
    print("这是module登录")
    return "module返回值"
@pytest.fixture(scope='function')#脚本级，每个每次
def login3():
    print("这是function登录")
    return "function返回值"
@pytest.fixture(scope="class")#类级，类前后1次
def login4():
    print("这是class登录")
    return "class返回值"
def test_a1(login1):
    print(login1)


def test_a2(login2):
    print()
class TestFix:
    def test_c(self,login3):
        print("test-c1")
    def test_c1(self,login1,login4):
        print("test-c1")
    @pytest.mark.usefixtures("login1")
    def test_c2(self):
        print("test-c1")
    def test_c3(self):
        print("test-c1")
    def test_c4(self,login2):
        print("test-c1")