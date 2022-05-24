# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril picture select
# -*- coding:utf-8 -*-
import os
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import desktop
from HandrilowOSLauncherCode.openHandrilow import set_path
from HandrilowOSLauncherCode.openHandrilow.sys_windoweng import *
import shutil
import random

A4 = 'white'
sw = 600
w_box = 60
h_box = w_box
fath_path = set_path.pwd()

def main():
    #with open("pic_path.path", "r", encoding='utf-8') as f:
        #filepath = f.read()
    ambient_path = fath_path + '/HandrilowOSLauncherCode/H_Picture'
    root = HandrilAppTop()
    #root = tk.Tk()
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    sh = round((sw*shc)/swc)
    x = random.randint(5, round(swc*(1/4)))
    y = random.randint(50, round(shc*(1/4)))
    root.geometry('+%d+%d' % (x, y))
    root.wm_attributes("-topmost", True)
    root['background'] = 'black'
    root.overrideredirect(True)
    # 框架容器
    list_frame = tk.Frame(root,bg='white')
    list_frame.pack(side='left')
    d = tk.Frame(root, bg='black')
    d.pack(side='right')
    type_frame = tk.Frame(root)
    type_frame.pack(side='top', pady=20)

    def on_move(event):
        root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
        width, height = None, None
        offset_x = event.x_root - root_x
        offset_y = event.y_root - root_y
        if width and height:
            geo_str = "%sx%s+%s+%s" % (width, height,
                                       abs_x + offset_x, abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
            root.geometry(geo_str)

        def _on_tap(event):
            root_x, root_y = event.x_root, event.y_root
            abs_x, abs_y = winfo_x(), winfo_y()
    root.bind('<B1-Motion>', on_move)
    # 左边栏

    def selectbg():
        with open("selectbg.psw", "r") as fp:
            bg = fp.read()
        theLB.config(selectbackground=bg)
        theLB.after(1000, selectbg)

    def printlb():
        None

    def printtheLB(_):
        printlb()

    def show_image(path):
        global img
        image = Image.open(path)
        re_image = resize(image)
        img = ImageTk.PhotoImage(re_image)
        canvas.create_image(sw/2, sh/2, anchor='center', image=img)

    def showtheLB(_):
        a = theLB.get(theLB.curselection())
        my_path = ambient_path+'/'+a
        name3.config(text="当前" + a)
        # cpk.unpathfilewrite("picpath.path","w",my_path)
        show_image(my_path)

    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(list_frame, text="Taskmgr",
                    width=w_box, height=h_box, bg=A4)
    pil_imag = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/picsfl.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='bottom', padx=0, pady=0)

    # 选择列表区
    theLB = tk.Listbox(list_frame, bd=0, bg='white', exportselection=True, fg='black', highlightcolor=A4, width=50, height=17,
                       selectforeground=A4, font=('等线', 12), highlightbackground=A4,
                       selectmod="browse")
    theLB.pack(side='top', pady=5, padx=0)
    selectbg()
    name2 = tk.Label(list_frame, bg=A4, fg='black', font=('等线', 15), bd=0)
    name2.pack(side='bottom', pady=0, padx=0)
    name2.config(text="图片文件")
    name3 = tk.Label(list_frame, bg=A4, fg='gray',
                     font=('等线', 9, "bold"), bd=0)
    name3.pack(side='bottom')
    name3.config(text="Handrilsoft@Picture View 1.0")
    filenames = os.listdir(ambient_path)
    for item in filenames:
        theLB.insert("end", item)
    theLB.bind('<Button-1>', showtheLB)
    theLB.bind('<Enter>', showtheLB)

    # 展示区
    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength
        mul1 = sh/mlength1
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    canvas = tk.Canvas(d, height=sh, width=sw, bd=0, bg='black')
    canvas.config(highlightthickness=0)
    image = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
    re_image = resize(image)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    canvas.pack(padx=10)

    name3 = tk.Label(d, fg=A4, bg='black', font=('等线', 12), bd=0)
    name3.pack(side='top', pady=10, padx=10)
    name3.config(text="当前壁纸")
    cpk.deskDockMode(fath_path + '/HandrilowOSLauncherCode/H_icon/picsfl.png')
    root.mainloop()
# main()


