import os
import tkinter as tk
import tkinter.messagebox
import pickle
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import windoweng
import shutil
import time
from shutil import *
from tkinter import filedialog
from HandrilowOSLauncherCode import cpupack as cpk
#import lockscreen


def lock():

    # 窗口
    window = tk.Toplevel()
    window.wm_attributes("-topmost", True)
    cpk.overide(window)

    swc = window.winfo_screenwidth()
    shc = window.winfo_screenheight()
    sw = 300
    sh = 400
    x = (swc-sw)/2
    y = (shc-sh)/2
    cpk.fathersize(window, sw, sh, x, y)
    # 注册函数

    def usr_sign_up():
        # 确认注册时的相应函数
        def usr_sign_quit():
            window_sign_up.destroy()

        def signtowcg():
            # 获取输入框内的内容
            nn = new_name.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()

            # 本地加载已有用户信息,如果没有则已有用户信息为空
            try:
                with open('usr_info.pickle', 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
            if nn in exist_usr_info:
                cpk.message('错误', '用户名已存在')
            elif np == '' or nn == '':
                cpk.message('错误', '用户名或密码为空')
            elif np != npf:
                cpk.message('错误', '密码前后不一致')
            # 注册信息没有问题则将用户名密码写入数据库
            else:
                exist_usr_info[nn] = np
                with open('usr_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    usr_sign_quit()
                cpk.message('欢迎', '注册成功')

        # 新建注册界面
        window_sign_up = tk.Toplevel(window)
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        x = (sw-350)/2
        y = 0
        window_sign_up.geometry('350x170+%d+%d' % (x, y))
        window_sign_up.overrideredirect(True)
        # 用户名变量及标签、输入框
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='用户名：', font=(
            '等线', 10), bd=0).place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
        # 密码变量及标签、输入框
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='请输入密码：', font=(
            '等线', 10), bd=0).place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=new_pwd,
                 show='*').place(x=150, y=50)
        # 重复密码变量及标签、输入框
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='请再次输入密码：',
                 font=('等线', 10), bd=0).place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=new_pwd_confirm,
                 show='*').place(x=150, y=90)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册', font=('等线', 12), bd=0,
                                       command=signtowcg)
        bt_confirm_sign_up.place(x=10, y=130)

        bt_confirm_sign_up = tk.Button(window_sign_up, text='⭕无操作', font=('等线', 10), bd=0,
                                       bg='#DDDDDD', command=usr_sign_quit)
        bt_confirm_sign_up.pack(side='bottom')

    sw = 100
    sh = 100

    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        # 找出最大的边
        mlength1 = min(w, h)
        # 缩放倍数
        mul = sw/mlength
        mul1 = sh/mlength1
        # 重新获得高和宽
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))

    # 退出的函数
    def usr_sign_quite():
        for i in range(-200, 20)[::-1]:
            canvas.place(x=i, y=35)
            canvas.update()
        canvas1 = tk.Canvas(window, height=sh, width=sw, bd=0)
        canvas1.config(highlightthickness=0)
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/unlock.png')
        re_image = resize(image)  # 调用函数
        img = ImageTk.PhotoImage(re_image)
        canvas1.create_image(sw/2, sh/2, anchor='center', image=img)
        for i in range(0, 35):
            canvas1.place(x=20, y=i)
            canvas1.update()
        time.sleep(0.5)
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        window.destroy()

    canvas = tk.Canvas(window, height=sh, width=sw, bd=0)
    canvas.config(highlightthickness=0)
    image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/log.png')
    re_image = resize(image)  # 调用函数
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    cpk.moveinto(canvas, 0, 20, 35)

    b = tk.Button(window, text='登录/注册含昭账号', font=('等线', 15),
                  bd=0, command=usr_sign_up)
    cpk.moveinto(b, 0, 20, 160)

    # 标签 用户名密码
    c = tk.Label(window, text='用户名:', font=('等线', 10))
    cpk.moveinto(c, 0, 20, 200)
    d = tk.Label(window, text='密码:', font=('等线', 10))
    cpk.moveinto(d, 0, 20, 240)

    # 用户名输入框
    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, bd=0)
    cpk.moveinto(entry_usr_name, 60, 80, 200)
    # 密码输入框
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*', bd=0)
    cpk.moveinto(entry_usr_pwd, 60, 80, 240)

    # 登录函数

    def usr():
        # 输入框获取用户名密码
        usr_name = var_usr_name.get()
        with open("usename.psw", "w") as f:
            f.write(usr_name)
        usr_pwd = var_usr_pwd.get()
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        # 判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                usr_sign_quite()
                filejob = open('./HandrilowOSLauncherCode/sys/login.sys', 'w')
                filejob.close()
                pass

            else:
                cpk.message('提示', '密码错误')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            cpk.message('Handrilow', '用户名或密码为空')
        # 不在数据库中弹出是否注册的框

    # 登录 注册按钮

    def relog():
        shutil.rmtree('./HandrilowOSLauncherCode/sys')
        os.mkdir('./HandrilowOSLauncherCode/sys')
        usr_sign_quite()
        lock()

    fileexists1 = os.path.exists("./HandrilowOSLauncherCode/sys/login.sys")
    ###################################
    bt_logup5 = tk.Label(window, text='登录前根据机器类型请正确选择登录方式',
                         bd=0, font=('等线', 10))
    cpk.moveinto(bt_logup5, 0, 20, 340)
    if fileexists1 == True:
        bt_login = tk.Button(
            window, text='关闭', command=usr_sign_quite, bd=0, font=('等线', 12), bg='#DDDDDD')
        cpk.moveinto(bt_login, 0, 20, 290)
    else:
        bt_login = tk.Button(window, text='登录', command=usr,
                             bd=0, font=('等线', 12), bg='#DDDDDD')
        cpk.moveinto(bt_login, 0, 20, 290)
    ####################################
    # 主循环

    def exite():
        window.destroy()
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2():
        cpk.mwoutto(bottomtype, 'bottom', 0, 8, 13)
        exite()

    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 8, 15)
        jump2()

    def mydock(_):
        exite()

    bottomtype = tk.Label(window, image=photo, bd=0, width=150, height=5)
    bottomtype.bind('<Button-1>', mydock)
    bottomtype.bind('<Leave>', jump1)
    # bottomtype.bind('<Enter>',jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 8)
    window.bind('<B1-Motion>', jump1)
    window.mainloop()


