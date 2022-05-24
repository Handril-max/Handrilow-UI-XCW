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
from HandrilowOSLauncherCode.openHandrilow import sys_win_cartoon as swc

#初始位置
wx=35
wy=40
num = 0
def main():
    def go():
        filepaths='./HandrilowOSLauncherCode/UserFile'
        global wx,wy,num
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

        pifi = os.listdir(filepaths)
        filename = pifi
        finum = len(pifi)
        num += 1
        name_nn = tk.Label(rootA,width=w_box,bg='#AAAAAA',fg='white')
        name_nn.config(text=filename[num-1])
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

        
        if num !=finum:
            go()
        if num == finum:
            print('done')
            
        rootA.mainloop()
    go()



