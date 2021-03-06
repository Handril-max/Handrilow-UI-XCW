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
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from HandrilowOSLauncherCode import windoweng
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
from HandrilowOSLauncherCode import threadpool as thdpol
from HandrilowOSLauncherCode import topiomould as tpmo
from HandrilowOSLauncherCode import Hfont
from HandrilowOSLauncherCode import consult
from HandrilowOSLauncherCode import desktopGrid
from HandrilowOSLauncherCode import panel_whitetype as pwt
from HandrilowOSLauncherCode.openHandrilow import set_path
from HandrilowOSLauncherCode.openHandrilow import mouse

fath_path = set_path.pwd()

# TOPMAINMENU


def main():
    A2 = 'white'
    A3 = colorlib.cola3()
    A8 = colorlib.cola8()
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    #f_top = tk.Toplevel()
    #f_top.wm_attributes("-topmost", True)
    filejob = open(fath_path + '/HandrilowOSLauncherCode/set/unblur.set', 'w')
    filejob.close()

    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        f_top.after(1000, nonea)
    nonea()

    A4 = 'white'
    A2 = 'black'
    A5 = A4
    A7 = A4
    root['background'] = A4

    bloud = None
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    x = 0
    y = 0
    sw = swc
    if swc <= 1366:
        shd = round(shc*(27/768))
        sh = shd-1
        w_box = round(shc*(22/768))
        h_box = w_box
        fontsize = round(shc*(10/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1440:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(8/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1600:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1680:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1792:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1856:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 1920:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 2048:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 2560:
        shd = round(shc*(22/768))
        sh = shd-1
        w_box = round(shc*(21/768))
        h_box = w_box
        fontsize = round(shc*(7/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    elif swc == 3000:
        shd = round(shc*(20/768))
        sh = shd-1
        w_box = round(shc*(19/768))
        h_box = w_box
        fontsize = round(shc*(4/768))
        root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))

    
    
    

    
    root.overrideredirect(True)
    butm = tk.Frame(root,width=sw-10,height=sh,bg=A4)
    butm.pack(side='top',fill='x',padx=3,pady=2)
    f_top = tk.Frame(butm,bg=A4)
    f_top.pack(side='left')
    f_top_r = tk.Frame(butm,bg=A4)
    f_top_r.pack(side='right')
    #root.overrideredirect(True)

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
        name.config(bg=A5, fg='black')

    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(f_top, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imag = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/LOGOALL.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left',padx=3)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)


####################################################
    sear_bg = '#F0F0F0'
    search = tk.Frame(f_top,width=100,height=sh,bg=sear_bg)
    search.pack(side='left')
    ser_tip = tk.Label(search,text="???????????????????????????",bg=sear_bg,fg='#778899',font=(None,9))
    ser_tip.pack(padx=30)
###################################################

    
    # ??????????????????????????????

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
    righttip = tk.Label(f_top_r, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/TOPRIGHTTIP.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.pack(side='left', padx=0, pady=1)

    

    def enter_file(_):
        file.config(bg=nonea(), fg='white')

    def leave_file(_):
        file.config(bg=A5, fg='black')
    filename2 = fath_path + '/HandrilowOSLauncherCode/H_icon/POST.png'
    photofile = ImageTk.PhotoImage(file=filename2)
    filetext = '??????'
    font = Hfont.fontchange(filetext)
    file = tk.Label(f_top_r, text=filetext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    file.bind('<Enter>', enter_file)
    file.bind('<Leave>', leave_file)
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=5, pady=1)
        file.update()

    def enter_idle(_):
        idle.config(bg=nonea(), fg='white')

    def leave_idle(_):
        idle.config(bg=A5, fg='black')
    filename3 = fath_path + '/HandrilowOSLauncherCode/H_icon/IDLE.png'
    photoidle = ImageTk.PhotoImage(file=filename3)
    idletext = '??????'
    font = Hfont.fontchange(idletext)
    idle = tk.Label(f_top_r, text=idletext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    idle.bind('<Enter>', enter_idle)
    idle.bind('<Leave>', leave_idle)
    for i in range(5, 10)[::-1]:
        idle.pack(side='left', padx=5, pady=1)

        idle.update()

    def enter_fun(_):
        fun.config(bg=nonea(), fg='white')

    def leave_fun(_):
        fun.config(bg=A5, fg='black')
    filename4 = fath_path + '/HandrilowOSLauncherCode/H_icon/FUN.png'
    photofun = ImageTk.PhotoImage(file=filename4)
    funtext = '??????'
    font = Hfont.fontchange(funtext)
    fun = tk.Label(f_top_r, text=funtext, fg=A2, width=None, height=None,
                   bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    fun.bind('<Enter>', enter_fun)
    fun.bind('<Leave>', leave_fun)
    for i in range(5, 10)[::-1]:
        fun.pack(side='left', padx=5, pady=1)

        fun.update()

    def enter_win(_):
        win.config(bg=nonea(), fg='white')

    def leave_win(_):
        win.config(bg=A5, fg='black')
    filename6 = fath_path + '/HandrilowOSLauncherCode/H_icon/WINDOW.png'
    photowin = ImageTk.PhotoImage(file=filename6)
    wintext = '??????'
    font = Hfont.fontchange(wintext)
    win = tk.Label(f_top_r, text=wintext, fg=A2, width=None, height=None,
                   bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    win.bind('<Enter>', enter_win)
    win.bind('<Leave>', leave_win)
    for i in range(5, 10)[::-1]:
        win.pack(side='left', padx=5, pady=1)
        win.update()

    def enter_powe(_):
        powe.config(bg=nonea(), fg='white')

    def leave_powe(_):
        powe.config(bg=A5, fg='black')
    filename5 = fath_path + '/HandrilowOSLauncherCode/H_icon/SHELL.png'
    photopow = ImageTk.PhotoImage(file=filename5)
    powetext = '??????'
    font = Hfont.fontchange(powetext)
    powe = tk.Label(f_top_r, text=powetext, fg=A2, width=None, height=None,
                    bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')

    powe.bind('<Enter>', enter_powe)
    powe.bind('<Leave>', leave_powe)
    for i in range(5, 10)[::-1]:
        powe.pack(side='left', padx=5, pady=0)

        powe.update()

####################################################
    def launchapp(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/applaunched.pid"
        cpk.pathfilewrite(pids, "w")
        path = fath_path + '/HandrilowOSLauncherCode/sys/programe'
        a = powe1.cget("text")
        reappath = path + '/' + a + '/' + a + fath_path + 'exe'
        linker.launch(reappath, a)

    def enter_powe(_):
        powe1.config(bg=nonea(), fg='white')
        HMmenu.deskmenu()

    def leave_powe(_):
        powe1.config(bg=A5, fg='black')

    def getword():
        with open("tipname.psw", "r", encoding='utf-8') as f:
            data = f.read()
        date = data
        font = Hfont.fontchange(date)
        powe1.config(text=date)
        f_top.after(100, getword)
    powe1 = tk.Label(f_top_r, text='font=(?????? ,10)', fg=A2, width=None, height=None,
                     bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    powe1.pack(side='left', padx=5, pady=0)
    powe1.bind('<Button-1>', launchapp)
    powe1.bind('<Enter>', enter_powe)
    powe1.bind('<Leave>', leave_powe)
    getword()

###################################################
    ###############################################
    def getusename():
        with open("usename.psw", "r", encoding='utf-8') as f:
            data = f.read()
        date = data
        font = Hfont.fontchange(date)
        powe2.config(text=date)
        f_top.after(100, getusename)
    powe2 = tk.Label(f_top_r, text='font=(?????? ,10)', bg=A5, fg='#000000',
                     width=None, height=None, bd=0, font=(font, fontsize))
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
    win1112 = tk.Label(f_top_r, text="Taskmgr", width=w_box,
                       height=h_box, bg=A5, font=(font, fontsize))
    pil_image12 = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/SHELL.png')
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
        f_top.after(100, gettime)

    def enter_lb(_):
        # lb.config(bg=nonea(),fg='white')
        None

    def leave_lb(_):
        # lb.config(bg=A5,fg='black')
        None
    lb = tk.Label(f_top_r, text='', bg=A5, fg=A2, bd=0,
                  activeforeground='#F0F0F0', font=(font, fontsize))
    lb.bind('<Enter>', enter_lb)
    # lb.bind('<Button-1>',time)
    lb.bind('<Leave>', leave_lb)
    lb.pack(side='right', pady=0, padx=2)
    gettime()

    fileexists1 = os.path.exists(fath_path + "/HandrilowOSLauncherCode/set/guding.set")
    fileexists2 = os.path.exists(fath_path + "/HandrilowOSLauncherCode/set/yidong.set")
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
            percent = str(round(battery.percent))
            plug = str(battery.power_plugged)
            batext = 'Plug'
            font = Hfont.fontchange(batext)
            if plug == 'False':
                ba.configure(text=percent+'%', fg=A4, font=(font, 8))
            else:
                ba.configure(text=batext, fg=A4, font=(font, 8), pady=1)
            f_top.after(100, barttery)

        def batips(_):
            battery = psutil.sensors_battery()
            percent = str(round(battery.percent))
            cpk.message('????????????', percent+'%')
            
        ba = tk.Label(f_top_r, bg=A5, fg=A2, width=2*w_box, height=h_box,
                      activebackground=A2, bd=0, activeforeground='#F0F0F0', compound='center')
        pil_image_ba = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/BA.png')
        w, h = pil_image_ba.size
        pil_image_resized = resize(w, h, 2*w_box, h_box, pil_image_ba)
        tk_imageba = ImageTk.PhotoImage(pil_image_resized)
        ba.config(image=tk_imageba)
        ba.bind('<Button-1>',batips)
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
    win11 = tk.Label(f_top, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_win11 = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/MAINDOCK9.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='left', padx=2, pady=1)
    win11.bind('<Enter>', enter_win11)
    # win11.bind('<Button-1>',colorset)
    win11.bind('<Leave>', leave_win11)
    # ??????????????????

    def statue1():
        with open("toptip.message", "r", encoding='utf-8') as f:
            data1 = f.read()
        date = data1
        font = Hfont.fontchange(date)
        tiplabel.config(text=date)
        f_top.after(100, statue1)
    tiplabel = tk.Label(f_top, text='font=(?????? ,10)', fg=A2, width=None, height=None,
                        bd=0, bg=A5, font=(font, fontsize), activeforeground='#F0F0F0')
    tiplabel.pack(side='left', padx=5, pady=0)
    statue1()

    # ??????????????????
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
    showok = tk.Label(f_top_r, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imags = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/NET.png')
    w, h = pil_imags.size
    pil_image_resizes = resizs(w, h, w_box, h_box, pil_imags)
    tks_imag = ImageTk.PhotoImage(pil_image_resizes)
    showok.config(image=tks_imag)
    showok.pack(side='right', padx=0)
    showok.bind('<Enter>', enter_showok)
    showok.bind('<Leave>', leave_showok)
    showok.bind('<Button-1>', netlist)
    showok.bind('<Button-3>', discon)

    

    def handril_menu(_):
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/m1.pid"
        fp.mainsys(pids)
        HMmenu.handrilmenu()
    name.bind('<Button-1>', handril_menu)

    def order(_):
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
    #cpk.deskDockMode(None)
    #mouse.main(root)
    cpk.dicoset()
    pwt.main()
    # desklist.main()
    f_top.mainloop()
