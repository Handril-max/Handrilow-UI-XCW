# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# main
# Handril cpk
# -*- coding:utf-8 -*-
import os

from HandrilowOSLauncherCode import (Hmessage, HMmenu, Horder, bottomfunic,
                                     deskfunic, desktop)
from HandrilowOSLauncherCode import fileprocess as fp
from HandrilowOSLauncherCode import game, linker
from HandrilowOSLauncherCode import lockscreen as lsc
from HandrilowOSLauncherCode import logicmem as lmem
from HandrilowOSLauncherCode import login
from HandrilowOSLauncherCode import midwindow as midwin
from HandrilowOSLauncherCode import note, prtsc, searchWindows
from HandrilowOSLauncherCode import topbase
from HandrilowOSLauncherCode import topbase as tbs
from HandrilowOSLauncherCode import topio as tio
from HandrilowOSLauncherCode import whitetype as wtp
from HandrilowOSLauncherCode import windoweng as weg
from HandrilowOSLauncherCode import dockMode

#dockmode
def deskDockMode(path):
    dockMode.main(path)
# musicsearchwindow
def MusicSearchWindow(root):
    searchWin = SearchWindows(root)
    searchWin.run()
# 中值窗口


def midpasswin():
    midwin.main()
# 缩放值


def rate():
    b = sr.main()
    return b
# exe or deb linker


def lnk(cmd):
    linker.launch(cmd)


def killlnk(cmd):
    linker.killprocess(cmd)
# game


def togame():
    game.main()
# 文本编辑


def notetype():
    note.main()
# 屏幕截图


def printscreen():
    prtsc.main()


def prtscother():  # 截图并保存文件
    prtsc.mainlock()
# 文件写入
#write text to file###


def unpathfilewrite(filename, statue, result):
    lmem.FileOperate.unpathfilewrite(filename, statue, result)
#make a file in path###


def pathfilewrite(path, statue):
    lmem.FileOperate.pathfilewrite(path, statue)
# 文件读取


