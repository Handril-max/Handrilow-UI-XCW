#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#Handril app list
# -*- coding:utf-8 -*-
import os , sys , time , psutil , six , shutil
import string ,  glob , webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from HandrilowOSLauncherCode import windoweng 
from shutil import *
from . import colorlib , linker , tool_app , auto_text
from . import colorlib as hcol
from . import cpupack as cpk
from . import fileprocess as fp
from . import softcover as sc
from . import picfiledialog as pflog
from . import environmentPathChange as epc
from .openHandrilow import set_path
from .openHandrilow import sys_name
from .disk import consult as allfile
from .disk import picture
from .disk import document
from .disk import video
from . import scound
from . import Horder
import multiprocessing
from .openHandrilow.sys_windoweng import *

fath_path = set_path.pwd()

A4='white'

#################################################################
def windowmenu():
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/windowmenu.pid"
        root = tk.Toplevel()
        root.wm_attributes("-topmost", True)
        root.attributes('-alpha',0.9)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        root.config(cursor='circle')
        if 800 <= sw <= 1366:
                shd = round(25)
        elif 1366 < sw <= 1920:
                shd = round(25)
        #######################
        swc=120
        shc=240
        with open("postx.psw", "r", encoding='utf-8') as f:
            data = f.read()
        x = int(data)-15
        y=31
        root.geometry('+%d+%d'%(x,y))
        root['background']= A4
        root.overrideredirect(True)
        #窗口移动函数
        def on_move(event):
                root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
                width, height = None, None
                offset_x = event.x_root - root_x
                offset_y = event.y_root - root_y
                if width and height:
                    geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
                else:
                    geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
                    root.geometry(geo_str)
                def _on_tap(event):
                    root_x, root_y = event.x_root, event.y_root
                    abs_x, abs_y = winfo_x(), winfo_y()
        root.bind('<B1-Motion>', on_move)
        #root = handriltopmenuWindow()
        
        def exite():
                fp.exitesys(root,pids)
                root.destroy()

        #小白条
        filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
        photo = ImageTk.PhotoImage(file=filename)
        def jump2(_):
                cpk.mwoutto(bottomtype,'bottom',0,0,3)
                exite()
        def mydock(_):
                exite()
        bottomtype = tk.Label(root,image=photo,bd=0,width=100,height=5)
        bottomtype.bind('<Leave>',jump2)
        cpk.mwinto(bottomtype,'bottom',0,0,3)
                
#任务
        def go(*args):
                pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/applaunched.pid"
                cpk.pathfilewrite(pids,"w")
                path = './HandrilowOSLauncherCode/sys/programe'
                a = comboxlist.get()
                icopath = path + '/' + a + '/' + a + '.ico'
                with open("icopath.psw","w") as fpico:
                    fpico.write(icopath)
                with open("icopath.psw","r") as f:
                    tipicon = f.read()
                
                #print(a)
                with open("tipname.psw","w") as f:
                    f.write(a)
                path = './HandrilowOSLauncherCode/sys/programe'
                reappath = path + '/' + a + '/' + a + '.exe'
                root.destroy()
                linker.launch(reappath,a)
                
        path = './HandrilowOSLauncherCode/job'
        comev = tk.StringVar()
        comboxlist=ttk.Combobox(root,textvariable=comev) #初始化
        with open("icopath.psw","r") as fpico:
                aico = fpico.read()
        if aico == "004":
                comboxlist.insert(0, '最近任务')
                comboxlist["values"]="尚无任务"
        else:
                comboxlist.insert(0, '最近任务')
                comboxlist["values"]=os.listdir(path)
        comboxlist.bind("<<ComboboxSelected>>",go)
        comboxlist.pack()

