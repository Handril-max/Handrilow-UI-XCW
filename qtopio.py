# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril screen top status
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import six
import shutil
import string
from HandrilowOSLauncherCode import colorselect
import glob
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from HandrilowOSLauncherCode import windoweng
import pyautogui as pag
from shutil import *
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import colorlib as hcol
from HandrilowOSLauncherCode import HMmenu, linker
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import fileprocess as fp
from HandrilowOSLauncherCode import diskpart, devicetest
from shutil import copytree
from psutil import disk_partitions
from HandrilowOSLauncherCode import net, desklist
from HandrilowOSLauncherCode import whitetype as wtt
from HandrilowOSLauncherCode import webview as wwb

# TOPMAINMENU


def main():
    A2 = 'white'
    A3 = colorlib.cola3()
    A8 = colorlib.cola8()
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    filejob = open('./HandrilowOSLauncherCode/set/unblur.set', 'w')
    filejob.close()

    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        root.after(1000, nonea)
    #none = tk.Label(root,bg='white')
    # none.pack()
    nonea()

    A4 = 'white'
    A2 = 'black'
    A5 = A4
    A7 = A4
    root['background'] = A4
    font = '微软雅黑'
    root.attributes('-alpha', 0.95)
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    # root.attributes('-transparentcolor',A4)
    sw = swc
    if swc <= 1366:
        shd = round(shc*(27/768))
        w_box = round(shc*(22/768))
        fontsize = round(shc*(9/768))
    elif swc == 1440:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 1600:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 1680:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 1792:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 1856:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 1920:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 2048:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 2560:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
    elif swc == 3000:
        shd = round(shc*(20/768))
        w_box = round(shc*(19/768))
        fontsize = round(shc*(4/768))

    h_box = w_box
    sh = shd-1
    x = 5
    y = 5

    root.geometry('%dx%d+%d+%d' % (sw-2*x, sh, x, y))
    root.overrideredirect(True)

    def blur(_):
        os.remove('./HandrilowOSLauncherCode/set/unblur.set')
        cpk.topbg()
    m3 = tk.PanedWindow(root, orient="vertical", bg=A5, width=1)
    m3.pack(fill="both", expand=1)

    def deviced():
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                #  输出可移动驱动器符号
                cpk.showhide('发现usb驱动：' + driver)
                cpk.unpathfilewrite("deviceinfo,psw", "w", driver)

        m3.after(100, deviced)

    ###########################################

    def enter_name(_):
        name.config(bg=nonea(), fg='white')

    def leave_name(_):
        name.config(bg=A5, fg='black')

    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(m3, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imag = Image.open('./HandrilowOSLauncherCode/H_icon/LOGOALL.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left', padx=2, pady=1)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)


