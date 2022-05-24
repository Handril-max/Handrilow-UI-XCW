# py:3
# HandrilOS@Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril thread pool v1.0
# -*- coding:utf-8 -*-
import threading
import shutil
import os
from HandrilowOSLauncherCode import cpupack as cpk
# threadcore 1 [covered 32 son core]
# 线程列表
thlist = []

# 线程数

def num_thlist():
    result = len(thlist)
    return result
# 注册表事件写入函数


def thdadd(targetnames):
    thlist.append(str(targetnames))


class dissetp():
    # 5核心线程—异步线程核心组
    '''
    描述：开启后，主线程继续往下执行代码，直到代码执行完毕，主线程结束了自己所有的任务，但是这个时候主线程并没有退出，也就是没有自动销毁，它在等待自己
        的子线程执行完毕，直到自己所有的子线程执行完毕后，主线程才会从程序中销毁，至此，所有的任务结束，所以我们可以把耗时的任务交给子线程去做，这样也就做
        到了异步的效果。
    '''
    def thdt(targetname, argse):
        thdadd(targetname)
        t = threading.Thread(target=targetname, args=argse)
        t.start()

    def thd(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()

    def thd2(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()

    def thd3(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()

    def thd4(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()

    def thd5(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()


class consetp():
    # 5核心线程—同步线程核心组
    '''
    描述：同步跟异步正好是相反的，当主线程遇到同步线程的时候，即遇到join()的时候会等待（即主线程进入堵塞状态，无法继续前行）所有的同步线程执行完毕之后，
        主线程才继续往下走，这里说的同步是针对主线程而言，意思是遇到join的时候，主线程会被堵塞，不会继续往下执行其它程序，而是等待join的线程执行完毕后再往下
        执行，而多个join的子线程之间是并行的，即互不影响。

    '''
    def thd(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()
        t.join()

    def thd2(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()
        t.join()

    def thd3(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()
        t.join()

    def thd4(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()
        t.join()

    def thd5(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.start()
        t.join()


class watchsetp():
    # 5核心线程—守护线程核心组
    '''
    描述：设置为守护线程之后，主线程一旦结束，就会退出，也就是自动销毁，不会等待子线程，主线程一旦销毁，则所有的子线程也会跟着销毁，无论任务是否执行完成，
        可以理解为一个大将军带领一群小兵去打仗，所谓擒贼先擒王，一旦将军牺牲了，则其它的小兵也不会继续作战，直接退出战场，因为他们是来守护主线程(将军)的。
    '''
    def thd(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.setDaemon(True)
        t.start()

    def thd2(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.setDaemon(True)
        t.start()

    def thd3(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.setDaemon(True)
        t.start()

    def thd4(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.setDaemon(True)
        t.start()

    def thd5(targetname):
        thdadd(targetname)
        t = threading.Thread(target=targetname)
        t.setDaemon(True)
        t.start()

# 自检程序核心


def check(pids, function1, function2):
    #pids = './HandrilowOSLauncherCode/H_fileprocess/cammer_transter.pid'
    cpk.pathfilewrite(pids, 'w')
    fileexists = os.path.exists(pids)
    if fileexists == True:
        # tpmo.cammer_transfer(fcen,w_box,h_box)
        function1
        pass
    else:
        function2
        pass
    # m3.after(1000,check.cammer)


def check_more(pids, function1, function2, function3, function4):
    #pids = './HandrilowOSLauncherCode/H_fileprocess/cammer_transter.pid'
    cpk.pathfilewrite(pids, 'w')
    fileexists = os.path.exists(pids)
    if fileexists != True:
        # tpmo.cammer_transfer(fcen,w_box,h_box)
        function1
        function2
        pass
    elif fileexists != False:
        function3
        function4
        pass
    # m3.after(1000,check.cammer)
