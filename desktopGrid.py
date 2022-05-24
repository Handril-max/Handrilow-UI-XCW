import os
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
from shutil import *
from HandrilowOSLauncherCode import colorlib as hcc
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol
from HandrilowOSLauncherCode import picfiledialog as pflog

#初始位置
wx=35
wy=40

def guding_main(namevlew):
    global wx,wy
    fatherpath = 'D:\Handrilow\HandrilowOSLauncherCode\H_icon\H_file_ico/'
    filepath = fatherpath + namevlew + '.png'
    #filepath=filedialog.askopenfilename()
    #print(filepath)
    rootA = tk.Toplevel()
    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        root.after(1000, nonea)
    nonea()
    A4= nonea()
    rootA['background']= A4
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    rootA.wm_attributes("-topmost", True)
    cpk.overide(rootA)
    swc = sw
    shc = sh
    
    if swc <= 1366:
        shd = round(shc*(27/768))
        w_box = round(swc*(54/1366))
        fontsize = round(shc*(10/768))
        x = wx
        y = wy + shd
    elif swc == 1440:
        shd = round(shc*(22/768))
        w_box = round(swc*(58/1366))
        fontsize = round(shc*(8/768))
        x = wx
        y = wy + shd
    elif swc == 1600:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1680:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1792:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1856:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1920:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2048:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2560:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd - 5
    elif swc == 3000:
        shd = round(shc*(20/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(4/768))
        x = wx 
        y = wy + shd + 10
    h_box = w_box
    wx += w_box +10
    print(wx)
    if wx+w_box+10 >= sw:
        wy += w_box + 20 +10
        wx = 35
    if wy+w_box + 20 +10 >= sh:
        rootA.destroy()
        cpk.message('提示','桌面空间已满')
    else:
        print('not fall')

    def enter_file(_):
        name.config(bg=nonea())
    def leave_file(_):
        name.config(bg='#AAAAAA')
    def resiz(w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(rootA,width=w_box, height=h_box,bg='#AAAAAA')
    #pil_imag = Image.open('./HandrilowOSLauncherCode/H_icon/LOGO.png')
    pil_imag = Image.open(filepath) 
    w, h = pil_imag.size  
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)  
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag) 
    name.pack(side='top')
    name.bind('<Enter>', enter_file)
    name.bind('<Leave>', leave_file)

    def opener(_):
        None
    name.bind('<Button-1>',opener)
    menubar = tk.Menu(rootA)
    menu = tk.Menu(rootA, tearoff=0)
        
    menu.add_command(label='打开')
    menu.add_command(label='清空回收站')
    menu.add_command(label='属性')

    def popumenua(event):
        fileexists = os.path.exists(
            "./HandrilowOSLauncherCode/set/lockscreen.set")
        if fileexists == True:
            None
        else:
            menu.post(event.x_root, event.y_root)
    name.bind('<Button-3>', popumenua)

    filepath, tempfilename = os.path.split(filepath)
    filename, extension = os.path.splitext(tempfilename)
    name_nn = tk.Label(rootA,width=w_box,bg='#AAAAAA',fg='white')
    name_nn.config(text=filename)
    name_nn.pack(side='bottom')
    
    cpk.fathersize(rootA,w_box,h_box+20,x,y)
    #退出动画
    def exite():
        global wx
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        rootA.destroy()
        wx -= w_box +10
    #检测时间
    def exitekey(_):
        thdpol.dissetp.thd(exite())
    #rootA.bind('<Button-3>', exitekey)
    #rootA.after(5000, exite)
    rootA.mainloop()


def main():
    global wx,wy
    
    filepath=filedialog.askopenfilename()

    #cv.imshow('output', output)
    #cv.imshow('input', img)
    #print(filepath)
    rootA = tk.Toplevel()
    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        root.after(1000, nonea)
    nonea()
    A4= nonea()
    rootA['background']= A4
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    rootA.wm_attributes("-topmost", True)
    cpk.overide(rootA)
    swc = sw
    shc = sh
    
    if swc <= 1366:
        shd = round(shc*(27/768))
        w_box = round(swc*(54/1366))
        fontsize = round(shc*(10/768))
        x = wx
        y = wy + shd
    elif swc == 1440:
        shd = round(shc*(22/768))
        w_box = round(swc*(58/1366))
        fontsize = round(shc*(8/768))
        x = wx
        y = wy + shd
    elif swc == 1600:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1680:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1792:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1856:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 1920:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2048:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd
    elif swc == 2560:
        shd = round(shc*(22/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(7/768))
        x = wx
        y = wy + shd - 5
    elif swc == 3000:
        shd = round(shc*(20/768))
        w_box = round(swc*(300/1366))
        fontsize = round(shc*(4/768))
        x = wx 
        y = wy + shd + 10
    h_box = w_box
    wx += w_box +10
    print(wx)
    if wx+w_box+10 >= sw:
        wy += w_box + 20 +10
        wx = 35
    if wy+w_box + 20 +10 >= sh:
        rootA.destroy()
        cpk.message('提示','桌面空间已满')
    else:
        print('not fall')

    def enter_file(_):
        name.config(bg=nonea())
    def leave_file(_):
        name.config(bg='#AAAAAA')
    def resiz(w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(rootA,width=w_box, height=h_box,bg='#AAAAAA')
    #pil_imag = Image.open('./HandrilowOSLauncherCode/H_icon/LOGO.png')
    pil_imag = Image.open(filepath)
    pil_imag =pil_imag.convert('RGBA')
    w, h = pil_imag.size  
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)  
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag) 
    name.pack(side='top')
    name.bind('<Enter>', enter_file)
    name.bind('<Leave>', leave_file)

    filepath, tempfilename = os.path.split(filepath)
    filename, extension = os.path.splitext(tempfilename)
    name_nn = tk.Label(rootA,width=w_box,bg='#AAAAAA',fg='white')
    name_nn.config(text=filename)
    name_nn.pack(side='bottom')
    
    cpk.fathersize(rootA,w_box,h_box+20,x,y)
    #退出动画
    def exite():
        global wx
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        rootA.destroy()
        wx -= w_box +10
    #检测时间
    def exitekey(_):
        thdpol.dissetp.thd(exite())
    rootA.bind('<Button-3>', exitekey)
    #rootA.after(5000, exite)
    rootA.mainloop()



