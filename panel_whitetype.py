# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# bottomtype
# -*- coding:utf-3 -*-
import os
import sys
import six
import shutil
from HandrilowOSLauncherCode import linker
import tkinter as tk
from tkinter import *
from PIL import *
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import windoweng


def main():
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    A4 = 'white'
    A2 = 'black'
    A5 = A4
    A7 = A4
    root['background'] = A4
    sw = swc/3
    sh = 6
    x = sw
    y = shc-10
    root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    root.overrideredirect(True)
    root.mainloop()


