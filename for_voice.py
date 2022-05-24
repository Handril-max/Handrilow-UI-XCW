# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril voice
# -*- coding:utf-8 -*-
from . import cpupack as cpk
from .openHandrilow.sys_windoweng import *
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
from tkinter import *
def main():
    root = HandrilAppNode()
    sw = root.winfo_screenwidth()
    shd = round(25)
    with open("postx.psw", "r", encoding='utf-8') as f:
            data = f.read()
    x = int(data)-300
    y=shd+6
    root.geometry('+%d+%d'%(x,y))
    def tosetvoice():
        per = int(voice.get())
        to_per = (per/100)*(-65.25)
        volume.SetMasterVolumeLevel(to_per, None)
        voice.after(1000,tosetvoice)
    voice = Scale(root,from_=0,to=100,tickinterval=100,orient=HORIZONTAL,length=350)
    voice.pack()
    tosetvoice()
    mainloop()