import os
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import windoweng
from HandrilowOSLauncherCode import colorlib as hcc
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol


def qrandom(title, randommessage):
    A1bg = hcc.black2()
    A3fg = hcc.cola3()
    root = tk.Toplevel()
    #root.wm_attributes("-topmost", True)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    mwh = 120/286
    if 2000 <= sw <= 3000:
        swc = 500
        shc = round(swc*mwh)
        #shc = 200
        x = (sw-swc)/2

    if 1366 <= sw <= 1920:
        swc = 286
        shc = round(swc*mwh)
        x = (sw-swc)/2
    if 800 <= sw <= 1366:
        swc = 286
        shc = round(swc*mwh)
        x = (sw-swc)/2
    y = sw*0+30
    root['background'] = A1bg
    root.overrideredirect(True)
    root.resizable(0, 0)
    for i in range(-100, 60, 45):  # 入
        root.geometry('%dx%d+%d+%d' % (swc, shc, x, i))
        root.update()
        time.sleep(0.01)

    title = tk.Label(root, text=title, bg=A1bg, fg=A3fg, font=('黑体', 15))
    title.pack(side='top', pady=10)

    mes = tk.Label(root, text=randommessage, bg=A1bg, fg=A3fg, font=('黑体', 16))
    mes.pack(side='top', pady=5)
    # cpk.atp(root)

    def exite():
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        for i in range(-100, 60, 45)[::-1]:  # 入
            root.geometry('%dx%d+%d+%d' % (swc, shc, x, i))
            root.update()
            time.sleep(0.01)
        root.destroy()

    def exitekey(_):
        exite()
    root.bind('<Alt-b>', exitekey)
    root.after(5000, exite)
    root.mainloop()


###############################################################################
wx=1000
wy=40
def random(title, randommessage):
    global wy
    x = wx
    y = wy
    wy += 50 +5
    rootA = tk.Tk()
    A4= '#F0F0F0'
    rootA['background']= 'black'
    #rootA.attributes('-transparentcolor',A4)
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    #rootA.wm_attributes("-topmost", True)
    cpk.fathersize(rootA,sw-1005,50,0,0)
    cpk.overide(rootA)
    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength  
        mul1 = sh/mlength1
        w1 = int(w * mul) 
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    canvas=tk.Canvas(rootA,height=50,width=sw-1005,bd=0,bg='#272727')
    canvas.config(highlightthickness=0)
    text_post_x = 150
    text_post_y = 25
    canvas.create_text(text_post_x, text_post_y, text=title + ':' + randommessage,font=("等线",15),fill='white')
    canvas.place(x=0,y=0)
    #进入动画
    for i in range(x,sw,15)[::-1]:
        rootA.geometry(f'+{i}+{y}')
        rootA.update()
    #退出动画
    def exite():
        global wy
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        for i in range(x,sw,15)[::1]:
            rootA.geometry(f'+{i}+{y}')
            rootA.update()
        rootA.destroy()
        wy -= 50 +5
    #检测时间
    def exitekey(_):
        thdpol.dissetp.thd(exite())
    rootA.bind('<Alt-b>', exitekey)
    rootA.after(5000, exite)
    rootA.mainloop()

#####################################################################################
def randomroot(title, randommessage):
    A1bg = hcc.black2()
    A3fg = hcc.cola3()
    root = tk.Toplevel()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    mwh = 120/286
    if 2000 <= sw <= 3000:
        swc = 500
        shc = round(swc*mwh)
        #shc = 200
        x = (sw-swc)/2

    if 1366 <= sw <= 1920:
        swc = 286
        shc = round(swc*mwh)
        x = (sw-swc)/2
    if 800 <= sw <= 1366:
        swc = 286
        shc = round(swc*mwh)
        x = (sw-swc)/2
    y = sw*0+30
    root['background'] = A1bg
    root.overrideredirect(True)
    root.resizable(0, 0)
    for i in range(-100, 60, 45):  # 入
        root.geometry('%dx%d+%d+%d' % (swc, shc, x, i))
        root.update()
        time.sleep(0.01)

    title = tk.Label(root, text=title, bg=A1bg, fg=A3fg, font=('黑体', 15))
    title.pack(side='top', pady=10)

    mes = tk.Label(root, text=randommessage, bg=A1bg, fg=A3fg, font=('黑体', 16))
    mes.pack(side='top', pady=5)

    def exite():
        cpk.unpathfilewrite("toptip.message", "w", " ")
        for i in range(-100, 60, 45)[::-1]:  # 入
            root.geometry('%dx%d+%d+%d' % (swc, shc, x, i))
            root.update()
            time.sleep(0.01)
        root.destroy()

    def exitekey(_):
        exite()
    root.bind('<Alt-b>', exitekey)
    root.after(5000, exite)

    root.mainloop()


def other(xpost, hbg, hfg, title, randommessage):
    xpost=None
    hbg=None
    hfg=None
    title=None
    randommessage=None
