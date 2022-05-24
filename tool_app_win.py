#Handrilsoft
#About a tool of DIY selfapp
#v1.0
from shutil import *
import os , shutil
import tkinter as tk
from tkinter import ttk
from HandrilowOSLauncherCode.openHandrilow import set_path
from HandrilowOSLauncherCode import cpupack as cpk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter

fath_path = set_path.pwd()
print(fath_path)

def main():
    cpk.unpathfilewrite("toptip.message", "w", "务司坊")
    root = tk.Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root['background'] = '#F0F0F0'
    root.config(cursor='circle')
    x = sw*(1/10)
    y = 50
    root.geometry('+%d+%d' % (x,y))
    root.wm_attributes("-topmost", True)
    root.overrideredirect(True)
    
    f1 = tk.Frame(root)
    f1.pack(side='left',pady=5)
    f0 = tk.Frame(f1)
    f0.pack()
    f11 = tk.Frame(f1)
    f11.pack()
    f2 = tk.Frame(f1)
    f2.pack()
    f3 = tk.Frame(f1)
    f3.pack()
    f4 = tk.Frame(f1)
    f4.pack()
    f5 = tk.Frame(f1)
    f5.pack()
    f6 = tk.Frame(root)
    f6.pack(side='bottom')
    f_show = tk.Frame(root,width=160,height=90)
    f_show.pack(side='left',padx=5,pady=5)

    ##基本元素展示窗口
    sys_topio = tk.Label(f_show,width=500,height=10,bg='#DCDCDC',font=(None,1))
    sys_topio.pack(side='top')
    logo = tk.Label(sys_topio,width=20,height=9,bg='#BEBEBE',font=(None,1))
    logo.place(x=0,y=0)
    title = tk.Label(sys_topio,width=100,height=9,bg='#BEBEBE',font=(None,1))
    title.place(x=30,y=0)
    window = tk.Label(f_show,width=500,height=100,bg='#DCDCDC',font=(None,1))
    window.pack(side='top',pady=2)
    hig = tk.Label(window,width=2,height=50,bg='#DCDCDC',fg='black',font=(None,1))
    hig.place(x=0,y=50)
    wid = tk.Label(window,width=100,height=1,bg='#DCDCDC',fg='black',font=(None,1))
    wid.place(x=0,y=0)
    ti = tk.Label(window,text=':-)  这是窗口样例',bg='#DCDCDC',fg='black',font=('等线',13))
    ti.place(x=5,y=15)
    bottomtype = tk.Canvas(f_show,width=200,height=5,bg='#DCDCDC')
    bottomtype.pack(side='bottom',pady=1)
    
    def makapp_main():
        appname = apna.get()
        savefile = fath_path + "/" + appname + "/" #建立应用文件夹
        os.mkdir(savefile)
        appclass = comboxlist.get()
        filepath = fath_path + "/HandrilowOSLauncherCode/openHandrilow/" + appclass + ".pyw"#获取模板文件
        app_filepath = fath_path + "/"+ appname + "/" + appclass + ".pyw"#获取模板文件
        copy(filepath,savefile)
        filepathio = fath_path + "/HandrilowOSLauncherCode/openHandrilow/sys_topio.py"#获取模板文件
        app_filepathio = fath_path + "/"+ appname + "/sys_topio.py"#获取模板文件
        copy(filepathio,app_filepathio)
        filepathint = fath_path + "/HandrilowOSLauncherCode/openHandrilow/__init__.py"#获取模板文件
        app_filepathint = fath_path + "/"+ appname + "/__init__.py"#获取模板文件
        copy(filepathint,app_filepathint)
        app_filepathico = fath_path + "/"+ appname +"/H_icon"
        os.mkdir(app_filepathico)
        #copy(savefile2,filepath)
        appfile = fath_path + "/" + appname + "/"+ appname + ".pyw"
        os.rename(app_filepath,appfile)
        #os.remove(savefile + "/" +  appclass + ".py")#删除模板文件
        wid = winwid.get()
        win_hig = winhig.get()
        win_bg = winbg.get()
        cpk.unpathfilewrite(savefile + "title.cfg", "w", appname)
        cpk.unpathfilewrite(savefile + "wid.cfg", "w", wid)
        cpk.unpathfilewrite(savefile + "win_hig.cfg", "w", win_hig)
        cpk.unpathfilewrite(savefile + "win_bg.cfg", "w", win_bg)
        iconpath = filedialog.askopenfilename(title='选择应用图标')
        savepath = app_filepathico + "/LOGOALL.png"
        copy(iconpath, savepath)

    def makapp_simple():#最简单样式
        makapp_main()
        root.destroy()
        cpk.message('提示','应用创建完成')
        
    def makapp_welcom():#欢迎界面
        makapp_main()
        appname = apna.get()
        app_filepathico = fath_path + "/"+ appname +"/H_icon"
        iconpath = filedialog.askopenfilename(title='选择背景图片')
        savepath = app_filepathico + "/BG.png"
        copy(iconpath, savepath)
        root.destroy()
        cpk.message('提示','应用创建完成')

    def makapp_welcom_import():#欢迎界面调用模板
        makapp_main()
        appname = apna.get()
        app_filepathico = fath_path + "/"+ appname +"/H_icon"
        iconpath = filedialog.askopenfilename(title='选择背景图片')
        savepath = app_filepathico + "/BG.png"
        copy(iconpath, savepath)
        root.destroy()
        cpk.message('提示','应用创建完成')

    

    tk.Label(f0, text='应用图标',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter1(_):
        def leave1(_):
            logo.config(bg='#BEBEBE')
        logo.config(bg='#778899')
        apnaico.bind('<Leave>',leave1)
    apnaico = tk.Entry(f0,cursor='circle',bd=0)
    apnaico.pack(side='left',padx=3,pady=3)
    apnaico.bind('<Enter>',enter1)
    
    
    new_pwd_confirm = tk.StringVar()
    tk.Label(f11, text='应用名称',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter2(_):
        def leave2(_):
            title.config(bg='#BEBEBE')
        title.config(bg='#778899')
        apna.bind('<Leave>',leave2)
    apna = tk.Entry(f11, textvariable=new_pwd_confirm,bd=0)
    apna.pack(side='left',padx=3,pady=3)
    apna.bind('<Enter>',enter2)
    
    new_pwd_confirm1 = tk.StringVar()
    tk.Label(f2, text='窗口宽度',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter3(_):
        def leave3(_):
            wid.config(bg='#DCDCDC')
        wid.config(bg='#778899')
        winwid.bind('<Leave>',leave3)
    winwid = tk.Entry(f2, textvariable=new_pwd_confirm1,bd=0)
    winwid.pack(side='left',padx=3,pady=3)
    winwid.bind('<Enter>',enter3)

    new_pwd_confirm2 = tk.StringVar()
    tk.Label(f3, text='窗口高度',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter4(_):
        def leave4(_):
            hig.config(bg='#DCDCDC')
        hig.config(bg='#778899')
        winhig.bind('<Leave>',leave4)
    winhig = tk.Entry(f3, textvariable=new_pwd_confirm2,bd=0)
    winhig.pack(side='left',padx=3,pady=3)
    winhig.bind('<Enter>',enter4)

    new_pwd_confirm3 = tk.StringVar()
    tk.Label(f4, text='背景颜色',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter5(_):
        def leave5(_):
            window.config(bg='#DCDCDC')
            ti1 = tk.Label(window,text=':-)  这是窗口样例',bg='#DCDCDC',fg='black',font=('等线',13))
            ti1.place(x=5,y=15)
        window.config(bg='#778899')
        winbg.bind('<Leave>',leave5)
    winbg = tk.Entry(f4, textvariable=new_pwd_confirm3,bd=0)
    winbg.pack(side='left',padx=3,pady=3)
    winbg.bind('<Enter>',enter5)

    gochange = tk.Label(f5,text='选择类型',bd=0,bg='#778899',fg='white')
    gochange.pack(side='left',padx=3,pady=3)
    comev = tk.StringVar()
    comboxlist=ttk.Combobox(f5,textvariable=comev) #初始化
    comboxlist.insert(0, '应用类型')
    applyclass = ['appMode_simple','appMode_welcome','appMode_welcome_import']
    comboxlist["values"]=applyclass
    def makeapp(_):
        classes = comboxlist.get()
        if classes == 'appMode_simple':
            makapp_simple()
        if classes == 'appMode_welcome':
            makapp_welcom()
        if classes == 'appMode_welcome_import':
            makapp_welcom()
    comboxlist.bind("<<ComboboxSelected>>",makeapp)
    comboxlist.pack(side='left',padx=3,pady=3)

    def jump2(_):
            cpk.unpathfilewrite("toptip.message", "w", " ")
            root.destroy()
    bottomtype = tk.Canvas(f1,width=100,height=5,bg='grey')
    bottomtype.pack(side='bottom',pady=4)
    bottomtype.bind('<Leave>',jump2)

    w_box = 60
    h_box = w_box
    def resize12(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image12.resize((width, height), Image.ANTIALIAS)
    win1112 = tk.Label(f1, text="Taskmgr", width=w_box,
                       height=h_box)
    pil_image12 = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/APPMK.png')
    w, h = pil_image12.size
    pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)
    tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
    win1112.config(image=tk_image12)
    win1112.pack(side='bottom', padx=5, pady=3)
    
    root.mainloop()