#清空
        def clsee():
                cpk.unpathfilewrite("apppath.psw", "w", "标签")
                fp.exitesys(root,pids)
                root.destroy()
        
        imcls = Image.open(fath_path + "/HandrilowOSLauncherCode/H_icon/CLEAN.png")
        photocls = ImageTk.PhotoImage(imcls)
        othcls = tk.Button(root,image=photocls,bd=0,bg=A4,pady=3,command=clsee)
        othcls.pack(side='bottom',pady=2)

        w_box = 80
        h_box = 80  
                
        def resize(w, h, w_box, h_box, pil_image):  
                f1 = 1.0*w_box/w 
                f2 = 1.0*h_box/h  
                factor = min([f1, f2])
                width = int(w*factor)  
                height = int(h*factor)  
                return pil_image.resize((width, height), Image.ANTIALIAS)
        def getico():
                with open("icopath.psw","r") as f:
                        tipicon = f.read()
                fileexists = os.path.exists(tipicon)
                if tipicon == "004":
                        file = './HandrilowOSLauncherCode/H_icon/HANDRIL.png'
                elif fileexists == False:
                        file = './HandrilowOSLauncherCode/H_icon/HANDRIL.png'
                else:
                        file = tipicon 
                return file
        win11 = tk.Label(root, width=w_box, height=h_box,bg=A4)
        pil_image = Image.open(getico()) 
        w, h = pil_image.size  
        pil_image_resized = resize(w, h, w_box, h_box, pil_image)  
        tk_image = ImageTk.PhotoImage(pil_image_resized)
        win11.config(image=tk_image) 
        win11.pack(side='bottom',pady=10)
        
        root.mainloop()
#################################################################
def handrilmenu():
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/m1.pid"
        root = tk.Toplevel()
        root.wm_attributes("-topmost", True)
        root.config(cursor='circle')
        #窗口移动函数
        def on_move(event):
                root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
                width, height = None, None
                offset_x = event.x_root - root_x
                offset_y = event.y_root - root_y
                if width and height:
                    geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
                else:
                    geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
                    root.geometry(geo_str)
                def _on_tap(event):
                    root_x, root_y = event.x_root, event.y_root
                    abs_x, abs_y = winfo_x(), winfo_y()
        root.bind('<B1-Motion>', on_move)
        root.attributes('-alpha',0.9)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if 800 <= sw <= 1366:
                shd = round(25)
        elif 1366 < sw <= 1920:
                shd = round(25)
        swcstr = str(root.winfo_screenwidth())
        #######################
        swc=120
        if swcstr > '1600':
                shc=290
        else:
                shc=240
        x = 5
        y=31
        
        root.geometry('+%d+%d'%(x,y))
        root['background']= A4
        cpk.overide(root)
        f1 = tk.Frame(root,bg=A4)
        f1.pack(side='top')
        #root = handriltopmenuWindow()
        hmenulist=['我的账户','系统爱好设置','应用列表','应用商店','最近的文件','重启','关于本机','关机']
        d = len(hmenulist)
        
        def exite():
                fp.exitesys(root,pids)
                root.destroy()
        def menuexite(_):
                exite()

        osname = sys_name.name()
        if osname == 'nt':
                path = fath_path + '/HandrilowOSLauncherCode/sys/programe/'
        else:
                path = '/usr/share/applications/'
        filenames = os.listdir(path)
        linker.applist(root,filenames,path,A4,f1)

        #小白条
        filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
        photo = ImageTk.PhotoImage(file=filename)
        def jump2(_):
                cpk.mwoutto(bottomtype,'bottom',0,0,3)
                exite()
        def mydock(_):
                exite()
        bottomtype = tk.Label(root,image=photo,bd=0,width=150,height=5)
        bottomtype.bind('<Leave>',jump2)
        cpk.mwinto(bottomtype,'bottom',0,0,3)
#关于本机
        def vat():
                exite()
                
                sc.about()
        def enter(_):
                def leave(_):
                        m7.config(bg=A4)
                m7.config(bg='#AAAAAA')
                m7.bind('<Leave>',leave)
        m7 = tk.Button(f1,bd=0,bg=A4,pady=3,command=vat,anchor='w')
        m7.config(text=hmenulist[6])
        m7.bind('<Enter>',enter)
        m7.pack(side='left',padx=0,pady=2)
        
#关机
        def vats():
                shutil.rmtree('./HandrilowOSLauncherCode/H_fileprocess')
                os.mkdir('./HandrilowOSLauncherCode/H_fileprocess')
                os.system('poweroff')
        def enters(_):
                def leaves(_):
                        m8.config(bg=A4,fg='black')
                m8.config(bg='#AAAAAA')
                m8.bind('<Leave>',leaves)
        m8 = tk.Button(f1,bd=0,bg=A4,pady=3,command=vats,anchor='w')
        m8.config(text=hmenulist[7])
        m8.bind('<Enter>',enters)
        m8.pack(side='left',padx=0,pady=2)
        
