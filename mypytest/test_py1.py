import pytest

from beTest.calculator import Calculator
'''
第一点：class内一定要self，否则内存不通
'''
def setup_function():
    print("这里是每次函数开头")
def teardown_function():
    print("这是每次函数结尾")
def setup_module():
    print("这里是1次函数开头——setup_module")
def teardown_module():
    print("这是1次函数结尾——teardown_module")
def test_a1():
    print("a1")
def test_a2():
    print("a2")
class TestMy:

    def setup_class(self):
        print("这里是1次类开头setup-class")
    def teardown_class(self):
        print("这里是1次类结尾teardown——class")
    def setup(self):
        print("这里是每次setup")
        self.cal=Calculator()
    def teardown_method(self):
        print("这里是每次teardown")
    @pytest.mark.xfail
    def test_add1(self):
        # cal = Calculator()
        assert 3==self.cal.add(1,3)
    @pytest.mark.add
    def test_add2(self):
        # cal = Calculator()
        assert 3==self.cal.add(1,2)
    def test_subtract(self):
        assert 4==self.cal.subtract(6,2)