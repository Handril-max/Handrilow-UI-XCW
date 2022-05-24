# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# bottomtype
# -*- coding:utf-3 -*-
import os , time
import sys
import six
import shutil
from HandrilowOSLauncherCode import linker
import tkinter as tk
from tkinter import *
from PIL import *
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import windoweng


def topshow(mpx):
    A4 = 'black'
    rootA = tk.Toplevel()
    rootA.wm_attributes("-topmost", True)
    rootA['background'] = A4
    rootA.attributes('-transparentcolor', A4)
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    swx = 20
    if 800 <= sw <= 1366:
        y = round(sh*(27/768))
        shy = y-round(sh*(20/768))
    elif 1366 < sw <= 1920:
        y = round(sh*(22/768))
        shy = y-round(sh*(20/768))
    x = int(mpx)-10
    cpk.fathersize(rootA, swx, shy, x, y)
    cpk.overide(rootA)

    def exite():
        # cpk.mwoutto(bottomtype,'bottom',0,0,3)
        rootA.destroy()
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2():
        cpk.mwoutto(bottomtype, 'left', 0, 0, 3)
        exite()

    bottomtype = tk.Label(rootA, image=photo, bd=0, width=5, height=3)
    cpk.mwinto(bottomtype, 'left', 0, 0, 3)
    bottomtype.after(1100, jump2)


def free():
    A4 = 'black'
    rootA = tk.Toplevel()
    rootA.wm_attributes("-topmost", True)
    rootA['background'] = A4
    rootA.attributes('-transparentcolor', A4)
    sw = 1000
    sh = 20
    cpk.fathersize(rootA, sw, sh, 0, 0)
    cpk.overide(rootA)

    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/TYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def mydock():
        None

    def jump2():
        cpk.mwoutto(bottomtype, 'top', 0, 3, 8)
        mydock()

    def jump1(_):
        cpk.mwinto(bottomtype, 'top', 0, 3, 10)
        jump2()

    bottomtype = tk.Label(rootA, image=photo, bd=0,
                          width=round(sw*(1/3)), height=5)
    bottomtype.bind('<Enter>', jump1)
    cpk.mwinto(bottomtype, 'top', 0, 0, 3)


def main(rootA):
    A4 = 'black'
    sw = rootA.winfo_screenwidth()

    def mydock(_):
        bottomtype.config(bg='#272727')
        cpk.unpathfilewrite("all_progress.psw", "w", "0")#进程操作标记文件：“1”为允许运行，“0”为禁止运行
        time.sleep(2.4)
        cpk.unpathfilewrite("all_progress.psw", "w", "1")
        bottomtype.config(bg='#F0F0F0')

    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/TYPE.png'
    photo = ImageTk.PhotoImage(file=filename)
    bottomtype = tk.Label(rootA, image=photo, bd=0,
                          width=round(sw*(1/3)), height=6,bg='#F0F0F0')
    bottomtype.bind('<Enter>', mydock)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 5)


def apptype(rootA):
    A4 = 'black'
    sw = rootA.winfo_screenwidth()

    def mydock():
        None

    def jump2():
        cpk.mwoutto(bottomtype, 'bottom', 0, 5, 10)
        mydock()

    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 5, 12)
        jump2()

    bottomtype = tk.Button(rootA, bd=1, width=round(
        sw*(1/3)), height=3, font=('等线', 1))
    bottomtype.bind('<Enter>', jump1)
    rootA.bind('<Tab>', jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 5)


def apptyperandom(root, function):
    def exite():
        function
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2():
        cpk.mwoutto(bottomtype, 'bottom', 0, 3, 8)
        exite()

    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 3, 10)
        jump2()

    def mydock(_):
        exite()

    bottomtype = tk.Label(root, image=photo, bd=0, width=100, height=5)
    bottomtype.bind('<Button-1>', mydock)
    bottomtype.bind('<Leave>', jump1)
    # bottomtype.bind('<Enter>',jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 3)


def apptyperandompid(root, pid):
    def exite():
        os.remove(pid)
        root.destroy()
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2():
        cpk.mwoutto(bottomtype, 'bottom', 0, 3, 8)
        exite()

    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 3, 10)
        jump2()

    def mydock(_):
        os.remove(pid)
        exite()

    bottomtype = tk.Label(root, image=photo, bd=0, width=100, height=5)
    # bottomtype.bind('<Button-1>',mydock)
    bottomtype.bind('<Leave>', jump1)
    # bottomtype.bind('<Enter>',jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 3)
