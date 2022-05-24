# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# midwindow
# -*- coding:utf-8 -*-
import os
import sys
import six
import shutil
import pygame
import psutil , time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image , ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk
import tkinter.ttk as ttk
from HandrilowOSLauncherCode import scound
from HandrilowOSLauncherCode.openHandrilow import set_path

fath_path = set_path.pwd()
pygame.mixer.init()

def main():
    cpk.unpathfilewrite("toptip.message", "w", "控制中心")
    A4 = '#272727'
    rootA = tk.Toplevel()
    rootA['background'] = A4
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    rootA.overrideredirect(True)
    rootA.config(cursor='circle')
    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength
        mul1 = sh/mlength1
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    canvas = tk.Canvas(rootA, height=sh, width=sw, bd=0)
    canvas.config(highlightthickness=0)
    cpk.prtscother()
    image = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
    re_image = resize(image)
    im = re_image.filter(ImageFilter.GaussianBlur(radius=80))
    img = ImageTk.PhotoImage(im)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    canvas.create_text(sw/12, 65, text='控制中心',font=("等线",20,"bold"),fill='white')
    canvas.place(x=0, y=0)

    def jump2():
        bottomtype.destroy()
        for h in range(1,100)[::-1]:
            i = h*(100/h)
            rootA.wm_attributes("-alpha", i/70)
            rootA.geometry('%dx%d+%d+%d'%(sw,sh,0,0))
            rootA.update()
        rootA.destroy()
        cpk.unpathfilewrite("toptip.message", "w", "")
        cpk.unpathfilewrite("iotest.psw", "w", "0")
    def jump1(_):
        #cpk.mwinto(bottomtype, 'bottom', 0, 5, 12)
        #bottomtype.destroy()
        jump2()
    
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/TYPE.png'
    photo = ImageTk.PhotoImage(file=filename)
    bottomtype = tk.Label(rootA, image=photo, bd=0,
                          width=sw/3, height=6)
    bottomtype.bind('<Leave>',jump1)
    bottomtype.pack(side='bottom',pady=5)

    rootA.bind_all('<Tab>',jump1)
    
    f1 = tk.Frame(rootA,width=110,height=110,bg='#F0F0F0')
    f1.place(x=sw/24,y=100)
    w_box = 25
    h_box = w_box
    with open("suond.message", "r", encoding='utf-8') as f:
        title = f.read()
    micname = tk.Label(f1,text=':-) '+str(title),bg='#F0F0F0',fg='black',anchor='e',wraplength=90,font=('等线' ,10))
    micname.place(x=10,y=10)
    def enter_name(_):
        name.config(bg='#D3D3D3', fg='white')
    def leave_name(_):
        name.config(bg="#F0F0F0", fg='black')
    name = tk.Label(f1, text="Taskmgr", width=25, height=25, bg="#F0F0F0")
    pil_imag = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/MUSIC.png')
    name.config(image=pil_imag)
    name.place(x=(110-w_box)/2,y=110-w_box-10)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)
    def to_oper(_):
        None
    name.bind('<Button-1>', to_oper)
    
    
    f2 = tk.Frame(rootA,width=110,height=50,bg='#F0F0F0')
    f2.place(x=(sw/24)+120,y=100)
    def enter_wifi(_):
        wifi.config(bg='#D3D3D3', fg='white')
    def leave_wifi(_):
        wifi.config(bg="#F0F0F0", fg='black')
    wifi = tk.Label(f2, text="Taskmgr", width=35, height=35, bg="#F0F0F0")
    pil_imag_wifi = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/WIFI_CTL.png')
    wifi.config(image=pil_imag_wifi)
    wifi.place(x=10,y=5)
    wifi.bind('<Enter>', enter_wifi)
    wifi.bind('<Leave>', leave_wifi)
    def to_oper_wifi(_):
        None
    wifi.bind('<Button-1>', to_oper_wifi)
    wifiname = tk.Label(f2,text='WIFI',bg='#F0F0F0',fg='black',anchor='e',wraplength=90,font=('等线' ,12))
    wifiname.place(x=50,y=15)

    f3 = tk.Frame(rootA,width=110,height=50,bg='#F0F0F0')
    f3.place(x=(sw/24)+120,y=160)
    def enter_bluetooth(_):
        bluetooth.config(bg='#D3D3D3', fg='white')
    def leave_bluetooth(_):
        bluetooth.config(bg="#F0F0F0", fg='black')
    bluetooth = tk.Label(f3, text="Taskmgr", width=35, height=35, bg="#F0F0F0")
    pil_imag_bluetooth = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/bluetooth_CTL.png')
    bluetooth.config(image=pil_imag_bluetooth)
    bluetooth.place(x=10,y=5)
    bluetooth.bind('<Enter>', enter_bluetooth)
    bluetooth.bind('<Leave>', leave_bluetooth)
    def to_oper_bluetooth(_):
        None
    bluetooth.bind('<Button-1>', to_oper_bluetooth)
    bluetoothname = tk.Label(f3,text='蓝牙',bg='#F0F0F0',fg='black',anchor='e',wraplength=90,font=('等线' ,12))
    bluetoothname.place(x=50,y=15)

    w_box_re = 80
    h_box_re = 80
    f4 = tk.Frame(rootA,width=230,height=100,bg='#F0F0F0')
    f4.place(x=(sw/24),y=220)
    
    def resize(w, h, w_box_re, h_box_re, pil_image_righttip):
        f1 = 1.0*w_box_re/w
        f2 = 1.0*h_box_re/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(f4, text="Taskmgr", width=w_box_re+2, height=h_box_re+2, bg='#F0F0F0')
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/info.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box_re, h_box_re, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.place(x=10,y=10)
    def to_oper_USER(_):
        None
    righttip.bind('<Button-1>', to_oper_USER)
    with open("usename.psw", "r") as f:
        user = f.read()
    USERname = tk.Label(f4,text=user,bg='#F0F0F0',fg='black',anchor='e',wraplength=90,font=('等线' ,16))
    USERname.place(x=100,y=30)
    tip = tk.Label(f4,text='正此为始，天下能之',bg='#F0F0F0',fg='black',anchor='e')
    tip.place(x=100,y=55)
    
    #控制中心设置列表
    f5 = tk.Frame(rootA,width=230,height=300,bg='#F0F0F0')
    f5.place(x=(sw/24),y=330)
    setlist = tk.Text(f5,bd=0)
    setlist.place(x=1,y=1)
    

    with open("iotest.psw", "r") as f:
        data = f.read()
    print('data'+data)
    if data == "1":
        print('1')
        None
    else:
        print('0')
        for h in range(1,100)[::1]:
            i = h*(100/h)
            rootA.wm_attributes("-alpha", i/70)
            rootA.geometry('%dx%d+%d+%d'%(sw,sh,0,0))
            rootA.update()
        cpk.unpathfilewrite("iotest.psw", "w", "1")
            
    rootA.mainloop()
