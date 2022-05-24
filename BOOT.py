# HandrilOS@Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril Start screen
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import shutil
import string
import glob
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import *
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from shutil import *
from HandrilowOSLauncherCode import desktop
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol
from HandrilowOSLauncherCode.openHandrilow import set_path
fath_path = set_path.pwd()
shutil.rmtree(fath_path+'/HandrilowOSLauncherCode/H_fileprocess')
os.mkdir(fath_path+'/HandrilowOSLauncherCode/H_fileprocess')
fath_path = set_path.pwd()


def start():
    dirs = fath_path+"/HandrilowOSLauncherCode/H_fileprocess/check"
    a = os.mkdir(dirs)
    dirsjob = fath_path+"/HandrilowOSLauncherCode/H_fileprocess/job"
    a1 = os.mkdir(dirsjob)

    def go_readywork():

        dirs1 = fath_path + "/HandrilowOSLauncherCode/set"
        shutil.rmtree(dirs1)
        os.mkdir(dirs1)
        battery = psutil.sensors_battery()
        if battery == None:
            print('<TIP>NO BATTERY')
            cpk.pathfilewrite(fath_path+'/HandrilowOSLauncherCode/set/guding.set', 'w')
        else:
            print('<TIP>BATTERY EXIST')
            cpk.pathfilewrite(fath_path+'/HandrilowOSLauncherCode/set/yidong.set', 'w')

        shutil.rmtree(fath_path+'/HandrilowOSLauncherCode/H_fileprocess')
        os.mkdir(fath_path+'/HandrilowOSLauncherCode/H_fileprocess')

        usenamefile = os.path.exists(
            fath_path + "/HandrilowOSLauncherCode/Musics")
        if usenamefile != False:
            print('<DIR>_Musics is ready')
        else:
            os.mkdir(fath_path + "/HandrilowOSLauncherCode/Musics")
        cpk.unpathfilewrite("wifistate.psw", "w", " ")
        cpk.unpathfilewrite("postx.psw", "w", " ")
        cpk.unpathfilewrite("posty.psw", "w", " ")
        cpk.unpathfilewrite("bluetooth_name.psw", "w", " ")
        cpk.unpathfilewrite("bluetooth_addr.psw", "w", " ")
        cpk.unpathfilewrite("desklist.psw", "w", "None")
        cpk.unpathfilewrite("deviceinfo.psw", "w", " ")
        cpk.unpathfilewrite("wifinameinfo.psw", "w", " ")
        filejob = open(
            fath_path + '/HandrilowOSLauncherCode/set/unblur.set', 'w')
        filejob.close()
        # 选择背景色
        if os.path.exists("selectbg.psw"):
            print('<file>selectbg.psw done')
        else:
            cpk.unpathfilewrite("selectbg.psw", "w", "#D3D3D3")
        # 选择字体色
        if os.path.exists("selectfg.psw"):
            print('<file>selectfg.psw done')
        else:
            cpk.unpathfilewrite("selectfg.psw", "w", "white")

        cpk.unpathfilewrite("systemorderlinework.order",
                            "w", " Handrilsoft@China Xian\n")
        cpk.unpathfilewrite("importlib.order", "w", " ")  # 动态引用
        cpk.unpathfilewrite("toptip.message", "w", " ")
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        bgfile = os.path.exists("black_bg.psw")
        if bgfile != False:
            print('<DIR>_BG is ready')
        else:
            cpk.unpathfilewrite("black_bg.psw", "w", "0")
        bgfile = os.path.exists("pic_path.path")
        if bgfile != False:
            print('<DIR>_BG_PATH is ready')
        else:
            cpk.unpathfilewrite(
                "pic_path.path", "w", "D:\Handrilow\HandrilowOSLauncherCode\H_Picture/")

        cpk.unpathfilewrite("apppath.psw", "w", "标签")
        desktop_path = fath_path + "/HandrilowOSLauncherCode/disk/allfile/desktop/"
        files_in_desk = os.listdir(desktop_path)   # 读入文件夹
        num_png = str(len(files_in_desk))
        cpk.unpathfilewrite("fileindesk.psw", "w", num_png)
        cpk.unpathfilewrite("selectfile.psw", "w", " ")
        cpk.unpathfilewrite("toptip.message", "w", " ")
        cpk.unpathfilewrite("tipname.psw", "w", "标签")
        cpk.unpathfilewrite("icopath.psw", "w", "004")
        cpk.pathfilewrite(fath_path+'/HandrilowOSLauncherCode/set/unblur.set', 'w')
        cpk.unpathfilewrite("iotest.psw", "w", "0")
        cpk.unpathfilewrite("suond.message", "w", "暂无播放")
        # 进程操作标记文件：“1”为允许运行，“0”为禁止运行
        cpk.unpathfilewrite("all_progress.psw", "w", "1")

    def welcompage():
        A1 = 'black'
        A2 = 'white'
        root = tk.Tk()
        root['background'] = A1
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()

        def autoexit():
            cpk.messageroot('提示', 's1366768')
            exit()

        def check():
            cpk.compelseNowhatLogicMin(sw, 3000, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 2560, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 2048, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1920, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1856, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1792, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1680, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1600, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1400, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1366, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 1280, print('pass'), autoexit())
            cpk.compelseNowhatLogicMin(sw, 800, print('pass'), autoexit())

        x = 0
        y = 0
        root.geometry("%dx%d+%d+%d" % (sw, sh, x, y))
        root.overrideredirect(True)
        filenamea = fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/H_START.png'
        photo = tk.PhotoImage(file=filenamea)

        def bgpart():
            cpk.mainscreen()

        def go():
            for i in range(0, 100, 5)[::-1]:  # 淡出
                root.attributes('-alpha', i/100)
                root.update()
                time.sleep(0.013)
            root.destroy()
            thdpol.dissetp.thd(bgpart)

        for i in range(0, 100, 5):  # 淡入
            root.attributes('-alpha', i/50)
            root.update()
            time.sleep(0.013)
        lb = tk.Label(root, bg='black', width=sw, height=sh)
        lb.configure(image=photo)
        lb.pack()

        # cpk.type()
        root.after(4000, go)
        root.mainloop()

    thdpol.dissetp.thd(go_readywork)
    thdpol.dissetp.thd(welcompage)
