import pywifi , time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from .openHandrilow.sys_windoweng import *
from HandrilowOSLauncherCode import windoweng 
from HandrilowOSLauncherCode import netconnect as netcon
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import progressbar as pgb
from .openHandrilow import set_path
from .openHandrilow import sys_bluetooth
from . import threadpool as thdpol
fath_path = set_path.pwd()

def discon():
    #netcon.discon()
    None()
def connectTest():#检测是否链接信号
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    if iface.status() == 4:
        status = '4'
        print('connect')
    else:
        status = '0'
        print('unconnect')
    return status
            
def order():#命令行获取
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    result=iface.scan_results()
    for i in result:
        print(i.ssid.encode('raw_unicode_escape').decode('utf-8'))
        
def main():
    cpk.unpathfilewrite("apppath.psw", "w", "无线网络状态")
    root = HandrilAppTop('无线网络状态')
    A4 = 'white'
    top = tk.Frame(root,bg='white')
    top.place(x=10,y=10)
    
    m1 = tk.Frame(root,bg='white')
    m1.pack(side='bottom')
    m2 = tk.Frame(root,bg='white')
    m2.pack(side='bottom')
    m3 = tk.Frame(root,bg='white')
    m3.pack(side='bottom',pady=5)
    input = tk.Frame(root,bg='white')
    input.pack(side='bottom')
    right_mode = tk.Frame(root,bg='white')
    right_mode.pack(side='right',padx=20,pady=5)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    if 800 <= sw <= 1366:
        shd = round(sh*(27/768))
        x = round(sh*(940/768))
    elif 1366 < sw <= 1920:
        shd = round(sh*(22/768))
        x = round(sw*(1000/1366))
    #######################
    swc=round(sh*(120/768))
    shc=round(sh*(120/768))
    w_box = 50
    h_box = 50
    y=shd+6
    root['background']= 'white'
    #窗口移动函数  
    wifi = pywifi.PyWiFi()
    
    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(top, text="Taskmgr", width=w_box, height=h_box,bg='white')
    pil_imag = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/NETCON.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.pack(side='left')
    title = tk.Label(top,justify='left',text='无线网络',font=('黑体', 16),bg='white')
    title.pack(side='left')
    tip = tk.Label(top,justify='left',text='''Handrilow XCW Netset
Copyright @ 2109-2022 XIAN China''',font=('黑体', 10),bg='white')
    tip.pack(side='left')
    

    def renew():
        root.destroy()
        main()
    def typerenew(_):
            renew()

    tip = tk.Label(input,justify='left',text='选择并输入密码>',font=('黑体', 12),bg='white')
    tip.pack(side='left')
    entry = tk.Entry(input,bd=0,bg='#C4C4C4',fg='black')
    entry.pack(side='left')
    
    def getpswd():
        pswd = entry.get()
        return pswd
    
    def printList():
        a = theLB.get(theLB.curselection())
        cpk.unpathfilewrite("wifinameinfo,psw","w",a)
        cpk.unpathfilewrite("toptipMessage.message","w","准备连接到"+a)
    def printListeed(_):
        printList()
    
    def connect(_):
        cpk.unpathfilewrite("toptipMessage.message","w","正在连接...")
        with open("wifinameinfo,psw","r") as f:
            data = f.read()
        passwd = getpswd()
        #root.destroy()
        netcon.connect(data,passwd)
        
        
    entry.bind('<Return>',connect)
    
    def show_id():
        iface = wifi.interfaces()[0]
        iface.scan()
        result=iface.scan_results()
        num = len(wifi.interfaces())
        if num == 0:
            None
        else:
            def selectbg():
                with open("selectbg.psw","r") as fp:
                    bg = fp.read()
                theLB.config(selectbackground=bg)
                theLB.after(1000,selectbg)
            theLB = tk.Listbox(root,bd=0, bg='#F3F2F2', exportselection=True, fg='black', highlightcolor=A4, width=25, height=20,
                            selectforeground=A4, font=('等线',11), highlightbackground=A4,
                            selectmod="browse")
            theLB.place(x=20,y=80)
            selectbg()
            theLB.delete(0, END)
            for i in result:
                theLB.insert("end", i.ssid.encode('raw_unicode_escape').decode('utf-8'))
            theLB.bind('<Button-1>', printListeed)
            theLB.bind('<Return>', printListeed)
    show_id()
#菜单项对应图标
    test = tk.Button(m3,text='检测刷新',bd=0,bg='white',font=('黑体', 12),height=2,command=renew)
    test.pack(side='left',pady=3,padx=3)
    discon = tk.Button(m3,text='断开连接',bd=0,bg='white',font=('黑体', 12),height=2)
    discon.pack(side='left',pady=3,padx=3)
    connect = tk.Button(m3,text='网络检测',bd=0,bg='white',font=('黑体', 12),height=2)
    connect.pack(side='left',pady=3,padx=3)
    help = tk.Button(m3,text='帮助',bd=0,bg='white',font=('黑体', 12),height=2)
    help.pack(side='left',pady=3,padx=3)

    te = tk.Button(right_mode,anchor="nw",text='相关设置',bd=0,bg='white',fg='grey',font=('黑体', 15),height=1,width=12)
    te.pack(side='top',pady=0,padx=3)
    test1 = tk.Button(right_mode,anchor="nw",text='硬件属性',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    test1.pack(side='top',pady=1,padx=3)
    discon1 = tk.Button(right_mode,anchor="nw",text='管理已知网络',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    discon1.pack(side='top',pady=1,padx=3)
    connect1 = tk.Button(right_mode,anchor="nw",text='更改高级共享',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    connect1.pack(side='top',pady=1,padx=3)
    help1 = tk.Button(right_mode,anchor="nw",text='随机硬件地址',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    help1.pack(side='top',pady=1,padx=3)
    help2 = tk.Button(right_mode,anchor="nw",text='Handrilow防火墙',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    help2.pack(side='top',pady=1,padx=3)
    help3 = tk.Button(right_mode,anchor="nw",text='获得反馈',bd=0,bg='white',fg='#4E6EF2',font=('黑体', 10),height=1,width=15)
    help3.pack(side='top',pady=1,padx=3)

    root.mainloop()

