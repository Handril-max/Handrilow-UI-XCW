import pygame , os , shutil , random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image , ImageFilter
from mutagen.mp3 import MP3
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import fileprocess as fp
from HandrilowOSLauncherCode.openHandrilow import set_path

fath_path = set_path.pwd()

pygame.mixer.init()
path = './HandrilowOSLauncherCode/disk/allfile/music'
pids = "./HandrilowOSLauncherCode/H_fileprocess/linde.pid"
pidt = "./HandrilowOSLauncherCode/H_fileprocess/lindesearch.pid"
A4 = '#F0F0F0'

def musicpath():
    path = './HandrilowOSLauncherCode/Musics/' 
    return path
def simplemain1(path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()

def mpause():
    pygame.mixer.pause()
def munpause():
    pygame.mixer.unpause()
        
def playsoundmode():
    root = tk.Toplevel()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    #wid = random.randint(500,700)
    wid = 600
    root['background'] = '#F0F0F0'
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.config(cursor='circle')
    #窗口移动函数
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
    root.bind('<B1-Motion>', on_move)

    w_box_re = 180
    h_box_re = 180
    
    def resize(w, h, w_box_re, h_box_re, pil_image_righttip):
        f1 = 1.0*w_box_re/w
        f2 = 1.0*h_box_re/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_righttip.resize((width, height), Image.ANTIALIAS)
    righttip = tk.Label(root, text="Taskmgr", width=w_box_re, height=h_box_re, bg='#F0F0F0')
    pil_image_righttip = Image.open(
        fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/MUSIC_BG.png')
    w, h = pil_image_righttip.size
    pil_image_resized_righttip = resize(w, h, w_box_re, h_box_re, pil_image_righttip)
    tk_image_righttip = ImageTk.PhotoImage(pil_image_resized_righttip)
    righttip.config(image=tk_image_righttip)
    righttip.place(x=400,y=20)
    
    def jump2():
        for h in range(1,10)[::-1]:
            i = h*(100/10)
            wc_wid = (wid/100)*i
            wc_hig = ((wid)/100)*i
            x = (((sw/i)*i)-wc_wid)/2
            y = (sh-wc_hig)/(i/50)
            root.geometry('%dx%d+%d+%d'%(wc_wid,wc_hig,x,y))
            root.update()
        cpk.unpathfilewrite("toptip.message", "w", "")
        fp.exitesys(m3,pids)
        pygame.mixer.stop()
        cpk.unpathfilewrite("toptip.message","w"," ")
        cpk.unpathfilewrite("suond.message","w", "暂无播放")
        root.destroy()
    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 5, 12)
        bottomtype.destroy()
        jump2()
    
    bottomtype = tk.Canvas(root,width=wid/3,height=5,bg='black')
    bottomtype.bind('<Leave>',jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 5)
    #root.bind('<Button-3>',maxwin)
    
    cpk.sys(pids)
    cpk.unpathfilewrite("toptip.message","w","麟德乐府 | 请选择您想播放的音频文件")
    def mpause():
        pygame.mixer.pause()
    def munpause():
        pygame.mixer.unpause()
    
    m3 = Frame(root,height=220, width=22)
    m3.pack(side='bottom',pady=15)

    m4 = Frame(m3,height=220, width=22)
    m4.pack(side='bottom',padx=5)

    def printList(_):
        a = theLB.get(theLB.curselection())
        cpk.unpathfilewrite("suond.message","w", a)
        cpk.unpathfilewrite("toptip.message","w","当前 | "+a)
        pygame.mixer.stop()
        playpath = path + '/' + a
        sound = pygame.mixer.Sound(playpath)
        sound.play()

    def deleat():
        a = theLB.get(theLB.curselection())
        b = theLB.delete("active")
        os.remove(path + '/' + a)
        for item in filenames:
            theLB.delete(0, END)
            theLB.insert("end", item)

    menubar = tk.Menu(m3)
    menu = tk.Menu(m3,tearoff = 0)
    menu.add_command(label='删除此音乐文件',command= deleat)
    menu.add_separator()
    def popumenua(event):
        menu.post(event.x_root,event.y_root)
    def selectbg():
        with open("selectbg.psw","r") as fp:
            bg = fp.read()
        theLB.config(selectbackground=bg)
        theLB.after(1000,selectbg)
    theLB = tk.Listbox(root,bd=0,bg='#F0F0F0',exportselection=True,fg='black',highlightcolor=A4,width=45,height=30,
                   selectforeground=A4,font=('等线',11),highlightbackground=A4,
                       selectmod="browse")
    theLB.place(x=20,y=20)
    selectbg()

    filenames = os.listdir(path)
    for item in filenames:
        theLB.insert("end", item)

    def renew(_):
        theLB.delete(0, END)
        theLB.insert("end", item)
            
    theLB.bind('<Button-3>',popumenua)
    theLB.bind('<Alt-n>',renew)
    theLB.bind('<Alt-N>',renew)
    theLB.bind('<Double-Button-1>', printList)
    theLB.bind('<Return>', printList)
    
    play = tk.Button(m4,bd=0,text="麟德乐府 |",font=("微软雅黑",15))
    play.pack(side='left')

    def enter_name(_):
        name.config(bg='#D3D3D3', fg='white')
    def leave_name(_):
        name.config(bg="#F0F0F0", fg='black')
    name = tk.Button(m4, text="Taskmgr",bd=0, width=25, height=25, bg="#F0F0F0")
    pil_imag = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/MUSIC.png')
    name.config(image=pil_imag)
    name.pack(side='left',padx=5)
    name.bind('<Enter>', enter_name)
    name.bind('<Leave>', leave_name)

    def enter_unname(_):
        unname.config(bg='#D3D3D3', fg='white')
    def leave_unname(_):
        unname.config(bg="#F0F0F0", fg='black')
    unname = tk.Button(m4, text="Taskmgr",bd=0, width=25, height=25, bg="#F0F0F0",command=mpause)
    pil_imag_unname = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/PLAY.png')
    unname.config(image=pil_imag_unname)
    unname.pack(side='left',padx=5)
    unname.bind('<Enter>', enter_unname)
    unname.bind('<Leave>', leave_unname)

    def enter_unname2(_):
        unname2.config(bg='#D3D3D3', fg='white')
    def leave_unname2(_):
        unname2.config(bg="#F0F0F0", fg='black')
    unname2 = tk.Button(m4, text="Taskmgr",bd=0, width=25, height=25, bg="#F0F0F0",command=munpause)
    pil_imag_unname2 = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/UNPLAY.png')
    unname2.config(image=pil_imag_unname2)
    unname2.pack(side='left',padx=5)
    unname2.bind('<Enter>', enter_unname2)
    unname2.bind('<Leave>', leave_unname2)

    def enter_menu(_):
        menu.config(bg='#D3D3D3', fg='white')
    def leave_menu(_):
        menu.config(bg="#F0F0F0", fg='black')
    menu = tk.Button(m4, text="Taskmgr",bd=0, width=25, height=25, bg="#F0F0F0")
    pil_imag_menu = tk.PhotoImage(file=fath_path + '/HandrilowOSLauncherCode/H_icon/MORE.png')
    menu.config(image=pil_imag_menu)
    menu.pack(side='left',padx=5)
    menu.bind('<Enter>', enter_menu)
    menu.bind('<Leave>', leave_menu)
    
    def sys_task_oper():#进程系统级别标记函数
        #print('sys_progress_pid')
        with open("all_progress.psw", "r", encoding='utf-8') as f:
            mark = f.read()
        if mark == "1":
            None
        elif mark == "0":
            jump2()
            cpk.unpathfilewrite("toptip.message", "w", "")
            cpk.unpathfilewrite("all_progress.psw", "w", "1")
            root.destroy()
        bottomtype.after(1000,sys_task_oper)
    sys_task_oper()
        
    for h in range(1,100):
        i = h*(100/100)
        root.wm_attributes("-alpha", i/70)
        wc_wid = wid
        wc_hig = wid
        x = (sw-wc_wid)/2
        y = (sh-wc_hig)/2
        root.geometry('%dx%d+%d+%d'%(wc_wid,wc_hig,x,y))
        root.update()
    
    
    root.mainloop()
    
