#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#Handril screen top status
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import six
import shutil
import string 
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from windoweng import *
from shutil import *
import colorlib
import colorlib as hcol
import HMmenu
import cpupack as cpk
import fileprocess as fp


#TOPMAINMENU    
def main(m3):
            w_box = 50
            h_box = 50  
                
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
                        print(tipicon)
                    fileexists = os.path.exists(tipicon)
                    if tipicon == "004" and fileexists == False:
                        print('原图标')
                        file = './H_icon/MAINDOCK9.png'
                    else:
                        print('应用图标')
                        file = tipicon 
                    return file
                getico()
            win11 = tk.Label(m3, width=w_box, height=h_box,bg='black')
            pil_image = Image.open(getico()) 
            w, h = pil_image.size  
            pil_image_resized = resize(w, h, w_box, h_box, pil_image)  
            tk_image = ImageTk.PhotoImage(pil_image_resized)
            win11.config(image=tk_image) 
            win11.pack(side='bottom',padx=2,pady=1)