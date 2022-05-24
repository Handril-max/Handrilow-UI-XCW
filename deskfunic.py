#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#Handril app list
# -*- coding:utf-8 -*-
import os , sys , time , psutil , six , shutil
import string , glob , webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from HandrilowOSLauncherCode import windoweng
from shutil import *
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import colorlib as hcol
from HandrilowOSLauncherCode import Hmessage
from HandrilowOSLauncherCode import fileprocess as fp

def main():
            fp.main("./H_fileprocess/dico.pid")
            fileexists1 = os.path.exists("./set/dico.set")
            if fileexists1 == True:
                None
            else:
                b = open("./set/dico.set",'w')
                b.close
            A2= colorlib.black1()
            A3= colorlib.cola3()
            A4= '#888888'
            A5= '#DDDDDD'
            A7= A4
            A8= colorlib.cola8()
            rootA = DragWindow()
            rootA['background']= A4
            rootA.attributes('-transparentcolor',A4)
            swc = rootA.winfo_screenwidth()
            shc = rootA.winfo_screenheight()
            
            sw = swc-220
            sh = round(shc*(680/768))
            x=sw
            y=50
            rootA.geometry('%dx%d+%d+%d' %(sw,sh,x,y))
            rootA.overrideredirect(True)
            
            f1 = tk.Label(rootA,bg=A4)
            f1.place(x=0,y=0)
            
            filenameCLOSE = './H_icon/H_buttom\LAJITONG.ico'#用户
            photoCLOSE = ImageTk.PhotoImage(file=filenameCLOSE)
            
            def enter(_):
                def leave(_):
                    ww1.config(bg=A4)
                ww1.config(bg='#BBFFFF')
                ww1.bind('<Leave>',leave)
            ww1 = tk.Button(f1,bg=A4,fg= A2,image=photoCLOSE,bd=0,activebackground=A4,padx=3,pady=3)
            ww1.grid(row=0, column=0)
            ww1.bind('<Enter>',enter)
           

            filename2 = './H_icon/H_buttom\EDGE.ico'#文档
            photoedge = ImageTk.PhotoImage(file=filename2)
            def enter2(_):
                def leav2(_):
                    ww2.config(bg=A4)
                ww2.config(bg='#BBFFFF')
                ww2.bind('<Leave>',leav2)
            file = ".\H_document"
            def dsz():
                sz1 = os.path.getsize(file)
                dirsz = str(sz1)+'kb'
                ww2.config(text=dirsz)
                f1.after(100,dsz)
            ww2 = tk.Button(f1,bg=A4,fg= 'black',image=photoedge,bd=0,activebackground=A4,padx=3,pady=3,compound='center')
            ww2.grid(row=1, column=0)
            ww2.bind('<Enter>',enter2)
            dsz()


            filename3 = './H_icon/H_buttom\YINYUE.ico'#表
            phototime = ImageTk.PhotoImage(file=filename3)
            def enter3(_):
                def leav3(_):
                    ww3.config(bg=A4)
                ww3.config(bg='#BBFFFF')
                ww3.bind('<Leave>',leav3)
            ww3 = tk.Button(f1,bg=A4,fg= A2,image=phototime,bd=0,activebackground=A4,padx=3,pady=3)
            ww3.grid(row=2, column=0)
            ww3.bind('<Enter>',enter3)

            filename4 = './H_icon/H_buttom\QWE.ico'#图
            photo4 = ImageTk.PhotoImage(file=filename4)
            def enter4(_):
                def leav4(_):
                    ww4.config(bg=A4)
                ww4.config(bg='#BBFFFF')
                ww4.bind('<Leave>',leav4)
            file2 = ".\H_Picture"
            def psz():
                sz2 = os.path.getsize(file2)
                dirsz = str(sz2)+'kb'
                ww4.config(text=dirsz)
                f1.after(100,psz)
            ww4 = tk.Button(f1,bg=A4,fg= 'white',image=photo4,bd=0,activebackground=A4,padx=3,pady=3,compound='center')
            ww4.grid(row=0, column=1)
            ww4.bind('<Enter>',enter4)
            psz()

            filename5 = './H_icon/H_buttom\TIME.ico'#文档
            photo5 = ImageTk.PhotoImage(file=filename5)
            def rili():
                Hfunction.calender()
            def enter5(_):
                def leav5(_):
                    ww5.config(bg=A4)
                ww5.config(bg='#BBFFFF')
                ww5.bind('<Leave>',leav5)
            ww5 = tk.Button(f1,bg=A4,fg= A2,image=photo5,bd=0,activebackground=A4,padx=3,pady=3,command=rili)
            ww5.grid(row=1, column=1)
            ww5.bind('<Enter>',enter5)
            rootA.mainloop()
