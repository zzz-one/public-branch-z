# @pytest.fixture(scope="session")#这个是目录级的，所有文件才会1次前后
# @pytest.fixture(scope="module")#脚本级，前后1次
# @pytest.fixture(scope="function")#脚本级，每个每次（要加形参）
# @pytest.fixture(scope="class")#类级，类前后1次（类里的第一个形参为头）
import pytest


@pytest.fixture(autouse=True)#默认scope=function，全部函数、方法(不用形参)
def loginA2():
    print("这是autouse2登录")
    return "autouse2返回值"

@pytest.fixture(scope="session")#这个是目录级的，所有文件才会1次前后
def loginA3():
    print("这是session2登录")
    return "session2返回值"
@pytest.fixture(scope="function")
def loginA4():
    print("这是function4登录")
    return "function4返回值"
@pytest.fixture()
def loginA5():
    print("这是fixture5登录")
    return "fixture5返回值"