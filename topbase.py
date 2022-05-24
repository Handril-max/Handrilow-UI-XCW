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
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
#import tkinter.font as font
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from HandrilowOSLauncherCode import windoweng
from shutil import *
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import colorlib as hcol
from HandrilowOSLauncherCode import cpupack as cpk

# TOPMAINMENU


def topmenu():
    A2 = colorlib.black1()
    A3 = colorlib.cola3()
    A4 = colorlib.cola4()
    A5 = 'grey'
    A7 = A4
    A8 = colorlib.cola8()
    rootA = tk.Toplevel()
    rootA.wm_attributes("-topmost", True)
    swc = rootA.winfo_screenwidth()
    shc = rootA.winfo_screenheight()
    rootA.attributes('-transparentcolor', 'grey')
    sw = swc/3
    if 800 <= swc <= 1366:
        shd = round(shc*(27/768))
    elif 1366 < swc <= 1920:
        shd = round(shc*(22/768))
    elif 2000 < swc <= 3000:
        shd = round(shc*(21/768))

    sh = shd*3
    x = (swc-sw)/2
    y = shc-sh
    cpk.fathersize(rootA, sw, sh, x, y)
    cpk.overide(rootA)

    cpk.graduallyinsc(rootA, 0, 100, 10)
    time.sleep(3)
    for i in range(0, 100, 5)[::-1]:  # 淡出
        rootA.attributes('-alpha', i/100)
        rootA.update()
        time.sleep(0.013)
    rootA.mainloop()
