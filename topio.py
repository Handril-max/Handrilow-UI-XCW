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
from . import colorselect
import glob
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from . import windoweng
from shutil import *
from . import colorlib
from . import colorlib as hcol
from . import HMmenu, linker
from . import cpupack as cpk
from . import fileprocess as fp
from . import diskpart, devicetest
from shutil import copytree
from psutil import disk_partitions
from . import net, desklist
from . import whitetype as wtt
from . import threadpool as thdpol
from . import topiomould as tpmo
from . import Hfont
from . import consult
from . import desktopGrid
from . import H_taskbar
from .openHandrilow import set_path
from .openHandrilow import mouse
from .openHandrilow.net import set_connect
from .openHandrilow.sys_windoweng import *
from .H_welcome import index
from . import midwindow
from .openHandrilow import hf_textanaly as hfa
from .openHandrilow.sys_windoweng import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
fath_path = set_path.pwd()
t_x = 0
winnum = 0
# TOPMAINMENU
menuwidth = 8 #the width of each menu bar

def main():
    root = tk.Toplevel()
    root.wm_attributes("-topmost", True)
    filejob = open(fath_path + '/HandrilowOSLauncherCode/set/unblur.set', 'w')
    filejob.close()

    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        root.after(1000, nonea)
    nonea()

    A2 = 'white'
    A4 = 'black'
    A5 = A4
    A7 = A4
    root['background'] = A4

    bloud = None
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    # root.attributes('-transparentcolor',A4)
    sw = swc
    shd = round(25)
    w_box = round(15)
    fontsize = round(8)
    h_box = w_box
    sh = shd-0
    t_x = 0
    t_y = 0
    root.geometry('%dx%d+%d+%d' % (sw, sh, t_x, t_y))
    root.overrideredirect(True)
    root.config(cursor='circle')

    #f_top.geometry('%dx%d+%d+%d' % (sw-10, sh, x, y))
    butm = tk.Frame(root, width=sw, height=sh, bg=A4)
    butm.pack(side='top', fill='x', padx=0, pady=0)
    f_top = tk.Frame(butm, bg=A4)
    f_top.pack(side='left')
    f_top_r = tk.Frame(butm, bg=A4)
    f_top_r.pack(side='right')
    # root.overrideredirect(True)

    def topfill():  # 状态栏顶格
        global t_x
        for i in range(0, 7)[::-1]:
            t_x = 0
            t_y = 0
            root.geometry('%dx%d+%d+%d' % (sw, sh, t_x, t_y))
            root.update()

    def topfly():  # 状态栏悬浮
        global t_x
        for i in range(0, 7):
            t_x = 2*i
            t_y = i-3
            root.geometry('%dx%d+%d+%d' % (sw-(2*t_x), sh, t_x, t_y))
            root.update()
        butm.after(1200, topfill)

    def select(_):
        global t_x
        if t_x == 0:
            with open("iotest.psw", "r", encoding='utf-8') as f:
                data = f.read()
            if data == '0':
                thdpol.dissetp.thd(topfly())
                thdpol.dissetp.thd(midwindow.main())
            if data == '1':
                None
            else:
                None
        else:
            None
            # topfill()
            # thdpol.dissetp.thd(midwindow.main())

    # butm.bind_all('<Tab>',select)
    # butm.bind('<Motion>',select)

    def blur(_):
        os.remove(fath_path + '/HandrilowOSLauncherCode/set/unblur.set')
        cpk.topbg()
    #m3 = tk.PanedWindow(f_top, orient="vertical", bg=A5, width=1)
    #m3.pack(fill="both", expand=1)

    def deviced():
        print('device mould')

    ###########################################

    def enter_name(_):
        name.config(bg=nonea(), fg='white')

    def leave_name(_):
        name.config(bg=A5, fg='white')

    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(f_top, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imag = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/LOGOALL.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left', padx=menuwidth,pady=1)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)
    
#######################################################

# 系统菜单

    def enter_file(_):
        file.config(bg=nonea(), fg='white')

    def leave_file(_):
        file.config(bg=A5, fg='white')
    filetext = '访至'
    font = Hfont.fontchange(filetext)
    file = tk.Label(f_top, text=filetext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, activeforeground='#F0F0F0')
    file.bind('<Enter>', enter_file)
    file.bind('<Leave>', leave_file)
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=menuwidth, pady=1)
        file.update()

    def enter_idle(_):
        idle.config(bg=nonea(), fg='white')

    def leave_idle(_):
        idle.config(bg=A5, fg='white')
    idletext = '编辑'
    font = Hfont.fontchange(idletext)
    idle = tk.Label(f_top, text=idletext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, activeforeground='#F0F0F0')
    idle.bind('<Enter>', enter_idle)
    idle.bind('<Leave>', leave_idle)
    for i in range(5, 10)[::-1]:
        idle.pack(side='left', padx=menuwidth, pady=1)

        idle.update()

    def enter_fun(_):
        fun.config(bg=nonea(), fg='white')

    def leave_fun(_):
        fun.config(bg=A5, fg='white')
    funtext = '添加'
    font = Hfont.fontchange(funtext)
    fun = tk.Label(f_top, text=funtext, fg=A2, width=None, height=None,
                   bd=0, bg=A5, activeforeground='#F0F0F0')
    fun.bind('<Enter>', enter_fun)
    fun.bind('<Leave>', leave_fun)
    for i in range(5, 10)[::-1]:
        fun.pack(side='left', padx=menuwidth, pady=1)

        fun.update()

    def enter_win(_):
        win.config(bg=nonea(), fg='white')

    def leave_win(_):
        win.config(bg=A5, fg='white')

    def foldico():
        None
    wintext = '查阅'
    font = Hfont.fontchange(wintext)
    win = tk.Label(f_top, text=wintext, fg=A2, width=None, height=None,
                   bd=0, bg=A5, activeforeground='#F0F0F0')
    win.bind('<Enter>', enter_win)
    win.bind('<Leave>', leave_win)
    win.pack(side='left', padx=menuwidth, pady=1)

    def enter_powe(_):
        powe.config(bg=nonea(), fg='white')

    def leave_powe(_):
        powe.config(bg=A5, fg='white')
    powetext = '窗口'
    font = Hfont.fontchange(powetext)
    powe = tk.Label(f_top, text=powetext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, activeforeground='#F0F0F0')
    powe.bind('<Enter>', enter_powe)
    powe.bind('<Leave>', leave_powe)
    powe.pack(side='left', padx=menuwidth, pady=1)
    powe.update()

    def tip():
        with open("apppath.psw", "r", encoding='utf-8') as f:
            data1 = f.read()
        date = data1
        font = Hfont.fontchange(date)
        tiplabel.config(text=date)
        f_top.after(100, tip)
    tiplabel = tk.Label(f_top, text='font=(等线 ,10)', fg=A2, width=None, height=None,
                        bd=0, bg=A5, activeforeground='#F0F0F0')
    tiplabel.pack(side='left', padx=menuwidth, pady=1)
    tip()