####################################################
    asd = tk.Label(m3, text='||', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    for i in range(5, 10)[::-1]:
        asd.pack(side='left', padx=5, pady=1)
        asd.update()
###################################################

    def enter_file(_):
        file.config(bg=nonea(), fg='white')

    def leave_file(_):
        file.config(bg=A5, fg='black')
    filename2 = r'./HandrilowOSLauncherCode/H_icon/POST.png'
    photofile = ImageTk.PhotoImage(file=filename2)
    file = tk.Label(m3, text='访至', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    file.bind('<Enter>', enter_file)
    file.bind('<Leave>', leave_file)
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=5, pady=1)
        file.update()

    def enter_idle(_):
        idle.config(bg=nonea(), fg='white')

    def leave_idle(_):
        idle.config(bg=A5, fg='black')
    filename3 = r'./HandrilowOSLauncherCode/H_icon/IDLE.png'
    photoidle = ImageTk.PhotoImage(file=filename3)
    idle = tk.Label(m3, text='编辑', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    idle.bind('<Enter>', enter_idle)
    idle.bind('<Leave>', leave_idle)
    for i in range(5, 10)[::-1]:
        idle.pack(side='left', padx=5, pady=1)

        idle.update()

    def enter_fun(_):
        fun.config(bg=nonea(), fg='white')

    def leave_fun(_):
        fun.config(bg=A5, fg='black')
    filename4 = r'./HandrilowOSLauncherCode/H_icon/FUN.png'
    photofun = ImageTk.PhotoImage(file=filename4)
    fun = tk.Label(m3, text='添加', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    fun.bind('<Enter>', enter_fun)
    fun.bind('<Leave>', leave_fun)
    for i in range(5, 10)[::-1]:
        fun.pack(side='left', padx=5, pady=1)

        fun.update()

    def enter_win(_):
        win.config(bg=nonea(), fg='white')

    def leave_win(_):
        win.config(bg=A5, fg='black')
    filename6 = r'./HandrilowOSLauncherCode/H_icon/WINDOW.png'
    photowin = ImageTk.PhotoImage(file=filename6)
    win = tk.Label(m3, text='查阅', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    win.bind('<Enter>', enter_win)
    win.bind('<Leave>', leave_win)
    for i in range(5, 10)[::-1]:
        win.pack(side='left', padx=5, pady=1)

        win.update()

    def enter_powe(_):
        powe.config(bg=nonea(), fg='white')

    def leave_powe(_):
        powe.config(bg=A5, fg='black')
    filename5 = r'./HandrilowOSLauncherCode/H_icon/SHELL.png'
    photopow = ImageTk.PhotoImage(file=filename5)
    powe = tk.Label(m3, text='窗口', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')

    powe.bind('<Enter>', enter_powe)
    powe.bind('<Leave>', leave_powe)
    for i in range(5, 10)[::-1]:
        powe.pack(side='left', padx=5, pady=0)

        powe.update()

####################################################
    def launchapp(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/applaunched.pid"
        cpk.pathfilewrite(pids, "w")
        path = './HandrilowOSLauncherCode/sys/programe'
        a = powe1.cget("text")
        reappath = path + '/' + a + '/' + a + '.exe'
        linker.launch(reappath, a)

    def enter_powe(_):
        powe1.config(bg=nonea(), fg='white')
        HMmenu.deskmenu()

    def leave_powe(_):
        powe1.config(bg=A5, fg='black')

    def getword():
        with open("tipname.psw", "r") as f:
            data = f.read()
        powe1.config(text=data)
        m3.after(100, getword)
    powe1 = tk.Label(m3, text='font=(等线 ,10)', fg=A2, width=None, height=None,
                     bd=0, bg=A5, font=(font, fontsize, "bold"), activeforeground='#F0F0F0')
    powe1.pack(side='left', padx=5, pady=0)
    powe1.bind('<Button-1>', launchapp)
    powe1.bind('<Enter>', enter_powe)
    powe1.bind('<Leave>', leave_powe)
    getword()

    asd = tk.Label(m3, text='||', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    asd.pack(side='left', padx=5, pady=1)
###################################################

    def resize1(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image1.resize((width, height), Image.ANTIALIAS)

    def enter_win111(_):
        win111.config(bg=nonea(), fg='white')

    def leave_win111(_):
        win111.config(bg=A5, fg='black')
    win111 = tk.Label(m3, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image1 = Image.open('./HandrilowOSLauncherCode/H_icon/SET.png')
    w, h = pil_image1.size
    pil_image_resized1 = resize1(w, h, w_box, h_box, pil_image1)
    tk_image1 = ImageTk.PhotoImage(pil_image_resized1)
    win111.config(image=tk_image1)
    win111.pack(side='right', padx=2, pady=1)
    win111.bind('<Enter>', enter_win111)
    # win111.bind('<Button-1>',rili)
    win111.bind('<Leave>', leave_win111)
    ###############################################

    def getusename():
        with open("usename.psw", "r") as f:
            data = f.read()
        powe2.config(text=data)
        m3.after(100, getusename)
    powe2 = tk.Label(m3, text='font=(等线 ,10)', bg=A5, fg='#000000',
                     width=None, height=None, bd=0, font=(font, fontsize, "bold"))
    powe2.pack(side='right', padx=5, pady=0)
    getusename()
    ###############################################

    def resize12(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image12.resize((width, height), Image.ANTIALIAS)

    def enter_win1112(_):
        win1112.config(bg=nonea(), fg='white')

    def leave_win1112(_):
        win1112.config(bg=A5, fg='black')

    def nearfile(_):
        desklist.main()
    win1112 = tk.Label(m3, text="Taskmgr", width=w_box,
                       height=h_box, bg=A5, font=(font, fontsize, "bold"))
    pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/SHELL.png')
    w, h = pil_image12.size
    pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)
    tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
    win1112.config(image=tk_image12)
    win1112.pack(side='right', padx=2, pady=1)
    win1112.bind('<Enter>', enter_win1112)
    win1112.bind('<Button-1>', nearfile)
    win1112.bind('<Leave>', leave_win1112)

    def gettime():
        timestr = time.strftime("%H:%M")
        lb.configure(text=timestr)
        m3.after(100, gettime)

    def enter_lb(_):
        # lb.config(bg=nonea(),fg='white')
        None

    def leave_lb(_):
        # lb.config(bg=A5,fg='black')
        None
    lb = tk.Label(m3, text='', bg=A5, fg=A2, bd=0,
                  activeforeground='#F0F0F0', font=(font, fontsize, "bold"))
    lb.bind('<Enter>', enter_lb)
    # lb.bind('<Button-1>',time)
    lb.bind('<Leave>', leave_lb)
    lb.pack(side='right', pady=0, padx=2)
    gettime()

    fileexists1 = os.path.exists("./HandrilowOSLauncherCode/set/guding.set")
    fileexists2 = os.path.exists("./HandrilowOSLauncherCode/set/yidong.set")
    ###################################
    if fileexists1 == True and fileexists2 == False:
        None
    elif fileexists2 == True and fileexists1 == False:
        # Battery Mode
        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0*w_box/w
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image_ba.resize((width, height), Image.ANTIALIAS)

        def barttery():
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            plug = str(battery.power_plugged)
            if plug == 'False':
                ba.configure(text=percent+'%', fg=A4, font=(font, 7, "bold"))
            else:
                ba.configure(text='插电', fg=A4, font=(font, 7, "bold"))
            m3.after(100, barttery)

        def batips():
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            Hmessage.random('电池状态', percent+'%')
        ba = tk.Label(m3, bg=A5, fg=A2, width=2*w_box, height=h_box,
                      activebackground=A2, bd=0, activeforeground='#F0F0F0', compound='center')
        pil_image_ba = Image.open('./HandrilowOSLauncherCode/H_icon/BA.png')
        w, h = pil_image_ba.size
        pil_image_resized = resize(w, h, 2*w_box, h_box, pil_image_ba)
        tk_imageba = ImageTk.PhotoImage(pil_image_resized)
        ba.config(image=tk_imageba)
        for i in range(0, 5)[::-1]:
            ba.pack(side='right')
            ba.update()

        barttery()

    def resize(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_win11.resize((width, height), Image.ANTIALIAS)

    def enter_win11(_):
        win11.config(bg=nonea(), fg='white')

    def leave_win11(_):
        win11.config(bg=A5, fg='black')
    win11 = tk.Label(m3, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_win11 = Image.open(
        './HandrilowOSLauncherCode/H_icon/MAINDOCK9.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='left', padx=2, pady=1)
    win11.bind('<Enter>', enter_win11)
    # win11.bind('<Button-1>',colorset)
    win11.bind('<Leave>', leave_win11)
    # 顶栏左间提示

    def statue1():
        with open("toptip.message", "r") as f:
            data1 = f.read()
        tiplabel.config(text=data1)
        m3.after(100, statue1)
    tiplabel = tk.Label(m3, text='font=(等线 ,10)', fg=A2, width=None, height=None,
                        bd=0, bg=A5, font=(font, fontsize, "bold"), activeforeground='#F0F0F0')
    tiplabel.pack(side='left', padx=5, pady=0)
    statue1()

    # 网络模块调用
    def enter_showok(_):
        showok.config(bg=nonea())

    def leave_showok(_):
        showok.config(bg=A5)

    def netlist(_):
        net.main()

    def discon(_):
        net.discon()

    def resizs(w, h, w_box, h_box, pil_images):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imags.resize((width, height), Image.ANTIALIAS)
    showok = tk.Label(m3, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imags = Image.open('./HandrilowOSLauncherCode/H_icon/NET.png')
    w, h = pil_imags.size
    pil_image_resizes = resizs(w, h, w_box, h_box, pil_imags)
    tks_imag = ImageTk.PhotoImage(pil_image_resizes)
    showok.config(image=tks_imag)
    showok.pack(side='right', padx=0)
    showok.bind('<Enter>', enter_showok)
    showok.bind('<Leave>', leave_showok)
    showok.bind('<Button-1>', netlist)
    showok.bind('<Button-3>', discon)

    # 顶栏右间消息辅助提示

    def enter_righttip(_):
        righttip.config(bg=nonea(), fg='white')

    def leave_righttip(_):
        righttip.config(bg=A5, fg='black')

    def resize(w, h, w_box, h_box, pil_image_righttip):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(m3, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_righttip = Image.open(
        './HandrilowOSLauncherCode/H_icon/TOPRIGHTTIP.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.pack(side='right', padx=0, pady=1)

    def showhide(_):
        mess = str(diskpart.update())
        cpk.showhide(mess)
    righttip.bind('<Button-1>', showhide)
    righttip.bind('<Enter>', enter_righttip)
    righttip.bind('<Leave>', leave_righttip)

    def statue2():
        with open("toptipMessage.message", "r") as f:
            data2 = f.read()
        tipMessageLabel.config(text=data2)
        m3.after(100, statue2)

    def enter_tipMessageLabel(_):
        tipMessageLabel .config(bg=nonea(), fg='white')

    def leave_tipMessageLabel(_):
        tipMessageLabel.config(bg=A5, fg='black')
    tipMessageLabel = tk.Label(m3, text='font=(等线 ,10)', fg=A2, width=None, height=None, bd=0, bg=A5, font=(
        font, fontsize, "bold"), activeforeground='#F0F0F0')
    tipMessageLabel.pack(side='right', padx=3, pady=0)

    def tiprclan(_):
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
    tipMessageLabel.bind('<Button-1>', tiprclan)
    tipMessageLabel.bind('<Enter>', enter_tipMessageLabel)
    tipMessageLabel.bind('<Leave>', leave_tipMessageLabel)
    statue2()
    # deviced()
    devicetest.main()

    def handril_menu(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/m1.pid"
        fp.mainsys(pids)
        HMmenu.handrilmenu()
    name.bind('<Button-1>', handril_menu)

    def order(_):
        #pids = "./HandrilowOSLauncherCode/H_fileprocess/order.pid"
        # fp.mainsys(pids)
        # HMmenu.order()
        cpk.message('查阅', '查看计算机资源')
    win.bind('<Button-1>', order)

    def colorset(_):
        colorselect.main()
    win11.bind('<Button-1>', colorset)

    def fangzhi(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/fangzhi.pid"
        fp.mainsys(pids)
        HMmenu.fangzhi()
    file.bind('<Button-1>', fangzhi)

    def ide(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/bianji.pid"
        fp.mainsys(pids)
        HMmenu.bianji()
    idle.bind('<Button-1>', ide)

    def dockwindow(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/windowmenu.pid"
        fp.mainsys(pids)
        HMmenu.windowmenu()
    powe.bind('<Button-1>', dockwindow)

    def web(_):
        pids = "./HandrilowOSLauncherCode/H_fileprocess/wwebview.pid"
        # fp.mainsys(pids)
        wwb.main()
    win111.bind('<Button-1>', web)

    def post(event):
        x = event.x_root
        cpk.unpathfilewrite("postx.psw", "w", str(x))
    root.bind('<Motion>', post)
    cpk.dicoset()
    # desklist.main()
    root.mainloop()
