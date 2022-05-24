import pywifi
from pywifi import *
import time
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import progressbar as pgb


def discon():
    wifi = PyWiFi()  # 创建一个无线对象
    ifaces = wifi.interfaces()[0]  # 获取第一个无线网卡
    ifaces.disconnect()
    cpk.unpathfilewrite("toptipMessage.message", "w", "已断开")


def connect(namessid, passwordkey):
    profile = pywifi.Profile()
    profile.ssid = namessid  # wifi名称
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = passwordkey  # 在此输入你的wifi密码
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    profile = iface.add_network_profile(profile)
    iface.connect(profile)
    time.sleep(2)  # 程序休眠时间5秒；如果没有此句，则会打印连接失败，因为它需要一定的检测时间
    if iface.status() == const.IFACE_CONNECTED:
        cpk.unpathfilewrite("toptipMessage.message", "w", "已连接")
        pgb.exite()
        cpk.message("网络", "已连接到网络")
    else:
        cpk.unpathfilewrite("toptipMessage.message", "w", "失败")
        pgb.exite()
        cpk.message("网络", "未能连接到网络")