def main():
    # 窗口
    window = tk.Toplevel()
    window.wm_attributes("-topmost", True)
    cpk.overide(window)

    swc = window.winfo_screenwidth()
    shc = window.winfo_screenheight()
    fileexists = os.path.exists("./HandrilowOSLauncherCode/sys/lockscreen.sys")
    fileexistsmy = os.path.exists("./HandrilowOSLauncherCode/sys/my.sys")
    fileexistsg = os.path.exists("./HandrilowOSLauncherCode/sys/vation.sys")
    #sw = window.winfo_screenwidth()*(300/1366)
    #sh = window.winfo_screenheight()*(400/768)
    sw = 300
    sh = 400
    x = (swc-sw)/2
    y = (shc-sh)/2
    cpk.fathersize(window, sw, sh, x, y)
    # 注册函数

    def usr_sign_up():
        # 确认注册时的相应函数
        def usr_sign_quit():
            window_sign_up.destroy()

        def signtowcg():
            # 获取输入框内的内容
            nn = new_name.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()

            # 本地加载已有用户信息,如果没有则已有用户信息为空
            try:
                with open('usr_info.pickle', 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
            if nn in exist_usr_info:
                cpk.message('错误', '用户名已存在')
            elif np == '' or nn == '':
                cpk.message('错误', '用户名或密码为空')
            elif np != npf:
                cpk.message('错误', '密码前后不一致')
            # 注册信息没有问题则将用户名密码写入数据库
            else:
                exist_usr_info[nn] = np
                with open('usr_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    usr_sign_quit()
                cpk.pathfilewrite(
                    './HandrilowOSLauncherCode/sys/login.sys', 'w')
                cpk.message('欢迎', '注册成功')

        # 新建注册界面
        window_sign_up = tk.Toplevel(window)
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        x = 0
        y = (sh-170)/2
        window_sign_up.geometry('350x170+%d+%d' % (x, y))
        window.wm_attributes("-topmost", True)
        window_sign_up.overrideredirect(True)
        # 用户名变量及标签、输入框
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='用户名：', font=(
            '等线', 10), bd=0).place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
        # 密码变量及标签、输入框
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='请输入密码：', font=(
            '等线', 10), bd=0).place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=new_pwd,
                 show='*').place(x=150, y=50)
        # 重复密码变量及标签、输入框
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='请再次输入密码：',
                 font=('等线', 10), bd=0).place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=new_pwd_confirm,
                 show='*').place(x=150, y=90)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册', font=('等线', 12), bd=0,
                                       command=signtowcg)
        bt_confirm_sign_up.place(x=10, y=130)

        bt_confirm_sign_up = tk.Button(window_sign_up, text='⭕无操作', font=('等线', 10), bd=0,
                                       bg='#DDDDDD', command=usr_sign_quit)
        bt_confirm_sign_up.pack(side='bottom')

    sw = 100
    sh = 100

    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        # 找出最大的边
        mlength1 = min(w, h)
        # 缩放倍数
        mul = sw/mlength
        mul1 = sh/mlength1
        # 重新获得高和宽
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))
    # 换头像

    def openpicture(_):
        for i in range(-200, 20)[::-1]:
            canvas.place(x=i, y=35)
            canvas.update()
        canvas1 = tk.Canvas(window, height=sh, width=sw, bd=0)
        canvas1.config(highlightthickness=0)
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/sysinfo.png')
        re_image = resize(image)  # 调用函数
        img = ImageTk.PhotoImage(re_image)
        canvas1.create_image(sw/2, sh/2, anchor='center', image=img)
        for i in range(0, 35):
            canvas1.place(x=20, y=i)
            canvas1.update()
        time.sleep(0.5)
        window.destroy()
        global fileindex, fatherpath
        filepath = filedialog.askopenfilename()
        savepath = r'./HandrilowOSLauncherCode/H_icon/H_bg/info.png'
        copy(filepath, savepath)
        cpk.message('提示', '账户头像已更换')

    # 主退出的函数
    def usr_sign_quite():
        for i in range(-200, 20)[::-1]:
            canvas.place(x=i, y=35)
            canvas.update()
        canvas1 = tk.Canvas(window, height=sh, width=sw, bd=0)
        canvas1.config(highlightthickness=0)
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/uninfo.png')
        re_image = resize(image)  # 调用函数
        img = ImageTk.PhotoImage(re_image)
        canvas1.create_image(sw/2, sh/2, anchor='center', image=img)
        if os.path.exists("./HandrilowOSLauncherCode/sys/my.sys") == True:
            os.remove('./HandrilowOSLauncherCode/sys/my.sys')
        else:
            None
        for i in range(0, 35):
            canvas1.place(x=20, y=i)
            canvas1.update()
        time.sleep(0.5)
        cpk.graduallyoutsc(window, 0, 100, 10)
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        window.destroy()
        if os.path.exists("./HandrilowOSLauncherCode/sys/lockscreen.sys") == True:
            os.remove('./HandrilowOSLauncherCode/sys/lockscreen.sys')
            cpk.type()
            cpk.top()
        else:
            None

    def usr_sign_quite1():
        if fileexistsg == True:
            os.remove('./HandrilowOSLauncherCode/sys/vation.sys')
        else:
            None
        for i in range(-200, 20)[::-1]:
            canvas.place(x=i, y=35)
            canvas.update()
        canvas1 = tk.Canvas(window, height=sh, width=sw, bd=0)
        canvas1.config(highlightthickness=0)
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/uninfo.png')
        re_image = resize(image)  # 调用函数
        img = ImageTk.PhotoImage(re_image)
        canvas1.create_image(sw/2, sh/2, anchor='center', image=img)
        for i in range(0, 35):
            canvas1.place(x=20, y=i)
            canvas1.update()
        time.sleep(0.5)
        window.destroy()

    canvas = tk.Canvas(window, height=sh, width=sw, bd=0)
    canvas.config(highlightthickness=0)
    if fileexistsg == True:
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/log.png')
    elif fileexistsg == False:
        image = Image.open('./HandrilowOSLauncherCode/H_icon/H_bg/info.png')
    re_image = resize(image)  # 调用函数
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    fileexists = os.path.exists("./HandrilowOSLauncherCode/sys/lockscreen.sys")
    if fileexists == True:
        None
    else:
        canvas.bind('<Button-3>', openpicture)
    for i in range(0, 20):
        canvas.place(x=i, y=35)
        canvas.update()
    fileexistsname = os.path.exists("./HandrilowOSLauncherCode/sys/login.sys")
    if fileexistsname == False:
        b = tk.Button(window, text='请登录/注册含昭账号',
                      font=('等线', 15), bd=0, command=usr_sign_up)
        for i in range(0, 20):
            b.place(x=i, y=160)
            b.update()
        c = tk.Label(window, text='用户名:', font=('等线', 10))
        for i in range(0, 20):
            c.place(x=i, y=200)
            c.update()
        d = tk.Label(window, text='密码:', font=('等线', 10))
        for i in range(0, 20):
            d.place(x=i, y=240)
            d.update()
        var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(window, textvariable=var_usr_name, bd=0)
        entry_usr_name.place(x=80, y=200)
        # 密码输入框
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(
            window, textvariable=var_usr_pwd, show='*', bd=0)
        entry_usr_pwd.place(x=80, y=240)
        bt_logup5 = tk.Label(
            window, text='登录前根据机器类型请正确选择登录方式', bd=0, font=('等线', 10))
        bt_logup5.place(x=20, y=340)
    else:
        with open("usename.psw", "r") as f:
            d = f.readline()
        b = tk.Button(window, text=d, font=(
            '等线', 20), bd=0, command=usr_sign_up)
        for i in range(0, 20):
            b.place(x=i, y=160)
            b.update()
        c = tk.Label(window)
        if fileexists == True:
            c.config(text=d + '，欢迎回来', font=('等线', 11))
        else:
            c.config(text='Handrilow X CW', font=('等线', 18))
        for i in range(0, 20):
            c.place(x=i, y=220)
            c.update()
        d = tk.Label(window, font=('等线', 10), justify='left')
        if fileexistsname == True:
            d.config(
                text='长安未央版 | 10.0.1 (内部版本2022)\nMID | ASFT-9IHY-64YD-8UY6-UI7D Bate')
        for i in range(0, 20):
            d.place(x=i, y=250)
            d.update()

        bt_logup6 = tk.Label(
            window, text='你的账户已经正确登录 Handrilsoft', bd=0, font=('等线', 10))
        bt_logup6.place(x=20, y=340)
    # 登录函数

    def usr():
        # 输入框获取用户名密码
        usr_name = var_usr_name.get()
        with open("usename.psw", "w") as f:
            f.write(usr_name)
        usr_pwd = var_usr_pwd.get()
        with open("pwd.psw", "w") as f:
            f.write(usr_pwd)
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        # 判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                usr_sign_quite()
                filejob = open('./HandrilowOSLauncherCode/sys/login.sys', 'w')
                filejob.close()
                pass

            else:
                cpk.message('提示', '密码错误')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            cpk.message('Handrilow', '用户名或密码为空')
        # 不在数据库中弹出是否注册的框

    # 登录 注册按钮

    def relog():
        shutil.rmtree('./HandrilowOSLauncherCode/sys')
        os.mkdir('./HandrilowOSLauncherCode/sys')
        usr_sign_quite()
        lock()

    fileexists1 = os.path.exists("./HandrilowOSLauncherCode/sys/login.sys")
    fileexists = os.path.exists("./HandrilowOSLauncherCode/sys/lockscreen.sys")
    fileexistsg = os.path.exists("./HandrilowOSLauncherCode/sys/vation.sys")
    ###################################
    if fileexists1 == True:
        bt_login = tk.Button(
            window, text='关闭', command=usr_sign_quite, bd=0, font=('等线', 12), bg='#DDDDDD')
        for i in range(0, 20):
            bt_login.place(x=i, y=290)
            bt_login.update()
    else:
        bt_login = tk.Button(window, text='登录', command=usr,
                             bd=0, font=('等线', 12), bg='#DDDDDD')
        for i in range(0, 20):
            bt_login.place(x=i, y=290)
            bt_login.update()
    ####################################
    # 主循环

    def exite():
        cpk.unpathfilewrite("toptipMessage.message", "w", " ")
        window.destroy()
    filename = './HandrilowOSLauncherCode/H_icon/H_buttom/APPTYPE.png'
    photo = ImageTk.PhotoImage(file=filename)

    def jump2():
        cpk.mwoutto(bottomtype, 'bottom', 0, 8, 13)
        exite()

    def jump1(_):
        cpk.mwinto(bottomtype, 'bottom', 0, 8, 15)
        jump2()

    def mydock(_):
        exite()

    bottomtype = tk.Label(window, image=photo, bd=0, width=150, height=5)
    bottomtype.bind('<Button-1>', mydock)
    bottomtype.bind('<Leave>', jump1)
    # bottomtype.bind('<Enter>',jump1)
    cpk.mwinto(bottomtype, 'bottom', 0, 0, 8)
    window.bind('<B1-Motion>', jump1)
    window.mainloop()
