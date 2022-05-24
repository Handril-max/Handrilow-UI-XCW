#Handrilsoft
#Handrilow HSF app
import win32gui
import random
import re
from tkinter import *
import tkinter as tk
from tkwebview2.tkwebview2 import WebView2
import os , sys , shutil , six , time
from shutil import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode.openHandrilow.sys_windoweng import *
from HandrilowOSLauncherCode.openHandrilow import sys_win_cartoon as swc

nowpath = os.getcwd()
def main(url):
    fd = win32gui.FindWindow("Shell_TrayWnd",None)
    win32gui.ShowWindow(fd,0)
    root=HandrilApp()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = random.randint(0,int(round(sw*(1/4))))
    y = 50
    wid  = int(round(sw*(19/20)))
    hig  = int(round(sh*(19/20)))
    root.config(cursor='circle')
    root.wm_attributes("-toolwindow", True)
    root.overrideredirect(True)
    m3 = tk.Frame(root)
    m3.pack()
    menu = tk.Canvas(m3,width=wid,height=30,bg='#F0F0F0')
    menu.pack(side='top')
    
    frame2=WebView2(m3,wid,hig)
    if re.match(r'^https?:/{2}\w.+$', url):
        frame2.load_url(url)
    else:
        frame2.load_html(url)
    frame2.pack(side='top',fill='both',expand=False)
    
    root.geometry('+%d+%d' % (x, y))
    #root.geometry('+50+50')
    root.mainloop()