def dialog():
    x = 5
    y = 40
    #with open("pic_path.path", "r", encoding='utf-8') as f:
        #filepath = f.read()
    ambient_path = fath_path + '/HandrilowOSLauncherCode/H_Picture/'
    root = tk.Toplevel()
    #root = tk.Tk()
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    x = random.randint(5, round(swc*(1/4)))
    y = random.randint(50, round(shc*(1/4)))
    sh = round((sw*shc)/swc)
    root.geometry('+%d+%d' % (x, y))
    root.wm_attributes("-topmost", True)
    root['background'] = 'black'
    root.overrideredirect(True)
    # 框架容器
    list_frame = tk.Frame(root,bg='white')
    list_frame.pack(side='left')
    d = tk.Frame(root, bg='black')
    d.pack(side='right')
    type_frame = tk.Frame(root)
    type_frame.pack(side='top', pady=20)

    def on_move(event):
        root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
        width, height = None, None
        offset_x = event.x_root - root_x
        offset_y = event.y_root - root_y
        if width and height:
            geo_str = "%sx%s+%s+%s" % (width, height,
                                       abs_x + offset_x, abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
            root.geometry(geo_str)

        def _on_tap(event):
            root_x, root_y = event.x_root, event.y_root
            abs_x, abs_y = winfo_x(), winfo_y()
    root.bind('<B1-Motion>', on_move)
    # 左边栏

    def selectbg():
        with open("selectbg.psw", "r") as fp:
            bg = fp.read()
        theLB.config(selectbackground=bg)
        theLB.after(1000, selectbg)

    def printlb():
        a = theLB.get(theLB.curselection())
        my_path = ambient_path+a
        cpk.unpathfilewrite("picpath.path", "w", my_path)
        root.destroy()
        cpk.message('背景', '变量已写入,点击按钮以切换')

    def printtheLB(_):
        printlb()

    def show_image(path):
        global img
        image = Image.open(path)
        re_image = resize(image)
        img = ImageTk.PhotoImage(re_image)
        canvas.create_image(sw/2, sh/2, anchor='center', image=img)
        canvas.create_rectangle(5, 5, 590, 15, fill='white')

    def showtheLB(_):
        a = theLB.get(theLB.curselection())
        name3.config(text='设置' + a + '为壁纸')
        my_path = ambient_path+a
        # cpk.unpathfilewrite("picpath.path","w",my_path)
        show_image(my_path)

     # 小白条
    filename = fath_path + '/HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2(_):
        root.destroy()
    bottomtype = tk.Label(list_frame, image=photo, bd=0, width=100, height=5)
    bottomtype.bind('<Leave>', jump2)
    bottomtype.pack(side='bottom', pady=2)

    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(list_frame, text="Taskmgr",
                    width=w_box, height=h_box, bg=A4)
    pil_imag = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/picsfl.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='bottom', padx=2, pady=0)

    # 选择列表区

    theLB = tk.Listbox(list_frame, bd=0, bg='#DCDCDC', exportselection=True, fg='black', highlightcolor=A4, width=50, height=25,
                       selectforeground=A4, font=('等线', 12), highlightbackground=A4,
                       selectmod="browse")
    theLB.pack(side='top', pady=0, padx=0)
    selectbg()
    
    name2 = tk.Label(list_frame, bg=A4, fg='black', font=('等线', 15), bd=0)
    name2.pack(side='bottom', pady=0, padx=0)
    name2.config(text="图片文件选择框")
    name3 = tk.Label(list_frame, bg=A4, fg='gray',
                     font=('等线', 9, "bold"), bd=0)
    name3.pack(side='bottom')
    name3.config(text="双击并回车\n选择你需要的文件")
    filenames = os.listdir(ambient_path)
    for item in filenames:
        theLB.insert("end", item)
    theLB.bind('<Button-1>', showtheLB)
    theLB.bind('<Return>', printtheLB)
    # 展示区

    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength
        mul1 = sh/mlength1
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    canvas = tk.Canvas(d, height=sh, width=sw, bd=0, bg='black')
    canvas.config(highlightthickness=0)
    image = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
    re_image = resize(image)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    canvas.create_rectangle(5, 5, 590, 20, fill='#F0F0F0')
    canvas.pack(side='top', padx=10)

    name3 = tk.Label(d, fg=A4, bg='black', font=('等线', 12), bd=0)
    name3.pack(side='top', pady=10, padx=10)
    name3.config(text="当前壁纸")

    root.mainloop()
# main()
