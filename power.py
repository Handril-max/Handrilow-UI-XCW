# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril power
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import six
import shutil
import string
import win32api
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from windoweng import *
import pyautogui as pag
from shutil import *
import colorlib
import linker
import colorlib as hcol
import cpupack as cpk
import fileprocess as fp

A4 = '#DDDDDD'
shd = 40


def main(function):
    A = handriltopmenuWindow()
    sw = A.winfo_screenwidth()
    sh = A.winfo_screenheight()
    #######################
    swc = 200
    shc = 120
    x = 140
    # y=sh*(21/768)
    y = shd+1
    A.geometry('%dx%d+%d+%d' % (swc, shc, x, y))
    A['background'] = A4
    A.overrideredirect(True)
    w_box = 80
    h_box = 80

    def off(_):
        function

    def resize(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def getico():
        file = './H_icon/POWER.png'
        return file
    win11 = tk.Label(A, width=w_box, height=h_box, bg=A4)
    pil_image = Image.open(getico())
    w, h = pil_image.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.bind('<button-1>', off)
    win11.pack(side='left', padx=5, pady=10)
    A.after(3000, A.destroy)
    A.mainloop()
