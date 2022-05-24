# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# main
# Handril PC screen
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import shutil
import string
import glob
import webbrowser
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import *
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from shutil import *
import gc
import win32gui
import multiprocessing
from tkwebview2.tkwebview2 import WebView2
from TkinterDnD2 import *
from HandrilowOSLauncherCode import windoweng as weg
from HandrilowOSLauncherCode import scound, for_web
from HandrilowOSLauncherCode import colorlib
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import threadpool as thdpol
from HandrilowOSLauncherCode import note_desk as notd
from HandrilowOSLauncherCode import consult
from HandrilowOSLauncherCode import colorselect
from HandrilowOSLauncherCode import partprtsc
from HandrilowOSLauncherCode import picfiledialog as pflog
from HandrilowOSLauncherCode import desktopGrid
from HandrilowOSLauncherCode import memorymanger as mmg
from HandrilowOSLauncherCode.openHandrilow import set_path
from HandrilowOSLauncherCode import topio
from HandrilowOSLauncherCode import H_list_all as hla
from HandrilowOSLauncherCode.openHandrilow import sys_win_cartoon as swc
from HandrilowOSLauncherCode import for_file
from . import H_bluetooth

fath_path = set_path.pwd()
desktop_path = fath_path + "/HandrilowOSLauncherCode/disk/allfile/desktop/"

def main():
    w_box = 30
    h_box = w_box

    def bg_and_base():
        cpk.unpathfilewrite("toptip.message", "w", " ")
        pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/desktop.pid"
        cpk.random(pids)

        dirs1 = fath_path + "/HandrilowOSLauncherCode/set"
        if os.path.exists(dirs1) == True:
            pass
        else:
            os.mkdir(dirs1)

        A2 = colorlib.cola2()
        A3 = colorlib.cola3()
        A4 = colorlib.cola4()
        A7 = A4
        A8 = colorlib.cola8()

        shd = 30
        root = TkinterDnD.Tk()
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        root.geometry("%dx%d+%d+%d" % (sw, sh, 0, 0))
        #cpk.fathersize(root, sw, sh, 0, 0)
        root['background'] = 'black'
