# py:3
# HandrilOS@Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril calender
# -*- coding:utf-8 -*-
from tkinter import *  # 或其他GUI库
import os
import time
import datetime
from HandrilowOSLauncherCode import colorlib  # 颜色库
from HandrilowOSLauncherCode import Hmessage, topbase  # 消息引擎和顶栏引擎的库
from shutil import *
from HandrilowOSLauncherCode import Hmessage  # 消息列队库
from HandrilowOSLauncherCode import cpupack  # 调度库
from HandrilowOSLauncherCode import cpupack as cpk
# 这些必须导入，是系统API部分的库
# 顶部菜单模块


def top(ts1, ts2, ts3, ts4, ts5):
    import windoweng
    t1 = ts1  # soft title
    t2 = ts2  # soft frist statue
    t3 = ts3  # soft second statue
    t4 = ts4  # soft thrid statue
    t5 = ts5  # soft forth statue
    windoweng.topdock(t1, t2, t3, t4, t5)


def mainsys(pid):
    # 系统模块进程
    fileexists = os.path.exists(pid)
    # 进程锁文件（控制进程数的关键也在此）
    if fileexists == True:
        # 判断进程文件是否存在，若有则阻止启动，若无，则创建进程文件及进程
        cpk.unpathfilewrite("toptipMessage.message", "w", "系统冲突！无二次权限!")
        Hmessage.random('Handrilow系统', '注意右顶栏提示')
        print("system lock has be launched")
    else:
        file = open(pid, 'w')
        file.close()


def mainsysa(pid, root):
    # 系统模块进程
    fileexists = os.path.exists(pid)
    # 进程锁文件（控制进程数的关键也在此）
    if fileexists == True:
        # 判断进程文件是否存在，若有则阻止启动，若无，则创建进程文件及进程
        # Hmessage.random('Handrilow系统','此模块无二次启动权限')
        root.destroy()
        os.remove(pid)
    else:
        file = open(pid, 'w')
        file.close()

# 应用功能模块


def mainapp(pid):
    # 文件进程判断
    fileexists = os.path.exists(pid)
    # 进程文件夹及进程文件
    fileexists1 = os.path.exists(
        "./HandrilowOSLauncherCodeH_fileprocess/check/存在")
    # 进程锁文件（控制进程数的关键也在此）
    if fileexists == True:
        # 判断进程文件是否存在，若有则阻止启动，若无，则创建进程文件及进程
        Hmessage.random('Handrilow系统', '此应用无二次启动权限')
        exit()
    else:
        file = open(pid, 'w')
        filejob = open('./HandrilowOSLauncherCodeH_fileprocess/check/存在', 'w')
        file.close()
        filejob.close()
    if fileexists1 == True:
        os.remove(pid)
        Hmessage.random('进程锁', '请关闭当前的应用')
        # 若存在进程锁文件，则无法启动设定数量以外的进程
        exit()
    else:
        pass


def main(pid):
    # 文件进程判断
    fileexists = os.path.exists(pid)
    # 进程锁文件（控制进程数的关键也在此）
    if fileexists == True:
        # 判断进程文件是否存在，若有则阻止启动，若无，则创建进程文件及进程
        Hmessage.random('Handrilow系统', '此应用无二次启动权限')
    else:
        file = open(pid, 'w')
        file.close()
# 以下便是应用对应的功能模块，但必须是在main函数之下
# 退出函数


def exitesys(root, pid):
    root.destroy()
    os.remove(pid)  # 清除系统进程文件


def cls():
    os.remove('./HandrilowOSLauncherCodeH_fileprocess/check/存在')  # 清除进程锁文件


def exite(root, pid):
    cls()
    for i in range(0, 200, 10)[::-1]:
        root.attributes('-alpha', i/100)
        root.update()
        time.sleep(0.013)
    root.destroy()
    os.remove(pid)  # 清除进程文件
