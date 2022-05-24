#py3
#Handrilsoft
#Bluetooth
import bluetooth
from cgitb import grey
from .openHandrilow.sys_windoweng import *
import tkinter as tk
from .openHandrilow import set_path
from .openHandrilow import sys_bluetooth
from . import threadpool as thdpol
fath_path = set_path.pwd()
def main():
    cpk.unpathfilewrite("apppath.psw", "w", "蓝牙")
    root = HandrilAppTop('蓝牙状态')
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    w_box = 50
    h_box = 50
    
    top = tk.Frame(root)
    top.pack(side='top',pady=5)
    dev_lis = tk.Frame(root)
    dev_lis.pack(side='top',pady=10)
    dev_fun = tk.Frame(root)
    dev_fun.pack(side='bottom',pady=5)
    function = tk.Frame(root)
    function.pack(side='bottom',pady=5)
    
    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(top, text="Taskmgr", width=w_box, height=h_box)
    pil_imag = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/BLUETOOTH.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left')
    title = tk.Label(top,justify='left',text='蓝牙',font=('黑体', 16))
    title.pack(side='left')
    tip = tk.Label(top,justify='left',text='''Handrilow XCW Bluetooth
Copyright @ 2109-2022 XIAN China''',font=('黑体', 10))
    tip.pack(side='left')
    
    title = tk.Label(dev_fun,justify='left',text='本设备名称>',font=('黑体', 12))
    title.pack(side='left')
    with open("usename.psw", "r") as f:
        data = f.read()
    dev_nam = tk.Label(dev_fun,text=data,font=('黑体', 12))
    dev_nam.pack(side='left')
    
    def resize(w, h, w_box, h_box, pil_image_righttip):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(dev_lis, text="Taskmgr",
                        width=w_box, height=h_box)
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/add.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.pack(side='left')
    title = tk.Label(dev_lis,justify='left',text='添加',font=('黑体', 16))
    title.pack(side='left')
    tip = tk.Label(dev_lis,justify='left',text='''点击“+”号添加相关设备
:-)在此选择添加比如耳机，移动设备
Hanphone音箱等''',font=('黑体', 10))
    tip.pack(side='left')
    
    def test_dev():
        nearby_devices = thdpol.dissetp.thd2(bluetooth.discover_devices(lookup_names=True, lookup_class=True))
        for (addr, name,type) in nearby_devices:
            title_name = tk.Label(root,text=sys_bluetooth.device_type(type,name),justify='left')
            title_name.pack(side='top') 
            
    def test_dev2():
        time = 0
        nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
        print(nearby_devices)
        
        root = HandrilAppTop('蓝牙耳机')
        swc = root.winfo_screenwidth()
        shc = root.winfo_screenheight()
        w_box = round(swc/20)
        h_box = w_box
        A4 = 'white'
        root['bg']=A4
        def resize(w, h, w_box, h_box, pil_image_righttip):
            f1 = 1.0*w_box/w
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            width = int(w*factor)
            height = int(h*factor)
            return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
        righttip = tk.Label(root, text="Taskmgr",width=w_box, height=h_box,bg=A4)
        pil_image_righttip = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/bluetooth/device/HANBLUE.png')
        w, h = pil_image_righttip.size
        pil_image_resized_righttip = resize(w, h, w_box, h_box, pil_image_righttip)
        tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
        righttip.config(image=tk_image_righttip)
        righttip.pack(side='top',pady=20) 
        for (addr, name,type) in nearby_devices:
            title_name = tk.Label(root,text=sys_bluetooth.device_type(type,name),bg=A4)
            title_name.pack(side='top',pady=2)  
        
        title = tk.Label(root,justify='left',text=':-)检测到蓝牙设备',font=('黑体', 15),bg=A4)
        title.pack(side='bottom',pady=20)
           
        root.mainloop()
            
    test = tk.Button(function,text='检测刷新',bd=1,font=('黑体', 12),height=2,command=test_dev)
    test.pack(side='left',pady=3,padx=3)
    discon = tk.Button(function,text='断开连接',bd=0,font=('黑体', 12),height=2)
    discon.pack(side='left',pady=3,padx=3)
    connect = tk.Button(function,text='连接到...',bd=0,font=('黑体', 12),height=2)
    connect.pack(side='left',pady=3,padx=3)
    help = tk.Button(function,text='帮助',bd=0,font=('黑体', 12),height=2)
    help.pack(side='left',pady=3,padx=3)
    
    root.mainloop()
    