import random
def test001_input():
    """
    # test01-输入+随机数+格式化输出
\n————————————————
\n 1.choice选择
\n 2.range范围，range100就是（1,100）choice可用，randint不可用，randint只接受整数型
\n 3.randint直接随机的方法
    :return:
    """
    # number=random.choice(range(100))
    number=random.randint(1,100)
    name=input("请输入您的名字：")
    print("恭喜%s获得了"%name,number)
def test002_IsChinese() :

    """
    #test02-加载文件、读取文件+分割+遍历+utf8符
\n————————————————
 #问题1：str不支持&与运算符
介绍：if not '\u4e00' <= c & c <= '\u9fff':这样是错的，python中只有二进制支持&与运算符
  解决办法:
第一种方式and
 if not c>='\u4e00' and c<= '\u9fff':
第二种方式直接写
 if not '\u4e00' <= c <= '\u9fff':
\n————————————————
 #问题2：utf符的看法
    :param:
    :return:
    """
    f=open("file.ini","r",encoding="utf-8")
    print("这是文件对象",f)
    f_read=f.read()
    f_list=f_read.split("\n")
    print("这是文件文本：", f_list)
    i=1
    for one_f in f_list:
        tips=""
        for c in one_f:
            if not c>='\u4e00' and c<= '\u9fff':
            # if not '\u4e00' <= c <= '\u9fff':
                tips=tips+c
        if tips:
            # print("文本的第%s行:"%i,one_f,"包含非中文字符"+tips)旧式字符串格式化
            print("文本的第%s行:%s包含非中文字符%s"%(i,one_f,tips))
        i=i+1

def test03_error_test():
    file=open("file.ini","r",encoding="utf-8")
    file_list=file.readlines(100)
    print(file_list)
    print(hex(ord("中")))
    print(ord("中"))
    print(u"中")
    print("\u4e2d")
    print("\u4e00")
    print("\u9eee")
    print(chr(20013))



def test04_test_cards():
    # str="最热、搜索关键字、主播评论数、播放量、更新数、播放增长率"
    str2="书籍主播、节目主播、书籍/节目主播"
    str="周榜、月榜、总榜"
    list=str.split("、")
    list2=str2.split("、")
    for i in list:
        for j in range(1,4):
            print("2.%s-" %j + "%s" % i + "有" + list2[j - 1])
    # j=1
    # for i in list:
    #     # print("1.%s-"%j+"配置%s"%i+"榜")
    #     for
    #     print("1.%s-"%j+"%s"%i+"有"+list2[j-1])
    #     j=j+1
test002_IsChinese()
