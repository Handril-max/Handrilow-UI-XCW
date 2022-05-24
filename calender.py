# py:3
# HandrilOS@Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril calender
# -*- coding:utf-8 -*-
from tkinter import *
import os
import time
import datetime
import tkinter as tk
from PIL import ImageTk, Image
import calendar
from windoweng import *
import Hmessage
from shutil import *
import colorlib
import colorlib as hcol
import cpupack as cpk
import HMmenu
import date
import windoweng
import fileprocess as fp


def main():
    #pids = "./H_fileprocess/rili.pid"
    # fp.mainapp(pids)
    #root = calenderWindow()
    root = DragWindow()
    A3 = colorlib.black1()
    A4 = '#F0F0F0'
    root['background'] = A4

    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    swcstr = str(root.winfo_screenwidth())

    filename1 = r'./H_icon\H_show\H_rili\RILI1.png'
    photo1 = ImageTk.PhotoImage(file=filename1)
    filename2 = r'./H_icon\H_show\H_rili\RILI2.png'
    photo2 = ImageTk.PhotoImage(file=filename2)
    filename3 = r'./H_icon\H_show\H_rili\RILI3.png'
    photo3 = ImageTk.PhotoImage(file=filename3)
    filename4 = r'./H_icon\H_show\H_rili\RILI4.png'
    photo4 = ImageTk.PhotoImage(file=filename4)
    filename5 = r'./H_icon\H_show\H_rili\RILI5.png'
    photo5 = ImageTk.PhotoImage(file=filename5)
    filename6 = r'./H_icon\H_show\H_rili\RILI6.png'
    photo6 = ImageTk.PhotoImage(file=filename6)
    filename7 = r'./H_icon\H_show\H_rili\RILI7.png'
    photo7 = ImageTk.PhotoImage(file=filename7)
    filename8 = r'./H_icon\H_show\H_rili\RILI8.png'
    photo8 = ImageTk.PhotoImage(file=filename8)
    filename9 = r'./H_icon\H_show\H_rili\RILI9.png'
    photo9 = ImageTk.PhotoImage(file=filename9)
    filename10 = r'./H_icon\H_show\H_rili\RILI10.png'
    photo10 = ImageTk.PhotoImage(file=filename10)
    filename11 = r'./H_icon\H_show\H_rili\RILI11.png'
    photo11 = ImageTk.PhotoImage(file=filename11)
    filename12 = r'./H_icon\H_show\H_rili\RILI12.png'
    photo12 = ImageTk.PhotoImage(file=filename12)

    filename2 = r'./H_icon\H_show\close.png'
    photoclose = ImageTk.PhotoImage(file=filename2)

    today = datetime.datetime.today()
    year = today.year
    month = today.month

    if swcstr > '1600':
        sw = 1200
    else:
        sw = 800
    sh = 500
    x = (swc-800)/2
    y = (shc-450)/2
    root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    root.overrideredirect(True)
    for b in range(0, 200, 10)[::1]:
        root.attributes('-alpha', b/100)
        root.update()
        time.sleep(0.013)

    pic = tk.Label(root, width=250, height=500, bd=0, bg=A4)
    if month == 1:
        pic.config(image=photo1)
    elif month == 2:
        pic.config(image=photo2)
    elif month == 3:
        pic.config(image=photo3)
    elif month == 4:
        pic.config(image=photo4)
    elif month == 5:
        pic.config(image=photo5)
    elif month == 6:
        pic.config(image=photo6)
    elif month == 7:
        pic.config(image=photo7)
    elif month == 8:
        pic.config(image=photo8)
    elif month == 9:
        pic.config(image=photo9)
    elif month == 10:
        pic.config(image=photo10)
    elif month == 11:
        pic.config(image=photo11)
    elif month == 12:
        pic.config(image=photo12)

    for i in range(0, 350, 35)[::-1]:
        pic.pack(side='left', padx=i)
        time.sleep(0.033)
        pic.update()

    def cls():
        None

    def exite():
        # fp.exite(root,pids)
        root.destroy()

    close = tk.Button(root, bd=0, fg=A3, image=photoclose,
                      bg=A4, command=exite)
    for i1 in range(0, 5)[::1]:
        close.pack(side='top', pady=i1)
        time.sleep(0.053)
        close.update()

    name = tk.Label(
        root, text='日历 | Handrilow OS 2021H4-1366768', bd=0, fg=A3, bg=A4)
    for i2 in range(0, 5)[::-1]:
        name.pack(side='bottom', pady=i2)
        time.sleep(0.033)
        name.update()

    wenben = tk.Text(root, fg=A3, bg=A4, font=(
        '黑体', 30), width=50, height=50, bd=0)
    wenben.insert(tk.INSERT, calendar.month(year, month))
    for i3 in range(40, 50):
        wenben.pack(side='right', padx=i3, pady=60)
        time.sleep(0.013)
        wenben.update()
    root.mainloop()