#######################################################################################
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
        win11.config(bg=A5, fg='white')
    win11 = tk.Label(f_top, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_win11 = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/MAINDOCK9.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='left',padx=menuwidth,pady=1)
    win11.bind('<Enter>', enter_win11)
    # win11.bind('<Button-1>',colorset)
    win11.bind('<Leave>', leave_win11)
###################################################
    ###############################################

    def enter_powe2(_):
        powe2.config(bg=nonea(), fg='white')

    def leave_powe2(_):
        powe2.config(bg=A5, fg='white')

    def getusename():
        with open("usename.psw", "r") as f:
            data = f.read()
        date = data
        font = Hfont.fontchange(date)
        powe2.config(text=date)
        f_top.after(100, getusename)
    powe2 = tk.Label(f_top_r, text='font=(等线 ,10)', bg=A5, fg=A2,
                     width=None, height=None, bd=0)
    powe2.pack(side='right', padx=5, pady=0)
    getusename()

    def ctl(_):
        midwindow.main()
    # powe2.bind('<Button-1>',select)
    powe2.bind('<Enter>', enter_powe2)
    powe2.bind('<Leave>', leave_powe2)

    ###############################################

    def resize12(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image12.resize((width, height), Image.ANTIALIAS)

    def enter_win1112(_):
        win1112.config(bg='#D3D3D3', fg='white')

    def leave_win1112(_):
        win1112.config(bg=A5, fg='white')

    def nearfile(_):
        desklist.main()
    win1112 = tk.Label(f_top_r, text="Taskmgr", width=w_box,fg=A2,
                       height=h_box, bg=A5)
    pil_image12 = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/SHELL.png')
    w, h = pil_image12.size
    pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)
    tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
    win1112.config(image=tk_image12)
    win1112.pack(side='right', padx=2, pady=1)
    win1112.bind('<Enter>', enter_win1112)
    #win1112.bind('<Button-1>', nearfile)
    win1112.bind('<Button-1>', select)
    win1112.bind('<Leave>', leave_win1112)

    # 声音
    def voicerr(_):
        v1 = volume.GetMasterVolumeLevel()
        vv1 = str(round(((0-v1)/65.25)*100))
        cpk.message('当前音量',vv1)
    def enter_righttip(_):
        righttip.config(bg=nonea(), fg='white')
    def leave_righttip(_):
        righttip.config(bg=A5, fg='white')
    def resize(w, h, w_box, h_box, pil_image_righttip):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(f_top_r, text="Taskmgr",
                        width=w_box, height=h_box, bg=A5)
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/TOPRIGHTTIP.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.bind('<Button-1>',voicerr)
    righttip.bind('<Enter>',enter_righttip)
    righttip.bind('<Leave>',leave_righttip)
    righttip.pack(side='right', padx=0, pady=5)

    def gettime():
        timestr = time.strftime("%H:%M")
        lb.configure(text=timestr)
        f_top.after(100, gettime)

    def enter_lb(_):
        # lb.config(bg=nonea(),fg='white')
        None

    def leave_lb(_):
        # lb.config(bg=A5,fg='white')
        None
    lb = tk.Label(f_top_r, text='', bg=A5, fg=A2, bd=0,
                  activeforeground='#F0F0F0')
    lb.bind('<Enter>', enter_lb)
    # lb.bind('<Button-1>',time)
    lb.bind('<Leave>', leave_lb)
    lb.pack(side='right', pady=0, padx=5)
    gettime()

    fileexists1 = os.path.exists(
        fath_path + "/HandrilowOSLauncherCode/set/guding.set")
    fileexists2 = os.path.exists(
        fath_path + "/HandrilowOSLauncherCode/set/yidong.set")
    ###################################
    f_battery = tk.Frame(f_top_r,width=w_box, height=h_box,bg=A5)
    f_battery.pack(side='right')
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
        
        def resizein(w, h, w_box, h_box, pil_image):
            f1 = 1.0*w_box/w
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image_bain.resize((width, height), Image.ANTIALIAS)

        def barttery():
            battery = psutil.sensors_battery()
            percent = str(round(battery.percent))
            plug = str(battery.power_plugged)
            if plug == 'False':
                ba.configure(text=percent)
                bain.forget()
            else:
                ba.configure(text=percent)
                bain.pack(side='left')
                
            f_top.after(100, barttery)

        def batips(_):
            battery = psutil.sensors_battery()
            percent = str(round(battery.percent))
            cpk.message('当前电池', percent)
        ba = tk.Label(f_battery, bg=A5, fg='white', width=2*w_box, height=h_box+5,
                      activebackground=A2, bd=0, activeforeground='#F0F0F0', compound='center',
                      font=(font, 7, 'bold'))
        pil_image_ba = Image.open(
            fath_path + '/HandrilowOSLauncherCode/H_icon/BA.png')
        w, h = pil_image_ba.size
        pil_image_resized = resize(w, h, 2*w_box, h_box, pil_image_ba)
        tk_imageba = ImageTk.PhotoImage(pil_image_resized)
        ba.config(image=tk_imageba)
        ba.bind('<Button-1>', batips)
        ba.pack(side='left')
        
        bain = tk.Label(f_battery, bg=A5, fg=A2, width=w_box, height=h_box,
                      activebackground=A2, bd=0, activeforeground='#F0F0F0', compound='center')
        pil_image_bain = Image.open(
            fath_path + '/HandrilowOSLauncherCode/H_icon/BAIN.png')
        w, h = pil_image_bain.size
        pil_image_resized_in = resizein(w, h, 2*w_box, h_box, pil_image_bain)
        tk_imagebain = ImageTk.PhotoImage(pil_image_resized_in)
        bain.config(image=tk_imagebain)
        bain.pack(side='left')
        
        barttery()
    ######################################################  

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

    showok = tk.Label(f_top_r, text="Taskmgr",
                      width=w_box, height=h_box, bg=A5)
    pil_imags = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/NET.png')
    w, h = pil_imags.size
    pil_image_resizes = resizs(w, h, w_box, h_box, pil_imags)
    tks_imag = ImageTk.PhotoImage(pil_image_resizes)
    showok.config(image=tks_imag)
    showok.pack(side='right')

    def ifcon():
        net_value = set_connect.chack_net_con.main()
        if net_value == 'True':
            statue.config(bg='#00CD66')
        elif net_value == 'False':
            statue.config(bg='red')
        else:
            statue.config(bg='orange')
        statue.after(1000, ifcon)
    statue = tk.Label(showok, width=2, height=1, bd=0, font=(None, 2))
    statue.place(x=w_box-6, y=w_box-5)
    ifcon()

    showok.bind('<Enter>', enter_showok)
    showok.bind('<Leave>', leave_showok)
    showok.bind('<Button-1>', netlist)

    # 顶栏提示
    def statue1():
        with open("toptip.message", "r", encoding='utf-8') as f:
            data1 = f.read()
        date = data1
        font = Hfont.fontchange(date)
        tiplabel12.config(text=date)
        f_top_r.after(100, statue1)
    tiplabel12 = tk.Label(f_top_r, text='font=(等线 ,10)', fg=A2, width=None, height=None,
                        bd=0, bg=A5, activeforeground='#F0F0F0')
    tiplabel12.pack(side='right', padx=5, pady=0)
    statue1()

    def getword4():
        with open("toptipMessage.message", "r", encoding='utf-8') as f:
            data4 = f.read()
        powe14.config(text=data4)
        powe14.after(100, getword4)

    def geteci(_):
        cpk.unpathfilewrite("toptipMessage.message", "w", "")
    powe14 = tk.Label(f_top_r, text='font=(等线 ,10)', fg=A2, width=None, height=None,
                      bd=0, bg=A5, activeforeground='#F0F0F0')
    powe14.pack(side='right', padx=5, pady=0)
    powe14.bind('<Button-1>', geteci)
    getword4()

    def handril_menu(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/m1.pid"
        fp.mainsys(pids)
        HMmenu.handrilmenu()
    name.bind('<Button-1>', handril_menu)

    def order(_):
        foldico()
        consult.main()
    win.bind('<Button-1>', order)

    fcen = tk.Frame(f_top, bg=A5)
    fcen.pack(side='right', pady=2)

    def colorset(_):
        colorselect.main()
    win11.bind('<Button-1>', colorset)

    def fangzhi(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/fangzhi.pid"
        fp.mainsys(pids)
        HMmenu.fangzhi()
    file.bind('<Button-1>', fangzhi)

    def ide(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/bianji.pid"
        fp.mainsys(pids)
        HMmenu.bianji()
    idle.bind('<Button-1>', ide)

    def dockwindow(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/windowmenu.pid"
        fp.mainsys(pids)
        HMmenu.windowmenu()
    powe.bind('<Button-1>', dockwindow)

    def add(_):
        HMmenu.add()
    fun.bind('<Button-1>', add)

    def post(event):
        x = event.x_root
        cpk.unpathfilewrite("postx.psw", "w", str(x))
    f_top.bind('<Motion>', post)
    #H_taskbar.main()
    
    root.mainloop()
