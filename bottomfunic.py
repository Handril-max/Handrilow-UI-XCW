# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril bottomfunic
# -*- coding:utf-8 -*-
import tkinter as tk
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
from PIL import ImageTk, Image
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from shutil import *
from HandrilowOSLauncherCode import windoweng
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import colorlib as hcol
from HandrilowOSLauncherCode import cpupack as cpk
import os
from HandrilowOSLauncherCode import linker
#import waiter


def dock():
    master = tk.Toplevel()
    A4 = '#F0F0F0'
    master['background'] = A4
    master.attributes('-transparentcolor', A4)
    master.attributes('-alpha', 0.8)
    sw = master.winfo_screenwidth()
    sh = master.winfo_screenheight()
    x = 0
    y = 0

    def exite(_):
        theLB.destroy()
    f1 = tk.Frame(master, bg=A4)
    f1.pack(side='top')
    f2 = tk.Frame(master, bg=A4)
    f2.pack(side='bottom')
    master.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    master.overrideredirect(True)
    master.wm_attributes("-topmost", True)
    path = './sys/programe'
    filenames = os.listdir(path)
    # print(filenames)
    linker.applist(master, filenames, path, A4, f1)
    master.after(10000, master.destroy)
    # waiter.main(A4,f1)
    # master.mainloop()