#reboot
        def vatsre():
                shutil.rmtree('./HandrilowOSLauncherCode/H_fileprocess')
                os.mkdir('./HandrilowOSLauncherCode/H_fileprocess')
                os.system('reboot')
        def entersre(_):
                def leavesre(_):
                        m9.config(bg=A4,fg='black')
                m9.config(bg='#AAAAAA')
                m9.bind('<Leave>',leavesre)
        m9 = tk.Button(f1,bd=0,bg=A4,pady=3,command=vatsre,anchor='w')
        m9.config(text=hmenulist[5])
        m9.bind('<Enter>',enters)
        m9.pack(side='left',padx=0,pady=2)
        
        #菜单项对应图标
        A5=  A4
        w_box = 60
        h_box = w_box
        def resize12(w, h, w_box, h_box, pil_image):  
                f1 = 1.0*w_box/w 
                f2 = 1.0*h_box/h  
                factor = min([f1, f2])
                width = int(w*factor)  
                height = int(h*factor)  
                return pil_image12.resize((width, height), Image.ANTIALIAS)
        win1112 = tk.Label(root,text="Taskmgr",width=w_box, height=h_box,bg=A5)
        pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/Application.png') 
        w, h = pil_image12.size  
        pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)  
        tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
        win1112.config(image=tk_image12) 
        win1112.pack(side='bottom',padx=5,pady=1)
        
        root.mainloop()
#################################################################

def fangzhi():
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/fangzhi.pid"
        root = tk.Toplevel()
        root.wm_attributes("-topmost", True)
        root.config(cursor='circle')
        #窗口移动函数
        def on_move(event):
                root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
                width, height = None, None
                offset_x = event.x_root - root_x
                offset_y = event.y_root - root_y
                if width and height:
                    geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
                else:
                    geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
                    root.geometry(geo_str)
                def _on_tap(event):
                    root_x, root_y = event.x_root, event.y_root
                    abs_x, abs_y = winfo_x(), winfo_y()
        root.bind('<B1-Motion>', on_move)
        root.attributes('-alpha',0.9)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if 800 <= sw <= 1366:
                shd = round(25)
        elif 1366 < sw <= 1920:
                shd = round(25)
        swcstr = str(root.winfo_screenwidth())
        #######################
        swc=120
        if swcstr > '1600':
                shc=290
        else:
                shc=240
        with open("postx.psw", "r", encoding='utf-8') as f:
            data = f.read()
        x = int(data)-15
        #y=sh*(21/768)
        y=31
        root.geometry('+%d+%d'%(x,y))
        root['background']= A4
        cpk.overide(root)
        #root = handriltopmenuWindow()
        hmenulist=['锁定屏幕','文档','图片','视频','音频','网页','还原系统','⭕无操作']
        d = len(hmenulist)
        def exite():
                fp.exitesys(root,pids)
                root.destroy()
        #小白条
        filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
        photo = ImageTk.PhotoImage(file=filename)
        def jump2(_):
                cpk.mwoutto(bottomtype,'bottom',0,0,3)
                exite()
        def mydock(_):
                exite()
        bottomtype = tk.Label(root,image=photo,bd=0,width=50,height=5)
        bottomtype.bind('<Leave>',jump2)
        cpk.mwinto(bottomtype,'bottom',0,0,3)

#显示器
        def lockscreen():
            cpk.prtscother()
            cpk.lockpart()
        def tolock():
            lockscreen()
        def midlock(_):
            tolock()
        def enter(_):
                def leave(_):
                        m1.config(bg=A4)
                m1.config(bg='#AAAAAA')
                m1.bind('<Leave>',leave)
        m1 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,anchor='w')
        m1.config(text=hmenulist[0])
        m1.bind('<Enter>',enter)
        m1.bind('<Button-1>',midlock)
        for i in range(0,15)[::-1]:
                m1.pack(padx=5,pady=2)
                m1.update()
#蓝牙
        def enter(_):
                def leave(_):
                        m2.config(bg=A4)
                m2.config(bg='#AAAAAA')
                m2.bind('<Leave>',leave)
        def topic():
                exite()
                picture.main()
        m2 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=topic,anchor='w')
        m2.config(text=hmenulist[2])
        m2.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m2.pack(padx=5,pady=2)
                m2.update()
