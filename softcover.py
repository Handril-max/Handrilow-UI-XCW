# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# main
# Handril PC screen
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import six
import shutil
import string
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from shutil import *
from HandrilowOSLauncherCode import windoweng as weg
from HandrilowOSLauncherCode import scound
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import cpupack as cpk


def main_a(pngpath):
    root = tk.Toplevel()
    root.wm_attributes("-topmost", True)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    if 800 <= sw <= 1366:
        shd = round(sh*(27/768))
    elif 1366 < sw <= 1920:
        shd = round(sh*(22/768))
    swcstr = str(root.winfo_screenwidth())
    #######################
    swc = 120
    if swcstr > '1600':
        shc = 290
    else:
        shc = 240
    scw = 774
    sch = 549
    x = (sw-scw)/2
    y = (sh-sch)/2
    A4 = 'white'
    root.geometry('%dx%d+%d+%d' % (scw, sch, x, y))
    root['background'] = A4
    cpk.overide(root)

    # 菜单项对应图标
    A5 = A4
    w_box = scw
    h_box = sch

    def resize12(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image12.resize((width, height), Image.ANTIALIAS)
    win1112 = tk.Label(root, text="Taskmgr", width=w_box, height=h_box, bg=A5)
    #pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/scbg/about.png')
    pil_image12 = Image.open(pngpath)
    w, h = pil_image12.size
    pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)
    tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
    win1112.config(image=tk_image12)
    win1112.pack(padx=5, pady=1)
    for i in range(0, 100, 10)[::1]:  # 淡入
        root.attributes('-alpha', i/100)
        root.update()
        time.sleep(0.013)

    def sc_exite():
        for i in range(0, 100, 5)[::-1]:  # 淡出
            root.attributes('-alpha', i/100)
            root.update()
            time.sleep(0.013)
        root.destroy()
        cpk.loginto()
    root.after(2700, sc_exite)
    root.mainloop()


def about():
    path = './HandrilowOSLauncherCode/H_icon/scbg/about.png'
    cpk.unpathfilewrite("toptipMessage.message", "w", "关于本机")
    main_a(path)
