# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import sys


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
    print("n1、、、、、、、、、、、这里是列表、、、、、、、、、、、、、、、、、")
    for i in range(1,4):
        print(i)
    list=[i**2 for i in range(1,4) if i!=1]
    print(list)
    print("n2、、、、、、、、、、、这里是元组、、、、、、、、、、、、、、、、、")
    tuple=1,2,4
    print("{0}:{1}".format(tuple,type(tuple)))
    print("{0}:{1}".format(123,456))
    print(id(tuple),"\n1sss")
    print(id(tuple[0]))
    print(type(id(tuple[0])))
    print(type(id(tuple[0])))
    """
    c2-这里是元组的更改
    """
    a=["a","b","c"]
    tuple2=1,2,a
    print(tuple2)
    tuple2[2][0]=1
    print(tuple2)
    print("n3、、、、、、、、、、、这里是集合、、、、、、、、、、、、、、、、、")

    print("L3、、、、、、、、、、、这里是字符串、、、、、、、、、、、、、、、、、")
    string="12345678"
    print(string[1:5])
    print(range(101))
    print(range(1,100))
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
import requests
print(sys.path)
print(os.getcwd())
print(os.path.abspath(__file__))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
