#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#Handril path set
# -*- coding:utf-8 -*-
import os
import tkinter as tk
from HandrilowOSLauncherCode import cpupack as cpk

def main():
        window_sign_up=tk.Toplevel()
        window_sign_up.wm_attributes("-topmost", True)
        sw = window_sign_up.winfo_screenwidth()
        sh = window_sign_up.winfo_screenheight()
        if 800 <= sw <= 1366:
                shd = round(sh*(27/768))
        elif 1366 < sw <= 1920:
                shd = round(sh*(22/768))
        swcstr = str(window_sign_up.winfo_screenwidth())
        #######################
        swc=120
        if swcstr > '1600':
                shc=290
        else:
                shc=240
        x = 80
        y=shd+6

        def exite():
            window_sign_up.destroy()
        window_sign_up.geometry('+%d+%d'%(x,y))
        window_sign_up.overrideredirect(True)
        new_name=tk.StringVar()

        line1 = tk.Label(window_sign_up)
        line1.pack(side='top')
        line2 = tk.Label(window_sign_up)
        line2.pack(side='top')
        line3 = tk.Label(window_sign_up)
        line3.pack(side='top')
        
        tk.Label(line1,text='总体变量',font=('等线',10),bd=0).pack(side='left',padx=3,pady=3)
        new_pwd=tk.Entry(line1,textvariable=new_name,bd=0)
        new_pwd.pack(side='left',padx=3,pady=3)
        new_pwd=tk.StringVar()
        
        tk.Label(line2,text='图形变量',font=('等线',10),bd=0).pack(side='left',padx=3,pady=3)
        new_pwd_confirm=tk.Entry(line2,textvariable=new_pwd,bd=0)
        new_pwd_confirm.pack(side='left',padx=3,pady=3)
        new_pwd_confirm=tk.StringVar()
        
        tk.Label(line3,text='文件变量',font=('等线',10),bd=0).pack(side='left',padx=3,pady=3)
        new_pwd_confirm1=tk.Entry(line3,textvariable=new_pwd_confirm,bd=0)
        new_pwd_confirm1.pack(side='left',padx=3,pady=3)    
        bt_confirm_sign_up=tk.Button(window_sign_up,text='确认更改',font=('等线',12),bd=0)
        bt_confirm_sign_up.pack(side='left',padx=3,pady=3)

        bt_confirm_sign_up=tk.Button(window_sign_up,text='⭕无操作',font=('等线',10),bd=0,
                                 bg='#DDDDDD',command=exite)
        bt_confirm_sign_up.pack(side='left',padx=3,pady=3)

        window_sign_up.mainloop()
    
