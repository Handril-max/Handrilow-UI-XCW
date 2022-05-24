#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture
#HandrilFunctionServices
#Handril desklist
# -*- coding:utf-8 -*-
import tkinter as tk
from HandrilowOSLauncherCode import linker
import os , shutil
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import HMmenu
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import windoweng 
from HandrilowOSLauncherCode import progressbar as pgb
from HandrilowOSLauncherCode import diskpart as fo
from HandrilowOSLauncherCode import colorlib as hcol

def main():
    with open("desklist.psw","r") as f:
        data2 = f.read()
    usenamefile = data2
    if usenamefile == 'started':
        print('20201028')
    elif usenamefile == 'None':
        pass
#post set
    
    root = tk.Toplevel()
    root.wm_attributes("-topmost", True)
    A4 = 'white'
    root['background']= A4
    #root.attributes('-transparentcolor',A4)
    root.attributes('-alpha',0.9)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    if 800 <= sw <= 1366:
        x = round(sw*(1100/1366))
    elif 1366 < sw <= 1920:
        x = round(sw*(1150/1366))
    else:
        None
    if 800 <= sw <= 1366:
        shd = round(sh*(27/768))
    elif 1366 < sw <= 1920:
        shd = round(sh*(22/768))
    else:
        None
    path = './HandrilowOSLauncherCode/UserFile'
    filenames = os.listdir(path)

    def quite():
        pgb.exite()
        cpk.unpathfilewrite("desklist.psw","w","None")
        root.destroy()
    #小白条
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)
    def jump2(_):
        cpk.mwoutto(bottomtype,'bottom',0,0,3)
        quite()
    bottomtype = tk.Label(root,image=photo,bd=0,width=150,height=5)
    bottomtype.bind('<Leave>',jump2)
    cpk.mwinto(bottomtype,'bottom',0,0,3)
    
    f1 = tk.Frame(root,bg=A4)
    f1.pack(side='bottom')
    f2 = tk.Frame(root,bg=A4)
    f2.pack(side='bottom')
    root.geometry('+%d+%d' %(x,shd+5))
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)

    #窗口移动函数
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None
    def on_move(event):
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
    root.bind('<B1-Motion>', on_move)


    name2 = tk.Label(f2, text="文件匣 @ Userfile", bg=A4,fg='#4D4D4D',font=('华文细黑',10,"bold"),height=1,bd=0)
    name2.pack(side='left',pady=5)
    
    def selectbg():
        with open("selectbg.psw","r") as fp:
            bg = fp.read()
        theLB.config(selectbackground=bg)
        theLB.after(1000,selectbg)
    theLB = tk.Listbox(root,bd=0,bg=A4,exportselection=True,fg='black',highlightcolor=A4,width=25,height=20,
                   selectforeground=A4,font=('华文细黑',10,"bold"),highlightbackground=A4,
                       selectmod="browse")
    theLB.pack(side='top',pady=15,padx=5)
    selectbg()

    
    def exite():
        cpk.unpathfilewrite("desklist.psw","w","None")
        root.destroy()
        cpk.unpathfilewrite("desklist.psw","w","started")
        main()

#新建文件夹
    def inputname_dir():
        def mkdir():
            b = command_input.get()
            os.mkdir(path+'/'+b)
            pgb.exite()
            exite()
        def makedir(_):
            mkdir()
        command_input=tk.Entry(f1,fg='black',bg='#DCDCDC',insertbackground='black',selectforeground='white',font=('华文细黑',10)
                               ,selectbackground='white',relief='flat',width=25)
        command_input.bind('<Return>',makedir)
        command_input.pack(side='left',pady=1)
        command_input.insert('insert','输入以创建')
        pgb.main()
    
#新建文件
    def inputname_file():
        def mkdir():
            b = command_input.get()
            target = path+'/'+b
            cpk.pathfilewrite(target,'w')
            pgb.exite()
            exite()
        def makedir(_):
            mkdir()
        command_input=tk.Entry(f1,fg='black',bg='#DCDCDC',insertbackground='black',selectforeground='white',font=('华文细黑',10)
                               ,selectbackground='white',relief='flat',width=25)
        command_input.bind('<Return>',makedir)
        command_input.pack(side='left',pady=1)
        command_input.insert('insert','输入以创建')
        pgb.main()
        
    for item in filenames:
        theLB.insert("end", item)
    def deleat():
        a = theLB.get(theLB.curselection())
        b = theLB.delete("active")
        target = path +'/'+ a
        fo.delete(target)
        exite()
        
    menubar = tk.Menu(root)
    menu = tk.Menu(root,tearoff = 0)
    menu.add_command(label='新建文件夹',command=inputname_dir)
    menu.add_command(label='新建单一文件',command=inputname_file)
    menu.add_command(label='复制')
    menu.add_command(label='剪切')
    menu.add_command(label='粘贴')
    menu.add_command(label='压缩到')
    menu.add_command(label='打开方式')
    menu.add_command(label='删除',command=deleat)
    menu.add_command(label='刷新',command=exite)
    #menu.add_separator()
    def popumenua(event):
        menu.post(event.x_root,event.y_root)

    def printList(event):
        a = theLB.get(theLB.curselection())
        if a=="":
            None
        elif os.isfile(a.replace('"','')) or os.isfile(os.getcwd()+a.replace('"','')) or os.isfile(a.replace('"','')+'.exe') or os.isfile(os.getcwd()+a.replace('"','')+'.exe') or os.isdir('dir '+os.getcwd()):#如果是个文件
            try:
                os.startfile(a.replace('"',''))
            except:
                try:
                    os.startfile(os.getcwd()+a.replace('"',''))
                except:
                    try:
                        os.startfile(a.replace('"','')+'.exe')
                    except:
                        try:
                            os.startfile(os.getcwd()+a.replace('"','')+'.exe')
                        except:
                            os.startfile('dir '+os.getcwd())
        
    theLB.bind('<Button-3>',popumenua)
    theLB.bind('<Double-Button-1>', printList)
    theLB.bind('<Return>', printList)

#菜单项对应图标
    A5=  A4
    w_box = 60
    h_box = w_box
    def resize12(w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_image12.resize((width, height), Image.ANTIALIAS)
    win1112 = tk.Label(f1,text="Taskmgr",width=w_box, height=h_box,bg=A5)
    pil_image12 = Image.open('./HandrilowOSLauncherCode/H_icon/SHELL.png') 
    w, h = pil_image12.size  
    pil_image_resized12 = resize12(w, h, w_box, h_box, pil_image12)  
    tk_image12 = ImageTk.PhotoImage(pil_image_resized12)
    win1112.config(image=tk_image12) 
    win1112.pack(side='bottom',padx=5,pady=1)
    root.mainloop()
#main()
