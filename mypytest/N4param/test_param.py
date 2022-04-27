import pytest
#第一种，手写
import yaml
@pytest.mark.parametrize("a,b,c",
                         [
                             [1,2,3],
                             (1,2,33),
                             (1,2,333),
                         ],ids=[
        "number1","数字number2","number3"
    ])
def test_a(a,b,c):
    print(a,b,c)
#第二种，ymal

aaa=yaml.safe_load(open("../beTest/param.yaml"))
aaa1=yaml.safe_load(open("../beTest/param2.yaml"))
#调试只能看逻辑问题，不要看错误❌问题
@pytest.mark.parametrize("a,b,c",aaa,ids=[
        "number1","number2","number3"
    ])
def test_b(a,b,c):
    print(aaa1)
    print(a,b,c)
class TestFix:
    def test_c(self):
        print("test-c1")
def check_b():
    print("check")
class CheckFix:
    def test_c(self):
        print("test-c1")