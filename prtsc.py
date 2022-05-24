#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#PrtSc
# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import *
from PIL import *
import ctypes, sys, time
from HandrilowOSLauncherCode import cpupack as cpk

def prtsc():
    filename ='sysprtsc.png'
    im =ImageGrab.grab()
    im.save(filename)
    root = tk.Toplevel()
    cpk.fathersize(root,480,300,20,40)
    x=20
    y = 40
    cpk.overide(root)
    root.wm_attributes("-topmost", True) 
    sw=480
    sh=300
    def exite():
            root.destroy()
    def resize(image):
            w, h = image.size
            mlength = max(w, h)
            mlength1 = min(w, h)
            mul = sw/mlength  
            mul1 = sh/mlength1
            w1 = int(w * mul) 
            h1 = int(h * mul1)
            return image.resize((w1, h1))
    canvas=tk.Canvas(root,height=sh,width=sw,bd=0)
    canvas.config(highlightthickness=0)
    image = Image.open(filename)
    re_image = resize(image)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    canvas.after(5400,exite)
    canvas.place(x=0,y=0)
    cpk.message('提示','截图已保存')
    root.mainloop()

def prtsclock():
    time.sleep(0)
    filename ='sysprtsc.png'
    im =ImageGrab.grab()
    im.save(filename)
    
def main():
    None
def mainlock():
    None