#声音
        def doc(_):
                exite()
                document.main()
        def enter(_):
                def leave(_):
                        m3.config(bg=A4)
                m3.config(bg='#AAAAAA')
                m3.bind('<Leave>',leave)
        m3 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite,anchor='w')
        m3.config(text=hmenulist[1])
        m3.bind('<Enter>',enter)
        m3.bind('<Button-1>',doc)
        for i in range(0,15)[::-1]:
                m3.pack(padx=5,pady=2)
                m3.update()
#我的手机
        def vid(_):
                exite()
                video.main()
        def enter(_):
                def leave(_):
                        m4.config(bg=A4)
                m4.config(bg='#AAAAAA')
                m4.bind('<Leave>',leave)
        m4 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite,anchor='w')
        m4.config(text=hmenulist[3])
        m4.bind('<Enter>',enter)
        m4.bind('<Button-1>',vid)
        for i in range(0,15)[::-1]:
                m4.pack(padx=5,pady=2)
                m4.update()
#应用程序
        def enter(_):
                def leave(_):
                        m5.config(bg=A4)
                m5.config(bg='#AAAAAA')
                m5.bind('<Leave>',leave)
        def tomusic():
                exite()
                scound.playsoundmode()
        m5 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=tomusic,anchor='w')
        m5.config(text=hmenulist[4])
        m5.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m5.pack(padx=5,pady=2)
                m5.update()
#文件搜索
        def enter(_):
                def leave(_):
                        m6.config(bg=A4)
                m6.config(bg='#AAAAAA')
                m6.bind('<Leave>',leave)
        def tochackallfile():
                exite()
                
                allfile.main()
        m6 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=tochackallfile,anchor='w')
        m6.config(text=hmenulist[5])
        m6.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m6.pack(padx=5,pady=2)
                m6.update()
#还原系统
        def end():
                exite()
                os.remove('usr_info.pickle')
                cpk.unpathfilewrite("usename.psw","w","HanBook")
                os.remove('./HandrilowOSLauncherCode/sys/login.sys')
                root.destroy()
                cpk.message('√系统已还原','下次启动时生效')
        def enter(_):
                def leave(_):
                        m7.config(bg=A4)
                m7.config(bg='#AAAAAA')
                m7.bind('<Leave>',leave)
        m7 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=end,anchor='w')
        m7.config(text=hmenulist[6])
        m7.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m7.pack(padx=5,pady=2)
                m7.update()
#菜单项对应图标
        A5=  A4
        w_box = 60
        h_box = w_box
        def resize12(w, h, w_box, h_box, pil_image):  
                f1 = 1.0*w_box/w 
                f2 = 1.0*h_box/h  
                factor = min([f1, f2])
                width = int(w*factor)  
                height = int(h*factor)  
                return pil_image12.resize((width, height), Image.ANTIALIAS)
        win1112 = tk.Label(root,text="Taskmgr",width=w_box, height=h_box,bg=A5)
        pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/FILE.png') 
        w, h = pil_image12.size  
        pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)  
        tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
        win1112.config(image=tk_image12) 
        win1112.pack(side='bottom',padx=5,pady=1)
        
        root.mainloop()
