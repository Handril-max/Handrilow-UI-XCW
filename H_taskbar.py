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
from .openHandrilow import set_path
from .openHandrilow import mouse
from .openHandrilow.net import set_connect
from .openHandrilow.sys_windoweng import *
from .H_welcome import index
from .import midwindow
from .openHandrilow import hf_textanaly as hfa
from .openHandrilow.sys_windoweng import *
fath_path = set_path.pwd()
t_x = 0
winnum = 0
# TOPMAINMENU
def main():
    A4 = 'white'
    root = tk.Toplevel()
    root.wm_attributes("-topmost", True)
    filejob = open(fath_path + '/HandrilowOSLauncherCode/set/unblur.set', 'w')
    filejob.close()

    def nonea():
        ebg = 'black'
        return ebg
    nonea()

    A4 = 'white'
    A2 = 'black'
    A5 = A4
    A7 = A4
    root['background'] = A4

    bloud = None
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    #root.attributes('-alpha',0.8)
    sw = swc
    shd = round(45)
    w_box = round(30)
    fontsize = round(1)
    h_box = w_box
    sh = shd
    t_x = 0
    t_y = shc-shd
    root.geometry('%dx%d+%d+%d' % (sw, sh, t_x, t_y))
    root.overrideredirect(True)
    root.config(cursor='circle')
    
    butm = tk.Frame(root,bg=A4)
    butm.pack()
    f_mid = tk.Frame(butm, bg=A4)
    f_mid.pack(padx=5,pady=5)
    #HOME
    def enter_name(_):
        name.config(width=w_box-5, height=h_box-5)
    def leave_name(_):
        name.config(width=w_box, height=h_box)
    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(f_mid, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_imag = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/H_taskbar/HOME.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left', padx=5)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)
    #BACK
    def resize(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_win11.resize((width, height), Image.ANTIALIAS)
    def enter_win11(_):
        win11.config(width=w_box-5, height=h_box-5)
    def leave_win11(_):
        win11.config(width=w_box, height=h_box)
    win11 = tk.Label(f_mid, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_win11 = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/H_taskbar/BACK.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='left', padx=6, pady=1)
    win11.bind('<Enter>', enter_win11)
    # win11.bind('<Button-1>',colorset)
    win11.bind('<Leave>', leave_win11)
    #SEARCH
    def enter_righttip(_):
        righttip.config(width=w_box-5, height=h_box-5)
    def leave_righttip(_):
        righttip.config(width=w_box, height=h_box)
    def resize(w, h, w_box, h_box, pil_image_righttip):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(f_mid, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/H_taskbar/SEARCH.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.pack(side='left', padx=6, pady=1)
    righttip.bind('<Enter>', enter_righttip)
    righttip.bind('<Leave>', leave_righttip)
    #TALK
    #TOSELF
    root.mainloop()