def readfile(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data


# 锁屏
'''
引用：cpk.lockpart()
'''


def lockpart():
    lsc.main()


def loginto():
    login.main()
    None


# 锁屏和登录判断&逻辑组
'''
引用：cpk.lockorlogin【锁或登录】/unlockmould【解锁】()
'''
# bease


def beaselogic(what, sth, sthl, condition1, condition2):
    lmem.BeaseLogic.fel(what, sth, sthl, condition1, condition2)
# compare###what###noelse


def compaerLogicMax(what, sth, sthl, condition1):
    lmem.BeaseLogic.felCompareMorethingMax(what, sth, sthl, condition1)


def compaerLogicMin(what, sth, sthl, condition1):
    lmem.BeaseLogic.felCompareMorethingMin(what, sth, sthl, condition1)
# compare###what###else


def compElselogicMax(what, sth, sthl, condition1, condition2):
    lmem.BeaseLogic.felCompareMax(what, sth, sthl, condition1, condition2)


def compElselogicMin(what, sth, sthl, condition1, condition2):
    lmem.BeaseLogic.felCompareMin(what, sth, sthl, condition1, condition2)
# compare###nowhat###noelse


def compNowhatLogicMax(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMorethingMax(sth, sthl, condition1, condition2)


def compNowhatLogicMin(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMorethingMin(sth, sthl, condition1, condition2)


def compPrintNowhatLogicMax(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMorethingMax(sth, sthl, x, condition1)


def compprintNowhatLogicMin(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMorethingMin(sth, sthl, x, condition1)
# compare###nowhat###else


def compelseNowhatLogicMax(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMax(sth, sthl, condition1)


def compelseNowhatLogicMin(sth, sthl, condition1):
    lmem.BeaseLogic.delCompareMax(sth, sthl, condition1)
# i###nowhat###noelse


def moreIn(sth, sthl, condition1):
    lmem.BeaseLogic.delMorethingIn(sth, sthl, condition1)


def lockorlogin():
    None
    lmem.lockandlogin()


def unlockmould():
    None
    lmem.unlockpart()


# 桌面
'''
引用：
cpk.mainscreen()
cpk.top()
cpk.deskico()
cpk.dicoset()
'''


def mainscreen():
    desktop.main()


def top():
    topbase.topmenu()


def deskico():
    deskfunic.main()


def dicoset():
    if os.path.exists("./set/dico.set") == False:
        None
    else:
        deskico()


# 小白条
'''
引用：cpk.type()[系统小白条]
cpk.atp(root)[应用小白条]
cpk.atprandom(root,function)[自定义小白条]
'''


def free():
    wtp.free()


def type(root):
    wtp.main(root)


def atp(root):
    wtp.apptype(root)


def atprandom(root, function):
    wtp.apptyperandom(root, function)


def atprandomto(root, pid):
    wtp.apptyperandomto(root, pid)


# 命令
'''
引用：cpk.order()
'''


def order():
    Horder.main()


# 状态栏
'''
引用：cpk.topbg【毛玻璃背板】/topfunc()【功能模组】
'''


def topbg():
    tbs.topmenu()


def topfunc():
    tio.main()


# 消息列队
'''
引用：cpk.message(title,ags)
title:消息标题
ags:消息内容
'''


def messageroot(title, ags):
    Hmessage.randomroot(title, ags)


def message(title, ags):
    Hmessage.random(title, ags)


def qmessage(title, ags):
    Hmessage.qrandom(title, ags)


# 程序坞接口
'''
引用：cpk.bfn()
'''


def bfn():
    bottomfunic.dock()


# 开机登录窗口
'''
引用：cpk.f_loglock/f_logshow()
'''


def f_loglock():
    login.lock()


def f_logshow():
    login.main()


# 窗口容器大小定义
'''
引用：cpk.fathersize(root)
root:窗口名称
sw,sh:窗口宽高
num1,num2: x,y值（坐标值）
'''


def fathersize(root, sw, sh, num1, num2):
    weg.screensize(root, sw, sh, num1, num2)


# 全屏
'''
引用：cpk.overide(root)
root:窗口名称
'''


def overide(root):
    weg.fullscreen(root)


# win窗口
'''
引用：cpk.winride(root)
root:窗口名称
'''


def winride(root):
    weg.winscreen(root)


# 渐显渐隐动画   (固定值，数值型)
'''
引用：cpk.graduallyin/graduallyout(assembly,root,num1,num2,num3),
assembly:控件名称
root:窗口名称
num1、num2:.place下x,y（坐标值）
'''


def graduallyin(assembly, root, num1, num2):
    weg.gradually_a_in(assembly, root, num1, num2)


def graduallyout(assembly, root, num1, num2):
    weg.gradually_a_out(assembly, root, num1, num2)


#渐显渐隐动画  (非固定)
'''
引用：cpk.graduallyinsc/graduallyoutsc(root,num1,num2,num3),
root:窗口名称
num1、num2、num3:对应语句为
for i in range(num1,num2,num3)[::+-1]
'''


def graduallyinsc(root, num1, num2, num3):
    weg.gradually_b_in(root, num1, num2, num3)


def graduallyoutsc(root, num1, num2, num3):
    weg.gradually_b_out(root, num1, num2, num3)


# 窗口移除和移入动画-横向
'''
引用：cpk.father_movein/father_moveout(root,num1,num2,num3,x,y,sh),
root:窗口名称
num1、num2、num3:对应语句为
for i in range(num1,num2,num3)[::+-1]
x,y:窗口位置
sh(或sw):窗口高（宽）
'''


def father_movein(root, num1, num2, num3, x, y, sh):
    weg.fathermovein(root, num1, num2, num3, x, y, sh)


def father_moveout(root, num1, num2, num3, x, y, sh):
    weg.fathermoveout(root, num1, num2, num3, x, y, sh)


# place型-横向出入
'''
引用：cpk.moveinto/moveoutto(assembly,num1,num2,num3),
assembly:控件名称
num1:起始值
num2:终值
num3:.place下x值，整数型
'''


def moveinto(assembly, num1, num2, num3):
    weg.move_in(assembly, num1, num2, num3)


def moveoutto(assembly, num1, num2, num3):
    weg.move_out(assembly, num1, num2, num3)


# pack型定值-纵向出入
'''
引用：cpk.mpinto/mpoutto(assembly,num0,num1,num2),
assembly:控件名称
num1:起始值
num2:终值
num0:.pack下pady值，整数型
'''


def mpinto(assembly, num0, num1, num2):
    weg.move_p_in(assembly, num0, num1, num2)


def mpoutto(assembly, num0, num1, num2):
    weg.move_p_out(assembly, num0, num1, num2)


# pack非定值型-横向出入
'''
引用：cpk.mqinto/mqoutto(assembly,where,num0,num1,num2),
assembly:控件名称
where:.pack下side条件，有且只有【top,left,right,bottom】
num1:起始值
num2:终值
num3:.pack下pady值，整数型
'''


def mqinto(assembly, where, num1, num2, num3):
    weg.move_q_in(assembly, where, num1, num2, num3)


def mqoutto(assembly, where, num1, num2, num3):
    weg.move_q_out(assembly, where, num1, num2, num3)


# 有方位纵向出入
'''
引用：cpk.mwinto/mwoutto(assembly,where,num0,num1,num2),
assembly:控件名称
where:.pack下side条件，有且只有【top,left,right,bottom】
num1:起始值
num2:终值
num0:.pack下padx值，整数型
'''


def mwinto(assembly, where, num0, num1, num2):
    weg.move_where_in(assembly, where, num0, num1, num2)


def mwoutto(assembly, where, num0, num1, num2):
    weg.move_where_out(assembly, where, num0, num1, num2)


# 文件进程调用
'''
引用：cpk.toptask(ts1,ts2,ts3,ts4,ts5)
expland t1 to t5:
soft title
soft frist statue
soft second statue
soft thrid statue
soft forth statue
'''


def toptask(ts1, ts2, ts3, ts4, ts5):
    fp.top(ts1, ts2, ts3, ts4, ts5)


def random(pid):
    fp.main(pid)


def sys(pid):
    fp.mainsys(pid)


def app(pid):
    fp.mainapp(pid)


def sysquite(root, pid):
    fp.exitesys(root, pid)


def appquite(root, pid):
    fp.exite(root, pid)


def showhide(write):
    unpathfilewrite("toptipMessage.message", "w", write)
    Hmessage.random('Handrilow系统', write)