#################################################################
def add():
        root = tk.Toplevel()
        root.wm_attributes("-topmost", True)
        root.config(cursor='circle')
        #窗口移动函数
        def on_move(event):
                root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
                width, height = None, None
                offset_x = event.x_root - root_x
                offset_y = event.y_root - root_y
                if width and height:
                    geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
                else:
                    geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
                    root.geometry(geo_str)
                def _on_tap(event):
                    root_x, root_y = event.x_root, event.y_root
                    abs_x, abs_y = winfo_x(), winfo_y()
        root.bind('<B1-Motion>', on_move)
        root.attributes('-alpha',0.9)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if 800 <= sw <= 1366:
                shd = round(25)
        elif 1366 < sw <= 1920:
                shd = round(25)
        swcstr = str(root.winfo_screenwidth())
        #######################
        swc=120
        if swcstr > '1600':
                shc=290
        else:
                shc=240
        with open("postx.psw", "r", encoding='utf-8') as f:
            data = f.read()
        x = int(data)-15
        #y=sh*(21/768)
        y=31
        root.geometry('+%d+%d'%(x,y))
        root['background']= A4
        cpk.overide(root)
        #root = handriltopmenuWindow()
        hmenulist=['环境变量','生物数据','组件和壁纸','可移动应用','系统组件','终端','系统更新','⭕无操作']
        d = len(hmenulist)
        def exite():
                root.destroy()
        #小白条
        filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
        photo = ImageTk.PhotoImage(file=filename)
        def jump2(_):
                cpk.mwoutto(bottomtype,'bottom',0,0,3)
                exite()
        def mydock(_):
                exite()
        bottomtype = tk.Label(root,image=photo,bd=0,width=50,height=5)
        bottomtype.bind('<Leave>',jump2)
        cpk.mwinto(bottomtype,'bottom',0,0,3)

        def togo():
               exite()
               epc.main()
        def enter(_):
                def leave(_):
                        m1.config(bg=A4)
                m1.config(bg='#AAAAAA')
                m1.bind('<Leave>',leave)
        m1 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=togo,anchor='w')
        m1.config(text=hmenulist[0])
        m1.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m1.pack(padx=5,pady=2)
                m1.update()

        def voice():
               None
                
        def pic():
               exite()
               cammerview.addface()
        def enter(_):
                def leave(_):
                        m2.config(bg=A4)
                m2.config(bg='#AAAAAA')
                m2.bind('<Leave>',leave)
        m2 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=voice,anchor='w')
        m2.config(text=hmenulist[2])
        m2.bind('<Enter>',enter)
        m2.bind('<Button-1>',pic)
        for i in range(0,15)[::-1]:
                m2.pack(padx=5,pady=2)
                m2.update()

        def enter(_):
                def leave(_):
                        m3.config(bg=A4)
                m3.config(bg='#AAAAAA')
                m3.bind('<Leave>',leave)
        m3 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=pic,anchor='w')
        m3.config(text=hmenulist[1])
        m3.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m3.pack(padx=5,pady=2)
                m3.update()

        def addapp():
                exite()
                tool_app.main()
                
        def enter(_):
                def leave(_):
                        m4.config(bg=A4)
                m4.config(bg='#AAAAAA')
                m4.bind('<Leave>',leave)
        m4 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=addapp,anchor='w')
        m4.config(text=hmenulist[3])
        m4.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m4.pack(padx=5,pady=2)
                m4.update()

        def enter(_):
                def leave(_):
                        m5.config(bg=A4)
                m5.config(bg='#AAAAAA')
                m5.bind('<Leave>',leave)
        m5 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite,anchor='w')
        m5.config(text=hmenulist[4])
        m5.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m5.pack(padx=5,pady=2)
                m5.update()

        def enter(_):
                def leave(_):
                        m6.config(bg=A4)
                m6.config(bg='#AAAAAA')
                m6.bind('<Leave>',leave)
        def terminal():
        	exite()
        	Horder.main()
        m6 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=terminal,anchor='w')
        m6.config(text=hmenulist[5])
        m6.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m6.pack(padx=5,pady=2)
                m6.update()

        def end():
                os.system('/usr/bin/x-terminal-emulator')
                exite()
                None
        def enter(_):
                def leave(_):
                        m7.config(bg=A4)
                m7.config(bg='#AAAAAA')
                m7.bind('<Leave>',leave)
        m7 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=end,anchor='w')
        m7.config(text=hmenulist[6])
        m7.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m7.pack(padx=5,pady=2)
                m7.update()
#菜单项对应图标
        A5=  A4
        w_box = 60
        h_box = w_box
        def resize12(w, h, w_box, h_box, pil_image):  
                f1 = 1.0*w_box/w 
                f2 = 1.0*h_box/h  
                factor = min([f1, f2])
                width = int(w*factor)  
                height = int(h*factor)  
                return pil_image12.resize((width, height), Image.ANTIALIAS)
        win1112 = tk.Label(root,text="Taskmgr",width=w_box, height=h_box,bg=A5)
        pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/ADD.png') 
        w, h = pil_image12.size  
        pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)  
        tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
        win1112.config(image=tk_image12) 
        win1112.pack(side='bottom',padx=5,pady=1)
        
        root.mainloop()
#######################
#################################################################


def order():
        cpk.order()

