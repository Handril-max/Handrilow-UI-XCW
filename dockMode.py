import os
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
from HandrilowOSLauncherCode import colorlib as hcc
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol

#初始位置
wx=5
wy=10

def main(filepath):
    global wx
    #filepath=filedialog.askopenfilename()
    rootA = tk.Toplevel()
    A4 = '#F0F0F0'
    rootA['background']= A4
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    swc = sw
    shc = sh
    
    if swc <= 1366:
        shd = round(shc*(27/768))
        w_box = round(shc*(22/768))
        fontsize = round(shc*(10/768))
        x = wx
        y = wy + shd
    elif swc == 1440:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(8/768))
        x = wx
        y = wy + shd
    elif swc == 1600:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1680:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1792:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1856:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1920:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2048:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2560:
        shd = round(shc*(22/768))
        w_box = round(shc*(21/768))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd - 5
    elif swc == 3000:
        shd = round(shc*(20/768))
        w_box = round(shc*(19/768))
        fontsize = round(shc*(4/768))
        x = wx 
        y = wy + shd
    wx += w_box +1
    h_box = w_box
    sh = shd-1
    rootA.wm_attributes("-topmost", True)
    cpk.overide(rootA)
    
    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)

    name = tk.Label(rootA,width=w_box, height=h_box)
    if filepath==None:
        pil_imag = Image.open('./HandrilowOSLauncherCode/H_icon/LOGO.png')
    else:
        pil_imag = Image.open(filepath) 
    w, h = pil_imag.size  
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)  
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    def name_bg():
        name.config(bg=A4)
        name.after(1005,name_bg)
    
    name.pack(side='left')
    
    
    cpk.fathersize(rootA,w_box,h_box,x,y)
    name_bg()
    
    #退出动画
    def exite():
        global wx
        #cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        rootA.destroy()
        wx -= w_box +1
    #检测时间
    def exitekey(_):
        thdpol.dissetp.thd(exite())
    rootA.bind('<Button-3>', exitekey)
    #rootA.after(5000, exite)
    rootA.mainloop()



