# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril screen top status
# -*- coding:utf-8 -*-
import tkinter as tk
import os
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol
A4 = 'white'
A5 = A4
pid_cammer = './HandrilowOSLauncherCode/H_fileprocess/cammer_transter.pid'


def cammer_transfer(m3):
    print('cammer_ico loading')
    name = tk.Label(m3, text="●", bg=A5, fg='green', font=(None, 10))

    fileexists = os.path.exists(pid_cammer)
    if fileexists != False:
        print('cammer_ico_destroy loading')
        None
    elif fileexists != True:
        print('cammer_ico_go loading')
        name.pack(side='left', padx=1, pady=2)
    else:
        cpk.message('提示', '摄像头错误！')

    def clean():
        while True:
            fileexists = os.path.exists(pid_cammer)
            print('789')
            if fileexists != False:
                print('cammer_ico_destroy loading')
                name.pack(side='left', padx=1, pady=2)

            elif fileexists != True:
                name.destroy()
                None
            print('78934567')
        # m3.after(1000,clean)
    thdpol.dissetp.thd(clean)