#编辑
def bianji():
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/bianji.pid"
        root = tk.Toplevel()
        root.wm_attributes("-topmost", True)
        root.config(cursor='circle')
        root.attributes('-alpha',0.9)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if 800 <= sw <= 1366:
                shd = round(25)
        elif 1366 < sw <= 1920:
                shd = round(25)
        swcstr = str(root.winfo_screenwidth())
        #窗口移动函数
        def on_move(event):
                root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
                width, height = None, None
                offset_x = event.x_root - root_x
                offset_y = event.y_root - root_y
                if width and height:
                    geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
                else:
                    geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
                    root.geometry(geo_str)
                def _on_tap(event):
                    root_x, root_y = event.x_root, event.y_root
                    abs_x, abs_y = winfo_x(), winfo_y()
        root.bind('<B1-Motion>', on_move)
        #######################
        swc=130
        if swcstr > '1600':
                shc=100
        else:
                shc=100
        with open("postx.psw", "r", encoding='utf-8') as f:
            data = f.read()
        x = int(data)-15
        #y=sh*(21/768)
        y=31
        root.geometry('+%d+%d'%(x,y))
        root['background']= A4
        cpk.overide(root)
        #root = handriltopmenuWindow()
        hmenulist=['创建文件','文本','隔空操作']
        d = len(hmenulist)
        def exite():
                fp.exitesys(root,pids)
                root.destroy()
        #小白条
        filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
        photo = ImageTk.PhotoImage(file=filename)
        def jump2(_):
                cpk.mwoutto(bottomtype,'bottom',0,0,3)
                exite()
        def mydock(_):
                exite()
        bottomtype = tk.Label(root,image=photo,bd=0,width=50,height=5)
        bottomtype.bind('<Leave>',jump2)
        cpk.mwinto(bottomtype,'bottom',0,0,3)
#创建文件       
        def enter(_):
                def leave(_):
                        m1.config(bg=A4)
                m1.config(bg='#AAAAAA')
                m1.bind('<Leave>',leave)
        m1 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite,anchor='w')
        m1.config(text=hmenulist[0])
        m1.bind('<Enter>',enter)
        for i in range(0,15)[::-1]:
                m1.pack(padx=5,pady=2)
                m1.update()
#文本
        def exite_launch_bianji():
                fp.exitesys(root,pids)
                root.destroy()
                cpk.notetype()
        def enter1(_):
                def leave1(_):
                        m2.config(bg=A4)
                m2.config(bg='#AAAAAA')
                m2.bind('<Leave>',leave1)
        m2 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite_launch_bianji,anchor='w')
        m2.config(text=hmenulist[1])
        m2.bind('<Enter>',enter1)
        for i in range(0,15)[::-1]:
                m2.pack(padx=5,pady=2)
                m2.update()

        def exite_launch_gekong():
                fp.exitesys(root,pids)
                root.destroy()
                from .openHandrilow.septum import septum
                desktip = HandrilApp()
                gekong = multiprocessing.Process(target = septum.main())
                gekong.start()
                def exit_stem():
                        gekong.exitcode
                to_tip = tk.Button(desktip,text='取消隔空操作',font=('黑体',15),bd=0,command=exit_stem)
                to_tip.pack()
                desktip.mainloop()
        def enter1_m3(_):
                def leave1_m3(_):
                        m3.config(bg=A4)
                m3.config(bg='#AAAAAA')
                m3.bind('<Leave>',leave1_m3)
        m3 = tk.Button(root,width=15,bd=0,bg=A4,pady=3,command=exite_launch_gekong,anchor='w')
        m3.config(text=hmenulist[2])
        m3.bind('<Enter>',enter1_m3)
        for i in range(0,15)[::-1]:
                m3.pack(padx=5,pady=2)
                m3.update()

#菜单项对应图标
        A5=  A4
        w_box = 60
        h_box = w_box
        def resize12(w, h, w_box, h_box, pil_image):  
                f1 = 1.0*w_box/w 
                f2 = 1.0*h_box/h  
                factor = min([f1, f2])
                width = int(w*factor)  
                height = int(h*factor)  
                return pil_image12.resize((width, height), Image.ANTIALIAS)
        win1112 = tk.Label(root,text="Taskmgr",width=w_box, height=h_box,bg=A5)
        pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/EDIT.png') 
        w, h = pil_image12.size  
        pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)  
        tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
        win1112.config(image=tk_image12) 
        win1112.pack(side='bottom',padx=5,pady=1)

        root.mainloop()
