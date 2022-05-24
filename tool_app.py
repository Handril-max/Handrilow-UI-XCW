#Handrilsoft
#About a tool of DIY selfapp
#v1.0
from shutil import *
import os , shutil
import tkinter as tk
from tkinter import ttk
from HandrilowOSLauncherCode.openHandrilow import set_path
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import for_code
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter
import multiprocessing

fath_path = set_path.pwd()
print(fath_path)

def main():
    cpk.unpathfilewrite("toptip.message", "w", "务司坊")
    root = tk.Toplevel()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root['background'] = '#F0F0F0'
    root.config(cursor='circle')
    
    root.wm_attributes("-topmost", True)
    root.overrideredirect(True)
    def nonea():
        with open("selectbg.psw", "r") as fp:
            ebg = fp.read()
        return ebg
        f_top.after(1000, nonea)
    nonea()
    def on_move(event):
        root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
        width, height = None, None
        offset_x = event.x_root - root_x
        offset_y = event.y_root - root_y
        if width and height:
            geo_str = "%sx%s+%s+%s" % (width, height, abs_x + offset_x, abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
            root.geometry(geo_str)
        def _on_tap(event):
            root_x, root_y = event.x_root, event.y_root
            abs_x, abs_y = winfo_x(), winfo_y()
    #root.bind('<B1-Motion>', on_move)
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
    sys_topio = tk.Label(f_show,width=400,height=10,bg='#DCDCDC',font=(None,1))
    sys_topio.pack(side='top')
    logo = tk.Label(sys_topio,width=20,height=9,bg='#BEBEBE',font=(None,1))
    logo.place(x=0,y=0)
    title = tk.Label(sys_topio,width=100,height=9,bg='#BEBEBE',font=(None,1))
    title.place(x=30,y=0)
    window = tk.Label(f_show,width=400,height=105,bg='#DCDCDC',font=(None,1))
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
        savefile = fath_path + "/HandrilowOSLauncherCode/disk/allfile/backup/" + appname + "/" #建立应用文件夹
        os.mkdir(savefile)
        appclass = comboxlist.get()
        
        filepath = fath_path + "/HandrilowOSLauncherCode/openHandrilow/" + appclass + ".pyw"#获取模板文件
        app_filepath = fath_path + "/HandrilowOSLauncherCode/disk/allfile/backup/"+ appname + "/" + appname + ".pyw"#获取模板文件
        copy(filepath,app_filepath)
        multiprocessing.Process(target = for_code.main())
        
    

    def makapp_simple():#最简单样式
        makapp_main()
        root.destroy()
        cpk.message('提示','应用创建完成')

    

    tk.Label(f0, text='应用图标',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter1(_):
        def leave1(_):
            logo.config(bg='#BEBEBE')
        logo.config(bg=nonea())
        apnaico.bind('<Leave>',leave1)
    apnaico = tk.Label(f0,text='确定类型后选择图标',bg='white',font=('等线', 10),cursor='circle',bd=0,padx=13,pady=3)
    apnaico.pack(side='left',padx=3,pady=3)
    apnaico.bind('<Enter>',enter1)
    
    
    new_pwd_confirm = tk.StringVar()
    tk.Label(f11, text='应用名称',font=('等线', 10), bd=0).pack(side='left',padx=3,pady=3)
    def enter2(_):
        def leave2(_):
            title.config(bg='#BEBEBE')
        title.config(bg=nonea())
        apna.bind('<Leave>',leave2)
    apna = tk.Entry(f11, textvariable=new_pwd_confirm,bd=0)
    apna.pack(side='left',padx=3,pady=3)
    apna.bind('<Enter>',enter2)

    gochange = tk.Label(f5,text='选择类型',bd=0,bg='#778899',fg='white')
    gochange.pack(side='left',padx=3,pady=3)
    comev = tk.StringVar()
    comboxlist=ttk.Combobox(f5,textvariable=comev) #初始化
    comboxlist.insert(0, '应用类型')
    applyclass = ['appMode_simple']
    comboxlist["values"]=applyclass
    def makeapp(_):
        classes = comboxlist.get()
        if classes == 'appMode_simple':
            makapp_simple()
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

    for i in range(1,100):
        x = (sw*(2/3))
        y = round(((sh/100)*i)*(35/768))
        root.geometry('+%d+%d' % (x,y))
        root.update()
    root.mainloop()
