import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import progressbar as pgb
from HandrilowOSLauncherCode.openHandrilow import sys_win_cartoon as swc

def lin3(root):
    m2 = tk.Frame(root)
    m2.pack(side='top', padx=10, pady=1)

    colornam1 = '#2B4490'

    def get1():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam1)
    color1 = tk.Button(m2, text=colornam1, bg=colornam1,
                       fg=colornam1, height=2, width=7, bd=0, command=get1)
    color1.pack(side='left', padx=1)

    colornam2 = '#7F7522'

    def get2():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam2)
    color2 = tk.Button(m2, text=colornam2, bg=colornam2,
                       fg=colornam2, height=2, width=7, bd=0, command=get2)
    color2.pack(side='left', padx=1)

    colornam3 = '#FEDCBD'

    def get3():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam3)
    color3 = tk.Button(m2, text=colornam3, bg=colornam3,
                       fg=colornam3, height=2, width=7, bd=0, command=get3)
    color3.pack(side='left', padx=1)

    colornam4 = '#EF5B9C'

    def get4():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam4)
    color4 = tk.Button(m2, text=colornam4, bg=colornam4,
                       fg=colornam4, height=2, width=7, bd=0, command=get4)
    color4.pack(side='left', padx=1)

    colornam5 = '#87843B'

    def get5():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam5)
    color5 = tk.Button(m2, text=colornam5, bg=colornam5,
                       fg=colornam5, height=2, width=7, bd=0, command=get5)
    color5.pack(side='left', padx=1)

    colornam6 = '#9053AD'

    def get6():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam6)
    color6 = tk.Button(m2, text=colornam6, bg=colornam6,
                       fg=colornam6, height=2, width=7, bd=0, command=get6)
    color6.pack(side='left', padx=1)

    colornam7 = '#4D4F36'

    def get7():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam7)
    color7 = tk.Button(m2, text=colornam7, bg=colornam7,
                       fg=colornam7, height=2, width=7, bd=0, command=get7)
    color7.pack(side='left', padx=1)


def lin2(root):
    m2 = tk.Frame(root)
    m2.pack(side='top', padx=10, pady=1)

    colornam1 = 'black'

    def get1():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam1)
    color1 = tk.Button(m2, text=colornam1, bg=colornam1,
                       fg=colornam1, height=2, width=7, bd=0, command=get1)
    color1.pack(side='left', padx=1)

    colornam2 = 'white'

    def get2():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam2)
    color2 = tk.Button(m2, text=colornam2, bg=colornam2,
                       fg=colornam2, height=2, width=7, bd=0, command=get2)
    color2.pack(side='left', padx=1)

    colornam3 = '#AAAAAA'

    def get3():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam3)
    color3 = tk.Button(m2, text=colornam3, bg=colornam3,
                       fg=colornam3, height=2, width=7, bd=0, command=get3)
    color3.pack(side='left', padx=1)

    colornam4 = '#444693'

    def get4():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam4)
    color4 = tk.Button(m2, text=colornam4, bg=colornam4,
                       fg=colornam4, height=2, width=7, bd=0, command=get4)
    color4.pack(side='left', padx=1)

    colornam5 = '#DEAB8A'

    def get5():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam5)
    color5 = tk.Button(m2, text=colornam5, bg=colornam5,
                       fg=colornam5, height=2, width=7, bd=0, command=get5)
    color5.pack(side='left', padx=1)

    colornam6 = '#817936'

    def get6():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam6)
    color6 = tk.Button(m2, text=colornam6, bg=colornam6,
                       fg=colornam6, height=2, width=7, bd=0, command=get6)
    color6.pack(side='left', padx=1)

    colornam7 = '#F7ACBC'

    def get7():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam7)
    color7 = tk.Button(m2, text=colornam7, bg=colornam7,
                       fg=colornam7, height=2, width=7, bd=0, command=get7)
    color7.pack(side='left', padx=1)


def lin1(root):
    m2 = tk.Frame(root)
    m2.pack(side='top', padx=10, pady=1)

    colornam1 = 'red'

    def get1():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam1)
    color1 = tk.Button(m2, text=colornam1, bg=colornam1,
                       fg=colornam1, height=2, width=7, bd=0, command=get1)
    color1.pack(side='left', padx=1)

    colornam2 = 'orange'

    def get2():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam2)
    color2 = tk.Button(m2, text=colornam2, bg=colornam2,
                       fg=colornam2, height=2, width=7, bd=0, command=get2)
    color2.pack(side='left', padx=1)

    colornam3 = 'yellow'

    def get3():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam3)
    color3 = tk.Button(m2, text=colornam3, bg=colornam3,
                       fg=colornam3, height=2, width=7, bd=0, command=get3)
    color3.pack(side='left', padx=1)

    colornam4 = 'green'

    def get4():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam4)
    color4 = tk.Button(m2, text=colornam4, bg=colornam4,
                       fg=colornam4, height=2, width=7, bd=0, command=get4)
    color4.pack(side='left', padx=1)

    colornam5 = '#00FFFF'

    def get5():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam5)
    color5 = tk.Button(m2, text=colornam5, bg=colornam5,
                       fg=colornam5, height=2, width=7, bd=0, command=get5)
    color5.pack(side='left', padx=1)

    colornam6 = 'blue'

    def get6():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam6)
    color6 = tk.Button(m2, text=colornam6, bg=colornam6,
                       fg=colornam6, height=2, width=7, bd=0, command=get6)
    color6.pack(side='left', padx=1)

    colornam7 = 'purple'

    def get7():
        cpk.unpathfilewrite("selectbg.psw", "w", colornam7)
    color7 = tk.Button(m2, text=colornam7, bg=colornam7,
                       fg=colornam7, height=2, width=7, bd=0, command=get7)
    color7.pack(side='left', padx=1)


