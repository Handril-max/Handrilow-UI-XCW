#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#bottomtype
# -*- coding:utf-8 -*-
import os , sys , six , shutil , psutil,time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk

def main():
    A4= '#F0F0F0'
    rootA = tk.Toplevel()
    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        root.after(1000, nonea)
    nonea()
    rootA['background']= A4
    sw = rootA.winfo_screenwidth()
    sh = rootA.winfo_screenheight()
    x=0
    y=700
    rootA.wm_attributes("-topmost", True)
    cpk.fathersize(rootA,sw,sh,0,0)
    cpk.overide(rootA)
    
    def exite():
        for i in range(-sh,0,30)[::-1]:
            rootA.geometry('%dx%d+%d+%d' %(sw,sh,x,i))
            rootA.update()
        rootA.destroy()
    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength  
        mul1 = sh/mlength1
        w1 = int(w * mul) 
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    canvas=tk.Canvas(rootA,height=sh,width=sw,bd=0)
    canvas.config(highlightthickness=0)
    image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/BG-1.png')
    re_image = resize(image)
    im=re_image.filter(ImageFilter.GaussianBlur(radius=0))
    img = ImageTk.PhotoImage(im)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    
    canvas.create_text(sw/2, sh*(24/25), text='含昭 | Photoed by Handril Art',font=("等线",14,"bold"),fill='white')
    canvas.place(x=0,y=0)

    def mydock(_):
        fileexists = os.path.exists("./set/lockscreen.set")
        if fileexists == True:
            os.remove('./set/lockscreen.set')
            exite()
        else:
            None


    w_box = 100
    h_box = 100
    def resiz(w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    def barttery():
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        plug = str(battery.power_plugged)
        if battery == None:
            name.configure(bg='green')
        elif plug == 'False':
            name.configure(bg='black')
        else:
            name.configure(bg=nonea())
        rootA.after(100,barttery)
    name = tk.Label(rootA,text="Taskmgr",width=w_box, height=h_box)
    pil_imag = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/syslogo.png') 
    w, h = pil_imag.size  
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)  
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag) 
    name.place(x=sw*0.1,y=0)
    barttery()
    
    def mydock(_):
        exite()
    for i in range(0,sh,15)[::-1]:
        rootA.geometry('%dx%d+%d+%d' %(sw,sh,x,i))
        rootA.update()

    rootA.bind('<B1-Motion>',mydock)
    rootA.bind('<MouseWheel>',mydock)
    rootA.bind('<Button-1>',mydock)
    rootA.mainloop()
#main()