#       root.attributes('-alpha',0.7)
        root.config(cursor='circle')
        root.overrideredirect(True)
        root.withdraw()
        root.grid_rowconfigure(1, weight=1, minsize=250)
        root.grid_columnconfigure(0, weight=1, minsize=300)
        m3 = tk.Frame(root)
        m3.place(x=0, y=0)
    # 电源条

        def deskmenu():
            def a():
                swc.intend_display(root, 1, 100, sw, sh, sw, sh)
                shutil.rmtree('./HandrilowOSLauncherCode/H_fileprocess')
                os.mkdir('./HandrilowOSLauncherCode/H_fileprocess')
                fd = win32gui.FindWindow("Shell_TrayWnd", None)
                win32gui.ShowWindow(fd, 5)
                root.destroy()
                exit()
            a()

        def exite(_):
            root.destroy()
            fp.exite(root, pids)
            input()
            # exit()

        huishou_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/HUISHOU.png")
        file_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/FILE.png")
        folder_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/FOLD.png")
        word_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/WORD.png")
        py_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PY.png")
        pic_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PIC.png")
        html_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/HTML.png")
        mic_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/MIC.png")
        ppt_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PPT.png")
        css_icon = PhotoImage(
            file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/CSS.png")

        def resize(image):
            #w, h = image.size
            w = image.width
            h = image.height
            img_wh = w/h
            if w > h:
                return image.resize((round(img_wh*int(sh)), round(int(sh))))
            elif w <= h:
                return image.resize((round(int(sw)), round(int(sw)/img_wh)))
        canvas = tk.Canvas(root, height=sh, width=sw, bd=0)
        canvas.config(highlightthickness=0)
        image = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
        # im=image.filter(ImageFilter.GaussianBlur(radius=20))
        re_image = resize(image)
        img = ImageTk.PhotoImage(re_image)
        canvas.create_image(sw/2, sh/2, anchor='center', image=img)

        canvas.config(highlightthickness=0)
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
        # im=image.filter(ImageFilter.GaussianBlur(radius=20))
        re_image = resize(image)
        img = ImageTk.PhotoImage(re_image)
        canvas.create_image(sw/2, sh/2, anchor='center', image=img)

        # store the filename associated with each canvas item in a dictionary
        canvas.filenames = {}
        # store the next icon's x and y coordinates in a list
        canvas.nextcoords = [75, 50]
        # add a boolean flag to the canvas which can be used to disable
        # files from the canvas being dropped on the canvas again
        canvas.dragging = False

        def add_file(filename):
            print(filename)
            icon = file_icon
            file2, type2 = os.path.splitext(filename)
            if os.path.basename(filename) == '回收站':
                icon = huishou_icon
            elif os.path.isdir(filename):
                icon = folder_icon
            elif type2 == '.doc' or type2 == '.docx':
                icon = word_icon
            elif type2 == '.py' or type2 == '.PY':
                icon = py_icon
            elif type2 == '.png' or type2 == '.jpg' or type2 == '.jpeg' or type2 == '.gif':
                icon = pic_icon
            elif type2 == '.pptx':
                icon = ppt_icon
            elif type2 == '.mp3' or type2 == '.wav':
                icon = mic_icon
            elif type2 == '.html':
                icon = html_icon
            elif type2 == '.css':
                icon = css_icon

            id1 = canvas.create_image(canvas.nextcoords[0], canvas.nextcoords[1],
                                      image=icon, anchor='n', tags=('file',))
            id2 = canvas.create_text(canvas.nextcoords[0], canvas.nextcoords[1] + 48,
                                     text=os.path.basename(filename), anchor='n',
                                     justify='center', width=90, fill='white')

            def select_item(ev):  # 选中的文件
                select_file = canvas.filenames[id2]
                os.startfile(select_file)
                canvas.select_from(id2, 0)
                canvas.select_to(id2, 'end')
                
            gridmenu = tk.Menu(root, tearoff=0)
            gridmenu.add_command(label='打开')
            gridmenu.add_command(label='复制')
            gridmenu.add_command(label='剪切')
            gridmenu.add_command(label='打开所在位置')
            gridmenu.add_command(label='删除')
            gridmenu.add_command(label='文件属性')
            def select_menu(event):
                gridmenu.post(event.x_root, event.y_root)
            canvas.tag_bind(id1, '<Double-Button-1>', select_item)
            canvas.tag_bind(id1, '<Button-3>', select_menu)
            canvas.tag_bind(id2, '<Double-Button-1>', select_item)
            canvas.filenames[id1] = filename
            canvas.filenames[id2] = filename
            if canvas.nextcoords[0] > sw-150:
                canvas.nextcoords = [75, canvas.nextcoords[1] + 80]
            else:
                canvas.nextcoords = [
                    canvas.nextcoords[0] + 100, canvas.nextcoords[1]]

        # drop methods

        def drop_enter(event):
            event.widget.focus_force()
            print('Entering %s' % event.widget)
            return event.action

        def drop_position(event):
            return event.action

        def drop_leave(event):
            print('Leaving %s' % event.widget)
            return event.action

        def drop(event):
            if canvas.dragging:
                # the canvas itself is the drag source
                return REFUSE_DROP
            if event.data:
                files = canvas.tk.splitlist(event.data)
                for f in files:
                    add_file(f)
            return event.action

        canvas.drop_target_register(DND_FILES)
        canvas.dnd_bind('<<DropEnter>>', drop_enter)
        canvas.dnd_bind('<<DropPosition>>', drop_position)
        canvas.dnd_bind('<<DropLeave>>', drop_leave)
        canvas.dnd_bind('<<Drop>>', drop)
        def filedesk():
            for file in os.listdir(desktop_path):
                add_file(desktop_path + file)
        filedesk()

        # drag methods

        def drag_init(event):
            data = ()
            sel = canvas.select_item()
            if sel:
                # in a decent application we should check here if the mouse
                # actually hit an item, but for now we will stick with this
                data = (canvas.filenames[sel],)
                canvas.dragging = True
                return ((ASK, COPY), (DND_FILES, DND_TEXT), data)
            else:
                # don't start a dnd-operation when nothing is selected; the
                # return "break" here is only cosmetical, return "foobar" would
                # probably do the same
                return 'break'

        def drag_end(event):
            # reset the "dragging" flag to enable drops again
            canvas.dragging = False

        canvas.drag_source_register(1, DND_FILES)
        canvas.dnd_bind('<<DragInitCmd>>', drag_init)
        canvas.dnd_bind('<<DragEndCmd>>', drag_end)

        root.update_idletasks()
        root.deiconify()
        canvas.grid(row=1, column=0, padx=5, pady=10, sticky='news')
        canvas.place(x=0, y=0)
        cpk.graduallyin(canvas, root, 0, 0)
        path = tk.StringVar()

        def show_image(path):
            global img
            image = Image.open(path)
            re_image = resize(image)
            # im=image.filter(ImageFilter.GaussianBlur(radius=20))
            img = ImageTk.PhotoImage(re_image)
            canvas.create_image(sw/2, sh/2, anchor='center', image=img)
            for file in os.listdir(desktop_path):
                add_file(desktop_path + file)
            renew()

        def openpicture():
            # 打开一张图片并显示
            global fileindex, fatherpath, files, file_num

            # with open("picpath.path", "r", encoding='utf-8') as f:
            #filepath = f.read()
            filepath = filedialog.askopenfilename()
            savepath = fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png'
            copy(filepath, savepath)
            show_image(savepath)

        def openpicture_midle():
            def changebg(_):
                openpicture()
                leftchance1.destroy()

            def changebg_close(_):
                leftchance1.destroy()

            leftchance1 = tk.Label(root)
            leftchance1.pack(side='bottom')

            def enter_file(_):
                name.config(bg='#C0C0C0')

            def leave_file(_):
                name.config(bg=A4)

            def resiz(w, h, w_box, h_box, pil_image):
                f1 = 1.0*w_box/w
                f2 = 1.0*h_box/h
                factor = min([f1, f2])
                width = int(w*factor)
                height = int(h*factor)
                return pil_imag.resize((width, height), Image.ANTIALIAS)
            name = tk.Label(leftchance1, text="Taskmgr",
                            width=w_box, height=h_box, bg=A4)
            pil_imag = Image.open(
                './HandrilowOSLauncherCode/H_icon/picsfl_change.png')
            w, h = pil_imag.size
            pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
            tk_imag = ImageTk.PhotoImage(pil_image_resize)
            name.config(image=tk_imag)
            name.pack(side='left', padx=2, pady=1)
            name.bind('<Button-1>', changebg)
            name.bind('<Enter>', enter_file)
            name.bind('<Leave>', leave_file)

            def enter_file1(_):
                name1.config(bg='#C0C0C0')

            def leave_file1(_):
                name1.config(bg=A4)

            def resiz1(w, h, w_box, h_box, pil_image):
                f1 = 1.0*w_box/w
                f2 = 1.0*h_box/h
                factor = min([f1, f2])
                width = int(w*factor)
                height = int(h*factor)
                return pil_imag1.resize((width, height), Image.ANTIALIAS)
            name1 = tk.Label(leftchance1, text="Taskmgr",
                             width=w_box, height=h_box, bg=A4)
            
            pil_imag1 = Image.open('./HandrilowOSLauncherCode/H_icon/BACK.png')
            w, h = pil_imag1.size
            pil_image_resize1 = resiz1(w, h, w_box, h_box, pil_imag1)
            tk_imag1 = ImageTk.PhotoImage(pil_image_resize1)
            name1.config(image=tk_imag1)
            name1.pack(side='left', padx=2, pady=1)
            name1.bind('<Button-1>', changebg_close)
            name1.bind('<Enter>', enter_file1)
            name1.bind('<Leave>', leave_file1)

            name3 = tk.Label(leftchance1, bg='#F0F0F0',
                             fg='black', font=('等线', 12), bd=0)
            name3.pack(side='top', padx=5)
            name3.config(text="选择完成后/n点击对号以更换壁纸")
            pflog.dialog()

        def keybgc(_):
            openpicture()
        root.bind('<Control-F5>', keybgc)

        def relock():
            root.destroy()
            shutil.rmtree('./HandrilowOSLauncherCode/H_fileprocess')
            os.mkdir('./HandrilowOSLauncherCode/H_fileprocess')

        def renew():
            relock()
            main()
        root.bind('<F5>', renew)

        def notelist():
            thdpol.dissetp.thd(notd.main)
        

        def lockscreen():
            # cpk.prtscother()#截图
            cpk.lockpart()

        def tolock():
            lockscreen()

        def midlock(_):
            tolock()

        root.bind_all('<Control-l>', midlock)
        root.bind_all('<Control-L>', midlock)
        menubar = tk.Menu(root)
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label='刷新', command=renew)
        wmenu = tk.Menu(menubar, tearoff=0)
        wmenu.add_command(label='图标整理')
        wmenu.add_command(label='闲置管理')
        wmenu.add_command(label='复制')
        wmenu.add_command(label='移动')
        wmenu.add_command(label='粘贴')
        def makefold():
            os.mkdir(desktop_path + "111")
            renew()
        wmenu.add_command(label='新建文件',command=makefold)
        menu.add_cascade(label='更多', menu=wmenu)
        menu.add_separator()

        amenu = tk.Menu(menubar, tearoff=0)

        def light():
            cpk.unpathfilewrite("black_bg.psw", "w", "0")
            filepath = fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG-1.png'
            fatherpath = os.path.dirname(filepath)
            filename = os.path.basename(filepath)
            files = os.listdir(fatherpath)
            file_num = len(files)
            fileindex = files.index(filename)
            show_image(filepath)

        menu.add_separator()
        xmenu = tk.Menu(menubar, tearoff=0)

        def bgc():
            openpicture()

        def menory(_):
            mmg.main()
        xmenu.add_command(label='选择  Ctrl+F5', command=bgc)
        menu.add_cascade(label='壁纸设置', menu=xmenu)
        ymenu = tk.Menu(menubar, tearoff=0)
        ymenu.add_command(label='便签', command=notelist)
        menu.add_cascade(label='微组件', menu=ymenu)
        menu.add_separator()
        root.bind_all('<Control-Shift-m>', menory)
        root.bind_all('<Control-Shift-M>', menory)

        def teminter():
            cpk.pathfilewrite(
                fath_path + '/HandrilowOSLauncherCode/H_fileprocess/outfreetype.pid', 'w')
            cpk.order()

        def teminterquick(_):
            teminter()
        root.bind_all('<Control-r>', teminterquick)
        root.bind_all('<Control-R>', teminterquick)
        menu.add_command(label='关闭', command=deskmenu)

        def popumenua(event):
            fileexists = os.path.exists(
                fath_path + "/HandrilowOSLauncherCode/set/lockscreen.set")
            if fileexists == True:
                None
            else:
                menu.post(event.x_root, event.y_root)
                cpk.unpathfilewrite("postx.psw", "w", str(event.x_root))
                cpk.unpathfilewrite("posty.psw", "w", str(event.y_root))
                # print(event.x_root,event.y_root)
        root.bind('<Button-3>', popumenua)

        def random_x(event):
            cpk.unpathfilewrite("postx.psw", "w", str(event.x_root))
        root.bind_all('<Motion>', random_x)

        def Xpostmark(event):  # 鼠标坐标器X
            x = event.x_root
            return x

        def Ypostmark(event):  # 鼠标坐标器Y
            y = event.y_root
            return y

        def mousepost(event):  # 鼠标测试接口
            x = event.x_root
            y = event.y_root
            xy = 'x:'+str(x)+'y:'+str(y)
            cpk.unpathfilewrite("toptip.message", "w", xy)
        # root.bind('<Motion>',mousepost)#鼠标测试接口

        def deskmenukey(_):
            deskmenu()
        root.bind_all('<Control-h>', deskmenukey)
        root.bind_all('<Control-H>', deskmenukey)
        root.bind_all('<Triple-Button-3>', deskmenukey)

        def prtsc(_):
            fileexists = os.path.exists(
                fath_path + "/HandrilowOSLauncherCode/set/lockscreen.set")
            if fileexists == True:
                None
            else:
                cpk.printscreen()
        root.bind_all('<Control-s>', prtsc)
        root.bind_all('<Control-S>', prtsc)

        def midwin(_):
            cpk.pathfilewrite(
                fath_path + "/HandrilowOSLauncherCode/H_fileprocess/slipsearch.pid", "w")
            cpk.midpasswin()
        # root.bind('<B1-Motion>',midwin)
        # root.bind('<MouseWheel>',midwin)
        root.bind('<Alt-s>', midwin)
        root.bind('<Alt-S>', midwin)

        def reload(_):
            None
        root.bind_all('<F5>', reload)

        def colorset(_):
            colorselect.asapp()
        root.bind_all('<Alt-e>', colorset)
        root.bind_all('<Alt-E>', colorset)

        def order(_):
            cpk.deskDockMode(root, fath_path +
                             '/HandrilowOSLauncherCode/H_icon/SHELL.png')
            consult.main()
        root.bind_all('<Control-e>', order)
        root.bind_all('<Control-E>', order)

        def listpid(_):
            hla.main()
        root.bind_all('<Alt-e>', listpid)
        root.bind_all('<Alt-E>', listpid)

        def picview(_):
            pflog.main()
        root.bind_all('<Control-p>', picview)
        root.bind_all('<Control-P>', picview)

        def playsound(_):
            pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/lindesearch.pid"

            fileexists = os.path.exists(pids)
            if fileexists == True:
                cpk.unpathfilewrite(
                    "toptipMessage.message", "w", "Linde Music|Close the search and watch the list again")
                cpk.message('Linde Music', 'Note the right place')
            elif fileexists == False:
                cpk.unpathfilewrite("toptip.message", "w",
                                    "Linde Music|Loading...")
                scound.playsoundmode()
        root.bind('<Alt-m>', playsound)
        root.bind('<Alt-M>', playsound)

        def to_bluetooth(_):
            thdpol.dissetp.thd2(H_bluetooth.main())
        root.bind('<Alt-b>', to_bluetooth)
        root.bind('<Alt-B>', to_bluetooth)

        def searchsound(_):
            pids = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/linde.pid"
            pidt = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/lindesearch.pid"

            fileexists = os.path.exists(pids)
            if fileexists == True:
                cpk.unpathfilewrite(
                    "toptipMessage.message", "w", "Linde Music|Close the list and search again")
                cpk.message('Linde Music', 'Note the right place')
            elif fileexists == False:
                cpk.sys(pidt)
                cpk.unpathfilewrite("toptip.message", "w",
                                    "Linde Music|search|Handrilsoft")
                cpk.MusicSearchWindow(root)
        root.bind('<Alt-Shift-m>', searchsound)
        root.bind('<Alt-Shift-M>', searchsound)

        def toweb(_):
            for_file.main()
        root.bind_all('<Return>', toweb)

        ##############################

        def tipbar():
            def bar():
                cpk.mwoutto(bottomtype, 'bottom', 0, 5, 10)
            cpk.mwinto(bottomtype, 'bottom', 0, 5, 15)
            bar()

        def dock(_):
            print('on')
            # 进程操作标记文件：“1”为允许运行，“0”为禁止运行
            cpk.unpathfilewrite("all_progress.psw", "w", "0")
            tipbar()
        bottomtype = tk.Canvas(root)
        bottomtype.config(width=round(sw/3), height=4)
        # bottomtype.bind('<Enter>',dock)
        cpk.mwinto(bottomtype, 'bottom', 0, 0, 5)
        ##############################
        def funct(_):
            def bar():
                cpk.mwoutto(bottomtype, 'bottom', 0, 5, 10)
                #canvas.config(width=sw, height=sh)
                bottomtype['state']=NORMAL
            bottomtype['state']=DISABLED
            #canvas.config(width=sw/2, height=sh/2)
            cpk.unpathfilewrite("all_progress.psw", "w", "0")
            cpk.mwinto(bottomtype, 'bottom', 0, 5, 15)
            bar()
        bottomtype.bind('<Leave>',funct)#移动
        root.bind_all('<Control-m>', dock)
        root.bind_all('<Control-M>', dock)

        def reallowlaunch(_):
            cpk.unpathfilewrite("all_progress.psw", "w", "1")
        root.bind('<Button-1>', reallowlaunch)
        # cpk.free()
        usenamefile = os.path.exists("usename.psw")
        if usenamefile == False:
            cpk.pathfilewrite("usename.psw", 'w')
            cpk.unpathfilewrite("usename.psw", "w", "HanBook")
        else:
            pass

        topio.main()

        root.mainloop()

    thdpol.dissetp.thd2(bg_and_base)