def asapp():
    root = tk.Toplevel()
    A4 = '#F0F0F0'
    root.wm_attributes("-topmost", True)
    m1 = tk.Frame(root)
    m1.pack(side='top', padx=10, pady=10)
    bottom = tk.Frame(root)
    bottom.pack(side='bottom', padx=1, pady=1)
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    if 800 <= sw <= 1366:
        shd = round(sh*(27/768))
        x = round(sh*(940/768))
    elif 1366 < sw <= 1920:
        shd = round(sh*(22/768))
        x = round(sw*(1000/1366))
    #######################
    swc = round(sh*(120/768))
    shc = round(sh*(120/768))
    y = shd+1
    root.geometry('+%d+%d' % (x, y))
    root['background'] = A4
    root.overrideredirect(True)
    root.attributes('-alpha', 0.9)

    top = tk.Label(root, text="movepoint", bg="#272727",
                   fg='black', height=1, bd=0, font=("微软雅黑", 15))
    top.pack(side='bottom')
    # 窗口移动函数

    def on_move(event):
        root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
        width, height = None, None
        offset_x = event.x_root - root_x
        offset_y = event.y_root - root_y
        if width and height:
            geo_str = "%sx%s+%s+%s" % (width, height,
                                       abs_x + offset_x, abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
            root.geometry(geo_str)

        def _on_tap(event):
            root_x, root_y = event.x_root, event.y_root
            abs_x, abs_y = winfo_x(), winfo_y()
    root.bind('<B1-Motion>', on_move)

    w_box = 40
    h_box = w_box

    def resize(w, h, w_box, h_box, pil_image):  # 主题色图标
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_win11.resize((width, height), Image.ANTIALIAS)
    win11 = tk.Label(m1, text="Taskmgr", width=w_box, height=h_box, bg=A4)
    pil_image_win11 = Image.open(
        './HandrilowOSLauncherCode/H_icon/THEMCOLOR.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='left', padx=2, pady=1)

    name = tk.Label(m1, text="颜色 | 主题色", bg="#F0F0F0",
                    fg='black', height=1, bd=0, font=("微软雅黑", 15))
    name.pack(side='left')
    lin1(root)
    lin2(root)
    lin3(root)
    root.mainloop()


def main():
    root = tk.Toplevel()
    A4 = '#F0F0F0'
    root.wm_attributes("-topmost", True)
    m1 = tk.Frame(root)
    m1.pack(side='top', padx=10, pady=10)

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    if 800 <= sw <= 1366:
        shd = round(sh*(27/768))
        x = round(sh*(0/1366))
    elif 1366 < sw <= 1920:
        shd = round(sh*(22/768))
        x = round(sw*(0/1366))
    #######################
    swc = round(sh*(120/768))
    shc = round(sh*(120/768))
    y = 30
    root.geometry('+%d+%d' % (x, y))
    root['background'] = A4
    root.overrideredirect(True)
    # 窗口移动函数
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def on_move(event):
        offset_x = event.x_root - root_x
        offset_y = event.y_root - root_y
        if width and height:
            geo_str = "%sx%s+%s+%s" % (width, height,
                                       abs_x + offset_x, abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (abs_x + offset_x, abs_y + offset_y)
            root.geometry(geo_str)

        def _on_tap(event):
            root_x, root_y = event.x_root, event.y_root
            abs_x, abs_y = winfo_x(), winfo_y()
    root.bind('<B1-Motion>', on_move)

    def quite():
        root.destroy()
    # 小白条
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2(_):
        cpk.mwoutto(bottomtype, 'bottom', 0, 0, 3)
        quite()
    bottomtype = tk.Label(root, image=photo, bd=0, width=150, height=5)
    bottomtype.bind('<Leave>', jump2)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 3)

    root.attributes('-alpha', 0.9)
    w_box = 50
    h_box = w_box

    def resize(w, h, w_box, h_box, pil_image):  # 主题色图标
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image_win11.resize((width, height), Image.ANTIALIAS)
    win11 = tk.Label(root, text="Taskmgr", width=w_box, height=h_box, bg=A4)
    pil_image_win11 = Image.open(
        './HandrilowOSLauncherCode/H_icon/THEMCOLOR.png')
    w, h = pil_image_win11.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image_win11)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    win11.config(image=tk_image)
    win11.pack(side='bottom', padx=2, pady=1)

    name = tk.Label(root, text="颜色选择 @ Select Color", bg="#F0F0F0",
                    fg='black', height=1, bd=0, font=("微软雅黑", 10))
    name.pack(side='bottom')
    lin1(root)
    lin2(root)
    lin3(root)
    root.mainloop()
